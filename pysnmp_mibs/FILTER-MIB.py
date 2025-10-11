# SNMP MIB module (FILTER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/FILTER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:47:53 2025
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

(dlink_common_mgmt,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlink-common-mgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

swFilterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37)
)


# Types definitions



class PortList(OctetString):
    """Custom type PortList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )




# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SwFilterDhcp_ObjectIdentity = ObjectIdentity
swFilterDhcp = _SwFilterDhcp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1)
)
_SwFilterDhcpPermitTable_Object = MibTable
swFilterDhcpPermitTable = _SwFilterDhcpPermitTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1)
)
if mibBuilder.loadTexts:
    swFilterDhcpPermitTable.setStatus("current")
_SwFilterDhcpPermitEntry_Object = MibTableRow
swFilterDhcpPermitEntry = _SwFilterDhcpPermitEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1, 1)
)
swFilterDhcpPermitEntry.setIndexNames(
    (0, "FILTER-MIB", "swFilterDhcpServerIP"),
    (0, "FILTER-MIB", "swFilterDhcpClientMac"),
)
if mibBuilder.loadTexts:
    swFilterDhcpPermitEntry.setStatus("current")
_SwFilterDhcpServerIP_Type = IpAddress
_SwFilterDhcpServerIP_Object = MibTableColumn
swFilterDhcpServerIP = _SwFilterDhcpServerIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1, 1, 1),
    _SwFilterDhcpServerIP_Type()
)
swFilterDhcpServerIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFilterDhcpServerIP.setStatus("current")
_SwFilterDhcpClientMac_Type = MacAddress
_SwFilterDhcpClientMac_Object = MibTableColumn
swFilterDhcpClientMac = _SwFilterDhcpClientMac_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1, 1, 2),
    _SwFilterDhcpClientMac_Type()
)
swFilterDhcpClientMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFilterDhcpClientMac.setStatus("current")
_SwFilterDhcpPorts_Type = PortList
_SwFilterDhcpPorts_Object = MibTableColumn
swFilterDhcpPorts = _SwFilterDhcpPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1, 1, 3),
    _SwFilterDhcpPorts_Type()
)
swFilterDhcpPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swFilterDhcpPorts.setStatus("current")
_SwFilterDhcpStatus_Type = RowStatus
_SwFilterDhcpStatus_Object = MibTableColumn
swFilterDhcpStatus = _SwFilterDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 1, 1, 4),
    _SwFilterDhcpStatus_Type()
)
swFilterDhcpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    swFilterDhcpStatus.setStatus("current")
_SwFilterDhcpPortTable_Object = MibTable
swFilterDhcpPortTable = _SwFilterDhcpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 2)
)
if mibBuilder.loadTexts:
    swFilterDhcpPortTable.setStatus("current")
_SwFilterDhcpPortEntry_Object = MibTableRow
swFilterDhcpPortEntry = _SwFilterDhcpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 2, 1)
)
swFilterDhcpPortEntry.setIndexNames(
    (0, "FILTER-MIB", "swFilterDhcpPortIndex"),
)
if mibBuilder.loadTexts:
    swFilterDhcpPortEntry.setStatus("current")


class _SwFilterDhcpPortIndex_Type(Integer32):
    """Custom type swFilterDhcpPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_SwFilterDhcpPortIndex_Type.__name__ = "Integer32"
_SwFilterDhcpPortIndex_Object = MibTableColumn
swFilterDhcpPortIndex = _SwFilterDhcpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 2, 1, 1),
    _SwFilterDhcpPortIndex_Type()
)
swFilterDhcpPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swFilterDhcpPortIndex.setStatus("current")


class _SwFilterDhcpPortState_Type(Integer32):
    """Custom type swFilterDhcpPortState based on Integer32"""
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


_SwFilterDhcpPortState_Type.__name__ = "Integer32"
_SwFilterDhcpPortState_Object = MibTableColumn
swFilterDhcpPortState = _SwFilterDhcpPortState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 2, 1, 2),
    _SwFilterDhcpPortState_Type()
)
swFilterDhcpPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterDhcpPortState.setStatus("current")


