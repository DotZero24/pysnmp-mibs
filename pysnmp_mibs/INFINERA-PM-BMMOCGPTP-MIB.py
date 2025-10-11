# SNMP MIB module (INFINERA-PM-BMMOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-BMMOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:04 2025
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

(FloatHundredths,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
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

bmmOcgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2)
)
if mibBuilder.loadTexts:
    bmmOcgPtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BmmOcgPtpPmRealTable_Object = MibTable
bmmOcgPtpPmRealTable = _BmmOcgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 1)
)
if mibBuilder.loadTexts:
    bmmOcgPtpPmRealTable.setStatus("current")
_BmmOcgPtpPmRealEntry_Object = MibTableRow
bmmOcgPtpPmRealEntry = _BmmOcgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 1, 1)
)
bmmOcgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bmmOcgPtpPmRealEntry.setStatus("current")
_BmmOcgPtpPmRealBmmOcgOpt_Type = FloatHundredths
_BmmOcgPtpPmRealBmmOcgOpt_Object = MibTableColumn
bmmOcgPtpPmRealBmmOcgOpt = _BmmOcgPtpPmRealBmmOcgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 1, 1, 1),
    _BmmOcgPtpPmRealBmmOcgOpt_Type()
)
bmmOcgPtpPmRealBmmOcgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpPmRealBmmOcgOpt.setStatus("current")
_BmmOcgPtpPmRealBmmOcgOpr_Type = FloatHundredths
_BmmOcgPtpPmRealBmmOcgOpr_Object = MibTableColumn
bmmOcgPtpPmRealBmmOcgOpr = _BmmOcgPtpPmRealBmmOcgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 1, 1, 2),
    _BmmOcgPtpPmRealBmmOcgOpr_Type()
)
bmmOcgPtpPmRealBmmOcgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpPmRealBmmOcgOpr.setStatus("current")
_BmmOcgPtpPmTable_Object = MibTable
bmmOcgPtpPmTable = _BmmOcgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2)
)
if mibBuilder.loadTexts:
    bmmOcgPtpPmTable.setStatus("current")
