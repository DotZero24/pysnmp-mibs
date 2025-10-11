# SNMP MIB module (SIAE-CUSTOM-CONFIGURATION-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siaemic/SIAE-CUSTOM-CONFIGURATION-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:13:04 2025
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

(siaeMib,) = mibBuilder.importSymbols(
    "SIAE-TREE-MIB",
    "siaeMib")

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

(DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

customCfgMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97)
)
if mibBuilder.loadTexts:
    customCfgMib.setRevisions(
        ("2015-07-21 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class CfgFtpTranferStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("none", 0),
          ("inProgress", 1),
          ("completed", 2),
          ("interrupted", 3))
    )



class CfgToolFtpTransferFailureReason(TextualConvention, Bits):
    status = "current"
    namedValues = NamedValues(
        *(("connectFailure", 0),
          ("fileTransferFailure", 1),
          ("fileSavingFailure", 2),
          ("aborted", 3))
    )


class ExecutionStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("notStarted", 1),
          ("running", 2),
          ("completed", 3),
          ("interrupted", 4))
    )



class ScriptType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("constructor", 1),
          ("destructor", 2))
    )



# MIB Managed Objects in the order of their OIDs



class _CustomCfgMibVersion_Type(Integer32):
    """Custom type customCfgMibVersion based on Integer32"""
    defaultValue = 1


_CustomCfgMibVersion_Type.__name__ = "Integer32"
_CustomCfgMibVersion_Object = MibScalar
customCfgMibVersion = _CustomCfgMibVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 1),
    _CustomCfgMibVersion_Type()
)
customCfgMibVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgMibVersion.setStatus("current")
_CustomCfgToolTable_Object = MibTable
customCfgToolTable = _CustomCfgToolTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2)
)
if mibBuilder.loadTexts:
    customCfgToolTable.setStatus("current")
_CustomCfgToolEntry_Object = MibTableRow
customCfgToolEntry = _CustomCfgToolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1)
)
customCfgToolEntry.setIndexNames(
    (0, "SIAE-CUSTOM-CONFIGURATION-MIB", "customCfgToolId"),
)
if mibBuilder.loadTexts:
    customCfgToolEntry.setStatus("current")
_CustomCfgToolId_Type = Integer32
_CustomCfgToolId_Object = MibTableColumn
customCfgToolId = _CustomCfgToolId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 1),
    _CustomCfgToolId_Type()
)
customCfgToolId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    customCfgToolId.setStatus("current")
_CustomCfgToolRowStatus_Type = RowStatus
_CustomCfgToolRowStatus_Object = MibTableColumn
customCfgToolRowStatus = _CustomCfgToolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 2),
    _CustomCfgToolRowStatus_Type()
)
customCfgToolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgToolRowStatus.setStatus("current")


class _CustomCfgToolDescription_Type(DisplayString):
    """Custom type customCfgToolDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CustomCfgToolDescription_Type.__name__ = "DisplayString"
_CustomCfgToolDescription_Object = MibTableColumn
customCfgToolDescription = _CustomCfgToolDescription_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 3),
    _CustomCfgToolDescription_Type()
)
customCfgToolDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgToolDescription.setStatus("current")


class _CustomCfgToolConstructorName_Type(DisplayString):
    """Custom type customCfgToolConstructorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CustomCfgToolConstructorName_Type.__name__ = "DisplayString"
_CustomCfgToolConstructorName_Object = MibTableColumn
customCfgToolConstructorName = _CustomCfgToolConstructorName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 4),
    _CustomCfgToolConstructorName_Type()
)
customCfgToolConstructorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgToolConstructorName.setStatus("current")


