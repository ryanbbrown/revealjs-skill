# Transitions

When navigating a presentation, we transition between slides by animating them from right to left by default. This transition can be changed by setting the `transition` config option to a valid [transition style](#styles). Transitions can also be overridden for a specific slide using the `data-transition` attribute.

```
<section data-transition="zoom">
  <h2>This slide will override the presentation transition and zoom!</h2>
</section>

<section data-transition-speed="fast">
  <h2>Choose from three transition speeds: default, fast or slow!</h2>
</section>
```

## Styles

This is a complete list of all available transition styles. They work for both slides and slide backgrounds.

| Name | Effect |
| --- | --- |
| none | Switch backgrounds instantly |
| fade | Cross fade — *default for background transitions* |
| slide | Slide between backgrounds — *default for slide transitions* |
| convex | Slide at a convex angle |
| concave | Slide at a concave angle |
| zoom | Scale the incoming slide up so it grows in from the center of the screen |

## Separate In-Out Transitions

You can also use different in and out transitions for the same slide by appending `-in` or `-out` to the transition name.

```
<section data-transition="slide">The train goes on …</section>
<section data-transition="slide">and on …</section>
<section data-transition="slide-in fade-out">and stops.</section>
<section data-transition="fade-in slide-out">
  (Passengers entering and leaving)
</section>
<section data-transition="slide">And it starts again.</section>
```

## Background Transitions

We transition between slide backgrounds using a cross fade by default. This can be changed on a global level or overridden for specific slides. To change background transitions for all slides, use the `backgroundTransition` config option.

```
Reveal.initialize({
  backgroundTransition: 'slide',
});
```

Alternatively you can use the `data-background-transition` attribute on any `<section>` to override that specific transition.