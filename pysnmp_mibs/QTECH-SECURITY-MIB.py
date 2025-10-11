# SNMP MIB module (QTECH-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-SECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:49 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "QTECH-TC",
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

qtechSecurityMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6)
)
if mibBuilder.loadTexts:
    qtechSecurityMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechSecurityMIBObjects_ObjectIdentity = ObjectIdentity
qtechSecurityMIBObjects = _QtechSecurityMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1)
)
_QtechUserManagementObjects_ObjectIdentity = ObjectIdentity
qtechUserManagementObjects = _QtechUserManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1)
)
_QtechEnableSnmpAgent_Type = EnabledStatus
_QtechEnableSnmpAgent_Object = MibScalar
qtechEnableSnmpAgent = _QtechEnableSnmpAgent_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 1),
    _QtechEnableSnmpAgent_Type()
)
qtechEnableSnmpAgent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechEnableSnmpAgent.setStatus("current")
_QtechEnableWeb_Type = EnabledStatus
_QtechEnableWeb_Object = MibScalar
qtechEnableWeb = _QtechEnableWeb_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 2),
    _QtechEnableWeb_Type()
)
qtechEnableWeb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechEnableWeb.setStatus("current")
_QtechEnableTelnet_Type = EnabledStatus
_QtechEnableTelnet_Object = MibScalar
qtechEnableTelnet = _QtechEnableTelnet_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 3),
    _QtechEnableTelnet_Type()
)
qtechEnableTelnet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechEnableTelnet.setStatus("current")
_QtechTelnetHostIpTable_Object = MibTable
qtechTelnetHostIpTable = _QtechTelnetHostIpTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 4)
)
if mibBuilder.loadTexts:
    qtechTelnetHostIpTable.setStatus("current")
_QtechTelnetHostIpEntry_Object = MibTableRow
qtechTelnetHostIpEntry = _QtechTelnetHostIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 4, 1)
)
qtechTelnetHostIpEntry.setIndexNames(
    (0, "QTECH-SECURITY-MIB", "qtechTelnetHostIpAddress"),
)
if mibBuilder.loadTexts:
    qtechTelnetHostIpEntry.setStatus("current")
_QtechTelnetHostIpAddress_Type = IpAddress
_QtechTelnetHostIpAddress_Object = MibTableColumn
qtechTelnetHostIpAddress = _QtechTelnetHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 4, 1, 1),
    _QtechTelnetHostIpAddress_Type()
)
qtechTelnetHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechTelnetHostIpAddress.setStatus("current")


class _QtechTelnetHostIpEnable_Type(Integer32):
    """Custom type qtechTelnetHostIpEnable based on Integer32"""
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


_QtechTelnetHostIpEnable_Type.__name__ = "Integer32"
_QtechTelnetHostIpEnable_Object = MibTableColumn
qtechTelnetHostIpEnable = _QtechTelnetHostIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 4, 1, 2),
    _QtechTelnetHostIpEnable_Type()
)
qtechTelnetHostIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechTelnetHostIpEnable.setStatus("current")
_QtechWebHostIpTable_Object = MibTable
qtechWebHostIpTable = _QtechWebHostIpTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 5)
)
if mibBuilder.loadTexts:
    qtechWebHostIpTable.setStatus("current")
_QtechWebHostIpEntry_Object = MibTableRow
qtechWebHostIpEntry = _QtechWebHostIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 5, 1)
)
qtechWebHostIpEntry.setIndexNames(
    (0, "QTECH-SECURITY-MIB", "qtechWebHostIpAddress"),
)
if mibBuilder.loadTexts:
    qtechWebHostIpEntry.setStatus("current")
_QtechWebHostIpAddress_Type = IpAddress
_QtechWebHostIpAddress_Object = MibTableColumn
qtechWebHostIpAddress = _QtechWebHostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 5, 1, 1),
    _QtechWebHostIpAddress_Type()
)
qtechWebHostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechWebHostIpAddress.setStatus("current")


class _QtechWebHostIpEnable_Type(Integer32):
    """Custom type qtechWebHostIpEnable based on Integer32"""
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


