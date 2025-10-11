# SNMP MIB module (NEWTEC-DSSOVERIPIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-DSSOVERIPIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:53 2025
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

ntcDssOverIpIn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700)
)
if mibBuilder.loadTexts:
    ntcDssOverIpIn.setRevisions(
        ("2017-07-10 12:00",
         "2015-02-19 09:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcDssOIpInObjects_ObjectIdentity = ObjectIdentity
ntcDssOIpInObjects = _NtcDssOIpInObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1)
)
if mibBuilder.loadTexts:
    ntcDssOIpInObjects.setStatus("current")


class _NtcDssOIpInEnable_Type(NtcEnable):
    """Custom type ntcDssOIpInEnable based on NtcEnable"""
    defaultValue = 0


_NtcDssOIpInEnable_Type.__name__ = "NtcEnable"
_NtcDssOIpInEnable_Object = MibScalar
ntcDssOIpInEnable = _NtcDssOIpInEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 1),
    _NtcDssOIpInEnable_Type()
)
ntcDssOIpInEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpInEnable.setStatus("current")


class _NtcDssOIpInInputSelection_Type(Integer32):
    """Custom type ntcDssOIpInInputSelection based on Integer32"""
    defaultValue = 1

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
        *(("none", 1),
          ("data1", 2),
          ("data2", 3),
          ("data", 4),
          ("any", 5))
    )


_NtcDssOIpInInputSelection_Type.__name__ = "Integer32"
_NtcDssOIpInInputSelection_Object = MibScalar
ntcDssOIpInInputSelection = _NtcDssOIpInInputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 2),
    _NtcDssOIpInInputSelection_Type()
)
ntcDssOIpInInputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpInInputSelection.setStatus("current")


class _NtcDssOIpInDssEncapProtocol_Type(Integer32):
    """Custom type ntcDssOIpInDssEncapProtocol based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("rtp", 1),
          ("rtpfec", 2))
    )


_NtcDssOIpInDssEncapProtocol_Type.__name__ = "Integer32"
_NtcDssOIpInDssEncapProtocol_Object = MibScalar
ntcDssOIpInDssEncapProtocol = _NtcDssOIpInDssEncapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 3),
    _NtcDssOIpInDssEncapProtocol_Type()
)
ntcDssOIpInDssEncapProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpInDssEncapProtocol.setStatus("current")


class _NtcDssOIpInIpAddressType_Type(Integer32):
    """Custom type ntcDssOIpInIpAddressType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("unicast", 0),
          ("multicast", 1))
    )


_NtcDssOIpInIpAddressType_Type.__name__ = "Integer32"
_NtcDssOIpInIpAddressType_Object = MibScalar
ntcDssOIpInIpAddressType = _NtcDssOIpInIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 4),
    _NtcDssOIpInIpAddressType_Type()
)
ntcDssOIpInIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpInIpAddressType.setStatus("current")


class _NtcDssOIpInMulticastAddress_Type(IpAddress):
    """Custom type ntcDssOIpInMulticastAddress based on IpAddress"""
    defaultHexValue = "e0010001"


_NtcDssOIpInMulticastAddress_Type.__name__ = "IpAddress"
_NtcDssOIpInMulticastAddress_Object = MibScalar
ntcDssOIpInMulticastAddress = _NtcDssOIpInMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 5),
    _NtcDssOIpInMulticastAddress_Type()
)
ntcDssOIpInMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpInMulticastAddress.setStatus("current")


class _NtcDssOIpInUdpPort_Type(Unsigned32):
    """Custom type ntcDssOIpInUdpPort based on Unsigned32"""
    defaultValue = 56789

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtcDssOIpInUdpPort_Type.__name__ = "Unsigned32"
_NtcDssOIpInUdpPort_Object = MibScalar
ntcDssOIpInUdpPort = _NtcDssOIpInUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 6),
    _NtcDssOIpInUdpPort_Type()
)
ntcDssOIpInUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpInUdpPort.setStatus("current")


class _NtcDssOIpInMaxBufferDelay_Type(Unsigned32):
    """Custom type ntcDssOIpInMaxBufferDelay based on Unsigned32"""
    defaultValue = 250


_NtcDssOIpInMaxBufferDelay_Type.__name__ = "Unsigned32"
_NtcDssOIpInMaxBufferDelay_Object = MibScalar
ntcDssOIpInMaxBufferDelay = _NtcDssOIpInMaxBufferDelay_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 7),
    _NtcDssOIpInMaxBufferDelay_Type()
)
ntcDssOIpInMaxBufferDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpInMaxBufferDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntcDssOIpInMaxBufferDelay.setUnits("ms")


