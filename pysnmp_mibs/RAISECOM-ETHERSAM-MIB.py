# SNMP MIB module (RAISECOM-ETHERSAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-ETHERSAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:35:38 2025
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

(iscomSwitch,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "iscomSwitch")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

rcEtherSam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74)
)
if mibBuilder.loadTexts:
    rcEtherSam.setRevisions(
        ("2012-09-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_RcEtherSamGlobalGroup_ObjectIdentity = ObjectIdentity
rcEtherSamGlobalGroup = _RcEtherSamGlobalGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 1)
)
_RcEtherSamServiceList_Type = Integer32
_RcEtherSamServiceList_Object = MibScalar
rcEtherSamServiceList = _RcEtherSamServiceList_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 1, 1),
    _RcEtherSamServiceList_Type()
)
rcEtherSamServiceList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceList.setStatus("current")


class _RcEtherSamServiceTestType_Type(Integer32):
    """Custom type rcEtherSamServiceTestType based on Integer32"""
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
        *(("configuration", 1),
          ("performance", 2),
          ("both", 3),
          ("rfc2544", 4),
          ("performance-inservice", 5))
    )


_RcEtherSamServiceTestType_Type.__name__ = "Integer32"
_RcEtherSamServiceTestType_Object = MibScalar
rcEtherSamServiceTestType = _RcEtherSamServiceTestType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 1, 2),
    _RcEtherSamServiceTestType_Type()
)
rcEtherSamServiceTestType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceTestType.setStatus("current")


class _RcEtherSamServiceTestOperate_Type(Integer32):
    """Custom type rcEtherSamServiceTestOperate based on Integer32"""
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
        *(("start", 1),
          ("stop", 2),
          ("testing", 3),
          ("idle", 4))
    )


_RcEtherSamServiceTestOperate_Type.__name__ = "Integer32"
_RcEtherSamServiceTestOperate_Object = MibScalar
rcEtherSamServiceTestOperate = _RcEtherSamServiceTestOperate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 1, 3),
    _RcEtherSamServiceTestOperate_Type()
)
rcEtherSamServiceTestOperate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceTestOperate.setStatus("current")


class _RcEtherSamPerformanceDuration_Type(Integer32):
    """Custom type rcEtherSamPerformanceDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(5, 1440),
    )


_RcEtherSamPerformanceDuration_Type.__name__ = "Integer32"
_RcEtherSamPerformanceDuration_Object = MibScalar
rcEtherSamPerformanceDuration = _RcEtherSamPerformanceDuration_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 1, 4),
    _RcEtherSamPerformanceDuration_Type()
)
rcEtherSamPerformanceDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceDuration.setStatus("current")


class _RcEtherSamTestElapsedTime_Type(Integer32):
    """Custom type rcEtherSamTestElapsedTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 172800),
    )


_RcEtherSamTestElapsedTime_Type.__name__ = "Integer32"
_RcEtherSamTestElapsedTime_Object = MibScalar
rcEtherSamTestElapsedTime = _RcEtherSamTestElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 1, 5),
    _RcEtherSamTestElapsedTime_Type()
)
rcEtherSamTestElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamTestElapsedTime.setStatus("current")


class _RcEtherSamServiceTestResult_Type(Integer32):
    """Custom type rcEtherSamServiceTestResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_RcEtherSamServiceTestResult_Type.__name__ = "Integer32"
_RcEtherSamServiceTestResult_Object = MibScalar
rcEtherSamServiceTestResult = _RcEtherSamServiceTestResult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 1, 6),
    _RcEtherSamServiceTestResult_Type()
)
rcEtherSamServiceTestResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamServiceTestResult.setStatus("current")
_RcEtherSamTestGroup_ObjectIdentity = ObjectIdentity
rcEtherSamTestGroup = _RcEtherSamTestGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2)
)
_RcEtherSamFlowTable_Object = MibTable
rcEtherSamFlowTable = _RcEtherSamFlowTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1)
)
if mibBuilder.loadTexts:
    rcEtherSamFlowTable.setStatus("current")
_RcEtherSamFlowEntry_Object = MibTableRow
rcEtherSamFlowEntry = _RcEtherSamFlowEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1)
)
rcEtherSamFlowEntry.setIndexNames(
    (0, "RAISECOM-ETHERSAM-MIB", "rcEtherSamFlowIndex"),
)
if mibBuilder.loadTexts:
    rcEtherSamFlowEntry.setStatus("current")


class _RcEtherSamFlowIndex_Type(Integer32):
    """Custom type rcEtherSamFlowIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RcEtherSamFlowIndex_Type.__name__ = "Integer32"
_RcEtherSamFlowIndex_Object = MibTableColumn
rcEtherSamFlowIndex = _RcEtherSamFlowIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 1),
    _RcEtherSamFlowIndex_Type()
)
rcEtherSamFlowIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcEtherSamFlowIndex.setStatus("current")


class _RcEtherSamFlowFrameType_Type(Integer32):
    """Custom type rcEtherSamFlowFrameType based on Integer32"""
    defaultValue = 2

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
              9)
        )
    )
    namedValues = NamedValues(
        *(("loopback", 1),
          ("ethernet", 2),
          ("ip", 3),
          ("tcp", 4),
          ("udp", 5),
          ("video", 6),
          ("voice-G711", 7),
          ("voice-G7231", 8),
          ("voice-G729", 9))
    )


_RcEtherSamFlowFrameType_Type.__name__ = "Integer32"
_RcEtherSamFlowFrameType_Object = MibTableColumn
rcEtherSamFlowFrameType = _RcEtherSamFlowFrameType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 2),
    _RcEtherSamFlowFrameType_Type()
)
rcEtherSamFlowFrameType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrameType.setStatus("current")


class _RcEtherSamFlowFrameEtherType_Type(Integer32):
    """Custom type rcEtherSamFlowFrameEtherType based on Integer32"""
    defaultValue = 2208


_RcEtherSamFlowFrameEtherType_Type.__name__ = "Integer32"
_RcEtherSamFlowFrameEtherType_Object = MibTableColumn
rcEtherSamFlowFrameEtherType = _RcEtherSamFlowFrameEtherType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 3),
    _RcEtherSamFlowFrameEtherType_Type()
)
rcEtherSamFlowFrameEtherType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrameEtherType.setStatus("current")


class _RcEtherSamFlowFrameLengthType_Type(Integer32):
    """Custom type rcEtherSamFlowFrameLengthType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("single", 1),
          ("mix", 2))
    )


_RcEtherSamFlowFrameLengthType_Type.__name__ = "Integer32"
_RcEtherSamFlowFrameLengthType_Object = MibTableColumn
rcEtherSamFlowFrameLengthType = _RcEtherSamFlowFrameLengthType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 4),
    _RcEtherSamFlowFrameLengthType_Type()
)
rcEtherSamFlowFrameLengthType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrameLengthType.setStatus("current")


class _RcEtherSamFlowFrameSize_Type(Integer32):
    """Custom type rcEtherSamFlowFrameSize based on Integer32"""
    defaultValue = 512

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 12288),
    )


_RcEtherSamFlowFrameSize_Type.__name__ = "Integer32"
_RcEtherSamFlowFrameSize_Object = MibTableColumn
rcEtherSamFlowFrameSize = _RcEtherSamFlowFrameSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 5),
    _RcEtherSamFlowFrameSize_Type()
)
rcEtherSamFlowFrameSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrameSize.setStatus("current")


class _RcEtherSamFlowFrameCvlan_Type(Integer32):
    """Custom type rcEtherSamFlowFrameCvlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RcEtherSamFlowFrameCvlan_Type.__name__ = "Integer32"
_RcEtherSamFlowFrameCvlan_Object = MibTableColumn
rcEtherSamFlowFrameCvlan = _RcEtherSamFlowFrameCvlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 6),
    _RcEtherSamFlowFrameCvlan_Type()
)
rcEtherSamFlowFrameCvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrameCvlan.setStatus("current")


