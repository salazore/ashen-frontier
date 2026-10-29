# Free-first asset shortlist

Research date: 2026-10-29. No paid assets are necessary for the proposed first build.

The public storefronts were blocked by this environment's network policy. Pack names, descriptions, formats, and free-download claims below were checked in the creator's public website source repository, commit `c219437bd230a5e66e1b523dbd8ee2bcf0dfb90b`, rather than by completing downloads. Preview images for Zombie Apocalypse, Survival, and Ultimate Buildings were also inspected. Download endpoints, archive contents, and Unity 6 import compatibility remain untested.

## Download these four first

| Pack | What it supplies | Use in this map | Formats listed | Creator page |
|---|---|---|---|---|
| **Quaternius Zombie Apocalypse Kit** | Character/enemy animations plus environmental and vehicle models; preview includes containers, barricades, signs and modified vehicles | Cinderhaven props, abandoned highway, salvage wrecks; characters are optional | FBX, OBJ, Blend, glTF | https://quaternius.com/packs/zombieapocalypsekit.html |
| **Quaternius Ultimate Buildings Pack** | Modular urban buildings and palette atlas textures; preview includes small buildings and storefronts | Depot shells, Glasswater streets and pharmacy exterior | FBX, OBJ, Blend | https://quaternius.com/packs/ultimatetexturedbuildings.html |
| **Quaternius Ultimate Nature Pack** | Low-poly natural scenery; catalog lists 150 models | Rocks, tree bases, scrub and ridgeline dressing; make burned variants yourself | FBX, OBJ, Blend | https://quaternius.com/packs/ultimatenature.html |
| **Quaternius Survival Pack** | Survival equipment; preview includes tents, bags, fuel cans, radios and other small props | Camp, salvage containers and quest dressing | FBX, OBJ, Blend | https://quaternius.com/packs/survival.html |

Use this single creator as the main visual family. These packs are colorful by default; the muted material palette and ruined variants are part of the art pass. Buildings are not guaranteed to include usable interiors, damage states, or colliders. A model of a radio, bag, or vehicle does not include working game logic.

## Add only when needed

| Pack | Role | Creator page | Scope |
|---|---|---|---|
| Quaternius Modular Streets Pack | Roads, junctions and street layouts | https://quaternius.com/packs/modularstreets.html | Free download described; FBX/OBJ/Blend. Add cracks and broken edges separately. |
| Quaternius Modular Train Pack | Trains for Rustline Yard | https://quaternius.com/packs/modulartrain.html | Free download described; FBX/OBJ/Blend. Verify tracks in the archive; build track strips if absent. |
| Quaternius Farm Buildings Pack | Barn and outbuilding forms for Old Orchard | https://quaternius.com/packs/farmbuildings.html | Free download described; FBX/OBJ/Blend. Weather and partially dismantle variants. |
| Quaternius Ultimate Modular Ruins Pack | Broken masonry for foundations, culverts and an old utility structure | https://quaternius.com/packs/ultimatemodularruins.html | Free download described; FBX/OBJ/Blend. Catalog describes ruins and dungeons: use sparingly to avoid a medieval look. |

The newer **Stylized Nature MegaKit** and **Downtown City MegaKit** have free Standard subsets and paid higher tiers. Their catalog explicitly reserves some extra models, engine projects, and custom shaders for other tiers. They are not needed for the first build; do not assume the full advertised set or ready-made URP shaders are free.

## License evidence and packaging

There is a real discrepancy in the creator's current source: the individual older pack pages above label the packs **CC0**, while the newer site-wide [license page](https://quaternius.com/license.html), dated August 28, 2026, describes **Quaternius Asset License v1.0**. QAL permits personal, educational and commercial projects and collaborators, but prohibits standalone asset redistribution. It also says future changes do not apply retroactively to assets already obtained under an earlier version.

For each actual download, retain the included license and acquisition date. Until the archive's terms are confirmed, treat it under the stated QAL restrictions: use it in the game, keep source assets private, and do not bundle model files in a public handoff or public asset repository. This design kit contains only original design documents and links. It does not claim every Quaternius download is currently CC0.

