# SNMP MIB module (Hirschmann-GIGA-LION-24TP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/Hirschmann-GIGA-LION-24TP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:53:47 2025
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
 Timeout,
 dot1dStpPort,
 dot1dStpPortEntry) = mibBuilder.importSymbols(
    "BRIDGE-MIB",
    "BridgeId",
    "Timeout",
    "dot1dStpPort",
    "dot1dStpPortEntry")

(hirschmann,) = mibBuilder.importSymbols(
    "HMPRIV-MGMT-SNMP-MIB",
    "hirschmann")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(PortList,
 VlanIndex) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList",
    "VlanIndex")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 MacAddress,
 PhysAddress,
 RowPointer,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gigaLion24tpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5)
)
if mibBuilder.loadTexts:
    gigaLion24tpMIB.setRevisions(
        ("2001-09-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class OspfAreaID(TextualConvention, IpAddress):
    status = "current"


class OspfBigMetric(TextualConvention, Integer32):
    status = "current"


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



class HsrpState(TextualConvention, Integer32):
    status = "current"
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
        *(("initial", 1),
          ("learn", 2),
          ("listen", 3),
          ("speak", 4),
          ("standby", 5),
          ("active", 6))
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

_Hiway_ObjectIdentity = ObjectIdentity
hiway = _Hiway_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13)
)
_FastEtherSwitch24_ObjectIdentity = ObjectIdentity
fastEtherSwitch24 = _FastEtherSwitch24_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7)
)
_Lion24tpMIBObjects_ObjectIdentity = ObjectIdentity
lion24tpMIBObjects = _Lion24tpMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1)
)
_SwitchMgt_ObjectIdentity = ObjectIdentity
switchMgt = _SwitchMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1)
)
_SwitchNumber_Type = Integer32
_SwitchNumber_Object = MibScalar
switchNumber = _SwitchNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 2),
    _SwitchNumber_Type()
)
switchNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchNumber.setStatus("current")
_SwitchInfoTable_Object = MibTable
switchInfoTable = _SwitchInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3)
)
if mibBuilder.loadTexts:
    switchInfoTable.setStatus("current")
_SwitchInfoEntry_Object = MibTableRow
switchInfoEntry = _SwitchInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1)
)
switchInfoEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "swUnitIndex"),
)
if mibBuilder.loadTexts:
    switchInfoEntry.setStatus("current")
_SwUnitIndex_Type = Integer32
_SwUnitIndex_Object = MibTableColumn
swUnitIndex = _SwUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 6),
    _SwOpCodeVer_Type()
)
swOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swOpCodeVer.setStatus("current")
_SwPortNumber_Type = Integer32
_SwPortNumber_Object = MibTableColumn
swPortNumber = _SwPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 10),
    _SwSerialNumber_Type()
)
swSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swSerialNumber.setStatus("current")


class _SwExpansionSlot1_Type(Integer32):
    """Custom type swExpansionSlot1 based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("other", 2),
          ("hundredBaseFxScMmf", 3),
          ("hundredBaseFxScSmf", 4),
          ("hundredBaseFxMtrjMmf", 5),
          ("thousandBaseSxScMmf", 6),
          ("thousandBaseSxMtrjMmf", 7),
          ("thousandBaseXGbic", 8),
          ("thousandBaseLxScSmf", 9),
          ("thousandBaseT", 10),
          ("stackingModule", 11),
          ("thousandBaseSfp", 12),
          ("tenHundredBaseT4port", 13),
          ("tenHundredBaseFxMtrj4port", 14),
          ("comboStackingSfp", 15),
          ("tenHundredBaseT", 16),
          ("comboThousandBaseTxSfp", 17),
          ("eightPortSfpModule", 18),
          ("tenGigaPortModule", 19))
    )


_SwExpansionSlot1_Type.__name__ = "Integer32"
_SwExpansionSlot1_Object = MibTableColumn
swExpansionSlot1 = _SwExpansionSlot1_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 11),
    _SwExpansionSlot1_Type()
)
swExpansionSlot1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swExpansionSlot1.setStatus("current")


class _SwExpansionSlot2_Type(Integer32):
    """Custom type swExpansionSlot2 based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("other", 2),
          ("hundredBaseFxScMmf", 3),
          ("hundredBaseFxScSmf", 4),
          ("hundredBaseFxMtrjMmf", 5),
          ("thousandBaseSxScMmf", 6),
          ("thousandBaseSxMtrjMmf", 7),
          ("thousandBaseXGbic", 8),
          ("thousandBaseLxScSmf", 9),
          ("thousandBaseT", 10),
          ("stackingModule", 11),
          ("thousandBaseSfp", 12),
          ("tenHundredBaseT4port", 13),
          ("tenHundredBaseFxMtrj4port", 14),
          ("comboStackingSfp", 15),
          ("tenHundredBaseT", 16),
          ("comboThousandBaseTxSfp", 17),
          ("eightPortSfpModule", 18),
          ("tenGigaPortModule", 19))
    )


_SwExpansionSlot2_Type.__name__ = "Integer32"
_SwExpansionSlot2_Object = MibTableColumn
swExpansionSlot2 = _SwExpansionSlot2_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 12),
    _SwExpansionSlot2_Type()
)
swExpansionSlot2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swExpansionSlot2.setStatus("current")


class _SwServiceTag_Type(DisplayString):
    """Custom type swServiceTag based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwServiceTag_Type.__name__ = "DisplayString"
_SwServiceTag_Object = MibTableColumn
swServiceTag = _SwServiceTag_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 14),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 15),
    _SwEpldVer_Type()
)
swEpldVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swEpldVer.setStatus("current")


class _SwExpectedModuleOpCodeVer_Type(DisplayString):
    """Custom type swExpectedModuleOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwExpectedModuleOpCodeVer_Type.__name__ = "DisplayString"
_SwExpectedModuleOpCodeVer_Object = MibTableColumn
swExpectedModuleOpCodeVer = _SwExpectedModuleOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 3, 1, 16),
    _SwExpectedModuleOpCodeVer_Type()
)
swExpectedModuleOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swExpectedModuleOpCodeVer.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 4),
    _SwitchOperState_Type()
)
switchOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchOperState.setStatus("current")
_SwitchProductId_ObjectIdentity = ObjectIdentity
switchProductId = _SwitchProductId_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 5)
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 5, 5),
    _SwProdUrl_Type()
)
swProdUrl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swProdUrl.setStatus("current")
_SwIdentifier_Type = Integer32
_SwIdentifier_Object = MibScalar
swIdentifier = _SwIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 5, 6),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 5, 7),
    _SwChassisServiceTag_Type()
)
swChassisServiceTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swChassisServiceTag.setStatus("current")
_SwitchIndivPowerTable_Object = MibTable
switchIndivPowerTable = _SwitchIndivPowerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 6)
)
if mibBuilder.loadTexts:
    switchIndivPowerTable.setStatus("current")
_SwitchIndivPowerEntry_Object = MibTableRow
switchIndivPowerEntry = _SwitchIndivPowerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 6, 1)
)
switchIndivPowerEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "swIndivPowerUnitIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "swIndivPowerIndex"),
)
if mibBuilder.loadTexts:
    switchIndivPowerEntry.setStatus("current")
_SwIndivPowerUnitIndex_Type = Integer32
_SwIndivPowerUnitIndex_Object = MibTableColumn
swIndivPowerUnitIndex = _SwIndivPowerUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 6, 1, 1),
    _SwIndivPowerUnitIndex_Type()
)
swIndivPowerUnitIndex.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 6, 1, 2),
    _SwIndivPowerIndex_Type()
)
swIndivPowerIndex.setMaxAccess("read-only")
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 7),
    _SwitchJumboFrameStatus_Type()
)
switchJumboFrameStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchJumboFrameStatus.setStatus("current")
_AmtrMgt_ObjectIdentity = ObjectIdentity
amtrMgt = _AmtrMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 8)
)
_AmtrMacAddrAgingStatus_Type = EnabledStatus
_AmtrMacAddrAgingStatus_Object = MibScalar
amtrMacAddrAgingStatus = _AmtrMacAddrAgingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 8, 3),
    _AmtrMacAddrAgingStatus_Type()
)
amtrMacAddrAgingStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    amtrMacAddrAgingStatus.setStatus("current")
_SwitchFanTable_Object = MibTable
switchFanTable = _SwitchFanTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 9)
)
if mibBuilder.loadTexts:
    switchFanTable.setStatus("current")
_SwitchFanEntry_Object = MibTableRow
switchFanEntry = _SwitchFanEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 9, 1)
)
switchFanEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "switchUnitIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "switchFanIndex"),
)
if mibBuilder.loadTexts:
    switchFanEntry.setStatus("current")
_SwitchUnitIndex_Type = Integer32
_SwitchUnitIndex_Object = MibTableColumn
switchUnitIndex = _SwitchUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 9, 1, 1),
    _SwitchUnitIndex_Type()
)
switchUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchUnitIndex.setStatus("current")
_SwitchFanIndex_Type = Integer32
_SwitchFanIndex_Object = MibTableColumn
switchFanIndex = _SwitchFanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 9, 1, 2),
    _SwitchFanIndex_Type()
)
switchFanIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchFanIndex.setStatus("current")


class _SwitchFanStatus_Type(Integer32):
    """Custom type switchFanStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("failure", 2))
    )


_SwitchFanStatus_Type.__name__ = "Integer32"
_SwitchFanStatus_Object = MibTableColumn
switchFanStatus = _SwitchFanStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 9, 1, 3),
    _SwitchFanStatus_Type()
)
switchFanStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchFanStatus.setStatus("current")
_SwitchFanAdminSpeed_Type = Integer32
_SwitchFanAdminSpeed_Object = MibTableColumn
switchFanAdminSpeed = _SwitchFanAdminSpeed_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 9, 1, 4),
    _SwitchFanAdminSpeed_Type()
)
switchFanAdminSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchFanAdminSpeed.setStatus("current")
_SwitchFanFailureCount_Type = Integer32
_SwitchFanFailureCount_Object = MibTableColumn
switchFanFailureCount = _SwitchFanFailureCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 9, 1, 5),
    _SwitchFanFailureCount_Type()
)
switchFanFailureCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchFanFailureCount.setStatus("current")
_SwitchFanOperSpeed_Type = Integer32
_SwitchFanOperSpeed_Object = MibTableColumn
switchFanOperSpeed = _SwitchFanOperSpeed_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 9, 1, 6),
    _SwitchFanOperSpeed_Type()
)
switchFanOperSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchFanOperSpeed.setStatus("current")
_SwitchThermalTempTable_Object = MibTable
switchThermalTempTable = _SwitchThermalTempTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 11)
)
if mibBuilder.loadTexts:
    switchThermalTempTable.setStatus("current")
_SwitchThermalTempEntry_Object = MibTableRow
switchThermalTempEntry = _SwitchThermalTempEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 11, 1)
)
switchThermalTempEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "switchThermalTempUnitIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "switchThermalTempThermalIndex"),
)
if mibBuilder.loadTexts:
    switchThermalTempEntry.setStatus("current")
_SwitchThermalTempUnitIndex_Type = Integer32
_SwitchThermalTempUnitIndex_Object = MibTableColumn
switchThermalTempUnitIndex = _SwitchThermalTempUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 11, 1, 1),
    _SwitchThermalTempUnitIndex_Type()
)
switchThermalTempUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchThermalTempUnitIndex.setStatus("current")
_SwitchThermalTempThermalIndex_Type = Integer32
_SwitchThermalTempThermalIndex_Object = MibTableColumn
switchThermalTempThermalIndex = _SwitchThermalTempThermalIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 11, 1, 2),
    _SwitchThermalTempThermalIndex_Type()
)
switchThermalTempThermalIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    switchThermalTempThermalIndex.setStatus("current")
_SwitchThermalTempValue_Type = Integer32
_SwitchThermalTempValue_Object = MibTableColumn
switchThermalTempValue = _SwitchThermalTempValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 11, 1, 3),
    _SwitchThermalTempValue_Type()
)
switchThermalTempValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchThermalTempValue.setStatus("current")
_SwitchThermalActionTable_Object = MibTable
switchThermalActionTable = _SwitchThermalActionTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 12)
)
if mibBuilder.loadTexts:
    switchThermalActionTable.setStatus("current")
_SwitchThermalActionEntry_Object = MibTableRow
switchThermalActionEntry = _SwitchThermalActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 12, 1)
)
switchThermalActionEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "switchThermalActionUnitIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "switchThermalActionThermalIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "switchThermalActionIndex"),
)
if mibBuilder.loadTexts:
    switchThermalActionEntry.setStatus("current")
_SwitchThermalActionUnitIndex_Type = Integer32
_SwitchThermalActionUnitIndex_Object = MibTableColumn
switchThermalActionUnitIndex = _SwitchThermalActionUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 12, 1, 1),
    _SwitchThermalActionUnitIndex_Type()
)
switchThermalActionUnitIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchThermalActionUnitIndex.setStatus("current")
_SwitchThermalActionThermalIndex_Type = Integer32
_SwitchThermalActionThermalIndex_Object = MibTableColumn
switchThermalActionThermalIndex = _SwitchThermalActionThermalIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 12, 1, 2),
    _SwitchThermalActionThermalIndex_Type()
)
switchThermalActionThermalIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchThermalActionThermalIndex.setStatus("current")
_SwitchThermalActionIndex_Type = Integer32
_SwitchThermalActionIndex_Object = MibTableColumn
switchThermalActionIndex = _SwitchThermalActionIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 12, 1, 3),
    _SwitchThermalActionIndex_Type()
)
switchThermalActionIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    switchThermalActionIndex.setStatus("current")
_SwitchThermalActionRisingThreshold_Type = Integer32
_SwitchThermalActionRisingThreshold_Object = MibTableColumn
switchThermalActionRisingThreshold = _SwitchThermalActionRisingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 12, 1, 4),
    _SwitchThermalActionRisingThreshold_Type()
)
switchThermalActionRisingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    switchThermalActionRisingThreshold.setStatus("current")
_SwitchThermalActionFallingThreshold_Type = Integer32
_SwitchThermalActionFallingThreshold_Object = MibTableColumn
switchThermalActionFallingThreshold = _SwitchThermalActionFallingThreshold_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 12, 1, 5),
    _SwitchThermalActionFallingThreshold_Type()
)
switchThermalActionFallingThreshold.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    switchThermalActionFallingThreshold.setStatus("current")


class _SwitchThermalActionAction_Type(Bits):
    """Custom type switchThermalActionAction based on Bits"""
    namedValues = NamedValues(
        ("trap", 0)
    )

_SwitchThermalActionAction_Type.__name__ = "Bits"
_SwitchThermalActionAction_Object = MibTableColumn
switchThermalActionAction = _SwitchThermalActionAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 12, 1, 6),
    _SwitchThermalActionAction_Type()
)
switchThermalActionAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    switchThermalActionAction.setStatus("current")
_SwitchThermalActionStatus_Type = ValidStatus
_SwitchThermalActionStatus_Object = MibTableColumn
switchThermalActionStatus = _SwitchThermalActionStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 12, 1, 7),
    _SwitchThermalActionStatus_Type()
)
switchThermalActionStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    switchThermalActionStatus.setStatus("current")
_SwitchModuleInfoTable_Object = MibTable
switchModuleInfoTable = _SwitchModuleInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13)
)
if mibBuilder.loadTexts:
    switchModuleInfoTable.setStatus("current")
_SwitchModuleInfoEntry_Object = MibTableRow
switchModuleInfoEntry = _SwitchModuleInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1)
)
switchModuleInfoEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "swModuleUnitIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "swModuleModuleIndex"),
)
if mibBuilder.loadTexts:
    switchModuleInfoEntry.setStatus("current")
_SwModuleUnitIndex_Type = Integer32
_SwModuleUnitIndex_Object = MibTableColumn
swModuleUnitIndex = _SwModuleUnitIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 1),
    _SwModuleUnitIndex_Type()
)
swModuleUnitIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swModuleUnitIndex.setStatus("current")
_SwModuleModuleIndex_Type = Integer32
_SwModuleModuleIndex_Object = MibTableColumn
swModuleModuleIndex = _SwModuleModuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 2),
    _SwModuleModuleIndex_Type()
)
swModuleModuleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    swModuleModuleIndex.setStatus("current")


class _SwModuleHardwareVer_Type(DisplayString):
    """Custom type swModuleHardwareVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwModuleHardwareVer_Type.__name__ = "DisplayString"
_SwModuleHardwareVer_Object = MibTableColumn
swModuleHardwareVer = _SwModuleHardwareVer_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 3),
    _SwModuleHardwareVer_Type()
)
swModuleHardwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleHardwareVer.setStatus("current")


class _SwModuleMicrocodeVer_Type(DisplayString):
    """Custom type swModuleMicrocodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwModuleMicrocodeVer_Type.__name__ = "DisplayString"
_SwModuleMicrocodeVer_Object = MibTableColumn
swModuleMicrocodeVer = _SwModuleMicrocodeVer_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 4),
    _SwModuleMicrocodeVer_Type()
)
swModuleMicrocodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleMicrocodeVer.setStatus("current")


class _SwModuleLoaderVer_Type(DisplayString):
    """Custom type swModuleLoaderVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwModuleLoaderVer_Type.__name__ = "DisplayString"
_SwModuleLoaderVer_Object = MibTableColumn
swModuleLoaderVer = _SwModuleLoaderVer_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 5),
    _SwModuleLoaderVer_Type()
)
swModuleLoaderVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleLoaderVer.setStatus("current")


class _SwModuleBootRomVer_Type(DisplayString):
    """Custom type swModuleBootRomVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwModuleBootRomVer_Type.__name__ = "DisplayString"
_SwModuleBootRomVer_Object = MibTableColumn
swModuleBootRomVer = _SwModuleBootRomVer_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 6),
    _SwModuleBootRomVer_Type()
)
swModuleBootRomVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleBootRomVer.setStatus("current")


class _SwModuleOpCodeVer_Type(DisplayString):
    """Custom type swModuleOpCodeVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwModuleOpCodeVer_Type.__name__ = "DisplayString"
_SwModuleOpCodeVer_Object = MibTableColumn
swModuleOpCodeVer = _SwModuleOpCodeVer_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 7),
    _SwModuleOpCodeVer_Type()
)
swModuleOpCodeVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleOpCodeVer.setStatus("current")
_SwModulePortNumber_Type = Integer32
_SwModulePortNumber_Object = MibTableColumn
swModulePortNumber = _SwModulePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 8),
    _SwModulePortNumber_Type()
)
swModulePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModulePortNumber.setStatus("current")


class _SwModuleSerialNumber_Type(DisplayString):
    """Custom type swModuleSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_SwModuleSerialNumber_Type.__name__ = "DisplayString"
_SwModuleSerialNumber_Object = MibTableColumn
swModuleSerialNumber = _SwModuleSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 9),
    _SwModuleSerialNumber_Type()
)
swModuleSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleSerialNumber.setStatus("current")


class _SwModuleType_Type(Integer32):
    """Custom type swModuleType based on Integer32"""
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
              19)
        )
    )
    namedValues = NamedValues(
        *(("notPresent", 1),
          ("other", 2),
          ("hundredBaseFxScMmf", 3),
          ("hundredBaseFxScSmf", 4),
          ("hundredBaseFxMtrjMmf", 5),
          ("thousandBaseSxScMmf", 6),
          ("thousandBaseSxMtrjMmf", 7),
          ("thousandBaseXGbic", 8),
          ("thousandBaseLxScSmf", 9),
          ("thousandBaseT", 10),
          ("stackingModule", 11),
          ("thousandBaseSfp", 12),
          ("tenHundredBaseT4port", 13),
          ("tenHundredBaseFxMtrj4port", 14),
          ("comboStackingSfp", 15),
          ("tenHundredBaseT", 16),
          ("comboThousandBaseTxSfp", 17),
          ("eightPortSfpModule", 18),
          ("tenGigaPortModule", 19))
    )


_SwModuleType_Type.__name__ = "Integer32"
_SwModuleType_Object = MibTableColumn
swModuleType = _SwModuleType_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 10),
    _SwModuleType_Type()
)
swModuleType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleType.setStatus("current")


class _SwModuleModelNumber_Type(DisplayString):
    """Custom type swModuleModelNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_SwModuleModelNumber_Type.__name__ = "DisplayString"
_SwModuleModelNumber_Object = MibTableColumn
swModuleModelNumber = _SwModuleModelNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 11),
    _SwModuleModelNumber_Type()
)
swModuleModelNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleModelNumber.setStatus("current")


class _SwModuleEpldVer_Type(DisplayString):
    """Custom type swModuleEpldVer based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_SwModuleEpldVer_Type.__name__ = "DisplayString"
_SwModuleEpldVer_Object = MibTableColumn
swModuleEpldVer = _SwModuleEpldVer_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 12),
    _SwModuleEpldVer_Type()
)
swModuleEpldVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleEpldVer.setStatus("current")


class _SwModuleDescr_Type(DisplayString):
    """Custom type swModuleDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_SwModuleDescr_Type.__name__ = "DisplayString"
_SwModuleDescr_Object = MibTableColumn
swModuleDescr = _SwModuleDescr_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 13, 1, 13),
    _SwModuleDescr_Type()
)
swModuleDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    swModuleDescr.setStatus("current")


class _SwitchRenumberUnitID_Type(Integer32):
    """Custom type switchRenumberUnitID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("renumber", 1),
          ("noRenumber", 2))
    )


_SwitchRenumberUnitID_Type.__name__ = "Integer32"
_SwitchRenumberUnitID_Object = MibScalar
switchRenumberUnitID = _SwitchRenumberUnitID_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 1, 14),
    _SwitchRenumberUnitID_Type()
)
switchRenumberUnitID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    switchRenumberUnitID.setStatus("current")
_PortMgt_ObjectIdentity = ObjectIdentity
portMgt = _PortMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2)
)
_PortTable_Object = MibTable
portTable = _PortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1)
)
if mibBuilder.loadTexts:
    portTable.setStatus("current")
_PortEntry_Object = MibTableRow
portEntry = _PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1)
)
portEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "portIndex"),
)
if mibBuilder.loadTexts:
    portEntry.setStatus("current")
_PortIndex_Type = Integer32
_PortIndex_Object = MibTableColumn
portIndex = _PortIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 4),
    _PortSpeedDpxCfg_Type()
)
portSpeedDpxCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSpeedDpxCfg.setStatus("current")


class _PortFlowCtrlCfg_Type(Integer32):
    """Custom type portFlowCtrlCfg based on Integer32"""
    defaultValue = 1

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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 6),
    _PortCapabilities_Type()
)
portCapabilities.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portCapabilities.setStatus("current")
_PortAutonegotiation_Type = EnabledStatus
_PortAutonegotiation_Object = MibTableColumn
portAutonegotiation = _PortAutonegotiation_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 9),
    _PortFlowCtrlStatus_Type()
)
portFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    portFlowCtrlStatus.setStatus("current")
_PortTrunkIndex_Type = Integer32
_PortTrunkIndex_Object = MibTableColumn
portTrunkIndex = _PortTrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 2, 1, 1, 12),
    _PortComboForcedMode_Type()
)
portComboForcedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portComboForcedMode.setStatus("current")
_TrunkMgt_ObjectIdentity = ObjectIdentity
trunkMgt = _TrunkMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 3)
)
_TrunkMaxId_Type = Integer32
_TrunkMaxId_Object = MibScalar
trunkMaxId = _TrunkMaxId_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 3, 1),
    _TrunkMaxId_Type()
)
trunkMaxId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkMaxId.setStatus("current")
_TrunkValidNumber_Type = Integer32
_TrunkValidNumber_Object = MibScalar
trunkValidNumber = _TrunkValidNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 3, 2),
    _TrunkValidNumber_Type()
)
trunkValidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkValidNumber.setStatus("current")
_TrunkTable_Object = MibTable
trunkTable = _TrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 3, 3)
)
if mibBuilder.loadTexts:
    trunkTable.setStatus("current")
_TrunkEntry_Object = MibTableRow
trunkEntry = _TrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 3, 3, 1)
)
trunkEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "trunkIndex"),
)
if mibBuilder.loadTexts:
    trunkEntry.setStatus("current")
_TrunkIndex_Type = Integer32
_TrunkIndex_Object = MibTableColumn
trunkIndex = _TrunkIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 3, 3, 1, 1),
    _TrunkIndex_Type()
)
trunkIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trunkIndex.setStatus("current")
_TrunkPorts_Type = PortList
_TrunkPorts_Object = MibTableColumn
trunkPorts = _TrunkPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 3, 3, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 3, 3, 1, 3),
    _TrunkCreation_Type()
)
trunkCreation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trunkCreation.setStatus("current")
_TrunkStatus_Type = ValidStatus
_TrunkStatus_Object = MibTableColumn
trunkStatus = _TrunkStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 3, 3, 1, 4),
    _TrunkStatus_Type()
)
trunkStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trunkStatus.setStatus("current")
_LacpMgt_ObjectIdentity = ObjectIdentity
lacpMgt = _LacpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 4)
)
_LacpPortTable_Object = MibTable
lacpPortTable = _LacpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 4, 1)
)
if mibBuilder.loadTexts:
    lacpPortTable.setStatus("current")
_LacpPortEntry_Object = MibTableRow
lacpPortEntry = _LacpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 4, 1, 1)
)
lacpPortEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "lacpPortIndex"),
)
if mibBuilder.loadTexts:
    lacpPortEntry.setStatus("current")
_LacpPortIndex_Type = Integer32
_LacpPortIndex_Object = MibTableColumn
lacpPortIndex = _LacpPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 4, 1, 1, 1),
    _LacpPortIndex_Type()
)
lacpPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    lacpPortIndex.setStatus("current")
_LacpPortStatus_Type = EnabledStatus
_LacpPortStatus_Object = MibTableColumn
lacpPortStatus = _LacpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 4, 1, 1, 2),
    _LacpPortStatus_Type()
)
lacpPortStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lacpPortStatus.setStatus("current")
_StaMgt_ObjectIdentity = ObjectIdentity
staMgt = _StaMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5)
)


class _StaSystemStatus_Type(EnabledStatus):
    """Custom type staSystemStatus based on EnabledStatus"""
    defaultValue = 1


_StaSystemStatus_Type.__name__ = "EnabledStatus"
_StaSystemStatus_Object = MibScalar
staSystemStatus = _StaSystemStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 1),
    _StaSystemStatus_Type()
)
staSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staSystemStatus.setStatus("current")
_StaPortTable_Object = MibTable
staPortTable = _StaPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2)
)
if mibBuilder.loadTexts:
    staPortTable.setStatus("current")
_StaPortEntry_Object = MibTableRow
staPortEntry = _StaPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2, 1)
)
if mibBuilder.loadTexts:
    staPortEntry.setStatus("current")
_StaPortFastForward_Type = EnabledStatus
_StaPortFastForward_Object = MibTableColumn
staPortFastForward = _StaPortFastForward_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2, 1, 2),
    _StaPortFastForward_Type()
)
staPortFastForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortFastForward.setStatus("current")
_StaPortProtocolMigration_Type = TruthValue
_StaPortProtocolMigration_Object = MibTableColumn
staPortProtocolMigration = _StaPortProtocolMigration_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2, 1, 3),
    _StaPortProtocolMigration_Type()
)
staPortProtocolMigration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortProtocolMigration.setStatus("current")
_StaPortAdminEdgePort_Type = TruthValue
_StaPortAdminEdgePort_Object = MibTableColumn
staPortAdminEdgePort = _StaPortAdminEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2, 1, 4),
    _StaPortAdminEdgePort_Type()
)
staPortAdminEdgePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminEdgePort.setStatus("current")
_StaPortOperEdgePort_Type = TruthValue
_StaPortOperEdgePort_Object = MibTableColumn
staPortOperEdgePort = _StaPortOperEdgePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2, 1, 6),
    _StaPortAdminPointToPoint_Type()
)
staPortAdminPointToPoint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortAdminPointToPoint.setStatus("current")
_StaPortOperPointToPoint_Type = TruthValue
_StaPortOperPointToPoint_Object = MibTableColumn
staPortOperPointToPoint = _StaPortOperPointToPoint_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2, 1, 9),
    _StaPortSystemStatus_Type()
)
staPortSystemStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPortSystemStatus.setStatus("current")


class _StaPortLongAdminPathCost_Type(Integer32):
    """Custom type staPortLongAdminPathCost based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 200000000),
    )


_StaPortLongAdminPathCost_Type.__name__ = "Integer32"
_StaPortLongAdminPathCost_Object = MibTableColumn
staPortLongAdminPathCost = _StaPortLongAdminPathCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2, 1, 10),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 2, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 5),
    _StaPathCostMethod_Type()
)
staPathCostMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    staPathCostMethod.setStatus("current")
_XstMgt_ObjectIdentity = ObjectIdentity
xstMgt = _XstMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6)
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 1),
    _MstName_Type()
)
mstName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstName.setStatus("current")
_MstRevision_Type = Integer32
_MstRevision_Object = MibScalar
mstRevision = _MstRevision_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 3),
    _MstMaxHops_Type()
)
mstMaxHops.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    mstMaxHops.setStatus("current")
_XstInstanceCfgTable_Object = MibTable
xstInstanceCfgTable = _XstInstanceCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4)
)
if mibBuilder.loadTexts:
    xstInstanceCfgTable.setStatus("current")
_XstInstanceCfgEntry_Object = MibTableRow
xstInstanceCfgEntry = _XstInstanceCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1)
)
xstInstanceCfgEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "xstInstanceCfgIndex"),
)
if mibBuilder.loadTexts:
    xstInstanceCfgEntry.setStatus("current")


