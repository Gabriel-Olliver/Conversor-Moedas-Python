# Conversor-Moedas-Python

Aplicação desktop em Python para conversão de valores entre moedas, com cotações atualizadas em tempo real e interface gráfica construída com CustomTkinter.

## Sobre o projeto

O usuário escolhe a moeda de origem, digita o valor a ser convertido e a moeda de destino é carregada de acordo com as conversões disponíveis para a origem selecionada. Ao clicar em "Converter", a aplicação consulta a cotação atual em uma API pública e exibe o resultado na tela.

## Funcionalidades

- Seleção da moeda de origem e da moeda de destino por menus
- Lista de destinos atualizada automaticamente conforme a moeda de origem escolhida
- Consulta da cotação em tempo real via API
- Cálculo e exibição do valor convertido na própria janela
- Aceita valores com vírgula ou ponto como separador decimal (por exemplo, 10,50 ou 10.50)
- Lista de consulta com os códigos e nomes das moedas disponíveis
- Moedas e pares de conversão configuráveis por arquivos XML

## Tecnologias utilizadas

- Python 3
- CustomTkinter, para a interface gráfica
- Requests, para as chamadas HTTP
- xmltodict, para a leitura dos arquivos XML
- AwesomeAPI, como fonte das cotações

## Estrutura do projeto

```
projeto/
    main.py              Interface gráfica e lógica de conversão
    pegar_moedas.py      Leitura dos arquivos XML de moedas e conversões
    pegar_cotacao.py     Consulta da cotação na API
    moedas.xml           Códigos e nomes das moedas disponíveis
    conversoes.xml       Pares de conversão permitidos (ex.: USD-BRL)
```

## Como funciona

1. Ao iniciar, o programa lê o arquivo `conversoes.xml` e monta um dicionário que relaciona cada moeda de origem às moedas de destino possíveis.
2. O arquivo `moedas.xml` fornece os nomes das moedas, exibidos na lista da parte inferior da janela.
3. Ao escolher a moeda de origem, o menu de destino é atualizado com as opções disponíveis.
4. Ao clicar em "Converter", o programa busca a cotação de compra (`bid`) na AwesomeAPI e multiplica pelo valor digitado.
5. O resultado é exibido na janela no formato `10.00 USD = 55.30 BRL`.

## Pré-requisitos

- Python 3.10 ou superior
- Conexão com a internet para consultar as cotações

## Instalação

1. Clone o repositório:

```
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Instale as dependências:

```
python -m pip install customtkinter requests xmltodict
```

## Como executar

Dentro da pasta do projeto, execute:

```
python main.py
```

## Como usar

1. Selecione a moeda de origem no primeiro menu.
2. Selecione a moeda de destino no segundo menu.
3. Digite o valor a ser convertido no campo de valor.
4. Clique em "Converter" para ver o resultado.

Observação: a lista de moedas de destino só é carregada depois que uma moeda de origem é selecionada no menu. Se o botão for pressionado antes disso, a aplicação pede que a moeda de origem seja escolhida.

## Personalização

Para incluir novas moedas ou novos pares de conversão, basta editar os arquivos XML:

- `moedas.xml`: adicione o código e o nome da moeda
- `conversoes.xml`: adicione o par no formato `ORIGEM-DESTINO`, desde que ele seja suportado pela AwesomeAPI

## Possíveis melhorias

- Tratamento de erros para campo de valor vazio ou com caracteres inválidos
- Tratamento de falhas de conexão com a API
- Inversão rápida entre moeda de origem e destino
- Histórico das últimas conversões

## Autor

Olliver

Projeto desenvolvido para fins de estudo e portfólio.
