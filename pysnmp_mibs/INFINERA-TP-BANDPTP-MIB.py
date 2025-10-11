# SNMP MIB module (INFINERA-TP-BANDPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-BANDPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:56 2025
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

(FloatTenths,
 InfnCircuitPackType,
 InfnEnableDisable,
 InfnEqptType,
 InfnPmHistStatsControl,
 InfnServiceType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnCircuitPackType",
    "InfnEnableDisable",
    "InfnEqptType",
    "InfnPmHistStatsControl",
    "InfnServiceType")

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


# MODULE-IDENTITY

bandPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20)
)
if mibBuilder.loadTexts:
    bandPtpMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_BandPtpTable_Object = MibTable
bandPtpTable = _BandPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1)
)
if mibBuilder.loadTexts:
    bandPtpTable.setStatus("current")
_BandPtpEntry_Object = MibTableRow
bandPtpEntry = _BandPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1)
)
bandPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    bandPtpEntry.setStatus("current")
_BandPtpProvisionedNeighborTP_Type = DisplayString
_BandPtpProvisionedNeighborTP_Object = MibTableColumn
bandPtpProvisionedNeighborTP = _BandPtpProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 1),
    _BandPtpProvisionedNeighborTP_Type()
)
bandPtpProvisionedNeighborTP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bandPtpProvisionedNeighborTP.setStatus("current")
_BandPtpProvAseTP_Type = DisplayString
_BandPtpProvAseTP_Object = MibTableColumn
bandPtpProvAseTP = _BandPtpProvAseTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 2),
    _BandPtpProvAseTP_Type()
)
bandPtpProvAseTP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpProvAseTP.setStatus("current")
_BandPtpPmHistStatsEnable_Type = InfnPmHistStatsControl
_BandPtpPmHistStatsEnable_Object = MibTableColumn
bandPtpPmHistStatsEnable = _BandPtpPmHistStatsEnable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 3),
    _BandPtpPmHistStatsEnable_Type()
)
bandPtpPmHistStatsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandPtpPmHistStatsEnable.setStatus("current")
_BandPtpBringupLoopbackMode_Type = InfnEnableDisable
_BandPtpBringupLoopbackMode_Object = MibTableColumn
bandPtpBringupLoopbackMode = _BandPtpBringupLoopbackMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 4),
    _BandPtpBringupLoopbackMode_Type()
)
bandPtpBringupLoopbackMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandPtpBringupLoopbackMode.setStatus("current")
_BandPtpTxProvNbrTP_Type = DisplayString
_BandPtpTxProvNbrTP_Object = MibTableColumn
bandPtpTxProvNbrTP = _BandPtpTxProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 5),
    _BandPtpTxProvNbrTP_Type()
)
bandPtpTxProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandPtpTxProvNbrTP.setStatus("current")
_BandPtpRxProvNbrTP_Type = DisplayString
_BandPtpRxProvNbrTP_Object = MibTableColumn
bandPtpRxProvNbrTP = _BandPtpRxProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 6),
    _BandPtpRxProvNbrTP_Type()
)
bandPtpRxProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandPtpRxProvNbrTP.setStatus("current")
_BandPtpTxProvEqptType_Type = InfnEqptType
_BandPtpTxProvEqptType_Object = MibTableColumn
bandPtpTxProvEqptType = _BandPtpTxProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 7),
    _BandPtpTxProvEqptType_Type()
)
bandPtpTxProvEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpTxProvEqptType.setStatus("current")
_BandPtpRxProvEqptType_Type = InfnEqptType
_BandPtpRxProvEqptType_Object = MibTableColumn
bandPtpRxProvEqptType = _BandPtpRxProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 8),
    _BandPtpRxProvEqptType_Type()
)
bandPtpRxProvEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpRxProvEqptType.setStatus("current")
_BandPtpAssociatedEqptType_Type = InfnEqptType
_BandPtpAssociatedEqptType_Object = MibTableColumn
bandPtpAssociatedEqptType = _BandPtpAssociatedEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 9),
    _BandPtpAssociatedEqptType_Type()
)
bandPtpAssociatedEqptType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bandPtpAssociatedEqptType.setStatus("current")
_BandPtpMuxFreqSlotAttenProfile_Type = DisplayString
_BandPtpMuxFreqSlotAttenProfile_Object = MibTableColumn
bandPtpMuxFreqSlotAttenProfile = _BandPtpMuxFreqSlotAttenProfile_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 10),
    _BandPtpMuxFreqSlotAttenProfile_Type()
)
bandPtpMuxFreqSlotAttenProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandPtpMuxFreqSlotAttenProfile.setStatus("current")
_BandPtpDemuxFreqSlotAttenProfile_Type = DisplayString
_BandPtpDemuxFreqSlotAttenProfile_Object = MibTableColumn
bandPtpDemuxFreqSlotAttenProfile = _BandPtpDemuxFreqSlotAttenProfile_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 11),
    _BandPtpDemuxFreqSlotAttenProfile_Type()
)
bandPtpDemuxFreqSlotAttenProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandPtpDemuxFreqSlotAttenProfile.setStatus("current")
_BandPtpProvisionedOpenWaveRemotePtp_Type = DisplayString
_BandPtpProvisionedOpenWaveRemotePtp_Object = MibTableColumn
bandPtpProvisionedOpenWaveRemotePtp = _BandPtpProvisionedOpenWaveRemotePtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 1, 1, 12),
    _BandPtpProvisionedOpenWaveRemotePtp_Type()
)
bandPtpProvisionedOpenWaveRemotePtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bandPtpProvisionedOpenWaveRemotePtp.setStatus("current")
_BandPtpConformance_ObjectIdentity = ObjectIdentity
bandPtpConformance = _BandPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 3)
)
_BandPtpCompliances_ObjectIdentity = ObjectIdentity
bandPtpCompliances = _BandPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 3, 1)
)
_BandPtpGroups_ObjectIdentity = ObjectIdentity
bandPtpGroups = _BandPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 3, 2)
)