class _CustomCfgToolDestructorName_Type(DisplayString):
    """Custom type customCfgToolDestructorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CustomCfgToolDestructorName_Type.__name__ = "DisplayString"
_CustomCfgToolDestructorName_Object = MibTableColumn
customCfgToolDestructorName = _CustomCfgToolDestructorName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 5),
    _CustomCfgToolDestructorName_Type()
)
customCfgToolDestructorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgToolDestructorName.setStatus("current")
_CustomCfgToolFtpServerIpAddress_Type = IpAddress
_CustomCfgToolFtpServerIpAddress_Object = MibTableColumn
customCfgToolFtpServerIpAddress = _CustomCfgToolFtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 6),
    _CustomCfgToolFtpServerIpAddress_Type()
)
customCfgToolFtpServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgToolFtpServerIpAddress.setStatus("current")


class _CustomCfgToolFtpConstructorName_Type(DisplayString):
    """Custom type customCfgToolFtpConstructorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CustomCfgToolFtpConstructorName_Type.__name__ = "DisplayString"
_CustomCfgToolFtpConstructorName_Object = MibTableColumn
customCfgToolFtpConstructorName = _CustomCfgToolFtpConstructorName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 7),
    _CustomCfgToolFtpConstructorName_Type()
)
customCfgToolFtpConstructorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgToolFtpConstructorName.setStatus("current")


class _CustomCfgToolFtpDestructorName_Type(DisplayString):
    """Custom type customCfgToolFtpDestructorName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CustomCfgToolFtpDestructorName_Type.__name__ = "DisplayString"
_CustomCfgToolFtpDestructorName_Object = MibTableColumn
customCfgToolFtpDestructorName = _CustomCfgToolFtpDestructorName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 8),
    _CustomCfgToolFtpDestructorName_Type()
)
customCfgToolFtpDestructorName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgToolFtpDestructorName.setStatus("current")


class _CustomCfgToolUploadActionRequest_Type(Integer32):
    """Custom type customCfgToolUploadActionRequest based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("loadCfg", 1),
          ("loadCfgContructor", 2),
          ("loadCfgDestructor", 3),
          ("removeCfg", 4))
    )


_CustomCfgToolUploadActionRequest_Type.__name__ = "Integer32"
_CustomCfgToolUploadActionRequest_Object = MibTableColumn
customCfgToolUploadActionRequest = _CustomCfgToolUploadActionRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 9),
    _CustomCfgToolUploadActionRequest_Type()
)
customCfgToolUploadActionRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgToolUploadActionRequest.setStatus("current")


class _CustomCfgToolUploadStatus_Type(CfgFtpTranferStatus):
    """Custom type customCfgToolUploadStatus based on CfgFtpTranferStatus"""
    defaultValue = 0


_CustomCfgToolUploadStatus_Type.__name__ = "CfgFtpTranferStatus"
_CustomCfgToolUploadStatus_Object = MibTableColumn
customCfgToolUploadStatus = _CustomCfgToolUploadStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 10),
    _CustomCfgToolUploadStatus_Type()
)
customCfgToolUploadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgToolUploadStatus.setStatus("current")
_CustomCfgToolUploadFailure_Type = CfgToolFtpTransferFailureReason
_CustomCfgToolUploadFailure_Object = MibTableColumn
customCfgToolUploadFailure = _CustomCfgToolUploadFailure_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 2, 1, 11),
    _CustomCfgToolUploadFailure_Type()
)
customCfgToolUploadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgToolUploadFailure.setStatus("current")


class _CustomCfgFlushActionRequest_Type(Integer32):
    """Custom type customCfgFlushActionRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("startRemove", 1))
    )


_CustomCfgFlushActionRequest_Type.__name__ = "Integer32"
_CustomCfgFlushActionRequest_Object = MibScalar
customCfgFlushActionRequest = _CustomCfgFlushActionRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 3),
    _CustomCfgFlushActionRequest_Type()
)
customCfgFlushActionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    customCfgFlushActionRequest.setStatus("current")
_CustomCfgListTable_Object = MibTable
customCfgListTable = _CustomCfgListTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 4)
)
if mibBuilder.loadTexts:
    customCfgListTable.setStatus("current")
_CustomCfgListEntry_Object = MibTableRow
customCfgListEntry = _CustomCfgListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 4, 1)
)
customCfgListEntry.setIndexNames(
    (0, "SIAE-CUSTOM-CONFIGURATION-MIB", "customCfgListId"),
)
if mibBuilder.loadTexts:
    customCfgListEntry.setStatus("current")
_CustomCfgListId_Type = Integer32
_CustomCfgListId_Object = MibTableColumn
customCfgListId = _CustomCfgListId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 4, 1, 1),
    _CustomCfgListId_Type()
)
customCfgListId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    customCfgListId.setStatus("current")
_CustomCfgListRowStatus_Type = RowStatus
_CustomCfgListRowStatus_Object = MibTableColumn
customCfgListRowStatus = _CustomCfgListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 4, 1, 2),
    _CustomCfgListRowStatus_Type()
)
customCfgListRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgListRowStatus.setStatus("current")


class _CustomCfgListName_Type(DisplayString):
    """Custom type customCfgListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CustomCfgListName_Type.__name__ = "DisplayString"
