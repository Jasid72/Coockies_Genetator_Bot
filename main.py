from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Oppening the Website
driver = webdriver.Chrome()
driver.get("https://orteil.dashnet.org/experiments/cookie/")


#Time-out
current_time = time.time() + 5
time_out = time.time() + 10 * 5

#Store Item
store = driver.find_element(By.ID, "store")
items = store.text.split('\n')
item_list = []


#Functions of Store Products
def Time_Machine():
    Tm = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b').text.replace("Time machine - ", "").replace(",", "")
    return int(Tm)

def Portal():
    portal = driver.find_element(By.XPATH, '//*[@id="buyPortal"]/b').text.replace("Portal - ", "").replace(",", "")
    return int(portal)

def Alchemy_Lab():
    Al = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b').text.replace("Alchemy lab - ", "").replace(",", "")
    return int(Al)

def Shipment():
    ship = driver.find_element(By.XPATH, '//*[@id="buyShipment"]/b').text.replace("Shipment - ", "").replace(",", "")
    return int(ship)

def Mine():
    mine = driver.find_element(By.XPATH, '//*[@id="buyMine"]/b').text.replace("Mine - ", "").replace(",", "")
    return int(mine)

def Factory():
    factory = driver.find_element(By.XPATH, '//*[@id="buyFactory"]/b').text.replace("Factory - ", "").replace(",", "")
    return int(factory)

def Grandma():
    grandma = driver.find_element(By.XPATH, '//*[@id="buyGrandma"]/b').text.replace("Grandma - ", "").replace(",", "")
    return int(grandma)

def Cursor():
    cursor = driver.find_element(By.XPATH, '//*[@id="buyCursor"]/b').text.replace("Cursor - ","").replace(",","")
    return int(cursor)

# Click Infinite Time on Cookie
condition_meet = False
while not condition_meet:
#Display The amount

    for item in range(0, len(items), 2):
        part = items[item]
        name, price = part.split(' - ')
        price = int(price.replace(',','').strip())
        item_list.append({"Name": name.strip(), "Price": price})

    if time.time() >= time_out:
        amount = driver.find_element(By.ID, "money").text.replace(",", '')
        money = int(amount)

        if money >= Time_Machine():
            click_Tm = driver.find_element(By.ID, "buyTime machine")
            click_Tm.click()

        elif money >= Portal():
            portal = driver.find_element(By.ID, "buyPortal")
            portal.click()

        elif money >= Alchemy_Lab():
            lab = driver.find_element(By.ID, "buyAlchemy lab")
            lab.click()

        elif money >= Shipment():
            ship = driver.find_element(By.ID, "buyShipment")
            ship.click()

        elif money >= Mine():
            mine = driver.find_element(By.ID, "buyMine")
            mine.click()

        elif money >= Factory():
            factory = driver.find_element(By.ID, "buyFactory")
            factory.click()

        elif money >= Grandma():
            grandma = driver.find_element(By.ID, "buyGrandma")
            grandma.click()

        else:
            cursor = driver.find_element(By.ID, "buyCursor")
            cursor.click()

    cookie_click = driver.find_element(By.ID, "cookie")
    cookie_click.click()



#time.sleep(50)
driver.close()