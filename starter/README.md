##### Quick note: This is not a regular readme. This .md file is meant to be used as a quick ref to look back on the topics covered during this units project. 

# Unit 1 Notes

<br>


## Table of Contents


- [Unit 1 Notes](#unit-1-notes)
  - [Table of Contents](#table-of-contents)
  - [Decorators](#decorators)
  - [RegEx](#regex)
    - [RegEx functions](#regex-functions)
    - [RegEx Expression Patterns](#regex-expression-patterns)

<br>

---

<br>

## Decorators

Decorators allow you to tack on additional functionality to existing functionality using the @ operator.

Syntax:

    def decorator_func(ori_func):
      # decorator code block which will contain the additional functionality
    
    @decorator_func
    def original_function():
      # original_func code block
    
    [same as]

    decorated_func = decorator_func(original_function)

Basically, what is happening is that the '@' signals that the following function will be passed into the decorator function which will have been defined previously

---

<br>

## RegEx 

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.

The *re* built-in pythong package is used to make this all work

Example

    import re

    txt = "The rain in Spain"
    x = re.search("^The.*Spain$", txt)

### RegEx functions
[link for functions](https://docs.python.org/3/library/re.html#functions)

### RegEx Expression Patterns
[link for expression patterns](https://cheatography.com/davechild/cheat-sheets/regular-expressions/)
