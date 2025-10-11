# SNMP MIB module (ELECTROLINE-DVM-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DVM-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:07:05 2025
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

(dvmPrivate,) = mibBuilder.importSymbols(
    "ELECTROLINE-DVM-ROOT-MIB",
    "dvmPrivate")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _DvmSwMode_Type(Integer32):
    """Custom type dvmSwMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              30)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("testOnly", 1),
          ("cmOnly", 2),
          ("ScanFeatureInDiagnosticMode", 30))
    )


_DvmSwMode_Type.__name__ = "Integer32"
_DvmSwMode_Object = MibScalar
dvmSwMode = _DvmSwMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 1),
    _DvmSwMode_Type()
)
dvmSwMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmSwMode.setStatus("current")
_DvmTest_ObjectIdentity = ObjectIdentity
dvmTest = _DvmTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2)
)
_DvmTestFpga_ObjectIdentity = ObjectIdentity
dvmTestFpga = _DvmTestFpga_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1)
)
_DvmTestFpgaSoftwareControl_ObjectIdentity = ObjectIdentity
dvmTestFpgaSoftwareControl = _DvmTestFpgaSoftwareControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 1)
)
_DvmTestFpgaSwImageNumber_Type = Integer32
_DvmTestFpgaSwImageNumber_Object = MibScalar
dvmTestFpgaSwImageNumber = _DvmTestFpgaSwImageNumber_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 1, 1),
    _DvmTestFpgaSwImageNumber_Type()
)
dvmTestFpgaSwImageNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmTestFpgaSwImageNumber.setStatus("current")
_DvmTestFpgaSwDloadTftpServer_Type = IpAddress
_DvmTestFpgaSwDloadTftpServer_Object = MibScalar
dvmTestFpgaSwDloadTftpServer = _DvmTestFpgaSwDloadTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 1, 2),
    _DvmTestFpgaSwDloadTftpServer_Type()
)
dvmTestFpgaSwDloadTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmTestFpgaSwDloadTftpServer.setStatus("current")
_DvmTestFpgaSwDloadTftpPath_Type = SnmpAdminString
_DvmTestFpgaSwDloadTftpPath_Object = MibScalar
dvmTestFpgaSwDloadTftpPath = _DvmTestFpgaSwDloadTftpPath_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 1, 3),
    _DvmTestFpgaSwDloadTftpPath_Type()
)
dvmTestFpgaSwDloadTftpPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmTestFpgaSwDloadTftpPath.setStatus("current")
_DvmTestFpgaSwDloadNow_Type = TruthValue
_DvmTestFpgaSwDloadNow_Object = MibScalar
dvmTestFpgaSwDloadNow = _DvmTestFpgaSwDloadNow_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 1, 4),
    _DvmTestFpgaSwDloadNow_Type()
)
dvmTestFpgaSwDloadNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmTestFpgaSwDloadNow.setStatus("current")


class _DvmTestFpgaSwDloadStatus_Type(Integer32):
    """Custom type dvmTestFpgaSwDloadStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("success", 1),
          ("inProgress", 2),
          ("other", 3))
    )


_DvmTestFpgaSwDloadStatus_Type.__name__ = "Integer32"
_DvmTestFpgaSwDloadStatus_Object = MibScalar
dvmTestFpgaSwDloadStatus = _DvmTestFpgaSwDloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 1, 5),
    _DvmTestFpgaSwDloadStatus_Type()
)
dvmTestFpgaSwDloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmTestFpgaSwDloadStatus.setStatus("current")
_DvmTestFpgaSwCopyImageFrom_Type = Integer32
_DvmTestFpgaSwCopyImageFrom_Object = MibScalar
dvmTestFpgaSwCopyImageFrom = _DvmTestFpgaSwCopyImageFrom_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 1, 6),
    _DvmTestFpgaSwCopyImageFrom_Type()
)
dvmTestFpgaSwCopyImageFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmTestFpgaSwCopyImageFrom.setStatus("current")


