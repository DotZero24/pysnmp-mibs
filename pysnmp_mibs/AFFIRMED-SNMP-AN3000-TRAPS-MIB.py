# SNMP MIB module (AFFIRMED-SNMP-AN3000-TRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsoft/AFFIRMED-SNMP-AN3000-TRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:30 2025
# On host Robs-Air.vegmond.io platform Darwin version 25.0.0 by user rob
# Using Python version 3.12.11 (main, Jun  3 2025, 15:41:47) [Clang 17.0.0 (clang-1700.0.13.3)]

if 'mibBuilder' not in globals():
    import sys

    sys.stderr.write(__doc__)
    sys.exit(1)

# Import base ASN.1 objects even if this MIB does not use it

(Integer,
 OctetString,
 ObjectIdentifier) = mibBuilder.importSymbols(
    "ASN1",
    "Integer",
    "OctetString",
    "ObjectIdentifier")

(NamedValues,) = mibBuilder.importSymbols(
    "ASN1-ENUMERATION",
    "NamedValues")
(ConstraintsIntersection,
 ConstraintsUnion,
 SingleValueConstraint,
 ValueRangeConstraint,
 ValueSizeConstraint) = mibBuilder.importSymbols(
    "ASN1-REFINEMENT",
    "ConstraintsIntersection",
    "ConstraintsUnion",
    "SingleValueConstraint",
    "ValueRangeConstraint",
    "ValueSizeConstraint")

# Import SMI symbols from the MIBs this MIB depends on

(action,
 actions,
 activesize,
 adminstate,
 affirmedAlarmChassisName,
 affirmedAlarmDateTime,
 affirmedAlarmDetails,
 affirmedAlarmRefSeqId,
 affirmedAlarmSeqId,
 affirmedAlarmSeverity,
 affirmedAlarmSourceId,
 affirmedCorrectiveAction,
 affirmedPotentialImpact,
 affirmedVmSourceIpAddress,
 affirmedVmSourceName,
 alarmid,
 apnname,
 availablesize,
 bfdsessiondescription,
 cafilename,
 chassis,
 chassisid,
 cid,
 clientid,
 clusterid,
 cpu,
 cpuid,
 currentstate,
 data,
 datetime,
 destination,
 dirname,
 diskid,
 expirydate,
 failuredescription,
 fault,
 filepath,
 gatewayipaddress,
 gatewayname,
 groupname,
 hardorsoft,
 ifadminstatus,
 ifindex,
 ifname,
 ifoperstatus,
 importnum,
 imsi,
 index,
 info,
 interfacename,
 ip,
 ipaddressthreshold,
 ipaddressutilization,
 ipversiontype,
 lasterrorcode,
 lasterrosubcode,
 ledcolor,
 ledname,
 level,
 localhostidentity,
 localpeeripaddr,
 mcmslotnumber,
 name,
 netcontext,
 netctxtname,
 node,
 nodeid,
 nodename,
 numpurged,
 operation,
 parent,
 peerhostidentity,
 peeringname,
 peeripaddress,
 peername,
 peerrealmname,
 port,
 portchunkthreshold,
 portchunkutilization,
 prefix,
 readerrors,
 realmname,
 reason,
 remotepeeripaddr,
 requiredsize,
 resource,
 resultstr,
 role,
 sensor,
 servicename,
 services,
 sessionthreshold,
 sessionutilization,
 sid,
 slot,
 slotid,
 slotnumber,
 standbysize,
 state,
 statestring,
 status,
 subsgroupname,
 subsidfilename,
 subtype,
 suggestedrecovery,
 taskname,
 threshold,
 time,
 type,
 uepoolutilization,
 unused,
 usid,
 writeerrors,
 xpath) = mibBuilder.importSymbols(
    "AFFIRMED-ALARM-MIB",
    "action",
    "actions",
    "activesize",
    "adminstate",
    "affirmedAlarmChassisName",
    "affirmedAlarmDateTime",
    "affirmedAlarmDetails",
    "affirmedAlarmRefSeqId",
    "affirmedAlarmSeqId",
    "affirmedAlarmSeverity",
    "affirmedAlarmSourceId",
    "affirmedCorrectiveAction",
    "affirmedPotentialImpact",
    "affirmedVmSourceIpAddress",
    "affirmedVmSourceName",
    "alarmid",
    "apnname",
    "availablesize",
    "bfdsessiondescription",
    "cafilename",
    "chassis",
    "chassisid",
    "cid",
    "clientid",
    "clusterid",
    "cpu",
    "cpuid",
    "currentstate",
    "data",
    "datetime",
    "destination",
    "dirname",
    "diskid",
    "expirydate",
    "failuredescription",
    "fault",
    "filepath",
    "gatewayipaddress",
    "gatewayname",
    "groupname",
    "hardorsoft",
    "ifadminstatus",
    "ifindex",
    "ifname",
    "ifoperstatus",
    "importnum",
    "imsi",
    "index",
    "info",
    "interfacename",
    "ip",
    "ipaddressthreshold",
    "ipaddressutilization",
    "ipversiontype",
    "lasterrorcode",
    "lasterrosubcode",
    "ledcolor",
    "ledname",
    "level",
    "localhostidentity",
    "localpeeripaddr",
    "mcmslotnumber",
    "name",
    "netcontext",
    "netctxtname",
    "node",
    "nodeid",
    "nodename",
    "numpurged",
    "operation",
    "parent",
    "peerhostidentity",
    "peeringname",
    "peeripaddress",
    "peername",
    "peerrealmname",
    "port",
    "portchunkthreshold",
    "portchunkutilization",
    "prefix",
    "readerrors",
    "realmname",
    "reason",
    "remotepeeripaddr",
    "requiredsize",
    "resource",
    "resultstr",
    "role",
    "sensor",
    "servicename",
    "services",
    "sessionthreshold",
    "sessionutilization",
    "sid",
    "slot",
    "slotid",
    "slotnumber",
    "standbysize",
    "state",
    "statestring",
    "status",
    "subsgroupname",
    "subsidfilename",
    "subtype",
    "suggestedrecovery",
    "taskname",
    "threshold",
    "time",
    "type",
    "uepoolutilization",
    "unused",
    "usid",
    "writeerrors",
    "xpath")

(affirmedSnmp,
 affirmedSnmpNotifications) = mibBuilder.importSymbols(
    "AFFIRMED-SNMP-MIB",
    "affirmedSnmp",
    "affirmedSnmpNotifications")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(Bits,
 Counter32,
 Counter64,
 Gauge32,
 Integer32,
 IpAddress,
 ModuleIdentity,
 MibIdentifier,
 NotificationType,
 ObjectIdentity,
 MibScalar,
 MibTable,
 MibTableRow,
 MibTableColumn,
 TimeTicks,
 Unsigned32,
 iso) = mibBuilder.importSymbols(
    "SNMPv2-SMI",
    "Bits",
    "Counter32",
    "Counter64",
    "Gauge32",
    "Integer32",
    "IpAddress",
    "ModuleIdentity",
    "MibIdentifier",
    "NotificationType",
    "ObjectIdentity",
    "MibScalar",
    "MibTable",
    "MibTableRow",
    "MibTableColumn",
    "TimeTicks",
    "Unsigned32",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

affirmedSnmpAn3000Traps = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AffirmedSnmpAn3000TrapsScalars_ObjectIdentity = ObjectIdentity
affirmedSnmpAn3000TrapsScalars = _AffirmedSnmpAn3000TrapsScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 1)
)
_AffirmedSnmpAn3000TrapsTables_ObjectIdentity = ObjectIdentity
affirmedSnmpAn3000TrapsTables = _AffirmedSnmpAn3000TrapsTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 2)
)
_AffirmedSnmpAn3000TrapsNotifications_ObjectIdentity = ObjectIdentity
affirmedSnmpAn3000TrapsNotifications = _AffirmedSnmpAn3000TrapsNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3)
)
_AffirmedSnmpAn3000TrapsNotificationPrefix_ObjectIdentity = ObjectIdentity
affirmedSnmpAn3000TrapsNotificationPrefix = _AffirmedSnmpAn3000TrapsNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0)
)
_AffirmedSnmpAn3000TrapsNotificationObjects_ObjectIdentity = ObjectIdentity
affirmedSnmpAn3000TrapsNotificationObjects = _AffirmedSnmpAn3000TrapsNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 1)
)

# Managed Objects groups


# Notification objects

fmSWCompMCMSwitchoverEventData = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 19)
)
fmSWCompMCMSwitchoverEventData.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "chassis"),
        ("AFFIRMED-ALARM-MIB", "cpu"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmSWCompMCMSwitchoverEventData.setStatus(
        "current"
    )

fmNmAn3000ColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 23)
)
fmNmAn3000ColdStart.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmNmAn3000ColdStart.setStatus(
        "current"
    )

fmNmAn3000Test = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 24)
)
fmNmAn3000Test.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmNmAn3000Test.setStatus(
        "current"
    )

fmNmAn3000Commit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 25)
)
fmNmAn3000Commit.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmNmAn3000Commit.setStatus(
        "current"
    )

fmHmCacheOperStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 28)
)
fmHmCacheOperStateDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmHmCacheOperStateDown.setStatus(
        "current"
    )

anTemperatureAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 29)
)
anTemperatureAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "data"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "sensor"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anTemperatureAlarm.setStatus(
        "current"
    )

anVoltageAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 30)
)
anVoltageAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "data"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "sensor"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anVoltageAlarm.setStatus(
        "current"
    )

anHotSwapAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 31)
)
anHotSwapAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "data"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "sensor"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anHotSwapAlarm.setStatus(
        "current"
    )

anTelcoAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 32)
)
anTelcoAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "data"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "sensor"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anTelcoAlarm.setStatus(
        "deprecated"
    )

anWatchdogAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 33)
)
anWatchdogAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "data"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "sensor"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anWatchdogAlarm.setStatus(
        "deprecated"
    )

anFanAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 34)
)
anFanAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "data"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "sensor"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anFanAlarm.setStatus(
        "deprecated"
    )

anAirFilterAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 35)
)
anAirFilterAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "data"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "sensor"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anAirFilterAlarm.setStatus(
        "current"
    )

anTachAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 36)
)
anTachAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "data"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "sensor"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anTachAlarm.setStatus(
        "current"
    )

anHWAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 37)
)
anHWAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "data"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "sensor"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anHWAlarm.setStatus(
        "current"
    )

fmCntnFilterCategoryFileTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 39)
)
fmCntnFilterCategoryFileTooBig.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmCntnFilterCategoryFileTooBig.setStatus(
        "current"
    )

fmCntnFilterCategoryFileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 40)
)
fmCntnFilterCategoryFileNotFound.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmCntnFilterCategoryFileNotFound.setStatus(
        "current"
    )

fmCntnFilterCategoryFileOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 41)
)
fmCntnFilterCategoryFileOverflow.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmCntnFilterCategoryFileOverflow.setStatus(
        "current"
    )

fmCntnFilterBlacklistFileOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 42)
)
fmCntnFilterBlacklistFileOverflow.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmCntnFilterBlacklistFileOverflow.setStatus(
        "current"
    )

fmCntnFilterBlacklistFileTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 44)
)
fmCntnFilterBlacklistFileTooBig.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmCntnFilterBlacklistFileTooBig.setStatus(
        "current"
    )

fmCntnFilterBlacklistFileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 45)
)
fmCntnFilterBlacklistFileNotFound.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmCntnFilterBlacklistFileNotFound.setStatus(
        "current"
    )

anCardNotBootingUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 46)
)
anCardNotBootingUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCardNotBootingUp.setStatus(
        "deprecated"
    )

fmCntnFilterCategoryFileInvalidEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 47)
)
fmCntnFilterCategoryFileInvalidEntry.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmCntnFilterCategoryFileInvalidEntry.setStatus(
        "current"
    )

fmCntnFilterBlacklistFileInvalidEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 48)
)
fmCntnFilterBlacklistFileInvalidEntry.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmCntnFilterBlacklistFileInvalidEntry.setStatus(
        "current"
    )

fmCntnHttpProxyServerConnectFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 49)
)
fmCntnHttpProxyServerConnectFail.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    fmCntnHttpProxyServerConnectFail.setStatus(
        "obsolete"
    )

anCntnFilterWhitelistFileInvalidEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 56)
)
anCntnFilterWhitelistFileInvalidEntry.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnFilterWhitelistFileInvalidEntry.setStatus(
        "current"
    )

anCntnFilterWhitelistFileOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 57)
)
anCntnFilterWhitelistFileOverflow.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnFilterWhitelistFileOverflow.setStatus(
        "current"
    )

anCntnFilterWhitelistFileTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 58)
)
anCntnFilterWhitelistFileTooBig.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnFilterWhitelistFileTooBig.setStatus(
        "current"
    )

anCntnFilterWhitelistFileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 59)
)
anCntnFilterWhitelistFileNotFound.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnFilterWhitelistFileNotFound.setStatus(
        "current"
    )

anGtpPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 60)
)
anGtpPeerDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGtpPeerDown.setStatus(
        "current"
    )

anCacheDiskOperationalStateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 61)
)
anCacheDiskOperationalStateAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCacheDiskOperationalStateAlarm.setStatus(
        "current"
    )

anCntnUrlListFileInvalidEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 62)
)
anCntnUrlListFileInvalidEntry.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnUrlListFileInvalidEntry.setStatus(
        "current"
    )

anCntnUrlListFileOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 63)
)
anCntnUrlListFileOverflow.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnUrlListFileOverflow.setStatus(
        "current"
    )

anCntnUrlListFileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 64)
)
anCntnUrlListFileNotFound.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnUrlListFileNotFound.setStatus(
        "current"
    )

anCntnUrlListFileTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 65)
)
anCntnUrlListFileTooBig.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnUrlListFileTooBig.setStatus(
        "current"
    )

anPlaFileDownloadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 67)
)
anPlaFileDownloadFail.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPlaFileDownloadFail.setStatus(
        "current"
    )

anThresholdCrossingAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 68)
)
anThresholdCrossingAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anThresholdCrossingAlarm.setStatus(
        "current"
    )

anTaskOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 69)
)
anTaskOverload.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "cpu"),
        ("AFFIRMED-ALARM-MIB", "level"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "subtype"),
        ("AFFIRMED-ALARM-MIB", "taskname"),
        ("AFFIRMED-ALARM-MIB", "time"),
        ("AFFIRMED-ALARM-MIB", "type"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anTaskOverload.setStatus(
        "current"
    )

anBladeOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 70)
)
anBladeOverload.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "actions"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "cpu"),
        ("AFFIRMED-ALARM-MIB", "level"),
        ("AFFIRMED-ALARM-MIB", "services"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anBladeOverload.setStatus(
        "current"
    )

anSystemOverload = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 71)
)
anSystemOverload.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "level"),
        ("AFFIRMED-ALARM-MIB", "subtype"),
        ("AFFIRMED-ALARM-MIB", "type"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anSystemOverload.setStatus(
        "obsolete"
    )

anCantPageSubscriberOutOfBuffers = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 73)
)
anCantPageSubscriberOutOfBuffers.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "chassis"),
        ("AFFIRMED-ALARM-MIB", "cpu"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCantPageSubscriberOutOfBuffers.setStatus(
        "deprecated"
    )

anLedStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 74)
)
anLedStateChange.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "ledcolor"),
        ("AFFIRMED-ALARM-MIB", "ledname"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLedStateChange.setStatus(
        "current"
    )

anRebootEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 78)
)
anRebootEvent.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "hardorsoft"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anRebootEvent.setStatus(
        "current"
    )

anCacheDiskErrorStateAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 79)
)
anCacheDiskErrorStateAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "readerrors"),
        ("AFFIRMED-ALARM-MIB", "writeerrors"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCacheDiskErrorStateAlarm.setStatus(
        "current"
    )

anPayloadFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 80)
)
anPayloadFailure.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "failuredescription"),
        ("AFFIRMED-ALARM-MIB", "slotnumber"),
        ("AFFIRMED-ALARM-MIB", "suggestedrecovery"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPayloadFailure.setStatus(
        "current"
    )

anLDAPServerConnectFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 81)
)
anLDAPServerConnectFail.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "netcontext"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLDAPServerConnectFail.setStatus(
        "current"
    )

anLDAPServerConnectLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 82)
)
anLDAPServerConnectLost.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "netcontext"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLDAPServerConnectLost.setStatus(
        "current"
    )

anLDAPProfNoServerConnected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 83)
)
anLDAPProfNoServerConnected.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLDAPProfNoServerConnected.setStatus(
        "current"
    )

anCntnUaProfDefaultAttsMissing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 86)
)
anCntnUaProfDefaultAttsMissing.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnUaProfDefaultAttsMissing.setStatus(
        "current"
    )

anIpInterfaceOperStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 88)
)
anIpInterfaceOperStatusDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anIpInterfaceOperStatusDown.setStatus(
        "current"
    )

anDiameterPeerLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 89)
)
anDiameterPeerLinkDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "localhostidentity"),
        ("AFFIRMED-ALARM-MIB", "nodename"),
        ("AFFIRMED-ALARM-MIB", "peerhostidentity"),
        ("AFFIRMED-ALARM-MIB", "peerrealmname"),
        ("AFFIRMED-ALARM-MIB", "realmname"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDiameterPeerLinkDown.setStatus(
        "current"
    )

anDiameterPeerLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 90)
)
anDiameterPeerLinkUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "localhostidentity"),
        ("AFFIRMED-ALARM-MIB", "nodename"),
        ("AFFIRMED-ALARM-MIB", "peerhostidentity"),
        ("AFFIRMED-ALARM-MIB", "peerrealmname"),
        ("AFFIRMED-ALARM-MIB", "realmname"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDiameterPeerLinkUp.setStatus(
        "deprecated"
    )

anRadiusPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 91)
)
anRadiusPeerDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "clientid"),
        ("AFFIRMED-ALARM-MIB", "peername"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anRadiusPeerDown.setStatus(
        "current"
    )

anRadiusPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 92)
)
anRadiusPeerUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "clientid"),
        ("AFFIRMED-ALARM-MIB", "peername"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anRadiusPeerUp.setStatus(
        "deprecated"
    )

anGtppPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 93)
)
anGtppPeerDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "peername"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGtppPeerDown.setStatus(
        "current"
    )

anGtppPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 94)
)
anGtppPeerUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "peername"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGtppPeerUp.setStatus(
        "deprecated"
    )

anSMSCServerConnectFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 95)
)
anSMSCServerConnectFail.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anSMSCServerConnectFail.setStatus(
        "current"
    )

anSMSCProfNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 96)
)
anSMSCProfNotFound.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anSMSCProfNotFound.setStatus(
        "current"
    )

anSMSCServerConnectLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 97)
)
anSMSCServerConnectLost.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anSMSCServerConnectLost.setStatus(
        "current"
    )

anPdnSessionAntiSpoofing = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 98)
)
anPdnSessionAntiSpoofing.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "imsi"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPdnSessionAntiSpoofing.setStatus(
        "current"
    )

anSgwServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 99)
)
anSgwServiceUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anSgwServiceUp.setStatus(
        "current"
    )

anSgwServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 100)
)
anSgwServiceDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anSgwServiceDown.setStatus(
        "current"
    )

anPgwServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 101)
)
anPgwServiceUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPgwServiceUp.setStatus(
        "current"
    )

anPgwServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 102)
)
anPgwServiceDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPgwServiceDown.setStatus(
        "current"
    )

anGgsnServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 103)
)
anGgsnServiceUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGgsnServiceUp.setStatus(
        "current"
    )

anGgsnServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 104)
)
anGgsnServiceDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGgsnServiceDown.setStatus(
        "current"
    )

anApnAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 105)
)
anApnAvailable.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "apnname"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anApnAvailable.setStatus(
        "current"
    )

anApnNotAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 106)
)
anApnNotAvailable.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "apnname"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anApnNotAvailable.setStatus(
        "current"
    )

anRedundancyOperState = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 107)
)
anRedundancyOperState.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "statestring"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anRedundancyOperState.setStatus(
        "current"
    )

anCpuTosTaskState = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 108)
)
anCpuTosTaskState.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "cpu"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "statestring"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCpuTosTaskState.setStatus(
        "current"
    )

anCntnUaProfFileInvalid = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 109)
)
anCntnUaProfFileInvalid.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnUaProfFileInvalid.setStatus(
        "current"
    )

anDataFabricOperStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 110)
)
anDataFabricOperStateDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDataFabricOperStateDown.setStatus(
        "current"
    )

anNewCoreFileDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 111)
)
anNewCoreFileDetected.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "chassis"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anNewCoreFileDetected.setStatus(
        "deprecated"
    )

anfileftpfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 112)
)
anfileftpfailure.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "filepath"),
        ("AFFIRMED-ALARM-MIB", "ip"),
        ("AFFIRMED-ALARM-MIB", "port"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anfileftpfailure.setStatus(
        "current"
    )

anFmSlotFrequentReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 114)
)
anFmSlotFrequentReboot.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "chassisid"),
        ("AFFIRMED-ALARM-MIB", "cpuid"),
        ("AFFIRMED-ALARM-MIB", "slotid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anFmSlotFrequentReboot.setStatus(
        "current"
    )

anGeoRedundancyStandbyOperStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 117)
)
anGeoRedundancyStandbyOperStatusDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGeoRedundancyStandbyOperStatusDown.setStatus(
        "current"
    )

anGeoRedundancyActiveOperStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 118)
)
anGeoRedundancyActiveOperStatusDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGeoRedundancyActiveOperStatusDown.setStatus(
        "current"
    )

anForcedSyncStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 125)
)
anForcedSyncStart.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anForcedSyncStart.setStatus(
        "current"
    )

anForcedSyncFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 126)
)
anForcedSyncFailed.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anForcedSyncFailed.setStatus(
        "current"
    )

anPortStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 127)
)
anPortStatusUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "port"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPortStatusUp.setStatus(
        "deprecated"
    )

anPortStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 128)
)
anPortStatusDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "port"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPortStatusDown.setStatus(
        "deprecated"
    )

anPortStatusUP = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 129)
)
anPortStatusUP.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "port"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPortStatusUP.setStatus(
        "deprecated"
    )

anfilepurgedduetodiskfull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 130)
)
anfilepurgedduetodiskfull.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "numpurged"),
        ("AFFIRMED-ALARM-MIB", "prefix"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anfilepurgedduetodiskfull.setStatus(
        "current"
    )

anSpsServerConnectFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 131)
)
anSpsServerConnectFail.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anSpsServerConnectFail.setStatus(
        "current"
    )

anSpsServerConnectLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 132)
)
anSpsServerConnectLost.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anSpsServerConnectLost.setStatus(
        "obsolete"
    )

anGeoRedundancyPrimaryNodeStandby = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 133)
)
anGeoRedundancyPrimaryNodeStandby.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGeoRedundancyPrimaryNodeStandby.setStatus(
        "current"
    )

anGeoRedundancySecondaryNodeActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 134)
)
anGeoRedundancySecondaryNodeActive.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGeoRedundancySecondaryNodeActive.setStatus(
        "current"
    )

anKernelOptionsModified = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 135)
)
anKernelOptionsModified.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "cpu"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anKernelOptionsModified.setStatus(
        "current"
    )

anGeoRedundancyLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 136)
)
anGeoRedundancyLinkDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGeoRedundancyLinkDown.setStatus(
        "current"
    )

anGeoRedundancyLinkVersionMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 137)
)
anGeoRedundancyLinkVersionMismatch.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGeoRedundancyLinkVersionMismatch.setStatus(
        "current"
    )

anFormatDisk = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 138)
)
anFormatDisk.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "diskid"),
        ("AFFIRMED-ALARM-MIB", "node"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anFormatDisk.setStatus(
        "deprecated"
    )

anDiskFull = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 139)
)
anDiskFull.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "diskid"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDiskFull.setStatus(
        "obsolete"
    )

anCaleaPeerLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 140)
)
anCaleaPeerLinkDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "interfacename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaPeerLinkDown.setStatus(
        "current"
    )

anCaleaPeerLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 141)
)
anCaleaPeerLinkUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "interfacename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaPeerLinkUp.setStatus(
        "deprecated"
    )

anHwNodeDepartureEventData = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 142)
)
anHwNodeDepartureEventData.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anHwNodeDepartureEventData.setStatus(
        "current"
    )

anGtpPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 143)
)
anGtpPeerUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGtpPeerUp.setStatus(
        "deprecated"
    )

anDataFabricOperStateDownPathA = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 144)
)
anDataFabricOperStateDownPathA.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDataFabricOperStateDownPathA.setStatus(
        "current"
    )

anDataFabricOperStateDownPathB = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 145)
)
anDataFabricOperStateDownPathB.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDataFabricOperStateDownPathB.setStatus(
        "current"
    )

anUEPoolThresholdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 146)
)
anUEPoolThresholdAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "ipversiontype"),
        ("AFFIRMED-ALARM-MIB", "threshold"),
        ("AFFIRMED-ALARM-MIB", "uepoolutilization"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anUEPoolThresholdAlarm.setStatus(
        "current"
    )

anBaseSwitchOperStateDownPathA = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 147)
)
anBaseSwitchOperStateDownPathA.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anBaseSwitchOperStateDownPathA.setStatus(
        "current"
    )

anBaseSwitchOperStateDownPathB = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 148)
)
anBaseSwitchOperStateDownPathB.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anBaseSwitchOperStateDownPathB.setStatus(
        "current"
    )

anBaseSwitchOperStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 149)
)
anBaseSwitchOperStateDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anBaseSwitchOperStateDown.setStatus(
        "current"
    )

anNtpSyncError = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 151)
)
anNtpSyncError.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anNtpSyncError.setStatus(
        "current"
    )

an3000WarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 152)
)
an3000WarmStart.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    an3000WarmStart.setStatus(
        "current"
    )

anLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 153)
)
anLinkUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "ifadminstatus"),
        ("AFFIRMED-ALARM-MIB", "ifindex"),
        ("AFFIRMED-ALARM-MIB", "ifoperstatus"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLinkUp.setStatus(
        "current"
    )

anLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 154)
)
anLinkDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "ifadminstatus"),
        ("AFFIRMED-ALARM-MIB", "ifindex"),
        ("AFFIRMED-ALARM-MIB", "ifoperstatus"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLinkDown.setStatus(
        "current"
    )

anNmLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 155)
)
anNmLoginFailure.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anNmLoginFailure.setStatus(
        "current"
    )

anCaleaTargetsCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 162)
)
anCaleaTargetsCleared.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaTargetsCleared.setStatus(
        "current"
    )

anCaleaInterfacesCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 163)
)
anCaleaInterfacesCleared.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaInterfacesCleared.setStatus(
        "current"
    )

anCaleaUtilizationLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 164)
)
anCaleaUtilizationLow.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaUtilizationLow.setStatus(
        "current"
    )

