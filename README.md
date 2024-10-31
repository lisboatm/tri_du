# Problema: Tri-du

No jogo de cartas Tri-du, o objetivo é formar uma dupla ou um trio de cartas do mesmo valor. Dadas duas cartas iniciais, o programa deve determinar qual valor para a terceira carta maximiza a probabilidade de vitória do jogador.

## Regras do Jogo

1. Um trio (três cartas do mesmo valor) é mais forte do que uma dupla.
2. Se houver dois trios, vence o de maior valor.
3. Se houver duas duplas, vence a de maior valor.

Neste problema, o jogador já recebeu duas cartas de valores conhecidos, e precisamos escolher um valor para a terceira carta que aumente suas chances de vencer.

## Entrada

- Uma linha contendo dois inteiros, `A` e `B` (1 ≤ A, B ≤ 13), que representam os valores das duas primeiras cartas recebidas.

## Saída

- Um único inteiro, representando o valor da terceira carta que maximiza as chances de o jogador ganhar a partida.

## Exemplos

### Exemplo 1

**Entrada**
```
10 7
```

**Saída**
```
10
```

**Explicação**: Para maximizar a probabilidade de ganhar, o jogador deve escolher a terceira carta como 10, formando uma dupla de maior valor.

### Exemplo 2

**Entrada**
```
2 2
```

**Saída**
```
2
```

**Explicação**: As duas cartas já formam uma dupla de valor 2. Escolhendo a terceira carta como 2, o jogador forma um trio, o que maximiza a chance de vitória.

## Estratégia de Solução

1. Se as duas cartas já têm o mesmo valor (`A == B`), a melhor opção é que a terceira carta também tenha esse valor, formando um trio.
2. Se as cartas têm valores diferentes (`A != B`), a melhor escolha é o valor mais alto entre `A` e `B`, formando a dupla mais forte possível.

## Pseudocódigo

```python
a, b = map(int, input().split())

if a == b:
    print(a)  # Ambas as cartas são iguais, formando um trio
else:
    print(max(a, b))  # Se diferentes, escolher a carta de maior valor
```

## Complexidade

- A solução é **O(1)**, pois a operação consiste em comparações e escolha de um valor entre dois números.

## Considerações

Este programa utiliza uma abordagem simples para determinar a carta ideal no jogo Tri-du, maximizando as chances de vitória ao formar o conjunto mais forte de cartas, conforme as regras estabelecidas.
