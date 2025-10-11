# SNMP MIB module (INFINERA-PM-OSCTCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-OSCTCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:14 2025
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

osctCtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11)
)
if mibBuilder.loadTexts:
    osctCtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsctCtpPmRealTable_Object = MibTable
osctCtpPmRealTable = _OsctCtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 1)
)
if mibBuilder.loadTexts:
    osctCtpPmRealTable.setStatus("current")
_OsctCtpPmRealEntry_Object = MibTableRow
osctCtpPmRealEntry = _OsctCtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 1, 1)
)
osctCtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    osctCtpPmRealEntry.setStatus("current")
_OsctCtpPmRealOscTOPT_Type = FloatHundredths
_OsctCtpPmRealOscTOPT_Object = MibTableColumn
osctCtpPmRealOscTOPT = _OsctCtpPmRealOscTOPT_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 1, 1, 1),
    _OsctCtpPmRealOscTOPT_Type()
)
osctCtpPmRealOscTOPT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctCtpPmRealOscTOPT.setStatus("current")
_OsctCtpPmRealOscTOPR_Type = FloatHundredths
_OsctCtpPmRealOscTOPR_Object = MibTableColumn
osctCtpPmRealOscTOPR = _OsctCtpPmRealOscTOPR_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 1, 1, 2),
    _OsctCtpPmRealOscTOPR_Type()
)
osctCtpPmRealOscTOPR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctCtpPmRealOscTOPR.setStatus("current")
_OsctCtpPmTable_Object = MibTable
osctCtpPmTable = _OsctCtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2)
)
if mibBuilder.loadTexts:
    osctCtpPmTable.setStatus("current")
