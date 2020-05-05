import os


class CreateFolder:
    base = r'/Users/samirotmani/Desktop/Test Ajout Film'
    base.replace('\\', '/')

    def cree_doss(self, user):
        dossier = '{0}/{1}-{2}'.format(self.base, user.name, user.Id)
        if os.path.isdir(dossier):
            print("ton dossier est deja present et c'est le suivant {0}".format(dossier))
        else:
            os.makedirs(dossier)
            print('Creation du dossier {0}'.format(dossier))
