from collections import defaultdict

class Twitter:
    def __init__(self):
        self.following = defaultdict(set) # userId -> set(userIds that they follow)
        self.tweets = defaultdict(list)   # userId -> (tweet timestamp, tweetid) 
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timestamp, tweetId))
        self.timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        follows = self.following[userId] | set([userId])
        timestamped = []
        for f in follows:
            timestamped.extend(self.tweets[f])
        print(timestamped)
        timestamped.sort()
        return [tweetId for _, tweetId in timestamped[:-11:-1]]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)        
