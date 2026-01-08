# 小项目：名言数据分析

## 第一天

### 需要完成：

- 翻页的URL怎么来
- 用 for 循环爬多页
- 能打印出每一页抓取状态
- 程序跑完不报错
- 已知：
- BASE_URL = "https://quotes.toscrape.com/page/{}/"
- HEADERS = {
  "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
  }

### 思考题：

- 1️⃣ BASE_URL 为什么要用 {}
    - {}为后面URL参数拼接所使用
- 2️⃣ for page in range(1, 4) 是怎么控制页数的
    - for循环从1开始到3结束左闭右开
- 3️⃣ 为什么要判断 status_code
    - status_code返回200证明请求成功，若不是200则需要注意是否被限制访问
- 4️⃣ 为什么 先 append 到 list，而不是直接写文件
    - 逐条写入的话使得IO频繁操作每次都需要打开-写入-关闭
    - 数据的一致性，为避免在爬取过程中出现的错误导致数据不完整或格式错误
    - 方便于数据的处理和清洗
    - 代码的可维护性和避免内存溢出

### 简短小记

- 学会通过 URL 规律进行翻页爬取
- 使用 for 循环批量请求页面
- 能判断请求是否成功

## 第二天

### 需要完成：

- 同时爬 名言 + 作者
- 用 dict 表示一条数据
- 用 list 保存所有数据
- 保存为 quotes.csv

### 思考题：

- 1️⃣ 为什么不用 find_all("span", class_="text") 直接爬？
    - 一个quote对应一个author，如果直接用find_all来爬取不能保证数据关联性
    - 减少数据错位风险
    - 可以获取更多相关数据
- 2️⃣ 为什么 list 里要放 dict？
    - 易于序列化和存储
    - 保持数据完整性
    - 便于数据处理和转换
    - 灵活的查询和操作
    - 更易于扩展
- 3️⃣ 为什么 CSV 是“数据分析最友好的格式”？
    - csv是纯文本格式中间用逗号隔开
    - 几乎所有的数据分析工具都支持CSV
    - 无需额外的依赖
    - 存储效率高
        - 格式；优点；缺点
        - CSV；纯文本，通用；无数据类型，无压缩
        - Excel；美观，公式；二进制，需要特定软件
        - JSON；结构化，嵌套；冗余，解析慢
        - Parquet；压缩好，列存；复杂，需要专门库
        - Pickle；Python对象；Python专用，不安全
    - 虽然CSV很友好，但也有局限性：
        - 无数据类型：所有数据都是字符串
        - 无嵌套结构：只适合二维表数据
        - 需要处理特殊字符：引号、换行、逗号等
        - 无压缩：文件体积较大
        - 无标准规范：不同方言（分隔符、引号等）

### 简短小记

- 使用 div.quote 作为数据块解析
- 将数据结构化为 list + dict
- 学会使用 csv.DictWriter 保存数据

## 第三天

### 需要完成：

- 用 pandas 读取 CSV
- 查看数据结构
- 做统计分析
- 输出“有意义的结果”

### 思考题

