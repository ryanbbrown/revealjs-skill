# Markup

Here's a barebones example of a fully working reveal.js presentation:

```
<html>
  <head>
    <link rel="stylesheet" href="dist/reveal.css" />
    <link rel="stylesheet" href="dist/theme/white.css" />
  </head>
  <body>
    <div class="reveal">
      <div class="slides">
        <section>Slide 1</section>
        <section>Slide 2</section>
      </div>
    </div>
    <script src="dist/reveal.js"></script>
    <script>
      Reveal.initialize();
    </script>
  </body>
</html>
```

The presentation markup hierarchy needs to be `.reveal > .slides > section` where the `section` element represents one slide and can be repeated indefinitely.

If you place multiple `section` elements inside of another `section` they will be shown as [vertical slides](/vertical-slides/). The first of the vertical slides is the "root" of the others (at the top), and will be included in the horizontal sequence. For example:

```
<div class="reveal">
  <div class="slides">
    <section>Horizontal Slide</section>
    <section>
      <section>Vertical Slide 1</section>
      <section>Vertical Slide 2</section>
    </section>
  </div>
</div>
```

It's also possible to write presentations using [Markdown](/markdown/).

## Viewport

The reveal.js viewport is the wrapper DOM element that determines the size of your presentation on a web page. By default, this will be the `body` element. If you're including multiple presentations on the same page each presentations `.reveal` element will act as their viewport.

The viewport is always decorated with a `reveal-viewport` class reveal.js is initialized.

## Slide States

If you set `data-state="make-it-pop"` on a slide `<section>`, "make-it-pop" will be applied as a class on the [viewport element](#viewport) when that slide is opened. This allows you to apply broad style changes to the page based on the active slide.

```
<section data-state="make-it-pop"></section>
```

```
/* CSS */
.make-it-pop {
  filter: drop-shadow(0 0 10px purple);
}
```

You can also listen to these changes in state via JavaScript:

```
Reveal.on('make-it-pop', () => {
  console.log('✨');
});
```