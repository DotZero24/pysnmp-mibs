# SNMP MIB module (H3C-FCOE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-FCOE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:19:30 2025
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

(fcmInstanceIndex,) = mibBuilder.importSymbols(
    "FC-MGMT-MIB",
    "fcmInstanceIndex")

(H3cFcNameId,) = mibBuilder.importSymbols(
    "H3C-FC-TC-MIB",
    "H3cFcNameId")

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(T11FabricIndex,) = mibBuilder.importSymbols(
    "T11-TC-MIB",
    "T11FabricIndex")


# MODULE-IDENTITY

h3cFCoE = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120)
)
if mibBuilder.loadTexts:
    h3cFCoE.setRevisions(
        ("2014-11-12 00:00",
         "2012-03-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cFCoEVfcBindType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interfaceIndex", 1),
          ("macAddress", 2))
    )



# MIB Managed Objects in the order of their OIDs

_H3cFCoEObjects_ObjectIdentity = ObjectIdentity
h3cFCoEObjects = _H3cFCoEObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1)
)
_H3cFCoEConfig_ObjectIdentity = ObjectIdentity
h3cFCoEConfig = _H3cFCoEConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1)
)
_H3cFCoECfgTable_Object = MibTable
h3cFCoECfgTable = _H3cFCoECfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1)
)
if mibBuilder.loadTexts:
    h3cFCoECfgTable.setStatus("current")
_H3cFCoECfgEntry_Object = MibTableRow
h3cFCoECfgEntry = _H3cFCoECfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1)
)
h3cFCoECfgEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
)
if mibBuilder.loadTexts:
    h3cFCoECfgEntry.setStatus("current")


class _H3cFCoECfgFcmap_Type(OctetString):
    """Custom type h3cFCoECfgFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_H3cFCoECfgFcmap_Type.__name__ = "OctetString"
_H3cFCoECfgFcmap_Object = MibTableColumn
h3cFCoECfgFcmap = _H3cFCoECfgFcmap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 1),
    _H3cFCoECfgFcmap_Type()
)
h3cFCoECfgFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoECfgFcmap.setStatus("current")


class _H3cFCoECfgDynamicVfcCreation_Type(TruthValue):
    """Custom type h3cFCoECfgDynamicVfcCreation based on TruthValue"""
    defaultValue = 2


_H3cFCoECfgDynamicVfcCreation_Type.__name__ = "TruthValue"
_H3cFCoECfgDynamicVfcCreation_Object = MibTableColumn
h3cFCoECfgDynamicVfcCreation = _H3cFCoECfgDynamicVfcCreation_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 2),
    _H3cFCoECfgDynamicVfcCreation_Type()
)
h3cFCoECfgDynamicVfcCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoECfgDynamicVfcCreation.setStatus("current")


class _H3cFCoECfgDefaultFCFPriority_Type(Unsigned32):
    """Custom type h3cFCoECfgDefaultFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cFCoECfgDefaultFCFPriority_Type.__name__ = "Unsigned32"
_H3cFCoECfgDefaultFCFPriority_Object = MibTableColumn
h3cFCoECfgDefaultFCFPriority = _H3cFCoECfgDefaultFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 3),
    _H3cFCoECfgDefaultFCFPriority_Type()
)
h3cFCoECfgDefaultFCFPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoECfgDefaultFCFPriority.setStatus("current")


class _H3cFCoECfgDATov_Type(Unsigned32):
    """Custom type h3cFCoECfgDATov based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 600),
    )


_H3cFCoECfgDATov_Type.__name__ = "Unsigned32"
_H3cFCoECfgDATov_Object = MibTableColumn
h3cFCoECfgDATov = _H3cFCoECfgDATov_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 4),
    _H3cFCoECfgDATov_Type()
)
h3cFCoECfgDATov.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoECfgDATov.setStatus("current")
if mibBuilder.loadTexts:
    h3cFCoECfgDATov.setUnits("seconds")


class _H3cFCoECfgAddressingMode_Type(Integer32):
    """Custom type h3cFCoECfgAddressingMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fpma", 1),
          ("spma", 2),
          ("fpmaAndSpma", 3))
    )


