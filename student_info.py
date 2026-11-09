class student:
    def __init__(self,name,student_id,department):
        self.name=name
        self.student_id=student_id
        self.department=department
    def display_info(self):
        print(f"Name:{self.name}")
        print(f"Student Id:{self.student_id}")
        print(f"Department:{self.department}")
    def     introduce(self):
        print(f"hello,my name is {self.name}.I am a Student")
             
s1=student("Husni","AK_0078","IT")
s2=student("Meru","AK_0079","Hafiz")
s3=student("Mohammed","AK_0080","Hafiz")      

s1.display_info()
s1.introduce()
s2.display_info()
s2.introduce()
s3.display_info()
s3.introduce()