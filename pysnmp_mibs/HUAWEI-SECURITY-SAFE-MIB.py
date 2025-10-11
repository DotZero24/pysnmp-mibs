# SNMP MIB module (HUAWEI-SECURITY-SAFE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/huawei/HUAWEI-SECURITY-SAFE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:24:52 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hwSAFEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20)
)
if mibBuilder.loadTexts:
    hwSAFEMIB.setRevisions(
        ("2017-07-13 16:49",
         "2017-06-19 16:49",
         "2017-04-07 14:41",
         "2009-06-30 17:00",
         "2017-01-24 17:00",
         "2017-02-22 17:00",
         "2017-04-07 14:41",
         "2017-04-07 14:41")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Huawei_ObjectIdentity = ObjectIdentity
huawei = _Huawei_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011)
)
_HuaweiUtility_ObjectIdentity = ObjectIdentity
huaweiUtility = _HuaweiUtility_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6)
)
_HwSecurity_ObjectIdentity = ObjectIdentity
hwSecurity = _HwSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122)
)
_HwDeviceObject_ObjectIdentity = ObjectIdentity
hwDeviceObject = _HwDeviceObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1)
)
_HwSANodeObject_ObjectIdentity = ObjectIdentity
hwSANodeObject = _HwSANodeObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1)
)
_HwSpuSysInfoTable_Object = MibTable
hwSpuSysInfoTable = _HwSpuSysInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hwSpuSysInfoTable.setStatus("current")
_HwSpuSysInfoEntry_Object = MibTableRow
hwSpuSysInfoEntry = _HwSpuSysInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 1, 1)
)
hwSpuSysInfoEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoIndex"),
)
if mibBuilder.loadTexts:
    hwSpuSysInfoEntry.setStatus("current")


class _HwSpuSysInfoIndex_Type(Gauge32):
    """Custom type hwSpuSysInfoIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSpuSysInfoIndex_Type.__name__ = "Gauge32"
_HwSpuSysInfoIndex_Object = MibTableColumn
hwSpuSysInfoIndex = _HwSpuSysInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 1, 1, 1),
    _HwSpuSysInfoIndex_Type()
)
hwSpuSysInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpuSysInfoIndex.setStatus("current")


class _HwSpuSysInfoLocation_Type(OctetString):
    """Custom type hwSpuSysInfoLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSpuSysInfoLocation_Type.__name__ = "OctetString"
_HwSpuSysInfoLocation_Object = MibTableColumn
hwSpuSysInfoLocation = _HwSpuSysInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 1, 1, 2),
    _HwSpuSysInfoLocation_Type()
)
hwSpuSysInfoLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuSysInfoLocation.setStatus("current")


class _HwSpuSysInfoType_Type(Integer32):
    """Custom type hwSpuSysInfoType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sas", 1),
          ("sps", 2))
    )


_HwSpuSysInfoType_Type.__name__ = "Integer32"
_HwSpuSysInfoType_Object = MibTableColumn
hwSpuSysInfoType = _HwSpuSysInfoType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 1, 1, 3),
    _HwSpuSysInfoType_Type()
)
hwSpuSysInfoType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuSysInfoType.setStatus("current")
_HwSpuSysInfoIPAddress_Type = IpAddress
_HwSpuSysInfoIPAddress_Object = MibTableColumn
hwSpuSysInfoIPAddress = _HwSpuSysInfoIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 1, 1, 4),
    _HwSpuSysInfoIPAddress_Type()
)
hwSpuSysInfoIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuSysInfoIPAddress.setStatus("current")


class _HwSpuSysInfoState_Type(Integer32):
    """Custom type hwSpuSysInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_HwSpuSysInfoState_Type.__name__ = "Integer32"
_HwSpuSysInfoState_Object = MibTableColumn
hwSpuSysInfoState = _HwSpuSysInfoState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 1, 1, 5),
    _HwSpuSysInfoState_Type()
)
hwSpuSysInfoState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuSysInfoState.setStatus("current")
_HwServiceLinkTable_Object = MibTable
hwServiceLinkTable = _HwServiceLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hwServiceLinkTable.setStatus("current")
_HwServiceLinkEntry_Object = MibTableRow
hwServiceLinkEntry = _HwServiceLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1)
)
hwServiceLinkEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkIndex"),
)
if mibBuilder.loadTexts:
    hwServiceLinkEntry.setStatus("current")


class _HwServiceLinkIndex_Type(Gauge32):
    """Custom type hwServiceLinkIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 320),
    )


_HwServiceLinkIndex_Type.__name__ = "Gauge32"
_HwServiceLinkIndex_Object = MibTableColumn
hwServiceLinkIndex = _HwServiceLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1, 1),
    _HwServiceLinkIndex_Type()
)
hwServiceLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwServiceLinkIndex.setStatus("current")


class _HwServiceLinkType_Type(Integer32):
    """Custom type hwServiceLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("oneg", 1),
          ("twodotfiveg", 2),
          ("teng", 3),
          ("fortyg", 4),
          ("onehundredg", 5))
    )


_HwServiceLinkType_Type.__name__ = "Integer32"
_HwServiceLinkType_Object = MibTableColumn
hwServiceLinkType = _HwServiceLinkType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1, 2),
    _HwServiceLinkType_Type()
)
hwServiceLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceLinkType.setStatus("current")


class _HwServiceLinkName_Type(OctetString):
    """Custom type hwServiceLinkName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwServiceLinkName_Type.__name__ = "OctetString"
_HwServiceLinkName_Object = MibTableColumn
hwServiceLinkName = _HwServiceLinkName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1, 3),
    _HwServiceLinkName_Type()
)
hwServiceLinkName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceLinkName.setStatus("current")


class _HwServiceLinkInsideInterface_Type(OctetString):
    """Custom type hwServiceLinkInsideInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwServiceLinkInsideInterface_Type.__name__ = "OctetString"
_HwServiceLinkInsideInterface_Object = MibTableColumn
hwServiceLinkInsideInterface = _HwServiceLinkInsideInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1, 4),
    _HwServiceLinkInsideInterface_Type()
)
hwServiceLinkInsideInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceLinkInsideInterface.setStatus("current")


class _HwServiceLinkOutsideInterface_Type(OctetString):
    """Custom type hwServiceLinkOutsideInterface based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwServiceLinkOutsideInterface_Type.__name__ = "OctetString"
_HwServiceLinkOutsideInterface_Object = MibTableColumn
hwServiceLinkOutsideInterface = _HwServiceLinkOutsideInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1, 5),
    _HwServiceLinkOutsideInterface_Type()
)
hwServiceLinkOutsideInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceLinkOutsideInterface.setStatus("current")


class _HwServiceLinkInsideInterfaceState_Type(Integer32):
    """Custom type hwServiceLinkInsideInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_HwServiceLinkInsideInterfaceState_Type.__name__ = "Integer32"
_HwServiceLinkInsideInterfaceState_Object = MibTableColumn
hwServiceLinkInsideInterfaceState = _HwServiceLinkInsideInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1, 6),
    _HwServiceLinkInsideInterfaceState_Type()
)
hwServiceLinkInsideInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceLinkInsideInterfaceState.setStatus("current")


class _HwServiceLinkOutsideInterfaceState_Type(Integer32):
    """Custom type hwServiceLinkOutsideInterfaceState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_HwServiceLinkOutsideInterfaceState_Type.__name__ = "Integer32"
_HwServiceLinkOutsideInterfaceState_Object = MibTableColumn
hwServiceLinkOutsideInterfaceState = _HwServiceLinkOutsideInterfaceState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1, 7),
    _HwServiceLinkOutsideInterfaceState_Type()
)
hwServiceLinkOutsideInterfaceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceLinkOutsideInterfaceState.setStatus("current")


class _HwServiceLinkInsideInterfaceBandWidth_Type(OctetString):
    """Custom type hwServiceLinkInsideInterfaceBandWidth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwServiceLinkInsideInterfaceBandWidth_Type.__name__ = "OctetString"
_HwServiceLinkInsideInterfaceBandWidth_Object = MibTableColumn
hwServiceLinkInsideInterfaceBandWidth = _HwServiceLinkInsideInterfaceBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1, 8),
    _HwServiceLinkInsideInterfaceBandWidth_Type()
)
hwServiceLinkInsideInterfaceBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceLinkInsideInterfaceBandWidth.setStatus("current")


class _HwServiceLinkOutsideInterfaceBandWidth_Type(OctetString):
    """Custom type hwServiceLinkOutsideInterfaceBandWidth based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwServiceLinkOutsideInterfaceBandWidth_Type.__name__ = "OctetString"
_HwServiceLinkOutsideInterfaceBandWidth_Object = MibTableColumn
hwServiceLinkOutsideInterfaceBandWidth = _HwServiceLinkOutsideInterfaceBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1, 9),
    _HwServiceLinkOutsideInterfaceBandWidth_Type()
)
hwServiceLinkOutsideInterfaceBandWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceLinkOutsideInterfaceBandWidth.setStatus("current")


class _HwServiceLinkBoundGroupNumber_Type(Gauge32):
    """Custom type hwServiceLinkBoundGroupNumber based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 320),
    )


_HwServiceLinkBoundGroupNumber_Type.__name__ = "Gauge32"
_HwServiceLinkBoundGroupNumber_Object = MibTableColumn
hwServiceLinkBoundGroupNumber = _HwServiceLinkBoundGroupNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 2, 1, 10),
    _HwServiceLinkBoundGroupNumber_Type()
)
hwServiceLinkBoundGroupNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceLinkBoundGroupNumber.setStatus("current")
_HwCascadeInterfaceTable_Object = MibTable
hwCascadeInterfaceTable = _HwCascadeInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hwCascadeInterfaceTable.setStatus("current")
_HwCascadeInterfaceEntry_Object = MibTableRow
hwCascadeInterfaceEntry = _HwCascadeInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 3, 1)
)
hwCascadeInterfaceEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwCascadeInterfaceIndex"),
)
if mibBuilder.loadTexts:
    hwCascadeInterfaceEntry.setStatus("current")


class _HwCascadeInterfaceIndex_Type(Gauge32):
    """Custom type hwCascadeInterfaceIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_HwCascadeInterfaceIndex_Type.__name__ = "Gauge32"
_HwCascadeInterfaceIndex_Object = MibTableColumn
hwCascadeInterfaceIndex = _HwCascadeInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 3, 1, 1),
    _HwCascadeInterfaceIndex_Type()
)
hwCascadeInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCascadeInterfaceIndex.setStatus("current")
_HwCascadeInterface_Type = OctetString
_HwCascadeInterface_Object = MibTableColumn
hwCascadeInterface = _HwCascadeInterface_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 3, 1, 2),
    _HwCascadeInterface_Type()
)
hwCascadeInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCascadeInterface.setStatus("current")
_HwCascadeInterfaceStatus_Type = OctetString
_HwCascadeInterfaceStatus_Object = MibTableColumn
hwCascadeInterfaceStatus = _HwCascadeInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 1, 3, 1, 3),
    _HwCascadeInterfaceStatus_Type()
)
hwCascadeInterfaceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCascadeInterfaceStatus.setStatus("current")
_HwSANodeTraps_ObjectIdentity = ObjectIdentity
hwSANodeTraps = _HwSANodeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 2)
)
_HwSAClusterObject_ObjectIdentity = ObjectIdentity
hwSAClusterObject = _HwSAClusterObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3)
)
_HwClusterNodeTable_Object = MibTable
hwClusterNodeTable = _HwClusterNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1)
)
if mibBuilder.loadTexts:
    hwClusterNodeTable.setStatus("current")
_HwClusterNodeEntry_Object = MibTableRow
hwClusterNodeEntry = _HwClusterNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1, 1)
)
hwClusterNodeEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIndex"),
)
if mibBuilder.loadTexts:
    hwClusterNodeEntry.setStatus("current")


class _HwClusterNodeIndex_Type(Integer32):
    """Custom type hwClusterNodeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwClusterNodeIndex_Type.__name__ = "Integer32"
_HwClusterNodeIndex_Object = MibTableColumn
hwClusterNodeIndex = _HwClusterNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1, 1, 1),
    _HwClusterNodeIndex_Type()
)
hwClusterNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClusterNodeIndex.setStatus("current")


class _HwClusterNodeName_Type(OctetString):
    """Custom type hwClusterNodeName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwClusterNodeName_Type.__name__ = "OctetString"
_HwClusterNodeName_Object = MibTableColumn
hwClusterNodeName = _HwClusterNodeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1, 1, 2),
    _HwClusterNodeName_Type()
)
hwClusterNodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterNodeName.setStatus("current")
_HwClusterNodeIPAddress_Type = IpAddress
_HwClusterNodeIPAddress_Object = MibTableColumn
hwClusterNodeIPAddress = _HwClusterNodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1, 1, 3),
    _HwClusterNodeIPAddress_Type()
)
hwClusterNodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterNodeIPAddress.setStatus("current")


class _HwClusterNodeRole_Type(Integer32):
    """Custom type hwClusterNodeRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("slave", 2),
          ("backup", 3))
    )


_HwClusterNodeRole_Type.__name__ = "Integer32"
_HwClusterNodeRole_Object = MibTableColumn
hwClusterNodeRole = _HwClusterNodeRole_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1, 1, 4),
    _HwClusterNodeRole_Type()
)
hwClusterNodeRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterNodeRole.setStatus("current")


class _HwClusterNodeStatus_Type(Integer32):
    """Custom type hwClusterNodeStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2),
          ("holdon", 3))
    )


_HwClusterNodeStatus_Type.__name__ = "Integer32"
_HwClusterNodeStatus_Object = MibTableColumn
hwClusterNodeStatus = _HwClusterNodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1, 1, 5),
    _HwClusterNodeStatus_Type()
)
hwClusterNodeStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterNodeStatus.setStatus("current")


class _HwNormalSPSNumber_Type(Integer32):
    """Custom type hwNormalSPSNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwNormalSPSNumber_Type.__name__ = "Integer32"
_HwNormalSPSNumber_Object = MibTableColumn
hwNormalSPSNumber = _HwNormalSPSNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1, 1, 6),
    _HwNormalSPSNumber_Type()
)
hwNormalSPSNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNormalSPSNumber.setStatus("current")
_HwCascadeCfg_Type = OctetString
_HwCascadeCfg_Object = MibTableColumn
hwCascadeCfg = _HwCascadeCfg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1, 1, 7),
    _HwCascadeCfg_Type()
)
hwCascadeCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCascadeCfg.setStatus("current")


class _HwCascadePeerState_Type(Integer32):
    """Custom type hwCascadePeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_HwCascadePeerState_Type.__name__ = "Integer32"
_HwCascadePeerState_Object = MibTableColumn
hwCascadePeerState = _HwCascadePeerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1, 1, 8),
    _HwCascadePeerState_Type()
)
hwCascadePeerState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCascadePeerState.setStatus("current")


class _HwCascadeSelfState_Type(Integer32):
    """Custom type hwCascadeSelfState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_HwCascadeSelfState_Type.__name__ = "Integer32"
_HwCascadeSelfState_Object = MibTableColumn
hwCascadeSelfState = _HwCascadeSelfState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 1, 1, 9),
    _HwCascadeSelfState_Type()
)
hwCascadeSelfState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCascadeSelfState.setStatus("current")
_HwClusterSasTable_Object = MibTable
hwClusterSasTable = _HwClusterSasTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 2)
)
if mibBuilder.loadTexts:
    hwClusterSasTable.setStatus("current")
_HwClusterSasEntry_Object = MibTableRow
hwClusterSasEntry = _HwClusterSasEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 2, 1)
)
hwClusterSasEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwClusterSasIndex"),
)
if mibBuilder.loadTexts:
    hwClusterSasEntry.setStatus("current")
_HwClusterSasIndex_Type = Gauge32
_HwClusterSasIndex_Object = MibTableColumn
hwClusterSasIndex = _HwClusterSasIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 2, 1, 1),
    _HwClusterSasIndex_Type()
)
hwClusterSasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClusterSasIndex.setStatus("current")


class _HwClusterSasNodeNumber_Type(Integer32):
    """Custom type hwClusterSasNodeNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_HwClusterSasNodeNumber_Type.__name__ = "Integer32"
_HwClusterSasNodeNumber_Object = MibTableColumn
hwClusterSasNodeNumber = _HwClusterSasNodeNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 2, 1, 2),
    _HwClusterSasNodeNumber_Type()
)
hwClusterSasNodeNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterSasNodeNumber.setStatus("current")


class _HwClusterSasSysLocation_Type(OctetString):
    """Custom type hwClusterSasSysLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwClusterSasSysLocation_Type.__name__ = "OctetString"
_HwClusterSasSysLocation_Object = MibTableColumn
hwClusterSasSysLocation = _HwClusterSasSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 2, 1, 3),
    _HwClusterSasSysLocation_Type()
)
hwClusterSasSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterSasSysLocation.setStatus("current")
_HwClusterSasSysIPAddress_Type = IpAddress
_HwClusterSasSysIPAddress_Object = MibTableColumn
hwClusterSasSysIPAddress = _HwClusterSasSysIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 2, 1, 4),
    _HwClusterSasSysIPAddress_Type()
)
hwClusterSasSysIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterSasSysIPAddress.setStatus("current")


class _HwClusterSasMode_Type(Integer32):
    """Custom type hwClusterSasMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("main", 3),
          ("wait", 4))
    )


_HwClusterSasMode_Type.__name__ = "Integer32"
_HwClusterSasMode_Object = MibTableColumn
hwClusterSasMode = _HwClusterSasMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 2, 1, 5),
    _HwClusterSasMode_Type()
)
hwClusterSasMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterSasMode.setStatus("current")
_HwClusterMapTable_Object = MibTable
hwClusterMapTable = _HwClusterMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 3)
)
if mibBuilder.loadTexts:
    hwClusterMapTable.setStatus("current")
_HwClusterMapEntry_Object = MibTableRow
hwClusterMapEntry = _HwClusterMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 3, 1)
)
hwClusterMapEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwClusterMapSasIndex"),
)
if mibBuilder.loadTexts:
    hwClusterMapEntry.setStatus("current")


class _HwClusterMapSasIndex_Type(Gauge32):
    """Custom type hwClusterMapSasIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwClusterMapSasIndex_Type.__name__ = "Gauge32"
_HwClusterMapSasIndex_Object = MibTableColumn
hwClusterMapSasIndex = _HwClusterMapSasIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 3, 1, 1),
    _HwClusterMapSasIndex_Type()
)
hwClusterMapSasIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwClusterMapSasIndex.setStatus("current")


class _HwClusterMapSysSasMode_Type(Integer32):
    """Custom type hwClusterMapSysSasMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("main", 3))
    )


_HwClusterMapSysSasMode_Type.__name__ = "Integer32"
_HwClusterMapSysSasMode_Object = MibTableColumn
hwClusterMapSysSasMode = _HwClusterMapSysSasMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 3, 1, 2),
    _HwClusterMapSysSasMode_Type()
)
hwClusterMapSysSasMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterMapSysSasMode.setStatus("current")


class _HwClusterMapNumberOfDG_Type(Integer32):
    """Custom type hwClusterMapNumberOfDG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_HwClusterMapNumberOfDG_Type.__name__ = "Integer32"
_HwClusterMapNumberOfDG_Object = MibTableColumn
hwClusterMapNumberOfDG = _HwClusterMapNumberOfDG_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 3, 1, 3),
    _HwClusterMapNumberOfDG_Type()
)
hwClusterMapNumberOfDG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterMapNumberOfDG.setStatus("current")


class _HwClusterMapDevices_Type(OctetString):
    """Custom type hwClusterMapDevices based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwClusterMapDevices_Type.__name__ = "OctetString"
_HwClusterMapDevices_Object = MibTableColumn
hwClusterMapDevices = _HwClusterMapDevices_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 3, 1, 4),
    _HwClusterMapDevices_Type()
)
hwClusterMapDevices.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwClusterMapDevices.setStatus("current")
_HwComponentTable_Object = MibTable
hwComponentTable = _HwComponentTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4)
)
if mibBuilder.loadTexts:
    hwComponentTable.setStatus("current")
_HwComponentEntry_Object = MibTableRow
hwComponentEntry = _HwComponentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4, 1)
)
hwComponentEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwComponentIndex"),
)
if mibBuilder.loadTexts:
    hwComponentEntry.setStatus("current")


class _HwComponentIndex_Type(Integer32):
    """Custom type hwComponentIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwComponentIndex_Type.__name__ = "Integer32"
_HwComponentIndex_Object = MibTableColumn
hwComponentIndex = _HwComponentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4, 1, 1),
    _HwComponentIndex_Type()
)
hwComponentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwComponentIndex.setStatus("current")


class _HwComponentType_Type(Integer32):
    """Custom type hwComponentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              13)
        )
    )
    namedValues = NamedValues(
        *(("dataanalysisserver", 2),
          ("policyserver", 3),
          ("managementserver", 4),
          ("serviceprobesystem", 5),
          ("serviceanalysesystem", 6),
          ("radiusproxy", 7),
          ("updateserver", 8),
          ("urlhealthcenter", 9),
          ("onlinechargingsystem", 10),
          ("policyandchargingrulesfunction", 11),
          ("quotamanagementserver", 13))
    )


_HwComponentType_Type.__name__ = "Integer32"
_HwComponentType_Object = MibTableColumn
hwComponentType = _HwComponentType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4, 1, 2),
    _HwComponentType_Type()
)
hwComponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwComponentType.setStatus("current")
_HwComponentNumber_Type = Integer32
_HwComponentNumber_Object = MibTableColumn
hwComponentNumber = _HwComponentNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4, 1, 3),
    _HwComponentNumber_Type()
)
hwComponentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwComponentNumber.setStatus("current")


class _HwComponentName_Type(OctetString):
    """Custom type hwComponentName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwComponentName_Type.__name__ = "OctetString"
_HwComponentName_Object = MibTableColumn
hwComponentName = _HwComponentName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4, 1, 4),
    _HwComponentName_Type()
)
hwComponentName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwComponentName.setStatus("current")
_HwComponentPrimaryIPAddress_Type = IpAddress
_HwComponentPrimaryIPAddress_Object = MibTableColumn
hwComponentPrimaryIPAddress = _HwComponentPrimaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4, 1, 5),
    _HwComponentPrimaryIPAddress_Type()
)
hwComponentPrimaryIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwComponentPrimaryIPAddress.setStatus("current")
_HwComponenSecondaryIPAddress_Type = IpAddress
_HwComponenSecondaryIPAddress_Object = MibTableColumn
hwComponenSecondaryIPAddress = _HwComponenSecondaryIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4, 1, 6),
    _HwComponenSecondaryIPAddress_Type()
)
hwComponenSecondaryIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwComponenSecondaryIPAddress.setStatus("current")


class _HwComponentPriIPConnStatus_Type(Integer32):
    """Custom type hwComponentPriIPConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_HwComponentPriIPConnStatus_Type.__name__ = "Integer32"
_HwComponentPriIPConnStatus_Object = MibTableColumn
hwComponentPriIPConnStatus = _HwComponentPriIPConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4, 1, 7),
    _HwComponentPriIPConnStatus_Type()
)
hwComponentPriIPConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwComponentPriIPConnStatus.setStatus("current")


class _HwComponentSecIPConnStatus_Type(Integer32):
    """Custom type hwComponentSecIPConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_HwComponentSecIPConnStatus_Type.__name__ = "Integer32"
_HwComponentSecIPConnStatus_Object = MibTableColumn
hwComponentSecIPConnStatus = _HwComponentSecIPConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4, 1, 8),
    _HwComponentSecIPConnStatus_Type()
)
hwComponentSecIPConnStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwComponentSecIPConnStatus.setStatus("current")


class _HwComponentUsageMode_Type(Integer32):
    """Custom type hwComponentUsageMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("standby", 2),
          ("main", 3),
          ("wait", 4),
          ("inactive", 5))
    )


_HwComponentUsageMode_Type.__name__ = "Integer32"
_HwComponentUsageMode_Object = MibTableColumn
hwComponentUsageMode = _HwComponentUsageMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 3, 4, 1, 9),
    _HwComponentUsageMode_Type()
)
hwComponentUsageMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwComponentUsageMode.setStatus("current")
_HwClusterTraps_ObjectIdentity = ObjectIdentity
hwClusterTraps = _HwClusterTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4)
)
_HwInternBypassObject_ObjectIdentity = ObjectIdentity
hwInternBypassObject = _HwInternBypassObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5)
)
_HwBypassLinkStateTable_Object = MibTable
hwBypassLinkStateTable = _HwBypassLinkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1)
)
if mibBuilder.loadTexts:
    hwBypassLinkStateTable.setStatus("current")
_HwBypassLinkStateEntry_Object = MibTableRow
hwBypassLinkStateEntry = _HwBypassLinkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1)
)
hwBypassLinkStateEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateIndex"),
)
if mibBuilder.loadTexts:
    hwBypassLinkStateEntry.setStatus("current")


class _HwBypassLinkStateIndex_Type(Gauge32):
    """Custom type hwBypassLinkStateIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwBypassLinkStateIndex_Type.__name__ = "Gauge32"
_HwBypassLinkStateIndex_Object = MibTableColumn
hwBypassLinkStateIndex = _HwBypassLinkStateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 1),
    _HwBypassLinkStateIndex_Type()
)
hwBypassLinkStateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBypassLinkStateIndex.setStatus("current")


class _HwBypassLinkStateLink_Type(OctetString):
    """Custom type hwBypassLinkStateLink based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwBypassLinkStateLink_Type.__name__ = "OctetString"
_HwBypassLinkStateLink_Object = MibTableColumn
hwBypassLinkStateLink = _HwBypassLinkStateLink_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 2),
    _HwBypassLinkStateLink_Type()
)
hwBypassLinkStateLink.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassLinkStateLink.setStatus("current")


class _HwBypassLinkStateMode_Type(Integer32):
    """Custom type hwBypassLinkStateMode based on Integer32"""
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
        *(("auto", 0),
          ("manual", 1),
          ("force", 2),
          ("lock", 3))
    )


_HwBypassLinkStateMode_Type.__name__ = "Integer32"
_HwBypassLinkStateMode_Object = MibTableColumn
hwBypassLinkStateMode = _HwBypassLinkStateMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 3),
    _HwBypassLinkStateMode_Type()
)
hwBypassLinkStateMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBypassLinkStateMode.setStatus("current")


class _HwBypassLinkStateChannel0State_Type(Integer32):
    """Custom type hwBypassLinkStateChannel0State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("working", 0),
          ("protection", 1))
    )


_HwBypassLinkStateChannel0State_Type.__name__ = "Integer32"
_HwBypassLinkStateChannel0State_Object = MibTableColumn
hwBypassLinkStateChannel0State = _HwBypassLinkStateChannel0State_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 4),
    _HwBypassLinkStateChannel0State_Type()
)
hwBypassLinkStateChannel0State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassLinkStateChannel0State.setStatus("current")


class _HwBypassLinkStateChannel1State_Type(Integer32):
    """Custom type hwBypassLinkStateChannel1State based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("working", 0),
          ("protection", 1))
    )


_HwBypassLinkStateChannel1State_Type.__name__ = "Integer32"
_HwBypassLinkStateChannel1State_Object = MibTableColumn
hwBypassLinkStateChannel1State = _HwBypassLinkStateChannel1State_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 5),
    _HwBypassLinkStateChannel1State_Type()
)
hwBypassLinkStateChannel1State.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassLinkStateChannel1State.setStatus("current")


class _HwBypassLinkStateRIsignal_Type(OctetString):
    """Custom type hwBypassLinkStateRIsignal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwBypassLinkStateRIsignal_Type.__name__ = "OctetString"
_HwBypassLinkStateRIsignal_Object = MibTableColumn
hwBypassLinkStateRIsignal = _HwBypassLinkStateRIsignal_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 6),
    _HwBypassLinkStateRIsignal_Type()
)
hwBypassLinkStateRIsignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassLinkStateRIsignal.setStatus("current")