_OsctCtpPmEntry_Object = MibTableRow
osctCtpPmEntry = _OsctCtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2, 1)
)
osctCtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-OSCTCTP-MIB", "osctCtpPmSampleDuration"),
    (0, "INFINERA-PM-OSCTCTP-MIB", "osctCtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    osctCtpPmEntry.setStatus("current")


class _OsctCtpPmTimestamp_Type(Integer32):
    """Custom type osctCtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OsctCtpPmTimestamp_Type.__name__ = "Integer32"
_OsctCtpPmTimestamp_Object = MibTableColumn
osctCtpPmTimestamp = _OsctCtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2, 1, 1),
    _OsctCtpPmTimestamp_Type()
)
osctCtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osctCtpPmTimestamp.setStatus("current")


class _OsctCtpPmSampleDuration_Type(Integer32):
    """Custom type osctCtpPmSampleDuration based on Integer32"""
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


_OsctCtpPmSampleDuration_Type.__name__ = "Integer32"
_OsctCtpPmSampleDuration_Object = MibTableColumn
osctCtpPmSampleDuration = _OsctCtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2, 1, 2),
    _OsctCtpPmSampleDuration_Type()
)
osctCtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osctCtpPmSampleDuration.setStatus("current")
_OsctCtpPmValidity_Type = TruthValue
_OsctCtpPmValidity_Object = MibTableColumn
osctCtpPmValidity = _OsctCtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2, 1, 3),
    _OsctCtpPmValidity_Type()
)
osctCtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctCtpPmValidity.setStatus("current")
_OsctCtpPmOscTOPTMin_Type = FloatHundredths
_OsctCtpPmOscTOPTMin_Object = MibTableColumn
osctCtpPmOscTOPTMin = _OsctCtpPmOscTOPTMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2, 1, 4),
    _OsctCtpPmOscTOPTMin_Type()
)
osctCtpPmOscTOPTMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctCtpPmOscTOPTMin.setStatus("current")
_OsctCtpPmOscTOPTMax_Type = FloatHundredths
_OsctCtpPmOscTOPTMax_Object = MibTableColumn
osctCtpPmOscTOPTMax = _OsctCtpPmOscTOPTMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2, 1, 5),
    _OsctCtpPmOscTOPTMax_Type()
)
osctCtpPmOscTOPTMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctCtpPmOscTOPTMax.setStatus("current")
_OsctCtpPmOscTOPTAve_Type = FloatHundredths
_OsctCtpPmOscTOPTAve_Object = MibTableColumn
osctCtpPmOscTOPTAve = _OsctCtpPmOscTOPTAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2, 1, 6),
    _OsctCtpPmOscTOPTAve_Type()
)
osctCtpPmOscTOPTAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctCtpPmOscTOPTAve.setStatus("current")
_OsctCtpPmOscTOPRMin_Type = FloatHundredths
_OsctCtpPmOscTOPRMin_Object = MibTableColumn
osctCtpPmOscTOPRMin = _OsctCtpPmOscTOPRMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2, 1, 7),
    _OsctCtpPmOscTOPRMin_Type()
)
osctCtpPmOscTOPRMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctCtpPmOscTOPRMin.setStatus("current")
_OsctCtpPmOscTOPRMax_Type = FloatHundredths
_OsctCtpPmOscTOPRMax_Object = MibTableColumn
osctCtpPmOscTOPRMax = _OsctCtpPmOscTOPRMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2, 1, 8),
    _OsctCtpPmOscTOPRMax_Type()
)
osctCtpPmOscTOPRMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctCtpPmOscTOPRMax.setStatus("current")
_OsctCtpPmOscTOPRAve_Type = FloatHundredths
_OsctCtpPmOscTOPRAve_Object = MibTableColumn
osctCtpPmOscTOPRAve = _OsctCtpPmOscTOPRAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 2, 1, 9),
    _OsctCtpPmOscTOPRAve_Type()
)
osctCtpPmOscTOPRAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osctCtpPmOscTOPRAve.setStatus("current")
_OsctCtpPmConformance_ObjectIdentity = ObjectIdentity
osctCtpPmConformance = _OsctCtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 3)
)
_OsctCtpPmCompliances_ObjectIdentity = ObjectIdentity
osctCtpPmCompliances = _OsctCtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 3, 1)
)
_OsctCtpPmGroups_ObjectIdentity = ObjectIdentity
osctCtpPmGroups = _OsctCtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 3, 2)
)

# Managed Objects groups

osctCtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 3, 2, 1)
)
osctCtpPmGroup.setObjects(
      *(("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmValidity"),
        ("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmOscTOPTMin"),
        ("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmOscTOPTMax"),
        ("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmOscTOPTAve"),
        ("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmOscTOPRMin"),
        ("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmOscTOPRMax"),
        ("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmOscTOPRAve"))
)
if mibBuilder.loadTexts:
    osctCtpPmGroup.setStatus("current")

osctCtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 3, 2, 2)
)
osctCtpPmRealGroup.setObjects(
      *(("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmRealOscTOPT"),
        ("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmRealOscTOPR"))
)
if mibBuilder.loadTexts:
    osctCtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osctCtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 3, 1, 1)
)
osctCtpPmCompliance.setObjects(
    ("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmGroup")
)
if mibBuilder.loadTexts:
    osctCtpPmCompliance.setStatus(
        "current"
    )

osctCtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 11, 3, 1, 2)
)
osctCtpPmRealCompliance.setObjects(
    ("INFINERA-PM-OSCTCTP-MIB", "osctCtpPmRealGroup")
)
if mibBuilder.loadTexts:
    osctCtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-OSCTCTP-MIB",
    **{"osctCtpPmMIB": osctCtpPmMIB,
       "osctCtpPmRealTable": osctCtpPmRealTable,
       "osctCtpPmRealEntry": osctCtpPmRealEntry,
       "osctCtpPmRealOscTOPT": osctCtpPmRealOscTOPT,
       "osctCtpPmRealOscTOPR": osctCtpPmRealOscTOPR,
       "osctCtpPmTable": osctCtpPmTable,
       "osctCtpPmEntry": osctCtpPmEntry,
       "osctCtpPmTimestamp": osctCtpPmTimestamp,
       "osctCtpPmSampleDuration": osctCtpPmSampleDuration,
       "osctCtpPmValidity": osctCtpPmValidity,
       "osctCtpPmOscTOPTMin": osctCtpPmOscTOPTMin,
       "osctCtpPmOscTOPTMax": osctCtpPmOscTOPTMax,
       "osctCtpPmOscTOPTAve": osctCtpPmOscTOPTAve,
       "osctCtpPmOscTOPRMin": osctCtpPmOscTOPRMin,
       "osctCtpPmOscTOPRMax": osctCtpPmOscTOPRMax,
       "osctCtpPmOscTOPRAve": osctCtpPmOscTOPRAve,
       "osctCtpPmConformance": osctCtpPmConformance,
       "osctCtpPmCompliances": osctCtpPmCompliances,
       "osctCtpPmCompliance": osctCtpPmCompliance,
       "osctCtpPmRealCompliance": osctCtpPmRealCompliance,
       "osctCtpPmGroups": osctCtpPmGroups,
       "osctCtpPmGroup": osctCtpPmGroup,
       "osctCtpPmRealGroup": osctCtpPmRealGroup}
)
