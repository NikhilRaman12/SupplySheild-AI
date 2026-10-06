def check_negative_inventory(df):
    return df[df['quantity_on_hand'] < 0]
