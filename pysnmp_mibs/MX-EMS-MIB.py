# SNMP MIB module (MX-EMS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-EMS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:29 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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

emsMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EmsMIBObjects_ObjectIdentity = ObjectIdentity
emsMIBObjects = _EmsMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1)
)
_ProvisioningGroup_ObjectIdentity = ObjectIdentity
provisioningGroup = _ProvisioningGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 100)
)


class _EmsProvisioningEnable_Type(MxEnableState):
    """Custom type emsProvisioningEnable based on MxEnableState"""
    defaultValue = 0


_EmsProvisioningEnable_Type.__name__ = "MxEnableState"
_EmsProvisioningEnable_Object = MibScalar
emsProvisioningEnable = _EmsProvisioningEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 100, 100),
    _EmsProvisioningEnable_Type()
)
emsProvisioningEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    emsProvisioningEnable.setStatus("current")


class _PeriodicProvisioningTimer_Type(OctetString):
    """Custom type periodicProvisioningTimer based on OctetString"""
    defaultValue = OctetString("daily")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 250),
    )


_PeriodicProvisioningTimer_Type.__name__ = "OctetString"
_PeriodicProvisioningTimer_Object = MibScalar
periodicProvisioningTimer = _PeriodicProvisioningTimer_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 100, 200),
    _PeriodicProvisioningTimer_Type()
)
periodicProvisioningTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    periodicProvisioningTimer.setStatus("current")
_TimersGroup_ObjectIdentity = ObjectIdentity
timersGroup = _TimersGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 150)
)


class _HourlyTimeRange_Type(OctetString):
    """Custom type hourlyTimeRange based on OctetString"""
    defaultValue = OctetString("55 - 05")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_HourlyTimeRange_Type.__name__ = "OctetString"
_HourlyTimeRange_Object = MibScalar
hourlyTimeRange = _HourlyTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 150, 100),
    _HourlyTimeRange_Type()
)
hourlyTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hourlyTimeRange.setStatus("current")


class _DailyTimeRange_Type(OctetString):
    """Custom type dailyTimeRange based on OctetString"""
    defaultValue = OctetString("01:00 - 03:00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_DailyTimeRange_Type.__name__ = "OctetString"
_DailyTimeRange_Object = MibScalar
dailyTimeRange = _DailyTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 150, 200),
    _DailyTimeRange_Type()
)
dailyTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dailyTimeRange.setStatus("current")


class _WeeklyTimeRange_Type(OctetString):
    """Custom type weeklyTimeRange based on OctetString"""
    defaultValue = OctetString("Monday 01:00 - Monday 03:00")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 50),
    )


_WeeklyTimeRange_Type.__name__ = "OctetString"
_WeeklyTimeRange_Object = MibScalar
weeklyTimeRange = _WeeklyTimeRange_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 150, 300),
    _WeeklyTimeRange_Type()
)
weeklyTimeRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    weeklyTimeRange.setStatus("current")
_StatusGroup_ObjectIdentity = ObjectIdentity
statusGroup = _StatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 200)
)


class _LastConnectionDateTime_Type(OctetString):
    """Custom type lastConnectionDateTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_LastConnectionDateTime_Type.__name__ = "OctetString"
_LastConnectionDateTime_Object = MibScalar
lastConnectionDateTime = _LastConnectionDateTime_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 200, 100),
    _LastConnectionDateTime_Type()
)
lastConnectionDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastConnectionDateTime.setStatus("current")


class _LastProvisioningResult_Type(Integer32):
    """Custom type lastProvisioningResult based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400,
              500,
              600)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("success", 200),
          ("partiallyProvisioned", 300),
          ("connectionFailed", 400),
          ("provisioningError", 500),
          ("unmanagedUnit", 600))
    )


_LastProvisioningResult_Type.__name__ = "Integer32"
_LastProvisioningResult_Object = MibScalar
lastProvisioningResult = _LastProvisioningResult_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 200, 200),
    _LastProvisioningResult_Type()
)
lastProvisioningResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lastProvisioningResult.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 4700, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-EMS-MIB",
    **{"emsMIB": emsMIB,
       "emsMIBObjects": emsMIBObjects,
       "provisioningGroup": provisioningGroup,
       "emsProvisioningEnable": emsProvisioningEnable,
       "periodicProvisioningTimer": periodicProvisioningTimer,
       "timersGroup": timersGroup,
       "hourlyTimeRange": hourlyTimeRange,
       "dailyTimeRange": dailyTimeRange,
       "weeklyTimeRange": weeklyTimeRange,
       "statusGroup": statusGroup,
       "lastConnectionDateTime": lastConnectionDateTime,
       "lastProvisioningResult": lastProvisioningResult,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
