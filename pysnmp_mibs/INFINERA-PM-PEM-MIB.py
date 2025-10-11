# SNMP MIB module (INFINERA-PM-PEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-PEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:48 2025
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

(FloatThousandths,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatThousandths")

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

pemPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5)
)
if mibBuilder.loadTexts:
    pemPmMIB.setRevisions(
        ("2015-02-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PemPmRealTable_Object = MibTable
pemPmRealTable = _PemPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 1)
)
if mibBuilder.loadTexts:
    pemPmRealTable.setStatus("current")
_PemPmRealEntry_Object = MibTableRow
pemPmRealEntry = _PemPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 1, 1)
)
pemPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pemPmRealEntry.setStatus("current")
_PemPmRealInVRaw_Type = FloatThousandths
_PemPmRealInVRaw_Object = MibTableColumn
pemPmRealInVRaw = _PemPmRealInVRaw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 1, 1, 1),
    _PemPmRealInVRaw_Type()
)
pemPmRealInVRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmRealInVRaw.setStatus("current")
_PemPmRealInCRaw_Type = FloatThousandths
_PemPmRealInCRaw_Object = MibTableColumn
pemPmRealInCRaw = _PemPmRealInCRaw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 1, 1, 2),
    _PemPmRealInCRaw_Type()
)
pemPmRealInCRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmRealInCRaw.setStatus("current")
_PemPmRealInPRaw_Type = FloatThousandths
_PemPmRealInPRaw_Object = MibTableColumn
pemPmRealInPRaw = _PemPmRealInPRaw_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 1, 1, 3),
    _PemPmRealInPRaw_Type()
)
pemPmRealInPRaw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmRealInPRaw.setStatus("current")
_PemPmTable_Object = MibTable
pemPmTable = _PemPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2)
)
if mibBuilder.loadTexts:
    pemPmTable.setStatus("current")
_PemPmEntry_Object = MibTableRow
pemPmEntry = _PemPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1)
)
pemPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-PEM-MIB", "pemPmSampleDuration"),
    (0, "INFINERA-PM-PEM-MIB", "pemPmTimestamp"),
)
if mibBuilder.loadTexts:
    pemPmEntry.setStatus("current")


