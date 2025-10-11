# SNMP MIB module (DLINKPRIME-MGMD-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-MGMD-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:45:42 2025
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

(dlinkPrimeCommon,) = mibBuilder.importSymbols(
    "DLINK-ID-REC-MIB",
    "dlinkPrimeCommon")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(PortList,
 VlanId,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "VlanIdOrNone")

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

dlinkPrimeMgmdSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 9)
)
if mibBuilder.loadTexts:
    dlinkPrimeMgmdSnoopingMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class SnoopingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmpSnooping", 1),
          ("mldSnooping", 2))
    )



# MIB Managed Objects in the order of their OIDs

_DpMgmdSnpMIBNotifications_ObjectIdentity = ObjectIdentity
dpMgmdSnpMIBNotifications = _DpMgmdSnpMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 0)
)
_DpMgmdSnpMIBObjects_ObjectIdentity = ObjectIdentity
dpMgmdSnpMIBObjects = _DpMgmdSnpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1)
)
_DpMgmdSnpGlobalCtrl_ObjectIdentity = ObjectIdentity
dpMgmdSnpGlobalCtrl = _DpMgmdSnpGlobalCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 1)
)


class _DpMgmdSnpStateGblEnabled_Type(Bits):
    """Custom type dpMgmdSnpStateGblEnabled based on Bits"""
    namedValues = NamedValues(
        *(("ipv4", 0),
          ("ipv6", 1))
    )

_DpMgmdSnpStateGblEnabled_Type.__name__ = "Bits"
_DpMgmdSnpStateGblEnabled_Object = MibScalar
dpMgmdSnpStateGblEnabled = _DpMgmdSnpStateGblEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 1, 1),
    _DpMgmdSnpStateGblEnabled_Type()
)
dpMgmdSnpStateGblEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpMgmdSnpStateGblEnabled.setStatus("current")
_DpMgmdSnpVlanIfCtrl_ObjectIdentity = ObjectIdentity
dpMgmdSnpVlanIfCtrl = _DpMgmdSnpVlanIfCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 2)
)
_DpMgmdSnpIfTable_Object = MibTable
dpMgmdSnpIfTable = _DpMgmdSnpIfTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dpMgmdSnpIfTable.setStatus("current")
_DpMgmdSnpIfEntry_Object = MibTableRow
dpMgmdSnpIfEntry = _DpMgmdSnpIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 2, 1, 1)
)
dpMgmdSnpIfEntry.setIndexNames(
    (0, "DLINKPRIME-MGMD-SNOOPING-MIB", "dpMgmdSnpIfVlanIfIndex"),
)
if mibBuilder.loadTexts:
    dpMgmdSnpIfEntry.setStatus("current")
_DpMgmdSnpIfVlanIfIndex_Type = InterfaceIndex
_DpMgmdSnpIfVlanIfIndex_Object = MibTableColumn
dpMgmdSnpIfVlanIfIndex = _DpMgmdSnpIfVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 2, 1, 1, 1),
    _DpMgmdSnpIfVlanIfIndex_Type()
)
dpMgmdSnpIfVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpMgmdSnpIfVlanIfIndex.setStatus("current")


class _DpMgmdSnpIfStateEnabled_Type(TruthValue):
    """Custom type dpMgmdSnpIfStateEnabled based on TruthValue"""
    defaultValue = 2


_DpMgmdSnpIfStateEnabled_Type.__name__ = "TruthValue"
_DpMgmdSnpIfStateEnabled_Object = MibTableColumn
dpMgmdSnpIfStateEnabled = _DpMgmdSnpIfStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 2, 1, 1, 2),
    _DpMgmdSnpIfStateEnabled_Type()
)
dpMgmdSnpIfStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpMgmdSnpIfStateEnabled.setStatus("current")


class _DpMgmdSnpIfQuerierStateEnabled_Type(TruthValue):
    """Custom type dpMgmdSnpIfQuerierStateEnabled based on TruthValue"""
    defaultValue = 2


_DpMgmdSnpIfQuerierStateEnabled_Type.__name__ = "TruthValue"
_DpMgmdSnpIfQuerierStateEnabled_Object = MibTableColumn
dpMgmdSnpIfQuerierStateEnabled = _DpMgmdSnpIfQuerierStateEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 2, 1, 1, 3),
    _DpMgmdSnpIfQuerierStateEnabled_Type()
)
dpMgmdSnpIfQuerierStateEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpMgmdSnpIfQuerierStateEnabled.setStatus("current")
_DpMgmdSnpGroupCtrl_ObjectIdentity = ObjectIdentity
dpMgmdSnpGroupCtrl = _DpMgmdSnpGroupCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3)
)
_DpMgmdSnpGroupTable_Object = MibTable
dpMgmdSnpGroupTable = _DpMgmdSnpGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 1)
)
if mibBuilder.loadTexts:
    dpMgmdSnpGroupTable.setStatus("current")
