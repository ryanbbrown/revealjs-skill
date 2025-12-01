# Pre-built Theme Usage Guide

This theme provides a professional consulting-style layout with fixed title positioning, decorative lines, and various content containers.

## Quick Start

1. Copy [styles.css](styles.css) to your presentation folder
2. Use the HTML boilerplate at the bottom of this file
3. Follow the slide structure and component patterns below

## Customization

If the user wants to customize the theme, ask about these options:

### Base Theme
The pre-built theme layers on top of reveal.js's `white.css`. Other light themes (`beige`, `serif`, `sky`, `simple`) should work with minimal changes. Dark themes (`black`, `dracula`, `moon`, `night`) require inverting colors - change `--box-bg`, `--box-border`, callout backgrounds to darker values.

### Things to Ask About
- **Colors**: Line color, accent colors for callouts (note/warning/tip), box backgrounds
- **Decorative lines**: Keep or remove the top title underline and bottom slide line
- **Typography**: Base font size, heading sizes
- **Box radius**: Sharp corners (0) vs rounded (8px default)

### Removing Decorative Lines

To remove the title underline:
```css
.reveal .slides section > h1,
.reveal .slides section > h2 {
  border-bottom: none;
  padding-bottom: 0;
}
```

To remove the bottom slide line:
```css
.reveal .slides section::after {
  display: none;
}
```

## Slide Structure

Every slide follows this pattern:

```html
<section>
  <h2>Slide Title</h2>
  <div class="content">
    <!-- Your content here -->
  </div>
  <div class="footnote">Optional footnote text</div>
</section>
```

- Title (`h1` or `h2`) stays fixed at top with underline
- `.content` wrapper centers content vertically in remaining space
- `.footnote` appears below the bottom decorative line

## Columns

```html
<div class="columns">
  <div>Column 1</div>
  <div>Column 2</div>
  <div>Column 3</div>
</div>
```

All direct children get equal width automatically.

## Boxes

Four box variants for containing content:

```html
<!-- Filled background with border -->
<div class="box">Content</div>

<!-- Border only, no fill -->
<div class="box-outlined">Content</div>

<!-- Header in box, content below (no outline) -->
<div class="box-header">
  <h3>Header</h3>
  <p>Content below header</p>
</div>

<!-- Header in box, everything outlined -->
<div class="box-header-outlined">
  <h3>Header</h3>
  <p>Content below header</p>
</div>
```

## Callouts

Base callout with color variants:

```html
<div class="callout callout-note">Note content</div>
<div class="callout callout-warning">Warning content</div>
<div class="callout callout-tip">Tip content</div>
<div class="callout callout-neutral">Neutral content</div>
```

### Callout Modifiers

Add these classes for different styles:

```html
<!-- Left border (default) -->
<div class="callout callout-note">...</div>

<!-- Left border + outline on all sides -->
<div class="callout callout-note callout-bordered">...</div>

<!-- Top border instead of left -->
<div class="callout callout-note callout-top">...</div>

<!-- Top border + outline -->
<div class="callout callout-note callout-top-bordered">...</div>

<!-- Top border + centered icon circle -->
<div class="callout callout-note callout-top-icon">
  <span class="callout-icon"><i class="fa-solid fa-lightbulb"></i></span>
  Content here
</div>
```

## Blockquotes

Standard blockquotes with optional citation:

```html
<blockquote>
  Quote text here.
  <cite>— Attribution</cite>
</blockquote>
```

## Icons

Include Font Awesome in the HTML head:

```html
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
```

Then use icons anywhere:

```html
<i class="fa-solid fa-gears"></i>
<i class="fa-solid fa-lightbulb"></i>
<i class="fa-solid fa-check"></i>
```

## Text Utilities

Size modifiers (base paragraph text is 0.7em):

```html
<p class="text-lg">Larger text (1em)</p>
<p class="text-xl">Extra large (1.3em)</p>
<p class="text-2xl">Double extra large (1.6em)</p>
```

Other utilities:

```html
<p class="text-muted">Grayed out secondary text</p>
<p class="text-center">Centered text</p>
<p class="text-xl text-center text-muted">Combine them</p>
```

## Section Dividers

For section title slides (centered, no decorative lines):

```html
<section id="section-intro" class="section-divider">
  <h1>Section Title</h1>
  <div class="content">
    <p>Optional subtitle</p>
  </div>
</section>
```

## CSS Variables

Customize the theme by overriding these variables:

```css
:root {
  /* Typography */
  --base-font-size: 32px;
  --text-size: 0.7em;
  --h1-size: 1.8em;
  --h2-size: 1.4em;
  --h3-size: 1.1em;

  /* Layout */
  --slide-padding: 60px;
  --content-gap: 30px;

  /* Colors */
  --text-color: #222;
  --line-color: #333;
  --box-bg: #f5f5f5;
  --box-border: #ddd;

  /* Callout colors */
  --note-color: #2196F3;
  --warning-color: #ff9800;
  --tip-color: #4caf50;
}
```

## HTML Boilerplate

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Presentation Title</title>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reset.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/white.css">
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="reveal">
    <div class="slides">

      <section>
        <h1>Title Slide</h1>
        <div class="content">
          <p>Subtitle or description</p>
        </div>
      </section>

      <!-- More sections... -->

    </div>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.js"></script>
  <script>
    Reveal.initialize({
      controls: true,
      progress: true,
      slideNumber: true,
      hash: true,
      transition: 'slide',
      center: false
    });
  </script>
</body>
</html>
```
