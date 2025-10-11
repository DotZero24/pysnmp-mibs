# SNMP MIB module (ZYXEL-SYSTEM-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zyxel/ZYXEL-SYSTEM-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:26 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(esMgmt,) = mibBuilder.importSymbols(
    "ZYXEL-ES-SMI",
    "esMgmt")


# MODULE-IDENTITY

zyxelManagement = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZyxelSysMgmt_ObjectIdentity = ObjectIdentity
zyxelSysMgmt = _ZyxelSysMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1)
)


class _ZySysMgmtConfigSave_Type(Integer32):
    """Custom type zySysMgmtConfigSave based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_ZySysMgmtConfigSave_Type.__name__ = "Integer32"
_ZySysMgmtConfigSave_Object = MibScalar
zySysMgmtConfigSave = _ZySysMgmtConfigSave_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 1),
    _ZySysMgmtConfigSave_Type()
)
zySysMgmtConfigSave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtConfigSave.setStatus("current")


class _ZySysMgmtBootupConfig_Type(Integer32):
    """Custom type zySysMgmtBootupConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_ZySysMgmtBootupConfig_Type.__name__ = "Integer32"
_ZySysMgmtBootupConfig_Object = MibScalar
zySysMgmtBootupConfig = _ZySysMgmtBootupConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 2),
    _ZySysMgmtBootupConfig_Type()
)
zySysMgmtBootupConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtBootupConfig.setStatus("current")


class _ZySysMgmtReboot_Type(Integer32):
    """Custom type zySysMgmtReboot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reboot", 1))
    )


_ZySysMgmtReboot_Type.__name__ = "Integer32"
_ZySysMgmtReboot_Object = MibScalar
zySysMgmtReboot = _ZySysMgmtReboot_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 3),
    _ZySysMgmtReboot_Type()
)
zySysMgmtReboot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtReboot.setStatus("current")


class _ZySysMgmtDefaultConfig_Type(Integer32):
    """Custom type zySysMgmtDefaultConfig based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("resetToDefault", 1))
    )


_ZySysMgmtDefaultConfig_Type.__name__ = "Integer32"
_ZySysMgmtDefaultConfig_Object = MibScalar
zySysMgmtDefaultConfig = _ZySysMgmtDefaultConfig_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 4),
    _ZySysMgmtDefaultConfig_Type()
)
zySysMgmtDefaultConfig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtDefaultConfig.setStatus("current")


class _ZySysMgmtLastActionStatus_Type(Integer32):
    """Custom type zySysMgmtLastActionStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("success", 1),
          ("fail", 2))
    )


_ZySysMgmtLastActionStatus_Type.__name__ = "Integer32"
_ZySysMgmtLastActionStatus_Object = MibScalar
zySysMgmtLastActionStatus = _ZySysMgmtLastActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 5),
    _ZySysMgmtLastActionStatus_Type()
)
zySysMgmtLastActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtLastActionStatus.setStatus("current")


class _ZySysMgmtSysStatus_Type(Bits):
    """Custom type zySysMgmtSysStatus based on Bits"""
    namedValues = NamedValues(
        *(("sysAlarmDetected", 0),
          ("sysTemperatureError", 1),
          ("sysFanRPMError", 2),
          ("sysVoltageRangeError", 3),
          ("sysNoDefect", 4))
    )

_ZySysMgmtSysStatus_Type.__name__ = "Bits"
_ZySysMgmtSysStatus_Object = MibScalar
zySysMgmtSysStatus = _ZySysMgmtSysStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 6),
    _ZySysMgmtSysStatus_Type()
)
zySysMgmtSysStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtSysStatus.setStatus("current")
_ZySysMgmtCPUUsage_Type = Integer32
_ZySysMgmtCPUUsage_Object = MibScalar
zySysMgmtCPUUsage = _ZySysMgmtCPUUsage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 7),
    _ZySysMgmtCPUUsage_Type()
)
zySysMgmtCPUUsage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtCPUUsage.setStatus("current")


class _ZySysMgmtBootupImage_Type(Integer32):
    """Custom type zySysMgmtBootupImage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("image1", 1),
          ("image2", 2))
    )


_ZySysMgmtBootupImage_Type.__name__ = "Integer32"
_ZySysMgmtBootupImage_Object = MibScalar
zySysMgmtBootupImage = _ZySysMgmtBootupImage_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 8),
    _ZySysMgmtBootupImage_Type()
)
zySysMgmtBootupImage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtBootupImage.setStatus("current")


