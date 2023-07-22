#include <bits/stdc++.h>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };

class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if(list1 == nullptr) {
            return list2;
        }
        if (list2 == nullptr) {
            return list2;
        }
        ListNode *head = nullptr;
        ListNode *body = nullptr;
        while(list1 != nullptr || list2 != nullptr) {
            if (list1 != nullptr && list1 -> val < list2 -> val) {
                if (body == nullptr) {
                    body = list1;
                }
                else {
                    body->next = list1;
                    body = body-> next;

                }
                list1 = list1->next;

            }
            else {
                if (body == nullptr) {
                    body = list2;
                }
                else {
                    body -> next = list2;
                    body = body-> next;

                }
                list2 = list2->next;

            }

        }
        return head;

    }
};

int main() {

}
