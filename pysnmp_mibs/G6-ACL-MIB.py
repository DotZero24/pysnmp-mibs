# SNMP MIB module (G6-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:08 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Acl_ObjectIdentity = ObjectIdentity
acl = _Acl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51)
)


class _AclEnableAclFiltering_Type(Integer32):
    """Custom type aclEnableAclFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_AclEnableAclFiltering_Type.__name__ = "Integer32"
_AclEnableAclFiltering_Object = MibScalar
aclEnableAclFiltering = _AclEnableAclFiltering_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 1),
    _AclEnableAclFiltering_Type()
)
aclEnableAclFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclEnableAclFiltering.setStatus("current")
_ActiveFilterPortConfigTable_Object = MibTable
activeFilterPortConfigTable = _ActiveFilterPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 2)
)
if mibBuilder.loadTexts:
    activeFilterPortConfigTable.setStatus("current")
_ActiveFilterPortConfigEntry_Object = MibTableRow
activeFilterPortConfigEntry = _ActiveFilterPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 2, 1)
)
activeFilterPortConfigEntry.setIndexNames(
    (0, "G6-ACL-MIB", "activeFilterPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    activeFilterPortConfigEntry.setStatus("current")


class _ActiveFilterPortConfigPortIndex_Type(Integer32):
    """Custom type activeFilterPortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 31),
    )


_ActiveFilterPortConfigPortIndex_Type.__name__ = "Integer32"
_ActiveFilterPortConfigPortIndex_Object = MibTableColumn
activeFilterPortConfigPortIndex = _ActiveFilterPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 2, 1, 1),
    _ActiveFilterPortConfigPortIndex_Type()
)
activeFilterPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    activeFilterPortConfigPortIndex.setStatus("current")


class _ActiveFilterPortConfigEnableAclFiltering_Type(Integer32):
    """Custom type activeFilterPortConfigEnableAclFiltering based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ActiveFilterPortConfigEnableAclFiltering_Type.__name__ = "Integer32"
_ActiveFilterPortConfigEnableAclFiltering_Object = MibTableColumn
activeFilterPortConfigEnableAclFiltering = _ActiveFilterPortConfigEnableAclFiltering_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 2, 1, 2),
    _ActiveFilterPortConfigEnableAclFiltering_Type()
)
activeFilterPortConfigEnableAclFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeFilterPortConfigEnableAclFiltering.setStatus("current")
_ActiveFilterPortConfigAclListName_Type = DisplayString
_ActiveFilterPortConfigAclListName_Object = MibTableColumn
activeFilterPortConfigAclListName = _ActiveFilterPortConfigAclListName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 2, 1, 3),
    _ActiveFilterPortConfigAclListName_Type()
)
activeFilterPortConfigAclListName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    activeFilterPortConfigAclListName.setStatus("current")
_ListTable_Object = MibTable
listTable = _ListTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 3)
)
if mibBuilder.loadTexts:
    listTable.setStatus("current")
_ListEntry_Object = MibTableRow
listEntry = _ListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 3, 1)
)
listEntry.setIndexNames(
    (0, "G6-ACL-MIB", "listIndex"),
)
if mibBuilder.loadTexts:
    listEntry.setStatus("current")


class _ListIndex_Type(Integer32):
    """Custom type listIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ListIndex_Type.__name__ = "Integer32"
_ListIndex_Object = MibTableColumn
listIndex = _ListIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 3, 1, 1),
    _ListIndex_Type()
)
listIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    listIndex.setStatus("current")
_ListName_Type = DisplayString
_ListName_Object = MibTableColumn
listName = _ListName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 3, 1, 2),
    _ListName_Type()
)
listName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listName.setStatus("current")
_ListDescription_Type = DisplayString
_ListDescription_Object = MibTableColumn
listDescription = _ListDescription_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 3, 1, 3),
    _ListDescription_Type()
)
listDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listDescription.setStatus("current")
_ListRules_Type = DisplayString
_ListRules_Object = MibTableColumn
listRules = _ListRules_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 3, 1, 4),
    _ListRules_Type()
)
listRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    listRules.setStatus("current")
_RulesTable_Object = MibTable
rulesTable = _RulesTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4)
)
if mibBuilder.loadTexts:
    rulesTable.setStatus("current")
_RulesEntry_Object = MibTableRow
rulesEntry = _RulesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1)
)
rulesEntry.setIndexNames(
    (0, "G6-ACL-MIB", "rulesIndex"),
)
if mibBuilder.loadTexts:
    rulesEntry.setStatus("current")


class _RulesIndex_Type(Integer32):
    """Custom type rulesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 127),
    )


_RulesIndex_Type.__name__ = "Integer32"
_RulesIndex_Object = MibTableColumn
rulesIndex = _RulesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 1),
    _RulesIndex_Type()
)
rulesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rulesIndex.setStatus("current")
_RulesName_Type = DisplayString
_RulesName_Object = MibTableColumn
rulesName = _RulesName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 2),
    _RulesName_Type()
)
rulesName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesName.setStatus("current")
_RulesDescription_Type = DisplayString
_RulesDescription_Object = MibTableColumn
rulesDescription = _RulesDescription_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 3),
    _RulesDescription_Type()
)
rulesDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesDescription.setStatus("current")


class _RulesMode_Type(Integer32):
    """Custom type rulesMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unused", 0),
          ("permit", 1),
          ("deny", 2))
    )


