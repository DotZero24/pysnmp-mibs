# SNMP MIB module (DHCP-SNOOPING-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/DHCP-SNOOPING-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:41:58 2025
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

(InetAddressIPv4,
 InetAddressIPv6) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv4",
    "InetAddressIPv6")

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcDhcpSnooping = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23)
)
if mibBuilder.loadTexts:
    rcDhcpSnooping.setRevisions(
        ("2010-12-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcDhcpSnoopingMibObjects_ObjectIdentity = ObjectIdentity
rcDhcpSnoopingMibObjects = _RcDhcpSnoopingMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1)
)
_RcDhcpSnoopingGroup_ObjectIdentity = ObjectIdentity
rcDhcpSnoopingGroup = _RcDhcpSnoopingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1)
)


class _RcDhcpSnoopingEnable_Type(EnableVar):
    """Custom type rcDhcpSnoopingEnable based on EnableVar"""
    defaultValue = 2


_RcDhcpSnoopingEnable_Type.__name__ = "EnableVar"
_RcDhcpSnoopingEnable_Object = MibScalar
rcDhcpSnoopingEnable = _RcDhcpSnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 1),
    _RcDhcpSnoopingEnable_Type()
)
rcDhcpSnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpSnoopingEnable.setStatus("current")
_RcDhcpSnoopingPortTable_Object = MibTable
rcDhcpSnoopingPortTable = _RcDhcpSnoopingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 2)
)
if mibBuilder.loadTexts:
    rcDhcpSnoopingPortTable.setStatus("current")
_RcDhcpSnoopingPortEntry_Object = MibTableRow
rcDhcpSnoopingPortEntry = _RcDhcpSnoopingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 2, 1)
)
rcDhcpSnoopingPortEntry.setIndexNames(
    (0, "DHCP-SNOOPING-MIB", "rcDhcpSnoopingPortIndex"),
)
if mibBuilder.loadTexts:
    rcDhcpSnoopingPortEntry.setStatus("current")
_RcDhcpSnoopingPortIndex_Type = Integer32
_RcDhcpSnoopingPortIndex_Object = MibTableColumn
rcDhcpSnoopingPortIndex = _RcDhcpSnoopingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 2, 1, 1),
    _RcDhcpSnoopingPortIndex_Type()
)
rcDhcpSnoopingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcpSnoopingPortIndex.setStatus("current")
_RcDhcpSnoopingPortEnable_Type = EnableVar
_RcDhcpSnoopingPortEnable_Object = MibTableColumn
rcDhcpSnoopingPortEnable = _RcDhcpSnoopingPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 2, 1, 2),
    _RcDhcpSnoopingPortEnable_Type()
)
rcDhcpSnoopingPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpSnoopingPortEnable.setStatus("current")


