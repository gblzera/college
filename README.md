
# Guia Completo: Concorrência e Manipulação de Exceções

Este material contém explicações, exemplos de código e perguntas frequentes para ajudar você a dominar os conceitos de concorrência, exceções e sua combinação, especialmente para uso em sala de aula.

---

## 🧵 1. Concorrência

### O que é Concorrência?

Concorrência é a capacidade de lidar com várias tarefas que estão em andamento, alternando entre elas para simular que acontecem ao mesmo tempo.  
Exemplo real: sozinho você faz café e frita ovo um após o outro (concorrência). Com um ajudante, faz os dois ao mesmo tempo (paralelismo).

### Relação com Paradigmas de Linguagens de Programação (PLP)

- No paradigma imperativo, controlamos o estado e o fluxo das tarefas diretamente.
- Concorrência exige cuidado com recursos compartilhados e sincronização para evitar erros.
- No paradigma funcional, a imutabilidade torna a concorrência mais segura e fácil de gerenciar.

### Código Exemplo

```python
import threading

def tarefa(nome):
    print(f"Executando {nome}")

threads = []
for i in range(3):
    t = threading.Thread(target=tarefa, args=(f'Tarefa {i}',))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### Explicação do Código

- Criamos 3 threads que executam a função `tarefa` simultaneamente.
- Cada thread imprime seu nome.
- O método `join()` é usado para aguardar o término de todas as threads.
- Isso demonstra a execução concorrente de múltiplas tarefas.

### Perguntas e Respostas

<details>
<summary>Qual a diferença entre concorrência e paralelismo?</summary>

Concorrência é alternar rapidamente entre tarefas para que pareçam simultâneas, enquanto paralelismo é executar múltiplas tarefas ao mesmo tempo em núcleos diferentes do processador.
</details>

<details>
<summary>Por que concorrência pode causar erros?</summary>

Porque múltiplas threads podem acessar e modificar dados compartilhados simultaneamente, causando condições de corrida e inconsistências.
</details>

---

## ⚠️ 2. Manipulação de Exceções

### O que são Exceções?

Exceções são eventos que interrompem o fluxo normal do programa, indicando erros ou condições inesperadas que precisam ser tratadas.

### Relação com Paradigmas de Linguagens de Programação (PLP)

- No paradigma imperativo, usamos blocos `try/except` para capturar e tratar erros.
- No paradigma funcional, funções puras não têm efeitos colaterais nem saltos inesperados, por isso exceções não são comuns. Usa-se tipos como `Maybe` ou `Either` para tratar falhas de forma explícita.

### Código Exemplo

```python
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: divisão por zero não é permitida."

print(dividir(10, 2))
print(dividir(10, 0))
```

### Explicação do Código

- A função `dividir` tenta realizar a divisão.
- Se o divisor for zero, uma exceção `ZeroDivisionError` é capturada.
- Uma mensagem amigável é retornada, evitando que o programa trave.

### Perguntas e Respostas

<details>
<summary>Por que usamos try/except?</summary>

Para tratar erros de forma controlada, evitando que o programa seja interrompido abruptamente e possibilitando uma resposta amigável ao usuário.
</details>

<details>
<summary>Por que exceções não são comuns em linguagens funcionais?</summary>

Porque funções puras devem ser previsíveis e não ter efeitos colaterais ou saltos inesperados. Em vez disso, falhas são tratadas explicitamente usando tipos que indicam sucesso ou falha (ex: `Maybe` ou `Either`).
</details>

---

## 🔄 3. Concorrência + Manipulação de Exceções

### O que acontece quando combinamos concorrência e exceções?

- Cada thread ou processo deve tratar suas próprias exceções para evitar que uma falha derrube o sistema inteiro.
- Em paradigmas imperativos, usamos `try/except` em cada thread.
- Em paradigmas funcionais concorrentes, processos são isolados e supervisionados, aplicando a filosofia "Let it crash".

### Relação com Paradigmas de Linguagens de Programação (PLP)

- No imperativo concorrente, falhas em threads são tratadas localmente.
- No funcional concorrente, falhas isoladas não afetam o sistema; supervisores reiniciam processos falhos.

### Código Exemplo

```python
import threading

def ler_arquivo(nome):
    try:
        with open(nome, 'r') as f:
            print(f"[{threading.current_thread().name}] Lendo arquivo {nome}")
            conteudo = f.read()
            print(conteudo)
    except FileNotFoundError:
        print(f"[{threading.current_thread().name}] Arquivo não encontrado: {nome}")

nomes_arquivos = ["dados1.txt", "dados2.txt", "inexistente.txt"]

threads = []
for nome in nomes_arquivos:
    t = threading.Thread(target=ler_arquivo, args=(nome,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
```

### Explicação do Código

- Três arquivos são lidos em threads concorrentes.
- Se um arquivo não existir, a exceção `FileNotFoundError` é capturada localmente na thread.
- O programa continua executando normalmente para os outros arquivos.

### Perguntas e Respostas

<details>
<summary>O que acontece se uma thread falhar ao ler um arquivo?</summary>

Ela trata o erro internamente com `try/except`, impedindo que a falha afete as outras threads.
</details>

<details>
<summary>Como linguagens funcionais tratam falhas concorrentes?</summary>

Usam processos isolados e supervisores que monitoram e reiniciam processos falhos automaticamente, seguindo a filosofia 'Let it crash'. Isso aumenta a resiliência do sistema.
</details>

---

# Conclusão

Este guia ajuda a entender os conceitos fundamentais de concorrência e manipulação de exceções, tanto em paradigmas imperativos quanto funcionais, e a aplicar esses conhecimentos na prática e na sala de aula.

---

# Referências

- [Documentação Python - threading](https://docs.python.org/3/library/threading.html)  
- [Python Exceptions](https://docs.python.org/3/tutorial/errors.html)  
- [Elixir Supervision Trees](https://hexdocs.pm/elixir/supervisor.html)  
- [Paradigma Funcional](https://en.wikipedia.org/wiki/Functional_programming)  
- [Concorrência vs Paralelismo](https://en.wikipedia.org/wiki/Concurrency_(computer_science))  
