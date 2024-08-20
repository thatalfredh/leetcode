# int main() {
#     vector<int> vec = {7,1,3,4,6,2,4};
#     // find minimum even number: mine
#     // find maximum even number: maxe
#     // find minimum odd number: mino
#     // find maximum odd number: maxo

#     int mine = INT_MAX, mino = INT_MAX;
#     int maxe = INT_MIN, maxo = INT_MIN;
#     for(auto& c: vec) {
#         if(c % 2) {
#             mino = min(mino, c);
#             maxo = max(maxo, c);
#         } else {
#             mine = min(mine, c);
#             maxe = max(maxe, c);
#         }
#     }

#     int cntE = 0;
#     int cntO = 0;
#     for(auto& c:vec) {
#         if(c >= mine && c <= maxe) cntE++;
#         if(c >= mino && c <= maxo) cntO++;
#     }
#     cout << max(cntE, cntO)<< endl;
#     return 0;
# }

# arr = [7, 1, 3, 4, 6, 2, 4]

arr = [2,4, 4, -5, 1,7]

min_odd = float('inf')
min_even = -float('inf')

max_odd = float('inf')
max_even = -float('inf')

for x in arr:
    if x % 2:
        min_odd = min(min_odd, x)
        max_odd = max(max_odd, x)
    else:
        min_even = min(min_even, x)
        max_even = max(max_even, x)

cnt_odd = 0
cnt_even = 0
for x in arr:
    if x >= min_even and x <= max_even:
        cnt_even += 1
    if x >= min_odd and x <= max_odd:
        cnt_odd += 1
        
print(min_odd)
print(max(cnt_even, cnt_odd))


