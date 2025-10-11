# SNMP MIB module (QTECH-URPF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-URPF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:10 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechUrpfMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46)
)
if mibBuilder.loadTexts:
    qtechUrpfMIB.setRevisions(
        ("2009-04-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechUrpfMIBObjects_ObjectIdentity = ObjectIdentity
qtechUrpfMIBObjects = _QtechUrpfMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0)
)
_QtechUrpfScalar_ObjectIdentity = ObjectIdentity
qtechUrpfScalar = _QtechUrpfScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 1)
)


class _QtechUrpfComputeInterval_Type(Integer32):
    """Custom type qtechUrpfComputeInterval based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_QtechUrpfComputeInterval_Type.__name__ = "Integer32"
_QtechUrpfComputeInterval_Object = MibScalar
qtechUrpfComputeInterval = _QtechUrpfComputeInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 1, 1),
    _QtechUrpfComputeInterval_Type()
)
qtechUrpfComputeInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechUrpfComputeInterval.setStatus("current")
if mibBuilder.loadTexts:
    qtechUrpfComputeInterval.setUnits("seconds")


class _QtechUrpfDropRateWindow_Type(Integer32):
    """Custom type qtechUrpfDropRateWindow based on Integer32"""
    defaultValue = 150

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(150, 1500),
    )


_QtechUrpfDropRateWindow_Type.__name__ = "Integer32"
_QtechUrpfDropRateWindow_Object = MibScalar
qtechUrpfDropRateWindow = _QtechUrpfDropRateWindow_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 1, 2),
    _QtechUrpfDropRateWindow_Type()
)
qtechUrpfDropRateWindow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUrpfDropRateWindow.setStatus("current")
if mibBuilder.loadTexts:
    qtechUrpfDropRateWindow.setUnits("seconds")


class _QtechUrpfDropNotifyHoldDownTime_Type(Integer32):
    """Custom type qtechUrpfDropNotifyHoldDownTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 300),
    )


_QtechUrpfDropNotifyHoldDownTime_Type.__name__ = "Integer32"
_QtechUrpfDropNotifyHoldDownTime_Object = MibScalar
qtechUrpfDropNotifyHoldDownTime = _QtechUrpfDropNotifyHoldDownTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 1, 3),
    _QtechUrpfDropNotifyHoldDownTime_Type()
)
qtechUrpfDropNotifyHoldDownTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechUrpfDropNotifyHoldDownTime.setStatus("current")
if mibBuilder.loadTexts:
    qtechUrpfDropNotifyHoldDownTime.setUnits("seconds")
_QtechUrpfStatistics_ObjectIdentity = ObjectIdentity
qtechUrpfStatistics = _QtechUrpfStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2)
)
_QtechUrpfTable_Object = MibTable
qtechUrpfTable = _QtechUrpfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2, 1)
)
if mibBuilder.loadTexts:
    qtechUrpfTable.setStatus("current")
_QtechUrpfEntry_Object = MibTableRow
qtechUrpfEntry = _QtechUrpfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2, 1, 1)
)
qtechUrpfEntry.setIndexNames(
    (0, "QTECH-URPF-MIB", "qtechUrpfIpVersion"),
)
if mibBuilder.loadTexts:
    qtechUrpfEntry.setStatus("current")


class _QtechUrpfIpVersion_Type(Integer32):
    """Custom type qtechUrpfIpVersion based on Integer32"""
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


_QtechUrpfIpVersion_Type.__name__ = "Integer32"
_QtechUrpfIpVersion_Object = MibTableColumn
qtechUrpfIpVersion = _QtechUrpfIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2, 1, 1, 1),
    _QtechUrpfIpVersion_Type()
)
qtechUrpfIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechUrpfIpVersion.setStatus("current")
_QtechUrpfDrops_Type = Counter32
_QtechUrpfDrops_Object = MibTableColumn
qtechUrpfDrops = _QtechUrpfDrops_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2, 1, 1, 2),
    _QtechUrpfDrops_Type()
)
qtechUrpfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUrpfDrops.setStatus("current")
if mibBuilder.loadTexts:
    qtechUrpfDrops.setUnits("packets")
_QtechUrpfDropRate_Type = Gauge32
_QtechUrpfDropRate_Object = MibTableColumn
qtechUrpfDropRate = _QtechUrpfDropRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2, 1, 1, 3),
    _QtechUrpfDropRate_Type()
)
qtechUrpfDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUrpfDropRate.setStatus("current")
if mibBuilder.loadTexts:
    qtechUrpfDropRate.setUnits("packets per second")
