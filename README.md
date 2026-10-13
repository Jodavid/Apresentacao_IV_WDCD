# IA, Inovação e Transformação da Ciência: Uma Perspectiva Estatística

> **Apresentação em Quarto Reveal.js para a Mesa-redonda do IV Workshop de Divulgação Científica e Didáticas (IV WDCD)**  
> **Data:** 15 de outubro de 2026 · **Local:** Auditório do CCEN · Universidade Federal de Pernambuco (UFPE)  
> **Palestrante:** [Prof. Dr. Jodavid Ferreira](http://jodavid.github.io) (Departamento de Estatística · CCEN/UFPE)  
> **Contato:** `jodavid.ferreira@ufpe.br`

---

## 📌 Sobre o Projeto

Este repositório contém o código-fonte, scripts de geração de figuras, estilos personalizados e a versão compilada da apresentação **"Inteligência Artificial, Inovação e Transformação da Ciência: Uma perspectiva estatística: fundamentos, incerteza e soberania"**.

A apresentação foi desenvolvida utilizando **[Quarto](https://quarto.org/)** com o framework **[Reveal.js](https://revealjs.com/)**, configurada para gerar um arquivo HTML **100% autocontido** (`embed-resources: true`), incluindo tipografia embutida em base64 e ilustrações vetoriais SVG. Isso garante portabilidade total para exibição offline sem dependências de conexão ou servidores externos.

---

## 🎯 Fio Condutor e Conteúdo

> *"A Inteligência Artificial pode acelerar a velocidade das nossas respostas. Mas é a Estatística que garante a solidez das nossas perguntas e a calibração das nossas incertezas."*

### Principais Tópicos Abordados

1. **O Cenário da IA na Ciência e o Paradoxo Brasileiro:**
   - Aumento da produção com IA vs. crise de replicabilidade (< 20% no *ReplicationBench*).
   - O paradoxo nacional: Top 15 mundial em publicações sobre IA, mas 53º colocado no Índice Global de Inovação (OMPI).
   - Soberania tecnológica, o papel dos SLMs e a lição dos medicamentos genéricos aplicada a dados locais (SUS, agro, clima e energia).

2. **Fundamentos Estatísticos e Limites da IA:**
   - **Inferência Indutiva:** A IA acelerou a otimização computacional, mas a Estatística decide o mecanismo gerador, desenho amostral, validação e decisão.
   - **Qualidade vs. Quantidade:** Porque mais dados não corrigem dados com viés amostral (Equação de Meng / Bradley et al., *Nature*).
   - **Regime Moderno de Aprendizado:** O fenômeno da *Dupla Descida* (*Double Descent*) em modelos sobreparametrizados ($p \gg n$).
   - **Calibração e Confiança:** Fluência verbal em LLMs não é calibração probabilística (redes profundas sobreconfiantes).
   - **Predição Conforme (*Conformal Prediction*):** Garantia de cobertura marginal em amostra finita vs. desigualdade de cobertura em subgrupos.
   - **Predição vs. Causalidade:** A Escada de Pearl e os riscos de confundir associação com intervenção no uso de IA para políticas públicas e saúde.

3. **Boas Práticas e Integridade Científica:**
   - Erros silenciosos: vazamento de dados (*data leakage*), dependência ignorada e sobreajuste por caminhos que se bifurcam (*garden of forking paths*).
   - Quatro perguntas de auditoria antes de confiar em um modelo preditivo.
   - Volume de artigos vs. profundidade e reprodutibilidade (ex.: submissões na AAAI-26 e uso de IA na revisão por pares).

4. **Implicações Pedagógicas e Éticas no Ensino Superior:**
   - Adaptação docente: transição da avaliação de respostas mecânicas para a avaliação do percurso, defesa de hipóteses e capacidade de questionar a IA com evidências.
   - Matriz de governança por risco (risco baixo, moderado e alto) alinhada às diretrizes internacionais (AI Act da UE) e ao PL 2.338/2023.

---

## 📂 Estrutura de Arquivos

```text
.
├── apresentacao_ia_estatistica.qmd   # Código-fonte principal da apresentação em Quarto Reveal.js
├── apresentacao_ia_estatistica.html  # Apresentação final renderizada (autocontida, pronta para exibição)
├── figs.py                           # Script Python para simulação e geração das figuras vetoriais
├── fig/                              # Figuras e diagramas vetoriais (SVG)
│   ├── paradoxo.svg                  # Gráfico: Top 15 produção científica vs 53º no GII
│   ├── dupla_descida.svg             # Simulação estatística do fenômeno da dupla descida
│   ├── calibracao.svg                # Curva de calibração vs sobreconfiança do modelo
│   └── conforme.svg                  # Intervalo conforme e cobertura por subgrupo
├── fonts/                            # Arquivos locais de fontes em formato WOFF2
│   ├── ibm-plex-sans-*.woff2         # Família tipográfica IBM Plex Sans (texto)
│   └── source-serif-4-*.woff2        # Família tipográfica Source Serif 4 (títulos)
├── tema.scss                         # Estilo SCSS da apresentação (referencia fontes locais)
├── tema_embed.scss                   # Estilo SCSS com fontes embutidas em Data URI base64
├── LEIA-ME.txt                       # Instruções rápidas de uso e teclas de atalho
└── README.md                         # Documentação completa do projeto
```

---

## ⌨️ Dicas para o Apresentador (Atalhos do Reveal.js)

Ao abrir os slides no navegador, utilize as seguintes teclas de atalho:

| Tecla | Função |
| :---: | :--- |
| **`S`** | **Modo do Apresentador** (*Speaker View* com notas, cronômetro e prévia do próximo slide) |
| **`F`** | Alternar modo de **Tela Cheia** (*Full Screen*) |
| **`O`** ou **`Esc`** | Alternar **Modo Visão Geral** (*Overview* de todos os slides) |
| **`B`** ou **`.`** | Pausar / Escurecer a tela (*Black screen*) para direcionar a atenção ao orador |
| **`Espaço`** / **`→`** | Avançar slide ou fragmento interativo |
| **`←`** | Voltar slide ou fragmento interativo |
| **`?`** | Exibir ajuda com a lista completa de atalhos de navegação |

> **Nota para a fala:** Alguns slides contêm animações/revelações por fragmento (indicados com `[clique]` nas notas do orador).


---

## 📜 Nota de Transparência

Em consonância com o debate proposto na apresentação sobre integridade e uso crítico de tecnologia, estes slides contaram com auxílio de Inteligência Artificial (**Claude Opus 5.5**, Anthropic). A curadoria, o rigor teórico e a responsabilidade autoral são integralmente do autor.

---

## 👨‍🏫 Autor

**Prof. Dr. Jodavid Ferreira**  
Departamento de Estatística — CCEN  
Universidade Federal de Pernambuco (UFPE)  
- **Site:** [jodavid.github.io](http://jodavid.github.io)  
- **E-mail:** `jodavid.ferreira@ufpe.br`
