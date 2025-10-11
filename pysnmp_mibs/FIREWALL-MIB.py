# SNMP MIB module (FIREWALL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/supermicro/FIREWALL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:44:15 2025
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

(InetAddress,
 InetAddressPrefixLength,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressPrefixLength",
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
 RowPointer,
 RowStatus,
 TextualConvention,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowPointer",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

firewall = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16)
)
if mibBuilder.loadTexts:
    firewall.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class Status(TextualConvention, Integer32):
    status = "current"
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



class ProtocolType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              6,
              8,
              9,
              11,
              17,
              28,
              35,
              46,
              48,
              88,
              89,
              255)
        )
    )
    namedValues = NamedValues(
        *(("icmp", 1),
          ("igmp", 2),
          ("ggp", 3),
          ("ip", 4),
          ("tcp", 6),
          ("egp", 8),
          ("igp", 9),
          ("nvp", 11),
          ("udp", 17),
          ("irtp", 28),
          ("idpr", 35),
          ("rsvp", 46),
          ("mhrp", 48),
          ("igrp", 88),
          ("ospfigp", 89),
          ("any", 255))
    )



# MIB Managed Objects in the order of their OIDs

_FwlGlobal_ObjectIdentity = ObjectIdentity
fwlGlobal = _FwlGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1)
)


class _FwlGlobalMasterControlSwitch_Type(Status):
    """Custom type fwlGlobalMasterControlSwitch based on Status"""
    defaultValue = 1


_FwlGlobalMasterControlSwitch_Type.__name__ = "Status"
_FwlGlobalMasterControlSwitch_Object = MibScalar
fwlGlobalMasterControlSwitch = _FwlGlobalMasterControlSwitch_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 1),
    _FwlGlobalMasterControlSwitch_Type()
)
fwlGlobalMasterControlSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalMasterControlSwitch.setStatus("current")


class _FwlGlobalICMPControlSwitch_Type(Integer32):
    """Custom type fwlGlobalICMPControlSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generate", 1),
          ("suppress", 2))
    )


_FwlGlobalICMPControlSwitch_Type.__name__ = "Integer32"
_FwlGlobalICMPControlSwitch_Object = MibScalar
fwlGlobalICMPControlSwitch = _FwlGlobalICMPControlSwitch_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 2),
    _FwlGlobalICMPControlSwitch_Type()
)
fwlGlobalICMPControlSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalICMPControlSwitch.setStatus("current")


class _FwlGlobalIpSpoofFiltering_Type(Status):
    """Custom type fwlGlobalIpSpoofFiltering based on Status"""
    defaultValue = 1


_FwlGlobalIpSpoofFiltering_Type.__name__ = "Status"
_FwlGlobalIpSpoofFiltering_Object = MibScalar
fwlGlobalIpSpoofFiltering = _FwlGlobalIpSpoofFiltering_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 3),
    _FwlGlobalIpSpoofFiltering_Type()
)
fwlGlobalIpSpoofFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalIpSpoofFiltering.setStatus("current")


class _FwlGlobalSrcRouteFiltering_Type(Status):
    """Custom type fwlGlobalSrcRouteFiltering based on Status"""
    defaultValue = 1


_FwlGlobalSrcRouteFiltering_Type.__name__ = "Status"
_FwlGlobalSrcRouteFiltering_Object = MibScalar
fwlGlobalSrcRouteFiltering = _FwlGlobalSrcRouteFiltering_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 4),
    _FwlGlobalSrcRouteFiltering_Type()
)
fwlGlobalSrcRouteFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalSrcRouteFiltering.setStatus("deprecated")


class _FwlGlobalTinyFragmentFiltering_Type(Status):
    """Custom type fwlGlobalTinyFragmentFiltering based on Status"""
    defaultValue = 1


_FwlGlobalTinyFragmentFiltering_Type.__name__ = "Status"
_FwlGlobalTinyFragmentFiltering_Object = MibScalar
fwlGlobalTinyFragmentFiltering = _FwlGlobalTinyFragmentFiltering_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 5),
    _FwlGlobalTinyFragmentFiltering_Type()
)
fwlGlobalTinyFragmentFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalTinyFragmentFiltering.setStatus("deprecated")


class _FwlGlobalTcpIntercept_Type(Status):
    """Custom type fwlGlobalTcpIntercept based on Status"""
    defaultValue = 1


_FwlGlobalTcpIntercept_Type.__name__ = "Status"
_FwlGlobalTcpIntercept_Object = MibScalar
fwlGlobalTcpIntercept = _FwlGlobalTcpIntercept_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 6),
    _FwlGlobalTcpIntercept_Type()
)
fwlGlobalTcpIntercept.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalTcpIntercept.setStatus("current")


class _FwlGlobalTrap_Type(Status):
    """Custom type fwlGlobalTrap based on Status"""
    defaultValue = 2


_FwlGlobalTrap_Type.__name__ = "Status"
_FwlGlobalTrap_Object = MibScalar
fwlGlobalTrap = _FwlGlobalTrap_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 7),
    _FwlGlobalTrap_Type()
)
fwlGlobalTrap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalTrap.setStatus("current")


class _FwlGlobalTrace_Type(Integer32):
    """Custom type fwlGlobalTrace based on Integer32"""
    defaultValue = 0


_FwlGlobalTrace_Type.__name__ = "Integer32"
_FwlGlobalTrace_Object = MibScalar
fwlGlobalTrace = _FwlGlobalTrace_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 8),
    _FwlGlobalTrace_Type()
)
fwlGlobalTrace.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalTrace.setStatus("current")


class _FwlGlobalDebug_Type(Status):
    """Custom type fwlGlobalDebug based on Status"""
    defaultValue = 2


_FwlGlobalDebug_Type.__name__ = "Status"
_FwlGlobalDebug_Object = MibScalar
fwlGlobalDebug = _FwlGlobalDebug_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 9),
    _FwlGlobalDebug_Type()
)
fwlGlobalDebug.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalDebug.setStatus("current")


class _FwlGlobalMaxFilters_Type(Integer32):
    """Custom type fwlGlobalMaxFilters based on Integer32"""
    defaultValue = 100


_FwlGlobalMaxFilters_Type.__name__ = "Integer32"
_FwlGlobalMaxFilters_Object = MibScalar
fwlGlobalMaxFilters = _FwlGlobalMaxFilters_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 10),
    _FwlGlobalMaxFilters_Type()
)
fwlGlobalMaxFilters.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlGlobalMaxFilters.setStatus("current")


class _FwlGlobalMaxRules_Type(Integer32):
    """Custom type fwlGlobalMaxRules based on Integer32"""
    defaultValue = 100


_FwlGlobalMaxRules_Type.__name__ = "Integer32"
_FwlGlobalMaxRules_Object = MibScalar
fwlGlobalMaxRules = _FwlGlobalMaxRules_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 11),
    _FwlGlobalMaxRules_Type()
)
fwlGlobalMaxRules.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlGlobalMaxRules.setStatus("current")


class _FwlGlobalUrlFiltering_Type(Status):
    """Custom type fwlGlobalUrlFiltering based on Status"""
    defaultValue = 2


_FwlGlobalUrlFiltering_Type.__name__ = "Status"
_FwlGlobalUrlFiltering_Object = MibScalar
fwlGlobalUrlFiltering = _FwlGlobalUrlFiltering_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 12),
    _FwlGlobalUrlFiltering_Type()
)
fwlGlobalUrlFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalUrlFiltering.setStatus("current")


class _FwlGlobalNetBiosFiltering_Type(Status):
    """Custom type fwlGlobalNetBiosFiltering based on Status"""
    defaultValue = 2


_FwlGlobalNetBiosFiltering_Type.__name__ = "Status"
_FwlGlobalNetBiosFiltering_Object = MibScalar
fwlGlobalNetBiosFiltering = _FwlGlobalNetBiosFiltering_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 13),
    _FwlGlobalNetBiosFiltering_Type()
)
fwlGlobalNetBiosFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalNetBiosFiltering.setStatus("current")


class _FwlGlobalNetBiosLan2Wan_Type(Status):
    """Custom type fwlGlobalNetBiosLan2Wan based on Status"""
    defaultValue = 2


_FwlGlobalNetBiosLan2Wan_Type.__name__ = "Status"
_FwlGlobalNetBiosLan2Wan_Object = MibScalar
fwlGlobalNetBiosLan2Wan = _FwlGlobalNetBiosLan2Wan_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 14),
    _FwlGlobalNetBiosLan2Wan_Type()
)
fwlGlobalNetBiosLan2Wan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalNetBiosLan2Wan.setStatus("current")


class _FwlGlobalICMPv6ControlSwitch_Type(Integer32):
    """Custom type fwlGlobalICMPv6ControlSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("generate", 1),
          ("suppress", 2))
    )


_FwlGlobalICMPv6ControlSwitch_Type.__name__ = "Integer32"
_FwlGlobalICMPv6ControlSwitch_Object = MibScalar
fwlGlobalICMPv6ControlSwitch = _FwlGlobalICMPv6ControlSwitch_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 15),
    _FwlGlobalICMPv6ControlSwitch_Type()
)
fwlGlobalICMPv6ControlSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalICMPv6ControlSwitch.setStatus("current")


class _FwlGlobalIpv6SpoofFiltering_Type(Status):
    """Custom type fwlGlobalIpv6SpoofFiltering based on Status"""
    defaultValue = 1


_FwlGlobalIpv6SpoofFiltering_Type.__name__ = "Status"
_FwlGlobalIpv6SpoofFiltering_Object = MibScalar
fwlGlobalIpv6SpoofFiltering = _FwlGlobalIpv6SpoofFiltering_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 16),
    _FwlGlobalIpv6SpoofFiltering_Type()
)
fwlGlobalIpv6SpoofFiltering.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalIpv6SpoofFiltering.setStatus("current")


class _FwlGlobalLogFileSize_Type(Unsigned32):
    """Custom type fwlGlobalLogFileSize based on Unsigned32"""
    defaultValue = 1048576


_FwlGlobalLogFileSize_Type.__name__ = "Unsigned32"
_FwlGlobalLogFileSize_Object = MibScalar
fwlGlobalLogFileSize = _FwlGlobalLogFileSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 17),
    _FwlGlobalLogFileSize_Type()
)
fwlGlobalLogFileSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalLogFileSize.setStatus("current")


