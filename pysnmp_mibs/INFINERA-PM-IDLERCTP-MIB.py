# SNMP MIB module (INFINERA-PM-IDLERCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-IDLERCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:31 2025
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

(FloatArbitraryPrecision,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision")

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

idlerCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86)
)
if mibBuilder.loadTexts:
    idlerCtpPmMIB.setRevisions(
        ("2017-06-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IdlerCtpPmRealTable_Object = MibTable
idlerCtpPmRealTable = _IdlerCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 1)
)
if mibBuilder.loadTexts:
    idlerCtpPmRealTable.setStatus("current")
_IdlerCtpPmRealEntry_Object = MibTableRow
idlerCtpPmRealEntry = _IdlerCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 1, 1)
)
idlerCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    idlerCtpPmRealEntry.setStatus("current")
_IdlerCtpPmRealCmnIdlerOpt_Type = FloatArbitraryPrecision
_IdlerCtpPmRealCmnIdlerOpt_Object = MibTableColumn
idlerCtpPmRealCmnIdlerOpt = _IdlerCtpPmRealCmnIdlerOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 1, 1, 1),
    _IdlerCtpPmRealCmnIdlerOpt_Type()
)
idlerCtpPmRealCmnIdlerOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmRealCmnIdlerOpt.setStatus("current")
_IdlerCtpPmRealCmnIdlerOpr_Type = FloatArbitraryPrecision
_IdlerCtpPmRealCmnIdlerOpr_Object = MibTableColumn
idlerCtpPmRealCmnIdlerOpr = _IdlerCtpPmRealCmnIdlerOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 1, 1, 2),
    _IdlerCtpPmRealCmnIdlerOpr_Type()
)
idlerCtpPmRealCmnIdlerOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmRealCmnIdlerOpr.setStatus("current")
_IdlerCtpPmRealCmnIdlerPostRxVoa_Type = FloatArbitraryPrecision
_IdlerCtpPmRealCmnIdlerPostRxVoa_Object = MibTableColumn
idlerCtpPmRealCmnIdlerPostRxVoa = _IdlerCtpPmRealCmnIdlerPostRxVoa_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 1, 1, 3),
    _IdlerCtpPmRealCmnIdlerPostRxVoa_Type()
)
idlerCtpPmRealCmnIdlerPostRxVoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmRealCmnIdlerPostRxVoa.setStatus("current")
_IdlerCtpPmTable_Object = MibTable
idlerCtpPmTable = _IdlerCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2)
)
if mibBuilder.loadTexts:
    idlerCtpPmTable.setStatus("current")
