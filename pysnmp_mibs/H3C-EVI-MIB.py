# SNMP MIB module (H3C-EVI-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-EVI-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:20:38 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(IsisSystemID,) = mibBuilder.importSymbols(
    "ISIS-MIB",
    "IsisSystemID")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

h3cEvi = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132)
)
if mibBuilder.loadTexts:
    h3cEvi.setRevisions(
        ("2013-04-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class H3cEviMacType(TextualConvention, Integer32):
    status = "current"
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
        *(("other", 1),
          ("dynamic", 2),
          ("static", 3),
          ("flood", 4))
    )



class H3cEviNeighborStatus(TextualConvention, Integer32):
    status = "current"
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



# MIB Managed Objects in the order of their OIDs

_H3cEviNotifications_ObjectIdentity = ObjectIdentity
h3cEviNotifications = _H3cEviNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 0)
)
_H3cEviObjects_ObjectIdentity = ObjectIdentity
h3cEviObjects = _H3cEviObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1)
)
_H3cEviBase_ObjectIdentity = ObjectIdentity
h3cEviBase = _H3cEviBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 1)
)


class _H3cEviDesignatedVlan_Type(VlanId):
    """Custom type h3cEviDesignatedVlan based on VlanId"""
    defaultValue = 1


_H3cEviDesignatedVlan_Type.__name__ = "VlanId"
_H3cEviDesignatedVlan_Object = MibScalar
h3cEviDesignatedVlan = _H3cEviDesignatedVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 1, 1),
    _H3cEviDesignatedVlan_Type()
)
h3cEviDesignatedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviDesignatedVlan.setStatus("current")


class _H3cEviSiteID_Type(Integer32):
    """Custom type h3cEviSiteID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cEviSiteID_Type.__name__ = "Integer32"
_H3cEviSiteID_Object = MibScalar
h3cEviSiteID = _H3cEviSiteID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 1, 2),
    _H3cEviSiteID_Type()
)
h3cEviSiteID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviSiteID.setStatus("current")
_H3cEviIf_ObjectIdentity = ObjectIdentity
h3cEviIf = _H3cEviIf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2)
)
_H3cEviIfExtendVlanTable_Object = MibTable
h3cEviIfExtendVlanTable = _H3cEviIfExtendVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 1)
)
if mibBuilder.loadTexts:
    h3cEviIfExtendVlanTable.setStatus("current")
_H3cEviIfExtendVlanEntry_Object = MibTableRow
h3cEviIfExtendVlanEntry = _H3cEviIfExtendVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 1, 1)
)
h3cEviIfExtendVlanEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EVI-MIB", "h3cEviIfExtendVlanIndex"),
)
if mibBuilder.loadTexts:
    h3cEviIfExtendVlanEntry.setStatus("current")
_H3cEviIfExtendVlanIndex_Type = VlanId
_H3cEviIfExtendVlanIndex_Object = MibTableColumn
h3cEviIfExtendVlanIndex = _H3cEviIfExtendVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 1, 1, 1),
    _H3cEviIfExtendVlanIndex_Type()
)
h3cEviIfExtendVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviIfExtendVlanIndex.setStatus("current")


class _H3cEviIfExtendVlanLAV_Type(TruthValue):
    """Custom type h3cEviIfExtendVlanLAV based on TruthValue"""
    defaultValue = 2


_H3cEviIfExtendVlanLAV_Type.__name__ = "TruthValue"
_H3cEviIfExtendVlanLAV_Object = MibTableColumn
h3cEviIfExtendVlanLAV = _H3cEviIfExtendVlanLAV_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 1, 1, 2),
    _H3cEviIfExtendVlanLAV_Type()
)
h3cEviIfExtendVlanLAV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviIfExtendVlanLAV.setStatus("current")
_H3cEviIfExtendVlanRowStatus_Type = RowStatus
_H3cEviIfExtendVlanRowStatus_Object = MibTableColumn
h3cEviIfExtendVlanRowStatus = _H3cEviIfExtendVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 1, 1, 3),
    _H3cEviIfExtendVlanRowStatus_Type()
)
h3cEviIfExtendVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEviIfExtendVlanRowStatus.setStatus("current")
_H3cEviIfVlanMappingTable_Object = MibTable
h3cEviIfVlanMappingTable = _H3cEviIfVlanMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 2)
)
if mibBuilder.loadTexts:
    h3cEviIfVlanMappingTable.setStatus("current")
_H3cEviIfVlanMappingEntry_Object = MibTableRow
h3cEviIfVlanMappingEntry = _H3cEviIfVlanMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 2, 1)
)
h3cEviIfVlanMappingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EVI-MIB", "h3cEviIfVlanMappingSiteId"),
    (0, "H3C-EVI-MIB", "h3cEviIfVlanMappingSrc"),
    (0, "H3C-EVI-MIB", "h3cEviIfVlanMappingDst"),
)
if mibBuilder.loadTexts:
    h3cEviIfVlanMappingEntry.setStatus("current")


class _H3cEviIfVlanMappingSiteId_Type(Integer32):
    """Custom type h3cEviIfVlanMappingSiteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cEviIfVlanMappingSiteId_Type.__name__ = "Integer32"
