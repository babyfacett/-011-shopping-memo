import streamlit as st


def main() -> None:
    """Simple shopping memo app.

    Users can enter items they want to buy and maintain a list of items. The list
    is stored in Streamlit's session state so it persists across reruns. Users
    can add new items, remove selected items, and clear the entire list.
    """
    st.title("買い物メモアプリ")
    st.write("欲しいものをメモしておくシンプルな買い物リストです。")

    # Initialise the shopping list in session state
    if "shopping_list" not in st.session_state:
        st.session_state["shopping_list"] = []

    # Input for new item
    new_item = st.text_input("買い物リストに追加するアイテムを入力してください")
    add_button = st.button("追加", key="add_item")

    # When the add button is pressed, append item if not empty
    if add_button and new_item.strip():
        st.session_state["shopping_list"].append(new_item.strip())
        st.success(f"'{new_item}' を追加しました。")

    # Show the current list and options to remove items
    if st.session_state["shopping_list"]:
        st.subheader("現在の買い物リスト")
        # Use a multiselect widget to choose items to remove
        items_to_remove = st.multiselect(
            "削除したいアイテムを選択してください",
            options=st.session_state["shopping_list"],
            key="remove_select",
        )
        if st.button("選択したアイテムを削除", key="remove_button"):
            st.session_state["shopping_list"] = [
                item for item in st.session_state["shopping_list"] if item not in items_to_remove
            ]
            st.success("選択したアイテムを削除しました。")

        st.write("### リスト内容")
        for idx, item in enumerate(st.session_state["shopping_list"], start=1):
            st.write(f"{idx}. {item}")

        # Option to clear the list
        if st.button("リストを全てクリア", key="clear_list"):
            st.session_state["shopping_list"] = []
            st.success("リストを空にしました。")
    else:
        st.info("現在、リストには何もありません。上の入力欄から追加してください。")


if __name__ == "__main__":
    main()