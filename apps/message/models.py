from django.db import models

# Create your models here.


class UserMessage(models.Model):
    # 加上u表示用Unicode编码，即可以用中文
    # name = models.CharField(max_length=20,verbose_name="name")
    # model.ForeignKey外键类型 models.DateTimeField对应数据库的时间类型 models.IntegerField整型类型
    # IPAddressField IP地址类型  models.FileField文件类型 models.ImageField图像类型
    # 没定义主键会自动创建id主键
    object_id = models.CharField(max_length=50, default="", primary_key=True, verbose_name=u"主键")
    name = models.CharField(max_length=20, null=True, blank=True, default="", verbose_name="用户名")
    email = models.EmailField(verbose_name=u"邮箱")
    address = models.CharField(max_length=100, verbose_name=u"联系地址")
    message = models.CharField(max_length=500, verbose_name=u"留言信息")

    class Meta:
        verbose_name = u"用户留言信息"
        # db_table = "user_message"


'''Django model中的 class Meta 详解
   通过一个内嵌类 "class Meta" 给你的 model 定义元数据
   app_label
        app_label这个选项只在一种情况下使用，就是你的模型类不在默认的应用程序包下的models.py文件中，
        这时候你需要指定你这个模型类是那个应用程序的。比如你在其他地方写了一个模型类，而这个模型类是属于myapp的，那么你这是需要指定为：
        app_label='myapp'
    db_table
        db_table是用于指定自定义数据库表名的。Django有一套默认的按照一定规则生成数据模型对应的数据库表名，如果你想使用自定义的表名，就通过这个属性指定，比如：
        table_name='my_owner_table'   
        若不提供该参数, Django 会使用 app_label + '_' + module_name 作为表的名字.
        若你的表的名字是一个 SQL 保留字, 或包含 Python 变量名不允许的字符--特别是连字符 --没关系. Django 会自动在幕后替你将列名字和表名字用引号引起来.
    ordering
        这个字段是告诉Django模型对象返回的记录结果集是按照哪个字段排序的。比如下面的代码：
            ordering=['order_date'] 
            # 按订单升序排列
            ordering=['-order_date'] 
            # 按订单降序排列，-表示降序
            ordering=['?order_date'] 
            # 随机排序，？表示随机
            ordering = ['-pub_date', 'author']
            # 对 pub_date 降序,然后对 author 升序
            需要注意的是:不论你使用了多少个字段排序, admin 只使用第一个字段
    verbose_name
        verbose_name就是给你的模型类起一个更可读的名字：
            verbose_name = "pizza"
            若未提供该选项, Django 则会用一个类名字的 munged 版本来代替: CamelCase becomes camel case
    verbose_name_plural
        这个选项是指定，模型的复数形式是什么，比如：
            verbose_name_plural = "stories"
            若未提供该选项, Django 会使用 verbose_name + "s"
'''

