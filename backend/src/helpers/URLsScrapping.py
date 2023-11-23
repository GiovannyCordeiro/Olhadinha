from helpers.checkWitheSpaceStoreName import checkWitheSpaceStoreName

class ULRsScrapping:
    logic = {
        "cuponomia": lambda store: f"https://www.cuponomia.com.br/desconto/{checkWitheSpaceStoreName(store)}",
        "zoom": lambda store: f"https://www.zoom.com.br/search?q={store}",
        "intershop": lambda store: f"https://intershop.bancointer.com.br/lojas/{checkWitheSpaceStoreName(store)}",
        "meudimdim": lambda store: f"https://www.meudimdim.com.br/loja/{checkWitheSpaceStoreName(store)}"
    }