_H3cEviIfVlanMappingSiteId_Object = MibTableColumn
h3cEviIfVlanMappingSiteId = _H3cEviIfVlanMappingSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 2, 1, 1),
    _H3cEviIfVlanMappingSiteId_Type()
)
h3cEviIfVlanMappingSiteId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviIfVlanMappingSiteId.setStatus("current")
_H3cEviIfVlanMappingSrc_Type = VlanId
_H3cEviIfVlanMappingSrc_Object = MibTableColumn
h3cEviIfVlanMappingSrc = _H3cEviIfVlanMappingSrc_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 2, 1, 2),
    _H3cEviIfVlanMappingSrc_Type()
)
h3cEviIfVlanMappingSrc.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviIfVlanMappingSrc.setStatus("current")
_H3cEviIfVlanMappingDst_Type = VlanId
_H3cEviIfVlanMappingDst_Object = MibTableColumn
h3cEviIfVlanMappingDst = _H3cEviIfVlanMappingDst_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 2, 1, 3),
    _H3cEviIfVlanMappingDst_Type()
)
h3cEviIfVlanMappingDst.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviIfVlanMappingDst.setStatus("current")
_H3cEviIfVlanMappingRowStatus_Type = RowStatus
_H3cEviIfVlanMappingRowStatus_Object = MibTableColumn
h3cEviIfVlanMappingRowStatus = _H3cEviIfVlanMappingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 2, 1, 4),
    _H3cEviIfVlanMappingRowStatus_Type()
)
h3cEviIfVlanMappingRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEviIfVlanMappingRowStatus.setStatus("current")
_H3cEviIfAttributeTable_Object = MibTable
h3cEviIfAttributeTable = _H3cEviIfAttributeTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 3)
)
if mibBuilder.loadTexts:
    h3cEviIfAttributeTable.setStatus("current")
_H3cEviIfAttributeEntry_Object = MibTableRow
h3cEviIfAttributeEntry = _H3cEviIfAttributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 3, 1)
)
h3cEviIfAttributeEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEviIfAttributeEntry.setStatus("current")


class _H3cEviIfFloodingMode_Type(TruthValue):
    """Custom type h3cEviIfFloodingMode based on TruthValue"""
    defaultValue = 2


_H3cEviIfFloodingMode_Type.__name__ = "TruthValue"
_H3cEviIfFloodingMode_Object = MibTableColumn
h3cEviIfFloodingMode = _H3cEviIfFloodingMode_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 3, 1, 1),
    _H3cEviIfFloodingMode_Type()
)
h3cEviIfFloodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviIfFloodingMode.setStatus("current")


class _H3cEviIfARPSuppression_Type(TruthValue):
    """Custom type h3cEviIfARPSuppression based on TruthValue"""
    defaultValue = 2


_H3cEviIfARPSuppression_Type.__name__ = "TruthValue"
_H3cEviIfARPSuppression_Object = MibTableColumn
h3cEviIfARPSuppression = _H3cEviIfARPSuppression_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 3, 1, 2),
    _H3cEviIfARPSuppression_Type()
)
h3cEviIfARPSuppression.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviIfARPSuppression.setStatus("current")
_H3cEviIfFloodingMacTable_Object = MibTable
h3cEviIfFloodingMacTable = _H3cEviIfFloodingMacTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 4)
)
if mibBuilder.loadTexts:
    h3cEviIfFloodingMacTable.setStatus("current")
_H3cEviIfFloodingMacEntry_Object = MibTableRow
h3cEviIfFloodingMacEntry = _H3cEviIfFloodingMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 4, 1)
)
h3cEviIfFloodingMacEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EVI-MIB", "h3cEviIfFloodingMacAddress"),
    (0, "H3C-EVI-MIB", "h3cEviIfFloodMacVlanIndex"),
)
if mibBuilder.loadTexts:
    h3cEviIfFloodingMacEntry.setStatus("current")
_H3cEviIfFloodingMacAddress_Type = MacAddress
_H3cEviIfFloodingMacAddress_Object = MibTableColumn
h3cEviIfFloodingMacAddress = _H3cEviIfFloodingMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 4, 1, 1),
    _H3cEviIfFloodingMacAddress_Type()
)
h3cEviIfFloodingMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviIfFloodingMacAddress.setStatus("current")
_H3cEviIfFloodMacVlanIndex_Type = VlanId
_H3cEviIfFloodMacVlanIndex_Object = MibTableColumn
h3cEviIfFloodMacVlanIndex = _H3cEviIfFloodMacVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 4, 1, 2),
    _H3cEviIfFloodMacVlanIndex_Type()
)
h3cEviIfFloodMacVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviIfFloodMacVlanIndex.setStatus("current")
_H3cEviIfFloodingMacRowStatus_Type = RowStatus
_H3cEviIfFloodingMacRowStatus_Object = MibTableColumn
h3cEviIfFloodingMacRowStatus = _H3cEviIfFloodingMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 2, 4, 1, 3),
    _H3cEviIfFloodingMacRowStatus_Type()
)
h3cEviIfFloodingMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEviIfFloodingMacRowStatus.setStatus("current")
_H3cEviMac_ObjectIdentity = ObjectIdentity
h3cEviMac = _H3cEviMac_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3)
)
_H3cEviMacCountTable_Object = MibTable
h3cEviMacCountTable = _H3cEviMacCountTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 1)
)
if mibBuilder.loadTexts:
    h3cEviMacCountTable.setStatus("current")
