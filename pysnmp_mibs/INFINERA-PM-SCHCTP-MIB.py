# SNMP MIB module (INFINERA-PM-SCHCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-SCHCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:16 2025
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

schCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38)
)
if mibBuilder.loadTexts:
    schCtpPmMIB.setRevisions(
        ("2013-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SchCtpPmRealTable_Object = MibTable
schCtpPmRealTable = _SchCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1)
)
if mibBuilder.loadTexts:
    schCtpPmRealTable.setStatus("current")
_SchCtpPmRealEntry_Object = MibTableRow
schCtpPmRealEntry = _SchCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1, 1)
)
schCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    schCtpPmRealEntry.setStatus("current")
_SchCtpPmRealChanSchOpt_Type = FloatHundredths
_SchCtpPmRealChanSchOpt_Object = MibTableColumn
schCtpPmRealChanSchOpt = _SchCtpPmRealChanSchOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1, 1, 1),
    _SchCtpPmRealChanSchOpt_Type()
)
schCtpPmRealChanSchOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmRealChanSchOpt.setStatus("current")
_SchCtpPmRealPmd_Type = FloatArbitraryPrecision
_SchCtpPmRealPmd_Object = MibTableColumn
schCtpPmRealPmd = _SchCtpPmRealPmd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1, 1, 2),
    _SchCtpPmRealPmd_Type()
)
schCtpPmRealPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmRealPmd.setStatus("current")
_SchCtpPmRealSoPmd_Type = FloatArbitraryPrecision
_SchCtpPmRealSoPmd_Object = MibTableColumn
schCtpPmRealSoPmd = _SchCtpPmRealSoPmd_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1, 1, 3),
    _SchCtpPmRealSoPmd_Type()
)
schCtpPmRealSoPmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmRealSoPmd.setStatus("current")
_SchCtpPmRealSchOpt_Type = FloatHundredths
_SchCtpPmRealSchOpt_Object = MibTableColumn
schCtpPmRealSchOpt = _SchCtpPmRealSchOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1, 1, 4),
    _SchCtpPmRealSchOpt_Type()
)
schCtpPmRealSchOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmRealSchOpt.setStatus("current")
_SchCtpPmRealSchEstimatedSpanOpt_Type = FloatHundredths
_SchCtpPmRealSchEstimatedSpanOpt_Object = MibTableColumn
schCtpPmRealSchEstimatedSpanOpt = _SchCtpPmRealSchEstimatedSpanOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1, 1, 5),
    _SchCtpPmRealSchEstimatedSpanOpt_Type()
)
schCtpPmRealSchEstimatedSpanOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmRealSchEstimatedSpanOpt.setStatus("current")
_SchCtpPmRealSchTargetSpanOpt_Type = FloatHundredths
_SchCtpPmRealSchTargetSpanOpt_Object = MibTableColumn
schCtpPmRealSchTargetSpanOpt = _SchCtpPmRealSchTargetSpanOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1, 1, 6),
    _SchCtpPmRealSchTargetSpanOpt_Type()
)
schCtpPmRealSchTargetSpanOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmRealSchTargetSpanOpt.setStatus("current")
_SchCtpPmRealSchOpr_Type = FloatHundredths
_SchCtpPmRealSchOpr_Object = MibTableColumn
schCtpPmRealSchOpr = _SchCtpPmRealSchOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1, 1, 7),
    _SchCtpPmRealSchOpr_Type()
)
schCtpPmRealSchOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmRealSchOpr.setStatus("current")
_SchCtpPmRealLastPollTimeStampOpt_Type = Integer32
_SchCtpPmRealLastPollTimeStampOpt_Object = MibTableColumn
schCtpPmRealLastPollTimeStampOpt = _SchCtpPmRealLastPollTimeStampOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1, 1, 8),
    _SchCtpPmRealLastPollTimeStampOpt_Type()
)
schCtpPmRealLastPollTimeStampOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmRealLastPollTimeStampOpt.setStatus("current")
_SchCtpPmRealLastPollTimeStampOpr_Type = Integer32
_SchCtpPmRealLastPollTimeStampOpr_Object = MibTableColumn
schCtpPmRealLastPollTimeStampOpr = _SchCtpPmRealLastPollTimeStampOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 1, 1, 9),
    _SchCtpPmRealLastPollTimeStampOpr_Type()
)
schCtpPmRealLastPollTimeStampOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmRealLastPollTimeStampOpr.setStatus("current")
_SchCtpPmTable_Object = MibTable
schCtpPmTable = _SchCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2)
)
if mibBuilder.loadTexts:
    schCtpPmTable.setStatus("current")
