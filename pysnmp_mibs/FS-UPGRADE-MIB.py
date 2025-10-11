# SNMP MIB module (FS-UPGRADE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-UPGRADE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:14:12 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsUpgradeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158)
)
if mibBuilder.loadTexts:
    fsUpgradeMIB.setRevisions(
        ("2018-01-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsUpgradeMIBObjects_ObjectIdentity = ObjectIdentity
fsUpgradeMIBObjects = _FsUpgradeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 1)
)
_FsUpgradeMIBGroups_ObjectIdentity = ObjectIdentity
fsUpgradeMIBGroups = _FsUpgradeMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 1, 1)
)


class _FsFileSystemUpgradeDownloadUrl_Type(DisplayString):
    """Custom type fsFileSystemUpgradeDownloadUrl based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FsFileSystemUpgradeDownloadUrl_Type.__name__ = "DisplayString"
_FsFileSystemUpgradeDownloadUrl_Object = MibScalar
fsFileSystemUpgradeDownloadUrl = _FsFileSystemUpgradeDownloadUrl_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 1, 1, 1),
    _FsFileSystemUpgradeDownloadUrl_Type()
)
fsFileSystemUpgradeDownloadUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFileSystemUpgradeDownloadUrl.setStatus("current")


class _FsFileSystemUpgradeDownloadFlag_Type(Integer32):
    """Custom type fsFileSystemUpgradeDownloadFlag based on Integer32"""
    defaultValue = 0


_FsFileSystemUpgradeDownloadFlag_Type.__name__ = "Integer32"
_FsFileSystemUpgradeDownloadFlag_Object = MibScalar
fsFileSystemUpgradeDownloadFlag = _FsFileSystemUpgradeDownloadFlag_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 1, 1, 2),
    _FsFileSystemUpgradeDownloadFlag_Type()
)
fsFileSystemUpgradeDownloadFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsFileSystemUpgradeDownloadFlag.setStatus("current")
_FsUpgradeMIBTraps_ObjectIdentity = ObjectIdentity
fsUpgradeMIBTraps = _FsUpgradeMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 2)
)
_FsUpgradeMIBConformance_ObjectIdentity = ObjectIdentity
fsUpgradeMIBConformance = _FsUpgradeMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 3)
)
_FsUpgradeMIBCompliances_ObjectIdentity = ObjectIdentity
fsUpgradeMIBCompliances = _FsUpgradeMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 3, 1)
)
_FsSystemCurrtenVersion_Type = DisplayString
_FsSystemCurrtenVersion_Object = MibScalar
fsSystemCurrtenVersion = _FsSystemCurrtenVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 3, 1, 1),
    _FsSystemCurrtenVersion_Type()
)
fsSystemCurrtenVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSystemCurrtenVersion.setStatus("current")
_FsSystemUpgradeFailNo_Type = Integer32
_FsSystemUpgradeFailNo_Object = MibScalar
fsSystemUpgradeFailNo = _FsSystemUpgradeFailNo_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 3, 1, 2),
    _FsSystemUpgradeFailNo_Type()
)
fsSystemUpgradeFailNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSystemUpgradeFailNo.setStatus("current")
_FsSystemUpgradeFailReason_Type = DisplayString
_FsSystemUpgradeFailReason_Object = MibScalar
fsSystemUpgradeFailReason = _FsSystemUpgradeFailReason_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 3, 1, 3),
    _FsSystemUpgradeFailReason_Type()
)
fsSystemUpgradeFailReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSystemUpgradeFailReason.setStatus("current")
_FsSystemUpgradeFailVersion_Type = DisplayString
_FsSystemUpgradeFailVersion_Object = MibScalar
fsSystemUpgradeFailVersion = _FsSystemUpgradeFailVersion_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 3, 1, 4),
    _FsSystemUpgradeFailVersion_Type()
)
fsSystemUpgradeFailVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSystemUpgradeFailVersion.setStatus("current")

# Managed Objects groups


# Notification objects

fsUpgradeFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 2, 1)
)
fsUpgradeFailTrap.setObjects(
      *(("FS-UPGRADE-MIB", "fsSystemCurrtenVersion"),
        ("FS-UPGRADE-MIB", "fsSystemUpgradeFailNo"),
        ("FS-UPGRADE-MIB", "fsSystemUpgradeFailReason"),
        ("FS-UPGRADE-MIB", "fsSystemUpgradeFailVersion"))
)
if mibBuilder.loadTexts:
    fsUpgradeFailTrap.setStatus(
        "current"
    )

fsUpgradeFailRecovTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 158, 2, 2)
)
fsUpgradeFailRecovTrap.setObjects(
      *(("FS-UPGRADE-MIB", "fsSystemCurrtenVersion"),
        ("FS-UPGRADE-MIB", "fsSystemUpgradeFailNo"),
        ("FS-UPGRADE-MIB", "fsSystemUpgradeFailReason"),
        ("FS-UPGRADE-MIB", "fsSystemUpgradeFailVersion"))
)
if mibBuilder.loadTexts:
    fsUpgradeFailRecovTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-UPGRADE-MIB",
    **{"fsUpgradeMIB": fsUpgradeMIB,
       "fsUpgradeMIBObjects": fsUpgradeMIBObjects,
       "fsUpgradeMIBGroups": fsUpgradeMIBGroups,
       "fsFileSystemUpgradeDownloadUrl": fsFileSystemUpgradeDownloadUrl,
       "fsFileSystemUpgradeDownloadFlag": fsFileSystemUpgradeDownloadFlag,
       "fsUpgradeMIBTraps": fsUpgradeMIBTraps,
       "fsUpgradeFailTrap": fsUpgradeFailTrap,
       "fsUpgradeFailRecovTrap": fsUpgradeFailRecovTrap,
       "fsUpgradeMIBConformance": fsUpgradeMIBConformance,
       "fsUpgradeMIBCompliances": fsUpgradeMIBCompliances,
       "fsSystemCurrtenVersion": fsSystemCurrtenVersion,
       "fsSystemUpgradeFailNo": fsSystemUpgradeFailNo,
       "fsSystemUpgradeFailReason": fsSystemUpgradeFailReason,
       "fsSystemUpgradeFailVersion": fsSystemUpgradeFailVersion}
)
