#!/usr/bin/env python3
"""
Auto-fills the "Algorithm" and "Edge Cases" sections of each problem's README.md
in your cp-committee-prep repo (or wherever you cloned it).

Usage:
    python3 autofill_readmes.py /path/to/your/cloned/repo

Run this from anywhere, just point it at your local repo folder. It walks every
subdirectory looking for a README.md whose folder name matches one of the 19
problems, and replaces the "_(fill in)_" placeholder under the ## Algorithm and
## Edge Cases headers with the writeups. Approach / Time Complexity / Space
Complexity are left untouched since you're filling those in yourself.

It only ever touches README.md files, and only the two placeholder sections
inside them, so nothing else in the repo (solution files, other README content)
is affected. Prints a summary of what got updated vs skipped at the end.

After running, just review the diff (git diff), then:
    git add -A
    git commit -m "Add algorithm and edge case writeups"
    git push
"""
import sys
import os
import re

DATA = {
 "minimum-window-substring": {
  "title": "76 Minimum Window Substring",
  "algorithm": "First I build a frequency map `com` of every character in `t`. Then a second map `win`, initialized to 0 for each character that appears in `t`, which tracks how many of those characters are currently sitting inside my window.\n\nBefore the main loop starts, I pre-fill `win` using the first `t.length() - 1` characters of `s` (I leave out the very last one on purpose, it gets picked up in the main loop instead).\n\n`p1` is my left pointer and `p2` is the right one, starting at `t.length() - 1`. I use a flag `movep2` to know whether I still need to add `s[p2]` into `win` this round.\n\nWhile `p2` is within bounds: if `movep2` is set, I add `s[p2]` to `win`. Then I check if the window is currently valid, looping over every key in `com` and checking if `win` has at least that many of each character. If it's valid, I've found a candidate window, so I compare it to my current best and update `min`/`minS` if it's smaller, then shrink from the left (remove `s[p1]` from `win`, `p1++`). If it's not valid, I expand right instead (`p2++`, `movep2 = 1` so it gets counted next round).\n\nAt the end, `minS` is the answer, or an empty string if nothing worked.",
  "edge": "- If `t` is longer than `s`, no window can possibly fit, so I check this at the very top and return an empty string right away.\n- `t` can have repeated characters (e.g. `t = \"aab\"`), which works fine since `com` stores counts, not just presence.\n- If no valid window exists, `minS` just stays empty, which gets returned.\n- If `s` and `t` are the same string, the whole string is the only valid window.\n- Characters in `s` that never appear in `t` get ignored automatically, since `win` only tracks keys that exist in `com`."
 },
 "sliding-window-maximum": {
  "title": "239 Sliding Window Maximum",
  "algorithm": "I use a max-heap (Python's heapq is min-heap, so I push negative values) plus a dict called `consider` that counts how many of each value are currently alive in the window. Instead of physically removing something from the heap once it leaves the window, I just decrement its count in `consider` and clean it up lazily later.\n\nI seed the heap and `consider` with the first `k - 1` elements. Then I slide `p2` from `k - 1` to the end. Each step: push `nums[p2]` into the heap if it's new, and increment its count. Then I look at the top of the heap, and if that value has a count of 0 in `consider` (meaning it already left the window), I pop it, repeating until the top is actually still valid. Whatever's left on top is the max for this window, which I append to the answer. Then I remove `nums[p1]` from the window (decrement its count, or delete the key if it hits 0) and move `p1` forward.\n\nReturn the collected maxima at the end.",
  "edge": "- Duplicate values in the same window are fine, since I'm counting occurrences rather than just tracking presence.\n- `k = 1` means every element is its own window, and this still works since `p1` and `p2` effectively move together.\n- `k = len(nums)` just means there's one window covering the whole array.\n- Sometimes a stale max sits at the top of the heap for several iterations before it gets popped. The while loop handles this by popping as many as needed each time, so it stays correct even if cleanup lags a bit.\n- Worth noting this is O(n log n) because of the heap, not the actual optimal O(n) monotonic deque approach, so I should be ready to explain why I went this way if asked."
 },
 "trapping-rain-water": {
  "title": "42 Trapping Rain Water",
  "algorithm": "My approach splits the array into what I'm calling the main region and the end region, and handles them with two separate passes instead of the usual two-pointer-with-running-max method.\n\nMain region, left to right: I scan until I find the first nonzero height, which becomes my left wall (`lim`, at index `limi`). As I keep scanning right, I subtract each shorter bar's height from a running deficit called `maybe`, until I hit a bar `>= lim`. That bar becomes the new right wall, so I add `maybe + (gap width) * lim` to `water`, then treat this right wall as my new left wall and continue (I actually step `i` back by one so the same index gets reprocessed as a left wall).\n\nIf the last wall I find reaches the end of the array, I set `finish = 1`, meaning there's no leftover unbound region.\n\nEnd region, right to left: if `finish` is still 0, there's a chunk past the last confirmed right wall where water couldn't be bound looking left to right, but small dips between bumps there can still hold water when viewed from the right side. So I redo the same wall-finding logic in reverse, starting from the end and working back to `revlimi` (the last left wall found in the main pass).\n\nI add up water from both passes and return the total.",
  "edge": "- An all-zero array, or a strictly increasing/decreasing one, means no water gets trapped: `l` never becomes 1, or the main loop just never finds a right wall `>= lim`.\n- A single-peak array is handled fully by the main pass alone.\n- Very short arrays (length 0, 1, or 2) can't trap anything, since the loop bounds naturally prevent any wall from forming.\n- Water trapped only near the very end of the array is exactly why the end-region reverse pass is needed. One forward pass alone would miss it, which is worth explaining if I'm asked why I split it into two passes."
 },
 "car-pooling": {
  "title": "1184 Car Pooling",
  "algorithm": "Instead of a difference array, I ended up using a sorted approach with a min-heap for this one. I sort all the trips by their end location first.\n\nThen I keep a min-heap of currently active trips, keyed by drop-off point, and a running `currentcap` that starts at full `capacity`. Going through trips in order of increasing end point: first I pop and process anyone in the heap whose drop-off is `<= this trip's start`, since those passengers have already left, and I add their seats back to `currentcap`. Then I check if `currentcap` can fit the new trip. If not, I return False right away. Otherwise I subtract the passengers and push this trip onto the heap, keyed by its own end point.\n\nIf I get through every trip without a capacity violation, I return True.",
  "edge": "- Two trips sharing the same start or end still work fine, as long as the `drop off <= start` comparison holds. I use `<=` rather than `<`, so a passenger dropped off exactly where the next pickup happens still frees the seat in time.\n- A trip starting exactly where another ends is handled correctly for the same reason.\n- Capacity exactly matching the max simultaneous passengers should still return True, since the check only fails on strict overflow.\n- An empty `trips` list just returns True immediately, since the loop body never runs.\n- Worth flagging: the topic here is difference array, but what I actually wrote uses a sort-plus-heap simulation instead. I should have the classic difference-array version ready too (`diff[start] += passengers`, `diff[end] -= passengers`, then scan for any point exceeding capacity), in case that's specifically what's being asked about."
 },
 "product-of-array-except-self": {
  "title": "238 Product of Array Except Self",
  "algorithm": "I build a `prefix` array where `prefix[i]` is the product of everything to the left of `i` (starting at 1, accumulated left to right). Then a `suffix` array built the same way, but from the right.\n\nThe answer at each index is just `prefix[i] * suffix[i]`, since that's everything except `nums[i]` itself.",
  "edge": "- One zero in the array: that index correctly gets the product of everything else (which is nonzero), while every other index becomes 0, since either its prefix or suffix product will include that zero.\n- Two or more zeros: every result becomes 0.\n- Negative numbers are fine, since the sign just works itself out through normal multiplication.\n- An array of length 1: `prefix[0]` and `suffix[0]` both stay at their initial value of 1, so the result is 1."
 },
 "top-k-frequent-elements": {
  "title": "347 Top K Frequent Elements",
  "algorithm": "I build a frequency hashmap of every number in `nums`, then copy the entries into a 2D array `arr` where `arr[i] = [value, frequency]`. I sort that array in descending order of frequency using bubble sort, a nested loop swapping adjacent pairs when they're out of order. Not the most efficient way, but it gets the job done.\n\nI take the first `k` entries' values as the result.",
  "edge": "- If a bunch of elements tie on frequency, my bubble sort is stable here (only swapping on strict `<`), so the tie-break order depends on whatever order the hashmap iterated in, which isn't technically guaranteed. The problem says the answer is unambiguous either way, so it's fine in practice.\n- `k` equal to the total number of distinct elements just returns the whole sorted array.\n- All elements identical means a single entry in the frequency map, which trivially works regardless of `k`.\n- Worth mentioning this is O(n\u00b2) because of the bubble sort, not the optimal O(n log n) heap-based approach or O(n) bucket sort. I should be ready to explain the more efficient version if asked, since efficiency is explicitly part of what's being evaluated here."
 },
 "find-x-sum-of-all-k-long-subarrays-i": {
  "title": "3610 Find X-Sum of All K-Long Subarrays I",
  "algorithm": "First I find the max value in `nums` so I know how large to make my frequency array. Then I slide a window of size `k` across the array, and for every window position I reset `freq` to all zeros and rebuild it from scratch by counting what's in `nums[p .. p+k-1]`. Then I call `findsum(freq, x)` to get that window's answer.\n\n`findsum` runs `x` times. Each time it finds whichever value has the highest frequency (ties go to the larger value, that's the `i > maxpos` check), adds `maxpos * freq[maxpos]` to a running sum, then zeroes that value's frequency out so it isn't picked again.\n\nI return the array of all the per-window answers.",
  "edge": "- If there are fewer than `x` distinct values left in a window, `findsum` just keeps finding `max = 0` for the remaining rounds and adds nothing further, so it doesn't break.\n- Ties in frequency are deliberately broken toward the larger value, matching what the problem asks for.\n- `k = nums.length` just means there's a single window.\n- I rebuild the whole frequency array from scratch every window rather than sliding it incrementally, so it ends up roughly O(n\u00b7k) overall. That's fine for this easy version's constraints, but the harder follow-up version would need the incremental approach to pass within its limits, worth mentioning if it comes up."
 },
 "find-all-numbers-disappeared-in-an-array": {
  "title": "448 Find All Numbers Disappeared in an Array",
  "algorithm": "The trick here is using the array itself as a hash table. For every number, I go to its \"home index\" (`abs(num) - 1`) and negate whatever's sitting there, as long as it isn't already negative. That negation is what marks a number as seen.\n\nI use `abs(num)` when computing the index, because by the time I get to some numbers, earlier steps may have already flipped their sign.\n\nAfter that pass, I scan the array again. Any index that's still positive means that number (`index + 1`) was never marked, so it's missing. I collect all of those and return them.",
  "edge": "- A number showing up more than twice is handled fine, since the `if nums[index] > 0` check stops me from double-negating something already negative.\n- If every number from 1 to n appears exactly once, everything gets negated and I return an empty list.\n- If the same number repeats across the whole array (like `[1,1,1]`), only index 0 ever gets touched, so indices 1 and 2 correctly show up as missing (2 and 3).\n- This runs in O(1) extra space, which is really the whole point. I should be ready to explain how encoding \"visited\" as a sign flip directly in the input array works, since it doesn't look like a frequency array at first glance."
 },
 "sum-of-all-subset-xor-totals": {
  "title": "1993 Sum of All Subset XOR Totals",
  "algorithm": "I wrote a recursive helper `dfs(i, run)`, where `run` is the XOR accumulated so far for whatever subset I'm currently building, and `i` is the index I'm deciding on next.\n\nBase case: once `i` reaches the end of `nums`, that means I've finished deciding on one complete subset, so I return its accumulated XOR (`run`).\n\nOtherwise I branch two ways: one where I include `nums[i]` (`dfs(i+1, run ^ nums[i])`) and one where I don't (`dfs(i+1, run)`), and I add the two results together.\n\nI start it off with `dfs(0, 0)`, which ends up exploring all 2\u207f subsets and summing each one's XOR total.",
  "edge": "- An empty array hits the base case immediately, since `i >= len(nums)` is already true, returning 0.\n- A single-element array `[a]` gives two branches: include `a` (XOR total `a`) or don't (XOR total 0), so the sum ends up being `a`.\n- An all-zero array means every subset's XOR total is 0, so the whole sum is 0.\n- This is honestly just brute-force O(2\u207f), so it doesn't really show off a clever bit-manipulation trick. The neater way to do this is `(OR of all nums) << (n - 1)`, since every bit set in any number ends up set in exactly half of all subset XORs. I should have that reasoning ready, since that's probably the actual point of this problem."
 },
 "reverse-bits": {
  "title": "190 Reverse Bits",
  "algorithm": "I start with a result `m = 0` and loop 32 times, since it's a 32-bit integer. Each round: shift `m` left by 1 to make room for the next bit, grab the current lowest bit of `n` with `n & 1` and add it into `m`, then shift `n` right by 1 to move to its next bit.\n\nAfter 32 rounds, `m` holds `n`'s bits reversed, and I return it.",
  "edge": "- `n = 0` means every extracted bit is 0, so the result stays 0.\n- `n` with all 32 bits set stays unchanged, since all 1s reversed is still all 1s.\n- Shifting into the sign bit is fine in Java, since it's operating on the raw bit pattern with two's complement, so no special-casing is needed.\n- Leading zeros in `n` turn into trailing zeros in the output and vice versa. Easy to describe incorrectly out loud, so worth practicing the explanation."
 },
 "smallest-number-with-all-set-bits": {
  "title": "3676 Smallest Number With All Set Bits",
  "algorithm": "The answer is the smallest number `>= n` whose binary form is all 1s, meaning something of the form `2^c - 1`.\n\nStarting at `c = 1`, I compute what a `c`-bit all-ones number equals by summing `2^0 + 2^1 + ... + 2^(c-1)` using `pow(2, d)`. If that total is `>= n`, I return it immediately, since it's the answer.\n\nOtherwise I bump `c` up by one and try again.",
  "edge": "- If `n` is already all 1s (e.g. `n = 7 = 0b111`), the loop finds `c = 3` gives exactly 7, which is `>= n`, so it returns `n` itself. The answer can be `n` when `n` already fits the pattern.\n- `n = 1`: `c = 1` gives `2^0 = 1 >= 1`, returning immediately.\n- I'm using `pow()`, which is floating point, to compute powers of 2. Works fine at this problem's scale, but a bit shift (`1 << d`) would've been the more natural fit for a bit-manipulation problem, worth mentioning if asked why I did it this way."
 },
 "koko-eating-bananas": {
  "title": "907 Koko Eating Bananas",
  "algorithm": "I find the largest pile, which becomes my upper bound `u` for possible eating speeds, since eating faster than the biggest pile is pointless. Lower bound `l = 1`.\n\nI binary search on the answer (the eating speed `k`) rather than the array itself. For a candidate `mid`, I work out how many hours it would take at that speed, summing `ceil(pile / mid)` across all piles.\n\nIf that total exceeds `h`, `mid` is too slow, so I search the upper half (`l = mid + 1`). If it's `<= h`, `mid` works, so I save it as `validk` and try to go lower (`u = mid - 1`).\n\nOnce `l > u`, I return `validk`.",
  "edge": "- `h` exactly equal to the number of piles forces the maximum possible speed, since Koko can only touch one pile per hour.\n- A single pile: `l` and `u` converge fast, and the answer is just `ceil(pile / h)`.\n- `h` much larger than needed: the smallest speed `k = 1` already satisfies the constraint, and the search correctly lands there.\n- The `Math.ceil` on a cast-to-double division matters a lot here. Forgetting to round up is the classic bug in this exact problem, so it's worth calling out specifically."
 },
 "capacity-to-ship-packages-within-d-days": {
  "title": "1056 Capacity To Ship Packages Within D Days",
  "algorithm": "I binary search on the answer again, this time the ship capacity `w`. `l` starts at the heaviest single package (can't go below that) and `u` starts at the sum of everything (ship it all in one day).\n\nFor a candidate `mid`, I simulate loading days: greedily add weights to the current day's load (`runW`) as long as they fit, and once the next package would overflow, I start a new day with it as the first item. I count how many days (`d`) that takes.\n\nIf `d > days`, `mid` is too small, so I search up (`l = mid + 1`). If `d <= days`, `mid` works, so I save it as `validw` and try smaller (`u = mid - 1`).\n\nI return `validw` once the search converges.",
  "edge": "- An array of length 1: `l` and `u` are both just that one weight, converging immediately.\n- `days` exactly equal to `weights.length` forces the capacity to be at least the biggest single weight, since basically every day carries exactly one package in that tightest case.\n- `days = 1` forces `validw` to be the sum of everything.\n- The day-counting logic bumps `d` one extra time right at the last index, to close out the final day properly even if it wasn't overflowed into. That's a slightly unusual way to end the loop, so I'd want to trace through a small example before explaining it live."
 },
 "split-array-largest-sum": {
  "title": "410 Split Array Largest Sum",
  "algorithm": "I binary search on the answer again, this time the largest subarray sum. `l` is the biggest single element, `u` is the sum of the whole array.\n\nFor a candidate `mid`, I greedily count how many subarrays I'd need if no subarray can exceed `mid`. I keep a running sum, and whenever adding the next element would push past `mid`, I start a new subarray (bump the count `t`, reset `sum` to just that element).\n\nIf the resulting count `t <= k`, `mid` is feasible, so I save it as `validm` and try to shrink further (`u = mid - 1`). If `t > k`, `mid` is too small (would need more than `k` subarrays), so I search up (`l = mid + 1`).\n\nI return `validm`.",
  "edge": "- `k = 1` forces `validm` to be the sum of the whole array, since only one subarray is allowed.\n- `k >= len(nums)` means each element can be its own subarray, so `validm` converges to `max(nums)`.\n- A single-element array: `l` and `u` are both just `nums[0]`, regardless of `k`.\n- All elements equal: the greedy split behaves predictably, which makes it a good problem to trace through by hand if I'm asked to walk through the binary search live."
 },
 "n-th-tribonacci-number": {
  "title": "1236 N-th Tribonacci Number",
  "algorithm": "I handle `T(0) = 0` and `T(1) = T(2) = 1` directly as base cases first.\n\nFor `n >= 3`, I loop from 3 up to `n`, keeping only the last three values (`a`, `b`, `c`) instead of a full DP array. This is basically the space-optimized version of the recurrence `T(i) = T(i-1) + T(i-2) + T(i-3)`. Each step I compute `d = a + b + c`, then shift everything forward: `a = b`, `b = c`, `c = d`.\n\nI return `d` at the end.",
  "edge": "- `n = 0` returns immediately through the base case, so the loop never runs.\n- `n = 1` or `n = 2` are also handled directly by the base case.\n- `n = 3`: the loop runs exactly once and correctly gives `T(3) = 1 + 1 + 0 = 2`.\n- For larger `n` near the constraint limit, the values grow fairly fast, so I'd want to double-check that `int` doesn't overflow if the constraints were ever pushed higher."
 },
 "maximum-subarray": {
  "title": "53 Maximum Subarray",
  "algorithm": "I set `max` to `nums[0]` to start (this matters for all-negative arrays) and `sum` to 0. I go through the array adding each element into `sum`, and after each addition I check whether `sum` is now bigger than `max`, updating `max` if so.\n\nThe main idea: if `sum` ever goes negative, I reset it back to 0, since a negative running sum can only drag down any future subarray, so it's better to just start fresh from the next element. This is the core Kadane's algorithm insight.\n\nI return `max`.",
  "edge": "- An all-negative array still works, since `max` starts at `nums[0]`. Even though `sum` keeps getting reset to 0, the true answer (the least negative single element) still gets caught by the `max` comparison before each reset.\n- A single-element array: both `max` and `sum` correctly resolve to that one value.\n- When the best subarray starts somewhere after a negative prefix, that's exactly what the `sum < 0` reset handles, and I should be ready to explain why discarding a negative running sum is always safe."
 },
 "n-queens": {
  "title": "51 N-Queens",
  "algorithm": "I keep the board as a 2D character grid, a `cols` set for which columns already have a queen, and a `placed` list of `(row, col)` for queens placed so far.\n\n`dfs(i, j)` tries placing a queen at row `i`, column `j`. Base case: if `placed` has `n` queens in it, that's a full solution, so I snapshot the board into `sol`. To check validity, I skip if column `j` is taken, or if any placed queen shares a diagonal with `(i, j)`, checked with `abs(i-x) == abs(j-y)` against every placed queen (no separate row check is needed, since the recursion only ever tries one queen per row).\n\nIf it's valid, I place the queen (mark `cols`, add to `placed`, set the board cell), then recurse into the next row starting at column 0 (`dfs(i+1, 0)`), and once that call returns, I undo all three of those changes (backtrack).\n\nThen, regardless of whether this cell worked, I also try the next column in the same row (`dfs(i, j+1)`), which is what actually walks through every column option per row.\n\nI kick it off with `dfs(0, 0)` and return `sol`.",
  "edge": "- `n = 1` trivially works: a single queen on a 1x1 board.\n- `n = 2` or `n = 3` has no valid placement at all, so `sol` stays empty, since every branch gets eliminated by the column and diagonal checks before `placed` ever reaches size `n`.\n- Queens sharing a diagonal that isn't directly adjacent are still caught correctly, since `abs(i-x) == abs(j-y)` works at any distance, not just neighboring cells.\n- Backtracking correctness is the part I'd want to explain carefully: popping `cols`, popping `placed`, and resetting the board cell all have to happen together after `dfs(i+1, 0)` returns, no matter the outcome, otherwise leftover state leaks into the `dfs(i, j+1)` branch."
 },
 "partition-to-k-equal-sum-subsets": {
  "title": "698 Partition to K Equal Sum Subsets",
  "algorithm": "If the total sum doesn't divide evenly by `k`, I return False right away, since no partition can work.\n\nI sort `nums` in descending order first, which helps fail bad branches faster, since larger numbers are the most constrained to place. `maxsum = total / k` is the target each of the `k` buckets needs to reach.\n\n`dfs(i, size)` tries to put `nums[i]` into one of the `k` buckets. Base case: if `size == len(nums)`, everything's been placed, so I return True. For each bucket `j`, if adding `nums[i]` wouldn't exceed `maxsum`, I place it there and recurse to the next number (`dfs(i+1, size+1)`), returning True right away if that succeeds. If it doesn't, I undo the placement and try the next bucket.\n\nOne optimization: if a bucket is still empty after failing to place the current number there, I stop trying other buckets for this number entirely, since placing it in any other empty bucket would just be the same situation repeated.\n\nI start with `dfs(0, 0)` and return the result.",
  "edge": "- A total not divisible by `k` gets caught immediately, with no recursion needed.\n- A single number larger than `maxsum` means every bucket fails for it, so `dfs` exhausts all branches and correctly returns False.\n- `k = 1` technically works out to True (the whole array is the one bucket), but it still goes through the full recursion instead of being special-cased, which is worth mentioning if asked.\n- Sorting descending as a pruning move is worth explaining: larger numbers have the fewest buckets that can actually fit them, so bad branches get cut off early instead of surfacing deep in the recursion."
 },
 "range-sum-query-immutable": {
  "title": "303 Range Sum Query - Immutable",
  "algorithm": "In the constructor, I build a running prefix sum array `pre`, where `pre[i]` is the sum of everything from index 0 to `i`.\n\nFor `sumRange(left, right)`, just computing `pre[right] - pre[left]` would exclude `nums[left]` itself, since `pre[left]` already includes it, so I add `num[left]` back in to correct for that: `pre[right] - pre[left] + num[left]`.\n\nEach query after the initial setup runs in O(1).",
  "edge": "- `left == right` correctly reduces down to just `num[left]`.\n- `left == 0` still works, since `pre[0]` is just `num[0]` to begin with.\n- Negative numbers don't cause any issues, since it's just addition with no assumption of positivity.\n- Repeated queries stay O(1) each, regardless of how large the range is, which is really the whole point of precomputing the prefix sums."
 }
}

