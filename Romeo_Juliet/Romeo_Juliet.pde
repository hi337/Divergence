PImage romeoImg, julietImg, backgroundImg;
boolean romeoDragging = false;
boolean julietDragging = false;
int romeoX, romeoY, julietX, julietY;
int romeoOffsetX, romeoOffsetY, julietOffsetX, julietOffsetY;
int dialogueBoxX, dialogueBoxY;
int dialogueBoxWidth = 1000;
int dialogueBoxHeight = 150;
int buttonWidth = 60;
int buttonHeight = 30;

String romeoDialogue = "Romeo's quote for the Act ";
String julietDialogue = "Juliet's quote for the Act ";

String[] romeoQuotes = {
  "Here's much to do with hate, but more with love",
  "It is the east and Juliet is the sun",
  "I do protest I never injured thee, But love thee better than thou canst devise, Till \n thou shalt know the reason of my love. And so, good Capulet—which name \n I tender As dearly as my own—be satisfied.",
  "Then I defy you, stars!",
  "O, here will I set up my everlasting rest, And shake the yoke of inauspicious stars \n From this world-wearied flesh."
};

String[] julietQuotes = {
  "Go ask his name. - If he be marrièd, My grave is like to be my wedding bed",
  "And i'll no longer be a Capulet",
  "Come, gentle night, come, loving, black-browed night, Give me my Romeo. And when I shall \ndie, Take him and cut him out in little stars, And he will make the face \n of heaven so fine That all the world will be in love with night And pay no worship to the garish sun.",
  "Where I have learnt to repent the sin Of disobedient opposition To you and your behests, \nand am enjoined By holy Laurence to fall prostrate here To beg your pardon. \n Pardon. I beseech you!",
  "O comfortable friar! where is my lord? I do remember well where I should be: And there I am.\n Where is my Romeo?"
};

boolean displayRomeoDialogue = false;
boolean displayJulietDialogue = false;
String currentDialogue = "";

// Positions for boxes for each act
int[] actBoxesX = {50, 50, 50, 50, 50}; // X positions for act boxes
int actBoxY = 20; // Y position for all act boxes
int actBoxWidth = 180; // Width for each act box
int actBoxHeight = 120; // Height for each act box

void setup() {
  size(1000, 800);
  romeoImg = loadImage("romeo.png");
  julietImg = loadImage("juliet.png");
  backgroundImg = loadImage("bruhbackground.jpeg");
  
  romeoImg.resize(100, 0);
  julietImg.resize(100, 0);
  
  // Initial positions for Romeo and Juliet
  romeoX = width / 4;
  romeoY = height / 12;
  julietX = width * 3 / 4;
  julietY = height / 12;
  
  // Position dialogue box
  dialogueBoxX = width / 2 - dialogueBoxWidth / 2;
  dialogueBoxY = height - dialogueBoxHeight - 20;
  
  // Set text size and alignment
  textSize(18);
  textAlign(CENTER);
}

void draw() {
  // Draw the background image first
  image(backgroundImg, 0, 0, width, height);
  
  // Display act boxes
  for (int i = 0; i < 5; i++) {
    fill(#c4fffb); // White boxes
    rect(actBoxesX[i], actBoxY + i * actBoxHeight, actBoxWidth, actBoxHeight);
    fill(0); // Black text
    text("Act " + (i + 1), actBoxesX[i] + actBoxWidth / 2, actBoxY + i * actBoxHeight + actBoxHeight / 2);
  }
  
  // Display Romeo
  image(romeoImg, romeoX, romeoY);
  
  // Display Juliet
  image(julietImg, julietX, julietY);
  
  // Display dialogue box if needed
  if (displayRomeoDialogue || displayJulietDialogue) {
    fill(173, 216, 230); // Light blue color
    rect(dialogueBoxX, dialogueBoxY, dialogueBoxWidth, dialogueBoxHeight);
    fill(0);
    text(currentDialogue, dialogueBoxX + dialogueBoxWidth / 2, dialogueBoxY + 30);
    
    // OKAY button
    fill(200);
    rect(dialogueBoxX + dialogueBoxWidth / 2 - buttonWidth / 2, dialogueBoxY + dialogueBoxHeight - 40, buttonWidth, buttonHeight, 5);
    fill(0);
    text("OKAY", dialogueBoxX + dialogueBoxWidth / 2, dialogueBoxY + dialogueBoxHeight - 20);
  }
}

void mousePressed() {
  if (mouseX > romeoX && mouseX < romeoX + romeoImg.width &&
      mouseY > romeoY && mouseY < romeoY + romeoImg.height) {
    romeoDragging = true;
    romeoOffsetX = mouseX - romeoX;
    romeoOffsetY = mouseY - romeoY;
    displayRomeoDialogue = true;
    int actIndex = (romeoY - actBoxY) / actBoxHeight; // Corrected line
    if (actIndex >= 0 && actIndex < 5) {
      currentDialogue = romeoDialogue + (actIndex + 1) + ": " + romeoQuotes[actIndex];
    }
  }
  
  if (mouseX > julietX && mouseX < julietX + julietImg.width &&
      mouseY > julietY && mouseY < julietY + julietImg.height) {
    julietDragging = true;
    julietOffsetX = mouseX - julietX;
    julietOffsetY = mouseY - julietY;
    displayJulietDialogue = true;
    int actIndex = (julietY - actBoxY) / actBoxHeight;
    if (actIndex >= 0 && actIndex < 5) {
      currentDialogue = julietDialogue + (actIndex + 1) + ": " + julietQuotes[actIndex];
    }
  }
}


void mouseDragged() {
  if (romeoDragging) {
    romeoX = mouseX - romeoOffsetX;
    romeoY = mouseY - romeoOffsetY;
  }
  
  if (julietDragging) {
    julietX = mouseX - julietOffsetX;
    julietY = mouseY - julietOffsetY;
  }
}

void mouseReleased() {
  romeoDragging = false;
  julietDragging = false;
}