_RulesMode_Type.__name__ = "Integer32"
_RulesMode_Object = MibTableColumn
rulesMode = _RulesMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 4),
    _RulesMode_Type()
)
rulesMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesMode.setStatus("current")


class _RulesEtherType_Type(Integer32):
    """Custom type rulesEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RulesEtherType_Type.__name__ = "Integer32"
_RulesEtherType_Object = MibTableColumn
rulesEtherType = _RulesEtherType_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 5),
    _RulesEtherType_Type()
)
rulesEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesEtherType.setStatus("current")


class _RulesProtocol_Type(Integer32):
    """Custom type rulesProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RulesProtocol_Type.__name__ = "Integer32"
_RulesProtocol_Object = MibTableColumn
rulesProtocol = _RulesProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 6),
    _RulesProtocol_Type()
)
rulesProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesProtocol.setStatus("current")


class _RulesVlanId_Type(Integer32):
    """Custom type rulesVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RulesVlanId_Type.__name__ = "Integer32"
_RulesVlanId_Object = MibTableColumn
rulesVlanId = _RulesVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 7),
    _RulesVlanId_Type()
)
rulesVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesVlanId.setStatus("current")
_RulesSourceMac_Type = MacAddress
_RulesSourceMac_Object = MibTableColumn
rulesSourceMac = _RulesSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 8),
    _RulesSourceMac_Type()
)
rulesSourceMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesSourceMac.setStatus("current")


class _RulesSourceIp_Type(OctetString):
    """Custom type rulesSourceIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RulesSourceIp_Type.__name__ = "OctetString"
_RulesSourceIp_Object = MibTableColumn
rulesSourceIp = _RulesSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 9),
    _RulesSourceIp_Type()
)
rulesSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesSourceIp.setStatus("current")


class _RulesSourceMask_Type(OctetString):
    """Custom type rulesSourceMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RulesSourceMask_Type.__name__ = "OctetString"
_RulesSourceMask_Object = MibTableColumn
rulesSourceMask = _RulesSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 10),
    _RulesSourceMask_Type()
)
rulesSourceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesSourceMask.setStatus("current")


class _RulesSourcePort_Type(Integer32):
    """Custom type rulesSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RulesSourcePort_Type.__name__ = "Integer32"
_RulesSourcePort_Object = MibTableColumn
rulesSourcePort = _RulesSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 11),
    _RulesSourcePort_Type()
)
rulesSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesSourcePort.setStatus("current")
_RulesDestinationMac_Type = MacAddress
_RulesDestinationMac_Object = MibTableColumn
rulesDestinationMac = _RulesDestinationMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 12),
    _RulesDestinationMac_Type()
)
rulesDestinationMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesDestinationMac.setStatus("current")


class _RulesDestinationIp_Type(OctetString):
    """Custom type rulesDestinationIp based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RulesDestinationIp_Type.__name__ = "OctetString"
_RulesDestinationIp_Object = MibTableColumn
rulesDestinationIp = _RulesDestinationIp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 13),
    _RulesDestinationIp_Type()
)
rulesDestinationIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesDestinationIp.setStatus("current")


class _RulesDestinationMask_Type(OctetString):
    """Custom type rulesDestinationMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_RulesDestinationMask_Type.__name__ = "OctetString"
_RulesDestinationMask_Object = MibTableColumn
rulesDestinationMask = _RulesDestinationMask_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 14),
    _RulesDestinationMask_Type()
)
rulesDestinationMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesDestinationMask.setStatus("current")


class _RulesDestinationPort_Type(Integer32):
    """Custom type rulesDestinationPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RulesDestinationPort_Type.__name__ = "Integer32"
_RulesDestinationPort_Object = MibTableColumn
rulesDestinationPort = _RulesDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 51, 4, 1, 15),
    _RulesDestinationPort_Type()
)
rulesDestinationPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rulesDestinationPort.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-ACL-MIB",
    **{"management": management,
       "acl": acl,
       "aclEnableAclFiltering": aclEnableAclFiltering,
       "activeFilterPortConfigTable": activeFilterPortConfigTable,
       "activeFilterPortConfigEntry": activeFilterPortConfigEntry,
       "activeFilterPortConfigPortIndex": activeFilterPortConfigPortIndex,
       "activeFilterPortConfigEnableAclFiltering": activeFilterPortConfigEnableAclFiltering,
       "activeFilterPortConfigAclListName": activeFilterPortConfigAclListName,
       "listTable": listTable,
       "listEntry": listEntry,
       "listIndex": listIndex,
       "listName": listName,
       "listDescription": listDescription,
       "listRules": listRules,
       "rulesTable": rulesTable,
       "rulesEntry": rulesEntry,
       "rulesIndex": rulesIndex,
       "rulesName": rulesName,
       "rulesDescription": rulesDescription,
       "rulesMode": rulesMode,
       "rulesEtherType": rulesEtherType,
       "rulesProtocol": rulesProtocol,
       "rulesVlanId": rulesVlanId,
       "rulesSourceMac": rulesSourceMac,
       "rulesSourceIp": rulesSourceIp,
       "rulesSourceMask": rulesSourceMask,
       "rulesSourcePort": rulesSourcePort,
       "rulesDestinationMac": rulesDestinationMac,
       "rulesDestinationIp": rulesDestinationIp,
       "rulesDestinationMask": rulesDestinationMask,
       "rulesDestinationPort": rulesDestinationPort}
)
