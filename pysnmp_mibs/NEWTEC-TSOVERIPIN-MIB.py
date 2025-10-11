# SNMP MIB module (NEWTEC-TSOVERIPIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-TSOVERIPIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:57 2025
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

ntcTsOverIpIn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600)
)
if mibBuilder.loadTexts:
    ntcTsOverIpIn.setRevisions(
        ("2017-07-10 12:00",
         "2016-02-02 07:00",
         "2015-02-19 09:00",
         "2014-09-09 09:00",
         "2013-03-27 10:00",
         "2012-06-28 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcTsOIpInObjects_ObjectIdentity = ObjectIdentity
ntcTsOIpInObjects = _NtcTsOIpInObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1)
)
if mibBuilder.loadTexts:
    ntcTsOIpInObjects.setStatus("current")


class _NtcTsOIpInEnable_Type(NtcEnable):
    """Custom type ntcTsOIpInEnable based on NtcEnable"""
    defaultValue = 0


_NtcTsOIpInEnable_Type.__name__ = "NtcEnable"
_NtcTsOIpInEnable_Object = MibScalar
ntcTsOIpInEnable = _NtcTsOIpInEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 1),
    _NtcTsOIpInEnable_Type()
)
ntcTsOIpInEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInEnable.setStatus("current")


class _NtcTsOIpInInputSelection_Type(Integer32):
    """Custom type ntcTsOIpInInputSelection based on Integer32"""
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


_NtcTsOIpInInputSelection_Type.__name__ = "Integer32"
_NtcTsOIpInInputSelection_Object = MibScalar
ntcTsOIpInInputSelection = _NtcTsOIpInInputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 2),
    _NtcTsOIpInInputSelection_Type()
)
ntcTsOIpInInputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInInputSelection.setStatus("current")


class _NtcTsOIpInTsEncapProtocol_Type(Integer32):
    """Custom type ntcTsOIpInTsEncapProtocol based on Integer32"""
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


_NtcTsOIpInTsEncapProtocol_Type.__name__ = "Integer32"
_NtcTsOIpInTsEncapProtocol_Object = MibScalar
ntcTsOIpInTsEncapProtocol = _NtcTsOIpInTsEncapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 3),
    _NtcTsOIpInTsEncapProtocol_Type()
)
ntcTsOIpInTsEncapProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInTsEncapProtocol.setStatus("current")


class _NtcTsOIpInIpAddressType_Type(Integer32):
    """Custom type ntcTsOIpInIpAddressType based on Integer32"""
    defaultValue = 0

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


_NtcTsOIpInIpAddressType_Type.__name__ = "Integer32"
_NtcTsOIpInIpAddressType_Object = MibScalar
ntcTsOIpInIpAddressType = _NtcTsOIpInIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 4),
    _NtcTsOIpInIpAddressType_Type()
)
ntcTsOIpInIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInIpAddressType.setStatus("current")


class _NtcTsOIpInMulticastAddress_Type(IpAddress):
    """Custom type ntcTsOIpInMulticastAddress based on IpAddress"""
    defaultHexValue = "e0010001"


_NtcTsOIpInMulticastAddress_Type.__name__ = "IpAddress"
_NtcTsOIpInMulticastAddress_Object = MibScalar
ntcTsOIpInMulticastAddress = _NtcTsOIpInMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 5),
    _NtcTsOIpInMulticastAddress_Type()
)
ntcTsOIpInMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInMulticastAddress.setStatus("current")


class _NtcTsOIpInUdpPort_Type(Unsigned32):
    """Custom type ntcTsOIpInUdpPort based on Unsigned32"""
    defaultValue = 56789

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtcTsOIpInUdpPort_Type.__name__ = "Unsigned32"
_NtcTsOIpInUdpPort_Object = MibScalar
ntcTsOIpInUdpPort = _NtcTsOIpInUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 6),
    _NtcTsOIpInUdpPort_Type()
)
ntcTsOIpInUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInUdpPort.setStatus("current")


