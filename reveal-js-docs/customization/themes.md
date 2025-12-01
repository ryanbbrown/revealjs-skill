# Themes

The framework comes with a few different themes included.

| Name | Preview |
| --- | --- |
| black (default) | Black background, white text, blue links |
| white | White background, black text, blue links |
| league | Gray background, white text, blue links |
| beige | Beige background, dark text, brown links |
| night | Black background, thick white text, orange links |
| serif | Cappuccino background, gray text, brown links |
| simple | White background, black text, blue links |
| solarized | Cream-colored background, dark green text, blue links |
| moon | Dark blue background, thick grey text, blue links |
| dracula |  |
| sky | Blue background, thin dark text, blue links |
| blood | Dark background, thick white text, red links |

Each theme is available as a separate stylesheet. To change theme you will need to replace **black** below with your desired theme name in index.html:

```
<link rel="stylesheet" href="dist/theme/black.css" />
```

## Custom Properties

All theme variables are exposed as CSS custom properties in the pseudo-class `:root`. See [the list of exposed variables](https://github.com/hakimel/reveal.js/blob/master/css/theme/template/exposer.scss).

## Creating a Theme

If you want to add a theme of your own see the instructions here: [/css/theme/README.md](https://github.com/hakimel/reveal.js/blob/master/css/theme/README.md).

Alternatively, if you want a clean start, you can opt to start from a blank CSS document and customize everything from the ground up.