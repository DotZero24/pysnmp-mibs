# SNMP MIB module (G6-IGMP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-IGMP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:16 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

protocol = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2)
)
if mibBuilder.loadTexts:
    protocol.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Igmp_ObjectIdentity = ObjectIdentity
igmp = _Igmp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40)
)


class _IgmpEnableIgmpSnooping_Type(Integer32):
    """Custom type igmpEnableIgmpSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IgmpEnableIgmpSnooping_Type.__name__ = "Integer32"
_IgmpEnableIgmpSnooping_Object = MibScalar
igmpEnableIgmpSnooping = _IgmpEnableIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 1),
    _IgmpEnableIgmpSnooping_Type()
)
igmpEnableIgmpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpEnableIgmpSnooping.setStatus("current")


class _IgmpEnableMldSnooping_Type(Integer32):
    """Custom type igmpEnableMldSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_IgmpEnableMldSnooping_Type.__name__ = "Integer32"
_IgmpEnableMldSnooping_Object = MibScalar
igmpEnableMldSnooping = _IgmpEnableMldSnooping_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 2),
    _IgmpEnableMldSnooping_Type()
)
igmpEnableMldSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpEnableMldSnooping.setStatus("current")
_IgmpShowMulticastForVlan_Type = DisplayString
_IgmpShowMulticastForVlan_Object = MibScalar
igmpShowMulticastForVlan = _IgmpShowMulticastForVlan_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 3),
    _IgmpShowMulticastForVlan_Type()
)
igmpShowMulticastForVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpShowMulticastForVlan.setStatus("current")
_IgmpShowMulticastForPort_Type = DisplayString
_IgmpShowMulticastForPort_Object = MibScalar
igmpShowMulticastForPort = _IgmpShowMulticastForPort_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 4),
    _IgmpShowMulticastForPort_Type()
)
igmpShowMulticastForPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpShowMulticastForPort.setStatus("current")
_ConfigTable_Object = MibTable
configTable = _ConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5)
)
if mibBuilder.loadTexts:
    configTable.setStatus("current")
_ConfigEntry_Object = MibTableRow
configEntry = _ConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1)
)
configEntry.setIndexNames(
    (0, "G6-IGMP-MIB", "configIndex"),
)
if mibBuilder.loadTexts:
    configEntry.setStatus("current")


class _ConfigIndex_Type(Integer32):
    """Custom type configIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ConfigIndex_Type.__name__ = "Integer32"
_ConfigIndex_Object = MibTableColumn
configIndex = _ConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 1),
    _ConfigIndex_Type()
)
configIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configIndex.setStatus("current")
_ConfigVlanId_Type = DisplayString
_ConfigVlanId_Object = MibTableColumn
configVlanId = _ConfigVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 2),
    _ConfigVlanId_Type()
)
configVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configVlanId.setStatus("current")


class _ConfigEnableIgmpSnooping_Type(Integer32):
    """Custom type configEnableIgmpSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnableIgmpSnooping_Type.__name__ = "Integer32"
_ConfigEnableIgmpSnooping_Object = MibTableColumn
configEnableIgmpSnooping = _ConfigEnableIgmpSnooping_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 3),
    _ConfigEnableIgmpSnooping_Type()
)
configEnableIgmpSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnableIgmpSnooping.setStatus("current")


class _ConfigEnableMldSnooping_Type(Integer32):
    """Custom type configEnableMldSnooping based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnableMldSnooping_Type.__name__ = "Integer32"
_ConfigEnableMldSnooping_Object = MibTableColumn
configEnableMldSnooping = _ConfigEnableMldSnooping_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 4),
    _ConfigEnableMldSnooping_Type()
)
configEnableMldSnooping.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnableMldSnooping.setStatus("current")
_ConfigSnoopingPorts_Type = Integer32
_ConfigSnoopingPorts_Object = MibTableColumn
configSnoopingPorts = _ConfigSnoopingPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 5),
    _ConfigSnoopingPorts_Type()
)
configSnoopingPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configSnoopingPorts.setStatus("current")
_ConfigStaticRouterPorts_Type = Integer32
_ConfigStaticRouterPorts_Object = MibTableColumn
configStaticRouterPorts = _ConfigStaticRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 6),
    _ConfigStaticRouterPorts_Type()
)
configStaticRouterPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configStaticRouterPorts.setStatus("current")


class _ConfigMulticastRouterDetection_Type(Integer32):
    """Custom type configMulticastRouterDetection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("routerDiscovery", 0),
          ("queryMessage", 1))
    )


