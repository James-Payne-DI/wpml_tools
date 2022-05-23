WPML TOOL: Spanish sitemap to CSV
- created as an easy to use GUI, one input field and two buttons, that's it!
- takes the spanish language sitemap as an input
---> slug should start with /es/
- outputs a CSV file that can be easily exported to other platforms


Tool Installation:
____________
Python Version: Python 3.7.3
- Link: https://www.python.org/downloads/release/python-373/
- Download file name: "macOS 64-bit installer"

____________
Python Modules used: bs4,requests, time, urllib3, csv, os
Terminal Commands:
pip3 install bs4
pip3 install requests
pip3 install time
pip3 install urllib3
pip3 install csv
pip3 install os



Error Log:
____________
KNOWN ERRORS: The below errors may appear in the CSV file after the program finishes running, please refer to the below definitions to know what they mean:
- urlError01: issue with acquiring the Spanish URL from the /es/ sitemap
- urlError02: unable to find the multilingual toggle CTA while on the /es/ page
- titleError01: unable to find the English page title while on  the page