class _NtcTsOIpInTrafficProfile_Type(Integer32):
    """Custom type ntcTsOIpInTrafficProfile based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("vbr", 0),
          ("cbr", 1))
    )


_NtcTsOIpInTrafficProfile_Type.__name__ = "Integer32"
_NtcTsOIpInTrafficProfile_Object = MibScalar
ntcTsOIpInTrafficProfile = _NtcTsOIpInTrafficProfile_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 7),
    _NtcTsOIpInTrafficProfile_Type()
)
ntcTsOIpInTrafficProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInTrafficProfile.setStatus("current")


class _NtcTsOIpInMaxTrafficJitter_Type(Unsigned32):
    """Custom type ntcTsOIpInMaxTrafficJitter based on Unsigned32"""
    defaultValue = 50


_NtcTsOIpInMaxTrafficJitter_Type.__name__ = "Unsigned32"
_NtcTsOIpInMaxTrafficJitter_Object = MibScalar
ntcTsOIpInMaxTrafficJitter = _NtcTsOIpInMaxTrafficJitter_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 8),
    _NtcTsOIpInMaxTrafficJitter_Type()
)
ntcTsOIpInMaxTrafficJitter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInMaxTrafficJitter.setStatus("deprecated")
if mibBuilder.loadTexts:
    ntcTsOIpInMaxTrafficJitter.setUnits("ms")


class _NtcTsOIpInMaxBufferDelay_Type(Unsigned32):
    """Custom type ntcTsOIpInMaxBufferDelay based on Unsigned32"""
    defaultValue = 250


_NtcTsOIpInMaxBufferDelay_Type.__name__ = "Unsigned32"
_NtcTsOIpInMaxBufferDelay_Object = MibScalar
ntcTsOIpInMaxBufferDelay = _NtcTsOIpInMaxBufferDelay_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 9),
    _NtcTsOIpInMaxBufferDelay_Type()
)
ntcTsOIpInMaxBufferDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInMaxBufferDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMaxBufferDelay.setUnits("ms")


class _NtcTsOIpInInputTsBitRate_Type(Unsigned32):
    """Custom type ntcTsOIpInInputTsBitRate based on Unsigned32"""
    defaultValue = 1000000


_NtcTsOIpInInputTsBitRate_Type.__name__ = "Unsigned32"
_NtcTsOIpInInputTsBitRate_Object = MibScalar
ntcTsOIpInInputTsBitRate = _NtcTsOIpInInputTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 10),
    _NtcTsOIpInInputTsBitRate_Type()
)
ntcTsOIpInInputTsBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInInputTsBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInInputTsBitRate.setUnits("bps")
_NtcTsOIpInMonitor_ObjectIdentity = ObjectIdentity
ntcTsOIpInMonitor = _NtcTsOIpInMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11)
)
if mibBuilder.loadTexts:
    ntcTsOIpInMonitor.setStatus("current")


class _NtcTsOIpInMonResetCounters_Type(Integer32):
    """Custom type ntcTsOIpInMonResetCounters based on Integer32"""
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


_NtcTsOIpInMonResetCounters_Type.__name__ = "Integer32"
_NtcTsOIpInMonResetCounters_Object = MibScalar
ntcTsOIpInMonResetCounters = _NtcTsOIpInMonResetCounters_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 1),
    _NtcTsOIpInMonResetCounters_Type()
)
ntcTsOIpInMonResetCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInMonResetCounters.setStatus("current")
_NtcTsOIpInMonInputTsBitRate_Type = Unsigned32
_NtcTsOIpInMonInputTsBitRate_Object = MibScalar
ntcTsOIpInMonInputTsBitRate = _NtcTsOIpInMonInputTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 2),
    _NtcTsOIpInMonInputTsBitRate_Type()
)
ntcTsOIpInMonInputTsBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonInputTsBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonInputTsBitRate.setUnits("bps")
_NtcTsOIpInMonBufferDelay_Type = Unsigned32
_NtcTsOIpInMonBufferDelay_Object = MibScalar
ntcTsOIpInMonBufferDelay = _NtcTsOIpInMonBufferDelay_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 3),
    _NtcTsOIpInMonBufferDelay_Type()
)
ntcTsOIpInMonBufferDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonBufferDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonBufferDelay.setUnits("ms")
_NtcTsOIpInMonMinBufferFilling_Type = Unsigned32
_NtcTsOIpInMonMinBufferFilling_Object = MibScalar
ntcTsOIpInMonMinBufferFilling = _NtcTsOIpInMonMinBufferFilling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 4),
    _NtcTsOIpInMonMinBufferFilling_Type()
)
ntcTsOIpInMonMinBufferFilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonMinBufferFilling.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonMinBufferFilling.setUnits("ms")
_NtcTsOIpInMonMaxBufferFilling_Type = Unsigned32
_NtcTsOIpInMonMaxBufferFilling_Object = MibScalar
ntcTsOIpInMonMaxBufferFilling = _NtcTsOIpInMonMaxBufferFilling_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 5),
    _NtcTsOIpInMonMaxBufferFilling_Type()
)
ntcTsOIpInMonMaxBufferFilling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonMaxBufferFilling.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonMaxBufferFilling.setUnits("ms")


class _NtcTsOIpInMonSourceInfo_Type(DisplayString):
    """Custom type ntcTsOIpInMonSourceInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcTsOIpInMonSourceInfo_Type.__name__ = "DisplayString"
