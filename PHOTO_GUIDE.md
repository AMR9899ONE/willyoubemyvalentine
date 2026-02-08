# 📸 How to Add Your Photos

## Quick Setup

### Step 1: Prepare Your Photos

1. Choose 5 special photos of you and your girlfriend
2. Rename them to:
   - `photo1.jpg`
   - `photo2.jpg`
   - `photo3.jpg`
   - `photo4.jpg`
   - `photo5.jpg`

3. **Pro tip:** Square photos work best! If your photos aren't square, they'll be cropped to fit the polaroid style.

### Step 2: Create an Images Folder

In your GitHub repository, create a folder called `images` and upload all 5 photos there.

**Via GitHub Website:**
1. In your repo, click "Add file" → "Create new file"
2. In the filename box, type `images/photo1.jpg` (this creates the folder)
3. Upload your photo
4. Repeat for all 5 photos

**Via Git Command Line:**
```bash
# Create images folder
mkdir images

# Copy your photos to the images folder
cp /path/to/your/photo1.jpg images/
cp /path/to/your/photo2.jpg images/
cp /path/to/your/photo3.jpg images/
cp /path/to/your/photo4.jpg images/
cp /path/to/your/photo5.jpg images/

# Add and commit
git add images/
git commit -m "Add our special photos 💕"
git push
```

### Step 3: Customize the Captions

Open `index.html` and find this section (around line 240):

```javascript
const polaroidPhotos = [
    { src: 'images/photo1.jpg', caption: 'Forever my favorite', rotation: -5 },
    { src: 'images/photo2.jpg', caption: 'Love you always', rotation: 3 },
    { src: 'images/photo3.jpg', caption: 'Our adventure', rotation: -3 },
    { src: 'images/photo4.jpg', caption: 'Best moments', rotation: 7 },
    { src: 'images/photo5.jpg', caption: 'You & Me', rotation: -7 }
];
```

Change the captions to match your photos! For example:
```javascript
const polaroidPhotos = [
    { src: 'images/photo1.jpg', caption: 'First date ❤️', rotation: -5 },
    { src: 'images/photo2.jpg', caption: 'Tokyo 2024', rotation: 3 },
    { src: 'images/photo3.jpg', caption: 'My favorite smile', rotation: -3 },
    { src: 'images/photo4.jpg', caption: 'Beach day 🌊', rotation: 7 },
    { src: 'images/photo5.jpg', caption: 'Forever together', rotation: -7 }
];
```

## 🎨 The Polaroid Effect

The photos will appear as:
- **Vintage polaroid prints** with white borders
- **Floating in the background** at slight angles
- **Gently bobbing** up and down
- **Enlarging on hover** so she can see them better
- **Semi-transparent** so they don't block the main content

## Want More or Fewer Photos?

### To Add More Photos (e.g., 8 photos):

1. Add more photo files: `photo6.jpg`, `photo7.jpg`, `photo8.jpg`

2. Update the JavaScript array:
```javascript
const polaroidPhotos = [
    { src: 'images/photo1.jpg', caption: 'Caption 1', rotation: -5 },
    { src: 'images/photo2.jpg', caption: 'Caption 2', rotation: 3 },
    { src: 'images/photo3.jpg', caption: 'Caption 3', rotation: -3 },
    { src: 'images/photo4.jpg', caption: 'Caption 4', rotation: 7 },
    { src: 'images/photo5.jpg', caption: 'Caption 5', rotation: -7 },
    { src: 'images/photo6.jpg', caption: 'Caption 6', rotation: 4 },
    { src: 'images/photo7.jpg', caption: 'Caption 7', rotation: -4 },
    { src: 'images/photo8.jpg', caption: 'Caption 8', rotation: 6 }
];
```

3. Add more positions to the positions array:
```javascript
const positions = [
    { top: '10%', left: '5%' },
    { top: '15%', right: '8%' },
    { bottom: '20%', left: '10%' },
    { top: '50%', right: '5%' },
    { bottom: '15%', right: '12%' },
    { top: '30%', left: '12%' },    // New position
    { bottom: '40%', right: '15%' }, // New position
    { top: '70%', left: '8%' }       // New position
];
```

### To Use Fewer Photos (e.g., 3 photos):

Just use fewer items in the array:
```javascript
const polaroidPhotos = [
    { src: 'images/photo1.jpg', caption: 'Caption 1', rotation: -5 },
    { src: 'images/photo2.jpg', caption: 'Caption 2', rotation: 3 },
    { src: 'images/photo3.jpg', caption: 'Caption 3', rotation: -3 }
];
```

## 🎵 About the Music

The page includes the **"My Neighbor Totoro" theme** by Joe Hisaishi that will try to autoplay when she opens the page.

**Note:** Most browsers block autoplay with sound, so she might need to click the play button (▶️) in the bottom right corner to start the music.

### Want Different Music?

You can change to other Ghibli soundtracks! Find the audio section in the HTML:

```html
<audio id="ghibliMusic" loop>
    <source src="YOUR_MUSIC_URL_HERE.mp3" type="audio/mpeg">
</audio>
```

**Popular Ghibli Music URLs:**
- My Neighbor Totoro: `https://cdn.jsdelivr.net/gh/napthedev/file-share@master/totoro.mp3`
- Spirited Away: Find on Archive.org or upload your own
- Howl's Moving Castle: Find on Archive.org or upload your own

**Or upload your own:**
1. Add an MP3 file to your repo (e.g., `music/ghibli_soundtrack.mp3`)
2. Change the source to: `src="music/ghibli_soundtrack.mp3"`

And update the track info:
```javascript
<div class="track-info">
    <div class="track-title">Merry-Go-Round of Life</div>
    <div>Howl's Moving Castle</div>
</div>
```

## 📱 Testing Locally

Before uploading to GitHub, you can test locally:

1. Put all files in a folder
2. Create an `images` subfolder with your photos
3. Open `index.html` in your web browser
4. Click the play button to start music
5. Check that photos appear and captions are correct

## 💡 Tips

- Use high-quality photos for the best look
- Square photos (1:1 ratio) work best
- Keep file sizes reasonable (under 1MB each) for fast loading
- The rotation values (-7 to 7) control the tilt angle - play with them!
- Photos fade in and hover to enlarge - very romantic effect! 💕

## ⚠️ Important Note

If you make the repo private, make sure GitHub Pages is enabled for private repos in your settings, or consider making it public so she can easily access it!

---

**Have fun adding your memories! This will make the page truly special and personal.** 🌸✨
