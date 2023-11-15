from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        for c in self.categories:
            if c.id == int(category_id):
                c.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for t in self.topics:
            if t.id == int(topic_id):
                t.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        for d in self.documents:
            if d.id == int(document_id):
                d.edit(new_file_name)

    """We can write the edit and delete methods using generators and staticmethod"""
    # @staticmethod
    # def __find_object(object_id, object_collection):
    #     return next((o for o in object_collection if o.id == object_id), None)
    #
    # def edit_category(self, category_id: int, new_name: str):
    #     category = self.__find_object(category_id, self.categories)
    #     if category:
    #         category.edit(new_name)
    #
    # def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
    #     topic = self.__find_object(topic_id, self.topics)
    #     if topic:
    #         topic.edit(new_topic, new_storage_folder)
    #
    # def edit_document(self, document_id: int, new_file_name: str):
    #     document = self.__find_object(document_id, self.documents)
    #     if document:
    #         document.edit(new_file_name)

    # def edit_category(self, category_id: int, new_name: str):
    #     category = self.__find_object(category_id, self.categories)
    #     if category:
    #         self.categories.remove(category)
    #
    # def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
    #     topic = self.__find_object(topic_id, self.topics)
    #     if topic:
    #         self.topics.remove(topic)
    #
    # def edit_document(self, document_id: int, new_file_name: str):
    #     document = self.__find_object(document_id, self.documents)
    #     if document:
    #         self.documents.remove(document)

    def delete_category(self, category_id):
        self.categories = [c for c in self.categories if c.id != category_id]

    def delete_topic(self, topic_id):
        self.topics = [t for t in self.topics if t.id != topic_id]

    def delete_document(self, document_id):
        self.documents = [d for d in self.documents if d.id != document_id]

    def get_document(self, document_id):
        for d in self.documents:
            if d.id == int(document_id):
                return d

    def __repr__(self):
        result = "\n".join([d.__repr__() for d in self.documents])
        return result
