
# Extrator

O "Extrator" é uma aplicação desenvolvida em Python utilizando a biblioteca Tkinter, que facilita a extração e transformação de dados de arquivos PDF para formatos CSV. O software é especialmente útil para processar grandes volumes de documentos PDF que contêm dados tabulares, como folhas de pagamento, e convertê-los em um formato mais acessível e manipulável.

## Funcionalidades

- **Importação de Arquivos PDF**: Permite ao usuário selecionar e importar múltiplos arquivos PDF simultaneamente.
- **Extração de Dados**: Extrai informações específicas como período, salário, adicionais noturnos e horas extras, organizando-as em colunas predefinidas.
- **Geração de Arquivos CSV**: Cada PDF processado é convertido em um arquivo CSV correspondente, facilitando análises e manipulações futuras dos dados.
- **Interface Gráfica Amigável**: Utiliza uma interface gráfica baseada no Tkinter e ttkbootstrap para uma experiência de usuário simples e direta.
- **Barra de Progresso**: Inclui uma barra de progresso que indica o avanço do processamento dos arquivos.

## Como Usar

1. Execute o programa.
2. Clique no botão "Importar todos PDFs" e selecione os arquivos que deseja processar.
3. Aguarde enquanto o programa processa os arquivos e os converte em CSV.
4. Ao finalizar, uma mensagem indicará onde os arquivos CSV foram salvos.

## Dependências

Para utilizar o "Extrator", é necessário ter as seguintes bibliotecas instaladas:

- `tkinter`
- `PyPDF2`
- `pandas`
- `ttkbootstrap`

Você pode instalar todas as dependências necessárias através do comando:

```bash
pip install PyPDF2 pandas ttkbootstrap
```

## Contribuições

Contribuições são sempre bem-vindas! Sinta-se à vontade para clonar, forkar ou enviar pull requests para melhorar o "Extrator".

