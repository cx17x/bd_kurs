// employee_table.js
async function fetchEmployees() {
    const response = await fetch('/api/employees/', { credentials: 'same-origin' });
    if (response.ok) {
        const employees = await response.json();
        displayEmployees(employees);
    } else {
        const error = await response.text();
        document.querySelector('tbody').innerHTML = `<tr><td colspan="4">${error}</td></tr>`;
    }
}

function displayEmployees(employees) {
    const tableBody = document.querySelector('#employeeTable tbody');
    if (employees.length === 0) {
        tableBody.innerHTML = `<tr><td colspan="4">No employees found.</td></tr>`;
        return;
    }
    employees.forEach(employee => {
        const row = tableBody.insertRow();
        row.insertCell(0).textContent = employee.id;
        row.insertCell(1).textContent = employee.name;
        row.insertCell(2).textContent = employee.position;
        row.insertCell(3).textContent = employee.department;
    });
}

fetchEmployees();