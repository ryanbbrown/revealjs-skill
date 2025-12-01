# Creating a Plugin 4.0.0

We provide a lightweight specification and API for plugins. This is used by our default plugins like [code highlighting](/code/) and [Markdown](/markdown/) but can also be used to create your own plugins.

## Plugin Definition

Plugins are objects that contain the following properties.

| Property | Value |
| --- | --- |
| id String | The plugins unique ID. This can be used to retrieve the plugin instance via `Reveal.getPlugin(<id>)`. |
| init Function | An optional function that is called when the plugin should run. It's invoked with one argument; a reference to the [presentation instance](/api/) that the plugin was registered with.  The init function can optionally return a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise). If a Promise is returned, reveal.js will wait for it to resolve before the presentation finishes initialization and fires the [ready event](/events/#ready). |
| destroy Function | Optional function that is called when the reveal.js instance that this plugin is registered to is uninitialized. |

Here's an example plugin which shuffles all slides in a presentation when the T key is pressed. Note that we export a function that returns a new plugin object. This is done because there may be [multiple presentation instances on the same page](/initialization/#multiple-presentations), and each should have their own instance of our plugin.

```
// toaster.js
export default () => ({
  id: 'toaster',
  init: (deck) => {
    deck.addKeyBinding({ keyCode: 84, key: 'T' }, () => {
      deck.shuffle();
      console.log('🍻');
    });
  },
});
```

## Registering a Plugin

Plugins are registered by including them in the `plugins` array of the [config options](/config/). You can also register a plugin at runtime using `Reveal.registerPlugin( Plugin )`.

```
import Reveal from 'dist/reveal.esm.js';
import Toaster from 'toaster.js';

Reveal.initialize({
  plugins: [Toaster],
});
```

### Async Plugins

If your plugin needs to run asynchronous code before reveal.js finishes initializing it can return a Promise. Here's an example plugin that will delay initialization for three seconds.

```
let WaitForIt = {
  id: 'wait-for-it',
  init: (deck) => {
    return new Promise((resolve) => setTimeout(resolve, 3000));
  },
};

Reveal.initialize({ plugins: [WaitForIt] }).then(() => {
  console.log('Three seconds later...');
});
```