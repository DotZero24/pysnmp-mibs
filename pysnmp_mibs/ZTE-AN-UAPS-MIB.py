# SNMP MIB module (ZTE-AN-UAPS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-UAPS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:32 2025
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

(ZxAnPortList,
 zxAn) = mibBuilder.importSymbols(
    "ZTE-AN-TC-MIB",
    "ZxAnPortList",
    "zxAn")


# MODULE-IDENTITY

zxAnUapsMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnUapsObjects_ObjectIdentity = ObjectIdentity
zxAnUapsObjects = _ZxAnUapsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1)
)


class _ZxAnUapsCapability_Type(Bits):
    """Custom type zxAnUapsCapability based on Bits"""
    namedValues = NamedValues(
        *(("ipLinkChk", 0),
          ("protectionTime", 1),
          ("supportSlaveSlotPorts", 2))
    )

_ZxAnUapsCapability_Type.__name__ = "Bits"
_ZxAnUapsCapability_Object = MibScalar
zxAnUapsCapability = _ZxAnUapsCapability_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 1),
    _ZxAnUapsCapability_Type()
)
zxAnUapsCapability.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnUapsCapability.setStatus("current")
_ZxAnUapsGroupTable_Object = MibTable
zxAnUapsGroupTable = _ZxAnUapsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnUapsGroupTable.setStatus("current")
_ZxAnUapsGroupEntry_Object = MibTableRow
zxAnUapsGroupEntry = _ZxAnUapsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1)
)
zxAnUapsGroupEntry.setIndexNames(
    (0, "ZTE-AN-UAPS-MIB", "zxAnUapsGroupIndex"),
)
if mibBuilder.loadTexts:
    zxAnUapsGroupEntry.setStatus("current")


class _ZxAnUapsGroupIndex_Type(Integer32):
    """Custom type zxAnUapsGroupIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_ZxAnUapsGroupIndex_Type.__name__ = "Integer32"
_ZxAnUapsGroupIndex_Object = MibTableColumn
zxAnUapsGroupIndex = _ZxAnUapsGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 1),
    _ZxAnUapsGroupIndex_Type()
)
zxAnUapsGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnUapsGroupIndex.setStatus("current")


class _ZxAnUapsGroupName_Type(DisplayString):
    """Custom type zxAnUapsGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnUapsGroupName_Type.__name__ = "DisplayString"
_ZxAnUapsGroupName_Object = MibTableColumn
zxAnUapsGroupName = _ZxAnUapsGroupName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 2),
    _ZxAnUapsGroupName_Type()
)
zxAnUapsGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsGroupName.setStatus("current")
_ZxAnUapsPrimaryPortList_Type = ObjectIdentifier
_ZxAnUapsPrimaryPortList_Object = MibTableColumn
zxAnUapsPrimaryPortList = _ZxAnUapsPrimaryPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 3),
    _ZxAnUapsPrimaryPortList_Type()
)
zxAnUapsPrimaryPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsPrimaryPortList.setStatus("current")
_ZxAnUapsSecondaryPortList_Type = ObjectIdentifier
_ZxAnUapsSecondaryPortList_Object = MibTableColumn
zxAnUapsSecondaryPortList = _ZxAnUapsSecondaryPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 4),
    _ZxAnUapsSecondaryPortList_Type()
)
zxAnUapsSecondaryPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsSecondaryPortList.setStatus("current")
_ZxAnUapsAutoFailbackEnable_Type = Integer32
_ZxAnUapsAutoFailbackEnable_Object = MibTableColumn
zxAnUapsAutoFailbackEnable = _ZxAnUapsAutoFailbackEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 5),
    _ZxAnUapsAutoFailbackEnable_Type()
)
zxAnUapsAutoFailbackEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsAutoFailbackEnable.setStatus("current")
_ZxAnUapsNextHopIp_Type = IpAddress
_ZxAnUapsNextHopIp_Object = MibTableColumn
zxAnUapsNextHopIp = _ZxAnUapsNextHopIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 6),
    _ZxAnUapsNextHopIp_Type()
)
zxAnUapsNextHopIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsNextHopIp.setStatus("current")


