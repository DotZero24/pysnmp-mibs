# SNMP MIB module (RUGGEDCOM-TIMECONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-TIMECONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:48 2025
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

(ruggedcomMgmt,) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomMgmt")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rcTimeConfig = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11)
)
if mibBuilder.loadTexts:
    rcTimeConfig.setRevisions(
        ("2015-09-28 13:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RcTimeSyncStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("disabled", 2),
          ("locked", 3),
          ("searching", 4),
          ("aquiring", 5),
          ("holdover", 6),
          ("parity", 7),
          ("decoder", 8),
          ("shortckt", 9),
          ("cfgfailure", 10))
    )



# MIB Managed Objects in the order of their OIDs

_RcTimeConfigBase_ObjectIdentity = ObjectIdentity
rcTimeConfigBase = _RcTimeConfigBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11, 1)
)


class _RcTimeSource_Type(Integer32):
    """Custom type rcTimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("irigb", 2),
          ("gps", 3),
          ("ieee1588", 4),
          ("ntp", 5),
          ("localclk", 6))
    )


_RcTimeSource_Type.__name__ = "Integer32"
_RcTimeSource_Object = MibScalar
rcTimeSource = _RcTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 1),
    _RcTimeSource_Type()
)
rcTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTimeSource.setStatus("current")
_RcTimeAndDate_Type = DateAndTime
_RcTimeAndDate_Object = MibScalar
rcTimeAndDate = _RcTimeAndDate_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 2),
    _RcTimeAndDate_Type()
)
rcTimeAndDate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTimeAndDate.setStatus("current")


class _RcDSTOfst_Type(Unsigned32):
    """Custom type rcDSTOfst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86399),
    )


_RcDSTOfst_Type.__name__ = "Unsigned32"
_RcDSTOfst_Object = MibScalar
rcDSTOfst = _RcDSTOfst_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 3),
    _RcDSTOfst_Type()
)
rcDSTOfst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDSTOfst.setStatus("current")
if mibBuilder.loadTexts:
    rcDSTOfst.setUnits("seconds")


class _RcCurrentUTCOfst_Type(Unsigned32):
    """Custom type rcCurrentUTCOfst based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcCurrentUTCOfst_Type.__name__ = "Unsigned32"
_RcCurrentUTCOfst_Object = MibScalar
rcCurrentUTCOfst = _RcCurrentUTCOfst_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 4),
    _RcCurrentUTCOfst_Type()
)
rcCurrentUTCOfst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcCurrentUTCOfst.setStatus("current")
if mibBuilder.loadTexts:
    rcCurrentUTCOfst.setUnits("seconds")
_RcLeapSecPending_Type = TruthValue
_RcLeapSecPending_Object = MibScalar
rcLeapSecPending = _RcLeapSecPending_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 5),
    _RcLeapSecPending_Type()
)
rcLeapSecPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcLeapSecPending.setStatus("current")


class _RcDSTRule_Type(DisplayString):
    """Custom type rcDSTRule based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcDSTRule_Type.__name__ = "DisplayString"
_RcDSTRule_Object = MibScalar
rcDSTRule = _RcDSTRule_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11, 1, 6),
    _RcDSTRule_Type()
)
rcDSTRule.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDSTRule.setStatus("current")
_RcTimeConfigConformance_ObjectIdentity = ObjectIdentity
rcTimeConfigConformance = _RcTimeConfigConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11, 3)
)
_RcTimeConfigGroups_ObjectIdentity = ObjectIdentity
rcTimeConfigGroups = _RcTimeConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11, 3, 2)
)

# Managed Objects groups

rcTimeConfigBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 11, 3, 2, 1)
)
rcTimeConfigBaseGroup.setObjects(
      *(("RUGGEDCOM-TIMECONFIG-MIB", "rcTimeSource"),
        ("RUGGEDCOM-TIMECONFIG-MIB", "rcTimeAndDate"),
        ("RUGGEDCOM-TIMECONFIG-MIB", "rcDSTOfst"),
        ("RUGGEDCOM-TIMECONFIG-MIB", "rcCurrentUTCOfst"),
        ("RUGGEDCOM-TIMECONFIG-MIB", "rcLeapSecPending"),
        ("RUGGEDCOM-TIMECONFIG-MIB", "rcDSTRule"))
)
if mibBuilder.loadTexts:
    rcTimeConfigBaseGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-TIMECONFIG-MIB",
    **{"RcTimeSyncStatus": RcTimeSyncStatus,
       "rcTimeConfig": rcTimeConfig,
       "rcTimeConfigBase": rcTimeConfigBase,
       "rcTimeSource": rcTimeSource,
       "rcTimeAndDate": rcTimeAndDate,
       "rcDSTOfst": rcDSTOfst,
       "rcCurrentUTCOfst": rcCurrentUTCOfst,
       "rcLeapSecPending": rcLeapSecPending,
       "rcDSTRule": rcDSTRule,
       "rcTimeConfigConformance": rcTimeConfigConformance,
       "rcTimeConfigGroups": rcTimeConfigGroups,
       "rcTimeConfigBaseGroup": rcTimeConfigBaseGroup}
)
