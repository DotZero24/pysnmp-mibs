# SNMP MIB module (AricentMIVlan-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siaemic/AricentMIVlan-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:20 2025
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

(fsDot1qStaticUnicastEntry,
 fsDot1qTpFdbEntry,
 fsDot1qTpFdbPort,
 fsDot1qTpPort,
 fsDot1qVlanStaticEntry,
 fsDot1qVlanStaticPortConfigEntry) = mibBuilder.importSymbols(
    "ARICENTQ-BRIDGE-MIB",
    "fsDot1qStaticUnicastEntry",
    "fsDot1qTpFdbEntry",
    "fsDot1qTpFdbPort",
    "fsDot1qTpPort",
    "fsDot1qVlanStaticEntry",
    "fsDot1qVlanStaticPortConfigEntry")

(VlanIdOrNone,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIdOrNone")

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

futureMIVlanMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 120)
)
if mibBuilder.loadTexts:
    futureMIVlanMIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class VlanId(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )



class EnabledStatus(TextualConvention, Integer32):
    status = "current"
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



class MacLearningStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("default", 3))
    )



# MIB Managed Objects in the order of their OIDs

_FsMIDot1qFutureVlan_ObjectIdentity = ObjectIdentity
fsMIDot1qFutureVlan = _FsMIDot1qFutureVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1)
)
_FsMIDot1qFutureVlanGlobalTrace_Type = TruthValue
_FsMIDot1qFutureVlanGlobalTrace_Object = MibScalar
fsMIDot1qFutureVlanGlobalTrace = _FsMIDot1qFutureVlanGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 1),
    _FsMIDot1qFutureVlanGlobalTrace_Type()
)
fsMIDot1qFutureVlanGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanGlobalTrace.setStatus("current")
_FsMIDot1qFutureVlanGlobalsTable_Object = MibTable
fsMIDot1qFutureVlanGlobalsTable = _FsMIDot1qFutureVlanGlobalsTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanGlobalsTable.setStatus("current")
_FsMIDot1qFutureVlanGlobalsEntry_Object = MibTableRow
fsMIDot1qFutureVlanGlobalsEntry = _FsMIDot1qFutureVlanGlobalsEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1)
)
fsMIDot1qFutureVlanGlobalsEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextId"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanGlobalsEntry.setStatus("current")


class _FsMIDot1qFutureVlanContextId_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDot1qFutureVlanContextId_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanContextId_Object = MibTableColumn
fsMIDot1qFutureVlanContextId = _FsMIDot1qFutureVlanContextId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 1),
    _FsMIDot1qFutureVlanContextId_Type()
)
fsMIDot1qFutureVlanContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanContextId.setStatus("current")
_FsMIDot1qFutureVlanStatus_Type = EnabledStatus
_FsMIDot1qFutureVlanStatus_Object = MibTableColumn
fsMIDot1qFutureVlanStatus = _FsMIDot1qFutureVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 2),
    _FsMIDot1qFutureVlanStatus_Type()
)
fsMIDot1qFutureVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanStatus.setStatus("current")
_FsMIDot1qFutureVlanMacBasedOnAllPorts_Type = EnabledStatus
_FsMIDot1qFutureVlanMacBasedOnAllPorts_Object = MibTableColumn
fsMIDot1qFutureVlanMacBasedOnAllPorts = _FsMIDot1qFutureVlanMacBasedOnAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 3),
    _FsMIDot1qFutureVlanMacBasedOnAllPorts_Type()
)
fsMIDot1qFutureVlanMacBasedOnAllPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanMacBasedOnAllPorts.setStatus("current")
_FsMIDot1qFutureVlanPortProtoBasedOnAllPorts_Type = EnabledStatus
_FsMIDot1qFutureVlanPortProtoBasedOnAllPorts_Object = MibTableColumn
fsMIDot1qFutureVlanPortProtoBasedOnAllPorts = _FsMIDot1qFutureVlanPortProtoBasedOnAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 4),
    _FsMIDot1qFutureVlanPortProtoBasedOnAllPorts_Type()
)
fsMIDot1qFutureVlanPortProtoBasedOnAllPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortProtoBasedOnAllPorts.setStatus("current")


class _FsMIDot1qFutureVlanShutdownStatus_Type(TruthValue):
    """Custom type fsMIDot1qFutureVlanShutdownStatus based on TruthValue"""
    defaultValue = 2


_FsMIDot1qFutureVlanShutdownStatus_Type.__name__ = "TruthValue"
_FsMIDot1qFutureVlanShutdownStatus_Object = MibTableColumn
fsMIDot1qFutureVlanShutdownStatus = _FsMIDot1qFutureVlanShutdownStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 5),
    _FsMIDot1qFutureVlanShutdownStatus_Type()
)
fsMIDot1qFutureVlanShutdownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanShutdownStatus.setStatus("deprecated")
_FsMIDot1qFutureGarpShutdownStatus_Type = TruthValue
_FsMIDot1qFutureGarpShutdownStatus_Object = MibTableColumn
fsMIDot1qFutureGarpShutdownStatus = _FsMIDot1qFutureGarpShutdownStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 6),
    _FsMIDot1qFutureGarpShutdownStatus_Type()
)
fsMIDot1qFutureGarpShutdownStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureGarpShutdownStatus.setStatus("current")


class _FsMIDot1qFutureVlanDebug_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanDebug based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 524287),
    )


_FsMIDot1qFutureVlanDebug_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanDebug_Object = MibTableColumn
fsMIDot1qFutureVlanDebug = _FsMIDot1qFutureVlanDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 7),
    _FsMIDot1qFutureVlanDebug_Type()
)
fsMIDot1qFutureVlanDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanDebug.setStatus("current")


class _FsMIDot1qFutureVlanLearningMode_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanLearningMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ivl", 1),
          ("svl", 2),
          ("hybrid", 3))
    )


_FsMIDot1qFutureVlanLearningMode_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanLearningMode_Object = MibTableColumn
fsMIDot1qFutureVlanLearningMode = _FsMIDot1qFutureVlanLearningMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 8),
    _FsMIDot1qFutureVlanLearningMode_Type()
)
fsMIDot1qFutureVlanLearningMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanLearningMode.setStatus("current")


class _FsMIDot1qFutureVlanHybridTypeDefault_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanHybridTypeDefault based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ivl", 1),
          ("svl", 2))
    )


_FsMIDot1qFutureVlanHybridTypeDefault_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanHybridTypeDefault_Object = MibTableColumn
fsMIDot1qFutureVlanHybridTypeDefault = _FsMIDot1qFutureVlanHybridTypeDefault_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 9),
    _FsMIDot1qFutureVlanHybridTypeDefault_Type()
)
fsMIDot1qFutureVlanHybridTypeDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanHybridTypeDefault.setStatus("current")
_FsMIDot1qFutureVlanOperStatus_Type = EnabledStatus
_FsMIDot1qFutureVlanOperStatus_Object = MibTableColumn
fsMIDot1qFutureVlanOperStatus = _FsMIDot1qFutureVlanOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 10),
    _FsMIDot1qFutureVlanOperStatus_Type()
)
fsMIDot1qFutureVlanOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanOperStatus.setStatus("current")
_FsMIDot1qFutureGvrpOperStatus_Type = EnabledStatus
_FsMIDot1qFutureGvrpOperStatus_Object = MibTableColumn
fsMIDot1qFutureGvrpOperStatus = _FsMIDot1qFutureGvrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 11),
    _FsMIDot1qFutureGvrpOperStatus_Type()
)
fsMIDot1qFutureGvrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureGvrpOperStatus.setStatus("current")
_FsMIDot1qFutureGmrpOperStatus_Type = EnabledStatus
_FsMIDot1qFutureGmrpOperStatus_Object = MibTableColumn
fsMIDot1qFutureGmrpOperStatus = _FsMIDot1qFutureGmrpOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 12),
    _FsMIDot1qFutureGmrpOperStatus_Type()
)
fsMIDot1qFutureGmrpOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureGmrpOperStatus.setStatus("current")


class _FsMIDot1qFutureVlanContextName_Type(DisplayString):
    """Custom type fsMIDot1qFutureVlanContextName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsMIDot1qFutureVlanContextName_Type.__name__ = "DisplayString"
_FsMIDot1qFutureVlanContextName_Object = MibTableColumn
fsMIDot1qFutureVlanContextName = _FsMIDot1qFutureVlanContextName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 13),
    _FsMIDot1qFutureVlanContextName_Type()
)
fsMIDot1qFutureVlanContextName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanContextName.setStatus("current")


class _FsMIDot1qFutureGarpDebug_Type(Integer32):
    """Custom type fsMIDot1qFutureGarpDebug based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_FsMIDot1qFutureGarpDebug_Type.__name__ = "Integer32"
_FsMIDot1qFutureGarpDebug_Object = MibTableColumn
fsMIDot1qFutureGarpDebug = _FsMIDot1qFutureGarpDebug_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 14),
    _FsMIDot1qFutureGarpDebug_Type()
)
fsMIDot1qFutureGarpDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureGarpDebug.setStatus("current")


class _FsMIDot1qFutureUnicastMacLearningLimit_Type(Unsigned32):
    """Custom type fsMIDot1qFutureUnicastMacLearningLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIDot1qFutureUnicastMacLearningLimit_Type.__name__ = "Unsigned32"
_FsMIDot1qFutureUnicastMacLearningLimit_Object = MibTableColumn
fsMIDot1qFutureUnicastMacLearningLimit = _FsMIDot1qFutureUnicastMacLearningLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 15),
    _FsMIDot1qFutureUnicastMacLearningLimit_Type()
)
fsMIDot1qFutureUnicastMacLearningLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureUnicastMacLearningLimit.setStatus("current")


class _FsMIDot1qFutureBaseBridgeMode_Type(Integer32):
    """Custom type fsMIDot1qFutureBaseBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dot1dTransparentMode", 1),
          ("dot1qVlanMode", 2))
    )


_FsMIDot1qFutureBaseBridgeMode_Type.__name__ = "Integer32"
_FsMIDot1qFutureBaseBridgeMode_Object = MibTableColumn
fsMIDot1qFutureBaseBridgeMode = _FsMIDot1qFutureBaseBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 16),
    _FsMIDot1qFutureBaseBridgeMode_Type()
)
fsMIDot1qFutureBaseBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureBaseBridgeMode.setStatus("current")
_FsMIDot1qFutureVlanSubnetBasedOnAllPorts_Type = EnabledStatus
_FsMIDot1qFutureVlanSubnetBasedOnAllPorts_Object = MibTableColumn
fsMIDot1qFutureVlanSubnetBasedOnAllPorts = _FsMIDot1qFutureVlanSubnetBasedOnAllPorts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 17),
    _FsMIDot1qFutureVlanSubnetBasedOnAllPorts_Type()
)
fsMIDot1qFutureVlanSubnetBasedOnAllPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanSubnetBasedOnAllPorts.setStatus("current")


class _FsMIDot1qFutureVlanGlobalMacLearningStatus_Type(EnabledStatus):
    """Custom type fsMIDot1qFutureVlanGlobalMacLearningStatus based on EnabledStatus"""
    defaultValue = 1


_FsMIDot1qFutureVlanGlobalMacLearningStatus_Type.__name__ = "EnabledStatus"
_FsMIDot1qFutureVlanGlobalMacLearningStatus_Object = MibTableColumn
fsMIDot1qFutureVlanGlobalMacLearningStatus = _FsMIDot1qFutureVlanGlobalMacLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 18),
    _FsMIDot1qFutureVlanGlobalMacLearningStatus_Type()
)
fsMIDot1qFutureVlanGlobalMacLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanGlobalMacLearningStatus.setStatus("current")


class _FsMIDot1qFutureVlanApplyEnhancedFilteringCriteria_Type(TruthValue):
    """Custom type fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria based on TruthValue"""
    defaultValue = 1


