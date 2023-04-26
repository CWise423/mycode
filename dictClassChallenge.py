#!/usr/bin/python3

def main():
    elvis_presley = {
        'birthday': 'january-8-1935',
        'place_of_birth': 'tupelo',
        'death': 'august-16-1977',
        'AKA': 'The King',
                    }

    print(elvis_presley)


    elvis_presley.update( {"house": "Graceland"} )

    print(elvis_presley.keys())

    counter = 1
    for keys in elvis_presley:
        print(f"{counter}: {keys}")
        counter += 1

    choice= int(input("Choose a key:\n> "))

    value= elvis_presley.get(choice, "No value found.")

    print(f"Elvis' {choice} was {value.upper()}")

if __name__ == "__main__":
    main()
