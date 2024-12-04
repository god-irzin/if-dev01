animes = {   
     "one piece" : {
        "episódios" : "1122 atualmente",
        "restrição" : "14 anos",
        "lançamento" : "1999",
        "autor" : "eiichiro oda",
        "nome original" : "one piece",
    },
    
    "attack on titan" : {

        "episódios" : "97",
        "restrição" : "16 anos",
        "lançamento" : "2013",
        "autor" : "hajime isayama",
        "nome original " : "shingeki no kyojin",
    },

    "naruto" : {

        "episódios" : "220",
        "restrição" : "12 anos",
        "lançamento" : "2007",
        "autor" : "masashi kishimoto",
        "nome original" : "naruto classico",
    },

    "jujutsu kaisen" : {
        
        "episódios" : "96 atualmente",
        "restrição" : "16 anos",
        "lançamento" : "2020",
        "autor" : "gege akutami",
        "nome original" : "jujutsu kaisen",
    },
    
    "tokyo revengers" : {
        
        "episódios" : "100 atualmente",
        "restrição" : "16 anos",
        "lançamento" : "2021",
        "autor" : "kem wakui",
        "nome original" : "tokyo revengers",
    },

   "dragon ball z": {
        
        "episódios" : "291",
        "restrição" : "12 anos",
        "lançamento" : "1989",
        "autor" : "akira toriyama",
        "nome original" : "dragon ball z",
    },

    "demon sleyer" : {
        
        "episódios" : "63 atualmente",
        "restrição" : "16 anos",
        "lançamento" : "2019",
        "autor" : "koyoharu gotouge",
        "nome original" : "kimetsu no yaiba",
    },

    "solo leveling" : {
        
        "episódios" : "12 atualmente",
        "restrição" : "16 anos",
        "Lançamento" : "2024",
        "autor" : "jang sung-rak",
        "nome original" : "solo levening",
    },

    "black clover" : {
        
        "episódios" : "171 atualmente",
        "restrição" : "12 anos",
        "lançamento" : "2017",
        "autor" : "yūki tabata",
        "nome original" : "black clover",
    },

    "naruto shippuden" : {
        
        "episódios" : "500",
        "restrição" : "12 anos",
        "lançamento" : "2007",
        "autor" : "masashi kishimoto",
        "nome original" : "naruto shippuden",
    },
    
 }

def exibir(nome):
    if nome in animes:
        anime = animes[nome]
        print(f"nome: {nome}")
        print(f"episódios: {anime['episódios']}")
        print(f"restrição: {anime['restrição']}")
        print(f"lançamento: {anime['lançamento']}")
        print(f"autor: {anime['autor']}")
        print(f"nome original: {anime['nome original']}")
    
    else:
        print("Anime não encontrado")

nome_anime = input("Digite um anime: ").lower()

exibir(nome_anime)

    
















































