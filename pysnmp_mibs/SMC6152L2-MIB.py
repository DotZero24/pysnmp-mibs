# SNMP MIB module (SMC6152L2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/smc/SMC6152L2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:37:43 2025
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

(BridgeId,
 MacAddress,
 Timeout,
 dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "MacAddress",
    "Timeout",
    "dot1dStpPort",
    "dot1dStpPortEntry")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

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

smc6152L2MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66)
)
if mibBuilder.loadTexts:
    smc6152L2MIB.setRevisions(
        ("2006-12-07 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class KeySegment(DisplayString):
    status = "current"
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )



class ValidStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )



class StaPathCostMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("short", 1),
          ("long", 2))
    )



class FileCopyStatus(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31)
        )
    )
    namedValues = NamedValues(
        *(("fileCopyTftpUndefError", 1),
          ("fileCopyTftpFileNotFound", 2),
          ("fileCopyTftpAccessViolation", 3),
          ("fileCopyTftpDiskFull", 4),
          ("fileCopyTftpIllegalOperation", 5),
          ("fileCopyTftpUnkownTransferId", 6),
          ("fileCopyTftpFileExisted", 7),
          ("fileCopyTftpNoSuchUser", 8),
          ("fileCopyTftpTimeout", 9),
          ("fileCopyTftpSendError", 10),
          ("fileCopyTftpReceiverError", 11),
          ("fileCopyTftpSocketOpenError", 12),
          ("fileCopyTftpSocketBindError", 13),
          ("fileCopyTftpUserCancel", 14),
          ("fileCopyTftpCompleted", 15),
          ("fileCopyParaError", 16),
          ("fileCopyBusy", 17),
          ("fileCopyUnknown", 18),
          ("fileCopyReadFileError", 19),
          ("fileCopySetStartupError", 20),
          ("fileCopyFileSizeExceed", 21),
          ("fileCopyMagicWordError", 22),
          ("fileCopyImageTypeError", 23),
          ("fileCopyHeaderChecksumError", 24),
          ("fileCopyImageChecksumError", 25),
          ("fileCopyWriteFlashFinish", 26),
          ("fileCopyWriteFlashError", 27),
          ("fileCopyWriteFlashProgramming", 28),
          ("fileCopyError", 29),
          ("fileCopySuccess", 30),
          ("fileCopyCompleted", 31))
    )



# MIB Managed Objects in the order of their OIDs

_Smc_ObjectIdentity = ObjectIdentity
smc = _Smc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202)
)
_SmcSwitches_ObjectIdentity = ObjectIdentity
smcSwitches = _SmcSwitches_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20)
)
_Smc6152L2MIBObjects_ObjectIdentity = ObjectIdentity
smc6152L2MIBObjects = _Smc6152L2MIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1)
)
_SwitchMgt_ObjectIdentity = ObjectIdentity
switchMgt = _SwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1)
)


class _SwitchManagementVlan_Type(Integer32):
    """Custom type switchManagementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SwitchManagementVlan_Type.__name__ = "Integer32"
_SwitchManagementVlan_Object = MibScalar
switchManagementVlan = _SwitchManagementVlan_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 1),
    _SwitchManagementVlan_Type()
)
switchManagementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchManagementVlan.setStatus("current")
_SwitchNumber_Type = Integer32
_SwitchNumber_Object = MibScalar
switchNumber = _SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 2),
    _SwitchNumber_Type()
)
switchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumber.setStatus("current")
_SwitchInfoTable_Object = MibTable
switchInfoTable = _SwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3)
)
if mibBuilder.loadTexts:
    switchInfoTable.setStatus("current")
_SwitchInfoEntry_Object = MibTableRow
switchInfoEntry = _SwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1)
)
switchInfoEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "swUnitIndex"),
)
if mibBuilder.loadTexts:
    switchInfoEntry.setStatus("current")
_SwUnitIndex_Type = Integer32
_SwUnitIndex_Object = MibTableColumn
swUnitIndex = _SwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 1),
    _SwUnitIndex_Type()
)
swUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swUnitIndex.setStatus("current")


class _SwHardwareVer_Type(DisplayString):
    """Custom type swHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwHardwareVer_Type.__name__ = "DisplayString"
_SwHardwareVer_Object = MibTableColumn
swHardwareVer = _SwHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 2),
    _SwHardwareVer_Type()
)
swHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swHardwareVer.setStatus("current")


class _SwMicrocodeVer_Type(DisplayString):
    """Custom type swMicrocodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwMicrocodeVer_Type.__name__ = "DisplayString"
_SwMicrocodeVer_Object = MibTableColumn
swMicrocodeVer = _SwMicrocodeVer_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 3),
    _SwMicrocodeVer_Type()
)
swMicrocodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swMicrocodeVer.setStatus("current")


class _SwLoaderVer_Type(DisplayString):
    """Custom type swLoaderVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwLoaderVer_Type.__name__ = "DisplayString"
_SwLoaderVer_Object = MibTableColumn
swLoaderVer = _SwLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 4),
    _SwLoaderVer_Type()
)
swLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swLoaderVer.setStatus("current")


class _SwBootRomVer_Type(DisplayString):
    """Custom type swBootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwBootRomVer_Type.__name__ = "DisplayString"
_SwBootRomVer_Object = MibTableColumn
swBootRomVer = _SwBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 5),
    _SwBootRomVer_Type()
)
swBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swBootRomVer.setStatus("current")


class _SwOpCodeVer_Type(DisplayString):
    """Custom type swOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwOpCodeVer_Type.__name__ = "DisplayString"
_SwOpCodeVer_Object = MibTableColumn
swOpCodeVer = _SwOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 6),
    _SwOpCodeVer_Type()
)
swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOpCodeVer.setStatus("current")
_SwPortNumber_Type = Integer32
_SwPortNumber_Object = MibTableColumn
swPortNumber = _SwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 7),
    _SwPortNumber_Type()
)
swPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPortNumber.setStatus("current")


class _SwPowerStatus_Type(Integer32):
    """Custom type swPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("internalPower", 1),
          ("redundantPower", 2),
          ("internalAndRedundantPower", 3))
    )


_SwPowerStatus_Type.__name__ = "Integer32"
_SwPowerStatus_Object = MibTableColumn
swPowerStatus = _SwPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 8),
    _SwPowerStatus_Type()
)
swPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swPowerStatus.setStatus("current")


class _SwRoleInSystem_Type(Integer32):
    """Custom type swRoleInSystem based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("master", 1),
          ("backupMaster", 2),
          ("slave", 3))
    )


_SwRoleInSystem_Type.__name__ = "Integer32"
_SwRoleInSystem_Object = MibTableColumn
swRoleInSystem = _SwRoleInSystem_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 9),
    _SwRoleInSystem_Type()
)
swRoleInSystem.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swRoleInSystem.setStatus("current")


class _SwSerialNumber_Type(DisplayString):
    """Custom type swSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwSerialNumber_Type.__name__ = "DisplayString"
_SwSerialNumber_Object = MibTableColumn
swSerialNumber = _SwSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 10),
    _SwSerialNumber_Type()
)
swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNumber.setStatus("current")


class _SwServiceTag_Type(DisplayString):
    """Custom type swServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwServiceTag_Type.__name__ = "DisplayString"
_SwServiceTag_Object = MibTableColumn
swServiceTag = _SwServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 13),
    _SwServiceTag_Type()
)
swServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swServiceTag.setStatus("current")


class _SwModelNumber_Type(DisplayString):
    """Custom type swModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwModelNumber_Type.__name__ = "DisplayString"
_SwModelNumber_Object = MibTableColumn
swModelNumber = _SwModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 14),
    _SwModelNumber_Type()
)
swModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModelNumber.setStatus("current")


class _SwEpldVer_Type(DisplayString):
    """Custom type swEpldVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwEpldVer_Type.__name__ = "DisplayString"
_SwEpldVer_Object = MibTableColumn
swEpldVer = _SwEpldVer_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 3, 1, 15),
    _SwEpldVer_Type()
)
swEpldVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEpldVer.setStatus("current")


class _SwitchOperState_Type(Integer32):
    """Custom type switchOperState based on Integer32"""
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
        *(("other", 1),
          ("unknown", 2),
          ("ok", 3),
          ("noncritical", 4),
          ("critical", 5),
          ("nonrecoverable", 6))
    )


_SwitchOperState_Type.__name__ = "Integer32"
_SwitchOperState_Object = MibScalar
switchOperState = _SwitchOperState_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 4),
    _SwitchOperState_Type()
)
switchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchOperState.setStatus("current")
_SwitchProductId_ObjectIdentity = ObjectIdentity
switchProductId = _SwitchProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 5)
)


class _SwProdName_Type(DisplayString):
    """Custom type swProdName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdName_Type.__name__ = "DisplayString"
_SwProdName_Object = MibScalar
swProdName = _SwProdName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 5, 1),
    _SwProdName_Type()
)
swProdName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdName.setStatus("current")


class _SwProdManufacturer_Type(DisplayString):
    """Custom type swProdManufacturer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdManufacturer_Type.__name__ = "DisplayString"
_SwProdManufacturer_Object = MibScalar
swProdManufacturer = _SwProdManufacturer_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 5, 2),
    _SwProdManufacturer_Type()
)
swProdManufacturer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdManufacturer.setStatus("current")


class _SwProdDescription_Type(DisplayString):
    """Custom type swProdDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdDescription_Type.__name__ = "DisplayString"
_SwProdDescription_Object = MibScalar
swProdDescription = _SwProdDescription_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 5, 3),
    _SwProdDescription_Type()
)
swProdDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdDescription.setStatus("current")


class _SwProdVersion_Type(DisplayString):
    """Custom type swProdVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdVersion_Type.__name__ = "DisplayString"
_SwProdVersion_Object = MibScalar
swProdVersion = _SwProdVersion_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 5, 4),
    _SwProdVersion_Type()
)
swProdVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdVersion.setStatus("current")


class _SwProdUrl_Type(DisplayString):
    """Custom type swProdUrl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SwProdUrl_Type.__name__ = "DisplayString"
_SwProdUrl_Object = MibScalar
swProdUrl = _SwProdUrl_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 5, 5),
    _SwProdUrl_Type()
)
swProdUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdUrl.setStatus("current")
_SwIdentifier_Type = Integer32
_SwIdentifier_Object = MibScalar
swIdentifier = _SwIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 5, 6),
    _SwIdentifier_Type()
)
swIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIdentifier.setStatus("current")


class _SwChassisServiceTag_Type(DisplayString):
    """Custom type swChassisServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwChassisServiceTag_Type.__name__ = "DisplayString"
_SwChassisServiceTag_Object = MibScalar
swChassisServiceTag = _SwChassisServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 5, 7),
    _SwChassisServiceTag_Type()
)
swChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swChassisServiceTag.setStatus("current")
_SwitchIndivPowerTable_Object = MibTable
switchIndivPowerTable = _SwitchIndivPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 6)
)
if mibBuilder.loadTexts:
    switchIndivPowerTable.setStatus("current")
_SwitchIndivPowerEntry_Object = MibTableRow
switchIndivPowerEntry = _SwitchIndivPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 6, 1)
)
switchIndivPowerEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "swIndivPowerUnitIndex"),
    (0, "SMC6152L2-MIB", "swIndivPowerIndex"),
)
if mibBuilder.loadTexts:
    switchIndivPowerEntry.setStatus("current")
_SwIndivPowerUnitIndex_Type = Integer32
_SwIndivPowerUnitIndex_Object = MibTableColumn
swIndivPowerUnitIndex = _SwIndivPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 6, 1, 1),
    _SwIndivPowerUnitIndex_Type()
)
swIndivPowerUnitIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swIndivPowerUnitIndex.setStatus("current")


class _SwIndivPowerIndex_Type(Integer32):
    """Custom type swIndivPowerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internalPower", 1),
          ("externalPower", 2))
    )


_SwIndivPowerIndex_Type.__name__ = "Integer32"
_SwIndivPowerIndex_Object = MibTableColumn
swIndivPowerIndex = _SwIndivPowerIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 6, 1, 2),
    _SwIndivPowerIndex_Type()
)
swIndivPowerIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    swIndivPowerIndex.setStatus("current")


class _SwIndivPowerStatus_Type(Integer32):
    """Custom type swIndivPowerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("green", 2),
          ("red", 3))
    )


_SwIndivPowerStatus_Type.__name__ = "Integer32"
_SwIndivPowerStatus_Object = MibTableColumn
swIndivPowerStatus = _SwIndivPowerStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 6, 1, 3),
    _SwIndivPowerStatus_Type()
)
swIndivPowerStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swIndivPowerStatus.setStatus("current")


class _SwitchJumboFrameStatus_Type(Integer32):
    """Custom type switchJumboFrameStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_SwitchJumboFrameStatus_Type.__name__ = "Integer32"
_SwitchJumboFrameStatus_Object = MibScalar
switchJumboFrameStatus = _SwitchJumboFrameStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 7),
    _SwitchJumboFrameStatus_Type()
)
switchJumboFrameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchJumboFrameStatus.setStatus("current")
_AmtrMgt_ObjectIdentity = ObjectIdentity
amtrMgt = _AmtrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 8)
)
_AmtrMacAddrAgingStatus_Type = EnabledStatus
_AmtrMacAddrAgingStatus_Object = MibScalar
amtrMacAddrAgingStatus = _AmtrMacAddrAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 1, 8, 3),
    _AmtrMacAddrAgingStatus_Type()
)
amtrMacAddrAgingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amtrMacAddrAgingStatus.setStatus("current")
_PortMgt_ObjectIdentity = ObjectIdentity
portMgt = _PortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1)
)
portEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 2),
    _PortName_Type()
)
portName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portName.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("hundredBaseTX", 2),
          ("hundredBaseFX", 3),
          ("thousandBaseSX", 4),
          ("thousandBaseLX", 5),
          ("thousandBaseT", 6),
          ("thousandBaseGBIC", 7),
          ("thousandBaseSfp", 8),
          ("hundredBaseFxScSingleMode", 9),
          ("hundredBaseFxScMultiMode", 10),
          ("thousandBaseCX", 11),
          ("tenG", 12))
    )


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 3),
    _PortType_Type()
)
portType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portType.setStatus("current")


class _PortSpeedDpxCfg_Type(Integer32):
    """Custom type portSpeedDpxCfg based on Integer32"""
    defaultValue = 2

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("reserved", 1),
          ("halfDuplex10", 2),
          ("fullDuplex10", 3),
          ("halfDuplex100", 4),
          ("fullDuplex100", 5),
          ("halfDuplex1000", 6),
          ("fullDuplex1000", 7),
          ("halfDuplex10g", 8),
          ("fullDuplex10g", 9))
    )


_PortSpeedDpxCfg_Type.__name__ = "Integer32"
_PortSpeedDpxCfg_Object = MibTableColumn
portSpeedDpxCfg = _PortSpeedDpxCfg_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 4),
    _PortSpeedDpxCfg_Type()
)
portSpeedDpxCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedDpxCfg.setStatus("current")


class _PortFlowCtrlCfg_Type(Integer32):
    """Custom type portFlowCtrlCfg based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2),
          ("tx", 5),
          ("rx", 6))
    )


_PortFlowCtrlCfg_Type.__name__ = "Integer32"
_PortFlowCtrlCfg_Object = MibTableColumn
portFlowCtrlCfg = _PortFlowCtrlCfg_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 5),
    _PortFlowCtrlCfg_Type()
)
portFlowCtrlCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portFlowCtrlCfg.setStatus("current")


class _PortCapabilities_Type(Bits):
    """Custom type portCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("portCap10half", 0),
          ("portCap10full", 1),
          ("portCap100half", 2),
          ("portCap100full", 3),
          ("portCap1000half", 4),
          ("portCap1000full", 5),
          ("portCap10gHalf", 6),
          ("portCap10gFull", 7),
          ("reserved8", 8),
          ("reserved9", 9),
          ("reserved10", 10),
          ("reserved11", 11),
          ("reserved12", 12),
          ("reserved13", 13),
          ("portCapSym", 14),
          ("portCapFlowCtrl", 15))
    )

_PortCapabilities_Type.__name__ = "Bits"
_PortCapabilities_Object = MibTableColumn
portCapabilities = _PortCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("current")
_PortAutonegotiation_Type = EnabledStatus
_PortAutonegotiation_Object = MibTableColumn
portAutonegotiation = _PortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 7),
    _PortAutonegotiation_Type()
)
portAutonegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portAutonegotiation.setStatus("current")


class _PortSpeedDpxStatus_Type(Integer32):
    """Custom type portSpeedDpxStatus based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("error", 1),
          ("halfDuplex10", 2),
          ("fullDuplex10", 3),
          ("halfDuplex100", 4),
          ("fullDuplex100", 5),
          ("halfDuplex1000", 6),
          ("fullDuplex1000", 7),
          ("halfDuplex10g", 8),
          ("fullDuplex10g", 9))
    )


_PortSpeedDpxStatus_Type.__name__ = "Integer32"
_PortSpeedDpxStatus_Object = MibTableColumn
portSpeedDpxStatus = _PortSpeedDpxStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 8),
    _PortSpeedDpxStatus_Type()
)
portSpeedDpxStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portSpeedDpxStatus.setStatus("current")


class _PortFlowCtrlStatus_Type(Integer32):
    """Custom type portFlowCtrlStatus based on Integer32"""
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
        *(("error", 1),
          ("backPressure", 2),
          ("dot3xFlowControl", 3),
          ("none", 4))
    )


_PortFlowCtrlStatus_Type.__name__ = "Integer32"
_PortFlowCtrlStatus_Object = MibTableColumn
portFlowCtrlStatus = _PortFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")
_PortTrunkIndex_Type = Integer32
_PortTrunkIndex_Object = MibTableColumn
portTrunkIndex = _PortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 10),
    _PortTrunkIndex_Type()
)
portTrunkIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portTrunkIndex.setStatus("current")


class _PortComboForcedMode_Type(Integer32):
    """Custom type portComboForcedMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("copperForced", 2),
          ("copperPreferredAuto", 3),
          ("sfpForced", 4),
          ("sfpPreferredAuto", 5))
    )


_PortComboForcedMode_Type.__name__ = "Integer32"
_PortComboForcedMode_Object = MibTableColumn
portComboForcedMode = _PortComboForcedMode_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 2, 1, 1, 12),
    _PortComboForcedMode_Type()
)
portComboForcedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portComboForcedMode.setStatus("current")
_TrunkMgt_ObjectIdentity = ObjectIdentity
trunkMgt = _TrunkMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 3)
)
_TrunkMaxId_Type = Integer32
_TrunkMaxId_Object = MibScalar
trunkMaxId = _TrunkMaxId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 3, 1),
    _TrunkMaxId_Type()
)
trunkMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMaxId.setStatus("current")
_TrunkValidNumber_Type = Integer32
_TrunkValidNumber_Object = MibScalar
trunkValidNumber = _TrunkValidNumber_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 3, 2),
    _TrunkValidNumber_Type()
)
trunkValidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkValidNumber.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 3, 3)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 3, 3, 1)
)
trunkEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "trunkIndex"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")
_TrunkIndex_Type = Integer32
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 3, 3, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPorts_Type = PortList
_TrunkPorts_Object = MibTableColumn
trunkPorts = _TrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 3, 3, 1, 2),
    _TrunkPorts_Type()
)
trunkPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkPorts.setStatus("current")


class _TrunkCreation_Type(Integer32):
    """Custom type trunkCreation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("lacp", 2))
    )


_TrunkCreation_Type.__name__ = "Integer32"
_TrunkCreation_Object = MibTableColumn
trunkCreation = _TrunkCreation_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 3, 3, 1, 3),
    _TrunkCreation_Type()
)
trunkCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCreation.setStatus("current")
_TrunkStatus_Type = ValidStatus
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 3, 3, 1, 4),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")
_LacpMgt_ObjectIdentity = ObjectIdentity
lacpMgt = _LacpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 4)
)
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 4, 1, 1)
)
lacpPortEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "lacpPortIndex"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")
_LacpPortIndex_Type = Integer32
_LacpPortIndex_Object = MibTableColumn
lacpPortIndex = _LacpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 4, 1, 1, 1),
    _LacpPortIndex_Type()
)
lacpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lacpPortIndex.setStatus("current")
_LacpPortStatus_Type = EnabledStatus
_LacpPortStatus_Object = MibTableColumn
lacpPortStatus = _LacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 4, 1, 1, 2),
    _LacpPortStatus_Type()
)
lacpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortStatus.setStatus("current")
_StaMgt_ObjectIdentity = ObjectIdentity
staMgt = _StaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5)
)


class _StaSystemStatus_Type(EnabledStatus):
    """Custom type staSystemStatus based on EnabledStatus"""
    defaultValue = 1


_StaSystemStatus_Type.__name__ = "EnabledStatus"
_StaSystemStatus_Object = MibScalar
staSystemStatus = _StaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 1),
    _StaSystemStatus_Type()
)
staSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staSystemStatus.setStatus("current")
_StaPortTable_Object = MibTable
staPortTable = _StaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2)
)
if mibBuilder.loadTexts:
    staPortTable.setStatus("current")
_StaPortEntry_Object = MibTableRow
staPortEntry = _StaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    staPortEntry.setStatus("current")
_StaPortFastForward_Type = EnabledStatus
_StaPortFastForward_Object = MibTableColumn
staPortFastForward = _StaPortFastForward_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2, 1, 2),
    _StaPortFastForward_Type()
)
staPortFastForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortFastForward.setStatus("current")
_StaPortProtocolMigration_Type = TruthValue
_StaPortProtocolMigration_Object = MibTableColumn
staPortProtocolMigration = _StaPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2, 1, 3),
    _StaPortProtocolMigration_Type()
)
staPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortProtocolMigration.setStatus("current")
_StaPortAdminEdgePort_Type = TruthValue
_StaPortAdminEdgePort_Object = MibTableColumn
staPortAdminEdgePort = _StaPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2, 1, 4),
    _StaPortAdminEdgePort_Type()
)
staPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminEdgePort.setStatus("current")
_StaPortOperEdgePort_Type = TruthValue
_StaPortOperEdgePort_Object = MibTableColumn
staPortOperEdgePort = _StaPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2, 1, 5),
    _StaPortOperEdgePort_Type()
)
staPortOperEdgePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperEdgePort.setStatus("current")


class _StaPortAdminPointToPoint_Type(Integer32):
    """Custom type staPortAdminPointToPoint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("forceTrue", 0),
          ("forceFalse", 1),
          ("auto", 2))
    )


_StaPortAdminPointToPoint_Type.__name__ = "Integer32"
_StaPortAdminPointToPoint_Object = MibTableColumn
staPortAdminPointToPoint = _StaPortAdminPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2, 1, 6),
    _StaPortAdminPointToPoint_Type()
)
staPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminPointToPoint.setStatus("current")
_StaPortOperPointToPoint_Type = TruthValue
_StaPortOperPointToPoint_Object = MibTableColumn
staPortOperPointToPoint = _StaPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2, 1, 7),
    _StaPortOperPointToPoint_Type()
)
staPortOperPointToPoint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortOperPointToPoint.setStatus("current")


class _StaPortSystemStatus_Type(EnabledStatus):
    """Custom type staPortSystemStatus based on EnabledStatus"""
    defaultValue = 1


_StaPortSystemStatus_Type.__name__ = "EnabledStatus"
_StaPortSystemStatus_Object = MibTableColumn
staPortSystemStatus = _StaPortSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2, 1, 9),
    _StaPortSystemStatus_Type()
)
staPortSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortSystemStatus.setStatus("current")


class _StaPortLongAdminPathCost_Type(Integer32):
    """Custom type staPortLongAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200000000),
    )


_StaPortLongAdminPathCost_Type.__name__ = "Integer32"
_StaPortLongAdminPathCost_Object = MibTableColumn
staPortLongAdminPathCost = _StaPortLongAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2, 1, 10),
    _StaPortLongAdminPathCost_Type()
)
staPortLongAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortLongAdminPathCost.setStatus("current")


class _StaPortLongOperPathCost_Type(Integer32):
    """Custom type staPortLongOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StaPortLongOperPathCost_Type.__name__ = "Integer32"
_StaPortLongOperPathCost_Object = MibTableColumn
staPortLongOperPathCost = _StaPortLongOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 2, 1, 11),
    _StaPortLongOperPathCost_Type()
)
staPortLongOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortLongOperPathCost.setStatus("current")


class _StaProtocolType_Type(Integer32):
    """Custom type staProtocolType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stp", 1),
          ("rstp", 2),
          ("mstp", 3))
    )


_StaProtocolType_Type.__name__ = "Integer32"
_StaProtocolType_Object = MibScalar
staProtocolType = _StaProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 3),
    _StaProtocolType_Type()
)
staProtocolType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staProtocolType.setStatus("current")


class _StaTxHoldCount_Type(Integer32):
    """Custom type staTxHoldCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_StaTxHoldCount_Type.__name__ = "Integer32"
_StaTxHoldCount_Object = MibScalar
staTxHoldCount = _StaTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 4),
    _StaTxHoldCount_Type()
)
staTxHoldCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staTxHoldCount.setStatus("current")


class _StaPathCostMethod_Type(StaPathCostMode):
    """Custom type staPathCostMethod based on StaPathCostMode"""
    defaultValue = 1


_StaPathCostMethod_Type.__name__ = "StaPathCostMode"
_StaPathCostMethod_Object = MibScalar
staPathCostMethod = _StaPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 5, 5),
    _StaPathCostMethod_Type()
)
staPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPathCostMethod.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 7)
)


class _RestartOpCodeFile_Type(DisplayString):
    """Custom type restartOpCodeFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RestartOpCodeFile_Type.__name__ = "DisplayString"
_RestartOpCodeFile_Object = MibScalar
restartOpCodeFile = _RestartOpCodeFile_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 7, 1),
    _RestartOpCodeFile_Type()
)
restartOpCodeFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartOpCodeFile.setStatus("current")


class _RestartConfigFile_Type(DisplayString):
    """Custom type restartConfigFile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_RestartConfigFile_Type.__name__ = "DisplayString"
_RestartConfigFile_Object = MibScalar
restartConfigFile = _RestartConfigFile_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 7, 2),
    _RestartConfigFile_Type()
)
restartConfigFile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartConfigFile.setStatus("current")


class _RestartControl_Type(Integer32):
    """Custom type restartControl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("running", 1),
          ("warmBoot", 2),
          ("coldBoot", 3))
    )


_RestartControl_Type.__name__ = "Integer32"
_RestartControl_Object = MibScalar
restartControl = _RestartControl_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 7, 3),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_MirrorMgt_ObjectIdentity = ObjectIdentity
mirrorMgt = _MirrorMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 8)
)
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 8, 1, 1)
)
mirrorEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "mirrorDestinationPort"),
    (0, "SMC6152L2-MIB", "mirrorSourcePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")
_MirrorDestinationPort_Type = Integer32
_MirrorDestinationPort_Object = MibTableColumn
mirrorDestinationPort = _MirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 8, 1, 1, 1),
    _MirrorDestinationPort_Type()
)
mirrorDestinationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mirrorDestinationPort.setStatus("current")
_MirrorSourcePort_Type = Integer32
_MirrorSourcePort_Object = MibTableColumn
mirrorSourcePort = _MirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 8, 1, 1, 2),
    _MirrorSourcePort_Type()
)
mirrorSourcePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mirrorSourcePort.setStatus("current")


class _MirrorType_Type(Integer32):
    """Custom type mirrorType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("rx", 1),
          ("tx", 2),
          ("both", 3))
    )


_MirrorType_Type.__name__ = "Integer32"
_MirrorType_Object = MibTableColumn
mirrorType = _MirrorType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 8, 1, 1, 3),
    _MirrorType_Type()
)
mirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorType.setStatus("current")
_MirrorStatus_Type = ValidStatus
_MirrorStatus_Object = MibTableColumn
mirrorStatus = _MirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 8, 1, 1, 4),
    _MirrorStatus_Type()
)
mirrorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorStatus.setStatus("current")
_IgmpSnoopMgt_ObjectIdentity = ObjectIdentity
igmpSnoopMgt = _IgmpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9)
)


class _IgmpSnoopStatus_Type(EnabledStatus):
    """Custom type igmpSnoopStatus based on EnabledStatus"""
    defaultValue = 1


_IgmpSnoopStatus_Type.__name__ = "EnabledStatus"
_IgmpSnoopStatus_Object = MibScalar
igmpSnoopStatus = _IgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 1),
    _IgmpSnoopStatus_Type()
)
igmpSnoopStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopStatus.setStatus("current")


class _IgmpSnoopQuerier_Type(EnabledStatus):
    """Custom type igmpSnoopQuerier based on EnabledStatus"""
    defaultValue = 1


_IgmpSnoopQuerier_Type.__name__ = "EnabledStatus"
_IgmpSnoopQuerier_Object = MibScalar
igmpSnoopQuerier = _IgmpSnoopQuerier_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 2),
    _IgmpSnoopQuerier_Type()
)
igmpSnoopQuerier.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQuerier.setStatus("current")


class _IgmpSnoopQueryCount_Type(Integer32):
    """Custom type igmpSnoopQueryCount based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_IgmpSnoopQueryCount_Type.__name__ = "Integer32"
_IgmpSnoopQueryCount_Object = MibScalar
igmpSnoopQueryCount = _IgmpSnoopQueryCount_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 3),
    _IgmpSnoopQueryCount_Type()
)
igmpSnoopQueryCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryCount.setStatus("current")


class _IgmpSnoopQueryInterval_Type(Integer32):
    """Custom type igmpSnoopQueryInterval based on Integer32"""
    defaultValue = 125

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 125),
    )


_IgmpSnoopQueryInterval_Type.__name__ = "Integer32"
_IgmpSnoopQueryInterval_Object = MibScalar
igmpSnoopQueryInterval = _IgmpSnoopQueryInterval_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 4),
    _IgmpSnoopQueryInterval_Type()
)
igmpSnoopQueryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryInterval.setStatus("current")


class _IgmpSnoopQueryMaxResponseTime_Type(Integer32):
    """Custom type igmpSnoopQueryMaxResponseTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 25),
    )


_IgmpSnoopQueryMaxResponseTime_Type.__name__ = "Integer32"
_IgmpSnoopQueryMaxResponseTime_Object = MibScalar
igmpSnoopQueryMaxResponseTime = _IgmpSnoopQueryMaxResponseTime_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 5),
    _IgmpSnoopQueryMaxResponseTime_Type()
)
igmpSnoopQueryMaxResponseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopQueryMaxResponseTime.setStatus("current")


class _IgmpSnoopRouterPortExpireTime_Type(Integer32):
    """Custom type igmpSnoopRouterPortExpireTime based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 500),
    )


