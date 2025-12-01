# Events

We dispatch a number of events to make it easy for you to react to changes in the presentation. `Reveal.on()` is used to add event listeners, and `Reveal.off()` is used to remove them.

```
Reveal.on('eventname', callbackFunction);
```

## Ready

The `ready` event is fired when reveal.js has loaded all non-async dependencies and is ready to accept API calls. To check if reveal.js is already 'ready' you can call `Reveal.isReady()`.

```
Reveal.on('ready', (event) => {
  // event.currentSlide, event.indexh, event.indexv
});
```

We also add a `.ready` class to the `.reveal` element so that you can hook into this with CSS.

The `Reveal.initialize` method also returns a [Promise](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise) which resolves when the presentation is ready. The following is synonymous to adding a listener for the `ready` event:

```
Reveal.initialize().then(() => {
  // reveal.js is ready
});
```

## Slide Changed

The `slidechanged` event is fired each time the slide changes. The event object holds the index values of the current slide as well as a reference to the previous and current slide HTML elements.

Some libraries, like MathJax (see [#226](https://github.com/hakimel/reveal.js/issues/226#issuecomment-10261609)), get confused by the transforms and display states of slides. Often times, this can be fixed by calling their update or render function from this callback.

```
Reveal.on('slidechanged', (event) => {
  // event.previousSlide, event.currentSlide, event.indexh, event.indexv
});
```

## Slide Transition End

The `slidechanged` event fires instantly as soon as the slide changes. If you'd rather invoke your event listener when the slide has finished transitioning and is fully visible, you can use the `slidetransitionend` event. The `slidetransitionend` event includes the same event data as `slidechanged`.

```
Reveal.on('slidetransitionend', (event) => {
  console.log(event.currentSlide);
});
```

## Resize

The `resize` event is fired when reveal.js changes the scale of the presentation.

```
Reveal.on('resize', (event) => {
  // event.scale, event.oldScale, event.size
});
```

## Feature-specific Events

* [Overview mode events](/overview/#events)
* [Fragment events](/fragments/#events)
* [Auto-Slide events](/auto-slide/#events)