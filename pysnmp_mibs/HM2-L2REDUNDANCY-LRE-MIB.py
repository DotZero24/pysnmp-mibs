# SNMP MIB module (HM2-L2REDUNDANCY-LRE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HM2-L2REDUNDANCY-LRE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:06 2025
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

(hm2L2RedundancyMibObjects,) = mibBuilder.importSymbols(
    "HM2-L2REDUNDANCY-MIB",
    "hm2L2RedundancyMibObjects")

(lreInterfaceConfigIndex,
 lreInterfaceStatsIndex) = mibBuilder.importSymbols(
    "IEC-62439-3-MIB",
    "lreInterfaceConfigIndex",
    "lreInterfaceStatsIndex")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

hm2LreMibGroup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2)
)
if mibBuilder.loadTexts:
    hm2LreMibGroup.setRevisions(
        ("2012-07-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Hm2LreEntityNotifications_ObjectIdentity = ObjectIdentity
hm2LreEntityNotifications = _Hm2LreEntityNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 0)
)
_Hm2LreEntityObjects_ObjectIdentity = ObjectIdentity
hm2LreEntityObjects = _Hm2LreEntityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1)
)
_Hm2LreConfiguration_ObjectIdentity = ObjectIdentity
hm2LreConfiguration = _Hm2LreConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1)
)
_Hm2LreConfigurationGeneralGroup_ObjectIdentity = ObjectIdentity
hm2LreConfigurationGeneralGroup = _Hm2LreConfigurationGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 1)
)
_Hm2LreConfigurationInterfaceGroup_ObjectIdentity = ObjectIdentity
hm2LreConfigurationInterfaceGroup = _Hm2LreConfigurationInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2)
)
_Hm2LreConfigurationInterfaces_ObjectIdentity = ObjectIdentity
hm2LreConfigurationInterfaces = _Hm2LreConfigurationInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1)
)
_Hm2LreInterfaceConfigTable_Object = MibTable
hm2LreInterfaceConfigTable = _Hm2LreInterfaceConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hm2LreInterfaceConfigTable.setStatus("current")
_Hm2LreInterfaceConfigEntry_Object = MibTableRow
hm2LreInterfaceConfigEntry = _Hm2LreInterfaceConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1)
)
hm2LreInterfaceConfigEntry.setIndexNames(
    (0, "IEC-62439-3-MIB", "lreInterfaceConfigIndex"),
)
if mibBuilder.loadTexts:
    hm2LreInterfaceConfigEntry.setStatus("current")
_Hm2LreInterfaceA_Type = InterfaceIndex
_Hm2LreInterfaceA_Object = MibTableColumn
hm2LreInterfaceA = _Hm2LreInterfaceA_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 1),
    _Hm2LreInterfaceA_Type()
)
hm2LreInterfaceA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreInterfaceA.setStatus("current")
_Hm2LreInterfaceB_Type = InterfaceIndex
_Hm2LreInterfaceB_Object = MibTableColumn
hm2LreInterfaceB = _Hm2LreInterfaceB_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 2),
    _Hm2LreInterfaceB_Type()
)
hm2LreInterfaceB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreInterfaceB.setStatus("current")
_Hm2LreProxyNodeTableSize_Type = Unsigned32
_Hm2LreProxyNodeTableSize_Object = MibTableColumn
hm2LreProxyNodeTableSize = _Hm2LreProxyNodeTableSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 3),
    _Hm2LreProxyNodeTableSize_Type()
)
hm2LreProxyNodeTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreProxyNodeTableSize.setStatus("current")


class _Hm2LreSupervisionTxEnable_Type(TruthValue):
    """Custom type hm2LreSupervisionTxEnable based on TruthValue"""
    defaultValue = 1


_Hm2LreSupervisionTxEnable_Type.__name__ = "TruthValue"
_Hm2LreSupervisionTxEnable_Object = MibTableColumn
hm2LreSupervisionTxEnable = _Hm2LreSupervisionTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 4),
    _Hm2LreSupervisionTxEnable_Type()
)
hm2LreSupervisionTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LreSupervisionTxEnable.setStatus("current")


class _Hm2LreSupervisionVDANsTxEnable_Type(TruthValue):
    """Custom type hm2LreSupervisionVDANsTxEnable based on TruthValue"""
    defaultValue = 1


_Hm2LreSupervisionVDANsTxEnable_Type.__name__ = "TruthValue"
_Hm2LreSupervisionVDANsTxEnable_Object = MibTableColumn
hm2LreSupervisionVDANsTxEnable = _Hm2LreSupervisionVDANsTxEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 5),
    _Hm2LreSupervisionVDANsTxEnable_Type()
)
hm2LreSupervisionVDANsTxEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LreSupervisionVDANsTxEnable.setStatus("current")


