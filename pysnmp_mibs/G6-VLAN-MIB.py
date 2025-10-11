# SNMP MIB module (G6-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:06 2025
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

protocol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2)
)
if mibBuilder.loadTexts:
    protocol.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Vlan_ObjectIdentity = ObjectIdentity
vlan = _Vlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82)
)


class _VlanEnableVlanFiltering_Type(Integer32):
    """Custom type vlanEnableVlanFiltering based on Integer32"""
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


_VlanEnableVlanFiltering_Type.__name__ = "Integer32"
_VlanEnableVlanFiltering_Object = MibScalar
vlanEnableVlanFiltering = _VlanEnableVlanFiltering_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 1),
    _VlanEnableVlanFiltering_Type()
)
vlanEnableVlanFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanEnableVlanFiltering.setStatus("current")
_VlanIdConfigTable_Object = MibTable
vlanIdConfigTable = _VlanIdConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 2)
)
if mibBuilder.loadTexts:
    vlanIdConfigTable.setStatus("current")
_VlanIdConfigEntry_Object = MibTableRow
vlanIdConfigEntry = _VlanIdConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 2, 1)
)
vlanIdConfigEntry.setIndexNames(
    (0, "G6-VLAN-MIB", "vlanIdConfigIndex"),
)
if mibBuilder.loadTexts:
    vlanIdConfigEntry.setStatus("current")


class _VlanIdConfigIndex_Type(Integer32):
    """Custom type vlanIdConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_VlanIdConfigIndex_Type.__name__ = "Integer32"
_VlanIdConfigIndex_Object = MibTableColumn
vlanIdConfigIndex = _VlanIdConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 2, 1, 1),
    _VlanIdConfigIndex_Type()
)
vlanIdConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanIdConfigIndex.setStatus("current")


class _VlanIdConfigManagementVlanId_Type(Integer32):
    """Custom type vlanIdConfigManagementVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanIdConfigManagementVlanId_Type.__name__ = "Integer32"
_VlanIdConfigManagementVlanId_Object = MibTableColumn
vlanIdConfigManagementVlanId = _VlanIdConfigManagementVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 2, 1, 2),
    _VlanIdConfigManagementVlanId_Type()
)
vlanIdConfigManagementVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIdConfigManagementVlanId.setStatus("current")


class _VlanIdConfigManagementPriority_Type(Integer32):
    """Custom type vlanIdConfigManagementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_VlanIdConfigManagementPriority_Type.__name__ = "Integer32"
_VlanIdConfigManagementPriority_Object = MibTableColumn
vlanIdConfigManagementPriority = _VlanIdConfigManagementPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 2, 1, 3),
    _VlanIdConfigManagementPriority_Type()
)
vlanIdConfigManagementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIdConfigManagementPriority.setStatus("current")


class _VlanIdConfigVoiceVlanId_Type(Integer32):
    """Custom type vlanIdConfigVoiceVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanIdConfigVoiceVlanId_Type.__name__ = "Integer32"
_VlanIdConfigVoiceVlanId_Object = MibTableColumn
vlanIdConfigVoiceVlanId = _VlanIdConfigVoiceVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 2, 1, 4),
    _VlanIdConfigVoiceVlanId_Type()
)
vlanIdConfigVoiceVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIdConfigVoiceVlanId.setStatus("current")


class _VlanIdConfigRstpVlanId_Type(Integer32):
    """Custom type vlanIdConfigRstpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanIdConfigRstpVlanId_Type.__name__ = "Integer32"
_VlanIdConfigRstpVlanId_Object = MibTableColumn
vlanIdConfigRstpVlanId = _VlanIdConfigRstpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 2, 1, 5),
    _VlanIdConfigRstpVlanId_Type()
)
vlanIdConfigRstpVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIdConfigRstpVlanId.setStatus("current")


class _VlanIdConfigUnauthorizedVlanId_Type(Integer32):
    """Custom type vlanIdConfigUnauthorizedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanIdConfigUnauthorizedVlanId_Type.__name__ = "Integer32"
_VlanIdConfigUnauthorizedVlanId_Object = MibTableColumn
vlanIdConfigUnauthorizedVlanId = _VlanIdConfigUnauthorizedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 2, 1, 6),
    _VlanIdConfigUnauthorizedVlanId_Type()
)
vlanIdConfigUnauthorizedVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIdConfigUnauthorizedVlanId.setStatus("current")


