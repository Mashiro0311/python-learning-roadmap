# 03-01
## 目标一句话：你要开始“像写爬虫一样写 Python”
- 理解 HTTP 请求与响应 
- 学会使用 requests.get
- 学会通过 params 传参co

# 03-02
## 目标一句话：你要能“看懂网页 → 发请求 → 解析数据”
- 理解为什么要使用 headers
- 学会通过 User-Agent 模拟浏览器
- 使用 BeautifulSoup 解析 HTML
- 能从真实网页提取结构化数据
- 关于解析器：分为Python标准库、lxml HTML、lxml XML、html5lib
- 其中python标准库的使用方法为BeautifulSoup(response.text, "html.parser")
  - 它的优点是Python内置的标准库；执行能力适中；文档容错能力强
  - 当然缺点是不能很好兼容Python 2.7 或者 3.3之前的版本
- lxml HTML 的用法是 BeautifulSoup(response.text, "lxml")
  - 它的优点是 速度快；文档容错能力强
  - 缺点是需要安装对应的库
- lxml XML 的用法是BeautifulSoup(response.text, "xml")
  - 它的优点是 速度快；唯一支持XML的解析器
  - 缺点是需要安装对应的库
- html5lib 的用法是BeautifulSoup(response.text, "html5lib")
  - 它的优点是 很好的容错性；以浏览器的方式解析文档；生成HTML5格式的文档
  - 缺点是 速度慢；不依赖外部扩展