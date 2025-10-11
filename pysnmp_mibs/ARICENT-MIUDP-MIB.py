# SNMP MIB module (ARICENT-MIUDP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MIUDP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:46 2025
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
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

fsMIUdpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28)
)
if mibBuilder.loadTexts:
    fsMIUdpMIB.setRevisions(
        ("2012-09-05 00:00",
         "1994-11-01 00:00",
         "1991-03-31 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIUdp_ObjectIdentity = ObjectIdentity
fsMIUdp = _FsMIUdp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1)
)
_FsMiUdpInDatagrams_Type = Counter32
_FsMiUdpInDatagrams_Object = MibScalar
fsMiUdpInDatagrams = _FsMiUdpInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 1),
    _FsMiUdpInDatagrams_Type()
)
fsMiUdpInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpInDatagrams.setStatus("current")
_FsMiUdpNoPorts_Type = Counter32
_FsMiUdpNoPorts_Object = MibScalar
fsMiUdpNoPorts = _FsMiUdpNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 2),
    _FsMiUdpNoPorts_Type()
)
fsMiUdpNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpNoPorts.setStatus("current")
_FsMiUdpInErrors_Type = Counter32
_FsMiUdpInErrors_Object = MibScalar
fsMiUdpInErrors = _FsMiUdpInErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 3),
    _FsMiUdpInErrors_Type()
)
fsMiUdpInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpInErrors.setStatus("current")
_FsMiUdpOutDatagrams_Type = Counter32
_FsMiUdpOutDatagrams_Object = MibScalar
fsMiUdpOutDatagrams = _FsMiUdpOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 4),
    _FsMiUdpOutDatagrams_Type()
)
fsMiUdpOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpOutDatagrams.setStatus("current")
_FsMiUdpInNoCksum_Type = Counter32
_FsMiUdpInNoCksum_Object = MibScalar
fsMiUdpInNoCksum = _FsMiUdpInNoCksum_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 5),
    _FsMiUdpInNoCksum_Type()
)
fsMiUdpInNoCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpInNoCksum.setStatus("current")
_FsMiUdpInIcmpErr_Type = Counter32
_FsMiUdpInIcmpErr_Object = MibScalar
fsMiUdpInIcmpErr = _FsMiUdpInIcmpErr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 6),
    _FsMiUdpInIcmpErr_Type()
)
fsMiUdpInIcmpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpInIcmpErr.setStatus("current")
_FsMiUdpInErrCksum_Type = Counter32
_FsMiUdpInErrCksum_Object = MibScalar
fsMiUdpInErrCksum = _FsMiUdpInErrCksum_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 7),
    _FsMiUdpInErrCksum_Type()
)
fsMiUdpInErrCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpInErrCksum.setStatus("current")
_FsMiUdpInBcast_Type = Counter32
_FsMiUdpInBcast_Object = MibScalar
fsMiUdpInBcast = _FsMiUdpInBcast_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 8),
    _FsMiUdpInBcast_Type()
)
fsMiUdpInBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpInBcast.setStatus("current")
_FsMiUdpHCInDatagrams_Type = Counter64
_FsMiUdpHCInDatagrams_Object = MibScalar
fsMiUdpHCInDatagrams = _FsMiUdpHCInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 9),
    _FsMiUdpHCInDatagrams_Type()
)
fsMiUdpHCInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpHCInDatagrams.setStatus("current")
_FsMiUdpHCOutDatagrams_Type = Counter64
_FsMiUdpHCOutDatagrams_Object = MibScalar
fsMiUdpHCOutDatagrams = _FsMiUdpHCOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 10),
    _FsMiUdpHCOutDatagrams_Type()
)
fsMiUdpHCOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpHCOutDatagrams.setStatus("current")
_FsMIUdpStatTable_Object = MibTable
fsMIUdpStatTable = _FsMIUdpStatTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11)
)
if mibBuilder.loadTexts:
    fsMIUdpStatTable.setStatus("current")
_FsMIUdpStatEntry_Object = MibTableRow
fsMIUdpStatEntry = _FsMIUdpStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1)
)
fsMIUdpStatEntry.setIndexNames(
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpIpvxContextId"),
)
if mibBuilder.loadTexts:
    fsMIUdpStatEntry.setStatus("current")