class _VlanIdConfigSmartofficeVlanId_Type(Integer32):
    """Custom type vlanIdConfigSmartofficeVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanIdConfigSmartofficeVlanId_Type.__name__ = "Integer32"
_VlanIdConfigSmartofficeVlanId_Object = MibTableColumn
vlanIdConfigSmartofficeVlanId = _VlanIdConfigSmartofficeVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 2, 1, 7),
    _VlanIdConfigSmartofficeVlanId_Type()
)
vlanIdConfigSmartofficeVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanIdConfigSmartofficeVlanId.setStatus("current")
_PortConfigTable_Object = MibTable
portConfigTable = _PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3)
)
if mibBuilder.loadTexts:
    portConfigTable.setStatus("current")
_PortConfigEntry_Object = MibTableRow
portConfigEntry = _PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3, 1)
)
portConfigEntry.setIndexNames(
    (0, "G6-VLAN-MIB", "portConfigPortIndex"),
)
if mibBuilder.loadTexts:
    portConfigEntry.setStatus("current")


class _PortConfigPortIndex_Type(Integer32):
    """Custom type portConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PortConfigPortIndex_Type.__name__ = "Integer32"
_PortConfigPortIndex_Object = MibTableColumn
portConfigPortIndex = _PortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3, 1, 1),
    _PortConfigPortIndex_Type()
)
portConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portConfigPortIndex.setStatus("current")


class _PortConfigVlanMode_Type(Integer32):
    """Custom type portConfigVlanMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("access", 0),
          ("hybrid", 1),
          ("trunk", 2),
          ("qInQCustomer", 3),
          ("qInQProvider", 4))
    )


_PortConfigVlanMode_Type.__name__ = "Integer32"
_PortConfigVlanMode_Object = MibTableColumn
portConfigVlanMode = _PortConfigVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3, 1, 2),
    _PortConfigVlanMode_Type()
)
portConfigVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigVlanMode.setStatus("current")


class _PortConfigDefaultVlanId_Type(Integer32):
    """Custom type portConfigDefaultVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortConfigDefaultVlanId_Type.__name__ = "Integer32"
_PortConfigDefaultVlanId_Object = MibTableColumn
portConfigDefaultVlanId = _PortConfigDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3, 1, 3),
    _PortConfigDefaultVlanId_Type()
)
portConfigDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDefaultVlanId.setStatus("current")


class _PortConfigForceDefaultVlanId_Type(Integer32):
    """Custom type portConfigForceDefaultVlanId based on Integer32"""
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


_PortConfigForceDefaultVlanId_Type.__name__ = "Integer32"
_PortConfigForceDefaultVlanId_Object = MibTableColumn
portConfigForceDefaultVlanId = _PortConfigForceDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3, 1, 4),
    _PortConfigForceDefaultVlanId_Type()
)
portConfigForceDefaultVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigForceDefaultVlanId.setStatus("current")


class _PortConfigDefaultPriority_Type(Integer32):
    """Custom type portConfigDefaultPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_PortConfigDefaultPriority_Type.__name__ = "Integer32"
_PortConfigDefaultPriority_Object = MibTableColumn
portConfigDefaultPriority = _PortConfigDefaultPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3, 1, 5),
    _PortConfigDefaultPriority_Type()
)
portConfigDefaultPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigDefaultPriority.setStatus("current")


class _PortConfigPriorityOverride_Type(Integer32):
    """Custom type portConfigPriorityOverride based on Integer32"""
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


_PortConfigPriorityOverride_Type.__name__ = "Integer32"
_PortConfigPriorityOverride_Object = MibTableColumn
portConfigPriorityOverride = _PortConfigPriorityOverride_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3, 1, 6),
    _PortConfigPriorityOverride_Type()
)
portConfigPriorityOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigPriorityOverride.setStatus("current")


class _PortConfigUnauthorizedVlanId_Type(Integer32):
    """Custom type portConfigUnauthorizedVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortConfigUnauthorizedVlanId_Type.__name__ = "Integer32"
_PortConfigUnauthorizedVlanId_Object = MibTableColumn
portConfigUnauthorizedVlanId = _PortConfigUnauthorizedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3, 1, 7),
    _PortConfigUnauthorizedVlanId_Type()
)
portConfigUnauthorizedVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigUnauthorizedVlanId.setStatus("current")


