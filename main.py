import json
import os

with open("v1.json", encoding="utf-8") as jsonFile:
    data = json.load(jsonFile)
    print(data.keys())

    domainClusterModel = data['ares_domainclustermodel']
    domainModel = data['ares_domainmodel']
    storyModel = data['ares_storymodel']
    substoryModel = data['ares_substorymodel']
    nodeModel = data['ares_nodemodel']
    stepResponseModel = data['ares_stepresponsemodel']
    nodePriorityModel = data['ares_nodeprioritymodel']
    bucketModel = data["ares_bucketmodel"]
    phraseModel = data["ares_phrasemodel"]
    sentenceSimilarityModel = data["ares_sentencesimilaritymodel"]
    entityTypeV2 = data["ares_entitytypev2"]
    globalEntityModel = data["ares_globalentitymodel"]
    nodeEntityModel = data["ares_nodeentitymodel"]
    genericResponseV2 = data["ares_genericresponsev2"]
    responseModel = data["ares_responsemodel"]
    nodeTraversalModel = data["ares_nodetraversalmodel"]

    with open(os.path.join("generations","domainClusterModel.json"),"w") as domainClusterModelFile:
        json.dump(domainClusterModel, domainClusterModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","domainModel.json"),"w") as domainModelFile:
        json.dump(domainModel, domainModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","storyModel.json"),"w") as storyModelFile:
        json.dump(storyModel, storyModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","substoryModel.json"),"w") as substoryModelFile:
        json.dump(substoryModel,substoryModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","nodeModel.json"),"w") as nodeModelFile:
        json.dump(nodeModel,nodeModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","stepResponseModel.json"),"w") as stepResponseModelFile:
        json.dump(stepResponseModel,stepResponseModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","nodePriorityModel.json"),"w") as nodePriorityModelFile:
        json.dump(nodePriorityModel,nodePriorityModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","bucketModel.json"),"w") as bucketModelFile:
        json.dump(bucketModel,bucketModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","phraseModel.json"),"w") as phraseModelFile:
        json.dump(phraseModel, phraseModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","sentenceSimilarityModel.json"),"w") as sentenceSimilarityModelFile:
        json.dump(sentenceSimilarityModel,sentenceSimilarityModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","entitytypev2.json"),"w") as entityTypeV2File:
        json.dump(entityTypeV2, entityTypeV2File, indent=4, sort_keys=True)

    with open(os.path.join("generations","globalEntityModel.json"),"w") as globalEntityModelFile:
        json.dump(globalEntityModel,globalEntityModelFile, indent=4, sort_keys=True) 

    with open(os.path.join("generations","nodeEntityModel.json"),"w") as nodeEntityModelFile:
        json.dump(nodeEntityModel,nodeEntityModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","genericResponseV2.json"),"w") as genericResponseV2File:
        json.dump(genericResponseV2,genericResponseV2File, indent=4, sort_keys=True)

    with open(os.path.join("generations","responseModel.json"),"w") as responseModelFile:
        json.dump(responseModel, responseModelFile, indent=4, sort_keys=True)

    with open(os.path.join("generations","nodeTraversalModel.json"),"w") as nodeTraversalModelFile:
        json.dump(nodeTraversalModel,nodeTraversalModelFile, indent=4, sort_keys=True) 