class _NtcDssOIpInMulticastSourceA_Type(NtcNetworkAddress):
    """Custom type ntcDssOIpInMulticastSourceA based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0")


_NtcDssOIpInMulticastSourceA_Type.__name__ = "NtcNetworkAddress"
_NtcDssOIpInMulticastSourceA_Object = MibScalar
ntcDssOIpInMulticastSourceA = _NtcDssOIpInMulticastSourceA_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 8),
    _NtcDssOIpInMulticastSourceA_Type()
)
ntcDssOIpInMulticastSourceA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpInMulticastSourceA.setStatus("current")


class _NtcDssOIpInMulticastSourceB_Type(NtcNetworkAddress):
    """Custom type ntcDssOIpInMulticastSourceB based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0")


_NtcDssOIpInMulticastSourceB_Type.__name__ = "NtcNetworkAddress"
_NtcDssOIpInMulticastSourceB_Object = MibScalar
ntcDssOIpInMulticastSourceB = _NtcDssOIpInMulticastSourceB_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 9),
    _NtcDssOIpInMulticastSourceB_Type()
)
ntcDssOIpInMulticastSourceB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpInMulticastSourceB.setStatus("current")
_NtcDssOIpInMonitor_ObjectIdentity = ObjectIdentity
ntcDssOIpInMonitor = _NtcDssOIpInMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10)
)
if mibBuilder.loadTexts:
    ntcDssOIpInMonitor.setStatus("current")


class _NtcDssOIpInMonResetCounters_Type(Integer32):
    """Custom type ntcDssOIpInMonResetCounters based on Integer32"""
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


_NtcDssOIpInMonResetCounters_Type.__name__ = "Integer32"
_NtcDssOIpInMonResetCounters_Object = MibScalar
ntcDssOIpInMonResetCounters = _NtcDssOIpInMonResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10, 1),
    _NtcDssOIpInMonResetCounters_Type()
)
ntcDssOIpInMonResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcDssOIpInMonResetCounters.setStatus("current")
_NtcDssOIpInMonInputDssBitRate_Type = Unsigned32
_NtcDssOIpInMonInputDssBitRate_Object = MibScalar
ntcDssOIpInMonInputDssBitRate = _NtcDssOIpInMonInputDssBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10, 2),
    _NtcDssOIpInMonInputDssBitRate_Type()
)
ntcDssOIpInMonInputDssBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInMonInputDssBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcDssOIpInMonInputDssBitRate.setUnits("bps")
_NtcDssOIpInMonBufferDelay_Type = Unsigned32
_NtcDssOIpInMonBufferDelay_Object = MibScalar
ntcDssOIpInMonBufferDelay = _NtcDssOIpInMonBufferDelay_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10, 3),
    _NtcDssOIpInMonBufferDelay_Type()
)
ntcDssOIpInMonBufferDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInMonBufferDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntcDssOIpInMonBufferDelay.setUnits("ms")
_NtcDssOIpInMonMinBufferFilling_Type = Unsigned32
_NtcDssOIpInMonMinBufferFilling_Object = MibScalar
ntcDssOIpInMonMinBufferFilling = _NtcDssOIpInMonMinBufferFilling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10, 4),
    _NtcDssOIpInMonMinBufferFilling_Type()
)
ntcDssOIpInMonMinBufferFilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInMonMinBufferFilling.setStatus("current")
if mibBuilder.loadTexts:
    ntcDssOIpInMonMinBufferFilling.setUnits("ms")
_NtcDssOIpInMonMaxBufferFilling_Type = Unsigned32
_NtcDssOIpInMonMaxBufferFilling_Object = MibScalar
ntcDssOIpInMonMaxBufferFilling = _NtcDssOIpInMonMaxBufferFilling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10, 5),
    _NtcDssOIpInMonMaxBufferFilling_Type()
)
ntcDssOIpInMonMaxBufferFilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInMonMaxBufferFilling.setStatus("current")
if mibBuilder.loadTexts:
    ntcDssOIpInMonMaxBufferFilling.setUnits("ms")


class _NtcDssOIpInMonSourceInfo_Type(DisplayString):
    """Custom type ntcDssOIpInMonSourceInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcDssOIpInMonSourceInfo_Type.__name__ = "DisplayString"
_NtcDssOIpInMonSourceInfo_Object = MibScalar
ntcDssOIpInMonSourceInfo = _NtcDssOIpInMonSourceInfo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10, 6),
    _NtcDssOIpInMonSourceInfo_Type()
)
ntcDssOIpInMonSourceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInMonSourceInfo.setStatus("current")


class _NtcDssOIpInMonRtpFecScheme_Type(DisplayString):
    """Custom type ntcDssOIpInMonRtpFecScheme based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcDssOIpInMonRtpFecScheme_Type.__name__ = "DisplayString"
