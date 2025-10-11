# SNMP MIB module (OG-OMTRAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/opengear/OG-OMTRAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:24 2025
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

(ogMgmt,) = mibBuilder.importSymbols(
    "OG-SMI-MIB",
    "ogMgmt")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

ogOMTRAPSMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18)
)
if mibBuilder.loadTexts:
    ogOMTRAPSMib.setRevisions(
        ("2020-11-10 15:00",
         "2019-08-29 15:00",
         "2019-08-07 15:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OgOMTRAPSObjects_ObjectIdentity = ObjectIdentity
ogOMTRAPSObjects = _OgOMTRAPSObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1)
)
_OgOMTRAPSEvent_ObjectIdentity = ObjectIdentity
ogOMTRAPSEvent = _OgOMTRAPSEvent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1)
)
_OgOMTRAPSConnectivityTestResult_Type = DisplayString
_OgOMTRAPSConnectivityTestResult_Object = MibScalar
ogOMTRAPSConnectivityTestResult = _OgOMTRAPSConnectivityTestResult_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 1),
    _OgOMTRAPSConnectivityTestResult_Type()
)
ogOMTRAPSConnectivityTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSConnectivityTestResult.setStatus("current")
_OgOMTRAPSConnectivityTestSignal_Type = DisplayString
_OgOMTRAPSConnectivityTestSignal_Object = MibScalar
ogOMTRAPSConnectivityTestSignal = _OgOMTRAPSConnectivityTestSignal_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 2),
    _OgOMTRAPSConnectivityTestSignal_Type()
)
ogOMTRAPSConnectivityTestSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSConnectivityTestSignal.setStatus("current")
_OgOMTRAPSConnectivityTestSignalStatus_Type = DisplayString
_OgOMTRAPSConnectivityTestSignalStatus_Object = MibScalar
ogOMTRAPSConnectivityTestSignalStatus = _OgOMTRAPSConnectivityTestSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 3),
    _OgOMTRAPSConnectivityTestSignalStatus_Type()
)
ogOMTRAPSConnectivityTestSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSConnectivityTestSignalStatus.setStatus("current")
_OgOMTRAPSSSHLoginStatus_Type = DisplayString
_OgOMTRAPSSSHLoginStatus_Object = MibScalar
ogOMTRAPSSSHLoginStatus = _OgOMTRAPSSSHLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 4),
    _OgOMTRAPSSSHLoginStatus_Type()
)
ogOMTRAPSSSHLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSSSHLoginStatus.setStatus("current")
_OgOMTRAPSWebLoginStatus_Type = DisplayString
_OgOMTRAPSWebLoginStatus_Object = MibScalar
ogOMTRAPSWebLoginStatus = _OgOMTRAPSWebLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 5),
    _OgOMTRAPSWebLoginStatus_Type()
)
ogOMTRAPSWebLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSWebLoginStatus.setStatus("current")
_OgOMTRAPSBusVoltage_Type = Integer32
_OgOMTRAPSBusVoltage_Object = MibScalar
ogOMTRAPSBusVoltage = _OgOMTRAPSBusVoltage_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 6),
    _OgOMTRAPSBusVoltage_Type()
)
ogOMTRAPSBusVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSBusVoltage.setStatus("current")
if mibBuilder.loadTexts:
    ogOMTRAPSBusVoltage.setUnits("0.1 Volt DC")
