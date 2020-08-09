from bs4 import BeautifulSoup
import requests
import argparse
import csv
from datetime import datetime

import college_parser



ap = argparse.ArgumentParser()
ap.add_argument("-u", "--URL", required=True,
	help="End Point of the List")
args = vars(ap.parse_args())
url = args["URL"]#"https://engineering.careers360.com/colleges/list-of-engineering-colleges-in-tamil-nadu"
dateTimeObj = datetime.now()
filename = "Collecge_List_%s.csv" % dateTimeObj
filename = filename.replace(" ","").replace(":","_")
print(filename)
colleges = college_parser.parse_colleges(url)
with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([ "College Name", "Course"])
    for college in colleges:
        writer.writerow([college.name, ""])
        for course in college.courses:
            writer.writerow(["",course])

# for college in colleges:
#     print(college.name)
#     print(college.courses)
#     print("#############")

print("Data Uploaded into %s",filename)
# headers = {
#     'Access-Control-Allow-Origin': '*',
#     'Access-Control-Allow-Methods': 'GET',
#     'Access-Control-Allow-Headers': 'Content-Type',
#     'Access-Control-Max-Age': '3600',
#     'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
#     }
# testCount = 0
# req = requests.get(url)
# soup = BeautifulSoup(req.content, 'html.parser')
# inputs = soup.find_all('input')
# for input in inputs:
#     if input.has_attr('class') and input['class'][0] == 'compareCollege':
#         # print(input)
#         name = input.get('name')
#         print(name)
#         parentdiv = input.find_parent('div').find_parent('div')
#         courseClass = parentdiv.find("div", class_="course")
#         allRef = courseClass.find_all('a')
#         try:
#             url_ = allRef[1].get('href')
#             courses_list = course_parser.parse_courses(url_)
#             print(courses_list)
#             testCount = testCount+1
#             if testCount == 5:
#                 break
#         except:
#             print("No Second URL")
#         # print(parentdiv)
#         print("#####################")


# College Name Tree structure for Parsing
# 11626 - 12252
# mainContainer (div)
# 	facetMain sectionLayout grayBg cardBlks (section)
# 		container (div)
# 			row (div)
# 				contentPart listingData (div)
# 					allData (div)
# 						facetContent (div)
# 							cardBlk featured (div)
# 								cardContent (div)
# 									content (div)
# 										applyCompare (div)
# 											control controlCheckbox (label)
# 												compareCollege (input)