class _PortConfigFallbackVlanId_Type(Integer32):
    """Custom type portConfigFallbackVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortConfigFallbackVlanId_Type.__name__ = "Integer32"
_PortConfigFallbackVlanId_Object = MibTableColumn
portConfigFallbackVlanId = _PortConfigFallbackVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3, 1, 8),
    _PortConfigFallbackVlanId_Type()
)
portConfigFallbackVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigFallbackVlanId.setStatus("current")


class _PortConfigQInQEthertype_Type(Integer32):
    """Custom type portConfigQInQEthertype based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ox88a8", 0),
          ("ox9100", 1),
          ("ox9200", 2),
          ("ox8100", 3))
    )


_PortConfigQInQEthertype_Type.__name__ = "Integer32"
_PortConfigQInQEthertype_Object = MibTableColumn
portConfigQInQEthertype = _PortConfigQInQEthertype_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 3, 1, 9),
    _PortConfigQInQEthertype_Type()
)
portConfigQInQEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portConfigQInQEthertype.setStatus("current")
_FilterConfigTable_Object = MibTable
filterConfigTable = _FilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4)
)
if mibBuilder.loadTexts:
    filterConfigTable.setStatus("current")
_FilterConfigEntry_Object = MibTableRow
filterConfigEntry = _FilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1)
)
filterConfigEntry.setIndexNames(
    (0, "G6-VLAN-MIB", "filterConfigIndex"),
)
if mibBuilder.loadTexts:
    filterConfigEntry.setStatus("current")


class _FilterConfigIndex_Type(Integer32):
    """Custom type filterConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FilterConfigIndex_Type.__name__ = "Integer32"
_FilterConfigIndex_Object = MibTableColumn
filterConfigIndex = _FilterConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1, 1),
    _FilterConfigIndex_Type()
)
filterConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    filterConfigIndex.setStatus("current")
_FilterConfigVlanId_Type = DisplayString
_FilterConfigVlanId_Object = MibTableColumn
filterConfigVlanId = _FilterConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1, 2),
    _FilterConfigVlanId_Type()
)
filterConfigVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterConfigVlanId.setStatus("current")


class _FilterConfigEntryMode_Type(Integer32):
    """Custom type filterConfigEntryMode based on Integer32"""
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


_FilterConfigEntryMode_Type.__name__ = "Integer32"
_FilterConfigEntryMode_Object = MibTableColumn
filterConfigEntryMode = _FilterConfigEntryMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1, 3),
    _FilterConfigEntryMode_Type()
)
filterConfigEntryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterConfigEntryMode.setStatus("current")
_FilterConfigAlias_Type = DisplayString
_FilterConfigAlias_Object = MibTableColumn
filterConfigAlias = _FilterConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1, 4),
    _FilterConfigAlias_Type()
)
filterConfigAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterConfigAlias.setStatus("current")


class _FilterConfigMstpGroup_Type(Integer32):
    """Custom type filterConfigMstpGroup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FilterConfigMstpGroup_Type.__name__ = "Integer32"
_FilterConfigMstpGroup_Object = MibTableColumn
filterConfigMstpGroup = _FilterConfigMstpGroup_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1, 5),
    _FilterConfigMstpGroup_Type()
)
filterConfigMstpGroup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterConfigMstpGroup.setStatus("current")
_FilterConfigFabricAttachISid_Type = Unsigned32
_FilterConfigFabricAttachISid_Object = MibTableColumn
filterConfigFabricAttachISid = _FilterConfigFabricAttachISid_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1, 6),
    _FilterConfigFabricAttachISid_Type()
)
filterConfigFabricAttachISid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterConfigFabricAttachISid.setStatus("current")
_FilterConfigPortMembers_Type = Integer32
_FilterConfigPortMembers_Object = MibTableColumn
filterConfigPortMembers = _FilterConfigPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1, 7),
    _FilterConfigPortMembers_Type()
)
filterConfigPortMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterConfigPortMembers.setStatus("current")


class _FilterConfigManagementMembers_Type(Integer32):
    """Custom type filterConfigManagementMembers based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("cpu1", 1),
          ("cpu2", 2),
          ("all", 3))
    )


_FilterConfigManagementMembers_Type.__name__ = "Integer32"
_FilterConfigManagementMembers_Object = MibTableColumn
filterConfigManagementMembers = _FilterConfigManagementMembers_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1, 8),
    _FilterConfigManagementMembers_Type()
)
filterConfigManagementMembers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterConfigManagementMembers.setStatus("current")


class _FilterConfigPriorityOverride_Type(Integer32):
    """Custom type filterConfigPriorityOverride based on Integer32"""
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


_FilterConfigPriorityOverride_Type.__name__ = "Integer32"
_FilterConfigPriorityOverride_Object = MibTableColumn
filterConfigPriorityOverride = _FilterConfigPriorityOverride_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1, 9),
    _FilterConfigPriorityOverride_Type()
)
filterConfigPriorityOverride.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterConfigPriorityOverride.setStatus("current")


class _FilterConfigNewPriority_Type(Integer32):
    """Custom type filterConfigNewPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("priority0", 0),
          ("priority1", 1),
          ("priority2", 2),
          ("priority3", 3),
          ("priority4", 4),
          ("priority5", 5),
          ("priority6", 6),
          ("priority7", 7))
    )


