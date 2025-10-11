# SNMP MIB module (SONICWALL-SMA-APPLIANCE-SYSTEM-HEALTH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sonicwall/SONICWALL-SMA-APPLIANCE-SYSTEM-HEALTH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:35 2025
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
 enterprises,
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
    "enterprises",
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

sonicwallSystemHealth = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AuthenticatedUsers_ObjectIdentity = ObjectIdentity
authenticatedUsers = _AuthenticatedUsers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 1)
)
_CurrentlyLoggedIn_Type = Integer32
_CurrentlyLoggedIn_Object = MibScalar
currentlyLoggedIn = _CurrentlyLoggedIn_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 1, 1),
    _CurrentlyLoggedIn_Type()
)
currentlyLoggedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentlyLoggedIn.setStatus("current")
_PeakLoggedIn_Type = Integer32
_PeakLoggedIn_Object = MibScalar
peakLoggedIn = _PeakLoggedIn_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 1, 2),
    _PeakLoggedIn_Type()
)
peakLoggedIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakLoggedIn.setStatus("current")
_MaximumlicensedUsers_Type = Integer32
_MaximumlicensedUsers_Object = MibScalar
maximumlicensedUsers = _MaximumlicensedUsers_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 1, 3),
    _MaximumlicensedUsers_Type()
)
maximumlicensedUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maximumlicensedUsers.setStatus("current")
_ConnectionUtilization_ObjectIdentity = ObjectIdentity
connectionUtilization = _ConnectionUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 2)
)
_CurrentConnections_Type = Integer32
_CurrentConnections_Object = MibScalar
currentConnections = _CurrentConnections_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 2, 1),
    _CurrentConnections_Type()
)
currentConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currentConnections.setStatus("current")
_PeakConnections_Type = Integer32
_PeakConnections_Object = MibScalar
peakConnections = _PeakConnections_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 2, 2),
    _PeakConnections_Type()
)
peakConnections.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    peakConnections.setStatus("current")
_CpuUtilization_Type = Integer32
_CpuUtilization_Object = MibScalar
cpuUtilization = _CpuUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 3),
    _CpuUtilization_Type()
)
cpuUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuUtilization.setStatus("current")
_MemoryTotalUtilization_ObjectIdentity = ObjectIdentity
memoryTotalUtilization = _MemoryTotalUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 4)
)
_RamUtilization_Type = Integer32
_RamUtilization_Object = MibScalar
ramUtilization = _RamUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 4, 1),
    _RamUtilization_Type()
)
ramUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ramUtilization.setStatus("current")
_SwapUtilization_Type = Integer32
_SwapUtilization_Object = MibScalar
swapUtilization = _SwapUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 4, 2),
    _SwapUtilization_Type()
)
swapUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swapUtilization.setStatus("current")
_BandwidthUtilization_ObjectIdentity = ObjectIdentity
bandwidthUtilization = _BandwidthUtilization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 5)
)
_InternalInterfaceCurrentThroughput_Type = Integer32
_InternalInterfaceCurrentThroughput_Object = MibScalar
internalInterfaceCurrentThroughput = _InternalInterfaceCurrentThroughput_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 5, 1),
    _InternalInterfaceCurrentThroughput_Type()
)
internalInterfaceCurrentThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalInterfaceCurrentThroughput.setStatus("current")
_InternalInterfacePeakThroughput_Type = Integer32
_InternalInterfacePeakThroughput_Object = MibScalar
internalInterfacePeakThroughput = _InternalInterfacePeakThroughput_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 5, 2),
    _InternalInterfacePeakThroughput_Type()
)
internalInterfacePeakThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    internalInterfacePeakThroughput.setStatus("current")
_ExternalInterfaceCurrentThroughput_Type = Integer32
_ExternalInterfaceCurrentThroughput_Object = MibScalar
externalInterfaceCurrentThroughput = _ExternalInterfaceCurrentThroughput_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 5, 3),
    _ExternalInterfaceCurrentThroughput_Type()
)
externalInterfaceCurrentThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalInterfaceCurrentThroughput.setStatus("current")
_ExternalInterfacePeakThroughput_Type = Integer32
_ExternalInterfacePeakThroughput_Object = MibScalar
externalInterfacePeakThroughput = _ExternalInterfacePeakThroughput_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 5, 4),
    _ExternalInterfacePeakThroughput_Type()
)
externalInterfacePeakThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    externalInterfacePeakThroughput.setStatus("current")
_ClusterlInterfaceCurrentThroughput_Type = Integer32
_ClusterlInterfaceCurrentThroughput_Object = MibScalar
clusterlInterfaceCurrentThroughput = _ClusterlInterfaceCurrentThroughput_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 5, 5),
    _ClusterlInterfaceCurrentThroughput_Type()
)
clusterlInterfaceCurrentThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterlInterfaceCurrentThroughput.setStatus("current")
_ClusterInterfacePeakThroughput_Type = Integer32
_ClusterInterfacePeakThroughput_Object = MibScalar
clusterInterfacePeakThroughput = _ClusterInterfacePeakThroughput_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 5, 6),
    _ClusterInterfacePeakThroughput_Type()
)
clusterInterfacePeakThroughput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterInterfacePeakThroughput.setStatus("current")
_LogUtilization_Type = Integer32
_LogUtilization_Object = MibScalar
logUtilization = _LogUtilization_Object(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 9),
    _LogUtilization_Type()
)
logUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    logUtilization.setStatus("current")

