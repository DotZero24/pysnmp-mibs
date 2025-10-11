# SNMP MIB module (FS-URPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-URPF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:30 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsUrpfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46)
)
if mibBuilder.loadTexts:
    fsUrpfMIB.setRevisions(
        ("2009-04-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsUrpfMIBObjects_ObjectIdentity = ObjectIdentity
fsUrpfMIBObjects = _FsUrpfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0)
)
_FsUrpfScalar_ObjectIdentity = ObjectIdentity
fsUrpfScalar = _FsUrpfScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 1)
)


class _FsUrpfComputeInterval_Type(Integer32):
    """Custom type fsUrpfComputeInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_FsUrpfComputeInterval_Type.__name__ = "Integer32"
_FsUrpfComputeInterval_Object = MibScalar
fsUrpfComputeInterval = _FsUrpfComputeInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 1, 1),
    _FsUrpfComputeInterval_Type()
)
fsUrpfComputeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsUrpfComputeInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsUrpfComputeInterval.setUnits("seconds")


class _FsUrpfDropRateWindow_Type(Integer32):
    """Custom type fsUrpfDropRateWindow based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 1500),
    )


_FsUrpfDropRateWindow_Type.__name__ = "Integer32"
_FsUrpfDropRateWindow_Object = MibScalar
fsUrpfDropRateWindow = _FsUrpfDropRateWindow_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 1, 2),
    _FsUrpfDropRateWindow_Type()
)
fsUrpfDropRateWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUrpfDropRateWindow.setStatus("current")
if mibBuilder.loadTexts:
    fsUrpfDropRateWindow.setUnits("seconds")


class _FsUrpfDropNotifyHoldDownTime_Type(Integer32):
    """Custom type fsUrpfDropNotifyHoldDownTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_FsUrpfDropNotifyHoldDownTime_Type.__name__ = "Integer32"
_FsUrpfDropNotifyHoldDownTime_Object = MibScalar
fsUrpfDropNotifyHoldDownTime = _FsUrpfDropNotifyHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 1, 3),
    _FsUrpfDropNotifyHoldDownTime_Type()
)
fsUrpfDropNotifyHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsUrpfDropNotifyHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    fsUrpfDropNotifyHoldDownTime.setUnits("seconds")
_FsUrpfStatistics_ObjectIdentity = ObjectIdentity
fsUrpfStatistics = _FsUrpfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2)
)
_FsUrpfTable_Object = MibTable
fsUrpfTable = _FsUrpfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2, 1)
)
if mibBuilder.loadTexts:
    fsUrpfTable.setStatus("current")
_FsUrpfEntry_Object = MibTableRow
fsUrpfEntry = _FsUrpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2, 1, 1)
)
fsUrpfEntry.setIndexNames(
    (0, "FS-URPF-MIB", "fsUrpfIpVersion"),
)
if mibBuilder.loadTexts:
    fsUrpfEntry.setStatus("current")


class _FsUrpfIpVersion_Type(Integer32):
    """Custom type fsUrpfIpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_FsUrpfIpVersion_Type.__name__ = "Integer32"
_FsUrpfIpVersion_Object = MibTableColumn
fsUrpfIpVersion = _FsUrpfIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2, 1, 1, 1),
    _FsUrpfIpVersion_Type()
)
fsUrpfIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsUrpfIpVersion.setStatus("current")
_FsUrpfDrops_Type = Counter32
_FsUrpfDrops_Object = MibTableColumn
fsUrpfDrops = _FsUrpfDrops_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2, 1, 1, 2),
    _FsUrpfDrops_Type()
)
fsUrpfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUrpfDrops.setStatus("current")
if mibBuilder.loadTexts:
    fsUrpfDrops.setUnits("packets")
_FsUrpfDropRate_Type = Gauge32
_FsUrpfDropRate_Object = MibTableColumn
fsUrpfDropRate = _FsUrpfDropRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2, 1, 1, 3),
    _FsUrpfDropRate_Type()
)
fsUrpfDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUrpfDropRate.setStatus("current")
if mibBuilder.loadTexts:
    fsUrpfDropRate.setUnits("packets per second")