_H3cFCoECfgAddressingMode_Type.__name__ = "Integer32"
_H3cFCoECfgAddressingMode_Object = MibTableColumn
h3cFCoECfgAddressingMode = _H3cFCoECfgAddressingMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 1, 1, 5),
    _H3cFCoECfgAddressingMode_Type()
)
h3cFCoECfgAddressingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoECfgAddressingMode.setStatus("current")
_H3cFCoEVLANTable_Object = MibTable
h3cFCoEVLANTable = _H3cFCoEVLANTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2)
)
if mibBuilder.loadTexts:
    h3cFCoEVLANTable.setStatus("current")
_H3cFCoEVLANEntry_Object = MibTableRow
h3cFCoEVLANEntry = _H3cFCoEVLANEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1)
)
h3cFCoEVLANEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEVLANIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFabricIndex"),
)
if mibBuilder.loadTexts:
    h3cFCoEVLANEntry.setStatus("current")
_H3cFCoEVLANIndex_Type = VlanIndex
_H3cFCoEVLANIndex_Object = MibTableColumn
h3cFCoEVLANIndex = _H3cFCoEVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 1),
    _H3cFCoEVLANIndex_Type()
)
h3cFCoEVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEVLANIndex.setStatus("current")
_H3cFCoEFabricIndex_Type = T11FabricIndex
_H3cFCoEFabricIndex_Object = MibTableColumn
h3cFCoEFabricIndex = _H3cFCoEFabricIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 2),
    _H3cFCoEFabricIndex_Type()
)
h3cFCoEFabricIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFabricIndex.setStatus("current")


class _H3cFCoEVLANOperState_Type(Integer32):
    """Custom type h3cFCoEVLANOperState based on Integer32"""
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


_H3cFCoEVLANOperState_Type.__name__ = "Integer32"
_H3cFCoEVLANOperState_Object = MibTableColumn
h3cFCoEVLANOperState = _H3cFCoEVLANOperState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 3),
    _H3cFCoEVLANOperState_Type()
)
h3cFCoEVLANOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEVLANOperState.setStatus("current")
_H3cFCoEVLANRowStatus_Type = RowStatus
_H3cFCoEVLANRowStatus_Object = MibTableColumn
h3cFCoEVLANRowStatus = _H3cFCoEVLANRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 2, 1, 4),
    _H3cFCoEVLANRowStatus_Type()
)
h3cFCoEVLANRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEVLANRowStatus.setStatus("current")
_H3cFCoEStaticVfcTable_Object = MibTable
h3cFCoEStaticVfcTable = _H3cFCoEStaticVfcTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3)
)
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcTable.setStatus("current")
_H3cFCoEStaticVfcEntry_Object = MibTableRow
h3cFCoEStaticVfcEntry = _H3cFCoEStaticVfcEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1)
)
h3cFCoEStaticVfcEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEStaticVfcIndex"),
)
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcEntry.setStatus("current")


class _H3cFCoEStaticVfcIndex_Type(Unsigned32):
    """Custom type h3cFCoEStaticVfcIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_H3cFCoEStaticVfcIndex_Type.__name__ = "Unsigned32"
_H3cFCoEStaticVfcIndex_Object = MibTableColumn
h3cFCoEStaticVfcIndex = _H3cFCoEStaticVfcIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 1),
    _H3cFCoEStaticVfcIndex_Type()
)
h3cFCoEStaticVfcIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcIndex.setStatus("current")


class _H3cFCoEStaticVfcFCFPriority_Type(Unsigned32):
    """Custom type h3cFCoEStaticVfcFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cFCoEStaticVfcFCFPriority_Type.__name__ = "Unsigned32"
