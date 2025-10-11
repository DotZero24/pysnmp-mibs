# SNMP MIB module (OS-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OS-COUNTERS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:04:53 2025
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

(oaOptiSwitch,) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "oaOptiSwitch")

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
 enterprises,
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
    "enterprises",
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

osCounters = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8)
)
if mibBuilder.loadTexts:
    osCounters.setRevisions(
        ("2016-12-27 00:00",
         "2011-04-05 00:00",
         "2010-07-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CntBooleanFlag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(-1,
              0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("other", -1),
          ("no", 0),
          ("yes", 1))
    )



class CntEntryStatusVal(TextualConvention, Integer32):
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
        *(("none", 1),
          ("invalid", 2),
          ("valid", 3),
          ("clear", 4))
    )



class CntEntryStatusExtVal(TextualConvention, Integer32):
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
        *(("none", 1),
          ("invalid", 2),
          ("valid", 3),
          ("delete", 4),
          ("create", 5),
          ("clear", 6))
    )



class CntTableStatusVal(TextualConvention, Integer32):
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
        *(("none", 1),
          ("invalidTbl", 2),
          ("validTbl", 3),
          ("clearAll", 4))
    )



class CntPortIndex(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )



class CntPortIndexOrAll(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )



class CntVlanId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class CntVlanIdOrAll(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )



class CntServiceLevelOrAll(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )



class CntDpLevelOrAll(TextualConvention, Integer32):
    status = "current"
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
        *(("all", 0),
          ("green", 1),
          ("yellow", 2),
          ("red", 3))
    )



class CntDirection(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ingress", 1),
          ("egress", 2))
    )



class CntMatchingId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2048),
    )



# MIB Managed Objects in the order of their OIDs

_OsCountersCapabilities_ObjectIdentity = ObjectIdentity
osCountersCapabilities = _OsCountersCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1)
)


class _OsCountersFeaturesSupport_Type(Bits):
    """Custom type osCountersFeaturesSupport based on Bits"""
    namedValues = NamedValues(
        *(("portIngressCounters", 0),
          ("portEgressCounters", 1),
          ("vifIngressCounters", 2),
          ("vifEgressCounters", 3),
          ("ingressSetCounters", 4),
          ("egressSetCounters", 5),
          ("ingressMatchingCounters", 6),
          ("egressMatchingCounters", 7),
          ("tunnelCounters", 8))
    )

_OsCountersFeaturesSupport_Type.__name__ = "Bits"
_OsCountersFeaturesSupport_Object = MibScalar
osCountersFeaturesSupport = _OsCountersFeaturesSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 1),
    _OsCountersFeaturesSupport_Type()
)
osCountersFeaturesSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCountersFeaturesSupport.setStatus("current")
_OsCntPrtEgrTblStatus_Type = CntTableStatusVal
_OsCntPrtEgrTblStatus_Object = MibScalar
osCntPrtEgrTblStatus = _OsCntPrtEgrTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 2),
    _OsCntPrtEgrTblStatus_Type()
)
osCntPrtEgrTblStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntPrtEgrTblStatus.setStatus("current")


class _OsCntPrtEgrCaps_Type(Bits):
    """Custom type osCntPrtEgrCaps based on Bits"""
    namedValues = NamedValues(
        *(("hasPassGrnOcts", 0),
          ("hasPassGrnPkts", 1),
          ("hasPassYelOcts", 2),
          ("hasPassYelPkts", 3),
          ("hasPassRedOcts", 4),
          ("hasPassRedPkts", 5),
          ("hasDropGrnOcts", 6),
          ("hasDropGrnPkts", 7),
          ("hasDropYelOcts", 8),
          ("hasDropYelPkts", 9),
          ("hasDropRedOcts", 10),
          ("hasDropRedPkts", 11))
    )

_OsCntPrtEgrCaps_Type.__name__ = "Bits"
_OsCntPrtEgrCaps_Object = MibScalar
osCntPrtEgrCaps = _OsCntPrtEgrCaps_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 3),
    _OsCntPrtEgrCaps_Type()
)
osCntPrtEgrCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrCaps.setStatus("current")
_OsCntVifDirTable_Object = MibTable
osCntVifDirTable = _OsCntVifDirTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 4)
)
if mibBuilder.loadTexts:
    osCntVifDirTable.setStatus("current")
_OsCntVifDirEntry_Object = MibTableRow
osCntVifDirEntry = _OsCntVifDirEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 4, 1)
)
osCntVifDirEntry.setIndexNames(
    (0, "OS-COUNTERS-MIB", "osCntVifDirection"),
)
if mibBuilder.loadTexts:
    osCntVifDirEntry.setStatus("current")
_OsCntVifDirection_Type = CntDirection
_OsCntVifDirection_Object = MibTableColumn
osCntVifDirection = _OsCntVifDirection_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 4, 1, 1),
    _OsCntVifDirection_Type()
)
osCntVifDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntVifDirection.setStatus("current")
_OsCntVifDirTblStatus_Type = CntTableStatusVal
_OsCntVifDirTblStatus_Object = MibTableColumn
osCntVifDirTblStatus = _OsCntVifDirTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 4, 1, 2),
    _OsCntVifDirTblStatus_Type()
)
osCntVifDirTblStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntVifDirTblStatus.setStatus("current")


class _OsCntVifCaps_Type(Bits):
    """Custom type osCntVifCaps based on Bits"""
    namedValues = NamedValues(
        *(("hasIngPassOcts", 0),
          ("hasIngPassPkts", 1),
          ("hasEgrPassOcts", 2),
          ("hasEgrPassPkts", 3))
    )

_OsCntVifCaps_Type.__name__ = "Bits"
_OsCntVifCaps_Object = MibScalar
osCntVifCaps = _OsCntVifCaps_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 5),
    _OsCntVifCaps_Type()
)
osCntVifCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntVifCaps.setStatus("current")
_OsCntIngSuiteTblStatus_Type = CntTableStatusVal
_OsCntIngSuiteTblStatus_Object = MibScalar
osCntIngSuiteTblStatus = _OsCntIngSuiteTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 6),
    _OsCntIngSuiteTblStatus_Type()
)
osCntIngSuiteTblStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntIngSuiteTblStatus.setStatus("current")


