# Registro de progresso · Portfólio David Évora

Atualizado em 16/11/2026. Nada foi publicado, commitado ou enviado a repositórios. Este arquivo é a fonte do estado do projeto e é atualizado a cada etapa.

## 1. Etapas concluídas

**Fase 1: primeira versão (08 e 09/11/2026)**
- Auditoria de memória, repositórios, links e certificados (InfoFrota, C-MAPSS, SGTCC, certificado Java).
- Curadoria das imagens do arquivo `portfolio_imagens_curadas.zip` (imagens WebP sem EXIF; relatório em `docs/relatorio-curadoria-e-pendencias.md`).
- Site bilíngue (PT/EN), tema claro e escuro, página única, conceito "Fieldnotes & Signals". Essa versão foi **substituída** na fase 3.

**Fase 2: nova base de design (10/11/2026)**
- Pedido do David: impeccable e taste-skill passam a ser a base principal; cores e conceito podem mudar; usar todas as skills e plugins; liberada a busca em vercel-labs/skills e skills.sh.
- Repositórios das duas skills clonados (somente leitura). O ZIP enviado traz o taste-skill 2.5.1.
- Leitura das referências essenciais (impeccable: `SKILL.md`, `craft-floor.md`, `new-work.md`, `init.md`, `mode-persuade.md`; taste-skill: `SKILL.md`, textos de copy, `system.md`, `layout-v4.md`).
- `PRODUCT.md` criado e aceito pelo launcher do impeccable. Memória atualizada.

**Fase 3: reconstrução sobre taste-skill e impeccable (10 a 12/11/2026)**
- Kit do taste-skill 2.5.1 instalado em `assets/` (tipo `service`, site-kind `other`) e gate armado em `.taste-skill/`.
- Direção sorteada pelo `deal` do taste-skill e fechada no contrato `.impeccable/review/direction-contract.md` e no brief `.impeccable/surfaces/index-html.md` (modo Experience).
- `tools/src/head.html`, `body.html` e `app.js` reescritos; `tools/build.py` ganhou `srcset`; `tools/make-variants.py` gera as variantes de imagem.
- Conteúdo reduzido para o que sustenta o caso: InfoFrota (4 seções), C-MAPSS, SGTCC, conquistas, certificados, contato.
- `copy-lint`, `consistency`, `layout/check`, `perf` e `gate` rodados em várias rodadas. O gate oficial rodou duas vezes: FAIL na primeira (4 achados, corrigidos) e PASS na segunda, que fechou a construção (`.taste-skill/build.done.json`; limite de 3 rodadas).
- Revisão independente (`impeccable-finish-reviewer`): nota 9/10; correções aplicadas (cópia, alturas, imagens do InfoFrota viraram link para o site do projeto).
- `DESIGN.md` e `.impeccable/design.json` escritos pelo `impeccable-documenter`.
- Ajustes finais após o gate: textos mais curtos, variantes `srcset` 480/720/1200, gráfico do C-MAPSS com rolagem lateral no celular, fotos secundárias escondidas abaixo de 1200 px, ajustes de altura em tablet e celular.
- **Verificação final (12/11/2026, no `index.html` entregue):** layout limpo em 1440×900, 1024×768, 820×1180, 768×1024 e 390×844; axe-core com 0 violações em 4 combinações (desktop claro PT, desktop escuro EN, celular claro PT, celular escuro EN); sem erro de console nem requisição falha; sem estouro horizontal; `perf` 0 FAIL, 0 WARN (411 KiB, FCP 142 ms, layout shift 0); `consistency --quick` com 1 FAIL (telefone, dispensado em `.taste-skill/waivers.json`) e 26 WARN.

