# 如果模块的名字太长，可以使用 as 指定模块的名称，以方便在代码中的使用
import hm_01_测试模块1 as DogModule
import hm_02_测试模块2 as CatModule

DogModule.say_hello()
CatModule.say_hello()

dog = DogModule.Dog()
print(dog)

cat = CatModule.Cat()
print(cat)
