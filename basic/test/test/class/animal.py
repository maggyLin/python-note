# 空的class
# class Animal:
#     pass

class Test:
    def __init__(self):  #constructor 要傳入self
        pass   # 沒有內容要寫pass
    

class Creature:
    def __init__(self):
        pass
    
    def breathe(self): # 一定要self
        return print("It's breathing.")
        
    

class Animal:
    def __init__(self,name,food):
        self.name = name
        self.food = food
        
    def eat(self):
        return print(self.name +" eat " +self.food)
    
    def run(self):
        return print(self.name +" running." )

# a = Animal("dog","meat")
# a.eat()

# 繼承 inheritance class Animal
class Dog(Animal): 
    def __init__(self,name,food):
        super().__init__(name,food)  # 使用super()呼叫父類的建構子,傳入參數
        # Animal.__init__(self,name,food) # 也可以指定呼叫父類的建構子(需要使用self)(多重繼承時)
        
    def run(self):  #override覆寫父類的方法(def)
        return print(self.name + "running. It's son.")
    
    def woof(self):  
        return print(self.name + "woof.")

# dog = Dog("dog","apple")
# dog.run()
# dog.eat()


# 多重繼承  Animal & Creature
class MixDog(Animal,Creature):
    def __init__(self,name,food):
        Animal.__init__(self,name,food)
        
mixdog = MixDog("mixdog","shrimp")
mixdog.breathe()
mixdog.run()
mixdog.eat()