_FsMIDot1qFutureVlanApplyEnhancedFilteringCriteria_Type.__name__ = "TruthValue"
_FsMIDot1qFutureVlanApplyEnhancedFilteringCriteria_Object = MibTableColumn
fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria = _FsMIDot1qFutureVlanApplyEnhancedFilteringCriteria_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 19),
    _FsMIDot1qFutureVlanApplyEnhancedFilteringCriteria_Type()
)
fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria.setStatus("current")


class _FsMIDot1qFutureVlanGlobalsFdbFlush_Type(TruthValue):
    """Custom type fsMIDot1qFutureVlanGlobalsFdbFlush based on TruthValue"""
    defaultValue = 2


_FsMIDot1qFutureVlanGlobalsFdbFlush_Type.__name__ = "TruthValue"
_FsMIDot1qFutureVlanGlobalsFdbFlush_Object = MibTableColumn
fsMIDot1qFutureVlanGlobalsFdbFlush = _FsMIDot1qFutureVlanGlobalsFdbFlush_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 20),
    _FsMIDot1qFutureVlanGlobalsFdbFlush_Type()
)
fsMIDot1qFutureVlanGlobalsFdbFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanGlobalsFdbFlush.setStatus("current")


class _FsMIDot1qFutureVlanUserDefinedTPID_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanUserDefinedTPID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDot1qFutureVlanUserDefinedTPID_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanUserDefinedTPID_Object = MibTableColumn
fsMIDot1qFutureVlanUserDefinedTPID = _FsMIDot1qFutureVlanUserDefinedTPID_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 21),
    _FsMIDot1qFutureVlanUserDefinedTPID_Type()
)
fsMIDot1qFutureVlanUserDefinedTPID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanUserDefinedTPID.setStatus("current")


class _FsMIDot1qFutureVlanRemoteFdbFlush_Type(TruthValue):
    """Custom type fsMIDot1qFutureVlanRemoteFdbFlush based on TruthValue"""
    defaultValue = 2


_FsMIDot1qFutureVlanRemoteFdbFlush_Type.__name__ = "TruthValue"
_FsMIDot1qFutureVlanRemoteFdbFlush_Object = MibTableColumn
fsMIDot1qFutureVlanRemoteFdbFlush = _FsMIDot1qFutureVlanRemoteFdbFlush_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 2, 1, 22),
    _FsMIDot1qFutureVlanRemoteFdbFlush_Type()
)
fsMIDot1qFutureVlanRemoteFdbFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanRemoteFdbFlush.setStatus("current")
_FsMIDot1qFutureVlanPortTable_Object = MibTable
fsMIDot1qFutureVlanPortTable = _FsMIDot1qFutureVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortTable.setStatus("current")
_FsMIDot1qFutureVlanPortEntry_Object = MibTableRow
fsMIDot1qFutureVlanPortEntry = _FsMIDot1qFutureVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1)
)
fsMIDot1qFutureVlanPortEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanPort"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortEntry.setStatus("current")


class _FsMIDot1qFutureVlanPort_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIDot1qFutureVlanPort_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPort_Object = MibTableColumn
fsMIDot1qFutureVlanPort = _FsMIDot1qFutureVlanPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 1),
    _FsMIDot1qFutureVlanPort_Type()
)
fsMIDot1qFutureVlanPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPort.setStatus("current")


class _FsMIDot1qFutureVlanPortType_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("accessPort", 1),
          ("trunkPort", 2),
          ("hybridPort", 3),
          ("hostPort", 4),
          ("promiscuousPort", 5))
    )


_FsMIDot1qFutureVlanPortType_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortType_Object = MibTableColumn
fsMIDot1qFutureVlanPortType = _FsMIDot1qFutureVlanPortType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 2),
    _FsMIDot1qFutureVlanPortType_Type()
)
fsMIDot1qFutureVlanPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortType.setStatus("current")
_FsMIDot1qFutureVlanPortMacBasedClassification_Type = EnabledStatus
_FsMIDot1qFutureVlanPortMacBasedClassification_Object = MibTableColumn
fsMIDot1qFutureVlanPortMacBasedClassification = _FsMIDot1qFutureVlanPortMacBasedClassification_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 3),
    _FsMIDot1qFutureVlanPortMacBasedClassification_Type()
)
fsMIDot1qFutureVlanPortMacBasedClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortMacBasedClassification.setStatus("current")
_FsMIDot1qFutureVlanPortPortProtoBasedClassification_Type = EnabledStatus
_FsMIDot1qFutureVlanPortPortProtoBasedClassification_Object = MibTableColumn
fsMIDot1qFutureVlanPortPortProtoBasedClassification = _FsMIDot1qFutureVlanPortPortProtoBasedClassification_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 4),
    _FsMIDot1qFutureVlanPortPortProtoBasedClassification_Type()
)
fsMIDot1qFutureVlanPortPortProtoBasedClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortPortProtoBasedClassification.setStatus("current")


class _FsMIDot1qFutureVlanFilteringUtilityCriteria_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanFilteringUtilityCriteria based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("enhanced", 2))
    )


_FsMIDot1qFutureVlanFilteringUtilityCriteria_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanFilteringUtilityCriteria_Object = MibTableColumn
fsMIDot1qFutureVlanFilteringUtilityCriteria = _FsMIDot1qFutureVlanFilteringUtilityCriteria_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 5),
    _FsMIDot1qFutureVlanFilteringUtilityCriteria_Type()
)
fsMIDot1qFutureVlanFilteringUtilityCriteria.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanFilteringUtilityCriteria.setStatus("current")


class _FsMIDot1qFutureVlanPortProtected_Type(TruthValue):
    """Custom type fsMIDot1qFutureVlanPortProtected based on TruthValue"""
    defaultValue = 2


_FsMIDot1qFutureVlanPortProtected_Type.__name__ = "TruthValue"
_FsMIDot1qFutureVlanPortProtected_Object = MibTableColumn
fsMIDot1qFutureVlanPortProtected = _FsMIDot1qFutureVlanPortProtected_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 6),
    _FsMIDot1qFutureVlanPortProtected_Type()
)
fsMIDot1qFutureVlanPortProtected.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortProtected.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetBasedClassification_Type = EnabledStatus
_FsMIDot1qFutureVlanPortSubnetBasedClassification_Object = MibTableColumn
fsMIDot1qFutureVlanPortSubnetBasedClassification = _FsMIDot1qFutureVlanPortSubnetBasedClassification_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 7),
    _FsMIDot1qFutureVlanPortSubnetBasedClassification_Type()
)
fsMIDot1qFutureVlanPortSubnetBasedClassification.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetBasedClassification.setStatus("current")


class _FsMIDot1qFutureVlanPortUnicastMacLearning_Type(EnabledStatus):
    """Custom type fsMIDot1qFutureVlanPortUnicastMacLearning based on EnabledStatus"""
    defaultValue = 1


_FsMIDot1qFutureVlanPortUnicastMacLearning_Type.__name__ = "EnabledStatus"
_FsMIDot1qFutureVlanPortUnicastMacLearning_Object = MibTableColumn
fsMIDot1qFutureVlanPortUnicastMacLearning = _FsMIDot1qFutureVlanPortUnicastMacLearning_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 8),
    _FsMIDot1qFutureVlanPortUnicastMacLearning_Type()
)
fsMIDot1qFutureVlanPortUnicastMacLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortUnicastMacLearning.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount = _FsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 9),
    _FsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount = _FsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 10),
    _FsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpJoinInTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpJoinInTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpJoinInTxCount = _FsMIDot1qFutureVlanPortGmrpJoinInTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 11),
    _FsMIDot1qFutureVlanPortGmrpJoinInTxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpJoinInTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpJoinInTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpJoinInRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpJoinInRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpJoinInRxCount = _FsMIDot1qFutureVlanPortGmrpJoinInRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 12),
    _FsMIDot1qFutureVlanPortGmrpJoinInRxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpJoinInRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpJoinInRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpLeaveInTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveInTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveInTxCount = _FsMIDot1qFutureVlanPortGmrpLeaveInTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 13),
    _FsMIDot1qFutureVlanPortGmrpLeaveInTxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpLeaveInTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpLeaveInTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpLeaveInRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveInRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveInRxCount = _FsMIDot1qFutureVlanPortGmrpLeaveInRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 14),
    _FsMIDot1qFutureVlanPortGmrpLeaveInRxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpLeaveInRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpLeaveInRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount = _FsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 15),
    _FsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount = _FsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 16),
    _FsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpEmptyTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpEmptyTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpEmptyTxCount = _FsMIDot1qFutureVlanPortGmrpEmptyTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 17),
    _FsMIDot1qFutureVlanPortGmrpEmptyTxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpEmptyTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpEmptyTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpEmptyRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpEmptyRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpEmptyRxCount = _FsMIDot1qFutureVlanPortGmrpEmptyRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 18),
    _FsMIDot1qFutureVlanPortGmrpEmptyRxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpEmptyRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpEmptyRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpLeaveAllTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveAllTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveAllTxCount = _FsMIDot1qFutureVlanPortGmrpLeaveAllTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 19),
    _FsMIDot1qFutureVlanPortGmrpLeaveAllTxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpLeaveAllTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpLeaveAllTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpLeaveAllRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpLeaveAllRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpLeaveAllRxCount = _FsMIDot1qFutureVlanPortGmrpLeaveAllRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 20),
    _FsMIDot1qFutureVlanPortGmrpLeaveAllRxCount_Type()
)
fsMIDot1qFutureVlanPortGmrpLeaveAllRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpLeaveAllRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGmrpDiscardCount_Type = Counter32
_FsMIDot1qFutureVlanPortGmrpDiscardCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGmrpDiscardCount = _FsMIDot1qFutureVlanPortGmrpDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 21),
    _FsMIDot1qFutureVlanPortGmrpDiscardCount_Type()
)
fsMIDot1qFutureVlanPortGmrpDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGmrpDiscardCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount = _FsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 22),
    _FsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount = _FsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 23),
    _FsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpJoinInTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpJoinInTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpJoinInTxCount = _FsMIDot1qFutureVlanPortGvrpJoinInTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 24),
    _FsMIDot1qFutureVlanPortGvrpJoinInTxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpJoinInTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpJoinInTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpJoinInRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpJoinInRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpJoinInRxCount = _FsMIDot1qFutureVlanPortGvrpJoinInRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 25),
    _FsMIDot1qFutureVlanPortGvrpJoinInRxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpJoinInRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpJoinInRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpLeaveInTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveInTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveInTxCount = _FsMIDot1qFutureVlanPortGvrpLeaveInTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 26),
    _FsMIDot1qFutureVlanPortGvrpLeaveInTxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpLeaveInTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpLeaveInTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpLeaveInRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveInRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveInRxCount = _FsMIDot1qFutureVlanPortGvrpLeaveInRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 27),
    _FsMIDot1qFutureVlanPortGvrpLeaveInRxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpLeaveInRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpLeaveInRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount = _FsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 28),
    _FsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount = _FsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 29),
    _FsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpEmptyTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpEmptyTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpEmptyTxCount = _FsMIDot1qFutureVlanPortGvrpEmptyTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 30),
    _FsMIDot1qFutureVlanPortGvrpEmptyTxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpEmptyTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpEmptyTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpEmptyRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpEmptyRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpEmptyRxCount = _FsMIDot1qFutureVlanPortGvrpEmptyRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 31),
    _FsMIDot1qFutureVlanPortGvrpEmptyRxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpEmptyRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpEmptyRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpLeaveAllTxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveAllTxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveAllTxCount = _FsMIDot1qFutureVlanPortGvrpLeaveAllTxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 32),
    _FsMIDot1qFutureVlanPortGvrpLeaveAllTxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpLeaveAllTxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpLeaveAllTxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpLeaveAllRxCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpLeaveAllRxCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpLeaveAllRxCount = _FsMIDot1qFutureVlanPortGvrpLeaveAllRxCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 33),
    _FsMIDot1qFutureVlanPortGvrpLeaveAllRxCount_Type()
)
fsMIDot1qFutureVlanPortGvrpLeaveAllRxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpLeaveAllRxCount.setStatus("current")
_FsMIDot1qFutureVlanPortGvrpDiscardCount_Type = Counter32
_FsMIDot1qFutureVlanPortGvrpDiscardCount_Object = MibTableColumn
fsMIDot1qFutureVlanPortGvrpDiscardCount = _FsMIDot1qFutureVlanPortGvrpDiscardCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 34),
    _FsMIDot1qFutureVlanPortGvrpDiscardCount_Type()
)
fsMIDot1qFutureVlanPortGvrpDiscardCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortGvrpDiscardCount.setStatus("current")


