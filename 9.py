def pair(lst,t):        
    
    res = []#λίστα αποτελεσμάτων
    for ele in lst:
        if ele[0] + ele[1] == t: 
            res.append(ele)
pair([(45, 5), (2, 74), (3, 6), (12, 2), (1, 8)],9)