_H3cEviMacCountEntry_Object = MibTableRow
h3cEviMacCountEntry = _H3cEviMacCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 1, 1)
)
h3cEviMacCountEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEviMacCountEntry.setStatus("current")
_H3cEviMacLocalMacs_Type = Counter32
_H3cEviMacLocalMacs_Object = MibTableColumn
h3cEviMacLocalMacs = _H3cEviMacLocalMacs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 1, 1, 1),
    _H3cEviMacLocalMacs_Type()
)
h3cEviMacLocalMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviMacLocalMacs.setStatus("current")
_H3cEviMacLocalConflicts_Type = Counter32
_H3cEviMacLocalConflicts_Object = MibTableColumn
h3cEviMacLocalConflicts = _H3cEviMacLocalConflicts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 1, 1, 2),
    _H3cEviMacLocalConflicts_Type()
)
h3cEviMacLocalConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviMacLocalConflicts.setStatus("current")
_H3cEviMacRemoteMacs_Type = Counter32
_H3cEviMacRemoteMacs_Object = MibTableColumn
h3cEviMacRemoteMacs = _H3cEviMacRemoteMacs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 1, 1, 3),
    _H3cEviMacRemoteMacs_Type()
)
h3cEviMacRemoteMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviMacRemoteMacs.setStatus("current")
_H3cEviMacRemoteConflicts_Type = Counter32
_H3cEviMacRemoteConflicts_Object = MibTableColumn
h3cEviMacRemoteConflicts = _H3cEviMacRemoteConflicts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 1, 1, 4),
    _H3cEviMacRemoteConflicts_Type()
)
h3cEviMacRemoteConflicts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviMacRemoteConflicts.setStatus("current")
_H3cEviMacLocalTable_Object = MibTable
h3cEviMacLocalTable = _H3cEviMacLocalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 2)
)
if mibBuilder.loadTexts:
    h3cEviMacLocalTable.setStatus("current")
_H3cEviMacLocalEntry_Object = MibTableRow
h3cEviMacLocalEntry = _H3cEviMacLocalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 2, 1)
)
h3cEviMacLocalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EVI-MIB", "h3cEviMacLocalVlan"),
    (0, "H3C-EVI-MIB", "h3cEviMacLocalMacAddr"),
)
if mibBuilder.loadTexts:
    h3cEviMacLocalEntry.setStatus("current")
_H3cEviMacLocalVlan_Type = VlanId
_H3cEviMacLocalVlan_Object = MibTableColumn
h3cEviMacLocalVlan = _H3cEviMacLocalVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 2, 1, 1),
    _H3cEviMacLocalVlan_Type()
)
h3cEviMacLocalVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviMacLocalVlan.setStatus("current")
_H3cEviMacLocalMacAddr_Type = MacAddress
_H3cEviMacLocalMacAddr_Object = MibTableColumn
h3cEviMacLocalMacAddr = _H3cEviMacLocalMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 2, 1, 2),
    _H3cEviMacLocalMacAddr_Type()
)
h3cEviMacLocalMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviMacLocalMacAddr.setStatus("current")
_H3cEviMacLocalMacType_Type = H3cEviMacType
_H3cEviMacLocalMacType_Object = MibTableColumn
h3cEviMacLocalMacType = _H3cEviMacLocalMacType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 2, 1, 3),
    _H3cEviMacLocalMacType_Type()
)
h3cEviMacLocalMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviMacLocalMacType.setStatus("current")
_H3cEviMacLocalConflict_Type = TruthValue
_H3cEviMacLocalConflict_Object = MibTableColumn
h3cEviMacLocalConflict = _H3cEviMacLocalConflict_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 2, 1, 4),
    _H3cEviMacLocalConflict_Type()
)
h3cEviMacLocalConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviMacLocalConflict.setStatus("current")
_H3cEviMacLocalFiltered_Type = TruthValue
_H3cEviMacLocalFiltered_Object = MibTableColumn
h3cEviMacLocalFiltered = _H3cEviMacLocalFiltered_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 2, 1, 5),
    _H3cEviMacLocalFiltered_Type()
)
h3cEviMacLocalFiltered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviMacLocalFiltered.setStatus("current")
_H3cEviMacRemoteTable_Object = MibTable
h3cEviMacRemoteTable = _H3cEviMacRemoteTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 3)
)
if mibBuilder.loadTexts:
    h3cEviMacRemoteTable.setStatus("current")
_H3cEviMacRemoteEntry_Object = MibTableRow
h3cEviMacRemoteEntry = _H3cEviMacRemoteEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 3, 1)
)
h3cEviMacRemoteEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EVI-MIB", "h3cEviMacRemoteVlan"),
    (0, "H3C-EVI-MIB", "h3cEviMacRemoteMacAddr"),
)
if mibBuilder.loadTexts:
    h3cEviMacRemoteEntry.setStatus("current")
