# Auto-Slide

Presentations can be configured to step through slides automatically, without any user input. To enable this you will need to specify an interval for slide changes using the `autoSlide` config option. The interval is provided in milliseconds.

```
// Slide every five seconds
Reveal.initialize({
  autoSlide: 5000,
  loop: true,
});
```

A play/pause control element will automatically appear for auto-sliding decks. Sliding is automatically paused if the user starts interacting with the deck. It's also possible to pause or resume sliding by pressing »A« on the keyboard (won't work in the embedded demo here).

You can disable the auto-slide controls and prevent sliding from being paused by specifying `autoSlideStoppable: false` in your [config options](/config/).

## Slide Timing

It's also possible to override the slide duration for individual slides and fragments by using the `data-autoslide` attribute.

```
<section data-autoslide="2000">
  <p>After 2 seconds the first fragment will be shown.</p>
  <p class="fragment" data-autoslide="10000">
    After 10 seconds the next fragment will be shown.
  </p>
  <p class="fragment">
    Now, the fragment is displayed for 2 seconds before the next slide is shown.
  </p>
</section>
```

## Auto-Slide Method

The `autoSlideMethod` config option can be used to override the default function used for navigation when auto-sliding.

We step through all slides, both horizontal and [vertical](/vertical-slides/), by default. To only navigate along the top layer and ignore vertical slides, you can provide a method that calls `Reveal.right()`.

```
Reveal.configure({
  autoSlideMethod: () => Reveal.right(),
});
```

## Events

We fire events whenever auto-sliding is paused or resumed.

```
Reveal.on('autoslideresumed', (event) => {
  /* ... */
});
Reveal.on('autoslidepaused', (event) => {
  /* ... */
});
```