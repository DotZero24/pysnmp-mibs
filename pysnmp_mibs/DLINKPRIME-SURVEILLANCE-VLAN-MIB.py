# SNMP MIB module (DLINKPRIME-SURVEILLANCE-VLAN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINKPRIME-SURVEILLANCE-VLAN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:49:40 2025
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

dlinkPrimeSurveillanceVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 19)
)
if mibBuilder.loadTexts:
    dlinkPrimeSurveillanceVlanMIB.setRevisions(
        ("2014-04-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OuiComponentType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("dlink", 2),
          ("vms", 3),
          ("vmsClient", 4),
          ("videoEncoder", 5),
          ("networkStorage", 6))
    )



# MIB Managed Objects in the order of their OIDs

_DpsvMIBNotifications_ObjectIdentity = ObjectIdentity
dpsvMIBNotifications = _DpsvMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 0)
)
_DpsvMIBObjects_ObjectIdentity = ObjectIdentity
dpsvMIBObjects = _DpsvMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1)
)
_DpsvGlobal_ObjectIdentity = ObjectIdentity
dpsvGlobal = _DpsvGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1)
)
_DpsvEnabled_Type = TruthValue
_DpsvEnabled_Object = MibScalar
dpsvEnabled = _DpsvEnabled_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 1),
    _DpsvEnabled_Type()
)
dpsvEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsvEnabled.setStatus("current")


class _DpsvVlanId_Type(VlanIdOrNone):
    """Custom type dpsvVlanId based on VlanIdOrNone"""
    defaultValue = 0


_DpsvVlanId_Type.__name__ = "VlanIdOrNone"
_DpsvVlanId_Object = MibScalar
dpsvVlanId = _DpsvVlanId_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 2),
    _DpsvVlanId_Type()
)
dpsvVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsvVlanId.setStatus("current")


class _DpsvQos_Type(Unsigned32):
    """Custom type dpsvQos based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DpsvQos_Type.__name__ = "Unsigned32"
_DpsvQos_Object = MibScalar
dpsvQos = _DpsvQos_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 3),
    _DpsvQos_Type()
)
dpsvQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsvQos.setStatus("current")


class _DpsvAgingTime_Type(Unsigned32):
    """Custom type dpsvAgingTime based on Unsigned32"""
    defaultValue = 720

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DpsvAgingTime_Type.__name__ = "Unsigned32"
_DpsvAgingTime_Object = MibScalar
dpsvAgingTime = _DpsvAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 4),
    _DpsvAgingTime_Type()
)
dpsvAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dpsvAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    dpsvAgingTime.setUnits("minutes")
_DpsvOuiTable_Object = MibTable
dpsvOuiTable = _DpsvOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 5)
)
if mibBuilder.loadTexts:
    dpsvOuiTable.setStatus("current")
_DpsvOuiEntry_Object = MibTableRow
dpsvOuiEntry = _DpsvOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 5, 1)
)
dpsvOuiEntry.setIndexNames(
    (0, "DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvOuiAddr"),
    (0, "DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvOuiMask"),
)
if mibBuilder.loadTexts:
    dpsvOuiEntry.setStatus("current")
_DpsvOuiAddr_Type = MacAddress
_DpsvOuiAddr_Object = MibTableColumn
dpsvOuiAddr = _DpsvOuiAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 5, 1, 1),
    _DpsvOuiAddr_Type()
)
dpsvOuiAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpsvOuiAddr.setStatus("current")
_DpsvOuiMask_Type = MacAddress
_DpsvOuiMask_Object = MibTableColumn
dpsvOuiMask = _DpsvOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 5, 1, 2),
    _DpsvOuiMask_Type()
)
dpsvOuiMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpsvOuiMask.setStatus("current")
_DpsvOuiComponentType_Type = OuiComponentType
_DpsvOuiComponentType_Object = MibTableColumn
dpsvOuiComponentType = _DpsvOuiComponentType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 5, 1, 3),
    _DpsvOuiComponentType_Type()
)
dpsvOuiComponentType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsvOuiComponentType.setStatus("current")


class _DpsvOuiDescription_Type(SnmpAdminString):
    """Custom type dpsvOuiDescription based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DpsvOuiDescription_Type.__name__ = "SnmpAdminString"
