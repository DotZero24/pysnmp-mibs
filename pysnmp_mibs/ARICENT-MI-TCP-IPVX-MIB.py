# SNMP MIB module (ARICENT-MI-TCP-IPVX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-MI-TCP-IPVX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:43:47 2025
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

fsMIStdTcpIpvx = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsMIStdContextTable_Object = MibTable
fsMIStdContextTable = _FsMIStdContextTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1)
)
if mibBuilder.loadTexts:
    fsMIStdContextTable.setStatus("current")
_FsMIStdContextEntry_Object = MibTableRow
fsMIStdContextEntry = _FsMIStdContextEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1)
)
fsMIStdContextEntry.setIndexNames(
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdContextId"),
)
if mibBuilder.loadTexts:
    fsMIStdContextEntry.setStatus("current")


class _FsMIStdContextId_Type(Integer32):
    """Custom type fsMIStdContextId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_FsMIStdContextId_Type.__name__ = "Integer32"
_FsMIStdContextId_Object = MibTableColumn
fsMIStdContextId = _FsMIStdContextId_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 1),
    _FsMIStdContextId_Type()
)
fsMIStdContextId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdContextId.setStatus("current")


class _FsMIStdTcpRtoAlgorithm_Type(Integer32):
    """Custom type fsMIStdTcpRtoAlgorithm based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("constant", 2),
          ("rsre", 3),
          ("vanj", 4),
          ("rfc2988", 5))
    )


_FsMIStdTcpRtoAlgorithm_Type.__name__ = "Integer32"
_FsMIStdTcpRtoAlgorithm_Object = MibTableColumn
fsMIStdTcpRtoAlgorithm = _FsMIStdTcpRtoAlgorithm_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 2),
    _FsMIStdTcpRtoAlgorithm_Type()
)
fsMIStdTcpRtoAlgorithm.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpRtoAlgorithm.setStatus("current")


class _FsMIStdTcpRtoMin_Type(Integer32):
    """Custom type fsMIStdTcpRtoMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIStdTcpRtoMin_Type.__name__ = "Integer32"
_FsMIStdTcpRtoMin_Object = MibTableColumn
fsMIStdTcpRtoMin = _FsMIStdTcpRtoMin_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 3),
    _FsMIStdTcpRtoMin_Type()
)
fsMIStdTcpRtoMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpRtoMin.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdTcpRtoMin.setUnits("milliseconds")


class _FsMIStdTcpRtoMax_Type(Integer32):
    """Custom type fsMIStdTcpRtoMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIStdTcpRtoMax_Type.__name__ = "Integer32"
_FsMIStdTcpRtoMax_Object = MibTableColumn
fsMIStdTcpRtoMax = _FsMIStdTcpRtoMax_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 4),
    _FsMIStdTcpRtoMax_Type()
)
fsMIStdTcpRtoMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpRtoMax.setStatus("current")
if mibBuilder.loadTexts:
    fsMIStdTcpRtoMax.setUnits("milliseconds")


