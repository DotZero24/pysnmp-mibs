# SNMP MIB module (INFINERA-PM-FEEDPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-PM-FEEDPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:55 2025
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

feedPtpPmMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46)
)
if mibBuilder.loadTexts:
    feedPtpPmMIB.setRevisions(
        ("2013-10-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FeedPtpPmRealTable_Object = MibTable
feedPtpPmRealTable = _FeedPtpPmRealTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 1)
)
if mibBuilder.loadTexts:
    feedPtpPmRealTable.setStatus("current")
_FeedPtpPmRealEntry_Object = MibTableRow
feedPtpPmRealEntry = _FeedPtpPmRealEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 1, 1)
)
feedPtpPmRealEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    feedPtpPmRealEntry.setStatus("current")
_FeedPtpPmRealInputVoltage_Type = FloatHundredths
_FeedPtpPmRealInputVoltage_Object = MibTableColumn
feedPtpPmRealInputVoltage = _FeedPtpPmRealInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 1, 1, 1),
    _FeedPtpPmRealInputVoltage_Type()
)
feedPtpPmRealInputVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feedPtpPmRealInputVoltage.setStatus("current")
_FeedPtpPmRealInputCurrent_Type = FloatHundredths
_FeedPtpPmRealInputCurrent_Object = MibTableColumn
feedPtpPmRealInputCurrent = _FeedPtpPmRealInputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 1, 1, 2),
    _FeedPtpPmRealInputCurrent_Type()
)
feedPtpPmRealInputCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feedPtpPmRealInputCurrent.setStatus("current")
_FeedPtpPmTable_Object = MibTable
feedPtpPmTable = _FeedPtpPmTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2)
)
if mibBuilder.loadTexts:
    feedPtpPmTable.setStatus("current")
_FeedPtpPmEntry_Object = MibTableRow
feedPtpPmEntry = _FeedPtpPmEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2, 1)
)
feedPtpPmEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "INFINERA-PM-FEEDPTP-MIB", "feedPtpPmSampleDuration"),
    (0, "INFINERA-PM-FEEDPTP-MIB", "feedPtpPmTimestamp"),
)
if mibBuilder.loadTexts:
    feedPtpPmEntry.setStatus("current")


