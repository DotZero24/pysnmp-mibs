# SNMP MIB module (RUGGEDCOM-SERIAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/RUGGEDCOM-SERIAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:37 2025
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

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(ruggedcomMgmt,) = mibBuilder.importSymbols(
    "RUGGEDCOM-MIB",
    "ruggedcomMgmt")

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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

rcSerial = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6)
)
if mibBuilder.loadTexts:
    rcSerial.setRevisions(
        ("2011-01-11 10:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class EnabledStatus(TextualConvention, Integer32):
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



class RcFlowControl(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("xonXoff", 2))
    )



class RcSerProtocol(TextualConvention, Integer32):
    status = "current"
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
        *(("noProtocol", 1),
          ("rawSock", 2),
          ("modbusServer", 3),
          ("modbusClient", 4),
          ("itcsWIN", 5),
          ("itcsTIN", 6),
          ("microlok", 7),
          ("dnp", 8),
          ("dnpRawSock", 9),
          ("mirrorBits", 10),
          ("preemptRawSock", 11),
          ("telnetComport", 12))
    )



class RcTransport(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("tcp", 2))
    )



class RcCallDir(TextualConvention, Integer32):
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
        *(("in", 0),
          ("out", 1),
          ("both", 2))
    )



class RcSerPortType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("rs232", 1),
          ("rs485", 2),
          ("rs422", 3),
          ("tpc", 4),
          ("fiber", 5))
    )



# MIB Managed Objects in the order of their OIDs

_RcSerialPortParams_ObjectIdentity = ObjectIdentity
rcSerialPortParams = _RcSerialPortParams_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1)
)
if mibBuilder.loadTexts:
    rcSerialPortParams.setStatus("current")
_RcSerialPortTable_Object = MibTable
rcSerialPortTable = _RcSerialPortTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1)
)
if mibBuilder.loadTexts:
    rcSerialPortTable.setStatus("current")
_RcSerialPortEntry_Object = MibTableRow
rcSerialPortEntry = _RcSerialPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1)
)
rcSerialPortEntry.setIndexNames(
    (0, "RUGGEDCOM-SERIAL-MIB", "rcSerialPortNumber"),
)
if mibBuilder.loadTexts:
    rcSerialPortEntry.setStatus("current")


class _RcSerialPortNumber_Type(Integer32):
    """Custom type rcSerialPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcSerialPortNumber_Type.__name__ = "Integer32"
_RcSerialPortNumber_Object = MibTableColumn
rcSerialPortNumber = _RcSerialPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1, 1),
    _RcSerialPortNumber_Type()
)
rcSerialPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcSerialPortNumber.setStatus("current")
_RcSerialPortIfIndex_Type = InterfaceIndex
_RcSerialPortIfIndex_Object = MibTableColumn
rcSerialPortIfIndex = _RcSerialPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1, 2),
    _RcSerialPortIfIndex_Type()
)
rcSerialPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcSerialPortIfIndex.setStatus("current")
_RcSerialProtocol_Type = RcSerProtocol
_RcSerialProtocol_Object = MibTableColumn
rcSerialProtocol = _RcSerialProtocol_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1, 3),
    _RcSerialProtocol_Type()
)
rcSerialProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSerialProtocol.setStatus("current")
_RcSerialPortType_Type = RcSerPortType
_RcSerialPortType_Object = MibTableColumn
rcSerialPortType = _RcSerialPortType_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1, 4),
    _RcSerialPortType_Type()
)
rcSerialPortType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSerialPortType.setStatus("current")


class _RcSerialForceHD_Type(Integer32):
    """Custom type rcSerialForceHD based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("on", 1),
          ("off", 2),
          ("notApplicable", 3))
    )


_RcSerialForceHD_Type.__name__ = "Integer32"
_RcSerialForceHD_Object = MibTableColumn
rcSerialForceHD = _RcSerialForceHD_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1, 5),
    _RcSerialForceHD_Type()
)
rcSerialForceHD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSerialForceHD.setStatus("current")


class _RcSerialTurnAround_Type(Integer32):
    """Custom type rcSerialTurnAround based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcSerialTurnAround_Type.__name__ = "Integer32"
_RcSerialTurnAround_Object = MibTableColumn
rcSerialTurnAround = _RcSerialTurnAround_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1, 6),
    _RcSerialTurnAround_Type()
)
rcSerialTurnAround.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSerialTurnAround.setStatus("current")
if mibBuilder.loadTexts:
    rcSerialTurnAround.setUnits("milliseconds")


class _RcSerialPostTxDelay_Type(Integer32):
    """Custom type rcSerialPostTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_RcSerialPostTxDelay_Type.__name__ = "Integer32"
_RcSerialPostTxDelay_Object = MibTableColumn
rcSerialPostTxDelay = _RcSerialPostTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1, 7),
    _RcSerialPostTxDelay_Type()
)
rcSerialPostTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSerialPostTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    rcSerialPostTxDelay.setUnits("bits")


class _RcSerialHoldTime_Type(Integer32):
    """Custom type rcSerialHoldTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15000),
    )


_RcSerialHoldTime_Type.__name__ = "Integer32"
_RcSerialHoldTime_Object = MibTableColumn
rcSerialHoldTime = _RcSerialHoldTime_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1, 8),
    _RcSerialHoldTime_Type()
)
rcSerialHoldTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSerialHoldTime.setStatus("current")
if mibBuilder.loadTexts:
    rcSerialHoldTime.setUnits("milliseconds")


class _RcSerialDscp_Type(Integer32):
    """Custom type rcSerialDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcSerialDscp_Type.__name__ = "Integer32"
_RcSerialDscp_Object = MibTableColumn
rcSerialDscp = _RcSerialDscp_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1, 9),
    _RcSerialDscp_Type()
)
rcSerialDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSerialDscp.setStatus("current")


class _RcSerialRxtoTxDelay_Type(Integer32):
    """Custom type rcSerialRxtoTxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_RcSerialRxtoTxDelay_Type.__name__ = "Integer32"
_RcSerialRxtoTxDelay_Object = MibTableColumn
rcSerialRxtoTxDelay = _RcSerialRxtoTxDelay_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 1, 1, 1, 10),
    _RcSerialRxtoTxDelay_Type()
)
rcSerialRxtoTxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSerialRxtoTxDelay.setStatus("current")
if mibBuilder.loadTexts:
    rcSerialRxtoTxDelay.setUnits("milliseconds")
_RcMbServer_ObjectIdentity = ObjectIdentity
rcMbServer = _RcMbServer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 2)
)
if mibBuilder.loadTexts:
    rcMbServer.setStatus("current")
_RcMbServerTable_Object = MibTable
rcMbServerTable = _RcMbServerTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 2, 1)
)
if mibBuilder.loadTexts:
    rcMbServerTable.setStatus("current")
_RcMbServerEntry_Object = MibTableRow
rcMbServerEntry = _RcMbServerEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 2, 1, 1)
)
rcMbServerEntry.setIndexNames(
    (0, "RUGGEDCOM-SERIAL-MIB", "rcMbServerPort"),
)
if mibBuilder.loadTexts:
    rcMbServerEntry.setStatus("current")


class _RcMbServerPort_Type(Integer32):
    """Custom type rcMbServerPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcMbServerPort_Type.__name__ = "Integer32"
_RcMbServerPort_Object = MibTableColumn
rcMbServerPort = _RcMbServerPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 2, 1, 1, 1),
    _RcMbServerPort_Type()
)
rcMbServerPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMbServerPort.setStatus("current")


class _RcMbServerRespTimer_Type(Integer32):
    """Custom type rcMbServerRespTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(50, 10000),
    )


_RcMbServerRespTimer_Type.__name__ = "Integer32"
_RcMbServerRespTimer_Object = MibTableColumn
rcMbServerRespTimer = _RcMbServerRespTimer_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 2, 1, 1, 2),
    _RcMbServerRespTimer_Type()
)
rcMbServerRespTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMbServerRespTimer.setStatus("current")
if mibBuilder.loadTexts:
    rcMbServerRespTimer.setUnits("milliseconds")


class _RcMbServerAuxTcpPort_Type(Integer32):
    """Custom type rcMbServerAuxTcpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcMbServerAuxTcpPort_Type.__name__ = "Integer32"
