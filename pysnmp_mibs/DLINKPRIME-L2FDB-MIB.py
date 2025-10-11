# SNMP MIB module (DLINKPRIME-L2FDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-L2FDB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:52:25 2025
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
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(PortList,
 VlanId,
 dot1qFdbId,
 dot1qStaticUnicastAddress) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanId",
    "dot1qFdbId",
    "dot1qStaticUnicastAddress")

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

dlinkPrimeL2FdbMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 5)
)
if mibBuilder.loadTexts:
    dlinkPrimeL2FdbMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpL2FdbMIBNotifications_ObjectIdentity = ObjectIdentity
dpL2FdbMIBNotifications = _DpL2FdbMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 0)
)
_DpL2FdbMIBObjects_ObjectIdentity = ObjectIdentity
dpL2FdbMIBObjects = _DpL2FdbMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1)
)
_DpL2FdbGblCtrl_ObjectIdentity = ObjectIdentity
dpL2FdbGblCtrl = _DpL2FdbGblCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 1)
)
_DpL2FdbClearCtrl_ObjectIdentity = ObjectIdentity
dpL2FdbClearCtrl = _DpL2FdbClearCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 1, 1)
)


class _DpL2FdbClearAllMacAddr_Type(Integer32):
    """Custom type dpL2FdbClearAllMacAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("noOp", 2))
    )


_DpL2FdbClearAllMacAddr_Type.__name__ = "Integer32"
_DpL2FdbClearAllMacAddr_Object = MibScalar
dpL2FdbClearAllMacAddr = _DpL2FdbClearAllMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 1, 1, 1),
    _DpL2FdbClearAllMacAddr_Type()
)
dpL2FdbClearAllMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpL2FdbClearAllMacAddr.setStatus("current")


class _DpL2FdbAgingTime_Type(Unsigned32):
    """Custom type dpL2FdbAgingTime based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 1000000),
    )


_DpL2FdbAgingTime_Type.__name__ = "Unsigned32"
_DpL2FdbAgingTime_Object = MibScalar
dpL2FdbAgingTime = _DpL2FdbAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 1, 2),
    _DpL2FdbAgingTime_Type()
)
dpL2FdbAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpL2FdbAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    dpL2FdbAgingTime.setUnits("second")
_DpL2FdbStaticUnicastTable_Object = MibTable
dpL2FdbStaticUnicastTable = _DpL2FdbStaticUnicastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 2)
)
if mibBuilder.loadTexts:
    dpL2FdbStaticUnicastTable.setStatus("current")
_DpL2FdbStaticUnicastEntry_Object = MibTableRow
dpL2FdbStaticUnicastEntry = _DpL2FdbStaticUnicastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 2, 1)
)
dpL2FdbStaticUnicastEntry.setIndexNames(
    (0, "DLINKPRIME-L2FDB-MIB", "dpL2FdbStaticUnicastVlanID"),
    (0, "DLINKPRIME-L2FDB-MIB", "dpL2FdbStaticUnicastMacAddr"),
)
if mibBuilder.loadTexts:
    dpL2FdbStaticUnicastEntry.setStatus("current")
_DpL2FdbStaticUnicastVlanID_Type = VlanId
_DpL2FdbStaticUnicastVlanID_Object = MibTableColumn
dpL2FdbStaticUnicastVlanID = _DpL2FdbStaticUnicastVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 2, 1, 1),
    _DpL2FdbStaticUnicastVlanID_Type()
)
dpL2FdbStaticUnicastVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpL2FdbStaticUnicastVlanID.setStatus("current")
_DpL2FdbStaticUnicastMacAddr_Type = MacAddress
_DpL2FdbStaticUnicastMacAddr_Object = MibTableColumn
dpL2FdbStaticUnicastMacAddr = _DpL2FdbStaticUnicastMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 2, 1, 2),
    _DpL2FdbStaticUnicastMacAddr_Type()
)
dpL2FdbStaticUnicastMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpL2FdbStaticUnicastMacAddr.setStatus("current")
_DpL2FdbStaticUnicastPortNum_Type = Integer32
_DpL2FdbStaticUnicastPortNum_Object = MibTableColumn
dpL2FdbStaticUnicastPortNum = _DpL2FdbStaticUnicastPortNum_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 2, 1, 3),
    _DpL2FdbStaticUnicastPortNum_Type()
)
dpL2FdbStaticUnicastPortNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpL2FdbStaticUnicastPortNum.setStatus("current")
_DpL2FdbStaticUnicastRowStatus_Type = RowStatus
_DpL2FdbStaticUnicastRowStatus_Object = MibTableColumn
dpL2FdbStaticUnicastRowStatus = _DpL2FdbStaticUnicastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 2, 1, 4),
    _DpL2FdbStaticUnicastRowStatus_Type()
)
dpL2FdbStaticUnicastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpL2FdbStaticUnicastRowStatus.setStatus("current")
_DpL2FdbStaticMulticastTable_Object = MibTable
dpL2FdbStaticMulticastTable = _DpL2FdbStaticMulticastTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 3)
)
if mibBuilder.loadTexts:
    dpL2FdbStaticMulticastTable.setStatus("current")
