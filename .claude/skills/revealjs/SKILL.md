---
name: revealjs
description: Create polished, professional reveal.js presentations from markdown. Use when the user asks to create slides, a presentation, a deck, or a slideshow. Supports themes, multi-column layouts, callout boxes, code highlighting, animations, speaker notes, and custom styling. Generates markdown + CSS and builds with mkslides or tidy-revealjs.
---

# Reveal.js Presentations

Create HTML presentations using reveal.js.

## What You Create

A reveal.js presentation consists of:

1. **HTML file** - Contains slides and loads reveal.js from CDN
2. **CSS file** (optional) - Custom styles for layouts, callouts, etc.

No build step needed - just open the HTML in a browser.

## Workflow

### Step 1: Ask Questions

Before creating the presentation, ask the user:

**Question 1: Do you want to use the pre-built professional theme?**

This theme includes fixed title positioning, decorative lines, columns, boxes, callouts with icons, and other polished components.

- **No** → Skip to Step 2, create custom CSS as needed
- **Yes** → Ask Question 2

**Question 2: Use the theme as-is, or customize it?**

- **As-is** → Copy [references/styles.css](references/styles.css) and follow [references/theme-usage.md](references/theme-usage.md)
- **Customize** → Ask about preferences:
  - Base reveal.js theme (white, black, etc.) - note: dark themes need color adjustments
  - Color scheme (accent colors, callout colors)
  - With or without decorative top/bottom lines
  - Typography preferences
  - Then modify the CSS variables in the theme accordingly

### Step 2: Create the Presentation

Generate the HTML file with this structure:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Presentation Title</title>

  <!-- Reveal.js core -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reset.css">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/reveal.css">

  <!-- Base theme: white, black, dracula, moon, night, beige, serif, solarized, league, sky, simple -->
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@5.1.0/dist/theme/white.css">

  <!-- Optional: Font Awesome for icons -->
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">

  <!-- Custom styles -->
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="reveal">
    <div class="slides">

      <section>
        <h1>Slide Title</h1>
        <p>Content here</p>
      </section>

      <section>
        <h2>Another Slide</h2>
        <ul>
          <li>Point one</li>
          <li>Point two</li>
        </ul>
      </section>

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
      center: false  // Set to false if using fixed title positioning
    });
  </script>
</body>
</html>
```

### Step 3: Design Principles

**Diverse presentation is key.** Even when slides have similar content types, vary the visual presentation:

- Use **different layouts** across slides: columns on one, stacked boxes on another, callouts with icons on a third
- Mix container styles: plain text, boxes, callouts, blockquotes
- Use **visual hierarchy**: `<strong>` for key terms, different colors to distinguish categories
- Break up lists with other elements (quotes, callouts, columns)
- Don't repeat the same layout pattern on consecutive slides

**Keep it scannable:**
- Short bullet points, not paragraphs
- One main idea per slide when possible
- Use icons (Font Awesome) to add visual interest

**Vary text sizes:** Use text utility classes to create visual hierarchy:
- `.text-lg` (1em), `.text-xl` (1.3em), `.text-2xl` (1.6em) for larger text
- `.text-muted` for secondary/grayed text
- `.text-center` to center text
- When a slide has less content, make it bigger - don't leave empty space with tiny text
- Combine classes: `<p class="text-xl text-center">Big centered text</p>`

## Reveal.js Basics

### Slides

Each `<section>` is a slide. **Always add a unique `id` attribute** to each slide for stable identification:

```html
<section id="intro">
  <h2>Introduction</h2>
  <p>Content</p>
</section>

<section id="key-concepts">
  <h2>Key Concepts</h2>
  <p>More content</p>
</section>
```

Use descriptive, kebab-case IDs (e.g., `title`, `why-this-talk`, `case-study-1`, `conclusion`). These IDs:
- Appear in screenshot filenames for easy identification
- Remain stable even if slides are reordered or deleted
- Enable direct linking to specific slides via URL hash

### Vertical Slides (Drill-down)

Nest sections for vertical navigation:

```html
<section>
  <section><h2>Main Topic</h2></section>
  <section><h2>Detail 1 (press down)</h2></section>
  <section><h2>Detail 2</h2></section>
</section>
```

### Fragments (Progressive Reveal)

```html
<p class="fragment">Appears on click</p>
<p class="fragment fade-up">Slides up</p>
<p class="fragment highlight-red">Turns red</p>
```

### Speaker Notes

```html
<section>
  <h2>Slide</h2>
  <p>Visible content</p>
  <aside class="notes">
    Private notes - press S to open speaker view
  </aside>
</section>
```

### Backgrounds

```html
<section data-background-color="#283b95">
<section data-background-image="image.jpg" data-background-opacity="0.5">
<section data-background-gradient="linear-gradient(to bottom, #283b95, #17b2c3)">
```

### Transitions

```html
<section data-transition="zoom">  <!-- none, fade, slide, convex, concave, zoom -->
```

## Capturing Slide Screenshots with Decktape

Use decktape to capture screenshots of slides for review. This project includes a fork with optimized `--slides` support that uses slide IDs in filenames.

### Initial Capture (All Slides)

When a presentation is first created, capture all slides with a timestamped directory:

```bash
cd <presentation-directory>
npx decktape reveal presentation.html output.pdf \
  --screenshots \
  --screenshots-directory "screenshots_$(date +%Y%m%d_%H%M%S)"
```

This creates screenshots named by slide ID (e.g., `output_title_1280x720.png`, `output_key-concepts_1280x720.png`).

### Targeted Capture (Specific Slides)

After reviewing screenshots and identifying slides that need edits, capture only those slides:

```bash
# Capture only slides 2, 5, and 7-9
npx decktape reveal presentation.html output.pdf \
  --screenshots \
  --screenshots-directory "screenshots_$(date +%Y%m%d_%H%M%S)" \
  --slides 2,5,7-9
```

The `--slides` argument accepts:
- Individual slides: `1,3,5`
- Ranges: `1-5`
- Combined: `1-3,5,8-10`

### Workflow

1. **Create presentation** → Generate HTML with unique IDs on each `<section>`
2. **Capture all slides** → Run decktape without `--slides`
3. **Review screenshots** → Identify slides needing changes (filenames include slide IDs)
4. **Edit slides** → Make changes to HTML
5. **Re-capture specific slides** → Run decktape with `--slides` for only the edited slides
6. **Repeat** steps 3-5 until satisfied

The timestamped directories help track iterations, and slide IDs in filenames make it easy to identify which slide needs work even if slide order changes.

## References

- [references/styles.css](references/styles.css) - Professional theme with columns, boxes, callouts
- [references/theme-usage.md](references/theme-usage.md) - How to use the pre-built theme components
- [references/revealjs-features.md](references/revealjs-features.md) - Advanced features (auto-animate, code highlighting, etc.)
