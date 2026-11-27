# Jo Makes the Call — A6 Amber Noir prompt package

Approved storyboard · 60 s · 9:16 vertical · English narration

## How to use this

1. **Generate the two identity sheets first** (Jo, neighbor) in your image tool with the listed style reference attached. Pick the best of each.
2. **Generate each shot's first frame** (s01–s10). Attach the style reference listed for that shot **and** the approved Jo / neighbor identity sheets where those characters appear.
3. **In Google Flow** choose *Veo 3.1 Fast*, 9:16, the lowest resolution for tests (720p for final), 8 s, frames-to-video. Upload the shot's first frame, paste its motion prompt, generate. Check the model/duration options Flow currently shows; they may have changed.
4. Keep only the best range from each clip (see timing). Reject clips where characters talk, gain extra limbs, change clothes, or the action is unclear.
5. Narration, sound effects, title and captions are added afterwards (see Finishing).

Style reference files (bundled with the skill, in `.claude/skills/directing-stickman-videos/assets/a6/`): `apartment-style-example.png`, `cafe-face-and-light.jpg`, `shop-full-body.jpg`. They set the drawing and lighting style only — not the characters' clothes.

## Narration (record separately — Gemini TTS, voice *Puck*)

Delivery: curious, engaged storytelling; slight intrigue at the opening, calm and clear on the rules, warm relief at the end. Not a flat announcer.

```text
It's 11 p.m. Jo's neighbor just collapsed at the bus stop. Her hands are shaking. What she does next matters.
Rule one: call 911 only for real emergencies — when someone's life, safety or property is in danger right now. This counts.
Rule two: say where you are first. Street, cross street, a landmark. If the call drops, help can still find you.
Rule three: say what happened, in plain words. "A man collapsed. He isn't breathing normally."
Rule four: answer every question. The dispatcher asks because help is already on the way.
Rule five: don't hang up until they tell you to. If they say push hard and fast on his chest — you do it.
And if you ever dial by accident? Stay on the line and say so. Hanging up means they have to call back to check on you.
Sirens. Lights. Jo did everything right.
Know the rules — before you need them.
```

## Timing and sound

| Shot | Final time | Beat | Sound effects |
|---|---|---|---|
| s01 | 0:00–0:05 | Collapse, bag drops | thud, paper bag spill, distant traffic |
| s02 | 0:05–0:08 | Taps 9-1-1 | 3 phone taps, low heartbeat thump |
| s03 | 0:08–0:14 | Rule 1: real emergency | phone ring tone |
| s04 | 0:14–0:21 | Rule 2: location first | neon hum |
| s05 | 0:21–0:27 | Rule 3: what happened | soft wind |
| s06 | 0:27–0:33 | Rule 4: answer questions | soft breath |
| s07 | 0:33–0:41 | Rule 5: stay on, follow instructions (CPR) | rhythmic chest presses |
| s08 | 0:41–0:49 | Accidental dial: stay on the line | phone buzz, TV murmur |
| s09 | 0:49–0:55 | Help arrives | siren rising, van doors |
| s10 | 0:55–1:00 | Relief, closing line | siren fading |

Final cut times follow the recorded narration. Each 8 s clip supplies only the retained range; do not speed up the voice to fit.

## Identity sheets

### jo-identity
Style reference to attach: `shop-body`

```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. Jo: a slim young-adult stick figure wearing a fitted deep-teal zip-up jacket with the zip half closed, charcoal-grey straight pants, black shoes and a small dark-brown cross-body bag on a thin strap over her right shoulder. Bare round black head, no hair, no hood. Shown standing neutral, both hands empty, small calm smile. Plain deep-plum studio backdrop with one warm amber side light; no props or location. Identity sheet: front view, three-quarter view and side view of Jo, full body, same scale, clear gaps between views. Identity reference only, not a video opening frame. Copy only the reference's drawing and light grammar, not its orange hoodie or shop. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

### neighbor-identity
Style reference to attach: `shop-body`

```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. The neighbor: an older stick figure, slightly shorter and stooped, wearing a mustard-yellow knit cardigan over a cream shirt, brown trousers and a brown flat cap on the round black head. Shown standing neutral with hands at his sides. Plain deep-plum studio backdrop with one warm amber side light; no props or location. Identity sheet: front, three-quarter and side full-body views of the neighbor, same scale, clear gaps. Identity reference only. Copy only the reference's drawing and light grammar, not its orange hoodie or shop. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

