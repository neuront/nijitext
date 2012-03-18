import table

from test_common import assert_eq
import nijiconf
import nijierr

text = '||cell1||cell2||cell3||'
esc_text = ((nijiconf.CELL_BEGIN % ('', 'cell1')) + nijiconf.CELL_END
          + (nijiconf.CELL_BEGIN % ('', 'cell2')) + nijiconf.CELL_END
          + (nijiconf.CELL_BEGIN % ('', 'cell3')) + nijiconf.CELL_END
          + (nijiconf.CELL_BEGIN % ('', '')) + nijiconf.CELL_END)
assert_eq(esc_text, table.row_extract(text))

text = '||cell||;hc;attr-cell'
esc_text = ((nijiconf.CELL_BEGIN % ('', 'cell')) + nijiconf.CELL_END
          + (nijiconf.CELL_BEGIN % (nijiconf.CELL_HORI_ALGN
                                  % nijiconf.CELL_HORI_ALIGNMENT_MAP['c']
                                 , 'attr-cell')) + nijiconf.CELL_END)
assert_eq(esc_text, table.row_extract(text))

text = '||n;htr2||no attr cell'
esc_text = ((nijiconf.CELL_BEGIN % ('', 'n;htr2')) + nijiconf.CELL_END
          + (nijiconf.CELL_BEGIN % ('', 'no attr cell')) + nijiconf.CELL_END)
assert_eq(esc_text, table.row_extract(text))

text = '|only one||| three lines||;another cell'
esc_text = ('|only one'
          + (nijiconf.CELL_BEGIN % ('', '| three lines')) + nijiconf.CELL_END
          + (nijiconf.CELL_BEGIN % ('', ';another cell')) + nijiconf.CELL_END)
assert_eq(esc_text, table.row_extract(text))

text = '||;hlvtr1;c3||;hrvbc3;r1'
esc_text = ((nijiconf.CELL_BEGIN % (nijiconf.CELL_HORI_ALGN
                                  % nijiconf.CELL_HORI_ALIGNMENT_MAP['l']
                                  + nijiconf.CELL_VERT_ALGN
                                  % nijiconf.CELL_VERT_ALIGNMENT_MAP['t']
                                  + nijiconf.CELL_ROW_SPAN % '1'
                                 , 'c3')) + nijiconf.CELL_END
          + (nijiconf.CELL_BEGIN % (nijiconf.CELL_HORI_ALGN
                                  % nijiconf.CELL_HORI_ALIGNMENT_MAP['r']
                                  + nijiconf.CELL_VERT_ALGN
                                  % nijiconf.CELL_VERT_ALIGNMENT_MAP['b']
                                  + nijiconf.CELL_COL_SPAN % '3'
                                 , 'r1')) + nijiconf.CELL_END)
assert_eq(esc_text, table.row_extract(text))

try:
    table.row_extract('||;ht;')
    raise AssertionError('Expected exception not raised')
except nijierr.ParseError, pe:
    assert_eq(nijierr.MSG_CELL_ATTR_ERROR + 'ht', pe.message)

try:
    table.row_extract('||;tr;')
    raise AssertionError('Expected exception not raised')
except nijierr.ParseError, pe:
    assert_eq(nijierr.MSG_CELL_ATTR_ERROR + 'tr', pe.message)
