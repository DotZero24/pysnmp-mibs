# SNMP MIB module (ELTEX-MES-ISS-SYSTEM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-SYSTEM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:49:58 2025
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

(mcTrapDescr,) = mibBuilder.importSymbols(
    "ELTEX-SMI",
    "mcTrapDescr")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssSystemMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18)
)
if mibBuilder.loadTexts:
    eltMesIssSystemMIB.setRevisions(
        ("2023-01-30 00:00",
         "2022-06-09 00:00",
         "2021-04-28 00:00",
         "2021-02-05 00:00",
         "2020-05-08 00:00",
         "2019-10-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesIssSysDelayedReloadMode(TextualConvention, Integer32):
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
        *(("reloadIn", 1),
          ("reloadAt", 2),
          ("noReload", 3))
    )



class EltMesIssSysImageType(TextualConvention, Integer32):
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
        *(("image", 1),
          ("boot", 2),
          ("preloader", 3))
    )



class EltMesIssSysImageState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("active", 1),
          ("inactive", 2))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssSysObjects_ObjectIdentity = ObjectIdentity
eltMesIssSysObjects = _EltMesIssSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1)
)
_EltMesIssSysGlobals_ObjectIdentity = ObjectIdentity
eltMesIssSysGlobals = _EltMesIssSysGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1)
)
_EltMesIssSysReloadParams_ObjectIdentity = ObjectIdentity
eltMesIssSysReloadParams = _EltMesIssSysReloadParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 1)
)


class _EltMesIssDelayReloadTime_Type(OctetString):
    """Custom type eltMesIssDelayReloadTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_EltMesIssDelayReloadTime_Type.__name__ = "OctetString"
_EltMesIssDelayReloadTime_Object = MibScalar
eltMesIssDelayReloadTime = _EltMesIssDelayReloadTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 1, 1),
    _EltMesIssDelayReloadTime_Type()
)
eltMesIssDelayReloadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDelayReloadTime.setStatus("current")


class _EltMesIssDelayReloadAction_Type(EltMesIssSysDelayedReloadMode):
    """Custom type eltMesIssDelayReloadAction based on EltMesIssSysDelayedReloadMode"""
    defaultValue = 3


_EltMesIssDelayReloadAction_Type.__name__ = "EltMesIssSysDelayedReloadMode"
_EltMesIssDelayReloadAction_Object = MibScalar
eltMesIssDelayReloadAction = _EltMesIssDelayReloadAction_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 1, 2),
    _EltMesIssDelayReloadAction_Type()
)
eltMesIssDelayReloadAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssDelayReloadAction.setStatus("current")
_EltMesIssSysLoggingParams_ObjectIdentity = ObjectIdentity
eltMesIssSysLoggingParams = _EltMesIssSysLoggingParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 2)
)
_EltMesIssSysClearDebugLogs_Type = TruthValue
_EltMesIssSysClearDebugLogs_Object = MibScalar
eltMesIssSysClearDebugLogs = _EltMesIssSysClearDebugLogs_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 2, 1),
    _EltMesIssSysClearDebugLogs_Type()
)
eltMesIssSysClearDebugLogs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSysClearDebugLogs.setStatus("current")


class _EltMesIssSysReloadRequestLoggingEnable_Type(TruthValue):
    """Custom type eltMesIssSysReloadRequestLoggingEnable based on TruthValue"""
    defaultValue = 1


_EltMesIssSysReloadRequestLoggingEnable_Type.__name__ = "TruthValue"
_EltMesIssSysReloadRequestLoggingEnable_Object = MibScalar
eltMesIssSysReloadRequestLoggingEnable = _EltMesIssSysReloadRequestLoggingEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 2, 2),
    _EltMesIssSysReloadRequestLoggingEnable_Type()
)
eltMesIssSysReloadRequestLoggingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSysReloadRequestLoggingEnable.setStatus("current")


class _EltMesIssSysStartupType_Type(Integer32):
    """Custom type eltMesIssSysStartupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("coldstart", 0),
          ("warmstart", 1),
          ("undefined", 2))
    )