class _ZySysMgmtCounterReset_Type(Integer32):
    """Custom type zySysMgmtCounterReset based on Integer32"""
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


_ZySysMgmtCounterReset_Type.__name__ = "Integer32"
_ZySysMgmtCounterReset_Object = MibScalar
zySysMgmtCounterReset = _ZySysMgmtCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 9),
    _ZySysMgmtCounterReset_Type()
)
zySysMgmtCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtCounterReset.setStatus("current")
_ZyxelSysMgmtTftpServiceSetup_ObjectIdentity = ObjectIdentity
zyxelSysMgmtTftpServiceSetup = _ZyxelSysMgmtTftpServiceSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10)
)
_ZySysMgmtTftpServiceServerIpAddress_Type = IpAddress
_ZySysMgmtTftpServiceServerIpAddress_Object = MibScalar
zySysMgmtTftpServiceServerIpAddress = _ZySysMgmtTftpServiceServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 1),
    _ZySysMgmtTftpServiceServerIpAddress_Type()
)
zySysMgmtTftpServiceServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtTftpServiceServerIpAddress.setStatus("current")
_ZySysMgmtTftpRemoteFileName_Type = DisplayString
_ZySysMgmtTftpRemoteFileName_Object = MibScalar
zySysMgmtTftpRemoteFileName = _ZySysMgmtTftpRemoteFileName_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 2),
    _ZySysMgmtTftpRemoteFileName_Type()
)
zySysMgmtTftpRemoteFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtTftpRemoteFileName.setStatus("current")


class _ZySysMgmtTftpConfigIndex_Type(Integer32):
    """Custom type zySysMgmtTftpConfigIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_ZySysMgmtTftpConfigIndex_Type.__name__ = "Integer32"
_ZySysMgmtTftpConfigIndex_Object = MibScalar
zySysMgmtTftpConfigIndex = _ZySysMgmtTftpConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 3),
    _ZySysMgmtTftpConfigIndex_Type()
)
zySysMgmtTftpConfigIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtTftpConfigIndex.setStatus("current")


class _ZySysMgmtTftpAction_Type(Integer32):
    """Custom type zySysMgmtTftpAction based on Integer32"""
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
          ("backupConfig", 1),
          ("restoreConfig", 2),
          ("mergeConfig", 3))
    )


_ZySysMgmtTftpAction_Type.__name__ = "Integer32"
_ZySysMgmtTftpAction_Object = MibScalar
zySysMgmtTftpAction = _ZySysMgmtTftpAction_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 4),
    _ZySysMgmtTftpAction_Type()
)
zySysMgmtTftpAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtTftpAction.setStatus("current")


class _ZySysMgmtTftpActionStatus_Type(Integer32):
    """Custom type zySysMgmtTftpActionStatus based on Integer32"""
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
          ("success", 1),
          ("fail", 2),
          ("underAction", 3))
    )


_ZySysMgmtTftpActionStatus_Type.__name__ = "Integer32"
_ZySysMgmtTftpActionStatus_Object = MibScalar
zySysMgmtTftpActionStatus = _ZySysMgmtTftpActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 5),
    _ZySysMgmtTftpActionStatus_Type()
)
zySysMgmtTftpActionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtTftpActionStatus.setStatus("current")


class _ZySysMgmtTftpActionPrivilege13_Type(Integer32):
    """Custom type zySysMgmtTftpActionPrivilege13 based on Integer32"""
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
          ("backupConfig", 1),
          ("restoreConfig", 2),
          ("mergeConfig", 3))
    )


_ZySysMgmtTftpActionPrivilege13_Type.__name__ = "Integer32"
_ZySysMgmtTftpActionPrivilege13_Object = MibScalar
zySysMgmtTftpActionPrivilege13 = _ZySysMgmtTftpActionPrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 10, 113),
    _ZySysMgmtTftpActionPrivilege13_Type()
)
zySysMgmtTftpActionPrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtTftpActionPrivilege13.setStatus("current")


class _ZySysMgmtReloadFactoryDefault_Type(Integer32):
    """Custom type zySysMgmtReloadFactoryDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reloadFactoryDefault", 1))
    )