_H3cFCoEStaticVfcFCFPriority_Object = MibTableColumn
h3cFCoEStaticVfcFCFPriority = _H3cFCoEStaticVfcFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 2),
    _H3cFCoEStaticVfcFCFPriority_Type()
)
h3cFCoEStaticVfcFCFPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcFCFPriority.setStatus("current")
_H3cFCoEStaticVfcBindType_Type = H3cFCoEVfcBindType
_H3cFCoEStaticVfcBindType_Object = MibTableColumn
h3cFCoEStaticVfcBindType = _H3cFCoEStaticVfcBindType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 3),
    _H3cFCoEStaticVfcBindType_Type()
)
h3cFCoEStaticVfcBindType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcBindType.setStatus("current")
_H3cFCoEStaticVfcBindIfIndex_Type = InterfaceIndexOrZero
_H3cFCoEStaticVfcBindIfIndex_Object = MibTableColumn
h3cFCoEStaticVfcBindIfIndex = _H3cFCoEStaticVfcBindIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 4),
    _H3cFCoEStaticVfcBindIfIndex_Type()
)
h3cFCoEStaticVfcBindIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcBindIfIndex.setStatus("current")
_H3cFCoEStaticVfcBindMACAddress_Type = MacAddress
_H3cFCoEStaticVfcBindMACAddress_Object = MibTableColumn
h3cFCoEStaticVfcBindMACAddress = _H3cFCoEStaticVfcBindMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 5),
    _H3cFCoEStaticVfcBindMACAddress_Type()
)
h3cFCoEStaticVfcBindMACAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcBindMACAddress.setStatus("current")
_H3cFCoEStaticVfcIfIndex_Type = InterfaceIndex
_H3cFCoEStaticVfcIfIndex_Object = MibTableColumn
h3cFCoEStaticVfcIfIndex = _H3cFCoEStaticVfcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 6),
    _H3cFCoEStaticVfcIfIndex_Type()
)
h3cFCoEStaticVfcIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcIfIndex.setStatus("current")
_H3cFCoEStaticVfcCreationTime_Type = TimeStamp
_H3cFCoEStaticVfcCreationTime_Object = MibTableColumn
h3cFCoEStaticVfcCreationTime = _H3cFCoEStaticVfcCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 7),
    _H3cFCoEStaticVfcCreationTime_Type()
)
h3cFCoEStaticVfcCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcCreationTime.setStatus("current")
_H3cFCoEStaticVfcFailureCause_Type = SnmpAdminString
_H3cFCoEStaticVfcFailureCause_Object = MibTableColumn
h3cFCoEStaticVfcFailureCause = _H3cFCoEStaticVfcFailureCause_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 8),
    _H3cFCoEStaticVfcFailureCause_Type()
)
h3cFCoEStaticVfcFailureCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcFailureCause.setStatus("current")
_H3cFCoEStaticVfcRowStatus_Type = RowStatus
_H3cFCoEStaticVfcRowStatus_Object = MibTableColumn
h3cFCoEStaticVfcRowStatus = _H3cFCoEStaticVfcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 3, 1, 9),
    _H3cFCoEStaticVfcRowStatus_Type()
)
h3cFCoEStaticVfcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEStaticVfcRowStatus.setStatus("current")
_H3cFCoEFIPSnoopingTable_Object = MibTable
h3cFCoEFIPSnoopingTable = _H3cFCoEFIPSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 4)
)
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingTable.setStatus("current")
_H3cFCoEFIPSnoopingEntry_Object = MibTableRow
h3cFCoEFIPSnoopingEntry = _H3cFCoEFIPSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 4, 1)
)
h3cFCoEFIPSnoopingEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingVLANIndex"),
)
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingEntry.setStatus("current")
_H3cFCoEFIPSnoopingVLANIndex_Type = VlanIndex
_H3cFCoEFIPSnoopingVLANIndex_Object = MibTableColumn
h3cFCoEFIPSnoopingVLANIndex = _H3cFCoEFIPSnoopingVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 4, 1, 1),
    _H3cFCoEFIPSnoopingVLANIndex_Type()
)
h3cFCoEFIPSnoopingVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingVLANIndex.setStatus("current")


class _H3cFCoEFIPSnoopingEnable_Type(TruthValue):
    """Custom type h3cFCoEFIPSnoopingEnable based on TruthValue"""
    defaultValue = 2


_H3cFCoEFIPSnoopingEnable_Type.__name__ = "TruthValue"
_H3cFCoEFIPSnoopingEnable_Object = MibTableColumn
h3cFCoEFIPSnoopingEnable = _H3cFCoEFIPSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 4, 1, 2),
    _H3cFCoEFIPSnoopingEnable_Type()
)
h3cFCoEFIPSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingEnable.setStatus("current")


