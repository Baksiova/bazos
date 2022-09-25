import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By


from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))




def site():
    driver.get ('https://www.bazos.cz/')
    print(driver.current_url)
    driver.find_element(By.ID, 'hledat').send_keys("sony wh-1000xm")
    driver.find_element(By.XPATH, '//*[@id="formt"]/div/div/b/input[4]').click()

    containers = driver.find_elements(By.XPATH,('.//div[@class="inzeraty inzeratyflex"]'))

    for item in containers:
        name1= item.find_element(By.XPATH,".//div[@class='inzeratynadpis']/span[@class='velikost10']")
        name = item.find_element(By.XPATH,'.//div[@class="inzeratynadpis"]')

        if "10. 2022" or "11. 2022" in name1.text:
            print(item.text)



    driver.close()


print(site())
