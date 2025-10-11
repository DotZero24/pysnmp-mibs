# SNMP MIB module (QTECH-IP-MANAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-IP-MANAGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:47 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

qtechIpManageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12)
)
if mibBuilder.loadTexts:
    qtechIpManageMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechDhcpMIBObjects_ObjectIdentity = ObjectIdentity
qtechDhcpMIBObjects = _QtechDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 1)
)


class _QtechDhcpRelayAgentGlobalStatus_Type(EnabledStatus):
    """Custom type qtechDhcpRelayAgentGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_QtechDhcpRelayAgentGlobalStatus_Type.__name__ = "EnabledStatus"
_QtechDhcpRelayAgentGlobalStatus_Object = MibScalar
qtechDhcpRelayAgentGlobalStatus = _QtechDhcpRelayAgentGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 1, 2),
    _QtechDhcpRelayAgentGlobalStatus_Type()
)
qtechDhcpRelayAgentGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDhcpRelayAgentGlobalStatus.setStatus("current")
_QtechDhcpServerIp_Type = IpAddress
_QtechDhcpServerIp_Object = MibScalar
qtechDhcpServerIp = _QtechDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 1, 3),
    _QtechDhcpServerIp_Type()
)
qtechDhcpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechDhcpServerIp.setStatus("current")
_QtechIpMIBObjects_ObjectIdentity = ObjectIdentity
qtechIpMIBObjects = _QtechIpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 2)
)
_QtechIpDefaultGateWay_Type = IpAddress
_QtechIpDefaultGateWay_Object = MibScalar
qtechIpDefaultGateWay = _QtechIpDefaultGateWay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 2, 1),
    _QtechIpDefaultGateWay_Type()
)
qtechIpDefaultGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIpDefaultGateWay.setStatus("current")
_QtechIpManageMIBConformance_ObjectIdentity = ObjectIdentity
qtechIpManageMIBConformance = _QtechIpManageMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 3)
)
_QtechIpManageMIBCompliances_ObjectIdentity = ObjectIdentity
qtechIpManageMIBCompliances = _QtechIpManageMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 3, 1)
)
_QtechIpManageMIBGroups_ObjectIdentity = ObjectIdentity
qtechIpManageMIBGroups = _QtechIpManageMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 3, 2)
)

# Managed Objects groups

qtechL2L3DhcpManageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 3, 2, 1)
)
qtechL2L3DhcpManageMIBGroup.setObjects(
      *(("QTECH-IP-MANAGE-MIB", "qtechDhcpRelayAgentGlobalStatus"),
        ("QTECH-IP-MANAGE-MIB", "qtechDhcpServerIp"))
)
if mibBuilder.loadTexts:
    qtechL2L3DhcpManageMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechIpManageMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 12, 3, 1, 1)
)
qtechIpManageMIBCompliance.setObjects(
    ("QTECH-IP-MANAGE-MIB", "qtechL2L3DhcpManageMIBGroup")
)
if mibBuilder.loadTexts:
    qtechIpManageMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-IP-MANAGE-MIB",
    **{"qtechIpManageMIB": qtechIpManageMIB,
       "qtechDhcpMIBObjects": qtechDhcpMIBObjects,
       "qtechDhcpRelayAgentGlobalStatus": qtechDhcpRelayAgentGlobalStatus,
       "qtechDhcpServerIp": qtechDhcpServerIp,
       "qtechIpMIBObjects": qtechIpMIBObjects,
       "qtechIpDefaultGateWay": qtechIpDefaultGateWay,
       "qtechIpManageMIBConformance": qtechIpManageMIBConformance,
       "qtechIpManageMIBCompliances": qtechIpManageMIBCompliances,
       "qtechIpManageMIBCompliance": qtechIpManageMIBCompliance,
       "qtechIpManageMIBGroups": qtechIpManageMIBGroups,
       "qtechL2L3DhcpManageMIBGroup": qtechL2L3DhcpManageMIBGroup}
)