_DpsvOuiDescription_Object = MibTableColumn
dpsvOuiDescription = _DpsvOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 5, 1, 4),
    _DpsvOuiDescription_Type()
)
dpsvOuiDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsvOuiDescription.setStatus("current")
_DpsvOuiRowStatus_Type = RowStatus
_DpsvOuiRowStatus_Object = MibTableColumn
dpsvOuiRowStatus = _DpsvOuiRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 1, 5, 1, 5),
    _DpsvOuiRowStatus_Type()
)
dpsvOuiRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dpsvOuiRowStatus.setStatus("current")
_DpsvInfo_ObjectIdentity = ObjectIdentity
dpsvInfo = _DpsvInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2)
)
_DpsvMemberPorts_Type = PortList
_DpsvMemberPorts_Object = MibScalar
dpsvMemberPorts = _DpsvMemberPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2, 1),
    _DpsvMemberPorts_Type()
)
dpsvMemberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsvMemberPorts.setStatus("current")
_DpsvDynamicPorts_Type = PortList
_DpsvDynamicPorts_Object = MibScalar
dpsvDynamicPorts = _DpsvDynamicPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2, 2),
    _DpsvDynamicPorts_Type()
)
dpsvDynamicPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsvDynamicPorts.setStatus("current")
_DpsvDeviceTable_Object = MibTable
dpsvDeviceTable = _DpsvDeviceTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2, 3)
)
if mibBuilder.loadTexts:
    dpsvDeviceTable.setStatus("current")
_DpsvDeviceEntry_Object = MibTableRow
dpsvDeviceEntry = _DpsvDeviceEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2, 3, 1)
)
dpsvDeviceEntry.setIndexNames(
    (0, "DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvDevicePortIfIdx"),
    (0, "DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvDeviceAddr"),
)
if mibBuilder.loadTexts:
    dpsvDeviceEntry.setStatus("current")
_DpsvDevicePortIfIdx_Type = InterfaceIndex
_DpsvDevicePortIfIdx_Object = MibTableColumn
dpsvDevicePortIfIdx = _DpsvDevicePortIfIdx_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2, 3, 1, 1),
    _DpsvDevicePortIfIdx_Type()
)
dpsvDevicePortIfIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpsvDevicePortIfIdx.setStatus("current")
_DpsvDeviceAddr_Type = MacAddress
_DpsvDeviceAddr_Object = MibTableColumn
dpsvDeviceAddr = _DpsvDeviceAddr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2, 3, 1, 2),
    _DpsvDeviceAddr_Type()
)
dpsvDeviceAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dpsvDeviceAddr.setStatus("current")
_DpsvDeviceCompType_Type = OuiComponentType
_DpsvDeviceCompType_Object = MibTableColumn
dpsvDeviceCompType = _DpsvDeviceCompType_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2, 3, 1, 3),
    _DpsvDeviceCompType_Type()
)
dpsvDeviceCompType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsvDeviceCompType.setStatus("current")


