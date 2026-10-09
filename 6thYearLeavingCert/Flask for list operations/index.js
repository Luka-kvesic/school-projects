let DataList1 = []
let DataList2 = []
function initialiseLists(){
   for (data of irisData){
        DataList1.push(data[0])
        DataList2.push(data[1])

   }
    irisDataList = [DataList1, DataList2]

}
console.log(irisData)
initialiseLists();



function calculateMean() {
    let Means = []
    for (let DataList of irisDataList){
        let numItems = DataList.length;
        let total = 0
        for (let item of DataList){
            total += parseFloat(item);
        }
        Means.push(total / numItems)
    }

    let Mean = String(Means[0]) + "___AND___"+  String(Means[1])
    return Mean
}
function calculateMedian() {
    let medians = []
    for (let Datalist of irisDataList){
        let numItems = Datalist.length;

        
        Datalist.sort(function(a,b){return a-b});



        if (numItems%2 == 0) {
            let firstValue = parseFloat(Datalist[numItems/2]);
            let secondValue = parseFloat(Datalist[(numItems/2)-1]);
            medians.push((firstValue + secondValue) / 2);
            
        } else if (numItems%2 == 1) {
            medians.push(Datalist[(numItems-1)/2]);
            
        } 
    }
    return String(medians[0]) + "___AND___" + String(medians[1])

    
}
function calculateMode() {
    let modes = []
    for (let DataList of irisDataList){
        
        let sortedArray = [];
        DataList.sort(function(a,b){return a-b});
        let numItems = DataList.length;
        let modeList = [] 
        sortedArray = DataList
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
        let biggestValue = -999999999999999;
        for (let item of modeList){
            if (biggestValue <= item[1] ) {
                biggestValue = item[1];
                mode = item[0]
            }
        }
        modes.push(mode)
    }

    
    return String(modes[0]) + "___AND___" + String(modes[1])
}

function calculateRange() {
    let ranges = []
    for (let DataList of irisDataList){
        DataList.sort(function(a,b){return a-b});
        ranges.push([DataList[0]," to ", DataList[DataList.length -1]])
    }
    
    return ranges[0]+ "  " + "___AND___" +"  " + ranges[1]
}

function calculateFrequency(){
    let frequencies = []

    for (let DataList of irisDataList) {
        
        let sortedArray = [];
        DataList.sort(function(a,b){return a-b});
        let numItems = DataList.length;
        let modeList = [] 
        sortedArray = DataList
        let value = sortedArray[0]

        let frequencyList = modeList.concat([[value,1]])

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
        frequencies.push(List)
    }
    
    return frequencies[0] + "___AND___" + frequencies[1]


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
