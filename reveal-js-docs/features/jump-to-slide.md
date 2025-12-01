# Jump to Slide 4.5.0

You can skip ahead to a specific slide using reveal.js' jump-to-slide shortcut. Here's how it works:

1. Press G to activate
2. Type a slide number or id
3. Press Enter to confirm

## Navigating to Slide Number

When jumping to a slide you can either enter numeric value or a string. If you provide a number reveal.js will navigate to the desired slide number. If you type a string, reveal.js will try to locate a slide with a matching `id` and navigate to it.

Here are a couple of examples of different input and their resulting navigation.

| Input | Result |
| --- | --- |
| 5 | Navigate to slide number 5 |
| 6/2 | Navigate to horizontal slide 6, vertical slide 2 |
| the-end | Navigate to a slide with this id (`<section id="the-end">`) |

## Disable Jump to Slide

Jump to Slide is enabled by default but if you want to turn it off you can set the `jumpToSlide` config value to `false`.

```
Reveal.initialize({
  jumpToSlide: false,
});
```