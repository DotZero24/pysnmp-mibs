# SNMP MIB module (NEWTEC-TSOVERIPOUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-TSOVERIPOUT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:55 2025
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

(ntcFunction,) = mibBuilder.importSymbols(
    "NEWTEC-MAIN-MIB",
    "ntcFunction")

(NtcAlarmState,
 NtcEnable,
 NtcNetworkAddress) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcAlarmState",
    "NtcEnable",
    "NtcNetworkAddress")

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

ntcTsOverIpOut = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400)
)
if mibBuilder.loadTexts:
    ntcTsOverIpOut.setRevisions(
        ("2017-07-10 12:00",
         "2016-12-05 12:00",
         "2016-02-02 07:00",
         "2014-09-09 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcTsOIpOutObjects_ObjectIdentity = ObjectIdentity
ntcTsOIpOutObjects = _NtcTsOIpOutObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1)
)
if mibBuilder.loadTexts:
    ntcTsOIpOutObjects.setStatus("current")
_NtcTsOIpOutConfiguration_ObjectIdentity = ObjectIdentity
ntcTsOIpOutConfiguration = _NtcTsOIpOutConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 1)
)
if mibBuilder.loadTexts:
    ntcTsOIpOutConfiguration.setStatus("current")


class _NtcTsOIpOutEnable_Type(NtcEnable):
    """Custom type ntcTsOIpOutEnable based on NtcEnable"""
    defaultValue = 0


_NtcTsOIpOutEnable_Type.__name__ = "NtcEnable"
_NtcTsOIpOutEnable_Object = MibScalar
ntcTsOIpOutEnable = _NtcTsOIpOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 1, 1),
    _NtcTsOIpOutEnable_Type()
)
ntcTsOIpOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpOutEnable.setStatus("current")


class _NtcTsOIpOutTsEncapProtocol_Type(Integer32):
    """Custom type ntcTsOIpOutTsEncapProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("rtp", 1),
          ("rtpfeccolsonly", 2),
          ("rtpfeccolsandrows", 3))
    )


_NtcTsOIpOutTsEncapProtocol_Type.__name__ = "Integer32"
_NtcTsOIpOutTsEncapProtocol_Object = MibScalar
ntcTsOIpOutTsEncapProtocol = _NtcTsOIpOutTsEncapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 1, 2),
    _NtcTsOIpOutTsEncapProtocol_Type()
)
ntcTsOIpOutTsEncapProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpOutTsEncapProtocol.setStatus("current")


class _NtcTsOIpOutDestUdpPort_Type(Unsigned32):
    """Custom type ntcTsOIpOutDestUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtcTsOIpOutDestUdpPort_Type.__name__ = "Unsigned32"
_NtcTsOIpOutDestUdpPort_Object = MibScalar
ntcTsOIpOutDestUdpPort = _NtcTsOIpOutDestUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 1, 3),
    _NtcTsOIpOutDestUdpPort_Type()
)
ntcTsOIpOutDestUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpOutDestUdpPort.setStatus("current")


class _NtcTsOIpOutDestIpAddress_Type(NtcNetworkAddress):
    """Custom type ntcTsOIpOutDestIpAddress based on NtcNetworkAddress"""
    defaultValue = OctetString("10.0.0.1")


_NtcTsOIpOutDestIpAddress_Type.__name__ = "NtcNetworkAddress"
_NtcTsOIpOutDestIpAddress_Object = MibScalar
ntcTsOIpOutDestIpAddress = _NtcTsOIpOutDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 1, 4),
    _NtcTsOIpOutDestIpAddress_Type()
)
ntcTsOIpOutDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpOutDestIpAddress.setStatus("current")


class _NtcTsOIpOutTtl_Type(Unsigned32):
    """Custom type ntcTsOIpOutTtl based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NtcTsOIpOutTtl_Type.__name__ = "Unsigned32"
_NtcTsOIpOutTtl_Object = MibScalar
ntcTsOIpOutTtl = _NtcTsOIpOutTtl_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 1, 5),
    _NtcTsOIpOutTtl_Type()
)
ntcTsOIpOutTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpOutTtl.setStatus("current")


class _NtcTsOIpOutTsPacketsInFrame_Type(Unsigned32):
    """Custom type ntcTsOIpOutTsPacketsInFrame based on Unsigned32"""
    defaultValue = 7

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 7),
    )


_NtcTsOIpOutTsPacketsInFrame_Type.__name__ = "Unsigned32"
_NtcTsOIpOutTsPacketsInFrame_Object = MibScalar
ntcTsOIpOutTsPacketsInFrame = _NtcTsOIpOutTsPacketsInFrame_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 1, 6),
    _NtcTsOIpOutTsPacketsInFrame_Type()
)
ntcTsOIpOutTsPacketsInFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpOutTsPacketsInFrame.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpOutTsPacketsInFrame.setUnits("packets")


class _NtcTsOIpOutRtpFecColumns_Type(Unsigned32):
    """Custom type ntcTsOIpOutRtpFecColumns based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NtcTsOIpOutRtpFecColumns_Type.__name__ = "Unsigned32"
