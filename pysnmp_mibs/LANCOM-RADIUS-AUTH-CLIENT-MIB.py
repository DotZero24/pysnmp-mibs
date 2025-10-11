# SNMP MIB module (LANCOM-RADIUS-AUTH-CLIENT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/lancom/LANCOM-RADIUS-AUTH-CLIENT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:21:01 2025
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

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

(fastPath,) = mibBuilder.importSymbols(
    "LANCOM-REF-MIB",
    "fastPath")

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

fastPathRadius = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8)
)
if mibBuilder.loadTexts:
    fastPathRadius.setRevisions(
        ("2018-03-10 00:00",
         "2018-02-13 00:00",
         "2017-03-30 00:00",
         "2016-11-21 00:00",
         "2016-09-29 00:00",
         "2014-04-21 00:00",
         "2011-12-14 00:00",
         "2011-09-26 00:00",
         "2011-01-26 00:00",
         "2007-05-23 00:00",
         "2003-11-21 00:00",
         "2003-05-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AgentRadiusConfigGroup_ObjectIdentity = ObjectIdentity
agentRadiusConfigGroup = _AgentRadiusConfigGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1)
)


class _AgentRadiusMaxTransmit_Type(Unsigned32):
    """Custom type agentRadiusMaxTransmit based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 15),
    )


_AgentRadiusMaxTransmit_Type.__name__ = "Unsigned32"
_AgentRadiusMaxTransmit_Object = MibScalar
agentRadiusMaxTransmit = _AgentRadiusMaxTransmit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 1),
    _AgentRadiusMaxTransmit_Type()
)
agentRadiusMaxTransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusMaxTransmit.setStatus("current")


class _AgentRadiusTimeout_Type(Unsigned32):
    """Custom type agentRadiusTimeout based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentRadiusTimeout_Type.__name__ = "Unsigned32"
_AgentRadiusTimeout_Object = MibScalar
agentRadiusTimeout = _AgentRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 2),
    _AgentRadiusTimeout_Type()
)
agentRadiusTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusTimeout.setStatus("current")


class _AgentRadiusAccountingMode_Type(Integer32):
    """Custom type agentRadiusAccountingMode based on Integer32"""
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


_AgentRadiusAccountingMode_Type.__name__ = "Integer32"
_AgentRadiusAccountingMode_Object = MibScalar
agentRadiusAccountingMode = _AgentRadiusAccountingMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 3),
    _AgentRadiusAccountingMode_Type()
)
agentRadiusAccountingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingMode.setStatus("current")


class _AgentRadiusStatsClear_Type(Integer32):
    """Custom type agentRadiusStatsClear based on Integer32"""
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


_AgentRadiusStatsClear_Type.__name__ = "Integer32"
_AgentRadiusStatsClear_Object = MibScalar
agentRadiusStatsClear = _AgentRadiusStatsClear_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 4),
    _AgentRadiusStatsClear_Type()
)
agentRadiusStatsClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusStatsClear.setStatus("current")


class _AgentRadiusAccountingIndexNextValid_Type(Integer32):
    """Custom type agentRadiusAccountingIndexNextValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusAccountingIndexNextValid_Type.__name__ = "Integer32"
_AgentRadiusAccountingIndexNextValid_Object = MibScalar
agentRadiusAccountingIndexNextValid = _AgentRadiusAccountingIndexNextValid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 5),
    _AgentRadiusAccountingIndexNextValid_Type()
)
agentRadiusAccountingIndexNextValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusAccountingIndexNextValid.setStatus("current")
_AgentRadiusAccountingConfigTable_Object = MibTable
agentRadiusAccountingConfigTable = _AgentRadiusAccountingConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6)
)
if mibBuilder.loadTexts:
    agentRadiusAccountingConfigTable.setStatus("current")
_AgentRadiusAccountingConfigEntry_Object = MibTableRow
agentRadiusAccountingConfigEntry = _AgentRadiusAccountingConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1)
)
agentRadiusAccountingConfigEntry.setIndexNames(
    (0, "LANCOM-RADIUS-AUTH-CLIENT-MIB", "agentRadiusAccountingServerIndex"),
)
if mibBuilder.loadTexts:
    agentRadiusAccountingConfigEntry.setStatus("current")


class _AgentRadiusAccountingServerIndex_Type(Integer32):
    """Custom type agentRadiusAccountingServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusAccountingServerIndex_Type.__name__ = "Integer32"
_AgentRadiusAccountingServerIndex_Object = MibTableColumn
agentRadiusAccountingServerIndex = _AgentRadiusAccountingServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 1),
    _AgentRadiusAccountingServerIndex_Type()
)
agentRadiusAccountingServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerIndex.setStatus("current")
_AgentRadiusAccountingServerAddress_Type = InetAddress
_AgentRadiusAccountingServerAddress_Object = MibTableColumn
agentRadiusAccountingServerAddress = _AgentRadiusAccountingServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 2),
    _AgentRadiusAccountingServerAddress_Type()
)
agentRadiusAccountingServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerAddress.setStatus("current")
_AgentRadiusAccountingServerAddressType_Type = InetAddressType
_AgentRadiusAccountingServerAddressType_Object = MibTableColumn
agentRadiusAccountingServerAddressType = _AgentRadiusAccountingServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 3),
    _AgentRadiusAccountingServerAddressType_Type()
)
agentRadiusAccountingServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerAddressType.setStatus("current")


class _AgentRadiusAccountingPort_Type(Unsigned32):
    """Custom type agentRadiusAccountingPort based on Unsigned32"""
    defaultValue = 1813

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentRadiusAccountingPort_Type.__name__ = "Unsigned32"
_AgentRadiusAccountingPort_Object = MibTableColumn
agentRadiusAccountingPort = _AgentRadiusAccountingPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 4),
    _AgentRadiusAccountingPort_Type()
)
agentRadiusAccountingPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingPort.setStatus("current")


class _AgentRadiusAccountingSecret_Type(DisplayString):
    """Custom type agentRadiusAccountingSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentRadiusAccountingSecret_Type.__name__ = "DisplayString"
_AgentRadiusAccountingSecret_Object = MibTableColumn
agentRadiusAccountingSecret = _AgentRadiusAccountingSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 5),
    _AgentRadiusAccountingSecret_Type()
)
agentRadiusAccountingSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingSecret.setStatus("current")
_AgentRadiusAccountingStatus_Type = RowStatus
_AgentRadiusAccountingStatus_Object = MibTableColumn
agentRadiusAccountingStatus = _AgentRadiusAccountingStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 6),
    _AgentRadiusAccountingStatus_Type()
)
agentRadiusAccountingStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingStatus.setStatus("current")


class _AgentRadiusAccountingServerName_Type(DisplayString):
    """Custom type agentRadiusAccountingServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentRadiusAccountingServerName_Type.__name__ = "DisplayString"
