# Week 1 flipped activities

## Set-up

You may need to alter your IDE (VS Code) to support HTML and CSS. Please check the documentation for your IDE.

- [HTML programming in VS Code](https://code.visualstudio.com/docs/languages/html)
- [HTML support in PyCharm](https://www.jetbrains.com/help/pycharm/editing-html-files.html)

To view HTML pages in a browser from VS Code requires an extension such as [Live Server](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer) to be installed. Once you have installed Live Server, if you right click on an HTML file in VS Code explorer then you can select an option to 'open with Live Server'. This opens the file in a browser.

You will need to a Python environment for the final activity only e.g create and activate a venv. Install pandas and Dash in the environment, e.g. run `pip3 install dash pandas` or `python -m pip3 install dash pandas` in the Terminal in VS Code or PyCharm.

## Activity 1: Create an html document [30 mins]

Read [html_intro.md](/activities/html_intro.md)

For this course, you will not write a lot of HTML. You will need to:

- be able to create a basic HTML document structure with head and body; and understand the purpose of each and what they contain
- understand the general syntax of HTML tags; and know where to find an HTML reference that explains how to use specific tags.

Aim to complete the activities before the lab session if possible, then use the session to ask questions.

By convention the main page of a website is often called  `index.html`.

Create a new html file called `index.html`.

The following code provides a basic html page structure. Add this to `index.html`:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Add page title here</title>
</head>
<body>
<!-- Add the main page elements here -->
</body>
</html>
```

Add the html elements listed below to the body of the html page. Add content to each of the elements (this is not given to you in the code below, you will need to read the reference and then add appropriate content yourself!).

[W3 schools HTML element reference](https://www.w3schools.com/tags/default.asp)

HTML elements to add:

```html
<title></title>
<h1></h1>
<ol>
    <li></li>
</ol>
<p><a href=""></a></p>
<img src="" alt="" height="" width="">
<table>
    <tr>
        <td></td>
    </tr>
</table>
```

## Activity 2: Add CSS styling your html [30 mins]

Read [css_intro.md](/activities/css_intro.md)

For this course you are not expected to write any CSS; further there are no marks in the coursework for writing CSS. You do need to understand what CSS is and how to apply CSS styling to your HTML elements.

This first activity introduces you to using an external stylesheet that you create yourself so you understand the structure and syntax. However, in the coursework you are more likely to use a third party stylesheet, ie an open source stylesheet created by someone else.

Create a stylesheet called `mystyles.css`

Add a link to the stylesheet in the `<head>` section of your html, e.g.

```html

<head>
    <link rel="stylesheet" type="text/css" href="mystyles.css">
</head>
```

Add styling for the html elements you included in your html.

The general syntax is explained here: [W3Schools CSS syntax](https://www.w3schools.com/css/css_syntax.asp)

A reference for the selectors is here: [W3Schools CSS reference](https://www.w3schools.com/cssref/default.asp)

```css
h1 {
    color: plum;
    text-decoration-line: underline;
}

img {
}

ol {
}

li {
}

a {
}

table {
}

tr {
}

th {
}

td {
}
```

## Activity 3: Use bootstrap to make your page follow a responsive design [30 mins]

Read [responsive_intro.md](/activities/responsive_intro.md)

For this course you are encouraged to use a third-party CSS such as Bootstrap. If used correctly, then a web page using Bootstrap should adhere to responsive design principles.

Replace your `mystyles.css` stylesheet with the [Bootstrap styles](https://getbootstrap.com/docs/5.2/getting-started/introduction/).

You will need to add the `<meta>` tag as well as the link to the online version of the stylesheet (or download the stylesheet and save to your folder, this is explained in their getting started documentation).

You also need to wrap your body content in a [container](https://getbootstrap.com/docs/5.2/layout/containers/).

```html
<head>
    <!-- Refer to https://getbootstrap.com/docs/5.2/getting-started/introduction/ -->
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous"> 
</head>
<body>
<div class="container">
  <!-- Content here -->
</div>
</body>

```

What does your page look like now?

To change the style of each of the elements on your page, you should apply specific Bootstrap styles to them also.

For example, remove any height and width tags from your image and instead add [Bootstrap image styling](https://getbootstrap.com/docs/5.2/content/images/) e.g.

```html
<img src="https://upload.wikimedia.org/wikipedia/commons/9/9e/Iris_sanguinea.JPG" alt="Iris" class="img-fluid">
```

Open the page in Live Server and see what happens to the image when you make the browser smaller and larger. Remove the Bootstrap class property to see the non-responsive version of the image.

## Activity 4: Create a basic Dash app with HTML and Bootstrap CSS styling [30 mins]

This activity aims to give you 'just enough' knowledge to get a basic Dash webpage that uses both HTML and Bootstrap CSS. It is adapted from the [Dash tutorial](https://dash.plotly.com/installation).

There are many freely available Dash tutorials; such as:

- [Dash tutorial](https://dash.plotly.com/installation)
- [Dash tutorial, Charming Data](https://www.youtube.com/watch?v=7m0Bq1EGPPg) - this is part of a larger series of video tutorials on Dash. Well worth watching IMHO.
- [Dash tutorial, Real Python](https://realpython.com/python-dash/)
- [Dash tutorial, Datacamp](https://www.datacamp.com/tutorial/learn-build-dash-python)

To complete this activity you will need to have a Python environment in which Dash and pandas has been installed (see setup at the start of this document).

### Basic Dash app with HTML

Create a Python file to launch the Dash app. Do not call it `dash.py` as this conflicts with Flask itself. Most tutorials suggest `app.py`, though you could call it the name of your app, e.g. `hello_world.py`.

Add the following code section.

When the app is run, it will return a page with the HTML paragraph tag with the words 'Hello, World!'.

The sections are explained in the Dash tutorial as follows:

1. The layout is composed of a tree of "components" such as html.Div and dcc.Graph.
2. The Dash HTML Components module (dash.html) has a component for every HTML tag. The html.H1(children='Hello Dash') component generates a `<h1>Hello Dash</h1>` HTML element in your app.
3. Not all components are pure HTML. The Dash Core Components module (dash.dcc) contains higher-level components that are interactive and are generated with JavaScript, HTML, and CSS through the React.js library.
4. Each component is described entirely through keyword attributes. Dash is declarative: you will primarily describe your app through these attributes.
5. The children property is special. By convention, it's always the first attribute which means that you can omit it: html.H1(children='Hello Dash') is the same as html.H1('Hello Dash'). It can contain a string, a number, a single component, or a list of components.

```python
# Import the required packages
from dash import Dash, html

# Creates the Dash app
app = Dash(__name__)

# Creates the HTML page layout and adds it to the app. This uses dash.html package to add HTML components.
app.layout = html.Div(
    # The first element is the html.Div. The 'child' elements of the Div are those elements that are inside the Div. In this case a H1 heading.
    children=[
        # The 'children' of the H1 element in this case is the content to be displayed. You can also ommit the keyword as shown in the P example.
        html.H1(children='Hello, World!'),
        html.P('My first app'),
        ]
)

if __name__ == '__main__':
    app.run_server(debug=True)

```

To run the app in VS Code, go to Terminal, (assuming you are in the same folder as `app.py`) enter `python app.py`.

You should see the server start. If it successfully starts your Dash app, the URL will be shown in the Terminal. You can open this URL in any browser. By default it will be [http://127.0.0.1:8050](http://127.0.0.1:8050)

### Basic Dash app with Bootstrap CSS styling (using dash-bootstrap-components)

For this activity, use the Bootstrap reference in [Dash Bootstrap Components](https://dash-bootstrap-components.opensource.faculty.ai/docs/) for how to add bootstrap to your Dash app and using the Bootstrap components. 

You may also need to refer to the [main Bootstrap documentation](https://getbootstrap.com/docs/5.3/getting-started/introduction/) to identify the classes needed to style other elements.

You first need to install the package: `pip install dash-bootstrap-components`

You can now add the import to your code:

```python
import dash_bootstrap_components as dbc
```

Dash bootstrap CSS (or any CSS) is passed as a parameter to the Dash app when you create it, e.g.:

```python
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
```

Bootstrap requires that you create the layout in a container. You need to change the current Div surrounding the app layout section to a dbc.Comtainer, e.g.:

```python
app.layout = dbc.Container(
    # HTML layout elements here
)
```

To make the layout responsive, Bootstrap expects the viewport to be set in the HTML head. You may have noticed that the layout in Bootstrap only lets you set tags in the page body. To set the head tags you need to pass these as a parameter when you create the dash app. This is [documented here](https://dash-bootstrap-components.opensource.faculty.ai/docs/faq/) and can be applied to your simple app as follows:

```python
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"},
    ],
)
```

When you save the changes, the Dash app automatically tries to restart and apply them. If not, you can stop and then restart the Dash app in VSCode by:

- In Terminal, press the CTRL + C keys together to quit Dash.
- Run the app again as you did before in Terminal e.g. `python app.py`.

To add a specific bootstrap class to an HTML element, you use the `className=` parameter for the element. For example, apply a [display heading bootstrap style](https://getbootstrap.com/docs/5.3/content/typography/#display-headings) to the H1 tag:

```python
app.layout = dbc.Container(
    children=[
        html.H1(children='Hello, World!', className="display-1"),
    ]
)
```

## Directory structure for a Dash app

A directory structure for a Dash app might be:

```
dash_app_name/
  /assets/  # An optional directory that contains CSS stylesheets and images. Dash will automatically serve all of the files that are included in this folder.
      app.css  
  /data/  # An optional directory that contains the data files (unless this is accessed via an API or database server).
      data.csv
  dash_app.py  # Contains your Dash app code and code to run the server. Sometimes named app.py or dashboard.py.
  .gitignore  # The files and folders to be ignored in git.
  requirements.txt  # The app's python dependencies.
  /.venv/   # Python venv with the dependencies installed.

```

This is not the only structure you will see. For example, Dash runs as a single page app, you may however want a multi-page app in which case you would have a sub-folder for each dash app and extract the function to run the server to
a separate file, typically run.py.


## Examples

- [Dash app examples in GitHub](https://github.com/plotly/dash-sample-apps)
- [Dash bootstrap components examples](https://dash-bootstrap-components.opensource.faculty.ai/examples/)