class _FsMiUdpIpvxContextId_Type(Integer32):
    """Custom type fsMiUdpIpvxContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_FsMiUdpIpvxContextId_Type.__name__ = "Integer32"
_FsMiUdpIpvxContextId_Object = MibTableColumn
fsMiUdpIpvxContextId = _FsMiUdpIpvxContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 1),
    _FsMiUdpIpvxContextId_Type()
)
fsMiUdpIpvxContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpIpvxContextId.setStatus("current")
_FsMiUdpIpvxInDatagrams_Type = Counter32
_FsMiUdpIpvxInDatagrams_Object = MibTableColumn
fsMiUdpIpvxInDatagrams = _FsMiUdpIpvxInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 2),
    _FsMiUdpIpvxInDatagrams_Type()
)
fsMiUdpIpvxInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxInDatagrams.setStatus("current")
_FsMiUdpIpvxNoPorts_Type = Counter32
_FsMiUdpIpvxNoPorts_Object = MibTableColumn
fsMiUdpIpvxNoPorts = _FsMiUdpIpvxNoPorts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 3),
    _FsMiUdpIpvxNoPorts_Type()
)
fsMiUdpIpvxNoPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxNoPorts.setStatus("current")
_FsMiUdpIpvxInErrors_Type = Counter32
_FsMiUdpIpvxInErrors_Object = MibTableColumn
fsMiUdpIpvxInErrors = _FsMiUdpIpvxInErrors_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 4),
    _FsMiUdpIpvxInErrors_Type()
)
fsMiUdpIpvxInErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxInErrors.setStatus("current")
_FsMiUdpIpvxOutDatagrams_Type = Counter32
_FsMiUdpIpvxOutDatagrams_Object = MibTableColumn
fsMiUdpIpvxOutDatagrams = _FsMiUdpIpvxOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 5),
    _FsMiUdpIpvxOutDatagrams_Type()
)
fsMiUdpIpvxOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxOutDatagrams.setStatus("current")
_FsMiUdpIpvxInNoCksum_Type = Counter32
_FsMiUdpIpvxInNoCksum_Object = MibTableColumn
fsMiUdpIpvxInNoCksum = _FsMiUdpIpvxInNoCksum_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 6),
    _FsMiUdpIpvxInNoCksum_Type()
)
fsMiUdpIpvxInNoCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxInNoCksum.setStatus("current")
_FsMiUdpIpvxInIcmpErr_Type = Counter32
_FsMiUdpIpvxInIcmpErr_Object = MibTableColumn
fsMiUdpIpvxInIcmpErr = _FsMiUdpIpvxInIcmpErr_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 7),
    _FsMiUdpIpvxInIcmpErr_Type()
)
fsMiUdpIpvxInIcmpErr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxInIcmpErr.setStatus("current")
_FsMiUdpIpvxInErrCksum_Type = Counter32
_FsMiUdpIpvxInErrCksum_Object = MibTableColumn
fsMiUdpIpvxInErrCksum = _FsMiUdpIpvxInErrCksum_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 8),
    _FsMiUdpIpvxInErrCksum_Type()
)
fsMiUdpIpvxInErrCksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxInErrCksum.setStatus("current")
_FsMiUdpIpvxInBcast_Type = Counter32
_FsMiUdpIpvxInBcast_Object = MibTableColumn
fsMiUdpIpvxInBcast = _FsMiUdpIpvxInBcast_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 9),
    _FsMiUdpIpvxInBcast_Type()
)
fsMiUdpIpvxInBcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxInBcast.setStatus("current")
_FsMiUdpIpvxHCInDatagrams_Type = Counter64
_FsMiUdpIpvxHCInDatagrams_Object = MibTableColumn
fsMiUdpIpvxHCInDatagrams = _FsMiUdpIpvxHCInDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 10),
    _FsMiUdpIpvxHCInDatagrams_Type()
)
fsMiUdpIpvxHCInDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxHCInDatagrams.setStatus("current")
_FsMiUdpIpvxHCOutDatagrams_Type = Counter64
_FsMiUdpIpvxHCOutDatagrams_Object = MibTableColumn
fsMiUdpIpvxHCOutDatagrams = _FsMiUdpIpvxHCOutDatagrams_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 11, 1, 11),
    _FsMiUdpIpvxHCOutDatagrams_Type()
)
fsMiUdpIpvxHCOutDatagrams.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxHCOutDatagrams.setStatus("current")
_FsMiUdpEndpointTable_Object = MibTable
fsMiUdpEndpointTable = _FsMiUdpEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 12)
)
if mibBuilder.loadTexts:
    fsMiUdpEndpointTable.setStatus("current")
_FsMiUdpEndpointEntry_Object = MibTableRow
fsMiUdpEndpointEntry = _FsMiUdpEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 12, 1)
)
fsMiUdpEndpointEntry.setIndexNames(
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpEndpointLocalAddressType"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpEndpointLocalAddress"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpEndpointLocalPort"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpEndpointRemoteAddressType"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpEndpointRemoteAddress"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpEndpointRemotePort"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpEndpointInstance"),
)
if mibBuilder.loadTexts:
    fsMiUdpEndpointEntry.setStatus("current")
_FsMiUdpEndpointLocalAddressType_Type = InetAddressType
_FsMiUdpEndpointLocalAddressType_Object = MibTableColumn
fsMiUdpEndpointLocalAddressType = _FsMiUdpEndpointLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 12, 1, 1),
    _FsMiUdpEndpointLocalAddressType_Type()
)
fsMiUdpEndpointLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpEndpointLocalAddressType.setStatus("current")


class _FsMiUdpEndpointLocalAddress_Type(InetAddress):
    """Custom type fsMiUdpEndpointLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMiUdpEndpointLocalAddress_Type.__name__ = "InetAddress"
