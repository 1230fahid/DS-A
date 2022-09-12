class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        if(len(score) == 1):
            return ["Gold Medal"]
        elif (len(score)==2):
            if(score[0] > score[1]):
                return ["Gold Medal", "Silver Medal"]
            else:
                return ["Silver Medal", "Gold Medal"]
        elif(len(score)==3):
            if (score[0] > score[1]) and (score[0] > score[2]):
                if(score[1] > score[2]):
                    return ["Gold Medal", "Silver Medal", "Bronze Medal"]
                else:
                    return ["Gold Medal", "Bronze Medal", "Silver Medal"]
            elif (score[1] > score[0]) and (score[1] > score[2]):
                if(score[0] > score[2]):
                    return ["Silver Medal", "Gold Medal", "Bronze Medal"]
                else:
                    return ["Bronze Medal", "Gold Medal", "Silver Medal"]
            elif (score[2] > score[0]) and (score[2] > score[1]):
                if(score[0] > score[1]):
                    return ["Silver Medal", "Bronze Medal", "Gold Medal"]
                else:
                    return ["Bronze Medal", "Silver Medal", "Gold Medal"]
        else:
            greatest = max(score)
            idx = score.index(greatest)
            score[idx] = -1
            mid = max(score)
            idx2 = score.index(mid)
            score[idx2] = -2
            third = max(score)
            idx3 = score.index(third)
            score[idx3] = -3
            answer = [0] * len(score)
            losers = []
            for i in range(0, len(score)):
                if(score[i] >= 0):
                    losers.append(score[i])
            losers.sort()
            losers = losers[::-1]
            #print(losers)
            lookup = {}
            for cnt, val in enumerate(losers):
                lookup[val] = cnt + 4
            for i in range(0, len(answer)):
                if i == idx:
                    answer[i] = "Gold Medal"
                elif i == idx2:
                    answer[i] = "Silver Medal"
                elif i == idx3:
                    answer[i] = "Bronze Medal"
                else:
                    answer[i] = str(lookup[score[i]])
                    #j+=1
                #print(i)
            return answer
