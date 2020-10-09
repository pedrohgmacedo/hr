function stupid(n, k) {
    return ((k | k - 1) <= n ? k - 1 : k - 2)
}