class _H3cFCoEFIPSnoopingFcmap_Type(OctetString):
    """Custom type h3cFCoEFIPSnoopingFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_H3cFCoEFIPSnoopingFcmap_Type.__name__ = "OctetString"
_H3cFCoEFIPSnoopingFcmap_Object = MibTableColumn
h3cFCoEFIPSnoopingFcmap = _H3cFCoEFIPSnoopingFcmap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 4, 1, 3),
    _H3cFCoEFIPSnoopingFcmap_Type()
)
h3cFCoEFIPSnoopingFcmap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingFcmap.setStatus("current")
_H3cFCoEVlanCfgTable_Object = MibTable
h3cFCoEVlanCfgTable = _H3cFCoEVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 5)
)
if mibBuilder.loadTexts:
    h3cFCoEVlanCfgTable.setStatus("current")
_H3cFCoEVlanCfgEntry_Object = MibTableRow
h3cFCoEVlanCfgEntry = _H3cFCoEVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 5, 1)
)
h3cFCoEVlanCfgEntry.setIndexNames(
    (0, "H3C-FCOE-MIB", "h3cFCoEVLANIndex"),
)
if mibBuilder.loadTexts:
    h3cFCoEVlanCfgEntry.setStatus("current")


class _H3cFCoEVlanCfgFcmap_Type(OctetString):
    """Custom type h3cFCoEVlanCfgFcmap based on OctetString"""
    defaultHexValue = "0EFC00"

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_H3cFCoEVlanCfgFcmap_Type.__name__ = "OctetString"
_H3cFCoEVlanCfgFcmap_Object = MibTableColumn
h3cFCoEVlanCfgFcmap = _H3cFCoEVlanCfgFcmap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 5, 1, 1),
    _H3cFCoEVlanCfgFcmap_Type()
)
h3cFCoEVlanCfgFcmap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEVlanCfgFcmap.setStatus("current")


class _H3cFCoEVlanCfgFCFPriority_Type(Unsigned32):
    """Custom type h3cFCoEVlanCfgFCFPriority based on Unsigned32"""
    defaultValue = 128

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_H3cFCoEVlanCfgFCFPriority_Type.__name__ = "Unsigned32"
_H3cFCoEVlanCfgFCFPriority_Object = MibTableColumn
h3cFCoEVlanCfgFCFPriority = _H3cFCoEVlanCfgFCFPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 5, 1, 2),
    _H3cFCoEVlanCfgFCFPriority_Type()
)
h3cFCoEVlanCfgFCFPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEVlanCfgFCFPriority.setStatus("current")


class _H3cFCoEVlanCfgDATov_Type(Unsigned32):
    """Custom type h3cFCoEVlanCfgDATov based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 600),
    )


_H3cFCoEVlanCfgDATov_Type.__name__ = "Unsigned32"
_H3cFCoEVlanCfgDATov_Object = MibTableColumn
h3cFCoEVlanCfgDATov = _H3cFCoEVlanCfgDATov_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 5, 1, 3),
    _H3cFCoEVlanCfgDATov_Type()
)
h3cFCoEVlanCfgDATov.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEVlanCfgDATov.setStatus("current")
if mibBuilder.loadTexts:
    h3cFCoEVlanCfgDATov.setUnits("seconds")