class _DvmTestFpgaSwCopyStatus_Type(Integer32):
    """Custom type dvmTestFpgaSwCopyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("success", 1),
          ("inProgress", 2),
          ("other", 3))
    )


_DvmTestFpgaSwCopyStatus_Type.__name__ = "Integer32"
_DvmTestFpgaSwCopyStatus_Object = MibScalar
dvmTestFpgaSwCopyStatus = _DvmTestFpgaSwCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 1, 7),
    _DvmTestFpgaSwCopyStatus_Type()
)
dvmTestFpgaSwCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmTestFpgaSwCopyStatus.setStatus("current")
_DvmTestFpgaSwSendImageFrom_Type = Integer32
_DvmTestFpgaSwSendImageFrom_Object = MibScalar
dvmTestFpgaSwSendImageFrom = _DvmTestFpgaSwSendImageFrom_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 1, 8),
    _DvmTestFpgaSwSendImageFrom_Type()
)
dvmTestFpgaSwSendImageFrom.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmTestFpgaSwSendImageFrom.setStatus("current")


class _DvmTestFpgaSwSendImageStatus_Type(Integer32):
    """Custom type dvmTestFpgaSwSendImageStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("failure", 0),
          ("success", 1),
          ("inProgress", 2),
          ("other", 3))
    )


_DvmTestFpgaSwSendImageStatus_Type.__name__ = "Integer32"
_DvmTestFpgaSwSendImageStatus_Object = MibScalar
dvmTestFpgaSwSendImageStatus = _DvmTestFpgaSwSendImageStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 1, 9),
    _DvmTestFpgaSwSendImageStatus_Type()
)
dvmTestFpgaSwSendImageStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmTestFpgaSwSendImageStatus.setStatus("current")
_DvmTestFpgaSotwareTable_Object = MibTable
dvmTestFpgaSotwareTable = _DvmTestFpgaSotwareTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2)
)
if mibBuilder.loadTexts:
    dvmTestFpgaSotwareTable.setStatus("current")
_DvmTestFpgaSotwareEntry_Object = MibTableRow
dvmTestFpgaSotwareEntry = _DvmTestFpgaSotwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2, 1)
)
dvmTestFpgaSotwareEntry.setIndexNames(
    (0, "ELECTROLINE-DVM-TEST-MIB", "dvmFpgaSoftwareTableIndex"),
)
if mibBuilder.loadTexts:
    dvmTestFpgaSotwareEntry.setStatus("current")


class _DvmFpgaSoftwareTableIndex_Type(Integer32):
    """Custom type dvmFpgaSoftwareTableIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DvmFpgaSoftwareTableIndex_Type.__name__ = "Integer32"
_DvmFpgaSoftwareTableIndex_Object = MibTableColumn
dvmFpgaSoftwareTableIndex = _DvmFpgaSoftwareTableIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2, 1, 1),
    _DvmFpgaSoftwareTableIndex_Type()
)
dvmFpgaSoftwareTableIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaSoftwareTableIndex.setStatus("current")
_DvmFpgaProcessorId_Type = Unsigned32
_DvmFpgaProcessorId_Object = MibTableColumn
dvmFpgaProcessorId = _DvmFpgaProcessorId_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2, 1, 2),
    _DvmFpgaProcessorId_Type()
)
dvmFpgaProcessorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaProcessorId.setStatus("current")
_DvmFpgaSoftwareMajorRevision_Type = Unsigned32
_DvmFpgaSoftwareMajorRevision_Object = MibTableColumn
dvmFpgaSoftwareMajorRevision = _DvmFpgaSoftwareMajorRevision_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2, 1, 3),
    _DvmFpgaSoftwareMajorRevision_Type()
)
dvmFpgaSoftwareMajorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaSoftwareMajorRevision.setStatus("current")
_DvmFpgaSoftwareMinorRevision_Type = Unsigned32
_DvmFpgaSoftwareMinorRevision_Object = MibTableColumn
dvmFpgaSoftwareMinorRevision = _DvmFpgaSoftwareMinorRevision_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2, 1, 4),
    _DvmFpgaSoftwareMinorRevision_Type()
)
dvmFpgaSoftwareMinorRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaSoftwareMinorRevision.setStatus("current")
_DvmFpgaBuildTime_Type = DateAndTime
_DvmFpgaBuildTime_Object = MibTableColumn
dvmFpgaBuildTime = _DvmFpgaBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2, 1, 5),
    _DvmFpgaBuildTime_Type()
)
dvmFpgaBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaBuildTime.setStatus("current")
_DvmFpgaFileLength_Type = Unsigned32
_DvmFpgaFileLength_Object = MibTableColumn
dvmFpgaFileLength = _DvmFpgaFileLength_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2, 1, 6),
    _DvmFpgaFileLength_Type()
)
dvmFpgaFileLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaFileLength.setStatus("current")
_DvmFpgaFileName_Type = DisplayString
_DvmFpgaFileName_Object = MibTableColumn
dvmFpgaFileName = _DvmFpgaFileName_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2, 1, 7),
    _DvmFpgaFileName_Type()
)
dvmFpgaFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaFileName.setStatus("current")
_DvmFpgaHeaderHCS_Type = Unsigned32
_DvmFpgaHeaderHCS_Object = MibTableColumn
dvmFpgaHeaderHCS = _DvmFpgaHeaderHCS_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2, 1, 8),
    _DvmFpgaHeaderHCS_Type()
)
dvmFpgaHeaderHCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaHeaderHCS.setStatus("current")
_DvmFpgaSoftwareCRC_Type = Unsigned32
_DvmFpgaSoftwareCRC_Object = MibTableColumn
dvmFpgaSoftwareCRC = _DvmFpgaSoftwareCRC_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 2, 1, 9),
    _DvmFpgaSoftwareCRC_Type()
)
dvmFpgaSoftwareCRC.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaSoftwareCRC.setStatus("current")
_DvmTestFpgaIOtest_ObjectIdentity = ObjectIdentity
dvmTestFpgaIOtest = _DvmTestFpgaIOtest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 3)
)
_DvmTestFpgaIoTestRunNow_Type = TruthValue
_DvmTestFpgaIoTestRunNow_Object = MibScalar
dvmTestFpgaIoTestRunNow = _DvmTestFpgaIoTestRunNow_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 3, 1),
    _DvmTestFpgaIoTestRunNow_Type()
)
dvmTestFpgaIoTestRunNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dvmTestFpgaIoTestRunNow.setStatus("current")


class _DvmTestFpgaIoTestStatus_Type(Integer32):
    """Custom type dvmTestFpgaIoTestStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("inProgress", 1),
          ("success", 2),
          ("fail", 3))
    )


