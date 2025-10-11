# SNMP MIB module (ALCATEL-ENT1-IP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/alcatel-ent1/ALCATEL-ENT1-IP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:09:05 2025
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

(softentIND1Ip,) = mibBuilder.importSymbols(
    "ALCATEL-ENT1-BASE",
    "softentIND1Ip")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(ipCidrRouteEntry,) = mibBuilder.importSymbols(
    "IP-FORWARD-MIB",
    "ipCidrRouteEntry")

(ipNetToMediaEntry,
 ipNetToMediaIfIndex,
 ipNetToMediaNetAddress) = mibBuilder.importSymbols(
    "IP-MIB",
    "ipNetToMediaEntry",
    "ipNetToMediaIfIndex",
    "ipNetToMediaNetAddress")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

alcatelIND1IPMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1)
)
if mibBuilder.loadTexts:
    alcatelIND1IPMIB.setRevisions(
        ("2016-02-25 00:00",
         "2015-09-09 00:00",
         "2014-10-17 00:00",
         "2012-03-23 00:00",
         "2011-03-07 00:00",
         "2011-01-25 00:00",
         "2010-05-13 00:00",
         "2009-05-19 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlaIpServiceSourceIpAppIndex(TextualConvention, Integer32):
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
              13)
        )
    )
    namedValues = NamedValues(
        *(("all", 1),
          ("dns", 2),
          ("ftp", 3),
          ("ldap", 4),
          ("ntp", 5),
          ("radius", 6),
          ("sflow", 7),
          ("snmp", 8),
          ("ssh", 9),
          ("swlog", 10),
          ("tacacs", 11),
          ("telnet", 12),
          ("tftp", 13))
    )



# MIB Managed Objects in the order of their OIDs

_AlcatelIND1IPMIBNotifications_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBNotifications = _AlcatelIND1IPMIBNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 0)
)
if mibBuilder.loadTexts:
    alcatelIND1IPMIBNotifications.setStatus("current")
_AlcatelIND1IPMIBObjects_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBObjects = _AlcatelIND1IPMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1)
)
_AlaIpConfig_ObjectIdentity = ObjectIdentity
alaIpConfig = _AlaIpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 1)
)


class _AlaIpClearArpCache_Type(Integer32):
    """Custom type alaIpClearArpCache based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaIpClearArpCache_Type.__name__ = "Integer32"
_AlaIpClearArpCache_Object = MibScalar
alaIpClearArpCache = _AlaIpClearArpCache_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 1, 1),
    _AlaIpClearArpCache_Type()
)
alaIpClearArpCache.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpClearArpCache.setStatus("current")


class _AlaIpDirectedBroadcast_Type(Integer32):
    """Custom type alaIpDirectedBroadcast based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AlaIpDirectedBroadcast_Type.__name__ = "Integer32"
_AlaIpDirectedBroadcast_Object = MibScalar
alaIpDirectedBroadcast = _AlaIpDirectedBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 1, 2),
    _AlaIpDirectedBroadcast_Type()
)
alaIpDirectedBroadcast.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpDirectedBroadcast.setStatus("current")


class _AlaIpClearArpFilter_Type(Integer32):
    """Custom type alaIpClearArpFilter based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clear", 1)
    )


_AlaIpClearArpFilter_Type.__name__ = "Integer32"
_AlaIpClearArpFilter_Object = MibScalar
alaIpClearArpFilter = _AlaIpClearArpFilter_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 1, 3),
    _AlaIpClearArpFilter_Type()
)
alaIpClearArpFilter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpClearArpFilter.setStatus("current")


class _AlaIpDistributedArp_Type(Integer32):
    """Custom type alaIpDistributedArp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )


_AlaIpDistributedArp_Type.__name__ = "Integer32"
_AlaIpDistributedArp_Object = MibScalar
alaIpDistributedArp = _AlaIpDistributedArp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 1, 4),
    _AlaIpDistributedArp_Type()
)
alaIpDistributedArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpDistributedArp.setStatus("current")
_AlaIpNetToMediaTable_Object = MibTable
alaIpNetToMediaTable = _AlaIpNetToMediaTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    alaIpNetToMediaTable.setStatus("current")
_AlaIpNetToMediaEntry_Object = MibTableRow
alaIpNetToMediaEntry = _AlaIpNetToMediaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1)
)
alaIpNetToMediaEntry.setIndexNames(
    (0, "IP-MIB", "ipNetToMediaIfIndex"),
    (0, "IP-MIB", "ipNetToMediaNetAddress"),
)
if mibBuilder.loadTexts:
    alaIpNetToMediaEntry.setStatus("current")
_AlaIpNetToMediaPhysAddress_Type = PhysAddress
_AlaIpNetToMediaPhysAddress_Object = MibTableColumn
alaIpNetToMediaPhysAddress = _AlaIpNetToMediaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 1),
    _AlaIpNetToMediaPhysAddress_Type()
)
alaIpNetToMediaPhysAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNetToMediaPhysAddress.setStatus("current")


class _AlaIpNetToMediaProxy_Type(Integer32):
    """Custom type alaIpNetToMediaProxy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlaIpNetToMediaProxy_Type.__name__ = "Integer32"
_AlaIpNetToMediaProxy_Object = MibTableColumn
alaIpNetToMediaProxy = _AlaIpNetToMediaProxy_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 2),
    _AlaIpNetToMediaProxy_Type()
)
alaIpNetToMediaProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNetToMediaProxy.setStatus("current")


class _AlaIpNetToMediaVrrp_Type(Integer32):
    """Custom type alaIpNetToMediaVrrp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlaIpNetToMediaVrrp_Type.__name__ = "Integer32"
_AlaIpNetToMediaVrrp_Object = MibTableColumn
alaIpNetToMediaVrrp = _AlaIpNetToMediaVrrp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 3),
    _AlaIpNetToMediaVrrp_Type()
)
alaIpNetToMediaVrrp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaVrrp.setStatus("current")


class _AlaIpNetToMediaAuth_Type(Integer32):
    """Custom type alaIpNetToMediaAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlaIpNetToMediaAuth_Type.__name__ = "Integer32"
_AlaIpNetToMediaAuth_Object = MibTableColumn
alaIpNetToMediaAuth = _AlaIpNetToMediaAuth_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 4),
    _AlaIpNetToMediaAuth_Type()
)
alaIpNetToMediaAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaAuth.setStatus("current")


class _AlaIpNetToMediaName_Type(SnmpAdminString):
    """Custom type alaIpNetToMediaName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_AlaIpNetToMediaName_Type.__name__ = "SnmpAdminString"
_AlaIpNetToMediaName_Object = MibTableColumn
alaIpNetToMediaName = _AlaIpNetToMediaName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 5),
    _AlaIpNetToMediaName_Type()
)
alaIpNetToMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNetToMediaName.setStatus("current")


class _AlaIpNetToMediaStaticIntfRt_Type(Integer32):
    """Custom type alaIpNetToMediaStaticIntfRt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("no", 0),
          ("yes", 1))
    )


_AlaIpNetToMediaStaticIntfRt_Type.__name__ = "Integer32"
_AlaIpNetToMediaStaticIntfRt_Object = MibTableColumn
alaIpNetToMediaStaticIntfRt = _AlaIpNetToMediaStaticIntfRt_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 2, 1, 6),
    _AlaIpNetToMediaStaticIntfRt_Type()
)
alaIpNetToMediaStaticIntfRt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaStaticIntfRt.setStatus("current")
_AlaDoSConfig_ObjectIdentity = ObjectIdentity
alaDoSConfig = _AlaDoSConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3)
)
_AlaDoSTable_Object = MibTable
alaDoSTable = _AlaDoSTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    alaDoSTable.setStatus("current")
_AlaDoSEntry_Object = MibTableRow
alaDoSEntry = _AlaDoSEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1)
)
alaDoSEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaDoSType"),
)
if mibBuilder.loadTexts:
    alaDoSEntry.setStatus("current")


class _AlaDoSType_Type(Integer32):
    """Custom type alaDoSType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("portscan", 0),
          ("tcpsyn", 1),
          ("pingofdeath", 2),
          ("smurf", 3),
          ("pepsi", 4),
          ("land", 5),
          ("teardropBonkBoink", 6),
          ("loopbacksrcip", 7),
          ("invalidip", 8),
          ("mcastmismatch", 9),
          ("ucastipmcastmac", 10),
          ("pingattack", 11),
          ("arpattack", 12),
          ("arppoison", 13),
          ("antispoof", 14))
    )


_AlaDoSType_Type.__name__ = "Integer32"
_AlaDoSType_Object = MibTableColumn
alaDoSType = _AlaDoSType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 1),
    _AlaDoSType_Type()
)
alaDoSType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSType.setStatus("current")
_AlaDoSDetected_Type = Counter32
_AlaDoSDetected_Object = MibTableColumn
alaDoSDetected = _AlaDoSDetected_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 2),
    _AlaDoSDetected_Type()
)
alaDoSDetected.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSDetected.setStatus("current")
_AlaDoSIp_Type = IpAddress
_AlaDoSIp_Object = MibTableColumn
alaDoSIp = _AlaDoSIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 3),
    _AlaDoSIp_Type()
)
alaDoSIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSIp.setStatus("current")
_AlaDoSMac_Type = MacAddress
_AlaDoSMac_Object = MibTableColumn
alaDoSMac = _AlaDoSMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 4),
    _AlaDoSMac_Type()
)
alaDoSMac.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSMac.setStatus("current")
_AlaDoSSlot_Type = Integer32
_AlaDoSSlot_Object = MibTableColumn
alaDoSSlot = _AlaDoSSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 5),
    _AlaDoSSlot_Type()
)
alaDoSSlot.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSSlot.setStatus("obsolete")
_AlaDoSPort_Type = Integer32
_AlaDoSPort_Object = MibTableColumn
alaDoSPort = _AlaDoSPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 6),
    _AlaDoSPort_Type()
)
alaDoSPort.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSPort.setStatus("obsolete")


class _AlaDoSStatus_Type(Integer32):
    """Custom type alaDoSStatus based on Integer32"""
    defaultValue = 1

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


_AlaDoSStatus_Type.__name__ = "Integer32"
_AlaDoSStatus_Object = MibTableColumn
alaDoSStatus = _AlaDoSStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 7),
    _AlaDoSStatus_Type()
)
alaDoSStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSStatus.setStatus("current")
_AlaDoSChassisId_Type = Integer32
_AlaDoSChassisId_Object = MibTableColumn
alaDoSChassisId = _AlaDoSChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 8),
    _AlaDoSChassisId_Type()
)
alaDoSChassisId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSChassisId.setStatus("obsolete")
_AlaDoSPortIfindex_Type = InterfaceIndexOrZero
_AlaDoSPortIfindex_Object = MibTableColumn
alaDoSPortIfindex = _AlaDoSPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 1, 1, 9),
    _AlaDoSPortIfindex_Type()
)
alaDoSPortIfindex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    alaDoSPortIfindex.setStatus("current")


class _AlaDoSPortScanClosePortPenalty_Type(Integer32):
    """Custom type alaDoSPortScanClosePortPenalty based on Integer32"""
    defaultValue = 10


_AlaDoSPortScanClosePortPenalty_Type.__name__ = "Integer32"
_AlaDoSPortScanClosePortPenalty_Object = MibScalar
alaDoSPortScanClosePortPenalty = _AlaDoSPortScanClosePortPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 2),
    _AlaDoSPortScanClosePortPenalty_Type()
)
alaDoSPortScanClosePortPenalty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanClosePortPenalty.setStatus("current")


class _AlaDoSPortScanTcpOpenPortPenalty_Type(Integer32):
    """Custom type alaDoSPortScanTcpOpenPortPenalty based on Integer32"""
    defaultValue = 0


_AlaDoSPortScanTcpOpenPortPenalty_Type.__name__ = "Integer32"
_AlaDoSPortScanTcpOpenPortPenalty_Object = MibScalar
alaDoSPortScanTcpOpenPortPenalty = _AlaDoSPortScanTcpOpenPortPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 3),
    _AlaDoSPortScanTcpOpenPortPenalty_Type()
)
alaDoSPortScanTcpOpenPortPenalty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanTcpOpenPortPenalty.setStatus("current")


class _AlaDoSPortScanUdpOpenPortPenalty_Type(Integer32):
    """Custom type alaDoSPortScanUdpOpenPortPenalty based on Integer32"""
    defaultValue = 0


_AlaDoSPortScanUdpOpenPortPenalty_Type.__name__ = "Integer32"
_AlaDoSPortScanUdpOpenPortPenalty_Object = MibScalar
alaDoSPortScanUdpOpenPortPenalty = _AlaDoSPortScanUdpOpenPortPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 4),
    _AlaDoSPortScanUdpOpenPortPenalty_Type()
)
alaDoSPortScanUdpOpenPortPenalty.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanUdpOpenPortPenalty.setStatus("current")
_AlaDoSPortScanTotalPenalty_Type = Integer32
_AlaDoSPortScanTotalPenalty_Object = MibScalar
alaDoSPortScanTotalPenalty = _AlaDoSPortScanTotalPenalty_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 5),
    _AlaDoSPortScanTotalPenalty_Type()
)
alaDoSPortScanTotalPenalty.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSPortScanTotalPenalty.setStatus("current")


