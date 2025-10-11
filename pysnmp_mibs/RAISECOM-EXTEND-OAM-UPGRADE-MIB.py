# SNMP MIB module (RAISECOM-EXTEND-OAM-UPGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-EXTEND-OAM-UPGRADE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:44 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(DateAndTime,
 EnableVar) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "DateAndTime",
    "EnableVar")


# MODULE-IDENTITY

raisecomRemoteUpgrade = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RaisecomExtendOamUpgradeGroup_ObjectIdentity = ObjectIdentity
raisecomExtendOamUpgradeGroup = _RaisecomExtendOamUpgradeGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1)
)
_RaisecomExtendOamUpgradeMibObjects_ObjectIdentity = ObjectIdentity
raisecomExtendOamUpgradeMibObjects = _RaisecomExtendOamUpgradeMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1)
)


class _RaisecomExtendOamUpgradeNextIndex_Type(Unsigned32):
    """Custom type raisecomExtendOamUpgradeNextIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaisecomExtendOamUpgradeNextIndex_Type.__name__ = "Unsigned32"
_RaisecomExtendOamUpgradeNextIndex_Object = MibScalar
raisecomExtendOamUpgradeNextIndex = _RaisecomExtendOamUpgradeNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 1),
    _RaisecomExtendOamUpgradeNextIndex_Type()
)
raisecomExtendOamUpgradeNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeNextIndex.setStatus("mandatory")
_RaisecomExtendOamUpgradeTable_Object = MibTable
raisecomExtendOamUpgradeTable = _RaisecomExtendOamUpgradeTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 2)
)
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeTable.setStatus("mandatory")
_RaisecomExtendOamUpgradeEntry_Object = MibTableRow
raisecomExtendOamUpgradeEntry = _RaisecomExtendOamUpgradeEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 2, 1)
)
raisecomExtendOamUpgradeEntry.setIndexNames(
    (0, "RAISECOM-EXTEND-OAM-UPGRADE-MIB", "raisecomExtendOamUpgradeIndex"),
)
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeEntry.setStatus("mandatory")


class _RaisecomExtendOamUpgradeIndex_Type(Unsigned32):
    """Custom type raisecomExtendOamUpgradeIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaisecomExtendOamUpgradeIndex_Type.__name__ = "Unsigned32"
_RaisecomExtendOamUpgradeIndex_Object = MibTableColumn
raisecomExtendOamUpgradeIndex = _RaisecomExtendOamUpgradeIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 2, 1, 1),
    _RaisecomExtendOamUpgradeIndex_Type()
)
raisecomExtendOamUpgradeIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeIndex.setStatus("mandatory")


class _RaisecomExtendOamUpgradeType_Type(Integer32):
    """Custom type raisecomExtendOamUpgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("upload", 2))
    )


_RaisecomExtendOamUpgradeType_Type.__name__ = "Integer32"
_RaisecomExtendOamUpgradeType_Object = MibTableColumn
raisecomExtendOamUpgradeType = _RaisecomExtendOamUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 2, 1, 2),
    _RaisecomExtendOamUpgradeType_Type()
)
raisecomExtendOamUpgradeType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeType.setStatus("mandatory")


class _RaisecomExtendOamUpgradeFileType_Type(Integer32):
    """Custom type raisecomExtendOamUpgradeFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("image", 1),
          ("startupconfig", 2),
          ("runningconfig", 3),
          ("others", 4),
          ("bootstrap", 5),
          ("fpga", 6))
    )


_RaisecomExtendOamUpgradeFileType_Type.__name__ = "Integer32"
_RaisecomExtendOamUpgradeFileType_Object = MibTableColumn
raisecomExtendOamUpgradeFileType = _RaisecomExtendOamUpgradeFileType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 2, 1, 3),
    _RaisecomExtendOamUpgradeFileType_Type()
)
raisecomExtendOamUpgradeFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeFileType.setStatus("mandatory")
_RaisecomExtendOamUpgradeFileName_Type = DisplayString
_RaisecomExtendOamUpgradeFileName_Object = MibTableColumn
raisecomExtendOamUpgradeFileName = _RaisecomExtendOamUpgradeFileName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 2, 1, 4),
    _RaisecomExtendOamUpgradeFileName_Type()
)
raisecomExtendOamUpgradeFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeFileName.setStatus("mandatory")


