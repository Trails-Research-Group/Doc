# Documentation for modding the Trails/Kiseki series

- [Mod list](Released-Mods.md)
- [Tutorials](https://github.com/Trails-Research-Group/Doc/wiki)

## What is currently doable
We define a difficulty scale for each item which reads like this:

☆☆☆☆☆ : straightforward, nothing difficult, takes literal minutes to be done\
★☆☆☆☆ : simple manipulation, no or very little coding background required\
★★☆☆☆ : a little more advanced, usually involves setting up a special environment like Python\
★★★☆☆ : a bit hard but still manageable for someone who has some background in programming and can interpret binary data\
★★★★☆ : pretty hard. not accessible to everyone. little to no documentation exist. A tool might exist but it is very rough\
★★★★★ : either a very difficult process with many complex and time consuming steps, or no tool exists (to our knowledge), you're on your own

### Trails in the Sky series
- Scena scripts editing: ★★☆☆☆ [FC, SC, 3rd] | [Guide](https://docs.google.com/document/d/1Nflb-dBPLLl0yWwk3MJTo0UxNyRPZDgy5zPanSrtotM/edit), [Tool](https://github.com/Ouroboros/EDDecompiler), [alternative tool](https://github.com/Kyuuhachi/Aureole)
- Texture injection/extraction: ★☆☆☆☆ [FC] | [Tool](https://github.com/Kaplas80/TranslationFramework2)
- Sprite extraction/injection: ★☆☆☆☆ [FC, SC, 3rd] | [Tool](https://github.com/Sewer56/Kiseki-Texture-Tool)
- Model extraction/injection: UNKNOWN [FC, SC, 3rd]
- Animation Scripts editing: ★★★☆☆ [FC] | [Tool FC](https://github.com/TwnKey/ED6ASDecompiler), [Tool 3rd](https://github.com/akatatsu27/FalcomToolsCollection/releases/tag/AS_Converter)
- Monster Scripts (MS.DT files) ★★☆☆☆ [3rd] | [Tool](https://github.com/akatatsu27/Falcom_Data_Formats/releases/tag/release)
- Table editing: ★☆☆☆☆ [FC] | [Tool](https://github.com/Kaplas80/TranslationFramework2)
- Font Creation: ★★☆☆☆ [FC, SC, 3rd] |[Tool](https://github.com/ZhenjianYang/SoraTranslation-Tools)
- BGM/OST extraction: ☆☆☆☆☆ [FC, SC, 3rd] | BGM folder contains all music files
- Replace BGM: ★☆☆☆☆ [FC, SC, 3rd] | [Guide](https://github.com/Trails-Research-Group/Doc/wiki/How-to:-Extract-and-replace-BGM)

### Crossbell series
- Scena/Animation Scripts editing: ★★☆☆☆ [Zero, Azure] | [Guide](https://docs.google.com/document/d/1Nflb-dBPLLl0yWwk3MJTo0UxNyRPZDgy5zPanSrtotM/edit), [Tool](https://github.com/AGraber/EDDecompiler), [alternative tool](https://github.com/Kyuuhachi/Aureole)
- Texture injection/extraction: ★★☆☆☆ [Zero, Azure] | [Tool](https://github.com/GeofrontTeam/EDDecompiler/blob/master/Decompiler/png32toitx.py), [DDS To 32Bits ITP](https://gist.github.com/Kyuuhachi/5af2b9c2036ae8e9b474e43b2854eef3)
- Sprite extraction/injection: ★★☆☆☆ [Zero, Azure] | [Tool](https://github.com/GeofrontTeam/EDDecompiler/blob/master/Decompiler/png32toitx.py)
- Model extraction/injection: UNKNOWN [Zero, Azure]
- Table editing: ★★★★★ [Zero, Azure] (Public tools might exist but they're scattered everywhere and don't support every table)
- Font Creation: ★☆☆☆☆ [Zero (NISA)] | [Tool](https://github.com/TwnKey/FalcomFontCreator)

### Trails of Cold Steel series
- Scena/Animation Scripts editing: ★★★☆☆ [CS, CS2] ★★☆☆☆ [CS3, CS4, Reverie] | [CS1, CS2](https://github.com/TwnKey/SenScriptsDecompiler), [CS3](https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED83), [CS4](https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED84), [Reverie](https://github.com/Ouroboros/Falcom/tree/master/Decompiler2/Falcom/ED85) | [SenScripts Guide](https://docs.google.com/document/d/1YVjFSkPsj9M0UgsI6_de4TSz35MeL_rGuhSQDtRTXxw/edit?usp=sharing)
- Texture injection/extraction: ★☆☆☆☆ [CS, CS2, CS3, CS4, Reverie] | [Guide](https://forums.dolphin-emu.org/Thread-custom-texture-tool-ps-v50-1?pid=482262#pid482262)
- Model extraction: ★★☆☆☆ [CS, CS2, CS3, CS4, Reverie] | [Tool](https://github.com/uyjulian/ed8pkg2glb)
- Model injection: ★★★★★ [CS3, CS4, Reverie] | [Tool (Maya)](https://github.com/Trails-Research-Group/Doc/releases/tag/v0.0) [Guide](https://github.com/Trails-Research-Group/Doc/wiki/How-to:-Import-custom-models-to-Cold-Steel-IV), [Tool (Blender, etc)](https://github.com/eArmada8/ed8pkg2gltf/releases)
- Table editing: ★☆☆☆☆ [CS, CS2, CS3, CS4, Reverie] | [Tool](https://git.sr.ht/~quf/tocs/tree/trunk/tbled/README.md) [Documentation](https://github.com/nnguyen259/SenSchema/wiki)
- Effect editing: ★★★★★ [CS, CS2, CS3, CS4, Reverie] | [Tool](https://github.com/uyjulian/ed8_eff_tools)
- Font Creation: ★☆☆☆☆ [CS, CS2, CS3, CS4, Reverie] | [Tool](https://github.com/TwnKey/FalcomFontCreator)
- BGM/OST extraction: ☆☆☆☆☆ [CS, CS2, CS3, CS4, Reverie] | data/bgm folder contains all music files
- Replace BGM: ★☆☆☆☆ [CS3] | [Guide](https://github.com/Trails-Research-Group/Doc/wiki/How-to:-Extract-and-replace-BGM)
- Voice extraction: ★☆☆☆☆ [CS, CS2, CS3, CS4, Reverie] | data/voice folder contains all voice lines, but finding a specific one requires some effort

### Calvard series
- Scena/Action Scripts editing: ★★★☆☆ [Kuro] | [Tool](https://github.com/nnguyen259/KuroTools), [Guide on scena editing](https://docs.google.com/document/d/19ajbTZzda54i5xZWDLXOq0oOVQrhJYXU9rmgz3Ya3Bc/edit?usp=sharing), [Guide on AI scripting](https://docs.google.com/document/d/1ofetrdRn3BY8GIqfnzWrutw9MnyNEfLYZ6NOgxZzg8A/edit)
- Table editing: ★★☆☆☆ [Kuro]| [Tool](https://github.com/nnguyen259/KuroTools) [Guide](https://docs.google.com/document/d/19ajbTZzda54i5xZWDLXOq0oOVQrhJYXU9rmgz3Ya3Bc/edit?usp=sharing)
- Texture injection/extraction: ☆☆☆☆☆ [Kuro]
- Model extraction: ★☆☆☆☆ [Kuro] | [Exe](https://github.com/nnguyen259/KuroTools) [Python (uyjulian)](https://gist.github.com/uyjulian/9a9d6395682dac55d113b503b1172009) [Python (eArmada8)](https://github.com/eArmada8/kuro_mdl_tool)
- Model injection: ★★☆☆☆ [Kuro] ([Exe](https://github.com/nnguyen259/KuroTools), [Guide](https://github.com/Trails-Research-Group/Doc/wiki/How-to:-Import-custom-models-to-Kuro-no-Kiseki)) [Python](https://github.com/eArmada8/kuro_mdl_tool)
- Font Creation: ★★★☆☆ [Kuro] | [Tool](https://github.com/TwnKey/ED9FontConverter)

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
