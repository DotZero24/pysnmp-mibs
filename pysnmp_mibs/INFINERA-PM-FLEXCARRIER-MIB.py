# SNMP MIB module (INFINERA-PM-FLEXCARRIER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-FLEXCARRIER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:31 2025
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

(FloatHundredths,
 InfnSampleDuration) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnSampleDuration")

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

flexCarrierPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60)
)
if mibBuilder.loadTexts:
    flexCarrierPmMIB.setRevisions(
        ("2015-04-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FlexCarrierPmRealTable_Object = MibTable
flexCarrierPmRealTable = _FlexCarrierPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 1)
)
if mibBuilder.loadTexts:
    flexCarrierPmRealTable.setStatus("current")
_FlexCarrierPmRealEntry_Object = MibTableRow
flexCarrierPmRealEntry = _FlexCarrierPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 1, 1)
)
flexCarrierPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    flexCarrierPmRealEntry.setStatus("current")
_FlexCarrierPmRealCmnScgOpt_Type = FloatHundredths
_FlexCarrierPmRealCmnScgOpt_Object = MibTableColumn
flexCarrierPmRealCmnScgOpt = _FlexCarrierPmRealCmnScgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 1, 1, 1),
    _FlexCarrierPmRealCmnScgOpt_Type()
)
flexCarrierPmRealCmnScgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmRealCmnScgOpt.setStatus("current")
_FlexCarrierPmRealCmnScgOpr_Type = FloatHundredths
_FlexCarrierPmRealCmnScgOpr_Object = MibTableColumn
flexCarrierPmRealCmnScgOpr = _FlexCarrierPmRealCmnScgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 1, 1, 2),
    _FlexCarrierPmRealCmnScgOpr_Type()
)
flexCarrierPmRealCmnScgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmRealCmnScgOpr.setStatus("current")
_FlexCarrierPmRealLastPollTimeStampOpt_Type = Integer32
_FlexCarrierPmRealLastPollTimeStampOpt_Object = MibTableColumn
flexCarrierPmRealLastPollTimeStampOpt = _FlexCarrierPmRealLastPollTimeStampOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 1, 1, 3),
    _FlexCarrierPmRealLastPollTimeStampOpt_Type()
)
flexCarrierPmRealLastPollTimeStampOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmRealLastPollTimeStampOpt.setStatus("current")
_FlexCarrierPmRealLastPollTimeStampOpr_Type = Integer32
_FlexCarrierPmRealLastPollTimeStampOpr_Object = MibTableColumn
flexCarrierPmRealLastPollTimeStampOpr = _FlexCarrierPmRealLastPollTimeStampOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 1, 1, 4),
    _FlexCarrierPmRealLastPollTimeStampOpr_Type()
)
flexCarrierPmRealLastPollTimeStampOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmRealLastPollTimeStampOpr.setStatus("current")
_FlexCarrierPmTable_Object = MibTable
flexCarrierPmTable = _FlexCarrierPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2)
)
if mibBuilder.loadTexts:
    flexCarrierPmTable.setStatus("current")
_FlexCarrierPmEntry_Object = MibTableRow
flexCarrierPmEntry = _FlexCarrierPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2, 1)
)
flexCarrierPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmSampleDuration"),
    (0, "INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmTimestamp"),
)
if mibBuilder.loadTexts:
    flexCarrierPmEntry.setStatus("current")


