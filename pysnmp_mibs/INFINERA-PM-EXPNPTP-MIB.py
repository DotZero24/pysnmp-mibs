# SNMP MIB module (INFINERA-PM-EXPNPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-EXPNPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:22 2025
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
 InfnSampleDuration) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
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

expnPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82)
)
if mibBuilder.loadTexts:
    expnPtpPmMIB.setRevisions(
        ("2017-02-13 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ExpnPtpPmRealTable_Object = MibTable
expnPtpPmRealTable = _ExpnPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 1)
)
if mibBuilder.loadTexts:
    expnPtpPmRealTable.setStatus("current")
_ExpnPtpPmRealEntry_Object = MibTableRow
expnPtpPmRealEntry = _ExpnPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 1, 1)
)
expnPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    expnPtpPmRealEntry.setStatus("current")
_ExpnPtpPmRealOpt_Type = FloatArbitraryPrecision
_ExpnPtpPmRealOpt_Object = MibTableColumn
expnPtpPmRealOpt = _ExpnPtpPmRealOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 1, 1, 1),
    _ExpnPtpPmRealOpt_Type()
)
expnPtpPmRealOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpPmRealOpt.setStatus("current")
_ExpnPtpPmRealOpr_Type = FloatArbitraryPrecision
_ExpnPtpPmRealOpr_Object = MibTableColumn
expnPtpPmRealOpr = _ExpnPtpPmRealOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 1, 1, 2),
    _ExpnPtpPmRealOpr_Type()
)
expnPtpPmRealOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpPmRealOpr.setStatus("current")
_ExpnPtpPmTable_Object = MibTable
expnPtpPmTable = _ExpnPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2)
)
if mibBuilder.loadTexts:
    expnPtpPmTable.setStatus("current")
