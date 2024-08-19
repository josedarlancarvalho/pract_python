from collections import Counter

vendas_tec = ["notebook samsung", "camera canon", "fone apple", "galaxy s22", "smartwatch xiaomi", "tablet lenovo", 
            "drone dji", "camera canon", "impressora epson", "monitor dell", "teclado mecânico logitech", 
            "camera canon", "mouse gamer razer", "caixa de som jbl", "tv lg 55 polegadas", "home theater sony", 
            "projetor epson", "ps5 sony", "xbox series x", "ssd samsung 1tb", "hd externo seagate 2tb", 
            "placa mãe asus", "placa de vídeo nvidia rtx 3070", "processador intel i7", "memória ram corsair 16gb", 
            "gabinete gamer nzxt", "ps5 sony", "fonte corsair 750w", "cooler master hyper 212", "cadeira gamer dxracer", 
            "webcam logitech c920", "microfone blue yeti", "headset hyperx cloud", "smartphone oneplus 9", 
            "cooler master hyper 212", "ipad apple", "macbook pro", "airpods pro", "kindle amazon", 
            "roteador tp-link ac1900", "switch gigabit netgear", "modem fibra óptica huawei", "hub usb-c anker", 
            "carregador portátil xiaomi 10000mah", "case para notebook", "smart lampada philips hue", "smart plug amazon", 
            "chromecast google", "fire tv stick amazon", "gamepad xbox", "smartwatch apple watch series 7", 
            "tablet samsung galaxy tab s7", "notebook dell xps 13"]

contador = Counter(vendas_tec)

produto_mais_comum = contador.most_common(3)
print(produto_mais_comum)