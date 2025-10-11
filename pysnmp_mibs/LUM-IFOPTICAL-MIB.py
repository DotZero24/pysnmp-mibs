# SNMP MIB module (LUM-IFOPTICAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFOPTICAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:46 2025
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

(lumIfOpticalMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfOpticalMIB",
    "lumModules")

(BerLevelMTOSI,
 DispersionSearchLimit,
 EnabledDisabledWithNA,
 FaultStatus,
 FaultStatusWithNA,
 FecType,
 Frequency,
 FrequencyOnlyNotApplicable,
 LaneFrequency,
 LaserMode,
 MgmtNameString,
 OnOff,
 ResetWithNA,
 SignalStatusWithNA,
 Signed32WithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "BerLevelMTOSI",
    "DispersionSearchLimit",
    "EnabledDisabledWithNA",
    "FaultStatus",
    "FaultStatusWithNA",
    "FecType",
    "Frequency",
    "FrequencyOnlyNotApplicable",
    "LaneFrequency",
    "LaserMode",
    "MgmtNameString",
    "OnOff",
    "ResetWithNA",
    "SignalStatusWithNA",
    "Signed32WithNA",
    "Unsigned32WithNA")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lumIfOpticalMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 48)
)
if mibBuilder.loadTexts:
    lumIfOpticalMIBModule.setRevisions(
        ("2017-08-30 00:00",
         "2017-06-15 00:00",
         "2017-04-17 00:00",
         "2016-11-30 00:00",
         "2015-12-22 00:00",
         "2015-11-30 00:00",
         "2014-09-30 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2013-05-31 00:00",
         "2012-11-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfOpticalConfs_ObjectIdentity = ObjectIdentity
lumIfOpticalConfs = _LumIfOpticalConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1)
)
_LumIfOpticalGroups_ObjectIdentity = ObjectIdentity
lumIfOpticalGroups = _LumIfOpticalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1)
)
_LumIfOpticalCompl_ObjectIdentity = ObjectIdentity
lumIfOpticalCompl = _LumIfOpticalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2)
)
_LumIfOpticalMIBObjects_ObjectIdentity = ObjectIdentity
lumIfOpticalMIBObjects = _LumIfOpticalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2)
)
_IfOpticalGeneral_ObjectIdentity = ObjectIdentity
ifOpticalGeneral = _IfOpticalGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1)
)
_IfOpticalGeneralConfigLastChangeTime_Type = DateAndTime
_IfOpticalGeneralConfigLastChangeTime_Object = MibScalar
ifOpticalGeneralConfigLastChangeTime = _IfOpticalGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 1),
    _IfOpticalGeneralConfigLastChangeTime_Type()
)
ifOpticalGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralConfigLastChangeTime.setStatus("current")
_IfOpticalGeneralStateLastChangeTime_Type = DateAndTime
_IfOpticalGeneralStateLastChangeTime_Object = MibScalar
ifOpticalGeneralStateLastChangeTime = _IfOpticalGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 2),
    _IfOpticalGeneralStateLastChangeTime_Type()
)
ifOpticalGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralStateLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalTransSectionTableSize_Type = Unsigned32
_IfOpticalGeneralIfOpticalTransSectionTableSize_Object = MibScalar
ifOpticalGeneralIfOpticalTransSectionTableSize = _IfOpticalGeneralIfOpticalTransSectionTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 3),
    _IfOpticalGeneralIfOpticalTransSectionTableSize_Type()
)
ifOpticalGeneralIfOpticalTransSectionTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalTransSectionTableSize.setStatus("current")
_IfOpticalGeneralIfOpticalTransSectionConfigLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalTransSectionConfigLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalTransSectionConfigLastChangeTime = _IfOpticalGeneralIfOpticalTransSectionConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 4),
    _IfOpticalGeneralIfOpticalTransSectionConfigLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalTransSectionConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalTransSectionConfigLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalTransSectionStateLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalTransSectionStateLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalTransSectionStateLastChangeTime = _IfOpticalGeneralIfOpticalTransSectionStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 5),
    _IfOpticalGeneralIfOpticalTransSectionStateLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalTransSectionStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalTransSectionStateLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalChannelTableSize_Type = Unsigned32
_IfOpticalGeneralIfOpticalChannelTableSize_Object = MibScalar
ifOpticalGeneralIfOpticalChannelTableSize = _IfOpticalGeneralIfOpticalChannelTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 6),
    _IfOpticalGeneralIfOpticalChannelTableSize_Type()
)
ifOpticalGeneralIfOpticalChannelTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalChannelTableSize.setStatus("current")
_IfOpticalGeneralIfOpticalChannelConfigLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalChannelConfigLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalChannelConfigLastChangeTime = _IfOpticalGeneralIfOpticalChannelConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 7),
    _IfOpticalGeneralIfOpticalChannelConfigLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalChannelConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalChannelConfigLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalChannelStateLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalChannelStateLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalChannelStateLastChangeTime = _IfOpticalGeneralIfOpticalChannelStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 8),
    _IfOpticalGeneralIfOpticalChannelStateLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalChannelStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalChannelStateLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalDigitalSignalRateTableSize_Type = Unsigned32
_IfOpticalGeneralIfOpticalDigitalSignalRateTableSize_Object = MibScalar
ifOpticalGeneralIfOpticalDigitalSignalRateTableSize = _IfOpticalGeneralIfOpticalDigitalSignalRateTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 9),
    _IfOpticalGeneralIfOpticalDigitalSignalRateTableSize_Type()
)
ifOpticalGeneralIfOpticalDigitalSignalRateTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalDigitalSignalRateTableSize.setStatus("current")
_IfOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime = _IfOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 10),
    _IfOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime = _IfOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 11),
    _IfOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalFecTableSize_Type = Unsigned32
_IfOpticalGeneralIfOpticalFecTableSize_Object = MibScalar
ifOpticalGeneralIfOpticalFecTableSize = _IfOpticalGeneralIfOpticalFecTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 12),
    _IfOpticalGeneralIfOpticalFecTableSize_Type()
)
ifOpticalGeneralIfOpticalFecTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalFecTableSize.setStatus("current")
_IfOpticalGeneralIfOpticalFecConfigLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalFecConfigLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalFecConfigLastChangeTime = _IfOpticalGeneralIfOpticalFecConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 13),
    _IfOpticalGeneralIfOpticalFecConfigLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalFecConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalFecConfigLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalFecStateLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalFecStateLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalFecStateLastChangeTime = _IfOpticalGeneralIfOpticalFecStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 14),
    _IfOpticalGeneralIfOpticalFecStateLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalFecStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalFecStateLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalTransLaneCarrierTableSize_Type = Unsigned32
_IfOpticalGeneralIfOpticalTransLaneCarrierTableSize_Object = MibScalar
ifOpticalGeneralIfOpticalTransLaneCarrierTableSize = _IfOpticalGeneralIfOpticalTransLaneCarrierTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 15),
    _IfOpticalGeneralIfOpticalTransLaneCarrierTableSize_Type()
)
ifOpticalGeneralIfOpticalTransLaneCarrierTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalTransLaneCarrierTableSize.setStatus("current")
_IfOpticalGeneralIfOpticalTransLaneCarrierConfigLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalTransLaneCarrierConfigLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalTransLaneCarrierConfigLastChangeTime = _IfOpticalGeneralIfOpticalTransLaneCarrierConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 16),
    _IfOpticalGeneralIfOpticalTransLaneCarrierConfigLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalTransLaneCarrierConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalTransLaneCarrierConfigLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalTransLaneCarrierStateLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalTransLaneCarrierStateLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalTransLaneCarrierStateLastChangeTime = _IfOpticalGeneralIfOpticalTransLaneCarrierStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 17),
    _IfOpticalGeneralIfOpticalTransLaneCarrierStateLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalTransLaneCarrierStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalTransLaneCarrierStateLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalTransLaneCarrierGroupTableSize_Type = Unsigned32
_IfOpticalGeneralIfOpticalTransLaneCarrierGroupTableSize_Object = MibScalar
ifOpticalGeneralIfOpticalTransLaneCarrierGroupTableSize = _IfOpticalGeneralIfOpticalTransLaneCarrierGroupTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 18),
    _IfOpticalGeneralIfOpticalTransLaneCarrierGroupTableSize_Type()
)
ifOpticalGeneralIfOpticalTransLaneCarrierGroupTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalTransLaneCarrierGroupTableSize.setStatus("current")
_IfOpticalGeneralIfOpticalTransLaneCarrierGrConfigLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalTransLaneCarrierGrConfigLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalTransLaneCarrierGrConfigLastChangeTime = _IfOpticalGeneralIfOpticalTransLaneCarrierGrConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 19),
    _IfOpticalGeneralIfOpticalTransLaneCarrierGrConfigLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalTransLaneCarrierGrConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalTransLaneCarrierGrConfigLastChangeTime.setStatus("current")
_IfOpticalGeneralIfOpticalTransLaneCarrierGrStateLastChangeTime_Type = DateAndTime
_IfOpticalGeneralIfOpticalTransLaneCarrierGrStateLastChangeTime_Object = MibScalar
ifOpticalGeneralIfOpticalTransLaneCarrierGrStateLastChangeTime = _IfOpticalGeneralIfOpticalTransLaneCarrierGrStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 1, 20),
    _IfOpticalGeneralIfOpticalTransLaneCarrierGrStateLastChangeTime_Type()
)
ifOpticalGeneralIfOpticalTransLaneCarrierGrStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalGeneralIfOpticalTransLaneCarrierGrStateLastChangeTime.setStatus("current")
_IfOpticalTransSectionList_ObjectIdentity = ObjectIdentity
ifOpticalTransSectionList = _IfOpticalTransSectionList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2)
)
_IfOpticalTransSectionTable_Object = MibTable
ifOpticalTransSectionTable = _IfOpticalTransSectionTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifOpticalTransSectionTable.setStatus("current")
_IfOpticalTransSectionEntry_Object = MibTableRow
ifOpticalTransSectionEntry = _IfOpticalTransSectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1)
)
ifOpticalTransSectionEntry.setIndexNames(
    (0, "LUM-IFOPTICAL-MIB", "ifOpticalTransSectionIndex"),
)
if mibBuilder.loadTexts:
    ifOpticalTransSectionEntry.setStatus("current")
