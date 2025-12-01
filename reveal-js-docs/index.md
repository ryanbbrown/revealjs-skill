# reveal.js Documentation Index

This is the complete reveal.js documentation, organized by category. reveal.js is an open source HTML presentation framework for creating stunning presentations on the web.

## Getting Started

| File | Description |
|------|-------------|
| [home.md](getting-started/home.md) | Overview of reveal.js, its features, and links to the online editor |
| [installation.md](getting-started/installation.md) | Three installation methods: basic setup, full setup with build tools, and npm install |

## Content

How to create and structure slide content.

| File | Description |
|------|-------------|
| [markup.md](content/markup.md) | HTML structure for presentations (`.reveal > .slides > section`), viewport, and slide states |
| [markdown.md](content/markdown.md) | Writing slides in Markdown using `data-markdown` attribute, external files, and configuration |
| [backgrounds.md](content/backgrounds.md) | Slide backgrounds: colors, images, videos, iframes, and transitions |
| [media.md](content/media.md) | Embedding images, videos, and iframes with lazy loading and autoplay options |
| [lightbox.md](content/lightbox.md) | NEW - Zooming images and media into a full-screen lightbox overlay |
| [code.md](content/code.md) | Syntax highlighting with highlight.js, line numbers, and step-by-step highlights |
| [math.md](content/math.md) | LaTeX math rendering with MathJax or KaTeX plugins |
| [fragments.md](content/fragments.md) | Step-by-step reveal of elements with animation styles (fade, grow, shrink, etc.) |
| [links.md](content/links.md) | Internal navigation links, numbered links, and hash navigation |
| [layout.md](content/layout.md) | Slide layout using r-stack, r-hstack, r-vstack, r-fit-text, and r-stretch classes |
| [slide-visibility.md](content/slide-visibility.md) | Hiding slides with `data-visibility="hidden"` or `"uncounted"` |

## Customization

Styling and configuring presentation appearance.

| File | Description |
|------|-------------|
| [themes.md](customization/themes.md) | Built-in themes (black, white, league, etc.) and creating custom themes |
| [transitions.md](customization/transitions.md) | Slide transitions: none, fade, slide, convex, concave, zoom |
| [config.md](customization/config.md) | Complete list of all configuration options (controls, progress, hash, keyboard, etc.) |
| [presentation-size.md](customization/presentation-size.md) | Setting presentation dimensions, margins, and responsive scaling |

## Features

Interactive features and presentation modes.

| File | Description |
|------|-------------|
| [vertical-slides.md](features/vertical-slides.md) | Creating nested vertical slides and navigation stacks |
| [auto-animate.md](features/auto-animate.md) | Automatic animation between slides with `data-auto-animate` |
| [auto-slide.md](features/auto-slide.md) | Automatic slide advancement with timing and pause controls |
| [speaker-view.md](features/speaker-view.md) | Speaker notes, timer, and next slide preview (press S key) |
| [scroll-view.md](features/scroll-view.md) | NEW - Scrollable presentation mode as alternative to paginated slides |
| [slide-numbers.md](features/slide-numbers.md) | Displaying slide numbers in various formats |
| [jump-to-slide.md](features/jump-to-slide.md) | Quick navigation to specific slides (press G key) |
| [touch-navigation.md](features/touch-navigation.md) | Touch and swipe navigation on mobile devices |
| [pdf-export.md](features/pdf-export.md) | Exporting presentations to PDF via print dialog |
| [overview.md](features/overview.md) | Bird's-eye view of all slides (press O key) |
| [fullscreen.md](features/fullscreen.md) | Fullscreen mode (press F key) |

## API

JavaScript API for controlling presentations programmatically.

| File | Description |
|------|-------------|
| [initialization.md](api/initialization.md) | Initializing reveal.js, async initialization, and multiple instances |
| [api.md](api/api.md) | JavaScript API methods: navigation, state queries, slide manipulation |
| [events.md](api/events.md) | Event listeners for slidechanged, ready, resize, and other events |
| [keyboard.md](api/keyboard.md) | Keyboard shortcuts and custom key bindings |
| [presentation-state.md](api/presentation-state.md) | Getting and restoring presentation state (current slide, overview, paused) |
| [postmessage.md](api/postmessage.md) | Controlling presentations via postMessage for iframe embeds |

## Plugins

Extending reveal.js functionality.

| File | Description |
|------|-------------|
| [plugins.md](plugins/plugins.md) | Using plugins, built-in plugins (Highlight, Markdown, Math, Notes, Search, Zoom) |
| [creating-plugins.md](plugins/creating-plugins.md) | Creating custom plugins with the plugin API |
| [multiplex.md](plugins/multiplex.md) | Syncing presentations across multiple clients (master/client setup) |

## Other

Additional topics.

| File | Description |
|------|-------------|
| [react.md](other/react.md) | Using reveal.js with React framework |
| [upgrading.md](other/upgrading.md) | Upgrade guide from reveal.js 3.x to 4.x |
