# SNMP MIB module (G6-FILES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/microsens/G6-FILES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:04 2025
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

(g6,) = mibBuilder.importSymbols(
    "MICROSENS-G6-MIB",
    "g6")

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
 enterprises,
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
    "enterprises",
    "iso")

(DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

management = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3)
)
if mibBuilder.loadTexts:
    management.setRevisions(
        ("2018-02-12 16:19",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Files_ObjectIdentity = ObjectIdentity
files = _Files_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72)
)
_AppsTable_Object = MibTable
appsTable = _AppsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1)
)
if mibBuilder.loadTexts:
    appsTable.setStatus("current")
_AppsEntry_Object = MibTableRow
appsEntry = _AppsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1)
)
appsEntry.setIndexNames(
    (0, "G6-FILES-MIB", "appsIndex"),
)
if mibBuilder.loadTexts:
    appsEntry.setStatus("current")


class _AppsIndex_Type(Integer32):
    """Custom type appsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_AppsIndex_Type.__name__ = "Integer32"
_AppsIndex_Object = MibTableColumn
appsIndex = _AppsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 1),
    _AppsIndex_Type()
)
appsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    appsIndex.setStatus("current")
_AppsListInstalledApps_Type = DisplayString
_AppsListInstalledApps_Object = MibTableColumn
appsListInstalledApps = _AppsListInstalledApps_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 2),
    _AppsListInstalledApps_Type()
)
appsListInstalledApps.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appsListInstalledApps.setStatus("current")
_AppsShowNotes_Type = DisplayString
_AppsShowNotes_Object = MibTableColumn
appsShowNotes = _AppsShowNotes_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 3),
    _AppsShowNotes_Type()
)
appsShowNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appsShowNotes.setStatus("current")
_AppsDisplayFiles_Type = DisplayString
_AppsDisplayFiles_Object = MibTableColumn
appsDisplayFiles = _AppsDisplayFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 4),
    _AppsDisplayFiles_Type()
)
appsDisplayFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appsDisplayFiles.setStatus("current")
_AppsDeleteFile_Type = DisplayString
_AppsDeleteFile_Object = MibTableColumn
appsDeleteFile = _AppsDeleteFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 5),
    _AppsDeleteFile_Type()
)
appsDeleteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appsDeleteFile.setStatus("current")
_AppsDownload_Type = DisplayString
_AppsDownload_Object = MibTableColumn
appsDownload = _AppsDownload_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 6),
    _AppsDownload_Type()
)
appsDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appsDownload.setStatus("current")
_AppsListMediaFiles_Type = DisplayString
_AppsListMediaFiles_Object = MibTableColumn
appsListMediaFiles = _AppsListMediaFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 7),
    _AppsListMediaFiles_Type()
)
appsListMediaFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appsListMediaFiles.setStatus("current")
_AppsExportToMedia_Type = DisplayString
_AppsExportToMedia_Object = MibTableColumn
appsExportToMedia = _AppsExportToMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 8),
    _AppsExportToMedia_Type()
)
appsExportToMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appsExportToMedia.setStatus("current")
_AppsImportFromMedia_Type = DisplayString
_AppsImportFromMedia_Object = MibTableColumn
appsImportFromMedia = _AppsImportFromMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 9),
    _AppsImportFromMedia_Type()
)
appsImportFromMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appsImportFromMedia.setStatus("current")
_AppsInstall_Type = DisplayString
_AppsInstall_Object = MibTableColumn
appsInstall = _AppsInstall_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 10),
    _AppsInstall_Type()
)
appsInstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appsInstall.setStatus("current")
_AppsDeinstall_Type = DisplayString
_AppsDeinstall_Object = MibTableColumn
appsDeinstall = _AppsDeinstall_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 1, 1, 11),
    _AppsDeinstall_Type()
)
appsDeinstall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    appsDeinstall.setStatus("current")
_ScriptsTable_Object = MibTable
scriptsTable = _ScriptsTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2)
)
if mibBuilder.loadTexts:
    scriptsTable.setStatus("current")
_ScriptsEntry_Object = MibTableRow
scriptsEntry = _ScriptsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2, 1)
)
scriptsEntry.setIndexNames(
    (0, "G6-FILES-MIB", "scriptsIndex"),
)
if mibBuilder.loadTexts:
    scriptsEntry.setStatus("current")


class _ScriptsIndex_Type(Integer32):
    """Custom type scriptsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ScriptsIndex_Type.__name__ = "Integer32"