class _FwlGlobalLogSizeThreshold_Type(Unsigned32):
    """Custom type fwlGlobalLogSizeThreshold based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FwlGlobalLogSizeThreshold_Type.__name__ = "Unsigned32"
_FwlGlobalLogSizeThreshold_Object = MibScalar
fwlGlobalLogSizeThreshold = _FwlGlobalLogSizeThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 18),
    _FwlGlobalLogSizeThreshold_Type()
)
fwlGlobalLogSizeThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalLogSizeThreshold.setStatus("current")


class _FwlGlobalIdsLogSize_Type(Unsigned32):
    """Custom type fwlGlobalIdsLogSize based on Unsigned32"""
    defaultValue = 1048576


_FwlGlobalIdsLogSize_Type.__name__ = "Unsigned32"
_FwlGlobalIdsLogSize_Object = MibScalar
fwlGlobalIdsLogSize = _FwlGlobalIdsLogSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 19),
    _FwlGlobalIdsLogSize_Type()
)
fwlGlobalIdsLogSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalIdsLogSize.setStatus("current")


class _FwlGlobalIdsLogThreshold_Type(Unsigned32):
    """Custom type fwlGlobalIdsLogThreshold based on Unsigned32"""
    defaultValue = 70

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 99),
    )


_FwlGlobalIdsLogThreshold_Type.__name__ = "Unsigned32"
_FwlGlobalIdsLogThreshold_Object = MibScalar
fwlGlobalIdsLogThreshold = _FwlGlobalIdsLogThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 20),
    _FwlGlobalIdsLogThreshold_Type()
)
fwlGlobalIdsLogThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalIdsLogThreshold.setStatus("current")


class _FwlGlobalIdsVersionInfo_Type(DisplayString):
    """Custom type fwlGlobalIdsVersionInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_FwlGlobalIdsVersionInfo_Type.__name__ = "DisplayString"
_FwlGlobalIdsVersionInfo_Object = MibScalar
fwlGlobalIdsVersionInfo = _FwlGlobalIdsVersionInfo_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 21),
    _FwlGlobalIdsVersionInfo_Type()
)
fwlGlobalIdsVersionInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlGlobalIdsVersionInfo.setStatus("current")
_FwlGlobalReloadIds_Type = Integer32
_FwlGlobalReloadIds_Object = MibScalar
fwlGlobalReloadIds = _FwlGlobalReloadIds_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 22),
    _FwlGlobalReloadIds_Type()
)
fwlGlobalReloadIds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalReloadIds.setStatus("current")


class _FwlGlobalIdsStatus_Type(Status):
    """Custom type fwlGlobalIdsStatus based on Status"""
    defaultValue = 1


_FwlGlobalIdsStatus_Type.__name__ = "Status"
_FwlGlobalIdsStatus_Object = MibScalar
fwlGlobalIdsStatus = _FwlGlobalIdsStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 23),
    _FwlGlobalIdsStatus_Type()
)
fwlGlobalIdsStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalIdsStatus.setStatus("current")


class _FwlGlobalLoadIdsRules_Type(Integer32):
    """Custom type fwlGlobalLoadIdsRules based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("load", 1),
          ("unload", 2))
    )


_FwlGlobalLoadIdsRules_Type.__name__ = "Integer32"
_FwlGlobalLoadIdsRules_Object = MibScalar
fwlGlobalLoadIdsRules = _FwlGlobalLoadIdsRules_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 1, 24),
    _FwlGlobalLoadIdsRules_Type()
)
fwlGlobalLoadIdsRules.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlGlobalLoadIdsRules.setStatus("current")
_FwlDefinition_ObjectIdentity = ObjectIdentity
fwlDefinition = _FwlDefinition_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2)
)


class _FwlDefnTcpInterceptThreshold_Type(Integer32):
    """Custom type fwlDefnTcpInterceptThreshold based on Integer32"""
    defaultValue = 50


_FwlDefnTcpInterceptThreshold_Type.__name__ = "Integer32"
_FwlDefnTcpInterceptThreshold_Object = MibScalar
fwlDefnTcpInterceptThreshold = _FwlDefnTcpInterceptThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 1),
    _FwlDefnTcpInterceptThreshold_Type()
)
fwlDefnTcpInterceptThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlDefnTcpInterceptThreshold.setStatus("current")


class _FwlDefnInterceptTimeout_Type(TimeTicks):
    """Custom type fwlDefnInterceptTimeout based on TimeTicks"""
    defaultValue = 1


_FwlDefnInterceptTimeout_Type.__name__ = "TimeTicks"
_FwlDefnInterceptTimeout_Object = MibScalar
fwlDefnInterceptTimeout = _FwlDefnInterceptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 2),
    _FwlDefnInterceptTimeout_Type()
)
fwlDefnInterceptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlDefnInterceptTimeout.setStatus("current")
_FwlDefnFilterTable_Object = MibTable
fwlDefnFilterTable = _FwlDefnFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3)
)
if mibBuilder.loadTexts:
    fwlDefnFilterTable.setStatus("current")
_FwlDefnFilterEntry_Object = MibTableRow
fwlDefnFilterEntry = _FwlDefnFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1)
)
fwlDefnFilterEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlFilterFilterName"),
)
if mibBuilder.loadTexts:
    fwlDefnFilterEntry.setStatus("current")


class _FwlFilterFilterName_Type(OctetString):
    """Custom type fwlFilterFilterName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_FwlFilterFilterName_Type.__name__ = "OctetString"
_FwlFilterFilterName_Object = MibTableColumn
fwlFilterFilterName = _FwlFilterFilterName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 1),
    _FwlFilterFilterName_Type()
)
fwlFilterFilterName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlFilterFilterName.setStatus("current")


class _FwlFilterSrcAddress_Type(DisplayString):
    """Custom type fwlFilterSrcAddress based on DisplayString"""
    defaultHexValue = ""


_FwlFilterSrcAddress_Type.__name__ = "DisplayString"
_FwlFilterSrcAddress_Object = MibTableColumn
fwlFilterSrcAddress = _FwlFilterSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 2),
    _FwlFilterSrcAddress_Type()
)
fwlFilterSrcAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterSrcAddress.setStatus("current")


class _FwlFilterDestAddress_Type(DisplayString):
    """Custom type fwlFilterDestAddress based on DisplayString"""
    defaultHexValue = ""


_FwlFilterDestAddress_Type.__name__ = "DisplayString"
_FwlFilterDestAddress_Object = MibTableColumn
fwlFilterDestAddress = _FwlFilterDestAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 3),
    _FwlFilterDestAddress_Type()
)
fwlFilterDestAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterDestAddress.setStatus("current")


class _FwlFilterProtocol_Type(ProtocolType):
    """Custom type fwlFilterProtocol based on ProtocolType"""
    defaultValue = 255


_FwlFilterProtocol_Type.__name__ = "ProtocolType"
_FwlFilterProtocol_Object = MibTableColumn
fwlFilterProtocol = _FwlFilterProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 4),
    _FwlFilterProtocol_Type()
)
fwlFilterProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterProtocol.setStatus("current")


class _FwlFilterSrcPort_Type(DisplayString):
    """Custom type fwlFilterSrcPort based on DisplayString"""
    defaultHexValue = ""


_FwlFilterSrcPort_Type.__name__ = "DisplayString"
_FwlFilterSrcPort_Object = MibTableColumn
fwlFilterSrcPort = _FwlFilterSrcPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 5),
    _FwlFilterSrcPort_Type()
)
fwlFilterSrcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterSrcPort.setStatus("current")


class _FwlFilterDestPort_Type(DisplayString):
    """Custom type fwlFilterDestPort based on DisplayString"""
    defaultHexValue = ""


_FwlFilterDestPort_Type.__name__ = "DisplayString"
_FwlFilterDestPort_Object = MibTableColumn
fwlFilterDestPort = _FwlFilterDestPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 6),
    _FwlFilterDestPort_Type()
)
fwlFilterDestPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterDestPort.setStatus("current")


class _FwlFilterAckBit_Type(Integer32):
    """Custom type fwlFilterAckBit based on Integer32"""
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
        *(("establish", 1),
          ("notEstablish", 2),
          ("any", 3))
    )


_FwlFilterAckBit_Type.__name__ = "Integer32"
_FwlFilterAckBit_Object = MibTableColumn
fwlFilterAckBit = _FwlFilterAckBit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 7),
    _FwlFilterAckBit_Type()
)
fwlFilterAckBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterAckBit.setStatus("deprecated")


class _FwlFilterRstBit_Type(Integer32):
    """Custom type fwlFilterRstBit based on Integer32"""
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
        *(("set", 1),
          ("notSet", 2),
          ("any", 3))
    )


_FwlFilterRstBit_Type.__name__ = "Integer32"
_FwlFilterRstBit_Object = MibTableColumn
fwlFilterRstBit = _FwlFilterRstBit_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 8),
    _FwlFilterRstBit_Type()
)
fwlFilterRstBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterRstBit.setStatus("deprecated")


class _FwlFilterTos_Type(Integer32):
    """Custom type fwlFilterTos based on Integer32"""
    defaultValue = 0


_FwlFilterTos_Type.__name__ = "Integer32"
_FwlFilterTos_Object = MibTableColumn
fwlFilterTos = _FwlFilterTos_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 9),
    _FwlFilterTos_Type()
)
fwlFilterTos.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterTos.setStatus("current")


class _FwlFilterAccounting_Type(Status):
    """Custom type fwlFilterAccounting based on Status"""
    defaultValue = 2


_FwlFilterAccounting_Type.__name__ = "Status"
_FwlFilterAccounting_Object = MibTableColumn
fwlFilterAccounting = _FwlFilterAccounting_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 10),
    _FwlFilterAccounting_Type()
)
fwlFilterAccounting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlFilterAccounting.setStatus("current")


class _FwlFilterHitClear_Type(TruthValue):
    """Custom type fwlFilterHitClear based on TruthValue"""
    defaultValue = 2


_FwlFilterHitClear_Type.__name__ = "TruthValue"
_FwlFilterHitClear_Object = MibTableColumn
fwlFilterHitClear = _FwlFilterHitClear_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 11),
    _FwlFilterHitClear_Type()
)
fwlFilterHitClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlFilterHitClear.setStatus("current")
_FwlFilterHitsCount_Type = Counter32
_FwlFilterHitsCount_Object = MibTableColumn
fwlFilterHitsCount = _FwlFilterHitsCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 12),
    _FwlFilterHitsCount_Type()
)
fwlFilterHitsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlFilterHitsCount.setStatus("current")
_FwlFilterAddrType_Type = InetAddressType
_FwlFilterAddrType_Object = MibTableColumn
fwlFilterAddrType = _FwlFilterAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 13),
    _FwlFilterAddrType_Type()
)
fwlFilterAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterAddrType.setStatus("current")


class _FwlFilterFlowId_Type(Unsigned32):
    """Custom type fwlFilterFlowId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048575),
    )


_FwlFilterFlowId_Type.__name__ = "Unsigned32"
_FwlFilterFlowId_Object = MibTableColumn
fwlFilterFlowId = _FwlFilterFlowId_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 14),
    _FwlFilterFlowId_Type()
)
fwlFilterFlowId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterFlowId.setStatus("current")


class _FwlFilterDscp_Type(Integer32):
    """Custom type fwlFilterDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_FwlFilterDscp_Type.__name__ = "Integer32"
_FwlFilterDscp_Object = MibTableColumn
fwlFilterDscp = _FwlFilterDscp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 15),
    _FwlFilterDscp_Type()
)
fwlFilterDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterDscp.setStatus("current")
_FwlFilterRowStatus_Type = RowStatus
_FwlFilterRowStatus_Object = MibTableColumn
fwlFilterRowStatus = _FwlFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 3, 1, 16),
    _FwlFilterRowStatus_Type()
)
fwlFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlFilterRowStatus.setStatus("current")
_FwlDefnRuleTable_Object = MibTable
fwlDefnRuleTable = _FwlDefnRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 4)
)
if mibBuilder.loadTexts:
    fwlDefnRuleTable.setStatus("current")
