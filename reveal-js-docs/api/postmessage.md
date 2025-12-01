# postMessage API

The framework has a built-in postMessage API that can be used when communicating with a presentation inside of another window. Here's an example showing how you'd make a reveal.js instance in the given window proceed to slide 2:

```
<window>.postMessage( JSON.stringify({ method: 'slide', args: [ 2 ] }), '*' );
```

## postMessage Events

When reveal.js runs inside of an iframe it can optionally bubble all of its events to the parent. Bubbled events are stringified JSON with three fields: namespace, eventName and state. Here's how you subscribe to them from the parent window:

```
window.addEventListener('message', (event) => {
  var data = JSON.parse(event.data);
  if (data.namespace === 'reveal' && data.eventName === 'slidechanged') {
    // Slide changed, see data.state for slide number
  }
});
```

## postMessage Callbacks

When you call any method via the postMessage API, reveal.js will dispatch a message with the return value. This is done so that you can call a getter method and see what the result is. Check out this example:

```
<revealWindow>.postMessage( JSON.stringify({ method: 'getTotalSlides' }), '*' );

window.addEventListener( 'message', event => {
  var data = JSON.parse( event.data );
  // `data.method`` is the method that we invoked
  if( data.namespace === 'reveal' && data.eventName === 'callback' && data.method === 'getTotalSlides' ) {
    data.result // = the total number of slides
  }
} );
```

## Turning postMessage on/off

This cross-window messaging can be toggled on or off using configuration flags. These are the default values.

```
Reveal.initialize({
  // Exposes the reveal.js API through window.postMessage
  postMessage: true,

  // Dispatches all reveal.js events to the parent window through postMessage
  postMessageEvents: false
});
```