# SNMP MIB module (MY-IP-MANAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruijie/MY-IP-MANAGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:28 2025
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

(myMgmt,) = mibBuilder.importSymbols(
    "MY-SMI",
    "myMgmt")

(ConfigStatus,
 MemberMap) = mibBuilder.importSymbols(
    "MY-TC",
    "ConfigStatus",
    "MemberMap")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(VlanId,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanId")

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

myIpManageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12)
)
if mibBuilder.loadTexts:
    myIpManageMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MyDhcpMIBObjects_ObjectIdentity = ObjectIdentity
myDhcpMIBObjects = _MyDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 1)
)


class _MyDhcpRelayAgentGlobalStatus_Type(EnabledStatus):
    """Custom type myDhcpRelayAgentGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_MyDhcpRelayAgentGlobalStatus_Type.__name__ = "EnabledStatus"
_MyDhcpRelayAgentGlobalStatus_Object = MibScalar
myDhcpRelayAgentGlobalStatus = _MyDhcpRelayAgentGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 1, 2),
    _MyDhcpRelayAgentGlobalStatus_Type()
)
myDhcpRelayAgentGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDhcpRelayAgentGlobalStatus.setStatus("current")
_MyDhcpServerIp_Type = IpAddress
_MyDhcpServerIp_Object = MibScalar
myDhcpServerIp = _MyDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 1, 3),
    _MyDhcpServerIp_Type()
)
myDhcpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myDhcpServerIp.setStatus("current")
_MyIpMIBObjects_ObjectIdentity = ObjectIdentity
myIpMIBObjects = _MyIpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 2)
)
_MyIpDefaultGateWay_Type = IpAddress
_MyIpDefaultGateWay_Object = MibScalar
myIpDefaultGateWay = _MyIpDefaultGateWay_Object(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 2, 1),
    _MyIpDefaultGateWay_Type()
)
myIpDefaultGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    myIpDefaultGateWay.setStatus("current")
_MyIpManageMIBConformance_ObjectIdentity = ObjectIdentity
myIpManageMIBConformance = _MyIpManageMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 3)
)
_MyIpManageMIBCompliances_ObjectIdentity = ObjectIdentity
myIpManageMIBCompliances = _MyIpManageMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 3, 1)
)
_MyIpManageMIBGroups_ObjectIdentity = ObjectIdentity
myIpManageMIBGroups = _MyIpManageMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 3, 2)
)

# Managed Objects groups

myL2L3DhcpManageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 3, 2, 1)
)
myL2L3DhcpManageMIBGroup.setObjects(
      *(("MY-IP-MANAGE-MIB", "myDhcpRelayAgentGlobalStatus"),
        ("MY-IP-MANAGE-MIB", "myDhcpServerIp"))
)
if mibBuilder.loadTexts:
    myL2L3DhcpManageMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

myIpManageMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4881, 1, 1, 10, 2, 12, 3, 1, 1)
)
myIpManageMIBCompliance.setObjects(
    ("MY-IP-MANAGE-MIB", "myL2L3DhcpManageMIBGroup")
)
if mibBuilder.loadTexts:
    myIpManageMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MY-IP-MANAGE-MIB",
    **{"myIpManageMIB": myIpManageMIB,
       "myDhcpMIBObjects": myDhcpMIBObjects,
       "myDhcpRelayAgentGlobalStatus": myDhcpRelayAgentGlobalStatus,
       "myDhcpServerIp": myDhcpServerIp,
       "myIpMIBObjects": myIpMIBObjects,
       "myIpDefaultGateWay": myIpDefaultGateWay,
       "myIpManageMIBConformance": myIpManageMIBConformance,
       "myIpManageMIBCompliances": myIpManageMIBCompliances,
       "myIpManageMIBCompliance": myIpManageMIBCompliance,
       "myIpManageMIBGroups": myIpManageMIBGroups,
       "myL2L3DhcpManageMIBGroup": myL2L3DhcpManageMIBGroup}
)