class _RcEtherSamFlowFrameCos_Type(Integer32):
    """Custom type rcEtherSamFlowFrameCos based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcEtherSamFlowFrameCos_Type.__name__ = "Integer32"
_RcEtherSamFlowFrameCos_Object = MibTableColumn
rcEtherSamFlowFrameCos = _RcEtherSamFlowFrameCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 7),
    _RcEtherSamFlowFrameCos_Type()
)
rcEtherSamFlowFrameCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrameCos.setStatus("current")
_RcEtherSamFlowRowStatus_Type = RowStatus
_RcEtherSamFlowRowStatus_Object = MibTableColumn
rcEtherSamFlowRowStatus = _RcEtherSamFlowRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 8),
    _RcEtherSamFlowRowStatus_Type()
)
rcEtherSamFlowRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowRowStatus.setStatus("current")


class _RcEtherSamFlowDescription_Type(OctetString):
    """Custom type rcEtherSamFlowDescription based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcEtherSamFlowDescription_Type.__name__ = "OctetString"
_RcEtherSamFlowDescription_Object = MibTableColumn
rcEtherSamFlowDescription = _RcEtherSamFlowDescription_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 9),
    _RcEtherSamFlowDescription_Type()
)
rcEtherSamFlowDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowDescription.setStatus("current")
_RcEtherSamFlowDestAddr_Type = IpAddress
_RcEtherSamFlowDestAddr_Object = MibTableColumn
rcEtherSamFlowDestAddr = _RcEtherSamFlowDestAddr_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 10),
    _RcEtherSamFlowDestAddr_Type()
)
rcEtherSamFlowDestAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowDestAddr.setStatus("current")


class _RcEtherSamFlowDscp_Type(Integer32):
    """Custom type rcEtherSamFlowDscp based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_RcEtherSamFlowDscp_Type.__name__ = "Integer32"
_RcEtherSamFlowDscp_Object = MibTableColumn
rcEtherSamFlowDscp = _RcEtherSamFlowDscp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 11),
    _RcEtherSamFlowDscp_Type()
)
rcEtherSamFlowDscp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowDscp.setStatus("current")


class _RcEtherSamFlowDatePattern_Type(Integer32):
    """Custom type rcEtherSamFlowDatePattern based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("null", 1),
          ("Crc32", 2))
    )


_RcEtherSamFlowDatePattern_Type.__name__ = "Integer32"
_RcEtherSamFlowDatePattern_Object = MibTableColumn
rcEtherSamFlowDatePattern = _RcEtherSamFlowDatePattern_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 12),
    _RcEtherSamFlowDatePattern_Type()
)
rcEtherSamFlowDatePattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowDatePattern.setStatus("current")


class _RcEtherSamFlowSourcePort_Type(Integer32):
    """Custom type rcEtherSamFlowSourcePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcEtherSamFlowSourcePort_Type.__name__ = "Integer32"
_RcEtherSamFlowSourcePort_Object = MibTableColumn
rcEtherSamFlowSourcePort = _RcEtherSamFlowSourcePort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 13),
    _RcEtherSamFlowSourcePort_Type()
)
rcEtherSamFlowSourcePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowSourcePort.setStatus("current")


class _RcEtherSamFlowDestPort_Type(Integer32):
    """Custom type rcEtherSamFlowDestPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RcEtherSamFlowDestPort_Type.__name__ = "Integer32"
_RcEtherSamFlowDestPort_Object = MibTableColumn
rcEtherSamFlowDestPort = _RcEtherSamFlowDestPort_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 14),
    _RcEtherSamFlowDestPort_Type()
)
rcEtherSamFlowDestPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowDestPort.setStatus("current")
_RcEtherSamFlowNextHopMac_Type = MacAddress
_RcEtherSamFlowNextHopMac_Object = MibTableColumn
rcEtherSamFlowNextHopMac = _RcEtherSamFlowNextHopMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 1, 1, 15),
    _RcEtherSamFlowNextHopMac_Type()
)
rcEtherSamFlowNextHopMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowNextHopMac.setStatus("current")
_RcEtherSamServiceTable_Object = MibTable
rcEtherSamServiceTable = _RcEtherSamServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2)
)
if mibBuilder.loadTexts:
    rcEtherSamServiceTable.setStatus("current")
_RcEtherSamServiceEntry_Object = MibTableRow
rcEtherSamServiceEntry = _RcEtherSamServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1)
)
rcEtherSamServiceEntry.setIndexNames(
    (0, "RAISECOM-ETHERSAM-MIB", "rcEtherSamServiceIndex"),
)
if mibBuilder.loadTexts:
    rcEtherSamServiceEntry.setStatus("current")


class _RcEtherSamServiceIndex_Type(Integer32):
    """Custom type rcEtherSamServiceIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 128),
    )


_RcEtherSamServiceIndex_Type.__name__ = "Integer32"
_RcEtherSamServiceIndex_Object = MibTableColumn
rcEtherSamServiceIndex = _RcEtherSamServiceIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 1),
    _RcEtherSamServiceIndex_Type()
)
rcEtherSamServiceIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcEtherSamServiceIndex.setStatus("current")


class _RcEtherSamServiceName_Type(OctetString):
    """Custom type rcEtherSamServiceName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_RcEtherSamServiceName_Type.__name__ = "OctetString"
_RcEtherSamServiceName_Object = MibTableColumn
rcEtherSamServiceName = _RcEtherSamServiceName_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 2),
    _RcEtherSamServiceName_Type()
)
rcEtherSamServiceName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceName.setStatus("current")


class _RcEtherSamServiceProfileNum_Type(Integer32):
    """Custom type rcEtherSamServiceProfileNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_RcEtherSamServiceProfileNum_Type.__name__ = "Integer32"
_RcEtherSamServiceProfileNum_Object = MibTableColumn
rcEtherSamServiceProfileNum = _RcEtherSamServiceProfileNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 3),
    _RcEtherSamServiceProfileNum_Type()
)
rcEtherSamServiceProfileNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceProfileNum.setStatus("current")


class _RcEtherSamServiceSvlan_Type(Integer32):
    """Custom type rcEtherSamServiceSvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RcEtherSamServiceSvlan_Type.__name__ = "Integer32"
_RcEtherSamServiceSvlan_Object = MibTableColumn
rcEtherSamServiceSvlan = _RcEtherSamServiceSvlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 4),
    _RcEtherSamServiceSvlan_Type()
)
rcEtherSamServiceSvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceSvlan.setStatus("current")


class _RcEtherSamServiceCos_Type(Integer32):
    """Custom type rcEtherSamServiceCos based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcEtherSamServiceCos_Type.__name__ = "Integer32"
_RcEtherSamServiceCos_Object = MibTableColumn
rcEtherSamServiceCos = _RcEtherSamServiceCos_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 5),
    _RcEtherSamServiceCos_Type()
)
rcEtherSamServiceCos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceCos.setStatus("current")
_RcEtherSamServiceUNI_Type = Integer32
_RcEtherSamServiceUNI_Object = MibTableColumn
rcEtherSamServiceUNI = _RcEtherSamServiceUNI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 6),
    _RcEtherSamServiceUNI_Type()
)
rcEtherSamServiceUNI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceUNI.setStatus("current")
_RcEtherSamServiceNNI_Type = Integer32
_RcEtherSamServiceNNI_Object = MibTableColumn
rcEtherSamServiceNNI = _RcEtherSamServiceNNI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 7),
    _RcEtherSamServiceNNI_Type()
)
rcEtherSamServiceNNI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceNNI.setStatus("current")


class _RcEtherSamServiceCir_Type(Integer32):
    """Custom type rcEtherSamServiceCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_RcEtherSamServiceCir_Type.__name__ = "Integer32"