_DvmTestFpgaIoTestStatus_Type.__name__ = "Integer32"
_DvmTestFpgaIoTestStatus_Object = MibScalar
dvmTestFpgaIoTestStatus = _DvmTestFpgaIoTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 3, 2),
    _DvmTestFpgaIoTestStatus_Type()
)
dvmTestFpgaIoTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmTestFpgaIoTestStatus.setStatus("current")
_DvmTestFpgaIoTestResultTable_Object = MibTable
dvmTestFpgaIoTestResultTable = _DvmTestFpgaIoTestResultTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 3, 3)
)
if mibBuilder.loadTexts:
    dvmTestFpgaIoTestResultTable.setStatus("current")
_DvmTestFpgaIoTestResultEntry_Object = MibTableRow
dvmTestFpgaIoTestResultEntry = _DvmTestFpgaIoTestResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 3, 3, 1)
)
dvmTestFpgaIoTestResultEntry.setIndexNames(
    (0, "ELECTROLINE-DVM-TEST-MIB", "dvmFpgaIoTestResultIndex"),
)
if mibBuilder.loadTexts:
    dvmTestFpgaIoTestResultEntry.setStatus("current")
_DvmFpgaIoTestResultIndex_Type = Integer32
_DvmFpgaIoTestResultIndex_Object = MibTableColumn
dvmFpgaIoTestResultIndex = _DvmFpgaIoTestResultIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 3, 3, 1, 1),
    _DvmFpgaIoTestResultIndex_Type()
)
dvmFpgaIoTestResultIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaIoTestResultIndex.setStatus("current")
_DvmFpgaIoTestResultInfo_Type = DisplayString
_DvmFpgaIoTestResultInfo_Object = MibTableColumn
dvmFpgaIoTestResultInfo = _DvmFpgaIoTestResultInfo_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 3, 3, 1, 2),
    _DvmFpgaIoTestResultInfo_Type()
)
dvmFpgaIoTestResultInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaIoTestResultInfo.setStatus("current")


