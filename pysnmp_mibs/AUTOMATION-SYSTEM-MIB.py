# SNMP MIB module (AUTOMATION-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/AUTOMATION-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:47 2025
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

(automationMgmt,) = mibBuilder.importSymbols(
    "AUTOMATION-SMI",
    "automationMgmt")

(AutomationFunctionStringTC,
 AutomationLocationStringTC,
 AutomationOrderNumberTC,
 AutomationSerialNumberTC,
 AutomationTriggerTC,
 AutomationVersionNumberTC) = mibBuilder.importSymbols(
    "AUTOMATION-TC",
    "AutomationFunctionStringTC",
    "AutomationLocationStringTC",
    "AutomationOrderNumberTC",
    "AutomationSerialNumberTC",
    "AutomationTriggerTC",
    "AutomationVersionNumberTC")

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

automationSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2)
)
if mibBuilder.loadTexts:
    automationSystemMIB.setRevisions(
        ("2013-08-27 00:00",
         "2013-06-25 00:00",
         "2012-07-01 00:00",
         "2012-06-01 00:00",
         "2009-03-10 00:00",
         "2008-11-10 00:00",
         "2008-04-29 00:00",
         "2005-01-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AutomationSystemObjects_ObjectIdentity = ObjectIdentity
automationSystemObjects = _AutomationSystemObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1)
)
_AutomationSystemIdent_ObjectIdentity = ObjectIdentity
automationSystemIdent = _AutomationSystemIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1)
)


class _AutomationManufacturerId_Type(Unsigned32):
    """Custom type automationManufacturerId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AutomationManufacturerId_Type.__name__ = "Unsigned32"
_AutomationManufacturerId_Object = MibScalar
automationManufacturerId = _AutomationManufacturerId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 1),
    _AutomationManufacturerId_Type()
)
automationManufacturerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationManufacturerId.setStatus("current")
_AutomationOrderNumber_Type = AutomationOrderNumberTC
_AutomationOrderNumber_Object = MibScalar
automationOrderNumber = _AutomationOrderNumber_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 2),
    _AutomationOrderNumber_Type()
)
automationOrderNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationOrderNumber.setStatus("current")
_AutomationSerialNumber_Type = AutomationSerialNumberTC
_AutomationSerialNumber_Object = MibScalar
automationSerialNumber = _AutomationSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 3),
    _AutomationSerialNumber_Type()
)
automationSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationSerialNumber.setStatus("current")
_AutomationHwRevision_Type = AutomationVersionNumberTC
_AutomationHwRevision_Object = MibScalar
automationHwRevision = _AutomationHwRevision_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 4),
    _AutomationHwRevision_Type()
)
automationHwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationHwRevision.setStatus("current")
_AutomationSwRevision_Type = AutomationVersionNumberTC
_AutomationSwRevision_Object = MibScalar
automationSwRevision = _AutomationSwRevision_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 5),
    _AutomationSwRevision_Type()
)
automationSwRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationSwRevision.setStatus("current")
_AutomationRevisionCounter_Type = Counter32
_AutomationRevisionCounter_Object = MibScalar
automationRevisionCounter = _AutomationRevisionCounter_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 6),
    _AutomationRevisionCounter_Type()
)
automationRevisionCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationRevisionCounter.setStatus("current")
_AutomationRevisionDate_Type = DateAndTime
_AutomationRevisionDate_Object = MibScalar
automationRevisionDate = _AutomationRevisionDate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 7),
    _AutomationRevisionDate_Type()
)
automationRevisionDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationRevisionDate.setStatus("current")
_AutomationFunctionTag_Type = AutomationFunctionStringTC
_AutomationFunctionTag_Object = MibScalar
automationFunctionTag = _AutomationFunctionTag_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 8),
    _AutomationFunctionTag_Type()
)
automationFunctionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationFunctionTag.setStatus("current")
_AutomationLocationTag_Type = AutomationLocationStringTC
_AutomationLocationTag_Object = MibScalar
automationLocationTag = _AutomationLocationTag_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 9),
    _AutomationLocationTag_Type()
)
automationLocationTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationLocationTag.setStatus("current")
_AutomationGeoLatitude_Type = DisplayString
_AutomationGeoLatitude_Object = MibScalar
automationGeoLatitude = _AutomationGeoLatitude_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 10),
    _AutomationGeoLatitude_Type()
)
automationGeoLatitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationGeoLatitude.setStatus("current")
_AutomationGeoLongitude_Type = DisplayString
_AutomationGeoLongitude_Object = MibScalar
automationGeoLongitude = _AutomationGeoLongitude_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 11),
    _AutomationGeoLongitude_Type()
)
automationGeoLongitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationGeoLongitude.setStatus("current")
_AutomationGeoHeight_Type = DisplayString
_AutomationGeoHeight_Object = MibScalar
automationGeoHeight = _AutomationGeoHeight_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 12),
    _AutomationGeoHeight_Type()
)
automationGeoHeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationGeoHeight.setStatus("current")


class _AutomationTimeZoneOffsetHours_Type(Integer32):
    """Custom type automationTimeZoneOffsetHours based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-23, 23),
    )


