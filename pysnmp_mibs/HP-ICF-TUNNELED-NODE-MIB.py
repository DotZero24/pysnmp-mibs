# SNMP MIB module (HP-ICF-TUNNELED-NODE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HP-ICF-TUNNELED-NODE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:43:36 2025
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(VidList,) = mibBuilder.importSymbols(
    "HP-ICF-TC",
    "VidList")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

hpicfTunneledNode = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128)
)
if mibBuilder.loadTexts:
    hpicfTunneledNode.setRevisions(
        ("2021-06-12 00:00",
         "2018-05-23 00:00",
         "2018-05-22 00:00",
         "2016-12-06 00:00",
         "2016-08-05 00:00",
         "2016-02-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfTunneledNodeObjects_ObjectIdentity = ObjectIdentity
hpicfTunneledNodeObjects = _HpicfTunneledNodeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1)
)
_HpicfTunneledNodeConfig_ObjectIdentity = ObjectIdentity
hpicfTunneledNodeConfig = _HpicfTunneledNodeConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1)
)
_HpicfTunneledNodeTable_Object = MibTable
hpicfTunneledNodeTable = _HpicfTunneledNodeTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1)
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeTable.setStatus("current")
_HpicfTunneledNodeEntry_Object = MibTableRow
hpicfTunneledNodeEntry = _HpicfTunneledNodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1)
)
hpicfTunneledNodeEntry.setIndexNames(
    (0, "HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeIndex"),
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeEntry.setStatus("current")
_HpicfTunneledNodeIndex_Type = Unsigned32
_HpicfTunneledNodeIndex_Object = MibTableColumn
hpicfTunneledNodeIndex = _HpicfTunneledNodeIndex_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 1),
    _HpicfTunneledNodeIndex_Type()
)
hpicfTunneledNodeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTunneledNodeIndex.setStatus("current")
_HpicfTunneledNodeEnable_Type = TruthValue
_HpicfTunneledNodeEnable_Object = MibTableColumn
hpicfTunneledNodeEnable = _HpicfTunneledNodeEnable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 2),
    _HpicfTunneledNodeEnable_Type()
)
hpicfTunneledNodeEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeEnable.setStatus("current")
_HpicfTunneledNodePrimaryAddrType_Type = InetAddressType
_HpicfTunneledNodePrimaryAddrType_Object = MibTableColumn
hpicfTunneledNodePrimaryAddrType = _HpicfTunneledNodePrimaryAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 3),
    _HpicfTunneledNodePrimaryAddrType_Type()
)
hpicfTunneledNodePrimaryAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePrimaryAddrType.setStatus("current")
_HpicfTunneledNodePrimaryAddr_Type = InetAddress
_HpicfTunneledNodePrimaryAddr_Object = MibTableColumn
hpicfTunneledNodePrimaryAddr = _HpicfTunneledNodePrimaryAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 4),
    _HpicfTunneledNodePrimaryAddr_Type()
)
hpicfTunneledNodePrimaryAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePrimaryAddr.setStatus("current")
_HpicfTunneledNodeBackupAddrType_Type = InetAddressType
_HpicfTunneledNodeBackupAddrType_Object = MibTableColumn
hpicfTunneledNodeBackupAddrType = _HpicfTunneledNodeBackupAddrType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 5),
    _HpicfTunneledNodeBackupAddrType_Type()
)
hpicfTunneledNodeBackupAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeBackupAddrType.setStatus("current")
_HpicfTunneledNodeBackupAddr_Type = InetAddress
_HpicfTunneledNodeBackupAddr_Object = MibTableColumn
hpicfTunneledNodeBackupAddr = _HpicfTunneledNodeBackupAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 6),
    _HpicfTunneledNodeBackupAddr_Type()
)
hpicfTunneledNodeBackupAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeBackupAddr.setStatus("current")


