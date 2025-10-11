# SNMP MIB module (FS-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-NTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:15:39 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49)
)
if mibBuilder.loadTexts:
    fsNtpMIB.setRevisions(
        ("2009-05-14 00:00",)
    )


# Types definitions



class NTPTimeStamp(OctetString):
    """Custom type NTPTimeStamp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8





class NTPLeapIndicator(Integer32):
    """Custom type NTPLeapIndicator based on Integer32"""
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
        *(("noWarning", 0),
          ("addSecond", 1),
          ("subtractSecond", 2),
          ("alarm", 3))
    )





class NTPSignedTimeValue(OctetString):
    """Custom type NTPSignedTimeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4





class NTPUnsignedTimeValue(OctetString):
    """Custom type NTPUnsignedTimeValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4





class NTPStratum(Integer32):
    """Custom type NTPStratum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )





class NTPRefId(OctetString):
    """Custom type NTPRefId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsNtpMIBObjects_ObjectIdentity = ObjectIdentity
fsNtpMIBObjects = _FsNtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1)
)
_FsntpSystem_ObjectIdentity = ObjectIdentity
fsntpSystem = _FsntpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1)
)
_FsntpSysLeap_Type = NTPLeapIndicator
_FsntpSysLeap_Object = MibScalar
fsntpSysLeap = _FsntpSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 1),
    _FsntpSysLeap_Type()
)
fsntpSysLeap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsntpSysLeap.setStatus("current")
_FsntpSysStratum_Type = NTPStratum
_FsntpSysStratum_Object = MibScalar
fsntpSysStratum = _FsntpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 2),
    _FsntpSysStratum_Type()
)
fsntpSysStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsntpSysStratum.setStatus("current")


class _FsntpSysPrecision_Type(Integer32):
    """Custom type fsntpSysPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )


_FsntpSysPrecision_Type.__name__ = "Integer32"
_FsntpSysPrecision_Object = MibScalar
fsntpSysPrecision = _FsntpSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 3),
    _FsntpSysPrecision_Type()
)
fsntpSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsntpSysPrecision.setStatus("current")
_FsntpSysRootDelay_Type = NTPSignedTimeValue
_FsntpSysRootDelay_Object = MibScalar
fsntpSysRootDelay = _FsntpSysRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 4),
    _FsntpSysRootDelay_Type()
)
fsntpSysRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsntpSysRootDelay.setStatus("current")
_FsntpSysRootDispersion_Type = NTPUnsignedTimeValue
_FsntpSysRootDispersion_Object = MibScalar
fsntpSysRootDispersion = _FsntpSysRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 5),
    _FsntpSysRootDispersion_Type()
)
fsntpSysRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsntpSysRootDispersion.setStatus("current")
_FsntpSysRefId_Type = NTPRefId
_FsntpSysRefId_Object = MibScalar
fsntpSysRefId = _FsntpSysRefId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 6),
    _FsntpSysRefId_Type()
)
fsntpSysRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsntpSysRefId.setStatus("current")
_FsntpSysRefTime_Type = NTPTimeStamp
_FsntpSysRefTime_Object = MibScalar
fsntpSysRefTime = _FsntpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 7),
    _FsntpSysRefTime_Type()
)
fsntpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsntpSysRefTime.setStatus("current")
_FsNTPServerIPAdd_Type = IpAddress
_FsNTPServerIPAdd_Object = MibScalar
fsNTPServerIPAdd = _FsNTPServerIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 8),
    _FsNTPServerIPAdd_Type()
)
fsNTPServerIPAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsNTPServerIPAdd.setStatus("current")


class _FsTimeAfterNTPCal_Type(OctetString):
    """Custom type fsTimeAfterNTPCal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_FsTimeAfterNTPCal_Type.__name__ = "OctetString"
_FsTimeAfterNTPCal_Object = MibScalar
fsTimeAfterNTPCal = _FsTimeAfterNTPCal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 9),
    _FsTimeAfterNTPCal_Type()
)
fsTimeAfterNTPCal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTimeAfterNTPCal.setStatus("current")


class _FsTimeSyncPeriod_Type(Integer32):
    """Custom type fsTimeSyncPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8640000),
    )


_FsTimeSyncPeriod_Type.__name__ = "Integer32"
_FsTimeSyncPeriod_Object = MibScalar
fsTimeSyncPeriod = _FsTimeSyncPeriod_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 10),
    _FsTimeSyncPeriod_Type()
)
fsTimeSyncPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTimeSyncPeriod.setStatus("current")
_FsNtpServerTable_Object = MibTable
fsNtpServerTable = _FsNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11)
)
if mibBuilder.loadTexts:
    fsNtpServerTable.setStatus("current")
_FsNtpServerEntry_Object = MibTableRow
fsNtpServerEntry = _FsNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11, 1)
)
fsNtpServerEntry.setIndexNames(
    (0, "FS-NTP-MIB", "fsNtpServerNetType"),
    (0, "FS-NTP-MIB", "fsNtpServerNetAddr"),
)
if mibBuilder.loadTexts:
    fsNtpServerEntry.setStatus("current")
_FsNtpServerNetType_Type = InetAddressType
_FsNtpServerNetType_Object = MibTableColumn
fsNtpServerNetType = _FsNtpServerNetType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11, 1, 1),
    _FsNtpServerNetType_Type()
)
fsNtpServerNetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNtpServerNetType.setStatus("current")
_FsNtpServerNetAddr_Type = InetAddress
_FsNtpServerNetAddr_Object = MibTableColumn
fsNtpServerNetAddr = _FsNtpServerNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11, 1, 2),
    _FsNtpServerNetAddr_Type()
)
fsNtpServerNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsNtpServerNetAddr.setStatus("current")


