# SNMP MIB module (INFINERA-PM-ODU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-ODU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:58 2025
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

(HCPerfIntervalCount,) = mibBuilder.importSymbols(
    "HC-PerfHist-TC-MIB",
    "HCPerfIntervalCount")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(perfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "perfMon")

(InfnSampleDuration,
 InfnServiceType,
 InfnValidityBitmap) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnSampleDuration",
    "InfnServiceType",
    "InfnValidityBitmap")

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

oduPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20)
)
if mibBuilder.loadTexts:
    oduPmMIB.setRevisions(
        ("2009-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OduPmRealTable_Object = MibTable
oduPmRealTable = _OduPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1)
)
if mibBuilder.loadTexts:
    oduPmRealTable.setStatus("current")
_OduPmRealEntry_Object = MibTableRow
oduPmRealEntry = _OduPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1)
)
oduPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oduPmRealEntry.setStatus("current")
_OduPmRealRxCVP_Type = HCPerfIntervalCount
_OduPmRealRxCVP_Object = MibTableColumn
oduPmRealRxCVP = _OduPmRealRxCVP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 1),
    _OduPmRealRxCVP_Type()
)
oduPmRealRxCVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealRxCVP.setStatus("current")
_OduPmRealTxCVP_Type = HCPerfIntervalCount
_OduPmRealTxCVP_Object = MibTableColumn
oduPmRealTxCVP = _OduPmRealTxCVP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 2),
    _OduPmRealTxCVP_Type()
)
oduPmRealTxCVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealTxCVP.setStatus("current")
_OduPmRealRxErroredBlocks_Type = HCPerfIntervalCount
_OduPmRealRxErroredBlocks_Object = MibTableColumn
oduPmRealRxErroredBlocks = _OduPmRealRxErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 3),
    _OduPmRealRxErroredBlocks_Type()
)
oduPmRealRxErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealRxErroredBlocks.setStatus("current")
_OduPmRealTxErroredBlocks_Type = HCPerfIntervalCount
_OduPmRealTxErroredBlocks_Object = MibTableColumn
oduPmRealTxErroredBlocks = _OduPmRealTxErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 4),
    _OduPmRealTxErroredBlocks_Type()
)
oduPmRealTxErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealTxErroredBlocks.setStatus("current")
_OduPmRealRxDefectSeconds_Type = Integer32
_OduPmRealRxDefectSeconds_Object = MibTableColumn
oduPmRealRxDefectSeconds = _OduPmRealRxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 5),
    _OduPmRealRxDefectSeconds_Type()
)
oduPmRealRxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealRxDefectSeconds.setStatus("current")
_OduPmRealTxDefectSeconds_Type = Integer32
_OduPmRealTxDefectSeconds_Object = MibTableColumn
oduPmRealTxDefectSeconds = _OduPmRealTxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 6),
    _OduPmRealTxDefectSeconds_Type()
)
oduPmRealTxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealTxDefectSeconds.setStatus("current")
_OduPmRealRxBeiCount_Type = HCPerfIntervalCount
_OduPmRealRxBeiCount_Object = MibTableColumn
oduPmRealRxBeiCount = _OduPmRealRxBeiCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 7),
    _OduPmRealRxBeiCount_Type()
)
oduPmRealRxBeiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealRxBeiCount.setStatus("current")
_OduPmRealTxBeiCount_Type = HCPerfIntervalCount
_OduPmRealTxBeiCount_Object = MibTableColumn
oduPmRealTxBeiCount = _OduPmRealTxBeiCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 8),
    _OduPmRealTxBeiCount_Type()
)
oduPmRealTxBeiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealTxBeiCount.setStatus("current")
_OduPmRealRxErroredBlocksFEND_Type = HCPerfIntervalCount
_OduPmRealRxErroredBlocksFEND_Object = MibTableColumn
oduPmRealRxErroredBlocksFEND = _OduPmRealRxErroredBlocksFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 9),
    _OduPmRealRxErroredBlocksFEND_Type()
)
oduPmRealRxErroredBlocksFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealRxErroredBlocksFEND.setStatus("current")
_OduPmRealTxErroredBlocksFEND_Type = HCPerfIntervalCount
_OduPmRealTxErroredBlocksFEND_Object = MibTableColumn
oduPmRealTxErroredBlocksFEND = _OduPmRealTxErroredBlocksFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 10),
    _OduPmRealTxErroredBlocksFEND_Type()
)
oduPmRealTxErroredBlocksFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealTxErroredBlocksFEND.setStatus("current")
_OduPmRealRxDefectSecondsFEND_Type = Integer32
_OduPmRealRxDefectSecondsFEND_Object = MibTableColumn
oduPmRealRxDefectSecondsFEND = _OduPmRealRxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 11),
    _OduPmRealRxDefectSecondsFEND_Type()
)
oduPmRealRxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealRxDefectSecondsFEND.setStatus("current")
_OduPmRealTxDefectSecondsFEND_Type = Integer32
_OduPmRealTxDefectSecondsFEND_Object = MibTableColumn
oduPmRealTxDefectSecondsFEND = _OduPmRealTxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 12),
    _OduPmRealTxDefectSecondsFEND_Type()
)
oduPmRealTxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealTxDefectSecondsFEND.setStatus("current")
_OduPmRealTribPRBSErr_Type = HCPerfIntervalCount
_OduPmRealTribPRBSErr_Object = MibTableColumn
oduPmRealTribPRBSErr = _OduPmRealTribPRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 13),
    _OduPmRealTribPRBSErr_Type()
)
oduPmRealTribPRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealTribPRBSErr.setStatus("current")
_OduPmRealTribPRBSSyncErr_Type = Integer32
_OduPmRealTribPRBSSyncErr_Object = MibTableColumn
oduPmRealTribPRBSSyncErr = _OduPmRealTribPRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 14),
    _OduPmRealTribPRBSSyncErr_Type()
)
oduPmRealTribPRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealTribPRBSSyncErr.setStatus("current")
_OduPmRealLinePRBSErr_Type = HCPerfIntervalCount
_OduPmRealLinePRBSErr_Object = MibTableColumn
oduPmRealLinePRBSErr = _OduPmRealLinePRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 15),
    _OduPmRealLinePRBSErr_Type()
)
oduPmRealLinePRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealLinePRBSErr.setStatus("current")
_OduPmRealLinePRBSSyncErr_Type = Integer32
_OduPmRealLinePRBSSyncErr_Object = MibTableColumn
oduPmRealLinePRBSSyncErr = _OduPmRealLinePRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 1, 1, 16),
    _OduPmRealLinePRBSSyncErr_Type()
)
oduPmRealLinePRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRealLinePRBSSyncErr.setStatus("current")
_OduPmTable_Object = MibTable
oduPmTable = _OduPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2)
)
if mibBuilder.loadTexts:
    oduPmTable.setStatus("current")
