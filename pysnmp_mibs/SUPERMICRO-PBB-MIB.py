# SNMP MIB module (SUPERMICRO-PBB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-PBB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:03:37 2025
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

(IEEE8021PbbComponentIdentifier,
 IEEE8021PbbIngressEgress,
 IEEE8021PbbServiceIdentifier,
 IEEE8021PbbServiceIdentifierOrUnassigned) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021PbbComponentIdentifier",
    "IEEE8021PbbIngressEgress",
    "IEEE8021PbbServiceIdentifier",
    "IEEE8021PbbServiceIdentifierOrUnassigned")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 RowStatus,
 StorageType,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "StorageType",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsPbbMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14)
)
if mibBuilder.loadTexts:
    fsPbbMib.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsPbbNotifications_ObjectIdentity = ObjectIdentity
fsPbbNotifications = _FsPbbNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 0)
)
_FsPbbObjects_ObjectIdentity = ObjectIdentity
fsPbbObjects = _FsPbbObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1)
)
_FsPbbProviderBackboneBridge_ObjectIdentity = ObjectIdentity
fsPbbProviderBackboneBridge = _FsPbbProviderBackboneBridge_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1)
)
_FsPbbBackboneEdgeBridgeObjects_ObjectIdentity = ObjectIdentity
fsPbbBackboneEdgeBridgeObjects = _FsPbbBackboneEdgeBridgeObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 1)
)
_FsPbbBackboneEdgeBridgeAddress_Type = MacAddress
_FsPbbBackboneEdgeBridgeAddress_Object = MibScalar
fsPbbBackboneEdgeBridgeAddress = _FsPbbBackboneEdgeBridgeAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 1, 1),
    _FsPbbBackboneEdgeBridgeAddress_Type()
)
fsPbbBackboneEdgeBridgeAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbBackboneEdgeBridgeAddress.setStatus("current")


class _FsPbbBackboneEdgeBridgeName_Type(SnmpAdminString):
    """Custom type fsPbbBackboneEdgeBridgeName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsPbbBackboneEdgeBridgeName_Type.__name__ = "SnmpAdminString"
_FsPbbBackboneEdgeBridgeName_Object = MibScalar
fsPbbBackboneEdgeBridgeName = _FsPbbBackboneEdgeBridgeName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 1, 2),
    _FsPbbBackboneEdgeBridgeName_Type()
)
fsPbbBackboneEdgeBridgeName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbBackboneEdgeBridgeName.setStatus("current")
_FsPbbNumberOfIComponents_Type = Unsigned32
_FsPbbNumberOfIComponents_Object = MibScalar
fsPbbNumberOfIComponents = _FsPbbNumberOfIComponents_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 1, 3),
    _FsPbbNumberOfIComponents_Type()
)
fsPbbNumberOfIComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbNumberOfIComponents.setStatus("current")


class _FsPbbNumberOfBComponents_Type(Unsigned32):
    """Custom type fsPbbNumberOfBComponents based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_FsPbbNumberOfBComponents_Type.__name__ = "Unsigned32"
_FsPbbNumberOfBComponents_Object = MibScalar
fsPbbNumberOfBComponents = _FsPbbNumberOfBComponents_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 1, 4),
    _FsPbbNumberOfBComponents_Type()
)
fsPbbNumberOfBComponents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbNumberOfBComponents.setStatus("current")
_FsPbbNumberOfBebPorts_Type = Unsigned32
_FsPbbNumberOfBebPorts_Object = MibScalar
fsPbbNumberOfBebPorts = _FsPbbNumberOfBebPorts_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 1, 5),
    _FsPbbNumberOfBebPorts_Type()
)
fsPbbNumberOfBebPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbNumberOfBebPorts.setStatus("current")
_FsPbbNextAvailablePipIfIndex_Type = InterfaceIndex
_FsPbbNextAvailablePipIfIndex_Object = MibScalar
fsPbbNextAvailablePipIfIndex = _FsPbbNextAvailablePipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 1, 6),
    _FsPbbNextAvailablePipIfIndex_Type()
)
fsPbbNextAvailablePipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbNextAvailablePipIfIndex.setStatus("current")
_FsPbbVipTable_Object = MibTable
fsPbbVipTable = _FsPbbVipTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 2)
)
if mibBuilder.loadTexts:
    fsPbbVipTable.setStatus("current")