_IgmpSnoopRouterPortExpireTime_Type.__name__ = "Integer32"
_IgmpSnoopRouterPortExpireTime_Object = MibScalar
igmpSnoopRouterPortExpireTime = _IgmpSnoopRouterPortExpireTime_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 6),
    _IgmpSnoopRouterPortExpireTime_Type()
)
igmpSnoopRouterPortExpireTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopRouterPortExpireTime.setStatus("current")


class _IgmpSnoopVersion_Type(Integer32):
    """Custom type igmpSnoopVersion based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_IgmpSnoopVersion_Type.__name__ = "Integer32"
_IgmpSnoopVersion_Object = MibScalar
igmpSnoopVersion = _IgmpSnoopVersion_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 7),
    _IgmpSnoopVersion_Type()
)
igmpSnoopVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopVersion.setStatus("current")
_IgmpSnoopRouterCurrentTable_Object = MibTable
igmpSnoopRouterCurrentTable = _IgmpSnoopRouterCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 8)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentTable.setStatus("current")
_IgmpSnoopRouterCurrentEntry_Object = MibTableRow
igmpSnoopRouterCurrentEntry = _IgmpSnoopRouterCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 8, 1)
)
igmpSnoopRouterCurrentEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "igmpSnoopRouterCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentEntry.setStatus("current")
_IgmpSnoopRouterCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object = MibTableColumn
igmpSnoopRouterCurrentVlanIndex = _IgmpSnoopRouterCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 8, 1, 1),
    _IgmpSnoopRouterCurrentVlanIndex_Type()
)
igmpSnoopRouterCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentVlanIndex.setStatus("current")
_IgmpSnoopRouterCurrentPorts_Type = PortList
_IgmpSnoopRouterCurrentPorts_Object = MibTableColumn
igmpSnoopRouterCurrentPorts = _IgmpSnoopRouterCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 8, 1, 2),
    _IgmpSnoopRouterCurrentPorts_Type()
)
igmpSnoopRouterCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentPorts.setStatus("current")
_IgmpSnoopRouterCurrentStatus_Type = PortList
_IgmpSnoopRouterCurrentStatus_Object = MibTableColumn
igmpSnoopRouterCurrentStatus = _IgmpSnoopRouterCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 8, 1, 3),
    _IgmpSnoopRouterCurrentStatus_Type()
)
igmpSnoopRouterCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentStatus.setStatus("current")
_IgmpSnoopRouterStaticTable_Object = MibTable
igmpSnoopRouterStaticTable = _IgmpSnoopRouterStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 9)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticTable.setStatus("current")
_IgmpSnoopRouterStaticEntry_Object = MibTableRow
igmpSnoopRouterStaticEntry = _IgmpSnoopRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 9, 1)
)
igmpSnoopRouterStaticEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "igmpSnoopRouterStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticEntry.setStatus("current")
_IgmpSnoopRouterStaticVlanIndex_Type = Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object = MibTableColumn
igmpSnoopRouterStaticVlanIndex = _IgmpSnoopRouterStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 9, 1, 1),
    _IgmpSnoopRouterStaticVlanIndex_Type()
)
igmpSnoopRouterStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticVlanIndex.setStatus("current")
_IgmpSnoopRouterStaticPorts_Type = PortList
_IgmpSnoopRouterStaticPorts_Object = MibTableColumn
igmpSnoopRouterStaticPorts = _IgmpSnoopRouterStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 9, 1, 2),
    _IgmpSnoopRouterStaticPorts_Type()
)
igmpSnoopRouterStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticPorts.setStatus("current")
_IgmpSnoopRouterStaticStatus_Type = ValidStatus
_IgmpSnoopRouterStaticStatus_Object = MibTableColumn
igmpSnoopRouterStaticStatus = _IgmpSnoopRouterStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 9, 1, 3),
    _IgmpSnoopRouterStaticStatus_Type()
)
igmpSnoopRouterStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticStatus.setStatus("current")
_IgmpSnoopMulticastCurrentTable_Object = MibTable
igmpSnoopMulticastCurrentTable = _IgmpSnoopMulticastCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 10)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentTable.setStatus("current")
_IgmpSnoopMulticastCurrentEntry_Object = MibTableRow
igmpSnoopMulticastCurrentEntry = _IgmpSnoopMulticastCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 10, 1)
)
igmpSnoopMulticastCurrentEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "igmpSnoopMulticastCurrentVlanIndex"),
    (0, "SMC6152L2-MIB", "igmpSnoopMulticastCurrentIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentEntry.setStatus("current")
_IgmpSnoopMulticastCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastCurrentVlanIndex_Object = MibTableColumn
igmpSnoopMulticastCurrentVlanIndex = _IgmpSnoopMulticastCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 10, 1, 1),
    _IgmpSnoopMulticastCurrentVlanIndex_Type()
)
igmpSnoopMulticastCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentVlanIndex.setStatus("current")
_IgmpSnoopMulticastCurrentIpAddress_Type = IpAddress
_IgmpSnoopMulticastCurrentIpAddress_Object = MibTableColumn
igmpSnoopMulticastCurrentIpAddress = _IgmpSnoopMulticastCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 10, 1, 2),
    _IgmpSnoopMulticastCurrentIpAddress_Type()
)
igmpSnoopMulticastCurrentIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentIpAddress.setStatus("current")
_IgmpSnoopMulticastCurrentPorts_Type = PortList
_IgmpSnoopMulticastCurrentPorts_Object = MibTableColumn
igmpSnoopMulticastCurrentPorts = _IgmpSnoopMulticastCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 10, 1, 3),
    _IgmpSnoopMulticastCurrentPorts_Type()
)
igmpSnoopMulticastCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentPorts.setStatus("current")
_IgmpSnoopMulticastCurrentStatus_Type = PortList
_IgmpSnoopMulticastCurrentStatus_Object = MibTableColumn
igmpSnoopMulticastCurrentStatus = _IgmpSnoopMulticastCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 10, 1, 4),
    _IgmpSnoopMulticastCurrentStatus_Type()
)
igmpSnoopMulticastCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentStatus.setStatus("current")
_IgmpSnoopMulticastStaticTable_Object = MibTable
igmpSnoopMulticastStaticTable = _IgmpSnoopMulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 11)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticTable.setStatus("current")
_IgmpSnoopMulticastStaticEntry_Object = MibTableRow
igmpSnoopMulticastStaticEntry = _IgmpSnoopMulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 11, 1)
)
igmpSnoopMulticastStaticEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "igmpSnoopMulticastStaticVlanIndex"),
    (0, "SMC6152L2-MIB", "igmpSnoopMulticastStaticIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticEntry.setStatus("current")
_IgmpSnoopMulticastStaticVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object = MibTableColumn
igmpSnoopMulticastStaticVlanIndex = _IgmpSnoopMulticastStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 11, 1, 1),
    _IgmpSnoopMulticastStaticVlanIndex_Type()
)
igmpSnoopMulticastStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticVlanIndex.setStatus("current")
_IgmpSnoopMulticastStaticIpAddress_Type = IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object = MibTableColumn
igmpSnoopMulticastStaticIpAddress = _IgmpSnoopMulticastStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 11, 1, 2),
    _IgmpSnoopMulticastStaticIpAddress_Type()
)
igmpSnoopMulticastStaticIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticIpAddress.setStatus("current")
_IgmpSnoopMulticastStaticPorts_Type = PortList
_IgmpSnoopMulticastStaticPorts_Object = MibTableColumn
igmpSnoopMulticastStaticPorts = _IgmpSnoopMulticastStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 11, 1, 3),
    _IgmpSnoopMulticastStaticPorts_Type()
)
igmpSnoopMulticastStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticPorts.setStatus("current")
_IgmpSnoopMulticastStaticStatus_Type = ValidStatus
_IgmpSnoopMulticastStaticStatus_Object = MibTableColumn
igmpSnoopMulticastStaticStatus = _IgmpSnoopMulticastStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 11, 1, 4),
    _IgmpSnoopMulticastStaticStatus_Type()
)
igmpSnoopMulticastStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticStatus.setStatus("current")
_IgmpSnoopCurrentVlanTable_Object = MibTable
igmpSnoopCurrentVlanTable = _IgmpSnoopCurrentVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 14)
)
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanTable.setStatus("current")
_IgmpSnoopCurrentVlanEntry_Object = MibTableRow
igmpSnoopCurrentVlanEntry = _IgmpSnoopCurrentVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 14, 1)
)
igmpSnoopCurrentVlanEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "igmpSnoopCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanEntry.setStatus("current")
_IgmpSnoopCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopCurrentVlanIndex_Object = MibTableColumn
igmpSnoopCurrentVlanIndex = _IgmpSnoopCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 14, 1, 1),
    _IgmpSnoopCurrentVlanIndex_Type()
)
igmpSnoopCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanIndex.setStatus("current")
_IgmpSnoopCurrentVlanImmediateLeave_Type = EnabledStatus
_IgmpSnoopCurrentVlanImmediateLeave_Object = MibTableColumn
igmpSnoopCurrentVlanImmediateLeave = _IgmpSnoopCurrentVlanImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 14, 1, 3),
    _IgmpSnoopCurrentVlanImmediateLeave_Type()
)
igmpSnoopCurrentVlanImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanImmediateLeave.setStatus("current")
_IgmpSnoopLeaveProxy_Type = EnabledStatus
_IgmpSnoopLeaveProxy_Object = MibScalar
igmpSnoopLeaveProxy = _IgmpSnoopLeaveProxy_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 15),
    _IgmpSnoopLeaveProxy_Type()
)
igmpSnoopLeaveProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopLeaveProxy.setStatus("current")
_IgmpSnoopFilterStatus_Type = EnabledStatus
_IgmpSnoopFilterStatus_Object = MibScalar
igmpSnoopFilterStatus = _IgmpSnoopFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 17),
    _IgmpSnoopFilterStatus_Type()
)
igmpSnoopFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopFilterStatus.setStatus("current")
_IgmpSnoopProfileTable_Object = MibTable
igmpSnoopProfileTable = _IgmpSnoopProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 18)
)
if mibBuilder.loadTexts:
    igmpSnoopProfileTable.setStatus("current")
_IgmpSnoopProfileEntry_Object = MibTableRow
igmpSnoopProfileEntry = _IgmpSnoopProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 18, 1)
)
igmpSnoopProfileEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "igmpSnoopProfileId"),
)
if mibBuilder.loadTexts:
    igmpSnoopProfileEntry.setStatus("current")
_IgmpSnoopProfileId_Type = Unsigned32
_IgmpSnoopProfileId_Object = MibTableColumn
igmpSnoopProfileId = _IgmpSnoopProfileId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 18, 1, 1),
    _IgmpSnoopProfileId_Type()
)
igmpSnoopProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileId.setStatus("current")


class _IgmpSnoopProfileAction_Type(Integer32):
    """Custom type igmpSnoopProfileAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_IgmpSnoopProfileAction_Type.__name__ = "Integer32"
_IgmpSnoopProfileAction_Object = MibTableColumn
igmpSnoopProfileAction = _IgmpSnoopProfileAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 18, 1, 2),
    _IgmpSnoopProfileAction_Type()
)
igmpSnoopProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileAction.setStatus("current")
_IgmpSnoopProfileStatus_Type = ValidStatus
_IgmpSnoopProfileStatus_Object = MibTableColumn
igmpSnoopProfileStatus = _IgmpSnoopProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 18, 1, 3),
    _IgmpSnoopProfileStatus_Type()
)
igmpSnoopProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileStatus.setStatus("current")
_IgmpSnoopProfileCtl_ObjectIdentity = ObjectIdentity
igmpSnoopProfileCtl = _IgmpSnoopProfileCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 19)
)
_IgmpSnoopProfileCtlId_Type = Unsigned32
_IgmpSnoopProfileCtlId_Object = MibScalar
igmpSnoopProfileCtlId = _IgmpSnoopProfileCtlId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 19, 1),
    _IgmpSnoopProfileCtlId_Type()
)
igmpSnoopProfileCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlId.setStatus("current")
_IgmpSnoopProfileCtlInetAddressType_Type = InetAddressType
_IgmpSnoopProfileCtlInetAddressType_Object = MibScalar
igmpSnoopProfileCtlInetAddressType = _IgmpSnoopProfileCtlInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 19, 2),
    _IgmpSnoopProfileCtlInetAddressType_Type()
)
igmpSnoopProfileCtlInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlInetAddressType.setStatus("current")
_IgmpSnoopProfileCtlStartInetAddress_Type = InetAddress
_IgmpSnoopProfileCtlStartInetAddress_Object = MibScalar
igmpSnoopProfileCtlStartInetAddress = _IgmpSnoopProfileCtlStartInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 19, 3),
    _IgmpSnoopProfileCtlStartInetAddress_Type()
)
igmpSnoopProfileCtlStartInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlStartInetAddress.setStatus("current")
_IgmpSnoopProfileCtlEndInetAddress_Type = InetAddress
_IgmpSnoopProfileCtlEndInetAddress_Object = MibScalar
igmpSnoopProfileCtlEndInetAddress = _IgmpSnoopProfileCtlEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 19, 4),
    _IgmpSnoopProfileCtlEndInetAddress_Type()
)
igmpSnoopProfileCtlEndInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlEndInetAddress.setStatus("current")


class _IgmpSnoopProfileCtlAction_Type(Integer32):
    """Custom type igmpSnoopProfileCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("create", 2),
          ("destroy", 3))
    )


_IgmpSnoopProfileCtlAction_Type.__name__ = "Integer32"
_IgmpSnoopProfileCtlAction_Object = MibScalar
igmpSnoopProfileCtlAction = _IgmpSnoopProfileCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 19, 5),
    _IgmpSnoopProfileCtlAction_Type()
)
igmpSnoopProfileCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlAction.setStatus("current")
_IgmpSnoopProfileRangeTable_Object = MibTable
igmpSnoopProfileRangeTable = _IgmpSnoopProfileRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 20)
)
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeTable.setStatus("current")
_IgmpSnoopProfileRangeEntry_Object = MibTableRow
igmpSnoopProfileRangeEntry = _IgmpSnoopProfileRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 20, 1)
)
igmpSnoopProfileRangeEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "igmpSnoopProfileRangeProfileId"),
    (0, "SMC6152L2-MIB", "igmpSnoopProfileRangeInetAddressType"),
    (0, "SMC6152L2-MIB", "igmpSnoopProfileRangeStartInetAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeEntry.setStatus("current")
_IgmpSnoopProfileRangeProfileId_Type = Unsigned32
_IgmpSnoopProfileRangeProfileId_Object = MibTableColumn
igmpSnoopProfileRangeProfileId = _IgmpSnoopProfileRangeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 20, 1, 1),
    _IgmpSnoopProfileRangeProfileId_Type()
)
igmpSnoopProfileRangeProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeProfileId.setStatus("current")
_IgmpSnoopProfileRangeInetAddressType_Type = InetAddressType
_IgmpSnoopProfileRangeInetAddressType_Object = MibTableColumn
igmpSnoopProfileRangeInetAddressType = _IgmpSnoopProfileRangeInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 20, 1, 2),
    _IgmpSnoopProfileRangeInetAddressType_Type()
)
igmpSnoopProfileRangeInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeInetAddressType.setStatus("current")
_IgmpSnoopProfileRangeStartInetAddress_Type = InetAddress
_IgmpSnoopProfileRangeStartInetAddress_Object = MibTableColumn
igmpSnoopProfileRangeStartInetAddress = _IgmpSnoopProfileRangeStartInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 20, 1, 3),
    _IgmpSnoopProfileRangeStartInetAddress_Type()
)
igmpSnoopProfileRangeStartInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeStartInetAddress.setStatus("current")
_IgmpSnoopProfileRangeEndInetAddress_Type = InetAddress
_IgmpSnoopProfileRangeEndInetAddress_Object = MibTableColumn
igmpSnoopProfileRangeEndInetAddress = _IgmpSnoopProfileRangeEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 20, 1, 4),
    _IgmpSnoopProfileRangeEndInetAddress_Type()
)
igmpSnoopProfileRangeEndInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeEndInetAddress.setStatus("current")


class _IgmpSnoopProfileRangeAction_Type(Integer32):
    """Custom type igmpSnoopProfileRangeAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_IgmpSnoopProfileRangeAction_Type.__name__ = "Integer32"
_IgmpSnoopProfileRangeAction_Object = MibTableColumn
igmpSnoopProfileRangeAction = _IgmpSnoopProfileRangeAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 20, 1, 5),
    _IgmpSnoopProfileRangeAction_Type()
)
igmpSnoopProfileRangeAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeAction.setStatus("current")
_IgmpSnoopFilterPortTable_Object = MibTable
igmpSnoopFilterPortTable = _IgmpSnoopFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 21)
)
if mibBuilder.loadTexts:
    igmpSnoopFilterPortTable.setStatus("current")
_IgmpSnoopFilterPortEntry_Object = MibTableRow
igmpSnoopFilterPortEntry = _IgmpSnoopFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 21, 1)
)
igmpSnoopFilterPortEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "igmpSnoopFilterPortIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopFilterPortEntry.setStatus("current")
_IgmpSnoopFilterPortIndex_Type = Unsigned32
_IgmpSnoopFilterPortIndex_Object = MibTableColumn
igmpSnoopFilterPortIndex = _IgmpSnoopFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 21, 1, 1),
    _IgmpSnoopFilterPortIndex_Type()
)
igmpSnoopFilterPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopFilterPortIndex.setStatus("current")
_IgmpSnoopFilterPortProfileId_Type = Integer32
_IgmpSnoopFilterPortProfileId_Object = MibTableColumn
igmpSnoopFilterPortProfileId = _IgmpSnoopFilterPortProfileId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 21, 1, 2),
    _IgmpSnoopFilterPortProfileId_Type()
)
igmpSnoopFilterPortProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopFilterPortProfileId.setStatus("current")
_IgmpSnoopThrottlePortTable_Object = MibTable
igmpSnoopThrottlePortTable = _IgmpSnoopThrottlePortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 22)
)
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortTable.setStatus("current")
_IgmpSnoopThrottlePortEntry_Object = MibTableRow
igmpSnoopThrottlePortEntry = _IgmpSnoopThrottlePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 22, 1)
)
igmpSnoopThrottlePortEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "igmpSnoopThrottlePortIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortEntry.setStatus("current")
_IgmpSnoopThrottlePortIndex_Type = Unsigned32
_IgmpSnoopThrottlePortIndex_Object = MibTableColumn
igmpSnoopThrottlePortIndex = _IgmpSnoopThrottlePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 22, 1, 1),
    _IgmpSnoopThrottlePortIndex_Type()
)
igmpSnoopThrottlePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortIndex.setStatus("current")
_IgmpSnoopThrottlePortRunningStatus_Type = TruthValue
_IgmpSnoopThrottlePortRunningStatus_Object = MibTableColumn
igmpSnoopThrottlePortRunningStatus = _IgmpSnoopThrottlePortRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 22, 1, 2),
    _IgmpSnoopThrottlePortRunningStatus_Type()
)
igmpSnoopThrottlePortRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortRunningStatus.setStatus("current")


class _IgmpSnoopThrottlePortAction_Type(Integer32):
    """Custom type igmpSnoopThrottlePortAction based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("replace", 1),
          ("deny", 2))
    )


_IgmpSnoopThrottlePortAction_Type.__name__ = "Integer32"
_IgmpSnoopThrottlePortAction_Object = MibTableColumn
igmpSnoopThrottlePortAction = _IgmpSnoopThrottlePortAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 22, 1, 3),
    _IgmpSnoopThrottlePortAction_Type()
)
igmpSnoopThrottlePortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortAction.setStatus("current")


class _IgmpSnoopThrottlePortMaxGroups_Type(Integer32):
    """Custom type igmpSnoopThrottlePortMaxGroups based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_IgmpSnoopThrottlePortMaxGroups_Type.__name__ = "Integer32"
_IgmpSnoopThrottlePortMaxGroups_Object = MibTableColumn
igmpSnoopThrottlePortMaxGroups = _IgmpSnoopThrottlePortMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 22, 1, 4),
    _IgmpSnoopThrottlePortMaxGroups_Type()
)
igmpSnoopThrottlePortMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortMaxGroups.setStatus("current")
_IgmpSnoopThrottlePortCurrentGroups_Type = Integer32
_IgmpSnoopThrottlePortCurrentGroups_Object = MibTableColumn
igmpSnoopThrottlePortCurrentGroups = _IgmpSnoopThrottlePortCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 9, 22, 1, 5),
    _IgmpSnoopThrottlePortCurrentGroups_Type()
)
igmpSnoopThrottlePortCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortCurrentGroups.setStatus("current")
_IpMgt_ObjectIdentity = ObjectIdentity
ipMgt = _IpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10)
)
_NetConfigTable_Object = MibTable
netConfigTable = _NetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 1)
)
if mibBuilder.loadTexts:
    netConfigTable.setStatus("current")
_NetConfigEntry_Object = MibTableRow
netConfigEntry = _NetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 1, 1)
)
netConfigEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "netConfigIfIndex"),
    (0, "SMC6152L2-MIB", "netConfigIPAddress"),
    (0, "SMC6152L2-MIB", "netConfigSubnetMask"),
)
if mibBuilder.loadTexts:
    netConfigEntry.setStatus("current")
_NetConfigIfIndex_Type = Integer32
_NetConfigIfIndex_Object = MibTableColumn
netConfigIfIndex = _NetConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 1, 1, 1),
    _NetConfigIfIndex_Type()
)
netConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigIfIndex.setStatus("current")
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibTableColumn
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 1, 1, 2),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("current")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibTableColumn
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 1, 1, 3),
    _NetConfigSubnetMask_Type()
)
netConfigSubnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigSubnetMask.setStatus("current")


class _NetConfigPrimaryInterface_Type(Integer32):
    """Custom type netConfigPrimaryInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("secondary", 2))
    )


_NetConfigPrimaryInterface_Type.__name__ = "Integer32"
_NetConfigPrimaryInterface_Object = MibTableColumn
netConfigPrimaryInterface = _NetConfigPrimaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 1, 1, 4),
    _NetConfigPrimaryInterface_Type()
)
netConfigPrimaryInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigPrimaryInterface.setStatus("current")


class _NetConfigUnnumbered_Type(Integer32):
    """Custom type netConfigUnnumbered based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unnumbered", 1),
          ("notUnnumbered", 2))
    )


_NetConfigUnnumbered_Type.__name__ = "Integer32"
_NetConfigUnnumbered_Object = MibTableColumn
netConfigUnnumbered = _NetConfigUnnumbered_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 1, 1, 5),
    _NetConfigUnnumbered_Type()
)
netConfigUnnumbered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigUnnumbered.setStatus("current")
_NetConfigStatus_Type = RowStatus
_NetConfigStatus_Object = MibTableColumn
netConfigStatus = _NetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 1, 1, 6),
    _NetConfigStatus_Type()
)
netConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigStatus.setStatus("current")
_NetDefaultGateway_Type = IpAddress
_NetDefaultGateway_Object = MibScalar
netDefaultGateway = _NetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 2),
    _NetDefaultGateway_Type()
)
netDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDefaultGateway.setStatus("current")
_IpHttpState_Type = EnabledStatus
_IpHttpState_Object = MibScalar
ipHttpState = _IpHttpState_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 3),
    _IpHttpState_Type()
)
ipHttpState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpState.setStatus("current")


class _IpHttpPort_Type(Integer32):
    """Custom type ipHttpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpHttpPort_Type.__name__ = "Integer32"
_IpHttpPort_Object = MibScalar
ipHttpPort = _IpHttpPort_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 4),
    _IpHttpPort_Type()
)
ipHttpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpPort.setStatus("current")


class _IpDhcpRestart_Type(Integer32):
    """Custom type ipDhcpRestart based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restart", 1),
          ("noRestart", 2))
    )


_IpDhcpRestart_Type.__name__ = "Integer32"
_IpDhcpRestart_Object = MibScalar
ipDhcpRestart = _IpDhcpRestart_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 5),
    _IpDhcpRestart_Type()
)
ipDhcpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpRestart.setStatus("current")
_IpHttpsState_Type = EnabledStatus
_IpHttpsState_Object = MibScalar
ipHttpsState = _IpHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 6),
    _IpHttpsState_Type()
)
ipHttpsState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsState.setStatus("current")


class _IpHttpsPort_Type(Integer32):
    """Custom type ipHttpsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_IpHttpsPort_Type.__name__ = "Integer32"
_IpHttpsPort_Object = MibScalar
ipHttpsPort = _IpHttpsPort_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 7),
    _IpHttpsPort_Type()
)
ipHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsPort.setStatus("current")
_DhcpMgt_ObjectIdentity = ObjectIdentity
dhcpMgt = _DhcpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 11)
)
_DhcpClient_ObjectIdentity = ObjectIdentity
dhcpClient = _DhcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 11, 1)
)
_DhcpcOptions_ObjectIdentity = ObjectIdentity
dhcpcOptions = _DhcpcOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 11, 1, 1)
)
_DhcpcInterfaceTable_Object = MibTable
dhcpcInterfaceTable = _DhcpcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpcInterfaceTable.setStatus("current")
_DhcpcInterfaceEntry_Object = MibTableRow
dhcpcInterfaceEntry = _DhcpcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 11, 1, 1, 1, 1)
)
dhcpcInterfaceEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "dhcpcIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpcInterfaceEntry.setStatus("current")
_DhcpcIfIndex_Type = Integer32
_DhcpcIfIndex_Object = MibTableColumn
dhcpcIfIndex = _DhcpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 11, 1, 1, 1, 1, 1),
    _DhcpcIfIndex_Type()
)
dhcpcIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpcIfIndex.setStatus("current")


class _DhcpcIfClientIdMode_Type(Integer32):
    """Custom type dhcpcIfClientIdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notSpecify", 1),
          ("text", 2),
          ("hex", 3))
    )


_DhcpcIfClientIdMode_Type.__name__ = "Integer32"
_DhcpcIfClientIdMode_Object = MibTableColumn
dhcpcIfClientIdMode = _DhcpcIfClientIdMode_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 11, 1, 1, 1, 1, 2),
    _DhcpcIfClientIdMode_Type()
)
dhcpcIfClientIdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpcIfClientIdMode.setStatus("current")


class _DhcpcIfClientId_Type(OctetString):
    """Custom type dhcpcIfClientId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DhcpcIfClientId_Type.__name__ = "OctetString"
_DhcpcIfClientId_Object = MibTableColumn
dhcpcIfClientId = _DhcpcIfClientId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 10, 11, 1, 1, 1, 1, 3),
    _DhcpcIfClientId_Type()
)
dhcpcIfClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpcIfClientId.setStatus("current")
_BcastStormMgt_ObjectIdentity = ObjectIdentity
bcastStormMgt = _BcastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 11)
)
_BcastStormTable_Object = MibTable
bcastStormTable = _BcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 11, 1)
)
if mibBuilder.loadTexts:
    bcastStormTable.setStatus("current")
_BcastStormEntry_Object = MibTableRow
bcastStormEntry = _BcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 11, 1, 1)
)
bcastStormEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "bcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    bcastStormEntry.setStatus("current")
_BcastStormIfIndex_Type = Integer32
_BcastStormIfIndex_Object = MibTableColumn
bcastStormIfIndex = _BcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 11, 1, 1, 1),
    _BcastStormIfIndex_Type()
)
bcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcastStormIfIndex.setStatus("current")
_BcastStormStatus_Type = EnabledStatus
_BcastStormStatus_Object = MibTableColumn
bcastStormStatus = _BcastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 11, 1, 1, 2),
    _BcastStormStatus_Type()
)
bcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormStatus.setStatus("current")
_BcastStormOctetRateInKilo_Type = Integer32
_BcastStormOctetRateInKilo_Object = MibTableColumn
bcastStormOctetRateInKilo = _BcastStormOctetRateInKilo_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 11, 1, 1, 7),
    _BcastStormOctetRateInKilo_Type()
)
bcastStormOctetRateInKilo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormOctetRateInKilo.setStatus("current")
_VlanMgt_ObjectIdentity = ObjectIdentity
vlanMgt = _VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanIndex_Type = Unsigned32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 1, 1, 1),
    _VlanIndex_Type()
)
vlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanIndex.setStatus("current")


class _VlanAddressMethod_Type(Integer32):
    """Custom type vlanAddressMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("user", 1),
          ("bootp", 2),
          ("dhcp", 3))
    )


_VlanAddressMethod_Type.__name__ = "Integer32"
_VlanAddressMethod_Object = MibTableColumn
vlanAddressMethod = _VlanAddressMethod_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 1, 1, 2),
    _VlanAddressMethod_Type()
)
vlanAddressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAddressMethod.setStatus("current")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 2)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("current")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 2, 1)
)
vlanPortEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "vlanPortIndex"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("current")
_VlanPortIndex_Type = Integer32
_VlanPortIndex_Object = MibTableColumn
vlanPortIndex = _VlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 2, 1, 1),
    _VlanPortIndex_Type()
)
vlanPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanPortIndex.setStatus("current")


class _VlanPortMode_Type(Integer32):
    """Custom type vlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hybrid", 1),
          ("dot1qTrunk", 2),
          ("access", 3))
    )


_VlanPortMode_Type.__name__ = "Integer32"
_VlanPortMode_Object = MibTableColumn
vlanPortMode = _VlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 2, 1, 2),
    _VlanPortMode_Type()
)
vlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortMode.setStatus("current")


class _VlanPortPrivateVlanType_Type(Integer32):
    """Custom type vlanPortPrivateVlanType based on Integer32"""
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
        *(("normal", 1),
          ("isolated", 2),
          ("community", 3),
          ("promiscous", 4))
    )


_VlanPortPrivateVlanType_Type.__name__ = "Integer32"
_VlanPortPrivateVlanType_Object = MibTableColumn
vlanPortPrivateVlanType = _VlanPortPrivateVlanType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 2, 1, 3),
    _VlanPortPrivateVlanType_Type()
)
vlanPortPrivateVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortPrivateVlanType.setStatus("current")
_ProtocolVlanTable_Object = MibTable
protocolVlanTable = _ProtocolVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 5)
)
if mibBuilder.loadTexts:
    protocolVlanTable.setStatus("current")
_ProtocolVlanEntry_Object = MibTableRow
protocolVlanEntry = _ProtocolVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 5, 1)
)
protocolVlanEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "protocolVlanGroupId"),
)
if mibBuilder.loadTexts:
    protocolVlanEntry.setStatus("current")
_ProtocolVlanGroupId_Type = Integer32
_ProtocolVlanGroupId_Object = MibTableColumn
protocolVlanGroupId = _ProtocolVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 5, 1, 1),
    _ProtocolVlanGroupId_Type()
)
protocolVlanGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protocolVlanGroupId.setStatus("current")
_ProtocolVlanGroupVid_Type = Integer32
_ProtocolVlanGroupVid_Object = MibTableColumn
protocolVlanGroupVid = _ProtocolVlanGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 12, 5, 1, 2),
    _ProtocolVlanGroupVid_Type()
)
protocolVlanGroupVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolVlanGroupVid.setStatus("current")
_PriorityMgt_ObjectIdentity = ObjectIdentity
priorityMgt = _PriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13)
)


class _PrioIpPrecDscpStatus_Type(Integer32):
    """Custom type prioIpPrecDscpStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("precedence", 2),
          ("dscp", 3))
    )


