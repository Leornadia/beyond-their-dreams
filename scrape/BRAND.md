# Beyond Their Dreams — Brand Palette & Type System

Refined from inline CSS on `https://www.beyondtheirdreams.com/`. 
Wix editor UI defaults are flagged separately so they don't pollute the brand palette.

## Wix theme palette — canonical brand colors

Wix stores 60+ slots, mostly duplicates. Below is the deduplicated palette the site is actually built from.

| Swatch | Hex | Wix slot(s) |
|---|---|---|
| <span style="display:inline-block;width:24px;height:24px;background:#ffffff;border:1px solid #999"></span> | `#ffffff` | --color_0, --color_1, --color_8 |
| <span style="display:inline-block;width:24px;height:24px;background:#ceecea;border:1px solid #999"></span> | `#ceecea` | --color_11, --color_36, --color_50, --color_51, --color_56, --color_57… |
| <span style="display:inline-block;width:24px;height:24px;background:#eaded6;border:1px solid #999"></span> | `#eaded6` | --color_21, --color_31 |
| <span style="display:inline-block;width:24px;height:24px;background:#c0e2df;border:1px solid #999"></span> | `#c0e2df` | --color_16, --color_44 |
| <span style="display:inline-block;width:24px;height:24px;background:#d4d5d6;border:1px solid #999"></span> | `#d4d5d6` | --color_26 |
| <span style="display:inline-block;width:24px;height:24px;background:#a2d9d6;border:1px solid #999"></span> | `#a2d9d6` | --color_12, --color_38 |
| <span style="display:inline-block;width:24px;height:24px;background:#ffcb05;border:1px solid #999"></span> | `#ffcb05` | --color_5 |
| <span style="display:inline-block;width:24px;height:24px;background:#bbb2ab;border:1px solid #999"></span> | `#bbb2ab` | --color_22, --color_32 |
| <span style="display:inline-block;width:24px;height:24px;background:#b0b0b0;border:1px solid #999"></span> | `#b0b0b0` | --color_7, --color_10 |
| <span style="display:inline-block;width:24px;height:24px;background:#9ab5b2;border:1px solid #999"></span> | `#9ab5b2` | --color_17 |
| <span style="display:inline-block;width:24px;height:24px;background:#aaacae;border:1px solid #999"></span> | `#aaacae` | --color_27 |
| <span style="display:inline-block;width:24px;height:24px;background:#7aa3a1;border:1px solid #999"></span> | `#7aa3a1` | --color_13, --color_39, --color_54, --color_55, --color_64, --color_65 |
| <span style="display:inline-block;width:24px;height:24px;background:#8c8580;border:1px solid #999"></span> | `#8c8580` | --color_23, --color_33 |
| <span style="display:inline-block;width:24px;height:24px;background:#808285;border:1px solid #999"></span> | `#808285` | --color_28 |
| <span style="display:inline-block;width:24px;height:24px;background:#738886;border:1px solid #999"></span> | `#738886` | --color_18, --color_41, --color_46, --color_48, --color_49, --color_52… |
| <span style="display:inline-block;width:24px;height:24px;background:#727272;border:1px solid #999"></span> | `#727272` | --color_6, --color_9 |
| <span style="display:inline-block;width:24px;height:24px;background:#0088cb;border:1px solid #999"></span> | `#0088cb` | --color_4 |
| <span style="display:inline-block;width:24px;height:24px;background:#516d6b;border:1px solid #999"></span> | `#516d6b` | --color_14, --color_40, --color_47 |
| <span style="display:inline-block;width:24px;height:24px;background:#ed1c24;border:1px solid #999"></span> | `#ed1c24` | --color_3 |
| <span style="display:inline-block;width:24px;height:24px;background:#5e5956;border:1px solid #999"></span> | `#5e5956` | --color_24, --color_34 |
| <span style="display:inline-block;width:24px;height:24px;background:#555759;border:1px solid #999"></span> | `#555759` | --color_29 |
| <span style="display:inline-block;width:24px;height:24px;background:#4d5a59;border:1px solid #999"></span> | `#4d5a59` | --color_19, --color_42 |
| <span style="display:inline-block;width:24px;height:24px;background:#293636;border:1px solid #999"></span> | `#293636` | --color_15, --color_37, --color_45 |
| <span style="display:inline-block;width:24px;height:24px;background:#2f2c2b;border:1px solid #999"></span> | `#2f2c2b` | --color_25, --color_35 |
| <span style="display:inline-block;width:24px;height:24px;background:#2b2b2c;border:1px solid #999"></span> | `#2b2b2c` | --color_30 |
| <span style="display:inline-block;width:24px;height:24px;background:#262d2d;border:1px solid #999"></span> | `#262d2d` | --color_20, --color_43 |
| <span style="display:inline-block;width:24px;height:24px;background:#000000;border:1px solid #999"></span> | `#000000` | --color_2 |

