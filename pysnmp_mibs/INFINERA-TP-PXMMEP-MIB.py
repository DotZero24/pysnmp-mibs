# SNMP MIB module (INFINERA-TP-PXMMEP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PXMMEP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:13 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(InfnAISInterval,
 InfnCFMAction,
 InfnCSFInterval,
 InfnEnableDisable,
 InfnEnableDisableType,
 InfnEqptType,
 InfnInterfaceStatusTLV,
 InfnIsEnabled,
 InfnLowestPriDef,
 InfnMepDirection,
 InfnMepRole,
 InfnPortStatusTLV) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnAISInterval",
    "InfnCFMAction",
    "InfnCSFInterval",
    "InfnEnableDisable",
    "InfnEnableDisableType",
    "InfnEqptType",
    "InfnInterfaceStatusTLV",
    "InfnIsEnabled",
    "InfnLowestPriDef",
    "InfnMepDirection",
    "InfnMepRole",
    "InfnPortStatusTLV")

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

mepMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_MepTable_Object = MibTable
mepTable = _MepTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1)
)
if mibBuilder.loadTexts:
    mepTable.setStatus("current")
_MepEntry_Object = MibTableRow
mepEntry = _MepEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1)
)
mepEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    mepEntry.setStatus("current")
_MepMaaId_Type = DisplayString
_MepMaaId_Object = MibTableColumn
mepMaaId = _MepMaaId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 1),
    _MepMaaId_Type()
)
mepMaaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mepMaaId.setStatus("current")
_MepRole_Type = InfnMepRole
_MepRole_Object = MibTableColumn
mepRole = _MepRole_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 2),
    _MepRole_Type()
)
mepRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mepRole.setStatus("current")
_MepCCIEnabled_Type = InfnIsEnabled
_MepCCIEnabled_Object = MibTableColumn
mepCCIEnabled = _MepCCIEnabled_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 3),
    _MepCCIEnabled_Type()
)
mepCCIEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepCCIEnabled.setStatus("current")
_MepMDLevel_Type = Integer32
_MepMDLevel_Object = MibTableColumn
mepMDLevel = _MepMDLevel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 4),
    _MepMDLevel_Type()
)
mepMDLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mepMDLevel.setStatus("current")
_MepOuterPrimaryVID_Type = Integer32
_MepOuterPrimaryVID_Object = MibTableColumn
mepOuterPrimaryVID = _MepOuterPrimaryVID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 5),
    _MepOuterPrimaryVID_Type()
)
mepOuterPrimaryVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepOuterPrimaryVID.setStatus("current")
_MepInnerPrimaryVID_Type = Integer32
_MepInnerPrimaryVID_Object = MibTableColumn
mepInnerPrimaryVID = _MepInnerPrimaryVID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 6),
    _MepInnerPrimaryVID_Type()
)
mepInnerPrimaryVID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepInnerPrimaryVID.setStatus("current")
_MepId_Type = Integer32
_MepId_Object = MibTableColumn
mepId = _MepId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 7),
    _MepId_Type()
)
mepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepId.setStatus("current")
_MepRMEPCrossCheck_Type = InfnEnableDisable
_MepRMEPCrossCheck_Object = MibTableColumn
mepRMEPCrossCheck = _MepRMEPCrossCheck_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 8),
    _MepRMEPCrossCheck_Type()
)
mepRMEPCrossCheck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepRMEPCrossCheck.setStatus("current")
_MepDirection_Type = InfnMepDirection
_MepDirection_Object = MibTableColumn
mepDirection = _MepDirection_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 9),
    _MepDirection_Type()
)
mepDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepDirection.setStatus("current")
_MepCcmPriority_Type = Integer32
_MepCcmPriority_Object = MibTableColumn
mepCcmPriority = _MepCcmPriority_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 10),
    _MepCcmPriority_Type()
)
mepCcmPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepCcmPriority.setStatus("current")
_MepCcmDEI_Type = InfnIsEnabled
_MepCcmDEI_Object = MibTableColumn
mepCcmDEI = _MepCcmDEI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 11),
    _MepCcmDEI_Type()
)
mepCcmDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepCcmDEI.setStatus("current")
_MepMacAddress_Type = DisplayString
_MepMacAddress_Object = MibTableColumn
mepMacAddress = _MepMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 12),
    _MepMacAddress_Type()
)
mepMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mepMacAddress.setStatus("current")
_MepLowestPriorityDefect_Type = InfnLowestPriDef
_MepLowestPriorityDefect_Object = MibTableColumn
mepLowestPriorityDefect = _MepLowestPriorityDefect_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 13),
    _MepLowestPriorityDefect_Type()
)
mepLowestPriorityDefect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepLowestPriorityDefect.setStatus("current")
_MepPortStatusTLV_Type = InfnPortStatusTLV
_MepPortStatusTLV_Object = MibTableColumn
mepPortStatusTLV = _MepPortStatusTLV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 14),
    _MepPortStatusTLV_Type()
)
mepPortStatusTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mepPortStatusTLV.setStatus("current")
_MepInterfaceStatusTLV_Type = InfnInterfaceStatusTLV
_MepInterfaceStatusTLV_Object = MibTableColumn
mepInterfaceStatusTLV = _MepInterfaceStatusTLV_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 15),
    _MepInterfaceStatusTLV_Type()
)
mepInterfaceStatusTLV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mepInterfaceStatusTLV.setStatus("current")
_MepSomeRMEPDefectCFMAction_Type = InfnCFMAction
_MepSomeRMEPDefectCFMAction_Object = MibTableColumn
mepSomeRMEPDefectCFMAction = _MepSomeRMEPDefectCFMAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 16),
    _MepSomeRMEPDefectCFMAction_Type()
)
mepSomeRMEPDefectCFMAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepSomeRMEPDefectCFMAction.setStatus("current")
_MepXconnDefectCFMAction_Type = InfnCFMAction
_MepXconnDefectCFMAction_Object = MibTableColumn
mepXconnDefectCFMAction = _MepXconnDefectCFMAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 17),
    _MepXconnDefectCFMAction_Type()
)
mepXconnDefectCFMAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepXconnDefectCFMAction.setStatus("current")
_MepErrorCCMDefectCFMAction_Type = InfnCFMAction
_MepErrorCCMDefectCFMAction_Object = MibTableColumn
mepErrorCCMDefectCFMAction = _MepErrorCCMDefectCFMAction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 18),
    _MepErrorCCMDefectCFMAction_Type()
)
mepErrorCCMDefectCFMAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepErrorCCMDefectCFMAction.setStatus("current")
_MepSomeMACStatusDefectCFMaction_Type = InfnCFMAction
_MepSomeMACStatusDefectCFMaction_Object = MibTableColumn
mepSomeMACStatusDefectCFMaction = _MepSomeMACStatusDefectCFMaction_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 19),
    _MepSomeMACStatusDefectCFMaction_Type()
)
mepSomeMACStatusDefectCFMaction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepSomeMACStatusDefectCFMaction.setStatus("current")
_MepAISCapability_Type = InfnIsEnabled
_MepAISCapability_Object = MibTableColumn
mepAISCapability = _MepAISCapability_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 20),
    _MepAISCapability_Type()
)
mepAISCapability.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepAISCapability.setStatus("current")
_MepClientMDLevel_Type = Integer32
_MepClientMDLevel_Object = MibTableColumn
mepClientMDLevel = _MepClientMDLevel_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 21),
    _MepClientMDLevel_Type()
)
mepClientMDLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepClientMDLevel.setStatus("current")
_MepAISInterval_Type = InfnAISInterval
_MepAISInterval_Object = MibTableColumn
mepAISInterval = _MepAISInterval_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 22),
    _MepAISInterval_Type()
)
mepAISInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepAISInterval.setStatus("current")
_MepAisPriority_Type = Integer32
_MepAisPriority_Object = MibTableColumn
mepAisPriority = _MepAisPriority_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 23),
    _MepAisPriority_Type()
)
mepAisPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepAisPriority.setStatus("current")
_MepAisDEI_Type = InfnIsEnabled
_MepAisDEI_Object = MibTableColumn
mepAisDEI = _MepAisDEI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 24),
    _MepAisDEI_Type()
)
mepAisDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepAisDEI.setStatus("current")
_MepPmHistStatsEnable_Type = InfnEnableDisable
_MepPmHistStatsEnable_Object = MibTableColumn
mepPmHistStatsEnable = _MepPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 25),
    _MepPmHistStatsEnable_Type()
)
mepPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepPmHistStatsEnable.setStatus("current")
_MepCSFSupport_Type = InfnEnableDisableType
_MepCSFSupport_Object = MibTableColumn
mepCSFSupport = _MepCSFSupport_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 26),
    _MepCSFSupport_Type()
)
mepCSFSupport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepCSFSupport.setStatus("current")
_MepCSFInterval_Type = InfnCSFInterval
_MepCSFInterval_Object = MibTableColumn
mepCSFInterval = _MepCSFInterval_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 27),
    _MepCSFInterval_Type()
)
mepCSFInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepCSFInterval.setStatus("current")
_MepCSFPriority_Type = Integer32
_MepCSFPriority_Object = MibTableColumn
mepCSFPriority = _MepCSFPriority_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 28),
    _MepCSFPriority_Type()
)
mepCSFPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepCSFPriority.setStatus("current")
_MepCSFDEI_Type = InfnIsEnabled
_MepCSFDEI_Object = MibTableColumn
mepCSFDEI = _MepCSFDEI_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 1, 1, 29),
    _MepCSFDEI_Type()
)
mepCSFDEI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mepCSFDEI.setStatus("current")
_MepConformance_ObjectIdentity = ObjectIdentity
mepConformance = _MepConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 3)
)
_MepCompliances_ObjectIdentity = ObjectIdentity
mepCompliances = _MepCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 3, 1)
)
_MepGroups_ObjectIdentity = ObjectIdentity
mepGroups = _MepGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 3, 2)
)

