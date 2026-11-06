# Handoff : plateforme de sessions IA partagées (pod par run)

## Contexte
Projet perso, sans lien avec Esker, destiné au CV. Il remplace l'idée initiale de RAG d'actualité politique, abandonnée. Aucun fichier n'a été écrit. Prochaine étape : rédiger la spec avec le skill `out1-specbook`. Le dossier de destination n'est pas choisi. Le répertoire de cette session n'est pas un dépôt.

## Produit
Un serveur où plusieurs utilisateurs rejoignent et reprennent des sessions partagées. Chaque prompt s'exécute dans un **pod Kubernetes éphémère**, avec les secrets de l'**auteur du prompt**.

## Décisions retenues

**Exécution**
- Un run = un pod éphémère. Mode chat par défaut ; outils (shell, fichiers, git) activables par session, par n'importe quel participant.
- Image unique fournie par la plateforme (git, node, python, go).
- Réseau sortant : Internet autorisé, réseau interne du cluster bloqué.
- Un seul run actif par session. Les autres prompts attendent dans une file FIFO visible de tous ; chacun peut retirer son propre prompt.
- Tout participant peut annuler le run en cours.
- Redémarrage du serveur : les runs en cours sont marqués *interrompus*, relancés explicitement par un utilisateur.
- Pas de limite d'usage pour l'instant, seulement l'affichage de l'usage et du coût par auteur.

**Sessions et fichiers**
- Tous les utilisateurs approuvés voient toutes les sessions et leur historique : messages avec auteur, fichiers, détail des appels d'outils (commandes, sorties).
- Un PVC ReadWriteOnce par session (runs sérialisés). Les fichiers sont visibles et téléchargeables, non modifiables hors run.
- Suppression automatique après une durée d'inactivité configurable.

**Accès**
- SSO Google, avec demandes d'accès approuvées ou refusées une par une par un administrateur.

**Providers et secrets**
- Un provider par compte utilisateur (clé API ou abonnement OAuth : ChatGPT, Claude, Copilot). Le modèle est choisi par prompt parmi ceux du provider.
- Secrets de provider chiffrés, jetons OAuth rafraîchis automatiquement. Un **proxy serveur** applique le secret, le pod ne le voit jamais.
- Secret absent, expiré ou rejeté : le run est refusé immédiatement avec un message clair, rien n'est lancé.

**Variables et plugins**
- Map de variables personnelles par utilisateur, chaque entrée marquée secrète ou non. Les valeurs ne sont jamais relues, seulement les noms et le drapeau `secret`.
- Pour les secrets de connexion (ex. token GitHub), l'**auteur sélectionne à chaque prompt** ceux à injecter dans le pod (variable d'environnement), uniquement avec les outils activés.
- Plugins installés depuis un dépôt Git, catalogue **commun** visible et sélectionnable par tous. Agents (system prompts) et skills figés sur un commit par session.
- Agent choisi par session, avec surcharge possible par prompt. Un agent = un system prompt nommé.
- Dépôt privé : accès via une variable secrète de l'utilisateur (ex. `GH_TOKEN`), jamais la clé du provider, sans repli sur un cache.

**Clients**
- Web et mobile à parité complète : créer et reprendre une session, prompts, streaming, voir fichiers et outils.
- Pas de notifications push : un **flux SSE** pour le client lourd et le mobile (run terminé, erreur, question en attente).

## Risques à documenter dans la spec
- L'accès OAuth par abonnement (ChatGPT, Claude, Copilot) est souvent limité aux clients officiels. À valider provider par provider.
- Sans quota, un utilisateur peut monopoliser le cluster ou le coût. Au minimum, prévoir une durée max par run.
- Les sorties d'outils sont visibles de tous : un secret injecté puis affiché par une commande est exposé. Documenter cette frontière de confiance.

## Points encore ouverts
- Format exact de l'abonnement OAuth par provider et du proxy.
- Durée d'inactivité par défaut, durée max par run.
- Stack (Go ou TypeScript, Postgres, NATS ou Redis) non tranchée. La spec doit rester sans implémentation.

## Plan de spec proposé (`spec/`)
- `README.md` : périmètre, exclusions, terminologie (Session, Run, Événement, Auteur, Pod de run, Variables, Plugin).
- `sessions/` : `event-log`, `collaboration` (file FIFO, annulation), `retention`.
- `runs/` : `execution` (pod éphémère, interruption), `streaming-sse`.
- `providers/` : `abstraction`, `oauth-accounts`.
- `security/` : `secrets-proxy`, `variables`, `isolation`.
- `plugins/` : `catalog-and-pinning`.
- `access/` : `sso-and-admission`.
- `usage/` : `attribution-and-cost`.
- `clients/` : `web-and-mobile`.

Chaque capacité suit le format `Rules` puis `Acceptance`, avec les mêmes noms de règles.

## Prompt de reprise suggéré
> Charge le skill `out1-specbook`. Lis le handoff ci-dessus. Rédige `spec/` pour ce projet dans `<chemin à préciser>`, sans implémentation. Pose une question ciblée pour chaque point encore ouvert avant de trancher.
