# SNMP MIB module (ADTRAN-GENERIC-VECTORING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-VECTORING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:25 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenVector,
 adGenVectorID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenVector",
    "adGenVectorID")

(adTAeSCUTrapAlarmLevel,) = mibBuilder.importSymbols(
    "ADTRAN-TAeSCUEXT1-MIB",
    "adTAeSCUTrapAlarmLevel")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenVectorMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 57, 1)
)
if mibBuilder.loadTexts:
    adGenVectorMIB.setRevisions(
        ("2018-02-01 00:00",
         "2017-06-14 00:00",
         "2016-09-22 00:00",
         "2015-08-13 00:00",
         "2015-07-17 00:00",
         "2015-05-27 00:00",
         "2014-07-26 00:00",
         "2014-07-25 00:00",
         "2014-03-03 00:00",
         "2013-11-26 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenVectorMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("blv", 1),
          ("slv", 2),
          ("both", 3),
          ("none", 4),
          ("dlv", 5),
          ("blv-dlv-slv", 7))
    )



class AdGenVectorGroupOperStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("upPartial", 3))
    )



class AdGenVectorLastChange(TextualConvention, TimeTicks):
    status = "current"


class AdGenVectorPhyPortErrorTimestamp(TextualConvention, TimeTicks):
    status = "current"


class AdGenVectorPhyLineState(TextualConvention, Integer32):
    status = "current"
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
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("notAvailable", 0),
          ("down", 1),
          ("train", 2),
          ("up", 3),
          ("deltActive", 4),
          ("deltDataExchange", 5),
          ("deltDataRequest", 6),
          ("deltComplete", 7),
          ("seltActive", 8),
          ("seltDataRequest", 9),
          ("seltComplete", 10))
    )



class AdGenVectorPhyPortVectoringState(TextualConvention, Integer32):
    status = "current"
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("idle", 0),
          ("dsInit-1-0", 1),
          ("dsInit-2-1", 2),
          ("usInit-1", 3),
          ("usInit-2", 4),
          ("steady", 5),
          ("trans", 6),
          ("waitForStart", 7),
          ("dsInit-1-1", 8),
          ("dsInit-2-0", 9),
          ("reset", 10),
          ("nonVectoring", 11),
          ("handshake", 12),
          ("waitForStart-Legacy", 13),
          ("init-Legacy", 14),
          ("steady-Legacy", 15),
          ("steadyB", 16),
          ("stopPending", 17),
          ("idle-FF", 18),
          ("dsInit-1-0-ff", 19),
          ("dsInit-2-1-ff", 20),
          ("usInit-1-ff", 21),
          ("usInit-2-ff", 22),
          ("steady-ff", 23),
          ("trans-ff", 24),
          ("waitForStart-ff", 25),
          ("dsInit-1-1-ff", 26),
          ("dsInit-2-0-ff", 27),
          ("steadyB-ff", 28),
          ("stopPending-ff", 29),
          ("unknown", 30),
          ("fallback", 31))
    )



class AdGenVectorGroupBandPlans(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("g998", 1),
          ("g998e", 2),
          ("g998ade", 3),
          ("g997", 4),
          ("g997e", 5),
          ("hpe", 6))
    )



class AdGenVectorGroupFallbackModes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("adsl2-multimode", 1),
          ("shutdown", 2),
          ("adsl2", 3),
          ("non-vectored", 4))
    )



# MIB Managed Objects in the order of their OIDs

_AdGenVectorMIBObjects_ObjectIdentity = ObjectIdentity
adGenVectorMIBObjects = _AdGenVectorMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1)
)
_AdGenVectorModuleConfTable_Object = MibTable
adGenVectorModuleConfTable = _AdGenVectorModuleConfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 1)
)
if mibBuilder.loadTexts:
    adGenVectorModuleConfTable.setStatus("current")