_PrioIpPrecDscpStatus_Type.__name__ = "Integer32"
_PrioIpPrecDscpStatus_Object = MibScalar
prioIpPrecDscpStatus = _PrioIpPrecDscpStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 1),
    _PrioIpPrecDscpStatus_Type()
)
prioIpPrecDscpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecDscpStatus.setStatus("current")
_PrioIpDscpTable_Object = MibTable
prioIpDscpTable = _PrioIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 4)
)
if mibBuilder.loadTexts:
    prioIpDscpTable.setStatus("current")
_PrioIpDscpEntry_Object = MibTableRow
prioIpDscpEntry = _PrioIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 4, 1)
)
prioIpDscpEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "prioIpDscpPort"),
    (0, "SMC6152L2-MIB", "prioIpDscpValue"),
)
if mibBuilder.loadTexts:
    prioIpDscpEntry.setStatus("current")
_PrioIpDscpPort_Type = Integer32
_PrioIpDscpPort_Object = MibTableColumn
prioIpDscpPort = _PrioIpDscpPort_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 4, 1, 1),
    _PrioIpDscpPort_Type()
)
prioIpDscpPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpDscpPort.setStatus("current")


class _PrioIpDscpValue_Type(Integer32):
    """Custom type prioIpDscpValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_PrioIpDscpValue_Type.__name__ = "Integer32"
_PrioIpDscpValue_Object = MibTableColumn
prioIpDscpValue = _PrioIpDscpValue_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 4, 1, 2),
    _PrioIpDscpValue_Type()
)
prioIpDscpValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpDscpValue.setStatus("current")


class _PrioIpDscpCos_Type(Integer32):
    """Custom type prioIpDscpCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpDscpCos_Type.__name__ = "Integer32"
_PrioIpDscpCos_Object = MibTableColumn
prioIpDscpCos = _PrioIpDscpCos_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 4, 1, 3),
    _PrioIpDscpCos_Type()
)
prioIpDscpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpCos.setStatus("current")
_PrioIpDscpRestoreDefault_Type = Integer32
_PrioIpDscpRestoreDefault_Object = MibScalar
prioIpDscpRestoreDefault = _PrioIpDscpRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 5),
    _PrioIpDscpRestoreDefault_Type()
)
prioIpDscpRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpRestoreDefault.setStatus("current")
_PrioCopy_ObjectIdentity = ObjectIdentity
prioCopy = _PrioCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 8)
)
_PrioCopyIpDscp_Type = OctetString
_PrioCopyIpDscp_Object = MibScalar
prioCopyIpDscp = _PrioCopyIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 8, 2),
    _PrioCopyIpDscp_Type()
)
prioCopyIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpDscp.setStatus("current")
_PrioWrrTable_Object = MibTable
prioWrrTable = _PrioWrrTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 9)
)
if mibBuilder.loadTexts:
    prioWrrTable.setStatus("current")
_PrioWrrEntry_Object = MibTableRow
prioWrrEntry = _PrioWrrEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 9, 1)
)
prioWrrEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "prioWrrTrafficClass"),
)
if mibBuilder.loadTexts:
    prioWrrEntry.setStatus("current")


class _PrioWrrTrafficClass_Type(Integer32):
    """Custom type prioWrrTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioWrrTrafficClass_Type.__name__ = "Integer32"
_PrioWrrTrafficClass_Object = MibTableColumn
prioWrrTrafficClass = _PrioWrrTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 9, 1, 1),
    _PrioWrrTrafficClass_Type()
)
prioWrrTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioWrrTrafficClass.setStatus("current")


class _PrioWrrWeight_Type(Integer32):
    """Custom type prioWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrioWrrWeight_Type.__name__ = "Integer32"
_PrioWrrWeight_Object = MibTableColumn
prioWrrWeight = _PrioWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 9, 1, 2),
    _PrioWrrWeight_Type()
)
prioWrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioWrrWeight.setStatus("current")


class _PrioQueueMode_Type(Integer32):
    """Custom type prioQueueMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("wrr", 1),
          ("strict", 2))
    )


_PrioQueueMode_Type.__name__ = "Integer32"
_PrioQueueMode_Object = MibScalar
prioQueueMode = _PrioQueueMode_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 13, 10),
    _PrioQueueMode_Type()
)
prioQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioQueueMode.setStatus("current")
_TrapDestMgt_ObjectIdentity = ObjectIdentity
trapDestMgt = _TrapDestMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 14)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 14, 1)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("current")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 14, 1, 1)
)
trapDestEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "trapDestAddress"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("current")
_TrapDestAddress_Type = IpAddress
_TrapDestAddress_Object = MibTableColumn
trapDestAddress = _TrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 14, 1, 1, 1),
    _TrapDestAddress_Type()
)
trapDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDestAddress.setStatus("current")


class _TrapDestCommunity_Type(OctetString):
    """Custom type trapDestCommunity based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_TrapDestCommunity_Type.__name__ = "OctetString"
_TrapDestCommunity_Object = MibTableColumn
trapDestCommunity = _TrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 14, 1, 1, 2),
    _TrapDestCommunity_Type()
)
trapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestCommunity.setStatus("current")
_TrapDestStatus_Type = ValidStatus
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 14, 1, 1, 3),
    _TrapDestStatus_Type()
)
trapDestStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestStatus.setStatus("current")


class _TrapDestVersion_Type(Integer32):
    """Custom type trapDestVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version2", 2))
    )


_TrapDestVersion_Type.__name__ = "Integer32"
_TrapDestVersion_Object = MibTableColumn
trapDestVersion = _TrapDestVersion_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 14, 1, 1, 4),
    _TrapDestVersion_Type()
)
trapDestVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestVersion.setStatus("current")


class _TrapDestUdpPort_Type(Integer32):
    """Custom type trapDestUdpPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TrapDestUdpPort_Type.__name__ = "Integer32"
_TrapDestUdpPort_Object = MibTableColumn
trapDestUdpPort = _TrapDestUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 14, 1, 1, 5),
    _TrapDestUdpPort_Type()
)
trapDestUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestUdpPort.setStatus("current")
_QosMgt_ObjectIdentity = ObjectIdentity
qosMgt = _QosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16)
)
_RateLimitMgt_ObjectIdentity = ObjectIdentity
rateLimitMgt = _RateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 1)
)
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("current")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 1, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "rlPortIndex"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("current")
_RlPortIndex_Type = Integer32
_RlPortIndex_Object = MibTableColumn
rlPortIndex = _RlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 1, 2, 1, 1),
    _RlPortIndex_Type()
)
rlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortIndex.setStatus("current")
_RlPortInputStatus_Type = EnabledStatus
_RlPortInputStatus_Object = MibTableColumn
rlPortInputStatus = _RlPortInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 1, 2, 1, 6),
    _RlPortInputStatus_Type()
)
rlPortInputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputStatus.setStatus("current")
_RlPortOutputStatus_Type = EnabledStatus
_RlPortOutputStatus_Object = MibTableColumn
rlPortOutputStatus = _RlPortOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 1, 2, 1, 7),
    _RlPortOutputStatus_Type()
)
rlPortOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputStatus.setStatus("current")
_RlPortInputLimitInKilo_Type = Integer32
_RlPortInputLimitInKilo_Object = MibTableColumn
rlPortInputLimitInKilo = _RlPortInputLimitInKilo_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 1, 2, 1, 10),
    _RlPortInputLimitInKilo_Type()
)
rlPortInputLimitInKilo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputLimitInKilo.setStatus("current")
_RlPortOutputLimitInKilo_Type = Integer32
_RlPortOutputLimitInKilo_Object = MibTableColumn
rlPortOutputLimitInKilo = _RlPortOutputLimitInKilo_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 1, 2, 1, 11),
    _RlPortOutputLimitInKilo_Type()
)
rlPortOutputLimitInKilo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputLimitInKilo.setStatus("current")
_DiffServMgt_ObjectIdentity = ObjectIdentity
diffServMgt = _DiffServMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4)
)
_DiffServPortTable_Object = MibTable
diffServPortTable = _DiffServPortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 9)
)
if mibBuilder.loadTexts:
    diffServPortTable.setStatus("current")
_DiffServPortEntry_Object = MibTableRow
diffServPortEntry = _DiffServPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 9, 1)
)
diffServPortEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "diffServPortIfIndex"),
)
if mibBuilder.loadTexts:
    diffServPortEntry.setStatus("current")
_DiffServPortIfIndex_Type = Integer32
_DiffServPortIfIndex_Object = MibTableColumn
diffServPortIfIndex = _DiffServPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 9, 1, 1),
    _DiffServPortIfIndex_Type()
)
diffServPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPortIfIndex.setStatus("current")
_DiffServPortPolicyMapIndex_Type = Integer32
_DiffServPortPolicyMapIndex_Object = MibTableColumn
diffServPortPolicyMapIndex = _DiffServPortPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 9, 1, 2),
    _DiffServPortPolicyMapIndex_Type()
)
diffServPortPolicyMapIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPortPolicyMapIndex.setStatus("current")
_DiffServPortIngressIpAclIndex_Type = Integer32
_DiffServPortIngressIpAclIndex_Object = MibTableColumn
diffServPortIngressIpAclIndex = _DiffServPortIngressIpAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 9, 1, 3),
    _DiffServPortIngressIpAclIndex_Type()
)
diffServPortIngressIpAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPortIngressIpAclIndex.setStatus("current")
_DiffServPortIngressMacAclIndex_Type = Integer32
_DiffServPortIngressMacAclIndex_Object = MibTableColumn
diffServPortIngressMacAclIndex = _DiffServPortIngressMacAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 9, 1, 4),
    _DiffServPortIngressMacAclIndex_Type()
)
diffServPortIngressMacAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPortIngressMacAclIndex.setStatus("current")
_DiffServPolicyMapTable_Object = MibTable
diffServPolicyMapTable = _DiffServPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 10)
)
if mibBuilder.loadTexts:
    diffServPolicyMapTable.setStatus("current")
_DiffServPolicyMapEntry_Object = MibTableRow
diffServPolicyMapEntry = _DiffServPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 10, 1)
)
diffServPolicyMapEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "diffServPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    diffServPolicyMapEntry.setStatus("current")
_DiffServPolicyMapIndex_Type = Integer32
_DiffServPolicyMapIndex_Object = MibTableColumn
diffServPolicyMapIndex = _DiffServPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 10, 1, 1),
    _DiffServPolicyMapIndex_Type()
)
diffServPolicyMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPolicyMapIndex.setStatus("current")


class _DiffServPolicyMapName_Type(DisplayString):
    """Custom type diffServPolicyMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DiffServPolicyMapName_Type.__name__ = "DisplayString"
_DiffServPolicyMapName_Object = MibTableColumn
diffServPolicyMapName = _DiffServPolicyMapName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 10, 1, 2),
    _DiffServPolicyMapName_Type()
)
diffServPolicyMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapName.setStatus("current")


class _DiffServPolicyMapDescription_Type(DisplayString):
    """Custom type diffServPolicyMapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiffServPolicyMapDescription_Type.__name__ = "DisplayString"
_DiffServPolicyMapDescription_Object = MibTableColumn
diffServPolicyMapDescription = _DiffServPolicyMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 10, 1, 3),
    _DiffServPolicyMapDescription_Type()
)
diffServPolicyMapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapDescription.setStatus("current")


class _DiffServPolicyMapElementIndexList_Type(OctetString):
    """Custom type diffServPolicyMapElementIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_DiffServPolicyMapElementIndexList_Type.__name__ = "OctetString"
_DiffServPolicyMapElementIndexList_Object = MibTableColumn
diffServPolicyMapElementIndexList = _DiffServPolicyMapElementIndexList_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 10, 1, 4),
    _DiffServPolicyMapElementIndexList_Type()
)
diffServPolicyMapElementIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServPolicyMapElementIndexList.setStatus("current")
_DiffServPolicyMapStatus_Type = RowStatus
_DiffServPolicyMapStatus_Object = MibTableColumn
diffServPolicyMapStatus = _DiffServPolicyMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 10, 1, 5),
    _DiffServPolicyMapStatus_Type()
)
diffServPolicyMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapStatus.setStatus("current")
_DiffServPolicyMapAttachCtl_ObjectIdentity = ObjectIdentity
diffServPolicyMapAttachCtl = _DiffServPolicyMapAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 11)
)
_DiffServPolicyMapAttachCtlIndex_Type = Integer32
_DiffServPolicyMapAttachCtlIndex_Object = MibScalar
diffServPolicyMapAttachCtlIndex = _DiffServPolicyMapAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 11, 1),
    _DiffServPolicyMapAttachCtlIndex_Type()
)
diffServPolicyMapAttachCtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlIndex.setStatus("current")
_DiffServPolicyMapAttachCtlElementIndex_Type = Integer32
_DiffServPolicyMapAttachCtlElementIndex_Object = MibScalar
diffServPolicyMapAttachCtlElementIndex = _DiffServPolicyMapAttachCtlElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 11, 2),
    _DiffServPolicyMapAttachCtlElementIndex_Type()
)
diffServPolicyMapAttachCtlElementIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlElementIndex.setStatus("current")


class _DiffServPolicyMapAttachCtlAction_Type(Integer32):
    """Custom type diffServPolicyMapAttachCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("attach", 2),
          ("detach", 3))
    )


_DiffServPolicyMapAttachCtlAction_Type.__name__ = "Integer32"
_DiffServPolicyMapAttachCtlAction_Object = MibScalar
diffServPolicyMapAttachCtlAction = _DiffServPolicyMapAttachCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 11, 3),
    _DiffServPolicyMapAttachCtlAction_Type()
)
diffServPolicyMapAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlAction.setStatus("current")
_DiffServPolicyMapElementTable_Object = MibTable
diffServPolicyMapElementTable = _DiffServPolicyMapElementTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 12)
)
if mibBuilder.loadTexts:
    diffServPolicyMapElementTable.setStatus("current")
_DiffServPolicyMapElementEntry_Object = MibTableRow
diffServPolicyMapElementEntry = _DiffServPolicyMapElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 12, 1)
)
diffServPolicyMapElementEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "diffServPolicyMapElementIndex"),
)
if mibBuilder.loadTexts:
    diffServPolicyMapElementEntry.setStatus("current")
_DiffServPolicyMapElementIndex_Type = Integer32
_DiffServPolicyMapElementIndex_Object = MibTableColumn
diffServPolicyMapElementIndex = _DiffServPolicyMapElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 12, 1, 1),
    _DiffServPolicyMapElementIndex_Type()
)
diffServPolicyMapElementIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPolicyMapElementIndex.setStatus("current")


class _DiffServPolicyMapElementClassMapIndex_Type(Integer32):
    """Custom type diffServPolicyMapElementClassMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DiffServPolicyMapElementClassMapIndex_Type.__name__ = "Integer32"
_DiffServPolicyMapElementClassMapIndex_Object = MibTableColumn
diffServPolicyMapElementClassMapIndex = _DiffServPolicyMapElementClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 12, 1, 2),
    _DiffServPolicyMapElementClassMapIndex_Type()
)
diffServPolicyMapElementClassMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementClassMapIndex.setStatus("current")
_DiffServPolicyMapElementMeterIndex_Type = Integer32
_DiffServPolicyMapElementMeterIndex_Object = MibTableColumn
diffServPolicyMapElementMeterIndex = _DiffServPolicyMapElementMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 12, 1, 3),
    _DiffServPolicyMapElementMeterIndex_Type()
)
diffServPolicyMapElementMeterIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementMeterIndex.setStatus("current")


class _DiffServPolicyMapElementActionIndex_Type(Integer32):
    """Custom type diffServPolicyMapElementActionIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_DiffServPolicyMapElementActionIndex_Type.__name__ = "Integer32"
_DiffServPolicyMapElementActionIndex_Object = MibTableColumn
diffServPolicyMapElementActionIndex = _DiffServPolicyMapElementActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 12, 1, 4),
    _DiffServPolicyMapElementActionIndex_Type()
)
diffServPolicyMapElementActionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementActionIndex.setStatus("current")
_DiffServPolicyMapElementStatus_Type = RowStatus
_DiffServPolicyMapElementStatus_Object = MibTableColumn
diffServPolicyMapElementStatus = _DiffServPolicyMapElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 12, 1, 5),
    _DiffServPolicyMapElementStatus_Type()
)
diffServPolicyMapElementStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementStatus.setStatus("current")
_DiffServClassMapTable_Object = MibTable
diffServClassMapTable = _DiffServClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 13)
)
if mibBuilder.loadTexts:
    diffServClassMapTable.setStatus("current")
_DiffServClassMapEntry_Object = MibTableRow
diffServClassMapEntry = _DiffServClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 13, 1)
)
diffServClassMapEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "diffServClassMapIndex"),
)
if mibBuilder.loadTexts:
    diffServClassMapEntry.setStatus("current")
_DiffServClassMapIndex_Type = Integer32
_DiffServClassMapIndex_Object = MibTableColumn
diffServClassMapIndex = _DiffServClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 13, 1, 1),
    _DiffServClassMapIndex_Type()
)
diffServClassMapIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServClassMapIndex.setStatus("current")


class _DiffServClassMapName_Type(DisplayString):
    """Custom type diffServClassMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DiffServClassMapName_Type.__name__ = "DisplayString"
_DiffServClassMapName_Object = MibTableColumn
diffServClassMapName = _DiffServClassMapName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 13, 1, 2),
    _DiffServClassMapName_Type()
)
diffServClassMapName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapName.setStatus("current")


class _DiffServClassMapDescription_Type(DisplayString):
    """Custom type diffServClassMapDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_DiffServClassMapDescription_Type.__name__ = "DisplayString"
_DiffServClassMapDescription_Object = MibTableColumn
diffServClassMapDescription = _DiffServClassMapDescription_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 13, 1, 3),
    _DiffServClassMapDescription_Type()
)
diffServClassMapDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapDescription.setStatus("current")


class _DiffServClassMapMatchType_Type(Integer32):
    """Custom type diffServClassMapMatchType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("matchAny", 1),
          ("matchAll", 2))
    )


_DiffServClassMapMatchType_Type.__name__ = "Integer32"
_DiffServClassMapMatchType_Object = MibTableColumn
diffServClassMapMatchType = _DiffServClassMapMatchType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 13, 1, 4),
    _DiffServClassMapMatchType_Type()
)
diffServClassMapMatchType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapMatchType.setStatus("current")


class _DiffServClassMapElementIndexTypeList_Type(OctetString):
    """Custom type diffServClassMapElementIndexTypeList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiffServClassMapElementIndexTypeList_Type.__name__ = "OctetString"
_DiffServClassMapElementIndexTypeList_Object = MibTableColumn
diffServClassMapElementIndexTypeList = _DiffServClassMapElementIndexTypeList_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 13, 1, 5),
    _DiffServClassMapElementIndexTypeList_Type()
)
diffServClassMapElementIndexTypeList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServClassMapElementIndexTypeList.setStatus("current")


class _DiffServClassMapElementIndexList_Type(OctetString):
    """Custom type diffServClassMapElementIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiffServClassMapElementIndexList_Type.__name__ = "OctetString"
_DiffServClassMapElementIndexList_Object = MibTableColumn
diffServClassMapElementIndexList = _DiffServClassMapElementIndexList_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 13, 1, 6),
    _DiffServClassMapElementIndexList_Type()
)
diffServClassMapElementIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServClassMapElementIndexList.setStatus("current")
_DiffServClassMapStatus_Type = RowStatus
_DiffServClassMapStatus_Object = MibTableColumn
diffServClassMapStatus = _DiffServClassMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 13, 1, 7),
    _DiffServClassMapStatus_Type()
)
diffServClassMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapStatus.setStatus("current")
_DiffServClassMapAttachCtl_ObjectIdentity = ObjectIdentity
diffServClassMapAttachCtl = _DiffServClassMapAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 14)
)
_DiffServClassMapAttachCtlIndex_Type = Integer32
_DiffServClassMapAttachCtlIndex_Object = MibScalar
diffServClassMapAttachCtlIndex = _DiffServClassMapAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 14, 1),
    _DiffServClassMapAttachCtlIndex_Type()
)
diffServClassMapAttachCtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlIndex.setStatus("current")


class _DiffServClassMapAttachCtlElementIndexType_Type(Integer32):
    """Custom type diffServClassMapAttachCtlElementIndexType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("macAce", 1),
          ("ipAce", 2),
          ("acl", 3))
    )


_DiffServClassMapAttachCtlElementIndexType_Type.__name__ = "Integer32"
_DiffServClassMapAttachCtlElementIndexType_Object = MibScalar
diffServClassMapAttachCtlElementIndexType = _DiffServClassMapAttachCtlElementIndexType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 14, 2),
    _DiffServClassMapAttachCtlElementIndexType_Type()
)
diffServClassMapAttachCtlElementIndexType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlElementIndexType.setStatus("current")
_DiffServClassMapAttachCtlElementIndex_Type = Integer32
_DiffServClassMapAttachCtlElementIndex_Object = MibScalar
diffServClassMapAttachCtlElementIndex = _DiffServClassMapAttachCtlElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 14, 3),
    _DiffServClassMapAttachCtlElementIndex_Type()
)
diffServClassMapAttachCtlElementIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlElementIndex.setStatus("current")


class _DiffServClassMapAttachCtlAction_Type(Integer32):
    """Custom type diffServClassMapAttachCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("attach", 2),
          ("detach", 3))
    )


_DiffServClassMapAttachCtlAction_Type.__name__ = "Integer32"
_DiffServClassMapAttachCtlAction_Object = MibScalar
diffServClassMapAttachCtlAction = _DiffServClassMapAttachCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 14, 4),
    _DiffServClassMapAttachCtlAction_Type()
)
diffServClassMapAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlAction.setStatus("current")
_DiffServAclTable_Object = MibTable
diffServAclTable = _DiffServAclTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 15)
)
if mibBuilder.loadTexts:
    diffServAclTable.setStatus("current")
_DiffServAclEntry_Object = MibTableRow
diffServAclEntry = _DiffServAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 15, 1)
)
diffServAclEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "diffServAclIndex"),
)
if mibBuilder.loadTexts:
    diffServAclEntry.setStatus("current")
_DiffServAclIndex_Type = Integer32
_DiffServAclIndex_Object = MibTableColumn
diffServAclIndex = _DiffServAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 15, 1, 1),
    _DiffServAclIndex_Type()
)
diffServAclIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServAclIndex.setStatus("current")


class _DiffServAclName_Type(DisplayString):
    """Custom type diffServAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DiffServAclName_Type.__name__ = "DisplayString"
_DiffServAclName_Object = MibTableColumn
diffServAclName = _DiffServAclName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 15, 1, 2),
    _DiffServAclName_Type()
)
diffServAclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAclName.setStatus("current")


class _DiffServAclType_Type(Integer32):
    """Custom type diffServAclType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ipstandard", 2),
          ("ipextended", 3))
    )


_DiffServAclType_Type.__name__ = "Integer32"
_DiffServAclType_Object = MibTableColumn
diffServAclType = _DiffServAclType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 15, 1, 3),
    _DiffServAclType_Type()
)
diffServAclType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAclType.setStatus("current")


class _DiffServAclAceIndexList_Type(OctetString):
    """Custom type diffServAclAceIndexList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DiffServAclAceIndexList_Type.__name__ = "OctetString"
_DiffServAclAceIndexList_Object = MibTableColumn
diffServAclAceIndexList = _DiffServAclAceIndexList_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 15, 1, 4),
    _DiffServAclAceIndexList_Type()
)
diffServAclAceIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAclAceIndexList.setStatus("current")
_DiffServAclStatus_Type = RowStatus
_DiffServAclStatus_Object = MibTableColumn
diffServAclStatus = _DiffServAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 15, 1, 5),
    _DiffServAclStatus_Type()
)
diffServAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAclStatus.setStatus("current")
_DiffServAclAttachCtl_ObjectIdentity = ObjectIdentity
diffServAclAttachCtl = _DiffServAclAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 16)
)
_DiffServAclAttachCtlIndex_Type = Integer32
_DiffServAclAttachCtlIndex_Object = MibScalar
diffServAclAttachCtlIndex = _DiffServAclAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 16, 1),
    _DiffServAclAttachCtlIndex_Type()
)
diffServAclAttachCtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlIndex.setStatus("current")


class _DiffServAclAttachCtlAceType_Type(Integer32):
    """Custom type diffServAclAttachCtlAceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("macAce", 1),
          ("ipAce", 2))
    )


_DiffServAclAttachCtlAceType_Type.__name__ = "Integer32"
_DiffServAclAttachCtlAceType_Object = MibScalar
diffServAclAttachCtlAceType = _DiffServAclAttachCtlAceType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 16, 2),
    _DiffServAclAttachCtlAceType_Type()
)
diffServAclAttachCtlAceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAceType.setStatus("current")
_DiffServAclAttachCtlAceIndex_Type = Integer32
_DiffServAclAttachCtlAceIndex_Object = MibScalar
diffServAclAttachCtlAceIndex = _DiffServAclAttachCtlAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 16, 3),
    _DiffServAclAttachCtlAceIndex_Type()
)
diffServAclAttachCtlAceIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAceIndex.setStatus("current")


class _DiffServAclAttachCtlAction_Type(Integer32):
    """Custom type diffServAclAttachCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 1),
          ("attach", 2),
          ("detach", 3))
    )


_DiffServAclAttachCtlAction_Type.__name__ = "Integer32"
_DiffServAclAttachCtlAction_Object = MibScalar
diffServAclAttachCtlAction = _DiffServAclAttachCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 16, 4),
    _DiffServAclAttachCtlAction_Type()
)
diffServAclAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAction.setStatus("current")
_DiffServIpAceTable_Object = MibTable
diffServIpAceTable = _DiffServIpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17)
)
if mibBuilder.loadTexts:
    diffServIpAceTable.setStatus("current")
_DiffServIpAceEntry_Object = MibTableRow
diffServIpAceEntry = _DiffServIpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1)
)
diffServIpAceEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "diffServIpAceIndex"),
)
if mibBuilder.loadTexts:
    diffServIpAceEntry.setStatus("current")
_DiffServIpAceIndex_Type = Integer32
_DiffServIpAceIndex_Object = MibTableColumn
diffServIpAceIndex = _DiffServIpAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 1),
    _DiffServIpAceIndex_Type()
)
diffServIpAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServIpAceIndex.setStatus("current")


class _DiffServIpAceType_Type(Integer32):
    """Custom type diffServIpAceType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("extended", 2))
    )


_DiffServIpAceType_Type.__name__ = "Integer32"
_DiffServIpAceType_Object = MibTableColumn
diffServIpAceType = _DiffServIpAceType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 2),
    _DiffServIpAceType_Type()
)
diffServIpAceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceType.setStatus("current")


class _DiffServIpAceAccess_Type(Integer32):
    """Custom type diffServIpAceAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_DiffServIpAceAccess_Type.__name__ = "Integer32"
_DiffServIpAceAccess_Object = MibTableColumn
diffServIpAceAccess = _DiffServIpAceAccess_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 3),
    _DiffServIpAceAccess_Type()
)
diffServIpAceAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceAccess.setStatus("current")
_DiffServIpAceSourceIpAddr_Type = IpAddress
_DiffServIpAceSourceIpAddr_Object = MibTableColumn
diffServIpAceSourceIpAddr = _DiffServIpAceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 4),
    _DiffServIpAceSourceIpAddr_Type()
)
diffServIpAceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourceIpAddr.setStatus("current")
_DiffServIpAceSourceIpAddrBitmask_Type = IpAddress
_DiffServIpAceSourceIpAddrBitmask_Object = MibTableColumn
diffServIpAceSourceIpAddrBitmask = _DiffServIpAceSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 5),
    _DiffServIpAceSourceIpAddrBitmask_Type()
)
diffServIpAceSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourceIpAddrBitmask.setStatus("current")
_DiffServIpAceDestIpAddr_Type = IpAddress
_DiffServIpAceDestIpAddr_Object = MibTableColumn
diffServIpAceDestIpAddr = _DiffServIpAceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 6),
    _DiffServIpAceDestIpAddr_Type()
)
diffServIpAceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestIpAddr.setStatus("current")
_DiffServIpAceDestIpAddrBitmask_Type = IpAddress
_DiffServIpAceDestIpAddrBitmask_Object = MibTableColumn
diffServIpAceDestIpAddrBitmask = _DiffServIpAceDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 7),
    _DiffServIpAceDestIpAddrBitmask_Type()
)
diffServIpAceDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestIpAddrBitmask.setStatus("current")


class _DiffServIpAceProtocol_Type(Integer32):
    """Custom type diffServIpAceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_DiffServIpAceProtocol_Type.__name__ = "Integer32"
_DiffServIpAceProtocol_Object = MibTableColumn
diffServIpAceProtocol = _DiffServIpAceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 8),
    _DiffServIpAceProtocol_Type()
)
diffServIpAceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceProtocol.setStatus("current")


class _DiffServIpAcePrec_Type(Integer32):
    """Custom type diffServIpAcePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DiffServIpAcePrec_Type.__name__ = "Integer32"
_DiffServIpAcePrec_Object = MibTableColumn
diffServIpAcePrec = _DiffServIpAcePrec_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 9),
    _DiffServIpAcePrec_Type()
)
diffServIpAcePrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAcePrec.setStatus("current")


class _DiffServIpAceTos_Type(Integer32):
    """Custom type diffServIpAceTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_DiffServIpAceTos_Type.__name__ = "Integer32"
_DiffServIpAceTos_Object = MibTableColumn
diffServIpAceTos = _DiffServIpAceTos_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 10),
    _DiffServIpAceTos_Type()
)
diffServIpAceTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceTos.setStatus("current")


class _DiffServIpAceDscp_Type(Integer32):
    """Custom type diffServIpAceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DiffServIpAceDscp_Type.__name__ = "Integer32"
_DiffServIpAceDscp_Object = MibTableColumn
diffServIpAceDscp = _DiffServIpAceDscp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 11),
    _DiffServIpAceDscp_Type()
)
diffServIpAceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDscp.setStatus("current")