_QtechUrpfIfMonTable_Object = MibTable
qtechUrpfIfMonTable = _QtechUrpfIfMonTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2, 2)
)
if mibBuilder.loadTexts:
    qtechUrpfIfMonTable.setStatus("current")
_QtechUrpfIfMonEntry_Object = MibTableRow
qtechUrpfIfMonEntry = _QtechUrpfIfMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2, 2, 1)
)
qtechUrpfIfMonEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "QTECH-URPF-MIB", "qtechUrpfIfIpVersion"),
)
if mibBuilder.loadTexts:
    qtechUrpfIfMonEntry.setStatus("current")


class _QtechUrpfIfIpVersion_Type(Integer32):
    """Custom type qtechUrpfIfIpVersion based on Integer32"""
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


_QtechUrpfIfIpVersion_Type.__name__ = "Integer32"
_QtechUrpfIfIpVersion_Object = MibTableColumn
qtechUrpfIfIpVersion = _QtechUrpfIfIpVersion_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2, 2, 1, 1),
    _QtechUrpfIfIpVersion_Type()
)
qtechUrpfIfIpVersion.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechUrpfIfIpVersion.setStatus("current")
_QtechUrpfIfDrops_Type = Counter32
_QtechUrpfIfDrops_Object = MibTableColumn
qtechUrpfIfDrops = _QtechUrpfIfDrops_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2, 2, 1, 2),
    _QtechUrpfIfDrops_Type()
)
qtechUrpfIfDrops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUrpfIfDrops.setStatus("current")
if mibBuilder.loadTexts:
    qtechUrpfIfDrops.setUnits("packets")
_QtechUrpfIfDropRate_Type = Gauge32
_QtechUrpfIfDropRate_Object = MibTableColumn
qtechUrpfIfDropRate = _QtechUrpfIfDropRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 2, 2, 1, 3),
    _QtechUrpfIfDropRate_Type()
)
qtechUrpfIfDropRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUrpfIfDropRate.setStatus("current")
if mibBuilder.loadTexts:
    qtechUrpfIfDropRate.setUnits("packets/second")
_QtechUrpfInterfaceConfig_ObjectIdentity = ObjectIdentity
qtechUrpfInterfaceConfig = _QtechUrpfInterfaceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 3)
)
_QtechUrpfIfConfTable_Object = MibTable
qtechUrpfIfConfTable = _QtechUrpfIfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 3, 1)
)
if mibBuilder.loadTexts:
    qtechUrpfIfConfTable.setStatus("current")
_QtechUrpfIfConfEntry_Object = MibTableRow
qtechUrpfIfConfEntry = _QtechUrpfIfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 3, 1, 1)
)
if mibBuilder.loadTexts:
    qtechUrpfIfConfEntry.setStatus("current")


class _QtechUrpfIfCheckStrict_Type(Integer32):
    """Custom type qtechUrpfIfCheckStrict based on Integer32"""
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


_QtechUrpfIfCheckStrict_Type.__name__ = "Integer32"
_QtechUrpfIfCheckStrict_Object = MibTableColumn
qtechUrpfIfCheckStrict = _QtechUrpfIfCheckStrict_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 3, 1, 1, 1),
    _QtechUrpfIfCheckStrict_Type()
)
qtechUrpfIfCheckStrict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUrpfIfCheckStrict.setStatus("current")


class _QtechUrpfIfDropRateNotifyEnable_Type(TruthValue):
    """Custom type qtechUrpfIfDropRateNotifyEnable based on TruthValue"""
    defaultValue = 2


_QtechUrpfIfDropRateNotifyEnable_Type.__name__ = "TruthValue"
_QtechUrpfIfDropRateNotifyEnable_Object = MibTableColumn
qtechUrpfIfDropRateNotifyEnable = _QtechUrpfIfDropRateNotifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 3, 1, 1, 2),
    _QtechUrpfIfDropRateNotifyEnable_Type()
)
qtechUrpfIfDropRateNotifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechUrpfIfDropRateNotifyEnable.setStatus("current")


class _QtechUrpfIfNotifyDropRateThreshold_Type(Unsigned32):
    """Custom type qtechUrpfIfNotifyDropRateThreshold based on Unsigned32"""
    defaultValue = 1000


