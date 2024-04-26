# Documentation for modding the Trails/Kiseki series

- [Mod list](Released-Mods.md)
- [Tutorials](tutorials)
- [Showcases](Mod-Showcases.md)
- [Cold Steel/Reverie documentation](cold-steel)

## What is currently doable
We define a difficulty scale for each item which reads like this:

☆☆☆☆☆ : straightforward, nothing difficult, takes literal minutes to be done\
★☆☆☆☆ : simple manipulation, no or very little coding background required\
★★☆☆☆ : a little more advanced, usually involves setting up a special environment like Python\
★★★☆☆ : a bit hard but still manageable for someone who has some background in programming and can interpret binary data\
★★★★☆ : pretty hard. not accessible to everyone. little to no documentation exist. A tool might exist but it is very rough\
★★★★★ : either a very difficult process with many complex and time consuming steps, or no tool exists (to our knowledge), you're on your own

- Textures/Sprites
  - [Sky, Crossbell] [Cradle](https://github.com/Kyuuhachi/Aureole)
  - [Crossbell] https://github.com/GeofrontTeam/EDDecompiler/blob/master/Decompiler/png32toitx.py
  - [Crossbell] https://gist.github.com/Kyuuhachi/5af2b9c2036ae8e9b474e43b2854eef3
  - [Cold Steel/Reverie] https://github.com/uyjulian/ed8pkg2glb
  - [CS3/CS4/Reverie] https://github.com/eArmada8/ed8pkg2gltf
  - [Cold Steel/Reverie] [Tool/Guide](https://forums.dolphin-emu.org/Thread-custom-texture-tool-ps-v50-2?pid=482262#pid482262)
  - [Sky] https://github.com/Sewer56/Kiseki-Texture-Tool
  - [Sky] https://github.com/Kaplas80/TranslationFramework2
  - [Kuro] https://github.com/nnguyen259/KuroTools
  - [Kuro] https://github.com/eArmada8/kuro_mdl_tool
- Models
  - [Sky, Crossbell] Unknown
  - [Cold Steel, Reverie] https://github.com/uyjulian/ed8pkg2glb
  - [CS3, CS4, Reverie] https://github.com/eArmada8/ed8pkg2gltf/releases
  - [CS3, CS4, Reverie] [Tool (Maya)](https://github.com/Trails-Research-Group/Doc/releases/tag/v0.0), [Guide](tutorials/Import-custom-models-to-Cold-Steel-IV.md)
  - [Kuro] [KuroTools](https://github.com/nnguyen259/KuroTools), [Guide](tutorials/Import-custom-models-to-Kuro-no-Kiseki.md)
  - [Kuro] https://github.com/eArmada8/kuro_mdl_tool
  - [Kuro] https://gist.github.com/uyjulian/9a9d6395682dac55d113b503b1172009
- Tables (stats, items, crafts, miscellaneous data)
  - [Sky] https://github.com/Kaplas80/TranslationFramework2
  - [Crossbell] Unknown
  - [Cold Steel, Reverie] https://git.sr.ht/~quf/tocs/tree/trunk/tbled/README.md
  - [CS3, CS4, Reverie] [conflict resolver for mods distributed in DLC format](https://github.com/eArmada8/misc_kiseki/blob/main/dlc_tables/dlc_conflict_resolver.py)
  - [CS3] https://github.com/nnguyen259/ColdSteel3Tools
  - [Kuro] [KuroTools](https://github.com/nnguyen259/KuroTools), [Guide](https://docs.google.com/document/d/19ajbTZzda54i5xZWDLXOq0oOVQrhJYXU9rmgz3Ya3Bc/edit#heading=h.805f9xdpyhea)
- Fonts
  - [Sky] https://github.com/ZhenjianYang/SoraTranslation-Tools
  - [Crossbell, Cold Steel, Reverie] https://github.com/TwnKey/FalcomFontCreator
  - [Kuro] https://github.com/TwnKey/ED9FontConverter
- Maps
  - [CS3, CS4, Reverie] https://github.com/eArmada8/ed8pkg2gltf
- Animations
  - [CS3, CS4, Reverie] https://github.com/eArmada8/ed8pkg2gltf
- Visual effects
  - [Cold Steel, Reverie] https://github.com/uyjulian/ed8_eff_tools
- Scenario scripts
  - [Sky, Crossbell] [Aureole](https://github.com/Kyuuhachi/Aureole)
  - [Sky] https://github.com/Ouroboros/EDDecompiler
  - [Crossbell] https://github.com/AGraber/EDDecompiler, [Guide](https://docs.google.com/document/d/1Nflb-dBPLLl0yWwk3MJTo0UxNyRPZDgy5zPanSrtotM/edit)
  - [CS3] https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED83
  - [CS4] https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED84
  - [Reverie] https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED85
  - [Cold Steel, Reverie] https://github.com/TwnKey/SenScriptsDecompiler, [Guide](https://docs.google.com/document/d/1YVjFSkPsj9M0UgsI6_de4TSz35MeL_rGuhSQDtRTXxw/edit)
  - [Kuro] https://github.com/nnguyen259/KuroTools, [Guide](https://docs.google.com/document/d/19ajbTZzda54i5xZWDLXOq0oOVQrhJYXU9rmgz3Ya3Bc/edit?usp=sharing)
- Animation scripts
  - [FC] https://github.com/TwnKey/ED6ASDecompiler
  - [3rd] https://github.com/akatatsu27/FalcomToolsCollection/releases/tag/AS_Converter
  - [Crossbell] https://github.com/AGraber/EDDecompiler
  - [CS3] https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED83
  - [CS4] https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED84
  - [Reverie] https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED85
  - [Cold Steel, Reverie] https://github.com/TwnKey/SenScriptsDecompiler, [Guide](https://docs.google.com/document/d/1YVjFSkPsj9M0UgsI6_de4TSz35MeL_rGuhSQDtRTXxw/edit)
- Monster/AI scripts
  - [3rd] https://github.com/akatatsu27/Falcom_Data_Formats/releases/tag/release
  - [Crossbell] Unknown
  - [Cold Steel, Reverie] https://github.com/TwnKey/SenScriptsDecompiler
  - [Kuro] https://github.com/nnguyen259/KuroTools, [Guide](https://docs.google.com/document/d/1ofetrdRn3BY8GIqfnzWrutw9MnyNEfLYZ6NOgxZzg8A/edit)
- Archive/Container/pkg/pka
  - [Sky, Crossbell] [Factoria](https://github.com/Kyuuhachi/Aureole)
  - [Sky, Crossbell] [unpacker for yamaneko PSP iso and cclm](https://gist.github.com/uyjulian/b596c978da0c1031047e124eaf5d4f84)
  - [Cold Steel, Reverie] [pkgtool](https://git.sr.ht/~quf/tocs/tree/trunk/pkgtool/README.md) (pkg/pka read/write)
  - [Cold Steel, Reverie] https://github.com/uyjulian/unpackpkg, https://github.com/uyjulian/unpackpka
  - [CS3, CS4, Reverie] https://github.com/eArmada8/ed8pkg2gltf (model tool, includes pkg read/write)
  - [CS3, CS4, Reverie] https://github.com/uyjulian/ed8pkg2glb (model tool, includes pkg read)
- BGM
  - Extraction doesn't require tools
  - [Sky, Crossbell, Cold Steel, Reverie] [BGM Insertion guide](tutorials/Extract-and-replace-BGM.md)
  - [Crossbell, CS1, CS2] [loop metadata editor](https://git.sr.ht/~quf/trails-ost-tool)
- Voice
  - [Crossbell, Cold Steel, Reverie] Extraction doesn't require tools
- Other
  - [Sky] [LB-Ark](https://github.com/Aureole-Suite/LB-ARK) (load modded files from the file system without updating an archive; load dll plugins)
  - [Cold Steel, Reverie] [SenPatcher](https://github.com/AdmiralCurtiss/SenPatcher) (load modded files from filesystem or .p3a archives)


## Places we recommend checking out
**[The Kiseki Modding Server](https://discord.gg/wYkWS33NQt)**

A fairly populated modding discord server with mod previews and notable people from the community; if you have a specific question that you can't find in any guide or FAQ, you can try to ask it here.

**[The Kiseki Difficulty Modding Server](https://discord.gg/EHhzrFGaRp)**

A discord server mainly focused on difficulty mods. Managed by [SoftBrilliant](https://github.com/SoftBrilliant).

**[The Trails/Kiseki modding GBATemp thread](https://gbatemp.net/threads/trails-kiseki-modding.476713/)**

Contains a list of ressources and useful links. Managed by [uyjulian](https://github.com/uyjulian)

**[The "Falcom" Github Repository](https://github.com/Ouroboros/Falcom)**

Contains a list of several tools gathered over the years. Managed by [Ouroboros](https://github.com/Ouroboros).

**[Trails in the Database](https://trailsinthedatabase.com/)**

Database containing the script for all the Trails games, sorted by script files, which can sometimes be of use for modding. Managed by [the database](https://github.com/the-database).
