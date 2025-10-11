# SNMP MIB module (RUGGEDCOM-STP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-STP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:31 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(ruggedcomMgmt,
 ruggedcomTraps) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomMgmt",
    "ruggedcomTraps")

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

rcRstp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5)
)
if mibBuilder.loadTexts:
    rcRstp.setRevisions(
        ("2012-06-01 17:00",
         "2012-06-01 17:00",
         "2010-10-10 10:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcRstpBase_ObjectIdentity = ObjectIdentity
rcRstpBase = _RcRstpBase_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 1)
)


class _RcRstpDot1dStpTxHoldCount_Type(Integer32):
    """Custom type rcRstpDot1dStpTxHoldCount based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(3, 100),
    )


_RcRstpDot1dStpTxHoldCount_Type.__name__ = "Integer32"
_RcRstpDot1dStpTxHoldCount_Object = MibScalar
rcRstpDot1dStpTxHoldCount = _RcRstpDot1dStpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 1),
    _RcRstpDot1dStpTxHoldCount_Type()
)
rcRstpDot1dStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRstpDot1dStpTxHoldCount.setStatus("current")
_RcRstpDot1dStpForwardingPorts_Type = PortList
_RcRstpDot1dStpForwardingPorts_Object = MibScalar
rcRstpDot1dStpForwardingPorts = _RcRstpDot1dStpForwardingPorts_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 2),
    _RcRstpDot1dStpForwardingPorts_Type()
)
rcRstpDot1dStpForwardingPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpDot1dStpForwardingPorts.setStatus("current")
_RcRstpDot1dStpBlockedPorts_Type = PortList
_RcRstpDot1dStpBlockedPorts_Object = MibScalar
rcRstpDot1dStpBlockedPorts = _RcRstpDot1dStpBlockedPorts_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 3),
    _RcRstpDot1dStpBlockedPorts_Type()
)
rcRstpDot1dStpBlockedPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpDot1dStpBlockedPorts.setStatus("current")
_RcRstpDot1dStpBrokenPorts_Type = PortList
_RcRstpDot1dStpBrokenPorts_Object = MibScalar
rcRstpDot1dStpBrokenPorts = _RcRstpDot1dStpBrokenPorts_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 4),
    _RcRstpDot1dStpBrokenPorts_Type()
)
rcRstpDot1dStpBrokenPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpDot1dStpBrokenPorts.setStatus("current")
_RcRstpDot1dRstpAlternatePorts_Type = PortList
_RcRstpDot1dRstpAlternatePorts_Object = MibScalar
rcRstpDot1dRstpAlternatePorts = _RcRstpDot1dRstpAlternatePorts_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 5),
    _RcRstpDot1dRstpAlternatePorts_Type()
)
rcRstpDot1dRstpAlternatePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpDot1dRstpAlternatePorts.setStatus("current")
_RcRstpDot1dRstpBackupPorts_Type = PortList
_RcRstpDot1dRstpBackupPorts_Object = MibScalar
rcRstpDot1dRstpBackupPorts = _RcRstpDot1dRstpBackupPorts_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 1, 6),
    _RcRstpDot1dRstpBackupPorts_Type()
)
rcRstpDot1dRstpBackupPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcRstpDot1dRstpBackupPorts.setStatus("current")
_RcRstpConformance_ObjectIdentity = ObjectIdentity
rcRstpConformance = _RcRstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 3)
)
_RcRstpGroups_ObjectIdentity = ObjectIdentity
rcRstpGroups = _RcRstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 3, 2)
)
_RuggedcomRstpTraps_ObjectIdentity = ObjectIdentity
ruggedcomRstpTraps = _RuggedcomRstpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 5, 11)
)

# Managed Objects groups

rcRstpBaseStpTxHoldCountGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 3, 2, 1)
)
rcRstpBaseStpTxHoldCountGroup.setObjects(
    ("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpTxHoldCount")
)
if mibBuilder.loadTexts:
    rcRstpBaseStpTxHoldCountGroup.setStatus("current")

rcRstpBaseGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 3, 2, 2)
)
rcRstpBaseGroup.setObjects(
      *(("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpForwardingPorts"),
        ("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpBlockedPorts"),
        ("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpBrokenPorts"),
        ("RUGGEDCOM-STP-MIB", "rcRstpDot1dRstpAlternatePorts"),
        ("RUGGEDCOM-STP-MIB", "rcRstpDot1dRstpBackupPorts"))
)
if mibBuilder.loadTexts:
    rcRstpBaseGroup.setStatus("current")

rcRstpNotifyGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 5, 3, 2, 3)
)
rcRstpNotifyGroup.setObjects(
    ("RUGGEDCOM-STP-MIB", "rcRstpNewTopology")
)
if mibBuilder.loadTexts:
    rcRstpNotifyGroup.setStatus("current")


# Notification objects

rcRstpNewTopology = NotificationType(
    (1, 3, 6, 1, 4, 1, 15004, 5, 11, 1)
)
rcRstpNewTopology.setObjects(
      *(("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpForwardingPorts"),
        ("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpBlockedPorts"),
        ("RUGGEDCOM-STP-MIB", "rcRstpDot1dStpBrokenPorts"),
        ("RUGGEDCOM-STP-MIB", "rcRstpDot1dRstpAlternatePorts"),
        ("RUGGEDCOM-STP-MIB", "rcRstpDot1dRstpBackupPorts"),
        ("RUGGEDCOM-STP-MIB", "dot1dStpRootPort"),
        ("RUGGEDCOM-STP-MIB", "dot1dStpDesignatedRoot"))
)
if mibBuilder.loadTexts:
    rcRstpNewTopology.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-STP-MIB",
    **{"rcRstp": rcRstp,
       "rcRstpBase": rcRstpBase,
       "rcRstpDot1dStpTxHoldCount": rcRstpDot1dStpTxHoldCount,
       "rcRstpDot1dStpForwardingPorts": rcRstpDot1dStpForwardingPorts,
       "rcRstpDot1dStpBlockedPorts": rcRstpDot1dStpBlockedPorts,
       "rcRstpDot1dStpBrokenPorts": rcRstpDot1dStpBrokenPorts,
       "rcRstpDot1dRstpAlternatePorts": rcRstpDot1dRstpAlternatePorts,
       "rcRstpDot1dRstpBackupPorts": rcRstpDot1dRstpBackupPorts,
       "rcRstpConformance": rcRstpConformance,
       "rcRstpGroups": rcRstpGroups,
       "rcRstpBaseStpTxHoldCountGroup": rcRstpBaseStpTxHoldCountGroup,
       "rcRstpBaseGroup": rcRstpBaseGroup,
       "rcRstpNotifyGroup": rcRstpNotifyGroup,
       "ruggedcomRstpTraps": ruggedcomRstpTraps,
       "rcRstpNewTopology": rcRstpNewTopology}
)