class _RcDhcpSnoopingPortTrust_Type(Integer32):
    """Custom type rcDhcpSnoopingPortTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_RcDhcpSnoopingPortTrust_Type.__name__ = "Integer32"
_RcDhcpSnoopingPortTrust_Object = MibTableColumn
rcDhcpSnoopingPortTrust = _RcDhcpSnoopingPortTrust_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 2, 1, 3),
    _RcDhcpSnoopingPortTrust_Type()
)
rcDhcpSnoopingPortTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpSnoopingPortTrust.setStatus("current")


class _RcDhcpSnoopingBindCurrentRows_Type(Integer32):
    """Custom type rcDhcpSnoopingBindCurrentRows based on Integer32"""
    defaultValue = 0


_RcDhcpSnoopingBindCurrentRows_Type.__name__ = "Integer32"
_RcDhcpSnoopingBindCurrentRows_Object = MibScalar
rcDhcpSnoopingBindCurrentRows = _RcDhcpSnoopingBindCurrentRows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 3),
    _RcDhcpSnoopingBindCurrentRows_Type()
)
rcDhcpSnoopingBindCurrentRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindCurrentRows.setStatus("current")


class _RcDhcpSnoopingBindHistoryMaxRows_Type(Integer32):
    """Custom type rcDhcpSnoopingBindHistoryMaxRows based on Integer32"""
    defaultValue = 0


_RcDhcpSnoopingBindHistoryMaxRows_Type.__name__ = "Integer32"
_RcDhcpSnoopingBindHistoryMaxRows_Object = MibScalar
rcDhcpSnoopingBindHistoryMaxRows = _RcDhcpSnoopingBindHistoryMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 4),
    _RcDhcpSnoopingBindHistoryMaxRows_Type()
)
rcDhcpSnoopingBindHistoryMaxRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindHistoryMaxRows.setStatus("current")
_RcDhcpSnoopingBindTable_Object = MibTable
rcDhcpSnoopingBindTable = _RcDhcpSnoopingBindTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 5)
)
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindTable.setStatus("current")
_RcDhcpSnoopingBindEntry_Object = MibTableRow
rcDhcpSnoopingBindEntry = _RcDhcpSnoopingBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 5, 1)
)
rcDhcpSnoopingBindEntry.setIndexNames(
    (0, "DHCP-SNOOPING-MIB", "rcDhcpSnoopingBindIp"),
)
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindEntry.setStatus("current")
_RcDhcpSnoopingBindIp_Type = InetAddressIPv4
_RcDhcpSnoopingBindIp_Object = MibTableColumn
rcDhcpSnoopingBindIp = _RcDhcpSnoopingBindIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 5, 1, 1),
    _RcDhcpSnoopingBindIp_Type()
)
rcDhcpSnoopingBindIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindIp.setStatus("current")
_RcDhcpSnoopingBindMac_Type = MacAddress
_RcDhcpSnoopingBindMac_Object = MibTableColumn
rcDhcpSnoopingBindMac = _RcDhcpSnoopingBindMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 5, 1, 2),
    _RcDhcpSnoopingBindMac_Type()
)
rcDhcpSnoopingBindMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindMac.setStatus("current")
_RcDhcpSnoopingBindLease_Type = Unsigned32
_RcDhcpSnoopingBindLease_Object = MibTableColumn
rcDhcpSnoopingBindLease = _RcDhcpSnoopingBindLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 5, 1, 3),
    _RcDhcpSnoopingBindLease_Type()
)
rcDhcpSnoopingBindLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindLease.setStatus("current")


class _RcDhcpSnoopingBindVlan_Type(Integer32):
    """Custom type rcDhcpSnoopingBindVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcDhcpSnoopingBindVlan_Type.__name__ = "Integer32"
_RcDhcpSnoopingBindVlan_Object = MibTableColumn
rcDhcpSnoopingBindVlan = _RcDhcpSnoopingBindVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 5, 1, 4),
    _RcDhcpSnoopingBindVlan_Type()
)
rcDhcpSnoopingBindVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindVlan.setStatus("current")
_RcDhcpSnoopingBindPort_Type = Integer32
_RcDhcpSnoopingBindPort_Object = MibTableColumn
rcDhcpSnoopingBindPort = _RcDhcpSnoopingBindPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 1, 5, 1, 5),
    _RcDhcpSnoopingBindPort_Type()
)
rcDhcpSnoopingBindPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindPort.setStatus("current")
_RcDhcp6SnoopingGroup_ObjectIdentity = ObjectIdentity
rcDhcp6SnoopingGroup = _RcDhcp6SnoopingGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2)
)


class _RcDhcp6SnoopingEnable_Type(EnableVar):
    """Custom type rcDhcp6SnoopingEnable based on EnableVar"""
    defaultValue = 2


_RcDhcp6SnoopingEnable_Type.__name__ = "EnableVar"
_RcDhcp6SnoopingEnable_Object = MibScalar
rcDhcp6SnoopingEnable = _RcDhcp6SnoopingEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 1),
    _RcDhcp6SnoopingEnable_Type()
)
rcDhcp6SnoopingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingEnable.setStatus("current")
_RcDhcp6SnoopingPortTable_Object = MibTable
rcDhcp6SnoopingPortTable = _RcDhcp6SnoopingPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 2)
)
if mibBuilder.loadTexts:
    rcDhcp6SnoopingPortTable.setStatus("current")
_RcDhcp6SnoopingPortEntry_Object = MibTableRow
rcDhcp6SnoopingPortEntry = _RcDhcp6SnoopingPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 2, 1)
)
rcDhcp6SnoopingPortEntry.setIndexNames(
    (0, "DHCP-SNOOPING-MIB", "rcDhcp6SnoopingPortIndex"),
)
if mibBuilder.loadTexts:
    rcDhcp6SnoopingPortEntry.setStatus("current")
