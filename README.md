# Algoritmos em Python 🐍

Coleção de algoritmos para quem está começando em Python, do mais simples ao mais elaborado. Cada algoritmo traz o código, a explicação, como executar e exercícios.

> **Algoritmo** é uma sequência finita de passos para resolver um problema.

---

## 📚 Índice

| # | Algoritmo | Arquivo | Assunto |
|---|-----------|---------|---------|
| 1 | [Alô Mundo!](#algoritmo-1--alô-mundo) | `alg1.py` | Comentários e `print()` |
| 2 | [Somando com o Python](#algoritmo-2--somando-com-o-python) | `alg2.py` | Soma e expressões |
| 3 | [Dividindo com o Python](#algoritmo-3--dividindo-com-o-python) | `alg3.py` | Divisão e números decimais |

---

## ▶️ Como executar qualquer algoritmo

**Pré-requisito:** Python 3 instalado.

```bash
python --version
```

Dentro da pasta do arquivo, execute:

```bash
python nome_do_arquivo.py
```

Se `python` não funcionar, tente `python3` (Linux/macOS) ou `py` (Windows).

---

## Algoritmo 1 — Alô Mundo!

Exibe a mensagem **"Alô Mundo!"** no console.

### 🎯 Objetivo

- Entender o que é um algoritmo.
- Conhecer os tipos de comentário em Python.
- Saber a diferença entre um arquivo `.py` e um notebook `.ipynb`.
- Executar o primeiro programa com `print()`.

### 📄 Código

Arquivo: `alg1.py`

```python
# algoritmo é uma sequência de passos
'''
   comentário de múltiplas linhas
'''
"""
  comentário de múltiplas linhas
  nomearquivo.py (arquivo python)
  notebook.ipynb (arquivo de data science)
"""
print("Alô Mundo!")
```

### 🔍 Explicação linha a linha

| Trecho | O que faz |
|--------|-----------|
| `# algoritmo é ...` | Comentário de **uma linha**. Começa com `#` e o Python o ignora. |
| `'''  ...  '''` | Texto entre aspas triplas simples. Usado como comentário de **várias linhas**. |
| `"""  ...  """` | Texto entre aspas triplas duplas. Mesmo uso; também é a forma padrão de escrever *docstrings*. |
| `print("Alô Mundo!")` | Função que **escreve** o texto entre parênteses na tela. |

**Tipos de arquivo citados**

| Extensão | Descrição |
|----------|-----------|
| `.py` | Arquivo Python comum, executado por inteiro no terminal. |
| `.ipynb` | Notebook (Jupyter), muito usado em ciência de dados, executado por células. |

### ✅ Saída esperada

```
Alô Mundo!
```

### 🧪 Experimente

1. Troque o texto pelo seu nome.
2. Adicione um segundo `print()` com outra mensagem.
3. Crie um comentário de uma linha explicando o que cada `print()` faz.

---

## Algoritmo 2 — Somando com o Python

Calcula `1 + 1` e exibe o resultado no console.

### 🎯 Objetivo

- Usar o Python como uma calculadora.
- Entender que o `print()` pode exibir o **resultado de uma expressão**, não só textos.
- Conhecer o operador de soma `+`.

### 📄 Código

Arquivo: `alg2.py`

```python
print(1+1)
```

### 🔍 Explicação linha a linha

| Trecho | O que faz |
|--------|-----------|
| `1+1` | **Expressão** aritmética. O Python calcula a soma e obtém `2`. |
| `print( ... )` | Escreve na tela o valor que está entre parênteses. |

**Por que não há aspas?**

| Código | Saída | Motivo |
|--------|-------|--------|
| `print(1+1)` | `2` | Sem aspas, o Python **calcula** a expressão. |
| `print("1+1")` | `1+1` | Com aspas, é um **texto** e é exibido do jeito que foi escrito. |

**Operadores aritméticos básicos**

| Operador | Operação | Exemplo | Resultado |
|----------|----------|---------|-----------|
| `+` | Soma | `print(5+3)` | `8` |
| `-` | Subtração | `print(5-3)` | `2` |
| `*` | Multiplicação | `print(5*3)` | `15` |
| `/` | Divisão | `print(6/3)` | `2.0` |

### ✅ Saída esperada

```
2
```

### 🧪 Experimente

1. Troque `1+1` por `10-4`.
2. Calcule `7*8`.
3. Compare `print(1+1)` com `print("1+1")` e explique a diferença.

---

## Algoritmo 3 — Dividindo com o Python

Calcula `3 / 2` e exibe o resultado no console.

### 🎯 Objetivo

- Conhecer o operador de divisão `/`.
- Perceber que a divisão em Python **sempre resulta em número decimal** (`float`).
- Conhecer a divisão inteira `//` e o resto `%`.

### 📄 Código

Arquivo: `alg3.py`

```python
print(3/2)
```

### 🔍 Explicação linha a linha

| Trecho | O que faz |
|--------|-----------|
| `3/2` | Divide 3 por 2. O resultado é `1.5`. |
| `print( ... )` | Escreve na tela o valor calculado. |

**Atenção:** o Python usa **ponto** como separador decimal (`1.5`), e não vírgula.

**Os três operadores da divisão**

| Operador | Operação | Exemplo | Resultado |
|----------|----------|---------|-----------|
| `/` | Divisão (decimal) | `print(3/2)` | `1.5` |
| `//` | Divisão inteira (descarta a parte decimal) | `print(3//2)` | `1` |
| `%` | Resto da divisão | `print(3%2)` | `1` |

**A divisão sempre devolve decimal**

| Código | Saída |
|--------|-------|
| `print(6/3)` | `2.0` |
| `print(6//3)` | `2` |

### ✅ Saída esperada

```
1.5
```

### 🧪 Experimente

1. Troque `3/2` por `10/4`.
2. Calcule `10//4` e `10%4` e explique por que `4 * 2 + 2 = 10`.
3. Descubra o que acontece com `print(5/0)` e leia a mensagem de erro.

---

## 👨‍🏫 Autor

**Prof. Rômulo**
