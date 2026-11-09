class person:
    def __init__(self,age):
        self._age=age

    @property
    def age(self): 
        return self._age
p=person(25)
print(p.age)

        