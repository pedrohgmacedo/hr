// console.log(__filename)
// console.log(__dirname)
// console.log(module)
// console.log(process)
// console.log(process.pid)
// console.log(process.versions)
// console.log(process.arch)
// console.log(process.argv)
// console.log(process.env)
// console.log(process.cwd())
// console.log(process.memoryUsage())

var events = require('events')
var emitter = new events.EventEmitter()

emitter.on('knock', function () {
    console.log('Who\'s there?')
})

emitter.on('knock', function () {
    console.log('Go away!')
})

emitter.emit('knock')
