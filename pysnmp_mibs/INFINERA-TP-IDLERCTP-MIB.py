# SNMP MIB module (INFINERA-TP-IDLERCTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-IDLERCTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:34 2025
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

(FloatArbitraryPrecision,
 InfnLaserStatus,
 InfnPmHistStatsControl,
 InfnSBSMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatArbitraryPrecision",
    "InfnLaserStatus",
    "InfnPmHistStatsControl",
    "InfnSBSMode")

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

idlerCtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85)
)
if mibBuilder.loadTexts:
    idlerCtpMIB.setRevisions(
        ("2017-06-28 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IdlerCtpTable_Object = MibTable
idlerCtpTable = _IdlerCtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1)
)
if mibBuilder.loadTexts:
    idlerCtpTable.setStatus("current")
_IdlerCtpEntry_Object = MibTableRow
idlerCtpEntry = _IdlerCtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1)
)
idlerCtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    idlerCtpEntry.setStatus("current")
_MoID_Type = DisplayString
_MoID_Object = MibTableColumn
moID = _MoID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 1),
    _MoID_Type()
)
moID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    moID.setStatus("current")
_SbsMode_Type = InfnSBSMode
_SbsMode_Object = MibTableColumn
sbsMode = _SbsMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 2),
    _SbsMode_Type()
)
sbsMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbsMode.setStatus("current")
_SbsAmplitude_Type = FloatArbitraryPrecision
_SbsAmplitude_Object = MibTableColumn
sbsAmplitude = _SbsAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 3),
    _SbsAmplitude_Type()
)
sbsAmplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbsAmplitude.setStatus("current")
_SbsFrequencyWidth_Type = FloatArbitraryPrecision
_SbsFrequencyWidth_Object = MibTableColumn
sbsFrequencyWidth = _SbsFrequencyWidth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 4),
    _SbsFrequencyWidth_Type()
)
sbsFrequencyWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sbsFrequencyWidth.setStatus("current")
_SbsTone_Type = FloatArbitraryPrecision
_SbsTone_Object = MibTableColumn
sbsTone = _SbsTone_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 5),
    _SbsTone_Type()
)
sbsTone.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sbsTone.setStatus("current")
_LaserStatus_Type = InfnLaserStatus
_LaserStatus_Object = MibTableColumn
laserStatus = _LaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 6),
    _LaserStatus_Type()
)
laserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    laserStatus.setStatus("current")
_TargetOpt_Type = FloatArbitraryPrecision
_TargetOpt_Object = MibTableColumn
targetOpt = _TargetOpt_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 7),
    _TargetOpt_Type()
)
targetOpt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    targetOpt.setStatus("current")
_ChannelFrequencyOffset_Type = FloatArbitraryPrecision
_ChannelFrequencyOffset_Object = MibTableColumn
channelFrequencyOffset = _ChannelFrequencyOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 8),
    _ChannelFrequencyOffset_Type()
)
channelFrequencyOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelFrequencyOffset.setStatus("current")
_ChannelFrequency_Type = FloatArbitraryPrecision
_ChannelFrequency_Object = MibTableColumn
channelFrequency = _ChannelFrequency_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 9),
    _ChannelFrequency_Type()
)
channelFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelFrequency.setStatus("current")
_ChannelPower_Type = FloatArbitraryPrecision
_ChannelPower_Object = MibTableColumn
channelPower = _ChannelPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 10),
    _ChannelPower_Type()
)
channelPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    channelPower.setStatus("current")
_PmHistStatsEnable_Type = InfnPmHistStatsControl
_PmHistStatsEnable_Object = MibTableColumn
pmHistStatsEnable = _PmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 1, 1, 11),
    _PmHistStatsEnable_Type()
)
pmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pmHistStatsEnable.setStatus("current")
_IdlerCtpConformance_ObjectIdentity = ObjectIdentity
idlerCtpConformance = _IdlerCtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 3)
)
_IdlerCtpCompliances_ObjectIdentity = ObjectIdentity
idlerCtpCompliances = _IdlerCtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 3, 1)
)
_IdlerCtpGroups_ObjectIdentity = ObjectIdentity
idlerCtpGroups = _IdlerCtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 3, 2)
)

# Managed Objects groups

idlerCtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 3, 2, 1)
)
idlerCtpGroup.setObjects(
      *(("INFINERA-TP-IDLERCTP-MIB", "moID"),
        ("INFINERA-TP-IDLERCTP-MIB", "sbsMode"),
        ("INFINERA-TP-IDLERCTP-MIB", "sbsAmplitude"),
        ("INFINERA-TP-IDLERCTP-MIB", "sbsFrequencyWidth"),
        ("INFINERA-TP-IDLERCTP-MIB", "sbsTone"),
        ("INFINERA-TP-IDLERCTP-MIB", "laserStatus"),
        ("INFINERA-TP-IDLERCTP-MIB", "targetOpt"),
        ("INFINERA-TP-IDLERCTP-MIB", "channelFrequencyOffset"),
        ("INFINERA-TP-IDLERCTP-MIB", "channelFrequency"),
        ("INFINERA-TP-IDLERCTP-MIB", "channelPower"),
        ("INFINERA-TP-IDLERCTP-MIB", "pmHistStatsEnable"))
)
if mibBuilder.loadTexts:
    idlerCtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

idlerCtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 85, 3, 1, 1)
)
idlerCtpCompliance.setObjects(
    ("INFINERA-TP-IDLERCTP-MIB", "idlerCtpGroup")
)
if mibBuilder.loadTexts:
    idlerCtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-IDLERCTP-MIB",
    **{"idlerCtpMIB": idlerCtpMIB,
       "idlerCtpTable": idlerCtpTable,
       "idlerCtpEntry": idlerCtpEntry,
       "moID": moID,
       "sbsMode": sbsMode,
       "sbsAmplitude": sbsAmplitude,
       "sbsFrequencyWidth": sbsFrequencyWidth,
       "sbsTone": sbsTone,
       "laserStatus": laserStatus,
       "targetOpt": targetOpt,
       "channelFrequencyOffset": channelFrequencyOffset,
       "channelFrequency": channelFrequency,
       "channelPower": channelPower,
       "pmHistStatsEnable": pmHistStatsEnable,
       "idlerCtpConformance": idlerCtpConformance,
       "idlerCtpCompliances": idlerCtpCompliances,
       "idlerCtpCompliance": idlerCtpCompliance,
       "idlerCtpGroups": idlerCtpGroups,
       "idlerCtpGroup": idlerCtpGroup}
)
