import os
def new_hw_setting():
    day, b, c = tuple(input('일 hw문제수 ws문제수 : ').split(' '))
    day, b, c = int(day), int(b), int(c)

    if day < 10:
        dir_name = f'0{day}'
    else:
        dir_name = f'{day}'

    os.system(f'mkdir {dir_name}')
    os.system(f'touch {dir_name}_homework.md')
    with open(f'{dir_name}_homework.md','w',encoding='utf-8') as f:
        f.write(f'# {dir_name}_homework\n')
        for i in range(1, b+1):
            if i<10:
                f.write(f'## 0{i}문제\n')
            else:
                f.write(f'## {i}문제\n')
            f.write(f'```python \n ```\n')
            
    os.system(f'mv {dir_name}_homework.md {dir_name}/{dir_name}_homework.md')
    
    
    os.system(f'touch {dir_name}_workshop.md')
    with open(f'{dir_name}_workshop.md','w',encoding='utf-8') as f:
        f.write(f'# {dir_name}_workshop\n')
        for i in range(1, b+1):
            if i<10:
                f.write(f'## 0{i}문제\n')
            else:
                f.write(f'## {i}문제\n')
            f.write(f'```python \n ```\n')
                
    os.system(f'mv {dir_name}_workshop.md {dir_name}/{dir_name}_workshop.md')