class _OsCntIngSuiteCaps_Type(Bits):
    """Custom type osCntIngSuiteCaps based on Bits"""
    namedValues = NamedValues(
        *(("hasPassPkts", 0),
          ("hasVlanDropPkts", 1),
          ("hasSecDropPkts", 2),
          ("hasOtherDropPkts", 3),
          ("hasServiceLevel", 4))
    )

_OsCntIngSuiteCaps_Type.__name__ = "Bits"
_OsCntIngSuiteCaps_Object = MibScalar
osCntIngSuiteCaps = _OsCntIngSuiteCaps_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 7),
    _OsCntIngSuiteCaps_Type()
)
osCntIngSuiteCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntIngSuiteCaps.setStatus("current")
_OsCntEgrSuiteTblStatus_Type = CntTableStatusVal
_OsCntEgrSuiteTblStatus_Object = MibScalar
osCntEgrSuiteTblStatus = _OsCntEgrSuiteTblStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 8),
    _OsCntEgrSuiteTblStatus_Type()
)
osCntEgrSuiteTblStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntEgrSuiteTblStatus.setStatus("current")


class _OsCntEgrSuiteCaps_Type(Bits):
    """Custom type osCntEgrSuiteCaps based on Bits"""
    namedValues = NamedValues(
        *(("hasUcPassPkts", 0),
          ("hasMcPassPkts", 1),
          ("hasBcPassPkts", 2),
          ("hasTxqDropPkts", 3),
          ("hasYellow", 4),
          ("hasSkip", 5),
          ("hasIntPort", 6))
    )

_OsCntEgrSuiteCaps_Type.__name__ = "Bits"
_OsCntEgrSuiteCaps_Object = MibScalar
osCntEgrSuiteCaps = _OsCntEgrSuiteCaps_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 9),
    _OsCntEgrSuiteCaps_Type()
)
osCntEgrSuiteCaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntEgrSuiteCaps.setStatus("current")


class _OsCountersVFeaturesSupport_Type(Bits):
    """Custom type osCountersVFeaturesSupport based on Bits"""
    namedValues = NamedValues(
        *(("hasAclIngress", 0),
          ("hasAclSecondIngress", 1),
          ("hasAclEgress", 2),
          ("hasVlanPassIngress", 3),
          ("hasVlanDropIngress", 4),
          ("hasVlanPassEgress", 5),
          ("hasVlanDropEgress", 6),
          ("hasPortEgress", 7),
          ("hasReserved1VBit", 8),
          ("hasReserved2VBit", 9),
          ("hasTrafficManager", 10))
    )

_OsCountersVFeaturesSupport_Type.__name__ = "Bits"
_OsCountersVFeaturesSupport_Object = MibScalar
osCountersVFeaturesSupport = _OsCountersVFeaturesSupport_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 1, 10),
    _OsCountersVFeaturesSupport_Type()
)
osCountersVFeaturesSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCountersVFeaturesSupport.setStatus("current")
_OsCntPrtEgrTable_Object = MibTable
osCntPrtEgrTable = _OsCntPrtEgrTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2)
)
if mibBuilder.loadTexts:
    osCntPrtEgrTable.setStatus("current")
_OsCntPrtEgrEntry_Object = MibTableRow
osCntPrtEgrEntry = _OsCntPrtEgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1)
)
osCntPrtEgrEntry.setIndexNames(
    (0, "OS-COUNTERS-MIB", "osCntPrtEgrPortIndex"),
    (0, "OS-COUNTERS-MIB", "osCntPrtEgrServiceLevel"),
)
if mibBuilder.loadTexts:
    osCntPrtEgrEntry.setStatus("current")