_NtcDssOIpInMonRtpFecScheme_Object = MibScalar
ntcDssOIpInMonRtpFecScheme = _NtcDssOIpInMonRtpFecScheme_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10, 7),
    _NtcDssOIpInMonRtpFecScheme_Type()
)
ntcDssOIpInMonRtpFecScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInMonRtpFecScheme.setStatus("current")
_NtcDssOIpInMonRtpDropCount_Type = Counter32
_NtcDssOIpInMonRtpDropCount_Object = MibScalar
ntcDssOIpInMonRtpDropCount = _NtcDssOIpInMonRtpDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10, 8),
    _NtcDssOIpInMonRtpDropCount_Type()
)
ntcDssOIpInMonRtpDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInMonRtpDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcDssOIpInMonRtpDropCount.setUnits("packets")
_NtcDssOIpInMonRtpRepairCount_Type = Counter32
_NtcDssOIpInMonRtpRepairCount_Object = MibScalar
ntcDssOIpInMonRtpRepairCount = _NtcDssOIpInMonRtpRepairCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10, 9),
    _NtcDssOIpInMonRtpRepairCount_Type()
)
ntcDssOIpInMonRtpRepairCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInMonRtpRepairCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcDssOIpInMonRtpRepairCount.setUnits("packets")
_NtcDssOIpInMonRtpFecDropCount_Type = Counter32
_NtcDssOIpInMonRtpFecDropCount_Object = MibScalar
ntcDssOIpInMonRtpFecDropCount = _NtcDssOIpInMonRtpFecDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 10, 10),
    _NtcDssOIpInMonRtpFecDropCount_Type()
)
ntcDssOIpInMonRtpFecDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInMonRtpFecDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcDssOIpInMonRtpFecDropCount.setUnits("packets")
_NtcDssOIpInAlarm_ObjectIdentity = ObjectIdentity
ntcDssOIpInAlarm = _NtcDssOIpInAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 11)
)
if mibBuilder.loadTexts:
    ntcDssOIpInAlarm.setStatus("current")
_NtcDssOIpInAlmNoInputData_Type = NtcAlarmState
_NtcDssOIpInAlmNoInputData_Object = MibScalar
ntcDssOIpInAlmNoInputData = _NtcDssOIpInAlmNoInputData_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 11, 1),
    _NtcDssOIpInAlmNoInputData_Type()
)
ntcDssOIpInAlmNoInputData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInAlmNoInputData.setStatus("current")
_NtcDssOIpInAlmBufferOverflow_Type = NtcAlarmState
_NtcDssOIpInAlmBufferOverflow_Object = MibScalar
ntcDssOIpInAlmBufferOverflow = _NtcDssOIpInAlmBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 11, 2),
    _NtcDssOIpInAlmBufferOverflow_Type()
)
ntcDssOIpInAlmBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInAlmBufferOverflow.setStatus("current")
_NtcDssOIpInAlmBufferUnflow_Type = NtcAlarmState
_NtcDssOIpInAlmBufferUnflow_Object = MibScalar
ntcDssOIpInAlmBufferUnflow = _NtcDssOIpInAlmBufferUnflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 11, 3),
    _NtcDssOIpInAlmBufferUnflow_Type()
)
ntcDssOIpInAlmBufferUnflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInAlmBufferUnflow.setStatus("current")
_NtcDssOIpInAlmRtpNoSync_Type = NtcAlarmState
_NtcDssOIpInAlmRtpNoSync_Object = MibScalar
ntcDssOIpInAlmRtpNoSync = _NtcDssOIpInAlmRtpNoSync_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 1, 11, 4),
    _NtcDssOIpInAlmRtpNoSync_Type()
)
ntcDssOIpInAlmRtpNoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcDssOIpInAlmRtpNoSync.setStatus("current")
_NtcDssOIpInConformance_ObjectIdentity = ObjectIdentity
ntcDssOIpInConformance = _NtcDssOIpInConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 2)
)
if mibBuilder.loadTexts:
    ntcDssOIpInConformance.setStatus("current")
_NtcDssOIpInConfCompliance_ObjectIdentity = ObjectIdentity
ntcDssOIpInConfCompliance = _NtcDssOIpInConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 2, 1)
)
if mibBuilder.loadTexts:
    ntcDssOIpInConfCompliance.setStatus("current")
