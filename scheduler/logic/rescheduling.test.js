import test from 'node:test';
import assert from 'node:assert/strict';
import { placeRescheduled } from './rescheduling.js';

// Return a task with the fields used when placing a rescheduled task.
const task = (lengthMinutes = null) => ({
  id: 'task',
  name: 'Task',
  idealTime: null,
  lengthMinutes,
  enteredAt: 1,
});

// Rule H: a rescheduling note must contain more than whitespace.
test('rejects an empty or whitespace-only rescheduling note', () => {
  assert.throws(
    () => placeRescheduled({
      task: task(30),
      note: '   ',
      todayTasks: [],
      bedtime: '22:00',
      now: '10:00',
    }),
    Error
  );
  assert.throws(
    () => placeRescheduled({
      task: task(30),
      note: '',
      todayTasks: [],
      bedtime: '22:00',
      now: '10:00',
    }),
    Error
  );
});

// Rule D: start after both now and the end of the latest timed task.
test('starts after now or the latest timed task, whichever is later', () => {
  const todayTasks = [
    { ...task(30), id: 'latest', idealTime: '11:00' },
    { ...task(60), id: 'morning', idealTime: '09:00' },
    { ...task(600), id: 'untimed', idealTime: null },
  ];

  assert.deepEqual(placeRescheduled({
    task: task(30),
    note: 'Continue after lunch',
    todayTasks,
    bedtime: '20:00',
    now: '11:15',
  }), { day: 'today', startTime: '11:30' });
  assert.deepEqual(placeRescheduled({
    task: task(30),
    note: 'Continue after lunch',
    todayTasks,
    bedtime: '20:00',
    now: '12:00',
  }), { day: 'today', startTime: '12:00' });
});

// Rule E and the required default: null length is 120 minutes.
test('uses 120 minutes by default and allows ending exactly at bedtime', () => {
  assert.deepEqual(placeRescheduled({
    task: task(),
    note: 'Finish tonight',
    todayTasks: [],
    bedtime: '22:00',
    now: '20:00',
  }), { day: 'today', startTime: '20:00' });
  assert.deepEqual(placeRescheduled({
    task: task(),
    note: 'Finish tonight',
    todayTasks: [],
    bedtime: '22:00',
    now: '20:01',
  }), { day: 'tomorrow', startTime: '06:00' });
});

// Rule C: bedtime 23:00 plus eight hours wraps tomorrow's wake time to 07:00.
test('wraps the wake time past midnight for a late bedtime', () => {
  assert.deepEqual(placeRescheduled({
    task: task(60),
    note: 'Need more time',
    todayTasks: [],
    bedtime: '23:00',
    now: '22:30',
  }), { day: 'tomorrow', startTime: '07:00' });
});

// Rules B, B', C, and E: an after-midnight bedtime ends the day, and tomorrow starts at wake time.
test('moves a task that does not fit before an after-midnight bedtime to wake time', () => {
  const todayTasks = [
    { ...task(30), id: 'late-task', idealTime: '01:00' },
  ];

  assert.deepEqual(placeRescheduled({
    task: task(60),
    note: 'Need more time',
    todayTasks,
    bedtime: '02:00',
    now: '01:30',
  }), { day: 'tomorrow', startTime: '10:00' });
});
