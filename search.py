# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST

    #util.raiseNotDefined()
    #print("Start:", problem.getStartState())
    #print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    #print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    #Initialize a stack
    Edges = util.Stack()
    #Track the nodes that where visited. We use a set because they do not allow duplicates.
    #Set fist node to be StartState
    start = ((problem.getStartState(),[]))
    Edges.push(start)
    Visited = []


    #While stack is not empty keep iterating. Meaning that until the stack is not empty it has not found the goal.
    while not Edges.isEmpty():
        state, direction = Edges.pop()

        if problem.isGoalState(state):
            return direction
        if state not in Visited:
            #A node is not visited ultil its edges have been searched.
            Visited.append(state)
            for cord, move, value in problem.getSuccessors(state):
                Edges.push((cord, direction + [move]))

    return []






#Pop the visited node.
        #If the node I visited has the solution I want then return the path
        #Else mark the edge as visited and grab their edges. This would expand the tree.




def breadthFirstSearch(problem: SearchProblem):
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    Edges = util.Queue()
    Visited = []
    Current = [problem.getStartState(), []]
    Edges.push(Current)

    while not Edges.isEmpty():
        state, direction = Edges.pop()
        if problem.isGoalState(state):
            return direction
        if state not in Visited:
            Visited.append(state)

            for coordinates, move, value in problem.getSuccessors(state):
                Edges.push((coordinates, direction + [move]))
    return []





def uniformCostSearch(problem: SearchProblem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    edges = util.PriorityQueue()
    visited = []
    edges.push((problem.getStartState(), [], 0), 0)

    while not edges.isEmpty():
        state, direction, cost = edges.pop()

        if problem.isGoalState(state):
            return direction

        if state not in visited:
            visited.append(state)

            for coord, move, price in problem.getSuccessors(state):
                value = cost + price
                edges.push((coord, direction + [move], value), value)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()

    edges = util.PriorityQueue()
    visited = set()

    edges.push((problem.getStartState(), [], 0), 0)

    while not edges.isEmpty():
        node, moves, cost = edges.pop()

        if problem.isGoalState(node):
            return moves
        if node not in visited:
            visited.add(node)

            for coord, direction, value in problem.getSuccessors(node):
                count = cost + value
                edges.push((coord, moves + [direction], count), count + heuristic(coord, problem))


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
