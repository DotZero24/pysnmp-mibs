# SNMP MIB module (FS-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-SECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:28 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

fsSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6)
)
if mibBuilder.loadTexts:
    fsSecurityMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsSecurityMIBObjects_ObjectIdentity = ObjectIdentity
fsSecurityMIBObjects = _FsSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1)
)
_FsUserManagementObjects_ObjectIdentity = ObjectIdentity
fsUserManagementObjects = _FsUserManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1)
)
_FsEnableSnmpAgent_Type = EnabledStatus
_FsEnableSnmpAgent_Object = MibScalar
fsEnableSnmpAgent = _FsEnableSnmpAgent_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 1),
    _FsEnableSnmpAgent_Type()
)
fsEnableSnmpAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEnableSnmpAgent.setStatus("current")
_FsEnableWeb_Type = EnabledStatus
_FsEnableWeb_Object = MibScalar
fsEnableWeb = _FsEnableWeb_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 2),
    _FsEnableWeb_Type()
)
fsEnableWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEnableWeb.setStatus("current")
_FsEnableTelnet_Type = EnabledStatus
_FsEnableTelnet_Object = MibScalar
fsEnableTelnet = _FsEnableTelnet_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 3),
    _FsEnableTelnet_Type()
)
fsEnableTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsEnableTelnet.setStatus("current")
_FsTelnetHostIpTable_Object = MibTable
fsTelnetHostIpTable = _FsTelnetHostIpTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    fsTelnetHostIpTable.setStatus("current")
_FsTelnetHostIpEntry_Object = MibTableRow
fsTelnetHostIpEntry = _FsTelnetHostIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 4, 1)
)
fsTelnetHostIpEntry.setIndexNames(
    (0, "FS-SECURITY-MIB", "fsTelnetHostIpAddress"),
)
if mibBuilder.loadTexts:
    fsTelnetHostIpEntry.setStatus("current")
_FsTelnetHostIpAddress_Type = IpAddress
_FsTelnetHostIpAddress_Object = MibTableColumn
fsTelnetHostIpAddress = _FsTelnetHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 4, 1, 1),
    _FsTelnetHostIpAddress_Type()
)
fsTelnetHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsTelnetHostIpAddress.setStatus("current")


class _FsTelnetHostIpEnable_Type(Integer32):
    """Custom type fsTelnetHostIpEnable based on Integer32"""
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


_FsTelnetHostIpEnable_Type.__name__ = "Integer32"
_FsTelnetHostIpEnable_Object = MibTableColumn
fsTelnetHostIpEnable = _FsTelnetHostIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 4, 1, 2),
    _FsTelnetHostIpEnable_Type()
)
fsTelnetHostIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsTelnetHostIpEnable.setStatus("current")
_FsWebHostIpTable_Object = MibTable
fsWebHostIpTable = _FsWebHostIpTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fsWebHostIpTable.setStatus("current")
_FsWebHostIpEntry_Object = MibTableRow
fsWebHostIpEntry = _FsWebHostIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 5, 1)
)
fsWebHostIpEntry.setIndexNames(
    (0, "FS-SECURITY-MIB", "fsWebHostIpAddress"),
)
if mibBuilder.loadTexts:
    fsWebHostIpEntry.setStatus("current")
_FsWebHostIpAddress_Type = IpAddress
_FsWebHostIpAddress_Object = MibTableColumn
fsWebHostIpAddress = _FsWebHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 5, 1, 1),
    _FsWebHostIpAddress_Type()
)
fsWebHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsWebHostIpAddress.setStatus("current")


class _FsWebHostIpEnable_Type(Integer32):
    """Custom type fsWebHostIpEnable based on Integer32"""
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


