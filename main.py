from model import Model
from field import CharField, IntegerField

if __name__ == '__main__':

    class StudentNew3(Model):
        first_name = CharField(max_length=128)
        last_name = CharField(max_length=128)
        age = IntegerField(default=0)

    a = StudentNew3()
    a.create(last_name='Hello', first_name='Mark', age=35)
    print(a.all())