_H3cEviMacRemoteVlan_Type = VlanId
_H3cEviMacRemoteVlan_Object = MibTableColumn
h3cEviMacRemoteVlan = _H3cEviMacRemoteVlan_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 3, 1, 1),
    _H3cEviMacRemoteVlan_Type()
)
h3cEviMacRemoteVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviMacRemoteVlan.setStatus("current")
_H3cEviMacRemoteMacAddr_Type = MacAddress
_H3cEviMacRemoteMacAddr_Object = MibTableColumn
h3cEviMacRemoteMacAddr = _H3cEviMacRemoteMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 3, 1, 2),
    _H3cEviMacRemoteMacAddr_Type()
)
h3cEviMacRemoteMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviMacRemoteMacAddr.setStatus("current")
_H3cEviMacRemoteMacEffect_Type = TruthValue
_H3cEviMacRemoteMacEffect_Object = MibTableColumn
h3cEviMacRemoteMacEffect = _H3cEviMacRemoteMacEffect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 3, 1, 3),
    _H3cEviMacRemoteMacEffect_Type()
)
h3cEviMacRemoteMacEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviMacRemoteMacEffect.setStatus("current")
_H3cEviMacRemoteConflict_Type = TruthValue
_H3cEviMacRemoteConflict_Object = MibTableColumn
h3cEviMacRemoteConflict = _H3cEviMacRemoteConflict_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 3, 3, 1, 4),
    _H3cEviMacRemoteConflict_Type()
)
h3cEviMacRemoteConflict.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviMacRemoteConflict.setStatus("current")
_H3cEviProcess_ObjectIdentity = ObjectIdentity
h3cEviProcess = _H3cEviProcess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4)
)
_H3cEviProcessPolicyTable_Object = MibTable
h3cEviProcessPolicyTable = _H3cEviProcessPolicyTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 1)
)
if mibBuilder.loadTexts:
    h3cEviProcessPolicyTable.setStatus("current")
_H3cEviProcessPolicyEntry_Object = MibTableRow
h3cEviProcessPolicyEntry = _H3cEviProcessPolicyEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 1, 1)
)
h3cEviProcessPolicyEntry.setIndexNames(
    (0, "H3C-EVI-MIB", "h3cEviProcessId"),
)
if mibBuilder.loadTexts:
    h3cEviProcessPolicyEntry.setStatus("current")


class _H3cEviProcessId_Type(Unsigned32):
    """Custom type h3cEviProcessId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_H3cEviProcessId_Type.__name__ = "Unsigned32"
_H3cEviProcessId_Object = MibTableColumn
h3cEviProcessId = _H3cEviProcessId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 1, 1, 1),
    _H3cEviProcessId_Type()
)
h3cEviProcessId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cEviProcessId.setStatus("current")
_H3cEviProcessPolicy_Type = DisplayString
_H3cEviProcessPolicy_Object = MibTableColumn
h3cEviProcessPolicy = _H3cEviProcessPolicy_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 1, 1, 2),
    _H3cEviProcessPolicy_Type()
)
h3cEviProcessPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviProcessPolicy.setStatus("current")
_H3cEviProcessGrTable_Object = MibTable
h3cEviProcessGrTable = _H3cEviProcessGrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 2)
)
if mibBuilder.loadTexts:
    h3cEviProcessGrTable.setStatus("current")
_H3cEviProcessGrEntry_Object = MibTableRow
h3cEviProcessGrEntry = _H3cEviProcessGrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 2, 1)
)
h3cEviProcessGrEntry.setIndexNames(
    (0, "H3C-EVI-MIB", "h3cEviProcessId"),
)
if mibBuilder.loadTexts:
    h3cEviProcessGrEntry.setStatus("current")


class _H3cEviProcessGrEnable_Type(TruthValue):
    """Custom type h3cEviProcessGrEnable based on TruthValue"""
    defaultValue = 2


_H3cEviProcessGrEnable_Type.__name__ = "TruthValue"
_H3cEviProcessGrEnable_Object = MibTableColumn
h3cEviProcessGrEnable = _H3cEviProcessGrEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 2, 1, 1),
    _H3cEviProcessGrEnable_Type()
)
h3cEviProcessGrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviProcessGrEnable.setStatus("current")


class _H3cEviProcessGrInterval_Type(Unsigned32):
    """Custom type h3cEviProcessGrInterval based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1800),
    )


_H3cEviProcessGrInterval_Type.__name__ = "Unsigned32"
_H3cEviProcessGrInterval_Object = MibTableColumn
h3cEviProcessGrInterval = _H3cEviProcessGrInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 2, 1, 2),
    _H3cEviProcessGrInterval_Type()
)
h3cEviProcessGrInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviProcessGrInterval.setStatus("current")
_H3cEviProcessVSysTable_Object = MibTable
h3cEviProcessVSysTable = _H3cEviProcessVSysTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 3)
)
if mibBuilder.loadTexts:
    h3cEviProcessVSysTable.setStatus("current")
_H3cEviProcessVSysEntry_Object = MibTableRow
h3cEviProcessVSysEntry = _H3cEviProcessVSysEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 3, 1)
)
h3cEviProcessVSysEntry.setIndexNames(
    (0, "H3C-EVI-MIB", "h3cEviProcessId"),
    (0, "H3C-EVI-MIB", "h3cEviVirtualSysId"),
)
if mibBuilder.loadTexts:
    h3cEviProcessVSysEntry.setStatus("current")
