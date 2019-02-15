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
|[Tecent](https://github.com/haochen95/python_tutorial/tree/master/Scrapy/tecentJob)|爬取腾讯招聘网页的信息，例如职位名、职位地点、职位个数、职位类别等|scrapy.Request(url. callback = self.parse), 爬取有翻页的网址|  
|[TencentCrawlSpider](https://github.com/haochen95/python_tutorial/tree/master/Scrapy/tencentCrawlSpider)|上同|CrawlSpider深度爬取的使用|
|[Dongguan](https://github.com/haochen95/python_tutorial/tree/master/Scrapy/dongguan)|爬出东莞阳光网上面的意见信息|深度爬取，url的内部内容提取|


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
