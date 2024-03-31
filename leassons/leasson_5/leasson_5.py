
# class Cat:
#     animal_type = "mammal"
#     def __init__(self, name, age, color):
#         self.name = name
#         self.age = age
#         self.color = color
#
#     def say(self):
#         print(self.name)
#
# cat = Cat('Barsik', 5, "black")
# print(cat.age)
# cat.say()


class Phone:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def __str__(self):
        return f'Phone {self.brand} {self.model} {self.price}'

phone1 = Phone('Samsung','a52', 7000)
phone2 = Phone('Samsung','a12', 4000)
phone3 = Phone('Samsung','s11', 37000)
phone4 = Phone('Xiomi','Redmi Note 11', 8700)
phone5 = Phone('Xiomi','12 Lite', 17000)
phone6 = Phone('Samsung','a52', 7000)


class Werhouse:
    def __init__(self, address):
        self.address = address
        self.storage = {}
    def add_to_storage(self, item, value):
        self.storage[item]=value
    def remove_from_storage(self, item):
        value = self.storage.pop(item,None)
        return value
    def get_item_value(self, item):
        return self.storage.get(item)
    def get_total_price(self):
        total = 0
        for key, cnt in self.storage.items():
            total += key.price * cnt
        return total
    def __str__(self):
        tmp = ''
        for item, cnt in self.storage.items():
            tmp += f'{str(item)}: {cnt} pcs. \n'
        return f'Werehouse at {self.address} contains:\n{tmp}'

wh = Werhouse('Kyiev, pr.peremogy, 135')
print(wh.get_total_price())
wh.add_to_storage(phone1,40)
wh.add_to_storage(phone2,23)
print(wh.get_total_price())
print(wh.get_item_value(phone2))
#


