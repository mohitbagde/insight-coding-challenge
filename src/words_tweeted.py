ipfile=open("tweet_input/tweets.txt","r+")
opfile=open("tweet_output/ft1.txt", "w")
#opfile = os.path.join(os.path.dirname(__file__), '/tweet_output/relative/path/to/file/you/want')
wordcount={}
for word in ipfile.read().split():
    if word not in wordcount:
        wordcount[word] = 1
    else:
        wordcount[word] += 1
for k,v in sorted(wordcount.items()):
    print('{:25s} {:6}'.format(k,v))
    opfile.write('{:25s} {:6}'.format(k,v)+'\n')
ipfile.close()
opfile.close()