_FsMiUdpEndpointLocalAddress_Object = MibTableColumn
fsMiUdpEndpointLocalAddress = _FsMiUdpEndpointLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 12, 1, 2),
    _FsMiUdpEndpointLocalAddress_Type()
)
fsMiUdpEndpointLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpEndpointLocalAddress.setStatus("current")
_FsMiUdpEndpointLocalPort_Type = InetPortNumber
_FsMiUdpEndpointLocalPort_Object = MibTableColumn
fsMiUdpEndpointLocalPort = _FsMiUdpEndpointLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 12, 1, 3),
    _FsMiUdpEndpointLocalPort_Type()
)
fsMiUdpEndpointLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpEndpointLocalPort.setStatus("current")
_FsMiUdpEndpointRemoteAddressType_Type = InetAddressType
_FsMiUdpEndpointRemoteAddressType_Object = MibTableColumn
fsMiUdpEndpointRemoteAddressType = _FsMiUdpEndpointRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 12, 1, 4),
    _FsMiUdpEndpointRemoteAddressType_Type()
)
fsMiUdpEndpointRemoteAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpEndpointRemoteAddressType.setStatus("current")


class _FsMiUdpEndpointRemoteAddress_Type(InetAddress):
    """Custom type fsMiUdpEndpointRemoteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMiUdpEndpointRemoteAddress_Type.__name__ = "InetAddress"
_FsMiUdpEndpointRemoteAddress_Object = MibTableColumn
fsMiUdpEndpointRemoteAddress = _FsMiUdpEndpointRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 12, 1, 5),
    _FsMiUdpEndpointRemoteAddress_Type()
)
fsMiUdpEndpointRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpEndpointRemoteAddress.setStatus("current")
_FsMiUdpEndpointRemotePort_Type = InetPortNumber
_FsMiUdpEndpointRemotePort_Object = MibTableColumn
fsMiUdpEndpointRemotePort = _FsMiUdpEndpointRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 12, 1, 6),
    _FsMiUdpEndpointRemotePort_Type()
)
fsMiUdpEndpointRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpEndpointRemotePort.setStatus("current")


class _FsMiUdpEndpointInstance_Type(Unsigned32):
    """Custom type fsMiUdpEndpointInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMiUdpEndpointInstance_Type.__name__ = "Unsigned32"
_FsMiUdpEndpointInstance_Object = MibTableColumn
fsMiUdpEndpointInstance = _FsMiUdpEndpointInstance_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 12, 1, 7),
    _FsMiUdpEndpointInstance_Type()
)
fsMiUdpEndpointInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpEndpointInstance.setStatus("current")
_FsMiUdpEndpointProcess_Type = Unsigned32
_FsMiUdpEndpointProcess_Object = MibTableColumn
fsMiUdpEndpointProcess = _FsMiUdpEndpointProcess_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 12, 1, 8),
    _FsMiUdpEndpointProcess_Type()
)
fsMiUdpEndpointProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpEndpointProcess.setStatus("current")
_FsMiUdpIpvxEndpointTable_Object = MibTable
fsMiUdpIpvxEndpointTable = _FsMiUdpIpvxEndpointTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 13)
)
if mibBuilder.loadTexts:
    fsMiUdpIpvxEndpointTable.setStatus("current")
