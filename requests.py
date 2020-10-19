from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import re

def crawPttMonkeysSaleTicketPage(date, seatDirection = '', seatArea = 'E', pushTag = '售'):
    url = "https://www.ptt.cc/bbs/Monkeys/M.1534603045.A.FFC.html"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urlopen(req).read().decode('utf-8')
    #print(html)
    soup = BeautifulSoup(html, features='lxml')
    pushDivs = soup.findAll("div", {"class": "push"})
    for eachDiv in pushDivs:
        idSpan = eachDiv.find("span", {"class": "f3 hl push-userid"})
        contentSpan = eachDiv.find("span", {"class": "f3 push-content"})
        dateSpan = eachDiv.find("span", {"class": "push-ipdatetime"})
        
        if re.search(r"[[" + pushTag + "]]", contentSpan.get_text()):
            if re.search(r"" + date +"", contentSpan.get_text()):
                if re.search(r"" + seatDirection + "", contentSpan.get_text()):
                    if re.search(r"[" + seatArea + "]", contentSpan.get_text()):
                        print(idSpan.get_text()+"|"+contentSpan.get_text()+"|"+dateSpan.get_text())