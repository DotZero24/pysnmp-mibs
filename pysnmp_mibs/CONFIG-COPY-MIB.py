# SNMP MIB module (CONFIG-COPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/CONFIG-COPY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:44 2025
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
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(mgmt,) = mibBuilder.importSymbols(
    "ZXR10-SMI",
    "mgmt")


# MODULE-IDENTITY

configCopyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1)
)
if mibBuilder.loadTexts:
    configCopyMIB.setRevisions(
        ("2007-02-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class ConfigCopyProtocol(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2))
    )



class ConfigCopyState(TextualConvention, Integer32):
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
        *(("waiting", 1),
          ("running", 2),
          ("successful", 3),
          ("failed", 4))
    )



class ConfigCopyFailCause(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("badFileName", 2),
          ("timeout", 3),
          ("noMem", 4),
          ("noConfig", 5),
          ("unsupportedProtocol", 6),
          ("someConfigApplyFailed", 7))
    )



class ConfigFileType(TextualConvention, Integer32):
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
        *(("networkFile", 1),
          ("localFile", 2),
          ("startupConfig", 3),
          ("runningConfig", 4))
    )



# MIB Managed Objects in the order of their OIDs

_ConfigCopyMIBObjects_ObjectIdentity = ObjectIdentity
configCopyMIBObjects = _ConfigCopyMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1)
)
_Copy_ObjectIdentity = ObjectIdentity
copy = _Copy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1)
)
_CopyTable_Object = MibTable
copyTable = _CopyTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    copyTable.setStatus("current")
_CopyEntry_Object = MibTableRow
copyEntry = _CopyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1)
)
copyEntry.setIndexNames(
    (0, "CONFIG-COPY-MIB", "copyIndex"),
)
if mibBuilder.loadTexts:
    copyEntry.setStatus("current")


class _CopyIndex_Type(Unsigned32):
    """Custom type copyIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_CopyIndex_Type.__name__ = "Unsigned32"
_CopyIndex_Object = MibTableColumn
copyIndex = _CopyIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 1),
    _CopyIndex_Type()
)
copyIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    copyIndex.setStatus("current")


class _CopyProtocol_Type(ConfigCopyProtocol):
    """Custom type copyProtocol based on ConfigCopyProtocol"""
    defaultValue = 2


_CopyProtocol_Type.__name__ = "ConfigCopyProtocol"
_CopyProtocol_Object = MibTableColumn
copyProtocol = _CopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 2),
    _CopyProtocol_Type()
)
copyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyProtocol.setStatus("current")
_CopySourceFileType_Type = ConfigFileType
_CopySourceFileType_Object = MibTableColumn
copySourceFileType = _CopySourceFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 3),
    _CopySourceFileType_Type()
)
copySourceFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copySourceFileType.setStatus("current")
_CopyDestFileType_Type = ConfigFileType
_CopyDestFileType_Object = MibTableColumn
copyDestFileType = _CopyDestFileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 4),
    _CopyDestFileType_Type()
)
copyDestFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyDestFileType.setStatus("current")
_CopyServerAddress_Type = IpAddress
_CopyServerAddress_Object = MibTableColumn
copyServerAddress = _CopyServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 5),
    _CopyServerAddress_Type()
)
copyServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyServerAddress.setStatus("current")


class _CopySrcFileName_Type(DisplayString):
    """Custom type copySrcFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CopySrcFileName_Type.__name__ = "DisplayString"
_CopySrcFileName_Object = MibTableColumn
copySrcFileName = _CopySrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 6),
    _CopySrcFileName_Type()
)
copySrcFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copySrcFileName.setStatus("current")


class _CopyDstFileName_Type(DisplayString):
    """Custom type copyDstFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_CopyDstFileName_Type.__name__ = "DisplayString"
_CopyDstFileName_Object = MibTableColumn
copyDstFileName = _CopyDstFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 7),
    _CopyDstFileName_Type()
)
copyDstFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyDstFileName.setStatus("current")


class _CopyUserName_Type(DisplayString):
    """Custom type copyUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CopyUserName_Type.__name__ = "DisplayString"
_CopyUserName_Object = MibTableColumn
copyUserName = _CopyUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 8),
    _CopyUserName_Type()
)
copyUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyUserName.setStatus("current")