class _FsMIDot1qFutureVlanPortFdbFlush_Type(TruthValue):
    """Custom type fsMIDot1qFutureVlanPortFdbFlush based on TruthValue"""
    defaultValue = 2


_FsMIDot1qFutureVlanPortFdbFlush_Type.__name__ = "TruthValue"
_FsMIDot1qFutureVlanPortFdbFlush_Object = MibTableColumn
fsMIDot1qFutureVlanPortFdbFlush = _FsMIDot1qFutureVlanPortFdbFlush_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 35),
    _FsMIDot1qFutureVlanPortFdbFlush_Type()
)
fsMIDot1qFutureVlanPortFdbFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortFdbFlush.setStatus("current")


class _FsMIDot1qFutureVlanPortIngressEtherType_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortIngressEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIDot1qFutureVlanPortIngressEtherType_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortIngressEtherType_Object = MibTableColumn
fsMIDot1qFutureVlanPortIngressEtherType = _FsMIDot1qFutureVlanPortIngressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 36),
    _FsMIDot1qFutureVlanPortIngressEtherType_Type()
)
fsMIDot1qFutureVlanPortIngressEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortIngressEtherType.setStatus("current")


class _FsMIDot1qFutureVlanPortEgressEtherType_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortEgressEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FsMIDot1qFutureVlanPortEgressEtherType_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortEgressEtherType_Object = MibTableColumn
fsMIDot1qFutureVlanPortEgressEtherType = _FsMIDot1qFutureVlanPortEgressEtherType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 37),
    _FsMIDot1qFutureVlanPortEgressEtherType_Type()
)
fsMIDot1qFutureVlanPortEgressEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortEgressEtherType.setStatus("current")


class _FsMIDot1qFutureVlanPortEgressTPIDType_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortEgressTPIDType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("portbased", 1),
          ("vlanbased", 2))
    )


_FsMIDot1qFutureVlanPortEgressTPIDType_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortEgressTPIDType_Object = MibTableColumn
fsMIDot1qFutureVlanPortEgressTPIDType = _FsMIDot1qFutureVlanPortEgressTPIDType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 38),
    _FsMIDot1qFutureVlanPortEgressTPIDType_Type()
)
fsMIDot1qFutureVlanPortEgressTPIDType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortEgressTPIDType.setStatus("current")


class _FsMIDot1qFutureVlanPortAllowableTPID1_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortAllowableTPID1 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDot1qFutureVlanPortAllowableTPID1_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortAllowableTPID1_Object = MibTableColumn
fsMIDot1qFutureVlanPortAllowableTPID1 = _FsMIDot1qFutureVlanPortAllowableTPID1_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 39),
    _FsMIDot1qFutureVlanPortAllowableTPID1_Type()
)
fsMIDot1qFutureVlanPortAllowableTPID1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortAllowableTPID1.setStatus("current")


class _FsMIDot1qFutureVlanPortAllowableTPID2_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortAllowableTPID2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDot1qFutureVlanPortAllowableTPID2_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortAllowableTPID2_Object = MibTableColumn
fsMIDot1qFutureVlanPortAllowableTPID2 = _FsMIDot1qFutureVlanPortAllowableTPID2_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 40),
    _FsMIDot1qFutureVlanPortAllowableTPID2_Type()
)
fsMIDot1qFutureVlanPortAllowableTPID2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortAllowableTPID2.setStatus("current")


class _FsMIDot1qFutureVlanPortAllowableTPID3_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortAllowableTPID3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDot1qFutureVlanPortAllowableTPID3_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortAllowableTPID3_Object = MibTableColumn
fsMIDot1qFutureVlanPortAllowableTPID3 = _FsMIDot1qFutureVlanPortAllowableTPID3_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 41),
    _FsMIDot1qFutureVlanPortAllowableTPID3_Type()
)
fsMIDot1qFutureVlanPortAllowableTPID3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortAllowableTPID3.setStatus("current")


class _FsMIDot1qFutureVlanPortClearGarpStats_Type(TruthValue):
    """Custom type fsMIDot1qFutureVlanPortClearGarpStats based on TruthValue"""
    defaultValue = 2


_FsMIDot1qFutureVlanPortClearGarpStats_Type.__name__ = "TruthValue"
_FsMIDot1qFutureVlanPortClearGarpStats_Object = MibTableColumn
fsMIDot1qFutureVlanPortClearGarpStats = _FsMIDot1qFutureVlanPortClearGarpStats_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 42),
    _FsMIDot1qFutureVlanPortClearGarpStats_Type()
)
fsMIDot1qFutureVlanPortClearGarpStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortClearGarpStats.setStatus("current")


class _FsMIDot1qFutureVlanPortUnicastMacSecType_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortUnicastMacSecType based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sav", 1),
          ("shv", 2),
          ("off", 3))
    )


_FsMIDot1qFutureVlanPortUnicastMacSecType_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortUnicastMacSecType_Object = MibTableColumn
fsMIDot1qFutureVlanPortUnicastMacSecType = _FsMIDot1qFutureVlanPortUnicastMacSecType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 43),
    _FsMIDot1qFutureVlanPortUnicastMacSecType_Type()
)
fsMIDot1qFutureVlanPortUnicastMacSecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortUnicastMacSecType.setStatus("current")


class _FsMIDot1qFutureVlanPortStVlanList_Type(OctetString):
    """Custom type fsMIDot1qFutureVlanPortStVlanList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_FsMIDot1qFutureVlanPortStVlanList_Type.__name__ = "OctetString"
_FsMIDot1qFutureVlanPortStVlanList_Object = MibTableColumn
fsMIDot1qFutureVlanPortStVlanList = _FsMIDot1qFutureVlanPortStVlanList_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 44),
    _FsMIDot1qFutureVlanPortStVlanList_Type()
)
fsMIDot1qFutureVlanPortStVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortStVlanList.setStatus("current")


class _FsMIDot1qFutureVlanPortStUntaggedVlan_Type(Unsigned32):
    """Custom type fsMIDot1qFutureVlanPortStUntaggedVlan based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_FsMIDot1qFutureVlanPortStUntaggedVlan_Type.__name__ = "Unsigned32"
_FsMIDot1qFutureVlanPortStUntaggedVlan_Object = MibTableColumn
fsMIDot1qFutureVlanPortStUntaggedVlan = _FsMIDot1qFutureVlanPortStUntaggedVlan_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 45),
    _FsMIDot1qFutureVlanPortStUntaggedVlan_Type()
)
fsMIDot1qFutureVlanPortStUntaggedVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortStUntaggedVlan.setStatus("current")


class _FsMIDot1qFuturePortPacketReflectionStatus_Type(TruthValue):
    """Custom type fsMIDot1qFuturePortPacketReflectionStatus based on TruthValue"""
    defaultValue = 2


_FsMIDot1qFuturePortPacketReflectionStatus_Type.__name__ = "TruthValue"
_FsMIDot1qFuturePortPacketReflectionStatus_Object = MibTableColumn
fsMIDot1qFuturePortPacketReflectionStatus = _FsMIDot1qFuturePortPacketReflectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 3, 1, 46),
    _FsMIDot1qFuturePortPacketReflectionStatus_Type()
)
fsMIDot1qFuturePortPacketReflectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFuturePortPacketReflectionStatus.setStatus("current")
_FsMIDot1qFutureVlanPortMacMapTable_Object = MibTable
fsMIDot1qFutureVlanPortMacMapTable = _FsMIDot1qFutureVlanPortMacMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 4)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortMacMapTable.setStatus("current")
_FsMIDot1qFutureVlanPortMacMapEntry_Object = MibTableRow
fsMIDot1qFutureVlanPortMacMapEntry = _FsMIDot1qFutureVlanPortMacMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 4, 1)
)
fsMIDot1qFutureVlanPortMacMapEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanPort"),
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanPortMacMapAddr"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortMacMapEntry.setStatus("current")
_FsMIDot1qFutureVlanPortMacMapAddr_Type = MacAddress
_FsMIDot1qFutureVlanPortMacMapAddr_Object = MibTableColumn
fsMIDot1qFutureVlanPortMacMapAddr = _FsMIDot1qFutureVlanPortMacMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 4, 1, 1),
    _FsMIDot1qFutureVlanPortMacMapAddr_Type()
)
fsMIDot1qFutureVlanPortMacMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortMacMapAddr.setStatus("current")
_FsMIDot1qFutureVlanPortMacMapVid_Type = VlanId
_FsMIDot1qFutureVlanPortMacMapVid_Object = MibTableColumn
fsMIDot1qFutureVlanPortMacMapVid = _FsMIDot1qFutureVlanPortMacMapVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 4, 1, 2),
    _FsMIDot1qFutureVlanPortMacMapVid_Type()
)
fsMIDot1qFutureVlanPortMacMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortMacMapVid.setStatus("current")
_FsMIDot1qFutureVlanPortMacMapName_Type = DisplayString
_FsMIDot1qFutureVlanPortMacMapName_Object = MibTableColumn
fsMIDot1qFutureVlanPortMacMapName = _FsMIDot1qFutureVlanPortMacMapName_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 4, 1, 3),
    _FsMIDot1qFutureVlanPortMacMapName_Type()
)
fsMIDot1qFutureVlanPortMacMapName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortMacMapName.setStatus("current")


class _FsMIDot1qFutureVlanPortMacMapMcastBcastOption_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortMacMapMcastBcastOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("supress", 2))
    )


_FsMIDot1qFutureVlanPortMacMapMcastBcastOption_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortMacMapMcastBcastOption_Object = MibTableColumn
fsMIDot1qFutureVlanPortMacMapMcastBcastOption = _FsMIDot1qFutureVlanPortMacMapMcastBcastOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 4, 1, 4),
    _FsMIDot1qFutureVlanPortMacMapMcastBcastOption_Type()
)
fsMIDot1qFutureVlanPortMacMapMcastBcastOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortMacMapMcastBcastOption.setStatus("current")
_FsMIDot1qFutureVlanPortMacMapRowStatus_Type = RowStatus
_FsMIDot1qFutureVlanPortMacMapRowStatus_Object = MibTableColumn
fsMIDot1qFutureVlanPortMacMapRowStatus = _FsMIDot1qFutureVlanPortMacMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 4, 1, 5),
    _FsMIDot1qFutureVlanPortMacMapRowStatus_Type()
)
fsMIDot1qFutureVlanPortMacMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortMacMapRowStatus.setStatus("current")
_FsMIDot1qFutureVlanFidMapTable_Object = MibTable
fsMIDot1qFutureVlanFidMapTable = _FsMIDot1qFutureVlanFidMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 5)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanFidMapTable.setStatus("current")
_FsMIDot1qFutureVlanFidMapEntry_Object = MibTableRow
fsMIDot1qFutureVlanFidMapEntry = _FsMIDot1qFutureVlanFidMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 5, 1)
)
fsMIDot1qFutureVlanFidMapEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextId"),
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanIndex"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanFidMapEntry.setStatus("current")


