from selenium import webdriver

browser = webdriver.Firefox()
webdriver.Firefox()
browser.get("http://localhost:8000")

assert "Django" in browser.title