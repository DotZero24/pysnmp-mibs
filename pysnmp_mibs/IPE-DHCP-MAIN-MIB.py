# SNMP MIB module (IPE-DHCP-MAIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-DHCP-MAIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:50 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 Opaque,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



class EnableDisableValue(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("disable", 1),
          ("enable", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_RadioEquipment_ObjectIdentity = ObjectIdentity
radioEquipment = _RadioEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69)
)
_System5_ObjectIdentity = ObjectIdentity
system5 = _System5_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5)
)
_IpeConfigurationGroup_ObjectIdentity = ObjectIdentity
ipeConfigurationGroup = _IpeConfigurationGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3)
)
_IpeCfgDhcpGroup_ObjectIdentity = ObjectIdentity
ipeCfgDhcpGroup = _IpeCfgDhcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13)
)
_IpeCfgDhcpMainServerTable_Object = MibTable
ipeCfgDhcpMainServerTable = _IpeCfgDhcpMainServerTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2)
)
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerTable.setStatus("current")
_IpeCfgDhcpMainServerEntry_Object = MibTableRow
ipeCfgDhcpMainServerEntry = _IpeCfgDhcpMainServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1)
)
ipeCfgDhcpMainServerEntry.setIndexNames(
    (0, "IPE-DHCP-MAIN-MIB", "ipeCfgDhcpMainServerIndex"),
)
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerEntry.setStatus("current")


class _IpeCfgDhcpMainServerIndex_Type(Integer32):
    """Custom type ipeCfgDhcpMainServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_IpeCfgDhcpMainServerIndex_Type.__name__ = "Integer32"
_IpeCfgDhcpMainServerIndex_Object = MibTableColumn
ipeCfgDhcpMainServerIndex = _IpeCfgDhcpMainServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 1),
    _IpeCfgDhcpMainServerIndex_Type()
)
ipeCfgDhcpMainServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerIndex.setStatus("current")
_IpeCfgDhcpMainServerNEAddress_Type = IpAddress
_IpeCfgDhcpMainServerNEAddress_Object = MibTableColumn
ipeCfgDhcpMainServerNEAddress = _IpeCfgDhcpMainServerNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 2),
    _IpeCfgDhcpMainServerNEAddress_Type()
)
ipeCfgDhcpMainServerNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerNEAddress.setStatus("current")


class _IpeCfgDhcpMainServerEnable_Type(EnableDisableValue):
    """Custom type ipeCfgDhcpMainServerEnable based on EnableDisableValue"""
    defaultValue = 1


_IpeCfgDhcpMainServerEnable_Type.__name__ = "EnableDisableValue"
_IpeCfgDhcpMainServerEnable_Object = MibTableColumn
ipeCfgDhcpMainServerEnable = _IpeCfgDhcpMainServerEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 3),
    _IpeCfgDhcpMainServerEnable_Type()
)
ipeCfgDhcpMainServerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerEnable.setStatus("current")


class _IpeCfgDhcpMainServerMode_Type(Integer32):
    """Custom type ipeCfgDhcpMainServerMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("server", 1),
          ("relay", 2))
    )


_IpeCfgDhcpMainServerMode_Type.__name__ = "Integer32"
_IpeCfgDhcpMainServerMode_Object = MibTableColumn
ipeCfgDhcpMainServerMode = _IpeCfgDhcpMainServerMode_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 4),
    _IpeCfgDhcpMainServerMode_Type()
)
ipeCfgDhcpMainServerMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerMode.setStatus("current")
_IpeCfgDhcpMainServerInterface_Type = InterfaceIndex
_IpeCfgDhcpMainServerInterface_Object = MibTableColumn
ipeCfgDhcpMainServerInterface = _IpeCfgDhcpMainServerInterface_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 5),
    _IpeCfgDhcpMainServerInterface_Type()
)
ipeCfgDhcpMainServerInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerInterface.setStatus("current")
_IpeCfgDhcpMainServerIpAddr_Type = IpAddress
_IpeCfgDhcpMainServerIpAddr_Object = MibTableColumn
ipeCfgDhcpMainServerIpAddr = _IpeCfgDhcpMainServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 6),
    _IpeCfgDhcpMainServerIpAddr_Type()
)
ipeCfgDhcpMainServerIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerIpAddr.setStatus("current")


