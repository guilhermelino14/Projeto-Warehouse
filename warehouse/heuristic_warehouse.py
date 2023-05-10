import numpy as np
from agentsearch.heuristic import Heuristic
from warehouse.cell import Cell
from warehouse.warehouse_problemforSearch import WarehouseProblemSearch
from warehouse.warehouse_state import WarehouseState


class HeuristicWarehouse(Heuristic[WarehouseProblemSearch, WarehouseState]):

    def __init__(self):
        super().__init__()

    def compute(self, state: WarehouseState) -> float:
        h = 0
        #for i in range(state.rows):
         #   for j in range(state.columns):
          #      tile = state.matrix[i][j]
           #     if tile != 0:
                    #tile_goal_line, tile_goal_column = self._goal_matrix_positions[tile]
                    # tile_goal_line, tile_goal_column = self._goal_matrix_positions.get(tile, (0, 0))
                    #print( "line:" + str(i) + " -- " + str(tile_goal_line) + " - column:" + str(j) + " -- " + str(tile_goal_column))
                    #h += abs(i - tile_goal_line) + abs(j - tile_goal_column)
                   # h = 1
        forkliftCell = Cell(state.line_forklift, state.column_forklift)
        goalCell = self.problem.goal_position
        h = abs(forkliftCell.line - goalCell.line) + abs(forkliftCell.column - goalCell.column)
        return h

    def __str__(self):
        return "# TODO"