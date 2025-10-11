# SNMP MIB module (ENTERASYS-RADIUS-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/enterasys/ENTERASYS-RADIUS-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:47:05 2025
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

(etsysModules,) = mibBuilder.importSymbols(
    "ENTERASYS-MIB-NAMES",
    "etsysModules")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

etsysRadiusSnoopingMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62)
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingMIB.setRevisions(
        ("2012-07-16 13:13",
         "2009-11-04 19:13",
         "2008-02-05 16:51")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EtsysRadiusSnoopingObjectBase_ObjectIdentity = ObjectIdentity
etsysRadiusSnoopingObjectBase = _EtsysRadiusSnoopingObjectBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2)
)
_EtsysRadiusSnoopingObjects_ObjectIdentity = ObjectIdentity
etsysRadiusSnoopingObjects = _EtsysRadiusSnoopingObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1)
)
_EtsysRadiusSnoopingSystem_ObjectIdentity = ObjectIdentity
etsysRadiusSnoopingSystem = _EtsysRadiusSnoopingSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 1)
)


class _EtsysRadiusSnoopingSystemEnable_Type(EnabledStatus):
    """Custom type etsysRadiusSnoopingSystemEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysRadiusSnoopingSystemEnable_Type.__name__ = "EnabledStatus"
_EtsysRadiusSnoopingSystemEnable_Object = MibScalar
etsysRadiusSnoopingSystemEnable = _EtsysRadiusSnoopingSystemEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 1, 1),
    _EtsysRadiusSnoopingSystemEnable_Type()
)
etsysRadiusSnoopingSystemEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSystemEnable.setStatus("current")


class _EtsysRadiusSnoopingSystemTimeout_Type(Integer32):
    """Custom type etsysRadiusSnoopingSystemTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_EtsysRadiusSnoopingSystemTimeout_Type.__name__ = "Integer32"
_EtsysRadiusSnoopingSystemTimeout_Object = MibScalar
etsysRadiusSnoopingSystemTimeout = _EtsysRadiusSnoopingSystemTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 1, 2),
    _EtsysRadiusSnoopingSystemTimeout_Type()
)
etsysRadiusSnoopingSystemTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSystemTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSystemTimeout.setUnits("seconds")
_EtsysRadiusSnoopingSystemConfiguredFlows_Type = Counter32
_EtsysRadiusSnoopingSystemConfiguredFlows_Object = MibScalar
etsysRadiusSnoopingSystemConfiguredFlows = _EtsysRadiusSnoopingSystemConfiguredFlows_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 1, 3),
    _EtsysRadiusSnoopingSystemConfiguredFlows_Type()
)
etsysRadiusSnoopingSystemConfiguredFlows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSystemConfiguredFlows.setStatus("current")
_EtsysRadiusSnoopingSystemActiveSessions_Type = Counter32
_EtsysRadiusSnoopingSystemActiveSessions_Object = MibScalar
etsysRadiusSnoopingSystemActiveSessions = _EtsysRadiusSnoopingSystemActiveSessions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 1, 4),
    _EtsysRadiusSnoopingSystemActiveSessions_Type()
)
etsysRadiusSnoopingSystemActiveSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSystemActiveSessions.setStatus("current")
_EtsysRadiusSnoopingPort_ObjectIdentity = ObjectIdentity
etsysRadiusSnoopingPort = _EtsysRadiusSnoopingPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 2)
)
_EtsysRadiusSnoopingPortTable_Object = MibTable
etsysRadiusSnoopingPortTable = _EtsysRadiusSnoopingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 2, 1)
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortTable.setStatus("current")
_EtsysRadiusSnoopingPortEntry_Object = MibTableRow
etsysRadiusSnoopingPortEntry = _EtsysRadiusSnoopingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 2, 1, 1)
)
etsysRadiusSnoopingPortEntry.setIndexNames(
    (0, "ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingPortIndex"),
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortEntry.setStatus("current")
_EtsysRadiusSnoopingPortIndex_Type = InterfaceIndex
_EtsysRadiusSnoopingPortIndex_Object = MibTableColumn
etsysRadiusSnoopingPortIndex = _EtsysRadiusSnoopingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 2, 1, 1, 1),
    _EtsysRadiusSnoopingPortIndex_Type()
)
etsysRadiusSnoopingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortIndex.setStatus("current")


