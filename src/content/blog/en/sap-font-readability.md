---
title: "Improving SAP readability with font settings (D2Coding and Pretendard)"
description: "How to fix SAP's default font readability with D2Coding and Pretendard — from download to applying them in SAP GUI, step by step."
pubDate: 2026-06-18
category: "operations"
series: "SAP, Explained Like a Restaurant"
level: "beginner"
tags: ["SAP-Operations", "SAP-GUI", "SAP-font", "SAP-settings"]
---

Hi, this is Rabbit! 🐰

Does your daily SAP screen feel somehow stuffy and hard to read — like wearing glasses with the wrong prescription? The cause is surprisingly simple: the **font**.

Today I'll cover how to dramatically improve SAP readability just by swapping fonts. It takes five minutes, and once you change it, going back is hard.

> **In 3 lines**
> - SAP's default font (Gulim) makes numbers and letters hard to tell apart, tiring the eyes.
> - Use D2Coding for fixed-width and Pretendard for proportional.
> - Install the fonts, set both in SAP GUI options, and you're done.

[[TOC]]

## Why start with the font

SAP GUI's default font is usually 'Gulim.' Honestly, its readability is dated, and it becomes a problem when working with data.

The number '0' and the letter 'O' get confused; the letter 'l' and the number '1' look like twins. These small differences pile up, tire your eyes, and sometimes lead to mistakes — like working through a foggy lens. No matter how good the features are, they're useless if you can't read clearly.

That's why font comes first when we talk about readability. You take off the old glasses and put on a new pair that fits.

## Two pairs of glasses: D2Coding and Pretendard

Depending on the use, I recommend two fonts — like coding glasses and everyday glasses.

**D2Coding — for fixed-width.** A free font Naver made for developers. Its biggest strength is clearly distinguishing similar-looking characters. It shines for fixed-width text like T-codes, numbers, and material codes. In SAP, set it as the 'fixed-width font.'

**Pretendard — for proportional.** A clean, widely used modern font, similar to Apple's system font. It makes variable-length text like material descriptions easy on the eyes. Set it as the 'proportional font' in SAP, and the once-rigid screen looks much tidier.

Splitting these two fonts by purpose makes SAP readability noticeably better.

## Install and apply (about 5 minutes)

### 1. Download the fonts

Get both first — both are free and available on official GitHub.

- D2Coding: [github.com/naver/d2codingfont](https://github.com/naver/d2codingfont)
- Pretendard: [github.com/orioncactus/pretendard](https://github.com/orioncactus/pretendard)

### 2. Install the fonts

Unzip and install. The two fonts install a bit differently.

**D2Coding** unzips to a single `.ttc` file. It bundles Regular and Bold together, so installing just that one applies both weights.

**Pretendard** unzips to a folder; go into `public → static` and you'll see multiple files. Select all with `Ctrl+A`, then in the right-click menu be sure to choose **'Install for all users.'**

> ⚠️ **Note**: For Pretendard, choose **'Install for all users,'** not just 'Install.' Miss this and the font may not appear in SAP.

### 3. Apply in SAP GUI

Now assign the new fonts in SAP.

1. Click the top-left icon in the SAP Logon window and go to **Options**.
2. Go to **Visual Design → Font Settings**.
3. Click **Select** to open the popup.
4. **Fixed-width font**: D2Coding, size 11 or 12
5. **Proportional font**: Pretendard, size 11 or 12
6. Click **Apply** and you're done.

![SAP font settings with D2Coding as fixed-width and Pretendard as proportional](/images/sap-font-readability-01_en.jpg)
*Figure 1. Fixed-width as D2Coding, proportional as Pretendard*

## Rabbit's Takeaway

"How much can one font really change?" you might think. But just making your daily screen comfortable cuts stress and reduces small mistakes too.

Using good tools well is part of a practitioner's skill. A five-minute investment to sharpen your screen makes every day of SAP work a little smoother. 😎

**Read more**

- [Why practitioners recommend the SAP Signature Theme](/en/blog/sap-signature-theme)
- [What is SAP? Understanding it through a restaurant kitchen](/en/blog/sap-what-is-sap)

<!-- 관련글: sap-signature-theme, sap-what-is-sap -->
