/*
Implement a program that provides the following operations on a binary tree.
insert adds an integer x into a binary tree T to give a binary tree R.
search returns true if x is contained in the binary tree T.
preorder lists the nodes of the binary tree T using preorder traversal.
inorder lists the nodes of the binary tree T using inorder traversal.
postorder lists the nodes of the binary tree T using postorder traversal.
*/


%insert method: insert(Tree,X,Newtree). 
/*
takes Tree and adds X to it to create Newtree, if X is already there, it just returns Newtree as Tree.
*/

insert(void,X,tree(X,void,void)).
insert(Tree,X,Tree) :- Tree = tree(X,_L,_R).		%putting an underscore in front of variables stops us from having "Singleton variable" error 
insert(tree(Root,Left,Right), X, tree(Root,L_new,Right)) :- X < Root, insert(Left,X,L_new).
insert(tree(Root,Left,Right), X, tree(Root,Left,R_new)) :- X > Root, insert(Right,X,R_new).

/*
sample test queries:
?- insert(Tree, 25, Newtree).
Newtree = tree(25, void, void),
Tree = void
?- insert(tree(25, void, void), 25, Newtree).
Newtree = tree(25, void, void)
?- insert(tree(25, tree(16, tree(8, void, void), tree(20, void, void)), tree(44, tree(32, void, void), tree(53, void, void))), 35, Newtree).
Newtree = tree(25, tree(16, tree(8, void, void), tree(20, void, void)), tree(44, tree(32, void, tree(35, void, void)), tree(53, void, void)))
false
*/

%search: find the value X in tree
search(tree(X,_L,_R),X) :- !.
search(tree(Root,Left,_R),X) :- X < Root, !, search(Left,X).
search(tree(_Root,_L,Right),X) :- search(Right,X). 

/*
sample test query:
?- search(tree(25, tree(16, tree(8, void, void), tree(20, void, void)), tree(44, tree(32, void, void), tree(53, void, void))), 30).
false
?- search(tree(25, tree(16, tree(8, void, void), tree(20, void, void)), tree(44, tree(32, void, void), tree(53, void, void))), 32).
true
*/


%Traversal Methods:

%preorder: go from the root, to left, to right
preorder(tree(N,_L, _R),N).
preorder(tree(_Root,Left,_R),N) :- preorder(Left,N).
preorder(tree(_Root,_L,Right),N) :- preorder(Right,N).

/*
sample test query:
?- preorder(tree(25, tree(16, tree(8, void, void), tree(20, void, void)), tree(44, tree(32, void, void), tree(53, void, void))),N).
N = 25
N = 16
N = 8
N = 20
N = 44
N = 32
N = 53
false
*/


%inorder: go from left, to root, to right
inorder(tree(_Root,Left,_R), N) :- inorder(Left,N).
inorder(tree(N,_L,_R), N).
inorder(tree(_Root,_L,Right), N) :- inorder(Right,N).

/*
sample test query:
?- inorder(tree(25, tree(16, tree(8, void, void), tree(20, void, void)), tree(44, tree(32, void, void), tree(53, void, void))),N).
N = 8
N = 16
N = 20
N = 25
N = 32
N = 44
N = 53
false
*/


%postorder: go from left, to right, to root
postorder(tree(_Root,Left,_R),N) :- postorder(Left,N).
postorder(tree(_Root,_L,Right),N) :- postorder(Right,N).
postorder(tree(N,_L,_R),N).

/*
sample test query:
?- postorder(tree(25, tree(16, tree(8, void, void), tree(20, void, void)), tree(44, tree(32, void, void), tree(53, void, void))),N).
N = 8
N = 20
N = 16
N = 32
N = 53
N = 44
N = 25
false
*/


/*
my sample tree:

         25
       /    \
      /      \
     16      44
    / \      / \
   8   20   32  53

Here are the results we should get from this tree:

preorder:    [25, 16, 8, 20, 44, 32, 53]
inorder:     [8, 16, 20, 25, 32, 44, 53]
postorder:   [8, 20, 16, 32, 53, 44, 25]
*/