_NtcTsOIpInMonSourceInfo_Object = MibScalar
ntcTsOIpInMonSourceInfo = _NtcTsOIpInMonSourceInfo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 6),
    _NtcTsOIpInMonSourceInfo_Type()
)
ntcTsOIpInMonSourceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonSourceInfo.setStatus("current")


class _NtcTsOIpInMonRtpFecScheme_Type(DisplayString):
    """Custom type ntcTsOIpInMonRtpFecScheme based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcTsOIpInMonRtpFecScheme_Type.__name__ = "DisplayString"
_NtcTsOIpInMonRtpFecScheme_Object = MibScalar
ntcTsOIpInMonRtpFecScheme = _NtcTsOIpInMonRtpFecScheme_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 7),
    _NtcTsOIpInMonRtpFecScheme_Type()
)
ntcTsOIpInMonRtpFecScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpFecScheme.setStatus("current")
_NtcTsOIpInMonTsInCount_Type = Counter32
_NtcTsOIpInMonTsInCount_Object = MibScalar
ntcTsOIpInMonTsInCount = _NtcTsOIpInMonTsInCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 8),
    _NtcTsOIpInMonTsInCount_Type()
)
ntcTsOIpInMonTsInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonTsInCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonTsInCount.setUnits("packets")
_NtcTsOIpInMonRtpInCount_Type = Counter32
_NtcTsOIpInMonRtpInCount_Object = MibScalar
ntcTsOIpInMonRtpInCount = _NtcTsOIpInMonRtpInCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 9),
    _NtcTsOIpInMonRtpInCount_Type()
)
ntcTsOIpInMonRtpInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpInCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpInCount.setUnits("packets")
_NtcTsOIpInMonRtpColumnFecInCount_Type = Counter32
_NtcTsOIpInMonRtpColumnFecInCount_Object = MibScalar
ntcTsOIpInMonRtpColumnFecInCount = _NtcTsOIpInMonRtpColumnFecInCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 10),
    _NtcTsOIpInMonRtpColumnFecInCount_Type()
)
ntcTsOIpInMonRtpColumnFecInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpColumnFecInCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpColumnFecInCount.setUnits("packets")
_NtcTsOIpInMonRtpRowFecInCount_Type = Counter32
_NtcTsOIpInMonRtpRowFecInCount_Object = MibScalar
ntcTsOIpInMonRtpRowFecInCount = _NtcTsOIpInMonRtpRowFecInCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 11),
    _NtcTsOIpInMonRtpRowFecInCount_Type()
)
ntcTsOIpInMonRtpRowFecInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpRowFecInCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpRowFecInCount.setUnits("packets")
_NtcTsOIpInMonTsOutCount_Type = Counter32
_NtcTsOIpInMonTsOutCount_Object = MibScalar
ntcTsOIpInMonTsOutCount = _NtcTsOIpInMonTsOutCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 12),
    _NtcTsOIpInMonTsOutCount_Type()
)
ntcTsOIpInMonTsOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonTsOutCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonTsOutCount.setUnits("packets")
_NtcTsOIpInMonTsDropCount_Type = Counter32
_NtcTsOIpInMonTsDropCount_Object = MibScalar
ntcTsOIpInMonTsDropCount = _NtcTsOIpInMonTsDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 13),
    _NtcTsOIpInMonTsDropCount_Type()
)
ntcTsOIpInMonTsDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonTsDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonTsDropCount.setUnits("packets")
_NtcTsOIpInMonTsOverflowCount_Type = Counter32
_NtcTsOIpInMonTsOverflowCount_Object = MibScalar
ntcTsOIpInMonTsOverflowCount = _NtcTsOIpInMonTsOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 14),
    _NtcTsOIpInMonTsOverflowCount_Type()
)
ntcTsOIpInMonTsOverflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonTsOverflowCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonTsOverflowCount.setUnits("packets")
_NtcTsOIpInMonRtpDropCount_Type = Counter32
_NtcTsOIpInMonRtpDropCount_Object = MibScalar
ntcTsOIpInMonRtpDropCount = _NtcTsOIpInMonRtpDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 15),
    _NtcTsOIpInMonRtpDropCount_Type()
)
ntcTsOIpInMonRtpDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpDropCount.setUnits("packets")
_NtcTsOIpInMonRtpRepairCount_Type = Counter32
_NtcTsOIpInMonRtpRepairCount_Object = MibScalar
ntcTsOIpInMonRtpRepairCount = _NtcTsOIpInMonRtpRepairCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 16),
    _NtcTsOIpInMonRtpRepairCount_Type()
)
ntcTsOIpInMonRtpRepairCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpRepairCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpRepairCount.setUnits("packets")
_NtcTsOIpInMonRtpFecDropCount_Type = Counter32
_NtcTsOIpInMonRtpFecDropCount_Object = MibScalar
ntcTsOIpInMonRtpFecDropCount = _NtcTsOIpInMonRtpFecDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 17),
    _NtcTsOIpInMonRtpFecDropCount_Type()
)
ntcTsOIpInMonRtpFecDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpFecDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcTsOIpInMonRtpFecDropCount.setUnits("packets")


class _NtcTsOIpInMonActivePCRPID_Type(Unsigned32):
    """Custom type ntcTsOIpInMonActivePCRPID based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8190),
    )