_RcMbServerAuxTcpPort_Object = MibTableColumn
rcMbServerAuxTcpPort = _RcMbServerAuxTcpPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 2, 1, 1, 3),
    _RcMbServerAuxTcpPort_Type()
)
rcMbServerAuxTcpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMbServerAuxTcpPort.setStatus("current")
_RcMbServerSendExcep_Type = EnabledStatus
_RcMbServerSendExcep_Object = MibTableColumn
rcMbServerSendExcep = _RcMbServerSendExcep_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 2, 1, 1, 4),
    _RcMbServerSendExcep_Type()
)
rcMbServerSendExcep.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMbServerSendExcep.setStatus("current")
_RcMbServerLinkStats_Type = EnabledStatus
_RcMbServerLinkStats_Object = MibTableColumn
rcMbServerLinkStats = _RcMbServerLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 2, 1, 1, 5),
    _RcMbServerLinkStats_Type()
)
rcMbServerLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMbServerLinkStats.setStatus("current")
_RcMbClient_ObjectIdentity = ObjectIdentity
rcMbClient = _RcMbClient_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 3)
)
if mibBuilder.loadTexts:
    rcMbClient.setStatus("current")


class _RcMbClientIPPort_Type(Integer32):
    """Custom type rcMbClientIPPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcMbClientIPPort_Type.__name__ = "Integer32"
_RcMbClientIPPort_Object = MibScalar
rcMbClientIPPort = _RcMbClientIPPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 3, 1),
    _RcMbClientIPPort_Type()
)
rcMbClientIPPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMbClientIPPort.setStatus("current")
_RcMbClientFwdExcp_Type = EnabledStatus
_RcMbClientFwdExcp_Object = MibScalar
rcMbClientFwdExcp = _RcMbClientFwdExcp_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 3, 2),
    _RcMbClientFwdExcp_Type()
)
rcMbClientFwdExcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMbClientFwdExcp.setStatus("current")
_RcMbClientLinkStats_Type = EnabledStatus
_RcMbClientLinkStats_Object = MibScalar
rcMbClientLinkStats = _RcMbClientLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 3, 3),
    _RcMbClientLinkStats_Type()
)
rcMbClientLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMbClientLinkStats.setStatus("current")


class _RcMbClientDscp_Type(Integer32):
    """Custom type rcMbClientDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcMbClientDscp_Type.__name__ = "Integer32"
_RcMbClientDscp_Object = MibScalar
rcMbClientDscp = _RcMbClientDscp_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 3, 4),
    _RcMbClientDscp_Type()
)
rcMbClientDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMbClientDscp.setStatus("current")
_RcRawSock_ObjectIdentity = ObjectIdentity
rcRawSock = _RcRawSock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4)
)
if mibBuilder.loadTexts:
    rcRawSock.setStatus("current")
_RcRawSockTable_Object = MibTable
rcRawSockTable = _RcRawSockTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1)
)
if mibBuilder.loadTexts:
    rcRawSockTable.setStatus("current")
_RcRawSockEntry_Object = MibTableRow
rcRawSockEntry = _RcRawSockEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1)
)
rcRawSockEntry.setIndexNames(
    (0, "RUGGEDCOM-SERIAL-MIB", "rcRawSockPort"),
)
if mibBuilder.loadTexts:
    rcRawSockEntry.setStatus("current")


class _RcRawSockPort_Type(Integer32):
    """Custom type rcRawSockPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcRawSockPort_Type.__name__ = "Integer32"
_RcRawSockPort_Object = MibTableColumn
rcRawSockPort = _RcRawSockPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 1),
    _RcRawSockPort_Type()
)
rcRawSockPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcRawSockPort.setStatus("current")


class _RcRawSockPackChar_Type(Integer32):
    """Custom type rcRawSockPackChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RcRawSockPackChar_Type.__name__ = "Integer32"
_RcRawSockPackChar_Object = MibTableColumn
rcRawSockPackChar = _RcRawSockPackChar_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 2),
    _RcRawSockPackChar_Type()
)
rcRawSockPackChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockPackChar.setStatus("current")


class _RcRawSockPackTimer_Type(Integer32):
    """Custom type rcRawSockPackTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_RcRawSockPackTimer_Type.__name__ = "Integer32"
_RcRawSockPackTimer_Object = MibTableColumn
rcRawSockPackTimer = _RcRawSockPackTimer_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 3),
    _RcRawSockPackTimer_Type()
)
rcRawSockPackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockPackTimer.setStatus("current")
if mibBuilder.loadTexts:
    rcRawSockPackTimer.setUnits("milliseconds")


class _RcRawSockPackSize_Type(Integer32):
    """Custom type rcRawSockPackSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1401),
    )


_RcRawSockPackSize_Type.__name__ = "Integer32"
_RcRawSockPackSize_Object = MibTableColumn
rcRawSockPackSize = _RcRawSockPackSize_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 4),
    _RcRawSockPackSize_Type()
)
rcRawSockPackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockPackSize.setStatus("current")
if mibBuilder.loadTexts:
    rcRawSockPackSize.setUnits("bytes")
_RcRawSockFlowControl_Type = RcFlowControl
_RcRawSockFlowControl_Object = MibTableColumn
rcRawSockFlowControl = _RcRawSockFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 5),
    _RcRawSockFlowControl_Type()
)
rcRawSockFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockFlowControl.setStatus("current")
_RcRawSockTransport_Type = RcTransport
_RcRawSockTransport_Object = MibTableColumn
rcRawSockTransport = _RcRawSockTransport_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 6),
    _RcRawSockTransport_Type()
)
rcRawSockTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockTransport.setStatus("current")
_RcRawSockCallDir_Type = RcCallDir
_RcRawSockCallDir_Object = MibTableColumn
rcRawSockCallDir = _RcRawSockCallDir_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 7),
    _RcRawSockCallDir_Type()
)
rcRawSockCallDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockCallDir.setStatus("current")


class _RcRawSockMaxConn_Type(Integer32):
    """Custom type rcRawSockMaxConn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RcRawSockMaxConn_Type.__name__ = "Integer32"
_RcRawSockMaxConn_Object = MibTableColumn
rcRawSockMaxConn = _RcRawSockMaxConn_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 8),
    _RcRawSockMaxConn_Type()
)
rcRawSockMaxConn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockMaxConn.setStatus("current")


class _RcRawSockLocPort_Type(Integer32):
    """Custom type rcRawSockLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcRawSockLocPort_Type.__name__ = "Integer32"
_RcRawSockLocPort_Object = MibTableColumn
rcRawSockLocPort = _RcRawSockLocPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 9),
    _RcRawSockLocPort_Type()
)
rcRawSockLocPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockLocPort.setStatus("current")


