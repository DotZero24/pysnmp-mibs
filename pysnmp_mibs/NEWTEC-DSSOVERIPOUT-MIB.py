# SNMP MIB module (NEWTEC-DSSOVERIPOUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-DSSOVERIPOUT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:48 2025
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

ntcDssOverIpOut = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300)
)
if mibBuilder.loadTexts:
    ntcDssOverIpOut.setRevisions(
        ("2017-07-10 12:00",
         "2016-02-02 07:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcDssOIpOutObjects_ObjectIdentity = ObjectIdentity
ntcDssOIpOutObjects = _NtcDssOIpOutObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1)
)
if mibBuilder.loadTexts:
    ntcDssOIpOutObjects.setStatus("current")
_NtcDssOIpOutConfiguration_ObjectIdentity = ObjectIdentity
ntcDssOIpOutConfiguration = _NtcDssOIpOutConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 1)
)
if mibBuilder.loadTexts:
    ntcDssOIpOutConfiguration.setStatus("current")


class _NtcDssOIpOutEnable_Type(NtcEnable):
    """Custom type ntcDssOIpOutEnable based on NtcEnable"""
    defaultValue = 0


_NtcDssOIpOutEnable_Type.__name__ = "NtcEnable"
_NtcDssOIpOutEnable_Object = MibScalar
ntcDssOIpOutEnable = _NtcDssOIpOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 1, 1),
    _NtcDssOIpOutEnable_Type()
)
ntcDssOIpOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpOutEnable.setStatus("current")


class _NtcDssOIpOutDssEncapProtocol_Type(Integer32):
    """Custom type ntcDssOIpOutDssEncapProtocol based on Integer32"""
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


_NtcDssOIpOutDssEncapProtocol_Type.__name__ = "Integer32"
_NtcDssOIpOutDssEncapProtocol_Object = MibScalar
ntcDssOIpOutDssEncapProtocol = _NtcDssOIpOutDssEncapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 1, 2),
    _NtcDssOIpOutDssEncapProtocol_Type()
)
ntcDssOIpOutDssEncapProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpOutDssEncapProtocol.setStatus("current")


class _NtcDssOIpOutDestUdpPort_Type(Unsigned32):
    """Custom type ntcDssOIpOutDestUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtcDssOIpOutDestUdpPort_Type.__name__ = "Unsigned32"
_NtcDssOIpOutDestUdpPort_Object = MibScalar
ntcDssOIpOutDestUdpPort = _NtcDssOIpOutDestUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 1, 3),
    _NtcDssOIpOutDestUdpPort_Type()
)
ntcDssOIpOutDestUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpOutDestUdpPort.setStatus("current")


class _NtcDssOIpOutDestIpAddress_Type(NtcNetworkAddress):
    """Custom type ntcDssOIpOutDestIpAddress based on NtcNetworkAddress"""
    defaultValue = OctetString("10.0.0.1")


_NtcDssOIpOutDestIpAddress_Type.__name__ = "NtcNetworkAddress"
_NtcDssOIpOutDestIpAddress_Object = MibScalar
ntcDssOIpOutDestIpAddress = _NtcDssOIpOutDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 1, 4),
    _NtcDssOIpOutDestIpAddress_Type()
)
ntcDssOIpOutDestIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpOutDestIpAddress.setStatus("current")


class _NtcDssOIpOutTtl_Type(Unsigned32):
    """Custom type ntcDssOIpOutTtl based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_NtcDssOIpOutTtl_Type.__name__ = "Unsigned32"
_NtcDssOIpOutTtl_Object = MibScalar
ntcDssOIpOutTtl = _NtcDssOIpOutTtl_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 1, 5),
    _NtcDssOIpOutTtl_Type()
)
ntcDssOIpOutTtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpOutTtl.setStatus("current")


