import re

source_path = "publish_v5_FINAL.py"
target_path = "publish_v6_FIXED.py"

try:
    with open(source_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex para encontrar a linha quebrada
    # Procura por: f'git commit ... "{args.name}""' (com aspa dupla extra)
    # Substitui por: f'git commit ... "{args.name}"' (sem aspa dupla extra)
    
    # Padrão errado específico que os agentes estavam gerando
    bad_pattern = r'run_command(f\'git commit -m \"Publish: {args.name}\"", cwd=os.getcwd())'
    
    # Padrão correto
    good_pattern = r"run_command(f'git commit -m \"Publish: {args.name}\"', cwd=os.getcwd())"
    
    new_content = re.sub(bad_pattern, good_pattern, content)
    
    # Verificação de segurança: Se nada mudou, algo está errado com o regex ou o arquivo já estava certo (improvável)
    if new_content == content:
        print("Aviso: Nenhuma substituição feita. Verificando padrão alternativo...")
        # Tenta um replace direto de string caso o regex falhe por escape
        bad_string = "run_command(f'git commit -m \"Publish: {args.name}\"", cwd=os.getcwd())"
        good_string = "run_command(f'git commit -m \"Publish: {args.name}\"', cwd=os.getcwd())"
        new_content = content.replace(bad_string, good_string)

    with open(target_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
        
    print(f"Sucesso! {target_path} gerado com a correção.")

except FileNotFoundError:
    print(f"Erro: Arquivo {source_path} não encontrado.")