<details><summary>All 60+ raw Wix slots</summary>

| Slot | Swatch | Hex | Raw value |
|---|---|---|---|
| `--color_0` | <span style="display:inline-block;width:18px;height:18px;background:#ffffff;border:1px solid #999"></span> | `#ffffff` | `255,255,255` |
| `--color_1` | <span style="display:inline-block;width:18px;height:18px;background:#ffffff;border:1px solid #999"></span> | `#ffffff` | `255,255,255` |
| `--color_2` | <span style="display:inline-block;width:18px;height:18px;background:#000000;border:1px solid #999"></span> | `#000000` | `0,0,0` |
| `--color_3` | <span style="display:inline-block;width:18px;height:18px;background:#ed1c24;border:1px solid #999"></span> | `#ed1c24` | `237,28,36` |
| `--color_4` | <span style="display:inline-block;width:18px;height:18px;background:#0088cb;border:1px solid #999"></span> | `#0088cb` | `0,136,203` |
| `--color_5` | <span style="display:inline-block;width:18px;height:18px;background:#ffcb05;border:1px solid #999"></span> | `#ffcb05` | `255,203,5` |
| `--color_6` | <span style="display:inline-block;width:18px;height:18px;background:#727272;border:1px solid #999"></span> | `#727272` | `114,114,114` |
| `--color_7` | <span style="display:inline-block;width:18px;height:18px;background:#b0b0b0;border:1px solid #999"></span> | `#b0b0b0` | `176,176,176` |
| `--color_8` | <span style="display:inline-block;width:18px;height:18px;background:#ffffff;border:1px solid #999"></span> | `#ffffff` | `255,255,255` |
| `--color_9` | <span style="display:inline-block;width:18px;height:18px;background:#727272;border:1px solid #999"></span> | `#727272` | `114,114,114` |
| `--color_10` | <span style="display:inline-block;width:18px;height:18px;background:#b0b0b0;border:1px solid #999"></span> | `#b0b0b0` | `176,176,176` |
| `--color_11` | <span style="display:inline-block;width:18px;height:18px;background:#ceecea;border:1px solid #999"></span> | `#ceecea` | `206,236,234` |
| `--color_12` | <span style="display:inline-block;width:18px;height:18px;background:#a2d9d6;border:1px solid #999"></span> | `#a2d9d6` | `162,217,214` |
| `--color_13` | <span style="display:inline-block;width:18px;height:18px;background:#7aa3a1;border:1px solid #999"></span> | `#7aa3a1` | `122,163,161` |
| `--color_14` | <span style="display:inline-block;width:18px;height:18px;background:#516d6b;border:1px solid #999"></span> | `#516d6b` | `81,109,107` |
| `--color_15` | <span style="display:inline-block;width:18px;height:18px;background:#293636;border:1px solid #999"></span> | `#293636` | `41,54,54` |
| `--color_16` | <span style="display:inline-block;width:18px;height:18px;background:#c0e2df;border:1px solid #999"></span> | `#c0e2df` | `192,226,223` |
| `--color_17` | <span style="display:inline-block;width:18px;height:18px;background:#9ab5b2;border:1px solid #999"></span> | `#9ab5b2` | `154,181,178` |
| `--color_18` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_19` | <span style="display:inline-block;width:18px;height:18px;background:#4d5a59;border:1px solid #999"></span> | `#4d5a59` | `77,90,89` |
| `--color_20` | <span style="display:inline-block;width:18px;height:18px;background:#262d2d;border:1px solid #999"></span> | `#262d2d` | `38,45,45` |
| `--color_21` | <span style="display:inline-block;width:18px;height:18px;background:#eaded6;border:1px solid #999"></span> | `#eaded6` | `234,222,214` |
| `--color_22` | <span style="display:inline-block;width:18px;height:18px;background:#bbb2ab;border:1px solid #999"></span> | `#bbb2ab` | `187,178,171` |
| `--color_23` | <span style="display:inline-block;width:18px;height:18px;background:#8c8580;border:1px solid #999"></span> | `#8c8580` | `140,133,128` |
| `--color_24` | <span style="display:inline-block;width:18px;height:18px;background:#5e5956;border:1px solid #999"></span> | `#5e5956` | `94,89,86` |
| `--color_25` | <span style="display:inline-block;width:18px;height:18px;background:#2f2c2b;border:1px solid #999"></span> | `#2f2c2b` | `47,44,43` |
| `--color_26` | <span style="display:inline-block;width:18px;height:18px;background:#d4d5d6;border:1px solid #999"></span> | `#d4d5d6` | `212,213,214` |
| `--color_27` | <span style="display:inline-block;width:18px;height:18px;background:#aaacae;border:1px solid #999"></span> | `#aaacae` | `170,172,174` |
| `--color_28` | <span style="display:inline-block;width:18px;height:18px;background:#808285;border:1px solid #999"></span> | `#808285` | `128,130,133` |
| `--color_29` | <span style="display:inline-block;width:18px;height:18px;background:#555759;border:1px solid #999"></span> | `#555759` | `85,87,89` |
| `--color_30` | <span style="display:inline-block;width:18px;height:18px;background:#2b2b2c;border:1px solid #999"></span> | `#2b2b2c` | `43,43,44` |
| `--color_31` | <span style="display:inline-block;width:18px;height:18px;background:#eaded6;border:1px solid #999"></span> | `#eaded6` | `234,222,214` |
| `--color_32` | <span style="display:inline-block;width:18px;height:18px;background:#bbb2ab;border:1px solid #999"></span> | `#bbb2ab` | `187,178,171` |
| `--color_33` | <span style="display:inline-block;width:18px;height:18px;background:#8c8580;border:1px solid #999"></span> | `#8c8580` | `140,133,128` |
| `--color_34` | <span style="display:inline-block;width:18px;height:18px;background:#5e5956;border:1px solid #999"></span> | `#5e5956` | `94,89,86` |
| `--color_35` | <span style="display:inline-block;width:18px;height:18px;background:#2f2c2b;border:1px solid #999"></span> | `#2f2c2b` | `47,44,43` |
| `--color_36` | <span style="display:inline-block;width:18px;height:18px;background:#ceecea;border:1px solid #999"></span> | `#ceecea` | `206,236,234` |
| `--color_37` | <span style="display:inline-block;width:18px;height:18px;background:#293636;border:1px solid #999"></span> | `#293636` | `41,54,54` |
| `--color_38` | <span style="display:inline-block;width:18px;height:18px;background:#a2d9d6;border:1px solid #999"></span> | `#a2d9d6` | `162,217,214` |
| `--color_39` | <span style="display:inline-block;width:18px;height:18px;background:#7aa3a1;border:1px solid #999"></span> | `#7aa3a1` | `122,163,161` |
| `--color_40` | <span style="display:inline-block;width:18px;height:18px;background:#516d6b;border:1px solid #999"></span> | `#516d6b` | `81,109,107` |
| `--color_41` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_42` | <span style="display:inline-block;width:18px;height:18px;background:#4d5a59;border:1px solid #999"></span> | `#4d5a59` | `77,90,89` |
| `--color_43` | <span style="display:inline-block;width:18px;height:18px;background:#262d2d;border:1px solid #999"></span> | `#262d2d` | `38,45,45` |
| `--color_44` | <span style="display:inline-block;width:18px;height:18px;background:#c0e2df;border:1px solid #999"></span> | `#c0e2df` | `192,226,223` |
| `--color_45` | <span style="display:inline-block;width:18px;height:18px;background:#293636;border:1px solid #999"></span> | `#293636` | `41,54,54` |
| `--color_46` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_47` | <span style="display:inline-block;width:18px;height:18px;background:#516d6b;border:1px solid #999"></span> | `#516d6b` | `81,109,107` |
| `--color_48` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_49` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_50` | <span style="display:inline-block;width:18px;height:18px;background:#ceecea;border:1px solid #999"></span> | `#ceecea` | `206,236,234` |
| `--color_51` | <span style="display:inline-block;width:18px;height:18px;background:#ceecea;border:1px solid #999"></span> | `#ceecea` | `206,236,234` |
| `--color_52` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_53` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_54` | <span style="display:inline-block;width:18px;height:18px;background:#7aa3a1;border:1px solid #999"></span> | `#7aa3a1` | `122,163,161` |
| `--color_55` | <span style="display:inline-block;width:18px;height:18px;background:#7aa3a1;border:1px solid #999"></span> | `#7aa3a1` | `122,163,161` |
| `--color_56` | <span style="display:inline-block;width:18px;height:18px;background:#ceecea;border:1px solid #999"></span> | `#ceecea` | `206,236,234` |
| `--color_57` | <span style="display:inline-block;width:18px;height:18px;background:#ceecea;border:1px solid #999"></span> | `#ceecea` | `206,236,234` |
| `--color_58` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_59` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_60` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_61` | <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | `115,136,134` |
| `--color_62` | <span style="display:inline-block;width:18px;height:18px;background:#ceecea;border:1px solid #999"></span> | `#ceecea` | `206,236,234` |
| `--color_63` | <span style="display:inline-block;width:18px;height:18px;background:#ceecea;border:1px solid #999"></span> | `#ceecea` | `206,236,234` |
| `--color_64` | <span style="display:inline-block;width:18px;height:18px;background:#7aa3a1;border:1px solid #999"></span> | `#7aa3a1` | `122,163,161` |
| `--color_65` | <span style="display:inline-block;width:18px;height:18px;background:#7aa3a1;border:1px solid #999"></span> | `#7aa3a1` | `122,163,161` |