_AdGenVectorModuleConfEntry_Object = MibTableRow
adGenVectorModuleConfEntry = _AdGenVectorModuleConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 1, 1)
)
adGenVectorModuleConfEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenVectorModuleConfEntry.setStatus("current")
_AdGenVectorModuleConfSupportedVectorModeTypes_Type = AdGenVectorMode
_AdGenVectorModuleConfSupportedVectorModeTypes_Object = MibTableColumn
adGenVectorModuleConfSupportedVectorModeTypes = _AdGenVectorModuleConfSupportedVectorModeTypes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 1, 1, 1),
    _AdGenVectorModuleConfSupportedVectorModeTypes_Type()
)
adGenVectorModuleConfSupportedVectorModeTypes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorModuleConfSupportedVectorModeTypes.setStatus("current")
_AdGenVectorModuleConfMaxBLVGroups_Type = Integer32
_AdGenVectorModuleConfMaxBLVGroups_Object = MibTableColumn
adGenVectorModuleConfMaxBLVGroups = _AdGenVectorModuleConfMaxBLVGroups_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 1, 1, 2),
    _AdGenVectorModuleConfMaxBLVGroups_Type()
)
adGenVectorModuleConfMaxBLVGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorModuleConfMaxBLVGroups.setStatus("current")
_AdGenVectorModuleConfMaxSLVGroups_Type = Integer32
_AdGenVectorModuleConfMaxSLVGroups_Object = MibTableColumn
adGenVectorModuleConfMaxSLVGroups = _AdGenVectorModuleConfMaxSLVGroups_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 1, 1, 3),
    _AdGenVectorModuleConfMaxSLVGroups_Type()
)
adGenVectorModuleConfMaxSLVGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorModuleConfMaxSLVGroups.setStatus("current")
_AdGenVectorModuleConfMaxPhysPerSLVGroup_Type = Integer32
_AdGenVectorModuleConfMaxPhysPerSLVGroup_Object = MibTableColumn
adGenVectorModuleConfMaxPhysPerSLVGroup = _AdGenVectorModuleConfMaxPhysPerSLVGroup_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 1, 1, 4),
    _AdGenVectorModuleConfMaxPhysPerSLVGroup_Type()
)
adGenVectorModuleConfMaxPhysPerSLVGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorModuleConfMaxPhysPerSLVGroup.setStatus("current")
_AdGenVectorModuleConfNumPhys_Type = Integer32
_AdGenVectorModuleConfNumPhys_Object = MibTableColumn
adGenVectorModuleConfNumPhys = _AdGenVectorModuleConfNumPhys_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 1, 1, 5),
    _AdGenVectorModuleConfNumPhys_Type()
)
adGenVectorModuleConfNumPhys.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorModuleConfNumPhys.setStatus("current")
_AdGenVectorModuleConfVectorEngineHwRev_Type = DisplayString
_AdGenVectorModuleConfVectorEngineHwRev_Object = MibTableColumn
adGenVectorModuleConfVectorEngineHwRev = _AdGenVectorModuleConfVectorEngineHwRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 1, 1, 6),
    _AdGenVectorModuleConfVectorEngineHwRev_Type()
)
adGenVectorModuleConfVectorEngineHwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorModuleConfVectorEngineHwRev.setStatus("current")
_AdGenVectorModuleConfVectorEngineSwRev_Type = DisplayString
_AdGenVectorModuleConfVectorEngineSwRev_Object = MibTableColumn
adGenVectorModuleConfVectorEngineSwRev = _AdGenVectorModuleConfVectorEngineSwRev_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 1, 1, 7),
    _AdGenVectorModuleConfVectorEngineSwRev_Type()
)
adGenVectorModuleConfVectorEngineSwRev.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorModuleConfVectorEngineSwRev.setStatus("current")
_AdGenVectorGroupTableLastError_Type = DisplayString
_AdGenVectorGroupTableLastError_Object = MibScalar
adGenVectorGroupTableLastError = _AdGenVectorGroupTableLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 2),
    _AdGenVectorGroupTableLastError_Type()
)
adGenVectorGroupTableLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorGroupTableLastError.setStatus("current")
_AdGenVectorGroupTable_Object = MibTable
adGenVectorGroupTable = _AdGenVectorGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3)
)
if mibBuilder.loadTexts:
    adGenVectorGroupTable.setStatus("current")
_AdGenVectorGroupEntry_Object = MibTableRow
adGenVectorGroupEntry = _AdGenVectorGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1)
)
adGenVectorGroupEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-VECTORING-MIB", "adGenVectorGroupIfIndex"),
)
if mibBuilder.loadTexts:
    adGenVectorGroupEntry.setStatus("current")
_AdGenVectorGroupIfIndex_Type = InterfaceIndex
_AdGenVectorGroupIfIndex_Object = MibTableColumn
adGenVectorGroupIfIndex = _AdGenVectorGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1, 1),
    _AdGenVectorGroupIfIndex_Type()
)
adGenVectorGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVectorGroupIfIndex.setStatus("current")


class _AdGenVectorGroupDescription_Type(DisplayString):
    """Custom type adGenVectorGroupDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenVectorGroupDescription_Type.__name__ = "DisplayString"
_AdGenVectorGroupDescription_Object = MibTableColumn
adGenVectorGroupDescription = _AdGenVectorGroupDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1, 2),
    _AdGenVectorGroupDescription_Type()
)
adGenVectorGroupDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVectorGroupDescription.setStatus("current")
_AdGenVectorGroupLastError_Type = DisplayString
_AdGenVectorGroupLastError_Object = MibTableColumn
adGenVectorGroupLastError = _AdGenVectorGroupLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1, 3),
    _AdGenVectorGroupLastError_Type()
)
adGenVectorGroupLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorGroupLastError.setStatus("current")
_AdGenVectorGroupBandPlan_Type = AdGenVectorGroupBandPlans
_AdGenVectorGroupBandPlan_Object = MibTableColumn
adGenVectorGroupBandPlan = _AdGenVectorGroupBandPlan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1, 4),
    _AdGenVectorGroupBandPlan_Type()
)
adGenVectorGroupBandPlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVectorGroupBandPlan.setStatus("current")
_AdGenVectorGroupRowStatus_Type = RowStatus
_AdGenVectorGroupRowStatus_Object = MibTableColumn
adGenVectorGroupRowStatus = _AdGenVectorGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1, 5),
    _AdGenVectorGroupRowStatus_Type()
)
adGenVectorGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVectorGroupRowStatus.setStatus("current")


class _AdGenVectorGroupFallbackMode_Type(AdGenVectorGroupFallbackModes):
    """Custom type adGenVectorGroupFallbackMode based on AdGenVectorGroupFallbackModes"""
    defaultValue = 3


_AdGenVectorGroupFallbackMode_Type.__name__ = "AdGenVectorGroupFallbackModes"
_AdGenVectorGroupFallbackMode_Object = MibTableColumn
adGenVectorGroupFallbackMode = _AdGenVectorGroupFallbackMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1, 6),
    _AdGenVectorGroupFallbackMode_Type()
)
adGenVectorGroupFallbackMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVectorGroupFallbackMode.setStatus("current")


class _AdGenVectorGroupFallbackAlarmSeverity_Type(Integer32):
    """Custom type adGenVectorGroupFallbackAlarmSeverity based on Integer32"""
    defaultValue = 1

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
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("alert", 3),
          ("info", 4))
    )


_AdGenVectorGroupFallbackAlarmSeverity_Type.__name__ = "Integer32"
_AdGenVectorGroupFallbackAlarmSeverity_Object = MibTableColumn
adGenVectorGroupFallbackAlarmSeverity = _AdGenVectorGroupFallbackAlarmSeverity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1, 7),
    _AdGenVectorGroupFallbackAlarmSeverity_Type()
)
adGenVectorGroupFallbackAlarmSeverity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVectorGroupFallbackAlarmSeverity.setStatus("current")


class _AdGenVectorGroupFallbackAlarmEnable_Type(Integer32):
    """Custom type adGenVectorGroupFallbackAlarmEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdGenVectorGroupFallbackAlarmEnable_Type.__name__ = "Integer32"
