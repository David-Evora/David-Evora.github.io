---
name: David Évora, portfólio
description: Site de uma página, bilíngue e em dois temas, em cinza frio com cobalto, onde o trabalho lidera e a interface recua.
colors:
  paper: "#eef0f3"
  surface: "#e2e5ea"
  ink: "#0b0c0e"
  muted: "#5d6470"
  cobalt: "#1f2de6"
  on-cobalt: "#ffffff"
  night: "#0d0e10"
  night-surface: "#181a1d"
  night-ink: "#eef0f3"
  night-muted: "#9ea3ad"
  periwinkle: "#8d98ff"
  on-periwinkle: "#0b0c0e"
  inverse-surface: "#17181a"
  inverse-muted: "#8e8f92"
typography:
  display:
    fontFamily: "Hanken Grotesk, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(38px, 3.24vw + 25.4px, 72px)"
    fontWeight: 400
    lineHeight: 1.04
    letterSpacing: "-0.038em"
  headline:
    fontFamily: "Hanken Grotesk, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "clamp(30px, 1.72vw + 23.3px, 48px)"
    fontWeight: 400
    lineHeight: 1.1
    letterSpacing: "-0.03em"
  title:
    fontFamily: "Hanken Grotesk, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "28px"
    fontWeight: 400
    lineHeight: 1.2
    letterSpacing: "-0.03em"
  card-title:
    fontFamily: "Hanken Grotesk, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "20px"
    fontWeight: 500
    lineHeight: 1.3
    letterSpacing: "-0.01em"
  body:
    fontFamily: "Hanken Grotesk, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "16px"
    fontWeight: 400
    lineHeight: 1.55
  small:
    fontFamily: "Hanken Grotesk, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "14px"
    fontWeight: 400
    lineHeight: 1.5
  label:
    fontFamily: "Hanken Grotesk, system-ui, -apple-system, Segoe UI, sans-serif"
    fontSize: "13px"
    fontWeight: 500
    lineHeight: 1.4
    letterSpacing: "0.01em"
rounded:
  sm: "8px"
  md: "12px"
  lg: "20px"
  pill: "99px"
spacing:
  s-1: "4px"
  s-2: "8px"
  s-3: "12px"
  s-4: "16px"
  s-5: "24px"
  s-6: "32px"
  s-7: "48px"
  s-8: "64px"
  s-9: "96px"
components:
  button-primary:
    backgroundColor: "{colors.cobalt}"
    textColor: "{colors.on-cobalt}"
    typography: "{typography.body}"
    rounded: "{rounded.sm}"
    padding: "0 24px"
    height: "44px"
  button-primary-dark:
    backgroundColor: "{colors.periwinkle}"
    textColor: "{colors.on-periwinkle}"
    rounded: "{rounded.sm}"
  button-secondary-tonal:
    backgroundColor: "{colors.surface}"
    textColor: "{colors.ink}"
    rounded: "{rounded.sm}"
    padding: "0 24px"
    height: "44px"
  tool-button:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.ink}"
    rounded: "{rounded.md}"
    height: "44px"
    width: "44px"
  copy-button:
    textColor: "{colors.ink}"
    typography: "{typography.label}"
    rounded: "{rounded.sm}"
    padding: "0 12px"
    height: "32px"
  shot-frame:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.lg}"
  bar-track:
    backgroundColor: "{colors.surface}"
    rounded: "{rounded.pill}"
    height: "14px"
---

# Design System: David Évora, portfólio

## Overview

**Creative North Star: "A Bancada de Evidências"**

O site é uma bancada onde o trabalho está exposto e a interface some do caminho: capturas, gráficos e fotos reais ocupam o palco, e o resto é papel cinza frio, tinta quase preta e um único cobalto para o que se pode clicar. É o modo Experience de um portfólio: o trabalho lidera, a interface recua. A voz é sóbria e técnica, sem ornamento que não carregue informação.

A densidade é baixa e o ritmo é de capítulos: cada seção ocupa uma ou duas telas, com um único `h2`. O sistema vem do kit taste-skill (grade, escala de espaço, escala de tipo, raios) e a página só define paleta, fonte e poucas sobreposições. Há dois temas desenhados à parte, não derivados por inversão: o claro (papel `#eef0f3`) e o escuro (`#0d0e10`), com o cobalto trocado por um lavanda-azulado claro para manter contraste. O idioma (PT padrão, EN completo) troca o texto inteiro, nunca mistura os dois na mesma tela.

**Key Characteristics:**
- Cinza frio com um só acento: cobalto no claro, lavanda-azulado no escuro.
- Uma família, Hanken Grotesk, em pesos 400 (títulos) e 500 (rótulos, cartões, botões), com tracking negativo nos títulos.
- Plano por padrão: profundidade por tom e filete de 1px, quase sem sombra.
- Dois momentos de movimento: capítulos fixos do fluxo do InfoFrota e a foto que se revela nas conquistas (só desktop).
- Alvos de toque de 44px, foco visível, `prefers-reduced-motion` respeitado.