</details>

## Other brand-named CSS variables

| Variable | Value |
|---|---|
| `--backgroundColor` | `0,0,0` |
| `--bg` | `255,255,255` |
| `--bg-gradient` | `none` |
| `--bg-overlay-color` | `transparent` |
| `--bg-position` | `absolute` |
| `--bgDrop` | `var(--color_11)` |
| `--bgctr` | `255,255,255` |
| `--bgd` | `204,204,204` |
| `--bgf` | `transparent` |
| `--bgh` | `128,130,133` |
| `--text-direction` | `var(--wix-opt-in-direction)` |
| `--text-padding` | `0px` |
| `--text-spacing` | `12px` |
| `--textAlign` | `var(--input-text-align)` |
| `--textOutline` | `0px 0px transparent` |
| `--textPadding` | `var(--text-padding)` |
| `--textShadow` | `0px 0px transparent` |

## Likely brand colors (excluding Wix UI defaults)

Colors that appear in the CSS but are NOT in the Wix editor's default UI palette — these are the genuine brand choices.

| Swatch | Hex | Count | Likely role |
|---|---|---|---|
| <span style="display:inline-block;width:18px;height:18px;background:#00000000;border:1px solid #999"></span> | `#00000000` | 175 | near-black / text |
| <span style="display:inline-block;width:18px;height:18px;background:#00000099;border:1px solid #999"></span> | `#00000099` | 41 | near-black / text |
| <span style="display:inline-block;width:18px;height:18px;background:#ba8963;border:1px solid #999"></span> | `#ba8963` | 26 | warm / brown / tan |
| <span style="display:inline-block;width:18px;height:18px;background:#00000080;border:1px solid #999"></span> | `#00000080` | 24 | near-black / text |
| <span style="display:inline-block;width:18px;height:18px;background:#69382d;border:1px solid #999"></span> | `#69382d@0.30` | 16 | warm / brown / tan |
| <span style="display:inline-block;width:18px;height:18px;background:#5f6360;border:1px solid #999"></span> | `#5f6360` | 14 | green / sage |
| <span style="display:inline-block;width:18px;height:18px;background:#080808;border:1px solid #999"></span> | `#080808` | 14 | near-black / text |
| <span style="display:inline-block;width:18px;height:18px;background:#000000b3;border:1px solid #999"></span> | `#000000b3` | 12 | near-black / text |
| <span style="display:inline-block;width:18px;height:18px;background:#e1e1e100;border:1px solid #999"></span> | `#e1e1e100` | 12 | neutral / grey |
| <span style="display:inline-block;width:18px;height:18px;background:#e7e7e700;border:1px solid #999"></span> | `#e7e7e700` | 12 | neutral / grey |
| <span style="display:inline-block;width:18px;height:18px;background:#ffffffcc;border:1px solid #999"></span> | `#ffffffcc` | 12 | near-white / background |
| <span style="display:inline-block;width:18px;height:18px;background:#8f8f8f;border:1px solid #999"></span> | `#8f8f8f` | 12 | neutral / grey |
| <span style="display:inline-block;width:18px;height:18px;background:#808285;border:1px solid #999"></span> | `#808285` | 12 | blue (likely Wix default) |
| <span style="display:inline-block;width:18px;height:18px;background:#b0a986;border:1px solid #999"></span> | `#b0a986` | 12 | warm / brown / tan |
| <span style="display:inline-block;width:18px;height:18px;background:#5e5956;border:1px solid #999"></span> | `#5e5956` | 9 | neutral / grey |
| <span style="display:inline-block;width:18px;height:18px;background:#ceecea;border:1px solid #999"></span> | `#ceecea` | 8 | green / sage |
| <span style="display:inline-block;width:18px;height:18px;background:#738886;border:1px solid #999"></span> | `#738886` | 7 | green / sage |
| <span style="display:inline-block;width:18px;height:18px;background:#a2d9d6;border:1px solid #999"></span> | `#a2d9d6` | 5 | green / sage |
| <span style="display:inline-block;width:18px;height:18px;background:#9ab5b2;border:1px solid #999"></span> | `#9ab5b2` | 4 | green / sage |
| <span style="display:inline-block;width:18px;height:18px;background:#293636;border:1px solid #999"></span> | `#293636` | 3 |  |
| <span style="display:inline-block;width:18px;height:18px;background:#516d6b;border:1px solid #999"></span> | `#516d6b` | 2 | green / sage |
| <span style="display:inline-block;width:18px;height:18px;background:#f6ebe4;border:1px solid #999"></span> | `#f6ebe4` | 2 | near-white / background |
| <span style="display:inline-block;width:18px;height:18px;background:#69382d;border:1px solid #999"></span> | `#69382d` | 1 | warm / brown / tan |
| <span style="display:inline-block;width:18px;height:18px;background:#eaded6;border:1px solid #999"></span> | `#eaded6` | 1 |  |
| <span style="display:inline-block;width:18px;height:18px;background:#555759;border:1px solid #999"></span> | `#555759` | 1 | blue (likely Wix default) |

