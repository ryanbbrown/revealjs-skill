# API

We provide an extensive JavaScript API for controlling navigation and checking the current state of a presentation. If you're working with a single presentation instance the API can be accessed via the global `Reveal` object.

### Navigation

```
// Navigate to a specific slide
Reveal.slide(indexh, indexv, indexf);

// Relative navigation
Reveal.left();
Reveal.right();
Reveal.up();
Reveal.down();
Reveal.prev();
Reveal.next();

// Fragment navigation
Reveal.navigateFragment(indexf); // (-1 means all fragments are invisible)
Reveal.prevFragment();
Reveal.nextFragment();

// Checks which directions we can navigate towards
// {top: false, right: true, bottom: false, left: false}
Reveal.availableRoutes();

// Checks which fragment directions we can navigate towards
// {prev: false, next: true}
Reveal.availableFragments();
```

### Misc

```
// Call this if you add or remove slides to update controls, progress, etc
Reveal.sync();
// Call this to sync just one slide
Reveal.syncSlide((slide = currentSlide));
// Call this to sync just one slide's fragments
Reveal.syncFragments((slide = currentSlide));

// Call this to update the presentation scale based on available viewport
Reveal.layout();

// Randomize the order of slides
Reveal.shuffle();

// Returns the present configuration options
Reveal.getConfig();

// Fetch the current scale of the presentation
Reveal.getScale();

// Returns an object with the scaled presentationWidth & presentationHeight
Reveal.getComputedSlideSize();

Reveal.getIndices((slide = currentSlide)); // Coordinates of the slide (e.g. { h: 0, v: 0, f: 0 })
Reveal.getProgress(); // (0 == first slide, 1 == last slide)

// Array of key:value maps of the attributes of each slide in the deck
Reveal.getSlidesAttributes();

// Returns the slide background element at the specified index
Reveal.getSlideBackground(indexh, indexv);

// Returns the speaker notes for the slide
Reveal.getSlideNotes((slide = currentSlide));

// Retrieves query string as a key:value map
Reveal.getQueryHash();

// Returns the path to the slide as represented in the URL
Reveal.getSlidePath((slide = currentSlide));
```

### Slides

```
// Returns the slide element matching the specified index
Reveal.getSlide(indexh, indexv);

// Retrieves the previous and current slide elements
Reveal.getPreviousSlide();
Reveal.getCurrentSlide();

// Returns an all horizontal/vertical slides in the deck
Reveal.getHorizontalSlides();
Reveal.getVerticalSlides();

// Total number of slides
Reveal.getTotalSlides();
Reveal.getSlidePastCount();

// Array of all slides
Reveal.getSlides();
```

### Slide State

```
// Checks if the presentation contains two or more
// horizontal/vertical slides
Reveal.hasHorizontalSlides();
Reveal.hasVerticalSlides();

// Checks if the deck has navigated on either axis at least once
Reveal.hasNavigatedHorizontally();
Reveal.hasNavigatedVertically();

Reveal.isFirstSlide();
Reveal.isLastSlide();
Reveal.isVerticalSlide();
Reveal.isLastVerticalSlide();
```

### Modes

```
// Shows a help overlay with keyboard shortcuts, optionally pass true/false
// to force on/off
Reveal.toggleHelp();

// Toggle presentation states, optionally pass true/false to force on/off
Reveal.toggleOverview();
Reveal.toggleAutoSlide();
Reveal.togglePause();

Reveal.isOverview();
Reveal.isAutoSliding();
Reveal.isPaused();
```

### DOM Elements

```
// Retrieve key DOM elements
Reveal.getRevealElement(); // <div class="reveal">
Reveal.getSlidesElement(); // <div class="slides">
Reveal.getViewportElement(); // <div class="reveal-viewport">
Reveal.getBackgroundsElement(); // <div class="backgrounds">
```

## More Reading

* [Plugin API](/plugins/#api)