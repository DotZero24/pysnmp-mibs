# SNMP MIB module (LUM-IFPHYSICAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/LUM-IFPHYSICAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:17:12 2025
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

(lumIfPhysicalMIB,
 lumModules) = mibBuilder.importSymbols(
    "LUM-REG",
    "lumIfPhysicalMIB",
    "lumModules")

(CommandString,
 DisplayStringWithNA,
 FaultStatusWithNA,
 Integer32WithNA,
 MgmtNameString,
 ResetWithNA,
 SignalStatusWithNA,
 SubrackNumber,
 TruthValueWithNA,
 TrxMediaWithNA,
 Unsigned32WithNA) = mibBuilder.importSymbols(
    "LUM-TC",
    "CommandString",
    "DisplayStringWithNA",
    "FaultStatusWithNA",
    "Integer32WithNA",
    "MgmtNameString",
    "ResetWithNA",
    "SignalStatusWithNA",
    "SubrackNumber",
    "TruthValueWithNA",
    "TrxMediaWithNA",
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

lumIfPhysicalMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 1, 1, 47)
)
if mibBuilder.loadTexts:
    lumIfPhysicalMIBModule.setRevisions(
        ("2017-06-15 00:00",
         "2017-04-21 00:00",
         "2016-12-12 00:00",
         "2016-11-30 00:00",
         "2015-12-22 00:00",
         "2015-10-30 00:00",
         "2015-01-23 00:00",
         "2014-10-30 00:00",
         "2014-09-30 00:00",
         "2014-05-16 00:00",
         "2013-11-15 00:00",
         "2012-11-20 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LumIfPhysicalConfs_ObjectIdentity = ObjectIdentity
lumIfPhysicalConfs = _LumIfPhysicalConfs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1)
)
_LumIfPhysicalGroups_ObjectIdentity = ObjectIdentity
lumIfPhysicalGroups = _LumIfPhysicalGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1)
)
_LumIfPhysicalCompl_ObjectIdentity = ObjectIdentity
lumIfPhysicalCompl = _LumIfPhysicalCompl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 2)
)
_LumIfPhysicalMIBObjects_ObjectIdentity = ObjectIdentity
lumIfPhysicalMIBObjects = _LumIfPhysicalMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2)
)
_IfPhysicalGeneral_ObjectIdentity = ObjectIdentity
ifPhysicalGeneral = _IfPhysicalGeneral_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 1)
)
_IfPhysicalGeneralConfigLastChangeTime_Type = DateAndTime
_IfPhysicalGeneralConfigLastChangeTime_Object = MibScalar
ifPhysicalGeneralConfigLastChangeTime = _IfPhysicalGeneralConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 1, 1),
    _IfPhysicalGeneralConfigLastChangeTime_Type()
)
ifPhysicalGeneralConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalGeneralConfigLastChangeTime.setStatus("current")
_IfPhysicalGeneralStateLastChangeTime_Type = DateAndTime
_IfPhysicalGeneralStateLastChangeTime_Object = MibScalar
ifPhysicalGeneralStateLastChangeTime = _IfPhysicalGeneralStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 1, 2),
    _IfPhysicalGeneralStateLastChangeTime_Type()
)
ifPhysicalGeneralStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalGeneralStateLastChangeTime.setStatus("current")
_IfPhysicalGeneralIfPhysicalTrxTableSize_Type = Unsigned32
_IfPhysicalGeneralIfPhysicalTrxTableSize_Object = MibScalar
ifPhysicalGeneralIfPhysicalTrxTableSize = _IfPhysicalGeneralIfPhysicalTrxTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 1, 3),
    _IfPhysicalGeneralIfPhysicalTrxTableSize_Type()
)
ifPhysicalGeneralIfPhysicalTrxTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalGeneralIfPhysicalTrxTableSize.setStatus("current")
_IfPhysicalGeneralIfPhysicalTrxConfigLastChangeTime_Type = DateAndTime
_IfPhysicalGeneralIfPhysicalTrxConfigLastChangeTime_Object = MibScalar
ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime = _IfPhysicalGeneralIfPhysicalTrxConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 1, 4),
    _IfPhysicalGeneralIfPhysicalTrxConfigLastChangeTime_Type()
)
ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime.setStatus("current")
_IfPhysicalGeneralIfPhysicalTrxStateLastChangeTime_Type = DateAndTime
_IfPhysicalGeneralIfPhysicalTrxStateLastChangeTime_Object = MibScalar
ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime = _IfPhysicalGeneralIfPhysicalTrxStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 1, 5),
    _IfPhysicalGeneralIfPhysicalTrxStateLastChangeTime_Type()
)
ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime.setStatus("current")
_IfPhysicalGeneralIfPhysicalCageTableSize_Type = Unsigned32
_IfPhysicalGeneralIfPhysicalCageTableSize_Object = MibScalar
ifPhysicalGeneralIfPhysicalCageTableSize = _IfPhysicalGeneralIfPhysicalCageTableSize_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 1, 6),
    _IfPhysicalGeneralIfPhysicalCageTableSize_Type()
)
ifPhysicalGeneralIfPhysicalCageTableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalGeneralIfPhysicalCageTableSize.setStatus("current")
_IfPhysicalGeneralIfPhysicalCageConfigLastChangeTime_Type = DateAndTime
_IfPhysicalGeneralIfPhysicalCageConfigLastChangeTime_Object = MibScalar
ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime = _IfPhysicalGeneralIfPhysicalCageConfigLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 1, 7),
    _IfPhysicalGeneralIfPhysicalCageConfigLastChangeTime_Type()
)
ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime.setStatus("current")
_IfPhysicalGeneralIfPhysicalCageStateLastChangeTime_Type = DateAndTime
_IfPhysicalGeneralIfPhysicalCageStateLastChangeTime_Object = MibScalar
ifPhysicalGeneralIfPhysicalCageStateLastChangeTime = _IfPhysicalGeneralIfPhysicalCageStateLastChangeTime_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 1, 8),
    _IfPhysicalGeneralIfPhysicalCageStateLastChangeTime_Type()
)
ifPhysicalGeneralIfPhysicalCageStateLastChangeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalGeneralIfPhysicalCageStateLastChangeTime.setStatus("current")
_IfPhysicalTrxList_ObjectIdentity = ObjectIdentity
ifPhysicalTrxList = _IfPhysicalTrxList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2)
)
_IfPhysicalTrxTable_Object = MibTable
ifPhysicalTrxTable = _IfPhysicalTrxTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1)
)
if mibBuilder.loadTexts:
    ifPhysicalTrxTable.setStatus("current")
