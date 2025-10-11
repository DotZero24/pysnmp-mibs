# SNMP MIB module (ELTEX-MES-ISS-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:21 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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


# MODULE-IDENTITY

eltMesIssIpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24)
)
if mibBuilder.loadTexts:
    eltMesIssIpMIB.setRevisions(
        ("2021-01-12 00:00",
         "2021-01-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssIpObjects_ObjectIdentity = ObjectIdentity
eltMesIssIpObjects = _EltMesIssIpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1)
)
_EltMesIssIpMgmt_ObjectIdentity = ObjectIdentity
eltMesIssIpMgmt = _EltMesIssIpMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 1)
)
_EltMesIssIpMgmtInterfaceTable_Object = MibTable
eltMesIssIpMgmtInterfaceTable = _EltMesIssIpMgmtInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssIpMgmtInterfaceTable.setStatus("current")
_EltMesIssIpMgmtInterfaceEntry_Object = MibTableRow
eltMesIssIpMgmtInterfaceEntry = _EltMesIssIpMgmtInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 1, 1, 1)
)
eltMesIssIpMgmtInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    eltMesIssIpMgmtInterfaceEntry.setStatus("current")
_EltMesIssIpMgmtInterfaceOuterVlanId_Type = VlanId
_EltMesIssIpMgmtInterfaceOuterVlanId_Object = MibTableColumn
eltMesIssIpMgmtInterfaceOuterVlanId = _EltMesIssIpMgmtInterfaceOuterVlanId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 1, 1, 1, 1),
    _EltMesIssIpMgmtInterfaceOuterVlanId_Type()
)
eltMesIssIpMgmtInterfaceOuterVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpMgmtInterfaceOuterVlanId.setStatus("current")
_EltMesIssIpAuthMgr_ObjectIdentity = ObjectIdentity
eltMesIssIpAuthMgr = _EltMesIssIpAuthMgr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2)
)
_EltMesIssIpAuthMgrTable_Object = MibTable
eltMesIssIpAuthMgrTable = _EltMesIssIpAuthMgrTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssIpAuthMgrTable.setStatus("current")
_EltMesIssIpAuthMgrEntry_Object = MibTableRow
eltMesIssIpAuthMgrEntry = _EltMesIssIpAuthMgrEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2, 1, 1)
)
eltMesIssIpAuthMgrEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-IP-MIB", "eltMesIssIpAuthMgrIpAddrType"),
    (0, "ELTEX-MES-ISS-IP-MIB", "eltMesIssIpAuthMgrIpAddr"),
    (0, "ELTEX-MES-ISS-IP-MIB", "eltMesIssIpAuthMgrIpPrefixLength"),
)
if mibBuilder.loadTexts:
    eltMesIssIpAuthMgrEntry.setStatus("current")
_EltMesIssIpAuthMgrIpAddrType_Type = InetAddressType
_EltMesIssIpAuthMgrIpAddrType_Object = MibTableColumn
eltMesIssIpAuthMgrIpAddrType = _EltMesIssIpAuthMgrIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2, 1, 1, 1),
    _EltMesIssIpAuthMgrIpAddrType_Type()
)
eltMesIssIpAuthMgrIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssIpAuthMgrIpAddrType.setStatus("current")
_EltMesIssIpAuthMgrIpAddr_Type = InetAddress
_EltMesIssIpAuthMgrIpAddr_Object = MibTableColumn
eltMesIssIpAuthMgrIpAddr = _EltMesIssIpAuthMgrIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2, 1, 1, 2),
    _EltMesIssIpAuthMgrIpAddr_Type()
)
eltMesIssIpAuthMgrIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssIpAuthMgrIpAddr.setStatus("current")
_EltMesIssIpAuthMgrIpPrefixLength_Type = InetAddressPrefixLength
_EltMesIssIpAuthMgrIpPrefixLength_Object = MibTableColumn
eltMesIssIpAuthMgrIpPrefixLength = _EltMesIssIpAuthMgrIpPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2, 1, 1, 3),
    _EltMesIssIpAuthMgrIpPrefixLength_Type()
)
eltMesIssIpAuthMgrIpPrefixLength.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssIpAuthMgrIpPrefixLength.setStatus("current")
_EltMesIssIpAuthMgrPortList_Type = PortList
_EltMesIssIpAuthMgrPortList_Object = MibTableColumn
eltMesIssIpAuthMgrPortList = _EltMesIssIpAuthMgrPortList_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2, 1, 1, 4),
    _EltMesIssIpAuthMgrPortList_Type()
)
eltMesIssIpAuthMgrPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpAuthMgrPortList.setStatus("current")
_EltMesIssIpAuthMgrVlanList_Type = OctetString
_EltMesIssIpAuthMgrVlanList_Object = MibTableColumn
eltMesIssIpAuthMgrVlanList = _EltMesIssIpAuthMgrVlanList_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2, 1, 1, 5),
    _EltMesIssIpAuthMgrVlanList_Type()
)
eltMesIssIpAuthMgrVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpAuthMgrVlanList.setStatus("current")


