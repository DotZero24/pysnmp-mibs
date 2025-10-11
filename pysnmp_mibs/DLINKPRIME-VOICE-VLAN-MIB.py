# SNMP MIB module (DLINKPRIME-VOICE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-VOICE-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:45:36 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,
 VlanIdOrNone) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIdOrNone")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

dlinkPrimeVoiceVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 27)
)
if mibBuilder.loadTexts:
    dlinkPrimeVoiceVlanMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DpVoiceVlanMIBNotifications_ObjectIdentity = ObjectIdentity
dpVoiceVlanMIBNotifications = _DpVoiceVlanMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 0)
)
_DpVoiceVlanMIBObjects_ObjectIdentity = ObjectIdentity
dpVoiceVlanMIBObjects = _DpVoiceVlanMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1)
)
_DpVoiceVlanGlobal_ObjectIdentity = ObjectIdentity
dpVoiceVlanGlobal = _DpVoiceVlanGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1)
)
_DpVoiceVlanEnabled_Type = TruthValue
_DpVoiceVlanEnabled_Object = MibScalar
dpVoiceVlanEnabled = _DpVoiceVlanEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1, 1),
    _DpVoiceVlanEnabled_Type()
)
dpVoiceVlanEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVoiceVlanEnabled.setStatus("current")


class _DpVoiceVlanVlanId_Type(VlanIdOrNone):
    """Custom type dpVoiceVlanVlanId based on VlanIdOrNone"""
    defaultValue = 0


_DpVoiceVlanVlanId_Type.__name__ = "VlanIdOrNone"
_DpVoiceVlanVlanId_Object = MibScalar
dpVoiceVlanVlanId = _DpVoiceVlanVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1, 2),
    _DpVoiceVlanVlanId_Type()
)
dpVoiceVlanVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVoiceVlanVlanId.setStatus("current")


class _DpVoiceVlanQos_Type(Unsigned32):
    """Custom type dpVoiceVlanQos based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DpVoiceVlanQos_Type.__name__ = "Unsigned32"
_DpVoiceVlanQos_Object = MibScalar
dpVoiceVlanQos = _DpVoiceVlanQos_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1, 3),
    _DpVoiceVlanQos_Type()
)
dpVoiceVlanQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVoiceVlanQos.setStatus("current")


class _DpVoiceVlanAgingTime_Type(Unsigned32):
    """Custom type dpVoiceVlanAgingTime based on Unsigned32"""
    defaultValue = 720

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DpVoiceVlanAgingTime_Type.__name__ = "Unsigned32"
_DpVoiceVlanAgingTime_Object = MibScalar
dpVoiceVlanAgingTime = _DpVoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1, 4),
    _DpVoiceVlanAgingTime_Type()
)
dpVoiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVoiceVlanAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    dpVoiceVlanAgingTime.setUnits("minutes")
_DpVoiceVlanOuiTable_Object = MibTable
dpVoiceVlanOuiTable = _DpVoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dpVoiceVlanOuiTable.setStatus("current")
_DpVoiceVlanOuiEntry_Object = MibTableRow
dpVoiceVlanOuiEntry = _DpVoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1, 5, 1)
)
dpVoiceVlanOuiEntry.setIndexNames(
    (0, "DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanOuiAddr"),
    (0, "DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanOuiMask"),
)
if mibBuilder.loadTexts:
    dpVoiceVlanOuiEntry.setStatus("current")
_DpVoiceVlanOuiAddr_Type = MacAddress
_DpVoiceVlanOuiAddr_Object = MibTableColumn
dpVoiceVlanOuiAddr = _DpVoiceVlanOuiAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1, 5, 1, 1),
    _DpVoiceVlanOuiAddr_Type()
)
dpVoiceVlanOuiAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpVoiceVlanOuiAddr.setStatus("current")
_DpVoiceVlanOuiMask_Type = MacAddress
_DpVoiceVlanOuiMask_Object = MibTableColumn
dpVoiceVlanOuiMask = _DpVoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1, 5, 1, 2),
    _DpVoiceVlanOuiMask_Type()
)
dpVoiceVlanOuiMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpVoiceVlanOuiMask.setStatus("current")


class _DpVoiceVlanOuiDes_Type(SnmpAdminString):
    """Custom type dpVoiceVlanOuiDes based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DpVoiceVlanOuiDes_Type.__name__ = "SnmpAdminString"