_AdGenVectorGroupFallbackAlarmEnable_Object = MibTableColumn
adGenVectorGroupFallbackAlarmEnable = _AdGenVectorGroupFallbackAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1, 8),
    _AdGenVectorGroupFallbackAlarmEnable_Type()
)
adGenVectorGroupFallbackAlarmEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVectorGroupFallbackAlarmEnable.setStatus("current")
_AdGenVectorGroupVectoringMode_Type = AdGenVectorMode
_AdGenVectorGroupVectoringMode_Object = MibTableColumn
adGenVectorGroupVectoringMode = _AdGenVectorGroupVectoringMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1, 9),
    _AdGenVectorGroupVectoringMode_Type()
)
adGenVectorGroupVectoringMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVectorGroupVectoringMode.setStatus("current")


class _AdGenVectorGroupAutoAddEnable_Type(Integer32):
    """Custom type adGenVectorGroupAutoAddEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AdGenVectorGroupAutoAddEnable_Type.__name__ = "Integer32"
_AdGenVectorGroupAutoAddEnable_Object = MibTableColumn
adGenVectorGroupAutoAddEnable = _AdGenVectorGroupAutoAddEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 3, 1, 10),
    _AdGenVectorGroupAutoAddEnable_Type()
)
adGenVectorGroupAutoAddEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVectorGroupAutoAddEnable.setStatus("current")
_AdGenVectorPhyMapTableLastError_Type = DisplayString
_AdGenVectorPhyMapTableLastError_Object = MibScalar
adGenVectorPhyMapTableLastError = _AdGenVectorPhyMapTableLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 4),
    _AdGenVectorPhyMapTableLastError_Type()
)
adGenVectorPhyMapTableLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorPhyMapTableLastError.setStatus("current")
_AdGenVectorPhyMapTable_Object = MibTable
adGenVectorPhyMapTable = _AdGenVectorPhyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 5)
)
if mibBuilder.loadTexts:
    adGenVectorPhyMapTable.setStatus("current")
_AdGenVectorPhyMapEntry_Object = MibTableRow
adGenVectorPhyMapEntry = _AdGenVectorPhyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 5, 1)
)
adGenVectorPhyMapEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-VECTORING-MIB", "adGenVectorPhyMapGroupIfIndex"),
    (0, "ADTRAN-GENERIC-VECTORING-MIB", "adGenVectorPhyMapPhyIfIndex"),
)
if mibBuilder.loadTexts:
    adGenVectorPhyMapEntry.setStatus("current")
_AdGenVectorPhyMapGroupIfIndex_Type = InterfaceIndex
_AdGenVectorPhyMapGroupIfIndex_Object = MibTableColumn
adGenVectorPhyMapGroupIfIndex = _AdGenVectorPhyMapGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 5, 1, 1),
    _AdGenVectorPhyMapGroupIfIndex_Type()
)
adGenVectorPhyMapGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVectorPhyMapGroupIfIndex.setStatus("current")
_AdGenVectorPhyMapPhyIfIndex_Type = InterfaceIndex
_AdGenVectorPhyMapPhyIfIndex_Object = MibTableColumn
adGenVectorPhyMapPhyIfIndex = _AdGenVectorPhyMapPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 5, 1, 2),
    _AdGenVectorPhyMapPhyIfIndex_Type()
)
adGenVectorPhyMapPhyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVectorPhyMapPhyIfIndex.setStatus("current")
_AdGenVectorPhyMapLastChange_Type = AdGenVectorLastChange
_AdGenVectorPhyMapLastChange_Object = MibTableColumn
adGenVectorPhyMapLastChange = _AdGenVectorPhyMapLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 5, 1, 3),
    _AdGenVectorPhyMapLastChange_Type()
)
adGenVectorPhyMapLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorPhyMapLastChange.setStatus("current")
_AdGenVectorPhyMapLastError_Type = DisplayString
_AdGenVectorPhyMapLastError_Object = MibTableColumn
adGenVectorPhyMapLastError = _AdGenVectorPhyMapLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 5, 1, 4),
    _AdGenVectorPhyMapLastError_Type()
)
adGenVectorPhyMapLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorPhyMapLastError.setStatus("current")
_AdGenVectorPhyMapRowStatus_Type = RowStatus
_AdGenVectorPhyMapRowStatus_Object = MibTableColumn
adGenVectorPhyMapRowStatus = _AdGenVectorPhyMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 5, 1, 5),
    _AdGenVectorPhyMapRowStatus_Type()
)
adGenVectorPhyMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVectorPhyMapRowStatus.setStatus("current")
_AdGenVectorGroupStatusTable_Object = MibTable
adGenVectorGroupStatusTable = _AdGenVectorGroupStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6)
)
if mibBuilder.loadTexts:
    adGenVectorGroupStatusTable.setStatus("current")
_AdGenVectorGroupStatusEntry_Object = MibTableRow
adGenVectorGroupStatusEntry = _AdGenVectorGroupStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1)
)
adGenVectorGroupStatusEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-VECTORING-MIB", "adGenVectorGroupStatusIfIndex"),
)
if mibBuilder.loadTexts:
    adGenVectorGroupStatusEntry.setStatus("current")
_AdGenVectorGroupStatusIfIndex_Type = InterfaceIndex
_AdGenVectorGroupStatusIfIndex_Object = MibTableColumn
adGenVectorGroupStatusIfIndex = _AdGenVectorGroupStatusIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1, 1),
    _AdGenVectorGroupStatusIfIndex_Type()
)
adGenVectorGroupStatusIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVectorGroupStatusIfIndex.setStatus("current")
_AdGenVectorGroupStatusNumProvisionedPorts_Type = Integer32
_AdGenVectorGroupStatusNumProvisionedPorts_Object = MibTableColumn
adGenVectorGroupStatusNumProvisionedPorts = _AdGenVectorGroupStatusNumProvisionedPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1, 2),
    _AdGenVectorGroupStatusNumProvisionedPorts_Type()
)
adGenVectorGroupStatusNumProvisionedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorGroupStatusNumProvisionedPorts.setStatus("current")
_AdGenVectorGroupStatusNumVectoredPorts_Type = Integer32
_AdGenVectorGroupStatusNumVectoredPorts_Object = MibTableColumn
adGenVectorGroupStatusNumVectoredPorts = _AdGenVectorGroupStatusNumVectoredPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1, 3),
    _AdGenVectorGroupStatusNumVectoredPorts_Type()
)
adGenVectorGroupStatusNumVectoredPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorGroupStatusNumVectoredPorts.setStatus("current")
_AdGenVectorGroupStatusNumUntrainedPorts_Type = Integer32
_AdGenVectorGroupStatusNumUntrainedPorts_Object = MibTableColumn
adGenVectorGroupStatusNumUntrainedPorts = _AdGenVectorGroupStatusNumUntrainedPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1, 4),
    _AdGenVectorGroupStatusNumUntrainedPorts_Type()
)
adGenVectorGroupStatusNumUntrainedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorGroupStatusNumUntrainedPorts.setStatus("deprecated")
_AdGenVectorGroupStatusNumVectorFriendlyPorts_Type = Integer32
_AdGenVectorGroupStatusNumVectorFriendlyPorts_Object = MibTableColumn
adGenVectorGroupStatusNumVectorFriendlyPorts = _AdGenVectorGroupStatusNumVectorFriendlyPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1, 5),
    _AdGenVectorGroupStatusNumVectorFriendlyPorts_Type()
)
adGenVectorGroupStatusNumVectorFriendlyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorGroupStatusNumVectorFriendlyPorts.setStatus("current")
_AdGenVectorGroupStatusNumNonVectoredPorts_Type = Integer32
_AdGenVectorGroupStatusNumNonVectoredPorts_Object = MibTableColumn
adGenVectorGroupStatusNumNonVectoredPorts = _AdGenVectorGroupStatusNumNonVectoredPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1, 6),
    _AdGenVectorGroupStatusNumNonVectoredPorts_Type()
)
adGenVectorGroupStatusNumNonVectoredPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorGroupStatusNumNonVectoredPorts.setStatus("current")
_AdGenVectorGroupStatusNumLegacyPorts_Type = Integer32
_AdGenVectorGroupStatusNumLegacyPorts_Object = MibTableColumn
adGenVectorGroupStatusNumLegacyPorts = _AdGenVectorGroupStatusNumLegacyPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1, 7),
    _AdGenVectorGroupStatusNumLegacyPorts_Type()
)
adGenVectorGroupStatusNumLegacyPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorGroupStatusNumLegacyPorts.setStatus("current")
_AdGenVectorGroupStatusOperStatus_Type = AdGenVectorGroupOperStatus
_AdGenVectorGroupStatusOperStatus_Object = MibTableColumn
adGenVectorGroupStatusOperStatus = _AdGenVectorGroupStatusOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1, 8),
    _AdGenVectorGroupStatusOperStatus_Type()
)
adGenVectorGroupStatusOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorGroupStatusOperStatus.setStatus("current")


class _AdGenVectorGroupStatusReset_Type(Integer32):
    """Custom type adGenVectorGroupStatusReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenVectorGroupStatusReset_Type.__name__ = "Integer32"