class _XstInstanceCfgIndex_Type(Integer32):
    """Custom type xstInstanceCfgIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_XstInstanceCfgIndex_Type.__name__ = "Integer32"
_XstInstanceCfgIndex_Object = MibTableColumn
xstInstanceCfgIndex = _XstInstanceCfgIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 2),
    _XstInstanceCfgPriority_Type()
)
xstInstanceCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    xstInstanceCfgPriority.setStatus("current")
_XstInstanceCfgTimeSinceTopologyChange_Type = TimeTicks
_XstInstanceCfgTimeSinceTopologyChange_Object = MibTableColumn
xstInstanceCfgTimeSinceTopologyChange = _XstInstanceCfgTimeSinceTopologyChange_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 3),
    _XstInstanceCfgTimeSinceTopologyChange_Type()
)
xstInstanceCfgTimeSinceTopologyChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTimeSinceTopologyChange.setStatus("current")
_XstInstanceCfgTopChanges_Type = Integer32
_XstInstanceCfgTopChanges_Object = MibTableColumn
xstInstanceCfgTopChanges = _XstInstanceCfgTopChanges_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 4),
    _XstInstanceCfgTopChanges_Type()
)
xstInstanceCfgTopChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTopChanges.setStatus("current")
_XstInstanceCfgDesignatedRoot_Type = BridgeId
_XstInstanceCfgDesignatedRoot_Object = MibTableColumn
xstInstanceCfgDesignatedRoot = _XstInstanceCfgDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 5),
    _XstInstanceCfgDesignatedRoot_Type()
)
xstInstanceCfgDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgDesignatedRoot.setStatus("current")
_XstInstanceCfgRootCost_Type = Integer32
_XstInstanceCfgRootCost_Object = MibTableColumn
xstInstanceCfgRootCost = _XstInstanceCfgRootCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 6),
    _XstInstanceCfgRootCost_Type()
)
xstInstanceCfgRootCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootCost.setStatus("current")
_XstInstanceCfgRootPort_Type = Integer32
_XstInstanceCfgRootPort_Object = MibTableColumn
xstInstanceCfgRootPort = _XstInstanceCfgRootPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 7),
    _XstInstanceCfgRootPort_Type()
)
xstInstanceCfgRootPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgRootPort.setStatus("current")
_XstInstanceCfgMaxAge_Type = Timeout
_XstInstanceCfgMaxAge_Object = MibTableColumn
xstInstanceCfgMaxAge = _XstInstanceCfgMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 8),
    _XstInstanceCfgMaxAge_Type()
)
xstInstanceCfgMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgMaxAge.setStatus("current")
_XstInstanceCfgHelloTime_Type = Timeout
_XstInstanceCfgHelloTime_Object = MibTableColumn
xstInstanceCfgHelloTime = _XstInstanceCfgHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 9),
    _XstInstanceCfgHelloTime_Type()
)
xstInstanceCfgHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHelloTime.setStatus("current")
_XstInstanceCfgHoldTime_Type = Timeout
_XstInstanceCfgHoldTime_Object = MibTableColumn
xstInstanceCfgHoldTime = _XstInstanceCfgHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 10),
    _XstInstanceCfgHoldTime_Type()
)
xstInstanceCfgHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgHoldTime.setStatus("current")
_XstInstanceCfgForwardDelay_Type = Timeout
_XstInstanceCfgForwardDelay_Object = MibTableColumn
xstInstanceCfgForwardDelay = _XstInstanceCfgForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 11),
    _XstInstanceCfgForwardDelay_Type()
)
xstInstanceCfgForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgForwardDelay.setStatus("current")
_XstInstanceCfgBridgeMaxAge_Type = Timeout
_XstInstanceCfgBridgeMaxAge_Object = MibTableColumn
xstInstanceCfgBridgeMaxAge = _XstInstanceCfgBridgeMaxAge_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 12),
    _XstInstanceCfgBridgeMaxAge_Type()
)
xstInstanceCfgBridgeMaxAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeMaxAge.setStatus("current")
_XstInstanceCfgBridgeHelloTime_Type = Timeout
_XstInstanceCfgBridgeHelloTime_Object = MibTableColumn
xstInstanceCfgBridgeHelloTime = _XstInstanceCfgBridgeHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 13),
    _XstInstanceCfgBridgeHelloTime_Type()
)
xstInstanceCfgBridgeHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeHelloTime.setStatus("current")
_XstInstanceCfgBridgeForwardDelay_Type = Timeout
_XstInstanceCfgBridgeForwardDelay_Object = MibTableColumn
xstInstanceCfgBridgeForwardDelay = _XstInstanceCfgBridgeForwardDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 14),
    _XstInstanceCfgBridgeForwardDelay_Type()
)
xstInstanceCfgBridgeForwardDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgBridgeForwardDelay.setStatus("current")
_XstInstanceCfgTxHoldCount_Type = Integer32
_XstInstanceCfgTxHoldCount_Object = MibTableColumn
xstInstanceCfgTxHoldCount = _XstInstanceCfgTxHoldCount_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 15),
    _XstInstanceCfgTxHoldCount_Type()
)
xstInstanceCfgTxHoldCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgTxHoldCount.setStatus("current")
_XstInstanceCfgPathCostMethod_Type = StaPathCostMode
_XstInstanceCfgPathCostMethod_Object = MibTableColumn
xstInstanceCfgPathCostMethod = _XstInstanceCfgPathCostMethod_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 4, 1, 16),
    _XstInstanceCfgPathCostMethod_Type()
)
xstInstanceCfgPathCostMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstanceCfgPathCostMethod.setStatus("current")
_XstInstancePortTable_Object = MibTable
xstInstancePortTable = _XstInstancePortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5)
)
if mibBuilder.loadTexts:
    xstInstancePortTable.setStatus("current")
_XstInstancePortEntry_Object = MibTableRow
xstInstancePortEntry = _XstInstancePortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1)
)
xstInstancePortEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "xstInstanceCfgIndex"),
    (0, "BRIDGE-MIB", "dot1dStpPort"),
)
if mibBuilder.loadTexts:
    xstInstancePortEntry.setStatus("current")


class _XstInstancePortPriority_Type(Integer32):
    """Custom type xstInstancePortPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_XstInstancePortPriority_Type.__name__ = "Integer32"
_XstInstancePortPriority_Object = MibTableColumn
xstInstancePortPriority = _XstInstancePortPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 4),
    _XstInstancePortState_Type()
)
xstInstancePortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortState.setStatus("current")
_XstInstancePortEnable_Type = EnabledStatus
_XstInstancePortEnable_Object = MibTableColumn
xstInstancePortEnable = _XstInstancePortEnable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 5),
    _XstInstancePortEnable_Type()
)
xstInstancePortEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortEnable.setStatus("current")
_XstInstancePortDesignatedRoot_Type = BridgeId
_XstInstancePortDesignatedRoot_Object = MibTableColumn
xstInstancePortDesignatedRoot = _XstInstancePortDesignatedRoot_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 7),
    _XstInstancePortDesignatedRoot_Type()
)
xstInstancePortDesignatedRoot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedRoot.setStatus("current")
_XstInstancePortDesignatedCost_Type = Integer32
_XstInstancePortDesignatedCost_Object = MibTableColumn
xstInstancePortDesignatedCost = _XstInstancePortDesignatedCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 8),
    _XstInstancePortDesignatedCost_Type()
)
xstInstancePortDesignatedCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedCost.setStatus("current")
_XstInstancePortDesignatedBridge_Type = BridgeId
_XstInstancePortDesignatedBridge_Object = MibTableColumn
xstInstancePortDesignatedBridge = _XstInstancePortDesignatedBridge_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 10),
    _XstInstancePortDesignatedPort_Type()
)
xstInstancePortDesignatedPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortDesignatedPort.setStatus("current")
_XstInstancePortForwardTransitions_Type = Counter32
_XstInstancePortForwardTransitions_Object = MibTableColumn
xstInstancePortForwardTransitions = _XstInstancePortForwardTransitions_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 11),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 12),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 13),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 5, 1, 14),
    _XstInstancePortOperPathCost_Type()
)
xstInstancePortOperPathCost.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    xstInstancePortOperPathCost.setStatus("current")
_MstInstanceEditTable_Object = MibTable
mstInstanceEditTable = _MstInstanceEditTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 6)
)
if mibBuilder.loadTexts:
    mstInstanceEditTable.setStatus("current")
_MstInstanceEditEntry_Object = MibTableRow
mstInstanceEditEntry = _MstInstanceEditEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 6, 1)
)
mstInstanceEditEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "mstInstanceEditIndex"),
)
if mibBuilder.loadTexts:
    mstInstanceEditEntry.setStatus("current")


class _MstInstanceEditIndex_Type(Integer32):
    """Custom type mstInstanceEditIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_MstInstanceEditIndex_Type.__name__ = "Integer32"
_MstInstanceEditIndex_Object = MibTableColumn
mstInstanceEditIndex = _MstInstanceEditIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 6, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 6, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 6, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 6, 1, 5),
    _MstInstanceEditVlansMap4k_Type()
)
mstInstanceEditVlansMap4k.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mstInstanceEditVlansMap4k.setStatus("current")
_MstInstanceEditRemainingHops_Type = Integer32
_MstInstanceEditRemainingHops_Object = MibTableColumn
mstInstanceEditRemainingHops = _MstInstanceEditRemainingHops_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 6, 1, 6),
    _MstInstanceEditRemainingHops_Type()
)
mstInstanceEditRemainingHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceEditRemainingHops.setStatus("current")
_MstInstanceOperTable_Object = MibTable
mstInstanceOperTable = _MstInstanceOperTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 7)
)
if mibBuilder.loadTexts:
    mstInstanceOperTable.setStatus("current")
_MstInstanceOperEntry_Object = MibTableRow
mstInstanceOperEntry = _MstInstanceOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 7, 1)
)
mstInstanceOperEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "mstInstanceOperIndex"),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 7, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 7, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 7, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 5, 6, 7, 1, 5),
    _MstInstanceOperVlansMap4k_Type()
)
mstInstanceOperVlansMap4k.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    mstInstanceOperVlansMap4k.setStatus("current")
_RestartMgt_ObjectIdentity = ObjectIdentity
restartMgt = _RestartMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 7)
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 7, 3),
    _RestartControl_Type()
)
restartControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    restartControl.setStatus("current")
_MirrorMgt_ObjectIdentity = ObjectIdentity
mirrorMgt = _MirrorMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 8)
)
_MirrorTable_Object = MibTable
mirrorTable = _MirrorTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 8, 1)
)
if mibBuilder.loadTexts:
    mirrorTable.setStatus("current")
_MirrorEntry_Object = MibTableRow
mirrorEntry = _MirrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 8, 1, 1)
)
mirrorEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "mirrorDestinationPort"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "mirrorSourcePort"),
)
if mibBuilder.loadTexts:
    mirrorEntry.setStatus("current")
_MirrorDestinationPort_Type = Integer32
_MirrorDestinationPort_Object = MibTableColumn
mirrorDestinationPort = _MirrorDestinationPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 8, 1, 1, 1),
    _MirrorDestinationPort_Type()
)
mirrorDestinationPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    mirrorDestinationPort.setStatus("current")
_MirrorSourcePort_Type = Integer32
_MirrorSourcePort_Object = MibTableColumn
mirrorSourcePort = _MirrorSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 8, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 8, 1, 1, 3),
    _MirrorType_Type()
)
mirrorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorType.setStatus("current")
_MirrorStatus_Type = ValidStatus
_MirrorStatus_Object = MibTableColumn
mirrorStatus = _MirrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 8, 1, 1, 4),
    _MirrorStatus_Type()
)
mirrorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    mirrorStatus.setStatus("current")
_IgmpSnoopMgt_ObjectIdentity = ObjectIdentity
igmpSnoopMgt = _IgmpSnoopMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9)
)


class _IgmpSnoopStatus_Type(EnabledStatus):
    """Custom type igmpSnoopStatus based on EnabledStatus"""
    defaultValue = 1


_IgmpSnoopStatus_Type.__name__ = "EnabledStatus"
_IgmpSnoopStatus_Object = MibScalar
igmpSnoopStatus = _IgmpSnoopStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 5),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 6),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 7),
    _IgmpSnoopVersion_Type()
)
igmpSnoopVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSnoopVersion.setStatus("current")
_IgmpSnoopRouterCurrentTable_Object = MibTable
igmpSnoopRouterCurrentTable = _IgmpSnoopRouterCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 8)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentTable.setStatus("current")
_IgmpSnoopRouterCurrentEntry_Object = MibTableRow
igmpSnoopRouterCurrentEntry = _IgmpSnoopRouterCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 8, 1)
)
igmpSnoopRouterCurrentEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "igmpSnoopRouterCurrentVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentEntry.setStatus("current")
_IgmpSnoopRouterCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopRouterCurrentVlanIndex_Object = MibTableColumn
igmpSnoopRouterCurrentVlanIndex = _IgmpSnoopRouterCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 8, 1, 1),
    _IgmpSnoopRouterCurrentVlanIndex_Type()
)
igmpSnoopRouterCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentVlanIndex.setStatus("current")
_IgmpSnoopRouterCurrentPorts_Type = PortList
_IgmpSnoopRouterCurrentPorts_Object = MibTableColumn
igmpSnoopRouterCurrentPorts = _IgmpSnoopRouterCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 8, 1, 2),
    _IgmpSnoopRouterCurrentPorts_Type()
)
igmpSnoopRouterCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentPorts.setStatus("current")
_IgmpSnoopRouterCurrentStatus_Type = PortList
_IgmpSnoopRouterCurrentStatus_Object = MibTableColumn
igmpSnoopRouterCurrentStatus = _IgmpSnoopRouterCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 8, 1, 3),
    _IgmpSnoopRouterCurrentStatus_Type()
)
igmpSnoopRouterCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopRouterCurrentStatus.setStatus("current")
_IgmpSnoopRouterStaticTable_Object = MibTable
igmpSnoopRouterStaticTable = _IgmpSnoopRouterStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 9)
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticTable.setStatus("current")
_IgmpSnoopRouterStaticEntry_Object = MibTableRow
igmpSnoopRouterStaticEntry = _IgmpSnoopRouterStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 9, 1)
)
igmpSnoopRouterStaticEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "igmpSnoopRouterStaticVlanIndex"),
)
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticEntry.setStatus("current")
_IgmpSnoopRouterStaticVlanIndex_Type = Unsigned32
_IgmpSnoopRouterStaticVlanIndex_Object = MibTableColumn
igmpSnoopRouterStaticVlanIndex = _IgmpSnoopRouterStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 9, 1, 1),
    _IgmpSnoopRouterStaticVlanIndex_Type()
)
igmpSnoopRouterStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticVlanIndex.setStatus("current")
_IgmpSnoopRouterStaticPorts_Type = PortList
_IgmpSnoopRouterStaticPorts_Object = MibTableColumn
igmpSnoopRouterStaticPorts = _IgmpSnoopRouterStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 9, 1, 2),
    _IgmpSnoopRouterStaticPorts_Type()
)
igmpSnoopRouterStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticPorts.setStatus("current")
_IgmpSnoopRouterStaticStatus_Type = ValidStatus
_IgmpSnoopRouterStaticStatus_Object = MibTableColumn
igmpSnoopRouterStaticStatus = _IgmpSnoopRouterStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 9, 1, 3),
    _IgmpSnoopRouterStaticStatus_Type()
)
igmpSnoopRouterStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopRouterStaticStatus.setStatus("current")
_IgmpSnoopMulticastCurrentTable_Object = MibTable
igmpSnoopMulticastCurrentTable = _IgmpSnoopMulticastCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 10)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentTable.setStatus("current")
_IgmpSnoopMulticastCurrentEntry_Object = MibTableRow
igmpSnoopMulticastCurrentEntry = _IgmpSnoopMulticastCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 10, 1)
)
igmpSnoopMulticastCurrentEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "igmpSnoopMulticastCurrentVlanIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "igmpSnoopMulticastCurrentIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentEntry.setStatus("current")
_IgmpSnoopMulticastCurrentVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastCurrentVlanIndex_Object = MibTableColumn
igmpSnoopMulticastCurrentVlanIndex = _IgmpSnoopMulticastCurrentVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 10, 1, 1),
    _IgmpSnoopMulticastCurrentVlanIndex_Type()
)
igmpSnoopMulticastCurrentVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentVlanIndex.setStatus("current")
_IgmpSnoopMulticastCurrentIpAddress_Type = IpAddress
_IgmpSnoopMulticastCurrentIpAddress_Object = MibTableColumn
igmpSnoopMulticastCurrentIpAddress = _IgmpSnoopMulticastCurrentIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 10, 1, 2),
    _IgmpSnoopMulticastCurrentIpAddress_Type()
)
igmpSnoopMulticastCurrentIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentIpAddress.setStatus("current")
_IgmpSnoopMulticastCurrentPorts_Type = PortList
_IgmpSnoopMulticastCurrentPorts_Object = MibTableColumn
igmpSnoopMulticastCurrentPorts = _IgmpSnoopMulticastCurrentPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 10, 1, 3),
    _IgmpSnoopMulticastCurrentPorts_Type()
)
igmpSnoopMulticastCurrentPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentPorts.setStatus("current")
_IgmpSnoopMulticastCurrentStatus_Type = PortList
_IgmpSnoopMulticastCurrentStatus_Object = MibTableColumn
igmpSnoopMulticastCurrentStatus = _IgmpSnoopMulticastCurrentStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 10, 1, 4),
    _IgmpSnoopMulticastCurrentStatus_Type()
)
igmpSnoopMulticastCurrentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSnoopMulticastCurrentStatus.setStatus("current")
_IgmpSnoopMulticastStaticTable_Object = MibTable
igmpSnoopMulticastStaticTable = _IgmpSnoopMulticastStaticTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 11)
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticTable.setStatus("current")
_IgmpSnoopMulticastStaticEntry_Object = MibTableRow
igmpSnoopMulticastStaticEntry = _IgmpSnoopMulticastStaticEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 11, 1)
)
igmpSnoopMulticastStaticEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "igmpSnoopMulticastStaticVlanIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "igmpSnoopMulticastStaticIpAddress"),
)
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticEntry.setStatus("current")
_IgmpSnoopMulticastStaticVlanIndex_Type = Unsigned32
_IgmpSnoopMulticastStaticVlanIndex_Object = MibTableColumn
igmpSnoopMulticastStaticVlanIndex = _IgmpSnoopMulticastStaticVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 11, 1, 1),
    _IgmpSnoopMulticastStaticVlanIndex_Type()
)
igmpSnoopMulticastStaticVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticVlanIndex.setStatus("current")
_IgmpSnoopMulticastStaticIpAddress_Type = IpAddress
_IgmpSnoopMulticastStaticIpAddress_Object = MibTableColumn
igmpSnoopMulticastStaticIpAddress = _IgmpSnoopMulticastStaticIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 11, 1, 2),
    _IgmpSnoopMulticastStaticIpAddress_Type()
)
igmpSnoopMulticastStaticIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticIpAddress.setStatus("current")
_IgmpSnoopMulticastStaticPorts_Type = PortList
_IgmpSnoopMulticastStaticPorts_Object = MibTableColumn
igmpSnoopMulticastStaticPorts = _IgmpSnoopMulticastStaticPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 11, 1, 3),
    _IgmpSnoopMulticastStaticPorts_Type()
)
igmpSnoopMulticastStaticPorts.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticPorts.setStatus("current")
_IgmpSnoopMulticastStaticStatus_Type = ValidStatus
_IgmpSnoopMulticastStaticStatus_Object = MibTableColumn
igmpSnoopMulticastStaticStatus = _IgmpSnoopMulticastStaticStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 9, 11, 1, 4),
    _IgmpSnoopMulticastStaticStatus_Type()
)
igmpSnoopMulticastStaticStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    igmpSnoopMulticastStaticStatus.setStatus("current")
_IpMgt_ObjectIdentity = ObjectIdentity
ipMgt = _IpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10)
)
_NetDefaultGateway_Type = IpAddress
_NetDefaultGateway_Object = MibScalar
netDefaultGateway = _NetDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 2),
    _NetDefaultGateway_Type()
)
netDefaultGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netDefaultGateway.setStatus("current")
_IpHttpState_Type = EnabledStatus
_IpHttpState_Object = MibScalar
ipHttpState = _IpHttpState_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 5),
    _IpDhcpRestart_Type()
)
ipDhcpRestart.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipDhcpRestart.setStatus("current")
_IpHttpsState_Type = EnabledStatus
_IpHttpsState_Object = MibScalar
ipHttpsState = _IpHttpsState_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 6),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 7),
    _IpHttpsPort_Type()
)
ipHttpsPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipHttpsPort.setStatus("current")
_IPAddrTable_Object = MibTable
iPAddrTable = _IPAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 16)
)
if mibBuilder.loadTexts:
    iPAddrTable.setStatus("current")
_IPAddrEntry_Object = MibTableRow
iPAddrEntry = _IPAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 16, 1)
)
iPAddrEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "iPAddrIPAddress"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "iPAddrSubnetMask"),
)
if mibBuilder.loadTexts:
    iPAddrEntry.setStatus("current")
_IPAddrIPAddress_Type = IpAddress
_IPAddrIPAddress_Object = MibTableColumn
iPAddrIPAddress = _IPAddrIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 16, 1, 1),
    _IPAddrIPAddress_Type()
)
iPAddrIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iPAddrIPAddress.setStatus("current")
_IPAddrSubnetMask_Type = IpAddress
_IPAddrSubnetMask_Object = MibTableColumn
iPAddrSubnetMask = _IPAddrSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 16, 1, 2),
    _IPAddrSubnetMask_Type()
)
iPAddrSubnetMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    iPAddrSubnetMask.setStatus("current")
_IPAddrIfIndex_Type = Integer32
_IPAddrIfIndex_Object = MibTableColumn
iPAddrIfIndex = _IPAddrIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 16, 1, 3),
    _IPAddrIfIndex_Type()
)
iPAddrIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPAddrIfIndex.setStatus("current")


class _IPAddrPrimaryInterface_Type(Integer32):
    """Custom type iPAddrPrimaryInterface based on Integer32"""
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


_IPAddrPrimaryInterface_Type.__name__ = "Integer32"
_IPAddrPrimaryInterface_Object = MibTableColumn
iPAddrPrimaryInterface = _IPAddrPrimaryInterface_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 16, 1, 4),
    _IPAddrPrimaryInterface_Type()
)
iPAddrPrimaryInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPAddrPrimaryInterface.setStatus("current")


class _IPAddrUnnumbered_Type(Integer32):
    """Custom type iPAddrUnnumbered based on Integer32"""
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


_IPAddrUnnumbered_Type.__name__ = "Integer32"
_IPAddrUnnumbered_Object = MibTableColumn
iPAddrUnnumbered = _IPAddrUnnumbered_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 16, 1, 5),
    _IPAddrUnnumbered_Type()
)
iPAddrUnnumbered.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    iPAddrUnnumbered.setStatus("current")
_IPAddrStatus_Type = RowStatus
_IPAddrStatus_Object = MibTableColumn
iPAddrStatus = _IPAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 10, 16, 1, 6),
    _IPAddrStatus_Type()
)
iPAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    iPAddrStatus.setStatus("current")
_BcastStormMgt_ObjectIdentity = ObjectIdentity
bcastStormMgt = _BcastStormMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 11)
)
_BcastStormTable_Object = MibTable
bcastStormTable = _BcastStormTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 11, 1)
)
if mibBuilder.loadTexts:
    bcastStormTable.setStatus("current")
_BcastStormEntry_Object = MibTableRow
bcastStormEntry = _BcastStormEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 11, 1, 1)
)
bcastStormEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "bcastStormIfIndex"),
)
if mibBuilder.loadTexts:
    bcastStormEntry.setStatus("current")
_BcastStormIfIndex_Type = Integer32
_BcastStormIfIndex_Object = MibTableColumn
bcastStormIfIndex = _BcastStormIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 11, 1, 1, 1),
    _BcastStormIfIndex_Type()
)
bcastStormIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    bcastStormIfIndex.setStatus("current")
_BcastStormStatus_Type = EnabledStatus
_BcastStormStatus_Object = MibTableColumn
bcastStormStatus = _BcastStormStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 11, 1, 1, 2),
    _BcastStormStatus_Type()
)
bcastStormStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormStatus.setStatus("current")
_BcastStormPktRate_Type = Integer32
_BcastStormPktRate_Object = MibTableColumn
bcastStormPktRate = _BcastStormPktRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 11, 1, 1, 4),
    _BcastStormPktRate_Type()
)
bcastStormPktRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bcastStormPktRate.setStatus("current")
_VlanMgt_ObjectIdentity = ObjectIdentity
vlanMgt = _VlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 12)
)
_VlanTable_Object = MibTable
vlanTable = _VlanTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 12, 1)
)
if mibBuilder.loadTexts:
    vlanTable.setStatus("current")
_VlanEntry_Object = MibTableRow
vlanEntry = _VlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 12, 1, 1)
)
vlanEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "vlanIndex"),
)
if mibBuilder.loadTexts:
    vlanEntry.setStatus("current")
_VlanIndex_Type = Unsigned32
_VlanIndex_Object = MibTableColumn
vlanIndex = _VlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 12, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 12, 1, 1, 2),
    _VlanAddressMethod_Type()
)
vlanAddressMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanAddressMethod.setStatus("current")
_VlanPortTable_Object = MibTable
vlanPortTable = _VlanPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 12, 2)
)
if mibBuilder.loadTexts:
    vlanPortTable.setStatus("current")
_VlanPortEntry_Object = MibTableRow
vlanPortEntry = _VlanPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 12, 2, 1)
)
vlanPortEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "vlanPortIndex"),
)
if mibBuilder.loadTexts:
    vlanPortEntry.setStatus("current")
_VlanPortIndex_Type = Integer32
_VlanPortIndex_Object = MibTableColumn
vlanPortIndex = _VlanPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 12, 2, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 12, 2, 1, 2),
    _VlanPortMode_Type()
)
vlanPortMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    vlanPortMode.setStatus("current")
_PriorityMgt_ObjectIdentity = ObjectIdentity
priorityMgt = _PriorityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13)
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 1),
    _PrioIpPrecDscpStatus_Type()
)
prioIpPrecDscpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecDscpStatus.setStatus("current")
_PrioIpPrecTable_Object = MibTable
prioIpPrecTable = _PrioIpPrecTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 2)
)
if mibBuilder.loadTexts:
    prioIpPrecTable.setStatus("current")
_PrioIpPrecEntry_Object = MibTableRow
prioIpPrecEntry = _PrioIpPrecEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 2, 1)
)
prioIpPrecEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "prioIpPrecPort"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "prioIpPrecValue"),
)
if mibBuilder.loadTexts:
    prioIpPrecEntry.setStatus("current")
_PrioIpPrecPort_Type = Integer32
_PrioIpPrecPort_Object = MibTableColumn
prioIpPrecPort = _PrioIpPrecPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 2, 1, 2),
    _PrioIpPrecPort_Type()
)
prioIpPrecPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPrecPort.setStatus("current")


class _PrioIpPrecValue_Type(Integer32):
    """Custom type prioIpPrecValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpPrecValue_Type.__name__ = "Integer32"
_PrioIpPrecValue_Object = MibTableColumn
prioIpPrecValue = _PrioIpPrecValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 2, 1, 3),
    _PrioIpPrecValue_Type()
)
prioIpPrecValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPrecValue.setStatus("current")


class _PrioIpPrecCos_Type(Integer32):
    """Custom type prioIpPrecCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpPrecCos_Type.__name__ = "Integer32"
_PrioIpPrecCos_Object = MibTableColumn
prioIpPrecCos = _PrioIpPrecCos_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 2, 1, 4),
    _PrioIpPrecCos_Type()
)
prioIpPrecCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecCos.setStatus("current")
_PrioIpPrecRestoreDefault_Type = Integer32
_PrioIpPrecRestoreDefault_Object = MibScalar
prioIpPrecRestoreDefault = _PrioIpPrecRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 3),
    _PrioIpPrecRestoreDefault_Type()
)
prioIpPrecRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPrecRestoreDefault.setStatus("current")
_PrioIpDscpTable_Object = MibTable
prioIpDscpTable = _PrioIpDscpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 4)
)
if mibBuilder.loadTexts:
    prioIpDscpTable.setStatus("current")
_PrioIpDscpEntry_Object = MibTableRow
prioIpDscpEntry = _PrioIpDscpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 4, 1)
)
prioIpDscpEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "prioIpDscpPort"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "prioIpDscpValue"),
)
if mibBuilder.loadTexts:
    prioIpDscpEntry.setStatus("current")
_PrioIpDscpPort_Type = Integer32
_PrioIpDscpPort_Object = MibTableColumn
prioIpDscpPort = _PrioIpDscpPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 4, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 4, 1, 3),
    _PrioIpDscpCos_Type()
)
prioIpDscpCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpCos.setStatus("current")
_PrioIpDscpRestoreDefault_Type = Integer32
_PrioIpDscpRestoreDefault_Object = MibScalar
prioIpDscpRestoreDefault = _PrioIpDscpRestoreDefault_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 5),
    _PrioIpDscpRestoreDefault_Type()
)
prioIpDscpRestoreDefault.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpDscpRestoreDefault.setStatus("current")
_PrioIpPortEnableStatus_Type = EnabledStatus
_PrioIpPortEnableStatus_Object = MibScalar
prioIpPortEnableStatus = _PrioIpPortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 6),
    _PrioIpPortEnableStatus_Type()
)
prioIpPortEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioIpPortEnableStatus.setStatus("current")
_PrioIpPortTable_Object = MibTable
prioIpPortTable = _PrioIpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 7)
)
if mibBuilder.loadTexts:
    prioIpPortTable.setStatus("current")
_PrioIpPortEntry_Object = MibTableRow
prioIpPortEntry = _PrioIpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 7, 1)
)
prioIpPortEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "prioIpPortPhysPort"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "prioIpPortValue"),
)
if mibBuilder.loadTexts:
    prioIpPortEntry.setStatus("current")
_PrioIpPortPhysPort_Type = Integer32
_PrioIpPortPhysPort_Object = MibTableColumn
prioIpPortPhysPort = _PrioIpPortPhysPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 7, 1, 1),
    _PrioIpPortPhysPort_Type()
)
prioIpPortPhysPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPortPhysPort.setStatus("current")


class _PrioIpPortValue_Type(Integer32):
    """Custom type prioIpPortValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_PrioIpPortValue_Type.__name__ = "Integer32"
_PrioIpPortValue_Object = MibTableColumn
prioIpPortValue = _PrioIpPortValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 7, 1, 2),
    _PrioIpPortValue_Type()
)
prioIpPortValue.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioIpPortValue.setStatus("current")


