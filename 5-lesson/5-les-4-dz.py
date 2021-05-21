with open('file_to_4_dz.txt', 'r') as f:
    content = f.read()
    print(f'{content}')

with open('file_to_4_new_dz.txt', 'w') as f:
    content = content.replace('One', 'Один')
    content = content.replace('Two', 'Два')
    content = content.replace('Three', 'Три')
    content = content.replace('Four', 'Четыре')
    f.writelines(content)