class _FsMIDot1qFutureVlanIndex_Type(Unsigned32):
    """Custom type fsMIDot1qFutureVlanIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIDot1qFutureVlanIndex_Type.__name__ = "Unsigned32"
_FsMIDot1qFutureVlanIndex_Object = MibTableColumn
fsMIDot1qFutureVlanIndex = _FsMIDot1qFutureVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 5, 1, 1),
    _FsMIDot1qFutureVlanIndex_Type()
)
fsMIDot1qFutureVlanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanIndex.setStatus("current")


class _FsMIDot1qFutureVlanFid_Type(Unsigned32):
    """Custom type fsMIDot1qFutureVlanFid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_FsMIDot1qFutureVlanFid_Type.__name__ = "Unsigned32"
_FsMIDot1qFutureVlanFid_Object = MibTableColumn
fsMIDot1qFutureVlanFid = _FsMIDot1qFutureVlanFid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 5, 1, 2),
    _FsMIDot1qFutureVlanFid_Type()
)
fsMIDot1qFutureVlanFid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanFid.setStatus("current")
_FsMIDot1qFutureVlanCounterTable_Object = MibTable
fsMIDot1qFutureVlanCounterTable = _FsMIDot1qFutureVlanCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterTable.setStatus("current")
_FsMIDot1qFutureVlanCounterEntry_Object = MibTableRow
fsMIDot1qFutureVlanCounterEntry = _FsMIDot1qFutureVlanCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1)
)
fsMIDot1qFutureVlanCounterEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextId"),
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanIndex"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterEntry.setStatus("current")
_FsMIDot1qFutureVlanCounterRxUcast_Type = Counter32
_FsMIDot1qFutureVlanCounterRxUcast_Object = MibTableColumn
fsMIDot1qFutureVlanCounterRxUcast = _FsMIDot1qFutureVlanCounterRxUcast_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 1),
    _FsMIDot1qFutureVlanCounterRxUcast_Type()
)
fsMIDot1qFutureVlanCounterRxUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterRxUcast.setStatus("current")
_FsMIDot1qFutureVlanCounterRxMcastBcast_Type = Counter32
_FsMIDot1qFutureVlanCounterRxMcastBcast_Object = MibTableColumn
fsMIDot1qFutureVlanCounterRxMcastBcast = _FsMIDot1qFutureVlanCounterRxMcastBcast_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 2),
    _FsMIDot1qFutureVlanCounterRxMcastBcast_Type()
)
fsMIDot1qFutureVlanCounterRxMcastBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterRxMcastBcast.setStatus("current")
_FsMIDot1qFutureVlanCounterTxUnknUcast_Type = Counter32
_FsMIDot1qFutureVlanCounterTxUnknUcast_Object = MibTableColumn
fsMIDot1qFutureVlanCounterTxUnknUcast = _FsMIDot1qFutureVlanCounterTxUnknUcast_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 3),
    _FsMIDot1qFutureVlanCounterTxUnknUcast_Type()
)
fsMIDot1qFutureVlanCounterTxUnknUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterTxUnknUcast.setStatus("current")
_FsMIDot1qFutureVlanCounterTxUcast_Type = Counter32
_FsMIDot1qFutureVlanCounterTxUcast_Object = MibTableColumn
fsMIDot1qFutureVlanCounterTxUcast = _FsMIDot1qFutureVlanCounterTxUcast_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 4),
    _FsMIDot1qFutureVlanCounterTxUcast_Type()
)
fsMIDot1qFutureVlanCounterTxUcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterTxUcast.setStatus("current")
_FsMIDot1qFutureVlanCounterTxBcast_Type = Counter32
_FsMIDot1qFutureVlanCounterTxBcast_Object = MibTableColumn
fsMIDot1qFutureVlanCounterTxBcast = _FsMIDot1qFutureVlanCounterTxBcast_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 5),
    _FsMIDot1qFutureVlanCounterTxBcast_Type()
)
fsMIDot1qFutureVlanCounterTxBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterTxBcast.setStatus("current")
_FsMIDot1qFutureVlanCounterRxFrames_Type = Counter32
_FsMIDot1qFutureVlanCounterRxFrames_Object = MibTableColumn
fsMIDot1qFutureVlanCounterRxFrames = _FsMIDot1qFutureVlanCounterRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 6),
    _FsMIDot1qFutureVlanCounterRxFrames_Type()
)
fsMIDot1qFutureVlanCounterRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterRxFrames.setStatus("current")
_FsMIDot1qFutureVlanCounterRxBytes_Type = Counter32
_FsMIDot1qFutureVlanCounterRxBytes_Object = MibTableColumn
fsMIDot1qFutureVlanCounterRxBytes = _FsMIDot1qFutureVlanCounterRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 7),
    _FsMIDot1qFutureVlanCounterRxBytes_Type()
)
fsMIDot1qFutureVlanCounterRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterRxBytes.setStatus("current")
_FsMIDot1qFutureVlanCounterTxFrames_Type = Counter32
_FsMIDot1qFutureVlanCounterTxFrames_Object = MibTableColumn
fsMIDot1qFutureVlanCounterTxFrames = _FsMIDot1qFutureVlanCounterTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 8),
    _FsMIDot1qFutureVlanCounterTxFrames_Type()
)
fsMIDot1qFutureVlanCounterTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterTxFrames.setStatus("current")
_FsMIDot1qFutureVlanCounterTxBytes_Type = Counter32
_FsMIDot1qFutureVlanCounterTxBytes_Object = MibTableColumn
fsMIDot1qFutureVlanCounterTxBytes = _FsMIDot1qFutureVlanCounterTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 9),
    _FsMIDot1qFutureVlanCounterTxBytes_Type()
)
fsMIDot1qFutureVlanCounterTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterTxBytes.setStatus("current")
_FsMIDot1qFutureVlanCounterDiscardFrames_Type = Counter32
_FsMIDot1qFutureVlanCounterDiscardFrames_Object = MibTableColumn
fsMIDot1qFutureVlanCounterDiscardFrames = _FsMIDot1qFutureVlanCounterDiscardFrames_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 10),
    _FsMIDot1qFutureVlanCounterDiscardFrames_Type()
)
fsMIDot1qFutureVlanCounterDiscardFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterDiscardFrames.setStatus("current")
_FsMIDot1qFutureVlanCounterDiscardBytes_Type = Counter32
_FsMIDot1qFutureVlanCounterDiscardBytes_Object = MibTableColumn
fsMIDot1qFutureVlanCounterDiscardBytes = _FsMIDot1qFutureVlanCounterDiscardBytes_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 11),
    _FsMIDot1qFutureVlanCounterDiscardBytes_Type()
)
fsMIDot1qFutureVlanCounterDiscardBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterDiscardBytes.setStatus("current")


class _FsMIDot1qFutureVlanCounterStatus_Type(EnabledStatus):
    """Custom type fsMIDot1qFutureVlanCounterStatus based on EnabledStatus"""
    defaultValue = 2


_FsMIDot1qFutureVlanCounterStatus_Type.__name__ = "EnabledStatus"
_FsMIDot1qFutureVlanCounterStatus_Object = MibTableColumn
fsMIDot1qFutureVlanCounterStatus = _FsMIDot1qFutureVlanCounterStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 6, 1, 12),
    _FsMIDot1qFutureVlanCounterStatus_Type()
)
fsMIDot1qFutureVlanCounterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanCounterStatus.setStatus("current")
_FsMIDot1qFutureVlanUnicastMacControlTable_Object = MibTable
fsMIDot1qFutureVlanUnicastMacControlTable = _FsMIDot1qFutureVlanUnicastMacControlTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 7)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanUnicastMacControlTable.setStatus("current")
_FsMIDot1qFutureVlanUnicastMacControlEntry_Object = MibTableRow
fsMIDot1qFutureVlanUnicastMacControlEntry = _FsMIDot1qFutureVlanUnicastMacControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 7, 1)
)
fsMIDot1qFutureVlanUnicastMacControlEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextId"),
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanIndex"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanUnicastMacControlEntry.setStatus("current")


