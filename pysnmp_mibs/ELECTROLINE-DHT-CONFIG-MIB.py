# SNMP MIB module (ELECTROLINE-DHT-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-DHT-CONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:06:58 2025
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

(dhtConfiguration,) = mibBuilder.importSymbols(
    "ELECTROLINE-DHT-ROOT-MIB",
    "dhtConfiguration")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_DhtCfgGlobal_ObjectIdentity = ObjectIdentity
dhtCfgGlobal = _DhtCfgGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dhtCfgGlobal.setStatus("current")
_DhtCfgHmsEms_ObjectIdentity = ObjectIdentity
dhtCfgHmsEms = _DhtCfgHmsEms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1)
)
if mibBuilder.loadTexts:
    dhtCfgHmsEms.setStatus("current")
_CfgHmsEmsAddressTable_Object = MibTable
cfgHmsEmsAddressTable = _CfgHmsEmsAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    cfgHmsEmsAddressTable.setStatus("current")
_CfgHmsEmsAddressEntry_Object = MibTableRow
cfgHmsEmsAddressEntry = _CfgHmsEmsAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 1, 1)
)
cfgHmsEmsAddressEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-CONFIG-MIB", "cfgHmsEmsAddressIndex"),
)
if mibBuilder.loadTexts:
    cfgHmsEmsAddressEntry.setStatus("current")
_CfgHmsEmsAddressIndex_Type = Integer32
_CfgHmsEmsAddressIndex_Object = MibTableColumn
cfgHmsEmsAddressIndex = _CfgHmsEmsAddressIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 1, 1, 1),
    _CfgHmsEmsAddressIndex_Type()
)
cfgHmsEmsAddressIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgHmsEmsAddressIndex.setStatus("current")
_CfgHmsEmsAddressIP_Type = IpAddress
_CfgHmsEmsAddressIP_Object = MibTableColumn
cfgHmsEmsAddressIP = _CfgHmsEmsAddressIP_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 1, 1, 2),
    _CfgHmsEmsAddressIP_Type()
)
cfgHmsEmsAddressIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHmsEmsAddressIP.setStatus("deprecated")
_CfgHmsEmsAddressStartTrapAssurance_Type = TruthValue
_CfgHmsEmsAddressStartTrapAssurance_Object = MibTableColumn
cfgHmsEmsAddressStartTrapAssurance = _CfgHmsEmsAddressStartTrapAssurance_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 1, 1, 3),
    _CfgHmsEmsAddressStartTrapAssurance_Type()
)
cfgHmsEmsAddressStartTrapAssurance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHmsEmsAddressStartTrapAssurance.setStatus("current")
_CfgHmsEmsAddressAlarmTrapAssurance_Type = TruthValue
_CfgHmsEmsAddressAlarmTrapAssurance_Object = MibTableColumn
cfgHmsEmsAddressAlarmTrapAssurance = _CfgHmsEmsAddressAlarmTrapAssurance_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 1, 1, 4),
    _CfgHmsEmsAddressAlarmTrapAssurance_Type()
)
cfgHmsEmsAddressAlarmTrapAssurance.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHmsEmsAddressAlarmTrapAssurance.setStatus("current")


class _CfgHmsEmsAddressTrapPortNumber_Type(Integer32):
    """Custom type cfgHmsEmsAddressTrapPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_CfgHmsEmsAddressTrapPortNumber_Type.__name__ = "Integer32"
_CfgHmsEmsAddressTrapPortNumber_Object = MibTableColumn
cfgHmsEmsAddressTrapPortNumber = _CfgHmsEmsAddressTrapPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 1, 1, 5),
    _CfgHmsEmsAddressTrapPortNumber_Type()
)
cfgHmsEmsAddressTrapPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHmsEmsAddressTrapPortNumber.setStatus("current")
_CfgHmsEmsAddressTypeInet_Type = InetAddressType
_CfgHmsEmsAddressTypeInet_Object = MibTableColumn
cfgHmsEmsAddressTypeInet = _CfgHmsEmsAddressTypeInet_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 1, 1, 6),
    _CfgHmsEmsAddressTypeInet_Type()
)
cfgHmsEmsAddressTypeInet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHmsEmsAddressTypeInet.setStatus("current")
_CfgHmsEmsAddressInet_Type = InetAddress
_CfgHmsEmsAddressInet_Object = MibTableColumn
cfgHmsEmsAddressInet = _CfgHmsEmsAddressInet_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 1, 1, 7),
    _CfgHmsEmsAddressInet_Type()
)
cfgHmsEmsAddressInet.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHmsEmsAddressInet.setStatus("current")


class _CfgEmsTimeout_Type(Integer32):
    """Custom type cfgEmsTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_CfgEmsTimeout_Type.__name__ = "Integer32"
