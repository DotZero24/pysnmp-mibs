# SNMP MIB module (INFINERA-TP-OTDRTESTRESULT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OTDRTESTRESULT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:26 2025
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

(FloatHundredths,
 InfnFiberType,
 InfnOtdrFileUploadStatus,
 InfnOtdrPtpConnState,
 InfnOtdrTestAcquisitionMode,
 InfnOtdrTestExecutionType,
 InfnOtdrTestPulseWidth) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnFiberType",
    "InfnOtdrFileUploadStatus",
    "InfnOtdrPtpConnState",
    "InfnOtdrTestAcquisitionMode",
    "InfnOtdrTestExecutionType",
    "InfnOtdrTestPulseWidth")

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

otdrTestResultMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtdrTestResultTable_Object = MibTable
otdrTestResultTable = _OtdrTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1)
)
if mibBuilder.loadTexts:
    otdrTestResultTable.setStatus("current")
_OtdrTestResultEntry_Object = MibTableRow
otdrTestResultEntry = _OtdrTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1)
)
otdrTestResultEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    otdrTestResultEntry.setStatus("current")
_OtdrTestResultTimeStamp_Type = Integer32
_OtdrTestResultTimeStamp_Object = MibTableColumn
otdrTestResultTimeStamp = _OtdrTestResultTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 1),
    _OtdrTestResultTimeStamp_Type()
)
otdrTestResultTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultTimeStamp.setStatus("current")
_OtdrTestResultOtdmSerialNumber_Type = DisplayString
_OtdrTestResultOtdmSerialNumber_Object = MibTableColumn
otdrTestResultOtdmSerialNumber = _OtdrTestResultOtdmSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 2),
    _OtdrTestResultOtdmSerialNumber_Type()
)
otdrTestResultOtdmSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultOtdmSerialNumber.setStatus("current")
_OtdrTestResultOtdmPortId_Type = DisplayString
_OtdrTestResultOtdmPortId_Object = MibTableColumn
otdrTestResultOtdmPortId = _OtdrTestResultOtdmPortId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 3),
    _OtdrTestResultOtdmPortId_Type()
)
otdrTestResultOtdmPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultOtdmPortId.setStatus("current")
_OtdrTestResultTestExecutionType_Type = InfnOtdrTestExecutionType
_OtdrTestResultTestExecutionType_Object = MibTableColumn
otdrTestResultTestExecutionType = _OtdrTestResultTestExecutionType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 4),
    _OtdrTestResultTestExecutionType_Type()
)
otdrTestResultTestExecutionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultTestExecutionType.setStatus("current")
_OtdrTestResultAcquisitionMode_Type = InfnOtdrTestAcquisitionMode
_OtdrTestResultAcquisitionMode_Object = MibTableColumn
otdrTestResultAcquisitionMode = _OtdrTestResultAcquisitionMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 5),
    _OtdrTestResultAcquisitionMode_Type()
)
otdrTestResultAcquisitionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultAcquisitionMode.setStatus("current")
_OtdrTestResultProvisionedNeighborPtp_Type = DisplayString
_OtdrTestResultProvisionedNeighborPtp_Object = MibTableColumn
otdrTestResultProvisionedNeighborPtp = _OtdrTestResultProvisionedNeighborPtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 6),
    _OtdrTestResultProvisionedNeighborPtp_Type()
)
otdrTestResultProvisionedNeighborPtp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultProvisionedNeighborPtp.setStatus("current")
_OtdrTestResultConnectivityState_Type = InfnOtdrPtpConnState
_OtdrTestResultConnectivityState_Object = MibTableColumn
otdrTestResultConnectivityState = _OtdrTestResultConnectivityState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 7),
    _OtdrTestResultConnectivityState_Type()
)
otdrTestResultConnectivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultConnectivityState.setStatus("current")
_OtdrTestResultTestCableID_Type = DisplayString
_OtdrTestResultTestCableID_Object = MibTableColumn
otdrTestResultTestCableID = _OtdrTestResultTestCableID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 8),
    _OtdrTestResultTestCableID_Type()
)
otdrTestResultTestCableID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultTestCableID.setStatus("current")
_OtdrTestResultTestFiberID_Type = DisplayString
_OtdrTestResultTestFiberID_Object = MibTableColumn
otdrTestResultTestFiberID = _OtdrTestResultTestFiberID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 9),
    _OtdrTestResultTestFiberID_Type()
)
otdrTestResultTestFiberID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultTestFiberID.setStatus("current")
_OtdrTestResultTestFiberType_Type = InfnFiberType
_OtdrTestResultTestFiberType_Object = MibTableColumn
otdrTestResultTestFiberType = _OtdrTestResultTestFiberType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 10),
    _OtdrTestResultTestFiberType_Type()
)
otdrTestResultTestFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultTestFiberType.setStatus("current")
_OtdrTestResultDataPointsCount_Type = Integer32
_OtdrTestResultDataPointsCount_Object = MibTableColumn
otdrTestResultDataPointsCount = _OtdrTestResultDataPointsCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 11),
    _OtdrTestResultDataPointsCount_Type()
)
otdrTestResultDataPointsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultDataPointsCount.setStatus("current")
_OtdrTestResultKeyEventsCount_Type = Integer32
_OtdrTestResultKeyEventsCount_Object = MibTableColumn
otdrTestResultKeyEventsCount = _OtdrTestResultKeyEventsCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 12),
    _OtdrTestResultKeyEventsCount_Type()
)
otdrTestResultKeyEventsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultKeyEventsCount.setStatus("current")
_OtdrTestResultEndToEndLoss_Type = FloatHundredths
_OtdrTestResultEndToEndLoss_Object = MibTableColumn
otdrTestResultEndToEndLoss = _OtdrTestResultEndToEndLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 13),
    _OtdrTestResultEndToEndLoss_Type()
)
otdrTestResultEndToEndLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultEndToEndLoss.setStatus("current")
_OtdrTestResultOpticalReturnLoss_Type = FloatHundredths
_OtdrTestResultOpticalReturnLoss_Object = MibTableColumn
otdrTestResultOpticalReturnLoss = _OtdrTestResultOpticalReturnLoss_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 14),
    _OtdrTestResultOpticalReturnLoss_Type()
)
otdrTestResultOpticalReturnLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultOpticalReturnLoss.setStatus("current")
_OtdrTestResultUnitsOfDistance_Type = DisplayString
_OtdrTestResultUnitsOfDistance_Object = MibTableColumn
otdrTestResultUnitsOfDistance = _OtdrTestResultUnitsOfDistance_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 15),
    _OtdrTestResultUnitsOfDistance_Type()
)
otdrTestResultUnitsOfDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultUnitsOfDistance.setStatus("current")
_OtdrTestResultPulseWidth_Type = InfnOtdrTestPulseWidth
_OtdrTestResultPulseWidth_Object = MibTableColumn
otdrTestResultPulseWidth = _OtdrTestResultPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 16),
    _OtdrTestResultPulseWidth_Type()
)
otdrTestResultPulseWidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultPulseWidth.setStatus("current")
_OtdrTestResultDataSpacing_Type = FloatHundredths
_OtdrTestResultDataSpacing_Object = MibTableColumn
otdrTestResultDataSpacing = _OtdrTestResultDataSpacing_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 17),
    _OtdrTestResultDataSpacing_Type()
)
otdrTestResultDataSpacing.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultDataSpacing.setStatus("current")
_OtdrTestResultBackScatterCoefficient_Type = Integer32
_OtdrTestResultBackScatterCoefficient_Object = MibTableColumn
otdrTestResultBackScatterCoefficient = _OtdrTestResultBackScatterCoefficient_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 18),
    _OtdrTestResultBackScatterCoefficient_Type()
)
otdrTestResultBackScatterCoefficient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultBackScatterCoefficient.setStatus("current")
_OtdrTestResultTestAcquisitionTime_Type = Integer32
_OtdrTestResultTestAcquisitionTime_Object = MibTableColumn
otdrTestResultTestAcquisitionTime = _OtdrTestResultTestAcquisitionTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 19),
    _OtdrTestResultTestAcquisitionTime_Type()
)
otdrTestResultTestAcquisitionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultTestAcquisitionTime.setStatus("current")
_OtdrTestResultAcquisitionRange_Type = Integer32
_OtdrTestResultAcquisitionRange_Object = MibTableColumn
otdrTestResultAcquisitionRange = _OtdrTestResultAcquisitionRange_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 20),
    _OtdrTestResultAcquisitionRange_Type()
)
otdrTestResultAcquisitionRange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultAcquisitionRange.setStatus("current")
_OtdrTestResultAcquisitionRangeDistance_Type = Integer32
_OtdrTestResultAcquisitionRangeDistance_Object = MibTableColumn
otdrTestResultAcquisitionRangeDistance = _OtdrTestResultAcquisitionRangeDistance_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 21),
    _OtdrTestResultAcquisitionRangeDistance_Type()
)
otdrTestResultAcquisitionRangeDistance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultAcquisitionRangeDistance.setStatus("current")
_OtdrTestResultEventLossThreshold_Type = FloatHundredths
_OtdrTestResultEventLossThreshold_Object = MibTableColumn
otdrTestResultEventLossThreshold = _OtdrTestResultEventLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 22),
    _OtdrTestResultEventLossThreshold_Type()
)
otdrTestResultEventLossThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultEventLossThreshold.setStatus("current")
_OtdrTestResultReflectanceThreshold_Type = Integer32
_OtdrTestResultReflectanceThreshold_Object = MibTableColumn
otdrTestResultReflectanceThreshold = _OtdrTestResultReflectanceThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 23),
    _OtdrTestResultReflectanceThreshold_Type()
)
otdrTestResultReflectanceThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultReflectanceThreshold.setStatus("current")
_OtdrTestResultEndOfFiberThreshold_Type = Integer32
_OtdrTestResultEndOfFiberThreshold_Object = MibTableColumn
otdrTestResultEndOfFiberThreshold = _OtdrTestResultEndOfFiberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 24),
    _OtdrTestResultEndOfFiberThreshold_Type()
)
otdrTestResultEndOfFiberThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultEndOfFiberThreshold.setStatus("current")
_OtdrTestResultUploadStatus_Type = InfnOtdrFileUploadStatus
_OtdrTestResultUploadStatus_Object = MibTableColumn
otdrTestResultUploadStatus = _OtdrTestResultUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 1, 1, 25),
    _OtdrTestResultUploadStatus_Type()
)
otdrTestResultUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdrTestResultUploadStatus.setStatus("current")
_OtdrTestResultConformance_ObjectIdentity = ObjectIdentity
otdrTestResultConformance = _OtdrTestResultConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 3)
)
_OtdrTestResultCompliances_ObjectIdentity = ObjectIdentity
otdrTestResultCompliances = _OtdrTestResultCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 3, 1)
)
_OtdrTestResultGroups_ObjectIdentity = ObjectIdentity
otdrTestResultGroups = _OtdrTestResultGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 3, 2)
)

