# SNMP MIB module (FS-IP-MANAGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-IP-MANAGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:53 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

fsIpManageMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12)
)
if mibBuilder.loadTexts:
    fsIpManageMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDhcpMIBObjects_ObjectIdentity = ObjectIdentity
fsDhcpMIBObjects = _FsDhcpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 1)
)


class _FsDhcpRelayAgentGlobalStatus_Type(EnabledStatus):
    """Custom type fsDhcpRelayAgentGlobalStatus based on EnabledStatus"""
    defaultValue = 2


_FsDhcpRelayAgentGlobalStatus_Type.__name__ = "EnabledStatus"
_FsDhcpRelayAgentGlobalStatus_Object = MibScalar
fsDhcpRelayAgentGlobalStatus = _FsDhcpRelayAgentGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 1, 2),
    _FsDhcpRelayAgentGlobalStatus_Type()
)
fsDhcpRelayAgentGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcpRelayAgentGlobalStatus.setStatus("current")
_FsDhcpServerIp_Type = IpAddress
_FsDhcpServerIp_Object = MibScalar
fsDhcpServerIp = _FsDhcpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 1, 3),
    _FsDhcpServerIp_Type()
)
fsDhcpServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDhcpServerIp.setStatus("current")
_FsIpMIBObjects_ObjectIdentity = ObjectIdentity
fsIpMIBObjects = _FsIpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 2)
)
_FsIpDefaultGateWay_Type = IpAddress
_FsIpDefaultGateWay_Object = MibScalar
fsIpDefaultGateWay = _FsIpDefaultGateWay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 2, 1),
    _FsIpDefaultGateWay_Type()
)
fsIpDefaultGateWay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIpDefaultGateWay.setStatus("current")
_FsIpManageMIBConformance_ObjectIdentity = ObjectIdentity
fsIpManageMIBConformance = _FsIpManageMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 3)
)
_FsIpManageMIBCompliances_ObjectIdentity = ObjectIdentity
fsIpManageMIBCompliances = _FsIpManageMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 3, 1)
)
_FsIpManageMIBGroups_ObjectIdentity = ObjectIdentity
fsIpManageMIBGroups = _FsIpManageMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 3, 2)
)

# Managed Objects groups

fsL2L3DhcpManageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 3, 2, 1)
)
fsL2L3DhcpManageMIBGroup.setObjects(
      *(("FS-IP-MANAGE-MIB", "fsDhcpRelayAgentGlobalStatus"),
        ("FS-IP-MANAGE-MIB", "fsDhcpServerIp"))
)
if mibBuilder.loadTexts:
    fsL2L3DhcpManageMIBGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsIpManageMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 12, 3, 1, 1)
)
fsIpManageMIBCompliance.setObjects(
    ("FS-IP-MANAGE-MIB", "fsL2L3DhcpManageMIBGroup")
)
if mibBuilder.loadTexts:
    fsIpManageMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-IP-MANAGE-MIB",
    **{"fsIpManageMIB": fsIpManageMIB,
       "fsDhcpMIBObjects": fsDhcpMIBObjects,
       "fsDhcpRelayAgentGlobalStatus": fsDhcpRelayAgentGlobalStatus,
       "fsDhcpServerIp": fsDhcpServerIp,
       "fsIpMIBObjects": fsIpMIBObjects,
       "fsIpDefaultGateWay": fsIpDefaultGateWay,
       "fsIpManageMIBConformance": fsIpManageMIBConformance,
       "fsIpManageMIBCompliances": fsIpManageMIBCompliances,
       "fsIpManageMIBCompliance": fsIpManageMIBCompliance,
       "fsIpManageMIBGroups": fsIpManageMIBGroups,
       "fsL2L3DhcpManageMIBGroup": fsL2L3DhcpManageMIBGroup}
)