_ScriptsIndex_Object = MibTableColumn
scriptsIndex = _ScriptsIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2, 1, 1),
    _ScriptsIndex_Type()
)
scriptsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scriptsIndex.setStatus("current")
_ScriptsListFiles_Type = DisplayString
_ScriptsListFiles_Object = MibTableColumn
scriptsListFiles = _ScriptsListFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2, 1, 2),
    _ScriptsListFiles_Type()
)
scriptsListFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsListFiles.setStatus("current")
_ScriptsShowFile_Type = DisplayString
_ScriptsShowFile_Object = MibTableColumn
scriptsShowFile = _ScriptsShowFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2, 1, 3),
    _ScriptsShowFile_Type()
)
scriptsShowFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsShowFile.setStatus("current")
_ScriptsExecute_Type = DisplayString
_ScriptsExecute_Object = MibTableColumn
scriptsExecute = _ScriptsExecute_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2, 1, 4),
    _ScriptsExecute_Type()
)
scriptsExecute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsExecute.setStatus("current")
_ScriptsDownloadFromServer_Type = DisplayString
_ScriptsDownloadFromServer_Object = MibTableColumn
scriptsDownloadFromServer = _ScriptsDownloadFromServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2, 1, 5),
    _ScriptsDownloadFromServer_Type()
)
scriptsDownloadFromServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsDownloadFromServer.setStatus("current")
_ScriptsUploadToServer_Type = DisplayString
_ScriptsUploadToServer_Object = MibTableColumn
scriptsUploadToServer = _ScriptsUploadToServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2, 1, 6),
    _ScriptsUploadToServer_Type()
)
scriptsUploadToServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsUploadToServer.setStatus("current")
_ScriptsCopyFile_Type = DisplayString
_ScriptsCopyFile_Object = MibTableColumn
scriptsCopyFile = _ScriptsCopyFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2, 1, 7),
    _ScriptsCopyFile_Type()
)
scriptsCopyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsCopyFile.setStatus("current")
_ScriptsDeleteFile_Type = DisplayString
_ScriptsDeleteFile_Object = MibTableColumn
scriptsDeleteFile = _ScriptsDeleteFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2, 1, 8),
    _ScriptsDeleteFile_Type()
)
scriptsDeleteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsDeleteFile.setStatus("current")
_ScriptsTerminate_Type = DisplayString
_ScriptsTerminate_Object = MibTableColumn
scriptsTerminate = _ScriptsTerminate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 2, 1, 9),
    _ScriptsTerminate_Type()
)
scriptsTerminate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptsTerminate.setStatus("current")
_ScriptdataTable_Object = MibTable
scriptdataTable = _ScriptdataTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3)
)
if mibBuilder.loadTexts:
    scriptdataTable.setStatus("current")
_ScriptdataEntry_Object = MibTableRow
scriptdataEntry = _ScriptdataEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1)
)
scriptdataEntry.setIndexNames(
    (0, "G6-FILES-MIB", "scriptdataIndex"),
)
if mibBuilder.loadTexts:
    scriptdataEntry.setStatus("current")


class _ScriptdataIndex_Type(Integer32):
    """Custom type scriptdataIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ScriptdataIndex_Type.__name__ = "Integer32"
_ScriptdataIndex_Object = MibTableColumn
scriptdataIndex = _ScriptdataIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1, 1),
    _ScriptdataIndex_Type()
)
scriptdataIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    scriptdataIndex.setStatus("current")
_ScriptdataListFiles_Type = DisplayString
_ScriptdataListFiles_Object = MibTableColumn
scriptdataListFiles = _ScriptdataListFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1, 2),
    _ScriptdataListFiles_Type()
)
scriptdataListFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptdataListFiles.setStatus("current")
_ScriptdataShowFile_Type = DisplayString
_ScriptdataShowFile_Object = MibTableColumn
scriptdataShowFile = _ScriptdataShowFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1, 3),
    _ScriptdataShowFile_Type()
)
scriptdataShowFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptdataShowFile.setStatus("current")
_ScriptdataDownloadFromServer_Type = DisplayString
_ScriptdataDownloadFromServer_Object = MibTableColumn
scriptdataDownloadFromServer = _ScriptdataDownloadFromServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1, 4),
    _ScriptdataDownloadFromServer_Type()
)
scriptdataDownloadFromServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptdataDownloadFromServer.setStatus("current")
_ScriptdataUploadToServer_Type = DisplayString
_ScriptdataUploadToServer_Object = MibTableColumn
scriptdataUploadToServer = _ScriptdataUploadToServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1, 5),
    _ScriptdataUploadToServer_Type()
)
scriptdataUploadToServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptdataUploadToServer.setStatus("current")
_ScriptdataCopyFile_Type = DisplayString
_ScriptdataCopyFile_Object = MibTableColumn
scriptdataCopyFile = _ScriptdataCopyFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1, 6),
    _ScriptdataCopyFile_Type()
)
scriptdataCopyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptdataCopyFile.setStatus("current")
_ScriptdataDeleteFile_Type = DisplayString
_ScriptdataDeleteFile_Object = MibTableColumn
scriptdataDeleteFile = _ScriptdataDeleteFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1, 7),
    _ScriptdataDeleteFile_Type()
)
scriptdataDeleteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptdataDeleteFile.setStatus("current")
_ScriptdataListMediaFiles_Type = DisplayString
_ScriptdataListMediaFiles_Object = MibTableColumn
scriptdataListMediaFiles = _ScriptdataListMediaFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1, 8),
    _ScriptdataListMediaFiles_Type()
)
scriptdataListMediaFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptdataListMediaFiles.setStatus("current")
_ScriptdataExportToMedia_Type = DisplayString
_ScriptdataExportToMedia_Object = MibTableColumn
scriptdataExportToMedia = _ScriptdataExportToMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1, 9),
    _ScriptdataExportToMedia_Type()
)
scriptdataExportToMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptdataExportToMedia.setStatus("current")
_ScriptdataImportFromMedia_Type = DisplayString
_ScriptdataImportFromMedia_Object = MibTableColumn
scriptdataImportFromMedia = _ScriptdataImportFromMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 3, 1, 10),
    _ScriptdataImportFromMedia_Type()
)
scriptdataImportFromMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    scriptdataImportFromMedia.setStatus("current")
_ConfigurationTable_Object = MibTable
configurationTable = _ConfigurationTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4)
)
if mibBuilder.loadTexts:
    configurationTable.setStatus("current")
_ConfigurationEntry_Object = MibTableRow
configurationEntry = _ConfigurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1)
)
configurationEntry.setIndexNames(
    (0, "G6-FILES-MIB", "configurationIndex"),
)
if mibBuilder.loadTexts:
    configurationEntry.setStatus("current")


class _ConfigurationIndex_Type(Integer32):
    """Custom type configurationIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ConfigurationIndex_Type.__name__ = "Integer32"
