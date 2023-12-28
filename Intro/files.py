# Робота з файлами

def create_file1() -> None:
    fname = "file1.txt"
    f = None
    try:
        f = open(fname, mode="w", encoding="utf-8")
        f.write("Hello")
        f.write("\nNew line")
    except OSError as err:
        print("File 1 creation error", err)
    else:
        f.flush()
        print(fname, "created successfully")
    finally:
        if f != None : f.close()
        
def create_file2() -> None:
    fname = "file2.txt"
    try:
        with open(fname, mode="w", encoding="utf-8") as f:
            f.write("Host: localhost\r\n")
            f.write("Connection: close\r\n")
            f.write("Content-Type: text/html")
    except OSError as err:
        print("File 2 creation error", err)
        
        
def parse_headers(fname) -> dict:
    header_dict = {}
    with open(fname, 'r') as f:
        for line in f:
            if ':' in line:
                key, value = map(str.strip, line.split(':', 1))
                header_dict[key] = value
    return header_dict


def parse_headers2(fname) -> dict:
    headers = {}
    for line in read_lines(fname):
        if ':' in line:
            key, value = map(str.strip, line.split(':', 1))
            headers[key] = value
    return headers


def parse_headers3(fname) -> dict:
    return{
        k: v for k,v in
        (map(str.strip, line.split(':', 1)) 
         for line in read_lines(fname))
    }


def read_all_text(fname) -> None:
    try:
        with open(fname, mode="r", encoding="utf-8") as f:
            return f.read()
    except OSError as err:
        return "File read error", err


def read_lines(fname) -> None:
    try:
        with open(fname, mode="r", encoding="utf-8") as f:
            return (line for line in f.readlines())
    except OSError as err:
        return "File read error", err

def main() -> None:
    # create_file2()
    # print(read_all_text("file2.txt"))
    # read_lines("file2.txt")
    for k,v in parse_headers3("file2.txt").items():
        print("> %s : %s" % (k,v))
if __name__ == "__main__":
    main()