_AdGenVectorGroupStatusReset_Object = MibTableColumn
adGenVectorGroupStatusReset = _AdGenVectorGroupStatusReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1, 9),
    _AdGenVectorGroupStatusReset_Type()
)
adGenVectorGroupStatusReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVectorGroupStatusReset.setStatus("current")
_AdGenVectorGroupStatusNumFallbackPorts_Type = Integer32
_AdGenVectorGroupStatusNumFallbackPorts_Object = MibTableColumn
adGenVectorGroupStatusNumFallbackPorts = _AdGenVectorGroupStatusNumFallbackPorts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 6, 1, 10),
    _AdGenVectorGroupStatusNumFallbackPorts_Type()
)
adGenVectorGroupStatusNumFallbackPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorGroupStatusNumFallbackPorts.setStatus("current")
_AdGenVectorPhyStatusTable_Object = MibTable
adGenVectorPhyStatusTable = _AdGenVectorPhyStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 7)
)
if mibBuilder.loadTexts:
    adGenVectorPhyStatusTable.setStatus("current")
_AdGenVectorPhyStatusEntry_Object = MibTableRow
adGenVectorPhyStatusEntry = _AdGenVectorPhyStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 7, 1)
)
adGenVectorPhyStatusEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-VECTORING-MIB", "adGenVectorPhyStatusPhyIfIndex"),
)
if mibBuilder.loadTexts:
    adGenVectorPhyStatusEntry.setStatus("current")