_OsCntPrtEgrPortIndex_Type = CntPortIndex
_OsCntPrtEgrPortIndex_Object = MibTableColumn
osCntPrtEgrPortIndex = _OsCntPrtEgrPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 1),
    _OsCntPrtEgrPortIndex_Type()
)
osCntPrtEgrPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntPrtEgrPortIndex.setStatus("current")
_OsCntPrtEgrServiceLevel_Type = CntServiceLevelOrAll
_OsCntPrtEgrServiceLevel_Object = MibTableColumn
osCntPrtEgrServiceLevel = _OsCntPrtEgrServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 2),
    _OsCntPrtEgrServiceLevel_Type()
)
osCntPrtEgrServiceLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntPrtEgrServiceLevel.setStatus("current")
_OsCntPrtEgrEntryStatus_Type = CntEntryStatusVal
_OsCntPrtEgrEntryStatus_Object = MibTableColumn
osCntPrtEgrEntryStatus = _OsCntPrtEgrEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 3),
    _OsCntPrtEgrEntryStatus_Type()
)
osCntPrtEgrEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntPrtEgrEntryStatus.setStatus("current")
_OsCntPrtEgrPassGrnOcts_Type = Counter64
_OsCntPrtEgrPassGrnOcts_Object = MibTableColumn
osCntPrtEgrPassGrnOcts = _OsCntPrtEgrPassGrnOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 4),
    _OsCntPrtEgrPassGrnOcts_Type()
)
osCntPrtEgrPassGrnOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrPassGrnOcts.setStatus("current")
_OsCntPrtEgrPassGrnPkts_Type = Counter64
_OsCntPrtEgrPassGrnPkts_Object = MibTableColumn
osCntPrtEgrPassGrnPkts = _OsCntPrtEgrPassGrnPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 5),
    _OsCntPrtEgrPassGrnPkts_Type()
)
osCntPrtEgrPassGrnPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrPassGrnPkts.setStatus("current")
_OsCntPrtEgrPassYlwOcts_Type = Counter64
_OsCntPrtEgrPassYlwOcts_Object = MibTableColumn
osCntPrtEgrPassYlwOcts = _OsCntPrtEgrPassYlwOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 6),
    _OsCntPrtEgrPassYlwOcts_Type()
)
osCntPrtEgrPassYlwOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrPassYlwOcts.setStatus("current")
_OsCntPrtEgrPassYlwPkts_Type = Counter64
_OsCntPrtEgrPassYlwPkts_Object = MibTableColumn
osCntPrtEgrPassYlwPkts = _OsCntPrtEgrPassYlwPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 7),
    _OsCntPrtEgrPassYlwPkts_Type()
)
osCntPrtEgrPassYlwPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrPassYlwPkts.setStatus("current")
_OsCntPrtEgrPassRedOcts_Type = Counter64
_OsCntPrtEgrPassRedOcts_Object = MibTableColumn
osCntPrtEgrPassRedOcts = _OsCntPrtEgrPassRedOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 8),
    _OsCntPrtEgrPassRedOcts_Type()
)
osCntPrtEgrPassRedOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrPassRedOcts.setStatus("current")
_OsCntPrtEgrPassRedPkts_Type = Counter64
_OsCntPrtEgrPassRedPkts_Object = MibTableColumn
osCntPrtEgrPassRedPkts = _OsCntPrtEgrPassRedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 9),
    _OsCntPrtEgrPassRedPkts_Type()
)
osCntPrtEgrPassRedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrPassRedPkts.setStatus("current")
_OsCntPrtEgrPassOcts_Type = Counter64
_OsCntPrtEgrPassOcts_Object = MibTableColumn
osCntPrtEgrPassOcts = _OsCntPrtEgrPassOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 10),
    _OsCntPrtEgrPassOcts_Type()
)
osCntPrtEgrPassOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrPassOcts.setStatus("current")
_OsCntPrtEgrPassPkts_Type = Counter64
_OsCntPrtEgrPassPkts_Object = MibTableColumn
osCntPrtEgrPassPkts = _OsCntPrtEgrPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 11),
    _OsCntPrtEgrPassPkts_Type()
)
osCntPrtEgrPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrPassPkts.setStatus("current")
_OsCntPrtEgrDropGrnOcts_Type = Counter64
_OsCntPrtEgrDropGrnOcts_Object = MibTableColumn
osCntPrtEgrDropGrnOcts = _OsCntPrtEgrDropGrnOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 12),
    _OsCntPrtEgrDropGrnOcts_Type()
)
osCntPrtEgrDropGrnOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrDropGrnOcts.setStatus("current")
_OsCntPrtEgrDropGrnPkts_Type = Counter64
_OsCntPrtEgrDropGrnPkts_Object = MibTableColumn
osCntPrtEgrDropGrnPkts = _OsCntPrtEgrDropGrnPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 13),
    _OsCntPrtEgrDropGrnPkts_Type()
)
osCntPrtEgrDropGrnPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrDropGrnPkts.setStatus("current")
_OsCntPrtEgrDropYlwOcts_Type = Counter64
_OsCntPrtEgrDropYlwOcts_Object = MibTableColumn
osCntPrtEgrDropYlwOcts = _OsCntPrtEgrDropYlwOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 14),
    _OsCntPrtEgrDropYlwOcts_Type()
)
osCntPrtEgrDropYlwOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrDropYlwOcts.setStatus("current")
_OsCntPrtEgrDropYlwPkts_Type = Counter64
_OsCntPrtEgrDropYlwPkts_Object = MibTableColumn
osCntPrtEgrDropYlwPkts = _OsCntPrtEgrDropYlwPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 15),
    _OsCntPrtEgrDropYlwPkts_Type()
)
osCntPrtEgrDropYlwPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrDropYlwPkts.setStatus("current")
_OsCntPrtEgrDropRedOcts_Type = Counter64
_OsCntPrtEgrDropRedOcts_Object = MibTableColumn
osCntPrtEgrDropRedOcts = _OsCntPrtEgrDropRedOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 16),
    _OsCntPrtEgrDropRedOcts_Type()
)
osCntPrtEgrDropRedOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrDropRedOcts.setStatus("current")
_OsCntPrtEgrDropRedPkts_Type = Counter64
_OsCntPrtEgrDropRedPkts_Object = MibTableColumn
osCntPrtEgrDropRedPkts = _OsCntPrtEgrDropRedPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 17),
    _OsCntPrtEgrDropRedPkts_Type()
)
osCntPrtEgrDropRedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrDropRedPkts.setStatus("current")
_OsCntPrtEgrDropOcts_Type = Counter64
_OsCntPrtEgrDropOcts_Object = MibTableColumn
osCntPrtEgrDropOcts = _OsCntPrtEgrDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 18),
    _OsCntPrtEgrDropOcts_Type()
)
osCntPrtEgrDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrDropOcts.setStatus("current")
_OsCntPrtEgrDropPkts_Type = Counter64
_OsCntPrtEgrDropPkts_Object = MibTableColumn
osCntPrtEgrDropPkts = _OsCntPrtEgrDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 2, 1, 19),
    _OsCntPrtEgrDropPkts_Type()
)
osCntPrtEgrDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntPrtEgrDropPkts.setStatus("current")
_OsCntVifTable_Object = MibTable
osCntVifTable = _OsCntVifTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 3)
)
if mibBuilder.loadTexts:
    osCntVifTable.setStatus("current")
_OsCntVifEntry_Object = MibTableRow
osCntVifEntry = _OsCntVifEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 3, 1)
)
osCntVifEntry.setIndexNames(
    (0, "OS-COUNTERS-MIB", "osCntVifDirection"),
    (0, "OS-COUNTERS-MIB", "osCntVifIndex"),
    (0, "OS-COUNTERS-MIB", "osCntVifServiceLevel"),
)
if mibBuilder.loadTexts:
    osCntVifEntry.setStatus("current")
