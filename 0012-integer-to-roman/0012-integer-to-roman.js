/**
 * @param {number} num
 * @return {string}
 */
var intToRoman = function(num) {
    const arr = [1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000]
    const rArr = ['I', 'IV', 'V', 'IX', 'X', 'XL', 'L', 'XC', 'C', 'CD', 'D', 'CM', 'M']
    
    let roman = ''
    let i = arr.length-1
    while (num !== 0) {
        for (; i >= 0; i-- ){ // i is intialized outside while loop so every time we break out we restart counting from the current i -> we don't reinitalize i
            if (arr[i] <= num) {
                roman += rArr[i]
                num = num - arr[i]
                break
            }
        }
    }
    
    return roman
};