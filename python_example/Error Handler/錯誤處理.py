class A:
    a_dict = {}

    def __getitem__(self, key):
        try:
            output = self.a_dict[key]
        except KeyError:
            output = key
            
        return output

a = A()
print(a["empty"])