# SNMP MIB module (SL-OTDR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/packetlight/SL-OTDR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:11:15 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(slService,) = mibBuilder.importSymbols(
    "SL-NE-MIB",
    "slService")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

slOTDR = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlOTDRConfig_ObjectIdentity = ObjectIdentity
slOTDRConfig = _SlOTDRConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1)
)
_SlOTDRMDConfigTable_Object = MibTable
slOTDRMDConfigTable = _SlOTDRMDConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1)
)
if mibBuilder.loadTexts:
    slOTDRMDConfigTable.setStatus("current")
_SlOTDRMDConfigEntry_Object = MibTableRow
slOTDRMDConfigEntry = _SlOTDRMDConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1)
)
slOTDRMDConfigEntry.setIndexNames(
    (0, "SL-OTDR-MIB", "slOTDRMDConfigLineIndex"),
)
if mibBuilder.loadTexts:
    slOTDRMDConfigEntry.setStatus("current")
_SlOTDRMDConfigLineIndex_Type = InterfaceIndex
_SlOTDRMDConfigLineIndex_Object = MibTableColumn
slOTDRMDConfigLineIndex = _SlOTDRMDConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 1),
    _SlOTDRMDConfigLineIndex_Type()
)
slOTDRMDConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRMDConfigLineIndex.setStatus("current")
_SlOTDRMDConfigAdminStatus_Type = Integer32
_SlOTDRMDConfigAdminStatus_Object = MibTableColumn
slOTDRMDConfigAdminStatus = _SlOTDRMDConfigAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 2),
    _SlOTDRMDConfigAdminStatus_Type()
)
slOTDRMDConfigAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRMDConfigAdminStatus.setStatus("current")
_SlOTDRMDConfigOperStatus_Type = Integer32
_SlOTDRMDConfigOperStatus_Object = MibTableColumn
slOTDRMDConfigOperStatus = _SlOTDRMDConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 3),
    _SlOTDRMDConfigOperStatus_Type()
)
slOTDRMDConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRMDConfigOperStatus.setStatus("current")
_SlOTDRMDConfigPN_Type = DisplayString
_SlOTDRMDConfigPN_Object = MibTableColumn
slOTDRMDConfigPN = _SlOTDRMDConfigPN_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 4),
    _SlOTDRMDConfigPN_Type()
)
slOTDRMDConfigPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRMDConfigPN.setStatus("current")
_SlOTDRMDConfigSNO_Type = DisplayString
_SlOTDRMDConfigSNO_Object = MibTableColumn
slOTDRMDConfigSNO = _SlOTDRMDConfigSNO_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 5),
    _SlOTDRMDConfigSNO_Type()
)
slOTDRMDConfigSNO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRMDConfigSNO.setStatus("current")
_SlOTDRMDConfigMF_Type = DisplayString
_SlOTDRMDConfigMF_Object = MibTableColumn
slOTDRMDConfigMF = _SlOTDRMDConfigMF_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 6),
    _SlOTDRMDConfigMF_Type()
)
slOTDRMDConfigMF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRMDConfigMF.setStatus("current")
_SlOTDRMDConfigHWR_Type = DisplayString
_SlOTDRMDConfigHWR_Object = MibTableColumn
slOTDRMDConfigHWR = _SlOTDRMDConfigHWR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 7),
    _SlOTDRMDConfigHWR_Type()
)
slOTDRMDConfigHWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRMDConfigHWR.setStatus("current")
_SlOTDRMDConfigFWR_Type = DisplayString
_SlOTDRMDConfigFWR_Object = MibTableColumn
slOTDRMDConfigFWR = _SlOTDRMDConfigFWR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 8),
    _SlOTDRMDConfigFWR_Type()
)
slOTDRMDConfigFWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRMDConfigFWR.setStatus("current")
_SlOTDRMDConfigPortLock_Type = Integer32
_SlOTDRMDConfigPortLock_Object = MibTableColumn
slOTDRMDConfigPortLock = _SlOTDRMDConfigPortLock_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 9),
    _SlOTDRMDConfigPortLock_Type()
)
slOTDRMDConfigPortLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRMDConfigPortLock.setStatus("current")
_SlOTDRMDConfigCycles_Type = Integer32
_SlOTDRMDConfigCycles_Object = MibTableColumn
slOTDRMDConfigCycles = _SlOTDRMDConfigCycles_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 10),
    _SlOTDRMDConfigCycles_Type()
)
slOTDRMDConfigCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRMDConfigCycles.setStatus("current")
_SlOTDRMDConfigDynamicRange_Type = Integer32
_SlOTDRMDConfigDynamicRange_Object = MibTableColumn
slOTDRMDConfigDynamicRange = _SlOTDRMDConfigDynamicRange_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 1, 1, 11),
    _SlOTDRMDConfigDynamicRange_Type()
)
slOTDRMDConfigDynamicRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRMDConfigDynamicRange.setStatus("current")
_SlOTDRPRConfigTable_Object = MibTable
slOTDRPRConfigTable = _SlOTDRPRConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2)
)
if mibBuilder.loadTexts:
    slOTDRPRConfigTable.setStatus("current")