_ConfigurationIndex_Object = MibTableColumn
configurationIndex = _ConfigurationIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 1),
    _ConfigurationIndex_Type()
)
configurationIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    configurationIndex.setStatus("current")
_ConfigurationListFolders_Type = DisplayString
_ConfigurationListFolders_Object = MibTableColumn
configurationListFolders = _ConfigurationListFolders_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 2),
    _ConfigurationListFolders_Type()
)
configurationListFolders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationListFolders.setStatus("current")
_ConfigurationBackupToFolder_Type = DisplayString
_ConfigurationBackupToFolder_Object = MibTableColumn
configurationBackupToFolder = _ConfigurationBackupToFolder_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 3),
    _ConfigurationBackupToFolder_Type()
)
configurationBackupToFolder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationBackupToFolder.setStatus("current")
_ConfigurationRestoreFromFolder_Type = DisplayString
_ConfigurationRestoreFromFolder_Object = MibTableColumn
configurationRestoreFromFolder = _ConfigurationRestoreFromFolder_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 4),
    _ConfigurationRestoreFromFolder_Type()
)
configurationRestoreFromFolder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationRestoreFromFolder.setStatus("current")
_ConfigurationCommitConfig_Type = DisplayString
_ConfigurationCommitConfig_Object = MibTableColumn
configurationCommitConfig = _ConfigurationCommitConfig_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 5),
    _ConfigurationCommitConfig_Type()
)
configurationCommitConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationCommitConfig.setStatus("current")
_ConfigurationCompareConfiguration_Type = DisplayString
_ConfigurationCompareConfiguration_Object = MibTableColumn
configurationCompareConfiguration = _ConfigurationCompareConfiguration_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 6),
    _ConfigurationCompareConfiguration_Type()
)
configurationCompareConfiguration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationCompareConfiguration.setStatus("current")
_ConfigurationCopyFolder_Type = DisplayString
_ConfigurationCopyFolder_Object = MibTableColumn
configurationCopyFolder = _ConfigurationCopyFolder_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 7),
    _ConfigurationCopyFolder_Type()
)
configurationCopyFolder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationCopyFolder.setStatus("current")
_ConfigurationDeleteFolder_Type = DisplayString
_ConfigurationDeleteFolder_Object = MibTableColumn
configurationDeleteFolder = _ConfigurationDeleteFolder_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 8),
    _ConfigurationDeleteFolder_Type()
)
configurationDeleteFolder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationDeleteFolder.setStatus("current")
_ConfigurationDownloadFromServer_Type = DisplayString
_ConfigurationDownloadFromServer_Object = MibTableColumn
configurationDownloadFromServer = _ConfigurationDownloadFromServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 9),
    _ConfigurationDownloadFromServer_Type()
)
configurationDownloadFromServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationDownloadFromServer.setStatus("current")
_ConfigurationUploadToServer_Type = DisplayString
_ConfigurationUploadToServer_Object = MibTableColumn
configurationUploadToServer = _ConfigurationUploadToServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 10),
    _ConfigurationUploadToServer_Type()
)
configurationUploadToServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationUploadToServer.setStatus("current")
_ConfigurationListMediaFolders_Type = DisplayString
_ConfigurationListMediaFolders_Object = MibTableColumn
configurationListMediaFolders = _ConfigurationListMediaFolders_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 11),
    _ConfigurationListMediaFolders_Type()
)
configurationListMediaFolders.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationListMediaFolders.setStatus("current")
_ConfigurationExportToMedia_Type = DisplayString
_ConfigurationExportToMedia_Object = MibTableColumn
configurationExportToMedia = _ConfigurationExportToMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 12),
    _ConfigurationExportToMedia_Type()
)
configurationExportToMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationExportToMedia.setStatus("current")
_ConfigurationImportFromMedia_Type = DisplayString
_ConfigurationImportFromMedia_Object = MibTableColumn
configurationImportFromMedia = _ConfigurationImportFromMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 13),
    _ConfigurationImportFromMedia_Type()
)
configurationImportFromMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationImportFromMedia.setStatus("current")
_ConfigurationFactoryDefaultFolder_Type = DisplayString
_ConfigurationFactoryDefaultFolder_Object = MibTableColumn
configurationFactoryDefaultFolder = _ConfigurationFactoryDefaultFolder_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 14),
    _ConfigurationFactoryDefaultFolder_Type()
)
configurationFactoryDefaultFolder.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationFactoryDefaultFolder.setStatus("current")
_ConfigurationForceFactoryDefault_Type = DisplayString
_ConfigurationForceFactoryDefault_Object = MibTableColumn
configurationForceFactoryDefault = _ConfigurationForceFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 4, 1, 15),
    _ConfigurationForceFactoryDefault_Type()
)
configurationForceFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    configurationForceFactoryDefault.setStatus("current")
_FirmwareTable_Object = MibTable
firmwareTable = _FirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5)
)
if mibBuilder.loadTexts:
    firmwareTable.setStatus("current")
