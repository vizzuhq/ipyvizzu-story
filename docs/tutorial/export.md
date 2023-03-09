# Export

You can export your story to an html file, just place the following code after
your story

```python
story.export_to_html(filename="mystory.html")
```

or you can get the html story as a string with the following code.

```python
html = story.to_html()
print(html)
```
