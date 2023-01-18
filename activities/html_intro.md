# Introduction to HTML

## HTML tag basics

The basic tag structure is `<start_tag> some content </end_tag>`. This set of opening tag + content + closing tag is referred to as an HTML element.

A small number of elements only have an opening tag e.g. `<img>`, `<br>`, `<hr>`. There is a list of these [void elements here](https://developer.mozilla.org/en-US/docs/Glossary/Void_element).

Elements can also have attributes that give additional information. In this course you will mostly use id e.g. `id="some-name"` and class e.g. `class="some-class"`. `id` is used to locate a particular element on a webpage, and `class` is used in adding styles to elements (more on these in later sections).

## Basic HTML page structure and tags

HTML documents start with a document type declaration `<!DOCTYPE html>`. This is required at the start of the document.

The HTML document itself begins with `<html>` and ends with `</html>`

The part that is mostly not visible in the final webpage is between `<head>` and `</head>`. This is typically meta data,
i.e. info about the page.

The part of the HTML document that is visible in the browser is between `<body>` and `</body>`.

The page structure looks like the following (also
see [/html_css_intro/html_intro_basic_structure.html](/html_css/html_intro_basic_structure.html)):

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>COMP0034 Introduction to HTML - Basic page structure</title>
</head>
<body>
<p>Here is some text on a page.</p>
</body>
</html>
```

## Displaying an HTML file in a browser

You can typically see the HTML for a page in a browser by right-clicking on a web page, and selecting ‘View Page
Source’ (or similar, varies by browser).

You can view an html file on your computer in a browser by simply opening it from within a browser.

In your IDE there may be a 'run' (PyCharm) or 'preview' (VSCode) function that will let you view the generated page. How this is done varies by IDE. Read the documentation for your IDE.

## Some commonly used HTML tags

These are in the file [/html_css_intro/html_intro.html](/html_css_intro/html_intro.html)

```html
<!-- comment: Comments are not displayed by the browser -->
<p>This is a paragraph.</p>
<h1>Heading 1</h1>
<h2>Heading 2</h2>
<h3>Heading 3</h3>
<h4>Heading 4</h4>
<h5>Heading 5</h5>
<h6>Heading 6</h6>
<!--An Unordered HTML List-->
<ul>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
</ul>
<!--An Ordered HTML List-->
<ol>
    <li>Coffee</li>
    <li>Tea</li>
    <li>Milk</li>
</ol>
<!--Hyperlink-->
<a href="https://www.ucl.ac.uk">UCL home page</a>
<!--Images: alt="" provides alternative text if the image cannot be displayed or used by screen readers
-->
<img src="/html_css_intro/images/butterfly_thumb.jpg" alt="Butterfly">
<!-- Table -->
<table>
    <tr>
        <th>Company Name</th>
        <th>Contact Person</th>
    </tr>
    <tr>
        <td>Iste</td>
        <td>Maria Anders</td>
    </tr>
</table>
<!-- Horizontal rule -->
<p>The &lt;hr&gt; tag defines a thematic break in an HTML page (e.g. a shift of topic).</p>
<p>It is used to separate content (or define a change) in an HTML page.</p>
<!-- Line break -->
<p>To break lines<br>in a text,<br>use the br element.</p>
<!-- The <form> element defines a form that is used to collect user input e.g.
<form name= ”signup” action="/signup.php" method="get">
The default method when submitting form data is GET, POST should be used for personal/sensitive information or data larger than ~3000 characters
-->
<form action="/action_page.php" method="post">
    <label for="firstname">First name:</label><br>
    <input type="text" id="firstname" name="firstname" value="Mickey"><br>
    <label for="lastname">Last name:</label> <br>
    <input type="text" name="lastname" value="Mouse"><br>
    <input type="submit" value="Submit">
</form>
<p>The input element can be displayed in several ways depending on the type attribute.</p>
<p>Other element types: radio, select, textarea, button, datalist, output.</p>
<p>Each input field must have a name attribute to be submitted.</p>
<p>Div</p>
<p>Used to divide content into block-level sections.
    The 'div' element is often used as a container for other HTML elements to style them with CSS or to perform certain
    tasks with JavaScript.
</p>
<div style="border: 1px solid black">Hello World</div>
<p>The DIV element is a block element, and will always start on a new line and take up the full width available
    (stretches out to the left and right as far as it can).</p>
<!-- Span -->
<p>Used to divide content in-inline. Unlike block-level elements, an inline element does not start on a new line and
    only takes up as much width as necessary.</p>
<p>This is an inline span <span style="border: 1px solid black">Hello World</span> element inside a paragraph.</p>
```

## HTML 5 layout

HTML5 offers semantic elements to define different parts of a web page. You do not have to use these.

<img src="../html_css/images/html5layout.png" alt="HTML 5 layout" width="30%">

`<header>` Defines a header for a document or a section

`<nav>` Defines a container for navigation links

`<section>` Defines a section in a document

`<article>` Defines an independent self-contained article

`<aside>` Defines content aside from the content (like a sidebar)

`<footer>` Defines a footer for a document or a section

## HTML references and tutorials

- [W3Schools](https://www.w3schools.com/tags/default.asp)
- [Mozilla HTML reference](https://developer.mozilla.org/en-US/docs/Web/HTML/Element)
- [Freecodecamp responsive web design (includes CSS & HTML)](https://www.freecodecamp.org/learn/2022/responsive-web-design) This is an interactive tutorial where you code online.
- [Mozilla learn HTML](https://developer.mozilla.org/en-US/docs/Learn/HTML)
