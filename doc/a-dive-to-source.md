= A Dive to the Source Code in Markdown Lexical Part
    Since NijiPress convert markdown content to HTML, basic knowledge about HTML or even CSS is nececcary. All HTML tags, tag attributes, character escaping, and some program logic like maps from markdown tag to HTML table cell attributes could be found in the python file ``**markdown/nijiconf.py**``.
    If you want to change the style of the output HTML, a simple approach is to directly modify the values of the tags in ``nijiconf.py``. For example, changing ``LINK_BEGIN`` to ``<a href='%s' style='color: navy;'>`` would color all links in navy.

    The entry for markdown parsing is ``forge`` in ``markdown/entire_doc.py``. At first, it will truncate padding spaces for all lines, then split the document into paragraphs.
    In ``markdown/paragraph.py`` there are various types of paragraphs, and the function ``splitDocument``, which is used to break the whole document into smaller parts (called paragraph) according to the markdown tags.
    The ``LINE_PATTERNS`` tuples is the very core structures for splitting the document. Each tuple contains the beginning pattern of a paragraph, then ending pattern of the paragraph, and what type it is, and finally pattern exclusion. Pattern exclusion means whether the beginning and ending parts should be excluded from the paragraph content. For example, a block of codes begin with ``{{{`` and end up with ``}}}``, but these two are not parts of the codes, they should not be displayed; while for bullets, its pattern is a line having an asterisk as line beginning, so this line itself is a bullet item.
    Each paragraph has a ``build`` function, which is discouraged to be overloaded in sub classes. This function returns a list of strings, including a **head** part, a **tail** part, and the content of the paragraph. By default the ``head`` and ``tail`` functions do nothing. In those paragraph that needs HTML tags around the content, these two functions are useful. For example a HTML table needs ``<table>`` at the beginning and ``</table>`` at the end, overloads for these functions could be helpful.
    The content of a paragraph is the result that the original content tranformed by a order-sensitive list of **``modifiers``**. A modifier is a function that substitutes certain patterns in text. The basic modifiers in NijiPress are in ``markdown/html.py`` (for HTML character escaping), ``markdown/inline.py`` (for inline patterns), and ``markdown/table.py`` (for HTML cell attributes).

    Generally, NijiPress will not report lexical error or begin-end patterns mismatch, and those mistakes will probably be displayed as normal content, except in the ``table.py`` an ``ParseError`` (defined in ``markdown/nijierr.py``) will be thrown if the cell attributes is invalid.