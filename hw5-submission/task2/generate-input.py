from collections import defaultdict

userset = {}
itemset = {}

ratefd = open("myratings.dat","r")
predfd = open("pair_Ratings.dat","r")
newrate = open("newratings.txt","w")

rate = ratefd.readlines()
for r in rate:
    field = r.split()
    if field[0] not in userset:
        userset[field[0]] = len(userset)
    
    if field[1] not in itemset:
        itemset[field[1]] = len(itemset)

    uid = userset[field[0]]
    iid = itemset[field[1]]
    newrate.write("%s\t%s\t%s\n" %(uid, iid, field[2]))
newrate.close()

newpred = open("newpair_Rating.txt", "w")
pred = predfd.readlines()
for r in pred:
    if r.startswith("reviewer"):
        newpred.write(r)
        continue
    field = r.split()
    if field[0] not in userset:
        userset[field[0]] = len(userset)

    if field[1] not in itemset:
        itemset[field[1]] = len(itemset)

    uid = userset[field[0]]
    iid = itemset[field[1]]
    newpred.write("%s\t%s\n" % (uid,iid))

newpred.close()
