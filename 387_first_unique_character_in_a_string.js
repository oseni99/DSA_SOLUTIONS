/**
 * @param {string} s
 * @return {number}
 */
var firstUniqChar = function (s) {
    let myStore = {}
    for (let i of s) {
        myStore[i] = (myStore[i] || 0) + 1
    }
    for (let i = 0; i < s.length; i++) {
        if (myStore[s[i]] === 1) {
            return i
        }
    } return -1
};