_RcEtherSamServiceCir_Object = MibTableColumn
rcEtherSamServiceCir = _RcEtherSamServiceCir_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 8),
    _RcEtherSamServiceCir_Type()
)
rcEtherSamServiceCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceCir.setStatus("current")


class _RcEtherSamServiceEir_Type(Integer32):
    """Custom type rcEtherSamServiceEir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_RcEtherSamServiceEir_Type.__name__ = "Integer32"
_RcEtherSamServiceEir_Object = MibTableColumn
rcEtherSamServiceEir = _RcEtherSamServiceEir_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 9),
    _RcEtherSamServiceEir_Type()
)
rcEtherSamServiceEir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceEir.setStatus("current")


class _RcEtherSamServiceMDL_Type(Integer32):
    """Custom type rcEtherSamServiceMDL based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_RcEtherSamServiceMDL_Type.__name__ = "Integer32"
_RcEtherSamServiceMDL_Object = MibTableColumn
rcEtherSamServiceMDL = _RcEtherSamServiceMDL_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 10),
    _RcEtherSamServiceMDL_Type()
)
rcEtherSamServiceMDL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceMDL.setStatus("current")
_RcEtherSamServiceDMAC_Type = MacAddress
_RcEtherSamServiceDMAC_Object = MibTableColumn
rcEtherSamServiceDMAC = _RcEtherSamServiceDMAC_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 11),
    _RcEtherSamServiceDMAC_Type()
)
rcEtherSamServiceDMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceDMAC.setStatus("current")


class _RcEtherSamServiceThresholdAvail_Type(Unsigned32):
    """Custom type rcEtherSamServiceThresholdAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamServiceThresholdAvail_Type.__name__ = "Unsigned32"
_RcEtherSamServiceThresholdAvail_Object = MibTableColumn
rcEtherSamServiceThresholdAvail = _RcEtherSamServiceThresholdAvail_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 12),
    _RcEtherSamServiceThresholdAvail_Type()
)
rcEtherSamServiceThresholdAvail.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceThresholdAvail.setStatus("current")


class _RcEtherSamServiceThresholdFD_Type(Unsigned32):
    """Custom type rcEtherSamServiceThresholdFD based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamServiceThresholdFD_Type.__name__ = "Unsigned32"
_RcEtherSamServiceThresholdFD_Object = MibTableColumn
rcEtherSamServiceThresholdFD = _RcEtherSamServiceThresholdFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 13),
    _RcEtherSamServiceThresholdFD_Type()
)
rcEtherSamServiceThresholdFD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceThresholdFD.setStatus("current")


class _RcEtherSamServiceThresholdFDV_Type(Unsigned32):
    """Custom type rcEtherSamServiceThresholdFDV based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamServiceThresholdFDV_Type.__name__ = "Unsigned32"
_RcEtherSamServiceThresholdFDV_Object = MibTableColumn
rcEtherSamServiceThresholdFDV = _RcEtherSamServiceThresholdFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 14),
    _RcEtherSamServiceThresholdFDV_Type()
)
rcEtherSamServiceThresholdFDV.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceThresholdFDV.setStatus("current")


class _RcEtherSamServiceThresholdFLR_Type(Unsigned32):
    """Custom type rcEtherSamServiceThresholdFLR based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamServiceThresholdFLR_Type.__name__ = "Unsigned32"
_RcEtherSamServiceThresholdFLR_Object = MibTableColumn
rcEtherSamServiceThresholdFLR = _RcEtherSamServiceThresholdFLR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 15),
    _RcEtherSamServiceThresholdFLR_Type()
)
rcEtherSamServiceThresholdFLR.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceThresholdFLR.setStatus("current")


class _RcEtherSamServiceBandWidth_Type(Integer32):
    """Custom type rcEtherSamServiceBandWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1048576),
    )


_RcEtherSamServiceBandWidth_Type.__name__ = "Integer32"
_RcEtherSamServiceBandWidth_Object = MibTableColumn
rcEtherSamServiceBandWidth = _RcEtherSamServiceBandWidth_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 16),
    _RcEtherSamServiceBandWidth_Type()
)
rcEtherSamServiceBandWidth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceBandWidth.setStatus("current")
_RcEtherSamServiceRowStatus_Type = RowStatus
_RcEtherSamServiceRowStatus_Object = MibTableColumn
rcEtherSamServiceRowStatus = _RcEtherSamServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 17),
    _RcEtherSamServiceRowStatus_Type()
)
rcEtherSamServiceRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceRowStatus.setStatus("current")
_RcEtherSamServiceSecondNNI_Type = Integer32
_RcEtherSamServiceSecondNNI_Object = MibTableColumn
rcEtherSamServiceSecondNNI = _RcEtherSamServiceSecondNNI_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 18),
    _RcEtherSamServiceSecondNNI_Type()
)
rcEtherSamServiceSecondNNI.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceSecondNNI.setStatus("current")


class _RcEtherSamServiceCfgBypassUniEnable_Type(EnableVar):
    """Custom type rcEtherSamServiceCfgBypassUniEnable based on EnableVar"""
    defaultValue = 2


_RcEtherSamServiceCfgBypassUniEnable_Type.__name__ = "EnableVar"
_RcEtherSamServiceCfgBypassUniEnable_Object = MibTableColumn
rcEtherSamServiceCfgBypassUniEnable = _RcEtherSamServiceCfgBypassUniEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 19),
    _RcEtherSamServiceCfgBypassUniEnable_Type()
)
rcEtherSamServiceCfgBypassUniEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceCfgBypassUniEnable.setStatus("current")
_RcEtherSamServiceDIPAddressType_Type = InetAddressType
_RcEtherSamServiceDIPAddressType_Object = MibTableColumn
rcEtherSamServiceDIPAddressType = _RcEtherSamServiceDIPAddressType_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 20),
    _RcEtherSamServiceDIPAddressType_Type()
)
rcEtherSamServiceDIPAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceDIPAddressType.setStatus("current")
_RcEtherSamServiceDIPAddress_Type = InetAddress
_RcEtherSamServiceDIPAddress_Object = MibTableColumn
rcEtherSamServiceDIPAddress = _RcEtherSamServiceDIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 2, 1, 21),
    _RcEtherSamServiceDIPAddress_Type()
)
rcEtherSamServiceDIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamServiceDIPAddress.setStatus("current")
_RcEtherSamCfgResultTable_Object = MibTable
rcEtherSamCfgResultTable = _RcEtherSamCfgResultTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 3)
)
if mibBuilder.loadTexts:
    rcEtherSamCfgResultTable.setStatus("current")
_RcEtherSamCfgResultEntry_Object = MibTableRow
rcEtherSamCfgResultEntry = _RcEtherSamCfgResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 3, 1)
)
rcEtherSamCfgResultEntry.setIndexNames(
    (0, "RAISECOM-ETHERSAM-MIB", "rcEtherSamServiceIndex"),
    (0, "RAISECOM-ETHERSAM-MIB", "rcEtherSamCfgStepNum"),
)
if mibBuilder.loadTexts:
    rcEtherSamCfgResultEntry.setStatus("current")


class _RcEtherSamCfgStepNum_Type(Integer32):
    """Custom type rcEtherSamCfgStepNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_RcEtherSamCfgStepNum_Type.__name__ = "Integer32"
_RcEtherSamCfgStepNum_Object = MibTableColumn
rcEtherSamCfgStepNum = _RcEtherSamCfgStepNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 3, 1, 1),
    _RcEtherSamCfgStepNum_Type()
)
rcEtherSamCfgStepNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcEtherSamCfgStepNum.setStatus("current")


