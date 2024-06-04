def remove_duplicates(data_list):
  no_dupes = []
  for i in range(len(data_list)):
    if data_list[i] not in no_dupes:
      no_dupes.append(data_list[i])
  return no_dupes
user_list = []
while True:
  element = input("Enter an element (or press Enter to finish): ")
  if not element:
    break
  user_list.append(element)

unique_list = remove_duplicates(user_list)
print("Unique elements:", unique_list)

print(" program created by : Ayush Tiwari . \n Course=Bca. \n section=F1. \n semester = 4. \n Rollno = 25.")