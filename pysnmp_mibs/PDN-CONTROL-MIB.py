# SNMP MIB module (PDN-CONTROL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/paradyne/PDN-CONTROL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 18:59:39 2025
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

(entPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entPhysicalIndex")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(pdn_common,) = mibBuilder.importSymbols(
    "PDN-HEADER-MIB",
    "pdn-common")

(SwitchState,) = mibBuilder.importSymbols(
    "PDN-TC",
    "SwitchState")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

pdnControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10)
)
if mibBuilder.loadTexts:
    pdnControl.setRevisions(
        ("1900-11-20 18:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PdnControlMIBTrapsV2_ObjectIdentity = ObjectIdentity
pdnControlMIBTrapsV2 = _PdnControlMIBTrapsV2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 0)
)
if mibBuilder.loadTexts:
    pdnControlMIBTrapsV2.setStatus("current")


class _DevHWControlReset_Type(Integer32):
    """Custom type devHWControlReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("reset", 2))
    )


_DevHWControlReset_Type.__name__ = "Integer32"
_DevHWControlReset_Object = MibScalar
devHWControlReset = _DevHWControlReset_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 1),
    _DevHWControlReset_Type()
)
devHWControlReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devHWControlReset.setStatus("current")
_DevControlTestTable_Object = MibTable
devControlTestTable = _DevControlTestTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 2)
)
if mibBuilder.loadTexts:
    devControlTestTable.setStatus("current")
_DevControlTestEntry_Object = MibTableRow
devControlTestEntry = _DevControlTestEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 2, 1)
)
devControlTestEntry.setIndexNames(
    (0, "PDN-CONTROL-MIB", "devControlTest"),
)
if mibBuilder.loadTexts:
    devControlTestEntry.setStatus("current")


class _DevControlTest_Type(Integer32):
    """Custom type devControlTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("lampTest", 1),
          ("v35DTELpbkTest", 2))
    )


_DevControlTest_Type.__name__ = "Integer32"
_DevControlTest_Object = MibTableColumn
devControlTest = _DevControlTest_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 2, 1, 1),
    _DevControlTest_Type()
)
devControlTest.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devControlTest.setStatus("current")


class _DevControlTestStatus_Type(Integer32):
    """Custom type devControlTestStatus based on Integer32"""
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


_DevControlTestStatus_Type.__name__ = "Integer32"
_DevControlTestStatus_Object = MibTableColumn
devControlTestStatus = _DevControlTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 2, 1, 2),
    _DevControlTestStatus_Type()
)
devControlTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devControlTestStatus.setStatus("current")


class _DevControlTestCmd_Type(Integer32):
    """Custom type devControlTestCmd based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("start", 1),
          ("stop", 2))
    )


_DevControlTestCmd_Type.__name__ = "Integer32"
_DevControlTestCmd_Object = MibTableColumn
devControlTestCmd = _DevControlTestCmd_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 2, 1, 3),
    _DevControlTestCmd_Type()
)
devControlTestCmd.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devControlTestCmd.setStatus("current")
_DevControlDownLoadTable_Object = MibTable
devControlDownLoadTable = _DevControlDownLoadTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 3)
)
if mibBuilder.loadTexts:
    devControlDownLoadTable.setStatus("current")
_DevControlDownLoadEntry_Object = MibTableRow
devControlDownLoadEntry = _DevControlDownLoadEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 3, 1)
)
devControlDownLoadEntry.setIndexNames(
    (0, "PDN-CONTROL-MIB", "devControlDownLoadIndex"),
)
if mibBuilder.loadTexts:
    devControlDownLoadEntry.setStatus("current")
_DevControlDownLoadIndex_Type = Integer32
_DevControlDownLoadIndex_Object = MibTableColumn
devControlDownLoadIndex = _DevControlDownLoadIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 3, 1, 1),
    _DevControlDownLoadIndex_Type()
)
devControlDownLoadIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devControlDownLoadIndex.setStatus("current")


class _DevControlDownLoadRelease_Type(DisplayString):
    """Custom type devControlDownLoadRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DevControlDownLoadRelease_Type.__name__ = "DisplayString"
_DevControlDownLoadRelease_Object = MibTableColumn
devControlDownLoadRelease = _DevControlDownLoadRelease_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 3, 1, 2),
    _DevControlDownLoadRelease_Type()
)
devControlDownLoadRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devControlDownLoadRelease.setStatus("current")


class _DevControlDownLoadOperStatus_Type(Integer32):
    """Custom type devControlDownLoadOperStatus based on Integer32"""
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


_DevControlDownLoadOperStatus_Type.__name__ = "Integer32"
_DevControlDownLoadOperStatus_Object = MibTableColumn
devControlDownLoadOperStatus = _DevControlDownLoadOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 3, 1, 3),
    _DevControlDownLoadOperStatus_Type()
)
devControlDownLoadOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devControlDownLoadOperStatus.setStatus("current")


class _DevControlDownLoadAdminStatus_Type(Integer32):
    """Custom type devControlDownLoadAdminStatus based on Integer32"""
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


_DevControlDownLoadAdminStatus_Type.__name__ = "Integer32"
_DevControlDownLoadAdminStatus_Object = MibTableColumn
devControlDownLoadAdminStatus = _DevControlDownLoadAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 3, 1, 4),
    _DevControlDownLoadAdminStatus_Type()
)
devControlDownLoadAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devControlDownLoadAdminStatus.setStatus("current")
_DevControlRMON_ObjectIdentity = ObjectIdentity
devControlRMON = _DevControlRMON_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 4)
)


class _DevControlRMONAdminStatus_Type(Integer32):
    """Custom type devControlRMONAdminStatus based on Integer32"""
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


_DevControlRMONAdminStatus_Type.__name__ = "Integer32"
_DevControlRMONAdminStatus_Object = MibScalar
devControlRMONAdminStatus = _DevControlRMONAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 4, 1),
    _DevControlRMONAdminStatus_Type()
)
devControlRMONAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devControlRMONAdminStatus.setStatus("current")
_DevSNSwitchFirmwareTable_Object = MibTable
devSNSwitchFirmwareTable = _DevSNSwitchFirmwareTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 5)
)
if mibBuilder.loadTexts:
    devSNSwitchFirmwareTable.setStatus("current")
_DevSNSwitchFirmwareEntry_Object = MibTableRow
devSNSwitchFirmwareEntry = _DevSNSwitchFirmwareEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 5, 1)
)
devSNSwitchFirmwareEntry.setIndexNames(
    (0, "PDN-CONTROL-MIB", "devSNSwitchFirmwareIndex"),
)
if mibBuilder.loadTexts:
    devSNSwitchFirmwareEntry.setStatus("current")
