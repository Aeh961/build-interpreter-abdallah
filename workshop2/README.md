# Workshop 2 Homework: Trees and Recursion

## Tree Diagrams

Exercise 1:

```text
A
+-- B
+-- C
```

Exercise 2:

```text
Documents
+-- Photos
|   +-- beach.jpg
|   +-- dog.png
+-- School
    +-- CS101
    +-- Notes
```

Exercise 11:

```text
      +
     / \
    1   *
       / \
      2   3
```

Exercise 13:

```text
      *
     / \
    +   5
   / \
  2   3
```

## Written Answers

1. The root is Documents.

2. The leaves are beach.jpg, dog.png, CS101, and Notes.

3. The parent of Notes is School.

4. The subtree rooted at Photos is Photos with its children, beach.jpg and dog.png.

5. countdown prints before the recursive call, so I see each number while the calls are going deeper. mystery prints after the recursive call, so it waits until the base case is reached and then prints as the calls return.

6. I think trees are useful for representing programs because programs have nested structure, and trees show how smaller pieces like numbers, operators, and expressions fit inside larger pieces.

7. Recursion works well on trees because each child is also a smaller tree, so the same function can solve the problem for the current node and then for each child.

8. The evaluator has to evaluate the children first because an operator needs the values of its left and right children before it can combine them.

9. The trickiest part for me was tracking whether work happens before or after the recursive call, because that changes the order of the output.

The code solution is in `workshop2_trees_recursion_homework.py`.
