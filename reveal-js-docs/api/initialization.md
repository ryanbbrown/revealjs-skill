# Initialization

The most common reveal.js use case is to have a single presentation which covers the full viewport. As of 4.0 we also support running [multiple presentations](#multiple-presentations) in parallel on the same page as well as including the library as an [ES module](#es-module).

If you only have a single presentation on the page we recommend initializing reveal.js using the global `Reveal` object. The `Reveal.initialize` method accepts one argument; a reveal.js [config object](/config/).

```
<script src="dist/reveal.js"></script>
<script>
  Reveal.initialize({ transition: 'none' });
</script>
```

The `initialize` method returns a promise which will resolve as soon as the presentation is ready and can be interacted with via the API.

```
Reveal.initialize().then(() => {
  // reveal.js is ready
});
```

## Multiple Presentations 4.0.0

To run multiple presentations side-by-side on the same page you can create instances of the `Reveal` class. The `Reveal` constructor accepts two arguments; the `.reveal` HTML element root of the presentation and an optional [config object](/config/).

Note that you will also need to set the [embedded](/presentation-size/#embedded) config option to true. This flag makes the presentations size themselves according to their `.reveal` root element size, rather than the browser viewport. You will also need to manually define the `width` and `height` CSS properties for each `.reveal .deck*` element in order to see them appear.

By default reveal.js will capture all keyboard events in the document. For embedded presentations we recommend initializing with `keyboardCondition: 'focused'` so that keyboard events are only captured when the presentation has been focused by the viewer.

```
<div class="reveal deck1">...</div>
<div class="reveal deck2">...</div>

<script src="dist/reveal.js"></script>
<script>
  let deck1 = new Reveal(document.querySelector('.deck1'), {
    embedded: true,
    keyboardCondition: 'focused', // only react to keys when focused
  });
  deck1.initialize();

  let deck2 = new Reveal(document.querySelector('.deck2'), {
    embedded: true,
  });
  deck2.initialize();
</script>
```

## ES Module 4.0.0

We provide two JavaScript bundles depending your use case. Our default presentation boilerplate uses `dist/reveal.js` which has broad cross browser support (ES5) and exposes Reveal to the global window (UMD).

The second bundle is `dist/reveal.esm.js` which makes it possible to import reveal.js as an ES module. This version can be used either directly in the browser with `<script type="module">` or bundled in your own build process.

Here's how to import and initialize the ES module version of reveal.js as well as the Markdown plugin:

```
<script type="module">
  import Reveal from 'dist/reveal.esm.js';
  import Markdown from 'plugin/markdown/markdown.esm.js';
  Reveal.initialize({
    plugins: [Markdown],
  });
</script>
```

If you're [installing reveal.js from npm](/installation/#installing-from-npm) and bundling it you should be able to use:

```
import Reveal from 'reveal.js';
Reveal.initialize();
```

## Uninitializing reveal.js 4.3.0

If you want to uninitialize reveal.js you can use the `destroy` API method. This will undo all changes that the framework has made to the DOM, remove all event listeners and unregister/destroy all plugins.

```
Reveal.destroy();
```