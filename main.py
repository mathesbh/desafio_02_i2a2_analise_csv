from processador_zip import LeitorNotasFiscais

def main():
    leitor = LeitorNotasFiscais("202401_NFs.zip")
    leitor.extrair_arquivos()
    leitor.carregar_dados_csv()
    leitor.montar_objetos_notas()

if __name__ == "__main__":
    main()