class _FlexCarrierPmTimestamp_Type(Integer32):
    """Custom type flexCarrierPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FlexCarrierPmTimestamp_Type.__name__ = "Integer32"
_FlexCarrierPmTimestamp_Object = MibTableColumn
flexCarrierPmTimestamp = _FlexCarrierPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2, 1, 1),
    _FlexCarrierPmTimestamp_Type()
)
flexCarrierPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flexCarrierPmTimestamp.setStatus("current")


class _FlexCarrierPmSampleDuration_Type(Integer32):
    """Custom type flexCarrierPmSampleDuration based on Integer32"""
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


_FlexCarrierPmSampleDuration_Type.__name__ = "Integer32"
_FlexCarrierPmSampleDuration_Object = MibTableColumn
flexCarrierPmSampleDuration = _FlexCarrierPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2, 1, 2),
    _FlexCarrierPmSampleDuration_Type()
)
flexCarrierPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    flexCarrierPmSampleDuration.setStatus("current")
_FlexCarrierPmValidity_Type = TruthValue
_FlexCarrierPmValidity_Object = MibTableColumn
flexCarrierPmValidity = _FlexCarrierPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2, 1, 3),
    _FlexCarrierPmValidity_Type()
)
flexCarrierPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmValidity.setStatus("current")
_FlexCarrierPmCmnScgOptMin_Type = FloatHundredths
_FlexCarrierPmCmnScgOptMin_Object = MibTableColumn
flexCarrierPmCmnScgOptMin = _FlexCarrierPmCmnScgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2, 1, 4),
    _FlexCarrierPmCmnScgOptMin_Type()
)
flexCarrierPmCmnScgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmCmnScgOptMin.setStatus("current")
_FlexCarrierPmCmnScgOptMax_Type = FloatHundredths
_FlexCarrierPmCmnScgOptMax_Object = MibTableColumn
flexCarrierPmCmnScgOptMax = _FlexCarrierPmCmnScgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2, 1, 5),
    _FlexCarrierPmCmnScgOptMax_Type()
)
flexCarrierPmCmnScgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmCmnScgOptMax.setStatus("current")
_FlexCarrierPmCmnScgOptAve_Type = FloatHundredths
_FlexCarrierPmCmnScgOptAve_Object = MibTableColumn
flexCarrierPmCmnScgOptAve = _FlexCarrierPmCmnScgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2, 1, 6),
    _FlexCarrierPmCmnScgOptAve_Type()
)
flexCarrierPmCmnScgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmCmnScgOptAve.setStatus("current")
_FlexCarrierPmCmnScgOprMin_Type = FloatHundredths
_FlexCarrierPmCmnScgOprMin_Object = MibTableColumn
flexCarrierPmCmnScgOprMin = _FlexCarrierPmCmnScgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2, 1, 7),
    _FlexCarrierPmCmnScgOprMin_Type()
)
flexCarrierPmCmnScgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmCmnScgOprMin.setStatus("current")
_FlexCarrierPmCmnScgOprMax_Type = FloatHundredths
_FlexCarrierPmCmnScgOprMax_Object = MibTableColumn
flexCarrierPmCmnScgOprMax = _FlexCarrierPmCmnScgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2, 1, 8),
    _FlexCarrierPmCmnScgOprMax_Type()
)
flexCarrierPmCmnScgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmCmnScgOprMax.setStatus("current")
_FlexCarrierPmCmnScgOprAve_Type = FloatHundredths
_FlexCarrierPmCmnScgOprAve_Object = MibTableColumn
flexCarrierPmCmnScgOprAve = _FlexCarrierPmCmnScgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 2, 1, 9),
    _FlexCarrierPmCmnScgOprAve_Type()
)
flexCarrierPmCmnScgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    flexCarrierPmCmnScgOprAve.setStatus("current")
_FlexCarrierPmConformance_ObjectIdentity = ObjectIdentity
flexCarrierPmConformance = _FlexCarrierPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 3)
)
_FlexCarrierPmCompliances_ObjectIdentity = ObjectIdentity
flexCarrierPmCompliances = _FlexCarrierPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 3, 1)
)
_FlexCarrierPmGroups_ObjectIdentity = ObjectIdentity
flexCarrierPmGroups = _FlexCarrierPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 3, 2)
)

# Managed Objects groups

flexCarrierPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 3, 2, 1)
)
flexCarrierPmGroup.setObjects(
      *(("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmTimestamp"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmSampleDuration"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmValidity"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmCmnScgOptMin"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmCmnScgOptMax"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmCmnScgOptAve"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmCmnScgOprMin"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmCmnScgOprMax"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmCmnScgOprAve"))
)
if mibBuilder.loadTexts:
    flexCarrierPmGroup.setStatus("current")

flexCarrierPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 3, 2, 2)
)
flexCarrierPmRealGroup.setObjects(
      *(("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmRealCmnScgOpt"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmRealCmnScgOpr"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmRealLastPollTimeStampOpt"),
        ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmRealLastPollTimeStampOpr"))
)
if mibBuilder.loadTexts:
    flexCarrierPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

flexCarrierPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 3, 1, 1)
)
flexCarrierPmCompliance.setObjects(
    ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmGroup")
)
if mibBuilder.loadTexts:
    flexCarrierPmCompliance.setStatus(
        "current"
    )

flexCarrierPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 60, 3, 1, 2)
)
flexCarrierPmRealCompliance.setObjects(
    ("INFINERA-PM-FLEXCARRIER-MIB", "flexCarrierPmRealGroup")
)
if mibBuilder.loadTexts:
    flexCarrierPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-FLEXCARRIER-MIB",
    **{"flexCarrierPmMIB": flexCarrierPmMIB,
       "flexCarrierPmRealTable": flexCarrierPmRealTable,
       "flexCarrierPmRealEntry": flexCarrierPmRealEntry,
       "flexCarrierPmRealCmnScgOpt": flexCarrierPmRealCmnScgOpt,
       "flexCarrierPmRealCmnScgOpr": flexCarrierPmRealCmnScgOpr,
       "flexCarrierPmRealLastPollTimeStampOpt": flexCarrierPmRealLastPollTimeStampOpt,
       "flexCarrierPmRealLastPollTimeStampOpr": flexCarrierPmRealLastPollTimeStampOpr,
       "flexCarrierPmTable": flexCarrierPmTable,
       "flexCarrierPmEntry": flexCarrierPmEntry,
       "flexCarrierPmTimestamp": flexCarrierPmTimestamp,
       "flexCarrierPmSampleDuration": flexCarrierPmSampleDuration,
       "flexCarrierPmValidity": flexCarrierPmValidity,
       "flexCarrierPmCmnScgOptMin": flexCarrierPmCmnScgOptMin,
       "flexCarrierPmCmnScgOptMax": flexCarrierPmCmnScgOptMax,
       "flexCarrierPmCmnScgOptAve": flexCarrierPmCmnScgOptAve,
       "flexCarrierPmCmnScgOprMin": flexCarrierPmCmnScgOprMin,
       "flexCarrierPmCmnScgOprMax": flexCarrierPmCmnScgOprMax,
       "flexCarrierPmCmnScgOprAve": flexCarrierPmCmnScgOprAve,
       "flexCarrierPmConformance": flexCarrierPmConformance,
       "flexCarrierPmCompliances": flexCarrierPmCompliances,
       "flexCarrierPmCompliance": flexCarrierPmCompliance,
       "flexCarrierPmRealCompliance": flexCarrierPmRealCompliance,
       "flexCarrierPmGroups": flexCarrierPmGroups,
       "flexCarrierPmGroup": flexCarrierPmGroup,
       "flexCarrierPmRealGroup": flexCarrierPmRealGroup}
)