_CfgEmsTimeout_Object = MibScalar
cfgEmsTimeout = _CfgEmsTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 2),
    _CfgEmsTimeout_Type()
)
cfgEmsTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsTimeout.setStatus("current")
_CfgEmsRetry_Type = Integer32
_CfgEmsRetry_Object = MibScalar
cfgEmsRetry = _CfgEmsRetry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 3),
    _CfgEmsRetry_Type()
)
cfgEmsRetry.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsRetry.setStatus("current")


class _CfgEmsDefaultHmsProperties_Type(Integer32):
    """Custom type cfgEmsDefaultHmsProperties based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("setToDefault", 1)
    )


_CfgEmsDefaultHmsProperties_Type.__name__ = "Integer32"
_CfgEmsDefaultHmsProperties_Object = MibScalar
cfgEmsDefaultHmsProperties = _CfgEmsDefaultHmsProperties_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 4),
    _CfgEmsDefaultHmsProperties_Type()
)
cfgEmsDefaultHmsProperties.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsDefaultHmsProperties.setStatus("current")


class _CfgEmsCompatibilityMode_Type(Integer32):
    """Custom type cfgEmsCompatibilityMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("hmsMode", 0),
          ("dhtMode", 1))
    )


_CfgEmsCompatibilityMode_Type.__name__ = "Integer32"
_CfgEmsCompatibilityMode_Object = MibScalar
cfgEmsCompatibilityMode = _CfgEmsCompatibilityMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 5),
    _CfgEmsCompatibilityMode_Type()
)
cfgEmsCompatibilityMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsCompatibilityMode.setStatus("obsolete")


class _CfgEmsXpdrName_Type(OctetString):
    """Custom type cfgEmsXpdrName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CfgEmsXpdrName_Type.__name__ = "OctetString"
_CfgEmsXpdrName_Object = MibScalar
cfgEmsXpdrName = _CfgEmsXpdrName_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 6),
    _CfgEmsXpdrName_Type()
)
cfgEmsXpdrName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsXpdrName.setStatus("current")


class _CfgEmsXpdrLocation_Type(OctetString):
    """Custom type cfgEmsXpdrLocation based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CfgEmsXpdrLocation_Type.__name__ = "OctetString"
_CfgEmsXpdrLocation_Object = MibScalar
cfgEmsXpdrLocation = _CfgEmsXpdrLocation_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 7),
    _CfgEmsXpdrLocation_Type()
)
cfgEmsXpdrLocation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsXpdrLocation.setStatus("current")


class _CfgEmsXpdrDescription_Type(OctetString):
    """Custom type cfgEmsXpdrDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CfgEmsXpdrDescription_Type.__name__ = "OctetString"
_CfgEmsXpdrDescription_Object = MibScalar
cfgEmsXpdrDescription = _CfgEmsXpdrDescription_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 8),
    _CfgEmsXpdrDescription_Type()
)
cfgEmsXpdrDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsXpdrDescription.setStatus("current")


class _CfgEmsXpdrGroupPath_Type(OctetString):
    """Custom type cfgEmsXpdrGroupPath based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CfgEmsXpdrGroupPath_Type.__name__ = "OctetString"
_CfgEmsXpdrGroupPath_Object = MibScalar
cfgEmsXpdrGroupPath = _CfgEmsXpdrGroupPath_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 9),
    _CfgEmsXpdrGroupPath_Type()
)
cfgEmsXpdrGroupPath.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsXpdrGroupPath.setStatus("current")