anCaleaUtilizationMedium = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 165)
)
anCaleaUtilizationMedium.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaUtilizationMedium.setStatus(
        "current"
    )

anCaleaUtilizationHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 166)
)
anCaleaUtilizationHigh.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaUtilizationHigh.setStatus(
        "current"
    )

anCaleaUtilizationCritical = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 167)
)
anCaleaUtilizationCritical.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaUtilizationCritical.setStatus(
        "current"
    )

anBaseSwitchReachabilityDiffersPathAPathB = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 168)
)
anBaseSwitchReachabilityDiffersPathAPathB.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anBaseSwitchReachabilityDiffersPathAPathB.setStatus(
        "current"
    )

anDataFabricReachabilityDiffersPathAPathB = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 169)
)
anDataFabricReachabilityDiffersPathAPathB.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDataFabricReachabilityDiffersPathAPathB.setStatus(
        "current"
    )

anIpBgpPeerOperStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 186)
)
anIpBgpPeerOperStatusDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "currentstate"),
        ("AFFIRMED-ALARM-MIB", "lasterrorcode"),
        ("AFFIRMED-ALARM-MIB", "lasterrosubcode"),
        ("AFFIRMED-ALARM-MIB", "localpeeripaddr"),
        ("AFFIRMED-ALARM-MIB", "netctxtname"),
        ("AFFIRMED-ALARM-MIB", "peeringname"),
        ("AFFIRMED-ALARM-MIB", "remotepeeripaddr"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anIpBgpPeerOperStatusDown.setStatus(
        "current"
    )

anCaleaCCBufferConfiguredSizeBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 189)
)
anCaleaCCBufferConfiguredSizeBelowThreshold.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "groupname"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaCCBufferConfiguredSizeBelowThreshold.setStatus(
        "current"
    )

anCaleaCCBufferUtilizationThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 190)
)
anCaleaCCBufferUtilizationThresholdReached.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "groupname"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaCCBufferUtilizationThresholdReached.setStatus(
        "current"
    )

anCaleaIRIBufferUtilizationThresholdReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 191)
)
anCaleaIRIBufferUtilizationThresholdReached.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "groupname"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaIRIBufferUtilizationThresholdReached.setStatus(
        "current"
    )

anCaleaTargetDBMaxSubsLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 192)
)
anCaleaTargetDBMaxSubsLimitReached.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaTargetDBMaxSubsLimitReached.setStatus(
        "current"
    )

anCaleaIRIBufferConfiguredSizeBelowThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 193)
)
anCaleaIRIBufferConfiguredSizeBelowThreshold.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "groupname"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaIRIBufferConfiguredSizeBelowThreshold.setStatus(
        "current"
    )

anCaleaIfOrIfGroupConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 194)
)
anCaleaIfOrIfGroupConfigChange.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaIfOrIfGroupConfigChange.setStatus(
        "current"
    )

anCaleaLITargetCreatedOrDeleted = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 195)
)
anCaleaLITargetCreatedOrDeleted.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaLITargetCreatedOrDeleted.setStatus(
        "current"
    )

anCaleaInterfaceGroupStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 196)
)
anCaleaInterfaceGroupStatusDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "groupname"),
        ("AFFIRMED-ALARM-MIB", "role"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaInterfaceGroupStatusDown.setStatus(
        "current"
    )

anCaleaCCBufferDataLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 197)
)
anCaleaCCBufferDataLost.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "groupname"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaCCBufferDataLost.setStatus(
        "current"
    )

anCaleaIRIBufferDataLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 198)
)
anCaleaIRIBufferDataLost.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "groupname"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaIRIBufferDataLost.setStatus(
        "current"
    )

anHwExtStorageCreateFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 199)
)
anHwExtStorageCreateFailure.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "operation"),
        ("AFFIRMED-ALARM-MIB", "state"),
        ("AFFIRMED-ALARM-MIB", "status"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anHwExtStorageCreateFailure.setStatus(
        "current"
    )

anHwExtStorageSizeMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 200)
)
anHwExtStorageSizeMismatch.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "activesize"),
        ("AFFIRMED-ALARM-MIB", "standbysize"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anHwExtStorageSizeMismatch.setStatus(
        "current"
    )

anHwNoExtStorageDiskAvailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 201)
)
anHwNoExtStorageDiskAvailable.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "mcmslotnumber"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anHwNoExtStorageDiskAvailable.setStatus(
        "current"
    )

anHwNotEnoughFreeStorageSpace = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 202)
)
anHwNotEnoughFreeStorageSpace.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "availablesize"),
        ("AFFIRMED-ALARM-MIB", "requiredsize"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anHwNotEnoughFreeStorageSpace.setStatus(
        "current"
    )

anHwExtStorageMoveFilesTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 203)
)
anHwExtStorageMoveFilesTimeout.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "operation"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anHwExtStorageMoveFilesTimeout.setStatus(
        "current"
    )

anHwExtStorageCloseFilesTimeout = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 204)
)
anHwExtStorageCloseFilesTimeout.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "operation"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anHwExtStorageCloseFilesTimeout.setStatus(
        "current"
    )

anDataRecordFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 205)
)
anDataRecordFailure.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDataRecordFailure.setStatus(
        "current"
    )

anPacketEngineError = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 206)
)
anPacketEngineError.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPacketEngineError.setStatus(
        "current"
    )

anPacketEngineCongestion = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 207)
)
anPacketEngineCongestion.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPacketEngineCongestion.setStatus(
        "current"
    )

anExtractionPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 208)
)
anExtractionPending.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anExtractionPending.setStatus(
        "current"
    )

anInsertionPending = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 209)
)
anInsertionPending.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "resource"),
        ("AFFIRMED-ALARM-MIB", "slot"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anInsertionPending.setStatus(
        "current"
    )

anDataFabricPartialReachabilityPathA = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 210)
)
anDataFabricPartialReachabilityPathA.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDataFabricPartialReachabilityPathA.setStatus(
        "current"
    )

anRemoteMountFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 211)
)
anRemoteMountFailed.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anRemoteMountFailed.setStatus(
        "current"
    )

anEmergencyCallAttemptFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 214)
)
anEmergencyCallAttemptFailed.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "reason"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anEmergencyCallAttemptFailed.setStatus(
        "current"
    )

anEmergencyCallDropped = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 215)
)
anEmergencyCallDropped.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "reason"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anEmergencyCallDropped.setStatus(
        "current"
    )

anCntnOnlineCatDBInstallationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 218)
)
anCntnOnlineCatDBInstallationFailure.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "importnum"),
        ("AFFIRMED-ALARM-MIB", "resultstr"),
        ("AFFIRMED-ALARM-MIB", "slotid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnOnlineCatDBInstallationFailure.setStatus(
        "current"
    )

anWagServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 220)
)
anWagServiceDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anWagServiceDown.setStatus(
        "current"
    )

anWagServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 221)
)
anWagServiceUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anWagServiceUp.setStatus(
        "current"
    )

anEdrServerConnectionFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 222)
)
anEdrServerConnectionFailed.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "ip"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "port"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anEdrServerConnectionFailed.setStatus(
        "current"
    )

anLicenseCapacityEnforcement = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 223)
)
anLicenseCapacityEnforcement.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLicenseCapacityEnforcement.setStatus(
        "current"
    )

anLicenseCapacityLimit = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 224)
)
anLicenseCapacityLimit.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLicenseCapacityLimit.setStatus(
        "current"
    )

anLicenseLifetimeEnforcement = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 225)
)
anLicenseLifetimeEnforcement.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLicenseLifetimeEnforcement.setStatus(
        "current"
    )

anLicenseLifetime = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 226)
)
anLicenseLifetime.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLicenseLifetime.setStatus(
        "current"
    )

anLicensePlsSeparation = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 227)
)
anLicensePlsSeparation.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLicensePlsSeparation.setStatus(
        "current"
    )

anLicensePlsGraceExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 228)
)
anLicensePlsGraceExpired.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anLicensePlsGraceExpired.setStatus(
        "current"
    )

anEpdgServiceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 230)
)
anEpdgServiceUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anEpdgServiceUp.setStatus(
        "current"
    )

anEpdgServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 231)
)
anEpdgServiceDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "servicename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anEpdgServiceDown.setStatus(
        "current"
    )

anPkix509expiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 232)
)
anPkix509expiring.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkix509expiring.setStatus(
        "current"
    )

anPkix509expired = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 233)
)
anPkix509expired.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkix509expired.setStatus(
        "current"
    )

anPkix509revoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 234)
)
anPkix509revoked.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkix509revoked.setStatus(
        "current"
    )

anPkiobjunreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 235)
)
anPkiobjunreachable.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkiobjunreachable.setStatus(
        "current"
    )

anPkiobjadded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 236)
)
anPkiobjadded.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkiobjadded.setStatus(
        "current"
    )

anPkiobjupdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 237)
)
anPkiobjupdated.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkiobjupdated.setStatus(
        "current"
    )

anPkiobjremoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 238)
)
anPkiobjremoved.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkiobjremoved.setStatus(
        "current"
    )

anPacketEngineWatchdogAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 239)
)
anPacketEngineWatchdogAlarm.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "info"),
        ("AFFIRMED-ALARM-MIB", "sid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPacketEngineWatchdogAlarm.setStatus(
        "current"
    )

anPkix509crlnextupdateavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 240)
)
anPkix509crlnextupdateavailable.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkix509crlnextupdateavailable.setStatus(
        "current"
    )

anPacketEngineKNIConfigurationMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 241)
)
anPacketEngineKNIConfigurationMismatch.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPacketEngineKNIConfigurationMismatch.setStatus(
        "current"
    )

anIsolCpusMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 242)
)
anIsolCpusMismatch.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anIsolCpusMismatch.setStatus(
        "current"
    )

anReleaseMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 244)
)
anReleaseMismatch.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anReleaseMismatch.setStatus(
        "current"
    )

anIpsecTunnelOperStatusDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 246)
)
anIpsecTunnelOperStatusDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "unused"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anIpsecTunnelOperStatusDown.setStatus(
        "current"
    )

anIpsecTunnelOperStatusUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 247)
)
anIpsecTunnelOperStatusUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "unused"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anIpsecTunnelOperStatusUp.setStatus(
        "current"
    )

anPkiobjupdatenotavailable = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 248)
)
anPkiobjupdatenotavailable.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkiobjupdatenotavailable.setStatus(
        "current"
    )

anPkisshauthorizedkeyaddedtouser = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 249)
)
anPkisshauthorizedkeyaddedtouser.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshauthorizedkeyaddedtouser.setStatus(
        "current"
    )

anPkisshauthorizedkeyremovedfromuser = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 250)
)
anPkisshauthorizedkeyremovedfromuser.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshauthorizedkeyremovedfromuser.setStatus(
        "current"
    )

anPkisshauthorizedkeyaddedtogroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 251)
)
anPkisshauthorizedkeyaddedtogroup.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshauthorizedkeyaddedtogroup.setStatus(
        "current"
    )

anPkisshauthorizedkeyremovedfromgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 252)
)
anPkisshauthorizedkeyremovedfromgroup.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshauthorizedkeyremovedfromgroup.setStatus(
        "current"
    )

anPkisshtrustedcakeyaddedtocluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 253)
)
anPkisshtrustedcakeyaddedtocluster.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshtrustedcakeyaddedtocluster.setStatus(
        "current"
    )

anPkisshtrustedcakeyremovedfromcluster = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 254)
)
anPkisshtrustedcakeyremovedfromcluster.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshtrustedcakeyremovedfromcluster.setStatus(
        "current"
    )

anPkisshtrustedcakeyaddedtogroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 255)
)
anPkisshtrustedcakeyaddedtogroup.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshtrustedcakeyaddedtogroup.setStatus(
        "current"
    )

anPkisshtrustedcakeyremovedfromgroup = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 256)
)
anPkisshtrustedcakeyremovedfromgroup.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshtrustedcakeyremovedfromgroup.setStatus(
        "current"
    )

anPkisshuseraddedtoauthorizedprincipals = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 257)
)
anPkisshuseraddedtoauthorizedprincipals.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshuseraddedtoauthorizedprincipals.setStatus(
        "deprecated"
    )

anPkisshuserremovedfromauthorizedprincipals = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 258)
)
anPkisshuserremovedfromauthorizedprincipals.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshuserremovedfromauthorizedprincipals.setStatus(
        "deprecated"
    )

anPkisshgroupaddedtoauthorizedprincipals = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 259)
)
anPkisshgroupaddedtoauthorizedprincipals.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshgroupaddedtoauthorizedprincipals.setStatus(
        "deprecated"
    )

anPkisshgroupremovedfromauthorizedprincipals = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 260)
)
anPkisshgroupremovedfromauthorizedprincipals.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshgroupremovedfromauthorizedprincipals.setStatus(
        "deprecated"
    )

anfileexportfailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 261)
)
anfileexportfailure.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "filepath"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anfileexportfailure.setStatus(
        "current"
    )

anPkisshnamesaddedtogroupauthorizedprincipals = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 262)
)
anPkisshnamesaddedtogroupauthorizedprincipals.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshnamesaddedtogroupauthorizedprincipals.setStatus(
        "current"
    )

anPkissherrorapplyingconfigurationtosshcontrolfiles = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 263)
)
anPkissherrorapplyingconfigurationtosshcontrolfiles.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkissherrorapplyingconfigurationtosshcontrolfiles.setStatus(
        "current"
    )

anPkisshnamesremovedfromauthorizedprincipals = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 264)
)
anPkisshnamesremovedfromauthorizedprincipals.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshnamesremovedfromauthorizedprincipals.setStatus(
        "current"
    )

anPkisshnamesaddedtoauthorizedprincipals = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 265)
)
anPkisshnamesaddedtoauthorizedprincipals.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshnamesaddedtoauthorizedprincipals.setStatus(
        "current"
    )

anPkisshnamesremovedfromgroupauthorizedprincipals = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 266)
)
anPkisshnamesremovedfromgroupauthorizedprincipals.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshnamesremovedfromgroupauthorizedprincipals.setStatus(
        "current"
    )

anPkisshmaximumsecuritylevelset = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 267)
)
anPkisshmaximumsecuritylevelset.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshmaximumsecuritylevelset.setStatus(
        "current"
    )

anPkisshcompatiblesecuritylevelset = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 268)
)
anPkisshcompatiblesecuritylevelset.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshcompatiblesecuritylevelset.setStatus(
        "current"
    )

anPkisshstricthostkeycheckingsettono = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 269)
)
anPkisshstricthostkeycheckingsettono.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshstricthostkeycheckingsettono.setStatus(
        "current"
    )

anPkisshstricthostkeycheckingsettoask = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 270)
)
anPkisshstricthostkeycheckingsettoask.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshstricthostkeycheckingsettoask.setStatus(
        "current"
    )

anPkisshstricthostkeycheckingsettoyes = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 271)
)
anPkisshstricthostkeycheckingsettoyes.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshstricthostkeycheckingsettoyes.setStatus(
        "current"
    )

anPkisshverifyhostkeydnssettono = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 272)
)
anPkisshverifyhostkeydnssettono.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshverifyhostkeydnssettono.setStatus(
        "current"
    )

anPkisshverifyhostkeydnssettoyes = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 273)
)
anPkisshverifyhostkeydnssettoyes.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshverifyhostkeydnssettoyes.setStatus(
        "current"
    )

anPkisshverifyhostkeydnssettoask = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 274)
)
anPkisshverifyhostkeydnssettoask.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshverifyhostkeydnssettoask.setStatus(
        "current"
    )

anPkisshknownhostcakeyremoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 275)
)
anPkisshknownhostcakeyremoved.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshknownhostcakeyremoved.setStatus(
        "current"
    )

anPkisshknownhostcakeyadded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 276)
)
anPkisshknownhostcakeyadded.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshknownhostcakeyadded.setStatus(
        "current"
    )

anPkisshknownhostkeyremoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 277)
)
anPkisshknownhostkeyremoved.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshknownhostkeyremoved.setStatus(
        "current"
    )

anPkisshknownhostkeyadded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 278)
)
anPkisshknownhostkeyadded.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshknownhostkeyadded.setStatus(
        "current"
    )

anPkisshlocalhostcertificatereplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 279)
)
anPkisshlocalhostcertificatereplaced.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshlocalhostcertificatereplaced.setStatus(
        "current"
    )

anPkisshlocalhostcertificateremoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 280)
)
anPkisshlocalhostcertificateremoved.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshlocalhostcertificateremoved.setStatus(
        "current"
    )

anPkisshlocalhostcertificateadded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 281)
)
anPkisshlocalhostcertificateadded.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshlocalhostcertificateadded.setStatus(
        "current"
    )

anPkisshrevoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 282)
)
anPkisshrevoked.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshrevoked.setStatus(
        "current"
    )

anPkimanuallyrevoked = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 283)
)
anPkimanuallyrevoked.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkimanuallyrevoked.setStatus(
        "current"
    )

anPkisshuserkrlreplaced = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 285)
)
anPkisshuserkrlreplaced.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshuserkrlreplaced.setStatus(
        "current"
    )

anPkisshuserkrladded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 286)
)
anPkisshuserkrladded.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshuserkrladded.setStatus(
        "current"
    )

anPkisshuserkrlremoved = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 287)
)
anPkisshuserkrlremoved.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshuserkrlremoved.setStatus(
        "current"
    )

anPkisshcertexpiring = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 288)
)
anPkisshcertexpiring.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshcertexpiring.setStatus(
        "current"
    )

anPkisshcertexpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 289)
)
anPkisshcertexpired.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPkisshcertexpired.setStatus(
        "current"
    )

anCntnFilterHashListFileInvalidEntry = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 291)
)
anCntnFilterHashListFileInvalidEntry.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnFilterHashListFileInvalidEntry.setStatus(
        "current"
    )

anCntnFilterHashListFileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 292)
)
anCntnFilterHashListFileNotFound.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnFilterHashListFileNotFound.setStatus(
        "current"
    )

