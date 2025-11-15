string="masala chai"
slice_string=string[7:]
print(slice_string)  # it will print "chai"
upper_string=string.upper()
print(upper_string)  # it will print "MASALA CHAI"

cap_string=string.capitalize()
print(cap_string)  # it will print "Masala chai"
#[start:end:step or updation] end is excluded

rev_string=string[::-1]
print(rev_string)  # it will print "iahc alasam"

user="    mama ji     "
print(user)
strip_user=user.strip()
print(strip_user)  # it will print "mama ji" without leading and trailing spaces

replace_string=string.replace("masala","ginger")
print(replace_string)  # it will print "ginger chai"

chai="masala chai, masala chai, masala chai"
split_string=chai.split(", ")
print(split_string)  # it will print ['masala chai', 'masala chai', 'masala chai']

find_string=string.find("chai")
print(find_string)  # it will print 7 because 'chai' starts at index 7

chai_count=chai.count("chai")
print(chai_count)  # it will print 3 because 'chai' occurs 3 times in the string

join_string="-".join(["masala","chai","is","great"])
print(join_string)  # it will print "masala-chai-is-great"

raw_string=r"C:\newfolder\testfile.txt"
print(raw_string)  # it will print C:\newfolder\testfile.txt without interpreting escape sequences

