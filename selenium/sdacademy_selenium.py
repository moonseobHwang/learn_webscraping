from pymongo import MongoClient
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

path = '/Users/sanghunoh/Documents/Develop/chromedriver'
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--no-sandbox')
# chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(path, chrome_options=chrome_options)

# login
driver.get('http://sdacademy.maniaro.com/teacher/index.php')
driver.implicitly_wait(5)
username = 'user name'
userpw = 'user password'
driver.find_element_by_name('strUid').send_keys(username)
driver.find_element_by_name('strPassword').send_keys(userpw)
driver.find_element_by_xpath("//input[@type='submit']").click()
driver.implicitly_wait(5)

# 비즈니스 모델을 활용한 빅데이터 분석 전문가 양성과정 (1회차)
driver.get(
    'http://sdacademy.maniaro.com/teacher/curri/ver5/lecture/index.php?Pcode=1')
driver.implicitly_wait(5)
trs = driver.find_elements_by_xpath("//tr[@class='link_yellow text-c']")

# connect MongoDB
client = MongoClient('mongodb://192.168.0.6:27017/')
# if ("sdacademydb" not in client.database_names()):
sdacademydb = client['sdacademydb']						# get Database

# check collections
if ("charters" not in sdacademydb.list_collection_names()):
    sdacademydb.create_collection('charters')
if ("meetings" not in sdacademydb.list_collection_names()):
    sdacademydb.create_collection('meetings')
if ("clientevaluates" not in sdacademydb.list_collection_names()):
    sdacademydb.create_collection('clientevaluates')
if ("answers" not in sdacademydb.list_collection_names()):
    sdacademydb.create_collection('answers')
if ("questions" not in sdacademydb.list_collection_names()):
    sdacademydb.create_collection('questions')

from itertools import product
from selenium.common.exceptions import NoSuchElementException

for i in range(len(trs)-1):     # without final project
    # charters page
    charterlist = driver.find_elements_by_xpath(
        "//tr[@class='link_yellow text-c']")[i]
    # print(charterlist.get_attribute('innerHTML'))
    source = charterlist.get_attribute('innerHTML')
    soup = BeautifulSoup(source, 'lxml')
    charter = soup.findAll('td')
    data = {'charter': charter[0].text, 'evaluteway': charter[1].text, 'lecturer': charter[2].text, 'startdate': charter[3].text,
            'enddate': charter[4].text, 'evaldate': charter[5].text, 'missdate': charter[6].text, 'reevaldate': charter[7].text, 'mean': charter[9].text}
    charters_infor = sdacademydb.charters.insert(data)

    charter_click = driver.find_elements_by_xpath(
        "//a[@class='button button-blue']")[i].click()
    driver.implicitly_wait(5)

    # 분석회의록 page
    driver.find_elements_by_xpath("//li[@class='floatL tab_off']")[0].click()
    driver.implicitly_wait(5)
    els = driver.find_elements_by_xpath(
        "//td[@class='body_center']/table/tbody/tr[@class='b_fff']/td")
    # print(meeting[1].text)
    data = {'meetdate': els[1].text,
            'content': els[3].text, 'detail': els[5].text, 'charter_objectid':charters_infor}
    meeting_infor = sdacademydb.meetings.insert(data)
    driver.back()   # evaluate main page

    # evaluate list page
    evaluate_list = driver.find_elements_by_xpath(
        "//li[@class='floatL tab_off']")[1]
    # print(evaluate_list.text)
    comparedstr = evaluate_list.text
    evaluate_list.click()
    driver.implicitly_wait(5)

    if comparedstr != '구두발표':
        # client anwser
        print('start client anwser')
        anwsersclick = driver.find_elements_by_xpath("//td[@class='b1 p10']/a/span[contains(@class,'f20')]")
        for k in range(len(anwsersclick)):
            driver.find_elements_by_xpath("//td[@class='b1 p10']/a/span[contains(@class,'f20')]")[k].click()
            driver.implicitly_wait(5)

            # clientevaluates
            clientname = driver.find_elements_by_xpath('//table[@class="mb10"]//tr[@class="b_fff"]/td[@class="b1 p10"]')[3].text
            evaluatecontent = ''
            try:
                evaluatecontent = driver.find_element_by_xpath("//textarea").text
            except NoSuchElementException as identifier:
                pass

            print(clientname, evaluatecontent)
            data = {'clientname': clientname, 'evaluatecontent': evaluatecontent, 'charter_objectid':charters_infor}
            client_infor = sdacademydb.clientevaluates.insert(data)

            evaluatelist = driver.find_elements_by_xpath("//tr[@class='link_yellow text-c cur']")
            scorelist = ''
            if comparedstr == '평가자체크리스트':
                scorelist = driver.find_elements_by_xpath("//td[@class='b1 p10 f20 fb arial']")
                
            answerlist = driver.find_elements_by_xpath("//tr[@class='b_darkgray']/td/div")

            for evaluate, answer, score in zip(evaluatelist, answerlist, scorelist):
                els = evaluate.find_elements_by_tag_name("td")
                evaluatescore = ''
                if comparedstr != '평가자체크리스트':
                    evaluatescore = els[4].find_element_by_tag_name("input").get_attribute("value")
                else :
                    evaluatescore = score.find_element_by_tag_name("input").get_attribute("value")
                    
                source = answer.get_attribute('innerHTML')
                soup = BeautifulSoup(source, 'html.parser')
                subels = soup.select('tr.b_fff>td.b1.p10')

                data = {'number': els[0].text, 'evaluatescore': evaluatescore,
                'answer': subels[5].text, 'client_infor':client_infor, 'charter_objectid':charters_infor}
                evaluate_infor = sdacademydb.answers.insert(data)

            driver.back()
        print('end client anwser')

        # evaluate question page
        driver.find_element_by_xpath("//a[@class='button button-blue']").click()
        driver.implicitly_wait(5)
        questionsclick = driver.find_elements_by_xpath("//td[@colspan='4']/div/p[contains(@class,'floatL')]")
        for j in range(len(questionsclick)):     # without final project
            questionelement = driver.find_elements_by_xpath("//td[@colspan='4']/div/p[contains(@class,'floatL')]")[j]
            sortofquestion = questionelement.text
            print(charter[0].text, questionelement.text)
            questionelement.click()
            # questions and standard answer
            questionlist = driver.find_elements_by_xpath(
                "//tr[@class='link_yellow text-c cur']")
            standardanswerlist = driver.find_elements_by_xpath("//tr[@class='b_darkgray']/td/div")

            for question, standardanswer in product(questionlist, standardanswerlist):
                els = question.find_elements_by_tag_name("td")
                source = standardanswer.get_attribute('innerHTML')
                soup = BeautifulSoup(source, 'html.parser')
                subels = soup.select('tr.b_fff.text-l>td')

                data = {'sortofquestion':sortofquestion,'number': els[1].text, 'question': els[2].text, 'score': els[3].text,
                'standardanswer': subels[3].text, 'standard': subels[5].text, 'charter_objectid':charters_infor}
                question_infor = sdacademydb.questions.insert(data)

    driver.find_elements_by_xpath("//a[@class='button button-black']")[1].click() # charters page
    driver.implicitly_wait(5)
    print('charter End!')

client.close()
driver.quit()
print('The End!')
