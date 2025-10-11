# SNMP MIB module (SUPERMICRO-MIStdRSTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MIStdRSTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:04:54 2025
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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")

(BridgeId,
 Timeout,
 fsDot1dBridge,
 fsDot1dStp,
 fsDot1dStpEntry,
 fsDot1dStpPortEntry) = mibBuilder.importSymbols(
    "SUPERMICRO-MIStdBRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "fsDot1dBridge",
    "fsDot1dStp",
    "fsDot1dStpEntry",
    "fsDot1dStpPortEntry")


# MODULE-IDENTITY

fsRstpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 11)
)
if mibBuilder.loadTexts:
    fsRstpMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsDot1dStpExtTable_Object = MibTable
fsDot1dStpExtTable = _FsDot1dStpExtTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 3)
)
if mibBuilder.loadTexts:
    fsDot1dStpExtTable.setStatus("current")
_FsDot1dStpExtEntry_Object = MibTableRow
fsDot1dStpExtEntry = _FsDot1dStpExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 3, 1)
)
if mibBuilder.loadTexts:
    fsDot1dStpExtEntry.setStatus("current")


class _FsDot1dStpVersion_Type(Integer32):
    """Custom type fsDot1dStpVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stpCompatible", 0),
          ("rstp", 2))
    )


_FsDot1dStpVersion_Type.__name__ = "Integer32"
_FsDot1dStpVersion_Object = MibTableColumn
fsDot1dStpVersion = _FsDot1dStpVersion_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 3, 1, 1),
    _FsDot1dStpVersion_Type()
)
fsDot1dStpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dStpVersion.setStatus("current")


class _FsDot1dStpTxHoldCount_Type(Integer32):
    """Custom type fsDot1dStpTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_FsDot1dStpTxHoldCount_Type.__name__ = "Integer32"
_FsDot1dStpTxHoldCount_Object = MibTableColumn
fsDot1dStpTxHoldCount = _FsDot1dStpTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 3, 1, 2),
    _FsDot1dStpTxHoldCount_Type()
)
fsDot1dStpTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dStpTxHoldCount.setStatus("current")


class _FsDot1dStpPathCostDefault_Type(Integer32):
    """Custom type fsDot1dStpPathCostDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stp8021d1998", 1),
          ("stp8021t2001", 2))
    )


_FsDot1dStpPathCostDefault_Type.__name__ = "Integer32"
_FsDot1dStpPathCostDefault_Object = MibTableColumn
fsDot1dStpPathCostDefault = _FsDot1dStpPathCostDefault_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 3, 1, 3),
    _FsDot1dStpPathCostDefault_Type()
)
fsDot1dStpPathCostDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dStpPathCostDefault.setStatus("obsolete")
_FsDot1dStpExtPortTable_Object = MibTable
fsDot1dStpExtPortTable = _FsDot1dStpExtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 4)
)
if mibBuilder.loadTexts:
    fsDot1dStpExtPortTable.setStatus("current")
_FsDot1dStpExtPortEntry_Object = MibTableRow
fsDot1dStpExtPortEntry = _FsDot1dStpExtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 4, 1)
)
if mibBuilder.loadTexts:
    fsDot1dStpExtPortEntry.setStatus("current")
_FsDot1dStpPortProtocolMigration_Type = TruthValue
_FsDot1dStpPortProtocolMigration_Object = MibTableColumn
fsDot1dStpPortProtocolMigration = _FsDot1dStpPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 4, 1, 1),
    _FsDot1dStpPortProtocolMigration_Type()
)
fsDot1dStpPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dStpPortProtocolMigration.setStatus("current")
_FsDot1dStpPortAdminEdgePort_Type = TruthValue
_FsDot1dStpPortAdminEdgePort_Object = MibTableColumn
fsDot1dStpPortAdminEdgePort = _FsDot1dStpPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 4, 1, 2),
    _FsDot1dStpPortAdminEdgePort_Type()
)
fsDot1dStpPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dStpPortAdminEdgePort.setStatus("current")
_FsDot1dStpPortOperEdgePort_Type = TruthValue
_FsDot1dStpPortOperEdgePort_Object = MibTableColumn
fsDot1dStpPortOperEdgePort = _FsDot1dStpPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 4, 1, 3),
    _FsDot1dStpPortOperEdgePort_Type()
)
fsDot1dStpPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dStpPortOperEdgePort.setStatus("current")


class _FsDot1dStpPortAdminPointToPoint_Type(Integer32):
    """Custom type fsDot1dStpPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_FsDot1dStpPortAdminPointToPoint_Type.__name__ = "Integer32"
_FsDot1dStpPortAdminPointToPoint_Object = MibTableColumn
fsDot1dStpPortAdminPointToPoint = _FsDot1dStpPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 4, 1, 4),
    _FsDot1dStpPortAdminPointToPoint_Type()
)
fsDot1dStpPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dStpPortAdminPointToPoint.setStatus("current")
_FsDot1dStpPortOperPointToPoint_Type = TruthValue
_FsDot1dStpPortOperPointToPoint_Object = MibTableColumn
fsDot1dStpPortOperPointToPoint = _FsDot1dStpPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 4, 1, 5),
    _FsDot1dStpPortOperPointToPoint_Type()
)
fsDot1dStpPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDot1dStpPortOperPointToPoint.setStatus("current")


