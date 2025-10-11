# SNMP MIB module (ELTEX-MES-ISS-SNOOP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-SNOOP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:51:03 2025
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

(fsSnoopPortEntry,
 fsSnoopVlanFilterEntry) = mibBuilder.importSymbols(
    "ARICENT-SNOOP-MIB",
    "fsSnoopPortEntry",
    "fsSnoopVlanFilterEntry")

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssSnoopMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8)
)
if mibBuilder.loadTexts:
    eltMesIssSnoopMIB.setRevisions(
        ("2021-05-17 00:00",
         "2020-12-04 00:00",
         "2020-11-17 00:00",
         "2019-04-19 00:00",
         "2019-01-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EltMesIssSnoopAuthType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("radius", 2))
    )



class EltMesIssSnoopAuthStatusType(TextualConvention, Integer32):
    status = "current"
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
        *(("waiting", 1),
          ("forward", 2),
          ("discard", 3),
          ("timeout", 4))
    )



# MIB Managed Objects in the order of their OIDs

_EltMesIssSnoopObjects_ObjectIdentity = ObjectIdentity
eltMesIssSnoopObjects = _EltMesIssSnoopObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1)
)
_EltMesIssSnoopGlobals_ObjectIdentity = ObjectIdentity
eltMesIssSnoopGlobals = _EltMesIssSnoopGlobals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 1)
)


class _EltMesIssSnoopClearGroups_Type(Integer32):
    """Custom type eltMesIssSnoopClearGroups based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4094),
    )


_EltMesIssSnoopClearGroups_Type.__name__ = "Integer32"
_EltMesIssSnoopClearGroups_Object = MibScalar
eltMesIssSnoopClearGroups = _EltMesIssSnoopClearGroups_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 1, 1),
    _EltMesIssSnoopClearGroups_Type()
)
eltMesIssSnoopClearGroups.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopClearGroups.setStatus("current")


class _EltMesIssSnoopAuthCacheClear_Type(InterfaceIndexOrZero):
    """Custom type eltMesIssSnoopAuthCacheClear based on InterfaceIndexOrZero"""
    defaultValue = 0


_EltMesIssSnoopAuthCacheClear_Type.__name__ = "InterfaceIndexOrZero"
_EltMesIssSnoopAuthCacheClear_Object = MibScalar
eltMesIssSnoopAuthCacheClear = _EltMesIssSnoopAuthCacheClear_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 1, 2),
    _EltMesIssSnoopAuthCacheClear_Type()
)
eltMesIssSnoopAuthCacheClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheClear.setStatus("current")
_EltMesIssSnoopVlan_ObjectIdentity = ObjectIdentity
eltMesIssSnoopVlan = _EltMesIssSnoopVlan_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 2)
)
_EltMesIssSnoopVlanFilterTable_Object = MibTable
eltMesIssSnoopVlanFilterTable = _EltMesIssSnoopVlanFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 2, 1)
)
if mibBuilder.loadTexts:
    eltMesIssSnoopVlanFilterTable.setStatus("current")
_EltMesIssSnoopVlanFilterEntry_Object = MibTableRow
eltMesIssSnoopVlanFilterEntry = _EltMesIssSnoopVlanFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssSnoopVlanFilterEntry.setStatus("current")


class _EltMesIssSnoopVlanCoS_Type(Integer32):
    """Custom type eltMesIssSnoopVlanCoS based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(255, 255),
    )


_EltMesIssSnoopVlanCoS_Type.__name__ = "Integer32"
_EltMesIssSnoopVlanCoS_Object = MibTableColumn
eltMesIssSnoopVlanCoS = _EltMesIssSnoopVlanCoS_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 2, 1, 1, 1),
    _EltMesIssSnoopVlanCoS_Type()
)
eltMesIssSnoopVlanCoS.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopVlanCoS.setStatus("current")


class _EltMesIssSnoopSparseMode_Type(Integer32):
    """Custom type eltMesIssSnoopSparseMode based on Integer32"""
    defaultValue = 2

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


