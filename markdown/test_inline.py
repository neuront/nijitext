import inline

from test_common import assert_eq, assert_ne
from nijiconf import MONO_BEGIN, MONO_END
from nijiconf import BOLD_BEGIN, BOLD_END
from nijiconf import ITALIC_BEGIN, ITALIC_END
from nijiconf import STROKE_BEGIN, STROKE_END
from nijiconf import LINK_BEGIN, LINK_END
from nijiconf import SUP_BEGIN, SUP_END
from nijiconf import SUB_BEGIN, SUB_END
from nijiconf import IMAGE

assert_eq('', inline.forge(''))

text = 'i want a ``**inline** code`` as'
esc_text = ('i want a ' + MONO_BEGIN + BOLD_BEGIN + 'inline' + BOLD_END
          + ' code' + MONO_END + ' as')

text = '@@http://www.google.com/@Google@@'
esc_text = LINK_BEGIN % 'http://www.google.com/' + 'Google' + LINK_END
assert_eq(esc_text, inline.forge(text))

text = '@@http://www.google.com/@Goo@gle@@'
esc_text = LINK_BEGIN % 'http://www.google.com/' + 'Goo@gle' + LINK_END
assert_eq(esc_text, inline.forge(text))

text = '@@http://www.google.com/ @Goo@gle@@'
esc_text = LINK_BEGIN % 'http://www.google.com/ ' + 'Goo@gle' + LINK_END
assert_ne(esc_text, inline.forge(text))

text = '@@http://example.com/#123@Example@@f(x)=a,,1,,^^2^^+a,,0,,'
esc_text = (LINK_BEGIN % 'http://example.com/#123' + 'Example' + LINK_END
          + 'f(x)=a' + SUB_BEGIN + '1' + SUB_END + SUP_BEGIN + '2' + SUP_END
          + '+a' + SUB_BEGIN + '0' + SUB_END)
assert_eq(esc_text, inline.forge(text))

text = 'this is an `\\`escaped`\\` tag. another *\\*escaped** tag.'
esc_text = 'this is an ``escaped`` tag. another **escaped** tag.'
assert_eq(esc_text, inline.forge(text))

text = '\\-\\`\\@\\#\\$\\%\\^\\&\\*\\(\\)\\[\\]\\{\\}=\\:\\;\\,\\/\\|\\\\'
esc_text = '-`@#$%^&*()[]{}=:;,/|\\'
assert_eq(esc_text, inline.forge(text))

text = 'escaping an\\y character\\s even \\\\.'
esc_text = 'escaping an\\y character\\s even \\.'
assert_eq(esc_text, inline.forge(text))

imgurl = 'http://upload.wikimedia.org/wikipedia/commons/6/63/Wikipedia-logo.png'
text = 'Insert an image [[img ' + imgurl + ']] here'
esc_text = 'Insert an image ' + IMAGE % imgurl + ' here'
assert_eq(esc_text, inline.forge(text))

text = 'Insert an image [[img ' + imgurl + ' ]] here'
esc_text = 'Insert an image ' + IMAGE % imgurl + ' here'
assert_eq(esc_text, inline.forge(text))

text = '///italic/font///'
esc_text = ITALIC_BEGIN + 'italic/font' + ITALIC_END
assert_eq(esc_text, inline.forge(text))

text = '--stroke-font--'
esc_text = STROKE_BEGIN + 'stroke-font' + STROKE_END
assert_eq(esc_text, inline.forge(text))
