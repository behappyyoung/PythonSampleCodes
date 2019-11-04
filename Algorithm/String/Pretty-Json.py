"""
Input 1:
    A = "{A:"B",C:{D:"E",F:{G:"H",I:"J"}}}"
Output 1:
    {
        A:"B",
        C:
        {
            D:"E",
            F:
            {
                G:"H",
                I:"J"
            }
        }
    }

Input 2:
    A = ["foo", {"bar":["baz",null,1.0,2]}]
Output 2:
   [
        "foo",
        {
            "bar":
            [
                "baz",
                null,
                1.0,
                2
            ]
        }
    ]

"""
def pretty_json(json_str):
    tab = '\t'
    tab_times = 0
    c_return = '\n'
    print_str = ''
    for s in json_str:
        if s == '{' or s == '[':
            print_str +=  c_return + tab_times*tab +  s + c_return + (tab_times+1)*tab
            tab_times += 1
        elif s == ',':
            print_str += s + c_return + tab_times*tab
        elif s == '}' or s == ']':
            tab_times -= 1
            print_str += c_return + tab_times * tab + s
        else:
            print_str += s
    return print_str

A = "{A:'B',C:{D:'E',F:{G:'H',I:'J'}}}"
print(pretty_json(A))
A= '{"id":100,"firstName":"Jack","lastName":"Jones","age":12}'
print(pretty_json(A))
A = '["foo", {"bar": ["baz", "null", 1.0, 2]}]'
print(pretty_json(A))
