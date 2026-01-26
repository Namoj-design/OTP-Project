import { generatePad } from "./pad";

export async function captureEntropyAndGeneratePad() {
  // temporary static image until camera UI
  const imagePath = "data/sample_images/test.jpg";
  return generatePad(imagePath);
}