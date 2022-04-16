from shutil import move as moverArquivoDePasta
import SystemPath as sp

diretorios = sp.lerDiretoriosArquivo("diretorios.txt")

for diretorio in diretorios:
    if not diretorio.is_dir():
        continue

    for arquivo in diretorio.glob('*'):

        if arquivo.is_dir():
            if sp.isPastaUmaPastaDoPrograma(arquivo) is True:
                continue

            categoriaDoArquivo = sp.acharCategoriaArquivo("pasta")
        else:
            categoriaDoArquivo = sp.acharCategoriaArquivo(arquivo.suffix[1:])    

        novoDiretorioDoArquivo = sp.Path(diretorio, categoriaDoArquivo)

        if not novoDiretorioDoArquivo.is_dir():
            novoDiretorioDoArquivo.mkdir(parents=True, exist_ok=True)

        if sp.checarArquivoRepetido(arquivo, novoDiretorioDoArquivo) == True:
            arquivo = arquivo.rename(sp.Path(arquivo.parent, sp.getNovoNomeArquivoRepetido(arquivo, novoDiretorioDoArquivo)))

        moverArquivoDePasta(arquivo, novoDiretorioDoArquivo)

            

