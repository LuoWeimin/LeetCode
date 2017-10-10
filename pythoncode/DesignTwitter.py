#!/usr/bin/python
# -*- coding: UTF-8 -*-
import heapq

import itertools

import collections


class Twitter(object):

    # def __init__(self):
    #     """
    #     Initialize your data structure here.
    #     """
    #     self.twitters = {}
    #     self.follows = {}
    #     self.index = 0
    #
    # def postTweet(self, userId, tweetId):
    #     """
    #     Compose a new tweet.
    #     :type userId: int
    #     :type tweetId: int
    #     :rtype: void
    #     """
    #     if userId not in self.twitters:
    #         self.twitters[userId] = {self.index: tweetId}
    #     else:
    #         self.twitters[userId][self.index] = tweetId
    #     self.index += 1
    #
    # def getNewsFeed(self, userId):
    #     """
    #     Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
    #     :type userId: int
    #     :rtype: List[int]
    #     """
    #     if userId in self.follows:
    #         users = self.follows[userId] + [userId]
    #         rs = []
    #         vrs = {}
    #         for userId in users:
    #             if userId in self.twitters:
    #                 dict = self.twitters[userId]
    #                 for key in dict:
    #                     heapq.heappush(rs, key)
    #                     vrs[key] = dict[key]
    #                     if len(rs) > 10:
    #                         vrs.pop(heapq.heappop(rs))
    #         rs = sorted(rs, reverse=True)
    #         return [vrs[i] for i in rs]
    #     else:
    #         if userId in self.twitters:
    #             rs = []
    #             vrs = {}
    #             dict = self.twitters[userId]
    #             for key in dict:
    #                 heapq.heappush(rs, key)
    #                 vrs[key] = dict[key]
    #                 if len(rs) > 10:
    #                     vrs.pop(heapq.heappop(rs))
    #             rs = sorted(rs, reverse=True)
    #             return [vrs[i] for i in rs]
    #         else:
    #             return []
    #
    # def follow(self, followerId, followeeId):
    #     """
    #     Follower follows a followee. If the operation is invalid, it should be a no-op.
    #     :type followerId: int
    #     :type followeeId: int
    #     :rtype: void
    #     """
    #     if followerId not in self.follows:
    #         self.follows[followerId] = [followeeId]
    #     else:
    #         self.follows[followerId].append(followeeId)
    #
    # def unfollow(self, followerId, followeeId):
    #     """
    #     Follower unfollows a followee. If the operation is invalid, it should be a no-op.
    #     :type followerId: int
    #     :type followeeId: int
    #     :rtype: void
    #     """
    #     if followerId in self.follows:
    #         if followeeId in self.follows[followerId]:
    #             self.follows[followerId].remove(followeeId)
    #
    #     # Your Twitter object will be instantiated and called as such:
    #     # obj = Twitter()
    #     # obj.postTweet(userId,tweetId)
    #     # param_2 = obj.getNewsFeed(userId)
    #     # obj.follow(followerId,followeeId)
    #     # obj.unfollow(followerId,followeeId)
    def __init__(self):
        self.timer = itertools.count(step=-1)
        self.tweets = collections.defaultdict(collections.deque)
        self.followees = collections.defaultdict(set)

    def postTweet(self, userId, tweetId):
        self.tweets[userId].appendleft((next(self.timer), tweetId))

    def getNewsFeed(self, userId):
        tweets = heapq.merge(*(self.tweets[u] for u in self.followees[userId] | {userId}))
        return [t for _, t in itertools.islice(tweets, 10)]

    def follow(self, followerId, followeeId):
        self.followees[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        self.followees[followerId].discard(followeeId)

twitter = Twitter()
twitter.postTweet(1, 5)
print twitter.getNewsFeed(1)
twitter.follow(1, 2)
twitter.postTweet(2, 6)
print twitter.getNewsFeed(1)
twitter.unfollow(1, 2)
print twitter.getNewsFeed(1)
print twitter.getNewsFeed(2)
twitter.follow(1, 2)
twitter.postTweet(2, 7)
twitter.postTweet(2, 8)
twitter.postTweet(2, 9)
twitter.postTweet(2, 10)
twitter.postTweet(2, 11)
twitter.postTweet(2, 12)
twitter.postTweet(2, 13)
twitter.postTweet(2, 14)
twitter.postTweet(2, 15)
twitter.postTweet(2, 16)
twitter.postTweet(2, 17)
for i in range(100, 1000):
    twitter.postTweet(i % 10, i)
twitter.follow(1, 3)
twitter.follow(1, 4)
twitter.follow(1, 5)
twitter.follow(1, 6)
twitter.follow(1, 7)
twitter.unfollow(1, 10)
twitter.follow(2, 1)
twitter.follow(2, 3)
twitter.follow(2, 4)
twitter.follow(2, 7)
twitter.follow(2, 9)
print twitter.getNewsFeed(1)
print twitter.getNewsFeed(2)
print twitter.getNewsFeed(3)
print twitter.getNewsFeed(4)
print twitter.getNewsFeed(5)
print twitter.getNewsFeed(6)
print twitter.getNewsFeed(7)
print twitter.getNewsFeed(8)