_EltMesIssSysStartupType_Type.__name__ = "Integer32"
_EltMesIssSysStartupType_Object = MibScalar
eltMesIssSysStartupType = _EltMesIssSysStartupType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 2, 3),
    _EltMesIssSysStartupType_Type()
)
eltMesIssSysStartupType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSysStartupType.setStatus("current")
_EltMesIssSysBootVar_ObjectIdentity = ObjectIdentity
eltMesIssSysBootVar = _EltMesIssSysBootVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3)
)
_EltMesIssSysBootVarTable_Object = MibTable
eltMesIssSysBootVarTable = _EltMesIssSysBootVarTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltMesIssSysBootVarTable.setStatus("current")
_EltMesIssSysBootVarEntry_Object = MibTableRow
eltMesIssSysBootVarEntry = _EltMesIssSysBootVarEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1)
)
eltMesIssSysBootVarEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-SYSTEM-MIB", "eltMesIssSysBootVarImageType"),
    (0, "ELTEX-MES-ISS-SYSTEM-MIB", "eltMesIssSysBootVarImageState"),
)
if mibBuilder.loadTexts:
    eltMesIssSysBootVarEntry.setStatus("current")
_EltMesIssSysBootVarImageType_Type = EltMesIssSysImageType
_EltMesIssSysBootVarImageType_Object = MibTableColumn
eltMesIssSysBootVarImageType = _EltMesIssSysBootVarImageType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 1),
    _EltMesIssSysBootVarImageType_Type()
)
eltMesIssSysBootVarImageType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssSysBootVarImageType.setStatus("current")
_EltMesIssSysBootVarImageState_Type = EltMesIssSysImageState
_EltMesIssSysBootVarImageState_Object = MibTableColumn
eltMesIssSysBootVarImageState = _EltMesIssSysBootVarImageState_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 2),
    _EltMesIssSysBootVarImageState_Type()
)
eltMesIssSysBootVarImageState.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssSysBootVarImageState.setStatus("current")
_EltMesIssSysBootVarValid_Type = TruthValue
_EltMesIssSysBootVarValid_Object = MibTableColumn
eltMesIssSysBootVarValid = _EltMesIssSysBootVarValid_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 3),
    _EltMesIssSysBootVarValid_Type()
)
eltMesIssSysBootVarValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSysBootVarValid.setStatus("current")
_EltMesIssSysBootVarVersion_Type = DisplayString
_EltMesIssSysBootVarVersion_Object = MibTableColumn
eltMesIssSysBootVarVersion = _EltMesIssSysBootVarVersion_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 4),
    _EltMesIssSysBootVarVersion_Type()
)
eltMesIssSysBootVarVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSysBootVarVersion.setStatus("current")
_EltMesIssSysBootVarCommit_Type = DisplayString
_EltMesIssSysBootVarCommit_Object = MibTableColumn
eltMesIssSysBootVarCommit = _EltMesIssSysBootVarCommit_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 5),
    _EltMesIssSysBootVarCommit_Type()
)
eltMesIssSysBootVarCommit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSysBootVarCommit.setStatus("current")
_EltMesIssSysBootVarBuild_Type = DisplayString
_EltMesIssSysBootVarBuild_Object = MibTableColumn
eltMesIssSysBootVarBuild = _EltMesIssSysBootVarBuild_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 6),
    _EltMesIssSysBootVarBuild_Type()
)
eltMesIssSysBootVarBuild.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSysBootVarBuild.setStatus("current")
_EltMesIssSysBootVarMd5Digest_Type = DisplayString
_EltMesIssSysBootVarMd5Digest_Object = MibTableColumn
eltMesIssSysBootVarMd5Digest = _EltMesIssSysBootVarMd5Digest_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 7),
    _EltMesIssSysBootVarMd5Digest_Type()
)
eltMesIssSysBootVarMd5Digest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSysBootVarMd5Digest.setStatus("current")
_EltMesIssSysBootVarTime_Type = DisplayString
_EltMesIssSysBootVarTime_Object = MibTableColumn
eltMesIssSysBootVarTime = _EltMesIssSysBootVarTime_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 8),
    _EltMesIssSysBootVarTime_Type()
)
eltMesIssSysBootVarTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSysBootVarTime.setStatus("current")
_EltMesIssSysBootVarImageStateAfterReboot_Type = EltMesIssSysImageState
_EltMesIssSysBootVarImageStateAfterReboot_Object = MibTableColumn
eltMesIssSysBootVarImageStateAfterReboot = _EltMesIssSysBootVarImageStateAfterReboot_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 3, 1, 1, 9),
    _EltMesIssSysBootVarImageStateAfterReboot_Type()
)
eltMesIssSysBootVarImageStateAfterReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSysBootVarImageStateAfterReboot.setStatus("current")