class _IpeCfgDhcpMainServerLeaseTime_Type(Integer32):
    """Custom type ipeCfgDhcpMainServerLeaseTime based on Integer32"""
    defaultValue = 86400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(60, 259200),
    )


_IpeCfgDhcpMainServerLeaseTime_Type.__name__ = "Integer32"
_IpeCfgDhcpMainServerLeaseTime_Object = MibTableColumn
ipeCfgDhcpMainServerLeaseTime = _IpeCfgDhcpMainServerLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 7),
    _IpeCfgDhcpMainServerLeaseTime_Type()
)
ipeCfgDhcpMainServerLeaseTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerLeaseTime.setStatus("current")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerLeaseTime.setUnits("seconds")


class _IpeCfgDhcpMainServerLeaseAddrRangeBegin_Type(IpAddress):
    """Custom type ipeCfgDhcpMainServerLeaseAddrRangeBegin based on IpAddress"""
    defaultHexValue = "00000000"


_IpeCfgDhcpMainServerLeaseAddrRangeBegin_Type.__name__ = "IpAddress"
_IpeCfgDhcpMainServerLeaseAddrRangeBegin_Object = MibTableColumn
ipeCfgDhcpMainServerLeaseAddrRangeBegin = _IpeCfgDhcpMainServerLeaseAddrRangeBegin_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 8),
    _IpeCfgDhcpMainServerLeaseAddrRangeBegin_Type()
)
ipeCfgDhcpMainServerLeaseAddrRangeBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerLeaseAddrRangeBegin.setStatus("current")


class _IpeCfgDhcpMainServerLeaseAddrRangeEnd_Type(IpAddress):
    """Custom type ipeCfgDhcpMainServerLeaseAddrRangeEnd based on IpAddress"""
    defaultHexValue = "00000000"


_IpeCfgDhcpMainServerLeaseAddrRangeEnd_Type.__name__ = "IpAddress"
_IpeCfgDhcpMainServerLeaseAddrRangeEnd_Object = MibTableColumn
ipeCfgDhcpMainServerLeaseAddrRangeEnd = _IpeCfgDhcpMainServerLeaseAddrRangeEnd_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 9),
    _IpeCfgDhcpMainServerLeaseAddrRangeEnd_Type()
)
ipeCfgDhcpMainServerLeaseAddrRangeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerLeaseAddrRangeEnd.setStatus("current")


class _IpeCfgDhcpMainServerLeaseAddrExcludeBegin_Type(IpAddress):
    """Custom type ipeCfgDhcpMainServerLeaseAddrExcludeBegin based on IpAddress"""
    defaultHexValue = "00000000"


_IpeCfgDhcpMainServerLeaseAddrExcludeBegin_Type.__name__ = "IpAddress"
_IpeCfgDhcpMainServerLeaseAddrExcludeBegin_Object = MibTableColumn
ipeCfgDhcpMainServerLeaseAddrExcludeBegin = _IpeCfgDhcpMainServerLeaseAddrExcludeBegin_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 10),
    _IpeCfgDhcpMainServerLeaseAddrExcludeBegin_Type()
)
ipeCfgDhcpMainServerLeaseAddrExcludeBegin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerLeaseAddrExcludeBegin.setStatus("current")


class _IpeCfgDhcpMainServerLeaseAddrExcludeEnd_Type(IpAddress):
    """Custom type ipeCfgDhcpMainServerLeaseAddrExcludeEnd based on IpAddress"""
    defaultHexValue = "00000000"


_IpeCfgDhcpMainServerLeaseAddrExcludeEnd_Type.__name__ = "IpAddress"
_IpeCfgDhcpMainServerLeaseAddrExcludeEnd_Object = MibTableColumn
ipeCfgDhcpMainServerLeaseAddrExcludeEnd = _IpeCfgDhcpMainServerLeaseAddrExcludeEnd_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 11),
    _IpeCfgDhcpMainServerLeaseAddrExcludeEnd_Type()
)
ipeCfgDhcpMainServerLeaseAddrExcludeEnd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerLeaseAddrExcludeEnd.setStatus("current")


