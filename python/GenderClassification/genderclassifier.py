from sklearn import tree 
#submodule tree helps in building a decision tree
#Decision tree is like a flowchart that stores data. 
#It asks each LABELLED data point it recieves a yes/no question
#Data moves in different directions based on answers
#Decision tree builds every node in the tree the more data points it recieves.
#Then an unlabelled dat point can be fed to the tree. It asks for a series of questions, until it labels it.
#That label is the classification.
#The more data we train it on the more accurate the classification is


#[height,wight,shoe size]

X = [[180,80,44],[177,70,43],[160,60,38], [154,54,37],
     [166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],
     [171,75,42],[181,85,43]]
#X here is a list data type. Each value is a list itself that contains 3 numbers. Our dataset size here is 11 people.


Y = ['male','female','female','female',
     'male','male','male','female','male',
     'female','male']
#Y stores a list of labels and each label is a gender & is associated with metric in the previous list
#Labels are written as strings, a data type used to represent text


clf = tree.DecisionTreeClassifier()
#clf is a variable thagt sgtores gthe decision tree model. DecisionTree method called on the tree object


clf = clf.fit(X, Y)
#Training tree varibale on our dataset. Fit method calle don the classifier variable
#Fit method traisn the decision tree on our dataset

prediction = clf.predict([[150,60,40]])

print (prediction)

print(tree.export_graphviz(clf, out_file='tree.png'))