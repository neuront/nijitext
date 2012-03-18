import entire_doc

from test_common import assert_list_eq
import nijiconf

assert_list_eq([
    nijiconf.SPACE + ': iii' + nijiconf.BR,
    ':iii' + nijiconf.BR,
    nijiconf.AA_BEGIN,
    '``not' + nijiconf.SPACE + 'code``' + nijiconf.BR,
    'just' + nijiconf.SPACE + '**aa**' + nijiconf.BR,
    nijiconf.AA_END,
    ': not ' + nijiconf.BOLD_BEGIN + 'aa' + nijiconf.BOLD_END + nijiconf.BR,
], entire_doc.forge([
    ' : iii',
    ':iii',
    ': ``not code``',
    ': just **aa**',
    '\\: not **aa**',
]))

assert_list_eq([
    nijiconf.AA_BEGIN,
    nijiconf.BR,
    'just' + nijiconf.SPACE + '**aa**' + nijiconf.BR,
    nijiconf.AA_END,
], entire_doc.forge([
    ':',
    ': just **aa**',
]))

assert_list_eq([
    nijiconf.AA_BEGIN,
    nijiconf.BR,
    'just' + nijiconf.SPACE + '**aa**' + nijiconf.BR,
    nijiconf.AA_END,
], entire_doc.forge([
    ': ',
    ': just **aa**',
]))

assert_list_eq([
    nijiconf.AA_BEGIN,
    'iii' + nijiconf.BR,
    nijiconf.BR,
    'just' + nijiconf.SPACE + '**aa**' + nijiconf.BR,
    nijiconf.BR,
    nijiconf.AA_END,
], entire_doc.forge([
    ': iii',
    ':',
    ': just **aa**',
    ': ',
]))