_AgentRadiusAccountingServerName_Object = MibTableColumn
agentRadiusAccountingServerName = _AgentRadiusAccountingServerName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 7),
    _AgentRadiusAccountingServerName_Type()
)
agentRadiusAccountingServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerName.setStatus("current")
_AgentRadiusAccountingLinkLocalIntf_Type = InterfaceIndexOrZero
_AgentRadiusAccountingLinkLocalIntf_Object = MibTableColumn
agentRadiusAccountingLinkLocalIntf = _AgentRadiusAccountingLinkLocalIntf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 8),
    _AgentRadiusAccountingLinkLocalIntf_Type()
)
agentRadiusAccountingLinkLocalIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingLinkLocalIntf.setStatus("current")


class _AgentRadiusAccountingServerTestUserName_Type(DisplayString):
    """Custom type agentRadiusAccountingServerTestUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentRadiusAccountingServerTestUserName_Type.__name__ = "DisplayString"
_AgentRadiusAccountingServerTestUserName_Object = MibTableColumn
agentRadiusAccountingServerTestUserName = _AgentRadiusAccountingServerTestUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 9),
    _AgentRadiusAccountingServerTestUserName_Type()
)
agentRadiusAccountingServerTestUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerTestUserName.setStatus("current")


class _AgentRadiusAccountingServerIdleTime_Type(Unsigned32):
    """Custom type agentRadiusAccountingServerIdleTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35791),
    )


_AgentRadiusAccountingServerIdleTime_Type.__name__ = "Unsigned32"
_AgentRadiusAccountingServerIdleTime_Object = MibTableColumn
agentRadiusAccountingServerIdleTime = _AgentRadiusAccountingServerIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 10),
    _AgentRadiusAccountingServerIdleTime_Type()
)
agentRadiusAccountingServerIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerIdleTime.setStatus("current")


class _AgentRadiusAccountingServerState_Type(Integer32):
    """Custom type agentRadiusAccountingServerState based on Integer32"""
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
        *(("up", 1),
          ("inactive", 2),
          ("dead", 3),
          ("quarantined", 4),
          ("unknown", 5))
    )


_AgentRadiusAccountingServerState_Type.__name__ = "Integer32"
_AgentRadiusAccountingServerState_Object = MibTableColumn
agentRadiusAccountingServerState = _AgentRadiusAccountingServerState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 11),
    _AgentRadiusAccountingServerState_Type()
)
agentRadiusAccountingServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerState.setStatus("current")
_AgentRadiusAccountingServerStateDuration_Type = Unsigned32
_AgentRadiusAccountingServerStateDuration_Object = MibTableColumn
agentRadiusAccountingServerStateDuration = _AgentRadiusAccountingServerStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 12),
    _AgentRadiusAccountingServerStateDuration_Type()
)
agentRadiusAccountingServerStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerStateDuration.setStatus("current")


class _AgentRadiusAccountingServerImmortalState_Type(Integer32):
    """Custom type agentRadiusAccountingServerImmortalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immortal", 1),
          ("mortal", 2))
    )


_AgentRadiusAccountingServerImmortalState_Type.__name__ = "Integer32"
_AgentRadiusAccountingServerImmortalState_Object = MibTableColumn
agentRadiusAccountingServerImmortalState = _AgentRadiusAccountingServerImmortalState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 6, 1, 13),
    _AgentRadiusAccountingServerImmortalState_Type()
)
agentRadiusAccountingServerImmortalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusAccountingServerImmortalState.setStatus("current")


class _AgentRadiusServerIndexNextValid_Type(Integer32):
    """Custom type agentRadiusServerIndexNextValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusServerIndexNextValid_Type.__name__ = "Integer32"
_AgentRadiusServerIndexNextValid_Object = MibScalar
agentRadiusServerIndexNextValid = _AgentRadiusServerIndexNextValid_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 7),
    _AgentRadiusServerIndexNextValid_Type()
)
agentRadiusServerIndexNextValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusServerIndexNextValid.setStatus("current")
_AgentRadiusServerConfigTable_Object = MibTable
agentRadiusServerConfigTable = _AgentRadiusServerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8)
)
if mibBuilder.loadTexts:
    agentRadiusServerConfigTable.setStatus("current")
_AgentRadiusServerConfigEntry_Object = MibTableRow
agentRadiusServerConfigEntry = _AgentRadiusServerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1)
)
agentRadiusServerConfigEntry.setIndexNames(
    (0, "LANCOM-RADIUS-AUTH-CLIENT-MIB", "agentRadiusServerIndex"),
)
if mibBuilder.loadTexts:
    agentRadiusServerConfigEntry.setStatus("current")


class _AgentRadiusServerIndex_Type(Integer32):
    """Custom type agentRadiusServerIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusServerIndex_Type.__name__ = "Integer32"
_AgentRadiusServerIndex_Object = MibTableColumn
agentRadiusServerIndex = _AgentRadiusServerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 1),
    _AgentRadiusServerIndex_Type()
)
agentRadiusServerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentRadiusServerIndex.setStatus("current")
_AgentRadiusServerAddress_Type = InetAddress
_AgentRadiusServerAddress_Object = MibTableColumn
agentRadiusServerAddress = _AgentRadiusServerAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 2),
    _AgentRadiusServerAddress_Type()
)
agentRadiusServerAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerAddress.setStatus("obsolete")
_AgentRadiusServerAddressType_Type = InetAddressType
_AgentRadiusServerAddressType_Object = MibTableColumn
agentRadiusServerAddressType = _AgentRadiusServerAddressType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 3),
    _AgentRadiusServerAddressType_Type()
)
agentRadiusServerAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerAddressType.setStatus("current")


class _AgentRadiusServerPort_Type(Unsigned32):
    """Custom type agentRadiusServerPort based on Unsigned32"""
    defaultValue = 1812

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_AgentRadiusServerPort_Type.__name__ = "Unsigned32"
_AgentRadiusServerPort_Object = MibTableColumn
agentRadiusServerPort = _AgentRadiusServerPort_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 4),
    _AgentRadiusServerPort_Type()
)
agentRadiusServerPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerPort.setStatus("current")


class _AgentRadiusServerSecret_Type(DisplayString):
    """Custom type agentRadiusServerSecret based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_AgentRadiusServerSecret_Type.__name__ = "DisplayString"
_AgentRadiusServerSecret_Object = MibTableColumn
agentRadiusServerSecret = _AgentRadiusServerSecret_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 5),
    _AgentRadiusServerSecret_Type()
)
agentRadiusServerSecret.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerSecret.setStatus("current")