class _IpeCfgDhcpMainServerOptGatewayAddrEnable_Type(Integer32):
    """Custom type ipeCfgDhcpMainServerOptGatewayAddrEnable based on Integer32"""
    defaultValue = 1

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
        *(("invalid", 0),
          ("enabledInterface", 1),
          ("enabledSpecify", 2),
          ("disabled", 3))
    )


_IpeCfgDhcpMainServerOptGatewayAddrEnable_Type.__name__ = "Integer32"
_IpeCfgDhcpMainServerOptGatewayAddrEnable_Object = MibTableColumn
ipeCfgDhcpMainServerOptGatewayAddrEnable = _IpeCfgDhcpMainServerOptGatewayAddrEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 12),
    _IpeCfgDhcpMainServerOptGatewayAddrEnable_Type()
)
ipeCfgDhcpMainServerOptGatewayAddrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerOptGatewayAddrEnable.setStatus("current")


class _IpeCfgDhcpMainServerOptGatewayAddr_Type(IpAddress):
    """Custom type ipeCfgDhcpMainServerOptGatewayAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpeCfgDhcpMainServerOptGatewayAddr_Type.__name__ = "IpAddress"
_IpeCfgDhcpMainServerOptGatewayAddr_Object = MibTableColumn
ipeCfgDhcpMainServerOptGatewayAddr = _IpeCfgDhcpMainServerOptGatewayAddr_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 13),
    _IpeCfgDhcpMainServerOptGatewayAddr_Type()
)
ipeCfgDhcpMainServerOptGatewayAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerOptGatewayAddr.setStatus("current")


class _IpeCfgDhcpMainServerOptDnsServerPrimary_Type(IpAddress):
    """Custom type ipeCfgDhcpMainServerOptDnsServerPrimary based on IpAddress"""
    defaultHexValue = "00000000"


_IpeCfgDhcpMainServerOptDnsServerPrimary_Type.__name__ = "IpAddress"
_IpeCfgDhcpMainServerOptDnsServerPrimary_Object = MibTableColumn
ipeCfgDhcpMainServerOptDnsServerPrimary = _IpeCfgDhcpMainServerOptDnsServerPrimary_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 14),
    _IpeCfgDhcpMainServerOptDnsServerPrimary_Type()
)
ipeCfgDhcpMainServerOptDnsServerPrimary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerOptDnsServerPrimary.setStatus("current")


class _IpeCfgDhcpMainServerOptDnsServerSecondary_Type(IpAddress):
    """Custom type ipeCfgDhcpMainServerOptDnsServerSecondary based on IpAddress"""
    defaultHexValue = "00000000"


_IpeCfgDhcpMainServerOptDnsServerSecondary_Type.__name__ = "IpAddress"
_IpeCfgDhcpMainServerOptDnsServerSecondary_Object = MibTableColumn
ipeCfgDhcpMainServerOptDnsServerSecondary = _IpeCfgDhcpMainServerOptDnsServerSecondary_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 15),
    _IpeCfgDhcpMainServerOptDnsServerSecondary_Type()
)
ipeCfgDhcpMainServerOptDnsServerSecondary.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerOptDnsServerSecondary.setStatus("current")


class _IpeCfgDhcpMainServerOptSpecifyEnable_Type(EnableDisableValue):
    """Custom type ipeCfgDhcpMainServerOptSpecifyEnable based on EnableDisableValue"""
    defaultValue = 1


_IpeCfgDhcpMainServerOptSpecifyEnable_Type.__name__ = "EnableDisableValue"
_IpeCfgDhcpMainServerOptSpecifyEnable_Object = MibTableColumn
ipeCfgDhcpMainServerOptSpecifyEnable = _IpeCfgDhcpMainServerOptSpecifyEnable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 16),
    _IpeCfgDhcpMainServerOptSpecifyEnable_Type()
)
ipeCfgDhcpMainServerOptSpecifyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerOptSpecifyEnable.setStatus("current")


class _IpeCfgDhcpMainServerOptSpecifyId_Type(Integer32):
    """Custom type ipeCfgDhcpMainServerOptSpecifyId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_IpeCfgDhcpMainServerOptSpecifyId_Type.__name__ = "Integer32"
