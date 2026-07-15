from Models.usuario import Usuario, UsuarioDAO
from Models.medicamentos import Medicamentos, MedicamentosDAO
from Models.aplicacao import Aplicacao, AplicacaoDAO
from Models.prontuario import Prontuario, ProntuarioDAO
from Models.doenca import Doenca, DoencaDAO
from Models.pet import Pet, PetDAO
from datetime import datetime

class View:

    # OPERAÇÕES USUÁRIOS: CRUD 

    @staticmethod
    def listar_usuarios():
        return UsuarioDAO().listar()    

    @staticmethod
    def criar_admim():
        for obj in View.listar_usuarios():
            if "admin@abc.com" in obj.get_email(): return
        View.inserir_usuario("Admin", "admin@abc.com", "admin123", "admin" )
    
    @staticmethod
    def autentica_usuario(email, senha):
        usuarios = UsuarioDAO().listar()
        for info in usuarios:
            if (info.get_email() == email) and (info.get_senha() == senha):
                return info.get_id()
        raise ValueError("Usuário ou senha inválidos.")
    
    @staticmethod
    def inserir_usuario(nome, email, senha, funcao):
        u= Usuario(0, nome, email, senha, funcao)
        UsuarioDAO().inserir(u)

    @staticmethod
    def listar_usuario_id(id):
        return UsuarioDAO().listar_id(id)
    
    @staticmethod
    def atualizar_usuario(id, nome, email, senha, funcao):
        u = Usuario(id, nome, email, senha, funcao)
        UsuarioDAO().atualizar(u)

    @staticmethod
    def excluir_usuario(id):
        UsuarioDAO().excluir(id)
    
    @staticmethod
    def listar_usuarios_nome_parcial(nome_parcial):
        todos_usuarios = UsuarioDAO().listar()
        return [u for u in todos_usuarios if nome_parcial.lower() in u.get_nome().lower()]
    
    #OPERAÇÕES MEDICAMENTOS: CRUD

    @staticmethod
    def listar_medicamentos():
        return MedicamentosDAO().listar()
    
    @staticmethod
    def inserir_medicamento(nome, descricao, quantidade, unidade_medida):
        m = Medicamentos(0, nome, descricao, quantidade, unidade_medida)
        MedicamentosDAO().inserir(m)

    @staticmethod
    def listar_medicamento_id(id):
        return MedicamentosDAO().listar_id(id)

    @staticmethod
    def atualizar_medicamento(id, nome, descricao, quantidade, unidade_medida):
        m = Medicamentos(id, nome, descricao, quantidade, unidade_medida)
        MedicamentosDAO().atualizar(m)

    @staticmethod
    def excluir_medicamento(id):
        MedicamentosDAO().excluir(id)
    
    @staticmethod
    def listar_medicamentos_nome_parcial(nome_parcial):
        todos_medicamentos = MedicamentosDAO().listar()
        return [m for m in todos_medicamentos if nome_parcial.lower() in m.get_nome().lower()]
    
    # OPERAÇÕES APLICAÇÃO: CRUD
    @staticmethod
    def listar_aplicacoes():
        return AplicacaoDAO().listar()
    
    @staticmethod
    def inserir_aplicacao(id_prontuario, id_medicamento, id_veterinario, id_auxiliar, dose_prescrita, instrucoes, status):
        medicamento = View.listar_medicamento_id(id_medicamento)
        if not medicamento:
            raise ValueError("Medicamento não encontrado.")
        
        if medicamento.get_quantidade() < dose_prescrita:
            raise ValueError(f"Atenção Veterinário: Estoque insuficiente para prescrição! Há apenas {medicamento.get_quantidade()} disponíveis.")
        
        a = Aplicacao(0, id_prontuario, id_medicamento, id_veterinario, id_auxiliar, dose_prescrita, instrucoes, status)
        AplicacaoDAO().inserir(a)

    @staticmethod
    def listar_aplicacao_id(id):
        return AplicacaoDAO().listar_id(id)
    
    @staticmethod
    def atualizar_aplicacao(id, id_prontuario, id_medicamento, id_veterinario, id_auxiliar, dose_prescrita, instrucoes, status):
        a = Aplicacao(id, id_prontuario, id_medicamento, id_veterinario, id_auxiliar, dose_prescrita, instrucoes, status)
        AplicacaoDAO().atualizar(a)
    
    @staticmethod
    def excluir_aplicacao(id):
        AplicacaoDAO().excluir(id)

    @staticmethod
    def listar_aplicacoes_por_prontuario(id_prontuario):
        todas_aplicacoes = AplicacaoDAO().listar()
        return [a for a in todas_aplicacoes if a.get_id_prontuario() == id_prontuario]
    
    @staticmethod
    def listar_aplicacoes_por_medicamento(id_medicamento):
        todas_aplicacoes = AplicacaoDAO().listar()
        return [a for a in todas_aplicacoes if a.get_id_medicamento() == id_medicamento]
    
    @staticmethod
    def listar_aplicacoes_por_nome_parcial(nome_parcial):
        todas_aplicacoes = AplicacaoDAO().listar()
        resultado = []
        for a in todas_aplicacoes:
            m = View.listar_medicamento_id(a.get_id_medicamento())
            if m and nome_parcial.lower() in m.get_nome().lower():
                resultado.append(a)
        return resultado
    
    @staticmethod
    def confirmar_aplicacao(id_aplicacao):
        aplicacao = AplicacaoDAO().listar_id(id_aplicacao)
        if not aplicacao:
            raise ValueError("Aplicação não encontrada.") 
        
        if aplicacao.get_status().lower() in ["cancelado"]:
            raise ValueError("Esta medicação foi cancelada e não pode ser aplicada!")
        
        if aplicacao.get_status().lower() in ["finalizado"]:
            raise ValueError("Esta medicação já foi registrada como aplicada!")

        
        medicamento = View.listar_medicamento_id(aplicacao.get_id_medicamento())
        if not medicamento:
            raise ValueError("Medicamento não encontrado no sistema.")
            
        dose = aplicacao.get_dose_prescrita()
        if medicamento.get_quantidade() < dose:
            raise ValueError(f"Estoque insuficiente! Temos apenas {medicamento.get_quantidade()} {medicamento.get_unidade_medida()} disponível.")
            
        
        novo_saldo = medicamento.get_quantidade() - dose
        medicamento.set_quantidade(novo_saldo)
        MedicamentosDAO().atualizar(medicamento)
        
        aplicacao.set_status("finalizado")
        AplicacaoDAO().atualizar(aplicacao)

    @staticmethod
    def listar_aplicacoes_pendentes():
        todas = AplicacaoDAO().listar()
        pendentes = [a for a in todas if a.get_status().lower() == "pendente"]

        if not pendentes:
            raise ValueError("Não há aplicações pendentes no momento.")
        
        texto = "=== Aplicações Pendentes ===\n"

        for a in pendentes:
            prontuario = View.listar_prontuario_id(a.get_id_prontuario())
            pet = View.listar_pet_id(prontuario.get_id_pet()) if prontuario else None
            medicamento = View.listar_medicamento_id(a.get_id_medicamento())
            texto += f"ID Aplicação: {a.get_id()} - Nome do Pet: {pet.get_nome() if pet else 'Desconhecido'} - Medicamento: {medicamento.get_nome() if medicamento else 'Desconhecido'} - Dose Prescrita: {a.get_dose_prescrita()} - Instruções: {a.get_instrucoes()} - Status: {a.get_status()}\n"
        
        return texto

    # OPERAÇÕES PET: CRUD

    @staticmethod
    def listar_pets():
        return PetDAO().listar()
    
    @staticmethod
    def inserir_pet(nome, especie, raca, idade, tutor):        
        p = Pet(0, nome, especie, raca, idade, tutor)
        PetDAO().inserir(p)

    @staticmethod
    def listar_pet_id(id):
        p = PetDAO().listar_id(id)
        if not p:
            raise ValueError("Pet não encontrado.")
        return p

    @staticmethod
    def atualizar_pet(id, nome, especie, raca, idade, tutor):
        p = Pet(id, nome, especie, raca, idade, tutor)
        PetDAO().atualizar(p)

    @staticmethod
    def excluir_pet(id):
        PetDAO().excluir(id)

    @staticmethod
    def listar_pets_nome_parcial(nome_parcial):
        todos_pets = PetDAO().listar()
        return [p for p in todos_pets if nome_parcial.lower() in p.get_nome().lower()]
    
    # OPERAÇÕES DOENÇA: CRUD

    @staticmethod
    def listar_doencas():
        return DoencaDAO().listar()

    @staticmethod
    def inserir_doenca(nome):
        d = Doenca(0, nome)
        DoencaDAO().inserir(d)

    @staticmethod
    def listar_doenca_id(id):
        return DoencaDAO().listar_id(id)

    @staticmethod
    def atualizar_doenca(id, nome):
        d = Doenca(id, nome)
        DoencaDAO().atualizar(d)

    @staticmethod
    def excluir_doenca(id):
        DoencaDAO().excluir(id)

    @staticmethod
    def listar_doencas_nome_parcial(nome_parcial):
        todas_doencas = DoencaDAO().listar()
        return [d for d in todas_doencas if nome_parcial.lower() in d.get_nome().lower()]
    
    # OPERAÇÕES PRONTUÁRIO: CRUD

    @staticmethod
    def listar_prontuarios():
        return ProntuarioDAO().listar()

    @staticmethod
    def inserir_prontuario(id_pet, id_doenca, data_entrada, status):
        p = Prontuario(0, id_pet, id_doenca, data_entrada, None, status)
        ProntuarioDAO().inserir(p)

    @staticmethod
    def listar_prontuario_id(id):
        p = ProntuarioDAO().listar_id(id)
        if not p:
            raise ValueError("Prontuário não encontrado.")
        pet = PetDAO().listar_id(p.get_id_pet())
        doenca = DoencaDAO().listar_id(p.get_id_doenca())
        nome_pet = pet.get_nome() if pet else "Desconhecido"
        nome_doenca = doenca.get_nome() if doenca else "Desconhecida"

        texto = f"ID Prontuário: {p.get_id()} - Nome do Pet: {nome_pet} - Doença: {nome_doenca} - Data de Entrada: {p.get_data_entrada().strftime('%d/%m/%Y')} - Data de Saída: {p.get_data_saida().strftime('%d/%m/%Y')} - Status: {p.get_status()}"

        return texto

    @staticmethod
    def atualizar_prontuario(id, id_pet, id_doenca, data_entrada, data_saida, status):
        p = Prontuario(id, id_pet, id_doenca, data_entrada, data_saida, status)
        ProntuarioDAO().atualizar(p)

    @staticmethod
    def excluir_prontuario(id):
        ProntuarioDAO().excluir(id)
        
    @staticmethod
    def dar_alta_prontuario(id):
        p = ProntuarioDAO().listar_id(id)
        if p:
            p.set_status("liberado")
            p.set_data_saida(datetime.now().strftime("%d/%m/%Y"))
            ProntuarioDAO().atualizar(p)

    @staticmethod
    def listar_internos():
        todos = ProntuarioDAO().listar()
        ativos = [p for p in todos if p.get_status().lower() == "interno"]

        if not ativos:
            raise ValueError("Não há pacientes internos no momento.")
        
        texto = "=== Pacientes Internos ===\n"

        for p in ativos:
            pet = View.listar_pet_id(p.get_id_pet())
            doenca = View.listar_doenca_id(p.get_id_doenca())
            texto += f"ID Prontuário: {p.get_id()} - Nome do Pet: {pet.get_nome()} - Doença: {doenca.get_nome()} - Data de Entrada: {p.get_data_entrada().strftime('%d/%m/%Y')} - Status: {p.get_status()}\n"

        return texto
    
