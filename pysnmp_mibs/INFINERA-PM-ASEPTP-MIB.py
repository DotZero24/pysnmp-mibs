# SNMP MIB module (INFINERA-PM-ASEPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-ASEPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:27 2025
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

asePtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84)
)
if mibBuilder.loadTexts:
    asePtpPmMIB.setRevisions(
        ("2017-06-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AsePtpPmRealTable_Object = MibTable
asePtpPmRealTable = _AsePtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 1)
)
if mibBuilder.loadTexts:
    asePtpPmRealTable.setStatus("current")
_AsePtpPmRealEntry_Object = MibTableRow
asePtpPmRealEntry = _AsePtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 1, 1)
)
asePtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    asePtpPmRealEntry.setStatus("current")
_AsePtpPmRealCmnAseOpt_Type = FloatArbitraryPrecision
_AsePtpPmRealCmnAseOpt_Object = MibTableColumn
asePtpPmRealCmnAseOpt = _AsePtpPmRealCmnAseOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 1, 1, 1),
    _AsePtpPmRealCmnAseOpt_Type()
)
asePtpPmRealCmnAseOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmRealCmnAseOpt.setStatus("current")
_AsePtpPmRealCmnAseOpr_Type = FloatArbitraryPrecision
_AsePtpPmRealCmnAseOpr_Object = MibTableColumn
asePtpPmRealCmnAseOpr = _AsePtpPmRealCmnAseOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 1, 1, 2),
    _AsePtpPmRealCmnAseOpr_Type()
)
asePtpPmRealCmnAseOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmRealCmnAseOpr.setStatus("current")
_AsePtpPmRealCmnAsePostRxVoa_Type = FloatArbitraryPrecision
_AsePtpPmRealCmnAsePostRxVoa_Object = MibTableColumn
asePtpPmRealCmnAsePostRxVoa = _AsePtpPmRealCmnAsePostRxVoa_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 1, 1, 3),
    _AsePtpPmRealCmnAsePostRxVoa_Type()
)
asePtpPmRealCmnAsePostRxVoa.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmRealCmnAsePostRxVoa.setStatus("current")
_AsePtpPmTable_Object = MibTable
asePtpPmTable = _AsePtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2)
)
if mibBuilder.loadTexts:
    asePtpPmTable.setStatus("current")