class _FsMIStdTcpMaxConn_Type(Integer32):
    """Custom type fsMIStdTcpMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, -1),
        ValueRangeConstraint(0, 2147483647),
    )


_FsMIStdTcpMaxConn_Type.__name__ = "Integer32"
_FsMIStdTcpMaxConn_Object = MibTableColumn
fsMIStdTcpMaxConn = _FsMIStdTcpMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 5),
    _FsMIStdTcpMaxConn_Type()
)
fsMIStdTcpMaxConn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpMaxConn.setStatus("current")
_FsMIStdTcpActiveOpens_Type = Counter32
_FsMIStdTcpActiveOpens_Object = MibTableColumn
fsMIStdTcpActiveOpens = _FsMIStdTcpActiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 6),
    _FsMIStdTcpActiveOpens_Type()
)
fsMIStdTcpActiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpActiveOpens.setStatus("current")
_FsMIStdTcpPassiveOpens_Type = Counter32
_FsMIStdTcpPassiveOpens_Object = MibTableColumn
fsMIStdTcpPassiveOpens = _FsMIStdTcpPassiveOpens_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 7),
    _FsMIStdTcpPassiveOpens_Type()
)
fsMIStdTcpPassiveOpens.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpPassiveOpens.setStatus("current")
_FsMIStdTcpAttemptFails_Type = Counter32
_FsMIStdTcpAttemptFails_Object = MibTableColumn
fsMIStdTcpAttemptFails = _FsMIStdTcpAttemptFails_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 8),
    _FsMIStdTcpAttemptFails_Type()
)
fsMIStdTcpAttemptFails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpAttemptFails.setStatus("current")
_FsMIStdTcpEstabResets_Type = Counter32
_FsMIStdTcpEstabResets_Object = MibTableColumn
fsMIStdTcpEstabResets = _FsMIStdTcpEstabResets_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 9),
    _FsMIStdTcpEstabResets_Type()
)
fsMIStdTcpEstabResets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpEstabResets.setStatus("current")
_FsMIStdTcpCurrEstab_Type = Gauge32
_FsMIStdTcpCurrEstab_Object = MibTableColumn
fsMIStdTcpCurrEstab = _FsMIStdTcpCurrEstab_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 10),
    _FsMIStdTcpCurrEstab_Type()
)
fsMIStdTcpCurrEstab.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpCurrEstab.setStatus("current")
_FsMIStdTcpInSegs_Type = Counter32
_FsMIStdTcpInSegs_Object = MibTableColumn
fsMIStdTcpInSegs = _FsMIStdTcpInSegs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 11),
    _FsMIStdTcpInSegs_Type()
)
fsMIStdTcpInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpInSegs.setStatus("current")
_FsMIStdTcpOutSegs_Type = Counter32
_FsMIStdTcpOutSegs_Object = MibTableColumn
fsMIStdTcpOutSegs = _FsMIStdTcpOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 12),
    _FsMIStdTcpOutSegs_Type()
)
fsMIStdTcpOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpOutSegs.setStatus("current")
_FsMIStdTcpRetransSegs_Type = Counter32
_FsMIStdTcpRetransSegs_Object = MibTableColumn
fsMIStdTcpRetransSegs = _FsMIStdTcpRetransSegs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 13),
    _FsMIStdTcpRetransSegs_Type()
)
fsMIStdTcpRetransSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpRetransSegs.setStatus("current")
_FsMIStdTcpInErrs_Type = Counter32
_FsMIStdTcpInErrs_Object = MibTableColumn
fsMIStdTcpInErrs = _FsMIStdTcpInErrs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 14),
    _FsMIStdTcpInErrs_Type()
)
fsMIStdTcpInErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpInErrs.setStatus("current")
_FsMIStdTcpOutRsts_Type = Counter32
_FsMIStdTcpOutRsts_Object = MibTableColumn
fsMIStdTcpOutRsts = _FsMIStdTcpOutRsts_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 15),
    _FsMIStdTcpOutRsts_Type()
)
fsMIStdTcpOutRsts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpOutRsts.setStatus("current")
_FsMIStdTcpHCInSegs_Type = Counter64
_FsMIStdTcpHCInSegs_Object = MibTableColumn
fsMIStdTcpHCInSegs = _FsMIStdTcpHCInSegs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 16),
    _FsMIStdTcpHCInSegs_Type()
)
fsMIStdTcpHCInSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpHCInSegs.setStatus("current")
_FsMIStdTcpHCOutSegs_Type = Counter64
_FsMIStdTcpHCOutSegs_Object = MibTableColumn
fsMIStdTcpHCOutSegs = _FsMIStdTcpHCOutSegs_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 1, 1, 17),
    _FsMIStdTcpHCOutSegs_Type()
)
fsMIStdTcpHCOutSegs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpHCOutSegs.setStatus("current")
_FsMIStdTcpConnectionTable_Object = MibTable
fsMIStdTcpConnectionTable = _FsMIStdTcpConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 2)
)
if mibBuilder.loadTexts:
    fsMIStdTcpConnectionTable.setStatus("current")
_FsMIStdTcpConnectionEntry_Object = MibTableRow
fsMIStdTcpConnectionEntry = _FsMIStdTcpConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 2, 1)
)
fsMIStdTcpConnectionEntry.setIndexNames(
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdContextId"),
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdTcpConnectionLocalAddressType"),
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdTcpConnectionLocalAddress"),
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdTcpConnectionLocalPort"),
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdTcpConnectionRemAddressType"),
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdTcpConnectionRemAddress"),
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdTcpConnectionRemPort"),
)
if mibBuilder.loadTexts:
    fsMIStdTcpConnectionEntry.setStatus("current")
_FsMIStdTcpConnectionLocalAddressType_Type = InetAddressType
_FsMIStdTcpConnectionLocalAddressType_Object = MibTableColumn
fsMIStdTcpConnectionLocalAddressType = _FsMIStdTcpConnectionLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 2, 1, 2),
    _FsMIStdTcpConnectionLocalAddressType_Type()
)
fsMIStdTcpConnectionLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdTcpConnectionLocalAddressType.setStatus("current")


class _FsMIStdTcpConnectionLocalAddress_Type(InetAddress):
    """Custom type fsMIStdTcpConnectionLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIStdTcpConnectionLocalAddress_Type.__name__ = "InetAddress"