class _RaisecomExtendOamUpgradeNotificationOnComplete_Type(TruthValue):
    """Custom type raisecomExtendOamUpgradeNotificationOnComplete based on TruthValue"""
    defaultValue = 2


_RaisecomExtendOamUpgradeNotificationOnComplete_Type.__name__ = "TruthValue"
_RaisecomExtendOamUpgradeNotificationOnComplete_Object = MibTableColumn
raisecomExtendOamUpgradeNotificationOnComplete = _RaisecomExtendOamUpgradeNotificationOnComplete_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 2, 1, 5),
    _RaisecomExtendOamUpgradeNotificationOnComplete_Type()
)
raisecomExtendOamUpgradeNotificationOnComplete.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeNotificationOnComplete.setStatus("mandatory")


class _RaisecomExtendOamUpgradeState_Type(Integer32):
    """Custom type raisecomExtendOamUpgradeState based on Integer32"""
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
          ("getsource", 2),
          ("writedest", 3),
          ("completed", 4))
    )


_RaisecomExtendOamUpgradeState_Type.__name__ = "Integer32"
_RaisecomExtendOamUpgradeState_Object = MibTableColumn
raisecomExtendOamUpgradeState = _RaisecomExtendOamUpgradeState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 2, 1, 6),
    _RaisecomExtendOamUpgradeState_Type()
)
raisecomExtendOamUpgradeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeState.setStatus("mandatory")


class _RaisecomExtendOamUpgradeDevices_Type(OctetString):
    """Custom type raisecomExtendOamUpgradeDevices based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 255),
    )


_RaisecomExtendOamUpgradeDevices_Type.__name__ = "OctetString"
_RaisecomExtendOamUpgradeDevices_Object = MibTableColumn
raisecomExtendOamUpgradeDevices = _RaisecomExtendOamUpgradeDevices_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 2, 1, 7),
    _RaisecomExtendOamUpgradeDevices_Type()
)
raisecomExtendOamUpgradeDevices.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeDevices.setStatus("mandatory")
_RaisecomExtendOamUpgradeEntryRowStatus_Type = RowStatus
_RaisecomExtendOamUpgradeEntryRowStatus_Object = MibTableColumn
raisecomExtendOamUpgradeEntryRowStatus = _RaisecomExtendOamUpgradeEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 2, 1, 8),
    _RaisecomExtendOamUpgradeEntryRowStatus_Type()
)
raisecomExtendOamUpgradeEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeEntryRowStatus.setStatus("mandatory")
_RaisecomExtendOamUpgradeStatusTable_Object = MibTable
raisecomExtendOamUpgradeStatusTable = _RaisecomExtendOamUpgradeStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 3)
)
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeStatusTable.setStatus("mandatory")
_RaisecomExtendOamUpgradeStatusEntry_Object = MibTableRow
raisecomExtendOamUpgradeStatusEntry = _RaisecomExtendOamUpgradeStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 3, 1)
)
raisecomExtendOamUpgradeStatusEntry.setIndexNames(
    (0, "RAISECOM-EXTEND-OAM-UPGRADE-MIB", "raisecomExtendOamUpgradeStatusIndex"),
    (0, "RAISECOM-EXTEND-OAM-UPGRADE-MIB", "raisecomExtendOamUpgradeStatusDevice"),
)
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeStatusEntry.setStatus("mandatory")


class _RaisecomExtendOamUpgradeStatusIndex_Type(Unsigned32):
    """Custom type raisecomExtendOamUpgradeStatusIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_RaisecomExtendOamUpgradeStatusIndex_Type.__name__ = "Unsigned32"
_RaisecomExtendOamUpgradeStatusIndex_Object = MibTableColumn
raisecomExtendOamUpgradeStatusIndex = _RaisecomExtendOamUpgradeStatusIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 3, 1, 1),
    _RaisecomExtendOamUpgradeStatusIndex_Type()
)
raisecomExtendOamUpgradeStatusIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeStatusIndex.setStatus("mandatory")
_RaisecomExtendOamUpgradeStatusDevice_Type = Integer32
_RaisecomExtendOamUpgradeStatusDevice_Object = MibTableColumn
raisecomExtendOamUpgradeStatusDevice = _RaisecomExtendOamUpgradeStatusDevice_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 3, 1, 2),
    _RaisecomExtendOamUpgradeStatusDevice_Type()
)
raisecomExtendOamUpgradeStatusDevice.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeStatusDevice.setStatus("mandatory")


