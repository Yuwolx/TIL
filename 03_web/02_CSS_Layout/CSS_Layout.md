# CSS Layout

## CSS Box Model

**Components**

- **contents**  
  - Can control width using the `width` property.

- **padding**  
  - Space between border and contents.

- **border**  
  - Shorthand attribute:
    - `border-width`, `border-style`, `border-color`
    - Can be set in one line.
    - Order is not important.

- **margin**: space outside the box  
  - If you use `auto` in margin size, it keeps the element centered (when used consistently).
  - **Shorthand:**
    - 4 values → top, right, bottom, left (clockwise)
    - 3 values → top, right & left, bottom
    - 2 values → top & bottom, right & left

**box-sizing: border-box**
- Use with `* { box-sizing: border-box; }`
  - Sets all elements' size based on border-box model.

### Outer display type

- Always creates a new row.
- Can use `width` and `height` properties.
- Pushes other boxes using `padding`, `margin`, and `border`.
- If `width` is not used, it takes full page width.

#### Inline-block

- Does not break to a new row: inserted within content on the same line.
- Inherits width from parent.
- Can set various properties.

#### none

- Not shown on the page and does not take up any space.
  - Used for hiding elements.
- Different from `visibility: hidden`.

## CSS Position

- Controls webpage layout by adjusting the location of components.
- Removes elements from normal flow.

**components**
- static

- relative
  - move to setting from original location left-upside dot
  - keep before location space

- absolute
  - remove location space
  - and move to setting from whole page left-upside dot
  - If parent have relative feature
    - absolute have criteria on parent
    - If use just relative, than remain original location space

- fixed
  - fixed position even move by scoll

- Sticky
  - Have own location but when page scrolled, element sticky setting position
  - If all category passing, than sticky elements go to upside

### Z-index
- default is auto 



**position: relative in class**
    .container {
      position: relative;}
- standard setting on container


## CSS Flex Box: inner displat type
- horizon line is main axis
  - vertical line is cross axis

**components**
- main axis start on up side
- cross axis  start on left side

**flex container attribute**
flex-wrap: wrap;
- keep contents in container

justify-content: center;
- align by flex direction

align-items: flex-start;
- align by cross direction