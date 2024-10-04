import "fmt"
func longestSubarray(nums []int) int {
    last_zero := -1
    curr_ones := 0
    max_ones := 0
    for index, num := range nums {
        if num == 1 {
            curr_ones++
        }else {
            if last_zero > -1 {
                curr_ones = index - last_zero - 1
            }
            last_zero = index
        }

        if curr_ones > max_ones {
            max_ones = curr_ones
        }
    }

    if max_ones == len(nums) {
        return max_ones - 1
    }

    return max_ones
}