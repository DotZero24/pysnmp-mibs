# SNMP MIB module (INFINERA-PM-CHANNELCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-CHANNELCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:16 2025
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

channelCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3)
)
if mibBuilder.loadTexts:
    channelCtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ChannelCtpPmRealTable_Object = MibTable
channelCtpPmRealTable = _ChannelCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1)
)
if mibBuilder.loadTexts:
    channelCtpPmRealTable.setStatus("current")
_ChannelCtpPmRealEntry_Object = MibTableRow
channelCtpPmRealEntry = _ChannelCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1)
)
channelCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    channelCtpPmRealEntry.setStatus("current")
_ChannelCtpPmRealChanOchOpr_Type = FloatHundredths
_ChannelCtpPmRealChanOchOpr_Object = MibTableColumn
channelCtpPmRealChanOchOpr = _ChannelCtpPmRealChanOchOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 1),
    _ChannelCtpPmRealChanOchOpr_Type()
)
channelCtpPmRealChanOchOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealChanOchOpr.setStatus("current")
_ChannelCtpPmRealChanOchOpt_Type = FloatHundredths
_ChannelCtpPmRealChanOchOpt_Object = MibTableColumn
channelCtpPmRealChanOchOpt = _ChannelCtpPmRealChanOchOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 2),
    _ChannelCtpPmRealChanOchOpt_Type()
)
channelCtpPmRealChanOchOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealChanOchOpt.setStatus("current")
_ChannelCtpPmRealChanOchLBC_Type = FloatHundredths
_ChannelCtpPmRealChanOchLBC_Object = MibTableColumn
channelCtpPmRealChanOchLBC = _ChannelCtpPmRealChanOchLBC_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 3),
    _ChannelCtpPmRealChanOchLBC_Type()
)
channelCtpPmRealChanOchLBC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealChanOchLBC.setStatus("current")
_ChannelCtpPmRealChanOchWavelength_Type = FloatHundredths
_ChannelCtpPmRealChanOchWavelength_Object = MibTableColumn
channelCtpPmRealChanOchWavelength = _ChannelCtpPmRealChanOchWavelength_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 4),
    _ChannelCtpPmRealChanOchWavelength_Type()
)
channelCtpPmRealChanOchWavelength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealChanOchWavelength.setStatus("current")
_ChannelCtpPmRealQFactor_Type = FloatHundredths
_ChannelCtpPmRealQFactor_Object = MibTableColumn
channelCtpPmRealQFactor = _ChannelCtpPmRealQFactor_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 5),
    _ChannelCtpPmRealQFactor_Type()
)
channelCtpPmRealQFactor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealQFactor.setStatus("current")
_ChannelCtpPmRealBerPreFec_Type = FloatArbitraryPrecision
_ChannelCtpPmRealBerPreFec_Object = MibTableColumn
channelCtpPmRealBerPreFec = _ChannelCtpPmRealBerPreFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 6),
    _ChannelCtpPmRealBerPreFec_Type()
)
channelCtpPmRealBerPreFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealBerPreFec.setStatus("current")
_ChannelCtpPmRealBerPostFec_Type = FloatArbitraryPrecision
_ChannelCtpPmRealBerPostFec_Object = MibTableColumn
channelCtpPmRealBerPostFec = _ChannelCtpPmRealBerPostFec_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 7),
    _ChannelCtpPmRealBerPostFec_Type()
)
channelCtpPmRealBerPostFec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealBerPostFec.setStatus("current")
_ChannelCtpPmRealFecCorrectedBits_Type = Counter64
_ChannelCtpPmRealFecCorrectedBits_Object = MibTableColumn
channelCtpPmRealFecCorrectedBits = _ChannelCtpPmRealFecCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 8),
    _ChannelCtpPmRealFecCorrectedBits_Type()
)
channelCtpPmRealFecCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealFecCorrectedBits.setStatus("current")
_ChannelCtpPmRealFecUncorrectedRows_Type = Counter64
_ChannelCtpPmRealFecUncorrectedRows_Object = MibTableColumn
channelCtpPmRealFecUncorrectedRows = _ChannelCtpPmRealFecUncorrectedRows_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 9),
    _ChannelCtpPmRealFecUncorrectedRows_Type()
)
channelCtpPmRealFecUncorrectedRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealFecUncorrectedRows.setStatus("current")
_ChannelCtpPmRealFecTotalCodeWords_Type = Counter64
_ChannelCtpPmRealFecTotalCodeWords_Object = MibTableColumn
channelCtpPmRealFecTotalCodeWords = _ChannelCtpPmRealFecTotalCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 10),
    _ChannelCtpPmRealFecTotalCodeWords_Type()
)
channelCtpPmRealFecTotalCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealFecTotalCodeWords.setStatus("current")
_ChannelCtpPmRealOchDtsCV_Type = Counter64
_ChannelCtpPmRealOchDtsCV_Object = MibTableColumn
channelCtpPmRealOchDtsCV = _ChannelCtpPmRealOchDtsCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 11),
    _ChannelCtpPmRealOchDtsCV_Type()
)
channelCtpPmRealOchDtsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealOchDtsCV.setStatus("current")
_ChannelCtpPmRealOchDtsES_Type = Integer32
_ChannelCtpPmRealOchDtsES_Object = MibTableColumn
channelCtpPmRealOchDtsES = _ChannelCtpPmRealOchDtsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 12),
    _ChannelCtpPmRealOchDtsES_Type()
)
channelCtpPmRealOchDtsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealOchDtsES.setStatus("current")
_ChannelCtpPmRealOchDtsSES_Type = Integer32
_ChannelCtpPmRealOchDtsSES_Object = MibTableColumn
channelCtpPmRealOchDtsSES = _ChannelCtpPmRealOchDtsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 13),
    _ChannelCtpPmRealOchDtsSES_Type()
)
channelCtpPmRealOchDtsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealOchDtsSES.setStatus("current")
_ChannelCtpPmRealPrbsSyncErr_Type = Integer32
_ChannelCtpPmRealPrbsSyncErr_Object = MibTableColumn
channelCtpPmRealPrbsSyncErr = _ChannelCtpPmRealPrbsSyncErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 14),
    _ChannelCtpPmRealPrbsSyncErr_Type()
)
channelCtpPmRealPrbsSyncErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealPrbsSyncErr.setStatus("current")
_ChannelCtpPmRealPrbsErr_Type = Integer32
_ChannelCtpPmRealPrbsErr_Object = MibTableColumn
channelCtpPmRealPrbsErr = _ChannelCtpPmRealPrbsErr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 1, 1, 15),
    _ChannelCtpPmRealPrbsErr_Type()
)
channelCtpPmRealPrbsErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmRealPrbsErr.setStatus("current")
_ChannelCtpPmTable_Object = MibTable
channelCtpPmTable = _ChannelCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2)
)
if mibBuilder.loadTexts:
    channelCtpPmTable.setStatus("current")
