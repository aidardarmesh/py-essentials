import argparse, json, os, tempfile

def write(path, data):
    with open(path, 'w+') as f:
        f.write(data)

def read(path):
    with open(path, 'r+') as f:
        return f.read()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')

if not os.path.exists(storage_path):
    write(storage_path, json.dumps({}))

data = json.loads(read(storage_path))

parser = argparse.ArgumentParser()
parser.add_argument("--key")
parser.add_argument("--value")
args = parser.parse_args()

if args.key and args.value:
    value = data.get(args.key, [])
    value.append(args.value)
    data[args.key] = value
elif args.key:
    if args.key in data:
        print(", ".join(data[args.key]))
    else:
        print()

write(storage_path, json.dumps(data))