## Wix UI defaults present (informational — not brand)

| Swatch | Hex | Count |
|---|---|---|
| <span style="display:inline-block;width:18px;height:18px;background:#ffffff;border:1px solid #999"></span> | `#ffffff` | 205 |
| <span style="display:inline-block;width:18px;height:18px;background:#000000;border:1px solid #999"></span> | `#000000` | 154 |
| <span style="display:inline-block;width:18px;height:18px;background:#116dff;border:1px solid #999"></span> | `#116dff` | 98 |
| <span style="display:inline-block;width:18px;height:18px;background:#000000;border:1px solid #999"></span> | `#000000@0.70` | 16 |
| <span style="display:inline-block;width:18px;height:18px;background:#eeeeee;border:1px solid #999"></span> | `#eeeeee` | 14 |
| <span style="display:inline-block;width:18px;height:18px;background:#e0e0e0;border:1px solid #999"></span> | `#e0e0e0` | 14 |
| <span style="display:inline-block;width:18px;height:18px;background:#ff4040;border:1px solid #999"></span> | `#ff4040` | 14 |
| <span style="display:inline-block;width:18px;height:18px;background:#7fccf7;border:1px solid #999"></span> | `#7fccf7` | 14 |
| <span style="display:inline-block;width:18px;height:18px;background:#3899ec;border:1px solid #999"></span> | `#3899ec` | 14 |
| <span style="display:inline-block;width:18px;height:18px;background:#fafafa;border:1px solid #999"></span> | `#fafafa` | 14 |
| <span style="display:inline-block;width:18px;height:18px;background:#edf0f2;border:1px solid #999"></span> | `#edf0f2` | 12 |
| <span style="display:inline-block;width:18px;height:18px;background:#000000;border:1px solid #999"></span> | `#000000@0.60` | 11 |
| <span style="display:inline-block;width:18px;height:18px;background:#525252;border:1px solid #999"></span> | `#525252` | 10 |
| <span style="display:inline-block;width:18px;height:18px;background:#e2e2e2;border:1px solid #999"></span> | `#e2e2e2` | 6 |
| <span style="display:inline-block;width:18px;height:18px;background:#000000;border:1px solid #999"></span> | `#000000@0.50` | 4 |
| <span style="display:inline-block;width:18px;height:18px;background:#7a7a7a;border:1px solid #999"></span> | `#7a7a7a` | 4 |
| <span style="display:inline-block;width:18px;height:18px;background:#000000;border:1px solid #999"></span> | `#000000@0.00` | 3 |
| <span style="display:inline-block;width:18px;height:18px;background:#e0e0e0;border:1px solid #999"></span> | `#e0e0e0@0.00` | 2 |
| <span style="display:inline-block;width:18px;height:18px;background:#e8e8e8;border:1px solid #999"></span> | `#e8e8e8@0.00` | 2 |
| <span style="display:inline-block;width:18px;height:18px;background:#ffffff;border:1px solid #999"></span> | `#ffffff@0.80` | 2 |
| <span style="display:inline-block;width:18px;height:18px;background:#393939;border:1px solid #999"></span> | `#393939` | 1 |
| <span style="display:inline-block;width:18px;height:18px;background:#373b4d;border:1px solid #999"></span> | `#373b4d` | 1 |
| <span style="display:inline-block;width:18px;height:18px;background:#dbdbdb;border:1px solid #999"></span> | `#dbdbdb` | 1 |
| <span style="display:inline-block;width:18px;height:18px;background:#000000;border:1px solid #999"></span> | `#000000@0.40` | 1 |

