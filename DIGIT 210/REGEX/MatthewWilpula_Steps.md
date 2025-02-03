# Steps for Regular Expressions

"&" - Already Changed
"<" - Showing ones on the xml
">" - Showing ones on the xml
(<movie>)(\D* \d+) - This gave me all titles that ended in a number, which I mistakenly thought was every title.
    -Replace with \1<title>\2<\title>
(<movie>)(\D*) - This gave me the all the titles without a number
    -\1<title>\2</title> -The only problem is it still grabbed the tabs.
(<movie>)(\D+\d+\t) - This gives me all the titles and the year it came out. I don't understand why though, because shouldn't the tab be stopping it?


