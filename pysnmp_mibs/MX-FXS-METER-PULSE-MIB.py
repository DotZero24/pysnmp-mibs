# SNMP MIB module (MX-FXS-METER-PULSE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-FXS-METER-PULSE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:33 2025
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

(mediatrixExperimental,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixExperimental")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fxsMeterPulseMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30)
)
if mibBuilder.loadTexts:
    fxsMeterPulseMIB.setRevisions(
        ("1902-11-04 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FxsMeterPulseMIBObjects_ObjectIdentity = ObjectIdentity
fxsMeterPulseMIBObjects = _FxsMeterPulseMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 1)
)
_FxsMeterPulseTable_Object = MibTable
fxsMeterPulseTable = _FxsMeterPulseTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 1, 30)
)
if mibBuilder.loadTexts:
    fxsMeterPulseTable.setStatus("current")
_FxsMeterPulseEntry_Object = MibTableRow
fxsMeterPulseEntry = _FxsMeterPulseEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 1, 30, 1)
)
fxsMeterPulseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fxsMeterPulseEntry.setStatus("current")


class _FxsMeterPulseDuration_Type(Unsigned32):
    """Custom type fxsMeterPulseDuration based on Unsigned32"""
    defaultValue = 160

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 220),
    )


_FxsMeterPulseDuration_Type.__name__ = "Unsigned32"
_FxsMeterPulseDuration_Object = MibTableColumn
fxsMeterPulseDuration = _FxsMeterPulseDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 1, 30, 1, 10),
    _FxsMeterPulseDuration_Type()
)
fxsMeterPulseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsMeterPulseDuration.setStatus("current")


class _FxsMeterPauseDuration_Type(Unsigned32):
    """Custom type fxsMeterPauseDuration based on Unsigned32"""
    defaultValue = 360

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(100, 600),
    )


_FxsMeterPauseDuration_Type.__name__ = "Unsigned32"
_FxsMeterPauseDuration_Object = MibTableColumn
fxsMeterPauseDuration = _FxsMeterPauseDuration_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 1, 30, 1, 15),
    _FxsMeterPauseDuration_Type()
)
fxsMeterPauseDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsMeterPauseDuration.setStatus("current")


class _FxsMeterPulseFreq_Type(Integer32):
    """Custom type fxsMeterPulseFreq based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("freq-12-kHz", 1),
          ("freq-16-kHz", 2))
    )


_FxsMeterPulseFreq_Type.__name__ = "Integer32"
_FxsMeterPulseFreq_Object = MibScalar
fxsMeterPulseFreq = _FxsMeterPulseFreq_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 1, 35),
    _FxsMeterPulseFreq_Type()
)
fxsMeterPulseFreq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fxsMeterPulseFreq.setStatus("current")
_FxsMeterPulseConformance_ObjectIdentity = ObjectIdentity
fxsMeterPulseConformance = _FxsMeterPulseConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 2)
)
_FxsMeterPulseCompliances_ObjectIdentity = ObjectIdentity
fxsMeterPulseCompliances = _FxsMeterPulseCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 2, 1)
)
_FxsMeterPulseGroups_ObjectIdentity = ObjectIdentity
fxsMeterPulseGroups = _FxsMeterPulseGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 2, 2)
)

# Managed Objects groups

fxsMeterPulseGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 2, 2, 1)
)
fxsMeterPulseGroupVer1.setObjects(
      *(("MX-FXS-METER-PULSE-MIB", "fxsMeterPulseDuration"),
        ("MX-FXS-METER-PULSE-MIB", "fxsMeterPauseDuration"),
        ("MX-FXS-METER-PULSE-MIB", "fxsMeterPulseFreq"))
)
if mibBuilder.loadTexts:
    fxsMeterPulseGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fxsMeterPulseBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 30, 2, 1, 1)
)
fxsMeterPulseBasicComplVer1.setObjects(
    ("MX-FXS-METER-PULSE-MIB", "fxsMeterPulseGroupVer1")
)
if mibBuilder.loadTexts:
    fxsMeterPulseBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-FXS-METER-PULSE-MIB",
    **{"fxsMeterPulseMIB": fxsMeterPulseMIB,
       "fxsMeterPulseMIBObjects": fxsMeterPulseMIBObjects,
       "fxsMeterPulseTable": fxsMeterPulseTable,
       "fxsMeterPulseEntry": fxsMeterPulseEntry,
       "fxsMeterPulseDuration": fxsMeterPulseDuration,
       "fxsMeterPauseDuration": fxsMeterPauseDuration,
       "fxsMeterPulseFreq": fxsMeterPulseFreq,
       "fxsMeterPulseConformance": fxsMeterPulseConformance,
       "fxsMeterPulseCompliances": fxsMeterPulseCompliances,
       "fxsMeterPulseBasicComplVer1": fxsMeterPulseBasicComplVer1,
       "fxsMeterPulseGroups": fxsMeterPulseGroups,
       "fxsMeterPulseGroupVer1": fxsMeterPulseGroupVer1}
)