_QtechWebHostIpEnable_Type.__name__ = "Integer32"
_QtechWebHostIpEnable_Object = MibTableColumn
qtechWebHostIpEnable = _QtechWebHostIpEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 1, 5, 1, 2),
    _QtechWebHostIpEnable_Type()
)
qtechWebHostIpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechWebHostIpEnable.setStatus("current")
_QtechSecurityAddressObjects_ObjectIdentity = ObjectIdentity
qtechSecurityAddressObjects = _QtechSecurityAddressObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2)
)
_QtechSecurityAddressTable_Object = MibTable
qtechSecurityAddressTable = _QtechSecurityAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qtechSecurityAddressTable.setStatus("current")
_QtechSecurityAddressEntry_Object = MibTableRow
qtechSecurityAddressEntry = _QtechSecurityAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 1, 1)
)
qtechSecurityAddressEntry.setIndexNames(
    (0, "QTECH-SECURITY-MIB", "qtechSecurityAddressFdbId"),
    (0, "QTECH-SECURITY-MIB", "qtechSecurityAddressAddress"),
    (0, "QTECH-SECURITY-MIB", "qtechSecurityAddressPort"),
    (0, "QTECH-SECURITY-MIB", "qtechSecurityAddressIpAddr"),
)
if mibBuilder.loadTexts:
    qtechSecurityAddressEntry.setStatus("current")
_QtechSecurityAddressFdbId_Type = Unsigned32
_QtechSecurityAddressFdbId_Object = MibTableColumn
qtechSecurityAddressFdbId = _QtechSecurityAddressFdbId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 1, 1, 1),
    _QtechSecurityAddressFdbId_Type()
)
qtechSecurityAddressFdbId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechSecurityAddressFdbId.setStatus("current")
_QtechSecurityAddressAddress_Type = MacAddress
_QtechSecurityAddressAddress_Object = MibTableColumn
qtechSecurityAddressAddress = _QtechSecurityAddressAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 1, 1, 2),
    _QtechSecurityAddressAddress_Type()
)
qtechSecurityAddressAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechSecurityAddressAddress.setStatus("current")
_QtechSecurityAddressPort_Type = IfIndex
_QtechSecurityAddressPort_Object = MibTableColumn
qtechSecurityAddressPort = _QtechSecurityAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 1, 1, 3),
    _QtechSecurityAddressPort_Type()
)
qtechSecurityAddressPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechSecurityAddressPort.setStatus("current")
_QtechSecurityAddressIpAddr_Type = IpAddress
_QtechSecurityAddressIpAddr_Object = MibTableColumn
qtechSecurityAddressIpAddr = _QtechSecurityAddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 1, 1, 4),
    _QtechSecurityAddressIpAddr_Type()
)
qtechSecurityAddressIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechSecurityAddressIpAddr.setStatus("current")
_QtechSecurityAddressIfBindIp_Type = TruthValue
_QtechSecurityAddressIfBindIp_Object = MibTableColumn
qtechSecurityAddressIfBindIp = _QtechSecurityAddressIfBindIp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 1, 1, 5),
    _QtechSecurityAddressIfBindIp_Type()
)
qtechSecurityAddressIfBindIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecurityAddressIfBindIp.setStatus("current")
_QtechSecurityAddressRemainAge_Type = Integer32
_QtechSecurityAddressRemainAge_Object = MibTableColumn
qtechSecurityAddressRemainAge = _QtechSecurityAddressRemainAge_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 1, 1, 6),
    _QtechSecurityAddressRemainAge_Type()
)
qtechSecurityAddressRemainAge.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSecurityAddressRemainAge.setStatus("current")


class _QtechSecurityAddressType_Type(Integer32):
    """Custom type qtechSecurityAddressType based on Integer32"""
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


_QtechSecurityAddressType_Type.__name__ = "Integer32"
_QtechSecurityAddressType_Object = MibTableColumn
qtechSecurityAddressType = _QtechSecurityAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 1, 1, 7),
    _QtechSecurityAddressType_Type()
)
qtechSecurityAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechSecurityAddressType.setStatus("current")
_QtechSecurityAddressStatus_Type = RowStatus
_QtechSecurityAddressStatus_Object = MibTableColumn
qtechSecurityAddressStatus = _QtechSecurityAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 1, 1, 8),
    _QtechSecurityAddressStatus_Type()
)
qtechSecurityAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechSecurityAddressStatus.setStatus("current")
_QtechBindAddressTable_Object = MibTable
qtechBindAddressTable = _QtechBindAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qtechBindAddressTable.setStatus("current")
_QtechBindAddressEntry_Object = MibTableRow
qtechBindAddressEntry = _QtechBindAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 2, 1)
)
qtechBindAddressEntry.setIndexNames(
    (0, "QTECH-SECURITY-MIB", "qtechBindAddressIpAddr"),
)
if mibBuilder.loadTexts:
    qtechBindAddressEntry.setStatus("current")
