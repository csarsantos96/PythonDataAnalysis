import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import re

df = pd.read_csv('ecommerce_estatistica.csv')
print(df.head().to_string())

col_map = {
    "item": "Título",
    "preco": "Preço",
    "quantidade": "Qtd_Vendidos",
    "nota": "Nota",
    "avaliacoes": "N_Avaliações",
    "desconto": "Desconto",
    "marca": "Marca",
    "categoria": "Gênero"
}

for key in ["preco","nota","avaliacoes","desconto"]:
    c = col_map[key]
    if c in df.columns:
        df[c] = pd.to_numeric(df[c], errors="coerce")

def parse_qtd(x):
    if pd.isna(x):
        return pd.NA
    s = str(x).lower().replace('+','').replace('.','').strip()
    if 'mil' in s:
        m = re.search(r'(\d+)', s)
        return float(m.group(1))*1000 if m else pd.NA
    m = re.search(r'\d+', s)
    return float(m.group(0)) if m else pd.NA

if col_map["quantidade"] in df.columns:
    df[col_map["quantidade"]] = df[col_map["quantidade"]].apply(parse_qtd)

if "Qtd_Vendidos_Cod" in df.columns and col_map["quantidade"] in df.columns:
    df[col_map["quantidade"]] = df[col_map["quantidade"]].fillna(
        pd.to_numeric(df["Qtd_Vendidos_Cod"], errors="coerce")
    )

if col_map["preco"] in df.columns:
    plt.hist(df[col_map["preco"]].dropna())
    plt.title("Histograma - Preços (simples)")
    plt.xlabel("Preço")
    plt.ylabel("Frequência")
    plt.savefig("hist_preco_simples.png", dpi=300, bbox_inches="tight")
    plt.show()

    plt.figure(figsize=(10,6))
    plt.hist(df[col_map["preco"]].dropna(), bins=50, color="green", alpha=0.8)
    plt.title("Histograma - Distribuição de Preços")
    plt.xlabel("Preço")
    plt.ylabel("Frequência")
    plt.grid(True)
    plt.savefig("hist_preco_detalhado.png", dpi=300, bbox_inches="tight")
    plt.show()

if all(c in df.columns for c in [col_map["preco"], col_map["quantidade"]]):
    plt.figure(figsize=(10,6))
    plt.scatter(df[col_map["preco"]], df[col_map["quantidade"]], alpha=0.6, s=30)
    plt.title("Dispersão - Preço x Quantidade")
    plt.xlabel("Preço")
    plt.ylabel("Quantidade")
    plt.savefig("disp_preco_quantidade.png", dpi=300, bbox_inches="tight")
    plt.show()

num_cols = [c for c in [col_map["preco"], col_map["quantidade"], col_map["nota"], col_map["desconto"]] if c in df.columns]
if len(num_cols) >= 2:
    corr = df[num_cols].corr()
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, annot=True, cmap="coolwarm")
    plt.title("Mapa de Calor - Correlação")
    plt.savefig("heatmap_correlacao.png", dpi=300, bbox_inches="tight")
    plt.show()

if all(c in df.columns for c in [col_map["item"], col_map["quantidade"]]):
    top_itens = (df.groupby(col_map["item"])[col_map["quantidade"]]
                   .sum()
                   .sort_values(ascending=False)
                   .head(10))
    labels_curto = [str(x)[:20] + ("…" if len(str(x)) > 20 else "") for x in top_itens.index]
    plt.figure(figsize=(12,6))
    plt.bar(range(len(top_itens)), top_itens.values)
    plt.xticks(range(len(top_itens)), labels_curto, rotation=30, ha='right')
    plt.title("Top 10 Itens mais vendidos")
    plt.xlabel("Item")
    plt.ylabel("Quantidade vendida")
    plt.tight_layout()
    plt.savefig("barras_top_itens.png", dpi=300, bbox_inches="tight")
    plt.show()

if all(c in df.columns for c in [col_map["categoria"], col_map["quantidade"]]):
    cat_share = (df.groupby(col_map["categoria"])[col_map["quantidade"]]
                   .sum()
                   .sort_values(ascending=False))

    total = cat_share.sum()
    cat_share_pct = (cat_share / total) * 100
    principais = cat_share_pct[cat_share_pct >= 3]
    outros = cat_share_pct[cat_share_pct < 3].sum()

    if outros > 0:
        principais["Outros"] = outros

    plt.figure(figsize=(8,8))
    wedges, texts, autotexts = plt.pie(
        principais.values,
        autopct="%1.1f%%",         # só percentual nas fatias
        startangle=90,
        textprops={'fontsize': 10}
    )

    plt.title("Participação de Vendas por Categoria")
    plt.legend(wedges, principais.index, title="Categorias",
               loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    plt.savefig("pizza_categorias.png", dpi=300, bbox_inches="tight")
    plt.show()

if col_map["preco"] in df.columns:
    plt.figure(figsize=(10,6))
    sns.kdeplot(df[col_map["preco"]].dropna(), fill=True)
    plt.title("Densidade - Preço")
    plt.xlabel("Preço")
    plt.ylabel("Densidade")
    plt.savefig("densidade_preco.png", dpi=300, bbox_inches="tight")
    plt.show()

if all(c in df.columns for c in [col_map["preco"], col_map["quantidade"]]):
    plt.figure(figsize=(10,6))
    sns.regplot(x=df[col_map["preco"]], y=df[col_map["quantidade"]], scatter_kws={'alpha':0.4, 's':25})
    plt.title("Regressão Linear - Preço x Quantidade")
    plt.xlabel("Preço")
    plt.ylabel("Quantidade")
    plt.savefig("regressao_preco_quantidade.png", dpi=300, bbox_inches="tight")
    plt.show()