_QtechUrpfIfNotifyDropRateThreshold_Type.__name__ = "Unsigned32"
_QtechUrpfIfNotifyDropRateThreshold_Object = MibTableColumn
qtechUrpfIfNotifyDropRateThreshold = _QtechUrpfIfNotifyDropRateThreshold_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 3, 1, 1, 3),
    _QtechUrpfIfNotifyDropRateThreshold_Type()
)
qtechUrpfIfNotifyDropRateThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechUrpfIfNotifyDropRateThreshold.setStatus("current")
if mibBuilder.loadTexts:
    qtechUrpfIfNotifyDropRateThreshold.setUnits("packets/second")


class _QtechUrpfIfNotifyDrHoldDownReset_Type(TruthValue):
    """Custom type qtechUrpfIfNotifyDrHoldDownReset based on TruthValue"""
    defaultValue = 2


_QtechUrpfIfNotifyDrHoldDownReset_Type.__name__ = "TruthValue"
_QtechUrpfIfNotifyDrHoldDownReset_Object = MibTableColumn
qtechUrpfIfNotifyDrHoldDownReset = _QtechUrpfIfNotifyDrHoldDownReset_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 3, 1, 1, 4),
    _QtechUrpfIfNotifyDrHoldDownReset_Type()
)
qtechUrpfIfNotifyDrHoldDownReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechUrpfIfNotifyDrHoldDownReset.setStatus("current")


class _QtechUrpfIfWhichRouteTableID_Type(Integer32):
    """Custom type qtechUrpfIfWhichRouteTableID based on Integer32"""
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


_QtechUrpfIfWhichRouteTableID_Type.__name__ = "Integer32"
_QtechUrpfIfWhichRouteTableID_Object = MibTableColumn
qtechUrpfIfWhichRouteTableID = _QtechUrpfIfWhichRouteTableID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 3, 1, 1, 5),
    _QtechUrpfIfWhichRouteTableID_Type()
)
qtechUrpfIfWhichRouteTableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUrpfIfWhichRouteTableID.setStatus("current")


