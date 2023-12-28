# Виключні ситуації
def throw() -> None:
    print ("Raising TypeError...")
    raise TypeError # аналог throw - створення виключення

def throw_with_message() -> None:
    print ("Raising ValueError...")
    raise ValueError("ValueError message")


def main() -> None:
    try:
        #throw()
        throw_with_message()
    except ValueError as err:
        print("Got message '%s'" % (err))
    except:
        print('Exception detected')
    else:
        print("Else action")
    finally:
        print("Finally action")
        
        
    pass # No operation - аналог порожнього тіла()

main()