_IfOpticalTransSectionIndex_Type = Unsigned32
_IfOpticalTransSectionIndex_Object = MibTableColumn
ifOpticalTransSectionIndex = _IfOpticalTransSectionIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 1),
    _IfOpticalTransSectionIndex_Type()
)
ifOpticalTransSectionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionIndex.setStatus("current")
_IfOpticalTransSectionName_Type = MgmtNameString
_IfOpticalTransSectionName_Object = MibTableColumn
ifOpticalTransSectionName = _IfOpticalTransSectionName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 2),
    _IfOpticalTransSectionName_Type()
)
ifOpticalTransSectionName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOpticalTransSectionName.setStatus("current")
_IfOpticalTransSectionConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOpticalTransSectionConnIfBasicIfIndex_Object = MibTableColumn
ifOpticalTransSectionConnIfBasicIfIndex = _IfOpticalTransSectionConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 3),
    _IfOpticalTransSectionConnIfBasicIfIndex_Type()
)
ifOpticalTransSectionConnIfBasicIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOpticalTransSectionConnIfBasicIfIndex.setStatus("current")


class _IfOpticalTransSectionForwardAls_Type(EnabledDisabledWithNA):
    """Custom type ifOpticalTransSectionForwardAls based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfOpticalTransSectionForwardAls_Type.__name__ = "EnabledDisabledWithNA"
_IfOpticalTransSectionForwardAls_Object = MibTableColumn
ifOpticalTransSectionForwardAls = _IfOpticalTransSectionForwardAls_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 4),
    _IfOpticalTransSectionForwardAls_Type()
)
ifOpticalTransSectionForwardAls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOpticalTransSectionForwardAls.setStatus("current")
_IfOpticalTransSectionRxPowerLevel_Type = Signed32WithNA
_IfOpticalTransSectionRxPowerLevel_Object = MibTableColumn
ifOpticalTransSectionRxPowerLevel = _IfOpticalTransSectionRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 5),
    _IfOpticalTransSectionRxPowerLevel_Type()
)
ifOpticalTransSectionRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionRxPowerLevel.setStatus("current")


class _IfOpticalTransSectionRxPowerLevelLowRelativeThld_Type(Signed32WithNA):
    """Custom type ifOpticalTransSectionRxPowerLevelLowRelativeThld based on Signed32WithNA"""
    defaultValue = 30

    subtypeSpec = Signed32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfOpticalTransSectionRxPowerLevelLowRelativeThld_Type.__name__ = "Signed32WithNA"
_IfOpticalTransSectionRxPowerLevelLowRelativeThld_Object = MibTableColumn
ifOpticalTransSectionRxPowerLevelLowRelativeThld = _IfOpticalTransSectionRxPowerLevelLowRelativeThld_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 6),
    _IfOpticalTransSectionRxPowerLevelLowRelativeThld_Type()
)
ifOpticalTransSectionRxPowerLevelLowRelativeThld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionRxPowerLevelLowRelativeThld.setStatus("current")
_IfOpticalTransSectionTxPowerLevel_Type = Signed32WithNA
_IfOpticalTransSectionTxPowerLevel_Object = MibTableColumn
ifOpticalTransSectionTxPowerLevel = _IfOpticalTransSectionTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 7),
    _IfOpticalTransSectionTxPowerLevel_Type()
)
ifOpticalTransSectionTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionTxPowerLevel.setStatus("current")


class _IfOpticalTransSectionLaserMode_Type(LaserMode):
    """Custom type ifOpticalTransSectionLaserMode based on LaserMode"""
    defaultValue = 1


_IfOpticalTransSectionLaserMode_Type.__name__ = "LaserMode"
_IfOpticalTransSectionLaserMode_Object = MibTableColumn
ifOpticalTransSectionLaserMode = _IfOpticalTransSectionLaserMode_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 8),
    _IfOpticalTransSectionLaserMode_Type()
)
ifOpticalTransSectionLaserMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOpticalTransSectionLaserMode.setStatus("current")
_IfOpticalTransSectionLaserStatus_Type = OnOff
_IfOpticalTransSectionLaserStatus_Object = MibTableColumn
ifOpticalTransSectionLaserStatus = _IfOpticalTransSectionLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 9),
    _IfOpticalTransSectionLaserStatus_Type()
)
ifOpticalTransSectionLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionLaserStatus.setStatus("current")
_IfOpticalTransSectionReceiverSensitivity_Type = Signed32WithNA
_IfOpticalTransSectionReceiverSensitivity_Object = MibTableColumn
ifOpticalTransSectionReceiverSensitivity = _IfOpticalTransSectionReceiverSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 10),
    _IfOpticalTransSectionReceiverSensitivity_Type()
)
ifOpticalTransSectionReceiverSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionReceiverSensitivity.setStatus("current")
_IfOpticalTransSectionTxSignalStatus_Type = SignalStatusWithNA
_IfOpticalTransSectionTxSignalStatus_Object = MibTableColumn
ifOpticalTransSectionTxSignalStatus = _IfOpticalTransSectionTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 11),
    _IfOpticalTransSectionTxSignalStatus_Type()
)
ifOpticalTransSectionTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionTxSignalStatus.setStatus("current")
_IfOpticalTransSectionRxSignalStatus_Type = SignalStatusWithNA
_IfOpticalTransSectionRxSignalStatus_Object = MibTableColumn
ifOpticalTransSectionRxSignalStatus = _IfOpticalTransSectionRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 12),
    _IfOpticalTransSectionRxSignalStatus_Type()
)
ifOpticalTransSectionRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionRxSignalStatus.setStatus("current")
_IfOpticalTransSectionLossOfSignal_Type = FaultStatusWithNA
_IfOpticalTransSectionLossOfSignal_Object = MibTableColumn
ifOpticalTransSectionLossOfSignal = _IfOpticalTransSectionLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 13),
    _IfOpticalTransSectionLossOfSignal_Type()
)
ifOpticalTransSectionLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionLossOfSignal.setStatus("current")
_IfOpticalTransSectionRxPowerLevelLow_Type = FaultStatusWithNA
_IfOpticalTransSectionRxPowerLevelLow_Object = MibTableColumn
ifOpticalTransSectionRxPowerLevelLow = _IfOpticalTransSectionRxPowerLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 14),
    _IfOpticalTransSectionRxPowerLevelLow_Type()
)
ifOpticalTransSectionRxPowerLevelLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionRxPowerLevelLow.setStatus("current")
_IfOpticalTransSectionRxPowerLevelHigh_Type = FaultStatusWithNA
_IfOpticalTransSectionRxPowerLevelHigh_Object = MibTableColumn
ifOpticalTransSectionRxPowerLevelHigh = _IfOpticalTransSectionRxPowerLevelHigh_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 15),
    _IfOpticalTransSectionRxPowerLevelHigh_Type()
)
ifOpticalTransSectionRxPowerLevelHigh.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionRxPowerLevelHigh.setStatus("current")
_IfOpticalTransSectionRxExcessiveInputPower_Type = FaultStatusWithNA
_IfOpticalTransSectionRxExcessiveInputPower_Object = MibTableColumn
ifOpticalTransSectionRxExcessiveInputPower = _IfOpticalTransSectionRxExcessiveInputPower_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 16),
    _IfOpticalTransSectionRxExcessiveInputPower_Type()
)
ifOpticalTransSectionRxExcessiveInputPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionRxExcessiveInputPower.setStatus("current")
_IfOpticalTransSectionTxPowerLow_Type = FaultStatusWithNA
_IfOpticalTransSectionTxPowerLow_Object = MibTableColumn
ifOpticalTransSectionTxPowerLow = _IfOpticalTransSectionTxPowerLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 17),
    _IfOpticalTransSectionTxPowerLow_Type()
)
ifOpticalTransSectionTxPowerLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionTxPowerLow.setStatus("current")


class _IfOpticalTransSectionRxPowerLevelLowAbsoluteThld_Type(Signed32WithNA):
    """Custom type ifOpticalTransSectionRxPowerLevelLowAbsoluteThld based on Signed32WithNA"""
    defaultValue = -140

    subtypeSpec = Signed32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-300, 50),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfOpticalTransSectionRxPowerLevelLowAbsoluteThld_Type.__name__ = "Signed32WithNA"
_IfOpticalTransSectionRxPowerLevelLowAbsoluteThld_Object = MibTableColumn
ifOpticalTransSectionRxPowerLevelLowAbsoluteThld = _IfOpticalTransSectionRxPowerLevelLowAbsoluteThld_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 18),
    _IfOpticalTransSectionRxPowerLevelLowAbsoluteThld_Type()
)
ifOpticalTransSectionRxPowerLevelLowAbsoluteThld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionRxPowerLevelLowAbsoluteThld.setStatus("current")


class _IfOpticalTransSectionLossThld_Type(Signed32WithNA):
    """Custom type ifOpticalTransSectionLossThld based on Signed32WithNA"""
    defaultValue = -350

    subtypeSpec = Signed32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-420, 60),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfOpticalTransSectionLossThld_Type.__name__ = "Signed32WithNA"
_IfOpticalTransSectionLossThld_Object = MibTableColumn
ifOpticalTransSectionLossThld = _IfOpticalTransSectionLossThld_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 19),
    _IfOpticalTransSectionLossThld_Type()
)
ifOpticalTransSectionLossThld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransSectionLossThld.setStatus("current")


class _IfOpticalTransSectionLaserForcedOn_Type(EnabledDisabledWithNA):
    """Custom type ifOpticalTransSectionLaserForcedOn based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfOpticalTransSectionLaserForcedOn_Type.__name__ = "EnabledDisabledWithNA"
