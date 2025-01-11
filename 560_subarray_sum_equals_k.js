/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function (nums, k) {
    const prefixSum = { 0: 1 }
    let currSum = 0
    let res = 0
    for (let i of nums) {
        currSum += i
        let diff = currSum - k
        if (prefixSum[diff]) {
            res += prefixSum[diff]
        }
        prefixSum[currSum] = (prefixSum[currSum] || 0) + 1
    }
    return res
};