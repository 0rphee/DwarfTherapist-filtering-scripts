stringy = ""

for n in range(83):
    stringy += (f"((d.labor_enabled({n}) && d.labor_rating({n}) < 5) || d.labor_enabled({n}) == false) &&")

#print(stringy)


sec_str = ""

for n in range(84):
    sec_str +=(f"(d.labor_enabled({n}) && d.labor_rating({n}) > 8) ||")

print(sec_str)
