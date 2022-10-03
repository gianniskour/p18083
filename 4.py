def FileWiki(fl,url):
	all_freq = {}
	max1 = 0
	max2 = 0
    results = 0
	with open(fl) as f:
		test_str = f.read()
	for i in test_str:
		  if i in all_freq:
		  	  all_freq[i] += 1
		  else:
		  	  all_freq[i] = 1
	for i in all_freq:
		if int(all_freq[i]) > int(max1): 
			print(i)
			max1 = all_freq[i] 
			char1 = str(i)
		elif int(all_freq[i]) > int(max2):  
			max2 = all_freq[i] 
			char2 = str(i)
	for i in range(len(url):
		if(i+1 <len(url)):
			if(url[i] == char1 && url[i+1] == char2) : 	results	 = results + 1
	
 
	

FileWiki("Άσκηση 4_file.txt","https://gunet2.cs.unipi.gr")