_EltMesIssSnoopSparseMode_Type.__name__ = "Integer32"
_EltMesIssSnoopSparseMode_Object = MibTableColumn
eltMesIssSnoopSparseMode = _EltMesIssSnoopSparseMode_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 2, 1, 1, 2),
    _EltMesIssSnoopSparseMode_Type()
)
eltMesIssSnoopSparseMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopSparseMode.setStatus("current")
_EltMesIssSnoopVlanReplaceSourceIp_Type = InetAddress
_EltMesIssSnoopVlanReplaceSourceIp_Object = MibTableColumn
eltMesIssSnoopVlanReplaceSourceIp = _EltMesIssSnoopVlanReplaceSourceIp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 2, 1, 1, 3),
    _EltMesIssSnoopVlanReplaceSourceIp_Type()
)
eltMesIssSnoopVlanReplaceSourceIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopVlanReplaceSourceIp.setStatus("current")
_EltMesIssSnoopPort_ObjectIdentity = ObjectIdentity
eltMesIssSnoopPort = _EltMesIssSnoopPort_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3)
)
_EltMesIssSnoopPortTable_Object = MibTable
eltMesIssSnoopPortTable = _EltMesIssSnoopPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 1)
)
if mibBuilder.loadTexts:
    eltMesIssSnoopPortTable.setStatus("current")
_EltMesIssSnoopPortEntry_Object = MibTableRow
eltMesIssSnoopPortEntry = _EltMesIssSnoopPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 1, 1)
)
if mibBuilder.loadTexts:
    eltMesIssSnoopPortEntry.setStatus("current")


class _EltMesIssSnoopProxyReportingTrust_Type(Integer32):
    """Custom type eltMesIssSnoopProxyReportingTrust based on Integer32"""
    defaultValue = 2

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


_EltMesIssSnoopProxyReportingTrust_Type.__name__ = "Integer32"
_EltMesIssSnoopProxyReportingTrust_Object = MibTableColumn
eltMesIssSnoopProxyReportingTrust = _EltMesIssSnoopProxyReportingTrust_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 1, 1, 1),
    _EltMesIssSnoopProxyReportingTrust_Type()
)
eltMesIssSnoopProxyReportingTrust.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopProxyReportingTrust.setStatus("current")
_EltMesIssSnoopAuthPortTable_Object = MibTable
eltMesIssSnoopAuthPortTable = _EltMesIssSnoopAuthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 2)
)
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthPortTable.setStatus("current")
_EltMesIssSnoopAuthPortEntry_Object = MibTableRow
eltMesIssSnoopAuthPortEntry = _EltMesIssSnoopAuthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 2, 1)
)
eltMesIssSnoopAuthPortEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-SNOOP-MIB", "eltMesIssSnoopAuthPortIfIndex"),
    (0, "ELTEX-MES-ISS-SNOOP-MIB", "eltMesIssSnoopAuthPortInetAddressType"),
)
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthPortEntry.setStatus("current")
_EltMesIssSnoopAuthPortIfIndex_Type = InterfaceIndex
_EltMesIssSnoopAuthPortIfIndex_Object = MibTableColumn
eltMesIssSnoopAuthPortIfIndex = _EltMesIssSnoopAuthPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 2, 1, 1),
    _EltMesIssSnoopAuthPortIfIndex_Type()
)
eltMesIssSnoopAuthPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthPortIfIndex.setStatus("current")
_EltMesIssSnoopAuthPortInetAddressType_Type = InetAddressType
_EltMesIssSnoopAuthPortInetAddressType_Object = MibTableColumn
eltMesIssSnoopAuthPortInetAddressType = _EltMesIssSnoopAuthPortInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 2, 1, 2),
    _EltMesIssSnoopAuthPortInetAddressType_Type()
)
eltMesIssSnoopAuthPortInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthPortInetAddressType.setStatus("current")


class _EltMesIssSnoopAuthPortType_Type(EltMesIssSnoopAuthType):
    """Custom type eltMesIssSnoopAuthPortType based on EltMesIssSnoopAuthType"""
    defaultValue = 1


_EltMesIssSnoopAuthPortType_Type.__name__ = "EltMesIssSnoopAuthType"
_EltMesIssSnoopAuthPortType_Object = MibTableColumn
eltMesIssSnoopAuthPortType = _EltMesIssSnoopAuthPortType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 2, 1, 3),
    _EltMesIssSnoopAuthPortType_Type()
)
eltMesIssSnoopAuthPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthPortType.setStatus("current")


class _EltMesIssSnoopAuthPortRequired_Type(TruthValue):
    """Custom type eltMesIssSnoopAuthPortRequired based on TruthValue"""
    defaultValue = 2


_EltMesIssSnoopAuthPortRequired_Type.__name__ = "TruthValue"
_EltMesIssSnoopAuthPortRequired_Object = MibTableColumn
eltMesIssSnoopAuthPortRequired = _EltMesIssSnoopAuthPortRequired_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 2, 1, 4),
    _EltMesIssSnoopAuthPortRequired_Type()
)
eltMesIssSnoopAuthPortRequired.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthPortRequired.setStatus("current")