_ConfigMulticastRouterDetection_Type.__name__ = "Integer32"
_ConfigMulticastRouterDetection_Object = MibTableColumn
configMulticastRouterDetection = _ConfigMulticastRouterDetection_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 7),
    _ConfigMulticastRouterDetection_Type()
)
configMulticastRouterDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMulticastRouterDetection.setStatus("current")


class _ConfigEnableReportAggregation_Type(Integer32):
    """Custom type configEnableReportAggregation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnableReportAggregation_Type.__name__ = "Integer32"
_ConfigEnableReportAggregation_Object = MibTableColumn
configEnableReportAggregation = _ConfigEnableReportAggregation_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 8),
    _ConfigEnableReportAggregation_Type()
)
configEnableReportAggregation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnableReportAggregation.setStatus("current")


class _ConfigEnableFloodingUnregisterPkt_Type(Integer32):
    """Custom type configEnableFloodingUnregisterPkt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnableFloodingUnregisterPkt_Type.__name__ = "Integer32"
_ConfigEnableFloodingUnregisterPkt_Object = MibTableColumn
configEnableFloodingUnregisterPkt = _ConfigEnableFloodingUnregisterPkt_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 9),
    _ConfigEnableFloodingUnregisterPkt_Type()
)
configEnableFloodingUnregisterPkt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnableFloodingUnregisterPkt.setStatus("current")


class _ConfigMcastGroupLimit_Type(Integer32):
    """Custom type configMcastGroupLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConfigMcastGroupLimit_Type.__name__ = "Integer32"
_ConfigMcastGroupLimit_Object = MibTableColumn
configMcastGroupLimit = _ConfigMcastGroupLimit_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 10),
    _ConfigMcastGroupLimit_Type()
)
configMcastGroupLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMcastGroupLimit.setStatus("current")


class _ConfigGroupMembershipInterval_Type(Integer32):
    """Custom type configGroupMembershipInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConfigGroupMembershipInterval_Type.__name__ = "Integer32"
_ConfigGroupMembershipInterval_Object = MibTableColumn
configGroupMembershipInterval = _ConfigGroupMembershipInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 11),
    _ConfigGroupMembershipInterval_Type()
)
configGroupMembershipInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configGroupMembershipInterval.setStatus("current")


class _ConfigMaxResponseTime_Type(Integer32):
    """Custom type configMaxResponseTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConfigMaxResponseTime_Type.__name__ = "Integer32"
_ConfigMaxResponseTime_Object = MibTableColumn
configMaxResponseTime = _ConfigMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 12),
    _ConfigMaxResponseTime_Type()
)
configMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configMaxResponseTime.setStatus("current")


class _ConfigEnableFastLeave_Type(Integer32):
    """Custom type configEnableFastLeave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ConfigEnableFastLeave_Type.__name__ = "Integer32"
_ConfigEnableFastLeave_Object = MibTableColumn
configEnableFastLeave = _ConfigEnableFastLeave_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 13),
    _ConfigEnableFastLeave_Type()
)
configEnableFastLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configEnableFastLeave.setStatus("current")


