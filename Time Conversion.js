function convertTimeToMilitary(s) {
    let times = s.split("")
    if (times[8] == "A") {
        if (times[0] == "1" && times[1] == "2") {
            times[0] = "0"
            times[1] = "0"
        }
    }

    if (times[8] == "P") {
        if (times[0] == "1" && times[1] == "2") {
            times[0] = "1"
            times[1] = "2"
        } else {
            times[0] = (parseInt(times[0]) + 1).toString()
            times[1] = (parseInt(times[1]) + 2).toString()
        }
    }
    return times.join("").slice(0, 8)
}

console.log(convertTimeToMilitary("12:05:45AM"))