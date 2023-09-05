class Interface:
    def Islem(self):
        return f"Bu bir {self} instancetır."
    
class A(Interface):
    pass

class B(Interface):
    pass

class C(Interface):
    pass

        
print(IslemYapici.IslemYap("a"))