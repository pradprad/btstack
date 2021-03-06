//
// btstack_config.h for esp32 port
//

#ifndef __BTSTACK_CONFIG
#define __BTSTACK_CONFIG

// Port related features
#define HAVE_EMBEDDED_TIME_MS
#define HAVE_MALLOC

// BTstack features that can be enabled
#define ENABLE_BLE
#define ENABLE_CLASSIC
#define ENABLE_LE_PERIPHERAL
#define ENABLE_LE_CENTRAL
#define ENABLE_LOG_ERROR
// #define ENABLE_LOG_INFO 
// #define ENABLE_LOG_DEBUG
// #define ENABLE_EHCILL

// BTstack configuration. buffers, sizes, ...
#define HCI_ACL_PAYLOAD_SIZE (1691 + 4)
#define MAX_NR_BNEP_CHANNELS MAX_SPP_CONNECTIONS
#define MAX_NR_BNEP_SERVICES 1
#define MAX_NR_BTSTACK_LINK_KEY_DB_MEMORY_ENTRIES  2
#define MAX_NR_GATT_CLIENTS 1
#define MAX_NR_HCI_CONNECTIONS MAX_SPP_CONNECTIONS
#define MAX_NR_HFP_CONNECTIONS 0
#define MAX_NR_L2CAP_CHANNELS  (1+MAX_SPP_CONNECTIONS)
#define MAX_NR_L2CAP_SERVICES  2
#define MAX_NR_RFCOMM_CHANNELS MAX_SPP_CONNECTIONS
#define MAX_NR_RFCOMM_MULTIPLEXERS MAX_SPP_CONNECTIONS
#define MAX_NR_RFCOMM_SERVICES 1
#define MAX_NR_SERVICE_RECORD_ITEMS 1
#define MAX_NR_SM_LOOKUP_ENTRIES 3
#define MAX_NR_WHITELIST_ENTRIES 1
#define MAX_SPP_CONNECTIONS 1
#define MAX_NR_LE_DEVICE_DB_ENTRIES 0
// 

// HCI Controller to Host Flow Control
//
// Needed on the ESP32, but not working yet
// see https://github.com/espressif/esp-idf/issues/480
//
// #define ENABLE_HCI_CONTROLLER_TO_HOST_FLOW_CONTROL

// Interal ring buffer
#define HCI_HOST_ACL_PACKET_NUM 10
#define HCI_HOST_ACL_PACKET_LEN 1024
#define HCI_HOST_SCO_PACKET_NUM 10
#define HCI_HOST_SCO_PACKET_LEN 60
#endif

