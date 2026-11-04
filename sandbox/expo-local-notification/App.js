// Import the screen and notification APIs.
import { useState } from 'react';
import { Button, Text, View } from 'react-native';
import * as Notifications from 'expo-notifications';

// Show scheduled notifications while the app is open.
Notifications.setNotificationHandler({
  handleNotification: async () => ({
    shouldShowBanner: true,
    shouldShowList: true,
    shouldPlaySound: false,
    shouldSetBadge: false,
  }),
});

// Ask for permission and schedule one reminder.
async function scheduleReminder(setMessage) {
  const permission = await Notifications.requestPermissionsAsync();
  if (permission.status !== 'granted') {
    setMessage('Permission denied');
    return;
  }

  const scheduledAt = new Date();
  const fireAt = new Date(scheduledAt.getTime() + 60 * 1000);
  await Notifications.scheduleNotificationAsync({
    content: {
      title: 'Test reminder',
      body: `Scheduled at ${scheduledAt.toLocaleTimeString()}; fires at ${fireAt.toLocaleTimeString()}`,
    },
    trigger: {
      type: Notifications.SchedulableTriggerInputTypes.DATE,
      date: fireAt,
    },
  });
  setMessage(
    `Scheduled at: ${scheduledAt.toLocaleTimeString()}\nFires at: ${fireAt.toLocaleTimeString()}`
  );
}

// Render the reminder button and its result.
export default function App() {
  const [message, setMessage] = useState('');

  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center' }}>
      <Button
        title="Remind me in 1 minute"
        onPress={() => scheduleReminder(setMessage)}
      />
      <Text>{message}</Text>
    </View>
  );
}
