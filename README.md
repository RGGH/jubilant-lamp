# Sphinx > GitHub Actions > Pages

![example workflow](https://github.com/RGGH/ghp2/actions/workflows/sphinx.yml/badge.svg)

### [jubilantlamp](https://rggh.github.io/jubilant-lamp/)

- click settings to enable github pages : https://docs.github.com/en/pages/quickstart
- add workflow permissions : https://github.com/ad-m/github-push-action/issues/96#issuecomment-889984928
- to use this as a base, use : git remote remove origin so you can start a new repo<br>
  eg : git remote add origin https://github.com/RGGH/the-new-repo-name.git
- The workflow action uses `pip install ghp-import`
- The yaml file uses 'master' not main
- [Full Article and Tutorial on the redandgreen website](https://redandgreen.co.uk/sphinx-to-github-pages-via-github-actions/)

`<script type="text/javascript" src="https://cdnjs.buymeacoffee.com/1.0.0/button.prod.min.js" data-name="bmc-button" data-slug="DrPi" data-color="#FFDD00" data-emoji=""  data-font="Cookie" data-text="Buy me a coffee" data-outline-color="#000000" data-font-color="#000000" data-coffee-color="#ffffff" > </script>`