_OsCntVifIndex_Type = CntVlanId
_OsCntVifIndex_Object = MibTableColumn
osCntVifIndex = _OsCntVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 3, 1, 1),
    _OsCntVifIndex_Type()
)
osCntVifIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntVifIndex.setStatus("current")
_OsCntVifServiceLevel_Type = CntServiceLevelOrAll
_OsCntVifServiceLevel_Object = MibTableColumn
osCntVifServiceLevel = _OsCntVifServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 3, 1, 2),
    _OsCntVifServiceLevel_Type()
)
osCntVifServiceLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntVifServiceLevel.setStatus("current")
_OsCntVifEntryStatus_Type = CntEntryStatusVal
_OsCntVifEntryStatus_Object = MibTableColumn
osCntVifEntryStatus = _OsCntVifEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 3, 1, 3),
    _OsCntVifEntryStatus_Type()
)
osCntVifEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntVifEntryStatus.setStatus("current")
_OsCntVifPassOcts_Type = Counter64
_OsCntVifPassOcts_Object = MibTableColumn
osCntVifPassOcts = _OsCntVifPassOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 3, 1, 4),
    _OsCntVifPassOcts_Type()
)
osCntVifPassOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntVifPassOcts.setStatus("current")
_OsCntVifPassPkts_Type = Counter64
_OsCntVifPassPkts_Object = MibTableColumn
osCntVifPassPkts = _OsCntVifPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 3, 1, 5),
    _OsCntVifPassPkts_Type()
)
osCntVifPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntVifPassPkts.setStatus("current")
_OsCntVifDropOcts_Type = Counter64
_OsCntVifDropOcts_Object = MibTableColumn
osCntVifDropOcts = _OsCntVifDropOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 3, 1, 6),
    _OsCntVifDropOcts_Type()
)
osCntVifDropOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntVifDropOcts.setStatus("current")
_OsCntVifDropPkts_Type = Counter64
_OsCntVifDropPkts_Object = MibTableColumn
osCntVifDropPkts = _OsCntVifDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 3, 1, 7),
    _OsCntVifDropPkts_Type()
)
osCntVifDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntVifDropPkts.setStatus("current")
_OsCntIngSuiteTable_Object = MibTable
osCntIngSuiteTable = _OsCntIngSuiteTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4)
)
if mibBuilder.loadTexts:
    osCntIngSuiteTable.setStatus("current")
_OsCntIngSuiteEntry_Object = MibTableRow
osCntIngSuiteEntry = _OsCntIngSuiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4, 1)
)
osCntIngSuiteEntry.setIndexNames(
    (0, "OS-COUNTERS-MIB", "osCntIngSuiteIndex"),
)
if mibBuilder.loadTexts:
    osCntIngSuiteEntry.setStatus("current")
_OsCntIngSuiteIndex_Type = Unsigned32
_OsCntIngSuiteIndex_Object = MibTableColumn
osCntIngSuiteIndex = _OsCntIngSuiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4, 1, 1),
    _OsCntIngSuiteIndex_Type()
)
osCntIngSuiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntIngSuiteIndex.setStatus("current")
_OsCntIngSuitePortIndex_Type = CntPortIndexOrAll
_OsCntIngSuitePortIndex_Object = MibTableColumn
osCntIngSuitePortIndex = _OsCntIngSuitePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4, 1, 2),
    _OsCntIngSuitePortIndex_Type()
)
osCntIngSuitePortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntIngSuitePortIndex.setStatus("current")
_OsCntIngSuiteVifIndex_Type = CntVlanIdOrAll
_OsCntIngSuiteVifIndex_Object = MibTableColumn
osCntIngSuiteVifIndex = _OsCntIngSuiteVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4, 1, 3),
    _OsCntIngSuiteVifIndex_Type()
)
osCntIngSuiteVifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntIngSuiteVifIndex.setStatus("current")
_OsCntIngSuiteServiceLevel_Type = CntServiceLevelOrAll
_OsCntIngSuiteServiceLevel_Object = MibTableColumn
osCntIngSuiteServiceLevel = _OsCntIngSuiteServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4, 1, 4),
    _OsCntIngSuiteServiceLevel_Type()
)
osCntIngSuiteServiceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntIngSuiteServiceLevel.setStatus("current")
_OsCntIngSuiteEntryStatus_Type = CntEntryStatusExtVal
_OsCntIngSuiteEntryStatus_Object = MibTableColumn
osCntIngSuiteEntryStatus = _OsCntIngSuiteEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4, 1, 5),
    _OsCntIngSuiteEntryStatus_Type()
)
osCntIngSuiteEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntIngSuiteEntryStatus.setStatus("current")
_OsCntIngSuitePassPkts_Type = Counter64
_OsCntIngSuitePassPkts_Object = MibTableColumn
osCntIngSuitePassPkts = _OsCntIngSuitePassPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4, 1, 6),
    _OsCntIngSuitePassPkts_Type()
)
osCntIngSuitePassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntIngSuitePassPkts.setStatus("current")
_OsCntIngSuiteVlanDropPkts_Type = Counter64
_OsCntIngSuiteVlanDropPkts_Object = MibTableColumn
osCntIngSuiteVlanDropPkts = _OsCntIngSuiteVlanDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4, 1, 7),
    _OsCntIngSuiteVlanDropPkts_Type()
)
osCntIngSuiteVlanDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntIngSuiteVlanDropPkts.setStatus("current")
_OsCntIngSuiteSecDropPkts_Type = Counter64
_OsCntIngSuiteSecDropPkts_Object = MibTableColumn
osCntIngSuiteSecDropPkts = _OsCntIngSuiteSecDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4, 1, 8),
    _OsCntIngSuiteSecDropPkts_Type()
)
osCntIngSuiteSecDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntIngSuiteSecDropPkts.setStatus("current")
_OsCntIngSuiteOtherDropPkts_Type = Counter64
_OsCntIngSuiteOtherDropPkts_Object = MibTableColumn
osCntIngSuiteOtherDropPkts = _OsCntIngSuiteOtherDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 4, 1, 9),
    _OsCntIngSuiteOtherDropPkts_Type()
)
osCntIngSuiteOtherDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntIngSuiteOtherDropPkts.setStatus("current")
_OsCntEgrSuiteTable_Object = MibTable
osCntEgrSuiteTable = _OsCntEgrSuiteTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5)
)
if mibBuilder.loadTexts:
    osCntEgrSuiteTable.setStatus("current")