_FirmwareEntry_Object = MibTableRow
firmwareEntry = _FirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1)
)
firmwareEntry.setIndexNames(
    (0, "G6-FILES-MIB", "firmwareIndex"),
)
if mibBuilder.loadTexts:
    firmwareEntry.setStatus("current")


class _FirmwareIndex_Type(Integer32):
    """Custom type firmwareIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_FirmwareIndex_Type.__name__ = "Integer32"
_FirmwareIndex_Object = MibTableColumn
firmwareIndex = _FirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 1),
    _FirmwareIndex_Type()
)
firmwareIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    firmwareIndex.setStatus("current")
_FirmwareListInstalledVersions_Type = DisplayString
_FirmwareListInstalledVersions_Object = MibTableColumn
firmwareListInstalledVersions = _FirmwareListInstalledVersions_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 2),
    _FirmwareListInstalledVersions_Type()
)
firmwareListInstalledVersions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareListInstalledVersions.setStatus("current")
_FirmwareDisplayFiles_Type = DisplayString
_FirmwareDisplayFiles_Object = MibTableColumn
firmwareDisplayFiles = _FirmwareDisplayFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 3),
    _FirmwareDisplayFiles_Type()
)
firmwareDisplayFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareDisplayFiles.setStatus("current")
_FirmwareDeleteFile_Type = DisplayString
_FirmwareDeleteFile_Object = MibTableColumn
firmwareDeleteFile = _FirmwareDeleteFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 4),
    _FirmwareDeleteFile_Type()
)
firmwareDeleteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareDeleteFile.setStatus("current")
_FirmwareDownload_Type = DisplayString
_FirmwareDownload_Object = MibTableColumn
firmwareDownload = _FirmwareDownload_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 5),
    _FirmwareDownload_Type()
)
firmwareDownload.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareDownload.setStatus("current")
_FirmwareVerifyUpdateFile_Type = DisplayString
_FirmwareVerifyUpdateFile_Object = MibTableColumn
firmwareVerifyUpdateFile = _FirmwareVerifyUpdateFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 6),
    _FirmwareVerifyUpdateFile_Type()
)
firmwareVerifyUpdateFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareVerifyUpdateFile.setStatus("current")
_FirmwareShowReleaseNotes_Type = DisplayString
_FirmwareShowReleaseNotes_Object = MibTableColumn
firmwareShowReleaseNotes = _FirmwareShowReleaseNotes_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 7),
    _FirmwareShowReleaseNotes_Type()
)
firmwareShowReleaseNotes.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareShowReleaseNotes.setStatus("current")
_FirmwareInstallSoftwareUpdate_Type = DisplayString
_FirmwareInstallSoftwareUpdate_Object = MibTableColumn
firmwareInstallSoftwareUpdate = _FirmwareInstallSoftwareUpdate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 8),
    _FirmwareInstallSoftwareUpdate_Type()
)
firmwareInstallSoftwareUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareInstallSoftwareUpdate.setStatus("current")
_FirmwareListMediaFiles_Type = DisplayString
_FirmwareListMediaFiles_Object = MibTableColumn
firmwareListMediaFiles = _FirmwareListMediaFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 9),
    _FirmwareListMediaFiles_Type()
)
firmwareListMediaFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareListMediaFiles.setStatus("current")
_FirmwareExportToMedia_Type = DisplayString
_FirmwareExportToMedia_Object = MibTableColumn
firmwareExportToMedia = _FirmwareExportToMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 10),
    _FirmwareExportToMedia_Type()
)
firmwareExportToMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareExportToMedia.setStatus("current")
_FirmwareImportFromMedia_Type = DisplayString
_FirmwareImportFromMedia_Object = MibTableColumn
firmwareImportFromMedia = _FirmwareImportFromMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 11),
    _FirmwareImportFromMedia_Type()
)
firmwareImportFromMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareImportFromMedia.setStatus("current")
_FirmwareMirrorSdCard_Type = DisplayString
_FirmwareMirrorSdCard_Object = MibTableColumn
firmwareMirrorSdCard = _FirmwareMirrorSdCard_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 5, 1, 12),
    _FirmwareMirrorSdCard_Type()
)
firmwareMirrorSdCard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    firmwareMirrorSdCard.setStatus("current")
_CertificateTable_Object = MibTable
certificateTable = _CertificateTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6)
)
if mibBuilder.loadTexts:
    certificateTable.setStatus("current")
_CertificateEntry_Object = MibTableRow
certificateEntry = _CertificateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6, 1)
)
certificateEntry.setIndexNames(
    (0, "G6-FILES-MIB", "certificateIndex"),
)
if mibBuilder.loadTexts:
    certificateEntry.setStatus("current")


class _CertificateIndex_Type(Integer32):
    """Custom type certificateIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_CertificateIndex_Type.__name__ = "Integer32"
