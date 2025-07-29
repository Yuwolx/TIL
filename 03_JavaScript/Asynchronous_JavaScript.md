# Asynchronous JavaScript (and Objects & Arrays)

---

## Object

> **An object is a collection of key-value pairs.**

### Structure

* Defined using `{}`

  ```js
  const user = {
    name: "Alice",
    age: 25
  };
  ```
* **Keys** must be strings (or will be coerced to strings)

  * Can use quotes if key has spaces: `"full name": "Tom"`
  * Values can be any data type

---

### Object Features

#### 1. Shorthand Property

If key and variable name are the same, you can omit one:

```js
const email = "a@a.com";
const user = { email };  // same as { email: email }
```

#### 2. Destructuring Assignment

Extract values from an object:

```js
const user = { name: "John", age: 30 };
const { name, age } = user;
```

#### 3. Methods (함수 속성)

```js
const user = {
  greet: function () {
    return "Hello";
  }
};
```

#### 4. `this` Keyword

* In a **method**, `this` refers to the **object that calls it**:

  ```js
  const user = {
    name: "Amy",
    sayHi() {
      console.log(this.name);
    }
  };
  user.sayHi(); // "Amy"
  ```

* In a **regular function**, `this` refers to `window` (or `undefined` in strict mode).

---

### Spread Syntax (전개 구문)

Used to **copy** or **merge** objects:

```js
const user = { name: "Tom" };
const copy = { ...user };
```

---

### Optional Chaining (`?.`)

Access nested properties **safely**:

```js
user?.address?.street  // won't throw error if address is undefined
```

---

## JSON (JavaScript Object Notation)

* A data format used for storing and exchanging data
* Similar to JS object, but:

  * All keys must be in **double quotes**
  * No functions allowed

```json
{
  "name": "Jane",
  "age": 25
}
```

* Use `JSON.stringify()` to convert JS → JSON
* Use `JSON.parse()` to convert JSON → JS

---

## Array

> Arrays are special objects used to store **ordered** collections.

```js
const arr = [1, 2, 3];
```

* `typeof arr` → `"object"`
* Use `for...of` to loop **by value**
* Use `for...in` to loop **by index** (not recommended for arrays)

---

### Array Helper Methods

#### `forEach()`

* Executes a function for each element (no return)

```js
arr.forEach(el => console.log(el));
```

#### `map()`

* Transforms each element and returns a **new array**

```js
const names = users.map(user => user.name);
```

#### `filter()`

* Returns a new array of elements that match a condition

```js
const adults = users.filter(user => user.age >= 18);
```

#### `find()`

* Returns the **first element** that matches a condition

```js
const admin = users.find(user => user.role === 'admin');
```

#### `some()` / `every()`

* `some`: returns `true` if **any** element passes the test
* `every`: returns `true` if **all** elements pass the test

---

**JS arr cannot use negetive indexing [-1]**


# Asynchronous JavaScript

---

## Synchronous vs Asynchronous

* **Synchronous**:

  * Code runs **in order**, line by line
  * Each step **waits** for the previous one to finish

* **Asynchronous**:

  * Multiple operations can **run in parallel** (non-blocking)
  * Execution continues while waiting for other tasks (e.g., network) to finish
  * Common tools: `callback`, `Promise`, `async/await`

> JavaScript is **single-threaded**, so it relies on browser features to handle asynchronous behavior

---

## How JavaScript Handles Async

JavaScript in browsers is powered by:

* **Call Stack**: the place where functions are executed
* **Web APIs**: provided by the browser to handle async tasks (e.g., `setTimeout`, `fetch`, `DOM events`)
* **Callback Queue**: where callback functions wait
* **Event Loop**: monitors the stack and pushes callbacks when the stack is clear

---

## AJAX (Asynchronous JavaScript and XML)

> Enables asynchronous HTTP requests without refreshing the whole page

* Originally used XML, but now **JSON is the standard**
* Allows partial page updates (e.g., updating only one section of a page)

---

### XMLHttpRequest (XHR)

```js
const xhr = new XMLHttpRequest();
xhr.open("GET", "url");
xhr.onload = function () {
  console.log(xhr.response);
};
xhr.send();
```

* Older way to make HTTP requests
* Can get messy with nested callbacks (callback hell)

---

## Asynchronous Callback

* Execution is **based on when the task completes**, not the order written
* Often leads to deeply nested code if not managed properly
  → Known as **callback hell**

---

## Promise

> Provides a cleaner way to handle asynchronous operations

```js
fetch(url)
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error(error));
```

* `.then()` handles **success**
* `.catch()` handles **errors**

### Promise States:

* `pending` → waiting
* `fulfilled` → success
* `rejected` → failure

---

## Axios

> A popular **Promise-based** HTTP client

### Why use Axios?

* Simpler syntax than XHR
* Automatically parses JSON
* Better error handling

### Usage (via CDN):

```html
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
```

### Example:

```js
axios.get("https://api.example.com/data")
  .then(response => console.log(response.data))
  .catch(error => console.error(error));
```

---

## (Coming Next) — `async` / `await` (Preview)

```js
async function fetchData() {
  try {
    const res = await axios.get("/data");
    console.log(res.data);
  } catch (e) {
    console.error(e);
  }
}
```

* Cleaner syntax than `.then()`
* Uses `try...catch` for error handling
* Still based on **Promise**