class _AgentRadiusServerPrimaryMode_Type(Integer32):
    """Custom type agentRadiusServerPrimaryMode based on Integer32"""
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


_AgentRadiusServerPrimaryMode_Type.__name__ = "Integer32"
_AgentRadiusServerPrimaryMode_Object = MibTableColumn
agentRadiusServerPrimaryMode = _AgentRadiusServerPrimaryMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 6),
    _AgentRadiusServerPrimaryMode_Type()
)
agentRadiusServerPrimaryMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerPrimaryMode.setStatus("current")


class _AgentRadiusServerCurrentMode_Type(Integer32):
    """Custom type agentRadiusServerCurrentMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("yes", 1),
          ("no", 2))
    )


_AgentRadiusServerCurrentMode_Type.__name__ = "Integer32"
_AgentRadiusServerCurrentMode_Object = MibTableColumn
agentRadiusServerCurrentMode = _AgentRadiusServerCurrentMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 7),
    _AgentRadiusServerCurrentMode_Type()
)
agentRadiusServerCurrentMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusServerCurrentMode.setStatus("current")


class _AgentRadiusServerMsgAuth_Type(Integer32):
    """Custom type agentRadiusServerMsgAuth based on Integer32"""
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


_AgentRadiusServerMsgAuth_Type.__name__ = "Integer32"
_AgentRadiusServerMsgAuth_Object = MibTableColumn
agentRadiusServerMsgAuth = _AgentRadiusServerMsgAuth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 8),
    _AgentRadiusServerMsgAuth_Type()
)
agentRadiusServerMsgAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerMsgAuth.setStatus("current")
_AgentRadiusServerRowStatus_Type = RowStatus
_AgentRadiusServerRowStatus_Object = MibTableColumn
agentRadiusServerRowStatus = _AgentRadiusServerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 9),
    _AgentRadiusServerRowStatus_Type()
)
agentRadiusServerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerRowStatus.setStatus("current")


class _AgentRadiusServerName_Type(DisplayString):
    """Custom type agentRadiusServerName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentRadiusServerName_Type.__name__ = "DisplayString"
_AgentRadiusServerName_Object = MibTableColumn
agentRadiusServerName = _AgentRadiusServerName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 10),
    _AgentRadiusServerName_Type()
)
agentRadiusServerName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerName.setStatus("current")
_AgentRadiusServerInetAddress_Type = InetAddress
_AgentRadiusServerInetAddress_Object = MibTableColumn
agentRadiusServerInetAddress = _AgentRadiusServerInetAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 11),
    _AgentRadiusServerInetAddress_Type()
)
agentRadiusServerInetAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerInetAddress.setStatus("current")


class _AgentRadiusServerTimeout_Type(Unsigned32):
    """Custom type agentRadiusServerTimeout based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 30),
    )


_AgentRadiusServerTimeout_Type.__name__ = "Unsigned32"
_AgentRadiusServerTimeout_Object = MibTableColumn
agentRadiusServerTimeout = _AgentRadiusServerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 12),
    _AgentRadiusServerTimeout_Type()
)
agentRadiusServerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerTimeout.setStatus("current")


class _AgentRadiusServerRetransmit_Type(Unsigned32):
    """Custom type agentRadiusServerRetransmit based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AgentRadiusServerRetransmit_Type.__name__ = "Unsigned32"
_AgentRadiusServerRetransmit_Object = MibTableColumn
agentRadiusServerRetransmit = _AgentRadiusServerRetransmit_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 13),
    _AgentRadiusServerRetransmit_Type()
)
agentRadiusServerRetransmit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerRetransmit.setStatus("current")


class _AgentRadiusServerDeadtime_Type(Unsigned32):
    """Custom type agentRadiusServerDeadtime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_AgentRadiusServerDeadtime_Type.__name__ = "Unsigned32"
_AgentRadiusServerDeadtime_Object = MibTableColumn
agentRadiusServerDeadtime = _AgentRadiusServerDeadtime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 14),
    _AgentRadiusServerDeadtime_Type()
)
agentRadiusServerDeadtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerDeadtime.setStatus("current")
_AgentRadiusServerSourceIPAddr_Type = IpAddress
_AgentRadiusServerSourceIPAddr_Object = MibTableColumn
agentRadiusServerSourceIPAddr = _AgentRadiusServerSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 15),
    _AgentRadiusServerSourceIPAddr_Type()
)
agentRadiusServerSourceIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerSourceIPAddr.setStatus("current")


class _AgentRadiusServerPriority_Type(Unsigned32):
    """Custom type agentRadiusServerPriority based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AgentRadiusServerPriority_Type.__name__ = "Unsigned32"
_AgentRadiusServerPriority_Object = MibTableColumn
agentRadiusServerPriority = _AgentRadiusServerPriority_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 16),
    _AgentRadiusServerPriority_Type()
)
agentRadiusServerPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerPriority.setStatus("current")


class _AgentRadiusServerUsageType_Type(Integer32):
    """Custom type agentRadiusServerUsageType based on Integer32"""
    defaultValue = 1

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
        *(("all", 1),
          ("login", 2),
          ("dot1x", 3),
          ("authmgr", 4))
    )


_AgentRadiusServerUsageType_Type.__name__ = "Integer32"
_AgentRadiusServerUsageType_Object = MibTableColumn
agentRadiusServerUsageType = _AgentRadiusServerUsageType_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 17),
    _AgentRadiusServerUsageType_Type()
)
agentRadiusServerUsageType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerUsageType.setStatus("current")
_AgentRadiusServerSourceIPv6Addr_Type = InetAddress
_AgentRadiusServerSourceIPv6Addr_Object = MibTableColumn
agentRadiusServerSourceIPv6Addr = _AgentRadiusServerSourceIPv6Addr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 18),
    _AgentRadiusServerSourceIPv6Addr_Type()
)
agentRadiusServerSourceIPv6Addr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerSourceIPv6Addr.setStatus("current")


class _AgentRadiusServerConfigAttr31MacFormat_Type(Integer32):
    """Custom type agentRadiusServerConfigAttr31MacFormat based on Integer32"""
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
        *(("radiusFormatLegacyLowerCase", 1),
          ("radiusFormatLegacyUpperCase", 2),
          ("radiusFormatIetfLowerrCase", 3),
          ("radiusFormatIetfUpperCase", 4),
          ("radiusFormatUnformatLowerCase", 5),
          ("radiusFormatUnformatUpperCase", 6))
    )


