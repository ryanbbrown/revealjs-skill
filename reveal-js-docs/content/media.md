# Media

We provide convenient mechanics for autoplaying and lazy loading HTML media elements and iframes based on slide visibility and proximity. This works for [<video>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/video), [<audio>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/audio) and [<iframe>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/iframe) elements.

## Autoplay

Add `data-autoplay` to your media element if you want it to automatically start playing when the slide is shown:

```
<video
  data-autoplay
  src="http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4"
></video>
```

If you want to enable or disable autoplay globally, for all embedded media, you can use the `autoPlayMedia` configuration option. If you set this option to `true` ALL media will autoplay regardless of individual `data-autoplay` attributes. If you set it to `autoPlayMedia: false` NO media will autoplay.

```
Reveal.initialize({
  autoPlayMedia: true,
});
```

Note that embedded HTML `<video>`/`<audio>` and YouTube/Vimeo iframes are automatically paused when you navigate away from a slide. This can be disabled by decorating your element with a `data-ignore` attribute.

## Lightbox

You can turn any element into a media lightbox by adding the `data‑preview‑image`, `data‑preview‑video` or `data‑preview‑link` attribute. This will cause the media to open in a full-screen overlay when clicked. Learn more in the [Lightbox docs](/lightbox).

```
<img src="reveal.png" data-preview-video="video.mp4">
<a href="https://hakim.se" data-preview-link>Open Link</a>
```

## Lazy Loading

When working on presentations with a lot of media or iframe content it's important to load lazily. Lazy loading means that reveal.js will only load content for the few slides nearest to the current slide. The number of slides that are preloaded is determined by the `viewDistance` configuration option.

To enable lazy loading all you need to do is change your `src` attributes to `data-src` as shown below. This is supported for image, video, audio and iframe elements.

```
<section>
  <img data-src="image.png">
  <iframe data-src="https://hakim.se"></iframe>
  <video>
    <source data-src="video.webm" type="video/webm" />
    <source data-src="video.mp4" type="video/mp4" />
  </video>
</section>
```

### Lazy Loading Iframes

Note that lazy loaded iframes ignore the `viewDistance` configuration and will only load when their containing slide becomes visible. Iframes are also unloaded as soon as the slide is hidden.

When we lazy load a video or audio element, reveal.js won't start playing that content until the slide becomes visible. However there is no way to control this for an iframe since that could contain any kind of content. That means if we loaded an iframe before the slide is visible on screen it could begin playing media and sound in the background.

You can override this behavior with the `data-preload` attribute. The iframe below will be loaded according to the `viewDistance`.

```
<section>
  <iframe data-src="https://hakim.se" data-preload></iframe>
</section>
```

You can also change the default globally with the `preloadIframes` configuration option. If set to `true` ALL iframes with a `data-src` attribute will be preloaded when within the `viewDistance` regardless of individual `data-preload` attributes. If set to `false`, all iframes will only be loaded when they become visible.

## Iframes

Using iframes is a convenient way to include content from external sources, like a YouTube video or Google Sheet. reveal.js automatically detects YouTube and Vimeo embed URLs and autoplays them when the slide becomes visible.

If you add an `<iframe>` inside your slide it's constrained by the size of the slide. To break out of this constraint and add a full page iframe, you can use an [iframe slide background](/backgrounds/#iframe-backgrounds).

### Iframe Post Message

reveal.js automatically pushes two [post messages](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) to embedded iframes. `slide:start` when the slide containing the iframe is made visible and `slide:stop` when it is hidden.

```
// JavaScript inside of an iframe embedded within reveal.js
window.addEventListener('message', (event) => {
  if (event.data === 'slide:start') {
    // The slide containing this iframe is visible
  } else if (event.data === 'slide:stop') {
    // The slide containing this iframe is not visible
  }
});
```