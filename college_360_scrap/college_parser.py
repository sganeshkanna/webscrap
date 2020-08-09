from bs4 import BeautifulSoup
import requests
import course_parser
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

class College:
  def __init__(self, name, courses):
    self.name = name
    self.courses = courses



def parse_colleges(url_):
    testCount = 0
    # print("parse_colleges")
    req = requests.get(url_,headers)
    soup = BeautifulSoup(req.content, 'html.parser')
    inputs = soup.find_all('input')
    colleges = []
    for input in inputs:
        if input.has_attr('class') and input['class'][0] == 'compareCollege':
            # print(input)
            name = input.get('name')
            print(name)
            parentdiv = input.find_parent('div').find_parent('div')
            courseClass = parentdiv.find("div", class_="course")
            allRef = courseClass.find_all('a')
            try:
                url_ = allRef[1].get('href')
                courses_list = course_parser.parse_courses(url_)
                print(courses_list)
                college = College(name,courses_list)
                colleges.append(college)
                testCount = testCount+1
                if testCount == 5:
                    break
            except:
                print("No Second URL")
            # print(parentdiv)
    return colleges
