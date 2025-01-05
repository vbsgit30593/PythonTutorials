metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)),
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
]

def match_records():
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print (f'{name:15} | {lat:9.4f} | {lon:9.4f}')
    print("#" * 50)

def match_telephone():
    telephone = [
        "18145003771",
        "919902633410",
    ]

    print(f'{"":10} | {"Number":<20}')
    for number in telephone:
        match tuple(number):
            case ['1', *rest]:
                print(f'{"US":10} | {number:<20}')
            case ['9', *rest]:
                print(f'{"India":10} | {number:<20}')

def match_dictrecord(record):
    match record:
        case {'type':'book', 'author':name}:
            return [name]
        
        case {'type':'book', 'authors': [*names]}:
            return names

        case {'type':'movie', 'director': name}:
            return [name]
        
        case _:
            raise ValueError(f"Invalid record : {record}")

def match_dictdata():
    data = [
        {
            'type': 'book',
            'authors': ["vasda", "asdadas", "asdaa"]
        },
        {
            'type': 'book',
            'author': "Vaibhav"
        },
        {
            'type': 'movie',
            'director': "Vishal"
        },
    ]

    for record in data:
        print (f"Current record: {record}, \nmatch found: ")
        print (*match_dictrecord(record), sep="\n")

match_records()
match_telephone()
match_dictdata()

