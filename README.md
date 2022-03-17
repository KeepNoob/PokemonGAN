# PokemonGAN
An attempt to create a Pokemon Generator that aims to create a new pokemon by using StyleGan3. Thank to the Nividia great work, it makes generator more robust and generate decent pokemons.

## Requirment and Environment
Before that install Anaconda or Miniconda
Open working directory and execute the following in Conda Prompt
```
git clone https://github.com/NVlabs/stylegan3.git
cd stylegan3
conda env create -f environment.yml
conda activate stylegan3
```
Notice that in case you are using Windows, please shall not use Visual Studio 2022 as your C++ (MSVC) runtime libraries beceasue it will occur error during network building process. 
## Dataset
