print("Training model...")

for i in range(1,11):
    print("Training %s%%"%(i*10))

print("Training done!!")

open("model.file", "w").write("Hello World")
open("/valohai/outputs/model.file", "w").write("Hello World")
