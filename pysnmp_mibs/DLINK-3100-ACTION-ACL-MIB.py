# SNMP MIB module (DLINK-3100-ACTION-ACL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/d-link/DLINK-3100-ACTION-ACL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:48:55 2025
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

(rnd,) = mibBuilder.importSymbols(
    "DLINK-3100-MIB",
    "rnd")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

rlActionAcl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130)
)
if mibBuilder.loadTexts:
    rlActionAcl.setRevisions(
        ("2007-11-18 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ClassMapAction(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("setIP-Precedence", 2),
          ("setDSCP", 3),
          ("setQueue", 4),
          ("setCos", 5),
          ("trustCos", 6),
          ("trustDSCP", 7),
          ("trustTCP-UDPport", 8),
          ("trustCosDscp", 9))
    )



# MIB Managed Objects in the order of their OIDs

_RlActionAclTable_Object = MibTable
rlActionAclTable = _RlActionAclTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1)
)
if mibBuilder.loadTexts:
    rlActionAclTable.setStatus("current")
_RlActionAclEntry_Object = MibTableRow
rlActionAclEntry = _RlActionAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1)
)
rlActionAclEntry.setIndexNames(
    (0, "DLINK-3100-ACTION-ACL-MIB", "rlActionAclAclIndex"),
)
if mibBuilder.loadTexts:
    rlActionAclEntry.setStatus("current")


class _RlActionAclAclIndex_Type(Integer32):
    """Custom type rlActionAclAclIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 240),
    )


_RlActionAclAclIndex_Type.__name__ = "Integer32"
_RlActionAclAclIndex_Object = MibTableColumn
rlActionAclAclIndex = _RlActionAclAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 1),
    _RlActionAclAclIndex_Type()
)
rlActionAclAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlActionAclAclIndex.setStatus("current")
_RlActionAclPorts_Type = PortList
_RlActionAclPorts_Object = MibTableColumn
rlActionAclPorts = _RlActionAclPorts_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 2),
    _RlActionAclPorts_Type()
)
rlActionAclPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlActionAclPorts.setStatus("current")
_RlActionAclClassMapAction_Type = ClassMapAction
_RlActionAclClassMapAction_Object = MibTableColumn
rlActionAclClassMapAction = _RlActionAclClassMapAction_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 3),
    _RlActionAclClassMapAction_Type()
)
rlActionAclClassMapAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlActionAclClassMapAction.setStatus("current")
_RlActionAclClassMapMarkValue_Type = Integer32
_RlActionAclClassMapMarkValue_Object = MibTableColumn
rlActionAclClassMapMarkValue = _RlActionAclClassMapMarkValue_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 4),
    _RlActionAclClassMapMarkValue_Type()
)
rlActionAclClassMapMarkValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlActionAclClassMapMarkValue.setStatus("current")
_RlActionAclPolicerIndex_Type = Integer32
_RlActionAclPolicerIndex_Object = MibTableColumn
rlActionAclPolicerIndex = _RlActionAclPolicerIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 5),
    _RlActionAclPolicerIndex_Type()
)
rlActionAclPolicerIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlActionAclPolicerIndex.setStatus("current")
_RlActionAclStatus_Type = RowStatus
_RlActionAclStatus_Object = MibTableColumn
rlActionAclStatus = _RlActionAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 1, 1, 6),
    _RlActionAclStatus_Type()
)
rlActionAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlActionAclStatus.setStatus("current")
_RlPort2AclsMappingTable_Object = MibTable
rlPort2AclsMappingTable = _RlPort2AclsMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 2)
)
if mibBuilder.loadTexts:
    rlPort2AclsMappingTable.setStatus("current")
_RlPort2AclsMappingEntry_Object = MibTableRow
rlPort2AclsMappingEntry = _RlPort2AclsMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 2, 1)
)
rlPort2AclsMappingEntry.setIndexNames(
    (0, "DLINK-3100-ACTION-ACL-MIB", "rlPorts2AclsMappingPortIndex"),
)
if mibBuilder.loadTexts:
    rlPort2AclsMappingEntry.setStatus("current")
_RlPorts2AclsMappingPortIndex_Type = Integer32
_RlPorts2AclsMappingPortIndex_Object = MibTableColumn
rlPorts2AclsMappingPortIndex = _RlPorts2AclsMappingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 2, 1, 1),
    _RlPorts2AclsMappingPortIndex_Type()
)
rlPorts2AclsMappingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPorts2AclsMappingPortIndex.setStatus("current")
_RlPorts2AclsMappingPortAcls_Type = PortList
_RlPorts2AclsMappingPortAcls_Object = MibTableColumn
rlPorts2AclsMappingPortAcls = _RlPorts2AclsMappingPortAcls_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 2, 1, 2),
    _RlPorts2AclsMappingPortAcls_Type()
)
rlPorts2AclsMappingPortAcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPorts2AclsMappingPortAcls.setStatus("current")


class _RlActionAclDeleteProfileIndex_Type(Integer32):
    """Custom type rlActionAclDeleteProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_RlActionAclDeleteProfileIndex_Type.__name__ = "Integer32"
_RlActionAclDeleteProfileIndex_Object = MibScalar
rlActionAclDeleteProfileIndex = _RlActionAclDeleteProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 3),
    _RlActionAclDeleteProfileIndex_Type()
)
rlActionAclDeleteProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlActionAclDeleteProfileIndex.setStatus("current")
_RlNumOfUsedTcamAces_Type = Integer32
_RlNumOfUsedTcamAces_Object = MibScalar
rlNumOfUsedTcamAces = _RlNumOfUsedTcamAces_Object(
    (1, 3, 6, 1, 4, 1, 171, 10, 94, 89, 89, 130, 4),
    _RlNumOfUsedTcamAces_Type()
)
rlNumOfUsedTcamAces.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlNumOfUsedTcamAces.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DLINK-3100-ACTION-ACL-MIB",
    **{"ClassMapAction": ClassMapAction,
       "rlActionAcl": rlActionAcl,
       "rlActionAclTable": rlActionAclTable,
       "rlActionAclEntry": rlActionAclEntry,
       "rlActionAclAclIndex": rlActionAclAclIndex,
       "rlActionAclPorts": rlActionAclPorts,
       "rlActionAclClassMapAction": rlActionAclClassMapAction,
       "rlActionAclClassMapMarkValue": rlActionAclClassMapMarkValue,
       "rlActionAclPolicerIndex": rlActionAclPolicerIndex,
       "rlActionAclStatus": rlActionAclStatus,
       "rlPort2AclsMappingTable": rlPort2AclsMappingTable,
       "rlPort2AclsMappingEntry": rlPort2AclsMappingEntry,
       "rlPorts2AclsMappingPortIndex": rlPorts2AclsMappingPortIndex,
       "rlPorts2AclsMappingPortAcls": rlPorts2AclsMappingPortAcls,
       "rlActionAclDeleteProfileIndex": rlActionAclDeleteProfileIndex,
       "rlNumOfUsedTcamAces": rlNumOfUsedTcamAces}
)
