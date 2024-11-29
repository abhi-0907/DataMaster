var pref = document.getElementById('preferences');
pref.innerHTML = '<h5>Your Preferences</h5><h6><strong>Course:</strong> ' + course + '</h6><h6><strong>Country:</strong> ' + country + '</h6><h6><strong>Maximum Fees (Year):</strong> ' + max_fees + '</h6>';


function populateTable() {

  var thead = document.getElementById('data-table-header');
  thead.innerHTML = "<tr><th>University Name</th><th>State</th><th>Country</th><th>Course Name</th><th>Average Fees in INR</th></tr>";

  var tbody = document.getElementById('data-table-body');
  tbody.innerHTML = "";

  tableData.forEach(function (row) {
    var tr = document.createElement('tr');
    tr.innerHTML = '<td>' + row["university_name"] + '</td>' +
      '<td>' + row["state"] + '</td>' +
      '<td>' + row["country"] + '</td>' +
      '<td>' + row["course_name"] + '</td>' +
      '<td>' + row["average_fees_in_inr"] + '</td>';

    tr.classList.add("table-row")
    tbody.appendChild(tr);
  });
}

window.onload = populateTable;

