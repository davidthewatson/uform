from uform import UForm

print(dir(UForm))
Cats = UForm.add_derivative('cats')

for c in [{'name': 'Keiko', 'age': 7},
          {'name': 'Goose', 'age': 13},
          {'name': 'Maxwell', 'age': 11}]:
    Cats.store(**c)

cats = Cats.select().execute()
for cat in cats:
    print(cat.attrs)