_NtcTsOIpInMonActivePCRPID_Type.__name__ = "Unsigned32"
_NtcTsOIpInMonActivePCRPID_Object = MibScalar
ntcTsOIpInMonActivePCRPID = _NtcTsOIpInMonActivePCRPID_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 11, 18),
    _NtcTsOIpInMonActivePCRPID_Type()
)
ntcTsOIpInMonActivePCRPID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInMonActivePCRPID.setStatus("current")
_NtcTsOIpInAlarm_ObjectIdentity = ObjectIdentity
ntcTsOIpInAlarm = _NtcTsOIpInAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 12)
)
if mibBuilder.loadTexts:
    ntcTsOIpInAlarm.setStatus("current")
_NtcTsOIpInAlmGeneralTsOverIpIn_Type = NtcAlarmState
_NtcTsOIpInAlmGeneralTsOverIpIn_Object = MibScalar
ntcTsOIpInAlmGeneralTsOverIpIn = _NtcTsOIpInAlmGeneralTsOverIpIn_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 12, 1),
    _NtcTsOIpInAlmGeneralTsOverIpIn_Type()
)
ntcTsOIpInAlmGeneralTsOverIpIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInAlmGeneralTsOverIpIn.setStatus("current")
_NtcTsOIpInAlmNoInputData_Type = NtcAlarmState
_NtcTsOIpInAlmNoInputData_Object = MibScalar
ntcTsOIpInAlmNoInputData = _NtcTsOIpInAlmNoInputData_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 12, 2),
    _NtcTsOIpInAlmNoInputData_Type()
)
ntcTsOIpInAlmNoInputData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInAlmNoInputData.setStatus("current")
_NtcTsOIpInAlmBufferOverflow_Type = NtcAlarmState
_NtcTsOIpInAlmBufferOverflow_Object = MibScalar
ntcTsOIpInAlmBufferOverflow = _NtcTsOIpInAlmBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 12, 3),
    _NtcTsOIpInAlmBufferOverflow_Type()
)
ntcTsOIpInAlmBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInAlmBufferOverflow.setStatus("current")
_NtcTsOIpInAlmBufferUnflow_Type = NtcAlarmState
_NtcTsOIpInAlmBufferUnflow_Object = MibScalar
ntcTsOIpInAlmBufferUnflow = _NtcTsOIpInAlmBufferUnflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 12, 4),
    _NtcTsOIpInAlmBufferUnflow_Type()
)
ntcTsOIpInAlmBufferUnflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInAlmBufferUnflow.setStatus("current")
_NtcTsOIpInAlmRtpNoSync_Type = NtcAlarmState
_NtcTsOIpInAlmRtpNoSync_Object = MibScalar
ntcTsOIpInAlmRtpNoSync = _NtcTsOIpInAlmRtpNoSync_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 12, 5),
    _NtcTsOIpInAlmRtpNoSync_Type()
)
ntcTsOIpInAlmRtpNoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInAlmRtpNoSync.setStatus("current")
_NtcTsOIpInAlmInvalidTsBitRate_Type = NtcAlarmState
_NtcTsOIpInAlmInvalidTsBitRate_Object = MibScalar
ntcTsOIpInAlmInvalidTsBitRate = _NtcTsOIpInAlmInvalidTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 12, 6),
    _NtcTsOIpInAlmInvalidTsBitRate_Type()
)
ntcTsOIpInAlmInvalidTsBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcTsOIpInAlmInvalidTsBitRate.setStatus("current")


