# SNMP MIB module (ARICENT-ISSU-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-ISSU-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:34 2025
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
 PhysAddress,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

fsIssu = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103)
)
if mibBuilder.loadTexts:
    fsIssu.setRevisions(
        ("2015-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsIssuSystem_ObjectIdentity = ObjectIdentity
fsIssuSystem = _FsIssuSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1)
)
_FsIssuMaintenanceMode_Type = TruthValue
_FsIssuMaintenanceMode_Object = MibScalar
fsIssuMaintenanceMode = _FsIssuMaintenanceMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 1),
    _FsIssuMaintenanceMode_Type()
)
fsIssuMaintenanceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIssuMaintenanceMode.setStatus("current")
_FsIssuMaintenanceOperStatus_Type = TruthValue
_FsIssuMaintenanceOperStatus_Object = MibScalar
fsIssuMaintenanceOperStatus = _FsIssuMaintenanceOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 2),
    _FsIssuMaintenanceOperStatus_Type()
)
fsIssuMaintenanceOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIssuMaintenanceOperStatus.setStatus("current")


class _FsIssuLoadSWPath_Type(DisplayString):
    """Custom type fsIssuLoadSWPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsIssuLoadSWPath_Type.__name__ = "DisplayString"
_FsIssuLoadSWPath_Object = MibScalar
fsIssuLoadSWPath = _FsIssuLoadSWPath_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 3),
    _FsIssuLoadSWPath_Type()
)
fsIssuLoadSWPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIssuLoadSWPath.setStatus("current")


class _FsIssuRollbackSWPath_Type(DisplayString):
    """Custom type fsIssuRollbackSWPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsIssuRollbackSWPath_Type.__name__ = "DisplayString"
_FsIssuRollbackSWPath_Object = MibScalar
fsIssuRollbackSWPath = _FsIssuRollbackSWPath_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 4),
    _FsIssuRollbackSWPath_Type()
)
fsIssuRollbackSWPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIssuRollbackSWPath.setStatus("current")


class _FsIssuCurrentSWPath_Type(DisplayString):
    """Custom type fsIssuCurrentSWPath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsIssuCurrentSWPath_Type.__name__ = "DisplayString"
_FsIssuCurrentSWPath_Object = MibScalar
fsIssuCurrentSWPath = _FsIssuCurrentSWPath_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 5),
    _FsIssuCurrentSWPath_Type()
)
fsIssuCurrentSWPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIssuCurrentSWPath.setStatus("current")


class _FsIssuSoftwareCompatFilePath_Type(DisplayString):
    """Custom type fsIssuSoftwareCompatFilePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsIssuSoftwareCompatFilePath_Type.__name__ = "DisplayString"
_FsIssuSoftwareCompatFilePath_Object = MibScalar
fsIssuSoftwareCompatFilePath = _FsIssuSoftwareCompatFilePath_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 6),
    _FsIssuSoftwareCompatFilePath_Type()
)
fsIssuSoftwareCompatFilePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIssuSoftwareCompatFilePath.setStatus("current")


class _FsIssuSoftwareCompatCheckInit_Type(TruthValue):
    """Custom type fsIssuSoftwareCompatCheckInit based on TruthValue"""
    defaultValue = 2


_FsIssuSoftwareCompatCheckInit_Type.__name__ = "TruthValue"
_FsIssuSoftwareCompatCheckInit_Object = MibScalar
fsIssuSoftwareCompatCheckInit = _FsIssuSoftwareCompatCheckInit_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 7),
    _FsIssuSoftwareCompatCheckInit_Type()
)
fsIssuSoftwareCompatCheckInit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIssuSoftwareCompatCheckInit.setStatus("current")


