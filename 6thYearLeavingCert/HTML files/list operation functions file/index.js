function calculateMean() {
    let dataFromInput = document.getElementById("userDataset_1").value;
    let dataInList = dataFromInput.split(",");

    let numItems = dataInList.length;
    let total = 0
    for (let item of dataInList){
        total += parseFloat(item);
    }
    let Mean = total / numItems
    return Mean
}
function calculateMedian() {
    let dataFromInput = document.getElementById("userDataset_1").value;
    let dataInList = dataFromInput.split(",");

    let numItems = dataInList.length;

    let soonToBeSortedArray = [];
    for (let item of dataInList){
        soonToBeSortedArray = soonToBeSortedArray.concat(parseFloat(item));
    }
    let sortedArray = [];
    let previousSmallestValue = -9999999999999999999999999999999999;
    let sorting = true
    while (sorting){
        smallestValue = 99999999999999999999999999;
        
        for (let item of soonToBeSortedArray){
            if (smallestValue >= item ) {
                smallestValue = item;
            }
        }
        soonToBeSortedArray.splice(soonToBeSortedArray.indexOf(smallestValue), 1)
        sortedArray = sortedArray.concat(smallestValue);
        if (soonToBeSortedArray.length === 0){
            sorting = false
        }
    }
    dataInList = sortedArray



    if (numItems%2 == 0) {
        let firstValue = parseFloat(dataInList[numItems/2]);
        let secondValue = parseFloat(dataInList[(numItems/2)-1]);
        let median = (firstValue + secondValue) / 2;
        return median
    } else if (numItems%2 == 1) {
        let median = dataInList[(numItems-1)/2];
        return median
    } 
}
function calculateMode() {
    let dataFromInput = document.getElementById("userDataset_1").value;
    let dataInList = dataFromInput.split(",");
    let soonToBeSortedArray = [];
    for (let item of dataInList){
        soonToBeSortedArray = soonToBeSortedArray.concat(parseFloat(item));
    }
    let sortedArray = [];
    let previousSmallestValue = -9999999999999999999999999999999999;
    let sorting = true
    while (sorting){
        smallestValue = 99999999999999999999999999;
        
        for (let item of soonToBeSortedArray){
            if (smallestValue >= item ) {
                smallestValue = item;
            }
        }
        soonToBeSortedArray.splice(soonToBeSortedArray.indexOf(smallestValue), 1)
        sortedArray = sortedArray.concat(smallestValue);
        if (soonToBeSortedArray.length === 0){
            sorting = false
        }
    }
    let numItems = dataInList.length;
    let modeList = [] 
    let value = sortedArray[0]

    modeList = modeList.concat([[value,1]])

    let found = false
    for  (let index1 = 1; index1 < numItems; index1++){
        found = false
        for  (let index2 = 0; index2 < modeList.length; index2++){
            if (modeList[index2][0] === sortedArray[index1]){
                modeList[index2][1] += 1
                
                found = true
            }
        }
        if (found === false) {
            modeList = modeList.concat([[sortedArray[index1],1]])
        }
    }
    let mode = 0
    let biggestValue = -99999999999999999999999;
    for (let item of modeList){
        if (biggestValue <= item[1] ) {
            biggestValue = item[1];
            mode = item[0]
        }
    }
    return mode
}

function calculateRange() {
    let dataFromInput = document.getElementById("userDataset_1").value;
    let dataInList = dataFromInput.split(",");

    let numItems = dataInList.length;
    biggestValue = -99999999999999999999999999;
    smallestValue = 99999999999999999999999999;
    for (let item of dataInList){
        if (biggestValue <= item ) {
            biggestValue = item;
        }
        if (smallestValue >= item ) {
            smallestValue = item;
        } 
    }
    return ([smallestValue," to ", biggestValue])
}

function calculateMeanBtn(){

    document.getElementById("meanPlaceholder").innerHTML = calculateMean();

}
function calculateMedianBtn(){

    document.getElementById("medianPlaceholder").innerHTML = calculateMedian();

}
function calculateModeBtn(){

    document.getElementById("modePlaceholder").innerHTML = calculateMode();

}
function calculateRangeBtn(){

    document.getElementById("rangePlaceholder").innerHTML = calculateRange();

}
