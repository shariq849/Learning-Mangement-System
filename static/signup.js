let reset_btn = document.getElementById("reset");
let radio_btn = document.querySelectorAll('input[type="radio"]');
let radio_st = document.getElementById("student");
let radio_ins = document.getElementById("instructor");
const st_form = document.getElementById("stuForm");
const ins_form = document.getElementById("InsForm");
st_form.style.display = "none";
ins_form.style.display = "none";
reset_btn.addEventListener("click", () => {
    radio_btn.forEach(radio => {
        radio.checked = false;
    });

    st_form.style.display = "none";
    ins_form.style.display = "none";
})

radio_st.addEventListener("change", () => {
    if (radio_st.checked) {
        st_form.style.display = "block";
        ins_form.style.display = "none";
    }
})

radio_ins.addEventListener("change", () => {
    if (radio_ins.checked) {
        ins_form.style.display = "block";
        st_form.style.display = "none";

    }
})