_IfOpticalTransSectionLaserForcedOn_Object = MibTableColumn
ifOpticalTransSectionLaserForcedOn = _IfOpticalTransSectionLaserForcedOn_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 2, 1, 1, 20),
    _IfOpticalTransSectionLaserForcedOn_Type()
)
ifOpticalTransSectionLaserForcedOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOpticalTransSectionLaserForcedOn.setStatus("current")
_IfOpticalChannelList_ObjectIdentity = ObjectIdentity
ifOpticalChannelList = _IfOpticalChannelList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3)
)
_IfOpticalChannelTable_Object = MibTable
ifOpticalChannelTable = _IfOpticalChannelTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifOpticalChannelTable.setStatus("current")
_IfOpticalChannelEntry_Object = MibTableRow
ifOpticalChannelEntry = _IfOpticalChannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1)
)
ifOpticalChannelEntry.setIndexNames(
    (0, "LUM-IFOPTICAL-MIB", "ifOpticalChannelIndex"),
)
if mibBuilder.loadTexts:
    ifOpticalChannelEntry.setStatus("current")
_IfOpticalChannelIndex_Type = Unsigned32
_IfOpticalChannelIndex_Object = MibTableColumn
ifOpticalChannelIndex = _IfOpticalChannelIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 1),
    _IfOpticalChannelIndex_Type()
)
ifOpticalChannelIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalChannelIndex.setStatus("current")
_IfOpticalChannelName_Type = MgmtNameString
_IfOpticalChannelName_Object = MibTableColumn
ifOpticalChannelName = _IfOpticalChannelName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 2),
    _IfOpticalChannelName_Type()
)
ifOpticalChannelName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOpticalChannelName.setStatus("current")
_IfOpticalChannelConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOpticalChannelConnIfBasicIfIndex_Object = MibTableColumn
ifOpticalChannelConnIfBasicIfIndex = _IfOpticalChannelConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 3),
    _IfOpticalChannelConnIfBasicIfIndex_Type()
)
ifOpticalChannelConnIfBasicIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOpticalChannelConnIfBasicIfIndex.setStatus("current")
_IfOpticalChannelTxFrequency_Type = Frequency
_IfOpticalChannelTxFrequency_Object = MibTableColumn
ifOpticalChannelTxFrequency = _IfOpticalChannelTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 4),
    _IfOpticalChannelTxFrequency_Type()
)
ifOpticalChannelTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalChannelTxFrequency.setStatus("current")


class _IfOpticalChannelExpectedTxFrequency_Type(FrequencyOnlyNotApplicable):
    """Custom type ifOpticalChannelExpectedTxFrequency based on FrequencyOnlyNotApplicable"""
    defaultValue = 0


_IfOpticalChannelExpectedTxFrequency_Type.__name__ = "FrequencyOnlyNotApplicable"
_IfOpticalChannelExpectedTxFrequency_Object = MibTableColumn
ifOpticalChannelExpectedTxFrequency = _IfOpticalChannelExpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 5),
    _IfOpticalChannelExpectedTxFrequency_Type()
)
ifOpticalChannelExpectedTxFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOpticalChannelExpectedTxFrequency.setStatus("current")
_IfOpticalChannelTxSignalStatus_Type = SignalStatusWithNA
_IfOpticalChannelTxSignalStatus_Object = MibTableColumn
ifOpticalChannelTxSignalStatus = _IfOpticalChannelTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 6),
    _IfOpticalChannelTxSignalStatus_Type()
)
ifOpticalChannelTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalChannelTxSignalStatus.setStatus("current")
_IfOpticalChannelRxSignalStatus_Type = SignalStatusWithNA
_IfOpticalChannelRxSignalStatus_Object = MibTableColumn
ifOpticalChannelRxSignalStatus = _IfOpticalChannelRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 7),
    _IfOpticalChannelRxSignalStatus_Type()
)
ifOpticalChannelRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalChannelRxSignalStatus.setStatus("current")
_IfOpticalChannelIllegalTxFrequency_Type = FaultStatusWithNA
_IfOpticalChannelIllegalTxFrequency_Object = MibTableColumn
ifOpticalChannelIllegalTxFrequency = _IfOpticalChannelIllegalTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 8),
    _IfOpticalChannelIllegalTxFrequency_Type()
)
ifOpticalChannelIllegalTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalChannelIllegalTxFrequency.setStatus("current")
_IfOpticalChannelUnexpectedTxFrequency_Type = FaultStatusWithNA
_IfOpticalChannelUnexpectedTxFrequency_Object = MibTableColumn
ifOpticalChannelUnexpectedTxFrequency = _IfOpticalChannelUnexpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 9),
    _IfOpticalChannelUnexpectedTxFrequency_Type()
)
ifOpticalChannelUnexpectedTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalChannelUnexpectedTxFrequency.setStatus("current")
_IfOpticalChannelNoTxFrequencySet_Type = FaultStatusWithNA
_IfOpticalChannelNoTxFrequencySet_Object = MibTableColumn
ifOpticalChannelNoTxFrequencySet = _IfOpticalChannelNoTxFrequencySet_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 10),
    _IfOpticalChannelNoTxFrequencySet_Type()
)
ifOpticalChannelNoTxFrequencySet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalChannelNoTxFrequencySet.setStatus("current")


class _IfOpticalChannelDispersionSearchLimit_Type(DispersionSearchLimit):
    """Custom type ifOpticalChannelDispersionSearchLimit based on DispersionSearchLimit"""
    defaultValue = 22500


_IfOpticalChannelDispersionSearchLimit_Type.__name__ = "DispersionSearchLimit"
_IfOpticalChannelDispersionSearchLimit_Object = MibTableColumn
ifOpticalChannelDispersionSearchLimit = _IfOpticalChannelDispersionSearchLimit_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 11),
    _IfOpticalChannelDispersionSearchLimit_Type()
)
ifOpticalChannelDispersionSearchLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalChannelDispersionSearchLimit.setStatus("current")
_IfOpticalChannelLaserNotTuned_Type = FaultStatusWithNA
_IfOpticalChannelLaserNotTuned_Object = MibTableColumn
ifOpticalChannelLaserNotTuned = _IfOpticalChannelLaserNotTuned_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 12),
    _IfOpticalChannelLaserNotTuned_Type()
)
ifOpticalChannelLaserNotTuned.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalChannelLaserNotTuned.setStatus("current")


class _IfOpticalChannelLineCoding_Type(Integer32):
    """Custom type ifOpticalChannelLineCoding based on Integer32"""
    defaultValue = 2147483647

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              2147483647)
        )
    )
    namedValues = NamedValues(
        *(("qam16", 1),
          ("dqpsk", 2),
          ("qpsk", 3),
          ("notApplicable", 2147483647))
    )


_IfOpticalChannelLineCoding_Type.__name__ = "Integer32"
_IfOpticalChannelLineCoding_Object = MibTableColumn
ifOpticalChannelLineCoding = _IfOpticalChannelLineCoding_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 3, 1, 1, 13),
    _IfOpticalChannelLineCoding_Type()
)
ifOpticalChannelLineCoding.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalChannelLineCoding.setStatus("current")
_IfOpticalDigitalSignalRateList_ObjectIdentity = ObjectIdentity
ifOpticalDigitalSignalRateList = _IfOpticalDigitalSignalRateList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4)
)
_IfOpticalDigitalSignalRateTable_Object = MibTable
ifOpticalDigitalSignalRateTable = _IfOpticalDigitalSignalRateTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1)
)
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateTable.setStatus("current")
_IfOpticalDigitalSignalRateEntry_Object = MibTableRow
ifOpticalDigitalSignalRateEntry = _IfOpticalDigitalSignalRateEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1, 1)
)
ifOpticalDigitalSignalRateEntry.setIndexNames(
    (0, "LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateIndex"),
)
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateEntry.setStatus("current")
_IfOpticalDigitalSignalRateIndex_Type = Unsigned32
_IfOpticalDigitalSignalRateIndex_Object = MibTableColumn
ifOpticalDigitalSignalRateIndex = _IfOpticalDigitalSignalRateIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1, 1, 1),
    _IfOpticalDigitalSignalRateIndex_Type()
)
ifOpticalDigitalSignalRateIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateIndex.setStatus("current")
_IfOpticalDigitalSignalRateName_Type = MgmtNameString
_IfOpticalDigitalSignalRateName_Object = MibTableColumn
ifOpticalDigitalSignalRateName = _IfOpticalDigitalSignalRateName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1, 1, 2),
    _IfOpticalDigitalSignalRateName_Type()
)
ifOpticalDigitalSignalRateName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateName.setStatus("current")
_IfOpticalDigitalSignalRateConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOpticalDigitalSignalRateConnIfBasicIfIndex_Object = MibTableColumn
ifOpticalDigitalSignalRateConnIfBasicIfIndex = _IfOpticalDigitalSignalRateConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1, 1, 3),
    _IfOpticalDigitalSignalRateConnIfBasicIfIndex_Type()
)
ifOpticalDigitalSignalRateConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateConnIfBasicIfIndex.setStatus("current")
_IfOpticalDigitalSignalRateMaxBitRate_Type = Unsigned32WithNA
_IfOpticalDigitalSignalRateMaxBitRate_Object = MibTableColumn
ifOpticalDigitalSignalRateMaxBitRate = _IfOpticalDigitalSignalRateMaxBitRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1, 1, 5),
    _IfOpticalDigitalSignalRateMaxBitRate_Type()
)
ifOpticalDigitalSignalRateMaxBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateMaxBitRate.setStatus("current")
_IfOpticalDigitalSignalRateMinBitRate_Type = Unsigned32WithNA
_IfOpticalDigitalSignalRateMinBitRate_Object = MibTableColumn
ifOpticalDigitalSignalRateMinBitRate = _IfOpticalDigitalSignalRateMinBitRate_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1, 1, 6),
    _IfOpticalDigitalSignalRateMinBitRate_Type()
)
ifOpticalDigitalSignalRateMinBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateMinBitRate.setStatus("current")
_IfOpticalDigitalSignalRateTxSignalStatus_Type = SignalStatusWithNA
_IfOpticalDigitalSignalRateTxSignalStatus_Object = MibTableColumn
ifOpticalDigitalSignalRateTxSignalStatus = _IfOpticalDigitalSignalRateTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1, 1, 7),
    _IfOpticalDigitalSignalRateTxSignalStatus_Type()
)
ifOpticalDigitalSignalRateTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateTxSignalStatus.setStatus("current")
_IfOpticalDigitalSignalRateRxSignalStatus_Type = SignalStatusWithNA
_IfOpticalDigitalSignalRateRxSignalStatus_Object = MibTableColumn
ifOpticalDigitalSignalRateRxSignalStatus = _IfOpticalDigitalSignalRateRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1, 1, 8),
    _IfOpticalDigitalSignalRateRxSignalStatus_Type()
)
ifOpticalDigitalSignalRateRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateRxSignalStatus.setStatus("current")
_IfOpticalDigitalSignalRateLossOfLock_Type = FaultStatusWithNA
_IfOpticalDigitalSignalRateLossOfLock_Object = MibTableColumn
ifOpticalDigitalSignalRateLossOfLock = _IfOpticalDigitalSignalRateLossOfLock_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1, 1, 9),
    _IfOpticalDigitalSignalRateLossOfLock_Type()
)
ifOpticalDigitalSignalRateLossOfLock.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateLossOfLock.setStatus("current")
_IfOpticalDigitalSignalRateBitrateUnavailable_Type = FaultStatusWithNA
_IfOpticalDigitalSignalRateBitrateUnavailable_Object = MibTableColumn
ifOpticalDigitalSignalRateBitrateUnavailable = _IfOpticalDigitalSignalRateBitrateUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 4, 1, 1, 10),
    _IfOpticalDigitalSignalRateBitrateUnavailable_Type()
)
ifOpticalDigitalSignalRateBitrateUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateBitrateUnavailable.setStatus("current")
_IfOpticalFecList_ObjectIdentity = ObjectIdentity
ifOpticalFecList = _IfOpticalFecList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5)
)
_IfOpticalFecTable_Object = MibTable
ifOpticalFecTable = _IfOpticalFecTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1)
)
if mibBuilder.loadTexts:
    ifOpticalFecTable.setStatus("current")