class _ZxAnUapsIpLinkType_Type(Integer32):
    """Custom type zxAnUapsIpLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("defaulIpLink", 1),
          ("serviceIpLink", 2))
    )


_ZxAnUapsIpLinkType_Type.__name__ = "Integer32"
_ZxAnUapsIpLinkType_Object = MibTableColumn
zxAnUapsIpLinkType = _ZxAnUapsIpLinkType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 7),
    _ZxAnUapsIpLinkType_Type()
)
zxAnUapsIpLinkType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsIpLinkType.setStatus("current")


class _ZxAnUapsIpLinkChkRetries_Type(Integer32):
    """Custom type zxAnUapsIpLinkChkRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZxAnUapsIpLinkChkRetries_Type.__name__ = "Integer32"
_ZxAnUapsIpLinkChkRetries_Object = MibTableColumn
zxAnUapsIpLinkChkRetries = _ZxAnUapsIpLinkChkRetries_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 8),
    _ZxAnUapsIpLinkChkRetries_Type()
)
zxAnUapsIpLinkChkRetries.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsIpLinkChkRetries.setStatus("current")


class _ZxAnUapsIpLinkChkTimeout_Type(Integer32):
    """Custom type zxAnUapsIpLinkChkTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_ZxAnUapsIpLinkChkTimeout_Type.__name__ = "Integer32"
_ZxAnUapsIpLinkChkTimeout_Object = MibTableColumn
zxAnUapsIpLinkChkTimeout = _ZxAnUapsIpLinkChkTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 9),
    _ZxAnUapsIpLinkChkTimeout_Type()
)
zxAnUapsIpLinkChkTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsIpLinkChkTimeout.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUapsIpLinkChkTimeout.setUnits("sec")


class _ZxAnUapsIpLinkStatus_Type(Integer32):
    """Custom type zxAnUapsIpLinkStatus based on Integer32"""
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4))
    )


_ZxAnUapsIpLinkStatus_Type.__name__ = "Integer32"
_ZxAnUapsIpLinkStatus_Object = MibTableColumn
zxAnUapsIpLinkStatus = _ZxAnUapsIpLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 10),
    _ZxAnUapsIpLinkStatus_Type()
)
zxAnUapsIpLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUapsIpLinkStatus.setStatus("current")
_ZxAnUapsForceSwap_Type = Integer32
_ZxAnUapsForceSwap_Object = MibTableColumn
zxAnUapsForceSwap = _ZxAnUapsForceSwap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 11),
    _ZxAnUapsForceSwap_Type()
)
zxAnUapsForceSwap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsForceSwap.setStatus("current")


class _ZxAnUapsPortWorkingStatus_Type(Integer32):
    """Custom type zxAnUapsPortWorkingStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primaryPortInWorking", 1),
          ("secondaryPortInWorking", 2))
    )


_ZxAnUapsPortWorkingStatus_Type.__name__ = "Integer32"
_ZxAnUapsPortWorkingStatus_Object = MibTableColumn
zxAnUapsPortWorkingStatus = _ZxAnUapsPortWorkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 12),
    _ZxAnUapsPortWorkingStatus_Type()
)
zxAnUapsPortWorkingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUapsPortWorkingStatus.setStatus("current")


class _ZxAnUapsSwapReason_Type(Integer32):
    """Custom type zxAnUapsSwapReason based on Integer32"""
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
        *(("failback", 0),
          ("failoverByPhyLinkDown", 1),
          ("failoverByIpLinkDown", 2),
          ("forceSwap", 3))
    )


_ZxAnUapsSwapReason_Type.__name__ = "Integer32"
_ZxAnUapsSwapReason_Object = MibTableColumn
zxAnUapsSwapReason = _ZxAnUapsSwapReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 13),
    _ZxAnUapsSwapReason_Type()
)
zxAnUapsSwapReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUapsSwapReason.setStatus("current")


