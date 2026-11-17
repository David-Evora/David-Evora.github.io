# Relatório: curadoria de imagens, decisões, testes e pendências

Portfólio de David Évora · versão de 16/11/2026 · nada foi publicado, commitado ou enviado para repositórios.

## 1. Conceito em uma frase

Um portfólio de uma página em que o trabalho lidera e a interface recua: cinza frio com cobalto só em botão, link e foco; Hanken Grotesk; retrato à direita no hero; InfoFrota primeiro, C-MAPSS depois, SGTCC em terceiro; PT e EN, claro e escuro. A direção veio do kit do taste-skill 2.5.1 (sorteio de paleta, tipo e momentos) e do contrato do impeccable (modo Experience). O nome "Fieldnotes & Signals" da primeira versão saiu: o taste-skill reprova esse tipo de nome. Descrição completa em `DESIGN.md`.

Mensagem de marca na página: "Curiosidade que vira código. Dados que viram conhecimento. Ideias que viram projetos."

## 2. Curadoria das imagens (arquivo `portfolio_imagens_curadas.zip`)

Todas as imagens do pacote estão em `assets/img/`, em WebP, sem EXIF, XMP nem localização, com variantes de 480, 720 e 1200 px onde o site precisa.

### Usadas no site (18 imagens-base)

| Uso | Arquivo |
|---|---|
| Hero (retrato profissional) | `hero.webp` |
| Certificados (abrem em imagem inteira por link) | `cert-grand-prix`, `cert-worldskills` (competidor), `cert-oracle`, `cert-java`, `cert-kaggle`, `cert-esx`, `cert-mundo-senai` |
| Fotos de WorldSkills | `worldskills-inicio`, `worldskills-competicao` |
| InfoFrota (capturas do site do projeto; clique abre o site) | `infofrota-hero-light/dark`, `infofrota-ia-light/dark`, `infofrota-tecnologia`, `infofrota-automacao`, `infofrota-dados` |
| C-MAPSS | `cmapss-previsto-vs-real` (gráfico de 3 painéis) |

### Deixadas de fora, e por quê

- **Oito imagens da primeira versão ficaram sem uso** na versão nova (Fórum IEL, Workshop Brasília, mais duas fotos de WorldSkills, o recorte do crachá e três gráficos do C-MAPSS). Tirei da pasta do site para não ficarem públicas sem aparecer na página. Estão em `/home/claude/portfolio-reserva/` neste ambiente e não entram no ZIP. Várias mostram outras pessoas. Se quiser alguma de volta, as originais continuam na sua curadoria.
- **Crachás de ESX e do Fórum IEL**: têm nome e QR code. Não entraram nem recortados.
- **Certificados Bradesco (Power BI e Excel)**: PDFs com QR e código de autenticação. Aparecem só como texto, sem imagem.
- **Foto da visita técnica (ArcelorMittal)**: qualidade fraca e outras pessoas na imagem.
- **Versão antiga do painel InfoFrota e modelo base do C-MAPSS (RMSE 16)**: versões substituídas.
- **Logos e capa OG do InfoFrota**: são do InfoFrota, não do portfólio.
- **`Repositorio.zip`** e a pasta **"Codigo C"**: dispensados por você.
- **Foto do hero some abaixo de 1200 px** (a foto grande que se revela) para a página caber nas alturas de tablet e celular. O retrato do hero continua em todos os tamanhos.

### Cuidado de privacidade nas imagens que ficaram

- O nome civil completo (David Evora Queiroz de Santana) aparece legível em vários certificados. Confirme se quer exibi-lo (item 6 da lista abaixo).
- O certificado Oracle Java mostra o nome e a assinatura da instrutora.
- As fotos de WorldSkills têm outras pessoas. Confirme que estão de acordo.
- As capturas do InfoFrota usam a interface azul do próprio site do projeto, com aviso de que os dados são sintéticos.

## 3. Projetos

| Projeto | Peso no site | Base dos fatos |
|---|---|---|
| **InfoFrota** | principal: 4 seções (visão, fluxo em passos, camada de IA, validação) | repositório, site do projeto, notebook Kaggle, adaptador no Hugging Face, artigo dev.to |
| **NASA C-MAPSS (RUL)** | segundo caso | repositório `cmapss-rul`: XGBoost final, RMSE 10,98 no teste, FD001, dados simulados, limites mostrados |
| **SGTCC** | terceiro, menor | repositório da equipe: README e código. Estado dos módulos (feito, em andamento, planejado) segue o README e o código |

Afirmações obrigatórias presentes: InfoFrota usa **dados sintéticos**; é projeto **independente, não oficial da CETURB/ES**; contagem de passageiros faz parte do InfoFrota; resultados experimentais não são desempenho em produção. O SGTCC aparece como "em desenvolvimento", sem link de demonstração (a versão hospedada não está disponível).

