# SNMP MIB module (INFINERA-PM-GAMOCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-GAMOCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:45 2025
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

gamOcgPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7)
)
if mibBuilder.loadTexts:
    gamOcgPtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_GamOcgPtpPmRealTable_Object = MibTable
gamOcgPtpPmRealTable = _GamOcgPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 1)
)
if mibBuilder.loadTexts:
    gamOcgPtpPmRealTable.setStatus("current")
_GamOcgPtpPmRealEntry_Object = MibTableRow
gamOcgPtpPmRealEntry = _GamOcgPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 1, 1)
)
gamOcgPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    gamOcgPtpPmRealEntry.setStatus("current")
_GamOcgPtpPmRealGamOcgOpt_Type = FloatHundredths
_GamOcgPtpPmRealGamOcgOpt_Object = MibTableColumn
gamOcgPtpPmRealGamOcgOpt = _GamOcgPtpPmRealGamOcgOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 1, 1, 1),
    _GamOcgPtpPmRealGamOcgOpt_Type()
)
gamOcgPtpPmRealGamOcgOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmRealGamOcgOpt.setStatus("current")
_GamOcgPtpPmRealGamOcgOpr_Type = FloatHundredths
_GamOcgPtpPmRealGamOcgOpr_Object = MibTableColumn
gamOcgPtpPmRealGamOcgOpr = _GamOcgPtpPmRealGamOcgOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 1, 1, 2),
    _GamOcgPtpPmRealGamOcgOpr_Type()
)
gamOcgPtpPmRealGamOcgOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmRealGamOcgOpr.setStatus("current")
_GamOcgPtpPmRealGamOcgLbc_Type = FloatHundredths
_GamOcgPtpPmRealGamOcgLbc_Object = MibTableColumn
gamOcgPtpPmRealGamOcgLbc = _GamOcgPtpPmRealGamOcgLbc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 1, 1, 3),
    _GamOcgPtpPmRealGamOcgLbc_Type()
)
gamOcgPtpPmRealGamOcgLbc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmRealGamOcgLbc.setStatus("current")
_GamOcgPtpPmTable_Object = MibTable
gamOcgPtpPmTable = _GamOcgPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2)
)
if mibBuilder.loadTexts:
    gamOcgPtpPmTable.setStatus("current")