class _HpicfTunneledNodeTimeout_Type(Unsigned32):
    """Custom type hpicfTunneledNodeTimeout based on Unsigned32"""
    defaultValue = 8


_HpicfTunneledNodeTimeout_Type.__name__ = "Unsigned32"
_HpicfTunneledNodeTimeout_Object = MibTableColumn
hpicfTunneledNodeTimeout = _HpicfTunneledNodeTimeout_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 7),
    _HpicfTunneledNodeTimeout_Type()
)
hpicfTunneledNodeTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeTimeout.setStatus("current")
_HpicfTunneledNodeRowStatus_Type = RowStatus
_HpicfTunneledNodeRowStatus_Object = MibTableColumn
hpicfTunneledNodeRowStatus = _HpicfTunneledNodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 8),
    _HpicfTunneledNodeRowStatus_Type()
)
hpicfTunneledNodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeRowStatus.setStatus("current")


class _HpicfTunneledNodeMode_Type(Integer32):
    """Custom type hpicfTunneledNodeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portbased", 1),
          ("rolebased", 2))
    )


_HpicfTunneledNodeMode_Type.__name__ = "Integer32"
_HpicfTunneledNodeMode_Object = MibTableColumn
hpicfTunneledNodeMode = _HpicfTunneledNodeMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 9),
    _HpicfTunneledNodeMode_Type()
)
hpicfTunneledNodeMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeMode.setStatus("current")


class _HpicfTunneledNodeVlanMode_Type(Integer32):
    """Custom type hpicfTunneledNodeVlanMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("vlanextend", 1),
          ("novlan", 2))
    )


_HpicfTunneledNodeVlanMode_Type.__name__ = "Integer32"
_HpicfTunneledNodeVlanMode_Object = MibTableColumn
hpicfTunneledNodeVlanMode = _HpicfTunneledNodeVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 10),
    _HpicfTunneledNodeVlanMode_Type()
)
hpicfTunneledNodeVlanMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeVlanMode.setStatus("current")
_HpicfTunneledNodeReservedVlanId_Type = VlanIndex
_HpicfTunneledNodeReservedVlanId_Object = MibTableColumn
hpicfTunneledNodeReservedVlanId = _HpicfTunneledNodeReservedVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 11),
    _HpicfTunneledNodeReservedVlanId_Type()
)
hpicfTunneledNodeReservedVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeReservedVlanId.setStatus("current")


