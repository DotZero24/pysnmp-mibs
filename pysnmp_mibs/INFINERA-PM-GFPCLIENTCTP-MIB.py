# SNMP MIB module (INFINERA-PM-GFPCLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-GFPCLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:54 2025
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
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
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

gfpClientCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28)
)
if mibBuilder.loadTexts:
    gfpClientCtpPmMIB.setRevisions(
        ("2011-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GfpClientCtpPmRealTable_Object = MibTable
gfpClientCtpPmRealTable = _GfpClientCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1)
)
if mibBuilder.loadTexts:
    gfpClientCtpPmRealTable.setStatus("current")
_GfpClientCtpPmRealEntry_Object = MibTableRow
gfpClientCtpPmRealEntry = _GfpClientCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1)
)
gfpClientCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gfpClientCtpPmRealEntry.setStatus("current")
_GfpClientCtpPmRealDataFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmRealDataFrames_Object = MibTableColumn
gfpClientCtpPmRealDataFrames = _GfpClientCtpPmRealDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 1),
    _GfpClientCtpPmRealDataFrames_Type()
)
gfpClientCtpPmRealDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealDataFrames.setStatus("current")
_GfpClientCtpPmRealMgmtFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmRealMgmtFrames_Object = MibTableColumn
gfpClientCtpPmRealMgmtFrames = _GfpClientCtpPmRealMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 2),
    _GfpClientCtpPmRealMgmtFrames_Type()
)
gfpClientCtpPmRealMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealMgmtFrames.setStatus("current")
_GfpClientCtpPmRealIdleFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmRealIdleFrames_Object = MibTableColumn
gfpClientCtpPmRealIdleFrames = _GfpClientCtpPmRealIdleFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 3),
    _GfpClientCtpPmRealIdleFrames_Type()
)
gfpClientCtpPmRealIdleFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealIdleFrames.setStatus("current")
_GfpClientCtpPmRealOtherFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmRealOtherFrames_Object = MibTableColumn
gfpClientCtpPmRealOtherFrames = _GfpClientCtpPmRealOtherFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 4),
    _GfpClientCtpPmRealOtherFrames_Type()
)
gfpClientCtpPmRealOtherFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealOtherFrames.setStatus("current")
_GfpClientCtpPmRealFCSFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmRealFCSFrames_Object = MibTableColumn
gfpClientCtpPmRealFCSFrames = _GfpClientCtpPmRealFCSFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 5),
    _GfpClientCtpPmRealFCSFrames_Type()
)
gfpClientCtpPmRealFCSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealFCSFrames.setStatus("current")
_GfpClientCtpPmRealErrFCSFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmRealErrFCSFrames_Object = MibTableColumn
gfpClientCtpPmRealErrFCSFrames = _GfpClientCtpPmRealErrFCSFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 6),
    _GfpClientCtpPmRealErrFCSFrames_Type()
)
gfpClientCtpPmRealErrFCSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealErrFCSFrames.setStatus("current")
_GfpClientCtpPmRealLinearEXIFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmRealLinearEXIFrames_Object = MibTableColumn
gfpClientCtpPmRealLinearEXIFrames = _GfpClientCtpPmRealLinearEXIFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 7),
    _GfpClientCtpPmRealLinearEXIFrames_Type()
)
gfpClientCtpPmRealLinearEXIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealLinearEXIFrames.setStatus("current")
_GfpClientCtpPmRealNullEXIFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmRealNullEXIFrames_Object = MibTableColumn
gfpClientCtpPmRealNullEXIFrames = _GfpClientCtpPmRealNullEXIFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 8),
    _GfpClientCtpPmRealNullEXIFrames_Type()
)
gfpClientCtpPmRealNullEXIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealNullEXIFrames.setStatus("current")
_GfpClientCtpPmRealSBitCHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmRealSBitCHECErrors_Object = MibTableColumn
gfpClientCtpPmRealSBitCHECErrors = _GfpClientCtpPmRealSBitCHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 9),
    _GfpClientCtpPmRealSBitCHECErrors_Type()
)
gfpClientCtpPmRealSBitCHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealSBitCHECErrors.setStatus("current")
_GfpClientCtpPmRealMBitCHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmRealMBitCHECErrors_Object = MibTableColumn
gfpClientCtpPmRealMBitCHECErrors = _GfpClientCtpPmRealMBitCHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 10),
    _GfpClientCtpPmRealMBitCHECErrors_Type()
)
gfpClientCtpPmRealMBitCHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealMBitCHECErrors.setStatus("current")
_GfpClientCtpPmRealSBitTHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmRealSBitTHECErrors_Object = MibTableColumn
gfpClientCtpPmRealSBitTHECErrors = _GfpClientCtpPmRealSBitTHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 11),
    _GfpClientCtpPmRealSBitTHECErrors_Type()
)
gfpClientCtpPmRealSBitTHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealSBitTHECErrors.setStatus("current")
_GfpClientCtpPmRealMBitTHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmRealMBitTHECErrors_Object = MibTableColumn
gfpClientCtpPmRealMBitTHECErrors = _GfpClientCtpPmRealMBitTHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 12),
    _GfpClientCtpPmRealMBitTHECErrors_Type()
)
gfpClientCtpPmRealMBitTHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealMBitTHECErrors.setStatus("current")
_GfpClientCtpPmRealSBitEHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmRealSBitEHECErrors_Object = MibTableColumn
gfpClientCtpPmRealSBitEHECErrors = _GfpClientCtpPmRealSBitEHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 13),
    _GfpClientCtpPmRealSBitEHECErrors_Type()
)
gfpClientCtpPmRealSBitEHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealSBitEHECErrors.setStatus("current")
_GfpClientCtpPmRealMBitEHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmRealMBitEHECErrors_Object = MibTableColumn
gfpClientCtpPmRealMBitEHECErrors = _GfpClientCtpPmRealMBitEHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 14),
    _GfpClientCtpPmRealMBitEHECErrors_Type()
)
gfpClientCtpPmRealMBitEHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealMBitEHECErrors.setStatus("current")
_GfpClientCtpPmRealEXIInvalid_Type = HCPerfIntervalCount
_GfpClientCtpPmRealEXIInvalid_Object = MibTableColumn
gfpClientCtpPmRealEXIInvalid = _GfpClientCtpPmRealEXIInvalid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 15),
    _GfpClientCtpPmRealEXIInvalid_Type()
)
gfpClientCtpPmRealEXIInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealEXIInvalid.setStatus("current")
_GfpClientCtpPmRealUPIInvalid_Type = HCPerfIntervalCount
_GfpClientCtpPmRealUPIInvalid_Object = MibTableColumn
gfpClientCtpPmRealUPIInvalid = _GfpClientCtpPmRealUPIInvalid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 16),
    _GfpClientCtpPmRealUPIInvalid_Type()
)
gfpClientCtpPmRealUPIInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealUPIInvalid.setStatus("current")
_GfpClientCtpPmRealCSFRaised_Type = HCPerfIntervalCount
_GfpClientCtpPmRealCSFRaised_Object = MibTableColumn
gfpClientCtpPmRealCSFRaised = _GfpClientCtpPmRealCSFRaised_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 17),
    _GfpClientCtpPmRealCSFRaised_Type()
)
gfpClientCtpPmRealCSFRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealCSFRaised.setStatus("current")
_GfpClientCtpPmRealOversized_Type = HCPerfIntervalCount
_GfpClientCtpPmRealOversized_Object = MibTableColumn
gfpClientCtpPmRealOversized = _GfpClientCtpPmRealOversized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 18),
    _GfpClientCtpPmRealOversized_Type()
)
gfpClientCtpPmRealOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealOversized.setStatus("current")
_GfpClientCtpPmRealUndersized_Type = HCPerfIntervalCount
_GfpClientCtpPmRealUndersized_Object = MibTableColumn
gfpClientCtpPmRealUndersized = _GfpClientCtpPmRealUndersized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 19),
    _GfpClientCtpPmRealUndersized_Type()
)
gfpClientCtpPmRealUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealUndersized.setStatus("current")
_GfpClientCtpPmRealIngressOverflow_Type = HCPerfIntervalCount
_GfpClientCtpPmRealIngressOverflow_Object = MibTableColumn
gfpClientCtpPmRealIngressOverflow = _GfpClientCtpPmRealIngressOverflow_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 20),
    _GfpClientCtpPmRealIngressOverflow_Type()
)
gfpClientCtpPmRealIngressOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealIngressOverflow.setStatus("current")
_GfpClientCtpPmRealRxEgressOverflow_Type = HCPerfIntervalCount
_GfpClientCtpPmRealRxEgressOverflow_Object = MibTableColumn
gfpClientCtpPmRealRxEgressOverflow = _GfpClientCtpPmRealRxEgressOverflow_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 1, 1, 21),
    _GfpClientCtpPmRealRxEgressOverflow_Type()
)
gfpClientCtpPmRealRxEgressOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRealRxEgressOverflow.setStatus("current")
_GfpClientCtpPmTable_Object = MibTable
gfpClientCtpPmTable = _GfpClientCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2)
)
if mibBuilder.loadTexts:
    gfpClientCtpPmTable.setStatus("current")
