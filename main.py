import emotes
import polars as pl

if __name__ == "__main__":
    emotes = emotes.get_all_emotes()
    # Save the emotes to a CSV file
    emotes_df = pl.DataFrame(
        {
            "id": map(lambda e: e["id"], emotes),
            "text": map(lambda e: e["text"], emotes),
            "vendor": map(lambda e: e["vendor"], emotes),
        }
    )
    emotes_df.write_csv("./test.csv")