class _FsNtpServerVersion_Type(Integer32):
    """Custom type fsNtpServerVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2),
          ("version3", 3))
    )


_FsNtpServerVersion_Type.__name__ = "Integer32"
_FsNtpServerVersion_Object = MibTableColumn
fsNtpServerVersion = _FsNtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11, 1, 3),
    _FsNtpServerVersion_Type()
)
fsNtpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsNtpServerVersion.setStatus("current")
_FsNtpServerStatus_Type = RowStatus
_FsNtpServerStatus_Object = MibTableColumn
fsNtpServerStatus = _FsNtpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 11, 1, 4),
    _FsNtpServerStatus_Type()
)
fsNtpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsNtpServerStatus.setStatus("current")


class _FsntpSysState_Type(Integer32):
    """Custom type fsntpSysState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unsynchronized", 0),
          ("synchronized", 1))
    )


_FsntpSysState_Type.__name__ = "Integer32"
_FsntpSysState_Object = MibScalar
fsntpSysState = _FsntpSysState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 1, 12),
    _FsntpSysState_Type()
)
fsntpSysState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsntpSysState.setStatus("current")
_FsNtpMIBTrap_ObjectIdentity = ObjectIdentity
fsNtpMIBTrap = _FsNtpMIBTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 2)
)
_FsNtpMIBConformance_ObjectIdentity = ObjectIdentity
fsNtpMIBConformance = _FsNtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 2)
)
_FsNtpMIBCompliances_ObjectIdentity = ObjectIdentity
fsNtpMIBCompliances = _FsNtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 2, 1)
)
_FsNtpMIBGroups_ObjectIdentity = ObjectIdentity
fsNtpMIBGroups = _FsNtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 2, 2)
)

# Managed Objects groups

fsNtpSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 2, 2, 1)
)
fsNtpSysGroup.setObjects(
      *(("FS-NTP-MIB", "fsntpSysLeap"),
        ("FS-NTP-MIB", "fsntpSysStratum"),
        ("FS-NTP-MIB", "fsntpSysPrecision"),
        ("FS-NTP-MIB", "fsntpSysRootDelay"),
        ("FS-NTP-MIB", "fsntpSysRootDispersion"),
        ("FS-NTP-MIB", "fsntpSysRefId"),
        ("FS-NTP-MIB", "fsntpSysRefTime"),
        ("FS-NTP-MIB", "fsNTPServerIPAdd"),
        ("FS-NTP-MIB", "fsTimeAfterNTPCal"),
        ("FS-NTP-MIB", "fsTimeSyncPeriod"),
        ("FS-NTP-MIB", "fsNtpServerNetType"),
        ("FS-NTP-MIB", "fsNtpServerNetAddr"),
        ("FS-NTP-MIB", "fsNtpServerVersion"),
        ("FS-NTP-MIB", "fsNtpServerStatus"),
        ("FS-NTP-MIB", "fsntpSysState"))
)
if mibBuilder.loadTexts:
    fsNtpSysGroup.setStatus("current")


# Notification objects

fsNtpStatussyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 1, 2, 1)
)
fsNtpStatussyncTrap.setObjects(
    ("FS-NTP-MIB", "fsntpSysState")
)
if mibBuilder.loadTexts:
    fsNtpStatussyncTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsNtpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 49, 2, 1, 1)
)
fsNtpMIBCompliance.setObjects(
    ("FS-NTP-MIB", "fsNtpMIBGroups")
)
if mibBuilder.loadTexts:
    fsNtpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-NTP-MIB",
    **{"NTPTimeStamp": NTPTimeStamp,
       "NTPLeapIndicator": NTPLeapIndicator,
       "NTPSignedTimeValue": NTPSignedTimeValue,
       "NTPUnsignedTimeValue": NTPUnsignedTimeValue,
       "NTPStratum": NTPStratum,
       "NTPRefId": NTPRefId,
       "fsNtpMIB": fsNtpMIB,
       "fsNtpMIBObjects": fsNtpMIBObjects,
       "fsntpSystem": fsntpSystem,
       "fsntpSysLeap": fsntpSysLeap,
       "fsntpSysStratum": fsntpSysStratum,
       "fsntpSysPrecision": fsntpSysPrecision,
       "fsntpSysRootDelay": fsntpSysRootDelay,
       "fsntpSysRootDispersion": fsntpSysRootDispersion,
       "fsntpSysRefId": fsntpSysRefId,
       "fsntpSysRefTime": fsntpSysRefTime,
       "fsNTPServerIPAdd": fsNTPServerIPAdd,
       "fsTimeAfterNTPCal": fsTimeAfterNTPCal,
       "fsTimeSyncPeriod": fsTimeSyncPeriod,
       "fsNtpServerTable": fsNtpServerTable,
       "fsNtpServerEntry": fsNtpServerEntry,
       "fsNtpServerNetType": fsNtpServerNetType,
       "fsNtpServerNetAddr": fsNtpServerNetAddr,
       "fsNtpServerVersion": fsNtpServerVersion,
       "fsNtpServerStatus": fsNtpServerStatus,
       "fsntpSysState": fsntpSysState,
       "fsNtpMIBTrap": fsNtpMIBTrap,
       "fsNtpStatussyncTrap": fsNtpStatussyncTrap,
       "fsNtpMIBConformance": fsNtpMIBConformance,
       "fsNtpMIBCompliances": fsNtpMIBCompliances,
       "fsNtpMIBCompliance": fsNtpMIBCompliance,
       "fsNtpMIBGroups": fsNtpMIBGroups,
       "fsNtpSysGroup": fsNtpSysGroup}
)
