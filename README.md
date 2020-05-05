---
## SECTION 1 : PROJECT TITLE
### News Bias Scoring System
<img width="812" alt="start_screen" src="https://github.com/SB1308/NBSS/blob/master/NBSS_Cover.jpg">

---
## SECTION 2 : EXECUTIVE SUMMARY / PAPER ABSTRACT
30 years ago, evening newscasts on Channel 8 and Channel 5 gave straightforward accounts of the day’s events, and the morning newspapers provide the hardcopy version of the news which told us what happened while we slept. Fast forward to today, we are constantly bombarded by information from multiple social media ( Facebook, Twitter, Instagram) which most would read them with a pinch of salt. Instead, we often rely on the mainstream news channels ( e.g. CNA, BBC ABC websites) as our source of truth to understand what is really happening around us.  
The mainstream news media often agree on the basic facts of a story. But they may still disagree on what people should think about them. This is because while the facts are clear, their implications are murky — hence it can be entirely legitimate for two articles to take utterly opposing views on the same story. A recent media bias chart in 2018 by Pew Research Centre revealed that even main stream media could be highly biased. 
Our project team would like to build a system that could compute the Neutrality Score for the coverage of that story as an additional dimension for the user.  Using the techniques imparted to us in lectures, our group first use the RPA tool UIpath to automate the scrapping of news from the mainstream news websites. We then develop an intelligent system using NLP and machine learning techniques to group them into related stories, then further analyse those groups to attempt to produce a metric for how well the set of articles covers multiple perspectives on the story.
Our team had an exciting time working on this project and hope to share our insights with everyone. Sentimental score analysis is more of an art than science and we only wish there was more time to work on the scope and scale of the project. 
  

---
## SECTION 3 : CREDITS / PROJECT CONTRIBUTION

| Official Full Name  | Student ID (MTech Applicable)  | Work Items (Who Did What) | Email (Optional) |
| :------------ |:---------------:| :-----| :-----|
| LIM CHONG SENG HERMANN  | A0195392U | Business idea generation, Web scraping UiPath robot, Powerpoint development and presentation, Project report, Project video | e0385023@u.nus.edu |
| YEO WHYE CHUNG NELSON | A0195405A | Business idea generation, Built the web application server and frontend, Developed the Google NLP interaction, Project video |  |
| KOH SOOK BING | A0195413E | Exploration of the python scripts for the News Bias Scoring System.   Project report write up. Develop powerpoint for the video.  |  |

---
## SECTION 4 : VIDEO OF SYSTEM MODELLING & USE CASE DEMO

https://drive.google.com/open?id=13KbkDhLXiejHGkEY79J_9Zz_xl15xI8l

---
## SECTION 5 : INSTALLATION AND USER GUIDE

The following steps must be taken during installation of the system on a different machine:
-	Each time a UIPath robot is deployed into a different environment, new authentication keys and tokens must be generated from the UIPath Cloud Orchestrator website. The detailed instructions can be found in the UIPath API guide (https://docs.uipath.com/orchestrator/reference/consuming-cloud-api). Namely, the settings.json file in the web app’s folder must be updated with the new User Key, Account Logical Name, Tenant Logical Name, and Client Id
-	After deployment, make sure the UIPath Robot/Assistant is launched, has successfully connected to the Orchestrator server and the robot has been downloaded
-	The web app’s folder (SLS_Proj1_SANA) must be transferred to the root directory of C: drive, due to the use of absolute paths in the configuration of the system. Relative pathing can be done as possible future improvements to the system code
-	Make sure Python 3.7 is installed and that it has been added to the Path system environmental variable
-	Enter the following commands into a command prompt:
-	C:/SLS_Proj1_SANA/venv/Scripts/activate
-	cd C:/SLS_Proj1_SANA
-	python main.py
-	The web app will launch, and the robot should start scheduled scraping within a minute
-	The web page can now be accessed at localhost:5000

---
## SECTION 6 : PROJECT REPORT / PAPER
https://github.com/SB1308/ISA-IPA-2019-01-19-IS01PT-GRP-NBSS/blob/master/Report.docx

