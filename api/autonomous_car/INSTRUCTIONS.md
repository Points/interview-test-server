## The Autonomous Car

Points is developing an autonomous vehicle program. It's going well, but we need to iron out a few bugs. The
 Engineering Team would like to demo our progress to the Product Team, so we need to develop a tool that can take
 track and travel log data, and then determine whether our autonomous vehicle successfully navigated the track.

Track and travel log data are encoded as JSON. The "track" array contains entries for any position of the track where
 there is an obstacle in any of the 3 lanes (`"a"`, `"b"` or `"c"`). The "travelLog" array contains entries for any
 position of the track where the car has changed lanes, either to the `"left"` or `"right"`.

The autonomous car starts at position `0` on lane `"b"`, drives itself to the end of the track and can shift only one
 lane per position. The simulation should end when the car hits an obstacle, goes out-of-bounds, or when all "track"
 and "travelLog" entries have been processed.

### Instructions

1. Download and run this server (see [Getting Started](../../README.md#getting-started)).
2. Build an application / tool in a language as agreed with your hiring manager:
   * Fetches an autonomous car route JSON object from this API server (see the different levels below).
   * Use the route object's "track" & "travelLog" information to determine if the simulation will end successfully or
     if it will fail.
   * If the simulation results in a success, the application must return the following success response:
     ```json
     {"status":  "success"}
     ```
   * If the simulation results in a failure (running out of bounds or hitting an obstacle), the application must
     return an error response showing at which position the simulation fails:
     ```json
     {"status":  "error", "position": 2}
     ```

**Please timebox your solution to one day**

### Level 1

For this level, you can use fetch a static route object from each of the following endpoints:
 * [/autonomous-car/routes/empty-route](http://localhost:5000/autonomous-car/routes/empty-route) will return a route
   object with an empty "track" and "travelLog" arrays.
 * [/autonomous-car/routes/success-no-obstacles](http://localhost:5000/autonomous-car/routes/success-no-obstacles)
   will return a route object that should result in a successful simulation, **with zero obstacles on the track**.
 * [/autonomous-car/routes/success-with-obstacles](http://localhost:5000/autonomous-car/routes/success-with-obstacles)
   will return a route object that should result in a successful simulation, **with obstacles on the track**.
 * [/autonomous-car/routes/failure-out-of-bounds](http://localhost:5000/autonomous-car/routes/failure-out-of-bounds)
   will return a route object that should result in failure due to running out of bounds.
 * [/autonomous-car/routes/failure-hits-obstacle](http://localhost:5000/autonomous-car/routes/failure-hits-obstacle)
   will return a route object that should result in failure due to running into an obstacle.


### Level 2

_sometimes returns bad responses, handle accordingly_

For this level, you can fetch a random route (including the empty-route) using the endpoint:
* [/autonomous-car/routes/random](http://localhost:5000/autonomous-car/routes/random)