class _FsMIDot1qFutureVlanUnicastMacLimit_Type(Unsigned32):
    """Custom type fsMIDot1qFutureVlanUnicastMacLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_FsMIDot1qFutureVlanUnicastMacLimit_Type.__name__ = "Unsigned32"
_FsMIDot1qFutureVlanUnicastMacLimit_Object = MibTableColumn
fsMIDot1qFutureVlanUnicastMacLimit = _FsMIDot1qFutureVlanUnicastMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 7, 1, 1),
    _FsMIDot1qFutureVlanUnicastMacLimit_Type()
)
fsMIDot1qFutureVlanUnicastMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanUnicastMacLimit.setStatus("current")


class _FsMIDot1qFutureVlanAdminMacLearningStatus_Type(MacLearningStatus):
    """Custom type fsMIDot1qFutureVlanAdminMacLearningStatus based on MacLearningStatus"""
    defaultValue = 3


_FsMIDot1qFutureVlanAdminMacLearningStatus_Type.__name__ = "MacLearningStatus"
_FsMIDot1qFutureVlanAdminMacLearningStatus_Object = MibTableColumn
fsMIDot1qFutureVlanAdminMacLearningStatus = _FsMIDot1qFutureVlanAdminMacLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 7, 1, 2),
    _FsMIDot1qFutureVlanAdminMacLearningStatus_Type()
)
fsMIDot1qFutureVlanAdminMacLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanAdminMacLearningStatus.setStatus("current")
_FsMIDot1qFutureVlanOperMacLearningStatus_Type = EnabledStatus
_FsMIDot1qFutureVlanOperMacLearningStatus_Object = MibTableColumn
fsMIDot1qFutureVlanOperMacLearningStatus = _FsMIDot1qFutureVlanOperMacLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 7, 1, 3),
    _FsMIDot1qFutureVlanOperMacLearningStatus_Type()
)
fsMIDot1qFutureVlanOperMacLearningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanOperMacLearningStatus.setStatus("current")
_FsMIDot1qFutureGarpGlobalTrace_Type = TruthValue
_FsMIDot1qFutureGarpGlobalTrace_Object = MibScalar
fsMIDot1qFutureGarpGlobalTrace = _FsMIDot1qFutureGarpGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 8),
    _FsMIDot1qFutureGarpGlobalTrace_Type()
)
fsMIDot1qFutureGarpGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureGarpGlobalTrace.setStatus("current")
_FsMIDot1qFutureVlanTpFdbTable_Object = MibTable
fsMIDot1qFutureVlanTpFdbTable = _FsMIDot1qFutureVlanTpFdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 9)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTpFdbTable.setStatus("current")
_FsMIDot1qFutureVlanTpFdbEntry_Object = MibTableRow
fsMIDot1qFutureVlanTpFdbEntry = _FsMIDot1qFutureVlanTpFdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 9, 1)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTpFdbEntry.setStatus("current")


class _FsMIDot1qFutureVlanOldTpFdbPort_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanOldTpFdbPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDot1qFutureVlanOldTpFdbPort_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanOldTpFdbPort_Object = MibTableColumn
fsMIDot1qFutureVlanOldTpFdbPort = _FsMIDot1qFutureVlanOldTpFdbPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 9, 1, 1),
    _FsMIDot1qFutureVlanOldTpFdbPort_Type()
)
fsMIDot1qFutureVlanOldTpFdbPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanOldTpFdbPort.setStatus("current")
_FsMIDot1qFutureConnectionIdentifier_Type = MacAddress
_FsMIDot1qFutureConnectionIdentifier_Object = MibTableColumn
fsMIDot1qFutureConnectionIdentifier = _FsMIDot1qFutureConnectionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 9, 1, 2),
    _FsMIDot1qFutureConnectionIdentifier_Type()
)
fsMIDot1qFutureConnectionIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureConnectionIdentifier.setStatus("current")
_FsMIDot1qFutureVlanWildCardTable_Object = MibTable
fsMIDot1qFutureVlanWildCardTable = _FsMIDot1qFutureVlanWildCardTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 10)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanWildCardTable.setStatus("current")
_FsMIDot1qFutureVlanWildCardEntry_Object = MibTableRow
fsMIDot1qFutureVlanWildCardEntry = _FsMIDot1qFutureVlanWildCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 10, 1)
)
fsMIDot1qFutureVlanWildCardEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextId"),
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanWildCardMacAddress"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanWildCardEntry.setStatus("current")
_FsMIDot1qFutureVlanWildCardMacAddress_Type = MacAddress
_FsMIDot1qFutureVlanWildCardMacAddress_Object = MibTableColumn
fsMIDot1qFutureVlanWildCardMacAddress = _FsMIDot1qFutureVlanWildCardMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 10, 1, 1),
    _FsMIDot1qFutureVlanWildCardMacAddress_Type()
)
fsMIDot1qFutureVlanWildCardMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanWildCardMacAddress.setStatus("current")
_FsMIDot1qFutureVlanWildCardRowStatus_Type = RowStatus
_FsMIDot1qFutureVlanWildCardRowStatus_Object = MibTableColumn
fsMIDot1qFutureVlanWildCardRowStatus = _FsMIDot1qFutureVlanWildCardRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 10, 1, 2),
    _FsMIDot1qFutureVlanWildCardRowStatus_Type()
)
fsMIDot1qFutureVlanWildCardRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanWildCardRowStatus.setStatus("current")
_FsMIDot1qFutureVlanWildCardPortTable_Object = MibTable
fsMIDot1qFutureVlanWildCardPortTable = _FsMIDot1qFutureVlanWildCardPortTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 11)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanWildCardPortTable.setStatus("current")
_FsMIDot1qFutureVlanWildCardPortEntry_Object = MibTableRow
fsMIDot1qFutureVlanWildCardPortEntry = _FsMIDot1qFutureVlanWildCardPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 11, 1)
)
fsMIDot1qFutureVlanWildCardPortEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextId"),
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanWildCardMacAddress"),
    (0, "ARICENTQ-BRIDGE-MIB", "fsDot1qTpPort"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanWildCardPortEntry.setStatus("current")
_FsMIDot1qFutureVlanIsWildCardEgressPort_Type = TruthValue
_FsMIDot1qFutureVlanIsWildCardEgressPort_Object = MibTableColumn
fsMIDot1qFutureVlanIsWildCardEgressPort = _FsMIDot1qFutureVlanIsWildCardEgressPort_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 11, 1, 1),
    _FsMIDot1qFutureVlanIsWildCardEgressPort_Type()
)
fsMIDot1qFutureVlanIsWildCardEgressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanIsWildCardEgressPort.setStatus("current")
_FsMIDot1qFutureStaticUnicastExtnTable_Object = MibTable
fsMIDot1qFutureStaticUnicastExtnTable = _FsMIDot1qFutureStaticUnicastExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 12)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureStaticUnicastExtnTable.setStatus("current")
_FsMIDot1qFutureStaticUnicastExtnEntry_Object = MibTableRow
fsMIDot1qFutureStaticUnicastExtnEntry = _FsMIDot1qFutureStaticUnicastExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 12, 1)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureStaticUnicastExtnEntry.setStatus("current")
_FsMIDot1qFutureStaticConnectionIdentifier_Type = MacAddress
_FsMIDot1qFutureStaticConnectionIdentifier_Object = MibTableColumn
fsMIDot1qFutureStaticConnectionIdentifier = _FsMIDot1qFutureStaticConnectionIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 12, 1, 1),
    _FsMIDot1qFutureStaticConnectionIdentifier_Type()
)
fsMIDot1qFutureStaticConnectionIdentifier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureStaticConnectionIdentifier.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapTable_Object = MibTable
fsMIDot1qFutureVlanPortSubnetMapTable = _FsMIDot1qFutureVlanPortSubnetMapTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 13)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapTable.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapEntry_Object = MibTableRow
fsMIDot1qFutureVlanPortSubnetMapEntry = _FsMIDot1qFutureVlanPortSubnetMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 13, 1)
)
fsMIDot1qFutureVlanPortSubnetMapEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanPort"),
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanPortSubnetMapAddr"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapEntry.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapAddr_Type = IpAddress
_FsMIDot1qFutureVlanPortSubnetMapAddr_Object = MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapAddr = _FsMIDot1qFutureVlanPortSubnetMapAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 13, 1, 1),
    _FsMIDot1qFutureVlanPortSubnetMapAddr_Type()
)
fsMIDot1qFutureVlanPortSubnetMapAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapAddr.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapVid_Type = VlanId
_FsMIDot1qFutureVlanPortSubnetMapVid_Object = MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapVid = _FsMIDot1qFutureVlanPortSubnetMapVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 13, 1, 2),
    _FsMIDot1qFutureVlanPortSubnetMapVid_Type()
)
fsMIDot1qFutureVlanPortSubnetMapVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapVid.setStatus("current")


class _FsMIDot1qFutureVlanPortSubnetMapARPOption_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortSubnetMapARPOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("suppress", 2))
    )


_FsMIDot1qFutureVlanPortSubnetMapARPOption_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortSubnetMapARPOption_Object = MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapARPOption = _FsMIDot1qFutureVlanPortSubnetMapARPOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 13, 1, 3),
    _FsMIDot1qFutureVlanPortSubnetMapARPOption_Type()
)
fsMIDot1qFutureVlanPortSubnetMapARPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapARPOption.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapRowStatus_Type = RowStatus
_FsMIDot1qFutureVlanPortSubnetMapRowStatus_Object = MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapRowStatus = _FsMIDot1qFutureVlanPortSubnetMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 13, 1, 4),
    _FsMIDot1qFutureVlanPortSubnetMapRowStatus_Type()
)
fsMIDot1qFutureVlanPortSubnetMapRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapRowStatus.setStatus("current")
_FsMIDot1qFutureVlanSwStatsEnabled_Type = TruthValue
_FsMIDot1qFutureVlanSwStatsEnabled_Object = MibScalar
fsMIDot1qFutureVlanSwStatsEnabled = _FsMIDot1qFutureVlanSwStatsEnabled_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 14),
    _FsMIDot1qFutureVlanSwStatsEnabled_Type()
)
fsMIDot1qFutureVlanSwStatsEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanSwStatsEnabled.setStatus("current")
_FsMIDot1qFutureStVlanExtTable_Object = MibTable
fsMIDot1qFutureStVlanExtTable = _FsMIDot1qFutureStVlanExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 15)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureStVlanExtTable.setStatus("current")
_FsMIDot1qFutureStVlanExtEntry_Object = MibTableRow
fsMIDot1qFutureStVlanExtEntry = _FsMIDot1qFutureStVlanExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 15, 1)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureStVlanExtEntry.setStatus("current")


class _FsMIDot1qFutureStVlanPVlanType_Type(Integer32):
    """Custom type fsMIDot1qFutureStVlanPVlanType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("primary", 2),
          ("isolated", 3),
          ("community", 4))
    )


_FsMIDot1qFutureStVlanPVlanType_Type.__name__ = "Integer32"
_FsMIDot1qFutureStVlanPVlanType_Object = MibTableColumn
fsMIDot1qFutureStVlanPVlanType = _FsMIDot1qFutureStVlanPVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 15, 1, 1),
    _FsMIDot1qFutureStVlanPVlanType_Type()
)
fsMIDot1qFutureStVlanPVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureStVlanPVlanType.setStatus("current")


class _FsMIDot1qFutureStVlanPrimaryVid_Type(VlanIdOrNone):
    """Custom type fsMIDot1qFutureStVlanPrimaryVid based on VlanIdOrNone"""
    defaultValue = 0


_FsMIDot1qFutureStVlanPrimaryVid_Type.__name__ = "VlanIdOrNone"
_FsMIDot1qFutureStVlanPrimaryVid_Object = MibTableColumn
fsMIDot1qFutureStVlanPrimaryVid = _FsMIDot1qFutureStVlanPrimaryVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 15, 1, 2),
    _FsMIDot1qFutureStVlanPrimaryVid_Type()
)
fsMIDot1qFutureStVlanPrimaryVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureStVlanPrimaryVid.setStatus("current")


class _FsMIDot1qFutureStVlanFdbFlush_Type(TruthValue):
    """Custom type fsMIDot1qFutureStVlanFdbFlush based on TruthValue"""
    defaultValue = 2


_FsMIDot1qFutureStVlanFdbFlush_Type.__name__ = "TruthValue"
_FsMIDot1qFutureStVlanFdbFlush_Object = MibTableColumn
fsMIDot1qFutureStVlanFdbFlush = _FsMIDot1qFutureStVlanFdbFlush_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 15, 1, 3),
    _FsMIDot1qFutureStVlanFdbFlush_Type()
)
fsMIDot1qFutureStVlanFdbFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureStVlanFdbFlush.setStatus("current")


