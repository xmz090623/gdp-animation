# gdp-ranking-bar-racing

数据来源:
https://databank.worldbank.org/indicator/NY.GDP.MKTP.CD/1ff4a498/Popular-Indicators#

各个国家和地区的GDP数据来自世界银行组织的官方网站。其提供了从1960年到2020年全球各个国家和地区的经济，人文，环境数据。
网站支持对原始数据进行筛选和格式化，并提供多种格式的数据的下载，其中包含在大数据处理领域广泛使用的csv（Comma-Separated Value）格式。
在网站筛选数据的时候，为了简化对数据的处理，按照以下条件筛选和输出数据：
1. 以十亿美元（billon dollars）为单位
2. 每一列为国家从1960年到2020年的GDP数据
3. 如果当年数据缺失，使用NA标识   
4. 只输出GDP数据
5. 然后以CSV形式下载数据并保存到本地

数据处理和gif绘制：
模块的名字叫pandas-alive，可以通过pip命令安装。这个模块可以读取csv文件，并转换成pandas的dataframe格式。在通过一个简单的函数调用，就可以生成gif文件并保存到本地。

- git repo: https://github.com/JackMcKew/pandas_alive
- 使用手册：https://pypi.org/project/pandas-alive/#usage

如何执行：
`$ python3.7 main.py -f wb_1960_2020_gdp_dollar.csv -g wb_1960_2020_gdp_dollar.gif -i 1000`
