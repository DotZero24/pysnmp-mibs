# SNMP MIB module (SUPERMICRO-MPLS-TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/SUPERMICRO-MPLS-TP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:05:24 2025
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

fsMplsTpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8)
)
if mibBuilder.loadTexts:
    fsMplsTpMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMplsTpNotifications_ObjectIdentity = ObjectIdentity
fsMplsTpNotifications = _FsMplsTpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 0)
)
_FsMplsTpObjects_ObjectIdentity = ObjectIdentity
fsMplsTpObjects = _FsMplsTpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1)
)
_FsMplsTpScalarObjects_ObjectIdentity = ObjectIdentity
fsMplsTpScalarObjects = _FsMplsTpScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 1)
)
_FsMplsTpGlobalConfigTable_Object = MibTable
fsMplsTpGlobalConfigTable = _FsMplsTpGlobalConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 2)
)
if mibBuilder.loadTexts:
    fsMplsTpGlobalConfigTable.setStatus("current")
_FsMplsTpGlobalConfigEntry_Object = MibTableRow
fsMplsTpGlobalConfigEntry = _FsMplsTpGlobalConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 2, 1)
)
fsMplsTpGlobalConfigEntry.setIndexNames(
    (0, "SUPERMICRO-MPLS-TP-MIB", "fsMplsTpContextId"),
)
if mibBuilder.loadTexts:
    fsMplsTpGlobalConfigEntry.setStatus("current")
_FsMplsTpContextId_Type = Unsigned32
_FsMplsTpContextId_Object = MibTableColumn
fsMplsTpContextId = _FsMplsTpContextId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 2, 1, 1),
    _FsMplsTpContextId_Type()
)
fsMplsTpContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsTpContextId.setStatus("current")


class _FsMplsTpOamModuleStatus_Type(Integer32):
    """Custom type fsMplsTpOamModuleStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_FsMplsTpOamModuleStatus_Type.__name__ = "Integer32"
_FsMplsTpOamModuleStatus_Object = MibTableColumn
fsMplsTpOamModuleStatus = _FsMplsTpOamModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 2, 1, 2),
    _FsMplsTpOamModuleStatus_Type()
)
fsMplsTpOamModuleStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsTpOamModuleStatus.setStatus("current")


class _FsMplsTpGlobalId_Type(Unsigned32):
    """Custom type fsMplsTpGlobalId based on Unsigned32"""
    defaultValue = 0


_FsMplsTpGlobalId_Type.__name__ = "Unsigned32"
_FsMplsTpGlobalId_Object = MibTableColumn
fsMplsTpGlobalId = _FsMplsTpGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 2, 1, 3),
    _FsMplsTpGlobalId_Type()
)
fsMplsTpGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsTpGlobalId.setStatus("current")


class _FsMplsTpIcc_Type(DisplayString):
    """Custom type fsMplsTpIcc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 6),
    )


_FsMplsTpIcc_Type.__name__ = "DisplayString"
_FsMplsTpIcc_Object = MibTableColumn
fsMplsTpIcc = _FsMplsTpIcc_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 2, 1, 4),
    _FsMplsTpIcc_Type()
)
fsMplsTpIcc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsTpIcc.setStatus("current")


class _FsMplsTpNodeIdentifier_Type(Unsigned32):
    """Custom type fsMplsTpNodeIdentifier based on Unsigned32"""
    defaultValue = 0


_FsMplsTpNodeIdentifier_Type.__name__ = "Unsigned32"
_FsMplsTpNodeIdentifier_Object = MibTableColumn
fsMplsTpNodeIdentifier = _FsMplsTpNodeIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 2, 1, 5),
    _FsMplsTpNodeIdentifier_Type()
)
fsMplsTpNodeIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsTpNodeIdentifier.setStatus("current")