_IdlerCtpPmEntry_Object = MibTableRow
idlerCtpPmEntry = _IdlerCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1)
)
idlerCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmSampleDuration"),
    (0, "INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    idlerCtpPmEntry.setStatus("current")


class _IdlerCtpPmTimestamp_Type(Integer32):
    """Custom type idlerCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IdlerCtpPmTimestamp_Type.__name__ = "Integer32"
_IdlerCtpPmTimestamp_Object = MibTableColumn
idlerCtpPmTimestamp = _IdlerCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 1),
    _IdlerCtpPmTimestamp_Type()
)
idlerCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    idlerCtpPmTimestamp.setStatus("current")


class _IdlerCtpPmSampleDuration_Type(Integer32):
    """Custom type idlerCtpPmSampleDuration based on Integer32"""
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


_IdlerCtpPmSampleDuration_Type.__name__ = "Integer32"
_IdlerCtpPmSampleDuration_Object = MibTableColumn
idlerCtpPmSampleDuration = _IdlerCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 2),
    _IdlerCtpPmSampleDuration_Type()
)
idlerCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    idlerCtpPmSampleDuration.setStatus("current")
_IdlerCtpPmValidity_Type = TruthValue
_IdlerCtpPmValidity_Object = MibTableColumn
idlerCtpPmValidity = _IdlerCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 3),
    _IdlerCtpPmValidity_Type()
)
idlerCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmValidity.setStatus("current")
_IdlerCtpPmCmnIdlerOptMin_Type = FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOptMin_Object = MibTableColumn
idlerCtpPmCmnIdlerOptMin = _IdlerCtpPmCmnIdlerOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 4),
    _IdlerCtpPmCmnIdlerOptMin_Type()
)
idlerCtpPmCmnIdlerOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmCmnIdlerOptMin.setStatus("current")
_IdlerCtpPmCmnIdlerOptMax_Type = FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOptMax_Object = MibTableColumn
idlerCtpPmCmnIdlerOptMax = _IdlerCtpPmCmnIdlerOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 5),
    _IdlerCtpPmCmnIdlerOptMax_Type()
)
idlerCtpPmCmnIdlerOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmCmnIdlerOptMax.setStatus("current")
_IdlerCtpPmCmnIdlerOptAve_Type = FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOptAve_Object = MibTableColumn
idlerCtpPmCmnIdlerOptAve = _IdlerCtpPmCmnIdlerOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 6),
    _IdlerCtpPmCmnIdlerOptAve_Type()
)
idlerCtpPmCmnIdlerOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmCmnIdlerOptAve.setStatus("current")
_IdlerCtpPmCmnIdlerOprMin_Type = FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOprMin_Object = MibTableColumn
idlerCtpPmCmnIdlerOprMin = _IdlerCtpPmCmnIdlerOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 7),
    _IdlerCtpPmCmnIdlerOprMin_Type()
)
idlerCtpPmCmnIdlerOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmCmnIdlerOprMin.setStatus("current")
_IdlerCtpPmCmnIdlerOprMax_Type = FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOprMax_Object = MibTableColumn
idlerCtpPmCmnIdlerOprMax = _IdlerCtpPmCmnIdlerOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 8),
    _IdlerCtpPmCmnIdlerOprMax_Type()
)
idlerCtpPmCmnIdlerOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmCmnIdlerOprMax.setStatus("current")
_IdlerCtpPmCmnIdlerOprAve_Type = FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerOprAve_Object = MibTableColumn
idlerCtpPmCmnIdlerOprAve = _IdlerCtpPmCmnIdlerOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 9),
    _IdlerCtpPmCmnIdlerOprAve_Type()
)
idlerCtpPmCmnIdlerOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmCmnIdlerOprAve.setStatus("current")
_IdlerCtpPmCmnIdlerPostRxVoaMin_Type = FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerPostRxVoaMin_Object = MibTableColumn
idlerCtpPmCmnIdlerPostRxVoaMin = _IdlerCtpPmCmnIdlerPostRxVoaMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 10),
    _IdlerCtpPmCmnIdlerPostRxVoaMin_Type()
)
idlerCtpPmCmnIdlerPostRxVoaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmCmnIdlerPostRxVoaMin.setStatus("current")
_IdlerCtpPmCmnIdlerPostRxVoaMax_Type = FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerPostRxVoaMax_Object = MibTableColumn
idlerCtpPmCmnIdlerPostRxVoaMax = _IdlerCtpPmCmnIdlerPostRxVoaMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 11),
    _IdlerCtpPmCmnIdlerPostRxVoaMax_Type()
)
idlerCtpPmCmnIdlerPostRxVoaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmCmnIdlerPostRxVoaMax.setStatus("current")
_IdlerCtpPmCmnIdlerPostRxVoaAve_Type = FloatArbitraryPrecision
_IdlerCtpPmCmnIdlerPostRxVoaAve_Object = MibTableColumn
idlerCtpPmCmnIdlerPostRxVoaAve = _IdlerCtpPmCmnIdlerPostRxVoaAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 2, 1, 12),
    _IdlerCtpPmCmnIdlerPostRxVoaAve_Type()
)
idlerCtpPmCmnIdlerPostRxVoaAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    idlerCtpPmCmnIdlerPostRxVoaAve.setStatus("current")
_IdlerCtpPmConformance_ObjectIdentity = ObjectIdentity
idlerCtpPmConformance = _IdlerCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 3)
)
_IdlerCtpPmCompliances_ObjectIdentity = ObjectIdentity
idlerCtpPmCompliances = _IdlerCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 3, 1)
)
_IdlerCtpPmGroups_ObjectIdentity = ObjectIdentity
idlerCtpPmGroups = _IdlerCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 3, 2)
)

# Managed Objects groups

idlerCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 3, 2, 1)
)
idlerCtpPmGroup.setObjects(
      *(("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmTimestamp"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmSampleDuration"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmValidity"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmCmnIdlerOptMin"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmCmnIdlerOptMax"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmCmnIdlerOptAve"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmCmnIdlerOprMin"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmCmnIdlerOprMax"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmCmnIdlerOprAve"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmCmnIdlerPostRxVoaMin"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmCmnIdlerPostRxVoaMax"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmCmnIdlerPostRxVoaAve"))
)
if mibBuilder.loadTexts:
    idlerCtpPmGroup.setStatus("current")

idlerCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 3, 2, 2)
)
idlerCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmRealCmnIdlerOpt"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmRealCmnIdlerOpr"),
        ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmRealCmnIdlerPostRxVoa"))
)
if mibBuilder.loadTexts:
    idlerCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

idlerCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 3, 1, 1)
)
idlerCtpPmCompliance.setObjects(
    ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmGroup")
)
if mibBuilder.loadTexts:
    idlerCtpPmCompliance.setStatus(
        "current"
    )

idlerCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 86, 3, 1, 2)
)
idlerCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-IDLERCTP-MIB", "idlerCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    idlerCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-IDLERCTP-MIB",
    **{"idlerCtpPmMIB": idlerCtpPmMIB,
       "idlerCtpPmRealTable": idlerCtpPmRealTable,
       "idlerCtpPmRealEntry": idlerCtpPmRealEntry,
       "idlerCtpPmRealCmnIdlerOpt": idlerCtpPmRealCmnIdlerOpt,
       "idlerCtpPmRealCmnIdlerOpr": idlerCtpPmRealCmnIdlerOpr,
       "idlerCtpPmRealCmnIdlerPostRxVoa": idlerCtpPmRealCmnIdlerPostRxVoa,
       "idlerCtpPmTable": idlerCtpPmTable,
       "idlerCtpPmEntry": idlerCtpPmEntry,
       "idlerCtpPmTimestamp": idlerCtpPmTimestamp,
       "idlerCtpPmSampleDuration": idlerCtpPmSampleDuration,
       "idlerCtpPmValidity": idlerCtpPmValidity,
       "idlerCtpPmCmnIdlerOptMin": idlerCtpPmCmnIdlerOptMin,
       "idlerCtpPmCmnIdlerOptMax": idlerCtpPmCmnIdlerOptMax,
       "idlerCtpPmCmnIdlerOptAve": idlerCtpPmCmnIdlerOptAve,
       "idlerCtpPmCmnIdlerOprMin": idlerCtpPmCmnIdlerOprMin,
       "idlerCtpPmCmnIdlerOprMax": idlerCtpPmCmnIdlerOprMax,
       "idlerCtpPmCmnIdlerOprAve": idlerCtpPmCmnIdlerOprAve,
       "idlerCtpPmCmnIdlerPostRxVoaMin": idlerCtpPmCmnIdlerPostRxVoaMin,
       "idlerCtpPmCmnIdlerPostRxVoaMax": idlerCtpPmCmnIdlerPostRxVoaMax,
       "idlerCtpPmCmnIdlerPostRxVoaAve": idlerCtpPmCmnIdlerPostRxVoaAve,
       "idlerCtpPmConformance": idlerCtpPmConformance,
       "idlerCtpPmCompliances": idlerCtpPmCompliances,
       "idlerCtpPmCompliance": idlerCtpPmCompliance,
       "idlerCtpPmRealCompliance": idlerCtpPmRealCompliance,
       "idlerCtpPmGroups": idlerCtpPmGroups,
       "idlerCtpPmGroup": idlerCtpPmGroup,
       "idlerCtpPmRealGroup": idlerCtpPmRealGroup}
)