_SlOTDRPRConfigEntry_Object = MibTableRow
slOTDRPRConfigEntry = _SlOTDRPRConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1)
)
slOTDRPRConfigEntry.setIndexNames(
    (0, "SL-OTDR-MIB", "slOTDRPRConfigLineIndex"),
)
if mibBuilder.loadTexts:
    slOTDRPRConfigEntry.setStatus("current")
_SlOTDRPRConfigLineIndex_Type = InterfaceIndex
_SlOTDRPRConfigLineIndex_Object = MibTableColumn
slOTDRPRConfigLineIndex = _SlOTDRPRConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 1),
    _SlOTDRPRConfigLineIndex_Type()
)
slOTDRPRConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRPRConfigLineIndex.setStatus("current")
_SlOTDRPRConfigAdmin_Type = Integer32
_SlOTDRPRConfigAdmin_Object = MibTableColumn
slOTDRPRConfigAdmin = _SlOTDRPRConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 2),
    _SlOTDRPRConfigAdmin_Type()
)
slOTDRPRConfigAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigAdmin.setStatus("current")
_SlOTDRPRConfigOper_Type = Integer32
_SlOTDRPRConfigOper_Object = MibTableColumn
slOTDRPRConfigOper = _SlOTDRPRConfigOper_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 3),
    _SlOTDRPRConfigOper_Type()
)
slOTDRPRConfigOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDRPRConfigOper.setStatus("current")
_SlOTDRPRConfigAlias_Type = DisplayString
_SlOTDRPRConfigAlias_Object = MibTableColumn
slOTDRPRConfigAlias = _SlOTDRPRConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 4),
    _SlOTDRPRConfigAlias_Type()
)
slOTDRPRConfigAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigAlias.setStatus("current")
_SlOTDRPRConfigUIOR_Type = Integer32
_SlOTDRPRConfigUIOR_Object = MibTableColumn
slOTDRPRConfigUIOR = _SlOTDRPRConfigUIOR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 5),
    _SlOTDRPRConfigUIOR_Type()
)
slOTDRPRConfigUIOR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigUIOR.setStatus("current")
_SlOTDRPRConfigTLOS_Type = Integer32
_SlOTDRPRConfigTLOS_Object = MibTableColumn
slOTDRPRConfigTLOS = _SlOTDRPRConfigTLOS_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 6),
    _SlOTDRPRConfigTLOS_Type()
)
slOTDRPRConfigTLOS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigTLOS.setStatus("current")
_SlOTDRPRConfigTREF_Type = Integer32
_SlOTDRPRConfigTREF_Object = MibTableColumn
slOTDRPRConfigTREF = _SlOTDRPRConfigTREF_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 7),
    _SlOTDRPRConfigTREF_Type()
)
slOTDRPRConfigTREF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigTREF.setStatus("current")
_SlOTDRPRConfigMTIM_Type = Integer32
_SlOTDRPRConfigMTIM_Object = MibTableColumn
slOTDRPRConfigMTIM = _SlOTDRPRConfigMTIM_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 8),
    _SlOTDRPRConfigMTIM_Type()
)
slOTDRPRConfigMTIM.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigMTIM.setStatus("current")
_SlOTDRPRConfigDIST_Type = Integer32
_SlOTDRPRConfigDIST_Object = MibTableColumn
slOTDRPRConfigDIST = _SlOTDRPRConfigDIST_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 9),
    _SlOTDRPRConfigDIST_Type()
)
slOTDRPRConfigDIST.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigDIST.setStatus("current")
_SlOTDRPRConfigPWIDTH_Type = Integer32
_SlOTDRPRConfigPWIDTH_Object = MibTableColumn
slOTDRPRConfigPWIDTH = _SlOTDRPRConfigPWIDTH_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 10),
    _SlOTDRPRConfigPWIDTH_Type()
)
slOTDRPRConfigPWIDTH.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigPWIDTH.setStatus("current")
_SlOTDRPRConfigRESOL_Type = Integer32
_SlOTDRPRConfigRESOL_Object = MibTableColumn
slOTDRPRConfigRESOL = _SlOTDRPRConfigRESOL_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 11),
    _SlOTDRPRConfigRESOL_Type()
)
slOTDRPRConfigRESOL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigRESOL.setStatus("current")
_SlOTDRPRConfigTEOF_Type = Integer32
_SlOTDRPRConfigTEOF_Object = MibTableColumn
slOTDRPRConfigTEOF = _SlOTDRPRConfigTEOF_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 12),
    _SlOTDRPRConfigTEOF_Type()
)
slOTDRPRConfigTEOF.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigTEOF.setStatus("current")
_SlOTDRPRConfigRefSavRmv_Type = Integer32
_SlOTDRPRConfigRefSavRmv_Object = MibTableColumn
slOTDRPRConfigRefSavRmv = _SlOTDRPRConfigRefSavRmv_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 2, 1, 13),
    _SlOTDRPRConfigRefSavRmv_Type()
)
slOTDRPRConfigRefSavRmv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOTDRPRConfigRefSavRmv.setStatus("current")
_SlOTDREventTable_Object = MibTable
slOTDREventTable = _SlOTDREventTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 3)
)
if mibBuilder.loadTexts:
    slOTDREventTable.setStatus("current")
