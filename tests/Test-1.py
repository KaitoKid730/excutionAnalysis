import excutionAnalysis

# ---------------------------

x = excutionAnalysis()
x.addProcess('Process1')
x.executionStarts('Process1')
d = ""
for s in range(500000):
	d += "3"
x.executionEnds('Process1')

# ---------------------------

x.addProcess('Process2')
x.executionStarts('Process2')
d = ""
for s in range(50000):
	d += "3"
x.executionEnds('Process2')

# ---------------------------

x.analyzeData()   # Very important
print(x)