- pandas 为什么比 csv 模块更适合分析？
    - 数据结构化保存
    
    - 内置数据处理功能，例如：
        - df.dropna()  # 删除缺失值
        - df.fillna(0) # 填充缺失值
        - df.drop_duplicates()  # 去重
        - df[df['age'] > 30]  # 条件筛选
        - df.query('salary > 50000')  # 查询语法
        - df.groupby('department')['salary'].mean() # 分组聚合
        
    - 高性能向量化操作，CSV需要循环而Pandas使用向量化计算对整个列进行操作
    
    - 丰富的数据接口
      - 合并数据
        - pd.merge(df1, df2, on='id')
        - pd.concat([df1, df2])
      - 透视表
        - df.pivot_table(values='sales', index='region', columns='month')
      - 时间序列处理
        - df['date'] = pd.to_datetime(df['date'])
        - df.resample('M')['sales'].sum()
      
    - 统计分析和描述
      - 一键获取统计信息
        - df.describe()  # 计数、均值、标准差、分位数等
        - df.corr()      # 相关系数矩阵
        - df['column'].value_counts()  # 频数统计
      
    - 与生态系统集成
      - 无缝连接其他库(比如matplotlib)
      - 机器学习集成
      
    - 内存优化和高效读取
      - 分块读取大文件
        - chunk_iter = pd.read_csv('large.csv', chunksize=10000)
        - for chunk in chunk_iter:
        - process(chunk)
      - 指定数据类型节省内存
        - dtypes = {'id': 'int32', 'price': 'float32'}
        - df = pd.read_csv('data.csv', dtype=dtypes)
      
    - 实用的便捷功能
      - 自动检测编码和分隔符
        - df = pd.read_csv('data.txt', sep=None, encoding='auto')
      - 处理多种格式
        - df.to_excel('output.xlsx')
        - df.to_json('output.json')
      - 缺失值灵活处理
        - df.interpolate()  # 插值填充
      
    - 对比：
      - 特性;csv 模块;pandas
      
      - 数据结构;原始列表/字典;DataFrame/Series
      
      - 数据清洗;手动编写代码;内置方法
      
      - 性能;Python循环，较慢;NumPy向量化，快速
      
      - 内存管理;基础;优化（分块、类型推断）
      
      - 统计分析;需手动实现;内置丰富统计函数
      
      - 数据可视化;无直接支持;集成matplotlib
      
      - 学习曲线;简单;较陡但功能强大
        - value_counts() 本质在做什么？
            - 核心本质是哈希表计数，步骤：
              - 遍历Series中的每一个元素
              - 使用哈希表记录每个唯一值出现的次数
              - 时间复杂度为O(n)
              
            - 底层工作机制：
              - 哈希表实现的核心逻辑
                -  类似的手动实现（简化版）
                   
                      ```python
                       import pandas as pd
                       def naive_value_counts(series):
                            counter = {}
                            for item in series:
                                if pd.isna(item):  # 处理缺失值
                                    item = None
                                counter[item] = counter.get(item, 0) + 1           
                           # 转换为有序结果
                             result_series = pd.Series(counter)
                             return result_series.sort_values(ascending=False)
                      
                           # pandas 实际使用优化的 Cython/C 实现，速度更快
                      ```

                - 内存优化的关键特性
                  
                  ```python
                   # pandas 内部使用哈希表 + 分类数据类型优化
                   import pandas as pd
                    s = pd.Series(['A', 'B', 'A', 'C'] * 1000000)
                  '''
                  实际内部处理：
                  将字符串映射为整数编码
                  对整数数组进行计数（效率更高）
                  最后再映射回原始值
                  '''
                  ```
                  
                - 重要参数解析
                
                  - normalize：转换为频率
                
                    ```python
                    import pandas as pd
                    s = pd.Series(['a', 'b', 'a', 'c', 'b', 'a'])
                    
                    # 原始计数
                    counts = s.value_counts()
                    # a    3
                    # b    2
                    # c    1
                    
                    # 频率分布
                    freq = s.value_counts(normalize=True)
                    # a    0.500000
                    # b    0.333333
                    # c    0.166667
                    ```
                
                  -  sort 和 ascending：排序控制
                
                    ```Python
                    # 按计数降序（默认）
                    s.value_counts(sort=True, ascending=False)
                    
                    # 按值字母顺序
                    s.value_counts(sort=False)  # 按首次出现的顺序
                    
                    # 按计数升序
                    s.value_counts(ascending=True)
                    ```
                
                  - bins：数值分箱统计
                
                    ```Python
                    # 对数值型数据自动分箱
                    nums = pd.Series([1.2, 2.5, 3.7, 4.1, 5.8, 6.3, 7.9])
                    
                    # 分成3个区间统计
                    nums.value_counts(bins=3)
                    # (5.8, 7.9]     2
                    # (3.7, 5.8]     2
                    # (1.192, 3.7]   3
                    ```
                
                  - dropna：缺失值处理
                
                    ```Python
                    s = pd.Series(['a', 'b', None, 'a', np.nan, 'b'])
                    
                    # 排除 NaN（默认）
                    s.value_counts(dropna=True)
                    # a    2
                    # b    2
                    
                    # 包含 NaN
                    s.value_counts(dropna=False)
                    # a      2
                    # b      2
                    # NaN    2
                    ```
                
                  - 性能优势体现
                
                    ```Python
                    import time
                    import numpy as np
                    
                    # 大数据量测试
                    large_series = pd.Series(np.random.choice(['A', 'B', 'C', 'D'], size=1000000))
                    
                    # 方法1：value_counts (最快)
                    start = time.time()
                    result1 = large_series.value_counts()
                    print(f"value_counts: {time.time()-start:.4f}s")
                    
                    # 方法2：groupby (较慢)
                    start = time.time()
                    result2 = large_series.groupby(large_series).size()
                    print(f"groupby: {time.time()-start:.4f}s")
                    
                    # 方法3：collections.Counter (最慢)
                    from collections import Counter
                    start = time.time()
                    result3 = pd.Series(Counter(large_series))
                    print(f"Counter: {time.time()-start:.4f}s")
                    ```
                
                - 特殊场景处理
                
                  1. 多列组合统计
                
                  ```python
                  df = pd.DataFrame({
                      'A': ['X', 'Y', 'X', 'Y'],
                      'B': [1, 1, 2, 2]
                  })
                  
                  # 对多列组合进行计数
                  df.groupby(['A', 'B']).size().sort_values(ascending=False)
                  # 等价于对多列进行 value_counts
                  ```

                  2. 大数据集的分块处理
                
                  ```python
                  # 当数据太大无法一次加载时
                  chunk_counts = pd.Series(dtype='int64')
                  for chunk in pd.read_csv('huge_file.csv', chunksize=100000):
                      chunk_counts = chunk_counts.add(
                          chunk['column'].value_counts(), 
                          fill_value=0
                      )
                  ```
            
                  3. 内存效率对比
                  ```python
                  # value_counts 的内存优化策略
                  data = pd.Series(['cat', 'dog', 'cat'] * 10000)
                  
                  # 内部使用分类类型优化
                  print(data.memory_usage(deep=True))  # 较大
                  counts = data.value_counts()
                  print(counts.memory_usage(deep=True))  # 很小
                  ```
                
              - 实际应用技巧
                
                ```python
                # 1. 快速数据质量检查
                df['column'].value_counts(normalize=True).head(10)
                
                # 2. 检测异常值
                counts = df['column'].value_counts()
                rare_values = counts[counts < 5]  # 出现少于5次的值
                
                # 3. 类别合并
                value_map = df['category'].value_counts()
                # 将低频类别合并为"其他"
                threshold = 10
                main_categories = value_map[value_map >= threshold].index
                df['category_clean'] = df['category'].where(
                    df['category'].isin(main_categories), 
                    '其他'
                )
                ```
    
  - 为什么“结论”比“代码本身”重要？
      - 从价值导向来讲，最高层是商业决策/行动指导（最终目标），而中层是洞察与结论（翻译数据的价值），底层只是数据清洗/处理（必要但不充分），最底层就是代码/工具/算法（实现手段）
      - 沟通效率：不同受众的需求 
      - 
        | 受众       | 关心代码 | 关心结论 | 原因                       |
        | :--------- | :------- | :------- | :------------------------- |
        | 高管       | 0%       | 100%     | 时间宝贵，需要直接决策依据 |
        | 业务经理   | 10%      | 90%      | 关注业务影响和行动方案     |
        | 数据分析师 | 50%      | 50%      | 既关注实现也关注洞见       |
        | 数据科学家 | 80%      | 20%      | 技术实现和模型优化         |
  
