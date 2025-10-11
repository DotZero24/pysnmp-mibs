# SNMP MIB module (INFINERA-PM-OTU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-OTU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:54 2025
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

(FloatHundredths,
 InfnSampleDuration,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnSampleDuration",
    "InfnServiceType")

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

otuPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22)
)
if mibBuilder.loadTexts:
    otuPmMIB.setRevisions(
        ("2009-07-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtuPmRealTable_Object = MibTable
otuPmRealTable = _OtuPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1)
)
if mibBuilder.loadTexts:
    otuPmRealTable.setStatus("current")
_OtuPmRealEntry_Object = MibTableRow
otuPmRealEntry = _OtuPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1)
)
otuPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    otuPmRealEntry.setStatus("current")
_OtuPmRealNumberOfCodeWords_Type = HCPerfIntervalCount
_OtuPmRealNumberOfCodeWords_Object = MibTableColumn
otuPmRealNumberOfCodeWords = _OtuPmRealNumberOfCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 1),
    _OtuPmRealNumberOfCodeWords_Type()
)
otuPmRealNumberOfCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealNumberOfCodeWords.setStatus("current")
_OtuPmRealNumberOfUncorrectedWords_Type = HCPerfIntervalCount
_OtuPmRealNumberOfUncorrectedWords_Object = MibTableColumn
otuPmRealNumberOfUncorrectedWords = _OtuPmRealNumberOfUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 2),
    _OtuPmRealNumberOfUncorrectedWords_Type()
)
otuPmRealNumberOfUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealNumberOfUncorrectedWords.setStatus("current")
_OtuPmRealNumberOfCorrectedZeros_Type = HCPerfIntervalCount
_OtuPmRealNumberOfCorrectedZeros_Object = MibTableColumn
otuPmRealNumberOfCorrectedZeros = _OtuPmRealNumberOfCorrectedZeros_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 3),
    _OtuPmRealNumberOfCorrectedZeros_Type()
)
otuPmRealNumberOfCorrectedZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealNumberOfCorrectedZeros.setStatus("current")
_OtuPmRealNumberOfCorrectedOnes_Type = HCPerfIntervalCount
_OtuPmRealNumberOfCorrectedOnes_Object = MibTableColumn
otuPmRealNumberOfCorrectedOnes = _OtuPmRealNumberOfCorrectedOnes_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 4),
    _OtuPmRealNumberOfCorrectedOnes_Type()
)
otuPmRealNumberOfCorrectedOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealNumberOfCorrectedOnes.setStatus("current")
_OtuPmRealRxCVS_Type = HCPerfIntervalCount
_OtuPmRealRxCVS_Object = MibTableColumn
otuPmRealRxCVS = _OtuPmRealRxCVS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 5),
    _OtuPmRealRxCVS_Type()
)
otuPmRealRxCVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealRxCVS.setStatus("current")
_OtuPmRealTxCVS_Type = HCPerfIntervalCount
_OtuPmRealTxCVS_Object = MibTableColumn
otuPmRealTxCVS = _OtuPmRealTxCVS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 6),
    _OtuPmRealTxCVS_Type()
)
otuPmRealTxCVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealTxCVS.setStatus("current")
_OtuPmRealRxErroredBlocks_Type = HCPerfIntervalCount
_OtuPmRealRxErroredBlocks_Object = MibTableColumn
otuPmRealRxErroredBlocks = _OtuPmRealRxErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 7),
    _OtuPmRealRxErroredBlocks_Type()
)
otuPmRealRxErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealRxErroredBlocks.setStatus("current")
_OtuPmRealTxErroredBlocks_Type = HCPerfIntervalCount
_OtuPmRealTxErroredBlocks_Object = MibTableColumn
otuPmRealTxErroredBlocks = _OtuPmRealTxErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 8),
    _OtuPmRealTxErroredBlocks_Type()
)
otuPmRealTxErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealTxErroredBlocks.setStatus("current")
_OtuPmRealRxDefectSeconds_Type = Integer32
_OtuPmRealRxDefectSeconds_Object = MibTableColumn
otuPmRealRxDefectSeconds = _OtuPmRealRxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 9),
    _OtuPmRealRxDefectSeconds_Type()
)
otuPmRealRxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealRxDefectSeconds.setStatus("current")
_OtuPmRealTxDefectSeconds_Type = Integer32
_OtuPmRealTxDefectSeconds_Object = MibTableColumn
otuPmRealTxDefectSeconds = _OtuPmRealTxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 10),
    _OtuPmRealTxDefectSeconds_Type()
)
otuPmRealTxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealTxDefectSeconds.setStatus("current")
_OtuPmRealTribPRBSErr_Type = HCPerfIntervalCount
_OtuPmRealTribPRBSErr_Object = MibTableColumn
otuPmRealTribPRBSErr = _OtuPmRealTribPRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 11),
    _OtuPmRealTribPRBSErr_Type()
)
otuPmRealTribPRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealTribPRBSErr.setStatus("current")
_OtuPmRealLinePRBSErr_Type = HCPerfIntervalCount
_OtuPmRealLinePRBSErr_Object = MibTableColumn
otuPmRealLinePRBSErr = _OtuPmRealLinePRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 12),
    _OtuPmRealLinePRBSErr_Type()
)
otuPmRealLinePRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealLinePRBSErr.setStatus("current")
_OtuPmRealTribPRBSSyncErr_Type = Integer32
_OtuPmRealTribPRBSSyncErr_Object = MibTableColumn
otuPmRealTribPRBSSyncErr = _OtuPmRealTribPRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 13),
    _OtuPmRealTribPRBSSyncErr_Type()
)
otuPmRealTribPRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealTribPRBSSyncErr.setStatus("current")
_OtuPmRealLinePRBSSyncErr_Type = Integer32
_OtuPmRealLinePRBSSyncErr_Object = MibTableColumn
otuPmRealLinePRBSSyncErr = _OtuPmRealLinePRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 14),
    _OtuPmRealLinePRBSSyncErr_Type()
)
otuPmRealLinePRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealLinePRBSSyncErr.setStatus("current")
_OtuPmRealRxBeiCount_Type = HCPerfIntervalCount
_OtuPmRealRxBeiCount_Object = MibTableColumn
otuPmRealRxBeiCount = _OtuPmRealRxBeiCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 15),
    _OtuPmRealRxBeiCount_Type()
)
otuPmRealRxBeiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealRxBeiCount.setStatus("current")
_OtuPmRealTxBeiCount_Type = HCPerfIntervalCount
_OtuPmRealTxBeiCount_Object = MibTableColumn
otuPmRealTxBeiCount = _OtuPmRealTxBeiCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 16),
    _OtuPmRealTxBeiCount_Type()
)
otuPmRealTxBeiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealTxBeiCount.setStatus("current")
_OtuPmRealRxErroredBlocksFEND_Type = HCPerfIntervalCount
_OtuPmRealRxErroredBlocksFEND_Object = MibTableColumn
otuPmRealRxErroredBlocksFEND = _OtuPmRealRxErroredBlocksFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 17),
    _OtuPmRealRxErroredBlocksFEND_Type()
)
otuPmRealRxErroredBlocksFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealRxErroredBlocksFEND.setStatus("current")
_OtuPmRealTxErroredBlocksFEND_Type = HCPerfIntervalCount
_OtuPmRealTxErroredBlocksFEND_Object = MibTableColumn
otuPmRealTxErroredBlocksFEND = _OtuPmRealTxErroredBlocksFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 18),
    _OtuPmRealTxErroredBlocksFEND_Type()
)
otuPmRealTxErroredBlocksFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealTxErroredBlocksFEND.setStatus("current")
_OtuPmRealRxDefectSecondsFEND_Type = Integer32
_OtuPmRealRxDefectSecondsFEND_Object = MibTableColumn
otuPmRealRxDefectSecondsFEND = _OtuPmRealRxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 19),
    _OtuPmRealRxDefectSecondsFEND_Type()
)
otuPmRealRxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealRxDefectSecondsFEND.setStatus("current")
_OtuPmRealTxDefectSecondsFEND_Type = Integer32
_OtuPmRealTxDefectSecondsFEND_Object = MibTableColumn
otuPmRealTxDefectSecondsFEND = _OtuPmRealTxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 20),
    _OtuPmRealTxDefectSecondsFEND_Type()
)
otuPmRealTxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealTxDefectSecondsFEND.setStatus("current")
_OtuPmRealCorrectedBits_Type = HCPerfIntervalCount
_OtuPmRealCorrectedBits_Object = MibTableColumn
otuPmRealCorrectedBits = _OtuPmRealCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 21),
    _OtuPmRealCorrectedBits_Type()
)
otuPmRealCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealCorrectedBits.setStatus("current")
_OtuPmRealRxIAE_Type = Integer32
_OtuPmRealRxIAE_Object = MibTableColumn
otuPmRealRxIAE = _OtuPmRealRxIAE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 22),
    _OtuPmRealRxIAE_Type()
)
otuPmRealRxIAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealRxIAE.setStatus("current")
_OtuPmRealTxIAE_Type = Integer32
_OtuPmRealTxIAE_Object = MibTableColumn
otuPmRealTxIAE = _OtuPmRealTxIAE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 23),
    _OtuPmRealTxIAE_Type()
)
otuPmRealTxIAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealTxIAE.setStatus("current")
_OtuPmRealRxBIAE_Type = Integer32
_OtuPmRealRxBIAE_Object = MibTableColumn
otuPmRealRxBIAE = _OtuPmRealRxBIAE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 24),
    _OtuPmRealRxBIAE_Type()
)
otuPmRealRxBIAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealRxBIAE.setStatus("current")
_OtuPmRealTxBIAE_Type = Integer32
_OtuPmRealTxBIAE_Object = MibTableColumn
otuPmRealTxBIAE = _OtuPmRealTxBIAE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 1, 1, 25),
    _OtuPmRealTxBIAE_Type()
)
otuPmRealTxBIAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRealTxBIAE.setStatus("current")
_OtuPmTable_Object = MibTable
otuPmTable = _OtuPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2)
)
if mibBuilder.loadTexts:
    otuPmTable.setStatus("current")