_IfOpticalFecEntry_Object = MibTableRow
ifOpticalFecEntry = _IfOpticalFecEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1)
)
ifOpticalFecEntry.setIndexNames(
    (0, "LUM-IFOPTICAL-MIB", "ifOpticalFecIndex"),
)
if mibBuilder.loadTexts:
    ifOpticalFecEntry.setStatus("current")
_IfOpticalFecIndex_Type = Unsigned32
_IfOpticalFecIndex_Object = MibTableColumn
ifOpticalFecIndex = _IfOpticalFecIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 1),
    _IfOpticalFecIndex_Type()
)
ifOpticalFecIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalFecIndex.setStatus("current")
_IfOpticalFecName_Type = MgmtNameString
_IfOpticalFecName_Object = MibTableColumn
ifOpticalFecName = _IfOpticalFecName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 2),
    _IfOpticalFecName_Type()
)
ifOpticalFecName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOpticalFecName.setStatus("current")
_IfOpticalFecConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOpticalFecConnIfBasicIfIndex_Object = MibTableColumn
ifOpticalFecConnIfBasicIfIndex = _IfOpticalFecConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 3),
    _IfOpticalFecConnIfBasicIfIndex_Type()
)
ifOpticalFecConnIfBasicIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOpticalFecConnIfBasicIfIndex.setStatus("current")


class _IfOpticalFecType_Type(FecType):
    """Custom type ifOpticalFecType based on FecType"""
    defaultValue = 1


_IfOpticalFecType_Type.__name__ = "FecType"
_IfOpticalFecType_Object = MibTableColumn
ifOpticalFecType = _IfOpticalFecType_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 4),
    _IfOpticalFecType_Type()
)
ifOpticalFecType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOpticalFecType.setStatus("current")
_IfOpticalFecTxSignalStatus_Type = SignalStatusWithNA
_IfOpticalFecTxSignalStatus_Object = MibTableColumn
ifOpticalFecTxSignalStatus = _IfOpticalFecTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 5),
    _IfOpticalFecTxSignalStatus_Type()
)
ifOpticalFecTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalFecTxSignalStatus.setStatus("current")
_IfOpticalFecRxSignalStatus_Type = SignalStatusWithNA
_IfOpticalFecRxSignalStatus_Object = MibTableColumn
ifOpticalFecRxSignalStatus = _IfOpticalFecRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 6),
    _IfOpticalFecRxSignalStatus_Type()
)
ifOpticalFecRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalFecRxSignalStatus.setStatus("current")
_IfOpticalFecFailure_Type = FaultStatusWithNA
_IfOpticalFecFailure_Object = MibTableColumn
ifOpticalFecFailure = _IfOpticalFecFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 7),
    _IfOpticalFecFailure_Type()
)
ifOpticalFecFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalFecFailure.setStatus("current")
_IfOpticalFecSignalDegraded_Type = FaultStatusWithNA
_IfOpticalFecSignalDegraded_Object = MibTableColumn
ifOpticalFecSignalDegraded = _IfOpticalFecSignalDegraded_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 8),
    _IfOpticalFecSignalDegraded_Type()
)
ifOpticalFecSignalDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalFecSignalDegraded.setStatus("current")


class _IfOpticalFecSignalDegradeThreshold_Type(BerLevelMTOSI):
    """Custom type ifOpticalFecSignalDegradeThreshold based on BerLevelMTOSI"""
    defaultValue = 13


_IfOpticalFecSignalDegradeThreshold_Type.__name__ = "BerLevelMTOSI"
_IfOpticalFecSignalDegradeThreshold_Object = MibTableColumn
ifOpticalFecSignalDegradeThreshold = _IfOpticalFecSignalDegradeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 9),
    _IfOpticalFecSignalDegradeThreshold_Type()
)
ifOpticalFecSignalDegradeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOpticalFecSignalDegradeThreshold.setStatus("current")
_IfOpticalFecTypeUnavailable_Type = FaultStatus
_IfOpticalFecTypeUnavailable_Object = MibTableColumn
ifOpticalFecTypeUnavailable = _IfOpticalFecTypeUnavailable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 10),
    _IfOpticalFecTypeUnavailable_Type()
)
ifOpticalFecTypeUnavailable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalFecTypeUnavailable.setStatus("current")


