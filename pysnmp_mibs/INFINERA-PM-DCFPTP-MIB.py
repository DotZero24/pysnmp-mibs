# SNMP MIB module (INFINERA-PM-DCFPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-DCFPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:54 2025
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

dcfPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17)
)
if mibBuilder.loadTexts:
    dcfPtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DcfPtpPmRealTable_Object = MibTable
dcfPtpPmRealTable = _DcfPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 1)
)
if mibBuilder.loadTexts:
    dcfPtpPmRealTable.setStatus("current")
_DcfPtpPmRealEntry_Object = MibTableRow
dcfPtpPmRealEntry = _DcfPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 1, 1)
)
dcfPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dcfPtpPmRealEntry.setStatus("current")
_DcfPtpPmRealOpt_Type = FloatHundredths
_DcfPtpPmRealOpt_Object = MibTableColumn
dcfPtpPmRealOpt = _DcfPtpPmRealOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 1, 1, 1),
    _DcfPtpPmRealOpt_Type()
)
dcfPtpPmRealOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpPmRealOpt.setStatus("current")
_DcfPtpPmRealOpr_Type = FloatHundredths
_DcfPtpPmRealOpr_Object = MibTableColumn
dcfPtpPmRealOpr = _DcfPtpPmRealOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 1, 1, 2),
    _DcfPtpPmRealOpr_Type()
)
dcfPtpPmRealOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpPmRealOpr.setStatus("current")
_DcfPtpPmTable_Object = MibTable
dcfPtpPmTable = _DcfPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2)
)
if mibBuilder.loadTexts:
    dcfPtpPmTable.setStatus("current")
