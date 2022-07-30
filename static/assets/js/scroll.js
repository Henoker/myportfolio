const blogContainers = [...document.querySelectorAll('.blog-container')];
const nxtBtn = [...document.querySelectorAll('.arrow-right')];
const preBtn = [...document.querySelectorAll('.arrow-left')];

blogContainers.forEach((item, i) => {
    let containerDimensions = item.getBoundingClientRect();
    let containerWidth = containerDimensions.width;

    nxtBtn[i].addEventListener('click', () => {
        item.scrollLeft += containerWidth;
    })

    preBtn[i].addEventListener('click', () => {
        item.scrollLeft -= containerWidth;
    })
})