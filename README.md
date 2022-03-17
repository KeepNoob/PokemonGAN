# PokemonGAN
An attempt to create a Pokemon Generator that aims to create a new pokemon by using StyleGan3. Thank to the Nividia great work, it makes generator more robust and generate decent pokemons.

## Requirment and Environment
Before that install Anaconda or Miniconda
Open working directory and execute the following in Conda Prompt
```
git clone https://github.com/KeepNoob/PokemonGAN.git
cd PokemonGAN
conda create --name <env> --file requirements.txt
conda activate stylegan3
```
In case, there are some package problem please refer to [Nvidia Stylegan3](https://github.com/NVlabs/stylegan3) 
Notice that in case you are using Windows, please shall not use Visual Studio 2022 as your C++ (MSVC) runtime libraries beceasue it will occur error during network building process. 
*My Personal PC Setup*
> CPU: i5-12600KF
> GPU: RTX 3070 Ti
> RAM: 32 GB
## Dataset
All the data within this mini project are obtained from [Pokémon Database](https://pokemondb.net/pokedex/national) using a webscraping python script.
And do some process to those images such as Stylegan3 only support RGB 3 channels images but not RGBA. So converting to RGB mode is a must. Moreover, there exists some duplicated images. However, after trying to delete all duplicated images, the problem still exist. And it is observed that the problem is due to image size different. If one is 300x256 and the other is 400x520, they could display same picture but the hash value is certainly different.  
```Python
python Download.py
python RM_Duplicate.py
```
Notice that the download script will be stopped at the last few pokemon "Wyrdeer" as the website directory pokemondb.net/artwork/urshifu does not exist.
## Preparing datasets
Nvidia Stylegan3 recommend to compresse the dataset into zip file, as it could lead to suboptimal performance.
Notice that all the data should be resize in a square like 128x128. And in this state, you can consider your GPU performance and VRam to decide which size. Indeed, all the images should be resize to 64x64 /128x128 or 256x256, as the original resolution is not quite high quality.
```Python
python dataset_tool.py --source=Poke --dest=datasets/<FILENAME>.zip --resolution = <width,hight>
```
## Training
kimg means the total iteration of the whole trainging, in default it is set in 25000. But according to author kimg = 5000 should provide a reasonable good enough quality. Moreover --batch, --tick, --snap should be set depend on GPU. Larger batch size requires more VRam. And --tick means after how many iterations the program prompts the status. Also tick\*snap means every k times the program will export a .pkl file. This file can be used in resume the learning. Beside that, if you want to speed up the training process, you can set --metrics=none and --cbase=16384. The first one usually uses for research purpose and the last one would reduce the quality to high resolution data. Last, the gamma value can significant affect the training.
```Python
python train.py --outdir=training-runs --cfg=stylegan3-t --data=dataset/PokePic-128x128.zip \
--gpus=1 --batch= <J> --gamma=<?> --kimg 5000 \
--tick <X> --snap <Y> --metrics=none --cbase=16384
```
## Reference 
[Nvidia Stylegan3](https://github.com/NVlabs/stylegan3)
## Example
Real
![Real](Picture/reals.png)
Fake only pass through 120 iterations
![Fake_120](Picture/fakes000120.png)
Due to limited time and computing power, it is hard to train the model in a satisfied iterations. It is an on going process, if I have enough time, I will resume my model training.  

