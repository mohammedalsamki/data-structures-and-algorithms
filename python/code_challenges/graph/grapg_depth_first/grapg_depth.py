def graph_depth_first_search(graph, start_node):
        """
        Traverse a graph in depth first pre-order for a given starting node.

        Argument:
            start_node (vertex): starting node

        Returns:
            list: collection of values in preorder
        """
        visited = []

        def traverse(start_node):
            if start_node in visited:
                return
            visited.append(start_node)
            neighbors = [edge.vertex for edge in graph.get_neighbors(start_node) if edge.vertex not in visited]
            for neighbor in neighbors:
                traverse(neighbor)
        traverse(start_node)
        return [v.value for v in visited]