## Shots — first-frame image prompt + motion prompt

### s01 · 0:00–0:05 · Collapse, bag drops
Attach: `apartment-style-example.png` (style) + approved Jo sheet + neighbor sheet (identity)

**First-frame image prompt**
```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. Jo: a slim young-adult stick figure wearing a fitted deep-teal zip-up jacket with the zip half closed, charcoal-grey straight pants, black shoes and a small dark-brown cross-body bag on a thin strap over her right shoulder. Bare round black head, no hair, no hood. The neighbor: an older stick figure, slightly shorter and stooped, wearing a mustard-yellow knit cardigan over a cream shirt, brown trousers and a brown flat cap on the round black head. A quiet city bus stop at 11 p.m.: a slim glass bus shelter with a wooden bench, one tall amber streetlamp, wet dark-plum asphalt with soft reflections, a brick building behind with a glowing amber corner-store window, a green street-name sign on a pole at the corner, distant violet apartment silhouettes. Wide vertical shot from the sidewalk. The neighbor sits at the left end of the bench, swaying, one hand on his chest, starting to tip sideways. Jo walks in from the right holding a paper grocery bag against her hip, head turning toward him. Streetlamp top-center. Grocery bag is a plain brown paper bag with a baguette and greens poking out. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

**Flow motion prompt** (Veo 3.1 Fast · 9:16 · 8 s · first frame attached)
```text
The older man in the mustard cardigan slowly tips sideways off the bench and slumps onto the pavement. The young woman in the teal jacket stops, startles, and drops her paper grocery bag, which spills. Slow push-in. Silent actors, no talking, mouths stay still. Quiet night ambience only.
```

### s02 · 0:05–0:08 · Taps 9-1-1
Attach: `cafe-face-and-light.jpg` (style) + approved Jo sheet (identity)

**First-frame image prompt**
```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. Jo: a slim young-adult stick figure wearing a fitted deep-teal zip-up jacket with the zip half closed, charcoal-grey straight pants, black shoes and a small dark-brown cross-body bag on a thin strap over her right shoulder. Bare round black head, no hair, no hood. A quiet city bus stop at 11 p.m.: a slim glass bus shelter with a wooden bench, one tall amber streetlamp, wet dark-plum asphalt with soft reflections, a brick building behind with a glowing amber corner-store window, a green street-name sign on a pole at the corner, distant violet apartment silhouettes. Background softly out of focus. Vertical close-up of Jo from chest up, three-quarter view. She holds a black smartphone in her right hand in front of her chest, screen facing her, its cool white glow lighting the lower half of her face against the amber streetlight. Wide alarmed eyes, mouth a small closed line. Phone screen shows only a soft blank glow, no digits. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

**Flow motion prompt** (Veo 3.1 Fast · 9:16 · 8 s · first frame attached)
```text
The woman in the teal jacket quickly taps the phone screen three times with her thumb, then lifts the phone toward her ear. Slight handheld drift. Silent actor, no talking, mouth stays a still line. Quiet ambience only.
```

### s03 · 0:08–0:14 · Rule 1: real emergency
Attach: `apartment-style-example.png` (style) + approved Jo sheet + neighbor sheet (identity)