class _RcRawSockRemPort_Type(Integer32):
    """Custom type rcRawSockRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcRawSockRemPort_Type.__name__ = "Integer32"
_RcRawSockRemPort_Object = MibTableColumn
rcRawSockRemPort = _RcRawSockRemPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 10),
    _RcRawSockRemPort_Type()
)
rcRawSockRemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockRemPort.setStatus("current")
_RcRawSockIpAdd_Type = IpAddress
_RcRawSockIpAdd_Object = MibTableColumn
rcRawSockIpAdd = _RcRawSockIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 11),
    _RcRawSockIpAdd_Type()
)
rcRawSockIpAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockIpAdd.setStatus("current")
_RcRawSockLinkStats_Type = EnabledStatus
_RcRawSockLinkStats_Object = MibTableColumn
rcRawSockLinkStats = _RcRawSockLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 4, 1, 1, 12),
    _RcRawSockLinkStats_Type()
)
rcRawSockLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcRawSockLinkStats.setStatus("current")
_RcPreemptRS_ObjectIdentity = ObjectIdentity
rcPreemptRS = _RcPreemptRS_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5)
)
if mibBuilder.loadTexts:
    rcPreemptRS.setStatus("current")
_RcPreemptRSTable_Object = MibTable
rcPreemptRSTable = _RcPreemptRSTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1)
)
if mibBuilder.loadTexts:
    rcPreemptRSTable.setStatus("current")
_RcPreemptRSEntry_Object = MibTableRow
rcPreemptRSEntry = _RcPreemptRSEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1)
)
rcPreemptRSEntry.setIndexNames(
    (0, "RUGGEDCOM-SERIAL-MIB", "rcPreemptRSPort"),
)
if mibBuilder.loadTexts:
    rcPreemptRSEntry.setStatus("current")


class _RcPreemptRSPort_Type(Integer32):
    """Custom type rcPreemptRSPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcPreemptRSPort_Type.__name__ = "Integer32"
_RcPreemptRSPort_Object = MibTableColumn
rcPreemptRSPort = _RcPreemptRSPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 1),
    _RcPreemptRSPort_Type()
)
rcPreemptRSPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcPreemptRSPort.setStatus("current")


class _RcPreemptRSPackChar_Type(Integer32):
    """Custom type rcPreemptRSPackChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RcPreemptRSPackChar_Type.__name__ = "Integer32"
_RcPreemptRSPackChar_Object = MibTableColumn
rcPreemptRSPackChar = _RcPreemptRSPackChar_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 2),
    _RcPreemptRSPackChar_Type()
)
rcPreemptRSPackChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSPackChar.setStatus("current")


class _RcPreemptRSPackTimer_Type(Integer32):
    """Custom type rcPreemptRSPackTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_RcPreemptRSPackTimer_Type.__name__ = "Integer32"
_RcPreemptRSPackTimer_Object = MibTableColumn
rcPreemptRSPackTimer = _RcPreemptRSPackTimer_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 3),
    _RcPreemptRSPackTimer_Type()
)
rcPreemptRSPackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSPackTimer.setStatus("current")
if mibBuilder.loadTexts:
    rcPreemptRSPackTimer.setUnits("milliseconds")


class _RcPreemptRSPackSize_Type(Integer32):
    """Custom type rcPreemptRSPackSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1400),
    )


_RcPreemptRSPackSize_Type.__name__ = "Integer32"
_RcPreemptRSPackSize_Object = MibTableColumn
rcPreemptRSPackSize = _RcPreemptRSPackSize_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 4),
    _RcPreemptRSPackSize_Type()
)
rcPreemptRSPackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSPackSize.setStatus("current")
if mibBuilder.loadTexts:
    rcPreemptRSPackSize.setUnits("bytes")
_RcPreemptRSFlowControl_Type = RcFlowControl
_RcPreemptRSFlowControl_Object = MibTableColumn
rcPreemptRSFlowControl = _RcPreemptRSFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 5),
    _RcPreemptRSFlowControl_Type()
)
rcPreemptRSFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSFlowControl.setStatus("current")


class _RcPreemptRSLocPort_Type(Integer32):
    """Custom type rcPreemptRSLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcPreemptRSLocPort_Type.__name__ = "Integer32"
_RcPreemptRSLocPort_Object = MibTableColumn
rcPreemptRSLocPort = _RcPreemptRSLocPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 6),
    _RcPreemptRSLocPort_Type()
)
rcPreemptRSLocPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSLocPort.setStatus("current")


class _RcPreemptRSRemPort_Type(Integer32):
    """Custom type rcPreemptRSRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcPreemptRSRemPort_Type.__name__ = "Integer32"
_RcPreemptRSRemPort_Object = MibTableColumn
rcPreemptRSRemPort = _RcPreemptRSRemPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 7),
    _RcPreemptRSRemPort_Type()
)
rcPreemptRSRemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSRemPort.setStatus("current")
_RcPreemptRSIpAdd_Type = IpAddress
_RcPreemptRSIpAdd_Object = MibTableColumn
rcPreemptRSIpAdd = _RcPreemptRSIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 8),
    _RcPreemptRSIpAdd_Type()
)
rcPreemptRSIpAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSIpAdd.setStatus("current")
_RcPreemptRSLinkStats_Type = EnabledStatus
_RcPreemptRSLinkStats_Object = MibTableColumn
rcPreemptRSLinkStats = _RcPreemptRSLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 9),
    _RcPreemptRSLinkStats_Type()
)
rcPreemptRSLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSLinkStats.setStatus("current")


class _RcPreemptRSDynPackChar_Type(Integer32):
    """Custom type rcPreemptRSDynPackChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RcPreemptRSDynPackChar_Type.__name__ = "Integer32"
_RcPreemptRSDynPackChar_Object = MibTableColumn
rcPreemptRSDynPackChar = _RcPreemptRSDynPackChar_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 10),
    _RcPreemptRSDynPackChar_Type()
)
rcPreemptRSDynPackChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSDynPackChar.setStatus("current")


class _RcPreemptRSDynPackTimer_Type(Integer32):
    """Custom type rcPreemptRSDynPackTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_RcPreemptRSDynPackTimer_Type.__name__ = "Integer32"
_RcPreemptRSDynPackTimer_Object = MibTableColumn
rcPreemptRSDynPackTimer = _RcPreemptRSDynPackTimer_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 11),
    _RcPreemptRSDynPackTimer_Type()
)
rcPreemptRSDynPackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSDynPackTimer.setStatus("current")
if mibBuilder.loadTexts:
    rcPreemptRSDynPackTimer.setUnits("milliseconds")


class _RcPreemptRSDynTimeout_Type(Integer32):
    """Custom type rcPreemptRSDynTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 3600),
    )


_RcPreemptRSDynTimeout_Type.__name__ = "Integer32"
_RcPreemptRSDynTimeout_Object = MibTableColumn
rcPreemptRSDynTimeout = _RcPreemptRSDynTimeout_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 5, 1, 1, 12),
    _RcPreemptRSDynTimeout_Type()
)
rcPreemptRSDynTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcPreemptRSDynTimeout.setStatus("current")
if mibBuilder.loadTexts:
    rcPreemptRSDynTimeout.setUnits("seconds")
_RcTinAndWin_ObjectIdentity = ObjectIdentity
rcTinAndWin = _RcTinAndWin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6)
)
if mibBuilder.loadTexts:
    rcTinAndWin.setStatus("current")


class _RcTinAndWinTinMode_Type(Integer32):
    """Custom type rcTinAndWinTinMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tin1", 1),
          ("tin2", 2))
    )


_RcTinAndWinTinMode_Type.__name__ = "Integer32"
_RcTinAndWinTinMode_Object = MibScalar
rcTinAndWinTinMode = _RcTinAndWinTinMode_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 1),
    _RcTinAndWinTinMode_Type()
)
rcTinAndWinTinMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinTinMode.setStatus("current")
_RcTinAndWinTinTrans_Type = RcTransport
_RcTinAndWinTinTrans_Object = MibScalar
rcTinAndWinTinTrans = _RcTinAndWinTinTrans_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 2),
    _RcTinAndWinTinTrans_Type()
)
rcTinAndWinTinTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinTinTrans.setStatus("current")
_RcTinAndWinWinTrans_Type = RcTransport
_RcTinAndWinWinTrans_Object = MibScalar
rcTinAndWinWinTrans = _RcTinAndWinWinTrans_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 3),
    _RcTinAndWinWinTrans_Type()
)
rcTinAndWinWinTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinWinTrans.setStatus("current")


class _RcTinAndWinTinIpPort_Type(Integer32):
    """Custom type rcTinAndWinTinIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcTinAndWinTinIpPort_Type.__name__ = "Integer32"
