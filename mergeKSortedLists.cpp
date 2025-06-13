#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <numeric>


using namespace std;




struct ListNode {
    int val;
    ListNode* next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode* next) : val(x), next(next) {}
};


ListNode* mergeKLists(vector<ListNode*>& lists) {
	for ( int i = 0; i < lists.size(); i++ ) {
            auto it = lists.begin();
            if ( !lists[i]){
                lists.erase(it+i);
                i--;
            }
        }
	int n = lists.size();

	auto customCompare = [&lists](int a, int b) {
		if (!lists[a]) return false;  // Handle null pointers
		if (!lists[b]) return true;
		return lists[a]->val > lists[b]->val;
	};
	
	priority_queue<int, vector<int>, decltype(customCompare)> pq(customCompare);

	for ( int i = 0; i < n; i++ ){
		pq.push(i);
	}

	int val = pq.top();
	ListNode* head = lists[val];
	ListNode* tail = lists[val];
	ListNode* prev = lists[val];
	pq.pop();
	lists[val] = lists[val]->next;
	while(!pq.empty() or tail->next){

		if ( tail->next ) {
			pq.push(val);
		}
		val = pq.top();
		tail = lists[val];
		prev->next = tail;
		prev=tail;
		pq.pop();
		lists[val] = lists[val]->next;
		//cout << "," << tail->val;
	}

	return head;
	
}
// Function prototype (assuming you implement this)

// Helper function to create a linked list from a vector
ListNode* createLinkedList(const vector<int>& values) {
    if (values.empty()) return nullptr;

    ListNode* head = new ListNode(values[0]);
    ListNode* current = head;
    
    for (size_t i = 1; i < values.size(); i++) {
        current->next = new ListNode(values[i]);
        current = current->next;
    }
    
    return head;
}

// Helper function to print a linked list
void printLinkedList(ListNode* head) {
    while (head) {
        cout << head->val << " -> ";
        head = head->next;
    }
    cout << "nullptr" << endl;
}

// Main function for testing
int main() {
    // Create test cases
    vector<ListNode*> lists;

    lists.push_back(createLinkedList({1, 4, 5}));
    lists.push_back(createLinkedList({3, 3, 4}));
    lists.push_back(createLinkedList({2}));
    lists.push_back(createLinkedList({0, 6, 7, 7}));
    lists.push_back(createLinkedList({}));

    cout << "Input lists:\n";
    for (auto list : lists) {
        printLinkedList(list);
    }

    // Call your function
    ListNode* mergedHead = mergeKLists(lists);

    //cout << "\nMerged list:\n";
    printLinkedList(mergedHead);

    return 0;
}