class _RcEtherSamCfgResult_Type(Integer32):
    """Custom type rcEtherSamCfgResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_RcEtherSamCfgResult_Type.__name__ = "Integer32"
_RcEtherSamCfgResult_Object = MibTableColumn
rcEtherSamCfgResult = _RcEtherSamCfgResult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 3, 1, 2),
    _RcEtherSamCfgResult_Type()
)
rcEtherSamCfgResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamCfgResult.setStatus("current")
_RcEtherSamCfgReceiveIR_Type = Integer32
_RcEtherSamCfgReceiveIR_Object = MibTableColumn
rcEtherSamCfgReceiveIR = _RcEtherSamCfgReceiveIR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 3, 1, 3),
    _RcEtherSamCfgReceiveIR_Type()
)
rcEtherSamCfgReceiveIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamCfgReceiveIR.setStatus("current")


class _RcEtherSamCfgFD_Type(Unsigned32):
    """Custom type rcEtherSamCfgFD based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamCfgFD_Type.__name__ = "Unsigned32"
_RcEtherSamCfgFD_Object = MibTableColumn
rcEtherSamCfgFD = _RcEtherSamCfgFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 3, 1, 4),
    _RcEtherSamCfgFD_Type()
)
rcEtherSamCfgFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamCfgFD.setStatus("current")


class _RcEtherSamCfgFDV_Type(Unsigned32):
    """Custom type rcEtherSamCfgFDV based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamCfgFDV_Type.__name__ = "Unsigned32"
_RcEtherSamCfgFDV_Object = MibTableColumn
rcEtherSamCfgFDV = _RcEtherSamCfgFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 3, 1, 5),
    _RcEtherSamCfgFDV_Type()
)
rcEtherSamCfgFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamCfgFDV.setStatus("current")


class _RcEtherSamCfgFLRf_Type(Unsigned32):
    """Custom type rcEtherSamCfgFLRf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamCfgFLRf_Type.__name__ = "Unsigned32"
_RcEtherSamCfgFLRf_Object = MibTableColumn
rcEtherSamCfgFLRf = _RcEtherSamCfgFLRf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 3, 1, 6),
    _RcEtherSamCfgFLRf_Type()
)
rcEtherSamCfgFLRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamCfgFLRf.setStatus("current")


class _RcEtherSamCfgFLRb_Type(Unsigned32):
    """Custom type rcEtherSamCfgFLRb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamCfgFLRb_Type.__name__ = "Unsigned32"
_RcEtherSamCfgFLRb_Object = MibTableColumn
rcEtherSamCfgFLRb = _RcEtherSamCfgFLRb_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 3, 1, 7),
    _RcEtherSamCfgFLRb_Type()
)
rcEtherSamCfgFLRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamCfgFLRb.setStatus("current")
_RcEtherSamPerformanceResultTable_Object = MibTable
rcEtherSamPerformanceResultTable = _RcEtherSamPerformanceResultTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4)
)
if mibBuilder.loadTexts:
    rcEtherSamPerformanceResultTable.setStatus("current")
_RcEtherSamPerformanceResultEntry_Object = MibTableRow
rcEtherSamPerformanceResultEntry = _RcEtherSamPerformanceResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1)
)
rcEtherSamPerformanceResultEntry.setIndexNames(
    (0, "RAISECOM-ETHERSAM-MIB", "rcEtherSamServiceIndex"),
)
if mibBuilder.loadTexts:
    rcEtherSamPerformanceResultEntry.setStatus("current")


class _RcEtherSamPerformanceResult_Type(Integer32):
    """Custom type rcEtherSamPerformanceResult based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pass", 1),
          ("fail", 2))
    )


_RcEtherSamPerformanceResult_Type.__name__ = "Integer32"
_RcEtherSamPerformanceResult_Object = MibTableColumn
rcEtherSamPerformanceResult = _RcEtherSamPerformanceResult_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 1),
    _RcEtherSamPerformanceResult_Type()
)
rcEtherSamPerformanceResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceResult.setStatus("current")
_RcEtherSamPerformanceCurrentReceiveIR_Type = Integer32
_RcEtherSamPerformanceCurrentReceiveIR_Object = MibTableColumn
rcEtherSamPerformanceCurrentReceiveIR = _RcEtherSamPerformanceCurrentReceiveIR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 2),
    _RcEtherSamPerformanceCurrentReceiveIR_Type()
)
rcEtherSamPerformanceCurrentReceiveIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceCurrentReceiveIR.setStatus("current")
_RcEtherSamPerformanceMaxReceiveIR_Type = Integer32
_RcEtherSamPerformanceMaxReceiveIR_Object = MibTableColumn
rcEtherSamPerformanceMaxReceiveIR = _RcEtherSamPerformanceMaxReceiveIR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 3),
    _RcEtherSamPerformanceMaxReceiveIR_Type()
)
rcEtherSamPerformanceMaxReceiveIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceMaxReceiveIR.setStatus("current")
_RcEtherSamPerformanceMinReceiveIR_Type = Integer32
_RcEtherSamPerformanceMinReceiveIR_Object = MibTableColumn
rcEtherSamPerformanceMinReceiveIR = _RcEtherSamPerformanceMinReceiveIR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 4),
    _RcEtherSamPerformanceMinReceiveIR_Type()
)
rcEtherSamPerformanceMinReceiveIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceMinReceiveIR.setStatus("current")
_RcEtherSamPerformanceAverageReceiveIR_Type = Integer32
_RcEtherSamPerformanceAverageReceiveIR_Object = MibTableColumn
rcEtherSamPerformanceAverageReceiveIR = _RcEtherSamPerformanceAverageReceiveIR_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 5),
    _RcEtherSamPerformanceAverageReceiveIR_Type()
)
rcEtherSamPerformanceAverageReceiveIR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceAverageReceiveIR.setStatus("current")


class _RcEtherSamPerformanceCurrentFD_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceCurrentFD based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamPerformanceCurrentFD_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceCurrentFD_Object = MibTableColumn
rcEtherSamPerformanceCurrentFD = _RcEtherSamPerformanceCurrentFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 6),
    _RcEtherSamPerformanceCurrentFD_Type()
)
rcEtherSamPerformanceCurrentFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceCurrentFD.setStatus("current")


class _RcEtherSamPerformanceMaxFD_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceMaxFD based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamPerformanceMaxFD_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceMaxFD_Object = MibTableColumn
rcEtherSamPerformanceMaxFD = _RcEtherSamPerformanceMaxFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 7),
    _RcEtherSamPerformanceMaxFD_Type()
)
rcEtherSamPerformanceMaxFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceMaxFD.setStatus("current")


class _RcEtherSamPerformanceMinFD_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceMinFD based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamPerformanceMinFD_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceMinFD_Object = MibTableColumn
rcEtherSamPerformanceMinFD = _RcEtherSamPerformanceMinFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 8),
    _RcEtherSamPerformanceMinFD_Type()
)
rcEtherSamPerformanceMinFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceMinFD.setStatus("current")


class _RcEtherSamPerformanceAverageFD_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceAverageFD based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamPerformanceAverageFD_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceAverageFD_Object = MibTableColumn
rcEtherSamPerformanceAverageFD = _RcEtherSamPerformanceAverageFD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 9),
    _RcEtherSamPerformanceAverageFD_Type()
)
rcEtherSamPerformanceAverageFD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceAverageFD.setStatus("current")


class _RcEtherSamPerformanceCurrentFDV_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceCurrentFDV based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamPerformanceCurrentFDV_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceCurrentFDV_Object = MibTableColumn
rcEtherSamPerformanceCurrentFDV = _RcEtherSamPerformanceCurrentFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 10),
    _RcEtherSamPerformanceCurrentFDV_Type()
)
rcEtherSamPerformanceCurrentFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceCurrentFDV.setStatus("current")


class _RcEtherSamPerformanceMaxFDV_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceMaxFDV based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamPerformanceMaxFDV_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceMaxFDV_Object = MibTableColumn
rcEtherSamPerformanceMaxFDV = _RcEtherSamPerformanceMaxFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 11),
    _RcEtherSamPerformanceMaxFDV_Type()
)
rcEtherSamPerformanceMaxFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceMaxFDV.setStatus("current")