_FsUrpfIfMonTable_Object = MibTable
fsUrpfIfMonTable = _FsUrpfIfMonTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2, 2)
)
if mibBuilder.loadTexts:
    fsUrpfIfMonTable.setStatus("current")
_FsUrpfIfMonEntry_Object = MibTableRow
fsUrpfIfMonEntry = _FsUrpfIfMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2, 2, 1)
)
fsUrpfIfMonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "FS-URPF-MIB", "fsUrpfIfIpVersion"),
)
if mibBuilder.loadTexts:
    fsUrpfIfMonEntry.setStatus("current")


class _FsUrpfIfIpVersion_Type(Integer32):
    """Custom type fsUrpfIfIpVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_FsUrpfIfIpVersion_Type.__name__ = "Integer32"
_FsUrpfIfIpVersion_Object = MibTableColumn
fsUrpfIfIpVersion = _FsUrpfIfIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2, 2, 1, 1),
    _FsUrpfIfIpVersion_Type()
)
fsUrpfIfIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsUrpfIfIpVersion.setStatus("current")
_FsUrpfIfDrops_Type = Counter32
_FsUrpfIfDrops_Object = MibTableColumn
fsUrpfIfDrops = _FsUrpfIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2, 2, 1, 2),
    _FsUrpfIfDrops_Type()
)
fsUrpfIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUrpfIfDrops.setStatus("current")
if mibBuilder.loadTexts:
    fsUrpfIfDrops.setUnits("packets")
_FsUrpfIfDropRate_Type = Gauge32
_FsUrpfIfDropRate_Object = MibTableColumn
fsUrpfIfDropRate = _FsUrpfIfDropRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 2, 2, 1, 3),
    _FsUrpfIfDropRate_Type()
)
fsUrpfIfDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUrpfIfDropRate.setStatus("current")
if mibBuilder.loadTexts:
    fsUrpfIfDropRate.setUnits("packets/second")
_FsUrpfInterfaceConfig_ObjectIdentity = ObjectIdentity
fsUrpfInterfaceConfig = _FsUrpfInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 3)
)
_FsUrpfIfConfTable_Object = MibTable
fsUrpfIfConfTable = _FsUrpfIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 3, 1)
)
if mibBuilder.loadTexts:
    fsUrpfIfConfTable.setStatus("current")
_FsUrpfIfConfEntry_Object = MibTableRow
fsUrpfIfConfEntry = _FsUrpfIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 3, 1, 1)
)
if mibBuilder.loadTexts:
    fsUrpfIfConfEntry.setStatus("current")


class _FsUrpfIfCheckStrict_Type(Integer32):
    """Custom type fsUrpfIfCheckStrict based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("strict", 1),
          ("loose", 2))
    )


_FsUrpfIfCheckStrict_Type.__name__ = "Integer32"
_FsUrpfIfCheckStrict_Object = MibTableColumn
fsUrpfIfCheckStrict = _FsUrpfIfCheckStrict_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 3, 1, 1, 1),
    _FsUrpfIfCheckStrict_Type()
)
fsUrpfIfCheckStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUrpfIfCheckStrict.setStatus("current")


class _FsUrpfIfDropRateNotifyEnable_Type(TruthValue):
    """Custom type fsUrpfIfDropRateNotifyEnable based on TruthValue"""
    defaultValue = 2


_FsUrpfIfDropRateNotifyEnable_Type.__name__ = "TruthValue"
_FsUrpfIfDropRateNotifyEnable_Object = MibTableColumn
fsUrpfIfDropRateNotifyEnable = _FsUrpfIfDropRateNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 3, 1, 1, 2),
    _FsUrpfIfDropRateNotifyEnable_Type()
)
fsUrpfIfDropRateNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsUrpfIfDropRateNotifyEnable.setStatus("current")


class _FsUrpfIfNotifyDropRateThreshold_Type(Unsigned32):
    """Custom type fsUrpfIfNotifyDropRateThreshold based on Unsigned32"""
    defaultValue = 1000