_IfPhysicalTrxEntry_Object = MibTableRow
ifPhysicalTrxEntry = _IfPhysicalTrxEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1)
)
ifPhysicalTrxEntry.setIndexNames(
    (0, "LUM-IFPHYSICAL-MIB", "ifPhysicalTrxIndex"),
)
if mibBuilder.loadTexts:
    ifPhysicalTrxEntry.setStatus("current")
_IfPhysicalTrxIndex_Type = Unsigned32
_IfPhysicalTrxIndex_Object = MibTableColumn
ifPhysicalTrxIndex = _IfPhysicalTrxIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 1),
    _IfPhysicalTrxIndex_Type()
)
ifPhysicalTrxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxIndex.setStatus("current")
_IfPhysicalTrxName_Type = MgmtNameString
_IfPhysicalTrxName_Object = MibTableColumn
ifPhysicalTrxName = _IfPhysicalTrxName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 2),
    _IfPhysicalTrxName_Type()
)
ifPhysicalTrxName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxName.setStatus("current")
_IfPhysicalTrxConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfPhysicalTrxConnIfBasicIfIndex_Object = MibTableColumn
ifPhysicalTrxConnIfBasicIfIndex = _IfPhysicalTrxConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 3),
    _IfPhysicalTrxConnIfBasicIfIndex_Type()
)
ifPhysicalTrxConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxConnIfBasicIfIndex.setStatus("current")
_IfPhysicalTrxLaserBias_Type = Unsigned32WithNA
_IfPhysicalTrxLaserBias_Object = MibTableColumn
ifPhysicalTrxLaserBias = _IfPhysicalTrxLaserBias_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 4),
    _IfPhysicalTrxLaserBias_Type()
)
ifPhysicalTrxLaserBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxLaserBias.setStatus("current")
_IfPhysicalTrxLaserTemp_Type = Integer32WithNA
_IfPhysicalTrxLaserTemp_Object = MibTableColumn
ifPhysicalTrxLaserTemp = _IfPhysicalTrxLaserTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 5),
    _IfPhysicalTrxLaserTemp_Type()
)
ifPhysicalTrxLaserTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxLaserTemp.setStatus("current")