class _RcEtherSamPerformanceMinFDV_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceMinFDV based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamPerformanceMinFDV_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceMinFDV_Object = MibTableColumn
rcEtherSamPerformanceMinFDV = _RcEtherSamPerformanceMinFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 12),
    _RcEtherSamPerformanceMinFDV_Type()
)
rcEtherSamPerformanceMinFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceMinFDV.setStatus("current")


class _RcEtherSamPerformanceAverageFDV_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceAverageFDV based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000),
    )


_RcEtherSamPerformanceAverageFDV_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceAverageFDV_Object = MibTableColumn
rcEtherSamPerformanceAverageFDV = _RcEtherSamPerformanceAverageFDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 13),
    _RcEtherSamPerformanceAverageFDV_Type()
)
rcEtherSamPerformanceAverageFDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceAverageFDV.setStatus("current")


class _RcEtherSamPerformanceCurrentFLRf_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceCurrentFLRf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamPerformanceCurrentFLRf_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceCurrentFLRf_Object = MibTableColumn
rcEtherSamPerformanceCurrentFLRf = _RcEtherSamPerformanceCurrentFLRf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 14),
    _RcEtherSamPerformanceCurrentFLRf_Type()
)
rcEtherSamPerformanceCurrentFLRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceCurrentFLRf.setStatus("current")


class _RcEtherSamPerformanceMaxFLRf_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceMaxFLRf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamPerformanceMaxFLRf_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceMaxFLRf_Object = MibTableColumn
rcEtherSamPerformanceMaxFLRf = _RcEtherSamPerformanceMaxFLRf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 15),
    _RcEtherSamPerformanceMaxFLRf_Type()
)
rcEtherSamPerformanceMaxFLRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceMaxFLRf.setStatus("current")


class _RcEtherSamPerformanceMinFLRf_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceMinFLRf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamPerformanceMinFLRf_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceMinFLRf_Object = MibTableColumn
rcEtherSamPerformanceMinFLRf = _RcEtherSamPerformanceMinFLRf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 16),
    _RcEtherSamPerformanceMinFLRf_Type()
)
rcEtherSamPerformanceMinFLRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceMinFLRf.setStatus("current")


class _RcEtherSamPerformanceAverageFLRf_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceAverageFLRf based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamPerformanceAverageFLRf_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceAverageFLRf_Object = MibTableColumn
rcEtherSamPerformanceAverageFLRf = _RcEtherSamPerformanceAverageFLRf_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 17),
    _RcEtherSamPerformanceAverageFLRf_Type()
)
rcEtherSamPerformanceAverageFLRf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceAverageFLRf.setStatus("current")


class _RcEtherSamPerformanceCurrentFLRb_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceCurrentFLRb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamPerformanceCurrentFLRb_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceCurrentFLRb_Object = MibTableColumn
rcEtherSamPerformanceCurrentFLRb = _RcEtherSamPerformanceCurrentFLRb_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 18),
    _RcEtherSamPerformanceCurrentFLRb_Type()
)
rcEtherSamPerformanceCurrentFLRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceCurrentFLRb.setStatus("current")


class _RcEtherSamPerformanceMaxFLRb_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceMaxFLRb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamPerformanceMaxFLRb_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceMaxFLRb_Object = MibTableColumn
rcEtherSamPerformanceMaxFLRb = _RcEtherSamPerformanceMaxFLRb_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 19),
    _RcEtherSamPerformanceMaxFLRb_Type()
)
rcEtherSamPerformanceMaxFLRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceMaxFLRb.setStatus("current")


class _RcEtherSamPerformanceMinFLRb_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceMinFLRb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamPerformanceMinFLRb_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceMinFLRb_Object = MibTableColumn
rcEtherSamPerformanceMinFLRb = _RcEtherSamPerformanceMinFLRb_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 20),
    _RcEtherSamPerformanceMinFLRb_Type()
)
rcEtherSamPerformanceMinFLRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceMinFLRb.setStatus("current")


class _RcEtherSamPerformanceAverageFLRb_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceAverageFLRb based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamPerformanceAverageFLRb_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceAverageFLRb_Object = MibTableColumn
rcEtherSamPerformanceAverageFLRb = _RcEtherSamPerformanceAverageFLRb_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 21),
    _RcEtherSamPerformanceAverageFLRb_Type()
)
rcEtherSamPerformanceAverageFLRb.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceAverageFLRb.setStatus("current")


