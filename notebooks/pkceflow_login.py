import marimo

__generated_with = "0.13.10"
app = marimo.App(width="medium")


@app.cell
def _():
    from moutils.oauth import PKCEFlow

    df = PKCEFlow(
        provider="github",
        client_id="Iv23lizZAx1IpMzYpu7C",
        redirect_uri="http://localhost:2718/",
        debug=True,
    )

    df
    return (df,)


@app.cell
def _(df, mo):
    # Display the access token when authentication is successful
    if df.access_token:
        mo.md("## Access Token")
        mo.md(f"```\n{df.access_token}\n```")
    return


if __name__ == "__main__":
    app.run()