class _ConfigLastMemberQueryTime_Type(Integer32):
    """Custom type configLastMemberQueryTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConfigLastMemberQueryTime_Type.__name__ = "Integer32"
_ConfigLastMemberQueryTime_Object = MibTableColumn
configLastMemberQueryTime = _ConfigLastMemberQueryTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 14),
    _ConfigLastMemberQueryTime_Type()
)
configLastMemberQueryTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configLastMemberQueryTime.setStatus("current")


class _ConfigNeighborDeadInterval_Type(Integer32):
    """Custom type configNeighborDeadInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConfigNeighborDeadInterval_Type.__name__ = "Integer32"
_ConfigNeighborDeadInterval_Object = MibTableColumn
configNeighborDeadInterval = _ConfigNeighborDeadInterval_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 15),
    _ConfigNeighborDeadInterval_Type()
)
configNeighborDeadInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configNeighborDeadInterval.setStatus("current")


class _ConfigRouterAgingTime_Type(Integer32):
    """Custom type configRouterAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConfigRouterAgingTime_Type.__name__ = "Integer32"
_ConfigRouterAgingTime_Object = MibTableColumn
configRouterAgingTime = _ConfigRouterAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 5, 1, 16),
    _ConfigRouterAgingTime_Type()
)
configRouterAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configRouterAgingTime.setStatus("current")
_StaticMulticastGroupsTable_Object = MibTable
staticMulticastGroupsTable = _StaticMulticastGroupsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 6)
)
if mibBuilder.loadTexts:
    staticMulticastGroupsTable.setStatus("current")
_StaticMulticastGroupsEntry_Object = MibTableRow
staticMulticastGroupsEntry = _StaticMulticastGroupsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 6, 1)
)
staticMulticastGroupsEntry.setIndexNames(
    (0, "G6-IGMP-MIB", "staticMulticastGroupsIndex"),
)
if mibBuilder.loadTexts:
    staticMulticastGroupsEntry.setStatus("current")


class _StaticMulticastGroupsIndex_Type(Integer32):
    """Custom type staticMulticastGroupsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_StaticMulticastGroupsIndex_Type.__name__ = "Integer32"
_StaticMulticastGroupsIndex_Object = MibTableColumn
staticMulticastGroupsIndex = _StaticMulticastGroupsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 6, 1, 1),
    _StaticMulticastGroupsIndex_Type()
)
staticMulticastGroupsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staticMulticastGroupsIndex.setStatus("current")
_StaticMulticastGroupsName_Type = DisplayString
_StaticMulticastGroupsName_Object = MibTableColumn
staticMulticastGroupsName = _StaticMulticastGroupsName_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 6, 1, 2),
    _StaticMulticastGroupsName_Type()
)
staticMulticastGroupsName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMulticastGroupsName.setStatus("current")
_StaticMulticastGroupsDescription_Type = DisplayString
_StaticMulticastGroupsDescription_Object = MibTableColumn
staticMulticastGroupsDescription = _StaticMulticastGroupsDescription_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 6, 1, 3),
    _StaticMulticastGroupsDescription_Type()
)
staticMulticastGroupsDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMulticastGroupsDescription.setStatus("current")
_StaticMulticastGroupsMulticastMac_Type = MacAddress
_StaticMulticastGroupsMulticastMac_Object = MibTableColumn
staticMulticastGroupsMulticastMac = _StaticMulticastGroupsMulticastMac_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 6, 1, 4),
    _StaticMulticastGroupsMulticastMac_Type()
)
staticMulticastGroupsMulticastMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMulticastGroupsMulticastMac.setStatus("current")
_StaticMulticastGroupsForwardingPortMask_Type = Integer32
_StaticMulticastGroupsForwardingPortMask_Object = MibTableColumn
staticMulticastGroupsForwardingPortMask = _StaticMulticastGroupsForwardingPortMask_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 6, 1, 5),
    _StaticMulticastGroupsForwardingPortMask_Type()
)
staticMulticastGroupsForwardingPortMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMulticastGroupsForwardingPortMask.setStatus("current")


