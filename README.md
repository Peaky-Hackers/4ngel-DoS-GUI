# 4ngel-DoS-GUI (BETA)

Uma versão com interface gráfica (GUI) do simulador de ataques HTTP, permitindo testes de carga de forma visual e intuitiva. Ideal para simulações de ataques DoS em ambientes controlados com maior facilidade de configuração.

## Introdução

**4ngel-DoS-GUI** oferece uma interface moderna para a realização de ataques DoS utilizando solicitações HTTP GET e POST em múltiplas threads. Com um design visual aprimorado, é fácil configurar e monitorar o comportamento de servidores sob teste, tornando o processo de simulação mais acessível.

## Funcionalidades
- Interface gráfica intuitiva.
- Configuração de múltiplas threads e número de requisições.
- Suporte a solicitações HTTP GET e POST.
- Agentes de usuário aleatórios para cada requisição.
- Feedback em tempo real das requisições enviadas.
- Desativação de avisos SSL inseguros.

## Como Usar

### Pré-requisitos:
- Python 3.6 ou superior.
- Instale as dependências com o comando:
```
pip install -r requirements.txt
```

### Execução:

1. Clone este repositório:
```
git clone https://github.com/Peaky-Hackers/4ngel-DoS-GUI.git
cd 4ngel-DoS-GUI
```

2. Execute o script com GUI:
```
python main_gui.py
```

3. Siga as instruções na interface gráfica:
- Insira a URL alvo.
- Defina o número de solicitações por thread.
- Escolha o número de threads.
- Selecione o método HTTP (GET ou POST).

## Links para os Repositórios

- Acesse a [versão sem interface gráfica](https://github.com/Peaky-Hackers/4ngel-DoS).

## Atenção

⚠️ Esta ferramenta deve ser usada apenas para testes éticos e em ambientes controlados, com permissão explícita. O uso inadequado pode ser ilegal. O autor não se responsabiliza por qualquer uso indevido.

## Contribuições
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou pull requests.