class _RcEtherSamPerformanceAvail_Type(Unsigned32):
    """Custom type rcEtherSamPerformanceAvail based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100000),
    )


_RcEtherSamPerformanceAvail_Type.__name__ = "Unsigned32"
_RcEtherSamPerformanceAvail_Object = MibTableColumn
rcEtherSamPerformanceAvail = _RcEtherSamPerformanceAvail_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 4, 1, 22),
    _RcEtherSamPerformanceAvail_Type()
)
rcEtherSamPerformanceAvail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamPerformanceAvail.setStatus("current")
_RcEtherSamStatisticTable_Object = MibTable
rcEtherSamStatisticTable = _RcEtherSamStatisticTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5)
)
if mibBuilder.loadTexts:
    rcEtherSamStatisticTable.setStatus("current")
_RcEtherSamStatisticEntry_Object = MibTableRow
rcEtherSamStatisticEntry = _RcEtherSamStatisticEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1)
)
rcEtherSamStatisticEntry.setIndexNames(
    (0, "RAISECOM-ETHERSAM-MIB", "rcEtherSamServiceIndex"),
)
if mibBuilder.loadTexts:
    rcEtherSamStatisticEntry.setStatus("current")
_RcEtherSamStatisticDropEvents_Type = Counter32
_RcEtherSamStatisticDropEvents_Object = MibTableColumn
rcEtherSamStatisticDropEvents = _RcEtherSamStatisticDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 1),
    _RcEtherSamStatisticDropEvents_Type()
)
rcEtherSamStatisticDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticDropEvents.setStatus("current")
_RcEtherSamStatisticCRCAlignErrors_Type = Counter32
_RcEtherSamStatisticCRCAlignErrors_Object = MibTableColumn
rcEtherSamStatisticCRCAlignErrors = _RcEtherSamStatisticCRCAlignErrors_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 2),
    _RcEtherSamStatisticCRCAlignErrors_Type()
)
rcEtherSamStatisticCRCAlignErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticCRCAlignErrors.setStatus("current")
_RcEtherSamStatisticUndersizePkts_Type = Counter32
_RcEtherSamStatisticUndersizePkts_Object = MibTableColumn
rcEtherSamStatisticUndersizePkts = _RcEtherSamStatisticUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 3),
    _RcEtherSamStatisticUndersizePkts_Type()
)
rcEtherSamStatisticUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticUndersizePkts.setStatus("current")
_RcEtherSamStatisticFragments_Type = Counter32
_RcEtherSamStatisticFragments_Object = MibTableColumn
rcEtherSamStatisticFragments = _RcEtherSamStatisticFragments_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 4),
    _RcEtherSamStatisticFragments_Type()
)
rcEtherSamStatisticFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticFragments.setStatus("current")
_RcEtherSamStatisticJabbers_Type = Counter32
_RcEtherSamStatisticJabbers_Object = MibTableColumn
rcEtherSamStatisticJabbers = _RcEtherSamStatisticJabbers_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 5),
    _RcEtherSamStatisticJabbers_Type()
)
rcEtherSamStatisticJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticJabbers.setStatus("current")
_RcEtherSamStatisticCollisions_Type = Counter32
_RcEtherSamStatisticCollisions_Object = MibTableColumn
rcEtherSamStatisticCollisions = _RcEtherSamStatisticCollisions_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 6),
    _RcEtherSamStatisticCollisions_Type()
)
rcEtherSamStatisticCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticCollisions.setStatus("current")
_RcEtherSamStatisticInUnicast_Type = Counter64
_RcEtherSamStatisticInUnicast_Object = MibTableColumn
rcEtherSamStatisticInUnicast = _RcEtherSamStatisticInUnicast_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 7),
    _RcEtherSamStatisticInUnicast_Type()
)
rcEtherSamStatisticInUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticInUnicast.setStatus("current")
_RcEtherSamStatisticInMulticast_Type = Counter64
_RcEtherSamStatisticInMulticast_Object = MibTableColumn
rcEtherSamStatisticInMulticast = _RcEtherSamStatisticInMulticast_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 8),
    _RcEtherSamStatisticInMulticast_Type()
)
rcEtherSamStatisticInMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticInMulticast.setStatus("current")
_RcEtherSamStatisticInBroadcast_Type = Counter64
_RcEtherSamStatisticInBroadcast_Object = MibTableColumn
rcEtherSamStatisticInBroadcast = _RcEtherSamStatisticInBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 9),
    _RcEtherSamStatisticInBroadcast_Type()
)
rcEtherSamStatisticInBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticInBroadcast.setStatus("current")
_RcEtherSamStatisticOutUnicast_Type = Counter64
_RcEtherSamStatisticOutUnicast_Object = MibTableColumn
rcEtherSamStatisticOutUnicast = _RcEtherSamStatisticOutUnicast_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 10),
    _RcEtherSamStatisticOutUnicast_Type()
)
rcEtherSamStatisticOutUnicast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticOutUnicast.setStatus("current")
_RcEtherSamStatisticOutMulticast_Type = Counter64
_RcEtherSamStatisticOutMulticast_Object = MibTableColumn
rcEtherSamStatisticOutMulticast = _RcEtherSamStatisticOutMulticast_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 11),
    _RcEtherSamStatisticOutMulticast_Type()
)
rcEtherSamStatisticOutMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticOutMulticast.setStatus("current")
_RcEtherSamStatisticOutBroadcast_Type = Counter64
_RcEtherSamStatisticOutBroadcast_Object = MibTableColumn
rcEtherSamStatisticOutBroadcast = _RcEtherSamStatisticOutBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 12),
    _RcEtherSamStatisticOutBroadcast_Type()
)
rcEtherSamStatisticOutBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatisticOutBroadcast.setStatus("current")
_RcEtherSamStatistic64to127octets_Type = Counter64
_RcEtherSamStatistic64to127octets_Object = MibTableColumn
rcEtherSamStatistic64to127octets = _RcEtherSamStatistic64to127octets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 13),
    _RcEtherSamStatistic64to127octets_Type()
)
rcEtherSamStatistic64to127octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatistic64to127octets.setStatus("current")
_RcEtherSamStatistic128to255octets_Type = Counter64
_RcEtherSamStatistic128to255octets_Object = MibTableColumn
rcEtherSamStatistic128to255octets = _RcEtherSamStatistic128to255octets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 14),
    _RcEtherSamStatistic128to255octets_Type()
)
rcEtherSamStatistic128to255octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatistic128to255octets.setStatus("current")
_RcEtherSamStatistic256to511octets_Type = Counter64
_RcEtherSamStatistic256to511octets_Object = MibTableColumn
rcEtherSamStatistic256to511octets = _RcEtherSamStatistic256to511octets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 15),
    _RcEtherSamStatistic256to511octets_Type()
)
rcEtherSamStatistic256to511octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatistic256to511octets.setStatus("current")
_RcEtherSamStatistic512to1023octets_Type = Counter64
_RcEtherSamStatistic512to1023octets_Object = MibTableColumn
rcEtherSamStatistic512to1023octets = _RcEtherSamStatistic512to1023octets_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 16),
    _RcEtherSamStatistic512to1023octets_Type()
)
rcEtherSamStatistic512to1023octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatistic512to1023octets.setStatus("current")
_RcEtherSamStatistic1024to1518Octet_Type = Counter64
_RcEtherSamStatistic1024to1518Octet_Object = MibTableColumn
rcEtherSamStatistic1024to1518Octet = _RcEtherSamStatistic1024to1518Octet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 17),
    _RcEtherSamStatistic1024to1518Octet_Type()
)
rcEtherSamStatistic1024to1518Octet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatistic1024to1518Octet.setStatus("current")
_RcEtherSamStatistic1519Octet_Type = Counter64
_RcEtherSamStatistic1519Octet_Object = MibTableColumn
rcEtherSamStatistic1519Octet = _RcEtherSamStatistic1519Octet_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 5, 1, 18),
    _RcEtherSamStatistic1519Octet_Type()
)
rcEtherSamStatistic1519Octet.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSamStatistic1519Octet.setStatus("current")
_RcEtherSam2544ResultTable_Object = MibTable
rcEtherSam2544ResultTable = _RcEtherSam2544ResultTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 6)
)
if mibBuilder.loadTexts:
    rcEtherSam2544ResultTable.setStatus("current")
_RcEtherSam2544ResultEntry_Object = MibTableRow
rcEtherSam2544ResultEntry = _RcEtherSam2544ResultEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 6, 1)
)
rcEtherSam2544ResultEntry.setIndexNames(
    (0, "RAISECOM-ETHERSAM-MIB", "rcEtherSamServiceIndex"),
    (0, "RAISECOM-ETHERSAM-MIB", "rcEtherSam2544FrameSize"),
)
if mibBuilder.loadTexts:
    rcEtherSam2544ResultEntry.setStatus("current")
_RcEtherSam2544FrameSize_Type = Integer32
_RcEtherSam2544FrameSize_Object = MibTableColumn
rcEtherSam2544FrameSize = _RcEtherSam2544FrameSize_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 6, 1, 1),
    _RcEtherSam2544FrameSize_Type()
)
rcEtherSam2544FrameSize.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    rcEtherSam2544FrameSize.setStatus("current")
_RcEtherSam2544Rate_Type = Integer32
_RcEtherSam2544Rate_Object = MibTableColumn
rcEtherSam2544Rate = _RcEtherSam2544Rate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 6, 1, 2),
    _RcEtherSam2544Rate_Type()
)
rcEtherSam2544Rate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSam2544Rate.setStatus("current")
_RcEtherSam2544BER_Type = Integer32
_RcEtherSam2544BER_Object = MibTableColumn
rcEtherSam2544BER = _RcEtherSam2544BER_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 6, 1, 3),
    _RcEtherSam2544BER_Type()
)
rcEtherSam2544BER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSam2544BER.setStatus("current")
_RcEtherSam2544FD_Type = Integer32
_RcEtherSam2544FD_Object = MibTableColumn
rcEtherSam2544FD = _RcEtherSam2544FD_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 6, 1, 4),
    _RcEtherSam2544FD_Type()
)
rcEtherSam2544FD.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSam2544FD.setStatus("current")
_RcEtherSam2544FDV_Type = Integer32
_RcEtherSam2544FDV_Object = MibTableColumn
rcEtherSam2544FDV = _RcEtherSam2544FDV_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 6, 1, 5),
    _RcEtherSam2544FDV_Type()
)
rcEtherSam2544FDV.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rcEtherSam2544FDV.setStatus("current")
_RcEtherSamFlowFrameLengthTable_Object = MibTable
rcEtherSamFlowFrameLengthTable = _RcEtherSamFlowFrameLengthTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 7)
)
if mibBuilder.loadTexts:
    rcEtherSamFlowFrameLengthTable.setStatus("current")
_RcEtherSamFlowFrameLengthEntry_Object = MibTableRow
rcEtherSamFlowFrameLengthEntry = _RcEtherSamFlowFrameLengthEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 7, 1)
)
rcEtherSamFlowFrameLengthEntry.setIndexNames(
    (0, "RAISECOM-ETHERSAM-MIB", "rcEtherSamFlowIndex"),
)
if mibBuilder.loadTexts:
    rcEtherSamFlowFrameLengthEntry.setStatus("current")


class _RcEtherSamFlowFrameNum_Type(Integer32):
    """Custom type rcEtherSamFlowFrameNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 6),
    )