_AutomationTimeZoneOffsetHours_Type.__name__ = "Integer32"
_AutomationTimeZoneOffsetHours_Object = MibScalar
automationTimeZoneOffsetHours = _AutomationTimeZoneOffsetHours_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 13),
    _AutomationTimeZoneOffsetHours_Type()
)
automationTimeZoneOffsetHours.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationTimeZoneOffsetHours.setStatus("current")


class _AutomationTimeZoneOffsetMinutes_Type(Integer32):
    """Custom type automationTimeZoneOffsetMinutes based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-59, 59),
    )


_AutomationTimeZoneOffsetMinutes_Type.__name__ = "Integer32"
_AutomationTimeZoneOffsetMinutes_Object = MibScalar
automationTimeZoneOffsetMinutes = _AutomationTimeZoneOffsetMinutes_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 14),
    _AutomationTimeZoneOffsetMinutes_Type()
)
automationTimeZoneOffsetMinutes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationTimeZoneOffsetMinutes.setStatus("current")
_AutomationSwUser_Type = DisplayString
_AutomationSwUser_Object = MibScalar
automationSwUser = _AutomationSwUser_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 15),
    _AutomationSwUser_Type()
)
automationSwUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationSwUser.setStatus("current")
_AutomationSwDate_Type = DateAndTime
_AutomationSwDate_Object = MibScalar
automationSwDate = _AutomationSwDate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 1, 16),
    _AutomationSwDate_Type()
)
automationSwDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationSwDate.setStatus("current")
_AutomationSystemStatus_ObjectIdentity = ObjectIdentity
automationSystemStatus = _AutomationSystemStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 2)
)


class _AutomationOperState_Type(Integer32):
    """Custom type automationOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 0),
          ("maintenanceRequired", 1),
          ("maintenanceDemanded", 2),
          ("fault", 3))
    )


_AutomationOperState_Type.__name__ = "Integer32"
_AutomationOperState_Object = MibScalar
automationOperState = _AutomationOperState_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 2, 1),
    _AutomationOperState_Type()
)
automationOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationOperState.setStatus("current")


class _AutomationApplicationOperState_Type(Integer32):
    """Custom type automationApplicationOperState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noControl", 1),
          ("run", 2),
          ("stop", 3))
    )


_AutomationApplicationOperState_Type.__name__ = "Integer32"
_AutomationApplicationOperState_Object = MibScalar
automationApplicationOperState = _AutomationApplicationOperState_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 2, 2),
    _AutomationApplicationOperState_Type()
)
automationApplicationOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationApplicationOperState.setStatus("current")
_AutomationSystemGeneric_ObjectIdentity = ObjectIdentity
automationSystemGeneric = _AutomationSystemGeneric_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 3)
)


class _AutomationSystemRestart_Type(Integer32):
    """Custom type automationSystemRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("noOperation", 0),
          ("coldstart", 1),
          ("warmstart", 2),
          ("restartBasicDefaults", 3),
          ("restartCompleteDefaults", 4))
    )


