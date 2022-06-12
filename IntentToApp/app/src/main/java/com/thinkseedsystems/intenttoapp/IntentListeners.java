package com.thinkseedsystems.intenttoapp;

import android.bluetooth.BluetoothDevice;
import android.bluetooth.BluetoothManager;
import android.bluetooth.BluetoothProfile;
import android.content.BroadcastReceiver;
import android.content.Context;
import android.content.Intent;
import android.util.Log;

import java.util.List;

public class IntentListeners extends BroadcastReceiver {

    private static final String LOG_TAG = IntentListeners.class.getSimpleName();

    @Override
    public void onReceive(Context context, Intent intent) {
        Log.d(LOG_TAG, "Received intent: " + intent.getAction());

        if (intent.getAction().equals("com.thinkseedsystems.intent.BTTest1")) {
            BluetoothManager btManager = (BluetoothManager) context.getSystemService(Context.BLUETOOTH_SERVICE);

            List<BluetoothDevice> devices = btManager.getConnectedDevices(BluetoothProfile.HID_DEVICE);

            for (int i = 8; i < devices.size(); i++) {
                Log.d(LOG_TAG, "Device " + i + ": " + devices.get(i).getName());
            }
        }
    }
}