class _PemPmTimestamp_Type(Integer32):
    """Custom type pemPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_PemPmTimestamp_Type.__name__ = "Integer32"
_PemPmTimestamp_Object = MibTableColumn
pemPmTimestamp = _PemPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 1),
    _PemPmTimestamp_Type()
)
pemPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pemPmTimestamp.setStatus("current")


class _PemPmSampleDuration_Type(Integer32):
    """Custom type pemPmSampleDuration based on Integer32"""
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


_PemPmSampleDuration_Type.__name__ = "Integer32"
_PemPmSampleDuration_Object = MibTableColumn
pemPmSampleDuration = _PemPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 2),
    _PemPmSampleDuration_Type()
)
pemPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pemPmSampleDuration.setStatus("current")
_PemPmValidity_Type = TruthValue
_PemPmValidity_Object = MibTableColumn
pemPmValidity = _PemPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 3),
    _PemPmValidity_Type()
)
pemPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmValidity.setStatus("current")
_PemPmInVMin_Type = FloatThousandths
_PemPmInVMin_Object = MibTableColumn
pemPmInVMin = _PemPmInVMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 4),
    _PemPmInVMin_Type()
)
pemPmInVMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmInVMin.setStatus("current")
_PemPmInVMax_Type = FloatThousandths
_PemPmInVMax_Object = MibTableColumn
pemPmInVMax = _PemPmInVMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 5),
    _PemPmInVMax_Type()
)
pemPmInVMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmInVMax.setStatus("current")
_PemPmInVAvg_Type = FloatThousandths
_PemPmInVAvg_Object = MibTableColumn
pemPmInVAvg = _PemPmInVAvg_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 6),
    _PemPmInVAvg_Type()
)
pemPmInVAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmInVAvg.setStatus("current")
_PemPmInCMin_Type = FloatThousandths
_PemPmInCMin_Object = MibTableColumn
pemPmInCMin = _PemPmInCMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 7),
    _PemPmInCMin_Type()
)
pemPmInCMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmInCMin.setStatus("current")
_PemPmInCMax_Type = FloatThousandths
_PemPmInCMax_Object = MibTableColumn
pemPmInCMax = _PemPmInCMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 8),
    _PemPmInCMax_Type()
)
pemPmInCMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmInCMax.setStatus("current")
_PemPmInCAvg_Type = FloatThousandths
_PemPmInCAvg_Object = MibTableColumn
pemPmInCAvg = _PemPmInCAvg_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 9),
    _PemPmInCAvg_Type()
)
pemPmInCAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmInCAvg.setStatus("current")
_PemPmInPMin_Type = FloatThousandths
_PemPmInPMin_Object = MibTableColumn
pemPmInPMin = _PemPmInPMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 10),
    _PemPmInPMin_Type()
)
pemPmInPMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmInPMin.setStatus("current")
_PemPmInPMax_Type = FloatThousandths
_PemPmInPMax_Object = MibTableColumn
pemPmInPMax = _PemPmInPMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 11),
    _PemPmInPMax_Type()
)
pemPmInPMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmInPMax.setStatus("current")
_PemPmInPAvg_Type = FloatThousandths
_PemPmInPAvg_Object = MibTableColumn
pemPmInPAvg = _PemPmInPAvg_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 2, 1, 12),
    _PemPmInPAvg_Type()
)
pemPmInPAvg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pemPmInPAvg.setStatus("current")
_PemPmConformance_ObjectIdentity = ObjectIdentity
pemPmConformance = _PemPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 3)
)
_PemPmCompliances_ObjectIdentity = ObjectIdentity
pemPmCompliances = _PemPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 3, 1)
)
_PemPmGroups_ObjectIdentity = ObjectIdentity
pemPmGroups = _PemPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 3, 2)
)

# Managed Objects groups

pemPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 3, 2, 1)
)
pemPmGroup.setObjects(
      *(("INFINERA-PM-PEM-MIB", "pemPmValidity"),
        ("INFINERA-PM-PEM-MIB", "pemPmInVMin"),
        ("INFINERA-PM-PEM-MIB", "pemPmInVMax"),
        ("INFINERA-PM-PEM-MIB", "pemPmInVAvg"),
        ("INFINERA-PM-PEM-MIB", "pemPmInCMin"),
        ("INFINERA-PM-PEM-MIB", "pemPmInCMax"),
        ("INFINERA-PM-PEM-MIB", "pemPmInCAvg"),
        ("INFINERA-PM-PEM-MIB", "pemPmInPMin"),
        ("INFINERA-PM-PEM-MIB", "pemPmInPMax"),
        ("INFINERA-PM-PEM-MIB", "pemPmInPAvg"))
)
if mibBuilder.loadTexts:
    pemPmGroup.setStatus("current")

pemPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 3, 2, 2)
)
pemPmRealGroup.setObjects(
      *(("INFINERA-PM-PEM-MIB", "pemPmRealInVRaw"),
        ("INFINERA-PM-PEM-MIB", "pemPmRealInCRaw"),
        ("INFINERA-PM-PEM-MIB", "pemPmRealInPRaw"))
)
if mibBuilder.loadTexts:
    pemPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

pemPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 3, 1, 1)
)
pemPmCompliance.setObjects(
    ("INFINERA-PM-PEM-MIB", "pemPmRealGroup")
)
if mibBuilder.loadTexts:
    pemPmCompliance.setStatus(
        "current"
    )

pemPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 11, 5, 3, 1, 2)
)
pemPmRealCompliance.setObjects(
    ("INFINERA-PM-PEM-MIB", "pemPmRealGroup")
)
if mibBuilder.loadTexts:
    pemPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-PEM-MIB",
    **{"pemPmMIB": pemPmMIB,
       "pemPmRealTable": pemPmRealTable,
       "pemPmRealEntry": pemPmRealEntry,
       "pemPmRealInVRaw": pemPmRealInVRaw,
       "pemPmRealInCRaw": pemPmRealInCRaw,
       "pemPmRealInPRaw": pemPmRealInPRaw,
       "pemPmTable": pemPmTable,
       "pemPmEntry": pemPmEntry,
       "pemPmTimestamp": pemPmTimestamp,
       "pemPmSampleDuration": pemPmSampleDuration,
       "pemPmValidity": pemPmValidity,
       "pemPmInVMin": pemPmInVMin,
       "pemPmInVMax": pemPmInVMax,
       "pemPmInVAvg": pemPmInVAvg,
       "pemPmInCMin": pemPmInCMin,
       "pemPmInCMax": pemPmInCMax,
       "pemPmInCAvg": pemPmInCAvg,
       "pemPmInPMin": pemPmInPMin,
       "pemPmInPMax": pemPmInPMax,
       "pemPmInPAvg": pemPmInPAvg,
       "pemPmConformance": pemPmConformance,
       "pemPmCompliances": pemPmCompliances,
       "pemPmCompliance": pemPmCompliance,
       "pemPmRealCompliance": pemPmRealCompliance,
       "pemPmGroups": pemPmGroups,
       "pemPmGroup": pemPmGroup,
       "pemPmRealGroup": pemPmRealGroup}
)