_FwlDefnRuleEntry_Object = MibTableRow
fwlDefnRuleEntry = _FwlDefnRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 4, 1)
)
fwlDefnRuleEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlRuleRuleName"),
)
if mibBuilder.loadTexts:
    fwlDefnRuleEntry.setStatus("current")


class _FwlRuleRuleName_Type(OctetString):
    """Custom type fwlRuleRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_FwlRuleRuleName_Type.__name__ = "OctetString"
_FwlRuleRuleName_Object = MibTableColumn
fwlRuleRuleName = _FwlRuleRuleName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 4, 1, 1),
    _FwlRuleRuleName_Type()
)
fwlRuleRuleName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlRuleRuleName.setStatus("current")
_FwlRuleFilterSet_Type = DisplayString
_FwlRuleFilterSet_Object = MibTableColumn
fwlRuleFilterSet = _FwlRuleFilterSet_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 4, 1, 2),
    _FwlRuleFilterSet_Type()
)
fwlRuleFilterSet.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlRuleFilterSet.setStatus("current")
_FwlRuleRowStatus_Type = RowStatus
_FwlRuleRowStatus_Object = MibTableColumn
fwlRuleRowStatus = _FwlRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 4, 1, 3),
    _FwlRuleRowStatus_Type()
)
fwlRuleRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlRuleRowStatus.setStatus("current")
_FwlDefnAclTable_Object = MibTable
fwlDefnAclTable = _FwlDefnAclTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5)
)
if mibBuilder.loadTexts:
    fwlDefnAclTable.setStatus("current")
_FwlDefnAclEntry_Object = MibTableRow
fwlDefnAclEntry = _FwlDefnAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5, 1)
)
fwlDefnAclEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlAclIfIndex"),
    (0, "FIREWALL-MIB", "fwlAclAclName"),
    (0, "FIREWALL-MIB", "fwlAclDirection"),
)
if mibBuilder.loadTexts:
    fwlDefnAclEntry.setStatus("current")


class _FwlAclIfIndex_Type(Integer32):
    """Custom type fwlAclIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FwlAclIfIndex_Type.__name__ = "Integer32"
_FwlAclIfIndex_Object = MibTableColumn
fwlAclIfIndex = _FwlAclIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5, 1, 1),
    _FwlAclIfIndex_Type()
)
fwlAclIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlAclIfIndex.setStatus("current")


class _FwlAclAclName_Type(OctetString):
    """Custom type fwlAclAclName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 35),
    )


_FwlAclAclName_Type.__name__ = "OctetString"
_FwlAclAclName_Object = MibTableColumn
fwlAclAclName = _FwlAclAclName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5, 1, 2),
    _FwlAclAclName_Type()
)
fwlAclAclName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlAclAclName.setStatus("current")


class _FwlAclDirection_Type(Integer32):
    """Custom type fwlAclDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_FwlAclDirection_Type.__name__ = "Integer32"
_FwlAclDirection_Object = MibTableColumn
fwlAclDirection = _FwlAclDirection_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5, 1, 3),
    _FwlAclDirection_Type()
)
fwlAclDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlAclDirection.setStatus("current")


class _FwlAclAction_Type(Integer32):
    """Custom type fwlAclAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("permit", 1),
          ("reject", 2))
    )


_FwlAclAction_Type.__name__ = "Integer32"
_FwlAclAction_Object = MibTableColumn
fwlAclAction = _FwlAclAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5, 1, 4),
    _FwlAclAction_Type()
)
fwlAclAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlAclAction.setStatus("current")


class _FwlAclSequenceNumber_Type(Integer32):
    """Custom type fwlAclSequenceNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FwlAclSequenceNumber_Type.__name__ = "Integer32"
_FwlAclSequenceNumber_Object = MibTableColumn
fwlAclSequenceNumber = _FwlAclSequenceNumber_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5, 1, 5),
    _FwlAclSequenceNumber_Type()
)
fwlAclSequenceNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlAclSequenceNumber.setStatus("current")


class _FwlAclAclType_Type(Integer32):
    """Custom type fwlAclAclType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("rule", 2))
    )


_FwlAclAclType_Type.__name__ = "Integer32"
_FwlAclAclType_Object = MibTableColumn
fwlAclAclType = _FwlAclAclType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5, 1, 6),
    _FwlAclAclType_Type()
)
fwlAclAclType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlAclAclType.setStatus("deprecated")


class _FwlAclLogTrigger_Type(Integer32):
    """Custom type fwlAclLogTrigger based on Integer32"""
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
        *(("none", 0),
          ("brief", 1),
          ("detail", 2))
    )


_FwlAclLogTrigger_Type.__name__ = "Integer32"
_FwlAclLogTrigger_Object = MibTableColumn
fwlAclLogTrigger = _FwlAclLogTrigger_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5, 1, 7),
    _FwlAclLogTrigger_Type()
)
fwlAclLogTrigger.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlAclLogTrigger.setStatus("current")


class _FwlAclFragAction_Type(Integer32):
    """Custom type fwlAclFragAction based on Integer32"""
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


_FwlAclFragAction_Type.__name__ = "Integer32"
_FwlAclFragAction_Object = MibTableColumn
fwlAclFragAction = _FwlAclFragAction_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5, 1, 8),
    _FwlAclFragAction_Type()
)
fwlAclFragAction.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlAclFragAction.setStatus("current")
_FwlAclRowStatus_Type = RowStatus
_FwlAclRowStatus_Object = MibTableColumn
fwlAclRowStatus = _FwlAclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 5, 1, 9),
    _FwlAclRowStatus_Type()
)
fwlAclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlAclRowStatus.setStatus("current")
_FwlDefnIfTable_Object = MibTable
fwlDefnIfTable = _FwlDefnIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6)
)
if mibBuilder.loadTexts:
    fwlDefnIfTable.setStatus("current")
_FwlDefnIfEntry_Object = MibTableRow
fwlDefnIfEntry = _FwlDefnIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6, 1)
)
fwlDefnIfEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlIfIfIndex"),
)
if mibBuilder.loadTexts:
    fwlDefnIfEntry.setStatus("current")


class _FwlIfIfIndex_Type(Integer32):
    """Custom type fwlIfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FwlIfIfIndex_Type.__name__ = "Integer32"
_FwlIfIfIndex_Object = MibTableColumn
fwlIfIfIndex = _FwlIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6, 1, 1),
    _FwlIfIfIndex_Type()
)
fwlIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlIfIfIndex.setStatus("current")


class _FwlIfIfType_Type(Integer32):
    """Custom type fwlIfIfType based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("internal", 1),
          ("external", 2))
    )


_FwlIfIfType_Type.__name__ = "Integer32"
_FwlIfIfType_Object = MibTableColumn
fwlIfIfType = _FwlIfIfType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6, 1, 2),
    _FwlIfIfType_Type()
)
fwlIfIfType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlIfIfType.setStatus("current")


class _FwlIfIpOptions_Type(Integer32):
    """Custom type fwlIfIpOptions based on Integer32"""
    defaultValue = 4

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
        *(("sourceRoute", 1),
          ("recordRoute", 2),
          ("timestamp", 3),
          ("anyOptions", 4),
          ("noOptions", 5),
          ("traceRoute", 6))
    )


_FwlIfIpOptions_Type.__name__ = "Integer32"
_FwlIfIpOptions_Object = MibTableColumn
fwlIfIpOptions = _FwlIfIpOptions_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6, 1, 3),
    _FwlIfIpOptions_Type()
)
fwlIfIpOptions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlIfIpOptions.setStatus("current")


class _FwlIfFragments_Type(Integer32):
    """Custom type fwlIfFragments based on Integer32"""
    defaultValue = 3

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
        *(("tinyFragment", 1),
          ("largeFragment", 2),
          ("anyFragment", 3),
          ("noFragment", 4))
    )


_FwlIfFragments_Type.__name__ = "Integer32"
_FwlIfFragments_Object = MibTableColumn
fwlIfFragments = _FwlIfFragments_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6, 1, 4),
    _FwlIfFragments_Type()
)
fwlIfFragments.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlIfFragments.setStatus("current")


class _FwlIfFragmentSize_Type(Unsigned32):
    """Custom type fwlIfFragmentSize based on Unsigned32"""
    defaultValue = 30000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65500),
    )


_FwlIfFragmentSize_Type.__name__ = "Unsigned32"
_FwlIfFragmentSize_Object = MibTableColumn
fwlIfFragmentSize = _FwlIfFragmentSize_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6, 1, 5),
    _FwlIfFragmentSize_Type()
)
fwlIfFragmentSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlIfFragmentSize.setStatus("current")


class _FwlIfICMPType_Type(Integer32):
    """Custom type fwlIfICMPType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              3,
              4,
              5,
              8,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              255)
        )
    )
    namedValues = NamedValues(
        *(("echoReply", 0),
          ("destinationUnreachable", 3),
          ("sourceQuench", 4),
          ("redirect", 5),
          ("echoRequest", 8),
          ("timeExceeded", 11),
          ("prameterProblem", 12),
          ("timestampRequest", 13),
          ("timestampReply", 14),
          ("informationRequest", 15),
          ("informationReply", 16),
          ("addressMaskRequest", 17),
          ("addressMaskReply", 18),
          ("noICMPType", 255))
    )


_FwlIfICMPType_Type.__name__ = "Integer32"
_FwlIfICMPType_Object = MibTableColumn
fwlIfICMPType = _FwlIfICMPType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6, 1, 6),
    _FwlIfICMPType_Type()
)
fwlIfICMPType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlIfICMPType.setStatus("current")


class _FwlIfICMPCode_Type(Integer32):
    """Custom type fwlIfICMPCode based on Integer32"""
    defaultValue = 255

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
              255)
        )
    )
    namedValues = NamedValues(
        *(("networkUnreachable", 0),
          ("hostUnreachable", 1),
          ("protocolUnreachable", 2),
          ("portUnreachable", 3),
          ("fragmentNeed", 4),
          ("sourceRouteFail", 5),
          ("destNetworkUnknown", 6),
          ("destHostUnknown", 7),
          ("srcHostIsolated", 8),
          ("destNetworkAdminProhibited", 9),
          ("destHostAdminProhibited", 10),
          ("networkUnreachableTOS", 11),
          ("hostUnreachableTOS", 12),
          ("noICMPCode", 255))
    )


_FwlIfICMPCode_Type.__name__ = "Integer32"
_FwlIfICMPCode_Object = MibTableColumn
fwlIfICMPCode = _FwlIfICMPCode_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6, 1, 7),
    _FwlIfICMPCode_Type()
)
fwlIfICMPCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlIfICMPCode.setStatus("deprecated")


class _FwlIfICMPv6MsgType_Type(Integer32):
    """Custom type fwlIfICMPv6MsgType based on Integer32"""
    defaultValue = 0