class _ZxAnUapsSupportSlaveSlotPorts_Type(Integer32):
    """Custom type zxAnUapsSupportSlaveSlotPorts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port", 1),
          ("csc", 2))
    )


_ZxAnUapsSupportSlaveSlotPorts_Type.__name__ = "Integer32"
_ZxAnUapsSupportSlaveSlotPorts_Object = MibTableColumn
zxAnUapsSupportSlaveSlotPorts = _ZxAnUapsSupportSlaveSlotPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 14),
    _ZxAnUapsSupportSlaveSlotPorts_Type()
)
zxAnUapsSupportSlaveSlotPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsSupportSlaveSlotPorts.setStatus("current")


class _ZxAnUapsProtectionTime_Type(Integer32):
    """Custom type zxAnUapsProtectionTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 900),
    )


_ZxAnUapsProtectionTime_Type.__name__ = "Integer32"
_ZxAnUapsProtectionTime_Object = MibTableColumn
zxAnUapsProtectionTime = _ZxAnUapsProtectionTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 15),
    _ZxAnUapsProtectionTime_Type()
)
zxAnUapsProtectionTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsProtectionTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnUapsProtectionTime.setUnits("second")
_ZxAnUapsIsInPrtctTime_Type = TruthValue
_ZxAnUapsIsInPrtctTime_Object = MibTableColumn
zxAnUapsIsInPrtctTime = _ZxAnUapsIsInPrtctTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 16),
    _ZxAnUapsIsInPrtctTime_Type()
)
zxAnUapsIsInPrtctTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUapsIsInPrtctTime.setStatus("current")


class _ZxAnUapsSwapRequestInCache_Type(Bits):
    """Custom type zxAnUapsSwapRequestInCache based on Bits"""
    namedValues = NamedValues(
        *(("failback", 0),
          ("failoverByPhyLinkDown", 1),
          ("failoverByIpLinkDown", 2),
          ("forceSwap", 3))
    )

_ZxAnUapsSwapRequestInCache_Type.__name__ = "Bits"
_ZxAnUapsSwapRequestInCache_Object = MibTableColumn
zxAnUapsSwapRequestInCache = _ZxAnUapsSwapRequestInCache_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 17),
    _ZxAnUapsSwapRequestInCache_Type()
)
zxAnUapsSwapRequestInCache.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUapsSwapRequestInCache.setStatus("current")


class _ZxAnUapsSwapLastRequest_Type(Integer32):
    """Custom type zxAnUapsSwapLastRequest based on Integer32"""
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
        *(("failback", 0),
          ("failoverByPhyLinkDown", 1),
          ("failoverByIpLinkDown", 2),
          ("forceSwap", 3))
    )


_ZxAnUapsSwapLastRequest_Type.__name__ = "Integer32"
_ZxAnUapsSwapLastRequest_Object = MibTableColumn
zxAnUapsSwapLastRequest = _ZxAnUapsSwapLastRequest_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 18),
    _ZxAnUapsSwapLastRequest_Type()
)
zxAnUapsSwapLastRequest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnUapsSwapLastRequest.setStatus("current")


class _ZxAnUapsSwapMode_Type(Integer32):
    """Custom type zxAnUapsSwapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("common", 1),
          ("trunk", 2),
          ("upPortNum", 3))
    )


_ZxAnUapsSwapMode_Type.__name__ = "Integer32"
_ZxAnUapsSwapMode_Object = MibTableColumn
zxAnUapsSwapMode = _ZxAnUapsSwapMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 19),
    _ZxAnUapsSwapMode_Type()
)
zxAnUapsSwapMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsSwapMode.setStatus("current")


class _ZxAnUapsSecondaryPortLighting_Type(Integer32):
    """Custom type zxAnUapsSecondaryPortLighting based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnUapsSecondaryPortLighting_Type.__name__ = "Integer32"
_ZxAnUapsSecondaryPortLighting_Object = MibTableColumn
zxAnUapsSecondaryPortLighting = _ZxAnUapsSecondaryPortLighting_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 20),
    _ZxAnUapsSecondaryPortLighting_Type()
)
zxAnUapsSecondaryPortLighting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsSecondaryPortLighting.setStatus("current")
_ZxAnUapsGroupRowStatus_Type = RowStatus
_ZxAnUapsGroupRowStatus_Object = MibTableColumn
zxAnUapsGroupRowStatus = _ZxAnUapsGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 1, 2, 1, 25),
    _ZxAnUapsGroupRowStatus_Type()
)
zxAnUapsGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnUapsGroupRowStatus.setStatus("current")
_ZxAnUapsTraps_ObjectIdentity = ObjectIdentity
zxAnUapsTraps = _ZxAnUapsTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 2)
)

