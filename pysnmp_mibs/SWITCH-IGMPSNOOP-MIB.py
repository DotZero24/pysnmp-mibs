# SNMP MIB module (SWITCH-IGMPSNOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/SWITCH-IGMPSNOOP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:16 2025
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

(dot1qStaticMulticastAddress,
 dot1qStaticMulticastReceivePort,
 dot1qVlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "dot1qStaticMulticastAddress",
    "dot1qStaticMulticastReceivePort",
    "dot1qVlanIndex")

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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

(EnableVar,
 PortList,
 Vlanset) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar",
    "PortList",
    "Vlanset")


# MODULE-IDENTITY

rcIgmpSnoop = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11)
)
if mibBuilder.loadTexts:
    rcIgmpSnoop.setRevisions(
        ("1904-12-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RcIgmpSnoopEnable_Type(EnableVar):
    """Custom type rcIgmpSnoopEnable based on EnableVar"""
    defaultValue = 1


_RcIgmpSnoopEnable_Type.__name__ = "EnableVar"
_RcIgmpSnoopEnable_Object = MibScalar
rcIgmpSnoopEnable = _RcIgmpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 1),
    _RcIgmpSnoopEnable_Type()
)
rcIgmpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpSnoopEnable.setStatus("current")
_RcIgmpSnoopAlerts_Type = TruthValue
_RcIgmpSnoopAlerts_Object = MibScalar
rcIgmpSnoopAlerts = _RcIgmpSnoopAlerts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 2),
    _RcIgmpSnoopAlerts_Type()
)
rcIgmpSnoopAlerts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpSnoopAlerts.setStatus("current")