class _HwBypassLinkCurrentState_Type(OctetString):
    """Custom type hwBypassLinkCurrentState based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwBypassLinkCurrentState_Type.__name__ = "OctetString"
_HwBypassLinkCurrentState_Object = MibTableColumn
hwBypassLinkCurrentState = _HwBypassLinkCurrentState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 7),
    _HwBypassLinkCurrentState_Type()
)
hwBypassLinkCurrentState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassLinkCurrentState.setStatus("current")
_HwBypassLinkLosTimes_Type = Integer32
_HwBypassLinkLosTimes_Object = MibTableColumn
hwBypassLinkLosTimes = _HwBypassLinkLosTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 8),
    _HwBypassLinkLosTimes_Type()
)
hwBypassLinkLosTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassLinkLosTimes.setStatus("current")
_HwBypassLinkLinkTimes_Type = Integer32
_HwBypassLinkLinkTimes_Object = MibTableColumn
hwBypassLinkLinkTimes = _HwBypassLinkLinkTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 9),
    _HwBypassLinkLinkTimes_Type()
)
hwBypassLinkLinkTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassLinkLinkTimes.setStatus("current")


class _HwBypassSwitchCurrentPosition_Type(OctetString):
    """Custom type hwBypassSwitchCurrentPosition based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwBypassSwitchCurrentPosition_Type.__name__ = "OctetString"
_HwBypassSwitchCurrentPosition_Object = MibTableColumn
hwBypassSwitchCurrentPosition = _HwBypassSwitchCurrentPosition_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 10),
    _HwBypassSwitchCurrentPosition_Type()
)
hwBypassSwitchCurrentPosition.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassSwitchCurrentPosition.setStatus("current")
_HwBypassSwitchWorkingTimes_Type = Integer32
_HwBypassSwitchWorkingTimes_Object = MibTableColumn
hwBypassSwitchWorkingTimes = _HwBypassSwitchWorkingTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 11),
    _HwBypassSwitchWorkingTimes_Type()
)
hwBypassSwitchWorkingTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassSwitchWorkingTimes.setStatus("current")
_HwBypassSwitchProtectionTimes_Type = Integer32
_HwBypassSwitchProtectionTimes_Object = MibTableColumn
hwBypassSwitchProtectionTimes = _HwBypassSwitchProtectionTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 12),
    _HwBypassSwitchProtectionTimes_Type()
)
hwBypassSwitchProtectionTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassSwitchProtectionTimes.setStatus("current")
_HwBypassSlotNum_Type = Integer32
_HwBypassSlotNum_Object = MibTableColumn
hwBypassSlotNum = _HwBypassSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 13),
    _HwBypassSlotNum_Type()
)
hwBypassSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassSlotNum.setStatus("current")


class _HwBypassPowerStatus_Type(OctetString):
    """Custom type hwBypassPowerStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwBypassPowerStatus_Type.__name__ = "OctetString"
_HwBypassPowerStatus_Object = MibTableColumn
hwBypassPowerStatus = _HwBypassPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 14),
    _HwBypassPowerStatus_Type()
)
hwBypassPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassPowerStatus.setStatus("current")


class _HwBypassAlarmDescription_Type(OctetString):
    """Custom type hwBypassAlarmDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwBypassAlarmDescription_Type.__name__ = "OctetString"
_HwBypassAlarmDescription_Object = MibTableColumn
hwBypassAlarmDescription = _HwBypassAlarmDescription_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 5, 1, 1, 15),
    _HwBypassAlarmDescription_Type()
)
hwBypassAlarmDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBypassAlarmDescription.setStatus("current")
_HwInternBypassTraps_ObjectIdentity = ObjectIdentity
hwInternBypassTraps = _HwInternBypassTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 6)
)
_HwSpuEntityObject_ObjectIdentity = ObjectIdentity
hwSpuEntityObject = _HwSpuEntityObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7)
)
_HwSpuEntityStateTable_Object = MibTable
hwSpuEntityStateTable = _HwSpuEntityStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1)
)
if mibBuilder.loadTexts:
    hwSpuEntityStateTable.setStatus("current")
_HwSpuEntityStateEntry_Object = MibTableRow
hwSpuEntityStateEntry = _HwSpuEntityStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1, 1)
)
hwSpuEntityStateEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityCpuNumber"),
)
if mibBuilder.loadTexts:
    hwSpuEntityStateEntry.setStatus("current")


class _HwSpuEntityCpuNumber_Type(Gauge32):
    """Custom type hwSpuEntityCpuNumber based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwSpuEntityCpuNumber_Type.__name__ = "Gauge32"
_HwSpuEntityCpuNumber_Object = MibTableColumn
hwSpuEntityCpuNumber = _HwSpuEntityCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1, 1, 1),
    _HwSpuEntityCpuNumber_Type()
)
hwSpuEntityCpuNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpuEntityCpuNumber.setStatus("current")


class _HwSpuEntityPhysicalIndex_Type(Gauge32):
    """Custom type hwSpuEntityPhysicalIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSpuEntityPhysicalIndex_Type.__name__ = "Gauge32"
_HwSpuEntityPhysicalIndex_Object = MibTableColumn
hwSpuEntityPhysicalIndex = _HwSpuEntityPhysicalIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1, 1, 2),
    _HwSpuEntityPhysicalIndex_Type()
)
hwSpuEntityPhysicalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuEntityPhysicalIndex.setStatus("current")


class _HwSpuEntityLocation_Type(OctetString):
    """Custom type hwSpuEntityLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSpuEntityLocation_Type.__name__ = "OctetString"
_HwSpuEntityLocation_Object = MibTableColumn
hwSpuEntityLocation = _HwSpuEntityLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1, 1, 3),
    _HwSpuEntityLocation_Type()
)
hwSpuEntityLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpuEntityLocation.setStatus("current")


class _HwSpuEntityCpuUsage_Type(Gauge32):
    """Custom type hwSpuEntityCpuUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwSpuEntityCpuUsage_Type.__name__ = "Gauge32"
_HwSpuEntityCpuUsage_Object = MibTableColumn
hwSpuEntityCpuUsage = _HwSpuEntityCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1, 1, 4),
    _HwSpuEntityCpuUsage_Type()
)
hwSpuEntityCpuUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuEntityCpuUsage.setStatus("current")


class _HwSpuEntityCpuUsageThreshold_Type(Integer32):
    """Custom type hwSpuEntityCpuUsageThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwSpuEntityCpuUsageThreshold_Type.__name__ = "Integer32"
_HwSpuEntityCpuUsageThreshold_Object = MibTableColumn
hwSpuEntityCpuUsageThreshold = _HwSpuEntityCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1, 1, 5),
    _HwSpuEntityCpuUsageThreshold_Type()
)
hwSpuEntityCpuUsageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuEntityCpuUsageThreshold.setStatus("current")


class _HwSpuEntityMemoryUsage_Type(Gauge32):
    """Custom type hwSpuEntityMemoryUsage based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwSpuEntityMemoryUsage_Type.__name__ = "Gauge32"
_HwSpuEntityMemoryUsage_Object = MibTableColumn
hwSpuEntityMemoryUsage = _HwSpuEntityMemoryUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1, 1, 6),
    _HwSpuEntityMemoryUsage_Type()
)
hwSpuEntityMemoryUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuEntityMemoryUsage.setStatus("current")


class _HwSpuEntityMemoryUsageThreshold_Type(Gauge32):
    """Custom type hwSpuEntityMemoryUsageThreshold based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_HwSpuEntityMemoryUsageThreshold_Type.__name__ = "Gauge32"
_HwSpuEntityMemoryUsageThreshold_Object = MibTableColumn
hwSpuEntityMemoryUsageThreshold = _HwSpuEntityMemoryUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1, 1, 7),
    _HwSpuEntityMemoryUsageThreshold_Type()
)
hwSpuEntityMemoryUsageThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuEntityMemoryUsageThreshold.setStatus("current")
_HwSpuEntityTemperature_Type = Integer32
_HwSpuEntityTemperature_Object = MibTableColumn
hwSpuEntityTemperature = _HwSpuEntityTemperature_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1, 1, 8),
    _HwSpuEntityTemperature_Type()
)
hwSpuEntityTemperature.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpuEntityTemperature.setStatus("current")
_HwSpuEntityTemperatureThreshold_Type = Integer32
_HwSpuEntityTemperatureThreshold_Object = MibTableColumn
hwSpuEntityTemperatureThreshold = _HwSpuEntityTemperatureThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 7, 1, 1, 9),
    _HwSpuEntityTemperatureThreshold_Type()
)
hwSpuEntityTemperatureThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpuEntityTemperatureThreshold.setStatus("current")
_HwSpuEntityTraps_ObjectIdentity = ObjectIdentity
hwSpuEntityTraps = _HwSpuEntityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 8)
)
_HwSpuLpuOverLoadObject_ObjectIdentity = ObjectIdentity
hwSpuLpuOverLoadObject = _HwSpuLpuOverLoadObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9)
)
_HwSpuOverLoadInfoTable_Object = MibTable
hwSpuOverLoadInfoTable = _HwSpuOverLoadInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9, 1)
)
if mibBuilder.loadTexts:
    hwSpuOverLoadInfoTable.setStatus("current")
_HwSpuOverLoadInfoEntry_Object = MibTableRow
hwSpuOverLoadInfoEntry = _HwSpuOverLoadInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9, 1, 1)
)
hwSpuOverLoadInfoEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpuOverLoadInfoIndex"),
)
if mibBuilder.loadTexts:
    hwSpuOverLoadInfoEntry.setStatus("current")


class _HwSpuOverLoadInfoIndex_Type(Gauge32):
    """Custom type hwSpuOverLoadInfoIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSpuOverLoadInfoIndex_Type.__name__ = "Gauge32"
_HwSpuOverLoadInfoIndex_Object = MibTableColumn
hwSpuOverLoadInfoIndex = _HwSpuOverLoadInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9, 1, 1, 1),
    _HwSpuOverLoadInfoIndex_Type()
)
hwSpuOverLoadInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpuOverLoadInfoIndex.setStatus("current")
_HwSpuOverLoadPackages_Type = Counter64
_HwSpuOverLoadPackages_Object = MibTableColumn
hwSpuOverLoadPackages = _HwSpuOverLoadPackages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9, 1, 1, 2),
    _HwSpuOverLoadPackages_Type()
)
hwSpuOverLoadPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuOverLoadPackages.setStatus("current")
_HwSpuOverLoadBytes_Type = Counter64
_HwSpuOverLoadBytes_Object = MibTableColumn
hwSpuOverLoadBytes = _HwSpuOverLoadBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9, 1, 1, 3),
    _HwSpuOverLoadBytes_Type()
)
hwSpuOverLoadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuOverLoadBytes.setStatus("current")
_HwLpuOverLoadInfoTable_Object = MibTable
hwLpuOverLoadInfoTable = _HwLpuOverLoadInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9, 2)
)
if mibBuilder.loadTexts:
    hwLpuOverLoadInfoTable.setStatus("current")
_HwLpuOverLoadInfoEntry_Object = MibTableRow
hwLpuOverLoadInfoEntry = _HwLpuOverLoadInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9, 2, 1)
)
hwLpuOverLoadInfoEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwLpuOverLoadInfoIndex"),
)
if mibBuilder.loadTexts:
    hwLpuOverLoadInfoEntry.setStatus("current")


class _HwLpuOverLoadInfoIndex_Type(Gauge32):
    """Custom type hwLpuOverLoadInfoIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwLpuOverLoadInfoIndex_Type.__name__ = "Gauge32"
_HwLpuOverLoadInfoIndex_Object = MibTableColumn
hwLpuOverLoadInfoIndex = _HwLpuOverLoadInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9, 2, 1, 1),
    _HwLpuOverLoadInfoIndex_Type()
)
hwLpuOverLoadInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLpuOverLoadInfoIndex.setStatus("current")
_HwLpuOverLoadPackages_Type = Counter32
_HwLpuOverLoadPackages_Object = MibTableColumn
hwLpuOverLoadPackages = _HwLpuOverLoadPackages_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9, 2, 1, 2),
    _HwLpuOverLoadPackages_Type()
)
hwLpuOverLoadPackages.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLpuOverLoadPackages.setStatus("current")
_HwLpuOverLoadBytes_Type = Counter64
_HwLpuOverLoadBytes_Object = MibTableColumn
hwLpuOverLoadBytes = _HwLpuOverLoadBytes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 9, 2, 1, 3),
    _HwLpuOverLoadBytes_Type()
)
hwLpuOverLoadBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLpuOverLoadBytes.setStatus("current")
_HwSpuLpuOverLoadTrap_ObjectIdentity = ObjectIdentity
hwSpuLpuOverLoadTrap = _HwSpuLpuOverLoadTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 10)
)
_HwSpuFlowOverLoadObject_ObjectIdentity = ObjectIdentity
hwSpuFlowOverLoadObject = _HwSpuFlowOverLoadObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 11)
)
_HwSpuFlowOverLoadTable_Object = MibTable
hwSpuFlowOverLoadTable = _HwSpuFlowOverLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 11, 1)
)
if mibBuilder.loadTexts:
    hwSpuFlowOverLoadTable.setStatus("current")
_HwSpuFlowOverLoadEntry_Object = MibTableRow
hwSpuFlowOverLoadEntry = _HwSpuFlowOverLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 11, 1, 1)
)
hwSpuFlowOverLoadEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpuFlowOverLoadCpuNumber"),
)
if mibBuilder.loadTexts:
    hwSpuFlowOverLoadEntry.setStatus("current")


class _HwSpuFlowOverLoadCpuNumber_Type(Gauge32):
    """Custom type hwSpuFlowOverLoadCpuNumber based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_HwSpuFlowOverLoadCpuNumber_Type.__name__ = "Gauge32"
_HwSpuFlowOverLoadCpuNumber_Object = MibTableColumn
hwSpuFlowOverLoadCpuNumber = _HwSpuFlowOverLoadCpuNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 11, 1, 1, 1),
    _HwSpuFlowOverLoadCpuNumber_Type()
)
hwSpuFlowOverLoadCpuNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpuFlowOverLoadCpuNumber.setStatus("current")


class _HwSpuFlowOverLoadPackets_Type(OctetString):
    """Custom type hwSpuFlowOverLoadPackets based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_HwSpuFlowOverLoadPackets_Type.__name__ = "OctetString"
_HwSpuFlowOverLoadPackets_Object = MibTableColumn
hwSpuFlowOverLoadPackets = _HwSpuFlowOverLoadPackets_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 11, 1, 1, 2),
    _HwSpuFlowOverLoadPackets_Type()
)
hwSpuFlowOverLoadPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuFlowOverLoadPackets.setStatus("current")


class _HwSpuFlowOverLoadLocation_Type(OctetString):
    """Custom type hwSpuFlowOverLoadLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSpuFlowOverLoadLocation_Type.__name__ = "OctetString"
_HwSpuFlowOverLoadLocation_Object = MibTableColumn
hwSpuFlowOverLoadLocation = _HwSpuFlowOverLoadLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 11, 1, 1, 3),
    _HwSpuFlowOverLoadLocation_Type()
)
hwSpuFlowOverLoadLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuFlowOverLoadLocation.setStatus("current")
_HwSpuFlowOverLoadTraps_ObjectIdentity = ObjectIdentity
hwSpuFlowOverLoadTraps = _HwSpuFlowOverLoadTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 12)
)
_HwHashModeVerifyTraps_ObjectIdentity = ObjectIdentity
hwHashModeVerifyTraps = _HwHashModeVerifyTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 13)
)
_HwServiceObject_ObjectIdentity = ObjectIdentity
hwServiceObject = _HwServiceObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2)
)
_HwServiceBasicObject_ObjectIdentity = ObjectIdentity
hwServiceBasicObject = _HwServiceBasicObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1)
)
_HwResourceUsageTable_Object = MibTable
hwResourceUsageTable = _HwResourceUsageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 1)
)
if mibBuilder.loadTexts:
    hwResourceUsageTable.setStatus("current")
_HwResourceUsageEntry_Object = MibTableRow
hwResourceUsageEntry = _HwResourceUsageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 1, 1)
)
hwResourceUsageEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwResourceUsageIndex"),
)
if mibBuilder.loadTexts:
    hwResourceUsageEntry.setStatus("current")


class _HwResourceUsageIndex_Type(Gauge32):
    """Custom type hwResourceUsageIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwResourceUsageIndex_Type.__name__ = "Gauge32"
_HwResourceUsageIndex_Object = MibTableColumn
hwResourceUsageIndex = _HwResourceUsageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 1, 1, 1),
    _HwResourceUsageIndex_Type()
)
hwResourceUsageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwResourceUsageIndex.setStatus("current")


class _HwResourceLocation_Type(OctetString):
    """Custom type hwResourceLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwResourceLocation_Type.__name__ = "OctetString"
_HwResourceLocation_Object = MibTableColumn
hwResourceLocation = _HwResourceLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 1, 1, 2),
    _HwResourceLocation_Type()
)
hwResourceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwResourceLocation.setStatus("current")


class _HwSAResourceType_Type(Integer32):
    """Custom type hwSAResourceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
              22)
        )
    )
    namedValues = NamedValues(
        *(("acts", 1),
          ("ip", 2),
          ("spammerip", 3),
          ("spammeracts", 4),
          ("wormip", 5),
          ("wormvip", 6),
          ("botnetip", 7),
          ("botnetvip", 8),
          ("ddoscleanip", 9),
          ("ddostopnip", 10),
          ("voipsignal", 11),
          ("voipmedia", 12),
          ("urlacts", 13),
          ("urlglbcls", 14),
          ("fup", 15),
          ("ocs", 16),
          ("greennet", 17),
          ("smartnet", 18),
          ("smartbrowse", 19),
          ("ipush", 20),
          ("nets", 21),
          ("gg", 22))
    )


_HwSAResourceType_Type.__name__ = "Integer32"
_HwSAResourceType_Object = MibTableColumn
hwSAResourceType = _HwSAResourceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 1, 1, 3),
    _HwSAResourceType_Type()
)
hwSAResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSAResourceType.setStatus("current")
_HwResourceCapacity_Type = Integer32
_HwResourceCapacity_Object = MibTableColumn
hwResourceCapacity = _HwResourceCapacity_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 1, 1, 4),
    _HwResourceCapacity_Type()
)
hwResourceCapacity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwResourceCapacity.setStatus("current")
_HwResourceUsage_Type = Integer32
_HwResourceUsage_Object = MibTableColumn
hwResourceUsage = _HwResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 1, 1, 5),
    _HwResourceUsage_Type()
)
hwResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwResourceUsage.setStatus("current")
_HwResourceLeft_Type = Integer32
_HwResourceLeft_Object = MibTableColumn
hwResourceLeft = _HwResourceLeft_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 1, 1, 6),
    _HwResourceLeft_Type()
)
hwResourceLeft.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwResourceLeft.setStatus("current")
_HwSACbbFileTable_Object = MibTable
hwSACbbFileTable = _HwSACbbFileTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 2)
)
if mibBuilder.loadTexts:
    hwSACbbFileTable.setStatus("current")
_HwSACbbFileEntry_Object = MibTableRow
hwSACbbFileEntry = _HwSACbbFileEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 2, 1)
)
hwSACbbFileEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSACbbEntryIndex"),
)
if mibBuilder.loadTexts:
    hwSACbbFileEntry.setStatus("current")


class _HwSACbbEntryIndex_Type(Gauge32):
    """Custom type hwSACbbEntryIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSACbbEntryIndex_Type.__name__ = "Gauge32"
_HwSACbbEntryIndex_Object = MibTableColumn
hwSACbbEntryIndex = _HwSACbbEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 2, 1, 1),
    _HwSACbbEntryIndex_Type()
)
hwSACbbEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSACbbEntryIndex.setStatus("current")


class _HwSACbbLocation_Type(OctetString):
    """Custom type hwSACbbLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSACbbLocation_Type.__name__ = "OctetString"
_HwSACbbLocation_Object = MibTableColumn
hwSACbbLocation = _HwSACbbLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 2, 1, 2),
    _HwSACbbLocation_Type()
)
hwSACbbLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSACbbLocation.setStatus("current")


class _HwSACbbVersion_Type(Gauge32):
    """Custom type hwSACbbVersion based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSACbbVersion_Type.__name__ = "Gauge32"
_HwSACbbVersion_Object = MibTableColumn
hwSACbbVersion = _HwSACbbVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 2, 1, 3),
    _HwSACbbVersion_Type()
)
hwSACbbVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSACbbVersion.setStatus("current")
_HwBWListTable_Object = MibTable
hwBWListTable = _HwBWListTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 3)
)
if mibBuilder.loadTexts:
    hwBWListTable.setStatus("current")
_HwBWListEntry_Object = MibTableRow
hwBWListEntry = _HwBWListEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 3, 1)
)
hwBWListEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwBWListEntryIndex"),
)
if mibBuilder.loadTexts:
    hwBWListEntry.setStatus("current")


class _HwBWListEntryIndex_Type(Gauge32):
    """Custom type hwBWListEntryIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwBWListEntryIndex_Type.__name__ = "Gauge32"
_HwBWListEntryIndex_Object = MibTableColumn
hwBWListEntryIndex = _HwBWListEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 3, 1, 1),
    _HwBWListEntryIndex_Type()
)
hwBWListEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBWListEntryIndex.setStatus("current")


class _HwBWListType_Type(Integer32):
    """Custom type hwBWListType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("spammerwhitelist", 0),
          ("spammerblacklist", 1),
          ("spammerserveriplist", 2),
          ("spammeremailaddlist", 3),
          ("voiptelblacklist", 4),
          ("voipipblacklist", 5),
          ("voipurlblacklist", 6))
    )


_HwBWListType_Type.__name__ = "Integer32"
_HwBWListType_Object = MibTableColumn
hwBWListType = _HwBWListType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 3, 1, 2),
    _HwBWListType_Type()
)
hwBWListType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwBWListType.setStatus("current")


class _HwBWListLocation_Type(OctetString):
    """Custom type hwBWListLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwBWListLocation_Type.__name__ = "OctetString"
_HwBWListLocation_Object = MibTableColumn
hwBWListLocation = _HwBWListLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 3, 1, 3),
    _HwBWListLocation_Type()
)
hwBWListLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBWListLocation.setStatus("current")


class _HwBWListVersion_Type(Gauge32):
    """Custom type hwBWListVersion based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwBWListVersion_Type.__name__ = "Gauge32"
_HwBWListVersion_Object = MibTableColumn
hwBWListVersion = _HwBWListVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 3, 1, 4),
    _HwBWListVersion_Type()
)
hwBWListVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBWListVersion.setStatus("current")
_HwSpsSasLinkTable_Object = MibTable
hwSpsSasLinkTable = _HwSpsSasLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 4)
)
if mibBuilder.loadTexts:
    hwSpsSasLinkTable.setStatus("current")
_HwSpsSasLinkEntry_Object = MibTableRow
hwSpsSasLinkEntry = _HwSpsSasLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 4, 1)
)
hwSpsSasLinkEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkIndex"),
)
if mibBuilder.loadTexts:
    hwSpsSasLinkEntry.setStatus("current")


class _HwSpsSasLinkIndex_Type(Gauge32):
    """Custom type hwSpsSasLinkIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSpsSasLinkIndex_Type.__name__ = "Gauge32"
_HwSpsSasLinkIndex_Object = MibTableColumn
hwSpsSasLinkIndex = _HwSpsSasLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 4, 1, 1),
    _HwSpsSasLinkIndex_Type()
)
hwSpsSasLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpsSasLinkIndex.setStatus("current")


class _HwSpsSasLinkSpsLocation_Type(OctetString):
    """Custom type hwSpsSasLinkSpsLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSpsSasLinkSpsLocation_Type.__name__ = "OctetString"
_HwSpsSasLinkSpsLocation_Object = MibTableColumn
hwSpsSasLinkSpsLocation = _HwSpsSasLinkSpsLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 4, 1, 2),
    _HwSpsSasLinkSpsLocation_Type()
)
hwSpsSasLinkSpsLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsSasLinkSpsLocation.setStatus("current")


class _HwSpsSasLinkSasLocation_Type(OctetString):
    """Custom type hwSpsSasLinkSasLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSpsSasLinkSasLocation_Type.__name__ = "OctetString"
_HwSpsSasLinkSasLocation_Object = MibTableColumn
hwSpsSasLinkSasLocation = _HwSpsSasLinkSasLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 4, 1, 3),
    _HwSpsSasLinkSasLocation_Type()
)
hwSpsSasLinkSasLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsSasLinkSasLocation.setStatus("current")
_HwSpsSasLinkSpsIP_Type = IpAddress
_HwSpsSasLinkSpsIP_Object = MibTableColumn
hwSpsSasLinkSpsIP = _HwSpsSasLinkSpsIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 4, 1, 4),
    _HwSpsSasLinkSpsIP_Type()
)
hwSpsSasLinkSpsIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpsSasLinkSpsIP.setStatus("current")
_HwSpsSasLinkSasIP_Type = IpAddress
_HwSpsSasLinkSasIP_Object = MibTableColumn
hwSpsSasLinkSasIP = _HwSpsSasLinkSasIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 4, 1, 5),
    _HwSpsSasLinkSasIP_Type()
)
hwSpsSasLinkSasIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpsSasLinkSasIP.setStatus("current")


class _HwSpsSasLinkStatus_Type(Integer32):
    """Custom type hwSpsSasLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_HwSpsSasLinkStatus_Type.__name__ = "Integer32"
_HwSpsSasLinkStatus_Object = MibTableColumn
hwSpsSasLinkStatus = _HwSpsSasLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 4, 1, 6),
    _HwSpsSasLinkStatus_Type()
)
hwSpsSasLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpsSasLinkStatus.setStatus("current")
_HwSpuCompLinkTable_Object = MibTable
hwSpuCompLinkTable = _HwSpuCompLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5)
)
if mibBuilder.loadTexts:
    hwSpuCompLinkTable.setStatus("current")
_HwSpuCompLinkEntry_Object = MibTableRow
hwSpuCompLinkEntry = _HwSpuCompLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1)
)
hwSpuCompLinkEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkIndex"),
)
if mibBuilder.loadTexts:
    hwSpuCompLinkEntry.setStatus("current")


class _HwSpuCompLinkIndex_Type(Gauge32):
    """Custom type hwSpuCompLinkIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSpuCompLinkIndex_Type.__name__ = "Gauge32"
_HwSpuCompLinkIndex_Object = MibTableColumn
hwSpuCompLinkIndex = _HwSpuCompLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 1),
    _HwSpuCompLinkIndex_Type()
)
hwSpuCompLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpuCompLinkIndex.setStatus("current")


class _HwSpuCompLinkSysLocation_Type(OctetString):
    """Custom type hwSpuCompLinkSysLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSpuCompLinkSysLocation_Type.__name__ = "OctetString"
_HwSpuCompLinkSysLocation_Object = MibTableColumn
hwSpuCompLinkSysLocation = _HwSpuCompLinkSysLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 2),
    _HwSpuCompLinkSysLocation_Type()
)
hwSpuCompLinkSysLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuCompLinkSysLocation.setStatus("current")


class _HwSpuCompLinkComponentType_Type(Integer32):
    """Custom type hwSpuCompLinkComponentType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
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
        *(("dataanalysisserver", 1),
          ("policyserver", 2),
          ("managementserver", 3),
          ("serviceprobesystem", 4),
          ("serviceanalysesystem", 5),
          ("radiusproxy", 6),
          ("updateserver", 7),
          ("urlhealthcenter", 8),
          ("onlinechargingsystem", 9),
          ("policyandchargingrulesfunction", 10),
          ("quotamanagementserver", 11))
    )


_HwSpuCompLinkComponentType_Type.__name__ = "Integer32"
_HwSpuCompLinkComponentType_Object = MibTableColumn
hwSpuCompLinkComponentType = _HwSpuCompLinkComponentType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 3),
    _HwSpuCompLinkComponentType_Type()
)
hwSpuCompLinkComponentType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuCompLinkComponentType.setStatus("current")
_HwSpuCompLinkCurrentDestIP_Type = IpAddress
_HwSpuCompLinkCurrentDestIP_Object = MibTableColumn
hwSpuCompLinkCurrentDestIP = _HwSpuCompLinkCurrentDestIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 4),
    _HwSpuCompLinkCurrentDestIP_Type()
)
hwSpuCompLinkCurrentDestIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuCompLinkCurrentDestIP.setStatus("current")


class _HwSpuCompLinkCurrentDestPort_Type(Gauge32):
    """Custom type hwSpuCompLinkCurrentDestPort based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwSpuCompLinkCurrentDestPort_Type.__name__ = "Gauge32"
