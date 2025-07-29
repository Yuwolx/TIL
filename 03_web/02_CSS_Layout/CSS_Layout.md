
# CSS Layout

---

## CSS Box Model

### Components

* **Content**

  * The actual content of the element
  * You can control the width using the `width` property.

* **Padding**

  * The space between the content and the border.

* **Border**

  * A line around the padding
  * Can be set with shorthand:

    ```css
    border: 1px solid black;
    ```

    * Combines `border-width`, `border-style`, and `border-color`
    * Order doesn't matter

* **Margin**

  * The space outside the element
  * If you set `margin: auto`, the element will be centered horizontally (if width is set)

  **Shorthand Rules:**

  * 4 values: `top right bottom left` (clockwise)
  * 3 values: `top right/left bottom`
  * 2 values: `top/bottom right/left`

---

### `box-sizing: border-box`

```css
* {
  box-sizing: border-box;
}
```

* Makes `width` and `height` include `padding` and `border`
* Prevents unexpected sizing issues

---

### Outer Display Types

* **Block** (default for `div`, `p`, etc.)

  * Takes up full width
  * Starts on a new line
  * Affected by `width`, `height`, `margin`, `padding`, `border`
  * If `width` is not set, fills the parent container width

* **Inline-block**

  * Flows with text, like `inline`
  * But allows setting width/height like `block`
  * Good for placing small boxes side by side

* **none**

  * Completely hides the element (as if it doesn’t exist in layout)
  * **Different from** `visibility: hidden`, which hides the element but keeps its space

---

## CSS Positioning

Used to control the position of elements outside the normal flow.

### Types

* **static** (default)

  * Follows normal document flow

* **relative**

  * Moves element from its **original position**
  * Still **reserves** the original space
  * Offsets using `top`, `left`, `right`, `bottom` from original location

* **absolute**

  * Removed from normal flow (does **not** reserve space)
  * Positioned from the **nearest positioned ancestor** (if any), otherwise from the `html` root
  * Common pattern:

    ```css
    .parent { position: relative; }
    .child { position: absolute; top: 0; left: 0; }
    ```

* **fixed**

  * Always stays in the same position even when scrolling
  * Positioned relative to the browser window

* **sticky**

  * Behaves like `relative` until a scroll threshold is reached, then becomes `fixed`
  * Requires top/left/right/bottom to activate

### `z-index`

* Controls the stacking order
* Higher value appears on top
* Default is `auto`

```css
.container {
  position: relative;  /* makes it a reference for absolute children */
}
```

---

## CSS Flexbox (inner display type)

**Used to align child elements inside a container.**

### Axes

* **Main axis**: horizontal by default (`row`)
* **Cross axis**: perpendicular to main axis (vertical by default)

---

### Flex Container Properties

```css
display: flex;
flex-wrap: wrap;
justify-content: center;
align-items: flex-start;
```

* `flex-wrap: wrap`
  → allows child items to wrap onto multiple lines

* `justify-content`
  → aligns items along the **main axis**

  * `center`, `space-between`, `flex-end`, etc.

* `align-items`
  → aligns items along the **cross axis**

  * `flex-start`, `center`, `stretch`, etc.

---

### Notes

* Flex properties only affect **direct children** of the flex container
* For precise layout control, combine `flex` with `margin`, `padding`, and `gap`
