from pathlib import Path


class PathResolver(object):

    @staticmethod
    def project():
        return Path(__file__).parents[1]

    @staticmethod
    def objects():
        return PathResolver.project() / 'objects'

    @staticmethod
    def pages():
        return PathResolver.project() / 'pages'

    @staticmethod
    def model_info():
        return PathResolver.project() / 'model_info'