_HwSpuCompLinkCurrentDestPort_Object = MibTableColumn
hwSpuCompLinkCurrentDestPort = _HwSpuCompLinkCurrentDestPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 5),
    _HwSpuCompLinkCurrentDestPort_Type()
)
hwSpuCompLinkCurrentDestPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuCompLinkCurrentDestPort.setStatus("current")
_HwSpuCompLinkConnState_Type = Integer32
_HwSpuCompLinkConnState_Object = MibTableColumn
hwSpuCompLinkConnState = _HwSpuCompLinkConnState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 6),
    _HwSpuCompLinkConnState_Type()
)
hwSpuCompLinkConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuCompLinkConnState.setStatus("current")
_HwSpuCompLinkNumPacketsSent_Type = Counter32
_HwSpuCompLinkNumPacketsSent_Object = MibTableColumn
hwSpuCompLinkNumPacketsSent = _HwSpuCompLinkNumPacketsSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 7),
    _HwSpuCompLinkNumPacketsSent_Type()
)
hwSpuCompLinkNumPacketsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuCompLinkNumPacketsSent.setStatus("current")
_HwSpuCompLinkBytesSent_Type = Counter32
_HwSpuCompLinkBytesSent_Object = MibTableColumn
hwSpuCompLinkBytesSent = _HwSpuCompLinkBytesSent_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 8),
    _HwSpuCompLinkBytesSent_Type()
)
hwSpuCompLinkBytesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuCompLinkBytesSent.setStatus("current")
_HwSpuCompLinkNumPacketsRecv_Type = Counter32
_HwSpuCompLinkNumPacketsRecv_Object = MibTableColumn
hwSpuCompLinkNumPacketsRecv = _HwSpuCompLinkNumPacketsRecv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 9),
    _HwSpuCompLinkNumPacketsRecv_Type()
)
hwSpuCompLinkNumPacketsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuCompLinkNumPacketsRecv.setStatus("current")
_HwSpuCompLinkBytesRecv_Type = Counter32
_HwSpuCompLinkBytesRecv_Object = MibTableColumn
hwSpuCompLinkBytesRecv = _HwSpuCompLinkBytesRecv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 10),
    _HwSpuCompLinkBytesRecv_Type()
)
hwSpuCompLinkBytesRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuCompLinkBytesRecv.setStatus("current")
_HwSpuCompLinkNumErrPacketsRecv_Type = Counter32
_HwSpuCompLinkNumErrPacketsRecv_Object = MibTableColumn
hwSpuCompLinkNumErrPacketsRecv = _HwSpuCompLinkNumErrPacketsRecv_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 5, 1, 11),
    _HwSpuCompLinkNumErrPacketsRecv_Type()
)
hwSpuCompLinkNumErrPacketsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpuCompLinkNumErrPacketsRecv.setStatus("current")
_HwSAFdiConnectTable_Object = MibTable
hwSAFdiConnectTable = _HwSAFdiConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 6)
)
if mibBuilder.loadTexts:
    hwSAFdiConnectTable.setStatus("current")
_HwSAFdiConnectEntry_Object = MibTableRow
hwSAFdiConnectEntry = _HwSAFdiConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 6, 1)
)
hwSAFdiConnectEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSAFdiConnectIndex"),
)
if mibBuilder.loadTexts:
    hwSAFdiConnectEntry.setStatus("current")


class _HwSAFdiConnectIndex_Type(Gauge32):
    """Custom type hwSAFdiConnectIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSAFdiConnectIndex_Type.__name__ = "Gauge32"
_HwSAFdiConnectIndex_Object = MibTableColumn
hwSAFdiConnectIndex = _HwSAFdiConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 6, 1, 1),
    _HwSAFdiConnectIndex_Type()
)
hwSAFdiConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSAFdiConnectIndex.setStatus("current")


class _HwSAFdiConnectLocation_Type(OctetString):
    """Custom type hwSAFdiConnectLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSAFdiConnectLocation_Type.__name__ = "OctetString"
_HwSAFdiConnectLocation_Object = MibTableColumn
hwSAFdiConnectLocation = _HwSAFdiConnectLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 6, 1, 2),
    _HwSAFdiConnectLocation_Type()
)
hwSAFdiConnectLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSAFdiConnectLocation.setStatus("current")
_HwSysFdiInstanceID_Type = Counter32
_HwSysFdiInstanceID_Object = MibTableColumn
hwSysFdiInstanceID = _HwSysFdiInstanceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 6, 1, 3),
    _HwSysFdiInstanceID_Type()
)
hwSysFdiInstanceID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSysFdiInstanceID.setStatus("current")
_HwSysFdiDestMasterIP_Type = IpAddress
_HwSysFdiDestMasterIP_Object = MibTableColumn
hwSysFdiDestMasterIP = _HwSysFdiDestMasterIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 6, 1, 4),
    _HwSysFdiDestMasterIP_Type()
)
hwSysFdiDestMasterIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysFdiDestMasterIP.setStatus("current")
_HwSysFdiDestBackupIP_Type = IpAddress
_HwSysFdiDestBackupIP_Object = MibTableColumn
hwSysFdiDestBackupIP = _HwSysFdiDestBackupIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 6, 1, 5),
    _HwSysFdiDestBackupIP_Type()
)
hwSysFdiDestBackupIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSysFdiDestBackupIP.setStatus("current")
_HwSpsRadisInfoTable_Object = MibTable
hwSpsRadisInfoTable = _HwSpsRadisInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 7)
)
if mibBuilder.loadTexts:
    hwSpsRadisInfoTable.setStatus("current")
_HwSpsRadisInfoEntry_Object = MibTableRow
hwSpsRadisInfoEntry = _HwSpsRadisInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 7, 1)
)
hwSpsRadisInfoEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpsRadisInfoIndex"),
)
if mibBuilder.loadTexts:
    hwSpsRadisInfoEntry.setStatus("current")


class _HwSpsRadisInfoIndex_Type(Gauge32):
    """Custom type hwSpsRadisInfoIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_HwSpsRadisInfoIndex_Type.__name__ = "Gauge32"
_HwSpsRadisInfoIndex_Object = MibTableColumn
hwSpsRadisInfoIndex = _HwSpsRadisInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 7, 1, 1),
    _HwSpsRadisInfoIndex_Type()
)
hwSpsRadisInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpsRadisInfoIndex.setStatus("current")


class _HwSnifferInfoLocation_Type(OctetString):
    """Custom type hwSnifferInfoLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSnifferInfoLocation_Type.__name__ = "OctetString"
_HwSnifferInfoLocation_Object = MibTableColumn
hwSnifferInfoLocation = _HwSnifferInfoLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 7, 1, 2),
    _HwSnifferInfoLocation_Type()
)
hwSnifferInfoLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSnifferInfoLocation.setStatus("current")
_HwPacketSendCount_Type = Counter64
_HwPacketSendCount_Object = MibTableColumn
hwPacketSendCount = _HwPacketSendCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 7, 1, 3),
    _HwPacketSendCount_Type()
)
hwPacketSendCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPacketSendCount.setStatus("current")
_HwPacketErrCount_Type = Counter64
_HwPacketErrCount_Object = MibTableColumn
hwPacketErrCount = _HwPacketErrCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 7, 1, 4),
    _HwPacketErrCount_Type()
)
hwPacketErrCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPacketErrCount.setStatus("current")
_HwSnifferSrcIPAddress_Type = IpAddress
_HwSnifferSrcIPAddress_Object = MibTableColumn
hwSnifferSrcIPAddress = _HwSnifferSrcIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 7, 1, 5),
    _HwSnifferSrcIPAddress_Type()
)
hwSnifferSrcIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSnifferSrcIPAddress.setStatus("current")
_HwSnifferDstIPAddress_Type = IpAddress
_HwSnifferDstIPAddress_Object = MibTableColumn
hwSnifferDstIPAddress = _HwSnifferDstIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 7, 1, 6),
    _HwSnifferDstIPAddress_Type()
)
hwSnifferDstIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSnifferDstIPAddress.setStatus("current")


class _HwSnifferInfoState_Type(Integer32):
    """Custom type hwSnifferInfoState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("abnormal", 2))
    )


_HwSnifferInfoState_Type.__name__ = "Integer32"
_HwSnifferInfoState_Object = MibTableColumn
hwSnifferInfoState = _HwSnifferInfoState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 7, 1, 7),
    _HwSnifferInfoState_Type()
)
hwSnifferInfoState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSnifferInfoState.setStatus("current")
_HwSpsUcssLinkTable_Object = MibTable
hwSpsUcssLinkTable = _HwSpsUcssLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 8)
)
if mibBuilder.loadTexts:
    hwSpsUcssLinkTable.setStatus("current")
_HwSpsUcssLinkEntry_Object = MibTableRow
hwSpsUcssLinkEntry = _HwSpsUcssLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 8, 1)
)
hwSpsUcssLinkEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkIndex"),
)
if mibBuilder.loadTexts:
    hwSpsUcssLinkEntry.setStatus("current")
_HwSpsUcssLinkIndex_Type = Gauge32
_HwSpsUcssLinkIndex_Object = MibTableColumn
hwSpsUcssLinkIndex = _HwSpsUcssLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 8, 1, 1),
    _HwSpsUcssLinkIndex_Type()
)
hwSpsUcssLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpsUcssLinkIndex.setStatus("current")


class _HwSpsUcssLinkSpsLocation_Type(OctetString):
    """Custom type hwSpsUcssLinkSpsLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSpsUcssLinkSpsLocation_Type.__name__ = "OctetString"
_HwSpsUcssLinkSpsLocation_Object = MibTableColumn
hwSpsUcssLinkSpsLocation = _HwSpsUcssLinkSpsLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 8, 1, 2),
    _HwSpsUcssLinkSpsLocation_Type()
)
hwSpsUcssLinkSpsLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsUcssLinkSpsLocation.setStatus("current")
_HwSpsUcssLinkSpsIP_Type = IpAddress
_HwSpsUcssLinkSpsIP_Object = MibTableColumn
hwSpsUcssLinkSpsIP = _HwSpsUcssLinkSpsIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 8, 1, 3),
    _HwSpsUcssLinkSpsIP_Type()
)
hwSpsUcssLinkSpsIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsUcssLinkSpsIP.setStatus("current")
_HwSpsUcssLinkUcssIP_Type = IpAddress
_HwSpsUcssLinkUcssIP_Object = MibTableColumn
hwSpsUcssLinkUcssIP = _HwSpsUcssLinkUcssIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 8, 1, 4),
    _HwSpsUcssLinkUcssIP_Type()
)
hwSpsUcssLinkUcssIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsUcssLinkUcssIP.setStatus("current")
_HwSasMessageNumberTable_Object = MibTable
hwSasMessageNumberTable = _HwSasMessageNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9)
)
if mibBuilder.loadTexts:
    hwSasMessageNumberTable.setStatus("current")
_HwSasMessageNumberEntry_Object = MibTableRow
hwSasMessageNumberEntry = _HwSasMessageNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9, 1)
)
hwSasMessageNumberEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSasMessageNumIndex"),
)
if mibBuilder.loadTexts:
    hwSasMessageNumberEntry.setStatus("current")
_HwSasMessageNumIndex_Type = Gauge32
_HwSasMessageNumIndex_Object = MibTableColumn
hwSasMessageNumIndex = _HwSasMessageNumIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9, 1, 1),
    _HwSasMessageNumIndex_Type()
)
hwSasMessageNumIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSasMessageNumIndex.setStatus("current")


class _HwSasMessageLocation_Type(OctetString):
    """Custom type hwSasMessageLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSasMessageLocation_Type.__name__ = "OctetString"
_HwSasMessageLocation_Object = MibTableColumn
hwSasMessageLocation = _HwSasMessageLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9, 1, 2),
    _HwSasMessageLocation_Type()
)
hwSasMessageLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSasMessageLocation.setStatus("current")
_HwSasIPAddress_Type = IpAddress
_HwSasIPAddress_Object = MibTableColumn
hwSasIPAddress = _HwSasIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9, 1, 3),
    _HwSasIPAddress_Type()
)
hwSasIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasIPAddress.setStatus("current")


class _HwSasMessageType_Type(Integer32):
    """Custom type hwSasMessageType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unknow", 1),
          ("fixed", 2),
          ("g", 3),
          ("c", 4),
          ("wimax", 5),
          ("static", 6))
    )


_HwSasMessageType_Type.__name__ = "Integer32"
_HwSasMessageType_Object = MibTableColumn
hwSasMessageType = _HwSasMessageType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9, 1, 4),
    _HwSasMessageType_Type()
)
hwSasMessageType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasMessageType.setStatus("current")
_HwSasMessageIpOnLineNum_Type = Gauge32
_HwSasMessageIpOnLineNum_Object = MibTableColumn
hwSasMessageIpOnLineNum = _HwSasMessageIpOnLineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9, 1, 5),
    _HwSasMessageIpOnLineNum_Type()
)
hwSasMessageIpOnLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasMessageIpOnLineNum.setStatus("current")
_HwSasMessageIpOffLineNum_Type = Gauge32
_HwSasMessageIpOffLineNum_Object = MibTableColumn
hwSasMessageIpOffLineNum = _HwSasMessageIpOffLineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9, 1, 6),
    _HwSasMessageIpOffLineNum_Type()
)
hwSasMessageIpOffLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasMessageIpOffLineNum.setStatus("current")
_HwSasMessageAccountOnLineNum_Type = Gauge32
_HwSasMessageAccountOnLineNum_Object = MibTableColumn
hwSasMessageAccountOnLineNum = _HwSasMessageAccountOnLineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9, 1, 7),
    _HwSasMessageAccountOnLineNum_Type()
)
hwSasMessageAccountOnLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasMessageAccountOnLineNum.setStatus("current")
_HwSasMessageAccountOffLineNum_Type = Gauge32
_HwSasMessageAccountOffLineNum_Object = MibTableColumn
hwSasMessageAccountOffLineNum = _HwSasMessageAccountOffLineNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9, 1, 8),
    _HwSasMessageAccountOffLineNum_Type()
)
hwSasMessageAccountOffLineNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasMessageAccountOffLineNum.setStatus("current")
_HwSasMessageTotalNum_Type = Gauge32
_HwSasMessageTotalNum_Object = MibTableColumn
hwSasMessageTotalNum = _HwSasMessageTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 9, 1, 9),
    _HwSasMessageTotalNum_Type()
)
hwSasMessageTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasMessageTotalNum.setStatus("current")
_HwSpsMessageNumberTable_Object = MibTable
hwSpsMessageNumberTable = _HwSpsMessageNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 10)
)
if mibBuilder.loadTexts:
    hwSpsMessageNumberTable.setStatus("current")
_HwSpsMessageNumberEntry_Object = MibTableRow
hwSpsMessageNumberEntry = _HwSpsMessageNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 10, 1)
)
hwSpsMessageNumberEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpsMessageNumberIndex"),
)
if mibBuilder.loadTexts:
    hwSpsMessageNumberEntry.setStatus("current")
_HwSpsMessageNumberIndex_Type = Gauge32
_HwSpsMessageNumberIndex_Object = MibTableColumn
hwSpsMessageNumberIndex = _HwSpsMessageNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 10, 1, 1),
    _HwSpsMessageNumberIndex_Type()
)
hwSpsMessageNumberIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpsMessageNumberIndex.setStatus("current")


class _HwSpsMessageNumberLocation_Type(OctetString):
    """Custom type hwSpsMessageNumberLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSpsMessageNumberLocation_Type.__name__ = "OctetString"
_HwSpsMessageNumberLocation_Object = MibTableColumn
hwSpsMessageNumberLocation = _HwSpsMessageNumberLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 10, 1, 2),
    _HwSpsMessageNumberLocation_Type()
)
hwSpsMessageNumberLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsMessageNumberLocation.setStatus("current")
_HwSpsIPAddress_Type = IpAddress
_HwSpsIPAddress_Object = MibTableColumn
hwSpsIPAddress = _HwSpsIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 10, 1, 3),
    _HwSpsIPAddress_Type()
)
hwSpsIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpsIPAddress.setStatus("current")
_HwSpsNewFlowNumber_Type = Gauge32
_HwSpsNewFlowNumber_Object = MibTableColumn
hwSpsNewFlowNumber = _HwSpsNewFlowNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 10, 1, 4),
    _HwSpsNewFlowNumber_Type()
)
hwSpsNewFlowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpsNewFlowNumber.setStatus("current")
_HwSpsNewTempFlowNumber_Type = Gauge32
_HwSpsNewTempFlowNumber_Object = MibTableColumn
hwSpsNewTempFlowNumber = _HwSpsNewTempFlowNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 10, 1, 5),
    _HwSpsNewTempFlowNumber_Type()
)
hwSpsNewTempFlowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpsNewTempFlowNumber.setStatus("current")
_HwSpsDeleteFlowNumber_Type = Gauge32
_HwSpsDeleteFlowNumber_Object = MibTableColumn
hwSpsDeleteFlowNumber = _HwSpsDeleteFlowNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 10, 1, 6),
    _HwSpsDeleteFlowNumber_Type()
)
hwSpsDeleteFlowNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpsDeleteFlowNumber.setStatus("current")
_HwBackupGroupTable_Object = MibTable
hwBackupGroupTable = _HwBackupGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11)
)
if mibBuilder.loadTexts:
    hwBackupGroupTable.setStatus("current")
_HwBackupGroupEntry_Object = MibTableRow
hwBackupGroupEntry = _HwBackupGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1)
)
hwBackupGroupEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwBackupGroupIndex"),
)
if mibBuilder.loadTexts:
    hwBackupGroupEntry.setStatus("current")


class _HwBackupGroupIndex_Type(Gauge32):
    """Custom type hwBackupGroupIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwBackupGroupIndex_Type.__name__ = "Gauge32"
_HwBackupGroupIndex_Object = MibTableColumn
hwBackupGroupIndex = _HwBackupGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1, 1),
    _HwBackupGroupIndex_Type()
)
hwBackupGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwBackupGroupIndex.setStatus("current")


class _HwBackupGroupID_Type(Integer32):
    """Custom type hwBackupGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwBackupGroupID_Type.__name__ = "Integer32"
_HwBackupGroupID_Object = MibTableColumn
hwBackupGroupID = _HwBackupGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1, 2),
    _HwBackupGroupID_Type()
)
hwBackupGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBackupGroupID.setStatus("current")


class _HwLocalClusterNodeID_Type(Integer32):
    """Custom type hwLocalClusterNodeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwLocalClusterNodeID_Type.__name__ = "Integer32"
_HwLocalClusterNodeID_Object = MibTableColumn
hwLocalClusterNodeID = _HwLocalClusterNodeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1, 3),
    _HwLocalClusterNodeID_Type()
)
hwLocalClusterNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalClusterNodeID.setStatus("current")


class _HwPeerClusterNodeID_Type(Integer32):
    """Custom type hwPeerClusterNodeID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_HwPeerClusterNodeID_Type.__name__ = "Integer32"
_HwPeerClusterNodeID_Object = MibTableColumn
hwPeerClusterNodeID = _HwPeerClusterNodeID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1, 4),
    _HwPeerClusterNodeID_Type()
)
hwPeerClusterNodeID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPeerClusterNodeID.setStatus("current")
_HwLocalClusterNodeIPAddress_Type = IpAddress
_HwLocalClusterNodeIPAddress_Object = MibTableColumn
hwLocalClusterNodeIPAddress = _HwLocalClusterNodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1, 5),
    _HwLocalClusterNodeIPAddress_Type()
)
hwLocalClusterNodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwLocalClusterNodeIPAddress.setStatus("current")
_HwPeerClusterNodeIPAddress_Type = IpAddress
_HwPeerClusterNodeIPAddress_Object = MibTableColumn
hwPeerClusterNodeIPAddress = _HwPeerClusterNodeIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1, 6),
    _HwPeerClusterNodeIPAddress_Type()
)
hwPeerClusterNodeIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwPeerClusterNodeIPAddress.setStatus("current")


class _HwBackupGroupLocalSlot_Type(Integer32):
    """Custom type hwBackupGroupLocalSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwBackupGroupLocalSlot_Type.__name__ = "Integer32"
_HwBackupGroupLocalSlot_Object = MibTableColumn
hwBackupGroupLocalSlot = _HwBackupGroupLocalSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1, 7),
    _HwBackupGroupLocalSlot_Type()
)
hwBackupGroupLocalSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBackupGroupLocalSlot.setStatus("current")


class _HwBackupGroupPeerSlot_Type(Integer32):
    """Custom type hwBackupGroupPeerSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_HwBackupGroupPeerSlot_Type.__name__ = "Integer32"
_HwBackupGroupPeerSlot_Object = MibTableColumn
hwBackupGroupPeerSlot = _HwBackupGroupPeerSlot_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1, 8),
    _HwBackupGroupPeerSlot_Type()
)
hwBackupGroupPeerSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBackupGroupPeerSlot.setStatus("current")


class _HwBackupGroupLocalState_Type(Integer32):
    """Custom type hwBackupGroupLocalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("backup", 2))
    )


_HwBackupGroupLocalState_Type.__name__ = "Integer32"
_HwBackupGroupLocalState_Object = MibTableColumn
hwBackupGroupLocalState = _HwBackupGroupLocalState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1, 9),
    _HwBackupGroupLocalState_Type()
)
hwBackupGroupLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBackupGroupLocalState.setStatus("current")


class _HwBackupGroupPeerState_Type(Integer32):
    """Custom type hwBackupGroupPeerState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("backup", 2))
    )


_HwBackupGroupPeerState_Type.__name__ = "Integer32"
_HwBackupGroupPeerState_Object = MibTableColumn
hwBackupGroupPeerState = _HwBackupGroupPeerState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 11, 1, 10),
    _HwBackupGroupPeerState_Type()
)
hwBackupGroupPeerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwBackupGroupPeerState.setStatus("current")
_HwSpsRdasLinkTable_Object = MibTable
hwSpsRdasLinkTable = _HwSpsRdasLinkTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 12)
)
if mibBuilder.loadTexts:
    hwSpsRdasLinkTable.setStatus("current")
_HwSpsRdasLinkEntry_Object = MibTableRow
hwSpsRdasLinkEntry = _HwSpsRdasLinkEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 12, 1)
)
hwSpsRdasLinkEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpsRdasLinkIndex"),
)
if mibBuilder.loadTexts:
    hwSpsRdasLinkEntry.setStatus("current")
_HwSpsRdasLinkIndex_Type = Gauge32
_HwSpsRdasLinkIndex_Object = MibTableColumn
hwSpsRdasLinkIndex = _HwSpsRdasLinkIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 12, 1, 1),
    _HwSpsRdasLinkIndex_Type()
)
hwSpsRdasLinkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpsRdasLinkIndex.setStatus("current")
_HwSpsRdasLinkSpsLocation_Type = OctetString
_HwSpsRdasLinkSpsLocation_Object = MibTableColumn
hwSpsRdasLinkSpsLocation = _HwSpsRdasLinkSpsLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 12, 1, 2),
    _HwSpsRdasLinkSpsLocation_Type()
)
hwSpsRdasLinkSpsLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsRdasLinkSpsLocation.setStatus("current")
_HwSpsRdasLinkRdasIP_Type = IpAddress
_HwSpsRdasLinkRdasIP_Object = MibTableColumn
hwSpsRdasLinkRdasIP = _HwSpsRdasLinkRdasIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 12, 1, 3),
    _HwSpsRdasLinkRdasIP_Type()
)
hwSpsRdasLinkRdasIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsRdasLinkRdasIP.setStatus("current")
_HwSpsFragmentTable_Object = MibTable
hwSpsFragmentTable = _HwSpsFragmentTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 13)
)
if mibBuilder.loadTexts:
    hwSpsFragmentTable.setStatus("current")
_HwSpsFragmentEntry_Object = MibTableRow
hwSpsFragmentEntry = _HwSpsFragmentEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 13, 1)
)
hwSpsFragmentEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpsFragmentIndex"),
)
if mibBuilder.loadTexts:
    hwSpsFragmentEntry.setStatus("current")
_HwSpsFragmentIndex_Type = Gauge32
_HwSpsFragmentIndex_Object = MibTableColumn
hwSpsFragmentIndex = _HwSpsFragmentIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 13, 1, 1),
    _HwSpsFragmentIndex_Type()
)
hwSpsFragmentIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpsFragmentIndex.setStatus("current")
_HwSpsFragmentSpsLocation_Type = OctetString
_HwSpsFragmentSpsLocation_Object = MibTableColumn
hwSpsFragmentSpsLocation = _HwSpsFragmentSpsLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 13, 1, 2),
    _HwSpsFragmentSpsLocation_Type()
)
hwSpsFragmentSpsLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsFragmentSpsLocation.setStatus("current")
_HwSasRpdAccountMessageTable_Object = MibTable
hwSasRpdAccountMessageTable = _HwSasRpdAccountMessageTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 14)
)
if mibBuilder.loadTexts:
    hwSasRpdAccountMessageTable.setStatus("current")
_HwSasRpdAccountMessageEntry_Object = MibTableRow
hwSasRpdAccountMessageEntry = _HwSasRpdAccountMessageEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 14, 1)
)
hwSasRpdAccountMessageEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSasRpdAccountMessageIndex"),
)
if mibBuilder.loadTexts:
    hwSasRpdAccountMessageEntry.setStatus("current")
_HwSasRpdAccountMessageIndex_Type = Gauge32
_HwSasRpdAccountMessageIndex_Object = MibTableColumn
hwSasRpdAccountMessageIndex = _HwSasRpdAccountMessageIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 14, 1, 1),
    _HwSasRpdAccountMessageIndex_Type()
)
hwSasRpdAccountMessageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSasRpdAccountMessageIndex.setStatus("current")
_HwSasRpdAccountMessageLocation_Type = OctetString
_HwSasRpdAccountMessageLocation_Object = MibTableColumn
hwSasRpdAccountMessageLocation = _HwSasRpdAccountMessageLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 14, 1, 2),
    _HwSasRpdAccountMessageLocation_Type()
)
hwSasRpdAccountMessageLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSasRpdAccountMessageLocation.setStatus("current")
_HwSasRpdAccountMessageRpdIP_Type = IpAddress
_HwSasRpdAccountMessageRpdIP_Object = MibTableColumn
hwSasRpdAccountMessageRpdIP = _HwSasRpdAccountMessageRpdIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 14, 1, 4),
    _HwSasRpdAccountMessageRpdIP_Type()
)
hwSasRpdAccountMessageRpdIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSasRpdAccountMessageRpdIP.setStatus("current")
_HwNPLUS1BackupGroupTable_Object = MibTable
hwNPLUS1BackupGroupTable = _HwNPLUS1BackupGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 15)
)
if mibBuilder.loadTexts:
    hwNPLUS1BackupGroupTable.setStatus("current")
_HwNPLUS1BackupGroupEntry_Object = MibTableRow
hwNPLUS1BackupGroupEntry = _HwNPLUS1BackupGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 15, 1)
)
hwNPLUS1BackupGroupEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1BackupGroupIndex"),
)
if mibBuilder.loadTexts:
    hwNPLUS1BackupGroupEntry.setStatus("current")


class _HwNPLUS1BackupGroupIndex_Type(Gauge32):
    """Custom type hwNPLUS1BackupGroupIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwNPLUS1BackupGroupIndex_Type.__name__ = "Gauge32"
_HwNPLUS1BackupGroupIndex_Object = MibTableColumn
hwNPLUS1BackupGroupIndex = _HwNPLUS1BackupGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 15, 1, 1),
    _HwNPLUS1BackupGroupIndex_Type()
)
hwNPLUS1BackupGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwNPLUS1BackupGroupIndex.setStatus("current")


class _HwNPLUS1BackupGroupID_Type(Integer32):
    """Custom type hwNPLUS1BackupGroupID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwNPLUS1BackupGroupID_Type.__name__ = "Integer32"
_HwNPLUS1BackupGroupID_Object = MibTableColumn
hwNPLUS1BackupGroupID = _HwNPLUS1BackupGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 15, 1, 2),
    _HwNPLUS1BackupGroupID_Type()
)
hwNPLUS1BackupGroupID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNPLUS1BackupGroupID.setStatus("current")


class _HwNPLUS1BackupGroupBoardList_Type(OctetString):
    """Custom type hwNPLUS1BackupGroupBoardList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwNPLUS1BackupGroupBoardList_Type.__name__ = "OctetString"