_H3cEviVirtualSysId_Type = IsisSystemID
_H3cEviVirtualSysId_Object = MibTableColumn
h3cEviVirtualSysId = _H3cEviVirtualSysId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 3, 1, 1),
    _H3cEviVirtualSysId_Type()
)
h3cEviVirtualSysId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviVirtualSysId.setStatus("current")
_H3cEviVirtualSysRowStatus_Type = RowStatus
_H3cEviVirtualSysRowStatus_Object = MibTableColumn
h3cEviVirtualSysRowStatus = _H3cEviVirtualSysRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 4, 3, 1, 2),
    _H3cEviVirtualSysRowStatus_Type()
)
h3cEviVirtualSysRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEviVirtualSysRowStatus.setStatus("current")
_H3cEviISIS_ObjectIdentity = ObjectIdentity
h3cEviISIS = _H3cEviISIS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5)
)
_H3cEviISISNbrSummaryTable_Object = MibTable
h3cEviISISNbrSummaryTable = _H3cEviISISNbrSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 1)
)
if mibBuilder.loadTexts:
    h3cEviISISNbrSummaryTable.setStatus("current")
_H3cEviISISNbrSummaryEntry_Object = MibTableRow
h3cEviISISNbrSummaryEntry = _H3cEviISISNbrSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 1, 1)
)
h3cEviISISNbrSummaryEntry.setIndexNames(
    (0, "H3C-EVI-MIB", "h3cEviProcessId"),
)
if mibBuilder.loadTexts:
    h3cEviISISNbrSummaryEntry.setStatus("current")
_H3cEviISISNbrMaxMultiHomes_Type = Unsigned32
_H3cEviISISNbrMaxMultiHomes_Object = MibTableColumn
h3cEviISISNbrMaxMultiHomes = _H3cEviISISNbrMaxMultiHomes_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 1, 1, 1),
    _H3cEviISISNbrMaxMultiHomes_Type()
)
h3cEviISISNbrMaxMultiHomes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviISISNbrMaxMultiHomes.setStatus("current")
_H3cEviISISNbrSiteNbrs_Type = Unsigned32
_H3cEviISISNbrSiteNbrs_Object = MibTableColumn
h3cEviISISNbrSiteNbrs = _H3cEviISISNbrSiteNbrs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 1, 1, 2),
    _H3cEviISISNbrSiteNbrs_Type()
)
h3cEviISISNbrSiteNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviISISNbrSiteNbrs.setStatus("current")
_H3cEviISISNbrLinkNbrs_Type = Unsigned32
_H3cEviISISNbrLinkNbrs_Object = MibTableColumn
h3cEviISISNbrLinkNbrs = _H3cEviISISNbrLinkNbrs_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 1, 1, 3),
    _H3cEviISISNbrLinkNbrs_Type()
)
h3cEviISISNbrLinkNbrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviISISNbrLinkNbrs.setStatus("current")
_H3cEviISISNbrTable_Object = MibTable
h3cEviISISNbrTable = _H3cEviISISNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 2)
)
if mibBuilder.loadTexts:
    h3cEviISISNbrTable.setStatus("current")
_H3cEviISISNbrEntry_Object = MibTableRow
h3cEviISISNbrEntry = _H3cEviISISNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 2, 1)
)
h3cEviISISNbrEntry.setIndexNames(
    (0, "H3C-EVI-MIB", "h3cEviProcessId"),
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EVI-MIB", "h3cEviISISNbrSysId"),
)
if mibBuilder.loadTexts:
    h3cEviISISNbrEntry.setStatus("current")
_H3cEviISISNbrSysId_Type = IsisSystemID
_H3cEviISISNbrSysId_Object = MibTableColumn
h3cEviISISNbrSysId = _H3cEviISISNbrSysId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 2, 1, 1),
    _H3cEviISISNbrSysId_Type()
)
h3cEviISISNbrSysId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cEviISISNbrSysId.setStatus("current")
_H3cEviISISNbrMacAddr_Type = MacAddress
_H3cEviISISNbrMacAddr_Object = MibTableColumn
h3cEviISISNbrMacAddr = _H3cEviISISNbrMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 2, 1, 2),
    _H3cEviISISNbrMacAddr_Type()
)
h3cEviISISNbrMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviISISNbrMacAddr.setStatus("current")


