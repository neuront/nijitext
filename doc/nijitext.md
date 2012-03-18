= NijiText
NijiText is the markdown parsing module in nijipress. This document will tell what NijiText supports.
== Inline Conversions
=== Hyperlink:
@\@http://example.org/@Example@\@ ==> @@http://example.org/@Example@@
Lexical rule is **@\@ Link @ Text @\@**, where **Link** is the URL linked to, and **Text** is what will be shown.
=== Strengthen
To show text in **strong** tag, put the text in double asterisks:
*\*text will be strong*\* ==> **text will be strong**
=== Italic
To show text in **i** tag, put the text in triple slashes:
/\/text will be italic/\/ ==> //text will be italic//

Not using double slashes but triple slashes because some programming language uses double slash for comments beginning.
=== Stroke
To show text in **s** tag, put the text in double minuses:
-\-text will be stroke-\- ==> --text will be stroke--
=== Inline code (monospace):
To show text in **tt** tag, put the text in double quotes (the key for this quote is at the left of the key for num "1" in keyboard main section):
\`\`text will be show in monospace\`\` ==> ``text will be show in monospace``
=== Superscript and subscript
Put text in **sub** or **sup** tag.
,\,subscript,\, ==> ,\,subscript,\,
^\^superscript^\^ ==> ^\^superscript^\^
a,\,2,\,x^\^2^\^+a,\,1,\,x+a,\,0,\,=0 ==> a,,2,,x^^2^^+a,,1,,x+a,,0,,=0
== Escaping
A backslash will help escape following characters: \`\@\#\$\%\^\&\*\(\)\[\]\{\}\=\:\;\,\/\|\\

double asterisks *\\* not convert to bold *\\*
a backslash type \\\\ to make it
{\\{{
and braces
}}\\}

will be convert to

double asterisks *\* not convert to bold *\*
a backslash type \\ to make it
{\{{
and braces
}}\}
== Headings
If a line begins with the equal sign(s) and a space, it will be converted to a heading.
\= Heading 1
\== Heading 2
\=== Heading 3
The number of equal signs determines what heading it is. Though HTML support up to level 6, NijiText support up to level 3 only.
== Block Code Conversion
Put lines in **tt** tag. Block codes begins with a line with only **{{{** and end with a line with only **}}}**. For example,

{\{{
code line 0
code line 1
}\}}

will be converted as
{{{
code line 0
code line 1
}}}
== ASCII Art
If a line begins with an colon and a space, it will be converted to ASCII art line.
: : .  |
: : |\ |
: : | \|
: : |  `
will be converted to
: .  |
: |\ |
: | \|
: |  `
The characters in ASCII art will be displayed in monospace. The difference between block code and ASCII art is that latter will not do inline convertion, like hyperlinks and character escaping backslash. Only HTML character escaping will be performed to the content, and all spaces will be converted to ``&nbsp``.
== Table Conversion
Tables begins with a line with only **[[[**, and end with a line with only **]]]**. Here is examples.
General table:

[\[[
|\|cell content|\|another cell
|\|row2|\|...
]\]]

will be converted to
[[[
||cell content||another cell
||row2||...
]]]
Table containing cells with attributes:

[\[[
|\|**;htr2;**hori-align is top and row span is 2
|\|row 2|\|...
]\]]

will be converted to
[[[
||;hcc2;hori-align is top and row span is 2
||row 2||...
]]]
Notice that **;hcr2;** is description of the cell. A semicolon (;) is the beginning of cell attributes, then **hc** means **Hori-align** is **center** and **c2** means **Col span** is **2**, then followed by another semicolon which means the ending of cell attributes.

More about cell attributes:
{{{
Semicolon ( Attribute )+ Semicolon CellContent
Attribute: AttributeTag AttributeValue
AttributeTag: c|r|h|v
}}}
Note ``AttributeTag`` is case-sensitive.
When ``AttributeTag`` is ``c`` or ``r``, ``AttributeValue`` could be number 2-9, indicating the columns or rows span count;
When ``AttributeTag`` is ``h``, ``AttributeValue`` could be ``l`` (left align), ``r`` (right align), ``j`` (justified) or ``c`` (center align);
When ``AttributeTag`` is ``v``, ``AttributeValue`` could be ``t`` (top align), ``b`` (bottom align), ``m`` (middle) or ``l`` (base line).

More example:
``||;r2ht;cell content`` this is the same as ``||;htr2;cell content``, a cell that spans 2 rows, top aligned horizontally with content as "cell content", say, attributes order doesn't matter;
``||;c3r2hjvm;kagami sama`` this is a cell that spans 2 rows and 3 columns (**c3** attribute), justified horizontally (**hj**), middle align vertically, with content as "kagami sama".
== Unordered List
If a line begins with an asterisk and a space, it will be converted to a list item.

\* this is a bullet
\* this is another bullet

will be converted to
* this is a bullet
* this is another bullet
= More Details About NijiText
Please read this @@a-dive-to-source.html@documentation@@ for markdown parsing source code.
