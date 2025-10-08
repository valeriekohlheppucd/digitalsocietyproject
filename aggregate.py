import pandas as pd
import plotly.express as px

# Load responses (export your Google Sheet as CSV)
df = pd.read_csv("responses.csv")

# Reshape data for ternary plot
present_df = df.rename(columns={
    "Present Equality": "Equality",
    "Present Security": "Security",
    "Present Efficiency": "Efficiency"
})
present_df["Time"] = "Present"

future_df = df.rename(columns={
    "Future Equality": "Equality",
    "Future Security": "Security",
    "Future Efficiency": "Efficiency"
})
future_df["Time"] = "2075"

combined = pd.concat([present_df, future_df], ignore_index=True)

# Plot
fig = px.scatter_ternary(
    combined,
    a="Equality", b="Security", c="Efficiency",
    color="Time",
    symbol="Time",
    title="Aggregated Values: Present vs 2075"
)

# Save outputs
fig.write_html("aggregated_plot.html")
fig.write_image("aggregated_plot.png")

print("✅ Aggregated plot saved as HTML and PNG")
