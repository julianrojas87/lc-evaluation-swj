import os
import peartree as pt

root_folder = "/home/julian/Desktop/lc-evaluation/raw-data/"
entries = os.listdir(root_folder)

for pto in entries:
    print(f'Busiest day for {pto} public transport network')
    feed = pt.get_representative_feed(root_folder + pto)
    print("-------------------------------------------------")