import subprocess
import os
import shutil
import zipfile

def create_layer():
    # Set up paths
    base_path = os.path.dirname(os.path.abspath(__file__))
    layer_path = os.path.join(base_path, 'python')
    requirements_path = os.path.join(base_path, 'requirements.txt')
    output_path = os.path.join(base_path, 'dependencies.zip')
    
    # Clean up previous builds
    if os.path.exists(layer_path):
        shutil.rmtree(layer_path)
    os.makedirs(layer_path)
    
    if os.path.exists(output_path):
        os.remove(output_path)
    
    # Install dependencies
    subprocess.check_call([
        'pip',
        'install',
        '-r', requirements_path,
        '-t', layer_path
    ])
    
    # Create zip file
    with zipfile.ZipFile(output_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, _, files in os.walk(layer_path):
            for file in files:
                full_path = os.path.join(root, file)
                archive_path = os.path.relpath(full_path, base_path)
                zf.write(full_path, archive_path)
    
    print(f"Layer package created at {output_path}")

if __name__ == '__main__':
    create_layer()