Não inventei prazo, métrica ou título. Onde a data de início não é verificável (os repositórios têm um commit consolidado), o site não afirma data.

## 4. Ferramentas: o que foi usado e o que não foi

Usado de verdade:
- **impeccable** (pbakaus): `context`, `PRODUCT.md`, modo Experience, contrato de direção, `impeccable detect`, agentes `impeccable-finish-reviewer` (revisão independente) e `impeccable-documenter` (`DESIGN.md`).
- **taste-skill 2.5.1** (Leonxlnx), pelo clone local e pelo ZIP: kit em `assets/`, `deal` de paleta/tipo/momentos, `copy-lint`, `consistency`, `layout/check`, `perf` e `gate`.
- Skills de design carregadas na sessão: `frontend-design`, `ui-ux-pro-max`, `artifact-design`.
- Playwright (Chromium), axe-core (axe-playwright-python), Pillow.
- Leitura direta dos repositórios (clones anônimos de repositórios públicos), páginas públicas e do PDF do certificado Java.

**Não usado**, apesar de citado no prompt: Spec Kit, Taskmaster, Serena, Understand Anything, fluxos do Superpowers, GStack, Trail of Bits, Strix e Vibe Coding Toolkit.

**Não feito:**
- O **taste-skill não está instalado como plugin**: não aparece no catálogo da minha conta, então usei o clone local. Para instalar, rode você mesmo no app: `/plugin marketplace add Leonxlnx/taste-skill` e depois `/plugin install taste-skill@taste-skill`. Comandos de barra só o usuário executa.
- **find-skills / skills.sh:** as buscas não acharam nada; não consegui distinguir "sem resultado" de "rede bloqueada". Nenhuma skill externa extra foi baixada.
- **concept-seed** do impeccable foi pulado: a superfície está fixada ("pinned") e a direção já vinha do taste-skill.
- **Sem comp visual:** não houve geração de imagem; o caminho foi code-first.
- **`PRODUCT.md`** não veio de uma entrevista nova com você; veio do prompt mestre e da memória.
- O revisor independente foi pedido em modelo opus e rodou em Sonnet 5.5. O documentador escreveu o `DESIGN.md` a partir do código, sem olhar capturas.
- Agentes anteriores (resumo de leitura) falharam com erro 429 do limite de uso; a leitura seguiu em etapas.

## 5. Testes realmente executados (Chromium, local)

| Verificação | Resultado |
|---|---|
| axe-core (WCAG 2.0/2.1/2.2 A e AA + boas práticas) em desktop claro PT, desktop escuro EN, celular claro PT, celular escuro EN | **0 violações** em cada uma |
| Estouro horizontal em 1440 px e 390 px, claro e escuro, PT e EN | nenhum |
| Imagens quebradas / visíveis sem texto alternativo | nenhuma / nenhuma |
| Texto no idioma errado visível | nenhum |
| Erros e avisos no console, requisições com falha | nenhum |
| Âncoras internas e arquivos locais referenciados | todos existem |
| Primeiro Tab vai ao link "pular para o conteúdo", foco visível | sim |
| Alternância de tema (claro para escuro e volta) | funciona |
| `prefers-reduced-motion` | sem erro, 7 títulos visíveis |
| Layout (`layout/check`) em 1440×900, 1024×768, 820×1180, 768×1024, 390×844 e 1917×1080 | sem achados (1280×720 mantém o achado antigo em Conquistas) |
| `perf` (1440 e 390) | 0 FAIL, 0 WARN |
| `consistency --quick` (1440 e 390) | 1 FAIL (telefone, com exceção) e 29 WARN |
| Gate oficial do taste-skill | 12/11: FAIL e depois PASS; **16/11 (versão final): PASS** (telefone dispensado, 24 WARN que não bloqueiam) |

**Gate:** o PASS de 16/11 vale para a versão entregue. A revisão independente (nota 9/10) e o `DESIGN.md` são de 12/11 e não cobrem as seções novas `#agente` e `#certificados`.

**Exceção registrada** em `.taste-skill/waivers.json`: o checador reprova o número de telefone em formato internacional. É o seu número real, publicado por decisão sua para recrutadores.

**WARN que aceitei:** `skip-link` e verbos (checadores só em inglês), `share-meta` (sem `og:image`), `empty-area`, `no-visual`, `text-only`, `container-edges` da cena fixada, `section-gaps`, `photo-set`, `copy-headline/headings/buttons`, `nav-labels`, `links`. Em 1280×720 o `layout/check` aponta uma seção vizinha visível em Conquistas. O detector do impeccable aponta 3 itens vindos de CSS do kit que o site não usa.

