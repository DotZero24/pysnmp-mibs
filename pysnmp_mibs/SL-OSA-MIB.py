# SNMP MIB module (SL-OSA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/packetlight/SL-OSA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:11:20 2025
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

slOSA = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SlOSAConfig_ObjectIdentity = ObjectIdentity
slOSAConfig = _SlOSAConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1)
)
_SlOCMConfigTable_Object = MibTable
slOCMConfigTable = _SlOCMConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1)
)
if mibBuilder.loadTexts:
    slOCMConfigTable.setStatus("current")
_SlOCMConfigEntry_Object = MibTableRow
slOCMConfigEntry = _SlOCMConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1)
)
slOCMConfigEntry.setIndexNames(
    (0, "SL-OSA-MIB", "slOCMConfigLineIndex"),
)
if mibBuilder.loadTexts:
    slOCMConfigEntry.setStatus("current")
_SlOCMConfigLineIndex_Type = InterfaceIndex
_SlOCMConfigLineIndex_Object = MibTableColumn
slOCMConfigLineIndex = _SlOCMConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1, 1),
    _SlOCMConfigLineIndex_Type()
)
slOCMConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOCMConfigLineIndex.setStatus("current")
_SlOCMConfigOperStatus_Type = Integer32
_SlOCMConfigOperStatus_Object = MibTableColumn
slOCMConfigOperStatus = _SlOCMConfigOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1, 2),
    _SlOCMConfigOperStatus_Type()
)
slOCMConfigOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOCMConfigOperStatus.setStatus("current")
_SlOCMConfigTemp_Type = Integer32
_SlOCMConfigTemp_Object = MibTableColumn
slOCMConfigTemp = _SlOCMConfigTemp_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1, 3),
    _SlOCMConfigTemp_Type()
)
slOCMConfigTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOCMConfigTemp.setStatus("current")
_SlOCMConfigSNO_Type = DisplayString
_SlOCMConfigSNO_Object = MibTableColumn
slOCMConfigSNO = _SlOCMConfigSNO_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1, 4),
    _SlOCMConfigSNO_Type()
)
slOCMConfigSNO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOCMConfigSNO.setStatus("current")
_SlOCMConfigMFD_Type = DisplayString
_SlOCMConfigMFD_Object = MibTableColumn
slOCMConfigMFD = _SlOCMConfigMFD_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1, 5),
    _SlOCMConfigMFD_Type()
)
slOCMConfigMFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOCMConfigMFD.setStatus("current")
_SlOCMConfigHWR_Type = DisplayString
_SlOCMConfigHWR_Object = MibTableColumn
slOCMConfigHWR = _SlOCMConfigHWR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1, 6),
    _SlOCMConfigHWR_Type()
)
slOCMConfigHWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOCMConfigHWR.setStatus("current")
_SlOCMConfigFWR_Type = DisplayString
_SlOCMConfigFWR_Object = MibTableColumn
slOCMConfigFWR = _SlOCMConfigFWR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1, 7),
    _SlOCMConfigFWR_Type()
)
slOCMConfigFWR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOCMConfigFWR.setStatus("current")
_SlOCMConfigPortLock_Type = Integer32
_SlOCMConfigPortLock_Object = MibTableColumn
slOCMConfigPortLock = _SlOCMConfigPortLock_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1, 8),
    _SlOCMConfigPortLock_Type()
)
slOCMConfigPortLock.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOCMConfigPortLock.setStatus("current")
_SlOCMConfigCycles_Type = Integer32
_SlOCMConfigCycles_Object = MibTableColumn
slOCMConfigCycles = _SlOCMConfigCycles_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1, 9),
    _SlOCMConfigCycles_Type()
)
slOCMConfigCycles.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOCMConfigCycles.setStatus("current")
_SlOCMConfigPN_Type = DisplayString
_SlOCMConfigPN_Object = MibTableColumn
slOCMConfigPN = _SlOCMConfigPN_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 1, 1, 10),
    _SlOCMConfigPN_Type()
)
slOCMConfigPN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOCMConfigPN.setStatus("current")
_SlOSPRConfigTable_Object = MibTable
slOSPRConfigTable = _SlOSPRConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2)
)
if mibBuilder.loadTexts:
    slOSPRConfigTable.setStatus("current")