_OtuPmEntry_Object = MibTableRow
otuPmEntry = _OtuPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1)
)
otuPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-OTU-MIB", "otuPmSampleDuration"),
    (0, "INFINERA-PM-OTU-MIB", "otuPmTimestamp"),
)
if mibBuilder.loadTexts:
    otuPmEntry.setStatus("current")


class _OtuPmTimestamp_Type(Integer32):
    """Custom type otuPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OtuPmTimestamp_Type.__name__ = "Integer32"
_OtuPmTimestamp_Object = MibTableColumn
otuPmTimestamp = _OtuPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 1),
    _OtuPmTimestamp_Type()
)
otuPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    otuPmTimestamp.setStatus("current")
_OtuPmSampleDuration_Type = InfnSampleDuration
_OtuPmSampleDuration_Object = MibTableColumn
otuPmSampleDuration = _OtuPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 2),
    _OtuPmSampleDuration_Type()
)
otuPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    otuPmSampleDuration.setStatus("current")
_OtuPmValidity_Type = TruthValue
_OtuPmValidity_Object = MibTableColumn
otuPmValidity = _OtuPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 3),
    _OtuPmValidity_Type()
)
otuPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmValidity.setStatus("current")
_OtuPmNumberOfCodeWords_Type = HCPerfIntervalCount
_OtuPmNumberOfCodeWords_Object = MibTableColumn
otuPmNumberOfCodeWords = _OtuPmNumberOfCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 4),
    _OtuPmNumberOfCodeWords_Type()
)
otuPmNumberOfCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmNumberOfCodeWords.setStatus("current")
_OtuPmNumberOfUncorrectedWords_Type = HCPerfIntervalCount
_OtuPmNumberOfUncorrectedWords_Object = MibTableColumn
otuPmNumberOfUncorrectedWords = _OtuPmNumberOfUncorrectedWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 5),
    _OtuPmNumberOfUncorrectedWords_Type()
)
otuPmNumberOfUncorrectedWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmNumberOfUncorrectedWords.setStatus("current")
_OtuPmNumberOfCorrectedZeros_Type = HCPerfIntervalCount
_OtuPmNumberOfCorrectedZeros_Object = MibTableColumn
otuPmNumberOfCorrectedZeros = _OtuPmNumberOfCorrectedZeros_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 6),
    _OtuPmNumberOfCorrectedZeros_Type()
)
otuPmNumberOfCorrectedZeros.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmNumberOfCorrectedZeros.setStatus("current")
_OtuPmNumberOfCorrectedOnes_Type = HCPerfIntervalCount
_OtuPmNumberOfCorrectedOnes_Object = MibTableColumn
otuPmNumberOfCorrectedOnes = _OtuPmNumberOfCorrectedOnes_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 7),
    _OtuPmNumberOfCorrectedOnes_Type()
)
otuPmNumberOfCorrectedOnes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmNumberOfCorrectedOnes.setStatus("current")
_OtuPmRxCVS_Type = HCPerfIntervalCount
_OtuPmRxCVS_Object = MibTableColumn
otuPmRxCVS = _OtuPmRxCVS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 8),
    _OtuPmRxCVS_Type()
)
otuPmRxCVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRxCVS.setStatus("current")
_OtuPmTxCVS_Type = HCPerfIntervalCount
_OtuPmTxCVS_Object = MibTableColumn
otuPmTxCVS = _OtuPmTxCVS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 9),
    _OtuPmTxCVS_Type()
)
otuPmTxCVS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmTxCVS.setStatus("current")
_OtuPmRxErroredBlocks_Type = HCPerfIntervalCount
_OtuPmRxErroredBlocks_Object = MibTableColumn
otuPmRxErroredBlocks = _OtuPmRxErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 10),
    _OtuPmRxErroredBlocks_Type()
)
otuPmRxErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRxErroredBlocks.setStatus("current")
_OtuPmTxErroredBlocks_Type = HCPerfIntervalCount
_OtuPmTxErroredBlocks_Object = MibTableColumn
otuPmTxErroredBlocks = _OtuPmTxErroredBlocks_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 11),
    _OtuPmTxErroredBlocks_Type()
)
otuPmTxErroredBlocks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmTxErroredBlocks.setStatus("current")
_OtuPmRxDefectSeconds_Type = Integer32
_OtuPmRxDefectSeconds_Object = MibTableColumn
otuPmRxDefectSeconds = _OtuPmRxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 12),
    _OtuPmRxDefectSeconds_Type()
)
otuPmRxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRxDefectSeconds.setStatus("current")
_OtuPmTxDefectSeconds_Type = Integer32
_OtuPmTxDefectSeconds_Object = MibTableColumn
otuPmTxDefectSeconds = _OtuPmTxDefectSeconds_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 13),
    _OtuPmTxDefectSeconds_Type()
)
otuPmTxDefectSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmTxDefectSeconds.setStatus("current")
_OtuPmTribPRBSErr_Type = HCPerfIntervalCount
_OtuPmTribPRBSErr_Object = MibTableColumn
otuPmTribPRBSErr = _OtuPmTribPRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 14),
    _OtuPmTribPRBSErr_Type()
)
otuPmTribPRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmTribPRBSErr.setStatus("current")
_OtuPmLinePRBSErr_Type = HCPerfIntervalCount
_OtuPmLinePRBSErr_Object = MibTableColumn
otuPmLinePRBSErr = _OtuPmLinePRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 15),
    _OtuPmLinePRBSErr_Type()
)
otuPmLinePRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmLinePRBSErr.setStatus("current")
_OtuPmTribPRBSSyncErr_Type = Integer32
_OtuPmTribPRBSSyncErr_Object = MibTableColumn
otuPmTribPRBSSyncErr = _OtuPmTribPRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 16),
    _OtuPmTribPRBSSyncErr_Type()
)
otuPmTribPRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmTribPRBSSyncErr.setStatus("current")
_OtuPmLinePRBSSyncErr_Type = Integer32
_OtuPmLinePRBSSyncErr_Object = MibTableColumn
otuPmLinePRBSSyncErr = _OtuPmLinePRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 17),
    _OtuPmLinePRBSSyncErr_Type()
)
otuPmLinePRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmLinePRBSSyncErr.setStatus("current")
_OtuPmRxBeiCount_Type = HCPerfIntervalCount
_OtuPmRxBeiCount_Object = MibTableColumn
otuPmRxBeiCount = _OtuPmRxBeiCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 18),
    _OtuPmRxBeiCount_Type()
)
otuPmRxBeiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRxBeiCount.setStatus("current")
_OtuPmTxBeiCount_Type = HCPerfIntervalCount
_OtuPmTxBeiCount_Object = MibTableColumn
otuPmTxBeiCount = _OtuPmTxBeiCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 19),
    _OtuPmTxBeiCount_Type()
)
otuPmTxBeiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmTxBeiCount.setStatus("current")
_OtuPmCircuitId_Type = DisplayString
_OtuPmCircuitId_Object = MibTableColumn
otuPmCircuitId = _OtuPmCircuitId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 20),
    _OtuPmCircuitId_Type()
)
otuPmCircuitId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmCircuitId.setStatus("current")
_OtuPmPayloadType_Type = InfnServiceType
_OtuPmPayloadType_Object = MibTableColumn
otuPmPayloadType = _OtuPmPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 21),
    _OtuPmPayloadType_Type()
)
otuPmPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmPayloadType.setStatus("current")
_OtuPmRxErroredBlocksFEND_Type = HCPerfIntervalCount
_OtuPmRxErroredBlocksFEND_Object = MibTableColumn
otuPmRxErroredBlocksFEND = _OtuPmRxErroredBlocksFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 22),
    _OtuPmRxErroredBlocksFEND_Type()
)
otuPmRxErroredBlocksFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRxErroredBlocksFEND.setStatus("current")
_OtuPmTxErroredBlocksFEND_Type = HCPerfIntervalCount
_OtuPmTxErroredBlocksFEND_Object = MibTableColumn
otuPmTxErroredBlocksFEND = _OtuPmTxErroredBlocksFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 23),
    _OtuPmTxErroredBlocksFEND_Type()
)
otuPmTxErroredBlocksFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmTxErroredBlocksFEND.setStatus("current")
_OtuPmRxDefectSecondsFEND_Type = Integer32
_OtuPmRxDefectSecondsFEND_Object = MibTableColumn
otuPmRxDefectSecondsFEND = _OtuPmRxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 24),
    _OtuPmRxDefectSecondsFEND_Type()
)
otuPmRxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRxDefectSecondsFEND.setStatus("current")
_OtuPmTxDefectSecondsFEND_Type = Integer32
_OtuPmTxDefectSecondsFEND_Object = MibTableColumn
otuPmTxDefectSecondsFEND = _OtuPmTxDefectSecondsFEND_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 25),
    _OtuPmTxDefectSecondsFEND_Type()
)
otuPmTxDefectSecondsFEND.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmTxDefectSecondsFEND.setStatus("current")
_OtuPmCorrectedBits_Type = HCPerfIntervalCount
_OtuPmCorrectedBits_Object = MibTableColumn
otuPmCorrectedBits = _OtuPmCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 26),
    _OtuPmCorrectedBits_Type()
)
otuPmCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmCorrectedBits.setStatus("current")
_OtuPmRxIAE_Type = Integer32
_OtuPmRxIAE_Object = MibTableColumn
otuPmRxIAE = _OtuPmRxIAE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 27),
    _OtuPmRxIAE_Type()
)
otuPmRxIAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRxIAE.setStatus("current")
_OtuPmTxIAE_Type = Integer32
_OtuPmTxIAE_Object = MibTableColumn
otuPmTxIAE = _OtuPmTxIAE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 28),
    _OtuPmTxIAE_Type()
)
otuPmTxIAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmTxIAE.setStatus("current")
_OtuPmRxBIAE_Type = Integer32
_OtuPmRxBIAE_Object = MibTableColumn
otuPmRxBIAE = _OtuPmRxBIAE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 29),
    _OtuPmRxBIAE_Type()
)
otuPmRxBIAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmRxBIAE.setStatus("current")
_OtuPmTxBIAE_Type = Integer32
_OtuPmTxBIAE_Object = MibTableColumn
otuPmTxBIAE = _OtuPmTxBIAE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 2, 1, 30),
    _OtuPmTxBIAE_Type()
)
otuPmTxBIAE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otuPmTxBIAE.setStatus("current")
_OtuPmConformance_ObjectIdentity = ObjectIdentity
otuPmConformance = _OtuPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 3)
)
_OtuPmCompliances_ObjectIdentity = ObjectIdentity
otuPmCompliances = _OtuPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 3, 1)
)
_OtuPmGroups_ObjectIdentity = ObjectIdentity
otuPmGroups = _OtuPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 3, 2)
)

# Managed Objects groups

otuPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 3, 2, 1)
)
otuPmGroup.setObjects(
      *(("INFINERA-PM-OTU-MIB", "otuPmTimestamp"),
        ("INFINERA-PM-OTU-MIB", "otuPmSampleDuration"),
        ("INFINERA-PM-OTU-MIB", "otuPmValidity"),
        ("INFINERA-PM-OTU-MIB", "otuPmNumberOfCodeWords"),
        ("INFINERA-PM-OTU-MIB", "otuPmNumberOfUncorrectedWords"),
        ("INFINERA-PM-OTU-MIB", "otuPmNumberOfCorrectedZeros"),
        ("INFINERA-PM-OTU-MIB", "otuPmNumberOfCorrectedOnes"),
        ("INFINERA-PM-OTU-MIB", "otuPmRxCVS"),
        ("INFINERA-PM-OTU-MIB", "otuPmTxCVS"),
        ("INFINERA-PM-OTU-MIB", "otuPmRxErroredBlocks"),
        ("INFINERA-PM-OTU-MIB", "otuPmTxErroredBlocks"),
        ("INFINERA-PM-OTU-MIB", "otuPmRxDefectSeconds"),
        ("INFINERA-PM-OTU-MIB", "otuPmTxDefectSeconds"),
        ("INFINERA-PM-OTU-MIB", "otuPmTribPRBSErr"),
        ("INFINERA-PM-OTU-MIB", "otuPmLinePRBSErr"),
        ("INFINERA-PM-OTU-MIB", "otuPmTribPRBSSyncErr"),
        ("INFINERA-PM-OTU-MIB", "otuPmLinePRBSSyncErr"),
        ("INFINERA-PM-OTU-MIB", "otuPmRxBeiCount"),
        ("INFINERA-PM-OTU-MIB", "otuPmTxBeiCount"),
        ("INFINERA-PM-OTU-MIB", "otuPmCircuitId"),
        ("INFINERA-PM-OTU-MIB", "otuPmPayloadType"),
        ("INFINERA-PM-OTU-MIB", "otuPmCorrectedBits"),
        ("INFINERA-PM-OTU-MIB", "otuPmRxIAE"),
        ("INFINERA-PM-OTU-MIB", "otuPmTxIAE"),
        ("INFINERA-PM-OTU-MIB", "otuPmRxBIAE"),
        ("INFINERA-PM-OTU-MIB", "otuPmTxBIAE"))
)
if mibBuilder.loadTexts:
    otuPmGroup.setStatus("current")

otuPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 3, 2, 2)
)
otuPmRealGroup.setObjects(
      *(("INFINERA-PM-OTU-MIB", "otuPmRealNumberOfCodeWords"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealNumberOfUncorrectedWords"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealNumberOfCorrectedZeros"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealNumberOfCorrectedOnes"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealRxCVS"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealTxCVS"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealRxErroredBlocks"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealTxErroredBlocks"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealRxCVS"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealTxCVS"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealRxDefectSeconds"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealTxDefectSeconds"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealTribPRBSErr"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealLinePRBSErr"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealTribPRBSSyncErr"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealLinePRBSSyncErr"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealRxBeiCount"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealTxBeiCount"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealCorrectedBits"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealRxIAE"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealTxIAE"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealRxBIAE"),
        ("INFINERA-PM-OTU-MIB", "otuPmRealTxBIAE"))
)
if mibBuilder.loadTexts:
    otuPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otuPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 3, 1, 1)
)
otuPmCompliance.setObjects(
    ("INFINERA-PM-OTU-MIB", "otuPmGroup")
)
if mibBuilder.loadTexts:
    otuPmCompliance.setStatus(
        "current"
    )

otuPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 22, 3, 1, 2)
)
otuPmRealCompliance.setObjects(
    ("INFINERA-PM-OTU-MIB", "otuPmRealGroup")
)
if mibBuilder.loadTexts:
    otuPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-OTU-MIB",
    **{"otuPmMIB": otuPmMIB,
       "otuPmRealTable": otuPmRealTable,
       "otuPmRealEntry": otuPmRealEntry,
       "otuPmRealNumberOfCodeWords": otuPmRealNumberOfCodeWords,
       "otuPmRealNumberOfUncorrectedWords": otuPmRealNumberOfUncorrectedWords,
       "otuPmRealNumberOfCorrectedZeros": otuPmRealNumberOfCorrectedZeros,
       "otuPmRealNumberOfCorrectedOnes": otuPmRealNumberOfCorrectedOnes,
       "otuPmRealRxCVS": otuPmRealRxCVS,
       "otuPmRealTxCVS": otuPmRealTxCVS,
       "otuPmRealRxErroredBlocks": otuPmRealRxErroredBlocks,
       "otuPmRealTxErroredBlocks": otuPmRealTxErroredBlocks,
       "otuPmRealRxDefectSeconds": otuPmRealRxDefectSeconds,
       "otuPmRealTxDefectSeconds": otuPmRealTxDefectSeconds,
       "otuPmRealTribPRBSErr": otuPmRealTribPRBSErr,
       "otuPmRealLinePRBSErr": otuPmRealLinePRBSErr,
       "otuPmRealTribPRBSSyncErr": otuPmRealTribPRBSSyncErr,
       "otuPmRealLinePRBSSyncErr": otuPmRealLinePRBSSyncErr,
       "otuPmRealRxBeiCount": otuPmRealRxBeiCount,
       "otuPmRealTxBeiCount": otuPmRealTxBeiCount,
       "otuPmRealRxErroredBlocksFEND": otuPmRealRxErroredBlocksFEND,
       "otuPmRealTxErroredBlocksFEND": otuPmRealTxErroredBlocksFEND,
       "otuPmRealRxDefectSecondsFEND": otuPmRealRxDefectSecondsFEND,
       "otuPmRealTxDefectSecondsFEND": otuPmRealTxDefectSecondsFEND,
       "otuPmRealCorrectedBits": otuPmRealCorrectedBits,
       "otuPmRealRxIAE": otuPmRealRxIAE,
       "otuPmRealTxIAE": otuPmRealTxIAE,
       "otuPmRealRxBIAE": otuPmRealRxBIAE,
       "otuPmRealTxBIAE": otuPmRealTxBIAE,
       "otuPmTable": otuPmTable,
       "otuPmEntry": otuPmEntry,
       "otuPmTimestamp": otuPmTimestamp,
       "otuPmSampleDuration": otuPmSampleDuration,
       "otuPmValidity": otuPmValidity,
       "otuPmNumberOfCodeWords": otuPmNumberOfCodeWords,
       "otuPmNumberOfUncorrectedWords": otuPmNumberOfUncorrectedWords,
       "otuPmNumberOfCorrectedZeros": otuPmNumberOfCorrectedZeros,
       "otuPmNumberOfCorrectedOnes": otuPmNumberOfCorrectedOnes,
       "otuPmRxCVS": otuPmRxCVS,
       "otuPmTxCVS": otuPmTxCVS,
       "otuPmRxErroredBlocks": otuPmRxErroredBlocks,
       "otuPmTxErroredBlocks": otuPmTxErroredBlocks,
       "otuPmRxDefectSeconds": otuPmRxDefectSeconds,
       "otuPmTxDefectSeconds": otuPmTxDefectSeconds,
       "otuPmTribPRBSErr": otuPmTribPRBSErr,
       "otuPmLinePRBSErr": otuPmLinePRBSErr,
       "otuPmTribPRBSSyncErr": otuPmTribPRBSSyncErr,
       "otuPmLinePRBSSyncErr": otuPmLinePRBSSyncErr,
       "otuPmRxBeiCount": otuPmRxBeiCount,
       "otuPmTxBeiCount": otuPmTxBeiCount,
       "otuPmCircuitId": otuPmCircuitId,
       "otuPmPayloadType": otuPmPayloadType,
       "otuPmRxErroredBlocksFEND": otuPmRxErroredBlocksFEND,
       "otuPmTxErroredBlocksFEND": otuPmTxErroredBlocksFEND,
       "otuPmRxDefectSecondsFEND": otuPmRxDefectSecondsFEND,
       "otuPmTxDefectSecondsFEND": otuPmTxDefectSecondsFEND,
       "otuPmCorrectedBits": otuPmCorrectedBits,
       "otuPmRxIAE": otuPmRxIAE,
       "otuPmTxIAE": otuPmTxIAE,
       "otuPmRxBIAE": otuPmRxBIAE,
       "otuPmTxBIAE": otuPmTxBIAE,
       "otuPmConformance": otuPmConformance,
       "otuPmCompliances": otuPmCompliances,
       "otuPmCompliance": otuPmCompliance,
       "otuPmRealCompliance": otuPmRealCompliance,
       "otuPmGroups": otuPmGroups,
       "otuPmGroup": otuPmGroup,
       "otuPmRealGroup": otuPmRealGroup}
)