class _EltMesIssIpAuthMgrOOBPort_Type(TruthValue):
    """Custom type eltMesIssIpAuthMgrOOBPort based on TruthValue"""
    defaultValue = 2


_EltMesIssIpAuthMgrOOBPort_Type.__name__ = "TruthValue"
_EltMesIssIpAuthMgrOOBPort_Object = MibTableColumn
eltMesIssIpAuthMgrOOBPort = _EltMesIssIpAuthMgrOOBPort_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2, 1, 1, 6),
    _EltMesIssIpAuthMgrOOBPort_Type()
)
eltMesIssIpAuthMgrOOBPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpAuthMgrOOBPort.setStatus("current")


class _EltMesIssIpAuthMgrAllowedServices_Type(Integer32):
    """Custom type eltMesIssIpAuthMgrAllowedServices based on Integer32"""
    defaultValue = 31


_EltMesIssIpAuthMgrAllowedServices_Type.__name__ = "Integer32"
_EltMesIssIpAuthMgrAllowedServices_Object = MibTableColumn
eltMesIssIpAuthMgrAllowedServices = _EltMesIssIpAuthMgrAllowedServices_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2, 1, 1, 7),
    _EltMesIssIpAuthMgrAllowedServices_Type()
)
eltMesIssIpAuthMgrAllowedServices.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssIpAuthMgrAllowedServices.setStatus("current")
_EltMesIssIpAuthMgrRowStatus_Type = RowStatus
_EltMesIssIpAuthMgrRowStatus_Object = MibTableColumn
eltMesIssIpAuthMgrRowStatus = _EltMesIssIpAuthMgrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 1, 2, 1, 1, 8),
    _EltMesIssIpAuthMgrRowStatus_Type()
)
eltMesIssIpAuthMgrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    eltMesIssIpAuthMgrRowStatus.setStatus("current")
_EltMesIssIpNotifications_ObjectIdentity = ObjectIdentity
eltMesIssIpNotifications = _EltMesIssIpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 24, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-IP-MIB",
    **{"eltMesIssIpMIB": eltMesIssIpMIB,
       "eltMesIssIpObjects": eltMesIssIpObjects,
       "eltMesIssIpMgmt": eltMesIssIpMgmt,
       "eltMesIssIpMgmtInterfaceTable": eltMesIssIpMgmtInterfaceTable,
       "eltMesIssIpMgmtInterfaceEntry": eltMesIssIpMgmtInterfaceEntry,
       "eltMesIssIpMgmtInterfaceOuterVlanId": eltMesIssIpMgmtInterfaceOuterVlanId,
       "eltMesIssIpAuthMgr": eltMesIssIpAuthMgr,
       "eltMesIssIpAuthMgrTable": eltMesIssIpAuthMgrTable,
       "eltMesIssIpAuthMgrEntry": eltMesIssIpAuthMgrEntry,
       "eltMesIssIpAuthMgrIpAddrType": eltMesIssIpAuthMgrIpAddrType,
       "eltMesIssIpAuthMgrIpAddr": eltMesIssIpAuthMgrIpAddr,
       "eltMesIssIpAuthMgrIpPrefixLength": eltMesIssIpAuthMgrIpPrefixLength,
       "eltMesIssIpAuthMgrPortList": eltMesIssIpAuthMgrPortList,
       "eltMesIssIpAuthMgrVlanList": eltMesIssIpAuthMgrVlanList,
       "eltMesIssIpAuthMgrOOBPort": eltMesIssIpAuthMgrOOBPort,
       "eltMesIssIpAuthMgrAllowedServices": eltMesIssIpAuthMgrAllowedServices,
       "eltMesIssIpAuthMgrRowStatus": eltMesIssIpAuthMgrRowStatus,
       "eltMesIssIpNotifications": eltMesIssIpNotifications}
)
