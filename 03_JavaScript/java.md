# JavaScript & DOM

---

## JavaScript

* A programming language based on **ECMAScript**

* Runs in browsers or environments like **Node.js**

* **ECMAScript** is the standard for JavaScript

* **TypeScript**

  * A stricter version of JavaScript with static typing
  * Useful for large-scale applications

---

### Variables

* **Variable Naming**

  * Must start with a letter, `$`, or `_`

* **Declaration Keywords**

  * `let`

    * Block-scoped
    * Reassignable
    * Not re-declarable in the same scope

  * `const` *(commonly used)*

    * Block-scoped
    * Not reassignable
    * Not re-declarable

> **Block Scope**:
> Variables declared inside `{}` cannot be accessed from outside.

---

### Data Types

#### Primitive Types (Immutable)

* `Number`, `String`, `Boolean`, `null`, `undefined`

  * `Number`: no distinction between int/float
  * `String`: supports `*`, `+`, and **template literals** `` `Hello ${name}` ``
  * `Boolean`: `true`, `false`
  * `undefined`: default when a variable is declared but not assigned
  * `null`: intentionally empty → but `typeof null` returns `'object'` → **JavaScript bug**

> `==` → compares after type coercion
> `===` → compares value and type (strict equality)

Logical operators:

* `&&` → AND
* `||` → OR
* `!` → NOT

---

#### Reference Types (Mutable)

* `Object`, `Array`, `Function`

  * Stored by reference
  * Changes affect all references to the same object

---

### Ternary Operator

```js
condition ? valueIfTrue : valueIfFalse
```

---

### Loops

* `while (condition) {}`

* `for (init; condition; step) {}`

* `for...in` → iterates over **keys** in an object

* `for...of` → iterates over **values** of an iterable (like arrays)

---

## DOM (Document Object Model)

* JavaScript interface for interacting with HTML
* Represents HTML as a **tree structure**

---

### DOM Selection

* `document.querySelector()`

  * Selects **first** matching element

* `document.querySelectorAll()`

  * Selects **all** matching elements (returns a **NodeList**)

---

### DOM Manipulation

#### Attributes & Content

* `getAttribute()`, `setAttribute()`, `removeAttribute()`
* `element.textContent`, `element.innerHTML`, etc.

#### Class Manipulation

* `element.classList.add()`
* `element.classList.remove()`
* `element.classList.toggle()`

#### Element Control

* `document.createElement()`
* `parent.appendChild(child)`
* `parent.removeChild(child)`

---

## Functions

```js
function name(param) {
  return value;
}
```

* If no `return`, result is `undefined`

* **Function Declaration**

  ```js
  function sayHello() {}
  ```

* **Function Expression** *(recommended)*

  ```js
  const sayHello = function () {}
  ```

* **Arrow Function Expression**

  ```js
  const greet = (name) => `Hello, ${name}`;
  ```

* Parameters default to `undefined` if not provided

---

## Events

* Any user action or browser signal (click, input, etc.)
* Events are objects created when something happens in the DOM

#### Event Handling

* Use `.addEventListener(type, handler)`

  * Attaches a handler function to an element
  * Example:

    ```js
    button.addEventListener("click", () => {
      alert("Clicked!");
    });
    ```

> **Note**: `addEventListener` is a **method**, not a function

---

### Bubbling & Capturing

* **Bubbling**: event propagates **upward** from the target
  → allows parent elements to react to child events
* **Capturing**: event propagates **downward** (less commonly used)

#### `preventDefault()`

* Prevents the default behavior (e.g., prevent form submission)
