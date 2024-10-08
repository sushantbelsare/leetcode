/*
*   input = "AABB" output = 0
*   input = "AAACDBB" output = 1
*   input = "CDCDAB" output = 0
*   input = "CADB" output = 4
*
*   approach:
*       if s[i] + s[i + 1] in substring
*           remove (i, i + 1)
*
*       else
*           i = i + 1 
*/

import "fmt"

func minLength(s string) int {
    n := len(s)
    i := 1
    j := 0
    stack := []byte{s[0]}

    for i < n {
        if len(stack) > 0 && ((stack[j] == 'A' && s[i] == 'B') || (stack[j] == 'C' && s[i] == 'D')) {
            stack = stack[:j]
            j = j - 1
        }else{
            stack = append(stack, s[i])
            j = j + 1
        }

        i = i + 1
    }

    return j + 1
}