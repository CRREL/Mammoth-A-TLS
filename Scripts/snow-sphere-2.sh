[
    {
        "type": "readers.rxp",
        "sync_to_pps": "false"
    },
    {
        "type":"filters.crop",
        "point":"POINT(-1.5 1.5 0.25)",
        "distance": "0.5, 0.5, 0.5"
    },
    {
        "type":"filters.stats",
        "dimensions":"X"
    },
    {
        "type":"writers.null"
    }
]