class _SwFilterDhcpServerIllegalSerLogSuppressDuration_Type(Integer32):
    """Custom type swFilterDhcpServerIllegalSerLogSuppressDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("duration-1min", 1),
          ("duration-5min", 2),
          ("duration-30min", 3))
    )


_SwFilterDhcpServerIllegalSerLogSuppressDuration_Type.__name__ = "Integer32"
_SwFilterDhcpServerIllegalSerLogSuppressDuration_Object = MibScalar
swFilterDhcpServerIllegalSerLogSuppressDuration = _SwFilterDhcpServerIllegalSerLogSuppressDuration_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 3),
    _SwFilterDhcpServerIllegalSerLogSuppressDuration_Type()
)
swFilterDhcpServerIllegalSerLogSuppressDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterDhcpServerIllegalSerLogSuppressDuration.setStatus("current")


class _SwFilterDhcpServerTrapLogState_Type(Integer32):
    """Custom type swFilterDhcpServerTrapLogState based on Integer32"""
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


_SwFilterDhcpServerTrapLogState_Type.__name__ = "Integer32"
_SwFilterDhcpServerTrapLogState_Object = MibScalar
swFilterDhcpServerTrapLogState = _SwFilterDhcpServerTrapLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 4),
    _SwFilterDhcpServerTrapLogState_Type()
)
swFilterDhcpServerTrapLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterDhcpServerTrapLogState.setStatus("current")


class _SwFilterDhcpServerTrapState_Type(Integer32):
    """Custom type swFilterDhcpServerTrapState based on Integer32"""
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


_SwFilterDhcpServerTrapState_Type.__name__ = "Integer32"
_SwFilterDhcpServerTrapState_Object = MibScalar
swFilterDhcpServerTrapState = _SwFilterDhcpServerTrapState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 5),
    _SwFilterDhcpServerTrapState_Type()
)
swFilterDhcpServerTrapState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterDhcpServerTrapState.setStatus("current")


class _SwFilterDhcpServerLogState_Type(Integer32):
    """Custom type swFilterDhcpServerLogState based on Integer32"""
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


_SwFilterDhcpServerLogState_Type.__name__ = "Integer32"
_SwFilterDhcpServerLogState_Object = MibScalar
swFilterDhcpServerLogState = _SwFilterDhcpServerLogState_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 1, 6),
    _SwFilterDhcpServerLogState_Type()
)
swFilterDhcpServerLogState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    swFilterDhcpServerLogState.setStatus("current")
_SwFilterNotify_ObjectIdentity = ObjectIdentity
swFilterNotify = _SwFilterNotify_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100)
)
_SwFilterNotifyPrefix_ObjectIdentity = ObjectIdentity
swFilterNotifyPrefix = _SwFilterNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100, 0)
)
_SwFilterNotificationBindings_ObjectIdentity = ObjectIdentity
swFilterNotificationBindings = _SwFilterNotificationBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100, 2)
)
_SwFilterDetectedIP_Type = IpAddress
_SwFilterDetectedIP_Object = MibScalar
swFilterDetectedIP = _SwFilterDetectedIP_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100, 2, 1),
    _SwFilterDetectedIP_Type()
)
swFilterDetectedIP.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swFilterDetectedIP.setStatus("current")
_SwFilterDetectedport_Type = Integer32
_SwFilterDetectedport_Object = MibScalar
swFilterDetectedport = _SwFilterDetectedport_Object(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100, 2, 2),
    _SwFilterDetectedport_Type()
)
swFilterDetectedport.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swFilterDetectedport.setStatus("current")

# Managed Objects groups


# Notification objects

swFilterDetectedTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 171, 12, 37, 100, 0, 1)
)
swFilterDetectedTrap.setObjects(
      *(("FILTER-MIB", "swFilterDetectedIP"),
        ("FILTER-MIB", "swFilterDetectedport"))
)
if mibBuilder.loadTexts:
    swFilterDetectedTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FILTER-MIB",
    **{"PortList": PortList,
       "swFilterMIB": swFilterMIB,
       "swFilterDhcp": swFilterDhcp,
       "swFilterDhcpPermitTable": swFilterDhcpPermitTable,
       "swFilterDhcpPermitEntry": swFilterDhcpPermitEntry,
       "swFilterDhcpServerIP": swFilterDhcpServerIP,
       "swFilterDhcpClientMac": swFilterDhcpClientMac,
       "swFilterDhcpPorts": swFilterDhcpPorts,
       "swFilterDhcpStatus": swFilterDhcpStatus,
       "swFilterDhcpPortTable": swFilterDhcpPortTable,
       "swFilterDhcpPortEntry": swFilterDhcpPortEntry,
       "swFilterDhcpPortIndex": swFilterDhcpPortIndex,
       "swFilterDhcpPortState": swFilterDhcpPortState,
       "swFilterDhcpServerIllegalSerLogSuppressDuration": swFilterDhcpServerIllegalSerLogSuppressDuration,
       "swFilterDhcpServerTrapLogState": swFilterDhcpServerTrapLogState,
       "swFilterDhcpServerTrapState": swFilterDhcpServerTrapState,
       "swFilterDhcpServerLogState": swFilterDhcpServerLogState,
       "swFilterNotify": swFilterNotify,
       "swFilterNotifyPrefix": swFilterNotifyPrefix,
       "swFilterDetectedTrap": swFilterDetectedTrap,
       "swFilterNotificationBindings": swFilterNotificationBindings,
       "swFilterDetectedIP": swFilterDetectedIP,
       "swFilterDetectedport": swFilterDetectedport}
)
