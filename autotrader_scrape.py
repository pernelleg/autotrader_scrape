# importing libraries
! pip install selenium
from selenium import webdriver
import pandas as pd

#finding the driver and opening it 
driver_path = 'C:\\chromedriver.exe'
driver = webdriver.Chrome(driver_path)

#opening the autotrader website so i can manually remove popups before starting scraping
url = 'https://www.autotrader.co.uk/car-search?postcode=tn132jn&include-delivery-option=on&advertising-location=at_cars&page=1'
driver.get(url)

#getting a list of all the brands
makes = []
j = 1
while True:
    try:
        makes.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[1]/div[1]/form/ul/li[2]/div/div/div/div[2]/button[{j}]/span[1]').text)
        j += 1
    except:
        break
print(makes)    

#making lists for each feature we are collecting
price = []
name = []
year = []
typ = []
mileage = []
engine_size = []
power = []
trans = []
fuel = []

#loop to go through all the brands 
for brand in makes:
    url1 = f'https://www.autotrader.co.uk/car-search?sort=relevance&postcode=tn132jn&radius=1500&make={brand}&include-delivery-option=on&year-to=2023&page=1'
    driver.get(url1)
    #finding the amount of pages for each brand
    pgno = driver.find_element('xpath','/html/body/main/div[1]/section[2]/div/header/nav/ul/li[3]/strong[2]').text
    pgint = int(pgno.replace(',',''))
    
    #loop that goes through either the first 100 pages for each brand or if there are less than 100, then all the pages
    for j in range(1,min(101,pageint)):
        try:
            driver.get(f'https://www.autotrader.co.uk/car-search?sort=relevance&postcode=tn132jn&radius=1500&make=Seat&include-delivery-option=on&year-to=2023&page={j}')
            i = 1
            while True:
                try:
                    try:
                        price.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i}]/article/div/div/div[1]/section[1]/div/div/span').text)
                        name.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i}]/article/div/div/div[1]/section[2]/h3').text)
                        year.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i}]/article/div/div/div[1]/section[2]/ul/li[1]').text)
                        typ.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i}]/article/div/div/div[1]/section[2]/ul/li[2]').text)
                        mileage.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i}]/article/div/div/div[1]/section[2]/ul/li[3]').text)
                        engine_size.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i}]/article/div/div/div[1]/section[2]/ul/li[4]').text)
                        power.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i}]/article/div/div/div[1]/section[2]/ul/li[5]').text)
                        trans.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i}]/article/div/div/div[1]/section[2]/ul/li[6]').text)
                        fuel.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i}]/article/div/div/div[1]/section[2]/ul/li[7]').text)
                        i += 1
                    except: #if there is an advert it will skip one
                        price.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i+1}]/article/div/div/div[1]/section[1]/div/div/span').text)
                        name.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i+1}]/article/div/div/div[1]/section[2]/h3').text)
                        year.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i+1}]/article/div/div/div[1]/section[2]/ul/li[1]').text)
                        typ.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i+1}]/article/div/div/div[1]/section[2]/ul/li[2]').text)
                        mileage.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i+1}]/article/div/div/div[1]/section[2]/ul/li[3]').text)
                        engine_size.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i+1}]/article/div/div/div[1]/section[2]/ul/li[4]').text)
                        power.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i+1}]/article/div/div/div[1]/section[2]/ul/li[5]').text)
                        trans.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i+1}]/article/div/div/div[1]/section[2]/ul/li[6]').text)
                        fuel.append(driver.find_element('xpath',f'/html/body/main/div[1]/section[2]/div/div[2]/ul/li[{i+1}]/article/div/div/div[1]/section[2]/ul/li[7]').text)
                        i += 1
                except: #when it comes to the end of the page the loop will end 
                    break
        except:
            break

        print(j)
        #taking 12 values per page as last val is ad
        price = price[:12*j]
        name = name[:12*j]
        year = year[:12*j]
        typ = typ[:12*j]
        mileage = mileage[:12*j]
        engine_size = engine_size[:12*j]
        power = power[:12*j]
        trans = trans[:12*j]
        fuel = fuel[:12*j]
    

        
#put this all together into a data frame
autotrader = pd.DataFrame({'name':name,
                          'price':price,
                          'year':year,
                          'type':typ,
                          'mileage':mileage,
                          'engine_size':engine_size,
                          'power':power,
                          'transmission':trans,
                          'fueltype':fuel})
print(autotrader)

#cleaning the dataframe
# creating a copy of the dataframe to make changes to
at2 = autotrader.copy()
# splitting up the make and model 
at2['make'] = [str(str(i).split(' ',1)[0]) for i in at['name']]

at2['model'] = [str(str(i).split(' ',1)[-1]) for i in at['name']]

at2.drop('name', axis = 1, inplace = True )

#making year into a number
at2['year'] = [str(i).split(' ',1)[0] for i in at['year']]

#making price into number
at2['price'] = [str(i).replace(',','').replace('£','') for i in at['price']]

#making mileage into a number
at2['mileage'] = [str(i).replace(',','').split(' ')[0] for i in at['mileage']]

#making engine size into a number
at2['engine_size'] = [float(str(i).replace('L','')) for i in at['engine_size']]

#making power into the same unit and into a number
power2 = []
for i in at['power']:
    if 'PS' in str(i):
        power2.append(round(float(str(i).replace('PS',''))*0.986))
    elif 'BHP' in str(i):
        power2.append(round(float(str(i).replace('BHP',''))))
    else:
        power2.append(i)
        
at2['power'] = power2

#export the dataframe as a csv
at2.to_csv('autotrader_clean.csv', index = False)