_SlOSPRConfigEntry_Object = MibTableRow
slOSPRConfigEntry = _SlOSPRConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1)
)
slOSPRConfigEntry.setIndexNames(
    (0, "SL-OSA-MIB", "slOSPRConfigLineIndex"),
)
if mibBuilder.loadTexts:
    slOSPRConfigEntry.setStatus("current")
_SlOSPRConfigLineIndex_Type = InterfaceIndex
_SlOSPRConfigLineIndex_Object = MibTableColumn
slOSPRConfigLineIndex = _SlOSPRConfigLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 1),
    _SlOSPRConfigLineIndex_Type()
)
slOSPRConfigLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSPRConfigLineIndex.setStatus("current")
_SlOSPRConfigAdmin_Type = Integer32
_SlOSPRConfigAdmin_Object = MibTableColumn
slOSPRConfigAdmin = _SlOSPRConfigAdmin_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 2),
    _SlOSPRConfigAdmin_Type()
)
slOSPRConfigAdmin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOSPRConfigAdmin.setStatus("current")
_SlOSPRConfigOper_Type = Integer32
_SlOSPRConfigOper_Object = MibTableColumn
slOSPRConfigOper = _SlOSPRConfigOper_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 3),
    _SlOSPRConfigOper_Type()
)
slOSPRConfigOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSPRConfigOper.setStatus("current")
_SlOSPRConfigAlias_Type = DisplayString
_SlOSPRConfigAlias_Object = MibTableColumn
slOSPRConfigAlias = _SlOSPRConfigAlias_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 4),
    _SlOSPRConfigAlias_Type()
)
slOSPRConfigAlias.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOSPRConfigAlias.setStatus("current")
_SlOSPRConfigGrid_Type = Integer32
_SlOSPRConfigGrid_Object = MibTableColumn
slOSPRConfigGrid = _SlOSPRConfigGrid_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 5),
    _SlOSPRConfigGrid_Type()
)
slOSPRConfigGrid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOSPRConfigGrid.setStatus("current")
_SlOSPRConfigLossDetectThresh_Type = Integer32
_SlOSPRConfigLossDetectThresh_Object = MibTableColumn
slOSPRConfigLossDetectThresh = _SlOSPRConfigLossDetectThresh_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 6),
    _SlOSPRConfigLossDetectThresh_Type()
)
slOSPRConfigLossDetectThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOSPRConfigLossDetectThresh.setStatus("current")
_SlOSPRConfigRefreshTime_Type = Integer32
_SlOSPRConfigRefreshTime_Object = MibTableColumn
slOSPRConfigRefreshTime = _SlOSPRConfigRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 7),
    _SlOSPRConfigRefreshTime_Type()
)
slOSPRConfigRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOSPRConfigRefreshTime.setStatus("current")
_SlOSPRConfigRestoreDefaults_Type = Integer32
_SlOSPRConfigRestoreDefaults_Object = MibTableColumn
slOSPRConfigRestoreDefaults = _SlOSPRConfigRestoreDefaults_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 8),
    _SlOSPRConfigRestoreDefaults_Type()
)
slOSPRConfigRestoreDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOSPRConfigRestoreDefaults.setStatus("current")
_SlOSPRConfigTR_Type = Integer32
_SlOSPRConfigTR_Object = MibTableColumn
slOSPRConfigTR = _SlOSPRConfigTR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 9),
    _SlOSPRConfigTR_Type()
)
slOSPRConfigTR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    slOSPRConfigTR.setStatus("current")
_SlOSPRConfigDL_Type = Integer32
_SlOSPRConfigDL_Object = MibTableColumn
slOSPRConfigDL = _SlOSPRConfigDL_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 10),
    _SlOSPRConfigDL_Type()
)
slOSPRConfigDL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSPRConfigDL.setStatus("current")
_SlOSPRConfigDU_Type = Integer32
_SlOSPRConfigDU_Object = MibTableColumn
slOSPRConfigDU = _SlOSPRConfigDU_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 11),
    _SlOSPRConfigDU_Type()
)
slOSPRConfigDU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSPRConfigDU.setStatus("current")
_SlOSPRConfigNL_Type = Integer32
_SlOSPRConfigNL_Object = MibTableColumn
slOSPRConfigNL = _SlOSPRConfigNL_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 12),
    _SlOSPRConfigNL_Type()
)
slOSPRConfigNL.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSPRConfigNL.setStatus("current")
_SlOSPRConfigNU_Type = Integer32
_SlOSPRConfigNU_Object = MibTableColumn
slOSPRConfigNU = _SlOSPRConfigNU_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 13),
    _SlOSPRConfigNU_Type()
)
slOSPRConfigNU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSPRConfigNU.setStatus("current")
_SlOSPRConfigBWX_Type = Integer32
_SlOSPRConfigBWX_Object = MibTableColumn
slOSPRConfigBWX = _SlOSPRConfigBWX_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 14),
    _SlOSPRConfigBWX_Type()
)
slOSPRConfigBWX.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSPRConfigBWX.setStatus("current")
_SlOSPRConfigNTR_Type = Integer32
_SlOSPRConfigNTR_Object = MibTableColumn
slOSPRConfigNTR = _SlOSPRConfigNTR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 15),
    _SlOSPRConfigNTR_Type()
)
slOSPRConfigNTR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSPRConfigNTR.setStatus("current")
_SlOSPRConfigRBW_Type = Integer32
_SlOSPRConfigRBW_Object = MibTableColumn
slOSPRConfigRBW = _SlOSPRConfigRBW_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 16),
    _SlOSPRConfigRBW_Type()
)
slOSPRConfigRBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSPRConfigRBW.setStatus("current")
_SlOSPRConfigBWT_Type = Integer32
_SlOSPRConfigBWT_Object = MibTableColumn
slOSPRConfigBWT = _SlOSPRConfigBWT_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 2, 1, 17),
    _SlOSPRConfigBWT_Type()
)
slOSPRConfigBWT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSPRConfigBWT.setStatus("current")
_SlOSChannelTable_Object = MibTable
slOSChannelTable = _SlOSChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 3)
)
if mibBuilder.loadTexts:
    slOSChannelTable.setStatus("current")
