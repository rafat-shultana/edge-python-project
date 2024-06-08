global_variable=0
def change_global_variable():
    global global_variable

    global_variable += 1
    print(f'''
          we are accessing a global variable valu inside our function.
          value has increased to {global_variable}
          ''')
change_global_variable()