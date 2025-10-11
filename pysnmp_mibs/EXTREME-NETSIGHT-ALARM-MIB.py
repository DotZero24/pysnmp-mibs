# SNMP MIB module (EXTREME-NETSIGHT-ALARM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/EXTREME-NETSIGHT-ALARM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:00 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

extremeNetsightAlarmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmMIB.setRevisions(
        ("2016-08-29 11:38",
         "2016-01-26 17:22",
         "2016-01-18 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExtremeNetsightAlarmObjects_ObjectIdentity = ObjectIdentity
extremeNetsightAlarmObjects = _ExtremeNetsightAlarmObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1)
)
_ExtremeNetsightAlarmNotifications_ObjectIdentity = ObjectIdentity
extremeNetsightAlarmNotifications = _ExtremeNetsightAlarmNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0)
)
_ExtremeNetsightAlarmVars_ObjectIdentity = ObjectIdentity
extremeNetsightAlarmVars = _ExtremeNetsightAlarmVars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 1)
)


class _ExtremeNetsightAlarmMessage_Type(OctetString):
    """Custom type extremeNetsightAlarmMessage based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExtremeNetsightAlarmMessage_Type.__name__ = "OctetString"
_ExtremeNetsightAlarmMessage_Object = MibScalar
extremeNetsightAlarmMessage = _ExtremeNetsightAlarmMessage_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 1, 1),
    _ExtremeNetsightAlarmMessage_Type()
)
extremeNetsightAlarmMessage.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetsightAlarmMessage.setStatus("current")


class _ExtremeNetsightAlarmSeverity_Type(Integer32):
    """Custom type extremeNetsightAlarmSeverity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("emergency", 0),
          ("alert", 1),
          ("critical", 2),
          ("error", 3),
          ("warning", 4),
          ("notice", 5),
          ("info", 6),
          ("debug", 7))
    )


_ExtremeNetsightAlarmSeverity_Type.__name__ = "Integer32"
_ExtremeNetsightAlarmSeverity_Object = MibScalar
extremeNetsightAlarmSeverity = _ExtremeNetsightAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 1, 2),
    _ExtremeNetsightAlarmSeverity_Type()
)
extremeNetsightAlarmSeverity.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetsightAlarmSeverity.setStatus("current")
_ExtremeNetsightAlarmTimestamp_Type = DateAndTime
_ExtremeNetsightAlarmTimestamp_Object = MibScalar
extremeNetsightAlarmTimestamp = _ExtremeNetsightAlarmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 1, 3),
    _ExtremeNetsightAlarmTimestamp_Type()
)
extremeNetsightAlarmTimestamp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetsightAlarmTimestamp.setStatus("current")
_ExtremeNetsightAlarmSourceDeviceAddressType_Type = InetAddressType
_ExtremeNetsightAlarmSourceDeviceAddressType_Object = MibScalar
extremeNetsightAlarmSourceDeviceAddressType = _ExtremeNetsightAlarmSourceDeviceAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 1, 4),
    _ExtremeNetsightAlarmSourceDeviceAddressType_Type()
)
extremeNetsightAlarmSourceDeviceAddressType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetsightAlarmSourceDeviceAddressType.setStatus("current")
_ExtremeNetsightAlarmSourceDeviceAddress_Type = InetAddress
_ExtremeNetsightAlarmSourceDeviceAddress_Object = MibScalar
extremeNetsightAlarmSourceDeviceAddress = _ExtremeNetsightAlarmSourceDeviceAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 1, 5),
    _ExtremeNetsightAlarmSourceDeviceAddress_Type()
)
extremeNetsightAlarmSourceDeviceAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetsightAlarmSourceDeviceAddress.setStatus("current")