_FsWebHostIpEnable_Type.__name__ = "Integer32"
_FsWebHostIpEnable_Object = MibTableColumn
fsWebHostIpEnable = _FsWebHostIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 1, 5, 1, 2),
    _FsWebHostIpEnable_Type()
)
fsWebHostIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsWebHostIpEnable.setStatus("current")
_FsSecurityAddressObjects_ObjectIdentity = ObjectIdentity
fsSecurityAddressObjects = _FsSecurityAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2)
)
_FsSecurityAddressTable_Object = MibTable
fsSecurityAddressTable = _FsSecurityAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsSecurityAddressTable.setStatus("current")
_FsSecurityAddressEntry_Object = MibTableRow
fsSecurityAddressEntry = _FsSecurityAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 1, 1)
)
fsSecurityAddressEntry.setIndexNames(
    (0, "FS-SECURITY-MIB", "fsSecurityAddressFdbId"),
    (0, "FS-SECURITY-MIB", "fsSecurityAddressAddress"),
    (0, "FS-SECURITY-MIB", "fsSecurityAddressPort"),
    (0, "FS-SECURITY-MIB", "fsSecurityAddressIpAddr"),
)
if mibBuilder.loadTexts:
    fsSecurityAddressEntry.setStatus("current")
_FsSecurityAddressFdbId_Type = Unsigned32
_FsSecurityAddressFdbId_Object = MibTableColumn
fsSecurityAddressFdbId = _FsSecurityAddressFdbId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 1, 1, 1),
    _FsSecurityAddressFdbId_Type()
)
fsSecurityAddressFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSecurityAddressFdbId.setStatus("current")
_FsSecurityAddressAddress_Type = MacAddress
_FsSecurityAddressAddress_Object = MibTableColumn
fsSecurityAddressAddress = _FsSecurityAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 1, 1, 2),
    _FsSecurityAddressAddress_Type()
)
fsSecurityAddressAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSecurityAddressAddress.setStatus("current")
_FsSecurityAddressPort_Type = IfIndex
_FsSecurityAddressPort_Object = MibTableColumn
fsSecurityAddressPort = _FsSecurityAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 1, 1, 3),
    _FsSecurityAddressPort_Type()
)
fsSecurityAddressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSecurityAddressPort.setStatus("current")
_FsSecurityAddressIpAddr_Type = IpAddress
_FsSecurityAddressIpAddr_Object = MibTableColumn
fsSecurityAddressIpAddr = _FsSecurityAddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 1, 1, 4),
    _FsSecurityAddressIpAddr_Type()
)
fsSecurityAddressIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsSecurityAddressIpAddr.setStatus("current")
_FsSecurityAddressIfBindIp_Type = TruthValue
_FsSecurityAddressIfBindIp_Object = MibTableColumn
fsSecurityAddressIfBindIp = _FsSecurityAddressIfBindIp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 1, 1, 5),
    _FsSecurityAddressIfBindIp_Type()
)
fsSecurityAddressIfBindIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecurityAddressIfBindIp.setStatus("current")
_FsSecurityAddressRemainAge_Type = Integer32
_FsSecurityAddressRemainAge_Object = MibTableColumn
fsSecurityAddressRemainAge = _FsSecurityAddressRemainAge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 1, 1, 6),
    _FsSecurityAddressRemainAge_Type()
)
fsSecurityAddressRemainAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSecurityAddressRemainAge.setStatus("current")