class _CfgEmsXpdrCustomField1_Type(OctetString):
    """Custom type cfgEmsXpdrCustomField1 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CfgEmsXpdrCustomField1_Type.__name__ = "OctetString"
_CfgEmsXpdrCustomField1_Object = MibScalar
cfgEmsXpdrCustomField1 = _CfgEmsXpdrCustomField1_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 10),
    _CfgEmsXpdrCustomField1_Type()
)
cfgEmsXpdrCustomField1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsXpdrCustomField1.setStatus("current")


class _CfgEmsXpdrCustomField2_Type(OctetString):
    """Custom type cfgEmsXpdrCustomField2 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CfgEmsXpdrCustomField2_Type.__name__ = "OctetString"
_CfgEmsXpdrCustomField2_Object = MibScalar
cfgEmsXpdrCustomField2 = _CfgEmsXpdrCustomField2_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 11),
    _CfgEmsXpdrCustomField2_Type()
)
cfgEmsXpdrCustomField2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsXpdrCustomField2.setStatus("current")


class _CfgEmsXpdrCustomField3_Type(OctetString):
    """Custom type cfgEmsXpdrCustomField3 based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_CfgEmsXpdrCustomField3_Type.__name__ = "OctetString"
_CfgEmsXpdrCustomField3_Object = MibScalar
cfgEmsXpdrCustomField3 = _CfgEmsXpdrCustomField3_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 1, 12),
    _CfgEmsXpdrCustomField3_Type()
)
cfgEmsXpdrCustomField3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEmsXpdrCustomField3.setStatus("current")


class _DhtCfgResetToFactory_Type(Integer32):
    """Custom type dhtCfgResetToFactory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_DhtCfgResetToFactory_Type.__name__ = "Integer32"
_DhtCfgResetToFactory_Object = MibScalar
dhtCfgResetToFactory = _DhtCfgResetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 2),
    _DhtCfgResetToFactory_Type()
)
dhtCfgResetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtCfgResetToFactory.setStatus("deprecated")


class _DhtCfgUsbMode_Type(Integer32):
    """Custom type dhtCfgUsbMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("cpe", 1),
          ("craft", 2))
    )


_DhtCfgUsbMode_Type.__name__ = "Integer32"
_DhtCfgUsbMode_Object = MibScalar
dhtCfgUsbMode = _DhtCfgUsbMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 3),
    _DhtCfgUsbMode_Type()
)
dhtCfgUsbMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtCfgUsbMode.setStatus("deprecated")
_DhtCfgTimers_ObjectIdentity = ObjectIdentity
dhtCfgTimers = _DhtCfgTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 4)
)
if mibBuilder.loadTexts:
    dhtCfgTimers.setStatus("deprecated")


class _CfgSnmpTimeout_Type(Integer32):
    """Custom type cfgSnmpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_CfgSnmpTimeout_Type.__name__ = "Integer32"
_CfgSnmpTimeout_Object = MibScalar
cfgSnmpTimeout = _CfgSnmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 4, 1),
    _CfgSnmpTimeout_Type()
)
cfgSnmpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgSnmpTimeout.setStatus("deprecated")
_DhtCfgIpInterfaces_ObjectIdentity = ObjectIdentity
dhtCfgIpInterfaces = _DhtCfgIpInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5)
)
if mibBuilder.loadTexts:
    dhtCfgIpInterfaces.setStatus("deprecated")