**First-frame image prompt**
```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. Jo: a slim young-adult stick figure wearing a fitted deep-teal zip-up jacket with the zip half closed, charcoal-grey straight pants, black shoes and a small dark-brown cross-body bag on a thin strap over her right shoulder. Bare round black head, no hair, no hood. The neighbor: an older stick figure, slightly shorter and stooped, wearing a mustard-yellow knit cardigan over a cream shirt, brown trousers and a brown flat cap on the round black head. A quiet city bus stop at 11 p.m.: a slim glass bus shelter with a wooden bench, one tall amber streetlamp, wet dark-plum asphalt with soft reflections, a brick building behind with a glowing amber corner-store window, a green street-name sign on a pole at the corner, distant violet apartment silhouettes. Vertical medium shot. The neighbor lies on his back on the wet pavement in front of the bench, cap fallen beside him, eyes closed. Jo kneels on one knee at his right side, phone held to her left ear with her left hand, right hand resting on his shoulder, face turned toward him. Dropped grocery bag spilled behind her. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

**Flow motion prompt** (Veo 3.1 Fast · 9:16 · 8 s · first frame attached)
```text
The kneeling woman holds the phone to her ear and gently shakes the man's shoulder, glancing between him and the street. Static camera. Silent actor, no talking, mouth stays still. Quiet ambience only.
```

### s04 · 0:14–0:21 · Rule 2: location first
Attach: `shop-full-body.jpg` (style) + approved Jo sheet (identity)

**First-frame image prompt**
```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. Jo: a slim young-adult stick figure wearing a fitted deep-teal zip-up jacket with the zip half closed, charcoal-grey straight pants, black shoes and a small dark-brown cross-body bag on a thin strap over her right shoulder. Bare round black head, no hair, no hood. A quiet city bus stop at 11 p.m.: a slim glass bus shelter with a wooden bench, one tall amber streetlamp, wet dark-plum asphalt with soft reflections, a brick building behind with a glowing amber corner-store window, a green street-name sign on a pole at the corner, distant violet apartment silhouettes. Low-angle vertical shot looking up past Jo, who kneels in the lower third with the phone at her ear and her right arm raised, pointing toward the green street-name sign on its pole and the glowing corner-store window in the upper half of the frame. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

**Flow motion prompt** (Veo 3.1 Fast · 9:16 · 8 s · first frame attached)
```text
The kneeling woman raises her arm and points firmly at the street sign and the glowing store window, then looks back down. Slow tilt up toward the sign. Silent actor, no talking, mouth still. Quiet ambience only.
```

### s05 · 0:21–0:27 · Rule 3: what happened
Attach: `cafe-face-and-light.jpg` (style) + approved Jo sheet + neighbor sheet (identity)

**First-frame image prompt**
```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. Jo: a slim young-adult stick figure wearing a fitted deep-teal zip-up jacket with the zip half closed, charcoal-grey straight pants, black shoes and a small dark-brown cross-body bag on a thin strap over her right shoulder. Bare round black head, no hair, no hood. The neighbor: an older stick figure, slightly shorter and stooped, wearing a mustard-yellow knit cardigan over a cream shirt, brown trousers and a brown flat cap on the round black head. A quiet city bus stop at 11 p.m.: a slim glass bus shelter with a wooden bench, one tall amber streetlamp, wet dark-plum asphalt with soft reflections, a brick building behind with a glowing amber corner-store window, a green street-name sign on a pole at the corner, distant violet apartment silhouettes. Background softly blurred. Vertical close-up of Jo's head and shoulders, phone at her left ear, her right open hand gesturing down and out of frame toward the neighbor, whose mustard sleeve and cap are visible at the bottom edge. Focused, serious expression, mouth a small closed line. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

**Flow motion prompt** (Veo 3.1 Fast · 9:16 · 8 s · first frame attached)
```text
The woman, phone at her ear, gestures down toward the man with her open hand, then nods once, listening. Very slow push-in. Silent actor, no talking, mouth stays a still line. Quiet ambience only.
```

### s06 · 0:27–0:33 · Rule 4: answer questions
Attach: `apartment-style-example.png` (style) + approved Jo sheet + neighbor sheet (identity)

**First-frame image prompt**
```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. Jo: a slim young-adult stick figure wearing a fitted deep-teal zip-up jacket with the zip half closed, charcoal-grey straight pants, black shoes and a small dark-brown cross-body bag on a thin strap over her right shoulder. Bare round black head, no hair, no hood. The neighbor: an older stick figure, slightly shorter and stooped, wearing a mustard-yellow knit cardigan over a cream shirt, brown trousers and a brown flat cap on the round black head. A quiet city bus stop at 11 p.m.: a slim glass bus shelter with a wooden bench, one tall amber streetlamp, wet dark-plum asphalt with soft reflections, a brick building behind with a glowing amber corner-store window, a green street-name sign on a pole at the corner, distant violet apartment silhouettes. Vertical over-the-shoulder shot from behind Jo's right shoulder: she leans over the neighbor lying on his back, watching his chest, phone pressed to her ear. The neighbor's face and mustard cardigan are lit by the amber streetlamp. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

