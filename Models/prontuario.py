from Models.DAO import DAO
from datetime import datetime

class Prontuario:
    def __init__(self, id, id_pet, id_doenca, data_entrada, data_saida, status):
        self.set_id(id) 
        self.set_id_pet(id_pet)
        self.set_id_doenca(id_doenca)
        self.set_data_entrada(data_entrada)
        self.set_data_saida(data_saida)
        self.set_status(status)

    def get_id(self): return self.__id
    def get_id_pet(self): return self.__id_pet
    def get_id_doenca(self): return self.__id_doenca
    def get_data_entrada(self): return self.__data_entrada
    def get_data_saida(self): return self.__data_saida
    def get_status(self): return self.__status

    def set_id(self, id):
        if (id > -1) and (id == int(id)): self.__id = id
        else: raise ValueError("ID deve ser um número inteiro positivo.")

    def set_id_pet(self, id_pet):
        if (id_pet > -1) and (id_pet == int(id_pet)): self.__id_pet = id_pet
        else: raise ValueError("ID deve ser um número inteiro positivo.")

    def set_id_doenca(self, id_doenca):
        if (id_doenca > -1) and (id_doenca == int(id_doenca)): self.__id_doenca = id_doenca
        else: raise ValueError("ID de doença deve ser um número inteiro positivo.")

    def set_data_entrada(self, data_entrada):
        if isinstance(data_entrada, datetime):
            self.__data_entrada = data_entrada
        else:
            self.__data_entrada = datetime.strptime(data_entrada, '%d/%m/%Y')

    def set_data_saida(self, data_saida):
        if data_saida is None or data_saida == "":
            self.__data_saida = ""
        else:
            # Se já for datetime, aceita. Se for string, converte.
            if isinstance(data_saida, datetime):
                self.__data_saida = data_saida
            else:
                self.__data_saida = datetime.strptime(data_saida, '%d/%m/%Y')

    def set_status(self, status):
        status = status.lower()
        if status in ["liberado", "interno", "óbito"]: self.__status = status
        else: raise ValueError("Status inválido.")
    
    def __str__(self):
        entrada = self.get_data_entrada().strftime('%d/%m/%Y')
        # Proteção: só usa strftime se for datetime, senão mostra vazio
        saida = self.get_data_saida().strftime('%d/%m/%Y') if isinstance(self.get_data_saida(), datetime) else ""
        return f"ID: {self.get_id()} - Pet: {self.get_id_pet()} - Entrada: {entrada} - Saída: {saida} - Status: {self.get_status()}"
    
    def to_json(self):
        return {
            "id": self.__id,
            "id_pet": self.__id_pet,
            "id_doenca": self.__id_doenca,
            # Converte para string para salvar no JSON
            "data_entrada": self.__data_entrada.strftime('%d/%m/%Y'),
            "data_saida": self.__data_saida.strftime('%d/%m/%Y') if isinstance(self.__data_saida, datetime) else "",
            "status": self.__status
        }
    
    @classmethod
    def from_json(cls, dic):
        return cls(
            dic.get("id"),
            dic.get("id_pet"),
            dic.get("id_doenca"),
            dic.get("data_entrada"),
            dic.get("data_saida", ""),
            dic.get("status")
        )

class ProntuarioDAO(DAO):
    def __init__(self):
        super().__init__(Prontuario, "Data/prontuario.json")