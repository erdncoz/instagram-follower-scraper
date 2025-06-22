
from know_user import username,password
from playwright import * 
from playwright.sync_api import sync_playwright

class instagram():
    def __init__(self,username,password):
        self.username=username
        self.password=password
    def entrance(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=True)
        self.page = self.browser.new_page()
        self.page.goto(f"https://www.instagram.com")
        self.page.locator('[name="username"]').fill(self.username)
        self.page.locator('[name="password"]').fill(self.password)

        self.page.keyboard.press("Enter")
        
       
        self.page.get_by_role("link", name=self.username).first.click()

    
        self.page.wait_for_selector('a[href*="following"]')
        self.page.locator('a[href*="following"]').click()
        self.name=input("Target User Account:")
        try:
          self.page.get_by_placeholder("Ara").fill(self.name)
          self.page.wait_for_timeout(3000)  
       
          self.page.locator(f'//span[text()="{self.name}"]').first.click()
        except:
            print("User Not Found")

    
        followers = self.page.locator('ul > li:nth-child(2)').first.text_content()

        following=self.page.locator('ul>li:nth-child(3)').first.text_content()

        print(f"Followers: {followers}")
        print(f"Following:{following}")
        self.browser.close()
        
ins=instagram(username,password)
ins.entrance()

