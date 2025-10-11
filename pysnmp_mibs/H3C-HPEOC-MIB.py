# SNMP MIB module (H3C-HPEOC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-HPEOC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:46 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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

h3cHPEOC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cHPEOCSystem_ObjectIdentity = ObjectIdentity
h3cHPEOCSystem = _H3cHPEOCSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1)
)


class _H3cHPEOCCltVlanType_Type(Integer32):
    """Custom type h3cHPEOCCltVlanType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ieee8021q", 1),
          ("portbased", 2))
    )


_H3cHPEOCCltVlanType_Type.__name__ = "Integer32"
_H3cHPEOCCltVlanType_Object = MibScalar
h3cHPEOCCltVlanType = _H3cHPEOCCltVlanType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 1),
    _H3cHPEOCCltVlanType_Type()
)
h3cHPEOCCltVlanType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltVlanType.setStatus("current")
_H3cHPEOCCltVlanManTable_Object = MibTable
h3cHPEOCCltVlanManTable = _H3cHPEOCCltVlanManTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 2)
)
if mibBuilder.loadTexts:
    h3cHPEOCCltVlanManTable.setStatus("current")
_H3cHPEOCCltVlanManEntry_Object = MibTableRow
h3cHPEOCCltVlanManEntry = _H3cHPEOCCltVlanManEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 2, 1)
)
h3cHPEOCCltVlanManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCCltVlanManEntry.setStatus("current")


class _H3cHPEOCCltEthPortType_Type(Integer32):
    """Custom type h3cHPEOCCltEthPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("debug", 2))
    )


_H3cHPEOCCltEthPortType_Type.__name__ = "Integer32"
_H3cHPEOCCltEthPortType_Object = MibTableColumn
h3cHPEOCCltEthPortType = _H3cHPEOCCltEthPortType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 2, 1, 1),
    _H3cHPEOCCltEthPortType_Type()
)
h3cHPEOCCltEthPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltEthPortType.setStatus("current")
_H3cHPEOCCltSysManTable_Object = MibTable
h3cHPEOCCltSysManTable = _H3cHPEOCCltSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 3)
)
if mibBuilder.loadTexts:
    h3cHPEOCCltSysManTable.setStatus("current")
_H3cHPEOCCltSysManEntry_Object = MibTableRow
h3cHPEOCCltSysManEntry = _H3cHPEOCCltSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 3, 1)
)
h3cHPEOCCltSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCCltSysManEntry.setStatus("current")