_NtcTsOIpOutRtpFecColumns_Object = MibScalar
ntcTsOIpOutRtpFecColumns = _NtcTsOIpOutRtpFecColumns_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 1, 7),
    _NtcTsOIpOutRtpFecColumns_Type()
)
ntcTsOIpOutRtpFecColumns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpOutRtpFecColumns.setStatus("current")


class _NtcTsOIpOutRtpFecRows_Type(Unsigned32):
    """Custom type ntcTsOIpOutRtpFecRows based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_NtcTsOIpOutRtpFecRows_Type.__name__ = "Unsigned32"
_NtcTsOIpOutRtpFecRows_Object = MibScalar
ntcTsOIpOutRtpFecRows = _NtcTsOIpOutRtpFecRows_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 1, 8),
    _NtcTsOIpOutRtpFecRows_Type()
)
ntcTsOIpOutRtpFecRows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpOutRtpFecRows.setStatus("current")


class _NtcTsOIpOutFlushScheduleTime_Type(Unsigned32):
    """Custom type ntcTsOIpOutFlushScheduleTime based on Unsigned32"""
    defaultValue = 4000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 5000),
    )


_NtcTsOIpOutFlushScheduleTime_Type.__name__ = "Unsigned32"
_NtcTsOIpOutFlushScheduleTime_Object = MibScalar
ntcTsOIpOutFlushScheduleTime = _NtcTsOIpOutFlushScheduleTime_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 1, 9),
    _NtcTsOIpOutFlushScheduleTime_Type()
)
ntcTsOIpOutFlushScheduleTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpOutFlushScheduleTime.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpOutFlushScheduleTime.setUnits("us")
_NtcTsOIpOutMonitoring_ObjectIdentity = ObjectIdentity
ntcTsOIpOutMonitoring = _NtcTsOIpOutMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 2)
)
if mibBuilder.loadTexts:
    ntcTsOIpOutMonitoring.setStatus("current")


class _NtcTsOIpOutCounterReset_Type(Integer32):
    """Custom type ntcTsOIpOutCounterReset based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("counting", 0),
          ("reset", 1))
    )


_NtcTsOIpOutCounterReset_Type.__name__ = "Integer32"
_NtcTsOIpOutCounterReset_Object = MibScalar
ntcTsOIpOutCounterReset = _NtcTsOIpOutCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 2, 1),
    _NtcTsOIpOutCounterReset_Type()
)
ntcTsOIpOutCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpOutCounterReset.setStatus("current")
_NtcTsOIpOutBitrate_Type = Unsigned32
_NtcTsOIpOutBitrate_Object = MibScalar
ntcTsOIpOutBitrate = _NtcTsOIpOutBitrate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 2, 2),
    _NtcTsOIpOutBitrate_Type()
)
ntcTsOIpOutBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpOutBitrate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpOutBitrate.setUnits("bps")
_NtcTsOIpOutDropCount_Type = Counter32
_NtcTsOIpOutDropCount_Object = MibScalar
ntcTsOIpOutDropCount = _NtcTsOIpOutDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 2, 3),
    _NtcTsOIpOutDropCount_Type()
)
ntcTsOIpOutDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpOutDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpOutDropCount.setUnits("packets")
_NtcTsOIpOutOverflowCount_Type = Counter32
_NtcTsOIpOutOverflowCount_Object = MibScalar
ntcTsOIpOutOverflowCount = _NtcTsOIpOutOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 2, 4),
    _NtcTsOIpOutOverflowCount_Type()
)
ntcTsOIpOutOverflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpOutOverflowCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpOutOverflowCount.setUnits("packets")
_NtcTsOIpOutAlarms_ObjectIdentity = ObjectIdentity
ntcTsOIpOutAlarms = _NtcTsOIpOutAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 3)
)
if mibBuilder.loadTexts:
    ntcTsOIpOutAlarms.setStatus("current")