_FsMIStdTcpConnectionLocalAddress_Object = MibTableColumn
fsMIStdTcpConnectionLocalAddress = _FsMIStdTcpConnectionLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 2, 1, 3),
    _FsMIStdTcpConnectionLocalAddress_Type()
)
fsMIStdTcpConnectionLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdTcpConnectionLocalAddress.setStatus("current")
_FsMIStdTcpConnectionLocalPort_Type = InetPortNumber
_FsMIStdTcpConnectionLocalPort_Object = MibTableColumn
fsMIStdTcpConnectionLocalPort = _FsMIStdTcpConnectionLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 2, 1, 4),
    _FsMIStdTcpConnectionLocalPort_Type()
)
fsMIStdTcpConnectionLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdTcpConnectionLocalPort.setStatus("current")
_FsMIStdTcpConnectionRemAddressType_Type = InetAddressType
_FsMIStdTcpConnectionRemAddressType_Object = MibTableColumn
fsMIStdTcpConnectionRemAddressType = _FsMIStdTcpConnectionRemAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 2, 1, 5),
    _FsMIStdTcpConnectionRemAddressType_Type()
)
fsMIStdTcpConnectionRemAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdTcpConnectionRemAddressType.setStatus("current")


class _FsMIStdTcpConnectionRemAddress_Type(InetAddress):
    """Custom type fsMIStdTcpConnectionRemAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIStdTcpConnectionRemAddress_Type.__name__ = "InetAddress"
_FsMIStdTcpConnectionRemAddress_Object = MibTableColumn
fsMIStdTcpConnectionRemAddress = _FsMIStdTcpConnectionRemAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 2, 1, 6),
    _FsMIStdTcpConnectionRemAddress_Type()
)
fsMIStdTcpConnectionRemAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdTcpConnectionRemAddress.setStatus("current")
_FsMIStdTcpConnectionRemPort_Type = InetPortNumber
_FsMIStdTcpConnectionRemPort_Object = MibTableColumn
fsMIStdTcpConnectionRemPort = _FsMIStdTcpConnectionRemPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 2, 1, 7),
    _FsMIStdTcpConnectionRemPort_Type()
)
fsMIStdTcpConnectionRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdTcpConnectionRemPort.setStatus("current")


class _FsMIStdTcpConnectionState_Type(Integer32):
    """Custom type fsMIStdTcpConnectionState based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("closed", 1),
          ("listen", 2),
          ("synSent", 3),
          ("synReceived", 4),
          ("established", 5),
          ("finWait1", 6),
          ("finWait2", 7),
          ("closeWait", 8),
          ("lastAck", 9),
          ("closing", 10),
          ("timeWait", 11),
          ("deleteTCB", 12))
    )


_FsMIStdTcpConnectionState_Type.__name__ = "Integer32"
_FsMIStdTcpConnectionState_Object = MibTableColumn
fsMIStdTcpConnectionState = _FsMIStdTcpConnectionState_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 2, 1, 8),
    _FsMIStdTcpConnectionState_Type()
)
fsMIStdTcpConnectionState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMIStdTcpConnectionState.setStatus("current")
_FsMIStdTcpConnectionProcess_Type = Unsigned32
_FsMIStdTcpConnectionProcess_Object = MibTableColumn
fsMIStdTcpConnectionProcess = _FsMIStdTcpConnectionProcess_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 2, 1, 9),
    _FsMIStdTcpConnectionProcess_Type()
)
fsMIStdTcpConnectionProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpConnectionProcess.setStatus("current")
_FsMIStdTcpListenerTable_Object = MibTable
fsMIStdTcpListenerTable = _FsMIStdTcpListenerTable_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 3)
)
if mibBuilder.loadTexts:
    fsMIStdTcpListenerTable.setStatus("current")
_FsMIStdTcpListenerEntry_Object = MibTableRow
fsMIStdTcpListenerEntry = _FsMIStdTcpListenerEntry_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 3, 1)
)
fsMIStdTcpListenerEntry.setIndexNames(
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdContextId"),
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdTcpListenerLocalAddressType"),
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdTcpListenerLocalAddress"),
    (0, "ARICENT-MI-TCP-IPVX-MIB", "fsMIStdTcpListenerLocalPort"),
)
if mibBuilder.loadTexts:
    fsMIStdTcpListenerEntry.setStatus("current")
_FsMIStdTcpListenerLocalAddressType_Type = InetAddressType
_FsMIStdTcpListenerLocalAddressType_Object = MibTableColumn
fsMIStdTcpListenerLocalAddressType = _FsMIStdTcpListenerLocalAddressType_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 3, 1, 2),
    _FsMIStdTcpListenerLocalAddressType_Type()
)
fsMIStdTcpListenerLocalAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdTcpListenerLocalAddressType.setStatus("current")