class _DpsvDeviceDescr_Type(SnmpAdminString):
    """Custom type dpsvDeviceDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DpsvDeviceDescr_Type.__name__ = "SnmpAdminString"
_DpsvDeviceDescr_Object = MibTableColumn
dpsvDeviceDescr = _DpsvDeviceDescr_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2, 3, 1, 4),
    _DpsvDeviceDescr_Type()
)
dpsvDeviceDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsvDeviceDescr.setStatus("current")
_DpsvDeviceStartTime_Type = DateAndTime
_DpsvDeviceStartTime_Object = MibTableColumn
dpsvDeviceStartTime = _DpsvDeviceStartTime_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2, 3, 1, 5),
    _DpsvDeviceStartTime_Type()
)
dpsvDeviceStartTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsvDeviceStartTime.setStatus("current")


class _DpsvDeviceStatus_Type(Integer32):
    """Custom type dpsvDeviceStatus based on Integer32"""
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


_DpsvDeviceStatus_Type.__name__ = "Integer32"
_DpsvDeviceStatus_Object = MibTableColumn
dpsvDeviceStatus = _DpsvDeviceStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 1, 2, 3, 1, 6),
    _DpsvDeviceStatus_Type()
)
dpsvDeviceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dpsvDeviceStatus.setStatus("current")
_DpsvMIBConformance_ObjectIdentity = ObjectIdentity
dpsvMIBConformance = _DpsvMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 2)
)
_DpsvMIBCompliances_ObjectIdentity = ObjectIdentity
dpsvMIBCompliances = _DpsvMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 2, 1)
)
_DpsvMIBGroups_ObjectIdentity = ObjectIdentity
dpsvMIBGroups = _DpsvMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 2, 2)
)

# Managed Objects groups

dpsvBasicGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 2, 2, 1)
)
dpsvBasicGroup.setObjects(
      *(("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvEnabled"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvVlanId"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvQos"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvAgingTime"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvMemberPorts"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvDynamicPorts"))
)
if mibBuilder.loadTexts:
    dpsvBasicGroup.setStatus("current")

dpsvOUICfgGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 2, 2, 2)
)
dpsvOUICfgGroup.setObjects(
      *(("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvOuiComponentType"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvOuiDescription"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvOuiRowStatus"))
)
if mibBuilder.loadTexts:
    dpsvOUICfgGroup.setStatus("current")

dpsvDeviceInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 2, 2, 3)
)
dpsvDeviceInfoGroup.setObjects(
      *(("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvDeviceCompType"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvDeviceDescr"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvDeviceStartTime"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvDeviceStatus"))
)
if mibBuilder.loadTexts:
    dpsvDeviceInfoGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

dpsvMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 171, 15, 19, 2, 1, 1)
)
dpsvMIBCompliance.setObjects(
      *(("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvBasicGroup"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvOUICfgGroup"),
        ("DLINKPRIME-SURVEILLANCE-VLAN-MIB", "dpsvDeviceInfoGroup"))
)
if mibBuilder.loadTexts:
    dpsvMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINKPRIME-SURVEILLANCE-VLAN-MIB",
    **{"OuiComponentType": OuiComponentType,
       "dlinkPrimeSurveillanceVlanMIB": dlinkPrimeSurveillanceVlanMIB,
       "dpsvMIBNotifications": dpsvMIBNotifications,
       "dpsvMIBObjects": dpsvMIBObjects,
       "dpsvGlobal": dpsvGlobal,
       "dpsvEnabled": dpsvEnabled,
       "dpsvVlanId": dpsvVlanId,
       "dpsvQos": dpsvQos,
       "dpsvAgingTime": dpsvAgingTime,
       "dpsvOuiTable": dpsvOuiTable,
       "dpsvOuiEntry": dpsvOuiEntry,
       "dpsvOuiAddr": dpsvOuiAddr,
       "dpsvOuiMask": dpsvOuiMask,
       "dpsvOuiComponentType": dpsvOuiComponentType,
       "dpsvOuiDescription": dpsvOuiDescription,
       "dpsvOuiRowStatus": dpsvOuiRowStatus,
       "dpsvInfo": dpsvInfo,
       "dpsvMemberPorts": dpsvMemberPorts,
       "dpsvDynamicPorts": dpsvDynamicPorts,
       "dpsvDeviceTable": dpsvDeviceTable,
       "dpsvDeviceEntry": dpsvDeviceEntry,
       "dpsvDevicePortIfIdx": dpsvDevicePortIfIdx,
       "dpsvDeviceAddr": dpsvDeviceAddr,
       "dpsvDeviceCompType": dpsvDeviceCompType,
       "dpsvDeviceDescr": dpsvDeviceDescr,
       "dpsvDeviceStartTime": dpsvDeviceStartTime,
       "dpsvDeviceStatus": dpsvDeviceStatus,
       "dpsvMIBConformance": dpsvMIBConformance,
       "dpsvMIBCompliances": dpsvMIBCompliances,
       "dpsvMIBCompliance": dpsvMIBCompliance,
       "dpsvMIBGroups": dpsvMIBGroups,
       "dpsvBasicGroup": dpsvBasicGroup,
       "dpsvOUICfgGroup": dpsvOUICfgGroup,
       "dpsvDeviceInfoGroup": dpsvDeviceInfoGroup}
)