class _DvmFpgaIoTestResultStatus_Type(Integer32):
    """Custom type dvmFpgaIoTestResultStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("success", 1),
          ("fail", 2))
    )


_DvmFpgaIoTestResultStatus_Type.__name__ = "Integer32"
_DvmFpgaIoTestResultStatus_Object = MibTableColumn
dvmFpgaIoTestResultStatus = _DvmFpgaIoTestResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 1, 3, 3, 1, 3),
    _DvmFpgaIoTestResultStatus_Type()
)
dvmFpgaIoTestResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmFpgaIoTestResultStatus.setStatus("current")
_Configuration_ObjectIdentity = ObjectIdentity
configuration = _Configuration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 3)
)


class _FormatFlash_Type(Integer32):
    """Custom type formatFlash based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("format", 1)
    )


_FormatFlash_Type.__name__ = "Integer32"
_FormatFlash_Object = MibScalar
formatFlash = _FormatFlash_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 3, 1),
    _FormatFlash_Type()
)
formatFlash.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    formatFlash.setStatus("current")
_MicroControllers_ObjectIdentity = ObjectIdentity
microControllers = _MicroControllers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 4)
)
_RenesassFirmwareVersion_Type = OctetString
_RenesassFirmwareVersion_Object = MibScalar
renesassFirmwareVersion = _RenesassFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 4, 1),
    _RenesassFirmwareVersion_Type()
)
renesassFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    renesassFirmwareVersion.setStatus("current")
_Leds_ObjectIdentity = ObjectIdentity
leds = _Leds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 3, 4, 2, 5)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DVM-TEST-MIB",
    **{"dvmSwMode": dvmSwMode,
       "dvmTest": dvmTest,
       "dvmTestFpga": dvmTestFpga,
       "dvmTestFpgaSoftwareControl": dvmTestFpgaSoftwareControl,
       "dvmTestFpgaSwImageNumber": dvmTestFpgaSwImageNumber,
       "dvmTestFpgaSwDloadTftpServer": dvmTestFpgaSwDloadTftpServer,
       "dvmTestFpgaSwDloadTftpPath": dvmTestFpgaSwDloadTftpPath,
       "dvmTestFpgaSwDloadNow": dvmTestFpgaSwDloadNow,
       "dvmTestFpgaSwDloadStatus": dvmTestFpgaSwDloadStatus,
       "dvmTestFpgaSwCopyImageFrom": dvmTestFpgaSwCopyImageFrom,
       "dvmTestFpgaSwCopyStatus": dvmTestFpgaSwCopyStatus,
       "dvmTestFpgaSwSendImageFrom": dvmTestFpgaSwSendImageFrom,
       "dvmTestFpgaSwSendImageStatus": dvmTestFpgaSwSendImageStatus,
       "dvmTestFpgaSotwareTable": dvmTestFpgaSotwareTable,
       "dvmTestFpgaSotwareEntry": dvmTestFpgaSotwareEntry,
       "dvmFpgaSoftwareTableIndex": dvmFpgaSoftwareTableIndex,
       "dvmFpgaProcessorId": dvmFpgaProcessorId,
       "dvmFpgaSoftwareMajorRevision": dvmFpgaSoftwareMajorRevision,
       "dvmFpgaSoftwareMinorRevision": dvmFpgaSoftwareMinorRevision,
       "dvmFpgaBuildTime": dvmFpgaBuildTime,
       "dvmFpgaFileLength": dvmFpgaFileLength,
       "dvmFpgaFileName": dvmFpgaFileName,
       "dvmFpgaHeaderHCS": dvmFpgaHeaderHCS,
       "dvmFpgaSoftwareCRC": dvmFpgaSoftwareCRC,
       "dvmTestFpgaIOtest": dvmTestFpgaIOtest,
       "dvmTestFpgaIoTestRunNow": dvmTestFpgaIoTestRunNow,
       "dvmTestFpgaIoTestStatus": dvmTestFpgaIoTestStatus,
       "dvmTestFpgaIoTestResultTable": dvmTestFpgaIoTestResultTable,
       "dvmTestFpgaIoTestResultEntry": dvmTestFpgaIoTestResultEntry,
       "dvmFpgaIoTestResultIndex": dvmFpgaIoTestResultIndex,
       "dvmFpgaIoTestResultInfo": dvmFpgaIoTestResultInfo,
       "dvmFpgaIoTestResultStatus": dvmFpgaIoTestResultStatus,
       "configuration": configuration,
       "formatFlash": formatFlash,
       "microControllers": microControllers,
       "renesassFirmwareVersion": renesassFirmwareVersion,
       "leds": leds}
)
