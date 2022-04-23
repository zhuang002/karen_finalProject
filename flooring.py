"""
class Flooring:
    def __init__(self, key, name, color, wood_type, price):
        self.key = key
        self.name = name
        self.color = color
        self.wood_type = wood_type
        self.price = price

    def get_total_price(self, area):
        return self.price * area
"""


class FlooringHelper:
    def __init__(self, flooring_list={}):
        self.flooring_list = flooring_list

    def calculate_total_price(self, key, area):
        return self.flooring_list[key]['price'] * area

    def choose_alternative_product(self, original_choice_key):
        original_prod = self.flooring_list[original_choice_key]

        return_choice = None
        min_price = original_prod['price']
        for prod_key in self.flooring_list:
            if prod_key == original_choice_key:
                continue

            prod = self.flooring_list[prod_key]
            if prod['color'] != original_prod['color']:
                continue

            if prod['price'] >= original_prod['price']:
                continue

            if prod['price'] < min_price:
                min_price = prod['price']
                return_choice = prod
        return return_choice

    def __str__(self):
        s = ""
        for key in self.flooring_list:
            s += key + ": " + self.flooring_list[key]['name'] + "\n"
        return s


floorings = {
    'LM0001': {
        'key': 'LM0001',
        'name': 'Napa River Oak Laminate Flooring',
        'color': 'Napa',
        'wood_type': 'Laminate',
        'price': 0.89
    },
    'LM0002': {
        'key': 'LM0002',
        'name': 'Hayes River Oak Water Resistant  Flooring',
        'color': 'Brown',
        'wood_type': 'Laminate',
        'price': 2.19
    },

}

flooring_helper = FlooringHelper(floorings)

print(flooring_helper)
choice = input("Please input your choice key:")
area = float(input("Please input your room area:"))
print('Total price: ' + flooring_helper.calculate_total_price(choice, area))
while True:
    yn = input("Is this within your budget? (y/n)")
    if yn == 'y':
        break
    alt_prod = flooring_helper.choose_alternative_product(choice)
    if not alt_prod:
        print('No cheaper product is found.')
        break
    print('We suggest product {key}: {name}, total price would be ${price}'.format(
        key=alt_prod['key'], name=alt_prod['name'], price=flooring_helper.calculate_total_price(alt_prod['kye'], area))
    )