_OduPmEntry_Object = MibTableRow
oduPmEntry = _OduPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1)
)
oduPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-ODU-MIB", "oduPmSampleDuration"),
    (0, "INFINERA-PM-ODU-MIB", "oduPmTimestamp"),
)
if mibBuilder.loadTexts:
    oduPmEntry.setStatus("current")


class _OduPmTimestamp_Type(Integer32):
    """Custom type oduPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OduPmTimestamp_Type.__name__ = "Integer32"
_OduPmTimestamp_Object = MibTableColumn
oduPmTimestamp = _OduPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 1),
    _OduPmTimestamp_Type()
)
oduPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oduPmTimestamp.setStatus("current")
_OduPmSampleDuration_Type = InfnSampleDuration
_OduPmSampleDuration_Object = MibTableColumn
oduPmSampleDuration = _OduPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 2),
    _OduPmSampleDuration_Type()
)
oduPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oduPmSampleDuration.setStatus("current")
_OduPmValidity_Type = InfnValidityBitmap
_OduPmValidity_Object = MibTableColumn
oduPmValidity = _OduPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 3),
    _OduPmValidity_Type()
)
oduPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmValidity.setStatus("current")
_OduPmRxCVP_Type = HCPerfIntervalCount
_OduPmRxCVP_Object = MibTableColumn
oduPmRxCVP = _OduPmRxCVP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 4),
    _OduPmRxCVP_Type()
)
oduPmRxCVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRxCVP.setStatus("current")
_OduPmTxCVP_Type = HCPerfIntervalCount
_OduPmTxCVP_Object = MibTableColumn
oduPmTxCVP = _OduPmTxCVP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 5),
    _OduPmTxCVP_Type()
)
oduPmTxCVP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmTxCVP.setStatus("current")
_OduPmRxErroredBlocks_Type = HCPerfIntervalCount
_OduPmRxErroredBlocks_Object = MibTableColumn
oduPmRxErroredBlocks = _OduPmRxErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 6),
    _OduPmRxErroredBlocks_Type()
)
oduPmRxErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRxErroredBlocks.setStatus("current")
_OduPmTxErroredBlocks_Type = HCPerfIntervalCount
_OduPmTxErroredBlocks_Object = MibTableColumn
oduPmTxErroredBlocks = _OduPmTxErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 7),
    _OduPmTxErroredBlocks_Type()
)
oduPmTxErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmTxErroredBlocks.setStatus("current")
_OduPmRxDefectSeconds_Type = Integer32
_OduPmRxDefectSeconds_Object = MibTableColumn
oduPmRxDefectSeconds = _OduPmRxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 9),
    _OduPmRxDefectSeconds_Type()
)
oduPmRxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRxDefectSeconds.setStatus("current")
_OduPmTxDefectSeconds_Type = Integer32
_OduPmTxDefectSeconds_Object = MibTableColumn
oduPmTxDefectSeconds = _OduPmTxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 10),
    _OduPmTxDefectSeconds_Type()
)
oduPmTxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmTxDefectSeconds.setStatus("current")
_OduPmRxBeiCount_Type = HCPerfIntervalCount
_OduPmRxBeiCount_Object = MibTableColumn
oduPmRxBeiCount = _OduPmRxBeiCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 11),
    _OduPmRxBeiCount_Type()
)
oduPmRxBeiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRxBeiCount.setStatus("current")
_OduPmTxBeiCount_Type = HCPerfIntervalCount
_OduPmTxBeiCount_Object = MibTableColumn
oduPmTxBeiCount = _OduPmTxBeiCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 12),
    _OduPmTxBeiCount_Type()
)
oduPmTxBeiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmTxBeiCount.setStatus("current")
_OduPmCircuitId_Type = DisplayString
_OduPmCircuitId_Object = MibTableColumn
oduPmCircuitId = _OduPmCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 13),
    _OduPmCircuitId_Type()
)
oduPmCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmCircuitId.setStatus("current")
_OduPmPayloadType_Type = InfnServiceType
_OduPmPayloadType_Object = MibTableColumn
oduPmPayloadType = _OduPmPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 14),
    _OduPmPayloadType_Type()
)
oduPmPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmPayloadType.setStatus("current")
_OduPmRxErroredBlocksFEND_Type = HCPerfIntervalCount
_OduPmRxErroredBlocksFEND_Object = MibTableColumn
oduPmRxErroredBlocksFEND = _OduPmRxErroredBlocksFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 15),
    _OduPmRxErroredBlocksFEND_Type()
)
oduPmRxErroredBlocksFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRxErroredBlocksFEND.setStatus("current")
_OduPmTxErroredBlocksFEND_Type = HCPerfIntervalCount
_OduPmTxErroredBlocksFEND_Object = MibTableColumn
oduPmTxErroredBlocksFEND = _OduPmTxErroredBlocksFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 16),
    _OduPmTxErroredBlocksFEND_Type()
)
oduPmTxErroredBlocksFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmTxErroredBlocksFEND.setStatus("current")
_OduPmRxDefectSecondsFEND_Type = Integer32
_OduPmRxDefectSecondsFEND_Object = MibTableColumn
oduPmRxDefectSecondsFEND = _OduPmRxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 17),
    _OduPmRxDefectSecondsFEND_Type()
)
oduPmRxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmRxDefectSecondsFEND.setStatus("current")
_OduPmTxDefectSecondsFEND_Type = Integer32
_OduPmTxDefectSecondsFEND_Object = MibTableColumn
oduPmTxDefectSecondsFEND = _OduPmTxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 18),
    _OduPmTxDefectSecondsFEND_Type()
)
oduPmTxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmTxDefectSecondsFEND.setStatus("current")
_OduPmTribPRBSErr_Type = HCPerfIntervalCount
_OduPmTribPRBSErr_Object = MibTableColumn
oduPmTribPRBSErr = _OduPmTribPRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 19),
    _OduPmTribPRBSErr_Type()
)
oduPmTribPRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmTribPRBSErr.setStatus("current")
_OduPmTribPRBSSyncErr_Type = Integer32
_OduPmTribPRBSSyncErr_Object = MibTableColumn
oduPmTribPRBSSyncErr = _OduPmTribPRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 20),
    _OduPmTribPRBSSyncErr_Type()
)
oduPmTribPRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmTribPRBSSyncErr.setStatus("current")
_OduPmLinePRBSErr_Type = HCPerfIntervalCount
_OduPmLinePRBSErr_Object = MibTableColumn
oduPmLinePRBSErr = _OduPmLinePRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 21),
    _OduPmLinePRBSErr_Type()
)
oduPmLinePRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmLinePRBSErr.setStatus("current")
_OduPmLinePRBSSyncErr_Type = Integer32
_OduPmLinePRBSSyncErr_Object = MibTableColumn
oduPmLinePRBSSyncErr = _OduPmLinePRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 2, 1, 22),
    _OduPmLinePRBSSyncErr_Type()
)
oduPmLinePRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oduPmLinePRBSSyncErr.setStatus("current")
_OduPmConformance_ObjectIdentity = ObjectIdentity
oduPmConformance = _OduPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 3)
)
_OduPmCompliances_ObjectIdentity = ObjectIdentity
oduPmCompliances = _OduPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 3, 1)
)
_OduPmGroups_ObjectIdentity = ObjectIdentity
oduPmGroups = _OduPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 3, 2)
)

# Managed Objects groups

oduPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 3, 2, 1)
)
oduPmGroup.setObjects(
      *(("INFINERA-PM-ODU-MIB", "oduPmTimestamp"),
        ("INFINERA-PM-ODU-MIB", "oduPmSampleDuration"),
        ("INFINERA-PM-ODU-MIB", "oduPmValidity"),
        ("INFINERA-PM-ODU-MIB", "oduPmRxCVP"),
        ("INFINERA-PM-ODU-MIB", "oduPmTxCVP"),
        ("INFINERA-PM-ODU-MIB", "oduPmRxErroredBlocks"),
        ("INFINERA-PM-ODU-MIB", "oduPmTxErroredBlocks"),
        ("INFINERA-PM-ODU-MIB", "oduPmRxDefectSeconds"),
        ("INFINERA-PM-ODU-MIB", "oduPmTxDefectSeconds"),
        ("INFINERA-PM-ODU-MIB", "oduPmRxBeiCount"),
        ("INFINERA-PM-ODU-MIB", "oduPmTxBeiCount"),
        ("INFINERA-PM-ODU-MIB", "oduPmCircuitId"),
        ("INFINERA-PM-ODU-MIB", "oduPmPayloadType"),
        ("INFINERA-PM-ODU-MIB", "oduPmRxErroredBlocksFEND"),
        ("INFINERA-PM-ODU-MIB", "oduPmTxErroredBlocksFEND"),
        ("INFINERA-PM-ODU-MIB", "oduPmRxDefectSecondsFEND"),
        ("INFINERA-PM-ODU-MIB", "oduPmTxDefectSecondsFEND"),
        ("INFINERA-PM-ODU-MIB", "oduPmTribPRBSErr"),
        ("INFINERA-PM-ODU-MIB", "oduPmTribPRBSSyncErr"),
        ("INFINERA-PM-ODU-MIB", "oduPmLinePRBSErr"),
        ("INFINERA-PM-ODU-MIB", "oduPmLinePRBSSyncErr"))
)
if mibBuilder.loadTexts:
    oduPmGroup.setStatus("current")

oduPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 3, 2, 2)
)
oduPmRealGroup.setObjects(
      *(("INFINERA-PM-ODU-MIB", "oduPmRealRxCVP"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealTxCVP"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealRxErroredBlocks"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealTxErroredBlocks"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealRxDefectSeconds"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealTxDefectSeconds"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealRxBeiCount"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealTxBeiCount"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealRxErroredBlocksFEND"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealTxErroredBlocksFEND"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealRxDefectSecondsFEND"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealTxDefectSecondsFEND"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealTribPRBSErr"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealTribPRBSSyncErr"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealLinePRBSErr"),
        ("INFINERA-PM-ODU-MIB", "oduPmRealLinePRBSSyncErr"))
)
if mibBuilder.loadTexts:
    oduPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oduPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 3, 1, 1)
)
oduPmCompliance.setObjects(
    ("INFINERA-PM-ODU-MIB", "oduPmGroup")
)
if mibBuilder.loadTexts:
    oduPmCompliance.setStatus(
        "current"
    )

oduPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 20, 3, 1, 2)
)
oduPmRealCompliance.setObjects(
    ("INFINERA-PM-ODU-MIB", "oduPmRealGroup")
)
if mibBuilder.loadTexts:
    oduPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-ODU-MIB",
    **{"oduPmMIB": oduPmMIB,
       "oduPmRealTable": oduPmRealTable,
       "oduPmRealEntry": oduPmRealEntry,
       "oduPmRealRxCVP": oduPmRealRxCVP,
       "oduPmRealTxCVP": oduPmRealTxCVP,
       "oduPmRealRxErroredBlocks": oduPmRealRxErroredBlocks,
       "oduPmRealTxErroredBlocks": oduPmRealTxErroredBlocks,
       "oduPmRealRxDefectSeconds": oduPmRealRxDefectSeconds,
       "oduPmRealTxDefectSeconds": oduPmRealTxDefectSeconds,
       "oduPmRealRxBeiCount": oduPmRealRxBeiCount,
       "oduPmRealTxBeiCount": oduPmRealTxBeiCount,
       "oduPmRealRxErroredBlocksFEND": oduPmRealRxErroredBlocksFEND,
       "oduPmRealTxErroredBlocksFEND": oduPmRealTxErroredBlocksFEND,
       "oduPmRealRxDefectSecondsFEND": oduPmRealRxDefectSecondsFEND,
       "oduPmRealTxDefectSecondsFEND": oduPmRealTxDefectSecondsFEND,
       "oduPmRealTribPRBSErr": oduPmRealTribPRBSErr,
       "oduPmRealTribPRBSSyncErr": oduPmRealTribPRBSSyncErr,
       "oduPmRealLinePRBSErr": oduPmRealLinePRBSErr,
       "oduPmRealLinePRBSSyncErr": oduPmRealLinePRBSSyncErr,
       "oduPmTable": oduPmTable,
       "oduPmEntry": oduPmEntry,
       "oduPmTimestamp": oduPmTimestamp,
       "oduPmSampleDuration": oduPmSampleDuration,
       "oduPmValidity": oduPmValidity,
       "oduPmRxCVP": oduPmRxCVP,
       "oduPmTxCVP": oduPmTxCVP,
       "oduPmRxErroredBlocks": oduPmRxErroredBlocks,
       "oduPmTxErroredBlocks": oduPmTxErroredBlocks,
       "oduPmRxDefectSeconds": oduPmRxDefectSeconds,
       "oduPmTxDefectSeconds": oduPmTxDefectSeconds,
       "oduPmRxBeiCount": oduPmRxBeiCount,
       "oduPmTxBeiCount": oduPmTxBeiCount,
       "oduPmCircuitId": oduPmCircuitId,
       "oduPmPayloadType": oduPmPayloadType,
       "oduPmRxErroredBlocksFEND": oduPmRxErroredBlocksFEND,
       "oduPmTxErroredBlocksFEND": oduPmTxErroredBlocksFEND,
       "oduPmRxDefectSecondsFEND": oduPmRxDefectSecondsFEND,
       "oduPmTxDefectSecondsFEND": oduPmTxDefectSecondsFEND,
       "oduPmTribPRBSErr": oduPmTribPRBSErr,
       "oduPmTribPRBSSyncErr": oduPmTribPRBSSyncErr,
       "oduPmLinePRBSErr": oduPmLinePRBSErr,
       "oduPmLinePRBSSyncErr": oduPmLinePRBSSyncErr,
       "oduPmConformance": oduPmConformance,
       "oduPmCompliances": oduPmCompliances,
       "oduPmCompliance": oduPmCompliance,
       "oduPmRealCompliance": oduPmRealCompliance,
       "oduPmGroups": oduPmGroups,
       "oduPmGroup": oduPmGroup,
       "oduPmRealGroup": oduPmRealGroup}
)
