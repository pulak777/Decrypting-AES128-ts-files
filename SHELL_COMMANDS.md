## **STEP 1**

Generate 32bit HEX KEY from 128bit encryption key file (link in the <file_name>.txt file)

`xxd -p <128bit key file name>.key`

you are expected to get a 32bit output like this - **bf8a8a87d912c8aafa73c4454e14fdda**

**Example**

`xxd -p eyJpdiI6InJkUmxORnFIWUVcL0NlSWZMMjBISWlnPT0iLCJ2YWx1ZSI6InFMWll2R2JkNEJ0VHRWSWszR3ZYdGc9PSIsIm1hYyI6IjU0YzliZWJmZDVmMWViYTZiZGUxYjAyNWY1YzE1NzVhN2FjOTNlN2RjMTNkYzM1YWIzYTU5MzM1NjdiODZhZWQifQ==.key`

(key file must be downloaded before running this command)

---

## **STEP 2**

Decrypt the downloaded encrypted ts file

`openssl aes-128-cbc -d -in <file_name>.ts -out <d_file_name>.ts -nosalt -iv <32bit HEX> -K <32bit KEY HEX>`

**Example**

`openssl aes-128-cbc -d -in dynamic_programming.ts -out d_dynamic_programming.ts -nosalt -iv 65e54cc65777504b227afe3964856508 -K bf8a8a87d912c8aafa73c4454e14fdda`

---

## **STEP 3**

Convert ts file to mp4 file format (optional, but reduces file size by almost 33%)

`ffmpeg -i d_file_name.ts file_name.mp4`

Example

`ffmpeg -i d_dynamic_programming.ts dynamic_programming.mp4`

### STEP 4 (Optional but recommanded)

Delete the unnecesary files (delete decrypted ts file only if already converted to mp4 or mkv etc. else you may loose your data)

`rm d_dynamic_programming.ts dynamic_programming.ts dynamic_programming.txt`

However, if you are downloading sequencial files from the same website, they may use the same encryption credential for every file (i.e. IV and KEY). So you **don't need to repeat STEP1** multiple times to obtain the **KEY HEX value**.
