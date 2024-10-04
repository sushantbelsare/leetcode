func maxOperations(nums []int, k int) int {
    freq := make(map[int]int)
    ops := 0
    for _, num := range nums {
        if v, ok := freq[k - num]; ok && v > 0 {
            freq[k - num]--
            ops++
        }else{
            freq[num]++
        }
    }
    return ops
}