_OgOMTRAPSRebootStatus_Type = DisplayString
_OgOMTRAPSRebootStatus_Object = MibScalar
ogOMTRAPSRebootStatus = _OgOMTRAPSRebootStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 7),
    _OgOMTRAPSRebootStatus_Type()
)
ogOMTRAPSRebootStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSRebootStatus.setStatus("current")
_OgOMTRAPSCellSignal_Type = Integer32
_OgOMTRAPSCellSignal_Object = MibScalar
ogOMTRAPSCellSignal = _OgOMTRAPSCellSignal_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 8),
    _OgOMTRAPSCellSignal_Type()
)
ogOMTRAPSCellSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSCellSignal.setStatus("current")
_OgOMTRAPSConsoleLoginStatus_Type = DisplayString
_OgOMTRAPSConsoleLoginStatus_Object = MibScalar
ogOMTRAPSConsoleLoginStatus = _OgOMTRAPSConsoleLoginStatus_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 9),
    _OgOMTRAPSConsoleLoginStatus_Type()
)
ogOMTRAPSConsoleLoginStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSConsoleLoginStatus.setStatus("current")
_OgOMTRAPSSerialPortID_Type = DisplayString
_OgOMTRAPSSerialPortID_Object = MibScalar
ogOMTRAPSSerialPortID = _OgOMTRAPSSerialPortID_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 10),
    _OgOMTRAPSSerialPortID_Type()
)
ogOMTRAPSSerialPortID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSSerialPortID.setStatus("current")
_OgOMTRAPSSerialPortUser_Type = DisplayString
_OgOMTRAPSSerialPortUser_Object = MibScalar
ogOMTRAPSSerialPortUser = _OgOMTRAPSSerialPortUser_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 11),
    _OgOMTRAPSSerialPortUser_Type()
)
ogOMTRAPSSerialPortUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSSerialPortUser.setStatus("current")
_OgOMTRAPSNetworkLinkState_Type = DisplayString
_OgOMTRAPSNetworkLinkState_Object = MibScalar
ogOMTRAPSNetworkLinkState = _OgOMTRAPSNetworkLinkState_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 12),
    _OgOMTRAPSNetworkLinkState_Type()
)
ogOMTRAPSNetworkLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSNetworkLinkState.setStatus("current")
_OgOMTRAPSNetworkLinkDescription_Type = DisplayString
_OgOMTRAPSNetworkLinkDescription_Object = MibScalar
ogOMTRAPSNetworkLinkDescription = _OgOMTRAPSNetworkLinkDescription_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 13),
    _OgOMTRAPSNetworkLinkDescription_Type()
)
ogOMTRAPSNetworkLinkDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSNetworkLinkDescription.setStatus("current")
_OgOMTRAPSSensorTemperature_Type = Integer32
_OgOMTRAPSSensorTemperature_Object = MibScalar
ogOMTRAPSSensorTemperature = _OgOMTRAPSSensorTemperature_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 14),
    _OgOMTRAPSSensorTemperature_Type()
)
ogOMTRAPSSensorTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSSensorTemperature.setStatus("current")
if mibBuilder.loadTexts:
    ogOMTRAPSSensorTemperature.setUnits("millidegrees Celsius")
_OgOMTRAPSSensorDevice_Type = DisplayString
_OgOMTRAPSSensorDevice_Object = MibScalar
ogOMTRAPSSensorDevice = _OgOMTRAPSSensorDevice_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 15),
    _OgOMTRAPSSensorDevice_Type()
)
ogOMTRAPSSensorDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSSensorDevice.setStatus("current")
_OgOMTRAPSAlarmSummary_Type = DisplayString
_OgOMTRAPSAlarmSummary_Object = MibScalar
ogOMTRAPSAlarmSummary = _OgOMTRAPSAlarmSummary_Object(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 1, 1, 16),
    _OgOMTRAPSAlarmSummary_Type()
)
ogOMTRAPSAlarmSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ogOMTRAPSAlarmSummary.setStatus("current")
_OgOMTRAPSNotificationPrefix_ObjectIdentity = ObjectIdentity
ogOMTRAPSNotificationPrefix = _OgOMTRAPSNotificationPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2)
)
_OgOMTRAPSNotification_ObjectIdentity = ObjectIdentity
ogOMTRAPSNotification = _OgOMTRAPSNotification_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0)
)
_OgOMTRAPSMibConformance_ObjectIdentity = ObjectIdentity
ogOMTRAPSMibConformance = _OgOMTRAPSMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 3)
)
_OgOMTRAPSMibCompliances_ObjectIdentity = ObjectIdentity
ogOMTRAPSMibCompliances = _OgOMTRAPSMibCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 3, 1)
)
_OgOMTRAPSMibGroups_ObjectIdentity = ObjectIdentity
ogOMTRAPSMibGroups = _OgOMTRAPSMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 3, 2)
)

# Managed Objects groups

ogOMTRAPSMibGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 3, 2, 1)
)
ogOMTRAPSMibGroup.setObjects(
      *(("OG-OMTRAPS-MIB", "ogOMTRAPSConnectivityTestResult"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSConnectivityTestSignal"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSConnectivityTestSignalStatus"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSSHLoginStatus"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSWebLoginStatus"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSBusVoltage"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSRebootStatus"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSCellSignal"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSConsoleLoginStatus"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSerialPortID"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSerialPortUser"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSNetworkLinkState"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSNetworkLinkDescription"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSensorTemperature"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSensorDevice"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSAlarmSummary"))
)
if mibBuilder.loadTexts:
    ogOMTRAPSMibGroup.setStatus("current")


# Notification objects

ogOMTRAPSConnectivityTest = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 1)
)
ogOMTRAPSConnectivityTest.setObjects(
      *(("OG-OMTRAPS-MIB", "ogOMTRAPSConnectivityTestResult"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSConnectivityTestSignal"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSConnectivityTestSignalStatus"))
)
if mibBuilder.loadTexts:
    ogOMTRAPSConnectivityTest.setStatus(
        "current"
    )

ogOMTRAPSSSHLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 2)
)
ogOMTRAPSSSHLogin.setObjects(
    ("OG-OMTRAPS-MIB", "ogOMTRAPSSSHLoginStatus")
)
if mibBuilder.loadTexts:
    ogOMTRAPSSSHLogin.setStatus(
        "current"
    )

ogOMTRAPSWebLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 3)
)
ogOMTRAPSWebLogin.setObjects(
    ("OG-OMTRAPS-MIB", "ogOMTRAPSWebLoginStatus")
)
if mibBuilder.loadTexts:
    ogOMTRAPSWebLogin.setStatus(
        "current"
    )

ogOMTRAPSPSU1VoltageRangeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 4)
)
ogOMTRAPSPSU1VoltageRangeAlert.setObjects(
    ("OG-OMTRAPS-MIB", "ogOMTRAPSBusVoltage")
)
if mibBuilder.loadTexts:
    ogOMTRAPSPSU1VoltageRangeAlert.setStatus(
        "current"
    )

ogOMTRAPSPSU2VoltageRangeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 5)
)
ogOMTRAPSPSU2VoltageRangeAlert.setObjects(
    ("OG-OMTRAPS-MIB", "ogOMTRAPSBusVoltage")
)
if mibBuilder.loadTexts:
    ogOMTRAPSPSU2VoltageRangeAlert.setStatus(
        "current"
    )

ogOMTRAPSReboot = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 6)
)
ogOMTRAPSReboot.setObjects(
    ("OG-OMTRAPS-MIB", "ogOMTRAPSRebootStatus")
)
if mibBuilder.loadTexts:
    ogOMTRAPSReboot.setStatus(
        "current"
    )

ogOMTRAPSCellSignalAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 7)
)
ogOMTRAPSCellSignalAlert.setObjects(
    ("OG-OMTRAPS-MIB", "ogOMTRAPSCellSignal")
)
if mibBuilder.loadTexts:
    ogOMTRAPSCellSignalAlert.setStatus(
        "current"
    )

ogOMTRAPSConfigChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 8)
)
if mibBuilder.loadTexts:
    ogOMTRAPSConfigChange.setStatus(
        "current"
    )

ogOMTRAPSConsoleLogin = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 9)
)
ogOMTRAPSConsoleLogin.setObjects(
    ("OG-OMTRAPS-MIB", "ogOMTRAPSConsoleLoginStatus")
)
if mibBuilder.loadTexts:
    ogOMTRAPSConsoleLogin.setStatus(
        "current"
    )

ogOMTRAPSSerialPortLoginAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 10)
)
ogOMTRAPSSerialPortLoginAlert.setObjects(
      *(("OG-OMTRAPS-MIB", "ogOMTRAPSSerialPortID"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSerialPortUser"))
)
if mibBuilder.loadTexts:
    ogOMTRAPSSerialPortLoginAlert.setStatus(
        "current"
    )

ogOMTRAPSSerialPortLogoutAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 11)
)
ogOMTRAPSSerialPortLogoutAlert.setObjects(
      *(("OG-OMTRAPS-MIB", "ogOMTRAPSSerialPortID"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSerialPortUser"))
)
if mibBuilder.loadTexts:
    ogOMTRAPSSerialPortLogoutAlert.setStatus(
        "current"
    )

ogOMTRAPSNetworkLinkStateAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 12)
)
ogOMTRAPSNetworkLinkStateAlert.setObjects(
      *(("OG-OMTRAPS-MIB", "ogOMTRAPSNetworkLinkState"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSNetworkLinkDescription"))
)
if mibBuilder.loadTexts:
    ogOMTRAPSNetworkLinkStateAlert.setStatus(
        "current"
    )

ogOMTRAPSSensorTemperatureRangeAlert = NotificationType(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 2, 0, 13)
)
ogOMTRAPSSensorTemperatureRangeAlert.setObjects(
      *(("OG-OMTRAPS-MIB", "ogOMTRAPSSensorTemperature"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSensorDevice"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSAlarmSummary"))
)
if mibBuilder.loadTexts:
    ogOMTRAPSSensorTemperatureRangeAlert.setStatus(
        "current"
    )


# Notifications groups

ogOMTRAPSNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 3, 2, 2)
)
ogOMTRAPSNotificationsGroup.setObjects(
      *(("OG-OMTRAPS-MIB", "ogOMTRAPSConnectivityTest"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSSHLogin"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSWebLogin"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSPSU1VoltageRangeAlert"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSPSU2VoltageRangeAlert"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSReboot"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSCellSignalAlert"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSConfigChange"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSConsoleLogin"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSerialPortLoginAlert"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSerialPortLogoutAlert"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSNetworkLinkStateAlert"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSSensorTemperatureRangeAlert"))
)
if mibBuilder.loadTexts:
    ogOMTRAPSNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

ogOMTRAPSMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 25049, 10, 18, 3, 1, 1)
)
ogOMTRAPSMibCompliance.setObjects(
      *(("OG-OMTRAPS-MIB", "ogOMTRAPSMibGroup"),
        ("OG-OMTRAPS-MIB", "ogOMTRAPSNotificationsGroup"))
)
if mibBuilder.loadTexts:
    ogOMTRAPSMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OG-OMTRAPS-MIB",
    **{"ogOMTRAPSMib": ogOMTRAPSMib,
       "ogOMTRAPSObjects": ogOMTRAPSObjects,
       "ogOMTRAPSEvent": ogOMTRAPSEvent,
       "ogOMTRAPSConnectivityTestResult": ogOMTRAPSConnectivityTestResult,
       "ogOMTRAPSConnectivityTestSignal": ogOMTRAPSConnectivityTestSignal,
       "ogOMTRAPSConnectivityTestSignalStatus": ogOMTRAPSConnectivityTestSignalStatus,
       "ogOMTRAPSSSHLoginStatus": ogOMTRAPSSSHLoginStatus,
       "ogOMTRAPSWebLoginStatus": ogOMTRAPSWebLoginStatus,
       "ogOMTRAPSBusVoltage": ogOMTRAPSBusVoltage,
       "ogOMTRAPSRebootStatus": ogOMTRAPSRebootStatus,
       "ogOMTRAPSCellSignal": ogOMTRAPSCellSignal,
       "ogOMTRAPSConsoleLoginStatus": ogOMTRAPSConsoleLoginStatus,
       "ogOMTRAPSSerialPortID": ogOMTRAPSSerialPortID,
       "ogOMTRAPSSerialPortUser": ogOMTRAPSSerialPortUser,
       "ogOMTRAPSNetworkLinkState": ogOMTRAPSNetworkLinkState,
       "ogOMTRAPSNetworkLinkDescription": ogOMTRAPSNetworkLinkDescription,
       "ogOMTRAPSSensorTemperature": ogOMTRAPSSensorTemperature,
       "ogOMTRAPSSensorDevice": ogOMTRAPSSensorDevice,
       "ogOMTRAPSAlarmSummary": ogOMTRAPSAlarmSummary,
       "ogOMTRAPSNotificationPrefix": ogOMTRAPSNotificationPrefix,
       "ogOMTRAPSNotification": ogOMTRAPSNotification,
       "ogOMTRAPSConnectivityTest": ogOMTRAPSConnectivityTest,
       "ogOMTRAPSSSHLogin": ogOMTRAPSSSHLogin,
       "ogOMTRAPSWebLogin": ogOMTRAPSWebLogin,
       "ogOMTRAPSPSU1VoltageRangeAlert": ogOMTRAPSPSU1VoltageRangeAlert,
       "ogOMTRAPSPSU2VoltageRangeAlert": ogOMTRAPSPSU2VoltageRangeAlert,
       "ogOMTRAPSReboot": ogOMTRAPSReboot,
       "ogOMTRAPSCellSignalAlert": ogOMTRAPSCellSignalAlert,
       "ogOMTRAPSConfigChange": ogOMTRAPSConfigChange,
       "ogOMTRAPSConsoleLogin": ogOMTRAPSConsoleLogin,
       "ogOMTRAPSSerialPortLoginAlert": ogOMTRAPSSerialPortLoginAlert,
       "ogOMTRAPSSerialPortLogoutAlert": ogOMTRAPSSerialPortLogoutAlert,
       "ogOMTRAPSNetworkLinkStateAlert": ogOMTRAPSNetworkLinkStateAlert,
       "ogOMTRAPSSensorTemperatureRangeAlert": ogOMTRAPSSensorTemperatureRangeAlert,
       "ogOMTRAPSMibConformance": ogOMTRAPSMibConformance,
       "ogOMTRAPSMibCompliances": ogOMTRAPSMibCompliances,
       "ogOMTRAPSMibCompliance": ogOMTRAPSMibCompliance,
       "ogOMTRAPSMibGroups": ogOMTRAPSMibGroups,
       "ogOMTRAPSMibGroup": ogOMTRAPSMibGroup,
       "ogOMTRAPSNotificationsGroup": ogOMTRAPSNotificationsGroup}
)
