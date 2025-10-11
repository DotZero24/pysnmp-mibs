# SNMP MIB module (RAD-TACACS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/rad/RAD-TACACS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:18:24 2025
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
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(radSecurity,) = mibBuilder.importSymbols(
    "RAD-SMI-MIB",
    "radSecurity")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

radTacacsPlus = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



class RadTacacsKeyString(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )



# MIB Managed Objects in the order of their OIDs

_TacplusAuthServerTable_Object = MibTable
tacplusAuthServerTable = _TacplusAuthServerTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1)
)
if mibBuilder.loadTexts:
    tacplusAuthServerTable.setStatus("current")
_TacplusAuthServerEntry_Object = MibTableRow
tacplusAuthServerEntry = _TacplusAuthServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1)
)
tacplusAuthServerEntry.setIndexNames(
    (0, "RAD-TACACS-MIB", "tacplusServerAddressType"),
    (0, "RAD-TACACS-MIB", "tacplusServerAddress"),
    (0, "RAD-TACACS-MIB", "tacplusServerPort"),
)
if mibBuilder.loadTexts:
    tacplusAuthServerEntry.setStatus("current")
_TacplusServerAddressType_Type = InetAddressType
_TacplusServerAddressType_Object = MibTableColumn
tacplusServerAddressType = _TacplusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 1),
    _TacplusServerAddressType_Type()
)
tacplusServerAddressType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacplusServerAddressType.setStatus("current")
_TacplusServerAddress_Type = InetAddress
_TacplusServerAddress_Object = MibTableColumn
tacplusServerAddress = _TacplusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 2),
    _TacplusServerAddress_Type()
)
tacplusServerAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacplusServerAddress.setStatus("current")


class _TacplusServerPort_Type(Unsigned32):
    """Custom type tacplusServerPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacplusServerPort_Type.__name__ = "Unsigned32"
_TacplusServerPort_Object = MibTableColumn
tacplusServerPort = _TacplusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 3),
    _TacplusServerPort_Type()
)
tacplusServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacplusServerPort.setStatus("current")
_TacplusRowStatus_Type = RowStatus
_TacplusRowStatus_Object = MibTableColumn
tacplusRowStatus = _TacplusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 4),
    _TacplusRowStatus_Type()
)
tacplusRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacplusRowStatus.setStatus("current")


class _TacplusSecretKey_Type(RadTacacsKeyString):
    """Custom type tacplusSecretKey based on RadTacacsKeyString"""
    defaultValue = OctetString("")


_TacplusSecretKey_Type.__name__ = "RadTacacsKeyString"
_TacplusSecretKey_Object = MibTableColumn
tacplusSecretKey = _TacplusSecretKey_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 6),
    _TacplusSecretKey_Type()
)
tacplusSecretKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacplusSecretKey.setStatus("current")


class _TacplusRetryCount_Type(Unsigned32):
    """Custom type tacplusRetryCount based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_TacplusRetryCount_Type.__name__ = "Unsigned32"
_TacplusRetryCount_Object = MibTableColumn
tacplusRetryCount = _TacplusRetryCount_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 7),
    _TacplusRetryCount_Type()
)
tacplusRetryCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacplusRetryCount.setStatus("current")


class _TacplusTimeout_Type(Unsigned32):
    """Custom type tacplusTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_TacplusTimeout_Type.__name__ = "Unsigned32"
_TacplusTimeout_Object = MibTableColumn
tacplusTimeout = _TacplusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 8),
    _TacplusTimeout_Type()
)
tacplusTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacplusTimeout.setStatus("current")


class _TacplusAuthentStatus_Type(Integer32):
    """Custom type tacplusAuthentStatus based on Integer32"""
    defaultValue = 4

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
        *(("authenticated", 1),
          ("authenticationFailure", 2),
          ("unknownFailure", 3),
          ("idle", 4))
    )


_TacplusAuthentStatus_Type.__name__ = "Integer32"
_TacplusAuthentStatus_Object = MibTableColumn
tacplusAuthentStatus = _TacplusAuthentStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 9),
    _TacplusAuthentStatus_Type()
)
tacplusAuthentStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusAuthentStatus.setStatus("current")


class _TacplusAccountingPort_Type(Unsigned32):
    """Custom type tacplusAccountingPort based on Unsigned32"""
    defaultValue = 49

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacplusAccountingPort_Type.__name__ = "Unsigned32"
_TacplusAccountingPort_Object = MibTableColumn
tacplusAccountingPort = _TacplusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 11),
    _TacplusAccountingPort_Type()
)
tacplusAccountingPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacplusAccountingPort.setStatus("current")


class _TacplusServerGroup_Type(Unsigned32):
    """Custom type tacplusServerGroup based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_TacplusServerGroup_Type.__name__ = "Unsigned32"
