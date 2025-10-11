# SNMP MIB module (RAD-Protection-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-Protection-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:38 2025
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

(ifAlias,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifAlias")

(alarmEventLogAlarmOrEventId,
 alarmEventLogDateAndTime,
 alarmEventLogDescription,
 alarmEventLogSeverity,
 alarmEventLogSourceName,
 alarmEventReason) = mibBuilder.importSymbols(
    "RAD-GEN-MIB",
    "alarmEventLogAlarmOrEventId",
    "alarmEventLogDateAndTime",
    "alarmEventLogDescription",
    "alarmEventLogSeverity",
    "alarmEventLogSourceName",
    "alarmEventReason")

(agnt,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "agnt")

(ProtectClassType,
 ProtectGroupCmdType,
 ProtectLastSwitchReasonType,
 ProtectionStateType) = mibBuilder.importSymbols(
    "RAD-TC",
    "ProtectClassType",
    "ProtectGroupCmdType",
    "ProtectLastSwitchReasonType",
    "ProtectionStateType")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

agnProtection = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ProtectionEvents_ObjectIdentity = ObjectIdentity
protectionEvents = _ProtectionEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 0)
)
if mibBuilder.loadTexts:
    protectionEvents.setStatus("current")
_ProtectGroupTable_Object = MibTable
protectGroupTable = _ProtectGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1)
)
if mibBuilder.loadTexts:
    protectGroupTable.setStatus("current")
_ProtectGroupEntry_Object = MibTableRow
protectGroupEntry = _ProtectGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1)
)
protectGroupEntry.setIndexNames(
    (0, "RAD-Protection-MIB", "protectGroupClass"),
    (0, "RAD-Protection-MIB", "protectGroupIdx"),
)
if mibBuilder.loadTexts:
    protectGroupEntry.setStatus("current")
_ProtectGroupClass_Type = ProtectClassType
_ProtectGroupClass_Object = MibTableColumn
protectGroupClass = _ProtectGroupClass_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 1),
    _ProtectGroupClass_Type()
)
protectGroupClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protectGroupClass.setStatus("current")
_ProtectGroupIdx_Type = Unsigned32
_ProtectGroupIdx_Object = MibTableColumn
protectGroupIdx = _ProtectGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 2),
    _ProtectGroupIdx_Type()
)
protectGroupIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protectGroupIdx.setStatus("current")
_ProtectGroupRowStatus_Type = RowStatus
_ProtectGroupRowStatus_Object = MibTableColumn
protectGroupRowStatus = _ProtectGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 3),
    _ProtectGroupRowStatus_Type()
)
protectGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectGroupRowStatus.setStatus("current")


class _ProtectGroupName_Type(SnmpAdminString):
    """Custom type protectGroupName based on SnmpAdminString"""
    defaultValue = OctetString("")


_ProtectGroupName_Type.__name__ = "SnmpAdminString"
_ProtectGroupName_Object = MibTableColumn
protectGroupName = _ProtectGroupName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 4),
    _ProtectGroupName_Type()
)
protectGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectGroupName.setStatus("current")


class _ProtectGroupMode_Type(Integer32):
    """Custom type protectGroupMode based on Integer32"""
    defaultValue = 3

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
        *(("manual", 1),
          ("onePlusOne", 2),
          ("oneToOne", 3),
          ("oneToOneIndepend", 4),
          ("oneToOneMaster", 5),
          ("oneToOneSlave", 6))
    )


_ProtectGroupMode_Type.__name__ = "Integer32"
_ProtectGroupMode_Object = MibTableColumn
protectGroupMode = _ProtectGroupMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 5),
    _ProtectGroupMode_Type()
)
protectGroupMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectGroupMode.setStatus("current")


class _ProtectGroupRevertMode_Type(Integer32):
    """Custom type protectGroupRevertMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nonRevertive", 1),
          ("revertive", 2))
    )


_ProtectGroupRevertMode_Type.__name__ = "Integer32"
_ProtectGroupRevertMode_Object = MibTableColumn
protectGroupRevertMode = _ProtectGroupRevertMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 6),
    _ProtectGroupRevertMode_Type()
)
protectGroupRevertMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectGroupRevertMode.setStatus("current")


class _ProtectGroupWaitToRestore_Type(Unsigned32):
    """Custom type protectGroupWaitToRestore based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 720),
    )


