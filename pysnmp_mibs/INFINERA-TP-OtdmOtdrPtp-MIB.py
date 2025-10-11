# SNMP MIB module (INFINERA-TP-OtdmOtdrPtp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OtdmOtdrPtp-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:49 2025
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
 InfnFiberType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnFiberType")

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

otdmOtdrPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48)
)
if mibBuilder.loadTexts:
    otdmOtdrPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtdmOtdrPtpTable_Object = MibTable
otdmOtdrPtpTable = _OtdmOtdrPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1)
)
if mibBuilder.loadTexts:
    otdmOtdrPtpTable.setStatus("current")
_OtdmOtdrPtpEntry_Object = MibTableRow
otdmOtdrPtpEntry = _OtdmOtdrPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1)
)
otdmOtdrPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    otdmOtdrPtpEntry.setStatus("current")


class _OtdmOtdrPtpConnectivityState_Type(Integer32):
    """Custom type otdmOtdrPtpConnectivityState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notVerified", 1),
          ("valid", 2),
          ("inValid", 3))
    )


_OtdmOtdrPtpConnectivityState_Type.__name__ = "Integer32"
_OtdmOtdrPtpConnectivityState_Object = MibTableColumn
otdmOtdrPtpConnectivityState = _OtdmOtdrPtpConnectivityState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 1),
    _OtdmOtdrPtpConnectivityState_Type()
)
otdmOtdrPtpConnectivityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdmOtdrPtpConnectivityState.setStatus("current")
_OtdmOtdrPtpLstSuccConnValidationTime_Type = Integer32
_OtdmOtdrPtpLstSuccConnValidationTime_Object = MibTableColumn
otdmOtdrPtpLstSuccConnValidationTime = _OtdmOtdrPtpLstSuccConnValidationTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 2),
    _OtdmOtdrPtpLstSuccConnValidationTime_Type()
)
otdmOtdrPtpLstSuccConnValidationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdmOtdrPtpLstSuccConnValidationTime.setStatus("current")
_OtdmOtdrPtpProvisionedNeighborPtp_Type = DisplayString
_OtdmOtdrPtpProvisionedNeighborPtp_Object = MibTableColumn
otdmOtdrPtpProvisionedNeighborPtp = _OtdmOtdrPtpProvisionedNeighborPtp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 3),
    _OtdmOtdrPtpProvisionedNeighborPtp_Type()
)
otdmOtdrPtpProvisionedNeighborPtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpProvisionedNeighborPtp.setStatus("current")


class _OtdmOtdrPtpTestControlStatus_Type(Integer32):
    """Custom type otdmOtdrPtpTestControlStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("inProgress", 1),
          ("queuedUp", 2),
          ("scheduled", 3),
          ("idle", 4))
    )


_OtdmOtdrPtpTestControlStatus_Type.__name__ = "Integer32"
_OtdmOtdrPtpTestControlStatus_Object = MibTableColumn
otdmOtdrPtpTestControlStatus = _OtdmOtdrPtpTestControlStatus_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 4),
    _OtdmOtdrPtpTestControlStatus_Type()
)
otdmOtdrPtpTestControlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestControlStatus.setStatus("current")


class _OtdmOtdrPtpTestAquistionMode_Type(Integer32):
    """Custom type otdmOtdrPtpTestAquistionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("automatic", 1),
          ("manual", 2))
    )


_OtdmOtdrPtpTestAquistionMode_Type.__name__ = "Integer32"
_OtdmOtdrPtpTestAquistionMode_Object = MibTableColumn
otdmOtdrPtpTestAquistionMode = _OtdmOtdrPtpTestAquistionMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 5),
    _OtdmOtdrPtpTestAquistionMode_Type()
)
otdmOtdrPtpTestAquistionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestAquistionMode.setStatus("current")


class _OtdmOtdrPtpTestPulseWidth_Type(Integer32):
    """Custom type otdmOtdrPtpTestPulseWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("ns5", 1),
          ("ns10", 2),
          ("ns30", 3),
          ("ns100", 4),
          ("ns300", 5),
          ("us1", 6),
          ("us3", 7),
          ("us10", 8),
          ("us20", 9))
    )


_OtdmOtdrPtpTestPulseWidth_Type.__name__ = "Integer32"
_OtdmOtdrPtpTestPulseWidth_Object = MibTableColumn
otdmOtdrPtpTestPulseWidth = _OtdmOtdrPtpTestPulseWidth_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 6),
    _OtdmOtdrPtpTestPulseWidth_Type()
)
otdmOtdrPtpTestPulseWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestPulseWidth.setStatus("current")


