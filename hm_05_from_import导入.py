# 如果希望从某一个模块中，导入部分工具，就可以使用 from ... import 的方式
# 不需要通过 模块名.　可以直接使用模块提供的工具来访问/调用 全局变量、函数、类
from hm_01_测试模块1 import Dog
from hm_02_测试模块2 import say_hello

say_hello()

wangcai = Dog()
print(wangcai)
