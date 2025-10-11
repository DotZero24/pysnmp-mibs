# SNMP MIB module (TIME-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/TIME-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:51:53 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

(Ipv6Address,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6Address")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

swTimeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 10)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SwTimeCapacity_Type(Bits):
    """Custom type swTimeCapacity based on Bits"""
    namedValues = NamedValues(
        *(("systemTime", 0),
          ("sntp", 1),
          ("summerTime", 2),
          ("realTimeClock", 3))
    )

_SwTimeCapacity_Type.__name__ = "Bits"
_SwTimeCapacity_Object = MibScalar
swTimeCapacity = _SwTimeCapacity_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 1),
    _SwTimeCapacity_Type()
)
swTimeCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swTimeCapacity.setStatus("current")
_SwCurrentClock_Type = DateAndTime
_SwCurrentClock_Object = MibScalar
swCurrentClock = _SwCurrentClock_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 2),
    _SwCurrentClock_Type()
)
swCurrentClock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swCurrentClock.setStatus("current")
_SwClockLostOnReboot_Type = TruthValue
_SwClockLostOnReboot_Object = MibScalar
swClockLostOnReboot = _SwClockLostOnReboot_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 3),
    _SwClockLostOnReboot_Type()
)
swClockLostOnReboot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swClockLostOnReboot.setStatus("current")
_SwSystemTime_ObjectIdentity = ObjectIdentity
swSystemTime = _SwSystemTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 10)
)


class _SwSystemCurrentTime_Type(DisplayString):
    """Custom type swSystemCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwSystemCurrentTime_Type.__name__ = "DisplayString"
_SwSystemCurrentTime_Object = MibScalar
swSystemCurrentTime = _SwSystemCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 10, 1),
    _SwSystemCurrentTime_Type()
)
swSystemCurrentTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSystemCurrentTime.setStatus("current")


class _SwSystemUpTime_Type(DisplayString):
    """Custom type swSystemUpTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwSystemUpTime_Type.__name__ = "DisplayString"
_SwSystemUpTime_Object = MibScalar
swSystemUpTime = _SwSystemUpTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 10, 2),
    _SwSystemUpTime_Type()
)
swSystemUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSystemUpTime.setStatus("current")


class _SwSystemBootTime_Type(DisplayString):
    """Custom type swSystemBootTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_SwSystemBootTime_Type.__name__ = "DisplayString"
_SwSystemBootTime_Object = MibScalar
swSystemBootTime = _SwSystemBootTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 10, 3),
    _SwSystemBootTime_Type()
)
swSystemBootTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSystemBootTime.setStatus("current")


class _SwSystemTimeZone_Type(Integer32):
    """Custom type swSystemTimeZone based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-779, 839),
    )


_SwSystemTimeZone_Type.__name__ = "Integer32"
_SwSystemTimeZone_Object = MibScalar
swSystemTimeZone = _SwSystemTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 10, 4),
    _SwSystemTimeZone_Type()
)
swSystemTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSystemTimeZone.setStatus("current")
_SwSNTP_ObjectIdentity = ObjectIdentity
swSNTP = _SwSNTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 11)
)


class _SwSNTPState_Type(Integer32):
    """Custom type swSNTPState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("disabled", 2),
          ("enabled", 3))
    )


_SwSNTPState_Type.__name__ = "Integer32"
_SwSNTPState_Object = MibScalar
swSNTPState = _SwSNTPState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 1),
    _SwSNTPState_Type()
)
swSNTPState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSNTPState.setStatus("current")


class _SwSNTPTimeSource_Type(Integer32):
    """Custom type swSNTPTimeSource based on Integer32"""
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
        *(("system", 0),
          ("server1", 1),
          ("server2", 2),
          ("ipv6server1", 3),
          ("ipv6server2", 4))
    )


_SwSNTPTimeSource_Type.__name__ = "Integer32"
_SwSNTPTimeSource_Object = MibScalar
swSNTPTimeSource = _SwSNTPTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 2),
    _SwSNTPTimeSource_Type()
)
swSNTPTimeSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSNTPTimeSource.setStatus("current")
_SwSNTPServer1IPAddr_Type = IpAddress
_SwSNTPServer1IPAddr_Object = MibScalar
swSNTPServer1IPAddr = _SwSNTPServer1IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 3),
    _SwSNTPServer1IPAddr_Type()
)
swSNTPServer1IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSNTPServer1IPAddr.setStatus("current")
_SwSNTPServer2IPAddr_Type = IpAddress
_SwSNTPServer2IPAddr_Object = MibScalar
swSNTPServer2IPAddr = _SwSNTPServer2IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 4),
    _SwSNTPServer2IPAddr_Type()
)
swSNTPServer2IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSNTPServer2IPAddr.setStatus("current")


class _SwSNTPPollInterval_Type(Integer32):
    """Custom type swSNTPPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 99999),
    )


