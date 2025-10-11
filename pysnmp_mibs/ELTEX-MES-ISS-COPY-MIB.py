# SNMP MIB module (ELTEX-MES-ISS-COPY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-COPY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:38 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssCopyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15)
)
if mibBuilder.loadTexts:
    eltMesIssCopyMIB.setRevisions(
        ("2019-05-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesCopyLocationType(TextualConvention, Integer32):
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
          ("sftp", 2))
    )



class EltMesBackupUserStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("starting", 1),
          ("stopped", 2))
    )



class EltMesCopyError(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("no-error", 1),
          ("send-failed", 2),
          ("save-failed", 3))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssCopyObjects_ObjectIdentity = ObjectIdentity
eltMesIssCopyObjects = _EltMesIssCopyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1)
)
_EltMesIssCopyBackup_ObjectIdentity = ObjectIdentity
eltMesIssCopyBackup = _EltMesIssCopyBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1)
)
_EltMesIssBackupConfigs_ObjectIdentity = ObjectIdentity
eltMesIssBackupConfigs = _EltMesIssBackupConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1)
)


class _EltMesBackupAutoEnable_Type(TruthValue):
    """Custom type eltMesBackupAutoEnable based on TruthValue"""
    defaultValue = 2


_EltMesBackupAutoEnable_Type.__name__ = "TruthValue"
_EltMesBackupAutoEnable_Object = MibScalar
eltMesBackupAutoEnable = _EltMesBackupAutoEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 1),
    _EltMesBackupAutoEnable_Type()
)
eltMesBackupAutoEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesBackupAutoEnable.setStatus("current")


class _EltMesBackupAutoTimeout_Type(Unsigned32):
    """Custom type eltMesBackupAutoTimeout based on Unsigned32"""
    defaultValue = 720


_EltMesBackupAutoTimeout_Type.__name__ = "Unsigned32"
_EltMesBackupAutoTimeout_Object = MibScalar
eltMesBackupAutoTimeout = _EltMesBackupAutoTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 2),
    _EltMesBackupAutoTimeout_Type()
)
eltMesBackupAutoTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesBackupAutoTimeout.setStatus("current")
_EltMesBackupAutoFilePath_Type = DisplayString
_EltMesBackupAutoFilePath_Object = MibScalar
eltMesBackupAutoFilePath = _EltMesBackupAutoFilePath_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 3),
    _EltMesBackupAutoFilePath_Type()
)
eltMesBackupAutoFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesBackupAutoFilePath.setStatus("current")
_EltMesBackupAutoServerAddress_Type = DisplayString
_EltMesBackupAutoServerAddress_Object = MibScalar
eltMesBackupAutoServerAddress = _EltMesBackupAutoServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 4),
    _EltMesBackupAutoServerAddress_Type()
)
eltMesBackupAutoServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesBackupAutoServerAddress.setStatus("current")


class _EltMesBackupAutoOnWrite_Type(TruthValue):
    """Custom type eltMesBackupAutoOnWrite based on TruthValue"""
    defaultValue = 2


_EltMesBackupAutoOnWrite_Type.__name__ = "TruthValue"
_EltMesBackupAutoOnWrite_Object = MibScalar
eltMesBackupAutoOnWrite = _EltMesBackupAutoOnWrite_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 5),
    _EltMesBackupAutoOnWrite_Type()
)
eltMesBackupAutoOnWrite.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesBackupAutoOnWrite.setStatus("current")


class _EltMesBackupUserStartAction_Type(EltMesBackupUserStatus):
    """Custom type eltMesBackupUserStartAction based on EltMesBackupUserStatus"""
    defaultValue = 2


_EltMesBackupUserStartAction_Type.__name__ = "EltMesBackupUserStatus"
_EltMesBackupUserStartAction_Object = MibScalar
eltMesBackupUserStartAction = _EltMesBackupUserStartAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 6),
    _EltMesBackupUserStartAction_Type()
)
eltMesBackupUserStartAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesBackupUserStartAction.setStatus("current")


class _EltMesBackupHistoryEnable_Type(TruthValue):
    """Custom type eltMesBackupHistoryEnable based on TruthValue"""
    defaultValue = 2


_EltMesBackupHistoryEnable_Type.__name__ = "TruthValue"
_EltMesBackupHistoryEnable_Object = MibScalar
eltMesBackupHistoryEnable = _EltMesBackupHistoryEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 7),
    _EltMesBackupHistoryEnable_Type()
)
eltMesBackupHistoryEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesBackupHistoryEnable.setStatus("current")