class _PrioIpPortCos_Type(Integer32):
    """Custom type prioIpPortCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioIpPortCos_Type.__name__ = "Integer32"
_PrioIpPortCos_Object = MibTableColumn
prioIpPortCos = _PrioIpPortCos_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 7, 1, 3),
    _PrioIpPortCos_Type()
)
prioIpPortCos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioIpPortCos.setStatus("current")
_PrioIpPortStatus_Type = ValidStatus
_PrioIpPortStatus_Object = MibTableColumn
prioIpPortStatus = _PrioIpPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 7, 1, 4),
    _PrioIpPortStatus_Type()
)
prioIpPortStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioIpPortStatus.setStatus("current")
_PrioCopy_ObjectIdentity = ObjectIdentity
prioCopy = _PrioCopy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 8)
)
_PrioCopyIpPrec_Type = OctetString
_PrioCopyIpPrec_Object = MibScalar
prioCopyIpPrec = _PrioCopyIpPrec_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 8, 1),
    _PrioCopyIpPrec_Type()
)
prioCopyIpPrec.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpPrec.setStatus("current")
_PrioCopyIpDscp_Type = OctetString
_PrioCopyIpDscp_Object = MibScalar
prioCopyIpDscp = _PrioCopyIpDscp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 8, 2),
    _PrioCopyIpDscp_Type()
)
prioCopyIpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpDscp.setStatus("current")
_PrioCopyIpPort_Type = OctetString
_PrioCopyIpPort_Object = MibScalar
prioCopyIpPort = _PrioCopyIpPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 8, 3),
    _PrioCopyIpPort_Type()
)
prioCopyIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioCopyIpPort.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 10),
    _PrioQueueMode_Type()
)
prioQueueMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioQueueMode.setStatus("current")
_PrioWrrPortTable_Object = MibTable
prioWrrPortTable = _PrioWrrPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 12)
)
if mibBuilder.loadTexts:
    prioWrrPortTable.setStatus("current")
_PrioWrrPortEntry_Object = MibTableRow
prioWrrPortEntry = _PrioWrrPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 12, 1)
)
prioWrrPortEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "prioWrrPortIfIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "prioWrrPortTrafficClass"),
)
if mibBuilder.loadTexts:
    prioWrrPortEntry.setStatus("current")
_PrioWrrPortIfIndex_Type = Integer32
_PrioWrrPortIfIndex_Object = MibTableColumn
prioWrrPortIfIndex = _PrioWrrPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 12, 1, 1),
    _PrioWrrPortIfIndex_Type()
)
prioWrrPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioWrrPortIfIndex.setStatus("current")


class _PrioWrrPortTrafficClass_Type(Integer32):
    """Custom type prioWrrPortTrafficClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioWrrPortTrafficClass_Type.__name__ = "Integer32"
_PrioWrrPortTrafficClass_Object = MibTableColumn
prioWrrPortTrafficClass = _PrioWrrPortTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 12, 1, 2),
    _PrioWrrPortTrafficClass_Type()
)
prioWrrPortTrafficClass.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioWrrPortTrafficClass.setStatus("current")


class _PrioWrrPortWeight_Type(Integer32):
    """Custom type prioWrrPortWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_PrioWrrPortWeight_Type.__name__ = "Integer32"
_PrioWrrPortWeight_Object = MibTableColumn
prioWrrPortWeight = _PrioWrrPortWeight_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 13, 12, 1, 3),
    _PrioWrrPortWeight_Type()
)
prioWrrPortWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    prioWrrPortWeight.setStatus("current")
_TrapDestMgt_ObjectIdentity = ObjectIdentity
trapDestMgt = _TrapDestMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14)
)
_TrapDestTable_Object = MibTable
trapDestTable = _TrapDestTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14, 1)
)
if mibBuilder.loadTexts:
    trapDestTable.setStatus("current")
_TrapDestEntry_Object = MibTableRow
trapDestEntry = _TrapDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14, 1, 1)
)
trapDestEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "trapDestAddress"),
)
if mibBuilder.loadTexts:
    trapDestEntry.setStatus("current")
_TrapDestAddress_Type = IpAddress
_TrapDestAddress_Object = MibTableColumn
trapDestAddress = _TrapDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14, 1, 1, 1),
    _TrapDestAddress_Type()
)
trapDestAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    trapDestAddress.setStatus("current")


class _TrapDestCommunity_Type(DisplayString):
    """Custom type trapDestCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TrapDestCommunity_Type.__name__ = "DisplayString"
_TrapDestCommunity_Object = MibTableColumn
trapDestCommunity = _TrapDestCommunity_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14, 1, 1, 2),
    _TrapDestCommunity_Type()
)
trapDestCommunity.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestCommunity.setStatus("current")
_TrapDestStatus_Type = ValidStatus
_TrapDestStatus_Object = MibTableColumn
trapDestStatus = _TrapDestStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14, 1, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14, 1, 1, 5),
    _TrapDestUdpPort_Type()
)
trapDestUdpPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    trapDestUdpPort.setStatus("current")
_TrapVar_ObjectIdentity = ObjectIdentity
trapVar = _TrapVar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14, 2)
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14, 2, 6),
    _TrapIpFilterRejectMode_Type()
)
trapIpFilterRejectMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIpFilterRejectMode.setStatus("current")
_TrapIpFilterRejectIp_Type = Integer32
_TrapIpFilterRejectIp_Object = MibScalar
trapIpFilterRejectIp = _TrapIpFilterRejectIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 14, 2, 7),
    _TrapIpFilterRejectIp_Type()
)
trapIpFilterRejectIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    trapIpFilterRejectIp.setStatus("current")
_QosMgt_ObjectIdentity = ObjectIdentity
qosMgt = _QosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16)
)
_RateLimitMgt_ObjectIdentity = ObjectIdentity
rateLimitMgt = _RateLimitMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 1)
)
_RateLimitPortTable_Object = MibTable
rateLimitPortTable = _RateLimitPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 1, 2)
)
if mibBuilder.loadTexts:
    rateLimitPortTable.setStatus("current")
_RateLimitPortEntry_Object = MibTableRow
rateLimitPortEntry = _RateLimitPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 1, 2, 1)
)
rateLimitPortEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "rlPortIndex"),
)
if mibBuilder.loadTexts:
    rateLimitPortEntry.setStatus("current")
_RlPortIndex_Type = Integer32
_RlPortIndex_Object = MibTableColumn
rlPortIndex = _RlPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 1, 2, 1, 1),
    _RlPortIndex_Type()
)
rlPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rlPortIndex.setStatus("current")
_RlPortInputLimit_Type = Integer32
_RlPortInputLimit_Object = MibTableColumn
rlPortInputLimit = _RlPortInputLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 1, 2, 1, 2),
    _RlPortInputLimit_Type()
)
rlPortInputLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputLimit.setStatus("current")
_RlPortOutputLimit_Type = Integer32
_RlPortOutputLimit_Object = MibTableColumn
rlPortOutputLimit = _RlPortOutputLimit_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 1, 2, 1, 3),
    _RlPortOutputLimit_Type()
)
rlPortOutputLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputLimit.setStatus("current")
_RlPortInputStatus_Type = EnabledStatus
_RlPortInputStatus_Object = MibTableColumn
rlPortInputStatus = _RlPortInputStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 1, 2, 1, 6),
    _RlPortInputStatus_Type()
)
rlPortInputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortInputStatus.setStatus("current")
_RlPortOutputStatus_Type = EnabledStatus
_RlPortOutputStatus_Object = MibTableColumn
rlPortOutputStatus = _RlPortOutputStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 1, 2, 1, 7),
    _RlPortOutputStatus_Type()
)
rlPortOutputStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rlPortOutputStatus.setStatus("current")
_MarkerMgt_ObjectIdentity = ObjectIdentity
markerMgt = _MarkerMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 2)
)
_MarkerTable_Object = MibTable
markerTable = _MarkerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 2, 1)
)
if mibBuilder.loadTexts:
    markerTable.setStatus("current")
_MarkerEntry_Object = MibTableRow
markerEntry = _MarkerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 2, 1, 1)
)
markerEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "markerIfIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "markerAclName"),
)
if mibBuilder.loadTexts:
    markerEntry.setStatus("current")
_MarkerIfIndex_Type = Integer32
_MarkerIfIndex_Object = MibTableColumn
markerIfIndex = _MarkerIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 2, 1, 1, 1),
    _MarkerIfIndex_Type()
)
markerIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    markerIfIndex.setStatus("current")


class _MarkerAclName_Type(DisplayString):
    """Custom type markerAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_MarkerAclName_Type.__name__ = "DisplayString"
_MarkerAclName_Object = MibTableColumn
markerAclName = _MarkerAclName_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 2, 1, 1, 2),
    _MarkerAclName_Type()
)
markerAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    markerAclName.setStatus("current")


class _MarkerActionBitList_Type(Bits):
    """Custom type markerActionBitList based on Bits"""
    namedValues = NamedValues(
        *(("dscp", 0),
          ("precedence", 1),
          ("priority", 2))
    )

_MarkerActionBitList_Type.__name__ = "Bits"
_MarkerActionBitList_Object = MibTableColumn
markerActionBitList = _MarkerActionBitList_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 2, 1, 1, 3),
    _MarkerActionBitList_Type()
)
markerActionBitList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markerActionBitList.setStatus("current")


class _MarkerDscp_Type(Integer32):
    """Custom type markerDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_MarkerDscp_Type.__name__ = "Integer32"
_MarkerDscp_Object = MibTableColumn
markerDscp = _MarkerDscp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 2, 1, 1, 4),
    _MarkerDscp_Type()
)
markerDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markerDscp.setStatus("current")


class _MarkerPrecedence_Type(Integer32):
    """Custom type markerPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MarkerPrecedence_Type.__name__ = "Integer32"
_MarkerPrecedence_Object = MibTableColumn
markerPrecedence = _MarkerPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 2, 1, 1, 5),
    _MarkerPrecedence_Type()
)
markerPrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markerPrecedence.setStatus("current")


class _MarkerPriority_Type(Integer32):
    """Custom type markerPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_MarkerPriority_Type.__name__ = "Integer32"
_MarkerPriority_Object = MibTableColumn
markerPriority = _MarkerPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 2, 1, 1, 6),
    _MarkerPriority_Type()
)
markerPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markerPriority.setStatus("current")
_MarkerStatus_Type = RowStatus
_MarkerStatus_Object = MibTableColumn
markerStatus = _MarkerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 2, 1, 1, 7),
    _MarkerStatus_Type()
)
markerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    markerStatus.setStatus("current")
_CosMgt_ObjectIdentity = ObjectIdentity
cosMgt = _CosMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 3)
)
_PrioAclToCosMappingTable_Object = MibTable
prioAclToCosMappingTable = _PrioAclToCosMappingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 3, 1)
)
if mibBuilder.loadTexts:
    prioAclToCosMappingTable.setStatus("current")
_PrioAclToCosMappingEntry_Object = MibTableRow
prioAclToCosMappingEntry = _PrioAclToCosMappingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 3, 1, 1)
)
prioAclToCosMappingEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "prioAclToCosMappingIfIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "prioAclToCosMappingAclName"),
)
if mibBuilder.loadTexts:
    prioAclToCosMappingEntry.setStatus("current")
_PrioAclToCosMappingIfIndex_Type = Integer32
_PrioAclToCosMappingIfIndex_Object = MibTableColumn
prioAclToCosMappingIfIndex = _PrioAclToCosMappingIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 3, 1, 1, 1),
    _PrioAclToCosMappingIfIndex_Type()
)
prioAclToCosMappingIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioAclToCosMappingIfIndex.setStatus("current")


class _PrioAclToCosMappingAclName_Type(DisplayString):
    """Custom type prioAclToCosMappingAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_PrioAclToCosMappingAclName_Type.__name__ = "DisplayString"
_PrioAclToCosMappingAclName_Object = MibTableColumn
prioAclToCosMappingAclName = _PrioAclToCosMappingAclName_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 3, 1, 1, 2),
    _PrioAclToCosMappingAclName_Type()
)
prioAclToCosMappingAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    prioAclToCosMappingAclName.setStatus("current")


class _PrioAclToCosMappingCosValue_Type(Integer32):
    """Custom type prioAclToCosMappingCosValue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_PrioAclToCosMappingCosValue_Type.__name__ = "Integer32"
_PrioAclToCosMappingCosValue_Object = MibTableColumn
prioAclToCosMappingCosValue = _PrioAclToCosMappingCosValue_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 3, 1, 1, 3),
    _PrioAclToCosMappingCosValue_Type()
)
prioAclToCosMappingCosValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioAclToCosMappingCosValue.setStatus("current")
_PrioAclToCosMappingStatus_Type = RowStatus
_PrioAclToCosMappingStatus_Object = MibTableColumn
prioAclToCosMappingStatus = _PrioAclToCosMappingStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 16, 3, 1, 1, 4),
    _PrioAclToCosMappingStatus_Type()
)
prioAclToCosMappingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    prioAclToCosMappingStatus.setStatus("current")
_SecurityMgt_ObjectIdentity = ObjectIdentity
securityMgt = _SecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17)
)
_PrivateVlanMgt_ObjectIdentity = ObjectIdentity
privateVlanMgt = _PrivateVlanMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 1)
)
_PrivateVlanStatus_Type = EnabledStatus
_PrivateVlanStatus_Object = MibScalar
privateVlanStatus = _PrivateVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 1, 1),
    _PrivateVlanStatus_Type()
)
privateVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanStatus.setStatus("current")
_PrivateVlanUplinkPorts_Type = PortList
_PrivateVlanUplinkPorts_Object = MibScalar
privateVlanUplinkPorts = _PrivateVlanUplinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 1, 2),
    _PrivateVlanUplinkPorts_Type()
)
privateVlanUplinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanUplinkPorts.setStatus("current")
_PrivateVlanDownlinkPorts_Type = PortList
_PrivateVlanDownlinkPorts_Object = MibScalar
privateVlanDownlinkPorts = _PrivateVlanDownlinkPorts_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 1, 3),
    _PrivateVlanDownlinkPorts_Type()
)
privateVlanDownlinkPorts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    privateVlanDownlinkPorts.setStatus("current")
_PortSecurityMgt_ObjectIdentity = ObjectIdentity
portSecurityMgt = _PortSecurityMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 2)
)
_PortSecPortTable_Object = MibTable
portSecPortTable = _PortSecPortTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 2, 1)
)
if mibBuilder.loadTexts:
    portSecPortTable.setStatus("current")
_PortSecPortEntry_Object = MibTableRow
portSecPortEntry = _PortSecPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 2, 1, 1)
)
portSecPortEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "portSecPortIndex"),
)
if mibBuilder.loadTexts:
    portSecPortEntry.setStatus("current")
_PortSecPortIndex_Type = Integer32
_PortSecPortIndex_Object = MibTableColumn
portSecPortIndex = _PortSecPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 2, 1, 1, 1),
    _PortSecPortIndex_Type()
)
portSecPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portSecPortIndex.setStatus("current")
_PortSecPortStatus_Type = EnabledStatus
_PortSecPortStatus_Object = MibTableColumn
portSecPortStatus = _PortSecPortStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 2, 1, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 2, 1, 1, 4),
    _PortSecMaxMacCount_Type()
)
portSecMaxMacCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    portSecMaxMacCount.setStatus("current")
_RadiusMgt_ObjectIdentity = ObjectIdentity
radiusMgt = _RadiusMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4)
)
_RadiusServerAddress_Type = IpAddress
_RadiusServerAddress_Object = MibScalar
radiusServerAddress = _RadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 1),
    _RadiusServerAddress_Type()
)
radiusServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerAddress.setStatus("current")


class _RadiusServerPortNumber_Type(Integer32):
    """Custom type radiusServerPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RadiusServerPortNumber_Type.__name__ = "Integer32"
_RadiusServerPortNumber_Object = MibScalar
radiusServerPortNumber = _RadiusServerPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 5),
    _RadiusServerTimeout_Type()
)
radiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    radiusServerTimeout.setStatus("current")
_RadiusMultipleServerTable_Object = MibTable
radiusMultipleServerTable = _RadiusMultipleServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 7)
)
if mibBuilder.loadTexts:
    radiusMultipleServerTable.setStatus("current")
_RadiusMultipleServerEntry_Object = MibTableRow
radiusMultipleServerEntry = _RadiusMultipleServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 7, 1)
)
radiusMultipleServerEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "radiusMultipleServerIndex"),
)
if mibBuilder.loadTexts:
    radiusMultipleServerEntry.setStatus("current")
_RadiusMultipleServerIndex_Type = Integer32
_RadiusMultipleServerIndex_Object = MibTableColumn
radiusMultipleServerIndex = _RadiusMultipleServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 7, 1, 1),
    _RadiusMultipleServerIndex_Type()
)
radiusMultipleServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    radiusMultipleServerIndex.setStatus("current")
_RadiusMultipleServerAddress_Type = IpAddress
_RadiusMultipleServerAddress_Object = MibTableColumn
radiusMultipleServerAddress = _RadiusMultipleServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 7, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 7, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 7, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 7, 1, 6),
    _RadiusMultipleServerTimeout_Type()
)
radiusMultipleServerTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerTimeout.setStatus("current")
_RadiusMultipleServerStatus_Type = ValidStatus
_RadiusMultipleServerStatus_Object = MibTableColumn
radiusMultipleServerStatus = _RadiusMultipleServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 4, 7, 1, 8),
    _RadiusMultipleServerStatus_Type()
)
radiusMultipleServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    radiusMultipleServerStatus.setStatus("current")
_TacacsMgt_ObjectIdentity = ObjectIdentity
tacacsMgt = _TacacsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 5)
)
_TacacsServerAddress_Type = IpAddress
_TacacsServerAddress_Object = MibScalar
tacacsServerAddress = _TacacsServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 5, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 5, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 5, 3),
    _TacacsServerKey_Type()
)
tacacsServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacacsServerKey.setStatus("current")
_SshMgt_ObjectIdentity = ObjectIdentity
sshMgt = _SshMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6)
)
_SshServerStatus_Type = EnabledStatus
_SshServerStatus_Object = MibScalar
sshServerStatus = _SshServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 1),
    _SshServerStatus_Type()
)
sshServerStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshServerStatus.setStatus("current")
_SshServerMajorVersion_Type = Integer32
_SshServerMajorVersion_Object = MibScalar
sshServerMajorVersion = _SshServerMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 2),
    _SshServerMajorVersion_Type()
)
sshServerMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshServerMajorVersion.setStatus("current")
_SshServerMinorVersion_Type = Integer32
_SshServerMinorVersion_Object = MibScalar
sshServerMinorVersion = _SshServerMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 4),
    _SshTimeout_Type()
)
sshTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshTimeout.setStatus("current")


class _SshAuthRetries_Type(Integer32):
    """Custom type sshAuthRetries based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_SshAuthRetries_Type.__name__ = "Integer32"
_SshAuthRetries_Object = MibScalar
sshAuthRetries = _SshAuthRetries_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 5),
    _SshAuthRetries_Type()
)
sshAuthRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshAuthRetries.setStatus("current")
_SshConnInfoTable_Object = MibTable
sshConnInfoTable = _SshConnInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 6)
)
if mibBuilder.loadTexts:
    sshConnInfoTable.setStatus("current")
_SshConnInfoEntry_Object = MibTableRow
sshConnInfoEntry = _SshConnInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 6, 1)
)
sshConnInfoEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "sshConnID"),
)
if mibBuilder.loadTexts:
    sshConnInfoEntry.setStatus("current")
_SshConnID_Type = Integer32
_SshConnID_Object = MibTableColumn
sshConnID = _SshConnID_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 6, 1, 1),
    _SshConnID_Type()
)
sshConnID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshConnID.setStatus("current")
_SshConnMajorVersion_Type = Integer32
_SshConnMajorVersion_Object = MibTableColumn
sshConnMajorVersion = _SshConnMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 6, 1, 2),
    _SshConnMajorVersion_Type()
)
sshConnMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshConnMajorVersion.setStatus("current")
_SshConnMinorVersion_Type = Integer32
_SshConnMinorVersion_Object = MibTableColumn
sshConnMinorVersion = _SshConnMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 6, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 6, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 6, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 6, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 6, 1, 8),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 7),
    _SshKeySize_Type()
)
sshKeySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshKeySize.setStatus("current")
_SshRsaHostKey1_Type = KeySegment
_SshRsaHostKey1_Object = MibScalar
sshRsaHostKey1 = _SshRsaHostKey1_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 8),
    _SshRsaHostKey1_Type()
)
sshRsaHostKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey1.setStatus("current")
_SshRsaHostKey2_Type = KeySegment
_SshRsaHostKey2_Object = MibScalar
sshRsaHostKey2 = _SshRsaHostKey2_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 9),
    _SshRsaHostKey2_Type()
)
sshRsaHostKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey2.setStatus("current")
_SshRsaHostKey3_Type = KeySegment
_SshRsaHostKey3_Object = MibScalar
sshRsaHostKey3 = _SshRsaHostKey3_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 10),
    _SshRsaHostKey3_Type()
)
sshRsaHostKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey3.setStatus("current")
_SshRsaHostKey4_Type = KeySegment
_SshRsaHostKey4_Object = MibScalar
sshRsaHostKey4 = _SshRsaHostKey4_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 11),
    _SshRsaHostKey4_Type()
)
sshRsaHostKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey4.setStatus("current")
_SshRsaHostKey5_Type = KeySegment
_SshRsaHostKey5_Object = MibScalar
sshRsaHostKey5 = _SshRsaHostKey5_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 12),
    _SshRsaHostKey5_Type()
)
sshRsaHostKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey5.setStatus("current")
_SshRsaHostKey6_Type = KeySegment
_SshRsaHostKey6_Object = MibScalar
sshRsaHostKey6 = _SshRsaHostKey6_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 13),
    _SshRsaHostKey6_Type()
)
sshRsaHostKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey6.setStatus("current")
_SshRsaHostKey7_Type = KeySegment
_SshRsaHostKey7_Object = MibScalar
sshRsaHostKey7 = _SshRsaHostKey7_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 14),
    _SshRsaHostKey7_Type()
)
sshRsaHostKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey7.setStatus("current")
_SshRsaHostKey8_Type = KeySegment
_SshRsaHostKey8_Object = MibScalar
sshRsaHostKey8 = _SshRsaHostKey8_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 15),
    _SshRsaHostKey8_Type()
)
sshRsaHostKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshRsaHostKey8.setStatus("current")
_SshDsaHostKey1_Type = KeySegment
_SshDsaHostKey1_Object = MibScalar
sshDsaHostKey1 = _SshDsaHostKey1_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 16),
    _SshDsaHostKey1_Type()
)
sshDsaHostKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey1.setStatus("current")
_SshDsaHostKey2_Type = KeySegment
_SshDsaHostKey2_Object = MibScalar
sshDsaHostKey2 = _SshDsaHostKey2_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 17),
    _SshDsaHostKey2_Type()
)
sshDsaHostKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey2.setStatus("current")
_SshDsaHostKey3_Type = KeySegment
_SshDsaHostKey3_Object = MibScalar
sshDsaHostKey3 = _SshDsaHostKey3_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 18),
    _SshDsaHostKey3_Type()
)
sshDsaHostKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey3.setStatus("current")
_SshDsaHostKey4_Type = KeySegment
_SshDsaHostKey4_Object = MibScalar
sshDsaHostKey4 = _SshDsaHostKey4_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 19),
    _SshDsaHostKey4_Type()
)
sshDsaHostKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey4.setStatus("current")
_SshDsaHostKey5_Type = KeySegment
_SshDsaHostKey5_Object = MibScalar
sshDsaHostKey5 = _SshDsaHostKey5_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 20),
    _SshDsaHostKey5_Type()
)
sshDsaHostKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey5.setStatus("current")
_SshDsaHostKey6_Type = KeySegment
_SshDsaHostKey6_Object = MibScalar
sshDsaHostKey6 = _SshDsaHostKey6_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 21),
    _SshDsaHostKey6_Type()
)
sshDsaHostKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey6.setStatus("current")
_SshDsaHostKey7_Type = KeySegment
_SshDsaHostKey7_Object = MibScalar
sshDsaHostKey7 = _SshDsaHostKey7_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 22),
    _SshDsaHostKey7_Type()
)
sshDsaHostKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshDsaHostKey7.setStatus("current")
_SshDsaHostKey8_Type = KeySegment
_SshDsaHostKey8_Object = MibScalar
sshDsaHostKey8 = _SshDsaHostKey8_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 23),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 24),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 25),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 26),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 27),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 28),
    _SshHostKeyDelAction_Type()
)
sshHostKeyDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshHostKeyDelAction.setStatus("current")
_SshUserTable_Object = MibTable
sshUserTable = _SshUserTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29)
)
if mibBuilder.loadTexts:
    sshUserTable.setStatus("current")
_SshUserEntry_Object = MibTableRow
sshUserEntry = _SshUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1)
)
sshUserEntry.setIndexNames(
    (1, "Hirschmann-GIGA-LION-24TP-MIB", "sshUserName"),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 1),
    _SshUserName_Type()
)
sshUserName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sshUserName.setStatus("current")
_SshUserRsaKey1_Type = KeySegment
_SshUserRsaKey1_Object = MibTableColumn
sshUserRsaKey1 = _SshUserRsaKey1_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 2),
    _SshUserRsaKey1_Type()
)
sshUserRsaKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey1.setStatus("current")
_SshUserRsaKey2_Type = KeySegment
_SshUserRsaKey2_Object = MibTableColumn
sshUserRsaKey2 = _SshUserRsaKey2_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 3),
    _SshUserRsaKey2_Type()
)
sshUserRsaKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey2.setStatus("current")
_SshUserRsaKey3_Type = KeySegment
_SshUserRsaKey3_Object = MibTableColumn
sshUserRsaKey3 = _SshUserRsaKey3_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 4),
    _SshUserRsaKey3_Type()
)
sshUserRsaKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey3.setStatus("current")
_SshUserRsaKey4_Type = KeySegment
_SshUserRsaKey4_Object = MibTableColumn
sshUserRsaKey4 = _SshUserRsaKey4_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 5),
    _SshUserRsaKey4_Type()
)
sshUserRsaKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey4.setStatus("current")
_SshUserRsaKey5_Type = KeySegment
_SshUserRsaKey5_Object = MibTableColumn
sshUserRsaKey5 = _SshUserRsaKey5_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 6),
    _SshUserRsaKey5_Type()
)
sshUserRsaKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey5.setStatus("current")
_SshUserRsaKey6_Type = KeySegment
_SshUserRsaKey6_Object = MibTableColumn
sshUserRsaKey6 = _SshUserRsaKey6_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 7),
    _SshUserRsaKey6_Type()
)
sshUserRsaKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey6.setStatus("current")
_SshUserRsaKey7_Type = KeySegment
_SshUserRsaKey7_Object = MibTableColumn
sshUserRsaKey7 = _SshUserRsaKey7_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 8),
    _SshUserRsaKey7_Type()
)
sshUserRsaKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey7.setStatus("current")
_SshUserRsaKey8_Type = KeySegment
_SshUserRsaKey8_Object = MibTableColumn
sshUserRsaKey8 = _SshUserRsaKey8_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 9),
    _SshUserRsaKey8_Type()
)
sshUserRsaKey8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserRsaKey8.setStatus("current")
_SshUserDsaKey1_Type = KeySegment
_SshUserDsaKey1_Object = MibTableColumn
sshUserDsaKey1 = _SshUserDsaKey1_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 10),
    _SshUserDsaKey1_Type()
)
sshUserDsaKey1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey1.setStatus("current")
_SshUserDsaKey2_Type = KeySegment
_SshUserDsaKey2_Object = MibTableColumn
sshUserDsaKey2 = _SshUserDsaKey2_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 11),
    _SshUserDsaKey2_Type()
)
sshUserDsaKey2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey2.setStatus("current")
_SshUserDsaKey3_Type = KeySegment
_SshUserDsaKey3_Object = MibTableColumn
sshUserDsaKey3 = _SshUserDsaKey3_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 12),
    _SshUserDsaKey3_Type()
)
sshUserDsaKey3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey3.setStatus("current")
_SshUserDsaKey4_Type = KeySegment
_SshUserDsaKey4_Object = MibTableColumn
sshUserDsaKey4 = _SshUserDsaKey4_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 13),
    _SshUserDsaKey4_Type()
)
sshUserDsaKey4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey4.setStatus("current")
_SshUserDsaKey5_Type = KeySegment
_SshUserDsaKey5_Object = MibTableColumn
sshUserDsaKey5 = _SshUserDsaKey5_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 14),
    _SshUserDsaKey5_Type()
)
sshUserDsaKey5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey5.setStatus("current")
_SshUserDsaKey6_Type = KeySegment
_SshUserDsaKey6_Object = MibTableColumn
sshUserDsaKey6 = _SshUserDsaKey6_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 15),
    _SshUserDsaKey6_Type()
)
sshUserDsaKey6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey6.setStatus("current")
_SshUserDsaKey7_Type = KeySegment
_SshUserDsaKey7_Object = MibTableColumn
sshUserDsaKey7 = _SshUserDsaKey7_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 16),
    _SshUserDsaKey7_Type()
)
sshUserDsaKey7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    sshUserDsaKey7.setStatus("current")
_SshUserDsaKey8_Type = KeySegment
_SshUserDsaKey8_Object = MibTableColumn
sshUserDsaKey8 = _SshUserDsaKey8_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 17),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 6, 29, 1, 18),
    _SshUserKeyDelAction_Type()
)
sshUserKeyDelAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sshUserKeyDelAction.setStatus("current")
_AclMgt_ObjectIdentity = ObjectIdentity
aclMgt = _AclMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7)
)
_AclIpAceTable_Object = MibTable
aclIpAceTable = _AclIpAceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1)
)
if mibBuilder.loadTexts:
    aclIpAceTable.setStatus("current")
_AclIpAceEntry_Object = MibTableRow
aclIpAceEntry = _AclIpAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1)
)
aclIpAceEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclIpAceName"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclIpAceIndex"),
)
if mibBuilder.loadTexts:
    aclIpAceEntry.setStatus("current")


class _AclIpAceName_Type(DisplayString):
    """Custom type aclIpAceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AclIpAceName_Type.__name__ = "DisplayString"
_AclIpAceName_Object = MibTableColumn
aclIpAceName = _AclIpAceName_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 1),
    _AclIpAceName_Type()
)
aclIpAceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIpAceName.setStatus("current")


class _AclIpAceIndex_Type(Integer32):
    """Custom type aclIpAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AclIpAceIndex_Type.__name__ = "Integer32"
_AclIpAceIndex_Object = MibTableColumn
aclIpAceIndex = _AclIpAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 2),
    _AclIpAceIndex_Type()
)
aclIpAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIpAceIndex.setStatus("current")


