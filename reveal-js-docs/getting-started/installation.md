# Installation

We provide three different ways to install reveal.js depending on your use case and technical experience.

1. The [basic setup](#basic-setup) is the easiest way to get started. No need to set up any build tools.
2. The [full setup](#full-setup) gives you access to the build tools needed to make changes to the reveal.js source code. It includes a web server which is required if you want to load external Markdown files (the basic setup paired with your own choice of local web server works too).
3. If you want to use reveal.js as a dependency in your project, you can [install from npm](#installing-from-npm).

#### Next Steps

Once reveal.js is installed, we recommend checking out the [Markup](/markup/) and [Config Option](/config/) guides.

## Basic Setup

We make a point of distributing reveal.js in a way that it can be used by as many people as possible. The basic setup is our most broadly accessible way to get started and only requires that you have a web browser. There's no need to go through a build process or install any dependencies.

1. Download the latest reveal.js version <https://github.com/hakimel/reveal.js/archive/master.zip>
2. Unzip and replace the example contents in index.html with your own
3. Open index.html in a browser to view it

That's it 🚀

## Full Setup - Recommended

Some reveal.js features, like external Markdown, require that presentations run from a local web server. The following instructions will set up such a server as well as all of the development tasks needed to make edits to the reveal.js source code.

1. Install [Node.js](https://nodejs.org/) (10.0.0 or later)
2. Clone the reveal.js repository

   ```
   $ git clone https://github.com/hakimel/reveal.js.git
   ```
3. Move to the reveal.js folder and install dependencies

   ```
   $ cd reveal.js && npm install
   ```
4. Serve the presentation and monitor source files for changes

   ```
   $ npm start
   ```
5. Open <http://localhost:8000> to view your presentation

### Development Server Port

The development server defaults to port 8000. You can use the `port` argument to switch to a different one:

```
npm start -- --port=8001
```

## Installing From npm

The framework is published to, and can be installed from, [npm](https://www.npmjs.com/package/reveal.js). Note that reveal.js is targeted at the browser and includes CSS, fonts and other assets so the npm dependency use case may be limited.

```
npm install reveal.js
# or
yarn add reveal.js
```

Once installed, you can include reveal.js as an ES module:

```
import Reveal from 'reveal.js';
import Markdown from 'reveal.js/plugin/markdown/markdown.esm.js';

let deck = new Reveal({
  plugins: [Markdown],
});
deck.initialize();
```

You'll also need to include the reveal.js styles and a [presentation theme](/themes/).

```
<link rel="stylesheet" href="/node_modules/reveal.js/dist/reveal.css" />
<link rel="stylesheet" href="/node_modules/reveal.js/dist/theme/black.css" />
```