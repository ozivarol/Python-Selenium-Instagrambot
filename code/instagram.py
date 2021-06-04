from selenium.webdriver.common import keys
from InstagramUserInfo import id,password,user
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
 
class Instagram:
    def __init__(self,id,password):
        self.browser=webdriver.Chrome()
        self.browser.set_window_size(1920,1080)
        self.browser.maximize_window()
        self.id=id
        self.followers=[]
        self.follow = []
        self.dif=[]
        
        self.password=password
    def logIn(self):
        
        self.browser.get("https://www.instagram.com/")
        
        time.sleep(2)
        id=self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input").send_keys(self.id)
        password=self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input").send_keys(self.password)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]").click()
        time.sleep(4)
    def searchUser(self,user):
        self.user=user
        self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(self.user)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(Keys.ENTER)
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]").click()
        time.sleep(2)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
    def getFollowers(self):
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a").click()
        
        time.sleep(3)
        c.scrollDown()
        sayac=0
        followers= self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
        for user in followers:
            link = user.find_element_by_css_selector(".FPmhX.notranslate._0imsa").text
            self.followers.append(link)
            sayac+=1
        print(self.followers)    
            
        print("toplam = "+str(sayac)+"takipçi")
            
    def scrollDown(self):
	    jsKomut = """
		sayfa = document.querySelector(".isgrP");
		sayfa.scrollTo(0,sayfa.scrollHeight);
		var sayfaSonu = sayfa.scrollHeight;
		return sayfaSonu;
		"""
	    sayfaSonu = self.browser.execute_script(jsKomut)
	    while True:
		    son = sayfaSonu 
		    time.sleep(1)
		    sayfaSonu = self.browser.execute_script(jsKomut)
		    if son == sayfaSonu:
			    break        
    
    def getFollow(self):
        self.browser.refresh()
        time.sleep(3)
        self.browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[3]/a").click()
        time.sleep(3)
        c.scrollDown()
        follows= self.browser.find_element_by_css_selector("div[role=dialog] ul").find_elements_by_css_selector("li")
        sayac=0
        for user in follows:
            link = user.find_element_by_css_selector(".FPmhX.notranslate._0imsa").text
            self.follow.append(link)
            sayac+=1
        print(self.follow)
        print("toplam = "+str(sayac)+"takip edilen")
    def diffrence(self):
        s=set(self.followers)
        self.diffrence = [x for x in self.follow if x not in s]
        print(self.diffrence)
        print(str(len(self.diffrence))+"kişi seni takip etmiyor")
    def close(self):
        self.browser.close()  






        
           

       
        
        
        

       


c=Instagram(id,password)


c.logIn()
c.searchUser(user)
c.getFollowers()
c.getFollow()
c.diffrence()
c.close()