class _H3cHPEOCCltDescr_Type(DisplayString):
    """Custom type h3cHPEOCCltDescr based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 126),
    )


_H3cHPEOCCltDescr_Type.__name__ = "DisplayString"
_H3cHPEOCCltDescr_Object = MibTableColumn
h3cHPEOCCltDescr = _H3cHPEOCCltDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 3, 1, 1),
    _H3cHPEOCCltDescr_Type()
)
h3cHPEOCCltDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltDescr.setStatus("current")
_H3cHPEOCCltFwVersion_Type = DisplayString
_H3cHPEOCCltFwVersion_Object = MibTableColumn
h3cHPEOCCltFwVersion = _H3cHPEOCCltFwVersion_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 3, 1, 2),
    _H3cHPEOCCltFwVersion_Type()
)
h3cHPEOCCltFwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCCltFwVersion.setStatus("current")


class _H3cHPEOCCltLinkState_Type(Integer32):
    """Custom type h3cHPEOCCltLinkState based on Integer32"""
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
        *(("physicaldown", 1),
          ("linkdown", 2),
          ("linkup", 3),
          ("loopback", 4))
    )


_H3cHPEOCCltLinkState_Type.__name__ = "Integer32"
_H3cHPEOCCltLinkState_Object = MibTableColumn
h3cHPEOCCltLinkState = _H3cHPEOCCltLinkState_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 3, 1, 3),
    _H3cHPEOCCltLinkState_Type()
)
h3cHPEOCCltLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCCltLinkState.setStatus("current")
_H3cHPEOCCnuSysManTable_Object = MibTable
h3cHPEOCCnuSysManTable = _H3cHPEOCCnuSysManTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 4)
)
if mibBuilder.loadTexts:
    h3cHPEOCCnuSysManTable.setStatus("current")
_H3cHPEOCCnuSysManEntry_Object = MibTableRow
h3cHPEOCCnuSysManEntry = _H3cHPEOCCnuSysManEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 4, 1)
)
h3cHPEOCCnuSysManEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCCnuSysManEntry.setStatus("current")
_H3cHPEOCCnuBcastControl_Type = TruthValue
_H3cHPEOCCnuBcastControl_Object = MibTableColumn
h3cHPEOCCnuBcastControl = _H3cHPEOCCnuBcastControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 4, 1, 1),
    _H3cHPEOCCnuBcastControl_Type()
)
h3cHPEOCCnuBcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCnuBcastControl.setStatus("current")
_H3cHPEOCCnuAnonymStatus_Type = TruthValue
_H3cHPEOCCnuAnonymStatus_Object = MibTableColumn
h3cHPEOCCnuAnonymStatus = _H3cHPEOCCnuAnonymStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 4, 1, 2),
    _H3cHPEOCCnuAnonymStatus_Type()
)
h3cHPEOCCnuAnonymStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCCnuAnonymStatus.setStatus("current")
_H3cHPEOCCnuMacLimit_Type = Unsigned32
_H3cHPEOCCnuMacLimit_Object = MibTableColumn
h3cHPEOCCnuMacLimit = _H3cHPEOCCnuMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 4, 1, 3),
    _H3cHPEOCCnuMacLimit_Type()
)
h3cHPEOCCnuMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCnuMacLimit.setStatus("current")


class _H3cHPEOCCltAutoUpgrade_Type(TruthValue):
    """Custom type h3cHPEOCCltAutoUpgrade based on TruthValue"""
    defaultValue = 2


_H3cHPEOCCltAutoUpgrade_Type.__name__ = "TruthValue"
_H3cHPEOCCltAutoUpgrade_Object = MibScalar
h3cHPEOCCltAutoUpgrade = _H3cHPEOCCltAutoUpgrade_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 5),
    _H3cHPEOCCltAutoUpgrade_Type()
)
h3cHPEOCCltAutoUpgrade.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltAutoUpgrade.setStatus("current")
_H3cHPEOCOnLineCnuNumber_Type = Integer32
_H3cHPEOCOnLineCnuNumber_Object = MibScalar
h3cHPEOCOnLineCnuNumber = _H3cHPEOCOnLineCnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 6),
    _H3cHPEOCOnLineCnuNumber_Type()
)
h3cHPEOCOnLineCnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCOnLineCnuNumber.setStatus("current")
_H3cHPEOCCpuMacAddress_Type = MacAddress
_H3cHPEOCCpuMacAddress_Object = MibScalar
h3cHPEOCCpuMacAddress = _H3cHPEOCCpuMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 7),
    _H3cHPEOCCpuMacAddress_Type()
)
h3cHPEOCCpuMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCCpuMacAddress.setStatus("current")
_H3cHPEOCOffLineCnuNumber_Type = Integer32
_H3cHPEOCOffLineCnuNumber_Object = MibScalar
h3cHPEOCOffLineCnuNumber = _H3cHPEOCOffLineCnuNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 8),
    _H3cHPEOCOffLineCnuNumber_Type()
)
h3cHPEOCOffLineCnuNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCOffLineCnuNumber.setStatus("current")
_H3cHPEOCDownLoadCNUFWResult_Type = DisplayString
_H3cHPEOCDownLoadCNUFWResult_Object = MibScalar
h3cHPEOCDownLoadCNUFWResult = _H3cHPEOCDownLoadCNUFWResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 9),
    _H3cHPEOCDownLoadCNUFWResult_Type()
)
h3cHPEOCDownLoadCNUFWResult.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    h3cHPEOCDownLoadCNUFWResult.setStatus("current")


class _H3cHPEOCCltAutoUpgradeType_Type(Integer32):
    """Custom type h3cHPEOCCltAutoUpgradeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("flash", 1),
          ("ftp", 2),
          ("tftp", 3))
    )


_H3cHPEOCCltAutoUpgradeType_Type.__name__ = "Integer32"
_H3cHPEOCCltAutoUpgradeType_Object = MibScalar
h3cHPEOCCltAutoUpgradeType = _H3cHPEOCCltAutoUpgradeType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 10),
    _H3cHPEOCCltAutoUpgradeType_Type()
)
h3cHPEOCCltAutoUpgradeType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltAutoUpgradeType.setStatus("current")
_H3cHPEOCAutoUpObjects_ObjectIdentity = ObjectIdentity
h3cHPEOCAutoUpObjects = _H3cHPEOCAutoUpObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 11)
)
_H3cHPEOCServerAddress_Type = IpAddress
_H3cHPEOCServerAddress_Object = MibScalar
h3cHPEOCServerAddress = _H3cHPEOCServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 11, 1),
    _H3cHPEOCServerAddress_Type()
)
h3cHPEOCServerAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCServerAddress.setStatus("current")
_H3cHPEOCServerUser_Type = DisplayString
_H3cHPEOCServerUser_Object = MibScalar
h3cHPEOCServerUser = _H3cHPEOCServerUser_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 11, 2),
    _H3cHPEOCServerUser_Type()
)
h3cHPEOCServerUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCServerUser.setStatus("current")
_H3cHPEOCServerPassword_Type = DisplayString
_H3cHPEOCServerPassword_Object = MibScalar
h3cHPEOCServerPassword = _H3cHPEOCServerPassword_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 11, 3),
    _H3cHPEOCServerPassword_Type()
)
h3cHPEOCServerPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCServerPassword.setStatus("current")


