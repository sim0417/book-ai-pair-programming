function twoSumImproved(nums, target) {
  const numMap = new Map(); // 해시 테이블 역할을 하는 Map 객체 생성

  for (let i = 0; i < nums.length; i++) {
    const complement = target - nums[i]; // 현재 요소와 짝을 이루어 target을 만들 수 있는 값 계산

    if (numMap.has(complement)) {
      // 만약 complement가 이미 Map에 있다면, 현재 요소와 짝이 될 수 있음
      return [numMap.get(complement), i]; // complement의 인덱스와 현재 요소의 인덱스 반환
    }

    numMap.set(nums[i], i); // 현재 요소의 값을 key로, 인덱스를 value로 Map에 저장
  }
}
const nums = [2, 7, 11, 15];
const target = 9;
console.log(twoSumImproved(nums, target)); // [0, 1]

const nums2 = [3, 1, 4, 6, 8];
const target2 = 10;
console.log(twoSumImproved(nums2, target2)); // [1, 3]

const nums3 = [5, 12, 9, 3, 6];
const target3 = 15;
console.log(twoSumImproved(nums3, target3)); // [1, 4]

const nums4 = [1, 2, 3, 4, 5];
const target4 = 7;
console.log(twoSumImproved(nums4, target4)); // [1, 4]

const nums5 = [10, 20, 30, 40, 50];
const target5 = 60;
console.log(twoSumImproved(nums5, target5)); // [2, 4]
