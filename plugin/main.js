const postHTML = async () => {
  // ローカルホストにPOSTリクエストを送信
  const res = await fetch('http://localhost:8000/', {
    method: 'POST',
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({

      // 開いているページのHTMLを送信
      page: document.querySelector('html').innerHTML
    })
  });

  data = await res.text()
  return data;
}


// 毎回要約されると面倒なので、要約ボタンを作成
const button = createButton()
buddton.addEventListener('click', () => {
  postHTML().then(ret => console.log(ret));
})
document.body.appendChild(button);

function createButton() {
  const button = document.createElement('button')
  button.textContent = '要約'

  // 画面左下に固定
  button.style.position = 'fixed'
  button.style.bottom = '10px'
  button.style.left = '10px'

  // add style
  button.style.zIndex = '100000'
  button.style.bgcolor = 'white'
  button.style.padding = '4px'
  return button
}