class _FsSecurityAddressType_Type(Integer32):
    """Custom type fsSecurityAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("secureConfigured", 1),
          ("dynamicLearn", 2))
    )


_FsSecurityAddressType_Type.__name__ = "Integer32"
_FsSecurityAddressType_Object = MibTableColumn
fsSecurityAddressType = _FsSecurityAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 1, 1, 7),
    _FsSecurityAddressType_Type()
)
fsSecurityAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsSecurityAddressType.setStatus("current")
_FsSecurityAddressStatus_Type = RowStatus
_FsSecurityAddressStatus_Object = MibTableColumn
fsSecurityAddressStatus = _FsSecurityAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 1, 1, 8),
    _FsSecurityAddressStatus_Type()
)
fsSecurityAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsSecurityAddressStatus.setStatus("current")
_FsBindAddressTable_Object = MibTable
fsBindAddressTable = _FsBindAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsBindAddressTable.setStatus("current")
_FsBindAddressEntry_Object = MibTableRow
fsBindAddressEntry = _FsBindAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 2, 1)
)
fsBindAddressEntry.setIndexNames(
    (0, "FS-SECURITY-MIB", "fsBindAddressIpAddr"),
)
if mibBuilder.loadTexts:
    fsBindAddressEntry.setStatus("current")
_FsBindAddressIpAddr_Type = IpAddress
_FsBindAddressIpAddr_Object = MibTableColumn
fsBindAddressIpAddr = _FsBindAddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 2, 1, 1),
    _FsBindAddressIpAddr_Type()
)
fsBindAddressIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsBindAddressIpAddr.setStatus("current")
_FsBindMacAddress_Type = MacAddress
_FsBindMacAddress_Object = MibTableColumn
fsBindMacAddress = _FsBindMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 2, 1, 2),
    _FsBindMacAddress_Type()
)
fsBindMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBindMacAddress.setStatus("current")
_FsBindAddressStatus_Type = ConfigStatus
_FsBindAddressStatus_Object = MibTableColumn
fsBindAddressStatus = _FsBindAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 2, 2, 1, 3),
    _FsBindAddressStatus_Type()
)
fsBindAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsBindAddressStatus.setStatus("current")
_FsPortSecrrityObjects_ObjectIdentity = ObjectIdentity
fsPortSecrrityObjects = _FsPortSecrrityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3)
)
_FsPortSecurityTable_Object = MibTable
fsPortSecurityTable = _FsPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsPortSecurityTable.setStatus("current")
_FsPortSecurityEntry_Object = MibTableRow
fsPortSecurityEntry = _FsPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1, 1)
)
fsPortSecurityEntry.setIndexNames(
    (0, "FS-SECURITY-MIB", "fsPortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    fsPortSecurityEntry.setStatus("current")
_FsPortSecurityPortIndex_Type = IfIndex
_FsPortSecurityPortIndex_Object = MibTableColumn
fsPortSecurityPortIndex = _FsPortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1, 1, 1),
    _FsPortSecurityPortIndex_Type()
)
fsPortSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPortSecurityPortIndex.setStatus("current")


class _FsPortSecurityStatus_Type(EnabledStatus):
    """Custom type fsPortSecurityStatus based on EnabledStatus"""
    defaultValue = 2


_FsPortSecurityStatus_Type.__name__ = "EnabledStatus"
_FsPortSecurityStatus_Object = MibTableColumn
fsPortSecurityStatus = _FsPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1, 1, 2),
    _FsPortSecurityStatus_Type()
)
fsPortSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPortSecurityStatus.setStatus("current")


class _FsPortSecurViolationType_Type(Integer32):
    """Custom type fsPortSecurViolationType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("violation-protect", 1),
          ("violation-restrict", 2),
          ("violation-shutdown", 3))
    )


_FsPortSecurViolationType_Type.__name__ = "Integer32"
_FsPortSecurViolationType_Object = MibTableColumn
fsPortSecurViolationType = _FsPortSecurViolationType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1, 1, 3),
    _FsPortSecurViolationType_Type()
)
fsPortSecurViolationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPortSecurViolationType.setStatus("current")
_FsPortSecurityAddrNum_Type = Integer32
_FsPortSecurityAddrNum_Object = MibTableColumn
fsPortSecurityAddrNum = _FsPortSecurityAddrNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1, 1, 4),
    _FsPortSecurityAddrNum_Type()
)
fsPortSecurityAddrNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPortSecurityAddrNum.setStatus("current")
_FsPortSecurityAddrAge_Type = Integer32
_FsPortSecurityAddrAge_Object = MibTableColumn
fsPortSecurityAddrAge = _FsPortSecurityAddrAge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1, 1, 5),
    _FsPortSecurityAddrAge_Type()
)
fsPortSecurityAddrAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPortSecurityAddrAge.setStatus("current")
_FsPortStaticSecurAddrIfAge_Type = EnabledStatus
_FsPortStaticSecurAddrIfAge_Object = MibTableColumn
fsPortStaticSecurAddrIfAge = _FsPortStaticSecurAddrIfAge_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1, 1, 6),
    _FsPortStaticSecurAddrIfAge_Type()
)
fsPortStaticSecurAddrIfAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsPortStaticSecurAddrIfAge.setStatus("current")
_FsPortSecurityAddressCurrentNum_Type = Integer32
_FsPortSecurityAddressCurrentNum_Object = MibTableColumn
fsPortSecurityAddressCurrentNum = _FsPortSecurityAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1, 1, 7),
    _FsPortSecurityAddressCurrentNum_Type()
)
fsPortSecurityAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPortSecurityAddressCurrentNum.setStatus("current")
_FsPortStaticSecurAddrCurrentNum_Type = Integer32
_FsPortStaticSecurAddrCurrentNum_Object = MibTableColumn
fsPortStaticSecurAddrCurrentNum = _FsPortStaticSecurAddrCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1, 1, 8),
    _FsPortStaticSecurAddrCurrentNum_Type()
)
fsPortStaticSecurAddrCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPortStaticSecurAddrCurrentNum.setStatus("current")


