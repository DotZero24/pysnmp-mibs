# SNMP MIB module (INFINERA-PM-DCHCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-DCHCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:06 2025
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

(FloatArbitraryPrecision,
 FloatHundredths) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "FloatHundredths")

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

dchCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    dchCtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DchCtpPmRealTable_Object = MibTable
dchCtpPmRealTable = _DchCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1)
)
if mibBuilder.loadTexts:
    dchCtpPmRealTable.setStatus("current")
_DchCtpPmRealEntry_Object = MibTableRow
dchCtpPmRealEntry = _DchCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1)
)
dchCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dchCtpPmRealEntry.setStatus("current")
_DchCtpPmRealQ_Type = FloatHundredths
_DchCtpPmRealQ_Object = MibTableColumn
dchCtpPmRealQ = _DchCtpPmRealQ_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 1),
    _DchCtpPmRealQ_Type()
)
dchCtpPmRealQ.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealQ.setStatus("current")
_DchCtpPmRealBerPreFec_Type = FloatArbitraryPrecision
_DchCtpPmRealBerPreFec_Object = MibTableColumn
dchCtpPmRealBerPreFec = _DchCtpPmRealBerPreFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 2),
    _DchCtpPmRealBerPreFec_Type()
)
dchCtpPmRealBerPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealBerPreFec.setStatus("current")
_DchCtpPmRealBerPostFec_Type = FloatArbitraryPrecision
_DchCtpPmRealBerPostFec_Object = MibTableColumn
dchCtpPmRealBerPostFec = _DchCtpPmRealBerPostFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 3),
    _DchCtpPmRealBerPostFec_Type()
)
dchCtpPmRealBerPostFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealBerPostFec.setStatus("current")
_DchCtpPmRealFecCorrectedBits_Type = Counter64
_DchCtpPmRealFecCorrectedBits_Object = MibTableColumn
dchCtpPmRealFecCorrectedBits = _DchCtpPmRealFecCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 4),
    _DchCtpPmRealFecCorrectedBits_Type()
)
dchCtpPmRealFecCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealFecCorrectedBits.setStatus("current")
_DchCtpPmRealFecUncorrectedRows_Type = Counter64
_DchCtpPmRealFecUncorrectedRows_Object = MibTableColumn
dchCtpPmRealFecUncorrectedRows = _DchCtpPmRealFecUncorrectedRows_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 5),
    _DchCtpPmRealFecUncorrectedRows_Type()
)
dchCtpPmRealFecUncorrectedRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealFecUncorrectedRows.setStatus("current")
_DchCtpPmRealFecTotalCodeWords_Type = Counter64
_DchCtpPmRealFecTotalCodeWords_Object = MibTableColumn
dchCtpPmRealFecTotalCodeWords = _DchCtpPmRealFecTotalCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 6),
    _DchCtpPmRealFecTotalCodeWords_Type()
)
dchCtpPmRealFecTotalCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealFecTotalCodeWords.setStatus("current")
_DchCtpPmRealDtsCV_Type = Counter64
_DchCtpPmRealDtsCV_Object = MibTableColumn
dchCtpPmRealDtsCV = _DchCtpPmRealDtsCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 7),
    _DchCtpPmRealDtsCV_Type()
)
dchCtpPmRealDtsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealDtsCV.setStatus("current")
_DchCtpPmRealDtsES_Type = Integer32
_DchCtpPmRealDtsES_Object = MibTableColumn
dchCtpPmRealDtsES = _DchCtpPmRealDtsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 8),
    _DchCtpPmRealDtsES_Type()
)
dchCtpPmRealDtsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealDtsES.setStatus("current")
_DchCtpPmRealDtsSES_Type = Integer32
_DchCtpPmRealDtsSES_Object = MibTableColumn
dchCtpPmRealDtsSES = _DchCtpPmRealDtsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 9),
    _DchCtpPmRealDtsSES_Type()
)
dchCtpPmRealDtsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealDtsSES.setStatus("current")
_DchCtpPmRealDtsSEFS_Type = Integer32
_DchCtpPmRealDtsSEFS_Object = MibTableColumn
dchCtpPmRealDtsSEFS = _DchCtpPmRealDtsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 10),
    _DchCtpPmRealDtsSEFS_Type()
)
dchCtpPmRealDtsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealDtsSEFS.setStatus("current")
_DchCtpPmRealCktId_Type = DisplayString
_DchCtpPmRealCktId_Object = MibTableColumn
dchCtpPmRealCktId = _DchCtpPmRealCktId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 11),
    _DchCtpPmRealCktId_Type()
)
dchCtpPmRealCktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealCktId.setStatus("current")
_DchCtpPmRealLinePRBSSyncErr_Type = Integer32
_DchCtpPmRealLinePRBSSyncErr_Object = MibTableColumn
dchCtpPmRealLinePRBSSyncErr = _DchCtpPmRealLinePRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 12),
    _DchCtpPmRealLinePRBSSyncErr_Type()
)
dchCtpPmRealLinePRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealLinePRBSSyncErr.setStatus("current")
_DchCtpPmRealLinePRBSErr_Type = HCPerfIntervalCount
_DchCtpPmRealLinePRBSErr_Object = MibTableColumn
dchCtpPmRealLinePRBSErr = _DchCtpPmRealLinePRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 13),
    _DchCtpPmRealLinePRBSErr_Type()
)
dchCtpPmRealLinePRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealLinePRBSErr.setStatus("current")
_DchCtpPmRealTribPRBSSyncErr_Type = Integer32
_DchCtpPmRealTribPRBSSyncErr_Object = MibTableColumn
dchCtpPmRealTribPRBSSyncErr = _DchCtpPmRealTribPRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 14),
    _DchCtpPmRealTribPRBSSyncErr_Type()
)
dchCtpPmRealTribPRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealTribPRBSSyncErr.setStatus("current")
_DchCtpPmRealTribPRBSErr_Type = HCPerfIntervalCount
_DchCtpPmRealTribPRBSErr_Object = MibTableColumn
dchCtpPmRealTribPRBSErr = _DchCtpPmRealTribPRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 1, 1, 15),
    _DchCtpPmRealTribPRBSErr_Type()
)
dchCtpPmRealTribPRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmRealTribPRBSErr.setStatus("current")
_DchCtpPmTable_Object = MibTable
dchCtpPmTable = _DchCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2)
)
if mibBuilder.loadTexts:
    dchCtpPmTable.setStatus("current")