_DpL2FdbStaticMulticastEntry_Object = MibTableRow
dpL2FdbStaticMulticastEntry = _DpL2FdbStaticMulticastEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 3, 1)
)
dpL2FdbStaticMulticastEntry.setIndexNames(
    (0, "DLINKPRIME-L2FDB-MIB", "dpL2FdbStaticMulticastVlanID"),
    (0, "DLINKPRIME-L2FDB-MIB", "dpL2FdbStaticMulticastMacAddr"),
)
if mibBuilder.loadTexts:
    dpL2FdbStaticMulticastEntry.setStatus("current")
_DpL2FdbStaticMulticastVlanID_Type = VlanId
_DpL2FdbStaticMulticastVlanID_Object = MibTableColumn
dpL2FdbStaticMulticastVlanID = _DpL2FdbStaticMulticastVlanID_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 3, 1, 1),
    _DpL2FdbStaticMulticastVlanID_Type()
)
dpL2FdbStaticMulticastVlanID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpL2FdbStaticMulticastVlanID.setStatus("current")
_DpL2FdbStaticMulticastMacAddr_Type = MacAddress
_DpL2FdbStaticMulticastMacAddr_Object = MibTableColumn
dpL2FdbStaticMulticastMacAddr = _DpL2FdbStaticMulticastMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 3, 1, 2),
    _DpL2FdbStaticMulticastMacAddr_Type()
)
dpL2FdbStaticMulticastMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpL2FdbStaticMulticastMacAddr.setStatus("current")
_DpL2FdbStaticMulticastEgressPorts_Type = PortList
_DpL2FdbStaticMulticastEgressPorts_Object = MibTableColumn
dpL2FdbStaticMulticastEgressPorts = _DpL2FdbStaticMulticastEgressPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 3, 1, 3),
    _DpL2FdbStaticMulticastEgressPorts_Type()
)
dpL2FdbStaticMulticastEgressPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpL2FdbStaticMulticastEgressPorts.setStatus("current")
_DpL2FdbStaticMulticastRowStatus_Type = RowStatus
_DpL2FdbStaticMulticastRowStatus_Object = MibTableColumn
dpL2FdbStaticMulticastRowStatus = _DpL2FdbStaticMulticastRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 3, 1, 4),
    _DpL2FdbStaticMulticastRowStatus_Type()
)
dpL2FdbStaticMulticastRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpL2FdbStaticMulticastRowStatus.setStatus("current")
_DpL2FdbIfCtrlTable_Object = MibTable
dpL2FdbIfCtrlTable = _DpL2FdbIfCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 4)
)
if mibBuilder.loadTexts:
    dpL2FdbIfCtrlTable.setStatus("current")
_DpL2FdbIfCtrlEntry_Object = MibTableRow
dpL2FdbIfCtrlEntry = _DpL2FdbIfCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 4, 1)
)
dpL2FdbIfCtrlEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    dpL2FdbIfCtrlEntry.setStatus("current")
_DpL2FdbIfMacLearningEnabled_Type = TruthValue
_DpL2FdbIfMacLearningEnabled_Object = MibTableColumn
dpL2FdbIfMacLearningEnabled = _DpL2FdbIfMacLearningEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 4, 1, 1),
    _DpL2FdbIfMacLearningEnabled_Type()
)
dpL2FdbIfMacLearningEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpL2FdbIfMacLearningEnabled.setStatus("current")


