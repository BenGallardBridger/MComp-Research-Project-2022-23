from LoadData import loadData

<<<<<<< HEAD
imageFolderLocation = r"C:\Users\benGa\Documents\University\Masters\MComp Research Project\Programming Repo\MComp-Research-Project-2022-23\Data\Pictures"
handSkeletonFolderLocation = r"C:\Users\benGa\Documents\University\Masters\MComp Research Project\Programming Repo\MComp-Research-Project-2022-23\Data\Handskeletons"
videoFolderLocation = r"C:\Users\benGa\Desktop\Testing Dataset\Videos"
#loadData.videoToImages(videoFolderLocation, imageFolderLocation)

#loadData.loadFromFolders(imageFolderLocation)

=======
imageFolderLocation = r"C:\Users\benGa\Documents\University\Masters\MComp Research Project\Programming\Dataset\Pictures"
handSkeletonFolderLocation = r"C:\Users\benGa\Documents\University\Masters\MComp Research Project\Programming\Dataset\HandSkeletons"
videoFolderLocation = r"C:\Users\benGa\Documents\University\Masters\MComp Research Project\Programming\Dataset\Videos"
#loadData.loadFromFolders(imageFolderLocation)
#loadData.videoToImages(videoFolderLocation, imageFolderLocation)
>>>>>>> parent of 522e694b (Upload new dataset)
loadData.createHandSkeletons(imageFolderLocation, handSkeletonFolderLocation)