_FilterConfigNewPriority_Type.__name__ = "Integer32"
_FilterConfigNewPriority_Object = MibTableColumn
filterConfigNewPriority = _FilterConfigNewPriority_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 4, 1, 10),
    _FilterConfigNewPriority_Type()
)
filterConfigNewPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    filterConfigNewPriority.setStatus("current")


class _VlanEnableMvrp_Type(Integer32):
    """Custom type vlanEnableMvrp based on Integer32"""
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


_VlanEnableMvrp_Type.__name__ = "Integer32"
_VlanEnableMvrp_Object = MibScalar
vlanEnableMvrp = _VlanEnableMvrp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 5),
    _VlanEnableMvrp_Type()
)
vlanEnableMvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanEnableMvrp.setStatus("current")
_MvrpPortConfigTable_Object = MibTable
mvrpPortConfigTable = _MvrpPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 6)
)
if mibBuilder.loadTexts:
    mvrpPortConfigTable.setStatus("current")
_MvrpPortConfigEntry_Object = MibTableRow
mvrpPortConfigEntry = _MvrpPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 6, 1)
)
mvrpPortConfigEntry.setIndexNames(
    (0, "G6-VLAN-MIB", "mvrpPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    mvrpPortConfigEntry.setStatus("current")


class _MvrpPortConfigPortIndex_Type(Integer32):
    """Custom type mvrpPortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_MvrpPortConfigPortIndex_Type.__name__ = "Integer32"
_MvrpPortConfigPortIndex_Object = MibTableColumn
mvrpPortConfigPortIndex = _MvrpPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 6, 1, 1),
    _MvrpPortConfigPortIndex_Type()
)
mvrpPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrpPortConfigPortIndex.setStatus("current")


class _MvrpPortConfigEnableMvrp_Type(Integer32):
    """Custom type mvrpPortConfigEnableMvrp based on Integer32"""
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


_MvrpPortConfigEnableMvrp_Type.__name__ = "Integer32"
_MvrpPortConfigEnableMvrp_Object = MibTableColumn
mvrpPortConfigEnableMvrp = _MvrpPortConfigEnableMvrp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 6, 1, 2),
    _MvrpPortConfigEnableMvrp_Type()
)
mvrpPortConfigEnableMvrp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrpPortConfigEnableMvrp.setStatus("current")


class _MvrpPortConfigRegistrationMode_Type(Integer32):
    """Custom type mvrpPortConfigRegistrationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("fixed", 1),
          ("forbidden", 2))
    )


_MvrpPortConfigRegistrationMode_Type.__name__ = "Integer32"
_MvrpPortConfigRegistrationMode_Object = MibTableColumn
mvrpPortConfigRegistrationMode = _MvrpPortConfigRegistrationMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 6, 1, 3),
    _MvrpPortConfigRegistrationMode_Type()
)
mvrpPortConfigRegistrationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrpPortConfigRegistrationMode.setStatus("current")
_MvrpPortConfigJoinTimer_Type = Unsigned32
_MvrpPortConfigJoinTimer_Object = MibTableColumn
mvrpPortConfigJoinTimer = _MvrpPortConfigJoinTimer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 6, 1, 4),
    _MvrpPortConfigJoinTimer_Type()
)
mvrpPortConfigJoinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrpPortConfigJoinTimer.setStatus("current")
_MvrpPortConfigLeaveTimer_Type = Unsigned32
_MvrpPortConfigLeaveTimer_Object = MibTableColumn
mvrpPortConfigLeaveTimer = _MvrpPortConfigLeaveTimer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 6, 1, 5),
    _MvrpPortConfigLeaveTimer_Type()
)
mvrpPortConfigLeaveTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrpPortConfigLeaveTimer.setStatus("current")
_MvrpPortConfigLeaveallTimer_Type = Unsigned32
_MvrpPortConfigLeaveallTimer_Object = MibTableColumn
mvrpPortConfigLeaveallTimer = _MvrpPortConfigLeaveallTimer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 6, 1, 6),
    _MvrpPortConfigLeaveallTimer_Type()
)
mvrpPortConfigLeaveallTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrpPortConfigLeaveallTimer.setStatus("current")
_FabricAttachPortConfigTable_Object = MibTable
fabricAttachPortConfigTable = _FabricAttachPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 7)
)
if mibBuilder.loadTexts:
    fabricAttachPortConfigTable.setStatus("current")
