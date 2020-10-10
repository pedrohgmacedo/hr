// The days of the week are: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"
function getDayName(dateString) {
    let dayName
    // Write your code here
    let weekdays = {
        "Sun": "Sunday",
        "Mon": "Monday",
        "Tue": "Tuesday",
        "Wed": "Wednesday",
        "Thu": "Thursday",
        "Fri": "Friday",
        "Sat": "Saturday",
    }
    let currentDay = new Date(dateString).toDateString().split(" ")[0]
    dayName = weekdays[currentDay]
    return dayName
}

let input = "10/11/2009"
console.log(getDayName(input))
// console.log(getDayName(new Date(inp).toDateString()))

// creating a date instance:
// Using new Date()
// Using new Date(value)
// Using new Date(dateString)
// Using new Date(year, month, day, hour, minutes, seconds, milliseconds)

// date has some get methods