class _OtdmOtdrPtpDetectionRange_Type(Integer32):
    """Custom type otdmOtdrPtpDetectionRange based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("km05", 1),
          ("km1", 2),
          ("km2", 3),
          ("km5", 4),
          ("km10", 5),
          ("km20", 6),
          ("km40", 7),
          ("km80", 8),
          ("km160", 9),
          ("km260", 10))
    )


_OtdmOtdrPtpDetectionRange_Type.__name__ = "Integer32"
_OtdmOtdrPtpDetectionRange_Object = MibTableColumn
otdmOtdrPtpDetectionRange = _OtdmOtdrPtpDetectionRange_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 7),
    _OtdmOtdrPtpDetectionRange_Type()
)
otdmOtdrPtpDetectionRange.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpDetectionRange.setStatus("current")


class _OtdmOtdrPtpAcquistionTime_Type(Integer32):
    """Custom type otdmOtdrPtpAcquistionTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10)
        )
    )
    namedValues = NamedValues(
        *(("sec1", 1),
          ("sec5", 2),
          ("sec10", 3),
          ("sec20", 4),
          ("sec30", 5),
          ("sec60", 6),
          ("sec120", 7),
          ("sec180", 8),
          ("sec240", 9),
          ("sec300", 10))
    )


_OtdmOtdrPtpAcquistionTime_Type.__name__ = "Integer32"
_OtdmOtdrPtpAcquistionTime_Object = MibTableColumn
otdmOtdrPtpAcquistionTime = _OtdmOtdrPtpAcquistionTime_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 8),
    _OtdmOtdrPtpAcquistionTime_Type()
)
otdmOtdrPtpAcquistionTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpAcquistionTime.setStatus("current")
_OtdmOtdrPtpTestCableID_Type = DisplayString
_OtdmOtdrPtpTestCableID_Object = MibTableColumn
otdmOtdrPtpTestCableID = _OtdmOtdrPtpTestCableID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 9),
    _OtdmOtdrPtpTestCableID_Type()
)
otdmOtdrPtpTestCableID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestCableID.setStatus("current")
_OtdmOtdrPtpTestFiberID_Type = DisplayString
_OtdmOtdrPtpTestFiberID_Object = MibTableColumn
otdmOtdrPtpTestFiberID = _OtdmOtdrPtpTestFiberID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 10),
    _OtdmOtdrPtpTestFiberID_Type()
)
otdmOtdrPtpTestFiberID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestFiberID.setStatus("current")
_OtdmOtdrPtpTestFiberType_Type = InfnFiberType
_OtdmOtdrPtpTestFiberType_Object = MibTableColumn
otdmOtdrPtpTestFiberType = _OtdmOtdrPtpTestFiberType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 11),
    _OtdmOtdrPtpTestFiberType_Type()
)
otdmOtdrPtpTestFiberType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestFiberType.setStatus("current")
_OtdmOtdrPtpTestEventLossThreshold_Type = FloatHundredths
_OtdmOtdrPtpTestEventLossThreshold_Object = MibTableColumn
otdmOtdrPtpTestEventLossThreshold = _OtdmOtdrPtpTestEventLossThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 12),
    _OtdmOtdrPtpTestEventLossThreshold_Type()
)
otdmOtdrPtpTestEventLossThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestEventLossThreshold.setStatus("current")
_OtdmOtdrPtpTestReflectionThreshold_Type = FloatHundredths
_OtdmOtdrPtpTestReflectionThreshold_Object = MibTableColumn
otdmOtdrPtpTestReflectionThreshold = _OtdmOtdrPtpTestReflectionThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 13),
    _OtdmOtdrPtpTestReflectionThreshold_Type()
)
otdmOtdrPtpTestReflectionThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestReflectionThreshold.setStatus("current")
_OtdmOtdrPtpTestEndOfFiberThreshold_Type = FloatHundredths
_OtdmOtdrPtpTestEndOfFiberThreshold_Object = MibTableColumn
otdmOtdrPtpTestEndOfFiberThreshold = _OtdmOtdrPtpTestEndOfFiberThreshold_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 15),
    _OtdmOtdrPtpTestEndOfFiberThreshold_Type()
)
otdmOtdrPtpTestEndOfFiberThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestEndOfFiberThreshold.setStatus("current")
_OtdmOtdrPtpTestResultFileName_Type = DisplayString
_OtdmOtdrPtpTestResultFileName_Object = MibTableColumn
otdmOtdrPtpTestResultFileName = _OtdmOtdrPtpTestResultFileName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 16),
    _OtdmOtdrPtpTestResultFileName_Type()
)
otdmOtdrPtpTestResultFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestResultFileName.setStatus("current")


