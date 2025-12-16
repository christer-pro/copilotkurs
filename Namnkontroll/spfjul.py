import pandas as pd
import os

spf_file = input("Ange filnamnet för SPF-filen (inkl. .xlsx): ").strip()
jul_file = input("Ange filnamnet för Jul-filen (inkl. .xlsx): ").strip()

spf_df = pd.read_excel(spf_file)
jul_df = pd.read_excel(jul_file)

# Normalisera kolumnnamn
spf_df.columns = spf_df.columns.str.strip().str.lower()
jul_df.columns = jul_df.columns.str.strip().str.lower()

print("Kolumner i SPF-filen:", spf_df.columns.tolist())
print("Kolumner i Jul-filen:", jul_df.columns.tolist())

# Skapa namnkolumn
spf_df["namn"] = spf_df["förnamn"].astype(str).str.strip() + " " + spf_df["efternamn"].astype(str).str.strip()
jul_df["namn"] = jul_df["förnamn"].astype(str).str.strip() + " " + jul_df["efternamn"].astype(str).str.strip()

# Jämför listorna
result_df = jul_df[~jul_df["namn"].isin(spf_df["namn"])]

# Spara resultatet i samma mapp som SPF-filen
output_dir = os.path.dirname(spf_file)
output_file = os.path.join(output_dir, "resultat.xlsx")

result_df.to_excel(output_file, index=False)

print(f"Resultatfilen sparades som: {output_file}")

