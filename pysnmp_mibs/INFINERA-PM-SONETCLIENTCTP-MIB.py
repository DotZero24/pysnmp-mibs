# SNMP MIB module (INFINERA-PM-SONETCLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-SONETCLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:15 2025
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

(commonPerfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "commonPerfMon")

(FloatArbitraryPrecision,
 FloatHundredths,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
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

sonetClientCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2)
)
if mibBuilder.loadTexts:
    sonetClientCtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SonetClientCtpPmRealTable_Object = MibTable
sonetClientCtpPmRealTable = _SonetClientCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1)
)
if mibBuilder.loadTexts:
    sonetClientCtpPmRealTable.setStatus("current")
_SonetClientCtpPmRealEntry_Object = MibTableRow
sonetClientCtpPmRealEntry = _SonetClientCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1)
)
sonetClientCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sonetClientCtpPmRealEntry.setStatus("current")
_SonetClientCtpPmRealRxCV_Type = Counter64
_SonetClientCtpPmRealRxCV_Object = MibTableColumn
sonetClientCtpPmRealRxCV = _SonetClientCtpPmRealRxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 1),
    _SonetClientCtpPmRealRxCV_Type()
)
sonetClientCtpPmRealRxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealRxCV.setStatus("current")
_SonetClientCtpPmRealRxES_Type = Integer32
_SonetClientCtpPmRealRxES_Object = MibTableColumn
sonetClientCtpPmRealRxES = _SonetClientCtpPmRealRxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 2),
    _SonetClientCtpPmRealRxES_Type()
)
sonetClientCtpPmRealRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealRxES.setStatus("current")
_SonetClientCtpPmRealRxSES_Type = Integer32
_SonetClientCtpPmRealRxSES_Object = MibTableColumn
sonetClientCtpPmRealRxSES = _SonetClientCtpPmRealRxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 3),
    _SonetClientCtpPmRealRxSES_Type()
)
sonetClientCtpPmRealRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealRxSES.setStatus("current")
_SonetClientCtpPmRealRxSEFS_Type = Integer32
_SonetClientCtpPmRealRxSEFS_Object = MibTableColumn
sonetClientCtpPmRealRxSEFS = _SonetClientCtpPmRealRxSEFS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 4),
    _SonetClientCtpPmRealRxSEFS_Type()
)
sonetClientCtpPmRealRxSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealRxSEFS.setStatus("current")
_SonetClientCtpPmRealTxCV_Type = Counter64
_SonetClientCtpPmRealTxCV_Object = MibTableColumn
sonetClientCtpPmRealTxCV = _SonetClientCtpPmRealTxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 5),
    _SonetClientCtpPmRealTxCV_Type()
)
sonetClientCtpPmRealTxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealTxCV.setStatus("current")
_SonetClientCtpPmRealTxES_Type = Integer32
_SonetClientCtpPmRealTxES_Object = MibTableColumn
sonetClientCtpPmRealTxES = _SonetClientCtpPmRealTxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 6),
    _SonetClientCtpPmRealTxES_Type()
)
sonetClientCtpPmRealTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealTxES.setStatus("current")
_SonetClientCtpPmRealTxSES_Type = Integer32
_SonetClientCtpPmRealTxSES_Object = MibTableColumn
sonetClientCtpPmRealTxSES = _SonetClientCtpPmRealTxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 7),
    _SonetClientCtpPmRealTxSES_Type()
)
sonetClientCtpPmRealTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealTxSES.setStatus("current")
_SonetClientCtpPmRealTxSEFS_Type = Integer32
_SonetClientCtpPmRealTxSEFS_Object = MibTableColumn
sonetClientCtpPmRealTxSEFS = _SonetClientCtpPmRealTxSEFS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 8),
    _SonetClientCtpPmRealTxSEFS_Type()
)
sonetClientCtpPmRealTxSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealTxSEFS.setStatus("current")
_SonetClientCtpPmRealCktId_Type = DisplayString
_SonetClientCtpPmRealCktId_Object = MibTableColumn
sonetClientCtpPmRealCktId = _SonetClientCtpPmRealCktId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 9),
    _SonetClientCtpPmRealCktId_Type()
)
sonetClientCtpPmRealCktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealCktId.setStatus("current")
_SonetClientCtpPmRealTribPRBSSyncErr_Type = Integer32
_SonetClientCtpPmRealTribPRBSSyncErr_Object = MibTableColumn
sonetClientCtpPmRealTribPRBSSyncErr = _SonetClientCtpPmRealTribPRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 10),
    _SonetClientCtpPmRealTribPRBSSyncErr_Type()
)
sonetClientCtpPmRealTribPRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealTribPRBSSyncErr.setStatus("current")
_SonetClientCtpPmRealTribPRBSErr_Type = HCPerfIntervalCount
_SonetClientCtpPmRealTribPRBSErr_Object = MibTableColumn
sonetClientCtpPmRealTribPRBSErr = _SonetClientCtpPmRealTribPRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 11),
    _SonetClientCtpPmRealTribPRBSErr_Type()
)
sonetClientCtpPmRealTribPRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealTribPRBSErr.setStatus("current")
_SonetClientCtpPmRealLinePRBSSyncErr_Type = Integer32
_SonetClientCtpPmRealLinePRBSSyncErr_Object = MibTableColumn
sonetClientCtpPmRealLinePRBSSyncErr = _SonetClientCtpPmRealLinePRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 12),
    _SonetClientCtpPmRealLinePRBSSyncErr_Type()
)
sonetClientCtpPmRealLinePRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealLinePRBSSyncErr.setStatus("current")
_SonetClientCtpPmRealLinePRBSErr_Type = HCPerfIntervalCount
_SonetClientCtpPmRealLinePRBSErr_Object = MibTableColumn
sonetClientCtpPmRealLinePRBSErr = _SonetClientCtpPmRealLinePRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 13),
    _SonetClientCtpPmRealLinePRBSErr_Type()
)
sonetClientCtpPmRealLinePRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealLinePRBSErr.setStatus("current")
_SonetClientCtpPmRealRxBER_Type = FloatArbitraryPrecision
_SonetClientCtpPmRealRxBER_Object = MibTableColumn
sonetClientCtpPmRealRxBER = _SonetClientCtpPmRealRxBER_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 14),
    _SonetClientCtpPmRealRxBER_Type()
)
sonetClientCtpPmRealRxBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealRxBER.setStatus("current")
_SonetClientCtpPmRealTxBER_Type = FloatArbitraryPrecision
_SonetClientCtpPmRealTxBER_Object = MibTableColumn
sonetClientCtpPmRealTxBER = _SonetClientCtpPmRealTxBER_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 1, 1, 15),
    _SonetClientCtpPmRealTxBER_Type()
)
sonetClientCtpPmRealTxBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRealTxBER.setStatus("current")
_SonetClientCtpPmTable_Object = MibTable
sonetClientCtpPmTable = _SonetClientCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2)
)
if mibBuilder.loadTexts:
    sonetClientCtpPmTable.setStatus("current")