class _IfPhysicalTrxTrxClass_Type(DisplayStringWithNA):
    """Custom type ifPhysicalTrxTrxClass based on DisplayStringWithNA"""
    defaultValue = OctetString("")


_IfPhysicalTrxTrxClass_Type.__name__ = "DisplayStringWithNA"
_IfPhysicalTrxTrxClass_Object = MibTableColumn
ifPhysicalTrxTrxClass = _IfPhysicalTrxTrxClass_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 6),
    _IfPhysicalTrxTrxClass_Type()
)
ifPhysicalTrxTrxClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxTrxClass.setStatus("current")


class _IfPhysicalTrxTrxMedia_Type(TrxMediaWithNA):
    """Custom type ifPhysicalTrxTrxMedia based on TrxMediaWithNA"""
    defaultValue = 1


_IfPhysicalTrxTrxMedia_Type.__name__ = "TrxMediaWithNA"
_IfPhysicalTrxTrxMedia_Object = MibTableColumn
ifPhysicalTrxTrxMedia = _IfPhysicalTrxTrxMedia_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 7),
    _IfPhysicalTrxTrxMedia_Type()
)
ifPhysicalTrxTrxMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ifPhysicalTrxTrxMedia.setStatus("current")


class _IfPhysicalTrxActualTrxMedia_Type(TrxMediaWithNA):
    """Custom type ifPhysicalTrxActualTrxMedia based on TrxMediaWithNA"""
    defaultValue = 1


_IfPhysicalTrxActualTrxMedia_Type.__name__ = "TrxMediaWithNA"
_IfPhysicalTrxActualTrxMedia_Object = MibTableColumn
ifPhysicalTrxActualTrxMedia = _IfPhysicalTrxActualTrxMedia_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 8),
    _IfPhysicalTrxActualTrxMedia_Type()
)
ifPhysicalTrxActualTrxMedia.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxActualTrxMedia.setStatus("current")
_IfPhysicalTrxTxSignalStatus_Type = SignalStatusWithNA
_IfPhysicalTrxTxSignalStatus_Object = MibTableColumn
ifPhysicalTrxTxSignalStatus = _IfPhysicalTrxTxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 9),
    _IfPhysicalTrxTxSignalStatus_Type()
)
ifPhysicalTrxTxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxTxSignalStatus.setStatus("current")
_IfPhysicalTrxRxSignalStatus_Type = SignalStatusWithNA
_IfPhysicalTrxRxSignalStatus_Object = MibTableColumn
ifPhysicalTrxRxSignalStatus = _IfPhysicalTrxRxSignalStatus_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 10),
    _IfPhysicalTrxRxSignalStatus_Type()
)
ifPhysicalTrxRxSignalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxRxSignalStatus.setStatus("current")
_IfPhysicalTrxTransmitterFailed_Type = FaultStatusWithNA
_IfPhysicalTrxTransmitterFailed_Object = MibTableColumn
ifPhysicalTrxTransmitterFailed = _IfPhysicalTrxTransmitterFailed_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 11),
    _IfPhysicalTrxTransmitterFailed_Type()
)
ifPhysicalTrxTransmitterFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxTransmitterFailed.setStatus("current")
_IfPhysicalTrxNonQualifiedTrx_Type = FaultStatusWithNA
_IfPhysicalTrxNonQualifiedTrx_Object = MibTableColumn
ifPhysicalTrxNonQualifiedTrx = _IfPhysicalTrxNonQualifiedTrx_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 12),
    _IfPhysicalTrxNonQualifiedTrx_Type()
)
ifPhysicalTrxNonQualifiedTrx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxNonQualifiedTrx.setStatus("current")
_IfPhysicalTrxTrxMissing_Type = FaultStatusWithNA
_IfPhysicalTrxTrxMissing_Object = MibTableColumn
ifPhysicalTrxTrxMissing = _IfPhysicalTrxTrxMissing_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 13),
    _IfPhysicalTrxTrxMissing_Type()
)
ifPhysicalTrxTrxMissing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxTrxMissing.setStatus("current")
_IfPhysicalTrxTrxMediaMismatch_Type = FaultStatusWithNA
_IfPhysicalTrxTrxMediaMismatch_Object = MibTableColumn
ifPhysicalTrxTrxMediaMismatch = _IfPhysicalTrxTrxMediaMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 14),
    _IfPhysicalTrxTrxMediaMismatch_Type()
)
ifPhysicalTrxTrxMediaMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxTrxMediaMismatch.setStatus("current")


