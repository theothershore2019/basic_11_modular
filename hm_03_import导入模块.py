# inmport 模块名，是一次性把模块中所有工具导入
# 并通过 模块名. 使用模块提供的工具 - 全局变量,函数,类
import hm_01_测试模块1
import hm_02_测试模块2

hm_01_测试模块1.say_hello()
hm_02_测试模块2.say_hello()

dog = hm_01_测试模块1.Dog()
print(dog)

cat = hm_02_测试模块2.Cat()
print(cat)