class _EtsysRadiusSnoopingPortEnable_Type(EnabledStatus):
    """Custom type etsysRadiusSnoopingPortEnable based on EnabledStatus"""
    defaultValue = 2


_EtsysRadiusSnoopingPortEnable_Type.__name__ = "EnabledStatus"
_EtsysRadiusSnoopingPortEnable_Object = MibTableColumn
etsysRadiusSnoopingPortEnable = _EtsysRadiusSnoopingPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 2, 1, 1, 2),
    _EtsysRadiusSnoopingPortEnable_Type()
)
etsysRadiusSnoopingPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortEnable.setStatus("current")


class _EtsysRadiusSnoopingPortTimeout_Type(Integer32):
    """Custom type etsysRadiusSnoopingPortTimeout based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_EtsysRadiusSnoopingPortTimeout_Type.__name__ = "Integer32"
_EtsysRadiusSnoopingPortTimeout_Object = MibTableColumn
etsysRadiusSnoopingPortTimeout = _EtsysRadiusSnoopingPortTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 2, 1, 1, 3),
    _EtsysRadiusSnoopingPortTimeout_Type()
)
etsysRadiusSnoopingPortTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortTimeout.setStatus("current")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortTimeout.setUnits("seconds")
_EtsysRadiusSnoopingPortInitialize_Type = TruthValue
_EtsysRadiusSnoopingPortInitialize_Object = MibTableColumn
etsysRadiusSnoopingPortInitialize = _EtsysRadiusSnoopingPortInitialize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 2, 1, 1, 4),
    _EtsysRadiusSnoopingPortInitialize_Type()
)
etsysRadiusSnoopingPortInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortInitialize.setStatus("current")


class _EtsysRadiusSnoopingPortDrop_Type(EnabledStatus):
    """Custom type etsysRadiusSnoopingPortDrop based on EnabledStatus"""
    defaultValue = 1


_EtsysRadiusSnoopingPortDrop_Type.__name__ = "EnabledStatus"
_EtsysRadiusSnoopingPortDrop_Object = MibTableColumn
etsysRadiusSnoopingPortDrop = _EtsysRadiusSnoopingPortDrop_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 2, 1, 1, 5),
    _EtsysRadiusSnoopingPortDrop_Type()
)
etsysRadiusSnoopingPortDrop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortDrop.setStatus("current")
_EtsysRadiusSnoopingPortAuthenticationsAllocated_Type = Unsigned32
_EtsysRadiusSnoopingPortAuthenticationsAllocated_Object = MibTableColumn
etsysRadiusSnoopingPortAuthenticationsAllocated = _EtsysRadiusSnoopingPortAuthenticationsAllocated_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 2, 1, 1, 6),
    _EtsysRadiusSnoopingPortAuthenticationsAllocated_Type()
)
etsysRadiusSnoopingPortAuthenticationsAllocated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortAuthenticationsAllocated.setStatus("current")
_EtsysRadiusSnoopingPortAuthenticationsAllowed_Type = Unsigned32
_EtsysRadiusSnoopingPortAuthenticationsAllowed_Object = MibTableColumn
etsysRadiusSnoopingPortAuthenticationsAllowed = _EtsysRadiusSnoopingPortAuthenticationsAllowed_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 2, 1, 1, 7),
    _EtsysRadiusSnoopingPortAuthenticationsAllowed_Type()
)
etsysRadiusSnoopingPortAuthenticationsAllowed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortAuthenticationsAllowed.setStatus("current")
_EtsysRadiusSnoopingSession_ObjectIdentity = ObjectIdentity
etsysRadiusSnoopingSession = _EtsysRadiusSnoopingSession_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3)
)
_EtsysRadiusSnoopingSessionTable_Object = MibTable
etsysRadiusSnoopingSessionTable = _EtsysRadiusSnoopingSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3, 1)
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionTable.setStatus("current")
_EtsysRadiusSnoopingSessionEntry_Object = MibTableRow
etsysRadiusSnoopingSessionEntry = _EtsysRadiusSnoopingSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3, 1, 1)
)
etsysRadiusSnoopingSessionEntry.setIndexNames(
    (0, "ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSessionMACAddress"),
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionEntry.setStatus("current")
_EtsysRadiusSnoopingSessionMACAddress_Type = MacAddress
_EtsysRadiusSnoopingSessionMACAddress_Object = MibTableColumn
etsysRadiusSnoopingSessionMACAddress = _EtsysRadiusSnoopingSessionMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3, 1, 1, 1),
    _EtsysRadiusSnoopingSessionMACAddress_Type()
)
etsysRadiusSnoopingSessionMACAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionMACAddress.setStatus("current")
_EtsysRadiusSnoopingSessionInitialize_Type = TruthValue
_EtsysRadiusSnoopingSessionInitialize_Object = MibTableColumn
etsysRadiusSnoopingSessionInitialize = _EtsysRadiusSnoopingSessionInitialize_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3, 1, 1, 2),
    _EtsysRadiusSnoopingSessionInitialize_Type()
)
etsysRadiusSnoopingSessionInitialize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionInitialize.setStatus("current")
_EtsysRadiusSnoopingSessionPort_Type = InterfaceIndex
_EtsysRadiusSnoopingSessionPort_Object = MibTableColumn
etsysRadiusSnoopingSessionPort = _EtsysRadiusSnoopingSessionPort_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3, 1, 1, 3),
    _EtsysRadiusSnoopingSessionPort_Type()
)
etsysRadiusSnoopingSessionPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionPort.setStatus("current")
_EtsysRadiusSnoopingSessionRadiusClientAddressType_Type = InetAddressType
_EtsysRadiusSnoopingSessionRadiusClientAddressType_Object = MibTableColumn
etsysRadiusSnoopingSessionRadiusClientAddressType = _EtsysRadiusSnoopingSessionRadiusClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3, 1, 1, 5),
    _EtsysRadiusSnoopingSessionRadiusClientAddressType_Type()
)
etsysRadiusSnoopingSessionRadiusClientAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionRadiusClientAddressType.setStatus("current")
_EtsysRadiusSnoopingSessionRadiusClientAddress_Type = InetAddress
_EtsysRadiusSnoopingSessionRadiusClientAddress_Object = MibTableColumn
etsysRadiusSnoopingSessionRadiusClientAddress = _EtsysRadiusSnoopingSessionRadiusClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3, 1, 1, 6),
    _EtsysRadiusSnoopingSessionRadiusClientAddress_Type()
)
etsysRadiusSnoopingSessionRadiusClientAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionRadiusClientAddress.setStatus("current")
_EtsysRadiusSnoopingSessionRadiusServerAddressType_Type = InetAddressType
_EtsysRadiusSnoopingSessionRadiusServerAddressType_Object = MibTableColumn
etsysRadiusSnoopingSessionRadiusServerAddressType = _EtsysRadiusSnoopingSessionRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3, 1, 1, 7),
    _EtsysRadiusSnoopingSessionRadiusServerAddressType_Type()
)
etsysRadiusSnoopingSessionRadiusServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionRadiusServerAddressType.setStatus("current")
_EtsysRadiusSnoopingSessionRadiusServerAddress_Type = InetAddress
_EtsysRadiusSnoopingSessionRadiusServerAddress_Object = MibTableColumn
etsysRadiusSnoopingSessionRadiusServerAddress = _EtsysRadiusSnoopingSessionRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3, 1, 1, 8),
    _EtsysRadiusSnoopingSessionRadiusServerAddress_Type()
)
etsysRadiusSnoopingSessionRadiusServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionRadiusServerAddress.setStatus("current")
_EtsysRadiusSnoopingSessionDuration_Type = Unsigned32
_EtsysRadiusSnoopingSessionDuration_Object = MibTableColumn
etsysRadiusSnoopingSessionDuration = _EtsysRadiusSnoopingSessionDuration_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 3, 1, 1, 9),
    _EtsysRadiusSnoopingSessionDuration_Type()
)
etsysRadiusSnoopingSessionDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionDuration.setStatus("current")
_EtsysRadiusSnoopingFlow_ObjectIdentity = ObjectIdentity
etsysRadiusSnoopingFlow = _EtsysRadiusSnoopingFlow_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4)
)
_EtsysRadiusSnoopingFlowTable_Object = MibTable
etsysRadiusSnoopingFlowTable = _EtsysRadiusSnoopingFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1)
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowTable.setStatus("current")
_EtsysRadiusSnoopingFlowEntry_Object = MibTableRow
etsysRadiusSnoopingFlowEntry = _EtsysRadiusSnoopingFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1)
)
etsysRadiusSnoopingFlowEntry.setIndexNames(
    (0, "ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowIndex"),
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowEntry.setStatus("current")


class _EtsysRadiusSnoopingFlowIndex_Type(Integer32):
    """Custom type etsysRadiusSnoopingFlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_EtsysRadiusSnoopingFlowIndex_Type.__name__ = "Integer32"