_H3cFCoEVlanCfgRowStatus_Type = RowStatus
_H3cFCoEVlanCfgRowStatus_Object = MibTableColumn
h3cFCoEVlanCfgRowStatus = _H3cFCoEVlanCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 5, 1, 4),
    _H3cFCoEVlanCfgRowStatus_Type()
)
h3cFCoEVlanCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cFCoEVlanCfgRowStatus.setStatus("current")
_H3cFCoEFIPSnoopingFCFTable_Object = MibTable
h3cFCoEFIPSnoopingFCFTable = _H3cFCoEFIPSnoopingFCFTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 6)
)
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingFCFTable.setStatus("current")
_H3cFCoEFIPSnoopingFCFEntry_Object = MibTableRow
h3cFCoEFIPSnoopingFCFEntry = _H3cFCoEFIPSnoopingFCFEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 6, 1)
)
h3cFCoEFIPSnoopingFCFEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingFCFVLANIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingFCFIfIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingFCFMAC"),
)
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingFCFEntry.setStatus("current")
_H3cFCoEFIPSnoopingFCFVLANIndex_Type = VlanIndex
_H3cFCoEFIPSnoopingFCFVLANIndex_Object = MibTableColumn
h3cFCoEFIPSnoopingFCFVLANIndex = _H3cFCoEFIPSnoopingFCFVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 6, 1, 1),
    _H3cFCoEFIPSnoopingFCFVLANIndex_Type()
)
h3cFCoEFIPSnoopingFCFVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingFCFVLANIndex.setStatus("current")
_H3cFCoEFIPSnoopingFCFIfIndex_Type = InterfaceIndex
_H3cFCoEFIPSnoopingFCFIfIndex_Object = MibTableColumn
h3cFCoEFIPSnoopingFCFIfIndex = _H3cFCoEFIPSnoopingFCFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 6, 1, 2),
    _H3cFCoEFIPSnoopingFCFIfIndex_Type()
)
h3cFCoEFIPSnoopingFCFIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingFCFIfIndex.setStatus("current")
_H3cFCoEFIPSnoopingFCFMAC_Type = MacAddress
_H3cFCoEFIPSnoopingFCFMAC_Object = MibTableColumn
h3cFCoEFIPSnoopingFCFMAC = _H3cFCoEFIPSnoopingFCFMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 6, 1, 3),
    _H3cFCoEFIPSnoopingFCFMAC_Type()
)
h3cFCoEFIPSnoopingFCFMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingFCFMAC.setStatus("current")
_H3cFCoEFIPSnoopingFCFSwitchName_Type = H3cFcNameId
_H3cFCoEFIPSnoopingFCFSwitchName_Object = MibTableColumn
h3cFCoEFIPSnoopingFCFSwitchName = _H3cFCoEFIPSnoopingFCFSwitchName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 6, 1, 4),
    _H3cFCoEFIPSnoopingFCFSwitchName_Type()
)
h3cFCoEFIPSnoopingFCFSwitchName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingFCFSwitchName.setStatus("current")
_H3cFCoEFIPSnoopingFCFFabricName_Type = H3cFcNameId
_H3cFCoEFIPSnoopingFCFFabricName_Object = MibTableColumn
h3cFCoEFIPSnoopingFCFFabricName = _H3cFCoEFIPSnoopingFCFFabricName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 6, 1, 5),
    _H3cFCoEFIPSnoopingFCFFabricName_Type()
)
h3cFCoEFIPSnoopingFCFFabricName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingFCFFabricName.setStatus("current")
_H3cFCoEFIPSnoopingFCFENodeCount_Type = Unsigned32
_H3cFCoEFIPSnoopingFCFENodeCount_Object = MibTableColumn
h3cFCoEFIPSnoopingFCFENodeCount = _H3cFCoEFIPSnoopingFCFENodeCount_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 6, 1, 6),
    _H3cFCoEFIPSnoopingFCFENodeCount_Type()
)
h3cFCoEFIPSnoopingFCFENodeCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingFCFENodeCount.setStatus("current")
_H3cFCoEFIPSnoopingENodeTable_Object = MibTable
h3cFCoEFIPSnoopingENodeTable = _H3cFCoEFIPSnoopingENodeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 7)
)
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingENodeTable.setStatus("current")
_H3cFCoEFIPSnoopingENodeEntry_Object = MibTableRow
h3cFCoEFIPSnoopingENodeEntry = _H3cFCoEFIPSnoopingENodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 7, 1)
)
h3cFCoEFIPSnoopingENodeEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingENodeVLANIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingENodeIfIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingENodeMAC"),
)
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingENodeEntry.setStatus("current")
_H3cFCoEFIPSnoopingENodeVLANIndex_Type = VlanIndex
_H3cFCoEFIPSnoopingENodeVLANIndex_Object = MibTableColumn
h3cFCoEFIPSnoopingENodeVLANIndex = _H3cFCoEFIPSnoopingENodeVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 7, 1, 1),
    _H3cFCoEFIPSnoopingENodeVLANIndex_Type()
)
h3cFCoEFIPSnoopingENodeVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingENodeVLANIndex.setStatus("current")
_H3cFCoEFIPSnoopingENodeIfIndex_Type = InterfaceIndex
_H3cFCoEFIPSnoopingENodeIfIndex_Object = MibTableColumn
h3cFCoEFIPSnoopingENodeIfIndex = _H3cFCoEFIPSnoopingENodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 7, 1, 2),
    _H3cFCoEFIPSnoopingENodeIfIndex_Type()
)
h3cFCoEFIPSnoopingENodeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingENodeIfIndex.setStatus("current")
_H3cFCoEFIPSnoopingENodeMAC_Type = MacAddress
_H3cFCoEFIPSnoopingENodeMAC_Object = MibTableColumn
h3cFCoEFIPSnoopingENodeMAC = _H3cFCoEFIPSnoopingENodeMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 7, 1, 3),
    _H3cFCoEFIPSnoopingENodeMAC_Type()
)
h3cFCoEFIPSnoopingENodeMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingENodeMAC.setStatus("current")
_H3cFCoEFIPSnoopingENodeName_Type = H3cFcNameId
_H3cFCoEFIPSnoopingENodeName_Object = MibTableColumn
h3cFCoEFIPSnoopingENodeName = _H3cFCoEFIPSnoopingENodeName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 7, 1, 4),
    _H3cFCoEFIPSnoopingENodeName_Type()
)
h3cFCoEFIPSnoopingENodeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingENodeName.setStatus("current")
_H3cFCoEFIPSnoopingVNTable_Object = MibTable
h3cFCoEFIPSnoopingVNTable = _H3cFCoEFIPSnoopingVNTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 8)
)
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingVNTable.setStatus("current")
_H3cFCoEFIPSnoopingVNEntry_Object = MibTableRow
h3cFCoEFIPSnoopingVNEntry = _H3cFCoEFIPSnoopingVNEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 8, 1)
)
h3cFCoEFIPSnoopingVNEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingVNVLANIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingVNENodeIfIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingVNENodeMAC"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingVNFCFMAC"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingVNMAC"),
)
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingVNEntry.setStatus("current")
_H3cFCoEFIPSnoopingVNVLANIndex_Type = VlanIndex
_H3cFCoEFIPSnoopingVNVLANIndex_Object = MibTableColumn
h3cFCoEFIPSnoopingVNVLANIndex = _H3cFCoEFIPSnoopingVNVLANIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 8, 1, 1),
    _H3cFCoEFIPSnoopingVNVLANIndex_Type()
)
h3cFCoEFIPSnoopingVNVLANIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingVNVLANIndex.setStatus("current")
_H3cFCoEFIPSnoopingVNENodeIfIndex_Type = InterfaceIndex
_H3cFCoEFIPSnoopingVNENodeIfIndex_Object = MibTableColumn
h3cFCoEFIPSnoopingVNENodeIfIndex = _H3cFCoEFIPSnoopingVNENodeIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 8, 1, 2),
    _H3cFCoEFIPSnoopingVNENodeIfIndex_Type()
)
h3cFCoEFIPSnoopingVNENodeIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingVNENodeIfIndex.setStatus("current")
_H3cFCoEFIPSnoopingVNENodeMAC_Type = MacAddress
_H3cFCoEFIPSnoopingVNENodeMAC_Object = MibTableColumn
h3cFCoEFIPSnoopingVNENodeMAC = _H3cFCoEFIPSnoopingVNENodeMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 8, 1, 3),
    _H3cFCoEFIPSnoopingVNENodeMAC_Type()
)
h3cFCoEFIPSnoopingVNENodeMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingVNENodeMAC.setStatus("current")
_H3cFCoEFIPSnoopingVNFCFMAC_Type = MacAddress
_H3cFCoEFIPSnoopingVNFCFMAC_Object = MibTableColumn
h3cFCoEFIPSnoopingVNFCFMAC = _H3cFCoEFIPSnoopingVNFCFMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 8, 1, 4),
    _H3cFCoEFIPSnoopingVNFCFMAC_Type()
)
h3cFCoEFIPSnoopingVNFCFMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingVNFCFMAC.setStatus("current")
_H3cFCoEFIPSnoopingVNMAC_Type = MacAddress
_H3cFCoEFIPSnoopingVNMAC_Object = MibTableColumn
h3cFCoEFIPSnoopingVNMAC = _H3cFCoEFIPSnoopingVNMAC_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 8, 1, 5),
    _H3cFCoEFIPSnoopingVNMAC_Type()
)
h3cFCoEFIPSnoopingVNMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingVNMAC.setStatus("current")
_H3cFCoEFIPSnoopingVNName_Type = H3cFcNameId
_H3cFCoEFIPSnoopingVNName_Object = MibTableColumn
h3cFCoEFIPSnoopingVNName = _H3cFCoEFIPSnoopingVNName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 8, 1, 6),
    _H3cFCoEFIPSnoopingVNName_Type()
)
h3cFCoEFIPSnoopingVNName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingVNName.setStatus("current")
_H3cFCoEFIPSnoopingVNFCFIfIndex_Type = InterfaceIndex
_H3cFCoEFIPSnoopingVNFCFIfIndex_Object = MibTableColumn
h3cFCoEFIPSnoopingVNFCFIfIndex = _H3cFCoEFIPSnoopingVNFCFIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 8, 1, 7),
    _H3cFCoEFIPSnoopingVNFCFIfIndex_Type()
)
h3cFCoEFIPSnoopingVNFCFIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingVNFCFIfIndex.setStatus("current")
_H3cFCoEFIPSnoopingIfCfgTable_Object = MibTable
h3cFCoEFIPSnoopingIfCfgTable = _H3cFCoEFIPSnoopingIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 9)
)
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingIfCfgTable.setStatus("current")
_H3cFCoEFIPSnoopingIfCfgEntry_Object = MibTableRow
h3cFCoEFIPSnoopingIfCfgEntry = _H3cFCoEFIPSnoopingIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 9, 1)
)
h3cFCoEFIPSnoopingIfCfgEntry.setIndexNames(
    (0, "FC-MGMT-MIB", "fcmInstanceIndex"),
    (0, "H3C-FCOE-MIB", "h3cFCoEFIPSnoopingIfCfgIfIndex"),
)
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingIfCfgEntry.setStatus("current")
_H3cFCoEFIPSnoopingIfCfgIfIndex_Type = InterfaceIndex
_H3cFCoEFIPSnoopingIfCfgIfIndex_Object = MibTableColumn
h3cFCoEFIPSnoopingIfCfgIfIndex = _H3cFCoEFIPSnoopingIfCfgIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 9, 1, 1),
    _H3cFCoEFIPSnoopingIfCfgIfIndex_Type()
)
h3cFCoEFIPSnoopingIfCfgIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingIfCfgIfIndex.setStatus("current")