class _EltMesBackupClearAction_Type(Integer32):
    """Custom type eltMesBackupClearAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("clearNow", 2))
    )


_EltMesBackupClearAction_Type.__name__ = "Integer32"
_EltMesBackupClearAction_Object = MibScalar
eltMesBackupClearAction = _EltMesBackupClearAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 1, 8),
    _EltMesBackupClearAction_Type()
)
eltMesBackupClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesBackupClearAction.setStatus("current")
_EltMesIssBackupStatistics_ObjectIdentity = ObjectIdentity
eltMesIssBackupStatistics = _EltMesIssBackupStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2)
)
_EltMesBackupHistoryTable_Object = MibTable
eltMesBackupHistoryTable = _EltMesBackupHistoryTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesBackupHistoryTable.setStatus("current")
_EltMesBackupHistoryEntry_Object = MibTableRow
eltMesBackupHistoryEntry = _EltMesBackupHistoryEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1)
)
eltMesBackupHistoryEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-COPY-MIB", "eltMesBackupHistoryIndex"),
)
if mibBuilder.loadTexts:
    eltMesBackupHistoryEntry.setStatus("current")
_EltMesBackupHistoryIndex_Type = Integer32
_EltMesBackupHistoryIndex_Object = MibTableColumn
eltMesBackupHistoryIndex = _EltMesBackupHistoryIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1, 1),
    _EltMesBackupHistoryIndex_Type()
)
eltMesBackupHistoryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesBackupHistoryIndex.setStatus("current")
_EltMesBackupHistoryDateTime_Type = DisplayString
_EltMesBackupHistoryDateTime_Object = MibTableColumn
eltMesBackupHistoryDateTime = _EltMesBackupHistoryDateTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1, 2),
    _EltMesBackupHistoryDateTime_Type()
)
eltMesBackupHistoryDateTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesBackupHistoryDateTime.setStatus("current")
_EltMesBackupHistoryDstLocationType_Type = EltMesCopyLocationType
_EltMesBackupHistoryDstLocationType_Object = MibTableColumn
eltMesBackupHistoryDstLocationType = _EltMesBackupHistoryDstLocationType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1, 3),
    _EltMesBackupHistoryDstLocationType_Type()
)
eltMesBackupHistoryDstLocationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesBackupHistoryDstLocationType.setStatus("current")
_EltMesBackupHistoryServerAddr_Type = DisplayString
_EltMesBackupHistoryServerAddr_Object = MibTableColumn
eltMesBackupHistoryServerAddr = _EltMesBackupHistoryServerAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1, 4),
    _EltMesBackupHistoryServerAddr_Type()
)
eltMesBackupHistoryServerAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesBackupHistoryServerAddr.setStatus("current")
_EltMesBackupHistoryFilePath_Type = DisplayString
_EltMesBackupHistoryFilePath_Object = MibTableColumn
eltMesBackupHistoryFilePath = _EltMesBackupHistoryFilePath_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 1, 2, 1, 1, 5),
    _EltMesBackupHistoryFilePath_Type()
)
eltMesBackupHistoryFilePath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesBackupHistoryFilePath.setStatus("current")
_EltMesIssCopyGlobal_ObjectIdentity = ObjectIdentity
eltMesIssCopyGlobal = _EltMesIssCopyGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 2)
)
_EltMesLastCopyError_Type = EltMesCopyError
_EltMesLastCopyError_Object = MibScalar
eltMesLastCopyError = _EltMesLastCopyError_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 15, 1, 2, 1),
    _EltMesLastCopyError_Type()
)
eltMesLastCopyError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesLastCopyError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-COPY-MIB",
    **{"EltMesCopyLocationType": EltMesCopyLocationType,
       "EltMesBackupUserStatus": EltMesBackupUserStatus,
       "EltMesCopyError": EltMesCopyError,
       "eltMesIssCopyMIB": eltMesIssCopyMIB,
       "eltMesIssCopyObjects": eltMesIssCopyObjects,
       "eltMesIssCopyBackup": eltMesIssCopyBackup,
       "eltMesIssBackupConfigs": eltMesIssBackupConfigs,
       "eltMesBackupAutoEnable": eltMesBackupAutoEnable,
       "eltMesBackupAutoTimeout": eltMesBackupAutoTimeout,
       "eltMesBackupAutoFilePath": eltMesBackupAutoFilePath,
       "eltMesBackupAutoServerAddress": eltMesBackupAutoServerAddress,
       "eltMesBackupAutoOnWrite": eltMesBackupAutoOnWrite,
       "eltMesBackupUserStartAction": eltMesBackupUserStartAction,
       "eltMesBackupHistoryEnable": eltMesBackupHistoryEnable,
       "eltMesBackupClearAction": eltMesBackupClearAction,
       "eltMesIssBackupStatistics": eltMesIssBackupStatistics,
       "eltMesBackupHistoryTable": eltMesBackupHistoryTable,
       "eltMesBackupHistoryEntry": eltMesBackupHistoryEntry,
       "eltMesBackupHistoryIndex": eltMesBackupHistoryIndex,
       "eltMesBackupHistoryDateTime": eltMesBackupHistoryDateTime,
       "eltMesBackupHistoryDstLocationType": eltMesBackupHistoryDstLocationType,
       "eltMesBackupHistoryServerAddr": eltMesBackupHistoryServerAddr,
       "eltMesBackupHistoryFilePath": eltMesBackupHistoryFilePath,
       "eltMesIssCopyGlobal": eltMesIssCopyGlobal,
       "eltMesLastCopyError": eltMesLastCopyError}
)
