# SNMP MIB module (FS-IP-SLA-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-IP-SLA-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:12:56 2025
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

(pingCtlOwnerIndex,
 pingCtlTestName) = mibBuilder.importSymbols(
    "DISMAN-PING-MIB",
    "pingCtlOwnerIndex",
    "pingCtlTestName")

(fsRouterQoSMIB,) = mibBuilder.importSymbols(
    "FS-ROUTER-QOS-MIB",
    "fsRouterQoSMIB")

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(ConfigStatus,
 IfIndex) = mibBuilder.importSymbols(
    "FS-TC",
    "ConfigStatus",
    "IfIndex")

(IANAifType,) = mibBuilder.importSymbols(
    "IANAifType-MIB",
    "IANAifType")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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

(DateAndTime,
 DisplayString,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fsIpSlaMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5)
)
if mibBuilder.loadTexts:
    fsIpSlaMIB.setRevisions(
        ("2014-09-12 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsIpSlaMIBObjects_ObjectIdentity = ObjectIdentity
fsIpSlaMIBObjects = _FsIpSlaMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1)
)
_FsIpSlaResultsTable_Object = MibTable
fsIpSlaResultsTable = _FsIpSlaResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1)
)
if mibBuilder.loadTexts:
    fsIpSlaResultsTable.setStatus("current")
_FsIpSlaResultsEntry_Object = MibTableRow
fsIpSlaResultsEntry = _FsIpSlaResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1)
)
fsIpSlaResultsEntry.setIndexNames(
    (0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"),
    (0, "DISMAN-PING-MIB", "pingCtlTestName"),
)
if mibBuilder.loadTexts:
    fsIpSlaResultsEntry.setStatus("current")


class _FsIpSlaResultsOperStatus_Type(Integer32):
    """Custom type fsIpSlaResultsOperStatus based on Integer32"""
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
          ("completed", 3))
    )


_FsIpSlaResultsOperStatus_Type.__name__ = "Integer32"
_FsIpSlaResultsOperStatus_Object = MibTableColumn
fsIpSlaResultsOperStatus = _FsIpSlaResultsOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 1),
    _FsIpSlaResultsOperStatus_Type()
)
fsIpSlaResultsOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsOperStatus.setStatus("current")


class _FsIpSlaResultsIpTargetAddressType_Type(InetAddressType):
    """Custom type fsIpSlaResultsIpTargetAddressType based on InetAddressType"""
    defaultValue = 0


_FsIpSlaResultsIpTargetAddressType_Type.__name__ = "InetAddressType"
_FsIpSlaResultsIpTargetAddressType_Object = MibTableColumn
fsIpSlaResultsIpTargetAddressType = _FsIpSlaResultsIpTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 2),
    _FsIpSlaResultsIpTargetAddressType_Type()
)
fsIpSlaResultsIpTargetAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsIpTargetAddressType.setStatus("current")


class _FsIpSlaResultsIpTargetAddress_Type(InetAddress):
    """Custom type fsIpSlaResultsIpTargetAddress based on InetAddress"""
    defaultHexValue = ""


_FsIpSlaResultsIpTargetAddress_Type.__name__ = "InetAddress"
_FsIpSlaResultsIpTargetAddress_Object = MibTableColumn
fsIpSlaResultsIpTargetAddress = _FsIpSlaResultsIpTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 3),
    _FsIpSlaResultsIpTargetAddress_Type()
)
fsIpSlaResultsIpTargetAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsIpTargetAddress.setStatus("current")
_FsIpSlaResultsMaxRtt_Type = Unsigned32
_FsIpSlaResultsMaxRtt_Object = MibTableColumn
fsIpSlaResultsMaxRtt = _FsIpSlaResultsMaxRtt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 4),
    _FsIpSlaResultsMaxRtt_Type()
)
fsIpSlaResultsMaxRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsMaxRtt.setStatus("current")
if mibBuilder.loadTexts:
    fsIpSlaResultsMaxRtt.setUnits("milliseconds")
_FsIpSlaResultsMinRtt_Type = Unsigned32
_FsIpSlaResultsMinRtt_Object = MibTableColumn
fsIpSlaResultsMinRtt = _FsIpSlaResultsMinRtt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 5),
    _FsIpSlaResultsMinRtt_Type()
)
fsIpSlaResultsMinRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsMinRtt.setStatus("current")
if mibBuilder.loadTexts:
    fsIpSlaResultsMinRtt.setUnits("milliseconds")
_FsIpSlaResultsAverageRtt_Type = Unsigned32
_FsIpSlaResultsAverageRtt_Object = MibTableColumn
fsIpSlaResultsAverageRtt = _FsIpSlaResultsAverageRtt_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 6),
    _FsIpSlaResultsAverageRtt_Type()
)
fsIpSlaResultsAverageRtt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsAverageRtt.setStatus("current")
if mibBuilder.loadTexts:
    fsIpSlaResultsAverageRtt.setUnits("milliseconds")