class _FsPortSecurityIpDistrMode_Type(Integer32):
    """Custom type fsPortSecurityIpDistrMode based on Integer32"""
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
        *(("static", 1),
          ("dynamic", 2),
          ("staticAndDynamic", 3),
          ("unSpecified", 4))
    )


_FsPortSecurityIpDistrMode_Type.__name__ = "Integer32"
_FsPortSecurityIpDistrMode_Object = MibTableColumn
fsPortSecurityIpDistrMode = _FsPortSecurityIpDistrMode_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 1, 3, 1, 1, 9),
    _FsPortSecurityIpDistrMode_Type()
)
fsPortSecurityIpDistrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsPortSecurityIpDistrMode.setStatus("current")
_FsSecurityTraps_ObjectIdentity = ObjectIdentity
fsSecurityTraps = _FsSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 2)
)
_FsSecurityMIBConformance_ObjectIdentity = ObjectIdentity
fsSecurityMIBConformance = _FsSecurityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 3)
)
_FsSecurityMIBCompliances_ObjectIdentity = ObjectIdentity
fsSecurityMIBCompliances = _FsSecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 3, 1)
)
_FsSecurityMIBGroups_ObjectIdentity = ObjectIdentity
fsSecurityMIBGroups = _FsSecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 3, 2)
)

# Managed Objects groups

fsUserManageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 3, 2, 1)
)
fsUserManageMIBGroup.setObjects(
      *(("FS-SECURITY-MIB", "fsEnableSnmpAgent"),
        ("FS-SECURITY-MIB", "fsEnableWeb"),
        ("FS-SECURITY-MIB", "fsEnableTelnet"))
)
if mibBuilder.loadTexts:
    fsUserManageMIBGroup.setStatus("current")

fsSecurityAddressMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 3, 2, 2)
)
fsSecurityAddressMIBGroup.setObjects(
      *(("FS-SECURITY-MIB", "fsSecurityAddressIfBindIp"),
        ("FS-SECURITY-MIB", "fsSecurityAddressRemainAge"),
        ("FS-SECURITY-MIB", "fsSecurityAddressType"),
        ("FS-SECURITY-MIB", "fsSecurityAddressStatus"),
        ("FS-SECURITY-MIB", "fsBindMacAddress"),
        ("FS-SECURITY-MIB", "fsBindAddressStatus"))
)
if mibBuilder.loadTexts:
    fsSecurityAddressMIBGroup.setStatus("current")

fsPortSecurityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 3, 2, 3)
)
fsPortSecurityMIBGroup.setObjects(
      *(("FS-SECURITY-MIB", "fsPortSecurityPortIndex"),
        ("FS-SECURITY-MIB", "fsPortSecurityStatus"),
        ("FS-SECURITY-MIB", "fsPortSecurViolationType"),
        ("FS-SECURITY-MIB", "fsPortSecurityAddrNum"),
        ("FS-SECURITY-MIB", "fsPortSecurityAddrAge"),
        ("FS-SECURITY-MIB", "fsPortStaticSecurAddrIfAge"),
        ("FS-SECURITY-MIB", "fsPortSecurityAddressCurrentNum"),
        ("FS-SECURITY-MIB", "fsPortStaticSecurAddrCurrentNum"),
        ("FS-SECURITY-MIB", "fsPortSecurityIpDistrMode"))
)
if mibBuilder.loadTexts:
    fsPortSecurityMIBGroup.setStatus("current")


# Notification objects

