import entire_doc

from test_common import assert_eq, assert_list_eq
import nijiconf

assert_eq([], entire_doc.forge([]))
assert_eq([nijiconf.BR], entire_doc.forge(['']))

assert_list_eq([
    'A' + nijiconf.BR,
    nijiconf.MONO_BLOCK_BEGIN,
    '$ this' + nijiconf.BOLD_BEGIN + 'mono' + nijiconf.BOLD_END + 'line' + nijiconf.BR,
    'another' + nijiconf.BOLD_BEGIN + 'mono' + nijiconf.BOLD_END + 'line' + nijiconf.BR,
    nijiconf.MONO_BLOCK_END,
    nijiconf.TABLE_BEGIN,
    nijiconf.ROW_BEGIN +
        (nijiconf.CELL_BEGIN % ('', ' table')) +
        nijiconf.CELL_END + (nijiconf.CELL_BEGIN % ('', 'in')) +
        nijiconf.CELL_END + nijiconf.ROW_END,
    nijiconf.ROW_BEGIN +
        (nijiconf.CELL_BEGIN % ((nijiconf.CELL_ROW_SPAN % '2'), 'it')) +
        nijiconf.CELL_END + nijiconf.ROW_END,
    nijiconf.TABLE_END,
], entire_doc.forge([
    'A',
    '{{{',
    '$ this**mono**line',
    'another**mono**line',
    '}}}',
    '[[[',
    '|| table||in',
    '||;r2;it',
    ']]]',
]))

assert_list_eq([
    'A' + nijiconf.BR,
    nijiconf.UL_BEGIN,
    nijiconf.LI_BEGIN + 'this bullet' + nijiconf.LI_END,
    nijiconf.LI_BEGIN + 'another bullet' + nijiconf.LI_END,
    nijiconf.UL_END,
    '*not a bullet' + nijiconf.BR,
    'end' + nijiconf.BR,
], entire_doc.forge([
    'A',
    '* this bullet',
    '* another bullet',
    '*not a bullet',
    'end',
]))

assert_list_eq([
    nijiconf.UL_BEGIN,
    nijiconf.LI_BEGIN + 'this bullet' + nijiconf.LI_END,
    nijiconf.UL_END,
    nijiconf.MONO_BLOCK_BEGIN,
    'end' + nijiconf.BR,
    nijiconf.MONO_BLOCK_END,
], entire_doc.forge([
    '* this bullet',
    '{{{',
    'end',
    '}}}',
]))

assert_list_eq([
    nijiconf.H1_BEGIN + 'this title1' + nijiconf.H1_END,
    nijiconf.H2_BEGIN + 'title2' + nijiconf.BOLD_BEGIN + 'bol' +
        nijiconf.BOLD_END + 'd' + nijiconf.H2_END,
    nijiconf.H3_BEGIN + 'title3' + nijiconf.MONO_BEGIN + 'monospace' +
        nijiconf.MONO_END + nijiconf.H3_END,
    '=not-a-title' + nijiconf.BR,
    nijiconf.SPACE + '== yet-not-a-title' + nijiconf.BR,
], entire_doc.forge([
    '= this title1',
    '== title2**bol**d',
    '=== title3``monospace``',
    '=not-a-title',
    ' == yet-not-a-title',
]))

assert_list_eq([
    nijiconf.STROKE_BEGIN + 'stroke' + nijiconf.MINUS * 3 + '-' + 'font' +
        nijiconf.STROKE_END + nijiconf.BR,
    nijiconf.STROKE_BEGIN + 'stroke font' + nijiconf.STROKE_END + nijiconf.BR,
], entire_doc.forge([
    '--stroke----font--',
    '--stroke font--',
]))