class _DpL2FdbMcastFilterMode_Type(Integer32):
    """Custom type dpL2FdbMcastFilterMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("forwardAll", 1),
          ("forwardUnregistered", 2),
          ("filterUnregistered", 3))
    )


_DpL2FdbMcastFilterMode_Type.__name__ = "Integer32"
_DpL2FdbMcastFilterMode_Object = MibScalar
dpL2FdbMcastFilterMode = _DpL2FdbMcastFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 1, 5),
    _DpL2FdbMcastFilterMode_Type()
)
dpL2FdbMcastFilterMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpL2FdbMcastFilterMode.setStatus("current")
_DpL2FdbMIBConformance_ObjectIdentity = ObjectIdentity
dpL2FdbMIBConformance = _DpL2FdbMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 2)
)
_DpL2FdbCompliances_ObjectIdentity = ObjectIdentity
dpL2FdbCompliances = _DpL2FdbCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 2, 1)
)
_DpL2FdbGroups_ObjectIdentity = ObjectIdentity
dpL2FdbGroups = _DpL2FdbGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 2, 2)
)

# Managed Objects groups

dpL2FdbGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 2, 2, 1)
)
dpL2FdbGlobalGroup.setObjects(
      *(("DLINKPRIME-L2FDB-MIB", "dpL2FdbClearAllMacAddr"),
        ("DLINKPRIME-L2FDB-MIB", "dpL2FdbAgingTime"))
)
if mibBuilder.loadTexts:
    dpL2FdbGlobalGroup.setStatus("current")

dpL2FdbMacAddrTableGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 2, 2, 2)
)
dpL2FdbMacAddrTableGroup.setObjects(
      *(("DLINKPRIME-L2FDB-MIB", "dpL2FdbStaticUnicastPortNum"),
        ("DLINKPRIME-L2FDB-MIB", "dpL2FdbStaticUnicastRowStatus"))
)
if mibBuilder.loadTexts:
    dpL2FdbMacAddrTableGroup.setStatus("current")

dpL2FdbInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 2, 2, 3)
)
dpL2FdbInterfaceGroup.setObjects(
    ("DLINKPRIME-L2FDB-MIB", "dpL2FdbIfMacLearningEnabled")
)
if mibBuilder.loadTexts:
    dpL2FdbInterfaceGroup.setStatus("current")

dpL2FdbMcastFilterModeCfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 2, 2, 4)
)
dpL2FdbMcastFilterModeCfgGroup.setObjects(
    ("DLINKPRIME-L2FDB-MIB", "dpL2FdbMcastFilterMode")
)
if mibBuilder.loadTexts:
    dpL2FdbMcastFilterModeCfgGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpL2FdbCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 5, 2, 1, 1)
)
dpL2FdbCompliance.setObjects(
      *(("DLINKPRIME-L2FDB-MIB", "dpL2FdbGlobalGroup"),
        ("DLINKPRIME-L2FDB-MIB", "dpL2FdbMacAddrTableGroup"),
        ("DLINKPRIME-L2FDB-MIB", "dpL2FdbInterfaceGroup"),
        ("DLINKPRIME-L2FDB-MIB", "dpL2FdbMcastFilterModeCfgGroup"))
)
if mibBuilder.loadTexts:
    dpL2FdbCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-L2FDB-MIB",
    **{"dlinkPrimeL2FdbMIB": dlinkPrimeL2FdbMIB,
       "dpL2FdbMIBNotifications": dpL2FdbMIBNotifications,
       "dpL2FdbMIBObjects": dpL2FdbMIBObjects,
       "dpL2FdbGblCtrl": dpL2FdbGblCtrl,
       "dpL2FdbClearCtrl": dpL2FdbClearCtrl,
       "dpL2FdbClearAllMacAddr": dpL2FdbClearAllMacAddr,
       "dpL2FdbAgingTime": dpL2FdbAgingTime,
       "dpL2FdbStaticUnicastTable": dpL2FdbStaticUnicastTable,
       "dpL2FdbStaticUnicastEntry": dpL2FdbStaticUnicastEntry,
       "dpL2FdbStaticUnicastVlanID": dpL2FdbStaticUnicastVlanID,
       "dpL2FdbStaticUnicastMacAddr": dpL2FdbStaticUnicastMacAddr,
       "dpL2FdbStaticUnicastPortNum": dpL2FdbStaticUnicastPortNum,
       "dpL2FdbStaticUnicastRowStatus": dpL2FdbStaticUnicastRowStatus,
       "dpL2FdbStaticMulticastTable": dpL2FdbStaticMulticastTable,
       "dpL2FdbStaticMulticastEntry": dpL2FdbStaticMulticastEntry,
       "dpL2FdbStaticMulticastVlanID": dpL2FdbStaticMulticastVlanID,
       "dpL2FdbStaticMulticastMacAddr": dpL2FdbStaticMulticastMacAddr,
       "dpL2FdbStaticMulticastEgressPorts": dpL2FdbStaticMulticastEgressPorts,
       "dpL2FdbStaticMulticastRowStatus": dpL2FdbStaticMulticastRowStatus,
       "dpL2FdbIfCtrlTable": dpL2FdbIfCtrlTable,
       "dpL2FdbIfCtrlEntry": dpL2FdbIfCtrlEntry,
       "dpL2FdbIfMacLearningEnabled": dpL2FdbIfMacLearningEnabled,
       "dpL2FdbMcastFilterMode": dpL2FdbMcastFilterMode,
       "dpL2FdbMIBConformance": dpL2FdbMIBConformance,
       "dpL2FdbCompliances": dpL2FdbCompliances,
       "dpL2FdbCompliance": dpL2FdbCompliance,
       "dpL2FdbGroups": dpL2FdbGroups,
       "dpL2FdbGlobalGroup": dpL2FdbGlobalGroup,
       "dpL2FdbMacAddrTableGroup": dpL2FdbMacAddrTableGroup,
       "dpL2FdbInterfaceGroup": dpL2FdbInterfaceGroup,
       "dpL2FdbMcastFilterModeCfgGroup": dpL2FdbMcastFilterModeCfgGroup}
)
