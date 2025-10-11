# SNMP MIB module (MX-FILE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-FILE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:34 2025
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

(mediatrixServices,) = mibBuilder.importSymbols(
    "MX-SMI2",
    "mediatrixServices")

(MxActivationState,
 MxAdvancedIpPort,
 MxDigitMap,
 MxEnableState,
 MxIpAddress,
 MxIpHostName,
 MxIpPort,
 MxIpSubnetMask) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxAdvancedIpPort",
    "MxDigitMap",
    "MxEnableState",
    "MxIpAddress",
    "MxIpHostName",
    "MxIpPort",
    "MxIpSubnetMask")

(MxFloat32,
 MxIpAddr,
 MxIpAddrMask,
 MxIpAddrPort,
 MxIpHostNamePort,
 MxUInt64,
 MxUri,
 MxUrl) = mibBuilder.importSymbols(
    "MX-TC2",
    "MxFloat32",
    "MxIpAddr",
    "MxIpAddrMask",
    "MxIpAddrPort",
    "MxIpHostNamePort",
    "MxUInt64",
    "MxUri",
    "MxUrl")

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

fileMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FileMIBObjects_ObjectIdentity = ObjectIdentity
fileMIBObjects = _FileMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1)
)
_FilesTable_Object = MibTable
filesTable = _FilesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 100)
)
if mibBuilder.loadTexts:
    filesTable.setStatus("current")
_FilesEntry_Object = MibTableRow
filesEntry = _FilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 100, 1)
)
filesEntry.setIndexNames(
    (0, "MX-FILE-MIB", "filesIndex"),
)
if mibBuilder.loadTexts:
    filesEntry.setStatus("current")
_FilesIndex_Type = Unsigned32
_FilesIndex_Object = MibTableColumn
filesIndex = _FilesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 100, 1, 101),
    _FilesIndex_Type()
)
filesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesIndex.setStatus("current")


class _FilesFileName_Type(OctetString):
    """Custom type filesFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 510),
    )


_FilesFileName_Type.__name__ = "OctetString"
_FilesFileName_Object = MibTableColumn
filesFileName = _FilesFileName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 100, 1, 201),
    _FilesFileName_Type()
)
filesFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesFileName.setStatus("current")


class _FilesFileDescription_Type(OctetString):
    """Custom type filesFileDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FilesFileDescription_Type.__name__ = "OctetString"
_FilesFileDescription_Object = MibTableColumn
filesFileDescription = _FilesFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 100, 1, 400),
    _FilesFileDescription_Type()
)
filesFileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesFileDescription.setStatus("current")
_FilesFileSize_Type = Unsigned32
_FilesFileSize_Object = MibTableColumn
filesFileSize = _FilesFileSize_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 100, 1, 500),
    _FilesFileSize_Type()
)
filesFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    filesFileSize.setStatus("current")
_VmImagesFilesTable_Object = MibTable
vmImagesFilesTable = _VmImagesFilesTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 150)
)
if mibBuilder.loadTexts:
    vmImagesFilesTable.setStatus("current")
_VmImagesFilesEntry_Object = MibTableRow
vmImagesFilesEntry = _VmImagesFilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 150, 1)
)
vmImagesFilesEntry.setIndexNames(
    (0, "MX-FILE-MIB", "vmImagesFilesIndex"),
)
if mibBuilder.loadTexts:
    vmImagesFilesEntry.setStatus("current")
_VmImagesFilesIndex_Type = Unsigned32
_VmImagesFilesIndex_Object = MibTableColumn
vmImagesFilesIndex = _VmImagesFilesIndex_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 150, 1, 100),
    _VmImagesFilesIndex_Type()
)
vmImagesFilesIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmImagesFilesIndex.setStatus("current")


class _VmImagesFilesFileName_Type(OctetString):
    """Custom type vmImagesFilesFileName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 510),
    )


_VmImagesFilesFileName_Type.__name__ = "OctetString"
_VmImagesFilesFileName_Object = MibTableColumn
vmImagesFilesFileName = _VmImagesFilesFileName_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 150, 1, 200),
    _VmImagesFilesFileName_Type()
)
vmImagesFilesFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmImagesFilesFileName.setStatus("current")


class _VmImagesFilesFileDescription_Type(OctetString):
    """Custom type vmImagesFilesFileDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_VmImagesFilesFileDescription_Type.__name__ = "OctetString"
_VmImagesFilesFileDescription_Object = MibTableColumn
vmImagesFilesFileDescription = _VmImagesFilesFileDescription_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 150, 1, 300),
    _VmImagesFilesFileDescription_Type()
)
vmImagesFilesFileDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmImagesFilesFileDescription.setStatus("current")
_VmImagesFilesFileSize_Type = Unsigned32
_VmImagesFilesFileSize_Object = MibTableColumn
vmImagesFilesFileSize = _VmImagesFilesFileSize_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 150, 1, 400),
    _VmImagesFilesFileSize_Type()
)
vmImagesFilesFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmImagesFilesFileSize.setStatus("current")
_FileSystemQuotaSize_Type = Unsigned32
_FileSystemQuotaSize_Object = MibScalar
fileSystemQuotaSize = _FileSystemQuotaSize_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 200),
    _FileSystemQuotaSize_Type()
)
fileSystemQuotaSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemQuotaSize.setStatus("current")
_FileSystemAvailableSize_Type = Unsigned32
_FileSystemAvailableSize_Object = MibScalar
fileSystemAvailableSize = _FileSystemAvailableSize_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 250),
    _FileSystemAvailableSize_Type()
)
fileSystemAvailableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileSystemAvailableSize.setStatus("current")
_VmImagesAvailableSize_Type = Unsigned32
_VmImagesAvailableSize_Object = MibScalar
vmImagesAvailableSize = _VmImagesAvailableSize_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 280),
    _VmImagesAvailableSize_Type()
)
vmImagesAvailableSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vmImagesAvailableSize.setStatus("current")
_TransferGroup_ObjectIdentity = ObjectIdentity
transferGroup = _TransferGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 500)
)