# Managed Objects groups


# Notification objects

cpuCapacityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 6)
)
cpuCapacityWarning.setObjects(
    ("SONICWALL-SMA-APPLIANCE-SYSTEM-HEALTH-MIB", "cpuUtilization")
)
if mibBuilder.loadTexts:
    cpuCapacityWarning.setStatus(
        "current"
    )

memoryCapacityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 7)
)
memoryCapacityWarning.setObjects(
    ("SONICWALL-SMA-APPLIANCE-SYSTEM-HEALTH-MIB", "ramUtilization")
)
if mibBuilder.loadTexts:
    memoryCapacityWarning.setStatus(
        "current"
    )

userLimitWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 8)
)
userLimitWarning.setObjects(
    ("SONICWALL-SMA-APPLIANCE-SYSTEM-HEALTH-MIB", "currentlyLoggedIn")
)
if mibBuilder.loadTexts:
    userLimitWarning.setStatus(
        "current"
    )

logCapacityWarning = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 100)
)
logCapacityWarning.setObjects(
    ("SONICWALL-SMA-APPLIANCE-SYSTEM-HEALTH-MIB", "logUtilization")
)
if mibBuilder.loadTexts:
    logCapacityWarning.setStatus(
        "current"
    )

userLimitReached = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 102)
)
userLimitReached.setObjects(
    ("SONICWALL-SMA-APPLIANCE-SYSTEM-HEALTH-MIB", "currentlyLoggedIn")
)
if mibBuilder.loadTexts:
    userLimitReached.setStatus(
        "current"
    )

userLimitExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 8741, 8, 1, 2, 103)
)
userLimitExceeded.setObjects(
    ("SONICWALL-SMA-APPLIANCE-SYSTEM-HEALTH-MIB", "currentlyLoggedIn")
)
if mibBuilder.loadTexts:
    userLimitExceeded.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-SMA-APPLIANCE-SYSTEM-HEALTH-MIB",
    **{"sonicwallSystemHealth": sonicwallSystemHealth,
       "authenticatedUsers": authenticatedUsers,
       "currentlyLoggedIn": currentlyLoggedIn,
       "peakLoggedIn": peakLoggedIn,
       "maximumlicensedUsers": maximumlicensedUsers,
       "connectionUtilization": connectionUtilization,
       "currentConnections": currentConnections,
       "peakConnections": peakConnections,
       "cpuUtilization": cpuUtilization,
       "memoryTotalUtilization": memoryTotalUtilization,
       "ramUtilization": ramUtilization,
       "swapUtilization": swapUtilization,
       "bandwidthUtilization": bandwidthUtilization,
       "internalInterfaceCurrentThroughput": internalInterfaceCurrentThroughput,
       "internalInterfacePeakThroughput": internalInterfacePeakThroughput,
       "externalInterfaceCurrentThroughput": externalInterfaceCurrentThroughput,
       "externalInterfacePeakThroughput": externalInterfacePeakThroughput,
       "clusterlInterfaceCurrentThroughput": clusterlInterfaceCurrentThroughput,
       "clusterInterfacePeakThroughput": clusterInterfacePeakThroughput,
       "cpuCapacityWarning": cpuCapacityWarning,
       "memoryCapacityWarning": memoryCapacityWarning,
       "userLimitWarning": userLimitWarning,
       "logUtilization": logUtilization,
       "logCapacityWarning": logCapacityWarning,
       "userLimitReached": userLimitReached,
       "userLimitExceeded": userLimitExceeded}
)
