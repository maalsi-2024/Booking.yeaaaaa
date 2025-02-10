# Nuxt Minimal Starter

Look at the [Nuxt documentation](https://nuxt.com/docs/getting-started/introduction) to learn more.

## Setup

Make sure to install dependencies:

```bash
# npm
npm install

# pnpm
pnpm install

# yarn
yarn install

# bun
bun install
```

## Development Server

Start the development server on `http://localhost:3000`:

```bash
# npm
npm run dev

# pnpm
pnpm dev

# yarn
yarn dev

# bun
bun run dev
```

## Production

Build the application for production:

```bash
# npm
npm run build

# pnpm
pnpm build

# yarn
yarn build

# bun
bun run build
```

Locally preview production build:

```bash
# npm
npm run preview

# pnpm
pnpm preview

# yarn
yarn preview

# bun
bun run preview
```

Check out the [deployment documentation](https://nuxt.com/docs/getting-started/deployment) for more information.


# Installation et Configuration : MySQL, MongoDB et Exportation des Données

## Prérequis
- **Windows / Linux / macOS**
- **MySQL Server & Workbench**
- **MongoDB Community Edition**
- **PHPMyAdmin**
- **Node.js et npm**

---

## 1. Installation de MySQL
### **1.1 Télécharger et Installer MySQL**
- Téléchargez [MySQL Community Server](https://dev.mysql.com/downloads/mysql/).
- Installez en mode serveur.
- Notez le port (par défaut **3306**, changez-le si nécessaire).
- Définissez un mot de passe root.

### **1.2 Configuration MySQL**
- Modifiez le fichier de configuration `my.ini` (Windows) ou `mysqld.cnf` (Linux) :
  ```ini
  bind-address = 0.0.0.0
  port = 3309  # Si 3306 est occupé
  ```
- Redémarrez MySQL :
  ```bash
  sudo systemctl restart mysql  # Linux
  net stop MySQL80 && net start MySQL80  # Windows
  ```

### **1.3 Création de l'utilisateur MySQL**
- Connectez-vous à MySQL :
  ```bash
  mysql -u root -p
  ```
- Créez un utilisateur `aux_user` :
  ```sql
  CREATE USER 'aux_user'@'%' IDENTIFIED BY 'secure_password';
  GRANT ALL PRIVILEGES ON *.* TO 'aux_user'@'%';
  FLUSH PRIVILEGES;
  ```

### **1.4 Vérifier la Connexion avec MySQL Workbench**
- Ajoutez une nouvelle connexion avec `host: localhost`, `port: 3309`, `user: aux_user`, `password: secure_password`.
- Testez la connexion.

---

## 2. Installation de MongoDB
### **2.1 Télécharger et Installer MongoDB**
- Téléchargez [MongoDB Community Edition](https://www.mongodb.com/try/download/community).
- Installez-le et démarrez `mongod`.

### **2.2 Création de la base et des collections**
- Ouvrez un terminal et tapez :
  ```bash
  mongo
  ```
- Créez la base de données et les collections :
  ```javascript
  use vacation_db;
  db.createCollection("users");
  db.createCollection("offers");
  db.createCollection("reservations");
  ```

- Insérez des données de test :
  ```javascript
  db.users.insertMany([
      { name: "John Doe", email: "john@example.com", password: "hashed_password", role: "admin" }
  ]);
  db.offers.insertMany([
      { type: "Beach", description: "Sunny beach", price: 500, photos: ["beach1.jpg"], availability: true }
  ]);
  ```

---

## 3. Exporter les Données MongoDB vers MySQL
### **3.1 Installer Node.js et les dépendances**
```bash
npm install mongodb mysql2
```

### **3.2 Créer le Script `export_to_mysql.js`**
```javascript
const { MongoClient } = require('mongodb');
const mysql = require('mysql2/promise');

const mongoUrl = 'mongodb://localhost:27017';
const mysqlConfig = {
    host: 'localhost',
    user: 'aux_user',
    password: 'secure_password',
    database: 'auxiliary_db',
    port: 3309
};

async function exportData() {
    const mongoClient = new MongoClient(mongoUrl);
    await mongoClient.connect();
    const db = mongoClient.db('vacation_db');
    const mysqlConn = await mysql.createConnection(mysqlConfig);

    // Export users
    const users = await db.collection('users').find().toArray();
    for (const user of users) {
        await mysqlConn.execute(
            'INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)',
            [user.name, user.email, user.password, user.role]
        );
    }

    console.log('Data exported successfully!');
    await mysqlConn.end();
    await mongoClient.close();
}

exportData().catch(console.error);
```

### **3.3 Exécuter le script**
```bash
node export_to_mysql.js
```

---

## 4. Configurer PHPMyAdmin pour MySQL Auxiliaire
### **4.1 Modifier le fichier `config.inc.php`**
- Ouvrez `config.inc.php` dans le dossier de PHPMyAdmin.
- Ajoutez cette configuration :
  ```php
  $i++;
  $cfg['Servers'][$i]['host'] = 'localhost';
  $cfg['Servers'][$i]['port'] = '3309';
  $cfg['Servers'][$i]['user'] = 'aux_user';
  $cfg['Servers'][$i]['password'] = 'secure_password';
  $cfg['Servers'][$i]['auth_type'] = 'cookie';
  ```

### **4.2 Vérifier l'Accès**
- Redémarrez Apache/WAMP/XAMPP.
- Ouvrez [PHPMyAdmin](http://localhost/phpmyadmin) et connectez-vous avec `aux_user`.

---

## 5. Automatiser l'Exportation avec Cron (Linux) ou Planificateur (Windows)
### **5.1 Créer une tâche planifiée Windows**
- Ouvrez le Planificateur de tâches Windows.
- Créez une tâche qui exécute `node export_to_mysql.js` toutes les heures.

### **5.2 Automatiser sous Linux (Cron Job)**
- Ouvrez crontab :
  ```bash
  crontab -e
  ```
- Ajoutez cette ligne pour exécuter toutes les heures :
  ```bash
  0 * * * * /usr/bin/node /chemin/vers/export_to_mysql.js
  ```