_CustomCfgListName_Object = MibTableColumn
customCfgListName = _CustomCfgListName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 4, 1, 3),
    _CustomCfgListName_Type()
)
customCfgListName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgListName.setStatus("current")


class _CustomCfgListStatus_Type(ExecutionStatus):
    """Custom type customCfgListStatus based on ExecutionStatus"""
    defaultValue = 1


_CustomCfgListStatus_Type.__name__ = "ExecutionStatus"
_CustomCfgListStatus_Object = MibTableColumn
customCfgListStatus = _CustomCfgListStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 4, 1, 4),
    _CustomCfgListStatus_Type()
)
customCfgListStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgListStatus.setStatus("current")


class _CustomCfgListActionRequest_Type(Integer32):
    """Custom type customCfgListActionRequest based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("notActive", 0),
          ("run", 1))
    )


_CustomCfgListActionRequest_Type.__name__ = "Integer32"
_CustomCfgListActionRequest_Object = MibTableColumn
customCfgListActionRequest = _CustomCfgListActionRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 4, 1, 5),
    _CustomCfgListActionRequest_Type()
)
customCfgListActionRequest.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgListActionRequest.setStatus("current")
_CustomCfgExecListTable_Object = MibTable
customCfgExecListTable = _CustomCfgExecListTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 5)
)
if mibBuilder.loadTexts:
    customCfgExecListTable.setStatus("current")
_CustomCfgExecListEntry_Object = MibTableRow
customCfgExecListEntry = _CustomCfgExecListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 5, 1)
)
customCfgExecListEntry.setIndexNames(
    (0, "SIAE-CUSTOM-CONFIGURATION-MIB", "customCfgListId"),
    (0, "SIAE-CUSTOM-CONFIGURATION-MIB", "customCfgExecElementNumber"),
)
if mibBuilder.loadTexts:
    customCfgExecListEntry.setStatus("current")
_CustomCfgExecElementNumber_Type = Integer32
_CustomCfgExecElementNumber_Object = MibTableColumn
customCfgExecElementNumber = _CustomCfgExecElementNumber_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 5, 1, 1),
    _CustomCfgExecElementNumber_Type()
)
customCfgExecElementNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    customCfgExecElementNumber.setStatus("current")
_CustomCfgExecRowStatus_Type = RowStatus
_CustomCfgExecRowStatus_Object = MibTableColumn
customCfgExecRowStatus = _CustomCfgExecRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 5, 1, 2),
    _CustomCfgExecRowStatus_Type()
)
customCfgExecRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgExecRowStatus.setStatus("current")
_CustomCfgExecToolId_Type = Integer32
_CustomCfgExecToolId_Object = MibTableColumn
customCfgExecToolId = _CustomCfgExecToolId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 5, 1, 3),
    _CustomCfgExecToolId_Type()
)
customCfgExecToolId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgExecToolId.setStatus("current")
_CustomCfgExecScriptType_Type = ScriptType
_CustomCfgExecScriptType_Object = MibTableColumn
customCfgExecScriptType = _CustomCfgExecScriptType_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 5, 1, 4),
    _CustomCfgExecScriptType_Type()
)
customCfgExecScriptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgExecScriptType.setStatus("current")


class _CustomCfgExecScriptStatus_Type(ExecutionStatus):
    """Custom type customCfgExecScriptStatus based on ExecutionStatus"""
    defaultValue = 1


_CustomCfgExecScriptStatus_Type.__name__ = "ExecutionStatus"
_CustomCfgExecScriptStatus_Object = MibTableColumn
customCfgExecScriptStatus = _CustomCfgExecScriptStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 5, 1, 5),
    _CustomCfgExecScriptStatus_Type()
)
customCfgExecScriptStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgExecScriptStatus.setStatus("current")
_CustomCfgCurrentExecPointTable_Object = MibTable
customCfgCurrentExecPointTable = _CustomCfgCurrentExecPointTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 6)
)
if mibBuilder.loadTexts:
    customCfgCurrentExecPointTable.setStatus("current")
_CustomCfgExecPointListEntry_Object = MibTableRow
customCfgExecPointListEntry = _CustomCfgExecPointListEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 6, 1)
)
customCfgExecPointListEntry.setIndexNames(
    (0, "SIAE-CUSTOM-CONFIGURATION-MIB", "customCfgExecPointId"),
)
if mibBuilder.loadTexts:
    customCfgExecPointListEntry.setStatus("current")


class _CustomCfgExecPointId_Type(Integer32):
    """Custom type customCfgExecPointId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_CustomCfgExecPointId_Type.__name__ = "Integer32"