class _CfgDhtIpMode_Type(Integer32):
    """Custom type cfgDhtIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("singleIp", 1),
          ("dualIp", 2))
    )


_CfgDhtIpMode_Type.__name__ = "Integer32"
_CfgDhtIpMode_Object = MibScalar
cfgDhtIpMode = _CfgDhtIpMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5, 1),
    _CfgDhtIpMode_Type()
)
cfgDhtIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgDhtIpMode.setStatus("deprecated")
_CfgHmsSnmpAgent_ObjectIdentity = ObjectIdentity
cfgHmsSnmpAgent = _CfgHmsSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5, 50)
)
if mibBuilder.loadTexts:
    cfgHmsSnmpAgent.setStatus("deprecated")
_HmsSnmpManagerCommunity_Type = DisplayString
_HmsSnmpManagerCommunity_Object = MibScalar
hmsSnmpManagerCommunity = _HmsSnmpManagerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5, 50, 1),
    _HmsSnmpManagerCommunity_Type()
)
hmsSnmpManagerCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmsSnmpManagerCommunity.setStatus("deprecated")
_HmsSnmpMonitorCommunity_Type = DisplayString
_HmsSnmpMonitorCommunity_Object = MibScalar
hmsSnmpMonitorCommunity = _HmsSnmpMonitorCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5, 50, 2),
    _HmsSnmpMonitorCommunity_Type()
)
hmsSnmpMonitorCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hmsSnmpMonitorCommunity.setStatus("deprecated")
_CfgHmsSnmpAccess_ObjectIdentity = ObjectIdentity
cfgHmsSnmpAccess = _CfgHmsSnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5, 50, 3)
)
if mibBuilder.loadTexts:
    cfgHmsSnmpAccess.setStatus("deprecated")
_CfgHmsSnmpAccessTable_Object = MibTable
cfgHmsSnmpAccessTable = _CfgHmsSnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5, 50, 3, 1)
)
if mibBuilder.loadTexts:
    cfgHmsSnmpAccessTable.setStatus("deprecated")
_CfgHmsSnmpAccessEntry_Object = MibTableRow
cfgHmsSnmpAccessEntry = _CfgHmsSnmpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5, 50, 3, 1, 1)
)
cfgHmsSnmpAccessEntry.setIndexNames(
    (0, "ELECTROLINE-DHT-CONFIG-MIB", "cfgHmsSnmpAccessIndex"),
)
if mibBuilder.loadTexts:
    cfgHmsSnmpAccessEntry.setStatus("deprecated")
_CfgHmsSnmpAccessIndex_Type = Integer32
_CfgHmsSnmpAccessIndex_Object = MibTableColumn
cfgHmsSnmpAccessIndex = _CfgHmsSnmpAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5, 50, 3, 1, 1, 1),
    _CfgHmsSnmpAccessIndex_Type()
)
cfgHmsSnmpAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgHmsSnmpAccessIndex.setStatus("deprecated")
_CfgHmsSnmpAccessIP_Type = IpAddress
_CfgHmsSnmpAccessIP_Object = MibTableColumn
cfgHmsSnmpAccessIP = _CfgHmsSnmpAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5, 50, 3, 1, 1, 2),
    _CfgHmsSnmpAccessIP_Type()
)
cfgHmsSnmpAccessIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHmsSnmpAccessIP.setStatus("deprecated")
_CfgHmsSnmpAccessIPMask_Type = IpAddress
_CfgHmsSnmpAccessIPMask_Object = MibTableColumn
cfgHmsSnmpAccessIPMask = _CfgHmsSnmpAccessIPMask_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 5, 50, 3, 1, 1, 3),
    _CfgHmsSnmpAccessIPMask_Type()
)
cfgHmsSnmpAccessIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHmsSnmpAccessIPMask.setStatus("deprecated")


class _DhtCfgVendorInfo_Type(OctetString):
    """Custom type dhtCfgVendorInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_DhtCfgVendorInfo_Type.__name__ = "OctetString"
_DhtCfgVendorInfo_Object = MibScalar
dhtCfgVendorInfo = _DhtCfgVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 6),
    _DhtCfgVendorInfo_Type()
)
dhtCfgVendorInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtCfgVendorInfo.setStatus("deprecated")


