import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc, Input, Output


# 1) Dados

df = pd.read_csv('ecommerce_estatistica.csv')

numeric_cols = [c for c in df.select_dtypes(include='number').columns if df[c].notna().any()]
categorical_cols = [c for c in df.select_dtypes(exclude='number').columns if df[c].notna().any()]

x_default = numeric_cols[0] if len(numeric_cols) > 0 else None
y_default = numeric_cols[1] if len(numeric_cols) > 1 else (numeric_cols[0] if len(numeric_cols) > 0 else None)
cat_default = categorical_cols[0] if len(categorical_cols) > 0 else None


# 2) App

app = Dash(__name__, title="Ecommerce Analytics")
server = app.server

def card(children, style=None):
    base = {
        "border": "1px solid #eaeaea",
        "borderRadius": "14px",
        "padding": "16px",
        "background": "white",
        "boxShadow": "0 4px 8px rgba(0,0,0,0.05)",
        "marginBottom": "16px"
    }
    if style: base.update(style)
    return html.Div(children, style=base)

app.layout = html.Div(
    style={"fontFamily":"system-ui,Segoe UI,Roboto,sans-serif","background":"#f7f7fb","padding":"18px"},
    children=[
        html.H1("Ecommerce Analytics", style={"marginBottom": 0}),
        html.P("Explore os dados interativamente."),

        card([
            html.H3("Controles"),
            html.Div(style={"display":"grid","gridTemplateColumns":"repeat(4,1fr)","gap":"12px"}, children=[
                html.Div([
                    html.Label("Coluna X (numérica)"),
                    dcc.Dropdown(id="x-col",
                        options=[{"label":c,"value":c} for c in numeric_cols],
                        value=x_default, placeholder="Selecione X")
                ]),
                html.Div([
                    html.Label("Coluna Y (numérica)"),
                    dcc.Dropdown(id="y-col",
                        options=[{"label":c,"value":c} for c in numeric_cols],
                        value=y_default, placeholder="Selecione Y")
                ]),
                html.Div([
                    html.Label("Coluna categórica"),
                    dcc.Dropdown(id="cat-col",
                        options=[{"label":c,"value":c} for c in categorical_cols],
                        value=cat_default, placeholder="Opcional")
                ]),
                html.Div([
                    html.Label("Filtrar valores da categoria"),
                    dcc.Dropdown(id="cat-values", options=[], value=[], multi=True,
                                 placeholder="Escolha valores (opcional)")
                ]),
            ]),
            html.Div(style={"display":"grid","gridTemplateColumns":"repeat(2,1fr)","gap":"12px","marginTop":"12px"}, children=[
                html.Div([
                    html.Label("Bins do Histograma"),
                    dcc.Slider(id="nbins", min=5, max=100, step=1, value=30,
                               marks={5:"5",30:"30",60:"60",100:"100"})
                ]),
                html.Div([
                    html.Label("Top-N da Barra"),
                    dcc.Slider(id="top-n", min=5, max=30, step=1, value=10,
                               marks={5:"5",10:"10",20:"20",30:"30"})
                ]),
            ])
        ]),

        card([html.H3("Histograma"), dcc.Graph(id="fig-hist")]),
        card([html.H3("Dispersão"), dcc.Graph(id="fig-scatter")]),
        card([html.H3("Correlação"), dcc.Graph(id="fig-corr")]),
        card([html.H3("Barras"), dcc.Graph(id="fig-bar")]),
        card([html.H3("Pizza"), dcc.Graph(id="fig-pie")]),
        card([html.H3("Densidade 2D"), dcc.Graph(id="fig-density")]),
    ]
)


# 3) Callbacks

@app.callback(
    Output("cat-values", "options"),
    Output("cat-values", "value"),
    Input("cat-col", "value")
)
def update_cat_values(cat_col):
    if cat_col and cat_col in df.columns:
        opts = [{"label": str(v), "value": v} for v in sorted(df[cat_col].dropna().unique())]
        return opts, []
    return [], []

def apply_cat_filter(local_df, cat_col, cat_values):
    if cat_col and cat_values:
        return local_df[local_df[cat_col].isin(cat_values)]
    return local_df

@app.callback(
    Output("fig-hist","figure"),
    Output("fig-scatter","figure"),
    Output("fig-corr","figure"),
    Output("fig-bar","figure"),
    Output("fig-pie","figure"),
    Output("fig-density","figure"),
    Input("x-col","value"),
    Input("y-col","value"),
    Input("cat-col","value"),
    Input("cat-values","value"),
    Input("nbins","value"),
    Input("top-n","value"),
)
def update_figs(x_col, y_col, cat_col, cat_values, nbins, topn):
    dfx = apply_cat_filter(df, cat_col, cat_values)

    fig_hist = px.histogram(dfx, x=x_col, nbins=nbins, color=cat_col) if x_col else px.histogram()
    fig_scatter = px.scatter(dfx, x=x_col, y=y_col, color=cat_col) if x_col and y_col else px.scatter()
    corr = dfx[numeric_cols].corr(numeric_only=True) if len(numeric_cols) >= 2 else None
    fig_corr = px.imshow(corr, text_auto=True, aspect="auto") if corr is not None else px.imshow([[0]])
    if cat_col:
        top_counts = dfx[cat_col].value_counts().head(topn).reset_index()
        top_counts.columns = [cat_col, "contagem"]
        fig_bar = px.bar(top_counts, x=cat_col, y="contagem")
        pie_df = dfx[cat_col].value_counts().reset_index()
        pie_df.columns = [cat_col, "contagem"]
        fig_pie = px.pie(pie_df, names=cat_col, values="contagem")
    else:
        fig_bar = px.bar()
        fig_pie = px.pie()
    fig_density = px.density_heatmap(dfx, x=x_col, y=y_col, nbinsx=30, nbinsy=30) if x_col and y_col else px.density_heatmap()

    return fig_hist, fig_scatter, fig_corr, fig_bar, fig_pie, fig_density

# 4) Run
if __name__ == "__main__":
    app.run(debug=True, port=8050)
