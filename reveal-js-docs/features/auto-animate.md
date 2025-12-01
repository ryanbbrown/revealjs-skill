# Auto-Animate 4.0.0

reveal.js can automatically animate elements across slides. All you need to do is add `data-auto-animate` to two adjacent slide `<section>` elements and Auto-Animate will animate all matching elements between the two.

Here's a simple example to give you a better idea of how it can be used.

```
<section data-auto-animate>
  <h1>Auto-Animate</h1>
</section>
<section data-auto-animate>
  <h1 style="margin-top: 100px; color: red;">Auto-Animate</h1>
</section>
```

This example uses the `margin-top` property to move the element but internally reveal.js will use a CSS transform to ensure smooth movement. This same approach to animation works with most animatable CSS properties meaning you can transition things like `position`, `font-size`, `line-height`, `color`, `background-color`, `padding` and `margin`.

### Movement Animations

Animations are not limited to changes in style. Auto-Animate can also be used to automatically move elements into their new position as content is added, removed or rearranged on a slide. All without a single line of inline CSS.

```
<section data-auto-animate>
  <h1>Implicit</h1>
</section>
<section data-auto-animate>
  <h1>Implicit</h1>
  <h1>Animation</h1>
</section>
```

## How Elements are Matched

When you navigate between two auto-animated slides we'll do our best to automatically find matching elements in the two slides. For text, we consider it a match if both the text contents and node type are identical. For images, videos and iframes we compare the `src` attribute. We also take into account the order in which the element appears in the DOM.

In situations where automatic matching is not feasible you can give the objects that you want to animate between a matching `data-id` attribute. We prioritize matching `data-id` values above our automatic matching.

Here's an example where we've given both blocks a matching ID since automatic matching has no content to go on.

```
<section data-auto-animate>
  <div data-id="box" style="height: 50px; background: salmon;"></div>
</section>
<section data-auto-animate>
  <div data-id="box" style="height: 200px; background: blue;"></div>
</section>
```

## Animation Settings

You can override specific animation settings such as easing and duration either for the whole presentation, per-slide or individually for each animated element. The following configuration attributes can be used to change the settings for a specific slide or element:

| Attribute | Default | Description |
| --- | --- | --- |
| data-auto-animate-easing | ease | A CSS [easing function](https://developer.mozilla.org/en-US/docs/Web/CSS/easing-function). |
| data-auto-animate-unmatched | true | Determines whether elements with no matching auto-animate target should fade in. Set to false to make them appear instantly. |
| data-auto-animate-duration | 1.0 | Animation duration in seconds. |
| data-auto-animate-delay | 0 | Animation delay in seconds (can only be set for specific elements, not at the slide level). |
| data-auto-animate-id | *absent* | An [id](#auto-animate-id-%26-restart) tying auto-animate slides together. |
| data-auto-animate-restart | *absent* | [Breaks apart](#auto-animate-id-%26-restart) two adjacent auto-animate slides (even with the same id). |

If you'd like to change the defaults for the whole deck, use the following config options:

```
Reveal.initialize({
  autoAnimateEasing: 'ease-out',
  autoAnimateDuration: 0.8,
  autoAnimateUnmatched: false,
});
```

## Auto-Animate Id & Restart

When you want separate groups of auto-animated slides right next to each other you can use the `data-auto-animate-id` and `data-auto-animate-restart` attributes.

With `data-auto-animate-id` you can specify arbitrary ids for your slides. Two adjacent slides will only auto-animate if they have the same id or if both don't have one.

Another way to control auto-animate is the `data-auto-animate-restart` attribute. Applying this attribute to a slide will prevent auto-animate between the previous slide and it (even if they have the same id) but *not* between it and the next slide.

```
<section data-auto-animate>
  <h1>Group A</h1>
</section>
<section data-auto-animate>
  <h1 style="color: #3B82F6;">Group A</h1>
</section>
<section data-auto-animate data-auto-animate-id="two">
  <h1>Group B</h1>
</section>
<section data-auto-animate data-auto-animate-id="two">
  <h1 style="color: #10B981;">Group B</h1>
</section>
<section data-auto-animate data-auto-animate-id="two" data-auto-animate-restart>
  <h1>Group C</h1>
</section>
<section data-auto-animate data-auto-animate-id="two">
  <h1 style="color: #EC4899;">Group C</h1>
</section>
```

## Events

The `autoanimate` event is dispatched each time you step between two auto-animated slides.

```
Reveal.on('autoanimate', (event) => {
  // event.fromSlide, event.toSlide
});
```

## Example: Animating Between Code Blocks

We support animations between code blocks. Make sure that the code block has `data-line-numbers` enabled and that all blocks have a matching `data-id` value.

```
<section data-auto-animate>
  <pre data-id="code-animation"><code data-trim data-line-numbers>
    let planets = [
      { name: 'mars', diameter: 6779 },
    ]
  </code></pre>
</section>
<section data-auto-animate>
  <pre data-id="code-animation"><code data-trim data-line-numbers>
    let planets = [
      { name: 'mars', diameter: 6779 },
      { name: 'earth', diameter: 12742 },
      { name: 'jupiter', diameter: 139820 }
    ]
  </code></pre>
</section>
<section data-auto-animate>
  <pre data-id="code-animation"><code data-trim data-line-numbers>
    let circumferenceReducer = ( c, planet ) => {
      return c + planet.diameter * Math.PI;
    }

    let planets = [
      { name: 'mars', diameter: 6779 },
      { name: 'earth', diameter: 12742 },
      { name: 'jupiter', diameter: 139820 }
    ]

    let c = planets.reduce( circumferenceReducer, 0 )
  </code></pre>
</section>
```

## Example: Animating Between Lists

We match list items individually to let you animate new items being added or removed.

```
<section data-auto-animate>
  <ul>
    <li>Mercury</li>
    <li>Jupiter</li>
    <li>Mars</li>
  </ul>
</section>
<section data-auto-animate>
  <ul>
    <li>Mercury</li>
    <li>Earth</li>
    <li>Jupiter</li>
    <li>Saturn</li>
    <li>Mars</li>
  </ul>
</section>
```

## Advanced: State Attributes

We add state attributes to the different elements involved in an auto-animation. These attributes can be tied into if you want to, for example, fine-tune the animation behavior with custom CSS.

Right before an auto-animation starts we add `data-auto-animate="pending"` to the slide `<section>` coming into view. At this point the upcoming slide is visible and all of the animated elements have been moved to their starting positions. Next we switch to `data-auto-animate="running"` to indicate when the elements start animating towards their final properties.

Each individual element is decorated with a `data-auto-animate-target` attribute. The value of the attribute is a unique ID for this particular animation OR "unmatched" if this element should animate as unmatched content.