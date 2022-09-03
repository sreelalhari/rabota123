from django.core.management.base import BaseCommand
from selenium import webdriver
import time
from urllib.parse import urljoin
from bs4 import BeautifulSoup
from job_search.models import Job
class Command(BaseCommand):
    help = "collect jobs"
    # define logic of command
    def handle(self, *args, **options):
        for param in range(1,11):
            driver = webdriver.Chrome("C:\Windows\chromedriver.exe")
            URL= "https://in.indeed.com/jobs?q=Data%20science&start={}0".format(param)
            driver.get(URL)

            time.sleep(10)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"html.parser")
            driver.close()
            result = soup.find(id="mosaic-provider-jobcards")
            job_elems = result.find_all("div", class_="job_seen_beacon")    
            for i in job_elems:
                url11 = i.find('a',class_='jcs-JobTitle css-jspxzf eu4oa1w0').get('href')
                url=urljoin(URL,url11)
                title = i.find("h2", class_="jobTitle").text
                company_name=i.find("span", class_="companyName").text
                company_link=''
                ratings_span = i.find('span',class_="ratingNumber")
                if ratings_span is None:
                    ratings='Not available'
                else:
                    ratings=ratings_span.text
                reviews = 'Nill'
                experience=''
                lst=[]
                skill=i.select_one('ul[style="list-style-type:circle;margin-top: 0px;margin-bottom: 0px;padding-left:20px;"]')
                if skill is None:
                    skills='Not Available'
                else:
                    for li in skill.find_all('li'):
                        if li is None:
                            skills='Not available'
                        else:
                            lst.append(li.text)
                skills=', '.join(map(str, lst))
                salary = soup.find("div", class_="attribute_snippet").text
                location = i.find('div',class_='companyLocation').text
                jobhistory=i.find('span',class_="date").text
                posted=jobhistory.replace('Posted','')
                
    
                # check if url in db
                try:
                # save in db
                    Job.objects.create(
                        url=url,
                        title=title,
                        company_link=company_link,
                        company_name=company_name,
                        ratings=ratings,
                        reviews=reviews,
                        experience=experience,
                        salary=salary,
                        location=location,
                        posted=posted,
                        skills=skills
                )

                
                except:
                    print('Exception')
        self.stdout.write( 'job complete' )

        for param in range(1,11):
            driver = webdriver.Chrome("C:\Windows\chromedriver.exe")
            URL= "https://www.naukri.com/data-science-jobs-{}?k=data%20science".format(param)
            driver.get(URL)

            time.sleep(10)
            content = driver.page_source.encode('utf-8').strip()
            soup = BeautifulSoup(content,"html.parser")
            driver.close()
            results=soup.find(class_='list')
            job_elems = results.find_all('article',class_='jobTuple bgWhite br4 mb-8')
            for i in job_elems:
                url = i.find('a',class_='title fw500 ellipsis').get('href')
                title = i.find('a',class_='title fw500 ellipsis').text
                company_link = i.find('a',class_="subTitle ellipsis fleft").get('href')
                company_name = i.find('a',class_="subTitle ellipsis fleft").text
                ratings_span = i.find('span',class_="starRating fleft dot")
                if ratings_span is None:
                    ratings='Not available'
                else:
                    ratings=ratings_span.text

                reviews_span = i.find('a',class_="reviewsCount ml-5 fleft blue-text")
                if reviews_span is None:
                    reviews='Not available'
                else:
                    reviews=reviews_span.text
                Exp = i.find('div',class_="job-description fs12 grey-text")
                if Exp is None:
                    experience='Not Available'
                else:
                    experience=Exp.text
                Sal = i.find('li',class_='fleft grey-text br2 placeHolderLi salary')
                Sal_span = Sal.find('span',class_='ellipsis fleft fs12 lh16')
                if Sal_span is None:
                    salary='Not Available'
                else:
                    salary = Sal_span.text

                Loc = i.find('li',class_='fleft grey-text br2 placeHolderLi location')
                Loc_exp = Loc.find('span',class_='ellipsis fleft fs12 lh16')
                if Loc_exp is None:
                    location='Nil'
                else:
                    location = Loc_exp.text
                Hist = i.find("div",["type br2 fleft grey","type br2 fleft green"])
                Post_Hist = Hist.find('span',class_='fleft fw500')
                if Post_Hist is None:
                    posted='Nil'
                else:
                    posted = Post_Hist.text
                skill=i.find('ul',class_="tags has-description")
                j=[]
                if skill is None:
                    j.append('Info not available')
                else:
                    for li in skill.find_all('li',class_="fleft fs12 grey-text lh16 dot"):
                        if li is None:
                            j.append(' ')
                        else:
                            j.append(li.text)

                skills=' | '.join(map(str, j))
                
    
                # check if url in db
                try:
                # save in db
                    Job.objects.create(
                        url=url,
                        title=title,
                        company_link=company_link,
                        company_name=company_name,
                        ratings=ratings,
                        reviews=reviews,
                        experience=experience,
                        salary=salary,
                        location=location,
                        posted=posted,
                        skills=skills
                )

                
                except:
                    print('Exception')
        self.stdout.write( 'job complete' )
