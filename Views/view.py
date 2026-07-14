from Models.usuario import Usuario, UsuarioDAO
from Models.medicamentos import Medicamentos, MedicamentosDAO
from Models.aplicacao import Aplicacao, AplicacaoDAO
from Models.prontuario import Prontuario, ProntuarioDAO
from Models.doenca import Doenca, DoencaDAO
from Models.pet import Pet, PetDAO
from datetime import datetime

class View:

    @staticmethod
    def listar_usuarios():
        return UsuarioDAO().listar()

    @staticmethod
    def criar_admim():
        ...
    
    @staticmethod
    def autentica_usuario(email, senha):
        ...