class _StaticMulticastGroupsVlanId_Type(Integer32):
    """Custom type staticMulticastGroupsVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_StaticMulticastGroupsVlanId_Type.__name__ = "Integer32"
_StaticMulticastGroupsVlanId_Object = MibTableColumn
staticMulticastGroupsVlanId = _StaticMulticastGroupsVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 6, 1, 6),
    _StaticMulticastGroupsVlanId_Type()
)
staticMulticastGroupsVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staticMulticastGroupsVlanId.setStatus("current")
_StatusTable_Object = MibTable
statusTable = _StatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100)
)
if mibBuilder.loadTexts:
    statusTable.setStatus("current")
_StatusEntry_Object = MibTableRow
statusEntry = _StatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1)
)
statusEntry.setIndexNames(
    (0, "G6-IGMP-MIB", "statusIndex"),
)
if mibBuilder.loadTexts:
    statusEntry.setStatus("current")


class _StatusIndex_Type(Integer32):
    """Custom type statusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_StatusIndex_Type.__name__ = "Integer32"
_StatusIndex_Object = MibTableColumn
statusIndex = _StatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 1),
    _StatusIndex_Type()
)
statusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    statusIndex.setStatus("current")
_StatusIgmpRouterPorts_Type = Integer32
_StatusIgmpRouterPorts_Object = MibTableColumn
statusIgmpRouterPorts = _StatusIgmpRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 2),
    _StatusIgmpRouterPorts_Type()
)
statusIgmpRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusIgmpRouterPorts.setStatus("current")
_StatusRxGeneralQueries_Type = Unsigned32
_StatusRxGeneralQueries_Object = MibTableColumn
statusRxGeneralQueries = _StatusRxGeneralQueries_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 3),
    _StatusRxGeneralQueries_Type()
)
statusRxGeneralQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRxGeneralQueries.setStatus("current")
_StatusRxGroupQueries_Type = Unsigned32
_StatusRxGroupQueries_Object = MibTableColumn
statusRxGroupQueries = _StatusRxGroupQueries_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 4),
    _StatusRxGroupQueries_Type()
)
statusRxGroupQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRxGroupQueries.setStatus("current")
_StatusRxReports_Type = Unsigned32
_StatusRxReports_Object = MibTableColumn
statusRxReports = _StatusRxReports_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 5),
    _StatusRxReports_Type()
)
statusRxReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRxReports.setStatus("current")
_StatusRxLeaves_Type = Unsigned32
_StatusRxLeaves_Object = MibTableColumn
statusRxLeaves = _StatusRxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 6),
    _StatusRxLeaves_Type()
)
statusRxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRxLeaves.setStatus("current")
_StatusRxAdvertisements_Type = Unsigned32
_StatusRxAdvertisements_Object = MibTableColumn
statusRxAdvertisements = _StatusRxAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 7),
    _StatusRxAdvertisements_Type()
)
statusRxAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRxAdvertisements.setStatus("current")
_StatusRxTerminations_Type = Unsigned32
_StatusRxTerminations_Object = MibTableColumn
statusRxTerminations = _StatusRxTerminations_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 8),
    _StatusRxTerminations_Type()
)
statusRxTerminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRxTerminations.setStatus("current")
_StatusRxUnsupported_Type = Unsigned32
_StatusRxUnsupported_Object = MibTableColumn
statusRxUnsupported = _StatusRxUnsupported_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 9),
    _StatusRxUnsupported_Type()
)
statusRxUnsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRxUnsupported.setStatus("current")
_StatusRxErrors_Type = Unsigned32
_StatusRxErrors_Object = MibTableColumn
statusRxErrors = _StatusRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 10),
    _StatusRxErrors_Type()
)
statusRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusRxErrors.setStatus("current")
_StatusTxSolicitations_Type = Unsigned32
_StatusTxSolicitations_Object = MibTableColumn
statusTxSolicitations = _StatusTxSolicitations_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 100, 1, 11),
    _StatusTxSolicitations_Type()
)
statusTxSolicitations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statusTxSolicitations.setStatus("current")
_MldStatusTable_Object = MibTable
mldStatusTable = _MldStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101)
)
if mibBuilder.loadTexts:
    mldStatusTable.setStatus("current")
