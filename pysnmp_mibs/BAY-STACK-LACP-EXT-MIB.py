# SNMP MIB module (BAY-STACK-LACP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/BAY-STACK-LACP-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:19:03 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackLacpExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 7)
)
if mibBuilder.loadTexts:
    bayStackLacpExtMib.setRevisions(
        ("2005-11-14 00:00",
         "2004-06-04 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsleNotifications_ObjectIdentity = ObjectIdentity
bsleNotifications = _BsleNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 7, 0)
)
_BsleObjects_ObjectIdentity = ObjectIdentity
bsleObjects = _BsleObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 7, 1)
)
_BsleScalars_ObjectIdentity = ObjectIdentity
bsleScalars = _BsleScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 7, 1, 1)
)


class _BsleDot3adCompatibilityMode_Type(Integer32):
    """Custom type bsleDot3adCompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("advanced", 2))
    )


_BsleDot3adCompatibilityMode_Type.__name__ = "Integer32"
_BsleDot3adCompatibilityMode_Object = MibScalar
bsleDot3adCompatibilityMode = _BsleDot3adCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 7, 1, 1, 1),
    _BsleDot3adCompatibilityMode_Type()
)
bsleDot3adCompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsleDot3adCompatibilityMode.setStatus("current")
_BsleDot3adAggPortExtTable_Object = MibTable
bsleDot3adAggPortExtTable = _BsleDot3adAggPortExtTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 7, 2)
)
if mibBuilder.loadTexts:
    bsleDot3adAggPortExtTable.setStatus("current")
_BsleDot3adAggPortExtEntry_Object = MibTableRow
bsleDot3adAggPortExtEntry = _BsleDot3adAggPortExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 7, 2, 1)
)
bsleDot3adAggPortExtEntry.setIndexNames(
    (0, "BAY-STACK-LACP-EXT-MIB", "bsleDot3adAggPortExtIndex"),
)
if mibBuilder.loadTexts:
    bsleDot3adAggPortExtEntry.setStatus("current")
_BsleDot3adAggPortExtIndex_Type = InterfaceIndex
_BsleDot3adAggPortExtIndex_Object = MibTableColumn
bsleDot3adAggPortExtIndex = _BsleDot3adAggPortExtIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 7, 2, 1, 1),
    _BsleDot3adAggPortExtIndex_Type()
)
bsleDot3adAggPortExtIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsleDot3adAggPortExtIndex.setStatus("current")
_BsleDot3adAggPortExtAdminEnabled_Type = TruthValue
_BsleDot3adAggPortExtAdminEnabled_Object = MibTableColumn
bsleDot3adAggPortExtAdminEnabled = _BsleDot3adAggPortExtAdminEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 7, 2, 1, 2),
    _BsleDot3adAggPortExtAdminEnabled_Type()
)
bsleDot3adAggPortExtAdminEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsleDot3adAggPortExtAdminEnabled.setStatus("current")
_BsleDot3adAggPortExtOperEnabled_Type = TruthValue
_BsleDot3adAggPortExtOperEnabled_Object = MibTableColumn
bsleDot3adAggPortExtOperEnabled = _BsleDot3adAggPortExtOperEnabled_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 7, 2, 1, 3),
    _BsleDot3adAggPortExtOperEnabled_Type()
)
bsleDot3adAggPortExtOperEnabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsleDot3adAggPortExtOperEnabled.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-LACP-EXT-MIB",
    **{"bayStackLacpExtMib": bayStackLacpExtMib,
       "bsleNotifications": bsleNotifications,
       "bsleObjects": bsleObjects,
       "bsleScalars": bsleScalars,
       "bsleDot3adCompatibilityMode": bsleDot3adCompatibilityMode,
       "bsleDot3adAggPortExtTable": bsleDot3adAggPortExtTable,
       "bsleDot3adAggPortExtEntry": bsleDot3adAggPortExtEntry,
       "bsleDot3adAggPortExtIndex": bsleDot3adAggPortExtIndex,
       "bsleDot3adAggPortExtAdminEnabled": bsleDot3adAggPortExtAdminEnabled,
       "bsleDot3adAggPortExtOperEnabled": bsleDot3adAggPortExtOperEnabled}
)