class _TransferHttpsCipherSuite_Type(Integer32):
    """Custom type transferHttpsCipherSuite based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300)
        )
    )
    namedValues = NamedValues(
        *(("cS1", 100),
          ("cS2", 200),
          ("cS3", 300))
    )


_TransferHttpsCipherSuite_Type.__name__ = "Integer32"
_TransferHttpsCipherSuite_Object = MibScalar
transferHttpsCipherSuite = _TransferHttpsCipherSuite_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 500, 100),
    _TransferHttpsCipherSuite_Type()
)
transferHttpsCipherSuite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferHttpsCipherSuite.setStatus("current")


class _TransferHttpsTlsVersion_Type(Integer32):
    """Custom type transferHttpsTlsVersion based on Integer32"""
    defaultValue = 200

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("sSLv3", 100),
          ("tLSv1", 200),
          ("tLSv1-1", 300),
          ("tLSv1-2", 400))
    )


_TransferHttpsTlsVersion_Type.__name__ = "Integer32"
_TransferHttpsTlsVersion_Object = MibScalar
transferHttpsTlsVersion = _TransferHttpsTlsVersion_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 500, 200),
    _TransferHttpsTlsVersion_Type()
)
transferHttpsTlsVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    transferHttpsTlsVersion.setStatus("current")
_Statistics_ObjectIdentity = ObjectIdentity
statistics = _Statistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 600)
)


class _StatLastDownloadFileResult_Type(Integer32):
    """Custom type statLastDownloadFileResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("downloading", 200),
          ("success", 300),
          ("failed", 400))
    )


_StatLastDownloadFileResult_Type.__name__ = "Integer32"
_StatLastDownloadFileResult_Object = MibScalar
statLastDownloadFileResult = _StatLastDownloadFileResult_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 600, 100),
    _StatLastDownloadFileResult_Type()
)
statLastDownloadFileResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statLastDownloadFileResult.setStatus("current")


class _StatLastUploadFileResult_Type(Integer32):
    """Custom type statLastUploadFileResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(100,
              200,
              300,
              400)
        )
    )
    namedValues = NamedValues(
        *(("none", 100),
          ("uploading", 200),
          ("success", 300),
          ("failed", 400))
    )


_StatLastUploadFileResult_Type.__name__ = "Integer32"
_StatLastUploadFileResult_Object = MibScalar
statLastUploadFileResult = _StatLastUploadFileResult_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 600, 200),
    _StatLastUploadFileResult_Type()
)
statLastUploadFileResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    statLastUploadFileResult.setStatus("current")
_NotificationsGroup_ObjectIdentity = ObjectIdentity
notificationsGroup = _NotificationsGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 60010)
)


class _MinSeverity_Type(Integer32):
    """Custom type minSeverity based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100,
              200,
              300,
              400,
              500)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("debug", 100),
          ("info", 200),
          ("warning", 300),
          ("error", 400),
          ("critical", 500))
    )


_MinSeverity_Type.__name__ = "Integer32"
_MinSeverity_Object = MibScalar
minSeverity = _MinSeverity_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 60010, 100),
    _MinSeverity_Type()
)
minSeverity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    minSeverity.setStatus("current")
_ConfigurationGroup_ObjectIdentity = ObjectIdentity
configurationGroup = _ConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 60020)
)


class _NeedRestartInfo_Type(Integer32):
    """Custom type needRestartInfo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              100)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 100))
    )


_NeedRestartInfo_Type.__name__ = "Integer32"
_NeedRestartInfo_Object = MibScalar
needRestartInfo = _NeedRestartInfo_Object(
    (1, 3, 6, 1, 4, 1, 4935, 1000, 100, 200, 100, 2600, 1, 60020, 100),
    _NeedRestartInfo_Type()
)
needRestartInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    needRestartInfo.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-FILE-MIB",
    **{"fileMIB": fileMIB,
       "fileMIBObjects": fileMIBObjects,
       "filesTable": filesTable,
       "filesEntry": filesEntry,
       "filesIndex": filesIndex,
       "filesFileName": filesFileName,
       "filesFileDescription": filesFileDescription,
       "filesFileSize": filesFileSize,
       "vmImagesFilesTable": vmImagesFilesTable,
       "vmImagesFilesEntry": vmImagesFilesEntry,
       "vmImagesFilesIndex": vmImagesFilesIndex,
       "vmImagesFilesFileName": vmImagesFilesFileName,
       "vmImagesFilesFileDescription": vmImagesFilesFileDescription,
       "vmImagesFilesFileSize": vmImagesFilesFileSize,
       "fileSystemQuotaSize": fileSystemQuotaSize,
       "fileSystemAvailableSize": fileSystemAvailableSize,
       "vmImagesAvailableSize": vmImagesAvailableSize,
       "transferGroup": transferGroup,
       "transferHttpsCipherSuite": transferHttpsCipherSuite,
       "transferHttpsTlsVersion": transferHttpsTlsVersion,
       "statistics": statistics,
       "statLastDownloadFileResult": statLastDownloadFileResult,
       "statLastUploadFileResult": statLastUploadFileResult,
       "notificationsGroup": notificationsGroup,
       "minSeverity": minSeverity,
       "configurationGroup": configurationGroup,
       "needRestartInfo": needRestartInfo}
)
