# SNMP MIB module (RAISECOM-DOT1X-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-DOT1X-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:13 2025
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

(dot1xPaePortEntry,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xPaePortEntry")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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


# MODULE-IDENTITY

rcDot1x = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 27)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcDot1xObjects_ObjectIdentity = ObjectIdentity
rcDot1xObjects = _RcDot1xObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1)
)
_RcDot1xConfig_ObjectIdentity = ObjectIdentity
rcDot1xConfig = _RcDot1xConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1)
)
_Dot1xPortTable_Object = MibTable
dot1xPortTable = _Dot1xPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot1xPortTable.setStatus("current")
_Dot1xPortEntry_Object = MibTableRow
dot1xPortEntry = _Dot1xPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dot1xPortEntry.setStatus("current")


class _Rcdot1xPortAuthControl_Type(Integer32):
    """Custom type rcdot1xPortAuthControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_Rcdot1xPortAuthControl_Type.__name__ = "Integer32"
_Rcdot1xPortAuthControl_Object = MibTableColumn
rcdot1xPortAuthControl = _Rcdot1xPortAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1, 1, 1, 1),
    _Rcdot1xPortAuthControl_Type()
)
rcdot1xPortAuthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcdot1xPortAuthControl.setStatus("current")
_Rcdot1xPortStatisticClear_Type = TruthValue
_Rcdot1xPortStatisticClear_Object = MibTableColumn
rcdot1xPortStatisticClear = _Rcdot1xPortStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1, 1, 1, 2),
    _Rcdot1xPortStatisticClear_Type()
)
rcdot1xPortStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcdot1xPortStatisticClear.setStatus("current")


class _Rcdot1xPortAuthMethod_Type(Integer32):
    """Custom type rcdot1xPortAuthMethod based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portbased", 1),
          ("macbased", 2))
    )


_Rcdot1xPortAuthMethod_Type.__name__ = "Integer32"
_Rcdot1xPortAuthMethod_Object = MibTableColumn
rcdot1xPortAuthMethod = _Rcdot1xPortAuthMethod_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 27, 1, 1, 1, 1, 3),
    _Rcdot1xPortAuthMethod_Type()
)
rcdot1xPortAuthMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcdot1xPortAuthMethod.setStatus("current")
dot1xPaePortEntry.registerAugmentions(
    ("RAISECOM-DOT1X-MIB",
     "dot1xPortEntry")
)
dot1xPortEntry.setIndexNames(*dot1xPaePortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-DOT1X-MIB",
    **{"rcDot1x": rcDot1x,
       "rcDot1xObjects": rcDot1xObjects,
       "rcDot1xConfig": rcDot1xConfig,
       "dot1xPortTable": dot1xPortTable,
       "dot1xPortEntry": dot1xPortEntry,
       "rcdot1xPortAuthControl": rcdot1xPortAuthControl,
       "rcdot1xPortStatisticClear": rcdot1xPortStatisticClear,
       "rcdot1xPortAuthMethod": rcdot1xPortAuthMethod}
)