class _DiffServIpAceSourcePortOp_Type(Integer32):
    """Custom type diffServIpAceSourcePortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperator", 1),
          ("equal", 2),
          ("range", 3))
    )


_DiffServIpAceSourcePortOp_Type.__name__ = "Integer32"
_DiffServIpAceSourcePortOp_Object = MibTableColumn
diffServIpAceSourcePortOp = _DiffServIpAceSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 12),
    _DiffServIpAceSourcePortOp_Type()
)
diffServIpAceSourcePortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourcePortOp.setStatus("current")


class _DiffServIpAceMinSourcePort_Type(Integer32):
    """Custom type diffServIpAceMinSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceMinSourcePort_Type.__name__ = "Integer32"
_DiffServIpAceMinSourcePort_Object = MibTableColumn
diffServIpAceMinSourcePort = _DiffServIpAceMinSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 13),
    _DiffServIpAceMinSourcePort_Type()
)
diffServIpAceMinSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceMinSourcePort.setStatus("current")


class _DiffServIpAceSourcePortBitmask_Type(Integer32):
    """Custom type diffServIpAceSourcePortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceSourcePortBitmask_Type.__name__ = "Integer32"
_DiffServIpAceSourcePortBitmask_Object = MibTableColumn
diffServIpAceSourcePortBitmask = _DiffServIpAceSourcePortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 15),
    _DiffServIpAceSourcePortBitmask_Type()
)
diffServIpAceSourcePortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourcePortBitmask.setStatus("current")


class _DiffServIpAceDestPortOp_Type(Integer32):
    """Custom type diffServIpAceDestPortOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperator", 1),
          ("equal", 2),
          ("range", 3))
    )


_DiffServIpAceDestPortOp_Type.__name__ = "Integer32"
_DiffServIpAceDestPortOp_Object = MibTableColumn
diffServIpAceDestPortOp = _DiffServIpAceDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 16),
    _DiffServIpAceDestPortOp_Type()
)
diffServIpAceDestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestPortOp.setStatus("current")


class _DiffServIpAceMinDestPort_Type(Integer32):
    """Custom type diffServIpAceMinDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceMinDestPort_Type.__name__ = "Integer32"
_DiffServIpAceMinDestPort_Object = MibTableColumn
diffServIpAceMinDestPort = _DiffServIpAceMinDestPort_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 17),
    _DiffServIpAceMinDestPort_Type()
)
diffServIpAceMinDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceMinDestPort.setStatus("current")


class _DiffServIpAceDestPortBitmask_Type(Integer32):
    """Custom type diffServIpAceDestPortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServIpAceDestPortBitmask_Type.__name__ = "Integer32"
_DiffServIpAceDestPortBitmask_Object = MibTableColumn
diffServIpAceDestPortBitmask = _DiffServIpAceDestPortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 19),
    _DiffServIpAceDestPortBitmask_Type()
)
diffServIpAceDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestPortBitmask.setStatus("current")


class _DiffServIpAceControlCode_Type(Integer32):
    """Custom type diffServIpAceControlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DiffServIpAceControlCode_Type.__name__ = "Integer32"
_DiffServIpAceControlCode_Object = MibTableColumn
diffServIpAceControlCode = _DiffServIpAceControlCode_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 20),
    _DiffServIpAceControlCode_Type()
)
diffServIpAceControlCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceControlCode.setStatus("current")


class _DiffServIpAceControlCodeBitmask_Type(Integer32):
    """Custom type diffServIpAceControlCodeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServIpAceControlCodeBitmask_Type.__name__ = "Integer32"
_DiffServIpAceControlCodeBitmask_Object = MibTableColumn
diffServIpAceControlCodeBitmask = _DiffServIpAceControlCodeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 21),
    _DiffServIpAceControlCodeBitmask_Type()
)
diffServIpAceControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceControlCodeBitmask.setStatus("current")
_DiffServIpAceStatus_Type = RowStatus
_DiffServIpAceStatus_Object = MibTableColumn
diffServIpAceStatus = _DiffServIpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 17, 1, 22),
    _DiffServIpAceStatus_Type()
)
diffServIpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceStatus.setStatus("current")
_DiffServMacAceTable_Object = MibTable
diffServMacAceTable = _DiffServMacAceTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18)
)
if mibBuilder.loadTexts:
    diffServMacAceTable.setStatus("current")
_DiffServMacAceEntry_Object = MibTableRow
diffServMacAceEntry = _DiffServMacAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1)
)
diffServMacAceEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "diffServMacAceIndex"),
)
if mibBuilder.loadTexts:
    diffServMacAceEntry.setStatus("current")
_DiffServMacAceIndex_Type = Integer32
_DiffServMacAceIndex_Object = MibTableColumn
diffServMacAceIndex = _DiffServMacAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 1),
    _DiffServMacAceIndex_Type()
)
diffServMacAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMacAceIndex.setStatus("current")


class _DiffServMacAceAccess_Type(Integer32):
    """Custom type diffServMacAceAccess based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("deny", 2))
    )


_DiffServMacAceAccess_Type.__name__ = "Integer32"
_DiffServMacAceAccess_Object = MibTableColumn
diffServMacAceAccess = _DiffServMacAceAccess_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 2),
    _DiffServMacAceAccess_Type()
)
diffServMacAceAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceAccess.setStatus("current")


class _DiffServMacAcePktformat_Type(Integer32):
    """Custom type diffServMacAcePktformat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("any", 1),
          ("untagged-Eth2", 2),
          ("untagged802Dot3", 3),
          ("tagggedEth2", 4),
          ("tagged802Dot3", 5))
    )


_DiffServMacAcePktformat_Type.__name__ = "Integer32"
_DiffServMacAcePktformat_Object = MibTableColumn
diffServMacAcePktformat = _DiffServMacAcePktformat_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 3),
    _DiffServMacAcePktformat_Type()
)
diffServMacAcePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAcePktformat.setStatus("current")
_DiffServMacAceSourceMacAddr_Type = MacAddress
_DiffServMacAceSourceMacAddr_Object = MibTableColumn
diffServMacAceSourceMacAddr = _DiffServMacAceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 4),
    _DiffServMacAceSourceMacAddr_Type()
)
diffServMacAceSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceSourceMacAddr.setStatus("current")
_DiffServMacAceSourceMacAddrBitmask_Type = MacAddress
_DiffServMacAceSourceMacAddrBitmask_Object = MibTableColumn
diffServMacAceSourceMacAddrBitmask = _DiffServMacAceSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 5),
    _DiffServMacAceSourceMacAddrBitmask_Type()
)
diffServMacAceSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceSourceMacAddrBitmask.setStatus("current")
_DiffServMacAceDestMacAddr_Type = MacAddress
_DiffServMacAceDestMacAddr_Object = MibTableColumn
diffServMacAceDestMacAddr = _DiffServMacAceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 6),
    _DiffServMacAceDestMacAddr_Type()
)
diffServMacAceDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceDestMacAddr.setStatus("current")
_DiffServMacAceDestMacAddrBitmask_Type = MacAddress
_DiffServMacAceDestMacAddrBitmask_Object = MibTableColumn
diffServMacAceDestMacAddrBitmask = _DiffServMacAceDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 7),
    _DiffServMacAceDestMacAddrBitmask_Type()
)
diffServMacAceDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceDestMacAddrBitmask.setStatus("current")


class _DiffServMacAceVidOp_Type(Integer32):
    """Custom type diffServMacAceVidOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperator", 1),
          ("equal", 2),
          ("range", 3))
    )


_DiffServMacAceVidOp_Type.__name__ = "Integer32"
_DiffServMacAceVidOp_Object = MibTableColumn
diffServMacAceVidOp = _DiffServMacAceVidOp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 8),
    _DiffServMacAceVidOp_Type()
)
diffServMacAceVidOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceVidOp.setStatus("current")


class _DiffServMacAceMinVid_Type(Integer32):
    """Custom type diffServMacAceMinVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_DiffServMacAceMinVid_Type.__name__ = "Integer32"
_DiffServMacAceMinVid_Object = MibTableColumn
diffServMacAceMinVid = _DiffServMacAceMinVid_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 9),
    _DiffServMacAceMinVid_Type()
)
diffServMacAceMinVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMinVid.setStatus("current")


class _DiffServMacAceVidBitmask_Type(Integer32):
    """Custom type diffServMacAceVidBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_DiffServMacAceVidBitmask_Type.__name__ = "Integer32"
_DiffServMacAceVidBitmask_Object = MibTableColumn
diffServMacAceVidBitmask = _DiffServMacAceVidBitmask_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 10),
    _DiffServMacAceVidBitmask_Type()
)
diffServMacAceVidBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceVidBitmask.setStatus("current")


class _DiffServMacAceEtherTypeOp_Type(Integer32):
    """Custom type diffServMacAceEtherTypeOp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOperator", 1),
          ("equal", 2),
          ("range", 3))
    )


_DiffServMacAceEtherTypeOp_Type.__name__ = "Integer32"
_DiffServMacAceEtherTypeOp_Object = MibTableColumn
diffServMacAceEtherTypeOp = _DiffServMacAceEtherTypeOp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 12),
    _DiffServMacAceEtherTypeOp_Type()
)
diffServMacAceEtherTypeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceEtherTypeOp.setStatus("current")


class _DiffServMacAceEtherTypeBitmask_Type(Integer32):
    """Custom type diffServMacAceEtherTypeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServMacAceEtherTypeBitmask_Type.__name__ = "Integer32"
_DiffServMacAceEtherTypeBitmask_Object = MibTableColumn
diffServMacAceEtherTypeBitmask = _DiffServMacAceEtherTypeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 13),
    _DiffServMacAceEtherTypeBitmask_Type()
)
diffServMacAceEtherTypeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceEtherTypeBitmask.setStatus("current")


class _DiffServMacAceMinEtherType_Type(Integer32):
    """Custom type diffServMacAceMinEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServMacAceMinEtherType_Type.__name__ = "Integer32"
_DiffServMacAceMinEtherType_Object = MibTableColumn
diffServMacAceMinEtherType = _DiffServMacAceMinEtherType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 14),
    _DiffServMacAceMinEtherType_Type()
)
diffServMacAceMinEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMinEtherType.setStatus("current")
_DiffServMacAceStatus_Type = RowStatus
_DiffServMacAceStatus_Object = MibTableColumn
diffServMacAceStatus = _DiffServMacAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 18, 1, 16),
    _DiffServMacAceStatus_Type()
)
diffServMacAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceStatus.setStatus("current")
_DiffServActionTable_Object = MibTable
diffServActionTable = _DiffServActionTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 19)
)
if mibBuilder.loadTexts:
    diffServActionTable.setStatus("current")
_DiffServActionEntry_Object = MibTableRow
diffServActionEntry = _DiffServActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 19, 1)
)
diffServActionEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "diffServActionIndex"),
)
if mibBuilder.loadTexts:
    diffServActionEntry.setStatus("current")
_DiffServActionIndex_Type = Integer32
_DiffServActionIndex_Object = MibTableColumn
diffServActionIndex = _DiffServActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 19, 1, 1),
    _DiffServActionIndex_Type()
)
diffServActionIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServActionIndex.setStatus("current")


class _DiffServActionList_Type(Bits):
    """Custom type diffServActionList based on Bits"""
    namedValues = NamedValues(
        *(("actionPktNewPri", 0),
          ("actionPktNewDscp", 2),
          ("actionRedPktNewDscp", 3),
          ("actionRedDrop", 4))
    )

_DiffServActionList_Type.__name__ = "Bits"
_DiffServActionList_Object = MibTableColumn
diffServActionList = _DiffServActionList_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 19, 1, 2),
    _DiffServActionList_Type()
)
diffServActionList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionList.setStatus("current")


class _DiffServActionPktNewPri_Type(Integer32):
    """Custom type diffServActionPktNewPri based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DiffServActionPktNewPri_Type.__name__ = "Integer32"
_DiffServActionPktNewPri_Object = MibTableColumn
diffServActionPktNewPri = _DiffServActionPktNewPri_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 19, 1, 3),
    _DiffServActionPktNewPri_Type()
)
diffServActionPktNewPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionPktNewPri.setStatus("current")


class _DiffServActionPktNewDscp_Type(Integer32):
    """Custom type diffServActionPktNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServActionPktNewDscp_Type.__name__ = "Integer32"
_DiffServActionPktNewDscp_Object = MibTableColumn
diffServActionPktNewDscp = _DiffServActionPktNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 19, 1, 5),
    _DiffServActionPktNewDscp_Type()
)
diffServActionPktNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionPktNewDscp.setStatus("current")


class _DiffServActionRedPktNewDscp_Type(Integer32):
    """Custom type diffServActionRedPktNewDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServActionRedPktNewDscp_Type.__name__ = "Integer32"
_DiffServActionRedPktNewDscp_Object = MibTableColumn
diffServActionRedPktNewDscp = _DiffServActionRedPktNewDscp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 19, 1, 6),
    _DiffServActionRedPktNewDscp_Type()
)
diffServActionRedPktNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionRedPktNewDscp.setStatus("current")
_DiffServActionRedDrop_Type = EnabledStatus
_DiffServActionRedDrop_Object = MibTableColumn
diffServActionRedDrop = _DiffServActionRedDrop_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 19, 1, 7),
    _DiffServActionRedDrop_Type()
)
diffServActionRedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionRedDrop.setStatus("current")
_DiffServActionStatus_Type = RowStatus
_DiffServActionStatus_Object = MibTableColumn
diffServActionStatus = _DiffServActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 19, 1, 8),
    _DiffServActionStatus_Type()
)
diffServActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionStatus.setStatus("current")
_DiffServMeterTable_Object = MibTable
diffServMeterTable = _DiffServMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 20)
)
if mibBuilder.loadTexts:
    diffServMeterTable.setStatus("current")
_DiffServMeterEntry_Object = MibTableRow
diffServMeterEntry = _DiffServMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 20, 1)
)
diffServMeterEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "diffServActionIndex"),
)
if mibBuilder.loadTexts:
    diffServMeterEntry.setStatus("current")
_DiffServMeterIndex_Type = Integer32
_DiffServMeterIndex_Object = MibTableColumn
diffServMeterIndex = _DiffServMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 20, 1, 1),
    _DiffServMeterIndex_Type()
)
diffServMeterIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServMeterIndex.setStatus("current")


class _DiffServMeterModel_Type(Integer32):
    """Custom type diffServMeterModel based on Integer32"""
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
        *(("default", 1),
          ("flow", 2),
          ("trTcmColorBlind", 3),
          ("trTcmColorAware", 4),
          ("srTcmColorBlind", 5),
          ("srTcmColorAware", 6))
    )


_DiffServMeterModel_Type.__name__ = "Integer32"
_DiffServMeterModel_Object = MibTableColumn
diffServMeterModel = _DiffServMeterModel_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 20, 1, 2),
    _DiffServMeterModel_Type()
)
diffServMeterModel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterModel.setStatus("current")


class _DiffServMeterRate_Type(Integer32):
    """Custom type diffServMeterRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_DiffServMeterRate_Type.__name__ = "Integer32"
_DiffServMeterRate_Object = MibTableColumn
diffServMeterRate = _DiffServMeterRate_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 20, 1, 3),
    _DiffServMeterRate_Type()
)
diffServMeterRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterRate.setStatus("current")


class _DiffServMeterBurstSize_Type(Integer32):
    """Custom type diffServMeterBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 524288),
    )


_DiffServMeterBurstSize_Type.__name__ = "Integer32"
_DiffServMeterBurstSize_Object = MibTableColumn
diffServMeterBurstSize = _DiffServMeterBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 20, 1, 4),
    _DiffServMeterBurstSize_Type()
)
diffServMeterBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterBurstSize.setStatus("current")
_DiffServMeterInterval_Type = Integer32
_DiffServMeterInterval_Object = MibTableColumn
diffServMeterInterval = _DiffServMeterInterval_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 20, 1, 5),
    _DiffServMeterInterval_Type()
)
diffServMeterInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterInterval.setStatus("current")
_DiffServMeterStatus_Type = RowStatus
_DiffServMeterStatus_Object = MibTableColumn
diffServMeterStatus = _DiffServMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 16, 4, 20, 1, 6),
    _DiffServMeterStatus_Type()
)
diffServMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterStatus.setStatus("current")
_SecurityMgt_ObjectIdentity = ObjectIdentity
securityMgt = _SecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17)
)
_PrivateVlanMgt_ObjectIdentity = ObjectIdentity
privateVlanMgt = _PrivateVlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1)
)
_PrivateVlanVlanTable_Object = MibTable
privateVlanVlanTable = _PrivateVlanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 4)
)
if mibBuilder.loadTexts:
    privateVlanVlanTable.setStatus("current")
_PrivateVlanVlanEntry_Object = MibTableRow
privateVlanVlanEntry = _PrivateVlanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 4, 1)
)
privateVlanVlanEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "privateVlanVlanIndex"),
)
if mibBuilder.loadTexts:
    privateVlanVlanEntry.setStatus("current")


class _PrivateVlanVlanIndex_Type(Integer32):
    """Custom type privateVlanVlanIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_PrivateVlanVlanIndex_Type.__name__ = "Integer32"
_PrivateVlanVlanIndex_Object = MibTableColumn
privateVlanVlanIndex = _PrivateVlanVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 4, 1, 1),
    _PrivateVlanVlanIndex_Type()
)
privateVlanVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateVlanVlanIndex.setStatus("current")


class _PrivateVlanVlanType_Type(Integer32):
    """Custom type privateVlanVlanType based on Integer32"""
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
        *(("invalid", 1),
          ("primary", 2),
          ("isolated", 3),
          ("community", 4))
    )


_PrivateVlanVlanType_Type.__name__ = "Integer32"
_PrivateVlanVlanType_Object = MibTableColumn
privateVlanVlanType = _PrivateVlanVlanType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 4, 1, 2),
    _PrivateVlanVlanType_Type()
)
privateVlanVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanVlanType.setStatus("current")


class _PrivateVlanAssoicatedPrimaryVlan_Type(Integer32):
    """Custom type privateVlanAssoicatedPrimaryVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PrivateVlanAssoicatedPrimaryVlan_Type.__name__ = "Integer32"
_PrivateVlanAssoicatedPrimaryVlan_Object = MibTableColumn
privateVlanAssoicatedPrimaryVlan = _PrivateVlanAssoicatedPrimaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 4, 1, 3),
    _PrivateVlanAssoicatedPrimaryVlan_Type()
)
privateVlanAssoicatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanAssoicatedPrimaryVlan.setStatus("current")
_PrivateVlanPrivatePortTable_Object = MibTable
privateVlanPrivatePortTable = _PrivateVlanPrivatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 5)
)
if mibBuilder.loadTexts:
    privateVlanPrivatePortTable.setStatus("current")
_PrivateVlanPrivatePortEntry_Object = MibTableRow
privateVlanPrivatePortEntry = _PrivateVlanPrivatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 5, 1)
)
privateVlanPrivatePortEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "privateVlanPrivatePortIfIndex"),
)
if mibBuilder.loadTexts:
    privateVlanPrivatePortEntry.setStatus("current")
_PrivateVlanPrivatePortIfIndex_Type = Integer32
_PrivateVlanPrivatePortIfIndex_Object = MibTableColumn
privateVlanPrivatePortIfIndex = _PrivateVlanPrivatePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 5, 1, 1),
    _PrivateVlanPrivatePortIfIndex_Type()
)
privateVlanPrivatePortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateVlanPrivatePortIfIndex.setStatus("current")


class _PrivateVlanPrivatePortSecondaryVlan_Type(Integer32):
    """Custom type privateVlanPrivatePortSecondaryVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PrivateVlanPrivatePortSecondaryVlan_Type.__name__ = "Integer32"
_PrivateVlanPrivatePortSecondaryVlan_Object = MibTableColumn
privateVlanPrivatePortSecondaryVlan = _PrivateVlanPrivatePortSecondaryVlan_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 5, 1, 2),
    _PrivateVlanPrivatePortSecondaryVlan_Type()
)
privateVlanPrivatePortSecondaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanPrivatePortSecondaryVlan.setStatus("current")
_PrivateVlanPromPortTable_Object = MibTable
privateVlanPromPortTable = _PrivateVlanPromPortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 6)
)
if mibBuilder.loadTexts:
    privateVlanPromPortTable.setStatus("current")
_PrivateVlanPromPortEntry_Object = MibTableRow
privateVlanPromPortEntry = _PrivateVlanPromPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 6, 1)
)
privateVlanPromPortEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "privateVlanPromPortIfIndex"),
)
if mibBuilder.loadTexts:
    privateVlanPromPortEntry.setStatus("current")
_PrivateVlanPromPortIfIndex_Type = Integer32
_PrivateVlanPromPortIfIndex_Object = MibTableColumn
privateVlanPromPortIfIndex = _PrivateVlanPromPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 6, 1, 1),
    _PrivateVlanPromPortIfIndex_Type()
)
privateVlanPromPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateVlanPromPortIfIndex.setStatus("current")


class _PrivateVlanPromPortPrimaryVlanId_Type(Integer32):
    """Custom type privateVlanPromPortPrimaryVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_PrivateVlanPromPortPrimaryVlanId_Type.__name__ = "Integer32"
_PrivateVlanPromPortPrimaryVlanId_Object = MibTableColumn
privateVlanPromPortPrimaryVlanId = _PrivateVlanPromPortPrimaryVlanId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 6, 1, 2),
    _PrivateVlanPromPortPrimaryVlanId_Type()
)
privateVlanPromPortPrimaryVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanPromPortPrimaryVlanId.setStatus("current")


class _PrivateVlanPromPortSecondaryRemap_Type(OctetString):
    """Custom type privateVlanPromPortSecondaryRemap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PrivateVlanPromPortSecondaryRemap_Type.__name__ = "OctetString"
_PrivateVlanPromPortSecondaryRemap_Object = MibTableColumn
privateVlanPromPortSecondaryRemap = _PrivateVlanPromPortSecondaryRemap_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 6, 1, 3),
    _PrivateVlanPromPortSecondaryRemap_Type()
)
privateVlanPromPortSecondaryRemap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVlanPromPortSecondaryRemap.setStatus("current")


class _PrivateVlanPromPortSecondaryRemap2k_Type(OctetString):
    """Custom type privateVlanPromPortSecondaryRemap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PrivateVlanPromPortSecondaryRemap2k_Type.__name__ = "OctetString"
_PrivateVlanPromPortSecondaryRemap2k_Object = MibTableColumn
privateVlanPromPortSecondaryRemap2k = _PrivateVlanPromPortSecondaryRemap2k_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 6, 1, 4),
    _PrivateVlanPromPortSecondaryRemap2k_Type()
)
privateVlanPromPortSecondaryRemap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVlanPromPortSecondaryRemap2k.setStatus("current")


class _PrivateVlanPromPortSecondaryRemap3k_Type(OctetString):
    """Custom type privateVlanPromPortSecondaryRemap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PrivateVlanPromPortSecondaryRemap3k_Type.__name__ = "OctetString"
_PrivateVlanPromPortSecondaryRemap3k_Object = MibTableColumn
privateVlanPromPortSecondaryRemap3k = _PrivateVlanPromPortSecondaryRemap3k_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 6, 1, 5),
    _PrivateVlanPromPortSecondaryRemap3k_Type()
)
privateVlanPromPortSecondaryRemap3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVlanPromPortSecondaryRemap3k.setStatus("current")


class _PrivateVlanPromPortSecondaryRemap4k_Type(OctetString):
    """Custom type privateVlanPromPortSecondaryRemap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_PrivateVlanPromPortSecondaryRemap4k_Type.__name__ = "OctetString"
_PrivateVlanPromPortSecondaryRemap4k_Object = MibTableColumn
privateVlanPromPortSecondaryRemap4k = _PrivateVlanPromPortSecondaryRemap4k_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 1, 6, 1, 6),
    _PrivateVlanPromPortSecondaryRemap4k_Type()
)
privateVlanPromPortSecondaryRemap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVlanPromPortSecondaryRemap4k.setStatus("current")
_PortSecurityMgt_ObjectIdentity = ObjectIdentity
portSecurityMgt = _PortSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 2)
)
_PortSecPortTable_Object = MibTable
portSecPortTable = _PortSecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    portSecPortTable.setStatus("current")
_PortSecPortEntry_Object = MibTableRow
portSecPortEntry = _PortSecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 2, 1, 1)
)
portSecPortEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "portSecPortIndex"),
)
if mibBuilder.loadTexts:
    portSecPortEntry.setStatus("current")
_PortSecPortIndex_Type = Integer32
_PortSecPortIndex_Object = MibTableColumn
portSecPortIndex = _PortSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 2, 1, 1, 1),
    _PortSecPortIndex_Type()
)
portSecPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSecPortIndex.setStatus("current")
_PortSecPortStatus_Type = EnabledStatus
_PortSecPortStatus_Object = MibTableColumn
portSecPortStatus = _PortSecPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 2, 1, 1, 2),
    _PortSecPortStatus_Type()
)
portSecPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecPortStatus.setStatus("current")


class _PortSecAction_Type(Integer32):
    """Custom type portSecAction based on Integer32"""
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
        *(("none", 1),
          ("trap", 2),
          ("shutdown", 3),
          ("trapAndShutdown", 4))
    )


_PortSecAction_Type.__name__ = "Integer32"
_PortSecAction_Object = MibTableColumn
portSecAction = _PortSecAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 2, 1, 1, 3),
    _PortSecAction_Type()
)
portSecAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecAction.setStatus("current")


class _PortSecMaxMacCount_Type(Integer32):
    """Custom type portSecMaxMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_PortSecMaxMacCount_Type.__name__ = "Integer32"
_PortSecMaxMacCount_Object = MibTableColumn
portSecMaxMacCount = _PortSecMaxMacCount_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 2, 1, 1, 4),
    _PortSecMaxMacCount_Type()
)
portSecMaxMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMaxMacCount.setStatus("current")
_RadiusMgt_ObjectIdentity = ObjectIdentity
radiusMgt = _RadiusMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4)
)


class _RadiusServerPortNumber_Type(Integer32):
    """Custom type radiusServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerPortNumber_Type.__name__ = "Integer32"
_RadiusServerPortNumber_Object = MibScalar
radiusServerPortNumber = _RadiusServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 2),
    _RadiusServerPortNumber_Type()
)
radiusServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerPortNumber.setStatus("current")


class _RadiusServerKey_Type(DisplayString):
    """Custom type radiusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RadiusServerKey_Type.__name__ = "DisplayString"
_RadiusServerKey_Object = MibScalar
radiusServerKey = _RadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 3),
    _RadiusServerKey_Type()
)
radiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerKey.setStatus("current")


class _RadiusServerRetransmit_Type(Integer32):
    """Custom type radiusServerRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RadiusServerRetransmit_Type.__name__ = "Integer32"
_RadiusServerRetransmit_Object = MibScalar
radiusServerRetransmit = _RadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 4),
    _RadiusServerRetransmit_Type()
)
radiusServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerRetransmit.setStatus("current")


class _RadiusServerTimeout_Type(Integer32):
    """Custom type radiusServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerTimeout_Type.__name__ = "Integer32"
_RadiusServerTimeout_Object = MibScalar
radiusServerTimeout = _RadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 5),
    _RadiusServerTimeout_Type()
)
radiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    radiusServerTimeout.setUnits("seconds")
_RadiusMultipleServerTable_Object = MibTable
radiusMultipleServerTable = _RadiusMultipleServerTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 7)
)
if mibBuilder.loadTexts:
    radiusMultipleServerTable.setStatus("current")
_RadiusMultipleServerEntry_Object = MibTableRow
radiusMultipleServerEntry = _RadiusMultipleServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 7, 1)
)
radiusMultipleServerEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "radiusMultipleServerIndex"),
)
if mibBuilder.loadTexts:
    radiusMultipleServerEntry.setStatus("current")
_RadiusMultipleServerIndex_Type = Integer32
_RadiusMultipleServerIndex_Object = MibTableColumn
radiusMultipleServerIndex = _RadiusMultipleServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 7, 1, 1),
    _RadiusMultipleServerIndex_Type()
)
radiusMultipleServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusMultipleServerIndex.setStatus("current")
_RadiusMultipleServerAddress_Type = IpAddress
_RadiusMultipleServerAddress_Object = MibTableColumn
radiusMultipleServerAddress = _RadiusMultipleServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 7, 1, 2),
    _RadiusMultipleServerAddress_Type()
)
radiusMultipleServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerAddress.setStatus("current")


class _RadiusMultipleServerPortNumber_Type(Integer32):
    """Custom type radiusMultipleServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusMultipleServerPortNumber_Type.__name__ = "Integer32"
_RadiusMultipleServerPortNumber_Object = MibTableColumn
radiusMultipleServerPortNumber = _RadiusMultipleServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 7, 1, 3),
    _RadiusMultipleServerPortNumber_Type()
)
radiusMultipleServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerPortNumber.setStatus("current")


class _RadiusMultipleServerKey_Type(DisplayString):
    """Custom type radiusMultipleServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RadiusMultipleServerKey_Type.__name__ = "DisplayString"
_RadiusMultipleServerKey_Object = MibTableColumn
radiusMultipleServerKey = _RadiusMultipleServerKey_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 7, 1, 4),
    _RadiusMultipleServerKey_Type()
)
radiusMultipleServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerKey.setStatus("current")


class _RadiusMultipleServerRetransmit_Type(Integer32):
    """Custom type radiusMultipleServerRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RadiusMultipleServerRetransmit_Type.__name__ = "Integer32"
_RadiusMultipleServerRetransmit_Object = MibTableColumn
radiusMultipleServerRetransmit = _RadiusMultipleServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 7, 1, 5),
    _RadiusMultipleServerRetransmit_Type()
)
radiusMultipleServerRetransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerRetransmit.setStatus("current")


class _RadiusMultipleServerTimeout_Type(Integer32):
    """Custom type radiusMultipleServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusMultipleServerTimeout_Type.__name__ = "Integer32"
_RadiusMultipleServerTimeout_Object = MibTableColumn
radiusMultipleServerTimeout = _RadiusMultipleServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 7, 1, 6),
    _RadiusMultipleServerTimeout_Type()
)
radiusMultipleServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    radiusMultipleServerTimeout.setUnits("seconds")
_RadiusMultipleServerStatus_Type = ValidStatus
_RadiusMultipleServerStatus_Object = MibTableColumn
radiusMultipleServerStatus = _RadiusMultipleServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 4, 7, 1, 8),
    _RadiusMultipleServerStatus_Type()
)
radiusMultipleServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerStatus.setStatus("current")
_TacacsMgt_ObjectIdentity = ObjectIdentity
tacacsMgt = _TacacsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 5)
)
_TacacsServerAddress_Type = IpAddress
_TacacsServerAddress_Object = MibScalar
tacacsServerAddress = _TacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 5, 1),
    _TacacsServerAddress_Type()
)
tacacsServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerAddress.setStatus("current")