_OsCntEgrSuiteEntry_Object = MibTableRow
osCntEgrSuiteEntry = _OsCntEgrSuiteEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1)
)
osCntEgrSuiteEntry.setIndexNames(
    (0, "OS-COUNTERS-MIB", "osCntEgrSuiteIndex"),
)
if mibBuilder.loadTexts:
    osCntEgrSuiteEntry.setStatus("current")
_OsCntEgrSuiteIndex_Type = Unsigned32
_OsCntEgrSuiteIndex_Object = MibTableColumn
osCntEgrSuiteIndex = _OsCntEgrSuiteIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 1),
    _OsCntEgrSuiteIndex_Type()
)
osCntEgrSuiteIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntEgrSuiteIndex.setStatus("current")
_OsCntEgrSuitePortIndex_Type = CntPortIndexOrAll
_OsCntEgrSuitePortIndex_Object = MibTableColumn
osCntEgrSuitePortIndex = _OsCntEgrSuitePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 2),
    _OsCntEgrSuitePortIndex_Type()
)
osCntEgrSuitePortIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntEgrSuitePortIndex.setStatus("current")
_OsCntEgrSuiteVifIndex_Type = CntVlanIdOrAll
_OsCntEgrSuiteVifIndex_Object = MibTableColumn
osCntEgrSuiteVifIndex = _OsCntEgrSuiteVifIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 3),
    _OsCntEgrSuiteVifIndex_Type()
)
osCntEgrSuiteVifIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntEgrSuiteVifIndex.setStatus("current")
_OsCntEgrSuiteServiceLevel_Type = CntServiceLevelOrAll
_OsCntEgrSuiteServiceLevel_Object = MibTableColumn
osCntEgrSuiteServiceLevel = _OsCntEgrSuiteServiceLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 4),
    _OsCntEgrSuiteServiceLevel_Type()
)
osCntEgrSuiteServiceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntEgrSuiteServiceLevel.setStatus("current")
_OsCntEgrSuiteDpLevel_Type = CntDpLevelOrAll
_OsCntEgrSuiteDpLevel_Object = MibTableColumn
osCntEgrSuiteDpLevel = _OsCntEgrSuiteDpLevel_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 5),
    _OsCntEgrSuiteDpLevel_Type()
)
osCntEgrSuiteDpLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntEgrSuiteDpLevel.setStatus("current")
_OsCntEgrSuiteIsSkip_Type = CntBooleanFlag
_OsCntEgrSuiteIsSkip_Object = MibTableColumn
osCntEgrSuiteIsSkip = _OsCntEgrSuiteIsSkip_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 6),
    _OsCntEgrSuiteIsSkip_Type()
)
osCntEgrSuiteIsSkip.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntEgrSuiteIsSkip.setStatus("current")
_OsCntEgrSuiteIsIntPort_Type = CntBooleanFlag
_OsCntEgrSuiteIsIntPort_Object = MibTableColumn
osCntEgrSuiteIsIntPort = _OsCntEgrSuiteIsIntPort_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 7),
    _OsCntEgrSuiteIsIntPort_Type()
)
osCntEgrSuiteIsIntPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntEgrSuiteIsIntPort.setStatus("current")
_OsCntEgrSuiteEntryStatus_Type = CntEntryStatusExtVal
_OsCntEgrSuiteEntryStatus_Object = MibTableColumn
osCntEgrSuiteEntryStatus = _OsCntEgrSuiteEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 8),
    _OsCntEgrSuiteEntryStatus_Type()
)
osCntEgrSuiteEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntEgrSuiteEntryStatus.setStatus("current")
_OsCntEgrSuiteUcPassPkts_Type = Counter64
_OsCntEgrSuiteUcPassPkts_Object = MibTableColumn
osCntEgrSuiteUcPassPkts = _OsCntEgrSuiteUcPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 9),
    _OsCntEgrSuiteUcPassPkts_Type()
)
osCntEgrSuiteUcPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntEgrSuiteUcPassPkts.setStatus("current")
_OsCntEgrSuiteMcPassPkts_Type = Counter64
_OsCntEgrSuiteMcPassPkts_Object = MibTableColumn
osCntEgrSuiteMcPassPkts = _OsCntEgrSuiteMcPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 10),
    _OsCntEgrSuiteMcPassPkts_Type()
)
osCntEgrSuiteMcPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntEgrSuiteMcPassPkts.setStatus("current")
_OsCntEgrSuiteBcPassPkts_Type = Counter64
_OsCntEgrSuiteBcPassPkts_Object = MibTableColumn
osCntEgrSuiteBcPassPkts = _OsCntEgrSuiteBcPassPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 11),
    _OsCntEgrSuiteBcPassPkts_Type()
)
osCntEgrSuiteBcPassPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntEgrSuiteBcPassPkts.setStatus("current")
_OsCntEgrSuiteTxqDropPkts_Type = Counter64
_OsCntEgrSuiteTxqDropPkts_Object = MibTableColumn
osCntEgrSuiteTxqDropPkts = _OsCntEgrSuiteTxqDropPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 5, 1, 12),
    _OsCntEgrSuiteTxqDropPkts_Type()
)
osCntEgrSuiteTxqDropPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntEgrSuiteTxqDropPkts.setStatus("current")
_OsCntAclTable_Object = MibTable
osCntAclTable = _OsCntAclTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 6)
)
if mibBuilder.loadTexts:
    osCntAclTable.setStatus("current")
_OsCntAclEntry_Object = MibTableRow
osCntAclEntry = _OsCntAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 6, 1)
)
osCntAclEntry.setIndexNames(
    (0, "OS-COUNTERS-MIB", "osCntAclDirection"),
    (0, "OS-COUNTERS-MIB", "osCntAclMatchingIndex"),
)
if mibBuilder.loadTexts:
    osCntAclEntry.setStatus("current")