**Fase 4: currículo, segunda rodada, agente e SGTCC (16/11/2026)**
- Pedido do David: incluir o currículo, usar a segunda rodada do assistente como resultado principal, acrescentar os agentes com MCP e descrever o SGTCC como aplicação web nascida de um problema da UVV, mantendo o resto.
- `assets/curriculo-david-evora.pdf` (o PDF que ele enviou, sem alteração) com link no contato e no fecho. O prompt original proibia botão de CV; a regra caiu porque ele mesmo enviou o arquivo.
- Validação: título "39 de 56", barras da segunda rodada (19, 28, 33, 39), a primeira rodada (36 de 56, antes de qualquer ajuste) mantida em nota e a ressalva de que a segunda foi planejada depois de analisar os erros.
- Nova seção `#agente`: agente com Tool Calling (gpt-oss-120b via Groq, 12 de 13 contra 9 de 13, 9 de 13 com o avaliador original, correção pós-resultado declarada), API `/agente`, servidor MCP, n8n, SQL somente leitura; diagrama próprio. Passos 3 e 4 do fluxo e o cartão do hero atualizados.
- SGTCC: "aplicação web para o TCC", problema da UVV, apoio do Cursor no backend, 9 entrevistas.
- Conquistas: papel de desenvolvedor de soluções no Grand Prix; Docker, MySQL, Grafana, Node-RED e CLP no WorldSkills (confirmados pelo currículo). InfoFrota: vice-líder técnico.
- Certificados viraram a seção `#certificados` (Google Cloud GenAI, Claude Academy, Hugging Face em andamento, Java, Kaggle, Bradesco agrupado, Database Foundations) com miniaturas e variantes de imagem. Separar era necessário: junto com Conquistas passava de 2 telas no celular.
- Verificação: layout limpo em 1440, 1024, 820, 768, 390 e 1917×1080 (1280×720 mantém o achado antigo); axe 0 violações nas 4 combinações; `perf` PASS; `consistency --quick` só com o telefone (dispensado); **gate oficial novo: PASS** na versão final.

## 2. Arquivos e componentes

| Caminho | O que é |
|---|---|
| `index.html` | site final (~54 KB), gerado por `tools/build.py` |
| `tools/build.py` | expande `[[PT :: EN]]`, injeta `srcset`, monta o `index.html` |
| `tools/make-variants.py` | gera variantes WebP 480/720/1200 (precisa de Pillow); rodar antes do `build.py` |
| `tools/src/head.html`, `body.html`, `app.js` | CSS da página e metadados, conteúdo PT/EN, comportamento (idioma, tema, menu, copiar contato) |
| `assets/system.css`, `system.js` | sistema do taste-skill (tokens, tipo, botões) |
| `assets/layout/`, `motion/`, `ui/`, `moments/`, `backgrounds/`, `icons/` | partes do kit: layout, movimento, cartões, momentos (`pinned-chapters`, `picture-develops`), fundos, ícones |
| `assets/fonts/` | Hanken Grotesk variável, arquivo local |
| `assets/img/` | WebP (originais e variantes 480/720/1200), sem EXIF |
| `assets/curriculo-david-evora.pdf` | currículo enviado pelo David |
| `PRODUCT.md` | verdade do produto para o impeccable |
| `DESIGN.md`, `.impeccable/design.json` | sistema de design derivado do site entregue |
| `.impeccable/` | contrato de direção, brief da superfície, capturas de revisão |
| `.taste-skill/` | estado do gate, histórico e exceções (`waivers.json`) |
| `README.md` | publicação no GitHub Pages, edição, imagens, currículo |
| `docs/relatorio-curadoria-e-pendencias.md` | curadoria, ferramentas, testes e itens a confirmar |

## 3. Decisões de design