class _CopyUserPassword_Type(DisplayString):
    """Custom type copyUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_CopyUserPassword_Type.__name__ = "DisplayString"
_CopyUserPassword_Object = MibTableColumn
copyUserPassword = _CopyUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 9),
    _CopyUserPassword_Type()
)
copyUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyUserPassword.setStatus("current")


class _CopyNotificationOnCompletion_Type(TruthValue):
    """Custom type copyNotificationOnCompletion based on TruthValue"""
    defaultValue = 2


_CopyNotificationOnCompletion_Type.__name__ = "TruthValue"
_CopyNotificationOnCompletion_Object = MibTableColumn
copyNotificationOnCompletion = _CopyNotificationOnCompletion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 10),
    _CopyNotificationOnCompletion_Type()
)
copyNotificationOnCompletion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyNotificationOnCompletion.setStatus("current")
_CopyState_Type = ConfigCopyState
_CopyState_Object = MibTableColumn
copyState = _CopyState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 11),
    _CopyState_Type()
)
copyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyState.setStatus("current")
_CopyTimeStarted_Type = TimeStamp
_CopyTimeStarted_Object = MibTableColumn
copyTimeStarted = _CopyTimeStarted_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 12),
    _CopyTimeStarted_Type()
)
copyTimeStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyTimeStarted.setStatus("current")
_CopyTimeCompleted_Type = TimeStamp
_CopyTimeCompleted_Object = MibTableColumn
copyTimeCompleted = _CopyTimeCompleted_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 13),
    _CopyTimeCompleted_Type()
)
copyTimeCompleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyTimeCompleted.setStatus("current")
_CopyFailCause_Type = ConfigCopyFailCause
_CopyFailCause_Object = MibTableColumn
copyFailCause = _CopyFailCause_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 14),
    _CopyFailCause_Type()
)
copyFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    copyFailCause.setStatus("current")
_CopyEntryRowStatus_Type = RowStatus
_CopyEntryRowStatus_Object = MibTableColumn
copyEntryRowStatus = _CopyEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 1, 1, 1, 1, 15),
    _CopyEntryRowStatus_Type()
)
copyEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    copyEntryRowStatus.setStatus("current")
_ConfigCopyMIBTrapPrefix_ObjectIdentity = ObjectIdentity
configCopyMIBTrapPrefix = _ConfigCopyMIBTrapPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 2)
)
_CopyMIBTraps_ObjectIdentity = ObjectIdentity
copyMIBTraps = _CopyMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 2, 1)
)

# Managed Objects groups


# Notification objects

copyCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 3902, 3, 202, 1, 2, 1, 1)
)
copyCompletion.setObjects(
      *(("CONFIG-COPY-MIB", "copyServerAddress"),
        ("CONFIG-COPY-MIB", "copySrcFileName"),
        ("CONFIG-COPY-MIB", "copyState"),
        ("CONFIG-COPY-MIB", "copyTimeStarted"),
        ("CONFIG-COPY-MIB", "copyTimeCompleted"),
        ("CONFIG-COPY-MIB", "copyFailCause"))
)
if mibBuilder.loadTexts:
    copyCompletion.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CONFIG-COPY-MIB",
    **{"ConfigCopyProtocol": ConfigCopyProtocol,
       "ConfigCopyState": ConfigCopyState,
       "ConfigCopyFailCause": ConfigCopyFailCause,
       "ConfigFileType": ConfigFileType,
       "configCopyMIB": configCopyMIB,
       "configCopyMIBObjects": configCopyMIBObjects,
       "copy": copy,
       "copyTable": copyTable,
       "copyEntry": copyEntry,
       "copyIndex": copyIndex,
       "copyProtocol": copyProtocol,
       "copySourceFileType": copySourceFileType,
       "copyDestFileType": copyDestFileType,
       "copyServerAddress": copyServerAddress,
       "copySrcFileName": copySrcFileName,
       "copyDstFileName": copyDstFileName,
       "copyUserName": copyUserName,
       "copyUserPassword": copyUserPassword,
       "copyNotificationOnCompletion": copyNotificationOnCompletion,
       "copyState": copyState,
       "copyTimeStarted": copyTimeStarted,
       "copyTimeCompleted": copyTimeCompleted,
       "copyFailCause": copyFailCause,
       "copyEntryRowStatus": copyEntryRowStatus,
       "configCopyMIBTrapPrefix": configCopyMIBTrapPrefix,
       "copyMIBTraps": copyMIBTraps,
       "copyCompletion": copyCompletion}
)