## Type system (deduped)

### Real font families in use

| Family | Usage count |
|---|---|
| `playfair display` | 224 |
| `brandon-grot-w01-light` | 44 |
| `din-next-w01-light` | 42 |
| `mr de haviland` | 28 |
| `avenir-lt-w01_35-light1475496` | 27 |
| `raleway` | 26 |
| `montserrat` | 21 |
| `avenir-lt-w01_85-heavy1475544` | 13 |
| `futura-lt-w01-light` | 13 |
| `poppins-extralight` | 9 |
| `poppins` | 8 |
| `helvetica-w01-light` | 8 |
| `bree-w01-thin-oblique` | 6 |
| `futura-lt-w01-book` | 5 |

### Unique @font-face declarations

Each family/weight/style is listed once.

| Family | Weight | Style | Source file(s) |
|---|---|---|---|
| mr de haviland | 400 | normal | OpNVnooIhJj96FdB73296ksbOg3L60P3NilAZTs.woff2 |
| din-next-w01-light | 400 | normal | din-next-w10-light.woff2 |
| brandon-grot-w01-light | 400 | normal | brandon-grot-w05-light.woff2 |
| playfair display | 700 | italic | nuFnD-vYSZviVYUb_rj3ij__anPXDTngOWwu6zRmFqWF_ljR.woff2 |
| playfair display | 400 | italic | nuFkD-vYSZviVYUb_rj3ij__anPXDTnojUk7yRZrPJ-M.woff2 |
| playfair display | 400 | normal | nuFiD-vYSZviVYUb_rj3ij__anPXDTPYgEM86xRbPQ.woff2 |
| playfair display | 700 | normal | nuFlD-vYSZviVYUb_rj3ij__anPXBYf9lWEe5j5hNKe1_w.woff2 |
| wf_5dcf186d606c4852b16d7e15c |  |  | file.woff2, file.woff, file.ttf |
| wf_c7130737212b4e92a1d015799 |  |  | file.woff2, file.woff, file.ttf |
| poppins-extralight | 400 | normal | h3r77AwDsldr1E_2g4qqGPk_vArhqVIZ0nv9q090hN8.woff2 |
| poppins-extralight | 700 | italic | Fm41upUVp7KTKUZhL0PfQVtXRa8TVwTICgirnJhmVJw.woff2 |
| poppins-extralight | 700 | normal | rijG6I_IOXJjsH07UEo2mw.woff2 |
| poppins-extralight | 400 | italic | -GlaWpWcSgdVagNuOGuFKRUOjZSKWg4xBWp_C_qQx0o.woff2 |
| poppins | 700 | italic | pxiDyp8kv8JHgFVrJJLmy15VGdeOYktMqlap.woff2 |
| poppins | 400 | italic | pxiGyp8kv8JHgFVrJJLufntAOvWDSHFF.woff2 |
| poppins | 400 | normal | pxiEyp8kv8JHgFVrJJnecnFHGPezSQ.woff2 |
| poppins | 700 | normal | pxiByp8kv8JHgFVrLCz7Z1JlFd2JQEl8qw.woff2 |
| raleway | 700 | normal | 1Ptug8zYS_SKggPNyCIIT4ttDfCmxA.woff2 |
| raleway | 700 | italic | 1Ptsg8zYS_SKggPNyCg4QoFqL_KWxWMT.woff2 |
| raleway | 400 | normal | 1Ptug8zYS_SKggPNyCIIT4ttDfCmxA.woff2 |
| raleway | 400 | italic | 1Ptsg8zYS_SKggPNyCg4QoFqL_KWxWMT.woff2 |
| avenir-lt-w01_35-light1475496 | 400 | normal | avenir-lt-w05_35-light.woff2 |
| avenir-lt-w01_85-heavy1475544 | 400 | normal | avenir-lt-w05_85-heavy.woff2 |
| futura-lt-w01-light | 400 | normal | futura-lt-w05-light.woff2 |
| helvetica-w01-light | 400 | normal | helvetica-w02-light.woff2 |
| montserrat | 400 | normal | JTUSjIg1_i6t8kCHKm459WZhyyTh89ZNpQ.woff2 |
| montserrat | 400 | italic | JTUQjIg1_i6t8kCHKm459WxRxi7m0dR9pBOi.woff2 |
| montserrat | 700 | normal | JTURjIg1_i6t8kCHKm45_dJE3gbD_vx3rCubqg.woff2 |
| montserrat | 700 | italic | JTUPjIg1_i6t8kCHKm459WxZcgvz8_Zwjimrq1Q_.woff2 |
| futura-lt-w01-book | 400 | normal | futura-lt-w01-book.woff2 |
| bree-w01-thin-oblique | 400 | normal | bree-w05-thin-oblique.woff2 |

## Files

- `css/_combined.css` — every inline + linked stylesheet glued together for analysis
- `fonts/` — all downloaded font files
- `styles_manifest.json` — raw machine-readable manifest
- `PALETTE.md` — full unfiltered report
- `BRAND.md` — this refined report (use this for the redesign)