**Flow motion prompt** (Veo 3.1 Fast · 9:16 · 8 s · first frame attached)
```text
The woman leans closer, watching the man's chest, then nods and presses the phone tighter to her ear. Static over-the-shoulder camera. Silent actor, no talking, mouth still. Quiet ambience only.
```

### s07 · 0:33–0:41 · Rule 5: stay on, follow instructions (CPR)
Attach: `apartment-style-example.png` (style) + approved Jo sheet + neighbor sheet (identity)

**First-frame image prompt**
```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. Jo: a slim young-adult stick figure wearing a fitted deep-teal zip-up jacket with the zip half closed, charcoal-grey straight pants, black shoes and a small dark-brown cross-body bag on a thin strap over her right shoulder. Bare round black head, no hair, no hood. The neighbor: an older stick figure, slightly shorter and stooped, wearing a mustard-yellow knit cardigan over a cream shirt, brown trousers and a brown flat cap on the round black head. Wet dark-plum pavement in front of a bus-shelter bench under amber streetlight, from above. Top-down vertical shot. The neighbor lies on his back, cap beside his head. Jo kneels at his right side, both hands stacked flat on the center of his chest, arms straight. Her black smartphone lies face-up on the pavement by her knee, glowing softly. Phone screen shows only a blank glow. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

**Flow motion prompt** (Veo 3.1 Fast · 9:16 · 8 s · first frame attached)
```text
The woman pushes down on the center of the man's chest with straight arms in a steady fast rhythm, the phone glowing on the pavement beside her. Static top-down camera. Silent actor, no talking. Quiet ambience only.
```

### s08 · 0:41–0:49 · Accidental dial: stay on the line
Attach: `apartment-style-example.png` (style)

**First-frame image prompt**
```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. A relaxed adult stick figure wearing a loose heather-grey hoodie with the hood down and dark-blue sweatpants, bare round black head. A cozy apartment living room at night: a worn burgundy couch, a low wooden coffee table with a bowl of popcorn, a glowing TV off-frame casting flickering amber light, a tall window with violet city lights, deep plum walls. Vertical medium-wide shot. The man sits slouched on the couch, holding a black smartphone up to his ear with his left hand, his right hand raised palm-out in an apologetic gesture, head tilted, sheepish expression with the mouth a small closed line. No bus stop, no Jo, no neighbor in this scene. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

**Flow motion prompt** (Veo 3.1 Fast · 9:16 · 8 s · first frame attached)
```text
The man on the couch notices the phone glowing, lifts it to his ear, raises his free hand in an apologetic wave and shrugs sheepishly. Static camera. Silent actor, no talking, mouth stays still. Quiet TV ambience only.
```

### s09 · 0:49–0:55 · Help arrives
Attach: `apartment-style-example.png` (style) + approved Jo sheet + neighbor sheet (identity)

