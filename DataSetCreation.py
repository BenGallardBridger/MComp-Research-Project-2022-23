from LoadData import loadData

imageFolderLocation = r"C:\Users\benGa\Documents\University\Masters\MComp Research Project\Programming\Dataset\Pictures"
handSkeletonFolderLocation = r"C:\Users\benGa\Documents\University\Masters\MComp Research Project\Programming\Dataset\HandSkeletons"
videoFolderLocation = r"C:\Users\benGa\Documents\University\Masters\MComp Research Project\Programming\Dataset\Videos"
#loadData.loadFromFolders(imageFolderLocation)
#loadData.videoToImages(videoFolderLocation, imageFolderLocation)
loadData.createHandSkeletons(imageFolderLocation, handSkeletonFolderLocation)