_RcTinAndWinTinIpPort_Object = MibScalar
rcTinAndWinTinIpPort = _RcTinAndWinTinIpPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 4),
    _RcTinAndWinTinIpPort_Type()
)
rcTinAndWinTinIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinTinIpPort.setStatus("current")


class _RcTinAndWinWinIpPort_Type(Integer32):
    """Custom type rcTinAndWinWinIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcTinAndWinWinIpPort_Type.__name__ = "Integer32"
_RcTinAndWinWinIpPort_Object = MibScalar
rcTinAndWinWinIpPort = _RcTinAndWinWinIpPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 5),
    _RcTinAndWinWinIpPort_Type()
)
rcTinAndWinWinIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinWinIpPort.setStatus("current")


class _RcTinAndWinMsgAgingTime_Type(Integer32):
    """Custom type rcTinAndWinMsgAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_RcTinAndWinMsgAgingTime_Type.__name__ = "Integer32"
_RcTinAndWinMsgAgingTime_Object = MibScalar
rcTinAndWinMsgAgingTime = _RcTinAndWinMsgAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 6),
    _RcTinAndWinMsgAgingTime_Type()
)
rcTinAndWinMsgAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinMsgAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    rcTinAndWinMsgAgingTime.setUnits("seconds")


class _RcTinAndWinAddrAgingTime_Type(Integer32):
    """Custom type rcTinAndWinAddrAgingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000),
    )


_RcTinAndWinAddrAgingTime_Type.__name__ = "Integer32"
_RcTinAndWinAddrAgingTime_Object = MibScalar
rcTinAndWinAddrAgingTime = _RcTinAndWinAddrAgingTime_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 7),
    _RcTinAndWinAddrAgingTime_Type()
)
rcTinAndWinAddrAgingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinAddrAgingTime.setStatus("current")
if mibBuilder.loadTexts:
    rcTinAndWinAddrAgingTime.setUnits("milliseconds")


class _RcTinAndWinBroadCastAddr_Type(Integer32):
    """Custom type rcTinAndWinBroadCastAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("staticAndDynamic", 3))
    )


_RcTinAndWinBroadCastAddr_Type.__name__ = "Integer32"
_RcTinAndWinBroadCastAddr_Object = MibScalar
rcTinAndWinBroadCastAddr = _RcTinAndWinBroadCastAddr_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 8),
    _RcTinAndWinBroadCastAddr_Type()
)
rcTinAndWinBroadCastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinBroadCastAddr.setStatus("current")


class _RcTinAndWinUniAddr_Type(Integer32):
    """Custom type rcTinAndWinUniAddr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("staticAndDynamic", 3))
    )


_RcTinAndWinUniAddr_Type.__name__ = "Integer32"
_RcTinAndWinUniAddr_Object = MibScalar
rcTinAndWinUniAddr = _RcTinAndWinUniAddr_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 9),
    _RcTinAndWinUniAddr_Type()
)
rcTinAndWinUniAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinUniAddr.setStatus("current")
_RcTinAndWinLinkStats_Type = EnabledStatus
_RcTinAndWinLinkStats_Object = MibScalar
rcTinAndWinLinkStats = _RcTinAndWinLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 10),
    _RcTinAndWinLinkStats_Type()
)
rcTinAndWinLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinLinkStats.setStatus("current")


class _RcTinAndWinWinDscp_Type(Integer32):
    """Custom type rcTinAndWinWinDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcTinAndWinWinDscp_Type.__name__ = "Integer32"
_RcTinAndWinWinDscp_Object = MibScalar
rcTinAndWinWinDscp = _RcTinAndWinWinDscp_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 11),
    _RcTinAndWinWinDscp_Type()
)
rcTinAndWinWinDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinWinDscp.setStatus("current")


class _RcTinAndWinTinDscp_Type(Integer32):
    """Custom type rcTinAndWinTinDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcTinAndWinTinDscp_Type.__name__ = "Integer32"
_RcTinAndWinTinDscp_Object = MibScalar
rcTinAndWinTinDscp = _RcTinAndWinTinDscp_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 6, 12),
    _RcTinAndWinTinDscp_Type()
)
rcTinAndWinTinDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTinAndWinTinDscp.setStatus("current")
_RcMicrolok_ObjectIdentity = ObjectIdentity
rcMicrolok = _RcMicrolok_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 7)
)
if mibBuilder.loadTexts:
    rcMicrolok.setStatus("current")
_RcMicrolokTransport_Type = RcTransport
_RcMicrolokTransport_Object = MibScalar
rcMicrolokTransport = _RcMicrolokTransport_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 7, 1),
    _RcMicrolokTransport_Type()
)
rcMicrolokTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMicrolokTransport.setStatus("current")


class _RcMicrolokIpPort_Type(Integer32):
    """Custom type rcMicrolokIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcMicrolokIpPort_Type.__name__ = "Integer32"
_RcMicrolokIpPort_Object = MibScalar
rcMicrolokIpPort = _RcMicrolokIpPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 7, 2),
    _RcMicrolokIpPort_Type()
)
rcMicrolokIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMicrolokIpPort.setStatus("current")
_RcMicrolokLinkStats_Type = EnabledStatus
_RcMicrolokLinkStats_Object = MibScalar
rcMicrolokLinkStats = _RcMicrolokLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 7, 3),
    _RcMicrolokLinkStats_Type()
)
rcMicrolokLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMicrolokLinkStats.setStatus("current")


class _RcMicrolokDscp_Type(Integer32):
    """Custom type rcMicrolokDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcMicrolokDscp_Type.__name__ = "Integer32"
_RcMicrolokDscp_Object = MibScalar
rcMicrolokDscp = _RcMicrolokDscp_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 7, 4),
    _RcMicrolokDscp_Type()
)
rcMicrolokDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMicrolokDscp.setStatus("current")
_RcDnp_ObjectIdentity = ObjectIdentity
rcDnp = _RcDnp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 8)
)
if mibBuilder.loadTexts:
    rcDnp.setStatus("current")
_RcDnpTransport_Type = RcTransport
_RcDnpTransport_Object = MibScalar
rcDnpTransport = _RcDnpTransport_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 8, 1),
    _RcDnpTransport_Type()
)
rcDnpTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpTransport.setStatus("current")


class _RcDnpIpPort_Type(Integer32):
    """Custom type rcDnpIpPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcDnpIpPort_Type.__name__ = "Integer32"
_RcDnpIpPort_Object = MibScalar
rcDnpIpPort = _RcDnpIpPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 8, 2),
    _RcDnpIpPort_Type()
)
rcDnpIpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpIpPort.setStatus("current")
_RcDnpLearning_Type = IpAddress
_RcDnpLearning_Object = MibScalar
rcDnpLearning = _RcDnpLearning_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 8, 3),
    _RcDnpLearning_Type()
)
rcDnpLearning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpLearning.setStatus("current")
_RcDnpAgingTimer_Type = Integer32
_RcDnpAgingTimer_Object = MibScalar
rcDnpAgingTimer = _RcDnpAgingTimer_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 8, 4),
    _RcDnpAgingTimer_Type()
)
rcDnpAgingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpAgingTimer.setStatus("current")
_RcDnpLinkStats_Type = Integer32
_RcDnpLinkStats_Object = MibScalar
rcDnpLinkStats = _RcDnpLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 8, 5),
    _RcDnpLinkStats_Type()
)
rcDnpLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpLinkStats.setStatus("current")


class _RcDnpDscp_Type(Integer32):
    """Custom type rcDnpDscp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcDnpDscp_Type.__name__ = "Integer32"
_RcDnpDscp_Object = MibScalar
rcDnpDscp = _RcDnpDscp_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 8, 6),
    _RcDnpDscp_Type()
)
rcDnpDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpDscp.setStatus("current")
_RcDnpRs_ObjectIdentity = ObjectIdentity
rcDnpRs = _RcDnpRs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9)
)
if mibBuilder.loadTexts:
    rcDnpRs.setStatus("current")
_RcDnpRsTable_Object = MibTable
rcDnpRsTable = _RcDnpRsTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9, 1)
)
if mibBuilder.loadTexts:
    rcDnpRsTable.setStatus("current")
_RcDnpRsEntry_Object = MibTableRow
rcDnpRsEntry = _RcDnpRsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9, 1, 1)
)
rcDnpRsEntry.setIndexNames(
    (0, "RUGGEDCOM-SERIAL-MIB", "rcDnpRsPort"),
)
if mibBuilder.loadTexts:
    rcDnpRsEntry.setStatus("current")


class _RcDnpRsPort_Type(Integer32):
    """Custom type rcDnpRsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcDnpRsPort_Type.__name__ = "Integer32"