_FsMiUdpIpvxEndpointEntry_Object = MibTableRow
fsMiUdpIpvxEndpointEntry = _FsMiUdpIpvxEndpointEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 13, 1)
)
fsMiUdpIpvxEndpointEntry.setIndexNames(
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpIpvxContextId"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpIpvxEndpointLocalAddressType"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpIpvxEndpointLocalAddress"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpIpvxEndpointLocalPort"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpIpvxEndpointRemoteAddressType"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpIpvxEndpointRemoteAddress"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpIpvxEndpointRemotePort"),
    (0, "ARICENT-MIUDP-MIB", "fsMiUdpIpvxEndpointInstance"),
)
if mibBuilder.loadTexts:
    fsMiUdpIpvxEndpointEntry.setStatus("current")
_FsMiUdpIpvxEndpointLocalAddressType_Type = InetAddressType
_FsMiUdpIpvxEndpointLocalAddressType_Object = MibTableColumn
fsMiUdpIpvxEndpointLocalAddressType = _FsMiUdpIpvxEndpointLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 13, 1, 1),
    _FsMiUdpIpvxEndpointLocalAddressType_Type()
)
fsMiUdpIpvxEndpointLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpIpvxEndpointLocalAddressType.setStatus("current")


class _FsMiUdpIpvxEndpointLocalAddress_Type(InetAddress):
    """Custom type fsMiUdpIpvxEndpointLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMiUdpIpvxEndpointLocalAddress_Type.__name__ = "InetAddress"
_FsMiUdpIpvxEndpointLocalAddress_Object = MibTableColumn
fsMiUdpIpvxEndpointLocalAddress = _FsMiUdpIpvxEndpointLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 13, 1, 2),
    _FsMiUdpIpvxEndpointLocalAddress_Type()
)
fsMiUdpIpvxEndpointLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpIpvxEndpointLocalAddress.setStatus("current")
_FsMiUdpIpvxEndpointLocalPort_Type = InetPortNumber
_FsMiUdpIpvxEndpointLocalPort_Object = MibTableColumn
fsMiUdpIpvxEndpointLocalPort = _FsMiUdpIpvxEndpointLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 13, 1, 3),
    _FsMiUdpIpvxEndpointLocalPort_Type()
)
fsMiUdpIpvxEndpointLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpIpvxEndpointLocalPort.setStatus("current")
_FsMiUdpIpvxEndpointRemoteAddressType_Type = InetAddressType
_FsMiUdpIpvxEndpointRemoteAddressType_Object = MibTableColumn
fsMiUdpIpvxEndpointRemoteAddressType = _FsMiUdpIpvxEndpointRemoteAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 13, 1, 4),
    _FsMiUdpIpvxEndpointRemoteAddressType_Type()
)
fsMiUdpIpvxEndpointRemoteAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpIpvxEndpointRemoteAddressType.setStatus("current")


class _FsMiUdpIpvxEndpointRemoteAddress_Type(InetAddress):
    """Custom type fsMiUdpIpvxEndpointRemoteAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMiUdpIpvxEndpointRemoteAddress_Type.__name__ = "InetAddress"
_FsMiUdpIpvxEndpointRemoteAddress_Object = MibTableColumn
fsMiUdpIpvxEndpointRemoteAddress = _FsMiUdpIpvxEndpointRemoteAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 13, 1, 5),
    _FsMiUdpIpvxEndpointRemoteAddress_Type()
)
fsMiUdpIpvxEndpointRemoteAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpIpvxEndpointRemoteAddress.setStatus("current")
_FsMiUdpIpvxEndpointRemotePort_Type = InetPortNumber
_FsMiUdpIpvxEndpointRemotePort_Object = MibTableColumn
fsMiUdpIpvxEndpointRemotePort = _FsMiUdpIpvxEndpointRemotePort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 13, 1, 6),
    _FsMiUdpIpvxEndpointRemotePort_Type()
)
fsMiUdpIpvxEndpointRemotePort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpIpvxEndpointRemotePort.setStatus("current")


