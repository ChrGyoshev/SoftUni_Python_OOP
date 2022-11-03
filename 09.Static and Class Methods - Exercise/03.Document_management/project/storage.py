from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self,category:Category):
        category = self.__adding(self.categories,category)
        if category != None:
            self.categories.append(category)

    def add_topic(self,topic:Topic):
        topic = self.__adding(self.topics,topic)
        if topic != None:
            self.topics.append(topic)

    def add_document(self,document:Document):
        document = self.__adding(self.documents, document)
        if document != None:
            self.documents.append(document)

    def __adding(self,entities,entity):
        for data in entities:
            if entity.id == data.id:
                return
        return entity


    def edit_category(self,category_id, new_name):
        for data in self.categories:
            if category_id == data.id:
                data.name = new_name
                return


    def edit_topic(self,topic_id,new_topic,new_storage_folder):
        for data in self.topics:
            if topic_id == data.id:
                data.topic = new_topic
                data.storage_folder = new_storage_folder
                return

    def edit_document(self,document_id, new_file_name):
        for data in self.documents:
            if document_id == data.id:
                data.file_name = new_file_name
                return

    def delete_category(self,category_id):
        category = self.__delete(self.categories,category_id)
        if category != None:
            self.categories.remove(category)

    def delete_topic(self,topic_id):
        topic = self.__delete(self.topics,topic_id)
        if topic != None:
            self.topics.remove(topic)

    def delete_document(self,document_id):
        doc = self.__delete(self.documents,document_id)
        if doc != None:
            self.documents.remove(doc)




    def __delete(self,entities,id):
        for data in entities:
            if id == data.id:
                return data

    def get_document(self,document_id):
        doc = self.__delete(self.documents,document_id)
        if doc!= None:
            return doc


    def __repr__(self):
        for doc in self.documents:
            return doc.__repr__()