_HwNPLUS1BackupGroupBoardList_Object = MibTableColumn
hwNPLUS1BackupGroupBoardList = _HwNPLUS1BackupGroupBoardList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 15, 1, 3),
    _HwNPLUS1BackupGroupBoardList_Type()
)
hwNPLUS1BackupGroupBoardList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNPLUS1BackupGroupBoardList.setStatus("current")
_HwNPLUS1BackupGroupBoardType_Type = OctetString
_HwNPLUS1BackupGroupBoardType_Object = MibTableColumn
hwNPLUS1BackupGroupBoardType = _HwNPLUS1BackupGroupBoardType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 15, 1, 4),
    _HwNPLUS1BackupGroupBoardType_Type()
)
hwNPLUS1BackupGroupBoardType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwNPLUS1BackupGroupBoardType.setStatus("current")


class _HwNPLUS1BackupIsEnable_Type(Integer32):
    """Custom type hwNPLUS1BackupIsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwNPLUS1BackupIsEnable_Type.__name__ = "Integer32"
_HwNPLUS1BackupIsEnable_Object = MibTableColumn
hwNPLUS1BackupIsEnable = _HwNPLUS1BackupIsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 15, 1, 5),
    _HwNPLUS1BackupIsEnable_Type()
)
hwNPLUS1BackupIsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwNPLUS1BackupIsEnable.setStatus("current")
_HwLocalBackupGroupStateTable_Object = MibTable
hwLocalBackupGroupStateTable = _HwLocalBackupGroupStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16)
)
if mibBuilder.loadTexts:
    hwLocalBackupGroupStateTable.setStatus("current")
_HwLocalBackupGroupStateEntry_Object = MibTableRow
hwLocalBackupGroupStateEntry = _HwLocalBackupGroupStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16, 1)
)
hwLocalBackupGroupStateEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwLocalBackupGroupStateCpuIndex"),
)
if mibBuilder.loadTexts:
    hwLocalBackupGroupStateEntry.setStatus("current")


class _HwLocalBackupGroupStateCpuIndex_Type(Integer32):
    """Custom type hwLocalBackupGroupStateCpuIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwLocalBackupGroupStateCpuIndex_Type.__name__ = "Integer32"
_HwLocalBackupGroupStateCpuIndex_Object = MibTableColumn
hwLocalBackupGroupStateCpuIndex = _HwLocalBackupGroupStateCpuIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16, 1, 1),
    _HwLocalBackupGroupStateCpuIndex_Type()
)
hwLocalBackupGroupStateCpuIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalBackupGroupStateCpuIndex.setStatus("current")
_HwLocalBackupGroupStateCpuLocation_Type = OctetString
_HwLocalBackupGroupStateCpuLocation_Object = MibTableColumn
hwLocalBackupGroupStateCpuLocation = _HwLocalBackupGroupStateCpuLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16, 1, 2),
    _HwLocalBackupGroupStateCpuLocation_Type()
)
hwLocalBackupGroupStateCpuLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalBackupGroupStateCpuLocation.setStatus("current")


class _HwLocalBackupGroupStateCpuType_Type(Integer32):
    """Custom type hwLocalBackupGroupStateCpuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sas", 1),
          ("sps", 2))
    )


_HwLocalBackupGroupStateCpuType_Type.__name__ = "Integer32"
_HwLocalBackupGroupStateCpuType_Object = MibTableColumn
hwLocalBackupGroupStateCpuType = _HwLocalBackupGroupStateCpuType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16, 1, 3),
    _HwLocalBackupGroupStateCpuType_Type()
)
hwLocalBackupGroupStateCpuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalBackupGroupStateCpuType.setStatus("current")


class _HwLocalBackupGroupStateIsEnable_Type(Integer32):
    """Custom type hwLocalBackupGroupStateIsEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_HwLocalBackupGroupStateIsEnable_Type.__name__ = "Integer32"
_HwLocalBackupGroupStateIsEnable_Object = MibTableColumn
hwLocalBackupGroupStateIsEnable = _HwLocalBackupGroupStateIsEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16, 1, 4),
    _HwLocalBackupGroupStateIsEnable_Type()
)
hwLocalBackupGroupStateIsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalBackupGroupStateIsEnable.setStatus("current")


class _HwLocalBackupGroupStateGroupId_Type(Integer32):
    """Custom type hwLocalBackupGroupStateGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_HwLocalBackupGroupStateGroupId_Type.__name__ = "Integer32"
_HwLocalBackupGroupStateGroupId_Object = MibTableColumn
hwLocalBackupGroupStateGroupId = _HwLocalBackupGroupStateGroupId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16, 1, 5),
    _HwLocalBackupGroupStateGroupId_Type()
)
hwLocalBackupGroupStateGroupId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalBackupGroupStateGroupId.setStatus("current")
_HwLocalBackupGroupStateSpuType_Type = OctetString
_HwLocalBackupGroupStateSpuType_Object = MibTableColumn
hwLocalBackupGroupStateSpuType = _HwLocalBackupGroupStateSpuType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16, 1, 6),
    _HwLocalBackupGroupStateSpuType_Type()
)
hwLocalBackupGroupStateSpuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalBackupGroupStateSpuType.setStatus("current")
_HwLocalBackupGroupStateCpuMode_Type = OctetString
_HwLocalBackupGroupStateCpuMode_Object = MibTableColumn
hwLocalBackupGroupStateCpuMode = _HwLocalBackupGroupStateCpuMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16, 1, 7),
    _HwLocalBackupGroupStateCpuMode_Type()
)
hwLocalBackupGroupStateCpuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalBackupGroupStateCpuMode.setStatus("current")


class _HwLocalBackupGroupIsStandby_Type(Integer32):
    """Custom type hwLocalBackupGroupIsStandby based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_HwLocalBackupGroupIsStandby_Type.__name__ = "Integer32"
_HwLocalBackupGroupIsStandby_Object = MibTableColumn
hwLocalBackupGroupIsStandby = _HwLocalBackupGroupIsStandby_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16, 1, 8),
    _HwLocalBackupGroupIsStandby_Type()
)
hwLocalBackupGroupIsStandby.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalBackupGroupIsStandby.setStatus("current")


class _HwLocalBackupSpuTypeInconsist_Type(Integer32):
    """Custom type hwLocalBackupSpuTypeInconsist based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_HwLocalBackupSpuTypeInconsist_Type.__name__ = "Integer32"
_HwLocalBackupSpuTypeInconsist_Object = MibTableColumn
hwLocalBackupSpuTypeInconsist = _HwLocalBackupSpuTypeInconsist_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 16, 1, 9),
    _HwLocalBackupSpuTypeInconsist_Type()
)
hwLocalBackupSpuTypeInconsist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwLocalBackupSpuTypeInconsist.setStatus("current")
_HwSpsLeastNumberTable_Object = MibTable
hwSpsLeastNumberTable = _HwSpsLeastNumberTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 17)
)
if mibBuilder.loadTexts:
    hwSpsLeastNumberTable.setStatus("current")
_HwSpsLeastNumberEntry_Object = MibTableRow
hwSpsLeastNumberEntry = _HwSpsLeastNumberEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 17, 1)
)
hwSpsLeastNumberEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpsCpuEntityIndex"),
)
if mibBuilder.loadTexts:
    hwSpsLeastNumberEntry.setStatus("current")


class _HwSpsLeastNumberCfg_Type(Integer32):
    """Custom type hwSpsLeastNumberCfg based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_HwSpsLeastNumberCfg_Type.__name__ = "Integer32"
_HwSpsLeastNumberCfg_Object = MibTableColumn
hwSpsLeastNumberCfg = _HwSpsLeastNumberCfg_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 17, 1, 1),
    _HwSpsLeastNumberCfg_Type()
)
hwSpsLeastNumberCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsLeastNumberCfg.setStatus("current")


class _HwSpsLeastNumberIndex_Type(Integer32):
    """Custom type hwSpsLeastNumberIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwSpsLeastNumberIndex_Type.__name__ = "Integer32"
_HwSpsLeastNumberIndex_Object = MibTableColumn
hwSpsLeastNumberIndex = _HwSpsLeastNumberIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 17, 1, 2),
    _HwSpsLeastNumberIndex_Type()
)
hwSpsLeastNumberIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsLeastNumberIndex.setStatus("current")
_HwSpsCpuStateTable_Object = MibTable
hwSpsCpuStateTable = _HwSpsCpuStateTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 18)
)
if mibBuilder.loadTexts:
    hwSpsCpuStateTable.setStatus("current")
_HwSpsCpuStateEntry_Object = MibTableRow
hwSpsCpuStateEntry = _HwSpsCpuStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 18, 1)
)
hwSpsCpuStateEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpsCpuEntityIndex"),
)
if mibBuilder.loadTexts:
    hwSpsCpuStateEntry.setStatus("current")


class _HwSpsEntityLocation_Type(OctetString):
    """Custom type hwSpsEntityLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSpsEntityLocation_Type.__name__ = "OctetString"
_HwSpsEntityLocation_Object = MibTableColumn
hwSpsEntityLocation = _HwSpsEntityLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 18, 1, 1),
    _HwSpsEntityLocation_Type()
)
hwSpsEntityLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsEntityLocation.setStatus("current")
_HwSpsAverageCpuUsage_Type = Integer32
_HwSpsAverageCpuUsage_Object = MibTableColumn
hwSpsAverageCpuUsage = _HwSpsAverageCpuUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 18, 1, 2),
    _HwSpsAverageCpuUsage_Type()
)
hwSpsAverageCpuUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsAverageCpuUsage.setStatus("current")
_HwSpsAverageCpuUsageThreshold_Type = Integer32
_HwSpsAverageCpuUsageThreshold_Object = MibTableColumn
hwSpsAverageCpuUsageThreshold = _HwSpsAverageCpuUsageThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 18, 1, 3),
    _HwSpsAverageCpuUsageThreshold_Type()
)
hwSpsAverageCpuUsageThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsAverageCpuUsageThreshold.setStatus("current")
_HwSpsQueueUsage_Type = Integer32
_HwSpsQueueUsage_Object = MibTableColumn
hwSpsQueueUsage = _HwSpsQueueUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 18, 1, 4),
    _HwSpsQueueUsage_Type()
)
hwSpsQueueUsage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsQueueUsage.setStatus("current")
_HwSpsOverloadThreshold_Type = Integer32
_HwSpsOverloadThreshold_Object = MibTableColumn
hwSpsOverloadThreshold = _HwSpsOverloadThreshold_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 18, 1, 5),
    _HwSpsOverloadThreshold_Type()
)
hwSpsOverloadThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsOverloadThreshold.setStatus("current")


class _HwSpsCpuEntityIndex_Type(Integer32):
    """Custom type hwSpsCpuEntityIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwSpsCpuEntityIndex_Type.__name__ = "Integer32"
_HwSpsCpuEntityIndex_Object = MibTableColumn
hwSpsCpuEntityIndex = _HwSpsCpuEntityIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 1, 18, 1, 6),
    _HwSpsCpuEntityIndex_Type()
)
hwSpsCpuEntityIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpsCpuEntityIndex.setStatus("current")
_HwServiceBasicTrap_ObjectIdentity = ObjectIdentity
hwServiceBasicTrap = _HwServiceBasicTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2)
)
_HwServiceWirelessObject_ObjectIdentity = ObjectIdentity
hwServiceWirelessObject = _HwServiceWirelessObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3)
)
_HwCGInfoTable_Object = MibTable
hwCGInfoTable = _HwCGInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 1)
)
if mibBuilder.loadTexts:
    hwCGInfoTable.setStatus("current")
_HwCGInfoEntry_Object = MibTableRow
hwCGInfoEntry = _HwCGInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 1, 1)
)
hwCGInfoEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwCGInfoIndex"),
)
if mibBuilder.loadTexts:
    hwCGInfoEntry.setStatus("current")


class _HwCGInfoIndex_Type(Gauge32):
    """Custom type hwCGInfoIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwCGInfoIndex_Type.__name__ = "Gauge32"
_HwCGInfoIndex_Object = MibTableColumn
hwCGInfoIndex = _HwCGInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 1, 1, 1),
    _HwCGInfoIndex_Type()
)
hwCGInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwCGInfoIndex.setStatus("current")


class _HwSASLocationConnectCG_Type(OctetString):
    """Custom type hwSASLocationConnectCG based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSASLocationConnectCG_Type.__name__ = "OctetString"
_HwSASLocationConnectCG_Object = MibTableColumn
hwSASLocationConnectCG = _HwSASLocationConnectCG_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 1, 1, 2),
    _HwSASLocationConnectCG_Type()
)
hwSASLocationConnectCG.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASLocationConnectCG.setStatus("current")
_HwCGIPAddress_Type = IpAddress
_HwCGIPAddress_Object = MibTableColumn
hwCGIPAddress = _HwCGIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 1, 1, 3),
    _HwCGIPAddress_Type()
)
hwCGIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCGIPAddress.setStatus("current")


class _HwCGPort_Type(Gauge32):
    """Custom type hwCGPort based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwCGPort_Type.__name__ = "Gauge32"
_HwCGPort_Object = MibTableColumn
hwCGPort = _HwCGPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 1, 1, 4),
    _HwCGPort_Type()
)
hwCGPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCGPort.setStatus("current")


class _HwCGGrade_Type(Gauge32):
    """Custom type hwCGGrade based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_HwCGGrade_Type.__name__ = "Gauge32"
_HwCGGrade_Object = MibTableColumn
hwCGGrade = _HwCGGrade_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 1, 1, 5),
    _HwCGGrade_Type()
)
hwCGGrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCGGrade.setStatus("current")


class _HwCGCdrCachePoolUsed_Type(Gauge32):
    """Custom type hwCGCdrCachePoolUsed based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_HwCGCdrCachePoolUsed_Type.__name__ = "Gauge32"
_HwCGCdrCachePoolUsed_Object = MibTableColumn
hwCGCdrCachePoolUsed = _HwCGCdrCachePoolUsed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 1, 1, 6),
    _HwCGCdrCachePoolUsed_Type()
)
hwCGCdrCachePoolUsed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCGCdrCachePoolUsed.setStatus("current")
_HwPCRFInfoTable_Object = MibTable
hwPCRFInfoTable = _HwPCRFInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 2)
)
if mibBuilder.loadTexts:
    hwPCRFInfoTable.setStatus("current")
_HwPCRFInfoEntry_Object = MibTableRow
hwPCRFInfoEntry = _HwPCRFInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 2, 1)
)
hwPCRFInfoEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwPCRFInfoIndex"),
)
if mibBuilder.loadTexts:
    hwPCRFInfoEntry.setStatus("current")


class _HwPCRFInfoIndex_Type(Gauge32):
    """Custom type hwPCRFInfoIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwPCRFInfoIndex_Type.__name__ = "Gauge32"
_HwPCRFInfoIndex_Object = MibTableColumn
hwPCRFInfoIndex = _HwPCRFInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 2, 1, 1),
    _HwPCRFInfoIndex_Type()
)
hwPCRFInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwPCRFInfoIndex.setStatus("current")


class _HwSASLocationConnectPCRF_Type(OctetString):
    """Custom type hwSASLocationConnectPCRF based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSASLocationConnectPCRF_Type.__name__ = "OctetString"
_HwSASLocationConnectPCRF_Object = MibTableColumn
hwSASLocationConnectPCRF = _HwSASLocationConnectPCRF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 2, 1, 2),
    _HwSASLocationConnectPCRF_Type()
)
hwSASLocationConnectPCRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASLocationConnectPCRF.setStatus("current")
_HwPCRFHostName_Type = OctetString
_HwPCRFHostName_Object = MibTableColumn
hwPCRFHostName = _HwPCRFHostName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 2, 1, 3),
    _HwPCRFHostName_Type()
)
hwPCRFHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPCRFHostName.setStatus("current")
_HwPCRFIPAddress_Type = IpAddress
_HwPCRFIPAddress_Object = MibTableColumn
hwPCRFIPAddress = _HwPCRFIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 2, 1, 4),
    _HwPCRFIPAddress_Type()
)
hwPCRFIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPCRFIPAddress.setStatus("current")


class _HwPCRFPort_Type(Gauge32):
    """Custom type hwPCRFPort based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwPCRFPort_Type.__name__ = "Gauge32"
_HwPCRFPort_Object = MibTableColumn
hwPCRFPort = _HwPCRFPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 2, 1, 5),
    _HwPCRFPort_Type()
)
hwPCRFPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwPCRFPort.setStatus("current")


class _HwSASNameConnectPCRF_Type(OctetString):
    """Custom type hwSASNameConnectPCRF based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSASNameConnectPCRF_Type.__name__ = "OctetString"
_HwSASNameConnectPCRF_Object = MibTableColumn
hwSASNameConnectPCRF = _HwSASNameConnectPCRF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 2, 1, 6),
    _HwSASNameConnectPCRF_Type()
)
hwSASNameConnectPCRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASNameConnectPCRF.setStatus("current")
_HwSASIPAddressConnectPCRF_Type = IpAddress
_HwSASIPAddressConnectPCRF_Object = MibTableColumn
hwSASIPAddressConnectPCRF = _HwSASIPAddressConnectPCRF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 2, 1, 7),
    _HwSASIPAddressConnectPCRF_Type()
)
hwSASIPAddressConnectPCRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASIPAddressConnectPCRF.setStatus("current")


class _HwSASPortConnectPCRF_Type(Gauge32):
    """Custom type hwSASPortConnectPCRF based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwSASPortConnectPCRF_Type.__name__ = "Gauge32"
_HwSASPortConnectPCRF_Object = MibTableColumn
hwSASPortConnectPCRF = _HwSASPortConnectPCRF_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 2, 1, 8),
    _HwSASPortConnectPCRF_Type()
)
hwSASPortConnectPCRF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASPortConnectPCRF.setStatus("current")
_HwOCSInfoTable_Object = MibTable
hwOCSInfoTable = _HwOCSInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 3)
)
if mibBuilder.loadTexts:
    hwOCSInfoTable.setStatus("current")
_HwOCSInfoEntry_Object = MibTableRow
hwOCSInfoEntry = _HwOCSInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 3, 1)
)
hwOCSInfoEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwOCSInfoIndex"),
)
if mibBuilder.loadTexts:
    hwOCSInfoEntry.setStatus("current")


class _HwOCSInfoIndex_Type(Gauge32):
    """Custom type hwOCSInfoIndex based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_HwOCSInfoIndex_Type.__name__ = "Gauge32"
_HwOCSInfoIndex_Object = MibTableColumn
hwOCSInfoIndex = _HwOCSInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 3, 1, 1),
    _HwOCSInfoIndex_Type()
)
hwOCSInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwOCSInfoIndex.setStatus("current")


class _HwSASLocationConnectOCS_Type(OctetString):
    """Custom type hwSASLocationConnectOCS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSASLocationConnectOCS_Type.__name__ = "OctetString"
_HwSASLocationConnectOCS_Object = MibTableColumn
hwSASLocationConnectOCS = _HwSASLocationConnectOCS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 3, 1, 2),
    _HwSASLocationConnectOCS_Type()
)
hwSASLocationConnectOCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASLocationConnectOCS.setStatus("current")


class _HwOCSHostName_Type(OctetString):
    """Custom type hwOCSHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwOCSHostName_Type.__name__ = "OctetString"
_HwOCSHostName_Object = MibTableColumn
hwOCSHostName = _HwOCSHostName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 3, 1, 3),
    _HwOCSHostName_Type()
)
hwOCSHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOCSHostName.setStatus("current")
_HwOCSIPAddress_Type = IpAddress
_HwOCSIPAddress_Object = MibTableColumn
hwOCSIPAddress = _HwOCSIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 3, 1, 4),
    _HwOCSIPAddress_Type()
)
hwOCSIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOCSIPAddress.setStatus("current")


class _HwOCSPort_Type(Gauge32):
    """Custom type hwOCSPort based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwOCSPort_Type.__name__ = "Gauge32"
_HwOCSPort_Object = MibTableColumn
hwOCSPort = _HwOCSPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 3, 1, 5),
    _HwOCSPort_Type()
)
hwOCSPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwOCSPort.setStatus("current")


class _HwSASNameConnectOCS_Type(OctetString):
    """Custom type hwSASNameConnectOCS based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSASNameConnectOCS_Type.__name__ = "OctetString"
_HwSASNameConnectOCS_Object = MibTableColumn
hwSASNameConnectOCS = _HwSASNameConnectOCS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 3, 1, 6),
    _HwSASNameConnectOCS_Type()
)
hwSASNameConnectOCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASNameConnectOCS.setStatus("current")
_HwSASIPAddressConnectOCS_Type = IpAddress
_HwSASIPAddressConnectOCS_Object = MibTableColumn
hwSASIPAddressConnectOCS = _HwSASIPAddressConnectOCS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 3, 1, 7),
    _HwSASIPAddressConnectOCS_Type()
)
hwSASIPAddressConnectOCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASIPAddressConnectOCS.setStatus("current")


class _HwSASPortConnectOCS_Type(Gauge32):
    """Custom type hwSASPortConnectOCS based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwSASPortConnectOCS_Type.__name__ = "Gauge32"
_HwSASPortConnectOCS_Object = MibTableColumn
hwSASPortConnectOCS = _HwSASPortConnectOCS_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 3, 1, 8),
    _HwSASPortConnectOCS_Type()
)
hwSASPortConnectOCS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASPortConnectOCS.setStatus("current")
_HwDRAInfoTable_Object = MibTable
hwDRAInfoTable = _HwDRAInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 4)
)
if mibBuilder.loadTexts:
    hwDRAInfoTable.setStatus("current")
_HwDRAInfoEntry_Object = MibTableRow
hwDRAInfoEntry = _HwDRAInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 4, 1)
)
hwDRAInfoEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwDRAInfoIndex"),
)
if mibBuilder.loadTexts:
    hwDRAInfoEntry.setStatus("current")
_HwDRAInfoIndex_Type = Gauge32
_HwDRAInfoIndex_Object = MibTableColumn
hwDRAInfoIndex = _HwDRAInfoIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 4, 1, 1),
    _HwDRAInfoIndex_Type()
)
hwDRAInfoIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwDRAInfoIndex.setStatus("current")


class _HwSASLocationConnectDRA_Type(OctetString):
    """Custom type hwSASLocationConnectDRA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSASLocationConnectDRA_Type.__name__ = "OctetString"
_HwSASLocationConnectDRA_Object = MibTableColumn
hwSASLocationConnectDRA = _HwSASLocationConnectDRA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 4, 1, 2),
    _HwSASLocationConnectDRA_Type()
)
hwSASLocationConnectDRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASLocationConnectDRA.setStatus("current")


class _HwDRAHostName_Type(OctetString):
    """Custom type hwDRAHostName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwDRAHostName_Type.__name__ = "OctetString"
_HwDRAHostName_Object = MibTableColumn
hwDRAHostName = _HwDRAHostName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 4, 1, 3),
    _HwDRAHostName_Type()
)
hwDRAHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDRAHostName.setStatus("current")
_HwDRAIPAddress_Type = IpAddress
_HwDRAIPAddress_Object = MibTableColumn
hwDRAIPAddress = _HwDRAIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 4, 1, 4),
    _HwDRAIPAddress_Type()
)
hwDRAIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDRAIPAddress.setStatus("current")


class _HwDRAPort_Type(Gauge32):
    """Custom type hwDRAPort based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwDRAPort_Type.__name__ = "Gauge32"
_HwDRAPort_Object = MibTableColumn
hwDRAPort = _HwDRAPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 4, 1, 5),
    _HwDRAPort_Type()
)
hwDRAPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwDRAPort.setStatus("current")


class _HwSASNameConnectDRA_Type(OctetString):
    """Custom type hwSASNameConnectDRA based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSASNameConnectDRA_Type.__name__ = "OctetString"
_HwSASNameConnectDRA_Object = MibTableColumn
hwSASNameConnectDRA = _HwSASNameConnectDRA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 4, 1, 6),
    _HwSASNameConnectDRA_Type()
)
hwSASNameConnectDRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASNameConnectDRA.setStatus("current")
_HwSASIPAddressConnectDRA_Type = IpAddress
_HwSASIPAddressConnectDRA_Object = MibTableColumn
hwSASIPAddressConnectDRA = _HwSASIPAddressConnectDRA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 4, 1, 7),
    _HwSASIPAddressConnectDRA_Type()
)
hwSASIPAddressConnectDRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASIPAddressConnectDRA.setStatus("current")


class _HwSASPortConnectDRA_Type(Gauge32):
    """Custom type hwSASPortConnectDRA based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwSASPortConnectDRA_Type.__name__ = "Gauge32"
_HwSASPortConnectDRA_Object = MibTableColumn
hwSASPortConnectDRA = _HwSASPortConnectDRA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 4, 1, 8),
    _HwSASPortConnectDRA_Type()
)
hwSASPortConnectDRA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSASPortConnectDRA.setStatus("current")
_HwSasGxPerformanceTable_Object = MibTable
hwSasGxPerformanceTable = _HwSasGxPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5)
)
if mibBuilder.loadTexts:
    hwSasGxPerformanceTable.setStatus("current")
_HwSasGxPerformanceEntry_Object = MibTableRow
hwSasGxPerformanceEntry = _HwSasGxPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1)
)
hwSasGxPerformanceEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSasGxPerformanceIndex"),
)
if mibBuilder.loadTexts:
    hwSasGxPerformanceEntry.setStatus("current")
_HwSasGxPerformanceIndex_Type = Gauge32
_HwSasGxPerformanceIndex_Object = MibTableColumn
hwSasGxPerformanceIndex = _HwSasGxPerformanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 1),
    _HwSasGxPerformanceIndex_Type()
)
hwSasGxPerformanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSasGxPerformanceIndex.setStatus("current")


