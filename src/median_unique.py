def mymed(lst):
    if len(lst) < 1:
            return None
    if len(lst) %2 == 1:
            return lst[((len(lst)+1)/2)-1]
    else:
            return float(sum(lst[(len(lst)/2)-1:(len(lst)/2)+1]))/2.0
ipfile=open("tweet_input/tweets.txt","r+")
opfile=open("tweet_output/ft2.txt","w")
uniquewordcounts=[]
for line in ipfile:
    wordcount={}
    unique = 0
    median = 0
    words = line.split()
    for word in words:
	if word not in wordcount:
		wordcount[word] = 1
		unique += 1
	else:
		wordcount[word] += 1
	#	unique -= 1
    uniquewordcounts.append(unique)
    median = mymed(uniquewordcounts)
    print median
    opfile.write("{0}{1}".format(median,'\n'))
ipfile.close()
opfile.close()    
