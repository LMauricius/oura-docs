# oura-docs
Documentation for the Oura programming language

# Language documentation
The documentation source and readable pages are part of this repo. The current documentation can be viewed using [Github's htmlpreview](https://htmlpreview.github.io/?https://github.com/LMauricius/oura-docs/blob/main/html/introduction.html)

# Building the html
It can be built by running the `compile.py` script inside the Docs directory.
`pandoc` must be installed as a prerequisite.

```bash
./compile.py ./content ./src ./html ./build "tango"
```