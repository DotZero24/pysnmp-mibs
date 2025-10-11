# SNMP MIB module (ES3552M-AND-PoE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/edgecore/ES3552M-AND-PoE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:51 2025
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

(dot1xAuthConfigEntry,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xAuthConfigEntry")

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

es3552m_and_poeMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12)
)
if mibBuilder.loadTexts:
    es3552m_and_poeMIB.setRevisions(
        ("2006-05-24 00:00",)
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

_Accton_ObjectIdentity = ObjectIdentity
accton = _Accton_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259)
)
_SnmpMgt_ObjectIdentity = ObjectIdentity
snmpMgt = _SnmpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 6)
)
_CheetahSwitchMgt_ObjectIdentity = ObjectIdentity
cheetahSwitchMgt = _CheetahSwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 6, 10)
)
_Edgecore_ObjectIdentity = ObjectIdentity
edgecore = _Edgecore_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8)
)
_EdgeCoreSwitchMgt_ObjectIdentity = ObjectIdentity
edgeCoreSwitchMgt = _EdgeCoreSwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1)
)
_Es3552m_and_poeMIBObjects_ObjectIdentity = ObjectIdentity
es3552m_and_poeMIBObjects = _Es3552m_and_poeMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1)
)
_SwitchMgt_ObjectIdentity = ObjectIdentity
switchMgt = _SwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1)
)
_SwitchNumber_Type = Integer32
_SwitchNumber_Object = MibScalar
switchNumber = _SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 2),
    _SwitchNumber_Type()
)
switchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumber.setStatus("current")
_SwitchInfoTable_Object = MibTable
switchInfoTable = _SwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3)
)
if mibBuilder.loadTexts:
    switchInfoTable.setStatus("current")
_SwitchInfoEntry_Object = MibTableRow
switchInfoEntry = _SwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1)
)
switchInfoEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "swUnitIndex"),
)
if mibBuilder.loadTexts:
    switchInfoEntry.setStatus("current")
_SwUnitIndex_Type = Integer32
_SwUnitIndex_Object = MibTableColumn
swUnitIndex = _SwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 6),
    _SwOpCodeVer_Type()
)
swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOpCodeVer.setStatus("current")
_SwPortNumber_Type = Integer32
_SwPortNumber_Object = MibTableColumn
swPortNumber = _SwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 3, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 4),
    _SwitchOperState_Type()
)
switchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchOperState.setStatus("current")
_SwitchProductId_ObjectIdentity = ObjectIdentity
switchProductId = _SwitchProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 5, 5),
    _SwProdUrl_Type()
)
swProdUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdUrl.setStatus("current")
_SwIdentifier_Type = Integer32
_SwIdentifier_Object = MibScalar
swIdentifier = _SwIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 5, 6),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 5, 7),
    _SwChassisServiceTag_Type()
)
swChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swChassisServiceTag.setStatus("current")
_SwitchIndivPowerTable_Object = MibTable
switchIndivPowerTable = _SwitchIndivPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 6)
)
if mibBuilder.loadTexts:
    switchIndivPowerTable.setStatus("current")
_SwitchIndivPowerEntry_Object = MibTableRow
switchIndivPowerEntry = _SwitchIndivPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 6, 1)
)
switchIndivPowerEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "swIndivPowerUnitIndex"),
    (0, "ES3552M-AND-PoE-MIB", "swIndivPowerIndex"),
)
if mibBuilder.loadTexts:
    switchIndivPowerEntry.setStatus("current")
_SwIndivPowerUnitIndex_Type = Integer32
_SwIndivPowerUnitIndex_Object = MibTableColumn
swIndivPowerUnitIndex = _SwIndivPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 7),
    _SwitchJumboFrameStatus_Type()
)
switchJumboFrameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchJumboFrameStatus.setStatus("current")
_AmtrMgt_ObjectIdentity = ObjectIdentity
amtrMgt = _AmtrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 8)
)
_AmtrMacAddrAgingStatus_Type = EnabledStatus
_AmtrMacAddrAgingStatus_Object = MibScalar
amtrMacAddrAgingStatus = _AmtrMacAddrAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 8, 3),
    _AmtrMacAddrAgingStatus_Type()
)
amtrMacAddrAgingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amtrMacAddrAgingStatus.setStatus("current")
_AmtrMacAddrDynamicCount_Type = Counter32
_AmtrMacAddrDynamicCount_Object = MibScalar
amtrMacAddrDynamicCount = _AmtrMacAddrDynamicCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 8, 4),
    _AmtrMacAddrDynamicCount_Type()
)
amtrMacAddrDynamicCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amtrMacAddrDynamicCount.setStatus("current")
_AmtrMacAddrStaticCount_Type = Counter32
_AmtrMacAddrStaticCount_Object = MibScalar
amtrMacAddrStaticCount = _AmtrMacAddrStaticCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 8, 5),
    _AmtrMacAddrStaticCount_Type()
)
amtrMacAddrStaticCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amtrMacAddrStaticCount.setStatus("current")
_AmtrMacAddrTotalCount_Type = Counter32
_AmtrMacAddrTotalCount_Object = MibScalar
amtrMacAddrTotalCount = _AmtrMacAddrTotalCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 1, 8, 6),
    _AmtrMacAddrTotalCount_Type()
)
amtrMacAddrTotalCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    amtrMacAddrTotalCount.setStatus("current")
_PortMgt_ObjectIdentity = ObjectIdentity
portMgt = _PortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1)
)
portEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 1),
    _PortIndex_Type()
)
portIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portIndex.setStatus("current")


class _PortName_Type(DisplayString):
    """Custom type portName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_PortName_Type.__name__ = "DisplayString"
_PortName_Object = MibTableColumn
portName = _PortName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("current")
_PortAutonegotiation_Type = EnabledStatus
_PortAutonegotiation_Object = MibTableColumn
portAutonegotiation = _PortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")
_PortTrunkIndex_Type = Integer32
_PortTrunkIndex_Object = MibTableColumn
portTrunkIndex = _PortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 12),
    _PortComboForcedMode_Type()
)
portComboForcedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portComboForcedMode.setStatus("current")


class _PortMasterSlaveModeCfg_Type(Integer32):
    """Custom type portMasterSlaveModeCfg based on Integer32"""
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
        *(("master", 1),
          ("slave", 2),
          ("auto", 3),
          ("autoPreferMaster", 4),
          ("autoPreferSlave", 5))
    )


_PortMasterSlaveModeCfg_Type.__name__ = "Integer32"
_PortMasterSlaveModeCfg_Object = MibTableColumn
portMasterSlaveModeCfg = _PortMasterSlaveModeCfg_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 1, 1, 15),
    _PortMasterSlaveModeCfg_Type()
)
portMasterSlaveModeCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portMasterSlaveModeCfg.setStatus("current")
_CableDiagMgt_ObjectIdentity = ObjectIdentity
cableDiagMgt = _CableDiagMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 3)
)
_CableDiagCtlAction_Type = Integer32
_CableDiagCtlAction_Object = MibScalar
cableDiagCtlAction = _CableDiagCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 3, 1),
    _CableDiagCtlAction_Type()
)
cableDiagCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cableDiagCtlAction.setStatus("current")
_CableDiagResultTable_Object = MibTable
cableDiagResultTable = _CableDiagResultTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 3, 2)
)
if mibBuilder.loadTexts:
    cableDiagResultTable.setStatus("current")
_CableDiagResultEntry_Object = MibTableRow
cableDiagResultEntry = _CableDiagResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 3, 2, 1)
)
cableDiagResultEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "cableDiagResultIfIndex"),
)
if mibBuilder.loadTexts:
    cableDiagResultEntry.setStatus("current")
_CableDiagResultIfIndex_Type = Integer32
_CableDiagResultIfIndex_Object = MibTableColumn
cableDiagResultIfIndex = _CableDiagResultIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 3, 2, 1, 1),
    _CableDiagResultIfIndex_Type()
)
cableDiagResultIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cableDiagResultIfIndex.setStatus("current")


class _CableDiagResultStatusPairA_Type(Integer32):
    """Custom type cableDiagResultStatusPairA based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notTestedYet", 1),
          ("ok", 2),
          ("open", 3),
          ("short", 4),
          ("openShort", 5),
          ("crosstalk", 6),
          ("unknown", 7),
          ("impedanceMismatch", 8),
          ("fail", 9),
          ("notSupport", 10))
    )


_CableDiagResultStatusPairA_Type.__name__ = "Integer32"
_CableDiagResultStatusPairA_Object = MibTableColumn
cableDiagResultStatusPairA = _CableDiagResultStatusPairA_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 3, 2, 1, 2),
    _CableDiagResultStatusPairA_Type()
)
cableDiagResultStatusPairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultStatusPairA.setStatus("current")


class _CableDiagResultStatusPairB_Type(Integer32):
    """Custom type cableDiagResultStatusPairB based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("notTestedYet", 1),
          ("ok", 2),
          ("open", 3),
          ("short", 4),
          ("openShort", 5),
          ("crosstalk", 6),
          ("unknown", 7),
          ("impedanceMismatch", 8),
          ("fail", 9),
          ("notSupport", 10))
    )


_CableDiagResultStatusPairB_Type.__name__ = "Integer32"
_CableDiagResultStatusPairB_Object = MibTableColumn
cableDiagResultStatusPairB = _CableDiagResultStatusPairB_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 3, 2, 1, 3),
    _CableDiagResultStatusPairB_Type()
)
cableDiagResultStatusPairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultStatusPairB.setStatus("current")
_CableDiagResultDistancePairA_Type = Integer32
_CableDiagResultDistancePairA_Object = MibTableColumn
cableDiagResultDistancePairA = _CableDiagResultDistancePairA_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 3, 2, 1, 6),
    _CableDiagResultDistancePairA_Type()
)
cableDiagResultDistancePairA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultDistancePairA.setStatus("current")
_CableDiagResultDistancePairB_Type = Integer32
_CableDiagResultDistancePairB_Object = MibTableColumn
cableDiagResultDistancePairB = _CableDiagResultDistancePairB_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 3, 2, 1, 7),
    _CableDiagResultDistancePairB_Type()
)
cableDiagResultDistancePairB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultDistancePairB.setStatus("current")


class _CableDiagResultTime_Type(DisplayString):
    """Custom type cableDiagResultTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_CableDiagResultTime_Type.__name__ = "DisplayString"
_CableDiagResultTime_Object = MibTableColumn
cableDiagResultTime = _CableDiagResultTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 3, 2, 1, 11),
    _CableDiagResultTime_Type()
)
cableDiagResultTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cableDiagResultTime.setStatus("current")
_PortUtilTable_Object = MibTable
portUtilTable = _PortUtilTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 6)
)
if mibBuilder.loadTexts:
    portUtilTable.setStatus("current")
_PortUtilEntry_Object = MibTableRow
portUtilEntry = _PortUtilEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 6, 1)
)
portUtilEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "portUtilIfIndex"),
)
if mibBuilder.loadTexts:
    portUtilEntry.setStatus("current")
_PortUtilIfIndex_Type = Integer32
_PortUtilIfIndex_Object = MibTableColumn
portUtilIfIndex = _PortUtilIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 6, 1, 1),
    _PortUtilIfIndex_Type()
)
portUtilIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portUtilIfIndex.setStatus("current")
_PortInOctetRate_Type = Counter64
_PortInOctetRate_Object = MibTableColumn
portInOctetRate = _PortInOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 6, 1, 2),
    _PortInOctetRate_Type()
)
portInOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInOctetRate.setStatus("current")
_PortInPacketRate_Type = Counter64
_PortInPacketRate_Object = MibTableColumn
portInPacketRate = _PortInPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 6, 1, 3),
    _PortInPacketRate_Type()
)
portInPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInPacketRate.setStatus("current")
_PortInUtil_Type = Integer32
_PortInUtil_Object = MibTableColumn
portInUtil = _PortInUtil_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 6, 1, 4),
    _PortInUtil_Type()
)
portInUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portInUtil.setStatus("current")
_PortOutOctetRate_Type = Counter64
_PortOutOctetRate_Object = MibTableColumn
portOutOctetRate = _PortOutOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 6, 1, 5),
    _PortOutOctetRate_Type()
)
portOutOctetRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutOctetRate.setStatus("current")
_PortOutPacketRate_Type = Counter64
_PortOutPacketRate_Object = MibTableColumn
portOutPacketRate = _PortOutPacketRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 6, 1, 6),
    _PortOutPacketRate_Type()
)
portOutPacketRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutPacketRate.setStatus("current")
_PortOutUtil_Type = Integer32
_PortOutUtil_Object = MibTableColumn
portOutUtil = _PortOutUtil_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 6, 1, 7),
    _PortOutUtil_Type()
)
portOutUtil.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portOutUtil.setStatus("current")
_PortVlanTrunkingTable_Object = MibTable
portVlanTrunkingTable = _PortVlanTrunkingTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 7)
)
if mibBuilder.loadTexts:
    portVlanTrunkingTable.setStatus("current")
_PortVlanTrunkingEntry_Object = MibTableRow
portVlanTrunkingEntry = _PortVlanTrunkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 7, 1)
)
portVlanTrunkingEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "portVlanTrunkingIfIndex"),
)
if mibBuilder.loadTexts:
    portVlanTrunkingEntry.setStatus("current")
_PortVlanTrunkingIfIndex_Type = Integer32
_PortVlanTrunkingIfIndex_Object = MibTableColumn
portVlanTrunkingIfIndex = _PortVlanTrunkingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 7, 1, 1),
    _PortVlanTrunkingIfIndex_Type()
)
portVlanTrunkingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portVlanTrunkingIfIndex.setStatus("current")
_PortVlanTrunkingStatus_Type = EnabledStatus
_PortVlanTrunkingStatus_Object = MibTableColumn
portVlanTrunkingStatus = _PortVlanTrunkingStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 2, 7, 1, 2),
    _PortVlanTrunkingStatus_Type()
)
portVlanTrunkingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portVlanTrunkingStatus.setStatus("current")
_TrunkMgt_ObjectIdentity = ObjectIdentity
trunkMgt = _TrunkMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 3)
)
_TrunkMaxId_Type = Integer32
_TrunkMaxId_Object = MibScalar
trunkMaxId = _TrunkMaxId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 3, 1),
    _TrunkMaxId_Type()
)
trunkMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMaxId.setStatus("current")
_TrunkValidNumber_Type = Integer32
_TrunkValidNumber_Object = MibScalar
trunkValidNumber = _TrunkValidNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 3, 2),
    _TrunkValidNumber_Type()
)
trunkValidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkValidNumber.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 3, 3)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 3, 3, 1)
)
trunkEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "trunkIndex"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")
_TrunkIndex_Type = Integer32
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 3, 3, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPorts_Type = PortList
_TrunkPorts_Object = MibTableColumn
trunkPorts = _TrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 3, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 3, 3, 1, 3),
    _TrunkCreation_Type()
)
trunkCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCreation.setStatus("current")
_TrunkStatus_Type = ValidStatus
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 3, 3, 1, 4),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")
_LacpMgt_ObjectIdentity = ObjectIdentity
lacpMgt = _LacpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 4)
)
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 4, 1, 1)
)
lacpPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "lacpPortIndex"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")
_LacpPortIndex_Type = Integer32
_LacpPortIndex_Object = MibTableColumn
lacpPortIndex = _LacpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 4, 1, 1, 1),
    _LacpPortIndex_Type()
)
lacpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lacpPortIndex.setStatus("current")
_LacpPortStatus_Type = EnabledStatus
_LacpPortStatus_Object = MibTableColumn
lacpPortStatus = _LacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 4, 1, 1, 2),
    _LacpPortStatus_Type()
)
lacpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortStatus.setStatus("current")
_StaMgt_ObjectIdentity = ObjectIdentity
staMgt = _StaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5)
)


class _StaSystemStatus_Type(EnabledStatus):
    """Custom type staSystemStatus based on EnabledStatus"""
    defaultValue = 1


_StaSystemStatus_Type.__name__ = "EnabledStatus"
_StaSystemStatus_Object = MibScalar
staSystemStatus = _StaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 1),
    _StaSystemStatus_Type()
)
staSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staSystemStatus.setStatus("current")
_StaPortTable_Object = MibTable
staPortTable = _StaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2)
)
if mibBuilder.loadTexts:
    staPortTable.setStatus("current")
_StaPortEntry_Object = MibTableRow
staPortEntry = _StaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    staPortEntry.setStatus("current")
_StaPortFastForward_Type = EnabledStatus
_StaPortFastForward_Object = MibTableColumn
staPortFastForward = _StaPortFastForward_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 2),
    _StaPortFastForward_Type()
)
staPortFastForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortFastForward.setStatus("current")
_StaPortProtocolMigration_Type = TruthValue
_StaPortProtocolMigration_Object = MibTableColumn
staPortProtocolMigration = _StaPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 3),
    _StaPortProtocolMigration_Type()
)
staPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortProtocolMigration.setStatus("current")
_StaPortOperEdgePort_Type = TruthValue
_StaPortOperEdgePort_Object = MibTableColumn
staPortOperEdgePort = _StaPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 6),
    _StaPortAdminPointToPoint_Type()
)
staPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminPointToPoint.setStatus("current")
_StaPortOperPointToPoint_Type = TruthValue
_StaPortOperPointToPoint_Object = MibTableColumn
staPortOperPointToPoint = _StaPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 11),
    _StaPortLongOperPathCost_Type()
)
staPortLongOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortLongOperPathCost.setStatus("current")
_StaPortRootGuardAdminStatus_Type = EnabledStatus
_StaPortRootGuardAdminStatus_Object = MibTableColumn
staPortRootGuardAdminStatus = _StaPortRootGuardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 13),
    _StaPortRootGuardAdminStatus_Type()
)
staPortRootGuardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortRootGuardAdminStatus.setStatus("current")
_StaPortRootGuardOperStatus_Type = EnabledStatus
_StaPortRootGuardOperStatus_Object = MibTableColumn
staPortRootGuardOperStatus = _StaPortRootGuardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 14),
    _StaPortRootGuardOperStatus_Type()
)
staPortRootGuardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    staPortRootGuardOperStatus.setStatus("current")
_StaPortBpduGuard_Type = EnabledStatus
_StaPortBpduGuard_Object = MibTableColumn
staPortBpduGuard = _StaPortBpduGuard_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 15),
    _StaPortBpduGuard_Type()
)
staPortBpduGuard.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortBpduGuard.setStatus("current")


class _StaPortAdminEdgePortWithAuto_Type(Integer32):
    """Custom type staPortAdminEdgePortWithAuto based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2),
          ("auto", 3))
    )


_StaPortAdminEdgePortWithAuto_Type.__name__ = "Integer32"
_StaPortAdminEdgePortWithAuto_Object = MibTableColumn
staPortAdminEdgePortWithAuto = _StaPortAdminEdgePortWithAuto_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 17),
    _StaPortAdminEdgePortWithAuto_Type()
)
staPortAdminEdgePortWithAuto.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminEdgePortWithAuto.setStatus("current")
_StaPortBpduFilter_Type = EnabledStatus
_StaPortBpduFilter_Object = MibTableColumn
staPortBpduFilter = _StaPortBpduFilter_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 18),
    _StaPortBpduFilter_Type()
)
staPortBpduFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortBpduFilter.setStatus("current")
_StaPortBpduGuardAutoRecovery_Type = EnabledStatus
_StaPortBpduGuardAutoRecovery_Object = MibTableColumn
staPortBpduGuardAutoRecovery = _StaPortBpduGuardAutoRecovery_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 19),
    _StaPortBpduGuardAutoRecovery_Type()
)
staPortBpduGuardAutoRecovery.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortBpduGuardAutoRecovery.setStatus("current")


class _StaPortBpduGuardAutoRecoveryInterval_Type(Unsigned32):
    """Custom type staPortBpduGuardAutoRecoveryInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 86400),
    )


_StaPortBpduGuardAutoRecoveryInterval_Type.__name__ = "Unsigned32"
_StaPortBpduGuardAutoRecoveryInterval_Object = MibTableColumn
staPortBpduGuardAutoRecoveryInterval = _StaPortBpduGuardAutoRecoveryInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 2, 1, 20),
    _StaPortBpduGuardAutoRecoveryInterval_Type()
)
staPortBpduGuardAutoRecoveryInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortBpduGuardAutoRecoveryInterval.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 5),
    _StaPathCostMethod_Type()
)
staPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPathCostMethod.setStatus("current")
_XstMgt_ObjectIdentity = ObjectIdentity
xstMgt = _XstMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6)
)


class _MstName_Type(DisplayString):
    """Custom type mstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_MstName_Type.__name__ = "DisplayString"
_MstName_Object = MibScalar
mstName = _MstName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 1),
    _MstName_Type()
)
mstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstName.setStatus("current")
_MstRevision_Type = Integer32
_MstRevision_Object = MibScalar
mstRevision = _MstRevision_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 2),
    _MstRevision_Type()
)
mstRevision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstRevision.setStatus("current")


class _MstMaxHops_Type(Integer32):
    """Custom type mstMaxHops based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 40),
    )


_MstMaxHops_Type.__name__ = "Integer32"
_MstMaxHops_Object = MibScalar
mstMaxHops = _MstMaxHops_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 3),
    _MstMaxHops_Type()
)
mstMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMaxHops.setStatus("current")
_XstInstanceCfgTable_Object = MibTable
xstInstanceCfgTable = _XstInstanceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    xstInstanceCfgTable.setStatus("current")
_XstInstanceCfgEntry_Object = MibTableRow
xstInstanceCfgEntry = _XstInstanceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1)
)
xstInstanceCfgEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "xstInstanceCfgIndex"),
)
if mibBuilder.loadTexts:
    xstInstanceCfgEntry.setStatus("current")


class _XstInstanceCfgIndex_Type(Integer32):
    """Custom type xstInstanceCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_XstInstanceCfgIndex_Type.__name__ = "Integer32"
_XstInstanceCfgIndex_Object = MibTableColumn
xstInstanceCfgIndex = _XstInstanceCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 1),
    _XstInstanceCfgIndex_Type()
)
xstInstanceCfgIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xstInstanceCfgIndex.setStatus("current")


class _XstInstanceCfgPriority_Type(Integer32):
    """Custom type xstInstanceCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 61440),
    )


_XstInstanceCfgPriority_Type.__name__ = "Integer32"
_XstInstanceCfgPriority_Object = MibTableColumn
xstInstanceCfgPriority = _XstInstanceCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 2),
    _XstInstanceCfgPriority_Type()
)
xstInstanceCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstanceCfgPriority.setStatus("current")
_XstInstanceCfgTimeSinceTopologyChange_Type = TimeTicks
_XstInstanceCfgTimeSinceTopologyChange_Object = MibTableColumn
xstInstanceCfgTimeSinceTopologyChange = _XstInstanceCfgTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 3),
    _XstInstanceCfgTimeSinceTopologyChange_Type()
)
xstInstanceCfgTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTimeSinceTopologyChange.setStatus("current")
_XstInstanceCfgTopChanges_Type = Integer32
_XstInstanceCfgTopChanges_Object = MibTableColumn
xstInstanceCfgTopChanges = _XstInstanceCfgTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 4),
    _XstInstanceCfgTopChanges_Type()
)
xstInstanceCfgTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTopChanges.setStatus("current")
_XstInstanceCfgDesignatedRoot_Type = BridgeId
_XstInstanceCfgDesignatedRoot_Object = MibTableColumn
xstInstanceCfgDesignatedRoot = _XstInstanceCfgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 5),
    _XstInstanceCfgDesignatedRoot_Type()
)
xstInstanceCfgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgDesignatedRoot.setStatus("current")
_XstInstanceCfgRootCost_Type = Integer32
_XstInstanceCfgRootCost_Object = MibTableColumn
xstInstanceCfgRootCost = _XstInstanceCfgRootCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 6),
    _XstInstanceCfgRootCost_Type()
)
xstInstanceCfgRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootCost.setStatus("current")
_XstInstanceCfgRootPort_Type = Integer32
_XstInstanceCfgRootPort_Object = MibTableColumn
xstInstanceCfgRootPort = _XstInstanceCfgRootPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 7),
    _XstInstanceCfgRootPort_Type()
)
xstInstanceCfgRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootPort.setStatus("current")
_XstInstanceCfgMaxAge_Type = Timeout
_XstInstanceCfgMaxAge_Object = MibTableColumn
xstInstanceCfgMaxAge = _XstInstanceCfgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 8),
    _XstInstanceCfgMaxAge_Type()
)
xstInstanceCfgMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgMaxAge.setStatus("current")
_XstInstanceCfgHelloTime_Type = Timeout
_XstInstanceCfgHelloTime_Object = MibTableColumn
xstInstanceCfgHelloTime = _XstInstanceCfgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 9),
    _XstInstanceCfgHelloTime_Type()
)
xstInstanceCfgHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHelloTime.setStatus("current")
_XstInstanceCfgHoldTime_Type = Timeout
_XstInstanceCfgHoldTime_Object = MibTableColumn
xstInstanceCfgHoldTime = _XstInstanceCfgHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 10),
    _XstInstanceCfgHoldTime_Type()
)
xstInstanceCfgHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHoldTime.setStatus("current")
_XstInstanceCfgForwardDelay_Type = Timeout
_XstInstanceCfgForwardDelay_Object = MibTableColumn
xstInstanceCfgForwardDelay = _XstInstanceCfgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 11),
    _XstInstanceCfgForwardDelay_Type()
)
xstInstanceCfgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgForwardDelay.setStatus("current")
_XstInstanceCfgBridgeMaxAge_Type = Timeout
_XstInstanceCfgBridgeMaxAge_Object = MibTableColumn
xstInstanceCfgBridgeMaxAge = _XstInstanceCfgBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 12),
    _XstInstanceCfgBridgeMaxAge_Type()
)
xstInstanceCfgBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeMaxAge.setStatus("current")
_XstInstanceCfgBridgeHelloTime_Type = Timeout
_XstInstanceCfgBridgeHelloTime_Object = MibTableColumn
xstInstanceCfgBridgeHelloTime = _XstInstanceCfgBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 13),
    _XstInstanceCfgBridgeHelloTime_Type()
)
xstInstanceCfgBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeHelloTime.setStatus("current")
_XstInstanceCfgBridgeForwardDelay_Type = Timeout
_XstInstanceCfgBridgeForwardDelay_Object = MibTableColumn
xstInstanceCfgBridgeForwardDelay = _XstInstanceCfgBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 14),
    _XstInstanceCfgBridgeForwardDelay_Type()
)
xstInstanceCfgBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeForwardDelay.setStatus("current")
_XstInstanceCfgTxHoldCount_Type = Integer32
_XstInstanceCfgTxHoldCount_Object = MibTableColumn
xstInstanceCfgTxHoldCount = _XstInstanceCfgTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 15),
    _XstInstanceCfgTxHoldCount_Type()
)
xstInstanceCfgTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTxHoldCount.setStatus("current")
_XstInstanceCfgPathCostMethod_Type = StaPathCostMode
_XstInstanceCfgPathCostMethod_Object = MibTableColumn
xstInstanceCfgPathCostMethod = _XstInstanceCfgPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 4, 1, 16),
    _XstInstanceCfgPathCostMethod_Type()
)
xstInstanceCfgPathCostMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgPathCostMethod.setStatus("current")
_XstInstancePortTable_Object = MibTable
xstInstancePortTable = _XstInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    xstInstancePortTable.setStatus("current")
_XstInstancePortEntry_Object = MibTableRow
xstInstancePortEntry = _XstInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1)
)
xstInstancePortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "xstInstancePortInstance"),
    (0, "ES3552M-AND-PoE-MIB", "xstInstancePortPort"),
)
if mibBuilder.loadTexts:
    xstInstancePortEntry.setStatus("current")
_XstInstancePortInstance_Type = Integer32
_XstInstancePortInstance_Object = MibTableColumn
xstInstancePortInstance = _XstInstancePortInstance_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 1),
    _XstInstancePortInstance_Type()
)
xstInstancePortInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xstInstancePortInstance.setStatus("current")
_XstInstancePortPort_Type = Integer32
_XstInstancePortPort_Object = MibTableColumn
xstInstancePortPort = _XstInstancePortPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 2),
    _XstInstancePortPort_Type()
)
xstInstancePortPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    xstInstancePortPort.setStatus("current")


class _XstInstancePortPriority_Type(Integer32):
    """Custom type xstInstancePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_XstInstancePortPriority_Type.__name__ = "Integer32"
_XstInstancePortPriority_Object = MibTableColumn
xstInstancePortPriority = _XstInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 3),
    _XstInstancePortPriority_Type()
)
xstInstancePortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortPriority.setStatus("current")


class _XstInstancePortState_Type(Integer32):
    """Custom type xstInstancePortState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("discarding", 1),
          ("learning", 2),
          ("forwarding", 3))
    )


_XstInstancePortState_Type.__name__ = "Integer32"
_XstInstancePortState_Object = MibTableColumn
xstInstancePortState = _XstInstancePortState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 4),
    _XstInstancePortState_Type()
)
xstInstancePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortState.setStatus("current")
_XstInstancePortEnable_Type = EnabledStatus
_XstInstancePortEnable_Object = MibTableColumn
xstInstancePortEnable = _XstInstancePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 5),
    _XstInstancePortEnable_Type()
)
xstInstancePortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortEnable.setStatus("current")


class _XstInstancePortPathCost_Type(Integer32):
    """Custom type xstInstancePortPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_XstInstancePortPathCost_Type.__name__ = "Integer32"
_XstInstancePortPathCost_Object = MibTableColumn
xstInstancePortPathCost = _XstInstancePortPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 6),
    _XstInstancePortPathCost_Type()
)
xstInstancePortPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortPathCost.setStatus("current")
_XstInstancePortDesignatedRoot_Type = BridgeId
_XstInstancePortDesignatedRoot_Object = MibTableColumn
xstInstancePortDesignatedRoot = _XstInstancePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 7),
    _XstInstancePortDesignatedRoot_Type()
)
xstInstancePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedRoot.setStatus("current")
_XstInstancePortDesignatedCost_Type = Integer32
_XstInstancePortDesignatedCost_Object = MibTableColumn
xstInstancePortDesignatedCost = _XstInstancePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 8),
    _XstInstancePortDesignatedCost_Type()
)
xstInstancePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedCost.setStatus("current")
_XstInstancePortDesignatedBridge_Type = BridgeId
_XstInstancePortDesignatedBridge_Object = MibTableColumn
xstInstancePortDesignatedBridge = _XstInstancePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 9),
    _XstInstancePortDesignatedBridge_Type()
)
xstInstancePortDesignatedBridge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedBridge.setStatus("current")


class _XstInstancePortDesignatedPort_Type(OctetString):
    """Custom type xstInstancePortDesignatedPort based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_XstInstancePortDesignatedPort_Type.__name__ = "OctetString"
_XstInstancePortDesignatedPort_Object = MibTableColumn
xstInstancePortDesignatedPort = _XstInstancePortDesignatedPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 10),
    _XstInstancePortDesignatedPort_Type()
)
xstInstancePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedPort.setStatus("current")
_XstInstancePortForwardTransitions_Type = Counter32
_XstInstancePortForwardTransitions_Object = MibTableColumn
xstInstancePortForwardTransitions = _XstInstancePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 11),
    _XstInstancePortForwardTransitions_Type()
)
xstInstancePortForwardTransitions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortForwardTransitions.setStatus("current")


class _XstInstancePortPortRole_Type(Integer32):
    """Custom type xstInstancePortPortRole based on Integer32"""
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
        *(("disabled", 1),
          ("root", 2),
          ("designated", 3),
          ("alternate", 4),
          ("backup", 5),
          ("master", 6))
    )


_XstInstancePortPortRole_Type.__name__ = "Integer32"
_XstInstancePortPortRole_Object = MibTableColumn
xstInstancePortPortRole = _XstInstancePortPortRole_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 12),
    _XstInstancePortPortRole_Type()
)
xstInstancePortPortRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortPortRole.setStatus("current")


class _XstInstancePortAdminPathCost_Type(Integer32):
    """Custom type xstInstancePortAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_XstInstancePortAdminPathCost_Type.__name__ = "Integer32"
_XstInstancePortAdminPathCost_Object = MibTableColumn
xstInstancePortAdminPathCost = _XstInstancePortAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 13),
    _XstInstancePortAdminPathCost_Type()
)
xstInstancePortAdminPathCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstancePortAdminPathCost.setStatus("current")


class _XstInstancePortOperPathCost_Type(Integer32):
    """Custom type xstInstancePortOperPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_XstInstancePortOperPathCost_Type.__name__ = "Integer32"
_XstInstancePortOperPathCost_Object = MibTableColumn
xstInstancePortOperPathCost = _XstInstancePortOperPathCost_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 5, 1, 14),
    _XstInstancePortOperPathCost_Type()
)
xstInstancePortOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortOperPathCost.setStatus("current")
_MstInstanceEditTable_Object = MibTable
mstInstanceEditTable = _MstInstanceEditTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 6)
)
if mibBuilder.loadTexts:
    mstInstanceEditTable.setStatus("current")
_MstInstanceEditEntry_Object = MibTableRow
mstInstanceEditEntry = _MstInstanceEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 6, 1)
)
mstInstanceEditEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mstInstanceEditIndex"),
)
if mibBuilder.loadTexts:
    mstInstanceEditEntry.setStatus("current")


class _MstInstanceEditIndex_Type(Integer32):
    """Custom type mstInstanceEditIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MstInstanceEditIndex_Type.__name__ = "Integer32"
_MstInstanceEditIndex_Object = MibTableColumn
mstInstanceEditIndex = _MstInstanceEditIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 6, 1, 1),
    _MstInstanceEditIndex_Type()
)
mstInstanceEditIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstInstanceEditIndex.setStatus("current")


class _MstInstanceEditVlansMap_Type(OctetString):
    """Custom type mstInstanceEditVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap_Object = MibTableColumn
mstInstanceEditVlansMap = _MstInstanceEditVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 6, 1, 2),
    _MstInstanceEditVlansMap_Type()
)
mstInstanceEditVlansMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap.setStatus("current")


class _MstInstanceEditVlansMap2k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap2k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap2k_Object = MibTableColumn
mstInstanceEditVlansMap2k = _MstInstanceEditVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 6, 1, 3),
    _MstInstanceEditVlansMap2k_Type()
)
mstInstanceEditVlansMap2k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap2k.setStatus("current")


class _MstInstanceEditVlansMap3k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap3k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap3k_Object = MibTableColumn
mstInstanceEditVlansMap3k = _MstInstanceEditVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 6, 1, 4),
    _MstInstanceEditVlansMap3k_Type()
)
mstInstanceEditVlansMap3k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap3k.setStatus("current")


class _MstInstanceEditVlansMap4k_Type(OctetString):
    """Custom type mstInstanceEditVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceEditVlansMap4k_Type.__name__ = "OctetString"
_MstInstanceEditVlansMap4k_Object = MibTableColumn
mstInstanceEditVlansMap4k = _MstInstanceEditVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 6, 1, 5),
    _MstInstanceEditVlansMap4k_Type()
)
mstInstanceEditVlansMap4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap4k.setStatus("current")
_MstInstanceEditRemainingHops_Type = Integer32
_MstInstanceEditRemainingHops_Object = MibTableColumn
mstInstanceEditRemainingHops = _MstInstanceEditRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 6, 1, 6),
    _MstInstanceEditRemainingHops_Type()
)
mstInstanceEditRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceEditRemainingHops.setStatus("current")
_MstInstanceOperTable_Object = MibTable
mstInstanceOperTable = _MstInstanceOperTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 7)
)
if mibBuilder.loadTexts:
    mstInstanceOperTable.setStatus("current")
_MstInstanceOperEntry_Object = MibTableRow
mstInstanceOperEntry = _MstInstanceOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 7, 1)
)
mstInstanceOperEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mstInstanceOperIndex"),
)
if mibBuilder.loadTexts:
    mstInstanceOperEntry.setStatus("current")


class _MstInstanceOperIndex_Type(Integer32):
    """Custom type mstInstanceOperIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MstInstanceOperIndex_Type.__name__ = "Integer32"
_MstInstanceOperIndex_Object = MibTableColumn
mstInstanceOperIndex = _MstInstanceOperIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 7, 1, 1),
    _MstInstanceOperIndex_Type()
)
mstInstanceOperIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mstInstanceOperIndex.setStatus("current")


class _MstInstanceOperVlansMap_Type(OctetString):
    """Custom type mstInstanceOperVlansMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap_Object = MibTableColumn
mstInstanceOperVlansMap = _MstInstanceOperVlansMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 7, 1, 2),
    _MstInstanceOperVlansMap_Type()
)
mstInstanceOperVlansMap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap.setStatus("current")


class _MstInstanceOperVlansMap2k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap2k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap2k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap2k_Object = MibTableColumn
mstInstanceOperVlansMap2k = _MstInstanceOperVlansMap2k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 7, 1, 3),
    _MstInstanceOperVlansMap2k_Type()
)
mstInstanceOperVlansMap2k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap2k.setStatus("current")


class _MstInstanceOperVlansMap3k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap3k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap3k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap3k_Object = MibTableColumn
mstInstanceOperVlansMap3k = _MstInstanceOperVlansMap3k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 7, 1, 4),
    _MstInstanceOperVlansMap3k_Type()
)
mstInstanceOperVlansMap3k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap3k.setStatus("current")


class _MstInstanceOperVlansMap4k_Type(OctetString):
    """Custom type mstInstanceOperVlansMap4k based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_MstInstanceOperVlansMap4k_Type.__name__ = "OctetString"
_MstInstanceOperVlansMap4k_Object = MibTableColumn
mstInstanceOperVlansMap4k = _MstInstanceOperVlansMap4k_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 6, 7, 1, 5),
    _MstInstanceOperVlansMap4k_Type()
)
mstInstanceOperVlansMap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap4k.setStatus("current")
_StaLoopbackDetectionPortTable_Object = MibTable
staLoopbackDetectionPortTable = _StaLoopbackDetectionPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 7)
)
if mibBuilder.loadTexts:
    staLoopbackDetectionPortTable.setStatus("current")
_StaLoopbackDetectionPortEntry_Object = MibTableRow
staLoopbackDetectionPortEntry = _StaLoopbackDetectionPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 7, 1)
)
staLoopbackDetectionPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "staLoopbackDetectionPortIfIndex"),
)
if mibBuilder.loadTexts:
    staLoopbackDetectionPortEntry.setStatus("current")
_StaLoopbackDetectionPortIfIndex_Type = InterfaceIndex
_StaLoopbackDetectionPortIfIndex_Object = MibTableColumn
staLoopbackDetectionPortIfIndex = _StaLoopbackDetectionPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 7, 1, 1),
    _StaLoopbackDetectionPortIfIndex_Type()
)
staLoopbackDetectionPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortIfIndex.setStatus("current")
_StaLoopbackDetectionPortStatus_Type = EnabledStatus
_StaLoopbackDetectionPortStatus_Object = MibTableColumn
staLoopbackDetectionPortStatus = _StaLoopbackDetectionPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 7, 1, 2),
    _StaLoopbackDetectionPortStatus_Type()
)
staLoopbackDetectionPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortStatus.setStatus("current")
_StaLoopbackDetectionPortTrapStatus_Type = EnabledStatus
_StaLoopbackDetectionPortTrapStatus_Object = MibTableColumn
staLoopbackDetectionPortTrapStatus = _StaLoopbackDetectionPortTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 7, 1, 3),
    _StaLoopbackDetectionPortTrapStatus_Type()
)
staLoopbackDetectionPortTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortTrapStatus.setStatus("current")


class _StaLoopbackDetectionPortReleaseMode_Type(Integer32):
    """Custom type staLoopbackDetectionPortReleaseMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2))
    )


_StaLoopbackDetectionPortReleaseMode_Type.__name__ = "Integer32"
_StaLoopbackDetectionPortReleaseMode_Object = MibTableColumn
staLoopbackDetectionPortReleaseMode = _StaLoopbackDetectionPortReleaseMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 7, 1, 4),
    _StaLoopbackDetectionPortReleaseMode_Type()
)
staLoopbackDetectionPortReleaseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortReleaseMode.setStatus("current")


class _StaLoopbackDetectionPortRelease_Type(Integer32):
    """Custom type staLoopbackDetectionPortRelease based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noRelease", 1),
          ("release", 2))
    )


_StaLoopbackDetectionPortRelease_Type.__name__ = "Integer32"
_StaLoopbackDetectionPortRelease_Object = MibTableColumn
staLoopbackDetectionPortRelease = _StaLoopbackDetectionPortRelease_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 5, 7, 1, 5),
    _StaLoopbackDetectionPortRelease_Type()
)
staLoopbackDetectionPortRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staLoopbackDetectionPortRelease.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 7)
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 7, 3),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_MirrorMgt_ObjectIdentity = ObjectIdentity
mirrorMgt = _MirrorMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8)
)
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 1, 1)
)
mirrorEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mirrorDestinationPort"),
    (0, "ES3552M-AND-PoE-MIB", "mirrorSourcePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")
_MirrorDestinationPort_Type = Integer32
_MirrorDestinationPort_Object = MibTableColumn
mirrorDestinationPort = _MirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 1, 1, 1),
    _MirrorDestinationPort_Type()
)
mirrorDestinationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mirrorDestinationPort.setStatus("current")
_MirrorSourcePort_Type = Integer32
_MirrorSourcePort_Object = MibTableColumn
mirrorSourcePort = _MirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 1, 1, 3),
    _MirrorType_Type()
)
mirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorType.setStatus("current")
_MirrorStatus_Type = ValidStatus
_MirrorStatus_Object = MibTableColumn
mirrorStatus = _MirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 1, 1, 4),
    _MirrorStatus_Type()
)
mirrorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorStatus.setStatus("current")
_VlanMirrorTable_Object = MibTable
vlanMirrorTable = _VlanMirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 2)
)
if mibBuilder.loadTexts:
    vlanMirrorTable.setStatus("current")
_VlanMirrorEntry_Object = MibTableRow
vlanMirrorEntry = _VlanMirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 2, 1)
)
vlanMirrorEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "vlanMirrorDestinationPort"),
    (0, "ES3552M-AND-PoE-MIB", "vlanMirrorSourceVlan"),
)
if mibBuilder.loadTexts:
    vlanMirrorEntry.setStatus("current")
_VlanMirrorDestinationPort_Type = Integer32
_VlanMirrorDestinationPort_Object = MibTableColumn
vlanMirrorDestinationPort = _VlanMirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 2, 1, 1),
    _VlanMirrorDestinationPort_Type()
)
vlanMirrorDestinationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanMirrorDestinationPort.setStatus("current")
_VlanMirrorSourceVlan_Type = Integer32
_VlanMirrorSourceVlan_Object = MibTableColumn
vlanMirrorSourceVlan = _VlanMirrorSourceVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 2, 1, 2),
    _VlanMirrorSourceVlan_Type()
)
vlanMirrorSourceVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanMirrorSourceVlan.setStatus("current")
_VlanMirrorStatus_Type = ValidStatus
_VlanMirrorStatus_Object = MibTableColumn
vlanMirrorStatus = _VlanMirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 8, 2, 1, 4),
    _VlanMirrorStatus_Type()
)
vlanMirrorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanMirrorStatus.setStatus("current")
_IgmpSnoopMgt_ObjectIdentity = ObjectIdentity
igmpSnoopMgt = _IgmpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9)
)


class _IgmpSnoopStatus_Type(EnabledStatus):
    """Custom type igmpSnoopStatus based on EnabledStatus"""
    defaultValue = 1


_IgmpSnoopStatus_Type.__name__ = "EnabledStatus"
_IgmpSnoopStatus_Object = MibScalar
igmpSnoopStatus = _IgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 6),
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
        ValueRangeConstraint(1, 3),
    )


_IgmpSnoopVersion_Type.__name__ = "Integer32"
_IgmpSnoopVersion_Object = MibScalar
igmpSnoopVersion = _IgmpSnoopVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 7),
    _IgmpSnoopVersion_Type()
)
igmpSnoopVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopVersion.setStatus("current")
_IgmpSnoopRouterCurrentTable_Object = MibTable
igmpSnoopRouterCurrentTable = _IgmpSnoopRouterCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 8)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentTable.setStatus("current")
_IgmpSnoopRouterCurrentEntry_Object = MibTableRow
igmpSnoopRouterCurrentEntry = _IgmpSnoopRouterCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 8, 1)
)
igmpSnoopRouterCurrentEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopRouterCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentEntry.setStatus("current")
_IgmpSnoopRouterCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object = MibTableColumn
igmpSnoopRouterCurrentVlanIndex = _IgmpSnoopRouterCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 8, 1, 1),
    _IgmpSnoopRouterCurrentVlanIndex_Type()
)
igmpSnoopRouterCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentVlanIndex.setStatus("current")
_IgmpSnoopRouterCurrentPorts_Type = PortList
_IgmpSnoopRouterCurrentPorts_Object = MibTableColumn
igmpSnoopRouterCurrentPorts = _IgmpSnoopRouterCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 8, 1, 2),
    _IgmpSnoopRouterCurrentPorts_Type()
)
igmpSnoopRouterCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentPorts.setStatus("current")
_IgmpSnoopRouterCurrentStatus_Type = PortList
_IgmpSnoopRouterCurrentStatus_Object = MibTableColumn
igmpSnoopRouterCurrentStatus = _IgmpSnoopRouterCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 8, 1, 3),
    _IgmpSnoopRouterCurrentStatus_Type()
)
igmpSnoopRouterCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentStatus.setStatus("current")
_IgmpSnoopRouterStaticTable_Object = MibTable
igmpSnoopRouterStaticTable = _IgmpSnoopRouterStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 9)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticTable.setStatus("current")
_IgmpSnoopRouterStaticEntry_Object = MibTableRow
igmpSnoopRouterStaticEntry = _IgmpSnoopRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 9, 1)
)
igmpSnoopRouterStaticEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopRouterStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticEntry.setStatus("current")
_IgmpSnoopRouterStaticVlanIndex_Type = Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object = MibTableColumn
igmpSnoopRouterStaticVlanIndex = _IgmpSnoopRouterStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 9, 1, 1),
    _IgmpSnoopRouterStaticVlanIndex_Type()
)
igmpSnoopRouterStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticVlanIndex.setStatus("current")
_IgmpSnoopRouterStaticPorts_Type = PortList
_IgmpSnoopRouterStaticPorts_Object = MibTableColumn
igmpSnoopRouterStaticPorts = _IgmpSnoopRouterStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 9, 1, 2),
    _IgmpSnoopRouterStaticPorts_Type()
)
igmpSnoopRouterStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticPorts.setStatus("current")
_IgmpSnoopRouterStaticStatus_Type = ValidStatus
_IgmpSnoopRouterStaticStatus_Object = MibTableColumn
igmpSnoopRouterStaticStatus = _IgmpSnoopRouterStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 9, 1, 3),
    _IgmpSnoopRouterStaticStatus_Type()
)
igmpSnoopRouterStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticStatus.setStatus("current")
_IgmpSnoopMulticastCurrentTable_Object = MibTable
igmpSnoopMulticastCurrentTable = _IgmpSnoopMulticastCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 10)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentTable.setStatus("current")
_IgmpSnoopMulticastCurrentEntry_Object = MibTableRow
igmpSnoopMulticastCurrentEntry = _IgmpSnoopMulticastCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 10, 1)
)
igmpSnoopMulticastCurrentEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopMulticastCurrentVlanIndex"),
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopMulticastCurrentIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentEntry.setStatus("current")
_IgmpSnoopMulticastCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastCurrentVlanIndex_Object = MibTableColumn
igmpSnoopMulticastCurrentVlanIndex = _IgmpSnoopMulticastCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 10, 1, 1),
    _IgmpSnoopMulticastCurrentVlanIndex_Type()
)
igmpSnoopMulticastCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentVlanIndex.setStatus("current")
_IgmpSnoopMulticastCurrentIpAddress_Type = IpAddress
_IgmpSnoopMulticastCurrentIpAddress_Object = MibTableColumn
igmpSnoopMulticastCurrentIpAddress = _IgmpSnoopMulticastCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 10, 1, 2),
    _IgmpSnoopMulticastCurrentIpAddress_Type()
)
igmpSnoopMulticastCurrentIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentIpAddress.setStatus("current")
_IgmpSnoopMulticastCurrentPorts_Type = PortList
_IgmpSnoopMulticastCurrentPorts_Object = MibTableColumn
igmpSnoopMulticastCurrentPorts = _IgmpSnoopMulticastCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 10, 1, 3),
    _IgmpSnoopMulticastCurrentPorts_Type()
)
igmpSnoopMulticastCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentPorts.setStatus("current")
_IgmpSnoopMulticastCurrentStatus_Type = PortList
_IgmpSnoopMulticastCurrentStatus_Object = MibTableColumn
igmpSnoopMulticastCurrentStatus = _IgmpSnoopMulticastCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 10, 1, 4),
    _IgmpSnoopMulticastCurrentStatus_Type()
)
igmpSnoopMulticastCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentStatus.setStatus("current")
_IgmpSnoopMulticastStaticTable_Object = MibTable
igmpSnoopMulticastStaticTable = _IgmpSnoopMulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 11)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticTable.setStatus("current")
_IgmpSnoopMulticastStaticEntry_Object = MibTableRow
igmpSnoopMulticastStaticEntry = _IgmpSnoopMulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 11, 1)
)
igmpSnoopMulticastStaticEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopMulticastStaticVlanIndex"),
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopMulticastStaticIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticEntry.setStatus("current")
_IgmpSnoopMulticastStaticVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object = MibTableColumn
igmpSnoopMulticastStaticVlanIndex = _IgmpSnoopMulticastStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 11, 1, 1),
    _IgmpSnoopMulticastStaticVlanIndex_Type()
)
igmpSnoopMulticastStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticVlanIndex.setStatus("current")
_IgmpSnoopMulticastStaticIpAddress_Type = IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object = MibTableColumn
igmpSnoopMulticastStaticIpAddress = _IgmpSnoopMulticastStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 11, 1, 2),
    _IgmpSnoopMulticastStaticIpAddress_Type()
)
igmpSnoopMulticastStaticIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticIpAddress.setStatus("current")
_IgmpSnoopMulticastStaticPorts_Type = PortList
_IgmpSnoopMulticastStaticPorts_Object = MibTableColumn
igmpSnoopMulticastStaticPorts = _IgmpSnoopMulticastStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 11, 1, 3),
    _IgmpSnoopMulticastStaticPorts_Type()
)
igmpSnoopMulticastStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticPorts.setStatus("current")
_IgmpSnoopMulticastStaticStatus_Type = ValidStatus
_IgmpSnoopMulticastStaticStatus_Object = MibTableColumn
igmpSnoopMulticastStaticStatus = _IgmpSnoopMulticastStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 11, 1, 4),
    _IgmpSnoopMulticastStaticStatus_Type()
)
igmpSnoopMulticastStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticStatus.setStatus("current")
_IgmpSnoopCurrentVlanTable_Object = MibTable
igmpSnoopCurrentVlanTable = _IgmpSnoopCurrentVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 14)
)
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanTable.setStatus("current")
_IgmpSnoopCurrentVlanEntry_Object = MibTableRow
igmpSnoopCurrentVlanEntry = _IgmpSnoopCurrentVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 14, 1)
)
igmpSnoopCurrentVlanEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanEntry.setStatus("current")
_IgmpSnoopCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopCurrentVlanIndex_Object = MibTableColumn
igmpSnoopCurrentVlanIndex = _IgmpSnoopCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 14, 1, 1),
    _IgmpSnoopCurrentVlanIndex_Type()
)
igmpSnoopCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanIndex.setStatus("current")
_IgmpSnoopCurrentVlanImmediateLeave_Type = EnabledStatus
_IgmpSnoopCurrentVlanImmediateLeave_Object = MibTableColumn
igmpSnoopCurrentVlanImmediateLeave = _IgmpSnoopCurrentVlanImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 14, 1, 3),
    _IgmpSnoopCurrentVlanImmediateLeave_Type()
)
igmpSnoopCurrentVlanImmediateLeave.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopCurrentVlanImmediateLeave.setStatus("current")
_IgmpSnoopLeaveProxy_Type = EnabledStatus
_IgmpSnoopLeaveProxy_Object = MibScalar
igmpSnoopLeaveProxy = _IgmpSnoopLeaveProxy_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 15),
    _IgmpSnoopLeaveProxy_Type()
)
igmpSnoopLeaveProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopLeaveProxy.setStatus("current")
_IgmpSnoopFilterStatus_Type = EnabledStatus
_IgmpSnoopFilterStatus_Object = MibScalar
igmpSnoopFilterStatus = _IgmpSnoopFilterStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 17),
    _IgmpSnoopFilterStatus_Type()
)
igmpSnoopFilterStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopFilterStatus.setStatus("current")
_IgmpSnoopProfileTable_Object = MibTable
igmpSnoopProfileTable = _IgmpSnoopProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 18)
)
if mibBuilder.loadTexts:
    igmpSnoopProfileTable.setStatus("current")
_IgmpSnoopProfileEntry_Object = MibTableRow
igmpSnoopProfileEntry = _IgmpSnoopProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 18, 1)
)
igmpSnoopProfileEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopProfileId"),
)
if mibBuilder.loadTexts:
    igmpSnoopProfileEntry.setStatus("current")
_IgmpSnoopProfileId_Type = Unsigned32
_IgmpSnoopProfileId_Object = MibTableColumn
igmpSnoopProfileId = _IgmpSnoopProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 18, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 18, 1, 2),
    _IgmpSnoopProfileAction_Type()
)
igmpSnoopProfileAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileAction.setStatus("current")
_IgmpSnoopProfileStatus_Type = ValidStatus
_IgmpSnoopProfileStatus_Object = MibTableColumn
igmpSnoopProfileStatus = _IgmpSnoopProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 18, 1, 3),
    _IgmpSnoopProfileStatus_Type()
)
igmpSnoopProfileStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileStatus.setStatus("current")
_IgmpSnoopProfileCtl_ObjectIdentity = ObjectIdentity
igmpSnoopProfileCtl = _IgmpSnoopProfileCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 19)
)
_IgmpSnoopProfileCtlId_Type = Unsigned32
_IgmpSnoopProfileCtlId_Object = MibScalar
igmpSnoopProfileCtlId = _IgmpSnoopProfileCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 19, 1),
    _IgmpSnoopProfileCtlId_Type()
)
igmpSnoopProfileCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlId.setStatus("current")
_IgmpSnoopProfileCtlInetAddressType_Type = InetAddressType
_IgmpSnoopProfileCtlInetAddressType_Object = MibScalar
igmpSnoopProfileCtlInetAddressType = _IgmpSnoopProfileCtlInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 19, 2),
    _IgmpSnoopProfileCtlInetAddressType_Type()
)
igmpSnoopProfileCtlInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlInetAddressType.setStatus("current")
_IgmpSnoopProfileCtlStartInetAddress_Type = InetAddress
_IgmpSnoopProfileCtlStartInetAddress_Object = MibScalar
igmpSnoopProfileCtlStartInetAddress = _IgmpSnoopProfileCtlStartInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 19, 3),
    _IgmpSnoopProfileCtlStartInetAddress_Type()
)
igmpSnoopProfileCtlStartInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlStartInetAddress.setStatus("current")
_IgmpSnoopProfileCtlEndInetAddress_Type = InetAddress
_IgmpSnoopProfileCtlEndInetAddress_Object = MibScalar
igmpSnoopProfileCtlEndInetAddress = _IgmpSnoopProfileCtlEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 19, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 19, 5),
    _IgmpSnoopProfileCtlAction_Type()
)
igmpSnoopProfileCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopProfileCtlAction.setStatus("current")
_IgmpSnoopProfileRangeTable_Object = MibTable
igmpSnoopProfileRangeTable = _IgmpSnoopProfileRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 20)
)
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeTable.setStatus("current")
_IgmpSnoopProfileRangeEntry_Object = MibTableRow
igmpSnoopProfileRangeEntry = _IgmpSnoopProfileRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 20, 1)
)
igmpSnoopProfileRangeEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopProfileRangeProfileId"),
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopProfileRangeInetAddressType"),
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopProfileRangeStartInetAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeEntry.setStatus("current")
_IgmpSnoopProfileRangeProfileId_Type = Unsigned32
_IgmpSnoopProfileRangeProfileId_Object = MibTableColumn
igmpSnoopProfileRangeProfileId = _IgmpSnoopProfileRangeProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 20, 1, 1),
    _IgmpSnoopProfileRangeProfileId_Type()
)
igmpSnoopProfileRangeProfileId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeProfileId.setStatus("current")
_IgmpSnoopProfileRangeInetAddressType_Type = InetAddressType
_IgmpSnoopProfileRangeInetAddressType_Object = MibTableColumn
igmpSnoopProfileRangeInetAddressType = _IgmpSnoopProfileRangeInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 20, 1, 2),
    _IgmpSnoopProfileRangeInetAddressType_Type()
)
igmpSnoopProfileRangeInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeInetAddressType.setStatus("current")
_IgmpSnoopProfileRangeStartInetAddress_Type = InetAddress
_IgmpSnoopProfileRangeStartInetAddress_Object = MibTableColumn
igmpSnoopProfileRangeStartInetAddress = _IgmpSnoopProfileRangeStartInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 20, 1, 3),
    _IgmpSnoopProfileRangeStartInetAddress_Type()
)
igmpSnoopProfileRangeStartInetAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeStartInetAddress.setStatus("current")
_IgmpSnoopProfileRangeEndInetAddress_Type = InetAddress
_IgmpSnoopProfileRangeEndInetAddress_Object = MibTableColumn
igmpSnoopProfileRangeEndInetAddress = _IgmpSnoopProfileRangeEndInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 20, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 20, 1, 5),
    _IgmpSnoopProfileRangeAction_Type()
)
igmpSnoopProfileRangeAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopProfileRangeAction.setStatus("current")
_IgmpSnoopFilterPortTable_Object = MibTable
igmpSnoopFilterPortTable = _IgmpSnoopFilterPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 21)
)
if mibBuilder.loadTexts:
    igmpSnoopFilterPortTable.setStatus("current")
_IgmpSnoopFilterPortEntry_Object = MibTableRow
igmpSnoopFilterPortEntry = _IgmpSnoopFilterPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 21, 1)
)
igmpSnoopFilterPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopFilterPortIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopFilterPortEntry.setStatus("current")
_IgmpSnoopFilterPortIndex_Type = Unsigned32
_IgmpSnoopFilterPortIndex_Object = MibTableColumn
igmpSnoopFilterPortIndex = _IgmpSnoopFilterPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 21, 1, 1),
    _IgmpSnoopFilterPortIndex_Type()
)
igmpSnoopFilterPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopFilterPortIndex.setStatus("current")
_IgmpSnoopFilterPortProfileId_Type = Integer32
_IgmpSnoopFilterPortProfileId_Object = MibTableColumn
igmpSnoopFilterPortProfileId = _IgmpSnoopFilterPortProfileId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 21, 1, 2),
    _IgmpSnoopFilterPortProfileId_Type()
)
igmpSnoopFilterPortProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopFilterPortProfileId.setStatus("current")
_IgmpSnoopThrottlePortTable_Object = MibTable
igmpSnoopThrottlePortTable = _IgmpSnoopThrottlePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 22)
)
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortTable.setStatus("current")
_IgmpSnoopThrottlePortEntry_Object = MibTableRow
igmpSnoopThrottlePortEntry = _IgmpSnoopThrottlePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 22, 1)
)
igmpSnoopThrottlePortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "igmpSnoopThrottlePortIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortEntry.setStatus("current")
_IgmpSnoopThrottlePortIndex_Type = Unsigned32
_IgmpSnoopThrottlePortIndex_Object = MibTableColumn
igmpSnoopThrottlePortIndex = _IgmpSnoopThrottlePortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 22, 1, 1),
    _IgmpSnoopThrottlePortIndex_Type()
)
igmpSnoopThrottlePortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortIndex.setStatus("current")
_IgmpSnoopThrottlePortRunningStatus_Type = TruthValue
_IgmpSnoopThrottlePortRunningStatus_Object = MibTableColumn
igmpSnoopThrottlePortRunningStatus = _IgmpSnoopThrottlePortRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 22, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 22, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 22, 1, 4),
    _IgmpSnoopThrottlePortMaxGroups_Type()
)
igmpSnoopThrottlePortMaxGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortMaxGroups.setStatus("current")
_IgmpSnoopThrottlePortCurrentGroups_Type = Integer32
_IgmpSnoopThrottlePortCurrentGroups_Object = MibTableColumn
igmpSnoopThrottlePortCurrentGroups = _IgmpSnoopThrottlePortCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 9, 22, 1, 5),
    _IgmpSnoopThrottlePortCurrentGroups_Type()
)
igmpSnoopThrottlePortCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopThrottlePortCurrentGroups.setStatus("current")
_IpMgt_ObjectIdentity = ObjectIdentity
ipMgt = _IpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10)
)
_NetConfigTable_Object = MibTable
netConfigTable = _NetConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 1)
)
if mibBuilder.loadTexts:
    netConfigTable.setStatus("current")
_NetConfigEntry_Object = MibTableRow
netConfigEntry = _NetConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 1, 1)
)
netConfigEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "netConfigIfIndex"),
    (0, "ES3552M-AND-PoE-MIB", "netConfigIPAddress"),
    (0, "ES3552M-AND-PoE-MIB", "netConfigSubnetMask"),
)
if mibBuilder.loadTexts:
    netConfigEntry.setStatus("current")
_NetConfigIfIndex_Type = Integer32
_NetConfigIfIndex_Object = MibTableColumn
netConfigIfIndex = _NetConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 1, 1, 1),
    _NetConfigIfIndex_Type()
)
netConfigIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigIfIndex.setStatus("current")
_NetConfigIPAddress_Type = IpAddress
_NetConfigIPAddress_Object = MibTableColumn
netConfigIPAddress = _NetConfigIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 1, 1, 2),
    _NetConfigIPAddress_Type()
)
netConfigIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netConfigIPAddress.setStatus("current")
_NetConfigSubnetMask_Type = IpAddress
_NetConfigSubnetMask_Object = MibTableColumn
netConfigSubnetMask = _NetConfigSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 1, 1, 5),
    _NetConfigUnnumbered_Type()
)
netConfigUnnumbered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netConfigUnnumbered.setStatus("current")
_NetConfigStatus_Type = RowStatus
_NetConfigStatus_Object = MibTableColumn
netConfigStatus = _NetConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 1, 1, 6),
    _NetConfigStatus_Type()
)
netConfigStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netConfigStatus.setStatus("current")
_NetDefaultGateway_Type = IpAddress
_NetDefaultGateway_Object = MibScalar
netDefaultGateway = _NetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 2),
    _NetDefaultGateway_Type()
)
netDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDefaultGateway.setStatus("current")
_IpHttpState_Type = EnabledStatus
_IpHttpState_Object = MibScalar
ipHttpState = _IpHttpState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 5),
    _IpDhcpRestart_Type()
)
ipDhcpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpRestart.setStatus("current")
_IpHttpsState_Type = EnabledStatus
_IpHttpsState_Object = MibScalar
ipHttpsState = _IpHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 6),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 7),
    _IpHttpsPort_Type()
)
ipHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsPort.setStatus("current")
_DhcpMgt_ObjectIdentity = ObjectIdentity
dhcpMgt = _DhcpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11)
)
_DhcpClient_ObjectIdentity = ObjectIdentity
dhcpClient = _DhcpClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11, 1)
)
_DhcpcOptions_ObjectIdentity = ObjectIdentity
dhcpcOptions = _DhcpcOptions_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11, 1, 1)
)
_DhcpcInterfaceTable_Object = MibTable
dhcpcInterfaceTable = _DhcpcInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11, 1, 1, 1)
)
if mibBuilder.loadTexts:
    dhcpcInterfaceTable.setStatus("current")
_DhcpcInterfaceEntry_Object = MibTableRow
dhcpcInterfaceEntry = _DhcpcInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11, 1, 1, 1, 1)
)
dhcpcInterfaceEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "dhcpcIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpcInterfaceEntry.setStatus("current")
_DhcpcIfIndex_Type = Integer32
_DhcpcIfIndex_Object = MibTableColumn
dhcpcIfIndex = _DhcpcIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11, 1, 1, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11, 1, 1, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11, 1, 1, 1, 1, 3),
    _DhcpcIfClientId_Type()
)
dhcpcIfClientId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpcIfClientId.setStatus("current")
_DhcpOption82_ObjectIdentity = ObjectIdentity
dhcpOption82 = _DhcpOption82_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11, 4)
)


class _DhcpOption82Status_Type(Integer32):
    """Custom type dhcpOption82Status based on Integer32"""
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


_DhcpOption82Status_Type.__name__ = "Integer32"
_DhcpOption82Status_Object = MibScalar
dhcpOption82Status = _DhcpOption82Status_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11, 4, 1),
    _DhcpOption82Status_Type()
)
dhcpOption82Status.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82Status.setStatus("current")


class _DhcpOption82Policy_Type(Integer32):
    """Custom type dhcpOption82Policy based on Integer32"""
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
          ("replace", 2),
          ("keep", 3))
    )


_DhcpOption82Policy_Type.__name__ = "Integer32"
_DhcpOption82Policy_Object = MibScalar
dhcpOption82Policy = _DhcpOption82Policy_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 11, 4, 2),
    _DhcpOption82Policy_Type()
)
dhcpOption82Policy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpOption82Policy.setStatus("current")


class _ArpCacheDeleteAll_Type(Integer32):
    """Custom type arpCacheDeleteAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("noDelete", 2))
    )


_ArpCacheDeleteAll_Type.__name__ = "Integer32"
_ArpCacheDeleteAll_Object = MibScalar
arpCacheDeleteAll = _ArpCacheDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 10, 17),
    _ArpCacheDeleteAll_Type()
)
arpCacheDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpCacheDeleteAll.setStatus("current")
_VlanMgt_ObjectIdentity = ObjectIdentity
vlanMgt = _VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanIndex_Type = Unsigned32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 1, 1, 2),
    _VlanAddressMethod_Type()
)
vlanAddressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAddressMethod.setStatus("current")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 2)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("current")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 2, 1)
)
vlanPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "vlanPortIndex"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("current")
_VlanPortIndex_Type = Integer32
_VlanPortIndex_Object = MibTableColumn
vlanPortIndex = _VlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 2, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 2, 1, 3),
    _VlanPortPrivateVlanType_Type()
)
vlanPortPrivateVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortPrivateVlanType.setStatus("current")
_ProtocolVlanTable_Object = MibTable
protocolVlanTable = _ProtocolVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 5)
)
if mibBuilder.loadTexts:
    protocolVlanTable.setStatus("current")
_ProtocolVlanEntry_Object = MibTableRow
protocolVlanEntry = _ProtocolVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 5, 1)
)
protocolVlanEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "protocolVlanGroupId"),
)
if mibBuilder.loadTexts:
    protocolVlanEntry.setStatus("current")
_ProtocolVlanGroupId_Type = Integer32
_ProtocolVlanGroupId_Object = MibTableColumn
protocolVlanGroupId = _ProtocolVlanGroupId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 5, 1, 1),
    _ProtocolVlanGroupId_Type()
)
protocolVlanGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    protocolVlanGroupId.setStatus("current")
_ProtocolVlanGroupVid_Type = Integer32
_ProtocolVlanGroupVid_Object = MibTableColumn
protocolVlanGroupVid = _ProtocolVlanGroupVid_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 5, 1, 2),
    _ProtocolVlanGroupVid_Type()
)
protocolVlanGroupVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    protocolVlanGroupVid.setStatus("current")
_VoiceVlanMgt_ObjectIdentity = ObjectIdentity
voiceVlanMgt = _VoiceVlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6)
)
_VoiceVlanOuiTable_Object = MibTable
voiceVlanOuiTable = _VoiceVlanOuiTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 1)
)
if mibBuilder.loadTexts:
    voiceVlanOuiTable.setStatus("current")
_VoiceVlanOuiEntry_Object = MibTableRow
voiceVlanOuiEntry = _VoiceVlanOuiEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 1, 1)
)
voiceVlanOuiEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "voiceVlanOuiAddress"),
)
if mibBuilder.loadTexts:
    voiceVlanOuiEntry.setStatus("current")
_VoiceVlanOuiAddress_Type = MacAddress
_VoiceVlanOuiAddress_Object = MibTableColumn
voiceVlanOuiAddress = _VoiceVlanOuiAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 1, 1, 1),
    _VoiceVlanOuiAddress_Type()
)
voiceVlanOuiAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    voiceVlanOuiAddress.setStatus("current")
_VoiceVlanOuiMask_Type = MacAddress
_VoiceVlanOuiMask_Object = MibTableColumn
voiceVlanOuiMask = _VoiceVlanOuiMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 1, 1, 2),
    _VoiceVlanOuiMask_Type()
)
voiceVlanOuiMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanOuiMask.setStatus("current")


class _VoiceVlanOuiDescription_Type(DisplayString):
    """Custom type voiceVlanOuiDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_VoiceVlanOuiDescription_Type.__name__ = "DisplayString"
_VoiceVlanOuiDescription_Object = MibTableColumn
voiceVlanOuiDescription = _VoiceVlanOuiDescription_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 1, 1, 3),
    _VoiceVlanOuiDescription_Type()
)
voiceVlanOuiDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanOuiDescription.setStatus("current")
_VoiceVlanOuiStatus_Type = ValidStatus
_VoiceVlanOuiStatus_Object = MibTableColumn
voiceVlanOuiStatus = _VoiceVlanOuiStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 1, 1, 4),
    _VoiceVlanOuiStatus_Type()
)
voiceVlanOuiStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    voiceVlanOuiStatus.setStatus("current")
_VoiceVlanEnabledId_Type = Integer32
_VoiceVlanEnabledId_Object = MibScalar
voiceVlanEnabledId = _VoiceVlanEnabledId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 2),
    _VoiceVlanEnabledId_Type()
)
voiceVlanEnabledId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanEnabledId.setStatus("current")


class _VoiceVlanAgingTime_Type(Integer32):
    """Custom type voiceVlanAgingTime based on Integer32"""
    defaultValue = 1440

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 43200),
    )


_VoiceVlanAgingTime_Type.__name__ = "Integer32"
_VoiceVlanAgingTime_Object = MibScalar
voiceVlanAgingTime = _VoiceVlanAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 3),
    _VoiceVlanAgingTime_Type()
)
voiceVlanAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanAgingTime.setStatus("current")
_VoiceVlanPortTable_Object = MibTable
voiceVlanPortTable = _VoiceVlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 7)
)
if mibBuilder.loadTexts:
    voiceVlanPortTable.setStatus("current")
_VoiceVlanPortEntry_Object = MibTableRow
voiceVlanPortEntry = _VoiceVlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 7, 1)
)
voiceVlanPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "voiceVlanPortIfIndex"),
)
if mibBuilder.loadTexts:
    voiceVlanPortEntry.setStatus("current")


class _VoiceVlanPortIfIndex_Type(Integer32):
    """Custom type voiceVlanPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_VoiceVlanPortIfIndex_Type.__name__ = "Integer32"
_VoiceVlanPortIfIndex_Object = MibTableColumn
voiceVlanPortIfIndex = _VoiceVlanPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 7, 1, 1),
    _VoiceVlanPortIfIndex_Type()
)
voiceVlanPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    voiceVlanPortIfIndex.setStatus("current")


class _VoiceVlanPortMode_Type(Integer32):
    """Custom type voiceVlanPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("manual", 2),
          ("none", 3))
    )


_VoiceVlanPortMode_Type.__name__ = "Integer32"
_VoiceVlanPortMode_Object = MibTableColumn
voiceVlanPortMode = _VoiceVlanPortMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 7, 1, 2),
    _VoiceVlanPortMode_Type()
)
voiceVlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortMode.setStatus("current")
_VoiceVlanPortSecurity_Type = EnabledStatus
_VoiceVlanPortSecurity_Object = MibTableColumn
voiceVlanPortSecurity = _VoiceVlanPortSecurity_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 7, 1, 3),
    _VoiceVlanPortSecurity_Type()
)
voiceVlanPortSecurity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortSecurity.setStatus("current")


class _VoiceVlanPortPriority_Type(Integer32):
    """Custom type voiceVlanPortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6),
    )


_VoiceVlanPortPriority_Type.__name__ = "Integer32"
_VoiceVlanPortPriority_Object = MibTableColumn
voiceVlanPortPriority = _VoiceVlanPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 7, 1, 4),
    _VoiceVlanPortPriority_Type()
)
voiceVlanPortPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortPriority.setStatus("current")
_VoiceVlanPortRuleOui_Type = EnabledStatus
_VoiceVlanPortRuleOui_Object = MibTableColumn
voiceVlanPortRuleOui = _VoiceVlanPortRuleOui_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 7, 1, 5),
    _VoiceVlanPortRuleOui_Type()
)
voiceVlanPortRuleOui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortRuleOui.setStatus("current")
_VoiceVlanPortRuleLldp_Type = EnabledStatus
_VoiceVlanPortRuleLldp_Object = MibTableColumn
voiceVlanPortRuleLldp = _VoiceVlanPortRuleLldp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 6, 7, 1, 6),
    _VoiceVlanPortRuleLldp_Type()
)
voiceVlanPortRuleLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    voiceVlanPortRuleLldp.setStatus("current")
_VlanDot1qTunnelGlobalConfig_ObjectIdentity = ObjectIdentity
vlanDot1qTunnelGlobalConfig = _VlanDot1qTunnelGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 7)
)
_VlanDot1qTunnelStatus_Type = EnabledStatus
_VlanDot1qTunnelStatus_Object = MibScalar
vlanDot1qTunnelStatus = _VlanDot1qTunnelStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 7, 1),
    _VlanDot1qTunnelStatus_Type()
)
vlanDot1qTunnelStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDot1qTunnelStatus.setStatus("current")
_VlanDot1qTunnelPortTable_Object = MibTable
vlanDot1qTunnelPortTable = _VlanDot1qTunnelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 8)
)
if mibBuilder.loadTexts:
    vlanDot1qTunnelPortTable.setStatus("current")
_VlanDot1qTunnelPortEntry_Object = MibTableRow
vlanDot1qTunnelPortEntry = _VlanDot1qTunnelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 8, 1)
)
vlanDot1qTunnelPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "vlanDot1qTunnelPortIndex"),
)
if mibBuilder.loadTexts:
    vlanDot1qTunnelPortEntry.setStatus("current")
_VlanDot1qTunnelPortIndex_Type = Integer32
_VlanDot1qTunnelPortIndex_Object = MibTableColumn
vlanDot1qTunnelPortIndex = _VlanDot1qTunnelPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 8, 1, 1),
    _VlanDot1qTunnelPortIndex_Type()
)
vlanDot1qTunnelPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanDot1qTunnelPortIndex.setStatus("current")


class _VlanDot1qTunnelPortMode_Type(Integer32):
    """Custom type vlanDot1qTunnelPortMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("dot1qTunnel", 2),
          ("dot1qTunnelUplink", 3))
    )


_VlanDot1qTunnelPortMode_Type.__name__ = "Integer32"
_VlanDot1qTunnelPortMode_Object = MibTableColumn
vlanDot1qTunnelPortMode = _VlanDot1qTunnelPortMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 8, 1, 2),
    _VlanDot1qTunnelPortMode_Type()
)
vlanDot1qTunnelPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDot1qTunnelPortMode.setStatus("current")


class _VlanDot1qTunnelPortEtherType_Type(Unsigned32):
    """Custom type vlanDot1qTunnelPortEtherType based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2048, 65535),
    )


_VlanDot1qTunnelPortEtherType_Type.__name__ = "Unsigned32"
_VlanDot1qTunnelPortEtherType_Object = MibTableColumn
vlanDot1qTunnelPortEtherType = _VlanDot1qTunnelPortEtherType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 8, 1, 3),
    _VlanDot1qTunnelPortEtherType_Type()
)
vlanDot1qTunnelPortEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanDot1qTunnelPortEtherType.setStatus("current")
_MacVlanTable_Object = MibTable
macVlanTable = _MacVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 11)
)
if mibBuilder.loadTexts:
    macVlanTable.setStatus("current")
_MacVlanEntry_Object = MibTableRow
macVlanEntry = _MacVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 11, 1)
)
macVlanEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "macVlanMacAddress"),
)
if mibBuilder.loadTexts:
    macVlanEntry.setStatus("current")
_MacVlanMacAddress_Type = MacAddress
_MacVlanMacAddress_Object = MibTableColumn
macVlanMacAddress = _MacVlanMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 11, 1, 1),
    _MacVlanMacAddress_Type()
)
macVlanMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macVlanMacAddress.setStatus("current")


class _MacVlanId_Type(Integer32):
    """Custom type macVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4092),
    )


_MacVlanId_Type.__name__ = "Integer32"
_MacVlanId_Object = MibTableColumn
macVlanId = _MacVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 11, 1, 2),
    _MacVlanId_Type()
)
macVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macVlanId.setStatus("current")
_MacVlanStatus_Type = ValidStatus
_MacVlanStatus_Object = MibTableColumn
macVlanStatus = _MacVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 11, 1, 4),
    _MacVlanStatus_Type()
)
macVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    macVlanStatus.setStatus("current")


class _MacVlanClearAction_Type(Integer32):
    """Custom type macVlanClearAction based on Integer32"""
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


_MacVlanClearAction_Type.__name__ = "Integer32"
_MacVlanClearAction_Object = MibScalar
macVlanClearAction = _MacVlanClearAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 12),
    _MacVlanClearAction_Type()
)
macVlanClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macVlanClearAction.setStatus("current")
_SubnetVlanTable_Object = MibTable
subnetVlanTable = _SubnetVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 13)
)
if mibBuilder.loadTexts:
    subnetVlanTable.setStatus("current")
_SubnetVlanEntry_Object = MibTableRow
subnetVlanEntry = _SubnetVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 13, 1)
)
subnetVlanEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "subnetVlanMask"),
    (0, "ES3552M-AND-PoE-MIB", "subnetVlanIpAddress"),
)
if mibBuilder.loadTexts:
    subnetVlanEntry.setStatus("current")
_SubnetVlanIpAddress_Type = IpAddress
_SubnetVlanIpAddress_Object = MibTableColumn
subnetVlanIpAddress = _SubnetVlanIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 13, 1, 1),
    _SubnetVlanIpAddress_Type()
)
subnetVlanIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetVlanIpAddress.setStatus("current")
_SubnetVlanMask_Type = IpAddress
_SubnetVlanMask_Object = MibTableColumn
subnetVlanMask = _SubnetVlanMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 13, 1, 2),
    _SubnetVlanMask_Type()
)
subnetVlanMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    subnetVlanMask.setStatus("current")


class _SubnetVlanId_Type(Integer32):
    """Custom type subnetVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_SubnetVlanId_Type.__name__ = "Integer32"
_SubnetVlanId_Object = MibTableColumn
subnetVlanId = _SubnetVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 13, 1, 3),
    _SubnetVlanId_Type()
)
subnetVlanId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subnetVlanId.setStatus("current")


class _SubnetVlanPriority_Type(Integer32):
    """Custom type subnetVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_SubnetVlanPriority_Type.__name__ = "Integer32"
_SubnetVlanPriority_Object = MibTableColumn
subnetVlanPriority = _SubnetVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 13, 1, 4),
    _SubnetVlanPriority_Type()
)
subnetVlanPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subnetVlanPriority.setStatus("current")
_SubnetVlanStatus_Type = ValidStatus
_SubnetVlanStatus_Object = MibTableColumn
subnetVlanStatus = _SubnetVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 13, 1, 5),
    _SubnetVlanStatus_Type()
)
subnetVlanStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    subnetVlanStatus.setStatus("current")


class _SubnetVlanClearAction_Type(Integer32):
    """Custom type subnetVlanClearAction based on Integer32"""
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


_SubnetVlanClearAction_Type.__name__ = "Integer32"
_SubnetVlanClearAction_Object = MibScalar
subnetVlanClearAction = _SubnetVlanClearAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 14),
    _SubnetVlanClearAction_Type()
)
subnetVlanClearAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subnetVlanClearAction.setStatus("current")
_VlanL2ProtocolTunnelPortTable_Object = MibTable
vlanL2ProtocolTunnelPortTable = _VlanL2ProtocolTunnelPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 16)
)
if mibBuilder.loadTexts:
    vlanL2ProtocolTunnelPortTable.setStatus("current")
_VlanL2ProtocolTunnelPortEntry_Object = MibTableRow
vlanL2ProtocolTunnelPortEntry = _VlanL2ProtocolTunnelPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 16, 1)
)
vlanL2ProtocolTunnelPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "vlanL2ptPortIndex"),
)
if mibBuilder.loadTexts:
    vlanL2ProtocolTunnelPortEntry.setStatus("current")
_VlanL2ptPortIndex_Type = Integer32
_VlanL2ptPortIndex_Object = MibTableColumn
vlanL2ptPortIndex = _VlanL2ptPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 16, 1, 1),
    _VlanL2ptPortIndex_Type()
)
vlanL2ptPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vlanL2ptPortIndex.setStatus("current")
_VlanL2ptPortSta_Type = EnabledStatus
_VlanL2ptPortSta_Object = MibTableColumn
vlanL2ptPortSta = _VlanL2ptPortSta_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 16, 1, 2),
    _VlanL2ptPortSta_Type()
)
vlanL2ptPortSta.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vlanL2ptPortSta.setStatus("current")
_VlanL2ptPortLldp_Type = EnabledStatus
_VlanL2ptPortLldp_Object = MibTableColumn
vlanL2ptPortLldp = _VlanL2ptPortLldp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 16, 1, 3),
    _VlanL2ptPortLldp_Type()
)
vlanL2ptPortLldp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanL2ptPortLldp.setStatus("current")
_VlanL2ptPortCdp_Type = EnabledStatus
_VlanL2ptPortCdp_Object = MibTableColumn
vlanL2ptPortCdp = _VlanL2ptPortCdp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 16, 1, 4),
    _VlanL2ptPortCdp_Type()
)
vlanL2ptPortCdp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanL2ptPortCdp.setStatus("current")
_VlanL2ptPortVtp_Type = EnabledStatus
_VlanL2ptPortVtp_Object = MibTableColumn
vlanL2ptPortVtp = _VlanL2ptPortVtp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 16, 1, 5),
    _VlanL2ptPortVtp_Type()
)
vlanL2ptPortVtp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanL2ptPortVtp.setStatus("current")
_VlanL2ptPortPvst_Type = EnabledStatus
_VlanL2ptPortPvst_Object = MibTableColumn
vlanL2ptPortPvst = _VlanL2ptPortPvst_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 16, 1, 6),
    _VlanL2ptPortPvst_Type()
)
vlanL2ptPortPvst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanL2ptPortPvst.setStatus("current")
_VlanL2ProtocolTunnelGlobalConfig_ObjectIdentity = ObjectIdentity
vlanL2ProtocolTunnelGlobalConfig = _VlanL2ProtocolTunnelGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 19)
)
_VlanL2ProtocolTunnelAddress_Type = MacAddress
_VlanL2ProtocolTunnelAddress_Object = MibScalar
vlanL2ProtocolTunnelAddress = _VlanL2ProtocolTunnelAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 12, 19, 1),
    _VlanL2ProtocolTunnelAddress_Type()
)
vlanL2ProtocolTunnelAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanL2ProtocolTunnelAddress.setStatus("current")
_PriorityMgt_ObjectIdentity = ObjectIdentity
priorityMgt = _PriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13)
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 1),
    _PrioIpPrecDscpStatus_Type()
)
prioIpPrecDscpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecDscpStatus.setStatus("current")
_PrioIpDscpTable_Object = MibTable
prioIpDscpTable = _PrioIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 4)
)
if mibBuilder.loadTexts:
    prioIpDscpTable.setStatus("current")
_PrioIpDscpEntry_Object = MibTableRow
prioIpDscpEntry = _PrioIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 4, 1)
)
prioIpDscpEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "prioIpDscpPort"),
    (0, "ES3552M-AND-PoE-MIB", "prioIpDscpValue"),
)
if mibBuilder.loadTexts:
    prioIpDscpEntry.setStatus("current")
_PrioIpDscpPort_Type = Integer32
_PrioIpDscpPort_Object = MibTableColumn
prioIpDscpPort = _PrioIpDscpPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 4, 1, 3),
    _PrioIpDscpCos_Type()
)
prioIpDscpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpCos.setStatus("current")
_PrioIpDscpRestoreDefault_Type = Integer32
_PrioIpDscpRestoreDefault_Object = MibScalar
prioIpDscpRestoreDefault = _PrioIpDscpRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 5),
    _PrioIpDscpRestoreDefault_Type()
)
prioIpDscpRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpRestoreDefault.setStatus("current")
_PrioCopy_ObjectIdentity = ObjectIdentity
prioCopy = _PrioCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 8)
)
_PrioCopyIpDscp_Type = OctetString
_PrioCopyIpDscp_Object = MibScalar
prioCopyIpDscp = _PrioCopyIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 8, 2),
    _PrioCopyIpDscp_Type()
)
prioCopyIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpDscp.setStatus("current")
_PrioWrrTable_Object = MibTable
prioWrrTable = _PrioWrrTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 9)
)
if mibBuilder.loadTexts:
    prioWrrTable.setStatus("current")
_PrioWrrEntry_Object = MibTableRow
prioWrrEntry = _PrioWrrEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 9, 1)
)
prioWrrEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "prioWrrTrafficClass"),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 9, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 9, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 13, 10),
    _PrioQueueMode_Type()
)
prioQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioQueueMode.setStatus("current")
_TrapDestMgt_ObjectIdentity = ObjectIdentity
trapDestMgt = _TrapDestMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 1)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("current")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 1, 1)
)
trapDestEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "trapDestAddress"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("current")
_TrapDestAddress_Type = IpAddress
_TrapDestAddress_Object = MibTableColumn
trapDestAddress = _TrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 1, 1, 2),
    _TrapDestCommunity_Type()
)
trapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestCommunity.setStatus("current")
_TrapDestStatus_Type = ValidStatus
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 1, 1, 5),
    _TrapDestUdpPort_Type()
)
trapDestUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestUdpPort.setStatus("current")
_TrapVar_ObjectIdentity = ObjectIdentity
trapVar = _TrapVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 2)
)


class _TrapIpFilterRejectMode_Type(Integer32):
    """Custom type trapIpFilterRejectMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("web", 1),
          ("snmp", 2),
          ("telnet", 3))
    )


_TrapIpFilterRejectMode_Type.__name__ = "Integer32"
_TrapIpFilterRejectMode_Object = MibScalar
trapIpFilterRejectMode = _TrapIpFilterRejectMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 2, 6),
    _TrapIpFilterRejectMode_Type()
)
trapIpFilterRejectMode.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIpFilterRejectMode.setStatus("current")
_TrapIpFilterRejectIp_Type = Integer32
_TrapIpFilterRejectIp_Object = MibScalar
trapIpFilterRejectIp = _TrapIpFilterRejectIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 2, 7),
    _TrapIpFilterRejectIp_Type()
)
trapIpFilterRejectIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIpFilterRejectIp.setStatus("current")


class _TrapAutoUpgradeResult_Type(Integer32):
    """Custom type trapAutoUpgradeResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("succeeded", 1),
          ("failed", 2))
    )


_TrapAutoUpgradeResult_Type.__name__ = "Integer32"
_TrapAutoUpgradeResult_Object = MibScalar
trapAutoUpgradeResult = _TrapAutoUpgradeResult_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 2, 18),
    _TrapAutoUpgradeResult_Type()
)
trapAutoUpgradeResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAutoUpgradeResult.setStatus("current")


class _TrapAutoUpgradeNewVer_Type(DisplayString):
    """Custom type trapAutoUpgradeNewVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_TrapAutoUpgradeNewVer_Type.__name__ = "DisplayString"
_TrapAutoUpgradeNewVer_Object = MibScalar
trapAutoUpgradeNewVer = _TrapAutoUpgradeNewVer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 2, 19),
    _TrapAutoUpgradeNewVer_Type()
)
trapAutoUpgradeNewVer.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapAutoUpgradeNewVer.setStatus("current")
_TrapDhcpClientPortIfIndex_Type = Integer32
_TrapDhcpClientPortIfIndex_Object = MibScalar
trapDhcpClientPortIfIndex = _TrapDhcpClientPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 2, 20),
    _TrapDhcpClientPortIfIndex_Type()
)
trapDhcpClientPortIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapDhcpClientPortIfIndex.setStatus("current")
_TrapDhcpServerIpAddress_Type = DisplayString
_TrapDhcpServerIpAddress_Object = MibScalar
trapDhcpServerIpAddress = _TrapDhcpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 2, 21),
    _TrapDhcpServerIpAddress_Type()
)
trapDhcpServerIpAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapDhcpServerIpAddress.setStatus("current")
_TrapPortSecurityIntrusionMac_Type = MacAddress
_TrapPortSecurityIntrusionMac_Object = MibScalar
trapPortSecurityIntrusionMac = _TrapPortSecurityIntrusionMac_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 2, 29),
    _TrapPortSecurityIntrusionMac_Type()
)
trapPortSecurityIntrusionMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapPortSecurityIntrusionMac.setStatus("current")
_TrapIfIndex_Type = Unsigned32
_TrapIfIndex_Object = MibScalar
trapIfIndex = _TrapIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 2, 30),
    _TrapIfIndex_Type()
)
trapIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapIfIndex.setStatus("current")
_TrapVlanId_Type = Unsigned32
_TrapVlanId_Object = MibScalar
trapVlanId = _TrapVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 14, 2, 31),
    _TrapVlanId_Type()
)
trapVlanId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    trapVlanId.setStatus("current")
_QosMgt_ObjectIdentity = ObjectIdentity
qosMgt = _QosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16)
)
_RateLimitMgt_ObjectIdentity = ObjectIdentity
rateLimitMgt = _RateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 1)
)
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("current")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 1, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "rlPortIndex"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("current")
_RlPortIndex_Type = Integer32
_RlPortIndex_Object = MibTableColumn
rlPortIndex = _RlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 1, 2, 1, 1),
    _RlPortIndex_Type()
)
rlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortIndex.setStatus("current")
_RlPortInputStatus_Type = EnabledStatus
_RlPortInputStatus_Object = MibTableColumn
rlPortInputStatus = _RlPortInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 1, 2, 1, 6),
    _RlPortInputStatus_Type()
)
rlPortInputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputStatus.setStatus("current")
_RlPortOutputStatus_Type = EnabledStatus
_RlPortOutputStatus_Object = MibTableColumn
rlPortOutputStatus = _RlPortOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 1, 2, 1, 7),
    _RlPortOutputStatus_Type()
)
rlPortOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputStatus.setStatus("current")
_RlPortInputLimitInKilo_Type = Integer32
_RlPortInputLimitInKilo_Object = MibTableColumn
rlPortInputLimitInKilo = _RlPortInputLimitInKilo_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 1, 2, 1, 10),
    _RlPortInputLimitInKilo_Type()
)
rlPortInputLimitInKilo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputLimitInKilo.setStatus("current")
_RlPortOutputLimitInKilo_Type = Integer32
_RlPortOutputLimitInKilo_Object = MibTableColumn
rlPortOutputLimitInKilo = _RlPortOutputLimitInKilo_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 1, 2, 1, 11),
    _RlPortOutputLimitInKilo_Type()
)
rlPortOutputLimitInKilo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputLimitInKilo.setStatus("current")
_DiffServMgt_ObjectIdentity = ObjectIdentity
diffServMgt = _DiffServMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4)
)
_DiffServPortTable_Object = MibTable
diffServPortTable = _DiffServPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 9)
)
if mibBuilder.loadTexts:
    diffServPortTable.setStatus("current")
_DiffServPortEntry_Object = MibTableRow
diffServPortEntry = _DiffServPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 9, 1)
)
diffServPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServPortIfIndex"),
)
if mibBuilder.loadTexts:
    diffServPortEntry.setStatus("current")
_DiffServPortIfIndex_Type = Integer32
_DiffServPortIfIndex_Object = MibTableColumn
diffServPortIfIndex = _DiffServPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 9, 1, 1),
    _DiffServPortIfIndex_Type()
)
diffServPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServPortIfIndex.setStatus("current")
_DiffServPortPolicyMapIndex_Type = Integer32
_DiffServPortPolicyMapIndex_Object = MibTableColumn
diffServPortPolicyMapIndex = _DiffServPortPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 9, 1, 2),
    _DiffServPortPolicyMapIndex_Type()
)
diffServPortPolicyMapIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPortPolicyMapIndex.setStatus("current")
_DiffServPortIngressIpAclIndex_Type = Integer32
_DiffServPortIngressIpAclIndex_Object = MibTableColumn
diffServPortIngressIpAclIndex = _DiffServPortIngressIpAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 9, 1, 3),
    _DiffServPortIngressIpAclIndex_Type()
)
diffServPortIngressIpAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPortIngressIpAclIndex.setStatus("current")
_DiffServPortIngressMacAclIndex_Type = Integer32
_DiffServPortIngressMacAclIndex_Object = MibTableColumn
diffServPortIngressMacAclIndex = _DiffServPortIngressMacAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 9, 1, 4),
    _DiffServPortIngressMacAclIndex_Type()
)
diffServPortIngressMacAclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPortIngressMacAclIndex.setStatus("current")
_DiffServPortIngressIpv6AclIndex_Type = Integer32
_DiffServPortIngressIpv6AclIndex_Object = MibTableColumn
diffServPortIngressIpv6AclIndex = _DiffServPortIngressIpv6AclIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 9, 1, 5),
    _DiffServPortIngressIpv6AclIndex_Type()
)
diffServPortIngressIpv6AclIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPortIngressIpv6AclIndex.setStatus("current")
_DiffServPolicyMapTable_Object = MibTable
diffServPolicyMapTable = _DiffServPolicyMapTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 10)
)
if mibBuilder.loadTexts:
    diffServPolicyMapTable.setStatus("current")
_DiffServPolicyMapEntry_Object = MibTableRow
diffServPolicyMapEntry = _DiffServPolicyMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 10, 1)
)
diffServPolicyMapEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServPolicyMapIndex"),
)
if mibBuilder.loadTexts:
    diffServPolicyMapEntry.setStatus("current")
_DiffServPolicyMapIndex_Type = Integer32
_DiffServPolicyMapIndex_Object = MibTableColumn
diffServPolicyMapIndex = _DiffServPolicyMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 10, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 10, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 10, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 10, 1, 4),
    _DiffServPolicyMapElementIndexList_Type()
)
diffServPolicyMapElementIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServPolicyMapElementIndexList.setStatus("current")
_DiffServPolicyMapStatus_Type = RowStatus
_DiffServPolicyMapStatus_Object = MibTableColumn
diffServPolicyMapStatus = _DiffServPolicyMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 10, 1, 5),
    _DiffServPolicyMapStatus_Type()
)
diffServPolicyMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapStatus.setStatus("current")
_DiffServPolicyMapAttachCtl_ObjectIdentity = ObjectIdentity
diffServPolicyMapAttachCtl = _DiffServPolicyMapAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 11)
)
_DiffServPolicyMapAttachCtlIndex_Type = Integer32
_DiffServPolicyMapAttachCtlIndex_Object = MibScalar
diffServPolicyMapAttachCtlIndex = _DiffServPolicyMapAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 11, 1),
    _DiffServPolicyMapAttachCtlIndex_Type()
)
diffServPolicyMapAttachCtlIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlIndex.setStatus("current")
_DiffServPolicyMapAttachCtlElementIndex_Type = Integer32
_DiffServPolicyMapAttachCtlElementIndex_Object = MibScalar
diffServPolicyMapAttachCtlElementIndex = _DiffServPolicyMapAttachCtlElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 11, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 11, 3),
    _DiffServPolicyMapAttachCtlAction_Type()
)
diffServPolicyMapAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServPolicyMapAttachCtlAction.setStatus("current")
_DiffServPolicyMapElementTable_Object = MibTable
diffServPolicyMapElementTable = _DiffServPolicyMapElementTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 12)
)
if mibBuilder.loadTexts:
    diffServPolicyMapElementTable.setStatus("current")
_DiffServPolicyMapElementEntry_Object = MibTableRow
diffServPolicyMapElementEntry = _DiffServPolicyMapElementEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 12, 1)
)
diffServPolicyMapElementEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServPolicyMapElementIndex"),
)
if mibBuilder.loadTexts:
    diffServPolicyMapElementEntry.setStatus("current")
_DiffServPolicyMapElementIndex_Type = Integer32
_DiffServPolicyMapElementIndex_Object = MibTableColumn
diffServPolicyMapElementIndex = _DiffServPolicyMapElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 12, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 12, 1, 2),
    _DiffServPolicyMapElementClassMapIndex_Type()
)
diffServPolicyMapElementClassMapIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementClassMapIndex.setStatus("current")
_DiffServPolicyMapElementMeterIndex_Type = Integer32
_DiffServPolicyMapElementMeterIndex_Object = MibTableColumn
diffServPolicyMapElementMeterIndex = _DiffServPolicyMapElementMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 12, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 12, 1, 4),
    _DiffServPolicyMapElementActionIndex_Type()
)
diffServPolicyMapElementActionIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementActionIndex.setStatus("current")
_DiffServPolicyMapElementStatus_Type = RowStatus
_DiffServPolicyMapElementStatus_Object = MibTableColumn
diffServPolicyMapElementStatus = _DiffServPolicyMapElementStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 12, 1, 5),
    _DiffServPolicyMapElementStatus_Type()
)
diffServPolicyMapElementStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServPolicyMapElementStatus.setStatus("current")
_DiffServClassMapTable_Object = MibTable
diffServClassMapTable = _DiffServClassMapTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 13)
)
if mibBuilder.loadTexts:
    diffServClassMapTable.setStatus("current")
_DiffServClassMapEntry_Object = MibTableRow
diffServClassMapEntry = _DiffServClassMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 13, 1)
)
diffServClassMapEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServClassMapIndex"),
)
if mibBuilder.loadTexts:
    diffServClassMapEntry.setStatus("current")
_DiffServClassMapIndex_Type = Integer32
_DiffServClassMapIndex_Object = MibTableColumn
diffServClassMapIndex = _DiffServClassMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 13, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 13, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 13, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 13, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 13, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 13, 1, 6),
    _DiffServClassMapElementIndexList_Type()
)
diffServClassMapElementIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServClassMapElementIndexList.setStatus("current")
_DiffServClassMapStatus_Type = RowStatus
_DiffServClassMapStatus_Object = MibTableColumn
diffServClassMapStatus = _DiffServClassMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 13, 1, 7),
    _DiffServClassMapStatus_Type()
)
diffServClassMapStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServClassMapStatus.setStatus("current")
_DiffServClassMapAttachCtl_ObjectIdentity = ObjectIdentity
diffServClassMapAttachCtl = _DiffServClassMapAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 14)
)
_DiffServClassMapAttachCtlIndex_Type = Integer32
_DiffServClassMapAttachCtlIndex_Object = MibScalar
diffServClassMapAttachCtlIndex = _DiffServClassMapAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 14, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 14, 2),
    _DiffServClassMapAttachCtlElementIndexType_Type()
)
diffServClassMapAttachCtlElementIndexType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlElementIndexType.setStatus("current")
_DiffServClassMapAttachCtlElementIndex_Type = Integer32
_DiffServClassMapAttachCtlElementIndex_Object = MibScalar
diffServClassMapAttachCtlElementIndex = _DiffServClassMapAttachCtlElementIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 14, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 14, 4),
    _DiffServClassMapAttachCtlAction_Type()
)
diffServClassMapAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServClassMapAttachCtlAction.setStatus("current")
_DiffServAclTable_Object = MibTable
diffServAclTable = _DiffServAclTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 15)
)
if mibBuilder.loadTexts:
    diffServAclTable.setStatus("current")
_DiffServAclEntry_Object = MibTableRow
diffServAclEntry = _DiffServAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 15, 1)
)
diffServAclEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServAclIndex"),
)
if mibBuilder.loadTexts:
    diffServAclEntry.setStatus("current")
_DiffServAclIndex_Type = Integer32
_DiffServAclIndex_Object = MibTableColumn
diffServAclIndex = _DiffServAclIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 15, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 15, 1, 2),
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
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("mac", 1),
          ("ipstandard", 2),
          ("ipextended", 3),
          ("ipv6standard", 4),
          ("ipv6extended", 5),
          ("arp", 6))
    )


_DiffServAclType_Type.__name__ = "Integer32"
_DiffServAclType_Object = MibTableColumn
diffServAclType = _DiffServAclType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 15, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 15, 1, 4),
    _DiffServAclAceIndexList_Type()
)
diffServAclAceIndexList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServAclAceIndexList.setStatus("current")
_DiffServAclStatus_Type = RowStatus
_DiffServAclStatus_Object = MibTableColumn
diffServAclStatus = _DiffServAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 15, 1, 5),
    _DiffServAclStatus_Type()
)
diffServAclStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServAclStatus.setStatus("current")
_DiffServAclAttachCtl_ObjectIdentity = ObjectIdentity
diffServAclAttachCtl = _DiffServAclAttachCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 16)
)
_DiffServAclAttachCtlIndex_Type = Integer32
_DiffServAclAttachCtlIndex_Object = MibScalar
diffServAclAttachCtlIndex = _DiffServAclAttachCtlIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 16, 1),
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
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("macAce", 1),
          ("ipAce", 2),
          ("ipv6Ace", 3),
          ("arpAce", 4))
    )


_DiffServAclAttachCtlAceType_Type.__name__ = "Integer32"
_DiffServAclAttachCtlAceType_Object = MibScalar
diffServAclAttachCtlAceType = _DiffServAclAttachCtlAceType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 16, 2),
    _DiffServAclAttachCtlAceType_Type()
)
diffServAclAttachCtlAceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAceType.setStatus("current")
_DiffServAclAttachCtlAceIndex_Type = Integer32
_DiffServAclAttachCtlAceIndex_Object = MibScalar
diffServAclAttachCtlAceIndex = _DiffServAclAttachCtlAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 16, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 16, 4),
    _DiffServAclAttachCtlAction_Type()
)
diffServAclAttachCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    diffServAclAttachCtlAction.setStatus("current")
_DiffServIpAceTable_Object = MibTable
diffServIpAceTable = _DiffServIpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17)
)
if mibBuilder.loadTexts:
    diffServIpAceTable.setStatus("current")
_DiffServIpAceEntry_Object = MibTableRow
diffServIpAceEntry = _DiffServIpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1)
)
diffServIpAceEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServIpAceIndex"),
)
if mibBuilder.loadTexts:
    diffServIpAceEntry.setStatus("current")
_DiffServIpAceIndex_Type = Integer32
_DiffServIpAceIndex_Object = MibTableColumn
diffServIpAceIndex = _DiffServIpAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 3),
    _DiffServIpAceAccess_Type()
)
diffServIpAceAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceAccess.setStatus("current")
_DiffServIpAceSourceIpAddr_Type = IpAddress
_DiffServIpAceSourceIpAddr_Object = MibTableColumn
diffServIpAceSourceIpAddr = _DiffServIpAceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 4),
    _DiffServIpAceSourceIpAddr_Type()
)
diffServIpAceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourceIpAddr.setStatus("current")
_DiffServIpAceSourceIpAddrBitmask_Type = IpAddress
_DiffServIpAceSourceIpAddrBitmask_Object = MibTableColumn
diffServIpAceSourceIpAddrBitmask = _DiffServIpAceSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 5),
    _DiffServIpAceSourceIpAddrBitmask_Type()
)
diffServIpAceSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceSourceIpAddrBitmask.setStatus("current")
_DiffServIpAceDestIpAddr_Type = IpAddress
_DiffServIpAceDestIpAddr_Object = MibTableColumn
diffServIpAceDestIpAddr = _DiffServIpAceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 6),
    _DiffServIpAceDestIpAddr_Type()
)
diffServIpAceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestIpAddr.setStatus("current")
_DiffServIpAceDestIpAddrBitmask_Type = IpAddress
_DiffServIpAceDestIpAddrBitmask_Object = MibTableColumn
diffServIpAceDestIpAddrBitmask = _DiffServIpAceDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 15),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 16),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 19),
    _DiffServIpAceDestPortBitmask_Type()
)
diffServIpAceDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceDestPortBitmask.setStatus("current")


class _DiffServIpAceControlCode_Type(Integer32):
    """Custom type diffServIpAceControlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_DiffServIpAceControlCode_Type.__name__ = "Integer32"
_DiffServIpAceControlCode_Object = MibTableColumn
diffServIpAceControlCode = _DiffServIpAceControlCode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 20),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 21),
    _DiffServIpAceControlCodeBitmask_Type()
)
diffServIpAceControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceControlCodeBitmask.setStatus("current")
_DiffServIpAceStatus_Type = RowStatus
_DiffServIpAceStatus_Object = MibTableColumn
diffServIpAceStatus = _DiffServIpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 17, 1, 22),
    _DiffServIpAceStatus_Type()
)
diffServIpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpAceStatus.setStatus("current")
_DiffServMacAceTable_Object = MibTable
diffServMacAceTable = _DiffServMacAceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18)
)
if mibBuilder.loadTexts:
    diffServMacAceTable.setStatus("current")
_DiffServMacAceEntry_Object = MibTableRow
diffServMacAceEntry = _DiffServMacAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1)
)
diffServMacAceEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServMacAceIndex"),
)
if mibBuilder.loadTexts:
    diffServMacAceEntry.setStatus("current")
_DiffServMacAceIndex_Type = Integer32
_DiffServMacAceIndex_Object = MibTableColumn
diffServMacAceIndex = _DiffServMacAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 3),
    _DiffServMacAcePktformat_Type()
)
diffServMacAcePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAcePktformat.setStatus("current")
_DiffServMacAceSourceMacAddr_Type = MacAddress
_DiffServMacAceSourceMacAddr_Object = MibTableColumn
diffServMacAceSourceMacAddr = _DiffServMacAceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 4),
    _DiffServMacAceSourceMacAddr_Type()
)
diffServMacAceSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceSourceMacAddr.setStatus("current")
_DiffServMacAceSourceMacAddrBitmask_Type = MacAddress
_DiffServMacAceSourceMacAddrBitmask_Object = MibTableColumn
diffServMacAceSourceMacAddrBitmask = _DiffServMacAceSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 5),
    _DiffServMacAceSourceMacAddrBitmask_Type()
)
diffServMacAceSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceSourceMacAddrBitmask.setStatus("current")
_DiffServMacAceDestMacAddr_Type = MacAddress
_DiffServMacAceDestMacAddr_Object = MibTableColumn
diffServMacAceDestMacAddr = _DiffServMacAceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 6),
    _DiffServMacAceDestMacAddr_Type()
)
diffServMacAceDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceDestMacAddr.setStatus("current")
_DiffServMacAceDestMacAddrBitmask_Type = MacAddress
_DiffServMacAceDestMacAddrBitmask_Object = MibTableColumn
diffServMacAceDestMacAddrBitmask = _DiffServMacAceDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 9),
    _DiffServMacAceMinVid_Type()
)
diffServMacAceMinVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMinVid.setStatus("current")


class _DiffServMacAceVidBitmask_Type(Integer32):
    """Custom type diffServMacAceVidBitmask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_DiffServMacAceVidBitmask_Type.__name__ = "Integer32"
_DiffServMacAceVidBitmask_Object = MibTableColumn
diffServMacAceVidBitmask = _DiffServMacAceVidBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 12),
    _DiffServMacAceEtherTypeOp_Type()
)
diffServMacAceEtherTypeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceEtherTypeOp.setStatus("current")


class _DiffServMacAceEtherTypeBitmask_Type(Integer32):
    """Custom type diffServMacAceEtherTypeBitmask based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_DiffServMacAceEtherTypeBitmask_Type.__name__ = "Integer32"
_DiffServMacAceEtherTypeBitmask_Object = MibTableColumn
diffServMacAceEtherTypeBitmask = _DiffServMacAceEtherTypeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 14),
    _DiffServMacAceMinEtherType_Type()
)
diffServMacAceMinEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMinEtherType.setStatus("current")
_DiffServMacAceStatus_Type = RowStatus
_DiffServMacAceStatus_Object = MibTableColumn
diffServMacAceStatus = _DiffServMacAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 16),
    _DiffServMacAceStatus_Type()
)
diffServMacAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceStatus.setStatus("current")


class _DiffServMacAceCosOp_Type(Integer32):
    """Custom type diffServMacAceCosOp based on Integer32"""
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


_DiffServMacAceCosOp_Type.__name__ = "Integer32"
_DiffServMacAceCosOp_Object = MibTableColumn
diffServMacAceCosOp = _DiffServMacAceCosOp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 17),
    _DiffServMacAceCosOp_Type()
)
diffServMacAceCosOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceCosOp.setStatus("current")


class _DiffServMacAceCosBitmask_Type(Integer32):
    """Custom type diffServMacAceCosBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DiffServMacAceCosBitmask_Type.__name__ = "Integer32"
_DiffServMacAceCosBitmask_Object = MibTableColumn
diffServMacAceCosBitmask = _DiffServMacAceCosBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 18),
    _DiffServMacAceCosBitmask_Type()
)
diffServMacAceCosBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceCosBitmask.setStatus("current")


class _DiffServMacAceMinCos_Type(Integer32):
    """Custom type diffServMacAceMinCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_DiffServMacAceMinCos_Type.__name__ = "Integer32"
_DiffServMacAceMinCos_Object = MibTableColumn
diffServMacAceMinCos = _DiffServMacAceMinCos_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 18, 1, 19),
    _DiffServMacAceMinCos_Type()
)
diffServMacAceMinCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMacAceMinCos.setStatus("current")
_DiffServActionTable_Object = MibTable
diffServActionTable = _DiffServActionTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 19)
)
if mibBuilder.loadTexts:
    diffServActionTable.setStatus("current")
_DiffServActionEntry_Object = MibTableRow
diffServActionEntry = _DiffServActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 19, 1)
)
diffServActionEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServActionIndex"),
)
if mibBuilder.loadTexts:
    diffServActionEntry.setStatus("current")
_DiffServActionIndex_Type = Integer32
_DiffServActionIndex_Object = MibTableColumn
diffServActionIndex = _DiffServActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 19, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 19, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 19, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 19, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 19, 1, 6),
    _DiffServActionRedPktNewDscp_Type()
)
diffServActionRedPktNewDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionRedPktNewDscp.setStatus("current")
_DiffServActionRedDrop_Type = EnabledStatus
_DiffServActionRedDrop_Object = MibTableColumn
diffServActionRedDrop = _DiffServActionRedDrop_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 19, 1, 7),
    _DiffServActionRedDrop_Type()
)
diffServActionRedDrop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServActionRedDrop.setStatus("current")
_DiffServActionStatus_Type = RowStatus
_DiffServActionStatus_Object = MibTableColumn
diffServActionStatus = _DiffServActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 19, 1, 8),
    _DiffServActionStatus_Type()
)
diffServActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServActionStatus.setStatus("current")
_DiffServMeterTable_Object = MibTable
diffServMeterTable = _DiffServMeterTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 20)
)
if mibBuilder.loadTexts:
    diffServMeterTable.setStatus("current")
_DiffServMeterEntry_Object = MibTableRow
diffServMeterEntry = _DiffServMeterEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 20, 1)
)
diffServMeterEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServActionIndex"),
)
if mibBuilder.loadTexts:
    diffServMeterEntry.setStatus("current")
_DiffServMeterIndex_Type = Integer32
_DiffServMeterIndex_Object = MibTableColumn
diffServMeterIndex = _DiffServMeterIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 20, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 20, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 20, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 20, 1, 4),
    _DiffServMeterBurstSize_Type()
)
diffServMeterBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterBurstSize.setStatus("current")
_DiffServMeterInterval_Type = Integer32
_DiffServMeterInterval_Object = MibTableColumn
diffServMeterInterval = _DiffServMeterInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 20, 1, 5),
    _DiffServMeterInterval_Type()
)
diffServMeterInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterInterval.setStatus("current")
_DiffServMeterStatus_Type = RowStatus
_DiffServMeterStatus_Object = MibTableColumn
diffServMeterStatus = _DiffServMeterStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 20, 1, 6),
    _DiffServMeterStatus_Type()
)
diffServMeterStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServMeterStatus.setStatus("current")
_DiffServIpv6AceTable_Object = MibTable
diffServIpv6AceTable = _DiffServIpv6AceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21)
)
if mibBuilder.loadTexts:
    diffServIpv6AceTable.setStatus("current")
_DiffServIpv6AceEntry_Object = MibTableRow
diffServIpv6AceEntry = _DiffServIpv6AceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21, 1)
)
diffServIpv6AceEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServIpv6AceIndex"),
)
if mibBuilder.loadTexts:
    diffServIpv6AceEntry.setStatus("current")
_DiffServIpv6AceIndex_Type = Integer32
_DiffServIpv6AceIndex_Object = MibTableColumn
diffServIpv6AceIndex = _DiffServIpv6AceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21, 1, 1),
    _DiffServIpv6AceIndex_Type()
)
diffServIpv6AceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServIpv6AceIndex.setStatus("current")


class _DiffServIpv6AceType_Type(Integer32):
    """Custom type diffServIpv6AceType based on Integer32"""
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


_DiffServIpv6AceType_Type.__name__ = "Integer32"
_DiffServIpv6AceType_Object = MibTableColumn
diffServIpv6AceType = _DiffServIpv6AceType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21, 1, 2),
    _DiffServIpv6AceType_Type()
)
diffServIpv6AceType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceType.setStatus("current")


class _DiffServIpv6AceAccess_Type(Integer32):
    """Custom type diffServIpv6AceAccess based on Integer32"""
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


_DiffServIpv6AceAccess_Type.__name__ = "Integer32"
_DiffServIpv6AceAccess_Object = MibTableColumn
diffServIpv6AceAccess = _DiffServIpv6AceAccess_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21, 1, 3),
    _DiffServIpv6AceAccess_Type()
)
diffServIpv6AceAccess.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceAccess.setStatus("current")


class _DiffServIpv6AceSourceIpAddr_Type(OctetString):
    """Custom type diffServIpv6AceSourceIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DiffServIpv6AceSourceIpAddr_Type.__name__ = "OctetString"
_DiffServIpv6AceSourceIpAddr_Object = MibTableColumn
diffServIpv6AceSourceIpAddr = _DiffServIpv6AceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21, 1, 4),
    _DiffServIpv6AceSourceIpAddr_Type()
)
diffServIpv6AceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceSourceIpAddr.setStatus("current")


class _DiffServIpv6AceSourceIpAddrPrefixLen_Type(Integer32):
    """Custom type diffServIpv6AceSourceIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 128),
    )


_DiffServIpv6AceSourceIpAddrPrefixLen_Type.__name__ = "Integer32"
_DiffServIpv6AceSourceIpAddrPrefixLen_Object = MibTableColumn
diffServIpv6AceSourceIpAddrPrefixLen = _DiffServIpv6AceSourceIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21, 1, 5),
    _DiffServIpv6AceSourceIpAddrPrefixLen_Type()
)
diffServIpv6AceSourceIpAddrPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceSourceIpAddrPrefixLen.setStatus("current")


class _DiffServIpv6AceDestIpAddr_Type(OctetString):
    """Custom type diffServIpv6AceDestIpAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_DiffServIpv6AceDestIpAddr_Type.__name__ = "OctetString"
_DiffServIpv6AceDestIpAddr_Object = MibTableColumn
diffServIpv6AceDestIpAddr = _DiffServIpv6AceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21, 1, 6),
    _DiffServIpv6AceDestIpAddr_Type()
)
diffServIpv6AceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceDestIpAddr.setStatus("current")


class _DiffServIpv6AceDestIpAddrPrefixLen_Type(Integer32):
    """Custom type diffServIpv6AceDestIpAddrPrefixLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_DiffServIpv6AceDestIpAddrPrefixLen_Type.__name__ = "Integer32"
_DiffServIpv6AceDestIpAddrPrefixLen_Object = MibTableColumn
diffServIpv6AceDestIpAddrPrefixLen = _DiffServIpv6AceDestIpAddrPrefixLen_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21, 1, 7),
    _DiffServIpv6AceDestIpAddrPrefixLen_Type()
)
diffServIpv6AceDestIpAddrPrefixLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceDestIpAddrPrefixLen.setStatus("current")


class _DiffServIpv6AceDscp_Type(Integer32):
    """Custom type diffServIpv6AceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_DiffServIpv6AceDscp_Type.__name__ = "Integer32"
_DiffServIpv6AceDscp_Object = MibTableColumn
diffServIpv6AceDscp = _DiffServIpv6AceDscp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21, 1, 9),
    _DiffServIpv6AceDscp_Type()
)
diffServIpv6AceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceDscp.setStatus("current")
_DiffServIpv6AceStatus_Type = RowStatus
_DiffServIpv6AceStatus_Object = MibTableColumn
diffServIpv6AceStatus = _DiffServIpv6AceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 21, 1, 11),
    _DiffServIpv6AceStatus_Type()
)
diffServIpv6AceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServIpv6AceStatus.setStatus("current")
_DiffServArpAceTable_Object = MibTable
diffServArpAceTable = _DiffServArpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23)
)
if mibBuilder.loadTexts:
    diffServArpAceTable.setStatus("current")
_DiffServArpAceEntry_Object = MibTableRow
diffServArpAceEntry = _DiffServArpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1)
)
diffServArpAceEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServArpAceIndex"),
)
if mibBuilder.loadTexts:
    diffServArpAceEntry.setStatus("current")


class _DiffServArpAceIndex_Type(Integer32):
    """Custom type diffServArpAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DiffServArpAceIndex_Type.__name__ = "Integer32"
_DiffServArpAceIndex_Object = MibTableColumn
diffServArpAceIndex = _DiffServArpAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 1),
    _DiffServArpAceIndex_Type()
)
diffServArpAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    diffServArpAceIndex.setStatus("current")


class _DiffServArpAceAction_Type(Integer32):
    """Custom type diffServArpAceAction based on Integer32"""
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


_DiffServArpAceAction_Type.__name__ = "Integer32"
_DiffServArpAceAction_Object = MibTableColumn
diffServArpAceAction = _DiffServArpAceAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 2),
    _DiffServArpAceAction_Type()
)
diffServArpAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceAction.setStatus("current")


class _DiffServArpAcePktType_Type(Integer32):
    """Custom type diffServArpAcePktType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("request", 1),
          ("response", 2),
          ("both", 3))
    )


_DiffServArpAcePktType_Type.__name__ = "Integer32"
_DiffServArpAcePktType_Object = MibTableColumn
diffServArpAcePktType = _DiffServArpAcePktType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 3),
    _DiffServArpAcePktType_Type()
)
diffServArpAcePktType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAcePktType.setStatus("current")
_DiffServArpAceSourceIpAddr_Type = IpAddress
_DiffServArpAceSourceIpAddr_Object = MibTableColumn
diffServArpAceSourceIpAddr = _DiffServArpAceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 4),
    _DiffServArpAceSourceIpAddr_Type()
)
diffServArpAceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceSourceIpAddr.setStatus("current")
_DiffServArpAceSourceIpAddrBitmask_Type = IpAddress
_DiffServArpAceSourceIpAddrBitmask_Object = MibTableColumn
diffServArpAceSourceIpAddrBitmask = _DiffServArpAceSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 5),
    _DiffServArpAceSourceIpAddrBitmask_Type()
)
diffServArpAceSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceSourceIpAddrBitmask.setStatus("current")
_DiffServArpAceDestIpAddr_Type = IpAddress
_DiffServArpAceDestIpAddr_Object = MibTableColumn
diffServArpAceDestIpAddr = _DiffServArpAceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 6),
    _DiffServArpAceDestIpAddr_Type()
)
diffServArpAceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceDestIpAddr.setStatus("current")
_DiffServArpAceDestIpAddrBitmask_Type = IpAddress
_DiffServArpAceDestIpAddrBitmask_Object = MibTableColumn
diffServArpAceDestIpAddrBitmask = _DiffServArpAceDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 7),
    _DiffServArpAceDestIpAddrBitmask_Type()
)
diffServArpAceDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceDestIpAddrBitmask.setStatus("current")


class _DiffServArpAceSourceMacAddr_Type(OctetString):
    """Custom type diffServArpAceSourceMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_DiffServArpAceSourceMacAddr_Type.__name__ = "OctetString"
_DiffServArpAceSourceMacAddr_Object = MibTableColumn
diffServArpAceSourceMacAddr = _DiffServArpAceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 8),
    _DiffServArpAceSourceMacAddr_Type()
)
diffServArpAceSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceSourceMacAddr.setStatus("current")


class _DiffServArpAceSourceMacAddrBitmask_Type(OctetString):
    """Custom type diffServArpAceSourceMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_DiffServArpAceSourceMacAddrBitmask_Type.__name__ = "OctetString"
_DiffServArpAceSourceMacAddrBitmask_Object = MibTableColumn
diffServArpAceSourceMacAddrBitmask = _DiffServArpAceSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 9),
    _DiffServArpAceSourceMacAddrBitmask_Type()
)
diffServArpAceSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceSourceMacAddrBitmask.setStatus("current")


class _DiffServArpAceDestMacAddr_Type(OctetString):
    """Custom type diffServArpAceDestMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_DiffServArpAceDestMacAddr_Type.__name__ = "OctetString"
_DiffServArpAceDestMacAddr_Object = MibTableColumn
diffServArpAceDestMacAddr = _DiffServArpAceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 10),
    _DiffServArpAceDestMacAddr_Type()
)
diffServArpAceDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceDestMacAddr.setStatus("current")


class _DiffServArpAceDestMacAddrBitmask_Type(OctetString):
    """Custom type diffServArpAceDestMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_DiffServArpAceDestMacAddrBitmask_Type.__name__ = "OctetString"
_DiffServArpAceDestMacAddrBitmask_Object = MibTableColumn
diffServArpAceDestMacAddrBitmask = _DiffServArpAceDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 11),
    _DiffServArpAceDestMacAddrBitmask_Type()
)
diffServArpAceDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceDestMacAddrBitmask.setStatus("current")
_DiffServArpAceLogStatus_Type = EnabledStatus
_DiffServArpAceLogStatus_Object = MibTableColumn
diffServArpAceLogStatus = _DiffServArpAceLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 12),
    _DiffServArpAceLogStatus_Type()
)
diffServArpAceLogStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceLogStatus.setStatus("current")
_DiffServArpAceStatus_Type = RowStatus
_DiffServArpAceStatus_Object = MibTableColumn
diffServArpAceStatus = _DiffServArpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 23, 1, 13),
    _DiffServArpAceStatus_Type()
)
diffServArpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    diffServArpAceStatus.setStatus("current")
_DiffServArpTable_Object = MibTable
diffServArpTable = _DiffServArpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 24)
)
if mibBuilder.loadTexts:
    diffServArpTable.setStatus("current")
_DiffServArpEntry_Object = MibTableRow
diffServArpEntry = _DiffServArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 24, 1)
)
diffServArpEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "diffServArpAclName"),
)
if mibBuilder.loadTexts:
    diffServArpEntry.setStatus("current")


class _DiffServArpAclName_Type(DisplayString):
    """Custom type diffServArpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DiffServArpAclName_Type.__name__ = "DisplayString"
_DiffServArpAclName_Object = MibTableColumn
diffServArpAclName = _DiffServArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 24, 1, 1),
    _DiffServArpAclName_Type()
)
diffServArpAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServArpAclName.setStatus("current")
_DiffServTcamMgt_ObjectIdentity = ObjectIdentity
diffServTcamMgt = _DiffServTcamMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 25)
)
_DiffServTcamTotalPolicyControlEntries_Type = Integer32
_DiffServTcamTotalPolicyControlEntries_Object = MibScalar
diffServTcamTotalPolicyControlEntries = _DiffServTcamTotalPolicyControlEntries_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 25, 1),
    _DiffServTcamTotalPolicyControlEntries_Type()
)
diffServTcamTotalPolicyControlEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServTcamTotalPolicyControlEntries.setStatus("current")
_DiffServTcamFreePolicyControlEntries_Type = Integer32
_DiffServTcamFreePolicyControlEntries_Object = MibScalar
diffServTcamFreePolicyControlEntries = _DiffServTcamFreePolicyControlEntries_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 25, 2),
    _DiffServTcamFreePolicyControlEntries_Type()
)
diffServTcamFreePolicyControlEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServTcamFreePolicyControlEntries.setStatus("current")


class _DiffServTcamUtilization_Type(Integer32):
    """Custom type diffServTcamUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_DiffServTcamUtilization_Type.__name__ = "Integer32"
_DiffServTcamUtilization_Object = MibScalar
diffServTcamUtilization = _DiffServTcamUtilization_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 16, 4, 25, 3),
    _DiffServTcamUtilization_Type()
)
diffServTcamUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    diffServTcamUtilization.setStatus("current")
_SecurityMgt_ObjectIdentity = ObjectIdentity
securityMgt = _SecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17)
)
_PrivateVlanMgt_ObjectIdentity = ObjectIdentity
privateVlanMgt = _PrivateVlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1)
)
_PrivateVlanStatus_Type = EnabledStatus
_PrivateVlanStatus_Object = MibScalar
privateVlanStatus = _PrivateVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 1),
    _PrivateVlanStatus_Type()
)
privateVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanStatus.setStatus("current")
_PrivateVlanVlanTable_Object = MibTable
privateVlanVlanTable = _PrivateVlanVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 4)
)
if mibBuilder.loadTexts:
    privateVlanVlanTable.setStatus("current")
_PrivateVlanVlanEntry_Object = MibTableRow
privateVlanVlanEntry = _PrivateVlanVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 4, 1)
)
privateVlanVlanEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "privateVlanVlanIndex"),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 4, 1, 3),
    _PrivateVlanAssoicatedPrimaryVlan_Type()
)
privateVlanAssoicatedPrimaryVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanAssoicatedPrimaryVlan.setStatus("current")
_PrivateVlanPrivatePortTable_Object = MibTable
privateVlanPrivatePortTable = _PrivateVlanPrivatePortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 5)
)
if mibBuilder.loadTexts:
    privateVlanPrivatePortTable.setStatus("current")
_PrivateVlanPrivatePortEntry_Object = MibTableRow
privateVlanPrivatePortEntry = _PrivateVlanPrivatePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 5, 1)
)
privateVlanPrivatePortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "privateVlanPrivatePortIfIndex"),
)
if mibBuilder.loadTexts:
    privateVlanPrivatePortEntry.setStatus("current")
_PrivateVlanPrivatePortIfIndex_Type = Integer32
_PrivateVlanPrivatePortIfIndex_Object = MibTableColumn
privateVlanPrivatePortIfIndex = _PrivateVlanPrivatePortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 5, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 5, 1, 2),
    _PrivateVlanPrivatePortSecondaryVlan_Type()
)
privateVlanPrivatePortSecondaryVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanPrivatePortSecondaryVlan.setStatus("current")
_PrivateVlanPromPortTable_Object = MibTable
privateVlanPromPortTable = _PrivateVlanPromPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 6)
)
if mibBuilder.loadTexts:
    privateVlanPromPortTable.setStatus("current")
_PrivateVlanPromPortEntry_Object = MibTableRow
privateVlanPromPortEntry = _PrivateVlanPromPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 6, 1)
)
privateVlanPromPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "privateVlanPromPortIfIndex"),
)
if mibBuilder.loadTexts:
    privateVlanPromPortEntry.setStatus("current")
_PrivateVlanPromPortIfIndex_Type = Integer32
_PrivateVlanPromPortIfIndex_Object = MibTableColumn
privateVlanPromPortIfIndex = _PrivateVlanPromPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 6, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 6, 1, 6),
    _PrivateVlanPromPortSecondaryRemap4k_Type()
)
privateVlanPromPortSecondaryRemap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    privateVlanPromPortSecondaryRemap4k.setStatus("current")
_PrivateVlanSessionTable_Object = MibTable
privateVlanSessionTable = _PrivateVlanSessionTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 8)
)
if mibBuilder.loadTexts:
    privateVlanSessionTable.setStatus("current")
_PrivateVlanSessionEntry_Object = MibTableRow
privateVlanSessionEntry = _PrivateVlanSessionEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 8, 1)
)
privateVlanSessionEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "privateVlanSessionId"),
)
if mibBuilder.loadTexts:
    privateVlanSessionEntry.setStatus("current")
_PrivateVlanSessionId_Type = Integer32
_PrivateVlanSessionId_Object = MibTableColumn
privateVlanSessionId = _PrivateVlanSessionId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 8, 1, 1),
    _PrivateVlanSessionId_Type()
)
privateVlanSessionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    privateVlanSessionId.setStatus("current")
_PrivateVlanSessionUplinkPorts_Type = PortList
_PrivateVlanSessionUplinkPorts_Object = MibTableColumn
privateVlanSessionUplinkPorts = _PrivateVlanSessionUplinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 8, 1, 2),
    _PrivateVlanSessionUplinkPorts_Type()
)
privateVlanSessionUplinkPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanSessionUplinkPorts.setStatus("current")
_PrivateVlanSessionDownlinkPorts_Type = PortList
_PrivateVlanSessionDownlinkPorts_Object = MibTableColumn
privateVlanSessionDownlinkPorts = _PrivateVlanSessionDownlinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 8, 1, 3),
    _PrivateVlanSessionDownlinkPorts_Type()
)
privateVlanSessionDownlinkPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanSessionDownlinkPorts.setStatus("current")
_PrivateVlanSessionStatus_Type = ValidStatus
_PrivateVlanSessionStatus_Object = MibTableColumn
privateVlanSessionStatus = _PrivateVlanSessionStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 8, 1, 4),
    _PrivateVlanSessionStatus_Type()
)
privateVlanSessionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    privateVlanSessionStatus.setStatus("current")


class _PrivateVlanUplinkToUplink_Type(Integer32):
    """Custom type privateVlanUplinkToUplink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blocking", 1),
          ("forwarding", 2))
    )


_PrivateVlanUplinkToUplink_Type.__name__ = "Integer32"
_PrivateVlanUplinkToUplink_Object = MibScalar
privateVlanUplinkToUplink = _PrivateVlanUplinkToUplink_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 1, 9),
    _PrivateVlanUplinkToUplink_Type()
)
privateVlanUplinkToUplink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanUplinkToUplink.setStatus("current")
_PortSecurityMgt_ObjectIdentity = ObjectIdentity
portSecurityMgt = _PortSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 2)
)
_PortSecPortTable_Object = MibTable
portSecPortTable = _PortSecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    portSecPortTable.setStatus("current")
_PortSecPortEntry_Object = MibTableRow
portSecPortEntry = _PortSecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 2, 1, 1)
)
portSecPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "portSecPortIndex"),
)
if mibBuilder.loadTexts:
    portSecPortEntry.setStatus("current")
_PortSecPortIndex_Type = Integer32
_PortSecPortIndex_Object = MibTableColumn
portSecPortIndex = _PortSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 2, 1, 1, 1),
    _PortSecPortIndex_Type()
)
portSecPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSecPortIndex.setStatus("current")
_PortSecPortStatus_Type = EnabledStatus
_PortSecPortStatus_Object = MibTableColumn
portSecPortStatus = _PortSecPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 2, 1, 1, 4),
    _PortSecMaxMacCount_Type()
)
portSecMaxMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMaxMacCount.setStatus("current")
_RadiusMgt_ObjectIdentity = ObjectIdentity
radiusMgt = _RadiusMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4)
)


class _RadiusServerGlobalAuthPort_Type(Integer32):
    """Custom type radiusServerGlobalAuthPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerGlobalAuthPort_Type.__name__ = "Integer32"
_RadiusServerGlobalAuthPort_Object = MibScalar
radiusServerGlobalAuthPort = _RadiusServerGlobalAuthPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 1),
    _RadiusServerGlobalAuthPort_Type()
)
radiusServerGlobalAuthPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalAuthPort.setStatus("current")


class _RadiusServerGlobalAcctPort_Type(Integer32):
    """Custom type radiusServerGlobalAcctPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerGlobalAcctPort_Type.__name__ = "Integer32"
_RadiusServerGlobalAcctPort_Object = MibScalar
radiusServerGlobalAcctPort = _RadiusServerGlobalAcctPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 2),
    _RadiusServerGlobalAcctPort_Type()
)
radiusServerGlobalAcctPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalAcctPort.setStatus("current")


class _RadiusServerGlobalKey_Type(DisplayString):
    """Custom type radiusServerGlobalKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RadiusServerGlobalKey_Type.__name__ = "DisplayString"
_RadiusServerGlobalKey_Object = MibScalar
radiusServerGlobalKey = _RadiusServerGlobalKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 3),
    _RadiusServerGlobalKey_Type()
)
radiusServerGlobalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalKey.setStatus("current")


class _RadiusServerGlobalRetransmit_Type(Integer32):
    """Custom type radiusServerGlobalRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_RadiusServerGlobalRetransmit_Type.__name__ = "Integer32"
_RadiusServerGlobalRetransmit_Object = MibScalar
radiusServerGlobalRetransmit = _RadiusServerGlobalRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 4),
    _RadiusServerGlobalRetransmit_Type()
)
radiusServerGlobalRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalRetransmit.setStatus("current")


class _RadiusServerGlobalTimeout_Type(Integer32):
    """Custom type radiusServerGlobalTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerGlobalTimeout_Type.__name__ = "Integer32"
_RadiusServerGlobalTimeout_Object = MibScalar
radiusServerGlobalTimeout = _RadiusServerGlobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 5),
    _RadiusServerGlobalTimeout_Type()
)
radiusServerGlobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerGlobalTimeout.setStatus("current")
_RadiusServerTable_Object = MibTable
radiusServerTable = _RadiusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 7)
)
if mibBuilder.loadTexts:
    radiusServerTable.setStatus("current")
_RadiusServerEntry_Object = MibTableRow
radiusServerEntry = _RadiusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 7, 1)
)
radiusServerEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "radiusServerIndex"),
)
if mibBuilder.loadTexts:
    radiusServerEntry.setStatus("current")
_RadiusServerIndex_Type = Integer32
_RadiusServerIndex_Object = MibTableColumn
radiusServerIndex = _RadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 7, 1, 1),
    _RadiusServerIndex_Type()
)
radiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusServerIndex.setStatus("current")
_RadiusServerAddress_Type = IpAddress
_RadiusServerAddress_Object = MibTableColumn
radiusServerAddress = _RadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 7, 1, 2),
    _RadiusServerAddress_Type()
)
radiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerAddress.setStatus("current")


class _RadiusServerAuthPortNumber_Type(Integer32):
    """Custom type radiusServerAuthPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerAuthPortNumber_Type.__name__ = "Integer32"
_RadiusServerAuthPortNumber_Object = MibTableColumn
radiusServerAuthPortNumber = _RadiusServerAuthPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 7, 1, 3),
    _RadiusServerAuthPortNumber_Type()
)
radiusServerAuthPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerAuthPortNumber.setStatus("current")


class _RadiusServerAcctPortNumber_Type(Integer32):
    """Custom type radiusServerAcctPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerAcctPortNumber_Type.__name__ = "Integer32"
_RadiusServerAcctPortNumber_Object = MibTableColumn
radiusServerAcctPortNumber = _RadiusServerAcctPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 7, 1, 4),
    _RadiusServerAcctPortNumber_Type()
)
radiusServerAcctPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerAcctPortNumber.setStatus("current")


class _RadiusServerKey_Type(DisplayString):
    """Custom type radiusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_RadiusServerKey_Type.__name__ = "DisplayString"
_RadiusServerKey_Object = MibTableColumn
radiusServerKey = _RadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 7, 1, 5),
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
_RadiusServerRetransmit_Object = MibTableColumn
radiusServerRetransmit = _RadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 7, 1, 6),
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
_RadiusServerTimeout_Object = MibTableColumn
radiusServerTimeout = _RadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 7, 1, 7),
    _RadiusServerTimeout_Type()
)
radiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerTimeout.setStatus("current")
_RadiusServerStatus_Type = ValidStatus
_RadiusServerStatus_Object = MibTableColumn
radiusServerStatus = _RadiusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 4, 7, 1, 8),
    _RadiusServerStatus_Type()
)
radiusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusServerStatus.setStatus("current")
_TacacsMgt_ObjectIdentity = ObjectIdentity
tacacsMgt = _TacacsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5)
)


class _TacacsPlusServerGlobalPortNumber_Type(Integer32):
    """Custom type tacacsPlusServerGlobalPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsPlusServerGlobalPortNumber_Type.__name__ = "Integer32"
_TacacsPlusServerGlobalPortNumber_Object = MibScalar
tacacsPlusServerGlobalPortNumber = _TacacsPlusServerGlobalPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 2),
    _TacacsPlusServerGlobalPortNumber_Type()
)
tacacsPlusServerGlobalPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalPortNumber.setStatus("current")


class _TacacsPlusServerGlobalKey_Type(DisplayString):
    """Custom type tacacsPlusServerGlobalKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TacacsPlusServerGlobalKey_Type.__name__ = "DisplayString"
_TacacsPlusServerGlobalKey_Object = MibScalar
tacacsPlusServerGlobalKey = _TacacsPlusServerGlobalKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 3),
    _TacacsPlusServerGlobalKey_Type()
)
tacacsPlusServerGlobalKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalKey.setStatus("current")
_TacacsPlusServerTable_Object = MibTable
tacacsPlusServerTable = _TacacsPlusServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 4)
)
if mibBuilder.loadTexts:
    tacacsPlusServerTable.setStatus("current")
_TacacsPlusServerEntry_Object = MibTableRow
tacacsPlusServerEntry = _TacacsPlusServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 4, 1)
)
tacacsPlusServerEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "tacacsPlusServerIndex"),
)
if mibBuilder.loadTexts:
    tacacsPlusServerEntry.setStatus("current")
_TacacsPlusServerIndex_Type = Integer32
_TacacsPlusServerIndex_Object = MibTableColumn
tacacsPlusServerIndex = _TacacsPlusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 4, 1, 1),
    _TacacsPlusServerIndex_Type()
)
tacacsPlusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacacsPlusServerIndex.setStatus("current")
_TacacsPlusServerAddress_Type = IpAddress
_TacacsPlusServerAddress_Object = MibTableColumn
tacacsPlusServerAddress = _TacacsPlusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 4, 1, 2),
    _TacacsPlusServerAddress_Type()
)
tacacsPlusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerAddress.setStatus("current")


class _TacacsPlusServerPortNumber_Type(Integer32):
    """Custom type tacacsPlusServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacacsPlusServerPortNumber_Type.__name__ = "Integer32"
_TacacsPlusServerPortNumber_Object = MibTableColumn
tacacsPlusServerPortNumber = _TacacsPlusServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 4, 1, 3),
    _TacacsPlusServerPortNumber_Type()
)
tacacsPlusServerPortNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerPortNumber.setStatus("current")


class _TacacsPlusServerKey_Type(DisplayString):
    """Custom type tacacsPlusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 48),
    )


_TacacsPlusServerKey_Type.__name__ = "DisplayString"
_TacacsPlusServerKey_Object = MibTableColumn
tacacsPlusServerKey = _TacacsPlusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 4, 1, 4),
    _TacacsPlusServerKey_Type()
)
tacacsPlusServerKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerKey.setStatus("current")
_TacacsPlusServerStatus_Type = ValidStatus
_TacacsPlusServerStatus_Object = MibTableColumn
tacacsPlusServerStatus = _TacacsPlusServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 4, 1, 8),
    _TacacsPlusServerStatus_Type()
)
tacacsPlusServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerStatus.setStatus("current")


class _TacacsPlusServerRetransmit_Type(Integer32):
    """Custom type tacacsPlusServerRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TacacsPlusServerRetransmit_Type.__name__ = "Integer32"
_TacacsPlusServerRetransmit_Object = MibTableColumn
tacacsPlusServerRetransmit = _TacacsPlusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 4, 1, 9),
    _TacacsPlusServerRetransmit_Type()
)
tacacsPlusServerRetransmit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerRetransmit.setStatus("current")


class _TacacsPlusServerTimeout_Type(Integer32):
    """Custom type tacacsPlusServerTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 540),
    )


_TacacsPlusServerTimeout_Type.__name__ = "Integer32"
_TacacsPlusServerTimeout_Object = MibTableColumn
tacacsPlusServerTimeout = _TacacsPlusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 4, 1, 10),
    _TacacsPlusServerTimeout_Type()
)
tacacsPlusServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacacsPlusServerTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tacacsPlusServerTimeout.setUnits("seconds")


class _TacacsPlusServerGlobalRetransmit_Type(Integer32):
    """Custom type tacacsPlusServerGlobalRetransmit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_TacacsPlusServerGlobalRetransmit_Type.__name__ = "Integer32"
_TacacsPlusServerGlobalRetransmit_Object = MibScalar
tacacsPlusServerGlobalRetransmit = _TacacsPlusServerGlobalRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 5),
    _TacacsPlusServerGlobalRetransmit_Type()
)
tacacsPlusServerGlobalRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalRetransmit.setStatus("current")


class _TacacsPlusServerGlobalTimeout_Type(Integer32):
    """Custom type tacacsPlusServerGlobalTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 540),
    )


_TacacsPlusServerGlobalTimeout_Type.__name__ = "Integer32"
_TacacsPlusServerGlobalTimeout_Object = MibScalar
tacacsPlusServerGlobalTimeout = _TacacsPlusServerGlobalTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 5, 6),
    _TacacsPlusServerGlobalTimeout_Type()
)
tacacsPlusServerGlobalTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalTimeout.setStatus("current")
if mibBuilder.loadTexts:
    tacacsPlusServerGlobalTimeout.setUnits("seconds")
_SshMgt_ObjectIdentity = ObjectIdentity
sshMgt = _SshMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6)
)
_SshServerStatus_Type = EnabledStatus
_SshServerStatus_Object = MibScalar
sshServerStatus = _SshServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 1),
    _SshServerStatus_Type()
)
sshServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerStatus.setStatus("current")
_SshServerMajorVersion_Type = Integer32
_SshServerMajorVersion_Object = MibScalar
sshServerMajorVersion = _SshServerMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 2),
    _SshServerMajorVersion_Type()
)
sshServerMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMajorVersion.setStatus("current")
_SshServerMinorVersion_Type = Integer32
_SshServerMinorVersion_Object = MibScalar
sshServerMinorVersion = _SshServerMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 5),
    _SshAuthRetries_Type()
)
sshAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAuthRetries.setStatus("current")
_SshConnInfoTable_Object = MibTable
sshConnInfoTable = _SshConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 6)
)
if mibBuilder.loadTexts:
    sshConnInfoTable.setStatus("current")
_SshConnInfoEntry_Object = MibTableRow
sshConnInfoEntry = _SshConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 6, 1)
)
sshConnInfoEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "sshConnID"),
)
if mibBuilder.loadTexts:
    sshConnInfoEntry.setStatus("current")
_SshConnID_Type = Integer32
_SshConnID_Object = MibTableColumn
sshConnID = _SshConnID_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 6, 1, 1),
    _SshConnID_Type()
)
sshConnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshConnID.setStatus("current")
_SshConnMajorVersion_Type = Integer32
_SshConnMajorVersion_Object = MibTableColumn
sshConnMajorVersion = _SshConnMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 6, 1, 2),
    _SshConnMajorVersion_Type()
)
sshConnMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMajorVersion.setStatus("current")
_SshConnMinorVersion_Type = Integer32
_SshConnMinorVersion_Object = MibTableColumn
sshConnMinorVersion = _SshConnMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 6, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 6, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 6, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 6, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 7),
    _SshKeySize_Type()
)
sshKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshKeySize.setStatus("current")
_SshRsaHostKey1_Type = KeySegment
_SshRsaHostKey1_Object = MibScalar
sshRsaHostKey1 = _SshRsaHostKey1_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 8),
    _SshRsaHostKey1_Type()
)
sshRsaHostKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey1.setStatus("current")
_SshRsaHostKey2_Type = KeySegment
_SshRsaHostKey2_Object = MibScalar
sshRsaHostKey2 = _SshRsaHostKey2_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 9),
    _SshRsaHostKey2_Type()
)
sshRsaHostKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey2.setStatus("current")
_SshRsaHostKey3_Type = KeySegment
_SshRsaHostKey3_Object = MibScalar
sshRsaHostKey3 = _SshRsaHostKey3_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 10),
    _SshRsaHostKey3_Type()
)
sshRsaHostKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey3.setStatus("current")
_SshRsaHostKey4_Type = KeySegment
_SshRsaHostKey4_Object = MibScalar
sshRsaHostKey4 = _SshRsaHostKey4_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 11),
    _SshRsaHostKey4_Type()
)
sshRsaHostKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey4.setStatus("current")
_SshRsaHostKey5_Type = KeySegment
_SshRsaHostKey5_Object = MibScalar
sshRsaHostKey5 = _SshRsaHostKey5_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 12),
    _SshRsaHostKey5_Type()
)
sshRsaHostKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey5.setStatus("current")
_SshRsaHostKey6_Type = KeySegment
_SshRsaHostKey6_Object = MibScalar
sshRsaHostKey6 = _SshRsaHostKey6_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 13),
    _SshRsaHostKey6_Type()
)
sshRsaHostKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey6.setStatus("current")
_SshRsaHostKey7_Type = KeySegment
_SshRsaHostKey7_Object = MibScalar
sshRsaHostKey7 = _SshRsaHostKey7_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 14),
    _SshRsaHostKey7_Type()
)
sshRsaHostKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey7.setStatus("current")
_SshRsaHostKey8_Type = KeySegment
_SshRsaHostKey8_Object = MibScalar
sshRsaHostKey8 = _SshRsaHostKey8_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 15),
    _SshRsaHostKey8_Type()
)
sshRsaHostKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey8.setStatus("current")
_SshDsaHostKey1_Type = KeySegment
_SshDsaHostKey1_Object = MibScalar
sshDsaHostKey1 = _SshDsaHostKey1_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 16),
    _SshDsaHostKey1_Type()
)
sshDsaHostKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey1.setStatus("current")
_SshDsaHostKey2_Type = KeySegment
_SshDsaHostKey2_Object = MibScalar
sshDsaHostKey2 = _SshDsaHostKey2_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 17),
    _SshDsaHostKey2_Type()
)
sshDsaHostKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey2.setStatus("current")
_SshDsaHostKey3_Type = KeySegment
_SshDsaHostKey3_Object = MibScalar
sshDsaHostKey3 = _SshDsaHostKey3_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 18),
    _SshDsaHostKey3_Type()
)
sshDsaHostKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey3.setStatus("current")
_SshDsaHostKey4_Type = KeySegment
_SshDsaHostKey4_Object = MibScalar
sshDsaHostKey4 = _SshDsaHostKey4_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 19),
    _SshDsaHostKey4_Type()
)
sshDsaHostKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey4.setStatus("current")
_SshDsaHostKey5_Type = KeySegment
_SshDsaHostKey5_Object = MibScalar
sshDsaHostKey5 = _SshDsaHostKey5_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 20),
    _SshDsaHostKey5_Type()
)
sshDsaHostKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey5.setStatus("current")
_SshDsaHostKey6_Type = KeySegment
_SshDsaHostKey6_Object = MibScalar
sshDsaHostKey6 = _SshDsaHostKey6_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 21),
    _SshDsaHostKey6_Type()
)
sshDsaHostKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey6.setStatus("current")
_SshDsaHostKey7_Type = KeySegment
_SshDsaHostKey7_Object = MibScalar
sshDsaHostKey7 = _SshDsaHostKey7_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 22),
    _SshDsaHostKey7_Type()
)
sshDsaHostKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey7.setStatus("current")
_SshDsaHostKey8_Type = KeySegment
_SshDsaHostKey8_Object = MibScalar
sshDsaHostKey8 = _SshDsaHostKey8_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 23),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 24),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 25),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 26),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 27),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 28),
    _SshHostKeyDelAction_Type()
)
sshHostKeyDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyDelAction.setStatus("current")
_SshUserTable_Object = MibTable
sshUserTable = _SshUserTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29)
)
if mibBuilder.loadTexts:
    sshUserTable.setStatus("current")
_SshUserEntry_Object = MibTableRow
sshUserEntry = _SshUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1)
)
sshUserEntry.setIndexNames(
    (1, "ES3552M-AND-PoE-MIB", "sshUserName"),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 1),
    _SshUserName_Type()
)
sshUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshUserName.setStatus("current")
_SshUserRsaKey1_Type = KeySegment
_SshUserRsaKey1_Object = MibTableColumn
sshUserRsaKey1 = _SshUserRsaKey1_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 2),
    _SshUserRsaKey1_Type()
)
sshUserRsaKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey1.setStatus("current")
_SshUserRsaKey2_Type = KeySegment
_SshUserRsaKey2_Object = MibTableColumn
sshUserRsaKey2 = _SshUserRsaKey2_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 3),
    _SshUserRsaKey2_Type()
)
sshUserRsaKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey2.setStatus("current")
_SshUserRsaKey3_Type = KeySegment
_SshUserRsaKey3_Object = MibTableColumn
sshUserRsaKey3 = _SshUserRsaKey3_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 4),
    _SshUserRsaKey3_Type()
)
sshUserRsaKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey3.setStatus("current")
_SshUserRsaKey4_Type = KeySegment
_SshUserRsaKey4_Object = MibTableColumn
sshUserRsaKey4 = _SshUserRsaKey4_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 5),
    _SshUserRsaKey4_Type()
)
sshUserRsaKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey4.setStatus("current")
_SshUserRsaKey5_Type = KeySegment
_SshUserRsaKey5_Object = MibTableColumn
sshUserRsaKey5 = _SshUserRsaKey5_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 6),
    _SshUserRsaKey5_Type()
)
sshUserRsaKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey5.setStatus("current")
_SshUserRsaKey6_Type = KeySegment
_SshUserRsaKey6_Object = MibTableColumn
sshUserRsaKey6 = _SshUserRsaKey6_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 7),
    _SshUserRsaKey6_Type()
)
sshUserRsaKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey6.setStatus("current")
_SshUserRsaKey7_Type = KeySegment
_SshUserRsaKey7_Object = MibTableColumn
sshUserRsaKey7 = _SshUserRsaKey7_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 8),
    _SshUserRsaKey7_Type()
)
sshUserRsaKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey7.setStatus("current")
_SshUserRsaKey8_Type = KeySegment
_SshUserRsaKey8_Object = MibTableColumn
sshUserRsaKey8 = _SshUserRsaKey8_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 9),
    _SshUserRsaKey8_Type()
)
sshUserRsaKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey8.setStatus("current")
_SshUserDsaKey1_Type = KeySegment
_SshUserDsaKey1_Object = MibTableColumn
sshUserDsaKey1 = _SshUserDsaKey1_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 10),
    _SshUserDsaKey1_Type()
)
sshUserDsaKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey1.setStatus("current")
_SshUserDsaKey2_Type = KeySegment
_SshUserDsaKey2_Object = MibTableColumn
sshUserDsaKey2 = _SshUserDsaKey2_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 11),
    _SshUserDsaKey2_Type()
)
sshUserDsaKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey2.setStatus("current")
_SshUserDsaKey3_Type = KeySegment
_SshUserDsaKey3_Object = MibTableColumn
sshUserDsaKey3 = _SshUserDsaKey3_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 12),
    _SshUserDsaKey3_Type()
)
sshUserDsaKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey3.setStatus("current")
_SshUserDsaKey4_Type = KeySegment
_SshUserDsaKey4_Object = MibTableColumn
sshUserDsaKey4 = _SshUserDsaKey4_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 13),
    _SshUserDsaKey4_Type()
)
sshUserDsaKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey4.setStatus("current")
_SshUserDsaKey5_Type = KeySegment
_SshUserDsaKey5_Object = MibTableColumn
sshUserDsaKey5 = _SshUserDsaKey5_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 14),
    _SshUserDsaKey5_Type()
)
sshUserDsaKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey5.setStatus("current")
_SshUserDsaKey6_Type = KeySegment
_SshUserDsaKey6_Object = MibTableColumn
sshUserDsaKey6 = _SshUserDsaKey6_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 15),
    _SshUserDsaKey6_Type()
)
sshUserDsaKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey6.setStatus("current")
_SshUserDsaKey7_Type = KeySegment
_SshUserDsaKey7_Object = MibTableColumn
sshUserDsaKey7 = _SshUserDsaKey7_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 16),
    _SshUserDsaKey7_Type()
)
sshUserDsaKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey7.setStatus("current")
_SshUserDsaKey8_Type = KeySegment
_SshUserDsaKey8_Object = MibTableColumn
sshUserDsaKey8 = _SshUserDsaKey8_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 29, 1, 18),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 30),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 31),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 32),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 6, 33),
    _SshDsaHostKeyMD5FingerPrint_Type()
)
sshDsaHostKeyMD5FingerPrint.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKeyMD5FingerPrint.setStatus("current")
_IpFilterMgt_ObjectIdentity = ObjectIdentity
ipFilterMgt = _IpFilterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9)
)
_IpFilterSnmpTable_Object = MibTable
ipFilterSnmpTable = _IpFilterSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 1)
)
if mibBuilder.loadTexts:
    ipFilterSnmpTable.setStatus("current")
_IpFilterSnmpEntry_Object = MibTableRow
ipFilterSnmpEntry = _IpFilterSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 1, 1)
)
ipFilterSnmpEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "ipFilterSnmpStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterSnmpEntry.setStatus("current")
_IpFilterSnmpStartAddress_Type = IpAddress
_IpFilterSnmpStartAddress_Object = MibTableColumn
ipFilterSnmpStartAddress = _IpFilterSnmpStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 1, 1, 1),
    _IpFilterSnmpStartAddress_Type()
)
ipFilterSnmpStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterSnmpStartAddress.setStatus("current")
_IpFilterSnmpEndAddress_Type = IpAddress
_IpFilterSnmpEndAddress_Object = MibTableColumn
ipFilterSnmpEndAddress = _IpFilterSnmpEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 1, 1, 2),
    _IpFilterSnmpEndAddress_Type()
)
ipFilterSnmpEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpEndAddress.setStatus("current")
_IpFilterSnmpStatus_Type = ValidStatus
_IpFilterSnmpStatus_Object = MibTableColumn
ipFilterSnmpStatus = _IpFilterSnmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 1, 1, 3),
    _IpFilterSnmpStatus_Type()
)
ipFilterSnmpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpStatus.setStatus("current")
_IpFilterHTTPTable_Object = MibTable
ipFilterHTTPTable = _IpFilterHTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 2)
)
if mibBuilder.loadTexts:
    ipFilterHTTPTable.setStatus("current")
_IpFilterHTTPEntry_Object = MibTableRow
ipFilterHTTPEntry = _IpFilterHTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 2, 1)
)
ipFilterHTTPEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "ipFilterHTTPStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterHTTPEntry.setStatus("current")
_IpFilterHTTPStartAddress_Type = IpAddress
_IpFilterHTTPStartAddress_Object = MibTableColumn
ipFilterHTTPStartAddress = _IpFilterHTTPStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 2, 1, 1),
    _IpFilterHTTPStartAddress_Type()
)
ipFilterHTTPStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterHTTPStartAddress.setStatus("current")
_IpFilterHTTPEndAddress_Type = IpAddress
_IpFilterHTTPEndAddress_Object = MibTableColumn
ipFilterHTTPEndAddress = _IpFilterHTTPEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 2, 1, 2),
    _IpFilterHTTPEndAddress_Type()
)
ipFilterHTTPEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHTTPEndAddress.setStatus("current")
_IpFilterHTTPStatus_Type = ValidStatus
_IpFilterHTTPStatus_Object = MibTableColumn
ipFilterHTTPStatus = _IpFilterHTTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 2, 1, 3),
    _IpFilterHTTPStatus_Type()
)
ipFilterHTTPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHTTPStatus.setStatus("current")
_IpFilterTelnetTable_Object = MibTable
ipFilterTelnetTable = _IpFilterTelnetTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 3)
)
if mibBuilder.loadTexts:
    ipFilterTelnetTable.setStatus("current")
_IpFilterTelnetEntry_Object = MibTableRow
ipFilterTelnetEntry = _IpFilterTelnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 3, 1)
)
ipFilterTelnetEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "ipFilterTelnetStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterTelnetEntry.setStatus("current")
_IpFilterTelnetStartAddress_Type = IpAddress
_IpFilterTelnetStartAddress_Object = MibTableColumn
ipFilterTelnetStartAddress = _IpFilterTelnetStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 3, 1, 1),
    _IpFilterTelnetStartAddress_Type()
)
ipFilterTelnetStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterTelnetStartAddress.setStatus("current")
_IpFilterTelnetEndAddress_Type = IpAddress
_IpFilterTelnetEndAddress_Object = MibTableColumn
ipFilterTelnetEndAddress = _IpFilterTelnetEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 3, 1, 2),
    _IpFilterTelnetEndAddress_Type()
)
ipFilterTelnetEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetEndAddress.setStatus("current")
_IpFilterTelnetStatus_Type = ValidStatus
_IpFilterTelnetStatus_Object = MibTableColumn
ipFilterTelnetStatus = _IpFilterTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 9, 3, 1, 3),
    _IpFilterTelnetStatus_Type()
)
ipFilterTelnetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetStatus.setStatus("current")
_Dot1xMgt_ObjectIdentity = ObjectIdentity
dot1xMgt = _Dot1xMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11)
)
_Dot1xAuthConfigExtTable_Object = MibTable
dot1xAuthConfigExtTable = _Dot1xAuthConfigExtTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 1)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigExtTable.setStatus("current")
_Dot1xAuthConfigExtEntry_Object = MibTableRow
dot1xAuthConfigExtEntry = _Dot1xAuthConfigExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 1, 1)
)
if mibBuilder.loadTexts:
    dot1xAuthConfigExtEntry.setStatus("current")


class _Dot1xAuthConfigExtOperMode_Type(Integer32):
    """Custom type dot1xAuthConfigExtOperMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("singleHost", 1),
          ("multiHost", 2),
          ("macBasedAuth", 3))
    )


_Dot1xAuthConfigExtOperMode_Type.__name__ = "Integer32"
_Dot1xAuthConfigExtOperMode_Object = MibTableColumn
dot1xAuthConfigExtOperMode = _Dot1xAuthConfigExtOperMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 1, 1, 1),
    _Dot1xAuthConfigExtOperMode_Type()
)
dot1xAuthConfigExtOperMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthConfigExtOperMode.setStatus("current")


class _Dot1xAuthConfigExtMultiHostMaxCnt_Type(Integer32):
    """Custom type dot1xAuthConfigExtMultiHostMaxCnt based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1024),
    )


_Dot1xAuthConfigExtMultiHostMaxCnt_Type.__name__ = "Integer32"
_Dot1xAuthConfigExtMultiHostMaxCnt_Object = MibTableColumn
dot1xAuthConfigExtMultiHostMaxCnt = _Dot1xAuthConfigExtMultiHostMaxCnt_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 1, 1, 2),
    _Dot1xAuthConfigExtMultiHostMaxCnt_Type()
)
dot1xAuthConfigExtMultiHostMaxCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthConfigExtMultiHostMaxCnt.setStatus("current")


class _Dot1xAuthConfigExtPortIntrusionAction_Type(Integer32):
    """Custom type dot1xAuthConfigExtPortIntrusionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block-traffic", 1),
          ("guest-vlan", 2))
    )


_Dot1xAuthConfigExtPortIntrusionAction_Type.__name__ = "Integer32"
_Dot1xAuthConfigExtPortIntrusionAction_Object = MibTableColumn
dot1xAuthConfigExtPortIntrusionAction = _Dot1xAuthConfigExtPortIntrusionAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 1, 1, 3),
    _Dot1xAuthConfigExtPortIntrusionAction_Type()
)
dot1xAuthConfigExtPortIntrusionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xAuthConfigExtPortIntrusionAction.setStatus("current")
_Dot1xSuppMgt_ObjectIdentity = ObjectIdentity
dot1xSuppMgt = _Dot1xSuppMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 2)
)


class _Dot1xSuppUserName_Type(DisplayString):
    """Custom type dot1xSuppUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Dot1xSuppUserName_Type.__name__ = "DisplayString"
_Dot1xSuppUserName_Object = MibScalar
dot1xSuppUserName = _Dot1xSuppUserName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 2, 1),
    _Dot1xSuppUserName_Type()
)
dot1xSuppUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xSuppUserName.setStatus("current")


class _Dot1xSuppPassword_Type(DisplayString):
    """Custom type dot1xSuppPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_Dot1xSuppPassword_Type.__name__ = "DisplayString"
_Dot1xSuppPassword_Object = MibScalar
dot1xSuppPassword = _Dot1xSuppPassword_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 2, 2),
    _Dot1xSuppPassword_Type()
)
dot1xSuppPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xSuppPassword.setStatus("current")
_Dot1xSuppConfigPortTable_Object = MibTable
dot1xSuppConfigPortTable = _Dot1xSuppConfigPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 2, 3)
)
if mibBuilder.loadTexts:
    dot1xSuppConfigPortTable.setStatus("current")
_Dot1xSuppConfigPortEntry_Object = MibTableRow
dot1xSuppConfigPortEntry = _Dot1xSuppConfigPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 2, 3, 1)
)
dot1xSuppConfigPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "dot1xSuppConfigPortIndex"),
)
if mibBuilder.loadTexts:
    dot1xSuppConfigPortEntry.setStatus("current")
_Dot1xSuppConfigPortIndex_Type = Integer32
_Dot1xSuppConfigPortIndex_Object = MibTableColumn
dot1xSuppConfigPortIndex = _Dot1xSuppConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 2, 3, 1, 1),
    _Dot1xSuppConfigPortIndex_Type()
)
dot1xSuppConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dot1xSuppConfigPortIndex.setStatus("current")
_Dot1xSuppConfigPortStatus_Type = EnabledStatus
_Dot1xSuppConfigPortStatus_Object = MibTableColumn
dot1xSuppConfigPortStatus = _Dot1xSuppConfigPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 2, 3, 1, 2),
    _Dot1xSuppConfigPortStatus_Type()
)
dot1xSuppConfigPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xSuppConfigPortStatus.setStatus("current")


class _Dot1xEapolPassThrough_Type(EnabledStatus):
    """Custom type dot1xEapolPassThrough based on EnabledStatus"""
    defaultValue = 2


_Dot1xEapolPassThrough_Type.__name__ = "EnabledStatus"
_Dot1xEapolPassThrough_Object = MibScalar
dot1xEapolPassThrough = _Dot1xEapolPassThrough_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 11, 3),
    _Dot1xEapolPassThrough_Type()
)
dot1xEapolPassThrough.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dot1xEapolPassThrough.setStatus("current")
_AaaMgt_ObjectIdentity = ObjectIdentity
aaaMgt = _AaaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12)
)
_AaaMethodTable_Object = MibTable
aaaMethodTable = _AaaMethodTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 1)
)
if mibBuilder.loadTexts:
    aaaMethodTable.setStatus("current")
_AaaMethodEntry_Object = MibTableRow
aaaMethodEntry = _AaaMethodEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 1, 1)
)
aaaMethodEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "aaaMethodIndex"),
)
if mibBuilder.loadTexts:
    aaaMethodEntry.setStatus("current")
_AaaMethodIndex_Type = Integer32
_AaaMethodIndex_Object = MibTableColumn
aaaMethodIndex = _AaaMethodIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 1, 1, 1),
    _AaaMethodIndex_Type()
)
aaaMethodIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaMethodIndex.setStatus("current")


class _AaaMethodName_Type(DisplayString):
    """Custom type aaaMethodName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AaaMethodName_Type.__name__ = "DisplayString"
_AaaMethodName_Object = MibTableColumn
aaaMethodName = _AaaMethodName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 1, 1, 2),
    _AaaMethodName_Type()
)
aaaMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodName.setStatus("current")


class _AaaMethodGroupName_Type(DisplayString):
    """Custom type aaaMethodGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AaaMethodGroupName_Type.__name__ = "DisplayString"
_AaaMethodGroupName_Object = MibTableColumn
aaaMethodGroupName = _AaaMethodGroupName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 1, 1, 3),
    _AaaMethodGroupName_Type()
)
aaaMethodGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodGroupName.setStatus("current")


class _AaaMethodMode_Type(Integer32):
    """Custom type aaaMethodMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start-stop", 1)
    )


_AaaMethodMode_Type.__name__ = "Integer32"
_AaaMethodMode_Object = MibTableColumn
aaaMethodMode = _AaaMethodMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 1, 1, 4),
    _AaaMethodMode_Type()
)
aaaMethodMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodMode.setStatus("current")
_AaaMethodStatus_Type = ValidStatus
_AaaMethodStatus_Object = MibTableColumn
aaaMethodStatus = _AaaMethodStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 1, 1, 5),
    _AaaMethodStatus_Type()
)
aaaMethodStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodStatus.setStatus("current")


class _AaaMethodClientType_Type(Integer32):
    """Custom type aaaMethodClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dot1x", 1),
          ("exec", 2),
          ("commands", 3))
    )


_AaaMethodClientType_Type.__name__ = "Integer32"
_AaaMethodClientType_Object = MibTableColumn
aaaMethodClientType = _AaaMethodClientType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 1, 1, 6),
    _AaaMethodClientType_Type()
)
aaaMethodClientType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodClientType.setStatus("current")


class _AaaMethodPrivilegeLevel_Type(Integer32):
    """Custom type aaaMethodPrivilegeLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AaaMethodPrivilegeLevel_Type.__name__ = "Integer32"
_AaaMethodPrivilegeLevel_Object = MibTableColumn
aaaMethodPrivilegeLevel = _AaaMethodPrivilegeLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 1, 1, 7),
    _AaaMethodPrivilegeLevel_Type()
)
aaaMethodPrivilegeLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaMethodPrivilegeLevel.setStatus("current")
_AaaRadiusGroupTable_Object = MibTable
aaaRadiusGroupTable = _AaaRadiusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 2)
)
if mibBuilder.loadTexts:
    aaaRadiusGroupTable.setStatus("current")
_AaaRadiusGroupEntry_Object = MibTableRow
aaaRadiusGroupEntry = _AaaRadiusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 2, 1)
)
aaaRadiusGroupEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "aaaRadiusGroupIndex"),
)
if mibBuilder.loadTexts:
    aaaRadiusGroupEntry.setStatus("current")
_AaaRadiusGroupIndex_Type = Integer32
_AaaRadiusGroupIndex_Object = MibTableColumn
aaaRadiusGroupIndex = _AaaRadiusGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 2, 1, 1),
    _AaaRadiusGroupIndex_Type()
)
aaaRadiusGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaRadiusGroupIndex.setStatus("current")


class _AaaRadiusGroupServerBitMap_Type(OctetString):
    """Custom type aaaRadiusGroupServerBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_AaaRadiusGroupServerBitMap_Type.__name__ = "OctetString"
_AaaRadiusGroupServerBitMap_Object = MibTableColumn
aaaRadiusGroupServerBitMap = _AaaRadiusGroupServerBitMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 2, 1, 2),
    _AaaRadiusGroupServerBitMap_Type()
)
aaaRadiusGroupServerBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaRadiusGroupServerBitMap.setStatus("current")
_AaaRadiusGroupName_Type = DisplayString
_AaaRadiusGroupName_Object = MibTableColumn
aaaRadiusGroupName = _AaaRadiusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 2, 1, 3),
    _AaaRadiusGroupName_Type()
)
aaaRadiusGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaRadiusGroupName.setStatus("current")
_AaaRadiusGroupStatus_Type = ValidStatus
_AaaRadiusGroupStatus_Object = MibTableColumn
aaaRadiusGroupStatus = _AaaRadiusGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 2, 1, 4),
    _AaaRadiusGroupStatus_Type()
)
aaaRadiusGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaRadiusGroupStatus.setStatus("current")
_AaaTacacsPlusGroupTable_Object = MibTable
aaaTacacsPlusGroupTable = _AaaTacacsPlusGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 3)
)
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupTable.setStatus("current")
_AaaTacacsPlusGroupEntry_Object = MibTableRow
aaaTacacsPlusGroupEntry = _AaaTacacsPlusGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 3, 1)
)
aaaTacacsPlusGroupEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "aaaTacacsPlusGroupIndex"),
)
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupEntry.setStatus("current")
_AaaTacacsPlusGroupIndex_Type = Integer32
_AaaTacacsPlusGroupIndex_Object = MibTableColumn
aaaTacacsPlusGroupIndex = _AaaTacacsPlusGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 3, 1, 1),
    _AaaTacacsPlusGroupIndex_Type()
)
aaaTacacsPlusGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupIndex.setStatus("current")


class _AaaTacacsPlusGroupServerBitMap_Type(OctetString):
    """Custom type aaaTacacsPlusGroupServerBitMap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_AaaTacacsPlusGroupServerBitMap_Type.__name__ = "OctetString"
_AaaTacacsPlusGroupServerBitMap_Object = MibTableColumn
aaaTacacsPlusGroupServerBitMap = _AaaTacacsPlusGroupServerBitMap_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 3, 1, 2),
    _AaaTacacsPlusGroupServerBitMap_Type()
)
aaaTacacsPlusGroupServerBitMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupServerBitMap.setStatus("current")
_AaaTacacsPlusGroupName_Type = DisplayString
_AaaTacacsPlusGroupName_Object = MibTableColumn
aaaTacacsPlusGroupName = _AaaTacacsPlusGroupName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 3, 1, 3),
    _AaaTacacsPlusGroupName_Type()
)
aaaTacacsPlusGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupName.setStatus("current")
_AaaTacacsPlusGroupStatus_Type = ValidStatus
_AaaTacacsPlusGroupStatus_Object = MibTableColumn
aaaTacacsPlusGroupStatus = _AaaTacacsPlusGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 3, 1, 4),
    _AaaTacacsPlusGroupStatus_Type()
)
aaaTacacsPlusGroupStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaTacacsPlusGroupStatus.setStatus("current")


class _AaaUpdate_Type(Integer32):
    """Custom type aaaUpdate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AaaUpdate_Type.__name__ = "Integer32"
_AaaUpdate_Object = MibScalar
aaaUpdate = _AaaUpdate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 4),
    _AaaUpdate_Type()
)
aaaUpdate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aaaUpdate.setStatus("current")
_AaaAccountTable_Object = MibTable
aaaAccountTable = _AaaAccountTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 5)
)
if mibBuilder.loadTexts:
    aaaAccountTable.setStatus("current")
_AaaAccountEntry_Object = MibTableRow
aaaAccountEntry = _AaaAccountEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 5, 1)
)
aaaAccountEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "aaaAccountIfIndex"),
)
if mibBuilder.loadTexts:
    aaaAccountEntry.setStatus("current")
_AaaAccountIfIndex_Type = Integer32
_AaaAccountIfIndex_Object = MibTableColumn
aaaAccountIfIndex = _AaaAccountIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 5, 1, 1),
    _AaaAccountIfIndex_Type()
)
aaaAccountIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaAccountIfIndex.setStatus("current")
_AaaAccountMethodName_Type = DisplayString
_AaaAccountMethodName_Object = MibTableColumn
aaaAccountMethodName = _AaaAccountMethodName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 5, 1, 2),
    _AaaAccountMethodName_Type()
)
aaaAccountMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAccountMethodName.setStatus("current")
_AaaAccountProtocol_Type = Integer32
_AaaAccountProtocol_Object = MibTableColumn
aaaAccountProtocol = _AaaAccountProtocol_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 5, 1, 3),
    _AaaAccountProtocol_Type()
)
aaaAccountProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aaaAccountProtocol.setStatus("current")
_AaaAccountStatus_Type = ValidStatus
_AaaAccountStatus_Object = MibTableColumn
aaaAccountStatus = _AaaAccountStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 5, 1, 4),
    _AaaAccountStatus_Type()
)
aaaAccountStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAccountStatus.setStatus("current")
_AaaCommandPrivilegesTable_Object = MibTable
aaaCommandPrivilegesTable = _AaaCommandPrivilegesTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 8)
)
if mibBuilder.loadTexts:
    aaaCommandPrivilegesTable.setStatus("current")
_AaaCommandPrivilegesEntry_Object = MibTableRow
aaaCommandPrivilegesEntry = _AaaCommandPrivilegesEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 8, 1)
)
aaaCommandPrivilegesEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "aaaCommandPrivilegesLevel"),
    (0, "ES3552M-AND-PoE-MIB", "aaaCommandPrivilegesInterfaceIndex"),
)
if mibBuilder.loadTexts:
    aaaCommandPrivilegesEntry.setStatus("current")


class _AaaCommandPrivilegesLevel_Type(Integer32):
    """Custom type aaaCommandPrivilegesLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AaaCommandPrivilegesLevel_Type.__name__ = "Integer32"
_AaaCommandPrivilegesLevel_Object = MibTableColumn
aaaCommandPrivilegesLevel = _AaaCommandPrivilegesLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 8, 1, 1),
    _AaaCommandPrivilegesLevel_Type()
)
aaaCommandPrivilegesLevel.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaCommandPrivilegesLevel.setStatus("current")


class _AaaCommandPrivilegesInterfaceIndex_Type(Integer32):
    """Custom type aaaCommandPrivilegesInterfaceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("vty", 2))
    )


_AaaCommandPrivilegesInterfaceIndex_Type.__name__ = "Integer32"
_AaaCommandPrivilegesInterfaceIndex_Object = MibTableColumn
aaaCommandPrivilegesInterfaceIndex = _AaaCommandPrivilegesInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 8, 1, 2),
    _AaaCommandPrivilegesInterfaceIndex_Type()
)
aaaCommandPrivilegesInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaCommandPrivilegesInterfaceIndex.setStatus("current")


class _AaaCommandPrivilegesMethodName_Type(DisplayString):
    """Custom type aaaCommandPrivilegesMethodName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AaaCommandPrivilegesMethodName_Type.__name__ = "DisplayString"
_AaaCommandPrivilegesMethodName_Object = MibTableColumn
aaaCommandPrivilegesMethodName = _AaaCommandPrivilegesMethodName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 8, 1, 3),
    _AaaCommandPrivilegesMethodName_Type()
)
aaaCommandPrivilegesMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaCommandPrivilegesMethodName.setStatus("current")
_AaaAccExecTable_Object = MibTable
aaaAccExecTable = _AaaAccExecTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 9)
)
if mibBuilder.loadTexts:
    aaaAccExecTable.setStatus("current")
_AaaAccExecEntry_Object = MibTableRow
aaaAccExecEntry = _AaaAccExecEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 9, 1)
)
aaaAccExecEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "aaaAccExecIndex"),
)
if mibBuilder.loadTexts:
    aaaAccExecEntry.setStatus("current")


class _AaaAccExecIndex_Type(Integer32):
    """Custom type aaaAccExecIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("console", 1),
          ("vty", 2))
    )


_AaaAccExecIndex_Type.__name__ = "Integer32"
_AaaAccExecIndex_Object = MibTableColumn
aaaAccExecIndex = _AaaAccExecIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 9, 1, 1),
    _AaaAccExecIndex_Type()
)
aaaAccExecIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aaaAccExecIndex.setStatus("current")
_AaaAccExecMethodName_Type = DisplayString
_AaaAccExecMethodName_Object = MibTableColumn
aaaAccExecMethodName = _AaaAccExecMethodName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 12, 9, 1, 2),
    _AaaAccExecMethodName_Type()
)
aaaAccExecMethodName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aaaAccExecMethodName.setStatus("current")
_NetworkAccessMgt_ObjectIdentity = ObjectIdentity
networkAccessMgt = _NetworkAccessMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13)
)
_NetworkAccessPortTable_Object = MibTable
networkAccessPortTable = _NetworkAccessPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2)
)
if mibBuilder.loadTexts:
    networkAccessPortTable.setStatus("current")
_NetworkAccessPortEntry_Object = MibTableRow
networkAccessPortEntry = _NetworkAccessPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2, 1)
)
networkAccessPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "networkAccessPortPortIndex"),
)
if mibBuilder.loadTexts:
    networkAccessPortEntry.setStatus("current")
_NetworkAccessPortPortIndex_Type = Integer32
_NetworkAccessPortPortIndex_Object = MibTableColumn
networkAccessPortPortIndex = _NetworkAccessPortPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2, 1, 1),
    _NetworkAccessPortPortIndex_Type()
)
networkAccessPortPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessPortPortIndex.setStatus("current")


class _NetworkAccessPortMaxMacCount_Type(Integer32):
    """Custom type networkAccessPortMaxMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_NetworkAccessPortMaxMacCount_Type.__name__ = "Integer32"
_NetworkAccessPortMaxMacCount_Object = MibTableColumn
networkAccessPortMaxMacCount = _NetworkAccessPortMaxMacCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2, 1, 3),
    _NetworkAccessPortMaxMacCount_Type()
)
networkAccessPortMaxMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortMaxMacCount.setStatus("current")
_NetworkAccessPortMode_Type = EnabledStatus
_NetworkAccessPortMode_Object = MibTableColumn
networkAccessPortMode = _NetworkAccessPortMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2, 1, 4),
    _NetworkAccessPortMode_Type()
)
networkAccessPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortMode.setStatus("current")


class _NetworkAccessPortMacFilter_Type(Integer32):
    """Custom type networkAccessPortMacFilter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_NetworkAccessPortMacFilter_Type.__name__ = "Integer32"
_NetworkAccessPortMacFilter_Object = MibTableColumn
networkAccessPortMacFilter = _NetworkAccessPortMacFilter_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2, 1, 5),
    _NetworkAccessPortMacFilter_Type()
)
networkAccessPortMacFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortMacFilter.setStatus("current")


class _NetworkAccessPortGuestVlan_Type(Integer32):
    """Custom type networkAccessPortGuestVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_NetworkAccessPortGuestVlan_Type.__name__ = "Integer32"
_NetworkAccessPortGuestVlan_Object = MibTableColumn
networkAccessPortGuestVlan = _NetworkAccessPortGuestVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2, 1, 6),
    _NetworkAccessPortGuestVlan_Type()
)
networkAccessPortGuestVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortGuestVlan.setStatus("current")
_NetworkAccessPortLinkDetectionStatus_Type = EnabledStatus
_NetworkAccessPortLinkDetectionStatus_Object = MibTableColumn
networkAccessPortLinkDetectionStatus = _NetworkAccessPortLinkDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2, 1, 7),
    _NetworkAccessPortLinkDetectionStatus_Type()
)
networkAccessPortLinkDetectionStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortLinkDetectionStatus.setStatus("current")


class _NetworkAccessPortLinkDetectionMode_Type(Integer32):
    """Custom type networkAccessPortLinkDetectionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("linkUp", 1),
          ("linkDown", 2),
          ("linkUpDown", 3))
    )


_NetworkAccessPortLinkDetectionMode_Type.__name__ = "Integer32"
_NetworkAccessPortLinkDetectionMode_Object = MibTableColumn
networkAccessPortLinkDetectionMode = _NetworkAccessPortLinkDetectionMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2, 1, 8),
    _NetworkAccessPortLinkDetectionMode_Type()
)
networkAccessPortLinkDetectionMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortLinkDetectionMode.setStatus("current")


class _NetworkAccessPortLinkDetectionAciton_Type(Integer32):
    """Custom type networkAccessPortLinkDetectionAciton based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("trap", 1),
          ("shutDown", 2),
          ("trapAndShutDown", 3))
    )


_NetworkAccessPortLinkDetectionAciton_Type.__name__ = "Integer32"
_NetworkAccessPortLinkDetectionAciton_Object = MibTableColumn
networkAccessPortLinkDetectionAciton = _NetworkAccessPortLinkDetectionAciton_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2, 1, 9),
    _NetworkAccessPortLinkDetectionAciton_Type()
)
networkAccessPortLinkDetectionAciton.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortLinkDetectionAciton.setStatus("current")
_NetworkAccessPortDynamicQos_Type = EnabledStatus
_NetworkAccessPortDynamicQos_Object = MibTableColumn
networkAccessPortDynamicQos = _NetworkAccessPortDynamicQos_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 2, 1, 10),
    _NetworkAccessPortDynamicQos_Type()
)
networkAccessPortDynamicQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessPortDynamicQos.setStatus("current")
_NetworkAccessClearMacAddressMgt_ObjectIdentity = ObjectIdentity
networkAccessClearMacAddressMgt = _NetworkAccessClearMacAddressMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 3)
)


class _NetworkAccessClearMacAddressAttribute_Type(Integer32):
    """Custom type networkAccessClearMacAddressAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("static", 2),
          ("dynamic", 3))
    )


_NetworkAccessClearMacAddressAttribute_Type.__name__ = "Integer32"
_NetworkAccessClearMacAddressAttribute_Object = MibScalar
networkAccessClearMacAddressAttribute = _NetworkAccessClearMacAddressAttribute_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 3, 1),
    _NetworkAccessClearMacAddressAttribute_Type()
)
networkAccessClearMacAddressAttribute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessClearMacAddressAttribute.setStatus("current")
_NetworkAccessClearMacAddressMacAddress_Type = MacAddress
_NetworkAccessClearMacAddressMacAddress_Object = MibScalar
networkAccessClearMacAddressMacAddress = _NetworkAccessClearMacAddressMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 3, 2),
    _NetworkAccessClearMacAddressMacAddress_Type()
)
networkAccessClearMacAddressMacAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessClearMacAddressMacAddress.setStatus("current")
_NetworkAccessClearMacAddressPort_Type = Integer32
_NetworkAccessClearMacAddressPort_Object = MibScalar
networkAccessClearMacAddressPort = _NetworkAccessClearMacAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 3, 3),
    _NetworkAccessClearMacAddressPort_Type()
)
networkAccessClearMacAddressPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessClearMacAddressPort.setStatus("current")


class _NetworkAccessClearMacAddressAction_Type(Integer32):
    """Custom type networkAccessClearMacAddressAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noclear", 1),
          ("clear", 2))
    )


_NetworkAccessClearMacAddressAction_Type.__name__ = "Integer32"
_NetworkAccessClearMacAddressAction_Object = MibScalar
networkAccessClearMacAddressAction = _NetworkAccessClearMacAddressAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 3, 4),
    _NetworkAccessClearMacAddressAction_Type()
)
networkAccessClearMacAddressAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessClearMacAddressAction.setStatus("current")
_NetworkAccessMacAddressTable_Object = MibTable
networkAccessMacAddressTable = _NetworkAccessMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 4)
)
if mibBuilder.loadTexts:
    networkAccessMacAddressTable.setStatus("current")
_NetworkAccessMacAddressEntry_Object = MibTableRow
networkAccessMacAddressEntry = _NetworkAccessMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 4, 1)
)
networkAccessMacAddressEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "networkAccessMacAddressAddress"),
    (0, "ES3552M-AND-PoE-MIB", "networkAccessMacAddressPort"),
)
if mibBuilder.loadTexts:
    networkAccessMacAddressEntry.setStatus("current")
_NetworkAccessMacAddressAddress_Type = MacAddress
_NetworkAccessMacAddressAddress_Object = MibTableColumn
networkAccessMacAddressAddress = _NetworkAccessMacAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 4, 1, 1),
    _NetworkAccessMacAddressAddress_Type()
)
networkAccessMacAddressAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessMacAddressAddress.setStatus("current")
_NetworkAccessMacAddressPort_Type = Integer32
_NetworkAccessMacAddressPort_Object = MibTableColumn
networkAccessMacAddressPort = _NetworkAccessMacAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 4, 1, 2),
    _NetworkAccessMacAddressPort_Type()
)
networkAccessMacAddressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessMacAddressPort.setStatus("current")
_NetworkAccessMacAddressInetAddressType_Type = InetAddressType
_NetworkAccessMacAddressInetAddressType_Object = MibTableColumn
networkAccessMacAddressInetAddressType = _NetworkAccessMacAddressInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 4, 1, 3),
    _NetworkAccessMacAddressInetAddressType_Type()
)
networkAccessMacAddressInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAccessMacAddressInetAddressType.setStatus("current")
_NetworkAccessMacAddressRadiusServerInetAddress_Type = InetAddress
_NetworkAccessMacAddressRadiusServerInetAddress_Object = MibTableColumn
networkAccessMacAddressRadiusServerInetAddress = _NetworkAccessMacAddressRadiusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 4, 1, 4),
    _NetworkAccessMacAddressRadiusServerInetAddress_Type()
)
networkAccessMacAddressRadiusServerInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAccessMacAddressRadiusServerInetAddress.setStatus("current")


class _NetworkAccessMacAddressTime_Type(DisplayString):
    """Custom type networkAccessMacAddressTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12


_NetworkAccessMacAddressTime_Type.__name__ = "DisplayString"
_NetworkAccessMacAddressTime_Object = MibTableColumn
networkAccessMacAddressTime = _NetworkAccessMacAddressTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 4, 1, 5),
    _NetworkAccessMacAddressTime_Type()
)
networkAccessMacAddressTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAccessMacAddressTime.setStatus("current")


class _NetworkAccessMacAddressAttribute_Type(Integer32):
    """Custom type networkAccessMacAddressAttribute based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_NetworkAccessMacAddressAttribute_Type.__name__ = "Integer32"
_NetworkAccessMacAddressAttribute_Object = MibTableColumn
networkAccessMacAddressAttribute = _NetworkAccessMacAddressAttribute_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 4, 1, 6),
    _NetworkAccessMacAddressAttribute_Type()
)
networkAccessMacAddressAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    networkAccessMacAddressAttribute.setStatus("current")
_NetworkAccessAging_Type = EnabledStatus
_NetworkAccessAging_Object = MibScalar
networkAccessAging = _NetworkAccessAging_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 5),
    _NetworkAccessAging_Type()
)
networkAccessAging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    networkAccessAging.setStatus("current")
_NetworkAccessMacFilterWithMaskTable_Object = MibTable
networkAccessMacFilterWithMaskTable = _NetworkAccessMacFilterWithMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 6)
)
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskTable.setStatus("current")
_NetworkAccessMacFilterWithMaskEntry_Object = MibTableRow
networkAccessMacFilterWithMaskEntry = _NetworkAccessMacFilterWithMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 6, 1)
)
networkAccessMacFilterWithMaskEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "networkAccessMacFilterWithMaskID"),
    (0, "ES3552M-AND-PoE-MIB", "networkAccessMacFilterWithMaskMacAddress"),
    (0, "ES3552M-AND-PoE-MIB", "networkAccessMacFilterWithMaskMacAddressMask"),
)
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskEntry.setStatus("current")
_NetworkAccessMacFilterWithMaskID_Type = Integer32
_NetworkAccessMacFilterWithMaskID_Object = MibTableColumn
networkAccessMacFilterWithMaskID = _NetworkAccessMacFilterWithMaskID_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 6, 1, 1),
    _NetworkAccessMacFilterWithMaskID_Type()
)
networkAccessMacFilterWithMaskID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskID.setStatus("current")
_NetworkAccessMacFilterWithMaskMacAddress_Type = MacAddress
_NetworkAccessMacFilterWithMaskMacAddress_Object = MibTableColumn
networkAccessMacFilterWithMaskMacAddress = _NetworkAccessMacFilterWithMaskMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 6, 1, 2),
    _NetworkAccessMacFilterWithMaskMacAddress_Type()
)
networkAccessMacFilterWithMaskMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskMacAddress.setStatus("current")
_NetworkAccessMacFilterWithMaskMacAddressMask_Type = MacAddress
_NetworkAccessMacFilterWithMaskMacAddressMask_Object = MibTableColumn
networkAccessMacFilterWithMaskMacAddressMask = _NetworkAccessMacFilterWithMaskMacAddressMask_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 6, 1, 3),
    _NetworkAccessMacFilterWithMaskMacAddressMask_Type()
)
networkAccessMacFilterWithMaskMacAddressMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskMacAddressMask.setStatus("current")
_NetworkAccessMacFilterWithMaskStatus_Type = ValidStatus
_NetworkAccessMacFilterWithMaskStatus_Object = MibTableColumn
networkAccessMacFilterWithMaskStatus = _NetworkAccessMacFilterWithMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 13, 6, 1, 4),
    _NetworkAccessMacFilterWithMaskStatus_Type()
)
networkAccessMacFilterWithMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    networkAccessMacFilterWithMaskStatus.setStatus("current")
_MacAuthMgt_ObjectIdentity = ObjectIdentity
macAuthMgt = _MacAuthMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 14)
)


class _MacAuthReauthTime_Type(Integer32):
    """Custom type macAuthReauthTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(120, 1000000),
    )


_MacAuthReauthTime_Type.__name__ = "Integer32"
_MacAuthReauthTime_Object = MibScalar
macAuthReauthTime = _MacAuthReauthTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 14, 1),
    _MacAuthReauthTime_Type()
)
macAuthReauthTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthReauthTime.setStatus("current")
_MacAuthPortTable_Object = MibTable
macAuthPortTable = _MacAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 14, 2)
)
if mibBuilder.loadTexts:
    macAuthPortTable.setStatus("current")
_MacAuthPortEntry_Object = MibTableRow
macAuthPortEntry = _MacAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 14, 2, 1)
)
macAuthPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "macAuthPortIndex"),
)
if mibBuilder.loadTexts:
    macAuthPortEntry.setStatus("current")
_MacAuthPortIndex_Type = Integer32
_MacAuthPortIndex_Object = MibTableColumn
macAuthPortIndex = _MacAuthPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 14, 2, 1, 1),
    _MacAuthPortIndex_Type()
)
macAuthPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    macAuthPortIndex.setStatus("current")


class _MacAuthPortMaxMacCount_Type(Integer32):
    """Custom type macAuthPortMaxMacCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1024),
    )


_MacAuthPortMaxMacCount_Type.__name__ = "Integer32"
_MacAuthPortMaxMacCount_Object = MibTableColumn
macAuthPortMaxMacCount = _MacAuthPortMaxMacCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 14, 2, 1, 2),
    _MacAuthPortMaxMacCount_Type()
)
macAuthPortMaxMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthPortMaxMacCount.setStatus("current")


class _MacAuthPortIntrusionAction_Type(Integer32):
    """Custom type macAuthPortIntrusionAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("block-traffic", 1),
          ("pass-traffic", 2))
    )


_MacAuthPortIntrusionAction_Type.__name__ = "Integer32"
_MacAuthPortIntrusionAction_Object = MibTableColumn
macAuthPortIntrusionAction = _MacAuthPortIntrusionAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 14, 2, 1, 3),
    _MacAuthPortIntrusionAction_Type()
)
macAuthPortIntrusionAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    macAuthPortIntrusionAction.setStatus("current")
_WebAuthMgt_ObjectIdentity = ObjectIdentity
webAuthMgt = _WebAuthMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15)
)
_WebAuthSystemAuthControl_Type = EnabledStatus
_WebAuthSystemAuthControl_Object = MibScalar
webAuthSystemAuthControl = _WebAuthSystemAuthControl_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 1),
    _WebAuthSystemAuthControl_Type()
)
webAuthSystemAuthControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthSystemAuthControl.setStatus("current")


class _WebAuthSessionTimeout_Type(Integer32):
    """Custom type webAuthSessionTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 3600),
    )


_WebAuthSessionTimeout_Type.__name__ = "Integer32"
_WebAuthSessionTimeout_Object = MibScalar
webAuthSessionTimeout = _WebAuthSessionTimeout_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 5),
    _WebAuthSessionTimeout_Type()
)
webAuthSessionTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthSessionTimeout.setStatus("current")


class _WebAuthQuietPeriod_Type(Integer32):
    """Custom type webAuthQuietPeriod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 180),
    )


_WebAuthQuietPeriod_Type.__name__ = "Integer32"
_WebAuthQuietPeriod_Object = MibScalar
webAuthQuietPeriod = _WebAuthQuietPeriod_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 6),
    _WebAuthQuietPeriod_Type()
)
webAuthQuietPeriod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthQuietPeriod.setStatus("current")


class _WebAuthLoginAttempts_Type(Integer32):
    """Custom type webAuthLoginAttempts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_WebAuthLoginAttempts_Type.__name__ = "Integer32"
_WebAuthLoginAttempts_Object = MibScalar
webAuthLoginAttempts = _WebAuthLoginAttempts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 7),
    _WebAuthLoginAttempts_Type()
)
webAuthLoginAttempts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthLoginAttempts.setStatus("current")
_WebAuthReauthenticateMgt_ObjectIdentity = ObjectIdentity
webAuthReauthenticateMgt = _WebAuthReauthenticateMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 8)
)
_WebAuthReauthenticatePort_Type = Integer32
_WebAuthReauthenticatePort_Object = MibScalar
webAuthReauthenticatePort = _WebAuthReauthenticatePort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 8, 1),
    _WebAuthReauthenticatePort_Type()
)
webAuthReauthenticatePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthReauthenticatePort.setStatus("current")
_WebAuthReauthenticateInetAddressType_Type = InetAddressType
_WebAuthReauthenticateInetAddressType_Object = MibScalar
webAuthReauthenticateInetAddressType = _WebAuthReauthenticateInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 8, 2),
    _WebAuthReauthenticateInetAddressType_Type()
)
webAuthReauthenticateInetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthReauthenticateInetAddressType.setStatus("current")
_WebAuthReauthenticateInetAddress_Type = InetAddress
_WebAuthReauthenticateInetAddress_Object = MibScalar
webAuthReauthenticateInetAddress = _WebAuthReauthenticateInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 8, 3),
    _WebAuthReauthenticateInetAddress_Type()
)
webAuthReauthenticateInetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthReauthenticateInetAddress.setStatus("current")


class _WebAuthReauthenticateAction_Type(Integer32):
    """Custom type webAuthReauthenticateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noReauth", 1),
          ("reauth", 2))
    )


_WebAuthReauthenticateAction_Type.__name__ = "Integer32"
_WebAuthReauthenticateAction_Object = MibScalar
webAuthReauthenticateAction = _WebAuthReauthenticateAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 8, 4),
    _WebAuthReauthenticateAction_Type()
)
webAuthReauthenticateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthReauthenticateAction.setStatus("current")
_WebAuthPortConfigTable_Object = MibTable
webAuthPortConfigTable = _WebAuthPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 9)
)
if mibBuilder.loadTexts:
    webAuthPortConfigTable.setStatus("current")
_WebAuthPortConfigEntry_Object = MibTableRow
webAuthPortConfigEntry = _WebAuthPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 9, 1)
)
webAuthPortConfigEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "webAuthPortConfigPortIndex"),
)
if mibBuilder.loadTexts:
    webAuthPortConfigEntry.setStatus("current")
_WebAuthPortConfigPortIndex_Type = Integer32
_WebAuthPortConfigPortIndex_Object = MibTableColumn
webAuthPortConfigPortIndex = _WebAuthPortConfigPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 9, 1, 1),
    _WebAuthPortConfigPortIndex_Type()
)
webAuthPortConfigPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webAuthPortConfigPortIndex.setStatus("current")
_WebAuthPortConfigStatus_Type = EnabledStatus
_WebAuthPortConfigStatus_Object = MibTableColumn
webAuthPortConfigStatus = _WebAuthPortConfigStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 9, 1, 2),
    _WebAuthPortConfigStatus_Type()
)
webAuthPortConfigStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    webAuthPortConfigStatus.setStatus("current")
_WebAuthPortConfigAuthenticatedHostCount_Type = Integer32
_WebAuthPortConfigAuthenticatedHostCount_Object = MibTableColumn
webAuthPortConfigAuthenticatedHostCount = _WebAuthPortConfigAuthenticatedHostCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 9, 1, 3),
    _WebAuthPortConfigAuthenticatedHostCount_Type()
)
webAuthPortConfigAuthenticatedHostCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAuthPortConfigAuthenticatedHostCount.setStatus("current")
_WebAuthPortInfoTable_Object = MibTable
webAuthPortInfoTable = _WebAuthPortInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 10)
)
if mibBuilder.loadTexts:
    webAuthPortInfoTable.setStatus("current")
_WebAuthPortInfoEntry_Object = MibTableRow
webAuthPortInfoEntry = _WebAuthPortInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 10, 1)
)
webAuthPortInfoEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "webAuthPortInfoPortIndex"),
    (0, "ES3552M-AND-PoE-MIB", "webAuthPortInfoPortAuthSuccessIndex"),
)
if mibBuilder.loadTexts:
    webAuthPortInfoEntry.setStatus("current")
_WebAuthPortInfoPortIndex_Type = Integer32
_WebAuthPortInfoPortIndex_Object = MibTableColumn
webAuthPortInfoPortIndex = _WebAuthPortInfoPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 10, 1, 1),
    _WebAuthPortInfoPortIndex_Type()
)
webAuthPortInfoPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webAuthPortInfoPortIndex.setStatus("current")
_WebAuthPortInfoPortAuthSuccessIndex_Type = Integer32
_WebAuthPortInfoPortAuthSuccessIndex_Object = MibTableColumn
webAuthPortInfoPortAuthSuccessIndex = _WebAuthPortInfoPortAuthSuccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 10, 1, 2),
    _WebAuthPortInfoPortAuthSuccessIndex_Type()
)
webAuthPortInfoPortAuthSuccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    webAuthPortInfoPortAuthSuccessIndex.setStatus("current")
_WebAuthPortInfoInetAddressType_Type = InetAddressType
_WebAuthPortInfoInetAddressType_Object = MibTableColumn
webAuthPortInfoInetAddressType = _WebAuthPortInfoInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 10, 1, 3),
    _WebAuthPortInfoInetAddressType_Type()
)
webAuthPortInfoInetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAuthPortInfoInetAddressType.setStatus("current")
_WebAuthPortInfoInetAddress_Type = InetAddress
_WebAuthPortInfoInetAddress_Object = MibTableColumn
webAuthPortInfoInetAddress = _WebAuthPortInfoInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 10, 1, 4),
    _WebAuthPortInfoInetAddress_Type()
)
webAuthPortInfoInetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAuthPortInfoInetAddress.setStatus("current")
_WebAuthPortInfoRemainingSessiontime_Type = Integer32
_WebAuthPortInfoRemainingSessiontime_Object = MibTableColumn
webAuthPortInfoRemainingSessiontime = _WebAuthPortInfoRemainingSessiontime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 10, 1, 5),
    _WebAuthPortInfoRemainingSessiontime_Type()
)
webAuthPortInfoRemainingSessiontime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAuthPortInfoRemainingSessiontime.setStatus("current")


class _WebAuthPortInfoStatus_Type(Integer32):
    """Custom type webAuthPortInfoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("authenticated", 1)
    )


_WebAuthPortInfoStatus_Type.__name__ = "Integer32"
_WebAuthPortInfoStatus_Object = MibTableColumn
webAuthPortInfoStatus = _WebAuthPortInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 17, 15, 10, 1, 6),
    _WebAuthPortInfoStatus_Type()
)
webAuthPortInfoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    webAuthPortInfoStatus.setStatus("current")
_SysLogMgt_ObjectIdentity = ObjectIdentity
sysLogMgt = _SysLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19)
)
_SysLogStatus_Type = EnabledStatus
_SysLogStatus_Object = MibScalar
sysLogStatus = _SysLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 3),
    _SysLogHistoryRamLevel_Type()
)
sysLogHistoryRamLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryRamLevel.setStatus("current")
_RemoteLogMgt_ObjectIdentity = ObjectIdentity
remoteLogMgt = _RemoteLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 6)
)
_RemoteLogStatus_Type = EnabledStatus
_RemoteLogStatus_Object = MibScalar
remoteLogStatus = _RemoteLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 6, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 6, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 6, 3),
    _RemoteLogFacilityType_Type()
)
remoteLogFacilityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogFacilityType.setStatus("current")
_RemoteLogServerTable_Object = MibTable
remoteLogServerTable = _RemoteLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 6, 4)
)
if mibBuilder.loadTexts:
    remoteLogServerTable.setStatus("current")
_RemoteLogServerEntry_Object = MibTableRow
remoteLogServerEntry = _RemoteLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 6, 4, 1)
)
remoteLogServerEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "remoteLogServerIp"),
)
if mibBuilder.loadTexts:
    remoteLogServerEntry.setStatus("current")
_RemoteLogServerIp_Type = IpAddress
_RemoteLogServerIp_Object = MibTableColumn
remoteLogServerIp = _RemoteLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 6, 4, 1, 1),
    _RemoteLogServerIp_Type()
)
remoteLogServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteLogServerIp.setStatus("current")
_RemoteLogServerStatus_Type = ValidStatus
_RemoteLogServerStatus_Object = MibTableColumn
remoteLogServerStatus = _RemoteLogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 6, 4, 1, 2),
    _RemoteLogServerStatus_Type()
)
remoteLogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteLogServerStatus.setStatus("current")
_SmtpMgt_ObjectIdentity = ObjectIdentity
smtpMgt = _SmtpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7)
)
_SmtpStatus_Type = EnabledStatus
_SmtpStatus_Object = MibScalar
smtpStatus = _SmtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 3),
    _SmtpSourceEMail_Type()
)
smtpSourceEMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSourceEMail.setStatus("current")
_SmtpServerIpTable_Object = MibTable
smtpServerIpTable = _SmtpServerIpTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 4)
)
if mibBuilder.loadTexts:
    smtpServerIpTable.setStatus("current")
_SmtpServerIpEntry_Object = MibTableRow
smtpServerIpEntry = _SmtpServerIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 4, 1)
)
smtpServerIpEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "smtpServerIp"),
)
if mibBuilder.loadTexts:
    smtpServerIpEntry.setStatus("current")
_SmtpServerIp_Type = IpAddress
_SmtpServerIp_Object = MibTableColumn
smtpServerIp = _SmtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 4, 1, 1),
    _SmtpServerIp_Type()
)
smtpServerIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    smtpServerIp.setStatus("current")
_SmtpServerIpStatus_Type = ValidStatus
_SmtpServerIpStatus_Object = MibTableColumn
smtpServerIpStatus = _SmtpServerIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 4, 1, 2),
    _SmtpServerIpStatus_Type()
)
smtpServerIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpServerIpStatus.setStatus("current")
_SmtpDestEMailTable_Object = MibTable
smtpDestEMailTable = _SmtpDestEMailTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 5)
)
if mibBuilder.loadTexts:
    smtpDestEMailTable.setStatus("current")
_SmtpDestEMailEntry_Object = MibTableRow
smtpDestEMailEntry = _SmtpDestEMailEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 5, 1)
)
smtpDestEMailEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "smtpDestEMail"),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 5, 1, 1),
    _SmtpDestEMail_Type()
)
smtpDestEMail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smtpDestEMail.setStatus("current")
_SmtpDestEMailStatus_Type = ValidStatus
_SmtpDestEMailStatus_Object = MibTableColumn
smtpDestEMailStatus = _SmtpDestEMailStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 19, 7, 5, 1, 2),
    _SmtpDestEMailStatus_Type()
)
smtpDestEMailStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpDestEMailStatus.setStatus("current")
_LineMgt_ObjectIdentity = ObjectIdentity
lineMgt = _LineMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20)
)
_ConsoleMgt_ObjectIdentity = ObjectIdentity
consoleMgt = _ConsoleMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 1)
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 1, 7),
    _ConsoleSilentTime_Type()
)
consoleSilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleSilentTime.setStatus("current")
_ConsoleAdminBaudRate_Type = Integer32
_ConsoleAdminBaudRate_Object = MibScalar
consoleAdminBaudRate = _ConsoleAdminBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 1, 8),
    _ConsoleAdminBaudRate_Type()
)
consoleAdminBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleAdminBaudRate.setStatus("current")
_ConsoleOperBaudRate_Type = Integer32
_ConsoleOperBaudRate_Object = MibScalar
consoleOperBaudRate = _ConsoleOperBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 1, 10),
    _ConsoleLoginResponseTimeout_Type()
)
consoleLoginResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleLoginResponseTimeout.setStatus("current")
_TelnetMgt_ObjectIdentity = ObjectIdentity
telnetMgt = _TelnetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 2)
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 20, 2, 5),
    _TelnetPortNumber_Type()
)
telnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortNumber.setStatus("current")
_SysTimeMgt_ObjectIdentity = ObjectIdentity
sysTimeMgt = _SysTimeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23)
)
_SntpMgt_ObjectIdentity = ObjectIdentity
sntpMgt = _SntpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 1)
)
_SntpStatus_Type = EnabledStatus
_SntpStatus_Object = MibScalar
sntpStatus = _SntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 1, 3),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 1, 4)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 1, 4, 1)
)
sntpServerEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "sntpServerIndex"),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 1, 4, 1, 1),
    _SntpServerIndex_Type()
)
sntpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sntpServerIndex.setStatus("current")
_SntpServerIpAddress_Type = IpAddress
_SntpServerIpAddress_Object = MibTableColumn
sntpServerIpAddress = _SntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 1, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 3),
    _SysTimeZone_Type()
)
sysTimeZone.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZone.setStatus("current")


class _SysTimeZoneName_Type(DisplayString):
    """Custom type sysTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 30),
    )


_SysTimeZoneName_Type.__name__ = "DisplayString"
_SysTimeZoneName_Object = MibScalar
sysTimeZoneName = _SysTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 4),
    _SysTimeZoneName_Type()
)
sysTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZoneName.setStatus("current")
_NtpMgt_ObjectIdentity = ObjectIdentity
ntpMgt = _NtpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5)
)
_NtpStatus_Type = EnabledStatus
_NtpStatus_Object = MibScalar
ntpStatus = _NtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 1),
    _NtpStatus_Type()
)
ntpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpStatus.setStatus("current")


class _NtpServiceMode_Type(Integer32):
    """Custom type ntpServiceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("unicast", 1)
    )


_NtpServiceMode_Type.__name__ = "Integer32"
_NtpServiceMode_Object = MibScalar
ntpServiceMode = _NtpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 2),
    _NtpServiceMode_Type()
)
ntpServiceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServiceMode.setStatus("current")
_NtpPollInterval_Type = Integer32
_NtpPollInterval_Object = MibScalar
ntpPollInterval = _NtpPollInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 3),
    _NtpPollInterval_Type()
)
ntpPollInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpPollInterval.setStatus("current")
_NtpAuthenticateStatus_Type = EnabledStatus
_NtpAuthenticateStatus_Object = MibScalar
ntpAuthenticateStatus = _NtpAuthenticateStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 4),
    _NtpAuthenticateStatus_Type()
)
ntpAuthenticateStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpAuthenticateStatus.setStatus("current")
_NtpServerTable_Object = MibTable
ntpServerTable = _NtpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 5)
)
if mibBuilder.loadTexts:
    ntpServerTable.setStatus("current")
_NtpServerEntry_Object = MibTableRow
ntpServerEntry = _NtpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 5, 1)
)
ntpServerEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "ntpServerIpAddress"),
)
if mibBuilder.loadTexts:
    ntpServerEntry.setStatus("current")
_NtpServerIpAddress_Type = IpAddress
_NtpServerIpAddress_Object = MibTableColumn
ntpServerIpAddress = _NtpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 5, 1, 1),
    _NtpServerIpAddress_Type()
)
ntpServerIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpServerIpAddress.setStatus("current")
_NtpServerVersion_Type = Integer32
_NtpServerVersion_Object = MibTableColumn
ntpServerVersion = _NtpServerVersion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 5, 1, 2),
    _NtpServerVersion_Type()
)
ntpServerVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntpServerVersion.setStatus("current")


class _NtpServerKeyId_Type(Integer32):
    """Custom type ntpServerKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtpServerKeyId_Type.__name__ = "Integer32"
_NtpServerKeyId_Object = MibTableColumn
ntpServerKeyId = _NtpServerKeyId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 5, 1, 3),
    _NtpServerKeyId_Type()
)
ntpServerKeyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntpServerKeyId.setStatus("current")


class _NtpServerStatus_Type(Integer32):
    """Custom type ntpServerStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("active", 2),
          ("destroy", 3))
    )


_NtpServerStatus_Type.__name__ = "Integer32"
_NtpServerStatus_Object = MibTableColumn
ntpServerStatus = _NtpServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 5, 1, 4),
    _NtpServerStatus_Type()
)
ntpServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpServerStatus.setStatus("current")
_NtpAuthKeyTable_Object = MibTable
ntpAuthKeyTable = _NtpAuthKeyTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 6)
)
if mibBuilder.loadTexts:
    ntpAuthKeyTable.setStatus("current")
_NtpAuthKeyEntry_Object = MibTableRow
ntpAuthKeyEntry = _NtpAuthKeyEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 6, 1)
)
ntpAuthKeyEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "ntpAuthKeyId"),
)
if mibBuilder.loadTexts:
    ntpAuthKeyEntry.setStatus("current")


class _NtpAuthKeyId_Type(Integer32):
    """Custom type ntpAuthKeyId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65536),
    )


_NtpAuthKeyId_Type.__name__ = "Integer32"
_NtpAuthKeyId_Object = MibTableColumn
ntpAuthKeyId = _NtpAuthKeyId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 6, 1, 1),
    _NtpAuthKeyId_Type()
)
ntpAuthKeyId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntpAuthKeyId.setStatus("current")


class _NtpAuthKeyWord_Type(OctetString):
    """Custom type ntpAuthKeyWord based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtpAuthKeyWord_Type.__name__ = "OctetString"
_NtpAuthKeyWord_Object = MibTableColumn
ntpAuthKeyWord = _NtpAuthKeyWord_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 6, 1, 2),
    _NtpAuthKeyWord_Type()
)
ntpAuthKeyWord.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpAuthKeyWord.setStatus("current")


class _NtpAuthKeyStatus_Type(Integer32):
    """Custom type ntpAuthKeyStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("create", 1),
          ("active", 2),
          ("destroy", 3))
    )


_NtpAuthKeyStatus_Type.__name__ = "Integer32"
_NtpAuthKeyStatus_Object = MibTableColumn
ntpAuthKeyStatus = _NtpAuthKeyStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 5, 6, 1, 3),
    _NtpAuthKeyStatus_Type()
)
ntpAuthKeyStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ntpAuthKeyStatus.setStatus("current")


class _SysTimeZonePredefined_Type(Integer32):
    """Custom type sysTimeZonePredefined based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              8000,
              9000,
              10000,
              10300,
              11000,
              12000,
              13000,
              13001,
              13002,
              14000,
              14001,
              14002,
              14003,
              15000,
              15001,
              15002,
              16000,
              16001,
              16002,
              16700,
              17000,
              17001,
              17002,
              18000,
              19000,
              19001,
              20000,
              20001,
              21000,
              21001,
              21002,
              21003,
              21004,
              22000,
              22001,
              22002,
              22003,
              22004,
              22005,
              23000,
              23001,
              23002,
              23003,
              23300,
              24000,
              24001,
              24300,
              25000,
              25001,
              25300,
              25450,
              26000,
              26001,
              26002,
              26300,
              27000,
              27001,
              28000,
              28001,
              28002,
              28003,
              28004,
              29000,
              29001,
              29002,
              29300,
              29301,
              30000,
              30001,
              30002,
              30003,
              30004,
              30300,
              31000,
              31300,
              32000,
              32001,
              32450,
              33000,
              34000)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("minus1200InternationalDateLineWest", 8000),
          ("minus1100MidwayIslandSamoa", 9000),
          ("minus1000Hawaii", 10000),
          ("minus0930Taiohae", 10300),
          ("minus0900Alaska", 11000),
          ("minus0800PacificTimeTijuana", 12000),
          ("minus0700Arizona", 13000),
          ("minus0700ChihuahuaLaPazMazatlan", 13001),
          ("minus0700MountainTimeUSCanada", 13002),
          ("minus0600CentralAmerica", 14000),
          ("minus0600CentralTimeUSCanada", 14001),
          ("minus0600GuadalajaraMexicoCityMonterrey", 14002),
          ("minus0600Saskatchewan", 14003),
          ("minus0500BogotaLimaQuito", 15000),
          ("minus0500EasternTimeUSCanada", 15001),
          ("minus0500IndianaEast", 15002),
          ("minus0400AtlanticTimeCanada", 16000),
          ("minus0400CaracasLaPaz", 16001),
          ("minus0400Santiago", 16002),
          ("minus0330Newfoundland", 16700),
          ("minus0300Brasilia", 17000),
          ("minus0300BuenosAiresGeorgetown", 17001),
          ("minus0300Greenland", 17002),
          ("minus0200MidAtlantic", 18000),
          ("minus0100Azores", 19000),
          ("minus0100CapeVerdeIs", 19001),
          ("gmtDublinEdinburghLisbonLondon", 20000),
          ("gmtCasablancaMonrovia", 20001),
          ("plus0100AmsterdamBerlinBernRomeStockholmVienna", 21000),
          ("plus0100BelgradeBratislavaBudapestLjubljanaPrague", 21001),
          ("plus0100BrusselsCopenhagenMadridParis", 21002),
          ("plus0100SarajevoSkopjeWarsawZagreb", 21003),
          ("plus0100WestCentralAfrica", 21004),
          ("plus0200AthensBeirutIstanbulMinsk", 22000),
          ("plus0200Bucharest", 22001),
          ("plus0200Cairo", 22002),
          ("plus0200HararePretoria", 22003),
          ("plus0200HelsinkiKyivRigaSofiaTallinnVilnius", 22004),
          ("plus0200Jerusalem", 22005),
          ("plus0300Baghdad", 23000),
          ("plus0300KuwaitRiyadh", 23001),
          ("plus0300MoscowStPetersburgVolgograd", 23002),
          ("plus0300Nairobi", 23003),
          ("plus0330Tehran", 23300),
          ("plus0400AbuDhabiMuscat", 24000),
          ("plus0400BakuTbilisiYerevan", 24001),
          ("plus0430Kabul", 24300),
          ("plus0500Ekaterinburg", 25000),
          ("plus0500IslamabadKarachiTashkent", 25001),
          ("plus0530ChennaiCalcutaMumbaiNewDelhi", 25300),
          ("plus0545Kathmandu", 25450),
          ("plus0600AlmatyNovosibirsk", 26000),
          ("plus0600AstanaDhaka", 26001),
          ("plus0600SriJayawardenepura", 26002),
          ("plus0630Rangoon", 26300),
          ("plus0700BangkokHanoiJakarta", 27000),
          ("plus0700Krasnoyarsk", 27001),
          ("plus0800BeijingChongqingHongKongUrumqi", 28000),
          ("plus0800IrkutskUlaanBataar", 28001),
          ("plus0800KualaLumpurSingapore", 28002),
          ("plus0800Perth", 28003),
          ("plus0800Taipei", 28004),
          ("plus0900OsakaSapporoTokyo", 29000),
          ("plus0900Seoul", 29001),
          ("plus0900Yakutsk", 29002),
          ("plus0930Adelaide", 29300),
          ("plus0930Darwin", 29301),
          ("plus1000Brisbane", 30000),
          ("plus1000CanberraMelbourneSydney", 30001),
          ("plus1000GuamPortMoresby", 30002),
          ("plus1000Hobart", 30003),
          ("plus1000Vladivostok", 30004),
          ("plus1030LordHoweIsland", 30300),
          ("plus1100MagadanSolomonIsNewCaledonia", 31000),
          ("plus1130Kingston", 31300),
          ("plus1200AucklandWellington", 32000),
          ("plus1200FijiKamchatkaMarshallIs", 32001),
          ("plus1245ChathamIsland", 32450),
          ("plus1300Nukualofa", 33000),
          ("plus1400Kiritimati", 34000))
    )


_SysTimeZonePredefined_Type.__name__ = "Integer32"
_SysTimeZonePredefined_Object = MibScalar
sysTimeZonePredefined = _SysTimeZonePredefined_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 6),
    _SysTimeZonePredefined_Type()
)
sysTimeZonePredefined.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZonePredefined.setStatus("current")
_SysSummerTimeMgt_ObjectIdentity = ObjectIdentity
sysSummerTimeMgt = _SysSummerTimeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 7)
)


class _SysSummerTimeZoneName_Type(DisplayString):
    """Custom type sysSummerTimeZoneName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_SysSummerTimeZoneName_Type.__name__ = "DisplayString"
_SysSummerTimeZoneName_Object = MibScalar
sysSummerTimeZoneName = _SysSummerTimeZoneName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 7, 1),
    _SysSummerTimeZoneName_Type()
)
sysSummerTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSummerTimeZoneName.setStatus("current")


class _SysSummerTimeMode_Type(Integer32):
    """Custom type sysSummerTimeMode based on Integer32"""
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
        *(("disabled", 1),
          ("recurring", 2),
          ("date", 3),
          ("predefined", 4))
    )


_SysSummerTimeMode_Type.__name__ = "Integer32"
_SysSummerTimeMode_Object = MibScalar
sysSummerTimeMode = _SysSummerTimeMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 7, 2),
    _SysSummerTimeMode_Type()
)
sysSummerTimeMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSummerTimeMode.setStatus("current")


class _SysSummerTimeRecurringTime_Type(DisplayString):
    """Custom type sysSummerTimeRecurringTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(37, 37),
    )
    fixed_length = 37


_SysSummerTimeRecurringTime_Type.__name__ = "DisplayString"
_SysSummerTimeRecurringTime_Object = MibScalar
sysSummerTimeRecurringTime = _SysSummerTimeRecurringTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 7, 3),
    _SysSummerTimeRecurringTime_Type()
)
sysSummerTimeRecurringTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSummerTimeRecurringTime.setStatus("current")


class _SysSummerTimeDateTime_Type(DisplayString):
    """Custom type sysSummerTimeDateTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(37, 37),
    )
    fixed_length = 37


_SysSummerTimeDateTime_Type.__name__ = "DisplayString"
_SysSummerTimeDateTime_Object = MibScalar
sysSummerTimeDateTime = _SysSummerTimeDateTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 7, 4),
    _SysSummerTimeDateTime_Type()
)
sysSummerTimeDateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSummerTimeDateTime.setStatus("current")


class _SysSummerTimePredefinedRegion_Type(Integer32):
    """Custom type sysSummerTimePredefinedRegion based on Integer32"""
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
          ("usa", 2),
          ("europe", 3),
          ("australia", 4),
          ("newZealand", 5))
    )


_SysSummerTimePredefinedRegion_Type.__name__ = "Integer32"
_SysSummerTimePredefinedRegion_Object = MibScalar
sysSummerTimePredefinedRegion = _SysSummerTimePredefinedRegion_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 7, 5),
    _SysSummerTimePredefinedRegion_Type()
)
sysSummerTimePredefinedRegion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSummerTimePredefinedRegion.setStatus("current")


class _SysSummerTimeOffset_Type(Integer32):
    """Custom type sysSummerTimeOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 99),
    )


_SysSummerTimeOffset_Type.__name__ = "Integer32"
_SysSummerTimeOffset_Object = MibScalar
sysSummerTimeOffset = _SysSummerTimeOffset_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 7, 6),
    _SysSummerTimeOffset_Type()
)
sysSummerTimeOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysSummerTimeOffset.setStatus("current")
_SysSummerTimeEffect_Type = TruthValue
_SysSummerTimeEffect_Object = MibScalar
sysSummerTimeEffect = _SysSummerTimeEffect_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 23, 7, 7),
    _SysSummerTimeEffect_Type()
)
sysSummerTimeEffect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sysSummerTimeEffect.setStatus("current")
_FileMgt_ObjectIdentity = ObjectIdentity
fileMgt = _FileMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24)
)
_FileCopyMgt_ObjectIdentity = ObjectIdentity
fileCopyMgt = _FileCopyMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1)
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
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("runningCfg", 2),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5),
          ("http", 6),
          ("ftp", 7))
    )


_FileCopySrcOperType_Type.__name__ = "Integer32"
_FileCopySrcOperType_Object = MibScalar
fileCopySrcOperType = _FileCopySrcOperType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 2),
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
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("runningCfg", 2),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5),
          ("http", 6),
          ("ftp", 7))
    )


_FileCopyDestOperType_Type.__name__ = "Integer32"
_FileCopyDestOperType_Object = MibScalar
fileCopyDestOperType = _FileCopyDestOperType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 4),
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
              3,
              5)
        )
    )
    namedValues = NamedValues(
        *(("opcode", 1),
          ("config", 2),
          ("bootRom", 3),
          ("loader", 5))
    )


_FileCopyFileType_Type.__name__ = "Integer32"
_FileCopyFileType_Object = MibScalar
fileCopyFileType = _FileCopyFileType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 5),
    _FileCopyFileType_Type()
)
fileCopyFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyFileType.setStatus("current")
_FileCopyTftpServer_Type = IpAddress
_FileCopyTftpServer_Object = MibScalar
fileCopyTftpServer = _FileCopyTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 6),
    _FileCopyTftpServer_Type()
)
fileCopyTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyTftpServer.setStatus("current")
_FileCopyUnitId_Type = Integer32
_FileCopyUnitId_Object = MibScalar
fileCopyUnitId = _FileCopyUnitId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 8),
    _FileCopyAction_Type()
)
fileCopyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyAction.setStatus("current")
_FileCopyStatus_Type = FileCopyStatus
_FileCopyStatus_Object = MibScalar
fileCopyStatus = _FileCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 9),
    _FileCopyStatus_Type()
)
fileCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyStatus.setStatus("current")


class _FileCopyFtpLoginUsername_Type(DisplayString):
    """Custom type fileCopyFtpLoginUsername based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_FileCopyFtpLoginUsername_Type.__name__ = "DisplayString"
_FileCopyFtpLoginUsername_Object = MibScalar
fileCopyFtpLoginUsername = _FileCopyFtpLoginUsername_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 12),
    _FileCopyFtpLoginUsername_Type()
)
fileCopyFtpLoginUsername.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyFtpLoginUsername.setStatus("current")


class _FileCopyFtpLoginPassword_Type(DisplayString):
    """Custom type fileCopyFtpLoginPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_FileCopyFtpLoginPassword_Type.__name__ = "DisplayString"
_FileCopyFtpLoginPassword_Object = MibScalar
fileCopyFtpLoginPassword = _FileCopyFtpLoginPassword_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 1, 13),
    _FileCopyFtpLoginPassword_Type()
)
fileCopyFtpLoginPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyFtpLoginPassword.setStatus("current")
_FileInfoMgt_ObjectIdentity = ObjectIdentity
fileInfoMgt = _FileInfoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 2)
)
_FileInfoTable_Object = MibTable
fileInfoTable = _FileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    fileInfoTable.setStatus("current")
_FileInfoEntry_Object = MibTableRow
fileInfoEntry = _FileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 2, 1, 1)
)
fileInfoEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "fileInfoUnitID"),
    (1, "ES3552M-AND-PoE-MIB", "fileInfoFileName"),
)
if mibBuilder.loadTexts:
    fileInfoEntry.setStatus("current")
_FileInfoUnitID_Type = Integer32
_FileInfoUnitID_Object = MibTableColumn
fileInfoUnitID = _FileInfoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 2, 1, 1, 3),
    _FileInfoFileType_Type()
)
fileInfoFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileType.setStatus("current")
_FileInfoIsStartUp_Type = TruthValue
_FileInfoIsStartUp_Object = MibTableColumn
fileInfoIsStartUp = _FileInfoIsStartUp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 2, 1, 1, 4),
    _FileInfoIsStartUp_Type()
)
fileInfoIsStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoIsStartUp.setStatus("current")
_FileInfoFileSize_Type = Integer32
_FileInfoFileSize_Object = MibTableColumn
fileInfoFileSize = _FileInfoFileSize_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 2, 1, 1, 7),
    _FileInfoDelete_Type()
)
fileInfoDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoDelete.setStatus("current")
_FileAutoDownloadResultTable_Object = MibTable
fileAutoDownloadResultTable = _FileAutoDownloadResultTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 3)
)
if mibBuilder.loadTexts:
    fileAutoDownloadResultTable.setStatus("current")
_FileAutoDownloadResultEntry_Object = MibTableRow
fileAutoDownloadResultEntry = _FileAutoDownloadResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 3, 1)
)
fileAutoDownloadResultEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "fileAutoDownloadResultUnitID"),
)
if mibBuilder.loadTexts:
    fileAutoDownloadResultEntry.setStatus("current")
_FileAutoDownloadResultUnitID_Type = Integer32
_FileAutoDownloadResultUnitID_Object = MibTableColumn
fileAutoDownloadResultUnitID = _FileAutoDownloadResultUnitID_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 3, 1, 2),
    _FileAutoDownloadResultAction_Type()
)
fileAutoDownloadResultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAutoDownloadResultAction.setStatus("current")
_FileAutoDownloadResultStatus_Type = FileCopyStatus
_FileAutoDownloadResultStatus_Object = MibTableColumn
fileAutoDownloadResultStatus = _FileAutoDownloadResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 3, 1, 3),
    _FileAutoDownloadResultStatus_Type()
)
fileAutoDownloadResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAutoDownloadResultStatus.setStatus("current")
_FileAutoUpgradeMgt_ObjectIdentity = ObjectIdentity
fileAutoUpgradeMgt = _FileAutoUpgradeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 4)
)
_FileAutoUpgradeOpCodeStatus_Type = EnabledStatus
_FileAutoUpgradeOpCodeStatus_Object = MibScalar
fileAutoUpgradeOpCodeStatus = _FileAutoUpgradeOpCodeStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 4, 1),
    _FileAutoUpgradeOpCodeStatus_Type()
)
fileAutoUpgradeOpCodeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileAutoUpgradeOpCodeStatus.setStatus("current")


class _FileAutoUpgradeOpCodePath_Type(DisplayString):
    """Custom type fileAutoUpgradeOpCodePath based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_FileAutoUpgradeOpCodePath_Type.__name__ = "DisplayString"
_FileAutoUpgradeOpCodePath_Object = MibScalar
fileAutoUpgradeOpCodePath = _FileAutoUpgradeOpCodePath_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 4, 2),
    _FileAutoUpgradeOpCodePath_Type()
)
fileAutoUpgradeOpCodePath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileAutoUpgradeOpCodePath.setStatus("current")


class _FileAutoUpgradeOpCodeFileName_Type(DisplayString):
    """Custom type fileAutoUpgradeOpCodeFileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_FileAutoUpgradeOpCodeFileName_Type.__name__ = "DisplayString"
_FileAutoUpgradeOpCodeFileName_Object = MibScalar
fileAutoUpgradeOpCodeFileName = _FileAutoUpgradeOpCodeFileName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 4, 3),
    _FileAutoUpgradeOpCodeFileName_Type()
)
fileAutoUpgradeOpCodeFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAutoUpgradeOpCodeFileName.setStatus("current")
_FileAutoUpgradeOpCodeForceModeStatus_Type = EnabledStatus
_FileAutoUpgradeOpCodeForceModeStatus_Object = MibScalar
fileAutoUpgradeOpCodeForceModeStatus = _FileAutoUpgradeOpCodeForceModeStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 24, 4, 4),
    _FileAutoUpgradeOpCodeForceModeStatus_Type()
)
fileAutoUpgradeOpCodeForceModeStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileAutoUpgradeOpCodeForceModeStatus.setStatus("current")
_DnsMgt_ObjectIdentity = ObjectIdentity
dnsMgt = _DnsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26)
)
_DnsDomainLookup_Type = EnabledStatus
_DnsDomainLookup_Object = MibScalar
dnsDomainLookup = _DnsDomainLookup_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 1),
    _DnsDomainLookup_Type()
)
dnsDomainLookup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainLookup.setStatus("current")


class _DnsDomainName_Type(DisplayString):
    """Custom type dnsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DnsDomainName_Type.__name__ = "DisplayString"
_DnsDomainName_Object = MibScalar
dnsDomainName = _DnsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 2),
    _DnsDomainName_Type()
)
dnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainName.setStatus("current")
_DnsHostTable_Object = MibTable
dnsHostTable = _DnsHostTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 3)
)
if mibBuilder.loadTexts:
    dnsHostTable.setStatus("current")
_DnsHostEntry_Object = MibTableRow
dnsHostEntry = _DnsHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 3, 1)
)
dnsHostEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "dnsHostName"),
    (0, "ES3552M-AND-PoE-MIB", "dnsHostIndex"),
)
if mibBuilder.loadTexts:
    dnsHostEntry.setStatus("current")


class _DnsHostName_Type(DisplayString):
    """Custom type dnsHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsHostName_Type.__name__ = "DisplayString"
_DnsHostName_Object = MibTableColumn
dnsHostName = _DnsHostName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 3, 1, 1),
    _DnsHostName_Type()
)
dnsHostName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsHostName.setStatus("current")


class _DnsHostIndex_Type(Integer32):
    """Custom type dnsHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_DnsHostIndex_Type.__name__ = "Integer32"
_DnsHostIndex_Object = MibTableColumn
dnsHostIndex = _DnsHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 3, 1, 2),
    _DnsHostIndex_Type()
)
dnsHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsHostIndex.setStatus("current")
_DnsHostIp_Type = IpAddress
_DnsHostIp_Object = MibTableColumn
dnsHostIp = _DnsHostIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 3, 1, 3),
    _DnsHostIp_Type()
)
dnsHostIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsHostIp.setStatus("current")
_DnsDomainListTable_Object = MibTable
dnsDomainListTable = _DnsDomainListTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 5)
)
if mibBuilder.loadTexts:
    dnsDomainListTable.setStatus("current")
_DnsDomainListEntry_Object = MibTableRow
dnsDomainListEntry = _DnsDomainListEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 5, 1)
)
dnsDomainListEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "dnsDomainListName"),
)
if mibBuilder.loadTexts:
    dnsDomainListEntry.setStatus("current")


class _DnsDomainListName_Type(DisplayString):
    """Custom type dnsDomainListName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsDomainListName_Type.__name__ = "DisplayString"
_DnsDomainListName_Object = MibTableColumn
dnsDomainListName = _DnsDomainListName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 5, 1, 1),
    _DnsDomainListName_Type()
)
dnsDomainListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsDomainListName.setStatus("current")
_DnsDomainListStatus_Type = ValidStatus
_DnsDomainListStatus_Object = MibTableColumn
dnsDomainListStatus = _DnsDomainListStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 5, 1, 2),
    _DnsDomainListStatus_Type()
)
dnsDomainListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsDomainListStatus.setStatus("current")
_DnsNameServerTable_Object = MibTable
dnsNameServerTable = _DnsNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 6)
)
if mibBuilder.loadTexts:
    dnsNameServerTable.setStatus("current")
_DnsNameServerEntry_Object = MibTableRow
dnsNameServerEntry = _DnsNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 6, 1)
)
dnsNameServerEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "dnsNameServerIndex"),
)
if mibBuilder.loadTexts:
    dnsNameServerEntry.setStatus("current")


class _DnsNameServerIndex_Type(Integer32):
    """Custom type dnsNameServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_DnsNameServerIndex_Type.__name__ = "Integer32"
_DnsNameServerIndex_Object = MibTableColumn
dnsNameServerIndex = _DnsNameServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 6, 1, 1),
    _DnsNameServerIndex_Type()
)
dnsNameServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsNameServerIndex.setStatus("current")
_DnsNameServerIp_Type = IpAddress
_DnsNameServerIp_Object = MibTableColumn
dnsNameServerIp = _DnsNameServerIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 6, 1, 2),
    _DnsNameServerIp_Type()
)
dnsNameServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNameServerIp.setStatus("current")
_DnsCacheTable_Object = MibTable
dnsCacheTable = _DnsCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 7)
)
if mibBuilder.loadTexts:
    dnsCacheTable.setStatus("current")
_DnsCacheEntry_Object = MibTableRow
dnsCacheEntry = _DnsCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 7, 1)
)
dnsCacheEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "dnsCacheIndex"),
)
if mibBuilder.loadTexts:
    dnsCacheEntry.setStatus("current")
_DnsCacheIndex_Type = Integer32
_DnsCacheIndex_Object = MibTableColumn
dnsCacheIndex = _DnsCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 7, 1, 1),
    _DnsCacheIndex_Type()
)
dnsCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsCacheIndex.setStatus("current")
_DnsCacheFlag_Type = Integer32
_DnsCacheFlag_Object = MibTableColumn
dnsCacheFlag = _DnsCacheFlag_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 7, 1, 2),
    _DnsCacheFlag_Type()
)
dnsCacheFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheFlag.setStatus("current")


class _DnsCacheType_Type(Integer32):
    """Custom type dnsCacheType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("address", 1),
          ("cname", 2))
    )


_DnsCacheType_Type.__name__ = "Integer32"
_DnsCacheType_Object = MibTableColumn
dnsCacheType = _DnsCacheType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 7, 1, 3),
    _DnsCacheType_Type()
)
dnsCacheType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheType.setStatus("current")
_DnsCacheIp_Type = IpAddress
_DnsCacheIp_Object = MibTableColumn
dnsCacheIp = _DnsCacheIp_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 7, 1, 4),
    _DnsCacheIp_Type()
)
dnsCacheIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheIp.setStatus("current")


class _DnsCacheTtl_Type(Integer32):
    """Custom type dnsCacheTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 876000),
    )


_DnsCacheTtl_Type.__name__ = "Integer32"
_DnsCacheTtl_Object = MibTableColumn
dnsCacheTtl = _DnsCacheTtl_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 7, 1, 5),
    _DnsCacheTtl_Type()
)
dnsCacheTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheTtl.setStatus("current")


class _DnsCacheDomain_Type(DisplayString):
    """Custom type dnsCacheDomain based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsCacheDomain_Type.__name__ = "DisplayString"
_DnsCacheDomain_Object = MibTableColumn
dnsCacheDomain = _DnsCacheDomain_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 26, 7, 1, 6),
    _DnsCacheDomain_Type()
)
dnsCacheDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheDomain.setStatus("current")
_StormMgt_ObjectIdentity = ObjectIdentity
stormMgt = _StormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33)
)
_McastStormMgt_ObjectIdentity = ObjectIdentity
mcastStormMgt = _McastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 1)
)
_McastStormTable_Object = MibTable
mcastStormTable = _McastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 1, 1)
)
if mibBuilder.loadTexts:
    mcastStormTable.setStatus("current")
_McastStormEntry_Object = MibTableRow
mcastStormEntry = _McastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 1, 1, 1)
)
mcastStormEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    mcastStormEntry.setStatus("current")
_McastStormIfIndex_Type = Integer32
_McastStormIfIndex_Object = MibTableColumn
mcastStormIfIndex = _McastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 1, 1, 1, 1),
    _McastStormIfIndex_Type()
)
mcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mcastStormIfIndex.setStatus("current")
_McastStormStatus_Type = EnabledStatus
_McastStormStatus_Object = MibTableColumn
mcastStormStatus = _McastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 1, 1, 1, 2),
    _McastStormStatus_Type()
)
mcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastStormStatus.setStatus("current")
_McastStormOctetRate_Type = Integer32
_McastStormOctetRate_Object = MibTableColumn
mcastStormOctetRate = _McastStormOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 1, 1, 1, 5),
    _McastStormOctetRate_Type()
)
mcastStormOctetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mcastStormOctetRate.setStatus("current")
_BcastStormMgt_ObjectIdentity = ObjectIdentity
bcastStormMgt = _BcastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 3)
)
_BcastStormTable_Object = MibTable
bcastStormTable = _BcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 3, 1)
)
if mibBuilder.loadTexts:
    bcastStormTable.setStatus("current")
_BcastStormEntry_Object = MibTableRow
bcastStormEntry = _BcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 3, 1, 1)
)
bcastStormEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "bcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    bcastStormEntry.setStatus("current")
_BcastStormIfIndex_Type = Integer32
_BcastStormIfIndex_Object = MibTableColumn
bcastStormIfIndex = _BcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 3, 1, 1, 1),
    _BcastStormIfIndex_Type()
)
bcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcastStormIfIndex.setStatus("current")
_BcastStormStatus_Type = EnabledStatus
_BcastStormStatus_Object = MibTableColumn
bcastStormStatus = _BcastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 3, 1, 1, 2),
    _BcastStormStatus_Type()
)
bcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormStatus.setStatus("current")
_BcastStormOctetRate_Type = Integer32
_BcastStormOctetRate_Object = MibTableColumn
bcastStormOctetRate = _BcastStormOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 3, 1, 1, 5),
    _BcastStormOctetRate_Type()
)
bcastStormOctetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormOctetRate.setStatus("current")
_UnknownUcastStormMgt_ObjectIdentity = ObjectIdentity
unknownUcastStormMgt = _UnknownUcastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 4)
)
_UnknownUcastStormTable_Object = MibTable
unknownUcastStormTable = _UnknownUcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 4, 1)
)
if mibBuilder.loadTexts:
    unknownUcastStormTable.setStatus("current")
_UnknownUcastStormEntry_Object = MibTableRow
unknownUcastStormEntry = _UnknownUcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 4, 1, 1)
)
unknownUcastStormEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "unknownUcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    unknownUcastStormEntry.setStatus("current")
_UnknownUcastStormIfIndex_Type = Integer32
_UnknownUcastStormIfIndex_Object = MibTableColumn
unknownUcastStormIfIndex = _UnknownUcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 4, 1, 1, 1),
    _UnknownUcastStormIfIndex_Type()
)
unknownUcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    unknownUcastStormIfIndex.setStatus("current")
_UnknownUcastStormStatus_Type = EnabledStatus
_UnknownUcastStormStatus_Object = MibTableColumn
unknownUcastStormStatus = _UnknownUcastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 4, 1, 1, 2),
    _UnknownUcastStormStatus_Type()
)
unknownUcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownUcastStormStatus.setStatus("current")
_UnknownUcastStormOctetRate_Type = Integer32
_UnknownUcastStormOctetRate_Object = MibTableColumn
unknownUcastStormOctetRate = _UnknownUcastStormOctetRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 4, 1, 1, 5),
    _UnknownUcastStormOctetRate_Type()
)
unknownUcastStormOctetRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    unknownUcastStormOctetRate.setStatus("current")
_AtcMgt_ObjectIdentity = ObjectIdentity
atcMgt = _AtcMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5)
)
_AtcBcastStormTcApplyTime_Type = Integer32
_AtcBcastStormTcApplyTime_Object = MibScalar
atcBcastStormTcApplyTime = _AtcBcastStormTcApplyTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 1),
    _AtcBcastStormTcApplyTime_Type()
)
atcBcastStormTcApplyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormTcApplyTime.setStatus("current")
_AtcBcastStormTcReleaseTime_Type = Integer32
_AtcBcastStormTcReleaseTime_Object = MibScalar
atcBcastStormTcReleaseTime = _AtcBcastStormTcReleaseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 2),
    _AtcBcastStormTcReleaseTime_Type()
)
atcBcastStormTcReleaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormTcReleaseTime.setStatus("current")
_AtcBcastStormTable_Object = MibTable
atcBcastStormTable = _AtcBcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3)
)
if mibBuilder.loadTexts:
    atcBcastStormTable.setStatus("current")
_AtcBcastStormEntry_Object = MibTableRow
atcBcastStormEntry = _AtcBcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1)
)
atcBcastStormEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "atcBcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    atcBcastStormEntry.setStatus("current")
_AtcBcastStormIfIndex_Type = Integer32
_AtcBcastStormIfIndex_Object = MibTableColumn
atcBcastStormIfIndex = _AtcBcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 1),
    _AtcBcastStormIfIndex_Type()
)
atcBcastStormIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atcBcastStormIfIndex.setStatus("current")
_AtcBcastStormEnable_Type = EnabledStatus
_AtcBcastStormEnable_Object = MibTableColumn
atcBcastStormEnable = _AtcBcastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 2),
    _AtcBcastStormEnable_Type()
)
atcBcastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormEnable.setStatus("current")
_AtcBcastStormAutoRelease_Type = EnabledStatus
_AtcBcastStormAutoRelease_Object = MibTableColumn
atcBcastStormAutoRelease = _AtcBcastStormAutoRelease_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 3),
    _AtcBcastStormAutoRelease_Type()
)
atcBcastStormAutoRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormAutoRelease.setStatus("current")


class _AtcBcastStormSampleType_Type(Integer32):
    """Custom type atcBcastStormSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("packet-rate", 1),
          ("octet-rate", 2),
          ("percent", 3))
    )


_AtcBcastStormSampleType_Type.__name__ = "Integer32"
_AtcBcastStormSampleType_Object = MibTableColumn
atcBcastStormSampleType = _AtcBcastStormSampleType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 4),
    _AtcBcastStormSampleType_Type()
)
atcBcastStormSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormSampleType.setStatus("current")
_AtcBcastStormCurrentTrafficRate_Type = Integer32
_AtcBcastStormCurrentTrafficRate_Object = MibTableColumn
atcBcastStormCurrentTrafficRate = _AtcBcastStormCurrentTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 5),
    _AtcBcastStormCurrentTrafficRate_Type()
)
atcBcastStormCurrentTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atcBcastStormCurrentTrafficRate.setStatus("current")
_AtcBcastStormAlarmFireThreshold_Type = Integer32
_AtcBcastStormAlarmFireThreshold_Object = MibTableColumn
atcBcastStormAlarmFireThreshold = _AtcBcastStormAlarmFireThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 6),
    _AtcBcastStormAlarmFireThreshold_Type()
)
atcBcastStormAlarmFireThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormAlarmFireThreshold.setStatus("current")
_AtcBcastStormAlarmClearThreshold_Type = Integer32
_AtcBcastStormAlarmClearThreshold_Object = MibTableColumn
atcBcastStormAlarmClearThreshold = _AtcBcastStormAlarmClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 7),
    _AtcBcastStormAlarmClearThreshold_Type()
)
atcBcastStormAlarmClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormAlarmClearThreshold.setStatus("current")


class _AtcBcastStormTcAction_Type(Integer32):
    """Custom type atcBcastStormTcAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-control", 1),
          ("shutdown", 2))
    )


_AtcBcastStormTcAction_Type.__name__ = "Integer32"
_AtcBcastStormTcAction_Object = MibTableColumn
atcBcastStormTcAction = _AtcBcastStormTcAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 8),
    _AtcBcastStormTcAction_Type()
)
atcBcastStormTcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormTcAction.setStatus("current")
_AtcBcastStormAlarmFireTrapStatus_Type = EnabledStatus
_AtcBcastStormAlarmFireTrapStatus_Object = MibTableColumn
atcBcastStormAlarmFireTrapStatus = _AtcBcastStormAlarmFireTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 9),
    _AtcBcastStormAlarmFireTrapStatus_Type()
)
atcBcastStormAlarmFireTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormAlarmFireTrapStatus.setStatus("current")
_AtcBcastStormAlarmClearTrapStatus_Type = EnabledStatus
_AtcBcastStormAlarmClearTrapStatus_Object = MibTableColumn
atcBcastStormAlarmClearTrapStatus = _AtcBcastStormAlarmClearTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 10),
    _AtcBcastStormAlarmClearTrapStatus_Type()
)
atcBcastStormAlarmClearTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormAlarmClearTrapStatus.setStatus("current")
_AtcBcastStormTcApplyTrapStatus_Type = EnabledStatus
_AtcBcastStormTcApplyTrapStatus_Object = MibTableColumn
atcBcastStormTcApplyTrapStatus = _AtcBcastStormTcApplyTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 11),
    _AtcBcastStormTcApplyTrapStatus_Type()
)
atcBcastStormTcApplyTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormTcApplyTrapStatus.setStatus("current")
_AtcBcastStormTcReleaseTrapStatus_Type = EnabledStatus
_AtcBcastStormTcReleaseTrapStatus_Object = MibTableColumn
atcBcastStormTcReleaseTrapStatus = _AtcBcastStormTcReleaseTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 3, 1, 12),
    _AtcBcastStormTcReleaseTrapStatus_Type()
)
atcBcastStormTcReleaseTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcBcastStormTcReleaseTrapStatus.setStatus("current")
_AtcMcastStormTcApplyTime_Type = Integer32
_AtcMcastStormTcApplyTime_Object = MibScalar
atcMcastStormTcApplyTime = _AtcMcastStormTcApplyTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 4),
    _AtcMcastStormTcApplyTime_Type()
)
atcMcastStormTcApplyTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormTcApplyTime.setStatus("current")
_AtcMcastStormTcReleaseTime_Type = Integer32
_AtcMcastStormTcReleaseTime_Object = MibScalar
atcMcastStormTcReleaseTime = _AtcMcastStormTcReleaseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 5),
    _AtcMcastStormTcReleaseTime_Type()
)
atcMcastStormTcReleaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormTcReleaseTime.setStatus("current")
_AtcMcastStormTable_Object = MibTable
atcMcastStormTable = _AtcMcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6)
)
if mibBuilder.loadTexts:
    atcMcastStormTable.setStatus("current")
_AtcMcastStormEntry_Object = MibTableRow
atcMcastStormEntry = _AtcMcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1)
)
atcMcastStormEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "atcMcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    atcMcastStormEntry.setStatus("current")
_AtcMcastStormIfIndex_Type = Integer32
_AtcMcastStormIfIndex_Object = MibTableColumn
atcMcastStormIfIndex = _AtcMcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 1),
    _AtcMcastStormIfIndex_Type()
)
atcMcastStormIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    atcMcastStormIfIndex.setStatus("current")
_AtcMcastStormEnable_Type = EnabledStatus
_AtcMcastStormEnable_Object = MibTableColumn
atcMcastStormEnable = _AtcMcastStormEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 2),
    _AtcMcastStormEnable_Type()
)
atcMcastStormEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormEnable.setStatus("current")
_AtcMcastStormAutoRelease_Type = EnabledStatus
_AtcMcastStormAutoRelease_Object = MibTableColumn
atcMcastStormAutoRelease = _AtcMcastStormAutoRelease_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 3),
    _AtcMcastStormAutoRelease_Type()
)
atcMcastStormAutoRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormAutoRelease.setStatus("current")


class _AtcMcastStormSampleType_Type(Integer32):
    """Custom type atcMcastStormSampleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("packet-rate", 1),
          ("octet-rate", 2),
          ("percent", 3))
    )


_AtcMcastStormSampleType_Type.__name__ = "Integer32"
_AtcMcastStormSampleType_Object = MibTableColumn
atcMcastStormSampleType = _AtcMcastStormSampleType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 4),
    _AtcMcastStormSampleType_Type()
)
atcMcastStormSampleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormSampleType.setStatus("current")
_AtcMcastStormCurrentTrafficRate_Type = Integer32
_AtcMcastStormCurrentTrafficRate_Object = MibTableColumn
atcMcastStormCurrentTrafficRate = _AtcMcastStormCurrentTrafficRate_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 5),
    _AtcMcastStormCurrentTrafficRate_Type()
)
atcMcastStormCurrentTrafficRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    atcMcastStormCurrentTrafficRate.setStatus("current")
_AtcMcastStormAlarmFireThreshold_Type = Integer32
_AtcMcastStormAlarmFireThreshold_Object = MibTableColumn
atcMcastStormAlarmFireThreshold = _AtcMcastStormAlarmFireThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 6),
    _AtcMcastStormAlarmFireThreshold_Type()
)
atcMcastStormAlarmFireThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormAlarmFireThreshold.setStatus("current")
_AtcMcastStormAlarmClearThreshold_Type = Integer32
_AtcMcastStormAlarmClearThreshold_Object = MibTableColumn
atcMcastStormAlarmClearThreshold = _AtcMcastStormAlarmClearThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 7),
    _AtcMcastStormAlarmClearThreshold_Type()
)
atcMcastStormAlarmClearThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormAlarmClearThreshold.setStatus("current")


class _AtcMcastStormTcAction_Type(Integer32):
    """Custom type atcMcastStormTcAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rate-control", 1),
          ("shutdown", 2))
    )


_AtcMcastStormTcAction_Type.__name__ = "Integer32"
_AtcMcastStormTcAction_Object = MibTableColumn
atcMcastStormTcAction = _AtcMcastStormTcAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 8),
    _AtcMcastStormTcAction_Type()
)
atcMcastStormTcAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormTcAction.setStatus("current")
_AtcMcastStormAlarmFireTrapStatus_Type = EnabledStatus
_AtcMcastStormAlarmFireTrapStatus_Object = MibTableColumn
atcMcastStormAlarmFireTrapStatus = _AtcMcastStormAlarmFireTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 9),
    _AtcMcastStormAlarmFireTrapStatus_Type()
)
atcMcastStormAlarmFireTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormAlarmFireTrapStatus.setStatus("current")
_AtcMcastStormAlarmClearTrapStatus_Type = EnabledStatus
_AtcMcastStormAlarmClearTrapStatus_Object = MibTableColumn
atcMcastStormAlarmClearTrapStatus = _AtcMcastStormAlarmClearTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 10),
    _AtcMcastStormAlarmClearTrapStatus_Type()
)
atcMcastStormAlarmClearTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormAlarmClearTrapStatus.setStatus("current")
_AtcMcastStormTcApplyTrapStatus_Type = EnabledStatus
_AtcMcastStormTcApplyTrapStatus_Object = MibTableColumn
atcMcastStormTcApplyTrapStatus = _AtcMcastStormTcApplyTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 11),
    _AtcMcastStormTcApplyTrapStatus_Type()
)
atcMcastStormTcApplyTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormTcApplyTrapStatus.setStatus("current")
_AtcMcastStormTcReleaseTrapStatus_Type = EnabledStatus
_AtcMcastStormTcReleaseTrapStatus_Object = MibTableColumn
atcMcastStormTcReleaseTrapStatus = _AtcMcastStormTcReleaseTrapStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 33, 5, 6, 1, 12),
    _AtcMcastStormTcReleaseTrapStatus_Type()
)
atcMcastStormTcReleaseTrapStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    atcMcastStormTcReleaseTrapStatus.setStatus("current")
_SysResourceMgt_ObjectIdentity = ObjectIdentity
sysResourceMgt = _SysResourceMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39)
)
_CpuStatus_ObjectIdentity = ObjectIdentity
cpuStatus = _CpuStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 2)
)


class _CpuCurrentUti_Type(Integer32):
    """Custom type cpuCurrentUti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpuCurrentUti_Type.__name__ = "Integer32"
_CpuCurrentUti_Object = MibScalar
cpuCurrentUti = _CpuCurrentUti_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 2, 1),
    _CpuCurrentUti_Type()
)
cpuCurrentUti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuCurrentUti.setStatus("current")
if mibBuilder.loadTexts:
    cpuCurrentUti.setUnits("%")


class _CpuStatMaxUti_Type(Integer32):
    """Custom type cpuStatMaxUti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpuStatMaxUti_Type.__name__ = "Integer32"
_CpuStatMaxUti_Object = MibScalar
cpuStatMaxUti = _CpuStatMaxUti_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 2, 2),
    _CpuStatMaxUti_Type()
)
cpuStatMaxUti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatMaxUti.setStatus("current")
if mibBuilder.loadTexts:
    cpuStatMaxUti.setUnits("%")


class _CpuStatAvgUti_Type(Integer32):
    """Custom type cpuStatAvgUti based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpuStatAvgUti_Type.__name__ = "Integer32"
_CpuStatAvgUti_Object = MibScalar
cpuStatAvgUti = _CpuStatAvgUti_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 2, 3),
    _CpuStatAvgUti_Type()
)
cpuStatAvgUti.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuStatAvgUti.setStatus("current")
if mibBuilder.loadTexts:
    cpuStatAvgUti.setUnits("%")
_CpuPeakTime_Type = DisplayString
_CpuPeakTime_Object = MibScalar
cpuPeakTime = _CpuPeakTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 2, 4),
    _CpuPeakTime_Type()
)
cpuPeakTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPeakTime.setStatus("current")
_CpuPeakDuration_Type = Integer32
_CpuPeakDuration_Object = MibScalar
cpuPeakDuration = _CpuPeakDuration_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 2, 5),
    _CpuPeakDuration_Type()
)
cpuPeakDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cpuPeakDuration.setStatus("current")
if mibBuilder.loadTexts:
    cpuPeakDuration.setUnits("second")


class _CpuUtiRisingThreshold_Type(Integer32):
    """Custom type cpuUtiRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpuUtiRisingThreshold_Type.__name__ = "Integer32"
_CpuUtiRisingThreshold_Object = MibScalar
cpuUtiRisingThreshold = _CpuUtiRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 2, 6),
    _CpuUtiRisingThreshold_Type()
)
cpuUtiRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuUtiRisingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cpuUtiRisingThreshold.setUnits("%")


class _CpuUtiFallingThreshold_Type(Integer32):
    """Custom type cpuUtiFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_CpuUtiFallingThreshold_Type.__name__ = "Integer32"
_CpuUtiFallingThreshold_Object = MibScalar
cpuUtiFallingThreshold = _CpuUtiFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 2, 7),
    _CpuUtiFallingThreshold_Type()
)
cpuUtiFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cpuUtiFallingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    cpuUtiFallingThreshold.setUnits("%")
_MemoryStatus_ObjectIdentity = ObjectIdentity
memoryStatus = _MemoryStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 3)
)
_MemoryTotal_Type = Integer32
_MemoryTotal_Object = MibScalar
memoryTotal = _MemoryTotal_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 3, 1),
    _MemoryTotal_Type()
)
memoryTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryTotal.setStatus("current")
_MemoryAllocated_Type = Integer32
_MemoryAllocated_Object = MibScalar
memoryAllocated = _MemoryAllocated_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 3, 2),
    _MemoryAllocated_Type()
)
memoryAllocated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryAllocated.setStatus("current")
_MemoryFreed_Type = Integer32
_MemoryFreed_Object = MibScalar
memoryFreed = _MemoryFreed_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 3, 3),
    _MemoryFreed_Type()
)
memoryFreed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFreed.setStatus("current")


class _MemoryFreedInPercent_Type(Integer32):
    """Custom type memoryFreedInPercent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MemoryFreedInPercent_Type.__name__ = "Integer32"
_MemoryFreedInPercent_Object = MibScalar
memoryFreedInPercent = _MemoryFreedInPercent_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 3, 4),
    _MemoryFreedInPercent_Type()
)
memoryFreedInPercent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    memoryFreedInPercent.setStatus("current")


class _MemoryUtiRisingThreshold_Type(Integer32):
    """Custom type memoryUtiRisingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MemoryUtiRisingThreshold_Type.__name__ = "Integer32"
_MemoryUtiRisingThreshold_Object = MibScalar
memoryUtiRisingThreshold = _MemoryUtiRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 3, 5),
    _MemoryUtiRisingThreshold_Type()
)
memoryUtiRisingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryUtiRisingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    memoryUtiRisingThreshold.setUnits("%")


class _MemoryUtiFallingThreshold_Type(Integer32):
    """Custom type memoryUtiFallingThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_MemoryUtiFallingThreshold_Type.__name__ = "Integer32"
_MemoryUtiFallingThreshold_Object = MibScalar
memoryUtiFallingThreshold = _MemoryUtiFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 39, 3, 6),
    _MemoryUtiFallingThreshold_Type()
)
memoryUtiFallingThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    memoryUtiFallingThreshold.setStatus("current")
if mibBuilder.loadTexts:
    memoryUtiFallingThreshold.setUnits("%")
_MvrMgt_ObjectIdentity = ObjectIdentity
mvrMgt = _MvrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44)
)
_MvrStatus_Type = EnabledStatus
_MvrStatus_Object = MibScalar
mvrStatus = _MvrStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 1),
    _MvrStatus_Type()
)
mvrStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrStatus.setStatus("current")
_MvrVlanId_Type = Integer32
_MvrVlanId_Object = MibScalar
mvrVlanId = _MvrVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 2),
    _MvrVlanId_Type()
)
mvrVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrVlanId.setStatus("current")
_MvrMaxGroups_Type = Integer32
_MvrMaxGroups_Object = MibScalar
mvrMaxGroups = _MvrMaxGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 3),
    _MvrMaxGroups_Type()
)
mvrMaxGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrMaxGroups.setStatus("current")
_MvrCurrentGroups_Type = Integer32
_MvrCurrentGroups_Object = MibScalar
mvrCurrentGroups = _MvrCurrentGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 4),
    _MvrCurrentGroups_Type()
)
mvrCurrentGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrCurrentGroups.setStatus("current")
_MvrGroupsCtl_ObjectIdentity = ObjectIdentity
mvrGroupsCtl = _MvrGroupsCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 5)
)
_MvrGroupsCtlId_Type = IpAddress
_MvrGroupsCtlId_Object = MibScalar
mvrGroupsCtlId = _MvrGroupsCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 5, 1),
    _MvrGroupsCtlId_Type()
)
mvrGroupsCtlId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupsCtlId.setStatus("current")
_MvrGroupsCtlCount_Type = Integer32
_MvrGroupsCtlCount_Object = MibScalar
mvrGroupsCtlCount = _MvrGroupsCtlCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 5, 3),
    _MvrGroupsCtlAction_Type()
)
mvrGroupsCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupsCtlAction.setStatus("current")
_MvrGroupTable_Object = MibTable
mvrGroupTable = _MvrGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 6)
)
if mibBuilder.loadTexts:
    mvrGroupTable.setStatus("current")
_MvrGroupEntry_Object = MibTableRow
mvrGroupEntry = _MvrGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 6, 1)
)
mvrGroupEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mvrGroupId"),
)
if mibBuilder.loadTexts:
    mvrGroupEntry.setStatus("current")
_MvrGroupId_Type = IpAddress
_MvrGroupId_Object = MibTableColumn
mvrGroupId = _MvrGroupId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 6, 1, 3),
    _MvrGroupStatus_Type()
)
mvrGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStatus.setStatus("current")
_MvrGroupStaticTable_Object = MibTable
mvrGroupStaticTable = _MvrGroupStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 7)
)
if mibBuilder.loadTexts:
    mvrGroupStaticTable.setStatus("current")
_MvrGroupStaticEntry_Object = MibTableRow
mvrGroupStaticEntry = _MvrGroupStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 7, 1)
)
mvrGroupStaticEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mvrGroupStaticAddress"),
)
if mibBuilder.loadTexts:
    mvrGroupStaticEntry.setStatus("current")
_MvrGroupStaticAddress_Type = IpAddress
_MvrGroupStaticAddress_Object = MibTableColumn
mvrGroupStaticAddress = _MvrGroupStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 7, 1, 1),
    _MvrGroupStaticAddress_Type()
)
mvrGroupStaticAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrGroupStaticAddress.setStatus("current")
_MvrGroupStaticPorts_Type = PortList
_MvrGroupStaticPorts_Object = MibTableColumn
mvrGroupStaticPorts = _MvrGroupStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 7, 1, 3),
    _MvrGroupStaticStatus_Type()
)
mvrGroupStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrGroupStaticStatus.setStatus("current")
_MvrGroupCurrentTable_Object = MibTable
mvrGroupCurrentTable = _MvrGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 8)
)
if mibBuilder.loadTexts:
    mvrGroupCurrentTable.setStatus("current")
_MvrGroupCurrentEntry_Object = MibTableRow
mvrGroupCurrentEntry = _MvrGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 8, 1)
)
mvrGroupCurrentEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mvrGroupCurrentAddress"),
)
if mibBuilder.loadTexts:
    mvrGroupCurrentEntry.setStatus("current")
_MvrGroupCurrentAddress_Type = IpAddress
_MvrGroupCurrentAddress_Object = MibTableColumn
mvrGroupCurrentAddress = _MvrGroupCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 8, 1, 1),
    _MvrGroupCurrentAddress_Type()
)
mvrGroupCurrentAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrGroupCurrentAddress.setStatus("current")
_MvrGroupCurrentPorts_Type = PortList
_MvrGroupCurrentPorts_Object = MibTableColumn
mvrGroupCurrentPorts = _MvrGroupCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 8, 1, 2),
    _MvrGroupCurrentPorts_Type()
)
mvrGroupCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroupCurrentPorts.setStatus("current")


class _MvrGroupCurrentReceiverVlan_Type(Integer32):
    """Custom type mvrGroupCurrentReceiverVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MvrGroupCurrentReceiverVlan_Type.__name__ = "Integer32"
_MvrGroupCurrentReceiverVlan_Object = MibTableColumn
mvrGroupCurrentReceiverVlan = _MvrGroupCurrentReceiverVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 8, 1, 3),
    _MvrGroupCurrentReceiverVlan_Type()
)
mvrGroupCurrentReceiverVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrGroupCurrentReceiverVlan.setStatus("current")
_MvrPortTable_Object = MibTable
mvrPortTable = _MvrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 9)
)
if mibBuilder.loadTexts:
    mvrPortTable.setStatus("current")
_MvrPortEntry_Object = MibTableRow
mvrPortEntry = _MvrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 9, 1)
)
mvrPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mvrIfIndex"),
)
if mibBuilder.loadTexts:
    mvrPortEntry.setStatus("current")
_MvrIfIndex_Type = InterfaceIndex
_MvrIfIndex_Object = MibTableColumn
mvrIfIndex = _MvrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 9, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 9, 1, 2),
    _MvrPortType_Type()
)
mvrPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrPortType.setStatus("current")
_MvrPortImmediateLeave_Type = EnabledStatus
_MvrPortImmediateLeave_Object = MibTableColumn
mvrPortImmediateLeave = _MvrPortImmediateLeave_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 9, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 9, 1, 4),
    _MvrPortActive_Type()
)
mvrPortActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrPortActive.setStatus("current")
_MvrRunningStatus_Type = TruthValue
_MvrRunningStatus_Object = MibScalar
mvrRunningStatus = _MvrRunningStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 10),
    _MvrRunningStatus_Type()
)
mvrRunningStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrRunningStatus.setStatus("current")


class _MvrReceiverVlanId_Type(Integer32):
    """Custom type mvrReceiverVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_MvrReceiverVlanId_Type.__name__ = "Integer32"
_MvrReceiverVlanId_Object = MibScalar
mvrReceiverVlanId = _MvrReceiverVlanId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 12),
    _MvrReceiverVlanId_Type()
)
mvrReceiverVlanId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrReceiverVlanId.setStatus("current")
_MvrMaxReceiverGroups_Type = Integer32
_MvrMaxReceiverGroups_Object = MibScalar
mvrMaxReceiverGroups = _MvrMaxReceiverGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 13),
    _MvrMaxReceiverGroups_Type()
)
mvrMaxReceiverGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrMaxReceiverGroups.setStatus("current")
_MvrCurrentReceiverGroups_Type = Integer32
_MvrCurrentReceiverGroups_Object = MibScalar
mvrCurrentReceiverGroups = _MvrCurrentReceiverGroups_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 14),
    _MvrCurrentReceiverGroups_Type()
)
mvrCurrentReceiverGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrCurrentReceiverGroups.setStatus("current")
_MvrReceiverGroupTable_Object = MibTable
mvrReceiverGroupTable = _MvrReceiverGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 15)
)
if mibBuilder.loadTexts:
    mvrReceiverGroupTable.setStatus("current")
_MvrReceiverGroupEntry_Object = MibTableRow
mvrReceiverGroupEntry = _MvrReceiverGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 15, 1)
)
mvrReceiverGroupEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mvrReceiverGroupId"),
)
if mibBuilder.loadTexts:
    mvrReceiverGroupEntry.setStatus("current")
_MvrReceiverGroupId_Type = IpAddress
_MvrReceiverGroupId_Object = MibTableColumn
mvrReceiverGroupId = _MvrReceiverGroupId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 15, 1, 1),
    _MvrReceiverGroupId_Type()
)
mvrReceiverGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrReceiverGroupId.setStatus("current")


class _MvrReceiverGroupActive_Type(Integer32):
    """Custom type mvrReceiverGroupActive based on Integer32"""
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


_MvrReceiverGroupActive_Type.__name__ = "Integer32"
_MvrReceiverGroupActive_Object = MibTableColumn
mvrReceiverGroupActive = _MvrReceiverGroupActive_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 15, 1, 2),
    _MvrReceiverGroupActive_Type()
)
mvrReceiverGroupActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrReceiverGroupActive.setStatus("current")


class _MvrReceiverGroupStatus_Type(Integer32):
    """Custom type mvrReceiverGroupStatus based on Integer32"""
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


_MvrReceiverGroupStatus_Type.__name__ = "Integer32"
_MvrReceiverGroupStatus_Object = MibTableColumn
mvrReceiverGroupStatus = _MvrReceiverGroupStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 15, 1, 3),
    _MvrReceiverGroupStatus_Type()
)
mvrReceiverGroupStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrReceiverGroupStatus.setStatus("current")
_MvrReceiverGroupStaticTable_Object = MibTable
mvrReceiverGroupStaticTable = _MvrReceiverGroupStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 16)
)
if mibBuilder.loadTexts:
    mvrReceiverGroupStaticTable.setStatus("current")
_MvrReceiverGroupStaticEntry_Object = MibTableRow
mvrReceiverGroupStaticEntry = _MvrReceiverGroupStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 16, 1)
)
mvrReceiverGroupStaticEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mvrReceiverGroupStaticAddress"),
)
if mibBuilder.loadTexts:
    mvrReceiverGroupStaticEntry.setStatus("current")
_MvrReceiverGroupStaticAddress_Type = IpAddress
_MvrReceiverGroupStaticAddress_Object = MibTableColumn
mvrReceiverGroupStaticAddress = _MvrReceiverGroupStaticAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 16, 1, 1),
    _MvrReceiverGroupStaticAddress_Type()
)
mvrReceiverGroupStaticAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrReceiverGroupStaticAddress.setStatus("current")
_MvrReceiverGroupStaticPorts_Type = PortList
_MvrReceiverGroupStaticPorts_Object = MibTableColumn
mvrReceiverGroupStaticPorts = _MvrReceiverGroupStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 16, 1, 2),
    _MvrReceiverGroupStaticPorts_Type()
)
mvrReceiverGroupStaticPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrReceiverGroupStaticPorts.setStatus("current")


class _MvrReceiverGroupStaticStatus_Type(Integer32):
    """Custom type mvrReceiverGroupStaticStatus based on Integer32"""
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


_MvrReceiverGroupStaticStatus_Type.__name__ = "Integer32"
_MvrReceiverGroupStaticStatus_Object = MibTableColumn
mvrReceiverGroupStaticStatus = _MvrReceiverGroupStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 16, 1, 3),
    _MvrReceiverGroupStaticStatus_Type()
)
mvrReceiverGroupStaticStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mvrReceiverGroupStaticStatus.setStatus("current")
_MvrReceiverGroupCurrentTable_Object = MibTable
mvrReceiverGroupCurrentTable = _MvrReceiverGroupCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 17)
)
if mibBuilder.loadTexts:
    mvrReceiverGroupCurrentTable.setStatus("current")
_MvrReceiverGroupCurrentEntry_Object = MibTableRow
mvrReceiverGroupCurrentEntry = _MvrReceiverGroupCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 17, 1)
)
mvrReceiverGroupCurrentEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "mvrReceiverGroupCurrentAddress"),
)
if mibBuilder.loadTexts:
    mvrReceiverGroupCurrentEntry.setStatus("current")
_MvrReceiverGroupCurrentAddress_Type = IpAddress
_MvrReceiverGroupCurrentAddress_Object = MibTableColumn
mvrReceiverGroupCurrentAddress = _MvrReceiverGroupCurrentAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 17, 1, 1),
    _MvrReceiverGroupCurrentAddress_Type()
)
mvrReceiverGroupCurrentAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mvrReceiverGroupCurrentAddress.setStatus("current")
_MvrReceiverGroupCurrentPorts_Type = PortList
_MvrReceiverGroupCurrentPorts_Object = MibTableColumn
mvrReceiverGroupCurrentPorts = _MvrReceiverGroupCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 44, 17, 1, 2),
    _MvrReceiverGroupCurrentPorts_Type()
)
mvrReceiverGroupCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mvrReceiverGroupCurrentPorts.setStatus("current")
_DhcpSnoopMgt_ObjectIdentity = ObjectIdentity
dhcpSnoopMgt = _DhcpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46)
)
_DhcpSnoopGlobal_ObjectIdentity = ObjectIdentity
dhcpSnoopGlobal = _DhcpSnoopGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 1)
)
_DhcpSnoopEnable_Type = EnabledStatus
_DhcpSnoopEnable_Object = MibScalar
dhcpSnoopEnable = _DhcpSnoopEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 1, 1),
    _DhcpSnoopEnable_Type()
)
dhcpSnoopEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopEnable.setStatus("current")
_DhcpSnoopVerifyMacAddressEnable_Type = EnabledStatus
_DhcpSnoopVerifyMacAddressEnable_Object = MibScalar
dhcpSnoopVerifyMacAddressEnable = _DhcpSnoopVerifyMacAddressEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 1, 2),
    _DhcpSnoopVerifyMacAddressEnable_Type()
)
dhcpSnoopVerifyMacAddressEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopVerifyMacAddressEnable.setStatus("current")
_DhcpSnoopInformationOptionEnable_Type = EnabledStatus
_DhcpSnoopInformationOptionEnable_Object = MibScalar
dhcpSnoopInformationOptionEnable = _DhcpSnoopInformationOptionEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 1, 4),
    _DhcpSnoopInformationOptionPolicy_Type()
)
dhcpSnoopInformationOptionPolicy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopInformationOptionPolicy.setStatus("current")


class _DhcpSnoopBindingsTableCtlAction_Type(Integer32):
    """Custom type dhcpSnoopBindingsTableCtlAction based on Integer32"""
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
          ("store", 2),
          ("clear", 3))
    )


_DhcpSnoopBindingsTableCtlAction_Type.__name__ = "Integer32"
_DhcpSnoopBindingsTableCtlAction_Object = MibScalar
dhcpSnoopBindingsTableCtlAction = _DhcpSnoopBindingsTableCtlAction_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 1, 5),
    _DhcpSnoopBindingsTableCtlAction_Type()
)
dhcpSnoopBindingsTableCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsTableCtlAction.setStatus("current")
_DhcpSnoopVlan_ObjectIdentity = ObjectIdentity
dhcpSnoopVlan = _DhcpSnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 2)
)
_DhcpSnoopVlanConfigTable_Object = MibTable
dhcpSnoopVlanConfigTable = _DhcpSnoopVlanConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 2, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopVlanConfigTable.setStatus("current")
_DhcpSnoopVlanConfigEntry_Object = MibTableRow
dhcpSnoopVlanConfigEntry = _DhcpSnoopVlanConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 2, 1, 1)
)
dhcpSnoopVlanConfigEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "dhcpSnoopVlanIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopVlanConfigEntry.setStatus("current")
_DhcpSnoopVlanIndex_Type = VlanIndex
_DhcpSnoopVlanIndex_Object = MibTableColumn
dhcpSnoopVlanIndex = _DhcpSnoopVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 2, 1, 1, 1),
    _DhcpSnoopVlanIndex_Type()
)
dhcpSnoopVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopVlanIndex.setStatus("current")
_DhcpSnoopVlanEnable_Type = EnabledStatus
_DhcpSnoopVlanEnable_Object = MibTableColumn
dhcpSnoopVlanEnable = _DhcpSnoopVlanEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 2, 1, 1, 2),
    _DhcpSnoopVlanEnable_Type()
)
dhcpSnoopVlanEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopVlanEnable.setStatus("current")
_DhcpSnoopInterface_ObjectIdentity = ObjectIdentity
dhcpSnoopInterface = _DhcpSnoopInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 3)
)
_DhcpSnoopPortConfigTable_Object = MibTable
dhcpSnoopPortConfigTable = _DhcpSnoopPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 3, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopPortConfigTable.setStatus("current")
_DhcpSnoopPortConfigEntry_Object = MibTableRow
dhcpSnoopPortConfigEntry = _DhcpSnoopPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 3, 1, 1)
)
dhcpSnoopPortConfigEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "dhcpSnoopPortIfIndex"),
)
if mibBuilder.loadTexts:
    dhcpSnoopPortConfigEntry.setStatus("current")
_DhcpSnoopPortIfIndex_Type = InterfaceIndex
_DhcpSnoopPortIfIndex_Object = MibTableColumn
dhcpSnoopPortIfIndex = _DhcpSnoopPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 3, 1, 1, 1),
    _DhcpSnoopPortIfIndex_Type()
)
dhcpSnoopPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopPortIfIndex.setStatus("current")
_DhcpSnoopPortTrustEnable_Type = EnabledStatus
_DhcpSnoopPortTrustEnable_Object = MibTableColumn
dhcpSnoopPortTrustEnable = _DhcpSnoopPortTrustEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 3, 1, 1, 2),
    _DhcpSnoopPortTrustEnable_Type()
)
dhcpSnoopPortTrustEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhcpSnoopPortTrustEnable.setStatus("current")
_DhcpSnoopBindings_ObjectIdentity = ObjectIdentity
dhcpSnoopBindings = _DhcpSnoopBindings_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 4)
)
_DhcpSnoopBindingsTable_Object = MibTable
dhcpSnoopBindingsTable = _DhcpSnoopBindingsTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 4, 1)
)
if mibBuilder.loadTexts:
    dhcpSnoopBindingsTable.setStatus("current")
_DhcpSnoopBindingsEntry_Object = MibTableRow
dhcpSnoopBindingsEntry = _DhcpSnoopBindingsEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 4, 1, 1)
)
dhcpSnoopBindingsEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "dhcpSnoopBindingsVlanIndex"),
    (0, "ES3552M-AND-PoE-MIB", "dhcpSnoopBindingsMacAddress"),
)
if mibBuilder.loadTexts:
    dhcpSnoopBindingsEntry.setStatus("current")
_DhcpSnoopBindingsVlanIndex_Type = VlanIndex
_DhcpSnoopBindingsVlanIndex_Object = MibTableColumn
dhcpSnoopBindingsVlanIndex = _DhcpSnoopBindingsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 4, 1, 1, 1),
    _DhcpSnoopBindingsVlanIndex_Type()
)
dhcpSnoopBindingsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsVlanIndex.setStatus("current")
_DhcpSnoopBindingsMacAddress_Type = MacAddress
_DhcpSnoopBindingsMacAddress_Object = MibTableColumn
dhcpSnoopBindingsMacAddress = _DhcpSnoopBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 4, 1, 1, 2),
    _DhcpSnoopBindingsMacAddress_Type()
)
dhcpSnoopBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsMacAddress.setStatus("current")
_DhcpSnoopBindingsAddrType_Type = InetAddressType
_DhcpSnoopBindingsAddrType_Object = MibTableColumn
dhcpSnoopBindingsAddrType = _DhcpSnoopBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 4, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 4, 1, 1, 4),
    _DhcpSnoopBindingsEntryType_Type()
)
dhcpSnoopBindingsEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsEntryType.setStatus("current")
_DhcpSnoopBindingsIpAddress_Type = IpAddress
_DhcpSnoopBindingsIpAddress_Object = MibTableColumn
dhcpSnoopBindingsIpAddress = _DhcpSnoopBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 4, 1, 1, 5),
    _DhcpSnoopBindingsIpAddress_Type()
)
dhcpSnoopBindingsIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsIpAddress.setStatus("current")
_DhcpSnoopBindingsPortIfIndex_Type = InterfaceIndex
_DhcpSnoopBindingsPortIfIndex_Object = MibTableColumn
dhcpSnoopBindingsPortIfIndex = _DhcpSnoopBindingsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 4, 1, 1, 6),
    _DhcpSnoopBindingsPortIfIndex_Type()
)
dhcpSnoopBindingsPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsPortIfIndex.setStatus("current")
_DhcpSnoopBindingsLeaseTime_Type = Unsigned32
_DhcpSnoopBindingsLeaseTime_Object = MibTableColumn
dhcpSnoopBindingsLeaseTime = _DhcpSnoopBindingsLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 4, 1, 1, 7),
    _DhcpSnoopBindingsLeaseTime_Type()
)
dhcpSnoopBindingsLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopBindingsLeaseTime.setStatus("current")
_DhcpSnoopStatistics_ObjectIdentity = ObjectIdentity
dhcpSnoopStatistics = _DhcpSnoopStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 5)
)
_DhcpSnoopTotalForwardedPkts_Type = Counter32
_DhcpSnoopTotalForwardedPkts_Object = MibScalar
dhcpSnoopTotalForwardedPkts = _DhcpSnoopTotalForwardedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 5, 1),
    _DhcpSnoopTotalForwardedPkts_Type()
)
dhcpSnoopTotalForwardedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopTotalForwardedPkts.setStatus("current")
_DhcpSnoopUntrustedPortDroppedPkts_Type = Counter32
_DhcpSnoopUntrustedPortDroppedPkts_Object = MibScalar
dhcpSnoopUntrustedPortDroppedPkts = _DhcpSnoopUntrustedPortDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 46, 5, 3),
    _DhcpSnoopUntrustedPortDroppedPkts_Type()
)
dhcpSnoopUntrustedPortDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dhcpSnoopUntrustedPortDroppedPkts.setStatus("current")
_ClusterMgt_ObjectIdentity = ObjectIdentity
clusterMgt = _ClusterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47)
)
_ClusterEnable_Type = EnabledStatus
_ClusterEnable_Object = MibScalar
clusterEnable = _ClusterEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 1),
    _ClusterEnable_Type()
)
clusterEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterEnable.setStatus("current")
_ClusterCommanderEnable_Type = EnabledStatus
_ClusterCommanderEnable_Object = MibScalar
clusterCommanderEnable = _ClusterCommanderEnable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 2),
    _ClusterCommanderEnable_Type()
)
clusterCommanderEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterCommanderEnable.setStatus("current")
_ClusterIpPool_Type = IpAddress
_ClusterIpPool_Object = MibScalar
clusterIpPool = _ClusterIpPool_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 4),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 5),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 6),
    _ClusterRole_Type()
)
clusterRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterRole.setStatus("current")
_ClusterMemberCount_Type = Counter32
_ClusterMemberCount_Object = MibScalar
clusterMemberCount = _ClusterMemberCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 7),
    _ClusterMemberCount_Type()
)
clusterMemberCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberCount.setStatus("current")
_ClusterCandidateCount_Type = Counter32
_ClusterCandidateCount_Object = MibScalar
clusterCandidateCount = _ClusterCandidateCount_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 8),
    _ClusterCandidateCount_Type()
)
clusterCandidateCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateCount.setStatus("current")
_ClusterCandidateTable_Object = MibTable
clusterCandidateTable = _ClusterCandidateTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 9)
)
if mibBuilder.loadTexts:
    clusterCandidateTable.setStatus("current")
_ClusterCandidateEntry_Object = MibTableRow
clusterCandidateEntry = _ClusterCandidateEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 9, 1)
)
clusterCandidateEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "clusterCandidateMacAddr"),
)
if mibBuilder.loadTexts:
    clusterCandidateEntry.setStatus("current")
_ClusterCandidateMacAddr_Type = MacAddress
_ClusterCandidateMacAddr_Object = MibTableColumn
clusterCandidateMacAddr = _ClusterCandidateMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 9, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 9, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 9, 1, 4),
    _ClusterCandidateRole_Type()
)
clusterCandidateRole.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterCandidateRole.setStatus("current")
_ClusterMemberTable_Object = MibTable
clusterMemberTable = _ClusterMemberTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 10)
)
if mibBuilder.loadTexts:
    clusterMemberTable.setStatus("current")
_ClusterMemberEntry_Object = MibTableRow
clusterMemberEntry = _ClusterMemberEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 10, 1)
)
clusterMemberEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "clusterMemberId"),
)
if mibBuilder.loadTexts:
    clusterMemberEntry.setStatus("current")
_ClusterMemberId_Type = Unsigned32
_ClusterMemberId_Object = MibTableColumn
clusterMemberId = _ClusterMemberId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 10, 1, 1),
    _ClusterMemberId_Type()
)
clusterMemberId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    clusterMemberId.setStatus("current")
_ClusterMemberMacAddr_Type = MacAddress
_ClusterMemberMacAddr_Object = MibTableColumn
clusterMemberMacAddr = _ClusterMemberMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 10, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 10, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 10, 1, 4),
    _ClusterMemberActive_Type()
)
clusterMemberActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    clusterMemberActive.setStatus("current")
_ClusterMemberAddCtl_ObjectIdentity = ObjectIdentity
clusterMemberAddCtl = _ClusterMemberAddCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 11)
)
_ClusterMemberAddCtlMacAddr_Type = MacAddress
_ClusterMemberAddCtlMacAddr_Object = MibScalar
clusterMemberAddCtlMacAddr = _ClusterMemberAddCtlMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 11, 1),
    _ClusterMemberAddCtlMacAddr_Type()
)
clusterMemberAddCtlMacAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberAddCtlMacAddr.setStatus("current")
_ClusterMemberAddCtlId_Type = Unsigned32
_ClusterMemberAddCtlId_Object = MibScalar
clusterMemberAddCtlId = _ClusterMemberAddCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 11, 2),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 11, 5),
    _ClusterMemberAddCtlAction_Type()
)
clusterMemberAddCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberAddCtlAction.setStatus("current")
_ClusterMemberRemoveCtl_ObjectIdentity = ObjectIdentity
clusterMemberRemoveCtl = _ClusterMemberRemoveCtl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 12)
)
_ClusterMemberRemoveCtlId_Type = Unsigned32
_ClusterMemberRemoveCtlId_Object = MibScalar
clusterMemberRemoveCtlId = _ClusterMemberRemoveCtlId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 12, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 47, 12, 2),
    _ClusterMemberRemoveCtlAction_Type()
)
clusterMemberRemoveCtlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    clusterMemberRemoveCtlAction.setStatus("current")
_IpSrcGuardMgt_ObjectIdentity = ObjectIdentity
ipSrcGuardMgt = _IpSrcGuardMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48)
)
_IpSrcGuardConfigTable_Object = MibTable
ipSrcGuardConfigTable = _IpSrcGuardConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 1)
)
if mibBuilder.loadTexts:
    ipSrcGuardConfigTable.setStatus("current")
_IpSrcGuardConfigEntry_Object = MibTableRow
ipSrcGuardConfigEntry = _IpSrcGuardConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 1, 1)
)
ipSrcGuardConfigEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "ipSrcGuardPortIfIndex"),
)
if mibBuilder.loadTexts:
    ipSrcGuardConfigEntry.setStatus("current")
_IpSrcGuardPortIfIndex_Type = InterfaceIndex
_IpSrcGuardPortIfIndex_Object = MibTableColumn
ipSrcGuardPortIfIndex = _IpSrcGuardPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 1, 1, 2),
    _IpSrcGuardMode_Type()
)
ipSrcGuardMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipSrcGuardMode.setStatus("current")
_IpSrcGuardAddrTable_Object = MibTable
ipSrcGuardAddrTable = _IpSrcGuardAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 2)
)
if mibBuilder.loadTexts:
    ipSrcGuardAddrTable.setStatus("current")
_IpSrcGuardAddrEntry_Object = MibTableRow
ipSrcGuardAddrEntry = _IpSrcGuardAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 2, 1)
)
ipSrcGuardAddrEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "ipSrcGuardBindingsVlanIndex"),
    (0, "ES3552M-AND-PoE-MIB", "ipSrcGuardBindingsMacAddress"),
)
if mibBuilder.loadTexts:
    ipSrcGuardAddrEntry.setStatus("current")
_IpSrcGuardBindingsVlanIndex_Type = VlanIndex
_IpSrcGuardBindingsVlanIndex_Object = MibTableColumn
ipSrcGuardBindingsVlanIndex = _IpSrcGuardBindingsVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 2, 1, 1),
    _IpSrcGuardBindingsVlanIndex_Type()
)
ipSrcGuardBindingsVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsVlanIndex.setStatus("current")
_IpSrcGuardBindingsMacAddress_Type = MacAddress
_IpSrcGuardBindingsMacAddress_Object = MibTableColumn
ipSrcGuardBindingsMacAddress = _IpSrcGuardBindingsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 2, 1, 2),
    _IpSrcGuardBindingsMacAddress_Type()
)
ipSrcGuardBindingsMacAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsMacAddress.setStatus("current")
_IpSrcGuardBindingsAddrType_Type = InetAddressType
_IpSrcGuardBindingsAddrType_Object = MibTableColumn
ipSrcGuardBindingsAddrType = _IpSrcGuardBindingsAddrType_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 2, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 2, 1, 4),
    _IpSrcGuardBindingsEntryType_Type()
)
ipSrcGuardBindingsEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsEntryType.setStatus("current")
_IpSrcGuardBindingsIpAddress_Type = IpAddress
_IpSrcGuardBindingsIpAddress_Object = MibTableColumn
ipSrcGuardBindingsIpAddress = _IpSrcGuardBindingsIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 2, 1, 5),
    _IpSrcGuardBindingsIpAddress_Type()
)
ipSrcGuardBindingsIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsIpAddress.setStatus("current")
_IpSrcGuardBindingsPortIfIndex_Type = InterfaceIndex
_IpSrcGuardBindingsPortIfIndex_Object = MibTableColumn
ipSrcGuardBindingsPortIfIndex = _IpSrcGuardBindingsPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 2, 1, 6),
    _IpSrcGuardBindingsPortIfIndex_Type()
)
ipSrcGuardBindingsPortIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsPortIfIndex.setStatus("current")
_IpSrcGuardBindingsLeaseTime_Type = Unsigned32
_IpSrcGuardBindingsLeaseTime_Object = MibTableColumn
ipSrcGuardBindingsLeaseTime = _IpSrcGuardBindingsLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 2, 1, 7),
    _IpSrcGuardBindingsLeaseTime_Type()
)
ipSrcGuardBindingsLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsLeaseTime.setStatus("current")
_IpSrcGuardBindingsStatus_Type = RowStatus
_IpSrcGuardBindingsStatus_Object = MibTableColumn
ipSrcGuardBindingsStatus = _IpSrcGuardBindingsStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 48, 2, 1, 8),
    _IpSrcGuardBindingsStatus_Type()
)
ipSrcGuardBindingsStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipSrcGuardBindingsStatus.setStatus("current")
_UpnpMgt_ObjectIdentity = ObjectIdentity
upnpMgt = _UpnpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 49)
)
_UpnpStatus_Type = EnabledStatus
_UpnpStatus_Object = MibScalar
upnpStatus = _UpnpStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 49, 1),
    _UpnpStatus_Type()
)
upnpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upnpStatus.setStatus("current")


class _UpnpAdvertisingDuration_Type(Integer32):
    """Custom type upnpAdvertisingDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 86400),
    )


_UpnpAdvertisingDuration_Type.__name__ = "Integer32"
_UpnpAdvertisingDuration_Object = MibScalar
upnpAdvertisingDuration = _UpnpAdvertisingDuration_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 49, 2),
    _UpnpAdvertisingDuration_Type()
)
upnpAdvertisingDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upnpAdvertisingDuration.setStatus("current")


class _UpnpTtl_Type(Integer32):
    """Custom type upnpTtl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_UpnpTtl_Type.__name__ = "Integer32"
_UpnpTtl_Object = MibScalar
upnpTtl = _UpnpTtl_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 49, 3),
    _UpnpTtl_Type()
)
upnpTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    upnpTtl.setStatus("current")
_SFlowMgt_ObjectIdentity = ObjectIdentity
sFlowMgt = _SFlowMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 55)
)
_SFlowStatus_Type = EnabledStatus
_SFlowStatus_Object = MibScalar
sFlowStatus = _SFlowStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 55, 1),
    _SFlowStatus_Type()
)
sFlowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sFlowStatus.setStatus("current")
_SFlowPortTable_Object = MibTable
sFlowPortTable = _SFlowPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 55, 2)
)
if mibBuilder.loadTexts:
    sFlowPortTable.setStatus("current")
_SFlowPortEntry_Object = MibTableRow
sFlowPortEntry = _SFlowPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 55, 2, 1)
)
sFlowPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "sFlowPortIndex"),
)
if mibBuilder.loadTexts:
    sFlowPortEntry.setStatus("current")
_SFlowPortIndex_Type = Integer32
_SFlowPortIndex_Object = MibTableColumn
sFlowPortIndex = _SFlowPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 55, 2, 1, 1),
    _SFlowPortIndex_Type()
)
sFlowPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sFlowPortIndex.setStatus("current")
_SFlowPortStatus_Type = EnabledStatus
_SFlowPortStatus_Object = MibTableColumn
sFlowPortStatus = _SFlowPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 55, 2, 1, 2),
    _SFlowPortStatus_Type()
)
sFlowPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    sFlowPortStatus.setStatus("current")
_DynamicArpInspectionMgt_ObjectIdentity = ObjectIdentity
dynamicArpInspectionMgt = _DynamicArpInspectionMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56)
)
_DaiGlobal_ObjectIdentity = ObjectIdentity
daiGlobal = _DaiGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 1)
)
_DaiGlobalStatus_Type = EnabledStatus
_DaiGlobalStatus_Object = MibScalar
daiGlobalStatus = _DaiGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 1, 1),
    _DaiGlobalStatus_Type()
)
daiGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalStatus.setStatus("current")
_DaiGlobalSrcMacValidation_Type = EnabledStatus
_DaiGlobalSrcMacValidation_Object = MibScalar
daiGlobalSrcMacValidation = _DaiGlobalSrcMacValidation_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 1, 2),
    _DaiGlobalSrcMacValidation_Type()
)
daiGlobalSrcMacValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalSrcMacValidation.setStatus("current")
_DaiGlobalDestMacValidation_Type = EnabledStatus
_DaiGlobalDestMacValidation_Object = MibScalar
daiGlobalDestMacValidation = _DaiGlobalDestMacValidation_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 1, 3),
    _DaiGlobalDestMacValidation_Type()
)
daiGlobalDestMacValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalDestMacValidation.setStatus("current")
_DaiGlobalIpAddrValidation_Type = EnabledStatus
_DaiGlobalIpAddrValidation_Object = MibScalar
daiGlobalIpAddrValidation = _DaiGlobalIpAddrValidation_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 1, 4),
    _DaiGlobalIpAddrValidation_Type()
)
daiGlobalIpAddrValidation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalIpAddrValidation.setStatus("current")


class _DaiGlobalLogNumber_Type(Integer32):
    """Custom type daiGlobalLogNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_DaiGlobalLogNumber_Type.__name__ = "Integer32"
_DaiGlobalLogNumber_Object = MibScalar
daiGlobalLogNumber = _DaiGlobalLogNumber_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 1, 5),
    _DaiGlobalLogNumber_Type()
)
daiGlobalLogNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalLogNumber.setStatus("current")


class _DaiGlobalLogInterval_Type(Integer32):
    """Custom type daiGlobalLogInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 86400),
    )


_DaiGlobalLogInterval_Type.__name__ = "Integer32"
_DaiGlobalLogInterval_Object = MibScalar
daiGlobalLogInterval = _DaiGlobalLogInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 1, 6),
    _DaiGlobalLogInterval_Type()
)
daiGlobalLogInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiGlobalLogInterval.setStatus("current")
_DaiGlobalAdditionalValidStatus_Type = EnabledStatus
_DaiGlobalAdditionalValidStatus_Object = MibScalar
daiGlobalAdditionalValidStatus = _DaiGlobalAdditionalValidStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 1, 7),
    _DaiGlobalAdditionalValidStatus_Type()
)
daiGlobalAdditionalValidStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiGlobalAdditionalValidStatus.setStatus("current")
_DaiVlan_ObjectIdentity = ObjectIdentity
daiVlan = _DaiVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 2)
)
_DaiVlanTable_Object = MibTable
daiVlanTable = _DaiVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 2, 1)
)
if mibBuilder.loadTexts:
    daiVlanTable.setStatus("current")
_DaiVlanEntry_Object = MibTableRow
daiVlanEntry = _DaiVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 2, 1, 1)
)
daiVlanEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "daiVlanIndex"),
)
if mibBuilder.loadTexts:
    daiVlanEntry.setStatus("current")
_DaiVlanIndex_Type = VlanIndex
_DaiVlanIndex_Object = MibTableColumn
daiVlanIndex = _DaiVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 2, 1, 1, 1),
    _DaiVlanIndex_Type()
)
daiVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    daiVlanIndex.setStatus("current")
_DaiVlanStatus_Type = EnabledStatus
_DaiVlanStatus_Object = MibTableColumn
daiVlanStatus = _DaiVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 2, 1, 1, 2),
    _DaiVlanStatus_Type()
)
daiVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiVlanStatus.setStatus("current")


class _DaiVlanArpAclName_Type(DisplayString):
    """Custom type daiVlanArpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_DaiVlanArpAclName_Type.__name__ = "DisplayString"
_DaiVlanArpAclName_Object = MibTableColumn
daiVlanArpAclName = _DaiVlanArpAclName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 2, 1, 1, 3),
    _DaiVlanArpAclName_Type()
)
daiVlanArpAclName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiVlanArpAclName.setStatus("current")


class _DaiVlanArpAclStatus_Type(Integer32):
    """Custom type daiVlanArpAclStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2))
    )


_DaiVlanArpAclStatus_Type.__name__ = "Integer32"
_DaiVlanArpAclStatus_Object = MibTableColumn
daiVlanArpAclStatus = _DaiVlanArpAclStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 2, 1, 1, 4),
    _DaiVlanArpAclStatus_Type()
)
daiVlanArpAclStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiVlanArpAclStatus.setStatus("current")
_DaiInterface_ObjectIdentity = ObjectIdentity
daiInterface = _DaiInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 3)
)
_DaiPortTable_Object = MibTable
daiPortTable = _DaiPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 3, 1)
)
if mibBuilder.loadTexts:
    daiPortTable.setStatus("current")
_DaiPortEntry_Object = MibTableRow
daiPortEntry = _DaiPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 3, 1, 1)
)
daiPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "daiPortIfIndex"),
)
if mibBuilder.loadTexts:
    daiPortEntry.setStatus("current")
_DaiPortIfIndex_Type = InterfaceIndex
_DaiPortIfIndex_Object = MibTableColumn
daiPortIfIndex = _DaiPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 3, 1, 1, 1),
    _DaiPortIfIndex_Type()
)
daiPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    daiPortIfIndex.setStatus("current")
_DaiPortTrustStatus_Type = EnabledStatus
_DaiPortTrustStatus_Object = MibTableColumn
daiPortTrustStatus = _DaiPortTrustStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 3, 1, 1, 2),
    _DaiPortTrustStatus_Type()
)
daiPortTrustStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiPortTrustStatus.setStatus("current")


class _DaiPortRateLimit_Type(Unsigned32):
    """Custom type daiPortRateLimit based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2048),
        ValueRangeConstraint(4294967295, 4294967295),
    )


_DaiPortRateLimit_Type.__name__ = "Unsigned32"
_DaiPortRateLimit_Object = MibTableColumn
daiPortRateLimit = _DaiPortRateLimit_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 3, 1, 1, 3),
    _DaiPortRateLimit_Type()
)
daiPortRateLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    daiPortRateLimit.setStatus("current")
_DaiLog_ObjectIdentity = ObjectIdentity
daiLog = _DaiLog_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 4)
)
_DaiLogTable_Object = MibTable
daiLogTable = _DaiLogTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 4, 1)
)
if mibBuilder.loadTexts:
    daiLogTable.setStatus("current")
_DaiLogEntry_Object = MibTableRow
daiLogEntry = _DaiLogEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 4, 1, 1)
)
daiLogEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "daiLogIndex"),
)
if mibBuilder.loadTexts:
    daiLogEntry.setStatus("current")
_DaiLogIndex_Type = Integer32
_DaiLogIndex_Object = MibTableColumn
daiLogIndex = _DaiLogIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 4, 1, 1, 1),
    _DaiLogIndex_Type()
)
daiLogIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    daiLogIndex.setStatus("current")
_DaiLogVlan_Type = VlanIndex
_DaiLogVlan_Object = MibTableColumn
daiLogVlan = _DaiLogVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 4, 1, 1, 2),
    _DaiLogVlan_Type()
)
daiLogVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogVlan.setStatus("current")
_DaiLogPort_Type = InterfaceIndex
_DaiLogPort_Object = MibTableColumn
daiLogPort = _DaiLogPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 4, 1, 1, 3),
    _DaiLogPort_Type()
)
daiLogPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogPort.setStatus("current")
_DaiLogSrcIpAddress_Type = IpAddress
_DaiLogSrcIpAddress_Object = MibTableColumn
daiLogSrcIpAddress = _DaiLogSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 4, 1, 1, 4),
    _DaiLogSrcIpAddress_Type()
)
daiLogSrcIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogSrcIpAddress.setStatus("current")
_DaiLogDestIpAddress_Type = IpAddress
_DaiLogDestIpAddress_Object = MibTableColumn
daiLogDestIpAddress = _DaiLogDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 4, 1, 1, 5),
    _DaiLogDestIpAddress_Type()
)
daiLogDestIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogDestIpAddress.setStatus("current")
_DaiLogSrcMacAddress_Type = MacAddress
_DaiLogSrcMacAddress_Object = MibTableColumn
daiLogSrcMacAddress = _DaiLogSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 4, 1, 1, 6),
    _DaiLogSrcMacAddress_Type()
)
daiLogSrcMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogSrcMacAddress.setStatus("current")
_DaiLogDestMacAddress_Type = MacAddress
_DaiLogDestMacAddress_Object = MibTableColumn
daiLogDestMacAddress = _DaiLogDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 4, 1, 1, 7),
    _DaiLogDestMacAddress_Type()
)
daiLogDestMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiLogDestMacAddress.setStatus("current")
_DaiStatistics_ObjectIdentity = ObjectIdentity
daiStatistics = _DaiStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 5)
)
_DaiTotalReceivedPkts_Type = Counter32
_DaiTotalReceivedPkts_Object = MibScalar
daiTotalReceivedPkts = _DaiTotalReceivedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 5, 1),
    _DaiTotalReceivedPkts_Type()
)
daiTotalReceivedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalReceivedPkts.setStatus("current")
_DaiTotalDroppedPkts_Type = Counter32
_DaiTotalDroppedPkts_Object = MibScalar
daiTotalDroppedPkts = _DaiTotalDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 5, 2),
    _DaiTotalDroppedPkts_Type()
)
daiTotalDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalDroppedPkts.setStatus("current")
_DaiTotalProcessedPkts_Type = Counter32
_DaiTotalProcessedPkts_Object = MibScalar
daiTotalProcessedPkts = _DaiTotalProcessedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 5, 3),
    _DaiTotalProcessedPkts_Type()
)
daiTotalProcessedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalProcessedPkts.setStatus("current")
_DaiTotalSrcMacDroppedPkts_Type = Counter32
_DaiTotalSrcMacDroppedPkts_Object = MibScalar
daiTotalSrcMacDroppedPkts = _DaiTotalSrcMacDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 5, 4),
    _DaiTotalSrcMacDroppedPkts_Type()
)
daiTotalSrcMacDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalSrcMacDroppedPkts.setStatus("current")
_DaiTotalDestMacDroppedPkts_Type = Counter32
_DaiTotalDestMacDroppedPkts_Object = MibScalar
daiTotalDestMacDroppedPkts = _DaiTotalDestMacDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 5, 5),
    _DaiTotalDestMacDroppedPkts_Type()
)
daiTotalDestMacDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalDestMacDroppedPkts.setStatus("current")
_DaiTotalIpAddrDroppedPkts_Type = Counter32
_DaiTotalIpAddrDroppedPkts_Object = MibScalar
daiTotalIpAddrDroppedPkts = _DaiTotalIpAddrDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 5, 6),
    _DaiTotalIpAddrDroppedPkts_Type()
)
daiTotalIpAddrDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalIpAddrDroppedPkts.setStatus("current")
_DaiTotalArpAclDroppedPkts_Type = Counter32
_DaiTotalArpAclDroppedPkts_Object = MibScalar
daiTotalArpAclDroppedPkts = _DaiTotalArpAclDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 5, 7),
    _DaiTotalArpAclDroppedPkts_Type()
)
daiTotalArpAclDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalArpAclDroppedPkts.setStatus("current")
_DaiTotalDhcpSnoopingDroppedPkts_Type = Counter32
_DaiTotalDhcpSnoopingDroppedPkts_Object = MibScalar
daiTotalDhcpSnoopingDroppedPkts = _DaiTotalDhcpSnoopingDroppedPkts_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 56, 5, 8),
    _DaiTotalDhcpSnoopingDroppedPkts_Type()
)
daiTotalDhcpSnoopingDroppedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    daiTotalDhcpSnoopingDroppedPkts.setStatus("current")
_ErpsMgt_ObjectIdentity = ObjectIdentity
erpsMgt = _ErpsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62)
)


class _ErpsGlobalStatus_Type(Integer32):
    """Custom type erpsGlobalStatus based on Integer32"""
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


_ErpsGlobalStatus_Type.__name__ = "Integer32"
_ErpsGlobalStatus_Object = MibScalar
erpsGlobalStatus = _ErpsGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 1),
    _ErpsGlobalStatus_Type()
)
erpsGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    erpsGlobalStatus.setStatus("current")
_ErpsDomainTable_Object = MibTable
erpsDomainTable = _ErpsDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2)
)
if mibBuilder.loadTexts:
    erpsDomainTable.setStatus("current")
_ErpsDomainEntry_Object = MibTableRow
erpsDomainEntry = _ErpsDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1)
)
erpsDomainEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "erpsDomainIndex"),
)
if mibBuilder.loadTexts:
    erpsDomainEntry.setStatus("current")


class _ErpsDomainIndex_Type(Integer32):
    """Custom type erpsDomainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ErpsDomainIndex_Type.__name__ = "Integer32"
_ErpsDomainIndex_Object = MibTableColumn
erpsDomainIndex = _ErpsDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 1),
    _ErpsDomainIndex_Type()
)
erpsDomainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    erpsDomainIndex.setStatus("current")


class _ErpsDomainName_Type(DisplayString):
    """Custom type erpsDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 12),
    )


_ErpsDomainName_Type.__name__ = "DisplayString"
_ErpsDomainName_Object = MibTableColumn
erpsDomainName = _ErpsDomainName_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 2),
    _ErpsDomainName_Type()
)
erpsDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainName.setStatus("current")


class _ErpsDomainMegLevel_Type(Integer32):
    """Custom type erpsDomainMegLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ErpsDomainMegLevel_Type.__name__ = "Integer32"
_ErpsDomainMegLevel_Object = MibTableColumn
erpsDomainMegLevel = _ErpsDomainMegLevel_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 3),
    _ErpsDomainMegLevel_Type()
)
erpsDomainMegLevel.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainMegLevel.setStatus("current")
_ErpsDomainNodeId_Type = MacAddress
_ErpsDomainNodeId_Object = MibTableColumn
erpsDomainNodeId = _ErpsDomainNodeId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 4),
    _ErpsDomainNodeId_Type()
)
erpsDomainNodeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainNodeId.setStatus("current")
_ErpsDomainWestRingPort_Type = Integer32
_ErpsDomainWestRingPort_Object = MibTableColumn
erpsDomainWestRingPort = _ErpsDomainWestRingPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 5),
    _ErpsDomainWestRingPort_Type()
)
erpsDomainWestRingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainWestRingPort.setStatus("current")
_ErpsDomainEastRingPort_Type = Integer32
_ErpsDomainEastRingPort_Object = MibTableColumn
erpsDomainEastRingPort = _ErpsDomainEastRingPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 6),
    _ErpsDomainEastRingPort_Type()
)
erpsDomainEastRingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainEastRingPort.setStatus("current")


class _ErpsDomainRplOwner_Type(Integer32):
    """Custom type erpsDomainRplOwner based on Integer32"""
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


_ErpsDomainRplOwner_Type.__name__ = "Integer32"
_ErpsDomainRplOwner_Object = MibTableColumn
erpsDomainRplOwner = _ErpsDomainRplOwner_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 7),
    _ErpsDomainRplOwner_Type()
)
erpsDomainRplOwner.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainRplOwner.setStatus("current")


class _ErpsDomainRplPort_Type(Integer32):
    """Custom type erpsDomainRplPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("west", 2),
          ("east", 3))
    )


_ErpsDomainRplPort_Type.__name__ = "Integer32"
_ErpsDomainRplPort_Object = MibTableColumn
erpsDomainRplPort = _ErpsDomainRplPort_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 8),
    _ErpsDomainRplPort_Type()
)
erpsDomainRplPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDomainRplPort.setStatus("current")


class _ErpsDomainGuardTimer_Type(Integer32):
    """Custom type erpsDomainGuardTimer based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 2000),
    )


_ErpsDomainGuardTimer_Type.__name__ = "Integer32"
_ErpsDomainGuardTimer_Object = MibTableColumn
erpsDomainGuardTimer = _ErpsDomainGuardTimer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 9),
    _ErpsDomainGuardTimer_Type()
)
erpsDomainGuardTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainGuardTimer.setStatus("current")


class _ErpsDomainHoldoffTimer_Type(Integer32):
    """Custom type erpsDomainHoldoffTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10000),
    )


_ErpsDomainHoldoffTimer_Type.__name__ = "Integer32"
_ErpsDomainHoldoffTimer_Object = MibTableColumn
erpsDomainHoldoffTimer = _ErpsDomainHoldoffTimer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 10),
    _ErpsDomainHoldoffTimer_Type()
)
erpsDomainHoldoffTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainHoldoffTimer.setStatus("current")


class _ErpsDomainWtrTimer_Type(Integer32):
    """Custom type erpsDomainWtrTimer based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 12),
    )


_ErpsDomainWtrTimer_Type.__name__ = "Integer32"
_ErpsDomainWtrTimer_Object = MibTableColumn
erpsDomainWtrTimer = _ErpsDomainWtrTimer_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 11),
    _ErpsDomainWtrTimer_Type()
)
erpsDomainWtrTimer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainWtrTimer.setStatus("current")
_ErpsDomainControlVlanID_Type = Integer32
_ErpsDomainControlVlanID_Object = MibTableColumn
erpsDomainControlVlanID = _ErpsDomainControlVlanID_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 12),
    _ErpsDomainControlVlanID_Type()
)
erpsDomainControlVlanID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainControlVlanID.setStatus("current")


class _ErpsDomainNodeState_Type(Integer32):
    """Custom type erpsDomainNodeState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("init", 1),
          ("idle", 2),
          ("protection", 3))
    )


_ErpsDomainNodeState_Type.__name__ = "Integer32"
_ErpsDomainNodeState_Object = MibTableColumn
erpsDomainNodeState = _ErpsDomainNodeState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 13),
    _ErpsDomainNodeState_Type()
)
erpsDomainNodeState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDomainNodeState.setStatus("current")


class _ErpsDomainWestRingPortState_Type(Integer32):
    """Custom type erpsDomainWestRingPortState based on Integer32"""
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
          ("blocking", 2),
          ("forwarding", 3))
    )


_ErpsDomainWestRingPortState_Type.__name__ = "Integer32"
_ErpsDomainWestRingPortState_Object = MibTableColumn
erpsDomainWestRingPortState = _ErpsDomainWestRingPortState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 14),
    _ErpsDomainWestRingPortState_Type()
)
erpsDomainWestRingPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDomainWestRingPortState.setStatus("current")


class _ErpsDomainEastRingPortState_Type(Integer32):
    """Custom type erpsDomainEastRingPortState based on Integer32"""
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
          ("blocking", 2),
          ("forwarding", 3))
    )


_ErpsDomainEastRingPortState_Type.__name__ = "Integer32"
_ErpsDomainEastRingPortState_Object = MibTableColumn
erpsDomainEastRingPortState = _ErpsDomainEastRingPortState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 15),
    _ErpsDomainEastRingPortState_Type()
)
erpsDomainEastRingPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    erpsDomainEastRingPortState.setStatus("current")
_ErpsDomainRowStatus_Type = RowStatus
_ErpsDomainRowStatus_Object = MibTableColumn
erpsDomainRowStatus = _ErpsDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 16),
    _ErpsDomainRowStatus_Type()
)
erpsDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainRowStatus.setStatus("current")
_ErpsDomainMajorDomainIndex_Type = Integer32
_ErpsDomainMajorDomainIndex_Object = MibTableColumn
erpsDomainMajorDomainIndex = _ErpsDomainMajorDomainIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 17),
    _ErpsDomainMajorDomainIndex_Type()
)
erpsDomainMajorDomainIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainMajorDomainIndex.setStatus("current")


class _ErpsDomainPropagateTC_Type(Integer32):
    """Custom type erpsDomainPropagateTC based on Integer32"""
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


_ErpsDomainPropagateTC_Type.__name__ = "Integer32"
_ErpsDomainPropagateTC_Object = MibTableColumn
erpsDomainPropagateTC = _ErpsDomainPropagateTC_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 18),
    _ErpsDomainPropagateTC_Type()
)
erpsDomainPropagateTC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainPropagateTC.setStatus("current")


class _ErpsDomainWestMepId_Type(Integer32):
    """Custom type erpsDomainWestMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ErpsDomainWestMepId_Type.__name__ = "Integer32"
_ErpsDomainWestMepId_Object = MibTableColumn
erpsDomainWestMepId = _ErpsDomainWestMepId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 20),
    _ErpsDomainWestMepId_Type()
)
erpsDomainWestMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainWestMepId.setStatus("current")


class _ErpsDomainEastMepId_Type(Integer32):
    """Custom type erpsDomainEastMepId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_ErpsDomainEastMepId_Type.__name__ = "Integer32"
_ErpsDomainEastMepId_Object = MibTableColumn
erpsDomainEastMepId = _ErpsDomainEastMepId_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 21),
    _ErpsDomainEastMepId_Type()
)
erpsDomainEastMepId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainEastMepId.setStatus("current")


class _ErpsDomainNonErpsDevProtect_Type(Integer32):
    """Custom type erpsDomainNonErpsDevProtect based on Integer32"""
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


_ErpsDomainNonErpsDevProtect_Type.__name__ = "Integer32"
_ErpsDomainNonErpsDevProtect_Object = MibTableColumn
erpsDomainNonErpsDevProtect = _ErpsDomainNonErpsDevProtect_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 62, 2, 1, 22),
    _ErpsDomainNonErpsDevProtect_Type()
)
erpsDomainNonErpsDevProtect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    erpsDomainNonErpsDevProtect.setStatus("current")
_LbdMgt_ObjectIdentity = ObjectIdentity
lbdMgt = _LbdMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63)
)
_LbdGlobal_ObjectIdentity = ObjectIdentity
lbdGlobal = _LbdGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 1)
)


class _LbdGlobalStatus_Type(Integer32):
    """Custom type lbdGlobalStatus based on Integer32"""
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


_LbdGlobalStatus_Type.__name__ = "Integer32"
_LbdGlobalStatus_Object = MibScalar
lbdGlobalStatus = _LbdGlobalStatus_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 1, 1),
    _LbdGlobalStatus_Type()
)
lbdGlobalStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdGlobalStatus.setStatus("current")


class _LbdTransmitInterval_Type(Unsigned32):
    """Custom type lbdTransmitInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32767),
    )


_LbdTransmitInterval_Type.__name__ = "Unsigned32"
_LbdTransmitInterval_Object = MibScalar
lbdTransmitInterval = _LbdTransmitInterval_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 1, 2),
    _LbdTransmitInterval_Type()
)
lbdTransmitInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdTransmitInterval.setStatus("current")


class _LbdRecoverTime_Type(Unsigned32):
    """Custom type lbdRecoverTime based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 1000000),
    )


_LbdRecoverTime_Type.__name__ = "Unsigned32"
_LbdRecoverTime_Object = MibScalar
lbdRecoverTime = _LbdRecoverTime_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 1, 3),
    _LbdRecoverTime_Type()
)
lbdRecoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdRecoverTime.setStatus("current")


class _LbdMode_Type(Integer32):
    """Custom type lbdMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("port-based", 1),
          ("VLAN-based", 2))
    )


_LbdMode_Type.__name__ = "Integer32"
_LbdMode_Object = MibScalar
lbdMode = _LbdMode_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 1, 4),
    _LbdMode_Type()
)
lbdMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdMode.setStatus("current")
_LbdInterface_ObjectIdentity = ObjectIdentity
lbdInterface = _LbdInterface_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 2)
)
_LbdPortTable_Object = MibTable
lbdPortTable = _LbdPortTable_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 2, 1)
)
if mibBuilder.loadTexts:
    lbdPortTable.setStatus("current")
_LbdPortEntry_Object = MibTableRow
lbdPortEntry = _LbdPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 2, 1, 1)
)
lbdPortEntry.setIndexNames(
    (0, "ES3552M-AND-PoE-MIB", "lbdPortIfIndex"),
)
if mibBuilder.loadTexts:
    lbdPortEntry.setStatus("current")
_LbdPortIfIndex_Type = InterfaceIndex
_LbdPortIfIndex_Object = MibTableColumn
lbdPortIfIndex = _LbdPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 2, 1, 1, 1),
    _LbdPortIfIndex_Type()
)
lbdPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lbdPortIfIndex.setStatus("current")


class _LbdPortAdminState_Type(Integer32):
    """Custom type lbdPortAdminState based on Integer32"""
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


_LbdPortAdminState_Type.__name__ = "Integer32"
_LbdPortAdminState_Object = MibTableColumn
lbdPortAdminState = _LbdPortAdminState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 2, 1, 1, 2),
    _LbdPortAdminState_Type()
)
lbdPortAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lbdPortAdminState.setStatus("current")


class _LbdPortOperState_Type(Integer32):
    """Custom type lbdPortOperState based on Integer32"""
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
          ("normal", 2),
          ("looped", 3))
    )


_LbdPortOperState_Type.__name__ = "Integer32"
_LbdPortOperState_Object = MibTableColumn
lbdPortOperState = _LbdPortOperState_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 2, 1, 1, 3),
    _LbdPortOperState_Type()
)
lbdPortOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbdPortOperState.setStatus("current")


class _LbdPortLoopedVlan_Type(OctetString):
    """Custom type lbdPortLoopedVlan based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_LbdPortLoopedVlan_Type.__name__ = "OctetString"
_LbdPortLoopedVlan_Object = MibTableColumn
lbdPortLoopedVlan = _LbdPortLoopedVlan_Object(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 1, 63, 2, 1, 1, 4),
    _LbdPortLoopedVlan_Type()
)
lbdPortLoopedVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lbdPortLoopedVlan.setStatus("current")
_Es3552m_and_poeNotifications_ObjectIdentity = ObjectIdentity
es3552m_and_poeNotifications = _Es3552m_and_poeNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2)
)
_Es3552m_and_poeTraps_ObjectIdentity = ObjectIdentity
es3552m_and_poeTraps = _Es3552m_and_poeTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1)
)
_Es3552m_and_poeTrapsPrefix_ObjectIdentity = ObjectIdentity
es3552m_and_poeTrapsPrefix = _Es3552m_and_poeTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0)
)
_Es3552m_and_poeConformance_ObjectIdentity = ObjectIdentity
es3552m_and_poeConformance = _Es3552m_and_poeConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 3)
)
dot1dStpPortEntry.registerAugmentions(
    ("ES3552M-AND-PoE-MIB",
     "staPortEntry")
)
staPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())
dot1xAuthConfigEntry.registerAugmentions(
    ("ES3552M-AND-PoE-MIB",
     "dot1xAuthConfigExtEntry")
)
dot1xAuthConfigExtEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())

# Managed Objects groups


# Notification objects

swPowerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 1)
)
swPowerStatusChangeTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "swIndivPowerUnitIndex"),
        ("ES3552M-AND-PoE-MIB", "swIndivPowerIndex"),
        ("ES3552M-AND-PoE-MIB", "swIndivPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerStatusChangeTrap.setStatus(
        "current"
    )

swPortSecurityTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 36)
)
swPortSecurityTrap.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    swPortSecurityTrap.setStatus(
        "current"
    )

swIpFilterRejectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 40)
)
swIpFilterRejectTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "trapIpFilterRejectMode"),
        ("ES3552M-AND-PoE-MIB", "trapIpFilterRejectIp"))
)
if mibBuilder.loadTexts:
    swIpFilterRejectTrap.setStatus(
        "current"
    )

swAuthenticationFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 66)
)
swAuthenticationFailure.setObjects(
      *(("ES3552M-AND-PoE-MIB", "trapVarLoginUserName"),
        ("ES3552M-AND-PoE-MIB", "trapVarLoginMethod"),
        ("ES3552M-AND-PoE-MIB", "trapVarLoginIPAddress"),
        ("ES3552M-AND-PoE-MIB", "trapVarLoginTime"))
)
if mibBuilder.loadTexts:
    swAuthenticationFailure.setStatus(
        "current"
    )

swAuthenticationSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 67)
)
swAuthenticationSuccess.setObjects(
      *(("ES3552M-AND-PoE-MIB", "trapVarLoginUserName"),
        ("ES3552M-AND-PoE-MIB", "trapVarLoginMethod"),
        ("ES3552M-AND-PoE-MIB", "trapVarLoginIPAddress"),
        ("ES3552M-AND-PoE-MIB", "trapVarLoginTime"))
)
if mibBuilder.loadTexts:
    swAuthenticationSuccess.setStatus(
        "current"
    )

swAtcBcastStormAlarmFireTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 70)
)
swAtcBcastStormAlarmFireTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "atcBcastStormIfIndex"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormSampleType"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormCurrentTrafficRate"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormAlarmFireThreshold"))
)
if mibBuilder.loadTexts:
    swAtcBcastStormAlarmFireTrap.setStatus(
        "current"
    )

swAtcBcastStormAlarmClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 71)
)
swAtcBcastStormAlarmClearTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "atcBcastStormIfIndex"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormSampleType"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormCurrentTrafficRate"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormAlarmClearThreshold"))
)
if mibBuilder.loadTexts:
    swAtcBcastStormAlarmClearTrap.setStatus(
        "current"
    )

swAtcBcastStormTcApplyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 72)
)
swAtcBcastStormTcApplyTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "atcBcastStormIfIndex"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormSampleType"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormCurrentTrafficRate"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormAlarmFireThreshold"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormTcApplyTime"))
)
if mibBuilder.loadTexts:
    swAtcBcastStormTcApplyTrap.setStatus(
        "current"
    )

swAtcBcastStormTcReleaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 73)
)
swAtcBcastStormTcReleaseTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "atcBcastStormIfIndex"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormSampleType"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormCurrentTrafficRate"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormAlarmClearThreshold"),
        ("ES3552M-AND-PoE-MIB", "atcBcastStormTcReleaseTime"))
)
if mibBuilder.loadTexts:
    swAtcBcastStormTcReleaseTrap.setStatus(
        "current"
    )

swAtcMcastStormAlarmFireTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 74)
)
swAtcMcastStormAlarmFireTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "atcMcastStormIfIndex"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormSampleType"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormCurrentTrafficRate"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormAlarmFireThreshold"))
)
if mibBuilder.loadTexts:
    swAtcMcastStormAlarmFireTrap.setStatus(
        "current"
    )

swAtcMcastStormAlarmClearTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 75)
)
swAtcMcastStormAlarmClearTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "atcMcastStormIfIndex"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormSampleType"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormCurrentTrafficRate"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormAlarmClearThreshold"))
)
if mibBuilder.loadTexts:
    swAtcMcastStormAlarmClearTrap.setStatus(
        "current"
    )

swAtcMcastStormTcApplyTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 76)
)
swAtcMcastStormTcApplyTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "atcMcastStormIfIndex"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormSampleType"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormCurrentTrafficRate"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormAlarmFireThreshold"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormTcApplyTime"))
)
if mibBuilder.loadTexts:
    swAtcMcastStormTcApplyTrap.setStatus(
        "current"
    )

swAtcMcastStormTcReleaseTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 77)
)
swAtcMcastStormTcReleaseTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "atcMcastStormIfIndex"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormSampleType"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormCurrentTrafficRate"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormAlarmClearThreshold"),
        ("ES3552M-AND-PoE-MIB", "atcMcastStormTcReleaseTime"))
)
if mibBuilder.loadTexts:
    swAtcMcastStormTcReleaseTrap.setStatus(
        "current"
    )

swLoopbackDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 92)
)
swLoopbackDetectionTrap.setObjects(
    ("ES3552M-AND-PoE-MIB", "staLoopbackDetectionPortIfIndex")
)
if mibBuilder.loadTexts:
    swLoopbackDetectionTrap.setStatus(
        "current"
    )

networkAccessPortLinkDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 96)
)
networkAccessPortLinkDetectionTrap.setObjects(
      *(("IF-MIB", "ifIndex"),
        ("ES3552M-AND-PoE-MIB", "ifOperStatus"),
        ("ES3552M-AND-PoE-MIB", "networkAccessPortLinkDetectionMode"),
        ("ES3552M-AND-PoE-MIB", "networkAccessPortLinkDetectionAciton"))
)
if mibBuilder.loadTexts:
    networkAccessPortLinkDetectionTrap.setStatus(
        "current"
    )

dot1agCfmMepUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 97)
)
dot1agCfmMepUpTrap.setObjects(
    ("ES3552M-AND-PoE-MIB", "dot1agCfmMepDbRMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmMepUpTrap.setStatus(
        "current"
    )

dot1agCfmMepDownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 98)
)
dot1agCfmMepDownTrap.setObjects(
    ("ES3552M-AND-PoE-MIB", "dot1agCfmMepDbRMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmMepDownTrap.setStatus(
        "current"
    )

dot1agCfmConfigFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 99)
)
dot1agCfmConfigFailTrap.setObjects(
    ("ES3552M-AND-PoE-MIB", "dot1agCfmMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmConfigFailTrap.setStatus(
        "current"
    )

dot1agCfmLoopFindTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 100)
)
dot1agCfmLoopFindTrap.setObjects(
    ("ES3552M-AND-PoE-MIB", "dot1agCfmMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmLoopFindTrap.setStatus(
        "current"
    )

dot1agCfmMepUnknownTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 101)
)
dot1agCfmMepUnknownTrap.setObjects(
    ("ES3552M-AND-PoE-MIB", "dot1agCfmMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmMepUnknownTrap.setStatus(
        "current"
    )

dot1agCfmMepMissingTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 102)
)
dot1agCfmMepMissingTrap.setObjects(
    ("ES3552M-AND-PoE-MIB", "dot1agCfmMepDbRMepIdentifier")
)
if mibBuilder.loadTexts:
    dot1agCfmMepMissingTrap.setStatus(
        "current"
    )

dot1agCfmMaUpTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 103)
)
dot1agCfmMaUpTrap.setObjects(
    ("ES3552M-AND-PoE-MIB", "dot1agCfmMaIndex")
)
if mibBuilder.loadTexts:
    dot1agCfmMaUpTrap.setStatus(
        "current"
    )

autoUpgradeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 104)
)
autoUpgradeTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "fileCopyFileType"),
        ("ES3552M-AND-PoE-MIB", "trapAutoUpgradeResult"),
        ("ES3552M-AND-PoE-MIB", "trapAutoUpgradeNewVer"))
)
if mibBuilder.loadTexts:
    autoUpgradeTrap.setStatus(
        "current"
    )

swCpuUtiRisingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 107)
)
if mibBuilder.loadTexts:
    swCpuUtiRisingNotification.setStatus(
        "current"
    )

swCpuUtiFallingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 108)
)
if mibBuilder.loadTexts:
    swCpuUtiFallingNotification.setStatus(
        "current"
    )

swMemoryUtiRisingThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 109)
)
if mibBuilder.loadTexts:
    swMemoryUtiRisingThresholdNotification.setStatus(
        "current"
    )

swMemoryUtiFallingThresholdNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 110)
)
if mibBuilder.loadTexts:
    swMemoryUtiFallingThresholdNotification.setStatus(
        "current"
    )

dhcpRougeServerAttackTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 114)
)
dhcpRougeServerAttackTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "trapDhcpClientPortIfIndex"),
        ("ES3552M-AND-PoE-MIB", "trapDhcpServerIpAddress"))
)
if mibBuilder.loadTexts:
    dhcpRougeServerAttackTrap.setStatus(
        "current"
    )

lbdDetectionTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 141)
)
lbdDetectionTrap.setObjects(
      *(("ES3552M-AND-PoE-MIB", "trapIfIndex"),
        ("ES3552M-AND-PoE-MIB", "trapVlanId"))
)
if mibBuilder.loadTexts:
    lbdDetectionTrap.setStatus(
        "current"
    )

lbdRecoveryTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 259, 8, 1, 12, 2, 1, 0, 142)
)
lbdRecoveryTrap.setObjects(
    ("ES3552M-AND-PoE-MIB", "trapIfIndex")
)
if mibBuilder.loadTexts:
    lbdRecoveryTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ES3552M-AND-PoE-MIB",
    **{"KeySegment": KeySegment,
       "ValidStatus": ValidStatus,
       "StaPathCostMode": StaPathCostMode,
       "FileCopyStatus": FileCopyStatus,
       "accton": accton,
       "snmpMgt": snmpMgt,
       "cheetahSwitchMgt": cheetahSwitchMgt,
       "edgecore": edgecore,
       "edgeCoreSwitchMgt": edgeCoreSwitchMgt,
       "es3552m-and-poeMIB": es3552m_and_poeMIB,
       "es3552m-and-poeMIBObjects": es3552m_and_poeMIBObjects,
       "switchMgt": switchMgt,
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
       "amtrMacAddrDynamicCount": amtrMacAddrDynamicCount,
       "amtrMacAddrStaticCount": amtrMacAddrStaticCount,
       "amtrMacAddrTotalCount": amtrMacAddrTotalCount,
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
       "portMasterSlaveModeCfg": portMasterSlaveModeCfg,
       "cableDiagMgt": cableDiagMgt,
       "cableDiagCtlAction": cableDiagCtlAction,
       "cableDiagResultTable": cableDiagResultTable,
       "cableDiagResultEntry": cableDiagResultEntry,
       "cableDiagResultIfIndex": cableDiagResultIfIndex,
       "cableDiagResultStatusPairA": cableDiagResultStatusPairA,
       "cableDiagResultStatusPairB": cableDiagResultStatusPairB,
       "cableDiagResultDistancePairA": cableDiagResultDistancePairA,
       "cableDiagResultDistancePairB": cableDiagResultDistancePairB,
       "cableDiagResultTime": cableDiagResultTime,
       "portUtilTable": portUtilTable,
       "portUtilEntry": portUtilEntry,
       "portUtilIfIndex": portUtilIfIndex,
       "portInOctetRate": portInOctetRate,
       "portInPacketRate": portInPacketRate,
       "portInUtil": portInUtil,
       "portOutOctetRate": portOutOctetRate,
       "portOutPacketRate": portOutPacketRate,
       "portOutUtil": portOutUtil,
       "portVlanTrunkingTable": portVlanTrunkingTable,
       "portVlanTrunkingEntry": portVlanTrunkingEntry,
       "portVlanTrunkingIfIndex": portVlanTrunkingIfIndex,
       "portVlanTrunkingStatus": portVlanTrunkingStatus,
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
       "staPortOperEdgePort": staPortOperEdgePort,
       "staPortAdminPointToPoint": staPortAdminPointToPoint,
       "staPortOperPointToPoint": staPortOperPointToPoint,
       "staPortSystemStatus": staPortSystemStatus,
       "staPortLongAdminPathCost": staPortLongAdminPathCost,
       "staPortLongOperPathCost": staPortLongOperPathCost,
       "staPortRootGuardAdminStatus": staPortRootGuardAdminStatus,
       "staPortRootGuardOperStatus": staPortRootGuardOperStatus,
       "staPortBpduGuard": staPortBpduGuard,
       "staPortAdminEdgePortWithAuto": staPortAdminEdgePortWithAuto,
       "staPortBpduFilter": staPortBpduFilter,
       "staPortBpduGuardAutoRecovery": staPortBpduGuardAutoRecovery,
       "staPortBpduGuardAutoRecoveryInterval": staPortBpduGuardAutoRecoveryInterval,
       "staProtocolType": staProtocolType,
       "staTxHoldCount": staTxHoldCount,
       "staPathCostMethod": staPathCostMethod,
       "xstMgt": xstMgt,
       "mstName": mstName,
       "mstRevision": mstRevision,
       "mstMaxHops": mstMaxHops,
       "xstInstanceCfgTable": xstInstanceCfgTable,
       "xstInstanceCfgEntry": xstInstanceCfgEntry,
       "xstInstanceCfgIndex": xstInstanceCfgIndex,
       "xstInstanceCfgPriority": xstInstanceCfgPriority,
       "xstInstanceCfgTimeSinceTopologyChange": xstInstanceCfgTimeSinceTopologyChange,
       "xstInstanceCfgTopChanges": xstInstanceCfgTopChanges,
       "xstInstanceCfgDesignatedRoot": xstInstanceCfgDesignatedRoot,
       "xstInstanceCfgRootCost": xstInstanceCfgRootCost,
       "xstInstanceCfgRootPort": xstInstanceCfgRootPort,
       "xstInstanceCfgMaxAge": xstInstanceCfgMaxAge,
       "xstInstanceCfgHelloTime": xstInstanceCfgHelloTime,
       "xstInstanceCfgHoldTime": xstInstanceCfgHoldTime,
       "xstInstanceCfgForwardDelay": xstInstanceCfgForwardDelay,
       "xstInstanceCfgBridgeMaxAge": xstInstanceCfgBridgeMaxAge,
       "xstInstanceCfgBridgeHelloTime": xstInstanceCfgBridgeHelloTime,
       "xstInstanceCfgBridgeForwardDelay": xstInstanceCfgBridgeForwardDelay,
       "xstInstanceCfgTxHoldCount": xstInstanceCfgTxHoldCount,
       "xstInstanceCfgPathCostMethod": xstInstanceCfgPathCostMethod,
       "xstInstancePortTable": xstInstancePortTable,
       "xstInstancePortEntry": xstInstancePortEntry,
       "xstInstancePortInstance": xstInstancePortInstance,
       "xstInstancePortPort": xstInstancePortPort,
       "xstInstancePortPriority": xstInstancePortPriority,
       "xstInstancePortState": xstInstancePortState,
       "xstInstancePortEnable": xstInstancePortEnable,
       "xstInstancePortPathCost": xstInstancePortPathCost,
       "xstInstancePortDesignatedRoot": xstInstancePortDesignatedRoot,
       "xstInstancePortDesignatedCost": xstInstancePortDesignatedCost,
       "xstInstancePortDesignatedBridge": xstInstancePortDesignatedBridge,
       "xstInstancePortDesignatedPort": xstInstancePortDesignatedPort,
       "xstInstancePortForwardTransitions": xstInstancePortForwardTransitions,
       "xstInstancePortPortRole": xstInstancePortPortRole,
       "xstInstancePortAdminPathCost": xstInstancePortAdminPathCost,
       "xstInstancePortOperPathCost": xstInstancePortOperPathCost,
       "mstInstanceEditTable": mstInstanceEditTable,
       "mstInstanceEditEntry": mstInstanceEditEntry,
       "mstInstanceEditIndex": mstInstanceEditIndex,
       "mstInstanceEditVlansMap": mstInstanceEditVlansMap,
       "mstInstanceEditVlansMap2k": mstInstanceEditVlansMap2k,
       "mstInstanceEditVlansMap3k": mstInstanceEditVlansMap3k,
       "mstInstanceEditVlansMap4k": mstInstanceEditVlansMap4k,
       "mstInstanceEditRemainingHops": mstInstanceEditRemainingHops,
       "mstInstanceOperTable": mstInstanceOperTable,
       "mstInstanceOperEntry": mstInstanceOperEntry,
       "mstInstanceOperIndex": mstInstanceOperIndex,
       "mstInstanceOperVlansMap": mstInstanceOperVlansMap,
       "mstInstanceOperVlansMap2k": mstInstanceOperVlansMap2k,
       "mstInstanceOperVlansMap3k": mstInstanceOperVlansMap3k,
       "mstInstanceOperVlansMap4k": mstInstanceOperVlansMap4k,
       "staLoopbackDetectionPortTable": staLoopbackDetectionPortTable,
       "staLoopbackDetectionPortEntry": staLoopbackDetectionPortEntry,
       "staLoopbackDetectionPortIfIndex": staLoopbackDetectionPortIfIndex,
       "staLoopbackDetectionPortStatus": staLoopbackDetectionPortStatus,
       "staLoopbackDetectionPortTrapStatus": staLoopbackDetectionPortTrapStatus,
       "staLoopbackDetectionPortReleaseMode": staLoopbackDetectionPortReleaseMode,
       "staLoopbackDetectionPortRelease": staLoopbackDetectionPortRelease,
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
       "vlanMirrorTable": vlanMirrorTable,
       "vlanMirrorEntry": vlanMirrorEntry,
       "vlanMirrorDestinationPort": vlanMirrorDestinationPort,
       "vlanMirrorSourceVlan": vlanMirrorSourceVlan,
       "vlanMirrorStatus": vlanMirrorStatus,
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
       "dhcpOption82": dhcpOption82,
       "dhcpOption82Status": dhcpOption82Status,
       "dhcpOption82Policy": dhcpOption82Policy,
       "arpCacheDeleteAll": arpCacheDeleteAll,
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
       "voiceVlanMgt": voiceVlanMgt,
       "voiceVlanOuiTable": voiceVlanOuiTable,
       "voiceVlanOuiEntry": voiceVlanOuiEntry,
       "voiceVlanOuiAddress": voiceVlanOuiAddress,
       "voiceVlanOuiMask": voiceVlanOuiMask,
       "voiceVlanOuiDescription": voiceVlanOuiDescription,
       "voiceVlanOuiStatus": voiceVlanOuiStatus,
       "voiceVlanEnabledId": voiceVlanEnabledId,
       "voiceVlanAgingTime": voiceVlanAgingTime,
       "voiceVlanPortTable": voiceVlanPortTable,
       "voiceVlanPortEntry": voiceVlanPortEntry,
       "voiceVlanPortIfIndex": voiceVlanPortIfIndex,
       "voiceVlanPortMode": voiceVlanPortMode,
       "voiceVlanPortSecurity": voiceVlanPortSecurity,
       "voiceVlanPortPriority": voiceVlanPortPriority,
       "voiceVlanPortRuleOui": voiceVlanPortRuleOui,
       "voiceVlanPortRuleLldp": voiceVlanPortRuleLldp,
       "vlanDot1qTunnelGlobalConfig": vlanDot1qTunnelGlobalConfig,
       "vlanDot1qTunnelStatus": vlanDot1qTunnelStatus,
       "vlanDot1qTunnelPortTable": vlanDot1qTunnelPortTable,
       "vlanDot1qTunnelPortEntry": vlanDot1qTunnelPortEntry,
       "vlanDot1qTunnelPortIndex": vlanDot1qTunnelPortIndex,
       "vlanDot1qTunnelPortMode": vlanDot1qTunnelPortMode,
       "vlanDot1qTunnelPortEtherType": vlanDot1qTunnelPortEtherType,
       "macVlanTable": macVlanTable,
       "macVlanEntry": macVlanEntry,
       "macVlanMacAddress": macVlanMacAddress,
       "macVlanId": macVlanId,
       "macVlanStatus": macVlanStatus,
       "macVlanClearAction": macVlanClearAction,
       "subnetVlanTable": subnetVlanTable,
       "subnetVlanEntry": subnetVlanEntry,
       "subnetVlanIpAddress": subnetVlanIpAddress,
       "subnetVlanMask": subnetVlanMask,
       "subnetVlanId": subnetVlanId,
       "subnetVlanPriority": subnetVlanPriority,
       "subnetVlanStatus": subnetVlanStatus,
       "subnetVlanClearAction": subnetVlanClearAction,
       "vlanL2ProtocolTunnelPortTable": vlanL2ProtocolTunnelPortTable,
       "vlanL2ProtocolTunnelPortEntry": vlanL2ProtocolTunnelPortEntry,
       "vlanL2ptPortIndex": vlanL2ptPortIndex,
       "vlanL2ptPortSta": vlanL2ptPortSta,
       "vlanL2ptPortLldp": vlanL2ptPortLldp,
       "vlanL2ptPortCdp": vlanL2ptPortCdp,
       "vlanL2ptPortVtp": vlanL2ptPortVtp,
       "vlanL2ptPortPvst": vlanL2ptPortPvst,
       "vlanL2ProtocolTunnelGlobalConfig": vlanL2ProtocolTunnelGlobalConfig,
       "vlanL2ProtocolTunnelAddress": vlanL2ProtocolTunnelAddress,
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
       "trapVar": trapVar,
       "trapIpFilterRejectMode": trapIpFilterRejectMode,
       "trapIpFilterRejectIp": trapIpFilterRejectIp,
       "trapAutoUpgradeResult": trapAutoUpgradeResult,
       "trapAutoUpgradeNewVer": trapAutoUpgradeNewVer,
       "trapDhcpClientPortIfIndex": trapDhcpClientPortIfIndex,
       "trapDhcpServerIpAddress": trapDhcpServerIpAddress,
       "trapPortSecurityIntrusionMac": trapPortSecurityIntrusionMac,
       "trapIfIndex": trapIfIndex,
       "trapVlanId": trapVlanId,
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
       "diffServPortIngressIpv6AclIndex": diffServPortIngressIpv6AclIndex,
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
       "diffServMacAceCosOp": diffServMacAceCosOp,
       "diffServMacAceCosBitmask": diffServMacAceCosBitmask,
       "diffServMacAceMinCos": diffServMacAceMinCos,
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
       "diffServIpv6AceTable": diffServIpv6AceTable,
       "diffServIpv6AceEntry": diffServIpv6AceEntry,
       "diffServIpv6AceIndex": diffServIpv6AceIndex,
       "diffServIpv6AceType": diffServIpv6AceType,
       "diffServIpv6AceAccess": diffServIpv6AceAccess,
       "diffServIpv6AceSourceIpAddr": diffServIpv6AceSourceIpAddr,
       "diffServIpv6AceSourceIpAddrPrefixLen": diffServIpv6AceSourceIpAddrPrefixLen,
       "diffServIpv6AceDestIpAddr": diffServIpv6AceDestIpAddr,
       "diffServIpv6AceDestIpAddrPrefixLen": diffServIpv6AceDestIpAddrPrefixLen,
       "diffServIpv6AceDscp": diffServIpv6AceDscp,
       "diffServIpv6AceStatus": diffServIpv6AceStatus,
       "diffServArpAceTable": diffServArpAceTable,
       "diffServArpAceEntry": diffServArpAceEntry,
       "diffServArpAceIndex": diffServArpAceIndex,
       "diffServArpAceAction": diffServArpAceAction,
       "diffServArpAcePktType": diffServArpAcePktType,
       "diffServArpAceSourceIpAddr": diffServArpAceSourceIpAddr,
       "diffServArpAceSourceIpAddrBitmask": diffServArpAceSourceIpAddrBitmask,
       "diffServArpAceDestIpAddr": diffServArpAceDestIpAddr,
       "diffServArpAceDestIpAddrBitmask": diffServArpAceDestIpAddrBitmask,
       "diffServArpAceSourceMacAddr": diffServArpAceSourceMacAddr,
       "diffServArpAceSourceMacAddrBitmask": diffServArpAceSourceMacAddrBitmask,
       "diffServArpAceDestMacAddr": diffServArpAceDestMacAddr,
       "diffServArpAceDestMacAddrBitmask": diffServArpAceDestMacAddrBitmask,
       "diffServArpAceLogStatus": diffServArpAceLogStatus,
       "diffServArpAceStatus": diffServArpAceStatus,
       "diffServArpTable": diffServArpTable,
       "diffServArpEntry": diffServArpEntry,
       "diffServArpAclName": diffServArpAclName,
       "diffServTcamMgt": diffServTcamMgt,
       "diffServTcamTotalPolicyControlEntries": diffServTcamTotalPolicyControlEntries,
       "diffServTcamFreePolicyControlEntries": diffServTcamFreePolicyControlEntries,
       "diffServTcamUtilization": diffServTcamUtilization,
       "securityMgt": securityMgt,
       "privateVlanMgt": privateVlanMgt,
       "privateVlanStatus": privateVlanStatus,
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
       "privateVlanSessionTable": privateVlanSessionTable,
       "privateVlanSessionEntry": privateVlanSessionEntry,
       "privateVlanSessionId": privateVlanSessionId,
       "privateVlanSessionUplinkPorts": privateVlanSessionUplinkPorts,
       "privateVlanSessionDownlinkPorts": privateVlanSessionDownlinkPorts,
       "privateVlanSessionStatus": privateVlanSessionStatus,
       "privateVlanUplinkToUplink": privateVlanUplinkToUplink,
       "portSecurityMgt": portSecurityMgt,
       "portSecPortTable": portSecPortTable,
       "portSecPortEntry": portSecPortEntry,
       "portSecPortIndex": portSecPortIndex,
       "portSecPortStatus": portSecPortStatus,
       "portSecAction": portSecAction,
       "portSecMaxMacCount": portSecMaxMacCount,
       "radiusMgt": radiusMgt,
       "radiusServerGlobalAuthPort": radiusServerGlobalAuthPort,
       "radiusServerGlobalAcctPort": radiusServerGlobalAcctPort,
       "radiusServerGlobalKey": radiusServerGlobalKey,
       "radiusServerGlobalRetransmit": radiusServerGlobalRetransmit,
       "radiusServerGlobalTimeout": radiusServerGlobalTimeout,
       "radiusServerTable": radiusServerTable,
       "radiusServerEntry": radiusServerEntry,
       "radiusServerIndex": radiusServerIndex,
       "radiusServerAddress": radiusServerAddress,
       "radiusServerAuthPortNumber": radiusServerAuthPortNumber,
       "radiusServerAcctPortNumber": radiusServerAcctPortNumber,
       "radiusServerKey": radiusServerKey,
       "radiusServerRetransmit": radiusServerRetransmit,
       "radiusServerTimeout": radiusServerTimeout,
       "radiusServerStatus": radiusServerStatus,
       "tacacsMgt": tacacsMgt,
       "tacacsPlusServerGlobalPortNumber": tacacsPlusServerGlobalPortNumber,
       "tacacsPlusServerGlobalKey": tacacsPlusServerGlobalKey,
       "tacacsPlusServerTable": tacacsPlusServerTable,
       "tacacsPlusServerEntry": tacacsPlusServerEntry,
       "tacacsPlusServerIndex": tacacsPlusServerIndex,
       "tacacsPlusServerAddress": tacacsPlusServerAddress,
       "tacacsPlusServerPortNumber": tacacsPlusServerPortNumber,
       "tacacsPlusServerKey": tacacsPlusServerKey,
       "tacacsPlusServerStatus": tacacsPlusServerStatus,
       "tacacsPlusServerRetransmit": tacacsPlusServerRetransmit,
       "tacacsPlusServerTimeout": tacacsPlusServerTimeout,
       "tacacsPlusServerGlobalRetransmit": tacacsPlusServerGlobalRetransmit,
       "tacacsPlusServerGlobalTimeout": tacacsPlusServerGlobalTimeout,
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
       "dot1xMgt": dot1xMgt,
       "dot1xAuthConfigExtTable": dot1xAuthConfigExtTable,
       "dot1xAuthConfigExtEntry": dot1xAuthConfigExtEntry,
       "dot1xAuthConfigExtOperMode": dot1xAuthConfigExtOperMode,
       "dot1xAuthConfigExtMultiHostMaxCnt": dot1xAuthConfigExtMultiHostMaxCnt,
       "dot1xAuthConfigExtPortIntrusionAction": dot1xAuthConfigExtPortIntrusionAction,
       "dot1xSuppMgt": dot1xSuppMgt,
       "dot1xSuppUserName": dot1xSuppUserName,
       "dot1xSuppPassword": dot1xSuppPassword,
       "dot1xSuppConfigPortTable": dot1xSuppConfigPortTable,
       "dot1xSuppConfigPortEntry": dot1xSuppConfigPortEntry,
       "dot1xSuppConfigPortIndex": dot1xSuppConfigPortIndex,
       "dot1xSuppConfigPortStatus": dot1xSuppConfigPortStatus,
       "dot1xEapolPassThrough": dot1xEapolPassThrough,
       "aaaMgt": aaaMgt,
       "aaaMethodTable": aaaMethodTable,
       "aaaMethodEntry": aaaMethodEntry,
       "aaaMethodIndex": aaaMethodIndex,
       "aaaMethodName": aaaMethodName,
       "aaaMethodGroupName": aaaMethodGroupName,
       "aaaMethodMode": aaaMethodMode,
       "aaaMethodStatus": aaaMethodStatus,
       "aaaMethodClientType": aaaMethodClientType,
       "aaaMethodPrivilegeLevel": aaaMethodPrivilegeLevel,
       "aaaRadiusGroupTable": aaaRadiusGroupTable,
       "aaaRadiusGroupEntry": aaaRadiusGroupEntry,
       "aaaRadiusGroupIndex": aaaRadiusGroupIndex,
       "aaaRadiusGroupServerBitMap": aaaRadiusGroupServerBitMap,
       "aaaRadiusGroupName": aaaRadiusGroupName,
       "aaaRadiusGroupStatus": aaaRadiusGroupStatus,
       "aaaTacacsPlusGroupTable": aaaTacacsPlusGroupTable,
       "aaaTacacsPlusGroupEntry": aaaTacacsPlusGroupEntry,
       "aaaTacacsPlusGroupIndex": aaaTacacsPlusGroupIndex,
       "aaaTacacsPlusGroupServerBitMap": aaaTacacsPlusGroupServerBitMap,
       "aaaTacacsPlusGroupName": aaaTacacsPlusGroupName,
       "aaaTacacsPlusGroupStatus": aaaTacacsPlusGroupStatus,
       "aaaUpdate": aaaUpdate,
       "aaaAccountTable": aaaAccountTable,
       "aaaAccountEntry": aaaAccountEntry,
       "aaaAccountIfIndex": aaaAccountIfIndex,
       "aaaAccountMethodName": aaaAccountMethodName,
       "aaaAccountProtocol": aaaAccountProtocol,
       "aaaAccountStatus": aaaAccountStatus,
       "aaaCommandPrivilegesTable": aaaCommandPrivilegesTable,
       "aaaCommandPrivilegesEntry": aaaCommandPrivilegesEntry,
       "aaaCommandPrivilegesLevel": aaaCommandPrivilegesLevel,
       "aaaCommandPrivilegesInterfaceIndex": aaaCommandPrivilegesInterfaceIndex,
       "aaaCommandPrivilegesMethodName": aaaCommandPrivilegesMethodName,
       "aaaAccExecTable": aaaAccExecTable,
       "aaaAccExecEntry": aaaAccExecEntry,
       "aaaAccExecIndex": aaaAccExecIndex,
       "aaaAccExecMethodName": aaaAccExecMethodName,
       "networkAccessMgt": networkAccessMgt,
       "networkAccessPortTable": networkAccessPortTable,
       "networkAccessPortEntry": networkAccessPortEntry,
       "networkAccessPortPortIndex": networkAccessPortPortIndex,
       "networkAccessPortMaxMacCount": networkAccessPortMaxMacCount,
       "networkAccessPortMode": networkAccessPortMode,
       "networkAccessPortMacFilter": networkAccessPortMacFilter,
       "networkAccessPortGuestVlan": networkAccessPortGuestVlan,
       "networkAccessPortLinkDetectionStatus": networkAccessPortLinkDetectionStatus,
       "networkAccessPortLinkDetectionMode": networkAccessPortLinkDetectionMode,
       "networkAccessPortLinkDetectionAciton": networkAccessPortLinkDetectionAciton,
       "networkAccessPortDynamicQos": networkAccessPortDynamicQos,
       "networkAccessClearMacAddressMgt": networkAccessClearMacAddressMgt,
       "networkAccessClearMacAddressAttribute": networkAccessClearMacAddressAttribute,
       "networkAccessClearMacAddressMacAddress": networkAccessClearMacAddressMacAddress,
       "networkAccessClearMacAddressPort": networkAccessClearMacAddressPort,
       "networkAccessClearMacAddressAction": networkAccessClearMacAddressAction,
       "networkAccessMacAddressTable": networkAccessMacAddressTable,
       "networkAccessMacAddressEntry": networkAccessMacAddressEntry,
       "networkAccessMacAddressAddress": networkAccessMacAddressAddress,
       "networkAccessMacAddressPort": networkAccessMacAddressPort,
       "networkAccessMacAddressInetAddressType": networkAccessMacAddressInetAddressType,
       "networkAccessMacAddressRadiusServerInetAddress": networkAccessMacAddressRadiusServerInetAddress,
       "networkAccessMacAddressTime": networkAccessMacAddressTime,
       "networkAccessMacAddressAttribute": networkAccessMacAddressAttribute,
       "networkAccessAging": networkAccessAging,
       "networkAccessMacFilterWithMaskTable": networkAccessMacFilterWithMaskTable,
       "networkAccessMacFilterWithMaskEntry": networkAccessMacFilterWithMaskEntry,
       "networkAccessMacFilterWithMaskID": networkAccessMacFilterWithMaskID,
       "networkAccessMacFilterWithMaskMacAddress": networkAccessMacFilterWithMaskMacAddress,
       "networkAccessMacFilterWithMaskMacAddressMask": networkAccessMacFilterWithMaskMacAddressMask,
       "networkAccessMacFilterWithMaskStatus": networkAccessMacFilterWithMaskStatus,
       "macAuthMgt": macAuthMgt,
       "macAuthReauthTime": macAuthReauthTime,
       "macAuthPortTable": macAuthPortTable,
       "macAuthPortEntry": macAuthPortEntry,
       "macAuthPortIndex": macAuthPortIndex,
       "macAuthPortMaxMacCount": macAuthPortMaxMacCount,
       "macAuthPortIntrusionAction": macAuthPortIntrusionAction,
       "webAuthMgt": webAuthMgt,
       "webAuthSystemAuthControl": webAuthSystemAuthControl,
       "webAuthSessionTimeout": webAuthSessionTimeout,
       "webAuthQuietPeriod": webAuthQuietPeriod,
       "webAuthLoginAttempts": webAuthLoginAttempts,
       "webAuthReauthenticateMgt": webAuthReauthenticateMgt,
       "webAuthReauthenticatePort": webAuthReauthenticatePort,
       "webAuthReauthenticateInetAddressType": webAuthReauthenticateInetAddressType,
       "webAuthReauthenticateInetAddress": webAuthReauthenticateInetAddress,
       "webAuthReauthenticateAction": webAuthReauthenticateAction,
       "webAuthPortConfigTable": webAuthPortConfigTable,
       "webAuthPortConfigEntry": webAuthPortConfigEntry,
       "webAuthPortConfigPortIndex": webAuthPortConfigPortIndex,
       "webAuthPortConfigStatus": webAuthPortConfigStatus,
       "webAuthPortConfigAuthenticatedHostCount": webAuthPortConfigAuthenticatedHostCount,
       "webAuthPortInfoTable": webAuthPortInfoTable,
       "webAuthPortInfoEntry": webAuthPortInfoEntry,
       "webAuthPortInfoPortIndex": webAuthPortInfoPortIndex,
       "webAuthPortInfoPortAuthSuccessIndex": webAuthPortInfoPortAuthSuccessIndex,
       "webAuthPortInfoInetAddressType": webAuthPortInfoInetAddressType,
       "webAuthPortInfoInetAddress": webAuthPortInfoInetAddress,
       "webAuthPortInfoRemainingSessiontime": webAuthPortInfoRemainingSessiontime,
       "webAuthPortInfoStatus": webAuthPortInfoStatus,
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
       "ntpMgt": ntpMgt,
       "ntpStatus": ntpStatus,
       "ntpServiceMode": ntpServiceMode,
       "ntpPollInterval": ntpPollInterval,
       "ntpAuthenticateStatus": ntpAuthenticateStatus,
       "ntpServerTable": ntpServerTable,
       "ntpServerEntry": ntpServerEntry,
       "ntpServerIpAddress": ntpServerIpAddress,
       "ntpServerVersion": ntpServerVersion,
       "ntpServerKeyId": ntpServerKeyId,
       "ntpServerStatus": ntpServerStatus,
       "ntpAuthKeyTable": ntpAuthKeyTable,
       "ntpAuthKeyEntry": ntpAuthKeyEntry,
       "ntpAuthKeyId": ntpAuthKeyId,
       "ntpAuthKeyWord": ntpAuthKeyWord,
       "ntpAuthKeyStatus": ntpAuthKeyStatus,
       "sysTimeZonePredefined": sysTimeZonePredefined,
       "sysSummerTimeMgt": sysSummerTimeMgt,
       "sysSummerTimeZoneName": sysSummerTimeZoneName,
       "sysSummerTimeMode": sysSummerTimeMode,
       "sysSummerTimeRecurringTime": sysSummerTimeRecurringTime,
       "sysSummerTimeDateTime": sysSummerTimeDateTime,
       "sysSummerTimePredefinedRegion": sysSummerTimePredefinedRegion,
       "sysSummerTimeOffset": sysSummerTimeOffset,
       "sysSummerTimeEffect": sysSummerTimeEffect,
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
       "fileCopyFtpLoginUsername": fileCopyFtpLoginUsername,
       "fileCopyFtpLoginPassword": fileCopyFtpLoginPassword,
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
       "fileAutoUpgradeMgt": fileAutoUpgradeMgt,
       "fileAutoUpgradeOpCodeStatus": fileAutoUpgradeOpCodeStatus,
       "fileAutoUpgradeOpCodePath": fileAutoUpgradeOpCodePath,
       "fileAutoUpgradeOpCodeFileName": fileAutoUpgradeOpCodeFileName,
       "fileAutoUpgradeOpCodeForceModeStatus": fileAutoUpgradeOpCodeForceModeStatus,
       "dnsMgt": dnsMgt,
       "dnsDomainLookup": dnsDomainLookup,
       "dnsDomainName": dnsDomainName,
       "dnsHostTable": dnsHostTable,
       "dnsHostEntry": dnsHostEntry,
       "dnsHostName": dnsHostName,
       "dnsHostIndex": dnsHostIndex,
       "dnsHostIp": dnsHostIp,
       "dnsDomainListTable": dnsDomainListTable,
       "dnsDomainListEntry": dnsDomainListEntry,
       "dnsDomainListName": dnsDomainListName,
       "dnsDomainListStatus": dnsDomainListStatus,
       "dnsNameServerTable": dnsNameServerTable,
       "dnsNameServerEntry": dnsNameServerEntry,
       "dnsNameServerIndex": dnsNameServerIndex,
       "dnsNameServerIp": dnsNameServerIp,
       "dnsCacheTable": dnsCacheTable,
       "dnsCacheEntry": dnsCacheEntry,
       "dnsCacheIndex": dnsCacheIndex,
       "dnsCacheFlag": dnsCacheFlag,
       "dnsCacheType": dnsCacheType,
       "dnsCacheIp": dnsCacheIp,
       "dnsCacheTtl": dnsCacheTtl,
       "dnsCacheDomain": dnsCacheDomain,
       "stormMgt": stormMgt,
       "mcastStormMgt": mcastStormMgt,
       "mcastStormTable": mcastStormTable,
       "mcastStormEntry": mcastStormEntry,
       "mcastStormIfIndex": mcastStormIfIndex,
       "mcastStormStatus": mcastStormStatus,
       "mcastStormOctetRate": mcastStormOctetRate,
       "bcastStormMgt": bcastStormMgt,
       "bcastStormTable": bcastStormTable,
       "bcastStormEntry": bcastStormEntry,
       "bcastStormIfIndex": bcastStormIfIndex,
       "bcastStormStatus": bcastStormStatus,
       "bcastStormOctetRate": bcastStormOctetRate,
       "unknownUcastStormMgt": unknownUcastStormMgt,
       "unknownUcastStormTable": unknownUcastStormTable,
       "unknownUcastStormEntry": unknownUcastStormEntry,
       "unknownUcastStormIfIndex": unknownUcastStormIfIndex,
       "unknownUcastStormStatus": unknownUcastStormStatus,
       "unknownUcastStormOctetRate": unknownUcastStormOctetRate,
       "atcMgt": atcMgt,
       "atcBcastStormTcApplyTime": atcBcastStormTcApplyTime,
       "atcBcastStormTcReleaseTime": atcBcastStormTcReleaseTime,
       "atcBcastStormTable": atcBcastStormTable,
       "atcBcastStormEntry": atcBcastStormEntry,
       "atcBcastStormIfIndex": atcBcastStormIfIndex,
       "atcBcastStormEnable": atcBcastStormEnable,
       "atcBcastStormAutoRelease": atcBcastStormAutoRelease,
       "atcBcastStormSampleType": atcBcastStormSampleType,
       "atcBcastStormCurrentTrafficRate": atcBcastStormCurrentTrafficRate,
       "atcBcastStormAlarmFireThreshold": atcBcastStormAlarmFireThreshold,
       "atcBcastStormAlarmClearThreshold": atcBcastStormAlarmClearThreshold,
       "atcBcastStormTcAction": atcBcastStormTcAction,
       "atcBcastStormAlarmFireTrapStatus": atcBcastStormAlarmFireTrapStatus,
       "atcBcastStormAlarmClearTrapStatus": atcBcastStormAlarmClearTrapStatus,
       "atcBcastStormTcApplyTrapStatus": atcBcastStormTcApplyTrapStatus,
       "atcBcastStormTcReleaseTrapStatus": atcBcastStormTcReleaseTrapStatus,
       "atcMcastStormTcApplyTime": atcMcastStormTcApplyTime,
       "atcMcastStormTcReleaseTime": atcMcastStormTcReleaseTime,
       "atcMcastStormTable": atcMcastStormTable,
       "atcMcastStormEntry": atcMcastStormEntry,
       "atcMcastStormIfIndex": atcMcastStormIfIndex,
       "atcMcastStormEnable": atcMcastStormEnable,
       "atcMcastStormAutoRelease": atcMcastStormAutoRelease,
       "atcMcastStormSampleType": atcMcastStormSampleType,
       "atcMcastStormCurrentTrafficRate": atcMcastStormCurrentTrafficRate,
       "atcMcastStormAlarmFireThreshold": atcMcastStormAlarmFireThreshold,
       "atcMcastStormAlarmClearThreshold": atcMcastStormAlarmClearThreshold,
       "atcMcastStormTcAction": atcMcastStormTcAction,
       "atcMcastStormAlarmFireTrapStatus": atcMcastStormAlarmFireTrapStatus,
       "atcMcastStormAlarmClearTrapStatus": atcMcastStormAlarmClearTrapStatus,
       "atcMcastStormTcApplyTrapStatus": atcMcastStormTcApplyTrapStatus,
       "atcMcastStormTcReleaseTrapStatus": atcMcastStormTcReleaseTrapStatus,
       "sysResourceMgt": sysResourceMgt,
       "cpuStatus": cpuStatus,
       "cpuCurrentUti": cpuCurrentUti,
       "cpuStatMaxUti": cpuStatMaxUti,
       "cpuStatAvgUti": cpuStatAvgUti,
       "cpuPeakTime": cpuPeakTime,
       "cpuPeakDuration": cpuPeakDuration,
       "cpuUtiRisingThreshold": cpuUtiRisingThreshold,
       "cpuUtiFallingThreshold": cpuUtiFallingThreshold,
       "memoryStatus": memoryStatus,
       "memoryTotal": memoryTotal,
       "memoryAllocated": memoryAllocated,
       "memoryFreed": memoryFreed,
       "memoryFreedInPercent": memoryFreedInPercent,
       "memoryUtiRisingThreshold": memoryUtiRisingThreshold,
       "memoryUtiFallingThreshold": memoryUtiFallingThreshold,
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
       "mvrGroupCurrentReceiverVlan": mvrGroupCurrentReceiverVlan,
       "mvrPortTable": mvrPortTable,
       "mvrPortEntry": mvrPortEntry,
       "mvrIfIndex": mvrIfIndex,
       "mvrPortType": mvrPortType,
       "mvrPortImmediateLeave": mvrPortImmediateLeave,
       "mvrPortActive": mvrPortActive,
       "mvrRunningStatus": mvrRunningStatus,
       "mvrReceiverVlanId": mvrReceiverVlanId,
       "mvrMaxReceiverGroups": mvrMaxReceiverGroups,
       "mvrCurrentReceiverGroups": mvrCurrentReceiverGroups,
       "mvrReceiverGroupTable": mvrReceiverGroupTable,
       "mvrReceiverGroupEntry": mvrReceiverGroupEntry,
       "mvrReceiverGroupId": mvrReceiverGroupId,
       "mvrReceiverGroupActive": mvrReceiverGroupActive,
       "mvrReceiverGroupStatus": mvrReceiverGroupStatus,
       "mvrReceiverGroupStaticTable": mvrReceiverGroupStaticTable,
       "mvrReceiverGroupStaticEntry": mvrReceiverGroupStaticEntry,
       "mvrReceiverGroupStaticAddress": mvrReceiverGroupStaticAddress,
       "mvrReceiverGroupStaticPorts": mvrReceiverGroupStaticPorts,
       "mvrReceiverGroupStaticStatus": mvrReceiverGroupStaticStatus,
       "mvrReceiverGroupCurrentTable": mvrReceiverGroupCurrentTable,
       "mvrReceiverGroupCurrentEntry": mvrReceiverGroupCurrentEntry,
       "mvrReceiverGroupCurrentAddress": mvrReceiverGroupCurrentAddress,
       "mvrReceiverGroupCurrentPorts": mvrReceiverGroupCurrentPorts,
       "dhcpSnoopMgt": dhcpSnoopMgt,
       "dhcpSnoopGlobal": dhcpSnoopGlobal,
       "dhcpSnoopEnable": dhcpSnoopEnable,
       "dhcpSnoopVerifyMacAddressEnable": dhcpSnoopVerifyMacAddressEnable,
       "dhcpSnoopInformationOptionEnable": dhcpSnoopInformationOptionEnable,
       "dhcpSnoopInformationOptionPolicy": dhcpSnoopInformationOptionPolicy,
       "dhcpSnoopBindingsTableCtlAction": dhcpSnoopBindingsTableCtlAction,
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
       "upnpMgt": upnpMgt,
       "upnpStatus": upnpStatus,
       "upnpAdvertisingDuration": upnpAdvertisingDuration,
       "upnpTtl": upnpTtl,
       "sFlowMgt": sFlowMgt,
       "sFlowStatus": sFlowStatus,
       "sFlowPortTable": sFlowPortTable,
       "sFlowPortEntry": sFlowPortEntry,
       "sFlowPortIndex": sFlowPortIndex,
       "sFlowPortStatus": sFlowPortStatus,
       "dynamicArpInspectionMgt": dynamicArpInspectionMgt,
       "daiGlobal": daiGlobal,
       "daiGlobalStatus": daiGlobalStatus,
       "daiGlobalSrcMacValidation": daiGlobalSrcMacValidation,
       "daiGlobalDestMacValidation": daiGlobalDestMacValidation,
       "daiGlobalIpAddrValidation": daiGlobalIpAddrValidation,
       "daiGlobalLogNumber": daiGlobalLogNumber,
       "daiGlobalLogInterval": daiGlobalLogInterval,
       "daiGlobalAdditionalValidStatus": daiGlobalAdditionalValidStatus,
       "daiVlan": daiVlan,
       "daiVlanTable": daiVlanTable,
       "daiVlanEntry": daiVlanEntry,
       "daiVlanIndex": daiVlanIndex,
       "daiVlanStatus": daiVlanStatus,
       "daiVlanArpAclName": daiVlanArpAclName,
       "daiVlanArpAclStatus": daiVlanArpAclStatus,
       "daiInterface": daiInterface,
       "daiPortTable": daiPortTable,
       "daiPortEntry": daiPortEntry,
       "daiPortIfIndex": daiPortIfIndex,
       "daiPortTrustStatus": daiPortTrustStatus,
       "daiPortRateLimit": daiPortRateLimit,
       "daiLog": daiLog,
       "daiLogTable": daiLogTable,
       "daiLogEntry": daiLogEntry,
       "daiLogIndex": daiLogIndex,
       "daiLogVlan": daiLogVlan,
       "daiLogPort": daiLogPort,
       "daiLogSrcIpAddress": daiLogSrcIpAddress,
       "daiLogDestIpAddress": daiLogDestIpAddress,
       "daiLogSrcMacAddress": daiLogSrcMacAddress,
       "daiLogDestMacAddress": daiLogDestMacAddress,
       "daiStatistics": daiStatistics,
       "daiTotalReceivedPkts": daiTotalReceivedPkts,
       "daiTotalDroppedPkts": daiTotalDroppedPkts,
       "daiTotalProcessedPkts": daiTotalProcessedPkts,
       "daiTotalSrcMacDroppedPkts": daiTotalSrcMacDroppedPkts,
       "daiTotalDestMacDroppedPkts": daiTotalDestMacDroppedPkts,
       "daiTotalIpAddrDroppedPkts": daiTotalIpAddrDroppedPkts,
       "daiTotalArpAclDroppedPkts": daiTotalArpAclDroppedPkts,
       "daiTotalDhcpSnoopingDroppedPkts": daiTotalDhcpSnoopingDroppedPkts,
       "erpsMgt": erpsMgt,
       "erpsGlobalStatus": erpsGlobalStatus,
       "erpsDomainTable": erpsDomainTable,
       "erpsDomainEntry": erpsDomainEntry,
       "erpsDomainIndex": erpsDomainIndex,
       "erpsDomainName": erpsDomainName,
       "erpsDomainMegLevel": erpsDomainMegLevel,
       "erpsDomainNodeId": erpsDomainNodeId,
       "erpsDomainWestRingPort": erpsDomainWestRingPort,
       "erpsDomainEastRingPort": erpsDomainEastRingPort,
       "erpsDomainRplOwner": erpsDomainRplOwner,
       "erpsDomainRplPort": erpsDomainRplPort,
       "erpsDomainGuardTimer": erpsDomainGuardTimer,
       "erpsDomainHoldoffTimer": erpsDomainHoldoffTimer,
       "erpsDomainWtrTimer": erpsDomainWtrTimer,
       "erpsDomainControlVlanID": erpsDomainControlVlanID,
       "erpsDomainNodeState": erpsDomainNodeState,
       "erpsDomainWestRingPortState": erpsDomainWestRingPortState,
       "erpsDomainEastRingPortState": erpsDomainEastRingPortState,
       "erpsDomainRowStatus": erpsDomainRowStatus,
       "erpsDomainMajorDomainIndex": erpsDomainMajorDomainIndex,
       "erpsDomainPropagateTC": erpsDomainPropagateTC,
       "erpsDomainWestMepId": erpsDomainWestMepId,
       "erpsDomainEastMepId": erpsDomainEastMepId,
       "erpsDomainNonErpsDevProtect": erpsDomainNonErpsDevProtect,
       "lbdMgt": lbdMgt,
       "lbdGlobal": lbdGlobal,
       "lbdGlobalStatus": lbdGlobalStatus,
       "lbdTransmitInterval": lbdTransmitInterval,
       "lbdRecoverTime": lbdRecoverTime,
       "lbdMode": lbdMode,
       "lbdInterface": lbdInterface,
       "lbdPortTable": lbdPortTable,
       "lbdPortEntry": lbdPortEntry,
       "lbdPortIfIndex": lbdPortIfIndex,
       "lbdPortAdminState": lbdPortAdminState,
       "lbdPortOperState": lbdPortOperState,
       "lbdPortLoopedVlan": lbdPortLoopedVlan,
       "es3552m-and-poeNotifications": es3552m_and_poeNotifications,
       "es3552m-and-poeTraps": es3552m_and_poeTraps,
       "es3552m-and-poeTrapsPrefix": es3552m_and_poeTrapsPrefix,
       "swPowerStatusChangeTrap": swPowerStatusChangeTrap,
       "swPortSecurityTrap": swPortSecurityTrap,
       "swIpFilterRejectTrap": swIpFilterRejectTrap,
       "swAuthenticationFailure": swAuthenticationFailure,
       "swAuthenticationSuccess": swAuthenticationSuccess,
       "swAtcBcastStormAlarmFireTrap": swAtcBcastStormAlarmFireTrap,
       "swAtcBcastStormAlarmClearTrap": swAtcBcastStormAlarmClearTrap,
       "swAtcBcastStormTcApplyTrap": swAtcBcastStormTcApplyTrap,
       "swAtcBcastStormTcReleaseTrap": swAtcBcastStormTcReleaseTrap,
       "swAtcMcastStormAlarmFireTrap": swAtcMcastStormAlarmFireTrap,
       "swAtcMcastStormAlarmClearTrap": swAtcMcastStormAlarmClearTrap,
       "swAtcMcastStormTcApplyTrap": swAtcMcastStormTcApplyTrap,
       "swAtcMcastStormTcReleaseTrap": swAtcMcastStormTcReleaseTrap,
       "swLoopbackDetectionTrap": swLoopbackDetectionTrap,
       "networkAccessPortLinkDetectionTrap": networkAccessPortLinkDetectionTrap,
       "dot1agCfmMepUpTrap": dot1agCfmMepUpTrap,
       "dot1agCfmMepDownTrap": dot1agCfmMepDownTrap,
       "dot1agCfmConfigFailTrap": dot1agCfmConfigFailTrap,
       "dot1agCfmLoopFindTrap": dot1agCfmLoopFindTrap,
       "dot1agCfmMepUnknownTrap": dot1agCfmMepUnknownTrap,
       "dot1agCfmMepMissingTrap": dot1agCfmMepMissingTrap,
       "dot1agCfmMaUpTrap": dot1agCfmMaUpTrap,
       "autoUpgradeTrap": autoUpgradeTrap,
       "swCpuUtiRisingNotification": swCpuUtiRisingNotification,
       "swCpuUtiFallingNotification": swCpuUtiFallingNotification,
       "swMemoryUtiRisingThresholdNotification": swMemoryUtiRisingThresholdNotification,
       "swMemoryUtiFallingThresholdNotification": swMemoryUtiFallingThresholdNotification,
       "dhcpRougeServerAttackTrap": dhcpRougeServerAttackTrap,
       "lbdDetectionTrap": lbdDetectionTrap,
       "lbdRecoveryTrap": lbdRecoveryTrap,
       "es3552m-and-poeConformance": es3552m_and_poeConformance}
)