class _AlaDoSPortScanThreshold_Type(Integer32):
    """Custom type alaDoSPortScanThreshold based on Integer32"""
    defaultValue = 1000


_AlaDoSPortScanThreshold_Type.__name__ = "Integer32"
_AlaDoSPortScanThreshold_Object = MibScalar
alaDoSPortScanThreshold = _AlaDoSPortScanThreshold_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 6),
    _AlaDoSPortScanThreshold_Type()
)
alaDoSPortScanThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanThreshold.setStatus("current")


class _AlaDoSPortScanDecay_Type(Integer32):
    """Custom type alaDoSPortScanDecay based on Integer32"""
    defaultValue = 2


_AlaDoSPortScanDecay_Type.__name__ = "Integer32"
_AlaDoSPortScanDecay_Object = MibScalar
alaDoSPortScanDecay = _AlaDoSPortScanDecay_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 7),
    _AlaDoSPortScanDecay_Type()
)
alaDoSPortScanDecay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPortScanDecay.setStatus("current")


class _AlaDoSTrapCntl_Type(Integer32):
    """Custom type alaDoSTrapCntl based on Integer32"""
    defaultValue = 1

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


_AlaDoSTrapCntl_Type.__name__ = "Integer32"
_AlaDoSTrapCntl_Object = MibScalar
alaDoSTrapCntl = _AlaDoSTrapCntl_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 8),
    _AlaDoSTrapCntl_Type()
)
alaDoSTrapCntl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSTrapCntl.setStatus("current")


class _AlaDoSARPRate_Type(Integer32):
    """Custom type alaDoSARPRate based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 500),
    )


_AlaDoSARPRate_Type.__name__ = "Integer32"
_AlaDoSARPRate_Object = MibScalar
alaDoSARPRate = _AlaDoSARPRate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 9),
    _AlaDoSARPRate_Type()
)
alaDoSARPRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSARPRate.setStatus("current")


class _AlaDoSPingRate_Type(Integer32):
    """Custom type alaDoSPingRate based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10000),
    )


_AlaDoSPingRate_Type.__name__ = "Integer32"
_AlaDoSPingRate_Object = MibScalar
alaDoSPingRate = _AlaDoSPingRate_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 10),
    _AlaDoSPingRate_Type()
)
alaDoSPingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSPingRate.setStatus("current")
_AlaDoSArpPoisonTable_Object = MibTable
alaDoSArpPoisonTable = _AlaDoSArpPoisonTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 11)
)
if mibBuilder.loadTexts:
    alaDoSArpPoisonTable.setStatus("current")
_AlaDoSArpPoisonEntry_Object = MibTableRow
alaDoSArpPoisonEntry = _AlaDoSArpPoisonEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 11, 1)
)
alaDoSArpPoisonEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaDoSArpPoisonIpAddr"),
)
if mibBuilder.loadTexts:
    alaDoSArpPoisonEntry.setStatus("current")
_AlaDoSArpPoisonIpAddr_Type = IpAddress
_AlaDoSArpPoisonIpAddr_Object = MibTableColumn
alaDoSArpPoisonIpAddr = _AlaDoSArpPoisonIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 11, 1, 1),
    _AlaDoSArpPoisonIpAddr_Type()
)
alaDoSArpPoisonIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDoSArpPoisonIpAddr.setStatus("current")
_AlaDoSArpPoisonDetected_Type = Counter32
_AlaDoSArpPoisonDetected_Object = MibTableColumn
alaDoSArpPoisonDetected = _AlaDoSArpPoisonDetected_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 11, 1, 2),
    _AlaDoSArpPoisonDetected_Type()
)
alaDoSArpPoisonDetected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSArpPoisonDetected.setStatus("current")
_AlaDoSArpPoisonRowStatus_Type = RowStatus
_AlaDoSArpPoisonRowStatus_Object = MibTableColumn
alaDoSArpPoisonRowStatus = _AlaDoSArpPoisonRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 11, 1, 3),
    _AlaDoSArpPoisonRowStatus_Type()
)
alaDoSArpPoisonRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDoSArpPoisonRowStatus.setStatus("current")


class _AlaDoSAntiSpoofGlobalCountReset_Type(Integer32):
    """Custom type alaDoSAntiSpoofGlobalCountReset based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaDoSAntiSpoofGlobalCountReset_Type.__name__ = "Integer32"
_AlaDoSAntiSpoofGlobalCountReset_Object = MibScalar
alaDoSAntiSpoofGlobalCountReset = _AlaDoSAntiSpoofGlobalCountReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 12),
    _AlaDoSAntiSpoofGlobalCountReset_Type()
)
alaDoSAntiSpoofGlobalCountReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofGlobalCountReset.setStatus("current")
_AlaDoSAntiSpoofTable_Object = MibTable
alaDoSAntiSpoofTable = _AlaDoSAntiSpoofTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13)
)
if mibBuilder.loadTexts:
    alaDoSAntiSpoofTable.setStatus("current")
_AlaDoSAntiSpoofEntry_Object = MibTableRow
alaDoSAntiSpoofEntry = _AlaDoSAntiSpoofEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13, 1)
)
alaDoSAntiSpoofEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaDoSAntiSpoofIPAddressType"),
    (0, "ALCATEL-ENT1-IP-MIB", "alaDoSAntiSpoofIPAddress"),
)
if mibBuilder.loadTexts:
    alaDoSAntiSpoofEntry.setStatus("current")


class _AlaDoSAntiSpoofIPAddressType_Type(InetAddressType):
    """Custom type alaDoSAntiSpoofIPAddressType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ipv4", 1),
          ("ipv6", 2))
    )


_AlaDoSAntiSpoofIPAddressType_Type.__name__ = "InetAddressType"
_AlaDoSAntiSpoofIPAddressType_Object = MibTableColumn
alaDoSAntiSpoofIPAddressType = _AlaDoSAntiSpoofIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13, 1, 1),
    _AlaDoSAntiSpoofIPAddressType_Type()
)
alaDoSAntiSpoofIPAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofIPAddressType.setStatus("current")


class _AlaDoSAntiSpoofIPAddress_Type(InetAddress):
    """Custom type alaDoSAntiSpoofIPAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_AlaDoSAntiSpoofIPAddress_Type.__name__ = "InetAddress"
_AlaDoSAntiSpoofIPAddress_Object = MibTableColumn
alaDoSAntiSpoofIPAddress = _AlaDoSAntiSpoofIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13, 1, 2),
    _AlaDoSAntiSpoofIPAddress_Type()
)
alaDoSAntiSpoofIPAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofIPAddress.setStatus("current")


class _AlaDoSAntiSpoofStatus_Type(Integer32):
    """Custom type alaDoSAntiSpoofStatus based on Integer32"""
    defaultValue = 1

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


_AlaDoSAntiSpoofStatus_Type.__name__ = "Integer32"
_AlaDoSAntiSpoofStatus_Object = MibTableColumn
alaDoSAntiSpoofStatus = _AlaDoSAntiSpoofStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13, 1, 3),
    _AlaDoSAntiSpoofStatus_Type()
)
alaDoSAntiSpoofStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofStatus.setStatus("current")
_AlaDoSAntiSpoofMacAddress_Type = MacAddress
_AlaDoSAntiSpoofMacAddress_Object = MibTableColumn
alaDoSAntiSpoofMacAddress = _AlaDoSAntiSpoofMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13, 1, 4),
    _AlaDoSAntiSpoofMacAddress_Type()
)
alaDoSAntiSpoofMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofMacAddress.setStatus("current")
_AlaDoSAntiSpoofIfIndex_Type = InterfaceIndexOrZero
_AlaDoSAntiSpoofIfIndex_Object = MibTableColumn
alaDoSAntiSpoofIfIndex = _AlaDoSAntiSpoofIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13, 1, 5),
    _AlaDoSAntiSpoofIfIndex_Type()
)
alaDoSAntiSpoofIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofIfIndex.setStatus("current")


class _AlaDoSAntiSpoofVlan_Type(Integer32):
    """Custom type alaDoSAntiSpoofVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaDoSAntiSpoofVlan_Type.__name__ = "Integer32"
_AlaDoSAntiSpoofVlan_Object = MibTableColumn
alaDoSAntiSpoofVlan = _AlaDoSAntiSpoofVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13, 1, 6),
    _AlaDoSAntiSpoofVlan_Type()
)
alaDoSAntiSpoofVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofVlan.setStatus("current")
_AlaDoSAntiSpoofCount_Type = Counter32
_AlaDoSAntiSpoofCount_Object = MibTableColumn
alaDoSAntiSpoofCount = _AlaDoSAntiSpoofCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13, 1, 7),
    _AlaDoSAntiSpoofCount_Type()
)
alaDoSAntiSpoofCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofCount.setStatus("current")


class _AlaDoSAntiSpoofCountReset_Type(Integer32):
    """Custom type alaDoSAntiSpoofCountReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 1),
          ("reset", 2))
    )


_AlaDoSAntiSpoofCountReset_Type.__name__ = "Integer32"
_AlaDoSAntiSpoofCountReset_Object = MibTableColumn
alaDoSAntiSpoofCountReset = _AlaDoSAntiSpoofCountReset_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13, 1, 8),
    _AlaDoSAntiSpoofCountReset_Type()
)
alaDoSAntiSpoofCountReset.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofCountReset.setStatus("current")
_AlaDoSAntiSpoofRowStatus_Type = RowStatus
_AlaDoSAntiSpoofRowStatus_Object = MibTableColumn
alaDoSAntiSpoofRowStatus = _AlaDoSAntiSpoofRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 3, 13, 1, 9),
    _AlaDoSAntiSpoofRowStatus_Type()
)
alaDoSAntiSpoofRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaDoSAntiSpoofRowStatus.setStatus("current")
_IpNetToMediaAugTable_Object = MibTable
ipNetToMediaAugTable = _IpNetToMediaAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4)
)
if mibBuilder.loadTexts:
    ipNetToMediaAugTable.setStatus("current")
_IpNetToMediaAugEntry_Object = MibTableRow
ipNetToMediaAugEntry = _IpNetToMediaAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    ipNetToMediaAugEntry.setStatus("current")
_IpNetToMediaSlot_Type = Integer32
_IpNetToMediaSlot_Object = MibTableColumn
ipNetToMediaSlot = _IpNetToMediaSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 1),
    _IpNetToMediaSlot_Type()
)
ipNetToMediaSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaSlot.setStatus("obsolete")
_IpNetToMediaPort_Type = Integer32
_IpNetToMediaPort_Object = MibTableColumn
ipNetToMediaPort = _IpNetToMediaPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 2),
    _IpNetToMediaPort_Type()
)
ipNetToMediaPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaPort.setStatus("obsolete")


class _IpNetToMediaName_Type(SnmpAdminString):
    """Custom type ipNetToMediaName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 31),
    )


_IpNetToMediaName_Type.__name__ = "SnmpAdminString"
_IpNetToMediaName_Object = MibTableColumn
ipNetToMediaName = _IpNetToMediaName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 3),
    _IpNetToMediaName_Type()
)
ipNetToMediaName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaName.setStatus("current")
_IpNetToMediaChassisId_Type = Integer32
_IpNetToMediaChassisId_Object = MibTableColumn
ipNetToMediaChassisId = _IpNetToMediaChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 4),
    _IpNetToMediaChassisId_Type()
)
ipNetToMediaChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaChassisId.setStatus("obsolete")
_IpNetToMediaPortIfindex_Type = InterfaceIndexOrZero
_IpNetToMediaPortIfindex_Object = MibTableColumn
ipNetToMediaPortIfindex = _IpNetToMediaPortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 5),
    _IpNetToMediaPortIfindex_Type()
)
ipNetToMediaPortIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ipNetToMediaPortIfindex.setStatus("current")


class _IpNetToMediaSubType_Type(Integer32):
    """Custom type ipNetToMediaSubType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("default", 0),
          ("sap", 1),
          ("sBind", 2))
    )


_IpNetToMediaSubType_Type.__name__ = "Integer32"
_IpNetToMediaSubType_Object = MibTableColumn
ipNetToMediaSubType = _IpNetToMediaSubType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 6),
    _IpNetToMediaSubType_Type()
)
ipNetToMediaSubType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNetToMediaSubType.setStatus("current")


class _IpNetToMediaSubId_Type(Integer32):
    """Custom type ipNetToMediaSubId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_IpNetToMediaSubId_Type.__name__ = "Integer32"
_IpNetToMediaSubId_Object = MibTableColumn
ipNetToMediaSubId = _IpNetToMediaSubId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 4, 1, 7),
    _IpNetToMediaSubId_Type()
)
ipNetToMediaSubId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipNetToMediaSubId.setStatus("current")
_TrafficEventTrapObjs_ObjectIdentity = ObjectIdentity
trafficEventTrapObjs = _TrafficEventTrapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 5)
)


