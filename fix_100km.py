with open('build_standalone.py', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("with open('index.html', 'w', encoding='utf-8') as f:\n        f.write(html_content)", "")
content = content.replace("print('Writing index.html...')", "")
content = content.replace("Successfully generated index.html, Ultra100_standalone.html", "Successfully generated Ultra100_standalone.html")

with open('build_standalone.py', 'w', encoding='utf-8') as f:
    f.write(content)