_FabricAttachPortConfigEntry_Object = MibTableRow
fabricAttachPortConfigEntry = _FabricAttachPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 7, 1)
)
fabricAttachPortConfigEntry.setIndexNames(
    (0, "G6-VLAN-MIB", "fabricAttachPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    fabricAttachPortConfigEntry.setStatus("current")


class _FabricAttachPortConfigPortIndex_Type(Integer32):
    """Custom type fabricAttachPortConfigPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_FabricAttachPortConfigPortIndex_Type.__name__ = "Integer32"
_FabricAttachPortConfigPortIndex_Object = MibTableColumn
fabricAttachPortConfigPortIndex = _FabricAttachPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 7, 1, 1),
    _FabricAttachPortConfigPortIndex_Type()
)
fabricAttachPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fabricAttachPortConfigPortIndex.setStatus("current")


class _FabricAttachPortConfigEnableFabricAttach_Type(Integer32):
    """Custom type fabricAttachPortConfigEnableFabricAttach based on Integer32"""
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


_FabricAttachPortConfigEnableFabricAttach_Type.__name__ = "Integer32"
_FabricAttachPortConfigEnableFabricAttach_Object = MibTableColumn
fabricAttachPortConfigEnableFabricAttach = _FabricAttachPortConfigEnableFabricAttach_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 7, 1, 2),
    _FabricAttachPortConfigEnableFabricAttach_Type()
)
fabricAttachPortConfigEnableFabricAttach.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fabricAttachPortConfigEnableFabricAttach.setStatus("current")


class _FabricAttachPortConfigMsgAuthentication_Type(Integer32):
    """Custom type fabricAttachPortConfigMsgAuthentication based on Integer32"""
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


_FabricAttachPortConfigMsgAuthentication_Type.__name__ = "Integer32"
_FabricAttachPortConfigMsgAuthentication_Object = MibTableColumn
fabricAttachPortConfigMsgAuthentication = _FabricAttachPortConfigMsgAuthentication_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 7, 1, 3),
    _FabricAttachPortConfigMsgAuthentication_Type()
)
fabricAttachPortConfigMsgAuthentication.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fabricAttachPortConfigMsgAuthentication.setStatus("current")
_FabricAttachPortConfigEnterFaAuthKey_Type = DisplayString
_FabricAttachPortConfigEnterFaAuthKey_Object = MibTableColumn
fabricAttachPortConfigEnterFaAuthKey = _FabricAttachPortConfigEnterFaAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 7, 1, 4),
    _FabricAttachPortConfigEnterFaAuthKey_Type()
)
fabricAttachPortConfigEnterFaAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fabricAttachPortConfigEnterFaAuthKey.setStatus("current")
_FabricAttachPortConfigEncryptedFaAuthKey_Type = DisplayString
_FabricAttachPortConfigEncryptedFaAuthKey_Object = MibTableColumn
fabricAttachPortConfigEncryptedFaAuthKey = _FabricAttachPortConfigEncryptedFaAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 7, 1, 5),
    _FabricAttachPortConfigEncryptedFaAuthKey_Type()
)
fabricAttachPortConfigEncryptedFaAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fabricAttachPortConfigEncryptedFaAuthKey.setStatus("current")


class _VlanNumberOfEntries_Type(Integer32):
    """Custom type vlanNumberOfEntries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_VlanNumberOfEntries_Type.__name__ = "Integer32"
_VlanNumberOfEntries_Object = MibScalar
vlanNumberOfEntries = _VlanNumberOfEntries_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 100),
    _VlanNumberOfEntries_Type()
)
vlanNumberOfEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanNumberOfEntries.setStatus("current")
_StatusTable_Object = MibTable
statusTable = _StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101)
)
if mibBuilder.loadTexts:
    statusTable.setStatus("current")
_StatusEntry_Object = MibTableRow
statusEntry = _StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1)
)
statusEntry.setIndexNames(
    (0, "G6-VLAN-MIB", "statusVlanIndex"),
)
if mibBuilder.loadTexts:
    statusEntry.setStatus("current")


