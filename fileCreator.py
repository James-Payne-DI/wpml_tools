import os.path,csv

#creates a .csv file on the Desktop and exports the data there
def createCSV(save_path,name_of_file,translationList):

    name_of_file = name_of_file.replace(" ","-")
    completeName = os.path.join(save_path, name_of_file+".csv")

    

    with open(completeName, mode='a+') as translation_list:
        
        translation_writer = csv.writer(translation_list, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        #assigns the top level field names to the csv file
        field_names = ["English Title","English Slug","Spanish Title","Spanish Slug"]
        translation_writer.writerow(field_names)

        #adds all the translation arrays from the translationList array which is passed in as a parameter
        for translation in translation_list:
            translation_writer.writerow(translation)
        #completeName.close()

    print("Data Added to File")


save_path = '/Users/jimmypayne/Documents/wpml_translation_files'
name_of_file = input("What is the name of the dealership: ")
translationList = [["English Title","English Slug","Spanish Title","Spanish Slug"],
               ["English Title","English Slug","Spanish Title","Spanish Slug"],
               ["English Title","English Slug","Spanish Title","Spanish Slug"],
               ["English Title","English Slug","Spanish Title","Spanish Slug"],
               ["English Title","English Slug","Spanish Title","Spanish Slug"]]

createCSV(save_path,name_of_file,translationList)
