from bisect import bisect_left
from pathlib import Path

pastaDownloads = Path("\\Downloads")

extensoesENomes = (
    (["exe", "msi", "jar"],                                                                                              ("Executaveis"         )),
    (["zip", "rar", "arc", "arj", "bin", "dmg", "gz", "gzip", "hqx", "sit", "sitx", "se", "ace", "uu", "uue", "7z"],     ("Compactados"         )),
    (["mp4", "mov", "avi", "flv", "mwv", "mpeg", "mkv", "asf", "rm", "rmvb", "vob", "ts", "dat"],                        ("Videos"              )),
    (["txt", "pdf"],                                                                                                     ("Textos"              )),
    (["png", "gif", "jpg", "jpeg", "tiff", "tif", "raw", "bmp", "psd", "eps", "svg", "ai", "pic", "wmf", "webp", "dwg"], ("Imagens"             )),
    (["docx", "docm", "dotx", "dotm", "doc", "dot", "odf"],                                                              ("Words"               )),
    (["lib", "css", "html", "js", "cpp", "c", "h", "hpp", "py"],                                                         ("Programação"         )),
    (["ini", "log"],                                                                                                     ("Arquivos de dados"   )),
    (["ova"],                                                                                                            ("Máquinas Virtuais"   ))
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
    