def process_readme(path, entry):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    changed = False

    algo_pattern = re.compile(
        r"(## Algorithm\s*\n\s*\n)_\(fill in\)_",
    )
    if algo_pattern.search(text):
        text = algo_pattern.sub(lambda m: m.group(1) + entry["algorithm"], text, count=1)
        changed = True

    edge_pattern = re.compile(
        r"(## Edge Cases\s*\n\s*\n)_\(fill in\)_",
    )
    if edge_pattern.search(text):
        text = edge_pattern.sub(lambda m: m.group(1) + entry["edge"], text, count=1)
        changed = True

    if changed:
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)

    return changed

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 autofill_readmes.py /path/to/your/cloned/repo")
        sys.exit(1)

    repo_root = sys.argv[1]
    if not os.path.isdir(repo_root):
        print(f"Not a directory: {repo_root}")
        sys.exit(1)

    updated = []
    already_filled_or_no_match = []
    not_found = set(DATA.keys())

    for dirpath, dirnames, filenames in os.walk(repo_root):
        folder_name = os.path.basename(dirpath)
        if folder_name in DATA and "README.md" in filenames:
            readme_path = os.path.join(dirpath, "README.md")
            entry = DATA[folder_name]
            not_found.discard(folder_name)
            if process_readme(readme_path, entry):
                updated.append(entry["title"])
            else:
                already_filled_or_no_match.append(entry["title"])

    print(f"Updated {len(updated)} README(s):")
    for t in updated:
        print(f"  - {t}")

    if already_filled_or_no_match:
        print(f"\nFound but nothing to fill (already filled, or headers didn't match) in {len(already_filled_or_no_match)}:")
        for t in already_filled_or_no_match:
            print(f"  - {t}")

    if not_found:
        print(f"\nCouldn't find a matching folder for {len(not_found)} problem(s), check these exist in the repo:")
        for slug in not_found:
            print(f"  - {slug}")

if __name__ == "__main__":
    main()