_RcEtherSamFlowFrameNum_Type.__name__ = "Integer32"
_RcEtherSamFlowFrameNum_Object = MibTableColumn
rcEtherSamFlowFrameNum = _RcEtherSamFlowFrameNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 7, 1, 1),
    _RcEtherSamFlowFrameNum_Type()
)
rcEtherSamFlowFrameNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrameNum.setStatus("current")


class _RcEtherSamFlowFrame1_Type(Integer32):
    """Custom type rcEtherSamFlowFrame1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 12288),
    )


_RcEtherSamFlowFrame1_Type.__name__ = "Integer32"
_RcEtherSamFlowFrame1_Object = MibTableColumn
rcEtherSamFlowFrame1 = _RcEtherSamFlowFrame1_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 7, 1, 2),
    _RcEtherSamFlowFrame1_Type()
)
rcEtherSamFlowFrame1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrame1.setStatus("current")


class _RcEtherSamFlowFrame2_Type(Integer32):
    """Custom type rcEtherSamFlowFrame2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 12288),
    )


_RcEtherSamFlowFrame2_Type.__name__ = "Integer32"
_RcEtherSamFlowFrame2_Object = MibTableColumn
rcEtherSamFlowFrame2 = _RcEtherSamFlowFrame2_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 7, 1, 3),
    _RcEtherSamFlowFrame2_Type()
)
rcEtherSamFlowFrame2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrame2.setStatus("current")


class _RcEtherSamFlowFrame3_Type(Integer32):
    """Custom type rcEtherSamFlowFrame3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 12288),
    )


_RcEtherSamFlowFrame3_Type.__name__ = "Integer32"
_RcEtherSamFlowFrame3_Object = MibTableColumn
rcEtherSamFlowFrame3 = _RcEtherSamFlowFrame3_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 7, 1, 4),
    _RcEtherSamFlowFrame3_Type()
)
rcEtherSamFlowFrame3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrame3.setStatus("current")


class _RcEtherSamFlowFrame4_Type(Integer32):
    """Custom type rcEtherSamFlowFrame4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 12288),
    )


_RcEtherSamFlowFrame4_Type.__name__ = "Integer32"
_RcEtherSamFlowFrame4_Object = MibTableColumn
rcEtherSamFlowFrame4 = _RcEtherSamFlowFrame4_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 7, 1, 5),
    _RcEtherSamFlowFrame4_Type()
)
rcEtherSamFlowFrame4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrame4.setStatus("current")


class _RcEtherSamFlowFrame5_Type(Integer32):
    """Custom type rcEtherSamFlowFrame5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 12288),
    )


_RcEtherSamFlowFrame5_Type.__name__ = "Integer32"
_RcEtherSamFlowFrame5_Object = MibTableColumn
rcEtherSamFlowFrame5 = _RcEtherSamFlowFrame5_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 7, 1, 6),
    _RcEtherSamFlowFrame5_Type()
)
rcEtherSamFlowFrame5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrame5.setStatus("current")


class _RcEtherSamFlowFrame6_Type(Integer32):
    """Custom type rcEtherSamFlowFrame6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 12288),
    )


_RcEtherSamFlowFrame6_Type.__name__ = "Integer32"
_RcEtherSamFlowFrame6_Object = MibTableColumn
rcEtherSamFlowFrame6 = _RcEtherSamFlowFrame6_Object(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 2, 7, 1, 7),
    _RcEtherSamFlowFrame6_Type()
)
rcEtherSamFlowFrame6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    rcEtherSamFlowFrame6.setStatus("current")
_RcEtherSamTestTrapGroup_ObjectIdentity = ObjectIdentity
rcEtherSamTestTrapGroup = _RcEtherSamTestTrapGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 3)
)

# Managed Objects groups


# Notification objects

rcEtherSamServiceTestFailTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 3, 1)
)
rcEtherSamServiceTestFailTrap.setObjects(
    ("RAISECOM-ETHERSAM-MIB", "rcEtherSamServiceIndex")
)
if mibBuilder.loadTexts:
    rcEtherSamServiceTestFailTrap.setStatus(
        "current"
    )

rcEtherSamServiceFinishTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 3, 2)
)
rcEtherSamServiceFinishTrap.setObjects(
    ("RAISECOM-ETHERSAM-MIB", "rcEtherSamServiceTestResult")
)
if mibBuilder.loadTexts:
    rcEtherSamServiceFinishTrap.setStatus(
        "current"
    )