_AgentRadiusServerConfigAttr31MacFormat_Type.__name__ = "Integer32"
_AgentRadiusServerConfigAttr31MacFormat_Object = MibTableColumn
agentRadiusServerConfigAttr31MacFormat = _AgentRadiusServerConfigAttr31MacFormat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 19),
    _AgentRadiusServerConfigAttr31MacFormat_Type()
)
agentRadiusServerConfigAttr31MacFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerConfigAttr31MacFormat.setStatus("deprecated")
_AgentRadiusServerLinkLocalIntf_Type = InterfaceIndexOrZero
_AgentRadiusServerLinkLocalIntf_Object = MibTableColumn
agentRadiusServerLinkLocalIntf = _AgentRadiusServerLinkLocalIntf_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 20),
    _AgentRadiusServerLinkLocalIntf_Type()
)
agentRadiusServerLinkLocalIntf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerLinkLocalIntf.setStatus("current")


class _AgentRadiusServerTestUserName_Type(DisplayString):
    """Custom type agentRadiusServerTestUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentRadiusServerTestUserName_Type.__name__ = "DisplayString"
_AgentRadiusServerTestUserName_Object = MibTableColumn
agentRadiusServerTestUserName = _AgentRadiusServerTestUserName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 21),
    _AgentRadiusServerTestUserName_Type()
)
agentRadiusServerTestUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    agentRadiusServerTestUserName.setStatus("current")


class _AgentRadiusServerIdleTime_Type(Unsigned32):
    """Custom type agentRadiusServerIdleTime based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 35791),
    )


_AgentRadiusServerIdleTime_Type.__name__ = "Unsigned32"
_AgentRadiusServerIdleTime_Object = MibTableColumn
agentRadiusServerIdleTime = _AgentRadiusServerIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 22),
    _AgentRadiusServerIdleTime_Type()
)
agentRadiusServerIdleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerIdleTime.setStatus("current")


class _AgentRadiusServerState_Type(Integer32):
    """Custom type agentRadiusServerState based on Integer32"""
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
        *(("up", 1),
          ("inactive", 2),
          ("dead", 3),
          ("quarantined", 4),
          ("unknown", 5))
    )


_AgentRadiusServerState_Type.__name__ = "Integer32"
_AgentRadiusServerState_Object = MibTableColumn
agentRadiusServerState = _AgentRadiusServerState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 23),
    _AgentRadiusServerState_Type()
)
agentRadiusServerState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusServerState.setStatus("current")
_AgentRadiusServerStateDuration_Type = Unsigned32
_AgentRadiusServerStateDuration_Object = MibTableColumn
agentRadiusServerStateDuration = _AgentRadiusServerStateDuration_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 24),
    _AgentRadiusServerStateDuration_Type()
)
agentRadiusServerStateDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusServerStateDuration.setStatus("current")


class _AgentRadiusServerImmortalState_Type(Integer32):
    """Custom type agentRadiusServerImmortalState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immortal", 1),
          ("mortal", 2))
    )


_AgentRadiusServerImmortalState_Type.__name__ = "Integer32"
_AgentRadiusServerImmortalState_Object = MibTableColumn
agentRadiusServerImmortalState = _AgentRadiusServerImmortalState_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 25),
    _AgentRadiusServerImmortalState_Type()
)
agentRadiusServerImmortalState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusServerImmortalState.setStatus("current")


class _AgentRadiusServerVSAAuth_Type(Integer32):
    """Custom type agentRadiusServerVSAAuth based on Integer32"""
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


_AgentRadiusServerVSAAuth_Type.__name__ = "Integer32"
_AgentRadiusServerVSAAuth_Object = MibTableColumn
agentRadiusServerVSAAuth = _AgentRadiusServerVSAAuth_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 8, 1, 26),
    _AgentRadiusServerVSAAuth_Type()
)
agentRadiusServerVSAAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerVSAAuth.setStatus("current")
_AgentRadiusAuthenticationServers_Type = Unsigned32
_AgentRadiusAuthenticationServers_Object = MibScalar
agentRadiusAuthenticationServers = _AgentRadiusAuthenticationServers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 9),
    _AgentRadiusAuthenticationServers_Type()
)
agentRadiusAuthenticationServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusAuthenticationServers.setStatus("current")
_AgentRadiusAccountingServers_Type = Unsigned32
_AgentRadiusAccountingServers_Object = MibScalar
agentRadiusAccountingServers = _AgentRadiusAccountingServers_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 10),
    _AgentRadiusAccountingServers_Type()
)
agentRadiusAccountingServers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusAccountingServers.setStatus("current")
_AgentRadiusNamedAuthenticationServerGroups_Type = Unsigned32
_AgentRadiusNamedAuthenticationServerGroups_Object = MibScalar
agentRadiusNamedAuthenticationServerGroups = _AgentRadiusNamedAuthenticationServerGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 11),
    _AgentRadiusNamedAuthenticationServerGroups_Type()
)
agentRadiusNamedAuthenticationServerGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusNamedAuthenticationServerGroups.setStatus("current")
_AgentRadiusNamedAccountingServerGroups_Type = Unsigned32
_AgentRadiusNamedAccountingServerGroups_Object = MibScalar
agentRadiusNamedAccountingServerGroups = _AgentRadiusNamedAccountingServerGroups_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 12),
    _AgentRadiusNamedAccountingServerGroups_Type()
)
agentRadiusNamedAccountingServerGroups.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusNamedAccountingServerGroups.setStatus("current")


class _AgentRadiusDeadTime_Type(Unsigned32):
    """Custom type agentRadiusDeadTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2000),
    )


_AgentRadiusDeadTime_Type.__name__ = "Unsigned32"
_AgentRadiusDeadTime_Object = MibScalar
agentRadiusDeadTime = _AgentRadiusDeadTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 13),
    _AgentRadiusDeadTime_Type()
)
agentRadiusDeadTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusDeadTime.setStatus("current")


class _AgentRadiusServerKey_Type(DisplayString):
    """Custom type agentRadiusServerKey based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AgentRadiusServerKey_Type.__name__ = "DisplayString"
_AgentRadiusServerKey_Object = MibScalar
agentRadiusServerKey = _AgentRadiusServerKey_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 14),
    _AgentRadiusServerKey_Type()
)
agentRadiusServerKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerKey.setStatus("current")
_AgentRadiusSourceIPAddr_Type = IpAddress
_AgentRadiusSourceIPAddr_Object = MibScalar
agentRadiusSourceIPAddr = _AgentRadiusSourceIPAddr_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 15),
    _AgentRadiusSourceIPAddr_Type()
)
agentRadiusSourceIPAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusSourceIPAddr.setStatus("current")
_AgentRadiusNasIpAddress_Type = IpAddress
_AgentRadiusNasIpAddress_Object = MibScalar
agentRadiusNasIpAddress = _AgentRadiusNasIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 16),
    _AgentRadiusNasIpAddress_Type()
)
agentRadiusNasIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusNasIpAddress.setStatus("current")


class _AgentAuthorizationNetworkRadiusMode_Type(Integer32):
    """Custom type agentAuthorizationNetworkRadiusMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_AgentAuthorizationNetworkRadiusMode_Type.__name__ = "Integer32"