_DpVoiceVlanOuiDes_Object = MibTableColumn
dpVoiceVlanOuiDes = _DpVoiceVlanOuiDes_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1, 5, 1, 3),
    _DpVoiceVlanOuiDes_Type()
)
dpVoiceVlanOuiDes.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpVoiceVlanOuiDes.setStatus("current")
_DpVoiceVlanOuiRowStatus_Type = RowStatus
_DpVoiceVlanOuiRowStatus_Object = MibTableColumn
dpVoiceVlanOuiRowStatus = _DpVoiceVlanOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 1, 5, 1, 4),
    _DpVoiceVlanOuiRowStatus_Type()
)
dpVoiceVlanOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpVoiceVlanOuiRowStatus.setStatus("current")
_DpVoiceVlanInterface_ObjectIdentity = ObjectIdentity
dpVoiceVlanInterface = _DpVoiceVlanInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 2)
)
_DpVoiceVlanInterfaceTable_Object = MibTable
dpVoiceVlanInterfaceTable = _DpVoiceVlanInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 2, 1)
)
if mibBuilder.loadTexts:
    dpVoiceVlanInterfaceTable.setStatus("current")
_DpVoiceVlanInterfaceEntry_Object = MibTableRow
dpVoiceVlanInterfaceEntry = _DpVoiceVlanInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 2, 1, 1)
)
dpVoiceVlanInterfaceEntry.setIndexNames(
    (0, "DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanIfIndex"),
)
if mibBuilder.loadTexts:
    dpVoiceVlanInterfaceEntry.setStatus("current")
_DpVoiceVlanIfIndex_Type = InterfaceIndex
_DpVoiceVlanIfIndex_Object = MibTableColumn
dpVoiceVlanIfIndex = _DpVoiceVlanIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 2, 1, 1, 1),
    _DpVoiceVlanIfIndex_Type()
)
dpVoiceVlanIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpVoiceVlanIfIndex.setStatus("current")
_DpVoiceVlanIfEnabled_Type = TruthValue
_DpVoiceVlanIfEnabled_Object = MibTableColumn
dpVoiceVlanIfEnabled = _DpVoiceVlanIfEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 2, 1, 1, 2),
    _DpVoiceVlanIfEnabled_Type()
)
dpVoiceVlanIfEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVoiceVlanIfEnabled.setStatus("current")