class _FsIssuSoftwareCompatCheckStatus_Type(Integer32):
    """Custom type fsIssuSoftwareCompatCheckStatus based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("notinitiated", 0),
          ("fullcompatible", 1),
          ("basecompatible", 2),
          ("incompatible", 3),
          ("checkinprogress", 4),
          ("failed", 5))
    )


_FsIssuSoftwareCompatCheckStatus_Type.__name__ = "Integer32"
_FsIssuSoftwareCompatCheckStatus_Object = MibScalar
fsIssuSoftwareCompatCheckStatus = _FsIssuSoftwareCompatCheckStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 8),
    _FsIssuSoftwareCompatCheckStatus_Type()
)
fsIssuSoftwareCompatCheckStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIssuSoftwareCompatCheckStatus.setStatus("current")


class _FsIssuMode_Type(Integer32):
    """Custom type fsIssuMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fullcompatible", 1),
          ("basecompatible", 2),
          ("incompatible", 3))
    )


_FsIssuMode_Type.__name__ = "Integer32"
_FsIssuMode_Object = MibScalar
fsIssuMode = _FsIssuMode_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 9),
    _FsIssuMode_Type()
)
fsIssuMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIssuMode.setStatus("current")


class _FsIssuCommand_Type(Integer32):
    """Custom type fsIssuCommand based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("loadversion", 1),
          ("forcestandby", 2))
    )


_FsIssuCommand_Type.__name__ = "Integer32"
_FsIssuCommand_Object = MibScalar
fsIssuCommand = _FsIssuCommand_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 10),
    _FsIssuCommand_Type()
)
fsIssuCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIssuCommand.setStatus("current")


class _FsIssuCommandStatus_Type(Integer32):
    """Custom type fsIssuCommandStatus based on Integer32"""
    defaultValue = 0

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
        *(("notstarted", 0),
          ("inprogress", 1),
          ("successful", 2),
          ("failed", 3))
    )


_FsIssuCommandStatus_Type.__name__ = "Integer32"
_FsIssuCommandStatus_Object = MibScalar
fsIssuCommandStatus = _FsIssuCommandStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 11),
    _FsIssuCommandStatus_Type()
)
fsIssuCommandStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIssuCommandStatus.setStatus("current")


class _FsIssuProcedureStatus_Type(Integer32):
    """Custom type fsIssuProcedureStatus based on Integer32"""
    defaultValue = 0

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
        *(("notinitiated", 0),
          ("inprogress", 1),
          ("successful", 2),
          ("failed", 3))
    )


_FsIssuProcedureStatus_Type.__name__ = "Integer32"
_FsIssuProcedureStatus_Object = MibScalar
fsIssuProcedureStatus = _FsIssuProcedureStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 12),
    _FsIssuProcedureStatus_Type()
)
fsIssuProcedureStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIssuProcedureStatus.setStatus("current")


class _FsIssuRollbackSoftwareVersion_Type(DisplayString):
    """Custom type fsIssuRollbackSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FsIssuRollbackSoftwareVersion_Type.__name__ = "DisplayString"
_FsIssuRollbackSoftwareVersion_Object = MibScalar
fsIssuRollbackSoftwareVersion = _FsIssuRollbackSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 13),
    _FsIssuRollbackSoftwareVersion_Type()
)
fsIssuRollbackSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIssuRollbackSoftwareVersion.setStatus("current")


class _FsIssuTraceOption_Type(Integer32):
    """Custom type fsIssuTraceOption based on Integer32"""
    defaultValue = 0


_FsIssuTraceOption_Type.__name__ = "Integer32"
_FsIssuTraceOption_Object = MibScalar
fsIssuTraceOption = _FsIssuTraceOption_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 14),
    _FsIssuTraceOption_Type()
)
fsIssuTraceOption.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIssuTraceOption.setStatus("current")


class _FsIssuTrapStatus_Type(Integer32):
    """Custom type fsIssuTrapStatus based on Integer32"""
    defaultValue = 1

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


_FsIssuTrapStatus_Type.__name__ = "Integer32"
_FsIssuTrapStatus_Object = MibScalar
fsIssuTrapStatus = _FsIssuTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 15),
    _FsIssuTrapStatus_Type()
)
fsIssuTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIssuTrapStatus.setStatus("current")
_FsIssuLastUpgradeTime_Type = TimeStamp
_FsIssuLastUpgradeTime_Object = MibScalar
fsIssuLastUpgradeTime = _FsIssuLastUpgradeTime_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 16),
    _FsIssuLastUpgradeTime_Type()
)
fsIssuLastUpgradeTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIssuLastUpgradeTime.setStatus("current")


