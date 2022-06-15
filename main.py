from functions import write_discrepancies
import os

# ███████╗ ██████╗ ███╗   ██╗ █████╗ ██████╗     ███████╗ ██████╗██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
# ██╔════╝██╔═══██╗████╗  ██║██╔══██╗██╔══██╗    ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
# ███████╗██║   ██║██╔██╗ ██║███████║██████╔╝    ███████╗██║     ██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
# ╚════██║██║   ██║██║╚██╗██║██╔══██║██╔══██╗    ╚════██║██║     ██╔══██╗██╔══██║██╔═══╝ ██╔═══╝ ██╔══╝  ██╔══██╗
# ███████║╚██████╔╝██║ ╚████║██║  ██║██║  ██║    ███████║╚██████╗██║  ██║██║  ██║██║     ██║     ███████╗██║  ██║
# ╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚══════╝╚═╝  ╚═╝
# V0.1

############# ALTERE SOMENTE ESSA VARIÁVEL
DIRETORIO_DE_INSTALACAO = r'C:\Users\balbi\Desktop\ger5'
############# 
DIRETORIO_DE_RELATORIOS = 'reports'
############# 

if __name__ == "__main__":
    os.chdir(DIRETORIO_DE_INSTALACAO)
    actual_dir = os.listdir()

    files_to_judge = [filename for filename in actual_dir if filename.endswith('.html')] 
    
    if not DIRETORIO_DE_RELATORIOS in actual_dir: 
        os.mkdir(DIRETORIO_DE_RELATORIOS)
    
    for file in files_to_judge:
        write_discrepancies(file, name=file, path=DIRETORIO_DE_RELATORIOS)

