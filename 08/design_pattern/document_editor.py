class WordDocument:
    def create(self):
        print("Word document created.")

    def get_property(self):
        print("Font, size, color")


class ExcelDocument:
    def create(self):
        print("Excel document created.")

    def get_property(self):
        print("Row, column, cell")


class DocumentEditor:
    document_types = {}

    @classmethod
    def register_document_type(cls, doc_type, doc_class):
        cls.document_types[doc_type] = doc_class

    def new_document(self, doc_type):
        if doc_type in self.document_types:
            return self.document_types[doc_type]()
        else:
            raise ValueError("Unknown document type")


# 각 문서 유형을 등록
DocumentEditor.register_document_type("word", WordDocument)
DocumentEditor.register_document_type("excel", ExcelDocument)


editor = DocumentEditor()
word_doc = editor.new_document("word")
word_doc.create()
word_doc.get_property()


excel_doc = editor.new_document("excel")
excel_doc.create()
excel_doc.get_property()