**First-frame image prompt**
```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. Jo: a slim young-adult stick figure wearing a fitted deep-teal zip-up jacket with the zip half closed, charcoal-grey straight pants, black shoes and a small dark-brown cross-body bag on a thin strap over her right shoulder. Bare round black head, no hair, no hood. The neighbor: an older stick figure, slightly shorter and stooped, wearing a mustard-yellow knit cardigan over a cream shirt, brown trousers and a brown flat cap on the round black head. Two paramedics shown as darker silhouettes in navy uniforms with reflective silver stripes on sleeves and trousers, faces turned away from camera. A quiet city bus stop at 11 p.m.: a slim glass bus shelter with a wooden bench, one tall amber streetlamp, wet dark-plum asphalt with soft reflections, a brick building behind with a glowing amber corner-store window, a green street-name sign on a pole at the corner, distant violet apartment silhouettes. An ambulance is pulling up at the curb on the left, its light bar casting red and blue light across the scene, mixed with the amber streetlight. Vertical wide shot. Jo still kneels beside the neighbor with hands on his chest, turning her head toward the ambulance. The two paramedic silhouettes hurry in from the left carrying a medical bag. Ambulance has no text or logos; just a white body with a red stripe. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

**Flow motion prompt** (Veo 3.1 Fast · 9:16 · 8 s · first frame attached)
```text
Red and blue light sweeps across the scene as the ambulance stops; two paramedics hurry in and kneel beside the man while the woman looks up and moves aside. Slow pull-back. Silent actors, no talking. Quiet ambience only.
```

### s10 · 0:55–1:00 · Relief, closing line
Attach: `cafe-face-and-light.jpg` (style) + approved Jo sheet (identity)

**First-frame image prompt**
```text
Two-dimensional A6 'Amber Noir' illustration in a vertical 9:16 frame: compact matte-black round heads joined to the torso by a short connected black neck, small cream-white oval eye marks, a compact cream line mouth, simplified black mitten-like hands and slim black stick limbs with readable silhouettes. Angular drawn contours, restrained cel shading, warm amber key light falling into deep plum and violet shadows, a thin warm rim light on figures, layered full-color illustrated environment. Not glossy 3D toys, not photoreal people. Jo: a slim young-adult stick figure wearing a fitted deep-teal zip-up jacket with the zip half closed, charcoal-grey straight pants, black shoes and a small dark-brown cross-body bag on a thin strap over her right shoulder. Bare round black head, no hair, no hood. A quiet city bus stop at 11 p.m.: a slim glass bus shelter with a wooden bench, one tall amber streetlamp, wet dark-plum asphalt with soft reflections, a brick building behind with a glowing amber corner-store window, a green street-name sign on a pole at the corner, distant violet apartment silhouettes. In the soft background, red and blue ambulance light glows and the paramedics' silhouettes crouch by the bench. Vertical medium shot of Jo standing on the sidewalk in the foreground, phone lowered in her right hand at her side, left hand on her chest, shoulders dropping as she exhales, looking toward the camera with tired relief. Amber key light on her face, red-blue rim light from behind. No readable words, letters, numbers, logos, captions or watermark anywhere; street signs and store signs are blank shapes or abstract glyphs. Every figure has exactly two arms, two legs, one head on a connected short neck, feet grounded; no floating limbs, no realistic fingers, no speech bubbles.
```

**Flow motion prompt** (Veo 3.1 Fast · 9:16 · 8 s · first frame attached)
```text
The woman lets her shoulders drop, exhales deeply, lowers her head briefly, then looks up toward the camera with tired relief. Red and blue light pulses softly behind her. Very slow push-in. Silent actor, no talking, mouth still. Quiet ambience only.
```

## Finishing

- **Title** (top-left, pure white, persistent): `THE 5 RULES OF` / `CALLING 911`.
- **Captions**: ALL CAPS, Impact, cream-white with black outline, bottom-center, 1–2 meaningful lines; the word being spoken highlighted amber; short pop on each new phrase.
- **Sound**: narration on top; effects from the timing table; mix around −16 LUFS, peaks ≤ −1 dBTP. No music required.
- No watermark.
- If you bring the clips and narration back to a Claude session, the skill's `a6_finish.py` adds the title and captions automatically.