class _HwSasGxPerformanceLocation_Type(OctetString):
    """Custom type hwSasGxPerformanceLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSasGxPerformanceLocation_Type.__name__ = "OctetString"
_HwSasGxPerformanceLocation_Object = MibTableColumn
hwSasGxPerformanceLocation = _HwSasGxPerformanceLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 2),
    _HwSasGxPerformanceLocation_Type()
)
hwSasGxPerformanceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxPerformanceLocation.setStatus("current")
_HwSasIPAddressForGxPerformance_Type = IpAddress
_HwSasIPAddressForGxPerformance_Object = MibTableColumn
hwSasIPAddressForGxPerformance = _HwSasIPAddressForGxPerformance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 3),
    _HwSasIPAddressForGxPerformance_Type()
)
hwSasIPAddressForGxPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasIPAddressForGxPerformance.setStatus("current")
_HwSasGxTotalSendNumber_Type = Gauge32
_HwSasGxTotalSendNumber_Object = MibTableColumn
hwSasGxTotalSendNumber = _HwSasGxTotalSendNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 4),
    _HwSasGxTotalSendNumber_Type()
)
hwSasGxTotalSendNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxTotalSendNumber.setStatus("current")
_HwSasGxTotalRecieveNumber_Type = Gauge32
_HwSasGxTotalRecieveNumber_Object = MibTableColumn
hwSasGxTotalRecieveNumber = _HwSasGxTotalRecieveNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 5),
    _HwSasGxTotalRecieveNumber_Type()
)
hwSasGxTotalRecieveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxTotalRecieveNumber.setStatus("current")
_HwSasGxCCRInitalNumber_Type = Gauge32
_HwSasGxCCRInitalNumber_Object = MibTableColumn
hwSasGxCCRInitalNumber = _HwSasGxCCRInitalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 6),
    _HwSasGxCCRInitalNumber_Type()
)
hwSasGxCCRInitalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxCCRInitalNumber.setStatus("current")
_HwSasGxCCAInitalNumber_Type = Gauge32
_HwSasGxCCAInitalNumber_Object = MibTableColumn
hwSasGxCCAInitalNumber = _HwSasGxCCAInitalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 7),
    _HwSasGxCCAInitalNumber_Type()
)
hwSasGxCCAInitalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxCCAInitalNumber.setStatus("current")
_HwSasGxCCRUpdateNumber_Type = Gauge32
_HwSasGxCCRUpdateNumber_Object = MibTableColumn
hwSasGxCCRUpdateNumber = _HwSasGxCCRUpdateNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 8),
    _HwSasGxCCRUpdateNumber_Type()
)
hwSasGxCCRUpdateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxCCRUpdateNumber.setStatus("current")
_HwSasGxCCAUpdateNumber_Type = Gauge32
_HwSasGxCCAUpdateNumber_Object = MibTableColumn
hwSasGxCCAUpdateNumber = _HwSasGxCCAUpdateNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 9),
    _HwSasGxCCAUpdateNumber_Type()
)
hwSasGxCCAUpdateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxCCAUpdateNumber.setStatus("current")
_HwSasGxCCRTerminateNumber_Type = Gauge32
_HwSasGxCCRTerminateNumber_Object = MibTableColumn
hwSasGxCCRTerminateNumber = _HwSasGxCCRTerminateNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 10),
    _HwSasGxCCRTerminateNumber_Type()
)
hwSasGxCCRTerminateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxCCRTerminateNumber.setStatus("current")
_HwSasGxCCATerminateNumber_Type = Gauge32
_HwSasGxCCATerminateNumber_Object = MibTableColumn
hwSasGxCCATerminateNumber = _HwSasGxCCATerminateNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 11),
    _HwSasGxCCATerminateNumber_Type()
)
hwSasGxCCATerminateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxCCATerminateNumber.setStatus("current")
_HwSasGxRARNumber_Type = Gauge32
_HwSasGxRARNumber_Object = MibTableColumn
hwSasGxRARNumber = _HwSasGxRARNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 12),
    _HwSasGxRARNumber_Type()
)
hwSasGxRARNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxRARNumber.setStatus("current")
_HwSasGxRAANumber_Type = Gauge32
_HwSasGxRAANumber_Object = MibTableColumn
hwSasGxRAANumber = _HwSasGxRAANumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 13),
    _HwSasGxRAANumber_Type()
)
hwSasGxRAANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxRAANumber.setStatus("current")
_HwSasGxASRNumber_Type = Gauge32
_HwSasGxASRNumber_Object = MibTableColumn
hwSasGxASRNumber = _HwSasGxASRNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 14),
    _HwSasGxASRNumber_Type()
)
hwSasGxASRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxASRNumber.setStatus("current")
_HwSasGxASANumber_Type = Gauge32
_HwSasGxASANumber_Object = MibTableColumn
hwSasGxASANumber = _HwSasGxASANumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 5, 1, 15),
    _HwSasGxASANumber_Type()
)
hwSasGxASANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxASANumber.setStatus("current")
_HwSasGxErrorTable_Object = MibTable
hwSasGxErrorTable = _HwSasGxErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 6)
)
if mibBuilder.loadTexts:
    hwSasGxErrorTable.setStatus("current")
_HwSasGxErrorEntry_Object = MibTableRow
hwSasGxErrorEntry = _HwSasGxErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 6, 1)
)
hwSasGxErrorEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSasGxErrorIndex"),
)
if mibBuilder.loadTexts:
    hwSasGxErrorEntry.setStatus("current")
_HwSasGxErrorIndex_Type = Gauge32
_HwSasGxErrorIndex_Object = MibTableColumn
hwSasGxErrorIndex = _HwSasGxErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 6, 1, 1),
    _HwSasGxErrorIndex_Type()
)
hwSasGxErrorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSasGxErrorIndex.setStatus("current")


class _HwSasGxErrorLocation_Type(OctetString):
    """Custom type hwSasGxErrorLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSasGxErrorLocation_Type.__name__ = "OctetString"
_HwSasGxErrorLocation_Object = MibTableColumn
hwSasGxErrorLocation = _HwSasGxErrorLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 6, 1, 2),
    _HwSasGxErrorLocation_Type()
)
hwSasGxErrorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxErrorLocation.setStatus("current")
_HwSasIPAddressForGxError_Type = IpAddress
_HwSasIPAddressForGxError_Object = MibTableColumn
hwSasIPAddressForGxError = _HwSasIPAddressForGxError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 6, 1, 3),
    _HwSasIPAddressForGxError_Type()
)
hwSasIPAddressForGxError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasIPAddressForGxError.setStatus("current")
_HwGxCommunitionInterruptedTimes_Type = Gauge32
_HwGxCommunitionInterruptedTimes_Object = MibTableColumn
hwGxCommunitionInterruptedTimes = _HwGxCommunitionInterruptedTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 6, 1, 4),
    _HwGxCommunitionInterruptedTimes_Type()
)
hwGxCommunitionInterruptedTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGxCommunitionInterruptedTimes.setStatus("current")
_HwSasGxCCRInitalRetransmissions_Type = Gauge32
_HwSasGxCCRInitalRetransmissions_Object = MibTableColumn
hwSasGxCCRInitalRetransmissions = _HwSasGxCCRInitalRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 6, 1, 5),
    _HwSasGxCCRInitalRetransmissions_Type()
)
hwSasGxCCRInitalRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxCCRInitalRetransmissions.setStatus("current")
_HwSasGxCCRUpdateRetransmissions_Type = Gauge32
_HwSasGxCCRUpdateRetransmissions_Object = MibTableColumn
hwSasGxCCRUpdateRetransmissions = _HwSasGxCCRUpdateRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 6, 1, 6),
    _HwSasGxCCRUpdateRetransmissions_Type()
)
hwSasGxCCRUpdateRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxCCRUpdateRetransmissions.setStatus("current")
_HwSasGxCCRTerminateRetransmissions_Type = Gauge32
_HwSasGxCCRTerminateRetransmissions_Object = MibTableColumn
hwSasGxCCRTerminateRetransmissions = _HwSasGxCCRTerminateRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 6, 1, 7),
    _HwSasGxCCRTerminateRetransmissions_Type()
)
hwSasGxCCRTerminateRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGxCCRTerminateRetransmissions.setStatus("current")
_HwSasGyPerformanceTable_Object = MibTable
hwSasGyPerformanceTable = _HwSasGyPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7)
)
if mibBuilder.loadTexts:
    hwSasGyPerformanceTable.setStatus("current")
_HwSasGyPerformanceEntry_Object = MibTableRow
hwSasGyPerformanceEntry = _HwSasGyPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1)
)
hwSasGyPerformanceEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSasGyPerformanceIndex"),
)
if mibBuilder.loadTexts:
    hwSasGyPerformanceEntry.setStatus("current")
_HwSasGyPerformanceIndex_Type = Gauge32
_HwSasGyPerformanceIndex_Object = MibTableColumn
hwSasGyPerformanceIndex = _HwSasGyPerformanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 1),
    _HwSasGyPerformanceIndex_Type()
)
hwSasGyPerformanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSasGyPerformanceIndex.setStatus("current")


class _HwSasGyPerformanceLocation_Type(OctetString):
    """Custom type hwSasGyPerformanceLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSasGyPerformanceLocation_Type.__name__ = "OctetString"
_HwSasGyPerformanceLocation_Object = MibTableColumn
hwSasGyPerformanceLocation = _HwSasGyPerformanceLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 2),
    _HwSasGyPerformanceLocation_Type()
)
hwSasGyPerformanceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyPerformanceLocation.setStatus("current")
_HwSasIPAddressForGyPerformance_Type = IpAddress
_HwSasIPAddressForGyPerformance_Object = MibTableColumn
hwSasIPAddressForGyPerformance = _HwSasIPAddressForGyPerformance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 3),
    _HwSasIPAddressForGyPerformance_Type()
)
hwSasIPAddressForGyPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasIPAddressForGyPerformance.setStatus("current")
_HwSasGyTotalSendNumber_Type = Gauge32
_HwSasGyTotalSendNumber_Object = MibTableColumn
hwSasGyTotalSendNumber = _HwSasGyTotalSendNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 4),
    _HwSasGyTotalSendNumber_Type()
)
hwSasGyTotalSendNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyTotalSendNumber.setStatus("current")
_HwSasGyTotalRecieveNumber_Type = Gauge32
_HwSasGyTotalRecieveNumber_Object = MibTableColumn
hwSasGyTotalRecieveNumber = _HwSasGyTotalRecieveNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 5),
    _HwSasGyTotalRecieveNumber_Type()
)
hwSasGyTotalRecieveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyTotalRecieveNumber.setStatus("current")
_HwSasGyCCRInitalNumber_Type = Gauge32
_HwSasGyCCRInitalNumber_Object = MibTableColumn
hwSasGyCCRInitalNumber = _HwSasGyCCRInitalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 6),
    _HwSasGyCCRInitalNumber_Type()
)
hwSasGyCCRInitalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyCCRInitalNumber.setStatus("current")
_HwSasGyCCAInitalNumber_Type = Gauge32
_HwSasGyCCAInitalNumber_Object = MibTableColumn
hwSasGyCCAInitalNumber = _HwSasGyCCAInitalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 7),
    _HwSasGyCCAInitalNumber_Type()
)
hwSasGyCCAInitalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyCCAInitalNumber.setStatus("current")
_HwSasGyCCRUpdateNumber_Type = Gauge32
_HwSasGyCCRUpdateNumber_Object = MibTableColumn
hwSasGyCCRUpdateNumber = _HwSasGyCCRUpdateNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 8),
    _HwSasGyCCRUpdateNumber_Type()
)
hwSasGyCCRUpdateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyCCRUpdateNumber.setStatus("current")
_HwSasGyCCAUpdateNumber_Type = Gauge32
_HwSasGyCCAUpdateNumber_Object = MibTableColumn
hwSasGyCCAUpdateNumber = _HwSasGyCCAUpdateNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 9),
    _HwSasGyCCAUpdateNumber_Type()
)
hwSasGyCCAUpdateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyCCAUpdateNumber.setStatus("current")
_HwSasGyCCRTerminateNumber_Type = Gauge32
_HwSasGyCCRTerminateNumber_Object = MibTableColumn
hwSasGyCCRTerminateNumber = _HwSasGyCCRTerminateNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 10),
    _HwSasGyCCRTerminateNumber_Type()
)
hwSasGyCCRTerminateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyCCRTerminateNumber.setStatus("current")
_HwSasGyCCATerminateNumber_Type = Gauge32
_HwSasGyCCATerminateNumber_Object = MibTableColumn
hwSasGyCCATerminateNumber = _HwSasGyCCATerminateNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 11),
    _HwSasGyCCATerminateNumber_Type()
)
hwSasGyCCATerminateNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyCCATerminateNumber.setStatus("current")
_HwSasGyRARNumber_Type = Gauge32
_HwSasGyRARNumber_Object = MibTableColumn
hwSasGyRARNumber = _HwSasGyRARNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 12),
    _HwSasGyRARNumber_Type()
)
hwSasGyRARNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyRARNumber.setStatus("current")
_HwSasGyRAANumber_Type = Gauge32
_HwSasGyRAANumber_Object = MibTableColumn
hwSasGyRAANumber = _HwSasGyRAANumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 13),
    _HwSasGyRAANumber_Type()
)
hwSasGyRAANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyRAANumber.setStatus("current")
_HwSasGyASRNumber_Type = Gauge32
_HwSasGyASRNumber_Object = MibTableColumn
hwSasGyASRNumber = _HwSasGyASRNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 14),
    _HwSasGyASRNumber_Type()
)
hwSasGyASRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyASRNumber.setStatus("current")
_HwSasGyASANumber_Type = Gauge32
_HwSasGyASANumber_Object = MibTableColumn
hwSasGyASANumber = _HwSasGyASANumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 7, 1, 15),
    _HwSasGyASANumber_Type()
)
hwSasGyASANumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyASANumber.setStatus("current")
_HwSasGyErrorTable_Object = MibTable
hwSasGyErrorTable = _HwSasGyErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8)
)
if mibBuilder.loadTexts:
    hwSasGyErrorTable.setStatus("current")
_HwSasGyErrorEntry_Object = MibTableRow
hwSasGyErrorEntry = _HwSasGyErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1)
)
hwSasGyErrorEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSasGyErrorIndex"),
)
if mibBuilder.loadTexts:
    hwSasGyErrorEntry.setStatus("current")
_HwSasGyErrorIndex_Type = Gauge32
_HwSasGyErrorIndex_Object = MibTableColumn
hwSasGyErrorIndex = _HwSasGyErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 1),
    _HwSasGyErrorIndex_Type()
)
hwSasGyErrorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSasGyErrorIndex.setStatus("current")


class _HwSasGyErrorLocation_Type(OctetString):
    """Custom type hwSasGyErrorLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSasGyErrorLocation_Type.__name__ = "OctetString"
_HwSasGyErrorLocation_Object = MibTableColumn
hwSasGyErrorLocation = _HwSasGyErrorLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 2),
    _HwSasGyErrorLocation_Type()
)
hwSasGyErrorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyErrorLocation.setStatus("current")
_HwSasIPAddressForGyError_Type = IpAddress
_HwSasIPAddressForGyError_Object = MibTableColumn
hwSasIPAddressForGyError = _HwSasIPAddressForGyError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 3),
    _HwSasIPAddressForGyError_Type()
)
hwSasIPAddressForGyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasIPAddressForGyError.setStatus("current")
_HwGyCommunitionInterruptedTimes_Type = Gauge32
_HwGyCommunitionInterruptedTimes_Object = MibTableColumn
hwGyCommunitionInterruptedTimes = _HwGyCommunitionInterruptedTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 4),
    _HwGyCommunitionInterruptedTimes_Type()
)
hwGyCommunitionInterruptedTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGyCommunitionInterruptedTimes.setStatus("current")
_HwSasGyCCRInitalRetransmissions_Type = Gauge32
_HwSasGyCCRInitalRetransmissions_Object = MibTableColumn
hwSasGyCCRInitalRetransmissions = _HwSasGyCCRInitalRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 5),
    _HwSasGyCCRInitalRetransmissions_Type()
)
hwSasGyCCRInitalRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyCCRInitalRetransmissions.setStatus("current")
_HwSasGyCCRUpdateRetransmissions_Type = Gauge32
_HwSasGyCCRUpdateRetransmissions_Object = MibTableColumn
hwSasGyCCRUpdateRetransmissions = _HwSasGyCCRUpdateRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 6),
    _HwSasGyCCRUpdateRetransmissions_Type()
)
hwSasGyCCRUpdateRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyCCRUpdateRetransmissions.setStatus("current")
_HwSasGyCCRTerminateRetransmissions_Type = Gauge32
_HwSasGyCCRTerminateRetransmissions_Object = MibTableColumn
hwSasGyCCRTerminateRetransmissions = _HwSasGyCCRTerminateRetransmissions_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 7),
    _HwSasGyCCRTerminateRetransmissions_Type()
)
hwSasGyCCRTerminateRetransmissions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGyCCRTerminateRetransmissions.setStatus("current")
_HwOcsFaultDeactiveNumber_Type = Gauge32
_HwOcsFaultDeactiveNumber_Object = MibTableColumn
hwOcsFaultDeactiveNumber = _HwOcsFaultDeactiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 8),
    _HwOcsFaultDeactiveNumber_Type()
)
hwOcsFaultDeactiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwOcsFaultDeactiveNumber.setStatus("current")
_HwGyType1ResultCode_Type = Gauge32
_HwGyType1ResultCode_Object = MibTableColumn
hwGyType1ResultCode = _HwGyType1ResultCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 9),
    _HwGyType1ResultCode_Type()
)
hwGyType1ResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGyType1ResultCode.setStatus("current")
_HwGyType2ResultCode_Type = Gauge32
_HwGyType2ResultCode_Object = MibTableColumn
hwGyType2ResultCode = _HwGyType2ResultCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 10),
    _HwGyType2ResultCode_Type()
)
hwGyType2ResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGyType2ResultCode.setStatus("current")
_HwGyType3ResultCode_Type = Gauge32
_HwGyType3ResultCode_Object = MibTableColumn
hwGyType3ResultCode = _HwGyType3ResultCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 11),
    _HwGyType3ResultCode_Type()
)
hwGyType3ResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGyType3ResultCode.setStatus("current")
_HwGyType4ResultCode_Type = Gauge32
_HwGyType4ResultCode_Object = MibTableColumn
hwGyType4ResultCode = _HwGyType4ResultCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 12),
    _HwGyType4ResultCode_Type()
)
hwGyType4ResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGyType4ResultCode.setStatus("current")
_HwGyType5ResultCode_Type = Gauge32
_HwGyType5ResultCode_Object = MibTableColumn
hwGyType5ResultCode = _HwGyType5ResultCode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 8, 1, 13),
    _HwGyType5ResultCode_Type()
)
hwGyType5ResultCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGyType5ResultCode.setStatus("current")
_HwSasGzPerformanceTable_Object = MibTable
hwSasGzPerformanceTable = _HwSasGzPerformanceTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 9)
)
if mibBuilder.loadTexts:
    hwSasGzPerformanceTable.setStatus("current")
_HwSasGzPerformanceEntry_Object = MibTableRow
hwSasGzPerformanceEntry = _HwSasGzPerformanceEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 9, 1)
)
hwSasGzPerformanceEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSasGzPerformanceIndex"),
)
if mibBuilder.loadTexts:
    hwSasGzPerformanceEntry.setStatus("current")
_HwSasGzPerformanceIndex_Type = Gauge32
_HwSasGzPerformanceIndex_Object = MibTableColumn
hwSasGzPerformanceIndex = _HwSasGzPerformanceIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 9, 1, 1),
    _HwSasGzPerformanceIndex_Type()
)
hwSasGzPerformanceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSasGzPerformanceIndex.setStatus("current")


class _HwSasGzPerformanceLocation_Type(OctetString):
    """Custom type hwSasGzPerformanceLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSasGzPerformanceLocation_Type.__name__ = "OctetString"
_HwSasGzPerformanceLocation_Object = MibTableColumn
hwSasGzPerformanceLocation = _HwSasGzPerformanceLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 9, 1, 2),
    _HwSasGzPerformanceLocation_Type()
)
hwSasGzPerformanceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGzPerformanceLocation.setStatus("current")
_HwSasIPAddressForGzPerformance_Type = IpAddress
_HwSasIPAddressForGzPerformance_Object = MibTableColumn
hwSasIPAddressForGzPerformance = _HwSasIPAddressForGzPerformance_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 9, 1, 3),
    _HwSasIPAddressForGzPerformance_Type()
)
hwSasIPAddressForGzPerformance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasIPAddressForGzPerformance.setStatus("current")
_HwSasGzSendCDRNumber_Type = Gauge32
_HwSasGzSendCDRNumber_Object = MibTableColumn
hwSasGzSendCDRNumber = _HwSasGzSendCDRNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 9, 1, 4),
    _HwSasGzSendCDRNumber_Type()
)
hwSasGzSendCDRNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGzSendCDRNumber.setStatus("current")
_HwSasGzErrorTable_Object = MibTable
hwSasGzErrorTable = _HwSasGzErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 10)
)
if mibBuilder.loadTexts:
    hwSasGzErrorTable.setStatus("current")
_HwSasGzErrorEntry_Object = MibTableRow
hwSasGzErrorEntry = _HwSasGzErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 10, 1)
)
hwSasGzErrorEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSasGzErrorIndex"),
)
if mibBuilder.loadTexts:
    hwSasGzErrorEntry.setStatus("current")
_HwSasGzErrorIndex_Type = Gauge32
_HwSasGzErrorIndex_Object = MibTableColumn
hwSasGzErrorIndex = _HwSasGzErrorIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 10, 1, 1),
    _HwSasGzErrorIndex_Type()
)
hwSasGzErrorIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSasGzErrorIndex.setStatus("current")


class _HwSasGzErrorLocation_Type(OctetString):
    """Custom type hwSasGzErrorLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSasGzErrorLocation_Type.__name__ = "OctetString"
_HwSasGzErrorLocation_Object = MibTableColumn
hwSasGzErrorLocation = _HwSasGzErrorLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 10, 1, 2),
    _HwSasGzErrorLocation_Type()
)
hwSasGzErrorLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGzErrorLocation.setStatus("current")
_HwSasIPAddressForGzError_Type = IpAddress
_HwSasIPAddressForGzError_Object = MibTableColumn
hwSasIPAddressForGzError = _HwSasIPAddressForGzError_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 10, 1, 3),
    _HwSasIPAddressForGzError_Type()
)
hwSasIPAddressForGzError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasIPAddressForGzError.setStatus("current")
_HwGzCommunitionInterruptedTimes_Type = Gauge32
_HwGzCommunitionInterruptedTimes_Object = MibTableColumn
hwGzCommunitionInterruptedTimes = _HwGzCommunitionInterruptedTimes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 10, 1, 4),
    _HwGzCommunitionInterruptedTimes_Type()
)
hwGzCommunitionInterruptedTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwGzCommunitionInterruptedTimes.setStatus("current")
_HwSasGzAbnormalSignalingNumber_Type = Gauge32
_HwSasGzAbnormalSignalingNumber_Object = MibTableColumn
hwSasGzAbnormalSignalingNumber = _HwSasGzAbnormalSignalingNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 10, 1, 5),
    _HwSasGzAbnormalSignalingNumber_Type()
)
hwSasGzAbnormalSignalingNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSasGzAbnormalSignalingNumber.setStatus("current")
_HwSpsLinkBandwidthTable_Object = MibTable
hwSpsLinkBandwidthTable = _HwSpsLinkBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 11)
)
if mibBuilder.loadTexts:
    hwSpsLinkBandwidthTable.setStatus("current")
_HwSpsLinkBandwidthEntry_Object = MibTableRow
hwSpsLinkBandwidthEntry = _HwSpsLinkBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 11, 1)
)
hwSpsLinkBandwidthEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwSpsLinkBandwidthIndex"),
)
if mibBuilder.loadTexts:
    hwSpsLinkBandwidthEntry.setStatus("current")
_HwSpsLinkBandwidthIndex_Type = Gauge32
_HwSpsLinkBandwidthIndex_Object = MibTableColumn
hwSpsLinkBandwidthIndex = _HwSpsLinkBandwidthIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 11, 1, 1),
    _HwSpsLinkBandwidthIndex_Type()
)
hwSpsLinkBandwidthIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwSpsLinkBandwidthIndex.setStatus("current")
_HwSpsLinkId_Type = Gauge32
_HwSpsLinkId_Object = MibTableColumn
hwSpsLinkId = _HwSpsLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 11, 1, 2),
    _HwSpsLinkId_Type()
)
hwSpsLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSpsLinkId.setStatus("current")


class _HwSPSLinkLocation_Type(OctetString):
    """Custom type hwSPSLinkLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwSPSLinkLocation_Type.__name__ = "OctetString"
_HwSPSLinkLocation_Object = MibTableColumn
hwSPSLinkLocation = _HwSPSLinkLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 11, 1, 3),
    _HwSPSLinkLocation_Type()
)
hwSPSLinkLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSPSLinkLocation.setStatus("current")
_HwUpstreamPassedBandwidth_Type = Counter64
_HwUpstreamPassedBandwidth_Object = MibTableColumn
hwUpstreamPassedBandwidth = _HwUpstreamPassedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 11, 1, 4),
    _HwUpstreamPassedBandwidth_Type()
)
hwUpstreamPassedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUpstreamPassedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwUpstreamPassedBandwidth.setUnits("Kbits/s")
_HwDownstreamPassedBandwidth_Type = Counter64
_HwDownstreamPassedBandwidth_Object = MibTableColumn
hwDownstreamPassedBandwidth = _HwDownstreamPassedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 11, 1, 5),
    _HwDownstreamPassedBandwidth_Type()
)
hwDownstreamPassedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDownstreamPassedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwDownstreamPassedBandwidth.setUnits("Kbits/s")
_HwUpstreamDiscardedBandwidth_Type = Counter64
_HwUpstreamDiscardedBandwidth_Object = MibTableColumn
hwUpstreamDiscardedBandwidth = _HwUpstreamDiscardedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 11, 1, 6),
    _HwUpstreamDiscardedBandwidth_Type()
)
hwUpstreamDiscardedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwUpstreamDiscardedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwUpstreamDiscardedBandwidth.setUnits("Kbits/s")
_HwDownstreamDiscardedBandwidth_Type = Counter64
_HwDownstreamDiscardedBandwidth_Object = MibTableColumn
hwDownstreamDiscardedBandwidth = _HwDownstreamDiscardedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 3, 11, 1, 7),
    _HwDownstreamDiscardedBandwidth_Type()
)
hwDownstreamDiscardedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwDownstreamDiscardedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    hwDownstreamDiscardedBandwidth.setUnits("Kbits/s")
_HwServiceWirelessTrap_ObjectIdentity = ObjectIdentity
hwServiceWirelessTrap = _HwServiceWirelessTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4)
)
_HwServiceVoIPObject_ObjectIdentity = ObjectIdentity
hwServiceVoIPObject = _HwServiceVoIPObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 5)
)
_HwServiceDDoSObject_ObjectIdentity = ObjectIdentity
hwServiceDDoSObject = _HwServiceDDoSObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 6)
)
_HwServiceTrap_ObjectIdentity = ObjectIdentity
hwServiceTrap = _HwServiceTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7)
)
_HwServiceTrapVB_ObjectIdentity = ObjectIdentity
hwServiceTrapVB = _HwServiceTrapVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1)
)
_HwServiceResourceLocation_Type = OctetString
_HwServiceResourceLocation_Object = MibScalar
hwServiceResourceLocation = _HwServiceResourceLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 1),
    _HwServiceResourceLocation_Type()
)
hwServiceResourceLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceResourceLocation.setStatus("current")
_HwServiceResourceType_Type = OctetString
_HwServiceResourceType_Object = MibScalar
hwServiceResourceType = _HwServiceResourceType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 2),
    _HwServiceResourceType_Type()
)
hwServiceResourceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceResourceType.setStatus("current")
_HwServiceResourceUsage_Type = Integer32
_HwServiceResourceUsage_Object = MibScalar
hwServiceResourceUsage = _HwServiceResourceUsage_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 3),
    _HwServiceResourceUsage_Type()
)
hwServiceResourceUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceResourceUsage.setStatus("current")
_HwServiceResourceVcpuId_Type = Integer32
_HwServiceResourceVcpuId_Object = MibScalar
hwServiceResourceVcpuId = _HwServiceResourceVcpuId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 4),
    _HwServiceResourceVcpuId_Type()
)
hwServiceResourceVcpuId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwServiceResourceVcpuId.setStatus("current")
_HwCollectorIP_Type = IpAddress
_HwCollectorIP_Object = MibScalar
hwCollectorIP = _HwCollectorIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 5),
    _HwCollectorIP_Type()
)
hwCollectorIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCollectorIP.setStatus("current")


class _HwCollectorPort_Type(Gauge32):
    """Custom type hwCollectorPort based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwCollectorPort_Type.__name__ = "Gauge32"
_HwCollectorPort_Object = MibScalar
hwCollectorPort = _HwCollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 6),
    _HwCollectorPort_Type()
)
hwCollectorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwCollectorPort.setStatus("current")


class _HwInterfaceList_Type(OctetString):
    """Custom type hwInterfaceList based on OctetString"""
    defaultValue = OctetString("NULL")


_HwInterfaceList_Type.__name__ = "OctetString"
_HwInterfaceList_Object = MibScalar
hwInterfaceList = _HwInterfaceList_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 7),
    _HwInterfaceList_Type()
)
hwInterfaceList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwInterfaceList.setStatus("current")


class _HwRecoverTrapCause_Type(OctetString):
    """Custom type hwRecoverTrapCause based on OctetString"""
    defaultValue = OctetString("consistent")


_HwRecoverTrapCause_Type.__name__ = "OctetString"
_HwRecoverTrapCause_Object = MibScalar
hwRecoverTrapCause = _HwRecoverTrapCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 8),
    _HwRecoverTrapCause_Type()
)
hwRecoverTrapCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwRecoverTrapCause.setStatus("current")
_HwSpammerFTPServeIP_Type = IpAddress
_HwSpammerFTPServeIP_Object = MibScalar
hwSpammerFTPServeIP = _HwSpammerFTPServeIP_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 9),
    _HwSpammerFTPServeIP_Type()
)
hwSpammerFTPServeIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpammerFTPServeIP.setStatus("current")


class _HwSpammerFTPServePort_Type(Gauge32):
    """Custom type hwSpammerFTPServePort based on Gauge32"""
    subtypeSpec = Gauge32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HwSpammerFTPServePort_Type.__name__ = "Gauge32"
_HwSpammerFTPServePort_Object = MibScalar
hwSpammerFTPServePort = _HwSpammerFTPServePort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 10),
    _HwSpammerFTPServePort_Type()
)
hwSpammerFTPServePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwSpammerFTPServePort.setStatus("current")