_AdGenVectorPhyStatusPhyIfIndex_Type = InterfaceIndex
_AdGenVectorPhyStatusPhyIfIndex_Object = MibTableColumn
adGenVectorPhyStatusPhyIfIndex = _AdGenVectorPhyStatusPhyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 7, 1, 1),
    _AdGenVectorPhyStatusPhyIfIndex_Type()
)
adGenVectorPhyStatusPhyIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVectorPhyStatusPhyIfIndex.setStatus("current")
_AdGenVectorPhyStatusGroupIfIndex_Type = InterfaceIndex
_AdGenVectorPhyStatusGroupIfIndex_Object = MibTableColumn
adGenVectorPhyStatusGroupIfIndex = _AdGenVectorPhyStatusGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 7, 1, 2),
    _AdGenVectorPhyStatusGroupIfIndex_Type()
)
adGenVectorPhyStatusGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorPhyStatusGroupIfIndex.setStatus("current")
_AdGenVectorPhyStatusGroupType_Type = AdGenVectorMode
_AdGenVectorPhyStatusGroupType_Object = MibTableColumn
adGenVectorPhyStatusGroupType = _AdGenVectorPhyStatusGroupType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 7, 1, 3),
    _AdGenVectorPhyStatusGroupType_Type()
)
adGenVectorPhyStatusGroupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorPhyStatusGroupType.setStatus("current")
_AdGenVectorPhyStatusPortLineState_Type = AdGenVectorPhyLineState
_AdGenVectorPhyStatusPortLineState_Object = MibTableColumn
adGenVectorPhyStatusPortLineState = _AdGenVectorPhyStatusPortLineState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 7, 1, 4),
    _AdGenVectorPhyStatusPortLineState_Type()
)
adGenVectorPhyStatusPortLineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorPhyStatusPortLineState.setStatus("deprecated")
_AdGenVectorPhyStatusPortVectoringState_Type = AdGenVectorPhyPortVectoringState
_AdGenVectorPhyStatusPortVectoringState_Object = MibTableColumn
adGenVectorPhyStatusPortVectoringState = _AdGenVectorPhyStatusPortVectoringState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 7, 1, 5),
    _AdGenVectorPhyStatusPortVectoringState_Type()
)
adGenVectorPhyStatusPortVectoringState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorPhyStatusPortVectoringState.setStatus("current")
_AdGenVectorPhyStatusVectoringError_Type = DisplayString
_AdGenVectorPhyStatusVectoringError_Object = MibTableColumn
adGenVectorPhyStatusVectoringError = _AdGenVectorPhyStatusVectoringError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 7, 1, 6),
    _AdGenVectorPhyStatusVectoringError_Type()
)
adGenVectorPhyStatusVectoringError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorPhyStatusVectoringError.setStatus("current")
_AdGenVectorPhyStatusVectoringErrorTimestamp_Type = AdGenVectorPhyPortErrorTimestamp
_AdGenVectorPhyStatusVectoringErrorTimestamp_Object = MibTableColumn
adGenVectorPhyStatusVectoringErrorTimestamp = _AdGenVectorPhyStatusVectoringErrorTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 7, 1, 7),
    _AdGenVectorPhyStatusVectoringErrorTimestamp_Type()
)
adGenVectorPhyStatusVectoringErrorTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorPhyStatusVectoringErrorTimestamp.setStatus("current")
if mibBuilder.loadTexts:
    adGenVectorPhyStatusVectoringErrorTimestamp.setUnits("seconds")