class _FsIssuSoftwareCompatForVersion_Type(DisplayString):
    """Custom type fsIssuSoftwareCompatForVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_FsIssuSoftwareCompatForVersion_Type.__name__ = "DisplayString"
_FsIssuSoftwareCompatForVersion_Object = MibScalar
fsIssuSoftwareCompatForVersion = _FsIssuSoftwareCompatForVersion_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 1, 17),
    _FsIssuSoftwareCompatForVersion_Type()
)
fsIssuSoftwareCompatForVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIssuSoftwareCompatForVersion.setStatus("current")
_FsIssuNotifications_ObjectIdentity = ObjectIdentity
fsIssuNotifications = _FsIssuNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 2)
)
_FsIssuTraps_ObjectIdentity = ObjectIdentity
fsIssuTraps = _FsIssuTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 2, 0)
)

# Managed Objects groups


# Notification objects

fsIssuMaintenanceStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 2, 0, 1)
)
fsIssuMaintenanceStatusTrap.setObjects(
      *(("ARICENT-ISSU-MIB", "fsIssuMaintenanceMode"),
        ("ARICENT-ISSU-MIB", "fsIssuMaintenanceOperStatus"))
)
if mibBuilder.loadTexts:
    fsIssuMaintenanceStatusTrap.setStatus(
        "current"
    )

fsIssuCommandStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 2, 0, 2)
)
fsIssuCommandStatusTrap.setObjects(
      *(("ARICENT-ISSU-MIB", "fsIssuCommand"),
        ("ARICENT-ISSU-MIB", "fsIssuCommandStatus"))
)
if mibBuilder.loadTexts:
    fsIssuCommandStatusTrap.setStatus(
        "current"
    )

fsIssuProcedureStatusTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 29601, 2, 103, 2, 0, 3)
)
fsIssuProcedureStatusTrap.setObjects(
    ("ARICENT-ISSU-MIB", "fsIssuProcedureStatus")
)
if mibBuilder.loadTexts:
    fsIssuProcedureStatusTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-ISSU-MIB",
    **{"fsIssu": fsIssu,
       "fsIssuSystem": fsIssuSystem,
       "fsIssuMaintenanceMode": fsIssuMaintenanceMode,
       "fsIssuMaintenanceOperStatus": fsIssuMaintenanceOperStatus,
       "fsIssuLoadSWPath": fsIssuLoadSWPath,
       "fsIssuRollbackSWPath": fsIssuRollbackSWPath,
       "fsIssuCurrentSWPath": fsIssuCurrentSWPath,
       "fsIssuSoftwareCompatFilePath": fsIssuSoftwareCompatFilePath,
       "fsIssuSoftwareCompatCheckInit": fsIssuSoftwareCompatCheckInit,
       "fsIssuSoftwareCompatCheckStatus": fsIssuSoftwareCompatCheckStatus,
       "fsIssuMode": fsIssuMode,
       "fsIssuCommand": fsIssuCommand,
       "fsIssuCommandStatus": fsIssuCommandStatus,
       "fsIssuProcedureStatus": fsIssuProcedureStatus,
       "fsIssuRollbackSoftwareVersion": fsIssuRollbackSoftwareVersion,
       "fsIssuTraceOption": fsIssuTraceOption,
       "fsIssuTrapStatus": fsIssuTrapStatus,
       "fsIssuLastUpgradeTime": fsIssuLastUpgradeTime,
       "fsIssuSoftwareCompatForVersion": fsIssuSoftwareCompatForVersion,
       "fsIssuNotifications": fsIssuNotifications,
       "fsIssuTraps": fsIssuTraps,
       "fsIssuMaintenanceStatusTrap": fsIssuMaintenanceStatusTrap,
       "fsIssuCommandStatusTrap": fsIssuCommandStatusTrap,
       "fsIssuProcedureStatusTrap": fsIssuProcedureStatusTrap}
)
