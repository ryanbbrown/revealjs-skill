# Speaker View

reveal.js comes with a speaker notes plugin which can be used to present per-slide notes in a separate browser window. The notes window also gives you a preview of the next upcoming slide so it may be helpful even if you haven't written any notes. Press the »S« key on your keyboard to open the notes window.

A speaker timer starts as soon as the speaker view is opened. You can reset the timer by clicking on it.

Notes are defined by appending an `<aside>` element to a slide as seen below. You can add the `data-markdown` attribute to the aside element if you prefer writing notes using Markdown.

Alternatively you can add your notes in a `data-notes` attribute on the slide. Like `<section data-notes="Something important"></section>`.

When used locally, this feature requires that reveal.js [runs from a local web server](/installation/#full-setup).

```
<section>
  <h2>Some Slide</h2>

  <aside class="notes">
    Shhh, these are your private notes 📝
  </aside>
</section>
```

If you're using the [Markdown](/markdown/) plugin, you can add notes with the help of a special delimiter:

```
<section data-markdown="example.md" data-separator="^\n\n\n"
         data-separator-vertical="^\n\n" data-separator-notes="^Note:">
# Title
## Sub-title

Here is some content...

Note:
This will only display in the notes window.
</section>
```

## Adding the Speaker Notes Plugin

The plugin is already bundled with reveal.js. To enable the speaker notes plugin, add the plugin source to the `index.html` and add the plugin to the initialization of reveal.js.

```
<script src="plugin/notes/notes.js"></script>
<script>
  Reveal.initialize({
    plugins: [RevealNotes],
  });
</script>
```

## Share and Print Speaker Notes

Notes are only visible to the speaker inside of the speaker view. If you wish to share your notes with others you can initialize reveal.js with the `showNotes` configuration value set to `true`. Notes will appear along the bottom of the presentations.

When `showNotes` is enabled notes are also included when you [export to PDF](/pdf-export/). By default, notes are printed in a box on top of the slide. If you'd rather print them on a separate page, after the slide, set `showNotes: "separate-page"`.

## Speaker Notes Clock and Timers

The speaker notes window will also show:

* Time elapsed since the beginning of the presentation. If you hover the mouse above this section, a timer reset button will appear.
* Current wall-clock time
* (Optionally) a pacing timer which indicates whether the current pace of the presentation is on track for the right timing (shown in green), and if not, whether the presenter should speed up (shown in red) or has the luxury of slowing down (blue).

The pacing timer can be enabled by configuring the `defaultTiming` parameter in the `Reveal` configuration block, which specifies the number of seconds per slide. 120 can be a reasonable rule of thumb. Alternatively, you can enable the timer by setting `totalTime`, which sets the total length of your presentation (also in seconds). If both values are specified, `totalTime` wins and `defaultTiming` is ignored. Regardless of the baseline timing method, timings can also be given per slide `<section>` by setting the `data-timing` attribute (again, in seconds).

## Server Side Speaker Notes

In some cases it can be desirable to run notes on a separate device from the one you're presenting on. The Node.js-based notes plugin lets you do this using the same note definitions as its client side counterpart. See <https://github.com/reveal/notes-server>.