_GfpClientCtpPmEntry_Object = MibTableRow
gfpClientCtpPmEntry = _GfpClientCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1)
)
gfpClientCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmSampleDuration"),
    (0, "INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    gfpClientCtpPmEntry.setStatus("current")


class _GfpClientCtpPmTimestamp_Type(Integer32):
    """Custom type gfpClientCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GfpClientCtpPmTimestamp_Type.__name__ = "Integer32"
_GfpClientCtpPmTimestamp_Object = MibTableColumn
gfpClientCtpPmTimestamp = _GfpClientCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 1),
    _GfpClientCtpPmTimestamp_Type()
)
gfpClientCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gfpClientCtpPmTimestamp.setStatus("current")


class _GfpClientCtpPmSampleDuration_Type(Integer32):
    """Custom type gfpClientCtpPmSampleDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fifteenMinutes", 1),
          ("day", 2))
    )


_GfpClientCtpPmSampleDuration_Type.__name__ = "Integer32"
_GfpClientCtpPmSampleDuration_Object = MibTableColumn
gfpClientCtpPmSampleDuration = _GfpClientCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 2),
    _GfpClientCtpPmSampleDuration_Type()
)
gfpClientCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gfpClientCtpPmSampleDuration.setStatus("current")
_GfpClientCtpPmDataFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmDataFrames_Object = MibTableColumn
gfpClientCtpPmDataFrames = _GfpClientCtpPmDataFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 3),
    _GfpClientCtpPmDataFrames_Type()
)
gfpClientCtpPmDataFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmDataFrames.setStatus("current")
_GfpClientCtpPmMgmtFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmMgmtFrames_Object = MibTableColumn
gfpClientCtpPmMgmtFrames = _GfpClientCtpPmMgmtFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 4),
    _GfpClientCtpPmMgmtFrames_Type()
)
gfpClientCtpPmMgmtFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmMgmtFrames.setStatus("current")
_GfpClientCtpPmIdleFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmIdleFrames_Object = MibTableColumn
gfpClientCtpPmIdleFrames = _GfpClientCtpPmIdleFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 5),
    _GfpClientCtpPmIdleFrames_Type()
)
gfpClientCtpPmIdleFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmIdleFrames.setStatus("current")
_GfpClientCtpPmOtherFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmOtherFrames_Object = MibTableColumn
gfpClientCtpPmOtherFrames = _GfpClientCtpPmOtherFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 6),
    _GfpClientCtpPmOtherFrames_Type()
)
gfpClientCtpPmOtherFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmOtherFrames.setStatus("current")
_GfpClientCtpPmFCSFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmFCSFrames_Object = MibTableColumn
gfpClientCtpPmFCSFrames = _GfpClientCtpPmFCSFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 7),
    _GfpClientCtpPmFCSFrames_Type()
)
gfpClientCtpPmFCSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmFCSFrames.setStatus("current")
_GfpClientCtpPmErrFCSFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmErrFCSFrames_Object = MibTableColumn
gfpClientCtpPmErrFCSFrames = _GfpClientCtpPmErrFCSFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 8),
    _GfpClientCtpPmErrFCSFrames_Type()
)
gfpClientCtpPmErrFCSFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmErrFCSFrames.setStatus("current")
_GfpClientCtpPmLinearEXIFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmLinearEXIFrames_Object = MibTableColumn
gfpClientCtpPmLinearEXIFrames = _GfpClientCtpPmLinearEXIFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 9),
    _GfpClientCtpPmLinearEXIFrames_Type()
)
gfpClientCtpPmLinearEXIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmLinearEXIFrames.setStatus("current")
_GfpClientCtpPmNullEXIFrames_Type = HCPerfIntervalCount
_GfpClientCtpPmNullEXIFrames_Object = MibTableColumn
gfpClientCtpPmNullEXIFrames = _GfpClientCtpPmNullEXIFrames_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 10),
    _GfpClientCtpPmNullEXIFrames_Type()
)
gfpClientCtpPmNullEXIFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmNullEXIFrames.setStatus("current")
_GfpClientCtpPmSBitCHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmSBitCHECErrors_Object = MibTableColumn
gfpClientCtpPmSBitCHECErrors = _GfpClientCtpPmSBitCHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 11),
    _GfpClientCtpPmSBitCHECErrors_Type()
)
gfpClientCtpPmSBitCHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmSBitCHECErrors.setStatus("current")
_GfpClientCtpPmMBitCHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmMBitCHECErrors_Object = MibTableColumn
gfpClientCtpPmMBitCHECErrors = _GfpClientCtpPmMBitCHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 12),
    _GfpClientCtpPmMBitCHECErrors_Type()
)
gfpClientCtpPmMBitCHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmMBitCHECErrors.setStatus("current")
_GfpClientCtpPmSBitTHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmSBitTHECErrors_Object = MibTableColumn
gfpClientCtpPmSBitTHECErrors = _GfpClientCtpPmSBitTHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 13),
    _GfpClientCtpPmSBitTHECErrors_Type()
)
gfpClientCtpPmSBitTHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmSBitTHECErrors.setStatus("current")
_GfpClientCtpPmMBitTHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmMBitTHECErrors_Object = MibTableColumn
gfpClientCtpPmMBitTHECErrors = _GfpClientCtpPmMBitTHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 14),
    _GfpClientCtpPmMBitTHECErrors_Type()
)
gfpClientCtpPmMBitTHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmMBitTHECErrors.setStatus("current")
_GfpClientCtpPmSBitEHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmSBitEHECErrors_Object = MibTableColumn
gfpClientCtpPmSBitEHECErrors = _GfpClientCtpPmSBitEHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 15),
    _GfpClientCtpPmSBitEHECErrors_Type()
)
gfpClientCtpPmSBitEHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmSBitEHECErrors.setStatus("current")
_GfpClientCtpPmMBitEHECErrors_Type = HCPerfIntervalCount
_GfpClientCtpPmMBitEHECErrors_Object = MibTableColumn
gfpClientCtpPmMBitEHECErrors = _GfpClientCtpPmMBitEHECErrors_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 16),
    _GfpClientCtpPmMBitEHECErrors_Type()
)
gfpClientCtpPmMBitEHECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmMBitEHECErrors.setStatus("current")
_GfpClientCtpPmEXIInvalid_Type = HCPerfIntervalCount
_GfpClientCtpPmEXIInvalid_Object = MibTableColumn
gfpClientCtpPmEXIInvalid = _GfpClientCtpPmEXIInvalid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 17),
    _GfpClientCtpPmEXIInvalid_Type()
)
gfpClientCtpPmEXIInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmEXIInvalid.setStatus("current")
_GfpClientCtpPmUPIInvalid_Type = HCPerfIntervalCount
_GfpClientCtpPmUPIInvalid_Object = MibTableColumn
gfpClientCtpPmUPIInvalid = _GfpClientCtpPmUPIInvalid_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 18),
    _GfpClientCtpPmUPIInvalid_Type()
)
gfpClientCtpPmUPIInvalid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmUPIInvalid.setStatus("current")
_GfpClientCtpPmCSFRaised_Type = HCPerfIntervalCount
_GfpClientCtpPmCSFRaised_Object = MibTableColumn
gfpClientCtpPmCSFRaised = _GfpClientCtpPmCSFRaised_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 19),
    _GfpClientCtpPmCSFRaised_Type()
)
gfpClientCtpPmCSFRaised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmCSFRaised.setStatus("current")
_GfpClientCtpPmOversized_Type = HCPerfIntervalCount
_GfpClientCtpPmOversized_Object = MibTableColumn
gfpClientCtpPmOversized = _GfpClientCtpPmOversized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 20),
    _GfpClientCtpPmOversized_Type()
)
gfpClientCtpPmOversized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmOversized.setStatus("current")
_GfpClientCtpPmUndersized_Type = HCPerfIntervalCount
_GfpClientCtpPmUndersized_Object = MibTableColumn
gfpClientCtpPmUndersized = _GfpClientCtpPmUndersized_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 21),
    _GfpClientCtpPmUndersized_Type()
)
gfpClientCtpPmUndersized.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmUndersized.setStatus("current")
_GfpClientCtpPmIngressOverflow_Type = HCPerfIntervalCount
_GfpClientCtpPmIngressOverflow_Object = MibTableColumn
gfpClientCtpPmIngressOverflow = _GfpClientCtpPmIngressOverflow_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 22),
    _GfpClientCtpPmIngressOverflow_Type()
)
gfpClientCtpPmIngressOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmIngressOverflow.setStatus("current")
_GfpClientCtpPmRxEgressOverflow_Type = HCPerfIntervalCount
_GfpClientCtpPmRxEgressOverflow_Object = MibTableColumn
gfpClientCtpPmRxEgressOverflow = _GfpClientCtpPmRxEgressOverflow_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 2, 1, 23),
    _GfpClientCtpPmRxEgressOverflow_Type()
)
gfpClientCtpPmRxEgressOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gfpClientCtpPmRxEgressOverflow.setStatus("current")
_GfpClientCtpPmConformance_ObjectIdentity = ObjectIdentity
gfpClientCtpPmConformance = _GfpClientCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 3)
)
_GfpClientCtpPmCompliances_ObjectIdentity = ObjectIdentity
gfpClientCtpPmCompliances = _GfpClientCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 3, 1)
)
_GfpClientCtpPmGroups_ObjectIdentity = ObjectIdentity
gfpClientCtpPmGroups = _GfpClientCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 3, 2)
)