_RcDnpRsPort_Object = MibTableColumn
rcDnpRsPort = _RcDnpRsPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9, 1, 1, 1),
    _RcDnpRsPort_Type()
)
rcDnpRsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcDnpRsPort.setStatus("current")
_RcDnpRsCalllDir_Type = RcCallDir
_RcDnpRsCalllDir_Object = MibTableColumn
rcDnpRsCalllDir = _RcDnpRsCalllDir_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9, 1, 1, 2),
    _RcDnpRsCalllDir_Type()
)
rcDnpRsCalllDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpRsCalllDir.setStatus("current")
_RcDnpRsTransport_Type = RcTransport
_RcDnpRsTransport_Object = MibTableColumn
rcDnpRsTransport = _RcDnpRsTransport_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9, 1, 1, 3),
    _RcDnpRsTransport_Type()
)
rcDnpRsTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpRsTransport.setStatus("current")


class _RcDnpRsMaxConns_Type(Integer32):
    """Custom type rcDnpRsMaxConns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_RcDnpRsMaxConns_Type.__name__ = "Integer32"
_RcDnpRsMaxConns_Object = MibTableColumn
rcDnpRsMaxConns = _RcDnpRsMaxConns_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9, 1, 1, 4),
    _RcDnpRsMaxConns_Type()
)
rcDnpRsMaxConns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpRsMaxConns.setStatus("current")


class _RcDnpRsLocPort_Type(Integer32):
    """Custom type rcDnpRsLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcDnpRsLocPort_Type.__name__ = "Integer32"
_RcDnpRsLocPort_Object = MibTableColumn
rcDnpRsLocPort = _RcDnpRsLocPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9, 1, 1, 5),
    _RcDnpRsLocPort_Type()
)
rcDnpRsLocPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpRsLocPort.setStatus("current")


class _RcDnpRsRemPort_Type(Integer32):
    """Custom type rcDnpRsRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcDnpRsRemPort_Type.__name__ = "Integer32"
_RcDnpRsRemPort_Object = MibTableColumn
rcDnpRsRemPort = _RcDnpRsRemPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9, 1, 1, 6),
    _RcDnpRsRemPort_Type()
)
rcDnpRsRemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpRsRemPort.setStatus("current")
_RcDnpRsIpAdd_Type = IpAddress
_RcDnpRsIpAdd_Object = MibTableColumn
rcDnpRsIpAdd = _RcDnpRsIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9, 1, 1, 7),
    _RcDnpRsIpAdd_Type()
)
rcDnpRsIpAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpRsIpAdd.setStatus("current")
_RcDnpRsLinkStats_Type = EnabledStatus
_RcDnpRsLinkStats_Object = MibTableColumn
rcDnpRsLinkStats = _RcDnpRsLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 9, 1, 1, 8),
    _RcDnpRsLinkStats_Type()
)
rcDnpRsLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcDnpRsLinkStats.setStatus("current")
_RcMirrorBits_ObjectIdentity = ObjectIdentity
rcMirrorBits = _RcMirrorBits_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 10)
)
if mibBuilder.loadTexts:
    rcMirrorBits.setStatus("current")
_RcMirrBitsTable_Object = MibTable
rcMirrBitsTable = _RcMirrBitsTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 10, 1)
)
if mibBuilder.loadTexts:
    rcMirrBitsTable.setStatus("current")
_RcMirrBitsEntry_Object = MibTableRow
rcMirrBitsEntry = _RcMirrBitsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 10, 1, 1)
)
rcMirrBitsEntry.setIndexNames(
    (0, "RUGGEDCOM-SERIAL-MIB", "rcMirrBitsPort"),
)
if mibBuilder.loadTexts:
    rcMirrBitsEntry.setStatus("current")


class _RcMirrBitsPort_Type(Integer32):
    """Custom type rcMirrBitsPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcMirrBitsPort_Type.__name__ = "Integer32"
_RcMirrBitsPort_Object = MibTableColumn
rcMirrBitsPort = _RcMirrBitsPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 10, 1, 1, 1),
    _RcMirrBitsPort_Type()
)
rcMirrBitsPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcMirrBitsPort.setStatus("current")
_RcMirrBitsTransport_Type = RcTransport
_RcMirrBitsTransport_Object = MibTableColumn
rcMirrBitsTransport = _RcMirrBitsTransport_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 10, 1, 1, 2),
    _RcMirrBitsTransport_Type()
)
rcMirrBitsTransport.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMirrBitsTransport.setStatus("current")


class _RcMirrBitsLocPort_Type(Integer32):
    """Custom type rcMirrBitsLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcMirrBitsLocPort_Type.__name__ = "Integer32"
_RcMirrBitsLocPort_Object = MibTableColumn
rcMirrBitsLocPort = _RcMirrBitsLocPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 10, 1, 1, 3),
    _RcMirrBitsLocPort_Type()
)
rcMirrBitsLocPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMirrBitsLocPort.setStatus("current")


class _RcMirrBitsRemPort_Type(Integer32):
    """Custom type rcMirrBitsRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcMirrBitsRemPort_Type.__name__ = "Integer32"
_RcMirrBitsRemPort_Object = MibTableColumn
rcMirrBitsRemPort = _RcMirrBitsRemPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 10, 1, 1, 4),
    _RcMirrBitsRemPort_Type()
)
rcMirrBitsRemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMirrBitsRemPort.setStatus("current")
_RcMirrBitsIpAdd_Type = IpAddress
_RcMirrBitsIpAdd_Object = MibTableColumn
rcMirrBitsIpAdd = _RcMirrBitsIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 10, 1, 1, 5),
    _RcMirrBitsIpAdd_Type()
)
rcMirrBitsIpAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMirrBitsIpAdd.setStatus("current")
_RcMirrBitsLinkStats_Type = EnabledStatus
_RcMirrBitsLinkStats_Object = MibTableColumn
rcMirrBitsLinkStats = _RcMirrBitsLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 10, 1, 1, 6),
    _RcMirrBitsLinkStats_Type()
)
rcMirrBitsLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcMirrBitsLinkStats.setStatus("current")
_RcTelnetComport_ObjectIdentity = ObjectIdentity
rcTelnetComport = _RcTelnetComport_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11)
)
if mibBuilder.loadTexts:
    rcTelnetComport.setStatus("current")
_RcTelnetComportTable_Object = MibTable
rcTelnetComportTable = _RcTelnetComportTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1)
)
if mibBuilder.loadTexts:
    rcTelnetComportTable.setStatus("current")
_RcTelnetComportEntry_Object = MibTableRow
rcTelnetComportEntry = _RcTelnetComportEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1)
)
rcTelnetComportEntry.setIndexNames(
    (0, "RUGGEDCOM-SERIAL-MIB", "rcTelnetComportPort"),
)
if mibBuilder.loadTexts:
    rcTelnetComportEntry.setStatus("current")


class _RcTelnetComportPort_Type(Integer32):
    """Custom type rcTelnetComportPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_RcTelnetComportPort_Type.__name__ = "Integer32"
_RcTelnetComportPort_Object = MibTableColumn
rcTelnetComportPort = _RcTelnetComportPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1, 1),
    _RcTelnetComportPort_Type()
)
rcTelnetComportPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcTelnetComportPort.setStatus("current")


class _RcTelnetComportPackChar_Type(Integer32):
    """Custom type rcTelnetComportPackChar based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RcTelnetComportPackChar_Type.__name__ = "Integer32"
