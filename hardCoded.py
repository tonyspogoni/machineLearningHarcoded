from sklearn import datasets
import random
iris = datasets.load_iris()

#print(iris.target_names)





class HardCoded:
    irisD = iris.data
    irisT = iris.target


    irisD = irisD.tolist()
    irisT = irisT.tolist()



    irisDict = dict(zip(range(150), irisD))


    def train(irisD, irisT):
        return 0

    def predict(irisD):
            print 'setosa'

    def results(irisDict):
        i = 0
        for key in irisDict:
            if key < 50:
                i += 1
                y = 100 * (float(i)/float(150))
        print y, 'percent are correct'


    train(irisDict.values(), irisDict.keys())
    predict(irisDict.values())
    results(irisDict)
