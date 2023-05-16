VMasker(document.getElementById("id_phone_number")).maskPattern("9999-9999")
var survey_form = document.getElementById("survey-form")
var button = document.getElementById("surveybtn")

htmx.on("loadError", (e) => {
    target = document.getElementById(e.detail.field_name)
    message_error_wrapper = document.getElementById(`${e.detail.field_name}_error_message`)
    if (e.detail.is_there_error) {
        target.classList.add("is-invalid")
        target.value = ""
        message_error_wrapper.innerHTML = e.detail.message_error
    } else {
        target.classList.remove("is-invalid")
        target.classList.add("is-valid")
        message_error_wrapper.innerHTML = ""
    }
})

htmx.on("htmx:beforeRequest", (e) => {
    if (e.srcElement.id === "survey-form") {
        button.disabled = true
    }
})

htmx.on("saveComplete", (e) => {
    if (e.detail.success) {
        survey_form.reset()
        button.disabled = !button.disabled;
        Swal.fire(
            'Good job!',
            'Thanks!',
            'success'
        )
        document.getElementsByTagName("input").forEach((element) => {
            element.classList.remove('is-invalid');
            element.classList.remove('is-valid');
        });
    }
})