class _H3cHPEOCCltLoopbackDetect_Type(Integer32):
    """Custom type h3cHPEOCCltLoopbackDetect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_H3cHPEOCCltLoopbackDetect_Type.__name__ = "Integer32"
_H3cHPEOCCltLoopbackDetect_Object = MibScalar
h3cHPEOCCltLoopbackDetect = _H3cHPEOCCltLoopbackDetect_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 12),
    _H3cHPEOCCltLoopbackDetect_Type()
)
h3cHPEOCCltLoopbackDetect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCltLoopbackDetect.setStatus("current")


class _H3cHPEOCTemplateEnable_Type(Integer32):
    """Custom type h3cHPEOCTemplateEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("false", 0),
          ("true", 1))
    )


_H3cHPEOCTemplateEnable_Type.__name__ = "Integer32"
_H3cHPEOCTemplateEnable_Object = MibScalar
h3cHPEOCTemplateEnable = _H3cHPEOCTemplateEnable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 1, 13),
    _H3cHPEOCTemplateEnable_Type()
)
h3cHPEOCTemplateEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateEnable.setStatus("current")
_H3cHPEOCCableInfo_ObjectIdentity = ObjectIdentity
h3cHPEOCCableInfo = _H3cHPEOCCableInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2)
)
_H3cHPEOCCableInfoTable_Object = MibTable
h3cHPEOCCableInfoTable = _H3cHPEOCCableInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1)
)
if mibBuilder.loadTexts:
    h3cHPEOCCableInfoTable.setStatus("current")
_H3cHPEOCCableInfoEntry_Object = MibTableRow
h3cHPEOCCableInfoEntry = _H3cHPEOCCableInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1)
)
h3cHPEOCCableInfoEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCCableInfoEntry.setStatus("current")
_H3cHPEOCFECErrors_Type = Counter64
_H3cHPEOCFECErrors_Object = MibTableColumn
h3cHPEOCFECErrors = _H3cHPEOCFECErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 1),
    _H3cHPEOCFECErrors_Type()
)
h3cHPEOCFECErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCFECErrors.setStatus("current")
_H3cHPEOCAvgBitsPerCarrier_Type = Unsigned32
_H3cHPEOCAvgBitsPerCarrier_Object = MibTableColumn
h3cHPEOCAvgBitsPerCarrier = _H3cHPEOCAvgBitsPerCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 2),
    _H3cHPEOCAvgBitsPerCarrier_Type()
)
h3cHPEOCAvgBitsPerCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCAvgBitsPerCarrier.setStatus("current")
_H3cHPEOCAvgSNRPerCarrier_Type = Integer32
_H3cHPEOCAvgSNRPerCarrier_Object = MibTableColumn
h3cHPEOCAvgSNRPerCarrier = _H3cHPEOCAvgSNRPerCarrier_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 3),
    _H3cHPEOCAvgSNRPerCarrier_Type()
)
h3cHPEOCAvgSNRPerCarrier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCAvgSNRPerCarrier.setStatus("current")
_H3cHPEOCAvgInPBCRCErrors_Type = Unsigned32
_H3cHPEOCAvgInPBCRCErrors_Object = MibTableColumn
h3cHPEOCAvgInPBCRCErrors = _H3cHPEOCAvgInPBCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 4),
    _H3cHPEOCAvgInPBCRCErrors_Type()
)
h3cHPEOCAvgInPBCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCAvgInPBCRCErrors.setStatus("current")
_H3cHPEOCInTotalPkts_Type = Counter64
_H3cHPEOCInTotalPkts_Object = MibTableColumn
h3cHPEOCInTotalPkts = _H3cHPEOCInTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 5),
    _H3cHPEOCInTotalPkts_Type()
)
h3cHPEOCInTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCInTotalPkts.setStatus("current")
_H3cHPEOCAvgOutPower_Type = Integer32
_H3cHPEOCAvgOutPower_Object = MibTableColumn
h3cHPEOCAvgOutPower = _H3cHPEOCAvgOutPower_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 6),
    _H3cHPEOCAvgOutPower_Type()
)
h3cHPEOCAvgOutPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCAvgOutPower.setStatus("current")
_H3cHPEOCAvgOutPBCRCErrors_Type = Unsigned32
_H3cHPEOCAvgOutPBCRCErrors_Object = MibTableColumn
h3cHPEOCAvgOutPBCRCErrors = _H3cHPEOCAvgOutPBCRCErrors_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 7),
    _H3cHPEOCAvgOutPBCRCErrors_Type()
)
h3cHPEOCAvgOutPBCRCErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCAvgOutPBCRCErrors.setStatus("current")
_H3cHPEOCOutTotalPkts_Type = Counter64
_H3cHPEOCOutTotalPkts_Object = MibTableColumn
h3cHPEOCOutTotalPkts = _H3cHPEOCOutTotalPkts_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 1, 1, 8),
    _H3cHPEOCOutTotalPkts_Type()
)
h3cHPEOCOutTotalPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCOutTotalPkts.setStatus("current")
_H3cHPEOCBitPerSymbolTable_Object = MibTable
h3cHPEOCBitPerSymbolTable = _H3cHPEOCBitPerSymbolTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 2)
)
if mibBuilder.loadTexts:
    h3cHPEOCBitPerSymbolTable.setStatus("current")