_CustomCfgExecPointId_Object = MibTableColumn
customCfgExecPointId = _CustomCfgExecPointId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 6, 1, 1),
    _CustomCfgExecPointId_Type()
)
customCfgExecPointId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    customCfgExecPointId.setStatus("current")
_CustomCfgExecPointListId_Type = Integer32
_CustomCfgExecPointListId_Object = MibTableColumn
customCfgExecPointListId = _CustomCfgExecPointListId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 6, 1, 2),
    _CustomCfgExecPointListId_Type()
)
customCfgExecPointListId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgExecPointListId.setStatus("current")
_CustomCfgExecPointListElementId_Type = Integer32
_CustomCfgExecPointListElementId_Object = MibTableColumn
customCfgExecPointListElementId = _CustomCfgExecPointListElementId_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 6, 1, 3),
    _CustomCfgExecPointListElementId_Type()
)
customCfgExecPointListElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgExecPointListElementId.setStatus("current")


class _CustomCfgExecPointScriptName_Type(DisplayString):
    """Custom type customCfgExecPointScriptName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CustomCfgExecPointScriptName_Type.__name__ = "DisplayString"
_CustomCfgExecPointScriptName_Object = MibTableColumn
customCfgExecPointScriptName = _CustomCfgExecPointScriptName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 6, 1, 4),
    _CustomCfgExecPointScriptName_Type()
)
customCfgExecPointScriptName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgExecPointScriptName.setStatus("current")
_CustomCfgExecPointScriptLine_Type = Integer32
_CustomCfgExecPointScriptLine_Object = MibTableColumn
customCfgExecPointScriptLine = _CustomCfgExecPointScriptLine_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 6, 1, 5),
    _CustomCfgExecPointScriptLine_Type()
)
customCfgExecPointScriptLine.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgExecPointScriptLine.setStatus("current")
_CustomCfgExecPointScriptRows_Type = Integer32
_CustomCfgExecPointScriptRows_Object = MibTableColumn
customCfgExecPointScriptRows = _CustomCfgExecPointScriptRows_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 6, 1, 6),
    _CustomCfgExecPointScriptRows_Type()
)
customCfgExecPointScriptRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgExecPointScriptRows.setStatus("current")
_CustomCfgActualConfigTable_Object = MibTable
customCfgActualConfigTable = _CustomCfgActualConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 7)
)
if mibBuilder.loadTexts:
    customCfgActualConfigTable.setStatus("current")
_CustomCfgActualConfigEntry_Object = MibTableRow
customCfgActualConfigEntry = _CustomCfgActualConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 7, 1)
)
customCfgActualConfigEntry.setIndexNames(
    (0, "SIAE-CUSTOM-CONFIGURATION-MIB", "customCfgActualConfigName"),
)
if mibBuilder.loadTexts:
    customCfgActualConfigEntry.setStatus("current")


class _CustomCfgActualConfigName_Type(DisplayString):
    """Custom type customCfgActualConfigName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_CustomCfgActualConfigName_Type.__name__ = "DisplayString"