_NtcDssOIpInConfGroup_ObjectIdentity = ObjectIdentity
ntcDssOIpInConfGroup = _NtcDssOIpInConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 2, 2)
)
if mibBuilder.loadTexts:
    ntcDssOIpInConfGroup.setStatus("current")

# Managed Objects groups

ntcDssOIpInConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 2, 2, 1)
)
ntcDssOIpInConfGrpV1Standard.setObjects(
      *(("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInEnable"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInInputSelection"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInDssEncapProtocol"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInIpAddressType"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMulticastAddress"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInUdpPort"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMaxBufferDelay"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMulticastSourceA"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMulticastSourceB"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMonResetCounters"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMonInputDssBitRate"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMonBufferDelay"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMonMinBufferFilling"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMonMaxBufferFilling"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMonSourceInfo"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMonRtpFecScheme"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMonRtpDropCount"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMonRtpRepairCount"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInMonRtpFecDropCount"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInAlmNoInputData"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInAlmBufferOverflow"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInAlmBufferUnflow"),
        ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInAlmRtpNoSync"))
)
if mibBuilder.loadTexts:
    ntcDssOIpInConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcDssOIpInConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 8700, 2, 1, 1)
)
ntcDssOIpInConfCompV1Standard.setObjects(
    ("NEWTEC-DSSOVERIPIN-MIB", "ntcDssOIpInConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcDssOIpInConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-DSSOVERIPIN-MIB",
    **{"ntcDssOverIpIn": ntcDssOverIpIn,
       "ntcDssOIpInObjects": ntcDssOIpInObjects,
       "ntcDssOIpInEnable": ntcDssOIpInEnable,
       "ntcDssOIpInInputSelection": ntcDssOIpInInputSelection,
       "ntcDssOIpInDssEncapProtocol": ntcDssOIpInDssEncapProtocol,
       "ntcDssOIpInIpAddressType": ntcDssOIpInIpAddressType,
       "ntcDssOIpInMulticastAddress": ntcDssOIpInMulticastAddress,
       "ntcDssOIpInUdpPort": ntcDssOIpInUdpPort,
       "ntcDssOIpInMaxBufferDelay": ntcDssOIpInMaxBufferDelay,
       "ntcDssOIpInMulticastSourceA": ntcDssOIpInMulticastSourceA,
       "ntcDssOIpInMulticastSourceB": ntcDssOIpInMulticastSourceB,
       "ntcDssOIpInMonitor": ntcDssOIpInMonitor,
       "ntcDssOIpInMonResetCounters": ntcDssOIpInMonResetCounters,
       "ntcDssOIpInMonInputDssBitRate": ntcDssOIpInMonInputDssBitRate,
       "ntcDssOIpInMonBufferDelay": ntcDssOIpInMonBufferDelay,
       "ntcDssOIpInMonMinBufferFilling": ntcDssOIpInMonMinBufferFilling,
       "ntcDssOIpInMonMaxBufferFilling": ntcDssOIpInMonMaxBufferFilling,
       "ntcDssOIpInMonSourceInfo": ntcDssOIpInMonSourceInfo,
       "ntcDssOIpInMonRtpFecScheme": ntcDssOIpInMonRtpFecScheme,
       "ntcDssOIpInMonRtpDropCount": ntcDssOIpInMonRtpDropCount,
       "ntcDssOIpInMonRtpRepairCount": ntcDssOIpInMonRtpRepairCount,
       "ntcDssOIpInMonRtpFecDropCount": ntcDssOIpInMonRtpFecDropCount,
       "ntcDssOIpInAlarm": ntcDssOIpInAlarm,
       "ntcDssOIpInAlmNoInputData": ntcDssOIpInAlmNoInputData,
       "ntcDssOIpInAlmBufferOverflow": ntcDssOIpInAlmBufferOverflow,
       "ntcDssOIpInAlmBufferUnflow": ntcDssOIpInAlmBufferUnflow,
       "ntcDssOIpInAlmRtpNoSync": ntcDssOIpInAlmRtpNoSync,
       "ntcDssOIpInConformance": ntcDssOIpInConformance,
       "ntcDssOIpInConfCompliance": ntcDssOIpInConfCompliance,
       "ntcDssOIpInConfCompV1Standard": ntcDssOIpInConfCompV1Standard,
       "ntcDssOIpInConfGroup": ntcDssOIpInConfGroup,
       "ntcDssOIpInConfGrpV1Standard": ntcDssOIpInConfGrpV1Standard}
)