_H3cHPEOCBitPerSymbolEntry_Object = MibTableRow
h3cHPEOCBitPerSymbolEntry = _H3cHPEOCBitPerSymbolEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 2, 1)
)
h3cHPEOCBitPerSymbolEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "H3C-HPEOC-MIB", "h3cHPEOCBitPerSymbolIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCBitPerSymbolEntry.setStatus("current")
_H3cHPEOCBitPerSymbolIndex_Type = Unsigned32
_H3cHPEOCBitPerSymbolIndex_Object = MibTableColumn
h3cHPEOCBitPerSymbolIndex = _H3cHPEOCBitPerSymbolIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 2, 1, 1),
    _H3cHPEOCBitPerSymbolIndex_Type()
)
h3cHPEOCBitPerSymbolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cHPEOCBitPerSymbolIndex.setStatus("current")
_H3cHPEOCBitPerSymbol_Type = OctetString
_H3cHPEOCBitPerSymbol_Object = MibTableColumn
h3cHPEOCBitPerSymbol = _H3cHPEOCBitPerSymbol_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 2, 2, 1, 2),
    _H3cHPEOCBitPerSymbol_Type()
)
h3cHPEOCBitPerSymbol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cHPEOCBitPerSymbol.setStatus("current")
_H3cHPEOCTemplate_ObjectIdentity = ObjectIdentity
h3cHPEOCTemplate = _H3cHPEOCTemplate_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3)
)
_H3cHPEOCTemplateGlobalTable_Object = MibTable
h3cHPEOCTemplateGlobalTable = _H3cHPEOCTemplateGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1)
)
if mibBuilder.loadTexts:
    h3cHPEOCTemplateGlobalTable.setStatus("current")
_H3cHPEOCTemplateGlobalEntry_Object = MibTableRow
h3cHPEOCTemplateGlobalEntry = _H3cHPEOCTemplateGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1)
)
h3cHPEOCTemplateGlobalEntry.setIndexNames(
    (0, "H3C-HPEOC-MIB", "h3cHPEOCTemplateIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCTemplateGlobalEntry.setStatus("current")
_H3cHPEOCTemplateIndex_Type = Integer32
_H3cHPEOCTemplateIndex_Object = MibTableColumn
h3cHPEOCTemplateIndex = _H3cHPEOCTemplateIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1, 1),
    _H3cHPEOCTemplateIndex_Type()
)
h3cHPEOCTemplateIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateIndex.setStatus("current")


class _H3cHPEOCTemplateType_Type(Integer32):
    """Custom type h3cHPEOCTemplateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("gateway", 2))
    )


_H3cHPEOCTemplateType_Type.__name__ = "Integer32"
_H3cHPEOCTemplateType_Object = MibTableColumn
h3cHPEOCTemplateType = _H3cHPEOCTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1, 2),
    _H3cHPEOCTemplateType_Type()
)
h3cHPEOCTemplateType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateType.setStatus("current")
_H3cHPEOCTemplateName_Type = DisplayString
_H3cHPEOCTemplateName_Object = MibTableColumn
h3cHPEOCTemplateName = _H3cHPEOCTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1, 3),
    _H3cHPEOCTemplateName_Type()
)
h3cHPEOCTemplateName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateName.setStatus("current")
_H3cHPEOCTemplateDescr_Type = DisplayString
_H3cHPEOCTemplateDescr_Object = MibTableColumn
h3cHPEOCTemplateDescr = _H3cHPEOCTemplateDescr_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1, 4),
    _H3cHPEOCTemplateDescr_Type()
)
h3cHPEOCTemplateDescr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateDescr.setStatus("current")
_H3cHPEOCTemplateCnuMaxDownBW_Type = Integer32
_H3cHPEOCTemplateCnuMaxDownBW_Object = MibTableColumn
h3cHPEOCTemplateCnuMaxDownBW = _H3cHPEOCTemplateCnuMaxDownBW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1, 5),
    _H3cHPEOCTemplateCnuMaxDownBW_Type()
)
h3cHPEOCTemplateCnuMaxDownBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateCnuMaxDownBW.setStatus("current")
_H3cHPEOCTemplateCnuMaxUpBW_Type = Integer32
_H3cHPEOCTemplateCnuMaxUpBW_Object = MibTableColumn
h3cHPEOCTemplateCnuMaxUpBW = _H3cHPEOCTemplateCnuMaxUpBW_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1, 6),
    _H3cHPEOCTemplateCnuMaxUpBW_Type()
)
h3cHPEOCTemplateCnuMaxUpBW.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateCnuMaxUpBW.setStatus("current")
_H3cHPEOCTemplateCnuBcastControl_Type = TruthValue
_H3cHPEOCTemplateCnuBcastControl_Object = MibTableColumn
h3cHPEOCTemplateCnuBcastControl = _H3cHPEOCTemplateCnuBcastControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1, 7),
    _H3cHPEOCTemplateCnuBcastControl_Type()
)
h3cHPEOCTemplateCnuBcastControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateCnuBcastControl.setStatus("current")
_H3cHPEOCTemplateCnuMacLimit_Type = Unsigned32
_H3cHPEOCTemplateCnuMacLimit_Object = MibTableColumn
h3cHPEOCTemplateCnuMacLimit = _H3cHPEOCTemplateCnuMacLimit_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1, 8),
    _H3cHPEOCTemplateCnuMacLimit_Type()
)
h3cHPEOCTemplateCnuMacLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateCnuMacLimit.setStatus("current")
_H3cHPEOCTemplateCb201VlanEn_Type = TruthValue
_H3cHPEOCTemplateCb201VlanEn_Object = MibTableColumn
h3cHPEOCTemplateCb201VlanEn = _H3cHPEOCTemplateCb201VlanEn_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1, 9),
    _H3cHPEOCTemplateCb201VlanEn_Type()
)
h3cHPEOCTemplateCb201VlanEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateCb201VlanEn.setStatus("current")
_H3cHPEOCTemplateRowStatus_Type = RowStatus
_H3cHPEOCTemplateRowStatus_Object = MibTableColumn
h3cHPEOCTemplateRowStatus = _H3cHPEOCTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 1, 1, 10),
    _H3cHPEOCTemplateRowStatus_Type()
)
h3cHPEOCTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateRowStatus.setStatus("current")
_H3cHPEOCTemplateSwitchTable_Object = MibTable
h3cHPEOCTemplateSwitchTable = _H3cHPEOCTemplateSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2)
)
if mibBuilder.loadTexts:
    h3cHPEOCTemplateSwitchTable.setStatus("current")
_H3cHPEOCTemplateSwitchEntry_Object = MibTableRow
h3cHPEOCTemplateSwitchEntry = _H3cHPEOCTemplateSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1)
)
h3cHPEOCTemplateSwitchEntry.setIndexNames(
    (0, "H3C-HPEOC-MIB", "h3cHPEOCTemplateIndex"),
    (0, "H3C-HPEOC-MIB", "h3cHPEOCTemplateUniIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCTemplateSwitchEntry.setStatus("current")
_H3cHPEOCTemplateUniIndex_Type = Integer32
_H3cHPEOCTemplateUniIndex_Object = MibTableColumn
h3cHPEOCTemplateUniIndex = _H3cHPEOCTemplateUniIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 1),
    _H3cHPEOCTemplateUniIndex_Type()
)
h3cHPEOCTemplateUniIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniIndex.setStatus("current")


class _H3cHPEOCTemplateUniSpeed_Type(Integer32):
    """Custom type h3cHPEOCTemplateUniSpeed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              10,
              100)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("s10M", 10),
          ("s100M", 100))
    )


