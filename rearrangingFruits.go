package main

import (
	"sort"
	"fmt"
)

func minCost(basket1 []int, basket2 []int) int64 {
	h := map[int]int{}
	n := len(basket1)
	a1 := make([]int, 0, n)
	a2 := make([]int, 0, n)
	least := basket1[0]
	for i := range basket1 {
		h[basket1[i]]+= 1
		h[basket2[i]]-= 1
		if least > basket1[i] {
			least = basket1[i]
		}
		if least > basket2[i] {
			least = basket2[i]
		}
	}

	var val int
	for key := range h {
		val = h[key]
		if val % 2 != 0 {
			return int64(-1)
		}
		if val < 0 {
			for i := 0; i < -val/2; i++ {
				a2 = append(a2, key)
			}
		}

		if val > 0 {
			for i := 0; i < val/2; i++ {
				a1 = append(a1, key)
			}
		}
	}
	if len(a1) != len(a2) {
		return -1
	}

	sort.Ints(a1)
	sort.Ints(a2)
	sum := 0
	min := 0
	m := len(a2)
	for j := range a1 {
		min = a1[j]
		if a2[m-j-1] < min {
			min = a2[m-j-1]
		}
		if least*2 < min {
			min = least*2
		}
		sum += min
	}

	fmt.Println(a1)
	fmt.Println(a2)
	return int64(sum)
}

func main(){
	//arr1 := []int{4,2,2,2}
	//arr2 := []int{1,4,1,2}
	arr1 := []int{84,80,43,8,80,88,43,14,100,88}
	arr2 := []int{32,32,42,68,68,100,42,84,14,8}


	fmt.Printf("min is %d", minCost(arr1, arr2))
}
