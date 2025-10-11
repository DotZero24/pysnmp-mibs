# SNMP MIB module (NG700-INVENTORY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netgear/NG700-INVENTORY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:28:01 2025
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

(ng700smartswitch,) = mibBuilder.importSymbols(
    "NG700-REF-MIB",
    "ng700smartswitch")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fastPathInventory = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13)
)
if mibBuilder.loadTexts:
    fastPathInventory.setRevisions(
        ("2011-01-26 00:00",
         "2007-05-23 00:00",
         "2004-10-28 20:37",
         "2003-05-26 19:30")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AgentInventoryUnitPreference(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("unsassigned", 1),
          ("assigned", 2))
    )



class AgentInventoryUnitType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


class AgentInventoryCardType(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "x"


# MIB Managed Objects in the order of their OIDs

_AgentInventoryStackGroup_ObjectIdentity = ObjectIdentity
agentInventoryStackGroup = _AgentInventoryStackGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 1)
)


class _AgentInventoryStackSTKname_Type(Integer32):
    """Custom type agentInventoryStackSTKname based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unconfigured", 1),
          ("image1", 2),
          ("image2", 3))
    )


_AgentInventoryStackSTKname_Type.__name__ = "Integer32"
_AgentInventoryStackSTKname_Object = MibScalar
agentInventoryStackSTKname = _AgentInventoryStackSTKname_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 1, 5),
    _AgentInventoryStackSTKname_Type()
)
agentInventoryStackSTKname.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackSTKname.setStatus("current")


class _AgentInventoryStackActivateSTK_Type(Integer32):
    """Custom type agentInventoryStackActivateSTK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryStackActivateSTK_Type.__name__ = "Integer32"
_AgentInventoryStackActivateSTK_Object = MibScalar
agentInventoryStackActivateSTK = _AgentInventoryStackActivateSTK_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 1, 6),
    _AgentInventoryStackActivateSTK_Type()
)
agentInventoryStackActivateSTK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackActivateSTK.setStatus("current")


