# Site Architecture

The initial package is semantic HTML, one CSS file, one progressively enhanced navigation script, and local raster assets. This minimizes migration cost and creates no build or framework dependency.

## Portability boundary

- all internal site assets use relative paths;
- repository documents are linked one directory upward and must be remapped during portfolio integration;
- no deployment configuration lives here;
- no Golden Apple package imports this directory;
- no claims are fetched dynamically until a signed release/status source exists.

## Accessibility baseline

Landmarks, keyboard skip navigation, visible focus behavior, semantic headings, reduced reliance on color, responsive layouts, and alt-equivalent descriptions are required. A production move must add automated and manual WCAG 2.2 AA review.