_AgentAuthorizationNetworkRadiusMode_Object = MibScalar
agentAuthorizationNetworkRadiusMode = _AgentAuthorizationNetworkRadiusMode_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 17),
    _AgentAuthorizationNetworkRadiusMode_Type()
)
agentAuthorizationNetworkRadiusMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentAuthorizationNetworkRadiusMode.setStatus("current")
_AgentRadiusSourceInterface_Type = InterfaceIndexOrZero
_AgentRadiusSourceInterface_Object = MibScalar
agentRadiusSourceInterface = _AgentRadiusSourceInterface_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 18),
    _AgentRadiusSourceInterface_Type()
)
agentRadiusSourceInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusSourceInterface.setStatus("current")
_AgentDasRequestsReceived_Type = Unsigned32
_AgentDasRequestsReceived_Object = MibScalar
agentDasRequestsReceived = _AgentDasRequestsReceived_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 19),
    _AgentDasRequestsReceived_Type()
)
agentDasRequestsReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDasRequestsReceived.setStatus("current")
_AgentDasACKResponsesSent_Type = Unsigned32
_AgentDasACKResponsesSent_Object = MibScalar
agentDasACKResponsesSent = _AgentDasACKResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 20),
    _AgentDasACKResponsesSent_Type()
)
agentDasACKResponsesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDasACKResponsesSent.setStatus("current")
_AgentDasNAKResponsesSent_Type = Unsigned32
_AgentDasNAKResponsesSent_Object = MibScalar
agentDasNAKResponsesSent = _AgentDasNAKResponsesSent_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 21),
    _AgentDasNAKResponsesSent_Type()
)
agentDasNAKResponsesSent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDasNAKResponsesSent.setStatus("current")
_AgentDasRequestsIgnored_Type = Unsigned32
_AgentDasRequestsIgnored_Object = MibScalar
agentDasRequestsIgnored = _AgentDasRequestsIgnored_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 22),
    _AgentDasRequestsIgnored_Type()
)
agentDasRequestsIgnored.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDasRequestsIgnored.setStatus("current")
_AgentDasRequestsWithMissingOrUnsupportedAttribute_Type = Unsigned32
_AgentDasRequestsWithMissingOrUnsupportedAttribute_Object = MibScalar
agentDasRequestsWithMissingOrUnsupportedAttribute = _AgentDasRequestsWithMissingOrUnsupportedAttribute_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 23),
    _AgentDasRequestsWithMissingOrUnsupportedAttribute_Type()
)
agentDasRequestsWithMissingOrUnsupportedAttribute.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDasRequestsWithMissingOrUnsupportedAttribute.setStatus("current")
_AgentDasRequestsWithSessionContextNotFound_Type = Unsigned32
_AgentDasRequestsWithSessionContextNotFound_Object = MibScalar
agentDasRequestsWithSessionContextNotFound = _AgentDasRequestsWithSessionContextNotFound_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 24),
    _AgentDasRequestsWithSessionContextNotFound_Type()
)
agentDasRequestsWithSessionContextNotFound.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDasRequestsWithSessionContextNotFound.setStatus("current")
_AgentDasRequestsWithInvalidAttributeValue_Type = Unsigned32
_AgentDasRequestsWithInvalidAttributeValue_Object = MibScalar
agentDasRequestsWithInvalidAttributeValue = _AgentDasRequestsWithInvalidAttributeValue_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 25),
    _AgentDasRequestsWithInvalidAttributeValue_Type()
)
agentDasRequestsWithInvalidAttributeValue.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDasRequestsWithInvalidAttributeValue.setStatus("current")
_AgentDasRequestsAdministrativelyProhibited_Type = Unsigned32
_AgentDasRequestsAdministrativelyProhibited_Object = MibScalar
agentDasRequestsAdministrativelyProhibited = _AgentDasRequestsAdministrativelyProhibited_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 26),
    _AgentDasRequestsAdministrativelyProhibited_Type()
)
agentDasRequestsAdministrativelyProhibited.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentDasRequestsAdministrativelyProhibited.setStatus("current")


class _AgentRadiusServicePortSrcInterface_Type(Integer32):
    """Custom type agentRadiusServicePortSrcInterface based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("servicePortEnable", 1),
          ("servicePortDisable", 2))
    )


_AgentRadiusServicePortSrcInterface_Type.__name__ = "Integer32"
_AgentRadiusServicePortSrcInterface_Object = MibScalar
agentRadiusServicePortSrcInterface = _AgentRadiusServicePortSrcInterface_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 27),
    _AgentRadiusServicePortSrcInterface_Type()
)
agentRadiusServicePortSrcInterface.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServicePortSrcInterface.setStatus("current")
_AgentRadiusNasIpv6Address_Type = InetAddress
_AgentRadiusNasIpv6Address_Object = MibScalar
agentRadiusNasIpv6Address = _AgentRadiusNasIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 28),
    _AgentRadiusNasIpv6Address_Type()
)
agentRadiusNasIpv6Address.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusNasIpv6Address.setStatus("current")


class _AgentRadiusServerAttr31MacFormat_Type(Integer32):
    """Custom type agentRadiusServerAttr31MacFormat based on Integer32"""
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
        *(("radiusFormatLegacyLowerCase", 1),
          ("radiusFormatLegacyUpperCase", 2),
          ("radiusFormatIetfLowerrCase", 3),
          ("radiusFormatIetfUpperCase", 4),
          ("radiusFormatUnformatLowerCase", 5),
          ("radiusFormatUnformatUpperCase", 6))
    )


_AgentRadiusServerAttr31MacFormat_Type.__name__ = "Integer32"
_AgentRadiusServerAttr31MacFormat_Object = MibScalar
agentRadiusServerAttr31MacFormat = _AgentRadiusServerAttr31MacFormat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 29),
    _AgentRadiusServerAttr31MacFormat_Type()
)
agentRadiusServerAttr31MacFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerAttr31MacFormat.setStatus("current")


class _AgentRadiusServerAttr30MacFormat_Type(Integer32):
    """Custom type agentRadiusServerAttr30MacFormat based on Integer32"""
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
        *(("radiusFormatLegacyLowerCase", 1),
          ("radiusFormatLegacyUpperCase", 2),
          ("radiusFormatIetfLowerrCase", 3),
          ("radiusFormatIetfUpperCase", 4),
          ("radiusFormatUnformatLowerCase", 5),
          ("radiusFormatUnformatUpperCase", 6))
    )


_AgentRadiusServerAttr30MacFormat_Type.__name__ = "Integer32"
_AgentRadiusServerAttr30MacFormat_Object = MibScalar
agentRadiusServerAttr30MacFormat = _AgentRadiusServerAttr30MacFormat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 30),
    _AgentRadiusServerAttr30MacFormat_Type()
)
agentRadiusServerAttr30MacFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerAttr30MacFormat.setStatus("current")


class _AgentRadiusServerAttr32MacFormat_Type(Integer32):
    """Custom type agentRadiusServerAttr32MacFormat based on Integer32"""
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
        *(("radiusFormatLegacyLowerCase", 1),
          ("radiusFormatLegacyUpperCase", 2),
          ("radiusFormatIetfLowerrCase", 3),
          ("radiusFormatIetfUpperCase", 4),
          ("radiusFormatUnformatLowerCase", 5),
          ("radiusFormatUnformatUpperCase", 6))
    )


_AgentRadiusServerAttr32MacFormat_Type.__name__ = "Integer32"
_AgentRadiusServerAttr32MacFormat_Object = MibScalar
agentRadiusServerAttr32MacFormat = _AgentRadiusServerAttr32MacFormat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 31),
    _AgentRadiusServerAttr32MacFormat_Type()
)
agentRadiusServerAttr32MacFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerAttr32MacFormat.setStatus("current")


class _AgentRadiusServerInclude32InAccessRequest_Type(Integer32):
    """Custom type agentRadiusServerInclude32InAccessRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotInclude", 1),
          ("include", 2))
    )