_DevSNSwitchFirmwareIndex_Type = Integer32
_DevSNSwitchFirmwareIndex_Object = MibTableColumn
devSNSwitchFirmwareIndex = _DevSNSwitchFirmwareIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 5, 1, 1),
    _DevSNSwitchFirmwareIndex_Type()
)
devSNSwitchFirmwareIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devSNSwitchFirmwareIndex.setStatus("current")


class _DevSNSwitchFirmwareBank_Type(Integer32):
    """Custom type devSNSwitchFirmwareBank based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("switch", 2))
    )


_DevSNSwitchFirmwareBank_Type.__name__ = "Integer32"
_DevSNSwitchFirmwareBank_Object = MibTableColumn
devSNSwitchFirmwareBank = _DevSNSwitchFirmwareBank_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 5, 1, 2),
    _DevSNSwitchFirmwareBank_Type()
)
devSNSwitchFirmwareBank.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devSNSwitchFirmwareBank.setStatus("current")
_DevControlFTP_ObjectIdentity = ObjectIdentity
devControlFTP = _DevControlFTP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 6)
)
_DevControlFTPRate_Type = Integer32
_DevControlFTPRate_Object = MibScalar
devControlFTPRate = _DevControlFTPRate_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 6, 1),
    _DevControlFTPRate_Type()
)
devControlFTPRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devControlFTPRate.setStatus("current")
_DevFileXferMIBObjects_ObjectIdentity = ObjectIdentity
devFileXferMIBObjects = _DevFileXferMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7)
)
_DevFileXferConfigTable_Object = MibTable
devFileXferConfigTable = _DevFileXferConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1)
)
if mibBuilder.loadTexts:
    devFileXferConfigTable.setStatus("current")
_DevFileXferConfigEntry_Object = MibTableRow
devFileXferConfigEntry = _DevFileXferConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1)
)
devFileXferConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    devFileXferConfigEntry.setStatus("current")
_DevFileXferFileName_Type = DisplayString
_DevFileXferFileName_Object = MibTableColumn
devFileXferFileName = _DevFileXferFileName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 1),
    _DevFileXferFileName_Type()
)
devFileXferFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFileXferFileName.setStatus("current")


class _DevFileXferCopyProtocol_Type(Integer32):
    """Custom type devFileXferCopyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2))
    )


_DevFileXferCopyProtocol_Type.__name__ = "Integer32"
_DevFileXferCopyProtocol_Object = MibTableColumn
devFileXferCopyProtocol = _DevFileXferCopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 2),
    _DevFileXferCopyProtocol_Type()
)
devFileXferCopyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFileXferCopyProtocol.setStatus("current")


class _DevFileXferFileType_Type(Integer32):
    """Custom type devFileXferFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firmware", 1),
          ("config", 2))
    )


_DevFileXferFileType_Type.__name__ = "Integer32"
_DevFileXferFileType_Object = MibTableColumn
devFileXferFileType = _DevFileXferFileType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 3),
    _DevFileXferFileType_Type()
)
devFileXferFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFileXferFileType.setStatus("current")
_DevFileXferServerIpAddress_Type = IpAddress
_DevFileXferServerIpAddress_Object = MibTableColumn
devFileXferServerIpAddress = _DevFileXferServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 4),
    _DevFileXferServerIpAddress_Type()
)
devFileXferServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFileXferServerIpAddress.setStatus("current")
_DevFileXferUserName_Type = DisplayString
_DevFileXferUserName_Object = MibTableColumn
devFileXferUserName = _DevFileXferUserName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 5),
    _DevFileXferUserName_Type()
)
devFileXferUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFileXferUserName.setStatus("current")
_DevFileXferUserPassword_Type = DisplayString
_DevFileXferUserPassword_Object = MibTableColumn
devFileXferUserPassword = _DevFileXferUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 6),
    _DevFileXferUserPassword_Type()
)
devFileXferUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFileXferUserPassword.setStatus("current")


class _DevFileXferOperation_Type(Integer32):
    """Custom type devFileXferOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("put", 2))
    )


_DevFileXferOperation_Type.__name__ = "Integer32"
_DevFileXferOperation_Object = MibTableColumn
devFileXferOperation = _DevFileXferOperation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 7),
    _DevFileXferOperation_Type()
)
devFileXferOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFileXferOperation.setStatus("current")
_DevFileXferPktsSent_Type = Counter32
_DevFileXferPktsSent_Object = MibTableColumn
devFileXferPktsSent = _DevFileXferPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 8),
    _DevFileXferPktsSent_Type()
)
devFileXferPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFileXferPktsSent.setStatus("current")
_DevFileXferPktsRecv_Type = Counter32
_DevFileXferPktsRecv_Object = MibTableColumn
devFileXferPktsRecv = _DevFileXferPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 9),
    _DevFileXferPktsRecv_Type()
)
devFileXferPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFileXferPktsRecv.setStatus("current")
_DevFileXferOctetsSent_Type = Counter32
_DevFileXferOctetsSent_Object = MibTableColumn
devFileXferOctetsSent = _DevFileXferOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 10),
    _DevFileXferOctetsSent_Type()
)
devFileXferOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFileXferOctetsSent.setStatus("current")
_DevFileXferOctetsRecv_Type = Counter32
_DevFileXferOctetsRecv_Object = MibTableColumn
devFileXferOctetsRecv = _DevFileXferOctetsRecv_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 11),
    _DevFileXferOctetsRecv_Type()
)
devFileXferOctetsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFileXferOctetsRecv.setStatus("current")