class _HwCAExpireTime_Type(OctetString):
    """Custom type hwCAExpireTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_HwCAExpireTime_Type.__name__ = "OctetString"
_HwCAExpireTime_Object = MibScalar
hwCAExpireTime = _HwCAExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 1, 11),
    _HwCAExpireTime_Type()
)
hwCAExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwCAExpireTime.setStatus("current")
_HwServiceTrapConfig_ObjectIdentity = ObjectIdentity
hwServiceTrapConfig = _HwServiceTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2)
)
_HwExtendedFeatureTrap_ObjectIdentity = ObjectIdentity
hwExtendedFeatureTrap = _HwExtendedFeatureTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 8)
)
_HwExtendedFeatureTrapVB_ObjectIdentity = ObjectIdentity
hwExtendedFeatureTrapVB = _HwExtendedFeatureTrapVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 8, 1)
)
_HwExtendedFeatureLocation_Type = OctetString
_HwExtendedFeatureLocation_Object = MibScalar
hwExtendedFeatureLocation = _HwExtendedFeatureLocation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 8, 1, 1),
    _HwExtendedFeatureLocation_Type()
)
hwExtendedFeatureLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExtendedFeatureLocation.setStatus("current")
_HwExtendedFeatureType_Type = OctetString
_HwExtendedFeatureType_Object = MibScalar
hwExtendedFeatureType = _HwExtendedFeatureType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 8, 1, 2),
    _HwExtendedFeatureType_Type()
)
hwExtendedFeatureType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwExtendedFeatureType.setStatus("current")
_HwExtendedModuleTrapConfig_ObjectIdentity = ObjectIdentity
hwExtendedModuleTrapConfig = _HwExtendedModuleTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 8, 2)
)
_HwSAInstanceTrap_ObjectIdentity = ObjectIdentity
hwSAInstanceTrap = _HwSAInstanceTrap_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 9)
)
_HwSAInstanceTrapVB_ObjectIdentity = ObjectIdentity
hwSAInstanceTrapVB = _HwSAInstanceTrapVB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 9, 1)
)


class _HwSAInstanceName_Type(OctetString):
    """Custom type hwSAInstanceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HwSAInstanceName_Type.__name__ = "OctetString"
_HwSAInstanceName_Object = MibScalar
hwSAInstanceName = _HwSAInstanceName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 9, 1, 1),
    _HwSAInstanceName_Type()
)
hwSAInstanceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSAInstanceName.setStatus("current")


class _HwSAinstanceCPUTotalNumber_Type(Integer32):
    """Custom type hwSAinstanceCPUTotalNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwSAinstanceCPUTotalNumber_Type.__name__ = "Integer32"
_HwSAinstanceCPUTotalNumber_Object = MibScalar
hwSAinstanceCPUTotalNumber = _HwSAinstanceCPUTotalNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 9, 1, 2),
    _HwSAinstanceCPUTotalNumber_Type()
)
hwSAinstanceCPUTotalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSAinstanceCPUTotalNumber.setStatus("current")


class _HwSAinstanceCPUActiveNumber_Type(Integer32):
    """Custom type hwSAinstanceCPUActiveNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwSAinstanceCPUActiveNumber_Type.__name__ = "Integer32"
_HwSAinstanceCPUActiveNumber_Object = MibScalar
hwSAinstanceCPUActiveNumber = _HwSAinstanceCPUActiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 9, 1, 3),
    _HwSAinstanceCPUActiveNumber_Type()
)
hwSAinstanceCPUActiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSAinstanceCPUActiveNumber.setStatus("current")


class _HwSAinstanceCPULeastActiveNumber_Type(Integer32):
    """Custom type hwSAinstanceCPULeastActiveNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_HwSAinstanceCPULeastActiveNumber_Type.__name__ = "Integer32"
_HwSAinstanceCPULeastActiveNumber_Object = MibScalar
hwSAinstanceCPULeastActiveNumber = _HwSAinstanceCPULeastActiveNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 9, 1, 4),
    _HwSAinstanceCPULeastActiveNumber_Type()
)
hwSAinstanceCPULeastActiveNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwSAinstanceCPULeastActiveNumber.setStatus("current")
_HwSAInstanceTrapConfig_ObjectIdentity = ObjectIdentity
hwSAInstanceTrapConfig = _HwSAInstanceTrapConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 9, 2)
)
_HwSALicense_ObjectIdentity = ObjectIdentity
hwSALicense = _HwSALicense_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 3)
)
_HwLicenseTable_Object = MibTable
hwLicenseTable = _HwLicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 3, 1)
)
if mibBuilder.loadTexts:
    hwLicenseTable.setStatus("current")
_HwLicenseEntry_Object = MibTableRow
hwLicenseEntry = _HwLicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 3, 1, 1)
)
hwLicenseEntry.setIndexNames(
    (0, "HUAWEI-SECURITY-SAFE-MIB", "hwLicenseServiceID"),
)
if mibBuilder.loadTexts:
    hwLicenseEntry.setStatus("current")


class _HwLicenseServiceID_Type(Integer32):
    """Custom type hwLicenseServiceID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_HwLicenseServiceID_Type.__name__ = "Integer32"
_HwLicenseServiceID_Object = MibTableColumn
hwLicenseServiceID = _HwLicenseServiceID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 3, 1, 1, 1),
    _HwLicenseServiceID_Type()
)
hwLicenseServiceID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hwLicenseServiceID.setStatus("current")


