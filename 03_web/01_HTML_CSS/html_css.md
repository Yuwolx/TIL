

# Web

**A service that enables interaction with users**

---

## Website

**A collection of multiple connected web pages**

---

### Components of a Web Page

* **HTML**

  * Provides the structure of the page

* **CSS**

  * Handles design and styling

* **JavaScript**

  * Adds behavior and interactivity

---

## HTML (HyperText Markup Language)

* **HyperText**: Connects to other web pages
* **Markup Language**: Describes the structure using tags
* Use lowercase for tag names
* Attribute values are usually wrapped in double quotes (`"`)

> HTML handles everything from images to text layout

---

### Basic Structure

```html
<!DOCTYPE html>     <!-- Declares this document is HTML -->
<html></html>       <!-- Root element -->
<head></head>       <!-- Metadata, title, links -->
<body></body>       <!-- Page content -->
```

* Closing tags use `/` before the tag name
* In VSCode, typing `!` + `Tab` generates a full HTML template

---

### HTML Attributes

* Attributes modify or provide additional info about elements
* Used to adjust behavior or appearance for user needs

**Writing rules:**

* Space between tag name and attributes
* Space between multiple attributes

  ```html
  <img src="..." alt="..." />
  ```

---

### Text Structure

* Tags like `<h1>` to `<h6>` provide semantic hierarchy

  * `<h1>` means top-level heading

**Unit tip**:

* `rem`: relative to the root font size
  → e.g., `1.5rem` = 1.5 × root font size

---

## CSS (Cascading Style Sheets)

* Language used for designing web pages
* Example:

```css
h1 {
  color: red;
  font-size: 30px;
}
```

* Feels similar to dictionaries
* `h1` is a **selector** (targets the element to style)

---

### How to Use External CSS

* Create a separate `.css` file and link it with `<link>` in the `<head>`
* Recommended for maintainability

---

### CSS Selectors

**Basic Selectors:**

* `*` → all elements
* `tag` → element selector
* `.class` → class selector
* `#id` → ID selector
* `[attr]` → attribute selector

**Combinators:**

* `" "` → descendant
* `>` → direct child

> `.animal` matches all elements with class="animal"
> (See: `04-css-selectors` for examples)

---

### Specificity (명시도)

**Cascade = CSS decision flow**

Priority Order (Higher wins):

1. `!important`

   * Highest, avoid using unless necessary
2. Inline styles

   * Written directly in elements (`style="..."`) — not recommended
3. Selector-based

   * `id` > `class` > `tag`
   * If specificity is equal, the later rule overrides earlier ones

---

### CSS Box Model

* Every element is rendered as a rectangular box
* Affects layout and spacing

**Outer Display Types:**

* `block` → takes full width, starts on new line
* `inline` → flows with text, only takes as much space as needed
  → This is called **normal flow**