_AgentRadiusServerInclude32InAccessRequest_Type.__name__ = "Integer32"
_AgentRadiusServerInclude32InAccessRequest_Object = MibScalar
agentRadiusServerInclude32InAccessRequest = _AgentRadiusServerInclude32InAccessRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 32),
    _AgentRadiusServerInclude32InAccessRequest_Type()
)
agentRadiusServerInclude32InAccessRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerInclude32InAccessRequest.setStatus("current")


class _AgentRadiusServerInclude32InAccessRequestFormat_Type(DisplayString):
    """Custom type agentRadiusServerInclude32InAccessRequestFormat based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 128),
    )


_AgentRadiusServerInclude32InAccessRequestFormat_Type.__name__ = "DisplayString"
_AgentRadiusServerInclude32InAccessRequestFormat_Object = MibScalar
agentRadiusServerInclude32InAccessRequestFormat = _AgentRadiusServerInclude32InAccessRequestFormat_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 33),
    _AgentRadiusServerInclude32InAccessRequestFormat_Type()
)
agentRadiusServerInclude32InAccessRequestFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerInclude32InAccessRequestFormat.setStatus("current")


class _AgentRadiusServerInclude44InAccessRequest_Type(Integer32):
    """Custom type agentRadiusServerInclude44InAccessRequest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("doNotInclude", 1),
          ("include", 2))
    )


_AgentRadiusServerInclude44InAccessRequest_Type.__name__ = "Integer32"
_AgentRadiusServerInclude44InAccessRequest_Object = MibScalar
agentRadiusServerInclude44InAccessRequest = _AgentRadiusServerInclude44InAccessRequest_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 34),
    _AgentRadiusServerInclude44InAccessRequest_Type()
)
agentRadiusServerInclude44InAccessRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerInclude44InAccessRequest.setStatus("current")
_AgentRadiusNamedAuthenticationServerGroupConfigTable_Object = MibTable
agentRadiusNamedAuthenticationServerGroupConfigTable = _AgentRadiusNamedAuthenticationServerGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 35)
)
if mibBuilder.loadTexts:
    agentRadiusNamedAuthenticationServerGroupConfigTable.setStatus("current")
_AgentRadiusNamedAuthenticationServerGroupConfigEntry_Object = MibTableRow
agentRadiusNamedAuthenticationServerGroupConfigEntry = _AgentRadiusNamedAuthenticationServerGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 35, 1)
)
agentRadiusNamedAuthenticationServerGroupConfigEntry.setIndexNames(
    (0, "LANCOM-RADIUS-AUTH-CLIENT-MIB", "agentRadiusNamedAuthenticationServerGroupName"),
)
if mibBuilder.loadTexts:
    agentRadiusNamedAuthenticationServerGroupConfigEntry.setStatus("current")


class _AgentRadiusNamedAuthenticationServerGroupName_Type(DisplayString):
    """Custom type agentRadiusNamedAuthenticationServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentRadiusNamedAuthenticationServerGroupName_Type.__name__ = "DisplayString"
_AgentRadiusNamedAuthenticationServerGroupName_Object = MibTableColumn
agentRadiusNamedAuthenticationServerGroupName = _AgentRadiusNamedAuthenticationServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 35, 1, 1),
    _AgentRadiusNamedAuthenticationServerGroupName_Type()
)
agentRadiusNamedAuthenticationServerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentRadiusNamedAuthenticationServerGroupName.setStatus("current")


class _AgentRadiusNamedAuthenticationServerGroupLoadBalanceMethod_Type(Integer32):
    """Custom type agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("least-outstanding-request", 2))
    )


_AgentRadiusNamedAuthenticationServerGroupLoadBalanceMethod_Type.__name__ = "Integer32"
_AgentRadiusNamedAuthenticationServerGroupLoadBalanceMethod_Object = MibTableColumn
agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod = _AgentRadiusNamedAuthenticationServerGroupLoadBalanceMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 35, 1, 2),
    _AgentRadiusNamedAuthenticationServerGroupLoadBalanceMethod_Type()
)
agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod.setStatus("current")


class _AgentRadiusNamedAuthenticationServerGroupBatchSize_Type(Unsigned32):
    """Custom type agentRadiusNamedAuthenticationServerGroupBatchSize based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusNamedAuthenticationServerGroupBatchSize_Type.__name__ = "Unsigned32"
_AgentRadiusNamedAuthenticationServerGroupBatchSize_Object = MibTableColumn
agentRadiusNamedAuthenticationServerGroupBatchSize = _AgentRadiusNamedAuthenticationServerGroupBatchSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 35, 1, 3),
    _AgentRadiusNamedAuthenticationServerGroupBatchSize_Type()
)
agentRadiusNamedAuthenticationServerGroupBatchSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusNamedAuthenticationServerGroupBatchSize.setStatus("current")
_AgentRadiusNamedAuthenticationServerGroupDeadCount_Type = Unsigned32
_AgentRadiusNamedAuthenticationServerGroupDeadCount_Object = MibTableColumn
agentRadiusNamedAuthenticationServerGroupDeadCount = _AgentRadiusNamedAuthenticationServerGroupDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 35, 1, 4),
    _AgentRadiusNamedAuthenticationServerGroupDeadCount_Type()
)
agentRadiusNamedAuthenticationServerGroupDeadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusNamedAuthenticationServerGroupDeadCount.setStatus("current")
_AgentRadiusNamedAccountingServerGroupConfigTable_Object = MibTable
agentRadiusNamedAccountingServerGroupConfigTable = _AgentRadiusNamedAccountingServerGroupConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 36)
)
if mibBuilder.loadTexts:
    agentRadiusNamedAccountingServerGroupConfigTable.setStatus("current")
_AgentRadiusNamedAccountingServerGroupConfigEntry_Object = MibTableRow
agentRadiusNamedAccountingServerGroupConfigEntry = _AgentRadiusNamedAccountingServerGroupConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 36, 1)
)
agentRadiusNamedAccountingServerGroupConfigEntry.setIndexNames(
    (0, "LANCOM-RADIUS-AUTH-CLIENT-MIB", "agentRadiusNamedAccountingServerGroupName"),
)
if mibBuilder.loadTexts:
    agentRadiusNamedAccountingServerGroupConfigEntry.setStatus("current")


class _AgentRadiusNamedAccountingServerGroupName_Type(DisplayString):
    """Custom type agentRadiusNamedAccountingServerGroupName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_AgentRadiusNamedAccountingServerGroupName_Type.__name__ = "DisplayString"