_CertificateIndex_Object = MibTableColumn
certificateIndex = _CertificateIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6, 1, 1),
    _CertificateIndex_Type()
)
certificateIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    certificateIndex.setStatus("current")
_CertificateListFiles_Type = DisplayString
_CertificateListFiles_Object = MibTableColumn
certificateListFiles = _CertificateListFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6, 1, 2),
    _CertificateListFiles_Type()
)
certificateListFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateListFiles.setStatus("current")
_CertificateDownloadFromServer_Type = DisplayString
_CertificateDownloadFromServer_Object = MibTableColumn
certificateDownloadFromServer = _CertificateDownloadFromServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6, 1, 3),
    _CertificateDownloadFromServer_Type()
)
certificateDownloadFromServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateDownloadFromServer.setStatus("current")
_CertificateUploadToServer_Type = DisplayString
_CertificateUploadToServer_Object = MibTableColumn
certificateUploadToServer = _CertificateUploadToServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6, 1, 4),
    _CertificateUploadToServer_Type()
)
certificateUploadToServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateUploadToServer.setStatus("current")
_CertificateDeleteFile_Type = DisplayString
_CertificateDeleteFile_Object = MibTableColumn
certificateDeleteFile = _CertificateDeleteFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6, 1, 5),
    _CertificateDeleteFile_Type()
)
certificateDeleteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateDeleteFile.setStatus("current")
_CertificateActivateForWeb_Type = DisplayString
_CertificateActivateForWeb_Object = MibTableColumn
certificateActivateForWeb = _CertificateActivateForWeb_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6, 1, 6),
    _CertificateActivateForWeb_Type()
)
certificateActivateForWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateActivateForWeb.setStatus("current")
_CertificateActivateForSupplicant_Type = DisplayString
_CertificateActivateForSupplicant_Object = MibTableColumn
certificateActivateForSupplicant = _CertificateActivateForSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6, 1, 7),
    _CertificateActivateForSupplicant_Type()
)
certificateActivateForSupplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateActivateForSupplicant.setStatus("current")
_CertificateDeactivateForSupplicant_Type = DisplayString
_CertificateDeactivateForSupplicant_Object = MibTableColumn
certificateDeactivateForSupplicant = _CertificateDeactivateForSupplicant_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6, 1, 8),
    _CertificateDeactivateForSupplicant_Type()
)
certificateDeactivateForSupplicant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateDeactivateForSupplicant.setStatus("current")
_CertificateViewActiveCertificates_Type = DisplayString
_CertificateViewActiveCertificates_Object = MibTableColumn
certificateViewActiveCertificates = _CertificateViewActiveCertificates_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 6, 1, 9),
    _CertificateViewActiveCertificates_Type()
)
certificateViewActiveCertificates.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    certificateViewActiveCertificates.setStatus("current")
_LicenseTable_Object = MibTable
licenseTable = _LicenseTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 7)
)
if mibBuilder.loadTexts:
    licenseTable.setStatus("current")
_LicenseEntry_Object = MibTableRow
licenseEntry = _LicenseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 7, 1)
)
licenseEntry.setIndexNames(
    (0, "G6-FILES-MIB", "licenseIndex"),
)
if mibBuilder.loadTexts:
    licenseEntry.setStatus("current")