class _AclIpAcePrecedence_Type(Integer32):
    """Custom type aclIpAcePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AclIpAcePrecedence_Type.__name__ = "Integer32"
_AclIpAcePrecedence_Object = MibTableColumn
aclIpAcePrecedence = _AclIpAcePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 3),
    _AclIpAcePrecedence_Type()
)
aclIpAcePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIpAcePrecedence.setStatus("current")


class _AclIpAceAction_Type(Integer32):
    """Custom type aclIpAceAction based on Integer32"""
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


_AclIpAceAction_Type.__name__ = "Integer32"
_AclIpAceAction_Object = MibTableColumn
aclIpAceAction = _AclIpAceAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 4),
    _AclIpAceAction_Type()
)
aclIpAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceAction.setStatus("current")
_AclIpAceSourceIpAddr_Type = IpAddress
_AclIpAceSourceIpAddr_Object = MibTableColumn
aclIpAceSourceIpAddr = _AclIpAceSourceIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 5),
    _AclIpAceSourceIpAddr_Type()
)
aclIpAceSourceIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourceIpAddr.setStatus("current")
_AclIpAceSourceIpAddrBitmask_Type = IpAddress
_AclIpAceSourceIpAddrBitmask_Object = MibTableColumn
aclIpAceSourceIpAddrBitmask = _AclIpAceSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 6),
    _AclIpAceSourceIpAddrBitmask_Type()
)
aclIpAceSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourceIpAddrBitmask.setStatus("current")
_AclIpAceDestIpAddr_Type = IpAddress
_AclIpAceDestIpAddr_Object = MibTableColumn
aclIpAceDestIpAddr = _AclIpAceDestIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 7),
    _AclIpAceDestIpAddr_Type()
)
aclIpAceDestIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestIpAddr.setStatus("current")
_AclIpAceDestIpAddrBitmask_Type = IpAddress
_AclIpAceDestIpAddrBitmask_Object = MibTableColumn
aclIpAceDestIpAddrBitmask = _AclIpAceDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 8),
    _AclIpAceDestIpAddrBitmask_Type()
)
aclIpAceDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestIpAddrBitmask.setStatus("current")


class _AclIpAceProtocol_Type(Integer32):
    """Custom type aclIpAceProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_AclIpAceProtocol_Type.__name__ = "Integer32"
_AclIpAceProtocol_Object = MibTableColumn
aclIpAceProtocol = _AclIpAceProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 9),
    _AclIpAceProtocol_Type()
)
aclIpAceProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceProtocol.setStatus("current")


class _AclIpAcePrec_Type(Integer32):
    """Custom type aclIpAcePrec based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AclIpAcePrec_Type.__name__ = "Integer32"
_AclIpAcePrec_Object = MibTableColumn
aclIpAcePrec = _AclIpAcePrec_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 10),
    _AclIpAcePrec_Type()
)
aclIpAcePrec.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAcePrec.setStatus("current")


class _AclIpAceTos_Type(Integer32):
    """Custom type aclIpAceTos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclIpAceTos_Type.__name__ = "Integer32"
_AclIpAceTos_Object = MibTableColumn
aclIpAceTos = _AclIpAceTos_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 11),
    _AclIpAceTos_Type()
)
aclIpAceTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceTos.setStatus("current")


class _AclIpAceDscp_Type(Integer32):
    """Custom type aclIpAceDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_AclIpAceDscp_Type.__name__ = "Integer32"
_AclIpAceDscp_Object = MibTableColumn
aclIpAceDscp = _AclIpAceDscp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 12),
    _AclIpAceDscp_Type()
)
aclIpAceDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDscp.setStatus("current")


class _AclIpAceSourcePortOp_Type(Integer32):
    """Custom type aclIpAceSourcePortOp based on Integer32"""
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


_AclIpAceSourcePortOp_Type.__name__ = "Integer32"
_AclIpAceSourcePortOp_Object = MibTableColumn
aclIpAceSourcePortOp = _AclIpAceSourcePortOp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 13),
    _AclIpAceSourcePortOp_Type()
)
aclIpAceSourcePortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourcePortOp.setStatus("current")


class _AclIpAceMinSourcePort_Type(Integer32):
    """Custom type aclIpAceMinSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMinSourcePort_Type.__name__ = "Integer32"
_AclIpAceMinSourcePort_Object = MibTableColumn
aclIpAceMinSourcePort = _AclIpAceMinSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 14),
    _AclIpAceMinSourcePort_Type()
)
aclIpAceMinSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMinSourcePort.setStatus("current")


class _AclIpAceMaxSourcePort_Type(Integer32):
    """Custom type aclIpAceMaxSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMaxSourcePort_Type.__name__ = "Integer32"
_AclIpAceMaxSourcePort_Object = MibTableColumn
aclIpAceMaxSourcePort = _AclIpAceMaxSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 15),
    _AclIpAceMaxSourcePort_Type()
)
aclIpAceMaxSourcePort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMaxSourcePort.setStatus("current")


class _AclIpAceSourcePortBitmask_Type(Integer32):
    """Custom type aclIpAceSourcePortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceSourcePortBitmask_Type.__name__ = "Integer32"
_AclIpAceSourcePortBitmask_Object = MibTableColumn
aclIpAceSourcePortBitmask = _AclIpAceSourcePortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 16),
    _AclIpAceSourcePortBitmask_Type()
)
aclIpAceSourcePortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceSourcePortBitmask.setStatus("current")


class _AclIpAceDestPortOp_Type(Integer32):
    """Custom type aclIpAceDestPortOp based on Integer32"""
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


_AclIpAceDestPortOp_Type.__name__ = "Integer32"
_AclIpAceDestPortOp_Object = MibTableColumn
aclIpAceDestPortOp = _AclIpAceDestPortOp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 17),
    _AclIpAceDestPortOp_Type()
)
aclIpAceDestPortOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestPortOp.setStatus("current")


class _AclIpAceMinDestPort_Type(Integer32):
    """Custom type aclIpAceMinDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMinDestPort_Type.__name__ = "Integer32"
_AclIpAceMinDestPort_Object = MibTableColumn
aclIpAceMinDestPort = _AclIpAceMinDestPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 18),
    _AclIpAceMinDestPort_Type()
)
aclIpAceMinDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMinDestPort.setStatus("current")


class _AclIpAceMaxDestPort_Type(Integer32):
    """Custom type aclIpAceMaxDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceMaxDestPort_Type.__name__ = "Integer32"
_AclIpAceMaxDestPort_Object = MibTableColumn
aclIpAceMaxDestPort = _AclIpAceMaxDestPort_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 19),
    _AclIpAceMaxDestPort_Type()
)
aclIpAceMaxDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceMaxDestPort.setStatus("current")


class _AclIpAceDestPortBitmask_Type(Integer32):
    """Custom type aclIpAceDestPortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIpAceDestPortBitmask_Type.__name__ = "Integer32"
_AclIpAceDestPortBitmask_Object = MibTableColumn
aclIpAceDestPortBitmask = _AclIpAceDestPortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 20),
    _AclIpAceDestPortBitmask_Type()
)
aclIpAceDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceDestPortBitmask.setStatus("current")


class _AclIpAceControlCode_Type(Integer32):
    """Custom type aclIpAceControlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclIpAceControlCode_Type.__name__ = "Integer32"
_AclIpAceControlCode_Object = MibTableColumn
aclIpAceControlCode = _AclIpAceControlCode_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 21),
    _AclIpAceControlCode_Type()
)
aclIpAceControlCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceControlCode.setStatus("current")


class _AclIpAceControlCodeBitmask_Type(Integer32):
    """Custom type aclIpAceControlCodeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclIpAceControlCodeBitmask_Type.__name__ = "Integer32"
_AclIpAceControlCodeBitmask_Object = MibTableColumn
aclIpAceControlCodeBitmask = _AclIpAceControlCodeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 22),
    _AclIpAceControlCodeBitmask_Type()
)
aclIpAceControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceControlCodeBitmask.setStatus("current")
_AclIpAceStatus_Type = RowStatus
_AclIpAceStatus_Object = MibTableColumn
aclIpAceStatus = _AclIpAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 1, 1, 23),
    _AclIpAceStatus_Type()
)
aclIpAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIpAceStatus.setStatus("current")
_AclMacAceTable_Object = MibTable
aclMacAceTable = _AclMacAceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2)
)
if mibBuilder.loadTexts:
    aclMacAceTable.setStatus("current")
_AclMacAceEntry_Object = MibTableRow
aclMacAceEntry = _AclMacAceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1)
)
aclMacAceEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclMacAceName"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclMacAceIndex"),
)
if mibBuilder.loadTexts:
    aclMacAceEntry.setStatus("current")


class _AclMacAceName_Type(DisplayString):
    """Custom type aclMacAceName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AclMacAceName_Type.__name__ = "DisplayString"
_AclMacAceName_Object = MibTableColumn
aclMacAceName = _AclMacAceName_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 1),
    _AclMacAceName_Type()
)
aclMacAceName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclMacAceName.setStatus("current")


class _AclMacAceIndex_Type(Integer32):
    """Custom type aclMacAceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_AclMacAceIndex_Type.__name__ = "Integer32"
_AclMacAceIndex_Object = MibTableColumn
aclMacAceIndex = _AclMacAceIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 2),
    _AclMacAceIndex_Type()
)
aclMacAceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclMacAceIndex.setStatus("current")


class _AclMacAcePrecedence_Type(Integer32):
    """Custom type aclMacAcePrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32),
    )


_AclMacAcePrecedence_Type.__name__ = "Integer32"
_AclMacAcePrecedence_Object = MibTableColumn
aclMacAcePrecedence = _AclMacAcePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 3),
    _AclMacAcePrecedence_Type()
)
aclMacAcePrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMacAcePrecedence.setStatus("current")


class _AclMacAceAction_Type(Integer32):
    """Custom type aclMacAceAction based on Integer32"""
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


_AclMacAceAction_Type.__name__ = "Integer32"
_AclMacAceAction_Object = MibTableColumn
aclMacAceAction = _AclMacAceAction_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 4),
    _AclMacAceAction_Type()
)
aclMacAceAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceAction.setStatus("current")


class _AclMacAcePktformat_Type(Integer32):
    """Custom type aclMacAcePktformat based on Integer32"""
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


_AclMacAcePktformat_Type.__name__ = "Integer32"
_AclMacAcePktformat_Object = MibTableColumn
aclMacAcePktformat = _AclMacAcePktformat_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 5),
    _AclMacAcePktformat_Type()
)
aclMacAcePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAcePktformat.setStatus("current")


class _AclMacAceSourceMacAddr_Type(OctetString):
    """Custom type aclMacAceSourceMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AclMacAceSourceMacAddr_Type.__name__ = "OctetString"
_AclMacAceSourceMacAddr_Object = MibTableColumn
aclMacAceSourceMacAddr = _AclMacAceSourceMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 6),
    _AclMacAceSourceMacAddr_Type()
)
aclMacAceSourceMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceSourceMacAddr.setStatus("current")


class _AclMacAceSourceMacAddrBitmask_Type(OctetString):
    """Custom type aclMacAceSourceMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AclMacAceSourceMacAddrBitmask_Type.__name__ = "OctetString"
_AclMacAceSourceMacAddrBitmask_Object = MibTableColumn
aclMacAceSourceMacAddrBitmask = _AclMacAceSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 7),
    _AclMacAceSourceMacAddrBitmask_Type()
)
aclMacAceSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceSourceMacAddrBitmask.setStatus("current")


class _AclMacAceDestMacAddr_Type(OctetString):
    """Custom type aclMacAceDestMacAddr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AclMacAceDestMacAddr_Type.__name__ = "OctetString"
_AclMacAceDestMacAddr_Object = MibTableColumn
aclMacAceDestMacAddr = _AclMacAceDestMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 8),
    _AclMacAceDestMacAddr_Type()
)
aclMacAceDestMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceDestMacAddr.setStatus("current")


class _AclMacAceDestMacAddrBitmask_Type(OctetString):
    """Custom type aclMacAceDestMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AclMacAceDestMacAddrBitmask_Type.__name__ = "OctetString"
_AclMacAceDestMacAddrBitmask_Object = MibTableColumn
aclMacAceDestMacAddrBitmask = _AclMacAceDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 9),
    _AclMacAceDestMacAddrBitmask_Type()
)
aclMacAceDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceDestMacAddrBitmask.setStatus("current")


class _AclMacAceVidOp_Type(Integer32):
    """Custom type aclMacAceVidOp based on Integer32"""
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


_AclMacAceVidOp_Type.__name__ = "Integer32"
_AclMacAceVidOp_Object = MibTableColumn
aclMacAceVidOp = _AclMacAceVidOp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 10),
    _AclMacAceVidOp_Type()
)
aclMacAceVidOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceVidOp.setStatus("current")


class _AclMacAceMinVid_Type(Integer32):
    """Custom type aclMacAceMinVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclMacAceMinVid_Type.__name__ = "Integer32"
_AclMacAceMinVid_Object = MibTableColumn
aclMacAceMinVid = _AclMacAceMinVid_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 11),
    _AclMacAceMinVid_Type()
)
aclMacAceMinVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMinVid.setStatus("current")


class _AclMacAceVidBitmask_Type(Integer32):
    """Custom type aclMacAceVidBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclMacAceVidBitmask_Type.__name__ = "Integer32"
_AclMacAceVidBitmask_Object = MibTableColumn
aclMacAceVidBitmask = _AclMacAceVidBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 12),
    _AclMacAceVidBitmask_Type()
)
aclMacAceVidBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceVidBitmask.setStatus("current")


class _AclMacAceMaxVid_Type(Integer32):
    """Custom type aclMacAceMaxVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4093),
    )


_AclMacAceMaxVid_Type.__name__ = "Integer32"
_AclMacAceMaxVid_Object = MibTableColumn
aclMacAceMaxVid = _AclMacAceMaxVid_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 13),
    _AclMacAceMaxVid_Type()
)
aclMacAceMaxVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMaxVid.setStatus("current")


class _AclMacAceEtherTypeOp_Type(Integer32):
    """Custom type aclMacAceEtherTypeOp based on Integer32"""
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


_AclMacAceEtherTypeOp_Type.__name__ = "Integer32"
_AclMacAceEtherTypeOp_Object = MibTableColumn
aclMacAceEtherTypeOp = _AclMacAceEtherTypeOp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 14),
    _AclMacAceEtherTypeOp_Type()
)
aclMacAceEtherTypeOp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceEtherTypeOp.setStatus("current")


class _AclMacAceEtherTypeBitmask_Type(Integer32):
    """Custom type aclMacAceEtherTypeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclMacAceEtherTypeBitmask_Type.__name__ = "Integer32"
_AclMacAceEtherTypeBitmask_Object = MibTableColumn
aclMacAceEtherTypeBitmask = _AclMacAceEtherTypeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 15),
    _AclMacAceEtherTypeBitmask_Type()
)
aclMacAceEtherTypeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceEtherTypeBitmask.setStatus("current")


class _AclMacAceMinEtherType_Type(Integer32):
    """Custom type aclMacAceMinEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_AclMacAceMinEtherType_Type.__name__ = "Integer32"
_AclMacAceMinEtherType_Object = MibTableColumn
aclMacAceMinEtherType = _AclMacAceMinEtherType_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 16),
    _AclMacAceMinEtherType_Type()
)
aclMacAceMinEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMinEtherType.setStatus("current")


class _AclMacAceMaxEtherType_Type(Integer32):
    """Custom type aclMacAceMaxEtherType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1536, 65535),
    )


_AclMacAceMaxEtherType_Type.__name__ = "Integer32"
_AclMacAceMaxEtherType_Object = MibTableColumn
aclMacAceMaxEtherType = _AclMacAceMaxEtherType_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 17),
    _AclMacAceMaxEtherType_Type()
)
aclMacAceMaxEtherType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceMaxEtherType.setStatus("current")
_AclMacAceStatus_Type = RowStatus
_AclMacAceStatus_Object = MibTableColumn
aclMacAceStatus = _AclMacAceStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 2, 1, 18),
    _AclMacAceStatus_Type()
)
aclMacAceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclMacAceStatus.setStatus("current")
_AclAclGroupTable_Object = MibTable
aclAclGroupTable = _AclAclGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 3)
)
if mibBuilder.loadTexts:
    aclAclGroupTable.setStatus("current")
_AclAclGroupEntry_Object = MibTableRow
aclAclGroupEntry = _AclAclGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 3, 1)
)
aclAclGroupEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclAclGroupIfIndex"),
)
if mibBuilder.loadTexts:
    aclAclGroupEntry.setStatus("current")
_AclAclGroupIfIndex_Type = Integer32
_AclAclGroupIfIndex_Object = MibTableColumn
aclAclGroupIfIndex = _AclAclGroupIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 3, 1, 1),
    _AclAclGroupIfIndex_Type()
)
aclAclGroupIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclAclGroupIfIndex.setStatus("current")


class _AclAclGroupIngressIpAcl_Type(DisplayString):
    """Custom type aclAclGroupIngressIpAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupIngressIpAcl_Type.__name__ = "DisplayString"
_AclAclGroupIngressIpAcl_Object = MibTableColumn
aclAclGroupIngressIpAcl = _AclAclGroupIngressIpAcl_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 3, 1, 2),
    _AclAclGroupIngressIpAcl_Type()
)
aclAclGroupIngressIpAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupIngressIpAcl.setStatus("current")


class _AclAclGroupEgressIpAcl_Type(DisplayString):
    """Custom type aclAclGroupEgressIpAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupEgressIpAcl_Type.__name__ = "DisplayString"
_AclAclGroupEgressIpAcl_Object = MibTableColumn
aclAclGroupEgressIpAcl = _AclAclGroupEgressIpAcl_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 3, 1, 3),
    _AclAclGroupEgressIpAcl_Type()
)
aclAclGroupEgressIpAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupEgressIpAcl.setStatus("current")


class _AclAclGroupIngressMacAcl_Type(DisplayString):
    """Custom type aclAclGroupIngressMacAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupIngressMacAcl_Type.__name__ = "DisplayString"
_AclAclGroupIngressMacAcl_Object = MibTableColumn
aclAclGroupIngressMacAcl = _AclAclGroupIngressMacAcl_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 3, 1, 4),
    _AclAclGroupIngressMacAcl_Type()
)
aclAclGroupIngressMacAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupIngressMacAcl.setStatus("current")


class _AclAclGroupEgressMacAcl_Type(DisplayString):
    """Custom type aclAclGroupEgressMacAcl based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 15),
    )


_AclAclGroupEgressMacAcl_Type.__name__ = "DisplayString"
_AclAclGroupEgressMacAcl_Object = MibTableColumn
aclAclGroupEgressMacAcl = _AclAclGroupEgressMacAcl_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 3, 1, 5),
    _AclAclGroupEgressMacAcl_Type()
)
aclAclGroupEgressMacAcl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    aclAclGroupEgressMacAcl.setStatus("current")
_AclIngressIpMaskTable_Object = MibTable
aclIngressIpMaskTable = _AclIngressIpMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4)
)
if mibBuilder.loadTexts:
    aclIngressIpMaskTable.setStatus("current")
_AclIngressIpMaskEntry_Object = MibTableRow
aclIngressIpMaskEntry = _AclIngressIpMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1)
)
aclIngressIpMaskEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclIngressIpMaskIndex"),
)
if mibBuilder.loadTexts:
    aclIngressIpMaskEntry.setStatus("current")


class _AclIngressIpMaskIndex_Type(Integer32):
    """Custom type aclIngressIpMaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AclIngressIpMaskIndex_Type.__name__ = "Integer32"
_AclIngressIpMaskIndex_Object = MibTableColumn
aclIngressIpMaskIndex = _AclIngressIpMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 1),
    _AclIngressIpMaskIndex_Type()
)
aclIngressIpMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIngressIpMaskIndex.setStatus("current")


class _AclIngressIpMaskPrecedence_Type(Integer32):
    """Custom type aclIngressIpMaskPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclIngressIpMaskPrecedence_Type.__name__ = "Integer32"
_AclIngressIpMaskPrecedence_Object = MibTableColumn
aclIngressIpMaskPrecedence = _AclIngressIpMaskPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 2),
    _AclIngressIpMaskPrecedence_Type()
)
aclIngressIpMaskPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIngressIpMaskPrecedence.setStatus("current")
_AclIngressIpMaskIsEnableTos_Type = EnabledStatus
_AclIngressIpMaskIsEnableTos_Object = MibTableColumn
aclIngressIpMaskIsEnableTos = _AclIngressIpMaskIsEnableTos_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 3),
    _AclIngressIpMaskIsEnableTos_Type()
)
aclIngressIpMaskIsEnableTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskIsEnableTos.setStatus("current")
_AclIngressIpMaskIsEnableDscp_Type = EnabledStatus
_AclIngressIpMaskIsEnableDscp_Object = MibTableColumn
aclIngressIpMaskIsEnableDscp = _AclIngressIpMaskIsEnableDscp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 4),
    _AclIngressIpMaskIsEnableDscp_Type()
)
aclIngressIpMaskIsEnableDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskIsEnableDscp.setStatus("current")
_AclIngressIpMaskIsEnablePrecedence_Type = EnabledStatus
_AclIngressIpMaskIsEnablePrecedence_Object = MibTableColumn
aclIngressIpMaskIsEnablePrecedence = _AclIngressIpMaskIsEnablePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 5),
    _AclIngressIpMaskIsEnablePrecedence_Type()
)
aclIngressIpMaskIsEnablePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskIsEnablePrecedence.setStatus("current")
_AclIngressIpMaskIsEnableProtocol_Type = EnabledStatus
_AclIngressIpMaskIsEnableProtocol_Object = MibTableColumn
aclIngressIpMaskIsEnableProtocol = _AclIngressIpMaskIsEnableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 6),
    _AclIngressIpMaskIsEnableProtocol_Type()
)
aclIngressIpMaskIsEnableProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskIsEnableProtocol.setStatus("current")


class _AclIngressIpMaskSourceIpAddrBitmask_Type(Unsigned32):
    """Custom type aclIngressIpMaskSourceIpAddrBitmask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AclIngressIpMaskSourceIpAddrBitmask_Type.__name__ = "Unsigned32"
_AclIngressIpMaskSourceIpAddrBitmask_Object = MibTableColumn
aclIngressIpMaskSourceIpAddrBitmask = _AclIngressIpMaskSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 7),
    _AclIngressIpMaskSourceIpAddrBitmask_Type()
)
aclIngressIpMaskSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskSourceIpAddrBitmask.setStatus("current")


class _AclIngressIpMaskDestIpAddrBitmask_Type(Unsigned32):
    """Custom type aclIngressIpMaskDestIpAddrBitmask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AclIngressIpMaskDestIpAddrBitmask_Type.__name__ = "Unsigned32"
_AclIngressIpMaskDestIpAddrBitmask_Object = MibTableColumn
aclIngressIpMaskDestIpAddrBitmask = _AclIngressIpMaskDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 8),
    _AclIngressIpMaskDestIpAddrBitmask_Type()
)
aclIngressIpMaskDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskDestIpAddrBitmask.setStatus("current")


class _AclIngressIpMaskSourcePortBitmask_Type(Integer32):
    """Custom type aclIngressIpMaskSourcePortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIngressIpMaskSourcePortBitmask_Type.__name__ = "Integer32"
_AclIngressIpMaskSourcePortBitmask_Object = MibTableColumn
aclIngressIpMaskSourcePortBitmask = _AclIngressIpMaskSourcePortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 9),
    _AclIngressIpMaskSourcePortBitmask_Type()
)
aclIngressIpMaskSourcePortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskSourcePortBitmask.setStatus("current")


class _AclIngressIpMaskDestPortBitmask_Type(Integer32):
    """Custom type aclIngressIpMaskDestPortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIngressIpMaskDestPortBitmask_Type.__name__ = "Integer32"
_AclIngressIpMaskDestPortBitmask_Object = MibTableColumn
aclIngressIpMaskDestPortBitmask = _AclIngressIpMaskDestPortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 10),
    _AclIngressIpMaskDestPortBitmask_Type()
)
aclIngressIpMaskDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskDestPortBitmask.setStatus("current")


class _AclIngressIpMaskControlCodeBitmask_Type(Integer32):
    """Custom type aclIngressIpMaskControlCodeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclIngressIpMaskControlCodeBitmask_Type.__name__ = "Integer32"
_AclIngressIpMaskControlCodeBitmask_Object = MibTableColumn
aclIngressIpMaskControlCodeBitmask = _AclIngressIpMaskControlCodeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 11),
    _AclIngressIpMaskControlCodeBitmask_Type()
)
aclIngressIpMaskControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskControlCodeBitmask.setStatus("current")
_AclIngressIpMaskStatus_Type = RowStatus
_AclIngressIpMaskStatus_Object = MibTableColumn
aclIngressIpMaskStatus = _AclIngressIpMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 4, 1, 12),
    _AclIngressIpMaskStatus_Type()
)
aclIngressIpMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressIpMaskStatus.setStatus("current")
_AclEgressIpMaskTable_Object = MibTable
aclEgressIpMaskTable = _AclEgressIpMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5)
)
if mibBuilder.loadTexts:
    aclEgressIpMaskTable.setStatus("current")
_AclEgressIpMaskEntry_Object = MibTableRow
aclEgressIpMaskEntry = _AclEgressIpMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1)
)
aclEgressIpMaskEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclEgressIpMaskIndex"),
)
if mibBuilder.loadTexts:
    aclEgressIpMaskEntry.setStatus("current")


class _AclEgressIpMaskIndex_Type(Integer32):
    """Custom type aclEgressIpMaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AclEgressIpMaskIndex_Type.__name__ = "Integer32"
_AclEgressIpMaskIndex_Object = MibTableColumn
aclEgressIpMaskIndex = _AclEgressIpMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 1),
    _AclEgressIpMaskIndex_Type()
)
aclEgressIpMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclEgressIpMaskIndex.setStatus("current")


class _AclEgressIpMaskPrecedence_Type(Integer32):
    """Custom type aclEgressIpMaskPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclEgressIpMaskPrecedence_Type.__name__ = "Integer32"
_AclEgressIpMaskPrecedence_Object = MibTableColumn
aclEgressIpMaskPrecedence = _AclEgressIpMaskPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 2),
    _AclEgressIpMaskPrecedence_Type()
)
aclEgressIpMaskPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclEgressIpMaskPrecedence.setStatus("current")
_AclEgressIpMaskIsEnableTos_Type = EnabledStatus
_AclEgressIpMaskIsEnableTos_Object = MibTableColumn
aclEgressIpMaskIsEnableTos = _AclEgressIpMaskIsEnableTos_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 3),
    _AclEgressIpMaskIsEnableTos_Type()
)
aclEgressIpMaskIsEnableTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskIsEnableTos.setStatus("current")
_AclEgressIpMaskIsEnableDscp_Type = EnabledStatus
_AclEgressIpMaskIsEnableDscp_Object = MibTableColumn
aclEgressIpMaskIsEnableDscp = _AclEgressIpMaskIsEnableDscp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 4),
    _AclEgressIpMaskIsEnableDscp_Type()
)
aclEgressIpMaskIsEnableDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskIsEnableDscp.setStatus("current")
_AclEgressIpMaskIsEnablePrecedence_Type = EnabledStatus
_AclEgressIpMaskIsEnablePrecedence_Object = MibTableColumn
aclEgressIpMaskIsEnablePrecedence = _AclEgressIpMaskIsEnablePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 5),
    _AclEgressIpMaskIsEnablePrecedence_Type()
)
aclEgressIpMaskIsEnablePrecedence.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskIsEnablePrecedence.setStatus("current")
_AclEgressIpMaskIsEnableProtocol_Type = EnabledStatus
_AclEgressIpMaskIsEnableProtocol_Object = MibTableColumn
aclEgressIpMaskIsEnableProtocol = _AclEgressIpMaskIsEnableProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 6),
    _AclEgressIpMaskIsEnableProtocol_Type()
)
aclEgressIpMaskIsEnableProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskIsEnableProtocol.setStatus("current")


class _AclEgressIpMaskSourceIpAddrBitmask_Type(Unsigned32):
    """Custom type aclEgressIpMaskSourceIpAddrBitmask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AclEgressIpMaskSourceIpAddrBitmask_Type.__name__ = "Unsigned32"
_AclEgressIpMaskSourceIpAddrBitmask_Object = MibTableColumn
aclEgressIpMaskSourceIpAddrBitmask = _AclEgressIpMaskSourceIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 7),
    _AclEgressIpMaskSourceIpAddrBitmask_Type()
)
aclEgressIpMaskSourceIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskSourceIpAddrBitmask.setStatus("current")


class _AclEgressIpMaskDestIpAddrBitmask_Type(Unsigned32):
    """Custom type aclEgressIpMaskDestIpAddrBitmask based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_AclEgressIpMaskDestIpAddrBitmask_Type.__name__ = "Unsigned32"
_AclEgressIpMaskDestIpAddrBitmask_Object = MibTableColumn
aclEgressIpMaskDestIpAddrBitmask = _AclEgressIpMaskDestIpAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 8),
    _AclEgressIpMaskDestIpAddrBitmask_Type()
)
aclEgressIpMaskDestIpAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskDestIpAddrBitmask.setStatus("current")


class _AclEgressIpMaskSourcePortBitmask_Type(Integer32):
    """Custom type aclEgressIpMaskSourcePortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclEgressIpMaskSourcePortBitmask_Type.__name__ = "Integer32"
_AclEgressIpMaskSourcePortBitmask_Object = MibTableColumn
aclEgressIpMaskSourcePortBitmask = _AclEgressIpMaskSourcePortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 9),
    _AclEgressIpMaskSourcePortBitmask_Type()
)
aclEgressIpMaskSourcePortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskSourcePortBitmask.setStatus("current")


class _AclEgressIpMaskDestPortBitmask_Type(Integer32):
    """Custom type aclEgressIpMaskDestPortBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclEgressIpMaskDestPortBitmask_Type.__name__ = "Integer32"
_AclEgressIpMaskDestPortBitmask_Object = MibTableColumn
aclEgressIpMaskDestPortBitmask = _AclEgressIpMaskDestPortBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 10),
    _AclEgressIpMaskDestPortBitmask_Type()
)
aclEgressIpMaskDestPortBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskDestPortBitmask.setStatus("current")


class _AclEgressIpMaskControlCodeBitmask_Type(Integer32):
    """Custom type aclEgressIpMaskControlCodeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AclEgressIpMaskControlCodeBitmask_Type.__name__ = "Integer32"
_AclEgressIpMaskControlCodeBitmask_Object = MibTableColumn
aclEgressIpMaskControlCodeBitmask = _AclEgressIpMaskControlCodeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 11),
    _AclEgressIpMaskControlCodeBitmask_Type()
)
aclEgressIpMaskControlCodeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskControlCodeBitmask.setStatus("current")
_AclEgressIpMaskStatus_Type = RowStatus
_AclEgressIpMaskStatus_Object = MibTableColumn
aclEgressIpMaskStatus = _AclEgressIpMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 5, 1, 12),
    _AclEgressIpMaskStatus_Type()
)
aclEgressIpMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressIpMaskStatus.setStatus("current")
_AclIngressMacMaskTable_Object = MibTable
aclIngressMacMaskTable = _AclIngressMacMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 6)
)
if mibBuilder.loadTexts:
    aclIngressMacMaskTable.setStatus("current")
