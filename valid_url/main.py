from valid_url import check_link, read_urls
from xml.dom.minidom import parseString
from xml.dom.minidom import parse
import requests
from csv import writer
import os
import csv
import xml.etree.ElementTree as ET


links = []

path = 'path_csvs'
files = []

#urls = read_urls(path)

xml_str = """<url>
<loc>https://www.fpc.gov/</loc>
<lastmod>2020-10-15T03:22:41+00:00</lastmod>
<priority>1.00</priority>
</url>
<url>
<loc>https://www.fpc.gov/vision-and-purpose/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/council-members/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/learn-about-federal-privacy-program/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/elements-of-federal-privacy-program/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/law-library/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/resources/SORNs/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/resources/omb/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/resources/glossary/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/programs-and-events/</loc>
<lastmod>2020-10-15T03:23:08+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/roles-in-federal-privacy/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/fair-info-practice-principles/</loc>
<lastmod>2022-02-02T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/privacy-act-1974/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/privacy-impact-asessments/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/coming-soon/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/privacy-policy/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/accessibility-policy/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/about-this-site/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.80</priority>
</url>
<url>
<loc>https://www.fpc.gov/elements-of-federal-privacy-program/breach-response/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.64</priority>
</url>
<url>
<loc>https://www.fpc.gov/elements-of-federal-privacy-program/privacy-impact-assessments/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.64</priority>
</url>
<url>
<loc>https://www.fpc.gov/elements-of-federal-privacy-program/system-of-record-notices/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.64</priority>
</url>
<url>
<loc>https://www.fpc.gov/elements-of-federal-privacy-program/privacy-workforce/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.64</priority>
</url>
<url>
<loc>https://www.fpc.gov/elements-of-federal-privacy-program/senior-agency-officials-for-privacy/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.64</priority>
</url>
<url>
<loc>https://www.fpc.gov/elements-of-federal-privacy-program/privacy=risky-management/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.64</priority>
</url>
<url>
<loc>https://www.fpc.gov/elements-of-federal-privacy-program/budget-and-acquisition/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.64</priority>
</url>
<url>
<loc>https://www.fpc.gov/elements-of-federal-privacy-program/website-and-digital-services/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.64</priority>
</url>
<url>
<loc>https://www.fpc.gov/elements-of-federal-privacy-program/training-and-accountability/</loc>
<lastmod>2020-10-15T03:23:09+00:00</lastmod>
<priority>0.64</priority>
</url>
<url>
<loc>https://www.fpc.gov/assets/pdf/m10-22.pdf</loc>
<lastmod>2020-10-15T03:22:58+00:00</lastmod>
<priority>0.64</priority>
</url>"""

root = ET.fromstring(f"<root>{xml_str}</root>")

urls = [loc.text for loc in root.findall(".//loc")]

print(urls[:5])

links = check_link(urls)

print(links)

with open('links.csv', 'w', newline='') as f:
    writer = writer(f)
    writer.writerow(['URL','Status'])
    writer.writerows(links)
    f.close()
    print('done, written to csv!')