import test from 'node:test';
import assert from 'node:assert/strict';
import { orderTasks } from './ordering.js';

// Return a task with only the fields needed by the ordering contract.
const task = (id, name, idealTime, enteredAt) => ({
  id,
  name,
  idealTime,
  lengthMinutes: null,
  enteredAt,
});

// Rule A: compare HH:MM values as minutes, and rule G: break ties by enteredAt.
test('orders tasks by ideal time and enteredAt', () => {
  const tasks = [
    task('late', 'Late', '14:05', 1),
    task('second', 'Second', '09:30', 20),
    task('first', 'First', '09:30', 10),
    task('early', 'Early', '08:05', 30),
  ];

  assert.deepEqual(orderTasks(tasks, []), ['early', 'first', 'second', 'late'].map(
    id => tasks.find(item => item.id === id)
  ));
});

// Rule F: use the floored average of the two middle same-name completions.
test('places an untimed task by the even-count median of same-name history', () => {
  const tasks = [
    task('tie', 'Tie', '09:30', 3),
    task('before', 'Before', '09:29', 1),
    task('exercise', 'Exercise', null, 2),
  ];
  const history = [
    { name: 'Exercise', completedAt: '09:00' },
    { name: 'Exercise', completedAt: '10:01' },
    { name: 'Reading', completedAt: '23:00' },
  ];

  assert.deepEqual(orderTasks(tasks, history).map(item => item.id), [
    'before',
    'exercise',
    'tie',
  ]);
});

// Issue rule: a task with neither time goes after timed tasks in entry order.
test('keeps untimed tasks without history after timed tasks in entry order', () => {
  const tasks = [
    task('untimed-second', 'Second', null, 20),
    task('timed', 'Timed', '12:00', 30),
    task('untimed-first', 'First', null, 10),
  ];

  assert.deepEqual(orderTasks(tasks, []).map(item => item.id), [
    'timed',
    'untimed-first',
    'untimed-second',
  ]);
});
