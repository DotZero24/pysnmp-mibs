# SNMP MIB module (INFINET-XGPEER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinet/INFINET-XGPEER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:08 2025
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

(xg,) = mibBuilder.importSymbols(
    "INFINET-XG-MIB",
    "xg")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

xgPeer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2)
)
if mibBuilder.loadTexts:
    xgPeer.setRevisions(
        ("2015-10-08 08:35",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_XgPeerSerialNumber_Type = Integer32
_XgPeerSerialNumber_Object = MibScalar
xgPeerSerialNumber = _XgPeerSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 1),
    _XgPeerSerialNumber_Type()
)
xgPeerSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgPeerSerialNumber.setStatus("current")
_XgPeerSysName_Type = DisplayString
_XgPeerSysName_Object = MibScalar
xgPeerSysName = _XgPeerSysName_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 2),
    _XgPeerSysName_Type()
)
xgPeerSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgPeerSysName.setStatus("current")
_XgPeerIpAddrTable_Object = MibTable
xgPeerIpAddrTable = _XgPeerIpAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 3)
)
if mibBuilder.loadTexts:
    xgPeerIpAddrTable.setStatus("current")
_XgPeerIpAddrEntry_Object = MibTableRow
xgPeerIpAddrEntry = _XgPeerIpAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 3, 1)
)
xgPeerIpAddrEntry.setIndexNames(
    (0, "INFINET-XGPEER-MIB", "xgPeerIpAddress"),
)
if mibBuilder.loadTexts:
    xgPeerIpAddrEntry.setStatus("current")
_XgPeerIpAddress_Type = IpAddress
_XgPeerIpAddress_Object = MibTableColumn
xgPeerIpAddress = _XgPeerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 3, 1, 1),
    _XgPeerIpAddress_Type()
)
xgPeerIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xgPeerIpAddress.setStatus("current")
_XgPeerMIBConformance_ObjectIdentity = ObjectIdentity
xgPeerMIBConformance = _XgPeerMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 10)
)
_XgPeerMIBCompliances_ObjectIdentity = ObjectIdentity
xgPeerMIBCompliances = _XgPeerMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 10, 1)
)
_XgPeerMIBGroups_ObjectIdentity = ObjectIdentity
xgPeerMIBGroups = _XgPeerMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 10, 2)
)

# Managed Objects groups

xgPeerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 10, 2, 1)
)
xgPeerGroup.setObjects(
      *(("INFINET-XGPEER-MIB", "xgPeerSerialNumber"),
        ("INFINET-XGPEER-MIB", "xgPeerSysName"),
        ("INFINET-XGPEER-MIB", "xgPeerIpAddress"))
)
if mibBuilder.loadTexts:
    xgPeerGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

xgPeerMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 3942, 4, 1, 2, 10, 1, 1)
)
xgPeerMIBCompliance.setObjects(
    ("INFINET-XGPEER-MIB", "xgPeerGroup")
)
if mibBuilder.loadTexts:
    xgPeerMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINET-XGPEER-MIB",
    **{"xgPeer": xgPeer,
       "xgPeerSerialNumber": xgPeerSerialNumber,
       "xgPeerSysName": xgPeerSysName,
       "xgPeerIpAddrTable": xgPeerIpAddrTable,
       "xgPeerIpAddrEntry": xgPeerIpAddrEntry,
       "xgPeerIpAddress": xgPeerIpAddress,
       "xgPeerMIBConformance": xgPeerMIBConformance,
       "xgPeerMIBCompliances": xgPeerMIBCompliances,
       "xgPeerMIBCompliance": xgPeerMIBCompliance,
       "xgPeerMIBGroups": xgPeerMIBGroups,
       "xgPeerGroup": xgPeerGroup}
)