_GamOcgPtpPmEntry_Object = MibTableRow
gamOcgPtpPmEntry = _GamOcgPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1)
)
gamOcgPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmSampleDuration"),
    (0, "INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    gamOcgPtpPmEntry.setStatus("current")


class _GamOcgPtpPmTimestamp_Type(Integer32):
    """Custom type gamOcgPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_GamOcgPtpPmTimestamp_Type.__name__ = "Integer32"
_GamOcgPtpPmTimestamp_Object = MibTableColumn
gamOcgPtpPmTimestamp = _GamOcgPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 1),
    _GamOcgPtpPmTimestamp_Type()
)
gamOcgPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gamOcgPtpPmTimestamp.setStatus("current")


class _GamOcgPtpPmSampleDuration_Type(Integer32):
    """Custom type gamOcgPtpPmSampleDuration based on Integer32"""
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


_GamOcgPtpPmSampleDuration_Type.__name__ = "Integer32"
_GamOcgPtpPmSampleDuration_Object = MibTableColumn
gamOcgPtpPmSampleDuration = _GamOcgPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 2),
    _GamOcgPtpPmSampleDuration_Type()
)
gamOcgPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    gamOcgPtpPmSampleDuration.setStatus("current")
_GamOcgPtpPmValidity_Type = TruthValue
_GamOcgPtpPmValidity_Object = MibTableColumn
gamOcgPtpPmValidity = _GamOcgPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 3),
    _GamOcgPtpPmValidity_Type()
)
gamOcgPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmValidity.setStatus("current")
_GamOcgPtpPmGamOcgOptMin_Type = FloatHundredths
_GamOcgPtpPmGamOcgOptMin_Object = MibTableColumn
gamOcgPtpPmGamOcgOptMin = _GamOcgPtpPmGamOcgOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 4),
    _GamOcgPtpPmGamOcgOptMin_Type()
)
gamOcgPtpPmGamOcgOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmGamOcgOptMin.setStatus("current")
_GamOcgPtpPmGamOcgOptMax_Type = FloatHundredths
_GamOcgPtpPmGamOcgOptMax_Object = MibTableColumn
gamOcgPtpPmGamOcgOptMax = _GamOcgPtpPmGamOcgOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 5),
    _GamOcgPtpPmGamOcgOptMax_Type()
)
gamOcgPtpPmGamOcgOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmGamOcgOptMax.setStatus("current")
_GamOcgPtpPmGamOcgOptAve_Type = FloatHundredths
_GamOcgPtpPmGamOcgOptAve_Object = MibTableColumn
gamOcgPtpPmGamOcgOptAve = _GamOcgPtpPmGamOcgOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 6),
    _GamOcgPtpPmGamOcgOptAve_Type()
)
gamOcgPtpPmGamOcgOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmGamOcgOptAve.setStatus("current")
_GamOcgPtpPmGamOcgOprMin_Type = FloatHundredths
_GamOcgPtpPmGamOcgOprMin_Object = MibTableColumn
gamOcgPtpPmGamOcgOprMin = _GamOcgPtpPmGamOcgOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 7),
    _GamOcgPtpPmGamOcgOprMin_Type()
)
gamOcgPtpPmGamOcgOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmGamOcgOprMin.setStatus("current")
_GamOcgPtpPmGamOcgOprMax_Type = FloatHundredths
_GamOcgPtpPmGamOcgOprMax_Object = MibTableColumn
gamOcgPtpPmGamOcgOprMax = _GamOcgPtpPmGamOcgOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 8),
    _GamOcgPtpPmGamOcgOprMax_Type()
)
gamOcgPtpPmGamOcgOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmGamOcgOprMax.setStatus("current")
_GamOcgPtpPmGamOcgOprAve_Type = FloatHundredths
_GamOcgPtpPmGamOcgOprAve_Object = MibTableColumn
gamOcgPtpPmGamOcgOprAve = _GamOcgPtpPmGamOcgOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 9),
    _GamOcgPtpPmGamOcgOprAve_Type()
)
gamOcgPtpPmGamOcgOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmGamOcgOprAve.setStatus("current")
_GamOcgPtpPmGamOcgLbcMin_Type = FloatHundredths
_GamOcgPtpPmGamOcgLbcMin_Object = MibTableColumn
gamOcgPtpPmGamOcgLbcMin = _GamOcgPtpPmGamOcgLbcMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 10),
    _GamOcgPtpPmGamOcgLbcMin_Type()
)
gamOcgPtpPmGamOcgLbcMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmGamOcgLbcMin.setStatus("current")
_GamOcgPtpPmGamOcgLbcMax_Type = FloatHundredths
_GamOcgPtpPmGamOcgLbcMax_Object = MibTableColumn
gamOcgPtpPmGamOcgLbcMax = _GamOcgPtpPmGamOcgLbcMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 11),
    _GamOcgPtpPmGamOcgLbcMax_Type()
)
gamOcgPtpPmGamOcgLbcMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmGamOcgLbcMax.setStatus("current")
_GamOcgPtpPmGamOcgLbcAve_Type = FloatHundredths
_GamOcgPtpPmGamOcgLbcAve_Object = MibTableColumn
gamOcgPtpPmGamOcgLbcAve = _GamOcgPtpPmGamOcgLbcAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 2, 1, 12),
    _GamOcgPtpPmGamOcgLbcAve_Type()
)
gamOcgPtpPmGamOcgLbcAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    gamOcgPtpPmGamOcgLbcAve.setStatus("current")
_GamOcgPtpPmConformance_ObjectIdentity = ObjectIdentity
gamOcgPtpPmConformance = _GamOcgPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 3)
)
_GamOcgPtpPmCompliances_ObjectIdentity = ObjectIdentity
gamOcgPtpPmCompliances = _GamOcgPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 3, 1)
)
_GamOcgPtpPmGroups_ObjectIdentity = ObjectIdentity
gamOcgPtpPmGroups = _GamOcgPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 3, 2)
)

# Managed Objects groups

gamOcgPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 3, 2, 1)
)
gamOcgPtpPmGroup.setObjects(
      *(("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmValidity"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmGamOcgOptMin"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmGamOcgOptMax"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmGamOcgOptAve"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmGamOcgOprMin"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmGamOcgOprMax"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmGamOcgOprAve"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmGamOcgLbcMin"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmGamOcgLbcMax"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmGamOcgLbcAve"))
)
if mibBuilder.loadTexts:
    gamOcgPtpPmGroup.setStatus("current")

gamOcgPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 3, 2, 2)
)
gamOcgPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmRealGamOcgOpt"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmRealGamOcgOpr"),
        ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmRealGamOcgLbc"))
)
if mibBuilder.loadTexts:
    gamOcgPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

gamOcgPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 3, 1, 1)
)
gamOcgPtpPmCompliance.setObjects(
    ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmGroup")
)
if mibBuilder.loadTexts:
    gamOcgPtpPmCompliance.setStatus(
        "current"
    )

gamOcgPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 7, 3, 1, 2)
)
gamOcgPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-GAMOCGPTP-MIB", "gamOcgPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    gamOcgPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-GAMOCGPTP-MIB",
    **{"gamOcgPtpPmMIB": gamOcgPtpPmMIB,
       "gamOcgPtpPmRealTable": gamOcgPtpPmRealTable,
       "gamOcgPtpPmRealEntry": gamOcgPtpPmRealEntry,
       "gamOcgPtpPmRealGamOcgOpt": gamOcgPtpPmRealGamOcgOpt,
       "gamOcgPtpPmRealGamOcgOpr": gamOcgPtpPmRealGamOcgOpr,
       "gamOcgPtpPmRealGamOcgLbc": gamOcgPtpPmRealGamOcgLbc,
       "gamOcgPtpPmTable": gamOcgPtpPmTable,
       "gamOcgPtpPmEntry": gamOcgPtpPmEntry,
       "gamOcgPtpPmTimestamp": gamOcgPtpPmTimestamp,
       "gamOcgPtpPmSampleDuration": gamOcgPtpPmSampleDuration,
       "gamOcgPtpPmValidity": gamOcgPtpPmValidity,
       "gamOcgPtpPmGamOcgOptMin": gamOcgPtpPmGamOcgOptMin,
       "gamOcgPtpPmGamOcgOptMax": gamOcgPtpPmGamOcgOptMax,
       "gamOcgPtpPmGamOcgOptAve": gamOcgPtpPmGamOcgOptAve,
       "gamOcgPtpPmGamOcgOprMin": gamOcgPtpPmGamOcgOprMin,
       "gamOcgPtpPmGamOcgOprMax": gamOcgPtpPmGamOcgOprMax,
       "gamOcgPtpPmGamOcgOprAve": gamOcgPtpPmGamOcgOprAve,
       "gamOcgPtpPmGamOcgLbcMin": gamOcgPtpPmGamOcgLbcMin,
       "gamOcgPtpPmGamOcgLbcMax": gamOcgPtpPmGamOcgLbcMax,
       "gamOcgPtpPmGamOcgLbcAve": gamOcgPtpPmGamOcgLbcAve,
       "gamOcgPtpPmConformance": gamOcgPtpPmConformance,
       "gamOcgPtpPmCompliances": gamOcgPtpPmCompliances,
       "gamOcgPtpPmCompliance": gamOcgPtpPmCompliance,
       "gamOcgPtpPmRealCompliance": gamOcgPtpPmRealCompliance,
       "gamOcgPtpPmGroups": gamOcgPtpPmGroups,
       "gamOcgPtpPmGroup": gamOcgPtpPmGroup,
       "gamOcgPtpPmRealGroup": gamOcgPtpPmRealGroup}
)
