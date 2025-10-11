# SNMP MIB module (ELECTROLINE-COMMON-CONFIG-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/electroline/ELECTROLINE-COMMON-CONFIG-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:06:52 2025
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

(commonConfiguration,) = mibBuilder.importSymbols(
    "ELECTROLINE-COMMON-ROOT-MIB",
    "commonConfiguration")

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

_CfgTimers_ObjectIdentity = ObjectIdentity
cfgTimers = _CfgTimers_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 1)
)
if mibBuilder.loadTexts:
    cfgTimers.setStatus("current")


class _CfgCommonSnmpTimeout_Type(Integer32):
    """Custom type cfgCommonSnmpTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10080),
    )


_CfgCommonSnmpTimeout_Type.__name__ = "Integer32"
_CfgCommonSnmpTimeout_Object = MibScalar
cfgCommonSnmpTimeout = _CfgCommonSnmpTimeout_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 1, 1),
    _CfgCommonSnmpTimeout_Type()
)
cfgCommonSnmpTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCommonSnmpTimeout.setStatus("current")
_CfgIpInterfaces_ObjectIdentity = ObjectIdentity
cfgIpInterfaces = _CfgIpInterfaces_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2)
)
if mibBuilder.loadTexts:
    cfgIpInterfaces.setStatus("current")


class _CfgIpMode_Type(Integer32):
    """Custom type cfgIpMode based on Integer32"""
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


_CfgIpMode_Type.__name__ = "Integer32"
_CfgIpMode_Object = MibScalar
cfgIpMode = _CfgIpMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2, 1),
    _CfgIpMode_Type()
)
cfgIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgIpMode.setStatus("current")
_CfgCommonHmsSnmpAgent_ObjectIdentity = ObjectIdentity
cfgCommonHmsSnmpAgent = _CfgCommonHmsSnmpAgent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2, 50)
)
if mibBuilder.loadTexts:
    cfgCommonHmsSnmpAgent.setStatus("current")
_CfgCommonHmsSnmpManagerCommunity_Type = DisplayString
_CfgCommonHmsSnmpManagerCommunity_Object = MibScalar
cfgCommonHmsSnmpManagerCommunity = _CfgCommonHmsSnmpManagerCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2, 50, 1),
    _CfgCommonHmsSnmpManagerCommunity_Type()
)
cfgCommonHmsSnmpManagerCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCommonHmsSnmpManagerCommunity.setStatus("current")
_CfgCommonHmsSnmpMonitorCommunity_Type = DisplayString
_CfgCommonHmsSnmpMonitorCommunity_Object = MibScalar
cfgCommonHmsSnmpMonitorCommunity = _CfgCommonHmsSnmpMonitorCommunity_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2, 50, 2),
    _CfgCommonHmsSnmpMonitorCommunity_Type()
)
cfgCommonHmsSnmpMonitorCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCommonHmsSnmpMonitorCommunity.setStatus("current")
_CfgCommonHmsSnmpAccess_ObjectIdentity = ObjectIdentity
cfgCommonHmsSnmpAccess = _CfgCommonHmsSnmpAccess_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2, 50, 3)
)
if mibBuilder.loadTexts:
    cfgCommonHmsSnmpAccess.setStatus("current")
_CfgCommonHmsSnmpAccessTable_Object = MibTable
cfgCommonHmsSnmpAccessTable = _CfgCommonHmsSnmpAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2, 50, 3, 1)
)
if mibBuilder.loadTexts:
    cfgCommonHmsSnmpAccessTable.setStatus("current")
_CfgCommonHmsSnmpAccessEntry_Object = MibTableRow
cfgCommonHmsSnmpAccessEntry = _CfgCommonHmsSnmpAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2, 50, 3, 1, 1)
)
cfgCommonHmsSnmpAccessEntry.setIndexNames(
    (0, "ELECTROLINE-COMMON-CONFIG-MIB", "cfgCommonHmsSnmpAccessIndex"),
)
if mibBuilder.loadTexts:
    cfgCommonHmsSnmpAccessEntry.setStatus("current")
_CfgCommonHmsSnmpAccessIndex_Type = Integer32
_CfgCommonHmsSnmpAccessIndex_Object = MibTableColumn
cfgCommonHmsSnmpAccessIndex = _CfgCommonHmsSnmpAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2, 50, 3, 1, 1, 1),
    _CfgCommonHmsSnmpAccessIndex_Type()
)
cfgCommonHmsSnmpAccessIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    cfgCommonHmsSnmpAccessIndex.setStatus("current")
_CfgCommonHmsSnmpAccessIP_Type = IpAddress
_CfgCommonHmsSnmpAccessIP_Object = MibTableColumn
cfgCommonHmsSnmpAccessIP = _CfgCommonHmsSnmpAccessIP_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2, 50, 3, 1, 1, 2),
    _CfgCommonHmsSnmpAccessIP_Type()
)
cfgCommonHmsSnmpAccessIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCommonHmsSnmpAccessIP.setStatus("current")
_CfgCommonHmsSnmpAccessIPMask_Type = IpAddress
_CfgCommonHmsSnmpAccessIPMask_Object = MibTableColumn
cfgCommonHmsSnmpAccessIPMask = _CfgCommonHmsSnmpAccessIPMask_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 2, 50, 3, 1, 1, 3),
    _CfgCommonHmsSnmpAccessIPMask_Type()
)
cfgCommonHmsSnmpAccessIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgCommonHmsSnmpAccessIPMask.setStatus("current")


class _CfgVendorInfo_Type(OctetString):
    """Custom type cfgVendorInfo based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_CfgVendorInfo_Type.__name__ = "OctetString"
