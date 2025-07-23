# Web  
**A service that enables interaction with users**

## Website  
**A space that consists of multiple web pages**

### Components of a Web Page  
- **HTML**  
  - Provides structure
 
- **CSS**  
  - Handles styling

- **JavaScript**  
  - Adds behavior and interactivity

## HTML

 - Hyper Text Markup Language
    - Hypertext: Connext another page
    - Markup Language: Write structure with tag
    - Write lower word
    - most cast attribute values warp by ""

### Structure
<!DOCTYPE HTML> # Indicate this document is write by html
<html></html>   # Include contents of whole page
<HEAD></HEAD>   #
<BODY></BODY>   #
- Closing tag use with '/' + opening tag

**[! + tap] can make html based code directly in vscode**

### HTML Attributes
- The value to adjust element's movement
- Setting element for match user's demand

**Writing norms**
- There is vacancy between name of attribute and attribute
- There is vancancy between attributes
- 
### Text structure
- Supplt text structure and meaning
  - Purpose of <h1> tag is indicate this text is top hieracy text

## CSS
**Cascading Style Sheet**
- Language of consist web design
- example
  - h1 {color:red; font-sizeL 30px;}
    - It seems like  dictionary
    - 'h1' is selector. Important thing is to designat

**How to use External style sheets**
- Create new file and write css core in it

#### CSS Selectors
- Basic selectors
  - * #_all
  - tag # element
  - . # class
  - '#' # tag id
  - attr # attribute

- Combinators
  - " " #space Descendant Combinators
  - "<" # child combinators

- Class selectors
  - "." #dot, all element in that class # ex: .animal
  **See 04-css-selectors**

  ## Specificity (명시도)
  - Cascade : stair style
    - Finally admit code is last code if have same speicficity

  - Specificity hieracy
    1. **!important**
      - extremely
    2. Inline style
      - write in inner directly
      - **Breaks specificity flow — generally discouraged**
    3. **Selectors**
      **id > class > elements**
      - Later rules in the source code override earlier ones with equal specificity
       - It is mean cascade

  ## CSS Box Model
  - Every element have box shape area
  - Outer display type
    - Block
    - inline
    - It is normal flow

  - Inner display type