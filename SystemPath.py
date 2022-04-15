from bisect import bisect_left
from pathlib import Path

extensoesENomes = (
    (["exe", "msi", "jar"],                                                                                                             ("Executaveis"         )),
    (["zip", "rar", "arc", "arj", "bin", "dmg", "gz", "gzip", "hqx", "sit", "sitx", "se", "ace", "uu", "uue", "7z"],                    ("Compactados"         )),
    (["mp4", "mov", "avi", "flv", "mwv", "mpeg", "mkv", "asf", "rm", "rmvb", "vob", "ts", "dat"],                                       ("Videos"              )),
    (["txt", "pdf"],                                                                                                                    ("Textos"              )),
    (["png", "gif", "jpg", "jpeg", "tiff", "tif", "raw", "bmp", "psd", "eps", "svg", "ai", "pic", "wmf", "webp", "dwg", "pptx", "odp"], ("Imagens"             )),
    (["docx", "docm", "dotx", "dotm", "doc", "dot", "odf", "odt"],                                                                      ("Words"               )),
    (["lib", "css", "html", "js", "cpp", "c", "h", "hpp", "py"],                                                                        ("Programação"         )),
    (["ini", "log"],                                                                                                                    ("Arquivos de dados"   )),
    (["ova"],                                                                                                                           ("Máquinas Virtuais"   ))
)

def colocarExtensoesENomesEmOrdemAlfabetica():
    global extensoesENomes
    for X in range(len(extensoesENomes)):
        extensoesENomes[X][0].sort()

colocarExtensoesENomesEmOrdemAlfabetica()

def pesquisaBinaria(elemento, vetorDeElementos):
    possivelLocal = bisect_left(vetorDeElementos, elemento)
    
    return possivelLocal if possivelLocal < len(vetorDeElementos) and vetorDeElementos[possivelLocal] == elemento else -1

def acharCategoriaArquivo(extensao):
    global extensoesENomes
    for X in range(len(extensoesENomes)):
        if pesquisaBinaria(extensao, extensoesENomes[X][0]) != -1:
            return extensoesENomes[X][1]

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
            tamanhoExtensao += 1
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
        return int(arquivo.stem[-tamanhoExtensaoRepetisao+1:-1])

def removerExtensaoRepetisao(arquivo : Path):
    tamanhoExtensaoRepetisao = getTamanhoExtensaoRepetisao(arquivo)
    if tamanhoExtensaoRepetisao == 0:
        return arquivo.stem
    else:
        return arquivo.stem[0:-tamanhoExtensaoRepetisao-1]

def checarArquivoRepetido(arquivo : Path, diretorio : Path):
    for arquivoDiretorio in diretorio.glob(f"*{arquivo.suffix}"):
        if arquivo.stem == arquivoDiretorio.stem:
            return True

    return False

def getNovoNomeArquivoRepetido(arquivo : Path, diretorio : Path):
    maiorNumeroExtensao = 0
    nomeArquivoSemExtensaoRepetisao = removerExtensaoRepetisao(arquivo)

    for arquivoDiretorio in diretorio.glob(f"*{arquivo.suffix}"):
        if nomeArquivoSemExtensaoRepetisao == removerExtensaoRepetisao(arquivoDiretorio):
            numeroExtensao = getNumeroExtensaoRepetisao(arquivoDiretorio)

            if (maiorNumeroExtensao < numeroExtensao):
                maiorNumeroExtensao = numeroExtensao

    return f"{removerExtensaoRepetisao(arquivo)} ({str(maiorNumeroExtensao+1)}){arquivo.suffix}"