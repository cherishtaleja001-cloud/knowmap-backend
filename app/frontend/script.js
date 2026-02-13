const API = "http://127.0.0.1:8000";

async function register() {
    const res = await fetch(`${API}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username: reg_username.value,
            email: reg_email.value,
            password: reg_password.value
        })
    });
    alert("Registered!");
}

async function login() {
    const res = await fetch(`${API}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            email: login_email.value,
            password: login_password.value
        })
    });
    alert("Login Successful!");
}

async function createDataset() {
    const res = await fetch(`${API}/datasets/?user_id=${dataset_user_id.value}`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            name: dataset_name.value,
            description: dataset_desc.value
        })
    });
    alert("Dataset Created!");
}
