/**
 * @param {string} s
 * @param {string} goal
 * @return {boolean}
 */
var buddyStrings = function (s, goal) {
    const diff = []
    if (s.length !== goal.length) {
        return false
    } if (s === goal) {
        const a = new Set(s)
        return a.size < s.length
    } for (let i = 0; i < s.length; i++) {
        // i can only swap twice 
        if (s[i] !== goal[i]) {
            diff.push([s[i], goal[i]])
        }
    }
    return diff.length === 2 && diff[0][0] === diff[1][1] && diff[0][1] === diff[1][0]
};