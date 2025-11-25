"""
買い物メモアプリ（フロントエンド版）
====================================

Streamlit のセッション状態に依存せずに、クライアント側の JavaScript で
買い物リストを管理する簡易アプリです。入力欄に商品名を入力して
「追加」を押すとリストに表示され、「リストを全てクリア」を押すと
リストが即座に空になります。ブラウザ版でセッション状態がうまく
反映されない環境でも正しく動作します。
"""

import streamlit as st
import streamlit.components.v1 as components


def main() -> None:
    """Render the shopping memo app using HTML/JavaScript.

    This implementation avoids relying on Streamlit's session state. All state
    (the list of items) is handled in JavaScript on the client side. This
    ensures that pressing the clear button once immediately removes all items
    from the display, even in environments where `session_state` doesn't
    consistently update between reruns. The UI is rendered with basic HTML
    elements and styled inline for simplicity.
    """
    st.set_page_config(page_title="買い物メモアプリ", page_icon="🛒")
    st.title("買い物メモアプリ")
    st.write("欲しいものをメモしておくシンプルな買い物リストです。")

    # Define the HTML and JavaScript code for the shopping list. All state is
    # managed in the browser using the `items` array. When the user clicks the
    # buttons, the array is updated and the list is re-rendered.
    html_code = """
    <div style="margin-top:1rem;">
      <input id="itemInput" type="text" placeholder="アイテム名を入力" style="padding:0.5rem; width:60%;">
      <button onclick="addItem()" style="margin-left:0.5rem; padding:0.5rem;">追加</button>
      <button onclick="clearList()" style="margin-left:0.5rem; padding:0.5rem;">リストを全てクリア</button>
      <ul id="itemList" style="margin-top:1rem; list-style-type:none; padding:0;"></ul>
    </div>
    <script>
    // Maintain the list of items in this array. Because this script runs in
    // the browser, each client will have its own independent copy.
    let items = [];
    function addItem() {
      const inputEl = document.getElementById('itemInput');
      const value = inputEl.value.trim();
      if (value !== '') {
        items.push(value);
        inputEl.value = '';
        updateList();
      }
    }
    function clearList() {
      // Empty the items array and update the list display immediately.
      items = [];
      updateList();
    }
    function updateList() {
      const listEl = document.getElementById('itemList');
      // Clear current list contents
      listEl.innerHTML = '';
      // Render each item with its index (1-based)
      items.forEach((item, index) => {
        const li = document.createElement('li');
        li.style.marginBottom = '0.25rem';
        li.textContent = (index + 1) + '. ' + item;
        listEl.appendChild(li);
      });
    }
    </script>
    """

    # Render the HTML/JS in a Streamlit component. Height is adjusted to allow
    # enough space for the list to grow.
    components.html(html_code, height=300)


if __name__ == "__main__":
    main()
