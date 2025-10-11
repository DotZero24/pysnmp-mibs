# SNMP MIB module (BRCM-PING-MGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/broadcom/BRCM-PING-MGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:08:22 2025
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

(cableDataMgmtBase,) = mibBuilder.importSymbols(
    "BRCM-CABLEDATA-MGMT-MIB",
    "cableDataMgmtBase")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

pingMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5)
)
if mibBuilder.loadTexts:
    pingMgmt.setRevisions(
        ("2007-02-05 00:00",
         "2006-06-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _PingTargetAddressType_Type(InetAddressType):
    """Custom type pingTargetAddressType based on InetAddressType"""
    defaultValue = 1


_PingTargetAddressType_Type.__name__ = "InetAddressType"
_PingTargetAddressType_Object = MibScalar
pingTargetAddressType = _PingTargetAddressType_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 1),
    _PingTargetAddressType_Type()
)
pingTargetAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTargetAddressType.setStatus("current")


class _PingTargetAddress_Type(InetAddress):
    """Custom type pingTargetAddress based on InetAddress"""
    defaultHexValue = "00000000"


_PingTargetAddress_Type.__name__ = "InetAddress"
_PingTargetAddress_Object = MibScalar
pingTargetAddress = _PingTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 2),
    _PingTargetAddress_Type()
)
pingTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTargetAddress.setStatus("current")


class _PingNumPkts_Type(Unsigned32):
    """Custom type pingNumPkts based on Unsigned32"""
    defaultValue = 3


_PingNumPkts_Type.__name__ = "Unsigned32"
_PingNumPkts_Object = MibScalar
pingNumPkts = _PingNumPkts_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 3),
    _PingNumPkts_Type()
)
pingNumPkts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingNumPkts.setStatus("current")


class _PingPktStartSize_Type(Unsigned32):
    """Custom type pingPktStartSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_PingPktStartSize_Type.__name__ = "Unsigned32"
_PingPktStartSize_Object = MibScalar
pingPktStartSize = _PingPktStartSize_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 4),
    _PingPktStartSize_Type()
)
pingPktStartSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingPktStartSize.setStatus("current")
if mibBuilder.loadTexts:
    pingPktStartSize.setUnits("bytes")


class _PingPktEndSize_Type(Unsigned32):
    """Custom type pingPktEndSize based on Unsigned32"""
    defaultValue = 64

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1518),
    )


_PingPktEndSize_Type.__name__ = "Unsigned32"
_PingPktEndSize_Object = MibScalar
pingPktEndSize = _PingPktEndSize_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 5),
    _PingPktEndSize_Type()
)
pingPktEndSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingPktEndSize.setStatus("current")
if mibBuilder.loadTexts:
    pingPktEndSize.setUnits("bytes")


class _PingPktStepSize_Type(Integer32):
    """Custom type pingPktStepSize based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1454, 1454),
    )


_PingPktStepSize_Type.__name__ = "Integer32"
_PingPktStepSize_Object = MibScalar
pingPktStepSize = _PingPktStepSize_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 6),
    _PingPktStepSize_Type()
)
pingPktStepSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingPktStepSize.setStatus("current")
if mibBuilder.loadTexts:
    pingPktStepSize.setUnits("bytes")


class _PingInterval_Type(Unsigned32):
    """Custom type pingInterval based on Unsigned32"""
    defaultValue = 0


_PingInterval_Type.__name__ = "Unsigned32"
_PingInterval_Object = MibScalar
pingInterval = _PingInterval_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 7),
    _PingInterval_Type()
)
pingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingInterval.setStatus("current")
if mibBuilder.loadTexts:
    pingInterval.setUnits("milliseconds")


class _PingTimeout_Type(Integer32):
    """Custom type pingTimeout based on Integer32"""
    defaultValue = 5000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 65535),
    )


_PingTimeout_Type.__name__ = "Integer32"
_PingTimeout_Object = MibScalar
pingTimeout = _PingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 8),
    _PingTimeout_Type()
)
pingTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingTimeout.setStatus("current")
if mibBuilder.loadTexts:
    pingTimeout.setUnits("milliseconds")