rcEtherSam2544FinishTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 6, 1, 74, 3, 3)
)
rcEtherSam2544FinishTrap.setObjects(
    ("RAISECOM-ETHERSAM-MIB", "rcEtherSamServiceList")
)
if mibBuilder.loadTexts:
    rcEtherSam2544FinishTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-ETHERSAM-MIB",
    **{"rcEtherSam": rcEtherSam,
       "rcEtherSamGlobalGroup": rcEtherSamGlobalGroup,
       "rcEtherSamServiceList": rcEtherSamServiceList,
       "rcEtherSamServiceTestType": rcEtherSamServiceTestType,
       "rcEtherSamServiceTestOperate": rcEtherSamServiceTestOperate,
       "rcEtherSamPerformanceDuration": rcEtherSamPerformanceDuration,
       "rcEtherSamTestElapsedTime": rcEtherSamTestElapsedTime,
       "rcEtherSamServiceTestResult": rcEtherSamServiceTestResult,
       "rcEtherSamTestGroup": rcEtherSamTestGroup,
       "rcEtherSamFlowTable": rcEtherSamFlowTable,
       "rcEtherSamFlowEntry": rcEtherSamFlowEntry,
       "rcEtherSamFlowIndex": rcEtherSamFlowIndex,
       "rcEtherSamFlowFrameType": rcEtherSamFlowFrameType,
       "rcEtherSamFlowFrameEtherType": rcEtherSamFlowFrameEtherType,
       "rcEtherSamFlowFrameLengthType": rcEtherSamFlowFrameLengthType,
       "rcEtherSamFlowFrameSize": rcEtherSamFlowFrameSize,
       "rcEtherSamFlowFrameCvlan": rcEtherSamFlowFrameCvlan,
       "rcEtherSamFlowFrameCos": rcEtherSamFlowFrameCos,
       "rcEtherSamFlowRowStatus": rcEtherSamFlowRowStatus,
       "rcEtherSamFlowDescription": rcEtherSamFlowDescription,
       "rcEtherSamFlowDestAddr": rcEtherSamFlowDestAddr,
       "rcEtherSamFlowDscp": rcEtherSamFlowDscp,
       "rcEtherSamFlowDatePattern": rcEtherSamFlowDatePattern,
       "rcEtherSamFlowSourcePort": rcEtherSamFlowSourcePort,
       "rcEtherSamFlowDestPort": rcEtherSamFlowDestPort,
       "rcEtherSamFlowNextHopMac": rcEtherSamFlowNextHopMac,
       "rcEtherSamServiceTable": rcEtherSamServiceTable,
       "rcEtherSamServiceEntry": rcEtherSamServiceEntry,
       "rcEtherSamServiceIndex": rcEtherSamServiceIndex,
       "rcEtherSamServiceName": rcEtherSamServiceName,
       "rcEtherSamServiceProfileNum": rcEtherSamServiceProfileNum,
       "rcEtherSamServiceSvlan": rcEtherSamServiceSvlan,
       "rcEtherSamServiceCos": rcEtherSamServiceCos,
       "rcEtherSamServiceUNI": rcEtherSamServiceUNI,
       "rcEtherSamServiceNNI": rcEtherSamServiceNNI,
       "rcEtherSamServiceCir": rcEtherSamServiceCir,
       "rcEtherSamServiceEir": rcEtherSamServiceEir,
       "rcEtherSamServiceMDL": rcEtherSamServiceMDL,
       "rcEtherSamServiceDMAC": rcEtherSamServiceDMAC,
       "rcEtherSamServiceThresholdAvail": rcEtherSamServiceThresholdAvail,
       "rcEtherSamServiceThresholdFD": rcEtherSamServiceThresholdFD,
       "rcEtherSamServiceThresholdFDV": rcEtherSamServiceThresholdFDV,
       "rcEtherSamServiceThresholdFLR": rcEtherSamServiceThresholdFLR,
       "rcEtherSamServiceBandWidth": rcEtherSamServiceBandWidth,
       "rcEtherSamServiceRowStatus": rcEtherSamServiceRowStatus,
       "rcEtherSamServiceSecondNNI": rcEtherSamServiceSecondNNI,
       "rcEtherSamServiceCfgBypassUniEnable": rcEtherSamServiceCfgBypassUniEnable,
       "rcEtherSamServiceDIPAddressType": rcEtherSamServiceDIPAddressType,
       "rcEtherSamServiceDIPAddress": rcEtherSamServiceDIPAddress,
       "rcEtherSamCfgResultTable": rcEtherSamCfgResultTable,
       "rcEtherSamCfgResultEntry": rcEtherSamCfgResultEntry,
       "rcEtherSamCfgStepNum": rcEtherSamCfgStepNum,
       "rcEtherSamCfgResult": rcEtherSamCfgResult,
       "rcEtherSamCfgReceiveIR": rcEtherSamCfgReceiveIR,
       "rcEtherSamCfgFD": rcEtherSamCfgFD,
       "rcEtherSamCfgFDV": rcEtherSamCfgFDV,
       "rcEtherSamCfgFLRf": rcEtherSamCfgFLRf,
       "rcEtherSamCfgFLRb": rcEtherSamCfgFLRb,
       "rcEtherSamPerformanceResultTable": rcEtherSamPerformanceResultTable,
       "rcEtherSamPerformanceResultEntry": rcEtherSamPerformanceResultEntry,
       "rcEtherSamPerformanceResult": rcEtherSamPerformanceResult,
       "rcEtherSamPerformanceCurrentReceiveIR": rcEtherSamPerformanceCurrentReceiveIR,
       "rcEtherSamPerformanceMaxReceiveIR": rcEtherSamPerformanceMaxReceiveIR,
       "rcEtherSamPerformanceMinReceiveIR": rcEtherSamPerformanceMinReceiveIR,
       "rcEtherSamPerformanceAverageReceiveIR": rcEtherSamPerformanceAverageReceiveIR,
       "rcEtherSamPerformanceCurrentFD": rcEtherSamPerformanceCurrentFD,
       "rcEtherSamPerformanceMaxFD": rcEtherSamPerformanceMaxFD,
       "rcEtherSamPerformanceMinFD": rcEtherSamPerformanceMinFD,
       "rcEtherSamPerformanceAverageFD": rcEtherSamPerformanceAverageFD,
       "rcEtherSamPerformanceCurrentFDV": rcEtherSamPerformanceCurrentFDV,
       "rcEtherSamPerformanceMaxFDV": rcEtherSamPerformanceMaxFDV,
       "rcEtherSamPerformanceMinFDV": rcEtherSamPerformanceMinFDV,
       "rcEtherSamPerformanceAverageFDV": rcEtherSamPerformanceAverageFDV,
       "rcEtherSamPerformanceCurrentFLRf": rcEtherSamPerformanceCurrentFLRf,
       "rcEtherSamPerformanceMaxFLRf": rcEtherSamPerformanceMaxFLRf,
       "rcEtherSamPerformanceMinFLRf": rcEtherSamPerformanceMinFLRf,
       "rcEtherSamPerformanceAverageFLRf": rcEtherSamPerformanceAverageFLRf,
       "rcEtherSamPerformanceCurrentFLRb": rcEtherSamPerformanceCurrentFLRb,
       "rcEtherSamPerformanceMaxFLRb": rcEtherSamPerformanceMaxFLRb,
       "rcEtherSamPerformanceMinFLRb": rcEtherSamPerformanceMinFLRb,
       "rcEtherSamPerformanceAverageFLRb": rcEtherSamPerformanceAverageFLRb,
       "rcEtherSamPerformanceAvail": rcEtherSamPerformanceAvail,
       "rcEtherSamStatisticTable": rcEtherSamStatisticTable,
       "rcEtherSamStatisticEntry": rcEtherSamStatisticEntry,
       "rcEtherSamStatisticDropEvents": rcEtherSamStatisticDropEvents,
       "rcEtherSamStatisticCRCAlignErrors": rcEtherSamStatisticCRCAlignErrors,
       "rcEtherSamStatisticUndersizePkts": rcEtherSamStatisticUndersizePkts,
       "rcEtherSamStatisticFragments": rcEtherSamStatisticFragments,
       "rcEtherSamStatisticJabbers": rcEtherSamStatisticJabbers,
       "rcEtherSamStatisticCollisions": rcEtherSamStatisticCollisions,
       "rcEtherSamStatisticInUnicast": rcEtherSamStatisticInUnicast,
       "rcEtherSamStatisticInMulticast": rcEtherSamStatisticInMulticast,
       "rcEtherSamStatisticInBroadcast": rcEtherSamStatisticInBroadcast,
       "rcEtherSamStatisticOutUnicast": rcEtherSamStatisticOutUnicast,
       "rcEtherSamStatisticOutMulticast": rcEtherSamStatisticOutMulticast,
       "rcEtherSamStatisticOutBroadcast": rcEtherSamStatisticOutBroadcast,
       "rcEtherSamStatistic64to127octets": rcEtherSamStatistic64to127octets,
       "rcEtherSamStatistic128to255octets": rcEtherSamStatistic128to255octets,
       "rcEtherSamStatistic256to511octets": rcEtherSamStatistic256to511octets,
       "rcEtherSamStatistic512to1023octets": rcEtherSamStatistic512to1023octets,
       "rcEtherSamStatistic1024to1518Octet": rcEtherSamStatistic1024to1518Octet,
       "rcEtherSamStatistic1519Octet": rcEtherSamStatistic1519Octet,
       "rcEtherSam2544ResultTable": rcEtherSam2544ResultTable,
       "rcEtherSam2544ResultEntry": rcEtherSam2544ResultEntry,
       "rcEtherSam2544FrameSize": rcEtherSam2544FrameSize,
       "rcEtherSam2544Rate": rcEtherSam2544Rate,
       "rcEtherSam2544BER": rcEtherSam2544BER,
       "rcEtherSam2544FD": rcEtherSam2544FD,
       "rcEtherSam2544FDV": rcEtherSam2544FDV,
       "rcEtherSamFlowFrameLengthTable": rcEtherSamFlowFrameLengthTable,
       "rcEtherSamFlowFrameLengthEntry": rcEtherSamFlowFrameLengthEntry,
       "rcEtherSamFlowFrameNum": rcEtherSamFlowFrameNum,
       "rcEtherSamFlowFrame1": rcEtherSamFlowFrame1,
       "rcEtherSamFlowFrame2": rcEtherSamFlowFrame2,
       "rcEtherSamFlowFrame3": rcEtherSamFlowFrame3,
       "rcEtherSamFlowFrame4": rcEtherSamFlowFrame4,
       "rcEtherSamFlowFrame5": rcEtherSamFlowFrame5,
       "rcEtherSamFlowFrame6": rcEtherSamFlowFrame6,
       "rcEtherSamTestTrapGroup": rcEtherSamTestTrapGroup,
       "rcEtherSamServiceTestFailTrap": rcEtherSamServiceTestFailTrap,
       "rcEtherSamServiceFinishTrap": rcEtherSamServiceFinishTrap,
       "rcEtherSam2544FinishTrap": rcEtherSam2544FinishTrap}
)