_ProtectGroupWaitToRestore_Type.__name__ = "Unsigned32"
_ProtectGroupWaitToRestore_Object = MibTableColumn
protectGroupWaitToRestore = _ProtectGroupWaitToRestore_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 7),
    _ProtectGroupWaitToRestore_Type()
)
protectGroupWaitToRestore.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectGroupWaitToRestore.setStatus("current")
if mibBuilder.loadTexts:
    protectGroupWaitToRestore.setUnits("seconds")


class _ProtectGroupCmd_Type(ProtectGroupCmdType):
    """Custom type protectGroupCmd based on ProtectGroupCmdType"""
    defaultValue = 1


_ProtectGroupCmd_Type.__name__ = "ProtectGroupCmdType"
_ProtectGroupCmd_Object = MibTableColumn
protectGroupCmd = _ProtectGroupCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 8),
    _ProtectGroupCmd_Type()
)
protectGroupCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectGroupCmd.setStatus("current")
_ProtectGroupLastCmd_Type = ProtectGroupCmdType
_ProtectGroupLastCmd_Object = MibTableColumn
protectGroupLastCmd = _ProtectGroupLastCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 9),
    _ProtectGroupLastCmd_Type()
)
protectGroupLastCmd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectGroupLastCmd.setStatus("current")
_ProtectGroupLastSwitchTime_Type = DateAndTime
_ProtectGroupLastSwitchTime_Object = MibTableColumn
protectGroupLastSwitchTime = _ProtectGroupLastSwitchTime_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 10),
    _ProtectGroupLastSwitchTime_Type()
)
protectGroupLastSwitchTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectGroupLastSwitchTime.setStatus("current")
_ProtectGroupLastSwitchReason_Type = ProtectLastSwitchReasonType
_ProtectGroupLastSwitchReason_Object = MibTableColumn
protectGroupLastSwitchReason = _ProtectGroupLastSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 11),
    _ProtectGroupLastSwitchReason_Type()
)
protectGroupLastSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectGroupLastSwitchReason.setStatus("current")


class _ProtectGroupSwitchReason_Type(Integer32):
    """Custom type protectGroupSwitchReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("revertiveModeMismatch", 2))
    )


_ProtectGroupSwitchReason_Type.__name__ = "Integer32"
_ProtectGroupSwitchReason_Object = MibTableColumn
protectGroupSwitchReason = _ProtectGroupSwitchReason_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 12),
    _ProtectGroupSwitchReason_Type()
)
protectGroupSwitchReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectGroupSwitchReason.setStatus("current")
_ProtectGroupDownDuration_Type = Unsigned32
_ProtectGroupDownDuration_Object = MibTableColumn
protectGroupDownDuration = _ProtectGroupDownDuration_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 1, 1, 13),
    _ProtectGroupDownDuration_Type()
)
protectGroupDownDuration.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectGroupDownDuration.setStatus("current")
_ProtectMemberTable_Object = MibTable
protectMemberTable = _ProtectMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 2)
)
if mibBuilder.loadTexts:
    protectMemberTable.setStatus("current")
_ProtectMemberEntry_Object = MibTableRow
protectMemberEntry = _ProtectMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 2, 1)
)
protectMemberEntry.setIndexNames(
    (0, "RAD-Protection-MIB", "protectGroupClass"),
    (0, "RAD-Protection-MIB", "protectGroupIdx"),
    (0, "RAD-Protection-MIB", "protectMemberNumber"),
)
if mibBuilder.loadTexts:
    protectMemberEntry.setStatus("current")
_ProtectMemberNumber_Type = Unsigned32
_ProtectMemberNumber_Object = MibTableColumn
protectMemberNumber = _ProtectMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 2, 1, 1),
    _ProtectMemberNumber_Type()
)
protectMemberNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protectMemberNumber.setStatus("current")
_ProtectMemberRowStatus_Type = RowStatus
_ProtectMemberRowStatus_Object = MibTableColumn
protectMemberRowStatus = _ProtectMemberRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 2, 1, 2),
    _ProtectMemberRowStatus_Type()
)
protectMemberRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectMemberRowStatus.setStatus("current")
_ProtectMemberId_Type = Unsigned32
_ProtectMemberId_Object = MibTableColumn
protectMemberId = _ProtectMemberId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 2, 1, 3),
    _ProtectMemberId_Type()
)
protectMemberId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectMemberId.setStatus("current")
_ProtectMemberState_Type = ProtectionStateType
_ProtectMemberState_Object = MibTableColumn
protectMemberState = _ProtectMemberState_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 2, 1, 4),
    _ProtectMemberState_Type()
)
protectMemberState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectMemberState.setStatus("current")


class _ProtectMemberIsProtected_Type(Integer32):
    """Custom type protectMemberIsProtected based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_ProtectMemberIsProtected_Type.__name__ = "Integer32"
