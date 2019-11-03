# 如果两个模块，存在同名的函数，那么后导入模块的函数，会覆盖掉先导入的函数
# from hm_01_测试模块1 import say_hello
# 开发时 import 代码应该统一写在代码的顶部，更容易及时发现冲突
# 一旦发现冲突，可以使用 as 关键字 给其中一个工具起一个别名
from hm_01_测试模块1 import say_hello as module1_say_hello
from hm_02_测试模块2 import say_hello

module1_say_hello()
say_hello()
