# SNMP MIB module (BAY-STACK-IGMP-EXT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/BAY-STACK-IGMP-EXT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:36 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanId) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

bayStackIgmpExtMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 32)
)
if mibBuilder.loadTexts:
    bayStackIgmpExtMib.setRevisions(
        ("2016-03-09 00:00",
         "2015-12-21 00:00",
         "2015-08-10 00:00",
         "2009-10-26 00:00",
         "2009-01-19 00:00",
         "2008-11-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BsIgmpExtNotifications_ObjectIdentity = ObjectIdentity
bsIgmpExtNotifications = _BsIgmpExtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 0)
)
_BsIgmpExtObjects_ObjectIdentity = ObjectIdentity
bsIgmpExtObjects = _BsIgmpExtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1)
)
_BsIgmpExtFilterProfileTable_Object = MibTable
bsIgmpExtFilterProfileTable = _BsIgmpExtFilterProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 1)
)
if mibBuilder.loadTexts:
    bsIgmpExtFilterProfileTable.setStatus("current")
_BsIgmpExtFilterProfileEntry_Object = MibTableRow
bsIgmpExtFilterProfileEntry = _BsIgmpExtFilterProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 1, 1)
)
bsIgmpExtFilterProfileEntry.setIndexNames(
    (0, "BAY-STACK-IGMP-EXT-MIB", "bsIgmpExtFilterProfileId"),
)
if mibBuilder.loadTexts:
    bsIgmpExtFilterProfileEntry.setStatus("current")


class _BsIgmpExtFilterProfileId_Type(Integer32):
    """Custom type bsIgmpExtFilterProfileId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_BsIgmpExtFilterProfileId_Type.__name__ = "Integer32"
_BsIgmpExtFilterProfileId_Object = MibTableColumn
bsIgmpExtFilterProfileId = _BsIgmpExtFilterProfileId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 1, 1, 1),
    _BsIgmpExtFilterProfileId_Type()
)
bsIgmpExtFilterProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIgmpExtFilterProfileId.setStatus("current")


class _BsIgmpExtFilterProfileType_Type(Integer32):
    """Custom type bsIgmpExtFilterProfileType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_BsIgmpExtFilterProfileType_Type.__name__ = "Integer32"
_BsIgmpExtFilterProfileType_Object = MibTableColumn
bsIgmpExtFilterProfileType = _BsIgmpExtFilterProfileType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 1, 1, 2),
    _BsIgmpExtFilterProfileType_Type()
)
bsIgmpExtFilterProfileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIgmpExtFilterProfileType.setStatus("current")


class _BsIgmpExtFilterProfilePortList_Type(PortList):
    """Custom type bsIgmpExtFilterProfilePortList based on PortList"""
    defaultHexValue = ""


_BsIgmpExtFilterProfilePortList_Type.__name__ = "PortList"
_BsIgmpExtFilterProfilePortList_Object = MibTableColumn
bsIgmpExtFilterProfilePortList = _BsIgmpExtFilterProfilePortList_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 1, 1, 3),
    _BsIgmpExtFilterProfilePortList_Type()
)
bsIgmpExtFilterProfilePortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIgmpExtFilterProfilePortList.setStatus("current")
_BsIgmpExtFilterProfileRowStatus_Type = RowStatus
_BsIgmpExtFilterProfileRowStatus_Object = MibTableColumn
bsIgmpExtFilterProfileRowStatus = _BsIgmpExtFilterProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 1, 1, 4),
    _BsIgmpExtFilterProfileRowStatus_Type()
)
bsIgmpExtFilterProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIgmpExtFilterProfileRowStatus.setStatus("current")
_BsIgmpExtFilterProfileDroppedPackets_Type = Counter32
_BsIgmpExtFilterProfileDroppedPackets_Object = MibTableColumn
bsIgmpExtFilterProfileDroppedPackets = _BsIgmpExtFilterProfileDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 1, 1, 5),
    _BsIgmpExtFilterProfileDroppedPackets_Type()
)
bsIgmpExtFilterProfileDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIgmpExtFilterProfileDroppedPackets.setStatus("current")
_BsIgmpExtFilterRangeTable_Object = MibTable
bsIgmpExtFilterRangeTable = _BsIgmpExtFilterRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 2)
)
if mibBuilder.loadTexts:
    bsIgmpExtFilterRangeTable.setStatus("current")