_FwlIfICMPv6MsgType_Type.__name__ = "Integer32"
_FwlIfICMPv6MsgType_Object = MibTableColumn
fwlIfICMPv6MsgType = _FwlIfICMPv6MsgType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6, 1, 8),
    _FwlIfICMPv6MsgType_Type()
)
fwlIfICMPv6MsgType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlIfICMPv6MsgType.setStatus("current")
_FwlIfRowStatus_Type = RowStatus
_FwlIfRowStatus_Object = MibTableColumn
fwlIfRowStatus = _FwlIfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 6, 1, 9),
    _FwlIfRowStatus_Type()
)
fwlIfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlIfRowStatus.setStatus("current")
_FwlDefnDmzTable_Object = MibTable
fwlDefnDmzTable = _FwlDefnDmzTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 7)
)
if mibBuilder.loadTexts:
    fwlDefnDmzTable.setStatus("current")
_FwlDefnDmzEntry_Object = MibTableRow
fwlDefnDmzEntry = _FwlDefnDmzEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 7, 1)
)
fwlDefnDmzEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlDmzIpIndex"),
)
if mibBuilder.loadTexts:
    fwlDefnDmzEntry.setStatus("current")
_FwlDmzIpIndex_Type = IpAddress
_FwlDmzIpIndex_Object = MibTableColumn
fwlDmzIpIndex = _FwlDmzIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 7, 1, 1),
    _FwlDmzIpIndex_Type()
)
fwlDmzIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlDmzIpIndex.setStatus("current")
_FwlDmzRowStatus_Type = RowStatus
_FwlDmzRowStatus_Object = MibTableColumn
fwlDmzRowStatus = _FwlDmzRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 7, 1, 2),
    _FwlDmzRowStatus_Type()
)
fwlDmzRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlDmzRowStatus.setStatus("current")
_FwlUrlFilterTable_Object = MibTable
fwlUrlFilterTable = _FwlUrlFilterTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 8)
)
if mibBuilder.loadTexts:
    fwlUrlFilterTable.setStatus("current")
_FwlUrlFilterEntry_Object = MibTableRow
fwlUrlFilterEntry = _FwlUrlFilterEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 8, 1)
)
fwlUrlFilterEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlUrlString"),
)
if mibBuilder.loadTexts:
    fwlUrlFilterEntry.setStatus("current")


class _FwlUrlString_Type(DisplayString):
    """Custom type fwlUrlString based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 99),
    )


_FwlUrlString_Type.__name__ = "DisplayString"
_FwlUrlString_Object = MibTableColumn
fwlUrlString = _FwlUrlString_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 8, 1, 1),
    _FwlUrlString_Type()
)
fwlUrlString.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlUrlString.setStatus("current")
_FwlUrlHitCount_Type = Counter32
_FwlUrlHitCount_Object = MibTableColumn
fwlUrlHitCount = _FwlUrlHitCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 8, 1, 2),
    _FwlUrlHitCount_Type()
)
fwlUrlHitCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlUrlHitCount.setStatus("current")
_FwlUrlFilterRowStatus_Type = RowStatus
_FwlUrlFilterRowStatus_Object = MibTableColumn
fwlUrlFilterRowStatus = _FwlUrlFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 8, 1, 3),
    _FwlUrlFilterRowStatus_Type()
)
fwlUrlFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlUrlFilterRowStatus.setStatus("current")
_FwlDefnBlkListTable_Object = MibTable
fwlDefnBlkListTable = _FwlDefnBlkListTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 9)
)
if mibBuilder.loadTexts:
    fwlDefnBlkListTable.setStatus("current")
_FwlDefnBlkListEntry_Object = MibTableRow
fwlDefnBlkListEntry = _FwlDefnBlkListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 9, 1)
)
fwlDefnBlkListEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlBlkListIpAddressType"),
    (0, "FIREWALL-MIB", "fwlBlkListIpAddress"),
    (0, "FIREWALL-MIB", "fwlBlkListIpMask"),
)
if mibBuilder.loadTexts:
    fwlDefnBlkListEntry.setStatus("current")
_FwlBlkListIpAddressType_Type = InetAddressType
_FwlBlkListIpAddressType_Object = MibTableColumn
fwlBlkListIpAddressType = _FwlBlkListIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 9, 1, 1),
    _FwlBlkListIpAddressType_Type()
)
fwlBlkListIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlBlkListIpAddressType.setStatus("current")
_FwlBlkListIpAddress_Type = InetAddress
_FwlBlkListIpAddress_Object = MibTableColumn
fwlBlkListIpAddress = _FwlBlkListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 9, 1, 2),
    _FwlBlkListIpAddress_Type()
)
fwlBlkListIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlBlkListIpAddress.setStatus("current")
_FwlBlkListIpMask_Type = InetAddressPrefixLength
_FwlBlkListIpMask_Object = MibTableColumn
fwlBlkListIpMask = _FwlBlkListIpMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 9, 1, 3),
    _FwlBlkListIpMask_Type()
)
fwlBlkListIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlBlkListIpMask.setStatus("current")
if mibBuilder.loadTexts:
    fwlBlkListIpMask.setUnits("bits")
_FwlBlkListHitsCount_Type = Counter32
_FwlBlkListHitsCount_Object = MibTableColumn
fwlBlkListHitsCount = _FwlBlkListHitsCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 9, 1, 4),
    _FwlBlkListHitsCount_Type()
)
fwlBlkListHitsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlBlkListHitsCount.setStatus("current")


class _FwlBlkListEntryType_Type(Integer32):
    """Custom type fwlBlkListEntryType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("static", 0),
          ("dynamic", 1))
    )


_FwlBlkListEntryType_Type.__name__ = "Integer32"
_FwlBlkListEntryType_Object = MibTableColumn
fwlBlkListEntryType = _FwlBlkListEntryType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 9, 1, 5),
    _FwlBlkListEntryType_Type()
)
fwlBlkListEntryType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlBlkListEntryType.setStatus("current")
_FwlBlkListRowStatus_Type = RowStatus
_FwlBlkListRowStatus_Object = MibTableColumn
fwlBlkListRowStatus = _FwlBlkListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 9, 1, 6),
    _FwlBlkListRowStatus_Type()
)
fwlBlkListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlBlkListRowStatus.setStatus("current")
_FwlDefnWhiteListTable_Object = MibTable
fwlDefnWhiteListTable = _FwlDefnWhiteListTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 10)
)
if mibBuilder.loadTexts:
    fwlDefnWhiteListTable.setStatus("current")
_FwlDefnWhiteListEntry_Object = MibTableRow
fwlDefnWhiteListEntry = _FwlDefnWhiteListEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 10, 1)
)
fwlDefnWhiteListEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlWhiteListIpAddressType"),
    (0, "FIREWALL-MIB", "fwlWhiteListIpAddress"),
    (0, "FIREWALL-MIB", "fwlWhiteListIpMask"),
)
if mibBuilder.loadTexts:
    fwlDefnWhiteListEntry.setStatus("current")
_FwlWhiteListIpAddressType_Type = InetAddressType
_FwlWhiteListIpAddressType_Object = MibTableColumn
fwlWhiteListIpAddressType = _FwlWhiteListIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 10, 1, 1),
    _FwlWhiteListIpAddressType_Type()
)
fwlWhiteListIpAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlWhiteListIpAddressType.setStatus("current")
_FwlWhiteListIpAddress_Type = InetAddress
_FwlWhiteListIpAddress_Object = MibTableColumn
fwlWhiteListIpAddress = _FwlWhiteListIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 10, 1, 2),
    _FwlWhiteListIpAddress_Type()
)
fwlWhiteListIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlWhiteListIpAddress.setStatus("current")
_FwlWhiteListIpMask_Type = InetAddressPrefixLength
_FwlWhiteListIpMask_Object = MibTableColumn
fwlWhiteListIpMask = _FwlWhiteListIpMask_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 10, 1, 3),
    _FwlWhiteListIpMask_Type()
)
fwlWhiteListIpMask.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlWhiteListIpMask.setStatus("current")
if mibBuilder.loadTexts:
    fwlWhiteListIpMask.setUnits("bits")
_FwlWhiteListHitsCount_Type = Counter32
_FwlWhiteListHitsCount_Object = MibTableColumn
fwlWhiteListHitsCount = _FwlWhiteListHitsCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 10, 1, 4),
    _FwlWhiteListHitsCount_Type()
)
fwlWhiteListHitsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlWhiteListHitsCount.setStatus("current")
_FwlWhiteListRowStatus_Type = RowStatus
_FwlWhiteListRowStatus_Object = MibTableColumn
fwlWhiteListRowStatus = _FwlWhiteListRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 10, 1, 5),
    _FwlWhiteListRowStatus_Type()
)
fwlWhiteListRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlWhiteListRowStatus.setStatus("current")
_FwlDefnIPv6DmzTable_Object = MibTable
fwlDefnIPv6DmzTable = _FwlDefnIPv6DmzTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 11)
)
if mibBuilder.loadTexts:
    fwlDefnIPv6DmzTable.setStatus("current")
_FwlDefnIPv6DmzEntry_Object = MibTableRow
fwlDefnIPv6DmzEntry = _FwlDefnIPv6DmzEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 11, 1)
)
fwlDefnIPv6DmzEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlDmzIpv6Index"),
)
if mibBuilder.loadTexts:
    fwlDefnIPv6DmzEntry.setStatus("current")
