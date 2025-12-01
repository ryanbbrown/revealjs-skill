# Touch Navigation

You can swipe to navigate through a presentation on any touch-enabled device. Horizontal swipes change between horizontal slides, vertical swipes change between vertical slides.

If you wish to disable this you can set the `touch` config option to false when initializing.

```
Reveal.initialize({
  touch: false,
});
```

If there's some part of your content that needs to remain accessible to touch events you'll need to highlight this by adding a `data-prevent-swipe` attribute to the element. One common example where this is useful is elements that need to be scrolled.

```
<section>
  <p data-prevent-swipe>Can't change slides by swiping across this element.</p>
</section>
```