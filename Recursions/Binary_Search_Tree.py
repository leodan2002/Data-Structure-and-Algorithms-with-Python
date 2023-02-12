# Define build_bst() below...
def build_bst(my_list):
  if my_list == []:
    return "No Child"
  middle_index = len(my_list) // 2
  middle_value = my_list[middle_index]
  print("Middle index: {0}".format(middle_index))
  print("Middle value: {0}".format(middle_value))
  tree_node = {"data": middle_value}
  tree_node["left_child"] = build_bst(my_list[: middle_index])
  tree_node["right_child"] = build_bst(my_list[middle_index+1 :])
  return tree_node
# For testing
sorted_list = [12, 13, 14, 15, 16]
binary_search_tree = build_bst(sorted_list)
print(binary_search_tree)

# fill in the runtime as a string
# 1, logN, N, N*logN, N^2, 2^N, N!
runtime = "N*logN"
