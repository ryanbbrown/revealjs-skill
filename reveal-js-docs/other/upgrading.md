# Upgrading From Version 3 to 4.0

We make a strong effort to avoid breaking changes but there are a couple in version 4.0. If you want to migrate an existing presentation follow these instructions.

### Update Asset Locations

Our JS and CSS assets have moved. In your presentation HTML, update the following `<script>` and `<link>` paths:

| Old location | New location |
| --- | --- |
| js/reveal.js | dist/reveal.js |
| css/reset.css | dist/reset.css |
| css/reveal.css | dist/reveal.css |
| css/theme/<theme-name>.css | dist/theme/<theme-name>.css |
| lib/css/monokai.css | plugin/highlight/monokai.css |
| lib/js/head.min.js | Deleted in 3.8.0 |

### Remove Print CSS from `<head>`

In your presentation HTML, remove the following script from the `<head>`. These styles are now baked into the reveal.css file.

```
<script>
  var link = document.createElement('link');
  link.rel = 'stylesheet';
  link.type = 'text/css';
  link.href = window.location.search.match(/print-pdf/gi)
    ? 'css/print/pdf.css'
    : 'css/print/paper.css';
  document.getElementsByTagName('head')[0].appendChild(link);
</script>
```

### Plugin Registration

If you keep a copy of the v3 /plugin directory there are *no breaking changes*. If you want to switch to the latest plugin versions, you'll need to update your `Reveal.initialize()` call to use the [new plugin registration syntax](/plugins/). Plugins are also available as ES modules.

```
<script src="dist/reveal.js"></script>
<script src="plugin/markdown/markdown.js"></script>
<script src="plugin/highlight/highlight.js"></script>
<script>
  Reveal.initialize({
    plugins: [RevealMarkdown, RevealHighlight],
  });
</script>
```

### Removed Multiplex and Notes Server

The Multiplex and Notes Server plugins have moved out of reveal.js core to their own repositories. See their corresponding README's for usage instructions.

* <https://github.com/reveal/multiplex>
* <https://github.com/reveal/notes-server>

### Other

* Removed `Reveal.navigateTo`, use `Reveal.slide` instead.
* We've switched build systems to gulp & rollup. Make sure to `npm install` to get the latest dependencies. The server is still started with `npm start`, just like before.