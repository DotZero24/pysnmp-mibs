# SNMP MIB module (PDN-ETHER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-ETHER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:00:28 2025
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

(ifJackIndex,
 ifMauEntry,
 ifMauIfIndex,
 ifMauIndex) = mibBuilder.importSymbols(
    "MAU-MIB",
    "ifJackIndex",
    "ifMauEntry",
    "ifMauIfIndex",
    "ifMauIndex")

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(ManagementType,
 ResetStates,
 SwitchState) = mibBuilder.importSymbols(
    "PDN-TC",
    "ManagementType",
    "ResetStates",
    "SwitchState")

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

pdn_ether = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18)
)
if mibBuilder.loadTexts:
    pdn_ether.setRevisions(
        ("1902-05-10 00:00",
         "1902-01-09 00:00",
         "2001-08-24 00:00",
         "2000-05-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnPortConfigMIBObjects_ObjectIdentity = ObjectIdentity
pdnPortConfigMIBObjects = _PdnPortConfigMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1)
)
_PdnPortConfigEthernet_ObjectIdentity = ObjectIdentity
pdnPortConfigEthernet = _PdnPortConfigEthernet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1)
)
_PdnPortConfigEthernetTable_Object = MibTable
pdnPortConfigEthernetTable = _PdnPortConfigEthernetTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1)
)
if mibBuilder.loadTexts:
    pdnPortConfigEthernetTable.setStatus("current")
_PdnPortConfigEthernetEntry_Object = MibTableRow
pdnPortConfigEthernetEntry = _PdnPortConfigEthernetEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1, 1)
)
pdnPortConfigEthernetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    pdnPortConfigEthernetEntry.setStatus("current")


class _PdnPortConfigEthernetDuplexMode_Type(SwitchState):
    """Custom type pdnPortConfigEthernetDuplexMode based on SwitchState"""
    defaultValue = 2


_PdnPortConfigEthernetDuplexMode_Type.__name__ = "SwitchState"
_PdnPortConfigEthernetDuplexMode_Object = MibTableColumn
pdnPortConfigEthernetDuplexMode = _PdnPortConfigEthernetDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1, 1, 1),
    _PdnPortConfigEthernetDuplexMode_Type()
)
pdnPortConfigEthernetDuplexMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPortConfigEthernetDuplexMode.setStatus("current")


class _PdnPortConfigEthernetManageType_Type(ManagementType):
    """Custom type pdnPortConfigEthernetManageType based on ManagementType"""
    defaultValue = 2


_PdnPortConfigEthernetManageType_Type.__name__ = "ManagementType"
_PdnPortConfigEthernetManageType_Object = MibTableColumn
pdnPortConfigEthernetManageType = _PdnPortConfigEthernetManageType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1, 1, 2),
    _PdnPortConfigEthernetManageType_Type()
)
pdnPortConfigEthernetManageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPortConfigEthernetManageType.setStatus("current")


class _PdnPortConfigEthernetResetState_Type(ResetStates):
    """Custom type pdnPortConfigEthernetResetState based on ResetStates"""
    defaultValue = 1


_PdnPortConfigEthernetResetState_Type.__name__ = "ResetStates"
_PdnPortConfigEthernetResetState_Object = MibTableColumn
pdnPortConfigEthernetResetState = _PdnPortConfigEthernetResetState_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1, 1, 3),
    _PdnPortConfigEthernetResetState_Type()
)
pdnPortConfigEthernetResetState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPortConfigEthernetResetState.setStatus("current")


class _PdnPortConfigEthernetAutoNegotiate_Type(SwitchState):
    """Custom type pdnPortConfigEthernetAutoNegotiate based on SwitchState"""
    defaultValue = 1


_PdnPortConfigEthernetAutoNegotiate_Type.__name__ = "SwitchState"
_PdnPortConfigEthernetAutoNegotiate_Object = MibTableColumn
pdnPortConfigEthernetAutoNegotiate = _PdnPortConfigEthernetAutoNegotiate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1, 1, 4),
    _PdnPortConfigEthernetAutoNegotiate_Type()
)
pdnPortConfigEthernetAutoNegotiate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPortConfigEthernetAutoNegotiate.setStatus("current")


class _PdnPortConfigEthernetSpeed_Type(Integer32):
    """Custom type pdnPortConfigEthernetSpeed based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tenBaseT", 1),
          ("hundredBaseT", 2))
    )


_PdnPortConfigEthernetSpeed_Type.__name__ = "Integer32"
_PdnPortConfigEthernetSpeed_Object = MibTableColumn
pdnPortConfigEthernetSpeed = _PdnPortConfigEthernetSpeed_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 1, 1, 1, 5),
    _PdnPortConfigEthernetSpeed_Type()
)
pdnPortConfigEthernetSpeed.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPortConfigEthernetSpeed.setStatus("current")
_PdnPortConfigGroups_ObjectIdentity = ObjectIdentity
pdnPortConfigGroups = _PdnPortConfigGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 2)
)
_PdnPortConfigMauExtMIBObject_ObjectIdentity = ObjectIdentity
pdnPortConfigMauExtMIBObject = _PdnPortConfigMauExtMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 3)
)
_PdnPortConfigMauExtTable_Object = MibTable
pdnPortConfigMauExtTable = _PdnPortConfigMauExtTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 3, 1)
)
if mibBuilder.loadTexts:
    pdnPortConfigMauExtTable.setStatus("current")
_PdnPortConfigMauExtEntry_Object = MibTableRow
pdnPortConfigMauExtEntry = _PdnPortConfigMauExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    pdnPortConfigMauExtEntry.setStatus("current")


class _PdnPortConfigXover_Type(Integer32):
    """Custom type pdnPortConfigXover based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2))
    )