_FwlDmzAddressType_Type = InetAddressType
_FwlDmzAddressType_Object = MibTableColumn
fwlDmzAddressType = _FwlDmzAddressType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 11, 1, 1),
    _FwlDmzAddressType_Type()
)
fwlDmzAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlDmzAddressType.setStatus("current")
_FwlDmzIpv6Index_Type = InetAddress
_FwlDmzIpv6Index_Object = MibTableColumn
fwlDmzIpv6Index = _FwlDmzIpv6Index_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 11, 1, 2),
    _FwlDmzIpv6Index_Type()
)
fwlDmzIpv6Index.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlDmzIpv6Index.setStatus("current")
_FwlDmzIpv6RowStatus_Type = RowStatus
_FwlDmzIpv6RowStatus_Object = MibTableColumn
fwlDmzIpv6RowStatus = _FwlDmzIpv6RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 2, 11, 1, 3),
    _FwlDmzIpv6RowStatus_Type()
)
fwlDmzIpv6RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fwlDmzIpv6RowStatus.setStatus("current")
_FwlStatistics_ObjectIdentity = ObjectIdentity
fwlStatistics = _FwlStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3)
)
_FwlStatInspectedPacketsCount_Type = Counter32
_FwlStatInspectedPacketsCount_Object = MibScalar
fwlStatInspectedPacketsCount = _FwlStatInspectedPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 1),
    _FwlStatInspectedPacketsCount_Type()
)
fwlStatInspectedPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatInspectedPacketsCount.setStatus("current")
_FwlStatTotalPacketsDenied_Type = Counter32
_FwlStatTotalPacketsDenied_Object = MibScalar
fwlStatTotalPacketsDenied = _FwlStatTotalPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 2),
    _FwlStatTotalPacketsDenied_Type()
)
fwlStatTotalPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalPacketsDenied.setStatus("current")
_FwlStatTotalPacketsAccepted_Type = Counter32
_FwlStatTotalPacketsAccepted_Object = MibScalar
fwlStatTotalPacketsAccepted = _FwlStatTotalPacketsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 3),
    _FwlStatTotalPacketsAccepted_Type()
)
fwlStatTotalPacketsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalPacketsAccepted.setStatus("current")
_FwlStatTotalIcmpPacketsDenied_Type = Counter32
_FwlStatTotalIcmpPacketsDenied_Object = MibScalar
fwlStatTotalIcmpPacketsDenied = _FwlStatTotalIcmpPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 4),
    _FwlStatTotalIcmpPacketsDenied_Type()
)
fwlStatTotalIcmpPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalIcmpPacketsDenied.setStatus("current")
_FwlStatTotalSynPacketsDenied_Type = Counter32
_FwlStatTotalSynPacketsDenied_Object = MibScalar
fwlStatTotalSynPacketsDenied = _FwlStatTotalSynPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 5),
    _FwlStatTotalSynPacketsDenied_Type()
)
fwlStatTotalSynPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalSynPacketsDenied.setStatus("current")
_FwlStatTotalIpSpoofedPacketsDenied_Type = Counter32
_FwlStatTotalIpSpoofedPacketsDenied_Object = MibScalar
fwlStatTotalIpSpoofedPacketsDenied = _FwlStatTotalIpSpoofedPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 6),
    _FwlStatTotalIpSpoofedPacketsDenied_Type()
)
fwlStatTotalIpSpoofedPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalIpSpoofedPacketsDenied.setStatus("current")
_FwlStatTotalSrcRoutePacketsDenied_Type = Counter32
_FwlStatTotalSrcRoutePacketsDenied_Object = MibScalar
fwlStatTotalSrcRoutePacketsDenied = _FwlStatTotalSrcRoutePacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 7),
    _FwlStatTotalSrcRoutePacketsDenied_Type()
)
fwlStatTotalSrcRoutePacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalSrcRoutePacketsDenied.setStatus("current")
_FwlStatTotalTinyFragmentPacketsDenied_Type = Counter32
_FwlStatTotalTinyFragmentPacketsDenied_Object = MibScalar
fwlStatTotalTinyFragmentPacketsDenied = _FwlStatTotalTinyFragmentPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 8),
    _FwlStatTotalTinyFragmentPacketsDenied_Type()
)
fwlStatTotalTinyFragmentPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalTinyFragmentPacketsDenied.setStatus("current")
_FwlStatTotalFragmentedPacketsDenied_Type = Counter32
_FwlStatTotalFragmentedPacketsDenied_Object = MibScalar
fwlStatTotalFragmentedPacketsDenied = _FwlStatTotalFragmentedPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 9),
    _FwlStatTotalFragmentedPacketsDenied_Type()
)
fwlStatTotalFragmentedPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalFragmentedPacketsDenied.setStatus("current")
_FwlStatTotalLargeFragmentPacketsDenied_Type = Counter32
_FwlStatTotalLargeFragmentPacketsDenied_Object = MibScalar
fwlStatTotalLargeFragmentPacketsDenied = _FwlStatTotalLargeFragmentPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 10),
    _FwlStatTotalLargeFragmentPacketsDenied_Type()
)
fwlStatTotalLargeFragmentPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalLargeFragmentPacketsDenied.setStatus("current")
_FwlStatTotalIpOptionPacketsDenied_Type = Counter32
_FwlStatTotalIpOptionPacketsDenied_Object = MibScalar
fwlStatTotalIpOptionPacketsDenied = _FwlStatTotalIpOptionPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 11),
    _FwlStatTotalIpOptionPacketsDenied_Type()
)
fwlStatTotalIpOptionPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalIpOptionPacketsDenied.setStatus("current")
_FwlStatTotalAttacksPacketsDenied_Type = Counter32
_FwlStatTotalAttacksPacketsDenied_Object = MibScalar
fwlStatTotalAttacksPacketsDenied = _FwlStatTotalAttacksPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 12),
    _FwlStatTotalAttacksPacketsDenied_Type()
)
fwlStatTotalAttacksPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatTotalAttacksPacketsDenied.setStatus("current")
_FwlStatMemoryAllocationFailCount_Type = Counter32
_FwlStatMemoryAllocationFailCount_Object = MibScalar
fwlStatMemoryAllocationFailCount = _FwlStatMemoryAllocationFailCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 13),
    _FwlStatMemoryAllocationFailCount_Type()
)
fwlStatMemoryAllocationFailCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatMemoryAllocationFailCount.setStatus("current")
_FwlStatIPv6InspectedPacketsCount_Type = Counter32
_FwlStatIPv6InspectedPacketsCount_Object = MibScalar
fwlStatIPv6InspectedPacketsCount = _FwlStatIPv6InspectedPacketsCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 14),
    _FwlStatIPv6InspectedPacketsCount_Type()
)
fwlStatIPv6InspectedPacketsCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIPv6InspectedPacketsCount.setStatus("current")
_FwlStatIPv6TotalPacketsDenied_Type = Counter32
_FwlStatIPv6TotalPacketsDenied_Object = MibScalar
fwlStatIPv6TotalPacketsDenied = _FwlStatIPv6TotalPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 15),
    _FwlStatIPv6TotalPacketsDenied_Type()
)
fwlStatIPv6TotalPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIPv6TotalPacketsDenied.setStatus("current")
_FwlStatIPv6TotalPacketsAccepted_Type = Counter32
_FwlStatIPv6TotalPacketsAccepted_Object = MibScalar
fwlStatIPv6TotalPacketsAccepted = _FwlStatIPv6TotalPacketsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 16),
    _FwlStatIPv6TotalPacketsAccepted_Type()
)
fwlStatIPv6TotalPacketsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIPv6TotalPacketsAccepted.setStatus("current")
_FwlStatIPv6TotalIcmpPacketsDenied_Type = Counter32
_FwlStatIPv6TotalIcmpPacketsDenied_Object = MibScalar
fwlStatIPv6TotalIcmpPacketsDenied = _FwlStatIPv6TotalIcmpPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 17),
    _FwlStatIPv6TotalIcmpPacketsDenied_Type()
)
fwlStatIPv6TotalIcmpPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIPv6TotalIcmpPacketsDenied.setStatus("current")
_FwlStatIPv6TotalSpoofedPacketsDenied_Type = Counter32
_FwlStatIPv6TotalSpoofedPacketsDenied_Object = MibScalar
fwlStatIPv6TotalSpoofedPacketsDenied = _FwlStatIPv6TotalSpoofedPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 18),
    _FwlStatIPv6TotalSpoofedPacketsDenied_Type()
)
fwlStatIPv6TotalSpoofedPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIPv6TotalSpoofedPacketsDenied.setStatus("current")
_FwlStatIPv6TotalAttacksPacketsDenied_Type = Counter32
_FwlStatIPv6TotalAttacksPacketsDenied_Object = MibScalar
fwlStatIPv6TotalAttacksPacketsDenied = _FwlStatIPv6TotalAttacksPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 19),
    _FwlStatIPv6TotalAttacksPacketsDenied_Type()
)
fwlStatIPv6TotalAttacksPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIPv6TotalAttacksPacketsDenied.setStatus("current")
_FwlStatIfTable_Object = MibTable
fwlStatIfTable = _FwlStatIfTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20)
)
if mibBuilder.loadTexts:
    fwlStatIfTable.setStatus("current")
_FwlStatIfEntry_Object = MibTableRow
fwlStatIfEntry = _FwlStatIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1)
)
fwlStatIfEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlStatIfIfIndex"),
)
if mibBuilder.loadTexts:
    fwlStatIfEntry.setStatus("current")


class _FwlStatIfIfIndex_Type(Integer32):
    """Custom type fwlStatIfIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_FwlStatIfIfIndex_Type.__name__ = "Integer32"
_FwlStatIfIfIndex_Object = MibTableColumn
fwlStatIfIfIndex = _FwlStatIfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 1),
    _FwlStatIfIfIndex_Type()
)
fwlStatIfIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlStatIfIfIndex.setStatus("current")
_FwlStatIfFilterCount_Type = Integer32
_FwlStatIfFilterCount_Object = MibTableColumn
fwlStatIfFilterCount = _FwlStatIfFilterCount_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 2),
    _FwlStatIfFilterCount_Type()
)
fwlStatIfFilterCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfFilterCount.setStatus("current")
_FwlStatIfPacketsDenied_Type = Counter32
_FwlStatIfPacketsDenied_Object = MibTableColumn
fwlStatIfPacketsDenied = _FwlStatIfPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 3),
    _FwlStatIfPacketsDenied_Type()
)
fwlStatIfPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfPacketsDenied.setStatus("current")
_FwlStatIfPacketsAccepted_Type = Counter32
_FwlStatIfPacketsAccepted_Object = MibTableColumn
fwlStatIfPacketsAccepted = _FwlStatIfPacketsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 4),
    _FwlStatIfPacketsAccepted_Type()
)
fwlStatIfPacketsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfPacketsAccepted.setStatus("current")
_FwlStatIfSynPacketsDenied_Type = Counter32
_FwlStatIfSynPacketsDenied_Object = MibTableColumn
fwlStatIfSynPacketsDenied = _FwlStatIfSynPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 5),
    _FwlStatIfSynPacketsDenied_Type()
)
fwlStatIfSynPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfSynPacketsDenied.setStatus("current")
_FwlStatIfIcmpPacketsDenied_Type = Counter32
_FwlStatIfIcmpPacketsDenied_Object = MibTableColumn
fwlStatIfIcmpPacketsDenied = _FwlStatIfIcmpPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 6),
    _FwlStatIfIcmpPacketsDenied_Type()
)
fwlStatIfIcmpPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfIcmpPacketsDenied.setStatus("current")
_FwlStatIfIpSpoofedPacketsDenied_Type = Counter32
_FwlStatIfIpSpoofedPacketsDenied_Object = MibTableColumn
fwlStatIfIpSpoofedPacketsDenied = _FwlStatIfIpSpoofedPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 7),
    _FwlStatIfIpSpoofedPacketsDenied_Type()
)
fwlStatIfIpSpoofedPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfIpSpoofedPacketsDenied.setStatus("current")
_FwlStatIfSrcRoutePacketsDenied_Type = Counter32
_FwlStatIfSrcRoutePacketsDenied_Object = MibTableColumn
fwlStatIfSrcRoutePacketsDenied = _FwlStatIfSrcRoutePacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 8),
    _FwlStatIfSrcRoutePacketsDenied_Type()
)
fwlStatIfSrcRoutePacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfSrcRoutePacketsDenied.setStatus("current")
_FwlStatIfTinyFragmentPacketsDenied_Type = Counter32
_FwlStatIfTinyFragmentPacketsDenied_Object = MibTableColumn
fwlStatIfTinyFragmentPacketsDenied = _FwlStatIfTinyFragmentPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 9),
    _FwlStatIfTinyFragmentPacketsDenied_Type()
)
fwlStatIfTinyFragmentPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfTinyFragmentPacketsDenied.setStatus("current")
_FwlStatIfFragmentPacketsDenied_Type = Counter32
_FwlStatIfFragmentPacketsDenied_Object = MibTableColumn
fwlStatIfFragmentPacketsDenied = _FwlStatIfFragmentPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 10),
    _FwlStatIfFragmentPacketsDenied_Type()
)
fwlStatIfFragmentPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfFragmentPacketsDenied.setStatus("current")
_FwlStatIfIpOptionPacketsDenied_Type = Counter32
_FwlStatIfIpOptionPacketsDenied_Object = MibTableColumn
fwlStatIfIpOptionPacketsDenied = _FwlStatIfIpOptionPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 11),
    _FwlStatIfIpOptionPacketsDenied_Type()
)
fwlStatIfIpOptionPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfIpOptionPacketsDenied.setStatus("current")


class _FwlStatIfClear_Type(TruthValue):
    """Custom type fwlStatIfClear based on TruthValue"""
    defaultValue = 2


_FwlStatIfClear_Type.__name__ = "TruthValue"
_FwlStatIfClear_Object = MibTableColumn
fwlStatIfClear = _FwlStatIfClear_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 12),
    _FwlStatIfClear_Type()
)
fwlStatIfClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlStatIfClear.setStatus("current")


class _FwlIfTrapThreshold_Type(Integer32):
    """Custom type fwlIfTrapThreshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 50000),
    )