_AgentRadiusNamedAccountingServerGroupName_Object = MibTableColumn
agentRadiusNamedAccountingServerGroupName = _AgentRadiusNamedAccountingServerGroupName_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 36, 1, 1),
    _AgentRadiusNamedAccountingServerGroupName_Type()
)
agentRadiusNamedAccountingServerGroupName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    agentRadiusNamedAccountingServerGroupName.setStatus("current")


class _AgentRadiusNamedAccountingServerGroupLoadBalanceMethod_Type(Integer32):
    """Custom type agentRadiusNamedAccountingServerGroupLoadBalanceMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("least-outstanding-request", 2))
    )


_AgentRadiusNamedAccountingServerGroupLoadBalanceMethod_Type.__name__ = "Integer32"
_AgentRadiusNamedAccountingServerGroupLoadBalanceMethod_Object = MibTableColumn
agentRadiusNamedAccountingServerGroupLoadBalanceMethod = _AgentRadiusNamedAccountingServerGroupLoadBalanceMethod_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 36, 1, 2),
    _AgentRadiusNamedAccountingServerGroupLoadBalanceMethod_Type()
)
agentRadiusNamedAccountingServerGroupLoadBalanceMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusNamedAccountingServerGroupLoadBalanceMethod.setStatus("current")


class _AgentRadiusNamedAccountingServerGroupBatchSize_Type(Unsigned32):
    """Custom type agentRadiusNamedAccountingServerGroupBatchSize based on Unsigned32"""
    defaultValue = 25

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AgentRadiusNamedAccountingServerGroupBatchSize_Type.__name__ = "Unsigned32"
_AgentRadiusNamedAccountingServerGroupBatchSize_Object = MibTableColumn
agentRadiusNamedAccountingServerGroupBatchSize = _AgentRadiusNamedAccountingServerGroupBatchSize_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 36, 1, 3),
    _AgentRadiusNamedAccountingServerGroupBatchSize_Type()
)
agentRadiusNamedAccountingServerGroupBatchSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusNamedAccountingServerGroupBatchSize.setStatus("current")
_AgentRadiusNamedAccountingServerGroupDeadCount_Type = Unsigned32
_AgentRadiusNamedAccountingServerGroupDeadCount_Object = MibTableColumn
agentRadiusNamedAccountingServerGroupDeadCount = _AgentRadiusNamedAccountingServerGroupDeadCount_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 36, 1, 4),
    _AgentRadiusNamedAccountingServerGroupDeadCount_Type()
)
agentRadiusNamedAccountingServerGroupDeadCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    agentRadiusNamedAccountingServerGroupDeadCount.setStatus("current")


class _AgentRadiusServerDeadCriteriaTime_Type(Unsigned32):
    """Custom type agentRadiusServerDeadCriteriaTime based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 120),
    )


_AgentRadiusServerDeadCriteriaTime_Type.__name__ = "Unsigned32"
_AgentRadiusServerDeadCriteriaTime_Object = MibScalar
agentRadiusServerDeadCriteriaTime = _AgentRadiusServerDeadCriteriaTime_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 37),
    _AgentRadiusServerDeadCriteriaTime_Type()
)
agentRadiusServerDeadCriteriaTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerDeadCriteriaTime.setStatus("current")