_MldStatusEntry_Object = MibTableRow
mldStatusEntry = _MldStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1)
)
mldStatusEntry.setIndexNames(
    (0, "G6-IGMP-MIB", "mldStatusIndex"),
)
if mibBuilder.loadTexts:
    mldStatusEntry.setStatus("current")


class _MldStatusIndex_Type(Integer32):
    """Custom type mldStatusIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_MldStatusIndex_Type.__name__ = "Integer32"
_MldStatusIndex_Object = MibTableColumn
mldStatusIndex = _MldStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 1),
    _MldStatusIndex_Type()
)
mldStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mldStatusIndex.setStatus("current")
_MldStatusMldRouterPorts_Type = Integer32
_MldStatusMldRouterPorts_Object = MibTableColumn
mldStatusMldRouterPorts = _MldStatusMldRouterPorts_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 2),
    _MldStatusMldRouterPorts_Type()
)
mldStatusMldRouterPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatusMldRouterPorts.setStatus("current")
_MldStatusRxGeneralQueries_Type = Unsigned32
_MldStatusRxGeneralQueries_Object = MibTableColumn
mldStatusRxGeneralQueries = _MldStatusRxGeneralQueries_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 3),
    _MldStatusRxGeneralQueries_Type()
)
mldStatusRxGeneralQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatusRxGeneralQueries.setStatus("current")
_MldStatusRxGroupQueries_Type = Unsigned32
_MldStatusRxGroupQueries_Object = MibTableColumn
mldStatusRxGroupQueries = _MldStatusRxGroupQueries_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 4),
    _MldStatusRxGroupQueries_Type()
)
mldStatusRxGroupQueries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatusRxGroupQueries.setStatus("current")
_MldStatusRxReports_Type = Unsigned32
_MldStatusRxReports_Object = MibTableColumn
mldStatusRxReports = _MldStatusRxReports_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 5),
    _MldStatusRxReports_Type()
)
mldStatusRxReports.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatusRxReports.setStatus("current")
_MldStatusRxLeaves_Type = Unsigned32
_MldStatusRxLeaves_Object = MibTableColumn
mldStatusRxLeaves = _MldStatusRxLeaves_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 6),
    _MldStatusRxLeaves_Type()
)
mldStatusRxLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatusRxLeaves.setStatus("current")
_MldStatusRxAdvertisements_Type = Unsigned32
_MldStatusRxAdvertisements_Object = MibTableColumn
mldStatusRxAdvertisements = _MldStatusRxAdvertisements_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 7),
    _MldStatusRxAdvertisements_Type()
)
mldStatusRxAdvertisements.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatusRxAdvertisements.setStatus("current")
_MldStatusRxTerminations_Type = Unsigned32
_MldStatusRxTerminations_Object = MibTableColumn
mldStatusRxTerminations = _MldStatusRxTerminations_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 8),
    _MldStatusRxTerminations_Type()
)
mldStatusRxTerminations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatusRxTerminations.setStatus("current")
_MldStatusRxUnsupported_Type = Unsigned32
_MldStatusRxUnsupported_Object = MibTableColumn
mldStatusRxUnsupported = _MldStatusRxUnsupported_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 9),
    _MldStatusRxUnsupported_Type()
)
mldStatusRxUnsupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatusRxUnsupported.setStatus("current")
_MldStatusRxErrors_Type = Unsigned32
_MldStatusRxErrors_Object = MibTableColumn
mldStatusRxErrors = _MldStatusRxErrors_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 10),
    _MldStatusRxErrors_Type()
)
mldStatusRxErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatusRxErrors.setStatus("current")
_MldStatusTxSolicitations_Type = Unsigned32
_MldStatusTxSolicitations_Object = MibTableColumn
mldStatusTxSolicitations = _MldStatusTxSolicitations_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 2, 40, 101, 1, 11),
    _MldStatusTxSolicitations_Type()
)
mldStatusTxSolicitations.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mldStatusTxSolicitations.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-IGMP-MIB",
    **{"protocol": protocol,
       "igmp": igmp,
       "igmpEnableIgmpSnooping": igmpEnableIgmpSnooping,
       "igmpEnableMldSnooping": igmpEnableMldSnooping,
       "igmpShowMulticastForVlan": igmpShowMulticastForVlan,
       "igmpShowMulticastForPort": igmpShowMulticastForPort,
       "configTable": configTable,
       "configEntry": configEntry,
       "configIndex": configIndex,
       "configVlanId": configVlanId,
       "configEnableIgmpSnooping": configEnableIgmpSnooping,
       "configEnableMldSnooping": configEnableMldSnooping,
       "configSnoopingPorts": configSnoopingPorts,
       "configStaticRouterPorts": configStaticRouterPorts,
       "configMulticastRouterDetection": configMulticastRouterDetection,
       "configEnableReportAggregation": configEnableReportAggregation,
       "configEnableFloodingUnregisterPkt": configEnableFloodingUnregisterPkt,
       "configMcastGroupLimit": configMcastGroupLimit,
       "configGroupMembershipInterval": configGroupMembershipInterval,
       "configMaxResponseTime": configMaxResponseTime,
       "configEnableFastLeave": configEnableFastLeave,
       "configLastMemberQueryTime": configLastMemberQueryTime,
       "configNeighborDeadInterval": configNeighborDeadInterval,
       "configRouterAgingTime": configRouterAgingTime,
       "staticMulticastGroupsTable": staticMulticastGroupsTable,
       "staticMulticastGroupsEntry": staticMulticastGroupsEntry,
       "staticMulticastGroupsIndex": staticMulticastGroupsIndex,
       "staticMulticastGroupsName": staticMulticastGroupsName,
       "staticMulticastGroupsDescription": staticMulticastGroupsDescription,
       "staticMulticastGroupsMulticastMac": staticMulticastGroupsMulticastMac,
       "staticMulticastGroupsForwardingPortMask": staticMulticastGroupsForwardingPortMask,
       "staticMulticastGroupsVlanId": staticMulticastGroupsVlanId,
       "statusTable": statusTable,
       "statusEntry": statusEntry,
       "statusIndex": statusIndex,
       "statusIgmpRouterPorts": statusIgmpRouterPorts,
       "statusRxGeneralQueries": statusRxGeneralQueries,
       "statusRxGroupQueries": statusRxGroupQueries,
       "statusRxReports": statusRxReports,
       "statusRxLeaves": statusRxLeaves,
       "statusRxAdvertisements": statusRxAdvertisements,
       "statusRxTerminations": statusRxTerminations,
       "statusRxUnsupported": statusRxUnsupported,
       "statusRxErrors": statusRxErrors,
       "statusTxSolicitations": statusTxSolicitations,
       "mldStatusTable": mldStatusTable,
       "mldStatusEntry": mldStatusEntry,
       "mldStatusIndex": mldStatusIndex,
       "mldStatusMldRouterPorts": mldStatusMldRouterPorts,
       "mldStatusRxGeneralQueries": mldStatusRxGeneralQueries,
       "mldStatusRxGroupQueries": mldStatusRxGroupQueries,
       "mldStatusRxReports": mldStatusRxReports,
       "mldStatusRxLeaves": mldStatusRxLeaves,
       "mldStatusRxAdvertisements": mldStatusRxAdvertisements,
       "mldStatusRxTerminations": mldStatusRxTerminations,
       "mldStatusRxUnsupported": mldStatusRxUnsupported,
       "mldStatusRxErrors": mldStatusRxErrors,
       "mldStatusTxSolicitations": mldStatusTxSolicitations}
)
