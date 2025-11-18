import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import pandas as pd
from datetime import datetime
import re

raw_lines = []

with open("next_games.txt", "r", encoding="utf-8") as f:
    raw_lines = f.readlines()

def parse_line(line, default_year=None):
    """Transforma uma linha de texto em dicionário com colunas.
       Robusto para campos como 'Home Over 1.5 goals: 100.0%'."""
    # split por vírgula tolerando espaços ao redor
    parts = [p.strip() for p in re.split(r"\s*,\s*", line.strip())]

    # garantir pelo menos 9 campos (preenche com "")
    while len(parts) < 9:
        parts.append("")

    date_str, match_str, avg_str, hO15, aO15, hU25, aU25, league, country = parts[:9]

    # parse date (append year if missing)
    year = default_year or datetime.now().year
    dt = pd.to_datetime(f"{date_str} {year}", format="%a %d %b %Y", errors='coerce')

    # parse match: "Home x Away"
    m = re.split(r"\s+x\s+|\s+X\s+|\s+vs\.?\s+", match_str)
    home = m[0].strip() if m and m[0] else ""
    away = m[1].strip() if len(m) > 1 else ""

    # helper to parse "Label: number" or percent
    def parse_number(field):
        if not field:
            return None
        s = field.strip()

        # 1) se tiver '%' -> pega o número antes do '%'
        m_pct = re.search(r"(-?\d+[.,]?\d*)\s*%$", s)
        if m_pct:
            val = m_pct.group(1).replace(',', '.')
            try:
                return float(val)
            except:
                return None

        # 2) se tiver '%' em alguma parte (ex: "100.0% , ..."), pega primeira ocorrência antes do %
        m_pct_any = re.search(r"(-?\d+[.,]?\d*)\s*%", s)
        if m_pct_any:
            val = m_pct_any.group(1).replace(',', '.')
            try:
                return float(val)
            except:
                return None

        # 3) caso não tenha '%' -> pega o ÚLTIMO número que aparecer na string
        all_nums = re.findall(r"(-?\d+[.,]?\d*)", s)
        if all_nums:
            val = all_nums[-1].replace(',', '.')
            try:
                return float(val)
            except:
                return None

        return None

    avg = parse_number(avg_str)
    home_ov15 = parse_number(hO15)
    away_ov15 = parse_number(aO15)
    home_ud25 = parse_number(hU25)
    away_ud25 = parse_number(aU25)

    return {
        "DateRaw": date_str,
        "Date": dt,
        "Home": home,
        "Away": away,
        "Match": match_str,
        "Average": avg,
        "HomeOv1.5": home_ov15,
        "AwayOv1.5": away_ov15,
        "HomeUd2.5": home_ud25,
        "AwayUd2.5": away_ud25,
        "League": league,
        "Country": country
    }

# ---------------------------
# Build DataFrame
# ---------------------------
def build_df(lines):
    rows = [parse_line(l) for l in lines]
    df = pd.DataFrame(rows)
    # keep Date as datetime if parsed; else try to coerce
    if df["Date"].isnull().any():
        year = datetime.now().year
    
        df["Date"] = df["DateRaw"].apply(lambda s: pd.to_datetime(f"{s} {year}", format="%a %d %b %Y", errors="coerce"))

        df["Date"] = df["Date"].dt.strftime("%d-%m-%Y")
    return df