class _HpicfTunneledNodeMPeriod_Type(Integer32):
    """Custom type hpicfTunneledNodeMPeriod based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 720),
    )


_HpicfTunneledNodeMPeriod_Type.__name__ = "Integer32"
_HpicfTunneledNodeMPeriod_Object = MibTableColumn
hpicfTunneledNodeMPeriod = _HpicfTunneledNodeMPeriod_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 12),
    _HpicfTunneledNodeMPeriod_Type()
)
hpicfTunneledNodeMPeriod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeMPeriod.setStatus("current")
if mibBuilder.loadTexts:
    hpicfTunneledNodeMPeriod.setUnits("hour")
_HpicfTunneledNodeWolVIDList_Type = VidList
_HpicfTunneledNodeWolVIDList_Object = MibTableColumn
hpicfTunneledNodeWolVIDList = _HpicfTunneledNodeWolVIDList_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 1, 1, 13),
    _HpicfTunneledNodeWolVIDList_Type()
)
hpicfTunneledNodeWolVIDList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeWolVIDList.setStatus("current")
_HpicfTunneledNodePortConfigTable_Object = MibTable
hpicfTunneledNodePortConfigTable = _HpicfTunneledNodePortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePortConfigTable.setStatus("current")
_HpicfTunneledNodePortConfigEntry_Object = MibTableRow
hpicfTunneledNodePortConfigEntry = _HpicfTunneledNodePortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 2, 1)
)
hpicfTunneledNodePortConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePortConfigEntry.setStatus("current")
_HpicfTunneledNodePortRowStatus_Type = RowStatus
_HpicfTunneledNodePortRowStatus_Object = MibTableColumn
hpicfTunneledNodePortRowStatus = _HpicfTunneledNodePortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 2, 1, 1),
    _HpicfTunneledNodePortRowStatus_Type()
)
hpicfTunneledNodePortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePortRowStatus.setStatus("current")
_HpicfTunneledNodeFallbackLclSw_Type = TruthValue
_HpicfTunneledNodeFallbackLclSw_Object = MibTableColumn
hpicfTunneledNodeFallbackLclSw = _HpicfTunneledNodeFallbackLclSw_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 2, 1, 2),
    _HpicfTunneledNodeFallbackLclSw_Type()
)
hpicfTunneledNodeFallbackLclSw.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodeFallbackLclSw.setStatus("current")


class _HpicfTunneledNodeClearStats_Type(TruthValue):
    """Custom type hpicfTunneledNodeClearStats based on TruthValue"""
    defaultValue = 2


_HpicfTunneledNodeClearStats_Type.__name__ = "TruthValue"
_HpicfTunneledNodeClearStats_Object = MibScalar
hpicfTunneledNodeClearStats = _HpicfTunneledNodeClearStats_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 3),
    _HpicfTunneledNodeClearStats_Type()
)
hpicfTunneledNodeClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfTunneledNodeClearStats.setStatus("current")
_HpicfTunneledNodePapiTable_Object = MibTable
hpicfTunneledNodePapiTable = _HpicfTunneledNodePapiTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiTable.setStatus("current")
_HpicfTunneledNodePapiEntry_Object = MibTableRow
hpicfTunneledNodePapiEntry = _HpicfTunneledNodePapiEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4, 1)
)
hpicfTunneledNodePapiEntry.setIndexNames(
    (0, "HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiAuthMode"),
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiEntry.setStatus("current")


class _HpicfTunneledNodePapiAuthMode_Type(Integer32):
    """Custom type hpicfTunneledNodePapiAuthMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("md5", 2))
    )


_HpicfTunneledNodePapiAuthMode_Type.__name__ = "Integer32"
_HpicfTunneledNodePapiAuthMode_Object = MibTableColumn
hpicfTunneledNodePapiAuthMode = _HpicfTunneledNodePapiAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4, 1, 1),
    _HpicfTunneledNodePapiAuthMode_Type()
)
hpicfTunneledNodePapiAuthMode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiAuthMode.setStatus("current")


class _HpicfTunneledNodePapiKeyValue_Type(OctetString):
    """Custom type hpicfTunneledNodePapiKeyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_HpicfTunneledNodePapiKeyValue_Type.__name__ = "OctetString"
_HpicfTunneledNodePapiKeyValue_Object = MibTableColumn
hpicfTunneledNodePapiKeyValue = _HpicfTunneledNodePapiKeyValue_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4, 1, 2),
    _HpicfTunneledNodePapiKeyValue_Type()
)
hpicfTunneledNodePapiKeyValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiKeyValue.setStatus("current")


class _HpicfTunneledNodePapiKeyEncr_Type(OctetString):
    """Custom type hpicfTunneledNodePapiKeyEncr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_HpicfTunneledNodePapiKeyEncr_Type.__name__ = "OctetString"