# Managed Objects groups


# Notification objects

zxAnUapsSwappedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 2, 1)
)
zxAnUapsSwappedTrap.setObjects(
      *(("ZTE-AN-UAPS-MIB", "zxAnUapsPortWorkingStatus"),
        ("ZTE-AN-UAPS-MIB", "zxAnUapsSwapReason"),
        ("ZTE-AN-UAPS-MIB", "zxAnUapsGroupName"),
        ("ZTE-AN-UAPS-MIB", "zxAnUapsPrimaryPortList"),
        ("ZTE-AN-UAPS-MIB", "zxAnUapsSecondaryPortList"))
)
if mibBuilder.loadTexts:
    zxAnUapsSwappedTrap.setStatus(
        "current"
    )

zxAnUapsSwappedAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 2, 2)
)
zxAnUapsSwappedAlm.setObjects(
      *(("ZTE-AN-UAPS-MIB", "zxAnUapsPortWorkingStatus"),
        ("ZTE-AN-UAPS-MIB", "zxAnUapsSwapReason"),
        ("ZTE-AN-UAPS-MIB", "zxAnUapsGroupName"),
        ("ZTE-AN-UAPS-MIB", "zxAnUapsPrimaryPortList"),
        ("ZTE-AN-UAPS-MIB", "zxAnUapsSecondaryPortList"))
)
if mibBuilder.loadTexts:
    zxAnUapsSwappedAlm.setStatus(
        "current"
    )

zxAnUapsSwappedClr = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 7, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnUapsSwappedClr.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-UAPS-MIB",
    **{"zxAnUapsMib": zxAnUapsMib,
       "zxAnUapsObjects": zxAnUapsObjects,
       "zxAnUapsCapability": zxAnUapsCapability,
       "zxAnUapsGroupTable": zxAnUapsGroupTable,
       "zxAnUapsGroupEntry": zxAnUapsGroupEntry,
       "zxAnUapsGroupIndex": zxAnUapsGroupIndex,
       "zxAnUapsGroupName": zxAnUapsGroupName,
       "zxAnUapsPrimaryPortList": zxAnUapsPrimaryPortList,
       "zxAnUapsSecondaryPortList": zxAnUapsSecondaryPortList,
       "zxAnUapsAutoFailbackEnable": zxAnUapsAutoFailbackEnable,
       "zxAnUapsNextHopIp": zxAnUapsNextHopIp,
       "zxAnUapsIpLinkType": zxAnUapsIpLinkType,
       "zxAnUapsIpLinkChkRetries": zxAnUapsIpLinkChkRetries,
       "zxAnUapsIpLinkChkTimeout": zxAnUapsIpLinkChkTimeout,
       "zxAnUapsIpLinkStatus": zxAnUapsIpLinkStatus,
       "zxAnUapsForceSwap": zxAnUapsForceSwap,
       "zxAnUapsPortWorkingStatus": zxAnUapsPortWorkingStatus,
       "zxAnUapsSwapReason": zxAnUapsSwapReason,
       "zxAnUapsSupportSlaveSlotPorts": zxAnUapsSupportSlaveSlotPorts,
       "zxAnUapsProtectionTime": zxAnUapsProtectionTime,
       "zxAnUapsIsInPrtctTime": zxAnUapsIsInPrtctTime,
       "zxAnUapsSwapRequestInCache": zxAnUapsSwapRequestInCache,
       "zxAnUapsSwapLastRequest": zxAnUapsSwapLastRequest,
       "zxAnUapsSwapMode": zxAnUapsSwapMode,
       "zxAnUapsSecondaryPortLighting": zxAnUapsSecondaryPortLighting,
       "zxAnUapsGroupRowStatus": zxAnUapsGroupRowStatus,
       "zxAnUapsTraps": zxAnUapsTraps,
       "zxAnUapsSwappedTrap": zxAnUapsSwappedTrap,
       "zxAnUapsSwappedAlm": zxAnUapsSwappedAlm,
       "zxAnUapsSwappedClr": zxAnUapsSwappedClr}
)
