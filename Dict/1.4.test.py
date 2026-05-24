### Test 1
test = { 600: 1000, 300: 200}

def print_test( arg ):
    test = { key:  value for key, value in sorted(arg.items()) }
    
    print(test)
    
print_test( test )


### Test 2
dash_apps_ = {
    '/simple_app': ('value1', 'item1'),
    '/population': ('value2', 'item2')
}

for url in dash_apps_:
    # print
    print( dash_apps_[url][0] )
