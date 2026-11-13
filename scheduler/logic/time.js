// Convert an HH:MM clock time to minutes since midnight.
export function toMinutes(time) {
  const [hours, minutes] = time.split(':').map(Number);
  return hours * 60 + minutes;
}

// Convert minutes since midnight to an HH:MM clock time.
export function fromMinutes(minutes) {
  const clockMinutes = ((minutes % 1440) + 1440) % 1440;
  const hours = Math.floor(clockMinutes / 60);
  const remainingMinutes = clockMinutes % 60;
  return `${String(hours).padStart(2, '0')}:${String(remainingMinutes).padStart(2, '0')}`;
}
