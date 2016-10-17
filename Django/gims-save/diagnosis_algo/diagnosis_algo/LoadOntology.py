#!/usr/bin/env python
from __future__ import print_function
from DatabaseConnection import DatabaseConnector
from operator import itemgetter
import math
# package: lca
class LoadOntology(object):

    ontologyMap = None
    ontologyMapChild = None
    ontologyLevels = None
    hpoToDiseaseMap = None
    diseaseToHpoMap = None
    lcaParentMap = None
    rootNode = -1
    totalDiseases = 0
    totalHPOTerms = 0
    totalLevels = 0
    sqrtLevels = 0
    booleanLoadedParent = False
    booleanLoadedChildren = False
    booleanLoadedHPOTerms = False
    booleanLoadedDiseaseTerms = False

    def __init__(self):

        self.ontologyMap = {}
        self.ontologyMapChild = {}
        self.ontologyLevels = {}
        self.hpoToDiseaseMap = {}
        self.diseaseToHpoMap = {}
        self.lcaParentMap = {}
        self.loadChildren()
        self.loadParents()
        self.loadDiseaseToHpo()
        self.loadHpoToDiseases()
        booleanLoadedParent = True
        booleanLoadedChildren = True
        booleanLoadedHPOTerms = True
        booleanLoadedDiseaseTerms = True

    def loadDiseaseToHpo(self):

        dbConnector = DatabaseConnector()
        hpoID = 0
        diseaseID = None
        prevDiseaseID = None
        hpoTermsList = None
        totalDiseases = 0
        try:
            dbConnection = dbConnector.getConnection()
            cursor = dbConnection.cursor()
            sql = "select t.id, eod.disease_id FROM term t, annotation a, external_object_disease eod " + " WHERE t.id = a.term_id AND a.external_object_disease_id = eod.external_object_id AND " + " t.subontology = 'O' AND t.is_obsolete = 0 " + " order by eod.disease_id "
            cursor.execute(sql)

            for results in cursor:
                hpoID = results[0]
                diseaseID = results[1]
                if not (diseaseID == prevDiseaseID):
                    if not (prevDiseaseID is None):
                        self.diseaseToHpoMap[prevDiseaseID] = hpoTermsList
                    hpoTermsList = []
                    prevDiseaseID = diseaseID
                    totalDiseases += 1
                if hpoTermsList != None:
                    hpoTermsList.append(hpoID)

            if diseaseID != None and hpoTermsList != None:
                self.diseaseToHpoMap[diseaseID] = hpoTermsList
            print("Total diseases = ")
            print(totalDiseases)
            self.totalDiseases = totalDiseases
        except Exception as ex:
            raise ex

    def loadHpoToDiseases(self):

        dbConnector = DatabaseConnector()
        hpoID = 0
        diseaseID = None
        prevHpoID = -1
        diseaseList = None
        totalDiseases = 0
        try:
            dbConnection = dbConnector.getConnection()
            cursor = dbConnection.cursor()
            sql = "select t.id, eod.disease_id FROM term t, annotation a, external_object_disease eod " + " WHERE t.id = a.term_id AND a.external_object_disease_id = eod.external_object_id AND " + " t.subontology = 'O' AND t.is_obsolete = 0 " + " order by t.id "
            cursor.execute(sql)

            for results in cursor:
                hpoID = results[0]
                diseaseID = results[1]
                if hpoID != prevHpoID:
                    if prevHpoID != -1:
                        self.hpoToDiseaseMap[prevHpoID]=  diseaseList
                    diseaseList = []
                    prevHpoID = hpoID
                if diseaseList != None:
                    diseaseList.append(diseaseID)
                totalDiseases += 1


            if hpoID != 0 and diseaseList != None:
                self.hpoToDiseaseMap[hpoID] = diseaseList
            #print("Total diseases = " + totalDiseases);
        except Exception as ex:
            raise ex

    def loadChildren(self):

        dbConnector = DatabaseConnector()
        hpoID = 0
        hpoChildID = 0
        is_root = 0
        prevHpoID = -1
        childList = None
        totalHPOTerms = 0
        recordsRetrieved = 0
        try:
            dbConnection = dbConnector.getConnection()
            sql = "select t.id, t.name, t.acc, t.is_root, t2t.term2_id FROM term t, term2term t2t " + " WHERE t.id = t2t.term1_id AND " + " t.subontology = 'O' AND t.is_obsolete = 0 " + " order by t.id "
            cursor = dbConnection.cursor()
            cursor.execute(sql)
            for results in cursor:
                hpoID = results[0]
                hpoChildID = results[4]
                is_root = results[3]
                if is_root == 1:
                    self.rootNode = hpoID
                if hpoID != prevHpoID:
                    # Previous HPO term exists and needs to be inserted into HashMap
                    if recordsRetrieved != 0 & prevHpoID != -1:
                        if childList != None:
                            self.ontologyMapChild[prevHpoID] = childList
                    # new HPO ID in the sorted list of HPO ID's so create a new list of parents
                    childList = []
                    prevHpoID = hpoID
                # add the new Parent to the existing list of parents
                if childList != None:
                    childList.append(hpoChildID)
                recordsRetrieved += 1
                totalHPOTerms += 1
            # finally add the last HPOid and its parents to the HashMap
            if hpoID != 0 and childList != None:
                self.ontologyMapChild[hpoID] = childList
            print("Root HPO Node = ")
            print (self.rootNode)
            print("Total Hpo Terms in Child  = ")
            print(totalHPOTerms)
        except Exception as e:
            #  TODO Auto-generated catch block
           print(e)

    def loadParents(self):

        dbConnector = DatabaseConnector()
        hpoID = 0
        hpoParentID = 0
        is_root = 0
        prevHpoID = -1
        parentsList = None
        totalHPOTerms = 0
        recordsRetrieved = 0
        try:
            dbConnection = dbConnector.getConnection()
            sql = "select t.id, t.name, t.acc, t.is_root, t2t.term1_id FROM term t, term2term t2t " + " WHERE t.id = t2t.term2_id AND " + " t.subontology = 'O' AND t.is_obsolete = 0 " + " order by t.id "
            cursor = dbConnection.cursor()
            cursor.execute(sql)

            for results in cursor:
                hpoID = results[0]
                hpoParentID = results[4]
                if hpoID != prevHpoID:
                    # Previous HPO term exists and needs to be inserted into HashMap
                    if recordsRetrieved != 0 & prevHpoID != -1:
                        if parentsList != None:
                            self.ontologyMap[prevHpoID] =  parentsList
                    # new HPO ID in the sorted list of HPO ID's so create a new list of parents
                    parentsList = []
                    prevHpoID = hpoID
                # add the new Parent to the existing list of parents
                if parentsList != None:
                    parentsList.append(hpoParentID)
                recordsRetrieved += 1
                totalHPOTerms += 1
            # finally add the last HPOid and its parents to the HashMap
            if hpoID != 0 and parentsList != None:
                self.ontologyMap[hpoID] =  parentsList
            print("Total Hpo Terms = ")
            print(totalHPOTerms)
        except Exception as e:
            print(e)

    def getInformationContent(self, node):

        ic = 0
        if node == self.rootNode or node not in self.ontologyMap:
            return ic
        if self.totalDiseases == 0:
            raise Exception("Invalid Ontology - Total number of diseases is zero")
        listedDisease = self.hpoToDiseaseMap.get(node)
        if listedDisease == None or len(listedDisease) == 0:
            return ic
        print(" total diseases = " )
        print(len(listedDisease))
        if len(listedDisease) > self.totalDiseases:
            raise Exception("Invalid Ontology - Disease associated for listed HPO term is greater than total number of Diseases/Disorder in Ontology")
        ic = -1 * math.log(float(len(listedDisease)) / self.totalDiseases)
        return ic

    #
    # 	 *
    #
    def getDiseaseFromHPO(self, hpoID):
        """ generated source for method getDiseaseFromHPO """
        listedDisease = None
        listedDisease = self.hpoToDiseaseMap.get(hpoID)
        return listedDisease

    def getSortedDiseaseList(self, queryHpoList):

        sum = 0
        totalQueryTerms = 0
        maxIC = -1.0
        ic = 0
        lca = -1
        avgQDScore = 0.0
        currentQueryHpoID = 0
        currentDiseaseHpoID = 0
        diseaseID = None
        diseaseHpoList = None
        unsortedDiseaseList = {}
        if queryHpoList == None or not queryHpoList:
            return unsortedDiseaseList
        # get disease list for all HPO terms
        diseaseList = self.getDiseaseListFromHpoList(queryHpoList)
        # loop through all possible disease id
        #diseaseIterator = diseaseList.iterator()
        #diseaseHpoIterator = None
        for diseaseID in diseaseList:
            #diseaseID = diseaseIterator.next()
            diseaseHpoList = self.diseaseToHpoMap.get(diseaseID)
            # reset summary variables
            sum = 0
            totalQueryTerms = 0
            #queryHpoIterator = queryHpoList.iterator()
            for currentQueryHpoID in queryHpoList :
                totalQueryTerms += 1
                #currentQueryHpoID = queryHpoIterator.next()
                # get HPO terms associated with diseaseID
                # there has to be alteast one HPO term for all diseases in the list as we retrieved disease by HPO term
                #diseaseHpoIterator = diseaseHpoList.iterator()
                for currentDiseaseHpoID in diseaseHpoList:
                    #currentDiseaseHpoID = diseaseHpoIterator.next()
                    # calcuate the least common ancestor of the two HPO terms and then calculate the IC
                    lca = self.computeLCA(currentQueryHpoID, currentDiseaseHpoID)
                    ic = self.getInformationContent(lca)
                    # find max IC
                    if ic > maxIC:
                        maxIC = ic
                sum += maxIC
            avgQDScore = sum / totalQueryTerms
            #diseaseScore = DiseaseScore(diseaseID, avgQDScore)
            unsortedDiseaseList[diseaseID] = avgQDScore

        #Collections.sort(sortedDiseaseList)
        sortedDiseaseList = sorted(unsortedDiseaseList.items(), key=itemgetter(1))
        return sortedDiseaseList

    def getDiseaseListFromHpoList(self, hpoList):
        """ generated source for method getDiseaseListFromHpoList """
        listedDisease = []
        tempDiseaseList = None
        if hpoList == None or not hpoList:
            return None

        for counter in hpoList:
            tempDiseaseList = self.getDiseaseFromHPO(counter)
            if tempDiseaseList != None:
                listedDisease.extend(tempDiseaseList);

        return listedDisease

    def getHpoFromDisease(self, diseaseID):
        """ generated source for method getHpoFromDisease """
        hpoList = None
        if diseaseID == None:
            return None
        hpoList = self.diseaseToHpoMap.get(diseaseID)
        return hpoList

    def getHpoFromDiseaseList(self, diseaseIDList):
        """ generated source for method getHpoFromDiseaseList """
        hpoList = []
        diseaseID = None
        hpoID = 0
        tempList = None
        if diseaseIDList == None or not diseaseIDList:
            return None
        size = 0
        for diseaseID in diseaseIDList:
            #diseaseID = diseaseIDList.get(size)
            tempList = self.diseaseToHpoMap.get(diseaseID)
            if tempList != None:
                hpoList.extend(tempList)
            size += 1
        return hpoList

    def computeLCA(self, node1, node2):
        """ generated source for method computeLCA """
        lcaNode = self.rootNode
        parentNode = 0
        currentNode = 0
        visitedNodesMap = {}
        parentsList = None
        currentList = None
        parentExists = False
        allParentsList = []
        # first traverse from node1 to the root and mark all visited nodes
        if not node1 in self.ontologyMap:
            raise Exception("Invalid Node doesn't exist in DAG : " + node1)
        if not node2 in self.ontologyMap:
            raise Exception("Invalid Node doesn't exist in DAG : " + node2)
        visitedNodesMap[node1] = 1
        # start with the node1
        parentsList = self.ontologyMap.get(node1)
        if parentsList != None:
            size = 0
            for parentNode in parentsList:
                #parentNode = parentsList.get(size)
                visitedNodesMap[parentNode] = 1
                # set all parents as visited node on the way to root
                allParentsList.append(parentNode)
                if parentNode in self.ontologyMap:
                    parentExists = True

            while parentExists:
                currentList = allParentsList
                parentExists = False
                allParentsList = []
                #size = 0
                for currentNode in currentList:
                    #currentNode = currentList.get(size)
                    parentsList = self.ontologyMap.get(currentNode)
                    if parentsList != None:
                        #i = 0
                        for parentNode in parentsList:
                            #parentNode = parentsList.get(i)
                            allParentsList.append(parentNode)
                            visitedNodesMap[parentNode] = 1
                            if parentNode in self.ontologyMap:
                                parentExists = True


        # now start with node2
        parentExists = False
        if node2 in visitedNodesMap:
            lcaNode = node2
        else:
            parentsList = self.ontologyMap.get(node2)
            allParentsList = []
            if parentsList != None:
                #size = 0
                for parentNode in parentsList:
                    #parentNode = parentsList.get(size)
                    if parentNode in visitedNodesMap:
                        lcaNode = parentNode
                        return lcaNode
                    allParentsList.append(parentNode)
                    if parentNode in self.ontologyMap:
                        parentExists = True

                while parentExists:
                    currentList = allParentsList
                    parentExists = False
                    allParentsList = []
                    #size = 0
                    for currentNode in currentList:
                        #currentNode = currentList.get(size)
                        parentsList = self.ontologyMap.get(currentNode)
                        if parentsList != None:

                            for parentNode in parentsList:
                                #parentNode = parentsList.get(i)
                                allParentsList.append(parentNode)
                                if parentNode in visitedNodesMap:
                                    lcaNode = parentNode
                                    return lcaNode
                                if parentNode in self.ontologyMap:
                                    parentExists = True


        return lcaNode

    @classmethod
    def main(cls, args):

        loader = LoadOntology()
        #loader.loadParents()
        #loader.loadChildren()
        #try:
        #    loader.loadDiseaseToHpo()
        #except Exception as e1:
        #
        #     print(e1)
        # try:
        #     loader.loadHpoToDiseases()
        # except Exception as e1:
        #
        #     print(e1)

        #loader.totalDiseases = len(loader.diseaseToHpoMap)
        loader.rootNode = 118
        # loader.totalLevels = loader.findNumberLevels(loader.rootNode);
        print( loader.totalLevels)
        print(len(loader.ontologyLevels))
        print( len(loader.hpoToDiseaseMap))
        print( len(loader.diseaseToHpoMap))
        try:
            lca = loader.computeLCA(2813, 2813)
            print("LCA is " )
            print( lca)
            ic = loader.getInformationContent(lca)
            print("Information Content of LCA is ")
            print( ic)
            queryTermsList = []
            queryTermsList.append(2817)
            queryTermsList.append(100570)
            sortedDisease = loader.getSortedDiseaseList(queryTermsList)
            if (sortedDisease != None):
               for key in sortedDisease:
                    print(key)

        except Exception as e:
            print(e)



if __name__ == '__main__':
    import sys
    LoadOntology.main(sys.argv)

