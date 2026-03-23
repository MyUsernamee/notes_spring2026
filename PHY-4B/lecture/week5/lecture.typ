#import "@preview/cetz:0.4.2"

This lecture was mostly going over Homework 3.

$ a + b = c $

#cetz.canvas({
  import cetz.draw: *

  line((-1., 1.0), (-1, -1.))
  content((-1, 1.5), text($ E $, fill: red))
  for (i) in range(0, 4) {
    let y = (2. * i/3 - 1.0)
    line((1., y), (-1., y), mark: (end: "stealth"), stroke: (paint: red))
  }
})
