from datetime import datetime
from elasticsearch_dsl import DocType, String, Date
from elasticsearch_dsl.connections import connections

# Define a default Elasticsearch client
connections.create_connection(hosts=['localhost'])

class IncomingFile(DocType):
    file_path = String(analyzer='snowball', fields={'raw': String(index='not_analyzed')})
    uuid = String(analyzer='snowball')
    #tags = String(index='not_analyzed')
    upload_date = Date()

    class Meta:
        index = 'incoming'

    def save(self, ** kwargs):
        return super(IncomingFile, self).save(** kwargs)
