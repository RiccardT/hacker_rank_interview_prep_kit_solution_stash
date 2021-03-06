

def swapNodes(indices: list, queries: list) -> list:
    partitioned_indices = partition_indices_for_tree_construction(indices)
    tree = construct_tree_from(partitioned_indices)
    processed_queries = process_queries_for_tree_swapping_given_depth_limit(queries, tree.depth)
    tree.perform_swapped_traversals_with(processed_queries)
    return tree.results


def partition_indices_for_tree_construction(indices: list) -> list:
    indices_partitioner = IndicesPartitioner(indices)
    partitioned_indices = indices_partitioner.partition_indices()
    return partitioned_indices


class IndicesPartitioner:

    def __init__(self, indices: list):
        self.indices: list = indices
        self.partitioned_indices: list = []

    def partition_indices(self):
        self.partition_indices_into_levels()
        return self.partitioned_indices

    def partition_indices_into_levels(self):
        indices_length = len(self.indices)
        current_index = 0
        number_of_non_null_nodes_in_previous_level = 1
        while current_index < indices_length:
            partition = self.construct_partition_with(current_index, number_of_non_null_nodes_in_previous_level)
            self.partitioned_indices.append(partition)
            current_index += len(partition) // 2
            number_of_non_null_nodes_in_previous_level = self.get_non_null_node_count_in(partition)

    def construct_partition_with(self, current_index: int, count_of_non_null_nodes_in_previous_level: int) -> list:
        start_index = current_index
        size = count_of_non_null_nodes_in_previous_level
        end_index = start_index + size
        sequential_partition = []
        for index in range(start_index, end_index):
            sequential_partition.extend(self.indices[index])
        return sequential_partition

    @staticmethod
    def get_non_null_node_count_in(partition: list):
        non_node_count = 0
        for data in partition:
            if data != -1:
                non_node_count += 1
        return non_node_count


def construct_tree_from(partitioned_indices: list):
    tree_factory = TreeFactory()
    tree_factory.construct_tree_with(partitioned_indices)
    tree = tree_factory.get_constructed_tree()
    return tree


class TreeFactory:

    def __init__(self):
        self.tree_root = None
        self.partitioned_indices: list = []
        self.tree_levels: list = []

    def get_constructed_tree(self):
        constructed_tree = Tree()
        constructed_tree.root = self.tree_root
        constructed_tree.tree_levels = self.tree_levels.copy()
        constructed_tree.depth = len(self.tree_levels) - 1
        return constructed_tree

    def construct_tree_with(self, partitioned_indices: list):

        self.tree_root: Node = Node(1)
        self.partitioned_indices = partitioned_indices
        self.construct_tree_levels_with_partitioned_indices()
        self.connect_levels()

    def construct_tree_levels_with_partitioned_indices(self):
        self.tree_levels.append([self.tree_root])
        for indices_partition in self.partitioned_indices:
            nodes = self.construct_nodes_with(indices_partition)
            self.tree_levels.append(nodes)

    @staticmethod
    def construct_nodes_with(indices_partition) -> list:
        nodes = []
        for data in indices_partition:
            node = Node(data) if data != -1 else None
            nodes.append(node)
        return nodes

    def connect_levels(self):
        connection_i = 0
        connection_j = 1
        number_of_connection_steps = len(self.tree_levels) - 1
        for _ in range(number_of_connection_steps):
            parents = self.tree_levels[connection_i]
            children = self.tree_levels[connection_j]
            self.connect(parents, children)
            connection_i += 1
            connection_j += 1

    @staticmethod
    def connect(parents: list, children: list):
        left_child_index = 0
        right_child_index = 1
        for parent in parents:
            if parent is not None:
                parent.left = children[left_child_index]
                parent.right = children[right_child_index]
                left_child_index += 2
                right_child_index += 2


class Tree:

    def __init__(self):
        self.root = None
        self.tree_levels = []
        self.depth = 0
        self.in_order_traversal_path: list = []
        self.results = []

    def perform_swapped_traversals_with(self, processed_queries: list):
        for processed_query in processed_queries:
            self.perform_swap_operations_with(processed_query)
            self.perform_in_order_traversal(self.root)
            result = self.in_order_traversal_path.copy()
            self.results.append(result)
            self.in_order_traversal_path.clear()

    def perform_swap_operations_with(self, processed_query: list):
        for tree_level_index in processed_query:
            self.swap_nodes_in_tree_level_with(tree_level_index - 1)  # level indices start at 0

    def swap_nodes_in_tree_level_with(self, tree_level_index: int):
        parents = self.tree_levels[tree_level_index]
        for parent_node in parents:
            if parent_node is not None:
                parent_node.left, parent_node.right = parent_node.right, parent_node.left

    def perform_in_order_traversal(self, current_node):
        if current_node.left is not None:
            self.perform_in_order_traversal(current_node.left)

        self.in_order_traversal_path.append(current_node.data)

        if current_node.right is not None:
            self.perform_in_order_traversal(current_node.right)


class Node:

    def __init__(self, data: int):
        self.data: int = data
        self.left = None
        self.right = None


def process_queries_for_tree_swapping_given_depth_limit(queries: list, depth_limit: int) -> list:
    query_processor = QueryProcessor(queries)
    processed_queries = query_processor.process_queries_with_depth_limit(depth_limit)
    return processed_queries


class QueryProcessor:

    def __init__(self, queries: list):
        self.queries: list = queries
        self.processed_queries: list = []

    def process_queries_with_depth_limit(self, depth_limit: int) -> list:
        for k in self.queries:
            depths_to_be_swapped = []
            multiple = 1
            product = multiple*k
            while product <= depth_limit:
                depths_to_be_swapped.append(product)
                multiple += 1
                product = multiple * k
            self.processed_queries.append(depths_to_be_swapped)
        return self.processed_queries.copy()
