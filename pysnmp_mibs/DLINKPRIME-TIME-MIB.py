# SNMP MIB module (DLINKPRIME-TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-TIME-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:46:10 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeTimeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 23)
)
if mibBuilder.loadTexts:
    dlinkPrimeTimeMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DlinkTimeSummerTimeValue(TextualConvention, OctetString):
    status = "current"
    displayHint = "2d-1d-1d,1d:1d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



# MIB Managed Objects in the order of their OIDs

_DpTimeMIBNotifications_ObjectIdentity = ObjectIdentity
dpTimeMIBNotifications = _DpTimeMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 0)
)
_DpTimeMIBObjects_ObjectIdentity = ObjectIdentity
dpTimeMIBObjects = _DpTimeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1)
)
_DpTimeGeneral_ObjectIdentity = ObjectIdentity
dpTimeGeneral = _DpTimeGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 1)
)
_DpTimeSntpEnabled_Type = TruthValue
_DpTimeSntpEnabled_Object = MibScalar
dpTimeSntpEnabled = _DpTimeSntpEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 1, 1),
    _DpTimeSntpEnabled_Type()
)
dpTimeSntpEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTimeSntpEnabled.setStatus("current")


class _DpTimeSntpPollInterval_Type(Unsigned32):
    """Custom type dpTimeSntpPollInterval based on Unsigned32"""
    defaultValue = 720

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 99999),
    )


_DpTimeSntpPollInterval_Type.__name__ = "Unsigned32"
_DpTimeSntpPollInterval_Object = MibScalar
dpTimeSntpPollInterval = _DpTimeSntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 1, 2),
    _DpTimeSntpPollInterval_Type()
)
dpTimeSntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTimeSntpPollInterval.setStatus("current")
_DpTimeClock_ObjectIdentity = ObjectIdentity
dpTimeClock = _DpTimeClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2)
)
_DpTimeManagedClock_Type = DateAndTime
_DpTimeManagedClock_Object = MibScalar
dpTimeManagedClock = _DpTimeManagedClock_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 1),
    _DpTimeManagedClock_Type()
)
dpTimeManagedClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTimeManagedClock.setStatus("current")


class _DpTimeCurrentTimeSource_Type(Integer32):
    """Custom type dpTimeCurrentTimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sntp", 1),
          ("noTimeSource", 2))
    )


_DpTimeCurrentTimeSource_Type.__name__ = "Integer32"
_DpTimeCurrentTimeSource_Object = MibScalar
dpTimeCurrentTimeSource = _DpTimeCurrentTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 2),
    _DpTimeCurrentTimeSource_Type()
)
dpTimeCurrentTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpTimeCurrentTimeSource.setStatus("current")
_DpTimeCurrentTime_Type = DateAndTime
_DpTimeCurrentTime_Object = MibScalar
dpTimeCurrentTime = _DpTimeCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 3),
    _DpTimeCurrentTime_Type()
)
dpTimeCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpTimeCurrentTime.setStatus("current")
_DpTimeSummerTime_ObjectIdentity = ObjectIdentity
dpTimeSummerTime = _DpTimeSummerTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4)
)


class _DpTimeSummerTimeAutoSwitchMode_Type(Integer32):
    """Custom type dpTimeSummerTimeAutoSwitchMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("date", 2))
    )


_DpTimeSummerTimeAutoSwitchMode_Type.__name__ = "Integer32"
_DpTimeSummerTimeAutoSwitchMode_Object = MibScalar
dpTimeSummerTimeAutoSwitchMode = _DpTimeSummerTimeAutoSwitchMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4, 1),
    _DpTimeSummerTimeAutoSwitchMode_Type()
)
dpTimeSummerTimeAutoSwitchMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTimeSummerTimeAutoSwitchMode.setStatus("current")


