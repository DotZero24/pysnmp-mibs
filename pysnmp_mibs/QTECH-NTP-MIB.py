# SNMP MIB module (QTECH-NTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-NTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:38 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechNtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49)
)
if mibBuilder.loadTexts:
    qtechNtpMIB.setRevisions(
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

_QtechNtpMIBObjects_ObjectIdentity = ObjectIdentity
qtechNtpMIBObjects = _QtechNtpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1)
)
_QtechntpSystem_ObjectIdentity = ObjectIdentity
qtechntpSystem = _QtechntpSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1)
)
_QtechntpSysLeap_Type = NTPLeapIndicator
_QtechntpSysLeap_Object = MibScalar
qtechntpSysLeap = _QtechntpSysLeap_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 1),
    _QtechntpSysLeap_Type()
)
qtechntpSysLeap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechntpSysLeap.setStatus("current")
_QtechntpSysStratum_Type = NTPStratum
_QtechntpSysStratum_Object = MibScalar
qtechntpSysStratum = _QtechntpSysStratum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 2),
    _QtechntpSysStratum_Type()
)
qtechntpSysStratum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechntpSysStratum.setStatus("current")


class _QtechntpSysPrecision_Type(Integer32):
    """Custom type qtechntpSysPrecision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-24, 24),
    )


_QtechntpSysPrecision_Type.__name__ = "Integer32"
_QtechntpSysPrecision_Object = MibScalar
qtechntpSysPrecision = _QtechntpSysPrecision_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 3),
    _QtechntpSysPrecision_Type()
)
qtechntpSysPrecision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechntpSysPrecision.setStatus("current")
_QtechntpSysRootDelay_Type = NTPSignedTimeValue
_QtechntpSysRootDelay_Object = MibScalar
qtechntpSysRootDelay = _QtechntpSysRootDelay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 4),
    _QtechntpSysRootDelay_Type()
)
qtechntpSysRootDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechntpSysRootDelay.setStatus("current")
_QtechntpSysRootDispersion_Type = NTPUnsignedTimeValue
_QtechntpSysRootDispersion_Object = MibScalar
qtechntpSysRootDispersion = _QtechntpSysRootDispersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 5),
    _QtechntpSysRootDispersion_Type()
)
qtechntpSysRootDispersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechntpSysRootDispersion.setStatus("current")
_QtechntpSysRefId_Type = NTPRefId
_QtechntpSysRefId_Object = MibScalar
qtechntpSysRefId = _QtechntpSysRefId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 6),
    _QtechntpSysRefId_Type()
)
qtechntpSysRefId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechntpSysRefId.setStatus("current")
_QtechntpSysRefTime_Type = NTPTimeStamp
_QtechntpSysRefTime_Object = MibScalar
qtechntpSysRefTime = _QtechntpSysRefTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 7),
    _QtechntpSysRefTime_Type()
)
qtechntpSysRefTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechntpSysRefTime.setStatus("current")
_QtechNTPServerIPAdd_Type = IpAddress
_QtechNTPServerIPAdd_Object = MibScalar
qtechNTPServerIPAdd = _QtechNTPServerIPAdd_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 8),
    _QtechNTPServerIPAdd_Type()
)
qtechNTPServerIPAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechNTPServerIPAdd.setStatus("current")


class _QtechTimeAfterNTPCal_Type(OctetString):
    """Custom type qtechTimeAfterNTPCal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_QtechTimeAfterNTPCal_Type.__name__ = "OctetString"
_QtechTimeAfterNTPCal_Object = MibScalar
qtechTimeAfterNTPCal = _QtechTimeAfterNTPCal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 9),
    _QtechTimeAfterNTPCal_Type()
)
qtechTimeAfterNTPCal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTimeAfterNTPCal.setStatus("current")


