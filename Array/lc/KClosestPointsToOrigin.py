#Initial conditions to watch out for
    # Is k > len(points)?
    # Can k be 0?
    # Can points matrix be empty?
    # Confirm that each value in points is specifically an ARRAY of LENGTH 2.
    #Time: O(nlog(n)) where n = len(points)
    #Space: O(n) where n = len(points)

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        arr =[]
        pDict={}
        result = []
        i = 0
        for i in range(0, len(points)): #get distances and add to an array to contain all distances, and get coordinates for corresponding distances as key-pair values in a dictionary
            distance = sqrt(points[i][0]**2 + points[i][1]**2)
            arr.append(distance)
            if(distance in pDict.keys()): #case for points with same distance
                pDict[distance].append(points[i])
            else:
                pDict[distance] = [points[i]]
        
        #arr.sort() #use built in sort operation to sort matrix, else could just do merge sort
        
        #using bucketsort
        

        newarr = []
        maxs = max(arr)
        mins = min(arr)
        rnge = (maxs - mins) / len(pDict.keys())
        
        print("maxs is", maxs)
        print("mins is", mins)
        print("rnge is", rnge)
        
        if(maxs != mins):
            for i in range(0, len(pDict.keys()) + 1):
                newarr.append([])
                
            print("len(newarr) is", len(newarr))
            # scatter the array elements
            # into the correct bucket
            for i in range(len(arr)):
                diff = (arr[i] - mins) / rnge - int((arr[i] - mins) / rnge)
  
                # append the boundary elements to the lower array
                if(diff == 0 and arr[i] != mins):
                    print(int((arr[i] - mins) / rnge) -1 )
                    newarr[int((arr[i] - mins) / rnge) - 1].append(arr[i])
  
                else:
                    num = int((arr[i] - mins) / rnge)
                    print(num)
                    newarr[num].append(arr[i])
  
            # Sort each bucket individually
            for i in range(len(newarr)):
                if len(newarr[i]) != 0:
                    newarr[i].sort()
  
            # Gather sorted elements 
            # to the original array
            m = 0
            for lst in newarr:
                if lst:
                    for i in lst:
                        arr[m] = i
                        m = m+1
        
            #print(arr)
            #print(pDict)
        
            i=0
            
        for i in range(0, k): #Here we just wanna get the k closest points, so get the coordinates of each distance from arr[0:k]
            result.append(pDict[arr[i]][0]) #get coordinate
            if(len(pDict[arr[i]]) == 1): #remove coordinate from dictionary
                del pDict[arr[i]]
            else:
                pDict[arr[i]].pop(0)
        
        return result #return