class _EltMesIssSnoopAuthPortForwardFirstEnable_Type(TruthValue):
    """Custom type eltMesIssSnoopAuthPortForwardFirstEnable based on TruthValue"""
    defaultValue = 2


_EltMesIssSnoopAuthPortForwardFirstEnable_Type.__name__ = "TruthValue"
_EltMesIssSnoopAuthPortForwardFirstEnable_Object = MibTableColumn
eltMesIssSnoopAuthPortForwardFirstEnable = _EltMesIssSnoopAuthPortForwardFirstEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 2, 1, 5),
    _EltMesIssSnoopAuthPortForwardFirstEnable_Type()
)
eltMesIssSnoopAuthPortForwardFirstEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthPortForwardFirstEnable.setStatus("current")


class _EltMesIssSnoopAuthPortExceptionProfileId_Type(Unsigned32):
    """Custom type eltMesIssSnoopAuthPortExceptionProfileId based on Unsigned32"""
    defaultValue = 0


_EltMesIssSnoopAuthPortExceptionProfileId_Type.__name__ = "Unsigned32"
_EltMesIssSnoopAuthPortExceptionProfileId_Object = MibTableColumn
eltMesIssSnoopAuthPortExceptionProfileId = _EltMesIssSnoopAuthPortExceptionProfileId_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 2, 1, 6),
    _EltMesIssSnoopAuthPortExceptionProfileId_Type()
)
eltMesIssSnoopAuthPortExceptionProfileId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthPortExceptionProfileId.setStatus("current")
_EltMesIssSnoopAuthCacheTable_Object = MibTable
eltMesIssSnoopAuthCacheTable = _EltMesIssSnoopAuthCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3)
)
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheTable.setStatus("current")
_EltMesIssSnoopAuthCacheEntry_Object = MibTableRow
eltMesIssSnoopAuthCacheEntry = _EltMesIssSnoopAuthCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3, 1)
)
eltMesIssSnoopAuthCacheEntry.setIndexNames(
    (0, "ELTEX-MES-ISS-SNOOP-MIB", "eltMesIssSnoopAuthCacheIfIndex"),
    (0, "ELTEX-MES-ISS-SNOOP-MIB", "eltMesIssSnoopAuthCacheClientMac"),
    (0, "ELTEX-MES-ISS-SNOOP-MIB", "eltMesIssSnoopAuthCacheInetAddressType"),
    (0, "ELTEX-MES-ISS-SNOOP-MIB", "eltMesIssSnoopAuthCacheClientIpAddr"),
    (0, "ELTEX-MES-ISS-SNOOP-MIB", "eltMesIssSnoopAuthCacheGroupIpAddr"),
)
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheEntry.setStatus("current")
_EltMesIssSnoopAuthCacheIfIndex_Type = InterfaceIndex
_EltMesIssSnoopAuthCacheIfIndex_Object = MibTableColumn
eltMesIssSnoopAuthCacheIfIndex = _EltMesIssSnoopAuthCacheIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3, 1, 1),
    _EltMesIssSnoopAuthCacheIfIndex_Type()
)
eltMesIssSnoopAuthCacheIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheIfIndex.setStatus("current")
_EltMesIssSnoopAuthCacheClientMac_Type = MacAddress
_EltMesIssSnoopAuthCacheClientMac_Object = MibTableColumn
eltMesIssSnoopAuthCacheClientMac = _EltMesIssSnoopAuthCacheClientMac_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3, 1, 2),
    _EltMesIssSnoopAuthCacheClientMac_Type()
)
eltMesIssSnoopAuthCacheClientMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheClientMac.setStatus("current")
_EltMesIssSnoopAuthCacheInetAddressType_Type = InetAddressType
_EltMesIssSnoopAuthCacheInetAddressType_Object = MibTableColumn
eltMesIssSnoopAuthCacheInetAddressType = _EltMesIssSnoopAuthCacheInetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3, 1, 3),
    _EltMesIssSnoopAuthCacheInetAddressType_Type()
)
eltMesIssSnoopAuthCacheInetAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheInetAddressType.setStatus("current")
_EltMesIssSnoopAuthCacheClientIpAddr_Type = InetAddress
_EltMesIssSnoopAuthCacheClientIpAddr_Object = MibTableColumn
eltMesIssSnoopAuthCacheClientIpAddr = _EltMesIssSnoopAuthCacheClientIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3, 1, 4),
    _EltMesIssSnoopAuthCacheClientIpAddr_Type()
)
eltMesIssSnoopAuthCacheClientIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheClientIpAddr.setStatus("current")
_EltMesIssSnoopAuthCacheGroupIpAddr_Type = InetAddress
_EltMesIssSnoopAuthCacheGroupIpAddr_Object = MibTableColumn
eltMesIssSnoopAuthCacheGroupIpAddr = _EltMesIssSnoopAuthCacheGroupIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3, 1, 5),
    _EltMesIssSnoopAuthCacheGroupIpAddr_Type()
)
eltMesIssSnoopAuthCacheGroupIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheGroupIpAddr.setStatus("current")
_EltMesIssSnoopAuthCacheAuthServerType_Type = EltMesIssSnoopAuthType
_EltMesIssSnoopAuthCacheAuthServerType_Object = MibTableColumn
eltMesIssSnoopAuthCacheAuthServerType = _EltMesIssSnoopAuthCacheAuthServerType_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3, 1, 6),
    _EltMesIssSnoopAuthCacheAuthServerType_Type()
)
eltMesIssSnoopAuthCacheAuthServerType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheAuthServerType.setStatus("current")
_EltMesIssSnoopAuthCacheAuthServerIpAddr_Type = InetAddress
_EltMesIssSnoopAuthCacheAuthServerIpAddr_Object = MibTableColumn
eltMesIssSnoopAuthCacheAuthServerIpAddr = _EltMesIssSnoopAuthCacheAuthServerIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3, 1, 7),
    _EltMesIssSnoopAuthCacheAuthServerIpAddr_Type()
)
eltMesIssSnoopAuthCacheAuthServerIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheAuthServerIpAddr.setStatus("current")
_EltMesIssSnoopAuthCacheTimeStamp_Type = TimeStamp
_EltMesIssSnoopAuthCacheTimeStamp_Object = MibTableColumn
eltMesIssSnoopAuthCacheTimeStamp = _EltMesIssSnoopAuthCacheTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3, 1, 8),
    _EltMesIssSnoopAuthCacheTimeStamp_Type()
)
eltMesIssSnoopAuthCacheTimeStamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheTimeStamp.setStatus("current")
_EltMesIssSnoopAuthCacheStatus_Type = EltMesIssSnoopAuthStatusType
_EltMesIssSnoopAuthCacheStatus_Object = MibTableColumn
eltMesIssSnoopAuthCacheStatus = _EltMesIssSnoopAuthCacheStatus_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 3, 3, 1, 9),
    _EltMesIssSnoopAuthCacheStatus_Type()
)
eltMesIssSnoopAuthCacheStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheStatus.setStatus("current")
_EltMesIssSnoopConfigs_ObjectIdentity = ObjectIdentity
eltMesIssSnoopConfigs = _EltMesIssSnoopConfigs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 4)
)