class _NtcDssOIpOutDssPacketsInFrame_Type(Unsigned32):
    """Custom type ntcDssOIpOutDssPacketsInFrame based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_NtcDssOIpOutDssPacketsInFrame_Type.__name__ = "Unsigned32"
_NtcDssOIpOutDssPacketsInFrame_Object = MibScalar
ntcDssOIpOutDssPacketsInFrame = _NtcDssOIpOutDssPacketsInFrame_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 1, 6),
    _NtcDssOIpOutDssPacketsInFrame_Type()
)
ntcDssOIpOutDssPacketsInFrame.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpOutDssPacketsInFrame.setStatus("current")
if mibBuilder.loadTexts:
    ntcDssOIpOutDssPacketsInFrame.setUnits("packets")


class _NtcDssOIpOutRtpFecColumns_Type(Unsigned32):
    """Custom type ntcDssOIpOutRtpFecColumns based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 20),
    )


_NtcDssOIpOutRtpFecColumns_Type.__name__ = "Unsigned32"
_NtcDssOIpOutRtpFecColumns_Object = MibScalar
ntcDssOIpOutRtpFecColumns = _NtcDssOIpOutRtpFecColumns_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 1, 7),
    _NtcDssOIpOutRtpFecColumns_Type()
)
ntcDssOIpOutRtpFecColumns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpOutRtpFecColumns.setStatus("current")


class _NtcDssOIpOutRtpFecRows_Type(Unsigned32):
    """Custom type ntcDssOIpOutRtpFecRows based on Unsigned32"""
    defaultValue = 10

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(4, 20),
    )


_NtcDssOIpOutRtpFecRows_Type.__name__ = "Unsigned32"
_NtcDssOIpOutRtpFecRows_Object = MibScalar
ntcDssOIpOutRtpFecRows = _NtcDssOIpOutRtpFecRows_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 1, 8),
    _NtcDssOIpOutRtpFecRows_Type()
)
ntcDssOIpOutRtpFecRows.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpOutRtpFecRows.setStatus("current")
_NtcDssOIpOutMonitoring_ObjectIdentity = ObjectIdentity
ntcDssOIpOutMonitoring = _NtcDssOIpOutMonitoring_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 2)
)
if mibBuilder.loadTexts:
    ntcDssOIpOutMonitoring.setStatus("current")


class _NtcDssOIpOutCounterReset_Type(Integer32):
    """Custom type ntcDssOIpOutCounterReset based on Integer32"""
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


_NtcDssOIpOutCounterReset_Type.__name__ = "Integer32"
_NtcDssOIpOutCounterReset_Object = MibScalar
ntcDssOIpOutCounterReset = _NtcDssOIpOutCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 2, 1),
    _NtcDssOIpOutCounterReset_Type()
)
ntcDssOIpOutCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpOutCounterReset.setStatus("current")
_NtcDssOIpOutBitrate_Type = Unsigned32
_NtcDssOIpOutBitrate_Object = MibScalar
ntcDssOIpOutBitrate = _NtcDssOIpOutBitrate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 2, 2),
    _NtcDssOIpOutBitrate_Type()
)
ntcDssOIpOutBitrate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpOutBitrate.setStatus("current")
if mibBuilder.loadTexts:
    ntcDssOIpOutBitrate.setUnits("bps")
_NtcDssOIpOutAlarms_ObjectIdentity = ObjectIdentity
ntcDssOIpOutAlarms = _NtcDssOIpOutAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 3)
)
if mibBuilder.loadTexts:
    ntcDssOIpOutAlarms.setStatus("current")
_NtcDssOIpOutAlNoOutput_Type = NtcAlarmState
_NtcDssOIpOutAlNoOutput_Object = MibScalar
ntcDssOIpOutAlNoOutput = _NtcDssOIpOutAlNoOutput_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 3, 1),
    _NtcDssOIpOutAlNoOutput_Type()
)
ntcDssOIpOutAlNoOutput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpOutAlNoOutput.setStatus("current")
_NtcDssOIpOutAlOutputOverflow_Type = NtcAlarmState
_NtcDssOIpOutAlOutputOverflow_Object = MibScalar
ntcDssOIpOutAlOutputOverflow = _NtcDssOIpOutAlOutputOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 1, 3, 2),
    _NtcDssOIpOutAlOutputOverflow_Type()
)
ntcDssOIpOutAlOutputOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpOutAlOutputOverflow.setStatus("current")
_NtcDssOIpOutConformance_ObjectIdentity = ObjectIdentity
ntcDssOIpOutConformance = _NtcDssOIpOutConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 2)
)
if mibBuilder.loadTexts:
    ntcDssOIpOutConformance.setStatus("current")