class _ExtremeNetsightAlarmSubcomponent_Type(OctetString):
    """Custom type extremeNetsightAlarmSubcomponent based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_ExtremeNetsightAlarmSubcomponent_Type.__name__ = "OctetString"
_ExtremeNetsightAlarmSubcomponent_Object = MibScalar
extremeNetsightAlarmSubcomponent = _ExtremeNetsightAlarmSubcomponent_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 1, 6),
    _ExtremeNetsightAlarmSubcomponent_Type()
)
extremeNetsightAlarmSubcomponent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    extremeNetsightAlarmSubcomponent.setStatus("current")
_ExtremeNetsightAlarmConformance_ObjectIdentity = ObjectIdentity
extremeNetsightAlarmConformance = _ExtremeNetsightAlarmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 2)
)
_ExtremeNetsightAlarmGroups_ObjectIdentity = ObjectIdentity
extremeNetsightAlarmGroups = _ExtremeNetsightAlarmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 2, 1)
)
_ExtremeNetsightAlarmCompliances_ObjectIdentity = ObjectIdentity
extremeNetsightAlarmCompliances = _ExtremeNetsightAlarmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 2, 2)
)

# Managed Objects groups

extremeNetsightAlarmSettings = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 2, 1, 1)
)
extremeNetsightAlarmSettings.setObjects(
      *(("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmMessage"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSeverity"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmTimestamp"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSourceDeviceAddressType"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSourceDeviceAddress"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSubcomponent"))
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmSettings.setStatus("current")


# Notification objects

extremeNetsightAlarmNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 1)
)
extremeNetsightAlarmNotification.setObjects(
      *(("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmMessage"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSeverity"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmTimestamp"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSourceDeviceAddressType"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSourceDeviceAddress"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSubcomponent"))
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNotification.setStatus(
        "current"
    )

extremeNetsightAlarmDeviceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 2)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmDeviceUp.setStatus(
        "current"
    )

extremeNetsightAlarmDeviceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 3)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmDeviceDown.setStatus(
        "current"
    )

extremeNetsightAlarmLinkUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 4)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmLinkUp.setStatus(
        "current"
    )

extremeNetsightAlarmLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 5)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmLinkDown.setStatus(
        "current"
    )

extremeNetsightAlarmFanOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 6)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmFanOK.setStatus(
        "current"
    )

extremeNetsightAlarmFanFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 7)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmFanFailure.setStatus(
        "current"
    )

extremeNetsightAlarmPowerSupplyNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 8)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmPowerSupplyNormal.setStatus(
        "current"
    )

extremeNetsightAlarmPowerSupplyFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 9)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmPowerSupplyFailed.setStatus(
        "current"
    )

extremeNetsightAlarmMultiAuthMaxUsersReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 10)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmMultiAuthMaxUsersReached.setStatus(
        "current"
    )

extremeNetsightAlarmMultiAuthModuleMaxUsersReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 11)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmMultiAuthModuleMaxUsersReached.setStatus(
        "current"
    )

extremeNetsightAlarmMultiAuthSystemMaxUsersReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 12)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmMultiAuthSystemMaxUsersReached.setStatus(
        "current"
    )

extremeNetsightAlarmOSPFConflictingPacket = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 13)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmOSPFConflictingPacket.setStatus(
        "current"
    )

extremeNetsightAlarmSpanguard = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 14)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmSpanguard.setStatus(
        "current"
    )

extremeNetsightAlarmMSTPLoopProtectEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 15)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmMSTPLoopProtectEvent.setStatus(
        "current"
    )

extremeNetsightAlarmSTPDiagnosticMSTI = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 16)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmSTPDiagnosticMSTI.setStatus(
        "current"
    )

extremeNetsightAlarmSTPDiagnosticCIST = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 17)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmSTPDiagnosticCIST.setStatus(
        "current"
    )

extremeNetsightAlarmColdStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 18)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmColdStart.setStatus(
        "current"
    )

extremeNetsightAlarmWarmStart = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 19)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmWarmStart.setStatus(
        "current"
    )

extremeNetsightAlarmMultiAuthSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 20)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmMultiAuthSuccess.setStatus(
        "current"
    )

extremeNetsightAlarmMultiAuthFailed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 21)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmMultiAuthFailed.setStatus(
        "current"
    )

extremeNetsightAlarmMultiAuthTerminated = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 22)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmMultiAuthTerminated.setStatus(
        "current"
    )

extremeNetsightAlarmConfigurationChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 23)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmConfigurationChanged.setStatus(
        "current"
    )

extremeNetsightAlarmAPInService = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 24)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmAPInService.setStatus(
        "current"
    )

extremeNetsightAlarmAPOutOfService = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 25)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmAPOutOfService.setStatus(
        "current"
    )

extremeNetsightAlarmAPRadioChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 26)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmAPRadioChange.setStatus(
        "current"
    )

extremeNetsightAlarmAPRadioOnOff = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 27)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmAPRadioOnOff.setStatus(
        "current"
    )

extremeNetsightAlarmInterferenceStopped = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 28)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmInterferenceStopped.setStatus(
        "current"
    )

extremeNetsightAlarmInterferenceStarted = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 29)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmInterferenceStarted.setStatus(
        "current"
    )

extremeNetsightAlarmThreatInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 30)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmThreatInactive.setStatus(
        "current"
    )

extremeNetsightAlarmThreatActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 31)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmThreatActive.setStatus(
        "current"
    )

extremeNetsightAlarmApplianceDiskUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 32)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmApplianceDiskUsage.setStatus(
        "current"
    )

extremeNetsightAlarmDatabaseBackupDiskUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 33)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmDatabaseBackupDiskUsage.setStatus(
        "current"
    )

extremeNetsightAlarmRogueInactive = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 34)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmRogueInactive.setStatus(
        "current"
    )

extremeNetsightAlarmRogueActive = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 35)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmRogueActive.setStatus(
        "current"
    )

extremeNetsightAlarmIPMIEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 36)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmIPMIEvent.setStatus(
        "current"
    )

extremeNetsightAlarmACPowerRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 37)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmACPowerRecovered.setStatus(
        "current"
    )

extremeNetsightAlarmACPowerLost = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 38)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmACPowerLost.setStatus(
        "current"
    )

extremeNetsightAlarmDriveFaultRecovered = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 39)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmDriveFaultRecovered.setStatus(
        "current"
    )

extremeNetsightAlarmDriveFault = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 40)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmDriveFault.setStatus(
        "current"
    )

extremeNetsightAlarmApplicationAnalyticsLicenseViolationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 41)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmApplicationAnalyticsLicenseViolationClear.setStatus(
        "current"
    )

extremeNetsightAlarmApplicationAnalyticsLicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 42)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmApplicationAnalyticsLicenseViolation.setStatus(
        "current"
    )

extremeNetsightAlarmApplicationAnalyticsApplianceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 43)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmApplicationAnalyticsApplianceUp.setStatus(
        "current"
    )

extremeNetsightAlarmApplicationAnalyticsApplianceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 44)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmApplicationAnalyticsApplianceDown.setStatus(
        "current"
    )

extremeNetsightAlarmNACApplianceUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 45)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACApplianceUp.setStatus(
        "current"
    )

extremeNetsightAlarmNACApplianceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 46)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACApplianceDown.setStatus(
        "current"
    )

extremeNetsightAlarmNACLicenseViolationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 47)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLicenseViolationClear.setStatus(
        "current"
    )

extremeNetsightAlarmNACLicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 48)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLicenseViolation.setStatus(
        "current"
    )

extremeNetsightAlarmNACAssessmentLicenseViolationClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 49)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACAssessmentLicenseViolationClear.setStatus(
        "current"
    )

extremeNetsightAlarmNACAssessmentLicenseViolation = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 50)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACAssessmentLicenseViolation.setStatus(
        "current"
    )

extremeNetsightAlarmNACLostContactWithSwitchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 51)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLostContactWithSwitchClear.setStatus(
        "current"
    )

extremeNetsightAlarmNACLostContactWithSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 52)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLostContactWithSwitch.setStatus(
        "current"
    )

extremeNetsightAlarmNACLostPartialContactWithSwitchClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 53)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLostPartialContactWithSwitchClear.setStatus(
        "current"
    )

extremeNetsightAlarmNACLostPartialContactWithSwitch = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 54)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLostPartialContactWithSwitch.setStatus(
        "current"
    )

extremeNetsightAlarmNACLostContactWithRADIUSServerClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 55)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLostContactWithRADIUSServerClear.setStatus(
        "current"
    )

extremeNetsightAlarmNACLostContactWithRADIUSServer = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 56)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLostContactWithRADIUSServer.setStatus(
        "current"
    )

extremeNetsightAlarmNACLostContactWithLDAPServiceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 57)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLostContactWithLDAPServiceClear.setStatus(
        "current"
    )

extremeNetsightAlarmNACLostContactWithLDAPService = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 58)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLostContactWithLDAPService.setStatus(
        "current"
    )

extremeNetsightAlarmNACLostPartialContactWithLDAPServiceClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 59)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLostPartialContactWithLDAPServiceClear.setStatus(
        "current"
    )

extremeNetsightAlarmNACLostPartialContactWithLDAPService = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 60)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACLostPartialContactWithLDAPService.setStatus(
        "current"
    )

extremeNetsightAlarmNACRFC3576ErrorClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 61)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACRFC3576ErrorClear.setStatus(
        "current"
    )

extremeNetsightAlarmNACRFC3576Error = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 62)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACRFC3576Error.setStatus(
        "current"
    )

extremeNetsightAlarmNACDatabaseTableServiceIsUp = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 63)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACDatabaseTableServiceIsUp.setStatus(
        "current"
    )

extremeNetsightAlarmNACDatabaseTableServiceDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 64)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACDatabaseTableServiceDown.setStatus(
        "current"
    )

extremeNetsightAlarmNACRADIUSRequestsWarningThresholdRectified = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 65)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACRADIUSRequestsWarningThresholdRectified.setStatus(
        "current"
    )

extremeNetsightAlarmNACRADIUSRequestsWarningThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 66)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACRADIUSRequestsWarningThresholdExceeded.setStatus(
        "current"
    )

extremeNetsightAlarmNACRADIUSRequestsCriticalThresholdRectified = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 67)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACRADIUSRequestsCriticalThresholdRectified.setStatus(
        "current"
    )

extremeNetsightAlarmNACRADIUSRequestsCriticalThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 68)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACRADIUSRequestsCriticalThresholdExceeded.setStatus(
        "current"
    )

extremeNetsightAlarmNACCertificateUpdated = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 69)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACCertificateUpdated.setStatus(
        "current"
    )

extremeNetsightAlarmNACCertificateHasInvalidDate = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 70)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACCertificateHasInvalidDate.setStatus(
        "current"
    )

extremeNetsightAlarmNACCertificateWarningCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 71)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACCertificateWarningCleared.setStatus(
        "current"
    )

extremeNetsightAlarmNACCertificateExpiringWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 72)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACCertificateExpiringWarning.setStatus(
        "current"
    )

extremeNetsightAlarmNACCertificateNoticeCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 73)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACCertificateNoticeCleared.setStatus(
        "current"
    )

extremeNetsightAlarmNACCertificateExpiringNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 74)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACCertificateExpiringNotice.setStatus(
        "current"
    )

extremeNetsightAlarmNACDuplicateSNMPEngineIDCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 75)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACDuplicateSNMPEngineIDCleared.setStatus(
        "current"
    )

extremeNetsightAlarmNACDuplicateSNMPEngineIDFound = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 76)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACDuplicateSNMPEngineIDFound.setStatus(
        "current"
    )

extremeNetsightAlarmDeviceTopologyChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 77)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmDeviceTopologyChange.setStatus(
        "current"
    )

extremeNetsightAlarmDevicePercentCPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 78)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmDevicePercentCPU.setStatus(
        "current"
    )

extremeNetsightAlarmDeviceMemoryPercentUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 79)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmDeviceMemoryPercentUsage.setStatus(
        "current"
    )

extremeNetsightAlarmHostPercentCPU = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 80)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmHostPercentCPU.setStatus(
        "current"
    )

extremeNetsightAlarmHostDiskPercentUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 81)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmHostDiskPercentUsage.setStatus(
        "current"
    )

extremeNetsightAlarmHostMemoryPercentUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 82)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmHostMemoryPercentUsage.setStatus(
        "current"
    )

extremeNetsightAlarmInterfacePercentUsage = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 83)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmInterfacePercentUsage.setStatus(
        "current"
    )

extremeNetsightAlarmInterfacePercentValidPackets = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 84)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmInterfacePercentValidPackets.setStatus(
        "current"
    )

extremeNetsightAlarmHistoricalPersistenceResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 85)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmHistoricalPersistenceResumed.setStatus(
        "current"
    )

extremeNetsightAlarmHistoricalPersistenceSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 86)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmHistoricalPersistenceSuspended.setStatus(
        "current"
    )

extremeNetsightAlarmAnalyticsPersistenceResumed = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 87)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmAnalyticsPersistenceResumed.setStatus(
        "current"
    )

extremeNetsightAlarmAnalyticsPersistenceSuspended = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 88)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmAnalyticsPersistenceSuspended.setStatus(
        "current"
    )

extremeNetsightAlarmControllerEstablishedSSHConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 89)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmControllerEstablishedSSHConnection.setStatus(
        "current"
    )

extremeNetsightAlarmControllerFailedSSHConnection = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 90)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmControllerFailedSSHConnection.setStatus(
        "current"
    )

extremeNetsightAlarmServerHeapMemoryOK = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 91)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmServerHeapMemoryOK.setStatus(
        "current"
    )

extremeNetsightAlarmServerHeapMemoryLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 92)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmServerHeapMemoryLow.setStatus(
        "current"
    )

extremeNetsightAlarmClientMACAvailabilityLow = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 93)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmClientMACAvailabilityLow.setStatus(
        "current"
    )

extremeNetsightAlarmClientMACIPChangesHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 94)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmClientMACIPChangesHigh.setStatus(
        "current"
    )

extremeNetsightAlarmNACEntriesPerGroupPerfThresholdRectified = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 95)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACEntriesPerGroupPerfThresholdRectified.setStatus(
        "current"
    )

extremeNetsightAlarmNACEntriesPerGroupPerfThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 96)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACEntriesPerGroupPerfThresholdExceeded.setStatus(
        "current"
    )

extremeNetsightAlarmNACCertificateUsesMD5SignatureCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 97)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACCertificateUsesMD5SignatureCleared.setStatus(
        "current"
    )

extremeNetsightAlarmNACCertificateUsesMD5SignatureNotice = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 98)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACCertificateUsesMD5SignatureNotice.setStatus(
        "current"
    )

extremeNetsightAlarmNACWinbinddProcessCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 99)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACWinbinddProcessCleared.setStatus(
        "current"
    )

extremeNetsightAlarmNACWinbinddProcessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 100)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACWinbinddProcessDown.setStatus(
        "current"
    )

extremeNetsightAlarmNACSquidProcessCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 101)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACSquidProcessCleared.setStatus(
        "current"
    )

extremeNetsightAlarmNACSquidProcessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 102)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACSquidProcessDown.setStatus(
        "current"
    )

extremeNetsightAlarmNACRadiusdProcessCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 103)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACRadiusdProcessCleared.setStatus(
        "current"
    )

extremeNetsightAlarmNACRadiusdProcessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 104)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACRadiusdProcessDown.setStatus(
        "current"
    )

extremeNetsightAlarmNACDnsproxyProcessCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 105)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACDnsproxyProcessCleared.setStatus(
        "current"
    )

extremeNetsightAlarmNACDnsproxyProcessDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 106)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACDnsproxyProcessDown.setStatus(
        "current"
    )

extremeNetsightAlarmNACIPMICriticalEventCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 107)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACIPMICriticalEventCleared.setStatus(
        "current"
    )

extremeNetsightAlarmNACIPMICriticalEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 108)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACIPMICriticalEvent.setStatus(
        "current"
    )

extremeNetsightAlarmNACDNSServersUnreachableCleared = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 109)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACDNSServersUnreachableCleared.setStatus(
        "current"
    )

extremeNetsightAlarmNACDNSServersUnreachable = NotificationType(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 1, 0, 110)
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmNACDNSServersUnreachable.setStatus(
        "current"
    )


# Notifications groups

extremeNetsightAlarmGenericNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 2, 1, 2)
)
extremeNetsightAlarmGenericNotificationGroup.setObjects(
    ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNotification")
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmGenericNotificationGroup.setStatus(
        "current"
    )

extremeNetsightAlarmSpecificNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 2, 1, 3)
)
extremeNetsightAlarmSpecificNotificationGroup.setObjects(
      *(("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmDeviceUp"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmDeviceDown"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmLinkUp"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmLinkDown"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmFanOK"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmFanFailure"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmPowerSupplyNormal"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmPowerSupplyFailed"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmMultiAuthMaxUsersReached"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmMultiAuthModuleMaxUsersReached"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmMultiAuthSystemMaxUsersReached"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmOSPFConflictingPacket"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSpanguard"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmMSTPLoopProtectEvent"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSTPDiagnosticMSTI"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSTPDiagnosticCIST"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmColdStart"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmWarmStart"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmMultiAuthSuccess"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmMultiAuthFailed"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmMultiAuthTerminated"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmConfigurationChanged"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmAPInService"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmAPOutOfService"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmAPRadioChange"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmAPRadioOnOff"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmInterferenceStopped"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmInterferenceStarted"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmThreatInactive"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmThreatActive"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmApplianceDiskUsage"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmDatabaseBackupDiskUsage"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmRogueInactive"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmRogueActive"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmIPMIEvent"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmACPowerRecovered"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmACPowerLost"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmDriveFaultRecovered"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmDriveFault"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmApplicationAnalyticsLicenseViolationClear"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmApplicationAnalyticsLicenseViolation"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmApplicationAnalyticsApplianceUp"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmApplicationAnalyticsApplianceDown"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACApplianceUp"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACApplianceDown"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLicenseViolationClear"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLicenseViolation"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACAssessmentLicenseViolationClear"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACAssessmentLicenseViolation"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLostContactWithSwitchClear"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLostContactWithSwitch"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLostPartialContactWithSwitchClear"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLostPartialContactWithSwitch"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLostContactWithRADIUSServerClear"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLostContactWithRADIUSServer"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLostContactWithLDAPServiceClear"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLostContactWithLDAPService"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLostPartialContactWithLDAPServiceClear"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACLostPartialContactWithLDAPService"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACRFC3576ErrorClear"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACRFC3576Error"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACDatabaseTableServiceIsUp"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACDatabaseTableServiceDown"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACRADIUSRequestsWarningThresholdRectified"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACRADIUSRequestsWarningThresholdExceeded"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACRADIUSRequestsCriticalThresholdRectified"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACRADIUSRequestsCriticalThresholdExceeded"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACCertificateUpdated"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACCertificateHasInvalidDate"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACCertificateWarningCleared"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACCertificateExpiringWarning"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACCertificateNoticeCleared"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACCertificateExpiringNotice"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACDuplicateSNMPEngineIDCleared"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACDuplicateSNMPEngineIDFound"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmDeviceTopologyChange"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmDevicePercentCPU"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmDeviceMemoryPercentUsage"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmHostPercentCPU"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmHostDiskPercentUsage"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmHostMemoryPercentUsage"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmInterfacePercentUsage"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmInterfacePercentValidPackets"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmHistoricalPersistenceResumed"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmHistoricalPersistenceSuspended"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmAnalyticsPersistenceResumed"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmAnalyticsPersistenceSuspended"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmControllerEstablishedSSHConnection"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmControllerFailedSSHConnection"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmServerHeapMemoryOK"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmServerHeapMemoryLow"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmClientMACAvailabilityLow"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmClientMACIPChangesHigh"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACEntriesPerGroupPerfThresholdRectified"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACEntriesPerGroupPerfThresholdExceeded"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACCertificateUsesMD5SignatureCleared"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACCertificateUsesMD5SignatureNotice"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACWinbinddProcessCleared"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACWinbinddProcessDown"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACSquidProcessCleared"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACSquidProcessDown"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACRadiusdProcessCleared"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACRadiusdProcessDown"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACDnsproxyProcessCleared"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACDnsproxyProcessDown"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACIPMICriticalEventCleared"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACIPMICriticalEvent"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACDNSServersUnreachableCleared"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmNACDNSServersUnreachable"))
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmSpecificNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

extremeNetsightAlarmComplianceGroup = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 105, 2, 2, 1)
)
extremeNetsightAlarmComplianceGroup.setObjects(
      *(("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSettings"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmGenericNotificationGroup"),
        ("EXTREME-NETSIGHT-ALARM-MIB", "extremeNetsightAlarmSpecificNotificationGroup"))
)
if mibBuilder.loadTexts:
    extremeNetsightAlarmComplianceGroup.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EXTREME-NETSIGHT-ALARM-MIB",
    **{"extremeNetsightAlarmMIB": extremeNetsightAlarmMIB,
       "extremeNetsightAlarmObjects": extremeNetsightAlarmObjects,
       "extremeNetsightAlarmNotifications": extremeNetsightAlarmNotifications,
       "extremeNetsightAlarmNotification": extremeNetsightAlarmNotification,
       "extremeNetsightAlarmDeviceUp": extremeNetsightAlarmDeviceUp,
       "extremeNetsightAlarmDeviceDown": extremeNetsightAlarmDeviceDown,
       "extremeNetsightAlarmLinkUp": extremeNetsightAlarmLinkUp,
       "extremeNetsightAlarmLinkDown": extremeNetsightAlarmLinkDown,
       "extremeNetsightAlarmFanOK": extremeNetsightAlarmFanOK,
       "extremeNetsightAlarmFanFailure": extremeNetsightAlarmFanFailure,
       "extremeNetsightAlarmPowerSupplyNormal": extremeNetsightAlarmPowerSupplyNormal,
       "extremeNetsightAlarmPowerSupplyFailed": extremeNetsightAlarmPowerSupplyFailed,
       "extremeNetsightAlarmMultiAuthMaxUsersReached": extremeNetsightAlarmMultiAuthMaxUsersReached,
       "extremeNetsightAlarmMultiAuthModuleMaxUsersReached": extremeNetsightAlarmMultiAuthModuleMaxUsersReached,
       "extremeNetsightAlarmMultiAuthSystemMaxUsersReached": extremeNetsightAlarmMultiAuthSystemMaxUsersReached,
       "extremeNetsightAlarmOSPFConflictingPacket": extremeNetsightAlarmOSPFConflictingPacket,
       "extremeNetsightAlarmSpanguard": extremeNetsightAlarmSpanguard,
       "extremeNetsightAlarmMSTPLoopProtectEvent": extremeNetsightAlarmMSTPLoopProtectEvent,
       "extremeNetsightAlarmSTPDiagnosticMSTI": extremeNetsightAlarmSTPDiagnosticMSTI,
       "extremeNetsightAlarmSTPDiagnosticCIST": extremeNetsightAlarmSTPDiagnosticCIST,
       "extremeNetsightAlarmColdStart": extremeNetsightAlarmColdStart,
       "extremeNetsightAlarmWarmStart": extremeNetsightAlarmWarmStart,
       "extremeNetsightAlarmMultiAuthSuccess": extremeNetsightAlarmMultiAuthSuccess,
       "extremeNetsightAlarmMultiAuthFailed": extremeNetsightAlarmMultiAuthFailed,
       "extremeNetsightAlarmMultiAuthTerminated": extremeNetsightAlarmMultiAuthTerminated,
       "extremeNetsightAlarmConfigurationChanged": extremeNetsightAlarmConfigurationChanged,
       "extremeNetsightAlarmAPInService": extremeNetsightAlarmAPInService,
       "extremeNetsightAlarmAPOutOfService": extremeNetsightAlarmAPOutOfService,
       "extremeNetsightAlarmAPRadioChange": extremeNetsightAlarmAPRadioChange,
       "extremeNetsightAlarmAPRadioOnOff": extremeNetsightAlarmAPRadioOnOff,
       "extremeNetsightAlarmInterferenceStopped": extremeNetsightAlarmInterferenceStopped,
       "extremeNetsightAlarmInterferenceStarted": extremeNetsightAlarmInterferenceStarted,
       "extremeNetsightAlarmThreatInactive": extremeNetsightAlarmThreatInactive,
       "extremeNetsightAlarmThreatActive": extremeNetsightAlarmThreatActive,
       "extremeNetsightAlarmApplianceDiskUsage": extremeNetsightAlarmApplianceDiskUsage,
       "extremeNetsightAlarmDatabaseBackupDiskUsage": extremeNetsightAlarmDatabaseBackupDiskUsage,
       "extremeNetsightAlarmRogueInactive": extremeNetsightAlarmRogueInactive,
       "extremeNetsightAlarmRogueActive": extremeNetsightAlarmRogueActive,
       "extremeNetsightAlarmIPMIEvent": extremeNetsightAlarmIPMIEvent,
       "extremeNetsightAlarmACPowerRecovered": extremeNetsightAlarmACPowerRecovered,
       "extremeNetsightAlarmACPowerLost": extremeNetsightAlarmACPowerLost,
       "extremeNetsightAlarmDriveFaultRecovered": extremeNetsightAlarmDriveFaultRecovered,
       "extremeNetsightAlarmDriveFault": extremeNetsightAlarmDriveFault,
       "extremeNetsightAlarmApplicationAnalyticsLicenseViolationClear": extremeNetsightAlarmApplicationAnalyticsLicenseViolationClear,
       "extremeNetsightAlarmApplicationAnalyticsLicenseViolation": extremeNetsightAlarmApplicationAnalyticsLicenseViolation,
       "extremeNetsightAlarmApplicationAnalyticsApplianceUp": extremeNetsightAlarmApplicationAnalyticsApplianceUp,
       "extremeNetsightAlarmApplicationAnalyticsApplianceDown": extremeNetsightAlarmApplicationAnalyticsApplianceDown,
       "extremeNetsightAlarmNACApplianceUp": extremeNetsightAlarmNACApplianceUp,
       "extremeNetsightAlarmNACApplianceDown": extremeNetsightAlarmNACApplianceDown,
       "extremeNetsightAlarmNACLicenseViolationClear": extremeNetsightAlarmNACLicenseViolationClear,
       "extremeNetsightAlarmNACLicenseViolation": extremeNetsightAlarmNACLicenseViolation,
       "extremeNetsightAlarmNACAssessmentLicenseViolationClear": extremeNetsightAlarmNACAssessmentLicenseViolationClear,
       "extremeNetsightAlarmNACAssessmentLicenseViolation": extremeNetsightAlarmNACAssessmentLicenseViolation,
       "extremeNetsightAlarmNACLostContactWithSwitchClear": extremeNetsightAlarmNACLostContactWithSwitchClear,
       "extremeNetsightAlarmNACLostContactWithSwitch": extremeNetsightAlarmNACLostContactWithSwitch,
       "extremeNetsightAlarmNACLostPartialContactWithSwitchClear": extremeNetsightAlarmNACLostPartialContactWithSwitchClear,
       "extremeNetsightAlarmNACLostPartialContactWithSwitch": extremeNetsightAlarmNACLostPartialContactWithSwitch,
       "extremeNetsightAlarmNACLostContactWithRADIUSServerClear": extremeNetsightAlarmNACLostContactWithRADIUSServerClear,
       "extremeNetsightAlarmNACLostContactWithRADIUSServer": extremeNetsightAlarmNACLostContactWithRADIUSServer,
       "extremeNetsightAlarmNACLostContactWithLDAPServiceClear": extremeNetsightAlarmNACLostContactWithLDAPServiceClear,
       "extremeNetsightAlarmNACLostContactWithLDAPService": extremeNetsightAlarmNACLostContactWithLDAPService,
       "extremeNetsightAlarmNACLostPartialContactWithLDAPServiceClear": extremeNetsightAlarmNACLostPartialContactWithLDAPServiceClear,
       "extremeNetsightAlarmNACLostPartialContactWithLDAPService": extremeNetsightAlarmNACLostPartialContactWithLDAPService,
       "extremeNetsightAlarmNACRFC3576ErrorClear": extremeNetsightAlarmNACRFC3576ErrorClear,
       "extremeNetsightAlarmNACRFC3576Error": extremeNetsightAlarmNACRFC3576Error,
       "extremeNetsightAlarmNACDatabaseTableServiceIsUp": extremeNetsightAlarmNACDatabaseTableServiceIsUp,
       "extremeNetsightAlarmNACDatabaseTableServiceDown": extremeNetsightAlarmNACDatabaseTableServiceDown,
       "extremeNetsightAlarmNACRADIUSRequestsWarningThresholdRectified": extremeNetsightAlarmNACRADIUSRequestsWarningThresholdRectified,
       "extremeNetsightAlarmNACRADIUSRequestsWarningThresholdExceeded": extremeNetsightAlarmNACRADIUSRequestsWarningThresholdExceeded,
       "extremeNetsightAlarmNACRADIUSRequestsCriticalThresholdRectified": extremeNetsightAlarmNACRADIUSRequestsCriticalThresholdRectified,
       "extremeNetsightAlarmNACRADIUSRequestsCriticalThresholdExceeded": extremeNetsightAlarmNACRADIUSRequestsCriticalThresholdExceeded,
       "extremeNetsightAlarmNACCertificateUpdated": extremeNetsightAlarmNACCertificateUpdated,
       "extremeNetsightAlarmNACCertificateHasInvalidDate": extremeNetsightAlarmNACCertificateHasInvalidDate,
       "extremeNetsightAlarmNACCertificateWarningCleared": extremeNetsightAlarmNACCertificateWarningCleared,
       "extremeNetsightAlarmNACCertificateExpiringWarning": extremeNetsightAlarmNACCertificateExpiringWarning,
       "extremeNetsightAlarmNACCertificateNoticeCleared": extremeNetsightAlarmNACCertificateNoticeCleared,
       "extremeNetsightAlarmNACCertificateExpiringNotice": extremeNetsightAlarmNACCertificateExpiringNotice,
       "extremeNetsightAlarmNACDuplicateSNMPEngineIDCleared": extremeNetsightAlarmNACDuplicateSNMPEngineIDCleared,
       "extremeNetsightAlarmNACDuplicateSNMPEngineIDFound": extremeNetsightAlarmNACDuplicateSNMPEngineIDFound,
       "extremeNetsightAlarmDeviceTopologyChange": extremeNetsightAlarmDeviceTopologyChange,
       "extremeNetsightAlarmDevicePercentCPU": extremeNetsightAlarmDevicePercentCPU,
       "extremeNetsightAlarmDeviceMemoryPercentUsage": extremeNetsightAlarmDeviceMemoryPercentUsage,
       "extremeNetsightAlarmHostPercentCPU": extremeNetsightAlarmHostPercentCPU,
       "extremeNetsightAlarmHostDiskPercentUsage": extremeNetsightAlarmHostDiskPercentUsage,
       "extremeNetsightAlarmHostMemoryPercentUsage": extremeNetsightAlarmHostMemoryPercentUsage,
       "extremeNetsightAlarmInterfacePercentUsage": extremeNetsightAlarmInterfacePercentUsage,
       "extremeNetsightAlarmInterfacePercentValidPackets": extremeNetsightAlarmInterfacePercentValidPackets,
       "extremeNetsightAlarmHistoricalPersistenceResumed": extremeNetsightAlarmHistoricalPersistenceResumed,
       "extremeNetsightAlarmHistoricalPersistenceSuspended": extremeNetsightAlarmHistoricalPersistenceSuspended,
       "extremeNetsightAlarmAnalyticsPersistenceResumed": extremeNetsightAlarmAnalyticsPersistenceResumed,
       "extremeNetsightAlarmAnalyticsPersistenceSuspended": extremeNetsightAlarmAnalyticsPersistenceSuspended,
       "extremeNetsightAlarmControllerEstablishedSSHConnection": extremeNetsightAlarmControllerEstablishedSSHConnection,
       "extremeNetsightAlarmControllerFailedSSHConnection": extremeNetsightAlarmControllerFailedSSHConnection,
       "extremeNetsightAlarmServerHeapMemoryOK": extremeNetsightAlarmServerHeapMemoryOK,
       "extremeNetsightAlarmServerHeapMemoryLow": extremeNetsightAlarmServerHeapMemoryLow,
       "extremeNetsightAlarmClientMACAvailabilityLow": extremeNetsightAlarmClientMACAvailabilityLow,
       "extremeNetsightAlarmClientMACIPChangesHigh": extremeNetsightAlarmClientMACIPChangesHigh,
       "extremeNetsightAlarmNACEntriesPerGroupPerfThresholdRectified": extremeNetsightAlarmNACEntriesPerGroupPerfThresholdRectified,
       "extremeNetsightAlarmNACEntriesPerGroupPerfThresholdExceeded": extremeNetsightAlarmNACEntriesPerGroupPerfThresholdExceeded,
       "extremeNetsightAlarmNACCertificateUsesMD5SignatureCleared": extremeNetsightAlarmNACCertificateUsesMD5SignatureCleared,
       "extremeNetsightAlarmNACCertificateUsesMD5SignatureNotice": extremeNetsightAlarmNACCertificateUsesMD5SignatureNotice,
       "extremeNetsightAlarmNACWinbinddProcessCleared": extremeNetsightAlarmNACWinbinddProcessCleared,
       "extremeNetsightAlarmNACWinbinddProcessDown": extremeNetsightAlarmNACWinbinddProcessDown,
       "extremeNetsightAlarmNACSquidProcessCleared": extremeNetsightAlarmNACSquidProcessCleared,
       "extremeNetsightAlarmNACSquidProcessDown": extremeNetsightAlarmNACSquidProcessDown,
       "extremeNetsightAlarmNACRadiusdProcessCleared": extremeNetsightAlarmNACRadiusdProcessCleared,
       "extremeNetsightAlarmNACRadiusdProcessDown": extremeNetsightAlarmNACRadiusdProcessDown,
       "extremeNetsightAlarmNACDnsproxyProcessCleared": extremeNetsightAlarmNACDnsproxyProcessCleared,
       "extremeNetsightAlarmNACDnsproxyProcessDown": extremeNetsightAlarmNACDnsproxyProcessDown,
       "extremeNetsightAlarmNACIPMICriticalEventCleared": extremeNetsightAlarmNACIPMICriticalEventCleared,
       "extremeNetsightAlarmNACIPMICriticalEvent": extremeNetsightAlarmNACIPMICriticalEvent,
       "extremeNetsightAlarmNACDNSServersUnreachableCleared": extremeNetsightAlarmNACDNSServersUnreachableCleared,
       "extremeNetsightAlarmNACDNSServersUnreachable": extremeNetsightAlarmNACDNSServersUnreachable,
       "extremeNetsightAlarmVars": extremeNetsightAlarmVars,
       "extremeNetsightAlarmMessage": extremeNetsightAlarmMessage,
       "extremeNetsightAlarmSeverity": extremeNetsightAlarmSeverity,
       "extremeNetsightAlarmTimestamp": extremeNetsightAlarmTimestamp,
       "extremeNetsightAlarmSourceDeviceAddressType": extremeNetsightAlarmSourceDeviceAddressType,
       "extremeNetsightAlarmSourceDeviceAddress": extremeNetsightAlarmSourceDeviceAddress,
       "extremeNetsightAlarmSubcomponent": extremeNetsightAlarmSubcomponent,
       "extremeNetsightAlarmConformance": extremeNetsightAlarmConformance,
       "extremeNetsightAlarmGroups": extremeNetsightAlarmGroups,
       "extremeNetsightAlarmSettings": extremeNetsightAlarmSettings,
       "extremeNetsightAlarmGenericNotificationGroup": extremeNetsightAlarmGenericNotificationGroup,
       "extremeNetsightAlarmSpecificNotificationGroup": extremeNetsightAlarmSpecificNotificationGroup,
       "extremeNetsightAlarmCompliances": extremeNetsightAlarmCompliances,
       "extremeNetsightAlarmComplianceGroup": extremeNetsightAlarmComplianceGroup}
)
