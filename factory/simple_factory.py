from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):

    @abstractmethod
    def falar(self):
        pass

class Cachorro(Animal):
    def falar(self):
        print('Au Au!')

class Gato(Animal):
    def falar(self):
        print('Miau')


class Fabrica:
    def criar_animal_falante(self, tipo):

        # O comando eval avalia uma string e tenta executar
        # como um comando python. Exemplo:
        # eval(tipo)() => eval('Cachorro')() => Cachorro()
        
        return eval(tipo)()
    

if __name__ == '__main__':
    fabrica = Fabrica()
    animal = input('Qual animal você quer que fale? [Cachorro, Gato]')
    objeto = fabrica.criar_animal_falante(animal)
    objeto.falar()