class _TacacsServerPortNumber_Type(Integer32):
    """Custom type tacacsServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsServerPortNumber_Type.__name__ = "Integer32"
_TacacsServerPortNumber_Object = MibScalar
tacacsServerPortNumber = _TacacsServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 5, 2),
    _TacacsServerPortNumber_Type()
)
tacacsServerPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerPortNumber.setStatus("current")


class _TacacsServerKey_Type(DisplayString):
    """Custom type tacacsServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TacacsServerKey_Type.__name__ = "DisplayString"
_TacacsServerKey_Object = MibScalar
tacacsServerKey = _TacacsServerKey_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 5, 3),
    _TacacsServerKey_Type()
)
tacacsServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerKey.setStatus("current")
_SshMgt_ObjectIdentity = ObjectIdentity
sshMgt = _SshMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6)
)
_SshServerStatus_Type = EnabledStatus
_SshServerStatus_Object = MibScalar
sshServerStatus = _SshServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 1),
    _SshServerStatus_Type()
)
sshServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerStatus.setStatus("current")
_SshServerMajorVersion_Type = Integer32
_SshServerMajorVersion_Object = MibScalar
sshServerMajorVersion = _SshServerMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 2),
    _SshServerMajorVersion_Type()
)
sshServerMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMajorVersion.setStatus("current")
_SshServerMinorVersion_Type = Integer32
_SshServerMinorVersion_Object = MibScalar
sshServerMinorVersion = _SshServerMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 3),
    _SshServerMinorVersion_Type()
)
sshServerMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMinorVersion.setStatus("current")


class _SshTimeout_Type(Integer32):
    """Custom type sshTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_SshTimeout_Type.__name__ = "Integer32"
_SshTimeout_Object = MibScalar
sshTimeout = _SshTimeout_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 4),
    _SshTimeout_Type()
)
sshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshTimeout.setStatus("current")
if mibBuilder.loadTexts:
    sshTimeout.setUnits("seconds")


class _SshAuthRetries_Type(Integer32):
    """Custom type sshAuthRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SshAuthRetries_Type.__name__ = "Integer32"
_SshAuthRetries_Object = MibScalar
sshAuthRetries = _SshAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 5),
    _SshAuthRetries_Type()
)
sshAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAuthRetries.setStatus("current")
_SshConnInfoTable_Object = MibTable
sshConnInfoTable = _SshConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 6)
)
if mibBuilder.loadTexts:
    sshConnInfoTable.setStatus("current")
_SshConnInfoEntry_Object = MibTableRow
sshConnInfoEntry = _SshConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 6, 1)
)
sshConnInfoEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "sshConnID"),
)
if mibBuilder.loadTexts:
    sshConnInfoEntry.setStatus("current")
_SshConnID_Type = Integer32
_SshConnID_Object = MibTableColumn
sshConnID = _SshConnID_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 6, 1, 1),
    _SshConnID_Type()
)
sshConnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshConnID.setStatus("current")
_SshConnMajorVersion_Type = Integer32
_SshConnMajorVersion_Object = MibTableColumn
sshConnMajorVersion = _SshConnMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 6, 1, 2),
    _SshConnMajorVersion_Type()
)
sshConnMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMajorVersion.setStatus("current")
_SshConnMinorVersion_Type = Integer32
_SshConnMinorVersion_Object = MibTableColumn
sshConnMinorVersion = _SshConnMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 6, 1, 3),
    _SshConnMinorVersion_Type()
)
sshConnMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMinorVersion.setStatus("current")


class _SshConnStatus_Type(Integer32):
    """Custom type sshConnStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("negotiationStart", 1),
          ("authenticationStart", 2),
          ("sessionStart", 3))
    )


_SshConnStatus_Type.__name__ = "Integer32"
_SshConnStatus_Object = MibTableColumn
sshConnStatus = _SshConnStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 6, 1, 5),
    _SshConnStatus_Type()
)
sshConnStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnStatus.setStatus("current")


class _SshConnUserName_Type(DisplayString):
    """Custom type sshConnUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SshConnUserName_Type.__name__ = "DisplayString"
_SshConnUserName_Object = MibTableColumn
sshConnUserName = _SshConnUserName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 6, 1, 6),
    _SshConnUserName_Type()
)
sshConnUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnUserName.setStatus("current")


class _SshDisconnect_Type(Integer32):
    """Custom type sshDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDisconnect", 1),
          ("disconnect", 2))
    )


_SshDisconnect_Type.__name__ = "Integer32"
_SshDisconnect_Object = MibTableColumn
sshDisconnect = _SshDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 6, 1, 7),
    _SshDisconnect_Type()
)
sshDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshDisconnect.setStatus("current")


class _SshConnEncryptionTypeStr_Type(DisplayString):
    """Custom type sshConnEncryptionTypeStr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_SshConnEncryptionTypeStr_Type.__name__ = "DisplayString"
_SshConnEncryptionTypeStr_Object = MibTableColumn
sshConnEncryptionTypeStr = _SshConnEncryptionTypeStr_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 6, 1, 8),
    _SshConnEncryptionTypeStr_Type()
)
sshConnEncryptionTypeStr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnEncryptionTypeStr.setStatus("current")


class _SshKeySize_Type(Integer32):
    """Custom type sshKeySize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(512, 896),
    )


_SshKeySize_Type.__name__ = "Integer32"
_SshKeySize_Object = MibScalar
sshKeySize = _SshKeySize_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 7),
    _SshKeySize_Type()
)
sshKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshKeySize.setStatus("current")
_SshRsaHostKey1_Type = KeySegment
_SshRsaHostKey1_Object = MibScalar
sshRsaHostKey1 = _SshRsaHostKey1_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 8),
    _SshRsaHostKey1_Type()
)
sshRsaHostKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey1.setStatus("current")
_SshRsaHostKey2_Type = KeySegment
_SshRsaHostKey2_Object = MibScalar
sshRsaHostKey2 = _SshRsaHostKey2_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 9),
    _SshRsaHostKey2_Type()
)
sshRsaHostKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey2.setStatus("current")
_SshRsaHostKey3_Type = KeySegment
_SshRsaHostKey3_Object = MibScalar
sshRsaHostKey3 = _SshRsaHostKey3_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 10),
    _SshRsaHostKey3_Type()
)
sshRsaHostKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey3.setStatus("current")
_SshRsaHostKey4_Type = KeySegment
_SshRsaHostKey4_Object = MibScalar
sshRsaHostKey4 = _SshRsaHostKey4_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 11),
    _SshRsaHostKey4_Type()
)
sshRsaHostKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey4.setStatus("current")
_SshRsaHostKey5_Type = KeySegment
_SshRsaHostKey5_Object = MibScalar
sshRsaHostKey5 = _SshRsaHostKey5_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 12),
    _SshRsaHostKey5_Type()
)
sshRsaHostKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey5.setStatus("current")
_SshRsaHostKey6_Type = KeySegment
_SshRsaHostKey6_Object = MibScalar
sshRsaHostKey6 = _SshRsaHostKey6_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 13),
    _SshRsaHostKey6_Type()
)
sshRsaHostKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey6.setStatus("current")
_SshRsaHostKey7_Type = KeySegment
_SshRsaHostKey7_Object = MibScalar
sshRsaHostKey7 = _SshRsaHostKey7_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 14),
    _SshRsaHostKey7_Type()
)
sshRsaHostKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey7.setStatus("current")
_SshRsaHostKey8_Type = KeySegment
_SshRsaHostKey8_Object = MibScalar
sshRsaHostKey8 = _SshRsaHostKey8_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 15),
    _SshRsaHostKey8_Type()
)
sshRsaHostKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey8.setStatus("current")
_SshDsaHostKey1_Type = KeySegment
_SshDsaHostKey1_Object = MibScalar
sshDsaHostKey1 = _SshDsaHostKey1_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 16),
    _SshDsaHostKey1_Type()
)
sshDsaHostKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey1.setStatus("current")
_SshDsaHostKey2_Type = KeySegment
_SshDsaHostKey2_Object = MibScalar
sshDsaHostKey2 = _SshDsaHostKey2_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 17),
    _SshDsaHostKey2_Type()
)
sshDsaHostKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey2.setStatus("current")
_SshDsaHostKey3_Type = KeySegment
_SshDsaHostKey3_Object = MibScalar
sshDsaHostKey3 = _SshDsaHostKey3_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 18),
    _SshDsaHostKey3_Type()
)
sshDsaHostKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey3.setStatus("current")
_SshDsaHostKey4_Type = KeySegment
_SshDsaHostKey4_Object = MibScalar
sshDsaHostKey4 = _SshDsaHostKey4_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 19),
    _SshDsaHostKey4_Type()
)
sshDsaHostKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey4.setStatus("current")
_SshDsaHostKey5_Type = KeySegment
_SshDsaHostKey5_Object = MibScalar
sshDsaHostKey5 = _SshDsaHostKey5_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 20),
    _SshDsaHostKey5_Type()
)
sshDsaHostKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey5.setStatus("current")
_SshDsaHostKey6_Type = KeySegment
_SshDsaHostKey6_Object = MibScalar
sshDsaHostKey6 = _SshDsaHostKey6_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 21),
    _SshDsaHostKey6_Type()
)
sshDsaHostKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey6.setStatus("current")
_SshDsaHostKey7_Type = KeySegment
_SshDsaHostKey7_Object = MibScalar
sshDsaHostKey7 = _SshDsaHostKey7_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 22),
    _SshDsaHostKey7_Type()
)
sshDsaHostKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey7.setStatus("current")
_SshDsaHostKey8_Type = KeySegment
_SshDsaHostKey8_Object = MibScalar
sshDsaHostKey8 = _SshDsaHostKey8_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 23),
    _SshDsaHostKey8_Type()
)
sshDsaHostKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey8.setStatus("current")


class _SshHostKeyGenAction_Type(Integer32):
    """Custom type sshHostKeyGenAction based on Integer32"""
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
        *(("noGen", 1),
          ("genRsaKey", 2),
          ("genDsaKey", 3),
          ("genBothKeys", 4))
    )


_SshHostKeyGenAction_Type.__name__ = "Integer32"
_SshHostKeyGenAction_Object = MibScalar
sshHostKeyGenAction = _SshHostKeyGenAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 24),
    _SshHostKeyGenAction_Type()
)
sshHostKeyGenAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyGenAction.setStatus("current")


class _SshHostKeyGenStatus_Type(Integer32):
    """Custom type sshHostKeyGenStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("success", 2),
          ("failure", 3))
    )


_SshHostKeyGenStatus_Type.__name__ = "Integer32"
_SshHostKeyGenStatus_Object = MibScalar
sshHostKeyGenStatus = _SshHostKeyGenStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 25),
    _SshHostKeyGenStatus_Type()
)
sshHostKeyGenStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshHostKeyGenStatus.setStatus("current")


class _SshHostKeySaveAction_Type(Integer32):
    """Custom type sshHostKeySaveAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noSave", 1),
          ("save", 2))
    )


_SshHostKeySaveAction_Type.__name__ = "Integer32"
_SshHostKeySaveAction_Object = MibScalar
sshHostKeySaveAction = _SshHostKeySaveAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 26),
    _SshHostKeySaveAction_Type()
)
sshHostKeySaveAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeySaveAction.setStatus("current")


class _SshHostKeySaveStatus_Type(Integer32):
    """Custom type sshHostKeySaveStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("success", 2),
          ("failure", 3))
    )


_SshHostKeySaveStatus_Type.__name__ = "Integer32"
_SshHostKeySaveStatus_Object = MibScalar
sshHostKeySaveStatus = _SshHostKeySaveStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 27),
    _SshHostKeySaveStatus_Type()
)
sshHostKeySaveStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshHostKeySaveStatus.setStatus("current")


class _SshHostKeyDelAction_Type(Integer32):
    """Custom type sshHostKeyDelAction based on Integer32"""
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
        *(("noDel", 1),
          ("delRsaKey", 2),
          ("delDsaKey", 3),
          ("delBothKeys", 4))
    )


_SshHostKeyDelAction_Type.__name__ = "Integer32"
_SshHostKeyDelAction_Object = MibScalar
sshHostKeyDelAction = _SshHostKeyDelAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 28),
    _SshHostKeyDelAction_Type()
)
sshHostKeyDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyDelAction.setStatus("current")
_SshUserTable_Object = MibTable
sshUserTable = _SshUserTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29)
)
if mibBuilder.loadTexts:
    sshUserTable.setStatus("current")
_SshUserEntry_Object = MibTableRow
sshUserEntry = _SshUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1)
)
sshUserEntry.setIndexNames(
    (1, "SMC6152L2-MIB", "sshUserName"),
)
if mibBuilder.loadTexts:
    sshUserEntry.setStatus("current")


class _SshUserName_Type(DisplayString):
    """Custom type sshUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 8),
    )


_SshUserName_Type.__name__ = "DisplayString"
_SshUserName_Object = MibTableColumn
sshUserName = _SshUserName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 1),
    _SshUserName_Type()
)
sshUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshUserName.setStatus("current")
_SshUserRsaKey1_Type = KeySegment
_SshUserRsaKey1_Object = MibTableColumn
sshUserRsaKey1 = _SshUserRsaKey1_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 2),
    _SshUserRsaKey1_Type()
)
sshUserRsaKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey1.setStatus("current")
_SshUserRsaKey2_Type = KeySegment
_SshUserRsaKey2_Object = MibTableColumn
sshUserRsaKey2 = _SshUserRsaKey2_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 3),
    _SshUserRsaKey2_Type()
)
sshUserRsaKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey2.setStatus("current")
_SshUserRsaKey3_Type = KeySegment
_SshUserRsaKey3_Object = MibTableColumn
sshUserRsaKey3 = _SshUserRsaKey3_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 4),
    _SshUserRsaKey3_Type()
)
sshUserRsaKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey3.setStatus("current")
_SshUserRsaKey4_Type = KeySegment
_SshUserRsaKey4_Object = MibTableColumn
sshUserRsaKey4 = _SshUserRsaKey4_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 5),
    _SshUserRsaKey4_Type()
)
sshUserRsaKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey4.setStatus("current")
_SshUserRsaKey5_Type = KeySegment
_SshUserRsaKey5_Object = MibTableColumn
sshUserRsaKey5 = _SshUserRsaKey5_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 6),
    _SshUserRsaKey5_Type()
)
sshUserRsaKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey5.setStatus("current")
_SshUserRsaKey6_Type = KeySegment
_SshUserRsaKey6_Object = MibTableColumn
sshUserRsaKey6 = _SshUserRsaKey6_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 7),
    _SshUserRsaKey6_Type()
)
sshUserRsaKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey6.setStatus("current")
_SshUserRsaKey7_Type = KeySegment
_SshUserRsaKey7_Object = MibTableColumn
sshUserRsaKey7 = _SshUserRsaKey7_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 8),
    _SshUserRsaKey7_Type()
)
sshUserRsaKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey7.setStatus("current")
_SshUserRsaKey8_Type = KeySegment
_SshUserRsaKey8_Object = MibTableColumn
sshUserRsaKey8 = _SshUserRsaKey8_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 9),
    _SshUserRsaKey8_Type()
)
sshUserRsaKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey8.setStatus("current")
_SshUserDsaKey1_Type = KeySegment
_SshUserDsaKey1_Object = MibTableColumn
sshUserDsaKey1 = _SshUserDsaKey1_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 10),
    _SshUserDsaKey1_Type()
)
sshUserDsaKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey1.setStatus("current")
_SshUserDsaKey2_Type = KeySegment
_SshUserDsaKey2_Object = MibTableColumn
sshUserDsaKey2 = _SshUserDsaKey2_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 11),
    _SshUserDsaKey2_Type()
)
sshUserDsaKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey2.setStatus("current")
_SshUserDsaKey3_Type = KeySegment
_SshUserDsaKey3_Object = MibTableColumn
sshUserDsaKey3 = _SshUserDsaKey3_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 12),
    _SshUserDsaKey3_Type()
)
sshUserDsaKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey3.setStatus("current")
_SshUserDsaKey4_Type = KeySegment
_SshUserDsaKey4_Object = MibTableColumn
sshUserDsaKey4 = _SshUserDsaKey4_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 13),
    _SshUserDsaKey4_Type()
)
sshUserDsaKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey4.setStatus("current")
_SshUserDsaKey5_Type = KeySegment
_SshUserDsaKey5_Object = MibTableColumn
sshUserDsaKey5 = _SshUserDsaKey5_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 14),
    _SshUserDsaKey5_Type()
)
sshUserDsaKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey5.setStatus("current")
_SshUserDsaKey6_Type = KeySegment
_SshUserDsaKey6_Object = MibTableColumn
sshUserDsaKey6 = _SshUserDsaKey6_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 15),
    _SshUserDsaKey6_Type()
)
sshUserDsaKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey6.setStatus("current")
_SshUserDsaKey7_Type = KeySegment
_SshUserDsaKey7_Object = MibTableColumn
sshUserDsaKey7 = _SshUserDsaKey7_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 16),
    _SshUserDsaKey7_Type()
)
sshUserDsaKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey7.setStatus("current")
_SshUserDsaKey8_Type = KeySegment
_SshUserDsaKey8_Object = MibTableColumn
sshUserDsaKey8 = _SshUserDsaKey8_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 17),
    _SshUserDsaKey8_Type()
)
sshUserDsaKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey8.setStatus("current")


class _SshUserKeyDelAction_Type(Integer32):
    """Custom type sshUserKeyDelAction based on Integer32"""
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
        *(("noDel", 1),
          ("delRsaKey", 2),
          ("delDsaKey", 3),
          ("delBothKeys", 4))
    )


_SshUserKeyDelAction_Type.__name__ = "Integer32"
_SshUserKeyDelAction_Object = MibTableColumn
sshUserKeyDelAction = _SshUserKeyDelAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 29, 1, 18),
    _SshUserKeyDelAction_Type()
)
sshUserKeyDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshUserKeyDelAction.setStatus("current")


class _SshRsaHostKeySHA1FingerPrint_Type(DisplayString):
    """Custom type sshRsaHostKeySHA1FingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(65, 65),
    )
    fixed_length = 65


_SshRsaHostKeySHA1FingerPrint_Type.__name__ = "DisplayString"
_SshRsaHostKeySHA1FingerPrint_Object = MibScalar
sshRsaHostKeySHA1FingerPrint = _SshRsaHostKeySHA1FingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 30),
    _SshRsaHostKeySHA1FingerPrint_Type()
)
sshRsaHostKeySHA1FingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKeySHA1FingerPrint.setStatus("current")


class _SshRsaHostKeyMD5FingerPrint_Type(DisplayString):
    """Custom type sshRsaHostKeyMD5FingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(47, 47),
    )
    fixed_length = 47


_SshRsaHostKeyMD5FingerPrint_Type.__name__ = "DisplayString"
_SshRsaHostKeyMD5FingerPrint_Object = MibScalar
sshRsaHostKeyMD5FingerPrint = _SshRsaHostKeyMD5FingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 31),
    _SshRsaHostKeyMD5FingerPrint_Type()
)
sshRsaHostKeyMD5FingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKeyMD5FingerPrint.setStatus("current")


class _SshDsaHostKeySHA1FingerPrint_Type(DisplayString):
    """Custom type sshDsaHostKeySHA1FingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(65, 65),
    )
    fixed_length = 65


_SshDsaHostKeySHA1FingerPrint_Type.__name__ = "DisplayString"
_SshDsaHostKeySHA1FingerPrint_Object = MibScalar
sshDsaHostKeySHA1FingerPrint = _SshDsaHostKeySHA1FingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 32),
    _SshDsaHostKeySHA1FingerPrint_Type()
)
sshDsaHostKeySHA1FingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKeySHA1FingerPrint.setStatus("current")


class _SshDsaHostKeyMD5FingerPrint_Type(DisplayString):
    """Custom type sshDsaHostKeyMD5FingerPrint based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(47, 47),
    )
    fixed_length = 47


_SshDsaHostKeyMD5FingerPrint_Type.__name__ = "DisplayString"
_SshDsaHostKeyMD5FingerPrint_Object = MibScalar
sshDsaHostKeyMD5FingerPrint = _SshDsaHostKeyMD5FingerPrint_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 6, 33),
    _SshDsaHostKeyMD5FingerPrint_Type()
)
sshDsaHostKeyMD5FingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKeyMD5FingerPrint.setStatus("current")
_AclMgt_ObjectIdentity = ObjectIdentity
aclMgt = _AclMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 7)
)
_IpFilterMgt_ObjectIdentity = ObjectIdentity
ipFilterMgt = _IpFilterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9)
)
_IpFilterSnmpTable_Object = MibTable
ipFilterSnmpTable = _IpFilterSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 1)
)
if mibBuilder.loadTexts:
    ipFilterSnmpTable.setStatus("current")
_IpFilterSnmpEntry_Object = MibTableRow
ipFilterSnmpEntry = _IpFilterSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 1, 1)
)
ipFilterSnmpEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "ipFilterSnmpStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterSnmpEntry.setStatus("current")
_IpFilterSnmpStartAddress_Type = IpAddress
_IpFilterSnmpStartAddress_Object = MibTableColumn
ipFilterSnmpStartAddress = _IpFilterSnmpStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 1, 1, 1),
    _IpFilterSnmpStartAddress_Type()
)
ipFilterSnmpStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterSnmpStartAddress.setStatus("current")
_IpFilterSnmpEndAddress_Type = IpAddress
_IpFilterSnmpEndAddress_Object = MibTableColumn
ipFilterSnmpEndAddress = _IpFilterSnmpEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 1, 1, 2),
    _IpFilterSnmpEndAddress_Type()
)
ipFilterSnmpEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpEndAddress.setStatus("current")
_IpFilterSnmpStatus_Type = ValidStatus
_IpFilterSnmpStatus_Object = MibTableColumn
ipFilterSnmpStatus = _IpFilterSnmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 1, 1, 3),
    _IpFilterSnmpStatus_Type()
)
ipFilterSnmpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpStatus.setStatus("current")
_IpFilterHTTPTable_Object = MibTable
ipFilterHTTPTable = _IpFilterHTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 2)
)
if mibBuilder.loadTexts:
    ipFilterHTTPTable.setStatus("current")
_IpFilterHTTPEntry_Object = MibTableRow
ipFilterHTTPEntry = _IpFilterHTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 2, 1)
)
ipFilterHTTPEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "ipFilterHTTPStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterHTTPEntry.setStatus("current")
_IpFilterHTTPStartAddress_Type = IpAddress
_IpFilterHTTPStartAddress_Object = MibTableColumn
ipFilterHTTPStartAddress = _IpFilterHTTPStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 2, 1, 1),
    _IpFilterHTTPStartAddress_Type()
)
ipFilterHTTPStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterHTTPStartAddress.setStatus("current")
_IpFilterHTTPEndAddress_Type = IpAddress
_IpFilterHTTPEndAddress_Object = MibTableColumn
ipFilterHTTPEndAddress = _IpFilterHTTPEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 2, 1, 2),
    _IpFilterHTTPEndAddress_Type()
)
ipFilterHTTPEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHTTPEndAddress.setStatus("current")
_IpFilterHTTPStatus_Type = ValidStatus
_IpFilterHTTPStatus_Object = MibTableColumn
ipFilterHTTPStatus = _IpFilterHTTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 2, 1, 3),
    _IpFilterHTTPStatus_Type()
)
ipFilterHTTPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHTTPStatus.setStatus("current")
_IpFilterTelnetTable_Object = MibTable
ipFilterTelnetTable = _IpFilterTelnetTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 3)
)
if mibBuilder.loadTexts:
    ipFilterTelnetTable.setStatus("current")
_IpFilterTelnetEntry_Object = MibTableRow
ipFilterTelnetEntry = _IpFilterTelnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 3, 1)
)
ipFilterTelnetEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "ipFilterTelnetStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterTelnetEntry.setStatus("current")
_IpFilterTelnetStartAddress_Type = IpAddress
_IpFilterTelnetStartAddress_Object = MibTableColumn
ipFilterTelnetStartAddress = _IpFilterTelnetStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 3, 1, 1),
    _IpFilterTelnetStartAddress_Type()
)
ipFilterTelnetStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterTelnetStartAddress.setStatus("current")
_IpFilterTelnetEndAddress_Type = IpAddress
_IpFilterTelnetEndAddress_Object = MibTableColumn
ipFilterTelnetEndAddress = _IpFilterTelnetEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 3, 1, 2),
    _IpFilterTelnetEndAddress_Type()
)
ipFilterTelnetEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetEndAddress.setStatus("current")
_IpFilterTelnetStatus_Type = ValidStatus
_IpFilterTelnetStatus_Object = MibTableColumn
ipFilterTelnetStatus = _IpFilterTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 17, 9, 3, 1, 3),
    _IpFilterTelnetStatus_Type()
)
ipFilterTelnetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetStatus.setStatus("current")
_SysLogMgt_ObjectIdentity = ObjectIdentity
sysLogMgt = _SysLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19)
)
_SysLogStatus_Type = EnabledStatus
_SysLogStatus_Object = MibScalar
sysLogStatus = _SysLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 1),
    _SysLogStatus_Type()
)
sysLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogStatus.setStatus("current")


class _SysLogHistoryFlashLevel_Type(Integer32):
    """Custom type sysLogHistoryFlashLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SysLogHistoryFlashLevel_Type.__name__ = "Integer32"
_SysLogHistoryFlashLevel_Object = MibScalar
sysLogHistoryFlashLevel = _SysLogHistoryFlashLevel_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 2),
    _SysLogHistoryFlashLevel_Type()
)
sysLogHistoryFlashLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryFlashLevel.setStatus("current")


class _SysLogHistoryRamLevel_Type(Integer32):
    """Custom type sysLogHistoryRamLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SysLogHistoryRamLevel_Type.__name__ = "Integer32"
_SysLogHistoryRamLevel_Object = MibScalar
sysLogHistoryRamLevel = _SysLogHistoryRamLevel_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 3),
    _SysLogHistoryRamLevel_Type()
)
sysLogHistoryRamLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryRamLevel.setStatus("current")
_RemoteLogMgt_ObjectIdentity = ObjectIdentity
remoteLogMgt = _RemoteLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 6)
)
_RemoteLogStatus_Type = EnabledStatus
_RemoteLogStatus_Object = MibScalar
remoteLogStatus = _RemoteLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 6, 1),
    _RemoteLogStatus_Type()
)
remoteLogStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogStatus.setStatus("current")


class _RemoteLogLevel_Type(Integer32):
    """Custom type remoteLogLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RemoteLogLevel_Type.__name__ = "Integer32"
_RemoteLogLevel_Object = MibScalar
remoteLogLevel = _RemoteLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 6, 2),
    _RemoteLogLevel_Type()
)
remoteLogLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogLevel.setStatus("current")


class _RemoteLogFacilityType_Type(Integer32):
    """Custom type remoteLogFacilityType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(16,
              17,
              18,
              19,
              20,
              21,
              22,
              23)
        )
    )
    namedValues = NamedValues(
        *(("localUse0", 16),
          ("localUse1", 17),
          ("localUse2", 18),
          ("localUse3", 19),
          ("localUse4", 20),
          ("localUse5", 21),
          ("localUse6", 22),
          ("localUse7", 23))
    )


_RemoteLogFacilityType_Type.__name__ = "Integer32"
_RemoteLogFacilityType_Object = MibScalar
remoteLogFacilityType = _RemoteLogFacilityType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 6, 3),
    _RemoteLogFacilityType_Type()
)
remoteLogFacilityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogFacilityType.setStatus("current")
_RemoteLogServerTable_Object = MibTable
remoteLogServerTable = _RemoteLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 6, 4)
)
if mibBuilder.loadTexts:
    remoteLogServerTable.setStatus("current")
_RemoteLogServerEntry_Object = MibTableRow
remoteLogServerEntry = _RemoteLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 6, 4, 1)
)
remoteLogServerEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "remoteLogServerIp"),
)
if mibBuilder.loadTexts:
    remoteLogServerEntry.setStatus("current")
_RemoteLogServerIp_Type = IpAddress
_RemoteLogServerIp_Object = MibTableColumn
remoteLogServerIp = _RemoteLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 6, 4, 1, 1),
    _RemoteLogServerIp_Type()
)
remoteLogServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteLogServerIp.setStatus("current")
_RemoteLogServerStatus_Type = ValidStatus
_RemoteLogServerStatus_Object = MibTableColumn
remoteLogServerStatus = _RemoteLogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 6, 4, 1, 2),
    _RemoteLogServerStatus_Type()
)
remoteLogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteLogServerStatus.setStatus("current")
_SmtpMgt_ObjectIdentity = ObjectIdentity
smtpMgt = _SmtpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7)
)
_SmtpStatus_Type = EnabledStatus
_SmtpStatus_Object = MibScalar
smtpStatus = _SmtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 1),
    _SmtpStatus_Type()
)
smtpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpStatus.setStatus("current")


class _SmtpSeverityLevel_Type(Integer32):
    """Custom type smtpSeverityLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SmtpSeverityLevel_Type.__name__ = "Integer32"
_SmtpSeverityLevel_Object = MibScalar
smtpSeverityLevel = _SmtpSeverityLevel_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 2),
    _SmtpSeverityLevel_Type()
)
smtpSeverityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSeverityLevel.setStatus("current")


class _SmtpSourceEMail_Type(DisplayString):
    """Custom type smtpSourceEMail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_SmtpSourceEMail_Type.__name__ = "DisplayString"
_SmtpSourceEMail_Object = MibScalar
smtpSourceEMail = _SmtpSourceEMail_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 3),
    _SmtpSourceEMail_Type()
)
smtpSourceEMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSourceEMail.setStatus("current")
_SmtpServerIpTable_Object = MibTable
smtpServerIpTable = _SmtpServerIpTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 4)
)
if mibBuilder.loadTexts:
    smtpServerIpTable.setStatus("current")
_SmtpServerIpEntry_Object = MibTableRow
smtpServerIpEntry = _SmtpServerIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 4, 1)
)
smtpServerIpEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "smtpServerIp"),
)
if mibBuilder.loadTexts:
    smtpServerIpEntry.setStatus("current")
_SmtpServerIp_Type = IpAddress
_SmtpServerIp_Object = MibTableColumn
smtpServerIp = _SmtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 4, 1, 1),
    _SmtpServerIp_Type()
)
smtpServerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smtpServerIp.setStatus("current")
_SmtpServerIpStatus_Type = ValidStatus
_SmtpServerIpStatus_Object = MibTableColumn
smtpServerIpStatus = _SmtpServerIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 4, 1, 2),
    _SmtpServerIpStatus_Type()
)
smtpServerIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpServerIpStatus.setStatus("current")
_SmtpDestEMailTable_Object = MibTable
smtpDestEMailTable = _SmtpDestEMailTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 5)
)
if mibBuilder.loadTexts:
    smtpDestEMailTable.setStatus("current")
_SmtpDestEMailEntry_Object = MibTableRow
smtpDestEMailEntry = _SmtpDestEMailEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 5, 1)
)
smtpDestEMailEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "smtpDestEMail"),
)
if mibBuilder.loadTexts:
    smtpDestEMailEntry.setStatus("current")


class _SmtpDestEMail_Type(DisplayString):
    """Custom type smtpDestEMail based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 41),
    )