class _IfPhysicalTrxTrxRxState_Type(DisplayStringWithNA):
    """Custom type ifPhysicalTrxTrxRxState based on DisplayStringWithNA"""
    defaultValue = OctetString("")


_IfPhysicalTrxTrxRxState_Type.__name__ = "DisplayStringWithNA"
_IfPhysicalTrxTrxRxState_Object = MibTableColumn
ifPhysicalTrxTrxRxState = _IfPhysicalTrxTrxRxState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 15),
    _IfPhysicalTrxTrxRxState_Type()
)
ifPhysicalTrxTrxRxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxTrxRxState.setStatus("current")


class _IfPhysicalTrxTrxTxState_Type(DisplayStringWithNA):
    """Custom type ifPhysicalTrxTrxTxState based on DisplayStringWithNA"""
    defaultValue = OctetString("")


_IfPhysicalTrxTrxTxState_Type.__name__ = "DisplayStringWithNA"
_IfPhysicalTrxTrxTxState_Object = MibTableColumn
ifPhysicalTrxTrxTxState = _IfPhysicalTrxTrxTxState_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 16),
    _IfPhysicalTrxTrxTxState_Type()
)
ifPhysicalTrxTrxTxState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxTrxTxState.setStatus("current")
_IfPhysicalTrxOpticalLayerMappingMismatch_Type = FaultStatusWithNA
_IfPhysicalTrxOpticalLayerMappingMismatch_Object = MibTableColumn
ifPhysicalTrxOpticalLayerMappingMismatch = _IfPhysicalTrxOpticalLayerMappingMismatch_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 17),
    _IfPhysicalTrxOpticalLayerMappingMismatch_Type()
)
ifPhysicalTrxOpticalLayerMappingMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxOpticalLayerMappingMismatch.setStatus("current")


class _IfPhysicalTrxPowerCycleReset_Type(ResetWithNA):
    """Custom type ifPhysicalTrxPowerCycleReset based on ResetWithNA"""
    defaultValue = 2


_IfPhysicalTrxPowerCycleReset_Type.__name__ = "ResetWithNA"
_IfPhysicalTrxPowerCycleReset_Object = MibTableColumn
ifPhysicalTrxPowerCycleReset = _IfPhysicalTrxPowerCycleReset_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 18),
    _IfPhysicalTrxPowerCycleReset_Type()
)
ifPhysicalTrxPowerCycleReset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxPowerCycleReset.setStatus("current")
_IfPhysicalTrxUId_Type = Unsigned32
_IfPhysicalTrxUId_Object = MibTableColumn
ifPhysicalTrxUId = _IfPhysicalTrxUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 19),
    _IfPhysicalTrxUId_Type()
)
ifPhysicalTrxUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxUId.setStatus("current")
_IfPhysicalTrxAid_Type = DisplayString
_IfPhysicalTrxAid_Object = MibTableColumn
ifPhysicalTrxAid = _IfPhysicalTrxAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 20),
    _IfPhysicalTrxAid_Type()
)
ifPhysicalTrxAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxAid.setStatus("current")
_IfPhysicalTrxPhysicalLocation_Type = DisplayString
_IfPhysicalTrxPhysicalLocation_Object = MibTableColumn
ifPhysicalTrxPhysicalLocation = _IfPhysicalTrxPhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 21),
    _IfPhysicalTrxPhysicalLocation_Type()
)
ifPhysicalTrxPhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxPhysicalLocation.setStatus("current")
_IfPhysicalTrxPowerOutOfRange_Type = FaultStatusWithNA
_IfPhysicalTrxPowerOutOfRange_Object = MibTableColumn
ifPhysicalTrxPowerOutOfRange = _IfPhysicalTrxPowerOutOfRange_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 22),
    _IfPhysicalTrxPowerOutOfRange_Type()
)
ifPhysicalTrxPowerOutOfRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxPowerOutOfRange.setStatus("current")
_IfPhysicalTrxLowTemp_Type = FaultStatusWithNA
_IfPhysicalTrxLowTemp_Object = MibTableColumn
ifPhysicalTrxLowTemp = _IfPhysicalTrxLowTemp_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 23),
    _IfPhysicalTrxLowTemp_Type()
)
ifPhysicalTrxLowTemp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxLowTemp.setStatus("current")
_IfPhysicalTrxCommunicationFailure_Type = FaultStatusWithNA
_IfPhysicalTrxCommunicationFailure_Object = MibTableColumn
ifPhysicalTrxCommunicationFailure = _IfPhysicalTrxCommunicationFailure_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 2, 1, 1, 24),
    _IfPhysicalTrxCommunicationFailure_Type()
)
ifPhysicalTrxCommunicationFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalTrxCommunicationFailure.setStatus("current")
_IfPhysicalCageList_ObjectIdentity = ObjectIdentity
ifPhysicalCageList = _IfPhysicalCageList_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3)
)
_IfPhysicalCageTable_Object = MibTable
ifPhysicalCageTable = _IfPhysicalCageTable_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1)
)
if mibBuilder.loadTexts:
    ifPhysicalCageTable.setStatus("current")
