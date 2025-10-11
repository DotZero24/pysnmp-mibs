# SNMP MIB module (ALCATEL-ENT1-VLAN-MGR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-VLAN-MGR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:10:47 2025
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

(softentIND1VlanMgt,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1VlanMgt")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

alcatelIND1VLANMgrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIB.setRevisions(
        ("2007-04-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1VLANMgrMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1VLANMgrMIBObjects = _AlcatelIND1VLANMgrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIBObjects.setStatus("current")
_VlanMgrVlan_ObjectIdentity = ObjectIdentity
vlanMgrVlan = _VlanMgrVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VLAN-MGR-MIB", "vlanNumber"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")


class _VlanNumber_Type(Integer32):
    """Custom type vlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanNumber_Type.__name__ = "Integer32"
_VlanNumber_Object = MibTableColumn
vlanNumber = _VlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 1),
    _VlanNumber_Type()
)
vlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanNumber.setStatus("current")


class _VlanDescription_Type(SnmpAdminString):
    """Custom type vlanDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_VlanDescription_Type.__name__ = "SnmpAdminString"
_VlanDescription_Object = MibTableColumn
vlanDescription = _VlanDescription_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 2),
    _VlanDescription_Type()
)
vlanDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanDescription.setStatus("current")


class _VlanAdmStatus_Type(Integer32):
    """Custom type vlanAdmStatus based on Integer32"""
    defaultValue = 1

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


_VlanAdmStatus_Type.__name__ = "Integer32"
_VlanAdmStatus_Object = MibTableColumn
vlanAdmStatus = _VlanAdmStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 3),
    _VlanAdmStatus_Type()
)
vlanAdmStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanAdmStatus.setStatus("current")


class _VlanOperStatus_Type(Integer32):
    """Custom type vlanOperStatus based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )


_VlanOperStatus_Type.__name__ = "Integer32"
_VlanOperStatus_Object = MibTableColumn
vlanOperStatus = _VlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 4),
    _VlanOperStatus_Type()
)
vlanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanOperStatus.setStatus("current")
_VlanStatus_Type = RowStatus
_VlanStatus_Object = MibTableColumn
vlanStatus = _VlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 5),
    _VlanStatus_Type()
)
vlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanStatus.setStatus("current")


class _VlanRouterStatus_Type(Integer32):
    """Custom type vlanRouterStatus based on Integer32"""
    defaultValue = 0

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
          ("ipv4router", 1),
          ("ipv6router", 2),
          ("both", 3))
    )


_VlanRouterStatus_Type.__name__ = "Integer32"
_VlanRouterStatus_Object = MibTableColumn
vlanRouterStatus = _VlanRouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 6),
    _VlanRouterStatus_Type()
)
vlanRouterStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanRouterStatus.setStatus("current")


class _VlanSrcLearningStatus_Type(Integer32):
    """Custom type vlanSrcLearningStatus based on Integer32"""
    defaultValue = 1

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


_VlanSrcLearningStatus_Type.__name__ = "Integer32"
_VlanSrcLearningStatus_Object = MibTableColumn
vlanSrcLearningStatus = _VlanSrcLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 7),
    _VlanSrcLearningStatus_Type()
)
vlanSrcLearningStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanSrcLearningStatus.setStatus("current")


class _VlanType_Type(Integer32):
    """Custom type vlanType based on Integer32"""
    defaultValue = 5

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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("service", 1),
          ("multicastEnt", 2),
          ("multicastService", 3),
          ("dynamic", 4),
          ("standard", 5),
          ("ipc", 6),
          ("vipVlan", 7),
          ("erpVlan", 8),
          ("mtpVlan", 9),
          ("unpDynamic", 10),
          ("dynamicRemote", 11),
          ("bvlan", 12),
          ("controlBvlan", 13),
          ("evbVlan", 14),
          ("vcmipc", 15),
          ("fcoeVlan", 16),
          ("openflowVlan", 17),
          ("routerVlan", 18),
          ("primaryVlan", 19),
          ("isolatedVlan", 20),
          ("communityVlan", 21),
          ("allVlan", 22),
          ("invalidVlan", 23))
    )


_VlanType_Type.__name__ = "Integer32"
_VlanType_Object = MibTableColumn
vlanType = _VlanType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 8),
    _VlanType_Type()
)
vlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanType.setStatus("current")


class _VlanMtu_Type(Integer32):
    """Custom type vlanMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 10222),
    )


_VlanMtu_Type.__name__ = "Integer32"
_VlanMtu_Object = MibTableColumn
vlanMtu = _VlanMtu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 9),
    _VlanMtu_Type()
)
vlanMtu.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMtu.setStatus("current")


