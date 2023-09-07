# A few words before starting
This is not really a _guide_ per se, but more general directions as well as instructions on how to use the tools (that we provide). This process was only achieved by one person so far (and the author of this "guide" is not them). Therefore, it is possible that you will waste time and be frustrated. I ask that you don't harass/insult me or anyone else, as we are basically handing you months of research and hard work. If you're expecting precise instructions that you just have to follow to get it working, then don't bother reading it, as you will need to use your brain to understand how things work above everything else.

TL;DR: you need a functional brain to proceed
# Introduction
This page is here to help you in the process of adding custom models to Cold Steel IV. It is currently one of the most complex operations in modding as it involves several steps, and is still at a somewhat early stage.

The guide will hopefully lead you to insert Van Arkride from Kuro no Kiseki to CSIV. 

The current process includes the following steps in chronological order:
- Obtaining the model to import (Van Arkride) as a FBX file
- Importing it in Maya 2015/2016/2017/2018
- Applying shaders to Van's materials in Maya (including his shadow shader)
- Exporting Van to .dae using the ColladaMaya plugin
- Importing Van in CSIV using CSIVAssetImportTool to obtain a .dae.phyre file
- Updating the shader names in it

The goal will be having Van in game.
However we will stop here due to the complexity of the process. Normally you would need to add the animations using scripting (I recommend using Ouroboros' ED84 decompiler to edit and decompile a character file copied from an existing character. You would also need to add new entries to TBLs for a new character, etc.)

Also note that due to multiple crashes with Maya and me unable to complete it, I can't provide more explanations that what is on this guide. You are free to contribute if you make any new finding or have anything new to bring to this process though, but I won't be able to help you further than this guide since I don't have all the answers myself nor am I sufficiently familiar with the process to help, in fact.

# The environment
The best advice I can give after several issues and wasted time and frustration about file paths, is that you should work in a single folder, for example called "WorkFolder", consisting of a "shaders" folder, where you will also put ED9AssetExporter, but also the CSIVAssetImportTool.
The pictures in this guide might not reflect that, because while writing this guide I was not fully aware of all the constraints. But at least the text should be up to date.\
Also note that a WorkFolder example with all the necessary tools is available [here](https://github.com/Trails-Research-Group/Doc/releases/download/v0.0/WorkFolder.zip)\
You will also find a reference document that can help you pinpoint the most often used shaders in CSIV, inside a txt called [Chr.Shaders.txt](https://github.com/Trails-Research-Group/Doc/releases/download/v0.0/Chr.Shaders.txt)
# Obtaining the model
To extract Van's model from Kuro no Kiseki game files, we will be using [KuroTools mdl exe](https://github.com/nnguyen259/KuroTools/releases/download/v1.2.1/KuroTools.v1.2.1.zip).\
First we search for Van's model file which is called chr0000.mdl. We will also grab his run (chr0000_mot_run.mdl) and idle (chr0000_mot_wait.mdl) animations. All the mdls are located in "THE LEGEND OF HEROES KURO NO KISEKI\c\asset\common\model".

Then we will put all the files inside a folder near ED9AssetExporter.exe:\
![image](https://user-images.githubusercontent.com/69110695/185991227-d2ad821a-addd-4b6f-8380-65b6feefebb2.png)\
And the folder (called "model", above) content:\
![image](https://user-images.githubusercontent.com/69110695/185991161-4dcfac71-ca52-4ba0-85f7-079809a53a4e.png)\
All that is left is drag and drop the folder containing van mdl and his animations onto ED9AssetExporter.exe.\
![van1](https://user-images.githubusercontent.com/69110695/185992671-d884f066-c27f-474a-b522-f4794c1234fa.gif)\
The tool outputs a FBX file. However, it does not have any texture. It is because textures are separate from the mdl file,
since they are located in "\THE LEGEND OF HEROES KURO NO KISEKI\c\asset\dx11\image".
To know which texture you need to use, you will have to run the tool and take note of what the tool is outputting on the console;
those are the missing textures:\
![image](https://user-images.githubusercontent.com/69110695/185995998-c4bc180e-d0ee-4e98-acd1-e7461cae5cc5.png)\
Get them all from c\asset\dx11\image and place them in the same directory than ED9AssetConverter:
![image](https://user-images.githubusercontent.com/69110695/185997459-a68df074-d912-4e49-8c84-0f0f777fac6e.png)

# Setting up the model in Maya
At the time of writing this guide, we didn't find a better tool than Maya 2015 to 2018, as Blender dae export doesn't seem to work well when injected in CSIV (supposedly, the skeleton doesn't seem compatible).\
That's why we will be using Maya 2018 from here.\
Once Maya is launched, import chr0000.fbx into the scene:\
![image](https://user-images.githubusercontent.com/69110695/185993530-9924f2ca-c36e-4472-86e3-9af4f68c99ee.png)\
You can ignore the possible warnings that show up. The result should look like this:\
![image](https://user-images.githubusercontent.com/69110695/185993749-091b952f-a8df-4ec0-9185-f95ad4109bc6.png)\
When enabling the texture, nothing really shows up. It is because Van's shadow is a mesh itself and is covering him.\
You can hide that mesh by selecting the kage one and CTRL + H.\
![image](https://user-images.githubusercontent.com/69110695/186008758-403e6306-bd17-4736-89c6-5eb5ef1e85cd.png)\
Note: if any texture looks wrong, you might want to convert them to DDS BC1.\
Right now, we don't really care, as the only thing we will be doing is applying a shader to each material.

Something that might get important later, is that some of the Kuro character models have too many bones to import correctly in Cold Steel. There is a hardcoded limit of bones per model that you need to respect, otherwise some bones will be removed without the associated weights being remapped, leading to animation issues. The only solution we found was to manually remove a few "non important" bones, and remap the vertexes they affected to another bone, close to the one being removed.

# Intro to shaders
Shaders are by far the most complex part of the process, so read carefully this section.

I will list what we know about shaders right now and explain briefly the process before getting into details:
* Shader files are the .fx files you can find when unpacking pkg files. 
* In their original form, they are source files written in HLSL language. In CS1 .fx.phyre files, you can find the source code in HLSL directly at the bottom of the files. From CS2 they are all compiled into binary form (called direct3D shader bytecode, read http://timjones.io/blog/archive/2015/09/02/parsing-direct3d-shader-bytecode).
The DXBC magic word can help identify the bytecode sections in a .fx file.
Note that it is possible to decompile them into HLSL again using some tools like this one https://github.com/etnlGD/HLSLDecompiler.
Also note that there is a project to reimplement the shader into unity (https://github.com/PMONickpop123/ED8Shader)
* Those files contain a set of shader parameters, switches, and functions. We do not know what the source code of those functions is but we can extract the value of the shader parameters after compilation (The values are present in the .dae.phyre).
* The switches disable or enable certain parts of the source file shader that are then not compiled into bytecode, which means that for a single source shader, it will exist multiple variants depending on which switches were selected. When compiled based on the switches, the binary content is different depending on which switches were selected, and a checksum is calculated based on that binary content, which leads to variants of the ed8_chr.fx file being called "ed8_chr.fx#HEXADECIMALSEQUENCE"; those files came from the same .fx source files but different switches and parameters were selected.
* The switches from our ed8_chr.fx file will be selected through Maya, and written as selected inside the exported .dae.

Finally, note that since we do not want to write any source code in HLSL, our goal is only to use already compiled shader files from the original game, eventually tuning the parameter values (we won't write any function or code in HLSL).\
This means our ed8_chr.fx file doesn't contain any code. Even if it the same set of parameters was used than an original Cold Steel shader inside Maya, since our fx file doesn't contain any function, the binary content after compilation will be shorter and different, thus a different checksum will be calculated. That will lead to a different filename for the resulting .fx.phyre file called "ed8_chr.fx#HEXADECIMALSEQUENCE2", which will be etched into the .dae.phyre file; this filename will need to be updated to refer to the original Cold Steel shader file that contain the functions implemented by the CS devs, functions that we want but couldn't write and compile ourselves.

In this guide, I will first explain how to parameterize a shader the whole way in Maya copying the parameter values of the original shader manually, then explain how to use the "presets" (or custom switches) that were added to simplify the process a bit. This is for the sake of understanding what is going on.
# Applying shaders

The very first step is to select existing shaders from original Cold Steel IV models. For this we will use the reference document that we provide that lists the usual shaders that are used for each part of the body. Note that if a shader is not listed here (for example, one not used in character models), you can still use it but it will require going through the "manual parameter setting method".\
Anyway, let's start with the shadow shader.\
The shader used for shadow is "ed8_chr.fx#7D5B6AA14716CB4C48A6EB8A4185E522.phyre", which is available in a lot of characters' PKGs.\
![image](https://user-images.githubusercontent.com/69110695/186251155-2c5fd0e6-17ed-4fdf-86c0-fda12cbdc68e.png)\
(Example here, it is taken from a Rean DLC pkg)\

So first, we need to open the .dae.phyre which is using this shadow shader with the PhyreDummyShaderCreator.
To do that, just drag and drop the .dae.phyre onto the PhyreDummyShaderCreator executable.\
![DummyShader](https://user-images.githubusercontent.com/69110695/186252733-b02b9a8e-c4ea-42d5-9c86-c15204d103de.gif)\
It will produce a list of fx files, one for each shader variant used by the .dae.phyre. The one we will open with notepad is the shadow one, #7D5.\
![image](https://user-images.githubusercontent.com/69110695/186252849-14262bc6-692d-490c-95c1-3ffaed4dde18.png)\
It gives us the shader parameter for the shadow. Those are the ones we will copy in Maya for the ed8_chr.fx file applied to the shadow material.

Note that we know #7D5 is used for the shadow because the DummyShaderCreator produces a txt file called materials.txt which links each material to its shader:\
![image](https://user-images.githubusercontent.com/69110695/186452310-2845bf74-b414-4c04-9f2c-166ce8c17652.png)\
"shadow_collada" (the las one) gives you #7D5.

We provide a generic ed8_chr.fx dummy shader without any code in it, only parameters, as explained in the shader intro section. Well, technically the current version has some code in there but we don't care about it (some leftover stuff), we only need the switches.\
The trick is that we will be using existing shaders from Cold Steel IV that were already compiled by the developers. In Maya, we are just using empty shaders to set the parameters in the output dae.

So in order to do that, move the COLLADA.mll file corresponding to your Maya version [get it here](https://github.com/Trails-Research-Group/Doc/releases/download/v0.0/ColladaMayaExporter.zip) to the Maya/bin/plug-ins folder. You also should switch
the rendering engine to DirectX11 (Windows > Preferences):\
![image](https://user-images.githubusercontent.com/69110695/186246925-26a795ef-2e66-4bdd-8a65-ef1bdb515dd3.png)\
Then restart Maya.
Once Maya is restarted, you need to open the plugins manager (Windows > Preferences > Plug-in manager), find COLLADA and tick the Loaded box.\
![image](https://user-images.githubusercontent.com/69110695/186244862-e15d4b3c-1097-4476-b749-0b80ae77e3da.png)\
Now you will be able to import .fx files and set the parameters for each material. 

Before doing anything more, make sure that your ed8_chr.fx file is put inside the shaders folder inside your work folder.
In Hypershade (Windows > Rendering Editors > Hypershade), select the chr_shadow material.\
![image](https://user-images.githubusercontent.com/69110695/186253758-7726a20f-71c7-4b04-9677-ab61946b4355.png)
On the right (The attribute editor), instead of "Lambert", select colladadx11Shader1.\
![image](https://user-images.githubusercontent.com/69110695/186246169-cb1af7f0-ca5d-4764-87fe-f81dd8d66ad5.png)\
And then below, select the provided ed8_chr.fx.

Here is the hard part. Once the fx is selected, a few sections appears.\
![image](https://user-images.githubusercontent.com/69110695/186258285-04cb4f15-d1ec-4be5-9c02-5dcb6f8806ab.png)\
Note that the name of the material changed to a generic collada shader one. In order to keep track of all materials, I recommend renaming the material.
Back to the reference doc, you have the name of the materials highligthted here:\
![image](https://user-images.githubusercontent.com/69110695/193454381-7bee0ea9-19c4-4a98-96e5-e8dbea3ce62c.png)
So I recommend giving them the name from the reference doc, so that you will know which shader from the original game you have been using for this material.

# The manual process of setting parameters
The following process is time consuming but allows you more control over the switches. **I don't recommend using it** but recommend reading it to understand a bit more how shaders work.\
You will first open the Material Switches one, and proceed to select every switches (every parameter name, if you want) that is present
in the dummy shader file we created for the shadow previously (and opened in notepad).
When you reach the "sampler" part after BloomIntensity, instead of activating all Samplers, just tick the "Activate Samplers" box, which will take care of all of them. Finally, the last one you want to tick is the Texture2D (the last line of the dummy fx file), DiffuseMapSampler.\
![image](https://user-images.githubusercontent.com/69110695/186258739-8fbef591-b38e-45d3-b686-c57811c77337.png)\
Once this is done, close this section and open the Material Parameters > Uniform section. You will get something like this:
![image](https://user-images.githubusercontent.com/69110695/186258877-5581dfed-0e5b-4e92-9da3-65dbc59de37a.png)\
We will now port all the values obtained from the dummy fx file:\
![image](https://user-images.githubusercontent.com/69110695/186259223-1d1ba4ec-8f0c-4503-9df5-43876820bc1c.png)\
Including the chr_shadow_conv.dds texture that will be used for the Texture2D parameter called DiffuseMapSampler. You will find this texture in any character PKG after conversion from .dds.phyre to .dds. However, you must first put the chr_shadow_conv.dds inside the folder where you store all the other textures; if you follow this guide, that would be ED9AssetConverter. Once you did that, select chr_shadow_conv from that folder.
For the half4 parameters, they use a color + a ".w" component". 
You set the color in RGB value which will deal with the first 3 values and you set the .w to the fourth one.\
![image](https://user-images.githubusercontent.com/69110695/186262665-387a709a-e2c8-4dfe-8845-177c0f1983e5.png)\
![image](https://user-images.githubusercontent.com/69110695/186262771-b2173e94-9f8e-4f01-bea2-7fe0c29323cb.png)\
However, usually they all have the same set of values, so the default values should do, and you shouldn't have to fill them.

You should finally obtain something like this:\
![image](https://user-images.githubusercontent.com/69110695/186262895-a41f15a8-1e83-4d6a-be0e-2c6e5dcdd4e0.png)\
where file1 is chr_shadow_conv.dds.

OK, that's one material done, now do all the others!...Except we will now use predefined set of parameters to speed it up a bit.\
# The manual, but easier way to use shaders
We will now redo the shadow shader. Start by selecting the collada fx shader like in the previous step. However, when selecting the switches, you now only have to select one switch, which is "ed8_chr.fx#7D5B6A":\
![image](https://user-images.githubusercontent.com/69110695/192744046-014035a2-c508-4051-8c71-59758166da06.png)\
This will automatically apply generic values for the shadow shaders and add the correct parameters. You can tune them later if you realize values don't work well in game, but usually they do work.\
![image](https://user-images.githubusercontent.com/69110695/192744166-ae24eb09-03f7-44fb-a34b-e4f1ca32367f.png)\
However, you still have to retrieve the original texture for the shadow like in the previous step, assigning the texture to the DiffuseMapSampler parameter.\
Once this material is done, you will need to repeat the same process for each material of the model. We provide a reference document called Chr Shaders that contains the names of the usual shaders used for the characters, with Skin and Unskinned versions. This will help you select the correct switch to apply for each material (Select the Skinned one when available in the switch materials panel).

# Export to dae
Now that the shader(s) have been taken care of, we will export the model to dae, which is the format used by the game.\
A very important step is to gather all your texture file
To do this, go to File > Export All, and set the export parameters like this:\
![image](https://user-images.githubusercontent.com/69110695/186264413-fb724f85-60bd-4b08-af4f-e0c40138a148.png)\
The "Files of type" field must be set to COLLADA exporter (not DAE_FBX export)\
![image](https://user-images.githubusercontent.com/69110695/186264545-eaafbf98-cf71-408b-9903-053bc9c39e27.png)\
Also, it is EXTREMELY IMPORTANT for you to export the .dae to the same folder where all your textures were located. If you used ED9AssetConverter to extract the model, then you need to export the dae to the folder containing ED9AssetConverter.exe, where all textures and fbx are located.
This is because the path of each texture in the dae is relative to the export location, but also because of an annoying constraint of the CS4 importer tool that requires all textures to be in the same folder than the model.

When the file has finished exporting, you can open the .dae with notepad and check if all DDS files have their path in the same folder than the dae, like this:\
![image](https://user-images.githubusercontent.com/69110695/186463069-5968a544-4061-4055-8357-3ce7678cec6c.png)\
And the same should go for the .fx file:\
![image](https://user-images.githubusercontent.com/69110695/186469265-15429cb1-7cf5-4b68-a9b5-3c46a9e31db9.png)

Note that if your character appears green, it doesn't necessarily mean that something went wrong. The rendering in Maya is irrelevant after you start applying the ed8_shader as no code (or barely) is present in our ed8_chr.fx, only switches and parameters. The rendering in game will be performed by the code in the original Cold Steel IV shaders that will replace our ed8_chr ones.

# Conversion to phyre format
Now we will use the CSIVAssetImportTool to produce the .dae.phyre and dds.phyre to later be packaged into a pkg. So if you respected my advice back at the beginning, Van's dae and all of his textures should be next to CSIVAssetImportTool.exe.
Remember that we have a shaders folder in it.
This folder is where you will put the ed8_chr.fx file.\
![image](https://user-images.githubusercontent.com/69110695/186469508-22ff9371-9f14-4d01-89e6-daea7f6e8236.png)

The folder should look like this (after getting rid of ED9AssetConverter, the fbx, and the model folder):\
![image](https://user-images.githubusercontent.com/69110695/186470131-879f7917-e03a-4146-a9a4-5c28f09b00f3.png)

Now, just drag and drop van.dae onto Process.bat.
It will create a D3D11 folder containing the textures as .dds.phyre and the model as .dae.phyre. It also contains a folder called shaders with 
multiple shaders (the ones on the picture might not reflect yours).\
![image](https://user-images.githubusercontent.com/69110695/186470773-f36a90e4-45c1-4337-ab1c-61384080f6b2.png)

## I end up with more shaders that before after compilation into phyre, what is happening?
The tool will sometimes generate two different types of shaders (with the same set of parameters), the regular one and the "-Skinned" one.
When opening the resulting .dae.phyre with the DummyShaderCreator, the materials_list.txt shows this:\
![image](https://user-images.githubusercontent.com/69110695/193466641-090844ee-0b8e-44b8-a596-2281067a5c19.png)\
In that case where you need to select an original Cold Steel IV shader for the skinned one and the unskinned one, please use the reference document:\
![image](https://user-images.githubusercontent.com/69110695/193466694-8c4d7535-eff3-45bf-bc6e-8d6dd67036be.png)\
It gives the skinned and unskinned versions of the shaders from Cold Steel IV that you will need to replace later.
 
Also note that it is possible to use only the skinned version for both shaders, as they have the same set of parameters (the crc is the same).

# Updating shader paths

This part is actually the hardest part to understand. As explained before, the shader ed8_chr.fx that we used in maya is devoid of code, and we only used it to insert the values of the shader parameters (colors, texture sampler, ...) into the dae. Upon compiling into .dae.phyre, the tool allocated enough memory for all the shader parameters and wrote it into the dae. What we are going to do now is to replace each of the shader written in the dae with the corresponding shader of the original game, which contains the shader code we want to execute.

To do this, we need to ensure that ALL the shaders in the dae that are replaced have the SAME exact number of parameters, with the same type, and written in the same order, than the original Cold Steel IV shaders. Otherwise, the game will certainly crash.

To be more concrete I will show an example of what you could have obtained for the .dae.phyre at this stage. First open your .dae.phyre with a hex editor and look for the text ".fx".\
![image](https://user-images.githubusercontent.com/69110695/193463144-969fb9f1-da46-4368-9402-103282efc3eb.png)\
This shows you the section where all the references to the shaders are written. Right now the shaders that are written here are our ed8_chr.fx shader variants that don't contain any code! That's why we need to replace them with the shaders from the original game.

To know which name to give to each shader, you can run the PhyreDummyCreator with your new .dae.phyre.
It will once again generate a material list which is shown here:\
![image](https://user-images.githubusercontent.com/69110695/193457796-89ba4c84-9b9f-4968-af8b-8922a7f7f826.png)\
Then, using the provided Chr.Shaders.txt doc and the material name that is listed on the left in materials_list.txt,\
![image](https://user-images.githubusercontent.com/69110695/193457832-a0d2f43f-064c-46f7-baf2-6d1a44d7e80e.png)\
(highlighted is the material name!)\
You can find the new name to use for a given shader in materials_list.txt. For example the collada "chr_shadow" material, which uses ed8_chr.fx#CE09E5FEED04015F703B4B955C73BCF2, will use the same shader than "kage01" (as explained in the shader ref document) material, which is ed8_chr.fx#7D5B6AA14716CB4C48A6EB8A4185E522. 

Which means that in your .dae.phyre, you will need to replace all the references of ed8_chr.fx#CE09E5FEED04015F703B4B955C73BCF2 with ed8_chr.fx#7D5B6AA14716CB4C48A6EB8A4185E522.

As a safety precaution, you could also check if all the parameters check out between ed8_chr.fx#CE09E5FEED04015F703B4B955C73BCF2 and 
ed8_chr.fx#7D5B6AA14716CB4C48A6EB8A4185E522. To do this, open the two dummy_XXXX.fx files and compare their content:
![ComparaisonDummies](https://user-images.githubusercontent.com/69110695/193458207-415e4805-ae70-4e8f-b678-75411dbe5a30.png)
They should be identical in order, in number and in type (value doesn't really matter though.)
Another way to compare two shader files to see if they are compatible is using the "crc" value that is provided in the shader reference document,
and in the material list. If both are equal, the files are compatible (as in, no crash should occur). But two completely different shaders could have the same set of parameters, so the same CRC, thus CRC is only an indicator that is at least enough to ensure no crash happens, but it is not a rule.

The best way to identify which shader to replace is to be extra cautious with the material names and refer to the shader doc.

Anyway, I suggest opening the material list txt and try linking with the shaders described in the reference document. When all the shaders have their equivalent, it is time to update the references in the .dae.phyre.

So, in order to do that, reopen the .dae.phyre with a hex editor and renavigate to the .fx section shown previously.
Now it is only a matter of replacing the hashcode with the one of the original cold steel shaders using the notepad file you wrote before.
For the shadow specifically, here's what you have:\
![image](https://user-images.githubusercontent.com/69110695/193463230-e48b9752-9c5b-4a37-a72c-a66ee77fe99c.png)\
You will want to replace CE09E5FEED04015F703B4B955C73BCF2 with 7D5B6AA14716CB4C48A6EB8A4185E522 like this:\
![image](https://user-images.githubusercontent.com/69110695/193463254-3bb29c6c-809e-45d2-bcfc-1f3609ff170f.png)\
Repeat the operation for all shaders. 

Finally, keep in mind that you CAN'T insert or remove existing byte, only replace them, as the file is filled with pointers. So keep the filesize in mind and make sure it doesn't change.

# Preparing the PKG

Now that all files are prepared, we need to pack them into a pkg. This involves creating a new folder called C_CHR000 (to replace Rean), and writing a new asset_D3D11.xml.
So first, create the folder, and put all the dae.phyre and dds.phyre, as well as an asset_D3D11.xml extracted from a random character PKG from CS4 (doesn't matter who).\
![image](https://user-images.githubusercontent.com/69110695/186475658-75354a43-1849-436c-a69d-be0c3a8c92e0.png)\
You also need to get the original shaders, the one for the shadow (which will be in the pkg you first unpacked, and is named #7D5) and all the others (that you can find in various other pkgs).
The final content of the folder should look like this (more shaders are expected though, pics are a bit outdated, but you will get the general idea):\
![image](https://user-images.githubusercontent.com/69110695/186476189-b14401d3-e9b4-417f-bbce-a6a3d5989db7.png)

The important part is the asset_D3D11.xml. Depending on what was your environment (folders) when compiling to dae.phyre, you need to set the correct paths in the xml.
In the .dae.phyre, all the texture and shader paths are relative to data/D3D11/, that means you need to keep this part of the path
in the asset XML and add the rest of the path found in the .dae.phyre.


![explanationsAssets](https://user-images.githubusercontent.com/69110695/193463446-e817c88b-6307-4b81-98a5-4dbd9da84457.png)\
On the right of the picture, you can see how the path for textures (the first highlighted text) and shaders (the second) might look like. 
It is actually **MANDATORY** to have the shaders in a "shaders" folder at the compilation, since the already compiled cold steel shaders reference themselves inside a "shaders" folder 
![image](https://user-images.githubusercontent.com/69110695/193462298-76886fd2-697e-427d-aa40-8c0ff25c10bc.png)

Just add that path right after data/D3D11/ in the asset xml. 

Do that for all textures and shaders (the dae should follow the original path which would be "data/D3D11/chr/chr/XXXXXX", which matches with the location of the .inf file in the game folder
 
![image](https://user-images.githubusercontent.com/69110695/193460658-987179d3-4485-402f-aa0c-f766a3873d89.png)\
After that, repack the PKG, and try it in game. Hopefully it works.
















