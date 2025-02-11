from random import randint
import requests

class Pokemon:
    pokemons = {} # { username : pokemon}
    # Inisialisasi objek (konstruktor)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()

        self.power = randint(30, 60)
        self.hp = randint(200, 400)

        Pokemon.pokemons[pokemon_trainer] = self

    # Metode untuk mendapatkan gambar pokemon melalui API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['sprites']["other"]['official-artwork']["front_default"])
        else:
            return "https://static.wikia.nocookie.net/anime-characters-fight/images/7/77/Pikachu.png/revision/latest/scale-to-width-down/700?cb=20181021155144&path-prefix=ru"
    
    # Metode untuk mendapatkan nama pokemon melalui API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Metode untuk mendapatkan informasi
    def info(self):
        return f"""Nama pokemon kamu: {self.name}
Kekuatan pokemon: {self.power}
Kesehatan pokemon: {self.hp}"""

    # Metode untuk mendapatkan gambar pokemon
    def show_img(self):
        return self.img
    
    def attack(self, enemy):
        if isinstance(enemy, Wizard):
            chance = randint(1,5)
            if chance == 1:
                return "Pokemon-penyihir menggunakan perisai dalam pertarungan"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"""Pertarungan antara @{self.pokemon_trainer} dan @{enemy.pokemon_trainer}
Kesehatan @{enemy.pokemon_trainer} sekarang {enemy.hp}"""
        else:
            enemy.hp = 0
            return f"Kemenangan untuk @{self.pokemon_trainer} melawan @{enemy.pokemon_trainer}! "

class Wizard(Pokemon):
  pass


class Fighter(Pokemon):
    def attack(self, enemy):
        super_power = randint(5,15)
        self.power += super_power
        result = super().attack(enemy)
        self.power -= super_power
        return result + f"\nPetarung menggunakan serangan super dengan kekuatan: {super_power} "
