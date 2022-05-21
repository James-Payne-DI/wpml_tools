WPML TOOL: Spanish sitemap to CSV
- created as an easy to use GUI, one input field and two buttons, that's it!
- takes the spanish language sitemap as an input
---> slug should start with /es/
- outputs a CSV file that can be easily exported to other platforms


____________
Python Modules used:
bs4,requests, time, urllib3, csv, os

____________
KNOWN ERRORS:
- urlError01: issue with acquiring the Spanish URL from the /es/ sitemap
- urlError02: unable to find the multilingual toggle CTA while on the /es/ page
- titleError01: unable to find the English page title while on  the page