_ExpnPtpPmEntry_Object = MibTableRow
expnPtpPmEntry = _ExpnPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2, 1)
)
expnPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-EXPNPTP-MIB", "expnPtpPmSampleDuration"),
    (0, "INFINERA-PM-EXPNPTP-MIB", "expnPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    expnPtpPmEntry.setStatus("current")


class _ExpnPtpPmTimestamp_Type(Integer32):
    """Custom type expnPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_ExpnPtpPmTimestamp_Type.__name__ = "Integer32"
_ExpnPtpPmTimestamp_Object = MibTableColumn
expnPtpPmTimestamp = _ExpnPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2, 1, 1),
    _ExpnPtpPmTimestamp_Type()
)
expnPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expnPtpPmTimestamp.setStatus("current")


class _ExpnPtpPmSampleDuration_Type(Integer32):
    """Custom type expnPtpPmSampleDuration based on Integer32"""
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


_ExpnPtpPmSampleDuration_Type.__name__ = "Integer32"
_ExpnPtpPmSampleDuration_Object = MibTableColumn
expnPtpPmSampleDuration = _ExpnPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2, 1, 2),
    _ExpnPtpPmSampleDuration_Type()
)
expnPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    expnPtpPmSampleDuration.setStatus("current")
_ExpnPtpPmValidity_Type = TruthValue
_ExpnPtpPmValidity_Object = MibTableColumn
expnPtpPmValidity = _ExpnPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2, 1, 3),
    _ExpnPtpPmValidity_Type()
)
expnPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpPmValidity.setStatus("current")
_ExpnPtpPmOptMin_Type = FloatArbitraryPrecision
_ExpnPtpPmOptMin_Object = MibTableColumn
expnPtpPmOptMin = _ExpnPtpPmOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2, 1, 4),
    _ExpnPtpPmOptMin_Type()
)
expnPtpPmOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpPmOptMin.setStatus("current")
_ExpnPtpPmOptMax_Type = FloatArbitraryPrecision
_ExpnPtpPmOptMax_Object = MibTableColumn
expnPtpPmOptMax = _ExpnPtpPmOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2, 1, 5),
    _ExpnPtpPmOptMax_Type()
)
expnPtpPmOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpPmOptMax.setStatus("current")
_ExpnPtpPmOptAve_Type = FloatArbitraryPrecision
_ExpnPtpPmOptAve_Object = MibTableColumn
expnPtpPmOptAve = _ExpnPtpPmOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2, 1, 6),
    _ExpnPtpPmOptAve_Type()
)
expnPtpPmOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpPmOptAve.setStatus("current")
_ExpnPtpPmOprMin_Type = FloatArbitraryPrecision
_ExpnPtpPmOprMin_Object = MibTableColumn
expnPtpPmOprMin = _ExpnPtpPmOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2, 1, 7),
    _ExpnPtpPmOprMin_Type()
)
expnPtpPmOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpPmOprMin.setStatus("current")
_ExpnPtpPmOprMax_Type = FloatArbitraryPrecision
_ExpnPtpPmOprMax_Object = MibTableColumn
expnPtpPmOprMax = _ExpnPtpPmOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2, 1, 8),
    _ExpnPtpPmOprMax_Type()
)
expnPtpPmOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpPmOprMax.setStatus("current")
_ExpnPtpPmOprAve_Type = FloatArbitraryPrecision
_ExpnPtpPmOprAve_Object = MibTableColumn
expnPtpPmOprAve = _ExpnPtpPmOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 2, 1, 9),
    _ExpnPtpPmOprAve_Type()
)
expnPtpPmOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    expnPtpPmOprAve.setStatus("current")
_ExpnPtpPmConformance_ObjectIdentity = ObjectIdentity
expnPtpPmConformance = _ExpnPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 3)
)
_ExpnPtpPmCompliances_ObjectIdentity = ObjectIdentity
expnPtpPmCompliances = _ExpnPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 3, 1)
)
_ExpnPtpPmGroups_ObjectIdentity = ObjectIdentity
expnPtpPmGroups = _ExpnPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 3, 2)
)

# Managed Objects groups

expnPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 3, 2, 1)
)
expnPtpPmGroup.setObjects(
      *(("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmTimestamp"),
        ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmSampleDuration"),
        ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmValidity"),
        ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmOptMin"),
        ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmOptMax"),
        ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmOptAve"),
        ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmOprMin"),
        ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmOprMax"),
        ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmOprAve"))
)
if mibBuilder.loadTexts:
    expnPtpPmGroup.setStatus("current")

expnPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 3, 2, 2)
)
expnPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmRealOpt"),
        ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmRealOpr"))
)
if mibBuilder.loadTexts:
    expnPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

expnPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 3, 1, 1)
)
expnPtpPmCompliance.setObjects(
    ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmGroup")
)
if mibBuilder.loadTexts:
    expnPtpPmCompliance.setStatus(
        "current"
    )

expnPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 82, 3, 1, 2)
)
expnPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-EXPNPTP-MIB", "expnPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    expnPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-EXPNPTP-MIB",
    **{"expnPtpPmMIB": expnPtpPmMIB,
       "expnPtpPmRealTable": expnPtpPmRealTable,
       "expnPtpPmRealEntry": expnPtpPmRealEntry,
       "expnPtpPmRealOpt": expnPtpPmRealOpt,
       "expnPtpPmRealOpr": expnPtpPmRealOpr,
       "expnPtpPmTable": expnPtpPmTable,
       "expnPtpPmEntry": expnPtpPmEntry,
       "expnPtpPmTimestamp": expnPtpPmTimestamp,
       "expnPtpPmSampleDuration": expnPtpPmSampleDuration,
       "expnPtpPmValidity": expnPtpPmValidity,
       "expnPtpPmOptMin": expnPtpPmOptMin,
       "expnPtpPmOptMax": expnPtpPmOptMax,
       "expnPtpPmOptAve": expnPtpPmOptAve,
       "expnPtpPmOprMin": expnPtpPmOprMin,
       "expnPtpPmOprMax": expnPtpPmOprMax,
       "expnPtpPmOprAve": expnPtpPmOprAve,
       "expnPtpPmConformance": expnPtpPmConformance,
       "expnPtpPmCompliances": expnPtpPmCompliances,
       "expnPtpPmCompliance": expnPtpPmCompliance,
       "expnPtpPmRealCompliance": expnPtpPmRealCompliance,
       "expnPtpPmGroups": expnPtpPmGroups,
       "expnPtpPmGroup": expnPtpPmGroup,
       "expnPtpPmRealGroup": expnPtpPmRealGroup}
)