_QtechBindAddressIpAddr_Type = IpAddress
_QtechBindAddressIpAddr_Object = MibTableColumn
qtechBindAddressIpAddr = _QtechBindAddressIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 2, 1, 1),
    _QtechBindAddressIpAddr_Type()
)
qtechBindAddressIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    qtechBindAddressIpAddr.setStatus("current")
_QtechBindMacAddress_Type = MacAddress
_QtechBindMacAddress_Object = MibTableColumn
qtechBindMacAddress = _QtechBindMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 2, 1, 2),
    _QtechBindMacAddress_Type()
)
qtechBindMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBindMacAddress.setStatus("current")
_QtechBindAddressStatus_Type = ConfigStatus
_QtechBindAddressStatus_Object = MibTableColumn
qtechBindAddressStatus = _QtechBindAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 2, 2, 1, 3),
    _QtechBindAddressStatus_Type()
)
qtechBindAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechBindAddressStatus.setStatus("current")
_QtechPortSecrrityObjects_ObjectIdentity = ObjectIdentity
qtechPortSecrrityObjects = _QtechPortSecrrityObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3)
)
_QtechPortSecurityTable_Object = MibTable
qtechPortSecurityTable = _QtechPortSecurityTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechPortSecurityTable.setStatus("current")
_QtechPortSecurityEntry_Object = MibTableRow
qtechPortSecurityEntry = _QtechPortSecurityEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1, 1)
)
qtechPortSecurityEntry.setIndexNames(
    (0, "QTECH-SECURITY-MIB", "qtechPortSecurityPortIndex"),
)
if mibBuilder.loadTexts:
    qtechPortSecurityEntry.setStatus("current")
_QtechPortSecurityPortIndex_Type = IfIndex
_QtechPortSecurityPortIndex_Object = MibTableColumn
qtechPortSecurityPortIndex = _QtechPortSecurityPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1, 1, 1),
    _QtechPortSecurityPortIndex_Type()
)
qtechPortSecurityPortIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPortSecurityPortIndex.setStatus("current")


class _QtechPortSecurityStatus_Type(EnabledStatus):
    """Custom type qtechPortSecurityStatus based on EnabledStatus"""
    defaultValue = 2


_QtechPortSecurityStatus_Type.__name__ = "EnabledStatus"
_QtechPortSecurityStatus_Object = MibTableColumn
qtechPortSecurityStatus = _QtechPortSecurityStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1, 1, 2),
    _QtechPortSecurityStatus_Type()
)
qtechPortSecurityStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPortSecurityStatus.setStatus("current")


class _QtechPortSecurViolationType_Type(Integer32):
    """Custom type qtechPortSecurViolationType based on Integer32"""
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


_QtechPortSecurViolationType_Type.__name__ = "Integer32"
_QtechPortSecurViolationType_Object = MibTableColumn
qtechPortSecurViolationType = _QtechPortSecurViolationType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1, 1, 3),
    _QtechPortSecurViolationType_Type()
)
qtechPortSecurViolationType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPortSecurViolationType.setStatus("current")
_QtechPortSecurityAddrNum_Type = Integer32
_QtechPortSecurityAddrNum_Object = MibTableColumn
qtechPortSecurityAddrNum = _QtechPortSecurityAddrNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1, 1, 4),
    _QtechPortSecurityAddrNum_Type()
)
qtechPortSecurityAddrNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPortSecurityAddrNum.setStatus("current")
_QtechPortSecurityAddrAge_Type = Integer32
_QtechPortSecurityAddrAge_Object = MibTableColumn
qtechPortSecurityAddrAge = _QtechPortSecurityAddrAge_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1, 1, 5),
    _QtechPortSecurityAddrAge_Type()
)
qtechPortSecurityAddrAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPortSecurityAddrAge.setStatus("current")
_QtechPortStaticSecurAddrIfAge_Type = EnabledStatus
_QtechPortStaticSecurAddrIfAge_Object = MibTableColumn
qtechPortStaticSecurAddrIfAge = _QtechPortStaticSecurAddrIfAge_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1, 1, 6),
    _QtechPortStaticSecurAddrIfAge_Type()
)
qtechPortStaticSecurAddrIfAge.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechPortStaticSecurAddrIfAge.setStatus("current")
_QtechPortSecurityAddressCurrentNum_Type = Integer32
_QtechPortSecurityAddressCurrentNum_Object = MibTableColumn
qtechPortSecurityAddressCurrentNum = _QtechPortSecurityAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1, 1, 7),
    _QtechPortSecurityAddressCurrentNum_Type()
)
qtechPortSecurityAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPortSecurityAddressCurrentNum.setStatus("current")
_QtechPortStaticSecurAddrCurrentNum_Type = Integer32
_QtechPortStaticSecurAddrCurrentNum_Object = MibTableColumn
qtechPortStaticSecurAddrCurrentNum = _QtechPortStaticSecurAddrCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1, 1, 8),
    _QtechPortStaticSecurAddrCurrentNum_Type()
)
qtechPortStaticSecurAddrCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPortStaticSecurAddrCurrentNum.setStatus("current")