_ChannelCtpPmEntry_Object = MibTableRow
channelCtpPmEntry = _ChannelCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1)
)
channelCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmSampleDuration"),
    (0, "INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    channelCtpPmEntry.setStatus("current")


class _ChannelCtpPmTimestamp_Type(Integer32):
    """Custom type channelCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ChannelCtpPmTimestamp_Type.__name__ = "Integer32"
_ChannelCtpPmTimestamp_Object = MibTableColumn
channelCtpPmTimestamp = _ChannelCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 1),
    _ChannelCtpPmTimestamp_Type()
)
channelCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelCtpPmTimestamp.setStatus("current")


class _ChannelCtpPmSampleDuration_Type(Integer32):
    """Custom type channelCtpPmSampleDuration based on Integer32"""
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


_ChannelCtpPmSampleDuration_Type.__name__ = "Integer32"
_ChannelCtpPmSampleDuration_Object = MibTableColumn
channelCtpPmSampleDuration = _ChannelCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 2),
    _ChannelCtpPmSampleDuration_Type()
)
channelCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    channelCtpPmSampleDuration.setStatus("current")
_ChannelCtpPmValidity_Type = TruthValue
_ChannelCtpPmValidity_Object = MibTableColumn
channelCtpPmValidity = _ChannelCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 3),
    _ChannelCtpPmValidity_Type()
)
channelCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmValidity.setStatus("current")
_ChannelCtpPmChanOchOprMin_Type = FloatHundredths
_ChannelCtpPmChanOchOprMin_Object = MibTableColumn
channelCtpPmChanOchOprMin = _ChannelCtpPmChanOchOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 4),
    _ChannelCtpPmChanOchOprMin_Type()
)
channelCtpPmChanOchOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchOprMin.setStatus("current")
_ChannelCtpPmChanOchOprMax_Type = FloatHundredths
_ChannelCtpPmChanOchOprMax_Object = MibTableColumn
channelCtpPmChanOchOprMax = _ChannelCtpPmChanOchOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 5),
    _ChannelCtpPmChanOchOprMax_Type()
)
channelCtpPmChanOchOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchOprMax.setStatus("current")
_ChannelCtpPmChanOchOprAve_Type = FloatHundredths
_ChannelCtpPmChanOchOprAve_Object = MibTableColumn
channelCtpPmChanOchOprAve = _ChannelCtpPmChanOchOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 6),
    _ChannelCtpPmChanOchOprAve_Type()
)
channelCtpPmChanOchOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchOprAve.setStatus("current")
_ChannelCtpPmChanOchOptMin_Type = FloatHundredths
_ChannelCtpPmChanOchOptMin_Object = MibTableColumn
channelCtpPmChanOchOptMin = _ChannelCtpPmChanOchOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 7),
    _ChannelCtpPmChanOchOptMin_Type()
)
channelCtpPmChanOchOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchOptMin.setStatus("current")
_ChannelCtpPmChanOchOptMax_Type = FloatHundredths
_ChannelCtpPmChanOchOptMax_Object = MibTableColumn
channelCtpPmChanOchOptMax = _ChannelCtpPmChanOchOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 8),
    _ChannelCtpPmChanOchOptMax_Type()
)
channelCtpPmChanOchOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchOptMax.setStatus("current")
_ChannelCtpPmChanOchOptAve_Type = FloatHundredths
_ChannelCtpPmChanOchOptAve_Object = MibTableColumn
channelCtpPmChanOchOptAve = _ChannelCtpPmChanOchOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 9),
    _ChannelCtpPmChanOchOptAve_Type()
)
channelCtpPmChanOchOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchOptAve.setStatus("current")
_ChannelCtpPmChanOchLBCMin_Type = FloatHundredths
_ChannelCtpPmChanOchLBCMin_Object = MibTableColumn
channelCtpPmChanOchLBCMin = _ChannelCtpPmChanOchLBCMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 10),
    _ChannelCtpPmChanOchLBCMin_Type()
)
channelCtpPmChanOchLBCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchLBCMin.setStatus("current")
_ChannelCtpPmChanOchLBCMax_Type = FloatHundredths
_ChannelCtpPmChanOchLBCMax_Object = MibTableColumn
channelCtpPmChanOchLBCMax = _ChannelCtpPmChanOchLBCMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 11),
    _ChannelCtpPmChanOchLBCMax_Type()
)
channelCtpPmChanOchLBCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchLBCMax.setStatus("current")
_ChannelCtpPmChanOchLBCAve_Type = FloatHundredths
_ChannelCtpPmChanOchLBCAve_Object = MibTableColumn
channelCtpPmChanOchLBCAve = _ChannelCtpPmChanOchLBCAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 12),
    _ChannelCtpPmChanOchLBCAve_Type()
)
channelCtpPmChanOchLBCAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchLBCAve.setStatus("current")
_ChannelCtpPmFecCorrectedBits_Type = HCPerfIntervalCount
_ChannelCtpPmFecCorrectedBits_Object = MibTableColumn
channelCtpPmFecCorrectedBits = _ChannelCtpPmFecCorrectedBits_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 13),
    _ChannelCtpPmFecCorrectedBits_Type()
)
channelCtpPmFecCorrectedBits.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmFecCorrectedBits.setStatus("current")
_ChannelCtpPmFecUncorrectedRows_Type = HCPerfIntervalCount
_ChannelCtpPmFecUncorrectedRows_Object = MibTableColumn
channelCtpPmFecUncorrectedRows = _ChannelCtpPmFecUncorrectedRows_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 14),
    _ChannelCtpPmFecUncorrectedRows_Type()
)
channelCtpPmFecUncorrectedRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmFecUncorrectedRows.setStatus("current")
_ChannelCtpPmFecTotalCodeWords_Type = HCPerfIntervalCount
_ChannelCtpPmFecTotalCodeWords_Object = MibTableColumn
channelCtpPmFecTotalCodeWords = _ChannelCtpPmFecTotalCodeWords_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 15),
    _ChannelCtpPmFecTotalCodeWords_Type()
)
channelCtpPmFecTotalCodeWords.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmFecTotalCodeWords.setStatus("current")
_ChannelCtpPmOchDtsCV_Type = HCPerfIntervalCount
_ChannelCtpPmOchDtsCV_Object = MibTableColumn
channelCtpPmOchDtsCV = _ChannelCtpPmOchDtsCV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 16),
    _ChannelCtpPmOchDtsCV_Type()
)
channelCtpPmOchDtsCV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmOchDtsCV.setStatus("current")
_ChannelCtpPmOchDtsES_Type = Integer32
_ChannelCtpPmOchDtsES_Object = MibTableColumn
channelCtpPmOchDtsES = _ChannelCtpPmOchDtsES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 17),
    _ChannelCtpPmOchDtsES_Type()
)
channelCtpPmOchDtsES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmOchDtsES.setStatus("current")
_ChannelCtpPmOchDtsSES_Type = Integer32
_ChannelCtpPmOchDtsSES_Object = MibTableColumn
channelCtpPmOchDtsSES = _ChannelCtpPmOchDtsSES_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 18),
    _ChannelCtpPmOchDtsSES_Type()
)
channelCtpPmOchDtsSES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmOchDtsSES.setStatus("current")
_ChannelCtpPmChanOchQValueMin_Type = FloatHundredths
_ChannelCtpPmChanOchQValueMin_Object = MibTableColumn
channelCtpPmChanOchQValueMin = _ChannelCtpPmChanOchQValueMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 19),
    _ChannelCtpPmChanOchQValueMin_Type()
)
channelCtpPmChanOchQValueMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchQValueMin.setStatus("current")
_ChannelCtpPmChanOchQValueMax_Type = FloatHundredths
_ChannelCtpPmChanOchQValueMax_Object = MibTableColumn
channelCtpPmChanOchQValueMax = _ChannelCtpPmChanOchQValueMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 20),
    _ChannelCtpPmChanOchQValueMax_Type()
)
channelCtpPmChanOchQValueMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchQValueMax.setStatus("current")
_ChannelCtpPmChanOchQValueAve_Type = FloatHundredths
_ChannelCtpPmChanOchQValueAve_Object = MibTableColumn
channelCtpPmChanOchQValueAve = _ChannelCtpPmChanOchQValueAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 2, 1, 21),
    _ChannelCtpPmChanOchQValueAve_Type()
)
channelCtpPmChanOchQValueAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    channelCtpPmChanOchQValueAve.setStatus("current")
_ChannelCtpPmConformance_ObjectIdentity = ObjectIdentity
channelCtpPmConformance = _ChannelCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 3)
)
_ChannelCtpPmCompliances_ObjectIdentity = ObjectIdentity
channelCtpPmCompliances = _ChannelCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 3, 1)
)
_ChannelCtpPmGroups_ObjectIdentity = ObjectIdentity
channelCtpPmGroups = _ChannelCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 3, 2)
)

# Managed Objects groups

channelCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 3, 2, 1)
)
channelCtpPmGroup.setObjects(
      *(("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmValidity"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchOprMin"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchOprMax"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchOprAve"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchOptMin"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchOptMax"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchOptAve"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchLBCMin"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchLBCMax"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchLBCAve"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmFecCorrectedBits"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmFecUncorrectedRows"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmFecTotalCodeWords"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmOchDtsCV"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmOchDtsES"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmOchDtsSES"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchQValueMin"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchQValueMax"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmChanOchQValueAve"))
)
if mibBuilder.loadTexts:
    channelCtpPmGroup.setStatus("current")

channelCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 3, 2, 2)
)
channelCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealChanOchOpr"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealChanOchOpt"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealChanOchLBC"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealChanOchWavelength"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealQFactor"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealBerPreFec"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealBerPostFec"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealFecCorrectedBits"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealFecUncorrectedRows"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealFecTotalCodeWords"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealOchDtsCV"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealOchDtsES"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealOchDtsSES"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealPrbsSyncErr"),
        ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealPrbsErr"))
)
if mibBuilder.loadTexts:
    channelCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

channelCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 3, 1, 1)
)
channelCtpPmCompliance.setObjects(
    ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmGroup")
)
if mibBuilder.loadTexts:
    channelCtpPmCompliance.setStatus(
        "current"
    )

channelCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 3, 3, 1, 2)
)
channelCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-CHANNELCTP-MIB", "channelCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    channelCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-CHANNELCTP-MIB",
    **{"channelCtpPmMIB": channelCtpPmMIB,
       "channelCtpPmRealTable": channelCtpPmRealTable,
       "channelCtpPmRealEntry": channelCtpPmRealEntry,
       "channelCtpPmRealChanOchOpr": channelCtpPmRealChanOchOpr,
       "channelCtpPmRealChanOchOpt": channelCtpPmRealChanOchOpt,
       "channelCtpPmRealChanOchLBC": channelCtpPmRealChanOchLBC,
       "channelCtpPmRealChanOchWavelength": channelCtpPmRealChanOchWavelength,
       "channelCtpPmRealQFactor": channelCtpPmRealQFactor,
       "channelCtpPmRealBerPreFec": channelCtpPmRealBerPreFec,
       "channelCtpPmRealBerPostFec": channelCtpPmRealBerPostFec,
       "channelCtpPmRealFecCorrectedBits": channelCtpPmRealFecCorrectedBits,
       "channelCtpPmRealFecUncorrectedRows": channelCtpPmRealFecUncorrectedRows,
       "channelCtpPmRealFecTotalCodeWords": channelCtpPmRealFecTotalCodeWords,
       "channelCtpPmRealOchDtsCV": channelCtpPmRealOchDtsCV,
       "channelCtpPmRealOchDtsES": channelCtpPmRealOchDtsES,
       "channelCtpPmRealOchDtsSES": channelCtpPmRealOchDtsSES,
       "channelCtpPmRealPrbsSyncErr": channelCtpPmRealPrbsSyncErr,
       "channelCtpPmRealPrbsErr": channelCtpPmRealPrbsErr,
       "channelCtpPmTable": channelCtpPmTable,
       "channelCtpPmEntry": channelCtpPmEntry,
       "channelCtpPmTimestamp": channelCtpPmTimestamp,
       "channelCtpPmSampleDuration": channelCtpPmSampleDuration,
       "channelCtpPmValidity": channelCtpPmValidity,
       "channelCtpPmChanOchOprMin": channelCtpPmChanOchOprMin,
       "channelCtpPmChanOchOprMax": channelCtpPmChanOchOprMax,
       "channelCtpPmChanOchOprAve": channelCtpPmChanOchOprAve,
       "channelCtpPmChanOchOptMin": channelCtpPmChanOchOptMin,
       "channelCtpPmChanOchOptMax": channelCtpPmChanOchOptMax,
       "channelCtpPmChanOchOptAve": channelCtpPmChanOchOptAve,
       "channelCtpPmChanOchLBCMin": channelCtpPmChanOchLBCMin,
       "channelCtpPmChanOchLBCMax": channelCtpPmChanOchLBCMax,
       "channelCtpPmChanOchLBCAve": channelCtpPmChanOchLBCAve,
       "channelCtpPmFecCorrectedBits": channelCtpPmFecCorrectedBits,
       "channelCtpPmFecUncorrectedRows": channelCtpPmFecUncorrectedRows,
       "channelCtpPmFecTotalCodeWords": channelCtpPmFecTotalCodeWords,
       "channelCtpPmOchDtsCV": channelCtpPmOchDtsCV,
       "channelCtpPmOchDtsES": channelCtpPmOchDtsES,
       "channelCtpPmOchDtsSES": channelCtpPmOchDtsSES,
       "channelCtpPmChanOchQValueMin": channelCtpPmChanOchQValueMin,
       "channelCtpPmChanOchQValueMax": channelCtpPmChanOchQValueMax,
       "channelCtpPmChanOchQValueAve": channelCtpPmChanOchQValueAve,
       "channelCtpPmConformance": channelCtpPmConformance,
       "channelCtpPmCompliances": channelCtpPmCompliances,
       "channelCtpPmCompliance": channelCtpPmCompliance,
       "channelCtpPmRealCompliance": channelCtpPmRealCompliance,
       "channelCtpPmGroups": channelCtpPmGroups,
       "channelCtpPmGroup": channelCtpPmGroup,
       "channelCtpPmRealGroup": channelCtpPmRealGroup}
)
