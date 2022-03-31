const express = require('express');
const PORT = 8888;
const app = express();

app.listen(PORT, () => {
    console.log('Example app listening at http://localhost:' + PORT);
});

app.use(express.urlencoded({
    extended: true
}));

app.use(express.json());

app.get('/get-users', function (req, res) {
    const numberOfUsers = 0;
    res.json({"activeUsers": numberOfUsers});
});

app.post('/create-user', function (req, res) {
    const body = req.body;
    const currentUser = {
        username: req.body.username,
        firstName: req.body.firstName,
        lastName: req.body.lastName,
    }
    if (body.username.length === 0 || body.username.trim().length === 0) {
        res.status(400);
        return res.send('Username cannot be empty.');
    }
    if (!body.firstName.match(/\d/) && !body.lastName.match(/\d/)) {
        console.log(`A new user was created: ${body.username}`);
        return res.send('User created: ' + body.username);
    } else {
        console.log("Name cannot contain numbers.")
        res.status(400);
        res.send('Name cannot contain numbers. Entered name: ' + body.firstName + " " + body.lastName);
    }
});