class _PktDropType_Type(Integer32):
    """Custom type pktDropType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("spoofedIp", 0),
          ("toBlockedPort", 1),
          ("rulematchTriggeredPortDisable", 2),
          ("spoofTriggeredUserPortDisable", 3),
          ("bpduTriggeredUserPortDisable", 4),
          ("bgpTriggeredUserPortDisable", 5),
          ("ospfTriggeredUserPortDisable", 6),
          ("ripTriggeredUserPortDisable", 7),
          ("vrrpTriggeredUserPortDisable", 8))
    )


_PktDropType_Type.__name__ = "Integer32"
_PktDropType_Object = MibScalar
pktDropType = _PktDropType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 5, 1),
    _PktDropType_Type()
)
pktDropType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropType.setStatus("current")
_PktDropIfIndex_Type = InterfaceIndexOrZero
_PktDropIfIndex_Object = MibScalar
pktDropIfIndex = _PktDropIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 5, 2),
    _PktDropIfIndex_Type()
)
pktDropIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropIfIndex.setStatus("current")
_PktDropCount_Type = Integer32
_PktDropCount_Object = MibScalar
pktDropCount = _PktDropCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 5, 3),
    _PktDropCount_Type()
)
pktDropCount.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropCount.setStatus("current")


class _PktDropFrag_Type(OctetString):
    """Custom type pktDropFrag based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_PktDropFrag_Type.__name__ = "OctetString"
_PktDropFrag_Object = MibScalar
pktDropFrag = _PktDropFrag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 5, 4),
    _PktDropFrag_Type()
)
pktDropFrag.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    pktDropFrag.setStatus("current")
_IpCidrRouteAugTable_Object = MibTable
ipCidrRouteAugTable = _IpCidrRouteAugTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 6)
)
if mibBuilder.loadTexts:
    ipCidrRouteAugTable.setStatus("current")
_IpCidrRouteAugEntry_Object = MibTableRow
ipCidrRouteAugEntry = _IpCidrRouteAugEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    ipCidrRouteAugEntry.setStatus("current")


class _IpCidrRouteScope_Type(Integer32):
    """Custom type ipCidrRouteScope based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("niroute", 1),
          ("emproute", 2))
    )


_IpCidrRouteScope_Type.__name__ = "Integer32"
_IpCidrRouteScope_Object = MibTableColumn
ipCidrRouteScope = _IpCidrRouteScope_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 6, 1, 1),
    _IpCidrRouteScope_Type()
)
ipCidrRouteScope.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ipCidrRouteScope.setStatus("current")
_AlaIcmpCtrlTable_Object = MibTable
alaIcmpCtrlTable = _AlaIcmpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7)
)
if mibBuilder.loadTexts:
    alaIcmpCtrlTable.setStatus("current")
_AlaIcmpCtrlEntry_Object = MibTableRow
alaIcmpCtrlEntry = _AlaIcmpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7, 1)
)
alaIcmpCtrlEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaIcmpCtrlType"),
    (0, "ALCATEL-ENT1-IP-MIB", "alaIcmpCtrlCode"),
)
if mibBuilder.loadTexts:
    alaIcmpCtrlEntry.setStatus("current")


class _AlaIcmpCtrlType_Type(Integer32):
    """Custom type alaIcmpCtrlType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 18),
    )


_AlaIcmpCtrlType_Type.__name__ = "Integer32"
_AlaIcmpCtrlType_Object = MibTableColumn
alaIcmpCtrlType = _AlaIcmpCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7, 1, 1),
    _AlaIcmpCtrlType_Type()
)
alaIcmpCtrlType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIcmpCtrlType.setStatus("current")


class _AlaIcmpCtrlCode_Type(Integer32):
    """Custom type alaIcmpCtrlCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_AlaIcmpCtrlCode_Type.__name__ = "Integer32"
_AlaIcmpCtrlCode_Object = MibTableColumn
alaIcmpCtrlCode = _AlaIcmpCtrlCode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7, 1, 2),
    _AlaIcmpCtrlCode_Type()
)
alaIcmpCtrlCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIcmpCtrlCode.setStatus("current")


class _AlaIcmpCtrlStatus_Type(Integer32):
    """Custom type alaIcmpCtrlStatus based on Integer32"""
    defaultValue = 1

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


_AlaIcmpCtrlStatus_Type.__name__ = "Integer32"
_AlaIcmpCtrlStatus_Object = MibTableColumn
alaIcmpCtrlStatus = _AlaIcmpCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7, 1, 3),
    _AlaIcmpCtrlStatus_Type()
)
alaIcmpCtrlStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIcmpCtrlStatus.setStatus("current")


class _AlaIcmpCtrlPktGap_Type(Integer32):
    """Custom type alaIcmpCtrlPktGap based on Integer32"""
    defaultValue = 0


_AlaIcmpCtrlPktGap_Type.__name__ = "Integer32"
_AlaIcmpCtrlPktGap_Object = MibTableColumn
alaIcmpCtrlPktGap = _AlaIcmpCtrlPktGap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 7, 1, 4),
    _AlaIcmpCtrlPktGap_Type()
)
alaIcmpCtrlPktGap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIcmpCtrlPktGap.setStatus("current")
_AlaIpRouteSumTable_Object = MibTable
alaIpRouteSumTable = _AlaIpRouteSumTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 9)
)
if mibBuilder.loadTexts:
    alaIpRouteSumTable.setStatus("current")
_AlaIpRouteSumEntry_Object = MibTableRow
alaIpRouteSumEntry = _AlaIpRouteSumEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 9, 1)
)
alaIpRouteSumEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaIpRouteProtocol"),
)
if mibBuilder.loadTexts:
    alaIpRouteSumEntry.setStatus("current")


class _AlaIpRouteProtocol_Type(Integer32):
    """Custom type alaIpRouteProtocol based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("total", 1),
          ("local", 2),
          ("netmgmt", 3),
          ("rip", 4),
          ("isis", 5),
          ("ospf", 6),
          ("bgp", 7),
          ("other", 8))
    )


_AlaIpRouteProtocol_Type.__name__ = "Integer32"
_AlaIpRouteProtocol_Object = MibTableColumn
alaIpRouteProtocol = _AlaIpRouteProtocol_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 9, 1, 1),
    _AlaIpRouteProtocol_Type()
)
alaIpRouteProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpRouteProtocol.setStatus("current")
_AlaIpRouteCount_Type = Integer32
_AlaIpRouteCount_Object = MibTableColumn
alaIpRouteCount = _AlaIpRouteCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 9, 1, 2),
    _AlaIpRouteCount_Type()
)
alaIpRouteCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpRouteCount.setStatus("current")
_AlaIcmpCtrl_ObjectIdentity = ObjectIdentity
alaIcmpCtrl = _AlaIcmpCtrl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 10)
)


class _AlaIcmpAllMsgStatus_Type(Integer32):
    """Custom type alaIcmpAllMsgStatus based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("other", 3))
    )


_AlaIcmpAllMsgStatus_Type.__name__ = "Integer32"
_AlaIcmpAllMsgStatus_Object = MibScalar
alaIcmpAllMsgStatus = _AlaIcmpAllMsgStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 10, 1),
    _AlaIcmpAllMsgStatus_Type()
)
alaIcmpAllMsgStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIcmpAllMsgStatus.setStatus("current")
_AlaIpArpFilterTable_Object = MibTable
alaIpArpFilterTable = _AlaIpArpFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11)
)
if mibBuilder.loadTexts:
    alaIpArpFilterTable.setStatus("current")
_AlaIpArpFilterEntry_Object = MibTableRow
alaIpArpFilterEntry = _AlaIpArpFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1)
)
alaIpArpFilterEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaIpArpFilterIpAddr"),
    (0, "ALCATEL-ENT1-IP-MIB", "alaIpArpFilterIpMask"),
    (0, "ALCATEL-ENT1-IP-MIB", "alaIpArpFilterVlan"),
    (0, "ALCATEL-ENT1-IP-MIB", "alaIpArpFilterType"),
)
if mibBuilder.loadTexts:
    alaIpArpFilterEntry.setStatus("current")
_AlaIpArpFilterIpAddr_Type = IpAddress
_AlaIpArpFilterIpAddr_Object = MibTableColumn
alaIpArpFilterIpAddr = _AlaIpArpFilterIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 1),
    _AlaIpArpFilterIpAddr_Type()
)
alaIpArpFilterIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpArpFilterIpAddr.setStatus("current")
_AlaIpArpFilterIpMask_Type = IpAddress
_AlaIpArpFilterIpMask_Object = MibTableColumn
alaIpArpFilterIpMask = _AlaIpArpFilterIpMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 2),
    _AlaIpArpFilterIpMask_Type()
)
alaIpArpFilterIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpArpFilterIpMask.setStatus("current")


class _AlaIpArpFilterVlan_Type(Integer32):
    """Custom type alaIpArpFilterVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpArpFilterVlan_Type.__name__ = "Integer32"
_AlaIpArpFilterVlan_Object = MibTableColumn
alaIpArpFilterVlan = _AlaIpArpFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 3),
    _AlaIpArpFilterVlan_Type()
)
alaIpArpFilterVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpArpFilterVlan.setStatus("current")


class _AlaIpArpFilterType_Type(Integer32):
    """Custom type alaIpArpFilterType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("target", 1),
          ("sender", 2))
    )


_AlaIpArpFilterType_Type.__name__ = "Integer32"
_AlaIpArpFilterType_Object = MibTableColumn
alaIpArpFilterType = _AlaIpArpFilterType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 4),
    _AlaIpArpFilterType_Type()
)
alaIpArpFilterType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpArpFilterType.setStatus("current")


class _AlaIpArpFilterMode_Type(Integer32):
    """Custom type alaIpArpFilterMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("allow", 1),
          ("block", 2))
    )


_AlaIpArpFilterMode_Type.__name__ = "Integer32"
_AlaIpArpFilterMode_Object = MibTableColumn
alaIpArpFilterMode = _AlaIpArpFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 5),
    _AlaIpArpFilterMode_Type()
)
alaIpArpFilterMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpArpFilterMode.setStatus("current")
_AlaIpArpFilterRowStatus_Type = RowStatus
_AlaIpArpFilterRowStatus_Object = MibTableColumn
alaIpArpFilterRowStatus = _AlaIpArpFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 11, 1, 6),
    _AlaIpArpFilterRowStatus_Type()
)
alaIpArpFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpArpFilterRowStatus.setStatus("current")
_AlaIpServiceTable_Object = MibTable
alaIpServiceTable = _AlaIpServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 12)
)
if mibBuilder.loadTexts:
    alaIpServiceTable.setStatus("current")
_AlaIpServiceEntry_Object = MibTableRow
alaIpServiceEntry = _AlaIpServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 12, 1)
)
alaIpServiceEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaIpServiceType"),
)
if mibBuilder.loadTexts:
    alaIpServiceEntry.setStatus("current")


class _AlaIpServiceType_Type(Integer32):
    """Custom type alaIpServiceType based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("ftp", 1),
          ("ssh", 2),
          ("telnet", 3),
          ("http", 4),
          ("ntp", 5),
          ("snmp", 6),
          ("https", 7),
          ("radius", 8))
    )


_AlaIpServiceType_Type.__name__ = "Integer32"
_AlaIpServiceType_Object = MibTableColumn
alaIpServiceType = _AlaIpServiceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 12, 1, 1),
    _AlaIpServiceType_Type()
)
alaIpServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpServiceType.setStatus("current")


class _AlaIpServicePort_Type(Integer32):
    """Custom type alaIpServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaIpServicePort_Type.__name__ = "Integer32"
_AlaIpServicePort_Object = MibTableColumn
alaIpServicePort = _AlaIpServicePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 12, 1, 2),
    _AlaIpServicePort_Type()
)
alaIpServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpServicePort.setStatus("current")


class _AlaIpServiceStatus_Type(Integer32):
    """Custom type alaIpServiceStatus based on Integer32"""
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
        *(("enabled", 1),
          ("disabled", 2),
          ("other", 3))
    )


_AlaIpServiceStatus_Type.__name__ = "Integer32"
_AlaIpServiceStatus_Object = MibTableColumn
alaIpServiceStatus = _AlaIpServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 12, 1, 3),
    _AlaIpServiceStatus_Type()
)
alaIpServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpServiceStatus.setStatus("current")
_AlaIpPortServiceTable_Object = MibTable
alaIpPortServiceTable = _AlaIpPortServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 13)
)
if mibBuilder.loadTexts:
    alaIpPortServiceTable.setStatus("deprecated")
_AlaIpPortServiceEntry_Object = MibTableRow
alaIpPortServiceEntry = _AlaIpPortServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 13, 1)
)
alaIpPortServiceEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaIpPortServicePort"),
)
if mibBuilder.loadTexts:
    alaIpPortServiceEntry.setStatus("deprecated")


class _AlaIpPortServicePort_Type(Integer32):
    """Custom type alaIpPortServicePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AlaIpPortServicePort_Type.__name__ = "Integer32"
_AlaIpPortServicePort_Object = MibTableColumn
alaIpPortServicePort = _AlaIpPortServicePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 13, 1, 1),
    _AlaIpPortServicePort_Type()
)
alaIpPortServicePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpPortServicePort.setStatus("deprecated")


class _AlaIpPortServiceStatus_Type(Integer32):
    """Custom type alaIpPortServiceStatus based on Integer32"""
    defaultValue = 1

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


_AlaIpPortServiceStatus_Type.__name__ = "Integer32"
_AlaIpPortServiceStatus_Object = MibTableColumn
alaIpPortServiceStatus = _AlaIpPortServiceStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 13, 1, 2),
    _AlaIpPortServiceStatus_Type()
)
alaIpPortServiceStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpPortServiceStatus.setStatus("deprecated")
_AlaIpInterfaceTable_Object = MibTable
alaIpInterfaceTable = _AlaIpInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14)
)
if mibBuilder.loadTexts:
    alaIpInterfaceTable.setStatus("current")
_AlaIpInterfaceEntry_Object = MibTableRow
alaIpInterfaceEntry = _AlaIpInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1)
)
alaIpInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    alaIpInterfaceEntry.setStatus("current")


class _AlaIpInterfaceName_Type(SnmpAdminString):
    """Custom type alaIpInterfaceName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaIpInterfaceName_Type.__name__ = "SnmpAdminString"