_RcDhcp6SnoopingPortIndex_Type = Integer32
_RcDhcp6SnoopingPortIndex_Object = MibTableColumn
rcDhcp6SnoopingPortIndex = _RcDhcp6SnoopingPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 2, 1, 1),
    _RcDhcp6SnoopingPortIndex_Type()
)
rcDhcp6SnoopingPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingPortIndex.setStatus("current")
_RcDhcp6SnoopingPortEnable_Type = EnableVar
_RcDhcp6SnoopingPortEnable_Object = MibTableColumn
rcDhcp6SnoopingPortEnable = _RcDhcp6SnoopingPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 2, 1, 2),
    _RcDhcp6SnoopingPortEnable_Type()
)
rcDhcp6SnoopingPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingPortEnable.setStatus("current")


class _RcDhcp6SnoopingPortTrust_Type(Integer32):
    """Custom type rcDhcp6SnoopingPortTrust based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trusted", 1),
          ("untrusted", 2))
    )


_RcDhcp6SnoopingPortTrust_Type.__name__ = "Integer32"
_RcDhcp6SnoopingPortTrust_Object = MibTableColumn
rcDhcp6SnoopingPortTrust = _RcDhcp6SnoopingPortTrust_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 2, 1, 3),
    _RcDhcp6SnoopingPortTrust_Type()
)
rcDhcp6SnoopingPortTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingPortTrust.setStatus("current")


class _RcDhcp6SnoopingBindCurrentRows_Type(Integer32):
    """Custom type rcDhcp6SnoopingBindCurrentRows based on Integer32"""
    defaultValue = 0


_RcDhcp6SnoopingBindCurrentRows_Type.__name__ = "Integer32"
_RcDhcp6SnoopingBindCurrentRows_Object = MibScalar
rcDhcp6SnoopingBindCurrentRows = _RcDhcp6SnoopingBindCurrentRows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 3),
    _RcDhcp6SnoopingBindCurrentRows_Type()
)
rcDhcp6SnoopingBindCurrentRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingBindCurrentRows.setStatus("current")


class _RcDhcp6SnoopingBindHistoryMaxRows_Type(Integer32):
    """Custom type rcDhcp6SnoopingBindHistoryMaxRows based on Integer32"""
    defaultValue = 0


_RcDhcp6SnoopingBindHistoryMaxRows_Type.__name__ = "Integer32"
_RcDhcp6SnoopingBindHistoryMaxRows_Object = MibScalar
rcDhcp6SnoopingBindHistoryMaxRows = _RcDhcp6SnoopingBindHistoryMaxRows_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 4),
    _RcDhcp6SnoopingBindHistoryMaxRows_Type()
)
rcDhcp6SnoopingBindHistoryMaxRows.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingBindHistoryMaxRows.setStatus("current")
_RcDhcp6SnoopingBindTable_Object = MibTable
rcDhcp6SnoopingBindTable = _RcDhcp6SnoopingBindTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 5)
)
if mibBuilder.loadTexts:
    rcDhcp6SnoopingBindTable.setStatus("current")
_RcDhcp6SnoopingBindEntry_Object = MibTableRow
rcDhcp6SnoopingBindEntry = _RcDhcp6SnoopingBindEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 5, 1)
)
rcDhcp6SnoopingBindEntry.setIndexNames(
    (0, "DHCP-SNOOPING-MIB", "rcDhcp6SnoopingBindIp"),
)
if mibBuilder.loadTexts:
    rcDhcp6SnoopingBindEntry.setStatus("current")
_RcDhcp6SnoopingBindIp_Type = InetAddressIPv6
_RcDhcp6SnoopingBindIp_Object = MibTableColumn
rcDhcp6SnoopingBindIp = _RcDhcp6SnoopingBindIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 5, 1, 1),
    _RcDhcp6SnoopingBindIp_Type()
)
rcDhcp6SnoopingBindIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingBindIp.setStatus("current")
_RcDhcp6SnoopingBindMac_Type = MacAddress
_RcDhcp6SnoopingBindMac_Object = MibTableColumn
rcDhcp6SnoopingBindMac = _RcDhcp6SnoopingBindMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 5, 1, 2),
    _RcDhcp6SnoopingBindMac_Type()
)
rcDhcp6SnoopingBindMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingBindMac.setStatus("current")
_RcDhcp6SnoopingBindLease_Type = Unsigned32
_RcDhcp6SnoopingBindLease_Object = MibTableColumn
rcDhcp6SnoopingBindLease = _RcDhcp6SnoopingBindLease_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 5, 1, 3),
    _RcDhcp6SnoopingBindLease_Type()
)
rcDhcp6SnoopingBindLease.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingBindLease.setStatus("current")
_RcDhcp6SnoopingBindVlan_Type = Integer32
_RcDhcp6SnoopingBindVlan_Object = MibTableColumn
rcDhcp6SnoopingBindVlan = _RcDhcp6SnoopingBindVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 5, 1, 4),
    _RcDhcp6SnoopingBindVlan_Type()
)
rcDhcp6SnoopingBindVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingBindVlan.setStatus("current")
_RcDhcp6SnoopingBindPort_Type = Integer32
_RcDhcp6SnoopingBindPort_Object = MibTableColumn
rcDhcp6SnoopingBindPort = _RcDhcp6SnoopingBindPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 2, 5, 1, 5),
    _RcDhcp6SnoopingBindPort_Type()
)
rcDhcp6SnoopingBindPort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingBindPort.setStatus("current")
_RcDhcp4SnoopingOptionGroup_ObjectIdentity = ObjectIdentity
rcDhcp4SnoopingOptionGroup = _RcDhcp4SnoopingOptionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 3)
)


class _RcDhcpSnoopingOptionList_Type(OctetString):
    """Custom type rcDhcpSnoopingOptionList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_RcDhcpSnoopingOptionList_Type.__name__ = "OctetString"
