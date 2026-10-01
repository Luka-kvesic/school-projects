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
    dataInList.sort(function(a,b){return a-b});



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
    dataInList.sort(function(a,b){return a-b});
    let numItems = dataInList.length;
    let modeList = [] 
    sortedArray = dataInList
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
    dataInList.sort(function(a,b){return a-b});
    return ([dataInList[0]," to ", dataInList[dataInList.length -1]])
}

function calculateFrequency(){
    let dataFromInput = document.getElementById("userDataset_1").value;
    let dataInList = dataFromInput.split(",");
    let soonToBeSortedArray = [];
    for (let item of dataInList){
        soonToBeSortedArray = soonToBeSortedArray.concat(parseFloat(item));
    }
    let sortedArray = [];
    dataInList.sort(function(a,b){return a-b});
    let numItems = dataInList.length;
    let modeList = [] 
    sortedArray = dataInList
    let value = sortedArray[0]

    frequencyList = modeList.concat([[value,1]])

    let found = false
    for  (let index1 = 1; index1 < numItems; index1++){
        found = false
        for  (let index2 = 0; index2 < frequencyList.length; index2++){
            if (frequencyList[index2][0] === sortedArray[index1]){
                frequencyList[index2][1] += 1
                
                found = true
            }
        }
        if (found === false) {
            frequencyList = frequencyList.concat([[sortedArray[index1],1]])
        }
    }
    let List = ""
    for (let item of frequencyList){
        List = List + "[" + String(item) + "]"
    }
    return List


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
function calculateFrequencyBtn(){

    document.getElementById("frequencyPlaceholder").innerHTML = calculateFrequency();

}
