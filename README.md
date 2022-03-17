# PokemonGAN
An attempt to create a Pokemon Generator that aims to create a new pokemon by using StyleGan3. Thank to the Nividia great work, it makes generator more robust and generate decent pokemons.

## Requirment and Environment
Before that install Anaconda or Miniconda
Open working directory and execute the following in Conda Prompt
```
-git clone https://github.com/NVlabs/stylegan3.git
-cd stylegan3
-conda env create -f environment.yml
-conda activate stylegan3
```
Notice that in case you are using Windows, please shall not use Visual Studio 2022 as your C++ (MSVC) runtime libraries beceasue it will occur error during network building process. 
## Dataset
All the data within this mini project are obtained from [Pokémon Database](https://pokemondb.net/pokedex/national) using a webscraping python script.
And do some process to those images such as Stylegan3 only support RGB 3 channels images but not RGBA. So converting to RGB mode is a must. Moreover, there exists some duplicated images. However, after trying to delete all duplicated images, the problem still exist. 
```Python
-python download.py
-python RM_Duplicate.py
```
Notice that the download script will be stopped at the last few pokemon "Wyrdeer" as the website directory pokemondb.net/artwork/urshifu does not exist.