class _FeedPtpPmTimestamp_Type(Integer32):
    """Custom type feedPtpPmTimestamp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FeedPtpPmTimestamp_Type.__name__ = "Integer32"
_FeedPtpPmTimestamp_Object = MibTableColumn
feedPtpPmTimestamp = _FeedPtpPmTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2, 1, 1),
    _FeedPtpPmTimestamp_Type()
)
feedPtpPmTimestamp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    feedPtpPmTimestamp.setStatus("current")


class _FeedPtpPmSampleDuration_Type(Integer32):
    """Custom type feedPtpPmSampleDuration based on Integer32"""
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


_FeedPtpPmSampleDuration_Type.__name__ = "Integer32"
_FeedPtpPmSampleDuration_Object = MibTableColumn
feedPtpPmSampleDuration = _FeedPtpPmSampleDuration_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2, 1, 2),
    _FeedPtpPmSampleDuration_Type()
)
feedPtpPmSampleDuration.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    feedPtpPmSampleDuration.setStatus("current")
_FeedPtpPmValidity_Type = TruthValue
_FeedPtpPmValidity_Object = MibTableColumn
feedPtpPmValidity = _FeedPtpPmValidity_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2, 1, 3),
    _FeedPtpPmValidity_Type()
)
feedPtpPmValidity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feedPtpPmValidity.setStatus("current")
_FeedPtpPmInputVoltageMin_Type = FloatHundredths
_FeedPtpPmInputVoltageMin_Object = MibTableColumn
feedPtpPmInputVoltageMin = _FeedPtpPmInputVoltageMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2, 1, 4),
    _FeedPtpPmInputVoltageMin_Type()
)
feedPtpPmInputVoltageMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feedPtpPmInputVoltageMin.setStatus("current")
_FeedPtpPmInputVoltageMax_Type = FloatHundredths
_FeedPtpPmInputVoltageMax_Object = MibTableColumn
feedPtpPmInputVoltageMax = _FeedPtpPmInputVoltageMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2, 1, 5),
    _FeedPtpPmInputVoltageMax_Type()
)
feedPtpPmInputVoltageMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feedPtpPmInputVoltageMax.setStatus("current")
_FeedPtpPmInputVoltageAve_Type = FloatHundredths
_FeedPtpPmInputVoltageAve_Object = MibTableColumn
feedPtpPmInputVoltageAve = _FeedPtpPmInputVoltageAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2, 1, 6),
    _FeedPtpPmInputVoltageAve_Type()
)
feedPtpPmInputVoltageAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feedPtpPmInputVoltageAve.setStatus("current")
_FeedPtpPmInputCurrentMin_Type = FloatHundredths
_FeedPtpPmInputCurrentMin_Object = MibTableColumn
feedPtpPmInputCurrentMin = _FeedPtpPmInputCurrentMin_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2, 1, 7),
    _FeedPtpPmInputCurrentMin_Type()
)
feedPtpPmInputCurrentMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feedPtpPmInputCurrentMin.setStatus("current")
_FeedPtpPmInputCurrentMax_Type = FloatHundredths
_FeedPtpPmInputCurrentMax_Object = MibTableColumn
feedPtpPmInputCurrentMax = _FeedPtpPmInputCurrentMax_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2, 1, 8),
    _FeedPtpPmInputCurrentMax_Type()
)
feedPtpPmInputCurrentMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feedPtpPmInputCurrentMax.setStatus("current")
_FeedPtpPmInputCurrentAve_Type = FloatHundredths
_FeedPtpPmInputCurrentAve_Object = MibTableColumn
feedPtpPmInputCurrentAve = _FeedPtpPmInputCurrentAve_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 2, 1, 9),
    _FeedPtpPmInputCurrentAve_Type()
)
feedPtpPmInputCurrentAve.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    feedPtpPmInputCurrentAve.setStatus("current")
_FeedPtpPmConformance_ObjectIdentity = ObjectIdentity
feedPtpPmConformance = _FeedPtpPmConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 3)
)
_FeedPtpPmCompliances_ObjectIdentity = ObjectIdentity
feedPtpPmCompliances = _FeedPtpPmCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 3, 1)
)
_FeedPtpPmGroups_ObjectIdentity = ObjectIdentity
feedPtpPmGroups = _FeedPtpPmGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 3, 2)
)

# Managed Objects groups

feedPtpPmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 3, 2, 1)
)
feedPtpPmGroup.setObjects(
      *(("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmValidity"),
        ("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmInputVoltageMin"),
        ("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmInputVoltageMax"),
        ("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmInputVoltageAve"),
        ("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmInputCurrentMin"),
        ("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmInputCurrentMax"),
        ("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmInputCurrentAve"))
)
if mibBuilder.loadTexts:
    feedPtpPmGroup.setStatus("current")

feedPtpPmRealGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 3, 2, 2)
)
feedPtpPmRealGroup.setObjects(
      *(("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmRealInputVoltage"),
        ("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmRealInputCurrent"))
)
if mibBuilder.loadTexts:
    feedPtpPmRealGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

feedPtpPmCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 3, 1, 1)
)
feedPtpPmCompliance.setObjects(
    ("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmGroup")
)
if mibBuilder.loadTexts:
    feedPtpPmCompliance.setStatus(
        "current"
    )

feedPtpPmRealCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 3, 46, 3, 1, 2)
)
feedPtpPmRealCompliance.setObjects(
    ("INFINERA-PM-FEEDPTP-MIB", "feedPtpPmRealGroup")
)
if mibBuilder.loadTexts:
    feedPtpPmRealCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-PM-FEEDPTP-MIB",
    **{"feedPtpPmMIB": feedPtpPmMIB,
       "feedPtpPmRealTable": feedPtpPmRealTable,
       "feedPtpPmRealEntry": feedPtpPmRealEntry,
       "feedPtpPmRealInputVoltage": feedPtpPmRealInputVoltage,
       "feedPtpPmRealInputCurrent": feedPtpPmRealInputCurrent,
       "feedPtpPmTable": feedPtpPmTable,
       "feedPtpPmEntry": feedPtpPmEntry,
       "feedPtpPmTimestamp": feedPtpPmTimestamp,
       "feedPtpPmSampleDuration": feedPtpPmSampleDuration,
       "feedPtpPmValidity": feedPtpPmValidity,
       "feedPtpPmInputVoltageMin": feedPtpPmInputVoltageMin,
       "feedPtpPmInputVoltageMax": feedPtpPmInputVoltageMax,
       "feedPtpPmInputVoltageAve": feedPtpPmInputVoltageAve,
       "feedPtpPmInputCurrentMin": feedPtpPmInputCurrentMin,
       "feedPtpPmInputCurrentMax": feedPtpPmInputCurrentMax,
       "feedPtpPmInputCurrentAve": feedPtpPmInputCurrentAve,
       "feedPtpPmConformance": feedPtpPmConformance,
       "feedPtpPmCompliances": feedPtpPmCompliances,
       "feedPtpPmCompliance": feedPtpPmCompliance,
       "feedPtpPmRealCompliance": feedPtpPmRealCompliance,
       "feedPtpPmGroups": feedPtpPmGroups,
       "feedPtpPmGroup": feedPtpPmGroup,
       "feedPtpPmRealGroup": feedPtpPmRealGroup}
)
