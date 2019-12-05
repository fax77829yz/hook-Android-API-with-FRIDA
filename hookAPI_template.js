Java.perform( function () {
  IMEI = '$IMEI'
  IMSI = '$IMSI'
  PHONENUMBER = '$PHONENUMBER'
  SIMOPERATORNAME = '$SIMOPERATORNAME'
  SERIAL = '$SERIAL'
  HARDWARE = '$HARDWARE'
  BRAND = '$BRAND'
  MODEL = '$MODEL'
  TAGS = '$TAGS'
  BATTERY = '$BATTERY'
  WIFI = '$WIFI'

  send("Hook Start...");
  // Feature Hook
  Java.use("android.telephony.TelephonyManager").getImei.overload().implementation=function() {
      return IMEI ;
  } 
  Java.use("android.telephony.TelephonyManager").getSubscriberId.overload().implementation=function() {
      return IMSI ;
  } 
  Java.use("android.telephony.TelephonyManager").getLine1Number.overload().implementation=function() {
      return PHONENUMBER ;
  } 
  Java.use("android.telephony.TelephonyManager").getSimOperatorName.overload().implementation=function() {
      return SIMOPERATORNAME ;
  } 
  // Build & System properties Hook
  var ver = Java.use('android.os.Build') ;
  ver.SERIAL.value = SERIAL ;
  ver.HARDWARE.value = HARDWARE ;
  ver.BRAND.value = BRAND ;
  ver.MODEL.value = MODEL ;
  ver.TAGS.value = TAGS ;

  // Battery Hook
  var Battery = Java.use('android.os.BatteryManager') ;
  Battery.EXTRA_LEVEL.value = "95" ;
  Battery.EXTRA_SCALE.value = "100" ;
  Battery.BATTERY_PROPERTY_CAPACITY.value = int(BATTERY) ;

  // Wifi Hook
  Java.use("android.net.wifi.WifiInfo").getMacAddress.overload().implementation=function() {
      return WIFI ;
  } 
  send("Hook end...") ;
});