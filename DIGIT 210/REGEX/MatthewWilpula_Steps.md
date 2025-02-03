# Steps for Regular Expressions

"&" - Already Changed
"<" - Showing ones on the xml
">" - Showing ones on the xml
(<movie>)(\D* \d+) - This gave me all titles that ended in a number, which I mistakenly thought was every title.
    -Replace with \1<title>\2<\title>
(<movie>)(\D*) - This gave me the all the titles without a number
    -\1<title>\2</title> -The only problem is it still grabbed the tabs.
(<movie>)(\D+\d+\t) - This gives me all the titles and the year it came out. I don't understand why though, because shouldn't the tab be stopping it?

(<movie>)(.+\t)
    \0<duration>
I forgot to record the step in between, but I looked for the "<duration>" marks and added unit="min" to it.
(<duration unit="min">)(\d+)(\s\w+)
    \1\2

Also, I figured out what the problem is I just have no idea how to search for it. 	 <- This isn't a tab, but I don't know/remember what it's called
so I don't know what to look up to search for the regular expression that would let me search for it and then just use that as a stop with
(.+) to grab everything before it, then just work up from there moving along each xml mark.


