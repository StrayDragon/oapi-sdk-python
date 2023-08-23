import dataclasses
from typing import Any, List, Optional, Sequence, Tuple, Dict

from typing_extensions import Literal

from lark_oapi.remaintain.extra.service.sheets.v2 import Service as ExtraSheetsV2Service
from lark_oapi.remaintain.extra.service.sheets.v2 import model as extra_sheets_v2_model
from lark_oapi.remaintain.shortcut.compact import FeishuOpenAPICompactSettings
from lark_oapi.remaintain.shortcut.sheets import utils
from lark_oapi.remaintain.shortcut.sheets.models import SheetRange, CellsRange, CellPos
from lark_oapi.remaintain.shortcut.sheets.models import cell_value_support_data_types


@dataclasses.dataclass
class FeishuSheetsShortcut:
    s: FeishuOpenAPICompactSettings

    extra_sheets_v2_service: ExtraSheetsV2Service = dataclasses.field(init=False)

    def __post_init__(self):
        self.extra_sheets_v2_service = ExtraSheetsV2Service(self.s.remaintain_extra_config)

    def merge_cells(
            self,
            ss_token: str,
            sheet_id: str,
            cr: CellsRange,
            merge_type: Literal["MERGE_ALL", "MERGE_ROWS", "MERGE_COLUMNS"] = "MERGE_ALL",
    ) -> str:
        r = extra_sheets_v2_model
        range_text = f"{sheet_id}!" + cr.to_param_range_pos_part()
        req = r.SpreadsheetsMergeCellsReqBody(
            spreadsheet_token=ss_token,
            range=range_text,
            merge_type=merge_type,
        )
        resp = (
            self.extra_sheets_v2_service.spreadsheetss.merge_cells(
                req,
            )
            .set_spreadsheetToken(
                ss_token,
            )
            .do()
        )
        if resp.code == 0:
            return ""
        return str(resp)

    def unmerge_cells(
            self,
            ss_token: str,
            sr: SheetRange,
    ) -> str:
        r = extra_sheets_v2_model
        range_text = sr.to_param_range()
        req = r.SpreadsheetsUnmergeCellsReqBody(
            range=range_text,
        )
        resp = (
            self.extra_sheets_v2_service.spreadsheetss.unmerge_cells(
                req,
            )
            .set_spreadsheetToken(
                ss_token,
            )
            .do()
        )
        if resp.code == 0:
            return ""
        return str(resp)

    def prepend_insert_values(
            self,
            ss_token: str,
            sheet_id: str,
            cr: CellsRange,
            values: Sequence[Sequence[Any]],
            headers: Sequence[Any] = (),
    ) -> str:
        if not values:
            return "not sheet"
        converted_values = []
        n_max_cols = 0
        n_rows = 0
        _headers = list(headers)
        if _headers:
            converted_values.append(_headers)
            n_rows += 1
        for row in values:
            n_max_cols = max(n_max_cols, len(row))
            converted_values.append(list(row))
            n_rows += 1
        if not cr.start_pos:
            cr.start_pos = CellPos(x="A", y=1)
        if not cr.end_pos:
            cr.end_pos = CellPos(x="")
        cr.end_pos.x = cr.end_pos.x or utils.column_number_to_name(n_max_cols)
        cr.end_pos.y = cr.end_pos.y or (n_rows + cr.start_pos.y)
        range_text = f"{sheet_id}!" + cr.to_param_range_pos_part()
        resp = (
            self.extra_sheets_v2_service.spreadsheetss.values_prepend(
                extra_sheets_v2_model.SpreadsheetsValuesPrependReqBody(
                    value_range=extra_sheets_v2_model.ValueRange(
                        range=range_text,
                        values=converted_values,
                    )
                )
            )
            .set_spreadsheetToken(ss_token)
            .do()
        )
        if resp.code == 0:
            return ""
        return str(resp)

    def batch_update_values(
            self,
            ss_token: str,
            sheet_id: str,
            cr_values: List[Tuple[CellsRange, Sequence[Sequence[Any]]]],
    ):
        if not cr_values:
            return "empty input"
        value_ranges = []
        for cr, values in cr_values:
            converted_values = []
            n_max_cols = 0
            n_rows = 0
            for row in values:
                n_max_cols = max(n_max_cols, len(row))
                converted_values.append(list(row))
                n_rows += 1
            if not cr.start_pos:
                cr.start_pos = CellPos(x="A", y=1)
            if not cr.end_pos:
                cr.end_pos = CellPos(x="")
            cr.end_pos.x = cr.end_pos.x or utils.column_number_to_name(n_max_cols)
            cr.end_pos.y = cr.end_pos.y or (n_rows + cr.start_pos.y)
            range_text = f"{sheet_id}!" + cr.to_param_range_pos_part()
            value_ranges.append(
                extra_sheets_v2_model.ValueRange(
                    range=range_text,
                    values=converted_values,
                ),
            )
        resp = (
            self.extra_sheets_v2_service.spreadsheetss.values_batch_update(
                extra_sheets_v2_model.SpreadsheetsValuesBatchUpdateReqBody(
                    value_ranges=value_ranges,
                )
            )
            .set_spreadsheetToken(ss_token)
            .do()
        )
        if resp.code == 0:
            return ""
        return str(resp)

    def batch_read_values(
            self,
            ss_token: str,
            sheet_id: str,
            crs: List[CellsRange],
            value_render_option: Literal["ToString", "FormattedValue", "Formula", "UnformattedValue"] = "ToString",
            date_time_render_option: str = "FormattedString",
    ) -> Tuple[Dict[str, List[list]], str]:
        if not crs:
            return {}, "empty input"
        range_texts = ",".join([f"{sheet_id}!" + cr.to_param_range_pos_part() for cr in crs])
        resp = (
            self.extra_sheets_v2_service.spreadsheetss.values_batch_get()
            .set_spreadsheetToken(ss_token)
            .set_ranges(range_texts)
            .set_valueRenderOption(value_render_option)
            .set_dateTimeRenderOption(date_time_render_option)
            .do()
        )
        if resp.code != 0:
            return {}, str(resp)
        range_cr__values = {}
        for vr in resp.data.value_ranges:
            range_cr__values[SheetRange.from_literal(vr.range).to_param_range_pos_part()] = vr.values
        return range_cr__values, ""

    def update_formula_value_cell(
            self,
            ss_token: str,
            sheet_id: str,
            formula_text: str,
            result_cell_pos: CellPos,
            auto_merge_cells_range: Optional[CellsRange] = None,
    ):
        values = [
            [
                cell_value_support_data_types.Formula(text=formula_text).dict(),
            ]
        ]
        op__err_msg = {}
        op__err_msg["insert_formula_value"] = self.batch_update_values(
            ss_token=ss_token,
            sheet_id=sheet_id,
            cr_values=[
                (CellsRange(start_pos=result_cell_pos, end_pos=result_cell_pos), values),
            ],
        )
        if auto_merge_cells_range and not op__err_msg["insert_formula_value"]:
            op__err_msg["merge_cells"] = self.merge_cells(
                ss_token=ss_token,
                sheet_id=sheet_id,
                cr=auto_merge_cells_range,
            )
        return op__err_msg

    def update_formula_value_cell_using_sum_of_cell_range(
            self,
            ss_token: str,
            sheet_id: str,
            target_cells_range: CellsRange,
            result_cell_pos: CellPos,
            auto_merge_cells_range: Optional[CellsRange] = None,
    ):
        return self.update_formula_value_cell(
            ss_token=ss_token,
            sheet_id=sheet_id,
            formula_text=f"=SUM({target_cells_range.to_param_range_pos_part()})",
            result_cell_pos=result_cell_pos,
            auto_merge_cells_range=auto_merge_cells_range,
        )

    def insert_dimension(
            self,
            ss_token: str,
            sheet_id: str,
            dimension: Literal["ROWS", "COLUMNS"] = "ROWS",
            start_index=0,
            end_index=1,
            inherit_style=None,
    ):
        resp = (
            self.extra_sheets_v2_service.spreadsheetss.insert_dimension_range(
                extra_sheets_v2_model.SpreadsheetsInsertDimensionRangeReqBody(
                    dimension=extra_sheets_v2_model.Dimension(
                        sheet_id=sheet_id,
                        major_dimension=dimension,
                        start_index=start_index,
                        end_index=end_index,
                    ),
                    inherit_style=inherit_style,
                )
            )
            .set_spreadsheetToken(
                ss_token,
            )
            .do()
        )
        if resp.code == 0:
            return ""
        return str(resp)

    def delete_dimension(
            self,
            ss_token: str,
            sheet_id: str,
            dimension: Literal["ROWS", "COLUMNS"] = "ROWS",
            start_index=1,
            end_index=1,
    ):
        resp = (
            self.extra_sheets_v2_service.spreadsheetss.dimension_range_delete(
                extra_sheets_v2_model.SpreadsheetsDimensionRangeDeleteReqBody(
                    dimension=extra_sheets_v2_model.Dimension(
                        sheet_id=sheet_id,
                        major_dimension=dimension,
                        start_index=start_index,
                        end_index=end_index,
                    ),
                )
            )
            .set_spreadsheetToken(
                ss_token,
            )
            .do()
        )
        if resp.code == 0:
            return ""
        return str(resp)