_H3cHPEOCTemplateUniSpeed_Type.__name__ = "Integer32"
_H3cHPEOCTemplateUniSpeed_Object = MibTableColumn
h3cHPEOCTemplateUniSpeed = _H3cHPEOCTemplateUniSpeed_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 2),
    _H3cHPEOCTemplateUniSpeed_Type()
)
h3cHPEOCTemplateUniSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniSpeed.setStatus("current")


class _H3cHPEOCTemplateUniDuplex_Type(Integer32):
    """Custom type h3cHPEOCTemplateUniDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("full", 1),
          ("half", 2),
          ("auto", 3))
    )


_H3cHPEOCTemplateUniDuplex_Type.__name__ = "Integer32"
_H3cHPEOCTemplateUniDuplex_Object = MibTableColumn
h3cHPEOCTemplateUniDuplex = _H3cHPEOCTemplateUniDuplex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 3),
    _H3cHPEOCTemplateUniDuplex_Type()
)
h3cHPEOCTemplateUniDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniDuplex.setStatus("current")


class _H3cHPEOCTemplateUniPriority_Type(Integer32):
    """Custom type h3cHPEOCTemplateUniPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_H3cHPEOCTemplateUniPriority_Type.__name__ = "Integer32"
_H3cHPEOCTemplateUniPriority_Object = MibTableColumn
h3cHPEOCTemplateUniPriority = _H3cHPEOCTemplateUniPriority_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 4),
    _H3cHPEOCTemplateUniPriority_Type()
)
h3cHPEOCTemplateUniPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniPriority.setStatus("current")


class _H3cHPEOCTemplateUniFlowControl_Type(TruthValue):
    """Custom type h3cHPEOCTemplateUniFlowControl based on TruthValue"""
    defaultValue = 2


_H3cHPEOCTemplateUniFlowControl_Type.__name__ = "TruthValue"
_H3cHPEOCTemplateUniFlowControl_Object = MibTableColumn
h3cHPEOCTemplateUniFlowControl = _H3cHPEOCTemplateUniFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 5),
    _H3cHPEOCTemplateUniFlowControl_Type()
)
h3cHPEOCTemplateUniFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniFlowControl.setStatus("current")
_H3cHPEOCTemplateUniUpLineRate_Type = Unsigned32
_H3cHPEOCTemplateUniUpLineRate_Object = MibTableColumn
h3cHPEOCTemplateUniUpLineRate = _H3cHPEOCTemplateUniUpLineRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 6),
    _H3cHPEOCTemplateUniUpLineRate_Type()
)
h3cHPEOCTemplateUniUpLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniUpLineRate.setStatus("current")
_H3cHPEOCTemplateUniDownLineRate_Type = Unsigned32
_H3cHPEOCTemplateUniDownLineRate_Object = MibTableColumn
h3cHPEOCTemplateUniDownLineRate = _H3cHPEOCTemplateUniDownLineRate_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 7),
    _H3cHPEOCTemplateUniDownLineRate_Type()
)
h3cHPEOCTemplateUniDownLineRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniDownLineRate.setStatus("current")


