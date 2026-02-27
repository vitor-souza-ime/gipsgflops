# GIPS-GFLOPS

Projeto para análise experimental de desempenho computacional utilizando métricas de **GIPS (Giga Instructions Per Second)** e **GFLOPS (Giga Floating Point Operations Per Second)**.

## 📌 Objetivo

Este repositório tem como objetivo implementar e avaliar benchmarks de desempenho computacional em diferentes arquiteturas, medindo:

- Taxa de execução de instruções (GIPS)
- Desempenho em operações de ponto flutuante (GFLOPS)
- Eficiência de CPU em tarefas intensivas
- Escalabilidade com múltiplos núcleos

O projeto é voltado para estudos em:

- Arquiteturas de alto desempenho
- Sistemas multi-core
- Análise de performance computacional
- Engenharia de desempenho

---

## 🧠 Fundamentação Teórica

As métricas utilizadas são amplamente adotadas em avaliação de sistemas computacionais:

- **GIPS**: mede quantas bilhões de instruções são executadas por segundo.
- **GFLOPS**: mede quantas bilhões de operações de ponto flutuante são realizadas por segundo.

GFLOPS é particularmente relevante em:

- Computação científica
- Simulações numéricas
- Redes neurais
- Processamento vetorial

---

## 🏗 Estrutura do Projeto

```

gipsgflops/
│
├── src/                # Código-fonte dos benchmarks
├── results/            # Resultados experimentais
├── scripts/            # Scripts auxiliares
├── docs/               # Documentação complementar
└── README.md

````

---

## 🚀 Como Executar

### 1️⃣ Clonar o repositório

```bash
git clone https://github.com/vitor-souza-ime/gipsgflops.git
cd gipsgflops
````

### 2️⃣ Executar benchmark

Exemplo genérico:

```bash
python benchmark.py
```

ou

```bash
gcc benchmark.c -O3 -o benchmark
./benchmark
```

---

## 📊 Metodologia Experimental

Os testes seguem as seguintes diretrizes:

* Compilação com otimização (`-O3`)
* Execução múltipla para média estatística
* Controle de interferências externas
* Medição de tempo com alta precisão

A métrica GFLOPS é calculada por:

[
GFLOPS = \frac{\text{Número total de operações}}{\text{Tempo de execução (s)} \times 10^9}
]

---

## 🖥 Requisitos

* Python 3.x (se aplicável)
* GCC ou Clang (para versões em C/C++)
* Sistema Linux recomendado
* CPU multi-core para testes paralelos

---

## 📈 Possíveis Extensões

* Paralelização com OpenMP
* Uso de bibliotecas BLAS
* Comparação entre CPU e GPU
* Análise de consumo energético
* Execução em arquiteturas NUMA

---

## 🎓 Aplicações Acadêmicas

Este projeto pode ser utilizado em disciplinas como:

* Arquitetura de Computadores
* Sistemas de Alto Desempenho
* Computação Paralela
* Engenharia de Software Experimental

---

## 👨‍🏫 Autor

Prof. Vitor Amadeu

---

## 📜 Licença

Este projeto está sob a licença MIT.