An independently checked CC0 alternative for simple city models is [Kenney's City Builder starter kit](https://github.com/KenneyNL/Starter-Kit-City-Builder). Its README explicitly identifies included sprites, 3D models and sound effects as CC0; the code is MIT. The starter itself is a Godot project, so use its model files as raw art, not as a Unity starter project. Check formats and scale before choosing this as an alternative; mixing it into the main Quaternius art family may require more adjustment.

## Unity tools — use the editor's compatible package versions

| Tool | Purpose | Source and cost status |
|---|---|---|
| Unity URP template / Universal RP | Main rendering pipeline, materials and post-processing | Included Unity tooling; obtain through Unity Hub/Package Manager. Unity subscription eligibility is separate from asset costs. |
| Terrain | Ground, terrain layers, trees and basic sculpting | Unity built-in tooling; no paid terrain generator needed. |
| ProBuilder, optional | Rapid custom dam, depot, mast and factory blockout | Unity Package Manager, package `com.unity.probuilder`; choose a version compatible with the pinned editor. Cubes/cylinders also suffice. |
| AI Navigation | NavMesh surfaces and links for walkable paths | Unity Package Manager, package `com.unity.ai.navigation`. Unity's [older NavMeshComponents repository](https://github.com/Unity-Technologies/NavMeshComponents) explicitly directs current projects to this package. Do not import the legacy repository alongside it. |
| Input System | Player input | Unity Package Manager, package `com.unity.inputsystem`; configure the project to match the controller implementation. |

The Unity documentation site could not be loaded from this environment. Package availability/API versions should be checked inside the selected editor rather than guessed from older tutorials. No premium controller, terrain, weather, road, streaming, or water package is required for the prototype.

## Import sequence

1. Create or open a Unity 6 URP project. Pin the editor version in `ProjectVersion.txt`; let Package Manager resolve versions compatible with it. Keep the existing repository checkout.
2. Download the selected free editions from the creator, inspect each archive's license, and preserve the evidence privately with the source art. Do not purchase upgrades automatically.
3. Prefer **FBX** exports. Import under `Assets/ThirdParty/Quaternius/<PackName>/`; include texture files. Do not require `.blend` imports, which depend on Blender, or assume Unity imports glTF without an importer.
4. Create a small import-test scene. Verify that a person is approximately 1.7–1.9 Unity units high and a doorway has plausible clearance. Adjust importer scale consistently rather than scaling every instance arbitrarily.
5. Extract/create materials, assign the supplied textures to URP/Lit or a deliberately simple URP shader, and check the whole scene for missing/pink materials. Copy or vary materials outside vendor folders; do not overwrite all source textures with a tint.
6. Check rig and clip import for any character chosen. Humanoid mapping must actually validate before using retargeted animations. Enemies and weapon systems are optional and should not block environment assembly.
7. Add simple box/capsule colliders for traversal and salvage. Use mesh colliders selectively for static structures. Add LOD groups where geometry warrants them and verify terrain-tree prefabs rather than assuming every downloaded tree has LODs.
8. Make project-owned prefab variants in `Assets/AshenFrontier/Prefabs/`. Keep custom shaders/materials, scripts and scenes outside vendor folders. Retain `.meta` files. Do not commit `Library`, `Temp`, `Logs`, or build output.

## Assets still to build

Free packs cover the bulk of scenery and dressing, not every landmark. Custom work remains:

- Mercy Dam: spillway, deck, sluice building, railings and downstream channel.
- Ashworks: two chimneys, pipes, processing sheds and conveyors.
- Dead Signal: lattice mast silhouette and broken antenna.
- Quarry: stepped terrain, conveyor silhouette; use a placeholder excavator until a suitable model is licensed.
- Damage: missing roofs, broken window panels, rubble, boarded doors and damaged vehicle variants.
- Water: a simple URP-compatible material plus clear collision/traversal rules.
- Atmosphere/audio: original simple ash particle effect; source ambience separately with an appropriate license, or use placeholders. No sound library was verified for this kit.

Start these with primitive meshes and a handful of materials. The first build can use a generic scrap-depot outpost instead of a detailed service-station interior.

## Source evidence

- [Quaternius website source](https://github.com/Quaternius/quaternius.github.io/tree/c219437bd230a5e66e1b523dbd8ee2bcf0dfb90b/packs): pack names, download claims, formats, previews and per-pack CC0 labels.
- [Quaternius global license source](https://github.com/Quaternius/quaternius.github.io/blob/c219437bd230a5e66e1b523dbd8ee2bcf0dfb90b/license.html): newer QAL terms and effective date.
- [Kenney City Builder README](https://github.com/KenneyNL/Starter-Kit-City-Builder#readme): assets explicitly CC0, template Godot, code MIT.
- [Unity NavMeshComponents README](https://github.com/Unity-Technologies/NavMeshComponents#readme): current AI Navigation package migration guidance.
