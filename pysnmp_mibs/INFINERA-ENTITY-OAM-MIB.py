# SNMP MIB module (INFINERA-ENTITY-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:39 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(FloatTenths,
 InfnEqptType,
 InfnOAOperatingMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnEqptType",
    "InfnOAOperatingMode")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

oamMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OamTable_Object = MibTable
oamTable = _OamTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1)
)
if mibBuilder.loadTexts:
    oamTable.setStatus("current")
_OamEntry_Object = MibTableRow
oamEntry = _OamEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1)
)
oamEntry.setIndexNames(
    (0, "ENTITY-MIB", "entPhysicalIndex"),
)
if mibBuilder.loadTexts:
    oamEntry.setStatus("current")
_OamMoId_Type = DisplayString
_OamMoId_Object = MibTableColumn
oamMoId = _OamMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 1),
    _OamMoId_Type()
)
oamMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamMoId.setStatus("current")
_OamProvisonedType_Type = InfnEqptType
_OamProvisonedType_Object = MibTableColumn
oamProvisonedType = _OamProvisonedType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 2),
    _OamProvisonedType_Type()
)
oamProvisonedType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamProvisonedType.setStatus("current")
_OamRxAmpDeviceSetpoint_Type = FloatTenths
_OamRxAmpDeviceSetpoint_Object = MibTableColumn
oamRxAmpDeviceSetpoint = _OamRxAmpDeviceSetpoint_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 3),
    _OamRxAmpDeviceSetpoint_Type()
)
oamRxAmpDeviceSetpoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamRxAmpDeviceSetpoint.setStatus("current")
_OamRxAmpDeviceTarget_Type = FloatTenths
_OamRxAmpDeviceTarget_Object = MibTableColumn
oamRxAmpDeviceTarget = _OamRxAmpDeviceTarget_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 4),
    _OamRxAmpDeviceTarget_Type()
)
oamRxAmpDeviceTarget.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamRxAmpDeviceTarget.setStatus("current")
_OamRxLastAmpDeviceCommitTs_Type = Integer32
_OamRxLastAmpDeviceCommitTs_Object = MibTableColumn
oamRxLastAmpDeviceCommitTs = _OamRxLastAmpDeviceCommitTs_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 5),
    _OamRxLastAmpDeviceCommitTs_Type()
)
oamRxLastAmpDeviceCommitTs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamRxLastAmpDeviceCommitTs.setStatus("current")
_OamLaunchPowerOffset_Type = FloatTenths
_OamLaunchPowerOffset_Object = MibTableColumn
oamLaunchPowerOffset = _OamLaunchPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 6),
    _OamLaunchPowerOffset_Type()
)
oamLaunchPowerOffset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamLaunchPowerOffset.setStatus("current")
_OamRxDampSeqNum_Type = Integer32
_OamRxDampSeqNum_Object = MibTableColumn
oamRxDampSeqNum = _OamRxDampSeqNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 7),
    _OamRxDampSeqNum_Type()
)
oamRxDampSeqNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamRxDampSeqNum.setStatus("current")
_OamTilt_Type = FloatTenths
_OamTilt_Object = MibTableColumn
oamTilt = _OamTilt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 8),
    _OamTilt_Type()
)
oamTilt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamTilt.setStatus("current")
_OamOperatingMode_Type = InfnOAOperatingMode
_OamOperatingMode_Object = MibTableColumn
oamOperatingMode = _OamOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 9),
    _OamOperatingMode_Type()
)
oamOperatingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamOperatingMode.setStatus("current")
_OamGain_Type = FloatTenths
_OamGain_Object = MibTableColumn
oamGain = _OamGain_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 10),
    _OamGain_Type()
)
oamGain.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamGain.setStatus("current")
_OamRowStatus_Type = RowStatus
_OamRowStatus_Object = MibTableColumn
oamRowStatus = _OamRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 11),
    _OamRowStatus_Type()
)
oamRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    oamRowStatus.setStatus("current")
_OamCBandSoakCapableFW_Type = TruthValue
_OamCBandSoakCapableFW_Object = MibTableColumn
oamCBandSoakCapableFW = _OamCBandSoakCapableFW_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 1, 1, 12),
    _OamCBandSoakCapableFW_Type()
)
oamCBandSoakCapableFW.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oamCBandSoakCapableFW.setStatus("current")
_OamConformance_ObjectIdentity = ObjectIdentity
oamConformance = _OamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 3)
)
_OamCompliances_ObjectIdentity = ObjectIdentity
oamCompliances = _OamCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 3, 1)
)
_OamGroups_ObjectIdentity = ObjectIdentity
oamGroups = _OamGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 3, 2)
)

# Managed Objects groups

oamGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 3, 2, 1)
)
oamGroup.setObjects(
      *(("INFINERA-ENTITY-OAM-MIB", "oamMoId"),
        ("INFINERA-ENTITY-OAM-MIB", "oamProvisonedType"),
        ("INFINERA-ENTITY-OAM-MIB", "oamRxAmpDeviceSetpoint"),
        ("INFINERA-ENTITY-OAM-MIB", "oamRxAmpDeviceTarget"),
        ("INFINERA-ENTITY-OAM-MIB", "oamRxLastAmpDeviceCommitTs"),
        ("INFINERA-ENTITY-OAM-MIB", "oamLaunchPowerOffset"),
        ("INFINERA-ENTITY-OAM-MIB", "oamRxDampSeqNum"),
        ("INFINERA-ENTITY-OAM-MIB", "oamTilt"),
        ("INFINERA-ENTITY-OAM-MIB", "oamOperatingMode"),
        ("INFINERA-ENTITY-OAM-MIB", "oamGain"),
        ("INFINERA-ENTITY-OAM-MIB", "oamRowStatus"),
        ("INFINERA-ENTITY-OAM-MIB", "oamCBandSoakCapableFW"))
)
if mibBuilder.loadTexts:
    oamGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

oamCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 11, 3, 1, 1)
)
oamCompliance.setObjects(
    ("INFINERA-ENTITY-OAM-MIB", "oamGroup")
)
if mibBuilder.loadTexts:
    oamCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OAM-MIB",
    **{"oamMIB": oamMIB,
       "oamTable": oamTable,
       "oamEntry": oamEntry,
       "oamMoId": oamMoId,
       "oamProvisonedType": oamProvisonedType,
       "oamRxAmpDeviceSetpoint": oamRxAmpDeviceSetpoint,
       "oamRxAmpDeviceTarget": oamRxAmpDeviceTarget,
       "oamRxLastAmpDeviceCommitTs": oamRxLastAmpDeviceCommitTs,
       "oamLaunchPowerOffset": oamLaunchPowerOffset,
       "oamRxDampSeqNum": oamRxDampSeqNum,
       "oamTilt": oamTilt,
       "oamOperatingMode": oamOperatingMode,
       "oamGain": oamGain,
       "oamRowStatus": oamRowStatus,
       "oamCBandSoakCapableFW": oamCBandSoakCapableFW,
       "oamConformance": oamConformance,
       "oamCompliances": oamCompliances,
       "oamCompliance": oamCompliance,
       "oamGroups": oamGroups,
       "oamGroup": oamGroup}
)
