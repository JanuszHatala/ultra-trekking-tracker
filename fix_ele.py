import re

for filename in ['build_standalone.py', 'build_standalone_75km.py']:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Fix regex
    content = content.replace(r"cp.ele.match(/\+?(\d+)m/)", r"cp.ele.match(/\+?\s*(\d+)\s*m/)")
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
