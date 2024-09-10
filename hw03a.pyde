"""
9103 hw1-2
alison yang
original link: https://github.com/DM-GY-6063-2023F-D/HW03A
original code:
    let diamSmall = 10;
let diamLarge = 3 * diamSmall;

function setup() {
  createCanvas(windowWidth, windowHeight);
}

function draw() {
  background("gold");
  stroke(0);

  fill(0);
  for (let x = 0; x < width; x += 5 * diamSmall) {
    for (let y = 0; y < height; y += 5 * diamSmall) {
      ellipse(x, y, diamSmall, diamSmall);
    }
  }

  for (let x = 0; x < width; x += 2 * 5 * diamSmall) {
    for (let y = 0; y < height; y += 2 * 5 * diamSmall) {
      ellipse(x, y, diamLarge, diamLarge);
    }
  }

  translate(5 * diamSmall, 5 * diamSmall);
  for (let x = 0; x < width; x += 2 * 5 * diamSmall) {
    for (let y = 0; y < height; y += 2 * 5 * diamSmall) {
      ellipse(x, y, diamLarge, diamLarge);
    }
  }
}
"""

diamSmall = 10
diamLarge = 3 * diamSmall

def setup():
    # windowWidth & windowHeight return a local error with absolute path, so i manually input a canvas size
    size(800, 800)
    
def draw():
    background(255,215,0)
    stroke(0)
    fill(0)
    
    for x in range(0, width, 5 * diamSmall):
        for y in range(0, height, 5 * diamSmall):
            ellipse(x, y, diamSmall, diamSmall)
            
    for x in range(0, width, 2 * 5 * diamSmall):
        for y in range(0, height, 2 * 5 * diamSmall):
            ellipse(x, y, diamLarge, diamLarge)
    
    translate(5 * diamSmall, 5 * diamSmall)
    for x in range(0, width, 2 * 5 * diamSmall):
        for y in range(0, height, 2 * 5 * diamSmall):
            ellipse(x, y, diamLarge, diamLarge)