class _DpTimeSummerTimeTimeZone_Type(Integer32):
    """Custom type dpTimeSummerTimeTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-779, 839),
    )


_DpTimeSummerTimeTimeZone_Type.__name__ = "Integer32"
_DpTimeSummerTimeTimeZone_Object = MibScalar
dpTimeSummerTimeTimeZone = _DpTimeSummerTimeTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4, 2),
    _DpTimeSummerTimeTimeZone_Type()
)
dpTimeSummerTimeTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTimeSummerTimeTimeZone.setStatus("current")
_DpTimeSummerTimeStart_Type = DlinkTimeSummerTimeValue
_DpTimeSummerTimeStart_Object = MibScalar
dpTimeSummerTimeStart = _DpTimeSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4, 3),
    _DpTimeSummerTimeStart_Type()
)
dpTimeSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTimeSummerTimeStart.setStatus("current")
_DpTimeSummerTimeEnd_Type = DlinkTimeSummerTimeValue
_DpTimeSummerTimeEnd_Object = MibScalar
dpTimeSummerTimeEnd = _DpTimeSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4, 4),
    _DpTimeSummerTimeEnd_Type()
)
dpTimeSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTimeSummerTimeEnd.setStatus("current")


class _DpTimeSummerTimeOffset_Type(Integer32):
    """Custom type dpTimeSummerTimeOffset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 30),
        ValueRangeConstraint(60, 60),
        ValueRangeConstraint(90, 90),
        ValueRangeConstraint(120, 120),
    )


_DpTimeSummerTimeOffset_Type.__name__ = "Integer32"
_DpTimeSummerTimeOffset_Object = MibScalar
dpTimeSummerTimeOffset = _DpTimeSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 2, 4, 5),
    _DpTimeSummerTimeOffset_Type()
)
dpTimeSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTimeSummerTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    dpTimeSummerTimeOffset.setUnits("Minutes")
_DpTimeServer_ObjectIdentity = ObjectIdentity
dpTimeServer = _DpTimeServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 3)
)
_DpTimeSntpServerAddr_Type = IpAddress
_DpTimeSntpServerAddr_Object = MibScalar
dpTimeSntpServerAddr = _DpTimeSntpServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 3, 1),
    _DpTimeSntpServerAddr_Type()
)
dpTimeSntpServerAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpTimeSntpServerAddr.setStatus("current")
_DpTimeSntpServerStratum_Type = Unsigned32
_DpTimeSntpServerStratum_Object = MibScalar
dpTimeSntpServerStratum = _DpTimeSntpServerStratum_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 3, 2),
    _DpTimeSntpServerStratum_Type()
)
dpTimeSntpServerStratum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpTimeSntpServerStratum.setStatus("current")
_DpTimeSntpServerVersion_Type = Unsigned32
_DpTimeSntpServerVersion_Object = MibScalar
dpTimeSntpServerVersion = _DpTimeSntpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 3, 3),
    _DpTimeSntpServerVersion_Type()
)
dpTimeSntpServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpTimeSntpServerVersion.setStatus("current")
_DpTimeSntpServerLastReceive_Type = Unsigned32
_DpTimeSntpServerLastReceive_Object = MibScalar
dpTimeSntpServerLastReceive = _DpTimeSntpServerLastReceive_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 1, 3, 4),
    _DpTimeSntpServerLastReceive_Type()
)
dpTimeSntpServerLastReceive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpTimeSntpServerLastReceive.setStatus("current")
if mibBuilder.loadTexts:
    dpTimeSntpServerLastReceive.setUnits("seconds")
_DpTimeMIBConformance_ObjectIdentity = ObjectIdentity
dpTimeMIBConformance = _DpTimeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 2)
)
_DpTimeCompliances_ObjectIdentity = ObjectIdentity
dpTimeCompliances = _DpTimeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 1)
)
_DpTimeGroups_ObjectIdentity = ObjectIdentity
dpTimeGroups = _DpTimeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 2)
)

# Managed Objects groups

dpTimeSysInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 2, 1)
)
dpTimeSysInfoGroup.setObjects(
      *(("DLINKPRIME-TIME-MIB", "dpTimeCurrentTimeSource"),
        ("DLINKPRIME-TIME-MIB", "dpTimeCurrentTime"))
)
if mibBuilder.loadTexts:
    dpTimeSysInfoGroup.setStatus("current")

dpTimeClockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 2, 2)
)
dpTimeClockGroup.setObjects(
    ("DLINKPRIME-TIME-MIB", "dpTimeManagedClock")
)
if mibBuilder.loadTexts:
    dpTimeClockGroup.setStatus("current")

dpTimeSntpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 2, 3)
)
dpTimeSntpGroup.setObjects(
      *(("DLINKPRIME-TIME-MIB", "dpTimeSntpEnabled"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSntpPollInterval"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSntpServerAddr"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSntpServerStratum"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSntpServerVersion"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSntpServerLastReceive"))
)
if mibBuilder.loadTexts:
    dpTimeSntpGroup.setStatus("current")

dpTimeSummerTimeCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 2, 4)
)
dpTimeSummerTimeCfgGroup.setObjects(
      *(("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeAutoSwitchMode"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeTimeZone"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeStart"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeEnd"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeOffset"))
)
if mibBuilder.loadTexts:
    dpTimeSummerTimeCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpTimeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 23, 2, 1, 1)
)
dpTimeCompliance.setObjects(
      *(("DLINKPRIME-TIME-MIB", "dpTimeSysInfoGroup"),
        ("DLINKPRIME-TIME-MIB", "dpTimeClockGroup"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSntpGroup"),
        ("DLINKPRIME-TIME-MIB", "dpTimeSummerTimeCfgGroup"))
)
if mibBuilder.loadTexts:
    dpTimeCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-TIME-MIB",
    **{"DlinkTimeSummerTimeValue": DlinkTimeSummerTimeValue,
       "dlinkPrimeTimeMIB": dlinkPrimeTimeMIB,
       "dpTimeMIBNotifications": dpTimeMIBNotifications,
       "dpTimeMIBObjects": dpTimeMIBObjects,
       "dpTimeGeneral": dpTimeGeneral,
       "dpTimeSntpEnabled": dpTimeSntpEnabled,
       "dpTimeSntpPollInterval": dpTimeSntpPollInterval,
       "dpTimeClock": dpTimeClock,
       "dpTimeManagedClock": dpTimeManagedClock,
       "dpTimeCurrentTimeSource": dpTimeCurrentTimeSource,
       "dpTimeCurrentTime": dpTimeCurrentTime,
       "dpTimeSummerTime": dpTimeSummerTime,
       "dpTimeSummerTimeAutoSwitchMode": dpTimeSummerTimeAutoSwitchMode,
       "dpTimeSummerTimeTimeZone": dpTimeSummerTimeTimeZone,
       "dpTimeSummerTimeStart": dpTimeSummerTimeStart,
       "dpTimeSummerTimeEnd": dpTimeSummerTimeEnd,
       "dpTimeSummerTimeOffset": dpTimeSummerTimeOffset,
       "dpTimeServer": dpTimeServer,
       "dpTimeSntpServerAddr": dpTimeSntpServerAddr,
       "dpTimeSntpServerStratum": dpTimeSntpServerStratum,
       "dpTimeSntpServerVersion": dpTimeSntpServerVersion,
       "dpTimeSntpServerLastReceive": dpTimeSntpServerLastReceive,
       "dpTimeMIBConformance": dpTimeMIBConformance,
       "dpTimeCompliances": dpTimeCompliances,
       "dpTimeCompliance": dpTimeCompliance,
       "dpTimeGroups": dpTimeGroups,
       "dpTimeSysInfoGroup": dpTimeSysInfoGroup,
       "dpTimeClockGroup": dpTimeClockGroup,
       "dpTimeSntpGroup": dpTimeSntpGroup,
       "dpTimeSummerTimeCfgGroup": dpTimeSummerTimeCfgGroup}
)
