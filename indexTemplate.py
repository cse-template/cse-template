from string import Template
import json
from userFunctions import head
  
# Opening JSON file
websiteData = json.loads(open("website-settings.json").read())

headerHtml = head("misc")

title = websiteData["Global Class Name"]

copyright = """<div class="copyright">"""
copyright += "Copyright © " + websiteData["Copyright Year"] + " " + websiteData["Copyright Name"] + "<br>"
copyright += """<a style= "color:white;" href="feedback.html">Feedback</a></div>"""

#open indexTemplate html file and read it into a string 
unitTemplate = open("indexTemplate.html", "r")
templateString = Template(unitTemplate.read())

#substitute settings data with appropriate variables 
result = templateString.safe_substitute(
    head = headerHtml,
    mainTitle = title,
    copyrightFooter = copyright
)


resultFile = open("generated/website/index.html", "w")
resultFile.write(result)
resultFile.close()

