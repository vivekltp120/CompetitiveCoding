
def similarity(d1,d2):
    sim=0
    inter=d1.intersection(d2)
    uni=d1.union(d2)
    if len(uni)>0:
     sim = float(len(inter)/len(uni))

    return sim
def printdocs():
    pass
    



if __name__=="__main__":
   # n=int(input())
   mydic={'13':{14,15,100,9,3}, '16':{32,1,9,3,5},'19':{15,29,2,6,8,7},'24':{7,10}}
   sim=0
   visit=set()
   for doc1,content1 in mydic.items():
       for doc2, content2 in mydic.items():
           if doc1!=doc2:
             if (doc1,doc2) in visit or  (doc2,doc1) in visit:
                 continue
             else:
                 sim=similarity(content1,content2)
                 if sim!=0:
                  print('{0},{1} {2}'.format(doc1,doc2,sim))
                  visit.add((doc1,doc2))