_FwlIfTrapThreshold_Type.__name__ = "Integer32"
_FwlIfTrapThreshold_Object = MibTableColumn
fwlIfTrapThreshold = _FwlIfTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 13),
    _FwlIfTrapThreshold_Type()
)
fwlIfTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlIfTrapThreshold.setStatus("current")
_FwlStatIfIPv6PacketsDenied_Type = Counter32
_FwlStatIfIPv6PacketsDenied_Object = MibTableColumn
fwlStatIfIPv6PacketsDenied = _FwlStatIfIPv6PacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 14),
    _FwlStatIfIPv6PacketsDenied_Type()
)
fwlStatIfIPv6PacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfIPv6PacketsDenied.setStatus("current")
_FwlStatIfIPv6PacketsAccepted_Type = Counter32
_FwlStatIfIPv6PacketsAccepted_Object = MibTableColumn
fwlStatIfIPv6PacketsAccepted = _FwlStatIfIPv6PacketsAccepted_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 15),
    _FwlStatIfIPv6PacketsAccepted_Type()
)
fwlStatIfIPv6PacketsAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfIPv6PacketsAccepted.setStatus("current")
_FwlStatIfIPv6IcmpPacketsDenied_Type = Counter32
_FwlStatIfIPv6IcmpPacketsDenied_Object = MibTableColumn
fwlStatIfIPv6IcmpPacketsDenied = _FwlStatIfIPv6IcmpPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 16),
    _FwlStatIfIPv6IcmpPacketsDenied_Type()
)
fwlStatIfIPv6IcmpPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfIPv6IcmpPacketsDenied.setStatus("current")
_FwlStatIfIPv6SpoofedPacketsDenied_Type = Counter32
_FwlStatIfIPv6SpoofedPacketsDenied_Object = MibTableColumn
fwlStatIfIPv6SpoofedPacketsDenied = _FwlStatIfIPv6SpoofedPacketsDenied_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 17),
    _FwlStatIfIPv6SpoofedPacketsDenied_Type()
)
fwlStatIfIPv6SpoofedPacketsDenied.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStatIfIPv6SpoofedPacketsDenied.setStatus("current")


class _FwlStatIfClearIPv6_Type(TruthValue):
    """Custom type fwlStatIfClearIPv6 based on TruthValue"""
    defaultValue = 2


_FwlStatIfClearIPv6_Type.__name__ = "TruthValue"
_FwlStatIfClearIPv6_Object = MibTableColumn
fwlStatIfClearIPv6 = _FwlStatIfClearIPv6_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 20, 1, 18),
    _FwlStatIfClearIPv6_Type()
)
fwlStatIfClearIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlStatIfClearIPv6.setStatus("current")


class _FwlStatClear_Type(TruthValue):
    """Custom type fwlStatClear based on TruthValue"""
    defaultValue = 2


_FwlStatClear_Type.__name__ = "TruthValue"
_FwlStatClear_Object = MibScalar
fwlStatClear = _FwlStatClear_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 21),
    _FwlStatClear_Type()
)
fwlStatClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlStatClear.setStatus("current")


class _FwlStatClearIPv6_Type(TruthValue):
    """Custom type fwlStatClearIPv6 based on TruthValue"""
    defaultValue = 2


_FwlStatClearIPv6_Type.__name__ = "TruthValue"
_FwlStatClearIPv6_Object = MibScalar
fwlStatClearIPv6 = _FwlStatClearIPv6_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 22),
    _FwlStatClearIPv6_Type()
)
fwlStatClearIPv6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlStatClearIPv6.setStatus("current")


class _FwlTrapThreshold_Type(Integer32):
    """Custom type fwlTrapThreshold based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 50000),
    )


_FwlTrapThreshold_Type.__name__ = "Integer32"
_FwlTrapThreshold_Object = MibScalar
fwlTrapThreshold = _FwlTrapThreshold_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 3, 23),
    _FwlTrapThreshold_Type()
)
fwlTrapThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlTrapThreshold.setStatus("current")
_FwlTraps_ObjectIdentity = ObjectIdentity
fwlTraps = _FwlTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4)
)
_FwlTrapTypes_ObjectIdentity = ObjectIdentity
fwlTrapTypes = _FwlTrapTypes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 0)
)
_FwlTrapControl_ObjectIdentity = ObjectIdentity
fwlTrapControl = _FwlTrapControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1)
)
_FwlTrapMemFailMessage_Type = DisplayString
_FwlTrapMemFailMessage_Object = MibScalar
fwlTrapMemFailMessage = _FwlTrapMemFailMessage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1, 1),
    _FwlTrapMemFailMessage_Type()
)
fwlTrapMemFailMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlTrapMemFailMessage.setStatus("current")
_FwlTrapAttackMessage_Type = DisplayString
_FwlTrapAttackMessage_Object = MibScalar
fwlTrapAttackMessage = _FwlTrapAttackMessage_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1, 2),
    _FwlTrapAttackMessage_Type()
)
fwlTrapAttackMessage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fwlTrapAttackMessage.setStatus("current")
_FwlIfIndex_Type = RowPointer
_FwlIfIndex_Object = MibScalar
fwlIfIndex = _FwlIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1, 3),
    _FwlIfIndex_Type()
)
fwlIfIndex.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwlIfIndex.setStatus("current")


class _FwlTrapEvent_Type(Integer32):
    """Custom type fwlTrapEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sizeexceeded", 1),
          ("sizethresholdhit", 2))
    )


_FwlTrapEvent_Type.__name__ = "Integer32"
_FwlTrapEvent_Object = MibScalar
fwlTrapEvent = _FwlTrapEvent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1, 4),
    _FwlTrapEvent_Type()
)
fwlTrapEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwlTrapEvent.setStatus("current")


class _FwlTrapEventTime_Type(DisplayString):
    """Custom type fwlTrapEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_FwlTrapEventTime_Type.__name__ = "DisplayString"
_FwlTrapEventTime_Object = MibScalar
fwlTrapEventTime = _FwlTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1, 5),
    _FwlTrapEventTime_Type()
)
fwlTrapEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwlTrapEventTime.setStatus("current")
_FwlTrapFileName_Type = DisplayString
_FwlTrapFileName_Object = MibScalar
fwlTrapFileName = _FwlTrapFileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1, 6),
    _FwlTrapFileName_Type()
)
fwlTrapFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlTrapFileName.setStatus("current")


class _FwlIdsTrapEvent_Type(Integer32):
    """Custom type fwlIdsTrapEvent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sizeexceeded", 1),
          ("sizethresholdhit", 2))
    )


_FwlIdsTrapEvent_Type.__name__ = "Integer32"
_FwlIdsTrapEvent_Object = MibScalar
fwlIdsTrapEvent = _FwlIdsTrapEvent_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1, 7),
    _FwlIdsTrapEvent_Type()
)
fwlIdsTrapEvent.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwlIdsTrapEvent.setStatus("current")


class _FwlIdsTrapEventTime_Type(DisplayString):
    """Custom type fwlIdsTrapEventTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(24, 24),
    )
    fixed_length = 24


_FwlIdsTrapEventTime_Type.__name__ = "DisplayString"
_FwlIdsTrapEventTime_Object = MibScalar
fwlIdsTrapEventTime = _FwlIdsTrapEventTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1, 8),
    _FwlIdsTrapEventTime_Type()
)
fwlIdsTrapEventTime.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwlIdsTrapEventTime.setStatus("current")
_FwlIdsTrapFileName_Type = DisplayString
_FwlIdsTrapFileName_Object = MibScalar
fwlIdsTrapFileName = _FwlIdsTrapFileName_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1, 9),
    _FwlIdsTrapFileName_Type()
)
fwlIdsTrapFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlIdsTrapFileName.setStatus("current")
_FwlIdsAttackPktIp_Type = DisplayString
_FwlIdsAttackPktIp_Object = MibScalar
fwlIdsAttackPktIp = _FwlIdsAttackPktIp_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 1, 10),
    _FwlIdsAttackPktIp_Type()
)
fwlIdsAttackPktIp.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    fwlIdsAttackPktIp.setStatus("current")
_FwlState_ObjectIdentity = ObjectIdentity
fwlState = _FwlState_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5)
)
_FwlStateTable_Object = MibTable
fwlStateTable = _FwlStateTable_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1)
)
if mibBuilder.loadTexts:
    fwlStateTable.setStatus("current")
_FwlStateEntry_Object = MibTableRow
fwlStateEntry = _FwlStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1)
)
fwlStateEntry.setIndexNames(
    (0, "FIREWALL-MIB", "fwlStateType"),
    (0, "FIREWALL-MIB", "fwlStateLocalIpAddrType"),
    (0, "FIREWALL-MIB", "fwlStateLocalIpAddress"),
    (0, "FIREWALL-MIB", "fwlStateRemoteIpAddrType"),
    (0, "FIREWALL-MIB", "fwlStateRemoteIpAddress"),
    (0, "FIREWALL-MIB", "fwlStateLocalPort"),
    (0, "FIREWALL-MIB", "fwlStateRemotePort"),
    (0, "FIREWALL-MIB", "fwlStateProtocol"),
    (0, "FIREWALL-MIB", "fwlStateDirection"),
)
if mibBuilder.loadTexts:
    fwlStateEntry.setStatus("current")


class _FwlStateType_Type(Integer32):
    """Custom type fwlStateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("stateful", 1),
          ("partialentry", 2),
          ("initflow", 3))
    )