class _LicenseIndex_Type(Integer32):
    """Custom type licenseIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LicenseIndex_Type.__name__ = "Integer32"
_LicenseIndex_Object = MibTableColumn
licenseIndex = _LicenseIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 7, 1, 1),
    _LicenseIndex_Type()
)
licenseIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    licenseIndex.setStatus("current")
_LicenseListFiles_Type = DisplayString
_LicenseListFiles_Object = MibTableColumn
licenseListFiles = _LicenseListFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 7, 1, 2),
    _LicenseListFiles_Type()
)
licenseListFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseListFiles.setStatus("current")
_LicenseShowFile_Type = DisplayString
_LicenseShowFile_Object = MibTableColumn
licenseShowFile = _LicenseShowFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 7, 1, 3),
    _LicenseShowFile_Type()
)
licenseShowFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseShowFile.setStatus("current")
_LicenseDownloadFromServer_Type = DisplayString
_LicenseDownloadFromServer_Object = MibTableColumn
licenseDownloadFromServer = _LicenseDownloadFromServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 7, 1, 4),
    _LicenseDownloadFromServer_Type()
)
licenseDownloadFromServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseDownloadFromServer.setStatus("current")
_LicenseDeleteFile_Type = DisplayString
_LicenseDeleteFile_Object = MibTableColumn
licenseDeleteFile = _LicenseDeleteFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 7, 1, 5),
    _LicenseDeleteFile_Type()
)
licenseDeleteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseDeleteFile.setStatus("current")
_LicenseActivate_Type = DisplayString
_LicenseActivate_Object = MibTableColumn
licenseActivate = _LicenseActivate_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 7, 1, 6),
    _LicenseActivate_Type()
)
licenseActivate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseActivate.setStatus("current")
_LicenseViewActiveLicenses_Type = DisplayString
_LicenseViewActiveLicenses_Object = MibTableColumn
licenseViewActiveLicenses = _LicenseViewActiveLicenses_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 7, 1, 7),
    _LicenseViewActiveLicenses_Type()
)
licenseViewActiveLicenses.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    licenseViewActiveLicenses.setStatus("current")
_HistoryTable_Object = MibTable
historyTable = _HistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 8)
)
if mibBuilder.loadTexts:
    historyTable.setStatus("current")
_HistoryEntry_Object = MibTableRow
historyEntry = _HistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 8, 1)
)
historyEntry.setIndexNames(
    (0, "G6-FILES-MIB", "historyIndex"),
)
if mibBuilder.loadTexts:
    historyEntry.setStatus("current")


class _HistoryIndex_Type(Integer32):
    """Custom type historyIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_HistoryIndex_Type.__name__ = "Integer32"
_HistoryIndex_Object = MibTableColumn
historyIndex = _HistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 8, 1, 1),
    _HistoryIndex_Type()
)
historyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    historyIndex.setStatus("current")
_HistoryListFiles_Type = DisplayString
_HistoryListFiles_Object = MibTableColumn
historyListFiles = _HistoryListFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 8, 1, 2),
    _HistoryListFiles_Type()
)
historyListFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyListFiles.setStatus("current")
_HistoryShowFile_Type = DisplayString
_HistoryShowFile_Object = MibTableColumn
historyShowFile = _HistoryShowFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 8, 1, 3),
    _HistoryShowFile_Type()
)
historyShowFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyShowFile.setStatus("current")
_HistoryUploadToServer_Type = DisplayString
_HistoryUploadToServer_Object = MibTableColumn
historyUploadToServer = _HistoryUploadToServer_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 8, 1, 4),
    _HistoryUploadToServer_Type()
)
historyUploadToServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyUploadToServer.setStatus("current")
_HistoryCopyFile_Type = DisplayString
_HistoryCopyFile_Object = MibTableColumn
historyCopyFile = _HistoryCopyFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 8, 1, 5),
    _HistoryCopyFile_Type()
)
historyCopyFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyCopyFile.setStatus("current")
_HistoryDeleteFile_Type = DisplayString
_HistoryDeleteFile_Object = MibTableColumn
historyDeleteFile = _HistoryDeleteFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 8, 1, 6),
    _HistoryDeleteFile_Type()
)
historyDeleteFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyDeleteFile.setStatus("current")
_HistoryListMediaFiles_Type = DisplayString
_HistoryListMediaFiles_Object = MibTableColumn
historyListMediaFiles = _HistoryListMediaFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 8, 1, 7),
    _HistoryListMediaFiles_Type()
)
historyListMediaFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyListMediaFiles.setStatus("current")
_HistoryExportToMedia_Type = DisplayString
_HistoryExportToMedia_Object = MibTableColumn
historyExportToMedia = _HistoryExportToMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 8, 1, 8),
    _HistoryExportToMedia_Type()
)
historyExportToMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    historyExportToMedia.setStatus("current")
_LogfilesTable_Object = MibTable
logfilesTable = _LogfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 9)
)
if mibBuilder.loadTexts:
    logfilesTable.setStatus("current")
_LogfilesEntry_Object = MibTableRow
logfilesEntry = _LogfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 9, 1)
)
logfilesEntry.setIndexNames(
    (0, "G6-FILES-MIB", "logfilesIndex"),
)
if mibBuilder.loadTexts:
    logfilesEntry.setStatus("current")


