export interface PadStatus {
    pad_id: string;
    pad_size: number;
    offset_out: number;
    offset_in: number;
    remaining: number;
  }
  
  export interface EncryptedPacket {
    pad_id: string;
    offset: number;
    length: number;
    ciphertext: string;
  }