_AdGenVectorPhyStatusVectoringErrorDateTime_Type = DisplayString
_AdGenVectorPhyStatusVectoringErrorDateTime_Object = MibTableColumn
adGenVectorPhyStatusVectoringErrorDateTime = _AdGenVectorPhyStatusVectoringErrorDateTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 7, 1, 8),
    _AdGenVectorPhyStatusVectoringErrorDateTime_Type()
)
adGenVectorPhyStatusVectoringErrorDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorPhyStatusVectoringErrorDateTime.setStatus("current")
_AdGenVectorAlarmsPrefix_ObjectIdentity = ObjectIdentity
adGenVectorAlarmsPrefix = _AdGenVectorAlarmsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 8)
)
_AdGenVectorAlarms_ObjectIdentity = ObjectIdentity
adGenVectorAlarms = _AdGenVectorAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 8, 0)
)
_AdGenVectorSlotConfTable_Object = MibTable
adGenVectorSlotConfTable = _AdGenVectorSlotConfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 9)
)
if mibBuilder.loadTexts:
    adGenVectorSlotConfTable.setStatus("current")
_AdGenVectorSlotConfEntry_Object = MibTableRow
adGenVectorSlotConfEntry = _AdGenVectorSlotConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 9, 1)
)
adGenVectorSlotConfEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenVectorSlotConfEntry.setStatus("current")


class _AdGenVectorSlotConfForceFallback_Type(Integer32):
    """Custom type adGenVectorSlotConfForceFallback based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceSlotFallback", 1),
          ("allowVectoring", 2))
    )


_AdGenVectorSlotConfForceFallback_Type.__name__ = "Integer32"
_AdGenVectorSlotConfForceFallback_Object = MibTableColumn
adGenVectorSlotConfForceFallback = _AdGenVectorSlotConfForceFallback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 9, 1, 1),
    _AdGenVectorSlotConfForceFallback_Type()
)
adGenVectorSlotConfForceFallback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVectorSlotConfForceFallback.setStatus("current")
_AdGenVectorSlotStatusTable_Object = MibTable
adGenVectorSlotStatusTable = _AdGenVectorSlotStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 10)
)
if mibBuilder.loadTexts:
    adGenVectorSlotStatusTable.setStatus("current")
_AdGenVectorSlotStatusEntry_Object = MibTableRow
adGenVectorSlotStatusEntry = _AdGenVectorSlotStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 10, 1)
)
adGenVectorSlotStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenVectorSlotStatusEntry.setStatus("current")


class _AdGenVectorSlotStatusFallbackState_Type(Integer32):
    """Custom type adGenVectorSlotStatusFallbackState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fallbackActive", 1),
          ("fallbackInactive", 2))
    )


_AdGenVectorSlotStatusFallbackState_Type.__name__ = "Integer32"
_AdGenVectorSlotStatusFallbackState_Object = MibTableColumn
adGenVectorSlotStatusFallbackState = _AdGenVectorSlotStatusFallbackState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 10, 1, 1),
    _AdGenVectorSlotStatusFallbackState_Type()
)
adGenVectorSlotStatusFallbackState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorSlotStatusFallbackState.setStatus("current")
_AdGenVectorBulk_ObjectIdentity = ObjectIdentity
adGenVectorBulk = _AdGenVectorBulk_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2)
)
_AdGenVectorBulkInstanceTable_Object = MibTable
adGenVectorBulkInstanceTable = _AdGenVectorBulkInstanceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 1)
)
if mibBuilder.loadTexts:
    adGenVectorBulkInstanceTable.setStatus("current")
_AdGenVectorBulkInstanceEntry_Object = MibTableRow
adGenVectorBulkInstanceEntry = _AdGenVectorBulkInstanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 1, 1)
)
adGenVectorBulkInstanceEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenVectorBulkInstanceEntry.setStatus("current")
_AdGenVectorBulkReserveSlotInstance_Type = Integer32
_AdGenVectorBulkReserveSlotInstance_Object = MibTableColumn
adGenVectorBulkReserveSlotInstance = _AdGenVectorBulkReserveSlotInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 1, 1, 1),
    _AdGenVectorBulkReserveSlotInstance_Type()
)
adGenVectorBulkReserveSlotInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVectorBulkReserveSlotInstance.setStatus("current")
_AdGenVectorBulkFilterTable_Object = MibTable
adGenVectorBulkFilterTable = _AdGenVectorBulkFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 2)
)
if mibBuilder.loadTexts:
    adGenVectorBulkFilterTable.setStatus("current")
_AdGenVectorBulkFilterEntry_Object = MibTableRow
adGenVectorBulkFilterEntry = _AdGenVectorBulkFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 2, 1)
)
adGenVectorBulkFilterEntry.setIndexNames(
    (0, "ADTRAN-GENERIC-VECTORING-MIB", "adGenVectorGroupStatusIfIndex"),
    (0, "ADTRAN-GENERIC-VECTORING-MIB", "adGenVectorBulkFilterInstance"),
)
if mibBuilder.loadTexts:
    adGenVectorBulkFilterEntry.setStatus("current")
_AdGenVectorBulkFilterInstance_Type = Integer32
_AdGenVectorBulkFilterInstance_Object = MibTableColumn
adGenVectorBulkFilterInstance = _AdGenVectorBulkFilterInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 2, 1, 1),
    _AdGenVectorBulkFilterInstance_Type()
)
adGenVectorBulkFilterInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVectorBulkFilterInstance.setStatus("current")
_AdGenVectorBulkFilterInterface_Type = InterfaceIndex
_AdGenVectorBulkFilterInterface_Object = MibTableColumn
adGenVectorBulkFilterInterface = _AdGenVectorBulkFilterInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 2, 1, 2),
    _AdGenVectorBulkFilterInterface_Type()
)
adGenVectorBulkFilterInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVectorBulkFilterInterface.setStatus("current")
_AdGenVectorBulkFilterSlot_Type = Integer32
_AdGenVectorBulkFilterSlot_Object = MibTableColumn
adGenVectorBulkFilterSlot = _AdGenVectorBulkFilterSlot_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 2, 1, 3),
    _AdGenVectorBulkFilterSlot_Type()
)
adGenVectorBulkFilterSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVectorBulkFilterSlot.setStatus("current")