_CfgVendorInfo_Object = MibScalar
cfgVendorInfo = _CfgVendorInfo_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 3),
    _CfgVendorInfo_Type()
)
cfgVendorInfo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgVendorInfo.setStatus("current")


class _CfgHmsTimeReference_Type(Integer32):
    """Custom type cfgHmsTimeReference based on Integer32"""
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


_CfgHmsTimeReference_Type.__name__ = "Integer32"
_CfgHmsTimeReference_Object = MibScalar
cfgHmsTimeReference = _CfgHmsTimeReference_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 4),
    _CfgHmsTimeReference_Type()
)
cfgHmsTimeReference.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgHmsTimeReference.setStatus("current")


class _CfgResetToFactory_Type(Integer32):
    """Custom type cfgResetToFactory based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_CfgResetToFactory_Type.__name__ = "Integer32"
_CfgResetToFactory_Object = MibScalar
cfgResetToFactory = _CfgResetToFactory_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 5),
    _CfgResetToFactory_Type()
)
cfgResetToFactory.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgResetToFactory.setStatus("current")


class _CfgLocalInterfaceMode_Type(Integer32):
    """Custom type cfgLocalInterfaceMode based on Integer32"""
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


_CfgLocalInterfaceMode_Type.__name__ = "Integer32"
_CfgLocalInterfaceMode_Object = MibScalar
cfgLocalInterfaceMode = _CfgLocalInterfaceMode_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 6),
    _CfgLocalInterfaceMode_Type()
)
cfgLocalInterfaceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgLocalInterfaceMode.setStatus("current")
_CfgChannelBondingEnable_Type = TruthValue
_CfgChannelBondingEnable_Object = MibScalar
cfgChannelBondingEnable = _CfgChannelBondingEnable_Object(
    (1, 3, 6, 1, 4, 1, 5802, 1, 3, 1, 4, 2, 7),
    _CfgChannelBondingEnable_Type()
)
cfgChannelBondingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    cfgChannelBondingEnable.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELECTROLINE-COMMON-CONFIG-MIB",
    **{"cfgTimers": cfgTimers,
       "cfgCommonSnmpTimeout": cfgCommonSnmpTimeout,
       "cfgIpInterfaces": cfgIpInterfaces,
       "cfgIpMode": cfgIpMode,
       "cfgCommonHmsSnmpAgent": cfgCommonHmsSnmpAgent,
       "cfgCommonHmsSnmpManagerCommunity": cfgCommonHmsSnmpManagerCommunity,
       "cfgCommonHmsSnmpMonitorCommunity": cfgCommonHmsSnmpMonitorCommunity,
       "cfgCommonHmsSnmpAccess": cfgCommonHmsSnmpAccess,
       "cfgCommonHmsSnmpAccessTable": cfgCommonHmsSnmpAccessTable,
       "cfgCommonHmsSnmpAccessEntry": cfgCommonHmsSnmpAccessEntry,
       "cfgCommonHmsSnmpAccessIndex": cfgCommonHmsSnmpAccessIndex,
       "cfgCommonHmsSnmpAccessIP": cfgCommonHmsSnmpAccessIP,
       "cfgCommonHmsSnmpAccessIPMask": cfgCommonHmsSnmpAccessIPMask,
       "cfgVendorInfo": cfgVendorInfo,
       "cfgHmsTimeReference": cfgHmsTimeReference,
       "cfgResetToFactory": cfgResetToFactory,
       "cfgLocalInterfaceMode": cfgLocalInterfaceMode,
       "cfgChannelBondingEnable": cfgChannelBondingEnable}
)