class _FsMIDot1qFutureStVlanEgressEthertype_Type(Integer32):
    """Custom type fsMIDot1qFutureStVlanEgressEthertype based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIDot1qFutureStVlanEgressEthertype_Type.__name__ = "Integer32"
_FsMIDot1qFutureStVlanEgressEthertype_Object = MibTableColumn
fsMIDot1qFutureStVlanEgressEthertype = _FsMIDot1qFutureStVlanEgressEthertype_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 15, 1, 4),
    _FsMIDot1qFutureStVlanEgressEthertype_Type()
)
fsMIDot1qFutureStVlanEgressEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureStVlanEgressEthertype.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapExtTable_Object = MibTable
fsMIDot1qFutureVlanPortSubnetMapExtTable = _FsMIDot1qFutureVlanPortSubnetMapExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 16)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapExtTable.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapExtEntry_Object = MibTableRow
fsMIDot1qFutureVlanPortSubnetMapExtEntry = _FsMIDot1qFutureVlanPortSubnetMapExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 16, 1)
)
fsMIDot1qFutureVlanPortSubnetMapExtEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanPort"),
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanPortSubnetMapExtAddr"),
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanPortSubnetMapExtMask"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapExtEntry.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapExtAddr_Type = IpAddress
_FsMIDot1qFutureVlanPortSubnetMapExtAddr_Object = MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapExtAddr = _FsMIDot1qFutureVlanPortSubnetMapExtAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 16, 1, 1),
    _FsMIDot1qFutureVlanPortSubnetMapExtAddr_Type()
)
fsMIDot1qFutureVlanPortSubnetMapExtAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapExtAddr.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapExtMask_Type = IpAddress
_FsMIDot1qFutureVlanPortSubnetMapExtMask_Object = MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapExtMask = _FsMIDot1qFutureVlanPortSubnetMapExtMask_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 16, 1, 2),
    _FsMIDot1qFutureVlanPortSubnetMapExtMask_Type()
)
fsMIDot1qFutureVlanPortSubnetMapExtMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapExtMask.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapExtVid_Type = VlanId
_FsMIDot1qFutureVlanPortSubnetMapExtVid_Object = MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapExtVid = _FsMIDot1qFutureVlanPortSubnetMapExtVid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 16, 1, 3),
    _FsMIDot1qFutureVlanPortSubnetMapExtVid_Type()
)
fsMIDot1qFutureVlanPortSubnetMapExtVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapExtVid.setStatus("current")


class _FsMIDot1qFutureVlanPortSubnetMapExtARPOption_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanPortSubnetMapExtARPOption based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("suppress", 2))
    )


_FsMIDot1qFutureVlanPortSubnetMapExtARPOption_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanPortSubnetMapExtARPOption_Object = MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapExtARPOption = _FsMIDot1qFutureVlanPortSubnetMapExtARPOption_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 16, 1, 4),
    _FsMIDot1qFutureVlanPortSubnetMapExtARPOption_Type()
)
fsMIDot1qFutureVlanPortSubnetMapExtARPOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapExtARPOption.setStatus("current")
_FsMIDot1qFutureVlanPortSubnetMapExtRowStatus_Type = RowStatus
_FsMIDot1qFutureVlanPortSubnetMapExtRowStatus_Object = MibTableColumn
fsMIDot1qFutureVlanPortSubnetMapExtRowStatus = _FsMIDot1qFutureVlanPortSubnetMapExtRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 16, 1, 5),
    _FsMIDot1qFutureVlanPortSubnetMapExtRowStatus_Type()
)
fsMIDot1qFutureVlanPortSubnetMapExtRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanPortSubnetMapExtRowStatus.setStatus("current")
_FsMIDot1qFuturePortVlanExtTable_Object = MibTable
fsMIDot1qFuturePortVlanExtTable = _FsMIDot1qFuturePortVlanExtTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 17)
)
if mibBuilder.loadTexts:
    fsMIDot1qFuturePortVlanExtTable.setStatus("current")
_FsMIDot1qFuturePortVlanExtEntry_Object = MibTableRow
fsMIDot1qFuturePortVlanExtEntry = _FsMIDot1qFuturePortVlanExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 17, 1)
)
if mibBuilder.loadTexts:
    fsMIDot1qFuturePortVlanExtEntry.setStatus("current")


class _FsMIDot1qFuturePortVlanFdbFlush_Type(TruthValue):
    """Custom type fsMIDot1qFuturePortVlanFdbFlush based on TruthValue"""
    defaultValue = 2


_FsMIDot1qFuturePortVlanFdbFlush_Type.__name__ = "TruthValue"
_FsMIDot1qFuturePortVlanFdbFlush_Object = MibTableColumn
fsMIDot1qFuturePortVlanFdbFlush = _FsMIDot1qFuturePortVlanFdbFlush_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 17, 1, 1),
    _FsMIDot1qFuturePortVlanFdbFlush_Type()
)
fsMIDot1qFuturePortVlanFdbFlush.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFuturePortVlanFdbFlush.setStatus("current")
_FsMIDot1qFutureVlanLoopbackTable_Object = MibTable
fsMIDot1qFutureVlanLoopbackTable = _FsMIDot1qFutureVlanLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 18)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanLoopbackTable.setStatus("current")
_FsMIDot1qFutureVlanLoopbackEntry_Object = MibTableRow
fsMIDot1qFutureVlanLoopbackEntry = _FsMIDot1qFutureVlanLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 18, 1)
)
fsMIDot1qFutureVlanLoopbackEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextId"),
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanIndex"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanLoopbackEntry.setStatus("current")


class _FsMIDot1qFutureVlanLoopbackStatus_Type(EnabledStatus):
    """Custom type fsMIDot1qFutureVlanLoopbackStatus based on EnabledStatus"""
    defaultValue = 2


_FsMIDot1qFutureVlanLoopbackStatus_Type.__name__ = "EnabledStatus"
_FsMIDot1qFutureVlanLoopbackStatus_Object = MibTableColumn
fsMIDot1qFutureVlanLoopbackStatus = _FsMIDot1qFutureVlanLoopbackStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 1, 18, 1, 1),
    _FsMIDot1qFutureVlanLoopbackStatus_Type()
)
fsMIDot1qFutureVlanLoopbackStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanLoopbackStatus.setStatus("current")
_FsMIDot1qFutureVlanTunnelConfig_ObjectIdentity = ObjectIdentity
fsMIDot1qFutureVlanTunnelConfig = _FsMIDot1qFutureVlanTunnelConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2)
)
_FsMIDot1qFutureVlanTunnelConfigTable_Object = MibTable
fsMIDot1qFutureVlanTunnelConfigTable = _FsMIDot1qFutureVlanTunnelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 1)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelConfigTable.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelConfigEntry_Object = MibTableRow
fsMIDot1qFutureVlanTunnelConfigEntry = _FsMIDot1qFutureVlanTunnelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 1, 1)
)
fsMIDot1qFutureVlanTunnelConfigEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextId"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelConfigEntry.setStatus("deprecated")


class _FsMIDot1qFutureVlanBridgeMode_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanBridgeMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("customerBridge", 1),
          ("providerBridge", 2),
          ("providerCoreBridge", 3),
          ("providerEdgeBridge", 4),
          ("invalidBridgeMode", 5))
    )


_FsMIDot1qFutureVlanBridgeMode_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanBridgeMode_Object = MibTableColumn
fsMIDot1qFutureVlanBridgeMode = _FsMIDot1qFutureVlanBridgeMode_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 1, 1, 1),
    _FsMIDot1qFutureVlanBridgeMode_Type()
)
fsMIDot1qFutureVlanBridgeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanBridgeMode.setStatus("deprecated")


class _FsMIDot1qFutureVlanTunnelBpduPri_Type(Integer32):
    """Custom type fsMIDot1qFutureVlanTunnelBpduPri based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_FsMIDot1qFutureVlanTunnelBpduPri_Type.__name__ = "Integer32"
_FsMIDot1qFutureVlanTunnelBpduPri_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelBpduPri = _FsMIDot1qFutureVlanTunnelBpduPri_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 1, 1, 2),
    _FsMIDot1qFutureVlanTunnelBpduPri_Type()
)
fsMIDot1qFutureVlanTunnelBpduPri.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelBpduPri.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelTable_Object = MibTable
fsMIDot1qFutureVlanTunnelTable = _FsMIDot1qFutureVlanTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 2)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelTable.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelEntry_Object = MibTableRow
fsMIDot1qFutureVlanTunnelEntry = _FsMIDot1qFutureVlanTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 2, 1)
)
fsMIDot1qFutureVlanTunnelEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanPort"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelEntry.setStatus("deprecated")


class _FsMIDot1qFutureVlanTunnelStatus_Type(EnabledStatus):
    """Custom type fsMIDot1qFutureVlanTunnelStatus based on EnabledStatus"""
    defaultValue = 2


_FsMIDot1qFutureVlanTunnelStatus_Type.__name__ = "EnabledStatus"
_FsMIDot1qFutureVlanTunnelStatus_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelStatus = _FsMIDot1qFutureVlanTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 2, 1, 1),
    _FsMIDot1qFutureVlanTunnelStatus_Type()
)
fsMIDot1qFutureVlanTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelStatus.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelProtocolTable_Object = MibTable
fsMIDot1qFutureVlanTunnelProtocolTable = _FsMIDot1qFutureVlanTunnelProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3)
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelProtocolTable.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelProtocolEntry_Object = MibTableRow
fsMIDot1qFutureVlanTunnelProtocolEntry = _FsMIDot1qFutureVlanTunnelProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3, 1)
)
fsMIDot1qFutureVlanTunnelProtocolEntry.setIndexNames(
    (0, "AricentMIVlan-MIB", "fsMIDot1qFutureVlanPort"),
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelProtocolEntry.setStatus("deprecated")


class _FsMIDot1qFutureVlanTunnelStpPDUs_Type(EnabledStatus):
    """Custom type fsMIDot1qFutureVlanTunnelStpPDUs based on EnabledStatus"""
    defaultValue = 2


_FsMIDot1qFutureVlanTunnelStpPDUs_Type.__name__ = "EnabledStatus"
_FsMIDot1qFutureVlanTunnelStpPDUs_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelStpPDUs = _FsMIDot1qFutureVlanTunnelStpPDUs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3, 1, 1),
    _FsMIDot1qFutureVlanTunnelStpPDUs_Type()
)
fsMIDot1qFutureVlanTunnelStpPDUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelStpPDUs.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelStpPDUsRecvd_Type = Counter32
_FsMIDot1qFutureVlanTunnelStpPDUsRecvd_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelStpPDUsRecvd = _FsMIDot1qFutureVlanTunnelStpPDUsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3, 1, 2),
    _FsMIDot1qFutureVlanTunnelStpPDUsRecvd_Type()
)
fsMIDot1qFutureVlanTunnelStpPDUsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelStpPDUsRecvd.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelStpPDUsSent_Type = Counter32
_FsMIDot1qFutureVlanTunnelStpPDUsSent_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelStpPDUsSent = _FsMIDot1qFutureVlanTunnelStpPDUsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3, 1, 3),
    _FsMIDot1qFutureVlanTunnelStpPDUsSent_Type()
)
fsMIDot1qFutureVlanTunnelStpPDUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelStpPDUsSent.setStatus("deprecated")


class _FsMIDot1qFutureVlanTunnelGvrpPDUs_Type(EnabledStatus):
    """Custom type fsMIDot1qFutureVlanTunnelGvrpPDUs based on EnabledStatus"""
    defaultValue = 1


_FsMIDot1qFutureVlanTunnelGvrpPDUs_Type.__name__ = "EnabledStatus"
_FsMIDot1qFutureVlanTunnelGvrpPDUs_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelGvrpPDUs = _FsMIDot1qFutureVlanTunnelGvrpPDUs_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3, 1, 4),
    _FsMIDot1qFutureVlanTunnelGvrpPDUs_Type()
)
fsMIDot1qFutureVlanTunnelGvrpPDUs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelGvrpPDUs.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelGvrpPDUsRecvd_Type = Counter32
_FsMIDot1qFutureVlanTunnelGvrpPDUsRecvd_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelGvrpPDUsRecvd = _FsMIDot1qFutureVlanTunnelGvrpPDUsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3, 1, 5),
    _FsMIDot1qFutureVlanTunnelGvrpPDUsRecvd_Type()
)
fsMIDot1qFutureVlanTunnelGvrpPDUsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelGvrpPDUsRecvd.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelGvrpPDUsSent_Type = Counter32
_FsMIDot1qFutureVlanTunnelGvrpPDUsSent_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelGvrpPDUsSent = _FsMIDot1qFutureVlanTunnelGvrpPDUsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3, 1, 6),
    _FsMIDot1qFutureVlanTunnelGvrpPDUsSent_Type()
)
fsMIDot1qFutureVlanTunnelGvrpPDUsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelGvrpPDUsSent.setStatus("deprecated")


class _FsMIDot1qFutureVlanTunnelIgmpPkts_Type(EnabledStatus):
    """Custom type fsMIDot1qFutureVlanTunnelIgmpPkts based on EnabledStatus"""
    defaultValue = 1