_RcDhcpSnoopingOptionList_Object = MibScalar
rcDhcpSnoopingOptionList = _RcDhcpSnoopingOptionList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 3, 1),
    _RcDhcpSnoopingOptionList_Type()
)
rcDhcpSnoopingOptionList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpSnoopingOptionList.setStatus("current")
_RcDhcp6SnoopingOptionGroup_ObjectIdentity = ObjectIdentity
rcDhcp6SnoopingOptionGroup = _RcDhcp6SnoopingOptionGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 4)
)


class _RcDhcp6SnoopingOptionList_Type(OctetString):
    """Custom type rcDhcp6SnoopingOptionList based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32


_RcDhcp6SnoopingOptionList_Type.__name__ = "OctetString"
_RcDhcp6SnoopingOptionList_Object = MibScalar
rcDhcp6SnoopingOptionList = _RcDhcp6SnoopingOptionList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 4, 1),
    _RcDhcp6SnoopingOptionList_Type()
)
rcDhcp6SnoopingOptionList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcp6SnoopingOptionList.setStatus("current")
_RcDhcpSnoopingBindSaveGroup_ObjectIdentity = ObjectIdentity
rcDhcpSnoopingBindSaveGroup = _RcDhcpSnoopingBindSaveGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 5)
)


class _RcDhcpSnoopingBindSaveEnable_Type(EnableVar):
    """Custom type rcDhcpSnoopingBindSaveEnable based on EnableVar"""
    defaultValue = 2


_RcDhcpSnoopingBindSaveEnable_Type.__name__ = "EnableVar"
_RcDhcpSnoopingBindSaveEnable_Object = MibScalar
rcDhcpSnoopingBindSaveEnable = _RcDhcpSnoopingBindSaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 5, 1),
    _RcDhcpSnoopingBindSaveEnable_Type()
)
rcDhcpSnoopingBindSaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindSaveEnable.setStatus("current")


class _RcDhcpSnoopingBindSaveWriteDelay_Type(Integer32):
    """Custom type rcDhcpSnoopingBindSaveWriteDelay based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 2147483647),
    )