_AlaIpInterfaceName_Object = MibTableColumn
alaIpInterfaceName = _AlaIpInterfaceName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 1),
    _AlaIpInterfaceName_Type()
)
alaIpInterfaceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceName.setStatus("current")


class _AlaIpInterfaceAddress_Type(IpAddress):
    """Custom type alaIpInterfaceAddress based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpInterfaceAddress_Type.__name__ = "IpAddress"
_AlaIpInterfaceAddress_Object = MibTableColumn
alaIpInterfaceAddress = _AlaIpInterfaceAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 2),
    _AlaIpInterfaceAddress_Type()
)
alaIpInterfaceAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceAddress.setStatus("current")


class _AlaIpInterfaceMask_Type(IpAddress):
    """Custom type alaIpInterfaceMask based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpInterfaceMask_Type.__name__ = "IpAddress"
_AlaIpInterfaceMask_Object = MibTableColumn
alaIpInterfaceMask = _AlaIpInterfaceMask_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 3),
    _AlaIpInterfaceMask_Type()
)
alaIpInterfaceMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceMask.setStatus("current")


class _AlaIpInterfaceAdminState_Type(Integer32):
    """Custom type alaIpInterfaceAdminState based on Integer32"""
    defaultValue = 1

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


_AlaIpInterfaceAdminState_Type.__name__ = "Integer32"
_AlaIpInterfaceAdminState_Object = MibTableColumn
alaIpInterfaceAdminState = _AlaIpInterfaceAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 4),
    _AlaIpInterfaceAdminState_Type()
)
alaIpInterfaceAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceAdminState.setStatus("current")


class _AlaIpInterfaceDeviceType_Type(Integer32):
    """Custom type alaIpInterfaceDeviceType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("unbound", 0),
          ("vlan", 1),
          ("emp", 2),
          ("loopback", 3),
          ("greTunnel", 4),
          ("ipipTunnel", 5),
          ("service", 6))
    )


_AlaIpInterfaceDeviceType_Type.__name__ = "Integer32"
_AlaIpInterfaceDeviceType_Object = MibTableColumn
alaIpInterfaceDeviceType = _AlaIpInterfaceDeviceType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 5),
    _AlaIpInterfaceDeviceType_Type()
)
alaIpInterfaceDeviceType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDeviceType.setStatus("current")


class _AlaIpInterfaceVlanID_Type(Integer32):
    """Custom type alaIpInterfaceVlanID based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AlaIpInterfaceVlanID_Type.__name__ = "Integer32"
_AlaIpInterfaceVlanID_Object = MibTableColumn
alaIpInterfaceVlanID = _AlaIpInterfaceVlanID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 6),
    _AlaIpInterfaceVlanID_Type()
)
alaIpInterfaceVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceVlanID.setStatus("current")


class _AlaIpInterfaceIpForward_Type(Integer32):
    """Custom type alaIpInterfaceIpForward based on Integer32"""
    defaultValue = 1

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


_AlaIpInterfaceIpForward_Type.__name__ = "Integer32"
_AlaIpInterfaceIpForward_Object = MibTableColumn
alaIpInterfaceIpForward = _AlaIpInterfaceIpForward_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 7),
    _AlaIpInterfaceIpForward_Type()
)
alaIpInterfaceIpForward.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceIpForward.setStatus("current")


class _AlaIpInterfaceEncap_Type(Integer32):
    """Custom type alaIpInterfaceEncap based on Integer32"""
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
        *(("ethernet2", 1),
          ("snap", 2),
          ("service", 3))
    )


_AlaIpInterfaceEncap_Type.__name__ = "Integer32"
_AlaIpInterfaceEncap_Object = MibTableColumn
alaIpInterfaceEncap = _AlaIpInterfaceEncap_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 8),
    _AlaIpInterfaceEncap_Type()
)
alaIpInterfaceEncap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceEncap.setStatus("current")


class _AlaIpInterfaceMtu_Type(Unsigned32):
    """Custom type alaIpInterfaceMtu based on Unsigned32"""
    defaultValue = 0


_AlaIpInterfaceMtu_Type.__name__ = "Unsigned32"
_AlaIpInterfaceMtu_Object = MibTableColumn
alaIpInterfaceMtu = _AlaIpInterfaceMtu_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 9),
    _AlaIpInterfaceMtu_Type()
)
alaIpInterfaceMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceMtu.setStatus("current")


class _AlaIpInterfaceLocalProxyArp_Type(Integer32):
    """Custom type alaIpInterfaceLocalProxyArp based on Integer32"""
    defaultValue = 1

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


_AlaIpInterfaceLocalProxyArp_Type.__name__ = "Integer32"
_AlaIpInterfaceLocalProxyArp_Object = MibTableColumn
alaIpInterfaceLocalProxyArp = _AlaIpInterfaceLocalProxyArp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 10),
    _AlaIpInterfaceLocalProxyArp_Type()
)
alaIpInterfaceLocalProxyArp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceLocalProxyArp.setStatus("current")


class _AlaIpInterfacePrimCfg_Type(Integer32):
    """Custom type alaIpInterfacePrimCfg based on Integer32"""
    defaultValue = 0

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


_AlaIpInterfacePrimCfg_Type.__name__ = "Integer32"
_AlaIpInterfacePrimCfg_Object = MibTableColumn
alaIpInterfacePrimCfg = _AlaIpInterfacePrimCfg_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 11),
    _AlaIpInterfacePrimCfg_Type()
)
alaIpInterfacePrimCfg.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfacePrimCfg.setStatus("current")


class _AlaIpInterfaceOperState_Type(Integer32):
    """Custom type alaIpInterfaceOperState based on Integer32"""
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


_AlaIpInterfaceOperState_Type.__name__ = "Integer32"
_AlaIpInterfaceOperState_Object = MibTableColumn
alaIpInterfaceOperState = _AlaIpInterfaceOperState_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 12),
    _AlaIpInterfaceOperState_Type()
)
alaIpInterfaceOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceOperState.setStatus("current")


class _AlaIpInterfaceOperReason_Type(Integer32):
    """Custom type alaIpInterfaceOperReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("interfaceUp", 0),
          ("adminDown", 1),
          ("unbound", 2),
          ("deviceDown", 3),
          ("noSuchDevice", 4),
          ("noRouterMac", 5),
          ("tunnelSrcInvalid", 6),
          ("tunnelDstUnreachable", 7),
          ("noVipAddress", 8))
    )


_AlaIpInterfaceOperReason_Type.__name__ = "Integer32"
_AlaIpInterfaceOperReason_Object = MibTableColumn
alaIpInterfaceOperReason = _AlaIpInterfaceOperReason_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 13),
    _AlaIpInterfaceOperReason_Type()
)
alaIpInterfaceOperReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceOperReason.setStatus("current")
_AlaIpInterfaceRouterMac_Type = MacAddress
_AlaIpInterfaceRouterMac_Object = MibTableColumn
alaIpInterfaceRouterMac = _AlaIpInterfaceRouterMac_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 14),
    _AlaIpInterfaceRouterMac_Type()
)
alaIpInterfaceRouterMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceRouterMac.setStatus("current")
_AlaIpInterfaceBcastAddr_Type = IpAddress
_AlaIpInterfaceBcastAddr_Object = MibTableColumn
alaIpInterfaceBcastAddr = _AlaIpInterfaceBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 15),
    _AlaIpInterfaceBcastAddr_Type()
)
alaIpInterfaceBcastAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceBcastAddr.setStatus("current")


class _AlaIpInterfacePrimAct_Type(Integer32):
    """Custom type alaIpInterfacePrimAct based on Integer32"""
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


_AlaIpInterfacePrimAct_Type.__name__ = "Integer32"
_AlaIpInterfacePrimAct_Object = MibTableColumn
alaIpInterfacePrimAct = _AlaIpInterfacePrimAct_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 16),
    _AlaIpInterfacePrimAct_Type()
)
alaIpInterfacePrimAct.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfacePrimAct.setStatus("current")
_AlaIpInterfaceRemoteAddr_Type = IpAddress
_AlaIpInterfaceRemoteAddr_Object = MibTableColumn
alaIpInterfaceRemoteAddr = _AlaIpInterfaceRemoteAddr_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 17),
    _AlaIpInterfaceRemoteAddr_Type()
)
alaIpInterfaceRemoteAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceRemoteAddr.setStatus("current")
_AlaIpInterfaceTunnelSrcAddressType_Type = InetAddressType
_AlaIpInterfaceTunnelSrcAddressType_Object = MibTableColumn
alaIpInterfaceTunnelSrcAddressType = _AlaIpInterfaceTunnelSrcAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 18),
    _AlaIpInterfaceTunnelSrcAddressType_Type()
)
alaIpInterfaceTunnelSrcAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelSrcAddressType.setStatus("current")
_AlaIpInterfaceTunnelSrc_Type = InetAddress
_AlaIpInterfaceTunnelSrc_Object = MibTableColumn
alaIpInterfaceTunnelSrc = _AlaIpInterfaceTunnelSrc_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 19),
    _AlaIpInterfaceTunnelSrc_Type()
)
alaIpInterfaceTunnelSrc.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelSrc.setStatus("current")
_AlaIpInterfaceTunnelDstAddressType_Type = InetAddressType
_AlaIpInterfaceTunnelDstAddressType_Object = MibTableColumn
alaIpInterfaceTunnelDstAddressType = _AlaIpInterfaceTunnelDstAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 20),
    _AlaIpInterfaceTunnelDstAddressType_Type()
)
alaIpInterfaceTunnelDstAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelDstAddressType.setStatus("current")
_AlaIpInterfaceTunnelDst_Type = InetAddress
_AlaIpInterfaceTunnelDst_Object = MibTableColumn
alaIpInterfaceTunnelDst = _AlaIpInterfaceTunnelDst_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 21),
    _AlaIpInterfaceTunnelDst_Type()
)
alaIpInterfaceTunnelDst.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTunnelDst.setStatus("current")


class _AlaIpInterfaceVipAddress_Type(IpAddress):
    """Custom type alaIpInterfaceVipAddress based on IpAddress"""
    defaultHexValue = "00000000"


_AlaIpInterfaceVipAddress_Type.__name__ = "IpAddress"
_AlaIpInterfaceVipAddress_Object = MibTableColumn
alaIpInterfaceVipAddress = _AlaIpInterfaceVipAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 22),
    _AlaIpInterfaceVipAddress_Type()
)
alaIpInterfaceVipAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceVipAddress.setStatus("current")


class _AlaIpInterfaceDhcpStatus_Type(Integer32):
    """Custom type alaIpInterfaceDhcpStatus based on Integer32"""
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
        *(("discovery", 1),
          ("active", 2),
          ("timeout", 3))
    )


_AlaIpInterfaceDhcpStatus_Type.__name__ = "Integer32"
_AlaIpInterfaceDhcpStatus_Object = MibTableColumn
alaIpInterfaceDhcpStatus = _AlaIpInterfaceDhcpStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 23),
    _AlaIpInterfaceDhcpStatus_Type()
)
alaIpInterfaceDhcpStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpStatus.setStatus("current")


class _AlaIpInterfaceDhcpIpRelease_Type(Integer32):
    """Custom type alaIpInterfaceDhcpIpRelease based on Integer32"""
    defaultValue = 2

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


_AlaIpInterfaceDhcpIpRelease_Type.__name__ = "Integer32"
_AlaIpInterfaceDhcpIpRelease_Object = MibTableColumn
alaIpInterfaceDhcpIpRelease = _AlaIpInterfaceDhcpIpRelease_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 24),
    _AlaIpInterfaceDhcpIpRelease_Type()
)
alaIpInterfaceDhcpIpRelease.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpIpRelease.setStatus("current")


class _AlaIpInterfaceDhcpIpRenew_Type(Integer32):
    """Custom type alaIpInterfaceDhcpIpRenew based on Integer32"""
    defaultValue = 2

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


_AlaIpInterfaceDhcpIpRenew_Type.__name__ = "Integer32"
_AlaIpInterfaceDhcpIpRenew_Object = MibTableColumn
alaIpInterfaceDhcpIpRenew = _AlaIpInterfaceDhcpIpRenew_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 25),
    _AlaIpInterfaceDhcpIpRenew_Type()
)
alaIpInterfaceDhcpIpRenew.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpIpRenew.setStatus("current")


class _AlaIpInterfaceDhcpOption60String_Type(SnmpAdminString):
    """Custom type alaIpInterfaceDhcpOption60String based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaIpInterfaceDhcpOption60String_Type.__name__ = "SnmpAdminString"
