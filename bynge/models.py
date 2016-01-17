from elasticsearch_dsl import DocType, String, Date


class IncomingFile(DocType):
    file_path = String(analyzer='snowball', fields={'raw': String(index='not_analyzed')})
    uuid = String(analyzer='snowball')
    processed = String(analyzer='snowball')
    process_date = Date()
    upload_date = Date()

    class Meta:
        index = 'bynge'

    def save(self, ** kwargs):
        return super(IncomingFile, self).save(** kwargs)


class AudioFile(DocType):
    file_path = String(analyzer='snowball', fields={'raw': String(index='not_analyzed')})
    uuid = String(analyzer='snowball')
    type = String(analyzer='standard')
    runtime = String(analyzer='standard')
    artist = String(analyzer='standard')
    title = String(analyzer='standard')
    album = String(analyzer='standard')
    year = String(analyzer='standard')
    composer = String(analyzer='standard')
    genre = String(analyzer='standard')
    comment = String(analyzer='standard')
    track = String(analyzer='standard')
    lossless = String(analyzer='standard')
    bitrate = String(analyzer='standard')
    encoder = String(analyzer='standard')
    faulty = String(analyzer='standard')
    lyrics = String(analyzer='standard')
    tabs = String(analyzer='standard')
    cover = String(analyzer='standard')
    live = String(analyzer='standard')
    tags = String(index='not_analyzed')
    entry_date = Date()

    class Meta:
        index = 'bynge'

    def save(self, ** kwargs):
        return super(AudioFile, self).save(** kwargs)


class ApiUser(DocType):
    username = String(analyzer='snowball', fields={'raw': String(index='not_analyzed')})
    password = String(index='not_analyzed')
    groups = String(analyzer='standard')
    entry_date = Date()

    class Meta:
        index = 'bynge'

    def save(self, ** kwargs):
        return super(ApiUser, self).save(** kwargs)