class _AdGenVectorBulkFilterDirection_Type(Integer32):
    """Custom type adGenVectorBulkFilterDirection based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("upstream", 1),
          ("downstream", 2))
    )


_AdGenVectorBulkFilterDirection_Type.__name__ = "Integer32"
_AdGenVectorBulkFilterDirection_Object = MibTableColumn
adGenVectorBulkFilterDirection = _AdGenVectorBulkFilterDirection_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 2, 1, 4),
    _AdGenVectorBulkFilterDirection_Type()
)
adGenVectorBulkFilterDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVectorBulkFilterDirection.setStatus("current")


class _AdGenVectorBulkFilterType_Type(Integer32):
    """Custom type adGenVectorBulkFilterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("weights", 1)
    )


_AdGenVectorBulkFilterType_Type.__name__ = "Integer32"
_AdGenVectorBulkFilterType_Object = MibTableColumn
adGenVectorBulkFilterType = _AdGenVectorBulkFilterType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 2, 1, 5),
    _AdGenVectorBulkFilterType_Type()
)
adGenVectorBulkFilterType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVectorBulkFilterType.setStatus("current")


class _AdGenVectorBulkSlotCreate_Type(Integer32):
    """Custom type adGenVectorBulkSlotCreate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("updateinstance", 1)
    )


_AdGenVectorBulkSlotCreate_Type.__name__ = "Integer32"
_AdGenVectorBulkSlotCreate_Object = MibTableColumn
adGenVectorBulkSlotCreate = _AdGenVectorBulkSlotCreate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 2, 2, 1, 6),
    _AdGenVectorBulkSlotCreate_Type()
)
adGenVectorBulkSlotCreate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVectorBulkSlotCreate.setStatus("current")

# Managed Objects groups


# Notification objects

adGenVectorAlarmsForcedFallbackClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 8, 0, 2)
)
adGenVectorAlarmsForcedFallbackClr.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenVectorAlarmsForcedFallbackClr.setStatus(
        "current"
    )

adGenVectorAlarmsForcedFallbackAct = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 57, 1, 8, 0, 3)
)
adGenVectorAlarmsForcedFallbackAct.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-TAeSCUEXT1-MIB", "adTAeSCUTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenVectorAlarmsForcedFallbackAct.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-VECTORING-MIB",
    **{"AdGenVectorMode": AdGenVectorMode,
       "AdGenVectorGroupOperStatus": AdGenVectorGroupOperStatus,
       "AdGenVectorLastChange": AdGenVectorLastChange,
       "AdGenVectorPhyPortErrorTimestamp": AdGenVectorPhyPortErrorTimestamp,
       "AdGenVectorPhyLineState": AdGenVectorPhyLineState,
       "AdGenVectorPhyPortVectoringState": AdGenVectorPhyPortVectoringState,
       "AdGenVectorGroupBandPlans": AdGenVectorGroupBandPlans,
       "AdGenVectorGroupFallbackModes": AdGenVectorGroupFallbackModes,
       "adGenVectorMIBObjects": adGenVectorMIBObjects,
       "adGenVectorModuleConfTable": adGenVectorModuleConfTable,
       "adGenVectorModuleConfEntry": adGenVectorModuleConfEntry,
       "adGenVectorModuleConfSupportedVectorModeTypes": adGenVectorModuleConfSupportedVectorModeTypes,
       "adGenVectorModuleConfMaxBLVGroups": adGenVectorModuleConfMaxBLVGroups,
       "adGenVectorModuleConfMaxSLVGroups": adGenVectorModuleConfMaxSLVGroups,
       "adGenVectorModuleConfMaxPhysPerSLVGroup": adGenVectorModuleConfMaxPhysPerSLVGroup,
       "adGenVectorModuleConfNumPhys": adGenVectorModuleConfNumPhys,
       "adGenVectorModuleConfVectorEngineHwRev": adGenVectorModuleConfVectorEngineHwRev,
       "adGenVectorModuleConfVectorEngineSwRev": adGenVectorModuleConfVectorEngineSwRev,
       "adGenVectorGroupTableLastError": adGenVectorGroupTableLastError,
       "adGenVectorGroupTable": adGenVectorGroupTable,
       "adGenVectorGroupEntry": adGenVectorGroupEntry,
       "adGenVectorGroupIfIndex": adGenVectorGroupIfIndex,
       "adGenVectorGroupDescription": adGenVectorGroupDescription,
       "adGenVectorGroupLastError": adGenVectorGroupLastError,
       "adGenVectorGroupBandPlan": adGenVectorGroupBandPlan,
       "adGenVectorGroupRowStatus": adGenVectorGroupRowStatus,
       "adGenVectorGroupFallbackMode": adGenVectorGroupFallbackMode,
       "adGenVectorGroupFallbackAlarmSeverity": adGenVectorGroupFallbackAlarmSeverity,
       "adGenVectorGroupFallbackAlarmEnable": adGenVectorGroupFallbackAlarmEnable,
       "adGenVectorGroupVectoringMode": adGenVectorGroupVectoringMode,
       "adGenVectorGroupAutoAddEnable": adGenVectorGroupAutoAddEnable,
       "adGenVectorPhyMapTableLastError": adGenVectorPhyMapTableLastError,
       "adGenVectorPhyMapTable": adGenVectorPhyMapTable,
       "adGenVectorPhyMapEntry": adGenVectorPhyMapEntry,
       "adGenVectorPhyMapGroupIfIndex": adGenVectorPhyMapGroupIfIndex,
       "adGenVectorPhyMapPhyIfIndex": adGenVectorPhyMapPhyIfIndex,
       "adGenVectorPhyMapLastChange": adGenVectorPhyMapLastChange,
       "adGenVectorPhyMapLastError": adGenVectorPhyMapLastError,
       "adGenVectorPhyMapRowStatus": adGenVectorPhyMapRowStatus,
       "adGenVectorGroupStatusTable": adGenVectorGroupStatusTable,
       "adGenVectorGroupStatusEntry": adGenVectorGroupStatusEntry,
       "adGenVectorGroupStatusIfIndex": adGenVectorGroupStatusIfIndex,
       "adGenVectorGroupStatusNumProvisionedPorts": adGenVectorGroupStatusNumProvisionedPorts,
       "adGenVectorGroupStatusNumVectoredPorts": adGenVectorGroupStatusNumVectoredPorts,
       "adGenVectorGroupStatusNumUntrainedPorts": adGenVectorGroupStatusNumUntrainedPorts,
       "adGenVectorGroupStatusNumVectorFriendlyPorts": adGenVectorGroupStatusNumVectorFriendlyPorts,
       "adGenVectorGroupStatusNumNonVectoredPorts": adGenVectorGroupStatusNumNonVectoredPorts,
       "adGenVectorGroupStatusNumLegacyPorts": adGenVectorGroupStatusNumLegacyPorts,
       "adGenVectorGroupStatusOperStatus": adGenVectorGroupStatusOperStatus,
       "adGenVectorGroupStatusReset": adGenVectorGroupStatusReset,
       "adGenVectorGroupStatusNumFallbackPorts": adGenVectorGroupStatusNumFallbackPorts,
       "adGenVectorPhyStatusTable": adGenVectorPhyStatusTable,
       "adGenVectorPhyStatusEntry": adGenVectorPhyStatusEntry,
       "adGenVectorPhyStatusPhyIfIndex": adGenVectorPhyStatusPhyIfIndex,
       "adGenVectorPhyStatusGroupIfIndex": adGenVectorPhyStatusGroupIfIndex,
       "adGenVectorPhyStatusGroupType": adGenVectorPhyStatusGroupType,
       "adGenVectorPhyStatusPortLineState": adGenVectorPhyStatusPortLineState,
       "adGenVectorPhyStatusPortVectoringState": adGenVectorPhyStatusPortVectoringState,
       "adGenVectorPhyStatusVectoringError": adGenVectorPhyStatusVectoringError,
       "adGenVectorPhyStatusVectoringErrorTimestamp": adGenVectorPhyStatusVectoringErrorTimestamp,
       "adGenVectorPhyStatusVectoringErrorDateTime": adGenVectorPhyStatusVectoringErrorDateTime,
       "adGenVectorAlarmsPrefix": adGenVectorAlarmsPrefix,
       "adGenVectorAlarms": adGenVectorAlarms,
       "adGenVectorAlarmsForcedFallbackClr": adGenVectorAlarmsForcedFallbackClr,
       "adGenVectorAlarmsForcedFallbackAct": adGenVectorAlarmsForcedFallbackAct,
       "adGenVectorSlotConfTable": adGenVectorSlotConfTable,
       "adGenVectorSlotConfEntry": adGenVectorSlotConfEntry,
       "adGenVectorSlotConfForceFallback": adGenVectorSlotConfForceFallback,
       "adGenVectorSlotStatusTable": adGenVectorSlotStatusTable,
       "adGenVectorSlotStatusEntry": adGenVectorSlotStatusEntry,
       "adGenVectorSlotStatusFallbackState": adGenVectorSlotStatusFallbackState,
       "adGenVectorBulk": adGenVectorBulk,
       "adGenVectorBulkInstanceTable": adGenVectorBulkInstanceTable,
       "adGenVectorBulkInstanceEntry": adGenVectorBulkInstanceEntry,
       "adGenVectorBulkReserveSlotInstance": adGenVectorBulkReserveSlotInstance,
       "adGenVectorBulkFilterTable": adGenVectorBulkFilterTable,
       "adGenVectorBulkFilterEntry": adGenVectorBulkFilterEntry,
       "adGenVectorBulkFilterInstance": adGenVectorBulkFilterInstance,
       "adGenVectorBulkFilterInterface": adGenVectorBulkFilterInterface,
       "adGenVectorBulkFilterSlot": adGenVectorBulkFilterSlot,
       "adGenVectorBulkFilterDirection": adGenVectorBulkFilterDirection,
       "adGenVectorBulkFilterType": adGenVectorBulkFilterType,
       "adGenVectorBulkSlotCreate": adGenVectorBulkSlotCreate,
       "adGenVectorMIB": adGenVectorMIB}
)
