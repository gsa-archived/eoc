from valid_url import check_link, read_urls
from xml.dom.minidom import parseString
from xml.dom.minidom import parse
import requests
from csv import writer
import os
import csv
import xml.etree.ElementTree as ET
import re


links = []

path = 'path_csvs'
files = []

#urls = read_urls(path)

xml_str = """<url>
<loc>https://www.evaluation.gov/agencies/agency-for-international-development/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-agriculture/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-commerce/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-defense/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-education/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-energy/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/health-and-human-services/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-homeland-security/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/housing-and-urban-development/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-justice/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-labor/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-state/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-the-interior/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-transportation/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-treasury/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/department-of-veterans-affairs/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/environmental-protection-agency/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/general-services-administration/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/national-aeronautics-and-space-administration/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/national-science-foundation/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/nuclear-regulatory-commission/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/office-of-personnel-management/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/small-business-administration/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/social-security-administration/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/cross-government/arp-equity-learning-agenda/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/cross-government/lgbtqi-equity-learning-agenda/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/cross-government/pma-learning-agenda/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/alix-gould-werth/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/anne-chiang/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/cecilia-hernandez/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/christine-heflin/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/erika-rissi/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/gregory-try/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/james-owendoff/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/jason-bossie/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/johnson-calvin/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/jolene-lauria/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/jonathan-soileau/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/jonathon-mcarthur/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/justin-abold-labreche/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/katherine-dawes/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/kelly-bidwell/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/lana-hurdle/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/matthew-soldner/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/patty-currier/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/raymond-furstenau/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/silvana-rubino-hallman/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/susan-jenkins/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/susan-wilschke/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/taryn-lovelace/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/members/winston-allen/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/other-agencies/AmeriCorps/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/other-agencies/IMLS/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/other-agencies/Millenial-Challenge-Corporation/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/other-agencies/National-Endowment/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/other-agencies/U.S-Merit/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/other-agencies/U.S-Trade-and-Development/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidence-plans/evaluation-policies/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidence-plans/summary/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/about-evaluation-officers/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/about/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidence-plans/annual-evaluation-plan/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidence-plans/capacity-assessments/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/collections/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/document-with-sidenav/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/document/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/interagency-council-on-evaluation-policy/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evaluation-officers/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evaluation-toolkit/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evaluation-toolkit/about-toolkit/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evaluation-toolkit/evaluation-101/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evaluation-toolkit/evaluation/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evaluation-toolkit/non-evaluator/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evaluation-toolkit/promoting-evaluation/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evaluation-toolkit/why-evaluate/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/faqs/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/keywords/community-engagement/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/keywords/design/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/keywords/dissemination/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/keywords/evaluation-questions/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/keywords/evaluation-types/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/keywords/evaluation-use/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/keywords/external-evaluation/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/keywords/methods/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/keywords/planning/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/keywords/resources/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidence-plans/learning-agenda/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/agencies/other-agencies/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2021/08/23/council-on-evaluation-policy/</loc>
<lastmod>2021-08-23T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2021/08/24/implementing-the-evidence-act/</loc>
<lastmod>2021-08-24T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2021/08/25/advance-our-priorities/</loc>
<lastmod>2021-08-25T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2021/08/26/evaluation-gov/</loc>
<lastmod>2021-08-26T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2021/09/27/OMB-M-21-27-guidance/</loc>
<lastmod>2021-09-27T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2021/10/11/eoc-awards-blog/</loc>
<lastmod>2021-10-11T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2021/11/17/in-the-spotlight-irs-raas/</loc>
<lastmod>2021-11-17T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2021/11/29/in-the-spotlight-evaluator-christina-yancey/</loc>
<lastmod>2021-11-29T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2021/12/15/in-the-spolight-Naomi-Goldstein/</loc>
<lastmod>2021-12-15T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/02/03/in-the-spotlight-clemencia-cosentino/</loc>
<lastmod>2022-02-03T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/02/23/in-the-spotlight-americorps/</loc>
<lastmod>2022-02-23T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/03/28/evidence-act-milestone/</loc>
<lastmod>2022-03-28T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/04/08/year-of-evidence-for-action-kicks-off/</loc>
<lastmod>2022-04-08T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/06/02/evidence-in-Action/</loc>
<lastmod>2022-06-02T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/06/09/build-equitable-recovery/</loc>
<lastmod>2022-06-09T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/06/27/importance-of-federal-evaluation-workforce/</loc>
<lastmod>2022-06-27T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/09/08/in-the-spotlight-USAID/</loc>
<lastmod>2022-09-08T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/09/15/pma-learning-agenda/</loc>
<lastmod>2022-09-15T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/10/20/announcing-2022-evaluation-community-awards/</loc>
<lastmod>2022-10-20T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2022/11/10/learning-agenda-questions/</loc>
<lastmod>2022-11-10T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2023/01/17/progress-on-the-white-house-YOE-for-action/</loc>
<lastmod>2023-01-17T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2023/03/13/commitment-to-evidence-and-evaluation/</loc>
<lastmod>2023-03-13T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2023/03/31/agencies-publish-evaluation-plans/</loc>
<lastmod>2023-03-31T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2023/08/30/new-way-to-get-evaluation-support/</loc>
<lastmod>2023-08-30T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2023/09/27/Hear-Directly-from-OMB-Evidence-Team-in-a-Recent-Podcast/</loc>
<lastmod>2023-09-27T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2023/10/23/evaluation-community-adward-2023/</loc>
<lastmod>2023-10-23T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2023/10/30/connecting-government-agencies-with-strategie-and-tools-for-sustainable-data-use/</loc>
<lastmod>2023-10-30T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/01/17/five-years-evidence-act/</loc>
<lastmod>2024-01-17T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/01/23/economy-recovery/</loc>
<lastmod>2024-01-23T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/01/29/history-blog/</loc>
<lastmod>2024-01-29T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/03/11/PMA-Learning-Agenda-FY23/</loc>
<lastmod>2024-03-11T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/03/19/President-Budget-Substains-investments/</loc>
<lastmod>2024-03-19T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/04/02/evaluation-plans-fy25/</loc>
<lastmod>2024-04-02T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/04/08/anncouncing-pma/</loc>
<lastmod>2024-04-08T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/04/16/leadership-academy-application/</loc>
<lastmod>2024-04-16T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/04/18/ipa-opportunity/</loc>
<lastmod>2024-04-18T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/06/04/uniform-grants-guidance/</loc>
<lastmod>2024-06-04T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/06/10/pma-learning-agenda-winners/</loc>
<lastmod>2024-06-10T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/08/13/public-participation/</loc>
<lastmod>2024-08-13T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/09/16/celebrating-evidence/</loc>
<lastmod>2024-09-16T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/09/27/challenge-winners/</loc>
<lastmod>2024-09-27T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/10/21/evidence-partnerships/</loc>
<lastmod>2024-10-21T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/10/24/evaluation-community-adward-2024/</loc>
<lastmod>2024-10-24T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/10/30/summer-ebt-for-children-program/</loc>
<lastmod>2024-10-30T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/11/12/USFWS-International-Conservation/</loc>
<lastmod>2024-11-12T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/2024/12/04/evidence-project-portal/</loc>
<lastmod>2024-12-04T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2023-03-09-ap-chapter-2024/</loc>
<lastmod>2023-03-09T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2023-03-09-highlight-from-evidence-chapter/</loc>
<lastmod>2023-03-09T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2023-08-22-program-evaluation/</loc>
<lastmod>2023-08-22T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2023-09-26-Highlights-from-the-PMALA-Workforce-Symposium/</loc>
<lastmod>2023-09-26T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2023-10-23-development-experience-clearinghouse/</loc>
<lastmod>2023-10-23T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2023-10-23-title-iv-e-prevention-services-clearinghouse/</loc>
<lastmod>2023-10-23T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2024-3-11-PMA-Learning-Agenda-FY23-Year-End-Report/</loc>
<lastmod>2024-03-11T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2024-3-14-Building-and-Using-Evidence/</loc>
<lastmod>2024-03-14T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2024-3-14-highlights-2025/</loc>
<lastmod>2024-03-14T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2024-6-18-program-evaluation-service-subgroup-ordering-procedures/</loc>
<lastmod>2024-06-18T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/2024-09-25-public-participation-community-engagement-toolkit/</loc>
<lastmod>2024-09-25T00:00:00+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/M-20-12-frequently-asked-questions/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/administer-united-states-foreign-assistance/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/administrative-data-for-statistical-purposes/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/building-and-using-evidence-to-improve-government-effectiveness-FY-2017/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/building-and-using-evidence-to-improve-government-effectiveness-FY-2018/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/building-and-using-evidence-to-improve-government-effectiveness-FY-2019/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/building-and-using-evidence-to-improve-government-effectiveness-FY-2020/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/building-and-using-evidence-to-improve-government-effectiveness-FY-2023/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/building-evidence-with-administrative-data-FY-2016/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/clearinghouse-for-labor-evaluation-and-research/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/clearinghouse-for-military-family-readiness/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/crimesolutions-national-institute-of-justice/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/evaluation-policy-and-federal-workforce/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/evidence-exchange-corporation-for-national-and-community-service/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/foreign-aid-transparency-and-accountability-act-of-2016/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/foundations-for-evidence-based-policymaking-act-of-2018/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/guide-paperwork-reduction-act/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/home-visiting-evidence-of-effectiveness/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/implementing-title-i-of-evidence-act/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/information-disseminated-by-federal-agencies/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/information-quality-act-public-law/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/information-quality-act/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/learning-agenda-annual-evaluation-plan-comparison/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/learning-agendas-personnel-and-planning-guidance/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/national-registry-of-evidence-based-programs-and-practices/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/omb-cIrcular-A-94/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/omb-circular-A-11/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/omb-m-21-27-evidence-based-policymaking/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/pathways-to-work-evidence-clearinghouse/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/performance-measurement-and-evaluation/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/president-biden-budget-invests-in-evidence/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/program-evaluation-FY-2011/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/program-evaluation-FY-2012/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/program-evaluation-and-data-analytics-FY-2013/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/program-evaluation-and-data-analytics-FY-2014/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/program-evaluation-and-data-analytics-FY-2015/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/program-evaluation-practices-one-pager/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/program-evaluation-standards-and-practices/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/program-evaluation-standards-one-pager/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/promise-evidence-based-policymaking/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/responsibilities-of-federal-statistical-agencies-and-recognized-statistical-units/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/results-first-clearinghouse-database/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/resources/what-works-clearinghouse/</loc>
<lastmod>2025-01-30T17:56:27+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/admin/</loc>
</url>
<url>
<loc>https://www.evaluation.gov/blog/</loc>
</url>
<url>
<loc>https://www.evaluation.gov/search/</loc>
</url>
<url>
<loc>https://www.evaluation.gov/</loc>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/DF_YEA%20Evidence%20Forum%20Readout.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/FAS-OMB%20Evidence%20Forum%20Readout.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/OMB%20Evidence%20Team%20IPA%20Opportunity.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/OSTP%20Evidence%20Forum%20PEW.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/OSTP%20Post%20Event%20Write%20Up%20FINAL-URBAN.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/PSU_YEA%20Evidence%20Forum%20Readout.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/Resource_What%20is%20Program%20Evaluation%20-%20A%20Beginners%20Guide.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/YEA%20Evidence%20Forum%20on%20Championing%20Evidence%20Use%20for%20Policy%20Impact%20in%20US%20Foreign%20Aid%20and%20Beyond.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/YEA%20Evidence%20Forum%20on%20Reducing%20Racial%20Wealth%20Gaps%20through%20Effective%20Support%20for%20Public%20Higher%20Education.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/YEA%20Evidence%20Forum%20on%20the%20Role%20of%20Higher%20Education%20in%20Solving%20Social%20Problems.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/YEA%20Forum%20on%20PMA%20Learning%20Agenda%20Readout.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/YEA%20Leveraging%20Air%20Pollution%20Research%20for%20Environment%20Health%20Policy.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/YEA%20Partnership%20Models%20to%20Strengthen%20Evidence-Informed%20Decision%20Making.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources-hidden/Year%20of%20Evidence%20Forum%20Report_August2022_RFA_CLEAN_FOR_POSTING.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/2024%20Evidence%20Chapter%20in%20Brief.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Buyers%20Guide_Program%20Evaluation%20Services%20Subgroup_508.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/CS_Evaluator%20Screening%20Tips.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/CS_Evidence%20for%20Action%20Pitch%20Decks.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/CS_Formative%20Evaluation%20Toolkit.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/CS_Program%20Evaluation%20Toolkit%20-%20Module%208%20Dissemination%20Approaches.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/CS_Research%20and%20Evaluation%20Capacity%20Self%20Assessment%20Tool.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Commission%20on%20evidence-based%20policymaking%20report.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Evaluation%20Policy%20and%20the%20Federal%20Workforce.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Evaluation.gov%20-%20FY%2025%20Highlights%20-%20Formatted.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/LA-and-AEP-Comparison.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Learning-Agenda-End-of-Year-Doc-508-Final.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/M-19-23.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/M-20-12-Frequently-Asked-Questions.pdf</loc>
<lastmod>2025-01-30T17:55:56+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/M-20-12.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/M-21-27.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/PMA%20Learning%20Agenda%20Workforce%20Symposium.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Performance-Measurement-and-Evaluation.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Portal%20-%20Challenge%20Opportunity.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Portal%20-%20GSA%20-%20Community%20Engagement%20Final.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Portal%20-%20NIH%20project%20with%20QA%20and%20slides.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Portal%20-%20Treasury%20-%20HAF%20w%20researcher%20interest.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Portal%20-%20Treasury%20-%20SLFRF%20w%20researcher%20interest.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Professional%20Services_Category_Attachment_Sol_47QSMD20R0001_Amd_17.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Program%20Evaluation%20Services%20Subgroup%20One-Pager.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Program-Evaluation-Practices.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Program-Evaluation-Standards.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Budgeting%20for%20Evaluation.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Communication%20Guide%20for%20TTCW%20Grantees%20-%20What%20to%20Consider%20When%20Sharing%20Program%20Accomplishments.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Dissemination%20Matrix%20Template.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Evaluation%20Questions%20Checklist%20for%20Program%20Evaluation.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Evaluator%20Screening%20Tips.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Formative%20Evaluation%20Toolkit.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_How%20to%20Apply%20Available%20Evidence.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_How%20to%20Develop%20a%20Program%20Logic%20Model.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_How%20to%20Develop%20the%20Right%20Research%20Questions%20for%20Program%20Evaluation.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_How%20to%20Manage%20an%20External%20Evaluation.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Identifying%20Resources%20for%20Evaluation.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Initiating%20an%20Evaluation%20Tip%20Sheet.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Introducing%20the%20Impact%20Evaluability%20Assessment%20Tool.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Program%20Evaluation%20Toolkit%20-%20Module%208%20Dissemination%20Approaches.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Quick%20Guide%20to%20Writing%20a%20Strong%20Evidence-Building%20Question.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Rapid%20Cycle%20Evaluation%20at%20a%20Glance.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_Research%20and%20Evaluation%20Capacity%20-%20Self%20Assessment%20Tool%20and%20Discussion%20Guide%20for%20CCDF%20Agencies.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Resource_The%20Administration%20for%20Children%20and%20Families%20Common%20Framework%20for%20Research%20and%20Evaluation.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/The%20Improve%20Group%20PPCE%20Toolkit%202024.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/The%20Improve%20Group%20PPCE%20Toolkit.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/Title-I-Evidence-Act-Brief.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/assets/resources/s290.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/404/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/about/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/admin/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/attachments/Community%20Engagement%20Project/Literature%20Review%20GSA_Final_Draft.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/attachments/Community%20Engagement%20Project/MSG-ProjectPortal-CE%20Impact%20Eval%20Plan%20and%20Survey%20Questions.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/attachments/Community%20Engagement%20Project/MSG-ProjectPortal-CE%20Impact%20Eval-Project%20Initiation.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/attachments/NIH%20-%20Measures%20for%20Impact/NIH%20interest%20meeting%20QA.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/attachments/NIH%20-%20Measures%20for%20Impact/NIH%20interest%20meeting%20slides.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/attachments/Treasury%20(HAF)/Treasury%20-%20HAF%20researcher%20interest%20meetings%20slides.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/attachments/Treasury%20(SLFRF)/Treasury%20-%20SLFRF%20Q%20and%20A.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/attachments/Treasury%20(SLFRF)/Treasury%20-%20SLFRF%20researcher%20interest%20meeting%20slides.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/completed/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/contact/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/contact/thank-you/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/documents/EP_FAQs.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/ongoing/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/open/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/project/Community%20Engagement%20Project/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/project/NIH%20-%20Measures%20for%20Impact/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/project/PMALA%20Challenge/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/project/Treasury%20(HAF)/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/project/Treasury%20(SLFRF)/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/search/</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal%20-%20Challenge%20Opportunity.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal%20-%20GSA%20-%20Community%20Engagement%20Final.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal%20-%20NIH%20opportunity.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal%20-%20Treasury%20-%20HAF.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal%20-%20Treasury%20-%20SLFRF.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal%20-%20Challenge%20Opportunity.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal%20-%20GSA-Community%20Engagement%20Final.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal%20-%20NIH%20opportunity.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal%20-%20Treasury%20-%20HAF.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal%20-%20Treasury%20-%20SLFRF.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal-Challenge%20Opportunity.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/Portal-GSA-Community%20Engagement%20Final.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>
<url>
<loc>https://www.evaluation.gov/evidenceportal/summary/test.pdf</loc>
<lastmod>2025-01-30T17:55:57+00:00</lastmod>
</url>"""

