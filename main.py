import bs4
from urllib.request import urlopen as urlReq
from bs4 import BeautifulSoup as bSoup

flip_url = 'https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_3_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_3_7_na_na_na&as-pos=3&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=3ce158b5-e07c-46b0-b18f-a727831d42c4&as-searchtext=laptop'

uClient = urlReq(flip_url)
html_page = uClient.read()
uClient.close()

soup_page = bSoup(html_page, "html.parser")

containers = soup_page.findAll("div" , {"class":"_1-2Iqu row"})

filename = "laptops.csv"
f = open(filename, "w")

headers = "Model, Processor, RAM, ROM, Display, Price\n"

f.write(headers)

for container in containers:
    model_name = container.findAll("div", {"class":"_3wU53n"})
    model = model_name[0].text

    price_container = container.findAll("div", {"class": "_1vC4OE _2rQ-NK"})
    price = price_container[0].text

    content = container.findAll("li" , {"class":"tVe95H"})
    processor = content[0].text
    ram = content[1].text
    rom = content[3].text
    display = content[4].text

    print("Model - "+model)
    print("Processor - "+processor)
    print("RAM - "+ram)
    print("HDD/SSD - "+rom)
    print("Screen Size - "+display)
    print("Price - "+price)

    prices = price.replace("," , "")

    f.write(model+ "," + processor + ","  + ram + "," + rom + "," + display + "," + prices.replace("\u20b9", "Rs.") +"\n")

f.close()