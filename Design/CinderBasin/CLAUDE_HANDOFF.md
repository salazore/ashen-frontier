# Prompt to give Claude

Copy the text below into a coding assistant that can access your Unity project. Attach this entire design folder and the downloaded assets, or provide their local paths. A chat-only assistant can write scripts but cannot demonstrate an assembled Unity scene without editor access.

---

Build the first playable environment for **Ashen Frontier**, using the attached **Cinder Basin** design.

Read `README.md`, `ASSETS.md`, and `region-layout.json` first. Treat the JSON coordinates and vector map as authoritative. Use the illustrated map only for art direction.

Use the existing repository checkout; each cloud task is already isolated, so do not create a Git worktree unless I explicitly request one. Inspect the repository and preserve existing files and changes. If this is still an empty repository, initialize a Unity 6 URP project using an installed, supported editor and record its exact version. If no Unity editor is available, finish the source/blockout tooling you can, then report that scene creation and engine validation remain unrun; do not claim a playable build.

Target a stylized third-person PC prototype using free assets first. Do not buy assets, import premium editions, or assume advertised engine-specific shaders are included in a free download. Read the actual archive licenses and keep restricted source assets out of a public repository. Use only imported files that exist. If an asset is missing, use a clearly named primitive placeholder and list it; do not invent prefab paths or download IDs.

**Build Phase 1 only before expanding the region:**

1. Use 1 Unity unit = 1 m, +X east, +Z north, +Y up. Create the 600 × 600 m starter area with world X/Z bounds 250–850, not the whole 9 km² region. Keep coordinates compatible with later region tiles. Sample actual terrain height for every placement; do not put all objects at Y=0.
2. Create a persistent bootstrap scene and one starter-area scene. Set up a third-person controller using the project's compatible input configuration, camera collision, ground detection and sensible slopes. Avoid building inventory, multiplayer, vehicles or streaming frameworks before the objective loop works.
3. Place Cinderhaven around X=480, Z=480: a small scrap-depot safe area, fence opening, stash placeholder, water point, amber light and spawn. Add the roadside salvage wreck near X=750, Z=450 and a relay near X=770, Z=760. Keep the local footpaths clear, with an optional return route via the water-tower landmark near X=600, Z=630.
4. Implement the smallest demonstrable loop: interact with the wreck to take one battery, take it to the relay, activate the relay, then return to a visibly changed outpost gate/radio. Provide clear prompts and a visible objective state. Prevent taking the unique battery twice or consuming it before the relay interaction succeeds. Save/load is not required in this phase.
5. Implement an editor builder with a menu item such as `Ashen Frontier/Build Starter Area`. Use region-layout.json or a matching serialized layout asset. Use a fixed seed, keep all generated objects under one root, and make rerunning the builder replace only its own generated objects. Use Undo where practical. Do not overwrite hand-authored scenes/prefabs without a safe separate output path. Provide a prefab mapping inspector; missing mappings should create labeled placeholders and a report.
6. Import-test the four core packs, then apply muted rust/ash/sage materials through project-owned variants. Keep vendor folders separate. Validate scale, colliders and any animation rig used. Add simple static water only if needed in the slice; the full river is outside it.
7. Build a navigable human-scale environment: no floating props, blocked mandatory route, invisible water walls, missing collisions or giant collision meshes preventing interaction. AI enemies are optional; if included, bake a NavMesh for the slice and confirm an agent can traverse it.
8. Use a restrained URP lighting setup, fog compatible with the installed pipeline, modest ash particles, and warm safe-hub lights. Terrain and silhouettes should do most of the work. Add no post-processing package that conflicts with the selected URP version.

**Acceptance checks you must actually perform when editor access is available:**

- The project opens and scripts compile without errors. Package and input settings match the installed editor.
- Running the builder twice leaves one generated starter root and one set of objective locations; no duplicates. It preserves unrelated objects/files.
- Enter Play mode at the spawn and walk to the wreck, relay, and home gate without teleporting or passing through terrain/mandatory structures.
- Complete the battery objective once and verify the outpost feedback changes. Attempt repeated interactions and verify they do not duplicate the battery or the completion reward.
- Inspect materials in the Game view; no missing/pink shaders. Check human scale with an actual player capsule.
- Produce Game-view screenshots and a short route/objective test report. If Unity can build locally, make and launch a development build and report its result. Do not call a successful code write a tested build.
- Profile on an identified target PC before claiming a frame-rate result. State hardware, scene and resolution with any performance numbers.

Return changed file paths, exact editor/package versions, build/menu instructions, screenshots, tests that actually ran, and unresolved placeholders or failures. Keep environment setup problems distinct from application defects. Do not continue into all nine region tiles until this slice is working and reviewed.

---

After the starter works, a separate follow-up can expand along the western loop, then add Mercy Dam and the industrial east. The JSON contains the region plan; it is not a terrain heightmap or a finished scene.
