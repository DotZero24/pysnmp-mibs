# SNMP MIB module (INFINERA-PM-SDHCLIENTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-SDHCLIENTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:41 2025
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

sdhClientCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    sdhClientCtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SdhClientCtpPmRealTable_Object = MibTable
sdhClientCtpPmRealTable = _SdhClientCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1)
)
if mibBuilder.loadTexts:
    sdhClientCtpPmRealTable.setStatus("current")
_SdhClientCtpPmRealEntry_Object = MibTableRow
sdhClientCtpPmRealEntry = _SdhClientCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1)
)
sdhClientCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    sdhClientCtpPmRealEntry.setStatus("current")
_SdhClientCtpPmRealRxBE_Type = Counter64
_SdhClientCtpPmRealRxBE_Object = MibTableColumn
sdhClientCtpPmRealRxBE = _SdhClientCtpPmRealRxBE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 1),
    _SdhClientCtpPmRealRxBE_Type()
)
sdhClientCtpPmRealRxBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealRxBE.setStatus("current")
_SdhClientCtpPmRealRxES_Type = Integer32
_SdhClientCtpPmRealRxES_Object = MibTableColumn
sdhClientCtpPmRealRxES = _SdhClientCtpPmRealRxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 2),
    _SdhClientCtpPmRealRxES_Type()
)
sdhClientCtpPmRealRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealRxES.setStatus("current")
_SdhClientCtpPmRealRxSES_Type = Integer32
_SdhClientCtpPmRealRxSES_Object = MibTableColumn
sdhClientCtpPmRealRxSES = _SdhClientCtpPmRealRxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 3),
    _SdhClientCtpPmRealRxSES_Type()
)
sdhClientCtpPmRealRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealRxSES.setStatus("current")
_SdhClientCtpPmRealRxOFS_Type = Integer32
_SdhClientCtpPmRealRxOFS_Object = MibTableColumn
sdhClientCtpPmRealRxOFS = _SdhClientCtpPmRealRxOFS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 4),
    _SdhClientCtpPmRealRxOFS_Type()
)
sdhClientCtpPmRealRxOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealRxOFS.setStatus("current")
_SdhClientCtpPmRealRxLOSS_Type = Integer32
_SdhClientCtpPmRealRxLOSS_Object = MibTableColumn
sdhClientCtpPmRealRxLOSS = _SdhClientCtpPmRealRxLOSS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 5),
    _SdhClientCtpPmRealRxLOSS_Type()
)
sdhClientCtpPmRealRxLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealRxLOSS.setStatus("current")
_SdhClientCtpPmRealTxBE_Type = Counter64
_SdhClientCtpPmRealTxBE_Object = MibTableColumn
sdhClientCtpPmRealTxBE = _SdhClientCtpPmRealTxBE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 6),
    _SdhClientCtpPmRealTxBE_Type()
)
sdhClientCtpPmRealTxBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealTxBE.setStatus("current")
_SdhClientCtpPmRealTxES_Type = Integer32
_SdhClientCtpPmRealTxES_Object = MibTableColumn
sdhClientCtpPmRealTxES = _SdhClientCtpPmRealTxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 7),
    _SdhClientCtpPmRealTxES_Type()
)
sdhClientCtpPmRealTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealTxES.setStatus("current")
_SdhClientCtpPmRealTxSES_Type = Integer32
_SdhClientCtpPmRealTxSES_Object = MibTableColumn
sdhClientCtpPmRealTxSES = _SdhClientCtpPmRealTxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 8),
    _SdhClientCtpPmRealTxSES_Type()
)
sdhClientCtpPmRealTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealTxSES.setStatus("current")
_SdhClientCtpPmRealTxOFS_Type = Integer32
_SdhClientCtpPmRealTxOFS_Object = MibTableColumn
sdhClientCtpPmRealTxOFS = _SdhClientCtpPmRealTxOFS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 9),
    _SdhClientCtpPmRealTxOFS_Type()
)
sdhClientCtpPmRealTxOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealTxOFS.setStatus("current")
_SdhClientCtpPmRealCktId_Type = DisplayString
_SdhClientCtpPmRealCktId_Object = MibTableColumn
sdhClientCtpPmRealCktId = _SdhClientCtpPmRealCktId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 10),
    _SdhClientCtpPmRealCktId_Type()
)
sdhClientCtpPmRealCktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealCktId.setStatus("current")
_SdhClientCtpPmRealLinePRBSSyncErr_Type = Integer32
_SdhClientCtpPmRealLinePRBSSyncErr_Object = MibTableColumn
sdhClientCtpPmRealLinePRBSSyncErr = _SdhClientCtpPmRealLinePRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 11),
    _SdhClientCtpPmRealLinePRBSSyncErr_Type()
)
sdhClientCtpPmRealLinePRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealLinePRBSSyncErr.setStatus("current")
_SdhClientCtpPmRealLinePRBSErr_Type = HCPerfIntervalCount
_SdhClientCtpPmRealLinePRBSErr_Object = MibTableColumn
sdhClientCtpPmRealLinePRBSErr = _SdhClientCtpPmRealLinePRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 12),
    _SdhClientCtpPmRealLinePRBSErr_Type()
)
sdhClientCtpPmRealLinePRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealLinePRBSErr.setStatus("current")
_SdhClientCtpPmRealTribPRBSSyncErr_Type = Integer32
_SdhClientCtpPmRealTribPRBSSyncErr_Object = MibTableColumn
sdhClientCtpPmRealTribPRBSSyncErr = _SdhClientCtpPmRealTribPRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 13),
    _SdhClientCtpPmRealTribPRBSSyncErr_Type()
)
sdhClientCtpPmRealTribPRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealTribPRBSSyncErr.setStatus("current")
_SdhClientCtpPmRealTribPRBSErr_Type = HCPerfIntervalCount
_SdhClientCtpPmRealTribPRBSErr_Object = MibTableColumn
sdhClientCtpPmRealTribPRBSErr = _SdhClientCtpPmRealTribPRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 14),
    _SdhClientCtpPmRealTribPRBSErr_Type()
)
sdhClientCtpPmRealTribPRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealTribPRBSErr.setStatus("current")
_SdhClientCtpPmRealRxUAS_Type = Integer32
_SdhClientCtpPmRealRxUAS_Object = MibTableColumn
sdhClientCtpPmRealRxUAS = _SdhClientCtpPmRealRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 15),
    _SdhClientCtpPmRealRxUAS_Type()
)
sdhClientCtpPmRealRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealRxUAS.setStatus("current")
_SdhClientCtpPmRealTxUAS_Type = Integer32
_SdhClientCtpPmRealTxUAS_Object = MibTableColumn
sdhClientCtpPmRealTxUAS = _SdhClientCtpPmRealTxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 16),
    _SdhClientCtpPmRealTxUAS_Type()
)
sdhClientCtpPmRealTxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealTxUAS.setStatus("current")
_SdhClientCtpPmRealRxBER_Type = FloatArbitraryPrecision
_SdhClientCtpPmRealRxBER_Object = MibTableColumn
sdhClientCtpPmRealRxBER = _SdhClientCtpPmRealRxBER_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 17),
    _SdhClientCtpPmRealRxBER_Type()
)
sdhClientCtpPmRealRxBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealRxBER.setStatus("current")
_SdhClientCtpPmRealTxBER_Type = FloatArbitraryPrecision
_SdhClientCtpPmRealTxBER_Object = MibTableColumn
sdhClientCtpPmRealTxBER = _SdhClientCtpPmRealTxBER_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 1, 1, 18),
    _SdhClientCtpPmRealTxBER_Type()
)
sdhClientCtpPmRealTxBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRealTxBER.setStatus("current")
_SdhClientCtpPmTable_Object = MibTable
sdhClientCtpPmTable = _SdhClientCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2)
)
if mibBuilder.loadTexts:
    sdhClientCtpPmTable.setStatus("current")