class _H3cEviISISNbrSiteId_Type(Integer32):
    """Custom type h3cEviISISNbrSiteId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cEviISISNbrSiteId_Type.__name__ = "Integer32"
_H3cEviISISNbrSiteId_Object = MibTableColumn
h3cEviISISNbrSiteId = _H3cEviISISNbrSiteId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 2, 1, 3),
    _H3cEviISISNbrSiteId_Type()
)
h3cEviISISNbrSiteId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviISISNbrSiteId.setStatus("current")
_H3cEviISISNbrTransStatus_Type = TruthValue
_H3cEviISISNbrTransStatus_Object = MibTableColumn
h3cEviISISNbrTransStatus = _H3cEviISISNbrTransStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 5, 2, 1, 4),
    _H3cEviISISNbrTransStatus_Type()
)
h3cEviISISNbrTransStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviISISNbrTransStatus.setStatus("current")
_H3cEviEnable_ObjectIdentity = ObjectIdentity
h3cEviEnable = _H3cEviEnable_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 6)
)
_H3cEviEnableTable_Object = MibTable
h3cEviEnableTable = _H3cEviEnableTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 6, 1)
)
if mibBuilder.loadTexts:
    h3cEviEnableTable.setStatus("current")
_H3cEviEnableEntry_Object = MibTableRow
h3cEviEnableEntry = _H3cEviEnableEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 6, 1, 1)
)
h3cEviEnableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEviEnableEntry.setStatus("current")


class _H3cEviEnableStatus_Type(TruthValue):
    """Custom type h3cEviEnableStatus based on TruthValue"""
    defaultValue = 2


_H3cEviEnableStatus_Type.__name__ = "TruthValue"
_H3cEviEnableStatus_Object = MibTableColumn
h3cEviEnableStatus = _H3cEviEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 6, 1, 1, 1),
    _H3cEviEnableStatus_Type()
)
h3cEviEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviEnableStatus.setStatus("current")
_H3cEviNbr_ObjectIdentity = ObjectIdentity
h3cEviNbr = _H3cEviNbr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7)
)
_H3cEviNbrBaseTable_Object = MibTable
h3cEviNbrBaseTable = _H3cEviNbrBaseTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 1)
)
if mibBuilder.loadTexts:
    h3cEviNbrBaseTable.setStatus("current")
_H3cEviNbrBaseEntry_Object = MibTableRow
h3cEviNbrBaseEntry = _H3cEviNbrBaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 1, 1)
)
h3cEviNbrBaseEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cEviNbrBaseEntry.setStatus("current")


class _H3cEviNbrSelfServerStatus_Type(TruthValue):
    """Custom type h3cEviNbrSelfServerStatus based on TruthValue"""
    defaultValue = 2


_H3cEviNbrSelfServerStatus_Type.__name__ = "TruthValue"
_H3cEviNbrSelfServerStatus_Object = MibTableColumn
h3cEviNbrSelfServerStatus = _H3cEviNbrSelfServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 1, 1, 1),
    _H3cEviNbrSelfServerStatus_Type()
)
h3cEviNbrSelfServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviNbrSelfServerStatus.setStatus("current")


class _H3cEviNbrAuthPassword_Type(OctetString):
    """Custom type h3cEviNbrAuthPassword based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 24),
    )


_H3cEviNbrAuthPassword_Type.__name__ = "OctetString"
_H3cEviNbrAuthPassword_Object = MibTableColumn
h3cEviNbrAuthPassword = _H3cEviNbrAuthPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 1, 1, 2),
    _H3cEviNbrAuthPassword_Type()
)
h3cEviNbrAuthPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviNbrAuthPassword.setStatus("current")