portSecurityViolate = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 2, 1)
)
portSecurityViolate.setObjects(
    ("IF-MIB", "ifIndex")
)
if mibBuilder.loadTexts:
    portSecurityViolate.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsSecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 6, 3, 1, 1)
)
fsSecurityMIBCompliance.setObjects(
      *(("FS-SECURITY-MIB", "fsUserManageMIBGroup"),
        ("FS-SECURITY-MIB", "fsSecurityAddressMIBGroup"),
        ("FS-SECURITY-MIB", "fsPortSecurityMIBGroup"))
)
if mibBuilder.loadTexts:
    fsSecurityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-SECURITY-MIB",
    **{"fsSecurityMIB": fsSecurityMIB,
       "fsSecurityMIBObjects": fsSecurityMIBObjects,
       "fsUserManagementObjects": fsUserManagementObjects,
       "fsEnableSnmpAgent": fsEnableSnmpAgent,
       "fsEnableWeb": fsEnableWeb,
       "fsEnableTelnet": fsEnableTelnet,
       "fsTelnetHostIpTable": fsTelnetHostIpTable,
       "fsTelnetHostIpEntry": fsTelnetHostIpEntry,
       "fsTelnetHostIpAddress": fsTelnetHostIpAddress,
       "fsTelnetHostIpEnable": fsTelnetHostIpEnable,
       "fsWebHostIpTable": fsWebHostIpTable,
       "fsWebHostIpEntry": fsWebHostIpEntry,
       "fsWebHostIpAddress": fsWebHostIpAddress,
       "fsWebHostIpEnable": fsWebHostIpEnable,
       "fsSecurityAddressObjects": fsSecurityAddressObjects,
       "fsSecurityAddressTable": fsSecurityAddressTable,
       "fsSecurityAddressEntry": fsSecurityAddressEntry,
       "fsSecurityAddressFdbId": fsSecurityAddressFdbId,
       "fsSecurityAddressAddress": fsSecurityAddressAddress,
       "fsSecurityAddressPort": fsSecurityAddressPort,
       "fsSecurityAddressIpAddr": fsSecurityAddressIpAddr,
       "fsSecurityAddressIfBindIp": fsSecurityAddressIfBindIp,
       "fsSecurityAddressRemainAge": fsSecurityAddressRemainAge,
       "fsSecurityAddressType": fsSecurityAddressType,
       "fsSecurityAddressStatus": fsSecurityAddressStatus,
       "fsBindAddressTable": fsBindAddressTable,
       "fsBindAddressEntry": fsBindAddressEntry,
       "fsBindAddressIpAddr": fsBindAddressIpAddr,
       "fsBindMacAddress": fsBindMacAddress,
       "fsBindAddressStatus": fsBindAddressStatus,
       "fsPortSecrrityObjects": fsPortSecrrityObjects,
       "fsPortSecurityTable": fsPortSecurityTable,
       "fsPortSecurityEntry": fsPortSecurityEntry,
       "fsPortSecurityPortIndex": fsPortSecurityPortIndex,
       "fsPortSecurityStatus": fsPortSecurityStatus,
       "fsPortSecurViolationType": fsPortSecurViolationType,
       "fsPortSecurityAddrNum": fsPortSecurityAddrNum,
       "fsPortSecurityAddrAge": fsPortSecurityAddrAge,
       "fsPortStaticSecurAddrIfAge": fsPortStaticSecurAddrIfAge,
       "fsPortSecurityAddressCurrentNum": fsPortSecurityAddressCurrentNum,
       "fsPortStaticSecurAddrCurrentNum": fsPortStaticSecurAddrCurrentNum,
       "fsPortSecurityIpDistrMode": fsPortSecurityIpDistrMode,
       "fsSecurityTraps": fsSecurityTraps,
       "portSecurityViolate": portSecurityViolate,
       "fsSecurityMIBConformance": fsSecurityMIBConformance,
       "fsSecurityMIBCompliances": fsSecurityMIBCompliances,
       "fsSecurityMIBCompliance": fsSecurityMIBCompliance,
       "fsSecurityMIBGroups": fsSecurityMIBGroups,
       "fsUserManageMIBGroup": fsUserManageMIBGroup,
       "fsSecurityAddressMIBGroup": fsSecurityAddressMIBGroup,
       "fsPortSecurityMIBGroup": fsPortSecurityMIBGroup}
)
