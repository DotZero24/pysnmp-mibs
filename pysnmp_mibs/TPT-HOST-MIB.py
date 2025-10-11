# SNMP MIB module (TPT-HOST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trendmicro/TPT-HOST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:06:13 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(tpt_tpa_objs,) = mibBuilder.importSymbols(
    "TPT-TPAMIBS-MIB",
    "tpt-tpa-objs")


# MODULE-IDENTITY

tpt_host_objs = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12)
)
if mibBuilder.loadTexts:
    tpt_host_objs.setRevisions(
        ("2016-05-25 18:54",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledOrNot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 0),
          ("enabled", 1))
    )



class ActiveOrNot(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )



class IpAddressType(TextualConvention, Integer32):
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
        *(("iptypeIPv4", 1),
          ("iptypeIPv6user", 2),
          ("iptypeIPv6local", 3),
          ("iptypeIPv6auto", 4))
    )



class FipsMode(TextualConvention, Integer32):
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
        *(("disabled", 0),
          ("crypto", 1),
          ("full", 2))
    )



class ActiveCert(TextualConvention, Integer32):
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
        *(("none", 0),
          ("temporary", 1),
          ("authorized", 2))
    )



class InitState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("in-progress", 0),
          ("complete", 1))
    )



# MIB Managed Objects in the order of their OIDs

_HostIpTable_Object = MibTable
hostIpTable = _HostIpTable_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1)
)
if mibBuilder.loadTexts:
    hostIpTable.setStatus("current")
_HostIpEntry_Object = MibTableRow
hostIpEntry = _HostIpEntry_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1)
)
hostIpEntry.setIndexNames(
    (0, "TPT-HOST-MIB", "hostIpIndex"),
)
if mibBuilder.loadTexts:
    hostIpEntry.setStatus("current")
_HostIpIndex_Type = Unsigned32
_HostIpIndex_Object = MibTableColumn
hostIpIndex = _HostIpIndex_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 1),
    _HostIpIndex_Type()
)
hostIpIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hostIpIndex.setStatus("current")


class _HostIpAddress_Type(OctetString):
    """Custom type hostIpAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HostIpAddress_Type.__name__ = "OctetString"
_HostIpAddress_Object = MibTableColumn
hostIpAddress = _HostIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 2),
    _HostIpAddress_Type()
)
hostIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIpAddress.setStatus("current")
_HostIpType_Type = IpAddressType
_HostIpType_Object = MibTableColumn
hostIpType = _HostIpType_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 3),
    _HostIpType_Type()
)
hostIpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIpType.setStatus("current")
_HostIpActive_Type = ActiveOrNot
_HostIpActive_Object = MibTableColumn
hostIpActive = _HostIpActive_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 1, 1, 4),
    _HostIpActive_Type()
)
hostIpActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIpActive.setStatus("current")


class _HostIPv4Gateway_Type(OctetString):
    """Custom type hostIPv4Gateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HostIPv4Gateway_Type.__name__ = "OctetString"
_HostIPv4Gateway_Object = MibScalar
hostIPv4Gateway = _HostIPv4Gateway_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 2),
    _HostIPv4Gateway_Type()
)
hostIPv4Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIPv4Gateway.setStatus("current")


class _HostIPv6Gateway_Type(OctetString):
    """Custom type hostIPv6Gateway based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_HostIPv6Gateway_Type.__name__ = "OctetString"
_HostIPv6Gateway_Object = MibScalar
hostIPv6Gateway = _HostIPv6Gateway_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 3),
    _HostIPv6Gateway_Type()
)
hostIPv6Gateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIPv6Gateway.setStatus("current")
_HostIPv6Enabled_Type = EnabledOrNot
_HostIPv6Enabled_Object = MibScalar
hostIPv6Enabled = _HostIPv6Enabled_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 4),
    _HostIPv6Enabled_Type()
)
hostIPv6Enabled.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIPv6Enabled.setStatus("current")
_HostIPv6AutoConfig_Type = EnabledOrNot
_HostIPv6AutoConfig_Object = MibScalar
hostIPv6AutoConfig = _HostIPv6AutoConfig_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 5),
    _HostIPv6AutoConfig_Type()
)
hostIPv6AutoConfig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostIPv6AutoConfig.setStatus("current")
_HostFipsCfgMode_Type = FipsMode
_HostFipsCfgMode_Object = MibScalar
hostFipsCfgMode = _HostFipsCfgMode_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 6),
    _HostFipsCfgMode_Type()
)
hostFipsCfgMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostFipsCfgMode.setStatus("current")
_HostFipsMode_Type = FipsMode
_HostFipsMode_Object = MibScalar
hostFipsMode = _HostFipsMode_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 7),
    _HostFipsMode_Type()
)
hostFipsMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostFipsMode.setStatus("current")
_HostSSLCert_Type = ActiveCert
_HostSSLCert_Object = MibScalar
hostSSLCert = _HostSSLCert_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 8),
    _HostSSLCert_Type()
)
hostSSLCert.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostSSLCert.setStatus("current")
_HostInitState_Type = InitState
_HostInitState_Object = MibScalar
hostInitState = _HostInitState_Object(
    (1, 3, 6, 1, 4, 1, 10734, 3, 3, 2, 12, 9),
    _HostInitState_Type()
)
hostInitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hostInitState.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TPT-HOST-MIB",
    **{"EnabledOrNot": EnabledOrNot,
       "ActiveOrNot": ActiveOrNot,
       "IpAddressType": IpAddressType,
       "FipsMode": FipsMode,
       "ActiveCert": ActiveCert,
       "InitState": InitState,
       "tpt-host-objs": tpt_host_objs,
       "hostIpTable": hostIpTable,
       "hostIpEntry": hostIpEntry,
       "hostIpIndex": hostIpIndex,
       "hostIpAddress": hostIpAddress,
       "hostIpType": hostIpType,
       "hostIpActive": hostIpActive,
       "hostIPv4Gateway": hostIPv4Gateway,
       "hostIPv6Gateway": hostIPv6Gateway,
       "hostIPv6Enabled": hostIPv6Enabled,
       "hostIPv6AutoConfig": hostIPv6AutoConfig,
       "hostFipsCfgMode": hostFipsCfgMode,
       "hostFipsMode": hostFipsMode,
       "hostSSLCert": hostSSLCert,
       "hostInitState": hostInitState}
)
