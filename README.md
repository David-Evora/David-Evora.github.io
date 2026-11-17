# Portfólio · David Évora

Site estático (HTML, CSS e JavaScript puro) com o portfólio de David Évora: Engenharia de Software · Dados · IA.
Português e inglês, tema claro e escuro. Base de design: taste-skill 2.5.1 e impeccable (cinza frio com cobalto, Hanken Grotesk). Detalhes em `DESIGN.md`.

Não usa backend, chaves de API, cookies nem rastreadores. Nenhum serviço externo é carregado: fonte e imagens ficam na própria pasta. Os únicos pedidos de rede são os links que o visitante clica.

> Este pacote **não foi publicado** em lugar nenhum. Nenhum repositório foi alterado e nenhum commit foi feito.
> Publicar é uma decisão sua, com os passos abaixo.

## O que tem na pasta

```
index.html            o site inteiro (página única, ~54 KB)
.nojekyll             pede ao GitHub Pages para servir os arquivos como estão
assets/img/           imagens WebP sem EXIF, com variantes 480/720/1200 px
assets/fonts/         Hanken Grotesk variável, arquivo local
assets/*.css, *.js    sistema do taste-skill (tokens, layout, movimento, cartões, momentos)
tools/build.py        gera o index.html a partir de tools/src/
tools/make-variants.py gera as variantes de imagem (precisa de Pillow)
tools/src/            head.html (CSS e metadados), body.html (conteúdo PT/EN), app.js (comportamento)
DESIGN.md, PRODUCT.md sistema de design e verdade do produto
docs/                 registro de progresso, relatório de curadoria e pendências
```

As pastas ocultas `.impeccable/` e `.taste-skill/` guardam o contrato de direção, capturas de revisão e o estado do gate de qualidade. Não são necessárias para o site funcionar. No ZIP entregue elas não vão; ao publicar, não precisa subir nada delas.

## Ver no computador

O site carrega módulos JavaScript, e o navegador não carrega módulos de `file://`. Use um servidor local:

```
python3 -m http.server 8000
```

e abra http://localhost:8000. Pelo GitHub Pages isso não é problema.

## Publicar no GitHub Pages

O site usa caminhos relativos (`assets/...`), então funciona tanto na raiz quanto em subpasta.

**Pela interface do GitHub (sem terminal):**

1. Crie um repositório novo na sua conta, por exemplo `portfolio`. Público.
2. Clique em **Add file → Upload files** e arraste o *conteúdo* desta pasta (`index.html`, `.nojekyll`, `assets`, `tools`, `docs`, `DESIGN.md`, `PRODUCT.md`, `README.md`). O arquivo `.nojekyll` é oculto: se o seu sistema não mostrar, crie-o depois com **Add file → Create new file**, nome `.nojekyll`, vazio.
3. Faça o commit.
4. Vá em **Settings → Pages**. Em *Build and deployment*, escolha **Deploy from a branch**, branch `main`, pasta `/ (root)`, e salve.
5. Em 1 a 2 minutos o endereço aparece na mesma tela. Para um repositório chamado `portfolio`, será `https://david-evora.github.io/portfolio/`.

**Endereço sem subpasta:** o seu currículo cita `david-evora.github.io`; para esse endereço, o repositório precisa se chamar exatamente `david-evora.github.io`.

**Pelo terminal** (depois de criar o repositório vazio no GitHub):

```
git init
git add .
git commit -m "Portfólio"
git branch -M main
git remote add origin https://github.com/David-Evora/portfolio.git
git push -u origin main
```

Depois siga o passo 4 acima.

## Depois de publicar

- Abra o site em uma janela anônima e teste: troca PT/EN, tema claro/escuro, menu no celular, botões de copiar contato, links dos certificados.
- Os links externos (InfoFrota, Kaggle, Hugging Face, dev.to, LinkedIn, GitHub, repositório do SGTCC) abrem em nova aba. Confira se todos respondem no dia da publicação.
- **Imagem de pré-visualização (Open Graph):** o site tem título e descrição para compartilhamento, mas **não tem `og:image`**, porque não há imagem própria para isso e o endereço final ainda não existe. Quando tiver o endereço, adicione em `tools/src/head.html`, junto das outras tags `og:`:
  ```html
  <meta property="og:image" content="https://SEU-ENDERECO/assets/img/hero.webp">
  <meta property="og:url" content="https://SEU-ENDERECO/">
  <link rel="canonical" href="https://SEU-ENDERECO/">
  ```
  e rode o `build.py` (abaixo). Uma imagem de 1200×630 px funciona melhor que o retrato do hero.

## Editar o conteúdo

1. Edite os textos em `tools/src/body.html`. Todo texto bilíngue usa o formato `[[texto em português :: text in English]]`. Se faltar o `::` ou algum `]]`, o `build.py` avisa.
2. Se trocou ou adicionou imagem, gere as variantes: `python3 tools/make-variants.py` (precisa de `pip install pillow`).
3. Rode, na raiz do projeto: `python3 tools/build.py` (só precisa de Python 3).
4. O `index.html` é regerado. Não edite o `index.html` à mão: a próxima geração apaga a edição.

Para mudar cores, tipografia ou espaçamentos, veja os tokens em `assets/system.css` e os ajustes da página em `tools/src/head.html`. O tema escuro é redefinido nos blocos `prefers-color-scheme` e `[data-theme="dark"]`. As seções do site têm altura pensada para o celular (uma ou duas telas); textos muito mais longos podem estourar essa altura. Ver a seção "Alturas" em `docs/registro-de-progresso.md`.

## Currículo

O PDF está em `assets/curriculo-david-evora.pdf`, com link no contato e no fecho da página. Para trocar a versão, substitua o arquivo mantendo o nome (ou mude o `href` em `tools/src/body.html` e rode o `build.py`). Remova do PDF o que não quiser público.

## Adicionar uma imagem nova

1. Remova EXIF e localização. Exemplo com Pillow:
   ```python
   from PIL import Image, ImageOps
   im = ImageOps.exif_transpose(Image.open("foto.jpg"))   # aplica a rotação do celular antes de perder o EXIF
   im.thumbnail((1600, 1600))
   im.save("assets/img/nome.webp", "WEBP", quality=82)    # o Pillow não grava EXIF por padrão
   ```
2. Não publique documentos com número, matrícula, QR code ou código de autenticação. Corte ou cubra a área.
3. Escreva o texto alternativo em português **e** em inglês (`alt` e `data-alt-en` no `body.html`).
4. Informe largura e altura na tag `<img>` e rode `make-variants.py` e `build.py`.

## Contatos exibidos

Os contatos abaixo foram autorizados por David para exibição pública. Para trocar, edite a seção de contato em `tools/src/body.html` e rode o `build.py`.

- E-mail: davievoraqs@gmail.com
- Telefone / WhatsApp: +55 27 99705-9161
- LinkedIn: https://www.linkedin.com/in/david-evora/
- GitHub: https://github.com/David-Evora
- Hugging Face: https://huggingface.co/David-Evora
- Kaggle: https://www.kaggle.com/davidevora

## Acessibilidade e idioma

- Link "pular para o conteúdo", foco visível, navegação completa por teclado, menu móvel com botão de abrir e fechar.
- Animações respeitam `prefers-reduced-motion`.
- A escolha de idioma e de tema fica salva no navegador (`localStorage`, chaves `de-lang` e `de-theme`). Sem escolha, o site segue o tema do sistema.
- Título, descrição e texto alternativo trocam junto com o idioma.
- Testado com axe-core em 4 combinações (0 violações). Isso é um piso automático, não prova de acessibilidade: falta teste com leitor de tela real.
