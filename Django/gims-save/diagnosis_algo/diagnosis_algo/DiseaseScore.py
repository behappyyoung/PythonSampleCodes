#!/usr/bin/env python
""" generated source for module DiseaseScore """
from __future__ import print_function
# package: lca
class DiseaseScore():

    diseaseID = None
    score = 0

    def __init__(self, diseaseID, score):

        super(DiseaseScore, self).__init__()
        self.diseaseID = diseaseID
        self.score = score

    def getDiseaseID(self):

        return self.diseaseID

    def getScore(self):
        
        return self.score