_ZySysMgmtReloadFactoryDefault_Type.__name__ = "Integer32"
_ZySysMgmtReloadFactoryDefault_Object = MibScalar
zySysMgmtReloadFactoryDefault = _ZySysMgmtReloadFactoryDefault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 11),
    _ZySysMgmtReloadFactoryDefault_Type()
)
zySysMgmtReloadFactoryDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtReloadFactoryDefault.setStatus("current")


class _ZySysMgmtReloadStackingDefault_Type(Integer32):
    """Custom type zySysMgmtReloadStackingDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reloadStackingDefault", 1))
    )


_ZySysMgmtReloadStackingDefault_Type.__name__ = "Integer32"
_ZySysMgmtReloadStackingDefault_Object = MibScalar
zySysMgmtReloadStackingDefault = _ZySysMgmtReloadStackingDefault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 12),
    _ZySysMgmtReloadStackingDefault_Type()
)
zySysMgmtReloadStackingDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtReloadStackingDefault.setStatus("current")


class _ZySysMgmtConfigSaveCustomDefault_Type(Integer32):
    """Custom type zySysMgmtConfigSaveCustomDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("configSaveCustomDefault", 1))
    )


_ZySysMgmtConfigSaveCustomDefault_Type.__name__ = "Integer32"
_ZySysMgmtConfigSaveCustomDefault_Object = MibScalar
zySysMgmtConfigSaveCustomDefault = _ZySysMgmtConfigSaveCustomDefault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 13),
    _ZySysMgmtConfigSaveCustomDefault_Type()
)
zySysMgmtConfigSaveCustomDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtConfigSaveCustomDefault.setStatus("current")


class _ZySysMgmtReloadCustomDefault_Type(Integer32):
    """Custom type zySysMgmtReloadCustomDefault based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("reloadCustomDefault", 1))
    )


_ZySysMgmtReloadCustomDefault_Type.__name__ = "Integer32"
_ZySysMgmtReloadCustomDefault_Object = MibScalar
zySysMgmtReloadCustomDefault = _ZySysMgmtReloadCustomDefault_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 14),
    _ZySysMgmtReloadCustomDefault_Type()
)
zySysMgmtReloadCustomDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtReloadCustomDefault.setStatus("current")
_ZyxelSysMgmtAutoConfiguration_ObjectIdentity = ObjectIdentity
zyxelSysMgmtAutoConfiguration = _ZyxelSysMgmtAutoConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15)
)
_ZyxelSysMgmtAutoConfigurationSetup_ObjectIdentity = ObjectIdentity
zyxelSysMgmtAutoConfigurationSetup = _ZyxelSysMgmtAutoConfigurationSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15, 1)
)
_ZySysMgmtAutoConfigurationState_Type = EnabledStatus
_ZySysMgmtAutoConfigurationState_Object = MibScalar
zySysMgmtAutoConfigurationState = _ZySysMgmtAutoConfigurationState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15, 1, 1),
    _ZySysMgmtAutoConfigurationState_Type()
)
zySysMgmtAutoConfigurationState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtAutoConfigurationState.setStatus("current")
_ZySysMgmtAutoConfigurationMode_Type = Integer32
_ZySysMgmtAutoConfigurationMode_Object = MibScalar
zySysMgmtAutoConfigurationMode = _ZySysMgmtAutoConfigurationMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15, 1, 2),
    _ZySysMgmtAutoConfigurationMode_Type()
)
zySysMgmtAutoConfigurationMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtAutoConfigurationMode.setStatus("current")
_ZySysMgmtAutoConfigurationVlanId_Type = Integer32
_ZySysMgmtAutoConfigurationVlanId_Object = MibScalar
zySysMgmtAutoConfigurationVlanId = _ZySysMgmtAutoConfigurationVlanId_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15, 1, 3),
    _ZySysMgmtAutoConfigurationVlanId_Type()
)
zySysMgmtAutoConfigurationVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtAutoConfigurationVlanId.setStatus("current")
_ZySysMgmtAutoConfigurationUrl_Type = DisplayString
_ZySysMgmtAutoConfigurationUrl_Object = MibScalar
zySysMgmtAutoConfigurationUrl = _ZySysMgmtAutoConfigurationUrl_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15, 1, 4),
    _ZySysMgmtAutoConfigurationUrl_Type()
)
zySysMgmtAutoConfigurationUrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtAutoConfigurationUrl.setStatus("current")
_ZyxelSysMgmtAutoConfigurationStatus_ObjectIdentity = ObjectIdentity
zyxelSysMgmtAutoConfigurationStatus = _ZyxelSysMgmtAutoConfigurationStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15, 2)
)
_ZyxelSysMgmtAutoConfigurationResult_ObjectIdentity = ObjectIdentity
zyxelSysMgmtAutoConfigurationResult = _ZyxelSysMgmtAutoConfigurationResult_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15, 2, 1)
)
_ZySysMgmtAutoConfigurationResultMode_Type = Integer32
_ZySysMgmtAutoConfigurationResultMode_Object = MibScalar
zySysMgmtAutoConfigurationResultMode = _ZySysMgmtAutoConfigurationResultMode_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15, 2, 1, 1),
    _ZySysMgmtAutoConfigurationResultMode_Type()
)
zySysMgmtAutoConfigurationResultMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtAutoConfigurationResultMode.setStatus("current")
_ZySysMgmtAutoConfigurationResultState_Type = Integer32
_ZySysMgmtAutoConfigurationResultState_Object = MibScalar
zySysMgmtAutoConfigurationResultState = _ZySysMgmtAutoConfigurationResultState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15, 2, 1, 2),
    _ZySysMgmtAutoConfigurationResultState_Type()
)
zySysMgmtAutoConfigurationResultState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtAutoConfigurationResultState.setStatus("current")
_ZySysMgmtAutoConfigurationResultFilename_Type = DisplayString
_ZySysMgmtAutoConfigurationResultFilename_Object = MibScalar
zySysMgmtAutoConfigurationResultFilename = _ZySysMgmtAutoConfigurationResultFilename_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 15, 2, 1, 3),
    _ZySysMgmtAutoConfigurationResultFilename_Type()
)
zySysMgmtAutoConfigurationResultFilename.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zySysMgmtAutoConfigurationResultFilename.setStatus("current")
_ZyxelSysMgmtCustomDefaultSetup_ObjectIdentity = ObjectIdentity
zyxelSysMgmtCustomDefaultSetup = _ZyxelSysMgmtCustomDefaultSetup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 16)
)


class _ZySysMgmtCustomDefaultState_Type(Integer32):
    """Custom type zySysMgmtCustomDefaultState based on Integer32"""
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


_ZySysMgmtCustomDefaultState_Type.__name__ = "Integer32"
_ZySysMgmtCustomDefaultState_Object = MibScalar
zySysMgmtCustomDefaultState = _ZySysMgmtCustomDefaultState_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 16, 1),
    _ZySysMgmtCustomDefaultState_Type()
)
zySysMgmtCustomDefaultState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtCustomDefaultState.setStatus("current")


class _ZySysMgmtConfigSavePrivilege13_Type(Integer32):
    """Custom type zySysMgmtConfigSavePrivilege13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config1", 1),
          ("config2", 2))
    )


