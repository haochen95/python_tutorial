# python_tutorial 

这里主要写一些做科研的时候需要使用到的python软件包的教程，主要包括以下：  

* Python语法  
* [Numpy](https://nbviewer.jupyter.org/github/haochen95/python_tutorial/blob/master/Numpy/numpy.ipynb)  
* [Pandas](https://nbviewer.jupyter.org/github/haochen95/python_tutorial/blob/master/Pandas/pandas.ipynb)  
* Scipy  
* Scikit-learn  
  * [Regression](https://nbviewer.jupyter.org/github/haochen95/python_tutorial/blob/master/Scikit-learn/Scikit-learning-Regression.ipynb)
  * [Classification](https://nbviewer.jupyter.org/github/haochen95/python_tutorial/blob/master/Scikit-learn/Scikit-learning-Classification.ipynb)
* Deep-learning  
  * tensorflow  
  * theano  
  * keras  
  * pyTorch
* Python可视化  
  * [Matplotlib](https://nbviewer.jupyter.org/github/haochen95/python_tutorial/blob/master/Python_Visualize/Scikit-learn-matplotlib-bar.ipynb)  
  * [Seaborn](https://github.com/haochen95/python_tutorial/blob/master/Python_Visualize/Seaborn.ipynb)  
  * plotly  
* Python正则表达式
* Python爬虫  
  * Request  
  * [Scrapy](#scrapy)  
* pygame  
* pyqt5
* [其他工具](#qita)  




# <span id = "matplotlib">Matplotlib</span>  

![](https://matplotlib.org/_static/logo2.png)

| 方法| 说明|  
|-----|-----|
| 子图的绘制| subplot,subplots|
| Scatter||  
|  chart||  
| Hist chart||  
| Pie chart||  
| Box chart||
| Text标注||  
| Plot高级||  
| 其他||  

# <span id = "scrapy">Scrapy</span>  

![](https://blog.scrapinghub.com/hs-fs/hubfs/Imported_Blog_Media/scrapy.png?width=300&name=scrapy.png)  

|案例|说明| 作用 |
|----|----|---|
|[mySpider](https://github.com/haochen95/python_tutorial/tree/master/Scrapy/mySpider)|爬取传智播客一页的老师名字、职称和介绍| reponse.xpath, parse, pipeline, yield|  
|[TecentSpider](https://github.com/haochen95/python_tutorial/tree/master/Scrapy/tecentJob)|爬取腾讯招聘网页的信息，例如职位名、职位地点、职位个数、职位类别等|scrapy.Request(url. callback = self.parse), 爬取有翻页的网址|  
|[TencentCrawlSpider](https://github.com/haochen95/python_tutorial/tree/master/Scrapy/tencentCrawlSpider)|上同|CrawlSpider深度爬取的使用|
|[DongguanCrawlSpider](https://github.com/haochen95/python_tutorial/tree/master/Scrapy/dongguan)|爬出东莞阳光网上面的意见信息|CrawlSpider深度爬取|
|[dongguanSpider](https://github.com/haochen95/python_tutorial/tree/master/Scrapy/dongguanSpider)|上同|Spider广义爬取|
|[douban](https://github.com/haochen95/python_tutorial/tree/master/Scrapy/douban)|爬取豆瓣电影的信息|将内容保存到MongDB数据库中|


# <span id = "qita">其他工具</span>  

|工具|功能|网址|  
|---|----|----|  
|itchat|微信小助手的创建||  
|wxpy|基于图灵机器人的微信尬聊||
|[pyecharts](https://github.com/haochen95/python_tutorial/tree/master/Others)|高逼格的图表可视化库||
|turtle|绘图模块||
|requests|网络请求||
|click|将一个函数变为一个命令行工具||
|lxml|HTML/XML解析器||
|wordcloud|图云||
|jieba|文本挖掘及分词功能||
|pdfkit|将文本转为pdf||
|IPy|IP地址处理模块||
|cfscrape|加密邮箱||
|pillow|图片处理模块||
|js2py|||
|PIL|||
|selenium|过驱动浏览器，完全模拟浏览器的操作||
|pyautogui|python自动化||
|pyscreenshoot|截屏模块||
|cv2|opencv模块||
|fake_useragent|模拟浏览器请求头||
|pyinstaller|打包py文件||
|ipaddress|处理IPV4和IPV6的网络地址||  
|contextlib|上下文管理器功能||  
|openpyxl|读写Excel||  
|graphics|图形库||
|dlib|人脸识别模块||
|xlrd|读excel||
|win_unicode_console||
|snowlp|情感分析||
|gensim|文章相似度||
|pywin32|||
|torch|||
|torchvision|||
|gym|强化学习||
|imageio|图像处理||
|qrcode|生成二维码||




# Contact-info  

Feel free to contact me to discuss any issues, questions, or comments.  

* Email: [haochen273@gmail.com](mailto:haochen273@gmail.com)
* Blog: [Unknown404](https://www.cnblogs.com/haochen273/)
* GitHub: [haochen95](https://github.com/haochen95)



# Licese  

This repository contains a variety of content; some developed by Hao Chen, and some from third-parties. The third-party content is distributed under the license provided by those parties.

```text  
Copyright 2019 Hao Chen

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

   http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