class _DevFileXferOwnerString_Type(OctetString):
    """Custom type devFileXferOwnerString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DevFileXferOwnerString_Type.__name__ = "OctetString"
_DevFileXferOwnerString_Object = MibTableColumn
devFileXferOwnerString = _DevFileXferOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 12),
    _DevFileXferOwnerString_Type()
)
devFileXferOwnerString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFileXferOwnerString.setStatus("current")


class _DevFileXferStatus_Type(Integer32):
    """Custom type devFileXferStatus based on Integer32"""
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
          ("success", 2),
          ("failure", 3),
          ("inprogress", 4))
    )


_DevFileXferStatus_Type.__name__ = "Integer32"
_DevFileXferStatus_Object = MibTableColumn
devFileXferStatus = _DevFileXferStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 13),
    _DevFileXferStatus_Type()
)
devFileXferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFileXferStatus.setStatus("current")
_DevFileXferErrorStatus_Type = Integer32
_DevFileXferErrorStatus_Object = MibTableColumn
devFileXferErrorStatus = _DevFileXferErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 14),
    _DevFileXferErrorStatus_Type()
)
devFileXferErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFileXferErrorStatus.setStatus("current")


class _DevFileXferSendEvent_Type(Integer32):
    """Custom type devFileXferSendEvent based on Integer32"""
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


_DevFileXferSendEvent_Type.__name__ = "Integer32"
_DevFileXferSendEvent_Object = MibTableColumn
devFileXferSendEvent = _DevFileXferSendEvent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 15),
    _DevFileXferSendEvent_Type()
)
devFileXferSendEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFileXferSendEvent.setStatus("current")
_DevFileXferRowStatus_Type = RowStatus
_DevFileXferRowStatus_Object = MibTableColumn
devFileXferRowStatus = _DevFileXferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 16),
    _DevFileXferRowStatus_Type()
)
devFileXferRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFileXferRowStatus.setStatus("current")
_DevFileXferXferTime_Type = TimeTicks
_DevFileXferXferTime_Object = MibTableColumn
devFileXferXferTime = _DevFileXferXferTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 1, 1, 17),
    _DevFileXferXferTime_Type()
)
devFileXferXferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFileXferXferTime.setStatus("current")
_PdnDevFileXferTable_Object = MibTable
pdnDevFileXferTable = _PdnDevFileXferTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2)
)
if mibBuilder.loadTexts:
    pdnDevFileXferTable.setStatus("current")
_PdnDevFileXferEntry_Object = MibTableRow
pdnDevFileXferEntry = _PdnDevFileXferEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1)
)
pdnDevFileXferEntry.setIndexNames(
    (0, "PDN-CONTROL-MIB", "pdnDevFileXferSessionID"),
)
if mibBuilder.loadTexts:
    pdnDevFileXferEntry.setStatus("current")
_PdnDevFileXferSessionID_Type = Integer32
_PdnDevFileXferSessionID_Object = MibTableColumn
pdnDevFileXferSessionID = _PdnDevFileXferSessionID_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 1),
    _PdnDevFileXferSessionID_Type()
)
pdnDevFileXferSessionID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    pdnDevFileXferSessionID.setStatus("current")
_PdnDevFileXferifIndex_Type = Integer32
_PdnDevFileXferifIndex_Object = MibTableColumn
pdnDevFileXferifIndex = _PdnDevFileXferifIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 2),
    _PdnDevFileXferifIndex_Type()
)
pdnDevFileXferifIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferifIndex.setStatus("current")
_PdnDevFileXferFileName_Type = DisplayString
_PdnDevFileXferFileName_Object = MibTableColumn
pdnDevFileXferFileName = _PdnDevFileXferFileName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 3),
    _PdnDevFileXferFileName_Type()
)
pdnDevFileXferFileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferFileName.setStatus("current")


class _PdnDevFileXferCopyProtocol_Type(Integer32):
    """Custom type pdnDevFileXferCopyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2))
    )


_PdnDevFileXferCopyProtocol_Type.__name__ = "Integer32"
_PdnDevFileXferCopyProtocol_Object = MibTableColumn
pdnDevFileXferCopyProtocol = _PdnDevFileXferCopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 4),
    _PdnDevFileXferCopyProtocol_Type()
)
pdnDevFileXferCopyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferCopyProtocol.setStatus("current")


class _PdnDevFileXferFileType_Type(Integer32):
    """Custom type pdnDevFileXferFileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("firmware", 1),
          ("config", 2))
    )


_PdnDevFileXferFileType_Type.__name__ = "Integer32"
_PdnDevFileXferFileType_Object = MibTableColumn
pdnDevFileXferFileType = _PdnDevFileXferFileType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 5),
    _PdnDevFileXferFileType_Type()
)
pdnDevFileXferFileType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferFileType.setStatus("current")
_PdnDevFileXferServerIpAddress_Type = IpAddress
_PdnDevFileXferServerIpAddress_Object = MibTableColumn
pdnDevFileXferServerIpAddress = _PdnDevFileXferServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 6),
    _PdnDevFileXferServerIpAddress_Type()
)
pdnDevFileXferServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferServerIpAddress.setStatus("current")
_PdnDevFileXferUserName_Type = DisplayString
_PdnDevFileXferUserName_Object = MibTableColumn
pdnDevFileXferUserName = _PdnDevFileXferUserName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 7),
    _PdnDevFileXferUserName_Type()
)
pdnDevFileXferUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferUserName.setStatus("current")
_PdnDevFileXferUserPassword_Type = DisplayString
_PdnDevFileXferUserPassword_Object = MibTableColumn
pdnDevFileXferUserPassword = _PdnDevFileXferUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 8),
    _PdnDevFileXferUserPassword_Type()
)
pdnDevFileXferUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferUserPassword.setStatus("current")
_PdnDevFileXferUserAccount_Type = DisplayString
_PdnDevFileXferUserAccount_Object = MibTableColumn
pdnDevFileXferUserAccount = _PdnDevFileXferUserAccount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 9),
    _PdnDevFileXferUserAccount_Type()
)
pdnDevFileXferUserAccount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferUserAccount.setStatus("current")


class _PdnDevFileXferOperation_Type(Integer32):
    """Custom type pdnDevFileXferOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("get", 1),
          ("put", 2))
    )


_PdnDevFileXferOperation_Type.__name__ = "Integer32"
_PdnDevFileXferOperation_Object = MibTableColumn
pdnDevFileXferOperation = _PdnDevFileXferOperation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 10),
    _PdnDevFileXferOperation_Type()
)
pdnDevFileXferOperation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferOperation.setStatus("current")
_PdnDevFileXferPktsSent_Type = Counter32
_PdnDevFileXferPktsSent_Object = MibTableColumn
pdnDevFileXferPktsSent = _PdnDevFileXferPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 11),
    _PdnDevFileXferPktsSent_Type()
)
pdnDevFileXferPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDevFileXferPktsSent.setStatus("current")
_PdnDevFileXferPktsRecv_Type = Counter32
_PdnDevFileXferPktsRecv_Object = MibTableColumn
pdnDevFileXferPktsRecv = _PdnDevFileXferPktsRecv_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 12),
    _PdnDevFileXferPktsRecv_Type()
)
pdnDevFileXferPktsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDevFileXferPktsRecv.setStatus("current")
_PdnDevFileXferOctetsSent_Type = Counter32
_PdnDevFileXferOctetsSent_Object = MibTableColumn
pdnDevFileXferOctetsSent = _PdnDevFileXferOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 13),
    _PdnDevFileXferOctetsSent_Type()
)
pdnDevFileXferOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDevFileXferOctetsSent.setStatus("current")
_PdnDevFileXferOctetsRecv_Type = Counter32
_PdnDevFileXferOctetsRecv_Object = MibTableColumn
pdnDevFileXferOctetsRecv = _PdnDevFileXferOctetsRecv_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 14),
    _PdnDevFileXferOctetsRecv_Type()
)
pdnDevFileXferOctetsRecv.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDevFileXferOctetsRecv.setStatus("current")