_NtcTsOIpOutAlNoOutput_Type = NtcAlarmState
_NtcTsOIpOutAlNoOutput_Object = MibScalar
ntcTsOIpOutAlNoOutput = _NtcTsOIpOutAlNoOutput_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 3, 1),
    _NtcTsOIpOutAlNoOutput_Type()
)
ntcTsOIpOutAlNoOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpOutAlNoOutput.setStatus("current")
_NtcTsOIpOutAlOutputOverflow_Type = NtcAlarmState
_NtcTsOIpOutAlOutputOverflow_Object = MibScalar
ntcTsOIpOutAlOutputOverflow = _NtcTsOIpOutAlOutputOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 1, 3, 2),
    _NtcTsOIpOutAlOutputOverflow_Type()
)
ntcTsOIpOutAlOutputOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpOutAlOutputOverflow.setStatus("current")
_NtcTsOIpOutConformance_ObjectIdentity = ObjectIdentity
ntcTsOIpOutConformance = _NtcTsOIpOutConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 2)
)
if mibBuilder.loadTexts:
    ntcTsOIpOutConformance.setStatus("current")
_NtcTsOIpOutConfCompliance_ObjectIdentity = ObjectIdentity
ntcTsOIpOutConfCompliance = _NtcTsOIpOutConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 2, 1)
)
if mibBuilder.loadTexts:
    ntcTsOIpOutConfCompliance.setStatus("current")
_NtcTsOIpOutConfGroup_ObjectIdentity = ObjectIdentity
ntcTsOIpOutConfGroup = _NtcTsOIpOutConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 2, 2)
)
if mibBuilder.loadTexts:
    ntcTsOIpOutConfGroup.setStatus("current")

# Managed Objects groups

ntcTsOIpOutConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 2, 2, 1)
)
ntcTsOIpOutConfGrpV1Standard.setObjects(
      *(("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutEnable"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutTsEncapProtocol"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutDestUdpPort"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutDestIpAddress"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutTtl"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutTsPacketsInFrame"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutRtpFecColumns"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutRtpFecRows"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutFlushScheduleTime"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutCounterReset"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutBitrate"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutDropCount"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutOverflowCount"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutAlNoOutput"),
        ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutAlOutputOverflow"))
)
if mibBuilder.loadTexts:
    ntcTsOIpOutConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcTsOIpOutConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8400, 2, 1, 1)
)
ntcTsOIpOutConfCompV1Standard.setObjects(
    ("NEWTEC-TSOVERIPOUT-MIB", "ntcTsOIpOutConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcTsOIpOutConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-TSOVERIPOUT-MIB",
    **{"ntcTsOverIpOut": ntcTsOverIpOut,
       "ntcTsOIpOutObjects": ntcTsOIpOutObjects,
       "ntcTsOIpOutConfiguration": ntcTsOIpOutConfiguration,
       "ntcTsOIpOutEnable": ntcTsOIpOutEnable,
       "ntcTsOIpOutTsEncapProtocol": ntcTsOIpOutTsEncapProtocol,
       "ntcTsOIpOutDestUdpPort": ntcTsOIpOutDestUdpPort,
       "ntcTsOIpOutDestIpAddress": ntcTsOIpOutDestIpAddress,
       "ntcTsOIpOutTtl": ntcTsOIpOutTtl,
       "ntcTsOIpOutTsPacketsInFrame": ntcTsOIpOutTsPacketsInFrame,
       "ntcTsOIpOutRtpFecColumns": ntcTsOIpOutRtpFecColumns,
       "ntcTsOIpOutRtpFecRows": ntcTsOIpOutRtpFecRows,
       "ntcTsOIpOutFlushScheduleTime": ntcTsOIpOutFlushScheduleTime,
       "ntcTsOIpOutMonitoring": ntcTsOIpOutMonitoring,
       "ntcTsOIpOutCounterReset": ntcTsOIpOutCounterReset,
       "ntcTsOIpOutBitrate": ntcTsOIpOutBitrate,
       "ntcTsOIpOutDropCount": ntcTsOIpOutDropCount,
       "ntcTsOIpOutOverflowCount": ntcTsOIpOutOverflowCount,
       "ntcTsOIpOutAlarms": ntcTsOIpOutAlarms,
       "ntcTsOIpOutAlNoOutput": ntcTsOIpOutAlNoOutput,
       "ntcTsOIpOutAlOutputOverflow": ntcTsOIpOutAlOutputOverflow,
       "ntcTsOIpOutConformance": ntcTsOIpOutConformance,
       "ntcTsOIpOutConfCompliance": ntcTsOIpOutConfCompliance,
       "ntcTsOIpOutConfCompV1Standard": ntcTsOIpOutConfCompV1Standard,
       "ntcTsOIpOutConfGroup": ntcTsOIpOutConfGroup,
       "ntcTsOIpOutConfGrpV1Standard": ntcTsOIpOutConfGrpV1Standard}
)
