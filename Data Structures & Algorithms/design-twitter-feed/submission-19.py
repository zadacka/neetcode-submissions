from collections import defaultdict
import heapq

class Twitter:
    def __init__(self):
        self.following = defaultdict(set) # userId -> set(userIds that they follow)
        self.tweets = defaultdict(list)   # userId -> (timestamp, userId, tweet, index) 
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        # build a heap with 'most recent' tweet per followee
        maxheap = []
        self.following[userId].add(userId) # ensure we look at own tweets
        for uid in self.following[userId]:
            if uid in self.tweets:
                tweets = self.tweets[uid]
                idx = len(tweets) - 1
                timestamp, tweet = tweets[-1]
                heapq.heappush_max(maxheap, (timestamp, uid, tweet, idx))
                # potential optimisation: we could trim the heap to size 10 here!
        result = []
        while maxheap and len(result) < 10:
            timestamp, uid, tweet, idx = heapq.heappop_max(maxheap)
            result.append(tweet)
            if idx != 0:
                next_timestamp, next_tweet = self.tweets[uid][idx-1]
                heapq.heappush_max(maxheap, (next_timestamp, uid, next_tweet, idx - 1))
        return result


    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)        