_HpicfTunneledNodePapiKeyEncr_Object = MibTableColumn
hpicfTunneledNodePapiKeyEncr = _HpicfTunneledNodePapiKeyEncr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4, 1, 3),
    _HpicfTunneledNodePapiKeyEncr_Type()
)
hpicfTunneledNodePapiKeyEncr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiKeyEncr.setStatus("current")
_HpicfTunneledNodePapiRowStatus_Type = RowStatus
_HpicfTunneledNodePapiRowStatus_Object = MibTableColumn
hpicfTunneledNodePapiRowStatus = _HpicfTunneledNodePapiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 1, 1, 4, 1, 4),
    _HpicfTunneledNodePapiRowStatus_Type()
)
hpicfTunneledNodePapiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiRowStatus.setStatus("current")
_HpicfTunneledNodeConformance_ObjectIdentity = ObjectIdentity
hpicfTunneledNodeConformance = _HpicfTunneledNodeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2)
)
_HpicfTunneledNodeCompliances_ObjectIdentity = ObjectIdentity
hpicfTunneledNodeCompliances = _HpicfTunneledNodeCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 1)
)
_HpicfTunneledNodeGroups_ObjectIdentity = ObjectIdentity
hpicfTunneledNodeGroups = _HpicfTunneledNodeGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2)
)

# Managed Objects groups

hpicfTunneledNodeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 1)
)
hpicfTunneledNodeGroup.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeEnable"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeTimeout"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeRowStatus"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeClearStats"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeGroup.setStatus("deprecated")

hpicfTunneledNodePortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 2)
)
hpicfTunneledNodePortGroup.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePortRowStatus"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeFallbackLclSw"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePortGroup.setStatus("current")

hpicfTunneledNodePapiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 3)
)
hpicfTunneledNodePapiGroup.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiKeyValue"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiKeyEncr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodePapiGroup.setStatus("current")

hpicfTunneledNodeGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 4)
)
hpicfTunneledNodeGroup1.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeEnable"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeTimeout"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeRowStatus"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeClearStats"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeMode"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeVlanMode"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeReservedVlanId"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeGroup1.setStatus("deprecated")

hpicfTunneledNodeGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 5)
)
hpicfTunneledNodeGroup2.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeEnable"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeTimeout"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeRowStatus"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeClearStats"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeMode"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeVlanMode"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeReservedVlanId"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeGroup2.setStatus("deprecated")

hpicfTunneledNodeGroup3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 6)
)
hpicfTunneledNodeGroup3.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeEnable"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeTimeout"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeRowStatus"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeClearStats"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeMode"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeVlanMode"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeReservedVlanId"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeMPeriod"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeGroup3.setStatus("deprecated")

hpicfTunneledNodeGroup4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 2, 7)
)
hpicfTunneledNodeGroup4.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeEnable"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePrimaryAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddrType"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeBackupAddr"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeTimeout"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeRowStatus"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeClearStats"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeMode"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeVlanMode"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeReservedVlanId"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeMPeriod"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeWolVIDList"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeGroup4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfTunneledNodeCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 1, 1)
)
hpicfTunneledNodeCompliance.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeGroup"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePortGroup"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiGroup"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeCompliance.setStatus(
        "deprecated"
    )

hpicfTunneledNodeCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 1, 2)
)
hpicfTunneledNodeCompliance1.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeGroup1"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePortGroup"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiGroup"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeCompliance1.setStatus(
        "deprecated"
    )

hpicfTunneledNodeCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 1, 3)
)
hpicfTunneledNodeCompliance2.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeGroup2"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePortGroup"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiGroup"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeCompliance2.setStatus(
        "deprecated"
    )

hpicfTunneledNodeCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 1, 4)
)
hpicfTunneledNodeCompliance3.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeGroup3"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePortGroup"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiGroup"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeCompliance3.setStatus(
        "deprecated"
    )

