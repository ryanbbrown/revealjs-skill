# Reveal.js Advanced Features

Reference for reveal.js features beyond basic slides.

## Slide Attributes

Use HTML comments to set per-slide properties:

```html
<section data-background="#1a1a2e">
<section data-transition="zoom">
<section data-auto-animate>
```

## Backgrounds

```html
<!-- Solid color -->
<section data-background-color="#283b95">

<!-- Gradient -->
<section data-background-gradient="linear-gradient(to bottom, #283b95, #17b2c3)">

<!-- Image -->
<section data-background-image="image.jpg" data-background-opacity="0.5">

<!-- Video -->
<section data-background-video="video.mp4" data-background-video-loop data-background-video-muted>
```

## Transitions

Per-slide: `data-transition="zoom"`

Options: `none`, `fade`, `slide`, `convex`, `concave`, `zoom`

Separate in/out: `data-transition="slide-in fade-out"`

## Auto-Animate

Smoothly animate elements between slides:

```html
<section data-auto-animate>
  <h1>Title</h1>
</section>

<section data-auto-animate>
  <h1>Title</h1>
  <h2>Subtitle appears with animation</h2>
</section>
```

For non-text elements, use matching `data-id`:

```html
<section data-auto-animate>
  <div data-id="box" style="width: 100px; background: blue;"></div>
</section>

<section data-auto-animate>
  <div data-id="box" style="width: 300px; background: red;"></div>
</section>
```

## Fragments

Progressive reveal within a slide:

```html
<p class="fragment">Appears first</p>
<p class="fragment fade-up">Slides up while fading in</p>
<p class="fragment highlight-red">Turns red</p>
```

Fragment styles:
- `fade-out`, `fade-up`, `fade-down`, `fade-left`, `fade-right`
- `fade-in-then-out`, `fade-in-then-semi-out`
- `grow`, `shrink`, `strike`
- `highlight-red`, `highlight-green`, `highlight-blue`

Control order:
```html
<p class="fragment" data-fragment-index="2">Shows second</p>
<p class="fragment" data-fragment-index="1">Shows first</p>
```

## Code Highlighting

Basic:
```html
<pre><code class="language-python">
def hello():
    print("Hello")
</code></pre>
```

Line highlighting (step-through):
```html
<pre><code data-line-numbers="1-2|3|4">
let a = 1;
let b = 2;
let c = x => 1 + 2 + x;
c(3);
</code></pre>
```

## Layout Utilities

Built-in reveal.js classes:

- `r-fit-text` - Auto-size text to fill slide
- `r-stretch` - Stretch element to fill remaining vertical space
- `r-stack` - Layer elements on top of each other

```html
<h1 class="r-fit-text">BIG TEXT</h1>

<img class="r-stretch" src="image.jpg">

<div class="r-stack">
  <img class="fragment" src="img1.jpg">
  <img class="fragment" src="img2.jpg">
</div>
```

## Vertical Slides

Create drill-down sections with nested `<section>` tags:

```html
<section>
  <section>
    <h2>Horizontal Slide 1</h2>
  </section>
  <section>
    <h2>Vertical Slide (down from Slide 1)</h2>
  </section>
</section>

<section>
  <h2>Horizontal Slide 2</h2>
</section>
```

## Configuration Options

```javascript
Reveal.initialize({
  controls: true,          // Show navigation arrows
  progress: true,          // Show progress bar
  slideNumber: true,       // Show slide numbers
  hash: true,              // Update URL hash for each slide
  transition: 'slide',     // none/fade/slide/convex/concave/zoom
  center: false,           // Vertical centering (false for fixed titles)
  autoSlide: 5000,         // Auto-advance (ms), 0 to disable
  loop: false,             // Loop presentation
});
```
