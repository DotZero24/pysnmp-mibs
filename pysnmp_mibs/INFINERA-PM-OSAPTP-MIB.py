# SNMP MIB module (INFINERA-PM-OSAPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-OSAPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:24 2025
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

osaPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19)
)
if mibBuilder.loadTexts:
    osaPtpPmMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OsaPtpPmRealTable_Object = MibTable
osaPtpPmRealTable = _OsaPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 1)
)
if mibBuilder.loadTexts:
    osaPtpPmRealTable.setStatus("current")
_OsaPtpPmRealEntry_Object = MibTableRow
osaPtpPmRealEntry = _OsaPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 1, 1)
)
osaPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    osaPtpPmRealEntry.setStatus("current")
_OsaPtpPmRealOpr_Type = FloatHundredths
_OsaPtpPmRealOpr_Object = MibTableColumn
osaPtpPmRealOpr = _OsaPtpPmRealOpr_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 1, 1, 1),
    _OsaPtpPmRealOpr_Type()
)
osaPtpPmRealOpr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaPtpPmRealOpr.setStatus("current")
_OsaOprOsaTapRatio_Type = FloatHundredths
_OsaOprOsaTapRatio_Object = MibTableColumn
osaOprOsaTapRatio = _OsaOprOsaTapRatio_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 1, 1, 2),
    _OsaOprOsaTapRatio_Type()
)
osaOprOsaTapRatio.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaOprOsaTapRatio.setStatus("current")
_OsaPtpPmTable_Object = MibTable
osaPtpPmTable = _OsaPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2)
)
if mibBuilder.loadTexts:
    osaPtpPmTable.setStatus("current")
_OsaPtpPmEntry_Object = MibTableRow
osaPtpPmEntry = _OsaPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1)
)
osaPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-OSAPTP-MIB", "osaPtpPmSampleDuration"),
    (0, "INFINERA-PM-OSAPTP-MIB", "osaPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    osaPtpPmEntry.setStatus("current")


class _OsaPtpPmTimestamp_Type(Integer32):
    """Custom type osaPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_OsaPtpPmTimestamp_Type.__name__ = "Integer32"
_OsaPtpPmTimestamp_Object = MibTableColumn
osaPtpPmTimestamp = _OsaPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 1),
    _OsaPtpPmTimestamp_Type()
)
osaPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osaPtpPmTimestamp.setStatus("current")


class _OsaPtpPmSampleDuration_Type(Integer32):
    """Custom type osaPtpPmSampleDuration based on Integer32"""
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


_OsaPtpPmSampleDuration_Type.__name__ = "Integer32"
_OsaPtpPmSampleDuration_Object = MibTableColumn
osaPtpPmSampleDuration = _OsaPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 2),
    _OsaPtpPmSampleDuration_Type()
)
osaPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    osaPtpPmSampleDuration.setStatus("current")
_OsaPtpPmValidity_Type = TruthValue
_OsaPtpPmValidity_Object = MibTableColumn
osaPtpPmValidity = _OsaPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 3),
    _OsaPtpPmValidity_Type()
)
osaPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaPtpPmValidity.setStatus("current")
_OsaPtpPmOprMin_Type = FloatHundredths
_OsaPtpPmOprMin_Object = MibTableColumn
osaPtpPmOprMin = _OsaPtpPmOprMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 4),
    _OsaPtpPmOprMin_Type()
)
osaPtpPmOprMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaPtpPmOprMin.setStatus("current")
_OsaPtpPmOprMax_Type = FloatHundredths
_OsaPtpPmOprMax_Object = MibTableColumn
osaPtpPmOprMax = _OsaPtpPmOprMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 5),
    _OsaPtpPmOprMax_Type()
)
osaPtpPmOprMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaPtpPmOprMax.setStatus("current")
_OsaPtpPmOprAve_Type = FloatHundredths
_OsaPtpPmOprAve_Object = MibTableColumn
osaPtpPmOprAve = _OsaPtpPmOprAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 2, 1, 6),
    _OsaPtpPmOprAve_Type()
)
osaPtpPmOprAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    osaPtpPmOprAve.setStatus("current")
_OsaPtpPmConformance_ObjectIdentity = ObjectIdentity
osaPtpPmConformance = _OsaPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3)
)
_OsaPtpPmCompliances_ObjectIdentity = ObjectIdentity
osaPtpPmCompliances = _OsaPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 1)
)
_OsaPtpPmGroups_ObjectIdentity = ObjectIdentity
osaPtpPmGroups = _OsaPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 2)
)

# Managed Objects groups

osaPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 2, 1)
)
osaPtpPmGroup.setObjects(
      *(("INFINERA-PM-OSAPTP-MIB", "osaPtpPmValidity"),
        ("INFINERA-PM-OSAPTP-MIB", "osaPtpPmOprMin"),
        ("INFINERA-PM-OSAPTP-MIB", "osaPtpPmOprMax"),
        ("INFINERA-PM-OSAPTP-MIB", "osaPtpPmOprAve"))
)
if mibBuilder.loadTexts:
    osaPtpPmGroup.setStatus("current")

osaPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 2, 2)
)
osaPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-OSAPTP-MIB", "osaPtpPmRealOpr"),
        ("INFINERA-PM-OSAPTP-MIB", "osaOprOsaTapRatio"))
)
if mibBuilder.loadTexts:
    osaPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

osaPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 1, 1)
)
osaPtpPmCompliance.setObjects(
    ("INFINERA-PM-OSAPTP-MIB", "osaPtpPmGroup")
)
if mibBuilder.loadTexts:
    osaPtpPmCompliance.setStatus(
        "current"
    )

osaPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 19, 3, 1, 2)
)
osaPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-OSAPTP-MIB", "osaPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    osaPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-OSAPTP-MIB",
    **{"osaPtpPmMIB": osaPtpPmMIB,
       "osaPtpPmRealTable": osaPtpPmRealTable,
       "osaPtpPmRealEntry": osaPtpPmRealEntry,
       "osaPtpPmRealOpr": osaPtpPmRealOpr,
       "osaOprOsaTapRatio": osaOprOsaTapRatio,
       "osaPtpPmTable": osaPtpPmTable,
       "osaPtpPmEntry": osaPtpPmEntry,
       "osaPtpPmTimestamp": osaPtpPmTimestamp,
       "osaPtpPmSampleDuration": osaPtpPmSampleDuration,
       "osaPtpPmValidity": osaPtpPmValidity,
       "osaPtpPmOprMin": osaPtpPmOprMin,
       "osaPtpPmOprMax": osaPtpPmOprMax,
       "osaPtpPmOprAve": osaPtpPmOprAve,
       "osaPtpPmConformance": osaPtpPmConformance,
       "osaPtpPmCompliances": osaPtpPmCompliances,
       "osaPtpPmCompliance": osaPtpPmCompliance,
       "osaPtpPmRealCompliance": osaPtpPmRealCompliance,
       "osaPtpPmGroups": osaPtpPmGroups,
       "osaPtpPmGroup": osaPtpPmGroup,
       "osaPtpPmRealGroup": osaPtpPmRealGroup}
)