_RcTelnetComportPackChar_Object = MibTableColumn
rcTelnetComportPackChar = _RcTelnetComportPackChar_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1, 2),
    _RcTelnetComportPackChar_Type()
)
rcTelnetComportPackChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetComportPackChar.setStatus("current")


class _RcTelnetComportPackTimer_Type(Integer32):
    """Custom type rcTelnetComportPackTimer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 1000),
    )


_RcTelnetComportPackTimer_Type.__name__ = "Integer32"
_RcTelnetComportPackTimer_Object = MibTableColumn
rcTelnetComportPackTimer = _RcTelnetComportPackTimer_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1, 3),
    _RcTelnetComportPackTimer_Type()
)
rcTelnetComportPackTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetComportPackTimer.setStatus("current")
if mibBuilder.loadTexts:
    rcTelnetComportPackTimer.setUnits("milliseconds")


class _RcTelnetComportPackSize_Type(Integer32):
    """Custom type rcTelnetComportPackSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 1400),
    )


_RcTelnetComportPackSize_Type.__name__ = "Integer32"
_RcTelnetComportPackSize_Object = MibTableColumn
rcTelnetComportPackSize = _RcTelnetComportPackSize_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1, 4),
    _RcTelnetComportPackSize_Type()
)
rcTelnetComportPackSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetComportPackSize.setStatus("current")
if mibBuilder.loadTexts:
    rcTelnetComportPackSize.setUnits("bytes")
_RcTelnetComportFlowControl_Type = RcFlowControl
_RcTelnetComportFlowControl_Object = MibTableColumn
rcTelnetComportFlowControl = _RcTelnetComportFlowControl_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1, 5),
    _RcTelnetComportFlowControl_Type()
)
rcTelnetComportFlowControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetComportFlowControl.setStatus("current")
_RcTelnetComportCallDir_Type = RcCallDir
_RcTelnetComportCallDir_Object = MibTableColumn
rcTelnetComportCallDir = _RcTelnetComportCallDir_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1, 6),
    _RcTelnetComportCallDir_Type()
)
rcTelnetComportCallDir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetComportCallDir.setStatus("current")


class _RcTelnetComportLocPort_Type(Integer32):
    """Custom type rcTelnetComportLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcTelnetComportLocPort_Type.__name__ = "Integer32"
_RcTelnetComportLocPort_Object = MibTableColumn
rcTelnetComportLocPort = _RcTelnetComportLocPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1, 7),
    _RcTelnetComportLocPort_Type()
)
rcTelnetComportLocPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetComportLocPort.setStatus("current")


class _RcTelnetComportRemPort_Type(Integer32):
    """Custom type rcTelnetComportRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcTelnetComportRemPort_Type.__name__ = "Integer32"
_RcTelnetComportRemPort_Object = MibTableColumn
rcTelnetComportRemPort = _RcTelnetComportRemPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1, 8),
    _RcTelnetComportRemPort_Type()
)
rcTelnetComportRemPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetComportRemPort.setStatus("current")
_RcTelnetComportIpAdd_Type = IpAddress
_RcTelnetComportIpAdd_Object = MibTableColumn
rcTelnetComportIpAdd = _RcTelnetComportIpAdd_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1, 9),
    _RcTelnetComportIpAdd_Type()
)
rcTelnetComportIpAdd.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetComportIpAdd.setStatus("current")
_RcTelnetComportLinkStats_Type = EnabledStatus
_RcTelnetComportLinkStats_Object = MibTableColumn
rcTelnetComportLinkStats = _RcTelnetComportLinkStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 11, 1, 1, 10),
    _RcTelnetComportLinkStats_Type()
)
rcTelnetComportLinkStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcTelnetComportLinkStats.setStatus("current")
_RcConnStats_ObjectIdentity = ObjectIdentity
rcConnStats = _RcConnStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 15)
)
if mibBuilder.loadTexts:
    rcConnStats.setStatus("current")
_RcConnStatsTable_Object = MibTable
rcConnStatsTable = _RcConnStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 15, 1)
)
if mibBuilder.loadTexts:
    rcConnStatsTable.setStatus("current")
_RcConnStatsEntry_Object = MibTableRow
rcConnStatsEntry = _RcConnStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 15, 1, 1)
)
rcConnStatsEntry.setIndexNames(
    (0, "RUGGEDCOM-SERIAL-MIB", "rcConnStatsRemIp"),
    (0, "RUGGEDCOM-SERIAL-MIB", "rcConnStatsRemPort"),
    (0, "RUGGEDCOM-SERIAL-MIB", "rcConnStatsLocPort"),
)
if mibBuilder.loadTexts:
    rcConnStatsEntry.setStatus("current")
_RcConnStatsRemIp_Type = IpAddress
_RcConnStatsRemIp_Object = MibTableColumn
rcConnStatsRemIp = _RcConnStatsRemIp_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 15, 1, 1, 1),
    _RcConnStatsRemIp_Type()
)
rcConnStatsRemIp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcConnStatsRemIp.setStatus("current")


class _RcConnStatsRemPort_Type(Integer32):
    """Custom type rcConnStatsRemPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcConnStatsRemPort_Type.__name__ = "Integer32"
_RcConnStatsRemPort_Object = MibTableColumn
rcConnStatsRemPort = _RcConnStatsRemPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 15, 1, 1, 2),
    _RcConnStatsRemPort_Type()
)
rcConnStatsRemPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcConnStatsRemPort.setStatus("current")


class _RcConnStatsLocPort_Type(Integer32):
    """Custom type rcConnStatsLocPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1024, 65535),
    )


_RcConnStatsLocPort_Type.__name__ = "Integer32"
_RcConnStatsLocPort_Object = MibTableColumn
rcConnStatsLocPort = _RcConnStatsLocPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 15, 1, 1, 3),
    _RcConnStatsLocPort_Type()
)
rcConnStatsLocPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcConnStatsLocPort.setStatus("current")
_RcConnStatsRxPkts_Type = Integer32
_RcConnStatsRxPkts_Object = MibTableColumn
rcConnStatsRxPkts = _RcConnStatsRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 15, 1, 1, 4),
    _RcConnStatsRxPkts_Type()
)
rcConnStatsRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcConnStatsRxPkts.setStatus("current")
_RcConnStatsTxPkts_Type = Integer32
_RcConnStatsTxPkts_Object = MibTableColumn
rcConnStatsTxPkts = _RcConnStatsTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 15, 1, 1, 5),
    _RcConnStatsTxPkts_Type()
)
rcConnStatsTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcConnStatsTxPkts.setStatus("current")
_RcSerDeviceCmnd_ObjectIdentity = ObjectIdentity
rcSerDeviceCmnd = _RcSerDeviceCmnd_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 16)
)
if mibBuilder.loadTexts:
    rcSerDeviceCmnd.setStatus("current")
_RcSerDeviceCmndResetPort_Type = PortList
_RcSerDeviceCmndResetPort_Object = MibScalar
rcSerDeviceCmndResetPort = _RcSerDeviceCmndResetPort_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 16, 1),
    _RcSerDeviceCmndResetPort_Type()
)
rcSerDeviceCmndResetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSerDeviceCmndResetPort.setStatus("current")
_RcSerDeviceCmndClearStats_Type = PortList
_RcSerDeviceCmndClearStats_Object = MibScalar
rcSerDeviceCmndClearStats = _RcSerDeviceCmndClearStats_Object(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 16, 2),
    _RcSerDeviceCmndClearStats_Type()
)
rcSerDeviceCmndClearStats.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcSerDeviceCmndClearStats.setStatus("current")
_RcSerialConformance_ObjectIdentity = ObjectIdentity
rcSerialConformance = _RcSerialConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18)
)
_RcSerialGroups_ObjectIdentity = ObjectIdentity
rcSerialGroups = _RcSerialGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2)
)

# Managed Objects groups

rcSerialPortParamsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 1)
)
rcSerialPortParamsGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcSerialPortIfIndex"),
        ("RUGGEDCOM-SERIAL-MIB", "rcSerialProtocol"),
        ("RUGGEDCOM-SERIAL-MIB", "rcSerialPortType"),
        ("RUGGEDCOM-SERIAL-MIB", "rcSerialForceHD"),
        ("RUGGEDCOM-SERIAL-MIB", "rcSerialTurnAround"),
        ("RUGGEDCOM-SERIAL-MIB", "rcSerialPostTxDelay"),
        ("RUGGEDCOM-SERIAL-MIB", "rcSerialHoldTime"),
        ("RUGGEDCOM-SERIAL-MIB", "rcSerialDscp"),
        ("RUGGEDCOM-SERIAL-MIB", "rcSerialRxtoTxDelay"))
)
if mibBuilder.loadTexts:
    rcSerialPortParamsGroup.setStatus("current")

rcSerialMbServerGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 2)
)
rcSerialMbServerGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcMbServerRespTimer"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMbServerAuxTcpPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMbServerSendExcep"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMbServerLinkStats"))
)
if mibBuilder.loadTexts:
    rcSerialMbServerGroup.setStatus("current")

rcSerialMbClientGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 3)
)
rcSerialMbClientGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcMbClientIPPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMbClientFwdExcp"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMbClientLinkStats"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMbClientDscp"))
)
if mibBuilder.loadTexts:
    rcSerialMbClientGroup.setStatus("current")

rcSerialRawSocketGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 4)
)
rcSerialRawSocketGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcRawSockPackChar"),
        ("RUGGEDCOM-SERIAL-MIB", "rcRawSockPackTimer"),
        ("RUGGEDCOM-SERIAL-MIB", "rcRawSockPackSize"),
        ("RUGGEDCOM-SERIAL-MIB", "rcRawSockFlowControl"),
        ("RUGGEDCOM-SERIAL-MIB", "rcRawSockTransport"),
        ("RUGGEDCOM-SERIAL-MIB", "rcRawSockCallDir"),
        ("RUGGEDCOM-SERIAL-MIB", "rcRawSockMaxConn"),
        ("RUGGEDCOM-SERIAL-MIB", "rcRawSockLocPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcRawSockRemPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcRawSockIpAdd"),
        ("RUGGEDCOM-SERIAL-MIB", "rcRawSockLinkStats"))
)
if mibBuilder.loadTexts:
    rcSerialRawSocketGroup.setStatus("current")

rcSerialPreEmpRawSockGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 5)
)
rcSerialPreEmpRawSockGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSPackChar"),
        ("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSPackTimer"),
        ("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSPackSize"),
        ("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSFlowControl"),
        ("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSLocPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSRemPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSIpAdd"),
        ("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSLinkStats"),
        ("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSDynPackChar"),
        ("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSDynPackTimer"),
        ("RUGGEDCOM-SERIAL-MIB", "rcPreemptRSDynTimeout"))
)
if mibBuilder.loadTexts:
    rcSerialPreEmpRawSockGroup.setStatus("current")

rcSerialTinAndWinGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 6)
)
rcSerialTinAndWinGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinTinMode"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinTinTrans"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinWinTrans"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinTinIpPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinWinIpPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinMsgAgingTime"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinAddrAgingTime"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinBroadCastAddr"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinUniAddr"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinLinkStats"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinWinDscp"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTinAndWinTinDscp"))
)
if mibBuilder.loadTexts:
    rcSerialTinAndWinGroup.setStatus("current")

rcSerialMicrolokGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 7)
)
rcSerialMicrolokGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcMicrolokTransport"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMicrolokIpPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMicrolokLinkStats"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMicrolokDscp"))
)
if mibBuilder.loadTexts:
    rcSerialMicrolokGroup.setStatus("current")

rcSerialDnpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 8)
)
rcSerialDnpGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcDnpTransport"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpIpPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpLearning"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpAgingTimer"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpLinkStats"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpDscp"))
)
if mibBuilder.loadTexts:
    rcSerialDnpGroup.setStatus("current")

rcSerialDnpRsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 9)
)
rcSerialDnpRsGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcDnpRsCalllDir"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpRsTransport"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpRsMaxConns"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpRsLocPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpRsRemPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpRsIpAdd"),
        ("RUGGEDCOM-SERIAL-MIB", "rcDnpRsLinkStats"))
)
if mibBuilder.loadTexts:
    rcSerialDnpRsGroup.setStatus("current")

rcSerialMirrBitsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 10)
)
rcSerialMirrBitsGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcMirrBitsTransport"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMirrBitsLocPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMirrBitsRemPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMirrBitsIpAdd"),
        ("RUGGEDCOM-SERIAL-MIB", "rcMirrBitsLinkStats"))
)
if mibBuilder.loadTexts:
    rcSerialMirrBitsGroup.setStatus("current")

rcSerialTelnetComportGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 11)
)
rcSerialTelnetComportGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcTelnetComportPackChar"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTelnetComportPackTimer"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTelnetComportPackSize"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTelnetComportFlowControl"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTelnetComportCallDir"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTelnetComportLocPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTelnetComportRemPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTelnetComportIpAdd"),
        ("RUGGEDCOM-SERIAL-MIB", "rcTelnetComportLinkStats"))
)
if mibBuilder.loadTexts:
    rcSerialTelnetComportGroup.setStatus("current")

rcSerialConnStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 15)
)
rcSerialConnStatsGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcConnStatsRxPkts"),
        ("RUGGEDCOM-SERIAL-MIB", "rcConnStatsTxPkts"))
)
if mibBuilder.loadTexts:
    rcSerialConnStatsGroup.setStatus("current")

rcSerialCommandsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 15004, 4, 6, 18, 2, 16)
)
rcSerialCommandsGroup.setObjects(
      *(("RUGGEDCOM-SERIAL-MIB", "rcSerDeviceCmndResetPort"),
        ("RUGGEDCOM-SERIAL-MIB", "rcSerDeviceCmndClearStats"))
)
if mibBuilder.loadTexts:
    rcSerialCommandsGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RUGGEDCOM-SERIAL-MIB",
    **{"EnabledStatus": EnabledStatus,
       "RcFlowControl": RcFlowControl,
       "RcSerProtocol": RcSerProtocol,
       "RcTransport": RcTransport,
       "RcCallDir": RcCallDir,
       "RcSerPortType": RcSerPortType,
       "rcSerial": rcSerial,
       "rcSerialPortParams": rcSerialPortParams,
       "rcSerialPortTable": rcSerialPortTable,
       "rcSerialPortEntry": rcSerialPortEntry,
       "rcSerialPortNumber": rcSerialPortNumber,
       "rcSerialPortIfIndex": rcSerialPortIfIndex,
       "rcSerialProtocol": rcSerialProtocol,
       "rcSerialPortType": rcSerialPortType,
       "rcSerialForceHD": rcSerialForceHD,
       "rcSerialTurnAround": rcSerialTurnAround,
       "rcSerialPostTxDelay": rcSerialPostTxDelay,
       "rcSerialHoldTime": rcSerialHoldTime,
       "rcSerialDscp": rcSerialDscp,
       "rcSerialRxtoTxDelay": rcSerialRxtoTxDelay,
       "rcMbServer": rcMbServer,
       "rcMbServerTable": rcMbServerTable,
       "rcMbServerEntry": rcMbServerEntry,
       "rcMbServerPort": rcMbServerPort,
       "rcMbServerRespTimer": rcMbServerRespTimer,
       "rcMbServerAuxTcpPort": rcMbServerAuxTcpPort,
       "rcMbServerSendExcep": rcMbServerSendExcep,
       "rcMbServerLinkStats": rcMbServerLinkStats,
       "rcMbClient": rcMbClient,
       "rcMbClientIPPort": rcMbClientIPPort,
       "rcMbClientFwdExcp": rcMbClientFwdExcp,
       "rcMbClientLinkStats": rcMbClientLinkStats,
       "rcMbClientDscp": rcMbClientDscp,
       "rcRawSock": rcRawSock,
       "rcRawSockTable": rcRawSockTable,
       "rcRawSockEntry": rcRawSockEntry,
       "rcRawSockPort": rcRawSockPort,
       "rcRawSockPackChar": rcRawSockPackChar,
       "rcRawSockPackTimer": rcRawSockPackTimer,
       "rcRawSockPackSize": rcRawSockPackSize,
       "rcRawSockFlowControl": rcRawSockFlowControl,
       "rcRawSockTransport": rcRawSockTransport,
       "rcRawSockCallDir": rcRawSockCallDir,
       "rcRawSockMaxConn": rcRawSockMaxConn,
       "rcRawSockLocPort": rcRawSockLocPort,
       "rcRawSockRemPort": rcRawSockRemPort,
       "rcRawSockIpAdd": rcRawSockIpAdd,
       "rcRawSockLinkStats": rcRawSockLinkStats,
       "rcPreemptRS": rcPreemptRS,
       "rcPreemptRSTable": rcPreemptRSTable,
       "rcPreemptRSEntry": rcPreemptRSEntry,
       "rcPreemptRSPort": rcPreemptRSPort,
       "rcPreemptRSPackChar": rcPreemptRSPackChar,
       "rcPreemptRSPackTimer": rcPreemptRSPackTimer,
       "rcPreemptRSPackSize": rcPreemptRSPackSize,
       "rcPreemptRSFlowControl": rcPreemptRSFlowControl,
       "rcPreemptRSLocPort": rcPreemptRSLocPort,
       "rcPreemptRSRemPort": rcPreemptRSRemPort,
       "rcPreemptRSIpAdd": rcPreemptRSIpAdd,
       "rcPreemptRSLinkStats": rcPreemptRSLinkStats,
       "rcPreemptRSDynPackChar": rcPreemptRSDynPackChar,
       "rcPreemptRSDynPackTimer": rcPreemptRSDynPackTimer,
       "rcPreemptRSDynTimeout": rcPreemptRSDynTimeout,
       "rcTinAndWin": rcTinAndWin,
       "rcTinAndWinTinMode": rcTinAndWinTinMode,
       "rcTinAndWinTinTrans": rcTinAndWinTinTrans,
       "rcTinAndWinWinTrans": rcTinAndWinWinTrans,
       "rcTinAndWinTinIpPort": rcTinAndWinTinIpPort,
       "rcTinAndWinWinIpPort": rcTinAndWinWinIpPort,
       "rcTinAndWinMsgAgingTime": rcTinAndWinMsgAgingTime,
       "rcTinAndWinAddrAgingTime": rcTinAndWinAddrAgingTime,
       "rcTinAndWinBroadCastAddr": rcTinAndWinBroadCastAddr,
       "rcTinAndWinUniAddr": rcTinAndWinUniAddr,
       "rcTinAndWinLinkStats": rcTinAndWinLinkStats,
       "rcTinAndWinWinDscp": rcTinAndWinWinDscp,
       "rcTinAndWinTinDscp": rcTinAndWinTinDscp,
       "rcMicrolok": rcMicrolok,
       "rcMicrolokTransport": rcMicrolokTransport,
       "rcMicrolokIpPort": rcMicrolokIpPort,
       "rcMicrolokLinkStats": rcMicrolokLinkStats,
       "rcMicrolokDscp": rcMicrolokDscp,
       "rcDnp": rcDnp,
       "rcDnpTransport": rcDnpTransport,
       "rcDnpIpPort": rcDnpIpPort,
       "rcDnpLearning": rcDnpLearning,
       "rcDnpAgingTimer": rcDnpAgingTimer,
       "rcDnpLinkStats": rcDnpLinkStats,
       "rcDnpDscp": rcDnpDscp,
       "rcDnpRs": rcDnpRs,
       "rcDnpRsTable": rcDnpRsTable,
       "rcDnpRsEntry": rcDnpRsEntry,
       "rcDnpRsPort": rcDnpRsPort,
       "rcDnpRsCalllDir": rcDnpRsCalllDir,
       "rcDnpRsTransport": rcDnpRsTransport,
       "rcDnpRsMaxConns": rcDnpRsMaxConns,
       "rcDnpRsLocPort": rcDnpRsLocPort,
       "rcDnpRsRemPort": rcDnpRsRemPort,
       "rcDnpRsIpAdd": rcDnpRsIpAdd,
       "rcDnpRsLinkStats": rcDnpRsLinkStats,
       "rcMirrorBits": rcMirrorBits,
       "rcMirrBitsTable": rcMirrBitsTable,
       "rcMirrBitsEntry": rcMirrBitsEntry,
       "rcMirrBitsPort": rcMirrBitsPort,
       "rcMirrBitsTransport": rcMirrBitsTransport,
       "rcMirrBitsLocPort": rcMirrBitsLocPort,
       "rcMirrBitsRemPort": rcMirrBitsRemPort,
       "rcMirrBitsIpAdd": rcMirrBitsIpAdd,
       "rcMirrBitsLinkStats": rcMirrBitsLinkStats,
       "rcTelnetComport": rcTelnetComport,
       "rcTelnetComportTable": rcTelnetComportTable,
       "rcTelnetComportEntry": rcTelnetComportEntry,
       "rcTelnetComportPort": rcTelnetComportPort,
       "rcTelnetComportPackChar": rcTelnetComportPackChar,
       "rcTelnetComportPackTimer": rcTelnetComportPackTimer,
       "rcTelnetComportPackSize": rcTelnetComportPackSize,
       "rcTelnetComportFlowControl": rcTelnetComportFlowControl,
       "rcTelnetComportCallDir": rcTelnetComportCallDir,
       "rcTelnetComportLocPort": rcTelnetComportLocPort,
       "rcTelnetComportRemPort": rcTelnetComportRemPort,
       "rcTelnetComportIpAdd": rcTelnetComportIpAdd,
       "rcTelnetComportLinkStats": rcTelnetComportLinkStats,
       "rcConnStats": rcConnStats,
       "rcConnStatsTable": rcConnStatsTable,
       "rcConnStatsEntry": rcConnStatsEntry,
       "rcConnStatsRemIp": rcConnStatsRemIp,
       "rcConnStatsRemPort": rcConnStatsRemPort,
       "rcConnStatsLocPort": rcConnStatsLocPort,
       "rcConnStatsRxPkts": rcConnStatsRxPkts,
       "rcConnStatsTxPkts": rcConnStatsTxPkts,
       "rcSerDeviceCmnd": rcSerDeviceCmnd,
       "rcSerDeviceCmndResetPort": rcSerDeviceCmndResetPort,
       "rcSerDeviceCmndClearStats": rcSerDeviceCmndClearStats,
       "rcSerialConformance": rcSerialConformance,
       "rcSerialGroups": rcSerialGroups,
       "rcSerialPortParamsGroup": rcSerialPortParamsGroup,
       "rcSerialMbServerGroup": rcSerialMbServerGroup,
       "rcSerialMbClientGroup": rcSerialMbClientGroup,
       "rcSerialRawSocketGroup": rcSerialRawSocketGroup,
       "rcSerialPreEmpRawSockGroup": rcSerialPreEmpRawSockGroup,
       "rcSerialTinAndWinGroup": rcSerialTinAndWinGroup,
       "rcSerialMicrolokGroup": rcSerialMicrolokGroup,
       "rcSerialDnpGroup": rcSerialDnpGroup,
       "rcSerialDnpRsGroup": rcSerialDnpRsGroup,
       "rcSerialMirrBitsGroup": rcSerialMirrBitsGroup,
       "rcSerialTelnetComportGroup": rcSerialTelnetComportGroup,
       "rcSerialConnStatsGroup": rcSerialConnStatsGroup,
       "rcSerialCommandsGroup": rcSerialCommandsGroup}
)
