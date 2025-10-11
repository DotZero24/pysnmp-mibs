# SNMP MIB module (ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:09:10 2025
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

(alcatelIND1VirtualChassisMIBVCSP,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-VIRTUAL-CHASSIS-MIB",
    "alcatelIND1VirtualChassisMIBVCSP")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

alaVCSPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaVCSPMIB.setRevisions(
        ("2013-10-14 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaVCSPChassisID(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )



class AlaVCSPOpState(TextualConvention, Integer32):
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
        *(("active", 1),
          ("protection", 2),
          ("inactive", 3))
    )



class AlaVCSPState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_AlaVCSPMIBNotifications_ObjectIdentity = ObjectIdentity
alaVCSPMIBNotifications = _AlaVCSPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 0)
)
_AlaVCSPMIBObjects_ObjectIdentity = ObjectIdentity
alaVCSPMIBObjects = _AlaVCSPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1)
)
_AlaVCSPHelperGlobalConfig_ObjectIdentity = ObjectIdentity
alaVCSPHelperGlobalConfig = _AlaVCSPHelperGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 1)
)


class _AlaVCSPHelperAdminState_Type(AlaVCSPState):
    """Custom type alaVCSPHelperAdminState based on AlaVCSPState"""
    defaultValue = 2


_AlaVCSPHelperAdminState_Type.__name__ = "AlaVCSPState"
_AlaVCSPHelperAdminState_Object = MibScalar
alaVCSPHelperAdminState = _AlaVCSPHelperAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 1, 1),
    _AlaVCSPHelperAdminState_Type()
)
alaVCSPHelperAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVCSPHelperAdminState.setStatus("current")
_AlaVCSPConfigInfo_ObjectIdentity = ObjectIdentity
alaVCSPConfigInfo = _AlaVCSPConfigInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2)
)


class _AlaVCSPAdminState_Type(AlaVCSPState):
    """Custom type alaVCSPAdminState based on AlaVCSPState"""
    defaultValue = 2


_AlaVCSPAdminState_Type.__name__ = "AlaVCSPState"
_AlaVCSPAdminState_Object = MibScalar
alaVCSPAdminState = _AlaVCSPAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2, 1),
    _AlaVCSPAdminState_Type()
)
alaVCSPAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVCSPAdminState.setStatus("current")


class _AlaVCSPLinkaggId_Type(Integer32):
    """Custom type alaVCSPLinkaggId based on Integer32"""
    defaultValue = -1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 128),
    )


_AlaVCSPLinkaggId_Type.__name__ = "Integer32"
_AlaVCSPLinkaggId_Object = MibScalar
alaVCSPLinkaggId = _AlaVCSPLinkaggId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2, 2),
    _AlaVCSPLinkaggId_Type()
)
alaVCSPLinkaggId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVCSPLinkaggId.setStatus("current")


class _AlaVCSPGuardTimer_Type(Integer32):
    """Custom type alaVCSPGuardTimer based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 100),
    )


_AlaVCSPGuardTimer_Type.__name__ = "Integer32"
_AlaVCSPGuardTimer_Object = MibScalar
alaVCSPGuardTimer = _AlaVCSPGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2, 3),
    _AlaVCSPGuardTimer_Type()
)
alaVCSPGuardTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaVCSPGuardTimer.setStatus("current")
_AlaVCSPUpTime_Type = TimeTicks
_AlaVCSPUpTime_Object = MibScalar
alaVCSPUpTime = _AlaVCSPUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2, 4),
    _AlaVCSPUpTime_Type()
)
alaVCSPUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVCSPUpTime.setStatus("current")
_AlaVCSPProtectionStateUpTime_Type = TimeTicks
_AlaVCSPProtectionStateUpTime_Object = MibScalar
alaVCSPProtectionStateUpTime = _AlaVCSPProtectionStateUpTime_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 2, 5),
    _AlaVCSPProtectionStateUpTime_Type()
)
alaVCSPProtectionStateUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVCSPProtectionStateUpTime.setStatus("current")
_AlaVCSPHelperLinkaggTable_Object = MibTable
alaVCSPHelperLinkaggTable = _AlaVCSPHelperLinkaggTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 3)
)
if mibBuilder.loadTexts:
    alaVCSPHelperLinkaggTable.setStatus("current")
_AlaVCSPHelperLinkaggEntry_Object = MibTableRow
alaVCSPHelperLinkaggEntry = _AlaVCSPHelperLinkaggEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 3, 1)
)
alaVCSPHelperLinkaggEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPHelperLinkaggId"),
)
if mibBuilder.loadTexts:
    alaVCSPHelperLinkaggEntry.setStatus("current")


class _AlaVCSPHelperLinkaggId_Type(Integer32):
    """Custom type alaVCSPHelperLinkaggId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_AlaVCSPHelperLinkaggId_Type.__name__ = "Integer32"
