categories = []
tempdict = []
sitesin = []
sitesout = []
mysection = False
#with open ('localdatabaseclean.txt', 'a') as localdbout:
with open ('localdatabase.txt', 'r') as localdb:
	for category in localdb:
		if 'define category' in category:
			category=category.rstrip()
			category=category[16:]
			categories.append(category)
			category=""
			#print(localdb)
with open ('localdatabase.txt', 'r') as localdb:
	for section in categories:
		print(section)
		for line in localdb:
			#print(line)
			#print(localdb)
			if line[0] == ';':
				continue
			elif 'define category ' + section in line:
				mysection = True
			elif 'end category ' + section in line:
				mysection = False
			elif mysection:
				line = line.strip()
				sitesin.append(line)
				print(sitesin)
		with open ('localdatabaseclean.txt', 'a') as localdbout:
			localdbout.write('define category ' + section + "\n" )
			for site in sitesin:
				localdbout.write(site + "\n")
			localdbout.write('end category ' + section + "\n\n")

