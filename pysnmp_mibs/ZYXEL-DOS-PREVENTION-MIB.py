# SNMP MIB module (ZYXEL-DOS-PREVENTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-DOS-PREVENTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:27 2025
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

(dot1dBasePort,) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "dot1dBasePort")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelDoSPrevention = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelDoSPreventionSetup_ObjectIdentity = ObjectIdentity
zyxelDoSPreventionSetup = _ZyxelDoSPreventionSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119, 1)
)
_ZyDoSPreventionState_Type = EnabledStatus
_ZyDoSPreventionState_Object = MibScalar
zyDoSPreventionState = _ZyDoSPreventionState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119, 1, 1),
    _ZyDoSPreventionState_Type()
)
zyDoSPreventionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDoSPreventionState.setStatus("current")
_ZyxelDoSPreventionPortTable_Object = MibTable
zyxelDoSPreventionPortTable = _ZyxelDoSPreventionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelDoSPreventionPortTable.setStatus("current")
_ZyxelDoSPreventionPortEntry_Object = MibTableRow
zyxelDoSPreventionPortEntry = _ZyxelDoSPreventionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119, 1, 2, 1)
)
zyxelDoSPreventionPortEntry.setIndexNames(
    (0, "BRIDGE-MIB", "dot1dBasePort"),
)
if mibBuilder.loadTexts:
    zyxelDoSPreventionPortEntry.setStatus("current")
_ZyDoSPreventionPortState_Type = EnabledStatus
_ZyDoSPreventionPortState_Object = MibTableColumn
zyDoSPreventionPortState = _ZyDoSPreventionPortState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 119, 1, 2, 1, 1),
    _ZyDoSPreventionPortState_Type()
)
zyDoSPreventionPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyDoSPreventionPortState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-DOS-PREVENTION-MIB",
    **{"zyxelDoSPrevention": zyxelDoSPrevention,
       "zyxelDoSPreventionSetup": zyxelDoSPreventionSetup,
       "zyDoSPreventionState": zyDoSPreventionState,
       "zyxelDoSPreventionPortTable": zyxelDoSPreventionPortTable,
       "zyxelDoSPreventionPortEntry": zyxelDoSPreventionPortEntry,
       "zyDoSPreventionPortState": zyDoSPreventionPortState}
)