_SmtpDestEMail_Type.__name__ = "DisplayString"
_SmtpDestEMail_Object = MibTableColumn
smtpDestEMail = _SmtpDestEMail_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 5, 1, 1),
    _SmtpDestEMail_Type()
)
smtpDestEMail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smtpDestEMail.setStatus("current")
_SmtpDestEMailStatus_Type = ValidStatus
_SmtpDestEMailStatus_Object = MibTableColumn
smtpDestEMailStatus = _SmtpDestEMailStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 19, 7, 5, 1, 2),
    _SmtpDestEMailStatus_Type()
)
smtpDestEMailStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpDestEMailStatus.setStatus("current")
_LineMgt_ObjectIdentity = ObjectIdentity
lineMgt = _LineMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20)
)
_ConsoleMgt_ObjectIdentity = ObjectIdentity
consoleMgt = _ConsoleMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 1)
)


class _ConsoleDataBits_Type(Integer32):
    """Custom type consoleDataBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("databits7", 1),
          ("databits8", 2))
    )


_ConsoleDataBits_Type.__name__ = "Integer32"
_ConsoleDataBits_Object = MibScalar
consoleDataBits = _ConsoleDataBits_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 1, 1),
    _ConsoleDataBits_Type()
)
consoleDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleDataBits.setStatus("current")


class _ConsoleParity_Type(Integer32):
    """Custom type consoleParity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("partyNone", 1),
          ("partyEven", 2),
          ("partyOdd", 3))
    )


_ConsoleParity_Type.__name__ = "Integer32"
_ConsoleParity_Object = MibScalar
consoleParity = _ConsoleParity_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 1, 2),
    _ConsoleParity_Type()
)
consoleParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleParity.setStatus("current")


class _ConsoleStopBits_Type(Integer32):
    """Custom type consoleStopBits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stopbits1", 1),
          ("stopbits2", 2))
    )


_ConsoleStopBits_Type.__name__ = "Integer32"
_ConsoleStopBits_Object = MibScalar
consoleStopBits = _ConsoleStopBits_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 1, 4),
    _ConsoleStopBits_Type()
)
consoleStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleStopBits.setStatus("current")


class _ConsoleExecTimeout_Type(Integer32):
    """Custom type consoleExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConsoleExecTimeout_Type.__name__ = "Integer32"
_ConsoleExecTimeout_Object = MibScalar
consoleExecTimeout = _ConsoleExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 1, 5),
    _ConsoleExecTimeout_Type()
)
consoleExecTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleExecTimeout.setStatus("current")


class _ConsolePasswordThreshold_Type(Integer32):
    """Custom type consolePasswordThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_ConsolePasswordThreshold_Type.__name__ = "Integer32"
_ConsolePasswordThreshold_Object = MibScalar
consolePasswordThreshold = _ConsolePasswordThreshold_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 1, 6),
    _ConsolePasswordThreshold_Type()
)
consolePasswordThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consolePasswordThreshold.setStatus("current")


class _ConsoleSilentTime_Type(Integer32):
    """Custom type consoleSilentTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ConsoleSilentTime_Type.__name__ = "Integer32"
_ConsoleSilentTime_Object = MibScalar
consoleSilentTime = _ConsoleSilentTime_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 1, 7),
    _ConsoleSilentTime_Type()
)
consoleSilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleSilentTime.setStatus("current")
_ConsoleAdminBaudRate_Type = Integer32
_ConsoleAdminBaudRate_Object = MibScalar
consoleAdminBaudRate = _ConsoleAdminBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 1, 8),
    _ConsoleAdminBaudRate_Type()
)
consoleAdminBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleAdminBaudRate.setStatus("current")
_ConsoleOperBaudRate_Type = Integer32
_ConsoleOperBaudRate_Object = MibScalar
consoleOperBaudRate = _ConsoleOperBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 1, 9),
    _ConsoleOperBaudRate_Type()
)
consoleOperBaudRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    consoleOperBaudRate.setStatus("current")


class _ConsoleLoginResponseTimeout_Type(Integer32):
    """Custom type consoleLoginResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 300),
    )


_ConsoleLoginResponseTimeout_Type.__name__ = "Integer32"
_ConsoleLoginResponseTimeout_Object = MibScalar
consoleLoginResponseTimeout = _ConsoleLoginResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 1, 10),
    _ConsoleLoginResponseTimeout_Type()
)
consoleLoginResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleLoginResponseTimeout.setStatus("current")
_TelnetMgt_ObjectIdentity = ObjectIdentity
telnetMgt = _TelnetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 2)
)


class _TelnetExecTimeout_Type(Integer32):
    """Custom type telnetExecTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetExecTimeout_Type.__name__ = "Integer32"
_TelnetExecTimeout_Object = MibScalar
telnetExecTimeout = _TelnetExecTimeout_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 2, 1),
    _TelnetExecTimeout_Type()
)
telnetExecTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetExecTimeout.setStatus("current")


class _TelnetPasswordThreshold_Type(Integer32):
    """Custom type telnetPasswordThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 120),
    )


_TelnetPasswordThreshold_Type.__name__ = "Integer32"
_TelnetPasswordThreshold_Object = MibScalar
telnetPasswordThreshold = _TelnetPasswordThreshold_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 2, 2),
    _TelnetPasswordThreshold_Type()
)
telnetPasswordThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPasswordThreshold.setStatus("current")


class _TelnetLoginResponseTimeout_Type(Integer32):
    """Custom type telnetLoginResponseTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_TelnetLoginResponseTimeout_Type.__name__ = "Integer32"
_TelnetLoginResponseTimeout_Object = MibScalar
telnetLoginResponseTimeout = _TelnetLoginResponseTimeout_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 2, 3),
    _TelnetLoginResponseTimeout_Type()
)
telnetLoginResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetLoginResponseTimeout.setStatus("current")


class _TelnetStatus_Type(EnabledStatus):
    """Custom type telnetStatus based on EnabledStatus"""
    defaultValue = 1


_TelnetStatus_Type.__name__ = "EnabledStatus"
_TelnetStatus_Object = MibScalar
telnetStatus = _TelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 2, 4),
    _TelnetStatus_Type()
)
telnetStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetStatus.setStatus("current")


class _TelnetPortNumber_Type(Integer32):
    """Custom type telnetPortNumber based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TelnetPortNumber_Type.__name__ = "Integer32"
_TelnetPortNumber_Object = MibScalar
telnetPortNumber = _TelnetPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 20, 2, 5),
    _TelnetPortNumber_Type()
)
telnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortNumber.setStatus("current")
_SysTimeMgt_ObjectIdentity = ObjectIdentity
sysTimeMgt = _SysTimeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23)
)
_SntpMgt_ObjectIdentity = ObjectIdentity
sntpMgt = _SntpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 1)
)
_SntpStatus_Type = EnabledStatus
_SntpStatus_Object = MibScalar
sntpStatus = _SntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 1, 1),
    _SntpStatus_Type()
)
sntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpStatus.setStatus("current")


class _SntpServiceMode_Type(Integer32):
    """Custom type sntpServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_SntpServiceMode_Type.__name__ = "Integer32"
_SntpServiceMode_Object = MibScalar
sntpServiceMode = _SntpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 1, 2),
    _SntpServiceMode_Type()
)
sntpServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServiceMode.setStatus("current")


class _SntpPollInterval_Type(Integer32):
    """Custom type sntpPollInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 16384),
    )


_SntpPollInterval_Type.__name__ = "Integer32"
_SntpPollInterval_Object = MibScalar
sntpPollInterval = _SntpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 1, 3),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 1, 4)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 1, 4, 1)
)
sntpServerEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "sntpServerIndex"),
)
if mibBuilder.loadTexts:
    sntpServerEntry.setStatus("current")


class _SntpServerIndex_Type(Integer32):
    """Custom type sntpServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_SntpServerIndex_Type.__name__ = "Integer32"
_SntpServerIndex_Object = MibTableColumn
sntpServerIndex = _SntpServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 1, 4, 1, 1),
    _SntpServerIndex_Type()
)
sntpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sntpServerIndex.setStatus("current")
_SntpServerIpAddress_Type = IpAddress
_SntpServerIpAddress_Object = MibTableColumn
sntpServerIpAddress = _SntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 1, 4, 1, 2),
    _SntpServerIpAddress_Type()
)
sntpServerIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpServerIpAddress.setStatus("current")


class _SysCurrentTime_Type(DisplayString):
    """Custom type sysCurrentTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_SysCurrentTime_Type.__name__ = "DisplayString"
_SysCurrentTime_Object = MibScalar
sysCurrentTime = _SysCurrentTime_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 2),
    _SysCurrentTime_Type()
)
sysCurrentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysCurrentTime.setStatus("current")


class _SysTimeZone_Type(DisplayString):
    """Custom type sysTimeZone based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_SysTimeZone_Type.__name__ = "DisplayString"
_SysTimeZone_Object = MibScalar
sysTimeZone = _SysTimeZone_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 3),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("current")


class _SysTimeZoneName_Type(DisplayString):
    """Custom type sysTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysTimeZoneName_Type.__name__ = "DisplayString"
_SysTimeZoneName_Object = MibScalar
sysTimeZoneName = _SysTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 23, 4),
    _SysTimeZoneName_Type()
)
sysTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZoneName.setStatus("current")
_FileMgt_ObjectIdentity = ObjectIdentity
fileMgt = _FileMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24)
)
_FileCopyMgt_ObjectIdentity = ObjectIdentity
fileCopyMgt = _FileCopyMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 1)
)


class _FileCopySrcOperType_Type(Integer32):
    """Custom type fileCopySrcOperType based on Integer32"""
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
        *(("file", 1),
          ("runningCfg", 2),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5),
          ("http", 6))
    )


_FileCopySrcOperType_Type.__name__ = "Integer32"
_FileCopySrcOperType_Object = MibScalar
fileCopySrcOperType = _FileCopySrcOperType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 1, 1),
    _FileCopySrcOperType_Type()
)
fileCopySrcOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopySrcOperType.setStatus("current")


class _FileCopySrcFileName_Type(DisplayString):
    """Custom type fileCopySrcFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FileCopySrcFileName_Type.__name__ = "DisplayString"
_FileCopySrcFileName_Object = MibScalar
fileCopySrcFileName = _FileCopySrcFileName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 1, 2),
    _FileCopySrcFileName_Type()
)
fileCopySrcFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopySrcFileName.setStatus("current")


class _FileCopyDestOperType_Type(Integer32):
    """Custom type fileCopyDestOperType based on Integer32"""
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
        *(("file", 1),
          ("runningCfg", 2),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5),
          ("http", 6))
    )


_FileCopyDestOperType_Type.__name__ = "Integer32"
_FileCopyDestOperType_Object = MibScalar
fileCopyDestOperType = _FileCopyDestOperType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 1, 3),
    _FileCopyDestOperType_Type()
)
fileCopyDestOperType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyDestOperType.setStatus("current")


class _FileCopyDestFileName_Type(DisplayString):
    """Custom type fileCopyDestFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FileCopyDestFileName_Type.__name__ = "DisplayString"
_FileCopyDestFileName_Object = MibScalar
fileCopyDestFileName = _FileCopyDestFileName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 1, 4),
    _FileCopyDestFileName_Type()
)
fileCopyDestFileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyDestFileName.setStatus("current")


class _FileCopyFileType_Type(Integer32):
    """Custom type fileCopyFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("opcode", 1),
          ("config", 2),
          ("bootRom", 3))
    )


_FileCopyFileType_Type.__name__ = "Integer32"
_FileCopyFileType_Object = MibScalar
fileCopyFileType = _FileCopyFileType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 1, 5),
    _FileCopyFileType_Type()
)
fileCopyFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyFileType.setStatus("current")
_FileCopyTftpServer_Type = IpAddress
_FileCopyTftpServer_Object = MibScalar
fileCopyTftpServer = _FileCopyTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 1, 6),
    _FileCopyTftpServer_Type()
)
fileCopyTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyTftpServer.setStatus("current")
_FileCopyUnitId_Type = Integer32
_FileCopyUnitId_Object = MibScalar
fileCopyUnitId = _FileCopyUnitId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 1, 7),
    _FileCopyUnitId_Type()
)
fileCopyUnitId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyUnitId.setStatus("current")


class _FileCopyAction_Type(Integer32):
    """Custom type fileCopyAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notCopying", 1),
          ("copy", 2))
    )


_FileCopyAction_Type.__name__ = "Integer32"
_FileCopyAction_Object = MibScalar
fileCopyAction = _FileCopyAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 1, 8),
    _FileCopyAction_Type()
)
fileCopyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyAction.setStatus("current")
_FileCopyStatus_Type = FileCopyStatus
_FileCopyStatus_Object = MibScalar
fileCopyStatus = _FileCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 1, 9),
    _FileCopyStatus_Type()
)
fileCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyStatus.setStatus("current")
_FileInfoMgt_ObjectIdentity = ObjectIdentity
fileInfoMgt = _FileInfoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 2)
)
_FileInfoTable_Object = MibTable
fileInfoTable = _FileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    fileInfoTable.setStatus("current")
_FileInfoEntry_Object = MibTableRow
fileInfoEntry = _FileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 2, 1, 1)
)
fileInfoEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "fileInfoUnitID"),
    (1, "SMC6152L2-MIB", "fileInfoFileName"),
)
if mibBuilder.loadTexts:
    fileInfoEntry.setStatus("current")
_FileInfoUnitID_Type = Integer32
_FileInfoUnitID_Object = MibTableColumn
fileInfoUnitID = _FileInfoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 2, 1, 1, 1),
    _FileInfoUnitID_Type()
)
fileInfoUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileInfoUnitID.setStatus("current")


class _FileInfoFileName_Type(DisplayString):
    """Custom type fileInfoFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FileInfoFileName_Type.__name__ = "DisplayString"
_FileInfoFileName_Object = MibTableColumn
fileInfoFileName = _FileInfoFileName_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 2, 1, 1, 2),
    _FileInfoFileName_Type()
)
fileInfoFileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileInfoFileName.setStatus("current")


class _FileInfoFileType_Type(Integer32):
    """Custom type fileInfoFileType based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("diag", 1),
          ("runtime", 2),
          ("syslog", 3),
          ("cmdlog", 4),
          ("config", 5),
          ("postlog", 6),
          ("private", 7),
          ("certificate", 8),
          ("webarchive", 9))
    )


_FileInfoFileType_Type.__name__ = "Integer32"
_FileInfoFileType_Object = MibTableColumn
fileInfoFileType = _FileInfoFileType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 2, 1, 1, 3),
    _FileInfoFileType_Type()
)
fileInfoFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileType.setStatus("current")
_FileInfoIsStartUp_Type = TruthValue
_FileInfoIsStartUp_Object = MibTableColumn
fileInfoIsStartUp = _FileInfoIsStartUp_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 2, 1, 1, 4),
    _FileInfoIsStartUp_Type()
)
fileInfoIsStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoIsStartUp.setStatus("current")
_FileInfoFileSize_Type = Integer32
_FileInfoFileSize_Object = MibTableColumn
fileInfoFileSize = _FileInfoFileSize_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 2, 1, 1, 5),
    _FileInfoFileSize_Type()
)
fileInfoFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileSize.setStatus("current")
if mibBuilder.loadTexts:
    fileInfoFileSize.setUnits("bytes")


class _FileInfoCreationTime_Type(DisplayString):
    """Custom type fileInfoCreationTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20


_FileInfoCreationTime_Type.__name__ = "DisplayString"
_FileInfoCreationTime_Object = MibTableColumn
fileInfoCreationTime = _FileInfoCreationTime_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 2, 1, 1, 6),
    _FileInfoCreationTime_Type()
)
fileInfoCreationTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoCreationTime.setStatus("current")


class _FileInfoDelete_Type(Integer32):
    """Custom type fileInfoDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noDelete", 1),
          ("delete", 2))
    )


_FileInfoDelete_Type.__name__ = "Integer32"
_FileInfoDelete_Object = MibTableColumn
fileInfoDelete = _FileInfoDelete_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 2, 1, 1, 7),
    _FileInfoDelete_Type()
)
fileInfoDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoDelete.setStatus("current")
_FileAutoDownloadResultTable_Object = MibTable
fileAutoDownloadResultTable = _FileAutoDownloadResultTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 3)
)
if mibBuilder.loadTexts:
    fileAutoDownloadResultTable.setStatus("current")
_FileAutoDownloadResultEntry_Object = MibTableRow
fileAutoDownloadResultEntry = _FileAutoDownloadResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 3, 1)
)
fileAutoDownloadResultEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "fileAutoDownloadResultUnitID"),
)
if mibBuilder.loadTexts:
    fileAutoDownloadResultEntry.setStatus("current")
_FileAutoDownloadResultUnitID_Type = Integer32
_FileAutoDownloadResultUnitID_Object = MibTableColumn
fileAutoDownloadResultUnitID = _FileAutoDownloadResultUnitID_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 3, 1, 1),
    _FileAutoDownloadResultUnitID_Type()
)
fileAutoDownloadResultUnitID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fileAutoDownloadResultUnitID.setStatus("current")


class _FileAutoDownloadResultAction_Type(Integer32):
    """Custom type fileAutoDownloadResultAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notCopying", 1),
          ("copying", 2))
    )


_FileAutoDownloadResultAction_Type.__name__ = "Integer32"
_FileAutoDownloadResultAction_Object = MibTableColumn
fileAutoDownloadResultAction = _FileAutoDownloadResultAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 3, 1, 2),
    _FileAutoDownloadResultAction_Type()
)
fileAutoDownloadResultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAutoDownloadResultAction.setStatus("current")
_FileAutoDownloadResultStatus_Type = FileCopyStatus
_FileAutoDownloadResultStatus_Object = MibTableColumn
fileAutoDownloadResultStatus = _FileAutoDownloadResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 24, 3, 1, 3),
    _FileAutoDownloadResultStatus_Type()
)
fileAutoDownloadResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAutoDownloadResultStatus.setStatus("current")
_MvrMgt_ObjectIdentity = ObjectIdentity
mvrMgt = _MvrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44)
)
_MvrStatus_Type = EnabledStatus
_MvrStatus_Object = MibScalar
mvrStatus = _MvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 1),
    _MvrStatus_Type()
)
mvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrStatus.setStatus("current")
_MvrVlanId_Type = Integer32
_MvrVlanId_Object = MibScalar
mvrVlanId = _MvrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 2),
    _MvrVlanId_Type()
)
mvrVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrVlanId.setStatus("current")
_MvrMaxGroups_Type = Integer32
_MvrMaxGroups_Object = MibScalar
mvrMaxGroups = _MvrMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 3),
    _MvrMaxGroups_Type()
)
mvrMaxGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrMaxGroups.setStatus("current")
_MvrCurrentGroups_Type = Integer32
_MvrCurrentGroups_Object = MibScalar
mvrCurrentGroups = _MvrCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 4),
    _MvrCurrentGroups_Type()
)
mvrCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrCurrentGroups.setStatus("current")
_MvrGroupsCtl_ObjectIdentity = ObjectIdentity
mvrGroupsCtl = _MvrGroupsCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 5)
)
_MvrGroupsCtlId_Type = IpAddress
_MvrGroupsCtlId_Object = MibScalar
mvrGroupsCtlId = _MvrGroupsCtlId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 5, 1),
    _MvrGroupsCtlId_Type()
)
mvrGroupsCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupsCtlId.setStatus("current")
_MvrGroupsCtlCount_Type = Integer32
_MvrGroupsCtlCount_Object = MibScalar
mvrGroupsCtlCount = _MvrGroupsCtlCount_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 5, 2),
    _MvrGroupsCtlCount_Type()
)
mvrGroupsCtlCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupsCtlCount.setStatus("current")


class _MvrGroupsCtlAction_Type(Integer32):
    """Custom type mvrGroupsCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAction", 0),
          ("create", 1),
          ("destory", 2))
    )


_MvrGroupsCtlAction_Type.__name__ = "Integer32"
_MvrGroupsCtlAction_Object = MibScalar
mvrGroupsCtlAction = _MvrGroupsCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 5, 3),
    _MvrGroupsCtlAction_Type()
)
mvrGroupsCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupsCtlAction.setStatus("current")
_MvrGroupTable_Object = MibTable
mvrGroupTable = _MvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 6)
)
if mibBuilder.loadTexts:
    mvrGroupTable.setStatus("current")
_MvrGroupEntry_Object = MibTableRow
mvrGroupEntry = _MvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 6, 1)
)
mvrGroupEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "mvrGroupId"),
)
if mibBuilder.loadTexts:
    mvrGroupEntry.setStatus("current")
_MvrGroupId_Type = IpAddress
_MvrGroupId_Object = MibTableColumn
mvrGroupId = _MvrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 6, 1, 1),
    _MvrGroupId_Type()
)
mvrGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrGroupId.setStatus("current")


class _MvrGroutActive_Type(Integer32):
    """Custom type mvrGroutActive based on Integer32"""
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


_MvrGroutActive_Type.__name__ = "Integer32"
_MvrGroutActive_Object = MibTableColumn
mvrGroutActive = _MvrGroutActive_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 6, 1, 2),
    _MvrGroutActive_Type()
)
mvrGroutActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroutActive.setStatus("current")


class _MvrGroupStatus_Type(Integer32):
    """Custom type mvrGroupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_MvrGroupStatus_Type.__name__ = "Integer32"
_MvrGroupStatus_Object = MibTableColumn
mvrGroupStatus = _MvrGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 6, 1, 3),
    _MvrGroupStatus_Type()
)
mvrGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStatus.setStatus("current")
_MvrGroupStaticTable_Object = MibTable
mvrGroupStaticTable = _MvrGroupStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 7)
)
if mibBuilder.loadTexts:
    mvrGroupStaticTable.setStatus("current")
_MvrGroupStaticEntry_Object = MibTableRow
mvrGroupStaticEntry = _MvrGroupStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 7, 1)
)
mvrGroupStaticEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "mvrGroupStaticAddress"),
)
if mibBuilder.loadTexts:
    mvrGroupStaticEntry.setStatus("current")
_MvrGroupStaticAddress_Type = IpAddress
_MvrGroupStaticAddress_Object = MibTableColumn
mvrGroupStaticAddress = _MvrGroupStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 7, 1, 1),
    _MvrGroupStaticAddress_Type()
)
mvrGroupStaticAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrGroupStaticAddress.setStatus("current")
_MvrGroupStaticPorts_Type = PortList
_MvrGroupStaticPorts_Object = MibTableColumn
mvrGroupStaticPorts = _MvrGroupStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 7, 1, 2),
    _MvrGroupStaticPorts_Type()
)
mvrGroupStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStaticPorts.setStatus("current")


class _MvrGroupStaticStatus_Type(Integer32):
    """Custom type mvrGroupStaticStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2))
    )


_MvrGroupStaticStatus_Type.__name__ = "Integer32"
_MvrGroupStaticStatus_Object = MibTableColumn
mvrGroupStaticStatus = _MvrGroupStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 7, 1, 3),
    _MvrGroupStaticStatus_Type()
)
mvrGroupStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStaticStatus.setStatus("current")
_MvrGroupCurrentTable_Object = MibTable
mvrGroupCurrentTable = _MvrGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 8)
)
if mibBuilder.loadTexts:
    mvrGroupCurrentTable.setStatus("current")
_MvrGroupCurrentEntry_Object = MibTableRow
mvrGroupCurrentEntry = _MvrGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 8, 1)
)
mvrGroupCurrentEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "mvrGroupCurrentAddress"),
)
if mibBuilder.loadTexts:
    mvrGroupCurrentEntry.setStatus("current")
_MvrGroupCurrentAddress_Type = IpAddress
_MvrGroupCurrentAddress_Object = MibTableColumn
mvrGroupCurrentAddress = _MvrGroupCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 8, 1, 1),
    _MvrGroupCurrentAddress_Type()
)
mvrGroupCurrentAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrGroupCurrentAddress.setStatus("current")
_MvrGroupCurrentPorts_Type = PortList
_MvrGroupCurrentPorts_Object = MibTableColumn
mvrGroupCurrentPorts = _MvrGroupCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 8, 1, 2),
    _MvrGroupCurrentPorts_Type()
)
mvrGroupCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroupCurrentPorts.setStatus("current")
_MvrPortTable_Object = MibTable
mvrPortTable = _MvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 9)
)
if mibBuilder.loadTexts:
    mvrPortTable.setStatus("current")
_MvrPortEntry_Object = MibTableRow
mvrPortEntry = _MvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 9, 1)
)
mvrPortEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "mvrIfIndex"),
)
if mibBuilder.loadTexts:
    mvrPortEntry.setStatus("current")
_MvrIfIndex_Type = InterfaceIndex
_MvrIfIndex_Object = MibTableColumn
mvrIfIndex = _MvrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 9, 1, 1),
    _MvrIfIndex_Type()
)
mvrIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrIfIndex.setStatus("current")


class _MvrPortType_Type(Integer32):
    """Custom type mvrPortType based on Integer32"""
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
          ("source", 1),
          ("receiver", 2))
    )


_MvrPortType_Type.__name__ = "Integer32"
_MvrPortType_Object = MibTableColumn
mvrPortType = _MvrPortType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 9, 1, 2),
    _MvrPortType_Type()
)
mvrPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortType.setStatus("current")
_MvrPortImmediateLeave_Type = EnabledStatus
_MvrPortImmediateLeave_Object = MibTableColumn
mvrPortImmediateLeave = _MvrPortImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 9, 1, 3),
    _MvrPortImmediateLeave_Type()
)
mvrPortImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortImmediateLeave.setStatus("current")


class _MvrPortActive_Type(Integer32):
    """Custom type mvrPortActive based on Integer32"""
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


_MvrPortActive_Type.__name__ = "Integer32"
_MvrPortActive_Object = MibTableColumn
mvrPortActive = _MvrPortActive_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 9, 1, 4),
    _MvrPortActive_Type()
)
mvrPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortActive.setStatus("current")
_MvrRunningStatus_Type = TruthValue
_MvrRunningStatus_Object = MibScalar
mvrRunningStatus = _MvrRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 44, 10),
    _MvrRunningStatus_Type()
)
mvrRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrRunningStatus.setStatus("current")
_DhcpSnoopMgt_ObjectIdentity = ObjectIdentity
dhcpSnoopMgt = _DhcpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46)
)
_DhcpSnoopGlobal_ObjectIdentity = ObjectIdentity
dhcpSnoopGlobal = _DhcpSnoopGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 1)
)
_DhcpSnoopEnable_Type = EnabledStatus
_DhcpSnoopEnable_Object = MibScalar
dhcpSnoopEnable = _DhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 1, 1),
    _DhcpSnoopEnable_Type()
)
dhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopEnable.setStatus("current")
_DhcpSnoopVerifyMacAddressEnable_Type = EnabledStatus
_DhcpSnoopVerifyMacAddressEnable_Object = MibScalar
dhcpSnoopVerifyMacAddressEnable = _DhcpSnoopVerifyMacAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 1, 2),
    _DhcpSnoopVerifyMacAddressEnable_Type()
)
dhcpSnoopVerifyMacAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopVerifyMacAddressEnable.setStatus("current")
_DhcpSnoopInformationOptionEnable_Type = EnabledStatus
_DhcpSnoopInformationOptionEnable_Object = MibScalar
dhcpSnoopInformationOptionEnable = _DhcpSnoopInformationOptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 1, 3),
    _DhcpSnoopInformationOptionEnable_Type()
)
dhcpSnoopInformationOptionEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopInformationOptionEnable.setStatus("current")


class _DhcpSnoopInformationOptionPolicy_Type(Integer32):
    """Custom type dhcpSnoopInformationOptionPolicy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("keep", 2),
          ("replace", 3))
    )


_DhcpSnoopInformationOptionPolicy_Type.__name__ = "Integer32"
_DhcpSnoopInformationOptionPolicy_Object = MibScalar
dhcpSnoopInformationOptionPolicy = _DhcpSnoopInformationOptionPolicy_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 1, 4),
    _DhcpSnoopInformationOptionPolicy_Type()
)
dhcpSnoopInformationOptionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopInformationOptionPolicy.setStatus("current")
_DhcpSnoopVlan_ObjectIdentity = ObjectIdentity
dhcpSnoopVlan = _DhcpSnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 2)
)
_DhcpSnoopVlanConfigTable_Object = MibTable
dhcpSnoopVlanConfigTable = _DhcpSnoopVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopVlanConfigTable.setStatus("current")
_DhcpSnoopVlanConfigEntry_Object = MibTableRow
dhcpSnoopVlanConfigEntry = _DhcpSnoopVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 2, 1, 1)
)
dhcpSnoopVlanConfigEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "dhcpSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopVlanConfigEntry.setStatus("current")
_DhcpSnoopVlanIndex_Type = VlanIndex
_DhcpSnoopVlanIndex_Object = MibTableColumn
dhcpSnoopVlanIndex = _DhcpSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 2, 1, 1, 1),
    _DhcpSnoopVlanIndex_Type()
)
dhcpSnoopVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopVlanIndex.setStatus("current")
_DhcpSnoopVlanEnable_Type = EnabledStatus
_DhcpSnoopVlanEnable_Object = MibTableColumn
dhcpSnoopVlanEnable = _DhcpSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 2, 1, 1, 2),
    _DhcpSnoopVlanEnable_Type()
)
dhcpSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopVlanEnable.setStatus("current")
_DhcpSnoopInterface_ObjectIdentity = ObjectIdentity
dhcpSnoopInterface = _DhcpSnoopInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 3)
)
_DhcpSnoopPortConfigTable_Object = MibTable
dhcpSnoopPortConfigTable = _DhcpSnoopPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortConfigTable.setStatus("current")
_DhcpSnoopPortConfigEntry_Object = MibTableRow
dhcpSnoopPortConfigEntry = _DhcpSnoopPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 3, 1, 1)
)
dhcpSnoopPortConfigEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "dhcpSnoopPortIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopPortConfigEntry.setStatus("current")
_DhcpSnoopPortIfIndex_Type = InterfaceIndex
_DhcpSnoopPortIfIndex_Object = MibTableColumn
dhcpSnoopPortIfIndex = _DhcpSnoopPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 3, 1, 1, 1),
    _DhcpSnoopPortIfIndex_Type()
)
dhcpSnoopPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopPortIfIndex.setStatus("current")
_DhcpSnoopPortTrustEnable_Type = EnabledStatus
_DhcpSnoopPortTrustEnable_Object = MibTableColumn
dhcpSnoopPortTrustEnable = _DhcpSnoopPortTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 3, 1, 1, 2),
    _DhcpSnoopPortTrustEnable_Type()
)
dhcpSnoopPortTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopPortTrustEnable.setStatus("current")
_DhcpSnoopBindings_ObjectIdentity = ObjectIdentity
dhcpSnoopBindings = _DhcpSnoopBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 4)
)
_DhcpSnoopBindingsTable_Object = MibTable
dhcpSnoopBindingsTable = _DhcpSnoopBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 4, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopBindingsTable.setStatus("current")
_DhcpSnoopBindingsEntry_Object = MibTableRow
dhcpSnoopBindingsEntry = _DhcpSnoopBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 4, 1, 1)
)
dhcpSnoopBindingsEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "dhcpSnoopBindingsVlanIndex"),
    (0, "SMC6152L2-MIB", "dhcpSnoopBindingsMacAddress"),
)
if mibBuilder.loadTexts:
    dhcpSnoopBindingsEntry.setStatus("current")