class _AgentInventoryStackDeleteSTK_Type(Integer32):
    """Custom type agentInventoryStackDeleteSTK based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AgentInventoryStackDeleteSTK_Type.__name__ = "Integer32"
_AgentInventoryStackDeleteSTK_Object = MibScalar
agentInventoryStackDeleteSTK = _AgentInventoryStackDeleteSTK_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 1, 7),
    _AgentInventoryStackDeleteSTK_Type()
)
agentInventoryStackDeleteSTK.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentInventoryStackDeleteSTK.setStatus("current")
_AgentInventoryCardGroup_ObjectIdentity = ObjectIdentity
agentInventoryCardGroup = _AgentInventoryCardGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 4)
)
_AgentInventoryCardTypeTable_Object = MibTable
agentInventoryCardTypeTable = _AgentInventoryCardTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 4, 1)
)
if mibBuilder.loadTexts:
    agentInventoryCardTypeTable.setStatus("current")
_AgentInventoryCardTypeEntry_Object = MibTableRow
agentInventoryCardTypeEntry = _AgentInventoryCardTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 4, 1, 1)
)
agentInventoryCardTypeEntry.setIndexNames(
    (0, "NG700-INVENTORY-MIB", "agentInventoryCardIndex"),
)
if mibBuilder.loadTexts:
    agentInventoryCardTypeEntry.setStatus("current")
_AgentInventoryCardIndex_Type = Unsigned32
_AgentInventoryCardIndex_Object = MibTableColumn
agentInventoryCardIndex = _AgentInventoryCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 4, 1, 1, 1),
    _AgentInventoryCardIndex_Type()
)
agentInventoryCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentInventoryCardIndex.setStatus("current")
_AgentInventoryCardType_Type = AgentInventoryCardType
_AgentInventoryCardType_Object = MibTableColumn
agentInventoryCardType = _AgentInventoryCardType_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 4, 1, 1, 2),
    _AgentInventoryCardType_Type()
)
agentInventoryCardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryCardType.setStatus("current")
_AgentInventoryCardModelIdentifier_Type = DisplayString
_AgentInventoryCardModelIdentifier_Object = MibTableColumn
agentInventoryCardModelIdentifier = _AgentInventoryCardModelIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 4, 1, 1, 3),
    _AgentInventoryCardModelIdentifier_Type()
)
agentInventoryCardModelIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryCardModelIdentifier.setStatus("current")
_AgentInventoryCardDescription_Type = DisplayString
_AgentInventoryCardDescription_Object = MibTableColumn
agentInventoryCardDescription = _AgentInventoryCardDescription_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 4, 1, 1, 4),
    _AgentInventoryCardDescription_Type()
)
agentInventoryCardDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryCardDescription.setStatus("current")
_AgentInventoryComponentGroup_ObjectIdentity = ObjectIdentity
agentInventoryComponentGroup = _AgentInventoryComponentGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 5)
)
_AgentInventoryComponentTable_Object = MibTable
agentInventoryComponentTable = _AgentInventoryComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 5, 1)
)
if mibBuilder.loadTexts:
    agentInventoryComponentTable.setStatus("current")
_AgentInventoryComponentEntry_Object = MibTableRow
agentInventoryComponentEntry = _AgentInventoryComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 5, 1, 1)
)
agentInventoryComponentEntry.setIndexNames(
    (0, "NG700-INVENTORY-MIB", "agentInventoryComponentIndex"),
)
if mibBuilder.loadTexts:
    agentInventoryComponentEntry.setStatus("current")
_AgentInventoryComponentIndex_Type = Unsigned32
_AgentInventoryComponentIndex_Object = MibTableColumn
agentInventoryComponentIndex = _AgentInventoryComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 5, 1, 1, 1),
    _AgentInventoryComponentIndex_Type()
)
agentInventoryComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentInventoryComponentIndex.setStatus("current")
_AgentInventoryComponentMnemonic_Type = DisplayString
_AgentInventoryComponentMnemonic_Object = MibTableColumn
agentInventoryComponentMnemonic = _AgentInventoryComponentMnemonic_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 5, 1, 1, 2),
    _AgentInventoryComponentMnemonic_Type()
)
agentInventoryComponentMnemonic.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryComponentMnemonic.setStatus("current")
_AgentInventoryComponentName_Type = DisplayString
_AgentInventoryComponentName_Object = MibTableColumn
agentInventoryComponentName = _AgentInventoryComponentName_Object(
    (1, 3, 6, 1, 4, 1, 4526, 11, 13, 5, 1, 1, 3),
    _AgentInventoryComponentName_Type()
)
agentInventoryComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentInventoryComponentName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NG700-INVENTORY-MIB",
    **{"AgentInventoryUnitPreference": AgentInventoryUnitPreference,
       "AgentInventoryUnitType": AgentInventoryUnitType,
       "AgentInventoryCardType": AgentInventoryCardType,
       "fastPathInventory": fastPathInventory,
       "agentInventoryStackGroup": agentInventoryStackGroup,
       "agentInventoryStackSTKname": agentInventoryStackSTKname,
       "agentInventoryStackActivateSTK": agentInventoryStackActivateSTK,
       "agentInventoryStackDeleteSTK": agentInventoryStackDeleteSTK,
       "agentInventoryCardGroup": agentInventoryCardGroup,
       "agentInventoryCardTypeTable": agentInventoryCardTypeTable,
       "agentInventoryCardTypeEntry": agentInventoryCardTypeEntry,
       "agentInventoryCardIndex": agentInventoryCardIndex,
       "agentInventoryCardType": agentInventoryCardType,
       "agentInventoryCardModelIdentifier": agentInventoryCardModelIdentifier,
       "agentInventoryCardDescription": agentInventoryCardDescription,
       "agentInventoryComponentGroup": agentInventoryComponentGroup,
       "agentInventoryComponentTable": agentInventoryComponentTable,
       "agentInventoryComponentEntry": agentInventoryComponentEntry,
       "agentInventoryComponentIndex": agentInventoryComponentIndex,
       "agentInventoryComponentMnemonic": agentInventoryComponentMnemonic,
       "agentInventoryComponentName": agentInventoryComponentName}
)