class _QtechTimeSyncPeriod_Type(Integer32):
    """Custom type qtechTimeSyncPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8640000),
    )


_QtechTimeSyncPeriod_Type.__name__ = "Integer32"
_QtechTimeSyncPeriod_Object = MibScalar
qtechTimeSyncPeriod = _QtechTimeSyncPeriod_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 10),
    _QtechTimeSyncPeriod_Type()
)
qtechTimeSyncPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechTimeSyncPeriod.setStatus("current")
_QtechNtpServerTable_Object = MibTable
qtechNtpServerTable = _QtechNtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11)
)
if mibBuilder.loadTexts:
    qtechNtpServerTable.setStatus("current")
_QtechNtpServerEntry_Object = MibTableRow
qtechNtpServerEntry = _QtechNtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11, 1)
)
qtechNtpServerEntry.setIndexNames(
    (0, "QTECH-NTP-MIB", "qtechNtpServerNetType"),
    (0, "QTECH-NTP-MIB", "qtechNtpServerNetAddr"),
)
if mibBuilder.loadTexts:
    qtechNtpServerEntry.setStatus("current")
_QtechNtpServerNetType_Type = InetAddressType
_QtechNtpServerNetType_Object = MibTableColumn
qtechNtpServerNetType = _QtechNtpServerNetType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11, 1, 1),
    _QtechNtpServerNetType_Type()
)
qtechNtpServerNetType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNtpServerNetType.setStatus("current")
_QtechNtpServerNetAddr_Type = InetAddress
_QtechNtpServerNetAddr_Object = MibTableColumn
qtechNtpServerNetAddr = _QtechNtpServerNetAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11, 1, 2),
    _QtechNtpServerNetAddr_Type()
)
qtechNtpServerNetAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechNtpServerNetAddr.setStatus("current")


class _QtechNtpServerVersion_Type(Integer32):
    """Custom type qtechNtpServerVersion based on Integer32"""
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


_QtechNtpServerVersion_Type.__name__ = "Integer32"
_QtechNtpServerVersion_Object = MibTableColumn
qtechNtpServerVersion = _QtechNtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11, 1, 3),
    _QtechNtpServerVersion_Type()
)
qtechNtpServerVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechNtpServerVersion.setStatus("current")
_QtechNtpServerStatus_Type = RowStatus
_QtechNtpServerStatus_Object = MibTableColumn
qtechNtpServerStatus = _QtechNtpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 1, 1, 11, 1, 4),
    _QtechNtpServerStatus_Type()
)
qtechNtpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechNtpServerStatus.setStatus("current")
_QtechNtpMIBConformance_ObjectIdentity = ObjectIdentity
qtechNtpMIBConformance = _QtechNtpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 2)
)
_QtechNtpMIBCompliances_ObjectIdentity = ObjectIdentity
qtechNtpMIBCompliances = _QtechNtpMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 2, 1)
)
_QtechNtpMIBGroups_ObjectIdentity = ObjectIdentity
qtechNtpMIBGroups = _QtechNtpMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 2, 2)
)

# Managed Objects groups

qtechNtpSysGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 2, 2, 1)
)
qtechNtpSysGroup.setObjects(
      *(("QTECH-NTP-MIB", "qtechntpSysLeap"),
        ("QTECH-NTP-MIB", "qtechntpSysStratum"),
        ("QTECH-NTP-MIB", "qtechntpSysPrecision"),
        ("QTECH-NTP-MIB", "qtechntpSysRootDelay"),
        ("QTECH-NTP-MIB", "qtechntpSysRootDispersion"),
        ("QTECH-NTP-MIB", "qtechntpSysRefId"),
        ("QTECH-NTP-MIB", "qtechntpSysRefTime"),
        ("QTECH-NTP-MIB", "qtechNTPServerIPAdd"),
        ("QTECH-NTP-MIB", "qtechTimeAfterNTPCal"),
        ("QTECH-NTP-MIB", "qtechTimeSyncPeriod"),
        ("QTECH-NTP-MIB", "qtechNtpServerNetType"),
        ("QTECH-NTP-MIB", "qtechNtpServerNetAddr"),
        ("QTECH-NTP-MIB", "qtechNtpServerVersion"),
        ("QTECH-NTP-MIB", "qtechNtpServerStatus"))
)
if mibBuilder.loadTexts:
    qtechNtpSysGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechNtpMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 49, 2, 1, 1)
)
qtechNtpMIBCompliance.setObjects(
    ("QTECH-NTP-MIB", "qtechNtpMIBGroups")
)
if mibBuilder.loadTexts:
    qtechNtpMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-NTP-MIB",
    **{"NTPTimeStamp": NTPTimeStamp,
       "NTPLeapIndicator": NTPLeapIndicator,
       "NTPSignedTimeValue": NTPSignedTimeValue,
       "NTPUnsignedTimeValue": NTPUnsignedTimeValue,
       "NTPStratum": NTPStratum,
       "NTPRefId": NTPRefId,
       "qtechNtpMIB": qtechNtpMIB,
       "qtechNtpMIBObjects": qtechNtpMIBObjects,
       "qtechntpSystem": qtechntpSystem,
       "qtechntpSysLeap": qtechntpSysLeap,
       "qtechntpSysStratum": qtechntpSysStratum,
       "qtechntpSysPrecision": qtechntpSysPrecision,
       "qtechntpSysRootDelay": qtechntpSysRootDelay,
       "qtechntpSysRootDispersion": qtechntpSysRootDispersion,
       "qtechntpSysRefId": qtechntpSysRefId,
       "qtechntpSysRefTime": qtechntpSysRefTime,
       "qtechNTPServerIPAdd": qtechNTPServerIPAdd,
       "qtechTimeAfterNTPCal": qtechTimeAfterNTPCal,
       "qtechTimeSyncPeriod": qtechTimeSyncPeriod,
       "qtechNtpServerTable": qtechNtpServerTable,
       "qtechNtpServerEntry": qtechNtpServerEntry,
       "qtechNtpServerNetType": qtechNtpServerNetType,
       "qtechNtpServerNetAddr": qtechNtpServerNetAddr,
       "qtechNtpServerVersion": qtechNtpServerVersion,
       "qtechNtpServerStatus": qtechNtpServerStatus,
       "qtechNtpMIBConformance": qtechNtpMIBConformance,
       "qtechNtpMIBCompliances": qtechNtpMIBCompliances,
       "qtechNtpMIBCompliance": qtechNtpMIBCompliance,
       "qtechNtpMIBGroups": qtechNtpMIBGroups,
       "qtechNtpSysGroup": qtechNtpSysGroup}
)
