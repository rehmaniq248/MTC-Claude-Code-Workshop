---
name: ui-design
description: Restyle a plain/functional HTML page into a polished, distinctive interface without changing its behavior. Use whenever the user asks to "style", "restyle", "design", "make this look good", or "polish the UI" for an existing single-file HTML app.
---

# UI Design — BarakahPlan house style

Restyle the given HTML file into a new file. Preserve every element ID,
class hook used by JS, data attribute, and behavior exactly — this is a
visual pass only, never a functional rewrite. If asked to restyle
`X.html` into `Y.html`, leave `X.html` untouched.

## Direction

A calm, contemporary "study app" aesthetic — closer to a well-made
productivity tool than a mosque flyer. Avoid literal clip-art (no
crescent-moon icons, no green-and-gold default). Let the craft carry the
theme instead.

- **Palette**: one deep anchor color (ink navy or deep teal, not pure
  black) for text and structure, one warm accent (amber/terracotta) used
  sparingly for emphasis and the current-time indicator, a soft neutral
  background (off-white or very light warm gray, not stark #fff). Reuse
  the same three-note palette for the conflict badges instead of
  inventing a fourth: red stays a true alert red, yellow shifts to the
  warm accent tone, green becomes a muted sage — all should look like
  they belong to the same family, not stock traffic-light colors.
- **Type**: one serif or well-shaped display face for headings (course
  titles, page title), one clean grotesk for body/UI text (times, labels,
  buttons). Two families max. Set real type scale and line-height —
  no browser-default heading sizes.
- **Grid**: the weekly Mon–Fri × 8:00–22:00 grid is the centerpiece.
  Give prayer-time bands enough visual weight to read as structure (thin
  colored bars with a label), not so much that they compete with class
  blocks. Class blocks get soft shadows/borders, rounded corners, and
  clear hover states; conflict badges are compact and legible at a
  glance, not alarming banners.
- **Spacing & rhythm**: generous whitespace, consistent 8px-multiple
  spacing scale, aligned edges. No component should touch the viewport
  edge without padding.
- **Motion**: subtle only — a 150–200ms ease transition on hover/focus
  and on badge state changes. Nothing that delays reading the grid.
- **Dark mode**: support `prefers-color-scheme: dark` with the same
  palette logic inverted (don't just invert lightness on the accent —
  keep it warm). If the page has no theme toggle, that's fine; media
  query support is enough.

## Rules

1. Keep all functionality identical — same JS, same IDs/classes JS
   queries, same data flow. You're allowed to add wrapper elements or
   classes purely for styling as long as existing hooks still resolve.
2. Inline all CSS in a single `<style>` block (this stays a single-file
   app) unless the source already links a stylesheet.
3. Real accessibility: minimum 4.5:1 text contrast, visible focus rings,
   badges distinguishable by more than color alone (icon or label, not
   color-only red/yellow/green).
4. Responsive down to a single-column layout below ~640px — the grid can
   scroll horizontally on mobile rather than cramming.
5. No external fonts/CDN dependencies unless the environment allows
   network access at runtime; prefer system font stacks that approximate
   the intended serif/grotesk pairing if in doubt.