class _Hm2LreStatisticsClear_Type(Integer32):
    """Custom type hm2LreStatisticsClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("clearStatistics", 1))
    )


_Hm2LreStatisticsClear_Type.__name__ = "Integer32"
_Hm2LreStatisticsClear_Object = MibTableColumn
hm2LreStatisticsClear = _Hm2LreStatisticsClear_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 6),
    _Hm2LreStatisticsClear_Type()
)
hm2LreStatisticsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LreStatisticsClear.setStatus("current")
_Hm2LreMaxFrameSizeLimit_Type = Unsigned32
_Hm2LreMaxFrameSizeLimit_Object = MibTableColumn
hm2LreMaxFrameSizeLimit = _Hm2LreMaxFrameSizeLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 7),
    _Hm2LreMaxFrameSizeLimit_Type()
)
hm2LreMaxFrameSizeLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreMaxFrameSizeLimit.setStatus("current")
_Hm2LreMaxFrameSize_Type = Unsigned32
_Hm2LreMaxFrameSize_Object = MibTableColumn
hm2LreMaxFrameSize = _Hm2LreMaxFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 8),
    _Hm2LreMaxFrameSize_Type()
)
hm2LreMaxFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LreMaxFrameSize.setStatus("current")


class _Hm2LreSpeed_Type(Integer32):
    """Custom type hm2LreSpeed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lreSpeed100Mbps", 1),
          ("lreSpeed1Gbps", 2))
    )


_Hm2LreSpeed_Type.__name__ = "Integer32"
_Hm2LreSpeed_Object = MibTableColumn
hm2LreSpeed = _Hm2LreSpeed_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 9),
    _Hm2LreSpeed_Type()
)
hm2LreSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LreSpeed.setStatus("current")


class _Hm2LreDuplicateDetectionAging_Type(Unsigned32):
    """Custom type hm2LreDuplicateDetectionAging based on Unsigned32"""
    defaultValue = 400

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 5000),
    )


_Hm2LreDuplicateDetectionAging_Type.__name__ = "Unsigned32"
_Hm2LreDuplicateDetectionAging_Object = MibTableColumn
hm2LreDuplicateDetectionAging = _Hm2LreDuplicateDetectionAging_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 10),
    _Hm2LreDuplicateDetectionAging_Type()
)
hm2LreDuplicateDetectionAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LreDuplicateDetectionAging.setStatus("current")


