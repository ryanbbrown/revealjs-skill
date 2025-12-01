# Presentation Size

All presentations have a "normal" size, that is, the resolution at which they are authored. reveal.js will automatically scale presentations uniformly based on the normal size to ensure that everything fits on any given display or viewport without changing the aspect ratio or layout of your content.

See below for a list of [config options](/config/) related to sizing, including their default values:

```
Reveal.initialize({
  // The "normal" size of the presentation, aspect ratio will
  // be preserved when the presentation is scaled to fit different
  // resolutions. Can be specified using percentage units.
  width: 960,
  height: 700,

  // Factor of the display size that should remain empty around
  // the content
  margin: 0.04,

  // Bounds for smallest/largest possible scale to apply to content
  minScale: 0.2,
  maxScale: 2.0,
});
```

## Center

Slides are vertically centered on the screen based on how much content they contain. To disable this and leave slides fixed at their configured height set `center` to `false`.

```
Reveal.initialize({ center: false });
```

## Embedded

By default, reveal.js will assume that it should cover the full browser viewport. If you want to embed your presentation within a smaller portion of a web page, or show [multiple presentations](/initialization/#multiple-presentations) on the same page, you can use the `embedded` [config option](/config/).

```
Reveal.initialize({ embedded: false });
```

An embedded presentation will base its size on the dimensions of its `.reveal` root. If the size of that element changes from a source other than the window `resize` event, you can call `Reveal.layout()` to manually trigger a layout update.

```
// Change the size of our presentation
document.querySelector('.reveal').style.width = '50vw';

// Make reveal.js aware of the size change
Reveal.layout();
```

## BYOL

If you want disable the built-in scaling and centering and Bring Your Own Layout, set `disableLayout: true`. That will make your slides cover 100% of the available page width and height and leave the responsive styling up to you.

```
Reveal.initialize({
  disableLayout: false,
});
```