# Use:
#  python convert_bdmv.py \
#   --bdmv "Ruta/a/BDMV" \
#   --output "Ruta/donde/guardar/nombre_archivo.mkv"

import os
import subprocess
import argparse
import shutil
import sys

def check_dependencies():
    if not shutil.which("mkvmerge"):
        print("❌ mkvmerge no está instalado o no está en el PATH.")
        print("ℹ️ Instálalo con apt, brew o desde https://mkvtoolnix.download/")
        sys.exit(1)

def find_largest_m2ts(stream_folder):
    m2ts_files = [f for f in os.listdir(stream_folder) if f.endswith('.m2ts')]
    if not m2ts_files:
        raise Exception("No se encontraron archivos .m2ts en la carpeta STREAM.")
    
    largest_file = max(
        m2ts_files,
        key=lambda f: os.path.getsize(os.path.join(stream_folder, f))
    )
    return os.path.join(stream_folder, largest_file)

def convert_to_mkv(input_m2ts, output_mkv):
    os.makedirs(os.path.dirname(output_mkv), exist_ok=True)
    cmd = [
        "mkvmerge",
        "-o", output_mkv,
        input_m2ts
    ]
    subprocess.run(cmd, check=True)
    print(f"✅ Conversión completada: {output_mkv}")

def main():
    parser = argparse.ArgumentParser(description="Convertir Blu-ray BDMV a archivo MKV.")
    parser.add_argument('--bdmv', required=True, help='Ruta a la carpeta BDMV')
    parser.add_argument('--output', required=True, help='Ruta completa al archivo de salida (ej. /ruta/pelicula.mkv)')

    args = parser.parse_args()

    check_dependencies()

    bdmv_path = args.bdmv
    output_file = args.output
    stream_path = os.path.join(bdmv_path, "STREAM")

    print("🔍 Buscando el archivo de video principal...")
    main_video = find_largest_m2ts(stream_path)

    print(f"🎬 Archivo seleccionado: {main_video}")
    print(f"🎞️ Iniciando la conversión a {output_file} ...")
    convert_to_mkv(main_video, output_file)

if __name__ == "__main__":
    main()