class _DhtCfgHmsTimeReference_Type(Integer32):
    """Custom type dhtCfgHmsTimeReference based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("local", 1),
          ("utc", 2))
    )


_DhtCfgHmsTimeReference_Type.__name__ = "Integer32"
_DhtCfgHmsTimeReference_Object = MibScalar
dhtCfgHmsTimeReference = _DhtCfgHmsTimeReference_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 1, 7),
    _DhtCfgHmsTimeReference_Type()
)
dhtCfgHmsTimeReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    dhtCfgHmsTimeReference.setStatus("deprecated")
_DhtCfgPowerSupply_ObjectIdentity = ObjectIdentity
dhtCfgPowerSupply = _DhtCfgPowerSupply_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dhtCfgPowerSupply.setStatus("current")
_DhtCfgBatterySave_ObjectIdentity = ObjectIdentity
dhtCfgBatterySave = _DhtCfgBatterySave_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 1)
)
if mibBuilder.loadTexts:
    dhtCfgBatterySave.setStatus("current")


class _CfgSleepVoltage_Type(Integer32):
    """Custom type cfgSleepVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1500),
    )


_CfgSleepVoltage_Type.__name__ = "Integer32"
_CfgSleepVoltage_Object = MibScalar
cfgSleepVoltage = _CfgSleepVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 1, 1),
    _CfgSleepVoltage_Type()
)
cfgSleepVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgSleepVoltage.setStatus("current")


class _CfgWakeUpDeltaVoltage_Type(Integer32):
    """Custom type cfgWakeUpDeltaVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 500),
    )


_CfgWakeUpDeltaVoltage_Type.__name__ = "Integer32"
_CfgWakeUpDeltaVoltage_Object = MibScalar
cfgWakeUpDeltaVoltage = _CfgWakeUpDeltaVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 1, 2),
    _CfgWakeUpDeltaVoltage_Type()
)
cfgWakeUpDeltaVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgWakeUpDeltaVoltage.setStatus("current")


class _CfgBatterySaveEnable_Type(Integer32):
    """Custom type cfgBatterySaveEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2),
          ("unavailable", 3))
    )


_CfgBatterySaveEnable_Type.__name__ = "Integer32"
_CfgBatterySaveEnable_Object = MibScalar
cfgBatterySaveEnable = _CfgBatterySaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 1, 3),
    _CfgBatterySaveEnable_Type()
)
cfgBatterySaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgBatterySaveEnable.setStatus("current")
_DhtCfgPsInverterTest_ObjectIdentity = ObjectIdentity
dhtCfgPsInverterTest = _DhtCfgPsInverterTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 2)
)
if mibBuilder.loadTexts:
    dhtCfgPsInverterTest.setStatus("current")


class _CfgPsInvTestAutoStopTimer_Type(Integer32):
    """Custom type cfgPsInvTestAutoStopTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 300),
    )


_CfgPsInvTestAutoStopTimer_Type.__name__ = "Integer32"
_CfgPsInvTestAutoStopTimer_Object = MibScalar
cfgPsInvTestAutoStopTimer = _CfgPsInvTestAutoStopTimer_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 2, 1),
    _CfgPsInvTestAutoStopTimer_Type()
)
cfgPsInvTestAutoStopTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPsInvTestAutoStopTimer.setStatus("current")
_DhtCfgPsSetting_ObjectIdentity = ObjectIdentity
dhtCfgPsSetting = _DhtCfgPsSetting_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 3)
)
if mibBuilder.loadTexts:
    dhtCfgPsSetting.setStatus("current")


class _CfgPsNominalInputVoltage_Type(Integer32):
    """Custom type cfgPsNominalInputVoltage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("oneHundredTwenty", 1),
          ("twoHundredFourty", 2))
    )


_CfgPsNominalInputVoltage_Type.__name__ = "Integer32"
_CfgPsNominalInputVoltage_Object = MibScalar
cfgPsNominalInputVoltage = _CfgPsNominalInputVoltage_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 3, 1),
    _CfgPsNominalInputVoltage_Type()
)
cfgPsNominalInputVoltage.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPsNominalInputVoltage.setStatus("current")
_CfgPsTemperatureCalibrationOffset_Type = Integer32
_CfgPsTemperatureCalibrationOffset_Object = MibScalar
cfgPsTemperatureCalibrationOffset = _CfgPsTemperatureCalibrationOffset_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 3, 2),
    _CfgPsTemperatureCalibrationOffset_Type()
)
cfgPsTemperatureCalibrationOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPsTemperatureCalibrationOffset.setStatus("current")