_NtcDssOIpOutConfCompliance_ObjectIdentity = ObjectIdentity
ntcDssOIpOutConfCompliance = _NtcDssOIpOutConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 2, 1)
)
if mibBuilder.loadTexts:
    ntcDssOIpOutConfCompliance.setStatus("current")
_NtcDssOIpOutConfGroup_ObjectIdentity = ObjectIdentity
ntcDssOIpOutConfGroup = _NtcDssOIpOutConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 2, 2)
)
if mibBuilder.loadTexts:
    ntcDssOIpOutConfGroup.setStatus("current")

# Managed Objects groups

ntcDssOIpOutConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 2, 2, 1)
)
ntcDssOIpOutConfGrpV1Standard.setObjects(
      *(("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutEnable"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutDssEncapProtocol"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutDestUdpPort"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutDestIpAddress"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutTtl"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutDssPacketsInFrame"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutRtpFecColumns"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutRtpFecRows"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutCounterReset"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutBitrate"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutAlNoOutput"),
        ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutAlOutputOverflow"))
)
if mibBuilder.loadTexts:
    ntcDssOIpOutConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcDssOIpOutConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9300, 2, 1, 1)
)
ntcDssOIpOutConfCompV1Standard.setObjects(
    ("NEWTEC-DSSOVERIPOUT-MIB", "ntcDssOIpOutConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcDssOIpOutConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-DSSOVERIPOUT-MIB",
    **{"ntcDssOverIpOut": ntcDssOverIpOut,
       "ntcDssOIpOutObjects": ntcDssOIpOutObjects,
       "ntcDssOIpOutConfiguration": ntcDssOIpOutConfiguration,
       "ntcDssOIpOutEnable": ntcDssOIpOutEnable,
       "ntcDssOIpOutDssEncapProtocol": ntcDssOIpOutDssEncapProtocol,
       "ntcDssOIpOutDestUdpPort": ntcDssOIpOutDestUdpPort,
       "ntcDssOIpOutDestIpAddress": ntcDssOIpOutDestIpAddress,
       "ntcDssOIpOutTtl": ntcDssOIpOutTtl,
       "ntcDssOIpOutDssPacketsInFrame": ntcDssOIpOutDssPacketsInFrame,
       "ntcDssOIpOutRtpFecColumns": ntcDssOIpOutRtpFecColumns,
       "ntcDssOIpOutRtpFecRows": ntcDssOIpOutRtpFecRows,
       "ntcDssOIpOutMonitoring": ntcDssOIpOutMonitoring,
       "ntcDssOIpOutCounterReset": ntcDssOIpOutCounterReset,
       "ntcDssOIpOutBitrate": ntcDssOIpOutBitrate,
       "ntcDssOIpOutAlarms": ntcDssOIpOutAlarms,
       "ntcDssOIpOutAlNoOutput": ntcDssOIpOutAlNoOutput,
       "ntcDssOIpOutAlOutputOverflow": ntcDssOIpOutAlOutputOverflow,
       "ntcDssOIpOutConformance": ntcDssOIpOutConformance,
       "ntcDssOIpOutConfCompliance": ntcDssOIpOutConfCompliance,
       "ntcDssOIpOutConfCompV1Standard": ntcDssOIpOutConfCompV1Standard,
       "ntcDssOIpOutConfGroup": ntcDssOIpOutConfGroup,
       "ntcDssOIpOutConfGrpV1Standard": ntcDssOIpOutConfGrpV1Standard}
)