# ---------------------------
# GUI (Tkinter)
# ---------------------------
class MatchesDashboard(tk.Tk):
    def __init__(self, df: pd.DataFrame):
        super().__init__()
        self.title("Matches Dashboard")
        self.geometry("1100x600")
        self.df_original = df.copy()
        self.df = df.copy()

        self.create_widgets()
        self.populate_filters()
        self.refresh_table(self.df)

    def create_widgets(self):
        frm_top = ttk.Frame(self, padding=8)
        frm_top.pack(side=tk.TOP, fill=tk.X)

        # Search entry (home/away)
        ttk.Label(frm_top, text="Pesquisar (time):").pack(side=tk.LEFT)
        self.search_var = tk.StringVar()
        ttk.Entry(frm_top, textvariable=self.search_var, width=20).pack(side=tk.LEFT, padx=6)

        # League combobox
        ttk.Label(frm_top, text="Liga:").pack(side=tk.LEFT, padx=(8,0))
        self.league_cb = ttk.Combobox(frm_top, state="readonly", width=18)
        self.league_cb.pack(side=tk.LEFT, padx=6)

        # Min Average
        ttk.Label(frm_top, text="Min Average:").pack(side=tk.LEFT, padx=(8,0))
        self.minavg_var = tk.DoubleVar(value=0.0)
        ttk.Spinbox(frm_top, from_=0.0, to=10.0, increment=0.1, textvariable=self.minavg_var, width=6).pack(side=tk.LEFT, padx=6)

        # Buttons
        ttk.Button(frm_top, text="Aplicar filtro", command=self.apply_filters).pack(side=tk.LEFT, padx=6)
        ttk.Button(frm_top, text="Limpar filtro", command=self.reset_filters).pack(side=tk.LEFT, padx=6)
        ttk.Button(frm_top, text="Exportar CSV", command=self.export_csv).pack(side=tk.LEFT, padx=6)

        # Table area
        columns = ["Date", "Home", "Away", "Average", "HomeOv1.5", "AwayOv1.5", "HomeUd2.5", "AwayUd2.5", "League", "Country"]
        self.columns = columns
        frm_table = ttk.Frame(self)
        frm_table.pack(fill=tk.BOTH, expand=True, padx=8, pady=8)

        self.tree = ttk.Treeview(frm_table, columns=columns, show="headings")
        vsb = ttk.Scrollbar(frm_table, orient="vertical", command=self.tree.yview)
        hsb = ttk.Scrollbar(frm_table, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
        self.tree.grid(row=0, column=0, sticky="nsew")
        vsb.grid(row=0, column=1, sticky="ns")
        hsb.grid(row=1, column=0, sticky="ew")
        frm_table.grid_rowconfigure(0, weight=1)
        frm_table.grid_columnconfigure(0, weight=1)

        # headings
        for col in columns:
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_by(c))
            self.tree.column(col, width=110, anchor="w")

        # bottom status
        self.status_var = tk.StringVar(value="")
        ttk.Label(self, textvariable=self.status_var, relief=tk.SUNKEN, anchor="w").pack(side=tk.BOTTOM, fill=tk.X)

    def populate_filters(self):
        leagues = sorted(self.df_original["League"].dropna().unique().tolist())
        countries = sorted(self.df_original["Country"].dropna().unique().tolist())
        self.league_cb['values'] = ["(Todos)"] + leagues
        self.league_cb.set("(Todos)")

    def refresh_table(self, df: pd.DataFrame):
        # clear
        for r in self.tree.get_children():
            self.tree.delete(r)
        # insert rows
        for _, row in df.iterrows():
            date_str = row["Date"].strftime("%d-%m-%Y") if pd.notnull(row["Date"]) else row["DateRaw"]
            vals = [ 
                date_str,
                row["Home"],
                row["Away"],
                "" if pd.isna(row["Average"]) else f"{row['Average']:.2f}",
                "" if pd.isna(row["HomeOv1.5"]) else f"{row['HomeOv1.5']:.2f}%",
                "" if pd.isna(row["AwayOv1.5"]) else f"{row['AwayOv1.5']:.2f}%",
                "" if pd.isna(row["HomeUd2.5"]) else f"{row['HomeUd2.5']:.2f}%",
                "" if pd.isna(row["AwayUd2.5"]) else f"{row['AwayUd2.5']:.2f}%",
                row["League"],
                row["Country"]
            ]
            self.tree.insert("", "end", values=vals)
        self.status_var.set(f"{len(df)} linhas exibidas")

    def apply_filters(self):
        df = self.df_original.copy()
        q = self.search_var.get().strip()
        if q:
            qlow = q.lower()
            df = df[df["Home"].str.lower().str.contains(qlow, na=False) | df["Away"].str.lower().str.contains(qlow, na=False)]

        sel_league = self.league_cb.get()
        if sel_league and sel_league != "(Todos)":
            df = df[df["League"] == sel_league]

        minavg = float(self.minavg_var.get() or 0.0)
        if minavg > 0:
            df = df[df["Average"].fillna(0) >= minavg]

        self.df = df
        self.refresh_table(self.df)

    def reset_filters(self):
        self.search_var.set("")
        self.league_cb.set("(Todos)")
        self.country_cb.set("(Todos)")
        self.minavg_var.set(0.0)
        self.df = self.df_original.copy()
        self.refresh_table(self.df)

    def export_csv(self):
        if self.df is None or self.df.empty:
            messagebox.showinfo("Exportar CSV", "Não há dados para exportar.")
            return
        path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files","*.csv")])
        if not path:
            return
        # export current filtered df
        self.df.to_csv(path, index=False)
        messagebox.showinfo("Exportar CSV", f"Exportado para {path}")

    def sort_by(self, col):
        # toggles ascending/descending
        ascending = getattr(self, "_sort_asc", {}).get(col, True)
        try:
            self.df = self.df.sort_values(by=col, ascending=ascending, na_position='last')
        except Exception:
            # fallback: sort by string repr
            self.df = self.df.sort_values(by=col, key=lambda s: s.astype(str), ascending=ascending)
        # store toggle
        if not hasattr(self, "_sort_asc"):
            self._sort_asc = {}
        self._sort_asc[col] = not ascending
        self.refresh_table(self.df)

# ---------------------------
# Main
# ---------------------------
def main():
    df = build_df(raw_lines)
    app = MatchesDashboard(df)
    app.mainloop()

if __name__ == "__main__":
    main()