_AutomationSystemRestart_Type.__name__ = "Integer32"
_AutomationSystemRestart_Object = MibScalar
automationSystemRestart = _AutomationSystemRestart_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 3, 1),
    _AutomationSystemRestart_Type()
)
automationSystemRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationSystemRestart.setStatus("current")
_AutomationPowerUpCount_Type = Counter32
_AutomationPowerUpCount_Object = MibScalar
automationPowerUpCount = _AutomationPowerUpCount_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 3, 3),
    _AutomationPowerUpCount_Type()
)
automationPowerUpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationPowerUpCount.setStatus("current")
_AutomationResetCounters_Type = AutomationTriggerTC
_AutomationResetCounters_Object = MibScalar
automationResetCounters = _AutomationResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 3, 4),
    _AutomationResetCounters_Type()
)
automationResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationResetCounters.setStatus("current")


class _AutomationConfigId_Type(OctetString):
    """Custom type automationConfigId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(64, 64),
    )
    fixed_length = 64


_AutomationConfigId_Type.__name__ = "OctetString"
_AutomationConfigId_Object = MibScalar
automationConfigId = _AutomationConfigId_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 3, 5),
    _AutomationConfigId_Type()
)
automationConfigId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationConfigId.setStatus("current")
_AutomationConfigUser_Type = DisplayString
_AutomationConfigUser_Object = MibScalar
automationConfigUser = _AutomationConfigUser_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 3, 6),
    _AutomationConfigUser_Type()
)
automationConfigUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationConfigUser.setStatus("current")
_AutomationConfigDate_Type = DateAndTime
_AutomationConfigDate_Object = MibScalar
automationConfigDate = _AutomationConfigDate_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 3, 7),
    _AutomationConfigDate_Type()
)
automationConfigDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    automationConfigDate.setStatus("current")
_AutomationSystemIp_ObjectIdentity = ObjectIdentity
automationSystemIp = _AutomationSystemIp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 4)
)
_AutomationSystemIpAddress_Type = IpAddress
_AutomationSystemIpAddress_Object = MibScalar
automationSystemIpAddress = _AutomationSystemIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 4, 1),
    _AutomationSystemIpAddress_Type()
)
automationSystemIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationSystemIpAddress.setStatus("deprecated")
_AutomationSystemIpSubnetMask_Type = IpAddress
_AutomationSystemIpSubnetMask_Object = MibScalar
automationSystemIpSubnetMask = _AutomationSystemIpSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 4, 2),
    _AutomationSystemIpSubnetMask_Type()
)
automationSystemIpSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationSystemIpSubnetMask.setStatus("deprecated")
_AutomationSystemIpGateway_Type = IpAddress
_AutomationSystemIpGateway_Object = MibScalar
automationSystemIpGateway = _AutomationSystemIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 4, 3),
    _AutomationSystemIpGateway_Type()
)
automationSystemIpGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationSystemIpGateway.setStatus("deprecated")
_AutomationSystemOutbandIp_Type = IpAddress
_AutomationSystemOutbandIp_Object = MibScalar
automationSystemOutbandIp = _AutomationSystemOutbandIp_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 4, 4),
    _AutomationSystemOutbandIp_Type()
)
automationSystemOutbandIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationSystemOutbandIp.setStatus("deprecated")
_AutomationSystemOutbandSubnetMask_Type = IpAddress
_AutomationSystemOutbandSubnetMask_Object = MibScalar
automationSystemOutbandSubnetMask = _AutomationSystemOutbandSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 1, 4, 5),
    _AutomationSystemOutbandSubnetMask_Type()
)
automationSystemOutbandSubnetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    automationSystemOutbandSubnetMask.setStatus("deprecated")
_AutomationSystemNotifications_ObjectIdentity = ObjectIdentity
automationSystemNotifications = _AutomationSystemNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 2)
)
_AutomationSystemNotificationsV2_ObjectIdentity = ObjectIdentity
automationSystemNotificationsV2 = _AutomationSystemNotificationsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 2, 0)
)
_AutomationSystemConformance_ObjectIdentity = ObjectIdentity
automationSystemConformance = _AutomationSystemConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3)
)
_AutomationSystemGroups_ObjectIdentity = ObjectIdentity
automationSystemGroups = _AutomationSystemGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1)
)
_AutomationSystemCompliances_ObjectIdentity = ObjectIdentity
automationSystemCompliances = _AutomationSystemCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 2)
)

# Managed Objects groups

automationIM0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 1)
)
automationIM0Group.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationManufacturerId"),
        ("AUTOMATION-SYSTEM-MIB", "automationOrderNumber"),
        ("AUTOMATION-SYSTEM-MIB", "automationSerialNumber"),
        ("AUTOMATION-SYSTEM-MIB", "automationHwRevision"),
        ("AUTOMATION-SYSTEM-MIB", "automationSwRevision"),
        ("AUTOMATION-SYSTEM-MIB", "automationRevisionCounter"))
)
if mibBuilder.loadTexts:
    automationIM0Group.setStatus("current")

automationIM1Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 2)
)
automationIM1Group.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationFunctionTag"),
        ("AUTOMATION-SYSTEM-MIB", "automationLocationTag"))
)
if mibBuilder.loadTexts:
    automationIM1Group.setStatus("current")

automationIM2Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 3)
)
automationIM2Group.setObjects(
    ("AUTOMATION-SYSTEM-MIB", "automationRevisionDate")
)
if mibBuilder.loadTexts:
    automationIM2Group.setStatus("current")

automationStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 4)
)
automationStatusGroup.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationOperState"),
        ("AUTOMATION-SYSTEM-MIB", "automationApplicationOperState"))
)
if mibBuilder.loadTexts:
    automationStatusGroup.setStatus("current")

automationRemoteRestartGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 5)
)
automationRemoteRestartGroup.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationSystemRestart"),
        ("AUTOMATION-SYSTEM-MIB", "automationPowerUpCount"))
)
if mibBuilder.loadTexts:
    automationRemoteRestartGroup.setStatus("current")

automationResetCounterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 6)
)
automationResetCounterGroup.setObjects(
    ("AUTOMATION-SYSTEM-MIB", "automationResetCounters")
)
if mibBuilder.loadTexts:
    automationResetCounterGroup.setStatus("current")

automationIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 7)
)
automationIpGroup.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationSystemIpAddress"),
        ("AUTOMATION-SYSTEM-MIB", "automationSystemIpSubnetMask"),
        ("AUTOMATION-SYSTEM-MIB", "automationSystemIpGateway"))
)
if mibBuilder.loadTexts:
    automationIpGroup.setStatus("deprecated")

automationOutbandGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 8)
)
automationOutbandGroup.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationSystemOutbandIp"),
        ("AUTOMATION-SYSTEM-MIB", "automationSystemOutbandSubnetMask"))
)
if mibBuilder.loadTexts:
    automationOutbandGroup.setStatus("deprecated")

automationGeoLocation = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 11)
)
automationGeoLocation.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationGeoLatitude"),
        ("AUTOMATION-SYSTEM-MIB", "automationGeoLongitude"),
        ("AUTOMATION-SYSTEM-MIB", "automationGeoHeight"))
)
if mibBuilder.loadTexts:
    automationGeoLocation.setStatus("current")

automationGeoLocationTimeShift = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 12)
)
automationGeoLocationTimeShift.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationGeoLatitude"),
        ("AUTOMATION-SYSTEM-MIB", "automationGeoLongitude"),
        ("AUTOMATION-SYSTEM-MIB", "automationGeoHeight"),
        ("AUTOMATION-SYSTEM-MIB", "automationTimeZoneOffsetHours"),
        ("AUTOMATION-SYSTEM-MIB", "automationTimeZoneOffsetMinutes"))
)
if mibBuilder.loadTexts:
    automationGeoLocationTimeShift.setStatus("current")

automationConfigIdGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 13)
)
automationConfigIdGroup.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationConfigId"),
        ("AUTOMATION-SYSTEM-MIB", "automationConfigUser"),
        ("AUTOMATION-SYSTEM-MIB", "automationConfigDate"))
)
if mibBuilder.loadTexts:
    automationConfigIdGroup.setStatus("current")

automationSwDownloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 14)
)
automationSwDownloadGroup.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationSwUser"),
        ("AUTOMATION-SYSTEM-MIB", "automationSwDate"))
)
if mibBuilder.loadTexts:
    automationSwDownloadGroup.setStatus("current")


# Notification objects

automationOperStateChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 2, 0, 1)
)
automationOperStateChanged.setObjects(
    ("AUTOMATION-SYSTEM-MIB", "automationOperState")
)
if mibBuilder.loadTexts:
    automationOperStateChanged.setStatus(
        "current"
    )

automationRevisionChanged = NotificationType(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 2, 0, 2)
)
if mibBuilder.loadTexts:
    automationRevisionChanged.setStatus(
        "current"
    )


# Notifications groups

automationStatusEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 9)
)
automationStatusEvents.setObjects(
    ("AUTOMATION-SYSTEM-MIB", "automationOperStateChanged")
)
if mibBuilder.loadTexts:
    automationStatusEvents.setStatus(
        "current"
    )

automationConfigurationEvents = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 1, 10)
)
automationConfigurationEvents.setObjects(
    ("AUTOMATION-SYSTEM-MIB", "automationRevisionChanged")
)
if mibBuilder.loadTexts:
    automationConfigurationEvents.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

automationSystemBasicCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 2, 1)
)
automationSystemBasicCompliance.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationIM0Group"),
        ("AUTOMATION-SYSTEM-MIB", "automationIM1Group"),
        ("AUTOMATION-SYSTEM-MIB", "automationIM2Group"),
        ("AUTOMATION-SYSTEM-MIB", "automationStatusGroup"),
        ("AUTOMATION-SYSTEM-MIB", "automationResetCounterGroup"))
)
if mibBuilder.loadTexts:
    automationSystemBasicCompliance.setStatus(
        "current"
    )

automationSystemExtCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 2, 2)
)
automationSystemExtCompliance.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationIM0Group"),
        ("AUTOMATION-SYSTEM-MIB", "automationIM1Group"),
        ("AUTOMATION-SYSTEM-MIB", "automationIM2Group"),
        ("AUTOMATION-SYSTEM-MIB", "automationIpGroup"),
        ("AUTOMATION-SYSTEM-MIB", "automationOutbandGroup"),
        ("AUTOMATION-SYSTEM-MIB", "automationRemoteRestartGroup"),
        ("AUTOMATION-SYSTEM-MIB", "automationStatusGroup"),
        ("AUTOMATION-SYSTEM-MIB", "automationResetCounterGroup"),
        ("AUTOMATION-SYSTEM-MIB", "automationConfigurationEvents"),
        ("AUTOMATION-SYSTEM-MIB", "automationStatusEvents"),
        ("AUTOMATION-SYSTEM-MIB", "automationGeoLocation"),
        ("AUTOMATION-SYSTEM-MIB", "automationGeoLocationTimeShift"))
)
if mibBuilder.loadTexts:
    automationSystemExtCompliance.setStatus(
        "deprecated"
    )

automationSystemExtCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3, 2, 3, 2, 3)
)
automationSystemExtCompliance2.setObjects(
      *(("AUTOMATION-SYSTEM-MIB", "automationIM0Group"),
        ("AUTOMATION-SYSTEM-MIB", "automationIM1Group"),
        ("AUTOMATION-SYSTEM-MIB", "automationIM2Group"),
        ("AUTOMATION-SYSTEM-MIB", "automationRemoteRestartGroup"),
        ("AUTOMATION-SYSTEM-MIB", "automationStatusGroup"),
        ("AUTOMATION-SYSTEM-MIB", "automationResetCounterGroup"),
        ("AUTOMATION-SYSTEM-MIB", "automationConfigurationEvents"),
        ("AUTOMATION-SYSTEM-MIB", "automationStatusEvents"),
        ("AUTOMATION-SYSTEM-MIB", "automationGeoLocation"),
        ("AUTOMATION-SYSTEM-MIB", "automationGeoLocationTimeShift"),
        ("AUTOMATION-SYSTEM-MIB", "automationConfigIdGroup"),
        ("AUTOMATION-SYSTEM-MIB", "automationSwDownloadGroup"))
)
if mibBuilder.loadTexts:
    automationSystemExtCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AUTOMATION-SYSTEM-MIB",
    **{"automationSystemMIB": automationSystemMIB,
       "automationSystemObjects": automationSystemObjects,
       "automationSystemIdent": automationSystemIdent,
       "automationManufacturerId": automationManufacturerId,
       "automationOrderNumber": automationOrderNumber,
       "automationSerialNumber": automationSerialNumber,
       "automationHwRevision": automationHwRevision,
       "automationSwRevision": automationSwRevision,
       "automationRevisionCounter": automationRevisionCounter,
       "automationRevisionDate": automationRevisionDate,
       "automationFunctionTag": automationFunctionTag,
       "automationLocationTag": automationLocationTag,
       "automationGeoLatitude": automationGeoLatitude,
       "automationGeoLongitude": automationGeoLongitude,
       "automationGeoHeight": automationGeoHeight,
       "automationTimeZoneOffsetHours": automationTimeZoneOffsetHours,
       "automationTimeZoneOffsetMinutes": automationTimeZoneOffsetMinutes,
       "automationSwUser": automationSwUser,
       "automationSwDate": automationSwDate,
       "automationSystemStatus": automationSystemStatus,
       "automationOperState": automationOperState,
       "automationApplicationOperState": automationApplicationOperState,
       "automationSystemGeneric": automationSystemGeneric,
       "automationSystemRestart": automationSystemRestart,
       "automationPowerUpCount": automationPowerUpCount,
       "automationResetCounters": automationResetCounters,
       "automationConfigId": automationConfigId,
       "automationConfigUser": automationConfigUser,
       "automationConfigDate": automationConfigDate,
       "automationSystemIp": automationSystemIp,
       "automationSystemIpAddress": automationSystemIpAddress,
       "automationSystemIpSubnetMask": automationSystemIpSubnetMask,
       "automationSystemIpGateway": automationSystemIpGateway,
       "automationSystemOutbandIp": automationSystemOutbandIp,
       "automationSystemOutbandSubnetMask": automationSystemOutbandSubnetMask,
       "automationSystemNotifications": automationSystemNotifications,
       "automationSystemNotificationsV2": automationSystemNotificationsV2,
       "automationOperStateChanged": automationOperStateChanged,
       "automationRevisionChanged": automationRevisionChanged,
       "automationSystemConformance": automationSystemConformance,
       "automationSystemGroups": automationSystemGroups,
       "automationIM0Group": automationIM0Group,
       "automationIM1Group": automationIM1Group,
       "automationIM2Group": automationIM2Group,
       "automationStatusGroup": automationStatusGroup,
       "automationRemoteRestartGroup": automationRemoteRestartGroup,
       "automationResetCounterGroup": automationResetCounterGroup,
       "automationIpGroup": automationIpGroup,
       "automationOutbandGroup": automationOutbandGroup,
       "automationStatusEvents": automationStatusEvents,
       "automationConfigurationEvents": automationConfigurationEvents,
       "automationGeoLocation": automationGeoLocation,
       "automationGeoLocationTimeShift": automationGeoLocationTimeShift,
       "automationConfigIdGroup": automationConfigIdGroup,
       "automationSwDownloadGroup": automationSwDownloadGroup,
       "automationSystemCompliances": automationSystemCompliances,
       "automationSystemBasicCompliance": automationSystemBasicCompliance,
       "automationSystemExtCompliance": automationSystemExtCompliance,
       "automationSystemExtCompliance2": automationSystemExtCompliance2}
)
