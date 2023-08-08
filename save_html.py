from selenium import webdriver
import os

# 指定URL
url = 'https://openknowledgemaps.org/map/282a4733a18a9e0b030cb4adbbf6dae1'

# 配置Chrome浏览器
options = webdriver.ChromeOptions()
options.headless = False # 设置为False，则可以看到浏览器窗口

# 打开浏览器
browser = webdriver.Chrome(options=options)
browser.get(url)

# 保存完整的页面到本地
save_as = os.path.join(os.getcwd(), 'complete_page.html')
with open(save_as, "w", encoding="utf-8") as file:
    file.write(browser.page_source)

# 关闭浏览器
browser.quit()