class _H3cHPEOCTemplateUniAdminStatus_Type(Integer32):
    """Custom type h3cHPEOCTemplateUniAdminStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_H3cHPEOCTemplateUniAdminStatus_Type.__name__ = "Integer32"
_H3cHPEOCTemplateUniAdminStatus_Object = MibTableColumn
h3cHPEOCTemplateUniAdminStatus = _H3cHPEOCTemplateUniAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 8),
    _H3cHPEOCTemplateUniAdminStatus_Type()
)
h3cHPEOCTemplateUniAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniAdminStatus.setStatus("current")


class _H3cHPEOCTemplateUniVLANType_Type(Integer32):
    """Custom type h3cHPEOCTemplateUniVLANType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("access", 1),
          ("trunk", 2),
          ("hybrid", 3))
    )


_H3cHPEOCTemplateUniVLANType_Type.__name__ = "Integer32"
_H3cHPEOCTemplateUniVLANType_Object = MibTableColumn
h3cHPEOCTemplateUniVLANType = _H3cHPEOCTemplateUniVLANType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 9),
    _H3cHPEOCTemplateUniVLANType_Type()
)
h3cHPEOCTemplateUniVLANType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniVLANType.setStatus("current")


class _H3cHPEOCTemplateUniPvid_Type(Integer32):
    """Custom type h3cHPEOCTemplateUniPvid based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_H3cHPEOCTemplateUniPvid_Type.__name__ = "Integer32"
_H3cHPEOCTemplateUniPvid_Object = MibTableColumn
h3cHPEOCTemplateUniPvid = _H3cHPEOCTemplateUniPvid_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 10),
    _H3cHPEOCTemplateUniPvid_Type()
)
h3cHPEOCTemplateUniPvid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniPvid.setStatus("current")


class _H3cHPEOCTemplateUniVlanTag_Type(Integer32):
    """Custom type h3cHPEOCTemplateUniVlanTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tagged", 1),
          ("untagged", 2))
    )


_H3cHPEOCTemplateUniVlanTag_Type.__name__ = "Integer32"
_H3cHPEOCTemplateUniVlanTag_Object = MibTableColumn
h3cHPEOCTemplateUniVlanTag = _H3cHPEOCTemplateUniVlanTag_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 3, 2, 1, 11),
    _H3cHPEOCTemplateUniVlanTag_Type()
)
h3cHPEOCTemplateUniVlanTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCTemplateUniVlanTag.setStatus("current")
_H3cHPEOCCnuAccess_ObjectIdentity = ObjectIdentity
h3cHPEOCCnuAccess = _H3cHPEOCCnuAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4)
)
_H3cHPEOCCnuAccessTable_Object = MibTable
h3cHPEOCCnuAccessTable = _H3cHPEOCCnuAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4, 1)
)
if mibBuilder.loadTexts:
    h3cHPEOCCnuAccessTable.setStatus("current")
_H3cHPEOCCnuAccessEntry_Object = MibTableRow
h3cHPEOCCnuAccessEntry = _H3cHPEOCCnuAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4, 1, 1)
)
h3cHPEOCCnuAccessEntry.setIndexNames(
    (0, "H3C-HPEOC-MIB", "h3cHPEOCCnuAccessIndex"),
)
if mibBuilder.loadTexts:
    h3cHPEOCCnuAccessEntry.setStatus("current")
_H3cHPEOCCnuAccessIndex_Type = Integer32
_H3cHPEOCCnuAccessIndex_Object = MibTableColumn
h3cHPEOCCnuAccessIndex = _H3cHPEOCCnuAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4, 1, 1, 1),
    _H3cHPEOCCnuAccessIndex_Type()
)
h3cHPEOCCnuAccessIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cHPEOCCnuAccessIndex.setStatus("current")
_H3cHPEOCCnuHFID_Type = DisplayString
_H3cHPEOCCnuHFID_Object = MibTableColumn
h3cHPEOCCnuHFID = _H3cHPEOCCnuHFID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4, 1, 1, 2),
    _H3cHPEOCCnuHFID_Type()
)
h3cHPEOCCnuHFID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCnuHFID.setStatus("current")
_H3cHPEOCManuInfo_Type = DisplayString
_H3cHPEOCManuInfo_Object = MibTableColumn
h3cHPEOCManuInfo = _H3cHPEOCManuInfo_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4, 1, 1, 3),
    _H3cHPEOCManuInfo_Type()
)
h3cHPEOCManuInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCManuInfo.setStatus("current")