- Fatos, regras de privacidade, avisos de dados sintéticos e contatos autorizados não mudaram desde a fase 1.
- Bilíngue por marcadores `[[PT :: EN]]`; chaves `de-lang` e `de-theme` no `localStorage`; tema claro e escuro obrigatórios (pedido do David vence a regra do taste-skill que limita o escuro).
- **Direção:** cinza frio com cobalto (`cool-grey-cobalt`), Hanken Grotesk peso 400 nos títulos, raio `soft`, botões `tonal`, hero `split` com retrato à direita, nav centralizada, rodapé em colunas, fechamento tipográfico. Interface 90 a 95% neutra; o cobalto só aparece em botão, link e foco. Sem violeta.
- **Momentos:** `pinned-chapters` no fluxo do InfoFrota e `picture-develops` (foto que se revela uma vez, só a partir de 1200 px).
- **Cortes em relação à fase 1:** Jornada, Conhecimentos, Próximos passos, tabelas estendidas de validação, lightbox e diário visual saíram, porque o taste-skill pede seções de uma ou duas telas. Certificados abrem em imagem inteira por link.
- **Alturas:** no celular cada seção fica em até 1,5 tela (1266 px a 844) ou 1,9 a 2 telas (1592 a 1688), para não enquadrar a seção vizinha; `--hm` define a altura mínima em telas; `.g2` usa duas linhas de uma tela.
- **Gráfico do C-MAPSS** no celular: rolagem lateral dentro do próprio quadro (mínimo de 1060 px), para o texto do gráfico ficar legível.
- **Capturas do InfoFrota** são link para o site do projeto (`david-evora.github.io/InfoFrota/`), com `aria-label`.
- O rótulo "Fieldnotes & Signals" não aparece mais (o taste-skill reprova o nome). Sem geração de imagem: caminho code-first, sem comp.
- **Exceção registrada:** `phone-number` (número real e público, autorizado por David).

## 4. Próximas tarefas

1. David revisa o site e a lista de itens a confirmar (relatório, seção 6). O currículo cita o portfólio em david-evora.github.io: o repositório precisa se chamar `david-evora.github.io` para o endereço bater.
2. David roda no app os dois comandos de plugin: `/plugin marketplace add Leonxlnx/taste-skill` e `/plugin install taste-skill@taste-skill`. Comandos de barra só o usuário executa.
3. Publicação no GitHub Pages: só com autorização explícita do David (passos no `README.md`).
4. Depois de publicar: preencher `og:image`, `og:url` e `canonical` com o endereço real e conferir os links externos.
5. Opcional: tentar de novo `npx skills find` e o ranking em skills.sh.

## 5. Problemas pendentes

- **Gate oficial:** PASS na versão de 16/11/2026 (segundo gate, aberto com `--start`). A revisão independente e o `DESIGN.md` são da versão de 12/11 e não foram refeitos para a seção `#agente` e `#certificados`.
- **Revisor independente:** pedi modelo opus, rodou em Sonnet 5.5.
- **DESIGN.md:** o documentador não olhou capturas de tela.
- **PRODUCT.md:** não veio de entrevista nova com o David.
- **Seed do concept-seed:** pulado (superfície "pinned", direção já fixada).
- **WARN aceitos na consistência:** `skip-link` e verbos (checadores só em inglês), `share-meta` (sem `og:image` até haver endereço), `empty-area`, `no-visual`, `text-only`, `container-edges` do momento fixado, `section-gaps`, `photo-set`, `copy-*`, `nav-labels`, `links`. No `layout/check` em 1280×720 há um achado de seção vizinha em Conquistas. O detector do impeccable acusa 3 itens vindos de CSS do kit que o site não usa.
- **Limite de uso:** agentes anteriores falharam com erro 429 (limite de 5 horas); o trabalho seguiu em etapas.
- **taste-skill como plugin:** não aparece no catálogo da conta; usei o clone local. Instalação como plugin depende dos comandos da seção 4.
- **find-skills / skills.sh:** a busca não achou nada nas três tentativas; não ficou claro se foi falta de resultado ou rede bloqueada.
- **Links externos:** não testados de novo nesta rodada.
- **Itens a confirmar com o David:** relatório, seção 6.
