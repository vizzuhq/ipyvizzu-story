# Export

You can export your `Story` into an `HTML` file, by calling the `export_to_html`
method. The data, the `Story` and the navigation buttons will all be included in
the generated `HTML` file.

```python
story.export_to_html(filename="mystory.html")
```

You can also get the raw `HTML` string using the following code.

```python
html = story.to_html()
print(html)
```