_AlaIpInterfaceDhcpOption60String_Object = MibTableColumn
alaIpInterfaceDhcpOption60String = _AlaIpInterfaceDhcpOption60String_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 26),
    _AlaIpInterfaceDhcpOption60String_Type()
)
alaIpInterfaceDhcpOption60String.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpOption60String.setStatus("current")
_AlaIpInterfaceChassisId_Type = Integer32
_AlaIpInterfaceChassisId_Object = MibTableColumn
alaIpInterfaceChassisId = _AlaIpInterfaceChassisId_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 27),
    _AlaIpInterfaceChassisId_Type()
)
alaIpInterfaceChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceChassisId.setStatus("obsolete")
_AlaIpInterfaceSlot_Type = Integer32
_AlaIpInterfaceSlot_Object = MibTableColumn
alaIpInterfaceSlot = _AlaIpInterfaceSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 28),
    _AlaIpInterfaceSlot_Type()
)
alaIpInterfaceSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceSlot.setStatus("obsolete")
_AlaIpInterfacePort_Type = Integer32
_AlaIpInterfacePort_Object = MibTableColumn
alaIpInterfacePort = _AlaIpInterfacePort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 29),
    _AlaIpInterfacePort_Type()
)
alaIpInterfacePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfacePort.setStatus("obsolete")


class _AlaIpInterfaceTag_Type(Integer32):
    """Custom type alaIpInterfaceTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unbound", 0),
          ("untagged", 1),
          ("tagged", 2))
    )


_AlaIpInterfaceTag_Type.__name__ = "Integer32"
_AlaIpInterfaceTag_Object = MibTableColumn
alaIpInterfaceTag = _AlaIpInterfaceTag_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 30),
    _AlaIpInterfaceTag_Type()
)
alaIpInterfaceTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceTag.setStatus("current")
_AlaIpInterfaceArpCount_Type = Counter32
_AlaIpInterfaceArpCount_Object = MibTableColumn
alaIpInterfaceArpCount = _AlaIpInterfaceArpCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 31),
    _AlaIpInterfaceArpCount_Type()
)
alaIpInterfaceArpCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceArpCount.setStatus("current")
_AlaIpInterfaceArpNiChassis_Type = Integer32
_AlaIpInterfaceArpNiChassis_Object = MibTableColumn
alaIpInterfaceArpNiChassis = _AlaIpInterfaceArpNiChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 32),
    _AlaIpInterfaceArpNiChassis_Type()
)
alaIpInterfaceArpNiChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceArpNiChassis.setStatus("current")
_AlaIpInterfaceArpNiSlot_Type = Integer32
_AlaIpInterfaceArpNiSlot_Object = MibTableColumn
alaIpInterfaceArpNiSlot = _AlaIpInterfaceArpNiSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 33),
    _AlaIpInterfaceArpNiSlot_Type()
)
alaIpInterfaceArpNiSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceArpNiSlot.setStatus("current")
_AlaIpInterfaceArpNiDevice_Type = Integer32
_AlaIpInterfaceArpNiDevice_Object = MibTableColumn
alaIpInterfaceArpNiDevice = _AlaIpInterfaceArpNiDevice_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 34),
    _AlaIpInterfaceArpNiDevice_Type()
)
alaIpInterfaceArpNiDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpInterfaceArpNiDevice.setStatus("current")
_AlaIpInterfacePortIfindex_Type = InterfaceIndexOrZero
_AlaIpInterfacePortIfindex_Object = MibTableColumn
alaIpInterfacePortIfindex = _AlaIpInterfacePortIfindex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 35),
    _AlaIpInterfacePortIfindex_Type()
)
alaIpInterfacePortIfindex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfacePortIfindex.setStatus("current")


class _AlaIpInterfaceDhcpVsiAcceptFilterString_Type(SnmpAdminString):
    """Custom type alaIpInterfaceDhcpVsiAcceptFilterString based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_AlaIpInterfaceDhcpVsiAcceptFilterString_Type.__name__ = "SnmpAdminString"
_AlaIpInterfaceDhcpVsiAcceptFilterString_Object = MibTableColumn
alaIpInterfaceDhcpVsiAcceptFilterString = _AlaIpInterfaceDhcpVsiAcceptFilterString_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 36),
    _AlaIpInterfaceDhcpVsiAcceptFilterString_Type()
)
alaIpInterfaceDhcpVsiAcceptFilterString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceDhcpVsiAcceptFilterString.setStatus("current")


class _AlaIpInterfaceServiceID_Type(Unsigned32):
    """Custom type alaIpInterfaceServiceID based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 32767),
    )


_AlaIpInterfaceServiceID_Type.__name__ = "Unsigned32"
_AlaIpInterfaceServiceID_Object = MibTableColumn
alaIpInterfaceServiceID = _AlaIpInterfaceServiceID_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 14, 1, 37),
    _AlaIpInterfaceServiceID_Type()
)
alaIpInterfaceServiceID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpInterfaceServiceID.setStatus("current")
_AlaIpItfConfigTable_Object = MibTable
alaIpItfConfigTable = _AlaIpItfConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 15)
)
if mibBuilder.loadTexts:
    alaIpItfConfigTable.setStatus("current")
_AlaIpItfConfigEntry_Object = MibTableRow
alaIpItfConfigEntry = _AlaIpItfConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 15, 1)
)
alaIpItfConfigEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaIpItfConfigName"),
)
if mibBuilder.loadTexts:
    alaIpItfConfigEntry.setStatus("current")


class _AlaIpItfConfigName_Type(SnmpAdminString):
    """Custom type alaIpItfConfigName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaIpItfConfigName_Type.__name__ = "SnmpAdminString"
_AlaIpItfConfigName_Object = MibTableColumn
alaIpItfConfigName = _AlaIpItfConfigName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 15, 1, 1),
    _AlaIpItfConfigName_Type()
)
alaIpItfConfigName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpItfConfigName.setStatus("current")
_AlaIpItfConfigIfIndex_Type = InterfaceIndexOrZero
_AlaIpItfConfigIfIndex_Object = MibTableColumn
alaIpItfConfigIfIndex = _AlaIpItfConfigIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 15, 1, 2),
    _AlaIpItfConfigIfIndex_Type()
)
alaIpItfConfigIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpItfConfigIfIndex.setStatus("current")
_AlaIpItfConfigRowStatus_Type = RowStatus
_AlaIpItfConfigRowStatus_Object = MibTableColumn
alaIpItfConfigRowStatus = _AlaIpItfConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 15, 1, 3),
    _AlaIpItfConfigRowStatus_Type()
)
alaIpItfConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpItfConfigRowStatus.setStatus("current")
_AlaIpFtpConfig_ObjectIdentity = ObjectIdentity
alaIpFtpConfig = _AlaIpFtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 16)
)


class _AlaIpFtpAdminStatus_Type(Integer32):
    """Custom type alaIpFtpAdminStatus based on Integer32"""
    defaultValue = 1

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


_AlaIpFtpAdminStatus_Type.__name__ = "Integer32"
_AlaIpFtpAdminStatus_Object = MibScalar
alaIpFtpAdminStatus = _AlaIpFtpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 16, 1),
    _AlaIpFtpAdminStatus_Type()
)
alaIpFtpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpFtpAdminStatus.setStatus("current")


class _AlaIpFtpPort_Type(Integer32):
    """Custom type alaIpFtpPort based on Integer32"""
    defaultValue = 21

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(21, 21),
        ValueRangeConstraint(1024, 65535),
    )


_AlaIpFtpPort_Type.__name__ = "Integer32"
_AlaIpFtpPort_Object = MibScalar
alaIpFtpPort = _AlaIpFtpPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 16, 2),
    _AlaIpFtpPort_Type()
)
alaIpFtpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpFtpPort.setStatus("current")
_AlaIpSshConfig_ObjectIdentity = ObjectIdentity
alaIpSshConfig = _AlaIpSshConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 17)
)


class _AlaIpSshAdminStatus_Type(Integer32):
    """Custom type alaIpSshAdminStatus based on Integer32"""
    defaultValue = 1

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


_AlaIpSshAdminStatus_Type.__name__ = "Integer32"
_AlaIpSshAdminStatus_Object = MibScalar
alaIpSshAdminStatus = _AlaIpSshAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 17, 1),
    _AlaIpSshAdminStatus_Type()
)
alaIpSshAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpSshAdminStatus.setStatus("current")


class _AlaIpSshPort_Type(Integer32):
    """Custom type alaIpSshPort based on Integer32"""
    defaultValue = 22

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(22, 22),
        ValueRangeConstraint(1024, 65535),
    )


_AlaIpSshPort_Type.__name__ = "Integer32"
_AlaIpSshPort_Object = MibScalar
alaIpSshPort = _AlaIpSshPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 17, 2),
    _AlaIpSshPort_Type()
)
alaIpSshPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpSshPort.setStatus("current")


class _AlaIpSshPubKeyEnforceAdminStatus_Type(Integer32):
    """Custom type alaIpSshPubKeyEnforceAdminStatus based on Integer32"""
    defaultValue = 2

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


_AlaIpSshPubKeyEnforceAdminStatus_Type.__name__ = "Integer32"
_AlaIpSshPubKeyEnforceAdminStatus_Object = MibScalar
alaIpSshPubKeyEnforceAdminStatus = _AlaIpSshPubKeyEnforceAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 17, 3),
    _AlaIpSshPubKeyEnforceAdminStatus_Type()
)
alaIpSshPubKeyEnforceAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpSshPubKeyEnforceAdminStatus.setStatus("current")


class _AlaIpSshStrongCiphersAdminStatus_Type(Integer32):
    """Custom type alaIpSshStrongCiphersAdminStatus based on Integer32"""
    defaultValue = 2

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


_AlaIpSshStrongCiphersAdminStatus_Type.__name__ = "Integer32"
_AlaIpSshStrongCiphersAdminStatus_Object = MibScalar
alaIpSshStrongCiphersAdminStatus = _AlaIpSshStrongCiphersAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 17, 4),
    _AlaIpSshStrongCiphersAdminStatus_Type()
)
alaIpSshStrongCiphersAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpSshStrongCiphersAdminStatus.setStatus("current")


class _AlaIpSshStrongHmacsAdminStatus_Type(Integer32):
    """Custom type alaIpSshStrongHmacsAdminStatus based on Integer32"""
    defaultValue = 2

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


_AlaIpSshStrongHmacsAdminStatus_Type.__name__ = "Integer32"
_AlaIpSshStrongHmacsAdminStatus_Object = MibScalar
alaIpSshStrongHmacsAdminStatus = _AlaIpSshStrongHmacsAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 17, 5),
    _AlaIpSshStrongHmacsAdminStatus_Type()
)
alaIpSshStrongHmacsAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpSshStrongHmacsAdminStatus.setStatus("current")
_AlaIpTelnetConfig_ObjectIdentity = ObjectIdentity
alaIpTelnetConfig = _AlaIpTelnetConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 18)
)


class _AlaIpTelnetAdminStatus_Type(Integer32):
    """Custom type alaIpTelnetAdminStatus based on Integer32"""
    defaultValue = 1

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


_AlaIpTelnetAdminStatus_Type.__name__ = "Integer32"
_AlaIpTelnetAdminStatus_Object = MibScalar
alaIpTelnetAdminStatus = _AlaIpTelnetAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 18, 1),
    _AlaIpTelnetAdminStatus_Type()
)
alaIpTelnetAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpTelnetAdminStatus.setStatus("current")


class _AlaIpTelnetPort_Type(Integer32):
    """Custom type alaIpTelnetPort based on Integer32"""
    defaultValue = 23

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(23, 23),
        ValueRangeConstraint(1024, 65535),
    )


_AlaIpTelnetPort_Type.__name__ = "Integer32"
_AlaIpTelnetPort_Object = MibScalar
alaIpTelnetPort = _AlaIpTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 18, 2),
    _AlaIpTelnetPort_Type()
)
alaIpTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpTelnetPort.setStatus("current")
_AlaIpDhcpHostIdentifierObjects_ObjectIdentity = ObjectIdentity
alaIpDhcpHostIdentifierObjects = _AlaIpDhcpHostIdentifierObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19)
)
_AlaIpDhcpServerAddressType_Type = InetAddressType
_AlaIpDhcpServerAddressType_Object = MibScalar
alaIpDhcpServerAddressType = _AlaIpDhcpServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 1),
    _AlaIpDhcpServerAddressType_Type()
)
alaIpDhcpServerAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpServerAddressType.setStatus("current")
_AlaIpDhcpServerAddress_Type = InetAddress
_AlaIpDhcpServerAddress_Object = MibScalar
alaIpDhcpServerAddress = _AlaIpDhcpServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 2),
    _AlaIpDhcpServerAddress_Type()
)
alaIpDhcpServerAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpServerAddress.setStatus("current")
_AlaIpDhcpRouterAddressType_Type = InetAddressType
_AlaIpDhcpRouterAddressType_Object = MibScalar
alaIpDhcpRouterAddressType = _AlaIpDhcpRouterAddressType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 3),
    _AlaIpDhcpRouterAddressType_Type()
)
alaIpDhcpRouterAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpRouterAddressType.setStatus("current")
_AlaIpDhcpRouterAddress_Type = InetAddress
_AlaIpDhcpRouterAddress_Object = MibScalar
alaIpDhcpRouterAddress = _AlaIpDhcpRouterAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 4),
    _AlaIpDhcpRouterAddress_Type()
)
alaIpDhcpRouterAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpRouterAddress.setStatus("current")