class _LogfilesIndex_Type(Integer32):
    """Custom type logfilesIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_LogfilesIndex_Type.__name__ = "Integer32"
_LogfilesIndex_Object = MibTableColumn
logfilesIndex = _LogfilesIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 9, 1, 1),
    _LogfilesIndex_Type()
)
logfilesIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    logfilesIndex.setStatus("current")
_LogfilesListFiles_Type = DisplayString
_LogfilesListFiles_Object = MibTableColumn
logfilesListFiles = _LogfilesListFiles_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 9, 1, 2),
    _LogfilesListFiles_Type()
)
logfilesListFiles.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logfilesListFiles.setStatus("current")
_LogfilesShowFile_Type = DisplayString
_LogfilesShowFile_Object = MibTableColumn
logfilesShowFile = _LogfilesShowFile_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 9, 1, 3),
    _LogfilesShowFile_Type()
)
logfilesShowFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logfilesShowFile.setStatus("current")
_LogfilesShowLastUpdateLog_Type = DisplayString
_LogfilesShowLastUpdateLog_Object = MibTableColumn
logfilesShowLastUpdateLog = _LogfilesShowLastUpdateLog_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 9, 1, 4),
    _LogfilesShowLastUpdateLog_Type()
)
logfilesShowLastUpdateLog.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logfilesShowLastUpdateLog.setStatus("current")
_LogfilesUploadLastSnapshot_Type = DisplayString
_LogfilesUploadLastSnapshot_Object = MibTableColumn
logfilesUploadLastSnapshot = _LogfilesUploadLastSnapshot_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 9, 1, 5),
    _LogfilesUploadLastSnapshot_Type()
)
logfilesUploadLastSnapshot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logfilesUploadLastSnapshot.setStatus("current")
_LogfilesExportToMedia_Type = DisplayString
_LogfilesExportToMedia_Object = MibTableColumn
logfilesExportToMedia = _LogfilesExportToMedia_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 9, 1, 6),
    _LogfilesExportToMedia_Type()
)
logfilesExportToMedia.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    logfilesExportToMedia.setStatus("current")
_ServerTable_Object = MibTable
serverTable = _ServerTable_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 10)
)
if mibBuilder.loadTexts:
    serverTable.setStatus("current")
_ServerEntry_Object = MibTableRow
serverEntry = _ServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 10, 1)
)
serverEntry.setIndexNames(
    (0, "G6-FILES-MIB", "serverIndex"),
)
if mibBuilder.loadTexts:
    serverEntry.setStatus("current")


class _ServerIndex_Type(Integer32):
    """Custom type serverIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
    )


_ServerIndex_Type.__name__ = "Integer32"
_ServerIndex_Object = MibTableColumn
serverIndex = _ServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 10, 1, 1),
    _ServerIndex_Type()
)
serverIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    serverIndex.setStatus("current")


class _ServerEnableTftp_Type(Integer32):
    """Custom type serverEnableTftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ServerEnableTftp_Type.__name__ = "Integer32"
_ServerEnableTftp_Object = MibTableColumn
serverEnableTftp = _ServerEnableTftp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 10, 1, 2),
    _ServerEnableTftp_Type()
)
serverEnableTftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverEnableTftp.setStatus("current")


class _ServerEnableFtp_Type(Integer32):
    """Custom type serverEnableFtp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ServerEnableFtp_Type.__name__ = "Integer32"
_ServerEnableFtp_Object = MibTableColumn
serverEnableFtp = _ServerEnableFtp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 10, 1, 3),
    _ServerEnableFtp_Type()
)
serverEnableFtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverEnableFtp.setStatus("current")


class _ServerEnableSftp_Type(Integer32):
    """Custom type serverEnableSftp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ServerEnableSftp_Type.__name__ = "Integer32"
_ServerEnableSftp_Object = MibTableColumn
serverEnableSftp = _ServerEnableSftp_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 10, 1, 4),
    _ServerEnableSftp_Type()
)
serverEnableSftp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverEnableSftp.setStatus("current")


class _ServerEnableApi_Type(Integer32):
    """Custom type serverEnableApi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )


_ServerEnableApi_Type.__name__ = "Integer32"
_ServerEnableApi_Object = MibTableColumn
serverEnableApi = _ServerEnableApi_Object(
    (1, 3, 6, 1, 4, 1, 3181, 10, 6, 3, 72, 10, 1, 5),
    _ServerEnableApi_Type()
)
serverEnableApi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serverEnableApi.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "G6-FILES-MIB",
    **{"management": management,
       "files": files,
       "appsTable": appsTable,
       "appsEntry": appsEntry,
       "appsIndex": appsIndex,
       "appsListInstalledApps": appsListInstalledApps,
       "appsShowNotes": appsShowNotes,
       "appsDisplayFiles": appsDisplayFiles,
       "appsDeleteFile": appsDeleteFile,
       "appsDownload": appsDownload,
       "appsListMediaFiles": appsListMediaFiles,
       "appsExportToMedia": appsExportToMedia,
       "appsImportFromMedia": appsImportFromMedia,
       "appsInstall": appsInstall,
       "appsDeinstall": appsDeinstall,
       "scriptsTable": scriptsTable,
       "scriptsEntry": scriptsEntry,
       "scriptsIndex": scriptsIndex,
       "scriptsListFiles": scriptsListFiles,
       "scriptsShowFile": scriptsShowFile,
       "scriptsExecute": scriptsExecute,
       "scriptsDownloadFromServer": scriptsDownloadFromServer,
       "scriptsUploadToServer": scriptsUploadToServer,
       "scriptsCopyFile": scriptsCopyFile,
       "scriptsDeleteFile": scriptsDeleteFile,
       "scriptsTerminate": scriptsTerminate,
       "scriptdataTable": scriptdataTable,
       "scriptdataEntry": scriptdataEntry,
       "scriptdataIndex": scriptdataIndex,
       "scriptdataListFiles": scriptdataListFiles,
       "scriptdataShowFile": scriptdataShowFile,
       "scriptdataDownloadFromServer": scriptdataDownloadFromServer,
       "scriptdataUploadToServer": scriptdataUploadToServer,
       "scriptdataCopyFile": scriptdataCopyFile,
       "scriptdataDeleteFile": scriptdataDeleteFile,
       "scriptdataListMediaFiles": scriptdataListMediaFiles,
       "scriptdataExportToMedia": scriptdataExportToMedia,
       "scriptdataImportFromMedia": scriptdataImportFromMedia,
       "configurationTable": configurationTable,
       "configurationEntry": configurationEntry,
       "configurationIndex": configurationIndex,
       "configurationListFolders": configurationListFolders,
       "configurationBackupToFolder": configurationBackupToFolder,
       "configurationRestoreFromFolder": configurationRestoreFromFolder,
       "configurationCommitConfig": configurationCommitConfig,
       "configurationCompareConfiguration": configurationCompareConfiguration,
       "configurationCopyFolder": configurationCopyFolder,
       "configurationDeleteFolder": configurationDeleteFolder,
       "configurationDownloadFromServer": configurationDownloadFromServer,
       "configurationUploadToServer": configurationUploadToServer,
       "configurationListMediaFolders": configurationListMediaFolders,
       "configurationExportToMedia": configurationExportToMedia,
       "configurationImportFromMedia": configurationImportFromMedia,
       "configurationFactoryDefaultFolder": configurationFactoryDefaultFolder,
       "configurationForceFactoryDefault": configurationForceFactoryDefault,
       "firmwareTable": firmwareTable,
       "firmwareEntry": firmwareEntry,
       "firmwareIndex": firmwareIndex,
       "firmwareListInstalledVersions": firmwareListInstalledVersions,
       "firmwareDisplayFiles": firmwareDisplayFiles,
       "firmwareDeleteFile": firmwareDeleteFile,
       "firmwareDownload": firmwareDownload,
       "firmwareVerifyUpdateFile": firmwareVerifyUpdateFile,
       "firmwareShowReleaseNotes": firmwareShowReleaseNotes,
       "firmwareInstallSoftwareUpdate": firmwareInstallSoftwareUpdate,
       "firmwareListMediaFiles": firmwareListMediaFiles,
       "firmwareExportToMedia": firmwareExportToMedia,
       "firmwareImportFromMedia": firmwareImportFromMedia,
       "firmwareMirrorSdCard": firmwareMirrorSdCard,
       "certificateTable": certificateTable,
       "certificateEntry": certificateEntry,
       "certificateIndex": certificateIndex,
       "certificateListFiles": certificateListFiles,
       "certificateDownloadFromServer": certificateDownloadFromServer,
       "certificateUploadToServer": certificateUploadToServer,
       "certificateDeleteFile": certificateDeleteFile,
       "certificateActivateForWeb": certificateActivateForWeb,
       "certificateActivateForSupplicant": certificateActivateForSupplicant,
       "certificateDeactivateForSupplicant": certificateDeactivateForSupplicant,
       "certificateViewActiveCertificates": certificateViewActiveCertificates,
       "licenseTable": licenseTable,
       "licenseEntry": licenseEntry,
       "licenseIndex": licenseIndex,
       "licenseListFiles": licenseListFiles,
       "licenseShowFile": licenseShowFile,
       "licenseDownloadFromServer": licenseDownloadFromServer,
       "licenseDeleteFile": licenseDeleteFile,
       "licenseActivate": licenseActivate,
       "licenseViewActiveLicenses": licenseViewActiveLicenses,
       "historyTable": historyTable,
       "historyEntry": historyEntry,
       "historyIndex": historyIndex,
       "historyListFiles": historyListFiles,
       "historyShowFile": historyShowFile,
       "historyUploadToServer": historyUploadToServer,
       "historyCopyFile": historyCopyFile,
       "historyDeleteFile": historyDeleteFile,
       "historyListMediaFiles": historyListMediaFiles,
       "historyExportToMedia": historyExportToMedia,
       "logfilesTable": logfilesTable,
       "logfilesEntry": logfilesEntry,
       "logfilesIndex": logfilesIndex,
       "logfilesListFiles": logfilesListFiles,
       "logfilesShowFile": logfilesShowFile,
       "logfilesShowLastUpdateLog": logfilesShowLastUpdateLog,
       "logfilesUploadLastSnapshot": logfilesUploadLastSnapshot,
       "logfilesExportToMedia": logfilesExportToMedia,
       "serverTable": serverTable,
       "serverEntry": serverEntry,
       "serverIndex": serverIndex,
       "serverEnableTftp": serverEnableTftp,
       "serverEnableFtp": serverEnableFtp,
       "serverEnableSftp": serverEnableSftp,
       "serverEnableApi": serverEnableApi}
)
