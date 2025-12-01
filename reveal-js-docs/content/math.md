# Math

The Math plugin lets you include beautifully typeset math formulas in your slides. To get started, make sure that reveal.js is initialized with the math plugin enabled.

```
<script src="plugin/math/math.js"></script>
<script>
  Reveal.initialize({ plugins: [RevealMath.KaTeX] });
</script>
```

We're using the KaTeX typesetter in this example but you can also choose from [MathJax 2](#mathjax-2) or [3](#mathjax-3-4.2.0).

Now that the plugin is registered we can start adding [LaTeX](https://en.wikipedia.org/wiki/LaTeX) formulas to our slides.

```
<section>
  <h2>The Lorenz Equations</h2>
  \[\begin{aligned} \dot{x} &amp; = \sigma(y-x) \\ \dot{y} &amp; = \rho x - y -
  xz \\ \dot{z} &amp; = -\beta z + xy \end{aligned} \]
</section>
```

## Markdown

To include math inside of a presentation written in Markdown, wrap the equation using one the available math delimiters like `$$`:

```
<section data-markdown>$$ J(\theta_0,\theta_1) = \sum_{i=0} $$</section>
```

## Typesetting Libraries

The math plugin offers three choices of math typesetting libraries that you can use to render your math. Each variant is its own plugin that can be accessed via `RevealMath.<Variant>`. If you don't have a preference, we recommend going with KaTeX.

| Library | Plugin Name | Config Property |
| --- | --- | --- |
| [KaTeX](https://katex.org/) | RevealMath.KaTeX | [katex](#katex-4.2.0) |
| [MathJax 2](https://docs.mathjax.org/en/v2.7-latest/) | RevealMath.MathJax2 | [mathjax2](#mathjax-2) |
| [MathJax 3](https://www.mathjax.org/) | RevealMath.MathJax3 | [mathjax3](#mathjax-3-4.2.0) |

### KaTeX 4.2.0

Adjust options through the `katex` configuration object. Below is how the plugin is configured by default. If you don't intend to change these values you do not need to include the `katex` config option at all.

```
Reveal.initialize({
  katex: {
    version: 'latest',
    delimiters: [
      { left: '$$', right: '$$', display: true },
      { left: '$', right: '$', display: false },
      { left: '\\(', right: '\\)', display: false },
      { left: '\\[', right: '\\]', display: true },
    ],
    ignoredTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
  },
  plugins: [RevealMath.KaTeX],
});
```

Note that by default the latest KaTeX is loaded from a remote server (<https://cdn.jsdelivr.net/npm/katex>). To use a fixed version set `version` to, for example, `0.13.18`.

If you want to use KaTeX offline you'll need to download a copy of the library (e.g. with npm) and use the `local` configuration option (the `version` option will then be ignored), for example:

```
Reveal.initialize({
  katex: {
    local: 'node_modules/katex',
  },
  plugins: [RevealMath.KaTeX],
});
```

### MathJax 2

Adjust options through the `mathjax2` configuration object. Below is how the plugin is configured by default. If you don't intend to change these values you do not need to include the `mathjax2` config option at all.

```
Reveal.initialize({
  mathjax2: {
    mathjax: 'https://cdn.jsdelivr.net/npm/mathjax@2/MathJax.js',
    config: 'TeX-AMS_HTML-full',
    // pass other options into `MathJax.Hub.Config()`
    tex2jax: {
      inlineMath: [
        ['$', '$'],
        ['\\(', '\\)'],
      ],
      skipTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    },
  },
  plugins: [RevealMath.MathJax2],
});
```

Note that the latest MathJax 2 is loaded from a remote server. To use a fixed version set mathjax to, for example, <https://cdn.jsdelivr.net/npm/mathjax@2.7.8/MathJax.js>.

If you want to use MathJax offline you'll need to download a copy of the library (e.g. with npm) and point `mathjax` to the local copy.

### MathJax 3 4.2.0

Adjust options through the `mathjax3` configuration object. Below is how the plugin is configured by default. If you don't intend to change these values you do not need to include the `mathjax3` config option at all.

```
Reveal.initialize({
  mathjax3: {
    mathjax: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js',
    tex: {
      inlineMath: [
        ['$', '$'],
        ['\\(', '\\)'],
      ],
    },
    options: {
      skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    },
  },
  plugins: [RevealMath.MathJax3],
});
```

Note that the latest MathJax 3 is loaded from a remote server. To use a fixed version set `mathjax` to, for example, <https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-mml-chtml.js>. Additionally, the config is now part of of the url, by default `tex-mml-chtml` is loaded which recognizes mathematics in both TeX and MathML notation, and generates output using HTML with CSS (the CommonHTML output format). This is one of the most general configurations, but it is also one of the largest, so you might want to consider a smaller one that is more tailored to your needs, e.g. `tex-svg`.

If you want to use MathJax offline you'll need to download a copy of the library (e.g. with npm) and adjust `mathjax` accordingly.