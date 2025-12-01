# Overview Mode

Press the »ESC« or »O« keys to toggle the overview mode on and off. While you're in this mode, you can still navigate between slides, as if you were at 1,000 feet above your presentation.

![Slide layout with vertical slides](/images/docs/overview.png)

## API

You can use the `toggleOverview()` API method to activate or deactivate the overview mode from JavaScript.

```
// Switch to the opposite of the current state
Reveal.toggleOverview();

// Activate the overview mode
Reveal.toggleOverview(true);

// Deactivate the overview mode
Reveal.toggleOverview(false);
```

## Events

We fire events when the overview mode is activated and deactivated.

```
Reveal.on('overviewshown', (event) => {
  /* ... */
});
Reveal.on('overviewhidden', (event) => {
  /* ... */
});
```