_AclIngressMacMaskEntry_Object = MibTableRow
aclIngressMacMaskEntry = _AclIngressMacMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 6, 1)
)
aclIngressMacMaskEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclIngressMacMaskIndex"),
)
if mibBuilder.loadTexts:
    aclIngressMacMaskEntry.setStatus("current")


class _AclIngressMacMaskIndex_Type(Integer32):
    """Custom type aclIngressMacMaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AclIngressMacMaskIndex_Type.__name__ = "Integer32"
_AclIngressMacMaskIndex_Object = MibTableColumn
aclIngressMacMaskIndex = _AclIngressMacMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 6, 1, 1),
    _AclIngressMacMaskIndex_Type()
)
aclIngressMacMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclIngressMacMaskIndex.setStatus("current")


class _AclIngressMacMaskPrecedence_Type(Integer32):
    """Custom type aclIngressMacMaskPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclIngressMacMaskPrecedence_Type.__name__ = "Integer32"
_AclIngressMacMaskPrecedence_Object = MibTableColumn
aclIngressMacMaskPrecedence = _AclIngressMacMaskPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 6, 1, 2),
    _AclIngressMacMaskPrecedence_Type()
)
aclIngressMacMaskPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIngressMacMaskPrecedence.setStatus("current")


class _AclIngressMacMaskSourceMacAddrBitmask_Type(OctetString):
    """Custom type aclIngressMacMaskSourceMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AclIngressMacMaskSourceMacAddrBitmask_Type.__name__ = "OctetString"
_AclIngressMacMaskSourceMacAddrBitmask_Object = MibTableColumn
aclIngressMacMaskSourceMacAddrBitmask = _AclIngressMacMaskSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 6, 1, 3),
    _AclIngressMacMaskSourceMacAddrBitmask_Type()
)
aclIngressMacMaskSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskSourceMacAddrBitmask.setStatus("current")


class _AclIngressMacMaskDestMacAddrBitmask_Type(OctetString):
    """Custom type aclIngressMacMaskDestMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AclIngressMacMaskDestMacAddrBitmask_Type.__name__ = "OctetString"
_AclIngressMacMaskDestMacAddrBitmask_Object = MibTableColumn
aclIngressMacMaskDestMacAddrBitmask = _AclIngressMacMaskDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 6, 1, 4),
    _AclIngressMacMaskDestMacAddrBitmask_Type()
)
aclIngressMacMaskDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskDestMacAddrBitmask.setStatus("current")


class _AclIngressMacMaskVidBitmask_Type(Integer32):
    """Custom type aclIngressMacMaskVidBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclIngressMacMaskVidBitmask_Type.__name__ = "Integer32"
_AclIngressMacMaskVidBitmask_Object = MibTableColumn
aclIngressMacMaskVidBitmask = _AclIngressMacMaskVidBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 6, 1, 5),
    _AclIngressMacMaskVidBitmask_Type()
)
aclIngressMacMaskVidBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskVidBitmask.setStatus("current")


class _AclIngressMacMaskEtherTypeBitmask_Type(Integer32):
    """Custom type aclIngressMacMaskEtherTypeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclIngressMacMaskEtherTypeBitmask_Type.__name__ = "Integer32"
_AclIngressMacMaskEtherTypeBitmask_Object = MibTableColumn
aclIngressMacMaskEtherTypeBitmask = _AclIngressMacMaskEtherTypeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 6, 1, 6),
    _AclIngressMacMaskEtherTypeBitmask_Type()
)
aclIngressMacMaskEtherTypeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskEtherTypeBitmask.setStatus("current")
_AclIngressMacMaskIsEnablePktformat_Type = EnabledStatus
_AclIngressMacMaskIsEnablePktformat_Object = MibTableColumn
aclIngressMacMaskIsEnablePktformat = _AclIngressMacMaskIsEnablePktformat_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 6, 1, 7),
    _AclIngressMacMaskIsEnablePktformat_Type()
)
aclIngressMacMaskIsEnablePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskIsEnablePktformat.setStatus("current")
_AclIngressMacMaskStatus_Type = RowStatus
_AclIngressMacMaskStatus_Object = MibTableColumn
aclIngressMacMaskStatus = _AclIngressMacMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 6, 1, 8),
    _AclIngressMacMaskStatus_Type()
)
aclIngressMacMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclIngressMacMaskStatus.setStatus("current")
_AclEgressMacMaskTable_Object = MibTable
aclEgressMacMaskTable = _AclEgressMacMaskTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 7)
)
if mibBuilder.loadTexts:
    aclEgressMacMaskTable.setStatus("current")
_AclEgressMacMaskEntry_Object = MibTableRow
aclEgressMacMaskEntry = _AclEgressMacMaskEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 7, 1)
)
aclEgressMacMaskEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclEgressMacMaskIndex"),
)
if mibBuilder.loadTexts:
    aclEgressMacMaskEntry.setStatus("current")


class _AclEgressMacMaskIndex_Type(Integer32):
    """Custom type aclEgressMacMaskIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AclEgressMacMaskIndex_Type.__name__ = "Integer32"
_AclEgressMacMaskIndex_Object = MibTableColumn
aclEgressMacMaskIndex = _AclEgressMacMaskIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 7, 1, 1),
    _AclEgressMacMaskIndex_Type()
)
aclEgressMacMaskIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    aclEgressMacMaskIndex.setStatus("current")


class _AclEgressMacMaskPrecedence_Type(Integer32):
    """Custom type aclEgressMacMaskPrecedence based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_AclEgressMacMaskPrecedence_Type.__name__ = "Integer32"
_AclEgressMacMaskPrecedence_Object = MibTableColumn
aclEgressMacMaskPrecedence = _AclEgressMacMaskPrecedence_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 7, 1, 2),
    _AclEgressMacMaskPrecedence_Type()
)
aclEgressMacMaskPrecedence.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclEgressMacMaskPrecedence.setStatus("current")


class _AclEgressMacMaskSourceMacAddrBitmask_Type(OctetString):
    """Custom type aclEgressMacMaskSourceMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AclEgressMacMaskSourceMacAddrBitmask_Type.__name__ = "OctetString"
_AclEgressMacMaskSourceMacAddrBitmask_Object = MibTableColumn
aclEgressMacMaskSourceMacAddrBitmask = _AclEgressMacMaskSourceMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 7, 1, 3),
    _AclEgressMacMaskSourceMacAddrBitmask_Type()
)
aclEgressMacMaskSourceMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskSourceMacAddrBitmask.setStatus("current")


class _AclEgressMacMaskDestMacAddrBitmask_Type(OctetString):
    """Custom type aclEgressMacMaskDestMacAddrBitmask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_AclEgressMacMaskDestMacAddrBitmask_Type.__name__ = "OctetString"
_AclEgressMacMaskDestMacAddrBitmask_Object = MibTableColumn
aclEgressMacMaskDestMacAddrBitmask = _AclEgressMacMaskDestMacAddrBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 7, 1, 4),
    _AclEgressMacMaskDestMacAddrBitmask_Type()
)
aclEgressMacMaskDestMacAddrBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskDestMacAddrBitmask.setStatus("current")


class _AclEgressMacMaskVidBitmask_Type(Integer32):
    """Custom type aclEgressMacMaskVidBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AclEgressMacMaskVidBitmask_Type.__name__ = "Integer32"
_AclEgressMacMaskVidBitmask_Object = MibTableColumn
aclEgressMacMaskVidBitmask = _AclEgressMacMaskVidBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 7, 1, 5),
    _AclEgressMacMaskVidBitmask_Type()
)
aclEgressMacMaskVidBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskVidBitmask.setStatus("current")


class _AclEgressMacMaskEtherTypeBitmask_Type(Integer32):
    """Custom type aclEgressMacMaskEtherTypeBitmask based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AclEgressMacMaskEtherTypeBitmask_Type.__name__ = "Integer32"
_AclEgressMacMaskEtherTypeBitmask_Object = MibTableColumn
aclEgressMacMaskEtherTypeBitmask = _AclEgressMacMaskEtherTypeBitmask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 7, 1, 6),
    _AclEgressMacMaskEtherTypeBitmask_Type()
)
aclEgressMacMaskEtherTypeBitmask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskEtherTypeBitmask.setStatus("current")
_AclEgressMacMaskIsEnablePktformat_Type = EnabledStatus
_AclEgressMacMaskIsEnablePktformat_Object = MibTableColumn
aclEgressMacMaskIsEnablePktformat = _AclEgressMacMaskIsEnablePktformat_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 7, 1, 7),
    _AclEgressMacMaskIsEnablePktformat_Type()
)
aclEgressMacMaskIsEnablePktformat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskIsEnablePktformat.setStatus("current")
_AclEgressMacMaskStatus_Type = RowStatus
_AclEgressMacMaskStatus_Object = MibTableColumn
aclEgressMacMaskStatus = _AclEgressMacMaskStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 7, 1, 8),
    _AclEgressMacMaskStatus_Type()
)
aclEgressMacMaskStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    aclEgressMacMaskStatus.setStatus("current")
_AclIpTable_Object = MibTable
aclIpTable = _AclIpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 8)
)
if mibBuilder.loadTexts:
    aclIpTable.setStatus("current")
_AclIpEntry_Object = MibTableRow
aclIpEntry = _AclIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 8, 1)
)
aclIpEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclIpAclName"),
)
if mibBuilder.loadTexts:
    aclIpEntry.setStatus("current")


class _AclIpAclName_Type(DisplayString):
    """Custom type aclIpAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AclIpAclName_Type.__name__ = "DisplayString"
_AclIpAclName_Object = MibTableColumn
aclIpAclName = _AclIpAclName_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 8, 1, 1),
    _AclIpAclName_Type()
)
aclIpAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclIpAclName.setStatus("current")
_AclMacTable_Object = MibTable
aclMacTable = _AclMacTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 9)
)
if mibBuilder.loadTexts:
    aclMacTable.setStatus("current")
_AclMacEntry_Object = MibTableRow
aclMacEntry = _AclMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 9, 1)
)
aclMacEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "aclMacAclName"),
)
if mibBuilder.loadTexts:
    aclMacEntry.setStatus("current")


class _AclMacAclName_Type(DisplayString):
    """Custom type aclMacAclName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 15),
    )


_AclMacAclName_Type.__name__ = "DisplayString"
_AclMacAclName_Object = MibTableColumn
aclMacAclName = _AclMacAclName_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 7, 9, 1, 1),
    _AclMacAclName_Type()
)
aclMacAclName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    aclMacAclName.setStatus("current")
_IpFilterMgt_ObjectIdentity = ObjectIdentity
ipFilterMgt = _IpFilterMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9)
)
_IpFilterSnmpTable_Object = MibTable
ipFilterSnmpTable = _IpFilterSnmpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 1)
)
if mibBuilder.loadTexts:
    ipFilterSnmpTable.setStatus("current")
_IpFilterSnmpEntry_Object = MibTableRow
ipFilterSnmpEntry = _IpFilterSnmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 1, 1)
)
ipFilterSnmpEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ipFilterSnmpStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterSnmpEntry.setStatus("current")
_IpFilterSnmpStartAddress_Type = IpAddress
_IpFilterSnmpStartAddress_Object = MibTableColumn
ipFilterSnmpStartAddress = _IpFilterSnmpStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 1, 1, 1),
    _IpFilterSnmpStartAddress_Type()
)
ipFilterSnmpStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterSnmpStartAddress.setStatus("current")
_IpFilterSnmpEndAddress_Type = IpAddress
_IpFilterSnmpEndAddress_Object = MibTableColumn
ipFilterSnmpEndAddress = _IpFilterSnmpEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 1, 1, 2),
    _IpFilterSnmpEndAddress_Type()
)
ipFilterSnmpEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpEndAddress.setStatus("current")
_IpFilterSnmpStatus_Type = ValidStatus
_IpFilterSnmpStatus_Object = MibTableColumn
ipFilterSnmpStatus = _IpFilterSnmpStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 1, 1, 3),
    _IpFilterSnmpStatus_Type()
)
ipFilterSnmpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterSnmpStatus.setStatus("current")
_IpFilterHTTPTable_Object = MibTable
ipFilterHTTPTable = _IpFilterHTTPTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 2)
)
if mibBuilder.loadTexts:
    ipFilterHTTPTable.setStatus("current")
_IpFilterHTTPEntry_Object = MibTableRow
ipFilterHTTPEntry = _IpFilterHTTPEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 2, 1)
)
ipFilterHTTPEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ipFilterHTTPStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterHTTPEntry.setStatus("current")
_IpFilterHTTPStartAddress_Type = IpAddress
_IpFilterHTTPStartAddress_Object = MibTableColumn
ipFilterHTTPStartAddress = _IpFilterHTTPStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 2, 1, 1),
    _IpFilterHTTPStartAddress_Type()
)
ipFilterHTTPStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterHTTPStartAddress.setStatus("current")
_IpFilterHTTPEndAddress_Type = IpAddress
_IpFilterHTTPEndAddress_Object = MibTableColumn
ipFilterHTTPEndAddress = _IpFilterHTTPEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 2, 1, 2),
    _IpFilterHTTPEndAddress_Type()
)
ipFilterHTTPEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHTTPEndAddress.setStatus("current")
_IpFilterHTTPStatus_Type = ValidStatus
_IpFilterHTTPStatus_Object = MibTableColumn
ipFilterHTTPStatus = _IpFilterHTTPStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 2, 1, 3),
    _IpFilterHTTPStatus_Type()
)
ipFilterHTTPStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterHTTPStatus.setStatus("current")
_IpFilterTelnetTable_Object = MibTable
ipFilterTelnetTable = _IpFilterTelnetTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 3)
)
if mibBuilder.loadTexts:
    ipFilterTelnetTable.setStatus("current")
_IpFilterTelnetEntry_Object = MibTableRow
ipFilterTelnetEntry = _IpFilterTelnetEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 3, 1)
)
ipFilterTelnetEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ipFilterTelnetStartAddress"),
)
if mibBuilder.loadTexts:
    ipFilterTelnetEntry.setStatus("current")
_IpFilterTelnetStartAddress_Type = IpAddress
_IpFilterTelnetStartAddress_Object = MibTableColumn
ipFilterTelnetStartAddress = _IpFilterTelnetStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 3, 1, 1),
    _IpFilterTelnetStartAddress_Type()
)
ipFilterTelnetStartAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipFilterTelnetStartAddress.setStatus("current")
_IpFilterTelnetEndAddress_Type = IpAddress
_IpFilterTelnetEndAddress_Object = MibTableColumn
ipFilterTelnetEndAddress = _IpFilterTelnetEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 3, 1, 2),
    _IpFilterTelnetEndAddress_Type()
)
ipFilterTelnetEndAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetEndAddress.setStatus("current")
_IpFilterTelnetStatus_Type = ValidStatus
_IpFilterTelnetStatus_Object = MibTableColumn
ipFilterTelnetStatus = _IpFilterTelnetStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 17, 9, 3, 1, 3),
    _IpFilterTelnetStatus_Type()
)
ipFilterTelnetStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipFilterTelnetStatus.setStatus("current")
_Layer3Mgt_ObjectIdentity = ObjectIdentity
layer3Mgt = _Layer3Mgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18)
)
_ArpMgt_ObjectIdentity = ObjectIdentity
arpMgt = _ArpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1)
)


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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 1),
    _ArpCacheDeleteAll_Type()
)
arpCacheDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpCacheDeleteAll.setStatus("current")


class _ArpCacheTimeout_Type(Integer32):
    """Custom type arpCacheTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(300, 86400),
    )


_ArpCacheTimeout_Type.__name__ = "Integer32"
_ArpCacheTimeout_Object = MibScalar
arpCacheTimeout = _ArpCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 2),
    _ArpCacheTimeout_Type()
)
arpCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpCacheTimeout.setStatus("current")
_ArpTrafficStatistics_ObjectIdentity = ObjectIdentity
arpTrafficStatistics = _ArpTrafficStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 3)
)
_ArpStatSendRequestPackets_Type = Counter32
_ArpStatSendRequestPackets_Object = MibScalar
arpStatSendRequestPackets = _ArpStatSendRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 3, 1),
    _ArpStatSendRequestPackets_Type()
)
arpStatSendRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatSendRequestPackets.setStatus("current")
_ArpStatRcvRequestPackets_Type = Counter32
_ArpStatRcvRequestPackets_Object = MibScalar
arpStatRcvRequestPackets = _ArpStatRcvRequestPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 3, 2),
    _ArpStatRcvRequestPackets_Type()
)
arpStatRcvRequestPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatRcvRequestPackets.setStatus("current")
_ArpStatSendReplyPackets_Type = Counter32
_ArpStatSendReplyPackets_Object = MibScalar
arpStatSendReplyPackets = _ArpStatSendReplyPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 3, 3),
    _ArpStatSendReplyPackets_Type()
)
arpStatSendReplyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatSendReplyPackets.setStatus("current")
_ArpStatRcvReplyPackets_Type = Counter32
_ArpStatRcvReplyPackets_Object = MibScalar
arpStatRcvReplyPackets = _ArpStatRcvReplyPackets_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 3, 4),
    _ArpStatRcvReplyPackets_Type()
)
arpStatRcvReplyPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arpStatRcvReplyPackets.setStatus("current")
_ArpProxyArpTable_Object = MibTable
arpProxyArpTable = _ArpProxyArpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 4)
)
if mibBuilder.loadTexts:
    arpProxyArpTable.setStatus("current")
_ArpProxyArpEntry_Object = MibTableRow
arpProxyArpEntry = _ArpProxyArpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 4, 1)
)
arpProxyArpEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "arpProxyArpIfIndex"),
)
if mibBuilder.loadTexts:
    arpProxyArpEntry.setStatus("current")
_ArpProxyArpIfIndex_Type = Integer32
_ArpProxyArpIfIndex_Object = MibTableColumn
arpProxyArpIfIndex = _ArpProxyArpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 4, 1, 1),
    _ArpProxyArpIfIndex_Type()
)
arpProxyArpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arpProxyArpIfIndex.setStatus("current")


class _ArpProxyArpStatus_Type(EnabledStatus):
    """Custom type arpProxyArpStatus based on EnabledStatus"""
    defaultValue = 1


_ArpProxyArpStatus_Type.__name__ = "EnabledStatus"
_ArpProxyArpStatus_Object = MibTableColumn
arpProxyArpStatus = _ArpProxyArpStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 1, 4, 1, 2),
    _ArpProxyArpStatus_Type()
)
arpProxyArpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arpProxyArpStatus.setStatus("current")
_RipMgt_ObjectIdentity = ObjectIdentity
ripMgt = _RipMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2)
)
_RipTimers_ObjectIdentity = ObjectIdentity
ripTimers = _RipTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 1)
)


class _RipUpdateTime_Type(Integer32):
    """Custom type ripUpdateTime based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 60),
    )


_RipUpdateTime_Type.__name__ = "Integer32"
_RipUpdateTime_Object = MibScalar
ripUpdateTime = _RipUpdateTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 1, 1),
    _RipUpdateTime_Type()
)
ripUpdateTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripUpdateTime.setStatus("current")


class _RipTimeoutTime_Type(Integer32):
    """Custom type ripTimeoutTime based on Integer32"""
    defaultValue = 180

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(90, 360),
    )


_RipTimeoutTime_Type.__name__ = "Integer32"
_RipTimeoutTime_Object = MibScalar
ripTimeoutTime = _RipTimeoutTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 1, 2),
    _RipTimeoutTime_Type()
)
ripTimeoutTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripTimeoutTime.setStatus("current")


class _RipGarbageCollectionTime_Type(Integer32):
    """Custom type ripGarbageCollectionTime based on Integer32"""
    defaultValue = 120

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 240),
    )


_RipGarbageCollectionTime_Type.__name__ = "Integer32"
_RipGarbageCollectionTime_Object = MibScalar
ripGarbageCollectionTime = _RipGarbageCollectionTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 1, 3),
    _RipGarbageCollectionTime_Type()
)
ripGarbageCollectionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ripGarbageCollectionTime.setStatus("current")


class _RipRoutingProcessStatus_Type(EnabledStatus):
    """Custom type ripRoutingProcessStatus based on EnabledStatus"""
    defaultValue = 2


_RipRoutingProcessStatus_Type.__name__ = "EnabledStatus"
_RipRoutingProcessStatus_Object = MibScalar
ripRoutingProcessStatus = _RipRoutingProcessStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 2),
    _RipRoutingProcessStatus_Type()
)
ripRoutingProcessStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripRoutingProcessStatus.setStatus("current")


class _RipRouterVersion_Type(Integer32):
    """Custom type ripRouterVersion based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("byInterface", 1),
          ("rip1", 2),
          ("rip2", 3))
    )


_RipRouterVersion_Type.__name__ = "Integer32"
_RipRouterVersion_Object = MibScalar
ripRouterVersion = _RipRouterVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 3),
    _RipRouterVersion_Type()
)
ripRouterVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripRouterVersion.setStatus("current")
_RipInstabilityPreventingTable_Object = MibTable
ripInstabilityPreventingTable = _RipInstabilityPreventingTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 4)
)
if mibBuilder.loadTexts:
    ripInstabilityPreventingTable.setStatus("current")
_RipInstabilityPreventingEntry_Object = MibTableRow
ripInstabilityPreventingEntry = _RipInstabilityPreventingEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 4, 1)
)
ripInstabilityPreventingEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ripVlanIndex"),
)
if mibBuilder.loadTexts:
    ripInstabilityPreventingEntry.setStatus("current")
_RipVlanIndex_Type = Integer32
_RipVlanIndex_Object = MibTableColumn
ripVlanIndex = _RipVlanIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 4, 1, 1),
    _RipVlanIndex_Type()
)
ripVlanIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ripVlanIndex.setStatus("current")


class _RipSplitHorizonStatus_Type(Integer32):
    """Custom type ripSplitHorizonStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("splitHorizon", 1),
          ("poisonReverse", 2),
          ("none", 3))
    )


_RipSplitHorizonStatus_Type.__name__ = "Integer32"
_RipSplitHorizonStatus_Object = MibTableColumn
ripSplitHorizonStatus = _RipSplitHorizonStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 4, 1, 2),
    _RipSplitHorizonStatus_Type()
)
ripSplitHorizonStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripSplitHorizonStatus.setStatus("current")


class _RipStatisticsReset_Type(Integer32):
    """Custom type ripStatisticsReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("reset", 1),
          ("noReset", 2))
    )


_RipStatisticsReset_Type.__name__ = "Integer32"
_RipStatisticsReset_Object = MibScalar
ripStatisticsReset = _RipStatisticsReset_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 5),
    _RipStatisticsReset_Type()
)
ripStatisticsReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ripStatisticsReset.setStatus("current")
_RipNetworkAddrTable_Object = MibTable
ripNetworkAddrTable = _RipNetworkAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 6)
)
if mibBuilder.loadTexts:
    ripNetworkAddrTable.setStatus("current")
_RipNetworkAddrEntry_Object = MibTableRow
ripNetworkAddrEntry = _RipNetworkAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 6, 1)
)
ripNetworkAddrEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ripNetworkAddrAddress"),
)
if mibBuilder.loadTexts:
    ripNetworkAddrEntry.setStatus("current")
_RipNetworkAddrAddress_Type = IpAddress
_RipNetworkAddrAddress_Object = MibTableColumn
ripNetworkAddrAddress = _RipNetworkAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 6, 1, 1),
    _RipNetworkAddrAddress_Type()
)
ripNetworkAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ripNetworkAddrAddress.setStatus("current")
_RipNetworkAddrStatus_Type = ValidStatus
_RipNetworkAddrStatus_Object = MibTableColumn
ripNetworkAddrStatus = _RipNetworkAddrStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 2, 6, 1, 2),
    _RipNetworkAddrStatus_Type()
)
ripNetworkAddrStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ripNetworkAddrStatus.setStatus("current")
_OspfMgt_ObjectIdentity = ObjectIdentity
ospfMgt = _OspfMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3)
)
_OspfSystemGroup_ObjectIdentity = ObjectIdentity
ospfSystemGroup = _OspfSystemGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1)
)


class _OspfRouterIdType_Type(Integer32):
    """Custom type ospfRouterIdType based on Integer32"""
    defaultValue = 1

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


_OspfRouterIdType_Type.__name__ = "Integer32"
_OspfRouterIdType_Object = MibScalar
ospfRouterIdType = _OspfRouterIdType_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1, 1),
    _OspfRouterIdType_Type()
)
ospfRouterIdType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfRouterIdType.setStatus("current")


class _OspfRfc1583CompatibleState_Type(EnabledStatus):
    """Custom type ospfRfc1583CompatibleState based on EnabledStatus"""
    defaultValue = 2


_OspfRfc1583CompatibleState_Type.__name__ = "EnabledStatus"
_OspfRfc1583CompatibleState_Object = MibScalar
ospfRfc1583CompatibleState = _OspfRfc1583CompatibleState_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1, 2),
    _OspfRfc1583CompatibleState_Type()
)
ospfRfc1583CompatibleState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfRfc1583CompatibleState.setStatus("current")


class _OspfAutoCost_Type(Integer32):
    """Custom type ospfAutoCost based on Integer32"""
    defaultValue = 100


_OspfAutoCost_Type.__name__ = "Integer32"
_OspfAutoCost_Object = MibScalar
ospfAutoCost = _OspfAutoCost_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1, 3),
    _OspfAutoCost_Type()
)
ospfAutoCost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAutoCost.setStatus("current")


class _OspfOriginateDefaultRoute_Type(EnabledStatus):
    """Custom type ospfOriginateDefaultRoute based on EnabledStatus"""
    defaultValue = 2


_OspfOriginateDefaultRoute_Type.__name__ = "EnabledStatus"
_OspfOriginateDefaultRoute_Object = MibScalar
ospfOriginateDefaultRoute = _OspfOriginateDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1, 4),
    _OspfOriginateDefaultRoute_Type()
)
ospfOriginateDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfOriginateDefaultRoute.setStatus("current")


class _OspfAdvertiseDefaultRoute_Type(Integer32):
    """Custom type ospfAdvertiseDefaultRoute based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("always", 1),
          ("notAlways", 2))
    )


_OspfAdvertiseDefaultRoute_Type.__name__ = "Integer32"
_OspfAdvertiseDefaultRoute_Object = MibScalar
ospfAdvertiseDefaultRoute = _OspfAdvertiseDefaultRoute_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1, 5),
    _OspfAdvertiseDefaultRoute_Type()
)
ospfAdvertiseDefaultRoute.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfAdvertiseDefaultRoute.setStatus("current")


class _OspfExternalMetricType_Type(Integer32):
    """Custom type ospfExternalMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_OspfExternalMetricType_Type.__name__ = "Integer32"
_OspfExternalMetricType_Object = MibScalar
ospfExternalMetricType = _OspfExternalMetricType_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1, 6),
    _OspfExternalMetricType_Type()
)
ospfExternalMetricType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfExternalMetricType.setStatus("current")


class _OspfDefaultExternalMetric_Type(OspfBigMetric):
    """Custom type ospfDefaultExternalMetric based on OspfBigMetric"""
    defaultValue = 10


_OspfDefaultExternalMetric_Type.__name__ = "OspfBigMetric"
_OspfDefaultExternalMetric_Object = MibScalar
ospfDefaultExternalMetric = _OspfDefaultExternalMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1, 7),
    _OspfDefaultExternalMetric_Type()
)
ospfDefaultExternalMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfDefaultExternalMetric.setStatus("current")


class _OspfSpfHoldTime_Type(Integer32):
    """Custom type ospfSpfHoldTime based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfSpfHoldTime_Type.__name__ = "Integer32"
_OspfSpfHoldTime_Object = MibScalar
ospfSpfHoldTime = _OspfSpfHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1, 8),
    _OspfSpfHoldTime_Type()
)
ospfSpfHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfSpfHoldTime.setStatus("current")


class _OspfSpfDelayTime_Type(Integer32):
    """Custom type ospfSpfDelayTime based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_OspfSpfDelayTime_Type.__name__ = "Integer32"
_OspfSpfDelayTime_Object = MibScalar
ospfSpfDelayTime = _OspfSpfDelayTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1, 9),
    _OspfSpfDelayTime_Type()
)
ospfSpfDelayTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ospfSpfDelayTime.setStatus("current")


class _OspfAreaNumber_Type(Integer32):
    """Custom type ospfAreaNumber based on Integer32"""
    defaultValue = 0


_OspfAreaNumber_Type.__name__ = "Integer32"
_OspfAreaNumber_Object = MibScalar
ospfAreaNumber = _OspfAreaNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 1, 10),
    _OspfAreaNumber_Type()
)
ospfAreaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ospfAreaNumber.setStatus("current")
_OspfNssaTable_Object = MibTable
ospfNssaTable = _OspfNssaTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 2)
)
if mibBuilder.loadTexts:
    ospfNssaTable.setStatus("current")
_OspfNssaEntry_Object = MibTableRow
ospfNssaEntry = _OspfNssaEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 2, 1)
)
ospfNssaEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ospfNssaAreaId"),
)
if mibBuilder.loadTexts:
    ospfNssaEntry.setStatus("current")
_OspfNssaAreaId_Type = OspfAreaID
_OspfNssaAreaId_Object = MibTableColumn
ospfNssaAreaId = _OspfNssaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 2, 1, 1),
    _OspfNssaAreaId_Type()
)
ospfNssaAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfNssaAreaId.setStatus("current")


class _OspfNssaRedistributeStatus_Type(EnabledStatus):
    """Custom type ospfNssaRedistributeStatus based on EnabledStatus"""
    defaultValue = 1


_OspfNssaRedistributeStatus_Type.__name__ = "EnabledStatus"
_OspfNssaRedistributeStatus_Object = MibTableColumn
ospfNssaRedistributeStatus = _OspfNssaRedistributeStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 2, 1, 2),
    _OspfNssaRedistributeStatus_Type()
)
ospfNssaRedistributeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNssaRedistributeStatus.setStatus("current")


class _OspfNssaOriginateDefaultInfoStatus_Type(EnabledStatus):
    """Custom type ospfNssaOriginateDefaultInfoStatus based on EnabledStatus"""
    defaultValue = 2


_OspfNssaOriginateDefaultInfoStatus_Type.__name__ = "EnabledStatus"
_OspfNssaOriginateDefaultInfoStatus_Object = MibTableColumn
ospfNssaOriginateDefaultInfoStatus = _OspfNssaOriginateDefaultInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 2, 1, 3),
    _OspfNssaOriginateDefaultInfoStatus_Type()
)
ospfNssaOriginateDefaultInfoStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNssaOriginateDefaultInfoStatus.setStatus("current")
_OspfNssaStatus_Type = RowStatus
_OspfNssaStatus_Object = MibTableColumn
ospfNssaStatus = _OspfNssaStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 2, 1, 4),
    _OspfNssaStatus_Type()
)
ospfNssaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNssaStatus.setStatus("current")
_OspfRedistributeTable_Object = MibTable
ospfRedistributeTable = _OspfRedistributeTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 3)
)
if mibBuilder.loadTexts:
    ospfRedistributeTable.setStatus("current")
_OspfRedistributeEntry_Object = MibTableRow
ospfRedistributeEntry = _OspfRedistributeEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 3, 1)
)
ospfRedistributeEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ospfRedistributeProtocol"),
)
if mibBuilder.loadTexts:
    ospfRedistributeEntry.setStatus("current")


class _OspfRedistributeProtocol_Type(Integer32):
    """Custom type ospfRedistributeProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("rip", 1),
          ("static", 2))
    )