_SdhClientCtpPmEntry_Object = MibTableRow
sdhClientCtpPmEntry = _SdhClientCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1)
)
sdhClientCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmSampleDuration"),
    (0, "INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    sdhClientCtpPmEntry.setStatus("current")


class _SdhClientCtpPmTimestamp_Type(Integer32):
    """Custom type sdhClientCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SdhClientCtpPmTimestamp_Type.__name__ = "Integer32"
_SdhClientCtpPmTimestamp_Object = MibTableColumn
sdhClientCtpPmTimestamp = _SdhClientCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 1),
    _SdhClientCtpPmTimestamp_Type()
)
sdhClientCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdhClientCtpPmTimestamp.setStatus("current")


class _SdhClientCtpPmSampleDuration_Type(Integer32):
    """Custom type sdhClientCtpPmSampleDuration based on Integer32"""
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


_SdhClientCtpPmSampleDuration_Type.__name__ = "Integer32"
_SdhClientCtpPmSampleDuration_Object = MibTableColumn
sdhClientCtpPmSampleDuration = _SdhClientCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 2),
    _SdhClientCtpPmSampleDuration_Type()
)
sdhClientCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sdhClientCtpPmSampleDuration.setStatus("current")
_SdhClientCtpPmValidity_Type = TruthValue
_SdhClientCtpPmValidity_Object = MibTableColumn
sdhClientCtpPmValidity = _SdhClientCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 3),
    _SdhClientCtpPmValidity_Type()
)
sdhClientCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmValidity.setStatus("current")
_SdhClientCtpPmRxBE_Type = HCPerfIntervalCount
_SdhClientCtpPmRxBE_Object = MibTableColumn
sdhClientCtpPmRxBE = _SdhClientCtpPmRxBE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 4),
    _SdhClientCtpPmRxBE_Type()
)
sdhClientCtpPmRxBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRxBE.setStatus("current")
_SdhClientCtpPmRxES_Type = Integer32
_SdhClientCtpPmRxES_Object = MibTableColumn
sdhClientCtpPmRxES = _SdhClientCtpPmRxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 5),
    _SdhClientCtpPmRxES_Type()
)
sdhClientCtpPmRxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRxES.setStatus("current")
_SdhClientCtpPmRxSES_Type = Integer32
_SdhClientCtpPmRxSES_Object = MibTableColumn
sdhClientCtpPmRxSES = _SdhClientCtpPmRxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 6),
    _SdhClientCtpPmRxSES_Type()
)
sdhClientCtpPmRxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRxSES.setStatus("current")
_SdhClientCtpPmRxOFS_Type = Integer32
_SdhClientCtpPmRxOFS_Object = MibTableColumn
sdhClientCtpPmRxOFS = _SdhClientCtpPmRxOFS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 7),
    _SdhClientCtpPmRxOFS_Type()
)
sdhClientCtpPmRxOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRxOFS.setStatus("current")
_SdhClientCtpPmRxLOSS_Type = Integer32
_SdhClientCtpPmRxLOSS_Object = MibTableColumn
sdhClientCtpPmRxLOSS = _SdhClientCtpPmRxLOSS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 8),
    _SdhClientCtpPmRxLOSS_Type()
)
sdhClientCtpPmRxLOSS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRxLOSS.setStatus("current")
_SdhClientCtpPmTxBE_Type = HCPerfIntervalCount
_SdhClientCtpPmTxBE_Object = MibTableColumn
sdhClientCtpPmTxBE = _SdhClientCtpPmTxBE_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 9),
    _SdhClientCtpPmTxBE_Type()
)
sdhClientCtpPmTxBE.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmTxBE.setStatus("current")
_SdhClientCtpPmTxES_Type = Integer32
_SdhClientCtpPmTxES_Object = MibTableColumn
sdhClientCtpPmTxES = _SdhClientCtpPmTxES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 10),
    _SdhClientCtpPmTxES_Type()
)
sdhClientCtpPmTxES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmTxES.setStatus("current")
_SdhClientCtpPmTxSES_Type = Integer32
_SdhClientCtpPmTxSES_Object = MibTableColumn
sdhClientCtpPmTxSES = _SdhClientCtpPmTxSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 11),
    _SdhClientCtpPmTxSES_Type()
)
sdhClientCtpPmTxSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmTxSES.setStatus("current")
_SdhClientCtpPmTxOFS_Type = Integer32
_SdhClientCtpPmTxOFS_Object = MibTableColumn
sdhClientCtpPmTxOFS = _SdhClientCtpPmTxOFS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 12),
    _SdhClientCtpPmTxOFS_Type()
)
sdhClientCtpPmTxOFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmTxOFS.setStatus("current")
_SdhClientCtpPmCktId_Type = DisplayString
_SdhClientCtpPmCktId_Object = MibTableColumn
sdhClientCtpPmCktId = _SdhClientCtpPmCktId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 13),
    _SdhClientCtpPmCktId_Type()
)
sdhClientCtpPmCktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmCktId.setStatus("current")
_SdhClientCtpPmTribPRBSSyncErr_Type = Integer32
_SdhClientCtpPmTribPRBSSyncErr_Object = MibTableColumn
sdhClientCtpPmTribPRBSSyncErr = _SdhClientCtpPmTribPRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 14),
    _SdhClientCtpPmTribPRBSSyncErr_Type()
)
sdhClientCtpPmTribPRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmTribPRBSSyncErr.setStatus("current")
_SdhClientCtpPmTribPRBSErr_Type = HCPerfIntervalCount
_SdhClientCtpPmTribPRBSErr_Object = MibTableColumn
sdhClientCtpPmTribPRBSErr = _SdhClientCtpPmTribPRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 15),
    _SdhClientCtpPmTribPRBSErr_Type()
)
sdhClientCtpPmTribPRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmTribPRBSErr.setStatus("current")
_SdhClientCtpPmPayloadType_Type = InfnServiceType
_SdhClientCtpPmPayloadType_Object = MibTableColumn
sdhClientCtpPmPayloadType = _SdhClientCtpPmPayloadType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 16),
    _SdhClientCtpPmPayloadType_Type()
)
sdhClientCtpPmPayloadType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmPayloadType.setStatus("current")
_SdhClientCtpPmRxUAS_Type = Integer32
_SdhClientCtpPmRxUAS_Object = MibTableColumn
sdhClientCtpPmRxUAS = _SdhClientCtpPmRxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 17),
    _SdhClientCtpPmRxUAS_Type()
)
sdhClientCtpPmRxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmRxUAS.setStatus("current")
_SdhClientCtpPmTxUAS_Type = Integer32
_SdhClientCtpPmTxUAS_Object = MibTableColumn
sdhClientCtpPmTxUAS = _SdhClientCtpPmTxUAS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 18),
    _SdhClientCtpPmTxUAS_Type()
)
sdhClientCtpPmTxUAS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmTxUAS.setStatus("current")
_SdhClientCtpPmLinePRBSSyncErr_Type = Integer32
_SdhClientCtpPmLinePRBSSyncErr_Object = MibTableColumn
sdhClientCtpPmLinePRBSSyncErr = _SdhClientCtpPmLinePRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 19),
    _SdhClientCtpPmLinePRBSSyncErr_Type()
)
sdhClientCtpPmLinePRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmLinePRBSSyncErr.setStatus("current")
_SdhClientCtpPmLinePRBSErr_Type = HCPerfIntervalCount
_SdhClientCtpPmLinePRBSErr_Object = MibTableColumn
sdhClientCtpPmLinePRBSErr = _SdhClientCtpPmLinePRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 2, 1, 20),
    _SdhClientCtpPmLinePRBSErr_Type()
)
sdhClientCtpPmLinePRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sdhClientCtpPmLinePRBSErr.setStatus("current")
_SdhClientCtpPmConformance_ObjectIdentity = ObjectIdentity
sdhClientCtpPmConformance = _SdhClientCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 3)
)
_SdhClientCtpPmCompliances_ObjectIdentity = ObjectIdentity
sdhClientCtpPmCompliances = _SdhClientCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 3, 1)
)
_SdhClientCtpPmGroups_ObjectIdentity = ObjectIdentity
sdhClientCtpPmGroups = _SdhClientCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 3, 2)
)

# Managed Objects groups

sdhClientCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 3, 2, 1)
)
sdhClientCtpPmGroup.setObjects(
      *(("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmValidity"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRxBE"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRxES"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRxSES"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRxOFS"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRxLOSS"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmTxBE"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmTxES"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmTxSES"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmTxOFS"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmCktId"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmTribPRBSSyncErr"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmTribPRBSErr"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmPayloadType"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRxUAS"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmTxUAS"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmLinePRBSSyncErr"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmLinePRBSErr"))
)
if mibBuilder.loadTexts:
    sdhClientCtpPmGroup.setStatus("current")

sdhClientCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 3, 2, 2)
)
sdhClientCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealRxBE"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealRxES"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealRxSES"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealRxOFS"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealRxLOSS"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealTxBE"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealTxES"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealTxSES"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealTxOFS"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealCktId"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealLinePRBSSyncErr"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealLinePRBSErr"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealTribPRBSSyncErr"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealTribPRBSErr"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRxUAS"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmTxUAS"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealRxBER"),
        ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealTxBER"))
)
if mibBuilder.loadTexts:
    sdhClientCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sdhClientCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 3, 1, 1)
)
sdhClientCtpPmCompliance.setObjects(
    ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmGroup")
)
if mibBuilder.loadTexts:
    sdhClientCtpPmCompliance.setStatus(
        "current"
    )

sdhClientCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 1, 3, 1, 2)
)
sdhClientCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-SDHCLIENTCTP-MIB", "sdhClientCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    sdhClientCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-SDHCLIENTCTP-MIB",
    **{"sdhClientCtpPmMIB": sdhClientCtpPmMIB,
       "sdhClientCtpPmRealTable": sdhClientCtpPmRealTable,
       "sdhClientCtpPmRealEntry": sdhClientCtpPmRealEntry,
       "sdhClientCtpPmRealRxBE": sdhClientCtpPmRealRxBE,
       "sdhClientCtpPmRealRxES": sdhClientCtpPmRealRxES,
       "sdhClientCtpPmRealRxSES": sdhClientCtpPmRealRxSES,
       "sdhClientCtpPmRealRxOFS": sdhClientCtpPmRealRxOFS,
       "sdhClientCtpPmRealRxLOSS": sdhClientCtpPmRealRxLOSS,
       "sdhClientCtpPmRealTxBE": sdhClientCtpPmRealTxBE,
       "sdhClientCtpPmRealTxES": sdhClientCtpPmRealTxES,
       "sdhClientCtpPmRealTxSES": sdhClientCtpPmRealTxSES,
       "sdhClientCtpPmRealTxOFS": sdhClientCtpPmRealTxOFS,
       "sdhClientCtpPmRealCktId": sdhClientCtpPmRealCktId,
       "sdhClientCtpPmRealLinePRBSSyncErr": sdhClientCtpPmRealLinePRBSSyncErr,
       "sdhClientCtpPmRealLinePRBSErr": sdhClientCtpPmRealLinePRBSErr,
       "sdhClientCtpPmRealTribPRBSSyncErr": sdhClientCtpPmRealTribPRBSSyncErr,
       "sdhClientCtpPmRealTribPRBSErr": sdhClientCtpPmRealTribPRBSErr,
       "sdhClientCtpPmRealRxUAS": sdhClientCtpPmRealRxUAS,
       "sdhClientCtpPmRealTxUAS": sdhClientCtpPmRealTxUAS,
       "sdhClientCtpPmRealRxBER": sdhClientCtpPmRealRxBER,
       "sdhClientCtpPmRealTxBER": sdhClientCtpPmRealTxBER,
       "sdhClientCtpPmTable": sdhClientCtpPmTable,
       "sdhClientCtpPmEntry": sdhClientCtpPmEntry,
       "sdhClientCtpPmTimestamp": sdhClientCtpPmTimestamp,
       "sdhClientCtpPmSampleDuration": sdhClientCtpPmSampleDuration,
       "sdhClientCtpPmValidity": sdhClientCtpPmValidity,
       "sdhClientCtpPmRxBE": sdhClientCtpPmRxBE,
       "sdhClientCtpPmRxES": sdhClientCtpPmRxES,
       "sdhClientCtpPmRxSES": sdhClientCtpPmRxSES,
       "sdhClientCtpPmRxOFS": sdhClientCtpPmRxOFS,
       "sdhClientCtpPmRxLOSS": sdhClientCtpPmRxLOSS,
       "sdhClientCtpPmTxBE": sdhClientCtpPmTxBE,
       "sdhClientCtpPmTxES": sdhClientCtpPmTxES,
       "sdhClientCtpPmTxSES": sdhClientCtpPmTxSES,
       "sdhClientCtpPmTxOFS": sdhClientCtpPmTxOFS,
       "sdhClientCtpPmCktId": sdhClientCtpPmCktId,
       "sdhClientCtpPmTribPRBSSyncErr": sdhClientCtpPmTribPRBSSyncErr,
       "sdhClientCtpPmTribPRBSErr": sdhClientCtpPmTribPRBSErr,
       "sdhClientCtpPmPayloadType": sdhClientCtpPmPayloadType,
       "sdhClientCtpPmRxUAS": sdhClientCtpPmRxUAS,
       "sdhClientCtpPmTxUAS": sdhClientCtpPmTxUAS,
       "sdhClientCtpPmLinePRBSSyncErr": sdhClientCtpPmLinePRBSSyncErr,
       "sdhClientCtpPmLinePRBSErr": sdhClientCtpPmLinePRBSErr,
       "sdhClientCtpPmConformance": sdhClientCtpPmConformance,
       "sdhClientCtpPmCompliances": sdhClientCtpPmCompliances,
       "sdhClientCtpPmCompliance": sdhClientCtpPmCompliance,
       "sdhClientCtpPmRealCompliance": sdhClientCtpPmRealCompliance,
       "sdhClientCtpPmGroups": sdhClientCtpPmGroups,
       "sdhClientCtpPmGroup": sdhClientCtpPmGroup,
       "sdhClientCtpPmRealGroup": sdhClientCtpPmRealGroup}
)
