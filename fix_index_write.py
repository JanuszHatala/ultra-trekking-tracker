def remove_index_write():
    filename = 'build_standalone_75km.py'
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    target = "with open('index.html', 'w', encoding='utf-8') as f:\n    f.write(html_template)\n"
    content = content.replace(target, '')
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done")

remove_index_write()