class _VlanAfdCfg_Type(Integer32):
    """Custom type vlanAfdCfg based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_VlanAfdCfg_Type.__name__ = "Integer32"
_VlanAfdCfg_Object = MibTableColumn
vlanAfdCfg = _VlanAfdCfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 1, 1, 1, 10),
    _VlanAfdCfg_Type()
)
vlanAfdCfg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanAfdCfg.setStatus("current")
_VlanMgrVpa_ObjectIdentity = ObjectIdentity
vlanMgrVpa = _VlanMgrVpa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2)
)
_VpaTable_Object = MibTable
vpaTable = _VpaTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    vpaTable.setStatus("current")
_VpaEntry_Object = MibTableRow
vpaEntry = _VpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1)
)
vpaEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VLAN-MGR-MIB", "vpaVlanNumber"),
    (0, "ALCATEL-ENT1-VLAN-MGR-MIB", "vpaIfIndex"),
)
if mibBuilder.loadTexts:
    vpaEntry.setStatus("current")


class _VpaVlanNumber_Type(Integer32):
    """Custom type vpaVlanNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VpaVlanNumber_Type.__name__ = "Integer32"
_VpaVlanNumber_Object = MibTableColumn
vpaVlanNumber = _VpaVlanNumber_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 1),
    _VpaVlanNumber_Type()
)
vpaVlanNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpaVlanNumber.setStatus("current")


class _VpaIfIndex_Type(Unsigned32):
    """Custom type vpaIfIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 4294967295),
    )


_VpaIfIndex_Type.__name__ = "Unsigned32"
_VpaIfIndex_Object = MibTableColumn
vpaIfIndex = _VpaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 2),
    _VpaIfIndex_Type()
)
vpaIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vpaIfIndex.setStatus("current")


class _VpaType_Type(Integer32):
    """Custom type vpaType based on Integer32"""
    defaultValue = 1

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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("cfgDefault", 1),
          ("qTagged", 2),
          ("dynamic", 3),
          ("vstkDoubleTag", 4),
          ("vstkTranslate", 5),
          ("forbidden", 6),
          ("mirrored", 7),
          ("bvpa", 8),
          ("unpUntagged", 9),
          ("unpTagged", 10),
          ("evbTagged", 11))
    )


_VpaType_Type.__name__ = "Integer32"
_VpaType_Object = MibTableColumn
vpaType = _VpaType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 3),
    _VpaType_Type()
)
vpaType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpaType.setStatus("current")


class _VpaState_Type(Integer32):
    """Custom type vpaState based on Integer32"""
    defaultValue = 2

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
        *(("forwarding", 0),
          ("blocking", 1),
          ("inactive", 2),
          ("invalid", 3),
          ("dhlBlocking", 4))
    )


_VpaState_Type.__name__ = "Integer32"
_VpaState_Object = MibTableColumn
vpaState = _VpaState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 4),
    _VpaState_Type()
)
vpaState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vpaState.setStatus("current")
_VpaStatus_Type = RowStatus
_VpaStatus_Object = MibTableColumn
vpaStatus = _VpaStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 2, 1, 1, 5),
    _VpaStatus_Type()
)
vpaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vpaStatus.setStatus("current")
_VlanMgrVlanSet_ObjectIdentity = ObjectIdentity
vlanMgrVlanSet = _VlanMgrVlanSet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3)
)


class _VlanSetVlanCount_Type(Integer32):
    """Custom type vlanSetVlanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_VlanSetVlanCount_Type.__name__ = "Integer32"
_VlanSetVlanCount_Object = MibScalar
vlanSetVlanCount = _VlanSetVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3, 1),
    _VlanSetVlanCount_Type()
)
vlanSetVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSetVlanCount.setStatus("current")


class _VlanSetDynamicVlanCount_Type(Integer32):
    """Custom type vlanSetDynamicVlanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanSetDynamicVlanCount_Type.__name__ = "Integer32"
_VlanSetDynamicVlanCount_Object = MibScalar
vlanSetDynamicVlanCount = _VlanSetDynamicVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3, 2),
    _VlanSetDynamicVlanCount_Type()
)
vlanSetDynamicVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSetDynamicVlanCount.setStatus("current")


class _VlanSetIpRouterCount_Type(Integer32):
    """Custom type vlanSetIpRouterCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanSetIpRouterCount_Type.__name__ = "Integer32"
_VlanSetIpRouterCount_Object = MibScalar
vlanSetIpRouterCount = _VlanSetIpRouterCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3, 3),
    _VlanSetIpRouterCount_Type()
)
vlanSetIpRouterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSetIpRouterCount.setStatus("current")