_IpeCfgDhcpMainServerOptSpecifyId_Object = MibTableColumn
ipeCfgDhcpMainServerOptSpecifyId = _IpeCfgDhcpMainServerOptSpecifyId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 17),
    _IpeCfgDhcpMainServerOptSpecifyId_Type()
)
ipeCfgDhcpMainServerOptSpecifyId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerOptSpecifyId.setStatus("current")


class _IpeCfgDhcpMainServerOptSpecifyType_Type(Integer32):
    """Custom type ipeCfgDhcpMainServerOptSpecifyType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("ipv4", 1),
          ("ipv6", 2),
          ("displayString", 3),
          ("octetString", 4))
    )


_IpeCfgDhcpMainServerOptSpecifyType_Type.__name__ = "Integer32"
_IpeCfgDhcpMainServerOptSpecifyType_Object = MibTableColumn
ipeCfgDhcpMainServerOptSpecifyType = _IpeCfgDhcpMainServerOptSpecifyType_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 18),
    _IpeCfgDhcpMainServerOptSpecifyType_Type()
)
ipeCfgDhcpMainServerOptSpecifyType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerOptSpecifyType.setStatus("current")


class _IpeCfgDhcpMainServerOptSpecifyValue_Type(OctetString):
    """Custom type ipeCfgDhcpMainServerOptSpecifyValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_IpeCfgDhcpMainServerOptSpecifyValue_Type.__name__ = "OctetString"
_IpeCfgDhcpMainServerOptSpecifyValue_Object = MibTableColumn
ipeCfgDhcpMainServerOptSpecifyValue = _IpeCfgDhcpMainServerOptSpecifyValue_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 19),
    _IpeCfgDhcpMainServerOptSpecifyValue_Type()
)
ipeCfgDhcpMainServerOptSpecifyValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerOptSpecifyValue.setStatus("current")


class _IpeCfgDhcpMainServerSecurityLevel_Type(Integer32):
    """Custom type ipeCfgDhcpMainServerSecurityLevel based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("any", 1),
          ("onlyRegistered", 2))
    )


_IpeCfgDhcpMainServerSecurityLevel_Type.__name__ = "Integer32"
_IpeCfgDhcpMainServerSecurityLevel_Object = MibTableColumn
ipeCfgDhcpMainServerSecurityLevel = _IpeCfgDhcpMainServerSecurityLevel_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 20),
    _IpeCfgDhcpMainServerSecurityLevel_Type()
)
ipeCfgDhcpMainServerSecurityLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerSecurityLevel.setStatus("current")


class _IpeCfgDhcpMainServerRegisteredMacId_Type(Integer32):
    """Custom type ipeCfgDhcpMainServerRegisteredMacId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3),
    )


_IpeCfgDhcpMainServerRegisteredMacId_Type.__name__ = "Integer32"
_IpeCfgDhcpMainServerRegisteredMacId_Object = MibTableColumn
ipeCfgDhcpMainServerRegisteredMacId = _IpeCfgDhcpMainServerRegisteredMacId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 2, 1, 21),
    _IpeCfgDhcpMainServerRegisteredMacId_Type()
)
ipeCfgDhcpMainServerRegisteredMacId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainServerRegisteredMacId.setStatus("current")
_IpeCfgDhcpMainRegisteredMacTable_Object = MibTable
ipeCfgDhcpMainRegisteredMacTable = _IpeCfgDhcpMainRegisteredMacTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 3)
)
if mibBuilder.loadTexts:
    ipeCfgDhcpMainRegisteredMacTable.setStatus("current")
_IpeCfgDhcpMainRegisteredMacEntry_Object = MibTableRow
ipeCfgDhcpMainRegisteredMacEntry = _IpeCfgDhcpMainRegisteredMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 3, 1)
)
ipeCfgDhcpMainRegisteredMacEntry.setIndexNames(
    (0, "IPE-DHCP-MAIN-MIB", "ipeCfgDhcpMainRegisteredMacId"),
    (0, "IPE-DHCP-MAIN-MIB", "ipeCfgDhcpMainRegisteredMacNo"),
)
if mibBuilder.loadTexts:
    ipeCfgDhcpMainRegisteredMacEntry.setStatus("current")