**Não executado:** Lighthouse, celulares reais, leitor de tela (NVDA, VoiceOver, TalkBack), Firefox e Safari, teste com o site hospedado (por isso não há `og:image` nem `canonical`) e nova checagem dos links externos nesta rodada. "0 violações no axe" não equivale a "acessível": é um piso automático.

## 6. O que preciso que você confirme

1. **Seu papel no SGTCC.** O README do repositório lista como autores Bianca Andrade (Backend) e Guilherme Suave (Frontend), e os commits que vi são da conta da Bianca. O site diz "atuo principalmente no backend", pela sua palavra. Quem abrir o repositório não vê seu nome. Sugestão: pedir para entrar no README e conferir com qual identidade você faz commits. Confirme também a frase "o grupo entrevistou 9 pessoas" e se a Bianca e a equipe concordam com o link.
2. ~~Papel no InfoFrota e equipe de quatro no Grand Prix~~: confirmados pelo seu currículo (vice-líder técnico; desenvolvedor de soluções; equipe de quatro).
3. ~~WorldSkills~~: Docker, MySQL, Grafana, Node-RED/CLP e a resposta 2x mais rápida vêm do seu currículo. Detalhes de dupla, TIA Portal e Ladder seguem fora do texto.
4. **Fórum IEL de Gestão 2025:** a data (jun 2025) e que você foi participante.
5. **Inglês B2:** consta no currículo. Há certificado ou teste?
6. **Nome civil completo e assinatura da instrutora** visíveis nos certificados.
7. **Fotos com outras pessoas** (WorldSkills): todas de acordo?
8. **Palavra "estágio"** no hero ("em busca de estágio") e no contato: é isso que quer dizer ao público?
9. **C-MAPSS "11,15 ± 0,10 na média de sementes":** o número veio da minha anotação de memória do projeto; confira com o repositório.
10. **Certificados:** datas e nomes como aparecem (Java Fundamentals, Oracle Academy, nov 2026; Kaggle, out 2026; ESX, set 2025; Mundo SENAI, jul 2025).
11. **Menção ao uso de assistentes de IA no desenvolvimento.** O artigo no dev.to diz que parte do desenvolvimento usou assistentes. O site não menciona. A decisão é sua; omitir não é falso, mas um recrutador pode ler o artigo.
12. **Currículo:** o PDF enviado em 16/11 está no site (`assets/curriculo-david-evora.pdf`, link no contato e no fecho). Ele traz o nome civil completo, telefone e e-mail. Para trocar por outra versão, substitua o arquivo.
13. **SGTCC hospedado:** a versão online não está disponível, então não há link de demo. Se mandar capturas de tela depois, entram.
14. **Conteúdo que não consegui ler por completo:** notebook do Kaggle (renderizado por JavaScript) e o artigo dev.to (leitura parcial). Dos 5 repositórios públicos do GitHub, avaliei InfoFrota e C-MAPSS; os outros 3 não entraram.
15. **Prévia em redes sociais:** sem imagem própria de 1200×630; depois de publicar, o README mostra como acrescentar `og:image`.

## 7. Limitações conhecidas

- Textos bilíngues no mesmo HTML: o código-fonte dobra o texto (~54 KB), e o site transfere cerca de 411 KiB no total.
- As seções foram dimensionadas para uma ou duas telas no celular. Texto novo muito longo pode estourar a altura e fazer o checador reclamar.
- Seções da primeira versão que saíram: Jornada (linha do tempo), Conhecimentos, Próximos passos, tabelas estendidas de validação, lightbox e diário visual. O conteúdo está no histórico da conversa e no relatório anterior; posso trazer de volta em seção própria se quiser.
- Os links externos foram lidos ao vivo durante a construção; não há verificação automática depois da publicação.

## 8. Mudanças de 16/11/2026

- Segunda rodada do assistente (39 de 56) como resultado principal; primeira rodada (36 de 56) em nota; ressalva de que a segunda foi planejada depois de analisar os erros.
- Seção `#agente`: Tool Calling, 12 de 13 contra 9 de 13 (diagnóstico de 13 perguntas sintéticas, uma rodada; 9 de 13 com o avaliador original; correção de hifens Unicode feita depois do resultado), API, MCP, n8n, SQL somente leitura.
- SGTCC como aplicação web nascida de um problema na UVV; Cursor no backend.
- Novos itens a confirmar: (a) "com apoio do Cursor" no SGTCC; (b) os números "3,38 contra 1,77 chamadas por pergunta" vieram do seu currículo, não do repositório que li; (c) o currículo cita o portfólio em david-evora.github.io.
- Não verifiquei o código do agente e do servidor MCP no repositório nesta rodada: os fatos vêm da sua memória de projeto e do currículo.