class _StatusVlanIndex_Type(Integer32):
    """Custom type statusVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StatusVlanIndex_Type.__name__ = "Integer32"
_StatusVlanIndex_Object = MibTableColumn
statusVlanIndex = _StatusVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 1),
    _StatusVlanIndex_Type()
)
statusVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statusVlanIndex.setStatus("current")


class _StatusVlanId_Type(Integer32):
    """Custom type statusVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StatusVlanId_Type.__name__ = "Integer32"
_StatusVlanId_Object = MibTableColumn
statusVlanId = _StatusVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 2),
    _StatusVlanId_Type()
)
statusVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusVlanId.setStatus("current")
_StatusTimeMark_Type = Unsigned32
_StatusTimeMark_Object = MibTableColumn
statusTimeMark = _StatusTimeMark_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 3),
    _StatusTimeMark_Type()
)
statusTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusTimeMark.setStatus("current")
_StatusAlias_Type = DisplayString
_StatusAlias_Object = MibTableColumn
statusAlias = _StatusAlias_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 4),
    _StatusAlias_Type()
)
statusAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusAlias.setStatus("current")
_StatusPortMembers_Type = Integer32
_StatusPortMembers_Object = MibTableColumn
statusPortMembers = _StatusPortMembers_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 5),
    _StatusPortMembers_Type()
)
statusPortMembers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusPortMembers.setStatus("current")
_StatusFilterDatabase_Type = Unsigned32
_StatusFilterDatabase_Object = MibTableColumn
statusFilterDatabase = _StatusFilterDatabase_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 6),
    _StatusFilterDatabase_Type()
)
statusFilterDatabase.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFilterDatabase.setStatus("current")
_StatusEgressPorts_Type = Integer32
_StatusEgressPorts_Object = MibTableColumn
statusEgressPorts = _StatusEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 7),
    _StatusEgressPorts_Type()
)
statusEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusEgressPorts.setStatus("current")
_StatusUntaggedPorts_Type = Integer32
_StatusUntaggedPorts_Object = MibTableColumn
statusUntaggedPorts = _StatusUntaggedPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 8),
    _StatusUntaggedPorts_Type()
)
statusUntaggedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusUntaggedPorts.setStatus("current")


class _StatusFabricAttachState_Type(Integer32):
    """Custom type statusFabricAttachState based on Integer32"""
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
          ("active", 1),
          ("rejected", 2))
    )


_StatusFabricAttachState_Type.__name__ = "Integer32"
_StatusFabricAttachState_Object = MibTableColumn
statusFabricAttachState = _StatusFabricAttachState_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 9),
    _StatusFabricAttachState_Type()
)
statusFabricAttachState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusFabricAttachState.setStatus("current")


class _StatusCreationMode_Type(Integer32):
    """Custom type statusCreationMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filterTable", 0),
          ("pacc", 1),
          ("mvrp", 2))
    )


_StatusCreationMode_Type.__name__ = "Integer32"
_StatusCreationMode_Object = MibTableColumn
statusCreationMode = _StatusCreationMode_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 10),
    _StatusCreationMode_Type()
)
statusCreationMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusCreationMode.setStatus("current")
_StatusCreationTime_Type = Counter32
_StatusCreationTime_Object = MibTableColumn
statusCreationTime = _StatusCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 101, 1, 11),
    _StatusCreationTime_Type()
)
statusCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusCreationTime.setStatus("current")
_PortStatusTable_Object = MibTable
portStatusTable = _PortStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 102)
)
if mibBuilder.loadTexts:
    portStatusTable.setStatus("current")
_PortStatusEntry_Object = MibTableRow
portStatusEntry = _PortStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 102, 1)
)
portStatusEntry.setIndexNames(
    (0, "G6-VLAN-MIB", "portStatusPortIndex"),
)
if mibBuilder.loadTexts:
    portStatusEntry.setStatus("current")


class _PortStatusPortIndex_Type(Integer32):
    """Custom type portStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_PortStatusPortIndex_Type.__name__ = "Integer32"
_PortStatusPortIndex_Object = MibTableColumn
portStatusPortIndex = _PortStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 102, 1, 1),
    _PortStatusPortIndex_Type()
)
portStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portStatusPortIndex.setStatus("current")
_PortStatusAssignedVlanIds_Type = DisplayString
_PortStatusAssignedVlanIds_Object = MibTableColumn
portStatusAssignedVlanIds = _PortStatusAssignedVlanIds_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 102, 1, 2),
    _PortStatusAssignedVlanIds_Type()
)
portStatusAssignedVlanIds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusAssignedVlanIds.setStatus("current")