_CustomCfgActualConfigName_Object = MibTableColumn
customCfgActualConfigName = _CustomCfgActualConfigName_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 7, 1, 1),
    _CustomCfgActualConfigName_Type()
)
customCfgActualConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgActualConfigName.setStatus("current")
_CustomCfgActualConfigRowStatus_Type = RowStatus
_CustomCfgActualConfigRowStatus_Object = MibTableColumn
customCfgActualConfigRowStatus = _CustomCfgActualConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 7, 1, 2),
    _CustomCfgActualConfigRowStatus_Type()
)
customCfgActualConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgActualConfigRowStatus.setStatus("current")


class _CustomCfgActualConfigDescription_Type(DisplayString):
    """Custom type customCfgActualConfigDescription based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CustomCfgActualConfigDescription_Type.__name__ = "DisplayString"
_CustomCfgActualConfigDescription_Object = MibTableColumn
customCfgActualConfigDescription = _CustomCfgActualConfigDescription_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 7, 1, 3),
    _CustomCfgActualConfigDescription_Type()
)
customCfgActualConfigDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgActualConfigDescription.setStatus("current")


class _CustomCfgActualConfigVersion_Type(DisplayString):
    """Custom type customCfgActualConfigVersion based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(5, 5),
    )


_CustomCfgActualConfigVersion_Type.__name__ = "DisplayString"
_CustomCfgActualConfigVersion_Object = MibTableColumn
customCfgActualConfigVersion = _CustomCfgActualConfigVersion_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 7, 1, 4),
    _CustomCfgActualConfigVersion_Type()
)
customCfgActualConfigVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    customCfgActualConfigVersion.setStatus("current")
_CustomCfgFtpLogTransfer_ObjectIdentity = ObjectIdentity
customCfgFtpLogTransfer = _CustomCfgFtpLogTransfer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 8)
)


class _CustomCfgLogActionRequest_Type(Integer32):
    """Custom type customCfgLogActionRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("deleteScriptExecLog", 1),
          ("readScriptExecLog", 2),
          ("deleteFaileCmdLog", 3),
          ("readFailedCmdLog", 4))
    )


_CustomCfgLogActionRequest_Type.__name__ = "Integer32"
_CustomCfgLogActionRequest_Object = MibScalar
customCfgLogActionRequest = _CustomCfgLogActionRequest_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 8, 1),
    _CustomCfgLogActionRequest_Type()
)
customCfgLogActionRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    customCfgLogActionRequest.setStatus("current")


class _CustomCfgLogFtpFilename_Type(DisplayString):
    """Custom type customCfgLogFtpFilename based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CustomCfgLogFtpFilename_Type.__name__ = "DisplayString"
_CustomCfgLogFtpFilename_Object = MibScalar
customCfgLogFtpFilename = _CustomCfgLogFtpFilename_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 8, 2),
    _CustomCfgLogFtpFilename_Type()
)
customCfgLogFtpFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    customCfgLogFtpFilename.setStatus("current")
_CustomCfgLogServerIpAddress_Type = IpAddress
_CustomCfgLogServerIpAddress_Object = MibScalar
customCfgLogServerIpAddress = _CustomCfgLogServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 8, 3),
    _CustomCfgLogServerIpAddress_Type()
)
customCfgLogServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    customCfgLogServerIpAddress.setStatus("current")


class _CustomCfgLogDownloadStatus_Type(CfgFtpTranferStatus):
    """Custom type customCfgLogDownloadStatus based on CfgFtpTranferStatus"""
    defaultValue = 0