class _H3cFCoEFIPSnoopingIfCfgPortType_Type(Integer32):
    """Custom type h3cFCoEFIPSnoopingIfCfgPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fcf", 1),
          ("enode", 2))
    )


_H3cFCoEFIPSnoopingIfCfgPortType_Type.__name__ = "Integer32"
_H3cFCoEFIPSnoopingIfCfgPortType_Object = MibTableColumn
h3cFCoEFIPSnoopingIfCfgPortType = _H3cFCoEFIPSnoopingIfCfgPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 120, 1, 1, 9, 1, 2),
    _H3cFCoEFIPSnoopingIfCfgPortType_Type()
)
h3cFCoEFIPSnoopingIfCfgPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFCoEFIPSnoopingIfCfgPortType.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-FCOE-MIB",
    **{"H3cFCoEVfcBindType": H3cFCoEVfcBindType,
       "h3cFCoE": h3cFCoE,
       "h3cFCoEObjects": h3cFCoEObjects,
       "h3cFCoEConfig": h3cFCoEConfig,
       "h3cFCoECfgTable": h3cFCoECfgTable,
       "h3cFCoECfgEntry": h3cFCoECfgEntry,
       "h3cFCoECfgFcmap": h3cFCoECfgFcmap,
       "h3cFCoECfgDynamicVfcCreation": h3cFCoECfgDynamicVfcCreation,
       "h3cFCoECfgDefaultFCFPriority": h3cFCoECfgDefaultFCFPriority,
       "h3cFCoECfgDATov": h3cFCoECfgDATov,
       "h3cFCoECfgAddressingMode": h3cFCoECfgAddressingMode,
       "h3cFCoEVLANTable": h3cFCoEVLANTable,
       "h3cFCoEVLANEntry": h3cFCoEVLANEntry,
       "h3cFCoEVLANIndex": h3cFCoEVLANIndex,
       "h3cFCoEFabricIndex": h3cFCoEFabricIndex,
       "h3cFCoEVLANOperState": h3cFCoEVLANOperState,
       "h3cFCoEVLANRowStatus": h3cFCoEVLANRowStatus,
       "h3cFCoEStaticVfcTable": h3cFCoEStaticVfcTable,
       "h3cFCoEStaticVfcEntry": h3cFCoEStaticVfcEntry,
       "h3cFCoEStaticVfcIndex": h3cFCoEStaticVfcIndex,
       "h3cFCoEStaticVfcFCFPriority": h3cFCoEStaticVfcFCFPriority,
       "h3cFCoEStaticVfcBindType": h3cFCoEStaticVfcBindType,
       "h3cFCoEStaticVfcBindIfIndex": h3cFCoEStaticVfcBindIfIndex,
       "h3cFCoEStaticVfcBindMACAddress": h3cFCoEStaticVfcBindMACAddress,
       "h3cFCoEStaticVfcIfIndex": h3cFCoEStaticVfcIfIndex,
       "h3cFCoEStaticVfcCreationTime": h3cFCoEStaticVfcCreationTime,
       "h3cFCoEStaticVfcFailureCause": h3cFCoEStaticVfcFailureCause,
       "h3cFCoEStaticVfcRowStatus": h3cFCoEStaticVfcRowStatus,
       "h3cFCoEFIPSnoopingTable": h3cFCoEFIPSnoopingTable,
       "h3cFCoEFIPSnoopingEntry": h3cFCoEFIPSnoopingEntry,
       "h3cFCoEFIPSnoopingVLANIndex": h3cFCoEFIPSnoopingVLANIndex,
       "h3cFCoEFIPSnoopingEnable": h3cFCoEFIPSnoopingEnable,
       "h3cFCoEFIPSnoopingFcmap": h3cFCoEFIPSnoopingFcmap,
       "h3cFCoEVlanCfgTable": h3cFCoEVlanCfgTable,
       "h3cFCoEVlanCfgEntry": h3cFCoEVlanCfgEntry,
       "h3cFCoEVlanCfgFcmap": h3cFCoEVlanCfgFcmap,
       "h3cFCoEVlanCfgFCFPriority": h3cFCoEVlanCfgFCFPriority,
       "h3cFCoEVlanCfgDATov": h3cFCoEVlanCfgDATov,
       "h3cFCoEVlanCfgRowStatus": h3cFCoEVlanCfgRowStatus,
       "h3cFCoEFIPSnoopingFCFTable": h3cFCoEFIPSnoopingFCFTable,
       "h3cFCoEFIPSnoopingFCFEntry": h3cFCoEFIPSnoopingFCFEntry,
       "h3cFCoEFIPSnoopingFCFVLANIndex": h3cFCoEFIPSnoopingFCFVLANIndex,
       "h3cFCoEFIPSnoopingFCFIfIndex": h3cFCoEFIPSnoopingFCFIfIndex,
       "h3cFCoEFIPSnoopingFCFMAC": h3cFCoEFIPSnoopingFCFMAC,
       "h3cFCoEFIPSnoopingFCFSwitchName": h3cFCoEFIPSnoopingFCFSwitchName,
       "h3cFCoEFIPSnoopingFCFFabricName": h3cFCoEFIPSnoopingFCFFabricName,
       "h3cFCoEFIPSnoopingFCFENodeCount": h3cFCoEFIPSnoopingFCFENodeCount,
       "h3cFCoEFIPSnoopingENodeTable": h3cFCoEFIPSnoopingENodeTable,
       "h3cFCoEFIPSnoopingENodeEntry": h3cFCoEFIPSnoopingENodeEntry,
       "h3cFCoEFIPSnoopingENodeVLANIndex": h3cFCoEFIPSnoopingENodeVLANIndex,
       "h3cFCoEFIPSnoopingENodeIfIndex": h3cFCoEFIPSnoopingENodeIfIndex,
       "h3cFCoEFIPSnoopingENodeMAC": h3cFCoEFIPSnoopingENodeMAC,
       "h3cFCoEFIPSnoopingENodeName": h3cFCoEFIPSnoopingENodeName,
       "h3cFCoEFIPSnoopingVNTable": h3cFCoEFIPSnoopingVNTable,
       "h3cFCoEFIPSnoopingVNEntry": h3cFCoEFIPSnoopingVNEntry,
       "h3cFCoEFIPSnoopingVNVLANIndex": h3cFCoEFIPSnoopingVNVLANIndex,
       "h3cFCoEFIPSnoopingVNENodeIfIndex": h3cFCoEFIPSnoopingVNENodeIfIndex,
       "h3cFCoEFIPSnoopingVNENodeMAC": h3cFCoEFIPSnoopingVNENodeMAC,
       "h3cFCoEFIPSnoopingVNFCFMAC": h3cFCoEFIPSnoopingVNFCFMAC,
       "h3cFCoEFIPSnoopingVNMAC": h3cFCoEFIPSnoopingVNMAC,
       "h3cFCoEFIPSnoopingVNName": h3cFCoEFIPSnoopingVNName,
       "h3cFCoEFIPSnoopingVNFCFIfIndex": h3cFCoEFIPSnoopingVNFCFIfIndex,
       "h3cFCoEFIPSnoopingIfCfgTable": h3cFCoEFIPSnoopingIfCfgTable,
       "h3cFCoEFIPSnoopingIfCfgEntry": h3cFCoEFIPSnoopingIfCfgEntry,
       "h3cFCoEFIPSnoopingIfCfgIfIndex": h3cFCoEFIPSnoopingIfCfgIfIndex,
       "h3cFCoEFIPSnoopingIfCfgPortType": h3cFCoEFIPSnoopingIfCfgPortType}
)
