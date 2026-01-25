import { generatePad } from "./pad";

export async function captureEntropyAndGeneratePad() {
  // For now: fixed image path (real camera later)
  return generatePad("data/sample_images/test.jpg");
}