class _FsMiUdpIpvxEndpointInstance_Type(Unsigned32):
    """Custom type fsMiUdpIpvxEndpointInstance based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMiUdpIpvxEndpointInstance_Type.__name__ = "Unsigned32"
_FsMiUdpIpvxEndpointInstance_Object = MibTableColumn
fsMiUdpIpvxEndpointInstance = _FsMiUdpIpvxEndpointInstance_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 13, 1, 7),
    _FsMiUdpIpvxEndpointInstance_Type()
)
fsMiUdpIpvxEndpointInstance.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMiUdpIpvxEndpointInstance.setStatus("current")
_FsMiUdpIpvxEndpointProcess_Type = Unsigned32
_FsMiUdpIpvxEndpointProcess_Object = MibTableColumn
fsMiUdpIpvxEndpointProcess = _FsMiUdpIpvxEndpointProcess_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 28, 1, 13, 1, 8),
    _FsMiUdpIpvxEndpointProcess_Type()
)
fsMiUdpIpvxEndpointProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMiUdpIpvxEndpointProcess.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MIUDP-MIB",
    **{"fsMIUdpMIB": fsMIUdpMIB,
       "fsMIUdp": fsMIUdp,
       "fsMiUdpInDatagrams": fsMiUdpInDatagrams,
       "fsMiUdpNoPorts": fsMiUdpNoPorts,
       "fsMiUdpInErrors": fsMiUdpInErrors,
       "fsMiUdpOutDatagrams": fsMiUdpOutDatagrams,
       "fsMiUdpInNoCksum": fsMiUdpInNoCksum,
       "fsMiUdpInIcmpErr": fsMiUdpInIcmpErr,
       "fsMiUdpInErrCksum": fsMiUdpInErrCksum,
       "fsMiUdpInBcast": fsMiUdpInBcast,
       "fsMiUdpHCInDatagrams": fsMiUdpHCInDatagrams,
       "fsMiUdpHCOutDatagrams": fsMiUdpHCOutDatagrams,
       "fsMIUdpStatTable": fsMIUdpStatTable,
       "fsMIUdpStatEntry": fsMIUdpStatEntry,
       "fsMiUdpIpvxContextId": fsMiUdpIpvxContextId,
       "fsMiUdpIpvxInDatagrams": fsMiUdpIpvxInDatagrams,
       "fsMiUdpIpvxNoPorts": fsMiUdpIpvxNoPorts,
       "fsMiUdpIpvxInErrors": fsMiUdpIpvxInErrors,
       "fsMiUdpIpvxOutDatagrams": fsMiUdpIpvxOutDatagrams,
       "fsMiUdpIpvxInNoCksum": fsMiUdpIpvxInNoCksum,
       "fsMiUdpIpvxInIcmpErr": fsMiUdpIpvxInIcmpErr,
       "fsMiUdpIpvxInErrCksum": fsMiUdpIpvxInErrCksum,
       "fsMiUdpIpvxInBcast": fsMiUdpIpvxInBcast,
       "fsMiUdpIpvxHCInDatagrams": fsMiUdpIpvxHCInDatagrams,
       "fsMiUdpIpvxHCOutDatagrams": fsMiUdpIpvxHCOutDatagrams,
       "fsMiUdpEndpointTable": fsMiUdpEndpointTable,
       "fsMiUdpEndpointEntry": fsMiUdpEndpointEntry,
       "fsMiUdpEndpointLocalAddressType": fsMiUdpEndpointLocalAddressType,
       "fsMiUdpEndpointLocalAddress": fsMiUdpEndpointLocalAddress,
       "fsMiUdpEndpointLocalPort": fsMiUdpEndpointLocalPort,
       "fsMiUdpEndpointRemoteAddressType": fsMiUdpEndpointRemoteAddressType,
       "fsMiUdpEndpointRemoteAddress": fsMiUdpEndpointRemoteAddress,
       "fsMiUdpEndpointRemotePort": fsMiUdpEndpointRemotePort,
       "fsMiUdpEndpointInstance": fsMiUdpEndpointInstance,
       "fsMiUdpEndpointProcess": fsMiUdpEndpointProcess,
       "fsMiUdpIpvxEndpointTable": fsMiUdpIpvxEndpointTable,
       "fsMiUdpIpvxEndpointEntry": fsMiUdpIpvxEndpointEntry,
       "fsMiUdpIpvxEndpointLocalAddressType": fsMiUdpIpvxEndpointLocalAddressType,
       "fsMiUdpIpvxEndpointLocalAddress": fsMiUdpIpvxEndpointLocalAddress,
       "fsMiUdpIpvxEndpointLocalPort": fsMiUdpIpvxEndpointLocalPort,
       "fsMiUdpIpvxEndpointRemoteAddressType": fsMiUdpIpvxEndpointRemoteAddressType,
       "fsMiUdpIpvxEndpointRemoteAddress": fsMiUdpIpvxEndpointRemoteAddress,
       "fsMiUdpIpvxEndpointRemotePort": fsMiUdpIpvxEndpointRemotePort,
       "fsMiUdpIpvxEndpointInstance": fsMiUdpIpvxEndpointInstance,
       "fsMiUdpIpvxEndpointProcess": fsMiUdpIpvxEndpointProcess}
)