class _PdnDevFileXferOwnerString_Type(OctetString):
    """Custom type pdnDevFileXferOwnerString based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_PdnDevFileXferOwnerString_Type.__name__ = "OctetString"
_PdnDevFileXferOwnerString_Object = MibTableColumn
pdnDevFileXferOwnerString = _PdnDevFileXferOwnerString_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 15),
    _PdnDevFileXferOwnerString_Type()
)
pdnDevFileXferOwnerString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferOwnerString.setStatus("current")


class _PdnDevFileXferStatus_Type(Integer32):
    """Custom type pdnDevFileXferStatus based on Integer32"""
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
          ("success", 2),
          ("failure", 3),
          ("inprogress", 4))
    )


_PdnDevFileXferStatus_Type.__name__ = "Integer32"
_PdnDevFileXferStatus_Object = MibTableColumn
pdnDevFileXferStatus = _PdnDevFileXferStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 16),
    _PdnDevFileXferStatus_Type()
)
pdnDevFileXferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDevFileXferStatus.setStatus("current")


class _PdnDevFileXferApply_Type(Integer32):
    """Custom type pdnDevFileXferApply based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_PdnDevFileXferApply_Type.__name__ = "Integer32"
_PdnDevFileXferApply_Object = MibTableColumn
pdnDevFileXferApply = _PdnDevFileXferApply_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 17),
    _PdnDevFileXferApply_Type()
)
pdnDevFileXferApply.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferApply.setStatus("current")
_PdnDevFileXferErrorStatus_Type = Integer32
_PdnDevFileXferErrorStatus_Object = MibTableColumn
pdnDevFileXferErrorStatus = _PdnDevFileXferErrorStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 18),
    _PdnDevFileXferErrorStatus_Type()
)
pdnDevFileXferErrorStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDevFileXferErrorStatus.setStatus("current")


class _PdnDevFileXferSendEvent_Type(Integer32):
    """Custom type pdnDevFileXferSendEvent based on Integer32"""
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


_PdnDevFileXferSendEvent_Type.__name__ = "Integer32"
_PdnDevFileXferSendEvent_Object = MibTableColumn
pdnDevFileXferSendEvent = _PdnDevFileXferSendEvent_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 19),
    _PdnDevFileXferSendEvent_Type()
)
pdnDevFileXferSendEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferSendEvent.setStatus("current")
_PdnDevFileXferXferTime_Type = TimeTicks
_PdnDevFileXferXferTime_Object = MibTableColumn
pdnDevFileXferXferTime = _PdnDevFileXferXferTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 20),
    _PdnDevFileXferXferTime_Type()
)
pdnDevFileXferXferTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDevFileXferXferTime.setStatus("current")
_PdnDevFileXferRowStatus_Type = RowStatus
_PdnDevFileXferRowStatus_Object = MibTableColumn
pdnDevFileXferRowStatus = _PdnDevFileXferRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 2, 1, 21),
    _PdnDevFileXferRowStatus_Type()
)
pdnDevFileXferRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnDevFileXferRowStatus.setStatus("current")
_PdnDevFileXferSessionIDNext_Type = Integer32
_PdnDevFileXferSessionIDNext_Object = MibScalar
pdnDevFileXferSessionIDNext = _PdnDevFileXferSessionIDNext_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 7, 3),
    _PdnDevFileXferSessionIDNext_Type()
)
pdnDevFileXferSessionIDNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pdnDevFileXferSessionIDNext.setStatus("current")
_DevFileXferMIBTraps_ObjectIdentity = ObjectIdentity
devFileXferMIBTraps = _DevFileXferMIBTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 8)
)
_DevFirmwareControlMIBObjects_ObjectIdentity = ObjectIdentity
devFirmwareControlMIBObjects = _DevFirmwareControlMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 9)
)
_DevFirmwareControlTable_Object = MibTable
devFirmwareControlTable = _DevFirmwareControlTable_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 9, 1)
)
if mibBuilder.loadTexts:
    devFirmwareControlTable.setStatus("current")
_DevFirmwareControlEntry_Object = MibTableRow
devFirmwareControlEntry = _DevFirmwareControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 9, 1, 1)
)
devFirmwareControlEntry.setIndexNames(
    (0, "PDN-CONTROL-MIB", "devFirmwareControlIndex"),
)
if mibBuilder.loadTexts:
    devFirmwareControlEntry.setStatus("current")
_DevFirmwareControlIndex_Type = Integer32
_DevFirmwareControlIndex_Object = MibTableColumn
devFirmwareControlIndex = _DevFirmwareControlIndex_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 9, 1, 1, 1),
    _DevFirmwareControlIndex_Type()
)
devFirmwareControlIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFirmwareControlIndex.setStatus("current")


class _DevFirmwareControlRelease_Type(DisplayString):
    """Custom type devFirmwareControlRelease based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_DevFirmwareControlRelease_Type.__name__ = "DisplayString"
_DevFirmwareControlRelease_Object = MibTableColumn
devFirmwareControlRelease = _DevFirmwareControlRelease_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 9, 1, 1, 2),
    _DevFirmwareControlRelease_Type()
)
devFirmwareControlRelease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFirmwareControlRelease.setStatus("current")


class _DevFirmwareControlOperStatus_Type(Integer32):
    """Custom type devFirmwareControlOperStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("invalid", 2),
          ("unknown", 3))
    )


_DevFirmwareControlOperStatus_Type.__name__ = "Integer32"
_DevFirmwareControlOperStatus_Object = MibTableColumn
devFirmwareControlOperStatus = _DevFirmwareControlOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 9, 1, 1, 3),
    _DevFirmwareControlOperStatus_Type()
)
devFirmwareControlOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devFirmwareControlOperStatus.setStatus("current")


class _DevFirmwareControlAdminStatus_Type(Integer32):
    """Custom type devFirmwareControlAdminStatus based on Integer32"""
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


