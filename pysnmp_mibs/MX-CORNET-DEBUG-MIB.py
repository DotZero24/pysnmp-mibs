# SNMP MIB module (MX-CORNET-DEBUG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-CORNET-DEBUG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:00 2025
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

corNetDebugMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 110)
)
if mibBuilder.loadTexts:
    corNetDebugMIB.setRevisions(
        ("2005-05-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_CorNetDebugMIBObjects_ObjectIdentity = ObjectIdentity
corNetDebugMIBObjects = _CorNetDebugMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 110, 1)
)


class _CorNetDebugToMSecTraceLevel_Type(Integer32):
    """Custom type corNetDebugToMSecTraceLevel based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              10,
              20,
              30,
              40,
              50,
              1000)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("error", 10),
          ("warning", 20),
          ("highPriorityInfo", 30),
          ("mediumPriorityInfo", 40),
          ("lowPriorityInfo", 50),
          ("all", 1000))
    )


_CorNetDebugToMSecTraceLevel_Type.__name__ = "Integer32"
_CorNetDebugToMSecTraceLevel_Object = MibScalar
corNetDebugToMSecTraceLevel = _CorNetDebugToMSecTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 4935, 99, 110, 1, 50),
    _CorNetDebugToMSecTraceLevel_Type()
)
corNetDebugToMSecTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    corNetDebugToMSecTraceLevel.setStatus("current")
_CorNetDebugConformance_ObjectIdentity = ObjectIdentity
corNetDebugConformance = _CorNetDebugConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 110, 2)
)
_CorNetDebugCompliances_ObjectIdentity = ObjectIdentity
corNetDebugCompliances = _CorNetDebugCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 110, 2, 1)
)
_CorNetDebugGroups_ObjectIdentity = ObjectIdentity
corNetDebugGroups = _CorNetDebugGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 99, 110, 2, 2)
)

# Managed Objects groups

corNetDebugGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 99, 110, 2, 2, 5)
)
corNetDebugGroupVer1.setObjects(
    ("MX-CORNET-DEBUG-MIB", "corNetDebugToMSecTraceLevel")
)
if mibBuilder.loadTexts:
    corNetDebugGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

corNetDebugBasicComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 99, 110, 2, 1, 5)
)
corNetDebugBasicComplVer1.setObjects(
    ("MX-CORNET-DEBUG-MIB", "corNetDebugGroupVer1")
)
if mibBuilder.loadTexts:
    corNetDebugBasicComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-CORNET-DEBUG-MIB",
    **{"corNetDebugMIB": corNetDebugMIB,
       "corNetDebugMIBObjects": corNetDebugMIBObjects,
       "corNetDebugToMSecTraceLevel": corNetDebugToMSecTraceLevel,
       "corNetDebugConformance": corNetDebugConformance,
       "corNetDebugCompliances": corNetDebugCompliances,
       "corNetDebugBasicComplVer1": corNetDebugBasicComplVer1,
       "corNetDebugGroups": corNetDebugGroups,
       "corNetDebugGroupVer1": corNetDebugGroupVer1}
)
