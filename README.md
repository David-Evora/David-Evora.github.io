# Portfólio | David Évora

Portfólio pessoal bilíngue (português e inglês), desenvolvido com HTML, CSS e JavaScript puro. O site é estático e pode ser hospedado diretamente no GitHub Pages.

## Estrutura

- `index.html`: página publicada (gerada pelos arquivos-fonte).
- `.nojekyll`: evita que o GitHub Pages processe a pasta com Jekyll.
- `assets/`: imagens, fontes, estilos e scripts usados pelo site.
- `tools/src/`: arquivos-fonte do conteúdo e da estrutura da página.
- `tools/build.py`: gera o `index.html` a partir de `tools/src/`.
- `tools/make-variants.py`: gera versões responsivas das imagens (requer Pillow).
- `DESIGN.md`: documentação do sistema visual.

## Visualizar localmente

Na raiz do projeto, execute:

```bash
python -m http.server 8000
```

Depois, abra `http://localhost:8000` no navegador.

## Atualizar o site

1. Edite o conteúdo em `tools/src/body.html` e os metadados/estilos em `tools/src/head.html`.
2. Quando adicionar ou substituir imagens, gere as variantes com `python -m pip install pillow` (uma vez) e `python tools/make-variants.py`.
3. Gere novamente a página com `python tools/build.py`.
4. Confira o resultado localmente e envie as alterações ao GitHub.

O `index.html` é gerado automaticamente. Evite editá-lo manualmente, pois a próxima execução de `build.py` sobrescreve as alterações.

## Publicar com GitHub Pages

Para usar o endereço `https://david-evora.github.io/`, o repositório deve se chamar `David-Evora.github.io`.

1. Crie esse repositório público no GitHub.
2. Coloque o conteúdo desta pasta na raiz do repositório.
3. Em **Settings → Pages**, selecione **Deploy from a branch**, branch `main` e pasta `/ (root)`.
4. Salve e aguarde a publicação.

Para enviar pelo terminal, depois de criar o repositório vazio:

```bash
git init
git add .
git commit -m "Publica portfólio"
git branch -M main
git remote add origin https://github.com/David-Evora/David-Evora.github.io.git
git push -u origin main
```

## Conteúdo e contatos

O portfólio apresenta projetos, experiências, certificados e formas de contato. Revise o conteúdo e os links antes de publicar e sempre que fizer atualizações.
