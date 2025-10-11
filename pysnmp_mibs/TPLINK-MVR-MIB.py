# SNMP MIB module (TPLINK-MVR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/tplink/TPLINK-MVR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:55:30 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tplinkMgmt,) = mibBuilder.importSymbols(
    "TPLINK-MIB",
    "tplinkMgmt")

(TPRowStatus,) = mibBuilder.importSymbols(
    "TPLINK-TC-MIB",
    "TPRowStatus")


# MODULE-IDENTITY

tplinkMvrMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99)
)
if mibBuilder.loadTexts:
    tplinkMvrMIB.setRevisions(
        ("2012-12-14 14:32",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TplinkMvrMIBObjects_ObjectIdentity = ObjectIdentity
tplinkMvrMIBObjects = _TplinkMvrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1)
)
_TpMvrGlobalConfig_ObjectIdentity = ObjectIdentity
tpMvrGlobalConfig = _TpMvrGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 1)
)


class _TpMvrAdminMode_Type(Integer32):
    """Custom type tpMvrAdminMode based on Integer32"""
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


_TpMvrAdminMode_Type.__name__ = "Integer32"
_TpMvrAdminMode_Object = MibScalar
tpMvrAdminMode = _TpMvrAdminMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 1, 1),
    _TpMvrAdminMode_Type()
)
tpMvrAdminMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMvrAdminMode.setStatus("current")


class _TpMvrModeType_Type(Integer32):
    """Custom type tpMvrModeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("compatible", 1),
          ("dynamic", 2))
    )


_TpMvrModeType_Type.__name__ = "Integer32"
_TpMvrModeType_Object = MibScalar
tpMvrModeType = _TpMvrModeType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 1, 2),
    _TpMvrModeType_Type()
)
tpMvrModeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMvrModeType.setStatus("current")


class _TpMvrMulticastVlanId_Type(Integer32):
    """Custom type tpMvrMulticastVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_TpMvrMulticastVlanId_Type.__name__ = "Integer32"
_TpMvrMulticastVlanId_Object = MibScalar
tpMvrMulticastVlanId = _TpMvrMulticastVlanId_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 1, 3),
    _TpMvrMulticastVlanId_Type()
)
tpMvrMulticastVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMvrMulticastVlanId.setStatus("current")
_TpMvrMaxMulticastGroupsCount_Type = Integer32
_TpMvrMaxMulticastGroupsCount_Object = MibScalar
tpMvrMaxMulticastGroupsCount = _TpMvrMaxMulticastGroupsCount_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 1, 4),
    _TpMvrMaxMulticastGroupsCount_Type()
)
tpMvrMaxMulticastGroupsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMvrMaxMulticastGroupsCount.setStatus("current")
_TpMvrCurrentMulticastGroupsCount_Type = Integer32
_TpMvrCurrentMulticastGroupsCount_Object = MibScalar
tpMvrCurrentMulticastGroupsCount = _TpMvrCurrentMulticastGroupsCount_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 1, 5),
    _TpMvrCurrentMulticastGroupsCount_Type()
)
tpMvrCurrentMulticastGroupsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMvrCurrentMulticastGroupsCount.setStatus("current")


class _TpMvrQueryTime_Type(Integer32):
    """Custom type tpMvrQueryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_TpMvrQueryTime_Type.__name__ = "Integer32"
_TpMvrQueryTime_Object = MibScalar
tpMvrQueryTime = _TpMvrQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 1, 6),
    _TpMvrQueryTime_Type()
)
tpMvrQueryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMvrQueryTime.setStatus("current")
_TpMvrPortConfig_ObjectIdentity = ObjectIdentity
tpMvrPortConfig = _TpMvrPortConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 2)
)
_TpMvrPortTable_Object = MibTable
tpMvrPortTable = _TpMvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tpMvrPortTable.setStatus("current")
_TpMvrPortEntry_Object = MibTableRow
tpMvrPortEntry = _TpMvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 2, 1, 1)
)
tpMvrPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    tpMvrPortEntry.setStatus("current")


class _TpMvrPortEnable_Type(Integer32):
    """Custom type tpMvrPortEnable based on Integer32"""
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


_TpMvrPortEnable_Type.__name__ = "Integer32"
_TpMvrPortEnable_Object = MibTableColumn
tpMvrPortEnable = _TpMvrPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 2, 1, 1, 2),
    _TpMvrPortEnable_Type()
)
tpMvrPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMvrPortEnable.setStatus("current")


class _TpMvrPortType_Type(Integer32):
    """Custom type tpMvrPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("source", 1),
          ("receiver", 2))
    )