class _VlanSetVstkVlanCount_Type(Integer32):
    """Custom type vlanSetVstkVlanCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_VlanSetVstkVlanCount_Type.__name__ = "Integer32"
_VlanSetVstkVlanCount_Object = MibScalar
vlanSetVstkVlanCount = _VlanSetVstkVlanCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 1, 3, 4),
    _VlanSetVstkVlanCount_Type()
)
vlanSetVstkVlanCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vlanSetVstkVlanCount.setStatus("current")
_AlcatelIND1VLANMgrMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1VLANMgrMIBConformance = _AlcatelIND1VLANMgrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIBConformance.setStatus("current")
_AlcatelIND1VLANMgrMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1VLANMgrMIBGroups = _AlcatelIND1VLANMgrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIBGroups.setStatus("current")
_AlcatelIND1VLANMgrMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1VLANMgrMIBCompliances = _AlcatelIND1VLANMgrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIBCompliances.setStatus("current")

# Managed Objects groups

vlanMgrVlanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 1, 1)
)
vlanMgrVlanGroup.setObjects(
      *(("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanDescription"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanAdmStatus"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanOperStatus"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanStatus"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanRouterStatus"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanSrcLearningStatus"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanType"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanMtu"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanAfdCfg"))
)
if mibBuilder.loadTexts:
    vlanMgrVlanGroup.setStatus("current")

vlanMgrVpaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 1, 2)
)
vlanMgrVpaGroup.setObjects(
      *(("ALCATEL-ENT1-VLAN-MGR-MIB", "vpaType"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vpaState"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vpaStatus"))
)
if mibBuilder.loadTexts:
    vlanMgrVpaGroup.setStatus("current")

vlanMgrVlanSetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 1, 3)
)
vlanMgrVlanSetGroup.setObjects(
      *(("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanSetVlanCount"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanSetDynamicVlanCount"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanSetIpRouterCount"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanSetVstkVlanCount"))
)
if mibBuilder.loadTexts:
    vlanMgrVlanSetGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

alcatelIND1VLANMgrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 3, 1, 2, 2, 1)
)
alcatelIND1VLANMgrMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanMgrVlanGroup"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanMgrVpaGroup"),
        ("ALCATEL-ENT1-VLAN-MGR-MIB", "vlanMgrVlanSetGroup"))
)
if mibBuilder.loadTexts:
    alcatelIND1VLANMgrMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-VLAN-MGR-MIB",
    **{"alcatelIND1VLANMgrMIB": alcatelIND1VLANMgrMIB,
       "alcatelIND1VLANMgrMIBObjects": alcatelIND1VLANMgrMIBObjects,
       "vlanMgrVlan": vlanMgrVlan,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanNumber": vlanNumber,
       "vlanDescription": vlanDescription,
       "vlanAdmStatus": vlanAdmStatus,
       "vlanOperStatus": vlanOperStatus,
       "vlanStatus": vlanStatus,
       "vlanRouterStatus": vlanRouterStatus,
       "vlanSrcLearningStatus": vlanSrcLearningStatus,
       "vlanType": vlanType,
       "vlanMtu": vlanMtu,
       "vlanAfdCfg": vlanAfdCfg,
       "vlanMgrVpa": vlanMgrVpa,
       "vpaTable": vpaTable,
       "vpaEntry": vpaEntry,
       "vpaVlanNumber": vpaVlanNumber,
       "vpaIfIndex": vpaIfIndex,
       "vpaType": vpaType,
       "vpaState": vpaState,
       "vpaStatus": vpaStatus,
       "vlanMgrVlanSet": vlanMgrVlanSet,
       "vlanSetVlanCount": vlanSetVlanCount,
       "vlanSetDynamicVlanCount": vlanSetDynamicVlanCount,
       "vlanSetIpRouterCount": vlanSetIpRouterCount,
       "vlanSetVstkVlanCount": vlanSetVstkVlanCount,
       "alcatelIND1VLANMgrMIBConformance": alcatelIND1VLANMgrMIBConformance,
       "alcatelIND1VLANMgrMIBGroups": alcatelIND1VLANMgrMIBGroups,
       "vlanMgrVlanGroup": vlanMgrVlanGroup,
       "vlanMgrVpaGroup": vlanMgrVpaGroup,
       "vlanMgrVlanSetGroup": vlanMgrVlanSetGroup,
       "alcatelIND1VLANMgrMIBCompliances": alcatelIND1VLANMgrMIBCompliances,
       "alcatelIND1VLANMgrMIBCompliance": alcatelIND1VLANMgrMIBCompliance}
)
