from shutil import move as moverArquivoDePasta
import SystemPath as sp

for arquivo in sp.pastaDownloads.glob('*'):
    categoriaDoArquivo = sp.acharCategoriaArquivo(arquivo.suffix[1:])
    
    if categoriaDoArquivo != "None":
        novoDiretorioDoArquivo = sp.Path(sp.pastaDownloads, categoriaDoArquivo)

        novoDiretorioDoArquivo.mkdir(parents=True, exist_ok=True)
        moverArquivoDePasta(arquivo, novoDiretorioDoArquivo)
