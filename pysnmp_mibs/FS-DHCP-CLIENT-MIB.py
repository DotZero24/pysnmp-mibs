# SNMP MIB module (FS-DHCP-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-DHCP-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:44 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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

fsDhcpClientMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135)
)
if mibBuilder.loadTexts:
    fsDhcpClientMIB.setRevisions(
        ("2015-02-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDhcpClientMIBObjects_ObjectIdentity = ObjectIdentity
fsDhcpClientMIBObjects = _FsDhcpClientMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0)
)
_FsDhcpClientConfig_ObjectIdentity = ObjectIdentity
fsDhcpClientConfig = _FsDhcpClientConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0, 1)
)
_FsDhcpClientIntfTable_Object = MibTable
fsDhcpClientIntfTable = _FsDhcpClientIntfTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0, 1, 2)
)
if mibBuilder.loadTexts:
    fsDhcpClientIntfTable.setStatus("current")
_FsDhcpClientIntfEntry_Object = MibTableRow
fsDhcpClientIntfEntry = _FsDhcpClientIntfEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0, 1, 2, 1)
)
fsDhcpClientIntfEntry.setIndexNames(
    (0, "FS-DHCP-CLIENT-MIB", "fsDhcpIntfClientIndex"),
)
if mibBuilder.loadTexts:
    fsDhcpClientIntfEntry.setStatus("current")
_FsDhcpIntfClientIndex_Type = InterfaceIndex
_FsDhcpIntfClientIndex_Object = MibTableColumn
fsDhcpIntfClientIndex = _FsDhcpIntfClientIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0, 1, 2, 1, 1),
    _FsDhcpIntfClientIndex_Type()
)
fsDhcpIntfClientIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDhcpIntfClientIndex.setStatus("current")


class _FsDhcpClientIpAddrDhcpStatus_Type(Integer32):
    """Custom type fsDhcpClientIpAddrDhcpStatus based on Integer32"""
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


_FsDhcpClientIpAddrDhcpStatus_Type.__name__ = "Integer32"
_FsDhcpClientIpAddrDhcpStatus_Object = MibTableColumn
fsDhcpClientIpAddrDhcpStatus = _FsDhcpClientIpAddrDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 0, 1, 2, 1, 2),
    _FsDhcpClientIpAddrDhcpStatus_Type()
)
fsDhcpClientIpAddrDhcpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsDhcpClientIpAddrDhcpStatus.setStatus("current")
_FsDhcpClientMIBConformance_ObjectIdentity = ObjectIdentity
fsDhcpClientMIBConformance = _FsDhcpClientMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 2)
)
_FsDhcpClientMIBCompliances_ObjectIdentity = ObjectIdentity
fsDhcpClientMIBCompliances = _FsDhcpClientMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 2, 1)
)
_FsDhcpClientMIBGroups_ObjectIdentity = ObjectIdentity
fsDhcpClientMIBGroups = _FsDhcpClientMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 2, 2)
)

# Managed Objects groups

fsDhcpClientIntfConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 2, 2, 1)
)
fsDhcpClientIntfConfigGroup.setObjects(
    ("FS-DHCP-CLIENT-MIB", "fsDhcpClientIpAddrDhcpStatus")
)
if mibBuilder.loadTexts:
    fsDhcpClientIntfConfigGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsDhcpClientMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 135, 2, 1, 1)
)
fsDhcpClientMIBCompliance.setObjects(
    ("FS-DHCP-CLIENT-MIB", "fsDhcpClientIntfConfigGroup")
)
if mibBuilder.loadTexts:
    fsDhcpClientMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-DHCP-CLIENT-MIB",
    **{"fsDhcpClientMIB": fsDhcpClientMIB,
       "fsDhcpClientMIBObjects": fsDhcpClientMIBObjects,
       "fsDhcpClientConfig": fsDhcpClientConfig,
       "fsDhcpClientIntfTable": fsDhcpClientIntfTable,
       "fsDhcpClientIntfEntry": fsDhcpClientIntfEntry,
       "fsDhcpIntfClientIndex": fsDhcpIntfClientIndex,
       "fsDhcpClientIpAddrDhcpStatus": fsDhcpClientIpAddrDhcpStatus,
       "fsDhcpClientMIBConformance": fsDhcpClientMIBConformance,
       "fsDhcpClientMIBCompliances": fsDhcpClientMIBCompliances,
       "fsDhcpClientMIBCompliance": fsDhcpClientMIBCompliance,
       "fsDhcpClientMIBGroups": fsDhcpClientMIBGroups,
       "fsDhcpClientIntfConfigGroup": fsDhcpClientIntfConfigGroup}
)
