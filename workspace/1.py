from selenium import webdriver
import time  
#利用chrome浏览器
# 后面是你的浏览器驱动位置，记得前面加r'','r'是防止字符转义的
driver=webdriver.Chrome(r'chromedriver/chromedriver.exe')    
#打开get到的网址
driver.get("http://www.baidu.com")  
# 找到百度的输入框，并输入“Python”
driver.find_element_by_id('kw').send_keys('Python')
# 点击搜索按钮
driver.find_element_by_id('su').click()
#停顿5秒，即5秒内一直在这个界面
time.sleep(5)   
#关闭所有由当前测试脚本打开的页面
driver.quit()
    