class _PortStatusDynamicDefaultVlanId_Type(Integer32):
    """Custom type portStatusDynamicDefaultVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_PortStatusDynamicDefaultVlanId_Type.__name__ = "Integer32"
_PortStatusDynamicDefaultVlanId_Object = MibTableColumn
portStatusDynamicDefaultVlanId = _PortStatusDynamicDefaultVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 102, 1, 3),
    _PortStatusDynamicDefaultVlanId_Type()
)
portStatusDynamicDefaultVlanId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusDynamicDefaultVlanId.setStatus("current")


class _PortStatusLastUpdateMethod_Type(Integer32):
    """Custom type portStatusLastUpdateMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("config", 0),
          ("viaMacTable", 1),
          ("macViaRadius", 2),
          ("ms8021xViaRadius", 3))
    )


_PortStatusLastUpdateMethod_Type.__name__ = "Integer32"
_PortStatusLastUpdateMethod_Object = MibTableColumn
portStatusLastUpdateMethod = _PortStatusLastUpdateMethod_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 102, 1, 4),
    _PortStatusLastUpdateMethod_Type()
)
portStatusLastUpdateMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusLastUpdateMethod.setStatus("current")
_PortStatusLastUpdatingMac_Type = MacAddress
_PortStatusLastUpdatingMac_Object = MibTableColumn
portStatusLastUpdatingMac = _PortStatusLastUpdatingMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 102, 1, 5),
    _PortStatusLastUpdatingMac_Type()
)
portStatusLastUpdatingMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusLastUpdatingMac.setStatus("current")
_PortStatusLastUpdateTime_Type = Counter32
_PortStatusLastUpdateTime_Object = MibTableColumn
portStatusLastUpdateTime = _PortStatusLastUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 102, 1, 6),
    _PortStatusLastUpdateTime_Type()
)
portStatusLastUpdateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portStatusLastUpdateTime.setStatus("current")
_MvrpStatusTable_Object = MibTable
mvrpStatusTable = _MvrpStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 103)
)
if mibBuilder.loadTexts:
    mvrpStatusTable.setStatus("current")
_MvrpStatusEntry_Object = MibTableRow
mvrpStatusEntry = _MvrpStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 103, 1)
)
mvrpStatusEntry.setIndexNames(
    (0, "G6-VLAN-MIB", "mvrpStatusPortIndex"),
)
if mibBuilder.loadTexts:
    mvrpStatusEntry.setStatus("current")