class _EltMesIssSysDescr_Type(DisplayString):
    """Custom type eltMesIssSysDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_EltMesIssSysDescr_Type.__name__ = "DisplayString"
_EltMesIssSysDescr_Object = MibScalar
eltMesIssSysDescr = _EltMesIssSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 1, 1, 4),
    _EltMesIssSysDescr_Type()
)
eltMesIssSysDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSysDescr.setStatus("current")
_EltMesIssSysNotifications_ObjectIdentity = ObjectIdentity
eltMesIssSysNotifications = _EltMesIssSysNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 2)
)
_EltMesIssSysNotificationsPrefix_ObjectIdentity = ObjectIdentity
eltMesIssSysNotificationsPrefix = _EltMesIssSysNotificationsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 2, 0)
)

# Managed Objects groups


# Notification objects

eltMesIssSysReloadRequestTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 18, 2, 0, 1)
)
eltMesIssSysReloadRequestTrap.setObjects(
    ("ELTEX-SMI", "mcTrapDescr")
)
if mibBuilder.loadTexts:
    eltMesIssSysReloadRequestTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-SYSTEM-MIB",
    **{"EltMesIssSysDelayedReloadMode": EltMesIssSysDelayedReloadMode,
       "EltMesIssSysImageType": EltMesIssSysImageType,
       "EltMesIssSysImageState": EltMesIssSysImageState,
       "eltMesIssSystemMIB": eltMesIssSystemMIB,
       "eltMesIssSysObjects": eltMesIssSysObjects,
       "eltMesIssSysGlobals": eltMesIssSysGlobals,
       "eltMesIssSysReloadParams": eltMesIssSysReloadParams,
       "eltMesIssDelayReloadTime": eltMesIssDelayReloadTime,
       "eltMesIssDelayReloadAction": eltMesIssDelayReloadAction,
       "eltMesIssSysLoggingParams": eltMesIssSysLoggingParams,
       "eltMesIssSysClearDebugLogs": eltMesIssSysClearDebugLogs,
       "eltMesIssSysReloadRequestLoggingEnable": eltMesIssSysReloadRequestLoggingEnable,
       "eltMesIssSysStartupType": eltMesIssSysStartupType,
       "eltMesIssSysBootVar": eltMesIssSysBootVar,
       "eltMesIssSysBootVarTable": eltMesIssSysBootVarTable,
       "eltMesIssSysBootVarEntry": eltMesIssSysBootVarEntry,
       "eltMesIssSysBootVarImageType": eltMesIssSysBootVarImageType,
       "eltMesIssSysBootVarImageState": eltMesIssSysBootVarImageState,
       "eltMesIssSysBootVarValid": eltMesIssSysBootVarValid,
       "eltMesIssSysBootVarVersion": eltMesIssSysBootVarVersion,
       "eltMesIssSysBootVarCommit": eltMesIssSysBootVarCommit,
       "eltMesIssSysBootVarBuild": eltMesIssSysBootVarBuild,
       "eltMesIssSysBootVarMd5Digest": eltMesIssSysBootVarMd5Digest,
       "eltMesIssSysBootVarTime": eltMesIssSysBootVarTime,
       "eltMesIssSysBootVarImageStateAfterReboot": eltMesIssSysBootVarImageStateAfterReboot,
       "eltMesIssSysDescr": eltMesIssSysDescr,
       "eltMesIssSysNotifications": eltMesIssSysNotifications,
       "eltMesIssSysNotificationsPrefix": eltMesIssSysNotificationsPrefix,
       "eltMesIssSysReloadRequestTrap": eltMesIssSysReloadRequestTrap}
)
