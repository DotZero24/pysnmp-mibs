# SNMP MIB module (IPV6-LOOPBACK-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/quanta/IPV6-LOOPBACK-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:12:57 2025
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

(InetAddressPrefixLength,) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressPrefixLength")

(Ipv6AddressPrefix,) = mibBuilder.importSymbols(
    "IPV6-TC",
    "Ipv6AddressPrefix")

(agentLoopbackID,) = mibBuilder.importSymbols(
    "LOOPBACK-MIB",
    "agentLoopbackID")

(switch,) = mibBuilder.importSymbols(
    "QUANTA-SWITCH-MIB",
    "switch")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

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

ipv6Loopback = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 23)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentLoopbackIpv6Group_ObjectIdentity = ObjectIdentity
agentLoopbackIpv6Group = _AgentLoopbackIpv6Group_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7244, 2, 23, 1)
)
_AgentLoopbackIpv6PrefixTable_Object = MibTable
agentLoopbackIpv6PrefixTable = _AgentLoopbackIpv6PrefixTable_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1)
)
if mibBuilder.loadTexts:
    agentLoopbackIpv6PrefixTable.setStatus("current")
_AgentLoopbackIpv6PrefixEntry_Object = MibTableRow
agentLoopbackIpv6PrefixEntry = _AgentLoopbackIpv6PrefixEntry_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1)
)
agentLoopbackIpv6PrefixEntry.setIndexNames(
    (0, "LOOPBACK-MIB", "agentLoopbackID"),
    (0, "IPV6-LOOPBACK-MIB", "agentLoopbackIpv6PrefixPrefix"),
    (0, "IPV6-LOOPBACK-MIB", "agentLoopbackIpv6PrefixPrefixLen"),
)
if mibBuilder.loadTexts:
    agentLoopbackIpv6PrefixEntry.setStatus("current")
_AgentLoopbackIpv6PrefixPrefix_Type = Ipv6AddressPrefix
_AgentLoopbackIpv6PrefixPrefix_Object = MibTableColumn
agentLoopbackIpv6PrefixPrefix = _AgentLoopbackIpv6PrefixPrefix_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1, 1),
    _AgentLoopbackIpv6PrefixPrefix_Type()
)
agentLoopbackIpv6PrefixPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLoopbackIpv6PrefixPrefix.setStatus("current")


class _AgentLoopbackIpv6PrefixPrefixLen_Type(InetAddressPrefixLength):
    """Custom type agentLoopbackIpv6PrefixPrefixLen based on InetAddressPrefixLength"""
    defaultValue = 0


_AgentLoopbackIpv6PrefixPrefixLen_Type.__name__ = "InetAddressPrefixLength"
_AgentLoopbackIpv6PrefixPrefixLen_Object = MibTableColumn
agentLoopbackIpv6PrefixPrefixLen = _AgentLoopbackIpv6PrefixPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1, 2),
    _AgentLoopbackIpv6PrefixPrefixLen_Type()
)
agentLoopbackIpv6PrefixPrefixLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentLoopbackIpv6PrefixPrefixLen.setStatus("current")
_AgentLoopbackIpv6PrefixStatus_Type = RowStatus
_AgentLoopbackIpv6PrefixStatus_Object = MibTableColumn
agentLoopbackIpv6PrefixStatus = _AgentLoopbackIpv6PrefixStatus_Object(
    (1, 3, 6, 1, 4, 1, 7244, 2, 23, 1, 1, 1, 3),
    _AgentLoopbackIpv6PrefixStatus_Type()
)
agentLoopbackIpv6PrefixStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentLoopbackIpv6PrefixStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPV6-LOOPBACK-MIB",
    **{"ipv6Loopback": ipv6Loopback,
       "agentLoopbackIpv6Group": agentLoopbackIpv6Group,
       "agentLoopbackIpv6PrefixTable": agentLoopbackIpv6PrefixTable,
       "agentLoopbackIpv6PrefixEntry": agentLoopbackIpv6PrefixEntry,
       "agentLoopbackIpv6PrefixPrefix": agentLoopbackIpv6PrefixPrefix,
       "agentLoopbackIpv6PrefixPrefixLen": agentLoopbackIpv6PrefixPrefixLen,
       "agentLoopbackIpv6PrefixStatus": agentLoopbackIpv6PrefixStatus}
)
