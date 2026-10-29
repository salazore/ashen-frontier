# Ashen Frontier — The Cinder Basin

A stylized 3D post-apocalyptic region designed for a free-first Unity build.

**Design proposal, not a playable Unity scene.** The repository did not contain a Unity project when this kit was created. Unity is not installed in this cloud environment, so engine imports, shader compatibility, gameplay, and performance have not been tested. No third-party asset archives are included.

## The region

An inland industrial valley, years after a catastrophic fire and infrastructure collapse. Rain has returned, the town has flooded, and a survivor outpost has taken over an old roadside service depot. The silhouettes tell the story: a broken radio mast in the northwest, a concrete dam in the east, and two ashworks chimneys in the southeast.

The mood is lonely and weathered, with pockets of warmth. Use soot, rust, exposed concrete, dead pines, washed-out signs, and improvised repairs. Reserve saturated amber for inhabited places. Zombies are an optional later direction; the region also works with human scavengers and environmental hazards.

Open `region-map.svg` for the exact layout. `region-layout.json` is the source of truth for coordinates, routes, and build phases. Any illustrated concept map is an art reference; use the JSON and vector map if the illustration differs.

## Scale and layout

- Full region: **3,000 × 3,000 m**, nine 1 km planning tiles.
- First playable area: **600 × 600 m**, from x/z 250 to 850, around Cinderhaven.
- Coordinate system: 1 Unity unit = 1 m; +X east, +Z north, +Y up. Southwest = (0, 0) on the XZ plane. Heights are determined by terrain; the JSON contains X/Z pairs, not fixed Y positions.
- Assumed workflow: desktop PC, third-person exploration, Unity 6 with URP. Pin the actual editor and compatible package versions when creating the project. No multiplayer or vehicle system is required for the initial build.

| Place | X, Z (m) | Role | Visual identity |
|---|---:|---|---|
| Cinderhaven | 480, 480 | Safe hub; stash, water, first task | Depot buildings, scrap fence, amber lamps |
| Old Orchard | 550, 1350 | Early food and tools | Abandoned farm, greenhouse ribs, living trees |
| Dead Signal Ridge | 580, 2460 | Navigation landmark; later radio task | Broken mast, wind, rocky switchback |
| Blackpine Burn | 1500, 2400 | Concealed salvage route | Charred trunks, pale ash, abandoned camps |
| Rustline Yard | 1510, 1680 | Mid-region salvage and route choice | Parallel tracks, freight cars, depot roof |
| Glasswater | 1450, 1050 | Flooded town; medical supplies | Rooftop paths, pharmacy/hospital sign, still water |
| Red Quarry | 2510, 2400 | High-exposure materials site | Stepped orange cut, conveyors, haul-road loops |
| Mercy Dam | 2190, 1510 | Controlled crossing; later shortcut | Spillway, sluice house, visible upstream reservoir |
| The Ashworks | 2550, 450 | Late-region industrial objective | Twin chimneys, pipes, collapsed processing halls |

Keep the dam's accessible deck continuous. The railway's broken span is visibly blocked; it is not an assumed traversable route. The initial route to the Ashworks uses the dam road. A second, southern river crossing is a later unlock, so the eastern route does not remain a permanent dead end.

## Exploration flow

1. Learn the outpost, collect a battery from the roadside wreck, and power the nearby relay inside the starter area. Return to an illuminated gate and a working radio. This is the first build target, not a promise of systems already implemented.
2. Travel north to Old Orchard, then choose the western ridge or the central rail yard. Hills and ruined walls hide new views; the mast and chimneys retain orientation.
3. Connect the western exploration loop: Cinderhaven → Orchard → Ridge → Blackpine → Rustline → Glasswater → Cinderhaven.
4. Cross Mercy Dam to reach the quarry or Ashworks. Industrial filters and warning signs telegraph the ash zone before a hazard mechanic is introduced.

Place a small story, resource, or route decision every roughly 100–200 m along traveled paths, not on a uniform grid. Prototype movement before fixing these distances. The nine major sites are destinations; intermediate stops keep the connecting terrain useful. Avoid filling the entire basin with buildings.

## Art recipe

| Use | Color |
|---|---|
| Soot and burnt timber | `#292C29` |
| Weathered concrete | `#8E9184` |
| Dry grass and dust | `#B5A07A` |
| Oxidized metal | `#A65F3E` |
| Surviving foliage | `#64745B` |
| Floodwater | `#426E70` |
| Occupied lights | `#E7AD54` |

Use broad readable geometry and restrained texture detail. Weather the world through missing roof sections, boards, blocked doors, rubble clusters, recolored materials, and asymmetric prop placement. Imported intact houses do not automatically become ruins. The dam, mast, processing plant, quarry conveyors, and damaged building variants are custom assembly tasks. Build their silhouettes with cubes, cylinders, and reusable modules before making detailed meshes.

URP setup: one directional sun, a global Volume, subdued saturation, restrained bloom for lamps, and distance fog supported by the selected URP version. Start with static water and inexpensive ash particles. Do not depend on HDRP volumetrics or paid terrain, water, road, or atmosphere packages.

## Build order

**Phase 1 — Starter loop:** one 600 m terrain, depot hub, salvage wreck, relay, two routes, simple third-person movement, interaction, one working battery objective, return feedback. Use placeholders for anything not imported.

**Phase 2 — Art test:** import only the four core packs in ASSETS.md. Rebuild materials for URP where necessary. Establish one outdoor scene with a building, vehicle, survivor prop, and tree before populating the region. Verify scale, color, collisions, and animation.

**Phase 3 — Starter polish:** replace placeholders, add limited ambience, bake navigation for the walkable slice, add visibility blockers and LODs, and measure performance on the target PC. A 60 fps goal is a target to measure, not a verified result.

**Phase 4 — Regional expansion:** use the nine planning tiles as additive scene boundaries if profiling and scene size justify it. Start with the southwest tile and add adjoining tiles; do not build a streaming framework before the first loop works. Match terrain edge heights, keep shared light/player/services persistent, and prevent duplicate global objects.

**Phase 5 — Landmark and route completion:** custom dam and factory modules, quarry, flooding, shortcuts, navigation connections, and save/load. Design interiors selectively; the initial town buildings may be exterior shells.

## Contents and next action

- `region-map.svg`: editable, precise overhead plan.
- `region-map.png`: exported blueprint for quick viewing or sharing.
- `region-concept.png`: illustrated art-direction map; the blueprint controls precise placement.
- `region-layout.json`: machine-readable POIs, path polylines, water, starter bounds, and phase definitions.
- `ASSETS.md`: free-first asset shortlist, source evidence, import guidance, and remaining custom work.
- `CLAUDE_HANDOFF.md`: a prompt and acceptance checklist for a coding assistant with access to the Unity project and editor.
- `render_map.py`: standard-library Python renderer; run beside the JSON to refresh the SVG after coordinate edits.

Begin with the four core asset links in ASSETS.md, then give Claude this folder plus the prompt. Claude still needs local files and a runnable Unity installation to import assets, assemble scenes, and demonstrate the result.
