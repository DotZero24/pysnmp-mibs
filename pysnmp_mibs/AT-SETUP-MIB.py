# SNMP MIB module (AT-SETUP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/allied-old/AT-SETUP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:23:36 2025
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

(modules,) = mibBuilder.importSymbols(
    "AT-SMI-MIB",
    "modules")

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

setup = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500)
)
if mibBuilder.loadTexts:
    setup.setRevisions(
        ("2008-10-02 00:00",
         "2008-09-30 00:00",
         "2008-09-24 00:00",
         "2008-05-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _RestartDevice_Type(Integer32):
    """Custom type restartDevice based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_RestartDevice_Type.__name__ = "Integer32"
_RestartDevice_Object = MibScalar
restartDevice = _RestartDevice_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 1),
    _RestartDevice_Type()
)
restartDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartDevice.setStatus("current")
_Firmware_ObjectIdentity = ObjectIdentity
firmware = _Firmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2)
)
_CurrentFirmware_ObjectIdentity = ObjectIdentity
currentFirmware = _CurrentFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1)
)
_CurrSoftVersion_Type = DisplayString
_CurrSoftVersion_Object = MibScalar
currSoftVersion = _CurrSoftVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 1),
    _CurrSoftVersion_Type()
)
currSoftVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currSoftVersion.setStatus("current")
_CurrSoftName_Type = DisplayString
_CurrSoftName_Object = MibScalar
currSoftName = _CurrSoftName_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 2),
    _CurrSoftName_Type()
)
currSoftName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    currSoftName.setStatus("current")
_CurrSoftSaveAs_Type = DisplayString
_CurrSoftSaveAs_Object = MibScalar
currSoftSaveAs = _CurrSoftSaveAs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 1, 3),
    _CurrSoftSaveAs_Type()
)
currSoftSaveAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    currSoftSaveAs.setStatus("current")
_NextBootFirmware_ObjectIdentity = ObjectIdentity
nextBootFirmware = _NextBootFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2)
)
_NextBootVersion_Type = DisplayString
_NextBootVersion_Object = MibScalar
nextBootVersion = _NextBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 1),
    _NextBootVersion_Type()
)
nextBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nextBootVersion.setStatus("current")
_NextBootPath_Type = DisplayString
_NextBootPath_Object = MibScalar
nextBootPath = _NextBootPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 2, 2),
    _NextBootPath_Type()
)
nextBootPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nextBootPath.setStatus("current")
_BackupFirmware_ObjectIdentity = ObjectIdentity
backupFirmware = _BackupFirmware_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3)
)
_BackupVersion_Type = DisplayString
_BackupVersion_Object = MibScalar
backupVersion = _BackupVersion_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 1),
    _BackupVersion_Type()
)
backupVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    backupVersion.setStatus("current")
_BackupPath_Type = DisplayString
_BackupPath_Object = MibScalar
backupPath = _BackupPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 2, 3, 2),
    _BackupPath_Type()
)
backupPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    backupPath.setStatus("current")
_DeviceConfiguration_ObjectIdentity = ObjectIdentity
deviceConfiguration = _DeviceConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3)
)
_RunningConfig_ObjectIdentity = ObjectIdentity
runningConfig = _RunningConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1)
)
_RunCnfgSaveAs_Type = DisplayString
_RunCnfgSaveAs_Object = MibScalar
runCnfgSaveAs = _RunCnfgSaveAs_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 1, 1),
    _RunCnfgSaveAs_Type()
)
runCnfgSaveAs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    runCnfgSaveAs.setStatus("current")
_NextBootConfig_ObjectIdentity = ObjectIdentity
nextBootConfig = _NextBootConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2)
)
_BootCnfgPath_Type = DisplayString
_BootCnfgPath_Object = MibScalar
bootCnfgPath = _BootCnfgPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 1),
    _BootCnfgPath_Type()
)
bootCnfgPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bootCnfgPath.setStatus("current")


class _BootCnfgExists_Type(TruthValue):
    """Custom type bootCnfgExists based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_BootCnfgExists_Type.__name__ = "TruthValue"
_BootCnfgExists_Object = MibScalar
bootCnfgExists = _BootCnfgExists_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 2, 2),
    _BootCnfgExists_Type()
)
bootCnfgExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bootCnfgExists.setStatus("current")
_DefaultConfig_ObjectIdentity = ObjectIdentity
defaultConfig = _DefaultConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3)
)
_DfltCnfgPath_Type = DisplayString
_DfltCnfgPath_Object = MibScalar
dfltCnfgPath = _DfltCnfgPath_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3, 1),
    _DfltCnfgPath_Type()
)
dfltCnfgPath.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfltCnfgPath.setStatus("current")