class _CfgPsOutputCurrent_Type(Integer32):
    """Custom type cfgPsOutputCurrent based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("high", 2))
    )


_CfgPsOutputCurrent_Type.__name__ = "Integer32"
_CfgPsOutputCurrent_Object = MibScalar
cfgPsOutputCurrent = _CfgPsOutputCurrent_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 3, 3),
    _CfgPsOutputCurrent_Type()
)
cfgPsOutputCurrent.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPsOutputCurrent.setStatus("current")
_DhtCfgUsmUnified_ObjectIdentity = ObjectIdentity
dhtCfgUsmUnified = _DhtCfgUsmUnified_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 3, 4)
)
if mibBuilder.loadTexts:
    dhtCfgUsmUnified.setStatus("current")


class _CfgUsmUnifiedMode_Type(Integer32):
    """Custom type cfgUsmUnifiedMode based on Integer32"""
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
        *(("auto", 1),
          ("usm", 2),
          ("usm2", 3),
          ("usm25", 4),
          ("apcSm7WithInputCurrent", 5),
          ("apcSm7WithoutInputCurrent", 6))
    )


_CfgUsmUnifiedMode_Type.__name__ = "Integer32"
_CfgUsmUnifiedMode_Object = MibScalar
cfgUsmUnifiedMode = _CfgUsmUnifiedMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 3, 4, 1),
    _CfgUsmUnifiedMode_Type()
)
cfgUsmUnifiedMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgUsmUnifiedMode.setStatus("current")
_CfgPsGenericCreation_Type = TruthValue
_CfgPsGenericCreation_Object = MibScalar
cfgPsGenericCreation = _CfgPsGenericCreation_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 3, 5),
    _CfgPsGenericCreation_Type()
)
cfgPsGenericCreation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPsGenericCreation.setStatus("current")


class _CfgPsMeasurementSource_Type(Integer32):
    """Custom type cfgPsMeasurementSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("analogPort", 1),
          ("communicationPort", 2))
    )


_CfgPsMeasurementSource_Type.__name__ = "Integer32"
_CfgPsMeasurementSource_Object = MibScalar
cfgPsMeasurementSource = _CfgPsMeasurementSource_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 2, 3, 6),
    _CfgPsMeasurementSource_Type()
)
cfgPsMeasurementSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgPsMeasurementSource.setStatus("current")
_DhtCfgHMS022_ObjectIdentity = ObjectIdentity
dhtCfgHMS022 = _DhtCfgHMS022_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 3)
)
if mibBuilder.loadTexts:
    dhtCfgHMS022.setStatus("current")


class _CfgStartAddress_Type(Integer32):
    """Custom type cfgStartAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CfgStartAddress_Type.__name__ = "Integer32"
_CfgStartAddress_Object = MibScalar
cfgStartAddress = _CfgStartAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 3, 1),
    _CfgStartAddress_Type()
)
cfgStartAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgStartAddress.setStatus("current")


class _CfgEndAddress_Type(Integer32):
    """Custom type cfgEndAddress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 31),
    )