# Managed Objects groups

otdrTestResultGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 3, 2, 1)
)
otdrTestResultGroup.setObjects(
      *(("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultTimeStamp"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultOtdmSerialNumber"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultOtdmPortId"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultTestExecutionType"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultAcquisitionMode"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultProvisionedNeighborPtp"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultConnectivityState"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultTestCableID"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultTestFiberID"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultTestFiberType"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultDataPointsCount"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultKeyEventsCount"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultEndToEndLoss"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultOpticalReturnLoss"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultUnitsOfDistance"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultPulseWidth"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultDataSpacing"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultBackScatterCoefficient"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultTestAcquisitionTime"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultAcquisitionRange"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultAcquisitionRangeDistance"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultEventLossThreshold"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultReflectanceThreshold"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultEndOfFiberThreshold"),
        ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultUploadStatus"))
)
if mibBuilder.loadTexts:
    otdrTestResultGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otdrTestResultCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 62, 3, 1, 1)
)
otdrTestResultCompliance.setObjects(
    ("INFINERA-TP-OTDRTESTRESULT-MIB", "otdrTestResultGroup")
)
if mibBuilder.loadTexts:
    otdrTestResultCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OTDRTESTRESULT-MIB",
    **{"otdrTestResultMIB": otdrTestResultMIB,
       "otdrTestResultTable": otdrTestResultTable,
       "otdrTestResultEntry": otdrTestResultEntry,
       "otdrTestResultTimeStamp": otdrTestResultTimeStamp,
       "otdrTestResultOtdmSerialNumber": otdrTestResultOtdmSerialNumber,
       "otdrTestResultOtdmPortId": otdrTestResultOtdmPortId,
       "otdrTestResultTestExecutionType": otdrTestResultTestExecutionType,
       "otdrTestResultAcquisitionMode": otdrTestResultAcquisitionMode,
       "otdrTestResultProvisionedNeighborPtp": otdrTestResultProvisionedNeighborPtp,
       "otdrTestResultConnectivityState": otdrTestResultConnectivityState,
       "otdrTestResultTestCableID": otdrTestResultTestCableID,
       "otdrTestResultTestFiberID": otdrTestResultTestFiberID,
       "otdrTestResultTestFiberType": otdrTestResultTestFiberType,
       "otdrTestResultDataPointsCount": otdrTestResultDataPointsCount,
       "otdrTestResultKeyEventsCount": otdrTestResultKeyEventsCount,
       "otdrTestResultEndToEndLoss": otdrTestResultEndToEndLoss,
       "otdrTestResultOpticalReturnLoss": otdrTestResultOpticalReturnLoss,
       "otdrTestResultUnitsOfDistance": otdrTestResultUnitsOfDistance,
       "otdrTestResultPulseWidth": otdrTestResultPulseWidth,
       "otdrTestResultDataSpacing": otdrTestResultDataSpacing,
       "otdrTestResultBackScatterCoefficient": otdrTestResultBackScatterCoefficient,
       "otdrTestResultTestAcquisitionTime": otdrTestResultTestAcquisitionTime,
       "otdrTestResultAcquisitionRange": otdrTestResultAcquisitionRange,
       "otdrTestResultAcquisitionRangeDistance": otdrTestResultAcquisitionRangeDistance,
       "otdrTestResultEventLossThreshold": otdrTestResultEventLossThreshold,
       "otdrTestResultReflectanceThreshold": otdrTestResultReflectanceThreshold,
       "otdrTestResultEndOfFiberThreshold": otdrTestResultEndOfFiberThreshold,
       "otdrTestResultUploadStatus": otdrTestResultUploadStatus,
       "otdrTestResultConformance": otdrTestResultConformance,
       "otdrTestResultCompliances": otdrTestResultCompliances,
       "otdrTestResultCompliance": otdrTestResultCompliance,
       "otdrTestResultGroups": otdrTestResultGroups,
       "otdrTestResultGroup": otdrTestResultGroup}
)