_ProtectMemberIsProtected_Object = MibTableColumn
protectMemberIsProtected = _ProtectMemberIsProtected_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 2, 1, 5),
    _ProtectMemberIsProtected_Type()
)
protectMemberIsProtected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectMemberIsProtected.setStatus("current")
_ProtectInverseMapTable_Object = MibTable
protectInverseMapTable = _ProtectInverseMapTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 3)
)
if mibBuilder.loadTexts:
    protectInverseMapTable.setStatus("current")
_ProtectInverseMapEntry_Object = MibTableRow
protectInverseMapEntry = _ProtectInverseMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 3, 1)
)
protectInverseMapEntry.setIndexNames(
    (0, "RAD-Protection-MIB", "protectInverseMapGroupClass"),
    (0, "RAD-Protection-MIB", "protectInverseMapMemberId"),
)
if mibBuilder.loadTexts:
    protectInverseMapEntry.setStatus("current")
_ProtectInverseMapGroupClass_Type = ProtectClassType
_ProtectInverseMapGroupClass_Object = MibTableColumn
protectInverseMapGroupClass = _ProtectInverseMapGroupClass_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 3, 1, 1),
    _ProtectInverseMapGroupClass_Type()
)
protectInverseMapGroupClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protectInverseMapGroupClass.setStatus("current")
_ProtectInverseMapMemberId_Type = Unsigned32
_ProtectInverseMapMemberId_Object = MibTableColumn
protectInverseMapMemberId = _ProtectInverseMapMemberId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 3, 1, 2),
    _ProtectInverseMapMemberId_Type()
)
protectInverseMapMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protectInverseMapMemberId.setStatus("current")
_ProtectInverseMapGroupIdx_Type = Unsigned32
_ProtectInverseMapGroupIdx_Object = MibTableColumn
protectInverseMapGroupIdx = _ProtectInverseMapGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 3, 1, 3),
    _ProtectInverseMapGroupIdx_Type()
)
protectInverseMapGroupIdx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectInverseMapGroupIdx.setStatus("current")
_ProtectInverseMapMemberNumber_Type = Unsigned32
_ProtectInverseMapMemberNumber_Object = MibTableColumn
protectInverseMapMemberNumber = _ProtectInverseMapMemberNumber_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 3, 1, 4),
    _ProtectInverseMapMemberNumber_Type()
)
protectInverseMapMemberNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectInverseMapMemberNumber.setStatus("current")
_ProtectEpsGroupTable_Object = MibTable
protectEpsGroupTable = _ProtectEpsGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 4)
)
if mibBuilder.loadTexts:
    protectEpsGroupTable.setStatus("current")
_ProtectEpsGroupEntry_Object = MibTableRow
protectEpsGroupEntry = _ProtectEpsGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 4, 1)
)
if mibBuilder.loadTexts:
    protectEpsGroupEntry.setStatus("current")


class _ProtectEpsGroupUseAps_Type(Integer32):
    """Custom type protectEpsGroupUseAps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no", 2),
          ("yes", 3))
    )


_ProtectEpsGroupUseAps_Type.__name__ = "Integer32"
_ProtectEpsGroupUseAps_Object = MibTableColumn
protectEpsGroupUseAps = _ProtectEpsGroupUseAps_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 4, 1, 1),
    _ProtectEpsGroupUseAps_Type()
)
protectEpsGroupUseAps.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectEpsGroupUseAps.setStatus("current")
_ProtectEpsGroupMaster_Type = Unsigned32
_ProtectEpsGroupMaster_Object = MibTableColumn
protectEpsGroupMaster = _ProtectEpsGroupMaster_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 4, 1, 2),
    _ProtectEpsGroupMaster_Type()
)
protectEpsGroupMaster.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectEpsGroupMaster.setStatus("current")


class _ProtectEpsGroupSwitchDirection_Type(Integer32):
    """Custom type protectEpsGroupSwitchDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("biDirectional", 2),
          ("uniDirectional", 3))
    )


_ProtectEpsGroupSwitchDirection_Type.__name__ = "Integer32"
_ProtectEpsGroupSwitchDirection_Object = MibTableColumn
protectEpsGroupSwitchDirection = _ProtectEpsGroupSwitchDirection_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 4, 1, 3),
    _ProtectEpsGroupSwitchDirection_Type()
)
protectEpsGroupSwitchDirection.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectEpsGroupSwitchDirection.setStatus("current")
_ProtectEpsMemberTable_Object = MibTable
protectEpsMemberTable = _ProtectEpsMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 5)
)
if mibBuilder.loadTexts:
    protectEpsMemberTable.setStatus("current")
