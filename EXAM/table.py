d = [["Mark", 12, 95, "ysv", 45, False, "Helsu" ],
     ["Jay", 11, 88, "ysv", 45, False, "Helsu" ],
     ["Jack", 14, 90, "ysv", 45, False, "Helsu" ]]
     
print ("{:<8} {:<15} {:<10}".format('Name','Age','Percent','Province','Town', 'Status', 'Husble'))

for v in d:
    name, age, perc,prov, town, state, husble = v
    print ("{:<10} {:<10} {:<10} {:<10} {:<10} {:<10} {:<10}".format( name, age, perc, prov, town, state, husble))