class _H3cEviNbrClientRegisterInterval_Type(Integer32):
    """Custom type h3cEviNbrClientRegisterInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 120),
    )


_H3cEviNbrClientRegisterInterval_Type.__name__ = "Integer32"
_H3cEviNbrClientRegisterInterval_Object = MibTableColumn
h3cEviNbrClientRegisterInterval = _H3cEviNbrClientRegisterInterval_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 1, 1, 3),
    _H3cEviNbrClientRegisterInterval_Type()
)
h3cEviNbrClientRegisterInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEviNbrClientRegisterInterval.setStatus("current")
_H3cEviNbrRemoteServerTable_Object = MibTable
h3cEviNbrRemoteServerTable = _H3cEviNbrRemoteServerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 2)
)
if mibBuilder.loadTexts:
    h3cEviNbrRemoteServerTable.setStatus("current")
_H3cEviNbrRemoteServerEntry_Object = MibTableRow
h3cEviNbrRemoteServerEntry = _H3cEviNbrRemoteServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 2, 1)
)
h3cEviNbrRemoteServerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EVI-MIB", "h3cEviNbrRemoteServerType"),
    (0, "H3C-EVI-MIB", "h3cEviNbrRemoteServer"),
)
if mibBuilder.loadTexts:
    h3cEviNbrRemoteServerEntry.setStatus("current")
_H3cEviNbrRemoteServerType_Type = InetAddressType
_H3cEviNbrRemoteServerType_Object = MibTableColumn
h3cEviNbrRemoteServerType = _H3cEviNbrRemoteServerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 2, 1, 1),
    _H3cEviNbrRemoteServerType_Type()
)
h3cEviNbrRemoteServerType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviNbrRemoteServerType.setStatus("current")
_H3cEviNbrRemoteServer_Type = InetAddress
_H3cEviNbrRemoteServer_Object = MibTableColumn
h3cEviNbrRemoteServer = _H3cEviNbrRemoteServer_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 2, 1, 2),
    _H3cEviNbrRemoteServer_Type()
)
h3cEviNbrRemoteServer.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviNbrRemoteServer.setStatus("current")
_H3cEviNbrRemoteServerRowStatus_Type = RowStatus
_H3cEviNbrRemoteServerRowStatus_Object = MibTableColumn
h3cEviNbrRemoteServerRowStatus = _H3cEviNbrRemoteServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 2, 1, 3),
    _H3cEviNbrRemoteServerRowStatus_Type()
)
h3cEviNbrRemoteServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEviNbrRemoteServerRowStatus.setStatus("current")
_H3cEviNbrTable_Object = MibTable
h3cEviNbrTable = _H3cEviNbrTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 3)
)
if mibBuilder.loadTexts:
    h3cEviNbrTable.setStatus("current")
_H3cEviNbrEntry_Object = MibTableRow
h3cEviNbrEntry = _H3cEviNbrEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 3, 1)
)
h3cEviNbrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-EVI-MIB", "h3cEviNbrAddressType"),
    (0, "H3C-EVI-MIB", "h3cEviNbrAddress"),
)
if mibBuilder.loadTexts:
    h3cEviNbrEntry.setStatus("current")
_H3cEviNbrAddressType_Type = InetAddressType
_H3cEviNbrAddressType_Object = MibTableColumn
h3cEviNbrAddressType = _H3cEviNbrAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 3, 1, 1),
    _H3cEviNbrAddressType_Type()
)
h3cEviNbrAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviNbrAddressType.setStatus("current")
_H3cEviNbrAddress_Type = InetAddress
_H3cEviNbrAddress_Object = MibTableColumn
h3cEviNbrAddress = _H3cEviNbrAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 3, 1, 2),
    _H3cEviNbrAddress_Type()
)
h3cEviNbrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEviNbrAddress.setStatus("current")
_H3cEviNbrSystemID_Type = MacAddress
_H3cEviNbrSystemID_Object = MibTableColumn
h3cEviNbrSystemID = _H3cEviNbrSystemID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 3, 1, 3),
    _H3cEviNbrSystemID_Type()
)
h3cEviNbrSystemID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviNbrSystemID.setStatus("current")
_H3cEviNbrExpireTime_Type = Integer32
_H3cEviNbrExpireTime_Object = MibTableColumn
h3cEviNbrExpireTime = _H3cEviNbrExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 3, 1, 4),
    _H3cEviNbrExpireTime_Type()
)
h3cEviNbrExpireTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviNbrExpireTime.setStatus("current")
_H3cEviNbrStatus_Type = H3cEviNeighborStatus
_H3cEviNbrStatus_Object = MibTableColumn
h3cEviNbrStatus = _H3cEviNbrStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 1, 7, 3, 1, 5),
    _H3cEviNbrStatus_Type()
)
h3cEviNbrStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEviNbrStatus.setStatus("current")

# Managed Objects groups


# Notification objects

h3cEviNewDed = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 0, 1)
)
h3cEviNewDed.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("H3C-EVI-MIB", "h3cEviProcessId"),
        ("H3C-EVI-MIB", "h3cEviISISNbrSysId"))
)
if mibBuilder.loadTexts:
    h3cEviNewDed.setStatus(
        "current"
    )

h3cEviSiteEDTopoChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 0, 2)
)
h3cEviSiteEDTopoChange.setObjects(
      *(("H3C-EVI-MIB", "h3cEviProcessId"),
        ("H3C-EVI-MIB", "h3cEviISISNbrSiteNbrs"))
)
if mibBuilder.loadTexts:
    h3cEviSiteEDTopoChange.setStatus(
        "current"
    )

h3cEviEDLinkDisconnect = NotificationType(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 132, 0, 3)
)
h3cEviEDLinkDisconnect.setObjects(
    ("H3C-EVI-MIB", "h3cEviProcessId")
)
if mibBuilder.loadTexts:
    h3cEviEDLinkDisconnect.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-EVI-MIB",
    **{"H3cEviMacType": H3cEviMacType,
       "H3cEviNeighborStatus": H3cEviNeighborStatus,
       "h3cEvi": h3cEvi,
       "h3cEviNotifications": h3cEviNotifications,
       "h3cEviNewDed": h3cEviNewDed,
       "h3cEviSiteEDTopoChange": h3cEviSiteEDTopoChange,
       "h3cEviEDLinkDisconnect": h3cEviEDLinkDisconnect,
       "h3cEviObjects": h3cEviObjects,
       "h3cEviBase": h3cEviBase,
       "h3cEviDesignatedVlan": h3cEviDesignatedVlan,
       "h3cEviSiteID": h3cEviSiteID,
       "h3cEviIf": h3cEviIf,
       "h3cEviIfExtendVlanTable": h3cEviIfExtendVlanTable,
       "h3cEviIfExtendVlanEntry": h3cEviIfExtendVlanEntry,
       "h3cEviIfExtendVlanIndex": h3cEviIfExtendVlanIndex,
       "h3cEviIfExtendVlanLAV": h3cEviIfExtendVlanLAV,
       "h3cEviIfExtendVlanRowStatus": h3cEviIfExtendVlanRowStatus,
       "h3cEviIfVlanMappingTable": h3cEviIfVlanMappingTable,
       "h3cEviIfVlanMappingEntry": h3cEviIfVlanMappingEntry,
       "h3cEviIfVlanMappingSiteId": h3cEviIfVlanMappingSiteId,
       "h3cEviIfVlanMappingSrc": h3cEviIfVlanMappingSrc,
       "h3cEviIfVlanMappingDst": h3cEviIfVlanMappingDst,
       "h3cEviIfVlanMappingRowStatus": h3cEviIfVlanMappingRowStatus,
       "h3cEviIfAttributeTable": h3cEviIfAttributeTable,
       "h3cEviIfAttributeEntry": h3cEviIfAttributeEntry,
       "h3cEviIfFloodingMode": h3cEviIfFloodingMode,
       "h3cEviIfARPSuppression": h3cEviIfARPSuppression,
       "h3cEviIfFloodingMacTable": h3cEviIfFloodingMacTable,
       "h3cEviIfFloodingMacEntry": h3cEviIfFloodingMacEntry,
       "h3cEviIfFloodingMacAddress": h3cEviIfFloodingMacAddress,
       "h3cEviIfFloodMacVlanIndex": h3cEviIfFloodMacVlanIndex,
       "h3cEviIfFloodingMacRowStatus": h3cEviIfFloodingMacRowStatus,
       "h3cEviMac": h3cEviMac,
       "h3cEviMacCountTable": h3cEviMacCountTable,
       "h3cEviMacCountEntry": h3cEviMacCountEntry,
       "h3cEviMacLocalMacs": h3cEviMacLocalMacs,
       "h3cEviMacLocalConflicts": h3cEviMacLocalConflicts,
       "h3cEviMacRemoteMacs": h3cEviMacRemoteMacs,
       "h3cEviMacRemoteConflicts": h3cEviMacRemoteConflicts,
       "h3cEviMacLocalTable": h3cEviMacLocalTable,
       "h3cEviMacLocalEntry": h3cEviMacLocalEntry,
       "h3cEviMacLocalVlan": h3cEviMacLocalVlan,
       "h3cEviMacLocalMacAddr": h3cEviMacLocalMacAddr,
       "h3cEviMacLocalMacType": h3cEviMacLocalMacType,
       "h3cEviMacLocalConflict": h3cEviMacLocalConflict,
       "h3cEviMacLocalFiltered": h3cEviMacLocalFiltered,
       "h3cEviMacRemoteTable": h3cEviMacRemoteTable,
       "h3cEviMacRemoteEntry": h3cEviMacRemoteEntry,
       "h3cEviMacRemoteVlan": h3cEviMacRemoteVlan,
       "h3cEviMacRemoteMacAddr": h3cEviMacRemoteMacAddr,
       "h3cEviMacRemoteMacEffect": h3cEviMacRemoteMacEffect,
       "h3cEviMacRemoteConflict": h3cEviMacRemoteConflict,
       "h3cEviProcess": h3cEviProcess,
       "h3cEviProcessPolicyTable": h3cEviProcessPolicyTable,
       "h3cEviProcessPolicyEntry": h3cEviProcessPolicyEntry,
       "h3cEviProcessId": h3cEviProcessId,
       "h3cEviProcessPolicy": h3cEviProcessPolicy,
       "h3cEviProcessGrTable": h3cEviProcessGrTable,
       "h3cEviProcessGrEntry": h3cEviProcessGrEntry,
       "h3cEviProcessGrEnable": h3cEviProcessGrEnable,
       "h3cEviProcessGrInterval": h3cEviProcessGrInterval,
       "h3cEviProcessVSysTable": h3cEviProcessVSysTable,
       "h3cEviProcessVSysEntry": h3cEviProcessVSysEntry,
       "h3cEviVirtualSysId": h3cEviVirtualSysId,
       "h3cEviVirtualSysRowStatus": h3cEviVirtualSysRowStatus,
       "h3cEviISIS": h3cEviISIS,
       "h3cEviISISNbrSummaryTable": h3cEviISISNbrSummaryTable,
       "h3cEviISISNbrSummaryEntry": h3cEviISISNbrSummaryEntry,
       "h3cEviISISNbrMaxMultiHomes": h3cEviISISNbrMaxMultiHomes,
       "h3cEviISISNbrSiteNbrs": h3cEviISISNbrSiteNbrs,
       "h3cEviISISNbrLinkNbrs": h3cEviISISNbrLinkNbrs,
       "h3cEviISISNbrTable": h3cEviISISNbrTable,
       "h3cEviISISNbrEntry": h3cEviISISNbrEntry,
       "h3cEviISISNbrSysId": h3cEviISISNbrSysId,
       "h3cEviISISNbrMacAddr": h3cEviISISNbrMacAddr,
       "h3cEviISISNbrSiteId": h3cEviISISNbrSiteId,
       "h3cEviISISNbrTransStatus": h3cEviISISNbrTransStatus,
       "h3cEviEnable": h3cEviEnable,
       "h3cEviEnableTable": h3cEviEnableTable,
       "h3cEviEnableEntry": h3cEviEnableEntry,
       "h3cEviEnableStatus": h3cEviEnableStatus,
       "h3cEviNbr": h3cEviNbr,
       "h3cEviNbrBaseTable": h3cEviNbrBaseTable,
       "h3cEviNbrBaseEntry": h3cEviNbrBaseEntry,
       "h3cEviNbrSelfServerStatus": h3cEviNbrSelfServerStatus,
       "h3cEviNbrAuthPassword": h3cEviNbrAuthPassword,
       "h3cEviNbrClientRegisterInterval": h3cEviNbrClientRegisterInterval,
       "h3cEviNbrRemoteServerTable": h3cEviNbrRemoteServerTable,
       "h3cEviNbrRemoteServerEntry": h3cEviNbrRemoteServerEntry,
       "h3cEviNbrRemoteServerType": h3cEviNbrRemoteServerType,
       "h3cEviNbrRemoteServer": h3cEviNbrRemoteServer,
       "h3cEviNbrRemoteServerRowStatus": h3cEviNbrRemoteServerRowStatus,
       "h3cEviNbrTable": h3cEviNbrTable,
       "h3cEviNbrEntry": h3cEviNbrEntry,
       "h3cEviNbrAddressType": h3cEviNbrAddressType,
       "h3cEviNbrAddress": h3cEviNbrAddress,
       "h3cEviNbrSystemID": h3cEviNbrSystemID,
       "h3cEviNbrExpireTime": h3cEviNbrExpireTime,
       "h3cEviNbrStatus": h3cEviNbrStatus}
)