class _H3cHPEOCCnuType_Type(Integer32):
    """Custom type h3cHPEOCCnuType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("switch", 1),
          ("gateway", 2))
    )


_H3cHPEOCCnuType_Type.__name__ = "Integer32"
_H3cHPEOCCnuType_Object = MibTableColumn
h3cHPEOCCnuType = _H3cHPEOCCnuType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4, 1, 1, 4),
    _H3cHPEOCCnuType_Type()
)
h3cHPEOCCnuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCnuType.setStatus("current")


class _H3cHPEOCCnuSwitchType_Type(Integer32):
    """Custom type h3cHPEOCCnuSwitchType based on Integer32"""
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
        *(("rtl8306e", 1),
          ("ar8236", 2),
          ("mv6061", 3),
          ("mv6031", 4))
    )


_H3cHPEOCCnuSwitchType_Type.__name__ = "Integer32"
_H3cHPEOCCnuSwitchType_Object = MibTableColumn
h3cHPEOCCnuSwitchType = _H3cHPEOCCnuSwitchType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4, 1, 1, 5),
    _H3cHPEOCCnuSwitchType_Type()
)
h3cHPEOCCnuSwitchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCnuSwitchType.setStatus("current")
_H3cHPEOCCnuUniNum_Type = Integer32
_H3cHPEOCCnuUniNum_Object = MibTableColumn
h3cHPEOCCnuUniNum = _H3cHPEOCCnuUniNum_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4, 1, 1, 6),
    _H3cHPEOCCnuUniNum_Type()
)
h3cHPEOCCnuUniNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCnuUniNum.setStatus("current")
_H3cHPEOCCnuPhy2Uni_Type = OctetString
_H3cHPEOCCnuPhy2Uni_Object = MibTableColumn
h3cHPEOCCnuPhy2Uni = _H3cHPEOCCnuPhy2Uni_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4, 1, 1, 7),
    _H3cHPEOCCnuPhy2Uni_Type()
)
h3cHPEOCCnuPhy2Uni.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cHPEOCCnuPhy2Uni.setStatus("current")
_H3cHPEOCCnuAccessRowStatus_Type = RowStatus
_H3cHPEOCCnuAccessRowStatus_Object = MibTableColumn
h3cHPEOCCnuAccessRowStatus = _H3cHPEOCCnuAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 84, 4, 1, 1, 8),
    _H3cHPEOCCnuAccessRowStatus_Type()
)
h3cHPEOCCnuAccessRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cHPEOCCnuAccessRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-HPEOC-MIB",
    **{"h3cHPEOC": h3cHPEOC,
       "h3cHPEOCSystem": h3cHPEOCSystem,
       "h3cHPEOCCltVlanType": h3cHPEOCCltVlanType,
       "h3cHPEOCCltVlanManTable": h3cHPEOCCltVlanManTable,
       "h3cHPEOCCltVlanManEntry": h3cHPEOCCltVlanManEntry,
       "h3cHPEOCCltEthPortType": h3cHPEOCCltEthPortType,
       "h3cHPEOCCltSysManTable": h3cHPEOCCltSysManTable,
       "h3cHPEOCCltSysManEntry": h3cHPEOCCltSysManEntry,
       "h3cHPEOCCltDescr": h3cHPEOCCltDescr,
       "h3cHPEOCCltFwVersion": h3cHPEOCCltFwVersion,
       "h3cHPEOCCltLinkState": h3cHPEOCCltLinkState,
       "h3cHPEOCCnuSysManTable": h3cHPEOCCnuSysManTable,
       "h3cHPEOCCnuSysManEntry": h3cHPEOCCnuSysManEntry,
       "h3cHPEOCCnuBcastControl": h3cHPEOCCnuBcastControl,
       "h3cHPEOCCnuAnonymStatus": h3cHPEOCCnuAnonymStatus,
       "h3cHPEOCCnuMacLimit": h3cHPEOCCnuMacLimit,
       "h3cHPEOCCltAutoUpgrade": h3cHPEOCCltAutoUpgrade,
       "h3cHPEOCOnLineCnuNumber": h3cHPEOCOnLineCnuNumber,
       "h3cHPEOCCpuMacAddress": h3cHPEOCCpuMacAddress,
       "h3cHPEOCOffLineCnuNumber": h3cHPEOCOffLineCnuNumber,
       "h3cHPEOCDownLoadCNUFWResult": h3cHPEOCDownLoadCNUFWResult,
       "h3cHPEOCCltAutoUpgradeType": h3cHPEOCCltAutoUpgradeType,
       "h3cHPEOCAutoUpObjects": h3cHPEOCAutoUpObjects,
       "h3cHPEOCServerAddress": h3cHPEOCServerAddress,
       "h3cHPEOCServerUser": h3cHPEOCServerUser,
       "h3cHPEOCServerPassword": h3cHPEOCServerPassword,
       "h3cHPEOCCltLoopbackDetect": h3cHPEOCCltLoopbackDetect,
       "h3cHPEOCTemplateEnable": h3cHPEOCTemplateEnable,
       "h3cHPEOCCableInfo": h3cHPEOCCableInfo,
       "h3cHPEOCCableInfoTable": h3cHPEOCCableInfoTable,
       "h3cHPEOCCableInfoEntry": h3cHPEOCCableInfoEntry,
       "h3cHPEOCFECErrors": h3cHPEOCFECErrors,
       "h3cHPEOCAvgBitsPerCarrier": h3cHPEOCAvgBitsPerCarrier,
       "h3cHPEOCAvgSNRPerCarrier": h3cHPEOCAvgSNRPerCarrier,
       "h3cHPEOCAvgInPBCRCErrors": h3cHPEOCAvgInPBCRCErrors,
       "h3cHPEOCInTotalPkts": h3cHPEOCInTotalPkts,
       "h3cHPEOCAvgOutPower": h3cHPEOCAvgOutPower,
       "h3cHPEOCAvgOutPBCRCErrors": h3cHPEOCAvgOutPBCRCErrors,
       "h3cHPEOCOutTotalPkts": h3cHPEOCOutTotalPkts,
       "h3cHPEOCBitPerSymbolTable": h3cHPEOCBitPerSymbolTable,
       "h3cHPEOCBitPerSymbolEntry": h3cHPEOCBitPerSymbolEntry,
       "h3cHPEOCBitPerSymbolIndex": h3cHPEOCBitPerSymbolIndex,
       "h3cHPEOCBitPerSymbol": h3cHPEOCBitPerSymbol,
       "h3cHPEOCTemplate": h3cHPEOCTemplate,
       "h3cHPEOCTemplateGlobalTable": h3cHPEOCTemplateGlobalTable,
       "h3cHPEOCTemplateGlobalEntry": h3cHPEOCTemplateGlobalEntry,
       "h3cHPEOCTemplateIndex": h3cHPEOCTemplateIndex,
       "h3cHPEOCTemplateType": h3cHPEOCTemplateType,
       "h3cHPEOCTemplateName": h3cHPEOCTemplateName,
       "h3cHPEOCTemplateDescr": h3cHPEOCTemplateDescr,
       "h3cHPEOCTemplateCnuMaxDownBW": h3cHPEOCTemplateCnuMaxDownBW,
       "h3cHPEOCTemplateCnuMaxUpBW": h3cHPEOCTemplateCnuMaxUpBW,
       "h3cHPEOCTemplateCnuBcastControl": h3cHPEOCTemplateCnuBcastControl,
       "h3cHPEOCTemplateCnuMacLimit": h3cHPEOCTemplateCnuMacLimit,
       "h3cHPEOCTemplateCb201VlanEn": h3cHPEOCTemplateCb201VlanEn,
       "h3cHPEOCTemplateRowStatus": h3cHPEOCTemplateRowStatus,
       "h3cHPEOCTemplateSwitchTable": h3cHPEOCTemplateSwitchTable,
       "h3cHPEOCTemplateSwitchEntry": h3cHPEOCTemplateSwitchEntry,
       "h3cHPEOCTemplateUniIndex": h3cHPEOCTemplateUniIndex,
       "h3cHPEOCTemplateUniSpeed": h3cHPEOCTemplateUniSpeed,
       "h3cHPEOCTemplateUniDuplex": h3cHPEOCTemplateUniDuplex,
       "h3cHPEOCTemplateUniPriority": h3cHPEOCTemplateUniPriority,
       "h3cHPEOCTemplateUniFlowControl": h3cHPEOCTemplateUniFlowControl,
       "h3cHPEOCTemplateUniUpLineRate": h3cHPEOCTemplateUniUpLineRate,
       "h3cHPEOCTemplateUniDownLineRate": h3cHPEOCTemplateUniDownLineRate,
       "h3cHPEOCTemplateUniAdminStatus": h3cHPEOCTemplateUniAdminStatus,
       "h3cHPEOCTemplateUniVLANType": h3cHPEOCTemplateUniVLANType,
       "h3cHPEOCTemplateUniPvid": h3cHPEOCTemplateUniPvid,
       "h3cHPEOCTemplateUniVlanTag": h3cHPEOCTemplateUniVlanTag,
       "h3cHPEOCCnuAccess": h3cHPEOCCnuAccess,
       "h3cHPEOCCnuAccessTable": h3cHPEOCCnuAccessTable,
       "h3cHPEOCCnuAccessEntry": h3cHPEOCCnuAccessEntry,
       "h3cHPEOCCnuAccessIndex": h3cHPEOCCnuAccessIndex,
       "h3cHPEOCCnuHFID": h3cHPEOCCnuHFID,
       "h3cHPEOCManuInfo": h3cHPEOCManuInfo,
       "h3cHPEOCCnuType": h3cHPEOCCnuType,
       "h3cHPEOCCnuSwitchType": h3cHPEOCCnuSwitchType,
       "h3cHPEOCCnuUniNum": h3cHPEOCCnuUniNum,
       "h3cHPEOCCnuPhy2Uni": h3cHPEOCCnuPhy2Uni,
       "h3cHPEOCCnuAccessRowStatus": h3cHPEOCCnuAccessRowStatus}
)
