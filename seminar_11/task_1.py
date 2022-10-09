from numpy import number


class Person:
    def __init__(self,name,sname,lname,phone):
        self.name = name
        self.sname = sname
        self.lname = lname
        self.phone = phone
    
    def get_name(self):
        return self.name
    
    def get_phone(self):
        return self.phone.get('private')
    
    def get_work_phone(self):
        return self.phone.get('work')

    def get_sms_text(self):
        return 'Уважаемый(ая) {} {}! Примите участие в нашей беспроигрышной лотерее!'.format(self.name,self.sname)


class Company():
    def __init__(self,company_name,company_type,phones,*person):
        self.company_name = company_name
        self.company_type = company_type
        self.phones = phones
        self.person_list = list(person)

    def get_phone(self, key = 'contact'):
        if key in self.phones is not None:
            return self.phones.get('contact')
        else:
            for person in self.person_list:
                number = person.get_work_phone()
                return number

    def get_name(self):
        return self.company_name

    def get_sms_text(self):
        return 'Для компании {}! Примите участие в лотерее для {}!'.format(self.company_name,self.company_type)

def send_sms(*args):
    for i in args:
        number = i.get_phone()
        if number:
            print(f'Отправлено СМС на номер {number} с текстом: {i.get_sms_text()}')
        else:
            print(f'Не удалось отправить сообщение абоненту: {i.get_name()}')

person1 = Person("Ivan", "Ivanovich", "Ivanov", {"private": 123, "work": 456})
person2 = Person("Ivan", "Petrovich", "Petrov", {"private": 789})
person3 = Person("Ivan", "Petrovich", "Sidorov", {"work": 789})
person4 = Person("John", "Unknown", "Doe", {})
company1 = Company("Bell", "ООО", {"contact": 111}, person3, person4)
company2 = Company("Cell", "АО", {"non_contact": 222}, person2, person3)
company3 = Company("Dell", "Ltd", {"non_contact": 333}, person2, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)

person1 = Person("Степан", "Петрович", "Джобсов", {"private": 555})
person2 = Person("Боря", "Иванович", "Гейтсов", {"private": 777, "work": 888})
person3 = Person("Семен", "Робертович", "Возняцкий", {"work": 789})
person4 = Person("Леонид", "Арсенович", "Торвальдсон", {})
company1 = Company("Яблочный комбинат", "ООО", {"contact": 111}, person1, person3)
company2 = Company("ПластОкно", "АО", {"non_contact": 222}, person2)
company3 = Company("Пингвинья ферма", "Ltd", {"non_contact": 333}, person4)
send_sms(person1, person2, person3, person4, company1, company2, company3)

