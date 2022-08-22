def solution(entrances, exits, path):
    """Ford-Fulkerson algorithm implementation"""
    # ASSUMING ACYCLIC GRAPH
    # add single start & end nodes
    # create flow edges matrix (initialized to zeroes).
    # REPEAT:
    #  - Find _path by DFS (if no _path to end exists return)
    #  - Update capacity and flow values
    from copy import deepcopy
    
    MAX_EDGE_WEIGHT = 100000000

    class ContinueException(Exception):
        pass

    class BreakException(Exception):
        pass

    def get_path_dfs(edge_capacities, edge_flows, current_path, current_min_edge):
        _current_node = current_path[-1]
        for cap_index in range(len(edge_capacities)):
            if cap_index not in current_path and edge_capacities[_current_node][cap_index] > 0:                    
                _new_path = current_path + [cap_index]
                _new_min_edge = min(current_min_edge, edge_capacities[_current_node][cap_index])
                if cap_index == len(edge_capacities) - 1:
                    return _new_path, _new_min_edge
                _res_path, _res_min_edge = get_path_dfs(edge_capacities, edge_flows, _new_path, _new_min_edge)
                if _res_path is not None:
                    return _res_path, _res_min_edge
        for flow_index in range(len(edge_flows)):
            if flow_index not in current_path and edge_flows[flow_index][_current_node] > 0:
                _new_path = current_path + [flow_index]
                _new_min_edge = min(current_min_edge, edge_capacities[flow_index][_current_node])
                _res_path, _res_min_edge = get_path_dfs(edge_capacities, edge_flows, _new_path, _new_min_edge)
                if _res_path is not None:
                    return _res_path, _res_min_edge
        return None, None

    def update_edges(edge_capacities, edge_flows, dfs_path, path_min_edge):
        for edge_start, edge_end in zip(dfs_path[:-1], dfs_path[1:]):
            if edge_capacities[edge_start][edge_end] != 0:
                edge_capacities[edge_start][edge_end] -= path_min_edge
                edge_flows[edge_start][edge_end] += path_min_edge
            else:
                edge_capacities[edge_start][edge_start] += path_min_edge

    start_node_edges = [MAX_EDGE_WEIGHT if i-1 in entrances else 0 for i in range(len(path) + 2)]
    end_node_edges = [0 for i in range(len(path) + 2)]
    edge_capacities = [[0] + row + [0] for row in path]
    for _exit in exits:
        edge_capacities[_exit][-1] = MAX_EDGE_WEIGHT  # Setting capacity for edge between exits and finish node
    edge_capacities = [start_node_edges] + edge_capacities + [end_node_edges]
    edge_flows = [[0 for i in range(len(edge_capacities))] for j in range(len(edge_capacities))]
    while True:
        dfs_path, min_edge = get_path_dfs(edge_capacities, edge_flows, [0], MAX_EDGE_WEIGHT)
        if dfs_path is None:
            break
        update_edges(edge_capacities, edge_flows, dfs_path, min_edge)
    return sum([row[-1] for row in edge_flows])


if __name__ == '__main__':
    print(solution([0], [3], [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]))
