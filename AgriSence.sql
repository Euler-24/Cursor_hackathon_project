DROP DATABASE IF EXISTS `agrisence`;
CREATE DATABASE IF NOT EXISTS `agrisence`
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;
USE `agrisence`;

CREATE TABLE IF NOT EXISTS `utilisateur` (
    id_utilisateur INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    prenom VARCHAR(100) NOT NULL,
    telephone VARCHAR(30) NOT NULL UNIQUE,
    email VARCHAR(150) NULL UNIQUE,
    mot_de_passe_hash VARCHAR(255) NOT NULL,
    role VARCHAR(30) NOT NULL,
    date_inscription DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS `exploitation` (
    id_exploitation INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(150) NOT NULL,
    localisation VARCHAR(255) NOT NULL,
    latitude DECIMAL(10,7) NULL,
    longitude DECIMAL(10,7) NULL,
    superficie DECIMAL(10,2) NULL,
    id_utilisateur INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_utilisateur) REFERENCES utilisateur(id_utilisateur)
);

CREATE TABLE IF NOT EXISTS `culture` (
    id_culture INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL UNIQUE,
    description TEXT NULL
);

CREATE TABLE IF NOT EXISTS `parcelle` (
    id_parcelle INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(100) NOT NULL,
    superficie DECIMAL(10,2) NOT NULL,
    date_plantation DATE NULL,
    id_exploitation INT UNSIGNED NOT NULL,
    id_culture INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_exploitation) REFERENCES exploitation(id_exploitation),
    FOREIGN KEY (id_culture) REFERENCES culture(id_culture)
);

CREATE TABLE IF NOT EXISTS `diagnostic` (
    id_diagnostic INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    date_diagnostic DATETIME NOT NULL,
    url_image VARCHAR(500) NULL,
    description_symptomes TEXT NULL,
    statut VARCHAR(30) NOT NULL,
    id_parcelle INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_parcelle) REFERENCES parcelle(id_parcelle)
);

CREATE TABLE IF NOT EXISTS `maladie` (
    id_maladie INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(150) NOT NULL UNIQUE,
    description_maladie TEXT NULL,
    symptomes TEXT NULL,
    gravite VARCHAR(30) NULL
);

CREATE TABLE IF NOT EXISTS `resultat_diagnostic` (
    id_resultat INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    id_diagnostic INT UNSIGNED NOT NULL,
    id_maladie INT UNSIGNED NOT NULL,
    score_confiance DECIMAL(5,2) NULL,
    rang TINYINT UNSIGNED NULL,
    est_retenu BOOLEAN DEFAULT FALSE,
    FOREIGN KEY (id_diagnostic) REFERENCES diagnostic(id_diagnostic),
    FOREIGN KEY (id_maladie) REFERENCES maladie(id_maladie)
);

CREATE TABLE IF NOT EXISTS `recommandation` (
    id_recommandation INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    titre VARCHAR(200) NOT NULL,
    contenu TEXT NOT NULL,
    niveau_urgence VARCHAR(30) NULL,
    id_maladie INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_maladie) REFERENCES maladie(id_maladie)
);

CREATE TABLE IF NOT EXISTS `marche` (
    id_marche INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(150) NOT NULL,
    localisation VARCHAR(255) NOT NULL,
    latitude DECIMAL(10,7) NULL,
    longitude DECIMAL(10,7) NULL
);

CREATE TABLE IF NOT EXISTS `prix` (
    id_prix INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    prix DECIMAL(12,2) NOT NULL,
    unite VARCHAR(50) NOT NULL,
    devise VARCHAR(10) NOT NULL,
    date_releve DATE NOT NULL,
    source VARCHAR(255) NULL,
    id_marche INT UNSIGNED NOT NULL,
    id_culture INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_marche) REFERENCES marche(id_marche),
    FOREIGN KEY (id_culture) REFERENCES culture(id_culture)
);

CREATE TABLE IF NOT EXISTS `zone_meteo` (
    id_zone INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(150) NOT NULL,
    latitude DECIMAL(10,7) NULL,
    longitude DECIMAL(10,7) NULL
);

CREATE TABLE IF NOT EXISTS `prevision_meteo` (
    id_prevision INT UNSIGNED PRIMARY KEY AUTO_INCREMENT,
    date_prevision DATE NOT NULL,
    temperature_min DECIMAL(5,2) NULL,
    temperature_max DECIMAL(5,2) NULL,
    humidite DECIMAL(5,2) NULL,
    probabilite_pluie DECIMAL(5,2) NULL,
    quantite_pluie DECIMAL(8,2) NULL,
    id_zone INT UNSIGNED NOT NULL,
    FOREIGN KEY (id_zone) REFERENCES zone_meteo(id_zone)
);