class _AgentRadiusServerDeadCriteriaTries_Type(Unsigned32):
    """Custom type agentRadiusServerDeadCriteriaTries based on Unsigned32"""
    defaultValue = 4

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_AgentRadiusServerDeadCriteriaTries_Type.__name__ = "Unsigned32"
_AgentRadiusServerDeadCriteriaTries_Object = MibScalar
agentRadiusServerDeadCriteriaTries = _AgentRadiusServerDeadCriteriaTries_Object(
    (1, 3, 6, 1, 4, 1, 2356, 16, 1, 8, 1, 38),
    _AgentRadiusServerDeadCriteriaTries_Type()
)
agentRadiusServerDeadCriteriaTries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    agentRadiusServerDeadCriteriaTries.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANCOM-RADIUS-AUTH-CLIENT-MIB",
    **{"fastPathRadius": fastPathRadius,
       "agentRadiusConfigGroup": agentRadiusConfigGroup,
       "agentRadiusMaxTransmit": agentRadiusMaxTransmit,
       "agentRadiusTimeout": agentRadiusTimeout,
       "agentRadiusAccountingMode": agentRadiusAccountingMode,
       "agentRadiusStatsClear": agentRadiusStatsClear,
       "agentRadiusAccountingIndexNextValid": agentRadiusAccountingIndexNextValid,
       "agentRadiusAccountingConfigTable": agentRadiusAccountingConfigTable,
       "agentRadiusAccountingConfigEntry": agentRadiusAccountingConfigEntry,
       "agentRadiusAccountingServerIndex": agentRadiusAccountingServerIndex,
       "agentRadiusAccountingServerAddress": agentRadiusAccountingServerAddress,
       "agentRadiusAccountingServerAddressType": agentRadiusAccountingServerAddressType,
       "agentRadiusAccountingPort": agentRadiusAccountingPort,
       "agentRadiusAccountingSecret": agentRadiusAccountingSecret,
       "agentRadiusAccountingStatus": agentRadiusAccountingStatus,
       "agentRadiusAccountingServerName": agentRadiusAccountingServerName,
       "agentRadiusAccountingLinkLocalIntf": agentRadiusAccountingLinkLocalIntf,
       "agentRadiusAccountingServerTestUserName": agentRadiusAccountingServerTestUserName,
       "agentRadiusAccountingServerIdleTime": agentRadiusAccountingServerIdleTime,
       "agentRadiusAccountingServerState": agentRadiusAccountingServerState,
       "agentRadiusAccountingServerStateDuration": agentRadiusAccountingServerStateDuration,
       "agentRadiusAccountingServerImmortalState": agentRadiusAccountingServerImmortalState,
       "agentRadiusServerIndexNextValid": agentRadiusServerIndexNextValid,
       "agentRadiusServerConfigTable": agentRadiusServerConfigTable,
       "agentRadiusServerConfigEntry": agentRadiusServerConfigEntry,
       "agentRadiusServerIndex": agentRadiusServerIndex,
       "agentRadiusServerAddress": agentRadiusServerAddress,
       "agentRadiusServerAddressType": agentRadiusServerAddressType,
       "agentRadiusServerPort": agentRadiusServerPort,
       "agentRadiusServerSecret": agentRadiusServerSecret,
       "agentRadiusServerPrimaryMode": agentRadiusServerPrimaryMode,
       "agentRadiusServerCurrentMode": agentRadiusServerCurrentMode,
       "agentRadiusServerMsgAuth": agentRadiusServerMsgAuth,
       "agentRadiusServerRowStatus": agentRadiusServerRowStatus,
       "agentRadiusServerName": agentRadiusServerName,
       "agentRadiusServerInetAddress": agentRadiusServerInetAddress,
       "agentRadiusServerTimeout": agentRadiusServerTimeout,
       "agentRadiusServerRetransmit": agentRadiusServerRetransmit,
       "agentRadiusServerDeadtime": agentRadiusServerDeadtime,
       "agentRadiusServerSourceIPAddr": agentRadiusServerSourceIPAddr,
       "agentRadiusServerPriority": agentRadiusServerPriority,
       "agentRadiusServerUsageType": agentRadiusServerUsageType,
       "agentRadiusServerSourceIPv6Addr": agentRadiusServerSourceIPv6Addr,
       "agentRadiusServerConfigAttr31MacFormat": agentRadiusServerConfigAttr31MacFormat,
       "agentRadiusServerLinkLocalIntf": agentRadiusServerLinkLocalIntf,
       "agentRadiusServerTestUserName": agentRadiusServerTestUserName,
       "agentRadiusServerIdleTime": agentRadiusServerIdleTime,
       "agentRadiusServerState": agentRadiusServerState,
       "agentRadiusServerStateDuration": agentRadiusServerStateDuration,
       "agentRadiusServerImmortalState": agentRadiusServerImmortalState,
       "agentRadiusServerVSAAuth": agentRadiusServerVSAAuth,
       "agentRadiusAuthenticationServers": agentRadiusAuthenticationServers,
       "agentRadiusAccountingServers": agentRadiusAccountingServers,
       "agentRadiusNamedAuthenticationServerGroups": agentRadiusNamedAuthenticationServerGroups,
       "agentRadiusNamedAccountingServerGroups": agentRadiusNamedAccountingServerGroups,
       "agentRadiusDeadTime": agentRadiusDeadTime,
       "agentRadiusServerKey": agentRadiusServerKey,
       "agentRadiusSourceIPAddr": agentRadiusSourceIPAddr,
       "agentRadiusNasIpAddress": agentRadiusNasIpAddress,
       "agentAuthorizationNetworkRadiusMode": agentAuthorizationNetworkRadiusMode,
       "agentRadiusSourceInterface": agentRadiusSourceInterface,
       "agentDasRequestsReceived": agentDasRequestsReceived,
       "agentDasACKResponsesSent": agentDasACKResponsesSent,
       "agentDasNAKResponsesSent": agentDasNAKResponsesSent,
       "agentDasRequestsIgnored": agentDasRequestsIgnored,
       "agentDasRequestsWithMissingOrUnsupportedAttribute": agentDasRequestsWithMissingOrUnsupportedAttribute,
       "agentDasRequestsWithSessionContextNotFound": agentDasRequestsWithSessionContextNotFound,
       "agentDasRequestsWithInvalidAttributeValue": agentDasRequestsWithInvalidAttributeValue,
       "agentDasRequestsAdministrativelyProhibited": agentDasRequestsAdministrativelyProhibited,
       "agentRadiusServicePortSrcInterface": agentRadiusServicePortSrcInterface,
       "agentRadiusNasIpv6Address": agentRadiusNasIpv6Address,
       "agentRadiusServerAttr31MacFormat": agentRadiusServerAttr31MacFormat,
       "agentRadiusServerAttr30MacFormat": agentRadiusServerAttr30MacFormat,
       "agentRadiusServerAttr32MacFormat": agentRadiusServerAttr32MacFormat,
       "agentRadiusServerInclude32InAccessRequest": agentRadiusServerInclude32InAccessRequest,
       "agentRadiusServerInclude32InAccessRequestFormat": agentRadiusServerInclude32InAccessRequestFormat,
       "agentRadiusServerInclude44InAccessRequest": agentRadiusServerInclude44InAccessRequest,
       "agentRadiusNamedAuthenticationServerGroupConfigTable": agentRadiusNamedAuthenticationServerGroupConfigTable,
       "agentRadiusNamedAuthenticationServerGroupConfigEntry": agentRadiusNamedAuthenticationServerGroupConfigEntry,
       "agentRadiusNamedAuthenticationServerGroupName": agentRadiusNamedAuthenticationServerGroupName,
       "agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod": agentRadiusNamedAuthenticationServerGroupLoadBalanceMethod,
       "agentRadiusNamedAuthenticationServerGroupBatchSize": agentRadiusNamedAuthenticationServerGroupBatchSize,
       "agentRadiusNamedAuthenticationServerGroupDeadCount": agentRadiusNamedAuthenticationServerGroupDeadCount,
       "agentRadiusNamedAccountingServerGroupConfigTable": agentRadiusNamedAccountingServerGroupConfigTable,
       "agentRadiusNamedAccountingServerGroupConfigEntry": agentRadiusNamedAccountingServerGroupConfigEntry,
       "agentRadiusNamedAccountingServerGroupName": agentRadiusNamedAccountingServerGroupName,
       "agentRadiusNamedAccountingServerGroupLoadBalanceMethod": agentRadiusNamedAccountingServerGroupLoadBalanceMethod,
       "agentRadiusNamedAccountingServerGroupBatchSize": agentRadiusNamedAccountingServerGroupBatchSize,
       "agentRadiusNamedAccountingServerGroupDeadCount": agentRadiusNamedAccountingServerGroupDeadCount,
       "agentRadiusServerDeadCriteriaTime": agentRadiusServerDeadCriteriaTime,
       "agentRadiusServerDeadCriteriaTries": agentRadiusServerDeadCriteriaTries}
)