class _QtechUrpfIfVrfName_Type(SnmpAdminString):
    """Custom type qtechUrpfIfVrfName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_QtechUrpfIfVrfName_Type.__name__ = "SnmpAdminString"
_QtechUrpfIfVrfName_Object = MibTableColumn
qtechUrpfIfVrfName = _QtechUrpfIfVrfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 0, 3, 1, 1, 6),
    _QtechUrpfIfVrfName_Type()
)
qtechUrpfIfVrfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechUrpfIfVrfName.setStatus("current")
_QtechUrpfMIBNotifs_ObjectIdentity = ObjectIdentity
qtechUrpfMIBNotifs = _QtechUrpfMIBNotifs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 1)
)
_QtechUrpfMIBConformance_ObjectIdentity = ObjectIdentity
qtechUrpfMIBConformance = _QtechUrpfMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 2)
)
_QtechUrpfMIBCompliances_ObjectIdentity = ObjectIdentity
qtechUrpfMIBCompliances = _QtechUrpfMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 2, 1)
)
_QtechUrpfMIBGroups_ObjectIdentity = ObjectIdentity
qtechUrpfMIBGroups = _QtechUrpfMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 2, 2)
)
qtechUrpfIfMonEntry.registerAugmentions(
    ("QTECH-URPF-MIB",
     "qtechUrpfIfConfEntry")
)
qtechUrpfIfConfEntry.setIndexNames(*qtechUrpfIfMonEntry.getIndexNames())

# Managed Objects groups

qtechUrpfMIBMainObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 2, 2, 1)
)
qtechUrpfMIBMainObjectGroup.setObjects(
      *(("QTECH-URPF-MIB", "qtechUrpfComputeInterval"),
        ("QTECH-URPF-MIB", "qtechUrpfDropRateWindow"),
        ("QTECH-URPF-MIB", "qtechUrpfDropNotifyHoldDownTime"),
        ("QTECH-URPF-MIB", "qtechUrpfDrops"),
        ("QTECH-URPF-MIB", "qtechUrpfDropRate"),
        ("QTECH-URPF-MIB", "qtechUrpfIfDrops"),
        ("QTECH-URPF-MIB", "qtechUrpfIfDropRate"),
        ("QTECH-URPF-MIB", "qtechUrpfIfCheckStrict"),
        ("QTECH-URPF-MIB", "qtechUrpfIfDropRateNotifyEnable"),
        ("QTECH-URPF-MIB", "qtechUrpfIfNotifyDropRateThreshold"),
        ("QTECH-URPF-MIB", "qtechUrpfIfNotifyDrHoldDownReset"))
)
if mibBuilder.loadTexts:
    qtechUrpfMIBMainObjectGroup.setStatus("current")

qtechUrpfMIBVrfObjectGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 2, 2, 2)
)
qtechUrpfMIBVrfObjectGroup.setObjects(
      *(("QTECH-URPF-MIB", "qtechUrpfIfWhichRouteTableID"),
        ("QTECH-URPF-MIB", "qtechUrpfIfVrfName"))
)
if mibBuilder.loadTexts:
    qtechUrpfMIBVrfObjectGroup.setStatus("current")


# Notification objects

qtechUrpfIfDropRateNotify = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 1, 1)
)
qtechUrpfIfDropRateNotify.setObjects(
    ("QTECH-URPF-MIB", "qtechUrpfIfDropRate")
)
if mibBuilder.loadTexts:
    qtechUrpfIfDropRateNotify.setStatus(
        "current"
    )


# Notifications groups

qtechUrpfMIBNotifyGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 2, 2, 3)
)
qtechUrpfMIBNotifyGroup.setObjects(
    ("QTECH-URPF-MIB", "qtechUrpfIfDropRateNotify")
)
if mibBuilder.loadTexts:
    qtechUrpfMIBNotifyGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

qtechUrpfMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 46, 2, 1, 1)
)
qtechUrpfMIBCompliance.setObjects(
      *(("QTECH-URPF-MIB", "qtechUrpfMIBMainObjectGroup"),
        ("QTECH-URPF-MIB", "qtechUrpfMIBNotifyGroup"),
        ("QTECH-URPF-MIB", "qtechUrpfMIBVrfObjectGroup"))
)
if mibBuilder.loadTexts:
    qtechUrpfMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-URPF-MIB",
    **{"qtechUrpfMIB": qtechUrpfMIB,
       "qtechUrpfMIBObjects": qtechUrpfMIBObjects,
       "qtechUrpfScalar": qtechUrpfScalar,
       "qtechUrpfComputeInterval": qtechUrpfComputeInterval,
       "qtechUrpfDropRateWindow": qtechUrpfDropRateWindow,
       "qtechUrpfDropNotifyHoldDownTime": qtechUrpfDropNotifyHoldDownTime,
       "qtechUrpfStatistics": qtechUrpfStatistics,
       "qtechUrpfTable": qtechUrpfTable,
       "qtechUrpfEntry": qtechUrpfEntry,
       "qtechUrpfIpVersion": qtechUrpfIpVersion,
       "qtechUrpfDrops": qtechUrpfDrops,
       "qtechUrpfDropRate": qtechUrpfDropRate,
       "qtechUrpfIfMonTable": qtechUrpfIfMonTable,
       "qtechUrpfIfMonEntry": qtechUrpfIfMonEntry,
       "qtechUrpfIfIpVersion": qtechUrpfIfIpVersion,
       "qtechUrpfIfDrops": qtechUrpfIfDrops,
       "qtechUrpfIfDropRate": qtechUrpfIfDropRate,
       "qtechUrpfInterfaceConfig": qtechUrpfInterfaceConfig,
       "qtechUrpfIfConfTable": qtechUrpfIfConfTable,
       "qtechUrpfIfConfEntry": qtechUrpfIfConfEntry,
       "qtechUrpfIfCheckStrict": qtechUrpfIfCheckStrict,
       "qtechUrpfIfDropRateNotifyEnable": qtechUrpfIfDropRateNotifyEnable,
       "qtechUrpfIfNotifyDropRateThreshold": qtechUrpfIfNotifyDropRateThreshold,
       "qtechUrpfIfNotifyDrHoldDownReset": qtechUrpfIfNotifyDrHoldDownReset,
       "qtechUrpfIfWhichRouteTableID": qtechUrpfIfWhichRouteTableID,
       "qtechUrpfIfVrfName": qtechUrpfIfVrfName,
       "qtechUrpfMIBNotifs": qtechUrpfMIBNotifs,
       "qtechUrpfIfDropRateNotify": qtechUrpfIfDropRateNotify,
       "qtechUrpfMIBConformance": qtechUrpfMIBConformance,
       "qtechUrpfMIBCompliances": qtechUrpfMIBCompliances,
       "qtechUrpfMIBCompliance": qtechUrpfMIBCompliance,
       "qtechUrpfMIBGroups": qtechUrpfMIBGroups,
       "qtechUrpfMIBMainObjectGroup": qtechUrpfMIBMainObjectGroup,
       "qtechUrpfMIBVrfObjectGroup": qtechUrpfMIBVrfObjectGroup,
       "qtechUrpfMIBNotifyGroup": qtechUrpfMIBNotifyGroup}
)
