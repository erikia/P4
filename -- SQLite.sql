-- SQLite
CREATE TABLE IF NOT EXISTS players (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Nom_de_famille VARCHAR(150), 
    Prénom VARCHAT(150),
    Date_de_naissance VARCHAT(150),
    Sexe VARCHAT(150),
    Rang INT,
    Numéro_associé SMALLINT,
    Score DECIMAL,
    Adversaires VARCHAT(150)
);

INSERT INTO IF NOT EXISTS players (
        Nom_de_famille,
        Prénom,
        Date_de_naissance,
        Sexe,
        Rang,
        Numéro_associé,
        Score
    ) VALUES (
        'Garry', 
        'Kasparov', 
        '1/06/1967', 
        'Homme', 
        593, 
        3, 
        0
        )
        ,(
        'Judit', 
        'Polgar', 
        '1/06/1967', 
        'Femme', 
        407, 
        4, 
        0
        )
        ,(
        'Fabiano', 
        'Caruana', 
        '15/11/1978', 
        'Homme', 
        57, 
        5, 
        0
        )
        ,(
        'Anish', 
        'Giri', 
        '26/03/2000', 
        'Homme', 
        68, 
        6, 
        0
        )
        ,(
        'Boris', 
        'Spassky', 
        '18/01/1935', 
        'Homme', 
        708, 
        7, 
        0
        )
        ,(
        'Hikaru', 
        'Nakamura', 
        '28/08/1985', 
        'Homme', 
        84, 
        8, 
        0
        );


DROP TABLE IF EXISTs players

SELECT *
FROM players

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS tournaments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Adresse VARCHAR(150), 
    Date VARCHAT(150),
    Totals_Rounds INT,
    Controle_du_temps VARCHAT(150),
    Rounds_en_cours ,
    Rounds_id INTEGER ,
    Joueurs_id INTEGER ,
    Commentaire VARCHAT(150),
    FOREIGN KEY (Rounds_id) REFERENCES rounds(id)
    FOREIGN KEY (Joueurs_id) REFERENCES players(id)
);

CREATE TABLE IF NOT EXISTS matches (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Joueur_1 VARCHAT(150),
    score_joueur_1 INTEGER,
    Joueur_2 VARCHAT(150),
    score_joueur_2 INTEGER
);

CREATE TABLE IF NOT EXISTS rounds (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    matches_id INTEGER,
    FOREIGN KEY (matches_id) REFERENCES macthes(id)
);