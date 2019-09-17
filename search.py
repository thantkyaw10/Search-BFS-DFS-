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

class node:
    def __init__(self, state, cost = 0, action = 0, parent = 0):
        # Initializes node, set cost to 0 if none provided
        # Initialize action and parent to 0 if startState node
        # Action, state and cost are from getSuccessors
        self.parent = parent # Is a node
        self.action = action 
        self.cost = cost
        self.state = state 

    def getPath(self):
        path = []
        cnode = self # Sets current node to self
        while (cnode.action != 0):
            path.append(cnode.action) # Append current node's action to path
            cnode = self.parent # Set current node to parent
        return path.reverse



def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print "Start:", problem.getStartState()
    print "Is the start a goal?", problem.isGoalState(problem.getStartState())
    print "Start's successors:", problem.getSuccessors(problem.getStartState())
    """
    "*** YOUR CODE HERE ***"
    #util.raiseNotDefined()
    explored = [] #list for states already explored
    frontier = util.Stack() #using stack data structure

    current = [problem.getStartState(), []] #format: [current state exploring, path or actions from initial to current]
    initialTo = util.Stack() #holds paths of each successecor getting explored; for them to then get explored

    #"Loop do" in psuedo code:
    while not frontier.isEmpty(): #"if empty? (frontier) then return failure"
        if problem.isGoalState(current[0]): #"if problem.goal-test(state)...
            return current[1]               # ...then return solution"
        if current not in explored: #"If node.state not in explored:"
            explored.append(current[0]) #"add node to explored"
            for succ,action,cost in (problem.getSuccessors(current[0])): #add node's children to frontier
                frontier.push(succ)
                initialTo.push(current[1] + [action])
        #go on to set the next to look at:
        temp0 = frontier.pop()
        temp1 = initialTo.pop()
        current = [temp0, temp1]
    return None #if frontier is empty and cannot find any solution for the given problem / start state

def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    startNode = node(problem.getStartState)# Initialize start node
    if problem.isGoalState(startNode.state):
        return [] # Return empty list if start is solution (no actions taken)
    frontier = util.Queue().push(startNode) # Initialize frontier with startNode
    explored = set()
    while not frontier.isEmpty():
        cnode = frontier.pop() # Pops shallowest node
        if problem.isGoalState(cnode.state): # Checks goal state
            return cnode.getPath()
        explored.add(cnode) # Add node to explored set
        for succ in problem.getSuccessors(cnode.state): # Iterate through successors, making a child node for each
            child = node(succ[0], succ[2], succ[1], node) # Initialize child node
            if child not in explored: # Adds child to frontier if not in explored 
                frontier.push(child)
    return #failure (but what is the return for failure?)

            



def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"
    util.raiseNotDefined()


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