_OsCntAclDirection_Type = CntDirection
_OsCntAclDirection_Object = MibTableColumn
osCntAclDirection = _OsCntAclDirection_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 6, 1, 1),
    _OsCntAclDirection_Type()
)
osCntAclDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntAclDirection.setStatus("current")
_OsCntAclMatchingIndex_Type = CntMatchingId
_OsCntAclMatchingIndex_Object = MibTableColumn
osCntAclMatchingIndex = _OsCntAclMatchingIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 6, 1, 2),
    _OsCntAclMatchingIndex_Type()
)
osCntAclMatchingIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntAclMatchingIndex.setStatus("current")
_OsCntAclEntryStatus_Type = CntEntryStatusVal
_OsCntAclEntryStatus_Object = MibTableColumn
osCntAclEntryStatus = _OsCntAclEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 6, 1, 3),
    _OsCntAclEntryStatus_Type()
)
osCntAclEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntAclEntryStatus.setStatus("current")
_OsCntAclMatchOcts_Type = Counter64
_OsCntAclMatchOcts_Object = MibTableColumn
osCntAclMatchOcts = _OsCntAclMatchOcts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 6, 1, 4),
    _OsCntAclMatchOcts_Type()
)
osCntAclMatchOcts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntAclMatchOcts.setStatus("current")
_OsCntAclMatchPkts_Type = Counter64
_OsCntAclMatchPkts_Object = MibTableColumn
osCntAclMatchPkts = _OsCntAclMatchPkts_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 6, 1, 5),
    _OsCntAclMatchPkts_Type()
)
osCntAclMatchPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntAclMatchPkts.setStatus("current")
_OsCntBindTable_Object = MibTable
osCntBindTable = _OsCntBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 10)
)
if mibBuilder.loadTexts:
    osCntBindTable.setStatus("current")
_OsCntBindEntry_Object = MibTableRow
osCntBindEntry = _OsCntBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 10, 1)
)
osCntBindEntry.setIndexNames(
    (0, "OS-COUNTERS-MIB", "osCntBindBlockIndex"),
)
if mibBuilder.loadTexts:
    osCntBindEntry.setStatus("current")
_OsCntBindBlockIndex_Type = Unsigned32
_OsCntBindBlockIndex_Object = MibTableColumn
osCntBindBlockIndex = _OsCntBindBlockIndex_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 10, 1, 1),
    _OsCntBindBlockIndex_Type()
)
osCntBindBlockIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntBindBlockIndex.setStatus("current")


class _OsCntBindCountersMode_Type(Integer32):
    """Custom type osCntBindCountersMode based on Integer32"""
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
        *(("none", 1),
          ("aclIngressCounter", 2),
          ("aclEgressCounter", 3),
          ("portEgressCounter", 4),
          ("vlanEgressCounter", 5),
          ("vlanIngressCounter", 6))
    )


_OsCntBindCountersMode_Type.__name__ = "Integer32"
_OsCntBindCountersMode_Object = MibTableColumn
osCntBindCountersMode = _OsCntBindCountersMode_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 10, 1, 2),
    _OsCntBindCountersMode_Type()
)
osCntBindCountersMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntBindCountersMode.setStatus("current")


class _OsCntBindCountersRange_Type(Integer32):
    """Custom type osCntBindCountersRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("range2k", 1),
          ("range4k", 2))
    )


_OsCntBindCountersRange_Type.__name__ = "Integer32"
_OsCntBindCountersRange_Object = MibTableColumn
osCntBindCountersRange = _OsCntBindCountersRange_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 10, 1, 3),
    _OsCntBindCountersRange_Type()
)
osCntBindCountersRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntBindCountersRange.setStatus("current")


class _OsCntBindLastError_Type(DisplayString):
    """Custom type osCntBindLastError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 160),
    )


_OsCntBindLastError_Type.__name__ = "DisplayString"
_OsCntBindLastError_Object = MibTableColumn
osCntBindLastError = _OsCntBindLastError_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 10, 1, 4),
    _OsCntBindLastError_Type()
)
osCntBindLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntBindLastError.setStatus("current")
_OsCntVBindTable_Object = MibTable
osCntVBindTable = _OsCntVBindTable_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 11)
)
if mibBuilder.loadTexts:
    osCntVBindTable.setStatus("current")
_OsCntVBindEntry_Object = MibTableRow
osCntVBindEntry = _OsCntVBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 11, 1)
)
osCntVBindEntry.setIndexNames(
    (0, "OS-COUNTERS-MIB", "osCntVBindClient"),
)
if mibBuilder.loadTexts:
    osCntVBindEntry.setStatus("current")


class _OsCntVBindClient_Type(Integer32):
    """Custom type osCntVBindClient based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("cncAclIngress", 1),
          ("cncAclSecondIngress", 2),
          ("cncAclEgress", 3),
          ("cncVlanPassIngress", 4),
          ("cncVlanDropIngress", 5),
          ("cncVlanPassEgress", 6),
          ("cncVlanDropEgress", 7),
          ("cncPortEgress", 8),
          ("cncReserved1VBit", 9),
          ("cncReserved2VBit", 10),
          ("cncTrafficManager", 11))
    )


_OsCntVBindClient_Type.__name__ = "Integer32"
_OsCntVBindClient_Object = MibTableColumn
osCntVBindClient = _OsCntVBindClient_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 11, 1, 1),
    _OsCntVBindClient_Type()
)
osCntVBindClient.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osCntVBindClient.setStatus("current")
_OsCntVBindIsActive_Type = TruthValue
_OsCntVBindIsActive_Object = MibTableColumn
osCntVBindIsActive = _OsCntVBindIsActive_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 11, 1, 3),
    _OsCntVBindIsActive_Type()
)
osCntVBindIsActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    osCntVBindIsActive.setStatus("current")


class _OsCntVBindLastError_Type(DisplayString):
    """Custom type osCntVBindLastError based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 160),
    )


