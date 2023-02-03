function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');



async function makeRequest(url, method ) {
    let response = await fetch(url, method);
    if (response.ok) {
        return await response.json();
    } else {
        let error = new Error(response.statusText);
        error.response = response;
        throw error;    }
}



async function ButtonClick(event) {
    let target = event.target;
    let url = target.dataset.indexLink;
    let id = target.dataset.operation;
    let a = document.getElementById('A').value;
    let b = document.getElementById('B').value;
    let data = {
        A : a,
        B : b
    }
    let r = JSON.stringify(data)
    let response = await makeRequest(url, {
        method: "POST",
        headers: {
            'X-CSRFToken': csrftoken,
            'Content-Type': 'application/json'
        },
        body : r});
    let t = document.getElementById('answer')
    if (response.ans.answer) {
        t.innerHTML = `Answer:${response.ans.answer}`;
        t.style.color = "green";
    } else {
        t.innerHTML = `${response.ans.errors}`;
        t.style.color = 'red'

    }
    return response



}