_IfPhysicalCageEntry_Object = MibTableRow
ifPhysicalCageEntry = _IfPhysicalCageEntry_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1, 1)
)
ifPhysicalCageEntry.setIndexNames(
    (0, "LUM-IFPHYSICAL-MIB", "ifPhysicalCageIndex"),
)
if mibBuilder.loadTexts:
    ifPhysicalCageEntry.setStatus("current")
_IfPhysicalCageIndex_Type = Unsigned32
_IfPhysicalCageIndex_Object = MibTableColumn
ifPhysicalCageIndex = _IfPhysicalCageIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1, 1, 1),
    _IfPhysicalCageIndex_Type()
)
ifPhysicalCageIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalCageIndex.setStatus("current")
_IfPhysicalCageName_Type = MgmtNameString
_IfPhysicalCageName_Object = MibTableColumn
ifPhysicalCageName = _IfPhysicalCageName_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1, 1, 2),
    _IfPhysicalCageName_Type()
)
ifPhysicalCageName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalCageName.setStatus("current")
_IfPhysicalCageConnIfBasicIfIndex_Type = Unsigned32WithNA
_IfPhysicalCageConnIfBasicIfIndex_Object = MibTableColumn
ifPhysicalCageConnIfBasicIfIndex = _IfPhysicalCageConnIfBasicIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1, 1, 3),
    _IfPhysicalCageConnIfBasicIfIndex_Type()
)
ifPhysicalCageConnIfBasicIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalCageConnIfBasicIfIndex.setStatus("current")
_IfPhysicalCageSubrack_Type = SubrackNumber
_IfPhysicalCageSubrack_Object = MibTableColumn
ifPhysicalCageSubrack = _IfPhysicalCageSubrack_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1, 1, 4),
    _IfPhysicalCageSubrack_Type()
)
ifPhysicalCageSubrack.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalCageSubrack.setStatus("current")
_IfPhysicalCageSlot_Type = Unsigned32
_IfPhysicalCageSlot_Object = MibTableColumn
ifPhysicalCageSlot = _IfPhysicalCageSlot_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1, 1, 5),
    _IfPhysicalCageSlot_Type()
)
ifPhysicalCageSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalCageSlot.setStatus("current")
_IfPhysicalCageAid_Type = DisplayString
_IfPhysicalCageAid_Object = MibTableColumn
ifPhysicalCageAid = _IfPhysicalCageAid_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1, 1, 6),
    _IfPhysicalCageAid_Type()
)
ifPhysicalCageAid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalCageAid.setStatus("current")
_IfPhysicalCagePhysicalLocation_Type = DisplayString
_IfPhysicalCagePhysicalLocation_Object = MibTableColumn
ifPhysicalCagePhysicalLocation = _IfPhysicalCagePhysicalLocation_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1, 1, 7),
    _IfPhysicalCagePhysicalLocation_Type()
)
ifPhysicalCagePhysicalLocation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalCagePhysicalLocation.setStatus("current")


class _IfPhysicalCageEquipped_Type(TruthValueWithNA):
    """Custom type ifPhysicalCageEquipped based on TruthValueWithNA"""
    defaultValue = 2147483647