class _QtechPortSecurityIpDistrMode_Type(Integer32):
    """Custom type qtechPortSecurityIpDistrMode based on Integer32"""
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


_QtechPortSecurityIpDistrMode_Type.__name__ = "Integer32"
_QtechPortSecurityIpDistrMode_Object = MibTableColumn
qtechPortSecurityIpDistrMode = _QtechPortSecurityIpDistrMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 1, 3, 1, 1, 9),
    _QtechPortSecurityIpDistrMode_Type()
)
qtechPortSecurityIpDistrMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechPortSecurityIpDistrMode.setStatus("current")
_QtechSecurityTraps_ObjectIdentity = ObjectIdentity
qtechSecurityTraps = _QtechSecurityTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 2)
)
_QtechSecurityMIBConformance_ObjectIdentity = ObjectIdentity
qtechSecurityMIBConformance = _QtechSecurityMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 3)
)
_QtechSecurityMIBCompliances_ObjectIdentity = ObjectIdentity
qtechSecurityMIBCompliances = _QtechSecurityMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 3, 1)
)
_QtechSecurityMIBGroups_ObjectIdentity = ObjectIdentity
qtechSecurityMIBGroups = _QtechSecurityMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 3, 2)
)

# Managed Objects groups

qtechUserManageMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 3, 2, 1)
)
qtechUserManageMIBGroup.setObjects(
      *(("QTECH-SECURITY-MIB", "qtechEnableSnmpAgent"),
        ("QTECH-SECURITY-MIB", "qtechEnableWeb"),
        ("QTECH-SECURITY-MIB", "qtechEnableTelnet"))
)
if mibBuilder.loadTexts:
    qtechUserManageMIBGroup.setStatus("current")

qtechSecurityAddressMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 3, 2, 2)
)
qtechSecurityAddressMIBGroup.setObjects(
      *(("QTECH-SECURITY-MIB", "qtechSecurityAddressIfBindIp"),
        ("QTECH-SECURITY-MIB", "qtechSecurityAddressRemainAge"),
        ("QTECH-SECURITY-MIB", "qtechSecurityAddressType"),
        ("QTECH-SECURITY-MIB", "qtechSecurityAddressStatus"),
        ("QTECH-SECURITY-MIB", "qtechBindMacAddress"),
        ("QTECH-SECURITY-MIB", "qtechBindAddressStatus"))
)
if mibBuilder.loadTexts:
    qtechSecurityAddressMIBGroup.setStatus("current")

qtechPortSecurityMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 3, 2, 3)
)
qtechPortSecurityMIBGroup.setObjects(
      *(("QTECH-SECURITY-MIB", "qtechPortSecurityPortIndex"),
        ("QTECH-SECURITY-MIB", "qtechPortSecurityStatus"),
        ("QTECH-SECURITY-MIB", "qtechPortSecurViolationType"),
        ("QTECH-SECURITY-MIB", "qtechPortSecurityAddrNum"),
        ("QTECH-SECURITY-MIB", "qtechPortSecurityAddrAge"),
        ("QTECH-SECURITY-MIB", "qtechPortStaticSecurAddrIfAge"),
        ("QTECH-SECURITY-MIB", "qtechPortSecurityAddressCurrentNum"),
        ("QTECH-SECURITY-MIB", "qtechPortStaticSecurAddrCurrentNum"),
        ("QTECH-SECURITY-MIB", "qtechPortSecurityIpDistrMode"))
)
if mibBuilder.loadTexts:
    qtechPortSecurityMIBGroup.setStatus("current")


# Notification objects

