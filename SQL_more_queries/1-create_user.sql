-- Créer l'utilisateur avec un mot de passe, sans échouer s'il existe déjà
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Accorder tous les privilèges sur toutes les bases de données et les tables avec l'option GRANT
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;

-- Rafraîchir les privilèges pour s'assurer que les changements prennent effet immédiatement
FLUSH PRIVILEGES;
