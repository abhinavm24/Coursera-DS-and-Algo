Priority Queues and Disjoint Sets
We start this module by considering priority queues which are used to efficiently schedule jobs, either in the context of a computer operating system or in real life, to sort huge files, which is the most important building block for any Big Data processing algorithm, and to efficiently compute shortest paths in graphs, which is a topic we will cover in our next course. For this reason, priority queues have built-in implementations in many programming languages, including C++, Java, and Python. We will see that these implementations are based on a beautiful idea of storing a complete binary tree in an array that allows to implement all priority queue methods in just few lines of code. We will then switch to disjoint sets data structure that is used, for example, in dynamic graph connectivity and image processing. We will see again how simple and natural ideas lead to an implementation that is both easy to code and very efficient. By completing this module, you will be able to implement both these data structures efficiently from scratch.


Learning Objectives
Describe how heaps and priority queues work
Describe how disjoint set union data structure works
Analyze the running time of operations with heaps
List the heuristics that speedup disjoint set union
Apply priority queues to schedule jobs on processors
Apply disjoint set union to merge tables in a database