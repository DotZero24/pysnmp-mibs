# SNMP MIB module (NETGEAR-MRP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/netgear/NETGEAR-MRP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:28:06 2025
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

(ng7000managedswitch,) = mibBuilder.importSymbols(
    "NETGEAR-REF-MIB",
    "ng7000managedswitch")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeInterval,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeInterval",
    "TruthValue")


# MODULE-IDENTITY

fastPathMRP = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60)
)
if mibBuilder.loadTexts:
    fastPathMRP.setRevisions(
        ("2011-04-29 00:00",
         "2011-01-26 00:00",
         "2010-10-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentDot1qMrp_ObjectIdentity = ObjectIdentity
agentDot1qMrp = _AgentDot1qMrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 1)
)
_AgentDot1qPortMrpTable_Object = MibTable
agentDot1qPortMrpTable = _AgentDot1qPortMrpTable_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1)
)
if mibBuilder.loadTexts:
    agentDot1qPortMrpTable.setStatus("current")
_AgentDot1qPortMrpEntry_Object = MibTableRow
agentDot1qPortMrpEntry = _AgentDot1qPortMrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1, 1)
)
agentDot1qPortMrpEntry.setIndexNames(
    (0, "NETGEAR-MRP-MIB", "agentDot1qMrpPort"),
)
if mibBuilder.loadTexts:
    agentDot1qPortMrpEntry.setStatus("current")


class _AgentDot1qMrpPort_Type(Unsigned32):
    """Custom type agentDot1qMrpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentDot1qMrpPort_Type.__name__ = "Unsigned32"
_AgentDot1qMrpPort_Object = MibTableColumn
agentDot1qMrpPort = _AgentDot1qMrpPort_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1, 1, 1),
    _AgentDot1qMrpPort_Type()
)
agentDot1qMrpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentDot1qMrpPort.setStatus("current")


class _AgentDot1qPortMrpJoinTime_Type(TimeInterval):
    """Custom type agentDot1qPortMrpJoinTime based on TimeInterval"""
    defaultValue = 20


_AgentDot1qPortMrpJoinTime_Type.__name__ = "TimeInterval"
_AgentDot1qPortMrpJoinTime_Object = MibTableColumn
agentDot1qPortMrpJoinTime = _AgentDot1qPortMrpJoinTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1, 1, 2),
    _AgentDot1qPortMrpJoinTime_Type()
)
agentDot1qPortMrpJoinTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1qPortMrpJoinTime.setStatus("current")


class _AgentDot1qPortMrpLeaveTime_Type(TimeInterval):
    """Custom type agentDot1qPortMrpLeaveTime based on TimeInterval"""
    defaultValue = 60


_AgentDot1qPortMrpLeaveTime_Type.__name__ = "TimeInterval"
_AgentDot1qPortMrpLeaveTime_Object = MibTableColumn
agentDot1qPortMrpLeaveTime = _AgentDot1qPortMrpLeaveTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1, 1, 3),
    _AgentDot1qPortMrpLeaveTime_Type()
)
agentDot1qPortMrpLeaveTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1qPortMrpLeaveTime.setStatus("current")


class _AgentDot1qPortMrpLeaveAllTime_Type(TimeInterval):
    """Custom type agentDot1qPortMrpLeaveAllTime based on TimeInterval"""
    defaultValue = 1000


_AgentDot1qPortMrpLeaveAllTime_Type.__name__ = "TimeInterval"
_AgentDot1qPortMrpLeaveAllTime_Object = MibTableColumn
agentDot1qPortMrpLeaveAllTime = _AgentDot1qPortMrpLeaveAllTime_Object(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 1, 1, 1, 4),
    _AgentDot1qPortMrpLeaveAllTime_Type()
)
agentDot1qPortMrpLeaveAllTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentDot1qPortMrpLeaveAllTime.setStatus("current")
_AgentDot1qMrpMxrp_ObjectIdentity = ObjectIdentity
agentDot1qMrpMxrp = _AgentDot1qMrpMxrp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4526, 10, 60, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETGEAR-MRP-MIB",
    **{"fastPathMRP": fastPathMRP,
       "agentDot1qMrp": agentDot1qMrp,
       "agentDot1qPortMrpTable": agentDot1qPortMrpTable,
       "agentDot1qPortMrpEntry": agentDot1qPortMrpEntry,
       "agentDot1qMrpPort": agentDot1qMrpPort,
       "agentDot1qPortMrpJoinTime": agentDot1qPortMrpJoinTime,
       "agentDot1qPortMrpLeaveTime": agentDot1qPortMrpLeaveTime,
       "agentDot1qPortMrpLeaveAllTime": agentDot1qPortMrpLeaveAllTime,
       "agentDot1qMrpMxrp": agentDot1qMrpMxrp}
)
