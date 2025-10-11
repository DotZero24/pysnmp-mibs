# SNMP MIB module (SONICWALL-SMA-APPLIANCE-TUNNEL-SERVER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sonicwall/SONICWALL-SMA-APPLIANCE-TUNNEL-SERVER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:29 2025
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

(InternationalDisplayString,) = mibBuilder.importSymbols(
    "HOST-RESOURCES-MIB",
    "InternationalDisplayString")

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

(sonicwallSMAAppliance,) = mibBuilder.importSymbols(
    "SONICWALL-SMA-MIB",
    "sonicwallSMAAppliance")


# MODULE-IDENTITY

sonicwallTunnelServer = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TunnelServerState_Type = InternationalDisplayString
_TunnelServerState_Object = MibScalar
tunnelServerState = _TunnelServerState_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 1),
    _TunnelServerState_Type()
)
tunnelServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServerState.setStatus("current")
_NumOfTunnelServiceClientAddrPool_Type = Integer32
_NumOfTunnelServiceClientAddrPool_Object = MibScalar
numOfTunnelServiceClientAddrPool = _NumOfTunnelServiceClientAddrPool_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 2),
    _NumOfTunnelServiceClientAddrPool_Type()
)
numOfTunnelServiceClientAddrPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfTunnelServiceClientAddrPool.setStatus("current")
_TunnelServiceClientAddrPoolRangesTable_Object = MibTable
tunnelServiceClientAddrPoolRangesTable = _TunnelServiceClientAddrPoolRangesTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 3)
)
if mibBuilder.loadTexts:
    tunnelServiceClientAddrPoolRangesTable.setStatus("current")
_TunnelServiceClientAddrPoolEntry_Object = MibTableRow
tunnelServiceClientAddrPoolEntry = _TunnelServiceClientAddrPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 3, 1)
)
tunnelServiceClientAddrPoolEntry.setIndexNames(
    (0, "SONICWALL-SMA-APPLIANCE-TUNNEL-SERVER-MIB", "tunnelServiceClientAddrPoolId"),
)
if mibBuilder.loadTexts:
    tunnelServiceClientAddrPoolEntry.setStatus("current")
_TunnelServiceClientAddrPoolId_Type = Integer32
_TunnelServiceClientAddrPoolId_Object = MibTableColumn
tunnelServiceClientAddrPoolId = _TunnelServiceClientAddrPoolId_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 3, 1, 1),
    _TunnelServiceClientAddrPoolId_Type()
)
tunnelServiceClientAddrPoolId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServiceClientAddrPoolId.setStatus("current")
_TunnelServiceClientAddrPoolUtilization_Type = Integer32
_TunnelServiceClientAddrPoolUtilization_Object = MibTableColumn
tunnelServiceClientAddrPoolUtilization = _TunnelServiceClientAddrPoolUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 3, 1, 2),
    _TunnelServiceClientAddrPoolUtilization_Type()
)
tunnelServiceClientAddrPoolUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServiceClientAddrPoolUtilization.setStatus("current")
_TunnelServiceStartRangeOfClientAddrPool_Type = InternationalDisplayString
_TunnelServiceStartRangeOfClientAddrPool_Object = MibTableColumn
tunnelServiceStartRangeOfClientAddrPool = _TunnelServiceStartRangeOfClientAddrPool_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 3, 1, 3),
    _TunnelServiceStartRangeOfClientAddrPool_Type()
)
tunnelServiceStartRangeOfClientAddrPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServiceStartRangeOfClientAddrPool.setStatus("current")
_TunnelServiceEndRangeOfClientAddrPool_Type = InternationalDisplayString
_TunnelServiceEndRangeOfClientAddrPool_Object = MibTableColumn
tunnelServiceEndRangeOfClientAddrPool = _TunnelServiceEndRangeOfClientAddrPool_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 3, 1, 4),
    _TunnelServiceEndRangeOfClientAddrPool_Type()
)
tunnelServiceEndRangeOfClientAddrPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServiceEndRangeOfClientAddrPool.setStatus("current")
_NumberOfTunnelServiceSslTunnels_Type = Integer32
_NumberOfTunnelServiceSslTunnels_Object = MibScalar
numberOfTunnelServiceSslTunnels = _NumberOfTunnelServiceSslTunnels_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 4),
    _NumberOfTunnelServiceSslTunnels_Type()
)
numberOfTunnelServiceSslTunnels.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numberOfTunnelServiceSslTunnels.setStatus("current")
_TunnelServiceSslTunnelTable_Object = MibTable
tunnelServiceSslTunnelTable = _TunnelServiceSslTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 5)
)
if mibBuilder.loadTexts:
    tunnelServiceSslTunnelTable.setStatus("current")
