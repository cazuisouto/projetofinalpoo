import json
from Views.view import View

class UI:
    @staticmethod
    def main():
        View.criar_admim() 
        
        while True:
            print("\n" + "="*40)
            print("🐾 SISTEMA VETERINÁRIO - LOGIN 🐾")
            print("="*40)
            email = input("E-mail (ou 'sair'): ")
            
            if email.lower() == 'sair':
                print("Encerrando o sistema...")
                break
                
            senha = input("Senha: ")
            
            try:
                user_id = View.autentica_usuario(email, senha)
                usuario = View.listar_usuario_id(user_id)
                funcao = usuario.get_funcao().lower()
                
                print(f"\n✅ Bem-vindo(a), {usuario.get_nome()}!")
                
                if "admin" in funcao:
                    UI.menu_admin()
                elif "auxiliar" in funcao:
                    UI.menu_auxiliar(user_id)
                elif "veterin" in funcao:
                    UI.menu_veterinario(user_id)
                else:
                    print("Perfil de acesso não reconhecido.")
                    
            except ValueError as e:
                print(f"\n❌ Erro: {e}")

    # ==========================================
    # MENU DO ADMINISTRADOR
    # ==========================================
    @staticmethod
    def menu_admin():
        while True:
            print("\n" + "="*30)
            print("👤 MENU ADMINISTRADOR")
            print("="*30)
            print("1 - Gerenciar Usuários")
            print("2 - Gerenciar Estoque/Medicamentos")
            print("0 - Fazer Logout")
            
            op = input("\nEscolha uma opção: ")
            
            if op == "0":
                break
                
            elif op == "1":
                print("\n--- GERENCIAR USUÁRIOS ---")
                print("1. Listar Todos | 2. Buscar por Nome | 3. Cadastrar | 4. Atualizar | 5. Excluir")
                sub_op = input("Opção: ")
                
                if sub_op == "1":
                    usuarios = [u.to_json() for u in View.listar_usuarios()]
                    print(json.dumps(usuarios, indent=4, ensure_ascii=False))
                
                elif sub_op == "2":
                    nome = input("Digite parte do nome: ")
                    usuarios = [u.to_json() for u in View.listar_usuarios_nome_parcial(nome)]
                    print(json.dumps(usuarios, indent=4, ensure_ascii=False) if usuarios else "Nenhum encontrado.")
                
                elif sub_op == "3":
                    nome = input("Nome: ")
                    email = input("E-mail: ")
                    senha = input("Senha: ")
                    funcao = input("Função (Admin/Veterinario/Auxiliar): ")
                    View.inserir_usuario(nome, email, senha, funcao)
                    print("✅ Usuário cadastrado com sucesso!")
                    
                elif sub_op == "4":
                    try:
                        id_usu = int(input("ID do usuário a atualizar: "))
                        nome = input("Novo Nome: ")
                        email = input("Novo E-mail: ")
                        senha = input("Nova Senha: ")
                        funcao = input("Nova Função: ")
                        View.atualizar_usuario(id_usu, nome, email, senha, funcao)
                        print("✅ Usuário atualizado com sucesso!")
                    except ValueError:
                        print("❌ Erro numérico.")
                        
                elif sub_op == "5":
                    try:
                        id_usu = int(input("ID do usuário a excluir: "))
                        View.excluir_usuario(id_usu)
                        print("✅ Usuário excluído!")
                    except ValueError:
                        print("❌ Erro numérico.")

            elif op == "2":
                print("\n--- GERENCIAR MEDICAMENTOS ---")
                print("1. Listar Todos | 2. Buscar por Nome | 3. Cadastrar | 4. Atualizar | 5. Excluir")
                sub_op = input("Opção: ")
                
                if sub_op == "1":
                    meds = [m.to_json() for m in View.listar_medicamentos()]
                    print(json.dumps(meds, indent=4, ensure_ascii=False))
                    
                elif sub_op == "2":
                    nome = input("Digite parte do nome: ")
                    meds = [m.to_json() for m in View.listar_medicamentos_nome_parcial(nome)]
                    print(json.dumps(meds, indent=4, ensure_ascii=False) if meds else "Nenhum encontrado.")
                    
                elif sub_op == "3":
                    try:
                        nome = input("Nome: ")
                        desc = input("Descrição: ")
                        qtd = float(input("Quantidade: "))
                        und = input("Unidade de medida: ")
                        View.inserir_medicamento(nome, desc, qtd, und)
                        print("✅ Medicamento inserido!")
                    except ValueError:
                        print("❌ Erro numérico.")
                        
                elif sub_op == "4":
                    try:
                        id_med = int(input("ID do medicamento a atualizar: "))
                        nome = input("Novo Nome: ")
                        desc = input("Nova Descrição: ")
                        qtd = float(input("Nova Quantidade: "))
                        und = input("Nova Unidade: ")
                        View.atualizar_medicamento(id_med, nome, desc, qtd, und)
                        print("✅ Medicamento atualizado!")
                    except ValueError:
                        print("❌ Erro numérico.")
                        
                elif sub_op == "5":
                    try:
                        id_med = int(input("ID do medicamento a excluir: "))
                        View.excluir_medicamento(id_med)
                        print("✅ Medicamento excluído!")
                    except ValueError:
                        print("❌ Erro numérico.")

    # ==========================================
    # MENU DO VETERINÁRIO
    # ==========================================
    @staticmethod
    def menu_veterinario(id_veterinario):
        while True:
            print("\n" + "="*30)
            print("🩺 MENU VETERINÁRIO")
            print("="*30)
            print("1 - Gerenciar Pets")
            print("2 - Gerenciar Doenças")
            print("3 - Gerenciar Prontuários")
            print("4 - Prescrever Medicação")
            print("5 - Dar Alta a um Paciente")
            print("6 - Ver Pacientes Internados")
            print("0 - Fazer Logout")
            
            op = input("\nEscolha uma opção: ")
            
            if op == "0":
                break
                
            elif op == "1":
                print("\n--- GERENCIAR PETS ---")
                print("1. Listar | 2. Buscar por Nome | 3. Cadastrar | 4. Atualizar | 5. Excluir")
                sub_op = input("Opção: ")
                if sub_op == "1":
                    pets = [p.to_json() for p in View.listar_pets()]
                    print(json.dumps(pets, indent=4, ensure_ascii=False))
                elif sub_op == "2":
                    nome = input("Digite parte do nome: ")
                    pets = [p.to_json() for p in View.listar_pets_nome_parcial(nome)]
                    print(json.dumps(pets, indent=4, ensure_ascii=False) if pets else "Nenhum encontrado.")
                elif sub_op == "3":
                    try:
                        View.inserir_pet(input("Nome: "), input("Espécie: "), input("Raça: "), int(input("Idade: ")), input("Tutor: "))
                        print("✅ Pet cadastrado!")
                    except ValueError:
                        print("❌ Idade deve ser número.")
                elif sub_op == "4":
                    try:
                        View.atualizar_pet(int(input("ID: ")), input("Novo Nome: "), input("Nova Espécie: "), input("Nova Raça: "), int(input("Nova Idade: ")), input("Novo Tutor: "))
                        print("✅ Pet atualizado!")
                    except ValueError:
                        print("❌ Erro numérico.")
                elif sub_op == "5":
                    try:
                        View.excluir_pet(int(input("ID a excluir: ")))
                        print("✅ Pet excluído!")
                    except ValueError:
                        print("❌ Erro numérico.")

            elif op == "2":
                print("\n--- GERENCIAR DOENÇAS ---")
                print("1. Listar | 2. Buscar por Nome | 3. Cadastrar | 4. Atualizar | 5. Excluir")
                sub_op = input("Opção: ")
                if sub_op == "1":
                    doencas = [d.to_json() for d in View.listar_doencas()]
                    print(json.dumps(doencas, indent=4, ensure_ascii=False))
                elif sub_op == "2":
                    nome = input("Digite parte do nome: ")
                    doencas = [d.to_json() for d in View.listar_doencas_nome_parcial(nome)]
                    print(json.dumps(doencas, indent=4, ensure_ascii=False) if doencas else "Nenhuma encontrada.")
                elif sub_op == "3":
                    View.inserir_doenca(input("Nome da doença: "))
                    print("✅ Doença cadastrada!")
                elif sub_op == "4":
                    try:
                        View.atualizar_doenca(int(input("ID: ")), input("Novo Nome: "))
                        print("✅ Doença atualizada!")
                    except ValueError:
                        print("❌ Erro numérico.")
                elif sub_op == "5":
                    try:
                        View.excluir_doenca(int(input("ID: ")))
                        print("✅ Doença excluída!")
                    except ValueError:
                        print("❌ Erro numérico.")

            elif op == "3":
                print("\n--- GERENCIAR PRONTUÁRIOS ---")
                print("1. Listar Todos | 2. Internar (Abrir) | 3. Atualizar | 4. Excluir")
                sub_op = input("Opção: ")
                if sub_op == "1":
                    try:
                        prontuarios = [p.to_json() for p in View.listar_prontuarios()]
                        print(json.dumps(prontuarios, indent=4, ensure_ascii=False))
                    except Exception as e:
                        print(f"Erro: {e}")
                elif sub_op == "2":
                    try:
                        View.inserir_prontuario(int(input("ID Pet: ")), int(input("ID Doença: ")), input("Data Entrada: "), "interno")
                        print("✅ Prontuário aberto!")
                    except ValueError:
                        print("❌ IDs devem ser números.")
                elif sub_op == "3":
                    try:
                        View.atualizar_prontuario(int(input("ID Prontuário: ")), int(input("Novo ID Pet: ")), int(input("Novo ID Doença: ")), input("Data Entrada: "), input("Data Saída: "), input("Status: "))
                        print("✅ Prontuário atualizado!")
                    except ValueError:
                        print("❌ Erro numérico.")
                elif sub_op == "4":
                    try:
                        View.excluir_prontuario(int(input("ID: ")))
                        print("✅ Prontuário excluído!")
                    except ValueError:
                        print("❌ Erro numérico.")

            elif op == "4":
                try:
                    View.inserir_aplicacao(int(input("ID Prontuário: ")), int(input("ID Medicamento: ")), id_veterinario, 0, float(input("Dose: ")), input("Instruções: "), "Pendente")
                    print("✅ Prescrição registrada!")
                except ValueError as e:
                    print(f"❌ Erro: {e}")

            elif op == "5":
                try:
                    View.dar_alta_prontuario(int(input("ID do Prontuário: ")))
                    print("✅ Paciente liberado!")
                except ValueError:
                    print("❌ Erro numérico.")

            elif op == "6":
                try:
                    print("\n" + View.listar_internos())
                except ValueError as e:
                    print(f"\nℹ️ {e}")

    # ==========================================
    # MENU DO AUXILIAR
    # ==========================================
    @staticmethod
    def menu_auxiliar(id_auxiliar):
        while True:
            print("\n" + "="*30)
            print("🩹 MENU AUXILIAR VETERINÁRIO")
            print("="*30)
            print("1 - Ver Medicações Pendentes")
            print("2 - Confirmar Aplicação de Remédio (Baixa Estoque)")
            print("3 - Listar Todas as Aplicações (Histórico)")
            print("0 - Fazer Logout")
            
            op = input("\nEscolha uma opção: ")
            
            if op == "0":
                break
                
            elif op == "1":
                try:
                    print("\n" + View.listar_aplicacoes_pendentes())
                except ValueError as e:
                    print(f"\nℹ️ {e}")
                    
            elif op == "2":
                try:
                    print("\n" + View.listar_aplicacoes_pendentes())
                    id_app = int(input("\nDigite o ID da aplicação administrada: "))
                    app = View.listar_aplicacao_id(id_app)
                    app.set_id_auxiliar(id_auxiliar)
                    View.confirmar_aplicacao(id_app)
                    print("✅ Aplicação confirmada e estoque reduzido!")
                except ValueError as e:
                    print(f"\n❌ ERRO: {e}")
                    
            elif op == "3":
                apps = [a.to_json() for a in View.listar_aplicacoes()]
                print(json.dumps(apps, indent=4, ensure_ascii=False) if apps else "Nenhuma aplicação registrada.")

if __name__ == "__main__":
    UI.main()