# Projeto Piloto Teste GFT
 Repositório de Teste para Desafio GFT
# Fluxo de Caixa 

 O projeto “Fluxo de Caixa” é um aplicativo de desktop simples, desenvolvido em Python, que permite aos usuários gerenciarem seu fluxo de caixa. Com uma interface amigável criada usando a biblioteca Tkinter, os usuários podem facilmente inserir suas receitas e despesas. O aplicativo então calcula o saldo atual, o total de receitas e o total de despesas, fornecendo uma visão clara da situação financeira do usuário. Este projeto é uma excelente ferramenta para quem busca uma maneira simples e eficaz de acompanhar suas finanças pessoais ou de negócios. Além disso, o código segue boas práticas de programação orientada a objetos, como encapsulamento e modularização, tornando-o um ótimo exemplo para aqueles que estão aprendendo a programar em Python. 

## Descrição 

  

Este é um aplicativo de desktop simples para gerenciar o fluxo de caixa. Ele permite que os usuários insiram receitas e despesas e calcula o saldo atual, o total de receitas e o total de despesas. 

  

## Instalação 

  

Para instalar o aplicativo, siga estas etapas: 

  

1. Clone o repositório: `git clone https://github.com/wladbi/fluxo-de-caixa.git` 

2. Navegue até o diretório do projeto: `cd Projeto-Piloto-Teste-GFT/` 

3. Instale as dependências: `pip install -r requirements.txt` 

  

## Uso 

Versão Python 3.12
Versão Pycharm 2023.2

Para iniciar o aplicativo, execute o seguinte comando no diretório do projeto: 

python3 https://github.com/wladbi/Projeto-Piloto-Teste-GFT/blob/main/projetopilotodesafioGFT.py

## Testes 

  

Aqui estão algumas sugestões de testes que você pode realizar para avaliar o programa: 

  

1. **Teste de interface do usuário**: Verifique se todos os campos e botões estão sendo exibidos corretamente na interface do usuário. 

2. **Teste de funcionalidade**: Insira valores nas entradas de receita e despesa e clique no botão 'Adicionar'. Verifique se o saldo, o total de receitas e o total de despesas estão sendo calculados e exibidos corretamente. 

3. **Teste de validação de entrada**: Tente inserir valores não numéricos ou deixar os campos em branco e clique no botão 'Adicionar'. O programa deve ser capaz de lidar com esses casos. 

4. **Teste de desempenho**: Insira valores nas entradas de receita e despesa repetidamente e verifique se o programa continua respondendo e calculando os valores corretamente. 

  

## Requisitos Não Funcionais 

  

1. **Disponibilidade do serviço de controle de lançamento**: Para garantir que o serviço de controle de lançamento não fique indisponível se o sistema de consolidação diária cair, você pode considerar a implementação de um mecanismo de tolerância a falhas. Isso pode ser feito através da separação dos dois serviços em diferentes processos ou, idealmente, em diferentes servidores. Dessa forma, se o sistema de consolidação diária falhar, ele não afetará o serviço de controle de lançamento. 

  

2. **Gerenciamento de carga de pico**: Para lidar com dias de pico onde o serviço de consolidação diária recebe 500 requisições por segundo, você pode considerar a implementação de um balanceador de carga. Um balanceador de carga distribuirá efetivamente as requisições entre vários servidores para evitar sobrecarregar um único servidor. Além disso, você pode considerar a implementação de escalabilidade automática, onde novos servidores são adicionados conforme a demanda aumenta. 

  

3. **Gerenciamento de perda de requisições**: Para garantir que no máximo 5% das requisições sejam perdidas durante picos de carga, você pode considerar a implementação de filas de mensagens. As filas de mensagens podem ajudar a lidar com picos de carga, armazenando temporariamente requisições durante períodos de alta demanda e processando-as em um ritmo que seus servidores possam lidar. 

** Para o ambiente especificado como requisitos não funcionais recomenda-se o use de uma arquitetura estabelecida em arquitetura Cloud. Pois fica mais integro a estruturação de ambiente de Loadbalance e Fail Safe. 

  

## Arquitetura 

  

O código Python 3.12 é um aplicativo de desktop simples criado usando o Tkinter, que é uma biblioteca padrão do Python para a criação de interfaces gráficas do usuário (GUI). Não parece estar explicitamente baseado em um framework de arquitetura de software específico como SOLID, CLEAN ou Hexagonal. Pois é um projeto muito simples para ser encaixado em um desses paradigmas. 

  

No entanto, o código segue algumas boas práticas de programação orientada a objetos (OOP), como encapsulamento e modularização. A classe `FluxoCaixa` encapsula os dados e métodos relacionados ao fluxo de caixa, e o código está organizado em métodos distintos para configurar a janela, criar campos de entrada e calcular o fluxo de caixa. 

## Contribuição 

  

Contribuições são bem-vindas! Por favor, leia as diretrizes de contribuição antes de enviar uma solicitação pull. 

  

## Licença 

  

Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para obter mais detalhes. 

 