_OspfRedistributeProtocol_Type.__name__ = "Integer32"
_OspfRedistributeProtocol_Object = MibTableColumn
ospfRedistributeProtocol = _OspfRedistributeProtocol_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 3, 1, 1),
    _OspfRedistributeProtocol_Type()
)
ospfRedistributeProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfRedistributeProtocol.setStatus("current")


class _OspfRedistributeMetricType_Type(Integer32):
    """Custom type ospfRedistributeMetricType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2))
    )


_OspfRedistributeMetricType_Type.__name__ = "Integer32"
_OspfRedistributeMetricType_Object = MibTableColumn
ospfRedistributeMetricType = _OspfRedistributeMetricType_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 3, 1, 2),
    _OspfRedistributeMetricType_Type()
)
ospfRedistributeMetricType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfRedistributeMetricType.setStatus("current")


class _OspfRedistributeMetric_Type(OspfBigMetric):
    """Custom type ospfRedistributeMetric based on OspfBigMetric"""
    defaultValue = 10


_OspfRedistributeMetric_Type.__name__ = "OspfBigMetric"
_OspfRedistributeMetric_Object = MibTableColumn
ospfRedistributeMetric = _OspfRedistributeMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 3, 1, 3),
    _OspfRedistributeMetric_Type()
)
ospfRedistributeMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfRedistributeMetric.setStatus("current")
_OspfRedistributeStatus_Type = RowStatus
_OspfRedistributeStatus_Object = MibTableColumn
ospfRedistributeStatus = _OspfRedistributeStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 3, 1, 4),
    _OspfRedistributeStatus_Type()
)
ospfRedistributeStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfRedistributeStatus.setStatus("current")
_OspfSummaryAddressTable_Object = MibTable
ospfSummaryAddressTable = _OspfSummaryAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 4)
)
if mibBuilder.loadTexts:
    ospfSummaryAddressTable.setStatus("current")
_OspfSummaryAddressEntry_Object = MibTableRow
ospfSummaryAddressEntry = _OspfSummaryAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 4, 1)
)
ospfSummaryAddressEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ospfSummaryAddress"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ospfSummaryMask"),
)
if mibBuilder.loadTexts:
    ospfSummaryAddressEntry.setStatus("current")
_OspfSummaryAddress_Type = IpAddress
_OspfSummaryAddress_Object = MibTableColumn
ospfSummaryAddress = _OspfSummaryAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 4, 1, 1),
    _OspfSummaryAddress_Type()
)
ospfSummaryAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfSummaryAddress.setStatus("current")
_OspfSummaryMask_Type = IpAddress
_OspfSummaryMask_Object = MibTableColumn
ospfSummaryMask = _OspfSummaryMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 4, 1, 2),
    _OspfSummaryMask_Type()
)
ospfSummaryMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfSummaryMask.setStatus("current")
_OspfSummaryStatus_Type = RowStatus
_OspfSummaryStatus_Object = MibTableColumn
ospfSummaryStatus = _OspfSummaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 4, 1, 3),
    _OspfSummaryStatus_Type()
)
ospfSummaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfSummaryStatus.setStatus("current")
_OspfNetworkAreaAddressTable_Object = MibTable
ospfNetworkAreaAddressTable = _OspfNetworkAreaAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 5)
)
if mibBuilder.loadTexts:
    ospfNetworkAreaAddressTable.setStatus("current")
_OspfNetworkAreaAddressEntry_Object = MibTableRow
ospfNetworkAreaAddressEntry = _OspfNetworkAreaAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 5, 1)
)
ospfNetworkAreaAddressEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ospfNetworkAareaAddress"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ospfNetworkAreaMask"),
)
if mibBuilder.loadTexts:
    ospfNetworkAreaAddressEntry.setStatus("current")
_OspfNetworkAareaAddress_Type = IpAddress
_OspfNetworkAareaAddress_Object = MibTableColumn
ospfNetworkAareaAddress = _OspfNetworkAareaAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 5, 1, 1),
    _OspfNetworkAareaAddress_Type()
)
ospfNetworkAareaAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfNetworkAareaAddress.setStatus("current")
_OspfNetworkAreaMask_Type = IpAddress
_OspfNetworkAreaMask_Object = MibTableColumn
ospfNetworkAreaMask = _OspfNetworkAreaMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 5, 1, 2),
    _OspfNetworkAreaMask_Type()
)
ospfNetworkAreaMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ospfNetworkAreaMask.setStatus("current")
_OspfNetworkAreaAreaId_Type = IpAddress
_OspfNetworkAreaAreaId_Object = MibTableColumn
ospfNetworkAreaAreaId = _OspfNetworkAreaAreaId_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 5, 1, 3),
    _OspfNetworkAreaAreaId_Type()
)
ospfNetworkAreaAreaId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNetworkAreaAreaId.setStatus("current")
_OspfNetworkAreaStatus_Type = RowStatus
_OspfNetworkAreaStatus_Object = MibTableColumn
ospfNetworkAreaStatus = _OspfNetworkAreaStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 3, 5, 1, 4),
    _OspfNetworkAreaStatus_Type()
)
ospfNetworkAreaStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ospfNetworkAreaStatus.setStatus("current")
_DvmrpMgt_ObjectIdentity = ObjectIdentity
dvmrpMgt = _DvmrpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4)
)
_DvmrpScalar_ObjectIdentity = ObjectIdentity
dvmrpScalar = _DvmrpScalar_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 1)
)
_DvmrpVersionString_Type = DisplayString
_DvmrpVersionString_Object = MibScalar
dvmrpVersionString = _DvmrpVersionString_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 1, 1),
    _DvmrpVersionString_Type()
)
dvmrpVersionString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpVersionString.setStatus("current")
_DvmrpNumRoutes_Type = Gauge32
_DvmrpNumRoutes_Object = MibScalar
dvmrpNumRoutes = _DvmrpNumRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 1, 3),
    _DvmrpNumRoutes_Type()
)
dvmrpNumRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNumRoutes.setStatus("current")
_DvmrpReachableRoutes_Type = Gauge32
_DvmrpReachableRoutes_Object = MibScalar
dvmrpReachableRoutes = _DvmrpReachableRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 1, 4),
    _DvmrpReachableRoutes_Type()
)
dvmrpReachableRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpReachableRoutes.setStatus("current")
_DvmrpInterfaceTable_Object = MibTable
dvmrpInterfaceTable = _DvmrpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2)
)
if mibBuilder.loadTexts:
    dvmrpInterfaceTable.setStatus("current")
_DvmrpInterfaceEntry_Object = MibTableRow
dvmrpInterfaceEntry = _DvmrpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1)
)
dvmrpInterfaceEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpInterfaceIndex"),
)
if mibBuilder.loadTexts:
    dvmrpInterfaceEntry.setStatus("current")
_DvmrpInterfaceIndex_Type = InterfaceIndex
_DvmrpInterfaceIndex_Object = MibTableColumn
dvmrpInterfaceIndex = _DvmrpInterfaceIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1, 1),
    _DvmrpInterfaceIndex_Type()
)
dvmrpInterfaceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpInterfaceIndex.setStatus("current")
_DvmrpInterfaceLocalAddress_Type = IpAddress
_DvmrpInterfaceLocalAddress_Object = MibTableColumn
dvmrpInterfaceLocalAddress = _DvmrpInterfaceLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1, 2),
    _DvmrpInterfaceLocalAddress_Type()
)
dvmrpInterfaceLocalAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceLocalAddress.setStatus("current")


class _DvmrpInterfaceMetric_Type(Integer32):
    """Custom type dvmrpInterfaceMetric based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_DvmrpInterfaceMetric_Type.__name__ = "Integer32"
_DvmrpInterfaceMetric_Object = MibTableColumn
dvmrpInterfaceMetric = _DvmrpInterfaceMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1, 3),
    _DvmrpInterfaceMetric_Type()
)
dvmrpInterfaceMetric.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceMetric.setStatus("current")
_DvmrpInterfaceStatus_Type = RowStatus
_DvmrpInterfaceStatus_Object = MibTableColumn
dvmrpInterfaceStatus = _DvmrpInterfaceStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1, 4),
    _DvmrpInterfaceStatus_Type()
)
dvmrpInterfaceStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceStatus.setStatus("current")
_DvmrpInterfaceRcvBadPkts_Type = Counter32
_DvmrpInterfaceRcvBadPkts_Object = MibTableColumn
dvmrpInterfaceRcvBadPkts = _DvmrpInterfaceRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1, 5),
    _DvmrpInterfaceRcvBadPkts_Type()
)
dvmrpInterfaceRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceRcvBadPkts.setStatus("current")
_DvmrpInterfaceRcvBadRoutes_Type = Counter32
_DvmrpInterfaceRcvBadRoutes_Object = MibTableColumn
dvmrpInterfaceRcvBadRoutes = _DvmrpInterfaceRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1, 6),
    _DvmrpInterfaceRcvBadRoutes_Type()
)
dvmrpInterfaceRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceRcvBadRoutes.setStatus("current")
_DvmrpInterfaceSentRoutes_Type = Counter32
_DvmrpInterfaceSentRoutes_Object = MibTableColumn
dvmrpInterfaceSentRoutes = _DvmrpInterfaceSentRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1, 7),
    _DvmrpInterfaceSentRoutes_Type()
)
dvmrpInterfaceSentRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceSentRoutes.setStatus("current")
_DvmrpInterfaceKey_Type = SnmpAdminString
_DvmrpInterfaceKey_Object = MibTableColumn
dvmrpInterfaceKey = _DvmrpInterfaceKey_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1, 8),
    _DvmrpInterfaceKey_Type()
)
dvmrpInterfaceKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceKey.setStatus("current")
_DvmrpInterfaceKeyVersion_Type = Integer32
_DvmrpInterfaceKeyVersion_Object = MibTableColumn
dvmrpInterfaceKeyVersion = _DvmrpInterfaceKeyVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1, 9),
    _DvmrpInterfaceKeyVersion_Type()
)
dvmrpInterfaceKeyVersion.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dvmrpInterfaceKeyVersion.setStatus("current")
_DvmrpInterfaceGenerationId_Type = Integer32
_DvmrpInterfaceGenerationId_Object = MibTableColumn
dvmrpInterfaceGenerationId = _DvmrpInterfaceGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 2, 1, 10),
    _DvmrpInterfaceGenerationId_Type()
)
dvmrpInterfaceGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpInterfaceGenerationId.setStatus("current")
_DvmrpNeighborTable_Object = MibTable
dvmrpNeighborTable = _DvmrpNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3)
)
if mibBuilder.loadTexts:
    dvmrpNeighborTable.setStatus("current")
_DvmrpNeighborEntry_Object = MibTableRow
dvmrpNeighborEntry = _DvmrpNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1)
)
dvmrpNeighborEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpNeighborIfIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpNeighborAddress"),
)
if mibBuilder.loadTexts:
    dvmrpNeighborEntry.setStatus("current")
_DvmrpNeighborIfIndex_Type = InterfaceIndex
_DvmrpNeighborIfIndex_Object = MibTableColumn
dvmrpNeighborIfIndex = _DvmrpNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 1),
    _DvmrpNeighborIfIndex_Type()
)
dvmrpNeighborIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpNeighborIfIndex.setStatus("current")
_DvmrpNeighborAddress_Type = IpAddress
_DvmrpNeighborAddress_Object = MibTableColumn
dvmrpNeighborAddress = _DvmrpNeighborAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 2),
    _DvmrpNeighborAddress_Type()
)
dvmrpNeighborAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpNeighborAddress.setStatus("current")
_DvmrpNeighborUpTime_Type = TimeTicks
_DvmrpNeighborUpTime_Object = MibTableColumn
dvmrpNeighborUpTime = _DvmrpNeighborUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 3),
    _DvmrpNeighborUpTime_Type()
)
dvmrpNeighborUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborUpTime.setStatus("current")
_DvmrpNeighborExpiryTime_Type = TimeTicks
_DvmrpNeighborExpiryTime_Object = MibTableColumn
dvmrpNeighborExpiryTime = _DvmrpNeighborExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 4),
    _DvmrpNeighborExpiryTime_Type()
)
dvmrpNeighborExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborExpiryTime.setStatus("current")
_DvmrpNeighborGenerationId_Type = Integer32
_DvmrpNeighborGenerationId_Object = MibTableColumn
dvmrpNeighborGenerationId = _DvmrpNeighborGenerationId_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 5),
    _DvmrpNeighborGenerationId_Type()
)
dvmrpNeighborGenerationId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborGenerationId.setStatus("current")


class _DvmrpNeighborMajorVersion_Type(Integer32):
    """Custom type dvmrpNeighborMajorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvmrpNeighborMajorVersion_Type.__name__ = "Integer32"
_DvmrpNeighborMajorVersion_Object = MibTableColumn
dvmrpNeighborMajorVersion = _DvmrpNeighborMajorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 6),
    _DvmrpNeighborMajorVersion_Type()
)
dvmrpNeighborMajorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborMajorVersion.setStatus("current")


class _DvmrpNeighborMinorVersion_Type(Integer32):
    """Custom type dvmrpNeighborMinorVersion based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_DvmrpNeighborMinorVersion_Type.__name__ = "Integer32"
_DvmrpNeighborMinorVersion_Object = MibTableColumn
dvmrpNeighborMinorVersion = _DvmrpNeighborMinorVersion_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 7),
    _DvmrpNeighborMinorVersion_Type()
)
dvmrpNeighborMinorVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborMinorVersion.setStatus("current")


class _DvmrpNeighborCapabilities_Type(Bits):
    """Custom type dvmrpNeighborCapabilities based on Bits"""
    namedValues = NamedValues(
        *(("leaf", 0),
          ("prune", 1),
          ("generationID", 2),
          ("mtrace", 3))
    )

_DvmrpNeighborCapabilities_Type.__name__ = "Bits"
_DvmrpNeighborCapabilities_Object = MibTableColumn
dvmrpNeighborCapabilities = _DvmrpNeighborCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 8),
    _DvmrpNeighborCapabilities_Type()
)
dvmrpNeighborCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborCapabilities.setStatus("current")
_DvmrpNeighborRcvRoutes_Type = Counter32
_DvmrpNeighborRcvRoutes_Object = MibTableColumn
dvmrpNeighborRcvRoutes = _DvmrpNeighborRcvRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 9),
    _DvmrpNeighborRcvRoutes_Type()
)
dvmrpNeighborRcvRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvRoutes.setStatus("current")
_DvmrpNeighborRcvBadPkts_Type = Counter32
_DvmrpNeighborRcvBadPkts_Object = MibTableColumn
dvmrpNeighborRcvBadPkts = _DvmrpNeighborRcvBadPkts_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 10),
    _DvmrpNeighborRcvBadPkts_Type()
)
dvmrpNeighborRcvBadPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvBadPkts.setStatus("current")
_DvmrpNeighborRcvBadRoutes_Type = Counter32
_DvmrpNeighborRcvBadRoutes_Object = MibTableColumn
dvmrpNeighborRcvBadRoutes = _DvmrpNeighborRcvBadRoutes_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 11),
    _DvmrpNeighborRcvBadRoutes_Type()
)
dvmrpNeighborRcvBadRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborRcvBadRoutes.setStatus("current")


class _DvmrpNeighborState_Type(Integer32):
    """Custom type dvmrpNeighborState based on Integer32"""
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
        *(("oneway", 1),
          ("active", 2),
          ("ignoring", 3),
          ("down", 4))
    )


_DvmrpNeighborState_Type.__name__ = "Integer32"
_DvmrpNeighborState_Object = MibTableColumn
dvmrpNeighborState = _DvmrpNeighborState_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 3, 1, 12),
    _DvmrpNeighborState_Type()
)
dvmrpNeighborState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpNeighborState.setStatus("current")
_DvmrpRouteTable_Object = MibTable
dvmrpRouteTable = _DvmrpRouteTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 4)
)
if mibBuilder.loadTexts:
    dvmrpRouteTable.setStatus("current")
_DvmrpRouteEntry_Object = MibTableRow
dvmrpRouteEntry = _DvmrpRouteEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 4, 1)
)
dvmrpRouteEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpRouteSource"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpRouteSourceMask"),
)
if mibBuilder.loadTexts:
    dvmrpRouteEntry.setStatus("current")
_DvmrpRouteSource_Type = IpAddress
_DvmrpRouteSource_Object = MibTableColumn
dvmrpRouteSource = _DvmrpRouteSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 4, 1, 1),
    _DvmrpRouteSource_Type()
)
dvmrpRouteSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteSource.setStatus("current")
_DvmrpRouteSourceMask_Type = IpAddress
_DvmrpRouteSourceMask_Object = MibTableColumn
dvmrpRouteSourceMask = _DvmrpRouteSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 4, 1, 2),
    _DvmrpRouteSourceMask_Type()
)
dvmrpRouteSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteSourceMask.setStatus("current")
_DvmrpRouteUpstreamNeighbor_Type = IpAddress
_DvmrpRouteUpstreamNeighbor_Object = MibTableColumn
dvmrpRouteUpstreamNeighbor = _DvmrpRouteUpstreamNeighbor_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 4, 1, 3),
    _DvmrpRouteUpstreamNeighbor_Type()
)
dvmrpRouteUpstreamNeighbor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteUpstreamNeighbor.setStatus("current")
_DvmrpRouteIfIndex_Type = InterfaceIndexOrZero
_DvmrpRouteIfIndex_Object = MibTableColumn
dvmrpRouteIfIndex = _DvmrpRouteIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 4, 1, 4),
    _DvmrpRouteIfIndex_Type()
)
dvmrpRouteIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteIfIndex.setStatus("current")


class _DvmrpRouteMetric_Type(Integer32):
    """Custom type dvmrpRouteMetric based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 32),
    )


_DvmrpRouteMetric_Type.__name__ = "Integer32"
_DvmrpRouteMetric_Object = MibTableColumn
dvmrpRouteMetric = _DvmrpRouteMetric_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 4, 1, 5),
    _DvmrpRouteMetric_Type()
)
dvmrpRouteMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteMetric.setStatus("current")
_DvmrpRouteExpiryTime_Type = TimeTicks
_DvmrpRouteExpiryTime_Object = MibTableColumn
dvmrpRouteExpiryTime = _DvmrpRouteExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 4, 1, 6),
    _DvmrpRouteExpiryTime_Type()
)
dvmrpRouteExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteExpiryTime.setStatus("current")
_DvmrpRouteUpTime_Type = TimeTicks
_DvmrpRouteUpTime_Object = MibTableColumn
dvmrpRouteUpTime = _DvmrpRouteUpTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 4, 1, 7),
    _DvmrpRouteUpTime_Type()
)
dvmrpRouteUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteUpTime.setStatus("current")
_DvmrpRouteNextHopTable_Object = MibTable
dvmrpRouteNextHopTable = _DvmrpRouteNextHopTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 5)
)
if mibBuilder.loadTexts:
    dvmrpRouteNextHopTable.setStatus("current")
_DvmrpRouteNextHopEntry_Object = MibTableRow
dvmrpRouteNextHopEntry = _DvmrpRouteNextHopEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 5, 1)
)
dvmrpRouteNextHopEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpRouteNextHopSource"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpRouteNextHopSourceMask"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpRouteNextHopIfIndex"),
)
if mibBuilder.loadTexts:
    dvmrpRouteNextHopEntry.setStatus("current")
_DvmrpRouteNextHopSource_Type = IpAddress
_DvmrpRouteNextHopSource_Object = MibTableColumn
dvmrpRouteNextHopSource = _DvmrpRouteNextHopSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 5, 1, 1),
    _DvmrpRouteNextHopSource_Type()
)
dvmrpRouteNextHopSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopSource.setStatus("current")
_DvmrpRouteNextHopSourceMask_Type = IpAddress
_DvmrpRouteNextHopSourceMask_Object = MibTableColumn
dvmrpRouteNextHopSourceMask = _DvmrpRouteNextHopSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 5, 1, 2),
    _DvmrpRouteNextHopSourceMask_Type()
)
dvmrpRouteNextHopSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopSourceMask.setStatus("current")
_DvmrpRouteNextHopIfIndex_Type = InterfaceIndex
_DvmrpRouteNextHopIfIndex_Object = MibTableColumn
dvmrpRouteNextHopIfIndex = _DvmrpRouteNextHopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 5, 1, 3),
    _DvmrpRouteNextHopIfIndex_Type()
)
dvmrpRouteNextHopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopIfIndex.setStatus("current")


class _DvmrpRouteNextHopType_Type(Integer32):
    """Custom type dvmrpRouteNextHopType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("leaf", 1),
          ("branch", 2))
    )


_DvmrpRouteNextHopType_Type.__name__ = "Integer32"
_DvmrpRouteNextHopType_Object = MibTableColumn
dvmrpRouteNextHopType = _DvmrpRouteNextHopType_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 5, 1, 4),
    _DvmrpRouteNextHopType_Type()
)
dvmrpRouteNextHopType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpRouteNextHopType.setStatus("current")
_DvmrpPruneTable_Object = MibTable
dvmrpPruneTable = _DvmrpPruneTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 6)
)
if mibBuilder.loadTexts:
    dvmrpPruneTable.setStatus("current")
_DvmrpPruneEntry_Object = MibTableRow
dvmrpPruneEntry = _DvmrpPruneEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 6, 1)
)
dvmrpPruneEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpPruneGroup"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpPruneSource"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dvmrpPruneSourceMask"),
)
if mibBuilder.loadTexts:
    dvmrpPruneEntry.setStatus("current")
_DvmrpPruneGroup_Type = IpAddress
_DvmrpPruneGroup_Object = MibTableColumn
dvmrpPruneGroup = _DvmrpPruneGroup_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 6, 1, 1),
    _DvmrpPruneGroup_Type()
)
dvmrpPruneGroup.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpPruneGroup.setStatus("current")
_DvmrpPruneSource_Type = IpAddress
_DvmrpPruneSource_Object = MibTableColumn
dvmrpPruneSource = _DvmrpPruneSource_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 6, 1, 2),
    _DvmrpPruneSource_Type()
)
dvmrpPruneSource.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpPruneSource.setStatus("current")
_DvmrpPruneSourceMask_Type = IpAddress
_DvmrpPruneSourceMask_Object = MibTableColumn
dvmrpPruneSourceMask = _DvmrpPruneSourceMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 6, 1, 3),
    _DvmrpPruneSourceMask_Type()
)
dvmrpPruneSourceMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dvmrpPruneSourceMask.setStatus("current")
_DvmrpPruneExpiryTime_Type = TimeTicks
_DvmrpPruneExpiryTime_Object = MibTableColumn
dvmrpPruneExpiryTime = _DvmrpPruneExpiryTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 4, 6, 1, 4),
    _DvmrpPruneExpiryTime_Type()
)
dvmrpPruneExpiryTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dvmrpPruneExpiryTime.setStatus("current")
_RouteMgt_ObjectIdentity = ObjectIdentity
routeMgt = _RouteMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 5)
)
_IpCidrRouteExtTable_Object = MibTable
ipCidrRouteExtTable = _IpCidrRouteExtTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 5, 2)
)
if mibBuilder.loadTexts:
    ipCidrRouteExtTable.setStatus("current")
_IpCidrRouteExtEntry_Object = MibTableRow
ipCidrRouteExtEntry = _IpCidrRouteExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 5, 2, 1)
)
ipCidrRouteExtEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ipCidrRouteExtDest"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ipCidrRouteExtMask"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ipCidrRouteExtTos"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "ipCidrRouteExtNextHop"),
)
if mibBuilder.loadTexts:
    ipCidrRouteExtEntry.setStatus("current")
_IpCidrRouteExtDest_Type = IpAddress
_IpCidrRouteExtDest_Object = MibTableColumn
ipCidrRouteExtDest = _IpCidrRouteExtDest_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 5, 2, 1, 1),
    _IpCidrRouteExtDest_Type()
)
ipCidrRouteExtDest.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCidrRouteExtDest.setStatus("current")
_IpCidrRouteExtMask_Type = IpAddress
_IpCidrRouteExtMask_Object = MibTableColumn
ipCidrRouteExtMask = _IpCidrRouteExtMask_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 5, 2, 1, 2),
    _IpCidrRouteExtMask_Type()
)
ipCidrRouteExtMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCidrRouteExtMask.setStatus("current")
_IpCidrRouteExtTos_Type = Integer32
_IpCidrRouteExtTos_Object = MibTableColumn
ipCidrRouteExtTos = _IpCidrRouteExtTos_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 5, 2, 1, 3),
    _IpCidrRouteExtTos_Type()
)
ipCidrRouteExtTos.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCidrRouteExtTos.setStatus("current")
_IpCidrRouteExtNextHop_Type = IpAddress
_IpCidrRouteExtNextHop_Object = MibTableColumn
ipCidrRouteExtNextHop = _IpCidrRouteExtNextHop_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 5, 2, 1, 4),
    _IpCidrRouteExtNextHop_Type()
)
ipCidrRouteExtNextHop.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipCidrRouteExtNextHop.setStatus("current")


class _IpCidrRouteExtOspfSubType_Type(Integer32):
    """Custom type ipCidrRouteExtOspfSubType based on Integer32"""
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
        *(("none", 1),
          ("ospfInter", 2),
          ("ospfIntra", 3),
          ("ospfNssa1", 4),
          ("ospfNssa2", 5),
          ("ospfType1", 6),
          ("ospfType2", 7))
    )


_IpCidrRouteExtOspfSubType_Type.__name__ = "Integer32"
_IpCidrRouteExtOspfSubType_Object = MibTableColumn
ipCidrRouteExtOspfSubType = _IpCidrRouteExtOspfSubType_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 18, 5, 2, 1, 5),
    _IpCidrRouteExtOspfSubType_Type()
)
ipCidrRouteExtOspfSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteExtOspfSubType.setStatus("current")
_SysLogMgt_ObjectIdentity = ObjectIdentity
sysLogMgt = _SysLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19)
)
_SysLogStatus_Type = EnabledStatus
_SysLogStatus_Object = MibScalar
sysLogStatus = _SysLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 3),
    _SysLogHistoryRamLevel_Type()
)
sysLogHistoryRamLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysLogHistoryRamLevel.setStatus("current")
_RemoteLogMgt_ObjectIdentity = ObjectIdentity
remoteLogMgt = _RemoteLogMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 6)
)
_RemoteLogStatus_Type = EnabledStatus
_RemoteLogStatus_Object = MibScalar
remoteLogStatus = _RemoteLogStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 6, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 6, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 6, 3),
    _RemoteLogFacilityType_Type()
)
remoteLogFacilityType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    remoteLogFacilityType.setStatus("current")
_RemoteLogServerTable_Object = MibTable
remoteLogServerTable = _RemoteLogServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 6, 4)
)
if mibBuilder.loadTexts:
    remoteLogServerTable.setStatus("current")
_RemoteLogServerEntry_Object = MibTableRow
remoteLogServerEntry = _RemoteLogServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 6, 4, 1)
)
remoteLogServerEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "remoteLogServerIp"),
)
if mibBuilder.loadTexts:
    remoteLogServerEntry.setStatus("current")
_RemoteLogServerIp_Type = IpAddress
_RemoteLogServerIp_Object = MibTableColumn
remoteLogServerIp = _RemoteLogServerIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 6, 4, 1, 1),
    _RemoteLogServerIp_Type()
)
remoteLogServerIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    remoteLogServerIp.setStatus("current")
_RemoteLogServerStatus_Type = ValidStatus
_RemoteLogServerStatus_Object = MibTableColumn
remoteLogServerStatus = _RemoteLogServerStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 6, 4, 1, 2),
    _RemoteLogServerStatus_Type()
)
remoteLogServerStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    remoteLogServerStatus.setStatus("current")
_SmtpMgt_ObjectIdentity = ObjectIdentity
smtpMgt = _SmtpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7)
)
_SmtpStatus_Type = EnabledStatus
_SmtpStatus_Object = MibScalar
smtpStatus = _SmtpStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 3),
    _SmtpSourceEMail_Type()
)
smtpSourceEMail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    smtpSourceEMail.setStatus("current")
_SmtpServerIpTable_Object = MibTable
smtpServerIpTable = _SmtpServerIpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 4)
)
if mibBuilder.loadTexts:
    smtpServerIpTable.setStatus("current")
_SmtpServerIpEntry_Object = MibTableRow
smtpServerIpEntry = _SmtpServerIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 4, 1)
)
smtpServerIpEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "smtpServerIp"),
)
if mibBuilder.loadTexts:
    smtpServerIpEntry.setStatus("current")
_SmtpServerIp_Type = IpAddress
_SmtpServerIp_Object = MibTableColumn
smtpServerIp = _SmtpServerIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 4, 1, 1),
    _SmtpServerIp_Type()
)
smtpServerIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    smtpServerIp.setStatus("current")
_SmtpServerIpStatus_Type = ValidStatus
_SmtpServerIpStatus_Object = MibTableColumn
smtpServerIpStatus = _SmtpServerIpStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 4, 1, 2),
    _SmtpServerIpStatus_Type()
)
smtpServerIpStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpServerIpStatus.setStatus("current")
_SmtpDestEMailTable_Object = MibTable
smtpDestEMailTable = _SmtpDestEMailTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 5)
)
if mibBuilder.loadTexts:
    smtpDestEMailTable.setStatus("current")
