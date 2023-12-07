class Tag:
    count = 0
    def __init__(self, name="nanana", height=160):
        self.name=name
        self.height = height
        Tag.count += 1
    def __str__(self):
        print(f"===== {self.name}.\n===== {self.height}")

    def __del__(self):
        print("eee12233e")

print(Tag.count)
morgen = Tag("sssss", 190)
print(Tag)
#morgen = Tag()
#abend = Tag(height=33)
#nacht = Tag(height=11)
#print(morgen.height)
#print(abend.height)
#print(nacht.height)
#print(nacht.count)
