# Presentation State

The presentation's current state can be fetched by using the `getState` method. A state object contains all of the information required to put the presentation back as it was when `getState` was first called. Sort of like a snapshot. It's a simple object that can easily be stringified and persisted or sent over the wire.

```
// Move to slide 1
Reveal.slide(1);

let state = Reveal.getState();
// {indexh: 1, indexv: 0, indexf: undefined, paused: false, overview: false}

// Move to slide 3
Reveal.slide(3);

// This restores the saved state, placing on slide 1 again
Reveal.setState(state);
```