class _AlaIpDhcpHostName_Type(SnmpAdminString):
    """Custom type alaIpDhcpHostName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 255),
    )


_AlaIpDhcpHostName_Type.__name__ = "SnmpAdminString"
_AlaIpDhcpHostName_Object = MibScalar
alaIpDhcpHostName = _AlaIpDhcpHostName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 5),
    _AlaIpDhcpHostName_Type()
)
alaIpDhcpHostName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpHostName.setStatus("current")
_AlaIpDhcpClientLeaseObtained_Type = TimeStamp
_AlaIpDhcpClientLeaseObtained_Object = MibScalar
alaIpDhcpClientLeaseObtained = _AlaIpDhcpClientLeaseObtained_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 6),
    _AlaIpDhcpClientLeaseObtained_Type()
)
alaIpDhcpClientLeaseObtained.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpClientLeaseObtained.setStatus("current")
_AlaIpDhcpClientLeaseExpires_Type = TimeStamp
_AlaIpDhcpClientLeaseExpires_Object = MibScalar
alaIpDhcpClientLeaseExpires = _AlaIpDhcpClientLeaseExpires_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 19, 7),
    _AlaIpDhcpClientLeaseExpires_Type()
)
alaIpDhcpClientLeaseExpires.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpDhcpClientLeaseExpires.setStatus("current")
_AlaIpNtpConfig_ObjectIdentity = ObjectIdentity
alaIpNtpConfig = _AlaIpNtpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 20)
)


class _AlaIpNtpVrfName_Type(SnmpAdminString):
    """Custom type alaIpNtpVrfName based on SnmpAdminString"""
    defaultValue = OctetString("default")

    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 20),
    )


_AlaIpNtpVrfName_Type.__name__ = "SnmpAdminString"
_AlaIpNtpVrfName_Object = MibScalar
alaIpNtpVrfName = _AlaIpNtpVrfName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 20, 1),
    _AlaIpNtpVrfName_Type()
)
alaIpNtpVrfName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    alaIpNtpVrfName.setStatus("current")
_AlaDistArpNiTable_Object = MibTable
alaDistArpNiTable = _AlaDistArpNiTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 21)
)
if mibBuilder.loadTexts:
    alaDistArpNiTable.setStatus("current")
_AlaDistArpNiEntry_Object = MibTableRow
alaDistArpNiEntry = _AlaDistArpNiEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 21, 1)
)
alaDistArpNiEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaDistArpNiChassis"),
    (0, "ALCATEL-ENT1-IP-MIB", "alaDistArpNiSlot"),
    (0, "ALCATEL-ENT1-IP-MIB", "alaDistArpNiDevice"),
)
if mibBuilder.loadTexts:
    alaDistArpNiEntry.setStatus("current")
_AlaDistArpNiChassis_Type = Unsigned32
_AlaDistArpNiChassis_Object = MibTableColumn
alaDistArpNiChassis = _AlaDistArpNiChassis_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 21, 1, 1),
    _AlaDistArpNiChassis_Type()
)
alaDistArpNiChassis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDistArpNiChassis.setStatus("current")
_AlaDistArpNiSlot_Type = Unsigned32
_AlaDistArpNiSlot_Object = MibTableColumn
alaDistArpNiSlot = _AlaDistArpNiSlot_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 21, 1, 2),
    _AlaDistArpNiSlot_Type()
)
alaDistArpNiSlot.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDistArpNiSlot.setStatus("current")
_AlaDistArpNiDevice_Type = Unsigned32
_AlaDistArpNiDevice_Object = MibTableColumn
alaDistArpNiDevice = _AlaDistArpNiDevice_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 21, 1, 3),
    _AlaDistArpNiDevice_Type()
)
alaDistArpNiDevice.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDistArpNiDevice.setStatus("current")
_AlaDistArpNiCount_Type = Counter32
_AlaDistArpNiCount_Object = MibTableColumn
alaDistArpNiCount = _AlaDistArpNiCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 21, 1, 4),
    _AlaDistArpNiCount_Type()
)
alaDistArpNiCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDistArpNiCount.setStatus("current")
_AlaDistArpNiMaxCount_Type = Counter32
_AlaDistArpNiMaxCount_Object = MibTableColumn
alaDistArpNiMaxCount = _AlaDistArpNiMaxCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 21, 1, 5),
    _AlaDistArpNiMaxCount_Type()
)
alaDistArpNiMaxCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDistArpNiMaxCount.setStatus("current")
_AlaIpServiceSourceIpTable_Object = MibTable
alaIpServiceSourceIpTable = _AlaIpServiceSourceIpTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 22)
)
if mibBuilder.loadTexts:
    alaIpServiceSourceIpTable.setStatus("current")
_AlaIpServiceSourceIpEntry_Object = MibTableRow
alaIpServiceSourceIpEntry = _AlaIpServiceSourceIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 22, 1)
)
alaIpServiceSourceIpEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaIpServiceSourceIpAppIndex"),
)
if mibBuilder.loadTexts:
    alaIpServiceSourceIpEntry.setStatus("current")
_AlaIpServiceSourceIpAppIndex_Type = AlaIpServiceSourceIpAppIndex
_AlaIpServiceSourceIpAppIndex_Object = MibTableColumn
alaIpServiceSourceIpAppIndex = _AlaIpServiceSourceIpAppIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 22, 1, 1),
    _AlaIpServiceSourceIpAppIndex_Type()
)
alaIpServiceSourceIpAppIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpServiceSourceIpAppIndex.setStatus("current")


class _AlaIpServiceSourceIpName_Type(SnmpAdminString):
    """Custom type alaIpServiceSourceIpName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AlaIpServiceSourceIpName_Type.__name__ = "SnmpAdminString"
_AlaIpServiceSourceIpName_Object = MibTableColumn
alaIpServiceSourceIpName = _AlaIpServiceSourceIpName_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 22, 1, 2),
    _AlaIpServiceSourceIpName_Type()
)
alaIpServiceSourceIpName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpServiceSourceIpName.setStatus("current")
_AlaIpServiceSourceIpRowStatus_Type = RowStatus
_AlaIpServiceSourceIpRowStatus_Object = MibTableColumn
alaIpServiceSourceIpRowStatus = _AlaIpServiceSourceIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 22, 1, 3),
    _AlaIpServiceSourceIpRowStatus_Type()
)
alaIpServiceSourceIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    alaIpServiceSourceIpRowStatus.setStatus("current")
_AlaDistArpItfTable_Object = MibTable
alaDistArpItfTable = _AlaDistArpItfTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 23)
)
if mibBuilder.loadTexts:
    alaDistArpItfTable.setStatus("current")
_AlaDistArpItfEntry_Object = MibTableRow
alaDistArpItfEntry = _AlaDistArpItfEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 23, 1)
)
alaDistArpItfEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaDistArpNiChassis"),
    (0, "ALCATEL-ENT1-IP-MIB", "alaDistArpNiSlot"),
    (0, "ALCATEL-ENT1-IP-MIB", "alaDistArpNiDevice"),
    (0, "ALCATEL-ENT1-IP-MIB", "alaDistArpItfIfIndex"),
)
if mibBuilder.loadTexts:
    alaDistArpItfEntry.setStatus("current")
_AlaDistArpItfIfIndex_Type = InterfaceIndexOrZero
_AlaDistArpItfIfIndex_Object = MibTableColumn
alaDistArpItfIfIndex = _AlaDistArpItfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 23, 1, 1),
    _AlaDistArpItfIfIndex_Type()
)
alaDistArpItfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDistArpItfIfIndex.setStatus("current")
_AlaDistArpItfCount_Type = Counter32
_AlaDistArpItfCount_Object = MibTableColumn
alaDistArpItfCount = _AlaDistArpItfCount_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 23, 1, 2),
    _AlaDistArpItfCount_Type()
)
alaDistArpItfCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaDistArpItfCount.setStatus("current")
_AlaIpNetToMediaDpaTable_Object = MibTable
alaIpNetToMediaDpaTable = _AlaIpNetToMediaDpaTable_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 24)
)
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaTable.setStatus("current")
_AlaIpNetToMediaDpaEntry_Object = MibTableRow
alaIpNetToMediaDpaEntry = _AlaIpNetToMediaDpaEntry_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 24, 1)
)
alaIpNetToMediaDpaEntry.setIndexNames(
    (0, "ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaDpaVlan"),
)
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaEntry.setStatus("current")
_AlaIpNetToMediaDpaVlan_Type = Unsigned32
_AlaIpNetToMediaDpaVlan_Object = MibTableColumn
alaIpNetToMediaDpaVlan = _AlaIpNetToMediaDpaVlan_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 24, 1, 1),
    _AlaIpNetToMediaDpaVlan_Type()
)
alaIpNetToMediaDpaVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaVlan.setStatus("current")
_AlaIpNetToMediaDpaPhysAddress_Type = PhysAddress
_AlaIpNetToMediaDpaPhysAddress_Object = MibTableColumn
alaIpNetToMediaDpaPhysAddress = _AlaIpNetToMediaDpaPhysAddress_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 24, 1, 2),
    _AlaIpNetToMediaDpaPhysAddress_Type()
)
alaIpNetToMediaDpaPhysAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaPhysAddress.setStatus("current")


class _AlaIpNetToMediaDpaIpType_Type(InetAddressType):
    """Custom type alaIpNetToMediaDpaIpType based on InetAddressType"""
    subtypeSpec = InetAddressType.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1),
    )


_AlaIpNetToMediaDpaIpType_Type.__name__ = "InetAddressType"
_AlaIpNetToMediaDpaIpType_Object = MibTableColumn
alaIpNetToMediaDpaIpType = _AlaIpNetToMediaDpaIpType_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 24, 1, 3),
    _AlaIpNetToMediaDpaIpType_Type()
)
alaIpNetToMediaDpaIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaIpType.setStatus("current")
_AlaIpNetToMediaDpaIp_Type = InetAddress
_AlaIpNetToMediaDpaIp_Object = MibTableColumn
alaIpNetToMediaDpaIp = _AlaIpNetToMediaDpaIp_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 24, 1, 4),
    _AlaIpNetToMediaDpaIp_Type()
)
alaIpNetToMediaDpaIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaIp.setStatus("current")
_AlaIpNetToMediaDpaIfIndex_Type = InterfaceIndexOrZero
_AlaIpNetToMediaDpaIfIndex_Object = MibTableColumn
alaIpNetToMediaDpaIfIndex = _AlaIpNetToMediaDpaIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 1, 24, 1, 5),
    _AlaIpNetToMediaDpaIfIndex_Type()
)
alaIpNetToMediaDpaIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    alaIpNetToMediaDpaIfIndex.setStatus("current")
_AlcatelIND1IPMIBConformance_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBConformance = _AlcatelIND1IPMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2)
)
_AlcatelIND1IPMIBCompliances_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBCompliances = _AlcatelIND1IPMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 1)
)
_AlcatelIND1IPMIBGroups_ObjectIdentity = ObjectIdentity
alcatelIND1IPMIBGroups = _AlcatelIND1IPMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2)
)
ipNetToMediaEntry.registerAugmentions(
    ("ALCATEL-ENT1-IP-MIB",
     "ipNetToMediaAugEntry")
)
ipNetToMediaAugEntry.setIndexNames(*ipNetToMediaEntry.getIndexNames())
ipCidrRouteEntry.registerAugmentions(
    ("ALCATEL-ENT1-IP-MIB",
     "ipCidrRouteAugEntry")
)
ipCidrRouteAugEntry.setIndexNames(*ipCidrRouteEntry.getIndexNames())

# Managed Objects groups

alaIpConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 1)
)
alaIpConfigGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpClearArpCache"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpDirectedBroadcast"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpClearArpFilter"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpDistributedArp"))
)
if mibBuilder.loadTexts:
    alaIpConfigGroup.setStatus("current")

alaIpNetToMediaGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 2)
)
alaIpNetToMediaGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaPhysAddress"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaProxy"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaVrrp"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaAuth"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaName"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaStaticIntfRt"))
)
if mibBuilder.loadTexts:
    alaIpNetToMediaGroup.setStatus("current")

alaDoSGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 3)
)
alaDoSGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDoSType"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSDetected"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSIp"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSMac"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSSlot"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSPort"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSStatus"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSChassisId"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSPortIfindex"))
)
if mibBuilder.loadTexts:
    alaDoSGroup.setStatus("current")

alaPortScanGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 4)
)
alaPortScanGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDoSPortScanClosePortPenalty"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSPortScanTcpOpenPortPenalty"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSPortScanUdpOpenPortPenalty"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSPortScanTotalPenalty"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSPortScanThreshold"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSPortScanDecay"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSTrapCntl"))
)
if mibBuilder.loadTexts:
    alaPortScanGroup.setStatus("current")

alaArpPingGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 5)
)
alaArpPingGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDoSARPRate"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSPingRate"))
)
if mibBuilder.loadTexts:
    alaArpPingGroup.setStatus("current")

alaArpPoisonGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 6)
)
alaArpPoisonGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDoSArpPoisonDetected"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSArpPoisonRowStatus"))
)
if mibBuilder.loadTexts:
    alaArpPoisonGroup.setStatus("current")

alaIpNetToMediaAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 7)
)
alaIpNetToMediaAugGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "ipNetToMediaSlot"),
        ("ALCATEL-ENT1-IP-MIB", "ipNetToMediaPort"),
        ("ALCATEL-ENT1-IP-MIB", "ipNetToMediaName"),
        ("ALCATEL-ENT1-IP-MIB", "ipNetToMediaChassisId"),
        ("ALCATEL-ENT1-IP-MIB", "ipNetToMediaPortIfindex"),
        ("ALCATEL-ENT1-IP-MIB", "ipNetToMediaSubId"),
        ("ALCATEL-ENT1-IP-MIB", "ipNetToMediaSubType"))
)
if mibBuilder.loadTexts:
    alaIpNetToMediaAugGroup.setStatus("current")

alaPktDropGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 8)
)
alaPktDropGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "pktDropType"),
        ("ALCATEL-ENT1-IP-MIB", "pktDropIfIndex"),
        ("ALCATEL-ENT1-IP-MIB", "pktDropCount"),
        ("ALCATEL-ENT1-IP-MIB", "pktDropFrag"))
)
if mibBuilder.loadTexts:
    alaPktDropGroup.setStatus("current")

alaIpCidrAugGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 9)
)
alaIpCidrAugGroup.setObjects(
    ("ALCATEL-ENT1-IP-MIB", "ipCidrRouteScope")
)
if mibBuilder.loadTexts:
    alaIpCidrAugGroup.setStatus("current")

alaIcmpCtrlGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 10)
)
alaIcmpCtrlGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIcmpCtrlType"),
        ("ALCATEL-ENT1-IP-MIB", "alaIcmpCtrlCode"),
        ("ALCATEL-ENT1-IP-MIB", "alaIcmpCtrlStatus"),
        ("ALCATEL-ENT1-IP-MIB", "alaIcmpCtrlPktGap"),
        ("ALCATEL-ENT1-IP-MIB", "alaIcmpAllMsgStatus"))
)
if mibBuilder.loadTexts:
    alaIcmpCtrlGroup.setStatus("current")

alaIpRouteSumGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 11)
)
alaIpRouteSumGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpRouteProtocol"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpRouteCount"))
)
if mibBuilder.loadTexts:
    alaIpRouteSumGroup.setStatus("current")

alaIpArpFilterGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 12)
)
alaIpArpFilterGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpArpFilterMode"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpArpFilterRowStatus"))
)
if mibBuilder.loadTexts:
    alaIpArpFilterGroup.setStatus("current")

alaIpServiceTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 13)
)
alaIpServiceTypeGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpServiceType"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpServicePort"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpServiceStatus"))
)
if mibBuilder.loadTexts:
    alaIpServiceTypeGroup.setStatus("current")

alaIpPortServiceTypeGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 14)
)
alaIpPortServiceTypeGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpPortServicePort"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpPortServiceStatus"))
)
if mibBuilder.loadTexts:
    alaIpPortServiceTypeGroup.setStatus("current")

alaIpInterfaceGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 15)
)
alaIpInterfaceGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceName"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceAddress"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceMask"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceAdminState"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceDeviceType"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceVlanID"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceIpForward"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceEncap"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceMtu"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceLocalProxyArp"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfacePrimCfg"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceOperState"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceOperReason"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceRouterMac"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceBcastAddr"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfacePrimAct"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceRemoteAddr"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceTunnelSrcAddressType"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceTunnelSrc"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceTunnelDstAddressType"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceTunnelDst"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceVipAddress"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceDhcpStatus"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceDhcpIpRelease"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceDhcpIpRenew"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceDhcpOption60String"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceChassisId"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceSlot"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfacePort"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceTag"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceArpCount"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceArpNiChassis"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceArpNiSlot"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceArpNiDevice"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfacePortIfindex"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceDhcpVsiAcceptFilterString"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceServiceID"))
)
if mibBuilder.loadTexts:
    alaIpInterfaceGroup.setStatus("current")

alaIpItfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 16)
)
alaIpItfGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpItfConfigName"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpItfConfigIfIndex"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpItfConfigRowStatus"))
)
if mibBuilder.loadTexts:
    alaIpItfGroup.setStatus("current")

alaIpFtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 17)
)
alaIpFtpGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpFtpAdminStatus"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpFtpPort"))
)
if mibBuilder.loadTexts:
    alaIpFtpGroup.setStatus("current")

alaIpSshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 18)
)
alaIpSshGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpSshAdminStatus"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpSshPort"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpSshPubKeyEnforceAdminStatus"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpSshStrongCiphersAdminStatus"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpSshStrongHmacsAdminStatus"))
)
if mibBuilder.loadTexts:
    alaIpSshGroup.setStatus("current")

alaIpTelnetGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 19)
)
alaIpTelnetGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpTelnetAdminStatus"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpTelnetPort"))
)
if mibBuilder.loadTexts:
    alaIpTelnetGroup.setStatus("current")

alaIpDhcpHostIdentifierGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 21)
)
alaIpDhcpHostIdentifierGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpDhcpServerAddressType"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpDhcpServerAddress"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpDhcpRouterAddressType"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpDhcpRouterAddress"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpDhcpHostName"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpDhcpClientLeaseObtained"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpDhcpClientLeaseExpires"))
)
if mibBuilder.loadTexts:
    alaIpDhcpHostIdentifierGroup.setStatus("current")

alaIpNtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 22)
)
alaIpNtpGroup.setObjects(
    ("ALCATEL-ENT1-IP-MIB", "alaIpNtpVrfName")
)
if mibBuilder.loadTexts:
    alaIpNtpGroup.setStatus("current")

alaDistArpNiGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 23)
)
alaDistArpNiGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDistArpNiChassis"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpNiSlot"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpNiDevice"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpNiMaxCount"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpNiCount"))
)
if mibBuilder.loadTexts:
    alaDistArpNiGroup.setStatus("current")

alaIpServiceSourceIpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 24)
)
alaIpServiceSourceIpGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpServiceSourceIpName"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpServiceSourceIpRowStatus"))
)
if mibBuilder.loadTexts:
    alaIpServiceSourceIpGroup.setStatus("current")

alaDistArpItfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 25)
)
alaDistArpItfGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDistArpItfIfIndex"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpItfCount"))
)
if mibBuilder.loadTexts:
    alaDistArpItfGroup.setStatus("current")

alaIpNetToMediaDpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 26)
)
alaIpNetToMediaDpGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaDpaPhysAddress"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaDpaIpType"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaDpaIp"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaDpaIfIndex"))
)
if mibBuilder.loadTexts:
    alaIpNetToMediaDpGroup.setStatus("current")

alaAntiSpoofGlobalGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 27)
)
alaAntiSpoofGlobalGroup.setObjects(
    ("ALCATEL-ENT1-IP-MIB", "alaDoSAntiSpoofGlobalCountReset")
)
if mibBuilder.loadTexts:
    alaAntiSpoofGlobalGroup.setStatus("current")

alaAntiSpoofGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 28)
)
alaAntiSpoofGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDoSAntiSpoofStatus"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSAntiSpoofMacAddress"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSAntiSpoofIfIndex"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSAntiSpoofVlan"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSAntiSpoofCount"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSAntiSpoofCountReset"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSAntiSpoofRowStatus"))
)
if mibBuilder.loadTexts:
    alaAntiSpoofGroup.setStatus("current")


# Notification objects

alaDoSTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 0, 1)
)
alaDoSTrap.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDoSType"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSDetected"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSIp"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSMac"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSSlot"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSPort"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSChassisId"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSPortIfindex"))
)
if mibBuilder.loadTexts:
    alaDoSTrap.setStatus(
        "current"
    )

pktDrop = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 0, 2)
)
pktDrop.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "pktDropType"),
        ("ALCATEL-ENT1-IP-MIB", "pktDropIfIndex"),
        ("ALCATEL-ENT1-IP-MIB", "pktDropCount"),
        ("ALCATEL-ENT1-IP-MIB", "pktDropFrag"))
)
if mibBuilder.loadTexts:
    pktDrop.setStatus(
        "current"
    )

alaDistArpItfChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 0, 3)
)
alaDistArpItfChange.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDistArpItfIfIndex"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpNiChassis"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpNiSlot"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpNiDevice"))
)
if mibBuilder.loadTexts:
    alaDistArpItfChange.setStatus(
        "current"
    )

alaDistArpNiThreshold = NotificationType(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 0, 4)
)
alaDistArpNiThreshold.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDistArpNiChassis"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpNiSlot"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpNiDevice"))
)
if mibBuilder.loadTexts:
    alaDistArpNiThreshold.setStatus(
        "current"
    )


# Notifications groups

alaIpNotificationGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 2, 20)
)
alaIpNotificationGroup.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaDoSTrap"),
        ("ALCATEL-ENT1-IP-MIB", "pktDrop"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpItfChange"),
        ("ALCATEL-ENT1-IP-MIB", "alaDistArpNiThreshold"))
)
if mibBuilder.loadTexts:
    alaIpNotificationGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

alaIpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6486, 801, 1, 2, 1, 23, 1, 2, 1, 1)
)
alaIpCompliance.setObjects(
      *(("ALCATEL-ENT1-IP-MIB", "alaIpConfigGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaDoSGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaPortScanGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaArpPingGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaArpPoisonGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaAugGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaPktDropGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpCidrAugGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIcmpCtrlGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpRouteSumGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpArpFilterGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpServiceTypeGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpPortServiceTypeGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpInterfaceGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpItfGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNotificationGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpDhcpHostIdentifierGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpServiceSourceIpGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaIpNetToMediaDpGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaAntiSpoofGlobalGroup"),
        ("ALCATEL-ENT1-IP-MIB", "alaAntiSpoofGroup"))
)
if mibBuilder.loadTexts:
    alaIpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ALCATEL-ENT1-IP-MIB",
    **{"AlaIpServiceSourceIpAppIndex": AlaIpServiceSourceIpAppIndex,
       "alcatelIND1IPMIB": alcatelIND1IPMIB,
       "alcatelIND1IPMIBNotifications": alcatelIND1IPMIBNotifications,
       "alaDoSTrap": alaDoSTrap,
       "pktDrop": pktDrop,
       "alaDistArpItfChange": alaDistArpItfChange,
       "alaDistArpNiThreshold": alaDistArpNiThreshold,
       "alcatelIND1IPMIBObjects": alcatelIND1IPMIBObjects,
       "alaIpConfig": alaIpConfig,
       "alaIpClearArpCache": alaIpClearArpCache,
       "alaIpDirectedBroadcast": alaIpDirectedBroadcast,
       "alaIpClearArpFilter": alaIpClearArpFilter,
       "alaIpDistributedArp": alaIpDistributedArp,
       "alaIpNetToMediaTable": alaIpNetToMediaTable,
       "alaIpNetToMediaEntry": alaIpNetToMediaEntry,
       "alaIpNetToMediaPhysAddress": alaIpNetToMediaPhysAddress,
       "alaIpNetToMediaProxy": alaIpNetToMediaProxy,
       "alaIpNetToMediaVrrp": alaIpNetToMediaVrrp,
       "alaIpNetToMediaAuth": alaIpNetToMediaAuth,
       "alaIpNetToMediaName": alaIpNetToMediaName,
       "alaIpNetToMediaStaticIntfRt": alaIpNetToMediaStaticIntfRt,
       "alaDoSConfig": alaDoSConfig,
       "alaDoSTable": alaDoSTable,
       "alaDoSEntry": alaDoSEntry,
       "alaDoSType": alaDoSType,
       "alaDoSDetected": alaDoSDetected,
       "alaDoSIp": alaDoSIp,
       "alaDoSMac": alaDoSMac,
       "alaDoSSlot": alaDoSSlot,
       "alaDoSPort": alaDoSPort,
       "alaDoSStatus": alaDoSStatus,
       "alaDoSChassisId": alaDoSChassisId,
       "alaDoSPortIfindex": alaDoSPortIfindex,
       "alaDoSPortScanClosePortPenalty": alaDoSPortScanClosePortPenalty,
       "alaDoSPortScanTcpOpenPortPenalty": alaDoSPortScanTcpOpenPortPenalty,
       "alaDoSPortScanUdpOpenPortPenalty": alaDoSPortScanUdpOpenPortPenalty,
       "alaDoSPortScanTotalPenalty": alaDoSPortScanTotalPenalty,
       "alaDoSPortScanThreshold": alaDoSPortScanThreshold,
       "alaDoSPortScanDecay": alaDoSPortScanDecay,
       "alaDoSTrapCntl": alaDoSTrapCntl,
       "alaDoSARPRate": alaDoSARPRate,
       "alaDoSPingRate": alaDoSPingRate,
       "alaDoSArpPoisonTable": alaDoSArpPoisonTable,
       "alaDoSArpPoisonEntry": alaDoSArpPoisonEntry,
       "alaDoSArpPoisonIpAddr": alaDoSArpPoisonIpAddr,
       "alaDoSArpPoisonDetected": alaDoSArpPoisonDetected,
       "alaDoSArpPoisonRowStatus": alaDoSArpPoisonRowStatus,
       "alaDoSAntiSpoofGlobalCountReset": alaDoSAntiSpoofGlobalCountReset,
       "alaDoSAntiSpoofTable": alaDoSAntiSpoofTable,
       "alaDoSAntiSpoofEntry": alaDoSAntiSpoofEntry,
       "alaDoSAntiSpoofIPAddressType": alaDoSAntiSpoofIPAddressType,
       "alaDoSAntiSpoofIPAddress": alaDoSAntiSpoofIPAddress,
       "alaDoSAntiSpoofStatus": alaDoSAntiSpoofStatus,
       "alaDoSAntiSpoofMacAddress": alaDoSAntiSpoofMacAddress,
       "alaDoSAntiSpoofIfIndex": alaDoSAntiSpoofIfIndex,
       "alaDoSAntiSpoofVlan": alaDoSAntiSpoofVlan,
       "alaDoSAntiSpoofCount": alaDoSAntiSpoofCount,
       "alaDoSAntiSpoofCountReset": alaDoSAntiSpoofCountReset,
       "alaDoSAntiSpoofRowStatus": alaDoSAntiSpoofRowStatus,
       "ipNetToMediaAugTable": ipNetToMediaAugTable,
       "ipNetToMediaAugEntry": ipNetToMediaAugEntry,
       "ipNetToMediaSlot": ipNetToMediaSlot,
       "ipNetToMediaPort": ipNetToMediaPort,
       "ipNetToMediaName": ipNetToMediaName,
       "ipNetToMediaChassisId": ipNetToMediaChassisId,
       "ipNetToMediaPortIfindex": ipNetToMediaPortIfindex,
       "ipNetToMediaSubType": ipNetToMediaSubType,
       "ipNetToMediaSubId": ipNetToMediaSubId,
       "trafficEventTrapObjs": trafficEventTrapObjs,
       "pktDropType": pktDropType,
       "pktDropIfIndex": pktDropIfIndex,
       "pktDropCount": pktDropCount,
       "pktDropFrag": pktDropFrag,
       "ipCidrRouteAugTable": ipCidrRouteAugTable,
       "ipCidrRouteAugEntry": ipCidrRouteAugEntry,
       "ipCidrRouteScope": ipCidrRouteScope,
       "alaIcmpCtrlTable": alaIcmpCtrlTable,
       "alaIcmpCtrlEntry": alaIcmpCtrlEntry,
       "alaIcmpCtrlType": alaIcmpCtrlType,
       "alaIcmpCtrlCode": alaIcmpCtrlCode,
       "alaIcmpCtrlStatus": alaIcmpCtrlStatus,
       "alaIcmpCtrlPktGap": alaIcmpCtrlPktGap,
       "alaIpRouteSumTable": alaIpRouteSumTable,
       "alaIpRouteSumEntry": alaIpRouteSumEntry,
       "alaIpRouteProtocol": alaIpRouteProtocol,
       "alaIpRouteCount": alaIpRouteCount,
       "alaIcmpCtrl": alaIcmpCtrl,
       "alaIcmpAllMsgStatus": alaIcmpAllMsgStatus,
       "alaIpArpFilterTable": alaIpArpFilterTable,
       "alaIpArpFilterEntry": alaIpArpFilterEntry,
       "alaIpArpFilterIpAddr": alaIpArpFilterIpAddr,
       "alaIpArpFilterIpMask": alaIpArpFilterIpMask,
       "alaIpArpFilterVlan": alaIpArpFilterVlan,
       "alaIpArpFilterType": alaIpArpFilterType,
       "alaIpArpFilterMode": alaIpArpFilterMode,
       "alaIpArpFilterRowStatus": alaIpArpFilterRowStatus,
       "alaIpServiceTable": alaIpServiceTable,
       "alaIpServiceEntry": alaIpServiceEntry,
       "alaIpServiceType": alaIpServiceType,
       "alaIpServicePort": alaIpServicePort,
       "alaIpServiceStatus": alaIpServiceStatus,
       "alaIpPortServiceTable": alaIpPortServiceTable,
       "alaIpPortServiceEntry": alaIpPortServiceEntry,
       "alaIpPortServicePort": alaIpPortServicePort,
       "alaIpPortServiceStatus": alaIpPortServiceStatus,
       "alaIpInterfaceTable": alaIpInterfaceTable,
       "alaIpInterfaceEntry": alaIpInterfaceEntry,
       "alaIpInterfaceName": alaIpInterfaceName,
       "alaIpInterfaceAddress": alaIpInterfaceAddress,
       "alaIpInterfaceMask": alaIpInterfaceMask,
       "alaIpInterfaceAdminState": alaIpInterfaceAdminState,
       "alaIpInterfaceDeviceType": alaIpInterfaceDeviceType,
       "alaIpInterfaceVlanID": alaIpInterfaceVlanID,
       "alaIpInterfaceIpForward": alaIpInterfaceIpForward,
       "alaIpInterfaceEncap": alaIpInterfaceEncap,
       "alaIpInterfaceMtu": alaIpInterfaceMtu,
       "alaIpInterfaceLocalProxyArp": alaIpInterfaceLocalProxyArp,
       "alaIpInterfacePrimCfg": alaIpInterfacePrimCfg,
       "alaIpInterfaceOperState": alaIpInterfaceOperState,
       "alaIpInterfaceOperReason": alaIpInterfaceOperReason,
       "alaIpInterfaceRouterMac": alaIpInterfaceRouterMac,
       "alaIpInterfaceBcastAddr": alaIpInterfaceBcastAddr,
       "alaIpInterfacePrimAct": alaIpInterfacePrimAct,
       "alaIpInterfaceRemoteAddr": alaIpInterfaceRemoteAddr,
       "alaIpInterfaceTunnelSrcAddressType": alaIpInterfaceTunnelSrcAddressType,
       "alaIpInterfaceTunnelSrc": alaIpInterfaceTunnelSrc,
       "alaIpInterfaceTunnelDstAddressType": alaIpInterfaceTunnelDstAddressType,
       "alaIpInterfaceTunnelDst": alaIpInterfaceTunnelDst,
       "alaIpInterfaceVipAddress": alaIpInterfaceVipAddress,
       "alaIpInterfaceDhcpStatus": alaIpInterfaceDhcpStatus,
       "alaIpInterfaceDhcpIpRelease": alaIpInterfaceDhcpIpRelease,
       "alaIpInterfaceDhcpIpRenew": alaIpInterfaceDhcpIpRenew,
       "alaIpInterfaceDhcpOption60String": alaIpInterfaceDhcpOption60String,
       "alaIpInterfaceChassisId": alaIpInterfaceChassisId,
       "alaIpInterfaceSlot": alaIpInterfaceSlot,
       "alaIpInterfacePort": alaIpInterfacePort,
       "alaIpInterfaceTag": alaIpInterfaceTag,
       "alaIpInterfaceArpCount": alaIpInterfaceArpCount,
       "alaIpInterfaceArpNiChassis": alaIpInterfaceArpNiChassis,
       "alaIpInterfaceArpNiSlot": alaIpInterfaceArpNiSlot,
       "alaIpInterfaceArpNiDevice": alaIpInterfaceArpNiDevice,
       "alaIpInterfacePortIfindex": alaIpInterfacePortIfindex,
       "alaIpInterfaceDhcpVsiAcceptFilterString": alaIpInterfaceDhcpVsiAcceptFilterString,
       "alaIpInterfaceServiceID": alaIpInterfaceServiceID,
       "alaIpItfConfigTable": alaIpItfConfigTable,
       "alaIpItfConfigEntry": alaIpItfConfigEntry,
       "alaIpItfConfigName": alaIpItfConfigName,
       "alaIpItfConfigIfIndex": alaIpItfConfigIfIndex,
       "alaIpItfConfigRowStatus": alaIpItfConfigRowStatus,
       "alaIpFtpConfig": alaIpFtpConfig,
       "alaIpFtpAdminStatus": alaIpFtpAdminStatus,
       "alaIpFtpPort": alaIpFtpPort,
       "alaIpSshConfig": alaIpSshConfig,
       "alaIpSshAdminStatus": alaIpSshAdminStatus,
       "alaIpSshPort": alaIpSshPort,
       "alaIpSshPubKeyEnforceAdminStatus": alaIpSshPubKeyEnforceAdminStatus,
       "alaIpSshStrongCiphersAdminStatus": alaIpSshStrongCiphersAdminStatus,
       "alaIpSshStrongHmacsAdminStatus": alaIpSshStrongHmacsAdminStatus,
       "alaIpTelnetConfig": alaIpTelnetConfig,
       "alaIpTelnetAdminStatus": alaIpTelnetAdminStatus,
       "alaIpTelnetPort": alaIpTelnetPort,
       "alaIpDhcpHostIdentifierObjects": alaIpDhcpHostIdentifierObjects,
       "alaIpDhcpServerAddressType": alaIpDhcpServerAddressType,
       "alaIpDhcpServerAddress": alaIpDhcpServerAddress,
       "alaIpDhcpRouterAddressType": alaIpDhcpRouterAddressType,
       "alaIpDhcpRouterAddress": alaIpDhcpRouterAddress,
       "alaIpDhcpHostName": alaIpDhcpHostName,
       "alaIpDhcpClientLeaseObtained": alaIpDhcpClientLeaseObtained,
       "alaIpDhcpClientLeaseExpires": alaIpDhcpClientLeaseExpires,
       "alaIpNtpConfig": alaIpNtpConfig,
       "alaIpNtpVrfName": alaIpNtpVrfName,
       "alaDistArpNiTable": alaDistArpNiTable,
       "alaDistArpNiEntry": alaDistArpNiEntry,
       "alaDistArpNiChassis": alaDistArpNiChassis,
       "alaDistArpNiSlot": alaDistArpNiSlot,
       "alaDistArpNiDevice": alaDistArpNiDevice,
       "alaDistArpNiCount": alaDistArpNiCount,
       "alaDistArpNiMaxCount": alaDistArpNiMaxCount,
       "alaIpServiceSourceIpTable": alaIpServiceSourceIpTable,
       "alaIpServiceSourceIpEntry": alaIpServiceSourceIpEntry,
       "alaIpServiceSourceIpAppIndex": alaIpServiceSourceIpAppIndex,
       "alaIpServiceSourceIpName": alaIpServiceSourceIpName,
       "alaIpServiceSourceIpRowStatus": alaIpServiceSourceIpRowStatus,
       "alaDistArpItfTable": alaDistArpItfTable,
       "alaDistArpItfEntry": alaDistArpItfEntry,
       "alaDistArpItfIfIndex": alaDistArpItfIfIndex,
       "alaDistArpItfCount": alaDistArpItfCount,
       "alaIpNetToMediaDpaTable": alaIpNetToMediaDpaTable,
       "alaIpNetToMediaDpaEntry": alaIpNetToMediaDpaEntry,
       "alaIpNetToMediaDpaVlan": alaIpNetToMediaDpaVlan,
       "alaIpNetToMediaDpaPhysAddress": alaIpNetToMediaDpaPhysAddress,
       "alaIpNetToMediaDpaIpType": alaIpNetToMediaDpaIpType,
       "alaIpNetToMediaDpaIp": alaIpNetToMediaDpaIp,
       "alaIpNetToMediaDpaIfIndex": alaIpNetToMediaDpaIfIndex,
       "alcatelIND1IPMIBConformance": alcatelIND1IPMIBConformance,
       "alcatelIND1IPMIBCompliances": alcatelIND1IPMIBCompliances,
       "alaIpCompliance": alaIpCompliance,
       "alcatelIND1IPMIBGroups": alcatelIND1IPMIBGroups,
       "alaIpConfigGroup": alaIpConfigGroup,
       "alaIpNetToMediaGroup": alaIpNetToMediaGroup,
       "alaDoSGroup": alaDoSGroup,
       "alaPortScanGroup": alaPortScanGroup,
       "alaArpPingGroup": alaArpPingGroup,
       "alaArpPoisonGroup": alaArpPoisonGroup,
       "alaIpNetToMediaAugGroup": alaIpNetToMediaAugGroup,
       "alaPktDropGroup": alaPktDropGroup,
       "alaIpCidrAugGroup": alaIpCidrAugGroup,
       "alaIcmpCtrlGroup": alaIcmpCtrlGroup,
       "alaIpRouteSumGroup": alaIpRouteSumGroup,
       "alaIpArpFilterGroup": alaIpArpFilterGroup,
       "alaIpServiceTypeGroup": alaIpServiceTypeGroup,
       "alaIpPortServiceTypeGroup": alaIpPortServiceTypeGroup,
       "alaIpInterfaceGroup": alaIpInterfaceGroup,
       "alaIpItfGroup": alaIpItfGroup,
       "alaIpFtpGroup": alaIpFtpGroup,
       "alaIpSshGroup": alaIpSshGroup,
       "alaIpTelnetGroup": alaIpTelnetGroup,
       "alaIpNotificationGroup": alaIpNotificationGroup,
       "alaIpDhcpHostIdentifierGroup": alaIpDhcpHostIdentifierGroup,
       "alaIpNtpGroup": alaIpNtpGroup,
       "alaDistArpNiGroup": alaDistArpNiGroup,
       "alaIpServiceSourceIpGroup": alaIpServiceSourceIpGroup,
       "alaDistArpItfGroup": alaDistArpItfGroup,
       "alaIpNetToMediaDpGroup": alaIpNetToMediaDpGroup,
       "alaAntiSpoofGlobalGroup": alaAntiSpoofGlobalGroup,
       "alaAntiSpoofGroup": alaAntiSpoofGroup}
)
