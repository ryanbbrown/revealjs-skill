# PDF Export

Presentations can be exported to PDF via a special print stylesheet. Here's an example of an exported presentation that's been uploaded to SlideShare: <https://slideshare.net/hakimel/revealjs-300>.

Note: This feature has only been confirmed to work in [Google Chrome](https://google.com/chrome) and [Chromium](https://www.chromium.org/Home).

## Instructions

1. Open your presentation with `print-pdf` included in the query string, for example: `http://localhost:8000/?print-pdf`. You can test this at [revealjs.com/demo?print-pdf](/demo/?print-pdf).
2. Open the in-browser print dialog (CTRL/CMD+P).
3. Change the **Destination** setting to **Save as PDF**.
4. Change the **Layout** to **Landscape**.
5. Change the **Margins** to **None**.
6. Enable the **Background graphics** option.
7. Click **Save** 🎉

![Chrome Print Settings](https://s3.amazonaws.com/hakim-static/reveal-js/pdf-print-settings-2.png)

## Speaker Notes

Your [speaker notes](/speaker-view/) can be included in the PDF export by enabling the `showNotes`.

```
Reveal.configure({ showNotes: true });
```

Notes are printed in an overlay box on top of the slide. If you'd rather print them on a separate page, after the slide, set `showNotes` to `"separate-page"`.

```
Reveal.configure({ showNotes: 'separate-page' });
```

## Page Numbers

If you want to number printed pages, make sure to enable [slide numbers](/slide-numbers/).

## Page Size

Export dimensions are inferred from the configured [presentation size](/presentation-size/). Slides that are too tall to fit within a single page will expand onto multiple pages. You can limit how many pages a slide may expand to using the `pdfMaxPagesPerSlide` config option. For example, to ensures that no slide ever grows to more than one printed page you can set it to 1.

```
Reveal.configure({ pdfMaxPagesPerSlide: 1 });
```

## Separate Pages for Fragments

[Fragments](/fragments/) are printed on separate slides by default. Meaning if you have a slide with three fragment steps, it will generate three separate slides where the fragments appear incrementally.

If you prefer printing all fragments in their visible states on the same slide you can use the `pdfSeparateFragments` config option.

```
Reveal.configure({ pdfSeparateFragments: false });
```

## Alternative Ways to Export

You can also use [decktape](https://github.com/astefanutti/decktape) to convert your presentation to PDF via the command line.