_SwSNTPPollInterval_Type.__name__ = "Integer32"
_SwSNTPPollInterval_Object = MibScalar
swSNTPPollInterval = _SwSNTPPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 5),
    _SwSNTPPollInterval_Type()
)
swSNTPPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSNTPPollInterval.setStatus("current")
_SwSNTPIPv6Server1IPAddr_Type = Ipv6Address
_SwSNTPIPv6Server1IPAddr_Object = MibScalar
swSNTPIPv6Server1IPAddr = _SwSNTPIPv6Server1IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 6),
    _SwSNTPIPv6Server1IPAddr_Type()
)
swSNTPIPv6Server1IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSNTPIPv6Server1IPAddr.setStatus("current")
_SwSNTPIPv6Server2IPAddr_Type = Ipv6Address
_SwSNTPIPv6Server2IPAddr_Object = MibScalar
swSNTPIPv6Server2IPAddr = _SwSNTPIPv6Server2IPAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 7),
    _SwSNTPIPv6Server2IPAddr_Type()
)
swSNTPIPv6Server2IPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSNTPIPv6Server2IPAddr.setStatus("current")


class _SwSNTPIPv6Server1InterfaceName_Type(DisplayString):
    """Custom type swSNTPIPv6Server1InterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwSNTPIPv6Server1InterfaceName_Type.__name__ = "DisplayString"
_SwSNTPIPv6Server1InterfaceName_Object = MibScalar
swSNTPIPv6Server1InterfaceName = _SwSNTPIPv6Server1InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 8),
    _SwSNTPIPv6Server1InterfaceName_Type()
)
swSNTPIPv6Server1InterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSNTPIPv6Server1InterfaceName.setStatus("current")


class _SwSNTPIPv6Server2InterfaceName_Type(DisplayString):
    """Custom type swSNTPIPv6Server2InterfaceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 12),
    )


_SwSNTPIPv6Server2InterfaceName_Type.__name__ = "DisplayString"
_SwSNTPIPv6Server2InterfaceName_Object = MibScalar
swSNTPIPv6Server2InterfaceName = _SwSNTPIPv6Server2InterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 11, 9),
    _SwSNTPIPv6Server2InterfaceName_Type()
)
swSNTPIPv6Server2InterfaceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSNTPIPv6Server2InterfaceName.setStatus("current")
_SwSummerTime_ObjectIdentity = ObjectIdentity
swSummerTime = _SwSummerTime_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 12)
)


class _SwSummerTimeStatus_Type(Integer32):
    """Custom type swSummerTimeStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("repeating", 1),
          ("annual", 2))
    )


_SwSummerTimeStatus_Type.__name__ = "Integer32"
_SwSummerTimeStatus_Object = MibScalar
swSummerTimeStatus = _SwSummerTimeStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 1),
    _SwSummerTimeStatus_Type()
)
swSummerTimeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSummerTimeStatus.setStatus("current")


class _SwSummerTimeOffset_Type(Integer32):
    """Custom type swSummerTimeOffset based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_SwSummerTimeOffset_Type.__name__ = "Integer32"
_SwSummerTimeOffset_Object = MibScalar
swSummerTimeOffset = _SwSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 2),
    _SwSummerTimeOffset_Type()
)
swSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swSummerTimeOffset.setStatus("current")
if mibBuilder.loadTexts:
    swSummerTimeOffset.setUnits("Minutes")


