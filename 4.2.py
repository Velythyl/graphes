class Node:
    def __init__(self, ID):
        self.id = ID
        self.edges = set()  # les sommets adjancents du sommet est un ensemble car G est simple

    def link(self, node):
        # G est simple et non-orienté, donc losqu'on lie deux sommets on doit ajouter un dans
        # la liste d'arêtes de l'autre et vice-versa
        self.edges.add(node)
        node.edges.add(self)

    def __str__(self):
        return self.id


V = list()  # Liste des sommets V
U = list()  # Liste des sommets U
for i in range(5):
    V.append(Node("v" + str(i)))
    U.append(Node("u" + str(i)))

for i in range(5):
    V[i].link(U[i])  # {u_i v_i | i=0,1,2,3,4}
    U[i].link(U[(i + 1) % 5])  # {u_i u_i+1 | i=0,1,2,3,4 add mod 5}
    V[i].link(V[(i + 2) % 5])  # {v_i v_i+2 | i=0,1,2,3,4 add mod 5}


# Cherche un cycle hamiltonien à partir d'un sommet
def seek(node, visited):
    if all(node in visited for node in (U + V)) and node == visited[0]:
        # Si on a visité tous les sommets et qu'on
        # parvient au premier sommet de la liste des sommets visités à partir du dernier, on a le cycle voulu
        return visited

    if node in visited:
        # Sinon, si le sommet est déjà visité, ce chemin d'arêtes de même pas à un cycle hamiltonien
        # par def.
        return None

    visited = visited + [node]  # On ajoute le sommet à l'étude aux sommets visités

    for edge in node.edges:  # Pour chaque sommet adjacent au sommet à l'étude
        # On cherche un cycle hamiltonien à partir du prochain sommet (ne pas oublier que
        # visited contient maintenant le sommet "node"
        res = seek(edge, visited)
        if res != None:
            # Si res n'est pas None, c'est qu'on a retourné une liste, et ça arrive seulement lorsqu'on a
            # trouvé un cycle!
            return res

    return None  # Si on a jamais trouvé de cycle à partir de "node" (dans la for-loop), on l'indique


def is_hamil(visited):
    print(visited)
    print("G est hamiltonien")
    exit()


def isnt_hamil():
    print("G n'est pas hamiltonien")


for i in range(5):  # Pour tous les sommets
    u_seek = seek(U[i], []) # On fait la recherche
    v_seek = seek(V[i], [])

    if u_seek != None:  # Si elle réussie, on l'indique et on quitte le programme
        is_hamil(u_seek)
    if v_seek != None:
        is_hamil(v_seek)

isnt_hamil()    # Si aucun sommet n'a eu de recherche non-nulle, on n'a pas de cycle hamiltonien.