_IfPhysicalCageEquipped_Type.__name__ = "TruthValueWithNA"
_IfPhysicalCageEquipped_Object = MibTableColumn
ifPhysicalCageEquipped = _IfPhysicalCageEquipped_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1, 1, 8),
    _IfPhysicalCageEquipped_Type()
)
ifPhysicalCageEquipped.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalCageEquipped.setStatus("current")
_IfPhysicalCageUId_Type = Unsigned32
_IfPhysicalCageUId_Object = MibTableColumn
ifPhysicalCageUId = _IfPhysicalCageUId_Object(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 2, 3, 1, 1, 9),
    _IfPhysicalCageUId_Type()
)
ifPhysicalCageUId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ifPhysicalCageUId.setStatus("current")

# Managed Objects groups

ifPhysicalGeneralGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1, 1)
)
ifPhysicalGeneralGroupV1.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralConfigLastChangeTime"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralStateLastChangeTime"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralIfPhysicalTrxTableSize"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifPhysicalGeneralGroupV1.setStatus("deprecated")

ifPhysicalTrxGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1, 2)
)
ifPhysicalTrxGroupV1.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxName"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxConnIfBasicIfIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserBias"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserTemp"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxClass"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxActualTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxRxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTransmitterFailed"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxNonQualifiedTrx"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMissing"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMediaMismatch"))
)
if mibBuilder.loadTexts:
    ifPhysicalTrxGroupV1.setStatus("deprecated")

ifPhysicalTrxGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1, 3)
)
ifPhysicalTrxGroupV2.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxName"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxConnIfBasicIfIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserBias"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserTemp"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxClass"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxActualTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxRxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTransmitterFailed"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxNonQualifiedTrx"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMissing"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMediaMismatch"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxRxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxTxState"))
)
if mibBuilder.loadTexts:
    ifPhysicalTrxGroupV2.setStatus("deprecated")

ifPhysicalTrxGroupV3 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1, 4)
)
ifPhysicalTrxGroupV3.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxName"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxConnIfBasicIfIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserBias"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserTemp"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxClass"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxActualTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxRxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTransmitterFailed"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxNonQualifiedTrx"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMissing"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMediaMismatch"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxRxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxTxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxOpticalLayerMappingMismatch"))
)
if mibBuilder.loadTexts:
    ifPhysicalTrxGroupV3.setStatus("deprecated")

ifPhysicalTrxGroupV4 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1, 5)
)
ifPhysicalTrxGroupV4.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxName"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxConnIfBasicIfIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserBias"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserTemp"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxClass"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxActualTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxRxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTransmitterFailed"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxNonQualifiedTrx"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMissing"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMediaMismatch"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxRxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxTxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxOpticalLayerMappingMismatch"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxPowerCycleReset"))
)
if mibBuilder.loadTexts:
    ifPhysicalTrxGroupV4.setStatus("deprecated")

ifPhysicalTrxGroupV5 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1, 6)
)
ifPhysicalTrxGroupV5.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxName"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxConnIfBasicIfIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserBias"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserTemp"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxClass"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxActualTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxRxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTransmitterFailed"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxNonQualifiedTrx"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMissing"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMediaMismatch"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxRxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxTxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxOpticalLayerMappingMismatch"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxPowerCycleReset"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxUId"))
)
if mibBuilder.loadTexts:
    ifPhysicalTrxGroupV5.setStatus("deprecated")

ifPhysicalGeneralGroupV2 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1, 7)
)
ifPhysicalGeneralGroupV2.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralConfigLastChangeTime"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralStateLastChangeTime"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralIfPhysicalTrxTableSize"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralIfPhysicalCageTableSize"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralIfPhysicalCageStateLastChangeTime"))
)
if mibBuilder.loadTexts:
    ifPhysicalGeneralGroupV2.setStatus("current")

ifPhysicalCageGroupV1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1, 8)
)
ifPhysicalCageGroupV1.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalCageIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalCageName"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalCageConnIfBasicIfIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalCageSubrack"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalCageSlot"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalCageAid"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalCagePhysicalLocation"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalCageEquipped"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalCageUId"))
)
if mibBuilder.loadTexts:
    ifPhysicalCageGroupV1.setStatus("current")

ifPhysicalTrxGroupV6 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1, 9)
)
ifPhysicalTrxGroupV6.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxName"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxConnIfBasicIfIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserBias"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserTemp"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxClass"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxActualTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxRxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTransmitterFailed"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxNonQualifiedTrx"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMissing"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMediaMismatch"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxRxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxTxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxOpticalLayerMappingMismatch"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxPowerCycleReset"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxUId"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxAid"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxPhysicalLocation"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxPowerOutOfRange"))
)
if mibBuilder.loadTexts:
    ifPhysicalTrxGroupV6.setStatus("deprecated")

