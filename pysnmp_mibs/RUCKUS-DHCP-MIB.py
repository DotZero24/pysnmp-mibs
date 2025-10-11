# SNMP MIB module (RUCKUS-DHCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ruckus/RUCKUS-DHCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:13:37 2025
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

(ruckusCommonDHCPModule,) = mibBuilder.importSymbols(
    "RUCKUS-ROOT-MIB",
    "ruckusCommonDHCPModule")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

ruckusDHCPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RuckusDHCPObjects_ObjectIdentity = ObjectIdentity
ruckusDHCPObjects = _RuckusDHCPObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 1)
)
_RuckusDHCPClientInfo_ObjectIdentity = ObjectIdentity
ruckusDHCPClientInfo = _RuckusDHCPClientInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 1, 1)
)
_RuckusDHCPClientTable_Object = MibTable
ruckusDHCPClientTable = _RuckusDHCPClientTable_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    ruckusDHCPClientTable.setStatus("current")
_RuckusDHCPClientEntry_Object = MibTableRow
ruckusDHCPClientEntry = _RuckusDHCPClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 1, 1, 1, 1)
)
ruckusDHCPClientEntry.setIndexNames(
    (0, "RUCKUS-DHCP-MIB", "ruckusDHCPClientHWAddress"),
)
if mibBuilder.loadTexts:
    ruckusDHCPClientEntry.setStatus("current")
_RuckusDHCPClientHWAddress_Type = MacAddress
_RuckusDHCPClientHWAddress_Object = MibTableColumn
ruckusDHCPClientHWAddress = _RuckusDHCPClientHWAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 1, 1, 1, 1, 1),
    _RuckusDHCPClientHWAddress_Type()
)
ruckusDHCPClientHWAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ruckusDHCPClientHWAddress.setStatus("current")
_RuckusDHCPClientIPAddress_Type = IpAddress
_RuckusDHCPClientIPAddress_Object = MibTableColumn
ruckusDHCPClientIPAddress = _RuckusDHCPClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 1, 1, 1, 1, 2),
    _RuckusDHCPClientIPAddress_Type()
)
ruckusDHCPClientIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDHCPClientIPAddress.setStatus("current")
_RuckusDHCPClientSubnetMask_Type = IpAddress
_RuckusDHCPClientSubnetMask_Object = MibTableColumn
ruckusDHCPClientSubnetMask = _RuckusDHCPClientSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 1, 1, 1, 1, 3),
    _RuckusDHCPClientSubnetMask_Type()
)
ruckusDHCPClientSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDHCPClientSubnetMask.setStatus("current")
_RuckusDHCPClientLeaseTime_Type = Unsigned32
_RuckusDHCPClientLeaseTime_Object = MibTableColumn
ruckusDHCPClientLeaseTime = _RuckusDHCPClientLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 1, 1, 1, 1, 4),
    _RuckusDHCPClientLeaseTime_Type()
)
ruckusDHCPClientLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ruckusDHCPClientLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    ruckusDHCPClientLeaseTime.setUnits("seconds")
_RuckusDHCPClientExternal_ObjectIdentity = ObjectIdentity
ruckusDHCPClientExternal = _RuckusDHCPClientExternal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 1, 2)
)


class _RuckusDHCPClientExternalRenew_Type(TruthValue):
    """Custom type ruckusDHCPClientExternalRenew based on TruthValue"""
    defaultValue = 1


_RuckusDHCPClientExternalRenew_Type.__name__ = "TruthValue"
_RuckusDHCPClientExternalRenew_Object = MibScalar
ruckusDHCPClientExternalRenew = _RuckusDHCPClientExternalRenew_Object(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 1, 2, 1),
    _RuckusDHCPClientExternalRenew_Type()
)
ruckusDHCPClientExternalRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ruckusDHCPClientExternalRenew.setStatus("current")
_RuckusDHCPClientEvents_ObjectIdentity = ObjectIdentity
ruckusDHCPClientEvents = _RuckusDHCPClientEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 25053, 1, 1, 7, 1, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUCKUS-DHCP-MIB",
    **{"ruckusDHCPMIB": ruckusDHCPMIB,
       "ruckusDHCPObjects": ruckusDHCPObjects,
       "ruckusDHCPClientInfo": ruckusDHCPClientInfo,
       "ruckusDHCPClientTable": ruckusDHCPClientTable,
       "ruckusDHCPClientEntry": ruckusDHCPClientEntry,
       "ruckusDHCPClientHWAddress": ruckusDHCPClientHWAddress,
       "ruckusDHCPClientIPAddress": ruckusDHCPClientIPAddress,
       "ruckusDHCPClientSubnetMask": ruckusDHCPClientSubnetMask,
       "ruckusDHCPClientLeaseTime": ruckusDHCPClientLeaseTime,
       "ruckusDHCPClientExternal": ruckusDHCPClientExternal,
       "ruckusDHCPClientExternalRenew": ruckusDHCPClientExternalRenew,
       "ruckusDHCPClientEvents": ruckusDHCPClientEvents}
)