_DpMgmdSnpGroupEntry_Object = MibTableRow
dpMgmdSnpGroupEntry = _DpMgmdSnpGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 1, 1)
)
dpMgmdSnpGroupEntry.setIndexNames(
    (0, "DLINKPRIME-MGMD-SNOOPING-MIB", "dpMgmdSnpGroupVlanIfIndex"),
    (0, "DLINKPRIME-MGMD-SNOOPING-MIB", "dpMgmdSnpGroupAddress"),
)
if mibBuilder.loadTexts:
    dpMgmdSnpGroupEntry.setStatus("current")
_DpMgmdSnpGroupVlanIfIndex_Type = InterfaceIndex
_DpMgmdSnpGroupVlanIfIndex_Object = MibTableColumn
dpMgmdSnpGroupVlanIfIndex = _DpMgmdSnpGroupVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 1, 1, 1),
    _DpMgmdSnpGroupVlanIfIndex_Type()
)
dpMgmdSnpGroupVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpMgmdSnpGroupVlanIfIndex.setStatus("current")
_DpMgmdSnpGroupAddress_Type = InetAddress
_DpMgmdSnpGroupAddress_Object = MibTableColumn
dpMgmdSnpGroupAddress = _DpMgmdSnpGroupAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 1, 1, 2),
    _DpMgmdSnpGroupAddress_Type()
)
dpMgmdSnpGroupAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpMgmdSnpGroupAddress.setStatus("current")
_DpMgmdSnpGroupIfIndex_Type = PortList
_DpMgmdSnpGroupIfIndex_Object = MibTableColumn
dpMgmdSnpGroupIfIndex = _DpMgmdSnpGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 1, 1, 3),
    _DpMgmdSnpGroupIfIndex_Type()
)
dpMgmdSnpGroupIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpMgmdSnpGroupIfIndex.setStatus("current")
_DpMgmdSnpStaticGrpTable_Object = MibTable
dpMgmdSnpStaticGrpTable = _DpMgmdSnpStaticGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 2)
)
if mibBuilder.loadTexts:
    dpMgmdSnpStaticGrpTable.setStatus("current")
_DpMgmdSnpStaticGrpEntry_Object = MibTableRow
dpMgmdSnpStaticGrpEntry = _DpMgmdSnpStaticGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 2, 1)
)
dpMgmdSnpStaticGrpEntry.setIndexNames(
    (0, "DLINKPRIME-MGMD-SNOOPING-MIB", "dpMgmdSnpStaticGrpVlanIfIndex"),
    (0, "DLINKPRIME-MGMD-SNOOPING-MIB", "dpMgmdSnpStaticGrpAddress"),
)
if mibBuilder.loadTexts:
    dpMgmdSnpStaticGrpEntry.setStatus("current")
_DpMgmdSnpStaticGrpVlanIfIndex_Type = InterfaceIndex
_DpMgmdSnpStaticGrpVlanIfIndex_Object = MibTableColumn
dpMgmdSnpStaticGrpVlanIfIndex = _DpMgmdSnpStaticGrpVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 2, 1, 1),
    _DpMgmdSnpStaticGrpVlanIfIndex_Type()
)
dpMgmdSnpStaticGrpVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpMgmdSnpStaticGrpVlanIfIndex.setStatus("current")
_DpMgmdSnpStaticGrpAddress_Type = InetAddress
_DpMgmdSnpStaticGrpAddress_Object = MibTableColumn
dpMgmdSnpStaticGrpAddress = _DpMgmdSnpStaticGrpAddress_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 2, 1, 2),
    _DpMgmdSnpStaticGrpAddress_Type()
)
dpMgmdSnpStaticGrpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpMgmdSnpStaticGrpAddress.setStatus("current")
_DpMgmdSnpStaticGrpIfIndex_Type = PortList
_DpMgmdSnpStaticGrpIfIndex_Object = MibTableColumn
dpMgmdSnpStaticGrpIfIndex = _DpMgmdSnpStaticGrpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 2, 1, 3),
    _DpMgmdSnpStaticGrpIfIndex_Type()
)
dpMgmdSnpStaticGrpIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpMgmdSnpStaticGrpIfIndex.setStatus("current")
_DpMgmdSnpStaticGrpStatus_Type = RowStatus
_DpMgmdSnpStaticGrpStatus_Object = MibTableColumn
dpMgmdSnpStaticGrpStatus = _DpMgmdSnpStaticGrpStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 1, 3, 2, 1, 4),
    _DpMgmdSnpStaticGrpStatus_Type()
)
dpMgmdSnpStaticGrpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpMgmdSnpStaticGrpStatus.setStatus("current")
_DpMgmdSnpMIBConformance_ObjectIdentity = ObjectIdentity
dpMgmdSnpMIBConformance = _DpMgmdSnpMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 2)
)
_DpMgmdSnpCompliances_ObjectIdentity = ObjectIdentity
dpMgmdSnpCompliances = _DpMgmdSnpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 2, 1)
)
_DpMgmdSnpGroups_ObjectIdentity = ObjectIdentity
dpMgmdSnpGroups = _DpMgmdSnpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 2, 2)
)

