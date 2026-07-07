. mongodb-env.sh
brew services stop mongodb/brew/mongodb-community
mkdir store
mongod --dbpath store
brew services start mongodb/brew/mongodb-community 