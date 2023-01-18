// External JavaScript example
function createParagraph() {
    let head_ext = document.querySelector('#external-js-heading')
    let p = document.createElement('p');
    p.innerHTML = 'You clicked the button!';
    head_ext.append(p);
}

// Event listener example
document.querySelector("#btn-listener").addEventListener("click", displayDate);

function displayDate() {
    document.querySelector("#demo").innerHTML = Date();
}