_DhcpSnoopBindingsVlanIndex_Type = VlanIndex
_DhcpSnoopBindingsVlanIndex_Object = MibTableColumn
dhcpSnoopBindingsVlanIndex = _DhcpSnoopBindingsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 4, 1, 1, 1),
    _DhcpSnoopBindingsVlanIndex_Type()
)
dhcpSnoopBindingsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsVlanIndex.setStatus("current")
_DhcpSnoopBindingsMacAddress_Type = MacAddress
_DhcpSnoopBindingsMacAddress_Object = MibTableColumn
dhcpSnoopBindingsMacAddress = _DhcpSnoopBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 4, 1, 1, 2),
    _DhcpSnoopBindingsMacAddress_Type()
)
dhcpSnoopBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsMacAddress.setStatus("current")
_DhcpSnoopBindingsAddrType_Type = InetAddressType
_DhcpSnoopBindingsAddrType_Object = MibTableColumn
dhcpSnoopBindingsAddrType = _DhcpSnoopBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 4, 1, 1, 3),
    _DhcpSnoopBindingsAddrType_Type()
)
dhcpSnoopBindingsAddrType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsAddrType.setStatus("current")


class _DhcpSnoopBindingsEntryType_Type(Integer32):
    """Custom type dhcpSnoopBindingsEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_DhcpSnoopBindingsEntryType_Type.__name__ = "Integer32"
_DhcpSnoopBindingsEntryType_Object = MibTableColumn
dhcpSnoopBindingsEntryType = _DhcpSnoopBindingsEntryType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 4, 1, 1, 4),
    _DhcpSnoopBindingsEntryType_Type()
)
dhcpSnoopBindingsEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsEntryType.setStatus("current")
_DhcpSnoopBindingsIpAddress_Type = IpAddress
_DhcpSnoopBindingsIpAddress_Object = MibTableColumn
dhcpSnoopBindingsIpAddress = _DhcpSnoopBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 4, 1, 1, 5),
    _DhcpSnoopBindingsIpAddress_Type()
)
dhcpSnoopBindingsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsIpAddress.setStatus("current")
_DhcpSnoopBindingsPortIfIndex_Type = InterfaceIndex
_DhcpSnoopBindingsPortIfIndex_Object = MibTableColumn
dhcpSnoopBindingsPortIfIndex = _DhcpSnoopBindingsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 4, 1, 1, 6),
    _DhcpSnoopBindingsPortIfIndex_Type()
)
dhcpSnoopBindingsPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsPortIfIndex.setStatus("current")
_DhcpSnoopBindingsLeaseTime_Type = Unsigned32
_DhcpSnoopBindingsLeaseTime_Object = MibTableColumn
dhcpSnoopBindingsLeaseTime = _DhcpSnoopBindingsLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 4, 1, 1, 7),
    _DhcpSnoopBindingsLeaseTime_Type()
)
dhcpSnoopBindingsLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsLeaseTime.setStatus("current")
_DhcpSnoopStatistics_ObjectIdentity = ObjectIdentity
dhcpSnoopStatistics = _DhcpSnoopStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 5)
)
_DhcpSnoopTotalForwardedPkts_Type = Counter32
_DhcpSnoopTotalForwardedPkts_Object = MibScalar
dhcpSnoopTotalForwardedPkts = _DhcpSnoopTotalForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 5, 1),
    _DhcpSnoopTotalForwardedPkts_Type()
)
dhcpSnoopTotalForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopTotalForwardedPkts.setStatus("current")
_DhcpSnoopUntrustedPortDroppedPkts_Type = Counter32
_DhcpSnoopUntrustedPortDroppedPkts_Object = MibScalar
dhcpSnoopUntrustedPortDroppedPkts = _DhcpSnoopUntrustedPortDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 46, 5, 3),
    _DhcpSnoopUntrustedPortDroppedPkts_Type()
)
dhcpSnoopUntrustedPortDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopUntrustedPortDroppedPkts.setStatus("current")
_ClusterMgt_ObjectIdentity = ObjectIdentity
clusterMgt = _ClusterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47)
)
_ClusterEnable_Type = EnabledStatus
_ClusterEnable_Object = MibScalar
clusterEnable = _ClusterEnable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 1),
    _ClusterEnable_Type()
)
clusterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterEnable.setStatus("current")
_ClusterCommanderEnable_Type = EnabledStatus
_ClusterCommanderEnable_Object = MibScalar
clusterCommanderEnable = _ClusterCommanderEnable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 2),
    _ClusterCommanderEnable_Type()
)
clusterCommanderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterCommanderEnable.setStatus("current")
_ClusterIpPool_Type = IpAddress
_ClusterIpPool_Object = MibScalar
clusterIpPool = _ClusterIpPool_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 4),
    _ClusterIpPool_Type()
)
clusterIpPool.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterIpPool.setStatus("current")


class _ClusterClearCandidateTable_Type(Integer32):
    """Custom type clusterClearCandidateTable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noClear", 1),
          ("clear", 2))
    )


_ClusterClearCandidateTable_Type.__name__ = "Integer32"
_ClusterClearCandidateTable_Object = MibScalar
clusterClearCandidateTable = _ClusterClearCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 5),
    _ClusterClearCandidateTable_Type()
)
clusterClearCandidateTable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterClearCandidateTable.setStatus("current")


class _ClusterRole_Type(Integer32):
    """Custom type clusterRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("commander", 1),
          ("candidate", 2),
          ("activeMember", 3),
          ("disabled", 5))
    )


_ClusterRole_Type.__name__ = "Integer32"
_ClusterRole_Object = MibScalar
clusterRole = _ClusterRole_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 6),
    _ClusterRole_Type()
)
clusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterRole.setStatus("current")
_ClusterMemberCount_Type = Counter32
_ClusterMemberCount_Object = MibScalar
clusterMemberCount = _ClusterMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 7),
    _ClusterMemberCount_Type()
)
clusterMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberCount.setStatus("current")
_ClusterCandidateCount_Type = Counter32
_ClusterCandidateCount_Object = MibScalar
clusterCandidateCount = _ClusterCandidateCount_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 8),
    _ClusterCandidateCount_Type()
)
clusterCandidateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateCount.setStatus("current")
_ClusterCandidateTable_Object = MibTable
clusterCandidateTable = _ClusterCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 9)
)
if mibBuilder.loadTexts:
    clusterCandidateTable.setStatus("current")
_ClusterCandidateEntry_Object = MibTableRow
clusterCandidateEntry = _ClusterCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 9, 1)
)
clusterCandidateEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "clusterCandidateMacAddr"),
)
if mibBuilder.loadTexts:
    clusterCandidateEntry.setStatus("current")
_ClusterCandidateMacAddr_Type = MacAddress
_ClusterCandidateMacAddr_Object = MibTableColumn
clusterCandidateMacAddr = _ClusterCandidateMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 9, 1, 1),
    _ClusterCandidateMacAddr_Type()
)
clusterCandidateMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterCandidateMacAddr.setStatus("current")


class _ClusterCandidateDesc_Type(DisplayString):
    """Custom type clusterCandidateDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_ClusterCandidateDesc_Type.__name__ = "DisplayString"
_ClusterCandidateDesc_Object = MibTableColumn
clusterCandidateDesc = _ClusterCandidateDesc_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 9, 1, 3),
    _ClusterCandidateDesc_Type()
)
clusterCandidateDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateDesc.setStatus("current")


class _ClusterCandidateRole_Type(Integer32):
    """Custom type clusterCandidateRole based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("candidate", 2),
          ("activeMember", 3),
          ("inactiveMember", 4))
    )


_ClusterCandidateRole_Type.__name__ = "Integer32"
_ClusterCandidateRole_Object = MibTableColumn
clusterCandidateRole = _ClusterCandidateRole_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 9, 1, 4),
    _ClusterCandidateRole_Type()
)
clusterCandidateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateRole.setStatus("current")
_ClusterMemberTable_Object = MibTable
clusterMemberTable = _ClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 10)
)
if mibBuilder.loadTexts:
    clusterMemberTable.setStatus("current")
_ClusterMemberEntry_Object = MibTableRow
clusterMemberEntry = _ClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 10, 1)
)
clusterMemberEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "clusterMemberId"),
)
if mibBuilder.loadTexts:
    clusterMemberEntry.setStatus("current")
_ClusterMemberId_Type = Unsigned32
_ClusterMemberId_Object = MibTableColumn
clusterMemberId = _ClusterMemberId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 10, 1, 1),
    _ClusterMemberId_Type()
)
clusterMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterMemberId.setStatus("current")
_ClusterMemberMacAddr_Type = MacAddress
_ClusterMemberMacAddr_Object = MibTableColumn
clusterMemberMacAddr = _ClusterMemberMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 10, 1, 2),
    _ClusterMemberMacAddr_Type()
)
clusterMemberMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberMacAddr.setStatus("current")


class _ClusterMemberDesc_Type(DisplayString):
    """Custom type clusterMemberDesc based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 42),
    )


_ClusterMemberDesc_Type.__name__ = "DisplayString"
_ClusterMemberDesc_Object = MibTableColumn
clusterMemberDesc = _ClusterMemberDesc_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 10, 1, 3),
    _ClusterMemberDesc_Type()
)
clusterMemberDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberDesc.setStatus("current")


class _ClusterMemberActive_Type(Integer32):
    """Custom type clusterMemberActive based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("activeMember", 3),
          ("inactiveMember", 4))
    )


_ClusterMemberActive_Type.__name__ = "Integer32"
_ClusterMemberActive_Object = MibTableColumn
clusterMemberActive = _ClusterMemberActive_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 10, 1, 4),
    _ClusterMemberActive_Type()
)
clusterMemberActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberActive.setStatus("current")
_ClusterMemberAddCtl_ObjectIdentity = ObjectIdentity
clusterMemberAddCtl = _ClusterMemberAddCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 11)
)
_ClusterMemberAddCtlMacAddr_Type = MacAddress
_ClusterMemberAddCtlMacAddr_Object = MibScalar
clusterMemberAddCtlMacAddr = _ClusterMemberAddCtlMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 11, 1),
    _ClusterMemberAddCtlMacAddr_Type()
)
clusterMemberAddCtlMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberAddCtlMacAddr.setStatus("current")
_ClusterMemberAddCtlId_Type = Unsigned32
_ClusterMemberAddCtlId_Object = MibScalar
clusterMemberAddCtlId = _ClusterMemberAddCtlId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 11, 2),
    _ClusterMemberAddCtlId_Type()
)
clusterMemberAddCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberAddCtlId.setStatus("current")


class _ClusterMemberAddCtlAction_Type(Integer32):
    """Custom type clusterMemberAddCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noAdd", 1),
          ("add", 2))
    )


_ClusterMemberAddCtlAction_Type.__name__ = "Integer32"
_ClusterMemberAddCtlAction_Object = MibScalar
clusterMemberAddCtlAction = _ClusterMemberAddCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 11, 5),
    _ClusterMemberAddCtlAction_Type()
)
clusterMemberAddCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberAddCtlAction.setStatus("current")
_ClusterMemberRemoveCtl_ObjectIdentity = ObjectIdentity
clusterMemberRemoveCtl = _ClusterMemberRemoveCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 12)
)
_ClusterMemberRemoveCtlId_Type = Unsigned32
_ClusterMemberRemoveCtlId_Object = MibScalar
clusterMemberRemoveCtlId = _ClusterMemberRemoveCtlId_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 12, 1),
    _ClusterMemberRemoveCtlId_Type()
)
clusterMemberRemoveCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberRemoveCtlId.setStatus("current")


class _ClusterMemberRemoveCtlAction_Type(Integer32):
    """Custom type clusterMemberRemoveCtlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRemove", 1),
          ("remove", 2))
    )


_ClusterMemberRemoveCtlAction_Type.__name__ = "Integer32"
_ClusterMemberRemoveCtlAction_Object = MibScalar
clusterMemberRemoveCtlAction = _ClusterMemberRemoveCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 47, 12, 2),
    _ClusterMemberRemoveCtlAction_Type()
)
clusterMemberRemoveCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberRemoveCtlAction.setStatus("current")
_IpSrcGuardMgt_ObjectIdentity = ObjectIdentity
ipSrcGuardMgt = _IpSrcGuardMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48)
)
_IpSrcGuardConfigTable_Object = MibTable
ipSrcGuardConfigTable = _IpSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 1)
)
if mibBuilder.loadTexts:
    ipSrcGuardConfigTable.setStatus("current")
_IpSrcGuardConfigEntry_Object = MibTableRow
ipSrcGuardConfigEntry = _IpSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 1, 1)
)
ipSrcGuardConfigEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "ipSrcGuardPortIfIndex"),
)
if mibBuilder.loadTexts:
    ipSrcGuardConfigEntry.setStatus("current")
_IpSrcGuardPortIfIndex_Type = InterfaceIndex
_IpSrcGuardPortIfIndex_Object = MibTableColumn
ipSrcGuardPortIfIndex = _IpSrcGuardPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 1, 1, 1),
    _IpSrcGuardPortIfIndex_Type()
)
ipSrcGuardPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardPortIfIndex.setStatus("current")


class _IpSrcGuardMode_Type(Integer32):
    """Custom type ipSrcGuardMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("diabled", 0),
          ("srcIp", 1),
          ("srcIpMac", 2))
    )


_IpSrcGuardMode_Type.__name__ = "Integer32"
_IpSrcGuardMode_Object = MibTableColumn
ipSrcGuardMode = _IpSrcGuardMode_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 1, 1, 2),
    _IpSrcGuardMode_Type()
)
ipSrcGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSrcGuardMode.setStatus("current")
_IpSrcGuardAddrTable_Object = MibTable
ipSrcGuardAddrTable = _IpSrcGuardAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 2)
)
if mibBuilder.loadTexts:
    ipSrcGuardAddrTable.setStatus("current")
_IpSrcGuardAddrEntry_Object = MibTableRow
ipSrcGuardAddrEntry = _IpSrcGuardAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 2, 1)
)
ipSrcGuardAddrEntry.setIndexNames(
    (0, "SMC6152L2-MIB", "ipSrcGuardBindingsVlanIndex"),
    (0, "SMC6152L2-MIB", "ipSrcGuardBindingsMacAddress"),
)
if mibBuilder.loadTexts:
    ipSrcGuardAddrEntry.setStatus("current")
_IpSrcGuardBindingsVlanIndex_Type = VlanIndex
_IpSrcGuardBindingsVlanIndex_Object = MibTableColumn
ipSrcGuardBindingsVlanIndex = _IpSrcGuardBindingsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 2, 1, 1),
    _IpSrcGuardBindingsVlanIndex_Type()
)
ipSrcGuardBindingsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsVlanIndex.setStatus("current")
_IpSrcGuardBindingsMacAddress_Type = MacAddress
_IpSrcGuardBindingsMacAddress_Object = MibTableColumn
ipSrcGuardBindingsMacAddress = _IpSrcGuardBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 2, 1, 2),
    _IpSrcGuardBindingsMacAddress_Type()
)
ipSrcGuardBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsMacAddress.setStatus("current")
_IpSrcGuardBindingsAddrType_Type = InetAddressType
_IpSrcGuardBindingsAddrType_Object = MibTableColumn
ipSrcGuardBindingsAddrType = _IpSrcGuardBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 2, 1, 3),
    _IpSrcGuardBindingsAddrType_Type()
)
ipSrcGuardBindingsAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsAddrType.setStatus("current")