class _IpeCfgDhcpMainRegisteredMacId_Type(Integer32):
    """Custom type ipeCfgDhcpMainRegisteredMacId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IpeCfgDhcpMainRegisteredMacId_Type.__name__ = "Integer32"
_IpeCfgDhcpMainRegisteredMacId_Object = MibTableColumn
ipeCfgDhcpMainRegisteredMacId = _IpeCfgDhcpMainRegisteredMacId_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 3, 1, 1),
    _IpeCfgDhcpMainRegisteredMacId_Type()
)
ipeCfgDhcpMainRegisteredMacId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainRegisteredMacId.setStatus("current")


class _IpeCfgDhcpMainRegisteredMacNo_Type(Integer32):
    """Custom type ipeCfgDhcpMainRegisteredMacNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_IpeCfgDhcpMainRegisteredMacNo_Type.__name__ = "Integer32"
_IpeCfgDhcpMainRegisteredMacNo_Object = MibTableColumn
ipeCfgDhcpMainRegisteredMacNo = _IpeCfgDhcpMainRegisteredMacNo_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 3, 1, 2),
    _IpeCfgDhcpMainRegisteredMacNo_Type()
)
ipeCfgDhcpMainRegisteredMacNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainRegisteredMacNo.setStatus("current")
_IpeCfgDhcpMainRegisteredMacNEAddress_Type = IpAddress
_IpeCfgDhcpMainRegisteredMacNEAddress_Object = MibTableColumn
ipeCfgDhcpMainRegisteredMacNEAddress = _IpeCfgDhcpMainRegisteredMacNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 3, 1, 3),
    _IpeCfgDhcpMainRegisteredMacNEAddress_Type()
)
ipeCfgDhcpMainRegisteredMacNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainRegisteredMacNEAddress.setStatus("current")
_IpeCfgDhcpMainRegisteredMacAddr_Type = MacAddress
_IpeCfgDhcpMainRegisteredMacAddr_Object = MibTableColumn
ipeCfgDhcpMainRegisteredMacAddr = _IpeCfgDhcpMainRegisteredMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 3, 1, 4),
    _IpeCfgDhcpMainRegisteredMacAddr_Type()
)
ipeCfgDhcpMainRegisteredMacAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainRegisteredMacAddr.setStatus("current")


class _IpeCfgDhcpMainRegisteredMacIpAddr_Type(IpAddress):
    """Custom type ipeCfgDhcpMainRegisteredMacIpAddr based on IpAddress"""
    defaultHexValue = "00000000"


_IpeCfgDhcpMainRegisteredMacIpAddr_Type.__name__ = "IpAddress"
_IpeCfgDhcpMainRegisteredMacIpAddr_Object = MibTableColumn
ipeCfgDhcpMainRegisteredMacIpAddr = _IpeCfgDhcpMainRegisteredMacIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 3, 1, 5),
    _IpeCfgDhcpMainRegisteredMacIpAddr_Type()
)
ipeCfgDhcpMainRegisteredMacIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainRegisteredMacIpAddr.setStatus("current")
_IpeCfgDhcpMainRegisteredMacRowStatus_Type = RowStatus
_IpeCfgDhcpMainRegisteredMacRowStatus_Object = MibTableColumn
ipeCfgDhcpMainRegisteredMacRowStatus = _IpeCfgDhcpMainRegisteredMacRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 3, 13, 3, 1, 6),
    _IpeCfgDhcpMainRegisteredMacRowStatus_Type()
)
ipeCfgDhcpMainRegisteredMacRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    ipeCfgDhcpMainRegisteredMacRowStatus.setStatus("current")
_IpeStatusGroup_ObjectIdentity = ObjectIdentity
ipeStatusGroup = _IpeStatusGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6)
)
_IpeStsDhcpGroup_ObjectIdentity = ObjectIdentity
ipeStsDhcpGroup = _IpeStsDhcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 13)
)
_IpeStsDhcpMainLeaseTable_Object = MibTable
ipeStsDhcpMainLeaseTable = _IpeStsDhcpMainLeaseTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 13, 1)
)
if mibBuilder.loadTexts:
    ipeStsDhcpMainLeaseTable.setStatus("current")