class _SwRepeatSummerTimeStart_Type(OctetString):
    """Custom type swRepeatSummerTimeStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SwRepeatSummerTimeStart_Type.__name__ = "OctetString"
_SwRepeatSummerTimeStart_Object = MibScalar
swRepeatSummerTimeStart = _SwRepeatSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 3),
    _SwRepeatSummerTimeStart_Type()
)
swRepeatSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRepeatSummerTimeStart.setStatus("current")


class _SwRepeatSummerTimeEnd_Type(OctetString):
    """Custom type swRepeatSummerTimeEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SwRepeatSummerTimeEnd_Type.__name__ = "OctetString"
_SwRepeatSummerTimeEnd_Object = MibScalar
swRepeatSummerTimeEnd = _SwRepeatSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 4),
    _SwRepeatSummerTimeEnd_Type()
)
swRepeatSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swRepeatSummerTimeEnd.setStatus("current")


class _SwAnnualSummerTimeStart_Type(OctetString):
    """Custom type swAnnualSummerTimeStart based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SwAnnualSummerTimeStart_Type.__name__ = "OctetString"
_SwAnnualSummerTimeStart_Object = MibScalar
swAnnualSummerTimeStart = _SwAnnualSummerTimeStart_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 5),
    _SwAnnualSummerTimeStart_Type()
)
swAnnualSummerTimeStart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAnnualSummerTimeStart.setStatus("current")


class _SwAnnualSummerTimeEnd_Type(OctetString):
    """Custom type swAnnualSummerTimeEnd based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_SwAnnualSummerTimeEnd_Type.__name__ = "OctetString"
_SwAnnualSummerTimeEnd_Object = MibScalar
swAnnualSummerTimeEnd = _SwAnnualSummerTimeEnd_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 12, 6),
    _SwAnnualSummerTimeEnd_Type()
)
swAnnualSummerTimeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swAnnualSummerTimeEnd.setStatus("current")
_SwTimeNotifPrefix_ObjectIdentity = ObjectIdentity
swTimeNotifPrefix = _SwTimeNotifPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 10, 13)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIME-MIB",
    **{"swTimeMIB": swTimeMIB,
       "swTimeCapacity": swTimeCapacity,
       "swCurrentClock": swCurrentClock,
       "swClockLostOnReboot": swClockLostOnReboot,
       "swSystemTime": swSystemTime,
       "swSystemCurrentTime": swSystemCurrentTime,
       "swSystemUpTime": swSystemUpTime,
       "swSystemBootTime": swSystemBootTime,
       "swSystemTimeZone": swSystemTimeZone,
       "swSNTP": swSNTP,
       "swSNTPState": swSNTPState,
       "swSNTPTimeSource": swSNTPTimeSource,
       "swSNTPServer1IPAddr": swSNTPServer1IPAddr,
       "swSNTPServer2IPAddr": swSNTPServer2IPAddr,
       "swSNTPPollInterval": swSNTPPollInterval,
       "swSNTPIPv6Server1IPAddr": swSNTPIPv6Server1IPAddr,
       "swSNTPIPv6Server2IPAddr": swSNTPIPv6Server2IPAddr,
       "swSNTPIPv6Server1InterfaceName": swSNTPIPv6Server1InterfaceName,
       "swSNTPIPv6Server2InterfaceName": swSNTPIPv6Server2InterfaceName,
       "swSummerTime": swSummerTime,
       "swSummerTimeStatus": swSummerTimeStatus,
       "swSummerTimeOffset": swSummerTimeOffset,
       "swRepeatSummerTimeStart": swRepeatSummerTimeStart,
       "swRepeatSummerTimeEnd": swRepeatSummerTimeEnd,
       "swAnnualSummerTimeStart": swAnnualSummerTimeStart,
       "swAnnualSummerTimeEnd": swAnnualSummerTimeEnd,
       "swTimeNotifPrefix": swTimeNotifPrefix}
)
