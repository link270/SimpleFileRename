import os, argparse

def setup_parser():
    parser = argparse.ArgumentParser(description ='Script to rename parts of files found in the sub directories.')
    parser.add_argument('--path', '-p', default='.', help ='Root path too look for files to change. Default is current path.')
    parser.add_argument('--original', '-o', default='', help ='The original word or part that needs to be changed.')
    parser.add_argument('--new', '-n', default='', help ='The new word or part to replace the old part with.')
    parser.add_argument('--manual', '-m', action='store_true', help ='Manually apprive name changes.')
    parser.add_argument('--auto', '-a', action='store_true', help ='Automatically change all files.')
    return parser.parse_args()



if __name__=="__main__":
    args = vars(setup_parser())
    o = args['original']
    n = args['new']
    if o == '' or n =='':
        print('please provide both -o and -n')
    else:
        i=0
        c=0
        for root, dirs, files in os.walk(args['path']):
            for file in files:
                if o in file:
                    i+=1
                    filePath = os.path.join(root, file)
                    newFilePath = filePath.replace(o, n)
                    if args['manual']:
                        inp = input(f"Replace: {filePath} \n   With: {newFilePath}\n? (y/n)\n")
                        if inp == 'y':
                            print('Replacing file.')
                            os.replace(filePath, newFilePath)
                            c+=1
                        elif inp == 'n':
                            print('Will not replace. Moving on.')
                        else:
                            print('Please enter a valid input.')
                    elif args['auto']:
                        print(f'Replacing {filePath} with {newFilePath}')
                        os.replace(filePath, newFilePath)
                        c+=1
                    else:
                        print(f'Replace: {filePath} \n   With: {newFilePath}\n')
        
        print(str(i)+ ' total file matches found.')
        print(str(c) + ' total files replaced.')