class _FsMIStdTcpListenerLocalAddress_Type(InetAddress):
    """Custom type fsMIStdTcpListenerLocalAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_FsMIStdTcpListenerLocalAddress_Type.__name__ = "InetAddress"
_FsMIStdTcpListenerLocalAddress_Object = MibTableColumn
fsMIStdTcpListenerLocalAddress = _FsMIStdTcpListenerLocalAddress_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 3, 1, 3),
    _FsMIStdTcpListenerLocalAddress_Type()
)
fsMIStdTcpListenerLocalAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdTcpListenerLocalAddress.setStatus("current")
_FsMIStdTcpListenerLocalPort_Type = InetPortNumber
_FsMIStdTcpListenerLocalPort_Object = MibTableColumn
fsMIStdTcpListenerLocalPort = _FsMIStdTcpListenerLocalPort_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 3, 1, 4),
    _FsMIStdTcpListenerLocalPort_Type()
)
fsMIStdTcpListenerLocalPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    fsMIStdTcpListenerLocalPort.setStatus("current")
_FsMIStdTcpListenerProcess_Type = Unsigned32
_FsMIStdTcpListenerProcess_Object = MibTableColumn
fsMIStdTcpListenerProcess = _FsMIStdTcpListenerProcess_Object(
    (1, 3, 6, 1, 4, 1, 29601, 2, 75, 3, 1, 5),
    _FsMIStdTcpListenerProcess_Type()
)
fsMIStdTcpListenerProcess.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMIStdTcpListenerProcess.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-MI-TCP-IPVX-MIB",
    **{"fsMIStdTcpIpvx": fsMIStdTcpIpvx,
       "fsMIStdContextTable": fsMIStdContextTable,
       "fsMIStdContextEntry": fsMIStdContextEntry,
       "fsMIStdContextId": fsMIStdContextId,
       "fsMIStdTcpRtoAlgorithm": fsMIStdTcpRtoAlgorithm,
       "fsMIStdTcpRtoMin": fsMIStdTcpRtoMin,
       "fsMIStdTcpRtoMax": fsMIStdTcpRtoMax,
       "fsMIStdTcpMaxConn": fsMIStdTcpMaxConn,
       "fsMIStdTcpActiveOpens": fsMIStdTcpActiveOpens,
       "fsMIStdTcpPassiveOpens": fsMIStdTcpPassiveOpens,
       "fsMIStdTcpAttemptFails": fsMIStdTcpAttemptFails,
       "fsMIStdTcpEstabResets": fsMIStdTcpEstabResets,
       "fsMIStdTcpCurrEstab": fsMIStdTcpCurrEstab,
       "fsMIStdTcpInSegs": fsMIStdTcpInSegs,
       "fsMIStdTcpOutSegs": fsMIStdTcpOutSegs,
       "fsMIStdTcpRetransSegs": fsMIStdTcpRetransSegs,
       "fsMIStdTcpInErrs": fsMIStdTcpInErrs,
       "fsMIStdTcpOutRsts": fsMIStdTcpOutRsts,
       "fsMIStdTcpHCInSegs": fsMIStdTcpHCInSegs,
       "fsMIStdTcpHCOutSegs": fsMIStdTcpHCOutSegs,
       "fsMIStdTcpConnectionTable": fsMIStdTcpConnectionTable,
       "fsMIStdTcpConnectionEntry": fsMIStdTcpConnectionEntry,
       "fsMIStdTcpConnectionLocalAddressType": fsMIStdTcpConnectionLocalAddressType,
       "fsMIStdTcpConnectionLocalAddress": fsMIStdTcpConnectionLocalAddress,
       "fsMIStdTcpConnectionLocalPort": fsMIStdTcpConnectionLocalPort,
       "fsMIStdTcpConnectionRemAddressType": fsMIStdTcpConnectionRemAddressType,
       "fsMIStdTcpConnectionRemAddress": fsMIStdTcpConnectionRemAddress,
       "fsMIStdTcpConnectionRemPort": fsMIStdTcpConnectionRemPort,
       "fsMIStdTcpConnectionState": fsMIStdTcpConnectionState,
       "fsMIStdTcpConnectionProcess": fsMIStdTcpConnectionProcess,
       "fsMIStdTcpListenerTable": fsMIStdTcpListenerTable,
       "fsMIStdTcpListenerEntry": fsMIStdTcpListenerEntry,
       "fsMIStdTcpListenerLocalAddressType": fsMIStdTcpListenerLocalAddressType,
       "fsMIStdTcpListenerLocalAddress": fsMIStdTcpListenerLocalAddress,
       "fsMIStdTcpListenerLocalPort": fsMIStdTcpListenerLocalPort,
       "fsMIStdTcpListenerProcess": fsMIStdTcpListenerProcess}
)