# Managed Objects groups

gfpClientCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 3, 2, 1)
)
gfpClientCtpPmGroup.setObjects(
      *(("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmTimestamp"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmSampleDuration"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmDataFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmMgmtFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmIdleFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmOtherFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmFCSFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmErrFCSFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmLinearEXIFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmNullEXIFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmSBitCHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmMBitCHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmSBitTHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmMBitTHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmSBitEHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmMBitEHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmEXIInvalid"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmUPIInvalid"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmCSFRaised"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmOversized"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmUndersized"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmIngressOverflow"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRxEgressOverflow"))
)
if mibBuilder.loadTexts:
    gfpClientCtpPmGroup.setStatus("current")

gfpClientCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 3, 2, 2)
)
gfpClientCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealDataFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealMgmtFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealIdleFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealOtherFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealFCSFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealErrFCSFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealLinearEXIFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealNullEXIFrames"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealSBitCHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealMBitCHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealSBitTHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealMBitTHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealSBitEHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealMBitEHECErrors"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealEXIInvalid"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealUPIInvalid"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealCSFRaised"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealOversized"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealUndersized"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealIngressOverflow"),
        ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealRxEgressOverflow"))
)
if mibBuilder.loadTexts:
    gfpClientCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gfpClientCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 3, 1, 1)
)
gfpClientCtpPmCompliance.setObjects(
    ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmGroup")
)
if mibBuilder.loadTexts:
    gfpClientCtpPmCompliance.setStatus(
        "current"
    )

gfpClientCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 28, 3, 1, 2)
)
gfpClientCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-GFPCLIENTCTP-MIB", "gfpClientCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    gfpClientCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-GFPCLIENTCTP-MIB",
    **{"gfpClientCtpPmMIB": gfpClientCtpPmMIB,
       "gfpClientCtpPmRealTable": gfpClientCtpPmRealTable,
       "gfpClientCtpPmRealEntry": gfpClientCtpPmRealEntry,
       "gfpClientCtpPmRealDataFrames": gfpClientCtpPmRealDataFrames,
       "gfpClientCtpPmRealMgmtFrames": gfpClientCtpPmRealMgmtFrames,
       "gfpClientCtpPmRealIdleFrames": gfpClientCtpPmRealIdleFrames,
       "gfpClientCtpPmRealOtherFrames": gfpClientCtpPmRealOtherFrames,
       "gfpClientCtpPmRealFCSFrames": gfpClientCtpPmRealFCSFrames,
       "gfpClientCtpPmRealErrFCSFrames": gfpClientCtpPmRealErrFCSFrames,
       "gfpClientCtpPmRealLinearEXIFrames": gfpClientCtpPmRealLinearEXIFrames,
       "gfpClientCtpPmRealNullEXIFrames": gfpClientCtpPmRealNullEXIFrames,
       "gfpClientCtpPmRealSBitCHECErrors": gfpClientCtpPmRealSBitCHECErrors,
       "gfpClientCtpPmRealMBitCHECErrors": gfpClientCtpPmRealMBitCHECErrors,
       "gfpClientCtpPmRealSBitTHECErrors": gfpClientCtpPmRealSBitTHECErrors,
       "gfpClientCtpPmRealMBitTHECErrors": gfpClientCtpPmRealMBitTHECErrors,
       "gfpClientCtpPmRealSBitEHECErrors": gfpClientCtpPmRealSBitEHECErrors,
       "gfpClientCtpPmRealMBitEHECErrors": gfpClientCtpPmRealMBitEHECErrors,
       "gfpClientCtpPmRealEXIInvalid": gfpClientCtpPmRealEXIInvalid,
       "gfpClientCtpPmRealUPIInvalid": gfpClientCtpPmRealUPIInvalid,
       "gfpClientCtpPmRealCSFRaised": gfpClientCtpPmRealCSFRaised,
       "gfpClientCtpPmRealOversized": gfpClientCtpPmRealOversized,
       "gfpClientCtpPmRealUndersized": gfpClientCtpPmRealUndersized,
       "gfpClientCtpPmRealIngressOverflow": gfpClientCtpPmRealIngressOverflow,
       "gfpClientCtpPmRealRxEgressOverflow": gfpClientCtpPmRealRxEgressOverflow,
       "gfpClientCtpPmTable": gfpClientCtpPmTable,
       "gfpClientCtpPmEntry": gfpClientCtpPmEntry,
       "gfpClientCtpPmTimestamp": gfpClientCtpPmTimestamp,
       "gfpClientCtpPmSampleDuration": gfpClientCtpPmSampleDuration,
       "gfpClientCtpPmDataFrames": gfpClientCtpPmDataFrames,
       "gfpClientCtpPmMgmtFrames": gfpClientCtpPmMgmtFrames,
       "gfpClientCtpPmIdleFrames": gfpClientCtpPmIdleFrames,
       "gfpClientCtpPmOtherFrames": gfpClientCtpPmOtherFrames,
       "gfpClientCtpPmFCSFrames": gfpClientCtpPmFCSFrames,
       "gfpClientCtpPmErrFCSFrames": gfpClientCtpPmErrFCSFrames,
       "gfpClientCtpPmLinearEXIFrames": gfpClientCtpPmLinearEXIFrames,
       "gfpClientCtpPmNullEXIFrames": gfpClientCtpPmNullEXIFrames,
       "gfpClientCtpPmSBitCHECErrors": gfpClientCtpPmSBitCHECErrors,
       "gfpClientCtpPmMBitCHECErrors": gfpClientCtpPmMBitCHECErrors,
       "gfpClientCtpPmSBitTHECErrors": gfpClientCtpPmSBitTHECErrors,
       "gfpClientCtpPmMBitTHECErrors": gfpClientCtpPmMBitTHECErrors,
       "gfpClientCtpPmSBitEHECErrors": gfpClientCtpPmSBitEHECErrors,
       "gfpClientCtpPmMBitEHECErrors": gfpClientCtpPmMBitEHECErrors,
       "gfpClientCtpPmEXIInvalid": gfpClientCtpPmEXIInvalid,
       "gfpClientCtpPmUPIInvalid": gfpClientCtpPmUPIInvalid,
       "gfpClientCtpPmCSFRaised": gfpClientCtpPmCSFRaised,
       "gfpClientCtpPmOversized": gfpClientCtpPmOversized,
       "gfpClientCtpPmUndersized": gfpClientCtpPmUndersized,
       "gfpClientCtpPmIngressOverflow": gfpClientCtpPmIngressOverflow,
       "gfpClientCtpPmRxEgressOverflow": gfpClientCtpPmRxEgressOverflow,
       "gfpClientCtpPmConformance": gfpClientCtpPmConformance,
       "gfpClientCtpPmCompliances": gfpClientCtpPmCompliances,
       "gfpClientCtpPmCompliance": gfpClientCtpPmCompliance,
       "gfpClientCtpPmRealCompliance": gfpClientCtpPmRealCompliance,
       "gfpClientCtpPmGroups": gfpClientCtpPmGroups,
       "gfpClientCtpPmGroup": gfpClientCtpPmGroup,
       "gfpClientCtpPmRealGroup": gfpClientCtpPmRealGroup}
)