_SonetClientCtpPmEntry_Object = MibTableRow
sonetClientCtpPmEntry = _SonetClientCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1)
)
sonetClientCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmSampleDuration"),
    (0, "INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    sonetClientCtpPmEntry.setStatus("current")


class _SonetClientCtpPmTimestamp_Type(Integer32):
    """Custom type sonetClientCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SonetClientCtpPmTimestamp_Type.__name__ = "Integer32"
_SonetClientCtpPmTimestamp_Object = MibTableColumn
sonetClientCtpPmTimestamp = _SonetClientCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 1),
    _SonetClientCtpPmTimestamp_Type()
)
sonetClientCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetClientCtpPmTimestamp.setStatus("current")


class _SonetClientCtpPmSampleDuration_Type(Integer32):
    """Custom type sonetClientCtpPmSampleDuration based on Integer32"""
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


_SonetClientCtpPmSampleDuration_Type.__name__ = "Integer32"
_SonetClientCtpPmSampleDuration_Object = MibTableColumn
sonetClientCtpPmSampleDuration = _SonetClientCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 2),
    _SonetClientCtpPmSampleDuration_Type()
)
sonetClientCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sonetClientCtpPmSampleDuration.setStatus("current")
_SonetClientCtpPmValidity_Type = TruthValue
_SonetClientCtpPmValidity_Object = MibTableColumn
sonetClientCtpPmValidity = _SonetClientCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 3),
    _SonetClientCtpPmValidity_Type()
)
sonetClientCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmValidity.setStatus("current")
_SonetClientCtpPmRxCV_Type = HCPerfIntervalCount
_SonetClientCtpPmRxCV_Object = MibTableColumn
sonetClientCtpPmRxCV = _SonetClientCtpPmRxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 4),
    _SonetClientCtpPmRxCV_Type()
)
sonetClientCtpPmRxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRxCV.setStatus("current")
_SonetClientCtpPmRxES_Type = Integer32
_SonetClientCtpPmRxES_Object = MibTableColumn
sonetClientCtpPmRxES = _SonetClientCtpPmRxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 5),
    _SonetClientCtpPmRxES_Type()
)
sonetClientCtpPmRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRxES.setStatus("current")
_SonetClientCtpPmRxSES_Type = Integer32
_SonetClientCtpPmRxSES_Object = MibTableColumn
sonetClientCtpPmRxSES = _SonetClientCtpPmRxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 6),
    _SonetClientCtpPmRxSES_Type()
)
sonetClientCtpPmRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRxSES.setStatus("current")
_SonetClientCtpPmRxSEFS_Type = Integer32
_SonetClientCtpPmRxSEFS_Object = MibTableColumn
sonetClientCtpPmRxSEFS = _SonetClientCtpPmRxSEFS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 7),
    _SonetClientCtpPmRxSEFS_Type()
)
sonetClientCtpPmRxSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRxSEFS.setStatus("current")
_SonetClientCtpPmTxCV_Type = HCPerfIntervalCount
_SonetClientCtpPmTxCV_Object = MibTableColumn
sonetClientCtpPmTxCV = _SonetClientCtpPmTxCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 8),
    _SonetClientCtpPmTxCV_Type()
)
sonetClientCtpPmTxCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmTxCV.setStatus("current")
_SonetClientCtpPmTxES_Type = Integer32
_SonetClientCtpPmTxES_Object = MibTableColumn
sonetClientCtpPmTxES = _SonetClientCtpPmTxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 9),
    _SonetClientCtpPmTxES_Type()
)
sonetClientCtpPmTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmTxES.setStatus("current")
_SonetClientCtpPmTxSES_Type = Integer32
_SonetClientCtpPmTxSES_Object = MibTableColumn
sonetClientCtpPmTxSES = _SonetClientCtpPmTxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 10),
    _SonetClientCtpPmTxSES_Type()
)
sonetClientCtpPmTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmTxSES.setStatus("current")
_SonetClientCtpPmTxSEFS_Type = Integer32
_SonetClientCtpPmTxSEFS_Object = MibTableColumn
sonetClientCtpPmTxSEFS = _SonetClientCtpPmTxSEFS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 11),
    _SonetClientCtpPmTxSEFS_Type()
)
sonetClientCtpPmTxSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmTxSEFS.setStatus("current")
_SonetClientCtpPmCktId_Type = DisplayString
_SonetClientCtpPmCktId_Object = MibTableColumn
sonetClientCtpPmCktId = _SonetClientCtpPmCktId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 12),
    _SonetClientCtpPmCktId_Type()
)
sonetClientCtpPmCktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmCktId.setStatus("current")
_SonetClientCtpPmTribPRBSSyncErr_Type = Integer32
_SonetClientCtpPmTribPRBSSyncErr_Object = MibTableColumn
sonetClientCtpPmTribPRBSSyncErr = _SonetClientCtpPmTribPRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 13),
    _SonetClientCtpPmTribPRBSSyncErr_Type()
)
sonetClientCtpPmTribPRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmTribPRBSSyncErr.setStatus("current")
_SonetClientCtpPmTribPRBSErr_Type = HCPerfIntervalCount
_SonetClientCtpPmTribPRBSErr_Object = MibTableColumn
sonetClientCtpPmTribPRBSErr = _SonetClientCtpPmTribPRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 14),
    _SonetClientCtpPmTribPRBSErr_Type()
)
sonetClientCtpPmTribPRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmTribPRBSErr.setStatus("current")
_SonetClientCtpPmPayloadType_Type = InfnServiceType
_SonetClientCtpPmPayloadType_Object = MibTableColumn
sonetClientCtpPmPayloadType = _SonetClientCtpPmPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 15),
    _SonetClientCtpPmPayloadType_Type()
)
sonetClientCtpPmPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmPayloadType.setStatus("current")
_SonetClientCtpPmLinePRBSSyncErr_Type = Integer32
_SonetClientCtpPmLinePRBSSyncErr_Object = MibTableColumn
sonetClientCtpPmLinePRBSSyncErr = _SonetClientCtpPmLinePRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 16),
    _SonetClientCtpPmLinePRBSSyncErr_Type()
)
sonetClientCtpPmLinePRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmLinePRBSSyncErr.setStatus("current")
_SonetClientCtpPmLinePRBSErr_Type = HCPerfIntervalCount
_SonetClientCtpPmLinePRBSErr_Object = MibTableColumn
sonetClientCtpPmLinePRBSErr = _SonetClientCtpPmLinePRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 17),
    _SonetClientCtpPmLinePRBSErr_Type()
)
sonetClientCtpPmLinePRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmLinePRBSErr.setStatus("current")
_SonetClientCtpPmRxBER_Type = FloatArbitraryPrecision
_SonetClientCtpPmRxBER_Object = MibTableColumn
sonetClientCtpPmRxBER = _SonetClientCtpPmRxBER_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 18),
    _SonetClientCtpPmRxBER_Type()
)
sonetClientCtpPmRxBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmRxBER.setStatus("current")
_SonetClientCtpPmTxBER_Type = FloatArbitraryPrecision
_SonetClientCtpPmTxBER_Object = MibTableColumn
sonetClientCtpPmTxBER = _SonetClientCtpPmTxBER_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 2, 1, 19),
    _SonetClientCtpPmTxBER_Type()
)
sonetClientCtpPmTxBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sonetClientCtpPmTxBER.setStatus("current")
_SonetClientCtpPmConformance_ObjectIdentity = ObjectIdentity
sonetClientCtpPmConformance = _SonetClientCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 3)
)
_SonetClientCtpPmCompliances_ObjectIdentity = ObjectIdentity
sonetClientCtpPmCompliances = _SonetClientCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 3, 1)
)
_SonetClientCtpPmGroups_ObjectIdentity = ObjectIdentity
sonetClientCtpPmGroups = _SonetClientCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 3, 2)
)

# Managed Objects groups

sonetClientCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 3, 2, 1)
)
sonetClientCtpPmGroup.setObjects(
      *(("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmValidity"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRxCV"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRxES"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRxSES"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRxSEFS"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmTxCV"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmTxES"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmTxSES"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmTxSEFS"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmCktId"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmTribPRBSSyncErr"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmTribPRBSErr"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmPayloadType"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmLinePRBSSyncErr"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmLinePRBSErr"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRxBER"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmTxBER"))
)
if mibBuilder.loadTexts:
    sonetClientCtpPmGroup.setStatus("current")

sonetClientCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 3, 2, 2)
)
sonetClientCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealRxCV"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealRxES"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealRxSES"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealRxSEFS"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealTxCV"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealTxES"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealTxSES"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealTxSEFS"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealCktId"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealTribPRBSSyncErr"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealTribPRBSErr"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealLinePRBSSyncErr"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealLinePRBSErr"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealRxBER"),
        ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealTxBER"))
)
if mibBuilder.loadTexts:
    sonetClientCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sonetClientCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 3, 1, 1)
)
sonetClientCtpPmCompliance.setObjects(
    ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmGroup")
)
if mibBuilder.loadTexts:
    sonetClientCtpPmCompliance.setStatus(
        "current"
    )

sonetClientCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 2, 3, 1, 2)
)
sonetClientCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-SONETCLIENTCTP-MIB", "sonetClientCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    sonetClientCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-SONETCLIENTCTP-MIB",
    **{"sonetClientCtpPmMIB": sonetClientCtpPmMIB,
       "sonetClientCtpPmRealTable": sonetClientCtpPmRealTable,
       "sonetClientCtpPmRealEntry": sonetClientCtpPmRealEntry,
       "sonetClientCtpPmRealRxCV": sonetClientCtpPmRealRxCV,
       "sonetClientCtpPmRealRxES": sonetClientCtpPmRealRxES,
       "sonetClientCtpPmRealRxSES": sonetClientCtpPmRealRxSES,
       "sonetClientCtpPmRealRxSEFS": sonetClientCtpPmRealRxSEFS,
       "sonetClientCtpPmRealTxCV": sonetClientCtpPmRealTxCV,
       "sonetClientCtpPmRealTxES": sonetClientCtpPmRealTxES,
       "sonetClientCtpPmRealTxSES": sonetClientCtpPmRealTxSES,
       "sonetClientCtpPmRealTxSEFS": sonetClientCtpPmRealTxSEFS,
       "sonetClientCtpPmRealCktId": sonetClientCtpPmRealCktId,
       "sonetClientCtpPmRealTribPRBSSyncErr": sonetClientCtpPmRealTribPRBSSyncErr,
       "sonetClientCtpPmRealTribPRBSErr": sonetClientCtpPmRealTribPRBSErr,
       "sonetClientCtpPmRealLinePRBSSyncErr": sonetClientCtpPmRealLinePRBSSyncErr,
       "sonetClientCtpPmRealLinePRBSErr": sonetClientCtpPmRealLinePRBSErr,
       "sonetClientCtpPmRealRxBER": sonetClientCtpPmRealRxBER,
       "sonetClientCtpPmRealTxBER": sonetClientCtpPmRealTxBER,
       "sonetClientCtpPmTable": sonetClientCtpPmTable,
       "sonetClientCtpPmEntry": sonetClientCtpPmEntry,
       "sonetClientCtpPmTimestamp": sonetClientCtpPmTimestamp,
       "sonetClientCtpPmSampleDuration": sonetClientCtpPmSampleDuration,
       "sonetClientCtpPmValidity": sonetClientCtpPmValidity,
       "sonetClientCtpPmRxCV": sonetClientCtpPmRxCV,
       "sonetClientCtpPmRxES": sonetClientCtpPmRxES,
       "sonetClientCtpPmRxSES": sonetClientCtpPmRxSES,
       "sonetClientCtpPmRxSEFS": sonetClientCtpPmRxSEFS,
       "sonetClientCtpPmTxCV": sonetClientCtpPmTxCV,
       "sonetClientCtpPmTxES": sonetClientCtpPmTxES,
       "sonetClientCtpPmTxSES": sonetClientCtpPmTxSES,
       "sonetClientCtpPmTxSEFS": sonetClientCtpPmTxSEFS,
       "sonetClientCtpPmCktId": sonetClientCtpPmCktId,
       "sonetClientCtpPmTribPRBSSyncErr": sonetClientCtpPmTribPRBSSyncErr,
       "sonetClientCtpPmTribPRBSErr": sonetClientCtpPmTribPRBSErr,
       "sonetClientCtpPmPayloadType": sonetClientCtpPmPayloadType,
       "sonetClientCtpPmLinePRBSSyncErr": sonetClientCtpPmLinePRBSSyncErr,
       "sonetClientCtpPmLinePRBSErr": sonetClientCtpPmLinePRBSErr,
       "sonetClientCtpPmRxBER": sonetClientCtpPmRxBER,
       "sonetClientCtpPmTxBER": sonetClientCtpPmTxBER,
       "sonetClientCtpPmConformance": sonetClientCtpPmConformance,
       "sonetClientCtpPmCompliances": sonetClientCtpPmCompliances,
       "sonetClientCtpPmCompliance": sonetClientCtpPmCompliance,
       "sonetClientCtpPmRealCompliance": sonetClientCtpPmRealCompliance,
       "sonetClientCtpPmGroups": sonetClientCtpPmGroups,
       "sonetClientCtpPmGroup": sonetClientCtpPmGroup,
       "sonetClientCtpPmRealGroup": sonetClientCtpPmRealGroup}
)
