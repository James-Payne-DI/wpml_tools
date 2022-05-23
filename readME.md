WPML TOOL: Spanish sitemap to CSV
------------
- created as an easy to use GUI, three input fields and two buttons, that's it!
Inputs:
- Spanish language sitemap - i.e. /es/mapa-del-sitio/
- Name of the dealership
- a file path for the place you want the csv file to save to

Outputs:
- outputs a CSV file that can be easily exported to other platforms


____________
Tool Installation:
------------
Python Version: Python 3.7.3
- Link: https://www.python.org/downloads/release/python-373/
- Download file name: "macOS 64-bit installer"


Python Modules used: bs4,requests, time, urllib3, csv, os
Terminal Commands:
- pip3 install bs4
- pip3 install requests
- pip3 install time
- pip3 install urllib3
- pip3 install csv
- pip3 install os


____________
Error Log:
------------
KNOWN ERRORS: The below errors may appear in the CSV file after the program finishes running, please refer to the below definitions to know what they mean:
- urlError01: issue with acquiring the Spanish URL from the /es/ sitemap
- urlError02: unable to find the multilingual toggle CTA while on the /es/ page
- titleError01: unable to find the English page title while on  the page


____________
To Do List:
------------
- Add progress bar to let the user know how far the program has gone
- Add input fields to help the user save the csv file with the use of the executable