class _HwActiveSpsNumber_Type(Integer32):
    """Custom type hwActiveSpsNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_HwActiveSpsNumber_Type.__name__ = "Integer32"
_HwActiveSpsNumber_Object = MibTableColumn
hwActiveSpsNumber = _HwActiveSpsNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 3, 1, 1, 2),
    _HwActiveSpsNumber_Type()
)
hwActiveSpsNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hwActiveSpsNumber.setStatus("current")
_HwEnabledFunction_Type = OctetString
_HwEnabledFunction_Object = MibTableColumn
hwEnabledFunction = _HwEnabledFunction_Object(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 3, 1, 1, 3),
    _HwEnabledFunction_Type()
)
hwEnabledFunction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hwEnabledFunction.setStatus("current")
_HwSALicenseTraps_ObjectIdentity = ObjectIdentity
hwSALicenseTraps = _HwSALicenseTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 3, 2)
)
_HwSAConformance_ObjectIdentity = ObjectIdentity
hwSAConformance = _HwSAConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 4)
)
_HwSACompliances_ObjectIdentity = ObjectIdentity
hwSACompliances = _HwSACompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 4, 1)
)
_HwSAGroups_ObjectIdentity = ObjectIdentity
hwSAGroups = _HwSAGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 4, 2)
)

# Managed Objects groups

hwSAObject = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 4, 2, 2)
)
hwSAObject.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkInsideInterface"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkOutsideInterface"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkInsideInterfaceState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkOutsideInterfaceState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeRole"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeStatus"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterSasNodeNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterSasSysLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterSasSysIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterSasMode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterMapSysSasMode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterMapNumberOfDG"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterMapDevices"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentUsageMode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityCpuUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityCpuUsageThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityMemoryUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityMemoryUsageThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAResourceType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwResourceCapacity"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwResourceUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwResourceLeft"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSACbbLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSACbbVersion"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBWListLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBWListVersion"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSpsIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSasIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkStatus"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkConnState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkNumPacketsSent"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkBytesSent"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkNumPacketsRecv"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkBytesRecv"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkNumErrPacketsRecv"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkComponentType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateLink"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentPrimaryIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponenSecondaryIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentSecIPConnStatus"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentPriIPConnStatus"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityTemperatureThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityPhysicalIndex"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityTemperature"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateMode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateChannel0State"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateChannel1State"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBWListType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuOverLoadPackages"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLpuOverLoadBytes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSasLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSpsLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSnifferInfoState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSnifferDstIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSnifferSrcIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPacketErrCount"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPacketSendCount"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSnifferInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSysFdiInstanceID"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkUcssIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkSpsIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkSpsLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkOutsideInterfaceBandWidth"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkInsideInterfaceBandWidth"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSysFdiDestBackupIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLpuOverLoadPackages"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuOverLoadBytes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkSysLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAFdiConnectLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsNewFlowNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsNewTempFlowNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsDeleteFlowNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBackupGroupPeerState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBackupGroupPeerSlot"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBackupGroupID"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeSelfState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadePeerState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeCfg"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNormalSPSNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwEnabledFunction"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwActiveSpsNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSysFdiDestMasterIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateRIsignal"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkCurrentState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkLosTimes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkLinkTimes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassSwitchCurrentPosition"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassSwitchWorkingTimes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassSwitchProtectionTimes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeInterfaceStatus"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceVcpuId"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeInterface"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalClusterNodeID"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPeerClusterNodeID"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBackupGroupLocalState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBackupGroupLocalSlot"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPeerClusterNodeIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSHostName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFHostName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGCdrCachePoolUsed"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGGrade"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalClusterNodeIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkBoundGroupNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectCG"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectPCRF"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASNameConnectPCRF"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASIPAddressConnectPCRF"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASPortConnectPCRF"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectOCS"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASPortConnectOCS"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsMessageNumberLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassAlarmDescription"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassPowerStatus"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassSlotNum"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxPerformanceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxTotalSendNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxTotalRecieveNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxCCRInitalNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxCCAInitalNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxCCRUpdateNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxCCAUpdateNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxRARNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxRAANumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxASRNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxASANumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxErrorLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwGxCommunitionInterruptedTimes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyPerformanceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyTotalSendNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyTotalRecieveNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyCCRInitalNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyCCAInitalNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyCCRUpdateNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyCCAUpdateNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyCCRTerminateNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyCCATerminateNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyRARNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyRAANumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyASRNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyASANumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyErrorLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwGyCommunitionInterruptedTimes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOcsFaultDeactiveNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGzPerformanceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGzSendCDRNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGzErrorLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwGzCommunitionInterruptedTimes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGzAbnormalSignalingNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASIPAddressConnectOCS"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASNameConnectOCS"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyCCRInitalRetransmissions"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyCCRUpdateRetransmissions"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasIPAddressForGxPerformance"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasIPAddressForGxError"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasIPAddressForGyPerformance"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasIPAddressForGyError"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasIPAddressForGzPerformance"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasIPAddressForGzError"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGyCCRTerminateRetransmissions"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxCCRInitalRetransmissions"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxCCRUpdateRetransmissions"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxCCRTerminateRetransmissions"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwGyType1ResultCode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwGyType2ResultCode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwGyType3ResultCode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwGyType4ResultCode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwGyType5ResultCode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasMessageTotalNum"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasMessageAccountOffLineNum"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasMessageAccountOnLineNum"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasMessageIpOffLineNum"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCollectorPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCollectorIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsRdasLinkRdasIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsRdasLinkSpsLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasMessageIpOnLineNum"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuFlowOverLoadLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuFlowOverLoadPackets"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsFragmentSpsLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasRpdAccountMessageRpdIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasRpdAccountMessageLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwRecoverTrapCause"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwInterfaceList"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpammerFTPServePort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpammerFTPServeIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1BackupGroupBoardType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1BackupGroupBoardList"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1BackupGroupID"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSPSLinkLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwUpstreamPassedBandwidth"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDownstreamPassedBandwidth"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwUpstreamDiscardedBandwidth"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDownstreamDiscardedBandwidth"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASPortConnectDRA"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASIPAddressConnectDRA"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASNameConnectDRA"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAHostName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectDRA"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsLinkId"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1BackupIsEnable"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalBackupGroupStateCpuIndex"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalBackupGroupStateCpuLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalBackupGroupStateCpuType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalBackupGroupStateIsEnable"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalBackupGroupStateGroupId"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalBackupGroupStateSpuType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalBackupGroupStateCpuMode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalBackupSpuTypeInconsist"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLocalBackupGroupIsStandby"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsLeastNumberCfg"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsQueueUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsOverloadThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsEntityLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsAverageCpuUsageThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsAverageCpuUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsCpuEntityIndex"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsLeastNumberIndex"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCAExpireTime"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAinstanceCPULeastActiveNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAinstanceCPUActiveNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAinstanceCPUTotalNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAInstanceName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasMessageType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasMessageLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxCCRTerminateNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasGxCCATerminateNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwExtendedFeatureLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwExtendedFeatureType"))
)
if mibBuilder.loadTexts:
    hwSAObject.setStatus("current")


# Notification objects

hwStateChangeToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 2, 1)
)
hwStateChangeToNormalTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoIPAddress"))
)
if mibBuilder.loadTexts:
    hwStateChangeToNormalTrap.setStatus(
        "current"
    )

hwStateChangeToAbnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 2, 2)
)
hwStateChangeToAbnormalTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoIPAddress"))
)
if mibBuilder.loadTexts:
    hwStateChangeToAbnormalTrap.setStatus(
        "current"
    )

hwLinkBandWidthChangeToUnequalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 2, 3)
)
hwLinkBandWidthChangeToUnequalTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkInsideInterface"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkOutsideInterface"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkInsideInterfaceBandWidth"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkOutsideInterfaceBandWidth"))
)
if mibBuilder.loadTexts:
    hwLinkBandWidthChangeToUnequalTrap.setStatus(
        "current"
    )

hwLinkBandWidthChangeToEqualTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 2, 4)
)
hwLinkBandWidthChangeToEqualTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkInsideInterface"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkOutsideInterface"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkInsideInterfaceBandWidth"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkOutsideInterfaceBandWidth"))
)
if mibBuilder.loadTexts:
    hwLinkBandWidthChangeToEqualTrap.setStatus(
        "current"
    )

hwLinkBoundGroupStateChangeToAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 2, 5)
)
hwLinkBoundGroupStateChangeToAbnormal.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkBoundGroupNumber")
)
if mibBuilder.loadTexts:
    hwLinkBoundGroupStateChangeToAbnormal.setStatus(
        "current"
    )

hwLinkBoundGroupStateChangeToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 2, 6)
)
hwLinkBoundGroupStateChangeToNormal.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceLinkBoundGroupNumber")
)
if mibBuilder.loadTexts:
    hwLinkBoundGroupStateChangeToNormal.setStatus(
        "current"
    )

hwCascadeLinkStateChangeToAbnormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 2, 7)
)
hwCascadeLinkStateChangeToAbnormal.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeInterface")
)
if mibBuilder.loadTexts:
    hwCascadeLinkStateChangeToAbnormal.setStatus(
        "current"
    )

hwCascadeLinkStateChangeToNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 2, 8)
)
hwCascadeLinkStateChangeToNormal.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeInterface")
)
if mibBuilder.loadTexts:
    hwCascadeLinkStateChangeToNormal.setStatus(
        "current"
    )

hwCascadeLinkOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 2, 9)
)
hwCascadeLinkOverloadTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeInterface")
)
if mibBuilder.loadTexts:
    hwCascadeLinkOverloadTrap.setStatus(
        "current"
    )

hwPeerNodeConnectDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 1)
)
hwPeerNodeConnectDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeRole"))
)
if mibBuilder.loadTexts:
    hwPeerNodeConnectDownTrap.setStatus(
        "current"
    )

hwPeerNodeConnectUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 2)
)
hwPeerNodeConnectUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeRole"))
)
if mibBuilder.loadTexts:
    hwPeerNodeConnectUpTrap.setStatus(
        "current"
    )

hwNodeModeChangeActiveTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 3)
)
hwNodeModeChangeActiveTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"))
)
if mibBuilder.loadTexts:
    hwNodeModeChangeActiveTrap.setStatus(
        "current"
    )

hwNodeModeChangeStandbyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 4)
)
hwNodeModeChangeStandbyTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"))
)
if mibBuilder.loadTexts:
    hwNodeModeChangeStandbyTrap.setStatus(
        "current"
    )

hwNodeCompConnectUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 5)
)
hwNodeCompConnectUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwComponentType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentPrimaryIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponenSecondaryIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentUsageMode"))
)
if mibBuilder.loadTexts:
    hwNodeCompConnectUpTrap.setStatus(
        "current"
    )

hwNodeCompConnectDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 6)
)
hwNodeCompConnectDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwComponentType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentPrimaryIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponenSecondaryIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentUsageMode"))
)
if mibBuilder.loadTexts:
    hwNodeCompConnectDownTrap.setStatus(
        "current"
    )

hwConfigurationInconsistentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 7)
)
hwConfigurationInconsistentTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"))
)
if mibBuilder.loadTexts:
    hwConfigurationInconsistentTrap.setStatus(
        "current"
    )

hwSPSAmountInsufficientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 8)
)
hwSPSAmountInsufficientTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNormalSPSNumber"))
)
if mibBuilder.loadTexts:
    hwSPSAmountInsufficientTrap.setStatus(
        "current"
    )

hwSPSAmountSufficientTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 9)
)
hwSPSAmountSufficientTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNormalSPSNumber"))
)
if mibBuilder.loadTexts:
    hwSPSAmountSufficientTrap.setStatus(
        "current"
    )

hwCascadeFailedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 10)
)
hwCascadeFailedTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeCfg"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadePeerState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeSelfState"))
)
if mibBuilder.loadTexts:
    hwCascadeFailedTrap.setStatus(
        "current"
    )

hwCascadeSuccessfulTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 11)
)
hwCascadeSuccessfulTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeCfg"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadePeerState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeSelfState"))
)
if mibBuilder.loadTexts:
    hwCascadeSuccessfulTrap.setStatus(
        "current"
    )

hwHotBackupConfigurationCheckFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 4, 12)
)
hwHotBackupConfigurationCheckFailTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"))
)
if mibBuilder.loadTexts:
    hwHotBackupConfigurationCheckFailTrap.setStatus(
        "current"
    )

hwBypassSwitchWorkingMode = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 6, 1)
)
hwBypassSwitchWorkingMode.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateLink"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateChannel1State"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateChannel0State"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateMode"))
)
if mibBuilder.loadTexts:
    hwBypassSwitchWorkingMode.setStatus(
        "current"
    )

hwBypassLinkState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 6, 2)
)
hwBypassLinkState.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateLink"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateRIsignal"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkCurrentState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkLosTimes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkLinkTimes"))
)
if mibBuilder.loadTexts:
    hwBypassLinkState.setStatus(
        "current"
    )

hwBypassLinkSwitchState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 6, 3)
)
hwBypassLinkSwitchState.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkStateLink"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassSwitchCurrentPosition"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassSwitchWorkingTimes"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassSwitchProtectionTimes"))
)
if mibBuilder.loadTexts:
    hwBypassLinkSwitchState.setStatus(
        "current"
    )

hwBypassMonitorState = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 6, 4)
)
hwBypassMonitorState.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwBypassSlotNum"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassPowerStatus"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassAlarmDescription"))
)
if mibBuilder.loadTexts:
    hwBypassMonitorState.setStatus(
        "current"
    )

hwSpuCpuUsageThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 8, 1)
)
hwSpuCpuUsageThresholdTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityCpuUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityCpuUsageThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityLocation"))
)
if mibBuilder.loadTexts:
    hwSpuCpuUsageThresholdTrap.setStatus(
        "current"
    )

hwSpuCpuUsageThresholdRestoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 8, 2)
)
hwSpuCpuUsageThresholdRestoreTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityCpuUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityCpuUsageThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityLocation"))
)
if mibBuilder.loadTexts:
    hwSpuCpuUsageThresholdRestoreTrap.setStatus(
        "current"
    )

hwSpuMemUsageThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 8, 3)
)
hwSpuMemUsageThresholdTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityMemoryUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityMemoryUsageThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityLocation"))
)
if mibBuilder.loadTexts:
    hwSpuMemUsageThresholdTrap.setStatus(
        "current"
    )

hwSpuMemUsageThresholdRestoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 8, 4)
)
hwSpuMemUsageThresholdRestoreTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityMemoryUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityMemoryUsageThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityLocation"))
)
if mibBuilder.loadTexts:
    hwSpuMemUsageThresholdRestoreTrap.setStatus(
        "current"
    )

hwSpuTemperatureThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 8, 5)
)
hwSpuTemperatureThresholdTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityTemperature"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityTemperatureThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityLocation"))
)
if mibBuilder.loadTexts:
    hwSpuTemperatureThresholdTrap.setStatus(
        "current"
    )

hwSpuTemperatureThresholdRestoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 8, 6)
)
hwSpuTemperatureThresholdRestoreTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityTemperature"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityTemperatureThreshold"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuEntityLocation"))
)
if mibBuilder.loadTexts:
    hwSpuTemperatureThresholdRestoreTrap.setStatus(
        "current"
    )

hwSpuOverLoadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 10, 1)
)
hwSpuOverLoadTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuOverLoadPackages"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuOverLoadBytes"))
)
if mibBuilder.loadTexts:
    hwSpuOverLoadTrap.setStatus(
        "current"
    )

hwLpuOverLoadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 10, 2)
)
hwLpuOverLoadTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwLpuOverLoadPackages"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLpuOverLoadBytes"))
)
if mibBuilder.loadTexts:
    hwLpuOverLoadTrap.setStatus(
        "current"
    )

hwSpuFlowOverLoadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 12, 1)
)
hwSpuFlowOverLoadTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuFlowOverLoadLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuFlowOverLoadPackets"))
)
if mibBuilder.loadTexts:
    hwSpuFlowOverLoadTrap.setStatus(
        "current"
    )

hwSpuFlowOverLoadRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 12, 2)
)
hwSpuFlowOverLoadRecoverTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuFlowOverLoadLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuFlowOverLoadPackets"))
)
if mibBuilder.loadTexts:
    hwSpuFlowOverLoadRecoverTrap.setStatus(
        "current"
    )

hwHashModeVerifyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 13, 1)
)
if mibBuilder.loadTexts:
    hwHashModeVerifyTrap.setStatus(
        "current"
    )

hwHashModeVerifyRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 1, 13, 2)
)
if mibBuilder.loadTexts:
    hwHashModeVerifyRecoverTrap.setStatus(
        "current"
    )

hwSpuCompLinkAddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 1)
)
hwSpuCompLinkAddTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkComponentType"))
)
if mibBuilder.loadTexts:
    hwSpuCompLinkAddTrap.setStatus(
        "current"
    )

hwSpuCompLinkDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 2)
)
hwSpuCompLinkDeleteTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkComponentType"))
)
if mibBuilder.loadTexts:
    hwSpuCompLinkDeleteTrap.setStatus(
        "current"
    )

hwSpuCompLinkConnectDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 3)
)
hwSpuCompLinkConnectDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkComponentType"))
)
if mibBuilder.loadTexts:
    hwSpuCompLinkConnectDownTrap.setStatus(
        "current"
    )

hwSpuCompLinkConnectUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 4)
)
hwSpuCompLinkConnectUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkComponentType"))
)
if mibBuilder.loadTexts:
    hwSpuCompLinkConnectUpTrap.setStatus(
        "current"
    )

hwSpsSasLinkAddTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 5)
)
hwSpsSasLinkAddTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSpsIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSasIP"))
)
if mibBuilder.loadTexts:
    hwSpsSasLinkAddTrap.setStatus(
        "current"
    )

hwSpsSasLinkDeleteTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 6)
)
hwSpsSasLinkDeleteTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSpsIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSasIP"))
)
if mibBuilder.loadTexts:
    hwSpsSasLinkDeleteTrap.setStatus(
        "current"
    )

hwSpsSasLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 7)
)
hwSpsSasLinkDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSpsIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSasIP"))
)
if mibBuilder.loadTexts:
    hwSpsSasLinkDownTrap.setStatus(
        "current"
    )

hwSpsSasLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 8)
)
hwSpsSasLinkUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSpsIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkSasIP"))
)
if mibBuilder.loadTexts:
    hwSpsSasLinkUpTrap.setStatus(
        "current"
    )

hwResourceNotEnoughTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 9)
)
hwResourceNotEnoughTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAResourceType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwResourceUsage"))
)
if mibBuilder.loadTexts:
    hwResourceNotEnoughTrap.setStatus(
        "current"
    )

hwBWListSyncErrTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 10)
)
hwBWListSyncErrTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwBWListLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBWListVersion"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBWListType"))
)
if mibBuilder.loadTexts:
    hwBWListSyncErrTrap.setStatus(
        "current"
    )

hwSAFdiConnectDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 11)
)
hwSAFdiConnectDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSAFdiConnectLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSysFdiInstanceID"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSysFdiDestMasterIP"))
)
if mibBuilder.loadTexts:
    hwSAFdiConnectDownTrap.setStatus(
        "current"
    )

hwRadiusSnifferNoAckTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 12)
)
hwRadiusSnifferNoAckTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSnifferInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSnifferSrcIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSnifferDstIPAddress"))
)
if mibBuilder.loadTexts:
    hwRadiusSnifferNoAckTrap.setStatus(
        "current"
    )

hwRadiusSnifferAckOkTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 13)
)
hwRadiusSnifferAckOkTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSnifferInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSnifferSrcIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSnifferDstIPAddress"))
)
if mibBuilder.loadTexts:
    hwRadiusSnifferAckOkTrap.setStatus(
        "current"
    )

hwSpsUcssLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 14)
)
hwSpsUcssLinkDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkSpsLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkSpsIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkUcssIP"))
)
if mibBuilder.loadTexts:
    hwSpsUcssLinkDownTrap.setStatus(
        "current"
    )

hwSpsUcssLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 15)
)
hwSpsUcssLinkUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkSpsLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkSpsIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkUcssIP"))
)
if mibBuilder.loadTexts:
    hwSpsUcssLinkUpTrap.setStatus(
        "current"
    )

hwBackupGroupStateChangeToMasterTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 19)
)
hwBackupGroupStateChangeToMasterTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwBackupGroupID")
)
if mibBuilder.loadTexts:
    hwBackupGroupStateChangeToMasterTrap.setStatus(
        "current"
    )

hwBackupGroupStateChangeToBackupTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 21)
)
hwBackupGroupStateChangeToBackupTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwBackupGroupID")
)
if mibBuilder.loadTexts:
    hwBackupGroupStateChangeToBackupTrap.setStatus(
        "current"
    )

hwSpsRdasLinkDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 22)
)
hwSpsRdasLinkDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsRdasLinkSpsLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsRdasLinkRdasIP"))
)
if mibBuilder.loadTexts:
    hwSpsRdasLinkDownTrap.setStatus(
        "current"
    )

hwSpsRdasLinkUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 23)
)
hwSpsRdasLinkUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsRdasLinkSpsLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsRdasLinkRdasIP"))
)
if mibBuilder.loadTexts:
    hwSpsRdasLinkUpTrap.setStatus(
        "current"
    )

hwSpsFragmentNotEnoughTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 25)
)
hwSpsFragmentNotEnoughTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsFragmentSpsLocation")
)
if mibBuilder.loadTexts:
    hwSpsFragmentNotEnoughTrap.setStatus(
        "current"
    )

hwSpsFragmentEnoughTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 26)
)
hwSpsFragmentEnoughTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsFragmentSpsLocation")
)
if mibBuilder.loadTexts:
    hwSpsFragmentEnoughTrap.setStatus(
        "current"
    )

hwSasRpdAccountMessageAbnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 27)
)
hwSasRpdAccountMessageAbnormalTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSasRpdAccountMessageLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasRpdAccountMessageRpdIP"))
)
if mibBuilder.loadTexts:
    hwSasRpdAccountMessageAbnormalTrap.setStatus(
        "current"
    )

hwSasRpdAccountMessageNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 28)
)
hwSasRpdAccountMessageNormalTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSasRpdAccountMessageLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasRpdAccountMessageRpdIP"))
)
if mibBuilder.loadTexts:
    hwSasRpdAccountMessageNormalTrap.setStatus(
        "current"
    )

hwNPLUS1HBKEnableSpuNeedResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 29)
)
hwNPLUS1HBKEnableSpuNeedResetTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1BackupGroupID"))
)
if mibBuilder.loadTexts:
    hwNPLUS1HBKEnableSpuNeedResetTrap.setStatus(
        "current"
    )

hwNPLUS1HBKEnableSpuResetRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 30)
)
hwNPLUS1HBKEnableSpuResetRecoverTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation")
)
if mibBuilder.loadTexts:
    hwNPLUS1HBKEnableSpuResetRecoverTrap.setStatus(
        "current"
    )

hwNPLUS1HBKDisableSpuNeedResetTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 31)
)
hwNPLUS1HBKDisableSpuNeedResetTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation")
)
if mibBuilder.loadTexts:
    hwNPLUS1HBKDisableSpuNeedResetTrap.setStatus(
        "current"
    )

hwNPLUS1HBKDisableSpuResetRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 32)
)
hwNPLUS1HBKDisableSpuResetRecoverTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation")
)
if mibBuilder.loadTexts:
    hwNPLUS1HBKDisableSpuResetRecoverTrap.setStatus(
        "current"
    )

hwNPLUS1HBKCpuStandbyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 33)
)
hwNPLUS1HBKCpuStandbyTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1BackupGroupID"))
)
if mibBuilder.loadTexts:
    hwNPLUS1HBKCpuStandbyTrap.setStatus(
        "current"
    )

hwNPLUS1HBKCpuStanbyRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 34)
)
hwNPLUS1HBKCpuStanbyRecoverTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation")
)
if mibBuilder.loadTexts:
    hwNPLUS1HBKCpuStanbyRecoverTrap.setStatus(
        "current"
    )

hwPlsCompLinkConnectDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 35)
)
hwPlsCompLinkConnectDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkComponentType"))
)
if mibBuilder.loadTexts:
    hwPlsCompLinkConnectDownTrap.setStatus(
        "current"
    )

hwPlsCompLinkConnectUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 36)
)
hwPlsCompLinkConnectUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuSysInfoIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwComponentNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkCurrentDestPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkComponentType"))
)
if mibBuilder.loadTexts:
    hwPlsCompLinkConnectUpTrap.setStatus(
        "current"
    )

hwAverageCpuUsageThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 37)
)
hwAverageCpuUsageThresholdTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsEntityLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsAverageCpuUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsAverageCpuUsageThreshold"))
)
if mibBuilder.loadTexts:
    hwAverageCpuUsageThresholdTrap.setStatus(
        "current"
    )

hwAverageCpuUsageThresholdRestoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 38)
)
hwAverageCpuUsageThresholdRestoreTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsEntityLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsAverageCpuUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsAverageCpuUsageThreshold"))
)
if mibBuilder.loadTexts:
    hwAverageCpuUsageThresholdRestoreTrap.setStatus(
        "current"
    )

hwForwardingQueueOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 39)
)
hwForwardingQueueOverloadTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsEntityLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsQueueUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsOverloadThreshold"))
)
if mibBuilder.loadTexts:
    hwForwardingQueueOverloadTrap.setStatus(
        "current"
    )

hwForwardingQueueRestoreTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 40)
)
hwForwardingQueueRestoreTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSpsEntityLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsQueueUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsOverloadThreshold"))
)
if mibBuilder.loadTexts:
    hwForwardingQueueRestoreTrap.setStatus(
        "current"
    )

hwSpsLeastNumberBelowTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 41)
)
hwSpsLeastNumberBelowTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsLeastNumberCfg")
)
if mibBuilder.loadTexts:
    hwSpsLeastNumberBelowTrap.setStatus(
        "current"
    )

hwSpsLeastNumberEqualTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 2, 42)
)
hwSpsLeastNumberEqualTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsLeastNumberCfg")
)
if mibBuilder.loadTexts:
    hwSpsLeastNumberEqualTrap.setStatus(
        "current"
    )

hwCGConnectDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 1)
)
hwCGConnectDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectCG"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGGrade"))
)
if mibBuilder.loadTexts:
    hwCGConnectDownTrap.setStatus(
        "current"
    )

hwCGConnectUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 2)
)
hwCGConnectUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectCG"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGGrade"))
)
if mibBuilder.loadTexts:
    hwCGConnectUpTrap.setStatus(
        "current"
    )

hwCGCdrMemOverloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 3)
)
hwCGCdrMemOverloadTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectCG"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGCdrCachePoolUsed"))
)
if mibBuilder.loadTexts:
    hwCGCdrMemOverloadTrap.setStatus(
        "current"
    )

hwCGCdrMemChangeToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 4)
)
hwCGCdrMemChangeToNormalTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectCG"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGCdrCachePoolUsed"))
)
if mibBuilder.loadTexts:
    hwCGCdrMemChangeToNormalTrap.setStatus(
        "current"
    )

hwCGCdrPoolFullTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 5)
)
hwCGCdrPoolFullTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectCG"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGCdrCachePoolUsed"))
)
if mibBuilder.loadTexts:
    hwCGCdrPoolFullTrap.setStatus(
        "current"
    )

hwCGCdrPoolFullClearedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 6)
)
hwCGCdrPoolFullClearedTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectCG"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGCdrCachePoolUsed"))
)
if mibBuilder.loadTexts:
    hwCGCdrPoolFullClearedTrap.setStatus(
        "current"
    )

hwPCRFConnectDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 7)
)
hwPCRFConnectDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectPCRF"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFHostName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASNameConnectPCRF"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASIPAddressConnectPCRF"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASPortConnectPCRF"))
)
if mibBuilder.loadTexts:
    hwPCRFConnectDownTrap.setStatus(
        "current"
    )

hwPCRFConnectUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 8)
)
hwPCRFConnectUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectPCRF"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFHostName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASNameConnectPCRF"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASIPAddressConnectPCRF"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASPortConnectPCRF"))
)
if mibBuilder.loadTexts:
    hwPCRFConnectUpTrap.setStatus(
        "current"
    )

hwOCSConnectDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 9)
)
hwOCSConnectDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectOCS"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSHostName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASNameConnectOCS"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASIPAddressConnectOCS"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASPortConnectOCS"))
)
if mibBuilder.loadTexts:
    hwOCSConnectDownTrap.setStatus(
        "current"
    )

hwOCSConnectUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 10)
)
hwOCSConnectUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectOCS"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSHostName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASNameConnectOCS"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASIPAddressConnectOCS"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASPortConnectOCS"))
)
if mibBuilder.loadTexts:
    hwOCSConnectUpTrap.setStatus(
        "current"
    )

hwDRAConnectDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 11)
)
hwDRAConnectDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectDRA"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAHostName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASNameConnectDRA"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASIPAddressConnectDRA"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASPortConnectDRA"))
)
if mibBuilder.loadTexts:
    hwDRAConnectDownTrap.setStatus(
        "current"
    )

hwDRAConnectUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 4, 12)
)
hwDRAConnectUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSASLocationConnectDRA"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAHostName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAPort"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASNameConnectDRA"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASIPAddressConnectDRA"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSASPortConnectDRA"))
)
if mibBuilder.loadTexts:
    hwDRAConnectUpTrap.setStatus(
        "current"
    )

hwCpuBeyondThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 1)
)
hwCpuBeyondThresholdTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceVcpuId"))
)
if mibBuilder.loadTexts:
    hwCpuBeyondThresholdTrap.setStatus(
        "current"
    )

hwCpuChangeToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 2)
)
hwCpuChangeToNormalTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceUsage"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceVcpuId"))
)
if mibBuilder.loadTexts:
    hwCpuChangeToNormalTrap.setStatus(
        "current"
    )

hwMemoryBeyondThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 3)
)
hwMemoryBeyondThresholdTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceUsage"))
)
if mibBuilder.loadTexts:
    hwMemoryBeyondThresholdTrap.setStatus(
        "current"
    )

hwMemoryChangeToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 4)
)
hwMemoryChangeToNormalTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceType"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceUsage"))
)
if mibBuilder.loadTexts:
    hwMemoryChangeToNormalTrap.setStatus(
        "current"
    )

hwCollectorConnectDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 5)
)
hwCollectorConnectDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCollectorIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCollectorPort"))
)
if mibBuilder.loadTexts:
    hwCollectorConnectDownTrap.setStatus(
        "current"
    )

hwCollectorConnectUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 6)
)
hwCollectorConnectUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCollectorIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCollectorPort"))
)
if mibBuilder.loadTexts:
    hwCollectorConnectUpTrap.setStatus(
        "current"
    )

hwHashModeInconsistentTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 7)
)
hwHashModeInconsistentTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwInterfaceList"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"))
)
if mibBuilder.loadTexts:
    hwHashModeInconsistentTrap.setStatus(
        "current"
    )

hwHashModeInconsistentRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 8)
)
hwHashModeInconsistentRecoverTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwRecoverTrapCause"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"))
)
if mibBuilder.loadTexts:
    hwHashModeInconsistentRecoverTrap.setStatus(
        "current"
    )

hwSpammerFTPDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 9)
)
hwSpammerFTPDownTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpammerFTPServeIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpammerFTPServePort"))
)
if mibBuilder.loadTexts:
    hwSpammerFTPDownTrap.setStatus(
        "current"
    )

hwSpammerFTPUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 10)
)
hwSpammerFTPUpTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpammerFTPServeIP"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpammerFTPServePort"))
)
if mibBuilder.loadTexts:
    hwSpammerFTPUpTrap.setStatus(
        "current"
    )

hwIPDbtOverLoadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 11)
)
hwIPDbtOverLoadTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation")
)
if mibBuilder.loadTexts:
    hwIPDbtOverLoadTrap.setStatus(
        "current"
    )

hwIPDbtOverLoadRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 12)
)
hwIPDbtOverLoadRecoverTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwServiceResourceLocation")
)
if mibBuilder.loadTexts:
    hwIPDbtOverLoadRecoverTrap.setStatus(
        "current"
    )

hwCABeforeExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 13)
)
hwCABeforeExpiredTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCAExpireTime"))
)
if mibBuilder.loadTexts:
    hwCABeforeExpiredTrap.setStatus(
        "current"
    )

hwCAExpiredTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 7, 2, 14)
)
hwCAExpiredTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwClusterNodeIPAddress"))
)
if mibBuilder.loadTexts:
    hwCAExpiredTrap.setStatus(
        "current"
    )

hwNeedResetForFeatureLoadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 8, 2, 1)
)
hwNeedResetForFeatureLoadTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwExtendedFeatureLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwExtendedFeatureType"))
)
if mibBuilder.loadTexts:
    hwNeedResetForFeatureLoadTrap.setStatus(
        "current"
    )

hwNeedResetForFeatureUnloadTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 8, 2, 3)
)
hwNeedResetForFeatureUnloadTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwExtendedFeatureLocation"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwExtendedFeatureType"))
)
if mibBuilder.loadTexts:
    hwNeedResetForFeatureUnloadTrap.setStatus(
        "current"
    )

hwNeedResetForFdrMemallocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 8, 2, 5)
)
hwNeedResetForFdrMemallocTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwExtendedFeatureLocation")
)
if mibBuilder.loadTexts:
    hwNeedResetForFdrMemallocTrap.setStatus(
        "current"
    )

hwNeedResetForUndoFdrMemallocTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 8, 2, 7)
)
hwNeedResetForUndoFdrMemallocTrap.setObjects(
    ("HUAWEI-SECURITY-SAFE-MIB", "hwExtendedFeatureLocation")
)
if mibBuilder.loadTexts:
    hwNeedResetForUndoFdrMemallocTrap.setStatus(
        "current"
    )

hwSAInstanceStateChangeToAbnormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 9, 2, 1)
)
hwSAInstanceStateChangeToAbnormalTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSAInstanceName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAinstanceCPUTotalNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAinstanceCPUActiveNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAinstanceCPULeastActiveNumber"))
)
if mibBuilder.loadTexts:
    hwSAInstanceStateChangeToAbnormalTrap.setStatus(
        "current"
    )

hwSAInstanceStateChangeToNormalTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 2, 9, 2, 2)
)
hwSAInstanceStateChangeToNormalTrap.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSAInstanceName"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAinstanceCPUTotalNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAinstanceCPUActiveNumber"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAinstanceCPULeastActiveNumber"))
)
if mibBuilder.loadTexts:
    hwSAInstanceStateChangeToNormalTrap.setStatus(
        "current"
    )


# Notifications groups

hwSATrapGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 4, 2, 1)
)
hwSATrapGroup.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwStateChangeToNormalTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwStateChangeToAbnormalTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPeerNodeConnectDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPeerNodeConnectUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNodeModeChangeActiveTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNodeModeChangeStandbyTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNodeCompConnectUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNodeCompConnectDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCpuUsageThresholdTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuMemUsageThresholdTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkAddTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkDeleteTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkConnectDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCompLinkConnectUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkAddTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkDeleteTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsSasLinkUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwResourceNotEnoughTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBWListSyncErrTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuTemperatureThresholdTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLpuOverLoadTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuOverLoadTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGCdrMemChangeToNormalTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGCdrMemOverloadTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGConnectUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGConnectDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassSwitchWorkingMode"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwRadiusSnifferAckOkTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwRadiusSnifferNoAckTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsUcssLinkDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGCdrPoolFullClearedTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLinkBandWidthChangeToEqualTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLinkBandWidthChangeToUnequalTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCGCdrPoolFullTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwMemoryBeyondThresholdTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwMemoryChangeToNormalTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCpuBeyondThresholdTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCpuChangeToNormalTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwConfigurationInconsistentTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBackupGroupStateChangeToBackupTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBackupGroupStateChangeToMasterTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwHotBackupConfigurationCheckFailTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeSuccessfulTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeFailedTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSPSAmountSufficientTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSPSAmountInsufficientTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeLinkStateChangeToAbnormal"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeLinkStateChangeToNormal"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCascadeLinkOverloadTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAFdiConnectDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassLinkSwitchState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSConnectUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwOCSConnectDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFConnectUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPCRFConnectDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwBypassMonitorState"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCollectorConnectUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCollectorConnectDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsRdasLinkUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsRdasLinkDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLinkBoundGroupStateChangeToNormal"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwLinkBoundGroupStateChangeToAbnormal"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuCpuUsageThresholdRestoreTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuMemUsageThresholdRestoreTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuTemperatureThresholdRestoreTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuFlowOverLoadRecoverTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpuFlowOverLoadTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsFragmentEnoughTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsFragmentNotEnoughTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasRpdAccountMessageAbnormalTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNeedResetForFeatureUnloadTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwHashModeVerifyRecoverTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwHashModeVerifyTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwHashModeInconsistentRecoverTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwHashModeInconsistentTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpammerFTPUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpammerFTPDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwIPDbtOverLoadRecoverTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwIPDbtOverLoadTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNeedResetForUndoFdrMemallocTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNeedResetForFdrMemallocTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1HBKEnableSpuNeedResetTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1HBKDisableSpuNeedResetTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1HBKCpuStanbyRecoverTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1HBKCpuStandbyTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1HBKDisableSpuResetRecoverTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNPLUS1HBKEnableSpuResetRecoverTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAConnectUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwDRAConnectDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwForwardingQueueOverloadTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwAverageCpuUsageThresholdTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsLeastNumberBelowTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwForwardingQueueRestoreTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSpsLeastNumberEqualTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwAverageCpuUsageThresholdRestoreTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPlsCompLinkConnectUpTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwPlsCompLinkConnectDownTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCABeforeExpiredTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwCAExpiredTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAInstanceStateChangeToNormalTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAInstanceStateChangeToAbnormalTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwNeedResetForFeatureLoadTrap"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSasRpdAccountMessageNormalTrap"))
)
if mibBuilder.loadTexts:
    hwSATrapGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

hwSAFECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 2011, 6, 122, 20, 4, 1, 1)
)
hwSAFECompliance.setObjects(
      *(("HUAWEI-SECURITY-SAFE-MIB", "hwSATrapGroup"),
        ("HUAWEI-SECURITY-SAFE-MIB", "hwSAObject"))
)
if mibBuilder.loadTexts:
    hwSAFECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HUAWEI-SECURITY-SAFE-MIB",
    **{"huawei": huawei,
       "huaweiUtility": huaweiUtility,
       "hwSecurity": hwSecurity,
       "hwSAFEMIB": hwSAFEMIB,
       "hwDeviceObject": hwDeviceObject,
       "hwSANodeObject": hwSANodeObject,
       "hwSpuSysInfoTable": hwSpuSysInfoTable,
       "hwSpuSysInfoEntry": hwSpuSysInfoEntry,
       "hwSpuSysInfoIndex": hwSpuSysInfoIndex,
       "hwSpuSysInfoLocation": hwSpuSysInfoLocation,
       "hwSpuSysInfoType": hwSpuSysInfoType,
       "hwSpuSysInfoIPAddress": hwSpuSysInfoIPAddress,
       "hwSpuSysInfoState": hwSpuSysInfoState,
       "hwServiceLinkTable": hwServiceLinkTable,
       "hwServiceLinkEntry": hwServiceLinkEntry,
       "hwServiceLinkIndex": hwServiceLinkIndex,
       "hwServiceLinkType": hwServiceLinkType,
       "hwServiceLinkName": hwServiceLinkName,
       "hwServiceLinkInsideInterface": hwServiceLinkInsideInterface,
       "hwServiceLinkOutsideInterface": hwServiceLinkOutsideInterface,
       "hwServiceLinkInsideInterfaceState": hwServiceLinkInsideInterfaceState,
       "hwServiceLinkOutsideInterfaceState": hwServiceLinkOutsideInterfaceState,
       "hwServiceLinkInsideInterfaceBandWidth": hwServiceLinkInsideInterfaceBandWidth,
       "hwServiceLinkOutsideInterfaceBandWidth": hwServiceLinkOutsideInterfaceBandWidth,
       "hwServiceLinkBoundGroupNumber": hwServiceLinkBoundGroupNumber,
       "hwCascadeInterfaceTable": hwCascadeInterfaceTable,
       "hwCascadeInterfaceEntry": hwCascadeInterfaceEntry,
       "hwCascadeInterfaceIndex": hwCascadeInterfaceIndex,
       "hwCascadeInterface": hwCascadeInterface,
       "hwCascadeInterfaceStatus": hwCascadeInterfaceStatus,
       "hwSANodeTraps": hwSANodeTraps,
       "hwStateChangeToNormalTrap": hwStateChangeToNormalTrap,
       "hwStateChangeToAbnormalTrap": hwStateChangeToAbnormalTrap,
       "hwLinkBandWidthChangeToUnequalTrap": hwLinkBandWidthChangeToUnequalTrap,
       "hwLinkBandWidthChangeToEqualTrap": hwLinkBandWidthChangeToEqualTrap,
       "hwLinkBoundGroupStateChangeToAbnormal": hwLinkBoundGroupStateChangeToAbnormal,
       "hwLinkBoundGroupStateChangeToNormal": hwLinkBoundGroupStateChangeToNormal,
       "hwCascadeLinkStateChangeToAbnormal": hwCascadeLinkStateChangeToAbnormal,
       "hwCascadeLinkStateChangeToNormal": hwCascadeLinkStateChangeToNormal,
       "hwCascadeLinkOverloadTrap": hwCascadeLinkOverloadTrap,
       "hwSAClusterObject": hwSAClusterObject,
       "hwClusterNodeTable": hwClusterNodeTable,
       "hwClusterNodeEntry": hwClusterNodeEntry,
       "hwClusterNodeIndex": hwClusterNodeIndex,
       "hwClusterNodeName": hwClusterNodeName,
       "hwClusterNodeIPAddress": hwClusterNodeIPAddress,
       "hwClusterNodeRole": hwClusterNodeRole,
       "hwClusterNodeStatus": hwClusterNodeStatus,
       "hwNormalSPSNumber": hwNormalSPSNumber,
       "hwCascadeCfg": hwCascadeCfg,
       "hwCascadePeerState": hwCascadePeerState,
       "hwCascadeSelfState": hwCascadeSelfState,
       "hwClusterSasTable": hwClusterSasTable,
       "hwClusterSasEntry": hwClusterSasEntry,
       "hwClusterSasIndex": hwClusterSasIndex,
       "hwClusterSasNodeNumber": hwClusterSasNodeNumber,
       "hwClusterSasSysLocation": hwClusterSasSysLocation,
       "hwClusterSasSysIPAddress": hwClusterSasSysIPAddress,
       "hwClusterSasMode": hwClusterSasMode,
       "hwClusterMapTable": hwClusterMapTable,
       "hwClusterMapEntry": hwClusterMapEntry,
       "hwClusterMapSasIndex": hwClusterMapSasIndex,
       "hwClusterMapSysSasMode": hwClusterMapSysSasMode,
       "hwClusterMapNumberOfDG": hwClusterMapNumberOfDG,
       "hwClusterMapDevices": hwClusterMapDevices,
       "hwComponentTable": hwComponentTable,
       "hwComponentEntry": hwComponentEntry,
       "hwComponentIndex": hwComponentIndex,
       "hwComponentType": hwComponentType,
       "hwComponentNumber": hwComponentNumber,
       "hwComponentName": hwComponentName,
       "hwComponentPrimaryIPAddress": hwComponentPrimaryIPAddress,
       "hwComponenSecondaryIPAddress": hwComponenSecondaryIPAddress,
       "hwComponentPriIPConnStatus": hwComponentPriIPConnStatus,
       "hwComponentSecIPConnStatus": hwComponentSecIPConnStatus,
       "hwComponentUsageMode": hwComponentUsageMode,
       "hwClusterTraps": hwClusterTraps,
       "hwPeerNodeConnectDownTrap": hwPeerNodeConnectDownTrap,
       "hwPeerNodeConnectUpTrap": hwPeerNodeConnectUpTrap,
       "hwNodeModeChangeActiveTrap": hwNodeModeChangeActiveTrap,
       "hwNodeModeChangeStandbyTrap": hwNodeModeChangeStandbyTrap,
       "hwNodeCompConnectUpTrap": hwNodeCompConnectUpTrap,
       "hwNodeCompConnectDownTrap": hwNodeCompConnectDownTrap,
       "hwConfigurationInconsistentTrap": hwConfigurationInconsistentTrap,
       "hwSPSAmountInsufficientTrap": hwSPSAmountInsufficientTrap,
       "hwSPSAmountSufficientTrap": hwSPSAmountSufficientTrap,
       "hwCascadeFailedTrap": hwCascadeFailedTrap,
       "hwCascadeSuccessfulTrap": hwCascadeSuccessfulTrap,
       "hwHotBackupConfigurationCheckFailTrap": hwHotBackupConfigurationCheckFailTrap,
       "hwInternBypassObject": hwInternBypassObject,
       "hwBypassLinkStateTable": hwBypassLinkStateTable,
       "hwBypassLinkStateEntry": hwBypassLinkStateEntry,
       "hwBypassLinkStateIndex": hwBypassLinkStateIndex,
       "hwBypassLinkStateLink": hwBypassLinkStateLink,
       "hwBypassLinkStateMode": hwBypassLinkStateMode,
       "hwBypassLinkStateChannel0State": hwBypassLinkStateChannel0State,
       "hwBypassLinkStateChannel1State": hwBypassLinkStateChannel1State,
       "hwBypassLinkStateRIsignal": hwBypassLinkStateRIsignal,
       "hwBypassLinkCurrentState": hwBypassLinkCurrentState,
       "hwBypassLinkLosTimes": hwBypassLinkLosTimes,
       "hwBypassLinkLinkTimes": hwBypassLinkLinkTimes,
       "hwBypassSwitchCurrentPosition": hwBypassSwitchCurrentPosition,
       "hwBypassSwitchWorkingTimes": hwBypassSwitchWorkingTimes,
       "hwBypassSwitchProtectionTimes": hwBypassSwitchProtectionTimes,
       "hwBypassSlotNum": hwBypassSlotNum,
       "hwBypassPowerStatus": hwBypassPowerStatus,
       "hwBypassAlarmDescription": hwBypassAlarmDescription,
       "hwInternBypassTraps": hwInternBypassTraps,
       "hwBypassSwitchWorkingMode": hwBypassSwitchWorkingMode,
       "hwBypassLinkState": hwBypassLinkState,
       "hwBypassLinkSwitchState": hwBypassLinkSwitchState,
       "hwBypassMonitorState": hwBypassMonitorState,
       "hwSpuEntityObject": hwSpuEntityObject,
       "hwSpuEntityStateTable": hwSpuEntityStateTable,
       "hwSpuEntityStateEntry": hwSpuEntityStateEntry,
       "hwSpuEntityCpuNumber": hwSpuEntityCpuNumber,
       "hwSpuEntityPhysicalIndex": hwSpuEntityPhysicalIndex,
       "hwSpuEntityLocation": hwSpuEntityLocation,
       "hwSpuEntityCpuUsage": hwSpuEntityCpuUsage,
       "hwSpuEntityCpuUsageThreshold": hwSpuEntityCpuUsageThreshold,
       "hwSpuEntityMemoryUsage": hwSpuEntityMemoryUsage,
       "hwSpuEntityMemoryUsageThreshold": hwSpuEntityMemoryUsageThreshold,
       "hwSpuEntityTemperature": hwSpuEntityTemperature,
       "hwSpuEntityTemperatureThreshold": hwSpuEntityTemperatureThreshold,
       "hwSpuEntityTraps": hwSpuEntityTraps,
       "hwSpuCpuUsageThresholdTrap": hwSpuCpuUsageThresholdTrap,
       "hwSpuCpuUsageThresholdRestoreTrap": hwSpuCpuUsageThresholdRestoreTrap,
       "hwSpuMemUsageThresholdTrap": hwSpuMemUsageThresholdTrap,
       "hwSpuMemUsageThresholdRestoreTrap": hwSpuMemUsageThresholdRestoreTrap,
       "hwSpuTemperatureThresholdTrap": hwSpuTemperatureThresholdTrap,
       "hwSpuTemperatureThresholdRestoreTrap": hwSpuTemperatureThresholdRestoreTrap,
       "hwSpuLpuOverLoadObject": hwSpuLpuOverLoadObject,
       "hwSpuOverLoadInfoTable": hwSpuOverLoadInfoTable,
       "hwSpuOverLoadInfoEntry": hwSpuOverLoadInfoEntry,
       "hwSpuOverLoadInfoIndex": hwSpuOverLoadInfoIndex,
       "hwSpuOverLoadPackages": hwSpuOverLoadPackages,
       "hwSpuOverLoadBytes": hwSpuOverLoadBytes,
       "hwLpuOverLoadInfoTable": hwLpuOverLoadInfoTable,
       "hwLpuOverLoadInfoEntry": hwLpuOverLoadInfoEntry,
       "hwLpuOverLoadInfoIndex": hwLpuOverLoadInfoIndex,
       "hwLpuOverLoadPackages": hwLpuOverLoadPackages,
       "hwLpuOverLoadBytes": hwLpuOverLoadBytes,
       "hwSpuLpuOverLoadTrap": hwSpuLpuOverLoadTrap,
       "hwSpuOverLoadTrap": hwSpuOverLoadTrap,
       "hwLpuOverLoadTrap": hwLpuOverLoadTrap,
       "hwSpuFlowOverLoadObject": hwSpuFlowOverLoadObject,
       "hwSpuFlowOverLoadTable": hwSpuFlowOverLoadTable,
       "hwSpuFlowOverLoadEntry": hwSpuFlowOverLoadEntry,
       "hwSpuFlowOverLoadCpuNumber": hwSpuFlowOverLoadCpuNumber,
       "hwSpuFlowOverLoadPackets": hwSpuFlowOverLoadPackets,
       "hwSpuFlowOverLoadLocation": hwSpuFlowOverLoadLocation,
       "hwSpuFlowOverLoadTraps": hwSpuFlowOverLoadTraps,
       "hwSpuFlowOverLoadTrap": hwSpuFlowOverLoadTrap,
       "hwSpuFlowOverLoadRecoverTrap": hwSpuFlowOverLoadRecoverTrap,
       "hwHashModeVerifyTraps": hwHashModeVerifyTraps,
       "hwHashModeVerifyTrap": hwHashModeVerifyTrap,
       "hwHashModeVerifyRecoverTrap": hwHashModeVerifyRecoverTrap,
       "hwServiceObject": hwServiceObject,
       "hwServiceBasicObject": hwServiceBasicObject,
       "hwResourceUsageTable": hwResourceUsageTable,
       "hwResourceUsageEntry": hwResourceUsageEntry,
       "hwResourceUsageIndex": hwResourceUsageIndex,
       "hwResourceLocation": hwResourceLocation,
       "hwSAResourceType": hwSAResourceType,
       "hwResourceCapacity": hwResourceCapacity,
       "hwResourceUsage": hwResourceUsage,
       "hwResourceLeft": hwResourceLeft,
       "hwSACbbFileTable": hwSACbbFileTable,
       "hwSACbbFileEntry": hwSACbbFileEntry,
       "hwSACbbEntryIndex": hwSACbbEntryIndex,
       "hwSACbbLocation": hwSACbbLocation,
       "hwSACbbVersion": hwSACbbVersion,
       "hwBWListTable": hwBWListTable,
       "hwBWListEntry": hwBWListEntry,
       "hwBWListEntryIndex": hwBWListEntryIndex,
       "hwBWListType": hwBWListType,
       "hwBWListLocation": hwBWListLocation,
       "hwBWListVersion": hwBWListVersion,
       "hwSpsSasLinkTable": hwSpsSasLinkTable,
       "hwSpsSasLinkEntry": hwSpsSasLinkEntry,
       "hwSpsSasLinkIndex": hwSpsSasLinkIndex,
       "hwSpsSasLinkSpsLocation": hwSpsSasLinkSpsLocation,
       "hwSpsSasLinkSasLocation": hwSpsSasLinkSasLocation,
       "hwSpsSasLinkSpsIP": hwSpsSasLinkSpsIP,
       "hwSpsSasLinkSasIP": hwSpsSasLinkSasIP,
       "hwSpsSasLinkStatus": hwSpsSasLinkStatus,
       "hwSpuCompLinkTable": hwSpuCompLinkTable,
       "hwSpuCompLinkEntry": hwSpuCompLinkEntry,
       "hwSpuCompLinkIndex": hwSpuCompLinkIndex,
       "hwSpuCompLinkSysLocation": hwSpuCompLinkSysLocation,
       "hwSpuCompLinkComponentType": hwSpuCompLinkComponentType,
       "hwSpuCompLinkCurrentDestIP": hwSpuCompLinkCurrentDestIP,
       "hwSpuCompLinkCurrentDestPort": hwSpuCompLinkCurrentDestPort,
       "hwSpuCompLinkConnState": hwSpuCompLinkConnState,
       "hwSpuCompLinkNumPacketsSent": hwSpuCompLinkNumPacketsSent,
       "hwSpuCompLinkBytesSent": hwSpuCompLinkBytesSent,
       "hwSpuCompLinkNumPacketsRecv": hwSpuCompLinkNumPacketsRecv,
       "hwSpuCompLinkBytesRecv": hwSpuCompLinkBytesRecv,
       "hwSpuCompLinkNumErrPacketsRecv": hwSpuCompLinkNumErrPacketsRecv,
       "hwSAFdiConnectTable": hwSAFdiConnectTable,
       "hwSAFdiConnectEntry": hwSAFdiConnectEntry,
       "hwSAFdiConnectIndex": hwSAFdiConnectIndex,
       "hwSAFdiConnectLocation": hwSAFdiConnectLocation,
       "hwSysFdiInstanceID": hwSysFdiInstanceID,
       "hwSysFdiDestMasterIP": hwSysFdiDestMasterIP,
       "hwSysFdiDestBackupIP": hwSysFdiDestBackupIP,
       "hwSpsRadisInfoTable": hwSpsRadisInfoTable,
       "hwSpsRadisInfoEntry": hwSpsRadisInfoEntry,
       "hwSpsRadisInfoIndex": hwSpsRadisInfoIndex,
       "hwSnifferInfoLocation": hwSnifferInfoLocation,
       "hwPacketSendCount": hwPacketSendCount,
       "hwPacketErrCount": hwPacketErrCount,
       "hwSnifferSrcIPAddress": hwSnifferSrcIPAddress,
       "hwSnifferDstIPAddress": hwSnifferDstIPAddress,
       "hwSnifferInfoState": hwSnifferInfoState,
       "hwSpsUcssLinkTable": hwSpsUcssLinkTable,
       "hwSpsUcssLinkEntry": hwSpsUcssLinkEntry,
       "hwSpsUcssLinkIndex": hwSpsUcssLinkIndex,
       "hwSpsUcssLinkSpsLocation": hwSpsUcssLinkSpsLocation,
       "hwSpsUcssLinkSpsIP": hwSpsUcssLinkSpsIP,
       "hwSpsUcssLinkUcssIP": hwSpsUcssLinkUcssIP,
       "hwSasMessageNumberTable": hwSasMessageNumberTable,
       "hwSasMessageNumberEntry": hwSasMessageNumberEntry,
       "hwSasMessageNumIndex": hwSasMessageNumIndex,
       "hwSasMessageLocation": hwSasMessageLocation,
       "hwSasIPAddress": hwSasIPAddress,
       "hwSasMessageType": hwSasMessageType,
       "hwSasMessageIpOnLineNum": hwSasMessageIpOnLineNum,
       "hwSasMessageIpOffLineNum": hwSasMessageIpOffLineNum,
       "hwSasMessageAccountOnLineNum": hwSasMessageAccountOnLineNum,
       "hwSasMessageAccountOffLineNum": hwSasMessageAccountOffLineNum,
       "hwSasMessageTotalNum": hwSasMessageTotalNum,
       "hwSpsMessageNumberTable": hwSpsMessageNumberTable,
       "hwSpsMessageNumberEntry": hwSpsMessageNumberEntry,
       "hwSpsMessageNumberIndex": hwSpsMessageNumberIndex,
       "hwSpsMessageNumberLocation": hwSpsMessageNumberLocation,
       "hwSpsIPAddress": hwSpsIPAddress,
       "hwSpsNewFlowNumber": hwSpsNewFlowNumber,
       "hwSpsNewTempFlowNumber": hwSpsNewTempFlowNumber,
       "hwSpsDeleteFlowNumber": hwSpsDeleteFlowNumber,
       "hwBackupGroupTable": hwBackupGroupTable,
       "hwBackupGroupEntry": hwBackupGroupEntry,
       "hwBackupGroupIndex": hwBackupGroupIndex,
       "hwBackupGroupID": hwBackupGroupID,
       "hwLocalClusterNodeID": hwLocalClusterNodeID,
       "hwPeerClusterNodeID": hwPeerClusterNodeID,
       "hwLocalClusterNodeIPAddress": hwLocalClusterNodeIPAddress,
       "hwPeerClusterNodeIPAddress": hwPeerClusterNodeIPAddress,
       "hwBackupGroupLocalSlot": hwBackupGroupLocalSlot,
       "hwBackupGroupPeerSlot": hwBackupGroupPeerSlot,
       "hwBackupGroupLocalState": hwBackupGroupLocalState,
       "hwBackupGroupPeerState": hwBackupGroupPeerState,
       "hwSpsRdasLinkTable": hwSpsRdasLinkTable,
       "hwSpsRdasLinkEntry": hwSpsRdasLinkEntry,
       "hwSpsRdasLinkIndex": hwSpsRdasLinkIndex,
       "hwSpsRdasLinkSpsLocation": hwSpsRdasLinkSpsLocation,
       "hwSpsRdasLinkRdasIP": hwSpsRdasLinkRdasIP,
       "hwSpsFragmentTable": hwSpsFragmentTable,
       "hwSpsFragmentEntry": hwSpsFragmentEntry,
       "hwSpsFragmentIndex": hwSpsFragmentIndex,
       "hwSpsFragmentSpsLocation": hwSpsFragmentSpsLocation,
       "hwSasRpdAccountMessageTable": hwSasRpdAccountMessageTable,
       "hwSasRpdAccountMessageEntry": hwSasRpdAccountMessageEntry,
       "hwSasRpdAccountMessageIndex": hwSasRpdAccountMessageIndex,
       "hwSasRpdAccountMessageLocation": hwSasRpdAccountMessageLocation,
       "hwSasRpdAccountMessageRpdIP": hwSasRpdAccountMessageRpdIP,
       "hwNPLUS1BackupGroupTable": hwNPLUS1BackupGroupTable,
       "hwNPLUS1BackupGroupEntry": hwNPLUS1BackupGroupEntry,
       "hwNPLUS1BackupGroupIndex": hwNPLUS1BackupGroupIndex,
       "hwNPLUS1BackupGroupID": hwNPLUS1BackupGroupID,
       "hwNPLUS1BackupGroupBoardList": hwNPLUS1BackupGroupBoardList,
       "hwNPLUS1BackupGroupBoardType": hwNPLUS1BackupGroupBoardType,
       "hwNPLUS1BackupIsEnable": hwNPLUS1BackupIsEnable,
       "hwLocalBackupGroupStateTable": hwLocalBackupGroupStateTable,
       "hwLocalBackupGroupStateEntry": hwLocalBackupGroupStateEntry,
       "hwLocalBackupGroupStateCpuIndex": hwLocalBackupGroupStateCpuIndex,
       "hwLocalBackupGroupStateCpuLocation": hwLocalBackupGroupStateCpuLocation,
       "hwLocalBackupGroupStateCpuType": hwLocalBackupGroupStateCpuType,
       "hwLocalBackupGroupStateIsEnable": hwLocalBackupGroupStateIsEnable,
       "hwLocalBackupGroupStateGroupId": hwLocalBackupGroupStateGroupId,
       "hwLocalBackupGroupStateSpuType": hwLocalBackupGroupStateSpuType,
       "hwLocalBackupGroupStateCpuMode": hwLocalBackupGroupStateCpuMode,
       "hwLocalBackupGroupIsStandby": hwLocalBackupGroupIsStandby,
       "hwLocalBackupSpuTypeInconsist": hwLocalBackupSpuTypeInconsist,
       "hwSpsLeastNumberTable": hwSpsLeastNumberTable,
       "hwSpsLeastNumberEntry": hwSpsLeastNumberEntry,
       "hwSpsLeastNumberCfg": hwSpsLeastNumberCfg,
       "hwSpsLeastNumberIndex": hwSpsLeastNumberIndex,
       "hwSpsCpuStateTable": hwSpsCpuStateTable,
       "hwSpsCpuStateEntry": hwSpsCpuStateEntry,
       "hwSpsEntityLocation": hwSpsEntityLocation,
       "hwSpsAverageCpuUsage": hwSpsAverageCpuUsage,
       "hwSpsAverageCpuUsageThreshold": hwSpsAverageCpuUsageThreshold,
       "hwSpsQueueUsage": hwSpsQueueUsage,
       "hwSpsOverloadThreshold": hwSpsOverloadThreshold,
       "hwSpsCpuEntityIndex": hwSpsCpuEntityIndex,
       "hwServiceBasicTrap": hwServiceBasicTrap,
       "hwSpuCompLinkAddTrap": hwSpuCompLinkAddTrap,
       "hwSpuCompLinkDeleteTrap": hwSpuCompLinkDeleteTrap,
       "hwSpuCompLinkConnectDownTrap": hwSpuCompLinkConnectDownTrap,
       "hwSpuCompLinkConnectUpTrap": hwSpuCompLinkConnectUpTrap,
       "hwSpsSasLinkAddTrap": hwSpsSasLinkAddTrap,
       "hwSpsSasLinkDeleteTrap": hwSpsSasLinkDeleteTrap,
       "hwSpsSasLinkDownTrap": hwSpsSasLinkDownTrap,
       "hwSpsSasLinkUpTrap": hwSpsSasLinkUpTrap,
       "hwResourceNotEnoughTrap": hwResourceNotEnoughTrap,
       "hwBWListSyncErrTrap": hwBWListSyncErrTrap,
       "hwSAFdiConnectDownTrap": hwSAFdiConnectDownTrap,
       "hwRadiusSnifferNoAckTrap": hwRadiusSnifferNoAckTrap,
       "hwRadiusSnifferAckOkTrap": hwRadiusSnifferAckOkTrap,
       "hwSpsUcssLinkDownTrap": hwSpsUcssLinkDownTrap,
       "hwSpsUcssLinkUpTrap": hwSpsUcssLinkUpTrap,
       "hwBackupGroupStateChangeToMasterTrap": hwBackupGroupStateChangeToMasterTrap,
       "hwBackupGroupStateChangeToBackupTrap": hwBackupGroupStateChangeToBackupTrap,
       "hwSpsRdasLinkDownTrap": hwSpsRdasLinkDownTrap,
       "hwSpsRdasLinkUpTrap": hwSpsRdasLinkUpTrap,
       "hwSpsFragmentNotEnoughTrap": hwSpsFragmentNotEnoughTrap,
       "hwSpsFragmentEnoughTrap": hwSpsFragmentEnoughTrap,
       "hwSasRpdAccountMessageAbnormalTrap": hwSasRpdAccountMessageAbnormalTrap,
       "hwSasRpdAccountMessageNormalTrap": hwSasRpdAccountMessageNormalTrap,
       "hwNPLUS1HBKEnableSpuNeedResetTrap": hwNPLUS1HBKEnableSpuNeedResetTrap,
       "hwNPLUS1HBKEnableSpuResetRecoverTrap": hwNPLUS1HBKEnableSpuResetRecoverTrap,
       "hwNPLUS1HBKDisableSpuNeedResetTrap": hwNPLUS1HBKDisableSpuNeedResetTrap,
       "hwNPLUS1HBKDisableSpuResetRecoverTrap": hwNPLUS1HBKDisableSpuResetRecoverTrap,
       "hwNPLUS1HBKCpuStandbyTrap": hwNPLUS1HBKCpuStandbyTrap,
       "hwNPLUS1HBKCpuStanbyRecoverTrap": hwNPLUS1HBKCpuStanbyRecoverTrap,
       "hwPlsCompLinkConnectDownTrap": hwPlsCompLinkConnectDownTrap,
       "hwPlsCompLinkConnectUpTrap": hwPlsCompLinkConnectUpTrap,
       "hwAverageCpuUsageThresholdTrap": hwAverageCpuUsageThresholdTrap,
       "hwAverageCpuUsageThresholdRestoreTrap": hwAverageCpuUsageThresholdRestoreTrap,
       "hwForwardingQueueOverloadTrap": hwForwardingQueueOverloadTrap,
       "hwForwardingQueueRestoreTrap": hwForwardingQueueRestoreTrap,
       "hwSpsLeastNumberBelowTrap": hwSpsLeastNumberBelowTrap,
       "hwSpsLeastNumberEqualTrap": hwSpsLeastNumberEqualTrap,
       "hwServiceWirelessObject": hwServiceWirelessObject,
       "hwCGInfoTable": hwCGInfoTable,
       "hwCGInfoEntry": hwCGInfoEntry,
       "hwCGInfoIndex": hwCGInfoIndex,
       "hwSASLocationConnectCG": hwSASLocationConnectCG,
       "hwCGIPAddress": hwCGIPAddress,
       "hwCGPort": hwCGPort,
       "hwCGGrade": hwCGGrade,
       "hwCGCdrCachePoolUsed": hwCGCdrCachePoolUsed,
       "hwPCRFInfoTable": hwPCRFInfoTable,
       "hwPCRFInfoEntry": hwPCRFInfoEntry,
       "hwPCRFInfoIndex": hwPCRFInfoIndex,
       "hwSASLocationConnectPCRF": hwSASLocationConnectPCRF,
       "hwPCRFHostName": hwPCRFHostName,
       "hwPCRFIPAddress": hwPCRFIPAddress,
       "hwPCRFPort": hwPCRFPort,
       "hwSASNameConnectPCRF": hwSASNameConnectPCRF,
       "hwSASIPAddressConnectPCRF": hwSASIPAddressConnectPCRF,
       "hwSASPortConnectPCRF": hwSASPortConnectPCRF,
       "hwOCSInfoTable": hwOCSInfoTable,
       "hwOCSInfoEntry": hwOCSInfoEntry,
       "hwOCSInfoIndex": hwOCSInfoIndex,
       "hwSASLocationConnectOCS": hwSASLocationConnectOCS,
       "hwOCSHostName": hwOCSHostName,
       "hwOCSIPAddress": hwOCSIPAddress,
       "hwOCSPort": hwOCSPort,
       "hwSASNameConnectOCS": hwSASNameConnectOCS,
       "hwSASIPAddressConnectOCS": hwSASIPAddressConnectOCS,
       "hwSASPortConnectOCS": hwSASPortConnectOCS,
       "hwDRAInfoTable": hwDRAInfoTable,
       "hwDRAInfoEntry": hwDRAInfoEntry,
       "hwDRAInfoIndex": hwDRAInfoIndex,
       "hwSASLocationConnectDRA": hwSASLocationConnectDRA,
       "hwDRAHostName": hwDRAHostName,
       "hwDRAIPAddress": hwDRAIPAddress,
       "hwDRAPort": hwDRAPort,
       "hwSASNameConnectDRA": hwSASNameConnectDRA,
       "hwSASIPAddressConnectDRA": hwSASIPAddressConnectDRA,
       "hwSASPortConnectDRA": hwSASPortConnectDRA,
       "hwSasGxPerformanceTable": hwSasGxPerformanceTable,
       "hwSasGxPerformanceEntry": hwSasGxPerformanceEntry,
       "hwSasGxPerformanceIndex": hwSasGxPerformanceIndex,
       "hwSasGxPerformanceLocation": hwSasGxPerformanceLocation,
       "hwSasIPAddressForGxPerformance": hwSasIPAddressForGxPerformance,
       "hwSasGxTotalSendNumber": hwSasGxTotalSendNumber,
       "hwSasGxTotalRecieveNumber": hwSasGxTotalRecieveNumber,
       "hwSasGxCCRInitalNumber": hwSasGxCCRInitalNumber,
       "hwSasGxCCAInitalNumber": hwSasGxCCAInitalNumber,
       "hwSasGxCCRUpdateNumber": hwSasGxCCRUpdateNumber,
       "hwSasGxCCAUpdateNumber": hwSasGxCCAUpdateNumber,
       "hwSasGxCCRTerminateNumber": hwSasGxCCRTerminateNumber,
       "hwSasGxCCATerminateNumber": hwSasGxCCATerminateNumber,
       "hwSasGxRARNumber": hwSasGxRARNumber,
       "hwSasGxRAANumber": hwSasGxRAANumber,
       "hwSasGxASRNumber": hwSasGxASRNumber,
       "hwSasGxASANumber": hwSasGxASANumber,
       "hwSasGxErrorTable": hwSasGxErrorTable,
       "hwSasGxErrorEntry": hwSasGxErrorEntry,
       "hwSasGxErrorIndex": hwSasGxErrorIndex,
       "hwSasGxErrorLocation": hwSasGxErrorLocation,
       "hwSasIPAddressForGxError": hwSasIPAddressForGxError,
       "hwGxCommunitionInterruptedTimes": hwGxCommunitionInterruptedTimes,
       "hwSasGxCCRInitalRetransmissions": hwSasGxCCRInitalRetransmissions,
       "hwSasGxCCRUpdateRetransmissions": hwSasGxCCRUpdateRetransmissions,
       "hwSasGxCCRTerminateRetransmissions": hwSasGxCCRTerminateRetransmissions,
       "hwSasGyPerformanceTable": hwSasGyPerformanceTable,
       "hwSasGyPerformanceEntry": hwSasGyPerformanceEntry,
       "hwSasGyPerformanceIndex": hwSasGyPerformanceIndex,
       "hwSasGyPerformanceLocation": hwSasGyPerformanceLocation,
       "hwSasIPAddressForGyPerformance": hwSasIPAddressForGyPerformance,
       "hwSasGyTotalSendNumber": hwSasGyTotalSendNumber,
       "hwSasGyTotalRecieveNumber": hwSasGyTotalRecieveNumber,
       "hwSasGyCCRInitalNumber": hwSasGyCCRInitalNumber,
       "hwSasGyCCAInitalNumber": hwSasGyCCAInitalNumber,
       "hwSasGyCCRUpdateNumber": hwSasGyCCRUpdateNumber,
       "hwSasGyCCAUpdateNumber": hwSasGyCCAUpdateNumber,
       "hwSasGyCCRTerminateNumber": hwSasGyCCRTerminateNumber,
       "hwSasGyCCATerminateNumber": hwSasGyCCATerminateNumber,
       "hwSasGyRARNumber": hwSasGyRARNumber,
       "hwSasGyRAANumber": hwSasGyRAANumber,
       "hwSasGyASRNumber": hwSasGyASRNumber,
       "hwSasGyASANumber": hwSasGyASANumber,
       "hwSasGyErrorTable": hwSasGyErrorTable,
       "hwSasGyErrorEntry": hwSasGyErrorEntry,
       "hwSasGyErrorIndex": hwSasGyErrorIndex,
       "hwSasGyErrorLocation": hwSasGyErrorLocation,
       "hwSasIPAddressForGyError": hwSasIPAddressForGyError,
       "hwGyCommunitionInterruptedTimes": hwGyCommunitionInterruptedTimes,
       "hwSasGyCCRInitalRetransmissions": hwSasGyCCRInitalRetransmissions,
       "hwSasGyCCRUpdateRetransmissions": hwSasGyCCRUpdateRetransmissions,
       "hwSasGyCCRTerminateRetransmissions": hwSasGyCCRTerminateRetransmissions,
       "hwOcsFaultDeactiveNumber": hwOcsFaultDeactiveNumber,
       "hwGyType1ResultCode": hwGyType1ResultCode,
       "hwGyType2ResultCode": hwGyType2ResultCode,
       "hwGyType3ResultCode": hwGyType3ResultCode,
       "hwGyType4ResultCode": hwGyType4ResultCode,
       "hwGyType5ResultCode": hwGyType5ResultCode,
       "hwSasGzPerformanceTable": hwSasGzPerformanceTable,
       "hwSasGzPerformanceEntry": hwSasGzPerformanceEntry,
       "hwSasGzPerformanceIndex": hwSasGzPerformanceIndex,
       "hwSasGzPerformanceLocation": hwSasGzPerformanceLocation,
       "hwSasIPAddressForGzPerformance": hwSasIPAddressForGzPerformance,
       "hwSasGzSendCDRNumber": hwSasGzSendCDRNumber,
       "hwSasGzErrorTable": hwSasGzErrorTable,
       "hwSasGzErrorEntry": hwSasGzErrorEntry,
       "hwSasGzErrorIndex": hwSasGzErrorIndex,
       "hwSasGzErrorLocation": hwSasGzErrorLocation,
       "hwSasIPAddressForGzError": hwSasIPAddressForGzError,
       "hwGzCommunitionInterruptedTimes": hwGzCommunitionInterruptedTimes,
       "hwSasGzAbnormalSignalingNumber": hwSasGzAbnormalSignalingNumber,
       "hwSpsLinkBandwidthTable": hwSpsLinkBandwidthTable,
       "hwSpsLinkBandwidthEntry": hwSpsLinkBandwidthEntry,
       "hwSpsLinkBandwidthIndex": hwSpsLinkBandwidthIndex,
       "hwSpsLinkId": hwSpsLinkId,
       "hwSPSLinkLocation": hwSPSLinkLocation,
       "hwUpstreamPassedBandwidth": hwUpstreamPassedBandwidth,
       "hwDownstreamPassedBandwidth": hwDownstreamPassedBandwidth,
       "hwUpstreamDiscardedBandwidth": hwUpstreamDiscardedBandwidth,
       "hwDownstreamDiscardedBandwidth": hwDownstreamDiscardedBandwidth,
       "hwServiceWirelessTrap": hwServiceWirelessTrap,
       "hwCGConnectDownTrap": hwCGConnectDownTrap,
       "hwCGConnectUpTrap": hwCGConnectUpTrap,
       "hwCGCdrMemOverloadTrap": hwCGCdrMemOverloadTrap,
       "hwCGCdrMemChangeToNormalTrap": hwCGCdrMemChangeToNormalTrap,
       "hwCGCdrPoolFullTrap": hwCGCdrPoolFullTrap,
       "hwCGCdrPoolFullClearedTrap": hwCGCdrPoolFullClearedTrap,
       "hwPCRFConnectDownTrap": hwPCRFConnectDownTrap,
       "hwPCRFConnectUpTrap": hwPCRFConnectUpTrap,
       "hwOCSConnectDownTrap": hwOCSConnectDownTrap,
       "hwOCSConnectUpTrap": hwOCSConnectUpTrap,
       "hwDRAConnectDownTrap": hwDRAConnectDownTrap,
       "hwDRAConnectUpTrap": hwDRAConnectUpTrap,
       "hwServiceVoIPObject": hwServiceVoIPObject,
       "hwServiceDDoSObject": hwServiceDDoSObject,
       "hwServiceTrap": hwServiceTrap,
       "hwServiceTrapVB": hwServiceTrapVB,
       "hwServiceResourceLocation": hwServiceResourceLocation,
       "hwServiceResourceType": hwServiceResourceType,
       "hwServiceResourceUsage": hwServiceResourceUsage,
       "hwServiceResourceVcpuId": hwServiceResourceVcpuId,
       "hwCollectorIP": hwCollectorIP,
       "hwCollectorPort": hwCollectorPort,
       "hwInterfaceList": hwInterfaceList,
       "hwRecoverTrapCause": hwRecoverTrapCause,
       "hwSpammerFTPServeIP": hwSpammerFTPServeIP,
       "hwSpammerFTPServePort": hwSpammerFTPServePort,
       "hwCAExpireTime": hwCAExpireTime,
       "hwServiceTrapConfig": hwServiceTrapConfig,
       "hwCpuBeyondThresholdTrap": hwCpuBeyondThresholdTrap,
       "hwCpuChangeToNormalTrap": hwCpuChangeToNormalTrap,
       "hwMemoryBeyondThresholdTrap": hwMemoryBeyondThresholdTrap,
       "hwMemoryChangeToNormalTrap": hwMemoryChangeToNormalTrap,
       "hwCollectorConnectDownTrap": hwCollectorConnectDownTrap,
       "hwCollectorConnectUpTrap": hwCollectorConnectUpTrap,
       "hwHashModeInconsistentTrap": hwHashModeInconsistentTrap,
       "hwHashModeInconsistentRecoverTrap": hwHashModeInconsistentRecoverTrap,
       "hwSpammerFTPDownTrap": hwSpammerFTPDownTrap,
       "hwSpammerFTPUpTrap": hwSpammerFTPUpTrap,
       "hwIPDbtOverLoadTrap": hwIPDbtOverLoadTrap,
       "hwIPDbtOverLoadRecoverTrap": hwIPDbtOverLoadRecoverTrap,
       "hwCABeforeExpiredTrap": hwCABeforeExpiredTrap,
       "hwCAExpiredTrap": hwCAExpiredTrap,
       "hwExtendedFeatureTrap": hwExtendedFeatureTrap,
       "hwExtendedFeatureTrapVB": hwExtendedFeatureTrapVB,
       "hwExtendedFeatureLocation": hwExtendedFeatureLocation,
       "hwExtendedFeatureType": hwExtendedFeatureType,
       "hwExtendedModuleTrapConfig": hwExtendedModuleTrapConfig,
       "hwNeedResetForFeatureLoadTrap": hwNeedResetForFeatureLoadTrap,
       "hwNeedResetForFeatureUnloadTrap": hwNeedResetForFeatureUnloadTrap,
       "hwNeedResetForFdrMemallocTrap": hwNeedResetForFdrMemallocTrap,
       "hwNeedResetForUndoFdrMemallocTrap": hwNeedResetForUndoFdrMemallocTrap,
       "hwSAInstanceTrap": hwSAInstanceTrap,
       "hwSAInstanceTrapVB": hwSAInstanceTrapVB,
       "hwSAInstanceName": hwSAInstanceName,
       "hwSAinstanceCPUTotalNumber": hwSAinstanceCPUTotalNumber,
       "hwSAinstanceCPUActiveNumber": hwSAinstanceCPUActiveNumber,
       "hwSAinstanceCPULeastActiveNumber": hwSAinstanceCPULeastActiveNumber,
       "hwSAInstanceTrapConfig": hwSAInstanceTrapConfig,
       "hwSAInstanceStateChangeToAbnormalTrap": hwSAInstanceStateChangeToAbnormalTrap,
       "hwSAInstanceStateChangeToNormalTrap": hwSAInstanceStateChangeToNormalTrap,
       "hwSALicense": hwSALicense,
       "hwLicenseTable": hwLicenseTable,
       "hwLicenseEntry": hwLicenseEntry,
       "hwLicenseServiceID": hwLicenseServiceID,
       "hwActiveSpsNumber": hwActiveSpsNumber,
       "hwEnabledFunction": hwEnabledFunction,
       "hwSALicenseTraps": hwSALicenseTraps,
       "hwSAConformance": hwSAConformance,
       "hwSACompliances": hwSACompliances,
       "hwSAFECompliance": hwSAFECompliance,
       "hwSAGroups": hwSAGroups,
       "hwSATrapGroup": hwSATrapGroup,
       "hwSAObject": hwSAObject}
)