_FsMIDot1qFutureVlanTunnelIgmpPkts_Type.__name__ = "EnabledStatus"
_FsMIDot1qFutureVlanTunnelIgmpPkts_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelIgmpPkts = _FsMIDot1qFutureVlanTunnelIgmpPkts_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3, 1, 7),
    _FsMIDot1qFutureVlanTunnelIgmpPkts_Type()
)
fsMIDot1qFutureVlanTunnelIgmpPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelIgmpPkts.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelIgmpPktsRecvd_Type = Counter32
_FsMIDot1qFutureVlanTunnelIgmpPktsRecvd_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelIgmpPktsRecvd = _FsMIDot1qFutureVlanTunnelIgmpPktsRecvd_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3, 1, 8),
    _FsMIDot1qFutureVlanTunnelIgmpPktsRecvd_Type()
)
fsMIDot1qFutureVlanTunnelIgmpPktsRecvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelIgmpPktsRecvd.setStatus("deprecated")
_FsMIDot1qFutureVlanTunnelIgmpPktsSent_Type = Counter32
_FsMIDot1qFutureVlanTunnelIgmpPktsSent_Object = MibTableColumn
fsMIDot1qFutureVlanTunnelIgmpPktsSent = _FsMIDot1qFutureVlanTunnelIgmpPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 2076, 120, 2, 3, 1, 9),
    _FsMIDot1qFutureVlanTunnelIgmpPktsSent_Type()
)
fsMIDot1qFutureVlanTunnelIgmpPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIDot1qFutureVlanTunnelIgmpPktsSent.setStatus("deprecated")
_FsMIDot1qFutureVlanTraps_ObjectIdentity = ObjectIdentity
fsMIDot1qFutureVlanTraps = _FsMIDot1qFutureVlanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 120, 3)
)
_FsMIDot1qVlanTraps_ObjectIdentity = ObjectIdentity
fsMIDot1qVlanTraps = _FsMIDot1qVlanTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 120, 3, 0)
)
_FsMIDot1qFutureVlanTrapControl_ObjectIdentity = ObjectIdentity
fsMIDot1qFutureVlanTrapControl = _FsMIDot1qFutureVlanTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 120, 4)
)
fsDot1qTpFdbEntry.registerAugmentions(
    ("AricentMIVlan-MIB",
     "fsMIDot1qFutureVlanTpFdbEntry")
)
fsMIDot1qFutureVlanTpFdbEntry.setIndexNames(*fsDot1qTpFdbEntry.getIndexNames())
fsDot1qStaticUnicastEntry.registerAugmentions(
    ("AricentMIVlan-MIB",
     "fsMIDot1qFutureStaticUnicastExtnEntry")
)
fsMIDot1qFutureStaticUnicastExtnEntry.setIndexNames(*fsDot1qStaticUnicastEntry.getIndexNames())
fsDot1qVlanStaticEntry.registerAugmentions(
    ("AricentMIVlan-MIB",
     "fsMIDot1qFutureStVlanExtEntry")
)
fsMIDot1qFutureStVlanExtEntry.setIndexNames(*fsDot1qVlanStaticEntry.getIndexNames())
fsDot1qVlanStaticPortConfigEntry.registerAugmentions(
    ("AricentMIVlan-MIB",
     "fsMIDot1qFuturePortVlanExtEntry")
)
fsMIDot1qFuturePortVlanExtEntry.setIndexNames(*fsDot1qVlanStaticPortConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

fsMIDot1qFutureMacThresholdTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 120, 3, 0, 1)
)
fsMIDot1qFutureMacThresholdTrap.setObjects(
      *(("AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextName"),
        ("AricentMIVlan-MIB", "fsMIDot1qFutureVlanIndex"),
        ("AricentMIVlan-MIB", "fsMIDot1qFutureVlanUnicastMacLimit"))
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureMacThresholdTrap.setStatus(
        "current"
    )

fsMIDot1qFutureSrcRelearnTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 120, 3, 0, 2)
)
fsMIDot1qFutureSrcRelearnTrap.setObjects(
      *(("AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextName"),
        ("AricentMIVlan-MIB", "fsMIDot1qFutureVlanFid"),
        ("ARICENTQ-BRIDGE-MIB", "fsDot1qTpFdbPort"),
        ("AricentMIVlan-MIB", "fsMIDot1qFutureVlanOldTpFdbPort"))
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureSrcRelearnTrap.setStatus(
        "current"
    )

fsMIDot1qFutureSwitchMacLimitTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 2076, 120, 3, 0, 3)
)
fsMIDot1qFutureSwitchMacLimitTrap.setObjects(
      *(("AricentMIVlan-MIB", "fsMIDot1qFutureVlanContextName"),
        ("AricentMIVlan-MIB", "fsMIDot1qFutureUnicastMacLearningLimit"))
)
if mibBuilder.loadTexts:
    fsMIDot1qFutureSwitchMacLimitTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AricentMIVlan-MIB",
    **{"VlanId": VlanId,
       "EnabledStatus": EnabledStatus,
       "MacLearningStatus": MacLearningStatus,
       "futureMIVlanMIB": futureMIVlanMIB,
       "fsMIDot1qFutureVlan": fsMIDot1qFutureVlan,
       "fsMIDot1qFutureVlanGlobalTrace": fsMIDot1qFutureVlanGlobalTrace,
       "fsMIDot1qFutureVlanGlobalsTable": fsMIDot1qFutureVlanGlobalsTable,
       "fsMIDot1qFutureVlanGlobalsEntry": fsMIDot1qFutureVlanGlobalsEntry,
       "fsMIDot1qFutureVlanContextId": fsMIDot1qFutureVlanContextId,
       "fsMIDot1qFutureVlanStatus": fsMIDot1qFutureVlanStatus,
       "fsMIDot1qFutureVlanMacBasedOnAllPorts": fsMIDot1qFutureVlanMacBasedOnAllPorts,
       "fsMIDot1qFutureVlanPortProtoBasedOnAllPorts": fsMIDot1qFutureVlanPortProtoBasedOnAllPorts,
       "fsMIDot1qFutureVlanShutdownStatus": fsMIDot1qFutureVlanShutdownStatus,
       "fsMIDot1qFutureGarpShutdownStatus": fsMIDot1qFutureGarpShutdownStatus,
       "fsMIDot1qFutureVlanDebug": fsMIDot1qFutureVlanDebug,
       "fsMIDot1qFutureVlanLearningMode": fsMIDot1qFutureVlanLearningMode,
       "fsMIDot1qFutureVlanHybridTypeDefault": fsMIDot1qFutureVlanHybridTypeDefault,
       "fsMIDot1qFutureVlanOperStatus": fsMIDot1qFutureVlanOperStatus,
       "fsMIDot1qFutureGvrpOperStatus": fsMIDot1qFutureGvrpOperStatus,
       "fsMIDot1qFutureGmrpOperStatus": fsMIDot1qFutureGmrpOperStatus,
       "fsMIDot1qFutureVlanContextName": fsMIDot1qFutureVlanContextName,
       "fsMIDot1qFutureGarpDebug": fsMIDot1qFutureGarpDebug,
       "fsMIDot1qFutureUnicastMacLearningLimit": fsMIDot1qFutureUnicastMacLearningLimit,
       "fsMIDot1qFutureBaseBridgeMode": fsMIDot1qFutureBaseBridgeMode,
       "fsMIDot1qFutureVlanSubnetBasedOnAllPorts": fsMIDot1qFutureVlanSubnetBasedOnAllPorts,
       "fsMIDot1qFutureVlanGlobalMacLearningStatus": fsMIDot1qFutureVlanGlobalMacLearningStatus,
       "fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria": fsMIDot1qFutureVlanApplyEnhancedFilteringCriteria,
       "fsMIDot1qFutureVlanGlobalsFdbFlush": fsMIDot1qFutureVlanGlobalsFdbFlush,
       "fsMIDot1qFutureVlanUserDefinedTPID": fsMIDot1qFutureVlanUserDefinedTPID,
       "fsMIDot1qFutureVlanRemoteFdbFlush": fsMIDot1qFutureVlanRemoteFdbFlush,
       "fsMIDot1qFutureVlanPortTable": fsMIDot1qFutureVlanPortTable,
       "fsMIDot1qFutureVlanPortEntry": fsMIDot1qFutureVlanPortEntry,
       "fsMIDot1qFutureVlanPort": fsMIDot1qFutureVlanPort,
       "fsMIDot1qFutureVlanPortType": fsMIDot1qFutureVlanPortType,
       "fsMIDot1qFutureVlanPortMacBasedClassification": fsMIDot1qFutureVlanPortMacBasedClassification,
       "fsMIDot1qFutureVlanPortPortProtoBasedClassification": fsMIDot1qFutureVlanPortPortProtoBasedClassification,
       "fsMIDot1qFutureVlanFilteringUtilityCriteria": fsMIDot1qFutureVlanFilteringUtilityCriteria,
       "fsMIDot1qFutureVlanPortProtected": fsMIDot1qFutureVlanPortProtected,
       "fsMIDot1qFutureVlanPortSubnetBasedClassification": fsMIDot1qFutureVlanPortSubnetBasedClassification,
       "fsMIDot1qFutureVlanPortUnicastMacLearning": fsMIDot1qFutureVlanPortUnicastMacLearning,
       "fsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount": fsMIDot1qFutureVlanPortGmrpJoinEmptyTxCount,
       "fsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount": fsMIDot1qFutureVlanPortGmrpJoinEmptyRxCount,
       "fsMIDot1qFutureVlanPortGmrpJoinInTxCount": fsMIDot1qFutureVlanPortGmrpJoinInTxCount,
       "fsMIDot1qFutureVlanPortGmrpJoinInRxCount": fsMIDot1qFutureVlanPortGmrpJoinInRxCount,
       "fsMIDot1qFutureVlanPortGmrpLeaveInTxCount": fsMIDot1qFutureVlanPortGmrpLeaveInTxCount,
       "fsMIDot1qFutureVlanPortGmrpLeaveInRxCount": fsMIDot1qFutureVlanPortGmrpLeaveInRxCount,
       "fsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount": fsMIDot1qFutureVlanPortGmrpLeaveEmptyTxCount,
       "fsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount": fsMIDot1qFutureVlanPortGmrpLeaveEmptyRxCount,
       "fsMIDot1qFutureVlanPortGmrpEmptyTxCount": fsMIDot1qFutureVlanPortGmrpEmptyTxCount,
       "fsMIDot1qFutureVlanPortGmrpEmptyRxCount": fsMIDot1qFutureVlanPortGmrpEmptyRxCount,
       "fsMIDot1qFutureVlanPortGmrpLeaveAllTxCount": fsMIDot1qFutureVlanPortGmrpLeaveAllTxCount,
       "fsMIDot1qFutureVlanPortGmrpLeaveAllRxCount": fsMIDot1qFutureVlanPortGmrpLeaveAllRxCount,
       "fsMIDot1qFutureVlanPortGmrpDiscardCount": fsMIDot1qFutureVlanPortGmrpDiscardCount,
       "fsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount": fsMIDot1qFutureVlanPortGvrpJoinEmptyTxCount,
       "fsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount": fsMIDot1qFutureVlanPortGvrpJoinEmptyRxCount,
       "fsMIDot1qFutureVlanPortGvrpJoinInTxCount": fsMIDot1qFutureVlanPortGvrpJoinInTxCount,
       "fsMIDot1qFutureVlanPortGvrpJoinInRxCount": fsMIDot1qFutureVlanPortGvrpJoinInRxCount,
       "fsMIDot1qFutureVlanPortGvrpLeaveInTxCount": fsMIDot1qFutureVlanPortGvrpLeaveInTxCount,
       "fsMIDot1qFutureVlanPortGvrpLeaveInRxCount": fsMIDot1qFutureVlanPortGvrpLeaveInRxCount,
       "fsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount": fsMIDot1qFutureVlanPortGvrpLeaveEmptyTxCount,
       "fsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount": fsMIDot1qFutureVlanPortGvrpLeaveEmptyRxCount,
       "fsMIDot1qFutureVlanPortGvrpEmptyTxCount": fsMIDot1qFutureVlanPortGvrpEmptyTxCount,
       "fsMIDot1qFutureVlanPortGvrpEmptyRxCount": fsMIDot1qFutureVlanPortGvrpEmptyRxCount,
       "fsMIDot1qFutureVlanPortGvrpLeaveAllTxCount": fsMIDot1qFutureVlanPortGvrpLeaveAllTxCount,
       "fsMIDot1qFutureVlanPortGvrpLeaveAllRxCount": fsMIDot1qFutureVlanPortGvrpLeaveAllRxCount,
       "fsMIDot1qFutureVlanPortGvrpDiscardCount": fsMIDot1qFutureVlanPortGvrpDiscardCount,
       "fsMIDot1qFutureVlanPortFdbFlush": fsMIDot1qFutureVlanPortFdbFlush,
       "fsMIDot1qFutureVlanPortIngressEtherType": fsMIDot1qFutureVlanPortIngressEtherType,
       "fsMIDot1qFutureVlanPortEgressEtherType": fsMIDot1qFutureVlanPortEgressEtherType,
       "fsMIDot1qFutureVlanPortEgressTPIDType": fsMIDot1qFutureVlanPortEgressTPIDType,
       "fsMIDot1qFutureVlanPortAllowableTPID1": fsMIDot1qFutureVlanPortAllowableTPID1,
       "fsMIDot1qFutureVlanPortAllowableTPID2": fsMIDot1qFutureVlanPortAllowableTPID2,
       "fsMIDot1qFutureVlanPortAllowableTPID3": fsMIDot1qFutureVlanPortAllowableTPID3,
       "fsMIDot1qFutureVlanPortClearGarpStats": fsMIDot1qFutureVlanPortClearGarpStats,
       "fsMIDot1qFutureVlanPortUnicastMacSecType": fsMIDot1qFutureVlanPortUnicastMacSecType,
       "fsMIDot1qFutureVlanPortStVlanList": fsMIDot1qFutureVlanPortStVlanList,
       "fsMIDot1qFutureVlanPortStUntaggedVlan": fsMIDot1qFutureVlanPortStUntaggedVlan,
       "fsMIDot1qFuturePortPacketReflectionStatus": fsMIDot1qFuturePortPacketReflectionStatus,
       "fsMIDot1qFutureVlanPortMacMapTable": fsMIDot1qFutureVlanPortMacMapTable,
       "fsMIDot1qFutureVlanPortMacMapEntry": fsMIDot1qFutureVlanPortMacMapEntry,
       "fsMIDot1qFutureVlanPortMacMapAddr": fsMIDot1qFutureVlanPortMacMapAddr,
       "fsMIDot1qFutureVlanPortMacMapVid": fsMIDot1qFutureVlanPortMacMapVid,
       "fsMIDot1qFutureVlanPortMacMapName": fsMIDot1qFutureVlanPortMacMapName,
       "fsMIDot1qFutureVlanPortMacMapMcastBcastOption": fsMIDot1qFutureVlanPortMacMapMcastBcastOption,
       "fsMIDot1qFutureVlanPortMacMapRowStatus": fsMIDot1qFutureVlanPortMacMapRowStatus,
       "fsMIDot1qFutureVlanFidMapTable": fsMIDot1qFutureVlanFidMapTable,
       "fsMIDot1qFutureVlanFidMapEntry": fsMIDot1qFutureVlanFidMapEntry,
       "fsMIDot1qFutureVlanIndex": fsMIDot1qFutureVlanIndex,
       "fsMIDot1qFutureVlanFid": fsMIDot1qFutureVlanFid,
       "fsMIDot1qFutureVlanCounterTable": fsMIDot1qFutureVlanCounterTable,
       "fsMIDot1qFutureVlanCounterEntry": fsMIDot1qFutureVlanCounterEntry,
       "fsMIDot1qFutureVlanCounterRxUcast": fsMIDot1qFutureVlanCounterRxUcast,
       "fsMIDot1qFutureVlanCounterRxMcastBcast": fsMIDot1qFutureVlanCounterRxMcastBcast,
       "fsMIDot1qFutureVlanCounterTxUnknUcast": fsMIDot1qFutureVlanCounterTxUnknUcast,
       "fsMIDot1qFutureVlanCounterTxUcast": fsMIDot1qFutureVlanCounterTxUcast,
       "fsMIDot1qFutureVlanCounterTxBcast": fsMIDot1qFutureVlanCounterTxBcast,
       "fsMIDot1qFutureVlanCounterRxFrames": fsMIDot1qFutureVlanCounterRxFrames,
       "fsMIDot1qFutureVlanCounterRxBytes": fsMIDot1qFutureVlanCounterRxBytes,
       "fsMIDot1qFutureVlanCounterTxFrames": fsMIDot1qFutureVlanCounterTxFrames,
       "fsMIDot1qFutureVlanCounterTxBytes": fsMIDot1qFutureVlanCounterTxBytes,
       "fsMIDot1qFutureVlanCounterDiscardFrames": fsMIDot1qFutureVlanCounterDiscardFrames,
       "fsMIDot1qFutureVlanCounterDiscardBytes": fsMIDot1qFutureVlanCounterDiscardBytes,
       "fsMIDot1qFutureVlanCounterStatus": fsMIDot1qFutureVlanCounterStatus,
       "fsMIDot1qFutureVlanUnicastMacControlTable": fsMIDot1qFutureVlanUnicastMacControlTable,
       "fsMIDot1qFutureVlanUnicastMacControlEntry": fsMIDot1qFutureVlanUnicastMacControlEntry,
       "fsMIDot1qFutureVlanUnicastMacLimit": fsMIDot1qFutureVlanUnicastMacLimit,
       "fsMIDot1qFutureVlanAdminMacLearningStatus": fsMIDot1qFutureVlanAdminMacLearningStatus,
       "fsMIDot1qFutureVlanOperMacLearningStatus": fsMIDot1qFutureVlanOperMacLearningStatus,
       "fsMIDot1qFutureGarpGlobalTrace": fsMIDot1qFutureGarpGlobalTrace,
       "fsMIDot1qFutureVlanTpFdbTable": fsMIDot1qFutureVlanTpFdbTable,
       "fsMIDot1qFutureVlanTpFdbEntry": fsMIDot1qFutureVlanTpFdbEntry,
       "fsMIDot1qFutureVlanOldTpFdbPort": fsMIDot1qFutureVlanOldTpFdbPort,
       "fsMIDot1qFutureConnectionIdentifier": fsMIDot1qFutureConnectionIdentifier,
       "fsMIDot1qFutureVlanWildCardTable": fsMIDot1qFutureVlanWildCardTable,
       "fsMIDot1qFutureVlanWildCardEntry": fsMIDot1qFutureVlanWildCardEntry,
       "fsMIDot1qFutureVlanWildCardMacAddress": fsMIDot1qFutureVlanWildCardMacAddress,
       "fsMIDot1qFutureVlanWildCardRowStatus": fsMIDot1qFutureVlanWildCardRowStatus,
       "fsMIDot1qFutureVlanWildCardPortTable": fsMIDot1qFutureVlanWildCardPortTable,
       "fsMIDot1qFutureVlanWildCardPortEntry": fsMIDot1qFutureVlanWildCardPortEntry,
       "fsMIDot1qFutureVlanIsWildCardEgressPort": fsMIDot1qFutureVlanIsWildCardEgressPort,
       "fsMIDot1qFutureStaticUnicastExtnTable": fsMIDot1qFutureStaticUnicastExtnTable,
       "fsMIDot1qFutureStaticUnicastExtnEntry": fsMIDot1qFutureStaticUnicastExtnEntry,
       "fsMIDot1qFutureStaticConnectionIdentifier": fsMIDot1qFutureStaticConnectionIdentifier,
       "fsMIDot1qFutureVlanPortSubnetMapTable": fsMIDot1qFutureVlanPortSubnetMapTable,
       "fsMIDot1qFutureVlanPortSubnetMapEntry": fsMIDot1qFutureVlanPortSubnetMapEntry,
       "fsMIDot1qFutureVlanPortSubnetMapAddr": fsMIDot1qFutureVlanPortSubnetMapAddr,
       "fsMIDot1qFutureVlanPortSubnetMapVid": fsMIDot1qFutureVlanPortSubnetMapVid,
       "fsMIDot1qFutureVlanPortSubnetMapARPOption": fsMIDot1qFutureVlanPortSubnetMapARPOption,
       "fsMIDot1qFutureVlanPortSubnetMapRowStatus": fsMIDot1qFutureVlanPortSubnetMapRowStatus,
       "fsMIDot1qFutureVlanSwStatsEnabled": fsMIDot1qFutureVlanSwStatsEnabled,
       "fsMIDot1qFutureStVlanExtTable": fsMIDot1qFutureStVlanExtTable,
       "fsMIDot1qFutureStVlanExtEntry": fsMIDot1qFutureStVlanExtEntry,
       "fsMIDot1qFutureStVlanPVlanType": fsMIDot1qFutureStVlanPVlanType,
       "fsMIDot1qFutureStVlanPrimaryVid": fsMIDot1qFutureStVlanPrimaryVid,
       "fsMIDot1qFutureStVlanFdbFlush": fsMIDot1qFutureStVlanFdbFlush,
       "fsMIDot1qFutureStVlanEgressEthertype": fsMIDot1qFutureStVlanEgressEthertype,
       "fsMIDot1qFutureVlanPortSubnetMapExtTable": fsMIDot1qFutureVlanPortSubnetMapExtTable,
       "fsMIDot1qFutureVlanPortSubnetMapExtEntry": fsMIDot1qFutureVlanPortSubnetMapExtEntry,
       "fsMIDot1qFutureVlanPortSubnetMapExtAddr": fsMIDot1qFutureVlanPortSubnetMapExtAddr,
       "fsMIDot1qFutureVlanPortSubnetMapExtMask": fsMIDot1qFutureVlanPortSubnetMapExtMask,
       "fsMIDot1qFutureVlanPortSubnetMapExtVid": fsMIDot1qFutureVlanPortSubnetMapExtVid,
       "fsMIDot1qFutureVlanPortSubnetMapExtARPOption": fsMIDot1qFutureVlanPortSubnetMapExtARPOption,
       "fsMIDot1qFutureVlanPortSubnetMapExtRowStatus": fsMIDot1qFutureVlanPortSubnetMapExtRowStatus,
       "fsMIDot1qFuturePortVlanExtTable": fsMIDot1qFuturePortVlanExtTable,
       "fsMIDot1qFuturePortVlanExtEntry": fsMIDot1qFuturePortVlanExtEntry,
       "fsMIDot1qFuturePortVlanFdbFlush": fsMIDot1qFuturePortVlanFdbFlush,
       "fsMIDot1qFutureVlanLoopbackTable": fsMIDot1qFutureVlanLoopbackTable,
       "fsMIDot1qFutureVlanLoopbackEntry": fsMIDot1qFutureVlanLoopbackEntry,
       "fsMIDot1qFutureVlanLoopbackStatus": fsMIDot1qFutureVlanLoopbackStatus,
       "fsMIDot1qFutureVlanTunnelConfig": fsMIDot1qFutureVlanTunnelConfig,
       "fsMIDot1qFutureVlanTunnelConfigTable": fsMIDot1qFutureVlanTunnelConfigTable,
       "fsMIDot1qFutureVlanTunnelConfigEntry": fsMIDot1qFutureVlanTunnelConfigEntry,
       "fsMIDot1qFutureVlanBridgeMode": fsMIDot1qFutureVlanBridgeMode,
       "fsMIDot1qFutureVlanTunnelBpduPri": fsMIDot1qFutureVlanTunnelBpduPri,
       "fsMIDot1qFutureVlanTunnelTable": fsMIDot1qFutureVlanTunnelTable,
       "fsMIDot1qFutureVlanTunnelEntry": fsMIDot1qFutureVlanTunnelEntry,
       "fsMIDot1qFutureVlanTunnelStatus": fsMIDot1qFutureVlanTunnelStatus,
       "fsMIDot1qFutureVlanTunnelProtocolTable": fsMIDot1qFutureVlanTunnelProtocolTable,
       "fsMIDot1qFutureVlanTunnelProtocolEntry": fsMIDot1qFutureVlanTunnelProtocolEntry,
       "fsMIDot1qFutureVlanTunnelStpPDUs": fsMIDot1qFutureVlanTunnelStpPDUs,
       "fsMIDot1qFutureVlanTunnelStpPDUsRecvd": fsMIDot1qFutureVlanTunnelStpPDUsRecvd,
       "fsMIDot1qFutureVlanTunnelStpPDUsSent": fsMIDot1qFutureVlanTunnelStpPDUsSent,
       "fsMIDot1qFutureVlanTunnelGvrpPDUs": fsMIDot1qFutureVlanTunnelGvrpPDUs,
       "fsMIDot1qFutureVlanTunnelGvrpPDUsRecvd": fsMIDot1qFutureVlanTunnelGvrpPDUsRecvd,
       "fsMIDot1qFutureVlanTunnelGvrpPDUsSent": fsMIDot1qFutureVlanTunnelGvrpPDUsSent,
       "fsMIDot1qFutureVlanTunnelIgmpPkts": fsMIDot1qFutureVlanTunnelIgmpPkts,
       "fsMIDot1qFutureVlanTunnelIgmpPktsRecvd": fsMIDot1qFutureVlanTunnelIgmpPktsRecvd,
       "fsMIDot1qFutureVlanTunnelIgmpPktsSent": fsMIDot1qFutureVlanTunnelIgmpPktsSent,
       "fsMIDot1qFutureVlanTraps": fsMIDot1qFutureVlanTraps,
       "fsMIDot1qVlanTraps": fsMIDot1qVlanTraps,
       "fsMIDot1qFutureMacThresholdTrap": fsMIDot1qFutureMacThresholdTrap,
       "fsMIDot1qFutureSrcRelearnTrap": fsMIDot1qFutureSrcRelearnTrap,
       "fsMIDot1qFutureSwitchMacLimitTrap": fsMIDot1qFutureSwitchMacLimitTrap,
       "fsMIDot1qFutureVlanTrapControl": fsMIDot1qFutureVlanTrapControl}
)