class _IfOpticalFecUId_Type(Unsigned32):
    """Custom type ifOpticalFecUId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IfOpticalFecUId_Type.__name__ = "Unsigned32"
_IfOpticalFecUId_Object = MibTableColumn
ifOpticalFecUId = _IfOpticalFecUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 11),
    _IfOpticalFecUId_Type()
)
ifOpticalFecUId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOpticalFecUId.setStatus("current")
_IfOpticalFecDecModeMismatch_Type = FaultStatusWithNA
_IfOpticalFecDecModeMismatch_Object = MibTableColumn
ifOpticalFecDecModeMismatch = _IfOpticalFecDecModeMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 5, 1, 1, 12),
    _IfOpticalFecDecModeMismatch_Type()
)
ifOpticalFecDecModeMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalFecDecModeMismatch.setStatus("current")
_IfOpticalTransLaneCarrierList_ObjectIdentity = ObjectIdentity
ifOpticalTransLaneCarrierList = _IfOpticalTransLaneCarrierList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6)
)
_IfOpticalTransLaneCarrierTable_Object = MibTable
ifOpticalTransLaneCarrierTable = _IfOpticalTransLaneCarrierTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1)
)
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierTable.setStatus("current")
_IfOpticalTransLaneCarrierEntry_Object = MibTableRow
ifOpticalTransLaneCarrierEntry = _IfOpticalTransLaneCarrierEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1)
)
ifOpticalTransLaneCarrierEntry.setIndexNames(
    (0, "LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierIndex"),
)
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierEntry.setStatus("current")
_IfOpticalTransLaneCarrierIndex_Type = Unsigned32
_IfOpticalTransLaneCarrierIndex_Object = MibTableColumn
ifOpticalTransLaneCarrierIndex = _IfOpticalTransLaneCarrierIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 1),
    _IfOpticalTransLaneCarrierIndex_Type()
)
ifOpticalTransLaneCarrierIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierIndex.setStatus("current")
_IfOpticalTransLaneCarrierName_Type = MgmtNameString
_IfOpticalTransLaneCarrierName_Object = MibTableColumn
ifOpticalTransLaneCarrierName = _IfOpticalTransLaneCarrierName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 2),
    _IfOpticalTransLaneCarrierName_Type()
)
ifOpticalTransLaneCarrierName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierName.setStatus("current")
_IfOpticalTransLaneCarrierConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOpticalTransLaneCarrierConnIfBasicIfIndex_Object = MibTableColumn
ifOpticalTransLaneCarrierConnIfBasicIfIndex = _IfOpticalTransLaneCarrierConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 3),
    _IfOpticalTransLaneCarrierConnIfBasicIfIndex_Type()
)
ifOpticalTransLaneCarrierConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierConnIfBasicIfIndex.setStatus("current")
_IfOpticalTransLaneCarrierConnIfOpticalTransLaneCarrierGrIndex_Type = Unsigned32WithNA
_IfOpticalTransLaneCarrierConnIfOpticalTransLaneCarrierGrIndex_Object = MibTableColumn
ifOpticalTransLaneCarrierConnIfOpticalTransLaneCarrierGrIndex = _IfOpticalTransLaneCarrierConnIfOpticalTransLaneCarrierGrIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 4),
    _IfOpticalTransLaneCarrierConnIfOpticalTransLaneCarrierGrIndex_Type()
)
ifOpticalTransLaneCarrierConnIfOpticalTransLaneCarrierGrIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierConnIfOpticalTransLaneCarrierGrIndex.setStatus("current")
_IfOpticalTransLaneCarrierLaneId_Type = Unsigned32
_IfOpticalTransLaneCarrierLaneId_Object = MibTableColumn
ifOpticalTransLaneCarrierLaneId = _IfOpticalTransLaneCarrierLaneId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 5),
    _IfOpticalTransLaneCarrierLaneId_Type()
)
ifOpticalTransLaneCarrierLaneId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierLaneId.setStatus("current")
_IfOpticalTransLaneCarrierTxSignalStatus_Type = SignalStatusWithNA
_IfOpticalTransLaneCarrierTxSignalStatus_Object = MibTableColumn
ifOpticalTransLaneCarrierTxSignalStatus = _IfOpticalTransLaneCarrierTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 6),
    _IfOpticalTransLaneCarrierTxSignalStatus_Type()
)
ifOpticalTransLaneCarrierTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierTxSignalStatus.setStatus("current")
_IfOpticalTransLaneCarrierRxSignalStatus_Type = SignalStatusWithNA
_IfOpticalTransLaneCarrierRxSignalStatus_Object = MibTableColumn
ifOpticalTransLaneCarrierRxSignalStatus = _IfOpticalTransLaneCarrierRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 7),
    _IfOpticalTransLaneCarrierRxSignalStatus_Type()
)
ifOpticalTransLaneCarrierRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierRxSignalStatus.setStatus("current")
_IfOpticalTransLaneCarrierRxPowerLevel_Type = Signed32WithNA
_IfOpticalTransLaneCarrierRxPowerLevel_Object = MibTableColumn
ifOpticalTransLaneCarrierRxPowerLevel = _IfOpticalTransLaneCarrierRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 8),
    _IfOpticalTransLaneCarrierRxPowerLevel_Type()
)
ifOpticalTransLaneCarrierRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierRxPowerLevel.setStatus("current")
_IfOpticalTransLaneCarrierLossOfSignal_Type = FaultStatusWithNA
_IfOpticalTransLaneCarrierLossOfSignal_Object = MibTableColumn
ifOpticalTransLaneCarrierLossOfSignal = _IfOpticalTransLaneCarrierLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 9),
    _IfOpticalTransLaneCarrierLossOfSignal_Type()
)
ifOpticalTransLaneCarrierLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierLossOfSignal.setStatus("current")
_IfOpticalTransLaneCarrierReceiverSensitivity_Type = Signed32WithNA
_IfOpticalTransLaneCarrierReceiverSensitivity_Object = MibTableColumn
ifOpticalTransLaneCarrierReceiverSensitivity = _IfOpticalTransLaneCarrierReceiverSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 10),
    _IfOpticalTransLaneCarrierReceiverSensitivity_Type()
)
ifOpticalTransLaneCarrierReceiverSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierReceiverSensitivity.setStatus("current")
_IfOpticalTransLaneCarrierRxPowerLevelLow_Type = FaultStatusWithNA
_IfOpticalTransLaneCarrierRxPowerLevelLow_Object = MibTableColumn
ifOpticalTransLaneCarrierRxPowerLevelLow = _IfOpticalTransLaneCarrierRxPowerLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 11),
    _IfOpticalTransLaneCarrierRxPowerLevelLow_Type()
)
ifOpticalTransLaneCarrierRxPowerLevelLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierRxPowerLevelLow.setStatus("current")
_IfOpticalTransLaneCarrierTxFrequency_Type = LaneFrequency
_IfOpticalTransLaneCarrierTxFrequency_Object = MibTableColumn
ifOpticalTransLaneCarrierTxFrequency = _IfOpticalTransLaneCarrierTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 12),
    _IfOpticalTransLaneCarrierTxFrequency_Type()
)
ifOpticalTransLaneCarrierTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierTxFrequency.setStatus("current")
_IfOpticalTransLaneCarrierCounterSes_Type = Unsigned32WithNA
_IfOpticalTransLaneCarrierCounterSes_Object = MibTableColumn
ifOpticalTransLaneCarrierCounterSes = _IfOpticalTransLaneCarrierCounterSes_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 13),
    _IfOpticalTransLaneCarrierCounterSes_Type()
)
ifOpticalTransLaneCarrierCounterSes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierCounterSes.setStatus("current")


class _IfOpticalTransLaneCarrierCounterSesReset_Type(ResetWithNA):
    """Custom type ifOpticalTransLaneCarrierCounterSesReset based on ResetWithNA"""
    defaultValue = 2


_IfOpticalTransLaneCarrierCounterSesReset_Type.__name__ = "ResetWithNA"
_IfOpticalTransLaneCarrierCounterSesReset_Object = MibTableColumn
ifOpticalTransLaneCarrierCounterSesReset = _IfOpticalTransLaneCarrierCounterSesReset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 6, 1, 1, 14),
    _IfOpticalTransLaneCarrierCounterSesReset_Type()
)
ifOpticalTransLaneCarrierCounterSesReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierCounterSesReset.setStatus("deprecated")
_IfOpticalTransLaneCarrierGroupList_ObjectIdentity = ObjectIdentity
ifOpticalTransLaneCarrierGroupList = _IfOpticalTransLaneCarrierGroupList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7)
)
_IfOpticalTransLaneCarrierGroupTable_Object = MibTable
ifOpticalTransLaneCarrierGroupTable = _IfOpticalTransLaneCarrierGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1)
)
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupTable.setStatus("current")
_IfOpticalTransLaneCarrierGroupEntry_Object = MibTableRow
ifOpticalTransLaneCarrierGroupEntry = _IfOpticalTransLaneCarrierGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1)
)
ifOpticalTransLaneCarrierGroupEntry.setIndexNames(
    (0, "LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupIndex"),
)
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupEntry.setStatus("current")
_IfOpticalTransLaneCarrierGroupIndex_Type = Unsigned32
_IfOpticalTransLaneCarrierGroupIndex_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupIndex = _IfOpticalTransLaneCarrierGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 1),
    _IfOpticalTransLaneCarrierGroupIndex_Type()
)
ifOpticalTransLaneCarrierGroupIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupIndex.setStatus("current")
_IfOpticalTransLaneCarrierGroupName_Type = MgmtNameString
_IfOpticalTransLaneCarrierGroupName_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupName = _IfOpticalTransLaneCarrierGroupName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 2),
    _IfOpticalTransLaneCarrierGroupName_Type()
)
ifOpticalTransLaneCarrierGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupName.setStatus("current")
_IfOpticalTransLaneCarrierGroupConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfOpticalTransLaneCarrierGroupConnIfBasicIfIndex_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupConnIfBasicIfIndex = _IfOpticalTransLaneCarrierGroupConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 3),
    _IfOpticalTransLaneCarrierGroupConnIfBasicIfIndex_Type()
)
ifOpticalTransLaneCarrierGroupConnIfBasicIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupConnIfBasicIfIndex.setStatus("current")
_IfOpticalTransLaneCarrierGroupTxSignalStatus_Type = SignalStatusWithNA
_IfOpticalTransLaneCarrierGroupTxSignalStatus_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupTxSignalStatus = _IfOpticalTransLaneCarrierGroupTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 4),
    _IfOpticalTransLaneCarrierGroupTxSignalStatus_Type()
)
ifOpticalTransLaneCarrierGroupTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupTxSignalStatus.setStatus("current")
_IfOpticalTransLaneCarrierGroupRxSignalStatus_Type = SignalStatusWithNA
_IfOpticalTransLaneCarrierGroupRxSignalStatus_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupRxSignalStatus = _IfOpticalTransLaneCarrierGroupRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 5),
    _IfOpticalTransLaneCarrierGroupRxSignalStatus_Type()
)
ifOpticalTransLaneCarrierGroupRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupRxSignalStatus.setStatus("current")


class _IfOpticalTransLaneCarrierGroupForwardAls_Type(EnabledDisabledWithNA):
    """Custom type ifOpticalTransLaneCarrierGroupForwardAls based on EnabledDisabledWithNA"""
    defaultValue = 1


_IfOpticalTransLaneCarrierGroupForwardAls_Type.__name__ = "EnabledDisabledWithNA"
_IfOpticalTransLaneCarrierGroupForwardAls_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupForwardAls = _IfOpticalTransLaneCarrierGroupForwardAls_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 6),
    _IfOpticalTransLaneCarrierGroupForwardAls_Type()
)
ifOpticalTransLaneCarrierGroupForwardAls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupForwardAls.setStatus("current")
_IfOpticalTransLaneCarrierGroupLaserStatus_Type = OnOff
_IfOpticalTransLaneCarrierGroupLaserStatus_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupLaserStatus = _IfOpticalTransLaneCarrierGroupLaserStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 7),
    _IfOpticalTransLaneCarrierGroupLaserStatus_Type()
)
ifOpticalTransLaneCarrierGroupLaserStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupLaserStatus.setStatus("current")
_IfOpticalTransLaneCarrierGroupTxPowerLevel_Type = Signed32WithNA
_IfOpticalTransLaneCarrierGroupTxPowerLevel_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupTxPowerLevel = _IfOpticalTransLaneCarrierGroupTxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 8),
    _IfOpticalTransLaneCarrierGroupTxPowerLevel_Type()
)
ifOpticalTransLaneCarrierGroupTxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupTxPowerLevel.setStatus("current")
_IfOpticalTransLaneCarrierGroupRxPowerLevel_Type = Signed32WithNA
_IfOpticalTransLaneCarrierGroupRxPowerLevel_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupRxPowerLevel = _IfOpticalTransLaneCarrierGroupRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 9),
    _IfOpticalTransLaneCarrierGroupRxPowerLevel_Type()
)
ifOpticalTransLaneCarrierGroupRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupRxPowerLevel.setStatus("current")
_IfOpticalTransLaneCarrierGroupLossOfSignal_Type = FaultStatusWithNA
_IfOpticalTransLaneCarrierGroupLossOfSignal_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupLossOfSignal = _IfOpticalTransLaneCarrierGroupLossOfSignal_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 10),
    _IfOpticalTransLaneCarrierGroupLossOfSignal_Type()
)
ifOpticalTransLaneCarrierGroupLossOfSignal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupLossOfSignal.setStatus("current")


class _IfOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld_Type(Signed32WithNA):
    """Custom type ifOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld based on Signed32WithNA"""
    defaultValue = 30

    subtypeSpec = Signed32WithNA.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-50, 100),
        ValueRangeConstraint(2147483646, 2147483646),
        ValueRangeConstraint(2147483647, 2147483647),
    )


_IfOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld_Type.__name__ = "Signed32WithNA"
_IfOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld = _IfOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 11),
    _IfOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld_Type()
)
ifOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld.setStatus("current")
_IfOpticalTransLaneCarrierGroupRxPowerLevelLow_Type = FaultStatusWithNA
_IfOpticalTransLaneCarrierGroupRxPowerLevelLow_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupRxPowerLevelLow = _IfOpticalTransLaneCarrierGroupRxPowerLevelLow_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 12),
    _IfOpticalTransLaneCarrierGroupRxPowerLevelLow_Type()
)
ifOpticalTransLaneCarrierGroupRxPowerLevelLow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupRxPowerLevelLow.setStatus("current")
_IfOpticalTransLaneCarrierGroupTxFrequency_Type = Frequency
_IfOpticalTransLaneCarrierGroupTxFrequency_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupTxFrequency = _IfOpticalTransLaneCarrierGroupTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 13),
    _IfOpticalTransLaneCarrierGroupTxFrequency_Type()
)
ifOpticalTransLaneCarrierGroupTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupTxFrequency.setStatus("current")


class _IfOpticalTransLaneCarrierGroupExpectedTxFrequency_Type(FrequencyOnlyNotApplicable):
    """Custom type ifOpticalTransLaneCarrierGroupExpectedTxFrequency based on FrequencyOnlyNotApplicable"""
    defaultValue = 0


_IfOpticalTransLaneCarrierGroupExpectedTxFrequency_Type.__name__ = "FrequencyOnlyNotApplicable"
_IfOpticalTransLaneCarrierGroupExpectedTxFrequency_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupExpectedTxFrequency = _IfOpticalTransLaneCarrierGroupExpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 14),
    _IfOpticalTransLaneCarrierGroupExpectedTxFrequency_Type()
)
ifOpticalTransLaneCarrierGroupExpectedTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupExpectedTxFrequency.setStatus("current")
_IfOpticalTransLaneCarrierGroupUnexpectedTxFrequency_Type = FaultStatusWithNA
_IfOpticalTransLaneCarrierGroupUnexpectedTxFrequency_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupUnexpectedTxFrequency = _IfOpticalTransLaneCarrierGroupUnexpectedTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 15),
    _IfOpticalTransLaneCarrierGroupUnexpectedTxFrequency_Type()
)
ifOpticalTransLaneCarrierGroupUnexpectedTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupUnexpectedTxFrequency.setStatus("current")
_IfOpticalTransLaneCarrierGroupIllegalTxFrequency_Type = FaultStatusWithNA
_IfOpticalTransLaneCarrierGroupIllegalTxFrequency_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupIllegalTxFrequency = _IfOpticalTransLaneCarrierGroupIllegalTxFrequency_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 16),
    _IfOpticalTransLaneCarrierGroupIllegalTxFrequency_Type()
)
ifOpticalTransLaneCarrierGroupIllegalTxFrequency.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupIllegalTxFrequency.setStatus("current")


class _IfOpticalTransLaneCarrierGroupCounterSesReset_Type(ResetWithNA):
    """Custom type ifOpticalTransLaneCarrierGroupCounterSesReset based on ResetWithNA"""
    defaultValue = 2


_IfOpticalTransLaneCarrierGroupCounterSesReset_Type.__name__ = "ResetWithNA"
_IfOpticalTransLaneCarrierGroupCounterSesReset_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupCounterSesReset = _IfOpticalTransLaneCarrierGroupCounterSesReset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 17),
    _IfOpticalTransLaneCarrierGroupCounterSesReset_Type()
)
ifOpticalTransLaneCarrierGroupCounterSesReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupCounterSesReset.setStatus("current")
_IfOpticalTransLaneCarrierGroupMinimumLaneRxPowerLevel_Type = Signed32WithNA
_IfOpticalTransLaneCarrierGroupMinimumLaneRxPowerLevel_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupMinimumLaneRxPowerLevel = _IfOpticalTransLaneCarrierGroupMinimumLaneRxPowerLevel_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 18),
    _IfOpticalTransLaneCarrierGroupMinimumLaneRxPowerLevel_Type()
)
ifOpticalTransLaneCarrierGroupMinimumLaneRxPowerLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupMinimumLaneRxPowerLevel.setStatus("current")
_IfOpticalTransLaneCarrierGroupReceiverLaneSensitivity_Type = Signed32WithNA
_IfOpticalTransLaneCarrierGroupReceiverLaneSensitivity_Object = MibTableColumn
ifOpticalTransLaneCarrierGroupReceiverLaneSensitivity = _IfOpticalTransLaneCarrierGroupReceiverLaneSensitivity_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 2, 7, 1, 1, 19),
    _IfOpticalTransLaneCarrierGroupReceiverLaneSensitivity_Type()
)
ifOpticalTransLaneCarrierGroupReceiverLaneSensitivity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupReceiverLaneSensitivity.setStatus("current")

# Managed Objects groups

ifOpticalGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 1)
)
ifOpticalGeneralGroupV1.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransSectionTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransSectionConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransSectionStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalChannelTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalChannelConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalChannelStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalDigitalSignalRateTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifOpticalGeneralGroupV1.setStatus("deprecated")

ifOpticalTransSectionGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 2)
)
ifOpticalTransSectionGroupV1.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionForwardAls"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLowRelativeThld"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLaserMode"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLaserStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionReceiverSensitivity"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLossOfSignal"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelHigh"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxExcessiveInputPower"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxPowerLow"))
)
if mibBuilder.loadTexts:
    ifOpticalTransSectionGroupV1.setStatus("deprecated")

ifOpticalChannelGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 3)
)
ifOpticalChannelGroupV1.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalChannelIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelExpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelIllegalTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelUnexpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelNoTxFrequencySet"))
)
if mibBuilder.loadTexts:
    ifOpticalChannelGroupV1.setStatus("deprecated")

ifOpticalDigitalSignalRateGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 4)
)
ifOpticalDigitalSignalRateGroupV1.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateMaxBitRate"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateMinBitRate"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateLossOfLock"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateBitrateUnavailable"))
)
if mibBuilder.loadTexts:
    ifOpticalDigitalSignalRateGroupV1.setStatus("current")

ifOpticalFecGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 5)
)
ifOpticalFecGroupV1.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalFecIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecType"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecFailure"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecSignalDegraded"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecSignalDegradeThreshold"))
)
if mibBuilder.loadTexts:
    ifOpticalFecGroupV1.setStatus("deprecated")

ifOpticalGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 6)
)
ifOpticalGeneralGroupV2.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransSectionTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransSectionConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransSectionStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalChannelTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalChannelConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalChannelStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalDigitalSignalRateTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalFecTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalFecConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalFecStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifOpticalGeneralGroupV2.setStatus("deprecated")

ifOpticalTransSectionGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 7)
)
ifOpticalTransSectionGroupV2.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionForwardAls"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLowRelativeThld"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLaserMode"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLaserStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionReceiverSensitivity"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLossOfSignal"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelHigh"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxExcessiveInputPower"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxPowerLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLowAbsoluteThld"))
)
if mibBuilder.loadTexts:
    ifOpticalTransSectionGroupV2.setStatus("deprecated")

ifOpticalGeneralGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 8)
)
ifOpticalGeneralGroupV3.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransSectionTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransSectionConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransSectionStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalChannelTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalChannelConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalChannelStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalDigitalSignalRateTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalFecTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalFecConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalFecStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransLaneCarrierTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransLaneCarrierConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransLaneCarrierStateLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransLaneCarrierGroupTableSize"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransLaneCarrierGrConfigLastChangeTime"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalGeneralIfOpticalTransLaneCarrierGrStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifOpticalGeneralGroupV3.setStatus("current")

ifOpticalTransLaneCarrierGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 9)
)
ifOpticalTransLaneCarrierGroupV1.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierConnIfOpticalTransLaneCarrierGrIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierLaneId"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierRxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierLossOfSignal"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierReceiverSensitivity"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierRxPowerLevelLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierCounterSes"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierCounterSesReset"))
)
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupV1.setStatus("current")

ifOpticalTransLaneCarrierGroupGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 10)
)
ifOpticalTransLaneCarrierGroupGroupV1.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupForwardAls"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupLaserStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupTxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupLossOfSignal"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxPowerLevelLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupExpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupUnexpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupIllegalTxFrequency"))
)
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupGroupV1.setStatus("deprecated")

ifOpticalTransLaneCarrierGroupGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 11)
)
ifOpticalTransLaneCarrierGroupGroupV2.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupForwardAls"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupLaserStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupTxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupLossOfSignal"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxPowerLevelLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupExpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupUnexpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupIllegalTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupCounterSesReset"))
)
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupGroupV2.setStatus("deprecated")

ifOpticalTransLaneCarrierGroupGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 12)
)
ifOpticalTransLaneCarrierGroupGroupV3.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupForwardAls"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupLaserStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupTxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupLossOfSignal"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupRxPowerLevelLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupExpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupUnexpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupIllegalTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupCounterSesReset"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupMinimumLaneRxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupReceiverLaneSensitivity"))
)
if mibBuilder.loadTexts:
    ifOpticalTransLaneCarrierGroupGroupV3.setStatus("current")

ifOpticalTransSectionGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 13)
)
ifOpticalTransSectionGroupV3.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionForwardAls"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLowRelativeThld"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLaserMode"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLaserStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionReceiverSensitivity"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLossOfSignal"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelHigh"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxExcessiveInputPower"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxPowerLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLowAbsoluteThld"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLossThld"))
)
if mibBuilder.loadTexts:
    ifOpticalTransSectionGroupV3.setStatus("deprecated")

ifOpticalChannelGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 14)
)
ifOpticalChannelGroupV2.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalChannelIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelExpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelIllegalTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelUnexpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelNoTxFrequencySet"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelDispersionSearchLimit"))
)
if mibBuilder.loadTexts:
    ifOpticalChannelGroupV2.setStatus("deprecated")

ifOpticalFecGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 15)
)
ifOpticalFecGroupV2.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalFecIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecType"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecFailure"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecSignalDegraded"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecSignalDegradeThreshold"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecTypeUnavailable"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecUId"))
)
if mibBuilder.loadTexts:
    ifOpticalFecGroupV2.setStatus("deprecated")

ifOpticalFecGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 16)
)
ifOpticalFecGroupV3.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalFecIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecType"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecFailure"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecSignalDegraded"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecSignalDegradeThreshold"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecTypeUnavailable"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecUId"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecDecModeMismatch"))
)
if mibBuilder.loadTexts:
    ifOpticalFecGroupV3.setStatus("current")

ifOpticalChannelGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 17)
)
ifOpticalChannelGroupV3.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalChannelIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelExpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelIllegalTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelUnexpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelNoTxFrequencySet"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelDispersionSearchLimit"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelLaserNotTuned"))
)
if mibBuilder.loadTexts:
    ifOpticalChannelGroupV3.setStatus("deprecated")

ifOpticalTransSectionGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 18)
)
ifOpticalTransSectionGroupV4.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionForwardAls"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLowRelativeThld"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxPowerLevel"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLaserMode"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLaserStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionReceiverSensitivity"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLossOfSignal"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelHigh"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxExcessiveInputPower"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionTxPowerLow"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionRxPowerLevelLowAbsoluteThld"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLossThld"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionLaserForcedOn"))
)
if mibBuilder.loadTexts:
    ifOpticalTransSectionGroupV4.setStatus("current")

ifOpticalChannelGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 1, 19)
)
ifOpticalChannelGroupV4.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalChannelIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelName"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelConnIfBasicIfIndex"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelExpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelTxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelRxSignalStatus"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelIllegalTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelUnexpectedTxFrequency"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelNoTxFrequencySet"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelDispersionSearchLimit"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelLaserNotTuned"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelLineCoding"))
)
if mibBuilder.loadTexts:
    ifOpticalChannelGroupV4.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfOpticalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2, 1)
)
lumIfOpticalComplV1.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfOpticalComplV1.setStatus(
        "deprecated"
    )

lumIfOpticalComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2, 2)
)
lumIfOpticalComplV2.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralGroupV2"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionGroupV2"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfOpticalComplV2.setStatus(
        "deprecated"
    )

lumIfOpticalComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2, 3)
)
lumIfOpticalComplV3.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionGroupV2"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfOpticalComplV3.setStatus(
        "deprecated"
    )

lumIfOpticalComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2, 4)
)
lumIfOpticalComplV4.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionGroupV2"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfOpticalComplV4.setStatus(
        "deprecated"
    )

lumIfOpticalComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2, 5)
)
lumIfOpticalComplV5.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionGroupV2"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfOpticalComplV5.setStatus(
        "deprecated"
    )

lumIfOpticalComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2, 6)
)
lumIfOpticalComplV6.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfOpticalComplV6.setStatus(
        "deprecated"
    )

lumIfOpticalComplV7 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2, 7)
)
lumIfOpticalComplV7.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecGroupV2"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfOpticalComplV7.setStatus(
        "deprecated"
    )

lumIfOpticalComplV8 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2, 8)
)
lumIfOpticalComplV8.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionGroupV4"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfOpticalComplV8.setStatus(
        "deprecated"
    )

lumIfOpticalComplV9 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2, 9)
)
lumIfOpticalComplV9.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionGroupV4"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelGroupV4"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfOpticalComplV9.setStatus(
        "deprecated"
    )

lumIfOpticalComplV10 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 48, 1, 2, 10)
)
lumIfOpticalComplV10.setObjects(
      *(("LUM-IFOPTICAL-MIB", "ifOpticalGeneralGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransSectionGroupV4"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalChannelGroupV4"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalDigitalSignalRateGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalFecGroupV3"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupV1"),
        ("LUM-IFOPTICAL-MIB", "ifOpticalTransLaneCarrierGroupGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfOpticalComplV10.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFOPTICAL-MIB",
    **{"lumIfOpticalMIBModule": lumIfOpticalMIBModule,
       "lumIfOpticalConfs": lumIfOpticalConfs,
       "lumIfOpticalGroups": lumIfOpticalGroups,
       "ifOpticalGeneralGroupV1": ifOpticalGeneralGroupV1,
       "ifOpticalTransSectionGroupV1": ifOpticalTransSectionGroupV1,
       "ifOpticalChannelGroupV1": ifOpticalChannelGroupV1,
       "ifOpticalDigitalSignalRateGroupV1": ifOpticalDigitalSignalRateGroupV1,
       "ifOpticalFecGroupV1": ifOpticalFecGroupV1,
       "ifOpticalGeneralGroupV2": ifOpticalGeneralGroupV2,
       "ifOpticalTransSectionGroupV2": ifOpticalTransSectionGroupV2,
       "ifOpticalGeneralGroupV3": ifOpticalGeneralGroupV3,
       "ifOpticalTransLaneCarrierGroupV1": ifOpticalTransLaneCarrierGroupV1,
       "ifOpticalTransLaneCarrierGroupGroupV1": ifOpticalTransLaneCarrierGroupGroupV1,
       "ifOpticalTransLaneCarrierGroupGroupV2": ifOpticalTransLaneCarrierGroupGroupV2,
       "ifOpticalTransLaneCarrierGroupGroupV3": ifOpticalTransLaneCarrierGroupGroupV3,
       "ifOpticalTransSectionGroupV3": ifOpticalTransSectionGroupV3,
       "ifOpticalChannelGroupV2": ifOpticalChannelGroupV2,
       "ifOpticalFecGroupV2": ifOpticalFecGroupV2,
       "ifOpticalFecGroupV3": ifOpticalFecGroupV3,
       "ifOpticalChannelGroupV3": ifOpticalChannelGroupV3,
       "ifOpticalTransSectionGroupV4": ifOpticalTransSectionGroupV4,
       "ifOpticalChannelGroupV4": ifOpticalChannelGroupV4,
       "lumIfOpticalCompl": lumIfOpticalCompl,
       "lumIfOpticalComplV1": lumIfOpticalComplV1,
       "lumIfOpticalComplV2": lumIfOpticalComplV2,
       "lumIfOpticalComplV3": lumIfOpticalComplV3,
       "lumIfOpticalComplV4": lumIfOpticalComplV4,
       "lumIfOpticalComplV5": lumIfOpticalComplV5,
       "lumIfOpticalComplV6": lumIfOpticalComplV6,
       "lumIfOpticalComplV7": lumIfOpticalComplV7,
       "lumIfOpticalComplV8": lumIfOpticalComplV8,
       "lumIfOpticalComplV9": lumIfOpticalComplV9,
       "lumIfOpticalComplV10": lumIfOpticalComplV10,
       "lumIfOpticalMIBObjects": lumIfOpticalMIBObjects,
       "ifOpticalGeneral": ifOpticalGeneral,
       "ifOpticalGeneralConfigLastChangeTime": ifOpticalGeneralConfigLastChangeTime,
       "ifOpticalGeneralStateLastChangeTime": ifOpticalGeneralStateLastChangeTime,
       "ifOpticalGeneralIfOpticalTransSectionTableSize": ifOpticalGeneralIfOpticalTransSectionTableSize,
       "ifOpticalGeneralIfOpticalTransSectionConfigLastChangeTime": ifOpticalGeneralIfOpticalTransSectionConfigLastChangeTime,
       "ifOpticalGeneralIfOpticalTransSectionStateLastChangeTime": ifOpticalGeneralIfOpticalTransSectionStateLastChangeTime,
       "ifOpticalGeneralIfOpticalChannelTableSize": ifOpticalGeneralIfOpticalChannelTableSize,
       "ifOpticalGeneralIfOpticalChannelConfigLastChangeTime": ifOpticalGeneralIfOpticalChannelConfigLastChangeTime,
       "ifOpticalGeneralIfOpticalChannelStateLastChangeTime": ifOpticalGeneralIfOpticalChannelStateLastChangeTime,
       "ifOpticalGeneralIfOpticalDigitalSignalRateTableSize": ifOpticalGeneralIfOpticalDigitalSignalRateTableSize,
       "ifOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime": ifOpticalGeneralIfOpticalDigitalSignalRateConfigLastChangeTime,
       "ifOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime": ifOpticalGeneralIfOpticalDigitalSignalRateStateLastChangeTime,
       "ifOpticalGeneralIfOpticalFecTableSize": ifOpticalGeneralIfOpticalFecTableSize,
       "ifOpticalGeneralIfOpticalFecConfigLastChangeTime": ifOpticalGeneralIfOpticalFecConfigLastChangeTime,
       "ifOpticalGeneralIfOpticalFecStateLastChangeTime": ifOpticalGeneralIfOpticalFecStateLastChangeTime,
       "ifOpticalGeneralIfOpticalTransLaneCarrierTableSize": ifOpticalGeneralIfOpticalTransLaneCarrierTableSize,
       "ifOpticalGeneralIfOpticalTransLaneCarrierConfigLastChangeTime": ifOpticalGeneralIfOpticalTransLaneCarrierConfigLastChangeTime,
       "ifOpticalGeneralIfOpticalTransLaneCarrierStateLastChangeTime": ifOpticalGeneralIfOpticalTransLaneCarrierStateLastChangeTime,
       "ifOpticalGeneralIfOpticalTransLaneCarrierGroupTableSize": ifOpticalGeneralIfOpticalTransLaneCarrierGroupTableSize,
       "ifOpticalGeneralIfOpticalTransLaneCarrierGrConfigLastChangeTime": ifOpticalGeneralIfOpticalTransLaneCarrierGrConfigLastChangeTime,
       "ifOpticalGeneralIfOpticalTransLaneCarrierGrStateLastChangeTime": ifOpticalGeneralIfOpticalTransLaneCarrierGrStateLastChangeTime,
       "ifOpticalTransSectionList": ifOpticalTransSectionList,
       "ifOpticalTransSectionTable": ifOpticalTransSectionTable,
       "ifOpticalTransSectionEntry": ifOpticalTransSectionEntry,
       "ifOpticalTransSectionIndex": ifOpticalTransSectionIndex,
       "ifOpticalTransSectionName": ifOpticalTransSectionName,
       "ifOpticalTransSectionConnIfBasicIfIndex": ifOpticalTransSectionConnIfBasicIfIndex,
       "ifOpticalTransSectionForwardAls": ifOpticalTransSectionForwardAls,
       "ifOpticalTransSectionRxPowerLevel": ifOpticalTransSectionRxPowerLevel,
       "ifOpticalTransSectionRxPowerLevelLowRelativeThld": ifOpticalTransSectionRxPowerLevelLowRelativeThld,
       "ifOpticalTransSectionTxPowerLevel": ifOpticalTransSectionTxPowerLevel,
       "ifOpticalTransSectionLaserMode": ifOpticalTransSectionLaserMode,
       "ifOpticalTransSectionLaserStatus": ifOpticalTransSectionLaserStatus,
       "ifOpticalTransSectionReceiverSensitivity": ifOpticalTransSectionReceiverSensitivity,
       "ifOpticalTransSectionTxSignalStatus": ifOpticalTransSectionTxSignalStatus,
       "ifOpticalTransSectionRxSignalStatus": ifOpticalTransSectionRxSignalStatus,
       "ifOpticalTransSectionLossOfSignal": ifOpticalTransSectionLossOfSignal,
       "ifOpticalTransSectionRxPowerLevelLow": ifOpticalTransSectionRxPowerLevelLow,
       "ifOpticalTransSectionRxPowerLevelHigh": ifOpticalTransSectionRxPowerLevelHigh,
       "ifOpticalTransSectionRxExcessiveInputPower": ifOpticalTransSectionRxExcessiveInputPower,
       "ifOpticalTransSectionTxPowerLow": ifOpticalTransSectionTxPowerLow,
       "ifOpticalTransSectionRxPowerLevelLowAbsoluteThld": ifOpticalTransSectionRxPowerLevelLowAbsoluteThld,
       "ifOpticalTransSectionLossThld": ifOpticalTransSectionLossThld,
       "ifOpticalTransSectionLaserForcedOn": ifOpticalTransSectionLaserForcedOn,
       "ifOpticalChannelList": ifOpticalChannelList,
       "ifOpticalChannelTable": ifOpticalChannelTable,
       "ifOpticalChannelEntry": ifOpticalChannelEntry,
       "ifOpticalChannelIndex": ifOpticalChannelIndex,
       "ifOpticalChannelName": ifOpticalChannelName,
       "ifOpticalChannelConnIfBasicIfIndex": ifOpticalChannelConnIfBasicIfIndex,
       "ifOpticalChannelTxFrequency": ifOpticalChannelTxFrequency,
       "ifOpticalChannelExpectedTxFrequency": ifOpticalChannelExpectedTxFrequency,
       "ifOpticalChannelTxSignalStatus": ifOpticalChannelTxSignalStatus,
       "ifOpticalChannelRxSignalStatus": ifOpticalChannelRxSignalStatus,
       "ifOpticalChannelIllegalTxFrequency": ifOpticalChannelIllegalTxFrequency,
       "ifOpticalChannelUnexpectedTxFrequency": ifOpticalChannelUnexpectedTxFrequency,
       "ifOpticalChannelNoTxFrequencySet": ifOpticalChannelNoTxFrequencySet,
       "ifOpticalChannelDispersionSearchLimit": ifOpticalChannelDispersionSearchLimit,
       "ifOpticalChannelLaserNotTuned": ifOpticalChannelLaserNotTuned,
       "ifOpticalChannelLineCoding": ifOpticalChannelLineCoding,
       "ifOpticalDigitalSignalRateList": ifOpticalDigitalSignalRateList,
       "ifOpticalDigitalSignalRateTable": ifOpticalDigitalSignalRateTable,
       "ifOpticalDigitalSignalRateEntry": ifOpticalDigitalSignalRateEntry,
       "ifOpticalDigitalSignalRateIndex": ifOpticalDigitalSignalRateIndex,
       "ifOpticalDigitalSignalRateName": ifOpticalDigitalSignalRateName,
       "ifOpticalDigitalSignalRateConnIfBasicIfIndex": ifOpticalDigitalSignalRateConnIfBasicIfIndex,
       "ifOpticalDigitalSignalRateMaxBitRate": ifOpticalDigitalSignalRateMaxBitRate,
       "ifOpticalDigitalSignalRateMinBitRate": ifOpticalDigitalSignalRateMinBitRate,
       "ifOpticalDigitalSignalRateTxSignalStatus": ifOpticalDigitalSignalRateTxSignalStatus,
       "ifOpticalDigitalSignalRateRxSignalStatus": ifOpticalDigitalSignalRateRxSignalStatus,
       "ifOpticalDigitalSignalRateLossOfLock": ifOpticalDigitalSignalRateLossOfLock,
       "ifOpticalDigitalSignalRateBitrateUnavailable": ifOpticalDigitalSignalRateBitrateUnavailable,
       "ifOpticalFecList": ifOpticalFecList,
       "ifOpticalFecTable": ifOpticalFecTable,
       "ifOpticalFecEntry": ifOpticalFecEntry,
       "ifOpticalFecIndex": ifOpticalFecIndex,
       "ifOpticalFecName": ifOpticalFecName,
       "ifOpticalFecConnIfBasicIfIndex": ifOpticalFecConnIfBasicIfIndex,
       "ifOpticalFecType": ifOpticalFecType,
       "ifOpticalFecTxSignalStatus": ifOpticalFecTxSignalStatus,
       "ifOpticalFecRxSignalStatus": ifOpticalFecRxSignalStatus,
       "ifOpticalFecFailure": ifOpticalFecFailure,
       "ifOpticalFecSignalDegraded": ifOpticalFecSignalDegraded,
       "ifOpticalFecSignalDegradeThreshold": ifOpticalFecSignalDegradeThreshold,
       "ifOpticalFecTypeUnavailable": ifOpticalFecTypeUnavailable,
       "ifOpticalFecUId": ifOpticalFecUId,
       "ifOpticalFecDecModeMismatch": ifOpticalFecDecModeMismatch,
       "ifOpticalTransLaneCarrierList": ifOpticalTransLaneCarrierList,
       "ifOpticalTransLaneCarrierTable": ifOpticalTransLaneCarrierTable,
       "ifOpticalTransLaneCarrierEntry": ifOpticalTransLaneCarrierEntry,
       "ifOpticalTransLaneCarrierIndex": ifOpticalTransLaneCarrierIndex,
       "ifOpticalTransLaneCarrierName": ifOpticalTransLaneCarrierName,
       "ifOpticalTransLaneCarrierConnIfBasicIfIndex": ifOpticalTransLaneCarrierConnIfBasicIfIndex,
       "ifOpticalTransLaneCarrierConnIfOpticalTransLaneCarrierGrIndex": ifOpticalTransLaneCarrierConnIfOpticalTransLaneCarrierGrIndex,
       "ifOpticalTransLaneCarrierLaneId": ifOpticalTransLaneCarrierLaneId,
       "ifOpticalTransLaneCarrierTxSignalStatus": ifOpticalTransLaneCarrierTxSignalStatus,
       "ifOpticalTransLaneCarrierRxSignalStatus": ifOpticalTransLaneCarrierRxSignalStatus,
       "ifOpticalTransLaneCarrierRxPowerLevel": ifOpticalTransLaneCarrierRxPowerLevel,
       "ifOpticalTransLaneCarrierLossOfSignal": ifOpticalTransLaneCarrierLossOfSignal,
       "ifOpticalTransLaneCarrierReceiverSensitivity": ifOpticalTransLaneCarrierReceiverSensitivity,
       "ifOpticalTransLaneCarrierRxPowerLevelLow": ifOpticalTransLaneCarrierRxPowerLevelLow,
       "ifOpticalTransLaneCarrierTxFrequency": ifOpticalTransLaneCarrierTxFrequency,
       "ifOpticalTransLaneCarrierCounterSes": ifOpticalTransLaneCarrierCounterSes,
       "ifOpticalTransLaneCarrierCounterSesReset": ifOpticalTransLaneCarrierCounterSesReset,
       "ifOpticalTransLaneCarrierGroupList": ifOpticalTransLaneCarrierGroupList,
       "ifOpticalTransLaneCarrierGroupTable": ifOpticalTransLaneCarrierGroupTable,
       "ifOpticalTransLaneCarrierGroupEntry": ifOpticalTransLaneCarrierGroupEntry,
       "ifOpticalTransLaneCarrierGroupIndex": ifOpticalTransLaneCarrierGroupIndex,
       "ifOpticalTransLaneCarrierGroupName": ifOpticalTransLaneCarrierGroupName,
       "ifOpticalTransLaneCarrierGroupConnIfBasicIfIndex": ifOpticalTransLaneCarrierGroupConnIfBasicIfIndex,
       "ifOpticalTransLaneCarrierGroupTxSignalStatus": ifOpticalTransLaneCarrierGroupTxSignalStatus,
       "ifOpticalTransLaneCarrierGroupRxSignalStatus": ifOpticalTransLaneCarrierGroupRxSignalStatus,
       "ifOpticalTransLaneCarrierGroupForwardAls": ifOpticalTransLaneCarrierGroupForwardAls,
       "ifOpticalTransLaneCarrierGroupLaserStatus": ifOpticalTransLaneCarrierGroupLaserStatus,
       "ifOpticalTransLaneCarrierGroupTxPowerLevel": ifOpticalTransLaneCarrierGroupTxPowerLevel,
       "ifOpticalTransLaneCarrierGroupRxPowerLevel": ifOpticalTransLaneCarrierGroupRxPowerLevel,
       "ifOpticalTransLaneCarrierGroupLossOfSignal": ifOpticalTransLaneCarrierGroupLossOfSignal,
       "ifOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld": ifOpticalTransLaneCarrierGroupRxPowerLevelLowRelativeThld,
       "ifOpticalTransLaneCarrierGroupRxPowerLevelLow": ifOpticalTransLaneCarrierGroupRxPowerLevelLow,
       "ifOpticalTransLaneCarrierGroupTxFrequency": ifOpticalTransLaneCarrierGroupTxFrequency,
       "ifOpticalTransLaneCarrierGroupExpectedTxFrequency": ifOpticalTransLaneCarrierGroupExpectedTxFrequency,
       "ifOpticalTransLaneCarrierGroupUnexpectedTxFrequency": ifOpticalTransLaneCarrierGroupUnexpectedTxFrequency,
       "ifOpticalTransLaneCarrierGroupIllegalTxFrequency": ifOpticalTransLaneCarrierGroupIllegalTxFrequency,
       "ifOpticalTransLaneCarrierGroupCounterSesReset": ifOpticalTransLaneCarrierGroupCounterSesReset,
       "ifOpticalTransLaneCarrierGroupMinimumLaneRxPowerLevel": ifOpticalTransLaneCarrierGroupMinimumLaneRxPowerLevel,
       "ifOpticalTransLaneCarrierGroupReceiverLaneSensitivity": ifOpticalTransLaneCarrierGroupReceiverLaneSensitivity}
)