_DcfPtpPmEntry_Object = MibTableRow
dcfPtpPmEntry = _DcfPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2, 1)
)
dcfPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-DCFPTP-MIB", "dcfPtpPmSampleDuration"),
    (0, "INFINERA-PM-DCFPTP-MIB", "dcfPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    dcfPtpPmEntry.setStatus("current")


class _DcfPtpPmTimestamp_Type(Integer32):
    """Custom type dcfPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DcfPtpPmTimestamp_Type.__name__ = "Integer32"
_DcfPtpPmTimestamp_Object = MibTableColumn
dcfPtpPmTimestamp = _DcfPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2, 1, 1),
    _DcfPtpPmTimestamp_Type()
)
dcfPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcfPtpPmTimestamp.setStatus("current")


class _DcfPtpPmSampleDuration_Type(Integer32):
    """Custom type dcfPtpPmSampleDuration based on Integer32"""
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


_DcfPtpPmSampleDuration_Type.__name__ = "Integer32"
_DcfPtpPmSampleDuration_Object = MibTableColumn
dcfPtpPmSampleDuration = _DcfPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2, 1, 2),
    _DcfPtpPmSampleDuration_Type()
)
dcfPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dcfPtpPmSampleDuration.setStatus("current")
_DcfPtpPmValidity_Type = TruthValue
_DcfPtpPmValidity_Object = MibTableColumn
dcfPtpPmValidity = _DcfPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2, 1, 3),
    _DcfPtpPmValidity_Type()
)
dcfPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpPmValidity.setStatus("current")
_DcfPtpPmOptMin_Type = FloatHundredths
_DcfPtpPmOptMin_Object = MibTableColumn
dcfPtpPmOptMin = _DcfPtpPmOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2, 1, 4),
    _DcfPtpPmOptMin_Type()
)
dcfPtpPmOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpPmOptMin.setStatus("current")
_DcfPtpPmOptMax_Type = FloatHundredths
_DcfPtpPmOptMax_Object = MibTableColumn
dcfPtpPmOptMax = _DcfPtpPmOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2, 1, 5),
    _DcfPtpPmOptMax_Type()
)
dcfPtpPmOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpPmOptMax.setStatus("current")
_DcfPtpPmOptAve_Type = FloatHundredths
_DcfPtpPmOptAve_Object = MibTableColumn
dcfPtpPmOptAve = _DcfPtpPmOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2, 1, 6),
    _DcfPtpPmOptAve_Type()
)
dcfPtpPmOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpPmOptAve.setStatus("current")
_DcfPtpPmOprMin_Type = FloatHundredths
_DcfPtpPmOprMin_Object = MibTableColumn
dcfPtpPmOprMin = _DcfPtpPmOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2, 1, 7),
    _DcfPtpPmOprMin_Type()
)
dcfPtpPmOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpPmOprMin.setStatus("current")
_DcfPtpPmOprMax_Type = FloatHundredths
_DcfPtpPmOprMax_Object = MibTableColumn
dcfPtpPmOprMax = _DcfPtpPmOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2, 1, 8),
    _DcfPtpPmOprMax_Type()
)
dcfPtpPmOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpPmOprMax.setStatus("current")
_DcfPtpPmOprAve_Type = FloatHundredths
_DcfPtpPmOprAve_Object = MibTableColumn
dcfPtpPmOprAve = _DcfPtpPmOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 2, 1, 9),
    _DcfPtpPmOprAve_Type()
)
dcfPtpPmOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dcfPtpPmOprAve.setStatus("current")
_DcfPtpPmConformance_ObjectIdentity = ObjectIdentity
dcfPtpPmConformance = _DcfPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 3)
)
_DcfPtpPmCompliances_ObjectIdentity = ObjectIdentity
dcfPtpPmCompliances = _DcfPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 3, 1)
)
_DcfPtpPmGroups_ObjectIdentity = ObjectIdentity
dcfPtpPmGroups = _DcfPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 3, 2)
)

# Managed Objects groups

dcfPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 3, 2, 1)
)
dcfPtpPmGroup.setObjects(
      *(("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmValidity"),
        ("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmOptMin"),
        ("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmOptMax"),
        ("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmOptAve"),
        ("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmOprMin"),
        ("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmOprMax"),
        ("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmOprAve"))
)
if mibBuilder.loadTexts:
    dcfPtpPmGroup.setStatus("current")

dcfPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 3, 2, 2)
)
dcfPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmRealOpt"),
        ("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmRealOpr"))
)
if mibBuilder.loadTexts:
    dcfPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dcfPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 3, 1, 1)
)
dcfPtpPmCompliance.setObjects(
    ("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmGroup")
)
if mibBuilder.loadTexts:
    dcfPtpPmCompliance.setStatus(
        "current"
    )

dcfPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 17, 3, 1, 2)
)
dcfPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-DCFPTP-MIB", "dcfPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    dcfPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-DCFPTP-MIB",
    **{"dcfPtpPmMIB": dcfPtpPmMIB,
       "dcfPtpPmRealTable": dcfPtpPmRealTable,
       "dcfPtpPmRealEntry": dcfPtpPmRealEntry,
       "dcfPtpPmRealOpt": dcfPtpPmRealOpt,
       "dcfPtpPmRealOpr": dcfPtpPmRealOpr,
       "dcfPtpPmTable": dcfPtpPmTable,
       "dcfPtpPmEntry": dcfPtpPmEntry,
       "dcfPtpPmTimestamp": dcfPtpPmTimestamp,
       "dcfPtpPmSampleDuration": dcfPtpPmSampleDuration,
       "dcfPtpPmValidity": dcfPtpPmValidity,
       "dcfPtpPmOptMin": dcfPtpPmOptMin,
       "dcfPtpPmOptMax": dcfPtpPmOptMax,
       "dcfPtpPmOptAve": dcfPtpPmOptAve,
       "dcfPtpPmOprMin": dcfPtpPmOprMin,
       "dcfPtpPmOprMax": dcfPtpPmOprMax,
       "dcfPtpPmOprAve": dcfPtpPmOprAve,
       "dcfPtpPmConformance": dcfPtpPmConformance,
       "dcfPtpPmCompliances": dcfPtpPmCompliances,
       "dcfPtpPmCompliance": dcfPtpPmCompliance,
       "dcfPtpPmRealCompliance": dcfPtpPmRealCompliance,
       "dcfPtpPmGroups": dcfPtpPmGroups,
       "dcfPtpPmGroup": dcfPtpPmGroup,
       "dcfPtpPmRealGroup": dcfPtpPmRealGroup}
)