class _RcIgmpSnoopAging_Type(Integer32):
    """Custom type rcIgmpSnoopAging based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(30, 3600),
    )


_RcIgmpSnoopAging_Type.__name__ = "Integer32"
_RcIgmpSnoopAging_Object = MibScalar
rcIgmpSnoopAging = _RcIgmpSnoopAging_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 3),
    _RcIgmpSnoopAging_Type()
)
rcIgmpSnoopAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpSnoopAging.setStatus("current")
if mibBuilder.loadTexts:
    rcIgmpSnoopAging.setUnits("second")
_RcIgmpSnoopVlan_Type = Vlanset
_RcIgmpSnoopVlan_Object = MibScalar
rcIgmpSnoopVlan = _RcIgmpSnoopVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 4),
    _RcIgmpSnoopVlan_Type()
)
rcIgmpSnoopVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpSnoopVlan.setStatus("current")
_RcIgmpSnoopLeave_Type = Vlanset
_RcIgmpSnoopLeave_Object = MibScalar
rcIgmpSnoopLeave = _RcIgmpSnoopLeave_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 5),
    _RcIgmpSnoopLeave_Type()
)
rcIgmpSnoopLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpSnoopLeave.setStatus("current")
_RcIgmpSnoopFilter_Type = TruthValue
_RcIgmpSnoopFilter_Object = MibScalar
rcIgmpSnoopFilter = _RcIgmpSnoopFilter_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 6),
    _RcIgmpSnoopFilter_Type()
)
rcIgmpSnoopFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpSnoopFilter.setStatus("current")
_RcIgmpSnoopTable_Object = MibTable
rcIgmpSnoopTable = _RcIgmpSnoopTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 7)
)
if mibBuilder.loadTexts:
    rcIgmpSnoopTable.setStatus("current")
_RcIgmpSnoopEntry_Object = MibTableRow
rcIgmpSnoopEntry = _RcIgmpSnoopEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 7, 1)
)
rcIgmpSnoopEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "Q-BRIDGE-MIB", "dot1qStaticMulticastAddress"),
    (0, "Q-BRIDGE-MIB", "dot1qStaticMulticastReceivePort"),
)
if mibBuilder.loadTexts:
    rcIgmpSnoopEntry.setStatus("current")
_RcIgmpSnoopEgressPorts_Type = PortList
_RcIgmpSnoopEgressPorts_Object = MibTableColumn
rcIgmpSnoopEgressPorts = _RcIgmpSnoopEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 7, 1, 1),
    _RcIgmpSnoopEgressPorts_Type()
)
rcIgmpSnoopEgressPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcIgmpSnoopEgressPorts.setStatus("current")
_RcIgmpSnoopMrouterTable_Object = MibTable
rcIgmpSnoopMrouterTable = _RcIgmpSnoopMrouterTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 8)
)
if mibBuilder.loadTexts:
    rcIgmpSnoopMrouterTable.setStatus("current")
_RcIgmpSnoopMrouterEntry_Object = MibTableRow
rcIgmpSnoopMrouterEntry = _RcIgmpSnoopMrouterEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 8, 1)
)
rcIgmpSnoopMrouterEntry.setIndexNames(
    (0, "SWITCH-IGMPSNOOP-MIB", "rcIgmpSnoopMrouterVlan"),
    (0, "SWITCH-IGMPSNOOP-MIB", "rcIgmpSnoopMrouterPort"),
)
if mibBuilder.loadTexts:
    rcIgmpSnoopMrouterEntry.setStatus("current")
_RcIgmpSnoopMrouterVlan_Type = Integer32
_RcIgmpSnoopMrouterVlan_Object = MibTableColumn
rcIgmpSnoopMrouterVlan = _RcIgmpSnoopMrouterVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 8, 1, 1),
    _RcIgmpSnoopMrouterVlan_Type()
)
rcIgmpSnoopMrouterVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIgmpSnoopMrouterVlan.setStatus("current")
_RcIgmpSnoopMrouterPort_Type = Integer32
_RcIgmpSnoopMrouterPort_Object = MibTableColumn
rcIgmpSnoopMrouterPort = _RcIgmpSnoopMrouterPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 8, 1, 2),
    _RcIgmpSnoopMrouterPort_Type()
)
rcIgmpSnoopMrouterPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIgmpSnoopMrouterPort.setStatus("current")
_RcIgmpSnoopMrouterStatus_Type = RowStatus
_RcIgmpSnoopMrouterStatus_Object = MibTableColumn
rcIgmpSnoopMrouterStatus = _RcIgmpSnoopMrouterStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 8, 1, 3),
    _RcIgmpSnoopMrouterStatus_Type()
)
rcIgmpSnoopMrouterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    rcIgmpSnoopMrouterStatus.setStatus("current")
_RcIgmpSnoopStaticMulticastTable_Object = MibTable
rcIgmpSnoopStaticMulticastTable = _RcIgmpSnoopStaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 9)
)
if mibBuilder.loadTexts:
    rcIgmpSnoopStaticMulticastTable.setStatus("current")
_RcIgmpSnoopStaticMulticastEntry_Object = MibTableRow
rcIgmpSnoopStaticMulticastEntry = _RcIgmpSnoopStaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 9, 1)
)
rcIgmpSnoopStaticMulticastEntry.setIndexNames(
    (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"),
    (0, "SWITCH-IGMPSNOOP-MIB", "rcIgmpSnoopStaticMulticastAddress"),
)
if mibBuilder.loadTexts:
    rcIgmpSnoopStaticMulticastEntry.setStatus("current")
_RcIgmpSnoopStaticMulticastAddress_Type = IpAddress
_RcIgmpSnoopStaticMulticastAddress_Object = MibTableColumn
rcIgmpSnoopStaticMulticastAddress = _RcIgmpSnoopStaticMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 9, 1, 1),
    _RcIgmpSnoopStaticMulticastAddress_Type()
)
rcIgmpSnoopStaticMulticastAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcIgmpSnoopStaticMulticastAddress.setStatus("current")
_RcIgmpSnoopStaticMulticastStaticEgressPorts_Type = PortList
_RcIgmpSnoopStaticMulticastStaticEgressPorts_Object = MibTableColumn
rcIgmpSnoopStaticMulticastStaticEgressPorts = _RcIgmpSnoopStaticMulticastStaticEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 9, 1, 2),
    _RcIgmpSnoopStaticMulticastStaticEgressPorts_Type()
)
rcIgmpSnoopStaticMulticastStaticEgressPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpSnoopStaticMulticastStaticEgressPorts.setStatus("current")


class _RcIgmpSnoopStaticMulticastStatus_Type(Integer32):
    """Custom type rcIgmpSnoopStaticMulticastStatus based on Integer32"""
    defaultValue = 3

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
        *(("other", 1),
          ("invalid", 2),
          ("permanent", 3),
          ("deleteOnReset", 4),
          ("deleteOnTimeout", 5))
    )


_RcIgmpSnoopStaticMulticastStatus_Type.__name__ = "Integer32"
_RcIgmpSnoopStaticMulticastStatus_Object = MibTableColumn
rcIgmpSnoopStaticMulticastStatus = _RcIgmpSnoopStaticMulticastStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 11, 9, 1, 3),
    _RcIgmpSnoopStaticMulticastStatus_Type()
)
rcIgmpSnoopStaticMulticastStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIgmpSnoopStaticMulticastStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SWITCH-IGMPSNOOP-MIB",
    **{"rcIgmpSnoop": rcIgmpSnoop,
       "rcIgmpSnoopEnable": rcIgmpSnoopEnable,
       "rcIgmpSnoopAlerts": rcIgmpSnoopAlerts,
       "rcIgmpSnoopAging": rcIgmpSnoopAging,
       "rcIgmpSnoopVlan": rcIgmpSnoopVlan,
       "rcIgmpSnoopLeave": rcIgmpSnoopLeave,
       "rcIgmpSnoopFilter": rcIgmpSnoopFilter,
       "rcIgmpSnoopTable": rcIgmpSnoopTable,
       "rcIgmpSnoopEntry": rcIgmpSnoopEntry,
       "rcIgmpSnoopEgressPorts": rcIgmpSnoopEgressPorts,
       "rcIgmpSnoopMrouterTable": rcIgmpSnoopMrouterTable,
       "rcIgmpSnoopMrouterEntry": rcIgmpSnoopMrouterEntry,
       "rcIgmpSnoopMrouterVlan": rcIgmpSnoopMrouterVlan,
       "rcIgmpSnoopMrouterPort": rcIgmpSnoopMrouterPort,
       "rcIgmpSnoopMrouterStatus": rcIgmpSnoopMrouterStatus,
       "rcIgmpSnoopStaticMulticastTable": rcIgmpSnoopStaticMulticastTable,
       "rcIgmpSnoopStaticMulticastEntry": rcIgmpSnoopStaticMulticastEntry,
       "rcIgmpSnoopStaticMulticastAddress": rcIgmpSnoopStaticMulticastAddress,
       "rcIgmpSnoopStaticMulticastStaticEgressPorts": rcIgmpSnoopStaticMulticastStaticEgressPorts,
       "rcIgmpSnoopStaticMulticastStatus": rcIgmpSnoopStaticMulticastStatus}
)
