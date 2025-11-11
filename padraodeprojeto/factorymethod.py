from abc import ABC, abstractmethod


# Interface comum para os produtos (Veículos)
class Veiculo(ABC):
    @abstractmethod
    def dirigir(self) -> str:
        pass


# Produtos concretos
class Carro(Veiculo):
    def dirigir(self) -> str:
        return "Dirigindo um carro"


class Moto(Veiculo):
    def dirigir(self) -> str:
        return "Pilotando uma moto"


# Superclasse Creator (define o método fábrica)
class VeiculoCreator(ABC):

    @abstractmethod
    def factory_method(self) -> Veiculo:
        """Cada subclasse deve implementar este método para criar o produto certo"""
        pass

# Subclasses concretas do Creator
class CarroCreator(VeiculoCreator):
    def factory_method(self) -> Veiculo:
        return Carro()


class MotoCreator(VeiculoCreator):
    def factory_method(self) -> Veiculo:
        return Moto()


# Código cliente (não precisa saber qual criador está sendo usado)
def client_code(creator: VeiculoCreator):
    print(f"Cliente: não sei qual criador estou usando, mas funciona.\n{creator.factory_method()}")


# Execução principal
if __name__ == "__main__":
    print("App: Usando o CarroCreator.")
    client_code(CarroCreator())

    print("\nApp: Usando o MotoCreator.")
    client_code(MotoCreator())