_IpeStsDhcpMainLeaseEntry_Object = MibTableRow
ipeStsDhcpMainLeaseEntry = _IpeStsDhcpMainLeaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 13, 1, 1)
)
ipeStsDhcpMainLeaseEntry.setIndexNames(
    (0, "IPE-DHCP-MAIN-MIB", "ipeStsDhcpMainLeaseServerIndex"),
    (0, "IPE-DHCP-MAIN-MIB", "ipeStsDhcpMainLeaseIpAddr"),
)
if mibBuilder.loadTexts:
    ipeStsDhcpMainLeaseEntry.setStatus("current")


class _IpeStsDhcpMainLeaseServerIndex_Type(Integer32):
    """Custom type ipeStsDhcpMainLeaseServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IpeStsDhcpMainLeaseServerIndex_Type.__name__ = "Integer32"
_IpeStsDhcpMainLeaseServerIndex_Object = MibTableColumn
ipeStsDhcpMainLeaseServerIndex = _IpeStsDhcpMainLeaseServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 13, 1, 1, 1),
    _IpeStsDhcpMainLeaseServerIndex_Type()
)
ipeStsDhcpMainLeaseServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsDhcpMainLeaseServerIndex.setStatus("current")
_IpeStsDhcpMainLeaseIpAddr_Type = IpAddress
_IpeStsDhcpMainLeaseIpAddr_Object = MibTableColumn
ipeStsDhcpMainLeaseIpAddr = _IpeStsDhcpMainLeaseIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 13, 1, 1, 2),
    _IpeStsDhcpMainLeaseIpAddr_Type()
)
ipeStsDhcpMainLeaseIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsDhcpMainLeaseIpAddr.setStatus("current")
_IpeStsDhcpMainLeaseNEAddress_Type = IpAddress
_IpeStsDhcpMainLeaseNEAddress_Object = MibTableColumn
ipeStsDhcpMainLeaseNEAddress = _IpeStsDhcpMainLeaseNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 13, 1, 1, 3),
    _IpeStsDhcpMainLeaseNEAddress_Type()
)
ipeStsDhcpMainLeaseNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeStsDhcpMainLeaseNEAddress.setStatus("current")
_IpeStsDhcpMainLeaseMacAddr_Type = MacAddress
_IpeStsDhcpMainLeaseMacAddr_Object = MibTableColumn
ipeStsDhcpMainLeaseMacAddr = _IpeStsDhcpMainLeaseMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 13, 1, 1, 4),
    _IpeStsDhcpMainLeaseMacAddr_Type()
)
ipeStsDhcpMainLeaseMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsDhcpMainLeaseMacAddr.setStatus("current")
_IpeStsDhcpMainLeaseDateAndTime_Type = DateAndTime
_IpeStsDhcpMainLeaseDateAndTime_Object = MibTableColumn
ipeStsDhcpMainLeaseDateAndTime = _IpeStsDhcpMainLeaseDateAndTime_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 6, 13, 1, 1, 5),
    _IpeStsDhcpMainLeaseDateAndTime_Type()
)
ipeStsDhcpMainLeaseDateAndTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipeStsDhcpMainLeaseDateAndTime.setStatus("current")
_IpeCommandGroup_ObjectIdentity = ObjectIdentity
ipeCommandGroup = _IpeCommandGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 8)
)
_IpeCmdDhcpGroup_ObjectIdentity = ObjectIdentity
ipeCmdDhcpGroup = _IpeCmdDhcpGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 8, 13)
)
_IpeCmdDhcpMainTable_Object = MibTable
ipeCmdDhcpMainTable = _IpeCmdDhcpMainTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 8, 13, 1)
)
if mibBuilder.loadTexts:
    ipeCmdDhcpMainTable.setStatus("current")
_IpeCmdDhcpMainEntry_Object = MibTableRow
ipeCmdDhcpMainEntry = _IpeCmdDhcpMainEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 8, 13, 1, 1)
)
ipeCmdDhcpMainEntry.setIndexNames(
    (0, "IPE-DHCP-MAIN-MIB", "ipeCmdDhcpMainIndex"),
    (0, "IPE-DHCP-MAIN-MIB", "ipeCmdDhcpMainLeaseIpAddr"),
)
if mibBuilder.loadTexts:
    ipeCmdDhcpMainEntry.setStatus("current")


class _IpeCmdDhcpMainIndex_Type(Integer32):
    """Custom type ipeCmdDhcpMainIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_IpeCmdDhcpMainIndex_Type.__name__ = "Integer32"
