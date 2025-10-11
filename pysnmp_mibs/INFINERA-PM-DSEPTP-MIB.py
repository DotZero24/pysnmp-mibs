# SNMP MIB module (INFINERA-PM-DSEPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-DSEPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:06 2025
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

dsePtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18)
)
if mibBuilder.loadTexts:
    dsePtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DsePtpPmRealTable_Object = MibTable
dsePtpPmRealTable = _DsePtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 1)
)
if mibBuilder.loadTexts:
    dsePtpPmRealTable.setStatus("current")
_DsePtpPmRealEntry_Object = MibTableRow
dsePtpPmRealEntry = _DsePtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 1, 1)
)
dsePtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dsePtpPmRealEntry.setStatus("current")
_DsePtpPmRealOpt_Type = FloatHundredths
_DsePtpPmRealOpt_Object = MibTableColumn
dsePtpPmRealOpt = _DsePtpPmRealOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 1, 1, 1),
    _DsePtpPmRealOpt_Type()
)
dsePtpPmRealOpt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsePtpPmRealOpt.setStatus("current")
_DsePtpPmRealOpr_Type = FloatHundredths
_DsePtpPmRealOpr_Object = MibTableColumn
dsePtpPmRealOpr = _DsePtpPmRealOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 1, 1, 2),
    _DsePtpPmRealOpr_Type()
)
dsePtpPmRealOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsePtpPmRealOpr.setStatus("current")
_DsePtpPmTable_Object = MibTable
dsePtpPmTable = _DsePtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2)
)
if mibBuilder.loadTexts:
    dsePtpPmTable.setStatus("current")
