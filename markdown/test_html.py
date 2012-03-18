import html

from test_common import assert_eq
import nijiconf

assert_eq('', html.forge(''))

text = '&nbsp;'
esc_text = nijiconf.AND + 'nbsp;'
assert_eq(esc_text, html.forge(text))

text = '&<>  "'
esc_text = nijiconf.AND + nijiconf.LT + nijiconf.GT + '  ' + nijiconf.DQUOT
assert_eq(esc_text, html.forge(text))

text = '''    "'"'''
esc_text = nijiconf.SPACE * 4 + nijiconf.DQUOT + nijiconf.SQUOT + nijiconf.DQUOT
assert_eq(esc_text, html.forge(text))

text = '''  ...<<... ----'''
esc_text = (nijiconf.SPACE * 2 + '...' + nijiconf.LT * 2 + '...' + ' '
          + nijiconf.MINUS * 3 + '-')
assert_eq(esc_text, html.forge(text))