hpicfTunneledNodeCompliance4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 128, 2, 1, 5)
)
hpicfTunneledNodeCompliance4.setObjects(
      *(("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodeGroup4"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePortGroup"),
        ("HP-ICF-TUNNELED-NODE-MIB", "hpicfTunneledNodePapiGroup"))
)
if mibBuilder.loadTexts:
    hpicfTunneledNodeCompliance4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-TUNNELED-NODE-MIB",
    **{"hpicfTunneledNode": hpicfTunneledNode,
       "hpicfTunneledNodeObjects": hpicfTunneledNodeObjects,
       "hpicfTunneledNodeConfig": hpicfTunneledNodeConfig,
       "hpicfTunneledNodeTable": hpicfTunneledNodeTable,
       "hpicfTunneledNodeEntry": hpicfTunneledNodeEntry,
       "hpicfTunneledNodeIndex": hpicfTunneledNodeIndex,
       "hpicfTunneledNodeEnable": hpicfTunneledNodeEnable,
       "hpicfTunneledNodePrimaryAddrType": hpicfTunneledNodePrimaryAddrType,
       "hpicfTunneledNodePrimaryAddr": hpicfTunneledNodePrimaryAddr,
       "hpicfTunneledNodeBackupAddrType": hpicfTunneledNodeBackupAddrType,
       "hpicfTunneledNodeBackupAddr": hpicfTunneledNodeBackupAddr,
       "hpicfTunneledNodeTimeout": hpicfTunneledNodeTimeout,
       "hpicfTunneledNodeRowStatus": hpicfTunneledNodeRowStatus,
       "hpicfTunneledNodeMode": hpicfTunneledNodeMode,
       "hpicfTunneledNodeVlanMode": hpicfTunneledNodeVlanMode,
       "hpicfTunneledNodeReservedVlanId": hpicfTunneledNodeReservedVlanId,
       "hpicfTunneledNodeMPeriod": hpicfTunneledNodeMPeriod,
       "hpicfTunneledNodeWolVIDList": hpicfTunneledNodeWolVIDList,
       "hpicfTunneledNodePortConfigTable": hpicfTunneledNodePortConfigTable,
       "hpicfTunneledNodePortConfigEntry": hpicfTunneledNodePortConfigEntry,
       "hpicfTunneledNodePortRowStatus": hpicfTunneledNodePortRowStatus,
       "hpicfTunneledNodeFallbackLclSw": hpicfTunneledNodeFallbackLclSw,
       "hpicfTunneledNodeClearStats": hpicfTunneledNodeClearStats,
       "hpicfTunneledNodePapiTable": hpicfTunneledNodePapiTable,
       "hpicfTunneledNodePapiEntry": hpicfTunneledNodePapiEntry,
       "hpicfTunneledNodePapiAuthMode": hpicfTunneledNodePapiAuthMode,
       "hpicfTunneledNodePapiKeyValue": hpicfTunneledNodePapiKeyValue,
       "hpicfTunneledNodePapiKeyEncr": hpicfTunneledNodePapiKeyEncr,
       "hpicfTunneledNodePapiRowStatus": hpicfTunneledNodePapiRowStatus,
       "hpicfTunneledNodeConformance": hpicfTunneledNodeConformance,
       "hpicfTunneledNodeCompliances": hpicfTunneledNodeCompliances,
       "hpicfTunneledNodeCompliance": hpicfTunneledNodeCompliance,
       "hpicfTunneledNodeCompliance1": hpicfTunneledNodeCompliance1,
       "hpicfTunneledNodeCompliance2": hpicfTunneledNodeCompliance2,
       "hpicfTunneledNodeCompliance3": hpicfTunneledNodeCompliance3,
       "hpicfTunneledNodeCompliance4": hpicfTunneledNodeCompliance4,
       "hpicfTunneledNodeGroups": hpicfTunneledNodeGroups,
       "hpicfTunneledNodeGroup": hpicfTunneledNodeGroup,
       "hpicfTunneledNodePortGroup": hpicfTunneledNodePortGroup,
       "hpicfTunneledNodePapiGroup": hpicfTunneledNodePapiGroup,
       "hpicfTunneledNodeGroup1": hpicfTunneledNodeGroup1,
       "hpicfTunneledNodeGroup2": hpicfTunneledNodeGroup2,
       "hpicfTunneledNodeGroup3": hpicfTunneledNodeGroup3,
       "hpicfTunneledNodeGroup4": hpicfTunneledNodeGroup4}
)