class _PingVerifyReply_Type(TruthValue):
    """Custom type pingVerifyReply based on TruthValue"""
    defaultValue = 1


_PingVerifyReply_Type.__name__ = "TruthValue"
_PingVerifyReply_Object = MibScalar
pingVerifyReply = _PingVerifyReply_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 9),
    _PingVerifyReply_Type()
)
pingVerifyReply.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingVerifyReply.setStatus("current")


class _PingIpStackNumber_Type(Integer32):
    """Custom type pingIpStackNumber based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_PingIpStackNumber_Type.__name__ = "Integer32"
_PingIpStackNumber_Object = MibScalar
pingIpStackNumber = _PingIpStackNumber_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 10),
    _PingIpStackNumber_Type()
)
pingIpStackNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingIpStackNumber.setStatus("current")


class _PingNow_Type(TruthValue):
    """Custom type pingNow based on TruthValue"""
    defaultValue = 1


_PingNow_Type.__name__ = "TruthValue"
_PingNow_Object = MibScalar
pingNow = _PingNow_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 11),
    _PingNow_Type()
)
pingNow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    pingNow.setStatus("current")
_PingPktsSent_Type = Counter32
_PingPktsSent_Object = MibScalar
pingPktsSent = _PingPktsSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 12),
    _PingPktsSent_Type()
)
pingPktsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingPktsSent.setStatus("current")
_PingRepliesReceived_Type = Counter32
_PingRepliesReceived_Object = MibScalar
pingRepliesReceived = _PingRepliesReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 13),
    _PingRepliesReceived_Type()
)
pingRepliesReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingRepliesReceived.setStatus("current")
_PingRepliesVerified_Type = Counter32
_PingRepliesVerified_Object = MibScalar
pingRepliesVerified = _PingRepliesVerified_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 14),
    _PingRepliesVerified_Type()
)
pingRepliesVerified.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingRepliesVerified.setStatus("current")
_PingOctetsSent_Type = Counter32
_PingOctetsSent_Object = MibScalar
pingOctetsSent = _PingOctetsSent_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 15),
    _PingOctetsSent_Type()
)
pingOctetsSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingOctetsSent.setStatus("current")
_PingOctetsReceived_Type = Counter32
_PingOctetsReceived_Object = MibScalar
pingOctetsReceived = _PingOctetsReceived_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 16),
    _PingOctetsReceived_Type()
)
pingOctetsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingOctetsReceived.setStatus("current")
_PingIcmpErrors_Type = Counter32
_PingIcmpErrors_Object = MibScalar
pingIcmpErrors = _PingIcmpErrors_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 17),
    _PingIcmpErrors_Type()
)
pingIcmpErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingIcmpErrors.setStatus("current")
_PingLastIcmpError_Type = Unsigned32
_PingLastIcmpError_Object = MibScalar
pingLastIcmpError = _PingLastIcmpError_Object(
    (1, 3, 6, 1, 4, 1, 4413, 2, 2, 2, 1, 1, 5, 18),
    _PingLastIcmpError_Type()
)
pingLastIcmpError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    pingLastIcmpError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "BRCM-PING-MGMT-MIB",
    **{"pingMgmt": pingMgmt,
       "pingTargetAddressType": pingTargetAddressType,
       "pingTargetAddress": pingTargetAddress,
       "pingNumPkts": pingNumPkts,
       "pingPktStartSize": pingPktStartSize,
       "pingPktEndSize": pingPktEndSize,
       "pingPktStepSize": pingPktStepSize,
       "pingInterval": pingInterval,
       "pingTimeout": pingTimeout,
       "pingVerifyReply": pingVerifyReply,
       "pingIpStackNumber": pingIpStackNumber,
       "pingNow": pingNow,
       "pingPktsSent": pingPktsSent,
       "pingRepliesReceived": pingRepliesReceived,
       "pingRepliesVerified": pingRepliesVerified,
       "pingOctetsSent": pingOctetsSent,
       "pingOctetsReceived": pingOctetsReceived,
       "pingIcmpErrors": pingIcmpErrors,
       "pingLastIcmpError": pingLastIcmpError}
)