_BmmOcgPtpPmEntry_Object = MibTableRow
bmmOcgPtpPmEntry = _BmmOcgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2, 1)
)
bmmOcgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmSampleDuration"),
    (0, "INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    bmmOcgPtpPmEntry.setStatus("current")


class _BmmOcgPtpPmTimestamp_Type(Integer32):
    """Custom type bmmOcgPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_BmmOcgPtpPmTimestamp_Type.__name__ = "Integer32"
_BmmOcgPtpPmTimestamp_Object = MibTableColumn
bmmOcgPtpPmTimestamp = _BmmOcgPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2, 1, 1),
    _BmmOcgPtpPmTimestamp_Type()
)
bmmOcgPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bmmOcgPtpPmTimestamp.setStatus("current")


class _BmmOcgPtpPmSampleDuration_Type(Integer32):
    """Custom type bmmOcgPtpPmSampleDuration based on Integer32"""
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


_BmmOcgPtpPmSampleDuration_Type.__name__ = "Integer32"
_BmmOcgPtpPmSampleDuration_Object = MibTableColumn
bmmOcgPtpPmSampleDuration = _BmmOcgPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2, 1, 2),
    _BmmOcgPtpPmSampleDuration_Type()
)
bmmOcgPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bmmOcgPtpPmSampleDuration.setStatus("current")
_BmmOcgPtpPmValidity_Type = TruthValue
_BmmOcgPtpPmValidity_Object = MibTableColumn
bmmOcgPtpPmValidity = _BmmOcgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2, 1, 3),
    _BmmOcgPtpPmValidity_Type()
)
bmmOcgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpPmValidity.setStatus("current")
_BmmOcgPtpPmBmmOcgOptMin_Type = FloatHundredths
_BmmOcgPtpPmBmmOcgOptMin_Object = MibTableColumn
bmmOcgPtpPmBmmOcgOptMin = _BmmOcgPtpPmBmmOcgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2, 1, 4),
    _BmmOcgPtpPmBmmOcgOptMin_Type()
)
bmmOcgPtpPmBmmOcgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpPmBmmOcgOptMin.setStatus("current")
_BmmOcgPtpPmBmmOcgOptMax_Type = FloatHundredths
_BmmOcgPtpPmBmmOcgOptMax_Object = MibTableColumn
bmmOcgPtpPmBmmOcgOptMax = _BmmOcgPtpPmBmmOcgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2, 1, 5),
    _BmmOcgPtpPmBmmOcgOptMax_Type()
)
bmmOcgPtpPmBmmOcgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpPmBmmOcgOptMax.setStatus("current")
_BmmOcgPtpPmBmmOcgOptAve_Type = FloatHundredths
_BmmOcgPtpPmBmmOcgOptAve_Object = MibTableColumn
bmmOcgPtpPmBmmOcgOptAve = _BmmOcgPtpPmBmmOcgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2, 1, 6),
    _BmmOcgPtpPmBmmOcgOptAve_Type()
)
bmmOcgPtpPmBmmOcgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpPmBmmOcgOptAve.setStatus("current")
_BmmOcgPtpPmBmmOcgOprMin_Type = FloatHundredths
_BmmOcgPtpPmBmmOcgOprMin_Object = MibTableColumn
bmmOcgPtpPmBmmOcgOprMin = _BmmOcgPtpPmBmmOcgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2, 1, 7),
    _BmmOcgPtpPmBmmOcgOprMin_Type()
)
bmmOcgPtpPmBmmOcgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpPmBmmOcgOprMin.setStatus("current")
_BmmOcgPtpPmBmmOcgOprMax_Type = FloatHundredths
_BmmOcgPtpPmBmmOcgOprMax_Object = MibTableColumn
bmmOcgPtpPmBmmOcgOprMax = _BmmOcgPtpPmBmmOcgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2, 1, 8),
    _BmmOcgPtpPmBmmOcgOprMax_Type()
)
bmmOcgPtpPmBmmOcgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpPmBmmOcgOprMax.setStatus("current")
_BmmOcgPtpPmBmmOcgOprAve_Type = FloatHundredths
_BmmOcgPtpPmBmmOcgOprAve_Object = MibTableColumn
bmmOcgPtpPmBmmOcgOprAve = _BmmOcgPtpPmBmmOcgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 2, 1, 9),
    _BmmOcgPtpPmBmmOcgOprAve_Type()
)
bmmOcgPtpPmBmmOcgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bmmOcgPtpPmBmmOcgOprAve.setStatus("current")
_BmmOcgPtpPmConformance_ObjectIdentity = ObjectIdentity
bmmOcgPtpPmConformance = _BmmOcgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 3)
)
_BmmOcgPtpPmCompliances_ObjectIdentity = ObjectIdentity
bmmOcgPtpPmCompliances = _BmmOcgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 3, 1)
)
_BmmOcgPtpPmGroups_ObjectIdentity = ObjectIdentity
bmmOcgPtpPmGroups = _BmmOcgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 3, 2)
)

# Managed Objects groups

bmmOcgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 3, 2, 1)
)
bmmOcgPtpPmGroup.setObjects(
      *(("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmValidity"),
        ("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmBmmOcgOptMin"),
        ("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmBmmOcgOptMax"),
        ("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmBmmOcgOptAve"),
        ("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmBmmOcgOprMin"),
        ("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmBmmOcgOprMax"),
        ("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmBmmOcgOprAve"))
)
if mibBuilder.loadTexts:
    bmmOcgPtpPmGroup.setStatus("current")

bmmOcgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 3, 2, 2)
)
bmmOcgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmRealBmmOcgOpt"),
        ("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmRealBmmOcgOpr"))
)
if mibBuilder.loadTexts:
    bmmOcgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bmmOcgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 3, 1, 1)
)
bmmOcgPtpPmCompliance.setObjects(
    ("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmGroup")
)
if mibBuilder.loadTexts:
    bmmOcgPtpPmCompliance.setStatus(
        "current"
    )

bmmOcgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 2, 3, 1, 2)
)
bmmOcgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-BMMOCGPTP-MIB", "bmmOcgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    bmmOcgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-BMMOCGPTP-MIB",
    **{"bmmOcgPtpPmMIB": bmmOcgPtpPmMIB,
       "bmmOcgPtpPmRealTable": bmmOcgPtpPmRealTable,
       "bmmOcgPtpPmRealEntry": bmmOcgPtpPmRealEntry,
       "bmmOcgPtpPmRealBmmOcgOpt": bmmOcgPtpPmRealBmmOcgOpt,
       "bmmOcgPtpPmRealBmmOcgOpr": bmmOcgPtpPmRealBmmOcgOpr,
       "bmmOcgPtpPmTable": bmmOcgPtpPmTable,
       "bmmOcgPtpPmEntry": bmmOcgPtpPmEntry,
       "bmmOcgPtpPmTimestamp": bmmOcgPtpPmTimestamp,
       "bmmOcgPtpPmSampleDuration": bmmOcgPtpPmSampleDuration,
       "bmmOcgPtpPmValidity": bmmOcgPtpPmValidity,
       "bmmOcgPtpPmBmmOcgOptMin": bmmOcgPtpPmBmmOcgOptMin,
       "bmmOcgPtpPmBmmOcgOptMax": bmmOcgPtpPmBmmOcgOptMax,
       "bmmOcgPtpPmBmmOcgOptAve": bmmOcgPtpPmBmmOcgOptAve,
       "bmmOcgPtpPmBmmOcgOprMin": bmmOcgPtpPmBmmOcgOprMin,
       "bmmOcgPtpPmBmmOcgOprMax": bmmOcgPtpPmBmmOcgOprMax,
       "bmmOcgPtpPmBmmOcgOprAve": bmmOcgPtpPmBmmOcgOprAve,
       "bmmOcgPtpPmConformance": bmmOcgPtpPmConformance,
       "bmmOcgPtpPmCompliances": bmmOcgPtpPmCompliances,
       "bmmOcgPtpPmCompliance": bmmOcgPtpPmCompliance,
       "bmmOcgPtpPmRealCompliance": bmmOcgPtpPmRealCompliance,
       "bmmOcgPtpPmGroups": bmmOcgPtpPmGroups,
       "bmmOcgPtpPmGroup": bmmOcgPtpPmGroup,
       "bmmOcgPtpPmRealGroup": bmmOcgPtpPmRealGroup}
)