_ProtectEpsMemberEntry_Object = MibTableRow
protectEpsMemberEntry = _ProtectEpsMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 5, 1)
)
if mibBuilder.loadTexts:
    protectEpsMemberEntry.setStatus("current")
_ProtectEpsOamCfmMdId_Type = Unsigned32
_ProtectEpsOamCfmMdId_Object = MibTableColumn
protectEpsOamCfmMdId = _ProtectEpsOamCfmMdId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 5, 1, 1),
    _ProtectEpsOamCfmMdId_Type()
)
protectEpsOamCfmMdId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectEpsOamCfmMdId.setStatus("current")
_ProtectEpsOamCfmMaId_Type = Unsigned32
_ProtectEpsOamCfmMaId_Object = MibTableColumn
protectEpsOamCfmMaId = _ProtectEpsOamCfmMaId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 5, 1, 2),
    _ProtectEpsOamCfmMaId_Type()
)
protectEpsOamCfmMaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectEpsOamCfmMaId.setStatus("current")


class _ProtectEpsOamCfmMepId_Type(Unsigned32):
    """Custom type protectEpsOamCfmMepId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ProtectEpsOamCfmMepId_Type.__name__ = "Unsigned32"
_ProtectEpsOamCfmMepId_Object = MibTableColumn
protectEpsOamCfmMepId = _ProtectEpsOamCfmMepId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 5, 1, 3),
    _ProtectEpsOamCfmMepId_Type()
)
protectEpsOamCfmMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectEpsOamCfmMepId.setStatus("current")
_ProtectEpsIfIndex_Type = Unsigned32
_ProtectEpsIfIndex_Object = MibTableColumn
protectEpsIfIndex = _ProtectEpsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 5, 1, 4),
    _ProtectEpsIfIndex_Type()
)
protectEpsIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    protectEpsIfIndex.setStatus("current")
_ProtectEpsMasterMapTable_Object = MibTable
protectEpsMasterMapTable = _ProtectEpsMasterMapTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 6)
)
if mibBuilder.loadTexts:
    protectEpsMasterMapTable.setStatus("current")
_ProtectEpsMasterMapEntry_Object = MibTableRow
protectEpsMasterMapEntry = _ProtectEpsMasterMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 6, 1)
)
protectEpsMasterMapEntry.setIndexNames(
    (0, "RAD-Protection-MIB", "protectEpsMasterMapMasterIdx"),
    (0, "RAD-Protection-MIB", "protectEpsMasterMapSlaveIdx"),
)
if mibBuilder.loadTexts:
    protectEpsMasterMapEntry.setStatus("current")
_ProtectEpsMasterMapMasterIdx_Type = Unsigned32
_ProtectEpsMasterMapMasterIdx_Object = MibTableColumn
protectEpsMasterMapMasterIdx = _ProtectEpsMasterMapMasterIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 6, 1, 1),
    _ProtectEpsMasterMapMasterIdx_Type()
)
protectEpsMasterMapMasterIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protectEpsMasterMapMasterIdx.setStatus("current")
_ProtectEpsMasterMapSlaveIdx_Type = Unsigned32
_ProtectEpsMasterMapSlaveIdx_Object = MibTableColumn
protectEpsMasterMapSlaveIdx = _ProtectEpsMasterMapSlaveIdx_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 6, 1, 2),
    _ProtectEpsMasterMapSlaveIdx_Type()
)
protectEpsMasterMapSlaveIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protectEpsMasterMapSlaveIdx.setStatus("current")
_ProtectEpsMasterMapParam_Type = Integer32
_ProtectEpsMasterMapParam_Object = MibTableColumn
protectEpsMasterMapParam = _ProtectEpsMasterMapParam_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 6, 1, 3),
    _ProtectEpsMasterMapParam_Type()
)
protectEpsMasterMapParam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    protectEpsMasterMapParam.setStatus("current")
protectGroupEntry.registerAugmentions(
    ("RAD-Protection-MIB",
     "protectEpsGroupEntry")
)
protectEpsGroupEntry.setIndexNames(*protectGroupEntry.getIndexNames())
protectMemberEntry.registerAugmentions(
    ("RAD-Protection-MIB",
     "protectEpsMemberEntry")
)
protectEpsMemberEntry.setIndexNames(*protectMemberEntry.getIndexNames())

# Managed Objects groups


# Notification objects

epsConfigurationMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 0, 3)
)
epsConfigurationMismatch.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-Protection-MIB", "protectGroupName"),
        ("RAD-Protection-MIB", "protectGroupSwitchReason"))
)
if mibBuilder.loadTexts:
    epsConfigurationMismatch.setStatus(
        "deprecated"
    )

etpEpsPortSwitchover = NotificationType(
    (1, 3, 6, 1, 4, 1, 164, 6, 2, 72, 0, 5)
)
etpEpsPortSwitchover.setObjects(
      *(("RAD-GEN-MIB", "alarmEventLogSourceName"),
        ("RAD-GEN-MIB", "alarmEventLogAlarmOrEventId"),
        ("RAD-GEN-MIB", "alarmEventLogDescription"),
        ("RAD-GEN-MIB", "alarmEventLogSeverity"),
        ("RAD-GEN-MIB", "alarmEventLogDateAndTime"),
        ("RAD-GEN-MIB", "alarmEventReason"),
        ("RAD-Protection-MIB", "protectGroupName"),
        ("IF-MIB", "ifAlias"),
        ("RAD-Protection-MIB", "protectGroupLastSwitchReason"))
)
if mibBuilder.loadTexts:
    etpEpsPortSwitchover.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-Protection-MIB",
    **{"agnProtection": agnProtection,
       "protectionEvents": protectionEvents,
       "epsConfigurationMismatch": epsConfigurationMismatch,
       "etpEpsPortSwitchover": etpEpsPortSwitchover,
       "protectGroupTable": protectGroupTable,
       "protectGroupEntry": protectGroupEntry,
       "protectGroupClass": protectGroupClass,
       "protectGroupIdx": protectGroupIdx,
       "protectGroupRowStatus": protectGroupRowStatus,
       "protectGroupName": protectGroupName,
       "protectGroupMode": protectGroupMode,
       "protectGroupRevertMode": protectGroupRevertMode,
       "protectGroupWaitToRestore": protectGroupWaitToRestore,
       "protectGroupCmd": protectGroupCmd,
       "protectGroupLastCmd": protectGroupLastCmd,
       "protectGroupLastSwitchTime": protectGroupLastSwitchTime,
       "protectGroupLastSwitchReason": protectGroupLastSwitchReason,
       "protectGroupSwitchReason": protectGroupSwitchReason,
       "protectGroupDownDuration": protectGroupDownDuration,
       "protectMemberTable": protectMemberTable,
       "protectMemberEntry": protectMemberEntry,
       "protectMemberNumber": protectMemberNumber,
       "protectMemberRowStatus": protectMemberRowStatus,
       "protectMemberId": protectMemberId,
       "protectMemberState": protectMemberState,
       "protectMemberIsProtected": protectMemberIsProtected,
       "protectInverseMapTable": protectInverseMapTable,
       "protectInverseMapEntry": protectInverseMapEntry,
       "protectInverseMapGroupClass": protectInverseMapGroupClass,
       "protectInverseMapMemberId": protectInverseMapMemberId,
       "protectInverseMapGroupIdx": protectInverseMapGroupIdx,
       "protectInverseMapMemberNumber": protectInverseMapMemberNumber,
       "protectEpsGroupTable": protectEpsGroupTable,
       "protectEpsGroupEntry": protectEpsGroupEntry,
       "protectEpsGroupUseAps": protectEpsGroupUseAps,
       "protectEpsGroupMaster": protectEpsGroupMaster,
       "protectEpsGroupSwitchDirection": protectEpsGroupSwitchDirection,
       "protectEpsMemberTable": protectEpsMemberTable,
       "protectEpsMemberEntry": protectEpsMemberEntry,
       "protectEpsOamCfmMdId": protectEpsOamCfmMdId,
       "protectEpsOamCfmMaId": protectEpsOamCfmMaId,
       "protectEpsOamCfmMepId": protectEpsOamCfmMepId,
       "protectEpsIfIndex": protectEpsIfIndex,
       "protectEpsMasterMapTable": protectEpsMasterMapTable,
       "protectEpsMasterMapEntry": protectEpsMasterMapEntry,
       "protectEpsMasterMapMasterIdx": protectEpsMasterMapMasterIdx,
       "protectEpsMasterMapSlaveIdx": protectEpsMasterMapSlaveIdx,
       "protectEpsMasterMapParam": protectEpsMasterMapParam}
)