_ZySysMgmtConfigSavePrivilege13_Type.__name__ = "Integer32"
_ZySysMgmtConfigSavePrivilege13_Object = MibScalar
zySysMgmtConfigSavePrivilege13 = _ZySysMgmtConfigSavePrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 113),
    _ZySysMgmtConfigSavePrivilege13_Type()
)
zySysMgmtConfigSavePrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtConfigSavePrivilege13.setStatus("current")


class _ZySysMgmtDefaultConfigPrivilege13_Type(Integer32):
    """Custom type zySysMgmtDefaultConfigPrivilege13 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nothing", 0),
          ("resetToDefault", 1))
    )


_ZySysMgmtDefaultConfigPrivilege13_Type.__name__ = "Integer32"
_ZySysMgmtDefaultConfigPrivilege13_Object = MibScalar
zySysMgmtDefaultConfigPrivilege13 = _ZySysMgmtDefaultConfigPrivilege13_Object(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 1, 213),
    _ZySysMgmtDefaultConfigPrivilege13_Type()
)
zySysMgmtDefaultConfigPrivilege13.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zySysMgmtDefaultConfigPrivilege13.setStatus("current")
_ZyxelSysMgmtNotifications_ObjectIdentity = ObjectIdentity
zyxelSysMgmtNotifications = _ZyxelSysMgmtNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2)
)

# Managed Objects groups


# Notification objects

zySysMgmtUncontrolledSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2, 1)
)
if mibBuilder.loadTexts:
    zySysMgmtUncontrolledSystemReset.setStatus(
        "current"
    )

zySysMgmtControlledSystemReset = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2, 2)
)
if mibBuilder.loadTexts:
    zySysMgmtControlledSystemReset.setStatus(
        "current"
    )

zySysMgmtBootImageInconsistence = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2, 3)
)
if mibBuilder.loadTexts:
    zySysMgmtBootImageInconsistence.setStatus(
        "current"
    )

zySysMgmtReloadCustomCAFail = NotificationType(
    (1, 3, 6, 1, 4, 1, 890, 1, 15, 3, 49, 2, 4)
)
if mibBuilder.loadTexts:
    zySysMgmtReloadCustomCAFail.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZYXEL-SYSTEM-MGMT-MIB",
    **{"zyxelManagement": zyxelManagement,
       "zyxelSysMgmt": zyxelSysMgmt,
       "zySysMgmtConfigSave": zySysMgmtConfigSave,
       "zySysMgmtBootupConfig": zySysMgmtBootupConfig,
       "zySysMgmtReboot": zySysMgmtReboot,
       "zySysMgmtDefaultConfig": zySysMgmtDefaultConfig,
       "zySysMgmtLastActionStatus": zySysMgmtLastActionStatus,
       "zySysMgmtSysStatus": zySysMgmtSysStatus,
       "zySysMgmtCPUUsage": zySysMgmtCPUUsage,
       "zySysMgmtBootupImage": zySysMgmtBootupImage,
       "zySysMgmtCounterReset": zySysMgmtCounterReset,
       "zyxelSysMgmtTftpServiceSetup": zyxelSysMgmtTftpServiceSetup,
       "zySysMgmtTftpServiceServerIpAddress": zySysMgmtTftpServiceServerIpAddress,
       "zySysMgmtTftpRemoteFileName": zySysMgmtTftpRemoteFileName,
       "zySysMgmtTftpConfigIndex": zySysMgmtTftpConfigIndex,
       "zySysMgmtTftpAction": zySysMgmtTftpAction,
       "zySysMgmtTftpActionStatus": zySysMgmtTftpActionStatus,
       "zySysMgmtTftpActionPrivilege13": zySysMgmtTftpActionPrivilege13,
       "zySysMgmtReloadFactoryDefault": zySysMgmtReloadFactoryDefault,
       "zySysMgmtReloadStackingDefault": zySysMgmtReloadStackingDefault,
       "zySysMgmtConfigSaveCustomDefault": zySysMgmtConfigSaveCustomDefault,
       "zySysMgmtReloadCustomDefault": zySysMgmtReloadCustomDefault,
       "zyxelSysMgmtAutoConfiguration": zyxelSysMgmtAutoConfiguration,
       "zyxelSysMgmtAutoConfigurationSetup": zyxelSysMgmtAutoConfigurationSetup,
       "zySysMgmtAutoConfigurationState": zySysMgmtAutoConfigurationState,
       "zySysMgmtAutoConfigurationMode": zySysMgmtAutoConfigurationMode,
       "zySysMgmtAutoConfigurationVlanId": zySysMgmtAutoConfigurationVlanId,
       "zySysMgmtAutoConfigurationUrl": zySysMgmtAutoConfigurationUrl,
       "zyxelSysMgmtAutoConfigurationStatus": zyxelSysMgmtAutoConfigurationStatus,
       "zyxelSysMgmtAutoConfigurationResult": zyxelSysMgmtAutoConfigurationResult,
       "zySysMgmtAutoConfigurationResultMode": zySysMgmtAutoConfigurationResultMode,
       "zySysMgmtAutoConfigurationResultState": zySysMgmtAutoConfigurationResultState,
       "zySysMgmtAutoConfigurationResultFilename": zySysMgmtAutoConfigurationResultFilename,
       "zyxelSysMgmtCustomDefaultSetup": zyxelSysMgmtCustomDefaultSetup,
       "zySysMgmtCustomDefaultState": zySysMgmtCustomDefaultState,
       "zySysMgmtConfigSavePrivilege13": zySysMgmtConfigSavePrivilege13,
       "zySysMgmtDefaultConfigPrivilege13": zySysMgmtDefaultConfigPrivilege13,
       "zyxelSysMgmtNotifications": zyxelSysMgmtNotifications,
       "zySysMgmtUncontrolledSystemReset": zySysMgmtUncontrolledSystemReset,
       "zySysMgmtControlledSystemReset": zySysMgmtControlledSystemReset,
       "zySysMgmtBootImageInconsistence": zySysMgmtBootImageInconsistence,
       "zySysMgmtReloadCustomCAFail": zySysMgmtReloadCustomCAFail}
)
