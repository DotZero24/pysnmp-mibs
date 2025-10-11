# SNMP MIB module (RUGGEDCOM-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:42 2025
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

(ruggedcomMgmt,) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomMgmt")

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

rcIp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3)
)
if mibBuilder.loadTexts:
    rcIp.setRevisions(
        ("2013-12-11 10:00",
         "2008-11-11 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcIpConfig_ObjectIdentity = ObjectIdentity
rcIpConfig = _RcIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3, 1)
)
if mibBuilder.loadTexts:
    rcIpConfig.setStatus("current")
_RcIpConfigMgmtIpAddress_Type = IpAddress
_RcIpConfigMgmtIpAddress_Object = MibScalar
rcIpConfigMgmtIpAddress = _RcIpConfigMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3, 1, 1),
    _RcIpConfigMgmtIpAddress_Type()
)
rcIpConfigMgmtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpConfigMgmtIpAddress.setStatus("current")
_RcIpConfigMgmtIpSubnet_Type = IpAddress
_RcIpConfigMgmtIpSubnet_Object = MibScalar
rcIpConfigMgmtIpSubnet = _RcIpConfigMgmtIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3, 1, 2),
    _RcIpConfigMgmtIpSubnet_Type()
)
rcIpConfigMgmtIpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpConfigMgmtIpSubnet.setStatus("current")
_RcIpConfigDefaultGateway_Type = IpAddress
_RcIpConfigDefaultGateway_Object = MibScalar
rcIpConfigDefaultGateway = _RcIpConfigDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3, 1, 3),
    _RcIpConfigDefaultGateway_Type()
)
rcIpConfigDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpConfigDefaultGateway.setStatus("current")
_RcIpConfigDfltMgmtIpAddress_Type = IpAddress
_RcIpConfigDfltMgmtIpAddress_Object = MibScalar
rcIpConfigDfltMgmtIpAddress = _RcIpConfigDfltMgmtIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3, 1, 4),
    _RcIpConfigDfltMgmtIpAddress_Type()
)
rcIpConfigDfltMgmtIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpConfigDfltMgmtIpAddress.setStatus("current")
_RcIpConfigDfltMgmtIpSubnet_Type = IpAddress
_RcIpConfigDfltMgmtIpSubnet_Object = MibScalar
rcIpConfigDfltMgmtIpSubnet = _RcIpConfigDfltMgmtIpSubnet_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3, 1, 5),
    _RcIpConfigDfltMgmtIpSubnet_Type()
)
rcIpConfigDfltMgmtIpSubnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcIpConfigDfltMgmtIpSubnet.setStatus("current")
_RcIpConformance_ObjectIdentity = ObjectIdentity
rcIpConformance = _RcIpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3, 5)
)
_RcIpGroups_ObjectIdentity = ObjectIdentity
rcIpGroups = _RcIpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3, 5, 1)
)

# Managed Objects groups

rcIpObjectsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3, 5, 1, 1)
)
rcIpObjectsGroup.setObjects(
      *(("RUGGEDCOM-IP-MIB", "rcIpConfigMgmtIpAddress"),
        ("RUGGEDCOM-IP-MIB", "rcIpConfigMgmtIpSubnet"),
        ("RUGGEDCOM-IP-MIB", "rcIpConfigDefaultGateway"))
)
if mibBuilder.loadTexts:
    rcIpObjectsGroup.setStatus("current")

rcIpObjectsGroupDflt = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 3, 5, 1, 2)
)
rcIpObjectsGroupDflt.setObjects(
      *(("RUGGEDCOM-IP-MIB", "rcIpConfigDfltMgmtIpAddress"),
        ("RUGGEDCOM-IP-MIB", "rcIpConfigDfltMgmtIpSubnet"))
)
if mibBuilder.loadTexts:
    rcIpObjectsGroupDflt.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-IP-MIB",
    **{"rcIp": rcIp,
       "rcIpConfig": rcIpConfig,
       "rcIpConfigMgmtIpAddress": rcIpConfigMgmtIpAddress,
       "rcIpConfigMgmtIpSubnet": rcIpConfigMgmtIpSubnet,
       "rcIpConfigDefaultGateway": rcIpConfigDefaultGateway,
       "rcIpConfigDfltMgmtIpAddress": rcIpConfigDfltMgmtIpAddress,
       "rcIpConfigDfltMgmtIpSubnet": rcIpConfigDfltMgmtIpSubnet,
       "rcIpConformance": rcIpConformance,
       "rcIpGroups": rcIpGroups,
       "rcIpObjectsGroup": rcIpObjectsGroup,
       "rcIpObjectsGroupDflt": rcIpObjectsGroupDflt}
)
