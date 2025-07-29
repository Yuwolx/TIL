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