- 如果作者有空格 / 异常值，该怎么清洗？
    ### **空格处理策略：**
    
    1. **预防优于治疗**：在数据录入阶段限制空格输入
    2. **标准化处理**：使用统一函数处理所有文本列
    3. **保留原始数据**：清洗前备份，使用新列存储清洗结果
    
    ### **异常值处理原则：**
    
    1. **不要盲目删除**：先分析异常值产生原因
    2. **分层处理**：根据业务重要性采用不同策略
    3. **记录处理过程**：保留异常值标记，便于追溯
    4. **考虑数据分布**：选择适合分布的处理方法
    
    ### **关键注意事项：**
    
    - **文本数据**：注意编码问题，统一使用UTF-8
    - **数值数据**：注意单位统一和格式标准化
    - **时间数据**：注意时区处理和格式统一
    - **分类数据**：注意类别一致性

### 简短小记

- 使用 pandas 读取 CSV
- 统计作者名言数量
- 输出分析结论
- 初步理解“数据分析的价值在于结论”
- 学会用函数拆分爬虫逻辑
- 理解 main 入口的作用
- 加入异常处理提高稳定性
- 代码开始具备“项目结构感”
- 学会使用随机 User-Agent
- 添加请求延时，降低封禁风险
- 理解反爬的基本逻辑
- 使用 matplotlib 进行基础数据可视化
- 将统计结果转为图表
- 理解“分析结果需要被表达”