# Blithedale Steps

'&'
'<'
'>'

'\D*\d*'
    '<xml>\0</xml>'

'\s+([IVX]+.  [\w\ \'\-\,]+)(\n)'
    '<title>\1</title>\n'

'^([IVX]+. [\w\ \'\-\,]+)(\n)'
    <chapter>\n<title>\1</title>

'<chapter>'
    '</chapter>\0'

'(</title>\n)(\w)'
    '\1<p>\2'

'\n\n'
    </p>\n\n<p>

'"([\w+\s*\,*\'*.*?*!*--*]+)"'
    '<quote>\1</quote>'

<p>(</cha)
    \1

'</chapter><chapter>\n<title>(I[n|t])'
    '<p>\1'

'</title>\w'
    Replaced with nothing

'<p></p>'
    Replaced with nothing