_EtsysRadiusSnoopingFlowIndex_Object = MibTableColumn
etsysRadiusSnoopingFlowIndex = _EtsysRadiusSnoopingFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 1),
    _EtsysRadiusSnoopingFlowIndex_Type()
)
etsysRadiusSnoopingFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowIndex.setStatus("current")


class _EtsysRadiusSnoopingFlowClientAddressType_Type(InetAddressType):
    """Custom type etsysRadiusSnoopingFlowClientAddressType based on InetAddressType"""
    defaultValue = 1


_EtsysRadiusSnoopingFlowClientAddressType_Type.__name__ = "InetAddressType"
_EtsysRadiusSnoopingFlowClientAddressType_Object = MibTableColumn
etsysRadiusSnoopingFlowClientAddressType = _EtsysRadiusSnoopingFlowClientAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 2),
    _EtsysRadiusSnoopingFlowClientAddressType_Type()
)
etsysRadiusSnoopingFlowClientAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowClientAddressType.setStatus("current")


class _EtsysRadiusSnoopingFlowClientAddress_Type(InetAddress):
    """Custom type etsysRadiusSnoopingFlowClientAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysRadiusSnoopingFlowClientAddress_Type.__name__ = "InetAddress"
_EtsysRadiusSnoopingFlowClientAddress_Object = MibTableColumn
etsysRadiusSnoopingFlowClientAddress = _EtsysRadiusSnoopingFlowClientAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 3),
    _EtsysRadiusSnoopingFlowClientAddress_Type()
)
etsysRadiusSnoopingFlowClientAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowClientAddress.setStatus("current")


class _EtsysRadiusSnoopingFlowServerAddressType_Type(InetAddressType):
    """Custom type etsysRadiusSnoopingFlowServerAddressType based on InetAddressType"""
    defaultValue = 1


_EtsysRadiusSnoopingFlowServerAddressType_Type.__name__ = "InetAddressType"
_EtsysRadiusSnoopingFlowServerAddressType_Object = MibTableColumn
etsysRadiusSnoopingFlowServerAddressType = _EtsysRadiusSnoopingFlowServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 4),
    _EtsysRadiusSnoopingFlowServerAddressType_Type()
)
etsysRadiusSnoopingFlowServerAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowServerAddressType.setStatus("current")


class _EtsysRadiusSnoopingFlowServerAddress_Type(InetAddress):
    """Custom type etsysRadiusSnoopingFlowServerAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_EtsysRadiusSnoopingFlowServerAddress_Type.__name__ = "InetAddress"
