# MicroIndexSpyder
self complemented MicroIndexSpyderbased on Selenium ，新浪微博指数(微指数)采集，包括综合指数，移动端指数，PC端指数。

# 项目介绍
1、微指数是基于海量用户行为数据、博文数据，采用科学计算方法统计得出的反映不同事件领域发展状况的指数产品。    
2、微指数对于收录的关键词，在指数方面提供微博数据层面的指数数据，包括综合指数、移动指数、PC指数三个指数。  

# 项目举例
以‘中兴’这一关键词为例，要求获取中兴的三个指数数据。微指数的数据收录时间有范围，范围表现在：  
1）整体趋势：2013-03-01-至今  
2）移动趋势：2014-01-06-至今  
3）PC趋势：2014-01-06-至今  
本例子设定start_date = '2016-05-29'，end_date = '2018-05-29'， 原始结果如下：

# 一、原始综合指数
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/sina_index_general.png)
# 二、原始移动/pc指数
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
# 一、综合指数
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/index_general_local.png)
# 二、移动指数
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/index_mobile_local.png)
# 三、PC指数
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/index_pc_local.png)
# 四、指数对比
![image](https://github.com/liuhuanyong/MicroIndexSpyder/blob/master/image/sina_index_vs.png)

# 总结
1、微指指数的采集难度介于百度指数与阿里指数之间，两个特点：1)指数有js动态请求而成，可以通过构造请求，解析获得。2)无需用户登录。    
2、微指数收录的日期比阿里指数要广，较百度指数要窄，但基于微博这一层面得到的数据，对于相关研究还是有一定新意的。 
