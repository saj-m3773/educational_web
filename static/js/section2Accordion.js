
const accor = document.querySelectorAll('.accord')
const text = document.querySelectorAll('.body')
const next=document.querySelector(' .next-profile')
const prov=document.querySelector('.prev-profile')

accor.forEach(item => {
    item.addEventListener('click', function () {
        text.forEach(text => {
            text.classList.toggle('active')

            if (text.style.height) {
                text.style.height = null
                item.innerHTML = "معرفی"

            } else {
                text.style.height = text.scrollHeight + 'px';
                item.innerHTML = "بستن"

            }
            next.addEventListener('click',()=>{
                text.style.height = null
                item.innerHTML = "معرفی"

            })
            prov.addEventListener('click',()=>{
                text.style.height = null

            })

        })

    })
})