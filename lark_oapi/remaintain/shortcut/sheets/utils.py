def column_number_to_name(n: int) -> str:
    """
    根据表格的列索引获取列名，从 0 开始
    比如 0 -> A, 1 -> B, 26 -> AA, 27 -> AB
    """
    d, m = divmod(n, 26)
    return '' if n < 0 else column_number_to_name(d - 1) + chr(m + 65)  # chr(65) = 'A'