class _FsMplsTpErrorCode_Type(Integer32):
    """Custom type fsMplsTpErrorCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("elpsAssociationExists", 1),
          ("megAssociationExists", 2),
          ("pseudowireAssociationExists", 3),
          ("proactiveSessionExists", 4),
          ("elpsProactiveSessionExists", 5),
          ("activeMeExists", 6))
    )


_FsMplsTpErrorCode_Type.__name__ = "Integer32"
_FsMplsTpErrorCode_Object = MibTableColumn
fsMplsTpErrorCode = _FsMplsTpErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 2, 1, 6),
    _FsMplsTpErrorCode_Type()
)
fsMplsTpErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMplsTpErrorCode.setStatus("current")


class _FsMplsTpTraceLevel_Type(Unsigned32):
    """Custom type fsMplsTpTraceLevel based on Unsigned32"""
    defaultValue = 0


_FsMplsTpTraceLevel_Type.__name__ = "Unsigned32"
_FsMplsTpTraceLevel_Object = MibTableColumn
fsMplsTpTraceLevel = _FsMplsTpTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 2, 1, 7),
    _FsMplsTpTraceLevel_Type()
)
fsMplsTpTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsTpTraceLevel.setStatus("current")


class _FsMplsTpNotificationEnable_Type(TruthValue):
    """Custom type fsMplsTpNotificationEnable based on TruthValue"""
    defaultValue = 2


_FsMplsTpNotificationEnable_Type.__name__ = "TruthValue"
_FsMplsTpNotificationEnable_Object = MibTableColumn
fsMplsTpNotificationEnable = _FsMplsTpNotificationEnable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 2, 1, 8),
    _FsMplsTpNotificationEnable_Type()
)
fsMplsTpNotificationEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsTpNotificationEnable.setStatus("current")
_FsMplsTpNodeMapTable_Object = MibTable
fsMplsTpNodeMapTable = _FsMplsTpNodeMapTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 3)
)
if mibBuilder.loadTexts:
    fsMplsTpNodeMapTable.setStatus("current")
_FsMplsTpNodeMapEntry_Object = MibTableRow
fsMplsTpNodeMapEntry = _FsMplsTpNodeMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 3, 1)
)
fsMplsTpNodeMapEntry.setIndexNames(
    (0, "SUPERMICRO-MPLS-TP-MIB", "fsMplsTpContextId"),
    (0, "SUPERMICRO-MPLS-TP-MIB", "fsMplsTpNodeMapLocalNum"),
)
if mibBuilder.loadTexts:
    fsMplsTpNodeMapEntry.setStatus("current")
_FsMplsTpNodeMapLocalNum_Type = Unsigned32
_FsMplsTpNodeMapLocalNum_Object = MibTableColumn
fsMplsTpNodeMapLocalNum = _FsMplsTpNodeMapLocalNum_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 3, 1, 1),
    _FsMplsTpNodeMapLocalNum_Type()
)
fsMplsTpNodeMapLocalNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMplsTpNodeMapLocalNum.setStatus("current")
_FsMplsTpNodeMapGlobalId_Type = Unsigned32
_FsMplsTpNodeMapGlobalId_Object = MibTableColumn
fsMplsTpNodeMapGlobalId = _FsMplsTpNodeMapGlobalId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 3, 1, 2),
    _FsMplsTpNodeMapGlobalId_Type()
)
fsMplsTpNodeMapGlobalId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsTpNodeMapGlobalId.setStatus("current")
_FsMplsTpNodeMapNodeId_Type = Unsigned32
_FsMplsTpNodeMapNodeId_Object = MibTableColumn
fsMplsTpNodeMapNodeId = _FsMplsTpNodeMapNodeId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 3, 1, 3),
    _FsMplsTpNodeMapNodeId_Type()
)
fsMplsTpNodeMapNodeId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMplsTpNodeMapNodeId.setStatus("current")
_FsMplsTpNodeMapRowStatus_Type = RowStatus
_FsMplsTpNodeMapRowStatus_Object = MibTableColumn
fsMplsTpNodeMapRowStatus = _FsMplsTpNodeMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 1, 3, 1, 4),
    _FsMplsTpNodeMapRowStatus_Type()
)
fsMplsTpNodeMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMplsTpNodeMapRowStatus.setStatus("current")
_FsMplsTpConformance_ObjectIdentity = ObjectIdentity
fsMplsTpConformance = _FsMplsTpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 13, 8, 2)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SUPERMICRO-MPLS-TP-MIB",
    **{"fsMplsTpMIB": fsMplsTpMIB,
       "fsMplsTpNotifications": fsMplsTpNotifications,
       "fsMplsTpObjects": fsMplsTpObjects,
       "fsMplsTpScalarObjects": fsMplsTpScalarObjects,
       "fsMplsTpGlobalConfigTable": fsMplsTpGlobalConfigTable,
       "fsMplsTpGlobalConfigEntry": fsMplsTpGlobalConfigEntry,
       "fsMplsTpContextId": fsMplsTpContextId,
       "fsMplsTpOamModuleStatus": fsMplsTpOamModuleStatus,
       "fsMplsTpGlobalId": fsMplsTpGlobalId,
       "fsMplsTpIcc": fsMplsTpIcc,
       "fsMplsTpNodeIdentifier": fsMplsTpNodeIdentifier,
       "fsMplsTpErrorCode": fsMplsTpErrorCode,
       "fsMplsTpTraceLevel": fsMplsTpTraceLevel,
       "fsMplsTpNotificationEnable": fsMplsTpNotificationEnable,
       "fsMplsTpNodeMapTable": fsMplsTpNodeMapTable,
       "fsMplsTpNodeMapEntry": fsMplsTpNodeMapEntry,
       "fsMplsTpNodeMapLocalNum": fsMplsTpNodeMapLocalNum,
       "fsMplsTpNodeMapGlobalId": fsMplsTpNodeMapGlobalId,
       "fsMplsTpNodeMapNodeId": fsMplsTpNodeMapNodeId,
       "fsMplsTpNodeMapRowStatus": fsMplsTpNodeMapRowStatus,
       "fsMplsTpConformance": fsMplsTpConformance}
)