class _NtcTsOIpInMulticastSourceA_Type(NtcNetworkAddress):
    """Custom type ntcTsOIpInMulticastSourceA based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0")


_NtcTsOIpInMulticastSourceA_Type.__name__ = "NtcNetworkAddress"
_NtcTsOIpInMulticastSourceA_Object = MibScalar
ntcTsOIpInMulticastSourceA = _NtcTsOIpInMulticastSourceA_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 13),
    _NtcTsOIpInMulticastSourceA_Type()
)
ntcTsOIpInMulticastSourceA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInMulticastSourceA.setStatus("current")


class _NtcTsOIpInMulticastSourceB_Type(NtcNetworkAddress):
    """Custom type ntcTsOIpInMulticastSourceB based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0")


_NtcTsOIpInMulticastSourceB_Type.__name__ = "NtcNetworkAddress"
_NtcTsOIpInMulticastSourceB_Object = MibScalar
ntcTsOIpInMulticastSourceB = _NtcTsOIpInMulticastSourceB_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 14),
    _NtcTsOIpInMulticastSourceB_Type()
)
ntcTsOIpInMulticastSourceB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInMulticastSourceB.setStatus("current")


class _NtcTsOIpInInputRateType_Type(Integer32):
    """Custom type ntcTsOIpInInputRateType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("userdefined", 0),
          ("pcr", 1))
    )


_NtcTsOIpInInputRateType_Type.__name__ = "Integer32"
_NtcTsOIpInInputRateType_Object = MibScalar
ntcTsOIpInInputRateType = _NtcTsOIpInInputRateType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 15),
    _NtcTsOIpInInputRateType_Type()
)
ntcTsOIpInInputRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInInputRateType.setStatus("current")


class _NtcTsOIpInAutoPcrDetection_Type(NtcEnable):
    """Custom type ntcTsOIpInAutoPcrDetection based on NtcEnable"""
    defaultValue = 1


_NtcTsOIpInAutoPcrDetection_Type.__name__ = "NtcEnable"
_NtcTsOIpInAutoPcrDetection_Object = MibScalar
ntcTsOIpInAutoPcrDetection = _NtcTsOIpInAutoPcrDetection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 16),
    _NtcTsOIpInAutoPcrDetection_Type()
)
ntcTsOIpInAutoPcrDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInAutoPcrDetection.setStatus("current")


class _NtcTsOIpInPcrPid_Type(Unsigned32):
    """Custom type ntcTsOIpInPcrPid based on Unsigned32"""
    defaultValue = 8191

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_NtcTsOIpInPcrPid_Type.__name__ = "Unsigned32"
_NtcTsOIpInPcrPid_Object = MibScalar
ntcTsOIpInPcrPid = _NtcTsOIpInPcrPid_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 1, 17),
    _NtcTsOIpInPcrPid_Type()
)
ntcTsOIpInPcrPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcTsOIpInPcrPid.setStatus("current")
_NtcTsOIpInConformance_ObjectIdentity = ObjectIdentity
ntcTsOIpInConformance = _NtcTsOIpInConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 2)
)
if mibBuilder.loadTexts:
    ntcTsOIpInConformance.setStatus("current")
_NtcTsOIpInConfCompliance_ObjectIdentity = ObjectIdentity
ntcTsOIpInConfCompliance = _NtcTsOIpInConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 2, 1)
)
if mibBuilder.loadTexts:
    ntcTsOIpInConfCompliance.setStatus("current")
_NtcTsOIpInConfGroup_ObjectIdentity = ObjectIdentity
ntcTsOIpInConfGroup = _NtcTsOIpInConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 2, 2)
)
if mibBuilder.loadTexts:
    ntcTsOIpInConfGroup.setStatus("current")

# Managed Objects groups

ntcTsOIpInConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 2, 2, 1)
)
ntcTsOIpInConfGrpV1Standard.setObjects(
      *(("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInEnable"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInInputSelection"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInTsEncapProtocol"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInIpAddressType"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMulticastAddress"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInUdpPort"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInTrafficProfile"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMaxBufferDelay"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInInputTsBitRate"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonResetCounters"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonInputTsBitRate"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonBufferDelay"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonMinBufferFilling"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonMaxBufferFilling"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonSourceInfo"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonRtpFecScheme"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonTsInCount"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonRtpInCount"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonRtpColumnFecInCount"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonRtpRowFecInCount"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonTsOutCount"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonTsDropCount"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonTsOverflowCount"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonRtpDropCount"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonRtpRepairCount"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonRtpFecDropCount"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMonActivePCRPID"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInAlmGeneralTsOverIpIn"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInAlmNoInputData"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInAlmBufferOverflow"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInAlmBufferUnflow"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInAlmRtpNoSync"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInAlmInvalidTsBitRate"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMulticastSourceA"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMulticastSourceB"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInInputRateType"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInAutoPcrDetection"),
        ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInPcrPid"))
)
if mibBuilder.loadTexts:
    ntcTsOIpInConfGrpV1Standard.setStatus("current")

ntcTsOIpInConfGrpObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 2, 2, 2)
)
ntcTsOIpInConfGrpObsolete.setObjects(
    ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInMaxTrafficJitter")
)
if mibBuilder.loadTexts:
    ntcTsOIpInConfGrpObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcTsOIpInConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 600, 2, 1, 1)
)
ntcTsOIpInConfCompV1Standard.setObjects(
    ("NEWTEC-TSOVERIPIN-MIB", "ntcTsOIpInConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcTsOIpInConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-TSOVERIPIN-MIB",
    **{"ntcTsOverIpIn": ntcTsOverIpIn,
       "ntcTsOIpInObjects": ntcTsOIpInObjects,
       "ntcTsOIpInEnable": ntcTsOIpInEnable,
       "ntcTsOIpInInputSelection": ntcTsOIpInInputSelection,
       "ntcTsOIpInTsEncapProtocol": ntcTsOIpInTsEncapProtocol,
       "ntcTsOIpInIpAddressType": ntcTsOIpInIpAddressType,
       "ntcTsOIpInMulticastAddress": ntcTsOIpInMulticastAddress,
       "ntcTsOIpInUdpPort": ntcTsOIpInUdpPort,
       "ntcTsOIpInTrafficProfile": ntcTsOIpInTrafficProfile,
       "ntcTsOIpInMaxTrafficJitter": ntcTsOIpInMaxTrafficJitter,
       "ntcTsOIpInMaxBufferDelay": ntcTsOIpInMaxBufferDelay,
       "ntcTsOIpInInputTsBitRate": ntcTsOIpInInputTsBitRate,
       "ntcTsOIpInMonitor": ntcTsOIpInMonitor,
       "ntcTsOIpInMonResetCounters": ntcTsOIpInMonResetCounters,
       "ntcTsOIpInMonInputTsBitRate": ntcTsOIpInMonInputTsBitRate,
       "ntcTsOIpInMonBufferDelay": ntcTsOIpInMonBufferDelay,
       "ntcTsOIpInMonMinBufferFilling": ntcTsOIpInMonMinBufferFilling,
       "ntcTsOIpInMonMaxBufferFilling": ntcTsOIpInMonMaxBufferFilling,
       "ntcTsOIpInMonSourceInfo": ntcTsOIpInMonSourceInfo,
       "ntcTsOIpInMonRtpFecScheme": ntcTsOIpInMonRtpFecScheme,
       "ntcTsOIpInMonTsInCount": ntcTsOIpInMonTsInCount,
       "ntcTsOIpInMonRtpInCount": ntcTsOIpInMonRtpInCount,
       "ntcTsOIpInMonRtpColumnFecInCount": ntcTsOIpInMonRtpColumnFecInCount,
       "ntcTsOIpInMonRtpRowFecInCount": ntcTsOIpInMonRtpRowFecInCount,
       "ntcTsOIpInMonTsOutCount": ntcTsOIpInMonTsOutCount,
       "ntcTsOIpInMonTsDropCount": ntcTsOIpInMonTsDropCount,
       "ntcTsOIpInMonTsOverflowCount": ntcTsOIpInMonTsOverflowCount,
       "ntcTsOIpInMonRtpDropCount": ntcTsOIpInMonRtpDropCount,
       "ntcTsOIpInMonRtpRepairCount": ntcTsOIpInMonRtpRepairCount,
       "ntcTsOIpInMonRtpFecDropCount": ntcTsOIpInMonRtpFecDropCount,
       "ntcTsOIpInMonActivePCRPID": ntcTsOIpInMonActivePCRPID,
       "ntcTsOIpInAlarm": ntcTsOIpInAlarm,
       "ntcTsOIpInAlmGeneralTsOverIpIn": ntcTsOIpInAlmGeneralTsOverIpIn,
       "ntcTsOIpInAlmNoInputData": ntcTsOIpInAlmNoInputData,
       "ntcTsOIpInAlmBufferOverflow": ntcTsOIpInAlmBufferOverflow,
       "ntcTsOIpInAlmBufferUnflow": ntcTsOIpInAlmBufferUnflow,
       "ntcTsOIpInAlmRtpNoSync": ntcTsOIpInAlmRtpNoSync,
       "ntcTsOIpInAlmInvalidTsBitRate": ntcTsOIpInAlmInvalidTsBitRate,
       "ntcTsOIpInMulticastSourceA": ntcTsOIpInMulticastSourceA,
       "ntcTsOIpInMulticastSourceB": ntcTsOIpInMulticastSourceB,
       "ntcTsOIpInInputRateType": ntcTsOIpInInputRateType,
       "ntcTsOIpInAutoPcrDetection": ntcTsOIpInAutoPcrDetection,
       "ntcTsOIpInPcrPid": ntcTsOIpInPcrPid,
       "ntcTsOIpInConformance": ntcTsOIpInConformance,
       "ntcTsOIpInConfCompliance": ntcTsOIpInConfCompliance,
       "ntcTsOIpInConfCompV1Standard": ntcTsOIpInConfCompV1Standard,
       "ntcTsOIpInConfGroup": ntcTsOIpInConfGroup,
       "ntcTsOIpInConfGrpV1Standard": ntcTsOIpInConfGrpV1Standard,
       "ntcTsOIpInConfGrpObsolete": ntcTsOIpInConfGrpObsolete}
)