_FsPbbVipEntry_Object = MibTableRow
fsPbbVipEntry = _FsPbbVipEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 2, 1)
)
fsPbbVipEntry.setIndexNames(
    (0, "SUPERMICRO-PBB-MIB", "fsdot1ahContextId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsPbbVipEntry.setStatus("current")


class _Fsdot1ahContextId_Type(Integer32):
    """Custom type fsdot1ahContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_Fsdot1ahContextId_Type.__name__ = "Integer32"
_Fsdot1ahContextId_Object = MibTableColumn
fsdot1ahContextId = _Fsdot1ahContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 2, 1, 1),
    _Fsdot1ahContextId_Type()
)
fsdot1ahContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsdot1ahContextId.setStatus("current")


class _FsPbbVipPipIfIndex_Type(InterfaceIndexOrZero):
    """Custom type fsPbbVipPipIfIndex based on InterfaceIndexOrZero"""
    defaultValue = 0


_FsPbbVipPipIfIndex_Type.__name__ = "InterfaceIndexOrZero"
_FsPbbVipPipIfIndex_Object = MibTableColumn
fsPbbVipPipIfIndex = _FsPbbVipPipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 2, 1, 2),
    _FsPbbVipPipIfIndex_Type()
)
fsPbbVipPipIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbVipPipIfIndex.setStatus("current")


class _FsPbbVipISid_Type(IEEE8021PbbServiceIdentifierOrUnassigned):
    """Custom type fsPbbVipISid based on IEEE8021PbbServiceIdentifierOrUnassigned"""
    defaultValue = 1


_FsPbbVipISid_Type.__name__ = "IEEE8021PbbServiceIdentifierOrUnassigned"
_FsPbbVipISid_Object = MibTableColumn
fsPbbVipISid = _FsPbbVipISid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 2, 1, 3),
    _FsPbbVipISid_Type()
)
fsPbbVipISid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbVipISid.setStatus("current")


class _FsPbbVipDefaultDstBMAC_Type(MacAddress):
    """Custom type fsPbbVipDefaultDstBMAC based on MacAddress"""
    defaultHexValue = "001e83000001"


_FsPbbVipDefaultDstBMAC_Type.__name__ = "MacAddress"
_FsPbbVipDefaultDstBMAC_Object = MibTableColumn
fsPbbVipDefaultDstBMAC = _FsPbbVipDefaultDstBMAC_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 2, 1, 4),
    _FsPbbVipDefaultDstBMAC_Type()
)
fsPbbVipDefaultDstBMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPbbVipDefaultDstBMAC.setStatus("current")


class _FsPbbVipType_Type(IEEE8021PbbIngressEgress):
    """Custom type fsPbbVipType based on IEEE8021PbbIngressEgress"""
    defaultHexValue = "03"


_FsPbbVipType_Type.__name__ = "IEEE8021PbbIngressEgress"
_FsPbbVipType_Object = MibTableColumn
fsPbbVipType = _FsPbbVipType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 2, 1, 5),
    _FsPbbVipType_Type()
)
fsPbbVipType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbVipType.setStatus("current")
_FsPbbVipRowStatus_Type = RowStatus
_FsPbbVipRowStatus_Object = MibTableColumn
fsPbbVipRowStatus = _FsPbbVipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 2, 1, 6),
    _FsPbbVipRowStatus_Type()
)
fsPbbVipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbVipRowStatus.setStatus("current")
_FsPbbISidToVipTable_Object = MibTable
fsPbbISidToVipTable = _FsPbbISidToVipTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 3)
)
if mibBuilder.loadTexts:
    fsPbbISidToVipTable.setStatus("current")
_FsPbbISidToVipEntry_Object = MibTableRow
fsPbbISidToVipEntry = _FsPbbISidToVipEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 3, 1)
)
fsPbbISidToVipEntry.setIndexNames(
    (0, "SUPERMICRO-PBB-MIB", "fsPbbISidToVipISid"),
)
if mibBuilder.loadTexts:
    fsPbbISidToVipEntry.setStatus("current")
_FsPbbISidToVipISid_Type = IEEE8021PbbServiceIdentifier
_FsPbbISidToVipISid_Object = MibTableColumn
fsPbbISidToVipISid = _FsPbbISidToVipISid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 3, 1, 1),
    _FsPbbISidToVipISid_Type()
)
fsPbbISidToVipISid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbISidToVipISid.setStatus("current")
_FsPbbISidToVipComponentId_Type = IEEE8021PbbComponentIdentifier
_FsPbbISidToVipComponentId_Object = MibTableColumn
fsPbbISidToVipComponentId = _FsPbbISidToVipComponentId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 3, 1, 2),
    _FsPbbISidToVipComponentId_Type()
)
fsPbbISidToVipComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbISidToVipComponentId.setStatus("current")
_FsPbbISidToVipPort_Type = InterfaceIndex
_FsPbbISidToVipPort_Object = MibTableColumn
fsPbbISidToVipPort = _FsPbbISidToVipPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 3, 1, 3),
    _FsPbbISidToVipPort_Type()
)
fsPbbISidToVipPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbISidToVipPort.setStatus("current")
_FsPbbPipTable_Object = MibTable
fsPbbPipTable = _FsPbbPipTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fsPbbPipTable.setStatus("current")
_FsPbbPipEntry_Object = MibTableRow
fsPbbPipEntry = _FsPbbPipEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 4, 1)
)
fsPbbPipEntry.setIndexNames(
    (0, "SUPERMICRO-PBB-MIB", "fsPbbPipIfIndex"),
)
if mibBuilder.loadTexts:
    fsPbbPipEntry.setStatus("current")
_FsPbbPipIfIndex_Type = InterfaceIndex
_FsPbbPipIfIndex_Object = MibTableColumn
fsPbbPipIfIndex = _FsPbbPipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 4, 1, 1),
    _FsPbbPipIfIndex_Type()
)
fsPbbPipIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbPipIfIndex.setStatus("current")
_FsPbbPipBMACAddress_Type = MacAddress
_FsPbbPipBMACAddress_Object = MibTableColumn
fsPbbPipBMACAddress = _FsPbbPipBMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 4, 1, 2),
    _FsPbbPipBMACAddress_Type()
)
fsPbbPipBMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbPipBMACAddress.setStatus("current")


class _FsPbbPipName_Type(SnmpAdminString):
    """Custom type fsPbbPipName based on SnmpAdminString"""
    defaultHexValue = ""

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FsPbbPipName_Type.__name__ = "SnmpAdminString"
_FsPbbPipName_Object = MibTableColumn
fsPbbPipName = _FsPbbPipName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 4, 1, 3),
    _FsPbbPipName_Type()
)
fsPbbPipName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbPipName.setStatus("current")
_FsPbbPipIComponentId_Type = IEEE8021PbbComponentIdentifier
_FsPbbPipIComponentId_Object = MibTableColumn
fsPbbPipIComponentId = _FsPbbPipIComponentId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 4, 1, 4),
    _FsPbbPipIComponentId_Type()
)
fsPbbPipIComponentId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbPipIComponentId.setStatus("current")
_FsPbbPipRowStatus_Type = RowStatus
_FsPbbPipRowStatus_Object = MibTableColumn
fsPbbPipRowStatus = _FsPbbPipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 4, 1, 5),
    _FsPbbPipRowStatus_Type()
)
fsPbbPipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbPipRowStatus.setStatus("current")
_FsPbbVipToPipMappingTable_Object = MibTable
fsPbbVipToPipMappingTable = _FsPbbVipToPipMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fsPbbVipToPipMappingTable.setStatus("current")
_FsPbbVipToPipMappingEntry_Object = MibTableRow
fsPbbVipToPipMappingEntry = _FsPbbVipToPipMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 5, 1)
)
fsPbbVipToPipMappingEntry.setIndexNames(
    (0, "SUPERMICRO-PBB-MIB", "fsdot1ahContextId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsPbbVipToPipMappingEntry.setStatus("current")
_FsPbbVipToPipMappingPipIfIndex_Type = InterfaceIndex
_FsPbbVipToPipMappingPipIfIndex_Object = MibTableColumn
fsPbbVipToPipMappingPipIfIndex = _FsPbbVipToPipMappingPipIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 5, 1, 1),
    _FsPbbVipToPipMappingPipIfIndex_Type()
)
fsPbbVipToPipMappingPipIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbVipToPipMappingPipIfIndex.setStatus("current")
_FsPbbVipToPipMappingStorageType_Type = StorageType
_FsPbbVipToPipMappingStorageType_Object = MibTableColumn
fsPbbVipToPipMappingStorageType = _FsPbbVipToPipMappingStorageType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 5, 1, 2),
    _FsPbbVipToPipMappingStorageType_Type()
)
fsPbbVipToPipMappingStorageType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbVipToPipMappingStorageType.setStatus("current")
_FsPbbVipToPipMappingRowStatus_Type = RowStatus
_FsPbbVipToPipMappingRowStatus_Object = MibTableColumn
fsPbbVipToPipMappingRowStatus = _FsPbbVipToPipMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 5, 1, 3),
    _FsPbbVipToPipMappingRowStatus_Type()
)
fsPbbVipToPipMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbVipToPipMappingRowStatus.setStatus("current")
_FsPbbCBPServiceMappingTable_Object = MibTable
fsPbbCBPServiceMappingTable = _FsPbbCBPServiceMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 6)
)
if mibBuilder.loadTexts:
    fsPbbCBPServiceMappingTable.setStatus("current")
_FsPbbCBPServiceMappingEntry_Object = MibTableRow
fsPbbCBPServiceMappingEntry = _FsPbbCBPServiceMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 6, 1)
)
fsPbbCBPServiceMappingEntry.setIndexNames(
    (0, "SUPERMICRO-PBB-MIB", "fsdot1ahContextId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "SUPERMICRO-PBB-MIB", "fsPbbCBPServiceMappingBackboneSid"),
)
if mibBuilder.loadTexts:
    fsPbbCBPServiceMappingEntry.setStatus("current")
_FsPbbCBPServiceMappingBackboneSid_Type = IEEE8021PbbServiceIdentifier
_FsPbbCBPServiceMappingBackboneSid_Object = MibTableColumn
fsPbbCBPServiceMappingBackboneSid = _FsPbbCBPServiceMappingBackboneSid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 6, 1, 1),
    _FsPbbCBPServiceMappingBackboneSid_Type()
)
fsPbbCBPServiceMappingBackboneSid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsPbbCBPServiceMappingBackboneSid.setStatus("current")
_FsPbbCBPServiceMappingBVid_Type = VlanId
_FsPbbCBPServiceMappingBVid_Object = MibTableColumn
fsPbbCBPServiceMappingBVid = _FsPbbCBPServiceMappingBVid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 6, 1, 2),
    _FsPbbCBPServiceMappingBVid_Type()
)
fsPbbCBPServiceMappingBVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbCBPServiceMappingBVid.setStatus("current")
_FsPbbCBPServiceMappingDefaultBackboneDest_Type = MacAddress
_FsPbbCBPServiceMappingDefaultBackboneDest_Object = MibTableColumn
fsPbbCBPServiceMappingDefaultBackboneDest = _FsPbbCBPServiceMappingDefaultBackboneDest_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 6, 1, 3),
    _FsPbbCBPServiceMappingDefaultBackboneDest_Type()
)
fsPbbCBPServiceMappingDefaultBackboneDest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbCBPServiceMappingDefaultBackboneDest.setStatus("current")
_FsPbbCBPServiceMappingType_Type = IEEE8021PbbIngressEgress
_FsPbbCBPServiceMappingType_Object = MibTableColumn
fsPbbCBPServiceMappingType = _FsPbbCBPServiceMappingType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 6, 1, 4),
    _FsPbbCBPServiceMappingType_Type()
)
fsPbbCBPServiceMappingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbCBPServiceMappingType.setStatus("current")


class _FsPbbCBPServiceMappingLocalSid_Type(IEEE8021PbbServiceIdentifierOrUnassigned):
    """Custom type fsPbbCBPServiceMappingLocalSid based on IEEE8021PbbServiceIdentifierOrUnassigned"""
    defaultValue = 1


_FsPbbCBPServiceMappingLocalSid_Type.__name__ = "IEEE8021PbbServiceIdentifierOrUnassigned"
_FsPbbCBPServiceMappingLocalSid_Object = MibTableColumn
fsPbbCBPServiceMappingLocalSid = _FsPbbCBPServiceMappingLocalSid_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 6, 1, 5),
    _FsPbbCBPServiceMappingLocalSid_Type()
)
fsPbbCBPServiceMappingLocalSid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbCBPServiceMappingLocalSid.setStatus("current")
_FsPbbCBPServiceMappingRowStatus_Type = RowStatus
_FsPbbCBPServiceMappingRowStatus_Object = MibTableColumn
fsPbbCBPServiceMappingRowStatus = _FsPbbCBPServiceMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 6, 1, 6),
    _FsPbbCBPServiceMappingRowStatus_Type()
)
fsPbbCBPServiceMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbCBPServiceMappingRowStatus.setStatus("current")
_FsPbbCbpTable_Object = MibTable
fsPbbCbpTable = _FsPbbCbpTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 7)
)
if mibBuilder.loadTexts:
    fsPbbCbpTable.setStatus("current")
_FsPbbCbpEntry_Object = MibTableRow
fsPbbCbpEntry = _FsPbbCbpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 7, 1)
)
fsPbbCbpEntry.setIndexNames(
    (0, "SUPERMICRO-PBB-MIB", "fsdot1ahContextId"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsPbbCbpEntry.setStatus("current")
_FsPbbCbpRowStatus_Type = RowStatus
_FsPbbCbpRowStatus_Object = MibTableColumn
fsPbbCbpRowStatus = _FsPbbCbpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 7, 1, 1),
    _FsPbbCbpRowStatus_Type()
)
fsPbbCbpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsPbbCbpRowStatus.setStatus("current")
_FsPbbPipToVipMappingTable_Object = MibTable
fsPbbPipToVipMappingTable = _FsPbbPipToVipMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 8)
)
if mibBuilder.loadTexts:
    fsPbbPipToVipMappingTable.setStatus("current")
_FsPbbPipToVipMappingEntry_Object = MibTableRow
fsPbbPipToVipMappingEntry = _FsPbbPipToVipMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 8, 1)
)
fsPbbPipToVipMappingEntry.setIndexNames(
    (0, "SUPERMICRO-PBB-MIB", "fsdot1ahContextId"),
    (0, "SUPERMICRO-PBB-MIB", "fsPbbPipIfIndex"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsPbbPipToVipMappingEntry.setStatus("current")
_FsPbbPipToVipMappingStatus_Type = TruthValue
_FsPbbPipToVipMappingStatus_Object = MibTableColumn
fsPbbPipToVipMappingStatus = _FsPbbPipToVipMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 1, 1, 8, 1, 1),
    _FsPbbPipToVipMappingStatus_Type()
)
fsPbbPipToVipMappingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPbbPipToVipMappingStatus.setStatus("current")
_FsPbbConformance_ObjectIdentity = ObjectIdentity
fsPbbConformance = _FsPbbConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 2)
)
_FsPbbGroups_ObjectIdentity = ObjectIdentity
fsPbbGroups = _FsPbbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 2, 1)
)
_FsPbbCompliances_ObjectIdentity = ObjectIdentity
fsPbbCompliances = _FsPbbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 2, 2)
)

# Managed Objects groups

fsPbbBackboneEdgeBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 2, 1, 1)
)
fsPbbBackboneEdgeBridgeGroup.setObjects(
      *(("SUPERMICRO-PBB-MIB", "fsPbbBackboneEdgeBridgeAddress"),
        ("SUPERMICRO-PBB-MIB", "fsPbbBackboneEdgeBridgeName"),
        ("SUPERMICRO-PBB-MIB", "fsPbbNumberOfIComponents"),
        ("SUPERMICRO-PBB-MIB", "fsPbbNumberOfBComponents"),
        ("SUPERMICRO-PBB-MIB", "fsPbbNumberOfBebPorts"))
)
if mibBuilder.loadTexts:
    fsPbbBackboneEdgeBridgeGroup.setStatus("current")

fsPbbVipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 2, 1, 2)
)
fsPbbVipGroup.setObjects(
      *(("SUPERMICRO-PBB-MIB", "fsPbbVipPipIfIndex"),
        ("SUPERMICRO-PBB-MIB", "fsPbbVipISid"),
        ("SUPERMICRO-PBB-MIB", "fsPbbVipDefaultDstBMAC"),
        ("SUPERMICRO-PBB-MIB", "fsPbbVipType"),
        ("SUPERMICRO-PBB-MIB", "fsPbbVipRowStatus"),
        ("SUPERMICRO-PBB-MIB", "fsPbbISidToVipComponentId"),
        ("SUPERMICRO-PBB-MIB", "fsPbbISidToVipPort"))
)
if mibBuilder.loadTexts:
    fsPbbVipGroup.setStatus("current")

fsPbbPipGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 2, 1, 3)
)
fsPbbPipGroup.setObjects(
      *(("SUPERMICRO-PBB-MIB", "fsPbbNextAvailablePipIfIndex"),
        ("SUPERMICRO-PBB-MIB", "fsPbbPipBMACAddress"),
        ("SUPERMICRO-PBB-MIB", "fsPbbPipName"),
        ("SUPERMICRO-PBB-MIB", "fsPbbPipIComponentId"),
        ("SUPERMICRO-PBB-MIB", "fsPbbPipRowStatus"))
)
if mibBuilder.loadTexts:
    fsPbbPipGroup.setStatus("current")

fsPbbVipToPipMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 2, 1, 4)
)
fsPbbVipToPipMappingGroup.setObjects(
      *(("SUPERMICRO-PBB-MIB", "fsPbbVipToPipMappingPipIfIndex"),
        ("SUPERMICRO-PBB-MIB", "fsPbbVipToPipMappingStorageType"),
        ("SUPERMICRO-PBB-MIB", "fsPbbVipToPipMappingRowStatus"))
)
if mibBuilder.loadTexts:
    fsPbbVipToPipMappingGroup.setStatus("current")

fsPbbCBPServiceMappingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 2, 1, 5)
)
fsPbbCBPServiceMappingGroup.setObjects(
      *(("SUPERMICRO-PBB-MIB", "fsPbbCBPServiceMappingBVid"),
        ("SUPERMICRO-PBB-MIB", "fsPbbCBPServiceMappingDefaultBackboneDest"),
        ("SUPERMICRO-PBB-MIB", "fsPbbCBPServiceMappingType"),
        ("SUPERMICRO-PBB-MIB", "fsPbbCBPServiceMappingLocalSid"),
        ("SUPERMICRO-PBB-MIB", "fsPbbCBPServiceMappingRowStatus"))
)
if mibBuilder.loadTexts:
    fsPbbCBPServiceMappingGroup.setStatus("current")

fsPbbDynamicCbpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 2, 1, 6)
)
fsPbbDynamicCbpGroup.setObjects(
    ("SUPERMICRO-PBB-MIB", "fsPbbCbpRowStatus")
)
if mibBuilder.loadTexts:
    fsPbbDynamicCbpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsPbbCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10876, 101, 2, 14, 2, 2, 1)
)
fsPbbCompliance.setObjects(
      *(("SUPERMICRO-PBB-MIB", "fsPbbBackboneEdgeBridgeGroup"),
        ("SUPERMICRO-PBB-MIB", "fsPbbVipGroup"),
        ("SUPERMICRO-PBB-MIB", "fsPbbPipGroup"),
        ("SUPERMICRO-PBB-MIB", "fsPbbVipToPipMappingGroup"),
        ("SUPERMICRO-PBB-MIB", "fsPbbCBPServiceMappingGroup"),
        ("SUPERMICRO-PBB-MIB", "fsPbbDynamicCbpGroup"))
)
if mibBuilder.loadTexts:
    fsPbbCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-PBB-MIB",
    **{"fsPbbMib": fsPbbMib,
       "fsPbbNotifications": fsPbbNotifications,
       "fsPbbObjects": fsPbbObjects,
       "fsPbbProviderBackboneBridge": fsPbbProviderBackboneBridge,
       "fsPbbBackboneEdgeBridgeObjects": fsPbbBackboneEdgeBridgeObjects,
       "fsPbbBackboneEdgeBridgeAddress": fsPbbBackboneEdgeBridgeAddress,
       "fsPbbBackboneEdgeBridgeName": fsPbbBackboneEdgeBridgeName,
       "fsPbbNumberOfIComponents": fsPbbNumberOfIComponents,
       "fsPbbNumberOfBComponents": fsPbbNumberOfBComponents,
       "fsPbbNumberOfBebPorts": fsPbbNumberOfBebPorts,
       "fsPbbNextAvailablePipIfIndex": fsPbbNextAvailablePipIfIndex,
       "fsPbbVipTable": fsPbbVipTable,
       "fsPbbVipEntry": fsPbbVipEntry,
       "fsdot1ahContextId": fsdot1ahContextId,
       "fsPbbVipPipIfIndex": fsPbbVipPipIfIndex,
       "fsPbbVipISid": fsPbbVipISid,
       "fsPbbVipDefaultDstBMAC": fsPbbVipDefaultDstBMAC,
       "fsPbbVipType": fsPbbVipType,
       "fsPbbVipRowStatus": fsPbbVipRowStatus,
       "fsPbbISidToVipTable": fsPbbISidToVipTable,
       "fsPbbISidToVipEntry": fsPbbISidToVipEntry,
       "fsPbbISidToVipISid": fsPbbISidToVipISid,
       "fsPbbISidToVipComponentId": fsPbbISidToVipComponentId,
       "fsPbbISidToVipPort": fsPbbISidToVipPort,
       "fsPbbPipTable": fsPbbPipTable,
       "fsPbbPipEntry": fsPbbPipEntry,
       "fsPbbPipIfIndex": fsPbbPipIfIndex,
       "fsPbbPipBMACAddress": fsPbbPipBMACAddress,
       "fsPbbPipName": fsPbbPipName,
       "fsPbbPipIComponentId": fsPbbPipIComponentId,
       "fsPbbPipRowStatus": fsPbbPipRowStatus,
       "fsPbbVipToPipMappingTable": fsPbbVipToPipMappingTable,
       "fsPbbVipToPipMappingEntry": fsPbbVipToPipMappingEntry,
       "fsPbbVipToPipMappingPipIfIndex": fsPbbVipToPipMappingPipIfIndex,
       "fsPbbVipToPipMappingStorageType": fsPbbVipToPipMappingStorageType,
       "fsPbbVipToPipMappingRowStatus": fsPbbVipToPipMappingRowStatus,
       "fsPbbCBPServiceMappingTable": fsPbbCBPServiceMappingTable,
       "fsPbbCBPServiceMappingEntry": fsPbbCBPServiceMappingEntry,
       "fsPbbCBPServiceMappingBackboneSid": fsPbbCBPServiceMappingBackboneSid,
       "fsPbbCBPServiceMappingBVid": fsPbbCBPServiceMappingBVid,
       "fsPbbCBPServiceMappingDefaultBackboneDest": fsPbbCBPServiceMappingDefaultBackboneDest,
       "fsPbbCBPServiceMappingType": fsPbbCBPServiceMappingType,
       "fsPbbCBPServiceMappingLocalSid": fsPbbCBPServiceMappingLocalSid,
       "fsPbbCBPServiceMappingRowStatus": fsPbbCBPServiceMappingRowStatus,
       "fsPbbCbpTable": fsPbbCbpTable,
       "fsPbbCbpEntry": fsPbbCbpEntry,
       "fsPbbCbpRowStatus": fsPbbCbpRowStatus,
       "fsPbbPipToVipMappingTable": fsPbbPipToVipMappingTable,
       "fsPbbPipToVipMappingEntry": fsPbbPipToVipMappingEntry,
       "fsPbbPipToVipMappingStatus": fsPbbPipToVipMappingStatus,
       "fsPbbConformance": fsPbbConformance,
       "fsPbbGroups": fsPbbGroups,
       "fsPbbBackboneEdgeBridgeGroup": fsPbbBackboneEdgeBridgeGroup,
       "fsPbbVipGroup": fsPbbVipGroup,
       "fsPbbPipGroup": fsPbbPipGroup,
       "fsPbbVipToPipMappingGroup": fsPbbVipToPipMappingGroup,
       "fsPbbCBPServiceMappingGroup": fsPbbCBPServiceMappingGroup,
       "fsPbbDynamicCbpGroup": fsPbbDynamicCbpGroup,
       "fsPbbCompliances": fsPbbCompliances,
       "fsPbbCompliance": fsPbbCompliance}
)
