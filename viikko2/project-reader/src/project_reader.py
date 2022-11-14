from urllib import request
from project import Project
from toml import loads


class ProjectReader:
    def __init__(self, url):
        self._url = url
    
    def list_dependencies(dependencies, self):
        return list(dependencies.keys())


    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        toml_deserialized = loads(content)["tool"]["poetry"]
        print(toml_deserialized)
        dependencies = list(toml_deserialized["dependencies"].keys())
        dev_dependencies = list(toml_deserialized["dev-dependencies"].keys())
        return Project(toml_deserialized["name"], toml_deserialized["description"], dependencies, dev_dependencies)
