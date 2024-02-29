# Gods
- https://github.com/cclgroupltd

## Xml
- https://github.com/martinblech/xmltodict/blob/master/xmltodict.py

# Zip

How to parse a zipped file with multiprocessing?
- https://stackoverflow.com/questions/73465509/how-to-parse-a-zipped-file-with-multiprocessing

Multithreaded File Unzipping in Python
- https://superfastpython.com/multithreaded-unzip-files/#How_to_Unzip_Files_Concurrently

# Sqlite

Having an SQLite database how to iterate thru all table items only knowing table name?
- https://stackoverflow.com/questions/56717346/having-an-sqlite-database-how-to-iterate-thru-all-table-items-only-knowing-table

# Json

- https://github.com/abrignoni/JSON-to-HTML-and-XLS

# Tips

## Comparing sqlite tables

- https://stackoverflow.com/questions/46867476/comparing-two-sqlite-databases-using-python

## Controll flow

```
def do_one():
  pass

def do_two():
  pass

def do_default():
  pass

actions = {1: do_one, 2: do_two}

actions = actions.get(x, do_default)
action(x)
```

## Html table sorting
```
function filterTable() {
  const query = q => document.querySelectorAll(q);
  const filters = [...query('th input')].map(e => new RegExp(e.value, 'i'));

  query('tbody tr').forEach(row => row.style.display = 
    filters.every((f, i) => f.test(row.cells[i].textContent)) ? '' : 'none');
}
<table>
  <thead>
    <tr>
      <th><input onkeyup="filterTable()" placeholder="Player... "></th>
      <th><input onkeyup="filterTable()" placeholder="Sport..."></th>
      <th><input onkeyup="filterTable()" placeholder="Team..."></th>
    </tr>
  </thead>
  <tbody>
    <tr><td> Michael Jordan </td><td> Basketball </td><td> Chicago Bulls         </td></tr>
    <tr><td> Kobe Bryant    </td><td> Basketball </td><td> LA Lakers             </td></tr>
    <tr><td> Brett Favre    </td><td> Football   </td><td> Greenbay Packers      </td></tr>
    <tr><td> Babe Ruth      </td><td> Baseball   </td><td> New York Yankees      </td></tr>
    <tr><td> Tom Brady      </td><td> Football   </td><td> New England Patriots  </td></tr>
    <tr><td> LeBron James   </td><td> Basketball </td><td> LA Lakers             </td></tr>
    <tr><td> Steph Curry    </td><td> Basketball </td><td> Golden State Warriors </td></tr>
    <tr><td> Jose Berrios   </td><td> Baseball   </td><td> Minnesota Twins       </td></tr>
    <tr><td> Kirby Pucket   </td><td> Baseball   </td><td> Minnesota Twins       </td></tr>
    <tr><td> Zach Parise    </td><td> Hockey     </td><td> Minnesota Wild        </td></tr>
    <tr><td> Jason Zucker   </td><td> Hockey     </td><td> Minnesota Wild        </td></tr>
  </tbody>
</table>
```