_SlOSChannelEntry_Object = MibTableRow
slOSChannelEntry = _SlOSChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 3, 1)
)
slOSChannelEntry.setIndexNames(
    (0, "SL-OSA-MIB", "slOSChannelLineIndex"),
    (0, "SL-OSA-MIB", "slOSChannelIndex"),
)
if mibBuilder.loadTexts:
    slOSChannelEntry.setStatus("current")
_SlOSChannelLineIndex_Type = InterfaceIndex
_SlOSChannelLineIndex_Object = MibTableColumn
slOSChannelLineIndex = _SlOSChannelLineIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 3, 1, 1),
    _SlOSChannelLineIndex_Type()
)
slOSChannelLineIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSChannelLineIndex.setStatus("current")
_SlOSChannelIndex_Type = Integer32
_SlOSChannelIndex_Object = MibTableColumn
slOSChannelIndex = _SlOSChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 3, 1, 2),
    _SlOSChannelIndex_Type()
)
slOSChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSChannelIndex.setStatus("current")
_SlOSChannelFR_Type = Integer32
_SlOSChannelFR_Object = MibTableColumn
slOSChannelFR = _SlOSChannelFR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 3, 1, 3),
    _SlOSChannelFR_Type()
)
slOSChannelFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSChannelFR.setStatus("current")
_SlOSChannelPO_Type = Integer32
_SlOSChannelPO_Object = MibTableColumn
slOSChannelPO = _SlOSChannelPO_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 3, 1, 4),
    _SlOSChannelPO_Type()
)
slOSChannelPO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSChannelPO.setStatus("current")
_SlOSChannelBW_Type = Integer32
_SlOSChannelBW_Object = MibTableColumn
slOSChannelBW = _SlOSChannelBW_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 3, 1, 5),
    _SlOSChannelBW_Type()
)
slOSChannelBW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSChannelBW.setStatus("current")
_SlOSChannelOSNR_Type = Integer32
_SlOSChannelOSNR_Object = MibTableColumn
slOSChannelOSNR = _SlOSChannelOSNR_Object(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 1, 3, 1, 6),
    _SlOSChannelOSNR_Type()
)
slOSChannelOSNR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    slOSChannelOSNR.setStatus("current")
_SlOSAPm_ObjectIdentity = ObjectIdentity
slOSAPm = _SlOSAPm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 2)
)
_SlOSATraps_ObjectIdentity = ObjectIdentity
slOSATraps = _SlOSATraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4515, 1, 1, 18, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SL-OSA-MIB",
    **{"slOSA": slOSA,
       "slOSAConfig": slOSAConfig,
       "slOCMConfigTable": slOCMConfigTable,
       "slOCMConfigEntry": slOCMConfigEntry,
       "slOCMConfigLineIndex": slOCMConfigLineIndex,
       "slOCMConfigOperStatus": slOCMConfigOperStatus,
       "slOCMConfigTemp": slOCMConfigTemp,
       "slOCMConfigSNO": slOCMConfigSNO,
       "slOCMConfigMFD": slOCMConfigMFD,
       "slOCMConfigHWR": slOCMConfigHWR,
       "slOCMConfigFWR": slOCMConfigFWR,
       "slOCMConfigPortLock": slOCMConfigPortLock,
       "slOCMConfigCycles": slOCMConfigCycles,
       "slOCMConfigPN": slOCMConfigPN,
       "slOSPRConfigTable": slOSPRConfigTable,
       "slOSPRConfigEntry": slOSPRConfigEntry,
       "slOSPRConfigLineIndex": slOSPRConfigLineIndex,
       "slOSPRConfigAdmin": slOSPRConfigAdmin,
       "slOSPRConfigOper": slOSPRConfigOper,
       "slOSPRConfigAlias": slOSPRConfigAlias,
       "slOSPRConfigGrid": slOSPRConfigGrid,
       "slOSPRConfigLossDetectThresh": slOSPRConfigLossDetectThresh,
       "slOSPRConfigRefreshTime": slOSPRConfigRefreshTime,
       "slOSPRConfigRestoreDefaults": slOSPRConfigRestoreDefaults,
       "slOSPRConfigTR": slOSPRConfigTR,
       "slOSPRConfigDL": slOSPRConfigDL,
       "slOSPRConfigDU": slOSPRConfigDU,
       "slOSPRConfigNL": slOSPRConfigNL,
       "slOSPRConfigNU": slOSPRConfigNU,
       "slOSPRConfigBWX": slOSPRConfigBWX,
       "slOSPRConfigNTR": slOSPRConfigNTR,
       "slOSPRConfigRBW": slOSPRConfigRBW,
       "slOSPRConfigBWT": slOSPRConfigBWT,
       "slOSChannelTable": slOSChannelTable,
       "slOSChannelEntry": slOSChannelEntry,
       "slOSChannelLineIndex": slOSChannelLineIndex,
       "slOSChannelIndex": slOSChannelIndex,
       "slOSChannelFR": slOSChannelFR,
       "slOSChannelPO": slOSChannelPO,
       "slOSChannelBW": slOSChannelBW,
       "slOSChannelOSNR": slOSChannelOSNR,
       "slOSAPm": slOSAPm,
       "slOSATraps": slOSATraps}
)
