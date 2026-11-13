// Import the shared clock conversion function.
import { toMinutes } from './time.js';

// Find the median completion time for one task name.
function medianFor(name, history) {
  const times = history
    .filter(entry => entry.name === name)
    .map(entry => toMinutes(entry.completedAt))
    .sort((first, second) => first - second);
  if (times.length === 0) return null;
  const middle = Math.floor(times.length / 2);
  if (times.length % 2 === 1) return times[middle];
  return Math.floor((times[middle - 1] + times[middle]) / 2);
}

// Assign each task its ordering key without changing the original task objects.
function keyedTasks(tasks, history) {
  return tasks.map(task => ({
    task,
    time: task.idealTime === null ? medianFor(task.name, history) : toMinutes(task.idealTime),
  }));
}

// Order by time (ideal time, else same-name median); ties by entry order; tasks with neither go last, by entry order.
export function orderTasks(tasks, history) {
  return keyedTasks(tasks, history)
    .sort((first, second) => {
      const firstUntimed = first.time === null;
      const secondUntimed = second.time === null;
      if (firstUntimed !== secondUntimed) return firstUntimed ? 1 : -1;
      if (firstUntimed) return first.task.enteredAt - second.task.enteredAt;
      return first.time - second.time || first.task.enteredAt - second.task.enteredAt;
    })
    .map(item => item.task);
}