_TpMvrPortType_Type.__name__ = "Integer32"
_TpMvrPortType_Object = MibTableColumn
tpMvrPortType = _TpMvrPortType_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 2, 1, 1, 3),
    _TpMvrPortType_Type()
)
tpMvrPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMvrPortType.setStatus("current")


class _TpMvrPortImmediateLeaveMode_Type(Integer32):
    """Custom type tpMvrPortImmediateLeaveMode based on Integer32"""
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


_TpMvrPortImmediateLeaveMode_Type.__name__ = "Integer32"
_TpMvrPortImmediateLeaveMode_Object = MibTableColumn
tpMvrPortImmediateLeaveMode = _TpMvrPortImmediateLeaveMode_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 2, 1, 1, 4),
    _TpMvrPortImmediateLeaveMode_Type()
)
tpMvrPortImmediateLeaveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMvrPortImmediateLeaveMode.setStatus("current")


class _TpMvrPortStatus_Type(Integer32):
    """Custom type tpMvrPortStatus based on Integer32"""
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
        *(("activeInVlan", 1),
          ("activeNotInVlan", 2),
          ("inactiveInVlan", 3),
          ("inactiveNotInVlan", 4))
    )


_TpMvrPortStatus_Type.__name__ = "Integer32"
_TpMvrPortStatus_Object = MibTableColumn
tpMvrPortStatus = _TpMvrPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 2, 1, 1, 5),
    _TpMvrPortStatus_Type()
)
tpMvrPortStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMvrPortStatus.setStatus("current")
_TpMvrGroupConfig_ObjectIdentity = ObjectIdentity
tpMvrGroupConfig = _TpMvrGroupConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 3)
)
_TpMvrGroupTable_Object = MibTable
tpMvrGroupTable = _TpMvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 3, 1)
)
if mibBuilder.loadTexts:
    tpMvrGroupTable.setStatus("current")
_TpMvrGroupEntry_Object = MibTableRow
tpMvrGroupEntry = _TpMvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 3, 1, 1)
)
tpMvrGroupEntry.setIndexNames(
    (0, "TPLINK-MVR-MIB", "tpMvrGroupIPAddress"),
)
if mibBuilder.loadTexts:
    tpMvrGroupEntry.setStatus("current")
_TpMvrGroupIPAddress_Type = IpAddress
_TpMvrGroupIPAddress_Object = MibTableColumn
tpMvrGroupIPAddress = _TpMvrGroupIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 3, 1, 1, 1),
    _TpMvrGroupIPAddress_Type()
)
tpMvrGroupIPAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMvrGroupIPAddress.setStatus("current")


class _TpMvrGroupStatus_Type(Integer32):
    """Custom type tpMvrGroupStatus based on Integer32"""
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


_TpMvrGroupStatus_Type.__name__ = "Integer32"
_TpMvrGroupStatus_Object = MibTableColumn
tpMvrGroupStatus = _TpMvrGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 3, 1, 1, 2),
    _TpMvrGroupStatus_Type()
)
tpMvrGroupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMvrGroupStatus.setStatus("current")


