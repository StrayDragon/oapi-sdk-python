import pytest

from lark_oapi.remaintain.shortcut.sheets import CellPos


@pytest.fixture(autouse=True)
def hooks():
    # before
    yield
    # after


class Test__prepend_insert_values:
    def test_default(self, fss, fss_ss):
        headers = ["num1", "数字2", "num三"]
        fss.prepend_insert_values(
            ss_token=fss_ss.ss_token,
            sheet_id=fss_ss.sheet_id,
            values=[
                [1, "2", 3.0],
                [4, "5", 6],
                [7.0, "8", 9],
            ],
            headers=headers,
        )

        fss.update_formula_value_cell(
            formula_text="=SUM(A:C)",
            result_cell_pos=CellPos.from_literal("D1"),
            **fss_ss.dict()
        )
