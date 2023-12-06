import json

def create_summary(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        lines = file.readlines()

    cheapest_product = None
    cheapest_price = 0.00
    costliest_product = None
    costliest_price = 0.00
    total_price = 0
    product_count = 0

    for line in lines:
        values = line.strip().split(',')
        product_name = values[0]
        price = float(values[2])

        # cheapest price ? 
        if price < cheapest_price : 
            cheapest_price = price
            cheapest_product = product_name

        # costliest price ? 
        if price > costliest_price :
            costliest_price = price 
            costliest_product = product_name

        # average price ? 
        total_price += price
        product_count += 1
        average_price = total_price / product_count 
        
        summary = {
            "cheapest product" : cheapest_product,
            "costliest product": costliest_product,
            "average price": average_price
        }

        with open(output_filename, 'w') as output_file :
            json.dump(summary, output_file)


create_summary('test.csv', 'results.json')
  