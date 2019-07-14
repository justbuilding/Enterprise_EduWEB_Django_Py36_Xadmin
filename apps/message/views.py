from django.shortcuts import render
import pymysql

from .models import UserMessage


def get_form(request):
    # 注意form.html内置有重名，需改为其他如message_form.html
    # all_messages = UserMessage.objects.all()
    # for i in all_messages:
    #     print(i.name)

    # 查
    # 查看是否有数据boddy来验证自己的思路是否值得考验
    # all_messages = UserMessage.objects.filter(name="boddy")
    # for i in all_messages:
    #     print(i.name)


    # user_message = UserMessage()
    # user_message.name = "bobby2"
    # user_message.message = "helloworld2"
    # user_message.address = "上海"
    # user_message.email = "2@1.com"
    # user_message.object_id = "helloworl2"
    # user_message.save()

    # 增
    # 获取提交的数据并存入数据库
    # if request.method == "POST":
    #     name = request.POST.get('name','')
    #     message = request.POST.get('message','')
    #     address = request.POST.get('address','')
    #     email = request.POST.get('email','')
    #     user_message = UserMessage()
    #     user_message.name = name
    #     user_message.message =  message
    #     user_message.address = address
    #     user_message.email = email
    #     user_message.object_id = "helloworl3"
    #     user_message.save()

    # 删
    # 删除全部
    # all_messages = UserMessage.objects.filter(name="boddy")
    # all_messages.delete()
    # 删除某条,设置条件
    # all_messages = UserMessage.objects.filter(name="boddy")
    # for i in all_messages:
    #     i.delete()

    # return render(request, 'message_form.html')


    message = None
    all_messages = UserMessage.objects.filter(name="bodd")
    if all_messages:
        message = all_messages[0]
    return render(request, 'message_form.html',{
        "my_name":message
    })




'''
使用ORM，则数据库操作就像使用类的属性一样简单，且本质上会根据对接的数据库引擎，翻译成对应的sql语句；
所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite….，如果数据库迁移，只需要更换Django的数据库引擎即可；
'''
# 原生数据库操作，即没有用ORM来操作数据库
# def book_list(request):
#     # 连接数据库
#     db = MySQLdb.connect(user='root', db='mydb', passwd='root', host='localhost')
#     # 使用数据库的游标
#     cursor = db.cursor()
#     # 通过cursor执行sql语句
#     cursor.execute('select name from books order by name')
#     # 取数组的第一列元素
#     names = [row[0] for row in cursor.fetchall()]
#     # 关闭连接
#     db.close()