_FwlStateType_Type.__name__ = "Integer32"
_FwlStateType_Object = MibTableColumn
fwlStateType = _FwlStateType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 1),
    _FwlStateType_Type()
)
fwlStateType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlStateType.setStatus("current")
_FwlStateLocalIpAddrType_Type = InetAddressType
_FwlStateLocalIpAddrType_Object = MibTableColumn
fwlStateLocalIpAddrType = _FwlStateLocalIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 2),
    _FwlStateLocalIpAddrType_Type()
)
fwlStateLocalIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlStateLocalIpAddrType.setStatus("current")


class _FwlStateLocalIpAddress_Type(OctetString):
    """Custom type fwlStateLocalIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_FwlStateLocalIpAddress_Type.__name__ = "OctetString"
_FwlStateLocalIpAddress_Object = MibTableColumn
fwlStateLocalIpAddress = _FwlStateLocalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 3),
    _FwlStateLocalIpAddress_Type()
)
fwlStateLocalIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlStateLocalIpAddress.setStatus("current")
_FwlStateRemoteIpAddrType_Type = InetAddressType
_FwlStateRemoteIpAddrType_Object = MibTableColumn
fwlStateRemoteIpAddrType = _FwlStateRemoteIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 4),
    _FwlStateRemoteIpAddrType_Type()
)
fwlStateRemoteIpAddrType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlStateRemoteIpAddrType.setStatus("current")


class _FwlStateRemoteIpAddress_Type(OctetString):
    """Custom type fwlStateRemoteIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_FwlStateRemoteIpAddress_Type.__name__ = "OctetString"
_FwlStateRemoteIpAddress_Object = MibTableColumn
fwlStateRemoteIpAddress = _FwlStateRemoteIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 5),
    _FwlStateRemoteIpAddress_Type()
)
fwlStateRemoteIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlStateRemoteIpAddress.setStatus("current")


class _FwlStateLocalPort_Type(Integer32):
    """Custom type fwlStateLocalPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FwlStateLocalPort_Type.__name__ = "Integer32"
_FwlStateLocalPort_Object = MibTableColumn
fwlStateLocalPort = _FwlStateLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 6),
    _FwlStateLocalPort_Type()
)
fwlStateLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlStateLocalPort.setStatus("current")


class _FwlStateRemotePort_Type(Integer32):
    """Custom type fwlStateRemotePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FwlStateRemotePort_Type.__name__ = "Integer32"
_FwlStateRemotePort_Object = MibTableColumn
fwlStateRemotePort = _FwlStateRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 7),
    _FwlStateRemotePort_Type()
)
fwlStateRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlStateRemotePort.setStatus("current")


class _FwlStateProtocol_Type(Integer32):
    """Custom type fwlStateProtocol based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_FwlStateProtocol_Type.__name__ = "Integer32"
_FwlStateProtocol_Object = MibTableColumn
fwlStateProtocol = _FwlStateProtocol_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 8),
    _FwlStateProtocol_Type()
)
fwlStateProtocol.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlStateProtocol.setStatus("current")


class _FwlStateDirection_Type(Integer32):
    """Custom type fwlStateDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("in", 1),
          ("out", 2))
    )


_FwlStateDirection_Type.__name__ = "Integer32"
_FwlStateDirection_Object = MibTableColumn
fwlStateDirection = _FwlStateDirection_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 9),
    _FwlStateDirection_Type()
)
fwlStateDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fwlStateDirection.setStatus("current")
_FwlStateEstablishedTime_Type = TimeStamp
_FwlStateEstablishedTime_Object = MibTableColumn
fwlStateEstablishedTime = _FwlStateEstablishedTime_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 10),
    _FwlStateEstablishedTime_Type()
)
fwlStateEstablishedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStateEstablishedTime.setStatus("current")


class _FwlStateLocalState_Type(Integer32):
    """Custom type fwlStateLocalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("new", 1),
          ("established", 2),
          ("related", 3),
          ("invalid", 4),
          ("listen", 10),
          ("synsent", 11),
          ("synrcvd", 12),
          ("synest", 13),
          ("finwait1", 14),
          ("finwait2", 15),
          ("closing", 16),
          ("timewait", 17),
          ("closewait", 18),
          ("lastack", 19),
          ("closed", 20))
    )


_FwlStateLocalState_Type.__name__ = "Integer32"
_FwlStateLocalState_Object = MibTableColumn
fwlStateLocalState = _FwlStateLocalState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 11),
    _FwlStateLocalState_Type()
)
fwlStateLocalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStateLocalState.setStatus("current")


class _FwlStateRemoteState_Type(Integer32):
    """Custom type fwlStateRemoteState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
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
              20)
        )
    )
    namedValues = NamedValues(
        *(("new", 1),
          ("established", 2),
          ("related", 3),
          ("invalid", 4),
          ("listen", 10),
          ("synsent", 11),
          ("synrcvd", 12),
          ("synest", 13),
          ("finwait1", 14),
          ("finwait2", 15),
          ("closing", 16),
          ("timewait", 17),
          ("closewait", 18),
          ("lastack", 19),
          ("closed", 20))
    )


_FwlStateRemoteState_Type.__name__ = "Integer32"
_FwlStateRemoteState_Object = MibTableColumn
fwlStateRemoteState = _FwlStateRemoteState_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 12),
    _FwlStateRemoteState_Type()
)
fwlStateRemoteState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStateRemoteState.setStatus("current")


class _FwlStateLogLevel_Type(Integer32):
    """Custom type fwlStateLogLevel based on Integer32"""
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
        *(("none", 0),
          ("brief", 1),
          ("detail", 2),
          ("must", 3))
    )


_FwlStateLogLevel_Type.__name__ = "Integer32"
_FwlStateLogLevel_Object = MibTableColumn
fwlStateLogLevel = _FwlStateLogLevel_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 13),
    _FwlStateLogLevel_Type()
)
fwlStateLogLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStateLogLevel.setStatus("current")


class _FwlStateCallStatus_Type(Integer32):
    """Custom type fwlStateCallStatus based on Integer32"""
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
        *(("nonsip", 0),
          ("hold", 1),
          ("unhold", 2))
    )


_FwlStateCallStatus_Type.__name__ = "Integer32"
_FwlStateCallStatus_Object = MibTableColumn
fwlStateCallStatus = _FwlStateCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 5, 1, 1, 14),
    _FwlStateCallStatus_Type()
)
fwlStateCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fwlStateCallStatus.setStatus("current")

# Managed Objects groups


# Notification objects

fwlTrapMemoryFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 0, 1)
)
fwlTrapMemoryFailure.setObjects(
    ("FIREWALL-MIB", "fwlTrapMemFailMessage")
)
if mibBuilder.loadTexts:
    fwlTrapMemoryFailure.setStatus(
        "current"
    )

fwlTrapAttackSummary = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 0, 2)
)
fwlTrapAttackSummary.setObjects(
    ("FIREWALL-MIB", "fwlTrapAttackMessage")
)
if mibBuilder.loadTexts:
    fwlTrapAttackSummary.setStatus(
        "current"
    )

fwlTrapThresholdExceeded = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 0, 3)
)
fwlTrapThresholdExceeded.setObjects(
      *(("FIREWALL-MIB", "fwlIfIndex"),
        ("FIREWALL-MIB", "fwlStatIfPacketsDenied"))
)
if mibBuilder.loadTexts:
    fwlTrapThresholdExceeded.setStatus(
        "current"
    )

fwlTrapMessage = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 0, 4)
)
fwlTrapMessage.setObjects(
      *(("FIREWALL-MIB", "fwlTrapEvent"),
        ("FIREWALL-MIB", "fwlTrapEventTime"),
        ("FIREWALL-MIB", "fwlTrapFileName"))
)
if mibBuilder.loadTexts:
    fwlTrapMessage.setStatus(
        "current"
    )

fwlIdsTrapLogging = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 0, 5)
)
fwlIdsTrapLogging.setObjects(
      *(("FIREWALL-MIB", "fwlIdsTrapEvent"),
        ("FIREWALL-MIB", "fwlIdsTrapEventTime"),
        ("FIREWALL-MIB", "fwlIdsTrapFileName"))
)
if mibBuilder.loadTexts:
    fwlIdsTrapLogging.setStatus(
        "current"
    )