_BsIgmpExtFilterRangeEntry_Object = MibTableRow
bsIgmpExtFilterRangeEntry = _BsIgmpExtFilterRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 2, 1)
)
bsIgmpExtFilterRangeEntry.setIndexNames(
    (0, "BAY-STACK-IGMP-EXT-MIB", "bsIgmpExtFilterProfileId"),
    (0, "BAY-STACK-IGMP-EXT-MIB", "bsIgmpExtFilterRangeId"),
)
if mibBuilder.loadTexts:
    bsIgmpExtFilterRangeEntry.setStatus("current")


class _BsIgmpExtFilterRangeId_Type(Integer32):
    """Custom type bsIgmpExtFilterRangeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_BsIgmpExtFilterRangeId_Type.__name__ = "Integer32"
_BsIgmpExtFilterRangeId_Object = MibTableColumn
bsIgmpExtFilterRangeId = _BsIgmpExtFilterRangeId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 2, 1, 1),
    _BsIgmpExtFilterRangeId_Type()
)
bsIgmpExtFilterRangeId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIgmpExtFilterRangeId.setStatus("current")
_BsIgmpExtFilterRangeAddressType_Type = InetAddressType
_BsIgmpExtFilterRangeAddressType_Object = MibTableColumn
bsIgmpExtFilterRangeAddressType = _BsIgmpExtFilterRangeAddressType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 2, 1, 2),
    _BsIgmpExtFilterRangeAddressType_Type()
)
bsIgmpExtFilterRangeAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIgmpExtFilterRangeAddressType.setStatus("current")
_BsIgmpExtFilterRangeAddressStart_Type = InetAddress
_BsIgmpExtFilterRangeAddressStart_Object = MibTableColumn
bsIgmpExtFilterRangeAddressStart = _BsIgmpExtFilterRangeAddressStart_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 2, 1, 3),
    _BsIgmpExtFilterRangeAddressStart_Type()
)
bsIgmpExtFilterRangeAddressStart.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIgmpExtFilterRangeAddressStart.setStatus("current")
_BsIgmpExtFilterRangeAddressEnd_Type = InetAddress
_BsIgmpExtFilterRangeAddressEnd_Object = MibTableColumn
bsIgmpExtFilterRangeAddressEnd = _BsIgmpExtFilterRangeAddressEnd_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 2, 1, 4),
    _BsIgmpExtFilterRangeAddressEnd_Type()
)
bsIgmpExtFilterRangeAddressEnd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIgmpExtFilterRangeAddressEnd.setStatus("current")
_BsIgmpExtFilterRangeRowStatus_Type = RowStatus
_BsIgmpExtFilterRangeRowStatus_Object = MibTableColumn
bsIgmpExtFilterRangeRowStatus = _BsIgmpExtFilterRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 2, 1, 5),
    _BsIgmpExtFilterRangeRowStatus_Type()
)
bsIgmpExtFilterRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIgmpExtFilterRangeRowStatus.setStatus("current")
_BsIgmpExtFilterProfileScalars_ObjectIdentity = ObjectIdentity
bsIgmpExtFilterProfileScalars = _BsIgmpExtFilterProfileScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 3)
)


class _BsIgmpExtFilterProfileClearStats_Type(Integer32):
    """Custom type bsIgmpExtFilterProfileClearStats based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_BsIgmpExtFilterProfileClearStats_Type.__name__ = "Integer32"
