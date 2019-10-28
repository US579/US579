import React, { Component } from 'react'

// TODO: Modify this function
function generateShortCode(storeId, transactionId) {
    // Logic goes here
    var date = new Date().getTime();
    // console.log(date)
    var uuid = 'x'.replace(/[xy]/g, function (c) {
        var appendedID = "" + storeId.toString().length + transactionId.toString().length + storeId + transactionId;
        console.log(c);
        var sar = ["0", "00", "000", "0000", "00000", "000000", "0000000"];
        var das = [1, 10, 100, 1000, 10000, 100000, 1000000];
        var l = (9 - appendedID.length) - 2;
        var docketNumber = 0
        if (appendedID.length === 9) {
            docketNumber = appendedID
        }
        if (appendedID.length < 9) {
            var randomnumber = Math.floor(Math.random() * ((9 - appendedID.length) - das[l + 1] + 1)) + das[l + 1];
            docketNumber = "" + appendedID + (9 - appendedID.length) + randomnumber;
        }
        //return docketNumber;
        return (c == 'x' ? docketNumber : "0000000");
    });
    // console.log(uuid)
    return uuid;
}

// TODO: Modify this function
function decodeShortCode(shortCode) {
    // Logic goes here
    var sLen = shortCode.substring(0, 1);
    var tLen = shortCode.substring(1, 2);
    var iLen = sLen + tLen
    return {
        storeId: parseInt(shortCode.substring(iLen.length, parseInt(sLen, 10) + iLen.length), 10), // store id goes here,
        shopDate: new Date(), // the date the customer shopped,
        transactionId: parseInt(shortCode.substring(parseInt(sLen, 10) + iLen.length, iLen.length + parseInt(sLen, 10) + parseInt(tLen, 10)), 10) // transaction id goes here
    };

}

// ------------------------------------------------------------------------------//
// --------------- Don't touch this area, all tests have to pass --------------- //
// ------------------------------------------------------------------------------//
function RunTests() {
    var storeIds = [175, 42, 0, 9]
    var transactionIds = [9675, 23, 123, 7]
    storeIds.forEach(function (storeId) {
        transactionIds.forEach(function (transactionId) {
            var shortCode = generateShortCode(storeId, transactionId);
            var decodeResult = decodeShortCode(shortCode);
            document.getElementById('test-results').append("<div>" + storeId + " - " + transactionId + ": " + shortCode + "</div>");
            AddTestResult("Length <= 9", shortCode.length <= 9);
            AddTestResult("Is String", (typeof shortCode === 'string'));
            AddTestResult("Is Today", IsToday(decodeResult.shopDate));
            AddTestResult("StoreId", storeId === decodeResult.storeId);
            AddTestResult("TransId", transactionId === decodeResult.transactionId);
        })
    })
}

function IsToday(inputDate) {
    // Get today's date
    var todaysDate = new Date();
    // call setHours to take the time out of the comparison
    return (inputDate.setHours(0, 0, 0, 0) == todaysDate.setHours(0, 0, 0, 0));
}

function AddTestResult(testName, testResult) {
    var div = document.getElementById('test-results').append("<div class='" + (testResult ? "pass" : "fail") + "'><span class='tname'>- " + testName + "</span><span class='tresult'>" + testResult + "</span></div>");
}

// funtion to clear the results Div
function clearDIV() {
    document.getElementById("test-results").innerHTML = "";
}


export class Q3 extends Component {
    render() {
        return (
            <div style={{ padding: "15px" }}>
                <h1 style={{
                        textAlign: "left",
                        padding: "15px",
                        fontSize: "30px",
                        color: "darkred",
                    }}
                >
                Q2: Level 200:
                </h1>
                <p style={{
                    
                    padding: "15px",
                    fontSize: "20px",
                }} >
                Our national retail client has a 200-store branch network, 
                they want to do a big promotion give-away. To participate, 
                customers must enter their email address with a unique code 
                (which is printed on their dockets) into OUR website. 
                No store has more than 10,000 customers/day.
                <br />
                The code must be no more than 9 characters long, and we have to be able to get the following information out:
                <br/>
                -Which store does the code belong to ?
                <br/>
                -Which date was the code issued ?
                <br/>
                -Which customer(transaction) did the docket belong to(a number starting again at 1 every day)
                </p>
                <div style={{ padding: "15px"}}>
                <p>
                <div style={{ paddingBottom: "10px",fontSize:"25px",color:"red"}}>Run tests</div>
                <button onClick={RunTests}>Run Tests</button>
                <button style={{ marginLeft: "10px" }} onClick={clearDIV}>clean Results</button>
                <h4 style={{paddingTop:"10px"}}>Test results:</h4>
                <div id="test-results"></div>
                </p >
                </div>
            </div>
        )
    }
}

export default Q3
