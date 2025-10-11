# SNMP MIB module (ZYXEL-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-OAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:01:51 2025
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

zyxelOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelOamSetup_ObjectIdentity = ObjectIdentity
zyxelOamSetup = _ZyxelOamSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1)
)
_ZyOamState_Type = EnabledStatus
_ZyOamState_Object = MibScalar
zyOamState = _ZyOamState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 1),
    _ZyOamState_Type()
)
zyOamState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOamState.setStatus("current")
_ZyxelOamPortTable_Object = MibTable
zyxelOamPortTable = _ZyxelOamPortTable_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2)
)
if mibBuilder.loadTexts:
    zyxelOamPortTable.setStatus("current")
_ZyxelOamPortEntry_Object = MibTableRow
zyxelOamPortEntry = _ZyxelOamPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1)
)
zyxelOamPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zyxelOamPortEntry.setStatus("current")


class _ZyOamPortFunctionsSupported_Type(Bits):
    """Custom type zyOamPortFunctionsSupported based on Bits"""
    namedValues = NamedValues(
        *(("unidirectionalSupport", 0),
          ("loopbackSupport", 1),
          ("eventSupport", 2),
          ("variableSupport", 3))
    )

_ZyOamPortFunctionsSupported_Type.__name__ = "Bits"
_ZyOamPortFunctionsSupported_Object = MibTableColumn
zyOamPortFunctionsSupported = _ZyOamPortFunctionsSupported_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 56, 1, 2, 1, 1),
    _ZyOamPortFunctionsSupported_Type()
)
zyOamPortFunctionsSupported.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zyOamPortFunctionsSupported.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-OAM-MIB",
    **{"zyxelOam": zyxelOam,
       "zyxelOamSetup": zyxelOamSetup,
       "zyOamState": zyOamState,
       "zyxelOamPortTable": zyxelOamPortTable,
       "zyxelOamPortEntry": zyxelOamPortEntry,
       "zyOamPortFunctionsSupported": zyOamPortFunctionsSupported}
)
