# React Framework

Reveal.js can be added to a React project a few different ways.

1. [Install and setup reveal.js via npm](#installing-from-npm)
2. [Use third-party packages](#third-party-packages)

## Installing From npm

You can add and initialize reveal.js in a JavaScript/TypeScript source file like `main.tsx` or `app.tsx`.

You can do so globally i.e. outside of app/component functions or inside one of them. In the latter case, you have to be careful not to stack initializations. Only initialize a slide deck once. If you need to reconfigure, use the `configure` function or `destroy` the deck before initializing again.

To begin, install reveal using `npm`:

```
npm install reveal.js
```

If you are using TypeScript, you need to install the types as well:

```
npm i --save-dev @types/reveal.js
```

#### Imports

You will need the following imports:

```
import Reveal from 'reveal.js';
import 'reveal.js/dist/reveal.css';
import 'reveal.js/dist/theme/black.css'; // "black" theme is just an example
```

#### Initialization

Finally, add the [initialization code](https://revealjs.com/initialization/) most suitable to your project's needs.

If you decide to initialize the slide deck inside an app or component function where slide deck containers are in the returned JSX, we recommended you use a `useEffect` hook to do so. This will ensure that initialization happens after the containers are first rendered.

It is also recommended to use refs to maintain a handle on the slide deck container `div` and the corresponding `reveal` instance. These refs can help make sure each slide deck is only initialized once.

#### Here's a full working example:

```
// App.tsx
import { useEffect, useRef } from "react";
import Reveal from "reveal.js";
import "reveal.js/dist/reveal.css";
import "reveal.js/dist/theme/black.css";

function App() {
    const deckDivRef = useRef<HTMLDivElement>(null); // reference to deck container div
    const deckRef = useRef<Reveal.Api | null>(null); // reference to deck reveal instance

    useEffect(() => {
        // Prevents double initialization in strict mode
        if (deckRef.current) return;

        deckRef.current = new Reveal(deckDivRef.current!, {
            transition: "slide",
            // other config options
        });

        deckRef.current.initialize().then(() => {
            // good place for event handlers and plugin setups
        });

        return () => {
            try {
                if (deckRef.current) {
                    deckRef.current.destroy();
                    deckRef.current = null;
                }
            } catch (e) {
                console.warn("Reveal.js destroy call failed.");
            }
        };
    }, []);

    return (
        // Your presentation is sized based on the width and height of
        // our parent element. Make sure the parent is not 0-height.
        <div className="reveal" ref={deckDivRef}>
            <div className="slides">
                <section>Slide 1</section>
                <section>Slide 2</section>
            </div>
        </div>
    );
}

export default App;
```

Note the use of `deckDivRef` in the `Reveal` constructor. This is important if you want to add multiple decks to the the same React app.

## React Portals

If you only want to sprinkle a few components into specific slides, we recommend keeping the reveal.js DOM tree outside of React and using [React Portals](https://react.dev/reference/react-dom/createPortal) to place react component into specific sections.

## Third Party Packages

The following third-party packages might prove useful for adding Reveal.js presentations to React projects or for adding React components/apps to Reveal.js presentations:

* [revealjs-react](https://github.com/blakeanedved/revealjs-react) - A React wrapper for the RevealJS Presentation Library.
* [react-reveal-slides](https://github.com/bouzidanas/react-reveal-slides) - A React component for creating Reveal.js presentations entirely in React.
* [revealjs-react-boilerplate](https://github.com/cberthou/revealjs-react-boilerplate) - A boilerplate for creating revealJS presentations using React.