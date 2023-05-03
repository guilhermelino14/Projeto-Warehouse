
import copy

import constants
from agentsearch.problem import Problem
from warehouse.actions import *
from warehouse.cell import Cell
from warehouse.warehouse_state import WarehouseState


class WarehouseProblemSearch(Problem[WarehouseState]):

    def __init__(self, initial_state: WarehouseState, goal_position: Cell):
        super().__init__(initial_state)
        self.actions = [ActionDown(), ActionUp(), ActionRight(), ActionLeft()]
        self.goal_position = goal_position
        self.adjacente = None
        if self.isProduct(self.goal_position):
            if (self.goal_position.line + 1) <= 4 and initial_state.matrix[self.goal_position.line + 1][self.goal_position.column] == constants.EMPTY:
                self.adjacente = Cell(self.goal_position.line + 1, self.goal_position.column)
            if (self.goal_position.column + 1) <= 4 and initial_state.matrix[self.goal_position.line][self.goal_position.column + 1] == constants.EMPTY:
                self.adjacente = Cell(self.goal_position.line, self.goal_position.column  + 1)
            if (self.goal_position.line - 1) <= 4 and initial_state.matrix[self.goal_position.line - 1][self.goal_position.column] == constants.EMPTY:
                self.adjacente = Cell(self.goal_position.line - 1, self.goal_position.column)
            if (self.goal_position.column + 1) <= 4 and initial_state.matrix[self.goal_position.line][self.goal_position.column -1] == constants.EMPTY:
                self.adjacente = Cell(self.goal_position.line, self.goal_position.column - 1)

    def get_actions(self, state: WarehouseState) -> list:
        valid_actions = []
        for action in self.actions:
            if action.is_valid(state):
                valid_actions.append(action)
        return valid_actions

    def get_successor(self, state: WarehouseState, action: Action) -> WarehouseState:
        successor = copy.deepcopy(state)
        action.execute(successor)
        return successor

    def is_goal(self, state: WarehouseState) -> bool:
        # TOD0
        # ir ao warehouse state buscar posicao do forklift coinincide com a goal_position
        forkliftCell = Cell(state.line_forklift, state.column_forklift)
        if self.isProduct(self.goal_position):
            return forkliftCell == self.adjacente
        return forkliftCell == self.goal_position

    def __str__(self):
        return str(self.initial_state.line_forklift) + " - " + str(self.initial_state.column_forklift) + " / " + str(self.goal_position.line) + " - " + str(self.goal_position.column)

    def isProduct(self, cell):
        return not (self.initial_state.line_exit == cell.line and self.initial_state.column_exit == cell.column)