_SmtpDestEMailEntry_Object = MibTableRow
smtpDestEMailEntry = _SmtpDestEMailEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 5, 1)
)
smtpDestEMailEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "smtpDestEMail"),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 5, 1, 1),
    _SmtpDestEMail_Type()
)
smtpDestEMail.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    smtpDestEMail.setStatus("current")
_SmtpDestEMailStatus_Type = ValidStatus
_SmtpDestEMailStatus_Object = MibTableColumn
smtpDestEMailStatus = _SmtpDestEMailStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 19, 7, 5, 1, 2),
    _SmtpDestEMailStatus_Type()
)
smtpDestEMailStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    smtpDestEMailStatus.setStatus("current")
_LineMgt_ObjectIdentity = ObjectIdentity
lineMgt = _LineMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20)
)
_ConsoleMgt_ObjectIdentity = ObjectIdentity
consoleMgt = _ConsoleMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 1)
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 1, 7),
    _ConsoleSilentTime_Type()
)
consoleSilentTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleSilentTime.setStatus("current")
_ConsoleAdminBaudRate_Type = Integer32
_ConsoleAdminBaudRate_Object = MibScalar
consoleAdminBaudRate = _ConsoleAdminBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 1, 8),
    _ConsoleAdminBaudRate_Type()
)
consoleAdminBaudRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleAdminBaudRate.setStatus("current")
_ConsoleOperBaudRate_Type = Integer32
_ConsoleOperBaudRate_Object = MibScalar
consoleOperBaudRate = _ConsoleOperBaudRate_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 1, 9),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 1, 10),
    _ConsoleLoginResponseTimeout_Type()
)
consoleLoginResponseTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    consoleLoginResponseTimeout.setStatus("current")
_TelnetMgt_ObjectIdentity = ObjectIdentity
telnetMgt = _TelnetMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 2)
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 2, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 2, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 2, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 2, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 20, 2, 5),
    _TelnetPortNumber_Type()
)
telnetPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telnetPortNumber.setStatus("current")
_SysTimeMgt_ObjectIdentity = ObjectIdentity
sysTimeMgt = _SysTimeMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23)
)
_SntpMgt_ObjectIdentity = ObjectIdentity
sntpMgt = _SntpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 1)
)
_SntpStatus_Type = EnabledStatus
_SntpStatus_Object = MibScalar
sntpStatus = _SntpStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 1, 1),
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
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 1),
          ("broadcast", 2),
          ("anycast", 3))
    )


_SntpServiceMode_Type.__name__ = "Integer32"
_SntpServiceMode_Object = MibScalar
sntpServiceMode = _SntpServiceMode_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 1, 3),
    _SntpPollInterval_Type()
)
sntpPollInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sntpPollInterval.setStatus("current")
_SntpServerTable_Object = MibTable
sntpServerTable = _SntpServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 1, 4)
)
if mibBuilder.loadTexts:
    sntpServerTable.setStatus("current")
_SntpServerEntry_Object = MibTableRow
sntpServerEntry = _SntpServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 1, 4, 1)
)
sntpServerEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "sntpServerIndex"),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 1, 4, 1, 1),
    _SntpServerIndex_Type()
)
sntpServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    sntpServerIndex.setStatus("current")
_SntpServerIpAddress_Type = IpAddress
_SntpServerIpAddress_Object = MibTableColumn
sntpServerIpAddress = _SntpServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 1, 4, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 23, 4),
    _SysTimeZoneName_Type()
)
sysTimeZoneName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sysTimeZoneName.setStatus("current")
_FileMgt_ObjectIdentity = ObjectIdentity
fileMgt = _FileMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24)
)
_FileCopyMgt_ObjectIdentity = ObjectIdentity
fileCopyMgt = _FileCopyMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 1)
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("runningCfg", 2),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5))
    )


_FileCopySrcOperType_Type.__name__ = "Integer32"
_FileCopySrcOperType_Object = MibScalar
fileCopySrcOperType = _FileCopySrcOperType_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 1, 2),
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
              5)
        )
    )
    namedValues = NamedValues(
        *(("file", 1),
          ("runningCfg", 2),
          ("startUpCfg", 3),
          ("tftp", 4),
          ("unit", 5))
    )


_FileCopyDestOperType_Type.__name__ = "Integer32"
_FileCopyDestOperType_Object = MibScalar
fileCopyDestOperType = _FileCopyDestOperType_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 1, 3),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 1, 5),
    _FileCopyFileType_Type()
)
fileCopyFileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyFileType.setStatus("current")
_FileCopyTftpServer_Type = IpAddress
_FileCopyTftpServer_Object = MibScalar
fileCopyTftpServer = _FileCopyTftpServer_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 1, 6),
    _FileCopyTftpServer_Type()
)
fileCopyTftpServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyTftpServer.setStatus("current")
_FileCopyUnitId_Type = Integer32
_FileCopyUnitId_Object = MibScalar
fileCopyUnitId = _FileCopyUnitId_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 1, 7),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 1, 8),
    _FileCopyAction_Type()
)
fileCopyAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileCopyAction.setStatus("current")
_FileCopyStatus_Type = FileCopyStatus
_FileCopyStatus_Object = MibScalar
fileCopyStatus = _FileCopyStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 1, 9),
    _FileCopyStatus_Type()
)
fileCopyStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileCopyStatus.setStatus("current")
_FileInfoMgt_ObjectIdentity = ObjectIdentity
fileInfoMgt = _FileInfoMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 2)
)
_FileInfoTable_Object = MibTable
fileInfoTable = _FileInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 2, 1)
)
if mibBuilder.loadTexts:
    fileInfoTable.setStatus("current")
_FileInfoEntry_Object = MibTableRow
fileInfoEntry = _FileInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 2, 1, 1)
)
fileInfoEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "fileInfoUnitID"),
    (1, "Hirschmann-GIGA-LION-24TP-MIB", "fileInfoFileName"),
)
if mibBuilder.loadTexts:
    fileInfoEntry.setStatus("current")
_FileInfoUnitID_Type = Integer32
_FileInfoUnitID_Object = MibTableColumn
fileInfoUnitID = _FileInfoUnitID_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 2, 1, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 2, 1, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 2, 1, 1, 3),
    _FileInfoFileType_Type()
)
fileInfoFileType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileType.setStatus("current")
_FileInfoIsStartUp_Type = TruthValue
_FileInfoIsStartUp_Object = MibTableColumn
fileInfoIsStartUp = _FileInfoIsStartUp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 2, 1, 1, 4),
    _FileInfoIsStartUp_Type()
)
fileInfoIsStartUp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoIsStartUp.setStatus("current")
_FileInfoFileSize_Type = Integer32
_FileInfoFileSize_Object = MibTableColumn
fileInfoFileSize = _FileInfoFileSize_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 2, 1, 1, 5),
    _FileInfoFileSize_Type()
)
fileInfoFileSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileInfoFileSize.setStatus("current")


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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 2, 1, 1, 6),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 2, 1, 1, 7),
    _FileInfoDelete_Type()
)
fileInfoDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fileInfoDelete.setStatus("current")
_FileAutoDownloadResultTable_Object = MibTable
fileAutoDownloadResultTable = _FileAutoDownloadResultTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 3)
)
if mibBuilder.loadTexts:
    fileAutoDownloadResultTable.setStatus("current")
_FileAutoDownloadResultEntry_Object = MibTableRow
fileAutoDownloadResultEntry = _FileAutoDownloadResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 3, 1)
)
fileAutoDownloadResultEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "fileAutoDownloadResultUnitID"),
)
if mibBuilder.loadTexts:
    fileAutoDownloadResultEntry.setStatus("current")
_FileAutoDownloadResultUnitID_Type = Integer32
_FileAutoDownloadResultUnitID_Object = MibTableColumn
fileAutoDownloadResultUnitID = _FileAutoDownloadResultUnitID_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 3, 1, 2),
    _FileAutoDownloadResultAction_Type()
)
fileAutoDownloadResultAction.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAutoDownloadResultAction.setStatus("current")
_FileAutoDownloadResultStatus_Type = FileCopyStatus
_FileAutoDownloadResultStatus_Object = MibTableColumn
fileAutoDownloadResultStatus = _FileAutoDownloadResultStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 24, 3, 1, 3),
    _FileAutoDownloadResultStatus_Type()
)
fileAutoDownloadResultStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fileAutoDownloadResultStatus.setStatus("current")
_DnsMgt_ObjectIdentity = ObjectIdentity
dnsMgt = _DnsMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26)
)
_DnsDomainLookup_Type = EnabledStatus
_DnsDomainLookup_Object = MibScalar
dnsDomainLookup = _DnsDomainLookup_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 2),
    _DnsDomainName_Type()
)
dnsDomainName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsDomainName.setStatus("current")
_DnsHostTable_Object = MibTable
dnsHostTable = _DnsHostTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 3)
)
if mibBuilder.loadTexts:
    dnsHostTable.setStatus("current")
_DnsHostEntry_Object = MibTableRow
dnsHostEntry = _DnsHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 3, 1)
)
dnsHostEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dnsHostName"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dnsHostIndex"),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 3, 1, 1),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 3, 1, 2),
    _DnsHostIndex_Type()
)
dnsHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsHostIndex.setStatus("current")
_DnsHostIp_Type = IpAddress
_DnsHostIp_Object = MibTableColumn
dnsHostIp = _DnsHostIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 3, 1, 3),
    _DnsHostIp_Type()
)
dnsHostIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsHostIp.setStatus("current")
_DnsAliasTable_Object = MibTable
dnsAliasTable = _DnsAliasTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 4)
)
if mibBuilder.loadTexts:
    dnsAliasTable.setStatus("current")
_DnsAliasEntry_Object = MibTableRow
dnsAliasEntry = _DnsAliasEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 4, 1)
)
dnsAliasEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dnsAliasName"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dnaAliasAlias"),
)
if mibBuilder.loadTexts:
    dnsAliasEntry.setStatus("current")


class _DnsAliasName_Type(DisplayString):
    """Custom type dnsAliasName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnsAliasName_Type.__name__ = "DisplayString"
_DnsAliasName_Object = MibTableColumn
dnsAliasName = _DnsAliasName_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 4, 1, 1),
    _DnsAliasName_Type()
)
dnsAliasName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsAliasName.setStatus("current")


class _DnaAliasAlias_Type(DisplayString):
    """Custom type dnaAliasAlias based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DnaAliasAlias_Type.__name__ = "DisplayString"
_DnaAliasAlias_Object = MibTableColumn
dnaAliasAlias = _DnaAliasAlias_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 4, 1, 2),
    _DnaAliasAlias_Type()
)
dnaAliasAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnaAliasAlias.setStatus("current")
_DnsDomainListTable_Object = MibTable
dnsDomainListTable = _DnsDomainListTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 5)
)
if mibBuilder.loadTexts:
    dnsDomainListTable.setStatus("current")
_DnsDomainListEntry_Object = MibTableRow
dnsDomainListEntry = _DnsDomainListEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 5, 1)
)
dnsDomainListEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dnsDomainListName"),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 5, 1, 1),
    _DnsDomainListName_Type()
)
dnsDomainListName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsDomainListName.setStatus("current")
_DnsDomainListStatus_Type = ValidStatus
_DnsDomainListStatus_Object = MibTableColumn
dnsDomainListStatus = _DnsDomainListStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 5, 1, 2),
    _DnsDomainListStatus_Type()
)
dnsDomainListStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    dnsDomainListStatus.setStatus("current")
_DnsNameServerTable_Object = MibTable
dnsNameServerTable = _DnsNameServerTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 6)
)
if mibBuilder.loadTexts:
    dnsNameServerTable.setStatus("current")
_DnsNameServerEntry_Object = MibTableRow
dnsNameServerEntry = _DnsNameServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 6, 1)
)
dnsNameServerEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dnsNameServerIndex"),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 6, 1, 1),
    _DnsNameServerIndex_Type()
)
dnsNameServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsNameServerIndex.setStatus("current")
_DnsNameServerIp_Type = IpAddress
_DnsNameServerIp_Object = MibTableColumn
dnsNameServerIp = _DnsNameServerIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 6, 1, 2),
    _DnsNameServerIp_Type()
)
dnsNameServerIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dnsNameServerIp.setStatus("current")
_DnsCacheTable_Object = MibTable
dnsCacheTable = _DnsCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 7)
)
if mibBuilder.loadTexts:
    dnsCacheTable.setStatus("current")
_DnsCacheEntry_Object = MibTableRow
dnsCacheEntry = _DnsCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 7, 1)
)
dnsCacheEntry.setIndexNames(
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "dnsCacheIndex"),
)
if mibBuilder.loadTexts:
    dnsCacheEntry.setStatus("current")
_DnsCacheIndex_Type = Integer32
_DnsCacheIndex_Object = MibTableColumn
dnsCacheIndex = _DnsCacheIndex_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 7, 1, 1),
    _DnsCacheIndex_Type()
)
dnsCacheIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    dnsCacheIndex.setStatus("current")
_DnsCacheFlag_Type = Integer32
_DnsCacheFlag_Object = MibTableColumn
dnsCacheFlag = _DnsCacheFlag_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 7, 1, 2),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 7, 1, 3),
    _DnsCacheType_Type()
)
dnsCacheType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheType.setStatus("current")
_DnsCacheIp_Type = IpAddress
_DnsCacheIp_Object = MibTableColumn
dnsCacheIp = _DnsCacheIp_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 7, 1, 4),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 7, 1, 5),
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
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 26, 7, 1, 6),
    _DnsCacheDomain_Type()
)
dnsCacheDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    dnsCacheDomain.setStatus("current")
_HsrpMgt_ObjectIdentity = ObjectIdentity
hsrpMgt = _HsrpMgt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29)
)
_CHsrpGlobalConfig_ObjectIdentity = ObjectIdentity
cHsrpGlobalConfig = _CHsrpGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 1)
)


class _CHsrpConfigTimeout_Type(Unsigned32):
    """Custom type cHsrpConfigTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_CHsrpConfigTimeout_Type.__name__ = "Unsigned32"
_CHsrpConfigTimeout_Object = MibScalar
cHsrpConfigTimeout = _CHsrpConfigTimeout_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 1, 1),
    _CHsrpConfigTimeout_Type()
)
cHsrpConfigTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cHsrpConfigTimeout.setStatus("current")
_CHsrpGroup_ObjectIdentity = ObjectIdentity
cHsrpGroup = _CHsrpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2)
)
_CHsrpGrpTable_Object = MibTable
cHsrpGrpTable = _CHsrpGrpTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1)
)
if mibBuilder.loadTexts:
    cHsrpGrpTable.setStatus("current")
_CHsrpGrpEntry_Object = MibTableRow
cHsrpGrpEntry = _CHsrpGrpEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1)
)
cHsrpGrpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "cHsrpGrpNumber"),
)
if mibBuilder.loadTexts:
    cHsrpGrpEntry.setStatus("current")


class _CHsrpGrpNumber_Type(Unsigned32):
    """Custom type cHsrpGrpNumber based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CHsrpGrpNumber_Type.__name__ = "Unsigned32"
_CHsrpGrpNumber_Object = MibTableColumn
cHsrpGrpNumber = _CHsrpGrpNumber_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 1),
    _CHsrpGrpNumber_Type()
)
cHsrpGrpNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cHsrpGrpNumber.setStatus("current")


class _CHsrpGrpAuth_Type(DisplayString):
    """Custom type cHsrpGrpAuth based on DisplayString"""
    defaultValue = OctetString("cisco")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 8),
    )


_CHsrpGrpAuth_Type.__name__ = "DisplayString"
_CHsrpGrpAuth_Object = MibTableColumn
cHsrpGrpAuth = _CHsrpGrpAuth_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 2),
    _CHsrpGrpAuth_Type()
)
cHsrpGrpAuth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpAuth.setStatus("current")


class _CHsrpGrpPriority_Type(Unsigned32):
    """Custom type cHsrpGrpPriority based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CHsrpGrpPriority_Type.__name__ = "Unsigned32"
_CHsrpGrpPriority_Object = MibTableColumn
cHsrpGrpPriority = _CHsrpGrpPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 3),
    _CHsrpGrpPriority_Type()
)
cHsrpGrpPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpPriority.setStatus("current")


class _CHsrpGrpPreempt_Type(TruthValue):
    """Custom type cHsrpGrpPreempt based on TruthValue"""
    defaultValue = 2


_CHsrpGrpPreempt_Type.__name__ = "TruthValue"
_CHsrpGrpPreempt_Object = MibTableColumn
cHsrpGrpPreempt = _CHsrpGrpPreempt_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 4),
    _CHsrpGrpPreempt_Type()
)
cHsrpGrpPreempt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpPreempt.setStatus("current")


class _CHsrpGrpPreemptDelay_Type(Unsigned32):
    """Custom type cHsrpGrpPreemptDelay based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_CHsrpGrpPreemptDelay_Type.__name__ = "Unsigned32"
_CHsrpGrpPreemptDelay_Object = MibTableColumn
cHsrpGrpPreemptDelay = _CHsrpGrpPreemptDelay_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 5),
    _CHsrpGrpPreemptDelay_Type()
)
cHsrpGrpPreemptDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpPreemptDelay.setStatus("current")
_CHsrpGrpUseConfiguredTimers_Type = TruthValue
_CHsrpGrpUseConfiguredTimers_Object = MibTableColumn
cHsrpGrpUseConfiguredTimers = _CHsrpGrpUseConfiguredTimers_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 6),
    _CHsrpGrpUseConfiguredTimers_Type()
)
cHsrpGrpUseConfiguredTimers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpUseConfiguredTimers.setStatus("current")


class _CHsrpGrpConfiguredHelloTime_Type(Unsigned32):
    """Custom type cHsrpGrpConfiguredHelloTime based on Unsigned32"""
    defaultValue = 3000


_CHsrpGrpConfiguredHelloTime_Type.__name__ = "Unsigned32"
_CHsrpGrpConfiguredHelloTime_Object = MibTableColumn
cHsrpGrpConfiguredHelloTime = _CHsrpGrpConfiguredHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 7),
    _CHsrpGrpConfiguredHelloTime_Type()
)
cHsrpGrpConfiguredHelloTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpConfiguredHelloTime.setStatus("current")


class _CHsrpGrpConfiguredHoldTime_Type(Unsigned32):
    """Custom type cHsrpGrpConfiguredHoldTime based on Unsigned32"""
    defaultValue = 10000


_CHsrpGrpConfiguredHoldTime_Type.__name__ = "Unsigned32"
_CHsrpGrpConfiguredHoldTime_Object = MibTableColumn
cHsrpGrpConfiguredHoldTime = _CHsrpGrpConfiguredHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 8),
    _CHsrpGrpConfiguredHoldTime_Type()
)
cHsrpGrpConfiguredHoldTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpConfiguredHoldTime.setStatus("current")


class _CHsrpGrpLearnedHelloTime_Type(Unsigned32):
    """Custom type cHsrpGrpLearnedHelloTime based on Unsigned32"""
    defaultValue = 3000


_CHsrpGrpLearnedHelloTime_Type.__name__ = "Unsigned32"
_CHsrpGrpLearnedHelloTime_Object = MibTableColumn
cHsrpGrpLearnedHelloTime = _CHsrpGrpLearnedHelloTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 9),
    _CHsrpGrpLearnedHelloTime_Type()
)
cHsrpGrpLearnedHelloTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpLearnedHelloTime.setStatus("current")


class _CHsrpGrpLearnedHoldTime_Type(Unsigned32):
    """Custom type cHsrpGrpLearnedHoldTime based on Unsigned32"""
    defaultValue = 10000


_CHsrpGrpLearnedHoldTime_Type.__name__ = "Unsigned32"
_CHsrpGrpLearnedHoldTime_Object = MibTableColumn
cHsrpGrpLearnedHoldTime = _CHsrpGrpLearnedHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 10),
    _CHsrpGrpLearnedHoldTime_Type()
)
cHsrpGrpLearnedHoldTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpLearnedHoldTime.setStatus("current")


class _CHsrpGrpVirtualIpAddr_Type(IpAddress):
    """Custom type cHsrpGrpVirtualIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_CHsrpGrpVirtualIpAddr_Type.__name__ = "IpAddress"
_CHsrpGrpVirtualIpAddr_Object = MibTableColumn
cHsrpGrpVirtualIpAddr = _CHsrpGrpVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 11),
    _CHsrpGrpVirtualIpAddr_Type()
)
cHsrpGrpVirtualIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpVirtualIpAddr.setStatus("current")
_CHsrpGrpUseConfigVirtualIpAddr_Type = TruthValue
_CHsrpGrpUseConfigVirtualIpAddr_Object = MibTableColumn
cHsrpGrpUseConfigVirtualIpAddr = _CHsrpGrpUseConfigVirtualIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 12),
    _CHsrpGrpUseConfigVirtualIpAddr_Type()
)
cHsrpGrpUseConfigVirtualIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpUseConfigVirtualIpAddr.setStatus("current")
_CHsrpGrpActiveRouter_Type = IpAddress
_CHsrpGrpActiveRouter_Object = MibTableColumn
cHsrpGrpActiveRouter = _CHsrpGrpActiveRouter_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 13),
    _CHsrpGrpActiveRouter_Type()
)
cHsrpGrpActiveRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpActiveRouter.setStatus("current")
_CHsrpGrpStandbyRouter_Type = IpAddress
_CHsrpGrpStandbyRouter_Object = MibTableColumn
cHsrpGrpStandbyRouter = _CHsrpGrpStandbyRouter_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 14),
    _CHsrpGrpStandbyRouter_Type()
)
cHsrpGrpStandbyRouter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpStandbyRouter.setStatus("current")
_CHsrpGrpStandbyState_Type = HsrpState
_CHsrpGrpStandbyState_Object = MibTableColumn
cHsrpGrpStandbyState = _CHsrpGrpStandbyState_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 15),
    _CHsrpGrpStandbyState_Type()
)
cHsrpGrpStandbyState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpStandbyState.setStatus("current")
_CHsrpGrpVirtualMacAddr_Type = MacAddress
_CHsrpGrpVirtualMacAddr_Object = MibTableColumn
cHsrpGrpVirtualMacAddr = _CHsrpGrpVirtualMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 16),
    _CHsrpGrpVirtualMacAddr_Type()
)
cHsrpGrpVirtualMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cHsrpGrpVirtualMacAddr.setStatus("current")
_CHsrpGrpEntryRowStatus_Type = RowStatus
_CHsrpGrpEntryRowStatus_Object = MibTableColumn
cHsrpGrpEntryRowStatus = _CHsrpGrpEntryRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 2, 1, 1, 17),
    _CHsrpGrpEntryRowStatus_Type()
)
cHsrpGrpEntryRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpGrpEntryRowStatus.setStatus("current")
_CHsrpExtGroup_ObjectIdentity = ObjectIdentity
cHsrpExtGroup = _CHsrpExtGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 3)
)
_CHsrpExtIfTrackedTable_Object = MibTable
cHsrpExtIfTrackedTable = _CHsrpExtIfTrackedTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 3, 1)
)
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedTable.setStatus("current")
_CHsrpExtIfTrackedEntry_Object = MibTableRow
cHsrpExtIfTrackedEntry = _CHsrpExtIfTrackedEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 3, 1, 1)
)
cHsrpExtIfTrackedEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "cHsrpGrpNumber"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "cHsrpExtIfTracked"),
)
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedEntry.setStatus("current")
_CHsrpExtIfTracked_Type = InterfaceIndex
_CHsrpExtIfTracked_Object = MibTableColumn
cHsrpExtIfTracked = _CHsrpExtIfTracked_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 3, 1, 1, 1),
    _CHsrpExtIfTracked_Type()
)
cHsrpExtIfTracked.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cHsrpExtIfTracked.setStatus("current")


class _CHsrpExtIfTrackedPriority_Type(Unsigned32):
    """Custom type cHsrpExtIfTrackedPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_CHsrpExtIfTrackedPriority_Type.__name__ = "Unsigned32"
_CHsrpExtIfTrackedPriority_Object = MibTableColumn
cHsrpExtIfTrackedPriority = _CHsrpExtIfTrackedPriority_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 3, 1, 1, 2),
    _CHsrpExtIfTrackedPriority_Type()
)
cHsrpExtIfTrackedPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedPriority.setStatus("current")
_CHsrpExtIfTrackedRowStatus_Type = RowStatus
_CHsrpExtIfTrackedRowStatus_Object = MibTableColumn
cHsrpExtIfTrackedRowStatus = _CHsrpExtIfTrackedRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 3, 1, 1, 3),
    _CHsrpExtIfTrackedRowStatus_Type()
)
cHsrpExtIfTrackedRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtIfTrackedRowStatus.setStatus("current")
_CHsrpExtSecAddrTable_Object = MibTable
cHsrpExtSecAddrTable = _CHsrpExtSecAddrTable_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 3, 2)
)
if mibBuilder.loadTexts:
    cHsrpExtSecAddrTable.setStatus("current")
_CHsrpExtSecAddrEntry_Object = MibTableRow
cHsrpExtSecAddrEntry = _CHsrpExtSecAddrEntry_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 3, 2, 1)
)
cHsrpExtSecAddrEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "cHsrpGrpNumber"),
    (0, "Hirschmann-GIGA-LION-24TP-MIB", "cHsrpExtSecAddrAddress"),
)
if mibBuilder.loadTexts:
    cHsrpExtSecAddrEntry.setStatus("current")
_CHsrpExtSecAddrAddress_Type = IpAddress
_CHsrpExtSecAddrAddress_Object = MibTableColumn
cHsrpExtSecAddrAddress = _CHsrpExtSecAddrAddress_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 3, 2, 1, 1),
    _CHsrpExtSecAddrAddress_Type()
)
cHsrpExtSecAddrAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    cHsrpExtSecAddrAddress.setStatus("current")
_CHsrpExtSecAddrRowStatus_Type = RowStatus
_CHsrpExtSecAddrRowStatus_Object = MibTableColumn
cHsrpExtSecAddrRowStatus = _CHsrpExtSecAddrRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 1, 29, 3, 2, 1, 2),
    _CHsrpExtSecAddrRowStatus_Type()
)
cHsrpExtSecAddrRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    cHsrpExtSecAddrRowStatus.setStatus("current")
_Lion24tpNotifications_ObjectIdentity = ObjectIdentity
lion24tpNotifications = _Lion24tpNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2)
)
_Lion24tpTraps_ObjectIdentity = ObjectIdentity
lion24tpTraps = _Lion24tpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1)
)
_Lion24tpTrapsPrefix_ObjectIdentity = ObjectIdentity
lion24tpTrapsPrefix = _Lion24tpTrapsPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0)
)
_Lion24tpConformance_ObjectIdentity = ObjectIdentity
lion24tpConformance = _Lion24tpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 3)
)
dot1dStpPortEntry.registerAugmentions(
    ("Hirschmann-GIGA-LION-24TP-MIB",
     "staPortEntry")
)
staPortEntry.setIndexNames(*dot1dStpPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects

swPowerStatusChangeTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 1)
)
swPowerStatusChangeTrap.setObjects(
      *(("Hirschmann-GIGA-LION-24TP-MIB", "swIndivPowerUnitIndex"),
        ("Hirschmann-GIGA-LION-24TP-MIB", "swIndivPowerIndex"),
        ("Hirschmann-GIGA-LION-24TP-MIB", "swIndivPowerStatus"))
)
if mibBuilder.loadTexts:
    swPowerStatusChangeTrap.setStatus(
        "current"
    )

swFanFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 17)
)
swFanFailureTrap.setObjects(
      *(("Hirschmann-GIGA-LION-24TP-MIB", "switchUnitIndex"),
        ("Hirschmann-GIGA-LION-24TP-MIB", "switchFanIndex"))
)
if mibBuilder.loadTexts:
    swFanFailureTrap.setStatus(
        "current"
    )

swFanRecoverTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 18)
)
swFanRecoverTrap.setObjects(
      *(("Hirschmann-GIGA-LION-24TP-MIB", "switchUnitIndex"),
        ("Hirschmann-GIGA-LION-24TP-MIB", "switchFanIndex"))
)
if mibBuilder.loadTexts:
    swFanRecoverTrap.setStatus(
        "current"
    )

swIpFilterRejectTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 40)
)
swIpFilterRejectTrap.setObjects(
      *(("Hirschmann-GIGA-LION-24TP-MIB", "trapIpFilterRejectMode"),
        ("Hirschmann-GIGA-LION-24TP-MIB", "trapIpFilterRejectIp"))
)
if mibBuilder.loadTexts:
    swIpFilterRejectTrap.setStatus(
        "current"
    )

swSmtpConnFailureTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 41)
)
swSmtpConnFailureTrap.setObjects(
    ("Hirschmann-GIGA-LION-24TP-MIB", "smtpServerIp")
)
if mibBuilder.loadTexts:
    swSmtpConnFailureTrap.setStatus(
        "current"
    )

swMainBoardVerMismatchNotificaiton = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 56)
)
swMainBoardVerMismatchNotificaiton.setObjects(
      *(("Hirschmann-GIGA-LION-24TP-MIB", "swOpCodeVer"),
        ("Hirschmann-GIGA-LION-24TP-MIB", "swOpCodeVer"))
)
if mibBuilder.loadTexts:
    swMainBoardVerMismatchNotificaiton.setStatus(
        "current"
    )

swModuleVerMismatchNotificaiton = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 57)
)
swModuleVerMismatchNotificaiton.setObjects(
      *(("Hirschmann-GIGA-LION-24TP-MIB", "swExpectedModuleOpCodeVer"),
        ("Hirschmann-GIGA-LION-24TP-MIB", "swModuleOpCodeVer"))
)
if mibBuilder.loadTexts:
    swModuleVerMismatchNotificaiton.setStatus(
        "current"
    )

swThermalRisingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 58)
)
swThermalRisingNotification.setObjects(
      *(("Hirschmann-GIGA-LION-24TP-MIB", "switchThermalTempValue"),
        ("Hirschmann-GIGA-LION-24TP-MIB", "switchThermalActionRisingThreshold"))
)
if mibBuilder.loadTexts:
    swThermalRisingNotification.setStatus(
        "current"
    )

swThermalFallingNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 59)
)
swThermalFallingNotification.setObjects(
      *(("Hirschmann-GIGA-LION-24TP-MIB", "switchThermalTempValue"),
        ("Hirschmann-GIGA-LION-24TP-MIB", "switchThermalActionFallingThreshold"))
)
if mibBuilder.loadTexts:
    swThermalFallingNotification.setStatus(
        "current"
    )

swModuleInsertionNotificaiton = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 60)
)
swModuleInsertionNotificaiton.setObjects(
    ("Hirschmann-GIGA-LION-24TP-MIB", "swModuleOpCodeVer")
)
if mibBuilder.loadTexts:
    swModuleInsertionNotificaiton.setStatus(
        "current"
    )

