class A :
    def method(self):
        print("A.mehtod")

class B(A) :
    def method(self):
        print("A.mehtod")

class C(A) :
    def method(self):
        print("A.mehtod")

class D(B, C) :
    def method(self):
        print("D.mehtod")
        super().method()