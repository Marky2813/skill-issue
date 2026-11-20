# Docker: questions

## Quiz misses (re-ask until correct)

- [ ] Why do orphan processes get reparented to PID 1? (first answer: "so they can be killed", but they can be killed anyway; real reason is reaping)
- [x] A server forks a child per request and never calls `wait()`. What breaks, and what resource actually runs out? (2026-11-19: zombies, each holding a PID; fork fails at the limit)
- [ ] Which namespace gives a container its own process list, and what does it isolate (and NOT isolate)? (2026-11-19: said "process namespace ... and the environment", which overreaches)

## Open questions