_IpeCmdDhcpMainIndex_Object = MibTableColumn
ipeCmdDhcpMainIndex = _IpeCmdDhcpMainIndex_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 8, 13, 1, 1, 1),
    _IpeCmdDhcpMainIndex_Type()
)
ipeCmdDhcpMainIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCmdDhcpMainIndex.setStatus("current")
_IpeCmdDhcpMainLeaseIpAddr_Type = IpAddress
_IpeCmdDhcpMainLeaseIpAddr_Object = MibTableColumn
ipeCmdDhcpMainLeaseIpAddr = _IpeCmdDhcpMainLeaseIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 8, 13, 1, 1, 2),
    _IpeCmdDhcpMainLeaseIpAddr_Type()
)
ipeCmdDhcpMainLeaseIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCmdDhcpMainLeaseIpAddr.setStatus("current")
_IpeCmdDhcpMainNEAddress_Type = IpAddress
_IpeCmdDhcpMainNEAddress_Object = MibTableColumn
ipeCmdDhcpMainNEAddress = _IpeCmdDhcpMainNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 8, 13, 1, 1, 3),
    _IpeCmdDhcpMainNEAddress_Type()
)
ipeCmdDhcpMainNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ipeCmdDhcpMainNEAddress.setStatus("current")


class _IpeCmdDhcpMainManualDelete_Type(Integer32):
    """Custom type ipeCmdDhcpMainManualDelete based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("normal", 1),
          ("manualDelete", 2))
    )


_IpeCmdDhcpMainManualDelete_Type.__name__ = "Integer32"
_IpeCmdDhcpMainManualDelete_Object = MibTableColumn
ipeCmdDhcpMainManualDelete = _IpeCmdDhcpMainManualDelete_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 5, 8, 13, 1, 1, 4),
    _IpeCmdDhcpMainManualDelete_Type()
)
ipeCmdDhcpMainManualDelete.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipeCmdDhcpMainManualDelete.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-DHCP-MAIN-MIB",
    **{"EnableDisableValue": EnableDisableValue,
       "nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "system5": system5,
       "ipeConfigurationGroup": ipeConfigurationGroup,
       "ipeCfgDhcpGroup": ipeCfgDhcpGroup,
       "ipeCfgDhcpMainServerTable": ipeCfgDhcpMainServerTable,
       "ipeCfgDhcpMainServerEntry": ipeCfgDhcpMainServerEntry,
       "ipeCfgDhcpMainServerIndex": ipeCfgDhcpMainServerIndex,
       "ipeCfgDhcpMainServerNEAddress": ipeCfgDhcpMainServerNEAddress,
       "ipeCfgDhcpMainServerEnable": ipeCfgDhcpMainServerEnable,
       "ipeCfgDhcpMainServerMode": ipeCfgDhcpMainServerMode,
       "ipeCfgDhcpMainServerInterface": ipeCfgDhcpMainServerInterface,
       "ipeCfgDhcpMainServerIpAddr": ipeCfgDhcpMainServerIpAddr,
       "ipeCfgDhcpMainServerLeaseTime": ipeCfgDhcpMainServerLeaseTime,
       "ipeCfgDhcpMainServerLeaseAddrRangeBegin": ipeCfgDhcpMainServerLeaseAddrRangeBegin,
       "ipeCfgDhcpMainServerLeaseAddrRangeEnd": ipeCfgDhcpMainServerLeaseAddrRangeEnd,
       "ipeCfgDhcpMainServerLeaseAddrExcludeBegin": ipeCfgDhcpMainServerLeaseAddrExcludeBegin,
       "ipeCfgDhcpMainServerLeaseAddrExcludeEnd": ipeCfgDhcpMainServerLeaseAddrExcludeEnd,
       "ipeCfgDhcpMainServerOptGatewayAddrEnable": ipeCfgDhcpMainServerOptGatewayAddrEnable,
       "ipeCfgDhcpMainServerOptGatewayAddr": ipeCfgDhcpMainServerOptGatewayAddr,
       "ipeCfgDhcpMainServerOptDnsServerPrimary": ipeCfgDhcpMainServerOptDnsServerPrimary,
       "ipeCfgDhcpMainServerOptDnsServerSecondary": ipeCfgDhcpMainServerOptDnsServerSecondary,
       "ipeCfgDhcpMainServerOptSpecifyEnable": ipeCfgDhcpMainServerOptSpecifyEnable,
       "ipeCfgDhcpMainServerOptSpecifyId": ipeCfgDhcpMainServerOptSpecifyId,
       "ipeCfgDhcpMainServerOptSpecifyType": ipeCfgDhcpMainServerOptSpecifyType,
       "ipeCfgDhcpMainServerOptSpecifyValue": ipeCfgDhcpMainServerOptSpecifyValue,
       "ipeCfgDhcpMainServerSecurityLevel": ipeCfgDhcpMainServerSecurityLevel,
       "ipeCfgDhcpMainServerRegisteredMacId": ipeCfgDhcpMainServerRegisteredMacId,
       "ipeCfgDhcpMainRegisteredMacTable": ipeCfgDhcpMainRegisteredMacTable,
       "ipeCfgDhcpMainRegisteredMacEntry": ipeCfgDhcpMainRegisteredMacEntry,
       "ipeCfgDhcpMainRegisteredMacId": ipeCfgDhcpMainRegisteredMacId,
       "ipeCfgDhcpMainRegisteredMacNo": ipeCfgDhcpMainRegisteredMacNo,
       "ipeCfgDhcpMainRegisteredMacNEAddress": ipeCfgDhcpMainRegisteredMacNEAddress,
       "ipeCfgDhcpMainRegisteredMacAddr": ipeCfgDhcpMainRegisteredMacAddr,
       "ipeCfgDhcpMainRegisteredMacIpAddr": ipeCfgDhcpMainRegisteredMacIpAddr,
       "ipeCfgDhcpMainRegisteredMacRowStatus": ipeCfgDhcpMainRegisteredMacRowStatus,
       "ipeStatusGroup": ipeStatusGroup,
       "ipeStsDhcpGroup": ipeStsDhcpGroup,
       "ipeStsDhcpMainLeaseTable": ipeStsDhcpMainLeaseTable,
       "ipeStsDhcpMainLeaseEntry": ipeStsDhcpMainLeaseEntry,
       "ipeStsDhcpMainLeaseServerIndex": ipeStsDhcpMainLeaseServerIndex,
       "ipeStsDhcpMainLeaseIpAddr": ipeStsDhcpMainLeaseIpAddr,
       "ipeStsDhcpMainLeaseNEAddress": ipeStsDhcpMainLeaseNEAddress,
       "ipeStsDhcpMainLeaseMacAddr": ipeStsDhcpMainLeaseMacAddr,
       "ipeStsDhcpMainLeaseDateAndTime": ipeStsDhcpMainLeaseDateAndTime,
       "ipeCommandGroup": ipeCommandGroup,
       "ipeCmdDhcpGroup": ipeCmdDhcpGroup,
       "ipeCmdDhcpMainTable": ipeCmdDhcpMainTable,
       "ipeCmdDhcpMainEntry": ipeCmdDhcpMainEntry,
       "ipeCmdDhcpMainIndex": ipeCmdDhcpMainIndex,
       "ipeCmdDhcpMainLeaseIpAddr": ipeCmdDhcpMainLeaseIpAddr,
       "ipeCmdDhcpMainNEAddress": ipeCmdDhcpMainNEAddress,
       "ipeCmdDhcpMainManualDelete": ipeCmdDhcpMainManualDelete}
)