_SchCtpPmEntry_Object = MibTableRow
schCtpPmEntry = _SchCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1)
)
schCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-SCHCTP-MIB", "schCtpPmSampleDuration"),
    (0, "INFINERA-PM-SCHCTP-MIB", "schCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    schCtpPmEntry.setStatus("current")


class _SchCtpPmTimestamp_Type(Integer32):
    """Custom type schCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_SchCtpPmTimestamp_Type.__name__ = "Integer32"
_SchCtpPmTimestamp_Object = MibTableColumn
schCtpPmTimestamp = _SchCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 1),
    _SchCtpPmTimestamp_Type()
)
schCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    schCtpPmTimestamp.setStatus("current")


class _SchCtpPmSampleDuration_Type(Integer32):
    """Custom type schCtpPmSampleDuration based on Integer32"""
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


_SchCtpPmSampleDuration_Type.__name__ = "Integer32"
_SchCtpPmSampleDuration_Object = MibTableColumn
schCtpPmSampleDuration = _SchCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 2),
    _SchCtpPmSampleDuration_Type()
)
schCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    schCtpPmSampleDuration.setStatus("current")
_SchCtpPmValidity_Type = TruthValue
_SchCtpPmValidity_Object = MibTableColumn
schCtpPmValidity = _SchCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 3),
    _SchCtpPmValidity_Type()
)
schCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmValidity.setStatus("current")
_SchCtpPmChanSchOptMin_Type = FloatHundredths
_SchCtpPmChanSchOptMin_Object = MibTableColumn
schCtpPmChanSchOptMin = _SchCtpPmChanSchOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 4),
    _SchCtpPmChanSchOptMin_Type()
)
schCtpPmChanSchOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmChanSchOptMin.setStatus("current")
_SchCtpPmChanSchOptMax_Type = FloatHundredths
_SchCtpPmChanSchOptMax_Object = MibTableColumn
schCtpPmChanSchOptMax = _SchCtpPmChanSchOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 5),
    _SchCtpPmChanSchOptMax_Type()
)
schCtpPmChanSchOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmChanSchOptMax.setStatus("current")
_SchCtpPmChanSchOptAve_Type = FloatHundredths
_SchCtpPmChanSchOptAve_Object = MibTableColumn
schCtpPmChanSchOptAve = _SchCtpPmChanSchOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 6),
    _SchCtpPmChanSchOptAve_Type()
)
schCtpPmChanSchOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmChanSchOptAve.setStatus("current")
_SchCtpPmPmdMin_Type = FloatArbitraryPrecision
_SchCtpPmPmdMin_Object = MibTableColumn
schCtpPmPmdMin = _SchCtpPmPmdMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 7),
    _SchCtpPmPmdMin_Type()
)
schCtpPmPmdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmPmdMin.setStatus("current")
_SchCtpPmPmdMax_Type = FloatArbitraryPrecision
_SchCtpPmPmdMax_Object = MibTableColumn
schCtpPmPmdMax = _SchCtpPmPmdMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 8),
    _SchCtpPmPmdMax_Type()
)
schCtpPmPmdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmPmdMax.setStatus("current")
_SchCtpPmPmdAve_Type = FloatArbitraryPrecision
_SchCtpPmPmdAve_Object = MibTableColumn
schCtpPmPmdAve = _SchCtpPmPmdAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 9),
    _SchCtpPmPmdAve_Type()
)
schCtpPmPmdAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmPmdAve.setStatus("current")
_SchCtpPmSoPmdMin_Type = FloatArbitraryPrecision
_SchCtpPmSoPmdMin_Object = MibTableColumn
schCtpPmSoPmdMin = _SchCtpPmSoPmdMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 10),
    _SchCtpPmSoPmdMin_Type()
)
schCtpPmSoPmdMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSoPmdMin.setStatus("current")
_SchCtpPmSoPmdMax_Type = FloatArbitraryPrecision
_SchCtpPmSoPmdMax_Object = MibTableColumn
schCtpPmSoPmdMax = _SchCtpPmSoPmdMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 11),
    _SchCtpPmSoPmdMax_Type()
)
schCtpPmSoPmdMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSoPmdMax.setStatus("current")
_SchCtpPmSoPmdAve_Type = FloatArbitraryPrecision
_SchCtpPmSoPmdAve_Object = MibTableColumn
schCtpPmSoPmdAve = _SchCtpPmSoPmdAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 12),
    _SchCtpPmSoPmdAve_Type()
)
schCtpPmSoPmdAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSoPmdAve.setStatus("current")
_SchCtpPmSchOptMin_Type = FloatHundredths
_SchCtpPmSchOptMin_Object = MibTableColumn
schCtpPmSchOptMin = _SchCtpPmSchOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 13),
    _SchCtpPmSchOptMin_Type()
)
schCtpPmSchOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchOptMin.setStatus("current")
_SchCtpPmSchOptMax_Type = FloatHundredths
_SchCtpPmSchOptMax_Object = MibTableColumn
schCtpPmSchOptMax = _SchCtpPmSchOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 14),
    _SchCtpPmSchOptMax_Type()
)
schCtpPmSchOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchOptMax.setStatus("current")
_SchCtpPmSchOptAve_Type = FloatHundredths
_SchCtpPmSchOptAve_Object = MibTableColumn
schCtpPmSchOptAve = _SchCtpPmSchOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 15),
    _SchCtpPmSchOptAve_Type()
)
schCtpPmSchOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchOptAve.setStatus("current")
_SchCtpPmSchEstimatedSpanOptMin_Type = FloatHundredths
_SchCtpPmSchEstimatedSpanOptMin_Object = MibTableColumn
schCtpPmSchEstimatedSpanOptMin = _SchCtpPmSchEstimatedSpanOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 16),
    _SchCtpPmSchEstimatedSpanOptMin_Type()
)
schCtpPmSchEstimatedSpanOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchEstimatedSpanOptMin.setStatus("current")
_SchCtpPmSchEstimatedSpanOptMax_Type = FloatHundredths
_SchCtpPmSchEstimatedSpanOptMax_Object = MibTableColumn
schCtpPmSchEstimatedSpanOptMax = _SchCtpPmSchEstimatedSpanOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 17),
    _SchCtpPmSchEstimatedSpanOptMax_Type()
)
schCtpPmSchEstimatedSpanOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchEstimatedSpanOptMax.setStatus("current")
_SchCtpPmSchEstimatedSpanOptAve_Type = FloatHundredths
_SchCtpPmSchEstimatedSpanOptAve_Object = MibTableColumn
schCtpPmSchEstimatedSpanOptAve = _SchCtpPmSchEstimatedSpanOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 18),
    _SchCtpPmSchEstimatedSpanOptAve_Type()
)
schCtpPmSchEstimatedSpanOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchEstimatedSpanOptAve.setStatus("current")
_SchCtpPmSchTargetSpanOptMin_Type = FloatHundredths
_SchCtpPmSchTargetSpanOptMin_Object = MibTableColumn
schCtpPmSchTargetSpanOptMin = _SchCtpPmSchTargetSpanOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 19),
    _SchCtpPmSchTargetSpanOptMin_Type()
)
schCtpPmSchTargetSpanOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchTargetSpanOptMin.setStatus("current")
_SchCtpPmSchTargetSpanOptMax_Type = FloatHundredths
_SchCtpPmSchTargetSpanOptMax_Object = MibTableColumn
schCtpPmSchTargetSpanOptMax = _SchCtpPmSchTargetSpanOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 20),
    _SchCtpPmSchTargetSpanOptMax_Type()
)
schCtpPmSchTargetSpanOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchTargetSpanOptMax.setStatus("current")
_SchCtpPmSchTargetSpanOptAve_Type = FloatHundredths
_SchCtpPmSchTargetSpanOptAve_Object = MibTableColumn
schCtpPmSchTargetSpanOptAve = _SchCtpPmSchTargetSpanOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 21),
    _SchCtpPmSchTargetSpanOptAve_Type()
)
schCtpPmSchTargetSpanOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchTargetSpanOptAve.setStatus("current")
_SchCtpPmSchOprMin_Type = FloatHundredths
_SchCtpPmSchOprMin_Object = MibTableColumn
schCtpPmSchOprMin = _SchCtpPmSchOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 22),
    _SchCtpPmSchOprMin_Type()
)
schCtpPmSchOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchOprMin.setStatus("current")
_SchCtpPmSchOprMax_Type = FloatHundredths
_SchCtpPmSchOprMax_Object = MibTableColumn
schCtpPmSchOprMax = _SchCtpPmSchOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 23),
    _SchCtpPmSchOprMax_Type()
)
schCtpPmSchOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchOprMax.setStatus("current")
_SchCtpPmSchOprAve_Type = FloatHundredths
_SchCtpPmSchOprAve_Object = MibTableColumn
schCtpPmSchOprAve = _SchCtpPmSchOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 2, 1, 24),
    _SchCtpPmSchOprAve_Type()
)
schCtpPmSchOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    schCtpPmSchOprAve.setStatus("current")
_SchCtpPmConformance_ObjectIdentity = ObjectIdentity
schCtpPmConformance = _SchCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 3)
)
_SchCtpPmCompliances_ObjectIdentity = ObjectIdentity
schCtpPmCompliances = _SchCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 3, 1)
)
_SchCtpPmGroups_ObjectIdentity = ObjectIdentity
schCtpPmGroups = _SchCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 3, 2)
)

# Managed Objects groups

schCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 3, 2, 1)
)
schCtpPmGroup.setObjects(
      *(("INFINERA-PM-SCHCTP-MIB", "schCtpPmValidity"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmChanSchOptMin"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmChanSchOptMax"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmChanSchOptAve"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmPmdMin"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmPmdMax"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmPmdAve"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSoPmdMin"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSoPmdMax"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSoPmdAve"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchOptMin"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchOptMax"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchOptAve"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchEstimatedSpanOptMin"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchEstimatedSpanOptMax"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchEstimatedSpanOptAve"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchTargetSpanOptMin"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchTargetSpanOptMax"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchTargetSpanOptAve"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchOprMin"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchOprMax"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmSchOprAve"))
)
if mibBuilder.loadTexts:
    schCtpPmGroup.setStatus("current")

schCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 3, 2, 2)
)
schCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-SCHCTP-MIB", "schCtpPmRealChanSchOpt"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmRealPmd"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmRealSoPmd"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmRealSchOpt"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmRealSchEstimatedSpanOpt"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmRealSchTargetSpanOpt"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmRealSchOpr"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmRealLastPollTimeStampOpt"),
        ("INFINERA-PM-SCHCTP-MIB", "schCtpPmRealLastPollTimeStampOpr"))
)
if mibBuilder.loadTexts:
    schCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

schCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 3, 1, 1)
)
schCtpPmCompliance.setObjects(
    ("INFINERA-PM-SCHCTP-MIB", "schCtpPmGroup")
)
if mibBuilder.loadTexts:
    schCtpPmCompliance.setStatus(
        "current"
    )

schCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 38, 3, 1, 2)
)
schCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-SCHCTP-MIB", "schCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    schCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-SCHCTP-MIB",
    **{"schCtpPmMIB": schCtpPmMIB,
       "schCtpPmRealTable": schCtpPmRealTable,
       "schCtpPmRealEntry": schCtpPmRealEntry,
       "schCtpPmRealChanSchOpt": schCtpPmRealChanSchOpt,
       "schCtpPmRealPmd": schCtpPmRealPmd,
       "schCtpPmRealSoPmd": schCtpPmRealSoPmd,
       "schCtpPmRealSchOpt": schCtpPmRealSchOpt,
       "schCtpPmRealSchEstimatedSpanOpt": schCtpPmRealSchEstimatedSpanOpt,
       "schCtpPmRealSchTargetSpanOpt": schCtpPmRealSchTargetSpanOpt,
       "schCtpPmRealSchOpr": schCtpPmRealSchOpr,
       "schCtpPmRealLastPollTimeStampOpt": schCtpPmRealLastPollTimeStampOpt,
       "schCtpPmRealLastPollTimeStampOpr": schCtpPmRealLastPollTimeStampOpr,
       "schCtpPmTable": schCtpPmTable,
       "schCtpPmEntry": schCtpPmEntry,
       "schCtpPmTimestamp": schCtpPmTimestamp,
       "schCtpPmSampleDuration": schCtpPmSampleDuration,
       "schCtpPmValidity": schCtpPmValidity,
       "schCtpPmChanSchOptMin": schCtpPmChanSchOptMin,
       "schCtpPmChanSchOptMax": schCtpPmChanSchOptMax,
       "schCtpPmChanSchOptAve": schCtpPmChanSchOptAve,
       "schCtpPmPmdMin": schCtpPmPmdMin,
       "schCtpPmPmdMax": schCtpPmPmdMax,
       "schCtpPmPmdAve": schCtpPmPmdAve,
       "schCtpPmSoPmdMin": schCtpPmSoPmdMin,
       "schCtpPmSoPmdMax": schCtpPmSoPmdMax,
       "schCtpPmSoPmdAve": schCtpPmSoPmdAve,
       "schCtpPmSchOptMin": schCtpPmSchOptMin,
       "schCtpPmSchOptMax": schCtpPmSchOptMax,
       "schCtpPmSchOptAve": schCtpPmSchOptAve,
       "schCtpPmSchEstimatedSpanOptMin": schCtpPmSchEstimatedSpanOptMin,
       "schCtpPmSchEstimatedSpanOptMax": schCtpPmSchEstimatedSpanOptMax,
       "schCtpPmSchEstimatedSpanOptAve": schCtpPmSchEstimatedSpanOptAve,
       "schCtpPmSchTargetSpanOptMin": schCtpPmSchTargetSpanOptMin,
       "schCtpPmSchTargetSpanOptMax": schCtpPmSchTargetSpanOptMax,
       "schCtpPmSchTargetSpanOptAve": schCtpPmSchTargetSpanOptAve,
       "schCtpPmSchOprMin": schCtpPmSchOprMin,
       "schCtpPmSchOprMax": schCtpPmSchOprMax,
       "schCtpPmSchOprAve": schCtpPmSchOprAve,
       "schCtpPmConformance": schCtpPmConformance,
       "schCtpPmCompliances": schCtpPmCompliances,
       "schCtpPmCompliance": schCtpPmCompliance,
       "schCtpPmRealCompliance": schCtpPmRealCompliance,
       "schCtpPmGroups": schCtpPmGroups,
       "schCtpPmGroup": schCtpPmGroup,
       "schCtpPmRealGroup": schCtpPmRealGroup}
)
