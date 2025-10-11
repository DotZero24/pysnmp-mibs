# SNMP MIB module (QTECH-DHCP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-DHCP-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:58:43 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

qtechDhcpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135)
)
if mibBuilder.loadTexts:
    qtechDhcpClientMIB.setRevisions(
        ("2015-02-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechDhcpClientMIBObjects_ObjectIdentity = ObjectIdentity
qtechDhcpClientMIBObjects = _QtechDhcpClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0)
)
_QtechDhcpClientConfig_ObjectIdentity = ObjectIdentity
qtechDhcpClientConfig = _QtechDhcpClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0, 1)
)
_QtechDhcpClientIntfTable_Object = MibTable
qtechDhcpClientIntfTable = _QtechDhcpClientIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0, 1, 2)
)
if mibBuilder.loadTexts:
    qtechDhcpClientIntfTable.setStatus("current")
_QtechDhcpClientIntfEntry_Object = MibTableRow
qtechDhcpClientIntfEntry = _QtechDhcpClientIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0, 1, 2, 1)
)
qtechDhcpClientIntfEntry.setIndexNames(
    (0, "QTECH-DHCP-CLIENT-MIB", "qtechDhcpIntfClientIndex"),
)
if mibBuilder.loadTexts:
    qtechDhcpClientIntfEntry.setStatus("current")
_QtechDhcpIntfClientIndex_Type = InterfaceIndex
_QtechDhcpIntfClientIndex_Object = MibTableColumn
qtechDhcpIntfClientIndex = _QtechDhcpIntfClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0, 1, 2, 1, 1),
    _QtechDhcpIntfClientIndex_Type()
)
qtechDhcpIntfClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDhcpIntfClientIndex.setStatus("current")


class _QtechDhcpClientIpAddrDhcpStatus_Type(Integer32):
    """Custom type qtechDhcpClientIpAddrDhcpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_QtechDhcpClientIpAddrDhcpStatus_Type.__name__ = "Integer32"
_QtechDhcpClientIpAddrDhcpStatus_Object = MibTableColumn
qtechDhcpClientIpAddrDhcpStatus = _QtechDhcpClientIpAddrDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 0, 1, 2, 1, 2),
    _QtechDhcpClientIpAddrDhcpStatus_Type()
)
qtechDhcpClientIpAddrDhcpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechDhcpClientIpAddrDhcpStatus.setStatus("current")
_QtechDhcpClientMIBConformance_ObjectIdentity = ObjectIdentity
qtechDhcpClientMIBConformance = _QtechDhcpClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 2)
)
_QtechDhcpClientMIBCompliances_ObjectIdentity = ObjectIdentity
qtechDhcpClientMIBCompliances = _QtechDhcpClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 2, 1)
)
_QtechDhcpClientMIBGroups_ObjectIdentity = ObjectIdentity
qtechDhcpClientMIBGroups = _QtechDhcpClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 2, 2)
)

# Managed Objects groups

qtechDhcpClientIntfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 2, 2, 1)
)
qtechDhcpClientIntfConfigGroup.setObjects(
    ("QTECH-DHCP-CLIENT-MIB", "qtechDhcpClientIpAddrDhcpStatus")
)
if mibBuilder.loadTexts:
    qtechDhcpClientIntfConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechDhcpClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 135, 2, 1, 1)
)
qtechDhcpClientMIBCompliance.setObjects(
    ("QTECH-DHCP-CLIENT-MIB", "qtechDhcpClientIntfConfigGroup")
)
if mibBuilder.loadTexts:
    qtechDhcpClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-DHCP-CLIENT-MIB",
    **{"qtechDhcpClientMIB": qtechDhcpClientMIB,
       "qtechDhcpClientMIBObjects": qtechDhcpClientMIBObjects,
       "qtechDhcpClientConfig": qtechDhcpClientConfig,
       "qtechDhcpClientIntfTable": qtechDhcpClientIntfTable,
       "qtechDhcpClientIntfEntry": qtechDhcpClientIntfEntry,
       "qtechDhcpIntfClientIndex": qtechDhcpIntfClientIndex,
       "qtechDhcpClientIpAddrDhcpStatus": qtechDhcpClientIpAddrDhcpStatus,
       "qtechDhcpClientMIBConformance": qtechDhcpClientMIBConformance,
       "qtechDhcpClientMIBCompliances": qtechDhcpClientMIBCompliances,
       "qtechDhcpClientMIBCompliance": qtechDhcpClientMIBCompliance,
       "qtechDhcpClientMIBGroups": qtechDhcpClientMIBGroups,
       "qtechDhcpClientIntfConfigGroup": qtechDhcpClientIntfConfigGroup}
)