_TacplusServerGroup_Object = MibTableColumn
tacplusServerGroup = _TacplusServerGroup_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 12),
    _TacplusServerGroup_Type()
)
tacplusServerGroup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacplusServerGroup.setStatus("current")


class _TacplusAuthenticationPort_Type(Unsigned32):
    """Custom type tacplusAuthenticationPort based on Unsigned32"""
    defaultValue = 49

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_TacplusAuthenticationPort_Type.__name__ = "Unsigned32"
_TacplusAuthenticationPort_Object = MibTableColumn
tacplusAuthenticationPort = _TacplusAuthenticationPort_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 1, 1, 13),
    _TacplusAuthenticationPort_Type()
)
tacplusAuthenticationPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacplusAuthenticationPort.setStatus("current")
_TacplusStatsTable_Object = MibTable
tacplusStatsTable = _TacplusStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2)
)
if mibBuilder.loadTexts:
    tacplusStatsTable.setStatus("current")
_TacplusStatsEntry_Object = MibTableRow
tacplusStatsEntry = _TacplusStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2, 1)
)
if mibBuilder.loadTexts:
    tacplusStatsEntry.setStatus("current")


class _TacplusClearStaticsCmd_Type(Integer32):
    """Custom type tacplusClearStaticsCmd based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2))
    )


_TacplusClearStaticsCmd_Type.__name__ = "Integer32"
_TacplusClearStaticsCmd_Object = MibTableColumn
tacplusClearStaticsCmd = _TacplusClearStaticsCmd_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2, 1, 1),
    _TacplusClearStaticsCmd_Type()
)
tacplusClearStaticsCmd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tacplusClearStaticsCmd.setStatus("current")
_TacplusAuthRequests_Type = Counter32
_TacplusAuthRequests_Object = MibTableColumn
tacplusAuthRequests = _TacplusAuthRequests_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2, 1, 2),
    _TacplusAuthRequests_Type()
)
tacplusAuthRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusAuthRequests.setStatus("current")
_TacplusAuthenRequestTimeouts_Type = Counter32
_TacplusAuthenRequestTimeouts_Object = MibTableColumn
tacplusAuthenRequestTimeouts = _TacplusAuthenRequestTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2, 1, 3),
    _TacplusAuthenRequestTimeouts_Type()
)
tacplusAuthenRequestTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusAuthenRequestTimeouts.setStatus("current")
_TacplusAuthenUnexpectedResponses_Type = Counter32
_TacplusAuthenUnexpectedResponses_Object = MibTableColumn
tacplusAuthenUnexpectedResponses = _TacplusAuthenUnexpectedResponses_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2, 1, 4),
    _TacplusAuthenUnexpectedResponses_Type()
)
tacplusAuthenUnexpectedResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusAuthenUnexpectedResponses.setStatus("current")
_TacplusAuthenServerErrorResponses_Type = Counter32
_TacplusAuthenServerErrorResponses_Object = MibTableColumn
tacplusAuthenServerErrorResponses = _TacplusAuthenServerErrorResponses_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2, 1, 5),
    _TacplusAuthenServerErrorResponses_Type()
)
tacplusAuthenServerErrorResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusAuthenServerErrorResponses.setStatus("current")
_TacplusAuthenIncorrectResponses_Type = Counter32
_TacplusAuthenIncorrectResponses_Object = MibTableColumn
tacplusAuthenIncorrectResponses = _TacplusAuthenIncorrectResponses_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2, 1, 6),
    _TacplusAuthenIncorrectResponses_Type()
)
tacplusAuthenIncorrectResponses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusAuthenIncorrectResponses.setStatus("current")
_TacplusAuthenTransactionSuccesses_Type = Counter32
_TacplusAuthenTransactionSuccesses_Object = MibTableColumn
tacplusAuthenTransactionSuccesses = _TacplusAuthenTransactionSuccesses_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2, 1, 7),
    _TacplusAuthenTransactionSuccesses_Type()
)
tacplusAuthenTransactionSuccesses.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusAuthenTransactionSuccesses.setStatus("current")
_TacplusAuthenTransactionFailures_Type = Counter32
_TacplusAuthenTransactionFailures_Object = MibTableColumn
tacplusAuthenTransactionFailures = _TacplusAuthenTransactionFailures_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2, 1, 8),
    _TacplusAuthenTransactionFailures_Type()
)
tacplusAuthenTransactionFailures.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusAuthenTransactionFailures.setStatus("current")
_TacplusAuthenPendingRequests_Type = Counter32
_TacplusAuthenPendingRequests_Object = MibTableColumn
tacplusAuthenPendingRequests = _TacplusAuthenPendingRequests_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 2, 1, 9),
    _TacplusAuthenPendingRequests_Type()
)
tacplusAuthenPendingRequests.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    tacplusAuthenPendingRequests.setStatus("current")
_TacplusServerGroupTable_Object = MibTable
tacplusServerGroupTable = _TacplusServerGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 3)
)
if mibBuilder.loadTexts:
    tacplusServerGroupTable.setStatus("current")
_TacplusServerGroupEntry_Object = MibTableRow
tacplusServerGroupEntry = _TacplusServerGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 3, 1)
)
tacplusServerGroupEntry.setIndexNames(
    (0, "RAD-TACACS-MIB", "tacplusServerGroupId"),
)
if mibBuilder.loadTexts:
    tacplusServerGroupEntry.setStatus("current")
_TacplusServerGroupId_Type = Unsigned32
_TacplusServerGroupId_Object = MibTableColumn
tacplusServerGroupId = _TacplusServerGroupId_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 3, 1, 1),
    _TacplusServerGroupId_Type()
)
tacplusServerGroupId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    tacplusServerGroupId.setStatus("current")
_TacplusServerGroupRowStatus_Type = RowStatus
_TacplusServerGroupRowStatus_Object = MibTableColumn
tacplusServerGroupRowStatus = _TacplusServerGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 3, 1, 2),
    _TacplusServerGroupRowStatus_Type()
)
tacplusServerGroupRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacplusServerGroupRowStatus.setStatus("current")
_TacplusServerGroupName_Type = SnmpAdminString
_TacplusServerGroupName_Object = MibTableColumn
tacplusServerGroupName = _TacplusServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 3, 1, 3),
    _TacplusServerGroupName_Type()
)
tacplusServerGroupName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacplusServerGroupName.setStatus("current")


class _TacplusServerGroupAccountingMode_Type(Bits):
    """Custom type tacplusServerGroupAccountingMode based on Bits"""
    namedValues = NamedValues(
        *(("shell", 0),
          ("system", 1),
          ("commands", 2))
    )

_TacplusServerGroupAccountingMode_Type.__name__ = "Bits"
_TacplusServerGroupAccountingMode_Object = MibTableColumn
tacplusServerGroupAccountingMode = _TacplusServerGroupAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 164, 6, 1, 14, 1, 3, 1, 4),
    _TacplusServerGroupAccountingMode_Type()
)
tacplusServerGroupAccountingMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    tacplusServerGroupAccountingMode.setStatus("current")
tacplusAuthServerEntry.registerAugmentions(
    ("RAD-TACACS-MIB",
     "tacplusStatsEntry")
)
tacplusStatsEntry.setIndexNames(*tacplusAuthServerEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAD-TACACS-MIB",
    **{"RadTacacsKeyString": RadTacacsKeyString,
       "radTacacsPlus": radTacacsPlus,
       "tacplusAuthServerTable": tacplusAuthServerTable,
       "tacplusAuthServerEntry": tacplusAuthServerEntry,
       "tacplusServerAddressType": tacplusServerAddressType,
       "tacplusServerAddress": tacplusServerAddress,
       "tacplusServerPort": tacplusServerPort,
       "tacplusRowStatus": tacplusRowStatus,
       "tacplusSecretKey": tacplusSecretKey,
       "tacplusRetryCount": tacplusRetryCount,
       "tacplusTimeout": tacplusTimeout,
       "tacplusAuthentStatus": tacplusAuthentStatus,
       "tacplusAccountingPort": tacplusAccountingPort,
       "tacplusServerGroup": tacplusServerGroup,
       "tacplusAuthenticationPort": tacplusAuthenticationPort,
       "tacplusStatsTable": tacplusStatsTable,
       "tacplusStatsEntry": tacplusStatsEntry,
       "tacplusClearStaticsCmd": tacplusClearStaticsCmd,
       "tacplusAuthRequests": tacplusAuthRequests,
       "tacplusAuthenRequestTimeouts": tacplusAuthenRequestTimeouts,
       "tacplusAuthenUnexpectedResponses": tacplusAuthenUnexpectedResponses,
       "tacplusAuthenServerErrorResponses": tacplusAuthenServerErrorResponses,
       "tacplusAuthenIncorrectResponses": tacplusAuthenIncorrectResponses,
       "tacplusAuthenTransactionSuccesses": tacplusAuthenTransactionSuccesses,
       "tacplusAuthenTransactionFailures": tacplusAuthenTransactionFailures,
       "tacplusAuthenPendingRequests": tacplusAuthenPendingRequests,
       "tacplusServerGroupTable": tacplusServerGroupTable,
       "tacplusServerGroupEntry": tacplusServerGroupEntry,
       "tacplusServerGroupId": tacplusServerGroupId,
       "tacplusServerGroupRowStatus": tacplusServerGroupRowStatus,
       "tacplusServerGroupName": tacplusServerGroupName,
       "tacplusServerGroupAccountingMode": tacplusServerGroupAccountingMode}
)
