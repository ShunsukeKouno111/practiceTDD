class TestCase:
    def __init__(self,name):
        self.name = name
    def run(self):
        method = getattr(self,self.name)
        method()

class WasRun(TestCase):
    def __init__(self,name):
        self.wasRun = False
        super().__init__(name)
    def testMethod(self):
        self.wasRun = True



test = WasRun("testMethod")
print('Did the test run?:' + str(test.wasRun))
test.run()
print('Did the test run?:' + str(test.wasRun))