swModuleRemovalNotificaiton = NotificationType(
    (1, 3, 6, 1, 4, 1, 248, 13, 7, 5, 2, 1, 0, 61)
)
swModuleRemovalNotificaiton.setObjects(
    ("Hirschmann-GIGA-LION-24TP-MIB", "swModuleOpCodeVer")
)
if mibBuilder.loadTexts:
    swModuleRemovalNotificaiton.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "Hirschmann-GIGA-LION-24TP-MIB",
    **{"OspfAreaID": OspfAreaID,
       "OspfBigMetric": OspfBigMetric,
       "KeySegment": KeySegment,
       "ValidStatus": ValidStatus,
       "HsrpState": HsrpState,
       "StaPathCostMode": StaPathCostMode,
       "FileCopyStatus": FileCopyStatus,
       "hiway": hiway,
       "fastEtherSwitch24": fastEtherSwitch24,
       "gigaLion24tpMIB": gigaLion24tpMIB,
       "lion24tpMIBObjects": lion24tpMIBObjects,
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
       "swExpansionSlot1": swExpansionSlot1,
       "swExpansionSlot2": swExpansionSlot2,
       "swServiceTag": swServiceTag,
       "swModelNumber": swModelNumber,
       "swEpldVer": swEpldVer,
       "swExpectedModuleOpCodeVer": swExpectedModuleOpCodeVer,
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
       "switchFanTable": switchFanTable,
       "switchFanEntry": switchFanEntry,
       "switchUnitIndex": switchUnitIndex,
       "switchFanIndex": switchFanIndex,
       "switchFanStatus": switchFanStatus,
       "switchFanAdminSpeed": switchFanAdminSpeed,
       "switchFanFailureCount": switchFanFailureCount,
       "switchFanOperSpeed": switchFanOperSpeed,
       "switchThermalTempTable": switchThermalTempTable,
       "switchThermalTempEntry": switchThermalTempEntry,
       "switchThermalTempUnitIndex": switchThermalTempUnitIndex,
       "switchThermalTempThermalIndex": switchThermalTempThermalIndex,
       "switchThermalTempValue": switchThermalTempValue,
       "switchThermalActionTable": switchThermalActionTable,
       "switchThermalActionEntry": switchThermalActionEntry,
       "switchThermalActionUnitIndex": switchThermalActionUnitIndex,
       "switchThermalActionThermalIndex": switchThermalActionThermalIndex,
       "switchThermalActionIndex": switchThermalActionIndex,
       "switchThermalActionRisingThreshold": switchThermalActionRisingThreshold,
       "switchThermalActionFallingThreshold": switchThermalActionFallingThreshold,
       "switchThermalActionAction": switchThermalActionAction,
       "switchThermalActionStatus": switchThermalActionStatus,
       "switchModuleInfoTable": switchModuleInfoTable,
       "switchModuleInfoEntry": switchModuleInfoEntry,
       "swModuleUnitIndex": swModuleUnitIndex,
       "swModuleModuleIndex": swModuleModuleIndex,
       "swModuleHardwareVer": swModuleHardwareVer,
       "swModuleMicrocodeVer": swModuleMicrocodeVer,
       "swModuleLoaderVer": swModuleLoaderVer,
       "swModuleBootRomVer": swModuleBootRomVer,
       "swModuleOpCodeVer": swModuleOpCodeVer,
       "swModulePortNumber": swModulePortNumber,
       "swModuleSerialNumber": swModuleSerialNumber,
       "swModuleType": swModuleType,
       "swModuleModelNumber": swModuleModelNumber,
       "swModuleEpldVer": swModuleEpldVer,
       "swModuleDescr": swModuleDescr,
       "switchRenumberUnitID": switchRenumberUnitID,
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
       "xstInstancePortPriority": xstInstancePortPriority,
       "xstInstancePortState": xstInstancePortState,
       "xstInstancePortEnable": xstInstancePortEnable,
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
       "ipMgt": ipMgt,
       "netDefaultGateway": netDefaultGateway,
       "ipHttpState": ipHttpState,
       "ipHttpPort": ipHttpPort,
       "ipDhcpRestart": ipDhcpRestart,
       "ipHttpsState": ipHttpsState,
       "ipHttpsPort": ipHttpsPort,
       "iPAddrTable": iPAddrTable,
       "iPAddrEntry": iPAddrEntry,
       "iPAddrIPAddress": iPAddrIPAddress,
       "iPAddrSubnetMask": iPAddrSubnetMask,
       "iPAddrIfIndex": iPAddrIfIndex,
       "iPAddrPrimaryInterface": iPAddrPrimaryInterface,
       "iPAddrUnnumbered": iPAddrUnnumbered,
       "iPAddrStatus": iPAddrStatus,
       "bcastStormMgt": bcastStormMgt,
       "bcastStormTable": bcastStormTable,
       "bcastStormEntry": bcastStormEntry,
       "bcastStormIfIndex": bcastStormIfIndex,
       "bcastStormStatus": bcastStormStatus,
       "bcastStormPktRate": bcastStormPktRate,
       "vlanMgt": vlanMgt,
       "vlanTable": vlanTable,
       "vlanEntry": vlanEntry,
       "vlanIndex": vlanIndex,
       "vlanAddressMethod": vlanAddressMethod,
       "vlanPortTable": vlanPortTable,
       "vlanPortEntry": vlanPortEntry,
       "vlanPortIndex": vlanPortIndex,
       "vlanPortMode": vlanPortMode,
       "priorityMgt": priorityMgt,
       "prioIpPrecDscpStatus": prioIpPrecDscpStatus,
       "prioIpPrecTable": prioIpPrecTable,
       "prioIpPrecEntry": prioIpPrecEntry,
       "prioIpPrecPort": prioIpPrecPort,
       "prioIpPrecValue": prioIpPrecValue,
       "prioIpPrecCos": prioIpPrecCos,
       "prioIpPrecRestoreDefault": prioIpPrecRestoreDefault,
       "prioIpDscpTable": prioIpDscpTable,
       "prioIpDscpEntry": prioIpDscpEntry,
       "prioIpDscpPort": prioIpDscpPort,
       "prioIpDscpValue": prioIpDscpValue,
       "prioIpDscpCos": prioIpDscpCos,
       "prioIpDscpRestoreDefault": prioIpDscpRestoreDefault,
       "prioIpPortEnableStatus": prioIpPortEnableStatus,
       "prioIpPortTable": prioIpPortTable,
       "prioIpPortEntry": prioIpPortEntry,
       "prioIpPortPhysPort": prioIpPortPhysPort,
       "prioIpPortValue": prioIpPortValue,
       "prioIpPortCos": prioIpPortCos,
       "prioIpPortStatus": prioIpPortStatus,
       "prioCopy": prioCopy,
       "prioCopyIpPrec": prioCopyIpPrec,
       "prioCopyIpDscp": prioCopyIpDscp,
       "prioCopyIpPort": prioCopyIpPort,
       "prioQueueMode": prioQueueMode,
       "prioWrrPortTable": prioWrrPortTable,
       "prioWrrPortEntry": prioWrrPortEntry,
       "prioWrrPortIfIndex": prioWrrPortIfIndex,
       "prioWrrPortTrafficClass": prioWrrPortTrafficClass,
       "prioWrrPortWeight": prioWrrPortWeight,
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
       "qosMgt": qosMgt,
       "rateLimitMgt": rateLimitMgt,
       "rateLimitPortTable": rateLimitPortTable,
       "rateLimitPortEntry": rateLimitPortEntry,
       "rlPortIndex": rlPortIndex,
       "rlPortInputLimit": rlPortInputLimit,
       "rlPortOutputLimit": rlPortOutputLimit,
       "rlPortInputStatus": rlPortInputStatus,
       "rlPortOutputStatus": rlPortOutputStatus,
       "markerMgt": markerMgt,
       "markerTable": markerTable,
       "markerEntry": markerEntry,
       "markerIfIndex": markerIfIndex,
       "markerAclName": markerAclName,
       "markerActionBitList": markerActionBitList,
       "markerDscp": markerDscp,
       "markerPrecedence": markerPrecedence,
       "markerPriority": markerPriority,
       "markerStatus": markerStatus,
       "cosMgt": cosMgt,
       "prioAclToCosMappingTable": prioAclToCosMappingTable,
       "prioAclToCosMappingEntry": prioAclToCosMappingEntry,
       "prioAclToCosMappingIfIndex": prioAclToCosMappingIfIndex,
       "prioAclToCosMappingAclName": prioAclToCosMappingAclName,
       "prioAclToCosMappingCosValue": prioAclToCosMappingCosValue,
       "prioAclToCosMappingStatus": prioAclToCosMappingStatus,
       "securityMgt": securityMgt,
       "privateVlanMgt": privateVlanMgt,
       "privateVlanStatus": privateVlanStatus,
       "privateVlanUplinkPorts": privateVlanUplinkPorts,
       "privateVlanDownlinkPorts": privateVlanDownlinkPorts,
       "portSecurityMgt": portSecurityMgt,
       "portSecPortTable": portSecPortTable,
       "portSecPortEntry": portSecPortEntry,
       "portSecPortIndex": portSecPortIndex,
       "portSecPortStatus": portSecPortStatus,
       "portSecAction": portSecAction,
       "portSecMaxMacCount": portSecMaxMacCount,
       "radiusMgt": radiusMgt,
       "radiusServerAddress": radiusServerAddress,
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
       "aclMgt": aclMgt,
       "aclIpAceTable": aclIpAceTable,
       "aclIpAceEntry": aclIpAceEntry,
       "aclIpAceName": aclIpAceName,
       "aclIpAceIndex": aclIpAceIndex,
       "aclIpAcePrecedence": aclIpAcePrecedence,
       "aclIpAceAction": aclIpAceAction,
       "aclIpAceSourceIpAddr": aclIpAceSourceIpAddr,
       "aclIpAceSourceIpAddrBitmask": aclIpAceSourceIpAddrBitmask,
       "aclIpAceDestIpAddr": aclIpAceDestIpAddr,
       "aclIpAceDestIpAddrBitmask": aclIpAceDestIpAddrBitmask,
       "aclIpAceProtocol": aclIpAceProtocol,
       "aclIpAcePrec": aclIpAcePrec,
       "aclIpAceTos": aclIpAceTos,
       "aclIpAceDscp": aclIpAceDscp,
       "aclIpAceSourcePortOp": aclIpAceSourcePortOp,
       "aclIpAceMinSourcePort": aclIpAceMinSourcePort,
       "aclIpAceMaxSourcePort": aclIpAceMaxSourcePort,
       "aclIpAceSourcePortBitmask": aclIpAceSourcePortBitmask,
       "aclIpAceDestPortOp": aclIpAceDestPortOp,
       "aclIpAceMinDestPort": aclIpAceMinDestPort,
       "aclIpAceMaxDestPort": aclIpAceMaxDestPort,
       "aclIpAceDestPortBitmask": aclIpAceDestPortBitmask,
       "aclIpAceControlCode": aclIpAceControlCode,
       "aclIpAceControlCodeBitmask": aclIpAceControlCodeBitmask,
       "aclIpAceStatus": aclIpAceStatus,
       "aclMacAceTable": aclMacAceTable,
       "aclMacAceEntry": aclMacAceEntry,
       "aclMacAceName": aclMacAceName,
       "aclMacAceIndex": aclMacAceIndex,
       "aclMacAcePrecedence": aclMacAcePrecedence,
       "aclMacAceAction": aclMacAceAction,
       "aclMacAcePktformat": aclMacAcePktformat,
       "aclMacAceSourceMacAddr": aclMacAceSourceMacAddr,
       "aclMacAceSourceMacAddrBitmask": aclMacAceSourceMacAddrBitmask,
       "aclMacAceDestMacAddr": aclMacAceDestMacAddr,
       "aclMacAceDestMacAddrBitmask": aclMacAceDestMacAddrBitmask,
       "aclMacAceVidOp": aclMacAceVidOp,
       "aclMacAceMinVid": aclMacAceMinVid,
       "aclMacAceVidBitmask": aclMacAceVidBitmask,
       "aclMacAceMaxVid": aclMacAceMaxVid,
       "aclMacAceEtherTypeOp": aclMacAceEtherTypeOp,
       "aclMacAceEtherTypeBitmask": aclMacAceEtherTypeBitmask,
       "aclMacAceMinEtherType": aclMacAceMinEtherType,
       "aclMacAceMaxEtherType": aclMacAceMaxEtherType,
       "aclMacAceStatus": aclMacAceStatus,
       "aclAclGroupTable": aclAclGroupTable,
       "aclAclGroupEntry": aclAclGroupEntry,
       "aclAclGroupIfIndex": aclAclGroupIfIndex,
       "aclAclGroupIngressIpAcl": aclAclGroupIngressIpAcl,
       "aclAclGroupEgressIpAcl": aclAclGroupEgressIpAcl,
       "aclAclGroupIngressMacAcl": aclAclGroupIngressMacAcl,
       "aclAclGroupEgressMacAcl": aclAclGroupEgressMacAcl,
       "aclIngressIpMaskTable": aclIngressIpMaskTable,
       "aclIngressIpMaskEntry": aclIngressIpMaskEntry,
       "aclIngressIpMaskIndex": aclIngressIpMaskIndex,
       "aclIngressIpMaskPrecedence": aclIngressIpMaskPrecedence,
       "aclIngressIpMaskIsEnableTos": aclIngressIpMaskIsEnableTos,
       "aclIngressIpMaskIsEnableDscp": aclIngressIpMaskIsEnableDscp,
       "aclIngressIpMaskIsEnablePrecedence": aclIngressIpMaskIsEnablePrecedence,
       "aclIngressIpMaskIsEnableProtocol": aclIngressIpMaskIsEnableProtocol,
       "aclIngressIpMaskSourceIpAddrBitmask": aclIngressIpMaskSourceIpAddrBitmask,
       "aclIngressIpMaskDestIpAddrBitmask": aclIngressIpMaskDestIpAddrBitmask,
       "aclIngressIpMaskSourcePortBitmask": aclIngressIpMaskSourcePortBitmask,
       "aclIngressIpMaskDestPortBitmask": aclIngressIpMaskDestPortBitmask,
       "aclIngressIpMaskControlCodeBitmask": aclIngressIpMaskControlCodeBitmask,
       "aclIngressIpMaskStatus": aclIngressIpMaskStatus,
       "aclEgressIpMaskTable": aclEgressIpMaskTable,
       "aclEgressIpMaskEntry": aclEgressIpMaskEntry,
       "aclEgressIpMaskIndex": aclEgressIpMaskIndex,
       "aclEgressIpMaskPrecedence": aclEgressIpMaskPrecedence,
       "aclEgressIpMaskIsEnableTos": aclEgressIpMaskIsEnableTos,
       "aclEgressIpMaskIsEnableDscp": aclEgressIpMaskIsEnableDscp,
       "aclEgressIpMaskIsEnablePrecedence": aclEgressIpMaskIsEnablePrecedence,
       "aclEgressIpMaskIsEnableProtocol": aclEgressIpMaskIsEnableProtocol,
       "aclEgressIpMaskSourceIpAddrBitmask": aclEgressIpMaskSourceIpAddrBitmask,
       "aclEgressIpMaskDestIpAddrBitmask": aclEgressIpMaskDestIpAddrBitmask,
       "aclEgressIpMaskSourcePortBitmask": aclEgressIpMaskSourcePortBitmask,
       "aclEgressIpMaskDestPortBitmask": aclEgressIpMaskDestPortBitmask,
       "aclEgressIpMaskControlCodeBitmask": aclEgressIpMaskControlCodeBitmask,
       "aclEgressIpMaskStatus": aclEgressIpMaskStatus,
       "aclIngressMacMaskTable": aclIngressMacMaskTable,
       "aclIngressMacMaskEntry": aclIngressMacMaskEntry,
       "aclIngressMacMaskIndex": aclIngressMacMaskIndex,
       "aclIngressMacMaskPrecedence": aclIngressMacMaskPrecedence,
       "aclIngressMacMaskSourceMacAddrBitmask": aclIngressMacMaskSourceMacAddrBitmask,
       "aclIngressMacMaskDestMacAddrBitmask": aclIngressMacMaskDestMacAddrBitmask,
       "aclIngressMacMaskVidBitmask": aclIngressMacMaskVidBitmask,
       "aclIngressMacMaskEtherTypeBitmask": aclIngressMacMaskEtherTypeBitmask,
       "aclIngressMacMaskIsEnablePktformat": aclIngressMacMaskIsEnablePktformat,
       "aclIngressMacMaskStatus": aclIngressMacMaskStatus,
       "aclEgressMacMaskTable": aclEgressMacMaskTable,
       "aclEgressMacMaskEntry": aclEgressMacMaskEntry,
       "aclEgressMacMaskIndex": aclEgressMacMaskIndex,
       "aclEgressMacMaskPrecedence": aclEgressMacMaskPrecedence,
       "aclEgressMacMaskSourceMacAddrBitmask": aclEgressMacMaskSourceMacAddrBitmask,
       "aclEgressMacMaskDestMacAddrBitmask": aclEgressMacMaskDestMacAddrBitmask,
       "aclEgressMacMaskVidBitmask": aclEgressMacMaskVidBitmask,
       "aclEgressMacMaskEtherTypeBitmask": aclEgressMacMaskEtherTypeBitmask,
       "aclEgressMacMaskIsEnablePktformat": aclEgressMacMaskIsEnablePktformat,
       "aclEgressMacMaskStatus": aclEgressMacMaskStatus,
       "aclIpTable": aclIpTable,
       "aclIpEntry": aclIpEntry,
       "aclIpAclName": aclIpAclName,
       "aclMacTable": aclMacTable,
       "aclMacEntry": aclMacEntry,
       "aclMacAclName": aclMacAclName,
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
       "layer3Mgt": layer3Mgt,
       "arpMgt": arpMgt,
       "arpCacheDeleteAll": arpCacheDeleteAll,
       "arpCacheTimeout": arpCacheTimeout,
       "arpTrafficStatistics": arpTrafficStatistics,
       "arpStatSendRequestPackets": arpStatSendRequestPackets,
       "arpStatRcvRequestPackets": arpStatRcvRequestPackets,
       "arpStatSendReplyPackets": arpStatSendReplyPackets,
       "arpStatRcvReplyPackets": arpStatRcvReplyPackets,
       "arpProxyArpTable": arpProxyArpTable,
       "arpProxyArpEntry": arpProxyArpEntry,
       "arpProxyArpIfIndex": arpProxyArpIfIndex,
       "arpProxyArpStatus": arpProxyArpStatus,
       "ripMgt": ripMgt,
       "ripTimers": ripTimers,
       "ripUpdateTime": ripUpdateTime,
       "ripTimeoutTime": ripTimeoutTime,
       "ripGarbageCollectionTime": ripGarbageCollectionTime,
       "ripRoutingProcessStatus": ripRoutingProcessStatus,
       "ripRouterVersion": ripRouterVersion,
       "ripInstabilityPreventingTable": ripInstabilityPreventingTable,
       "ripInstabilityPreventingEntry": ripInstabilityPreventingEntry,
       "ripVlanIndex": ripVlanIndex,
       "ripSplitHorizonStatus": ripSplitHorizonStatus,
       "ripStatisticsReset": ripStatisticsReset,
       "ripNetworkAddrTable": ripNetworkAddrTable,
       "ripNetworkAddrEntry": ripNetworkAddrEntry,
       "ripNetworkAddrAddress": ripNetworkAddrAddress,
       "ripNetworkAddrStatus": ripNetworkAddrStatus,
       "ospfMgt": ospfMgt,
       "ospfSystemGroup": ospfSystemGroup,
       "ospfRouterIdType": ospfRouterIdType,
       "ospfRfc1583CompatibleState": ospfRfc1583CompatibleState,
       "ospfAutoCost": ospfAutoCost,
       "ospfOriginateDefaultRoute": ospfOriginateDefaultRoute,
       "ospfAdvertiseDefaultRoute": ospfAdvertiseDefaultRoute,
       "ospfExternalMetricType": ospfExternalMetricType,
       "ospfDefaultExternalMetric": ospfDefaultExternalMetric,
       "ospfSpfHoldTime": ospfSpfHoldTime,
       "ospfSpfDelayTime": ospfSpfDelayTime,
       "ospfAreaNumber": ospfAreaNumber,
       "ospfNssaTable": ospfNssaTable,
       "ospfNssaEntry": ospfNssaEntry,
       "ospfNssaAreaId": ospfNssaAreaId,
       "ospfNssaRedistributeStatus": ospfNssaRedistributeStatus,
       "ospfNssaOriginateDefaultInfoStatus": ospfNssaOriginateDefaultInfoStatus,
       "ospfNssaStatus": ospfNssaStatus,
       "ospfRedistributeTable": ospfRedistributeTable,
       "ospfRedistributeEntry": ospfRedistributeEntry,
       "ospfRedistributeProtocol": ospfRedistributeProtocol,
       "ospfRedistributeMetricType": ospfRedistributeMetricType,
       "ospfRedistributeMetric": ospfRedistributeMetric,
       "ospfRedistributeStatus": ospfRedistributeStatus,
       "ospfSummaryAddressTable": ospfSummaryAddressTable,
       "ospfSummaryAddressEntry": ospfSummaryAddressEntry,
       "ospfSummaryAddress": ospfSummaryAddress,
       "ospfSummaryMask": ospfSummaryMask,
       "ospfSummaryStatus": ospfSummaryStatus,
       "ospfNetworkAreaAddressTable": ospfNetworkAreaAddressTable,
       "ospfNetworkAreaAddressEntry": ospfNetworkAreaAddressEntry,
       "ospfNetworkAareaAddress": ospfNetworkAareaAddress,
       "ospfNetworkAreaMask": ospfNetworkAreaMask,
       "ospfNetworkAreaAreaId": ospfNetworkAreaAreaId,
       "ospfNetworkAreaStatus": ospfNetworkAreaStatus,
       "dvmrpMgt": dvmrpMgt,
       "dvmrpScalar": dvmrpScalar,
       "dvmrpVersionString": dvmrpVersionString,
       "dvmrpNumRoutes": dvmrpNumRoutes,
       "dvmrpReachableRoutes": dvmrpReachableRoutes,
       "dvmrpInterfaceTable": dvmrpInterfaceTable,
       "dvmrpInterfaceEntry": dvmrpInterfaceEntry,
       "dvmrpInterfaceIndex": dvmrpInterfaceIndex,
       "dvmrpInterfaceLocalAddress": dvmrpInterfaceLocalAddress,
       "dvmrpInterfaceMetric": dvmrpInterfaceMetric,
       "dvmrpInterfaceStatus": dvmrpInterfaceStatus,
       "dvmrpInterfaceRcvBadPkts": dvmrpInterfaceRcvBadPkts,
       "dvmrpInterfaceRcvBadRoutes": dvmrpInterfaceRcvBadRoutes,
       "dvmrpInterfaceSentRoutes": dvmrpInterfaceSentRoutes,
       "dvmrpInterfaceKey": dvmrpInterfaceKey,
       "dvmrpInterfaceKeyVersion": dvmrpInterfaceKeyVersion,
       "dvmrpInterfaceGenerationId": dvmrpInterfaceGenerationId,
       "dvmrpNeighborTable": dvmrpNeighborTable,
       "dvmrpNeighborEntry": dvmrpNeighborEntry,
       "dvmrpNeighborIfIndex": dvmrpNeighborIfIndex,
       "dvmrpNeighborAddress": dvmrpNeighborAddress,
       "dvmrpNeighborUpTime": dvmrpNeighborUpTime,
       "dvmrpNeighborExpiryTime": dvmrpNeighborExpiryTime,
       "dvmrpNeighborGenerationId": dvmrpNeighborGenerationId,
       "dvmrpNeighborMajorVersion": dvmrpNeighborMajorVersion,
       "dvmrpNeighborMinorVersion": dvmrpNeighborMinorVersion,
       "dvmrpNeighborCapabilities": dvmrpNeighborCapabilities,
       "dvmrpNeighborRcvRoutes": dvmrpNeighborRcvRoutes,
       "dvmrpNeighborRcvBadPkts": dvmrpNeighborRcvBadPkts,
       "dvmrpNeighborRcvBadRoutes": dvmrpNeighborRcvBadRoutes,
       "dvmrpNeighborState": dvmrpNeighborState,
       "dvmrpRouteTable": dvmrpRouteTable,
       "dvmrpRouteEntry": dvmrpRouteEntry,
       "dvmrpRouteSource": dvmrpRouteSource,
       "dvmrpRouteSourceMask": dvmrpRouteSourceMask,
       "dvmrpRouteUpstreamNeighbor": dvmrpRouteUpstreamNeighbor,
       "dvmrpRouteIfIndex": dvmrpRouteIfIndex,
       "dvmrpRouteMetric": dvmrpRouteMetric,
       "dvmrpRouteExpiryTime": dvmrpRouteExpiryTime,
       "dvmrpRouteUpTime": dvmrpRouteUpTime,
       "dvmrpRouteNextHopTable": dvmrpRouteNextHopTable,
       "dvmrpRouteNextHopEntry": dvmrpRouteNextHopEntry,
       "dvmrpRouteNextHopSource": dvmrpRouteNextHopSource,
       "dvmrpRouteNextHopSourceMask": dvmrpRouteNextHopSourceMask,
       "dvmrpRouteNextHopIfIndex": dvmrpRouteNextHopIfIndex,
       "dvmrpRouteNextHopType": dvmrpRouteNextHopType,
       "dvmrpPruneTable": dvmrpPruneTable,
       "dvmrpPruneEntry": dvmrpPruneEntry,
       "dvmrpPruneGroup": dvmrpPruneGroup,
       "dvmrpPruneSource": dvmrpPruneSource,
       "dvmrpPruneSourceMask": dvmrpPruneSourceMask,
       "dvmrpPruneExpiryTime": dvmrpPruneExpiryTime,
       "routeMgt": routeMgt,
       "ipCidrRouteExtTable": ipCidrRouteExtTable,
       "ipCidrRouteExtEntry": ipCidrRouteExtEntry,
       "ipCidrRouteExtDest": ipCidrRouteExtDest,
       "ipCidrRouteExtMask": ipCidrRouteExtMask,
       "ipCidrRouteExtTos": ipCidrRouteExtTos,
       "ipCidrRouteExtNextHop": ipCidrRouteExtNextHop,
       "ipCidrRouteExtOspfSubType": ipCidrRouteExtOspfSubType,
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
       "dnsMgt": dnsMgt,
       "dnsDomainLookup": dnsDomainLookup,
       "dnsDomainName": dnsDomainName,
       "dnsHostTable": dnsHostTable,
       "dnsHostEntry": dnsHostEntry,
       "dnsHostName": dnsHostName,
       "dnsHostIndex": dnsHostIndex,
       "dnsHostIp": dnsHostIp,
       "dnsAliasTable": dnsAliasTable,
       "dnsAliasEntry": dnsAliasEntry,
       "dnsAliasName": dnsAliasName,
       "dnaAliasAlias": dnaAliasAlias,
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
       "hsrpMgt": hsrpMgt,
       "cHsrpGlobalConfig": cHsrpGlobalConfig,
       "cHsrpConfigTimeout": cHsrpConfigTimeout,
       "cHsrpGroup": cHsrpGroup,
       "cHsrpGrpTable": cHsrpGrpTable,
       "cHsrpGrpEntry": cHsrpGrpEntry,
       "cHsrpGrpNumber": cHsrpGrpNumber,
       "cHsrpGrpAuth": cHsrpGrpAuth,
       "cHsrpGrpPriority": cHsrpGrpPriority,
       "cHsrpGrpPreempt": cHsrpGrpPreempt,
       "cHsrpGrpPreemptDelay": cHsrpGrpPreemptDelay,
       "cHsrpGrpUseConfiguredTimers": cHsrpGrpUseConfiguredTimers,
       "cHsrpGrpConfiguredHelloTime": cHsrpGrpConfiguredHelloTime,
       "cHsrpGrpConfiguredHoldTime": cHsrpGrpConfiguredHoldTime,
       "cHsrpGrpLearnedHelloTime": cHsrpGrpLearnedHelloTime,
       "cHsrpGrpLearnedHoldTime": cHsrpGrpLearnedHoldTime,
       "cHsrpGrpVirtualIpAddr": cHsrpGrpVirtualIpAddr,
       "cHsrpGrpUseConfigVirtualIpAddr": cHsrpGrpUseConfigVirtualIpAddr,
       "cHsrpGrpActiveRouter": cHsrpGrpActiveRouter,
       "cHsrpGrpStandbyRouter": cHsrpGrpStandbyRouter,
       "cHsrpGrpStandbyState": cHsrpGrpStandbyState,
       "cHsrpGrpVirtualMacAddr": cHsrpGrpVirtualMacAddr,
       "cHsrpGrpEntryRowStatus": cHsrpGrpEntryRowStatus,
       "cHsrpExtGroup": cHsrpExtGroup,
       "cHsrpExtIfTrackedTable": cHsrpExtIfTrackedTable,
       "cHsrpExtIfTrackedEntry": cHsrpExtIfTrackedEntry,
       "cHsrpExtIfTracked": cHsrpExtIfTracked,
       "cHsrpExtIfTrackedPriority": cHsrpExtIfTrackedPriority,
       "cHsrpExtIfTrackedRowStatus": cHsrpExtIfTrackedRowStatus,
       "cHsrpExtSecAddrTable": cHsrpExtSecAddrTable,
       "cHsrpExtSecAddrEntry": cHsrpExtSecAddrEntry,
       "cHsrpExtSecAddrAddress": cHsrpExtSecAddrAddress,
       "cHsrpExtSecAddrRowStatus": cHsrpExtSecAddrRowStatus,
       "lion24tpNotifications": lion24tpNotifications,
       "lion24tpTraps": lion24tpTraps,
       "lion24tpTrapsPrefix": lion24tpTrapsPrefix,
       "swPowerStatusChangeTrap": swPowerStatusChangeTrap,
       "swFanFailureTrap": swFanFailureTrap,
       "swFanRecoverTrap": swFanRecoverTrap,
       "swIpFilterRejectTrap": swIpFilterRejectTrap,
       "swSmtpConnFailureTrap": swSmtpConnFailureTrap,
       "swMainBoardVerMismatchNotificaiton": swMainBoardVerMismatchNotificaiton,
       "swModuleVerMismatchNotificaiton": swModuleVerMismatchNotificaiton,
       "swThermalRisingNotification": swThermalRisingNotification,
       "swThermalFallingNotification": swThermalFallingNotification,
       "swModuleInsertionNotificaiton": swModuleInsertionNotificaiton,
       "swModuleRemovalNotificaiton": swModuleRemovalNotificaiton,
       "lion24tpConformance": lion24tpConformance}
)