_DsePtpPmEntry_Object = MibTableRow
dsePtpPmEntry = _DsePtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2, 1)
)
dsePtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-DSEPTP-MIB", "dsePtpPmSampleDuration"),
    (0, "INFINERA-PM-DSEPTP-MIB", "dsePtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    dsePtpPmEntry.setStatus("current")


class _DsePtpPmTimestamp_Type(Integer32):
    """Custom type dsePtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_DsePtpPmTimestamp_Type.__name__ = "Integer32"
_DsePtpPmTimestamp_Object = MibTableColumn
dsePtpPmTimestamp = _DsePtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2, 1, 1),
    _DsePtpPmTimestamp_Type()
)
dsePtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsePtpPmTimestamp.setStatus("current")


class _DsePtpPmSampleDuration_Type(Integer32):
    """Custom type dsePtpPmSampleDuration based on Integer32"""
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


_DsePtpPmSampleDuration_Type.__name__ = "Integer32"
_DsePtpPmSampleDuration_Object = MibTableColumn
dsePtpPmSampleDuration = _DsePtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2, 1, 2),
    _DsePtpPmSampleDuration_Type()
)
dsePtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dsePtpPmSampleDuration.setStatus("current")
_DsePtpPmValidity_Type = TruthValue
_DsePtpPmValidity_Object = MibTableColumn
dsePtpPmValidity = _DsePtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2, 1, 3),
    _DsePtpPmValidity_Type()
)
dsePtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsePtpPmValidity.setStatus("current")
_DsePtpPmOptMin_Type = FloatHundredths
_DsePtpPmOptMin_Object = MibTableColumn
dsePtpPmOptMin = _DsePtpPmOptMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2, 1, 4),
    _DsePtpPmOptMin_Type()
)
dsePtpPmOptMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsePtpPmOptMin.setStatus("current")
_DsePtpPmOptMax_Type = FloatHundredths
_DsePtpPmOptMax_Object = MibTableColumn
dsePtpPmOptMax = _DsePtpPmOptMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2, 1, 5),
    _DsePtpPmOptMax_Type()
)
dsePtpPmOptMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsePtpPmOptMax.setStatus("current")
_DsePtpPmOptAve_Type = FloatHundredths
_DsePtpPmOptAve_Object = MibTableColumn
dsePtpPmOptAve = _DsePtpPmOptAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2, 1, 6),
    _DsePtpPmOptAve_Type()
)
dsePtpPmOptAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsePtpPmOptAve.setStatus("current")
_DsePtpPmOprMin_Type = FloatHundredths
_DsePtpPmOprMin_Object = MibTableColumn
dsePtpPmOprMin = _DsePtpPmOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2, 1, 7),
    _DsePtpPmOprMin_Type()
)
dsePtpPmOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsePtpPmOprMin.setStatus("current")
_DsePtpPmOprMax_Type = FloatHundredths
_DsePtpPmOprMax_Object = MibTableColumn
dsePtpPmOprMax = _DsePtpPmOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2, 1, 8),
    _DsePtpPmOprMax_Type()
)
dsePtpPmOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsePtpPmOprMax.setStatus("current")
_DsePtpPmOprAve_Type = FloatHundredths
_DsePtpPmOprAve_Object = MibTableColumn
dsePtpPmOprAve = _DsePtpPmOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 2, 1, 9),
    _DsePtpPmOprAve_Type()
)
dsePtpPmOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dsePtpPmOprAve.setStatus("current")
_DsePtpPmConformance_ObjectIdentity = ObjectIdentity
dsePtpPmConformance = _DsePtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 3)
)
_DsePtpPmCompliances_ObjectIdentity = ObjectIdentity
dsePtpPmCompliances = _DsePtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 3, 1)
)
_DsePtpPmGroups_ObjectIdentity = ObjectIdentity
dsePtpPmGroups = _DsePtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 3, 2)
)

# Managed Objects groups

dsePtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 3, 2, 1)
)
dsePtpPmGroup.setObjects(
      *(("INFINERA-PM-DSEPTP-MIB", "dsePtpPmValidity"),
        ("INFINERA-PM-DSEPTP-MIB", "dsePtpPmOptMin"),
        ("INFINERA-PM-DSEPTP-MIB", "dsePtpPmOptMax"),
        ("INFINERA-PM-DSEPTP-MIB", "dsePtpPmOptAve"),
        ("INFINERA-PM-DSEPTP-MIB", "dsePtpPmOprMin"),
        ("INFINERA-PM-DSEPTP-MIB", "dsePtpPmOprMax"),
        ("INFINERA-PM-DSEPTP-MIB", "dsePtpPmOprAve"))
)
if mibBuilder.loadTexts:
    dsePtpPmGroup.setStatus("current")

dsePtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 3, 2, 2)
)
dsePtpPmRealGroup.setObjects(
      *(("INFINERA-PM-DSEPTP-MIB", "dsePtpPmRealOpt"),
        ("INFINERA-PM-DSEPTP-MIB", "dsePtpPmRealOpr"))
)
if mibBuilder.loadTexts:
    dsePtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dsePtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 3, 1, 1)
)
dsePtpPmCompliance.setObjects(
    ("INFINERA-PM-DSEPTP-MIB", "dsePtpPmGroup")
)
if mibBuilder.loadTexts:
    dsePtpPmCompliance.setStatus(
        "current"
    )

dsePtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 18, 3, 1, 2)
)
dsePtpPmRealCompliance.setObjects(
    ("INFINERA-PM-DSEPTP-MIB", "dsePtpPmRealGroup")
)
if mibBuilder.loadTexts:
    dsePtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-DSEPTP-MIB",
    **{"dsePtpPmMIB": dsePtpPmMIB,
       "dsePtpPmRealTable": dsePtpPmRealTable,
       "dsePtpPmRealEntry": dsePtpPmRealEntry,
       "dsePtpPmRealOpt": dsePtpPmRealOpt,
       "dsePtpPmRealOpr": dsePtpPmRealOpr,
       "dsePtpPmTable": dsePtpPmTable,
       "dsePtpPmEntry": dsePtpPmEntry,
       "dsePtpPmTimestamp": dsePtpPmTimestamp,
       "dsePtpPmSampleDuration": dsePtpPmSampleDuration,
       "dsePtpPmValidity": dsePtpPmValidity,
       "dsePtpPmOptMin": dsePtpPmOptMin,
       "dsePtpPmOptMax": dsePtpPmOptMax,
       "dsePtpPmOptAve": dsePtpPmOptAve,
       "dsePtpPmOprMin": dsePtpPmOprMin,
       "dsePtpPmOprMax": dsePtpPmOprMax,
       "dsePtpPmOprAve": dsePtpPmOprAve,
       "dsePtpPmConformance": dsePtpPmConformance,
       "dsePtpPmCompliances": dsePtpPmCompliances,
       "dsePtpPmCompliance": dsePtpPmCompliance,
       "dsePtpPmRealCompliance": dsePtpPmRealCompliance,
       "dsePtpPmGroups": dsePtpPmGroups,
       "dsePtpPmGroup": dsePtpPmGroup,
       "dsePtpPmRealGroup": dsePtpPmRealGroup}
)