## Colors

Paleta cool-grey-cobalt: um papel cinza azulado, tinta quase preta, e um acento cobalto usado só em ação, link e dado em destaque.

### Primary
- **Cobalto de Ação** (#1f2de6): botão primário, links sublinhados, estado "copiado", barra do melhor resultado, destaque de seleção. Contraste 7,14:1 sobre o papel e 8,15:1 com texto branco (#ffffff).
- **Lavanda de Ação, tema escuro** (#8d98ff): substitui o cobalto no escuro; texto sobre ele é a tinta `#0b0c0e`. Contraste 7,42:1 sobre `#0d0e10`.

### Neutral
- **Papel Frio** (#eef0f3): fundo do tema claro e tinta do tema escuro.
- **Chapa Cinza** (#e2e5ea): superfícies, trilhos de barras, molduras de imagem, fundo do botão tonal.
- **Tinta de Grafite** (#0b0c0e): texto no claro; contraste 17,14:1 sobre o papel.
- **Névoa de Apoio** (#5d6470): texto secundário no claro; 5,22:1 sobre o papel.
- **Noite** (#0d0e10) e **Noite Elevada** (#181a1d): fundo e superfície do tema escuro.
- **Névoa Noturna** (#9ea3ad): texto secundário no escuro; 7,63:1 sobre a noite.
- **Faixa Inversa** (#17181a, apoio #8e8f92): superfície e texto de apoio das faixas invertidas do claro.

### Named Rules
**A Regra do Único Acento.** O cobalto (ou a lavanda no escuro) marca o que é clicável ou o melhor dado; texto corrido, títulos e molduras ficam em tinta e cinza.
**A Regra dos Dois Temas.** Cada tema tem seus próprios valores; o escuro não é o claro invertido. Imagens que existem em claro e escuro (capturas do InfoFrota) trocam com o tema.
**A Regra do Filete.** Bordas e linhas são a tinta a 11% (`--line`) ou 20% (`--line-strong`) sobre o fundo, nunca uma cor própria.

## Typography

**Display Font:** Hanken Grotesk (fallback system-ui, -apple-system, Segoe UI, sans-serif), variável, arquivo local `hanken-grotesk-latin-wght-normal.woff2`
**Body Font:** Hanken Grotesk, a mesma família
**Label/Mono Font:** sem mono em uso

**Character:** Uma grotesca neutra e firme; a hierarquia vem de tamanho e de tracking apertado nos títulos, não de uma segunda família.

### Hierarchy
- **Display** (400, clamp(38px, 3.24vw + 25.4px, 72px), 1.04, tracking -0.038em): `h1` do hero.
- **Headline** (400, clamp(30px, 1.72vw + 23.3px, 48px), 1.1, tracking -0.03em): um `h2` por seção.
- **Title** (400, 24px no celular e 28px a partir de 1024px, 1.2): `h3`, passos do fluxo.
- **Card title** (500, 18px, 20px a partir de 1024px, 1.3, tracking -0.01em): nomes em cartões e linhas, nome das barras.
- **Body** (400, 16px, 1.55): texto corrido; notas limitadas a 56ch.
- **Small** (400, 14px, 1.5): metadados, links de apoio, legendas.
- **Label** (500, 13px, 1.4, tracking 0.01em): botão de copiar, rótulos curtos.

### Named Rules
**A Regra da Escala Fechada.** Só existem os tamanhos acima (`--t-label` a `--t-h1`); a página nunca cria um tamanho novo. Números grandes ficam um degrau abaixo do `h2` (`--t-stat`, 38px em 1440).
**A Regra do Título Inteiro.** Títulos usam `text-wrap: balance` e `hyphens: manual`; nunca quebram palavra.

## Layout

Uma coluna de 1280px (`--container`) com margem lateral de 80px no desktop, 48px a partir de 640px e 24px no celular; grade de 12 colunas com intervalo de 24px (12px no celular). O hero é dividido: texto em 5 colunas à esquerda, retrato em 6 colunas à direita (início na 7). O menu fica centralizado, 72px de altura (56px no celular), fixo, com o logotipo à esquerda e idioma e tema à direita; o item da seção atual ganha um filete de 2px sob o link. Seções recebem 120px de respiro acima e 72px abaixo (96 e 48 no celular). Escala de espaço de 4/8: 4, 8, 12, 16, 24, 32, 48, 64, 96 e 128px. O rodapé é em colunas (duas colunas de 4 de 12 na grade, em 1024px ou mais).

No celular (até 767px) todo link e botão fora de texto corrido tem 44px de altura, fotos laterais vão para baixo do texto com altura de `min(100vw - 2rem, 380px)`, e a foto das conquistas é omitida. Gráficos largos rolam na horizontal dentro da própria figura (1100px de largura mínima).

### Named Rules
**A Regra da Tela por Seção.** Cada seção tem uma ou duas telas de altura e um único `h2`; o que não cabe é cortado, não espremido.

## Elevation & Depth

Plano por padrão. A profundidade vem de tom (chapa cinza sobre o papel) e de um filete de 1px (`box-shadow: 0 0 0 1px var(--line)`) em capturas e molduras. Sombra de verdade só aparece em estado: o pulso do indicador "ao vivo" e os pontos de interesse do kit, ambos fora do fluxo de leitura. Cartões do kit usam `inset 0 1px 0` mais `0 1px 2px` sutis.

### Named Rules
**A Regra do Plano.** Em repouso, superfícies são planas; moldura é filete, não sombra.

## Shapes

Raios suaves em escala única (`data-radius="soft"`): 8px em botões e campos pequenos, 12px em ferramentas da barra, 20px em fotos e capturas, e 99px só nos trilhos das barras de comparação. O botão de copiar usa 8px. Fotos ficam recortadas pelo raio de 20px; capturas de tela do fluxo InfoFrota ficam em proporção 1600/939 sem recorte nas bordas.

## Components

### Buttons
- **Shape:** raio de 8px, altura de 44px (36px na variante pequena), padding horizontal de 24px, peso 500, 16px.
- **Primary:** fundo cobalto (#1f2de6), texto branco; no escuro, lavanda (#8d98ff) com texto de tinta. Hover mistura 86% da ação com a tinta.
- **Secondary (tonal):** fundo da tinta a 8% sobre o fundo, com contorno de 1px em tinta (acrescentado no build porque, sem contorno, o contraste era 1,22:1). Hover a 14%.
- **Press:** `translateY(1px) scale(.985)`. Transições de 150ms (entrada) e 120ms (saída), ease `cubic-bezier(.2, .8, .2, 1)`.

### Navigation
Barra fixa centralizada com fundo do tema e filete inferior. Links com 44px de altura de toque; seção atual marcada por sublinhado de 2px. Idioma e tema são botões de 44x44px com raio de 12px; hover em tinta a 8%. Skip-link no início.

### Cards / Containers
Dois contêineres: a moldura de imagem (`shot`, fundo chapa cinza, raio 20px, filete de 1px) e as linhas (`rows`), listas separadas por filete com 16px de respiro inferior e links sublinhados em cor de ação (sublinhado a 40% da ação, 3px de afastamento). Não há cartões sombreados.

### Barras de comparação
Trilho de 14px de altura em chapa cinza, preenchimento em tinta a 38% sobre o fundo, e só a melhor barra em cor de acento. Valores em numerais tabulares.

### Fluxo fixo do InfoFrota (pinned-chapters)
Passos de texto à esquerda e capturas à direita fixas na tela; o passo ativo mantém tinta cheia e filete lateral de 1px, os outros ficam em cinza de apoio. Troca de captura em 480ms de opacidade e 900ms de escala (1.03 para 1). Sem movimento sob `prefers-reduced-motion`.

### Foto que se revela (picture-develops)
Foto das conquistas, com a altura do texto ao lado (até 560px), que se revela em 1400ms de escala. Só no desktop; abaixo de 1024px vira bloco 4/3 e no celular some.

### Botão de copiar
32px de altura, contorno de 1px na tinta a 20%, raio 8px; no estado copiado, contorno e texto na cor de ação.

## Do's and Don'ts

### Do:
- **Do** usar cobalto (#1f2de6) ou lavanda (#8d98ff no escuro) só para ação, link e o melhor dado.
- **Do** desenhar cada tema com seus próprios valores e conferir contraste de texto em AA nos dois.
- **Do** manter botões e links com 44px de altura de toque no celular.
- **Do** usar apenas a escala de tipo e a de espaço do kit (4/8) e a escala de raios 8, 12 e 20px.
- **Do** emoldurar imagens com filete de 1px e raio de 20px, sem sombra.
- **Do** marcar cada texto bilíngue como `[[PT :: EN]]` no fonte do build, e mostrar um idioma por vez.

### Don't:
- **Don't** adicionar uma segunda família tipográfica ou tamanhos fora da escala.
- **Don't** usar sombra para elevar cartões ou molduras em repouso.
- **Don't** usar o cobalto como cor de texto corrido, de título ou de fundo de seção.
- **Don't** mostrar barras de proficiência, partículas, robôs ou cérebros (compromisso de marca do PRODUCT.md).
- **Don't** misturar português e inglês na mesma tela.
- **Don't** editar `assets/`: o kit é fonte fixa; ajustes ficam no `<style>` de `tools/src/head.html`.