_OsCntVBindLastError_Type.__name__ = "DisplayString"
_OsCntVBindLastError_Object = MibTableColumn
osCntVBindLastError = _OsCntVBindLastError_Object(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 11, 1, 4),
    _OsCntVBindLastError_Type()
)
osCntVBindLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osCntVBindLastError.setStatus("current")
_OsCountersConformance_ObjectIdentity = ObjectIdentity
osCountersConformance = _OsCountersConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 100)
)
_OsCountersMIBCompliances_ObjectIdentity = ObjectIdentity
osCountersMIBCompliances = _OsCountersMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 100, 1)
)
_OsCountersMIBGroups_ObjectIdentity = ObjectIdentity
osCountersMIBGroups = _OsCountersMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 100, 2)
)

# Managed Objects groups

osCountersMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 100, 2, 1)
)
osCountersMandatoryGroup.setObjects(
    ("OS-COUNTERS-MIB", "osCountersFeaturesSupport")
)
if mibBuilder.loadTexts:
    osCountersMandatoryGroup.setStatus("current")

osCountersOptGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 100, 2, 2)
)
osCountersOptGroup.setObjects(
      *(("OS-COUNTERS-MIB", "osCntPrtEgrTblStatus"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrCaps"),
        ("OS-COUNTERS-MIB", "osCntVifDirTblStatus"),
        ("OS-COUNTERS-MIB", "osCntVifCaps"),
        ("OS-COUNTERS-MIB", "osCntIngSuiteTblStatus"),
        ("OS-COUNTERS-MIB", "osCntIngSuiteCaps"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteTblStatus"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteCaps"),
        ("OS-COUNTERS-MIB", "osCountersVFeaturesSupport"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrEntryStatus"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrPassGrnOcts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrPassGrnPkts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrPassYlwOcts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrPassYlwPkts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrPassRedOcts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrPassRedPkts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrPassOcts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrPassPkts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrDropGrnOcts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrDropGrnPkts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrDropYlwOcts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrDropYlwPkts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrDropRedOcts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrDropRedPkts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrDropOcts"),
        ("OS-COUNTERS-MIB", "osCntPrtEgrDropPkts"),
        ("OS-COUNTERS-MIB", "osCntVifEntryStatus"),
        ("OS-COUNTERS-MIB", "osCntVifPassOcts"),
        ("OS-COUNTERS-MIB", "osCntVifPassPkts"),
        ("OS-COUNTERS-MIB", "osCntVifDropOcts"),
        ("OS-COUNTERS-MIB", "osCntVifDropPkts"),
        ("OS-COUNTERS-MIB", "osCntIngSuitePortIndex"),
        ("OS-COUNTERS-MIB", "osCntIngSuiteVifIndex"),
        ("OS-COUNTERS-MIB", "osCntIngSuiteServiceLevel"),
        ("OS-COUNTERS-MIB", "osCntIngSuiteEntryStatus"),
        ("OS-COUNTERS-MIB", "osCntIngSuitePassPkts"),
        ("OS-COUNTERS-MIB", "osCntIngSuiteVlanDropPkts"),
        ("OS-COUNTERS-MIB", "osCntIngSuiteSecDropPkts"),
        ("OS-COUNTERS-MIB", "osCntIngSuiteOtherDropPkts"),
        ("OS-COUNTERS-MIB", "osCntEgrSuitePortIndex"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteVifIndex"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteServiceLevel"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteDpLevel"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteIsSkip"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteIsIntPort"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteEntryStatus"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteUcPassPkts"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteMcPassPkts"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteBcPassPkts"),
        ("OS-COUNTERS-MIB", "osCntEgrSuiteTxqDropPkts"),
        ("OS-COUNTERS-MIB", "osCntAclEntryStatus"),
        ("OS-COUNTERS-MIB", "osCntAclMatchOcts"),
        ("OS-COUNTERS-MIB", "osCntAclMatchPkts"),
        ("OS-COUNTERS-MIB", "osCntBindCountersMode"),
        ("OS-COUNTERS-MIB", "osCntBindCountersRange"),
        ("OS-COUNTERS-MIB", "osCntBindLastError"),
        ("OS-COUNTERS-MIB", "osCntVBindIsActive"),
        ("OS-COUNTERS-MIB", "osCntVBindLastError"))
)
if mibBuilder.loadTexts:
    osCountersOptGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osCountersMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6926, 2, 8, 100, 1, 1)
)
osCountersMIBCompliance.setObjects(
      *(("OS-COUNTERS-MIB", "osCountersMandatoryGroup"),
        ("OS-COUNTERS-MIB", "osCountersOptGroup"))
)
if mibBuilder.loadTexts:
    osCountersMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OS-COUNTERS-MIB",
    **{"CntBooleanFlag": CntBooleanFlag,
       "CntEntryStatusVal": CntEntryStatusVal,
       "CntEntryStatusExtVal": CntEntryStatusExtVal,
       "CntTableStatusVal": CntTableStatusVal,
       "CntPortIndex": CntPortIndex,
       "CntPortIndexOrAll": CntPortIndexOrAll,
       "CntVlanId": CntVlanId,
       "CntVlanIdOrAll": CntVlanIdOrAll,
       "CntServiceLevelOrAll": CntServiceLevelOrAll,
       "CntDpLevelOrAll": CntDpLevelOrAll,
       "CntDirection": CntDirection,
       "CntMatchingId": CntMatchingId,
       "osCounters": osCounters,
       "osCountersCapabilities": osCountersCapabilities,
       "osCountersFeaturesSupport": osCountersFeaturesSupport,
       "osCntPrtEgrTblStatus": osCntPrtEgrTblStatus,
       "osCntPrtEgrCaps": osCntPrtEgrCaps,
       "osCntVifDirTable": osCntVifDirTable,
       "osCntVifDirEntry": osCntVifDirEntry,
       "osCntVifDirection": osCntVifDirection,
       "osCntVifDirTblStatus": osCntVifDirTblStatus,
       "osCntVifCaps": osCntVifCaps,
       "osCntIngSuiteTblStatus": osCntIngSuiteTblStatus,
       "osCntIngSuiteCaps": osCntIngSuiteCaps,
       "osCntEgrSuiteTblStatus": osCntEgrSuiteTblStatus,
       "osCntEgrSuiteCaps": osCntEgrSuiteCaps,
       "osCountersVFeaturesSupport": osCountersVFeaturesSupport,
       "osCntPrtEgrTable": osCntPrtEgrTable,
       "osCntPrtEgrEntry": osCntPrtEgrEntry,
       "osCntPrtEgrPortIndex": osCntPrtEgrPortIndex,
       "osCntPrtEgrServiceLevel": osCntPrtEgrServiceLevel,
       "osCntPrtEgrEntryStatus": osCntPrtEgrEntryStatus,
       "osCntPrtEgrPassGrnOcts": osCntPrtEgrPassGrnOcts,
       "osCntPrtEgrPassGrnPkts": osCntPrtEgrPassGrnPkts,
       "osCntPrtEgrPassYlwOcts": osCntPrtEgrPassYlwOcts,
       "osCntPrtEgrPassYlwPkts": osCntPrtEgrPassYlwPkts,
       "osCntPrtEgrPassRedOcts": osCntPrtEgrPassRedOcts,
       "osCntPrtEgrPassRedPkts": osCntPrtEgrPassRedPkts,
       "osCntPrtEgrPassOcts": osCntPrtEgrPassOcts,
       "osCntPrtEgrPassPkts": osCntPrtEgrPassPkts,
       "osCntPrtEgrDropGrnOcts": osCntPrtEgrDropGrnOcts,
       "osCntPrtEgrDropGrnPkts": osCntPrtEgrDropGrnPkts,
       "osCntPrtEgrDropYlwOcts": osCntPrtEgrDropYlwOcts,
       "osCntPrtEgrDropYlwPkts": osCntPrtEgrDropYlwPkts,
       "osCntPrtEgrDropRedOcts": osCntPrtEgrDropRedOcts,
       "osCntPrtEgrDropRedPkts": osCntPrtEgrDropRedPkts,
       "osCntPrtEgrDropOcts": osCntPrtEgrDropOcts,
       "osCntPrtEgrDropPkts": osCntPrtEgrDropPkts,
       "osCntVifTable": osCntVifTable,
       "osCntVifEntry": osCntVifEntry,
       "osCntVifIndex": osCntVifIndex,
       "osCntVifServiceLevel": osCntVifServiceLevel,
       "osCntVifEntryStatus": osCntVifEntryStatus,
       "osCntVifPassOcts": osCntVifPassOcts,
       "osCntVifPassPkts": osCntVifPassPkts,
       "osCntVifDropOcts": osCntVifDropOcts,
       "osCntVifDropPkts": osCntVifDropPkts,
       "osCntIngSuiteTable": osCntIngSuiteTable,
       "osCntIngSuiteEntry": osCntIngSuiteEntry,
       "osCntIngSuiteIndex": osCntIngSuiteIndex,
       "osCntIngSuitePortIndex": osCntIngSuitePortIndex,
       "osCntIngSuiteVifIndex": osCntIngSuiteVifIndex,
       "osCntIngSuiteServiceLevel": osCntIngSuiteServiceLevel,
       "osCntIngSuiteEntryStatus": osCntIngSuiteEntryStatus,
       "osCntIngSuitePassPkts": osCntIngSuitePassPkts,
       "osCntIngSuiteVlanDropPkts": osCntIngSuiteVlanDropPkts,
       "osCntIngSuiteSecDropPkts": osCntIngSuiteSecDropPkts,
       "osCntIngSuiteOtherDropPkts": osCntIngSuiteOtherDropPkts,
       "osCntEgrSuiteTable": osCntEgrSuiteTable,
       "osCntEgrSuiteEntry": osCntEgrSuiteEntry,
       "osCntEgrSuiteIndex": osCntEgrSuiteIndex,
       "osCntEgrSuitePortIndex": osCntEgrSuitePortIndex,
       "osCntEgrSuiteVifIndex": osCntEgrSuiteVifIndex,
       "osCntEgrSuiteServiceLevel": osCntEgrSuiteServiceLevel,
       "osCntEgrSuiteDpLevel": osCntEgrSuiteDpLevel,
       "osCntEgrSuiteIsSkip": osCntEgrSuiteIsSkip,
       "osCntEgrSuiteIsIntPort": osCntEgrSuiteIsIntPort,
       "osCntEgrSuiteEntryStatus": osCntEgrSuiteEntryStatus,
       "osCntEgrSuiteUcPassPkts": osCntEgrSuiteUcPassPkts,
       "osCntEgrSuiteMcPassPkts": osCntEgrSuiteMcPassPkts,
       "osCntEgrSuiteBcPassPkts": osCntEgrSuiteBcPassPkts,
       "osCntEgrSuiteTxqDropPkts": osCntEgrSuiteTxqDropPkts,
       "osCntAclTable": osCntAclTable,
       "osCntAclEntry": osCntAclEntry,
       "osCntAclDirection": osCntAclDirection,
       "osCntAclMatchingIndex": osCntAclMatchingIndex,
       "osCntAclEntryStatus": osCntAclEntryStatus,
       "osCntAclMatchOcts": osCntAclMatchOcts,
       "osCntAclMatchPkts": osCntAclMatchPkts,
       "osCntBindTable": osCntBindTable,
       "osCntBindEntry": osCntBindEntry,
       "osCntBindBlockIndex": osCntBindBlockIndex,
       "osCntBindCountersMode": osCntBindCountersMode,
       "osCntBindCountersRange": osCntBindCountersRange,
       "osCntBindLastError": osCntBindLastError,
       "osCntVBindTable": osCntVBindTable,
       "osCntVBindEntry": osCntVBindEntry,
       "osCntVBindClient": osCntVBindClient,
       "osCntVBindIsActive": osCntVBindIsActive,
       "osCntVBindLastError": osCntVBindLastError,
       "osCountersConformance": osCountersConformance,
       "osCountersMIBCompliances": osCountersMIBCompliances,
       "osCountersMIBCompliance": osCountersMIBCompliance,
       "osCountersMIBGroups": osCountersMIBGroups,
       "osCountersMandatoryGroup": osCountersMandatoryGroup,
       "osCountersOptGroup": osCountersOptGroup}
)
