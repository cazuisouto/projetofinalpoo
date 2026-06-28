from DAO import DAO
class Usuario:
    def __init__(self, id, nome, email, senha, funcao):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_senha(senha)
        self.set_funcao(funcao)

    def get_id(self):          return self.__id
    def get_nome(self):        return self.__nome
    def get_email(self):       return self.__email
    def get_senha(self):       return self.__senha
    def get_funcao(self):      return self.__funcao

    def set_id(self, id):
        if (id > -1) and (id == int(id)):
            self.__id = id
        else:
            raise ValueError("ID deve ser um número inteiro positivo.")
        
    def set_nome(self, nome):
        if (nome != "") and (isinstance(nome, str)):
            self.__nome = nome
        else:
            raise ValueError("Nome deve ser do tipo string  e não pode ser vazia.")
        
    def set_email(self, email):
        if (email != "") and ("@" in email) and ("." in email) and (isinstance(email, str)):
            self.__email = email
        else:
            raise ValueError("Digite um email válido.")
        
    def set_senha(self, senha):
        if (senha != "") and (len(senha) >= 6):
            self.__senha = senha
        else:
            raise ValueError("A senha deve conter pelo menos 6 caracteres.")
        
    def set_funcao(self, funcao):
        opcoes_validas = ["admin", "veterinário", "veterinária", "auxiliar veterinário"]

        if funcao.lower() in opcoes_validas:
            self.__funcao = funcao
        else:
            raise ValueError("Função inválida. Opções válidas: admin, veterinário, veterinária, auxiliar veterinário")
        
    def __str__(self):
        return f"ID: {self.get_id()} - Nome: {self.get_nome()} - Email: {self.get_email()} - Função: {self.get_funcao()}"

    def to_json(self):
        return {
            "id": self.get_id(),
            "nome": self.get_nome(),
            "email": self.get_email(),
            "senha": self.get_senha(),
            "funcao": self.get_funcao()
        }

    @staticmethod    
    def from_json(dic):
        return Usuario(dic["id"], dic["nome"], dic["email"], dic["senha"], dic["funcao"])