anCntnFilterHashListFileOverflow = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 293)
)
anCntnFilterHashListFileOverflow.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnFilterHashListFileOverflow.setStatus(
        "current"
    )

anCntnFilterHashListFileTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 294)
)
anCntnFilterHashListFileTooBig.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnFilterHashListFileTooBig.setStatus(
        "current"
    )

anGwSubsGrpFileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 296)
)
anGwSubsGrpFileNotFound.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "subsgroupname"),
        ("AFFIRMED-ALARM-MIB", "subsidfilename"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anGwSubsGrpFileNotFound.setStatus(
        "current"
    )

anNewMemImageFileDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 298)
)
anNewMemImageFileDetected.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "chassis"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anNewMemImageFileDetected.setStatus(
        "deprecated"
    )

anCaleaUserBanFeatureConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 299)
)
anCaleaUserBanFeatureConfigChange.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "state"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaUserBanFeatureConfigChange.setStatus(
        "current"
    )

anCaleaCCDataLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 300)
)
anCaleaCCDataLost.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "ifname"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaCCDataLost.setStatus(
        "current"
    )

anCaleaIRIDataLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 301)
)
anCaleaIRIDataLost.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "ifname"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaIRIDataLost.setStatus(
        "current"
    )

anIpOspfv2NbrDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 302)
)
anIpOspfv2NbrDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "unused"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anIpOspfv2NbrDown.setStatus(
        "current"
    )

anIpOspfv3NbrDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 303)
)
anIpOspfv3NbrDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "unused"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anIpOspfv3NbrDown.setStatus(
        "current"
    )

anNatPoolSessionAlarmThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 304)
)
anNatPoolSessionAlarmThreshold.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "sessionthreshold"),
        ("AFFIRMED-ALARM-MIB", "sessionutilization"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anNatPoolSessionAlarmThreshold.setStatus(
        "current"
    )

anNatPoolIpAddressAlarmThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 305)
)
anNatPoolIpAddressAlarmThreshold.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "ipaddressthreshold"),
        ("AFFIRMED-ALARM-MIB", "ipaddressutilization"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anNatPoolIpAddressAlarmThreshold.setStatus(
        "current"
    )

anNatPoolPortChunkAlarmThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 306)
)
anNatPoolPortChunkAlarmThreshold.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "portchunkthreshold"),
        ("AFFIRMED-ALARM-MIB", "portchunkutilization"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anNatPoolPortChunkAlarmThreshold.setStatus(
        "current"
    )

anNewFaultFileDetected = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 309)
)
anNewFaultFileDetected.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "chassis"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anNewFaultFileDetected.setStatus(
        "current"
    )

anCntnHealthCheckStateDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 320)
)
anCntnHealthCheckStateDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "destination"),
        ("AFFIRMED-ALARM-MIB", "parent"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnHealthCheckStateDown.setStatus(
        "current"
    )

anPfcpPeerDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 321)
)
anPfcpPeerDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "gatewayipaddress"),
        ("AFFIRMED-ALARM-MIB", "gatewayname"),
        ("AFFIRMED-ALARM-MIB", "peeripaddress"),
        ("AFFIRMED-ALARM-MIB", "peername"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPfcpPeerDown.setStatus(
        "current"
    )

anPfcpPeerUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 322)
)
anPfcpPeerUp.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "gatewayipaddress"),
        ("AFFIRMED-ALARM-MIB", "gatewayname"),
        ("AFFIRMED-ALARM-MIB", "peeripaddress"),
        ("AFFIRMED-ALARM-MIB", "peername"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPfcpPeerUp.setStatus(
        "deprecated"
    )

anCaleaIfGrpSourceProfileConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 323)
)
anCaleaIfGrpSourceProfileConfigChange.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaIfGrpSourceProfileConfigChange.setStatus(
        "current"
    )

anCaleaIfGrpSourceProfileNotFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 324)
)
anCaleaIfGrpSourceProfileNotFound.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaIfGrpSourceProfileNotFound.setStatus(
        "current"
    )

anBfdSessionDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 329)
)
anBfdSessionDown.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "bfdsessiondescription"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anBfdSessionDown.setStatus(
        "current"
    )

anNodeRebootRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 332)
)
anNodeRebootRequired.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anNodeRebootRequired.setStatus(
        "current"
    )

anPortmapFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 333)
)
anPortmapFailure.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "failuredescription"),
        ("AFFIRMED-ALARM-MIB", "slotnumber"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anPortmapFailure.setStatus(
        "current"
    )

anRadiusAccountingOnMsgNotSent = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 334)
)
anRadiusAccountingOnMsgNotSent.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anRadiusAccountingOnMsgNotSent.setStatus(
        "current"
    )

anCntnCACertExpired = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 335)
)
anCntnCACertExpired.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cafilename"),
        ("AFFIRMED-ALARM-MIB", "expirydate"),
        ("AFFIRMED-ALARM-MIB", "index"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCntnCACertExpired.setStatus(
        "current"
    )

anClusterRebootRequired = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 338)
)
anClusterRebootRequired.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "cid"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anClusterRebootRequired.setStatus(
        "current"
    )

anCaleaPdhirNotSupportedForSx3lifTunnelToCPF = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 342)
)
anCaleaPdhirNotSupportedForSx3lifTunnelToCPF.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaPdhirNotSupportedForSx3lifTunnelToCPF.setStatus(
        "current"
    )

anCaleaDecryptFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 343)
)
anCaleaDecryptFail.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anCaleaDecryptFail.setStatus(
        "current"
    )

anDnsServerConfigLoadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 348)
)
anDnsServerConfigLoadFail.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDnsServerConfigLoadFail.setStatus(
        "current"
    )

anDnsServerRecClientHardLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 349)
)
anDnsServerRecClientHardLimitExceeded.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDnsServerRecClientHardLimitExceeded.setStatus(
        "current"
    )

anDnsServerRecClientSoftLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 350)
)
anDnsServerRecClientSoftLimitExceeded.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDnsServerRecClientSoftLimitExceeded.setStatus(
        "current"
    )

anDnsServerZoneLoadFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 351)
)
anDnsServerZoneLoadFail.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anDnsServerZoneLoadFail.setStatus(
        "current"
    )

