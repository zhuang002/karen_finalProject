class GridEditor {
    constructor(titles, records) {
        this.titles = titles;
        this.root = document.createElement('div');
        var tab = document.createElement('table');
        this.root.appendChild(tab);
        var thead = document.createElement('thead');
        tab.appendChild(thead);
        var tbody = document.createElement('tbody');
        tab.appendChild(tbody);

        var tr = document.createElement('tr');
        thead.appendChild(tr);
        var td = document.createElement('td');
        tr.appendChild(td);
        for (var i=0;i<titles.length;i++) {
            td = document.createElement('td');
            tr.appendChild(td);
            td.innerText=titles[i].toUpperCase();
        }
        td = document.createElement('td');
        tr.appendChild(td);

        this.setRecords(records);
        var submit=document.createElement('button');
        submit.innerText = "SUBMIT";
        this.root.appendChild(submit);
        submit.addEventListener('click', (evt)=>{
            var records=this.collectRecords();
            var json = JSON.stringify(records);
            fetch('/test/update_materials',
                {
                    method: 'POST',
                    headers: {
                      'Accept': 'application/json',
                      'Content-Type': 'application/json'
                    },
                    body: json
                }
            ).then(response => response.json())
              .then(data => console.log(data))
              .catch(error=>console.log(error));
        });

    }

    getRoot() {
        return this.root;
    }

    setRecords(records) {
        this.records = records;
        var tbody = this.root.children[0].children[1];
        tbody.innerHTML="";
        var tr;
        var td;

        for (var i=0;i<records.length;i++) {
            tr = document.createElement('tr');
            tbody.appendChild(tr);
            var record = records[i];
            this.setRowRecord(tr,record);

        }

        tr = document.createElement('tr'); // this is the adding row
        tbody.appendChild(tr);
        td = document.createElement('td');
        tr.appendChild(td);
        for (var i=0;i<this.titles.length;i++) {
            td = document.createElement('td');
            tr.appendChild(td);
            var input = document.createElement('input');
            td.appendChild(input);
            input.type='text';
            input.name=this.titles[i];
        }
        td = document.createElement('td');
        tr.appendChild(td);
        var btn = document.createElement('button');
        btn.textContent = 'Add';
        td.appendChild(btn);
        btn.addEventListener('click', (evt) => {
            var tr = evt.currentTarget.parentElement.parentElement;
            var record = this.collectAddRecord(tr);
            var newTr = document.createElement('tr');
            var tbody = tr.parentElement;
            tbody.insertBefore(newTr, tr);
            this.setRowRecord(newTr, record);
            this.clearAddRow(tr);
        });
    }

    setRowRecord(tr, record) {
        var td = document.createElement('td');
        tr.appendChild(td);
        for (var j=0;j<this.titles.length;j++) {
            td = document.createElement('td');
            tr.appendChild(td);
            var a = document.createElement('a');
            td.appendChild(a);
            a.innerText = record[this.titles[j]];
            var input = document.createElement('input');
            td.appendChild(input);
            input.value = a.innerText;
            input.name = this.titles[j];
            input.style.display = 'none';
            if (input.name == 'code') {
                input.readOnly = true;
            }
        }
        td = document.createElement('td');
        tr.appendChild(td);
        td.innerHTML = "<button>Edit</button>&nbsp;&nbsp;<button>Delete</button>";
        var editBtn = td.children[0];
        editBtn.addEventListener('click', (evt)=>{
            var btn = evt.currentTarget;
            if (btn.textContent == 'Edit') {
                btn.textContent = 'Done';
            } else {
                btn.textContent = 'Edit';
            }
            var tr = evt.currentTarget.parentElement.parentElement;
            var tds = tr.children;
            for (var i=0;i<tds.length;i++) {
                var td = tds[i];
                if (td.children.length > 0) {
                    var a = td.children[0];
                    if (a.tagName.toLowerCase() == 'a') {
                        a.style.display = (btn.textContent=='Edit')?'':'none';

                        var input = td.children[1];
                        if (input.tagName.toLowerCase() == 'input') {
                            input.style.display = (btn.textContent=='Edit')?'none':'';
                        }

                        if (btn.textContent == 'Edit') {
                            a.innerText = input.value;
                        }
                    }

                }
            }
            evt.currentTarget.text = 'Done';
        });

        var delBtn = td.children[1];
        delBtn.addEventListener('click', (evt) => {
            tr.parentElement.removeChild(tr);
        })
    }

    collectRecords() {
        var records = [];
        var table = this.root.children[0];
        var tbody = table.tbodies[0];
        for (var i=0;i<tbody.children.length;i++) {
            var tr = tbody.children[i];
            var record = this.collectRecord(row);
            records.push(record);
        }
        return records;
    }

    collectRecord(row) {
        var record = {};
        var tds = addRow.children;

        for (var i=0;i<tds.length;i++) {
            var td = tds[i];
            if (td.children.length > 1) {
                var input = td.children[1];
                if (input.tagName.toLowerCase() == 'input') {
                    var a=td.children[0];
                    record[input.name] = a.value;
                }
            }
        };
        return record;
    }

    collectAddRecord(addRow) {
        var record = {};
        var tds = addRow.children;

        for (var i=0;i<tds.length;i++) {
            var td = tds[i];
            if (td.children.length > 0) {
                var input = td.children[0];
                if (input.tagName.toLowerCase() == 'input') {
                    record[input.name] = input.value;
                    input.value = '';
                }
            }
        };
        return record;
    }

    clearAddRow(tr) {
        for (var i=0;i<tr.children.length;i++) {
            var td = tr.children[i];
            if (td.children.length>0) {
                var input = td.children[0];
                if (input.tagName.toLowerCase()=='input') {
                    input.value = '';
                }
            }

        }
    }

    onEdit(evt) {

    }
}