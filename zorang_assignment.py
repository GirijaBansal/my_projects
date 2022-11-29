import requests,math

def dis(var1,var2):
    x1,y1 = var1[0],var1[1]
    x2,y2 = var2[0], var2[1]
    return math.sqrt((x2-x1)**2 + (y2-y1)**2)


p = requests.get("https://zorang-recrutment.s3.ap-south-1.amazonaws.com/addresses.json")
p = p.json() 


c1,c2 = map(float,input().split())  


arr = []
for i in p:
    arr.append([i["latitude"],i["longitude"],i["_id"]])

lo = 0
hi = 10**10
ans = []
while(lo<=hi):
    mid = (lo+hi)/2 
    res = [[] for i in range(10)]
    def check(mid):
        value = 0
        arr2 = []
        for i in arr:
            arr2.append(i)
        totdist = 0
        var1, var2 = c1,c2
        while(value<10 and len(arr2)>0):
            dist = []
            index = 0
            for i,j,k in arr2:
                dist.append([dis([i,j],[var1,var2]),i,j,k,index])
                index+=1
            dist.sort()
            totdist+=dist[0][0]
            finaldist = dis([c1,c2],[dist[0][1],dist[0][2]])
            if totdist+finaldist<=mid:
                var1,var2 = dist[0][1],dist[0][2]
                res[value].append(dist[0][3])
                arr2.pop(dist[0][4])
            else:
                value+=1
                totdist = 0
                var1,var2 = c1,c2
        if len(arr2)==0:
            return res
        else:
            return False
    if check(mid):
        ans = res.copy()
        hi = mid-1
    else:
        lo = mid+1
left = 0
for i in ans:
    if len(i)==0:
        left+=1
l = []
for i in range(len(ans)):
    if left==0:
        break
    while(len(ans[i])>1 and left>0):
        l.append(ans[i].pop())
        left-=1
for i in range(len(ans)):
    if ans[i]==[]:
        ans[i].append(l.pop()) 
print(ans)



#I have solved this problem using binary search whose steps are written below-First we'll retrieve data
#from a given url with the help of request module in variable ‘p’.Then I have stored the given
#location of the store in variables c1,c2. Now, I have taken the value of latitude, longitude,
#and id in an array ‘arr’.Then i’ll perform binary search in which l’ll take ‘mid’ as minimum
#of maximum distance covered by delivery agents (‘lo’ as lowest possible distance covered by
#delivery agents, and ‘hi’ as some maximum value).I’ll check if it is possible to deliver all
#the orders by the delivery agents on covering that ‘mid’ distance.If yes, then i’ll store the
#order in which delivery agents will do the deliveries in array ‘ans’ and try to minimise ‘mid’
#by decreasing ‘hi’ value otherwise i’ll increase ‘mid’ by increasing ‘lo’.At the end, i’ll print the ‘ans’ array.