ifPhysicalTrxGroupV7 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 1, 10)
)
ifPhysicalTrxGroupV7.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxName"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxConnIfBasicIfIndex"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserBias"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLaserTemp"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxClass"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxActualTrxMedia"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxRxSignalStatus"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTransmitterFailed"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxNonQualifiedTrx"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMissing"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxMediaMismatch"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxRxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxTrxTxState"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxOpticalLayerMappingMismatch"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxPowerCycleReset"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxUId"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxAid"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxPhysicalLocation"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxPowerOutOfRange"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxLowTemp"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxCommunicationFailure"))
)
if mibBuilder.loadTexts:
    ifPhysicalTrxGroupV7.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lumIfPhysicalComplV1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 2, 1)
)
lumIfPhysicalComplV1.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralGroupV1"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPhysicalComplV1.setStatus(
        "deprecated"
    )

lumIfPhysicalComplV2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 2, 2)
)
lumIfPhysicalComplV2.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralGroupV1"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxGroupV2"))
)
if mibBuilder.loadTexts:
    lumIfPhysicalComplV2.setStatus(
        "deprecated"
    )

lumIfPhysicalComplV3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 2, 3)
)
lumIfPhysicalComplV3.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralGroupV1"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxGroupV3"))
)
if mibBuilder.loadTexts:
    lumIfPhysicalComplV3.setStatus(
        "deprecated"
    )

lumIfPhysicalComplV4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 2, 4)
)
lumIfPhysicalComplV4.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralGroupV1"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxGroupV5"))
)
if mibBuilder.loadTexts:
    lumIfPhysicalComplV4.setStatus(
        "deprecated"
    )

lumIfPhysicalComplV5 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 2, 5)
)
lumIfPhysicalComplV5.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralGroupV2"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxGroupV6"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalCageGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPhysicalComplV5.setStatus(
        "deprecated"
    )