xml_2 = """"
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Account/Login</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/apply</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/apply/stories</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/attachment/downloadattachmentpdf/21540?description=Landscaping_FINAL_Applicable_Clauses_and_Provisions_1_5_16.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/attachment/downloadattachmentpdf/21634?description=Navy%20Example%2001-2017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/attachment/downloadattachmentpdf/21678?description=Ground%20Maintenance%20Services%20for%20Logan%20RD.docx</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/attachment/downloadattachmentpdf/21679?description=GSA%20Landscaping%20Services%20Bricker%20Bldg.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/attachment/downloadattachmentpdf/21680?description=Utah%20Ground%20Maintenance%20%20Snow%20Removal.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/attachment/downloadattachmentpdf/230?description=InstructionsToOfferorsAndEvalLanguageLandscapingServices.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/12%20KatyHatcher%20VeronicaBlette%20-%20EO%2013514%20water%20guidance.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Better%20Buying%20Power%202.0.pdf.pdf.pdf.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/BOMA%20360%20%28Statutory%20Compliance%20with%20Guiding%20Principles%29_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/BOMA%20360%20(Statutory%20Compliance%20with%20Guiding%20Principles)_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/BOMA%20Best%203.0%20%28Statutory%20Compliance%20with%20Guiding%20Principles%29_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/BOMA%20Best%203.0%20(Statutory%20Compliance%20with%20Guiding%20Principles)_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/BREEAM%202016%20%28Statutory%20Compliance%20with%20Guiding%20Principles%29_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/BREEAM%202016%20(Statutory%20Compliance%20with%20Guiding%20Principles)_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Columbia_A_Temperature_%20and_Seasonal_Energy_Analysis.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Facility%20Manager%20JTA%20For%20Public%20Comment.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Green%20Globes%20Existing%20Buildings%20%28Statutory%20Compliance%20with%20Guiding%20Principles%29%202013_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Green%20Globes%20Existing%20Buildings%20(Statutory%20Compliance%20with%20Guiding%20Principles)%202013_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Green%20Globes%20New%20Construction%20%28Statutory%20Compliance%20with%20Guiding%20Principles%29%202013_02-2021.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Green%20Globes%20New%20Construction%20(Statutory%20Compliance%20with%20Guiding%20Principles)%202013_02-2021.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/GSA%20GEB%20Case%20Study%20Report%20Mar%202021.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/GSA%20GEB%20Infographic%20May%202021.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/GSA%20Supply%20Chain%20Climate%20Risk%20Mgmt%20Framework_Final_508c.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/GSA_IPM_Guidance.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/guiding_principles_for_sustainable_federal_buildings_and_associated_instructions_february_2016.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/11%20CaraCarmichael%20Victor%20Olgyay%20-%20RMI%20Deep%20Energy%20Retrofits.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/13%20Judith%20Heerwagen%20-%20EPA%20Denver%20Demonstration%20Project.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/2%20-%20Overview%20of%20the%20BTO%20Cybersecurity%20Related%20Buildings%20Project.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/2%20Chuck%20Hardy%20-%20GSA%20Total%20Workplace%20Program.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/3%20-%20092216_ISWG%20Campus%20Management_FINAL.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/3%20-%20ISWG_DataCenterLiquidCooling_03072019%20final%20draft%20030419.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/3%20-%20NIST-G%20Solar%20PV%20Array%20presentation%20to%20ISWG%206-18-20_v2.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/3%20-%20Sandler%20presentation%20ISWG%202020%20final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/4%20-%20EUI_Findings_Presentation_to_ISWG_011017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/4%20-%20NREL%20-%203Flow%20-%20Smart%20Labs%20-%20LVMP%20Preso%20for%20ISWG%203-7-19%20v1.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/4%20-%20Solar%20Decathlon%20Briefing%20ISWG.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/5%20-%20ISWG_Presentation_PV%20OM%2009_19_18.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/6%20Steve%20Keppler%20-%20Better%20Buildings%20Challenge%20Data%20Centers.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/8%20Kristine%20Kingery%20-%20Army%20Net%20Zero%20Initiative.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/BBFA%20Winner%20BGNDRF_%20RShaw%20SHolland%20updtd%20May%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Building%20Glass%20and%20Lighting%20Impacts%20and%20Solutions%20%28FWS%20Mar%202015%29.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Building%20Glass%20and%20Lighting%20Impacts%20and%20Solutions%20(FWS%20Mar%202015).pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Circadian%20Light%20for%20Your%20Health%20%E2%80%93%20B.%20Steverson%20March%202017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Columbus%20LPOE_Interagency%20Sustainability%20Group%20Presentation_12.03.2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Deep%20Energy%20Savings%20Using%20ESPCs.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Dyess%20AFB%20ISWG%20slides%2025%20Jan%202018.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Federal%20Center%20South%20Building%201202%20%E2%80%93%20RThomas%2C%20Mar.%202013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Federal%20Center%20South%20Building%201202%20%E2%80%93%20RThomas,%20Mar.%202013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/FEWCIP%20Huxley%20and%20Koprowski%20ISWG%204.15.21.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/GPG%20-%20K%20Powell%20GSA%20-%20ISWG%20180517.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/GSA%20Advanced%20Metering%20-%20%20ION%20EEM%20Status_FY2015%20with%20value%20to%20programs.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/GSA%20CMU%20TECI%20ISWG%20October%202020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/GSA%20Impact%20Study_ISWGpost.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/High-Performance%20Building%20Design%20and%20Project%20Delivery%20in%20the%20Federal%20Sector%20-%20RCheng%2C%20Apr.%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Hot%20Water%20Temperature%20Maintenance%20Efficiency%20Opportunities.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Indoor%20Water%20Conservation.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Interior%20Lighting%20Campaign%20%E2%80%93%20M.%20Myer%20March%202017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/ISWG%20Audit%20Presentation%20BGustafson%201_21_2016_final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/ISWG%20Briefing%20on%20VA%20Energy%20Program%20200423.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/ISWG%20Presentation%20ReOpt1%20State%20Dept%20Final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/ISWG_ASID%20HQ%20Presentation_10-2017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/LA%20Courthouse%20-%20D%20Allen%20GSA%20-%20ISWG%20180517.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/NASA%20Ames%20Sustainability%20Base_SDianati%20Nov%202012.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/NASA%20JPL%20ESPC%20with%20notes.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Numbers%20and%20Names_ZNE%20-%20CHiggins%20updtd%20Feb.%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Overview%20of%20WaterSense%20Resources.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/RO%20Powerpoint%20Presentation%20for%20Sustainability%20Group%20%28Liz%20Dawson%20FWS%20151103%29.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/RO%20Powerpoint%20Presentation%20for%20Sustainability%20Group%20(Liz%20Dawson%20FWS%20151103).pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Sustainability%20Success%20at%20the%20Provo%20Area%20Office%20%E2%80%93%20J.%20Kresge%20and%20C.%20Southworth%20March%202017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Sustainable%20Building%20Study%20Using%20Whole-System%20and%20Life-Cycle%20Thinking%20-%20JParisi%2C%20Nov.%202012.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Sustainable%20Building%20Study%20Using%20Whole-System%20and%20Life-Cycle%20Thinking%20-%20JParisi,%20Nov.%202012.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/USDA%20Green%20Buildings%20%E2%80%93%20CBroad%2C%20Sep.%202013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/USDA%20Green%20Buildings%20%E2%80%93%20CBroad,%20Sep.%202013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/WaterSense%20Update%205-17-18%20final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Zhivov%20-%20Energy%20planning%20resilience%20ISWG%20181206%20Final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/1%20-%20GSA_Challenges%20in%20Implementing%20an%20Agency-wide%20Advanced%20Metering%20System-%20%20IT%20Security%20and%20Support%20Needs_v2%201.12.17.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/1%20-%20HPBCS%20Update%20brief_ISWG_May%2016%202019.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/1%20-%20Pomeroy%20DCOI%20Deck_ISWG.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/1%20Don%20Horn%20-%20189%202014%20Update.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/10%20Donna%20McIntire%20-%20Sustainability%20Global%20Portfolio.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/15%20Keith%20Welch-%20DoD%20Sustainable%20Buildings%20Strategy.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/16%20ChristinaStamper%20JohnPark%20-%20VA%20Green%20Building%20Program.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/2%20-%201%20GW%20Goal%20-%20ISWG%202016.11.10.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/2%20-%2050001Ready%20for%20ISWG%202.13.20%20Final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/2%20-%20GP%20ISWG%205-19%20%28Finalv2%29.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/2%20-%20GP%20ISWG%205-19%20(Finalv2).pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/2%20Chuck%20Hardy%20-%20GSA%20Total%20Workplace%20Program.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/3%20-%20092216_ISWG%20Campus%20Management_FINAL.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/3%20-%202018%2009%2013%20DHS_ISWG%20combined.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/3%20-%20ASHRAE%2090.1-2013%20and%2010%20CFR%20433%20-%20Halverson%20ISWG%20191205.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/3%20-%20CBECS%20Update%20for%20ISWG%20-%20May%202016.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/3%20-%20ISWG%2012%20Jan%20haeg.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/3%20-%20NREL%20ISWG%20Presentation%20Nov%2010%202016.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/4%20-%20EPA%20ISWG%20meeting%202_2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/4%20-%20Sandler-Hydras%20GEB%20talk%20for%20ISWG%2012-5-19%20v5.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/4%20Alison%20Kinn%20Bennett%20-%20EPP%20Update%204-2015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/5%20-%20EPA%20Water%20Reuse%20-%20Lape%20191205.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/7%20Joelle%20Michaels%20-%20CBECS%20Update.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/8%20Kristine%20Kingery%20-%20Army%20Net%20Zero%20Initiative.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Adv%20Comm%20update%20to%20ISWG%2011-28-17.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/AFFECT%20Grant%20Program.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Building-Grid%20Integration%2C%20Zero%20Energy%20Buildings%2C%20and%20Strategic%20Energy&amp;</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Buildings%20Energy%20Star%20Portfolio%20Manager%20-%20CHatcher%2C%20Mar.%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Buildings%20Energy%20Star%20Portfolio%20Manager%20-%20CHatcher,%20Mar.%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Coming%20Attractions%20from%20GSA%20GBAC.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Defining%20Zero%20Energy%20Buildings%20-%20SPunjabi%2C%20Mar.%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Defining%20Zero%20Energy%20Buildings%20-%20SPunjabi,%20Mar.%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/EPA%20Recommendations%20-%20ISWG%205-2017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ESPC%20ENABLE%20Update%20%E2%80%93%20I.%20Birnbaum%20March%202017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ESPC%20ESA%20Update%20%E2%80%93%20T.%20Niro%20March%202017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/FEMP%20RE%20Presentation%20FINAL.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Green%20Building%20Certification%20and%20Fossil%20Fuel%20Reduction%20-%20SJensen%20updtd%20May%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Green%20Leasing%20-%20AKosmides%20Mar2013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/GSA%20Sustainable%20Buildings%20Program.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Interior%20Lighting%20Campaign%20%E2%80%93%20M.%20Myer%20March%202017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG%20%28Army%20Net%20Zero%20Waste%29%28Jul%202016%29.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG%20(Army%20Net%20Zero%20Waste)(Jul%202016).pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG%20Bourne%20Fitwel%2007-20-2017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG%20green%20leasing%20update%207-20-16.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG%20HAWG%201-25-18.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG%20Jensen%20slides%2090.1-2013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG%20Meeting%2050001.Boomsma.1.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG%20Tremper%2007-20-2017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG%20York%20Fitwel%2007-20-2017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG_Army_Climate_Resilience_Brief.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG_ASID%20HQ%20Presentation_10-2017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG_GSA%20WELL%20Intro%202.0.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG_Net%20Zero%20Overview_10-05-17.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Living%20Building%20Challenge%20-%20ASturgeon%20Nov2013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/NASA%20Sustainable%20Facilities%20and%20Principles_EMszarupdatedJun15.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Net%20Zero%20Waste%20ISWG%20EPA%20Region%209.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/NREL%20Storage%20Presentation%203-19-18_edited.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Persily-Walls%20189_IgCC%20to%20ISWG%201-25-18.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Presidio%20Abby%20Morris%20July%2021%20ISWG%20Net%20Zero%20Waste%20Panel.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Summary%20Impacts%20of%20EA%202020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Sustainable%20Buildings-Resolving%20Sticky%20Issues%20-%20CMeincke%20MMyers%2C%20Mar.%202012.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Sustainable%20Buildings-Resolving%20Sticky%20Issues%20-%20CMeincke%20MMyers,%20Mar.%202012.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Taylor%20-%20ZEB%20Definition%202015-11-12.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/U.S.%20EPA%20Activities%20to%20Support%20Green%20Power%20Purchasing.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/USCG%20Advd%20Metering%20Program%20-%20L.Smolinski%20Nov.%202013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/1%20-%2020160519%20LCIC%20ISWG%20FINAL.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/1%20-%20EEx%20and%20BB%20Summit%202018%20-%20ISWG%20Updates%20Sept%202018.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/1%20-%20Energy%20Exchange%202019%20Update%20_%20ISWG%20072519.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/1%20-%20Energy%20Exchange%202019%20Update%20_%20ISWG_030719.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/1%20-%20FEMP%20EEx20%20ISWG_2020-06-18%20%28updated%29.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/1%20-%20FEMP%20EEx20%20ISWG_2020-06-18%20(updated).pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/1%20-%20ISWG_EEx20%20Update_02.13.20%20final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/1%20-%20SFTool%20ecomedes%20ISWG%2011-10-16.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/14%20Erin%20Shaffer%20-%20Principles%20for%20New%20and%20Renovation%20Construction.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/2%20-%20EEx19%20Overview%20ISWG%20-%2012.05.19.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/2%20-%20ISWG%20FBTPA%20Tools%20and%20Resources%20Brief%20180920.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/2%20-%20Sustainable%20acquisition%20training%20%28Shab%209-22-16%29.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/2%20-%20Sustainable%20acquisition%20training%20(Shab%209-22-16).pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/2020%20EEx%20ISWG%20Presentation%20200423.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/3%20-%20Energy%20Exchange%202019%20Update%20_%20ISWG_051619.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/3%20-%20GBI%20ISWG%202019-%20FINAL%20JMH.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/3%20-%20NREL%20ISWG%20Presentation%20Nov%2010%202016.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/3%20DanielStuder%20ElizaHotchkiss%20-%20TPEx%20Overview%20and%20Update.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/4%20-%20eProject%20Builder%20Update%20for%2020%20Sept%202018.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/4%20-%20ISWG_SLCdemo_05192016_final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/4%20-%20LEED%20v4.1%20GSA%20190725%20pic_final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/5%20-%20Energy%20Exchange%202017%20-%20ISWG%201-12-17.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/5%20-%20LBT%20webinar%20slides%205-10-19.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/9%20Kristin%20Tadonio%20-%20Cross-Sector%20EE%20Opportunities.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Beverly%20Dyer-%20FEMP%20Training_ISWG%20Presentation%20Jan2013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/BTM%20Battery%20Storage%203-22-18%20Di%20Wu.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Building%20Glass%20and%20Lighting%20Impacts%20and%20Solutions%20%28FWS%20Mar%202015%29.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Building%20Glass%20and%20Lighting%20Impacts%20and%20Solutions%20(FWS%20Mar%202015).pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Buildings%20Energy%20Star%20Portfolio%20Manager%20-%20CHatcher%2C%20Mar.%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Buildings%20Energy%20Star%20Portfolio%20Manager%20-%20CHatcher,%20Mar.%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Commercial%20Buildings%20Integration%20Group%20Update.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/EEx%20-BBS%20Overview%20_ISWG_July%202018%20%28Baker%29.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/EEx%20-BBS%20Overview%20_ISWG_July%202018%20(Baker).pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/EEx20_ISWG%20Oct%20-%202020-10-15.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/EEx21_April%202021_ISWG_2021-04-14.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Energy%20Exchange%20Overview_ISWG.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/FBPTA%20Program%20Brief%20-%20BGilligan%20Apr.%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/FEMP%20FRCS%20Overview%20%20Training%20Deck%202020-10-22.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/FEMP%20Tech%20Deployment%20Tools%20-%20ISWG%20Presentation%20012116.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/FEMP%20Water%20Efficiency%20Tools%20and%20Training.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/GBCIGuiding%20Principles_LStanley%20and%20MGallagherRogers%20Sept2013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Golden%20-%20ICP%20Presentation%20to%20ISWG%201-25-18.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/GPG%20Overview%20-%20KPowell%20Sep2013%2C%20updated%20May2015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/GPG%20Overview%20-%20KPowell%20Sep2013,%20updated%20May2015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/GSA%20Carbon%20Footprint%20Tool.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Hatcher%20-%20ENERGY%20STAR%20PM%20Update%20_ISWG%207-26-18.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Interior%20Lighting%20Campaign%20%E2%80%93%20M.%20Myer%20March%202017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Inventory%20of%20Federal%20Greenhouse%20Gas%20Emissions%2C%20Reductions%20to%20Date%2C%20and%20Potential%20Reductions.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Inventory%20of%20Federal%20Greenhouse%20Gas%20Emissions,%20Reductions%20to%20Date,%20and%20Potential%20Reductions.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/ISWG%205_25_17%20-%20SFTool.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/ISWG%20Baker%20GPs%20FAQ%2007-20-2017.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/ISWG%20Dashboard%20Overview%20%2807%20Dec%2017%29.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/ISWG%20Dashboard%20Overview%20(07%20Dec%2017).pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/ISWG%20FEDSAT%20Brief%20Final%20-%2011-10-2015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/ISWG%20Presentation%20ReOpt1%20State%20Dept%20Final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/ISWG.ESPC%20ENABLE%20Jan%2021%202016_final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/ISWG_EEx%20Feedback%20Presentation_10-05-17.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/ISWG_REopt%20NREL-FEMP%20Final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Living%20Building%20Challenge%20-%20ASturgeon%20Nov2013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Net%20Zero%20Partnerships.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Nmair%20O%20and%20M-ISWG%2012-06-2018%20Final.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Overview%20-%20Materials%20Management%20and%20Waste%20Tracking%20in%20Portfolio%20Manager.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Overview%20of%20WaterSense%20Resources.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/RE%20Catalog%20of%20Servcies%20-%20BKovacic%20May2013.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/SFTool.gov%20Serious%20Games_MBloom%20May%202015.pptx.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Smarter%20DC%20Challenge.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/Sustainable%20Infrastructure%20and%20the%20Role%20of%20Envision.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/LEED%20v4%20BDC%20%28Statutory%20Compliance%20with%20Guiding%20Principles%29_02-2021.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/LEED%20v4%20BDC%20(Statutory%20Compliance%20with%20Guiding%20Principles)_02-2021.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/LEED%20v4%20OM%20%28Statutory%20Compliance%20with%20Guiding%20Principles%29_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/LEED%20v4%20OM%20(Statutory%20Compliance%20with%20Guiding%20Principles)_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Living%20Building%20Challenge%20EB%20%28Statutory%20Compliance%20with%20Guiding%20Principles%29_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Living%20Building%20Challenge%20EB%20(Statutory%20Compliance%20with%20Guiding%20Principles)_12-2020.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Living_Architecture_Green_Roofs_for_Public_Buildings.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Net%20Zero%20Partnerships.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Pollinator%20Health%20Strategy%202015.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Proficiency%20Level%20Approach%20Update%20-%20March%2013.2018.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/recommendations_on_sustainable_landscaping_practices.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Signed%20DoD%20green%20purchasing%20reporting%20memo.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Signed%20PC%20Power%20Memo.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/supporting_the_health_of_honey_bees_and_other_pollinators.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/T8S1_Zekert.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/water_implementing_instructions.pdf</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/developer</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Explore</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/1/lighting</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/10/solid-waste</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/11/planted-roof</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/12/submetering</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/2/hvac</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/3/water</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/8/ieq</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/1/lighting/lighting</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/1/lighting/system-overview</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/10/hvac/integrative-design-process</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/12/hvac/system-bundling</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/13/hvac/relevant-mandates-and-rating-systems</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/14/hvac/resources-and-case-studies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/18/water/system-overview</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/19/water/integrative-design-process</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/2/lighting/integrative-design-process</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/21/water/system-bundling</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/22/water/relevant-mandates-and-rating-systems</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/23/water/resources-and-case-studies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/30/ieq/system-overview</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/31/ieq/integrative-design-process</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/33/ieq/system-bundling</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/34/ieq/relevant-mandates-and-rating-systems</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/35/ieq/resources-and-case-studies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/36/lighting/resources-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/37/lighting/human-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/38/lighting/financial-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/39/lighting/o-m-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/4/lighting/system-bundling</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/40/water/resources-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/41/water/human-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/42/water/financial-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/43/water/o-m-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/44/hvac/resources-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/45/hvac/human-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/46/hvac/financial-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/47/hvac/o-m-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/48/ieq/resources-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/49/ieq/human-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/5/lighting/relevant-mandates-and-rating-systems</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/50/ieq/financial-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/51/ieq/o-m-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/57/solid-waste/system-overview</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/59/solid-waste/integrative-design-process</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/6/lighting/resources-and-case-studies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/63/solid-waste/system-bundling</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/65/solid-waste/relevant-mandates-and-rating-systems</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/67/solid-waste/resources-and-case-studies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/69/solid-waste/resources-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/71/solid-waste/human-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/73/solid-waste/financial-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/75/solid-waste/om-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/76/planted-roof/system-overview</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/77/planted-roof/integrative-design-process</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/79/planted-roof/system-bundling</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/80/planted-roof/relevant-mandates-and-rating-systems</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/81/planted-roof/resources-and-case-studies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/82/planted-roof/resources-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/83/planted-roof/human-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/84/planted-roof/financial-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/85/planted-roof/o-m-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/86/submetering/system-overview</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/87/submetering/integrative-design-process</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/89/submetering/system-bundling</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/9/hvac/system-overview</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/90/submetering/relevant-mandates-and-rating-systems</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/91/submetering/resources-and-case-studies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/92/submetering/resources-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/93/submetering/human-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/94/submetering/financial-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-building/section/95/submetering/o-m-impact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/47/private-office</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/48/receptionlobby</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/61/open-office-area</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/81/tenant-corridor</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/82/tenant-restroom</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/83/enclosed-conference</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/84/open-teaming-space</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/85/breakpantry</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/86/computerlan-room</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/87/support-area</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/88/cafeteria</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/explore/green-workspace/89/laboratory</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/fedsat</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/fedsat/about</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/feedback/new</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/GpcDownload/GpcProductsByServiceXlsx/3</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/GpcDownload/GpcProductsCsv</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/GpcDownload/GpcProductsTxt</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/GpcDownload/GpcProductsXlsx</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/green-guidance</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/green-guidance/for/1/facility-manager</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/green-guidance/for/2/procurement-professional</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/green-guidance/for/3/leasing-specialist</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/green-guidance/for/4/project-manager</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/about</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/dod</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/doe</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/federal</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/1263/wood-concrete-sealers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies//1303/asphalt-restorers/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/1346/concrete-asphalt-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/1347/erosion-control-materials/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/1591/skylights/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/1787/epoxy-systems/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/1809/photovoltaic-modules-inverters/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/1827/storm-windows/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/22/building-insulation/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/231/roofing-materials/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/272/windows/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/29/cement-concrete/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/76/doors/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/79/dust-suppressants/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1/construction-building-supplies/99/flowable-fill/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/38/combination-unitsmulti-function-devices</loc> <lastmod>2024-06-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/39/commercial-audio-visual-equipment/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/58/computers/0</loc> <lastmod>2024-06-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/62/copiers/0</loc> <lastmod>2024-06-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/1401/data-center-storage/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/69/digital-duplicators/0</loc> <lastmod>2024-06-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/194/digital-picture-frames/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/68/digital-signage/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/80/dvd-blu-ray-disc-players/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/89/fax-machines/0</loc> <lastmod>2024-06-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/128/home-audiovideo/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/1402/large-network-equipment/0</loc> <lastmod>2024-06-19T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/153/mailing-machines/0</loc> <lastmod>2024-06-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/1760/mobile-phones/0</loc> <lastmod>2024-06-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/164/monitors/0</loc> <lastmod>2024-06-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/213/printers/0</loc> <lastmod>2024-06-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/236/scanners-all-in-one-devices/0</loc> <lastmod>2024-06-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/237/servers/0</loc> <lastmod>2024-07-17T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/63/telephones/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/10/office-equipment-electronics/252/televisions/0</loc> <lastmod>2024-07-10T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1048/shipping-packaging-supplies/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1048/shipping-packaging-supplies/1248/films/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1048/shipping-packaging-supplies/1252/manual-grade-strapping/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1048/shipping-packaging-supplies/1310/packing-insulating-materials/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1048/shipping-packaging-supplies/1254/pallets/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1048/shipping-packaging-supplies/186/paperboard-packaging-products/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1048/shipping-packaging-supplies/1800/product-packaging/0</loc> <lastmod>2024-07-19T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/1048/shipping-packaging-supplies/1354/thermal-shipping-containers/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/1276/athletic-field-paint/0</loc> <lastmod>2024-06-11T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/17/bike-racks/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/1791/fire-logs-fire-starters/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/138/ice-skating-rinks/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/188/park-benches/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/1357/picnic-tables/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/202/plastic-fencing/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/1798/playground-athletic-surface-materials/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/208/playground-equipment/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/209/playground-surfaces/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/235/running-tracks/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/12/outdoor-recreational-equipment/1805/toys-sporting-gear/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/13/printing-supplies/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/13/printing-supplies/1313/specialty-inks/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/13/printing-supplies/1314/sheetfed-inks/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/13/printing-supplies/1317/toner-ink/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/13/printing-supplies/225/remanufactured-printer-ribbons/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/13/printing-supplies/224/toner-cartridges/0</loc> <lastmod>2024-08-24T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/17/traffic-control/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/17/traffic-control/33/channelizers/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/17/traffic-control/66/delineators/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/17/traffic-control/95/flexible-delineators/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/17/traffic-control/189/parking-stops/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/17/traffic-control/220/railroad-grade-crossing-surfaces/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/17/traffic-control/1806/traffic-zone-marking-paints/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/17/traffic-control/256/traffic-barricades/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/17/traffic-control/257/traffic-cones/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/1419/aircraft-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/1235/alternative-fuels/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/1421/automotive-care-products/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/1420/boatrv-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/1834/de-icers-fluid/0</loc> <lastmod>2024-08-02T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/67/diesel-fuel-additives/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/1740/electric-vehicle-charging-stations/0</loc> <lastmod>2024-11-20T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/222/engine-coolants/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/1423/gasoline-fuel-additives/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/165/motor-vehicle-air-conditioning/0</loc> <lastmod>2024-05-07T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/223/refrigerated-transport/0</loc> <lastmod>2024-05-07T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/230/retread-tires/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/18/transportation-automotive/1649/tire-additives/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1335/bath-products/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1372/bath-towels/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1281/cuts-burns-abrasions-ointments/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1389/deodorants/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1789/facial-care-products/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1790/feminine-care-products/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1336/foot-care-products/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1337/hair-care-products/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/125/hand-sanitizers/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1251/lip-care-products/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1393/lotions-moisturizers/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1394/shaving-products/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1396/sun-care-products/0</loc> <lastmod>2024-07-26T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/20/personal-care-products/1260/topical-pain-relief-products/0</loc> <lastmod>2024-03-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/123/commercial-griddles/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/131/residential-refrigerators/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/1358/residential-freezers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/1555/residential-clothes-dryers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/1598/commercial-clothes-washers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/1743/commercial-coffee-brewers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/1753/commercial-laboratory-grade-refrigerator-freezer/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/179/commercial-ovens/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/229/commercial-retail-food-refrigeration/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/35/residential-clothes-washers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/40/commercial-dishwashers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/41/commercial-freezers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/44/commercial-fryers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/46/commercial-hot-food-holding-cabinets/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/47/commercial-ice-makers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/49/commercial-steam-cookers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/51/commercial-refrigerators/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/71/residential-dishwashers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/37/commercial-cold-storage-warehouses/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/1830/commercial-electric-cooktop/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/141/commercial-industrial-process-refrigeration-systems/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/261/commercial-vending-machines/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/263/commercial-low-temperature-refrigeration-systems/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/266/commercial-water-coolers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/21/appliances/1826/residential-electric-cooking-products/0</loc> <lastmod>2024-02-26T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/22/lighting-electrical/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/22/lighting-electrical/28/ceiling-fans/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/22/lighting-electrical/65/decorative-light-strings/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/22/lighting-electrical/1408/exterior-lighting/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/22/lighting-electrical/1410/fluorescent-lighting/0</loc> <lastmod>2024-06-24T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/22/lighting-electrical/1739/led-luminaires-commercial-industrial/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/22/lighting-electrical/1414/light-bulbs/0</loc> <lastmod>2024-05-15T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/22/lighting-electrical/151/light-fixtures/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/22/lighting-electrical/1831/smart-home-energy-management-system/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/11/bathroom-sink-faucets-accessories-residential/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/1592/pool-pumps/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/1284/septic-system-treatments/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/239/showerheads/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/1829/spray-sprinkler-bodies/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/255/toilets/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/259/urinals/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/1285/wastewater-inoculants/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/1397/wastewater-systems-coatings/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/1398/water-clarifying-agents/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/23/plumbing-systems-fixtures/268/water-tank-coatings/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/107/furnaces/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/108/commercial-gas-water-heaters/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/112/heat-pumps-geothermal-ground-source/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/1245/dehumidifiers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/1257/air-purifiers-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/126/non-mechanical-heat-transfer-systems/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/1321/boilers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/1322/air-conditioning-central/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/1378/residential-water-heaters/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/140/industrial-process-air-conditioning/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/150/light-commercial-heating-cooling/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/1597/ductless-heating-cooling/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/1652/hvac-maintenance-products/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/1654/air-conditioner-coil-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/173/non-pressure-pipes/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/1754/smart-thermostats/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/232/air-conditioning-room/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/262/ventilation-fans/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/34/chillers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/24/hvac-mechanical/6/heat-pumps-air-source/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/26/custodial-supplies/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/26/custodial-supplies/1301/air-fresheners-deodorizers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/26/custodial-supplies/1360/bathroom-tissue/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/26/custodial-supplies/1359/facial-tissues/0</loc> <lastmod>2024-08-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/26/custodial-supplies/124/hand-soaps-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/26/custodial-supplies/177/office-recycling-containers-waste-receptacles/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/26/custodial-supplies/1363/plastic-trash-bags/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/27/furniture-fixtures/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/27/furniture-fixtures/1734/furniture/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/27/furniture-fixtures/176/office-furniture-components/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/1238/adhesives/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/1732/ceiling-tiles/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/56/composite-panels/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/23/flooring-carpet/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/27/flooring-carpet-cushion/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/1307/flooring-hard-surface/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/154/flooring-mats/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/98/flooring-resilient/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/143/laminated-paperboard/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/163/modular-threshold-ramps/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/1338/paint/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/1799/powder-coatings/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/238/shower-restroom-dividerspartitions/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/241/signage/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/251/structural-fiberboard/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/1804/surface-guards-molding-trim-products/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/1808/wall-coverings/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/1735/wallboardgypsum-boarddrywall/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/3/building-finishes-materials/1312/wood-concrete-stains/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/1644/appliance-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/1850/bags-liners-compostable-organic-materials/0</loc> <lastmod>2024-10-25T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/1286/dishwashing-products/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/72/disposable-containers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/73/disposable-cutlery/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/74/disposable-tableware/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/1785/durable-cutlery/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/1786/durable-tableware/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/105/food-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/1655/kitchencountertop-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/1795/kitchenware-accessories/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/1288/oven-grill-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/183/paper-napkins/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/1362/paper-towels/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/4/cafeteria-supplies/185/paper-tray-liners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/4/adhesive-mastic-removers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1388/animal-cleaning-products/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1779/animal-habitat-care-products/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1302/asphalt-tar-removers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/10/bathroom-spa-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1657/biological-based-grease-trap-lift-station-maintainers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1658/biological-based-holding-tank-treatment-deodorizers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1648/brick-masonry-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/25/carpet-upholstery-cleaners-general-purpose/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/26/carpet-upholstery-cleaners-spot-removers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1242/cleaning-solvents/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1780/cleaning-tools/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1346/concrete-asphalt-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1651/descalers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1282/drain-maintainers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1744/dry-erase-board-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1306/electronic-components-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1283/floor-cleaners-protectors/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/96/floor-strippers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1309/furniture-cleaners-protectors/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1361/general-purpose-industrial-wipers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/114/glass-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/116/graffiti-grease-removers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1647/granite-stone-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/130/household-cleaners-general-purpose/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/139/industrial-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/142/ink-removers-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1745/jewelry-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/146/laundry-products-general-purpose/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/147/laundry-products-pretreatmentspot-removers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1392/leather-vinyl-rubber-care-products/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1650/medical-instrument-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1428/metal-cleaners-corrosion-removers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1432/microbial-cleaning-products/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/167/multipurpose-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1746/outdoor-furniture-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1437/paint-removers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1255/parts-wash-solution/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1258/sorbents/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1395/specialty-precision-cleaners-solvents/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1259/sterilants/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/5/cleaning-products/1645/wood-cleaners/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/1387/agricultural-spray-adjuvants/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/1275/animal-repellents/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/57/compost/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/1345/compost-activators-accelerators/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/1244/de-icers-salts/0</loc> <lastmod>2024-08-02T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/1390/dethatchers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/90/fertilizers/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/1793/gardening-supplies-accessories/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/129/hoses/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/134/hydraulic-mulch/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/145/landscape-irrigation-services/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/148/lawn-garden-edging/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/166/mulch/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/204/plastic-lumber-landscaping-timber-posts/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/1803/soil-amendments/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/6/landscaping-supplies/270/weather-sensor-based-irrigation-control-technologies/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/32/chain-cable-lubricants/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/61/concrete-asphalt-release-fluids/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/1440/engine-crankcase-oil/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/85/engine-lubricating-oils/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/94/firearm-cleaners-lubricants-protectants-clp/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/106/forming-lubricants/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/1391/fuel-conditioners/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/109/gear-lubricants/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/1268/greases/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/122/greases-truck/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/127/heat-transfer-fluids/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/1237/hydraulic-fluids/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/1269/metalworking-fluids/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/162/mobile-equipment-hydraulic-fluid/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/168/multipurpose-lubricants/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/1796/other-lubricants/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/193/penetrating-lubricants/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/1311/pneumatic-equipment-lubricants/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/226/re-refined-lubricating-oils/0</loc> <lastmod>2024-07-31T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/1274/slide-lubricants/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/1807/transmission-fluids/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/258/turbine-drip-oils/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/3/two-cycle-engine-oils/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/7/lubricants-fluids/1441/water-turbine-bearing-oils/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1239/aerosols/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1240/bedding/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1277/bilge-maintainers/0</loc> <lastmod>2024-02-09T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1278/bioremediation-materials/0</loc> <lastmod>2024-06-11T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1304/blast-media/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1241/blasting-grit/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1305/candles-wax-melts/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1243/corrosion-preventatives/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1247/expanded-polystyrene-foam-recycling-products/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1833/fire-defense-products/0</loc> <lastmod>2024-07-19T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/92/fire-suppression-explosion-protection/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/100/fluid-filled-transformers/0</loc> <lastmod>2024-02-27T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1832/foam-blowing-agents/0</loc> <lastmod>2024-07-30T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1794/heating-fuels-wick-lamps/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1250/industrial-drums/0</loc> <lastmod>2024-08-01T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/8/miscellaneous/1797/phase-change-materials/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/9/office-supplies/0</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/9/office-supplies/8/awards-plaques/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/9/office-supplies/18/binders/0</loc> <lastmod>2024-06-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/9/office-supplies/1792/folders-filing-products/0</loc> <lastmod>2024-08-07T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/9/office-supplies/214/paper-paper-office-supplies/0</loc> <lastmod>2024-08-06T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/9/office-supplies/171/paper-newsprint/0</loc> <lastmod>2024-08-02T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products/9/office-supplies/199/plastic-office-supplies/0</loc> <lastmod>2024-08-05T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/47/private-office</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/48/receptionlobby</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/61/open-office-area</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/81/tenant-corridor</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/82/tenant-restroom</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/83/enclosed-conference</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/84/open-teaming-space</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/85/breakpantry</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/86/computerlan-room</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/87/support-area</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/88/cafeteria</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-products-workspaces/89/laboratory</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-services/10/meeting-conference-services</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-services/11/transportation-services</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-services/3/landscaping-services</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-services/4/pest-management</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-services/5/electronic-equipment-leasing</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-services/6/fleet-maintenance</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-services/7/custodial-services</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-services/8/laundry-services</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/green-services/9/cafeteria-food-services</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/greenprocurement/workspaces</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/guidingprinciples</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/home/about</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/home/accessibilityaids</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/home/contact</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/home/privacypolicy</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/home/sitemap</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/home/teach</loc> <lastmod>2021-07-30T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/1</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/1/sustainability-topics</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/10129/agency-practices</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/2</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/2/federal-requirements</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/2/legal-requirements</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/42</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/42/case-studies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/1/indoor-environmental-quality-ieq</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/142/workplace-environment-catalyst-social-change</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/166</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/166/high-performance-buildings-marketplace</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/181</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/181/buildings-energy</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/182</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/182/water-consumption</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/183</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/183/buildings-water</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/184</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/184/us-waste-recycling</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/185</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/185/recycling-bottles</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/201</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/201/post-consumer-fiber-paper</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/202</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/202/time-indoors</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/204</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/204/ieq-asthma</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/241/sense-place</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/242</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/242/occupant-comfort</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/243/flexible-workplace-design</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/244/health</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/245/spatial-equity</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/371/environmental-programs</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/41/sustainability</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/426/plug-loads</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/683/plug-load-nuggets</loc> <lastmod>2025-02-04T02:30:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/43/materials-resources</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/435/department-defense-dod-sustainable-product-purchasing</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/44</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/444</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/445</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/446</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/45/water-efficiency</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/46/sustainable-sites</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/480</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/480/energy-management-systems-enms</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/481</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/481/sustainability-program-development</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/502/child-care-centers</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/540/other-gpc-links</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/551</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/551/sftool-product-search</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/563</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/563/pass-fedsat-earn-hour-continuing-education</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/564</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/564/led-price-drop</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/566</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/566/web-policies-important-links</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/571</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/571/building-heating-ventilation-air-conditioning-hvac</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/572</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/572/building-plug-loads</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/573</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/573/energy-savings-performance-contracts-espcs</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/574</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/574/helpful-tools</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/576/buildings-health</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/577/circadian-light</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/579/importance-daylight</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/580/biophilic-design</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/617</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/617/recycling-checklist</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/626/enhancing-health-indoor-air</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/631/guiding-principles-sustainable-federal-buildings</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/632/back</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/633/building-selection</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/638/grid-interactive-efficient-buildings</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/639/climate-terms-tools</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/64</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/64/adaptable-workplace-laboratory</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/66</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/66/indoor-air-quality</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/agency-practices/444/iswg-policies-strategies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/agency-practices/445/iswg-tools</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/agency-practices/446/iswg-case-studies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/crosswalk</loc> <lastmod>2022-01-20T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1959/broadloom-carpet</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1960/carpet-tile</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1961/ceramic-tile</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1962/linoleum</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1963/vinyl-flooring</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1964/wood-flooring</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1965/concrete-flooring</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1966/rubber-flooring</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1967/fluid-applied</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1968/cork</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1969/bamboo</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1970/cut-natural-stone</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1971/terrazzo</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1974/dry-erase-wall-panels</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1975/millwork-panels</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1978/drywall</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1979/demountable-partitions</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1980/linoleum-base</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1981/vinyl-base</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1982/wood-bamboo-base</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1983/ceiling-tile</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1984/gypsum-board</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1985/metal-systems</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1986/wood</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1987/open-ceiling</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1988/incandescent</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1989/overhead-direct-indirect</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1990/direct-lighting</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1992/task-lighting</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1993/occupant-sensor</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1995/manual-light-switch</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1996/timer</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1997/overhead-air-distribution</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1998/floor-air-distribution</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/1999/thermostat</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2000/sound-boots</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2005/vinyl-frame</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2006/fiberglass-frame</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2007/fiberglass</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2008/glass---single-pane</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2009/glass---multi-pane</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2010/glass---low-emissivity</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2012/shades</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2013/blinds</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2014/interior-light-shelves</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2015/clerestory-window</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2016/skylights-solar-tubes</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2017/composite-wood</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2018/alternative-bio-based-composite</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2019/solid-wood</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2020/metal</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2021/glass</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2022/conventional-toilets</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2023/pressure-assisted-toilets</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2029/low-flow-faucet</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2030/metering-sensor-operated</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2031/conventional-shower</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2032/low-flow-shower</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2033/floor-mounted</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2034/ceiling-hung-partitions</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2036/kitchen-appliances</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2037/filtration-system</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2038/low-flow-faucet</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2039/copy-equipment</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2040/equipment</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2043/seating</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2044/desk</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2045/casework-millwork</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2046/composite-wood-furniture</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2047/metal-furniture</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2048/wood-bamboo-furniture</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2050/concrete</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2051/paper-composite</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2052/natural-stone</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2053/laminate</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2054/entrance-mats</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2055/plants-planters</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2101/paints-coatings</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2102/wall-covering</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2103/interior-glazing</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2104/wood-base</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2105/decorative-accent-lighting</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2106/daylight-controls</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2107/sound-masking</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2108/steel-frame</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2109/aluminum-frame</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2110/wood-frame</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2111/glass---tinted-colored-fritted</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2112/dual-flush-toilets</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2113/composting-toilets</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2114/conventional-urinal</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2115/low-flow-urinal</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2116/waterless-urinal</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2117/toilet-shower-accessories</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2118/video-conferencing</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2119/recycling-containers</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2120/lighting-control-software</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2121/wall-tile</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2122/porcelain-tile</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2123/storefront-curtainwall-assemblies</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2124/ceiling-fans</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2125/fabrics-upholstery</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2126/electronic-waste</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2127/compost</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2128/frozen-yogurt</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2129/reach-refrigeration</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2130/salad-bar</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2131/hot-pre-made-food-pick</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2132/hot-order-food</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2133/soup-station</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2134/deep-fryer</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2135/gas-burner</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2136/grill-griddle</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2138/oven</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2139/oven-grill-cleaners</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2140/pasta-cooker</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2141/cool-food-prep-area</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2142/freezer</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2143/refrigerator</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2144/dish-washing-products</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2145/dish-washing-station</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2146/food-washing-station</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2147/handwashing-sink</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2148/skylights-solar-tubes</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2149/dry-storage</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2150/hot-food-holding-cabinets</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2151/counter-refrigeration</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2152/paper-towel-hand-drying</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2153/toilet-partitions</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2154/systems-furniture</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2155/task-seating</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2156/kitchen-exhaust-hoods</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2157/conventional-faucet</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2158/high-efficiency-faucet</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2159/high-efficiency-shower</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2160/high-efficiency-toilets</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2161/high-efficiency-urinal-heu</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2162/low-flow-toilets</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2164/manual-control</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2165/automatic-low-power-state</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2166/schedule-timer-control-device</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2167/load-sensing-control-device</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2168/occupancy-control-device</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2169/manual-on-vacancy-off-control-device</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2170/bio-based-tile</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2171/solid-surface</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2172/engineered-stone</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2173/stainless-steel</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2174/perimeter-units</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2175/fluorescent-including-cfl</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2176/led</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/material/2177/air-hand-drying</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/250/keys-success</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/261/integrative-design-process</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/263/project-guidance</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/264/materials-furniture-furnishings-replacement</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/265/space-reconfiguration-renovation-projects</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/266/10000-sf-interiors-gut-rehab-project</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/267/building-systems-upgrades</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/268/building-operations-maintenance-services</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/399/life-cycle-perspective-life-cycle-thinking</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/400/life-cycle-assessment</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/401/conducting-life-cycle-assessment</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/402/environmental-product-declarations-epds</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/403/life-cycle-assessment-buildings</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/419/acquisition-life-cycle-tools</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/420/net-energy</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/421/transformation-net-energy</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/422/net-examples</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/423/additional-resources</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/procure/about/545/responsible-business-conduct</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/583/collaborative-strategies-project-teams</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/584/project-executive</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/585/project-manager</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/586/project-team</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/587/contracting-officer-procurement-professional</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/628/lca-building-standards-certification-systems</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/629/lca</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/630/lca-key-terms</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/87/overview</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/submetering</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/submetering/electrical-circuit</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/submetering/electrical---end-device</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/submetering/electrical-system</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/submetering/gas</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/submetering/water</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/upgrades</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/upgrades/faq</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/upgrades/selections</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/teach</loc> <lastmod>2021-07-30T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/589</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/589?fmi-program-updates</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/589?slug=fmi-program-updates</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/590</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/590?slug=industry-linksknowledge-portalswhite-papers</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/591</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/591?slug=federal-government-linksknowledge-portalspublications</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/592</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/592?slug=university-college-resource-links</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/596</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/596?slug=fmi-courses-reviewed-public-comment</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/612</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/612?slug=accelerate-fm-user-manual-training-guide</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/615</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/615?slug=professional-facility-management-institute-profmi-holmes-corporation</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/637</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/637?slug=korn-ferry</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/tws</loc> <lastmod>2021-07-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/plan/408/green-teams</loc> <lastmod>2021-08-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/642/doe-greenspace-award</loc> <lastmod>2021-09-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/643/health-enhancing-strategies</loc> <lastmod>2021-09-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/644/greenhouse-gas-accounting</loc> <lastmod>2021-12-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/645/healthy-cleaning</loc> <lastmod>2021-12-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/GRScrosswalk</loc> <lastmod>2022-01-29T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/649</loc> <lastmod>2022-02-14T21:00:00+00:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/650</loc> <lastmod>2022-04-05T10:17:39-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/train/about/651</loc> <lastmod>2022-04-25T09:54:39-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/procure/about/671/acquisition-life-cycle-tools</loc> <lastmod>2022-09-27T13:21:46-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/653</loc> <lastmod>2023-06-09T15:44:28-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/657</loc> <lastmod>2023-08-10T01:53:08-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/658</loc> <lastmod>2023-08-10T01:53:12-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/659</loc> <lastmod>2023-08-10T01:53:15-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/learn/about/666/electric-vehicles-electric-vehicle-supply-equipment</loc> <lastmod>2023-09-25T17:04:40-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Solid_Waste_Management_in_the_Home_Office.pdf</loc> <lastmod>2024-03-08T08:46:22-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Improving_Energy_Efficiency_of_the_Home_Office.pdf</loc> <lastmod>2024-03-08T08:46:26-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/SA-DOE-GreenBuyAwdGuide-FY2024.pdf</loc> <lastmod>2024-03-08T08:48:48-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1.00</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/EEPP Overview for ISWG_20240222.pdf</loc> <lastmod>2024-03-08T08:49:03-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/EPA Draft Label Program for Low Embodied Carbon Construction Materials_ISWG_20240222.pdf</loc> <lastmod>2024-03-08T08:49:27-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/TH and Re-tuning_ISWG_20240222.pdf</loc> <lastmod>2024-03-08T08:49:37-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/SCEP Overview_ISWG_May2023.pdf</loc> <lastmod>2024-03-08T08:49:56-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/AFFECT BIL FAC Presentation_ISWG May 2023.pdf </loc> <lastmod>2024-03-08T08:50:09-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/Sielcken Denver Fed Ctr - ISWG 3-16-23 .pdf</loc> <lastmod>2024-03-08T08:50:21-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/DOE-GreenBuyAwdGuide-FY2023.docx</loc> <lastmod>2024-03-08T08:50:32-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/DHS Climate-Energy-Sustainability_ISWG 032023.pdf</loc> <lastmod>2024-03-08T08:50:49-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/EPA's IRA Low Embodied Carbon Efforts -Bennett, Oct 2023.pdf</loc> <lastmod>2024-03-08T08:50:59-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/FBPTA Competencies Model update - 5.30.2023.xlsx</loc> <lastmod>2024-03-08T08:51:14-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/FBPTA Update (5.8.2023).pdf</loc> <lastmod>2024-03-08T08:51:25-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/ISWG May 2023 FEMP Announcement v2.pdf</loc> <lastmod>2024-03-08T08:51:36-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-tools/October FEMP Announcements-Armwood.pdf</loc> <lastmod>2024-03-08T08:51:52-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/FMI SUBMISSION - IFMA SFP 2023 (Public Comment).xlsm</loc> <lastmod>2024-03-08T08:52:09-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/4 - Grid and Transmission Federal Funding Opportunities.pdf</loc> <lastmod>2024-03-08T08:53:04-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/12-07-23_Green Building Advisory Committee's Federal Building Decarbonization Advice Letter.pdf</loc> <lastmod>2024-03-08T08:56:24-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/John Kliem GSA Reagan Building Decarbonization Electrification Case Study.pdf</loc> <lastmod>2024-03-08T08:56:35-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/12-07-23_ ISWG - LED and Controls Guidance for Federal Agencies.pdf</loc> <lastmod>2024-03-08T08:56:45-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/3 - ISWG 1.26.23 Sotos slide.pdf</loc> <lastmod>2024-03-08T08:56:56-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/2 - NZL_ISWG_Briefing_01242023.pdf</loc> <lastmod>2024-03-08T08:57:07-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/SFTool Brief Template_01-2023.pptx</loc> <lastmod>2024-03-08T08:57:21-06:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/learn/about/668/green-building-certification-systems</loc> <lastmod>2024-07-03T00:47:51-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG Agency Metering Plan Summary Metering Connectivity EMIS_04-11-2024.pdf</loc> <lastmod>2024-07-08T12:42:48-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-case-studies/ASHRAE HQ Building Case Study June ISWG.pdf</loc> <lastmod>2024-07-08T13:39:40-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Clean Energy Rule Update June ISWG.pdf</loc> <lastmod>2024-07-08T13:40:54-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Decarbonization Audits June ISWG.pdf</loc> <lastmod>2024-07-08T13:41:13-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Climate Risk Management Guidance and Template_04-18-2024.pdf</loc> <lastmod>2024-07-08T13:42:17-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Inventory-Wide Approach to Building Decarbonization ISWG June.pdf</loc> <lastmod>2024-07-08T13:42:57-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/ISWG Engagement Strategy for the Future_04-11-2024.pdf</loc> <lastmod>2024-07-08T13:43:13-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Iswg/iswg-policies-strategies/Briefing_Sustainable Practices for PC_Murrell_04-11-2024.pdf</loc> <lastmod>2024-07-08T13:43:38-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url> <loc>https://sftool.gov/Content/attachments/Promote_Health_Comfort_And_Performance_While_Working_From_Home.pdf</loc> <lastmod>2024-08-09T13:54:08-05:00</lastmod> <changefreq>daily</changefreq>
<priority>1</priority> </url> <url><loc>https://sftool.gov/procure/about/681/procurement-topics</loc></url></urlset>"""

locs = re.compile(r"<loc>(.*?)</loc>")

urls = locs.findall(xml_2)

print(urls[999])

locs = re.compile(r"<loc>(.*?)</loc>")

print(locs[:5])

links = check_link(locs)

print(links)

with open('sftool_links.csv', 'w', newline='') as f:
    writer = writer(f)
    writer.writerow(['URL','Status'])
    writer.writerows(links)
    f.close()
    print('done, written to csv!')