_RcDhcpSnoopingBindSaveWriteDelay_Type.__name__ = "Integer32"
_RcDhcpSnoopingBindSaveWriteDelay_Object = MibScalar
rcDhcpSnoopingBindSaveWriteDelay = _RcDhcpSnoopingBindSaveWriteDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 23, 1, 5, 2),
    _RcDhcpSnoopingBindSaveWriteDelay_Type()
)
rcDhcpSnoopingBindSaveWriteDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDhcpSnoopingBindSaveWriteDelay.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DHCP-SNOOPING-MIB",
    **{"rcDhcpSnooping": rcDhcpSnooping,
       "rcDhcpSnoopingMibObjects": rcDhcpSnoopingMibObjects,
       "rcDhcpSnoopingGroup": rcDhcpSnoopingGroup,
       "rcDhcpSnoopingEnable": rcDhcpSnoopingEnable,
       "rcDhcpSnoopingPortTable": rcDhcpSnoopingPortTable,
       "rcDhcpSnoopingPortEntry": rcDhcpSnoopingPortEntry,
       "rcDhcpSnoopingPortIndex": rcDhcpSnoopingPortIndex,
       "rcDhcpSnoopingPortEnable": rcDhcpSnoopingPortEnable,
       "rcDhcpSnoopingPortTrust": rcDhcpSnoopingPortTrust,
       "rcDhcpSnoopingBindCurrentRows": rcDhcpSnoopingBindCurrentRows,
       "rcDhcpSnoopingBindHistoryMaxRows": rcDhcpSnoopingBindHistoryMaxRows,
       "rcDhcpSnoopingBindTable": rcDhcpSnoopingBindTable,
       "rcDhcpSnoopingBindEntry": rcDhcpSnoopingBindEntry,
       "rcDhcpSnoopingBindIp": rcDhcpSnoopingBindIp,
       "rcDhcpSnoopingBindMac": rcDhcpSnoopingBindMac,
       "rcDhcpSnoopingBindLease": rcDhcpSnoopingBindLease,
       "rcDhcpSnoopingBindVlan": rcDhcpSnoopingBindVlan,
       "rcDhcpSnoopingBindPort": rcDhcpSnoopingBindPort,
       "rcDhcp6SnoopingGroup": rcDhcp6SnoopingGroup,
       "rcDhcp6SnoopingEnable": rcDhcp6SnoopingEnable,
       "rcDhcp6SnoopingPortTable": rcDhcp6SnoopingPortTable,
       "rcDhcp6SnoopingPortEntry": rcDhcp6SnoopingPortEntry,
       "rcDhcp6SnoopingPortIndex": rcDhcp6SnoopingPortIndex,
       "rcDhcp6SnoopingPortEnable": rcDhcp6SnoopingPortEnable,
       "rcDhcp6SnoopingPortTrust": rcDhcp6SnoopingPortTrust,
       "rcDhcp6SnoopingBindCurrentRows": rcDhcp6SnoopingBindCurrentRows,
       "rcDhcp6SnoopingBindHistoryMaxRows": rcDhcp6SnoopingBindHistoryMaxRows,
       "rcDhcp6SnoopingBindTable": rcDhcp6SnoopingBindTable,
       "rcDhcp6SnoopingBindEntry": rcDhcp6SnoopingBindEntry,
       "rcDhcp6SnoopingBindIp": rcDhcp6SnoopingBindIp,
       "rcDhcp6SnoopingBindMac": rcDhcp6SnoopingBindMac,
       "rcDhcp6SnoopingBindLease": rcDhcp6SnoopingBindLease,
       "rcDhcp6SnoopingBindVlan": rcDhcp6SnoopingBindVlan,
       "rcDhcp6SnoopingBindPort": rcDhcp6SnoopingBindPort,
       "rcDhcp4SnoopingOptionGroup": rcDhcp4SnoopingOptionGroup,
       "rcDhcpSnoopingOptionList": rcDhcpSnoopingOptionList,
       "rcDhcp6SnoopingOptionGroup": rcDhcp6SnoopingOptionGroup,
       "rcDhcp6SnoopingOptionList": rcDhcp6SnoopingOptionList,
       "rcDhcpSnoopingBindSaveGroup": rcDhcpSnoopingBindSaveGroup,
       "rcDhcpSnoopingBindSaveEnable": rcDhcpSnoopingBindSaveEnable,
       "rcDhcpSnoopingBindSaveWriteDelay": rcDhcpSnoopingBindSaveWriteDelay}
)