_DchCtpPmEntry_Object = MibTableRow
dchCtpPmEntry = _DchCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1)
)
dchCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-DCHCTP-MIB", "dchCtpPmSampleDuration"),
    (0, "INFINERA-PM-DCHCTP-MIB", "dchCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    dchCtpPmEntry.setStatus("current")


class _DchCtpPmTimestamp_Type(Integer32):
    """Custom type dchCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DchCtpPmTimestamp_Type.__name__ = "Integer32"
_DchCtpPmTimestamp_Object = MibTableColumn
dchCtpPmTimestamp = _DchCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 1),
    _DchCtpPmTimestamp_Type()
)
dchCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dchCtpPmTimestamp.setStatus("current")


class _DchCtpPmSampleDuration_Type(Integer32):
    """Custom type dchCtpPmSampleDuration based on Integer32"""
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


_DchCtpPmSampleDuration_Type.__name__ = "Integer32"
_DchCtpPmSampleDuration_Object = MibTableColumn
dchCtpPmSampleDuration = _DchCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 2),
    _DchCtpPmSampleDuration_Type()
)
dchCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dchCtpPmSampleDuration.setStatus("current")
_DchCtpPmValidity_Type = TruthValue
_DchCtpPmValidity_Object = MibTableColumn
dchCtpPmValidity = _DchCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 3),
    _DchCtpPmValidity_Type()
)
dchCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmValidity.setStatus("current")
_DchCtpPmFecCorrectedBits_Type = HCPerfIntervalCount
_DchCtpPmFecCorrectedBits_Object = MibTableColumn
dchCtpPmFecCorrectedBits = _DchCtpPmFecCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 4),
    _DchCtpPmFecCorrectedBits_Type()
)
dchCtpPmFecCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmFecCorrectedBits.setStatus("current")
_DchCtpPmFecUncorrectedRows_Type = HCPerfIntervalCount
_DchCtpPmFecUncorrectedRows_Object = MibTableColumn
dchCtpPmFecUncorrectedRows = _DchCtpPmFecUncorrectedRows_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 5),
    _DchCtpPmFecUncorrectedRows_Type()
)
dchCtpPmFecUncorrectedRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmFecUncorrectedRows.setStatus("current")
_DchCtpPmFecTotalCodeWords_Type = HCPerfIntervalCount
_DchCtpPmFecTotalCodeWords_Object = MibTableColumn
dchCtpPmFecTotalCodeWords = _DchCtpPmFecTotalCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 6),
    _DchCtpPmFecTotalCodeWords_Type()
)
dchCtpPmFecTotalCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmFecTotalCodeWords.setStatus("current")
_DchCtpPmDtsCV_Type = HCPerfIntervalCount
_DchCtpPmDtsCV_Object = MibTableColumn
dchCtpPmDtsCV = _DchCtpPmDtsCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 7),
    _DchCtpPmDtsCV_Type()
)
dchCtpPmDtsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmDtsCV.setStatus("current")
_DchCtpPmDtsES_Type = Integer32
_DchCtpPmDtsES_Object = MibTableColumn
dchCtpPmDtsES = _DchCtpPmDtsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 8),
    _DchCtpPmDtsES_Type()
)
dchCtpPmDtsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmDtsES.setStatus("current")
_DchCtpPmDtsSES_Type = Integer32
_DchCtpPmDtsSES_Object = MibTableColumn
dchCtpPmDtsSES = _DchCtpPmDtsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 9),
    _DchCtpPmDtsSES_Type()
)
dchCtpPmDtsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmDtsSES.setStatus("current")
_DchCtpPmDtsSEFS_Type = Integer32
_DchCtpPmDtsSEFS_Object = MibTableColumn
dchCtpPmDtsSEFS = _DchCtpPmDtsSEFS_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 10),
    _DchCtpPmDtsSEFS_Type()
)
dchCtpPmDtsSEFS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmDtsSEFS.setStatus("current")
_DchCtpPmCktId_Type = DisplayString
_DchCtpPmCktId_Object = MibTableColumn
dchCtpPmCktId = _DchCtpPmCktId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 11),
    _DchCtpPmCktId_Type()
)
dchCtpPmCktId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmCktId.setStatus("current")
_DchCtpPmTribPRBSSyncErr_Type = Integer32
_DchCtpPmTribPRBSSyncErr_Object = MibTableColumn
dchCtpPmTribPRBSSyncErr = _DchCtpPmTribPRBSSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 12),
    _DchCtpPmTribPRBSSyncErr_Type()
)
dchCtpPmTribPRBSSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmTribPRBSSyncErr.setStatus("current")
_DchCtpPmTribPRBSErr_Type = HCPerfIntervalCount
_DchCtpPmTribPRBSErr_Object = MibTableColumn
dchCtpPmTribPRBSErr = _DchCtpPmTribPRBSErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 2, 1, 13),
    _DchCtpPmTribPRBSErr_Type()
)
dchCtpPmTribPRBSErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dchCtpPmTribPRBSErr.setStatus("current")
_DchCtpPmConformance_ObjectIdentity = ObjectIdentity
dchCtpPmConformance = _DchCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 3)
)
_DchCtpPmCompliances_ObjectIdentity = ObjectIdentity
dchCtpPmCompliances = _DchCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 3, 1)
)
_DchCtpPmGroups_ObjectIdentity = ObjectIdentity
dchCtpPmGroups = _DchCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 3, 2)
)

# Managed Objects groups

dchCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 3, 2, 1)
)
dchCtpPmGroup.setObjects(
      *(("INFINERA-PM-DCHCTP-MIB", "dchCtpPmValidity"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmFecCorrectedBits"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmFecUncorrectedRows"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmFecTotalCodeWords"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmDtsCV"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmDtsES"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmDtsSES"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmDtsSEFS"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmCktId"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmTribPRBSSyncErr"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmTribPRBSErr"))
)
if mibBuilder.loadTexts:
    dchCtpPmGroup.setStatus("current")

dchCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 3, 2, 2)
)
dchCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealQ"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealBerPreFec"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealBerPostFec"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealFecCorrectedBits"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealFecUncorrectedRows"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealFecTotalCodeWords"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealDtsCV"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealDtsES"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealDtsSES"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealDtsSEFS"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealCktId"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealLinePRBSSyncErr"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealLinePRBSErr"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealTribPRBSSyncErr"),
        ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealTribPRBSErr"))
)
if mibBuilder.loadTexts:
    dchCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dchCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 3, 1, 1)
)
dchCtpPmCompliance.setObjects(
    ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmGroup")
)
if mibBuilder.loadTexts:
    dchCtpPmCompliance.setStatus(
        "current"
    )

dchCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 4, 3, 1, 2)
)
dchCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-DCHCTP-MIB", "dchCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    dchCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-DCHCTP-MIB",
    **{"dchCtpPmMIB": dchCtpPmMIB,
       "dchCtpPmRealTable": dchCtpPmRealTable,
       "dchCtpPmRealEntry": dchCtpPmRealEntry,
       "dchCtpPmRealQ": dchCtpPmRealQ,
       "dchCtpPmRealBerPreFec": dchCtpPmRealBerPreFec,
       "dchCtpPmRealBerPostFec": dchCtpPmRealBerPostFec,
       "dchCtpPmRealFecCorrectedBits": dchCtpPmRealFecCorrectedBits,
       "dchCtpPmRealFecUncorrectedRows": dchCtpPmRealFecUncorrectedRows,
       "dchCtpPmRealFecTotalCodeWords": dchCtpPmRealFecTotalCodeWords,
       "dchCtpPmRealDtsCV": dchCtpPmRealDtsCV,
       "dchCtpPmRealDtsES": dchCtpPmRealDtsES,
       "dchCtpPmRealDtsSES": dchCtpPmRealDtsSES,
       "dchCtpPmRealDtsSEFS": dchCtpPmRealDtsSEFS,
       "dchCtpPmRealCktId": dchCtpPmRealCktId,
       "dchCtpPmRealLinePRBSSyncErr": dchCtpPmRealLinePRBSSyncErr,
       "dchCtpPmRealLinePRBSErr": dchCtpPmRealLinePRBSErr,
       "dchCtpPmRealTribPRBSSyncErr": dchCtpPmRealTribPRBSSyncErr,
       "dchCtpPmRealTribPRBSErr": dchCtpPmRealTribPRBSErr,
       "dchCtpPmTable": dchCtpPmTable,
       "dchCtpPmEntry": dchCtpPmEntry,
       "dchCtpPmTimestamp": dchCtpPmTimestamp,
       "dchCtpPmSampleDuration": dchCtpPmSampleDuration,
       "dchCtpPmValidity": dchCtpPmValidity,
       "dchCtpPmFecCorrectedBits": dchCtpPmFecCorrectedBits,
       "dchCtpPmFecUncorrectedRows": dchCtpPmFecUncorrectedRows,
       "dchCtpPmFecTotalCodeWords": dchCtpPmFecTotalCodeWords,
       "dchCtpPmDtsCV": dchCtpPmDtsCV,
       "dchCtpPmDtsES": dchCtpPmDtsES,
       "dchCtpPmDtsSES": dchCtpPmDtsSES,
       "dchCtpPmDtsSEFS": dchCtpPmDtsSEFS,
       "dchCtpPmCktId": dchCtpPmCktId,
       "dchCtpPmTribPRBSSyncErr": dchCtpPmTribPRBSSyncErr,
       "dchCtpPmTribPRBSErr": dchCtpPmTribPRBSErr,
       "dchCtpPmConformance": dchCtpPmConformance,
       "dchCtpPmCompliances": dchCtpPmCompliances,
       "dchCtpPmCompliance": dchCtpPmCompliance,
       "dchCtpPmRealCompliance": dchCtpPmRealCompliance,
       "dchCtpPmGroups": dchCtpPmGroups,
       "dchCtpPmGroup": dchCtpPmGroup,
       "dchCtpPmRealGroup": dchCtpPmRealGroup}
)