class _OtdmOtdrPtpTestResultUpload_Type(Integer32):
    """Custom type otdmOtdrPtpTestResultUpload based on Integer32"""
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


_OtdmOtdrPtpTestResultUpload_Type.__name__ = "Integer32"
_OtdmOtdrPtpTestResultUpload_Object = MibTableColumn
otdmOtdrPtpTestResultUpload = _OtdmOtdrPtpTestResultUpload_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 1, 1, 17),
    _OtdmOtdrPtpTestResultUpload_Type()
)
otdmOtdrPtpTestResultUpload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otdmOtdrPtpTestResultUpload.setStatus("current")
_OtdmOtdrPtpConformance_ObjectIdentity = ObjectIdentity
otdmOtdrPtpConformance = _OtdmOtdrPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 3)
)
_OtdmOtdrPtpCompliances_ObjectIdentity = ObjectIdentity
otdmOtdrPtpCompliances = _OtdmOtdrPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 3, 1)
)
_OtdmOtdrPtpGroups_ObjectIdentity = ObjectIdentity
otdmOtdrPtpGroups = _OtdmOtdrPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 3, 2)
)

# Managed Objects groups

otdmOtdrPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 3, 2, 1)
)
otdmOtdrPtpGroup.setObjects(
      *(("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpConnectivityState"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpLstSuccConnValidationTime"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpProvisionedNeighborPtp"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestControlStatus"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestAquistionMode"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestPulseWidth"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpDetectionRange"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpAcquistionTime"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestCableID"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestFiberID"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestFiberType"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestEventLossThreshold"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestReflectionThreshold"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestEndOfFiberThreshold"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestResultFileName"),
        ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpTestResultUpload"))
)
if mibBuilder.loadTexts:
    otdmOtdrPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otdmOtdrPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 48, 3, 1, 1)
)
otdmOtdrPtpCompliance.setObjects(
    ("INFINERA-TP-OtdmOtdrPtp-MIB", "otdmOtdrPtpGroup")
)
if mibBuilder.loadTexts:
    otdmOtdrPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OtdmOtdrPtp-MIB",
    **{"otdmOtdrPtpMIB": otdmOtdrPtpMIB,
       "otdmOtdrPtpTable": otdmOtdrPtpTable,
       "otdmOtdrPtpEntry": otdmOtdrPtpEntry,
       "otdmOtdrPtpConnectivityState": otdmOtdrPtpConnectivityState,
       "otdmOtdrPtpLstSuccConnValidationTime": otdmOtdrPtpLstSuccConnValidationTime,
       "otdmOtdrPtpProvisionedNeighborPtp": otdmOtdrPtpProvisionedNeighborPtp,
       "otdmOtdrPtpTestControlStatus": otdmOtdrPtpTestControlStatus,
       "otdmOtdrPtpTestAquistionMode": otdmOtdrPtpTestAquistionMode,
       "otdmOtdrPtpTestPulseWidth": otdmOtdrPtpTestPulseWidth,
       "otdmOtdrPtpDetectionRange": otdmOtdrPtpDetectionRange,
       "otdmOtdrPtpAcquistionTime": otdmOtdrPtpAcquistionTime,
       "otdmOtdrPtpTestCableID": otdmOtdrPtpTestCableID,
       "otdmOtdrPtpTestFiberID": otdmOtdrPtpTestFiberID,
       "otdmOtdrPtpTestFiberType": otdmOtdrPtpTestFiberType,
       "otdmOtdrPtpTestEventLossThreshold": otdmOtdrPtpTestEventLossThreshold,
       "otdmOtdrPtpTestReflectionThreshold": otdmOtdrPtpTestReflectionThreshold,
       "otdmOtdrPtpTestEndOfFiberThreshold": otdmOtdrPtpTestEndOfFiberThreshold,
       "otdmOtdrPtpTestResultFileName": otdmOtdrPtpTestResultFileName,
       "otdmOtdrPtpTestResultUpload": otdmOtdrPtpTestResultUpload,
       "otdmOtdrPtpConformance": otdmOtdrPtpConformance,
       "otdmOtdrPtpCompliances": otdmOtdrPtpCompliances,
       "otdmOtdrPtpCompliance": otdmOtdrPtpCompliance,
       "otdmOtdrPtpGroups": otdmOtdrPtpGroups,
       "otdmOtdrPtpGroup": otdmOtdrPtpGroup}
)
