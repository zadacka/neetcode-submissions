class Twitter:

    def __init__(self):
        self.counter = 0
        self.following = defaultdict(set)
        self.tweets = defaultdict(list)
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        minheap = self.tweets[userId]
        heapq.heappush(minheap, (self.counter, tweetId))
        self.counter += 1
        if len(minheap) == 11:
            _ = heapq.heappop(minheap)
        

    def getNewsFeed(self, userId: int) -> List[int]:
        follow_accounts = self.following[userId].union({userId})
        minheaps = [self.tweets[a] for a in follow_accounts]
        follows = heapq.merge(*minheaps)
        newest_first = sorted(heapq.nlargest(10, follows), reverse=True)
        return [x[1] for x in newest_first]

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].discard(followeeId)