fwlIdsTrapAttackPktFromIds = NotificationType(
    (1, 3, 6, 1, 4, 1, 10876, 101, 1, 16, 4, 0, 6)
)
fwlIdsTrapAttackPktFromIds.setObjects(
    ("FIREWALL-MIB", "fwlIdsAttackPktIp")
)
if mibBuilder.loadTexts:
    fwlIdsTrapAttackPktFromIds.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FIREWALL-MIB",
    **{"Status": Status,
       "ProtocolType": ProtocolType,
       "firewall": firewall,
       "fwlGlobal": fwlGlobal,
       "fwlGlobalMasterControlSwitch": fwlGlobalMasterControlSwitch,
       "fwlGlobalICMPControlSwitch": fwlGlobalICMPControlSwitch,
       "fwlGlobalIpSpoofFiltering": fwlGlobalIpSpoofFiltering,
       "fwlGlobalSrcRouteFiltering": fwlGlobalSrcRouteFiltering,
       "fwlGlobalTinyFragmentFiltering": fwlGlobalTinyFragmentFiltering,
       "fwlGlobalTcpIntercept": fwlGlobalTcpIntercept,
       "fwlGlobalTrap": fwlGlobalTrap,
       "fwlGlobalTrace": fwlGlobalTrace,
       "fwlGlobalDebug": fwlGlobalDebug,
       "fwlGlobalMaxFilters": fwlGlobalMaxFilters,
       "fwlGlobalMaxRules": fwlGlobalMaxRules,
       "fwlGlobalUrlFiltering": fwlGlobalUrlFiltering,
       "fwlGlobalNetBiosFiltering": fwlGlobalNetBiosFiltering,
       "fwlGlobalNetBiosLan2Wan": fwlGlobalNetBiosLan2Wan,
       "fwlGlobalICMPv6ControlSwitch": fwlGlobalICMPv6ControlSwitch,
       "fwlGlobalIpv6SpoofFiltering": fwlGlobalIpv6SpoofFiltering,
       "fwlGlobalLogFileSize": fwlGlobalLogFileSize,
       "fwlGlobalLogSizeThreshold": fwlGlobalLogSizeThreshold,
       "fwlGlobalIdsLogSize": fwlGlobalIdsLogSize,
       "fwlGlobalIdsLogThreshold": fwlGlobalIdsLogThreshold,
       "fwlGlobalIdsVersionInfo": fwlGlobalIdsVersionInfo,
       "fwlGlobalReloadIds": fwlGlobalReloadIds,
       "fwlGlobalIdsStatus": fwlGlobalIdsStatus,
       "fwlGlobalLoadIdsRules": fwlGlobalLoadIdsRules,
       "fwlDefinition": fwlDefinition,
       "fwlDefnTcpInterceptThreshold": fwlDefnTcpInterceptThreshold,
       "fwlDefnInterceptTimeout": fwlDefnInterceptTimeout,
       "fwlDefnFilterTable": fwlDefnFilterTable,
       "fwlDefnFilterEntry": fwlDefnFilterEntry,
       "fwlFilterFilterName": fwlFilterFilterName,
       "fwlFilterSrcAddress": fwlFilterSrcAddress,
       "fwlFilterDestAddress": fwlFilterDestAddress,
       "fwlFilterProtocol": fwlFilterProtocol,
       "fwlFilterSrcPort": fwlFilterSrcPort,
       "fwlFilterDestPort": fwlFilterDestPort,
       "fwlFilterAckBit": fwlFilterAckBit,
       "fwlFilterRstBit": fwlFilterRstBit,
       "fwlFilterTos": fwlFilterTos,
       "fwlFilterAccounting": fwlFilterAccounting,
       "fwlFilterHitClear": fwlFilterHitClear,
       "fwlFilterHitsCount": fwlFilterHitsCount,
       "fwlFilterAddrType": fwlFilterAddrType,
       "fwlFilterFlowId": fwlFilterFlowId,
       "fwlFilterDscp": fwlFilterDscp,
       "fwlFilterRowStatus": fwlFilterRowStatus,
       "fwlDefnRuleTable": fwlDefnRuleTable,
       "fwlDefnRuleEntry": fwlDefnRuleEntry,
       "fwlRuleRuleName": fwlRuleRuleName,
       "fwlRuleFilterSet": fwlRuleFilterSet,
       "fwlRuleRowStatus": fwlRuleRowStatus,
       "fwlDefnAclTable": fwlDefnAclTable,
       "fwlDefnAclEntry": fwlDefnAclEntry,
       "fwlAclIfIndex": fwlAclIfIndex,
       "fwlAclAclName": fwlAclAclName,
       "fwlAclDirection": fwlAclDirection,
       "fwlAclAction": fwlAclAction,
       "fwlAclSequenceNumber": fwlAclSequenceNumber,
       "fwlAclAclType": fwlAclAclType,
       "fwlAclLogTrigger": fwlAclLogTrigger,
       "fwlAclFragAction": fwlAclFragAction,
       "fwlAclRowStatus": fwlAclRowStatus,
       "fwlDefnIfTable": fwlDefnIfTable,
       "fwlDefnIfEntry": fwlDefnIfEntry,
       "fwlIfIfIndex": fwlIfIfIndex,
       "fwlIfIfType": fwlIfIfType,
       "fwlIfIpOptions": fwlIfIpOptions,
       "fwlIfFragments": fwlIfFragments,
       "fwlIfFragmentSize": fwlIfFragmentSize,
       "fwlIfICMPType": fwlIfICMPType,
       "fwlIfICMPCode": fwlIfICMPCode,
       "fwlIfICMPv6MsgType": fwlIfICMPv6MsgType,
       "fwlIfRowStatus": fwlIfRowStatus,
       "fwlDefnDmzTable": fwlDefnDmzTable,
       "fwlDefnDmzEntry": fwlDefnDmzEntry,
       "fwlDmzIpIndex": fwlDmzIpIndex,
       "fwlDmzRowStatus": fwlDmzRowStatus,
       "fwlUrlFilterTable": fwlUrlFilterTable,
       "fwlUrlFilterEntry": fwlUrlFilterEntry,
       "fwlUrlString": fwlUrlString,
       "fwlUrlHitCount": fwlUrlHitCount,
       "fwlUrlFilterRowStatus": fwlUrlFilterRowStatus,
       "fwlDefnBlkListTable": fwlDefnBlkListTable,
       "fwlDefnBlkListEntry": fwlDefnBlkListEntry,
       "fwlBlkListIpAddressType": fwlBlkListIpAddressType,
       "fwlBlkListIpAddress": fwlBlkListIpAddress,
       "fwlBlkListIpMask": fwlBlkListIpMask,
       "fwlBlkListHitsCount": fwlBlkListHitsCount,
       "fwlBlkListEntryType": fwlBlkListEntryType,
       "fwlBlkListRowStatus": fwlBlkListRowStatus,
       "fwlDefnWhiteListTable": fwlDefnWhiteListTable,
       "fwlDefnWhiteListEntry": fwlDefnWhiteListEntry,
       "fwlWhiteListIpAddressType": fwlWhiteListIpAddressType,
       "fwlWhiteListIpAddress": fwlWhiteListIpAddress,
       "fwlWhiteListIpMask": fwlWhiteListIpMask,
       "fwlWhiteListHitsCount": fwlWhiteListHitsCount,
       "fwlWhiteListRowStatus": fwlWhiteListRowStatus,
       "fwlDefnIPv6DmzTable": fwlDefnIPv6DmzTable,
       "fwlDefnIPv6DmzEntry": fwlDefnIPv6DmzEntry,
       "fwlDmzAddressType": fwlDmzAddressType,
       "fwlDmzIpv6Index": fwlDmzIpv6Index,
       "fwlDmzIpv6RowStatus": fwlDmzIpv6RowStatus,
       "fwlStatistics": fwlStatistics,
       "fwlStatInspectedPacketsCount": fwlStatInspectedPacketsCount,
       "fwlStatTotalPacketsDenied": fwlStatTotalPacketsDenied,
       "fwlStatTotalPacketsAccepted": fwlStatTotalPacketsAccepted,
       "fwlStatTotalIcmpPacketsDenied": fwlStatTotalIcmpPacketsDenied,
       "fwlStatTotalSynPacketsDenied": fwlStatTotalSynPacketsDenied,
       "fwlStatTotalIpSpoofedPacketsDenied": fwlStatTotalIpSpoofedPacketsDenied,
       "fwlStatTotalSrcRoutePacketsDenied": fwlStatTotalSrcRoutePacketsDenied,
       "fwlStatTotalTinyFragmentPacketsDenied": fwlStatTotalTinyFragmentPacketsDenied,
       "fwlStatTotalFragmentedPacketsDenied": fwlStatTotalFragmentedPacketsDenied,
       "fwlStatTotalLargeFragmentPacketsDenied": fwlStatTotalLargeFragmentPacketsDenied,
       "fwlStatTotalIpOptionPacketsDenied": fwlStatTotalIpOptionPacketsDenied,
       "fwlStatTotalAttacksPacketsDenied": fwlStatTotalAttacksPacketsDenied,
       "fwlStatMemoryAllocationFailCount": fwlStatMemoryAllocationFailCount,
       "fwlStatIPv6InspectedPacketsCount": fwlStatIPv6InspectedPacketsCount,
       "fwlStatIPv6TotalPacketsDenied": fwlStatIPv6TotalPacketsDenied,
       "fwlStatIPv6TotalPacketsAccepted": fwlStatIPv6TotalPacketsAccepted,
       "fwlStatIPv6TotalIcmpPacketsDenied": fwlStatIPv6TotalIcmpPacketsDenied,
       "fwlStatIPv6TotalSpoofedPacketsDenied": fwlStatIPv6TotalSpoofedPacketsDenied,
       "fwlStatIPv6TotalAttacksPacketsDenied": fwlStatIPv6TotalAttacksPacketsDenied,
       "fwlStatIfTable": fwlStatIfTable,
       "fwlStatIfEntry": fwlStatIfEntry,
       "fwlStatIfIfIndex": fwlStatIfIfIndex,
       "fwlStatIfFilterCount": fwlStatIfFilterCount,
       "fwlStatIfPacketsDenied": fwlStatIfPacketsDenied,
       "fwlStatIfPacketsAccepted": fwlStatIfPacketsAccepted,
       "fwlStatIfSynPacketsDenied": fwlStatIfSynPacketsDenied,
       "fwlStatIfIcmpPacketsDenied": fwlStatIfIcmpPacketsDenied,
       "fwlStatIfIpSpoofedPacketsDenied": fwlStatIfIpSpoofedPacketsDenied,
       "fwlStatIfSrcRoutePacketsDenied": fwlStatIfSrcRoutePacketsDenied,
       "fwlStatIfTinyFragmentPacketsDenied": fwlStatIfTinyFragmentPacketsDenied,
       "fwlStatIfFragmentPacketsDenied": fwlStatIfFragmentPacketsDenied,
       "fwlStatIfIpOptionPacketsDenied": fwlStatIfIpOptionPacketsDenied,
       "fwlStatIfClear": fwlStatIfClear,
       "fwlIfTrapThreshold": fwlIfTrapThreshold,
       "fwlStatIfIPv6PacketsDenied": fwlStatIfIPv6PacketsDenied,
       "fwlStatIfIPv6PacketsAccepted": fwlStatIfIPv6PacketsAccepted,
       "fwlStatIfIPv6IcmpPacketsDenied": fwlStatIfIPv6IcmpPacketsDenied,
       "fwlStatIfIPv6SpoofedPacketsDenied": fwlStatIfIPv6SpoofedPacketsDenied,
       "fwlStatIfClearIPv6": fwlStatIfClearIPv6,
       "fwlStatClear": fwlStatClear,
       "fwlStatClearIPv6": fwlStatClearIPv6,
       "fwlTrapThreshold": fwlTrapThreshold,
       "fwlTraps": fwlTraps,
       "fwlTrapTypes": fwlTrapTypes,
       "fwlTrapMemoryFailure": fwlTrapMemoryFailure,
       "fwlTrapAttackSummary": fwlTrapAttackSummary,
       "fwlTrapThresholdExceeded": fwlTrapThresholdExceeded,
       "fwlTrapMessage": fwlTrapMessage,
       "fwlIdsTrapLogging": fwlIdsTrapLogging,
       "fwlIdsTrapAttackPktFromIds": fwlIdsTrapAttackPktFromIds,
       "fwlTrapControl": fwlTrapControl,
       "fwlTrapMemFailMessage": fwlTrapMemFailMessage,
       "fwlTrapAttackMessage": fwlTrapAttackMessage,
       "fwlIfIndex": fwlIfIndex,
       "fwlTrapEvent": fwlTrapEvent,
       "fwlTrapEventTime": fwlTrapEventTime,
       "fwlTrapFileName": fwlTrapFileName,
       "fwlIdsTrapEvent": fwlIdsTrapEvent,
       "fwlIdsTrapEventTime": fwlIdsTrapEventTime,
       "fwlIdsTrapFileName": fwlIdsTrapFileName,
       "fwlIdsAttackPktIp": fwlIdsAttackPktIp,
       "fwlState": fwlState,
       "fwlStateTable": fwlStateTable,
       "fwlStateEntry": fwlStateEntry,
       "fwlStateType": fwlStateType,
       "fwlStateLocalIpAddrType": fwlStateLocalIpAddrType,
       "fwlStateLocalIpAddress": fwlStateLocalIpAddress,
       "fwlStateRemoteIpAddrType": fwlStateRemoteIpAddrType,
       "fwlStateRemoteIpAddress": fwlStateRemoteIpAddress,
       "fwlStateLocalPort": fwlStateLocalPort,
       "fwlStateRemotePort": fwlStateRemotePort,
       "fwlStateProtocol": fwlStateProtocol,
       "fwlStateDirection": fwlStateDirection,
       "fwlStateEstablishedTime": fwlStateEstablishedTime,
       "fwlStateLocalState": fwlStateLocalState,
       "fwlStateRemoteState": fwlStateRemoteState,
       "fwlStateLogLevel": fwlStateLogLevel,
       "fwlStateCallStatus": fwlStateCallStatus}
)
