predefined_urls = {
        '/about': '/Home/about',
        '/privacy': '/Home/privacy',
        '/': '/Home/index',
        '/shop': '/Shop/index',
        '/cart': '/Shop/cart'
}

def parse_path(path:str) -> dict:
    parts = path.split('/') 
    # запит         parts
    # /             ['','']
    # /controller   ['','controller']
    # /controller/ ['','controller','']
    # /controller/action ['','controller','action']
    # /controller/action/ ['','controller','action','']
    return {
        "controller": (parts[1].capitalize() if len(parts) > 1 and parts[1] != '' else 'Home') + "Controller",
        "action": parts[2] if len(parts) > 2 and parts[2] != '' else 'index',
        "lang": "uk",
        "path-id": None
    }