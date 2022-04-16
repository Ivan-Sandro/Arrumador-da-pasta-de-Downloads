from bisect import bisect_left
from pathlib import Path

extensoesENomes = (
    (("Executaveis"         ), ["exe", "msi", "jar"]),
    (("Compactados"         ), ["zip", "rar", "arc", "arj", "bin", "dmg", "gz", "gzip", "hqx", "sit", "sitx", "se", "ace", "uu", "uue", "7z"]),
    (("Videos"              ), ["mp4", "mov", "avi", "flv", "mwv", "mpeg", "mkv", "asf", "rm", "rmvb", "vob", "ts", "dat"]),
    (("Textos"              ), ["txt", "pdf"]),
    (("Imagens"             ), ["png", "gif", "jpg", "jpeg", "tiff", "tif", "raw", "bmp", "psd", "eps", "svg", "ai", "pic", "wmf", "webp", "dwg", "pptx", "odp"]),
    (("Words"               ), ["docx", "docm", "dotx", "dotm", "doc", "dot", "odf", "odt"]),
    (("Programação"         ), ["lib", "css", "html", "js", "cpp", "c", "h", "hpp", "py"]),
    (("Arquivos de dados"   ), ["ini", "log"]),
    (("Máquinas Virtuais"   ), ["ova"])
)

def acharCategoriaArquivo(extensao):
    global extensoesENomes
    for X in range(len(extensoesENomes)):
        if extensao in extensoesENomes[X][1]:
            return extensoesENomes[X][0]
    
    return "None"

def lerDiretoriosArquivo(nomeArquivo):

    if not Path(nomeArquivo).is_file():
        with open(nomeArquivo, 'a'):
            pass

    with open(nomeArquivo, 'r') as arquivo:
        diretorios = set(map(lambda diretorio: Path(diretorio.replace('\n','')), arquivo.readlines()))
    
    return diretorios

def getTamanhoExtensaoRepetisao(arquivo : Path):
    tamanhoExtensao = 0
    for letra in arquivo.stem[::-1]:
        if letra == ')' or letra.isdigit():
            tamanhoExtensao += 1
        elif letra == '(':
            tamanhoExtensao += 2
            break
        else:
            tamanhoExtensao = 0
            break
    
    return tamanhoExtensao

def getNumeroExtensaoRepetisao(arquivo : Path):
    tamanhoExtensaoRepetisao = getTamanhoExtensaoRepetisao(arquivo)
    if tamanhoExtensaoRepetisao == 0:
        return 0
    else:
        return int(arquivo.stem[-tamanhoExtensaoRepetisao+2:-1])

def removerExtensaoRepetisao(arquivo : Path):
    tamanhoExtensaoRepetisao = getTamanhoExtensaoRepetisao(arquivo)
    if tamanhoExtensaoRepetisao == 0:
        return arquivo.stem
    else:
        return arquivo.stem[0:-tamanhoExtensaoRepetisao]

def checarArquivoRepetido(arquivo : Path, diretorio : Path):
    for arquivoDiretorio in diretorio.glob(f"*{arquivo.suffix}"):
        if arquivo.stem == arquivoDiretorio.stem:
            return True

    return False

def getNovoNomeArquivoRepetido(arquivo : Path, diretorio : Path):
    NumeroExtensaoPossivel = 0
    nomeArquivoSemExtensaoRepetisao = removerExtensaoRepetisao(arquivo)

    for arquivoDiretorio in diretorio.glob(f"*{arquivo.suffix}"):
        if nomeArquivoSemExtensaoRepetisao == removerExtensaoRepetisao(arquivoDiretorio):
            numeroExtensaoDiretorio = getNumeroExtensaoRepetisao(arquivoDiretorio)

            if (NumeroExtensaoPossivel == numeroExtensaoDiretorio-1):
                NumeroExtensaoPossivel = numeroExtensaoDiretorio
            else:
                break

    return f"{removerExtensaoRepetisao(arquivo)} ({str(NumeroExtensaoPossivel+1)}){arquivo.suffix}"