class _Hm2LreProxyNodeTableAging_Type(Unsigned32):
    """Custom type hm2LreProxyNodeTableAging based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 300),
    )


_Hm2LreProxyNodeTableAging_Type.__name__ = "Unsigned32"
_Hm2LreProxyNodeTableAging_Object = MibTableColumn
hm2LreProxyNodeTableAging = _Hm2LreProxyNodeTableAging_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 1, 2, 1, 1, 1, 11),
    _Hm2LreProxyNodeTableAging_Type()
)
hm2LreProxyNodeTableAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hm2LreProxyNodeTableAging.setStatus("current")
_Hm2LreStatistics_ObjectIdentity = ObjectIdentity
hm2LreStatistics = _Hm2LreStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2)
)
_Hm2LreStatisticsInterfaceGroup_ObjectIdentity = ObjectIdentity
hm2LreStatisticsInterfaceGroup = _Hm2LreStatisticsInterfaceGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1)
)
_Hm2LreStatisticsInterfaces_ObjectIdentity = ObjectIdentity
hm2LreStatisticsInterfaces = _Hm2LreStatisticsInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1)
)
_Hm2LreInterfaceStatsTable_Object = MibTable
hm2LreInterfaceStatsTable = _Hm2LreInterfaceStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hm2LreInterfaceStatsTable.setStatus("current")
_Hm2LreInterfaceStatsEntry_Object = MibTableRow
hm2LreInterfaceStatsEntry = _Hm2LreInterfaceStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1)
)
hm2LreInterfaceStatsEntry.setIndexNames(
    (0, "IEC-62439-3-MIB", "lreInterfaceStatsIndex"),
)
if mibBuilder.loadTexts:
    hm2LreInterfaceStatsEntry.setStatus("current")
_Hm2LreProxyNodeTableEntries_Type = Unsigned32
_Hm2LreProxyNodeTableEntries_Object = MibTableColumn
hm2LreProxyNodeTableEntries = _Hm2LreProxyNodeTableEntries_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 1),
    _Hm2LreProxyNodeTableEntries_Type()
)
hm2LreProxyNodeTableEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreProxyNodeTableEntries.setStatus("current")
_Hm2LreRxAError_Type = Counter32
_Hm2LreRxAError_Object = MibTableColumn
hm2LreRxAError = _Hm2LreRxAError_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 2),
    _Hm2LreRxAError_Type()
)
hm2LreRxAError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxAError.setStatus("current")
_Hm2LreRxACrcError_Type = Counter32
_Hm2LreRxACrcError_Object = MibTableColumn
hm2LreRxACrcError = _Hm2LreRxACrcError_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 3),
    _Hm2LreRxACrcError_Type()
)
hm2LreRxACrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxACrcError.setStatus("current")
_Hm2LreRxBError_Type = Counter32
_Hm2LreRxBError_Object = MibTableColumn
hm2LreRxBError = _Hm2LreRxBError_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 4),
    _Hm2LreRxBError_Type()
)
hm2LreRxBError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxBError.setStatus("current")
_Hm2LreRxBCrcError_Type = Counter32
_Hm2LreRxBCrcError_Object = MibTableColumn
hm2LreRxBCrcError = _Hm2LreRxBCrcError_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 5),
    _Hm2LreRxBCrcError_Type()
)
hm2LreRxBCrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxBCrcError.setStatus("current")
_Hm2LreRxIError_Type = Counter32
_Hm2LreRxIError_Object = MibTableColumn
hm2LreRxIError = _Hm2LreRxIError_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 6),
    _Hm2LreRxIError_Type()
)
hm2LreRxIError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxIError.setStatus("current")
_Hm2LreRxICrcError_Type = Counter32
_Hm2LreRxICrcError_Object = MibTableColumn
hm2LreRxICrcError = _Hm2LreRxICrcError_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 7),
    _Hm2LreRxICrcError_Type()
)
hm2LreRxICrcError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxICrcError.setStatus("current")
_Hm2LreRxAWrongLan_Type = Counter32
_Hm2LreRxAWrongLan_Object = MibTableColumn
hm2LreRxAWrongLan = _Hm2LreRxAWrongLan_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 8),
    _Hm2LreRxAWrongLan_Type()
)
hm2LreRxAWrongLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxAWrongLan.setStatus("current")
_Hm2LreRxBWrongLan_Type = Counter32
_Hm2LreRxBWrongLan_Object = MibTableColumn
hm2LreRxBWrongLan = _Hm2LreRxBWrongLan_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 9),
    _Hm2LreRxBWrongLan_Type()
)
hm2LreRxBWrongLan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxBWrongLan.setStatus("current")
_Hm2LreRxAllFrameA_Type = Counter32
_Hm2LreRxAllFrameA_Object = MibTableColumn
hm2LreRxAllFrameA = _Hm2LreRxAllFrameA_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 10),
    _Hm2LreRxAllFrameA_Type()
)
hm2LreRxAllFrameA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxAllFrameA.setStatus("current")
_Hm2LreRxAllFrameB_Type = Counter32
_Hm2LreRxAllFrameB_Object = MibTableColumn
hm2LreRxAllFrameB = _Hm2LreRxAllFrameB_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 11),
    _Hm2LreRxAllFrameB_Type()
)
hm2LreRxAllFrameB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxAllFrameB.setStatus("current")
_Hm2LreRxAllFrameIl_Type = Counter32
_Hm2LreRxAllFrameIl_Object = MibTableColumn
hm2LreRxAllFrameIl = _Hm2LreRxAllFrameIl_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 12),
    _Hm2LreRxAllFrameIl_Type()
)
hm2LreRxAllFrameIl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxAllFrameIl.setStatus("current")
_Hm2LreRxShortFrameA_Type = Counter32
_Hm2LreRxShortFrameA_Object = MibTableColumn
hm2LreRxShortFrameA = _Hm2LreRxShortFrameA_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 13),
    _Hm2LreRxShortFrameA_Type()
)
hm2LreRxShortFrameA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxShortFrameA.setStatus("current")
_Hm2LreRxShortFrameB_Type = Counter32
_Hm2LreRxShortFrameB_Object = MibTableColumn
hm2LreRxShortFrameB = _Hm2LreRxShortFrameB_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 14),
    _Hm2LreRxShortFrameB_Type()
)
hm2LreRxShortFrameB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxShortFrameB.setStatus("current")
_Hm2LreRxLongFrameA_Type = Counter32
_Hm2LreRxLongFrameA_Object = MibTableColumn
hm2LreRxLongFrameA = _Hm2LreRxLongFrameA_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 15),
    _Hm2LreRxLongFrameA_Type()
)
hm2LreRxLongFrameA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxLongFrameA.setStatus("current")
_Hm2LreRxLongFrameB_Type = Counter32
_Hm2LreRxLongFrameB_Object = MibTableColumn
hm2LreRxLongFrameB = _Hm2LreRxLongFrameB_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 16),
    _Hm2LreRxLongFrameB_Type()
)
hm2LreRxLongFrameB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxLongFrameB.setStatus("current")
_Hm2LreRxADiscard_Type = Counter32
_Hm2LreRxADiscard_Object = MibTableColumn
hm2LreRxADiscard = _Hm2LreRxADiscard_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 17),
    _Hm2LreRxADiscard_Type()
)
hm2LreRxADiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxADiscard.setStatus("current")
_Hm2LreRxBDiscard_Type = Counter32
_Hm2LreRxBDiscard_Object = MibTableColumn
hm2LreRxBDiscard = _Hm2LreRxBDiscard_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 18),
    _Hm2LreRxBDiscard_Type()
)
hm2LreRxBDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxBDiscard.setStatus("current")
_Hm2LreRxIlDiscard_Type = Counter32
_Hm2LreRxIlDiscard_Object = MibTableColumn
hm2LreRxIlDiscard = _Hm2LreRxIlDiscard_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 19),
    _Hm2LreRxIlDiscard_Type()
)
hm2LreRxIlDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxIlDiscard.setStatus("current")
_Hm2LreRxCpuDiscard_Type = Counter32
_Hm2LreRxCpuDiscard_Object = MibTableColumn
hm2LreRxCpuDiscard = _Hm2LreRxCpuDiscard_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 20),
    _Hm2LreRxCpuDiscard_Type()
)
hm2LreRxCpuDiscard.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreRxCpuDiscard.setStatus("current")
_Hm2LreTxARct_Type = Counter32
_Hm2LreTxARct_Object = MibTableColumn
hm2LreTxARct = _Hm2LreTxARct_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 21),
    _Hm2LreTxARct_Type()
)
hm2LreTxARct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreTxARct.setStatus("current")
_Hm2LreTxAHsr_Type = Counter32
_Hm2LreTxAHsr_Object = MibTableColumn
hm2LreTxAHsr = _Hm2LreTxAHsr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 22),
    _Hm2LreTxAHsr_Type()
)
hm2LreTxAHsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreTxAHsr.setStatus("current")
_Hm2LreTxAWithoutRct_Type = Counter32
_Hm2LreTxAWithoutRct_Object = MibTableColumn
hm2LreTxAWithoutRct = _Hm2LreTxAWithoutRct_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 23),
    _Hm2LreTxAWithoutRct_Type()
)
hm2LreTxAWithoutRct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreTxAWithoutRct.setStatus("current")
_Hm2LreTxBRct_Type = Counter32
_Hm2LreTxBRct_Object = MibTableColumn
hm2LreTxBRct = _Hm2LreTxBRct_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 24),
    _Hm2LreTxBRct_Type()
)
hm2LreTxBRct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreTxBRct.setStatus("current")
_Hm2LreTxBHsr_Type = Counter32
_Hm2LreTxBHsr_Object = MibTableColumn
hm2LreTxBHsr = _Hm2LreTxBHsr_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 25),
    _Hm2LreTxBHsr_Type()
)
hm2LreTxBHsr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreTxBHsr.setStatus("current")
_Hm2LreTxBWithoutRct_Type = Counter32
_Hm2LreTxBWithoutRct_Object = MibTableColumn
hm2LreTxBWithoutRct = _Hm2LreTxBWithoutRct_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 26),
    _Hm2LreTxBWithoutRct_Type()
)
hm2LreTxBWithoutRct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreTxBWithoutRct.setStatus("current")
_Hm2LreTxIlRct_Type = Counter32
_Hm2LreTxIlRct_Object = MibTableColumn
hm2LreTxIlRct = _Hm2LreTxIlRct_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 27),
    _Hm2LreTxIlRct_Type()
)
hm2LreTxIlRct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreTxIlRct.setStatus("current")
_Hm2LreTxIlWithoutRct_Type = Counter32
_Hm2LreTxIlWithoutRct_Object = MibTableColumn
hm2LreTxIlWithoutRct = _Hm2LreTxIlWithoutRct_Object(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 1, 2, 1, 1, 1, 1, 28),
    _Hm2LreTxIlWithoutRct_Type()
)
hm2LreTxIlWithoutRct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hm2LreTxIlWithoutRct.setStatus("current")
_Hm2LreEntityConformance_ObjectIdentity = ObjectIdentity
hm2LreEntityConformance = _Hm2LreEntityConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 11, 40, 1, 2, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HM2-L2REDUNDANCY-LRE-MIB",
    **{"hm2LreMibGroup": hm2LreMibGroup,
       "hm2LreEntityNotifications": hm2LreEntityNotifications,
       "hm2LreEntityObjects": hm2LreEntityObjects,
       "hm2LreConfiguration": hm2LreConfiguration,
       "hm2LreConfigurationGeneralGroup": hm2LreConfigurationGeneralGroup,
       "hm2LreConfigurationInterfaceGroup": hm2LreConfigurationInterfaceGroup,
       "hm2LreConfigurationInterfaces": hm2LreConfigurationInterfaces,
       "hm2LreInterfaceConfigTable": hm2LreInterfaceConfigTable,
       "hm2LreInterfaceConfigEntry": hm2LreInterfaceConfigEntry,
       "hm2LreInterfaceA": hm2LreInterfaceA,
       "hm2LreInterfaceB": hm2LreInterfaceB,
       "hm2LreProxyNodeTableSize": hm2LreProxyNodeTableSize,
       "hm2LreSupervisionTxEnable": hm2LreSupervisionTxEnable,
       "hm2LreSupervisionVDANsTxEnable": hm2LreSupervisionVDANsTxEnable,
       "hm2LreStatisticsClear": hm2LreStatisticsClear,
       "hm2LreMaxFrameSizeLimit": hm2LreMaxFrameSizeLimit,
       "hm2LreMaxFrameSize": hm2LreMaxFrameSize,
       "hm2LreSpeed": hm2LreSpeed,
       "hm2LreDuplicateDetectionAging": hm2LreDuplicateDetectionAging,
       "hm2LreProxyNodeTableAging": hm2LreProxyNodeTableAging,
       "hm2LreStatistics": hm2LreStatistics,
       "hm2LreStatisticsInterfaceGroup": hm2LreStatisticsInterfaceGroup,
       "hm2LreStatisticsInterfaces": hm2LreStatisticsInterfaces,
       "hm2LreInterfaceStatsTable": hm2LreInterfaceStatsTable,
       "hm2LreInterfaceStatsEntry": hm2LreInterfaceStatsEntry,
       "hm2LreProxyNodeTableEntries": hm2LreProxyNodeTableEntries,
       "hm2LreRxAError": hm2LreRxAError,
       "hm2LreRxACrcError": hm2LreRxACrcError,
       "hm2LreRxBError": hm2LreRxBError,
       "hm2LreRxBCrcError": hm2LreRxBCrcError,
       "hm2LreRxIError": hm2LreRxIError,
       "hm2LreRxICrcError": hm2LreRxICrcError,
       "hm2LreRxAWrongLan": hm2LreRxAWrongLan,
       "hm2LreRxBWrongLan": hm2LreRxBWrongLan,
       "hm2LreRxAllFrameA": hm2LreRxAllFrameA,
       "hm2LreRxAllFrameB": hm2LreRxAllFrameB,
       "hm2LreRxAllFrameIl": hm2LreRxAllFrameIl,
       "hm2LreRxShortFrameA": hm2LreRxShortFrameA,
       "hm2LreRxShortFrameB": hm2LreRxShortFrameB,
       "hm2LreRxLongFrameA": hm2LreRxLongFrameA,
       "hm2LreRxLongFrameB": hm2LreRxLongFrameB,
       "hm2LreRxADiscard": hm2LreRxADiscard,
       "hm2LreRxBDiscard": hm2LreRxBDiscard,
       "hm2LreRxIlDiscard": hm2LreRxIlDiscard,
       "hm2LreRxCpuDiscard": hm2LreRxCpuDiscard,
       "hm2LreTxARct": hm2LreTxARct,
       "hm2LreTxAHsr": hm2LreTxAHsr,
       "hm2LreTxAWithoutRct": hm2LreTxAWithoutRct,
       "hm2LreTxBRct": hm2LreTxBRct,
       "hm2LreTxBHsr": hm2LreTxBHsr,
       "hm2LreTxBWithoutRct": hm2LreTxBWithoutRct,
       "hm2LreTxIlRct": hm2LreTxIlRct,
       "hm2LreTxIlWithoutRct": hm2LreTxIlWithoutRct,
       "hm2LreEntityConformance": hm2LreEntityConformance}
)