_AlaVCSPHelperLinkaggId_Object = MibTableColumn
alaVCSPHelperLinkaggId = _AlaVCSPHelperLinkaggId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 3, 1, 1),
    _AlaVCSPHelperLinkaggId_Type()
)
alaVCSPHelperLinkaggId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVCSPHelperLinkaggId.setStatus("current")
_AlaVCSPHelperLinkaggRowStatus_Type = RowStatus
_AlaVCSPHelperLinkaggRowStatus_Object = MibTableColumn
alaVCSPHelperLinkaggRowStatus = _AlaVCSPHelperLinkaggRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 3, 1, 2),
    _AlaVCSPHelperLinkaggRowStatus_Type()
)
alaVCSPHelperLinkaggRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaVCSPHelperLinkaggRowStatus.setStatus("current")
_AlaVCSPStateTable_Object = MibTable
alaVCSPStateTable = _AlaVCSPStateTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 4)
)
if mibBuilder.loadTexts:
    alaVCSPStateTable.setStatus("current")
_AlaVCSPStateEntry_Object = MibTableRow
alaVCSPStateEntry = _AlaVCSPStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 4, 1)
)
alaVCSPStateEntry.setIndexNames(
    (0, "ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPTableChassisID"),
)
if mibBuilder.loadTexts:
    alaVCSPStateEntry.setStatus("current")
_AlaVCSPTableChassisID_Type = AlaVCSPChassisID
_AlaVCSPTableChassisID_Object = MibTableColumn
alaVCSPTableChassisID = _AlaVCSPTableChassisID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 4, 1, 1),
    _AlaVCSPTableChassisID_Type()
)
alaVCSPTableChassisID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVCSPTableChassisID.setStatus("current")
_AlaVCSPTableOperState_Type = AlaVCSPOpState
_AlaVCSPTableOperState_Object = MibTableColumn
alaVCSPTableOperState = _AlaVCSPTableOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 1, 4, 1, 2),
    _AlaVCSPTableOperState_Type()
)
alaVCSPTableOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaVCSPTableOperState.setStatus("current")
_AlaVCSPMIBConformance_ObjectIdentity = ObjectIdentity
alaVCSPMIBConformance = _AlaVCSPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2)
)
_AlaVCSPMIBGroups_ObjectIdentity = ObjectIdentity
alaVCSPMIBGroups = _AlaVCSPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 1)
)
_AlaVCSPMIBCompliances_ObjectIdentity = ObjectIdentity
alaVCSPMIBCompliances = _AlaVCSPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 2)
)

# Managed Objects groups

alaVCSPConfigInfoGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 1, 2)
)
alaVCSPConfigInfoGroup.setObjects(
      *(("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPLinkaggId"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPProtectionStateUpTime"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPTableChassisID"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPTableOperState"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPUpTime"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPGuardTimer"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPAdminState"))
)
if mibBuilder.loadTexts:
    alaVCSPConfigInfoGroup.setStatus("current")

alaVCSPHelperGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 1, 3)
)
alaVCSPHelperGroup.setObjects(
      *(("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPHelperAdminState"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPHelperLinkaggId"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPHelperLinkaggRowStatus"))
)
if mibBuilder.loadTexts:
    alaVCSPHelperGroup.setStatus("current")


# Notification objects

alaVCSPProtectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 0, 1)
)
alaVCSPProtectionTrap.setObjects(
    ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPTableChassisID")
)
if mibBuilder.loadTexts:
    alaVCSPProtectionTrap.setStatus(
        "current"
    )

alaVCSPRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 0, 2)
)
alaVCSPRecoveryTrap.setObjects(
    ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPTableChassisID")
)
if mibBuilder.loadTexts:
    alaVCSPRecoveryTrap.setStatus(
        "current"
    )


# Notifications groups

alaVCSPNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 1, 1)
)
alaVCSPNotificationGroup.setObjects(
      *(("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPProtectionTrap"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPRecoveryTrap"))
)
if mibBuilder.loadTexts:
    alaVCSPNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaVCSPMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 69, 1, 3, 1, 2, 2, 1)
)
alaVCSPMIBCompliance.setObjects(
      *(("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPNotificationGroup"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPConfigInfoGroup"),
        ("ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB", "alaVCSPHelperGroup"))
)
if mibBuilder.loadTexts:
    alaVCSPMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-VC-SPLIT-PROTECTION-MIB",
    **{"AlaVCSPChassisID": AlaVCSPChassisID,
       "AlaVCSPOpState": AlaVCSPOpState,
       "AlaVCSPState": AlaVCSPState,
       "alaVCSPMIB": alaVCSPMIB,
       "alaVCSPMIBNotifications": alaVCSPMIBNotifications,
       "alaVCSPProtectionTrap": alaVCSPProtectionTrap,
       "alaVCSPRecoveryTrap": alaVCSPRecoveryTrap,
       "alaVCSPMIBObjects": alaVCSPMIBObjects,
       "alaVCSPHelperGlobalConfig": alaVCSPHelperGlobalConfig,
       "alaVCSPHelperAdminState": alaVCSPHelperAdminState,
       "alaVCSPConfigInfo": alaVCSPConfigInfo,
       "alaVCSPAdminState": alaVCSPAdminState,
       "alaVCSPLinkaggId": alaVCSPLinkaggId,
       "alaVCSPGuardTimer": alaVCSPGuardTimer,
       "alaVCSPUpTime": alaVCSPUpTime,
       "alaVCSPProtectionStateUpTime": alaVCSPProtectionStateUpTime,
       "alaVCSPHelperLinkaggTable": alaVCSPHelperLinkaggTable,
       "alaVCSPHelperLinkaggEntry": alaVCSPHelperLinkaggEntry,
       "alaVCSPHelperLinkaggId": alaVCSPHelperLinkaggId,
       "alaVCSPHelperLinkaggRowStatus": alaVCSPHelperLinkaggRowStatus,
       "alaVCSPStateTable": alaVCSPStateTable,
       "alaVCSPStateEntry": alaVCSPStateEntry,
       "alaVCSPTableChassisID": alaVCSPTableChassisID,
       "alaVCSPTableOperState": alaVCSPTableOperState,
       "alaVCSPMIBConformance": alaVCSPMIBConformance,
       "alaVCSPMIBGroups": alaVCSPMIBGroups,
       "alaVCSPNotificationGroup": alaVCSPNotificationGroup,
       "alaVCSPConfigInfoGroup": alaVCSPConfigInfoGroup,
       "alaVCSPHelperGroup": alaVCSPHelperGroup,
       "alaVCSPMIBCompliances": alaVCSPMIBCompliances,
       "alaVCSPMIBCompliance": alaVCSPMIBCompliance}
)