class _RaisecomExtendOamUpgradeFailCause_Type(Integer32):
    """Custom type raisecomExtendOamUpgradeFailCause based on Integer32"""
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
              10,
              11,
              12,
              13,
              14)
        )
    )
    namedValues = NamedValues(
        *(("noerror", 1),
          ("invalidfilename", 2),
          ("fileopenfail", 3),
          ("filewritefail", 4),
          ("nomem", 5),
          ("filetoolarge", 6),
          ("oamlinkbusy", 7),
          ("oamtimeout", 8),
          ("oamnotconnnected", 9),
          ("remotenotsupport", 10),
          ("unknown", 11),
          ("invalidupgradetype", 12),
          ("invalidfiletype", 13),
          ("filecheckfail", 14))
    )


_RaisecomExtendOamUpgradeFailCause_Type.__name__ = "Integer32"
_RaisecomExtendOamUpgradeFailCause_Object = MibTableColumn
raisecomExtendOamUpgradeFailCause = _RaisecomExtendOamUpgradeFailCause_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 1, 3, 1, 3),
    _RaisecomExtendOamUpgradeFailCause_Type()
)
raisecomExtendOamUpgradeFailCause.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeFailCause.setStatus("mandatory")
_RaisecomExtendOamMibTraps_ObjectIdentity = ObjectIdentity
raisecomExtendOamMibTraps = _RaisecomExtendOamMibTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 2)
)

# Managed Objects groups


# Notification objects

raisecomExtendOamUpgradeCompletion = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 11, 1, 2, 1)
)
raisecomExtendOamUpgradeCompletion.setObjects(
    ("RAISECOM-EXTEND-OAM-UPGRADE-MIB", "raisecomExtendOamUpgradeDevices")
)
if mibBuilder.loadTexts:
    raisecomExtendOamUpgradeCompletion.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-EXTEND-OAM-UPGRADE-MIB",
    **{"raisecomRemoteUpgrade": raisecomRemoteUpgrade,
       "raisecomExtendOamUpgradeGroup": raisecomExtendOamUpgradeGroup,
       "raisecomExtendOamUpgradeMibObjects": raisecomExtendOamUpgradeMibObjects,
       "raisecomExtendOamUpgradeNextIndex": raisecomExtendOamUpgradeNextIndex,
       "raisecomExtendOamUpgradeTable": raisecomExtendOamUpgradeTable,
       "raisecomExtendOamUpgradeEntry": raisecomExtendOamUpgradeEntry,
       "raisecomExtendOamUpgradeIndex": raisecomExtendOamUpgradeIndex,
       "raisecomExtendOamUpgradeType": raisecomExtendOamUpgradeType,
       "raisecomExtendOamUpgradeFileType": raisecomExtendOamUpgradeFileType,
       "raisecomExtendOamUpgradeFileName": raisecomExtendOamUpgradeFileName,
       "raisecomExtendOamUpgradeNotificationOnComplete": raisecomExtendOamUpgradeNotificationOnComplete,
       "raisecomExtendOamUpgradeState": raisecomExtendOamUpgradeState,
       "raisecomExtendOamUpgradeDevices": raisecomExtendOamUpgradeDevices,
       "raisecomExtendOamUpgradeEntryRowStatus": raisecomExtendOamUpgradeEntryRowStatus,
       "raisecomExtendOamUpgradeStatusTable": raisecomExtendOamUpgradeStatusTable,
       "raisecomExtendOamUpgradeStatusEntry": raisecomExtendOamUpgradeStatusEntry,
       "raisecomExtendOamUpgradeStatusIndex": raisecomExtendOamUpgradeStatusIndex,
       "raisecomExtendOamUpgradeStatusDevice": raisecomExtendOamUpgradeStatusDevice,
       "raisecomExtendOamUpgradeFailCause": raisecomExtendOamUpgradeFailCause,
       "raisecomExtendOamMibTraps": raisecomExtendOamMibTraps,
       "raisecomExtendOamUpgradeCompletion": raisecomExtendOamUpgradeCompletion}
)