# Managed Objects groups

bandPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 3, 2, 1)
)
bandPtpGroup.setObjects(
      *(("INFINERA-TP-BANDPTP-MIB", "bandPtpProvisionedNeighborTP"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpProvAseTP"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpPmHistStatsEnable"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpBringupLoopbackMode"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpTxProvNbrTP"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpRxProvNbrTP"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpTxProvEqptType"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpRxProvEqptType"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpAssociatedEqptType"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpMuxFreqSlotAttenProfile"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpDemuxFreqSlotAttenProfile"),
        ("INFINERA-TP-BANDPTP-MIB", "bandPtpProvisionedOpenWaveRemotePtp"))
)
if mibBuilder.loadTexts:
    bandPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

bandPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 20, 3, 1, 1)
)
bandPtpCompliance.setObjects(
    ("INFINERA-TP-BANDPTP-MIB", "bandPtpGroup")
)
if mibBuilder.loadTexts:
    bandPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-BANDPTP-MIB",
    **{"bandPtpMIB": bandPtpMIB,
       "bandPtpTable": bandPtpTable,
       "bandPtpEntry": bandPtpEntry,
       "bandPtpProvisionedNeighborTP": bandPtpProvisionedNeighborTP,
       "bandPtpProvAseTP": bandPtpProvAseTP,
       "bandPtpPmHistStatsEnable": bandPtpPmHistStatsEnable,
       "bandPtpBringupLoopbackMode": bandPtpBringupLoopbackMode,
       "bandPtpTxProvNbrTP": bandPtpTxProvNbrTP,
       "bandPtpRxProvNbrTP": bandPtpRxProvNbrTP,
       "bandPtpTxProvEqptType": bandPtpTxProvEqptType,
       "bandPtpRxProvEqptType": bandPtpRxProvEqptType,
       "bandPtpAssociatedEqptType": bandPtpAssociatedEqptType,
       "bandPtpMuxFreqSlotAttenProfile": bandPtpMuxFreqSlotAttenProfile,
       "bandPtpDemuxFreqSlotAttenProfile": bandPtpDemuxFreqSlotAttenProfile,
       "bandPtpProvisionedOpenWaveRemotePtp": bandPtpProvisionedOpenWaveRemotePtp,
       "bandPtpConformance": bandPtpConformance,
       "bandPtpCompliances": bandPtpCompliances,
       "bandPtpCompliance": bandPtpCompliance,
       "bandPtpGroups": bandPtpGroups,
       "bandPtpGroup": bandPtpGroup}
)