class _IpSrcGuardBindingsEntryType_Type(Integer32):
    """Custom type ipSrcGuardBindingsEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 3))
    )


_IpSrcGuardBindingsEntryType_Type.__name__ = "Integer32"
_IpSrcGuardBindingsEntryType_Object = MibTableColumn
ipSrcGuardBindingsEntryType = _IpSrcGuardBindingsEntryType_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 2, 1, 4),
    _IpSrcGuardBindingsEntryType_Type()
)
ipSrcGuardBindingsEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsEntryType.setStatus("current")
_IpSrcGuardBindingsIpAddress_Type = IpAddress
_IpSrcGuardBindingsIpAddress_Object = MibTableColumn
ipSrcGuardBindingsIpAddress = _IpSrcGuardBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 2, 1, 5),
    _IpSrcGuardBindingsIpAddress_Type()
)
ipSrcGuardBindingsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsIpAddress.setStatus("current")
_IpSrcGuardBindingsPortIfIndex_Type = InterfaceIndex
_IpSrcGuardBindingsPortIfIndex_Object = MibTableColumn
ipSrcGuardBindingsPortIfIndex = _IpSrcGuardBindingsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 2, 1, 6),
    _IpSrcGuardBindingsPortIfIndex_Type()
)
ipSrcGuardBindingsPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsPortIfIndex.setStatus("current")
_IpSrcGuardBindingsLeaseTime_Type = Unsigned32
_IpSrcGuardBindingsLeaseTime_Object = MibTableColumn
ipSrcGuardBindingsLeaseTime = _IpSrcGuardBindingsLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 2, 1, 7),
    _IpSrcGuardBindingsLeaseTime_Type()
)
ipSrcGuardBindingsLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsLeaseTime.setStatus("current")
_IpSrcGuardBindingsStatus_Type = RowStatus
_IpSrcGuardBindingsStatus_Object = MibTableColumn
ipSrcGuardBindingsStatus = _IpSrcGuardBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 1, 48, 2, 1, 8),
    _IpSrcGuardBindingsStatus_Type()
)
ipSrcGuardBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsStatus.setStatus("current")
_Smc6152L2Notifications_ObjectIdentity = ObjectIdentity
smc6152L2Notifications = _Smc6152L2Notifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 2)
)
_Smc6152L2Traps_ObjectIdentity = ObjectIdentity
smc6152L2Traps = _Smc6152L2Traps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 2, 1)
)
_Smc6152L2TrapsPrefix_ObjectIdentity = ObjectIdentity
smc6152L2TrapsPrefix = _Smc6152L2TrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 2, 1, 0)
)
_Smc6152L2Conformance_ObjectIdentity = ObjectIdentity
smc6152L2Conformance = _Smc6152L2Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 3)
)
dot1dStpPortEntry.registerAugmentions(
    ("SMC6152L2-MIB",
     "staPortEntry")
)
staPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

swPowerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 2, 1, 0, 1)
)
swPowerStatusChangeTrap.setObjects(
      *(("SMC6152L2-MIB", "swIndivPowerUnitIndex"),
        ("SMC6152L2-MIB", "swIndivPowerIndex"),
        ("SMC6152L2-MIB", "swIndivPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerStatusChangeTrap.setStatus(
        "current"
    )

swPortSecurityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 202, 20, 66, 2, 1, 0, 36)
)
swPortSecurityTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    swPortSecurityTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SMC6152L2-MIB",
    **{"KeySegment": KeySegment,
       "ValidStatus": ValidStatus,
       "StaPathCostMode": StaPathCostMode,
       "FileCopyStatus": FileCopyStatus,
       "smc": smc,
       "smcSwitches": smcSwitches,
       "smc6152L2MIB": smc6152L2MIB,
       "smc6152L2MIBObjects": smc6152L2MIBObjects,
       "switchMgt": switchMgt,
       "switchManagementVlan": switchManagementVlan,
       "switchNumber": switchNumber,
       "switchInfoTable": switchInfoTable,
       "switchInfoEntry": switchInfoEntry,
       "swUnitIndex": swUnitIndex,
       "swHardwareVer": swHardwareVer,
       "swMicrocodeVer": swMicrocodeVer,
       "swLoaderVer": swLoaderVer,
       "swBootRomVer": swBootRomVer,
       "swOpCodeVer": swOpCodeVer,
       "swPortNumber": swPortNumber,
       "swPowerStatus": swPowerStatus,
       "swRoleInSystem": swRoleInSystem,
       "swSerialNumber": swSerialNumber,
       "swServiceTag": swServiceTag,
       "swModelNumber": swModelNumber,
       "swEpldVer": swEpldVer,
       "switchOperState": switchOperState,
       "switchProductId": switchProductId,
       "swProdName": swProdName,
       "swProdManufacturer": swProdManufacturer,
       "swProdDescription": swProdDescription,
       "swProdVersion": swProdVersion,
       "swProdUrl": swProdUrl,
       "swIdentifier": swIdentifier,
       "swChassisServiceTag": swChassisServiceTag,
       "switchIndivPowerTable": switchIndivPowerTable,
       "switchIndivPowerEntry": switchIndivPowerEntry,
       "swIndivPowerUnitIndex": swIndivPowerUnitIndex,
       "swIndivPowerIndex": swIndivPowerIndex,
       "swIndivPowerStatus": swIndivPowerStatus,
       "switchJumboFrameStatus": switchJumboFrameStatus,
       "amtrMgt": amtrMgt,
       "amtrMacAddrAgingStatus": amtrMacAddrAgingStatus,
       "portMgt": portMgt,
       "portTable": portTable,
       "portEntry": portEntry,
       "portIndex": portIndex,
       "portName": portName,
       "portType": portType,
       "portSpeedDpxCfg": portSpeedDpxCfg,
       "portFlowCtrlCfg": portFlowCtrlCfg,
       "portCapabilities": portCapabilities,
       "portAutonegotiation": portAutonegotiation,
       "portSpeedDpxStatus": portSpeedDpxStatus,
       "portFlowCtrlStatus": portFlowCtrlStatus,
       "portTrunkIndex": portTrunkIndex,
       "portComboForcedMode": portComboForcedMode,
       "trunkMgt": trunkMgt,
       "trunkMaxId": trunkMaxId,
       "trunkValidNumber": trunkValidNumber,
       "trunkTable": trunkTable,
       "trunkEntry": trunkEntry,
       "trunkIndex": trunkIndex,
       "trunkPorts": trunkPorts,
       "trunkCreation": trunkCreation,
       "trunkStatus": trunkStatus,
       "lacpMgt": lacpMgt,
       "lacpPortTable": lacpPortTable,
       "lacpPortEntry": lacpPortEntry,
       "lacpPortIndex": lacpPortIndex,
       "lacpPortStatus": lacpPortStatus,
       "staMgt": staMgt,
       "staSystemStatus": staSystemStatus,
       "staPortTable": staPortTable,
       "staPortEntry": staPortEntry,
       "staPortFastForward": staPortFastForward,
       "staPortProtocolMigration": staPortProtocolMigration,
       "staPortAdminEdgePort": staPortAdminEdgePort,
       "staPortOperEdgePort": staPortOperEdgePort,
       "staPortAdminPointToPoint": staPortAdminPointToPoint,
       "staPortOperPointToPoint": staPortOperPointToPoint,
       "staPortSystemStatus": staPortSystemStatus,
       "staPortLongAdminPathCost": staPortLongAdminPathCost,
       "staPortLongOperPathCost": staPortLongOperPathCost,
       "staProtocolType": staProtocolType,
       "staTxHoldCount": staTxHoldCount,
       "staPathCostMethod": staPathCostMethod,
       "restartMgt": restartMgt,
       "restartOpCodeFile": restartOpCodeFile,
       "restartConfigFile": restartConfigFile,
       "restartControl": restartControl,
       "mirrorMgt": mirrorMgt,
       "mirrorTable": mirrorTable,
       "mirrorEntry": mirrorEntry,
       "mirrorDestinationPort": mirrorDestinationPort,
       "mirrorSourcePort": mirrorSourcePort,
       "mirrorType": mirrorType,
       "mirrorStatus": mirrorStatus,
       "igmpSnoopMgt": igmpSnoopMgt,
       "igmpSnoopStatus": igmpSnoopStatus,
       "igmpSnoopQuerier": igmpSnoopQuerier,
       "igmpSnoopQueryCount": igmpSnoopQueryCount,
       "igmpSnoopQueryInterval": igmpSnoopQueryInterval,
       "igmpSnoopQueryMaxResponseTime": igmpSnoopQueryMaxResponseTime,
       "igmpSnoopRouterPortExpireTime": igmpSnoopRouterPortExpireTime,
       "igmpSnoopVersion": igmpSnoopVersion,
       "igmpSnoopRouterCurrentTable": igmpSnoopRouterCurrentTable,
       "igmpSnoopRouterCurrentEntry": igmpSnoopRouterCurrentEntry,
       "igmpSnoopRouterCurrentVlanIndex": igmpSnoopRouterCurrentVlanIndex,
       "igmpSnoopRouterCurrentPorts": igmpSnoopRouterCurrentPorts,
       "igmpSnoopRouterCurrentStatus": igmpSnoopRouterCurrentStatus,
       "igmpSnoopRouterStaticTable": igmpSnoopRouterStaticTable,
       "igmpSnoopRouterStaticEntry": igmpSnoopRouterStaticEntry,
       "igmpSnoopRouterStaticVlanIndex": igmpSnoopRouterStaticVlanIndex,
       "igmpSnoopRouterStaticPorts": igmpSnoopRouterStaticPorts,
       "igmpSnoopRouterStaticStatus": igmpSnoopRouterStaticStatus,
       "igmpSnoopMulticastCurrentTable": igmpSnoopMulticastCurrentTable,
       "igmpSnoopMulticastCurrentEntry": igmpSnoopMulticastCurrentEntry,
       "igmpSnoopMulticastCurrentVlanIndex": igmpSnoopMulticastCurrentVlanIndex,
       "igmpSnoopMulticastCurrentIpAddress": igmpSnoopMulticastCurrentIpAddress,
       "igmpSnoopMulticastCurrentPorts": igmpSnoopMulticastCurrentPorts,
       "igmpSnoopMulticastCurrentStatus": igmpSnoopMulticastCurrentStatus,
       "igmpSnoopMulticastStaticTable": igmpSnoopMulticastStaticTable,
       "igmpSnoopMulticastStaticEntry": igmpSnoopMulticastStaticEntry,
       "igmpSnoopMulticastStaticVlanIndex": igmpSnoopMulticastStaticVlanIndex,
       "igmpSnoopMulticastStaticIpAddress": igmpSnoopMulticastStaticIpAddress,
       "igmpSnoopMulticastStaticPorts": igmpSnoopMulticastStaticPorts,
       "igmpSnoopMulticastStaticStatus": igmpSnoopMulticastStaticStatus,
       "igmpSnoopCurrentVlanTable": igmpSnoopCurrentVlanTable,
       "igmpSnoopCurrentVlanEntry": igmpSnoopCurrentVlanEntry,
       "igmpSnoopCurrentVlanIndex": igmpSnoopCurrentVlanIndex,
       "igmpSnoopCurrentVlanImmediateLeave": igmpSnoopCurrentVlanImmediateLeave,
       "igmpSnoopLeaveProxy": igmpSnoopLeaveProxy,
       "igmpSnoopFilterStatus": igmpSnoopFilterStatus,
       "igmpSnoopProfileTable": igmpSnoopProfileTable,
       "igmpSnoopProfileEntry": igmpSnoopProfileEntry,
       "igmpSnoopProfileId": igmpSnoopProfileId,
       "igmpSnoopProfileAction": igmpSnoopProfileAction,
       "igmpSnoopProfileStatus": igmpSnoopProfileStatus,
       "igmpSnoopProfileCtl": igmpSnoopProfileCtl,
       "igmpSnoopProfileCtlId": igmpSnoopProfileCtlId,
       "igmpSnoopProfileCtlInetAddressType": igmpSnoopProfileCtlInetAddressType,
       "igmpSnoopProfileCtlStartInetAddress": igmpSnoopProfileCtlStartInetAddress,
       "igmpSnoopProfileCtlEndInetAddress": igmpSnoopProfileCtlEndInetAddress,
       "igmpSnoopProfileCtlAction": igmpSnoopProfileCtlAction,
       "igmpSnoopProfileRangeTable": igmpSnoopProfileRangeTable,
       "igmpSnoopProfileRangeEntry": igmpSnoopProfileRangeEntry,
       "igmpSnoopProfileRangeProfileId": igmpSnoopProfileRangeProfileId,
       "igmpSnoopProfileRangeInetAddressType": igmpSnoopProfileRangeInetAddressType,
       "igmpSnoopProfileRangeStartInetAddress": igmpSnoopProfileRangeStartInetAddress,
       "igmpSnoopProfileRangeEndInetAddress": igmpSnoopProfileRangeEndInetAddress,
       "igmpSnoopProfileRangeAction": igmpSnoopProfileRangeAction,
       "igmpSnoopFilterPortTable": igmpSnoopFilterPortTable,
       "igmpSnoopFilterPortEntry": igmpSnoopFilterPortEntry,
       "igmpSnoopFilterPortIndex": igmpSnoopFilterPortIndex,
       "igmpSnoopFilterPortProfileId": igmpSnoopFilterPortProfileId,
       "igmpSnoopThrottlePortTable": igmpSnoopThrottlePortTable,
       "igmpSnoopThrottlePortEntry": igmpSnoopThrottlePortEntry,
       "igmpSnoopThrottlePortIndex": igmpSnoopThrottlePortIndex,
       "igmpSnoopThrottlePortRunningStatus": igmpSnoopThrottlePortRunningStatus,
       "igmpSnoopThrottlePortAction": igmpSnoopThrottlePortAction,
       "igmpSnoopThrottlePortMaxGroups": igmpSnoopThrottlePortMaxGroups,
       "igmpSnoopThrottlePortCurrentGroups": igmpSnoopThrottlePortCurrentGroups,
       "ipMgt": ipMgt,
       "netConfigTable": netConfigTable,
       "netConfigEntry": netConfigEntry,
       "netConfigIfIndex": netConfigIfIndex,
       "netConfigIPAddress": netConfigIPAddress,
       "netConfigSubnetMask": netConfigSubnetMask,
       "netConfigPrimaryInterface": netConfigPrimaryInterface,
       "netConfigUnnumbered": netConfigUnnumbered,
       "netConfigStatus": netConfigStatus,
       "netDefaultGateway": netDefaultGateway,
       "ipHttpState": ipHttpState,
       "ipHttpPort": ipHttpPort,
       "ipDhcpRestart": ipDhcpRestart,
       "ipHttpsState": ipHttpsState,
       "ipHttpsPort": ipHttpsPort,
       "dhcpMgt": dhcpMgt,
       "dhcpClient": dhcpClient,
       "dhcpcOptions": dhcpcOptions,
       "dhcpcInterfaceTable": dhcpcInterfaceTable,
       "dhcpcInterfaceEntry": dhcpcInterfaceEntry,
       "dhcpcIfIndex": dhcpcIfIndex,
       "dhcpcIfClientIdMode": dhcpcIfClientIdMode,
       "dhcpcIfClientId": dhcpcIfClientId,
       "bcastStormMgt": bcastStormMgt,
       "bcastStormTable": bcastStormTable,
       "bcastStormEntry": bcastStormEntry,
       "bcastStormIfIndex": bcastStormIfIndex,
       "bcastStormStatus": bcastStormStatus,
       "bcastStormOctetRateInKilo": bcastStormOctetRateInKilo,
       "vlanMgt": vlanMgt,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIndex": vlanIndex,
       "vlanAddressMethod": vlanAddressMethod,
       "vlanPortTable": vlanPortTable,
       "vlanPortEntry": vlanPortEntry,
       "vlanPortIndex": vlanPortIndex,
       "vlanPortMode": vlanPortMode,
       "vlanPortPrivateVlanType": vlanPortPrivateVlanType,
       "protocolVlanTable": protocolVlanTable,
       "protocolVlanEntry": protocolVlanEntry,
       "protocolVlanGroupId": protocolVlanGroupId,
       "protocolVlanGroupVid": protocolVlanGroupVid,
       "priorityMgt": priorityMgt,
       "prioIpPrecDscpStatus": prioIpPrecDscpStatus,
       "prioIpDscpTable": prioIpDscpTable,
       "prioIpDscpEntry": prioIpDscpEntry,
       "prioIpDscpPort": prioIpDscpPort,
       "prioIpDscpValue": prioIpDscpValue,
       "prioIpDscpCos": prioIpDscpCos,
       "prioIpDscpRestoreDefault": prioIpDscpRestoreDefault,
       "prioCopy": prioCopy,
       "prioCopyIpDscp": prioCopyIpDscp,
       "prioWrrTable": prioWrrTable,
       "prioWrrEntry": prioWrrEntry,
       "prioWrrTrafficClass": prioWrrTrafficClass,
       "prioWrrWeight": prioWrrWeight,
       "prioQueueMode": prioQueueMode,
       "trapDestMgt": trapDestMgt,
       "trapDestTable": trapDestTable,
       "trapDestEntry": trapDestEntry,
       "trapDestAddress": trapDestAddress,
       "trapDestCommunity": trapDestCommunity,
       "trapDestStatus": trapDestStatus,
       "trapDestVersion": trapDestVersion,
       "trapDestUdpPort": trapDestUdpPort,
       "qosMgt": qosMgt,
       "rateLimitMgt": rateLimitMgt,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rlPortIndex": rlPortIndex,
       "rlPortInputStatus": rlPortInputStatus,
       "rlPortOutputStatus": rlPortOutputStatus,
       "rlPortInputLimitInKilo": rlPortInputLimitInKilo,
       "rlPortOutputLimitInKilo": rlPortOutputLimitInKilo,
       "diffServMgt": diffServMgt,
       "diffServPortTable": diffServPortTable,
       "diffServPortEntry": diffServPortEntry,
       "diffServPortIfIndex": diffServPortIfIndex,
       "diffServPortPolicyMapIndex": diffServPortPolicyMapIndex,
       "diffServPortIngressIpAclIndex": diffServPortIngressIpAclIndex,
       "diffServPortIngressMacAclIndex": diffServPortIngressMacAclIndex,
       "diffServPolicyMapTable": diffServPolicyMapTable,
       "diffServPolicyMapEntry": diffServPolicyMapEntry,
       "diffServPolicyMapIndex": diffServPolicyMapIndex,
       "diffServPolicyMapName": diffServPolicyMapName,
       "diffServPolicyMapDescription": diffServPolicyMapDescription,
       "diffServPolicyMapElementIndexList": diffServPolicyMapElementIndexList,
       "diffServPolicyMapStatus": diffServPolicyMapStatus,
       "diffServPolicyMapAttachCtl": diffServPolicyMapAttachCtl,
       "diffServPolicyMapAttachCtlIndex": diffServPolicyMapAttachCtlIndex,
       "diffServPolicyMapAttachCtlElementIndex": diffServPolicyMapAttachCtlElementIndex,
       "diffServPolicyMapAttachCtlAction": diffServPolicyMapAttachCtlAction,
       "diffServPolicyMapElementTable": diffServPolicyMapElementTable,
       "diffServPolicyMapElementEntry": diffServPolicyMapElementEntry,
       "diffServPolicyMapElementIndex": diffServPolicyMapElementIndex,
       "diffServPolicyMapElementClassMapIndex": diffServPolicyMapElementClassMapIndex,
       "diffServPolicyMapElementMeterIndex": diffServPolicyMapElementMeterIndex,
       "diffServPolicyMapElementActionIndex": diffServPolicyMapElementActionIndex,
       "diffServPolicyMapElementStatus": diffServPolicyMapElementStatus,
       "diffServClassMapTable": diffServClassMapTable,
       "diffServClassMapEntry": diffServClassMapEntry,
       "diffServClassMapIndex": diffServClassMapIndex,
       "diffServClassMapName": diffServClassMapName,
       "diffServClassMapDescription": diffServClassMapDescription,
       "diffServClassMapMatchType": diffServClassMapMatchType,
       "diffServClassMapElementIndexTypeList": diffServClassMapElementIndexTypeList,
       "diffServClassMapElementIndexList": diffServClassMapElementIndexList,
       "diffServClassMapStatus": diffServClassMapStatus,
       "diffServClassMapAttachCtl": diffServClassMapAttachCtl,
       "diffServClassMapAttachCtlIndex": diffServClassMapAttachCtlIndex,
       "diffServClassMapAttachCtlElementIndexType": diffServClassMapAttachCtlElementIndexType,
       "diffServClassMapAttachCtlElementIndex": diffServClassMapAttachCtlElementIndex,
       "diffServClassMapAttachCtlAction": diffServClassMapAttachCtlAction,
       "diffServAclTable": diffServAclTable,
       "diffServAclEntry": diffServAclEntry,
       "diffServAclIndex": diffServAclIndex,
       "diffServAclName": diffServAclName,
       "diffServAclType": diffServAclType,
       "diffServAclAceIndexList": diffServAclAceIndexList,
       "diffServAclStatus": diffServAclStatus,
       "diffServAclAttachCtl": diffServAclAttachCtl,
       "diffServAclAttachCtlIndex": diffServAclAttachCtlIndex,
       "diffServAclAttachCtlAceType": diffServAclAttachCtlAceType,
       "diffServAclAttachCtlAceIndex": diffServAclAttachCtlAceIndex,
       "diffServAclAttachCtlAction": diffServAclAttachCtlAction,
       "diffServIpAceTable": diffServIpAceTable,
       "diffServIpAceEntry": diffServIpAceEntry,
       "diffServIpAceIndex": diffServIpAceIndex,
       "diffServIpAceType": diffServIpAceType,
       "diffServIpAceAccess": diffServIpAceAccess,
       "diffServIpAceSourceIpAddr": diffServIpAceSourceIpAddr,
       "diffServIpAceSourceIpAddrBitmask": diffServIpAceSourceIpAddrBitmask,
       "diffServIpAceDestIpAddr": diffServIpAceDestIpAddr,
       "diffServIpAceDestIpAddrBitmask": diffServIpAceDestIpAddrBitmask,
       "diffServIpAceProtocol": diffServIpAceProtocol,
       "diffServIpAcePrec": diffServIpAcePrec,
       "diffServIpAceTos": diffServIpAceTos,
       "diffServIpAceDscp": diffServIpAceDscp,
       "diffServIpAceSourcePortOp": diffServIpAceSourcePortOp,
       "diffServIpAceMinSourcePort": diffServIpAceMinSourcePort,
       "diffServIpAceSourcePortBitmask": diffServIpAceSourcePortBitmask,
       "diffServIpAceDestPortOp": diffServIpAceDestPortOp,
       "diffServIpAceMinDestPort": diffServIpAceMinDestPort,
       "diffServIpAceDestPortBitmask": diffServIpAceDestPortBitmask,
       "diffServIpAceControlCode": diffServIpAceControlCode,
       "diffServIpAceControlCodeBitmask": diffServIpAceControlCodeBitmask,
       "diffServIpAceStatus": diffServIpAceStatus,
       "diffServMacAceTable": diffServMacAceTable,
       "diffServMacAceEntry": diffServMacAceEntry,
       "diffServMacAceIndex": diffServMacAceIndex,
       "diffServMacAceAccess": diffServMacAceAccess,
       "diffServMacAcePktformat": diffServMacAcePktformat,
       "diffServMacAceSourceMacAddr": diffServMacAceSourceMacAddr,
       "diffServMacAceSourceMacAddrBitmask": diffServMacAceSourceMacAddrBitmask,
       "diffServMacAceDestMacAddr": diffServMacAceDestMacAddr,
       "diffServMacAceDestMacAddrBitmask": diffServMacAceDestMacAddrBitmask,
       "diffServMacAceVidOp": diffServMacAceVidOp,
       "diffServMacAceMinVid": diffServMacAceMinVid,
       "diffServMacAceVidBitmask": diffServMacAceVidBitmask,
       "diffServMacAceEtherTypeOp": diffServMacAceEtherTypeOp,
       "diffServMacAceEtherTypeBitmask": diffServMacAceEtherTypeBitmask,
       "diffServMacAceMinEtherType": diffServMacAceMinEtherType,
       "diffServMacAceStatus": diffServMacAceStatus,
       "diffServActionTable": diffServActionTable,
       "diffServActionEntry": diffServActionEntry,
       "diffServActionIndex": diffServActionIndex,
       "diffServActionList": diffServActionList,
       "diffServActionPktNewPri": diffServActionPktNewPri,
       "diffServActionPktNewDscp": diffServActionPktNewDscp,
       "diffServActionRedPktNewDscp": diffServActionRedPktNewDscp,
       "diffServActionRedDrop": diffServActionRedDrop,
       "diffServActionStatus": diffServActionStatus,
       "diffServMeterTable": diffServMeterTable,
       "diffServMeterEntry": diffServMeterEntry,
       "diffServMeterIndex": diffServMeterIndex,
       "diffServMeterModel": diffServMeterModel,
       "diffServMeterRate": diffServMeterRate,
       "diffServMeterBurstSize": diffServMeterBurstSize,
       "diffServMeterInterval": diffServMeterInterval,
       "diffServMeterStatus": diffServMeterStatus,
       "securityMgt": securityMgt,
       "privateVlanMgt": privateVlanMgt,
       "privateVlanVlanTable": privateVlanVlanTable,
       "privateVlanVlanEntry": privateVlanVlanEntry,
       "privateVlanVlanIndex": privateVlanVlanIndex,
       "privateVlanVlanType": privateVlanVlanType,
       "privateVlanAssoicatedPrimaryVlan": privateVlanAssoicatedPrimaryVlan,
       "privateVlanPrivatePortTable": privateVlanPrivatePortTable,
       "privateVlanPrivatePortEntry": privateVlanPrivatePortEntry,
       "privateVlanPrivatePortIfIndex": privateVlanPrivatePortIfIndex,
       "privateVlanPrivatePortSecondaryVlan": privateVlanPrivatePortSecondaryVlan,
       "privateVlanPromPortTable": privateVlanPromPortTable,
       "privateVlanPromPortEntry": privateVlanPromPortEntry,
       "privateVlanPromPortIfIndex": privateVlanPromPortIfIndex,
       "privateVlanPromPortPrimaryVlanId": privateVlanPromPortPrimaryVlanId,
       "privateVlanPromPortSecondaryRemap": privateVlanPromPortSecondaryRemap,
       "privateVlanPromPortSecondaryRemap2k": privateVlanPromPortSecondaryRemap2k,
       "privateVlanPromPortSecondaryRemap3k": privateVlanPromPortSecondaryRemap3k,
       "privateVlanPromPortSecondaryRemap4k": privateVlanPromPortSecondaryRemap4k,
       "portSecurityMgt": portSecurityMgt,
       "portSecPortTable": portSecPortTable,
       "portSecPortEntry": portSecPortEntry,
       "portSecPortIndex": portSecPortIndex,
       "portSecPortStatus": portSecPortStatus,
       "portSecAction": portSecAction,
       "portSecMaxMacCount": portSecMaxMacCount,
       "radiusMgt": radiusMgt,
       "radiusServerPortNumber": radiusServerPortNumber,
       "radiusServerKey": radiusServerKey,
       "radiusServerRetransmit": radiusServerRetransmit,
       "radiusServerTimeout": radiusServerTimeout,
       "radiusMultipleServerTable": radiusMultipleServerTable,
       "radiusMultipleServerEntry": radiusMultipleServerEntry,
       "radiusMultipleServerIndex": radiusMultipleServerIndex,
       "radiusMultipleServerAddress": radiusMultipleServerAddress,
       "radiusMultipleServerPortNumber": radiusMultipleServerPortNumber,
       "radiusMultipleServerKey": radiusMultipleServerKey,
       "radiusMultipleServerRetransmit": radiusMultipleServerRetransmit,
       "radiusMultipleServerTimeout": radiusMultipleServerTimeout,
       "radiusMultipleServerStatus": radiusMultipleServerStatus,
       "tacacsMgt": tacacsMgt,
       "tacacsServerAddress": tacacsServerAddress,
       "tacacsServerPortNumber": tacacsServerPortNumber,
       "tacacsServerKey": tacacsServerKey,
       "sshMgt": sshMgt,
       "sshServerStatus": sshServerStatus,
       "sshServerMajorVersion": sshServerMajorVersion,
       "sshServerMinorVersion": sshServerMinorVersion,
       "sshTimeout": sshTimeout,
       "sshAuthRetries": sshAuthRetries,
       "sshConnInfoTable": sshConnInfoTable,
       "sshConnInfoEntry": sshConnInfoEntry,
       "sshConnID": sshConnID,
       "sshConnMajorVersion": sshConnMajorVersion,
       "sshConnMinorVersion": sshConnMinorVersion,
       "sshConnStatus": sshConnStatus,
       "sshConnUserName": sshConnUserName,
       "sshDisconnect": sshDisconnect,
       "sshConnEncryptionTypeStr": sshConnEncryptionTypeStr,
       "sshKeySize": sshKeySize,
       "sshRsaHostKey1": sshRsaHostKey1,
       "sshRsaHostKey2": sshRsaHostKey2,
       "sshRsaHostKey3": sshRsaHostKey3,
       "sshRsaHostKey4": sshRsaHostKey4,
       "sshRsaHostKey5": sshRsaHostKey5,
       "sshRsaHostKey6": sshRsaHostKey6,
       "sshRsaHostKey7": sshRsaHostKey7,
       "sshRsaHostKey8": sshRsaHostKey8,
       "sshDsaHostKey1": sshDsaHostKey1,
       "sshDsaHostKey2": sshDsaHostKey2,
       "sshDsaHostKey3": sshDsaHostKey3,
       "sshDsaHostKey4": sshDsaHostKey4,
       "sshDsaHostKey5": sshDsaHostKey5,
       "sshDsaHostKey6": sshDsaHostKey6,
       "sshDsaHostKey7": sshDsaHostKey7,
       "sshDsaHostKey8": sshDsaHostKey8,
       "sshHostKeyGenAction": sshHostKeyGenAction,
       "sshHostKeyGenStatus": sshHostKeyGenStatus,
       "sshHostKeySaveAction": sshHostKeySaveAction,
       "sshHostKeySaveStatus": sshHostKeySaveStatus,
       "sshHostKeyDelAction": sshHostKeyDelAction,
       "sshUserTable": sshUserTable,
       "sshUserEntry": sshUserEntry,
       "sshUserName": sshUserName,
       "sshUserRsaKey1": sshUserRsaKey1,
       "sshUserRsaKey2": sshUserRsaKey2,
       "sshUserRsaKey3": sshUserRsaKey3,
       "sshUserRsaKey4": sshUserRsaKey4,
       "sshUserRsaKey5": sshUserRsaKey5,
       "sshUserRsaKey6": sshUserRsaKey6,
       "sshUserRsaKey7": sshUserRsaKey7,
       "sshUserRsaKey8": sshUserRsaKey8,
       "sshUserDsaKey1": sshUserDsaKey1,
       "sshUserDsaKey2": sshUserDsaKey2,
       "sshUserDsaKey3": sshUserDsaKey3,
       "sshUserDsaKey4": sshUserDsaKey4,
       "sshUserDsaKey5": sshUserDsaKey5,
       "sshUserDsaKey6": sshUserDsaKey6,
       "sshUserDsaKey7": sshUserDsaKey7,
       "sshUserDsaKey8": sshUserDsaKey8,
       "sshUserKeyDelAction": sshUserKeyDelAction,
       "sshRsaHostKeySHA1FingerPrint": sshRsaHostKeySHA1FingerPrint,
       "sshRsaHostKeyMD5FingerPrint": sshRsaHostKeyMD5FingerPrint,
       "sshDsaHostKeySHA1FingerPrint": sshDsaHostKeySHA1FingerPrint,
       "sshDsaHostKeyMD5FingerPrint": sshDsaHostKeyMD5FingerPrint,
       "aclMgt": aclMgt,
       "ipFilterMgt": ipFilterMgt,
       "ipFilterSnmpTable": ipFilterSnmpTable,
       "ipFilterSnmpEntry": ipFilterSnmpEntry,
       "ipFilterSnmpStartAddress": ipFilterSnmpStartAddress,
       "ipFilterSnmpEndAddress": ipFilterSnmpEndAddress,
       "ipFilterSnmpStatus": ipFilterSnmpStatus,
       "ipFilterHTTPTable": ipFilterHTTPTable,
       "ipFilterHTTPEntry": ipFilterHTTPEntry,
       "ipFilterHTTPStartAddress": ipFilterHTTPStartAddress,
       "ipFilterHTTPEndAddress": ipFilterHTTPEndAddress,
       "ipFilterHTTPStatus": ipFilterHTTPStatus,
       "ipFilterTelnetTable": ipFilterTelnetTable,
       "ipFilterTelnetEntry": ipFilterTelnetEntry,
       "ipFilterTelnetStartAddress": ipFilterTelnetStartAddress,
       "ipFilterTelnetEndAddress": ipFilterTelnetEndAddress,
       "ipFilterTelnetStatus": ipFilterTelnetStatus,
       "sysLogMgt": sysLogMgt,
       "sysLogStatus": sysLogStatus,
       "sysLogHistoryFlashLevel": sysLogHistoryFlashLevel,
       "sysLogHistoryRamLevel": sysLogHistoryRamLevel,
       "remoteLogMgt": remoteLogMgt,
       "remoteLogStatus": remoteLogStatus,
       "remoteLogLevel": remoteLogLevel,
       "remoteLogFacilityType": remoteLogFacilityType,
       "remoteLogServerTable": remoteLogServerTable,
       "remoteLogServerEntry": remoteLogServerEntry,
       "remoteLogServerIp": remoteLogServerIp,
       "remoteLogServerStatus": remoteLogServerStatus,
       "smtpMgt": smtpMgt,
       "smtpStatus": smtpStatus,
       "smtpSeverityLevel": smtpSeverityLevel,
       "smtpSourceEMail": smtpSourceEMail,
       "smtpServerIpTable": smtpServerIpTable,
       "smtpServerIpEntry": smtpServerIpEntry,
       "smtpServerIp": smtpServerIp,
       "smtpServerIpStatus": smtpServerIpStatus,
       "smtpDestEMailTable": smtpDestEMailTable,
       "smtpDestEMailEntry": smtpDestEMailEntry,
       "smtpDestEMail": smtpDestEMail,
       "smtpDestEMailStatus": smtpDestEMailStatus,
       "lineMgt": lineMgt,
       "consoleMgt": consoleMgt,
       "consoleDataBits": consoleDataBits,
       "consoleParity": consoleParity,
       "consoleStopBits": consoleStopBits,
       "consoleExecTimeout": consoleExecTimeout,
       "consolePasswordThreshold": consolePasswordThreshold,
       "consoleSilentTime": consoleSilentTime,
       "consoleAdminBaudRate": consoleAdminBaudRate,
       "consoleOperBaudRate": consoleOperBaudRate,
       "consoleLoginResponseTimeout": consoleLoginResponseTimeout,
       "telnetMgt": telnetMgt,
       "telnetExecTimeout": telnetExecTimeout,
       "telnetPasswordThreshold": telnetPasswordThreshold,
       "telnetLoginResponseTimeout": telnetLoginResponseTimeout,
       "telnetStatus": telnetStatus,
       "telnetPortNumber": telnetPortNumber,
       "sysTimeMgt": sysTimeMgt,
       "sntpMgt": sntpMgt,
       "sntpStatus": sntpStatus,
       "sntpServiceMode": sntpServiceMode,
       "sntpPollInterval": sntpPollInterval,
       "sntpServerTable": sntpServerTable,
       "sntpServerEntry": sntpServerEntry,
       "sntpServerIndex": sntpServerIndex,
       "sntpServerIpAddress": sntpServerIpAddress,
       "sysCurrentTime": sysCurrentTime,
       "sysTimeZone": sysTimeZone,
       "sysTimeZoneName": sysTimeZoneName,
       "fileMgt": fileMgt,
       "fileCopyMgt": fileCopyMgt,
       "fileCopySrcOperType": fileCopySrcOperType,
       "fileCopySrcFileName": fileCopySrcFileName,
       "fileCopyDestOperType": fileCopyDestOperType,
       "fileCopyDestFileName": fileCopyDestFileName,
       "fileCopyFileType": fileCopyFileType,
       "fileCopyTftpServer": fileCopyTftpServer,
       "fileCopyUnitId": fileCopyUnitId,
       "fileCopyAction": fileCopyAction,
       "fileCopyStatus": fileCopyStatus,
       "fileInfoMgt": fileInfoMgt,
       "fileInfoTable": fileInfoTable,
       "fileInfoEntry": fileInfoEntry,
       "fileInfoUnitID": fileInfoUnitID,
       "fileInfoFileName": fileInfoFileName,
       "fileInfoFileType": fileInfoFileType,
       "fileInfoIsStartUp": fileInfoIsStartUp,
       "fileInfoFileSize": fileInfoFileSize,
       "fileInfoCreationTime": fileInfoCreationTime,
       "fileInfoDelete": fileInfoDelete,
       "fileAutoDownloadResultTable": fileAutoDownloadResultTable,
       "fileAutoDownloadResultEntry": fileAutoDownloadResultEntry,
       "fileAutoDownloadResultUnitID": fileAutoDownloadResultUnitID,
       "fileAutoDownloadResultAction": fileAutoDownloadResultAction,
       "fileAutoDownloadResultStatus": fileAutoDownloadResultStatus,
       "mvrMgt": mvrMgt,
       "mvrStatus": mvrStatus,
       "mvrVlanId": mvrVlanId,
       "mvrMaxGroups": mvrMaxGroups,
       "mvrCurrentGroups": mvrCurrentGroups,
       "mvrGroupsCtl": mvrGroupsCtl,
       "mvrGroupsCtlId": mvrGroupsCtlId,
       "mvrGroupsCtlCount": mvrGroupsCtlCount,
       "mvrGroupsCtlAction": mvrGroupsCtlAction,
       "mvrGroupTable": mvrGroupTable,
       "mvrGroupEntry": mvrGroupEntry,
       "mvrGroupId": mvrGroupId,
       "mvrGroutActive": mvrGroutActive,
       "mvrGroupStatus": mvrGroupStatus,
       "mvrGroupStaticTable": mvrGroupStaticTable,
       "mvrGroupStaticEntry": mvrGroupStaticEntry,
       "mvrGroupStaticAddress": mvrGroupStaticAddress,
       "mvrGroupStaticPorts": mvrGroupStaticPorts,
       "mvrGroupStaticStatus": mvrGroupStaticStatus,
       "mvrGroupCurrentTable": mvrGroupCurrentTable,
       "mvrGroupCurrentEntry": mvrGroupCurrentEntry,
       "mvrGroupCurrentAddress": mvrGroupCurrentAddress,
       "mvrGroupCurrentPorts": mvrGroupCurrentPorts,
       "mvrPortTable": mvrPortTable,
       "mvrPortEntry": mvrPortEntry,
       "mvrIfIndex": mvrIfIndex,
       "mvrPortType": mvrPortType,
       "mvrPortImmediateLeave": mvrPortImmediateLeave,
       "mvrPortActive": mvrPortActive,
       "mvrRunningStatus": mvrRunningStatus,
       "dhcpSnoopMgt": dhcpSnoopMgt,
       "dhcpSnoopGlobal": dhcpSnoopGlobal,
       "dhcpSnoopEnable": dhcpSnoopEnable,
       "dhcpSnoopVerifyMacAddressEnable": dhcpSnoopVerifyMacAddressEnable,
       "dhcpSnoopInformationOptionEnable": dhcpSnoopInformationOptionEnable,
       "dhcpSnoopInformationOptionPolicy": dhcpSnoopInformationOptionPolicy,
       "dhcpSnoopVlan": dhcpSnoopVlan,
       "dhcpSnoopVlanConfigTable": dhcpSnoopVlanConfigTable,
       "dhcpSnoopVlanConfigEntry": dhcpSnoopVlanConfigEntry,
       "dhcpSnoopVlanIndex": dhcpSnoopVlanIndex,
       "dhcpSnoopVlanEnable": dhcpSnoopVlanEnable,
       "dhcpSnoopInterface": dhcpSnoopInterface,
       "dhcpSnoopPortConfigTable": dhcpSnoopPortConfigTable,
       "dhcpSnoopPortConfigEntry": dhcpSnoopPortConfigEntry,
       "dhcpSnoopPortIfIndex": dhcpSnoopPortIfIndex,
       "dhcpSnoopPortTrustEnable": dhcpSnoopPortTrustEnable,
       "dhcpSnoopBindings": dhcpSnoopBindings,
       "dhcpSnoopBindingsTable": dhcpSnoopBindingsTable,
       "dhcpSnoopBindingsEntry": dhcpSnoopBindingsEntry,
       "dhcpSnoopBindingsVlanIndex": dhcpSnoopBindingsVlanIndex,
       "dhcpSnoopBindingsMacAddress": dhcpSnoopBindingsMacAddress,
       "dhcpSnoopBindingsAddrType": dhcpSnoopBindingsAddrType,
       "dhcpSnoopBindingsEntryType": dhcpSnoopBindingsEntryType,
       "dhcpSnoopBindingsIpAddress": dhcpSnoopBindingsIpAddress,
       "dhcpSnoopBindingsPortIfIndex": dhcpSnoopBindingsPortIfIndex,
       "dhcpSnoopBindingsLeaseTime": dhcpSnoopBindingsLeaseTime,
       "dhcpSnoopStatistics": dhcpSnoopStatistics,
       "dhcpSnoopTotalForwardedPkts": dhcpSnoopTotalForwardedPkts,
       "dhcpSnoopUntrustedPortDroppedPkts": dhcpSnoopUntrustedPortDroppedPkts,
       "clusterMgt": clusterMgt,
       "clusterEnable": clusterEnable,
       "clusterCommanderEnable": clusterCommanderEnable,
       "clusterIpPool": clusterIpPool,
       "clusterClearCandidateTable": clusterClearCandidateTable,
       "clusterRole": clusterRole,
       "clusterMemberCount": clusterMemberCount,
       "clusterCandidateCount": clusterCandidateCount,
       "clusterCandidateTable": clusterCandidateTable,
       "clusterCandidateEntry": clusterCandidateEntry,
       "clusterCandidateMacAddr": clusterCandidateMacAddr,
       "clusterCandidateDesc": clusterCandidateDesc,
       "clusterCandidateRole": clusterCandidateRole,
       "clusterMemberTable": clusterMemberTable,
       "clusterMemberEntry": clusterMemberEntry,
       "clusterMemberId": clusterMemberId,
       "clusterMemberMacAddr": clusterMemberMacAddr,
       "clusterMemberDesc": clusterMemberDesc,
       "clusterMemberActive": clusterMemberActive,
       "clusterMemberAddCtl": clusterMemberAddCtl,
       "clusterMemberAddCtlMacAddr": clusterMemberAddCtlMacAddr,
       "clusterMemberAddCtlId": clusterMemberAddCtlId,
       "clusterMemberAddCtlAction": clusterMemberAddCtlAction,
       "clusterMemberRemoveCtl": clusterMemberRemoveCtl,
       "clusterMemberRemoveCtlId": clusterMemberRemoveCtlId,
       "clusterMemberRemoveCtlAction": clusterMemberRemoveCtlAction,
       "ipSrcGuardMgt": ipSrcGuardMgt,
       "ipSrcGuardConfigTable": ipSrcGuardConfigTable,
       "ipSrcGuardConfigEntry": ipSrcGuardConfigEntry,
       "ipSrcGuardPortIfIndex": ipSrcGuardPortIfIndex,
       "ipSrcGuardMode": ipSrcGuardMode,
       "ipSrcGuardAddrTable": ipSrcGuardAddrTable,
       "ipSrcGuardAddrEntry": ipSrcGuardAddrEntry,
       "ipSrcGuardBindingsVlanIndex": ipSrcGuardBindingsVlanIndex,
       "ipSrcGuardBindingsMacAddress": ipSrcGuardBindingsMacAddress,
       "ipSrcGuardBindingsAddrType": ipSrcGuardBindingsAddrType,
       "ipSrcGuardBindingsEntryType": ipSrcGuardBindingsEntryType,
       "ipSrcGuardBindingsIpAddress": ipSrcGuardBindingsIpAddress,
       "ipSrcGuardBindingsPortIfIndex": ipSrcGuardBindingsPortIfIndex,
       "ipSrcGuardBindingsLeaseTime": ipSrcGuardBindingsLeaseTime,
       "ipSrcGuardBindingsStatus": ipSrcGuardBindingsStatus,
       "smc6152L2Notifications": smc6152L2Notifications,
       "smc6152L2Traps": smc6152L2Traps,
       "smc6152L2TrapsPrefix": smc6152L2TrapsPrefix,
       "swPowerStatusChangeTrap": swPowerStatusChangeTrap,
       "swPortSecurityTrap": swPortSecurityTrap,
       "smc6152L2Conformance": smc6152L2Conformance}
)