_FsUrpfIfNotifyDropRateThreshold_Type.__name__ = "Unsigned32"
_FsUrpfIfNotifyDropRateThreshold_Object = MibTableColumn
fsUrpfIfNotifyDropRateThreshold = _FsUrpfIfNotifyDropRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 3, 1, 1, 3),
    _FsUrpfIfNotifyDropRateThreshold_Type()
)
fsUrpfIfNotifyDropRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsUrpfIfNotifyDropRateThreshold.setStatus("current")
if mibBuilder.loadTexts:
    fsUrpfIfNotifyDropRateThreshold.setUnits("packets/second")


class _FsUrpfIfNotifyDrHoldDownReset_Type(TruthValue):
    """Custom type fsUrpfIfNotifyDrHoldDownReset based on TruthValue"""
    defaultValue = 2


_FsUrpfIfNotifyDrHoldDownReset_Type.__name__ = "TruthValue"
_FsUrpfIfNotifyDrHoldDownReset_Object = MibTableColumn
fsUrpfIfNotifyDrHoldDownReset = _FsUrpfIfNotifyDrHoldDownReset_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 3, 1, 1, 4),
    _FsUrpfIfNotifyDrHoldDownReset_Type()
)
fsUrpfIfNotifyDrHoldDownReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsUrpfIfNotifyDrHoldDownReset.setStatus("current")


class _FsUrpfIfWhichRouteTableID_Type(Integer32):
    """Custom type fsUrpfIfWhichRouteTableID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("vrf", 2))
    )


_FsUrpfIfWhichRouteTableID_Type.__name__ = "Integer32"
_FsUrpfIfWhichRouteTableID_Object = MibTableColumn
fsUrpfIfWhichRouteTableID = _FsUrpfIfWhichRouteTableID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 3, 1, 1, 5),
    _FsUrpfIfWhichRouteTableID_Type()
)
fsUrpfIfWhichRouteTableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUrpfIfWhichRouteTableID.setStatus("current")


class _FsUrpfIfVrfName_Type(SnmpAdminString):
    """Custom type fsUrpfIfVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsUrpfIfVrfName_Type.__name__ = "SnmpAdminString"
_FsUrpfIfVrfName_Object = MibTableColumn
fsUrpfIfVrfName = _FsUrpfIfVrfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 0, 3, 1, 1, 6),
    _FsUrpfIfVrfName_Type()
)
fsUrpfIfVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsUrpfIfVrfName.setStatus("current")
_FsUrpfMIBNotifs_ObjectIdentity = ObjectIdentity
fsUrpfMIBNotifs = _FsUrpfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 1)
)
_FsUrpfMIBConformance_ObjectIdentity = ObjectIdentity
fsUrpfMIBConformance = _FsUrpfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 2)
)
_FsUrpfMIBCompliances_ObjectIdentity = ObjectIdentity
fsUrpfMIBCompliances = _FsUrpfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 2, 1)
)
_FsUrpfMIBGroups_ObjectIdentity = ObjectIdentity
fsUrpfMIBGroups = _FsUrpfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 2, 2)
)
fsUrpfIfMonEntry.registerAugmentions(
    ("FS-URPF-MIB",
     "fsUrpfIfConfEntry")
)
fsUrpfIfConfEntry.setIndexNames(*fsUrpfIfMonEntry.getIndexNames())

# Managed Objects groups

fsUrpfMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 2, 2, 1)
)
fsUrpfMIBMainObjectGroup.setObjects(
      *(("FS-URPF-MIB", "fsUrpfComputeInterval"),
        ("FS-URPF-MIB", "fsUrpfDropRateWindow"),
        ("FS-URPF-MIB", "fsUrpfDropNotifyHoldDownTime"),
        ("FS-URPF-MIB", "fsUrpfDrops"),
        ("FS-URPF-MIB", "fsUrpfDropRate"),
        ("FS-URPF-MIB", "fsUrpfIfDrops"),
        ("FS-URPF-MIB", "fsUrpfIfDropRate"),
        ("FS-URPF-MIB", "fsUrpfIfCheckStrict"),
        ("FS-URPF-MIB", "fsUrpfIfDropRateNotifyEnable"),
        ("FS-URPF-MIB", "fsUrpfIfNotifyDropRateThreshold"),
        ("FS-URPF-MIB", "fsUrpfIfNotifyDrHoldDownReset"))
)
if mibBuilder.loadTexts:
    fsUrpfMIBMainObjectGroup.setStatus("current")

fsUrpfMIBVrfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 2, 2, 2)
)
fsUrpfMIBVrfObjectGroup.setObjects(
      *(("FS-URPF-MIB", "fsUrpfIfWhichRouteTableID"),
        ("FS-URPF-MIB", "fsUrpfIfVrfName"))
)
if mibBuilder.loadTexts:
    fsUrpfMIBVrfObjectGroup.setStatus("current")


# Notification objects

fsUrpfIfDropRateNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 1, 1)
)
fsUrpfIfDropRateNotify.setObjects(
    ("FS-URPF-MIB", "fsUrpfIfDropRate")
)
if mibBuilder.loadTexts:
    fsUrpfIfDropRateNotify.setStatus(
        "current"
    )


# Notifications groups

fsUrpfMIBNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 2, 2, 3)
)
fsUrpfMIBNotifyGroup.setObjects(
    ("FS-URPF-MIB", "fsUrpfIfDropRateNotify")
)
if mibBuilder.loadTexts:
    fsUrpfMIBNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

fsUrpfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 46, 2, 1, 1)
)
fsUrpfMIBCompliance.setObjects(
      *(("FS-URPF-MIB", "fsUrpfMIBMainObjectGroup"),
        ("FS-URPF-MIB", "fsUrpfMIBNotifyGroup"),
        ("FS-URPF-MIB", "fsUrpfMIBVrfObjectGroup"))
)
if mibBuilder.loadTexts:
    fsUrpfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-URPF-MIB",
    **{"fsUrpfMIB": fsUrpfMIB,
       "fsUrpfMIBObjects": fsUrpfMIBObjects,
       "fsUrpfScalar": fsUrpfScalar,
       "fsUrpfComputeInterval": fsUrpfComputeInterval,
       "fsUrpfDropRateWindow": fsUrpfDropRateWindow,
       "fsUrpfDropNotifyHoldDownTime": fsUrpfDropNotifyHoldDownTime,
       "fsUrpfStatistics": fsUrpfStatistics,
       "fsUrpfTable": fsUrpfTable,
       "fsUrpfEntry": fsUrpfEntry,
       "fsUrpfIpVersion": fsUrpfIpVersion,
       "fsUrpfDrops": fsUrpfDrops,
       "fsUrpfDropRate": fsUrpfDropRate,
       "fsUrpfIfMonTable": fsUrpfIfMonTable,
       "fsUrpfIfMonEntry": fsUrpfIfMonEntry,
       "fsUrpfIfIpVersion": fsUrpfIfIpVersion,
       "fsUrpfIfDrops": fsUrpfIfDrops,
       "fsUrpfIfDropRate": fsUrpfIfDropRate,
       "fsUrpfInterfaceConfig": fsUrpfInterfaceConfig,
       "fsUrpfIfConfTable": fsUrpfIfConfTable,
       "fsUrpfIfConfEntry": fsUrpfIfConfEntry,
       "fsUrpfIfCheckStrict": fsUrpfIfCheckStrict,
       "fsUrpfIfDropRateNotifyEnable": fsUrpfIfDropRateNotifyEnable,
       "fsUrpfIfNotifyDropRateThreshold": fsUrpfIfNotifyDropRateThreshold,
       "fsUrpfIfNotifyDrHoldDownReset": fsUrpfIfNotifyDrHoldDownReset,
       "fsUrpfIfWhichRouteTableID": fsUrpfIfWhichRouteTableID,
       "fsUrpfIfVrfName": fsUrpfIfVrfName,
       "fsUrpfMIBNotifs": fsUrpfMIBNotifs,
       "fsUrpfIfDropRateNotify": fsUrpfIfDropRateNotify,
       "fsUrpfMIBConformance": fsUrpfMIBConformance,
       "fsUrpfMIBCompliances": fsUrpfMIBCompliances,
       "fsUrpfMIBCompliance": fsUrpfMIBCompliance,
       "fsUrpfMIBGroups": fsUrpfMIBGroups,
       "fsUrpfMIBMainObjectGroup": fsUrpfMIBMainObjectGroup,
       "fsUrpfMIBVrfObjectGroup": fsUrpfMIBVrfObjectGroup,
       "fsUrpfMIBNotifyGroup": fsUrpfMIBNotifyGroup}
)
