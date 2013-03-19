import entire_doc

from test_common import assert_list_eq
import nijiconf

assert_list_eq([
    nijiconf.SPACE + '{{{' + nijiconf.BR,
    nijiconf.MONO_BLOCK_BEGIN % '',
    nijiconf.BOLD_BEGIN + 'print' + nijiconf.BOLD_END + ' ' + nijiconf.DQUOT +
        'hello, world' + nijiconf.DQUOT + nijiconf.BR,
    nijiconf.MONO_BLOCK_END,
], entire_doc.forge([
    ' {{{',
    '{{{',
    '**print** "hello, world"',
    '}}}',
]))

assert_list_eq([
    nijiconf.MONO_BLOCK_BEGIN % ' lang-python',
    nijiconf.BOLD_BEGIN + 'print' + nijiconf.BOLD_END + ' ' + nijiconf.DQUOT +
        'hello, world' + nijiconf.DQUOT + nijiconf.BR,
    nijiconf.MONO_BLOCK_END,
], entire_doc.forge([
    '{{{ python',
    '**print** "hello, world"',
    '}}}',
]))
