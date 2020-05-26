#include "linkedlist.h"

#include <iostream>
#include <vector>

int main(int argc, char** argv) {
  std::vector<int> nums({1, 2, 3, 4, 5});

  linkedlist::LinkedList linked_list_obj(nums);
  linkedlist::LinkedList linked_list_obj_2(nums);

  std::cout << "----- before deletion -----" << std::endl;

  linkedlist::Node* node = linked_list_obj.head;
  for (int i=0; i < linked_list_obj.size; i++) {
    std::cout << node->data << std::endl;
    node = node->next;
  }

  linked_list_obj.delete_(4);

  std::cout << "***** after deletion *****" << std::endl;

  node = linked_list_obj.head;
  for (int i=0; i < linked_list_obj.size; i++) {
    std::cout << node->data << std::endl;
    node = node->next;
  }

  std::cout << "----- before reversal -----" << std::endl;
  linkedlist::Node* node_2 = linked_list_obj_2.head;
  for (int i=0; i < linked_list_obj_2.size; i++) {
    std::cout << node_2->data << std::endl;
    node_2 = node_2->next;
  }

  std::cout << "***** after reversal *****" << std::endl;
  linked_list_obj_2.reverse_();
  node = linked_list_obj_2.head;
  for (int i=0; i < linked_list_obj_2.size; i++) {
    std::cout << node_2->data << std::endl;
    node_2 = node_2->next;
  }

  return 0;
}
