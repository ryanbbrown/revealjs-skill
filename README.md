# reveal-js-skill

A Claude Code skill for creating polished reveal.js presentations.

## What's Here

- **`.claude/skills/revealjs/`** - The skill itself
  - `SKILL.md` - Main skill instructions
  - `references/` - Pre-built theme CSS, usage docs, and reveal.js feature reference
- **`reveal-js-docs/`** - Scraped reveal.js documentation (markdown)
- **`scraping/`** - Python scripts used to fetch the docs
- **`examples/`** - Example presentations
- **`package.json`** - Includes [decktape fork](https://github.com/ryanbbrown/decktape) for slide screenshots

## Usage

Copy `.claude/skills/revealjs/` into your project's `.claude/skills/` directory. When you ask Claude Code to create a presentation, it will use this skill.

## Screenshot Workflow

The skill includes a decktape-based workflow for iterating on slides:

```bash
# Capture all slides
npx decktape reveal presentation.html output.pdf \
  --screenshots --screenshots-directory "screenshots_$(date +%Y%m%d_%H%M%S)"

# Re-capture only specific slides after edits
npx decktape reveal presentation.html output.pdf \
  --screenshots --screenshots-directory "screenshots_$(date +%Y%m%d_%H%M%S)" \
  --slides 2,5,7-9
```

## TODO

- [ ] Add example slide layouts (columns, callouts, tables, etc.) that the skill can reference for visual inspiration