class _TpMvrGroupForwardPorts_Type(OctetString):
    """Custom type tpMvrGroupForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMvrGroupForwardPorts_Type.__name__ = "OctetString"
_TpMvrGroupForwardPorts_Object = MibTableColumn
tpMvrGroupForwardPorts = _TpMvrGroupForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 3, 1, 1, 3),
    _TpMvrGroupForwardPorts_Type()
)
tpMvrGroupForwardPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tpMvrGroupForwardPorts.setStatus("current")


class _TpMvrGroupAddForwardPorts_Type(OctetString):
    """Custom type tpMvrGroupAddForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMvrGroupAddForwardPorts_Type.__name__ = "OctetString"
_TpMvrGroupAddForwardPorts_Object = MibTableColumn
tpMvrGroupAddForwardPorts = _TpMvrGroupAddForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 3, 1, 1, 4),
    _TpMvrGroupAddForwardPorts_Type()
)
tpMvrGroupAddForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMvrGroupAddForwardPorts.setStatus("current")


class _TpMvrGroupDelForwardPorts_Type(OctetString):
    """Custom type tpMvrGroupDelForwardPorts based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_TpMvrGroupDelForwardPorts_Type.__name__ = "OctetString"
_TpMvrGroupDelForwardPorts_Object = MibTableColumn
tpMvrGroupDelForwardPorts = _TpMvrGroupDelForwardPorts_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 3, 1, 1, 5),
    _TpMvrGroupDelForwardPorts_Type()
)
tpMvrGroupDelForwardPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tpMvrGroupDelForwardPorts.setStatus("current")
_TpMvrGroupRowStatus_Type = TPRowStatus
_TpMvrGroupRowStatus_Object = MibTableColumn
tpMvrGroupRowStatus = _TpMvrGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 1, 3, 1, 1, 6),
    _TpMvrGroupRowStatus_Type()
)
tpMvrGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tpMvrGroupRowStatus.setStatus("current")
_TplinkMvrNotifications_ObjectIdentity = ObjectIdentity
tplinkMvrNotifications = _TplinkMvrNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11863, 6, 99, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPLINK-MVR-MIB",
    **{"tplinkMvrMIB": tplinkMvrMIB,
       "tplinkMvrMIBObjects": tplinkMvrMIBObjects,
       "tpMvrGlobalConfig": tpMvrGlobalConfig,
       "tpMvrAdminMode": tpMvrAdminMode,
       "tpMvrModeType": tpMvrModeType,
       "tpMvrMulticastVlanId": tpMvrMulticastVlanId,
       "tpMvrMaxMulticastGroupsCount": tpMvrMaxMulticastGroupsCount,
       "tpMvrCurrentMulticastGroupsCount": tpMvrCurrentMulticastGroupsCount,
       "tpMvrQueryTime": tpMvrQueryTime,
       "tpMvrPortConfig": tpMvrPortConfig,
       "tpMvrPortTable": tpMvrPortTable,
       "tpMvrPortEntry": tpMvrPortEntry,
       "tpMvrPortEnable": tpMvrPortEnable,
       "tpMvrPortType": tpMvrPortType,
       "tpMvrPortImmediateLeaveMode": tpMvrPortImmediateLeaveMode,
       "tpMvrPortStatus": tpMvrPortStatus,
       "tpMvrGroupConfig": tpMvrGroupConfig,
       "tpMvrGroupTable": tpMvrGroupTable,
       "tpMvrGroupEntry": tpMvrGroupEntry,
       "tpMvrGroupIPAddress": tpMvrGroupIPAddress,
       "tpMvrGroupStatus": tpMvrGroupStatus,
       "tpMvrGroupForwardPorts": tpMvrGroupForwardPorts,
       "tpMvrGroupAddForwardPorts": tpMvrGroupAddForwardPorts,
       "tpMvrGroupDelForwardPorts": tpMvrGroupDelForwardPorts,
       "tpMvrGroupRowStatus": tpMvrGroupRowStatus,
       "tplinkMvrNotifications": tplinkMvrNotifications}
)