# Managed Objects groups

dpMgmdSnpGblCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 2, 2, 1)
)
dpMgmdSnpGblCfgGroup.setObjects(
    ("DLINKPRIME-MGMD-SNOOPING-MIB", "dpMgmdSnpStateGblEnabled")
)
if mibBuilder.loadTexts:
    dpMgmdSnpGblCfgGroup.setStatus("current")

dpMgmdSnpVlanIfCfgGoup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 2, 2, 2)
)
dpMgmdSnpVlanIfCfgGoup.setObjects(
      *(("DLINKPRIME-MGMD-SNOOPING-MIB", "dpMgmdSnpIfStateEnabled"),
        ("DLINKPRIME-MGMD-SNOOPING-MIB", "dpMgmdSnpIfQuerierStateEnabled"))
)
if mibBuilder.loadTexts:
    dpMgmdSnpVlanIfCfgGoup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpMgmdSnpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 9, 2, 1, 1)
)
dpMgmdSnpCompliance.setObjects(
      *(("DLINKPRIME-MGMD-SNOOPING-MIB", "dpMgmdSnpGblCfgGroup"),
        ("DLINKPRIME-MGMD-SNOOPING-MIB", "dpMgmdSnpVlanIfCfgGoup"))
)
if mibBuilder.loadTexts:
    dpMgmdSnpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-MGMD-SNOOPING-MIB",
    **{"SnoopingType": SnoopingType,
       "dlinkPrimeMgmdSnoopingMIB": dlinkPrimeMgmdSnoopingMIB,
       "dpMgmdSnpMIBNotifications": dpMgmdSnpMIBNotifications,
       "dpMgmdSnpMIBObjects": dpMgmdSnpMIBObjects,
       "dpMgmdSnpGlobalCtrl": dpMgmdSnpGlobalCtrl,
       "dpMgmdSnpStateGblEnabled": dpMgmdSnpStateGblEnabled,
       "dpMgmdSnpVlanIfCtrl": dpMgmdSnpVlanIfCtrl,
       "dpMgmdSnpIfTable": dpMgmdSnpIfTable,
       "dpMgmdSnpIfEntry": dpMgmdSnpIfEntry,
       "dpMgmdSnpIfVlanIfIndex": dpMgmdSnpIfVlanIfIndex,
       "dpMgmdSnpIfStateEnabled": dpMgmdSnpIfStateEnabled,
       "dpMgmdSnpIfQuerierStateEnabled": dpMgmdSnpIfQuerierStateEnabled,
       "dpMgmdSnpGroupCtrl": dpMgmdSnpGroupCtrl,
       "dpMgmdSnpGroupTable": dpMgmdSnpGroupTable,
       "dpMgmdSnpGroupEntry": dpMgmdSnpGroupEntry,
       "dpMgmdSnpGroupVlanIfIndex": dpMgmdSnpGroupVlanIfIndex,
       "dpMgmdSnpGroupAddress": dpMgmdSnpGroupAddress,
       "dpMgmdSnpGroupIfIndex": dpMgmdSnpGroupIfIndex,
       "dpMgmdSnpStaticGrpTable": dpMgmdSnpStaticGrpTable,
       "dpMgmdSnpStaticGrpEntry": dpMgmdSnpStaticGrpEntry,
       "dpMgmdSnpStaticGrpVlanIfIndex": dpMgmdSnpStaticGrpVlanIfIndex,
       "dpMgmdSnpStaticGrpAddress": dpMgmdSnpStaticGrpAddress,
       "dpMgmdSnpStaticGrpIfIndex": dpMgmdSnpStaticGrpIfIndex,
       "dpMgmdSnpStaticGrpStatus": dpMgmdSnpStaticGrpStatus,
       "dpMgmdSnpMIBConformance": dpMgmdSnpMIBConformance,
       "dpMgmdSnpCompliances": dpMgmdSnpCompliances,
       "dpMgmdSnpCompliance": dpMgmdSnpCompliance,
       "dpMgmdSnpGroups": dpMgmdSnpGroups,
       "dpMgmdSnpGblCfgGroup": dpMgmdSnpGblCfgGroup,
       "dpMgmdSnpVlanIfCfgGoup": dpMgmdSnpVlanIfCfgGoup}
)
