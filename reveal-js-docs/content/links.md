# Internal links

You can create links from one slide to another. Start by giving your target slide a unique `id` attribute. Next, you can create an anchor with an href in the format `#/<id>`. Here's a complete working example:

```
<section>
	<a href="#/grand-finale">Go to the last slide</a>
</section>
<section>
	<h2>Slide 2</h2>
</section>
<section id="grand-finale">
	<h2>The end</h2>
	<a href="#/0">Back to the first</a>
</section>
```

## Numbered Links

It's also possible to link to slides based on their slide index. The href format for an numbered link is `#/0` where 0 is the horizontal slide number. To link to a [vertical slide](/vertical-slides/) use `#/0/0` where the second number is the index of the vertical slide target.

```
<a href="#/2">Go to 2nd slide</a>
<a href="#/3/2">Go to the 2nd vertical slide inside of the 3rd slide</a>
```

## Navigation Links

You can add relative navigation links that work similarly to the built in directional control arrows. This is done by adding one of the following classes to any clickable HTML element inside of the `.reveal` container.

```
<button class="navigate-left">Left</button>
<button class="navigate-right">Right</button>
<button class="navigate-up">Up</button>
<button class="navigate-down">Down</button>

<!-- Previous vertical OR horizontal slide -->
<button class="navigate-prev">Prev</button>

<!-- Next vertical OR horizontal slide -->
<button class="navigate-next">Next</button>
```

Each navigation element is automatically given an `enabled` class when it's a valid navigation route based on the current slide. For example, if you're on the first slide only `navigate-right` will have the `enabled` class since it's not possible to navigate towards the left.

## Lightbox Links

If the website you're linking to supports iframe embedding, you can use the `data-preview-link` attribute to open the link in an iframe lightbox. This way you can show an external website without leaving the slide deck. Learn more in the [Lightbox docs](/lightbox/#iframe-lightbox).

```
<a href="https://hakim.se" data-preview-link>Open Link</a>
```

Note that this will only work if the link allows for embedding. Many websites prevent embedding via `x-frame-options` or `Content-Security-Policy`.