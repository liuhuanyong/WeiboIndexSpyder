# MicroIndexSpyder
self complemented MicroIndexSpyderbased on Selenium ，新浪微博指数抓取，包括综合指数，移动端指数，PC端指数。

# 项目介绍
1、阿里指数 是了解电子商务平台市场动向的数据分析平台，2012年11月26日，阿里指数正式上线。根据阿里巴巴网站每日运营的基本数据包括每天网站浏览量、每天浏览的人次、每天新增供求产品数、新增公司数和产品数这5项指标统计计算得出。  
2、阿里指数对于收录的商品关键词，在指数方面提供阿里商品指数抓取，包括淘宝采购指数，淘宝供应指数，1688供应指数三个指数，基于三个指数，可以在一定程度上反映出该商品的供需行情，与商品的价格相比，能够得出一些相关性的结论。

# 项目举例
以‘连衣裙’这一商品关键词为例，要求获取连衣裙的三个指数数据。由于阿里指数至提供近一年的指数数据，因此，只能采集一年的数据，原始结果如下：
# 原始综合指数
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/sina_index_general.png)
# 原始移动/pc指数
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/sina_index_yd.png)
# 实现流程
    '''主函数'''
    def index_main(self, word, start_date, end_date):
        # 打开数据页面
        print('step1, open page....')
        driver = self.search_index(word)
        # 构造请求，获取指数json数据
        print('step2, get data....')
        data = self.get_data(driver, start_date, end_date)
        # 判断数据返回类型，若微博没有收录改词，则退出，显示退出信息
        if data['zt']:
            print('step3, save data ...')
            self.output_data(word, data)
            print('finished....')
        else:
            print('not be record...')
        #关闭浏览器对象
        driver.close()
# 执行
    def demo():
        start_date = '2016-05-29'
        end_date = '2018-05-29'
        sina = SinaIndex()
        search_word = '中兴'
        sina.index_main(search_word, start_date, end_date)
    demo()
# 效果
将得到的数据文件，进行本地可视化，效果如下：
# 综合指数
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/index_general_local.png)
# 移动指数
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/index_mobile_local.png)
# PC指数
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/index_pc_local.png)
# 指数对比
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/sina_index_vs.png)

# 总结
1、阿里指数的采集较为简单，1)阿里指数直接将历时数据写在前端页面中，可以直接解析获得。2)无需用户登录。    
2、阿里指数与百度指数不同，其对应的关键词实体需要对应到具体的行业或商品上，而用户查询的关键词具有多样性，这样会导致可能无法正确获取严格的关键词商品指数，如搜索iphone，会得到电子产品的指数。  
3、比较遗憾的是，阿里指数只提供以查询当日为结束如日，往前推一年为开始日期的数据，对于历时数据的构建来说，不是太方便。  
