# IHM_Groupe5

## Première fois avec GIT ?

Présentation de GIT: https://www.youtube.com/watch?v=rP3T0Ee6pLU

Il existe énormément de ressources en ligne pour apprendre à utiliser Git. Pour les TPs ici vous n'aurez besoin que des bases, mais c'est une très bonne idée d'apprendre à l'utiliser. Vous l'utiliserez quasi-systématiquement dans votre vie de développeur·euse.

## Mise en place de votre repo git

Il faut d'abord créer votre copie du projet _TP IHM PyQt - Groupe5_, copie sur laquelle vous mettrez votre travail.

- Aller sur le projet _TP IHM PyQt - Groupe5_
- Cliquer sur _Forks_ à droite. On arrive sur une page _Fork project_
	- Dans _Project name_, changez le nom du projet pour ajouter votre nom de famille. Par exemple "TP IHM PyQt - Groupe5 - Loizeau"
	- Sous _Project URL_, vous devez choisir le _namespace_: choisissez le vôtre (votre nom)
	- Dans _Visibility level_, choisissez "Private"

Votre repo est créé ! Maintenant, il faut en donner l'accès au·à la professeur·e:

- Aller sur votre copie du projet: "TP IHM PyQt - Groupe5 - VotreNom". Vous devriez y voir un message indiquant que ce projet est issu d'un fork.
- Dans le menu à gauche, aller dans _Manage_ -> _Members_
- Cliquez sur "Invite members" en haute à droite
- Cherchez "Alice Loizeau" et sélectionnez
- Pour _Select a role_, choisissez "Maintainer"
- Cliquez sur _Invite_ pour valider

Normalement le·a professeur·e a maintenant accès à votre repo. Vous pouvez le vérifier en regardant la liste des membres du projet ( _Manage_ -> _Members_).
À présent, pour pouvoir travailler sur votre repo, il faut que vous en ayez une version en local. Pour cela, vous allez **cloner** le repo distant.

- Sur la page de votre projet "TP IHM PyQt - Groupe5 - VotreNom", cliquez sur _Clone_ à droite puis copiez l'url sous _Clone with HTTPS_
- Ouvrez le terminal dans le dossier dans le lequel vous voulez avoir votre projet (ou ouvrez le terminal puis déplacez vous dans le dossier que vous voulez).
- écrivez dans le terminal "git clone " puis collez l'url de votre repo. Faites entrer
- entrez vos identifiants gitlab

Vous avez maintenant votre projet en local !

## Modifications

Vous allez maintenant pouvoir travailler sur le TP. Dans le dossier de votre projet sur votre ordinateur, vous pourrez créer des fichiers et des dossiers et les modifier.

Git vous permet de faire une sauvegarde de chaque état du projet au cours du temps. À chaque fois que vous ajoutez une fonctionnalité à votre projet ou que vous résolvez un bug, vous pouvez enregistrer l'état de votre code. Ce point dans le temps s'appelle un _commit_
Pour ce TP, on vous demande de faire **un commit pour chaque question du TP**

- Faites la première question du TP1 (Vous trouverez le sujet sur le portail du FIL https://www.fil.univ-lille.fr/portail/index.php?dipl=L&sem=S5&ue=IHM&label=Programme -> _cette page_ -> _TP5 : PyQt 1_)
- Sur votre terminal, placez-vous dans votre projet et tapez "git status". Vous devriez voir apparaître la liste des fichiers que vous avez créé et modifié.
- Tapez ensuite "git add " suivi de la liste des fichiers que vous voulez mettre dans votre prochain commit. Si vous voulez ajouter tous les fichiers dernièrement modifiés, tapez "git add ."
- Tapez "git status" à nouveau. Vous voyez apparaître les noms des fichiers modifiés, dont ceux que vous allez ajouter à votre commit.
- Si la liste vous convient, tapez "git commit -m "Message"". Remplacez "message" par ce que vous avez fait dans ce commit. Par exemple "TP1 Question1", "Bug question3 résolu" etc.

Vous avez maintenant créé votre commit, votre point dans le temps de l'état de votre projet. Vous pouvez faire plusieurs commit en local, mais les modifications ne sont enregistrées que sur votre ordinateur, pas sur le serveur. Pour envoyer vos modifications au serveur distant, il vous faut faire un _push_.

- Dans votre terminal, placé dans votre projet, tapez "git status". Vous devriez voir le nombre de commits que vous avez en local.
- Tapez "git push", entrer, puis entrez vos identifiants gitlab.

Si votre push s'est bien passé, vous devriez le voir sur gitlab. Rechargez la page de votre projet sur le gitlab: vous devriez y voir vos fichiers et les commits que vous avez réalisé.