class _FsDot1dStpPortAdminPathCost_Type(Integer32):
    """Custom type fsDot1dStpPortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_FsDot1dStpPortAdminPathCost_Type.__name__ = "Integer32"
_FsDot1dStpPortAdminPathCost_Object = MibTableColumn
fsDot1dStpPortAdminPathCost = _FsDot1dStpPortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 2, 4, 1, 6),
    _FsDot1dStpPortAdminPathCost_Type()
)
fsDot1dStpPortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsDot1dStpPortAdminPathCost.setStatus("current")
_FsRstpMIBObjects_ObjectIdentity = ObjectIdentity
fsRstpMIBObjects = _FsRstpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 11, 1)
)
_FsRstpConformance_ObjectIdentity = ObjectIdentity
fsRstpConformance = _FsRstpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 11, 2)
)
_FsRstpGroups_ObjectIdentity = ObjectIdentity
fsRstpGroups = _FsRstpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 11, 2, 1)
)
_FsRstpCompliances_ObjectIdentity = ObjectIdentity
fsRstpCompliances = _FsRstpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 11, 2, 2)
)
fsDot1dStpEntry.registerAugmentions(
    ("SUPERMICRO-MIStdRSTP-MIB",
     "fsDot1dStpExtEntry")
)
fsDot1dStpExtEntry.setIndexNames(*fsDot1dStpEntry.getIndexNames())
fsDot1dStpPortEntry.registerAugmentions(
    ("SUPERMICRO-MIStdRSTP-MIB",
     "fsDot1dStpExtPortEntry")
)
fsDot1dStpExtPortEntry.setIndexNames(*fsDot1dStpPortEntry.getIndexNames())

# Managed Objects groups

fsRstpBridgeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 11, 2, 1, 1)
)
fsRstpBridgeGroup.setObjects(
      *(("SUPERMICRO-MIStdRSTP-MIB", "fsDot1dStpVersion"),
        ("SUPERMICRO-MIStdRSTP-MIB", "fsDot1dStpTxHoldCount"))
)
if mibBuilder.loadTexts:
    fsRstpBridgeGroup.setStatus("current")

fsRstpPortGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 11, 2, 1, 2)
)
fsRstpPortGroup.setObjects(
      *(("SUPERMICRO-MIStdRSTP-MIB", "fsDot1dStpPortProtocolMigration"),
        ("SUPERMICRO-MIStdRSTP-MIB", "fsDot1dStpPortAdminEdgePort"),
        ("SUPERMICRO-MIStdRSTP-MIB", "fsDot1dStpPortOperEdgePort"),
        ("SUPERMICRO-MIStdRSTP-MIB", "fsDot1dStpPortAdminPointToPoint"),
        ("SUPERMICRO-MIStdRSTP-MIB", "fsDot1dStpPortOperPointToPoint"))
)
if mibBuilder.loadTexts:
    fsRstpPortGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsRstpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 116, 11, 2, 2, 1)
)
fsRstpCompliance.setObjects(
      *(("SUPERMICRO-MIStdRSTP-MIB", "fsRstpBridgeGroup"),
        ("SUPERMICRO-MIStdRSTP-MIB", "fsRstpPortGroup"))
)
if mibBuilder.loadTexts:
    fsRstpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MIStdRSTP-MIB",
    **{"fsDot1dStpExtTable": fsDot1dStpExtTable,
       "fsDot1dStpExtEntry": fsDot1dStpExtEntry,
       "fsDot1dStpVersion": fsDot1dStpVersion,
       "fsDot1dStpTxHoldCount": fsDot1dStpTxHoldCount,
       "fsDot1dStpPathCostDefault": fsDot1dStpPathCostDefault,
       "fsDot1dStpExtPortTable": fsDot1dStpExtPortTable,
       "fsDot1dStpExtPortEntry": fsDot1dStpExtPortEntry,
       "fsDot1dStpPortProtocolMigration": fsDot1dStpPortProtocolMigration,
       "fsDot1dStpPortAdminEdgePort": fsDot1dStpPortAdminEdgePort,
       "fsDot1dStpPortOperEdgePort": fsDot1dStpPortOperEdgePort,
       "fsDot1dStpPortAdminPointToPoint": fsDot1dStpPortAdminPointToPoint,
       "fsDot1dStpPortOperPointToPoint": fsDot1dStpPortOperPointToPoint,
       "fsDot1dStpPortAdminPathCost": fsDot1dStpPortAdminPathCost,
       "fsRstpMIB": fsRstpMIB,
       "fsRstpMIBObjects": fsRstpMIBObjects,
       "fsRstpConformance": fsRstpConformance,
       "fsRstpGroups": fsRstpGroups,
       "fsRstpBridgeGroup": fsRstpBridgeGroup,
       "fsRstpPortGroup": fsRstpPortGroup,
       "fsRstpCompliances": fsRstpCompliances,
       "fsRstpCompliance": fsRstpCompliance}
)