_EtsysRadiusSnoopingFlowServerAddress_Object = MibTableColumn
etsysRadiusSnoopingFlowServerAddress = _EtsysRadiusSnoopingFlowServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 5),
    _EtsysRadiusSnoopingFlowServerAddress_Type()
)
etsysRadiusSnoopingFlowServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowServerAddress.setStatus("current")


class _EtsysRadiusSnoopingFlowServerPortNumber_Type(Integer32):
    """Custom type etsysRadiusSnoopingFlowServerPortNumber based on Integer32"""
    defaultValue = 1812

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_EtsysRadiusSnoopingFlowServerPortNumber_Type.__name__ = "Integer32"
_EtsysRadiusSnoopingFlowServerPortNumber_Object = MibTableColumn
etsysRadiusSnoopingFlowServerPortNumber = _EtsysRadiusSnoopingFlowServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 6),
    _EtsysRadiusSnoopingFlowServerPortNumber_Type()
)
etsysRadiusSnoopingFlowServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowServerPortNumber.setStatus("current")


class _EtsysRadiusSnoopingFlowSecret_Type(OctetString):
    """Custom type etsysRadiusSnoopingFlowSecret based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_EtsysRadiusSnoopingFlowSecret_Type.__name__ = "OctetString"
_EtsysRadiusSnoopingFlowSecret_Object = MibTableColumn
etsysRadiusSnoopingFlowSecret = _EtsysRadiusSnoopingFlowSecret_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 7),
    _EtsysRadiusSnoopingFlowSecret_Type()
)
etsysRadiusSnoopingFlowSecret.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowSecret.setStatus("current")
_EtsysRadiusSnoopingFlowRowStatus_Type = RowStatus
_EtsysRadiusSnoopingFlowRowStatus_Object = MibTableColumn
etsysRadiusSnoopingFlowRowStatus = _EtsysRadiusSnoopingFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 8),
    _EtsysRadiusSnoopingFlowRowStatus_Type()
)
etsysRadiusSnoopingFlowRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowRowStatus.setStatus("current")
_EtsysRadiusSnoopingFlowSecretEntered_Type = TruthValue
_EtsysRadiusSnoopingFlowSecretEntered_Object = MibTableColumn
etsysRadiusSnoopingFlowSecretEntered = _EtsysRadiusSnoopingFlowSecretEntered_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 9),
    _EtsysRadiusSnoopingFlowSecretEntered_Type()
)
etsysRadiusSnoopingFlowSecretEntered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowSecretEntered.setStatus("current")
_EtsysRadiusSnoopingFlowCurrentSessions_Type = Counter32
_EtsysRadiusSnoopingFlowCurrentSessions_Object = MibTableColumn
etsysRadiusSnoopingFlowCurrentSessions = _EtsysRadiusSnoopingFlowCurrentSessions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 10),
    _EtsysRadiusSnoopingFlowCurrentSessions_Type()
)
etsysRadiusSnoopingFlowCurrentSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowCurrentSessions.setStatus("current")
_EtsysRadiusSnoopingFlowPendingAuthentications_Type = Counter32
_EtsysRadiusSnoopingFlowPendingAuthentications_Object = MibTableColumn
etsysRadiusSnoopingFlowPendingAuthentications = _EtsysRadiusSnoopingFlowPendingAuthentications_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 11),
    _EtsysRadiusSnoopingFlowPendingAuthentications_Type()
)
etsysRadiusSnoopingFlowPendingAuthentications.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowPendingAuthentications.setStatus("current")
_EtsysRadiusSnoopingFlowTotalSessions_Type = Counter32
_EtsysRadiusSnoopingFlowTotalSessions_Object = MibTableColumn
etsysRadiusSnoopingFlowTotalSessions = _EtsysRadiusSnoopingFlowTotalSessions_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 12),
    _EtsysRadiusSnoopingFlowTotalSessions_Type()
)
etsysRadiusSnoopingFlowTotalSessions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowTotalSessions.setStatus("current")
_EtsysRadiusSnoopingFlowAccessRequests_Type = Counter32
_EtsysRadiusSnoopingFlowAccessRequests_Object = MibTableColumn
etsysRadiusSnoopingFlowAccessRequests = _EtsysRadiusSnoopingFlowAccessRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 13),
    _EtsysRadiusSnoopingFlowAccessRequests_Type()
)
etsysRadiusSnoopingFlowAccessRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowAccessRequests.setStatus("current")
_EtsysRadiusSnoopingFlowAccessAccepts_Type = Counter32
_EtsysRadiusSnoopingFlowAccessAccepts_Object = MibTableColumn
etsysRadiusSnoopingFlowAccessAccepts = _EtsysRadiusSnoopingFlowAccessAccepts_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 14),
    _EtsysRadiusSnoopingFlowAccessAccepts_Type()
)
etsysRadiusSnoopingFlowAccessAccepts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowAccessAccepts.setStatus("current")
_EtsysRadiusSnoopingFlowAccessRejects_Type = Counter32
_EtsysRadiusSnoopingFlowAccessRejects_Object = MibTableColumn
etsysRadiusSnoopingFlowAccessRejects = _EtsysRadiusSnoopingFlowAccessRejects_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 15),
    _EtsysRadiusSnoopingFlowAccessRejects_Type()
)
etsysRadiusSnoopingFlowAccessRejects.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowAccessRejects.setStatus("current")
_EtsysRadiusSnoopingFlowInvalidRequests_Type = Counter32
_EtsysRadiusSnoopingFlowInvalidRequests_Object = MibTableColumn
etsysRadiusSnoopingFlowInvalidRequests = _EtsysRadiusSnoopingFlowInvalidRequests_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 16),
    _EtsysRadiusSnoopingFlowInvalidRequests_Type()
)
etsysRadiusSnoopingFlowInvalidRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowInvalidRequests.setStatus("current")
_EtsysRadiusSnoopingFlowInvalidResponses_Type = Counter32
_EtsysRadiusSnoopingFlowInvalidResponses_Object = MibTableColumn
etsysRadiusSnoopingFlowInvalidResponses = _EtsysRadiusSnoopingFlowInvalidResponses_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 17),
    _EtsysRadiusSnoopingFlowInvalidResponses_Type()
)
etsysRadiusSnoopingFlowInvalidResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowInvalidResponses.setStatus("current")
_EtsysRadiusSnoopingFlowTotalDroppedPackets_Type = Counter32
_EtsysRadiusSnoopingFlowTotalDroppedPackets_Object = MibTableColumn
etsysRadiusSnoopingFlowTotalDroppedPackets = _EtsysRadiusSnoopingFlowTotalDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 18),
    _EtsysRadiusSnoopingFlowTotalDroppedPackets_Type()
)
etsysRadiusSnoopingFlowTotalDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowTotalDroppedPackets.setStatus("current")
_EtsysRadiusSnoopingFlowUnsupportedReqPackets_Type = Counter32
_EtsysRadiusSnoopingFlowUnsupportedReqPackets_Object = MibTableColumn
etsysRadiusSnoopingFlowUnsupportedReqPackets = _EtsysRadiusSnoopingFlowUnsupportedReqPackets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 19),
    _EtsysRadiusSnoopingFlowUnsupportedReqPackets_Type()
)
etsysRadiusSnoopingFlowUnsupportedReqPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowUnsupportedReqPackets.setStatus("current")
_EtsysRadiusSnoopingFlowUnsupportedRspPackets_Type = Counter32
_EtsysRadiusSnoopingFlowUnsupportedRspPackets_Object = MibTableColumn
etsysRadiusSnoopingFlowUnsupportedRspPackets = _EtsysRadiusSnoopingFlowUnsupportedRspPackets_Object(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 1, 4, 1, 1, 20),
    _EtsysRadiusSnoopingFlowUnsupportedRspPackets_Type()
)
etsysRadiusSnoopingFlowUnsupportedRspPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowUnsupportedRspPackets.setStatus("current")
_EtsysRadiusSnoopingConformance_ObjectIdentity = ObjectIdentity
etsysRadiusSnoopingConformance = _EtsysRadiusSnoopingConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 2)
)
_EtsysRadiusSnoopingGroups_ObjectIdentity = ObjectIdentity
etsysRadiusSnoopingGroups = _EtsysRadiusSnoopingGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 2, 1)
)
_EtsysRadiusSnoopingCompliances_ObjectIdentity = ObjectIdentity
etsysRadiusSnoopingCompliances = _EtsysRadiusSnoopingCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 2, 2)
)

# Managed Objects groups

etsysRadiusSnoopingSystemGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 2, 1, 1)
)
etsysRadiusSnoopingSystemGroup.setObjects(
      *(("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSystemEnable"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSystemTimeout"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSystemConfiguredFlows"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSystemActiveSessions"))
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSystemGroup.setStatus("current")

etsysRadiusSnoopingPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 2, 1, 2)
)
etsysRadiusSnoopingPortGroup.setObjects(
      *(("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingPortEnable"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingPortTimeout"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingPortInitialize"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingPortDrop"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingPortAuthenticationsAllocated"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingPortAuthenticationsAllowed"))
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingPortGroup.setStatus("current")

etsysRadiusSnoopingSessionGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 2, 1, 3)
)
etsysRadiusSnoopingSessionGroup.setObjects(
      *(("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSessionInitialize"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSessionPort"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSessionRadiusClientAddressType"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSessionRadiusClientAddress"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSessionRadiusServerAddressType"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSessionRadiusServerAddress"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSessionDuration"))
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingSessionGroup.setStatus("current")

etsysRadiusSnoopingFlowGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 2, 1, 4)
)
etsysRadiusSnoopingFlowGroup.setObjects(
      *(("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowClientAddressType"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowClientAddress"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowServerAddressType"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowServerAddress"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowServerPortNumber"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowSecret"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowRowStatus"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowSecretEntered"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowCurrentSessions"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowPendingAuthentications"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowTotalSessions"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowAccessRequests"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowAccessAccepts"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowAccessRejects"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowInvalidRequests"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowInvalidResponses"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowTotalDroppedPackets"))
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowGroup.setStatus("deprecated")

etsysRadiusSnoopingFlowGroup2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 2, 1, 5)
)
etsysRadiusSnoopingFlowGroup2.setObjects(
      *(("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowClientAddressType"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowClientAddress"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowServerAddressType"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowServerAddress"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowServerPortNumber"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowSecret"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowRowStatus"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowSecretEntered"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowCurrentSessions"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowPendingAuthentications"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowTotalSessions"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowAccessRequests"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowAccessAccepts"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowAccessRejects"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowInvalidRequests"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowInvalidResponses"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowTotalDroppedPackets"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowUnsupportedReqPackets"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowUnsupportedRspPackets"))
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingFlowGroup2.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

etsysRadiusSnoopingCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 2, 2, 1)
)
etsysRadiusSnoopingCompliance.setObjects(
      *(("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSystemGroup"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingPortGroup"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSessionGroup"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowGroup"))
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingCompliance.setStatus(
        "deprecated"
    )

etsysRadiusSnoopingCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5624, 1, 2, 62, 2, 2, 2, 2)
)
etsysRadiusSnoopingCompliance2.setObjects(
      *(("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSystemGroup"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingPortGroup"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingSessionGroup"),
        ("ENTERASYS-RADIUS-SNOOPING-MIB", "etsysRadiusSnoopingFlowGroup2"))
)
if mibBuilder.loadTexts:
    etsysRadiusSnoopingCompliance2.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ENTERASYS-RADIUS-SNOOPING-MIB",
    **{"etsysRadiusSnoopingMIB": etsysRadiusSnoopingMIB,
       "etsysRadiusSnoopingObjectBase": etsysRadiusSnoopingObjectBase,
       "etsysRadiusSnoopingObjects": etsysRadiusSnoopingObjects,
       "etsysRadiusSnoopingSystem": etsysRadiusSnoopingSystem,
       "etsysRadiusSnoopingSystemEnable": etsysRadiusSnoopingSystemEnable,
       "etsysRadiusSnoopingSystemTimeout": etsysRadiusSnoopingSystemTimeout,
       "etsysRadiusSnoopingSystemConfiguredFlows": etsysRadiusSnoopingSystemConfiguredFlows,
       "etsysRadiusSnoopingSystemActiveSessions": etsysRadiusSnoopingSystemActiveSessions,
       "etsysRadiusSnoopingPort": etsysRadiusSnoopingPort,
       "etsysRadiusSnoopingPortTable": etsysRadiusSnoopingPortTable,
       "etsysRadiusSnoopingPortEntry": etsysRadiusSnoopingPortEntry,
       "etsysRadiusSnoopingPortIndex": etsysRadiusSnoopingPortIndex,
       "etsysRadiusSnoopingPortEnable": etsysRadiusSnoopingPortEnable,
       "etsysRadiusSnoopingPortTimeout": etsysRadiusSnoopingPortTimeout,
       "etsysRadiusSnoopingPortInitialize": etsysRadiusSnoopingPortInitialize,
       "etsysRadiusSnoopingPortDrop": etsysRadiusSnoopingPortDrop,
       "etsysRadiusSnoopingPortAuthenticationsAllocated": etsysRadiusSnoopingPortAuthenticationsAllocated,
       "etsysRadiusSnoopingPortAuthenticationsAllowed": etsysRadiusSnoopingPortAuthenticationsAllowed,
       "etsysRadiusSnoopingSession": etsysRadiusSnoopingSession,
       "etsysRadiusSnoopingSessionTable": etsysRadiusSnoopingSessionTable,
       "etsysRadiusSnoopingSessionEntry": etsysRadiusSnoopingSessionEntry,
       "etsysRadiusSnoopingSessionMACAddress": etsysRadiusSnoopingSessionMACAddress,
       "etsysRadiusSnoopingSessionInitialize": etsysRadiusSnoopingSessionInitialize,
       "etsysRadiusSnoopingSessionPort": etsysRadiusSnoopingSessionPort,
       "etsysRadiusSnoopingSessionRadiusClientAddressType": etsysRadiusSnoopingSessionRadiusClientAddressType,
       "etsysRadiusSnoopingSessionRadiusClientAddress": etsysRadiusSnoopingSessionRadiusClientAddress,
       "etsysRadiusSnoopingSessionRadiusServerAddressType": etsysRadiusSnoopingSessionRadiusServerAddressType,
       "etsysRadiusSnoopingSessionRadiusServerAddress": etsysRadiusSnoopingSessionRadiusServerAddress,
       "etsysRadiusSnoopingSessionDuration": etsysRadiusSnoopingSessionDuration,
       "etsysRadiusSnoopingFlow": etsysRadiusSnoopingFlow,
       "etsysRadiusSnoopingFlowTable": etsysRadiusSnoopingFlowTable,
       "etsysRadiusSnoopingFlowEntry": etsysRadiusSnoopingFlowEntry,
       "etsysRadiusSnoopingFlowIndex": etsysRadiusSnoopingFlowIndex,
       "etsysRadiusSnoopingFlowClientAddressType": etsysRadiusSnoopingFlowClientAddressType,
       "etsysRadiusSnoopingFlowClientAddress": etsysRadiusSnoopingFlowClientAddress,
       "etsysRadiusSnoopingFlowServerAddressType": etsysRadiusSnoopingFlowServerAddressType,
       "etsysRadiusSnoopingFlowServerAddress": etsysRadiusSnoopingFlowServerAddress,
       "etsysRadiusSnoopingFlowServerPortNumber": etsysRadiusSnoopingFlowServerPortNumber,
       "etsysRadiusSnoopingFlowSecret": etsysRadiusSnoopingFlowSecret,
       "etsysRadiusSnoopingFlowRowStatus": etsysRadiusSnoopingFlowRowStatus,
       "etsysRadiusSnoopingFlowSecretEntered": etsysRadiusSnoopingFlowSecretEntered,
       "etsysRadiusSnoopingFlowCurrentSessions": etsysRadiusSnoopingFlowCurrentSessions,
       "etsysRadiusSnoopingFlowPendingAuthentications": etsysRadiusSnoopingFlowPendingAuthentications,
       "etsysRadiusSnoopingFlowTotalSessions": etsysRadiusSnoopingFlowTotalSessions,
       "etsysRadiusSnoopingFlowAccessRequests": etsysRadiusSnoopingFlowAccessRequests,
       "etsysRadiusSnoopingFlowAccessAccepts": etsysRadiusSnoopingFlowAccessAccepts,
       "etsysRadiusSnoopingFlowAccessRejects": etsysRadiusSnoopingFlowAccessRejects,
       "etsysRadiusSnoopingFlowInvalidRequests": etsysRadiusSnoopingFlowInvalidRequests,
       "etsysRadiusSnoopingFlowInvalidResponses": etsysRadiusSnoopingFlowInvalidResponses,
       "etsysRadiusSnoopingFlowTotalDroppedPackets": etsysRadiusSnoopingFlowTotalDroppedPackets,
       "etsysRadiusSnoopingFlowUnsupportedReqPackets": etsysRadiusSnoopingFlowUnsupportedReqPackets,
       "etsysRadiusSnoopingFlowUnsupportedRspPackets": etsysRadiusSnoopingFlowUnsupportedRspPackets,
       "etsysRadiusSnoopingConformance": etsysRadiusSnoopingConformance,
       "etsysRadiusSnoopingGroups": etsysRadiusSnoopingGroups,
       "etsysRadiusSnoopingSystemGroup": etsysRadiusSnoopingSystemGroup,
       "etsysRadiusSnoopingPortGroup": etsysRadiusSnoopingPortGroup,
       "etsysRadiusSnoopingSessionGroup": etsysRadiusSnoopingSessionGroup,
       "etsysRadiusSnoopingFlowGroup": etsysRadiusSnoopingFlowGroup,
       "etsysRadiusSnoopingFlowGroup2": etsysRadiusSnoopingFlowGroup2,
       "etsysRadiusSnoopingCompliances": etsysRadiusSnoopingCompliances,
       "etsysRadiusSnoopingCompliance": etsysRadiusSnoopingCompliance,
       "etsysRadiusSnoopingCompliance2": etsysRadiusSnoopingCompliance2}
)