lumIfPhysicalComplV6 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 8708, 2, 47, 1, 2, 6)
)
lumIfPhysicalComplV6.setObjects(
      *(("LUM-IFPHYSICAL-MIB", "ifPhysicalGeneralGroupV2"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalTrxGroupV7"),
        ("LUM-IFPHYSICAL-MIB", "ifPhysicalCageGroupV1"))
)
if mibBuilder.loadTexts:
    lumIfPhysicalComplV6.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LUM-IFPHYSICAL-MIB",
    **{"lumIfPhysicalMIBModule": lumIfPhysicalMIBModule,
       "lumIfPhysicalConfs": lumIfPhysicalConfs,
       "lumIfPhysicalGroups": lumIfPhysicalGroups,
       "ifPhysicalGeneralGroupV1": ifPhysicalGeneralGroupV1,
       "ifPhysicalTrxGroupV1": ifPhysicalTrxGroupV1,
       "ifPhysicalTrxGroupV2": ifPhysicalTrxGroupV2,
       "ifPhysicalTrxGroupV3": ifPhysicalTrxGroupV3,
       "ifPhysicalTrxGroupV4": ifPhysicalTrxGroupV4,
       "ifPhysicalTrxGroupV5": ifPhysicalTrxGroupV5,
       "ifPhysicalGeneralGroupV2": ifPhysicalGeneralGroupV2,
       "ifPhysicalCageGroupV1": ifPhysicalCageGroupV1,
       "ifPhysicalTrxGroupV6": ifPhysicalTrxGroupV6,
       "ifPhysicalTrxGroupV7": ifPhysicalTrxGroupV7,
       "lumIfPhysicalCompl": lumIfPhysicalCompl,
       "lumIfPhysicalComplV1": lumIfPhysicalComplV1,
       "lumIfPhysicalComplV2": lumIfPhysicalComplV2,
       "lumIfPhysicalComplV3": lumIfPhysicalComplV3,
       "lumIfPhysicalComplV4": lumIfPhysicalComplV4,
       "lumIfPhysicalComplV5": lumIfPhysicalComplV5,
       "lumIfPhysicalComplV6": lumIfPhysicalComplV6,
       "lumIfPhysicalMIBObjects": lumIfPhysicalMIBObjects,
       "ifPhysicalGeneral": ifPhysicalGeneral,
       "ifPhysicalGeneralConfigLastChangeTime": ifPhysicalGeneralConfigLastChangeTime,
       "ifPhysicalGeneralStateLastChangeTime": ifPhysicalGeneralStateLastChangeTime,
       "ifPhysicalGeneralIfPhysicalTrxTableSize": ifPhysicalGeneralIfPhysicalTrxTableSize,
       "ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime": ifPhysicalGeneralIfPhysicalTrxConfigLastChangeTime,
       "ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime": ifPhysicalGeneralIfPhysicalTrxStateLastChangeTime,
       "ifPhysicalGeneralIfPhysicalCageTableSize": ifPhysicalGeneralIfPhysicalCageTableSize,
       "ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime": ifPhysicalGeneralIfPhysicalCageConfigLastChangeTime,
       "ifPhysicalGeneralIfPhysicalCageStateLastChangeTime": ifPhysicalGeneralIfPhysicalCageStateLastChangeTime,
       "ifPhysicalTrxList": ifPhysicalTrxList,
       "ifPhysicalTrxTable": ifPhysicalTrxTable,
       "ifPhysicalTrxEntry": ifPhysicalTrxEntry,
       "ifPhysicalTrxIndex": ifPhysicalTrxIndex,
       "ifPhysicalTrxName": ifPhysicalTrxName,
       "ifPhysicalTrxConnIfBasicIfIndex": ifPhysicalTrxConnIfBasicIfIndex,
       "ifPhysicalTrxLaserBias": ifPhysicalTrxLaserBias,
       "ifPhysicalTrxLaserTemp": ifPhysicalTrxLaserTemp,
       "ifPhysicalTrxTrxClass": ifPhysicalTrxTrxClass,
       "ifPhysicalTrxTrxMedia": ifPhysicalTrxTrxMedia,
       "ifPhysicalTrxActualTrxMedia": ifPhysicalTrxActualTrxMedia,
       "ifPhysicalTrxTxSignalStatus": ifPhysicalTrxTxSignalStatus,
       "ifPhysicalTrxRxSignalStatus": ifPhysicalTrxRxSignalStatus,
       "ifPhysicalTrxTransmitterFailed": ifPhysicalTrxTransmitterFailed,
       "ifPhysicalTrxNonQualifiedTrx": ifPhysicalTrxNonQualifiedTrx,
       "ifPhysicalTrxTrxMissing": ifPhysicalTrxTrxMissing,
       "ifPhysicalTrxTrxMediaMismatch": ifPhysicalTrxTrxMediaMismatch,
       "ifPhysicalTrxTrxRxState": ifPhysicalTrxTrxRxState,
       "ifPhysicalTrxTrxTxState": ifPhysicalTrxTrxTxState,
       "ifPhysicalTrxOpticalLayerMappingMismatch": ifPhysicalTrxOpticalLayerMappingMismatch,
       "ifPhysicalTrxPowerCycleReset": ifPhysicalTrxPowerCycleReset,
       "ifPhysicalTrxUId": ifPhysicalTrxUId,
       "ifPhysicalTrxAid": ifPhysicalTrxAid,
       "ifPhysicalTrxPhysicalLocation": ifPhysicalTrxPhysicalLocation,
       "ifPhysicalTrxPowerOutOfRange": ifPhysicalTrxPowerOutOfRange,
       "ifPhysicalTrxLowTemp": ifPhysicalTrxLowTemp,
       "ifPhysicalTrxCommunicationFailure": ifPhysicalTrxCommunicationFailure,
       "ifPhysicalCageList": ifPhysicalCageList,
       "ifPhysicalCageTable": ifPhysicalCageTable,
       "ifPhysicalCageEntry": ifPhysicalCageEntry,
       "ifPhysicalCageIndex": ifPhysicalCageIndex,
       "ifPhysicalCageName": ifPhysicalCageName,
       "ifPhysicalCageConnIfBasicIfIndex": ifPhysicalCageConnIfBasicIfIndex,
       "ifPhysicalCageSubrack": ifPhysicalCageSubrack,
       "ifPhysicalCageSlot": ifPhysicalCageSlot,
       "ifPhysicalCageAid": ifPhysicalCageAid,
       "ifPhysicalCagePhysicalLocation": ifPhysicalCagePhysicalLocation,
       "ifPhysicalCageEquipped": ifPhysicalCageEquipped,
       "ifPhysicalCageUId": ifPhysicalCageUId}
)