class _EltMesIssSnoopAuthEnable_Type(TruthValue):
    """Custom type eltMesIssSnoopAuthEnable based on TruthValue"""
    defaultValue = 2


_EltMesIssSnoopAuthEnable_Type.__name__ = "TruthValue"
_EltMesIssSnoopAuthEnable_Object = MibScalar
eltMesIssSnoopAuthEnable = _EltMesIssSnoopAuthEnable_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 4, 1),
    _EltMesIssSnoopAuthEnable_Type()
)
eltMesIssSnoopAuthEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthEnable.setStatus("current")


class _EltMesIssSnoopAuthCacheTimeout_Type(Unsigned32):
    """Custom type eltMesIssSnoopAuthCacheTimeout based on Unsigned32"""
    defaultValue = 600


_EltMesIssSnoopAuthCacheTimeout_Type.__name__ = "Unsigned32"
_EltMesIssSnoopAuthCacheTimeout_Object = MibScalar
eltMesIssSnoopAuthCacheTimeout = _EltMesIssSnoopAuthCacheTimeout_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 8, 1, 4, 2),
    _EltMesIssSnoopAuthCacheTimeout_Type()
)
eltMesIssSnoopAuthCacheTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssSnoopAuthCacheTimeout.setStatus("current")
fsSnoopVlanFilterEntry.registerAugmentions(
    ("ELTEX-MES-ISS-SNOOP-MIB",
     "eltMesIssSnoopVlanFilterEntry")
)
eltMesIssSnoopVlanFilterEntry.setIndexNames(*fsSnoopVlanFilterEntry.getIndexNames())
fsSnoopPortEntry.registerAugmentions(
    ("ELTEX-MES-ISS-SNOOP-MIB",
     "eltMesIssSnoopPortEntry")
)
eltMesIssSnoopPortEntry.setIndexNames(*fsSnoopPortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-SNOOP-MIB",
    **{"EltMesIssSnoopAuthType": EltMesIssSnoopAuthType,
       "EltMesIssSnoopAuthStatusType": EltMesIssSnoopAuthStatusType,
       "eltMesIssSnoopMIB": eltMesIssSnoopMIB,
       "eltMesIssSnoopObjects": eltMesIssSnoopObjects,
       "eltMesIssSnoopGlobals": eltMesIssSnoopGlobals,
       "eltMesIssSnoopClearGroups": eltMesIssSnoopClearGroups,
       "eltMesIssSnoopAuthCacheClear": eltMesIssSnoopAuthCacheClear,
       "eltMesIssSnoopVlan": eltMesIssSnoopVlan,
       "eltMesIssSnoopVlanFilterTable": eltMesIssSnoopVlanFilterTable,
       "eltMesIssSnoopVlanFilterEntry": eltMesIssSnoopVlanFilterEntry,
       "eltMesIssSnoopVlanCoS": eltMesIssSnoopVlanCoS,
       "eltMesIssSnoopSparseMode": eltMesIssSnoopSparseMode,
       "eltMesIssSnoopVlanReplaceSourceIp": eltMesIssSnoopVlanReplaceSourceIp,
       "eltMesIssSnoopPort": eltMesIssSnoopPort,
       "eltMesIssSnoopPortTable": eltMesIssSnoopPortTable,
       "eltMesIssSnoopPortEntry": eltMesIssSnoopPortEntry,
       "eltMesIssSnoopProxyReportingTrust": eltMesIssSnoopProxyReportingTrust,
       "eltMesIssSnoopAuthPortTable": eltMesIssSnoopAuthPortTable,
       "eltMesIssSnoopAuthPortEntry": eltMesIssSnoopAuthPortEntry,
       "eltMesIssSnoopAuthPortIfIndex": eltMesIssSnoopAuthPortIfIndex,
       "eltMesIssSnoopAuthPortInetAddressType": eltMesIssSnoopAuthPortInetAddressType,
       "eltMesIssSnoopAuthPortType": eltMesIssSnoopAuthPortType,
       "eltMesIssSnoopAuthPortRequired": eltMesIssSnoopAuthPortRequired,
       "eltMesIssSnoopAuthPortForwardFirstEnable": eltMesIssSnoopAuthPortForwardFirstEnable,
       "eltMesIssSnoopAuthPortExceptionProfileId": eltMesIssSnoopAuthPortExceptionProfileId,
       "eltMesIssSnoopAuthCacheTable": eltMesIssSnoopAuthCacheTable,
       "eltMesIssSnoopAuthCacheEntry": eltMesIssSnoopAuthCacheEntry,
       "eltMesIssSnoopAuthCacheIfIndex": eltMesIssSnoopAuthCacheIfIndex,
       "eltMesIssSnoopAuthCacheClientMac": eltMesIssSnoopAuthCacheClientMac,
       "eltMesIssSnoopAuthCacheInetAddressType": eltMesIssSnoopAuthCacheInetAddressType,
       "eltMesIssSnoopAuthCacheClientIpAddr": eltMesIssSnoopAuthCacheClientIpAddr,
       "eltMesIssSnoopAuthCacheGroupIpAddr": eltMesIssSnoopAuthCacheGroupIpAddr,
       "eltMesIssSnoopAuthCacheAuthServerType": eltMesIssSnoopAuthCacheAuthServerType,
       "eltMesIssSnoopAuthCacheAuthServerIpAddr": eltMesIssSnoopAuthCacheAuthServerIpAddr,
       "eltMesIssSnoopAuthCacheTimeStamp": eltMesIssSnoopAuthCacheTimeStamp,
       "eltMesIssSnoopAuthCacheStatus": eltMesIssSnoopAuthCacheStatus,
       "eltMesIssSnoopConfigs": eltMesIssSnoopConfigs,
       "eltMesIssSnoopAuthEnable": eltMesIssSnoopAuthEnable,
       "eltMesIssSnoopAuthCacheTimeout": eltMesIssSnoopAuthCacheTimeout}
)
