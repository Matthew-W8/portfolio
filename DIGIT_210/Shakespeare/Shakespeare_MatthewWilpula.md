# Shakespeare steps

&
<
>
[\D\d\s]+
    <xml>\0<xml>
[IVXLC]+$
    <sonnet number="\0">
^.+[\n]
    <line>\0</line>
<line>  (<sonnet number="[IVXLC]+">\n)</line>
      \1
 (</line>\n)(  <son)
    \1</sonnet>\2
I had to manually change the <line> around <xml> because I forgot and add the last sonnet tag.