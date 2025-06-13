package main

import (
	"fmt"
)

//Definition for singly-linked list.
type ListNode struct {
    Val int
    Next *ListNode
}

func reverseKGroup(head *ListNode, k int) *ListNode {
	sentinel_begin := &ListNode{0, head} 
	sentinel := sentinel_begin 

	buffer := make([]ListNode, 0, k)
	current := head
	for current != nil {
		buffer = append(buffer, *current)
		current = current.Next
		fmt.Println(current)
		fmt.Println(buffer)
		if len(buffer) == k {

			for i := range buffer[1:] {
				buffer[k-i-1].Next = &buffer[k-i-2]
			}
			sentinel.Next = &buffer[k-1]
			sentinel = &buffer[0]
			sentinel.Next = nil
			buffer = make([]ListNode, 0, k)
		}
	}

	if len(buffer) != 0 { 
		sentinel.Next = &buffer[0]
	}

	return sentinel_begin.Next
}


func main(){
    node5 := &ListNode{Val: 5, Next: nil}
    node4 := &ListNode{Val: 4, Next: node5}
    node3 := &ListNode{Val: 3, Next: node4}
    node2 := &ListNode{Val: 2, Next: node3}
    node1 := &ListNode{Val: 1, Next: node2}

    // Starting point of the linked list
    head := node1
    reversed_head := reverseKGroup(head, 3)
    // Printing the linked list
    printList(reversed_head)

}

func printList(node *ListNode) {
    for node != nil {
        fmt.Println(node.Val)
        node = node.Next
    }
}