_CfgEndAddress_Type.__name__ = "Integer32"
_CfgEndAddress_Object = MibScalar
cfgEndAddress = _CfgEndAddress_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 2, 2, 3, 2),
    _CfgEndAddress_Type()
)
cfgEndAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgEndAddress.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-DHT-CONFIG-MIB",
    **{"dhtCfgGlobal": dhtCfgGlobal,
       "dhtCfgHmsEms": dhtCfgHmsEms,
       "cfgHmsEmsAddressTable": cfgHmsEmsAddressTable,
       "cfgHmsEmsAddressEntry": cfgHmsEmsAddressEntry,
       "cfgHmsEmsAddressIndex": cfgHmsEmsAddressIndex,
       "cfgHmsEmsAddressIP": cfgHmsEmsAddressIP,
       "cfgHmsEmsAddressStartTrapAssurance": cfgHmsEmsAddressStartTrapAssurance,
       "cfgHmsEmsAddressAlarmTrapAssurance": cfgHmsEmsAddressAlarmTrapAssurance,
       "cfgHmsEmsAddressTrapPortNumber": cfgHmsEmsAddressTrapPortNumber,
       "cfgHmsEmsAddressTypeInet": cfgHmsEmsAddressTypeInet,
       "cfgHmsEmsAddressInet": cfgHmsEmsAddressInet,
       "cfgEmsTimeout": cfgEmsTimeout,
       "cfgEmsRetry": cfgEmsRetry,
       "cfgEmsDefaultHmsProperties": cfgEmsDefaultHmsProperties,
       "cfgEmsCompatibilityMode": cfgEmsCompatibilityMode,
       "cfgEmsXpdrName": cfgEmsXpdrName,
       "cfgEmsXpdrLocation": cfgEmsXpdrLocation,
       "cfgEmsXpdrDescription": cfgEmsXpdrDescription,
       "cfgEmsXpdrGroupPath": cfgEmsXpdrGroupPath,
       "cfgEmsXpdrCustomField1": cfgEmsXpdrCustomField1,
       "cfgEmsXpdrCustomField2": cfgEmsXpdrCustomField2,
       "cfgEmsXpdrCustomField3": cfgEmsXpdrCustomField3,
       "dhtCfgResetToFactory": dhtCfgResetToFactory,
       "dhtCfgUsbMode": dhtCfgUsbMode,
       "dhtCfgTimers": dhtCfgTimers,
       "cfgSnmpTimeout": cfgSnmpTimeout,
       "dhtCfgIpInterfaces": dhtCfgIpInterfaces,
       "cfgDhtIpMode": cfgDhtIpMode,
       "cfgHmsSnmpAgent": cfgHmsSnmpAgent,
       "hmsSnmpManagerCommunity": hmsSnmpManagerCommunity,
       "hmsSnmpMonitorCommunity": hmsSnmpMonitorCommunity,
       "cfgHmsSnmpAccess": cfgHmsSnmpAccess,
       "cfgHmsSnmpAccessTable": cfgHmsSnmpAccessTable,
       "cfgHmsSnmpAccessEntry": cfgHmsSnmpAccessEntry,
       "cfgHmsSnmpAccessIndex": cfgHmsSnmpAccessIndex,
       "cfgHmsSnmpAccessIP": cfgHmsSnmpAccessIP,
       "cfgHmsSnmpAccessIPMask": cfgHmsSnmpAccessIPMask,
       "dhtCfgVendorInfo": dhtCfgVendorInfo,
       "dhtCfgHmsTimeReference": dhtCfgHmsTimeReference,
       "dhtCfgPowerSupply": dhtCfgPowerSupply,
       "dhtCfgBatterySave": dhtCfgBatterySave,
       "cfgSleepVoltage": cfgSleepVoltage,
       "cfgWakeUpDeltaVoltage": cfgWakeUpDeltaVoltage,
       "cfgBatterySaveEnable": cfgBatterySaveEnable,
       "dhtCfgPsInverterTest": dhtCfgPsInverterTest,
       "cfgPsInvTestAutoStopTimer": cfgPsInvTestAutoStopTimer,
       "dhtCfgPsSetting": dhtCfgPsSetting,
       "cfgPsNominalInputVoltage": cfgPsNominalInputVoltage,
       "cfgPsTemperatureCalibrationOffset": cfgPsTemperatureCalibrationOffset,
       "cfgPsOutputCurrent": cfgPsOutputCurrent,
       "dhtCfgUsmUnified": dhtCfgUsmUnified,
       "cfgUsmUnifiedMode": cfgUsmUnifiedMode,
       "cfgPsGenericCreation": cfgPsGenericCreation,
       "cfgPsMeasurementSource": cfgPsMeasurementSource,
       "dhtCfgHMS022": dhtCfgHMS022,
       "cfgStartAddress": cfgStartAddress,
       "cfgEndAddress": cfgEndAddress}
)