_CustomCfgLogDownloadStatus_Type.__name__ = "CfgFtpTranferStatus"
_CustomCfgLogDownloadStatus_Object = MibScalar
customCfgLogDownloadStatus = _CustomCfgLogDownloadStatus_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 8, 4),
    _CustomCfgLogDownloadStatus_Type()
)
customCfgLogDownloadStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgLogDownloadStatus.setStatus("current")
_CustomCfgLogDownloadFailure_Type = CfgToolFtpTransferFailureReason
_CustomCfgLogDownloadFailure_Object = MibScalar
customCfgLogDownloadFailure = _CustomCfgLogDownloadFailure_Object(
    (1, 3, 6, 1, 4, 1, 3373, 1103, 97, 8, 5),
    _CustomCfgLogDownloadFailure_Type()
)
customCfgLogDownloadFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    customCfgLogDownloadFailure.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SIAE-CUSTOM-CONFIGURATION-MIB",
    **{"CfgFtpTranferStatus": CfgFtpTranferStatus,
       "CfgToolFtpTransferFailureReason": CfgToolFtpTransferFailureReason,
       "ExecutionStatus": ExecutionStatus,
       "ScriptType": ScriptType,
       "customCfgMib": customCfgMib,
       "customCfgMibVersion": customCfgMibVersion,
       "customCfgToolTable": customCfgToolTable,
       "customCfgToolEntry": customCfgToolEntry,
       "customCfgToolId": customCfgToolId,
       "customCfgToolRowStatus": customCfgToolRowStatus,
       "customCfgToolDescription": customCfgToolDescription,
       "customCfgToolConstructorName": customCfgToolConstructorName,
       "customCfgToolDestructorName": customCfgToolDestructorName,
       "customCfgToolFtpServerIpAddress": customCfgToolFtpServerIpAddress,
       "customCfgToolFtpConstructorName": customCfgToolFtpConstructorName,
       "customCfgToolFtpDestructorName": customCfgToolFtpDestructorName,
       "customCfgToolUploadActionRequest": customCfgToolUploadActionRequest,
       "customCfgToolUploadStatus": customCfgToolUploadStatus,
       "customCfgToolUploadFailure": customCfgToolUploadFailure,
       "customCfgFlushActionRequest": customCfgFlushActionRequest,
       "customCfgListTable": customCfgListTable,
       "customCfgListEntry": customCfgListEntry,
       "customCfgListId": customCfgListId,
       "customCfgListRowStatus": customCfgListRowStatus,
       "customCfgListName": customCfgListName,
       "customCfgListStatus": customCfgListStatus,
       "customCfgListActionRequest": customCfgListActionRequest,
       "customCfgExecListTable": customCfgExecListTable,
       "customCfgExecListEntry": customCfgExecListEntry,
       "customCfgExecElementNumber": customCfgExecElementNumber,
       "customCfgExecRowStatus": customCfgExecRowStatus,
       "customCfgExecToolId": customCfgExecToolId,
       "customCfgExecScriptType": customCfgExecScriptType,
       "customCfgExecScriptStatus": customCfgExecScriptStatus,
       "customCfgCurrentExecPointTable": customCfgCurrentExecPointTable,
       "customCfgExecPointListEntry": customCfgExecPointListEntry,
       "customCfgExecPointId": customCfgExecPointId,
       "customCfgExecPointListId": customCfgExecPointListId,
       "customCfgExecPointListElementId": customCfgExecPointListElementId,
       "customCfgExecPointScriptName": customCfgExecPointScriptName,
       "customCfgExecPointScriptLine": customCfgExecPointScriptLine,
       "customCfgExecPointScriptRows": customCfgExecPointScriptRows,
       "customCfgActualConfigTable": customCfgActualConfigTable,
       "customCfgActualConfigEntry": customCfgActualConfigEntry,
       "customCfgActualConfigName": customCfgActualConfigName,
       "customCfgActualConfigRowStatus": customCfgActualConfigRowStatus,
       "customCfgActualConfigDescription": customCfgActualConfigDescription,
       "customCfgActualConfigVersion": customCfgActualConfigVersion,
       "customCfgFtpLogTransfer": customCfgFtpLogTransfer,
       "customCfgLogActionRequest": customCfgLogActionRequest,
       "customCfgLogFtpFilename": customCfgLogFtpFilename,
       "customCfgLogServerIpAddress": customCfgLogServerIpAddress,
       "customCfgLogDownloadStatus": customCfgLogDownloadStatus,
       "customCfgLogDownloadFailure": customCfgLogDownloadFailure}
)