_TunnelServiceSslTunnelEntry_Object = MibTableRow
tunnelServiceSslTunnelEntry = _TunnelServiceSslTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 5, 1)
)
tunnelServiceSslTunnelEntry.setIndexNames(
    (0, "SONICWALL-SMA-APPLIANCE-TUNNEL-SERVER-MIB", "tunnelServiceSslTunnelId"),
)
if mibBuilder.loadTexts:
    tunnelServiceSslTunnelEntry.setStatus("current")
_TunnelServiceSslTunnelId_Type = Integer32
_TunnelServiceSslTunnelId_Object = MibTableColumn
tunnelServiceSslTunnelId = _TunnelServiceSslTunnelId_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 5, 1, 1),
    _TunnelServiceSslTunnelId_Type()
)
tunnelServiceSslTunnelId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServiceSslTunnelId.setStatus("current")
_TunnelServiceSslTunnelUser_Type = InternationalDisplayString
_TunnelServiceSslTunnelUser_Object = MibTableColumn
tunnelServiceSslTunnelUser = _TunnelServiceSslTunnelUser_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 5, 1, 2),
    _TunnelServiceSslTunnelUser_Type()
)
tunnelServiceSslTunnelUser.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServiceSslTunnelUser.setStatus("current")
_TunnelServiceSslTunnelVIP_Type = InternationalDisplayString
_TunnelServiceSslTunnelVIP_Object = MibTableColumn
tunnelServiceSslTunnelVIP = _TunnelServiceSslTunnelVIP_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 5, 1, 3),
    _TunnelServiceSslTunnelVIP_Type()
)
tunnelServiceSslTunnelVIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServiceSslTunnelVIP.setStatus("current")
_NumOfTunnelServiceFlowsPerTunnel_Type = Integer32
_NumOfTunnelServiceFlowsPerTunnel_Object = MibTableColumn
numOfTunnelServiceFlowsPerTunnel = _NumOfTunnelServiceFlowsPerTunnel_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 5, 1, 4),
    _NumOfTunnelServiceFlowsPerTunnel_Type()
)
numOfTunnelServiceFlowsPerTunnel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    numOfTunnelServiceFlowsPerTunnel.setStatus("current")
_TunnelServiceSslTunnelUpTime_Type = Integer32
_TunnelServiceSslTunnelUpTime_Object = MibTableColumn
tunnelServiceSslTunnelUpTime = _TunnelServiceSslTunnelUpTime_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 5, 1, 5),
    _TunnelServiceSslTunnelUpTime_Type()
)
tunnelServiceSslTunnelUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tunnelServiceSslTunnelUpTime.setStatus("current")

# Managed Objects groups


# Notification objects

tunnelServiceclientAddrPoolUtilizationWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 100)
)
if mibBuilder.loadTexts:
    tunnelServiceclientAddrPoolUtilizationWarning.setStatus(
        "current"
    )

tunnelServerStateChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 5, 101)
)
if mibBuilder.loadTexts:
    tunnelServerStateChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-SMA-APPLIANCE-TUNNEL-SERVER-MIB",
    **{"sonicwallTunnelServer": sonicwallTunnelServer,
       "tunnelServerState": tunnelServerState,
       "numOfTunnelServiceClientAddrPool": numOfTunnelServiceClientAddrPool,
       "tunnelServiceClientAddrPoolRangesTable": tunnelServiceClientAddrPoolRangesTable,
       "tunnelServiceClientAddrPoolEntry": tunnelServiceClientAddrPoolEntry,
       "tunnelServiceClientAddrPoolId": tunnelServiceClientAddrPoolId,
       "tunnelServiceClientAddrPoolUtilization": tunnelServiceClientAddrPoolUtilization,
       "tunnelServiceStartRangeOfClientAddrPool": tunnelServiceStartRangeOfClientAddrPool,
       "tunnelServiceEndRangeOfClientAddrPool": tunnelServiceEndRangeOfClientAddrPool,
       "numberOfTunnelServiceSslTunnels": numberOfTunnelServiceSslTunnels,
       "tunnelServiceSslTunnelTable": tunnelServiceSslTunnelTable,
       "tunnelServiceSslTunnelEntry": tunnelServiceSslTunnelEntry,
       "tunnelServiceSslTunnelId": tunnelServiceSslTunnelId,
       "tunnelServiceSslTunnelUser": tunnelServiceSslTunnelUser,
       "tunnelServiceSslTunnelVIP": tunnelServiceSslTunnelVIP,
       "numOfTunnelServiceFlowsPerTunnel": numOfTunnelServiceFlowsPerTunnel,
       "tunnelServiceSslTunnelUpTime": tunnelServiceSslTunnelUpTime,
       "tunnelServiceclientAddrPoolUtilizationWarning": tunnelServiceclientAddrPoolUtilizationWarning,
       "tunnelServerStateChange": tunnelServerStateChange}
)
