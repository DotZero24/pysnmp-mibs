# SNMP MIB module (INFINERA-PM-OSCPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-OSCPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:09 2025
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

oscPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34)
)
if mibBuilder.loadTexts:
    oscPtpPmMIB.setRevisions(
        ("2012-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OscPtpPmRealTable_Object = MibTable
oscPtpPmRealTable = _OscPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 1)
)
if mibBuilder.loadTexts:
    oscPtpPmRealTable.setStatus("current")
_OscPtpPmRealEntry_Object = MibTableRow
oscPtpPmRealEntry = _OscPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 1, 1)
)
oscPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    oscPtpPmRealEntry.setStatus("current")
_OscPtpPmRealOscOPR_Type = FloatHundredths
_OscPtpPmRealOscOPR_Object = MibTableColumn
oscPtpPmRealOscOPR = _OscPtpPmRealOscOPR_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 1, 1, 1),
    _OscPtpPmRealOscOPR_Type()
)
oscPtpPmRealOscOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscPtpPmRealOscOPR.setStatus("current")
_OscPtpPmTable_Object = MibTable
oscPtpPmTable = _OscPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2)
)
if mibBuilder.loadTexts:
    oscPtpPmTable.setStatus("current")
_OscPtpPmEntry_Object = MibTableRow
oscPtpPmEntry = _OscPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1)
)
oscPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-OSCPTP-MIB", "oscPtpPmSampleDuration"),
    (0, "INFINERA-PM-OSCPTP-MIB", "oscPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    oscPtpPmEntry.setStatus("current")


class _OscPtpPmTimestamp_Type(Integer32):
    """Custom type oscPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OscPtpPmTimestamp_Type.__name__ = "Integer32"
_OscPtpPmTimestamp_Object = MibTableColumn
oscPtpPmTimestamp = _OscPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1, 1),
    _OscPtpPmTimestamp_Type()
)
oscPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oscPtpPmTimestamp.setStatus("current")


class _OscPtpPmSampleDuration_Type(Integer32):
    """Custom type oscPtpPmSampleDuration based on Integer32"""
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


_OscPtpPmSampleDuration_Type.__name__ = "Integer32"
_OscPtpPmSampleDuration_Object = MibTableColumn
oscPtpPmSampleDuration = _OscPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1, 2),
    _OscPtpPmSampleDuration_Type()
)
oscPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    oscPtpPmSampleDuration.setStatus("current")
_OscPtpPmOscOPRMin_Type = FloatHundredths
_OscPtpPmOscOPRMin_Object = MibTableColumn
oscPtpPmOscOPRMin = _OscPtpPmOscOPRMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1, 3),
    _OscPtpPmOscOPRMin_Type()
)
oscPtpPmOscOPRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscPtpPmOscOPRMin.setStatus("current")
_OscPtpPmOscOPRMax_Type = FloatHundredths
_OscPtpPmOscOPRMax_Object = MibTableColumn
oscPtpPmOscOPRMax = _OscPtpPmOscOPRMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1, 4),
    _OscPtpPmOscOPRMax_Type()
)
oscPtpPmOscOPRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscPtpPmOscOPRMax.setStatus("current")
_OscPtpPmOscOPRAve_Type = FloatHundredths
_OscPtpPmOscOPRAve_Object = MibTableColumn
oscPtpPmOscOPRAve = _OscPtpPmOscOPRAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 2, 1, 5),
    _OscPtpPmOscOPRAve_Type()
)
oscPtpPmOscOPRAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oscPtpPmOscOPRAve.setStatus("current")
_OscPtpPmConformance_ObjectIdentity = ObjectIdentity
oscPtpPmConformance = _OscPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3)
)
_OscPtpPmCompliances_ObjectIdentity = ObjectIdentity
oscPtpPmCompliances = _OscPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 1)
)
_OscPtpPmGroups_ObjectIdentity = ObjectIdentity
oscPtpPmGroups = _OscPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 2)
)

# Managed Objects groups

oscPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 2, 1)
)
oscPtpPmGroup.setObjects(
      *(("INFINERA-PM-OSCPTP-MIB", "oscPtpPmOscOPRMin"),
        ("INFINERA-PM-OSCPTP-MIB", "oscPtpPmOscOPRMax"),
        ("INFINERA-PM-OSCPTP-MIB", "oscPtpPmOscOPRAve"))
)
if mibBuilder.loadTexts:
    oscPtpPmGroup.setStatus("current")

oscPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 2, 2)
)
oscPtpPmRealGroup.setObjects(
    ("INFINERA-PM-OSCPTP-MIB", "oscPtpPmRealOscOPR")
)
if mibBuilder.loadTexts:
    oscPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oscPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 1, 1)
)
oscPtpPmCompliance.setObjects(
    ("INFINERA-PM-OSCPTP-MIB", "oscPtpPmGroup")
)
if mibBuilder.loadTexts:
    oscPtpPmCompliance.setStatus(
        "current"
    )

oscPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 34, 3, 1, 2)
)
oscPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-OSCPTP-MIB", "oscPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    oscPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-OSCPTP-MIB",
    **{"oscPtpPmMIB": oscPtpPmMIB,
       "oscPtpPmRealTable": oscPtpPmRealTable,
       "oscPtpPmRealEntry": oscPtpPmRealEntry,
       "oscPtpPmRealOscOPR": oscPtpPmRealOscOPR,
       "oscPtpPmTable": oscPtpPmTable,
       "oscPtpPmEntry": oscPtpPmEntry,
       "oscPtpPmTimestamp": oscPtpPmTimestamp,
       "oscPtpPmSampleDuration": oscPtpPmSampleDuration,
       "oscPtpPmOscOPRMin": oscPtpPmOscOPRMin,
       "oscPtpPmOscOPRMax": oscPtpPmOscOPRMax,
       "oscPtpPmOscOPRAve": oscPtpPmOscOPRAve,
       "oscPtpPmConformance": oscPtpPmConformance,
       "oscPtpPmCompliances": oscPtpPmCompliances,
       "oscPtpPmCompliance": oscPtpPmCompliance,
       "oscPtpPmRealCompliance": oscPtpPmRealCompliance,
       "oscPtpPmGroups": oscPtpPmGroups,
       "oscPtpPmGroup": oscPtpPmGroup,
       "oscPtpPmRealGroup": oscPtpPmRealGroup}
)