_BsIgmpExtFilterProfileClearStats_Object = MibScalar
bsIgmpExtFilterProfileClearStats = _BsIgmpExtFilterProfileClearStats_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 3, 1),
    _BsIgmpExtFilterProfileClearStats_Type()
)
bsIgmpExtFilterProfileClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIgmpExtFilterProfileClearStats.setStatus("current")
_BsIgmpExtScalars_ObjectIdentity = ObjectIdentity
bsIgmpExtScalars = _BsIgmpExtScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 4)
)
_BsIgmpExtAvailableHardwareResources_Type = Gauge32
_BsIgmpExtAvailableHardwareResources_Object = MibScalar
bsIgmpExtAvailableHardwareResources = _BsIgmpExtAvailableHardwareResources_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 4, 1),
    _BsIgmpExtAvailableHardwareResources_Type()
)
bsIgmpExtAvailableHardwareResources.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIgmpExtAvailableHardwareResources.setStatus("current")


class _BsIgmpExtHardwareCompatibilityMode_Type(Integer32):
    """Custom type bsIgmpExtHardwareCompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ers5510", 1),
          ("nonErs5510", 2))
    )


_BsIgmpExtHardwareCompatibilityMode_Type.__name__ = "Integer32"
_BsIgmpExtHardwareCompatibilityMode_Object = MibScalar
bsIgmpExtHardwareCompatibilityMode = _BsIgmpExtHardwareCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 4, 2),
    _BsIgmpExtHardwareCompatibilityMode_Type()
)
bsIgmpExtHardwareCompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIgmpExtHardwareCompatibilityMode.setStatus("current")


class _BsIgmpExtStreamFlushAll_Type(Integer32):
    """Custom type bsIgmpExtStreamFlushAll based on Integer32"""
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
        *(("none", 1),
          ("flushAllGroup", 2),
          ("flushAllStream", 3),
          ("flushAllMrouter", 4),
          ("flushAll", 5))
    )


_BsIgmpExtStreamFlushAll_Type.__name__ = "Integer32"
_BsIgmpExtStreamFlushAll_Object = MibScalar
bsIgmpExtStreamFlushAll = _BsIgmpExtStreamFlushAll_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 4, 3),
    _BsIgmpExtStreamFlushAll_Type()
)
bsIgmpExtStreamFlushAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIgmpExtStreamFlushAll.setStatus("current")
_BsIgmpExtStreamCount_Type = Gauge32
_BsIgmpExtStreamCount_Object = MibScalar
bsIgmpExtStreamCount = _BsIgmpExtStreamCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 4, 4),
    _BsIgmpExtStreamCount_Type()
)
bsIgmpExtStreamCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIgmpExtStreamCount.setStatus("current")
_BsIgmpExtGroupCount_Type = Gauge32
_BsIgmpExtGroupCount_Object = MibScalar
bsIgmpExtGroupCount = _BsIgmpExtGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 4, 5),
    _BsIgmpExtGroupCount_Type()
)
bsIgmpExtGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bsIgmpExtGroupCount.setStatus("current")
_BsIgmpExtMvrGlobal_ObjectIdentity = ObjectIdentity
bsIgmpExtMvrGlobal = _BsIgmpExtMvrGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 5)
)
_BsIgmpExtMvrGlobalEnable_Type = TruthValue
_BsIgmpExtMvrGlobalEnable_Object = MibScalar
bsIgmpExtMvrGlobalEnable = _BsIgmpExtMvrGlobalEnable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 5, 1),
    _BsIgmpExtMvrGlobalEnable_Type()
)
bsIgmpExtMvrGlobalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIgmpExtMvrGlobalEnable.setStatus("current")
_BsIgmpExtMvrGlobalSourceVlan_Type = VlanId
_BsIgmpExtMvrGlobalSourceVlan_Object = MibScalar
bsIgmpExtMvrGlobalSourceVlan = _BsIgmpExtMvrGlobalSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 5, 2),
    _BsIgmpExtMvrGlobalSourceVlan_Type()
)
bsIgmpExtMvrGlobalSourceVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bsIgmpExtMvrGlobalSourceVlan.setStatus("current")
_BsIgmpExtMvrGroupRangeTable_Object = MibTable
bsIgmpExtMvrGroupRangeTable = _BsIgmpExtMvrGroupRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 6)
)
if mibBuilder.loadTexts:
    bsIgmpExtMvrGroupRangeTable.setStatus("current")
_BsIgmpExtMvrGroupRangeEntry_Object = MibTableRow
bsIgmpExtMvrGroupRangeEntry = _BsIgmpExtMvrGroupRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 6, 1)
)
bsIgmpExtMvrGroupRangeEntry.setIndexNames(
    (0, "BAY-STACK-IGMP-EXT-MIB", "bsIgmpExtMvrGroupRangeAddress"),
    (0, "BAY-STACK-IGMP-EXT-MIB", "bsIgmpExtMvrGroupRangeMask"),
)
if mibBuilder.loadTexts:
    bsIgmpExtMvrGroupRangeEntry.setStatus("current")
_BsIgmpExtMvrGroupRangeAddress_Type = IpAddress
_BsIgmpExtMvrGroupRangeAddress_Object = MibTableColumn
bsIgmpExtMvrGroupRangeAddress = _BsIgmpExtMvrGroupRangeAddress_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 6, 1, 1),
    _BsIgmpExtMvrGroupRangeAddress_Type()
)
bsIgmpExtMvrGroupRangeAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIgmpExtMvrGroupRangeAddress.setStatus("current")
_BsIgmpExtMvrGroupRangeMask_Type = IpAddress
_BsIgmpExtMvrGroupRangeMask_Object = MibTableColumn
bsIgmpExtMvrGroupRangeMask = _BsIgmpExtMvrGroupRangeMask_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 6, 1, 2),
    _BsIgmpExtMvrGroupRangeMask_Type()
)
bsIgmpExtMvrGroupRangeMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIgmpExtMvrGroupRangeMask.setStatus("current")
_BsIgmpExtMvrGroupRangeRowStatus_Type = RowStatus
_BsIgmpExtMvrGroupRangeRowStatus_Object = MibTableColumn
bsIgmpExtMvrGroupRangeRowStatus = _BsIgmpExtMvrGroupRangeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 6, 1, 3),
    _BsIgmpExtMvrGroupRangeRowStatus_Type()
)
bsIgmpExtMvrGroupRangeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIgmpExtMvrGroupRangeRowStatus.setStatus("current")
_BsIgmpExtMvrReceiversTable_Object = MibTable
bsIgmpExtMvrReceiversTable = _BsIgmpExtMvrReceiversTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 7)
)
if mibBuilder.loadTexts:
    bsIgmpExtMvrReceiversTable.setStatus("current")
_BsIgmpExtMvrReceiversEntry_Object = MibTableRow
bsIgmpExtMvrReceiversEntry = _BsIgmpExtMvrReceiversEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 7, 1)
)
bsIgmpExtMvrReceiversEntry.setIndexNames(
    (0, "BAY-STACK-IGMP-EXT-MIB", "bsIgmpExtMvrReceiversVlanId"),
)
if mibBuilder.loadTexts:
    bsIgmpExtMvrReceiversEntry.setStatus("current")
_BsIgmpExtMvrReceiversVlanId_Type = VlanId
_BsIgmpExtMvrReceiversVlanId_Object = MibTableColumn
bsIgmpExtMvrReceiversVlanId = _BsIgmpExtMvrReceiversVlanId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 7, 1, 1),
    _BsIgmpExtMvrReceiversVlanId_Type()
)
bsIgmpExtMvrReceiversVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bsIgmpExtMvrReceiversVlanId.setStatus("current")
_BsIgmpExtMvrReceiversRowStatus_Type = RowStatus
_BsIgmpExtMvrReceiversRowStatus_Object = MibTableColumn
bsIgmpExtMvrReceiversRowStatus = _BsIgmpExtMvrReceiversRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 32, 1, 7, 1, 2),
    _BsIgmpExtMvrReceiversRowStatus_Type()
)
bsIgmpExtMvrReceiversRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bsIgmpExtMvrReceiversRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BAY-STACK-IGMP-EXT-MIB",
    **{"bayStackIgmpExtMib": bayStackIgmpExtMib,
       "bsIgmpExtNotifications": bsIgmpExtNotifications,
       "bsIgmpExtObjects": bsIgmpExtObjects,
       "bsIgmpExtFilterProfileTable": bsIgmpExtFilterProfileTable,
       "bsIgmpExtFilterProfileEntry": bsIgmpExtFilterProfileEntry,
       "bsIgmpExtFilterProfileId": bsIgmpExtFilterProfileId,
       "bsIgmpExtFilterProfileType": bsIgmpExtFilterProfileType,
       "bsIgmpExtFilterProfilePortList": bsIgmpExtFilterProfilePortList,
       "bsIgmpExtFilterProfileRowStatus": bsIgmpExtFilterProfileRowStatus,
       "bsIgmpExtFilterProfileDroppedPackets": bsIgmpExtFilterProfileDroppedPackets,
       "bsIgmpExtFilterRangeTable": bsIgmpExtFilterRangeTable,
       "bsIgmpExtFilterRangeEntry": bsIgmpExtFilterRangeEntry,
       "bsIgmpExtFilterRangeId": bsIgmpExtFilterRangeId,
       "bsIgmpExtFilterRangeAddressType": bsIgmpExtFilterRangeAddressType,
       "bsIgmpExtFilterRangeAddressStart": bsIgmpExtFilterRangeAddressStart,
       "bsIgmpExtFilterRangeAddressEnd": bsIgmpExtFilterRangeAddressEnd,
       "bsIgmpExtFilterRangeRowStatus": bsIgmpExtFilterRangeRowStatus,
       "bsIgmpExtFilterProfileScalars": bsIgmpExtFilterProfileScalars,
       "bsIgmpExtFilterProfileClearStats": bsIgmpExtFilterProfileClearStats,
       "bsIgmpExtScalars": bsIgmpExtScalars,
       "bsIgmpExtAvailableHardwareResources": bsIgmpExtAvailableHardwareResources,
       "bsIgmpExtHardwareCompatibilityMode": bsIgmpExtHardwareCompatibilityMode,
       "bsIgmpExtStreamFlushAll": bsIgmpExtStreamFlushAll,
       "bsIgmpExtStreamCount": bsIgmpExtStreamCount,
       "bsIgmpExtGroupCount": bsIgmpExtGroupCount,
       "bsIgmpExtMvrGlobal": bsIgmpExtMvrGlobal,
       "bsIgmpExtMvrGlobalEnable": bsIgmpExtMvrGlobalEnable,
       "bsIgmpExtMvrGlobalSourceVlan": bsIgmpExtMvrGlobalSourceVlan,
       "bsIgmpExtMvrGroupRangeTable": bsIgmpExtMvrGroupRangeTable,
       "bsIgmpExtMvrGroupRangeEntry": bsIgmpExtMvrGroupRangeEntry,
       "bsIgmpExtMvrGroupRangeAddress": bsIgmpExtMvrGroupRangeAddress,
       "bsIgmpExtMvrGroupRangeMask": bsIgmpExtMvrGroupRangeMask,
       "bsIgmpExtMvrGroupRangeRowStatus": bsIgmpExtMvrGroupRangeRowStatus,
       "bsIgmpExtMvrReceiversTable": bsIgmpExtMvrReceiversTable,
       "bsIgmpExtMvrReceiversEntry": bsIgmpExtMvrReceiversEntry,
       "bsIgmpExtMvrReceiversVlanId": bsIgmpExtMvrReceiversVlanId,
       "bsIgmpExtMvrReceiversRowStatus": bsIgmpExtMvrReceiversRowStatus}
)