class _DfltCnfgExists_Type(TruthValue):
    """Custom type dfltCnfgExists based on TruthValue"""
    subtypeSpec = TruthValue.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_DfltCnfgExists_Type.__name__ = "TruthValue"
_DfltCnfgExists_Object = MibScalar
dfltCnfgExists = _DfltCnfgExists_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 3, 3, 2),
    _DfltCnfgExists_Type()
)
dfltCnfgExists.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dfltCnfgExists.setStatus("current")
_ServiceConfig_ObjectIdentity = ObjectIdentity
serviceConfig = _ServiceConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5)
)
_SrvcTelnetEnable_Type = TruthValue
_SrvcTelnetEnable_Object = MibScalar
srvcTelnetEnable = _SrvcTelnetEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5, 1),
    _SrvcTelnetEnable_Type()
)
srvcTelnetEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvcTelnetEnable.setStatus("current")
_SrvcSshEnable_Type = TruthValue
_SrvcSshEnable_Object = MibScalar
srvcSshEnable = _SrvcSshEnable_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 5, 2),
    _SrvcSshEnable_Type()
)
srvcSshEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    srvcSshEnable.setStatus("current")
_GuiConfig_ObjectIdentity = ObjectIdentity
guiConfig = _GuiConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6)
)
_GuiAppletConfig_ObjectIdentity = ObjectIdentity
guiAppletConfig = _GuiAppletConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1)
)
_GuiAppletSysSwVer_Type = DisplayString
_GuiAppletSysSwVer_Object = MibScalar
guiAppletSysSwVer = _GuiAppletSysSwVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1, 1),
    _GuiAppletSysSwVer_Type()
)
guiAppletSysSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    guiAppletSysSwVer.setStatus("current")
_GuiAppletSwVer_Type = DisplayString
_GuiAppletSwVer_Object = MibScalar
guiAppletSwVer = _GuiAppletSwVer_Object(
    (1, 3, 6, 1, 4, 1, 207, 8, 4, 4, 4, 500, 6, 1, 2),
    _GuiAppletSwVer_Type()
)
guiAppletSwVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    guiAppletSwVer.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AT-SETUP-MIB",
    **{"setup": setup,
       "restartDevice": restartDevice,
       "firmware": firmware,
       "currentFirmware": currentFirmware,
       "currSoftVersion": currSoftVersion,
       "currSoftName": currSoftName,
       "currSoftSaveAs": currSoftSaveAs,
       "nextBootFirmware": nextBootFirmware,
       "nextBootVersion": nextBootVersion,
       "nextBootPath": nextBootPath,
       "backupFirmware": backupFirmware,
       "backupVersion": backupVersion,
       "backupPath": backupPath,
       "deviceConfiguration": deviceConfiguration,
       "runningConfig": runningConfig,
       "runCnfgSaveAs": runCnfgSaveAs,
       "nextBootConfig": nextBootConfig,
       "bootCnfgPath": bootCnfgPath,
       "bootCnfgExists": bootCnfgExists,
       "defaultConfig": defaultConfig,
       "dfltCnfgPath": dfltCnfgPath,
       "dfltCnfgExists": dfltCnfgExists,
       "serviceConfig": serviceConfig,
       "srvcTelnetEnable": srvcTelnetEnable,
       "srvcSshEnable": srvcSshEnable,
       "guiConfig": guiConfig,
       "guiAppletConfig": guiAppletConfig,
       "guiAppletSysSwVer": guiAppletSysSwVer,
       "guiAppletSwVer": guiAppletSwVer}
)