class _DpVoiceVlanIfMode_Type(Integer32):
    """Custom type dpVoiceVlanIfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("autoUntagged", 1),
          ("autoTagged", 2),
          ("manual", 3))
    )


_DpVoiceVlanIfMode_Type.__name__ = "Integer32"
_DpVoiceVlanIfMode_Object = MibTableColumn
dpVoiceVlanIfMode = _DpVoiceVlanIfMode_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 2, 1, 1, 3),
    _DpVoiceVlanIfMode_Type()
)
dpVoiceVlanIfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpVoiceVlanIfMode.setStatus("current")
_DpVoiceVlanInfo_ObjectIdentity = ObjectIdentity
dpVoiceVlanInfo = _DpVoiceVlanInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 3)
)
_DpVoiceVlanMemberPorts_Type = PortList
_DpVoiceVlanMemberPorts_Object = MibScalar
dpVoiceVlanMemberPorts = _DpVoiceVlanMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 3, 1),
    _DpVoiceVlanMemberPorts_Type()
)
dpVoiceVlanMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpVoiceVlanMemberPorts.setStatus("current")
_DpVoiceVlanDynamicMemberPorts_Type = PortList
_DpVoiceVlanDynamicMemberPorts_Object = MibScalar
dpVoiceVlanDynamicMemberPorts = _DpVoiceVlanDynamicMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 3, 2),
    _DpVoiceVlanDynamicMemberPorts_Type()
)
dpVoiceVlanDynamicMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpVoiceVlanDynamicMemberPorts.setStatus("current")
_DpVoiceVlanDeviceTable_Object = MibTable
dpVoiceVlanDeviceTable = _DpVoiceVlanDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dpVoiceVlanDeviceTable.setStatus("current")
_DpVoiceVlanDeviceEntry_Object = MibTableRow
dpVoiceVlanDeviceEntry = _DpVoiceVlanDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 3, 3, 1)
)
dpVoiceVlanDeviceEntry.setIndexNames(
    (0, "DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanDevicePortIfindex"),
    (0, "DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanDeviceAddr"),
)
if mibBuilder.loadTexts:
    dpVoiceVlanDeviceEntry.setStatus("current")
_DpVoiceVlanDevicePortIfindex_Type = InterfaceIndex
_DpVoiceVlanDevicePortIfindex_Object = MibTableColumn
dpVoiceVlanDevicePortIfindex = _DpVoiceVlanDevicePortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 3, 3, 1, 1),
    _DpVoiceVlanDevicePortIfindex_Type()
)
dpVoiceVlanDevicePortIfindex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpVoiceVlanDevicePortIfindex.setStatus("current")
_DpVoiceVlanDeviceAddr_Type = MacAddress
_DpVoiceVlanDeviceAddr_Object = MibTableColumn
dpVoiceVlanDeviceAddr = _DpVoiceVlanDeviceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 3, 3, 1, 2),
    _DpVoiceVlanDeviceAddr_Type()
)
dpVoiceVlanDeviceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpVoiceVlanDeviceAddr.setStatus("current")
_DpVoiceVlanDeviceStartTime_Type = DateAndTime
_DpVoiceVlanDeviceStartTime_Object = MibTableColumn
dpVoiceVlanDeviceStartTime = _DpVoiceVlanDeviceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 3, 3, 1, 3),
    _DpVoiceVlanDeviceStartTime_Type()
)
dpVoiceVlanDeviceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpVoiceVlanDeviceStartTime.setStatus("current")


class _DpVoiceVlanDeviceStatus_Type(Integer32):
    """Custom type dpVoiceVlanDeviceStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("aging", 2))
    )


_DpVoiceVlanDeviceStatus_Type.__name__ = "Integer32"
_DpVoiceVlanDeviceStatus_Object = MibTableColumn
dpVoiceVlanDeviceStatus = _DpVoiceVlanDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 1, 3, 3, 1, 4),
    _DpVoiceVlanDeviceStatus_Type()
)
dpVoiceVlanDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpVoiceVlanDeviceStatus.setStatus("current")
_DpVoiceVlanMIBConformance_ObjectIdentity = ObjectIdentity
dpVoiceVlanMIBConformance = _DpVoiceVlanMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 2)
)
_DpVoiceVlanMIBCompliances_ObjectIdentity = ObjectIdentity
dpVoiceVlanMIBCompliances = _DpVoiceVlanMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 2, 1)
)
_DpVoiceVlanMIBGroups_ObjectIdentity = ObjectIdentity
dpVoiceVlanMIBGroups = _DpVoiceVlanMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 2, 2)
)

# Managed Objects groups

dpVoiceVlanBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 2, 2, 1)
)
dpVoiceVlanBasicGroup.setObjects(
      *(("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanEnabled"),
        ("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanVlanId"),
        ("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanQos"),
        ("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanAgingTime"),
        ("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanMemberPorts"),
        ("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanDynamicMemberPorts"))
)
if mibBuilder.loadTexts:
    dpVoiceVlanBasicGroup.setStatus("current")

dpVoiceVlanOUICfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 2, 2, 2)
)
dpVoiceVlanOUICfgGroup.setObjects(
      *(("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanOuiDes"),
        ("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanOuiRowStatus"))
)
if mibBuilder.loadTexts:
    dpVoiceVlanOUICfgGroup.setStatus("current")

dpVoiceVlanDeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 2, 2, 3)
)
dpVoiceVlanDeviceInfoGroup.setObjects(
      *(("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanDeviceStartTime"),
        ("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanDeviceStatus"))
)
if mibBuilder.loadTexts:
    dpVoiceVlanDeviceInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpVoiceVlanMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 27, 2, 1, 1)
)
dpVoiceVlanMIBCompliance.setObjects(
      *(("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanBasicGroup"),
        ("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanOUICfgGroup"),
        ("DLINKPRIME-VOICE-VLAN-MIB", "dpVoiceVlanDeviceInfoGroup"))
)
if mibBuilder.loadTexts:
    dpVoiceVlanMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-VOICE-VLAN-MIB",
    **{"dlinkPrimeVoiceVlanMIB": dlinkPrimeVoiceVlanMIB,
       "dpVoiceVlanMIBNotifications": dpVoiceVlanMIBNotifications,
       "dpVoiceVlanMIBObjects": dpVoiceVlanMIBObjects,
       "dpVoiceVlanGlobal": dpVoiceVlanGlobal,
       "dpVoiceVlanEnabled": dpVoiceVlanEnabled,
       "dpVoiceVlanVlanId": dpVoiceVlanVlanId,
       "dpVoiceVlanQos": dpVoiceVlanQos,
       "dpVoiceVlanAgingTime": dpVoiceVlanAgingTime,
       "dpVoiceVlanOuiTable": dpVoiceVlanOuiTable,
       "dpVoiceVlanOuiEntry": dpVoiceVlanOuiEntry,
       "dpVoiceVlanOuiAddr": dpVoiceVlanOuiAddr,
       "dpVoiceVlanOuiMask": dpVoiceVlanOuiMask,
       "dpVoiceVlanOuiDes": dpVoiceVlanOuiDes,
       "dpVoiceVlanOuiRowStatus": dpVoiceVlanOuiRowStatus,
       "dpVoiceVlanInterface": dpVoiceVlanInterface,
       "dpVoiceVlanInterfaceTable": dpVoiceVlanInterfaceTable,
       "dpVoiceVlanInterfaceEntry": dpVoiceVlanInterfaceEntry,
       "dpVoiceVlanIfIndex": dpVoiceVlanIfIndex,
       "dpVoiceVlanIfEnabled": dpVoiceVlanIfEnabled,
       "dpVoiceVlanIfMode": dpVoiceVlanIfMode,
       "dpVoiceVlanInfo": dpVoiceVlanInfo,
       "dpVoiceVlanMemberPorts": dpVoiceVlanMemberPorts,
       "dpVoiceVlanDynamicMemberPorts": dpVoiceVlanDynamicMemberPorts,
       "dpVoiceVlanDeviceTable": dpVoiceVlanDeviceTable,
       "dpVoiceVlanDeviceEntry": dpVoiceVlanDeviceEntry,
       "dpVoiceVlanDevicePortIfindex": dpVoiceVlanDevicePortIfindex,
       "dpVoiceVlanDeviceAddr": dpVoiceVlanDeviceAddr,
       "dpVoiceVlanDeviceStartTime": dpVoiceVlanDeviceStartTime,
       "dpVoiceVlanDeviceStatus": dpVoiceVlanDeviceStatus,
       "dpVoiceVlanMIBConformance": dpVoiceVlanMIBConformance,
       "dpVoiceVlanMIBCompliances": dpVoiceVlanMIBCompliances,
       "dpVoiceVlanMIBCompliance": dpVoiceVlanMIBCompliance,
       "dpVoiceVlanMIBGroups": dpVoiceVlanMIBGroups,
       "dpVoiceVlanBasicGroup": dpVoiceVlanBasicGroup,
       "dpVoiceVlanOUICfgGroup": dpVoiceVlanOUICfgGroup,
       "dpVoiceVlanDeviceInfoGroup": dpVoiceVlanDeviceInfoGroup}
)