# Managed Objects groups

mepGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 3, 2, 1)
)
mepGroup.setObjects(
      *(("INFINERA-TP-PXMMEP-MIB", "mepMaaId"),
        ("INFINERA-TP-PXMMEP-MIB", "mepRole"),
        ("INFINERA-TP-PXMMEP-MIB", "mepCCIEnabled"),
        ("INFINERA-TP-PXMMEP-MIB", "mepMDLevel"),
        ("INFINERA-TP-PXMMEP-MIB", "mepOuterPrimaryVID"),
        ("INFINERA-TP-PXMMEP-MIB", "mepInnerPrimaryVID"),
        ("INFINERA-TP-PXMMEP-MIB", "mepId"),
        ("INFINERA-TP-PXMMEP-MIB", "mepRMEPCrossCheck"),
        ("INFINERA-TP-PXMMEP-MIB", "mepDirection"),
        ("INFINERA-TP-PXMMEP-MIB", "mepCcmPriority"),
        ("INFINERA-TP-PXMMEP-MIB", "mepCcmDEI"),
        ("INFINERA-TP-PXMMEP-MIB", "mepMacAddress"),
        ("INFINERA-TP-PXMMEP-MIB", "mepLowestPriorityDefect"),
        ("INFINERA-TP-PXMMEP-MIB", "mepPortStatusTLV"),
        ("INFINERA-TP-PXMMEP-MIB", "mepInterfaceStatusTLV"),
        ("INFINERA-TP-PXMMEP-MIB", "mepSomeRMEPDefectCFMAction"),
        ("INFINERA-TP-PXMMEP-MIB", "mepXconnDefectCFMAction"),
        ("INFINERA-TP-PXMMEP-MIB", "mepErrorCCMDefectCFMAction"),
        ("INFINERA-TP-PXMMEP-MIB", "mepSomeMACStatusDefectCFMaction"),
        ("INFINERA-TP-PXMMEP-MIB", "mepAISCapability"),
        ("INFINERA-TP-PXMMEP-MIB", "mepClientMDLevel"),
        ("INFINERA-TP-PXMMEP-MIB", "mepAISInterval"),
        ("INFINERA-TP-PXMMEP-MIB", "mepAisPriority"),
        ("INFINERA-TP-PXMMEP-MIB", "mepAisDEI"),
        ("INFINERA-TP-PXMMEP-MIB", "mepPmHistStatsEnable"),
        ("INFINERA-TP-PXMMEP-MIB", "mepCSFSupport"),
        ("INFINERA-TP-PXMMEP-MIB", "mepCSFInterval"),
        ("INFINERA-TP-PXMMEP-MIB", "mepCSFPriority"),
        ("INFINERA-TP-PXMMEP-MIB", "mepCSFDEI"))
)
if mibBuilder.loadTexts:
    mepGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

mepCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 43, 3, 1, 1)
)
mepCompliance.setObjects(
    ("INFINERA-TP-PXMMEP-MIB", "mepGroup")
)
if mibBuilder.loadTexts:
    mepCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PXMMEP-MIB",
    **{"mepMIB": mepMIB,
       "mepTable": mepTable,
       "mepEntry": mepEntry,
       "mepMaaId": mepMaaId,
       "mepRole": mepRole,
       "mepCCIEnabled": mepCCIEnabled,
       "mepMDLevel": mepMDLevel,
       "mepOuterPrimaryVID": mepOuterPrimaryVID,
       "mepInnerPrimaryVID": mepInnerPrimaryVID,
       "mepId": mepId,
       "mepRMEPCrossCheck": mepRMEPCrossCheck,
       "mepDirection": mepDirection,
       "mepCcmPriority": mepCcmPriority,
       "mepCcmDEI": mepCcmDEI,
       "mepMacAddress": mepMacAddress,
       "mepLowestPriorityDefect": mepLowestPriorityDefect,
       "mepPortStatusTLV": mepPortStatusTLV,
       "mepInterfaceStatusTLV": mepInterfaceStatusTLV,
       "mepSomeRMEPDefectCFMAction": mepSomeRMEPDefectCFMAction,
       "mepXconnDefectCFMAction": mepXconnDefectCFMAction,
       "mepErrorCCMDefectCFMAction": mepErrorCCMDefectCFMAction,
       "mepSomeMACStatusDefectCFMaction": mepSomeMACStatusDefectCFMaction,
       "mepAISCapability": mepAISCapability,
       "mepClientMDLevel": mepClientMDLevel,
       "mepAISInterval": mepAISInterval,
       "mepAisPriority": mepAisPriority,
       "mepAisDEI": mepAisDEI,
       "mepPmHistStatsEnable": mepPmHistStatsEnable,
       "mepCSFSupport": mepCSFSupport,
       "mepCSFInterval": mepCSFInterval,
       "mepCSFPriority": mepCSFPriority,
       "mepCSFDEI": mepCSFDEI,
       "mepConformance": mepConformance,
       "mepCompliances": mepCompliances,
       "mepCompliance": mepCompliance,
       "mepGroups": mepGroups,
       "mepGroup": mepGroup}
)