anTaskTermination = NotificationType(
    (1, 3, 6, 1, 4, 1, 37963, 4, 0, 4, 3, 0, 354)
)
anTaskTermination.setObjects(
      *(("AFFIRMED-ALARM-MIB", "affirmedAlarmSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDateTime"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmChassisName"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSourceId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmSeverity"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmRefSeqId"),
        ("AFFIRMED-ALARM-MIB", "affirmedAlarmDetails"),
        ("AFFIRMED-ALARM-MIB", "affirmedPotentialImpact"),
        ("AFFIRMED-ALARM-MIB", "affirmedCorrectiveAction"),
        ("AFFIRMED-ALARM-MIB", "name"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceIpAddress"),
        ("AFFIRMED-ALARM-MIB", "affirmedVmSourceName"))
)
if mibBuilder.loadTexts:
    anTaskTermination.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AFFIRMED-SNMP-AN3000-TRAPS-MIB",
    **{"affirmedSnmpAn3000Traps": affirmedSnmpAn3000Traps,
       "affirmedSnmpAn3000TrapsScalars": affirmedSnmpAn3000TrapsScalars,
       "affirmedSnmpAn3000TrapsTables": affirmedSnmpAn3000TrapsTables,
       "affirmedSnmpAn3000TrapsNotifications": affirmedSnmpAn3000TrapsNotifications,
       "affirmedSnmpAn3000TrapsNotificationPrefix": affirmedSnmpAn3000TrapsNotificationPrefix,
       "fmSWCompMCMSwitchoverEventData": fmSWCompMCMSwitchoverEventData,
       "fmNmAn3000ColdStart": fmNmAn3000ColdStart,
       "fmNmAn3000Test": fmNmAn3000Test,
       "fmNmAn3000Commit": fmNmAn3000Commit,
       "fmHmCacheOperStateDown": fmHmCacheOperStateDown,
       "anTemperatureAlarm": anTemperatureAlarm,
       "anVoltageAlarm": anVoltageAlarm,
       "anHotSwapAlarm": anHotSwapAlarm,
       "anTelcoAlarm": anTelcoAlarm,
       "anWatchdogAlarm": anWatchdogAlarm,
       "anFanAlarm": anFanAlarm,
       "anAirFilterAlarm": anAirFilterAlarm,
       "anTachAlarm": anTachAlarm,
       "anHWAlarm": anHWAlarm,
       "fmCntnFilterCategoryFileTooBig": fmCntnFilterCategoryFileTooBig,
       "fmCntnFilterCategoryFileNotFound": fmCntnFilterCategoryFileNotFound,
       "fmCntnFilterCategoryFileOverflow": fmCntnFilterCategoryFileOverflow,
       "fmCntnFilterBlacklistFileOverflow": fmCntnFilterBlacklistFileOverflow,
       "fmCntnFilterBlacklistFileTooBig": fmCntnFilterBlacklistFileTooBig,
       "fmCntnFilterBlacklistFileNotFound": fmCntnFilterBlacklistFileNotFound,
       "anCardNotBootingUp": anCardNotBootingUp,
       "fmCntnFilterCategoryFileInvalidEntry": fmCntnFilterCategoryFileInvalidEntry,
       "fmCntnFilterBlacklistFileInvalidEntry": fmCntnFilterBlacklistFileInvalidEntry,
       "fmCntnHttpProxyServerConnectFail": fmCntnHttpProxyServerConnectFail,
       "anCntnFilterWhitelistFileInvalidEntry": anCntnFilterWhitelistFileInvalidEntry,
       "anCntnFilterWhitelistFileOverflow": anCntnFilterWhitelistFileOverflow,
       "anCntnFilterWhitelistFileTooBig": anCntnFilterWhitelistFileTooBig,
       "anCntnFilterWhitelistFileNotFound": anCntnFilterWhitelistFileNotFound,
       "anGtpPeerDown": anGtpPeerDown,
       "anCacheDiskOperationalStateAlarm": anCacheDiskOperationalStateAlarm,
       "anCntnUrlListFileInvalidEntry": anCntnUrlListFileInvalidEntry,
       "anCntnUrlListFileOverflow": anCntnUrlListFileOverflow,
       "anCntnUrlListFileNotFound": anCntnUrlListFileNotFound,
       "anCntnUrlListFileTooBig": anCntnUrlListFileTooBig,
       "anPlaFileDownloadFail": anPlaFileDownloadFail,
       "anThresholdCrossingAlarm": anThresholdCrossingAlarm,
       "anTaskOverload": anTaskOverload,
       "anBladeOverload": anBladeOverload,
       "anSystemOverload": anSystemOverload,
       "anCantPageSubscriberOutOfBuffers": anCantPageSubscriberOutOfBuffers,
       "anLedStateChange": anLedStateChange,
       "anRebootEvent": anRebootEvent,
       "anCacheDiskErrorStateAlarm": anCacheDiskErrorStateAlarm,
       "anPayloadFailure": anPayloadFailure,
       "anLDAPServerConnectFail": anLDAPServerConnectFail,
       "anLDAPServerConnectLost": anLDAPServerConnectLost,
       "anLDAPProfNoServerConnected": anLDAPProfNoServerConnected,
       "anCntnUaProfDefaultAttsMissing": anCntnUaProfDefaultAttsMissing,
       "anIpInterfaceOperStatusDown": anIpInterfaceOperStatusDown,
       "anDiameterPeerLinkDown": anDiameterPeerLinkDown,
       "anDiameterPeerLinkUp": anDiameterPeerLinkUp,
       "anRadiusPeerDown": anRadiusPeerDown,
       "anRadiusPeerUp": anRadiusPeerUp,
       "anGtppPeerDown": anGtppPeerDown,
       "anGtppPeerUp": anGtppPeerUp,
       "anSMSCServerConnectFail": anSMSCServerConnectFail,
       "anSMSCProfNotFound": anSMSCProfNotFound,
       "anSMSCServerConnectLost": anSMSCServerConnectLost,
       "anPdnSessionAntiSpoofing": anPdnSessionAntiSpoofing,
       "anSgwServiceUp": anSgwServiceUp,
       "anSgwServiceDown": anSgwServiceDown,
       "anPgwServiceUp": anPgwServiceUp,
       "anPgwServiceDown": anPgwServiceDown,
       "anGgsnServiceUp": anGgsnServiceUp,
       "anGgsnServiceDown": anGgsnServiceDown,
       "anApnAvailable": anApnAvailable,
       "anApnNotAvailable": anApnNotAvailable,
       "anRedundancyOperState": anRedundancyOperState,
       "anCpuTosTaskState": anCpuTosTaskState,
       "anCntnUaProfFileInvalid": anCntnUaProfFileInvalid,
       "anDataFabricOperStateDown": anDataFabricOperStateDown,
       "anNewCoreFileDetected": anNewCoreFileDetected,
       "anfileftpfailure": anfileftpfailure,
       "anFmSlotFrequentReboot": anFmSlotFrequentReboot,
       "anGeoRedundancyStandbyOperStatusDown": anGeoRedundancyStandbyOperStatusDown,
       "anGeoRedundancyActiveOperStatusDown": anGeoRedundancyActiveOperStatusDown,
       "anForcedSyncStart": anForcedSyncStart,
       "anForcedSyncFailed": anForcedSyncFailed,
       "anPortStatusUp": anPortStatusUp,
       "anPortStatusDown": anPortStatusDown,
       "anPortStatusUP": anPortStatusUP,
       "anfilepurgedduetodiskfull": anfilepurgedduetodiskfull,
       "anSpsServerConnectFail": anSpsServerConnectFail,
       "anSpsServerConnectLost": anSpsServerConnectLost,
       "anGeoRedundancyPrimaryNodeStandby": anGeoRedundancyPrimaryNodeStandby,
       "anGeoRedundancySecondaryNodeActive": anGeoRedundancySecondaryNodeActive,
       "anKernelOptionsModified": anKernelOptionsModified,
       "anGeoRedundancyLinkDown": anGeoRedundancyLinkDown,
       "anGeoRedundancyLinkVersionMismatch": anGeoRedundancyLinkVersionMismatch,
       "anFormatDisk": anFormatDisk,
       "anDiskFull": anDiskFull,
       "anCaleaPeerLinkDown": anCaleaPeerLinkDown,
       "anCaleaPeerLinkUp": anCaleaPeerLinkUp,
       "anHwNodeDepartureEventData": anHwNodeDepartureEventData,
       "anGtpPeerUp": anGtpPeerUp,
       "anDataFabricOperStateDownPathA": anDataFabricOperStateDownPathA,
       "anDataFabricOperStateDownPathB": anDataFabricOperStateDownPathB,
       "anUEPoolThresholdAlarm": anUEPoolThresholdAlarm,
       "anBaseSwitchOperStateDownPathA": anBaseSwitchOperStateDownPathA,
       "anBaseSwitchOperStateDownPathB": anBaseSwitchOperStateDownPathB,
       "anBaseSwitchOperStateDown": anBaseSwitchOperStateDown,
       "anNtpSyncError": anNtpSyncError,
       "an3000WarmStart": an3000WarmStart,
       "anLinkUp": anLinkUp,
       "anLinkDown": anLinkDown,
       "anNmLoginFailure": anNmLoginFailure,
       "anCaleaTargetsCleared": anCaleaTargetsCleared,
       "anCaleaInterfacesCleared": anCaleaInterfacesCleared,
       "anCaleaUtilizationLow": anCaleaUtilizationLow,
       "anCaleaUtilizationMedium": anCaleaUtilizationMedium,
       "anCaleaUtilizationHigh": anCaleaUtilizationHigh,
       "anCaleaUtilizationCritical": anCaleaUtilizationCritical,
       "anBaseSwitchReachabilityDiffersPathAPathB": anBaseSwitchReachabilityDiffersPathAPathB,
       "anDataFabricReachabilityDiffersPathAPathB": anDataFabricReachabilityDiffersPathAPathB,
       "anIpBgpPeerOperStatusDown": anIpBgpPeerOperStatusDown,
       "anCaleaCCBufferConfiguredSizeBelowThreshold": anCaleaCCBufferConfiguredSizeBelowThreshold,
       "anCaleaCCBufferUtilizationThresholdReached": anCaleaCCBufferUtilizationThresholdReached,
       "anCaleaIRIBufferUtilizationThresholdReached": anCaleaIRIBufferUtilizationThresholdReached,
       "anCaleaTargetDBMaxSubsLimitReached": anCaleaTargetDBMaxSubsLimitReached,
       "anCaleaIRIBufferConfiguredSizeBelowThreshold": anCaleaIRIBufferConfiguredSizeBelowThreshold,
       "anCaleaIfOrIfGroupConfigChange": anCaleaIfOrIfGroupConfigChange,
       "anCaleaLITargetCreatedOrDeleted": anCaleaLITargetCreatedOrDeleted,
       "anCaleaInterfaceGroupStatusDown": anCaleaInterfaceGroupStatusDown,
       "anCaleaCCBufferDataLost": anCaleaCCBufferDataLost,
       "anCaleaIRIBufferDataLost": anCaleaIRIBufferDataLost,
       "anHwExtStorageCreateFailure": anHwExtStorageCreateFailure,
       "anHwExtStorageSizeMismatch": anHwExtStorageSizeMismatch,
       "anHwNoExtStorageDiskAvailable": anHwNoExtStorageDiskAvailable,
       "anHwNotEnoughFreeStorageSpace": anHwNotEnoughFreeStorageSpace,
       "anHwExtStorageMoveFilesTimeout": anHwExtStorageMoveFilesTimeout,
       "anHwExtStorageCloseFilesTimeout": anHwExtStorageCloseFilesTimeout,
       "anDataRecordFailure": anDataRecordFailure,
       "anPacketEngineError": anPacketEngineError,
       "anPacketEngineCongestion": anPacketEngineCongestion,
       "anExtractionPending": anExtractionPending,
       "anInsertionPending": anInsertionPending,
       "anDataFabricPartialReachabilityPathA": anDataFabricPartialReachabilityPathA,
       "anRemoteMountFailed": anRemoteMountFailed,
       "anEmergencyCallAttemptFailed": anEmergencyCallAttemptFailed,
       "anEmergencyCallDropped": anEmergencyCallDropped,
       "anCntnOnlineCatDBInstallationFailure": anCntnOnlineCatDBInstallationFailure,
       "anWagServiceDown": anWagServiceDown,
       "anWagServiceUp": anWagServiceUp,
       "anEdrServerConnectionFailed": anEdrServerConnectionFailed,
       "anLicenseCapacityEnforcement": anLicenseCapacityEnforcement,
       "anLicenseCapacityLimit": anLicenseCapacityLimit,
       "anLicenseLifetimeEnforcement": anLicenseLifetimeEnforcement,
       "anLicenseLifetime": anLicenseLifetime,
       "anLicensePlsSeparation": anLicensePlsSeparation,
       "anLicensePlsGraceExpired": anLicensePlsGraceExpired,
       "anEpdgServiceUp": anEpdgServiceUp,
       "anEpdgServiceDown": anEpdgServiceDown,
       "anPkix509expiring": anPkix509expiring,
       "anPkix509expired": anPkix509expired,
       "anPkix509revoked": anPkix509revoked,
       "anPkiobjunreachable": anPkiobjunreachable,
       "anPkiobjadded": anPkiobjadded,
       "anPkiobjupdated": anPkiobjupdated,
       "anPkiobjremoved": anPkiobjremoved,
       "anPacketEngineWatchdogAlarm": anPacketEngineWatchdogAlarm,
       "anPkix509crlnextupdateavailable": anPkix509crlnextupdateavailable,
       "anPacketEngineKNIConfigurationMismatch": anPacketEngineKNIConfigurationMismatch,
       "anIsolCpusMismatch": anIsolCpusMismatch,
       "anReleaseMismatch": anReleaseMismatch,
       "anIpsecTunnelOperStatusDown": anIpsecTunnelOperStatusDown,
       "anIpsecTunnelOperStatusUp": anIpsecTunnelOperStatusUp,
       "anPkiobjupdatenotavailable": anPkiobjupdatenotavailable,
       "anPkisshauthorizedkeyaddedtouser": anPkisshauthorizedkeyaddedtouser,
       "anPkisshauthorizedkeyremovedfromuser": anPkisshauthorizedkeyremovedfromuser,
       "anPkisshauthorizedkeyaddedtogroup": anPkisshauthorizedkeyaddedtogroup,
       "anPkisshauthorizedkeyremovedfromgroup": anPkisshauthorizedkeyremovedfromgroup,
       "anPkisshtrustedcakeyaddedtocluster": anPkisshtrustedcakeyaddedtocluster,
       "anPkisshtrustedcakeyremovedfromcluster": anPkisshtrustedcakeyremovedfromcluster,
       "anPkisshtrustedcakeyaddedtogroup": anPkisshtrustedcakeyaddedtogroup,
       "anPkisshtrustedcakeyremovedfromgroup": anPkisshtrustedcakeyremovedfromgroup,
       "anPkisshuseraddedtoauthorizedprincipals": anPkisshuseraddedtoauthorizedprincipals,
       "anPkisshuserremovedfromauthorizedprincipals": anPkisshuserremovedfromauthorizedprincipals,
       "anPkisshgroupaddedtoauthorizedprincipals": anPkisshgroupaddedtoauthorizedprincipals,
       "anPkisshgroupremovedfromauthorizedprincipals": anPkisshgroupremovedfromauthorizedprincipals,
       "anfileexportfailure": anfileexportfailure,
       "anPkisshnamesaddedtogroupauthorizedprincipals": anPkisshnamesaddedtogroupauthorizedprincipals,
       "anPkissherrorapplyingconfigurationtosshcontrolfiles": anPkissherrorapplyingconfigurationtosshcontrolfiles,
       "anPkisshnamesremovedfromauthorizedprincipals": anPkisshnamesremovedfromauthorizedprincipals,
       "anPkisshnamesaddedtoauthorizedprincipals": anPkisshnamesaddedtoauthorizedprincipals,
       "anPkisshnamesremovedfromgroupauthorizedprincipals": anPkisshnamesremovedfromgroupauthorizedprincipals,
       "anPkisshmaximumsecuritylevelset": anPkisshmaximumsecuritylevelset,
       "anPkisshcompatiblesecuritylevelset": anPkisshcompatiblesecuritylevelset,
       "anPkisshstricthostkeycheckingsettono": anPkisshstricthostkeycheckingsettono,
       "anPkisshstricthostkeycheckingsettoask": anPkisshstricthostkeycheckingsettoask,
       "anPkisshstricthostkeycheckingsettoyes": anPkisshstricthostkeycheckingsettoyes,
       "anPkisshverifyhostkeydnssettono": anPkisshverifyhostkeydnssettono,
       "anPkisshverifyhostkeydnssettoyes": anPkisshverifyhostkeydnssettoyes,
       "anPkisshverifyhostkeydnssettoask": anPkisshverifyhostkeydnssettoask,
       "anPkisshknownhostcakeyremoved": anPkisshknownhostcakeyremoved,
       "anPkisshknownhostcakeyadded": anPkisshknownhostcakeyadded,
       "anPkisshknownhostkeyremoved": anPkisshknownhostkeyremoved,
       "anPkisshknownhostkeyadded": anPkisshknownhostkeyadded,
       "anPkisshlocalhostcertificatereplaced": anPkisshlocalhostcertificatereplaced,
       "anPkisshlocalhostcertificateremoved": anPkisshlocalhostcertificateremoved,
       "anPkisshlocalhostcertificateadded": anPkisshlocalhostcertificateadded,
       "anPkisshrevoked": anPkisshrevoked,
       "anPkimanuallyrevoked": anPkimanuallyrevoked,
       "anPkisshuserkrlreplaced": anPkisshuserkrlreplaced,
       "anPkisshuserkrladded": anPkisshuserkrladded,
       "anPkisshuserkrlremoved": anPkisshuserkrlremoved,
       "anPkisshcertexpiring": anPkisshcertexpiring,
       "anPkisshcertexpired": anPkisshcertexpired,
       "anCntnFilterHashListFileInvalidEntry": anCntnFilterHashListFileInvalidEntry,
       "anCntnFilterHashListFileNotFound": anCntnFilterHashListFileNotFound,
       "anCntnFilterHashListFileOverflow": anCntnFilterHashListFileOverflow,
       "anCntnFilterHashListFileTooBig": anCntnFilterHashListFileTooBig,
       "anGwSubsGrpFileNotFound": anGwSubsGrpFileNotFound,
       "anNewMemImageFileDetected": anNewMemImageFileDetected,
       "anCaleaUserBanFeatureConfigChange": anCaleaUserBanFeatureConfigChange,
       "anCaleaCCDataLost": anCaleaCCDataLost,
       "anCaleaIRIDataLost": anCaleaIRIDataLost,
       "anIpOspfv2NbrDown": anIpOspfv2NbrDown,
       "anIpOspfv3NbrDown": anIpOspfv3NbrDown,
       "anNatPoolSessionAlarmThreshold": anNatPoolSessionAlarmThreshold,
       "anNatPoolIpAddressAlarmThreshold": anNatPoolIpAddressAlarmThreshold,
       "anNatPoolPortChunkAlarmThreshold": anNatPoolPortChunkAlarmThreshold,
       "anNewFaultFileDetected": anNewFaultFileDetected,
       "anCntnHealthCheckStateDown": anCntnHealthCheckStateDown,
       "anPfcpPeerDown": anPfcpPeerDown,
       "anPfcpPeerUp": anPfcpPeerUp,
       "anCaleaIfGrpSourceProfileConfigChange": anCaleaIfGrpSourceProfileConfigChange,
       "anCaleaIfGrpSourceProfileNotFound": anCaleaIfGrpSourceProfileNotFound,
       "anBfdSessionDown": anBfdSessionDown,
       "anNodeRebootRequired": anNodeRebootRequired,
       "anPortmapFailure": anPortmapFailure,
       "anRadiusAccountingOnMsgNotSent": anRadiusAccountingOnMsgNotSent,
       "anCntnCACertExpired": anCntnCACertExpired,
       "anClusterRebootRequired": anClusterRebootRequired,
       "anCaleaPdhirNotSupportedForSx3lifTunnelToCPF": anCaleaPdhirNotSupportedForSx3lifTunnelToCPF,
       "anCaleaDecryptFail": anCaleaDecryptFail,
       "anDnsServerConfigLoadFail": anDnsServerConfigLoadFail,
       "anDnsServerRecClientHardLimitExceeded": anDnsServerRecClientHardLimitExceeded,
       "anDnsServerRecClientSoftLimitExceeded": anDnsServerRecClientSoftLimitExceeded,
       "anDnsServerZoneLoadFail": anDnsServerZoneLoadFail,
       "anTaskTermination": anTaskTermination,
       "affirmedSnmpAn3000TrapsNotificationObjects": affirmedSnmpAn3000TrapsNotificationObjects}
)