_PdnPortConfigXover_Type.__name__ = "Integer32"
_PdnPortConfigXover_Object = MibTableColumn
pdnPortConfigXover = _PdnPortConfigXover_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 3, 1, 1, 1),
    _PdnPortConfigXover_Type()
)
pdnPortConfigXover.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnPortConfigXover.setStatus("current")
_PdnPortConfigIfJackMIBObject_ObjectIdentity = ObjectIdentity
pdnPortConfigIfJackMIBObject = _PdnPortConfigIfJackMIBObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 4)
)
_PdnIfJackTable_Object = MibTable
pdnIfJackTable = _PdnIfJackTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 4, 1)
)
if mibBuilder.loadTexts:
    pdnIfJackTable.setStatus("current")
_PdnIfJackEntry_Object = MibTableRow
pdnIfJackEntry = _PdnIfJackEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 4, 1, 1)
)
pdnIfJackEntry.setIndexNames(
    (0, "MAU-MIB", "ifMauIfIndex"),
    (0, "MAU-MIB", "ifMauIndex"),
    (0, "MAU-MIB", "ifJackIndex"),
)
if mibBuilder.loadTexts:
    pdnIfJackEntry.setStatus("current")


class _PdnActiveJack_Type(Integer32):
    """Custom type pdnActiveJack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fiber", 1),
          ("rj45", 2),
          ("auto", 3))
    )


_PdnActiveJack_Type.__name__ = "Integer32"
_PdnActiveJack_Object = MibTableColumn
pdnActiveJack = _PdnActiveJack_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 4, 1, 1, 1),
    _PdnActiveJack_Type()
)
pdnActiveJack.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnActiveJack.setStatus("current")
_PdnPortConfigMIBTraps_ObjectIdentity = ObjectIdentity
pdnPortConfigMIBTraps = _PdnPortConfigMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 2)
)
ifMauEntry.registerAugmentions(
    ("PDN-ETHER-MIB",
     "pdnPortConfigMauExtEntry")
)
pdnPortConfigMauExtEntry.setIndexNames(*ifMauEntry.getIndexNames())

# Managed Objects groups

pdnPortConfigEthernetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 2, 1)
)
pdnPortConfigEthernetGroup.setObjects(
      *(("PDN-ETHER-MIB", "pdnPortConfigEthernetDuplexMode"),
        ("PDN-ETHER-MIB", "pdnPortConfigEthernetManageType"),
        ("PDN-ETHER-MIB", "pdnPortConfigEthernetResetState"),
        ("PDN-ETHER-MIB", "pdnPortConfigEthernetAutoNegotiate"),
        ("PDN-ETHER-MIB", "pdnPortConfigEthernetSpeed"))
)
if mibBuilder.loadTexts:
    pdnPortConfigEthernetGroup.setStatus("current")

pdnPortConfigExtMauGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 2, 2)
)
pdnPortConfigExtMauGroup.setObjects(
    ("PDN-ETHER-MIB", "pdnPortConfigXover")
)
if mibBuilder.loadTexts:
    pdnPortConfigExtMauGroup.setStatus("current")

pdnPortConfigExtIfJackGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 18, 1, 2, 3)
)
pdnPortConfigExtIfJackGroup.setObjects(
    ("PDN-ETHER-MIB", "pdnActiveJack")
)
if mibBuilder.loadTexts:
    pdnPortConfigExtIfJackGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-ETHER-MIB",
    **{"pdn-ether": pdn_ether,
       "pdnPortConfigMIBObjects": pdnPortConfigMIBObjects,
       "pdnPortConfigEthernet": pdnPortConfigEthernet,
       "pdnPortConfigEthernetTable": pdnPortConfigEthernetTable,
       "pdnPortConfigEthernetEntry": pdnPortConfigEthernetEntry,
       "pdnPortConfigEthernetDuplexMode": pdnPortConfigEthernetDuplexMode,
       "pdnPortConfigEthernetManageType": pdnPortConfigEthernetManageType,
       "pdnPortConfigEthernetResetState": pdnPortConfigEthernetResetState,
       "pdnPortConfigEthernetAutoNegotiate": pdnPortConfigEthernetAutoNegotiate,
       "pdnPortConfigEthernetSpeed": pdnPortConfigEthernetSpeed,
       "pdnPortConfigGroups": pdnPortConfigGroups,
       "pdnPortConfigEthernetGroup": pdnPortConfigEthernetGroup,
       "pdnPortConfigExtMauGroup": pdnPortConfigExtMauGroup,
       "pdnPortConfigExtIfJackGroup": pdnPortConfigExtIfJackGroup,
       "pdnPortConfigMauExtMIBObject": pdnPortConfigMauExtMIBObject,
       "pdnPortConfigMauExtTable": pdnPortConfigMauExtTable,
       "pdnPortConfigMauExtEntry": pdnPortConfigMauExtEntry,
       "pdnPortConfigXover": pdnPortConfigXover,
       "pdnPortConfigIfJackMIBObject": pdnPortConfigIfJackMIBObject,
       "pdnIfJackTable": pdnIfJackTable,
       "pdnIfJackEntry": pdnIfJackEntry,
       "pdnActiveJack": pdnActiveJack,
       "pdnPortConfigMIBTraps": pdnPortConfigMIBTraps}
)