_AsePtpPmEntry_Object = MibTableRow
asePtpPmEntry = _AsePtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1)
)
asePtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-ASEPTP-MIB", "asePtpPmSampleDuration"),
    (0, "INFINERA-PM-ASEPTP-MIB", "asePtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    asePtpPmEntry.setStatus("current")


class _AsePtpPmTimestamp_Type(Integer32):
    """Custom type asePtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AsePtpPmTimestamp_Type.__name__ = "Integer32"
_AsePtpPmTimestamp_Object = MibTableColumn
asePtpPmTimestamp = _AsePtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 1),
    _AsePtpPmTimestamp_Type()
)
asePtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asePtpPmTimestamp.setStatus("current")


class _AsePtpPmSampleDuration_Type(Integer32):
    """Custom type asePtpPmSampleDuration based on Integer32"""
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


_AsePtpPmSampleDuration_Type.__name__ = "Integer32"
_AsePtpPmSampleDuration_Object = MibTableColumn
asePtpPmSampleDuration = _AsePtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 2),
    _AsePtpPmSampleDuration_Type()
)
asePtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    asePtpPmSampleDuration.setStatus("current")
_AsePtpPmValidity_Type = TruthValue
_AsePtpPmValidity_Object = MibTableColumn
asePtpPmValidity = _AsePtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 3),
    _AsePtpPmValidity_Type()
)
asePtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmValidity.setStatus("current")
_AsePtpPmCmnAseOptMin_Type = FloatArbitraryPrecision
_AsePtpPmCmnAseOptMin_Object = MibTableColumn
asePtpPmCmnAseOptMin = _AsePtpPmCmnAseOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 4),
    _AsePtpPmCmnAseOptMin_Type()
)
asePtpPmCmnAseOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmCmnAseOptMin.setStatus("current")
_AsePtpPmCmnAseOptMax_Type = FloatArbitraryPrecision
_AsePtpPmCmnAseOptMax_Object = MibTableColumn
asePtpPmCmnAseOptMax = _AsePtpPmCmnAseOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 5),
    _AsePtpPmCmnAseOptMax_Type()
)
asePtpPmCmnAseOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmCmnAseOptMax.setStatus("current")
_AsePtpPmCmnAseOptAve_Type = FloatArbitraryPrecision
_AsePtpPmCmnAseOptAve_Object = MibTableColumn
asePtpPmCmnAseOptAve = _AsePtpPmCmnAseOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 6),
    _AsePtpPmCmnAseOptAve_Type()
)
asePtpPmCmnAseOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmCmnAseOptAve.setStatus("current")
_AsePtpPmCmnAseOprMin_Type = FloatArbitraryPrecision
_AsePtpPmCmnAseOprMin_Object = MibTableColumn
asePtpPmCmnAseOprMin = _AsePtpPmCmnAseOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 7),
    _AsePtpPmCmnAseOprMin_Type()
)
asePtpPmCmnAseOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmCmnAseOprMin.setStatus("current")
_AsePtpPmCmnAseOprMax_Type = FloatArbitraryPrecision
_AsePtpPmCmnAseOprMax_Object = MibTableColumn
asePtpPmCmnAseOprMax = _AsePtpPmCmnAseOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 8),
    _AsePtpPmCmnAseOprMax_Type()
)
asePtpPmCmnAseOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmCmnAseOprMax.setStatus("current")
_AsePtpPmCmnAseOprAve_Type = FloatArbitraryPrecision
_AsePtpPmCmnAseOprAve_Object = MibTableColumn
asePtpPmCmnAseOprAve = _AsePtpPmCmnAseOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 9),
    _AsePtpPmCmnAseOprAve_Type()
)
asePtpPmCmnAseOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmCmnAseOprAve.setStatus("current")
_AsePtpPmCmnAsePostRxVoaMin_Type = FloatArbitraryPrecision
_AsePtpPmCmnAsePostRxVoaMin_Object = MibTableColumn
asePtpPmCmnAsePostRxVoaMin = _AsePtpPmCmnAsePostRxVoaMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 10),
    _AsePtpPmCmnAsePostRxVoaMin_Type()
)
asePtpPmCmnAsePostRxVoaMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmCmnAsePostRxVoaMin.setStatus("current")
_AsePtpPmCmnAsePostRxVoaMax_Type = FloatArbitraryPrecision
_AsePtpPmCmnAsePostRxVoaMax_Object = MibTableColumn
asePtpPmCmnAsePostRxVoaMax = _AsePtpPmCmnAsePostRxVoaMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 11),
    _AsePtpPmCmnAsePostRxVoaMax_Type()
)
asePtpPmCmnAsePostRxVoaMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmCmnAsePostRxVoaMax.setStatus("current")
_AsePtpPmCmnAsePostRxVoaAve_Type = FloatArbitraryPrecision
_AsePtpPmCmnAsePostRxVoaAve_Object = MibTableColumn
asePtpPmCmnAsePostRxVoaAve = _AsePtpPmCmnAsePostRxVoaAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 2, 1, 12),
    _AsePtpPmCmnAsePostRxVoaAve_Type()
)
asePtpPmCmnAsePostRxVoaAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    asePtpPmCmnAsePostRxVoaAve.setStatus("current")
_AsePtpPmConformance_ObjectIdentity = ObjectIdentity
asePtpPmConformance = _AsePtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 3)
)
_AsePtpPmCompliances_ObjectIdentity = ObjectIdentity
asePtpPmCompliances = _AsePtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 3, 1)
)
_AsePtpPmGroups_ObjectIdentity = ObjectIdentity
asePtpPmGroups = _AsePtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 3, 2)
)

# Managed Objects groups

asePtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 3, 2, 1)
)
asePtpPmGroup.setObjects(
      *(("INFINERA-PM-ASEPTP-MIB", "asePtpPmTimestamp"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmSampleDuration"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmValidity"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmCmnAseOptMin"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmCmnAseOptMax"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmCmnAseOptAve"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmCmnAseOprMin"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmCmnAseOprMax"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmCmnAseOprAve"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmCmnAsePostRxVoaMin"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmCmnAsePostRxVoaMax"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmCmnAsePostRxVoaAve"))
)
if mibBuilder.loadTexts:
    asePtpPmGroup.setStatus("current")

asePtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 3, 2, 2)
)
asePtpPmRealGroup.setObjects(
      *(("INFINERA-PM-ASEPTP-MIB", "asePtpPmRealCmnAseOpt"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmRealCmnAseOpr"),
        ("INFINERA-PM-ASEPTP-MIB", "asePtpPmRealCmnAsePostRxVoa"))
)
if mibBuilder.loadTexts:
    asePtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

asePtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 3, 1, 1)
)
asePtpPmCompliance.setObjects(
    ("INFINERA-PM-ASEPTP-MIB", "asePtpPmGroup")
)
if mibBuilder.loadTexts:
    asePtpPmCompliance.setStatus(
        "current"
    )

asePtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 84, 3, 1, 2)
)
asePtpPmRealCompliance.setObjects(
    ("INFINERA-PM-ASEPTP-MIB", "asePtpPmRealGroup")
)
if mibBuilder.loadTexts:
    asePtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-ASEPTP-MIB",
    **{"asePtpPmMIB": asePtpPmMIB,
       "asePtpPmRealTable": asePtpPmRealTable,
       "asePtpPmRealEntry": asePtpPmRealEntry,
       "asePtpPmRealCmnAseOpt": asePtpPmRealCmnAseOpt,
       "asePtpPmRealCmnAseOpr": asePtpPmRealCmnAseOpr,
       "asePtpPmRealCmnAsePostRxVoa": asePtpPmRealCmnAsePostRxVoa,
       "asePtpPmTable": asePtpPmTable,
       "asePtpPmEntry": asePtpPmEntry,
       "asePtpPmTimestamp": asePtpPmTimestamp,
       "asePtpPmSampleDuration": asePtpPmSampleDuration,
       "asePtpPmValidity": asePtpPmValidity,
       "asePtpPmCmnAseOptMin": asePtpPmCmnAseOptMin,
       "asePtpPmCmnAseOptMax": asePtpPmCmnAseOptMax,
       "asePtpPmCmnAseOptAve": asePtpPmCmnAseOptAve,
       "asePtpPmCmnAseOprMin": asePtpPmCmnAseOprMin,
       "asePtpPmCmnAseOprMax": asePtpPmCmnAseOprMax,
       "asePtpPmCmnAseOprAve": asePtpPmCmnAseOprAve,
       "asePtpPmCmnAsePostRxVoaMin": asePtpPmCmnAsePostRxVoaMin,
       "asePtpPmCmnAsePostRxVoaMax": asePtpPmCmnAsePostRxVoaMax,
       "asePtpPmCmnAsePostRxVoaAve": asePtpPmCmnAsePostRxVoaAve,
       "asePtpPmConformance": asePtpPmConformance,
       "asePtpPmCompliances": asePtpPmCompliances,
       "asePtpPmCompliance": asePtpPmCompliance,
       "asePtpPmRealCompliance": asePtpPmRealCompliance,
       "asePtpPmGroups": asePtpPmGroups,
       "asePtpPmGroup": asePtpPmGroup,
       "asePtpPmRealGroup": asePtpPmRealGroup}
)
