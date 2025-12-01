# Slide Backgrounds

Slides are contained within a limited portion of the screen by default to allow them to fit any display and scale uniformly. You can apply full page backgrounds outside of the slide area by adding a `data-background` attribute to your `<section>` elements. Four different types of backgrounds are supported: color, image, video and iframe.

## Color Backgrounds

All CSS color formats are supported, including hex values, keywords, `rgba()` or `hsl()`.

```
<section data-background-color="aquamarine">
  <h2>🍦</h2>
</section>
<section data-background-color="rgb(70, 70, 255)">
  <h2>🍰</h2>
</section>
```

## Gradient Backgrounds

All CSS gradient formats are supported, including `linear-gradient`, `radial-gradient` and `conic-gradient`.

```
<section data-background-gradient="linear-gradient(to bottom, #283b95, #17b2c3)">
  <h2>🐟</h2>
</section>
<section data-background-gradient="radial-gradient(#283b95, #17b2c3)">
  <h2>🐳</h2>
</section>
```

## Image Backgrounds

By default, background images are resized to cover the full page. Available options:

| Attribute | Default | Description |
| --- | --- | --- |
| data-background-image |  | URL of the image to show. GIFs restart when the slide opens. |
| data-background-size | cover | See [background-size](https://developer.mozilla.org/docs/Web/CSS/background-size) on MDN. |
| data-background-position | center | See [background-position](https://developer.mozilla.org/docs/Web/CSS/background-position) on MDN. |
| data-background-repeat | no-repeat | See [background-repeat](https://developer.mozilla.org/docs/Web/CSS/background-repeat) on MDN. |
| data-background-opacity | 1 | Opacity of the background image on a 0-1 scale. 0 is transparent and 1 is fully opaque. |

```
<section data-background-image="http://example.com/image.png">
  <h2>Image</h2>
</section>
<section data-background-image="http://example.com/image.png"
          data-background-size="100px" data-background-repeat="repeat">
  <h2>This background image will be sized to 100px and repeated</h2>
</section>
```

## Video Backgrounds

Automatically plays a full size video behind the slide.

| Attribute | Default | Description |
| --- | --- | --- |
| data-background-video |  | A single video source, or a comma separated list of video sources. |
| data-background-video-loop | false | Flags if the video should play repeatedly. |
| data-background-video-muted | false | Flags if the audio should be muted. |
| data-background-size | cover | Use `cover` for full screen and some cropping or `contain` for letterboxing. |
| data-background-opacity | 1 | Opacity of the background video on a 0-1 scale. 0 is transparent and 1 is fully opaque. |

```
<section data-background-video="https://static.slid.es/site/homepage/v1/homepage-video-editor.mp4"
          data-background-video-loop data-background-video-muted>
  <h2>Video</h2>
</section>
```

## Iframe Backgrounds

Embeds a web page as a slide background that covers 100% of the reveal.js width and height. The iframe is in the background layer, behind your slides, and as such it's not possible to interact with it by default. To make your background interactive, you can add the `data-background-interactive` attribute.

| Attribute | Default | Description |
| --- | --- | --- |
| data-background-iframe |  | URL of the iframe to load |
| data-background-interactive | false | Include this attribute to make it possible to interact with the iframe contents. Enabling this will prevent interaction with the slide content. |

```
<section data-background-iframe="https://slides.com"
          data-background-interactive>
  <h2>Iframe</h2>
</section>
```

Iframes are lazy-loaded when they become visible. If you'd like to preload iframes ahead of time, you can append a `data-preload` attribute to the slide `<section>`. You can also enable preloading globally for all iframes using the `preloadIframes` configuration option.

## Background Transitions

We'll use a cross fade to transition between slide backgrounds by default. This can be changed using the [`backgroundTransition`](/transitions/#background-transitions) config option.

## Parallax Background

If you want to use a parallax scrolling background, set the first two properties below when initializing reveal.js (the other two are optional).

```
Reveal.initialize({
  // Parallax background image
  parallaxBackgroundImage: '', // e.g. "https://s3.amazonaws.com/hakim-static/reveal-js/reveal-parallax-1.jpg"

  // Parallax background size
  parallaxBackgroundSize: '', // CSS syntax, e.g. "2100px 900px" - currently only pixels are supported (don't use % or auto)

  // Number of pixels to move the parallax background per slide
  // - Calculated automatically unless specified
  // - Set to 0 to disable movement along an axis
  parallaxBackgroundHorizontal: 200,
  parallaxBackgroundVertical: 50
});
```

Make sure that the background size is much bigger than screen size to allow for some scrolling. [View example](/demo?parallaxBackgroundImage=https%3A%2F%2Fs3.amazonaws.com%2Fhakim-static%2Freveal-js%2Freveal-parallax-1.jpg&parallaxBackgroundSize=2100px%20900px).