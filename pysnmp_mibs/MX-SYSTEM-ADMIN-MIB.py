# SNMP MIB module (MX-SYSTEM-ADMIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SYSTEM-ADMIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:27 2025
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

(mediatrixAdmin,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixAdmin")

(MxEnableState,) = mibBuilder.importSymbols(
    "MX-TC",
    "MxEnableState")

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

sysAdminMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1)
)
if mibBuilder.loadTexts:
    sysAdminMIB.setRevisions(
        ("2006-03-06 00:00",
         "2005-04-20 00:00",
         "2004-02-12 00:00",
         "1903-12-02 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SysAdminMIBObjects_ObjectIdentity = ObjectIdentity
sysAdminMIBObjects = _SysAdminMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 1)
)


class _SysAdminCommand_Type(Integer32):
    """Custom type sysAdminCommand based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 0),
          ("checkRam", 1),
          ("checkRom", 2),
          ("downloadSoftware", 3),
          ("resetStats", 4),
          ("setConfigSourcesStatic", 5),
          ("updateConfiguration", 6))
    )


_SysAdminCommand_Type.__name__ = "Integer32"
_SysAdminCommand_Object = MibScalar
sysAdminCommand = _SysAdminCommand_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 1),
    _SysAdminCommand_Type()
)
sysAdminCommand.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAdminCommand.setStatus("current")


class _SysAdminDefaultSettingsEnable_Type(MxEnableState):
    """Custom type sysAdminDefaultSettingsEnable based on MxEnableState"""
    defaultValue = 1


_SysAdminDefaultSettingsEnable_Type.__name__ = "MxEnableState"
_SysAdminDefaultSettingsEnable_Object = MibScalar
sysAdminDefaultSettingsEnable = _SysAdminDefaultSettingsEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 5),
    _SysAdminDefaultSettingsEnable_Type()
)
sysAdminDefaultSettingsEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysAdminDefaultSettingsEnable.setStatus("current")


class _SysAdminLastCheckRam_Type(Integer32):
    """Custom type sysAdminLastCheckRam based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notTested", 0),
          ("fail", 1),
          ("success", 2))
    )


_SysAdminLastCheckRam_Type.__name__ = "Integer32"
_SysAdminLastCheckRam_Object = MibScalar
sysAdminLastCheckRam = _SysAdminLastCheckRam_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 11),
    _SysAdminLastCheckRam_Type()
)
sysAdminLastCheckRam.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAdminLastCheckRam.setStatus("current")


class _SysAdminLastCheckRom_Type(Integer32):
    """Custom type sysAdminLastCheckRom based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("success", 2))
    )


_SysAdminLastCheckRom_Type.__name__ = "Integer32"
_SysAdminLastCheckRom_Object = MibScalar
sysAdminLastCheckRom = _SysAdminLastCheckRom_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 12),
    _SysAdminLastCheckRom_Type()
)
sysAdminLastCheckRom.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAdminLastCheckRom.setStatus("current")


class _SysAdminLastDownloadSoftware_Type(Integer32):
    """Custom type sysAdminLastDownloadSoftware based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fail", 1),
          ("success", 2))
    )


_SysAdminLastDownloadSoftware_Type.__name__ = "Integer32"
_SysAdminLastDownloadSoftware_Object = MibScalar
sysAdminLastDownloadSoftware = _SysAdminLastDownloadSoftware_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 14),
    _SysAdminLastDownloadSoftware_Type()
)
sysAdminLastDownloadSoftware.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAdminLastDownloadSoftware.setStatus("current")


class _SysAdminDownloadConfigFileStatus_Type(Integer32):
    """Custom type sysAdminDownloadConfigFileStatus based on Integer32"""
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
        *(("idle", 0),
          ("fail", 1),
          ("success", 2),
          ("inProgress", 3),
          ("listening", 4))
    )


_SysAdminDownloadConfigFileStatus_Type.__name__ = "Integer32"
_SysAdminDownloadConfigFileStatus_Object = MibScalar
sysAdminDownloadConfigFileStatus = _SysAdminDownloadConfigFileStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 30),
    _SysAdminDownloadConfigFileStatus_Type()
)
sysAdminDownloadConfigFileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAdminDownloadConfigFileStatus.setStatus("current")


class _SysAdminAppMode_Type(Integer32):
    """Custom type sysAdminAppMode based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("recovery", 1))
    )


_SysAdminAppMode_Type.__name__ = "Integer32"
_SysAdminAppMode_Object = MibScalar
sysAdminAppMode = _SysAdminAppMode_Object(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 1, 50),
    _SysAdminAppMode_Type()
)
sysAdminAppMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysAdminAppMode.setStatus("current")
_SysAdminConformance_ObjectIdentity = ObjectIdentity
sysAdminConformance = _SysAdminConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 2)
)
_SysAdminCompliances_ObjectIdentity = ObjectIdentity
sysAdminCompliances = _SysAdminCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 2, 1)
)
_SysAdminGroups_ObjectIdentity = ObjectIdentity
sysAdminGroups = _SysAdminGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 2, 2)
)

# Managed Objects groups

sysAdminGroupVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 2, 2, 1)
)
sysAdminGroupVer1.setObjects(
      *(("MX-SYSTEM-ADMIN-MIB", "sysAdminDownloadConfigFileStatus"),
        ("MX-SYSTEM-ADMIN-MIB", "sysAdminCommand"),
        ("MX-SYSTEM-ADMIN-MIB", "sysAdminDefaultSettingsEnable"),
        ("MX-SYSTEM-ADMIN-MIB", "sysAdminLastCheckRam"),
        ("MX-SYSTEM-ADMIN-MIB", "sysAdminLastCheckRom"),
        ("MX-SYSTEM-ADMIN-MIB", "sysAdminLastDownloadSoftware"),
        ("MX-SYSTEM-ADMIN-MIB", "sysAdminAppMode"))
)
if mibBuilder.loadTexts:
    sysAdminGroupVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

sysAdminComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 5, 1, 2, 1, 1)
)
sysAdminComplVer1.setObjects(
    ("MX-SYSTEM-ADMIN-MIB", "sysAdminGroupVer1")
)
if mibBuilder.loadTexts:
    sysAdminComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SYSTEM-ADMIN-MIB",
    **{"sysAdminMIB": sysAdminMIB,
       "sysAdminMIBObjects": sysAdminMIBObjects,
       "sysAdminCommand": sysAdminCommand,
       "sysAdminDefaultSettingsEnable": sysAdminDefaultSettingsEnable,
       "sysAdminLastCheckRam": sysAdminLastCheckRam,
       "sysAdminLastCheckRom": sysAdminLastCheckRom,
       "sysAdminLastDownloadSoftware": sysAdminLastDownloadSoftware,
       "sysAdminDownloadConfigFileStatus": sysAdminDownloadConfigFileStatus,
       "sysAdminAppMode": sysAdminAppMode,
       "sysAdminConformance": sysAdminConformance,
       "sysAdminCompliances": sysAdminCompliances,
       "sysAdminComplVer1": sysAdminComplVer1,
       "sysAdminGroups": sysAdminGroups,
       "sysAdminGroupVer1": sysAdminGroupVer1}
)