_DevFirmwareControlAdminStatus_Type.__name__ = "Integer32"
_DevFirmwareControlAdminStatus_Object = MibTableColumn
devFirmwareControlAdminStatus = _DevFirmwareControlAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 9, 1, 1, 4),
    _DevFirmwareControlAdminStatus_Type()
)
devFirmwareControlAdminStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    devFirmwareControlAdminStatus.setStatus("current")
_PdnConfigChangeMgmt_ObjectIdentity = ObjectIdentity
pdnConfigChangeMgmt = _PdnConfigChangeMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10)
)
_PdnCCMAutoBackup_ObjectIdentity = ObjectIdentity
pdnCCMAutoBackup = _PdnCCMAutoBackup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1)
)


class _PdnCCMAutoBackupType_Type(Integer32):
    """Custom type pdnCCMAutoBackupType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("fixed", 1),
          ("dynamic", 2))
    )


_PdnCCMAutoBackupType_Type.__name__ = "Integer32"
_PdnCCMAutoBackupType_Object = MibScalar
pdnCCMAutoBackupType = _PdnCCMAutoBackupType_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 1),
    _PdnCCMAutoBackupType_Type()
)
pdnCCMAutoBackupType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupType.setStatus("current")


class _PdnCCMAutoBackupFixedDay_Type(Bits):
    """Custom type pdnCCMAutoBackupFixedDay based on Bits"""
    namedValues = NamedValues(
        *(("sunday", 0),
          ("monday", 1),
          ("tuesday", 2),
          ("wednesday", 3),
          ("thursday", 4),
          ("friday", 5),
          ("saturday", 6))
    )

_PdnCCMAutoBackupFixedDay_Type.__name__ = "Bits"
_PdnCCMAutoBackupFixedDay_Object = MibScalar
pdnCCMAutoBackupFixedDay = _PdnCCMAutoBackupFixedDay_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 2),
    _PdnCCMAutoBackupFixedDay_Type()
)
pdnCCMAutoBackupFixedDay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupFixedDay.setStatus("current")


class _PdnCCMAutoBackupFixedTime_Type(Integer32):
    """Custom type pdnCCMAutoBackupFixedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1440),
    )


_PdnCCMAutoBackupFixedTime_Type.__name__ = "Integer32"
_PdnCCMAutoBackupFixedTime_Object = MibScalar
pdnCCMAutoBackupFixedTime = _PdnCCMAutoBackupFixedTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 3),
    _PdnCCMAutoBackupFixedTime_Type()
)
pdnCCMAutoBackupFixedTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupFixedTime.setStatus("current")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupFixedTime.setUnits("minutes")


class _PdnCCMAutoBackupDynamicTime_Type(Integer32):
    """Custom type pdnCCMAutoBackupDynamicTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 1440),
    )


_PdnCCMAutoBackupDynamicTime_Type.__name__ = "Integer32"
_PdnCCMAutoBackupDynamicTime_Object = MibScalar
pdnCCMAutoBackupDynamicTime = _PdnCCMAutoBackupDynamicTime_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 4),
    _PdnCCMAutoBackupDynamicTime_Type()
)
pdnCCMAutoBackupDynamicTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupDynamicTime.setStatus("current")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupDynamicTime.setUnits("minutes")


class _PdnCCMAutoBackupAppendTimeStampToFilename_Type(Integer32):
    """Custom type pdnCCMAutoBackupAppendTimeStampToFilename based on Integer32"""
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


_PdnCCMAutoBackupAppendTimeStampToFilename_Type.__name__ = "Integer32"
_PdnCCMAutoBackupAppendTimeStampToFilename_Object = MibScalar
pdnCCMAutoBackupAppendTimeStampToFilename = _PdnCCMAutoBackupAppendTimeStampToFilename_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 5),
    _PdnCCMAutoBackupAppendTimeStampToFilename_Type()
)
pdnCCMAutoBackupAppendTimeStampToFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupAppendTimeStampToFilename.setStatus("current")
_PdnCCMAutoBackupFilename_Type = DisplayString
_PdnCCMAutoBackupFilename_Object = MibScalar
pdnCCMAutoBackupFilename = _PdnCCMAutoBackupFilename_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 6),
    _PdnCCMAutoBackupFilename_Type()
)
pdnCCMAutoBackupFilename.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupFilename.setStatus("current")
_PdnCCMAutoBackupServerIpAddress_Type = IpAddress
_PdnCCMAutoBackupServerIpAddress_Object = MibScalar
pdnCCMAutoBackupServerIpAddress = _PdnCCMAutoBackupServerIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 7),
    _PdnCCMAutoBackupServerIpAddress_Type()
)
pdnCCMAutoBackupServerIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupServerIpAddress.setStatus("current")
_PdnCCMAutoBackupUserName_Type = DisplayString
_PdnCCMAutoBackupUserName_Object = MibScalar
pdnCCMAutoBackupUserName = _PdnCCMAutoBackupUserName_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 8),
    _PdnCCMAutoBackupUserName_Type()
)
pdnCCMAutoBackupUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupUserName.setStatus("current")
_PdnCCMAutoBackupUserPassword_Type = DisplayString
_PdnCCMAutoBackupUserPassword_Object = MibScalar
pdnCCMAutoBackupUserPassword = _PdnCCMAutoBackupUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 9),
    _PdnCCMAutoBackupUserPassword_Type()
)
pdnCCMAutoBackupUserPassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupUserPassword.setStatus("current")
_PdnCCMAutoBackupUserAccount_Type = DisplayString
_PdnCCMAutoBackupUserAccount_Object = MibScalar
pdnCCMAutoBackupUserAccount = _PdnCCMAutoBackupUserAccount_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 10),
    _PdnCCMAutoBackupUserAccount_Type()
)
pdnCCMAutoBackupUserAccount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupUserAccount.setStatus("current")


class _PdnCCMAutoBackupCopyProtocol_Type(Integer32):
    """Custom type pdnCCMAutoBackupCopyProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tftp", 1),
          ("ftp", 2))
    )


_PdnCCMAutoBackupCopyProtocol_Type.__name__ = "Integer32"
_PdnCCMAutoBackupCopyProtocol_Object = MibScalar
pdnCCMAutoBackupCopyProtocol = _PdnCCMAutoBackupCopyProtocol_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 1, 11),
    _PdnCCMAutoBackupCopyProtocol_Type()
)
pdnCCMAutoBackupCopyProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    pdnCCMAutoBackupCopyProtocol.setStatus("current")
_PdnCCMAutoRestore_Type = SwitchState
_PdnCCMAutoRestore_Object = MibScalar
pdnCCMAutoRestore = _PdnCCMAutoRestore_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 2),
    _PdnCCMAutoRestore_Type()
)
pdnCCMAutoRestore.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCCMAutoRestore.setStatus("current")