class _MvrpStatusPortIndex_Type(Integer32):
    """Custom type mvrpStatusPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 24),
    )


_MvrpStatusPortIndex_Type.__name__ = "Integer32"
_MvrpStatusPortIndex_Object = MibTableColumn
mvrpStatusPortIndex = _MvrpStatusPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 103, 1, 1),
    _MvrpStatusPortIndex_Type()
)
mvrpStatusPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrpStatusPortIndex.setStatus("current")
_MvrpStatusLastSourceMac_Type = MacAddress
_MvrpStatusLastSourceMac_Object = MibTableColumn
mvrpStatusLastSourceMac = _MvrpStatusLastSourceMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 103, 1, 2),
    _MvrpStatusLastSourceMac_Type()
)
mvrpStatusLastSourceMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrpStatusLastSourceMac.setStatus("current")
_MvrpStatusFailedRegistrations_Type = Unsigned32
_MvrpStatusFailedRegistrations_Object = MibTableColumn
mvrpStatusFailedRegistrations = _MvrpStatusFailedRegistrations_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 82, 103, 1, 3),
    _MvrpStatusFailedRegistrations_Type()
)
mvrpStatusFailedRegistrations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrpStatusFailedRegistrations.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-VLAN-MIB",
    **{"protocol": protocol,
       "vlan": vlan,
       "vlanEnableVlanFiltering": vlanEnableVlanFiltering,
       "vlanIdConfigTable": vlanIdConfigTable,
       "vlanIdConfigEntry": vlanIdConfigEntry,
       "vlanIdConfigIndex": vlanIdConfigIndex,
       "vlanIdConfigManagementVlanId": vlanIdConfigManagementVlanId,
       "vlanIdConfigManagementPriority": vlanIdConfigManagementPriority,
       "vlanIdConfigVoiceVlanId": vlanIdConfigVoiceVlanId,
       "vlanIdConfigRstpVlanId": vlanIdConfigRstpVlanId,
       "vlanIdConfigUnauthorizedVlanId": vlanIdConfigUnauthorizedVlanId,
       "vlanIdConfigSmartofficeVlanId": vlanIdConfigSmartofficeVlanId,
       "portConfigTable": portConfigTable,
       "portConfigEntry": portConfigEntry,
       "portConfigPortIndex": portConfigPortIndex,
       "portConfigVlanMode": portConfigVlanMode,
       "portConfigDefaultVlanId": portConfigDefaultVlanId,
       "portConfigForceDefaultVlanId": portConfigForceDefaultVlanId,
       "portConfigDefaultPriority": portConfigDefaultPriority,
       "portConfigPriorityOverride": portConfigPriorityOverride,
       "portConfigUnauthorizedVlanId": portConfigUnauthorizedVlanId,
       "portConfigFallbackVlanId": portConfigFallbackVlanId,
       "portConfigQInQEthertype": portConfigQInQEthertype,
       "filterConfigTable": filterConfigTable,
       "filterConfigEntry": filterConfigEntry,
       "filterConfigIndex": filterConfigIndex,
       "filterConfigVlanId": filterConfigVlanId,
       "filterConfigEntryMode": filterConfigEntryMode,
       "filterConfigAlias": filterConfigAlias,
       "filterConfigMstpGroup": filterConfigMstpGroup,
       "filterConfigFabricAttachISid": filterConfigFabricAttachISid,
       "filterConfigPortMembers": filterConfigPortMembers,
       "filterConfigManagementMembers": filterConfigManagementMembers,
       "filterConfigPriorityOverride": filterConfigPriorityOverride,
       "filterConfigNewPriority": filterConfigNewPriority,
       "vlanEnableMvrp": vlanEnableMvrp,
       "mvrpPortConfigTable": mvrpPortConfigTable,
       "mvrpPortConfigEntry": mvrpPortConfigEntry,
       "mvrpPortConfigPortIndex": mvrpPortConfigPortIndex,
       "mvrpPortConfigEnableMvrp": mvrpPortConfigEnableMvrp,
       "mvrpPortConfigRegistrationMode": mvrpPortConfigRegistrationMode,
       "mvrpPortConfigJoinTimer": mvrpPortConfigJoinTimer,
       "mvrpPortConfigLeaveTimer": mvrpPortConfigLeaveTimer,
       "mvrpPortConfigLeaveallTimer": mvrpPortConfigLeaveallTimer,
       "fabricAttachPortConfigTable": fabricAttachPortConfigTable,
       "fabricAttachPortConfigEntry": fabricAttachPortConfigEntry,
       "fabricAttachPortConfigPortIndex": fabricAttachPortConfigPortIndex,
       "fabricAttachPortConfigEnableFabricAttach": fabricAttachPortConfigEnableFabricAttach,
       "fabricAttachPortConfigMsgAuthentication": fabricAttachPortConfigMsgAuthentication,
       "fabricAttachPortConfigEnterFaAuthKey": fabricAttachPortConfigEnterFaAuthKey,
       "fabricAttachPortConfigEncryptedFaAuthKey": fabricAttachPortConfigEncryptedFaAuthKey,
       "vlanNumberOfEntries": vlanNumberOfEntries,
       "statusTable": statusTable,
       "statusEntry": statusEntry,
       "statusVlanIndex": statusVlanIndex,
       "statusVlanId": statusVlanId,
       "statusTimeMark": statusTimeMark,
       "statusAlias": statusAlias,
       "statusPortMembers": statusPortMembers,
       "statusFilterDatabase": statusFilterDatabase,
       "statusEgressPorts": statusEgressPorts,
       "statusUntaggedPorts": statusUntaggedPorts,
       "statusFabricAttachState": statusFabricAttachState,
       "statusCreationMode": statusCreationMode,
       "statusCreationTime": statusCreationTime,
       "portStatusTable": portStatusTable,
       "portStatusEntry": portStatusEntry,
       "portStatusPortIndex": portStatusPortIndex,
       "portStatusAssignedVlanIds": portStatusAssignedVlanIds,
       "portStatusDynamicDefaultVlanId": portStatusDynamicDefaultVlanId,
       "portStatusLastUpdateMethod": portStatusLastUpdateMethod,
       "portStatusLastUpdatingMac": portStatusLastUpdatingMac,
       "portStatusLastUpdateTime": portStatusLastUpdateTime,
       "mvrpStatusTable": mvrpStatusTable,
       "mvrpStatusEntry": mvrpStatusEntry,
       "mvrpStatusPortIndex": mvrpStatusPortIndex,
       "mvrpStatusLastSourceMac": mvrpStatusLastSourceMac,
       "mvrpStatusFailedRegistrations": mvrpStatusFailedRegistrations}
)
