# SNMP MIB module (INFINERA-PM-FAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-FAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:17 2025
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

(commonPerfMon,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "commonPerfMon")

(FloatTenths,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths")

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

fanPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4)
)
if mibBuilder.loadTexts:
    fanPmMIB.setRevisions(
        ("2015-02-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FanPmRealTable_Object = MibTable
fanPmRealTable = _FanPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 1)
)
if mibBuilder.loadTexts:
    fanPmRealTable.setStatus("current")
_FanPmRealEntry_Object = MibTableRow
fanPmRealEntry = _FanPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 1, 1)
)
fanPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fanPmRealEntry.setStatus("current")
_FanPmRealInRpmRaw_Type = FloatTenths
_FanPmRealInRpmRaw_Object = MibTableColumn
fanPmRealInRpmRaw = _FanPmRealInRpmRaw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 1, 1, 1),
    _FanPmRealInRpmRaw_Type()
)
fanPmRealInRpmRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanPmRealInRpmRaw.setStatus("current")
_FanPmTable_Object = MibTable
fanPmTable = _FanPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2)
)
if mibBuilder.loadTexts:
    fanPmTable.setStatus("current")
_FanPmEntry_Object = MibTableRow
fanPmEntry = _FanPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1)
)
fanPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-FAN-MIB", "fanPmSampleDuration"),
    (0, "INFINERA-PM-FAN-MIB", "fanPmTimestamp"),
)
if mibBuilder.loadTexts:
    fanPmEntry.setStatus("current")


class _FanPmTimestamp_Type(Integer32):
    """Custom type fanPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FanPmTimestamp_Type.__name__ = "Integer32"
_FanPmTimestamp_Object = MibTableColumn
fanPmTimestamp = _FanPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 1),
    _FanPmTimestamp_Type()
)
fanPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanPmTimestamp.setStatus("current")


class _FanPmSampleDuration_Type(Integer32):
    """Custom type fanPmSampleDuration based on Integer32"""
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


_FanPmSampleDuration_Type.__name__ = "Integer32"
_FanPmSampleDuration_Object = MibTableColumn
fanPmSampleDuration = _FanPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 2),
    _FanPmSampleDuration_Type()
)
fanPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fanPmSampleDuration.setStatus("current")
_FanPmValidity_Type = TruthValue
_FanPmValidity_Object = MibTableColumn
fanPmValidity = _FanPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 3),
    _FanPmValidity_Type()
)
fanPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanPmValidity.setStatus("current")
_FanPmInRpmMin_Type = FloatTenths
_FanPmInRpmMin_Object = MibTableColumn
fanPmInRpmMin = _FanPmInRpmMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 4),
    _FanPmInRpmMin_Type()
)
fanPmInRpmMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanPmInRpmMin.setStatus("current")
_FanPmInRpmMax_Type = FloatTenths
_FanPmInRpmMax_Object = MibTableColumn
fanPmInRpmMax = _FanPmInRpmMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 5),
    _FanPmInRpmMax_Type()
)
fanPmInRpmMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanPmInRpmMax.setStatus("current")
_FanPmInRpmAvg_Type = FloatTenths
_FanPmInRpmAvg_Object = MibTableColumn
fanPmInRpmAvg = _FanPmInRpmAvg_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 2, 1, 6),
    _FanPmInRpmAvg_Type()
)
fanPmInRpmAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fanPmInRpmAvg.setStatus("current")
_FanPmConformance_ObjectIdentity = ObjectIdentity
fanPmConformance = _FanPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3)
)
_FanPmCompliances_ObjectIdentity = ObjectIdentity
fanPmCompliances = _FanPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 1)
)
_FanPmGroups_ObjectIdentity = ObjectIdentity
fanPmGroups = _FanPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 2)
)

# Managed Objects groups

fanPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 2, 1)
)
fanPmGroup.setObjects(
      *(("INFINERA-PM-FAN-MIB", "fanPmValidity"),
        ("INFINERA-PM-FAN-MIB", "fanPmInRpmMin"),
        ("INFINERA-PM-FAN-MIB", "fanPmInRpmMax"),
        ("INFINERA-PM-FAN-MIB", "fanPmInRpmAvg"))
)
if mibBuilder.loadTexts:
    fanPmGroup.setStatus("current")

fanPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 2, 2)
)
fanPmRealGroup.setObjects(
    ("INFINERA-PM-FAN-MIB", "fanPmRealInRpmRaw")
)
if mibBuilder.loadTexts:
    fanPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fanPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 1, 1)
)
fanPmCompliance.setObjects(
    ("INFINERA-PM-FAN-MIB", "fanPmRealGroup")
)
if mibBuilder.loadTexts:
    fanPmCompliance.setStatus(
        "current"
    )

fanPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 4, 3, 1, 2)
)
fanPmRealCompliance.setObjects(
    ("INFINERA-PM-FAN-MIB", "fanPmRealGroup")
)
if mibBuilder.loadTexts:
    fanPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-FAN-MIB",
    **{"fanPmMIB": fanPmMIB,
       "fanPmRealTable": fanPmRealTable,
       "fanPmRealEntry": fanPmRealEntry,
       "fanPmRealInRpmRaw": fanPmRealInRpmRaw,
       "fanPmTable": fanPmTable,
       "fanPmEntry": fanPmEntry,
       "fanPmTimestamp": fanPmTimestamp,
       "fanPmSampleDuration": fanPmSampleDuration,
       "fanPmValidity": fanPmValidity,
       "fanPmInRpmMin": fanPmInRpmMin,
       "fanPmInRpmMax": fanPmInRpmMax,
       "fanPmInRpmAvg": fanPmInRpmAvg,
       "fanPmConformance": fanPmConformance,
       "fanPmCompliances": fanPmCompliances,
       "fanPmCompliance": fanPmCompliance,
       "fanPmRealCompliance": fanPmRealCompliance,
       "fanPmGroups": fanPmGroups,
       "fanPmGroup": fanPmGroup,
       "fanPmRealGroup": fanPmRealGroup}
)
