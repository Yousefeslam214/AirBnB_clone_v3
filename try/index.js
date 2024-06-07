
const express = require('express');
const app = express()
const port = 4080;

app.use(express.json())

app.listen(
    port,
    () => console.log(`it's alive on http://localhost:${port}`)
)
app.get(
    '/tshirt', (req, res) => {
        res.status(200).send({
            tshirt: 'yousef',
            size: 'large'
        })
    })

app.post('/tshirt/:id', (req, res) => {
    const { id } = req.params;
    const { logo } = req.body;
    if (!logo) {
        res.status(418).send({ message: 'We need a logo!' })
    }
    res.send({
        tshirt: ` tshirt with your ${logo} and ID of ${id}`,
    });
});
