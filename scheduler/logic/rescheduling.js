// Import the shared clock conversion functions.
import { fromMinutes, toMinutes } from './time.js';

// Put a clock time after midnight on the late-night end of the current day.
function dayPosition(time, wakeTime) {
  const minutes = toMinutes(time);
  return minutes < wakeTime ? minutes + 1440 : minutes;
}

// Return the end of the latest timed task, ignoring tasks without an ideal time.
function latestTimedEnd(todayTasks, wakeTime) {
  return todayTasks
    .filter(task => task.idealTime !== null)
    .map(task => dayPosition(task.idealTime, wakeTime) + (task.lengthMinutes ?? 120))
    .reduce((latest, end) => Math.max(latest, end), -Infinity);
}

// Require a note before placing a rescheduled task.
function requireNote(note) {
  if (note.trim() === '') throw new Error('A rescheduling note is required');
}

// Place the task today when it fits, or tomorrow at the next wake time.
export function placeRescheduled({ task, note, todayTasks, bedtime, now }) {
  requireNote(note);
  const bedtimeMinutes = toMinutes(bedtime);
  const wakeTime = (bedtimeMinutes + 480) % 1440;
  const bedtimePosition = dayPosition(bedtime, wakeTime);
  const start = Math.max(dayPosition(now, wakeTime), latestTimedEnd(todayTasks, wakeTime));
  const length = task.lengthMinutes ?? 120;
  if (start + length <= bedtimePosition) {
    return { day: 'today', startTime: fromMinutes(start) };
  }
  return { day: 'tomorrow', startTime: fromMinutes(wakeTime) };
}