class _PdnCCMResyncOperation_Type(Integer32):
    """Custom type pdnCCMResyncOperation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noOp", 1),
          ("get", 2),
          ("put", 3))
    )


_PdnCCMResyncOperation_Type.__name__ = "Integer32"
_PdnCCMResyncOperation_Object = MibScalar
pdnCCMResyncOperation = _PdnCCMResyncOperation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 3),
    _PdnCCMResyncOperation_Type()
)
pdnCCMResyncOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCCMResyncOperation.setStatus("current")


class _PdnCCMOperation_Type(Integer32):
    """Custom type pdnCCMOperation based on Integer32"""
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
        *(("noOp", 1),
          ("apply", 2),
          ("save", 3),
          ("reset", 4),
          ("revert", 5),
          ("default", 6))
    )


_PdnCCMOperation_Type.__name__ = "Integer32"
_PdnCCMOperation_Object = MibScalar
pdnCCMOperation = _PdnCCMOperation_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 10, 4),
    _PdnCCMOperation_Type()
)
pdnCCMOperation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pdnCCMOperation.setStatus("current")
_PdnControlMIBGroups_ObjectIdentity = ObjectIdentity
pdnControlMIBGroups = _PdnControlMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11)
)
_PdnAutoFw_ObjectIdentity = ObjectIdentity
pdnAutoFw = _PdnAutoFw_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 12)
)
_DevIsAutoFwEnabled_Type = SwitchState
_DevIsAutoFwEnabled_Object = MibScalar
devIsAutoFwEnabled = _DevIsAutoFwEnabled_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 12, 1),
    _DevIsAutoFwEnabled_Type()
)
devIsAutoFwEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    devIsAutoFwEnabled.setStatus("current")


class _DevAutoFwStatus_Type(DisplayString):
    """Custom type devAutoFwStatus based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_DevAutoFwStatus_Type.__name__ = "DisplayString"
_DevAutoFwStatus_Object = MibScalar
devAutoFwStatus = _DevAutoFwStatus_Object(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 12, 2),
    _DevAutoFwStatus_Type()
)
devAutoFwStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    devAutoFwStatus.setStatus("current")

# Managed Objects groups

devResetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 1)
)
devResetGroup.setObjects(
    ("PDN-CONTROL-MIB", "devHWControlReset")
)
if mibBuilder.loadTexts:
    devResetGroup.setStatus("current")

devControlTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 2)
)
devControlTestGroup.setObjects(
      *(("PDN-CONTROL-MIB", "devControlTest"),
        ("PDN-CONTROL-MIB", "devControlTestStatus"),
        ("PDN-CONTROL-MIB", "devControlTestCmd"))
)
if mibBuilder.loadTexts:
    devControlTestGroup.setStatus("current")

devControlDownloadGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 3)
)
devControlDownloadGroup.setObjects(
      *(("PDN-CONTROL-MIB", "devControlDownLoadIndex"),
        ("PDN-CONTROL-MIB", "devControlDownLoadRelease"),
        ("PDN-CONTROL-MIB", "devControlDownLoadOperStatus"),
        ("PDN-CONTROL-MIB", "devControlDownLoadAdminStatus"))
)
if mibBuilder.loadTexts:
    devControlDownloadGroup.setStatus("current")

devControlRMONGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 4)
)
devControlRMONGroup.setObjects(
    ("PDN-CONTROL-MIB", "devControlRMONAdminStatus")
)
if mibBuilder.loadTexts:
    devControlRMONGroup.setStatus("current")

devSNSwitchFirmwareGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 5)
)
devSNSwitchFirmwareGroup.setObjects(
      *(("PDN-CONTROL-MIB", "devSNSwitchFirmwareIndex"),
        ("PDN-CONTROL-MIB", "devSNSwitchFirmwareBank"))
)
if mibBuilder.loadTexts:
    devSNSwitchFirmwareGroup.setStatus("current")

devControlFTPGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 6)
)
devControlFTPGroup.setObjects(
    ("PDN-CONTROL-MIB", "devControlFTPRate")
)
if mibBuilder.loadTexts:
    devControlFTPGroup.setStatus("current")

devFileXferMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 7)
)
devFileXferMIBGroup.setObjects(
      *(("PDN-CONTROL-MIB", "devFileXferFileName"),
        ("PDN-CONTROL-MIB", "devFileXferCopyProtocol"),
        ("PDN-CONTROL-MIB", "devFileXferFileType"),
        ("PDN-CONTROL-MIB", "devFileXferServerIpAddress"),
        ("PDN-CONTROL-MIB", "devFileXferUserName"),
        ("PDN-CONTROL-MIB", "devFileXferUserPassword"),
        ("PDN-CONTROL-MIB", "devFileXferOperation"),
        ("PDN-CONTROL-MIB", "devFileXferPktsSent"),
        ("PDN-CONTROL-MIB", "devFileXferPktsRecv"),
        ("PDN-CONTROL-MIB", "devFileXferOctetsSent"),
        ("PDN-CONTROL-MIB", "devFileXferOctetsRecv"),
        ("PDN-CONTROL-MIB", "devFileXferOwnerString"),
        ("PDN-CONTROL-MIB", "devFileXferStatus"),
        ("PDN-CONTROL-MIB", "devFileXferErrorStatus"),
        ("PDN-CONTROL-MIB", "devFileXferSendEvent"),
        ("PDN-CONTROL-MIB", "devFileXferRowStatus"),
        ("PDN-CONTROL-MIB", "devFileXferXferTime"))
)
if mibBuilder.loadTexts:
    devFileXferMIBGroup.setStatus("current")

devFirmwareControlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 8)
)
devFirmwareControlGroup.setObjects(
      *(("PDN-CONTROL-MIB", "devFirmwareControlIndex"),
        ("PDN-CONTROL-MIB", "devFirmwareControlRelease"),
        ("PDN-CONTROL-MIB", "devFirmwareControlOperStatus"),
        ("PDN-CONTROL-MIB", "devFirmwareControlAdminStatus"))
)
if mibBuilder.loadTexts:
    devFirmwareControlGroup.setStatus("current")

devConfigChangeMgmtGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 9)
)
devConfigChangeMgmtGroup.setObjects(
      *(("PDN-CONTROL-MIB", "pdnCCMAutoBackupType"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoBackupFixedDay"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoBackupFixedTime"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoBackupDynamicTime"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoBackupAppendTimeStampToFilename"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoBackupFilename"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoBackupServerIpAddress"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoBackupUserName"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoBackupUserPassword"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoBackupUserAccount"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoBackupCopyProtocol"),
        ("PDN-CONTROL-MIB", "pdnCCMAutoRestore"),
        ("PDN-CONTROL-MIB", "pdnCCMResyncOperation"),
        ("PDN-CONTROL-MIB", "pdnCCMOperation"))
)
if mibBuilder.loadTexts:
    devConfigChangeMgmtGroup.setStatus("current")

pdnAutoFwGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 12)
)
pdnAutoFwGroup.setObjects(
      *(("PDN-CONTROL-MIB", "devIsAutoFwEnabled"),
        ("PDN-CONTROL-MIB", "devAutoFwStatus"))
)
if mibBuilder.loadTexts:
    pdnAutoFwGroup.setStatus("current")

pdnDevFileXferMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 14)
)
pdnDevFileXferMIBGroup.setObjects(
      *(("PDN-CONTROL-MIB", "pdnDevFileXferifIndex"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferFileName"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferCopyProtocol"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferFileType"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferServerIpAddress"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferUserName"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferUserPassword"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferUserAccount"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferOperation"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferPktsSent"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferPktsRecv"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferOctetsSent"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferOctetsRecv"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferOwnerString"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferStatus"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferApply"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferErrorStatus"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferSendEvent"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferXferTime"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferRowStatus"))
)
if mibBuilder.loadTexts:
    pdnDevFileXferMIBGroup.setStatus("current")

devNextTableObjectMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 15)
)
devNextTableObjectMIBGroup.setObjects(
    ("PDN-CONTROL-MIB", "pdnDevFileXferSessionIDNext")
)
if mibBuilder.loadTexts:
    devNextTableObjectMIBGroup.setStatus("current")


# Notification objects

devFileXferEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 0, 1)
)
devFileXferEvent.setObjects(
      *(("PDN-CONTROL-MIB", "devFileXferStatus"),
        ("PDN-CONTROL-MIB", "devFileXferErrorStatus"),
        ("PDN-CONTROL-MIB", "devFileXferOperation"),
        ("PDN-CONTROL-MIB", "devFileXferFileType"),
        ("PDN-CONTROL-MIB", "devFileXferFileName"))
)
if mibBuilder.loadTexts:
    devFileXferEvent.setStatus(
        "current"
    )

devAutoBackupFailEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 0, 2)
)
devAutoBackupFailEvent.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    devAutoBackupFailEvent.setStatus(
        "current"
    )

devConfigRestoreFailEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 0, 3)
)
devConfigRestoreFailEvent.setObjects(
    ("ENTITY-MIB", "entPhysicalIndex")
)
if mibBuilder.loadTexts:
    devConfigRestoreFailEvent.setStatus(
        "current"
    )

devAutoFwEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 0, 4)
)
devAutoFwEvent.setObjects(
    ("PDN-CONTROL-MIB", "devAutoFwStatus")
)
if mibBuilder.loadTexts:
    devAutoFwEvent.setStatus(
        "current"
    )

pdnDevFileXferEvent = NotificationType(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 0, 5)
)
pdnDevFileXferEvent.setObjects(
      *(("PDN-CONTROL-MIB", "pdnDevFileXferStatus"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferErrorStatus"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferOperation"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferFileType"),
        ("PDN-CONTROL-MIB", "pdnDevFileXferFileName"))
)
if mibBuilder.loadTexts:
    pdnDevFileXferEvent.setStatus(
        "current"
    )


# Notifications groups

devFileXferEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 10)
)
devFileXferEventGroup.setObjects(
    ("PDN-CONTROL-MIB", "devFileXferEvent")
)
if mibBuilder.loadTexts:
    devFileXferEventGroup.setStatus(
        "current"
    )

devCCMEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 11)
)
devCCMEventGroup.setObjects(
      *(("PDN-CONTROL-MIB", "devAutoBackupFailEvent"),
        ("PDN-CONTROL-MIB", "devConfigRestoreFailEvent"))
)
if mibBuilder.loadTexts:
    devCCMEventGroup.setStatus(
        "current"
    )

devAutoFwEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 13)
)
devAutoFwEventGroup.setObjects(
    ("PDN-CONTROL-MIB", "devAutoFwEvent")
)
if mibBuilder.loadTexts:
    devAutoFwEventGroup.setStatus(
        "current"
    )

pdnDevFileXferEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 10, 11, 16)
)
pdnDevFileXferEventGroup.setObjects(
    ("PDN-CONTROL-MIB", "pdnDevFileXferEvent")
)
if mibBuilder.loadTexts:
    pdnDevFileXferEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "PDN-CONTROL-MIB",
    **{"pdnControl": pdnControl,
       "pdnControlMIBTrapsV2": pdnControlMIBTrapsV2,
       "devFileXferEvent": devFileXferEvent,
       "devAutoBackupFailEvent": devAutoBackupFailEvent,
       "devConfigRestoreFailEvent": devConfigRestoreFailEvent,
       "devAutoFwEvent": devAutoFwEvent,
       "pdnDevFileXferEvent": pdnDevFileXferEvent,
       "devHWControlReset": devHWControlReset,
       "devControlTestTable": devControlTestTable,
       "devControlTestEntry": devControlTestEntry,
       "devControlTest": devControlTest,
       "devControlTestStatus": devControlTestStatus,
       "devControlTestCmd": devControlTestCmd,
       "devControlDownLoadTable": devControlDownLoadTable,
       "devControlDownLoadEntry": devControlDownLoadEntry,
       "devControlDownLoadIndex": devControlDownLoadIndex,
       "devControlDownLoadRelease": devControlDownLoadRelease,
       "devControlDownLoadOperStatus": devControlDownLoadOperStatus,
       "devControlDownLoadAdminStatus": devControlDownLoadAdminStatus,
       "devControlRMON": devControlRMON,
       "devControlRMONAdminStatus": devControlRMONAdminStatus,
       "devSNSwitchFirmwareTable": devSNSwitchFirmwareTable,
       "devSNSwitchFirmwareEntry": devSNSwitchFirmwareEntry,
       "devSNSwitchFirmwareIndex": devSNSwitchFirmwareIndex,
       "devSNSwitchFirmwareBank": devSNSwitchFirmwareBank,
       "devControlFTP": devControlFTP,
       "devControlFTPRate": devControlFTPRate,
       "devFileXferMIBObjects": devFileXferMIBObjects,
       "devFileXferConfigTable": devFileXferConfigTable,
       "devFileXferConfigEntry": devFileXferConfigEntry,
       "devFileXferFileName": devFileXferFileName,
       "devFileXferCopyProtocol": devFileXferCopyProtocol,
       "devFileXferFileType": devFileXferFileType,
       "devFileXferServerIpAddress": devFileXferServerIpAddress,
       "devFileXferUserName": devFileXferUserName,
       "devFileXferUserPassword": devFileXferUserPassword,
       "devFileXferOperation": devFileXferOperation,
       "devFileXferPktsSent": devFileXferPktsSent,
       "devFileXferPktsRecv": devFileXferPktsRecv,
       "devFileXferOctetsSent": devFileXferOctetsSent,
       "devFileXferOctetsRecv": devFileXferOctetsRecv,
       "devFileXferOwnerString": devFileXferOwnerString,
       "devFileXferStatus": devFileXferStatus,
       "devFileXferErrorStatus": devFileXferErrorStatus,
       "devFileXferSendEvent": devFileXferSendEvent,
       "devFileXferRowStatus": devFileXferRowStatus,
       "devFileXferXferTime": devFileXferXferTime,
       "pdnDevFileXferTable": pdnDevFileXferTable,
       "pdnDevFileXferEntry": pdnDevFileXferEntry,
       "pdnDevFileXferSessionID": pdnDevFileXferSessionID,
       "pdnDevFileXferifIndex": pdnDevFileXferifIndex,
       "pdnDevFileXferFileName": pdnDevFileXferFileName,
       "pdnDevFileXferCopyProtocol": pdnDevFileXferCopyProtocol,
       "pdnDevFileXferFileType": pdnDevFileXferFileType,
       "pdnDevFileXferServerIpAddress": pdnDevFileXferServerIpAddress,
       "pdnDevFileXferUserName": pdnDevFileXferUserName,
       "pdnDevFileXferUserPassword": pdnDevFileXferUserPassword,
       "pdnDevFileXferUserAccount": pdnDevFileXferUserAccount,
       "pdnDevFileXferOperation": pdnDevFileXferOperation,
       "pdnDevFileXferPktsSent": pdnDevFileXferPktsSent,
       "pdnDevFileXferPktsRecv": pdnDevFileXferPktsRecv,
       "pdnDevFileXferOctetsSent": pdnDevFileXferOctetsSent,
       "pdnDevFileXferOctetsRecv": pdnDevFileXferOctetsRecv,
       "pdnDevFileXferOwnerString": pdnDevFileXferOwnerString,
       "pdnDevFileXferStatus": pdnDevFileXferStatus,
       "pdnDevFileXferApply": pdnDevFileXferApply,
       "pdnDevFileXferErrorStatus": pdnDevFileXferErrorStatus,
       "pdnDevFileXferSendEvent": pdnDevFileXferSendEvent,
       "pdnDevFileXferXferTime": pdnDevFileXferXferTime,
       "pdnDevFileXferRowStatus": pdnDevFileXferRowStatus,
       "pdnDevFileXferSessionIDNext": pdnDevFileXferSessionIDNext,
       "devFileXferMIBTraps": devFileXferMIBTraps,
       "devFirmwareControlMIBObjects": devFirmwareControlMIBObjects,
       "devFirmwareControlTable": devFirmwareControlTable,
       "devFirmwareControlEntry": devFirmwareControlEntry,
       "devFirmwareControlIndex": devFirmwareControlIndex,
       "devFirmwareControlRelease": devFirmwareControlRelease,
       "devFirmwareControlOperStatus": devFirmwareControlOperStatus,
       "devFirmwareControlAdminStatus": devFirmwareControlAdminStatus,
       "pdnConfigChangeMgmt": pdnConfigChangeMgmt,
       "pdnCCMAutoBackup": pdnCCMAutoBackup,
       "pdnCCMAutoBackupType": pdnCCMAutoBackupType,
       "pdnCCMAutoBackupFixedDay": pdnCCMAutoBackupFixedDay,
       "pdnCCMAutoBackupFixedTime": pdnCCMAutoBackupFixedTime,
       "pdnCCMAutoBackupDynamicTime": pdnCCMAutoBackupDynamicTime,
       "pdnCCMAutoBackupAppendTimeStampToFilename": pdnCCMAutoBackupAppendTimeStampToFilename,
       "pdnCCMAutoBackupFilename": pdnCCMAutoBackupFilename,
       "pdnCCMAutoBackupServerIpAddress": pdnCCMAutoBackupServerIpAddress,
       "pdnCCMAutoBackupUserName": pdnCCMAutoBackupUserName,
       "pdnCCMAutoBackupUserPassword": pdnCCMAutoBackupUserPassword,
       "pdnCCMAutoBackupUserAccount": pdnCCMAutoBackupUserAccount,
       "pdnCCMAutoBackupCopyProtocol": pdnCCMAutoBackupCopyProtocol,
       "pdnCCMAutoRestore": pdnCCMAutoRestore,
       "pdnCCMResyncOperation": pdnCCMResyncOperation,
       "pdnCCMOperation": pdnCCMOperation,
       "pdnControlMIBGroups": pdnControlMIBGroups,
       "devResetGroup": devResetGroup,
       "devControlTestGroup": devControlTestGroup,
       "devControlDownloadGroup": devControlDownloadGroup,
       "devControlRMONGroup": devControlRMONGroup,
       "devSNSwitchFirmwareGroup": devSNSwitchFirmwareGroup,
       "devControlFTPGroup": devControlFTPGroup,
       "devFileXferMIBGroup": devFileXferMIBGroup,
       "devFirmwareControlGroup": devFirmwareControlGroup,
       "devConfigChangeMgmtGroup": devConfigChangeMgmtGroup,
       "devFileXferEventGroup": devFileXferEventGroup,
       "devCCMEventGroup": devCCMEventGroup,
       "pdnAutoFwGroup": pdnAutoFwGroup,
       "devAutoFwEventGroup": devAutoFwEventGroup,
       "pdnDevFileXferMIBGroup": pdnDevFileXferMIBGroup,
       "devNextTableObjectMIBGroup": devNextTableObjectMIBGroup,
       "pdnDevFileXferEventGroup": pdnDevFileXferEventGroup,
       "pdnAutoFw": pdnAutoFw,
       "devIsAutoFwEnabled": devIsAutoFwEnabled,
       "devAutoFwStatus": devAutoFwStatus}
)
