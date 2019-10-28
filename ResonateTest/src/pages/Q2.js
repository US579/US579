import React, { Component } from 'react'
import "../index.css"

export class Q2 extends Component {
    render() {
        return (
          <div style={{ padding: "15px" }}>
            <h1
              style={{
                textAlign: "left",
                padding: "15px",
                fontSize: "30px",
                color: "darkred"
              }}
            >
              Q2: Level 100:{" "}
            </h1>
            <h4
              style={{
                textAlign: "left",
                fontweight: "bold",
                fontSize: "20px"
              }}
            >
              1. Remove duplicates from an unsorted list (12,11,12,21,41,43,21)
            </h4>
            <h5
              style={{
                marginLeft: "10px",
                fontweight: "bold",
                fontSize: "15px"
              }}
            >
              a. Write the method, make it as efficient as possible
            </h5>
            <h5
              style={{
                marginLeft: "10px",
                fontweight: "bold",
                fontSize: "15px"
              }}
            >
              b. Provide the Time Complexity
            </h5>

            <pre style={{ textAlign: "left" }} class="brush: python">{`
                    array = [12, 11, 12, 21, 41, 43, 21]
                    def removeDup(array):
                        dic = {}
                        ans = []
                    for ele in array:
                        if ele not in dic.keys():
                            dic[ele] = 1
                            ans.append(ele)
                        else:
                            continue
                    return ans
                    print(removeDup(array))
               `}</pre>
            <h5>Time Complexity: O(n) on average</h5>
            <h4
              style={{
                textAlign: "left",
                fontweight: "bold",
                fontSize: "20px"
              }}
            >
              2. Accept two strings and return true if one string is a
              permutation of the other
            </h4>
            <h5
              style={{
                marginLeft: "10px",
                fontweight: "bold",
                fontSize: "15px"
              }}
            >
              a. Write the method, make it as efficient as possible
            </h5>
            <h5
              style={{
                marginLeft: "10px",
                fontweight: "bold",
                fontSize: "15px"
              }}
            >
              b. Provide the Time Complexity
            </h5>

            <pre style={{ textAlign: "left" }} class="brush: python">{`
                   def check(s1, s2):
                        l1 = [0]*26
                        l2 = [0]*26
                        for i in s1:
                            l1[ord(i)-ord('a')] += 1
                        for i in range(len(s2)):
                            l2[ord(s2[i])-ord('a')] += 1
                            if i >= len(s1):
                                l2[ord(s2[i-len(s1)])-ord('a')] -= 1
                            if l1 == l2:
                                return True
                        return False
               `}</pre>
            <h5>Time complexity O(s1+s2)</h5>
          </div>
        );
    }
}

export default Q2