_FsIpSlaResultsDelayJitter_Type = Unsigned32
_FsIpSlaResultsDelayJitter_Object = MibTableColumn
fsIpSlaResultsDelayJitter = _FsIpSlaResultsDelayJitter_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 7),
    _FsIpSlaResultsDelayJitter_Type()
)
fsIpSlaResultsDelayJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsDelayJitter.setStatus("current")
if mibBuilder.loadTexts:
    fsIpSlaResultsDelayJitter.setUnits("milliseconds")
_FsIpSlaResultsPktsLossRate_Type = Unsigned32
_FsIpSlaResultsPktsLossRate_Object = MibTableColumn
fsIpSlaResultsPktsLossRate = _FsIpSlaResultsPktsLossRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 8),
    _FsIpSlaResultsPktsLossRate_Type()
)
fsIpSlaResultsPktsLossRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsPktsLossRate.setStatus("current")
_FsIpSlaResultsNetworkAF_Type = Unsigned32
_FsIpSlaResultsNetworkAF_Object = MibTableColumn
fsIpSlaResultsNetworkAF = _FsIpSlaResultsNetworkAF_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 9),
    _FsIpSlaResultsNetworkAF_Type()
)
fsIpSlaResultsNetworkAF.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsNetworkAF.setStatus("current")
_FsIpSlaResultsProbeResponses_Type = Gauge32
_FsIpSlaResultsProbeResponses_Object = MibTableColumn
fsIpSlaResultsProbeResponses = _FsIpSlaResultsProbeResponses_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 10),
    _FsIpSlaResultsProbeResponses_Type()
)
fsIpSlaResultsProbeResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsProbeResponses.setStatus("current")
if mibBuilder.loadTexts:
    fsIpSlaResultsProbeResponses.setUnits("responses")
_FsIpSlaResultsSentProbes_Type = Gauge32
_FsIpSlaResultsSentProbes_Object = MibTableColumn
fsIpSlaResultsSentProbes = _FsIpSlaResultsSentProbes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 11),
    _FsIpSlaResultsSentProbes_Type()
)
fsIpSlaResultsSentProbes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsSentProbes.setStatus("current")
if mibBuilder.loadTexts:
    fsIpSlaResultsSentProbes.setUnits("probes")
_FsIpSlaResultsRttSumOfSquares_Type = Unsigned32
_FsIpSlaResultsRttSumOfSquares_Object = MibTableColumn
fsIpSlaResultsRttSumOfSquares = _FsIpSlaResultsRttSumOfSquares_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 12),
    _FsIpSlaResultsRttSumOfSquares_Type()
)
fsIpSlaResultsRttSumOfSquares.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsRttSumOfSquares.setStatus("current")
if mibBuilder.loadTexts:
    fsIpSlaResultsRttSumOfSquares.setUnits("milliseconds")
_FsIpSlaResultsLastGoodProbe_Type = DateAndTime
_FsIpSlaResultsLastGoodProbe_Object = MibTableColumn
fsIpSlaResultsLastGoodProbe = _FsIpSlaResultsLastGoodProbe_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 106, 5, 1, 1, 1, 13),
    _FsIpSlaResultsLastGoodProbe_Type()
)
fsIpSlaResultsLastGoodProbe.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsIpSlaResultsLastGoodProbe.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-IP-SLA-MIB",
    **{"fsIpSlaMIB": fsIpSlaMIB,
       "fsIpSlaMIBObjects": fsIpSlaMIBObjects,
       "fsIpSlaResultsTable": fsIpSlaResultsTable,
       "fsIpSlaResultsEntry": fsIpSlaResultsEntry,
       "fsIpSlaResultsOperStatus": fsIpSlaResultsOperStatus,
       "fsIpSlaResultsIpTargetAddressType": fsIpSlaResultsIpTargetAddressType,
       "fsIpSlaResultsIpTargetAddress": fsIpSlaResultsIpTargetAddress,
       "fsIpSlaResultsMaxRtt": fsIpSlaResultsMaxRtt,
       "fsIpSlaResultsMinRtt": fsIpSlaResultsMinRtt,
       "fsIpSlaResultsAverageRtt": fsIpSlaResultsAverageRtt,
       "fsIpSlaResultsDelayJitter": fsIpSlaResultsDelayJitter,
       "fsIpSlaResultsPktsLossRate": fsIpSlaResultsPktsLossRate,
       "fsIpSlaResultsNetworkAF": fsIpSlaResultsNetworkAF,
       "fsIpSlaResultsProbeResponses": fsIpSlaResultsProbeResponses,
       "fsIpSlaResultsSentProbes": fsIpSlaResultsSentProbes,
       "fsIpSlaResultsRttSumOfSquares": fsIpSlaResultsRttSumOfSquares,
       "fsIpSlaResultsLastGoodProbe": fsIpSlaResultsLastGoodProbe}
)