portSecurityViolate = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 2, 1)
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

qtechSecurityMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 6, 3, 1, 1)
)
qtechSecurityMIBCompliance.setObjects(
      *(("QTECH-SECURITY-MIB", "qtechUserManageMIBGroup"),
        ("QTECH-SECURITY-MIB", "qtechSecurityAddressMIBGroup"),
        ("QTECH-SECURITY-MIB", "qtechPortSecurityMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechSecurityMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-SECURITY-MIB",
    **{"qtechSecurityMIB": qtechSecurityMIB,
       "qtechSecurityMIBObjects": qtechSecurityMIBObjects,
       "qtechUserManagementObjects": qtechUserManagementObjects,
       "qtechEnableSnmpAgent": qtechEnableSnmpAgent,
       "qtechEnableWeb": qtechEnableWeb,
       "qtechEnableTelnet": qtechEnableTelnet,
       "qtechTelnetHostIpTable": qtechTelnetHostIpTable,
       "qtechTelnetHostIpEntry": qtechTelnetHostIpEntry,
       "qtechTelnetHostIpAddress": qtechTelnetHostIpAddress,
       "qtechTelnetHostIpEnable": qtechTelnetHostIpEnable,
       "qtechWebHostIpTable": qtechWebHostIpTable,
       "qtechWebHostIpEntry": qtechWebHostIpEntry,
       "qtechWebHostIpAddress": qtechWebHostIpAddress,
       "qtechWebHostIpEnable": qtechWebHostIpEnable,
       "qtechSecurityAddressObjects": qtechSecurityAddressObjects,
       "qtechSecurityAddressTable": qtechSecurityAddressTable,
       "qtechSecurityAddressEntry": qtechSecurityAddressEntry,
       "qtechSecurityAddressFdbId": qtechSecurityAddressFdbId,
       "qtechSecurityAddressAddress": qtechSecurityAddressAddress,
       "qtechSecurityAddressPort": qtechSecurityAddressPort,
       "qtechSecurityAddressIpAddr": qtechSecurityAddressIpAddr,
       "qtechSecurityAddressIfBindIp": qtechSecurityAddressIfBindIp,
       "qtechSecurityAddressRemainAge": qtechSecurityAddressRemainAge,
       "qtechSecurityAddressType": qtechSecurityAddressType,
       "qtechSecurityAddressStatus": qtechSecurityAddressStatus,
       "qtechBindAddressTable": qtechBindAddressTable,
       "qtechBindAddressEntry": qtechBindAddressEntry,
       "qtechBindAddressIpAddr": qtechBindAddressIpAddr,
       "qtechBindMacAddress": qtechBindMacAddress,
       "qtechBindAddressStatus": qtechBindAddressStatus,
       "qtechPortSecrrityObjects": qtechPortSecrrityObjects,
       "qtechPortSecurityTable": qtechPortSecurityTable,
       "qtechPortSecurityEntry": qtechPortSecurityEntry,
       "qtechPortSecurityPortIndex": qtechPortSecurityPortIndex,
       "qtechPortSecurityStatus": qtechPortSecurityStatus,
       "qtechPortSecurViolationType": qtechPortSecurViolationType,
       "qtechPortSecurityAddrNum": qtechPortSecurityAddrNum,
       "qtechPortSecurityAddrAge": qtechPortSecurityAddrAge,
       "qtechPortStaticSecurAddrIfAge": qtechPortStaticSecurAddrIfAge,
       "qtechPortSecurityAddressCurrentNum": qtechPortSecurityAddressCurrentNum,
       "qtechPortStaticSecurAddrCurrentNum": qtechPortStaticSecurAddrCurrentNum,
       "qtechPortSecurityIpDistrMode": qtechPortSecurityIpDistrMode,
       "qtechSecurityTraps": qtechSecurityTraps,
       "portSecurityViolate": portSecurityViolate,
       "qtechSecurityMIBConformance": qtechSecurityMIBConformance,
       "qtechSecurityMIBCompliances": qtechSecurityMIBCompliances,
       "qtechSecurityMIBCompliance": qtechSecurityMIBCompliance,
       "qtechSecurityMIBGroups": qtechSecurityMIBGroups,
       "qtechUserManageMIBGroup": qtechUserManageMIBGroup,
       "qtechSecurityAddressMIBGroup": qtechSecurityAddressMIBGroup,
       "qtechPortSecurityMIBGroup": qtechPortSecurityMIBGroup}
)