_SlOTDREventEntry_Object = MibTableRow
slOTDREventEntry = _SlOTDREventEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 3, 1)
)
slOTDREventEntry.setIndexNames(
    (0, "SL-OTDR-MIB", "slOTDREventLineIndex"),
    (0, "SL-OTDR-MIB", "slOTDREventTableIndex"),
    (0, "SL-OTDR-MIB", "slOTDREventIndex"),
)
if mibBuilder.loadTexts:
    slOTDREventEntry.setStatus("current")
_SlOTDREventLineIndex_Type = InterfaceIndex
_SlOTDREventLineIndex_Object = MibTableColumn
slOTDREventLineIndex = _SlOTDREventLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 3, 1, 1),
    _SlOTDREventLineIndex_Type()
)
slOTDREventLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDREventLineIndex.setStatus("current")
_SlOTDREventTableIndex_Type = Integer32
_SlOTDREventTableIndex_Object = MibTableColumn
slOTDREventTableIndex = _SlOTDREventTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 3, 1, 2),
    _SlOTDREventTableIndex_Type()
)
slOTDREventTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDREventTableIndex.setStatus("current")
_SlOTDREventIndex_Type = Integer32
_SlOTDREventIndex_Object = MibTableColumn
slOTDREventIndex = _SlOTDREventIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 3, 1, 3),
    _SlOTDREventIndex_Type()
)
slOTDREventIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDREventIndex.setStatus("current")
_SlOTDREventType_Type = Integer32
_SlOTDREventType_Object = MibTableColumn
slOTDREventType = _SlOTDREventType_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 3, 1, 4),
    _SlOTDREventType_Type()
)
slOTDREventType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDREventType.setStatus("current")
_SlOTDREventDistance_Type = Integer32
_SlOTDREventDistance_Object = MibTableColumn
slOTDREventDistance = _SlOTDREventDistance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 3, 1, 5),
    _SlOTDREventDistance_Type()
)
slOTDREventDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDREventDistance.setStatus("current")
_SlOTDREventReflectance_Type = Integer32
_SlOTDREventReflectance_Object = MibTableColumn
slOTDREventReflectance = _SlOTDREventReflectance_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 3, 1, 6),
    _SlOTDREventReflectance_Type()
)
slOTDREventReflectance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDREventReflectance.setStatus("current")
_SlOTDREventLoss_Type = Integer32
_SlOTDREventLoss_Object = MibTableColumn
slOTDREventLoss = _SlOTDREventLoss_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 3, 1, 7),
    _SlOTDREventLoss_Type()
)
slOTDREventLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDREventLoss.setStatus("current")
_SlOTDREventTLoss_Type = Integer32
_SlOTDREventTLoss_Object = MibTableColumn
slOTDREventTLoss = _SlOTDREventTLoss_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 1, 3, 1, 8),
    _SlOTDREventTLoss_Type()
)
slOTDREventTLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOTDREventTLoss.setStatus("current")
_SlOTDRPm_ObjectIdentity = ObjectIdentity
slOTDRPm = _SlOTDRPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 2)
)
_SlOTDRTraps_ObjectIdentity = ObjectIdentity
slOTDRTraps = _SlOTDRTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 19, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-OTDR-MIB",
    **{"slOTDR": slOTDR,
       "slOTDRConfig": slOTDRConfig,
       "slOTDRMDConfigTable": slOTDRMDConfigTable,
       "slOTDRMDConfigEntry": slOTDRMDConfigEntry,
       "slOTDRMDConfigLineIndex": slOTDRMDConfigLineIndex,
       "slOTDRMDConfigAdminStatus": slOTDRMDConfigAdminStatus,
       "slOTDRMDConfigOperStatus": slOTDRMDConfigOperStatus,
       "slOTDRMDConfigPN": slOTDRMDConfigPN,
       "slOTDRMDConfigSNO": slOTDRMDConfigSNO,
       "slOTDRMDConfigMF": slOTDRMDConfigMF,
       "slOTDRMDConfigHWR": slOTDRMDConfigHWR,
       "slOTDRMDConfigFWR": slOTDRMDConfigFWR,
       "slOTDRMDConfigPortLock": slOTDRMDConfigPortLock,
       "slOTDRMDConfigCycles": slOTDRMDConfigCycles,
       "slOTDRMDConfigDynamicRange": slOTDRMDConfigDynamicRange,
       "slOTDRPRConfigTable": slOTDRPRConfigTable,
       "slOTDRPRConfigEntry": slOTDRPRConfigEntry,
       "slOTDRPRConfigLineIndex": slOTDRPRConfigLineIndex,
       "slOTDRPRConfigAdmin": slOTDRPRConfigAdmin,
       "slOTDRPRConfigOper": slOTDRPRConfigOper,
       "slOTDRPRConfigAlias": slOTDRPRConfigAlias,
       "slOTDRPRConfigUIOR": slOTDRPRConfigUIOR,
       "slOTDRPRConfigTLOS": slOTDRPRConfigTLOS,
       "slOTDRPRConfigTREF": slOTDRPRConfigTREF,
       "slOTDRPRConfigMTIM": slOTDRPRConfigMTIM,
       "slOTDRPRConfigDIST": slOTDRPRConfigDIST,
       "slOTDRPRConfigPWIDTH": slOTDRPRConfigPWIDTH,
       "slOTDRPRConfigRESOL": slOTDRPRConfigRESOL,
       "slOTDRPRConfigTEOF": slOTDRPRConfigTEOF,
       "slOTDRPRConfigRefSavRmv": slOTDRPRConfigRefSavRmv,
       "slOTDREventTable": slOTDREventTable,
       "slOTDREventEntry": slOTDREventEntry,
       "slOTDREventLineIndex": slOTDREventLineIndex,
       "slOTDREventTableIndex": slOTDREventTableIndex,
       "slOTDREventIndex": slOTDREventIndex,
       "slOTDREventType": slOTDREventType,
       "slOTDREventDistance": slOTDREventDistance,
       "slOTDREventReflectance": slOTDREventReflectance,
       "slOTDREventLoss": slOTDREventLoss,
       "slOTDREventTLoss": slOTDREventTLoss,
       "slOTDRPm": slOTDRPm,
       "slOTDRTraps": slOTDRTraps}
)
