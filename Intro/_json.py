# робота з JSON
import json # модуль з "коробки" для роботи з JSON

def main() -> None:
    try:
        with open("sample.json") as f:
            data = json.load(f)
    except OSError as err:
        print("File read error", err)
    
    # print(type(data),data)
    
    # for key in data:
    #     print(key,data[key],type(data[key]))
    
    data['newItem1'] = 'newValue1'
    data['newItem2'] = 'Привіт'
    print(data)
    print(json.dumps(data,
                     ensure_ascii=False, # не екранувати Unicode
                     indent=4))          # pretty print(відступ 4 пробіли)
    
    
    key = "arr"
    if key in data:
        print(key, "exists")
    else:
        print(key, "does not exist")
    
    try:
        with open("sample2.json", "w", encoding="utf-8") as f:
            json.dump(data, f)
    except OSError as err:
        print("File write error", err)
    else:
        print("Write OK")

    


if __name__ == "__main__":
    main()
