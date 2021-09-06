#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time : 2021/9/6 11:27
# @Author : Dongyang Li
# @File : 两数之和.py

class Solution():
    def twoSun(self, nums, target):
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]


# 那么我们先来个简单的测试，去测试一下：

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSun([2,7,11,15], 9))
