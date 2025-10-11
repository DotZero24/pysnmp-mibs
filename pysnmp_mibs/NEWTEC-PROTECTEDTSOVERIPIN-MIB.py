# SNMP MIB module (NEWTEC-PROTECTEDTSOVERIPIN-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-PROTECTEDTSOVERIPIN-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:04:16 2025
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

ntcProtectedTsOverIpIn = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400)
)
if mibBuilder.loadTexts:
    ntcProtectedTsOverIpIn.setRevisions(
        ("2018-04-04 10:00",
         "2017-07-10 12:00",
         "2016-02-02 07:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcProtTsOIpInObjects_ObjectIdentity = ObjectIdentity
ntcProtTsOIpInObjects = _NtcProtTsOIpInObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInObjects.setStatus("current")


class _NtcProtTsOIpInEnable_Type(NtcEnable):
    """Custom type ntcProtTsOIpInEnable based on NtcEnable"""
    defaultValue = 0


_NtcProtTsOIpInEnable_Type.__name__ = "NtcEnable"
_NtcProtTsOIpInEnable_Object = MibScalar
ntcProtTsOIpInEnable = _NtcProtTsOIpInEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 1),
    _NtcProtTsOIpInEnable_Type()
)
ntcProtTsOIpInEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInEnable.setStatus("current")


class _NtcProtTsOIpInProtInpSelection_Type(Integer32):
    """Custom type ntcProtTsOIpInProtInpSelection based on Integer32"""
    defaultValue = 3

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
        *(("tsoip1", 1),
          ("tsoip2", 2),
          ("tsoip1or2", 3),
          ("tsoip1before2", 4),
          ("tsoip2before1", 5))
    )


_NtcProtTsOIpInProtInpSelection_Type.__name__ = "Integer32"
_NtcProtTsOIpInProtInpSelection_Object = MibScalar
ntcProtTsOIpInProtInpSelection = _NtcProtTsOIpInProtInpSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 2),
    _NtcProtTsOIpInProtInpSelection_Type()
)
ntcProtTsOIpInProtInpSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInProtInpSelection.setStatus("current")
_NtcProtTsOIpInConfTable_Object = MibTable
ntcProtTsOIpInConfTable = _NtcProtTsOIpInConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInConfTable.setStatus("current")
_NtcProtTsOIpInConfEntry_Object = MibTableRow
ntcProtTsOIpInConfEntry = _NtcProtTsOIpInConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1)
)
ntcProtTsOIpInConfEntry.setIndexNames(
    (0, "NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInConfName"),
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInConfEntry.setStatus("current")


class _NtcProtTsOIpInConfName_Type(DisplayString):
    """Custom type ntcProtTsOIpInConfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_NtcProtTsOIpInConfName_Type.__name__ = "DisplayString"
_NtcProtTsOIpInConfName_Object = MibTableColumn
ntcProtTsOIpInConfName = _NtcProtTsOIpInConfName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 1),
    _NtcProtTsOIpInConfName_Type()
)
ntcProtTsOIpInConfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcProtTsOIpInConfName.setStatus("current")


class _NtcProtTsOIpInInpSelection_Type(Integer32):
    """Custom type ntcProtTsOIpInInpSelection based on Integer32"""
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


_NtcProtTsOIpInInpSelection_Type.__name__ = "Integer32"
_NtcProtTsOIpInInpSelection_Object = MibTableColumn
ntcProtTsOIpInInpSelection = _NtcProtTsOIpInInpSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 2),
    _NtcProtTsOIpInInpSelection_Type()
)
ntcProtTsOIpInInpSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInInpSelection.setStatus("current")


class _NtcProtTsOIpInTsEncapProtocol_Type(Integer32):
    """Custom type ntcProtTsOIpInTsEncapProtocol based on Integer32"""
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


_NtcProtTsOIpInTsEncapProtocol_Type.__name__ = "Integer32"
_NtcProtTsOIpInTsEncapProtocol_Object = MibTableColumn
ntcProtTsOIpInTsEncapProtocol = _NtcProtTsOIpInTsEncapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 3),
    _NtcProtTsOIpInTsEncapProtocol_Type()
)
ntcProtTsOIpInTsEncapProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInTsEncapProtocol.setStatus("current")


class _NtcProtTsOIpInIpAddressType_Type(Integer32):
    """Custom type ntcProtTsOIpInIpAddressType based on Integer32"""
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


_NtcProtTsOIpInIpAddressType_Type.__name__ = "Integer32"
_NtcProtTsOIpInIpAddressType_Object = MibTableColumn
ntcProtTsOIpInIpAddressType = _NtcProtTsOIpInIpAddressType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 4),
    _NtcProtTsOIpInIpAddressType_Type()
)
ntcProtTsOIpInIpAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInIpAddressType.setStatus("current")


class _NtcProtTsOIpInMulticastAddress_Type(IpAddress):
    """Custom type ntcProtTsOIpInMulticastAddress based on IpAddress"""
    defaultHexValue = "e0010001"


_NtcProtTsOIpInMulticastAddress_Type.__name__ = "IpAddress"
_NtcProtTsOIpInMulticastAddress_Object = MibTableColumn
ntcProtTsOIpInMulticastAddress = _NtcProtTsOIpInMulticastAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 5),
    _NtcProtTsOIpInMulticastAddress_Type()
)
ntcProtTsOIpInMulticastAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMulticastAddress.setStatus("current")


class _NtcProtTsOIpInMulticastSourceA_Type(NtcNetworkAddress):
    """Custom type ntcProtTsOIpInMulticastSourceA based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0")


_NtcProtTsOIpInMulticastSourceA_Type.__name__ = "NtcNetworkAddress"
_NtcProtTsOIpInMulticastSourceA_Object = MibTableColumn
ntcProtTsOIpInMulticastSourceA = _NtcProtTsOIpInMulticastSourceA_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 6),
    _NtcProtTsOIpInMulticastSourceA_Type()
)
ntcProtTsOIpInMulticastSourceA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMulticastSourceA.setStatus("current")


class _NtcProtTsOIpInMulticastSourceB_Type(NtcNetworkAddress):
    """Custom type ntcProtTsOIpInMulticastSourceB based on NtcNetworkAddress"""
    defaultValue = OctetString("0.0.0.0")


_NtcProtTsOIpInMulticastSourceB_Type.__name__ = "NtcNetworkAddress"
_NtcProtTsOIpInMulticastSourceB_Object = MibTableColumn
ntcProtTsOIpInMulticastSourceB = _NtcProtTsOIpInMulticastSourceB_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 7),
    _NtcProtTsOIpInMulticastSourceB_Type()
)
ntcProtTsOIpInMulticastSourceB.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMulticastSourceB.setStatus("current")


class _NtcProtTsOIpInUdpPort_Type(Unsigned32):
    """Custom type ntcProtTsOIpInUdpPort based on Unsigned32"""
    defaultValue = 56789

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtcProtTsOIpInUdpPort_Type.__name__ = "Unsigned32"
_NtcProtTsOIpInUdpPort_Object = MibTableColumn
ntcProtTsOIpInUdpPort = _NtcProtTsOIpInUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 8),
    _NtcProtTsOIpInUdpPort_Type()
)
ntcProtTsOIpInUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInUdpPort.setStatus("current")


class _NtcProtTsOIpInTrafficProfile_Type(Integer32):
    """Custom type ntcProtTsOIpInTrafficProfile based on Integer32"""
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


_NtcProtTsOIpInTrafficProfile_Type.__name__ = "Integer32"
_NtcProtTsOIpInTrafficProfile_Object = MibTableColumn
ntcProtTsOIpInTrafficProfile = _NtcProtTsOIpInTrafficProfile_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 9),
    _NtcProtTsOIpInTrafficProfile_Type()
)
ntcProtTsOIpInTrafficProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInTrafficProfile.setStatus("current")


class _NtcProtTsOIpInInputRateType_Type(Integer32):
    """Custom type ntcProtTsOIpInInputRateType based on Integer32"""
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


_NtcProtTsOIpInInputRateType_Type.__name__ = "Integer32"
_NtcProtTsOIpInInputRateType_Object = MibTableColumn
ntcProtTsOIpInInputRateType = _NtcProtTsOIpInInputRateType_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 10),
    _NtcProtTsOIpInInputRateType_Type()
)
ntcProtTsOIpInInputRateType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInInputRateType.setStatus("current")


class _NtcProtTsOIpInAutoPcrDetection_Type(NtcEnable):
    """Custom type ntcProtTsOIpInAutoPcrDetection based on NtcEnable"""
    defaultValue = 1


_NtcProtTsOIpInAutoPcrDetection_Type.__name__ = "NtcEnable"
_NtcProtTsOIpInAutoPcrDetection_Object = MibTableColumn
ntcProtTsOIpInAutoPcrDetection = _NtcProtTsOIpInAutoPcrDetection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 11),
    _NtcProtTsOIpInAutoPcrDetection_Type()
)
ntcProtTsOIpInAutoPcrDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInAutoPcrDetection.setStatus("current")


class _NtcProtTsOIpInPcrPid_Type(Unsigned32):
    """Custom type ntcProtTsOIpInPcrPid based on Unsigned32"""
    defaultValue = 8191

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8191),
    )


_NtcProtTsOIpInPcrPid_Type.__name__ = "Unsigned32"
_NtcProtTsOIpInPcrPid_Object = MibTableColumn
ntcProtTsOIpInPcrPid = _NtcProtTsOIpInPcrPid_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 12),
    _NtcProtTsOIpInPcrPid_Type()
)
ntcProtTsOIpInPcrPid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInPcrPid.setStatus("current")


class _NtcProtTsOIpInMaxBufferDelay_Type(Unsigned32):
    """Custom type ntcProtTsOIpInMaxBufferDelay based on Unsigned32"""
    defaultValue = 250


_NtcProtTsOIpInMaxBufferDelay_Type.__name__ = "Unsigned32"
_NtcProtTsOIpInMaxBufferDelay_Object = MibTableColumn
ntcProtTsOIpInMaxBufferDelay = _NtcProtTsOIpInMaxBufferDelay_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 13),
    _NtcProtTsOIpInMaxBufferDelay_Type()
)
ntcProtTsOIpInMaxBufferDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMaxBufferDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMaxBufferDelay.setUnits("ms")


class _NtcProtTsOIpInInputTsBitRate_Type(Unsigned32):
    """Custom type ntcProtTsOIpInInputTsBitRate based on Unsigned32"""
    defaultValue = 1000000


_NtcProtTsOIpInInputTsBitRate_Type.__name__ = "Unsigned32"
_NtcProtTsOIpInInputTsBitRate_Object = MibTableColumn
ntcProtTsOIpInInputTsBitRate = _NtcProtTsOIpInInputTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 3, 1, 14),
    _NtcProtTsOIpInInputTsBitRate_Type()
)
ntcProtTsOIpInInputTsBitRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInInputTsBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInInputTsBitRate.setUnits("bps")
_NtcProtTsOIpInMon_ObjectIdentity = ObjectIdentity
ntcProtTsOIpInMon = _NtcProtTsOIpInMon_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInMon.setStatus("current")


class _NtcProtTsOIpInCounterReset_Type(Integer32):
    """Custom type ntcProtTsOIpInCounterReset based on Integer32"""
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


_NtcProtTsOIpInCounterReset_Type.__name__ = "Integer32"
_NtcProtTsOIpInCounterReset_Object = MibScalar
ntcProtTsOIpInCounterReset = _NtcProtTsOIpInCounterReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 1),
    _NtcProtTsOIpInCounterReset_Type()
)
ntcProtTsOIpInCounterReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInCounterReset.setStatus("current")
_NtcProtTsOIpInMInpSelTsBRate_Type = Unsigned32
_NtcProtTsOIpInMInpSelTsBRate_Object = MibScalar
ntcProtTsOIpInMInpSelTsBRate = _NtcProtTsOIpInMInpSelTsBRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 2),
    _NtcProtTsOIpInMInpSelTsBRate_Type()
)
ntcProtTsOIpInMInpSelTsBRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMInpSelTsBRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMInpSelTsBRate.setUnits("bps")
_NtcProtTsOIpInSwitchCount_Type = Counter32
_NtcProtTsOIpInSwitchCount_Object = MibScalar
ntcProtTsOIpInSwitchCount = _NtcProtTsOIpInSwitchCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 3),
    _NtcProtTsOIpInSwitchCount_Type()
)
ntcProtTsOIpInSwitchCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInSwitchCount.setStatus("current")


class _NtcProtTsOIpInActiveInput_Type(Integer32):
    """Custom type ntcProtTsOIpInActiveInput based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 0),
          ("tsoip1", 1),
          ("tsoip2", 2))
    )


_NtcProtTsOIpInActiveInput_Type.__name__ = "Integer32"
_NtcProtTsOIpInActiveInput_Object = MibScalar
ntcProtTsOIpInActiveInput = _NtcProtTsOIpInActiveInput_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 4),
    _NtcProtTsOIpInActiveInput_Type()
)
ntcProtTsOIpInActiveInput.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInActiveInput.setStatus("current")
_NtcProtTsOIpInMonTable_Object = MibTable
ntcProtTsOIpInMonTable = _NtcProtTsOIpInMonTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonTable.setStatus("current")
_NtcProtTsOIpInMonEntry_Object = MibTableRow
ntcProtTsOIpInMonEntry = _NtcProtTsOIpInMonEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1)
)
ntcProtTsOIpInMonEntry.setIndexNames(
    (0, "NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonName"),
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonEntry.setStatus("current")


class _NtcProtTsOIpInMonName_Type(DisplayString):
    """Custom type ntcProtTsOIpInMonName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcProtTsOIpInMonName_Type.__name__ = "DisplayString"
_NtcProtTsOIpInMonName_Object = MibTableColumn
ntcProtTsOIpInMonName = _NtcProtTsOIpInMonName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 1),
    _NtcProtTsOIpInMonName_Type()
)
ntcProtTsOIpInMonName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonName.setStatus("current")
_NtcProtTsOIpInMonMeasInTsBitRate_Type = Unsigned32
_NtcProtTsOIpInMonMeasInTsBitRate_Object = MibTableColumn
ntcProtTsOIpInMonMeasInTsBitRate = _NtcProtTsOIpInMonMeasInTsBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 2),
    _NtcProtTsOIpInMonMeasInTsBitRate_Type()
)
ntcProtTsOIpInMonMeasInTsBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonMeasInTsBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonMeasInTsBitRate.setUnits("bps")
_NtcProtTsOIpInMonBufferDelay_Type = Unsigned32
_NtcProtTsOIpInMonBufferDelay_Object = MibTableColumn
ntcProtTsOIpInMonBufferDelay = _NtcProtTsOIpInMonBufferDelay_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 3),
    _NtcProtTsOIpInMonBufferDelay_Type()
)
ntcProtTsOIpInMonBufferDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonBufferDelay.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonBufferDelay.setUnits("ms")
_NtcProtTsOIpInMonMinBufferFill_Type = Unsigned32
_NtcProtTsOIpInMonMinBufferFill_Object = MibTableColumn
ntcProtTsOIpInMonMinBufferFill = _NtcProtTsOIpInMonMinBufferFill_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 4),
    _NtcProtTsOIpInMonMinBufferFill_Type()
)
ntcProtTsOIpInMonMinBufferFill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonMinBufferFill.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonMinBufferFill.setUnits("ms")
_NtcProtTsOIpInMonMaxBufferFill_Type = Unsigned32
_NtcProtTsOIpInMonMaxBufferFill_Object = MibTableColumn
ntcProtTsOIpInMonMaxBufferFill = _NtcProtTsOIpInMonMaxBufferFill_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 5),
    _NtcProtTsOIpInMonMaxBufferFill_Type()
)
ntcProtTsOIpInMonMaxBufferFill.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonMaxBufferFill.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonMaxBufferFill.setUnits("ms")


class _NtcProtTsOIpInMonSourceInfo_Type(DisplayString):
    """Custom type ntcProtTsOIpInMonSourceInfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcProtTsOIpInMonSourceInfo_Type.__name__ = "DisplayString"
_NtcProtTsOIpInMonSourceInfo_Object = MibTableColumn
ntcProtTsOIpInMonSourceInfo = _NtcProtTsOIpInMonSourceInfo_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 6),
    _NtcProtTsOIpInMonSourceInfo_Type()
)
ntcProtTsOIpInMonSourceInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonSourceInfo.setStatus("current")


class _NtcProtTsOIpInMonRtpFecScheme_Type(DisplayString):
    """Custom type ntcProtTsOIpInMonRtpFecScheme based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcProtTsOIpInMonRtpFecScheme_Type.__name__ = "DisplayString"
_NtcProtTsOIpInMonRtpFecScheme_Object = MibTableColumn
ntcProtTsOIpInMonRtpFecScheme = _NtcProtTsOIpInMonRtpFecScheme_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 7),
    _NtcProtTsOIpInMonRtpFecScheme_Type()
)
ntcProtTsOIpInMonRtpFecScheme.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpFecScheme.setStatus("current")
_NtcProtTsOIpInMonTsInCount_Type = Counter32
_NtcProtTsOIpInMonTsInCount_Object = MibTableColumn
ntcProtTsOIpInMonTsInCount = _NtcProtTsOIpInMonTsInCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 8),
    _NtcProtTsOIpInMonTsInCount_Type()
)
ntcProtTsOIpInMonTsInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonTsInCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonTsInCount.setUnits("packets")
_NtcProtTsOIpInMonRtpInCount_Type = Counter32
_NtcProtTsOIpInMonRtpInCount_Object = MibTableColumn
ntcProtTsOIpInMonRtpInCount = _NtcProtTsOIpInMonRtpInCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 9),
    _NtcProtTsOIpInMonRtpInCount_Type()
)
ntcProtTsOIpInMonRtpInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpInCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpInCount.setUnits("packets")
_NtcProtTsOIpInMonRtpColFecInCnt_Type = Counter32
_NtcProtTsOIpInMonRtpColFecInCnt_Object = MibTableColumn
ntcProtTsOIpInMonRtpColFecInCnt = _NtcProtTsOIpInMonRtpColFecInCnt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 10),
    _NtcProtTsOIpInMonRtpColFecInCnt_Type()
)
ntcProtTsOIpInMonRtpColFecInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpColFecInCnt.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpColFecInCnt.setUnits("packets")
_NtcProtTsOIpInMonRtpRowFecInCnt_Type = Counter32
_NtcProtTsOIpInMonRtpRowFecInCnt_Object = MibTableColumn
ntcProtTsOIpInMonRtpRowFecInCnt = _NtcProtTsOIpInMonRtpRowFecInCnt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 11),
    _NtcProtTsOIpInMonRtpRowFecInCnt_Type()
)
ntcProtTsOIpInMonRtpRowFecInCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpRowFecInCnt.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpRowFecInCnt.setUnits("packets")
_NtcProtTsOIpInMonTsOutCount_Type = Counter32
_NtcProtTsOIpInMonTsOutCount_Object = MibTableColumn
ntcProtTsOIpInMonTsOutCount = _NtcProtTsOIpInMonTsOutCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 12),
    _NtcProtTsOIpInMonTsOutCount_Type()
)
ntcProtTsOIpInMonTsOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonTsOutCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonTsOutCount.setUnits("packets")
_NtcProtTsOIpInMonTsDropCount_Type = Counter32
_NtcProtTsOIpInMonTsDropCount_Object = MibTableColumn
ntcProtTsOIpInMonTsDropCount = _NtcProtTsOIpInMonTsDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 13),
    _NtcProtTsOIpInMonTsDropCount_Type()
)
ntcProtTsOIpInMonTsDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonTsDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonTsDropCount.setUnits("packets")
_NtcProtTsOIpInMonTsOverflowCount_Type = Counter32
_NtcProtTsOIpInMonTsOverflowCount_Object = MibTableColumn
ntcProtTsOIpInMonTsOverflowCount = _NtcProtTsOIpInMonTsOverflowCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 14),
    _NtcProtTsOIpInMonTsOverflowCount_Type()
)
ntcProtTsOIpInMonTsOverflowCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonTsOverflowCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonTsOverflowCount.setUnits("packets")
_NtcProtTsOIpInMonRtpDropCount_Type = Counter32
_NtcProtTsOIpInMonRtpDropCount_Object = MibTableColumn
ntcProtTsOIpInMonRtpDropCount = _NtcProtTsOIpInMonRtpDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 15),
    _NtcProtTsOIpInMonRtpDropCount_Type()
)
ntcProtTsOIpInMonRtpDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpDropCount.setUnits("packets")
_NtcProtTsOIpInMonRtpFecDropCount_Type = Counter32
_NtcProtTsOIpInMonRtpFecDropCount_Object = MibTableColumn
ntcProtTsOIpInMonRtpFecDropCount = _NtcProtTsOIpInMonRtpFecDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 16),
    _NtcProtTsOIpInMonRtpFecDropCount_Type()
)
ntcProtTsOIpInMonRtpFecDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpFecDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpFecDropCount.setUnits("packets")
_NtcProtTsOIpInMonRtpRepairCount_Type = Counter32
_NtcProtTsOIpInMonRtpRepairCount_Object = MibTableColumn
ntcProtTsOIpInMonRtpRepairCount = _NtcProtTsOIpInMonRtpRepairCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 17),
    _NtcProtTsOIpInMonRtpRepairCount_Type()
)
ntcProtTsOIpInMonRtpRepairCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpRepairCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInMonRtpRepairCount.setUnits("packets")


class _NtcProtTsOIpInActivePcrPid_Type(Unsigned32):
    """Custom type ntcProtTsOIpInActivePcrPid based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8190),
    )


_NtcProtTsOIpInActivePcrPid_Type.__name__ = "Unsigned32"
_NtcProtTsOIpInActivePcrPid_Object = MibTableColumn
ntcProtTsOIpInActivePcrPid = _NtcProtTsOIpInActivePcrPid_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 4, 5, 1, 18),
    _NtcProtTsOIpInActivePcrPid_Type()
)
ntcProtTsOIpInActivePcrPid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInActivePcrPid.setStatus("current")
_NtcProtTsOIpInAlarms_ObjectIdentity = ObjectIdentity
ntcProtTsOIpInAlarms = _NtcProtTsOIpInAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 5)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlarms.setStatus("current")
_NtcProtTsOIpInAlarmStatusTable_Object = MibTable
ntcProtTsOIpInAlarmStatusTable = _NtcProtTsOIpInAlarmStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 5, 1)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlarmStatusTable.setStatus("current")
_NtcProtTsOIpInAlarmStatusEntry_Object = MibTableRow
ntcProtTsOIpInAlarmStatusEntry = _NtcProtTsOIpInAlarmStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 5, 1, 1)
)
ntcProtTsOIpInAlarmStatusEntry.setIndexNames(
    (0, "NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInAlarmStatusName"),
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlarmStatusEntry.setStatus("current")


class _NtcProtTsOIpInAlarmStatusName_Type(DisplayString):
    """Custom type ntcProtTsOIpInAlarmStatusName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NtcProtTsOIpInAlarmStatusName_Type.__name__ = "DisplayString"
_NtcProtTsOIpInAlarmStatusName_Object = MibTableColumn
ntcProtTsOIpInAlarmStatusName = _NtcProtTsOIpInAlarmStatusName_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 5, 1, 1, 1),
    _NtcProtTsOIpInAlarmStatusName_Type()
)
ntcProtTsOIpInAlarmStatusName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlarmStatusName.setStatus("current")
_NtcProtTsOIpInNoInputData_Type = NtcAlarmState
_NtcProtTsOIpInNoInputData_Object = MibTableColumn
ntcProtTsOIpInNoInputData = _NtcProtTsOIpInNoInputData_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 5, 1, 1, 2),
    _NtcProtTsOIpInNoInputData_Type()
)
ntcProtTsOIpInNoInputData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInNoInputData.setStatus("current")
_NtcProtTsOIpInBufferUnderflow_Type = NtcAlarmState
_NtcProtTsOIpInBufferUnderflow_Object = MibTableColumn
ntcProtTsOIpInBufferUnderflow = _NtcProtTsOIpInBufferUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 5, 1, 1, 3),
    _NtcProtTsOIpInBufferUnderflow_Type()
)
ntcProtTsOIpInBufferUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInBufferUnderflow.setStatus("current")
_NtcProtTsOIpInBufferOverflow_Type = NtcAlarmState
_NtcProtTsOIpInBufferOverflow_Object = MibTableColumn
ntcProtTsOIpInBufferOverflow = _NtcProtTsOIpInBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 5, 1, 1, 4),
    _NtcProtTsOIpInBufferOverflow_Type()
)
ntcProtTsOIpInBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInBufferOverflow.setStatus("current")
_NtcProtTsOIpInRtpNoSync_Type = NtcAlarmState
_NtcProtTsOIpInRtpNoSync_Object = MibTableColumn
ntcProtTsOIpInRtpNoSync = _NtcProtTsOIpInRtpNoSync_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 5, 1, 1, 5),
    _NtcProtTsOIpInRtpNoSync_Type()
)
ntcProtTsOIpInRtpNoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInRtpNoSync.setStatus("current")
_NtcProtTsOIpInAlarm_ObjectIdentity = ObjectIdentity
ntcProtTsOIpInAlarm = _NtcProtTsOIpInAlarm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 6)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlarm.setStatus("current")
_NtcProtTsOIpInAlRedFailure_Type = NtcAlarmState
_NtcProtTsOIpInAlRedFailure_Object = MibScalar
ntcProtTsOIpInAlRedFailure = _NtcProtTsOIpInAlRedFailure_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 6, 1),
    _NtcProtTsOIpInAlRedFailure_Type()
)
ntcProtTsOIpInAlRedFailure.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlRedFailure.setStatus("current")
_NtcProtTsOIpInAlRedDegraded_Type = NtcAlarmState
_NtcProtTsOIpInAlRedDegraded_Object = MibScalar
ntcProtTsOIpInAlRedDegraded = _NtcProtTsOIpInAlRedDegraded_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 6, 2),
    _NtcProtTsOIpInAlRedDegraded_Type()
)
ntcProtTsOIpInAlRedDegraded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlRedDegraded.setStatus("current")
_NtcProtTsOIpInAlNoInputData_Type = NtcAlarmState
_NtcProtTsOIpInAlNoInputData_Object = MibScalar
ntcProtTsOIpInAlNoInputData = _NtcProtTsOIpInAlNoInputData_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 6, 3),
    _NtcProtTsOIpInAlNoInputData_Type()
)
ntcProtTsOIpInAlNoInputData.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlNoInputData.setStatus("current")
_NtcProtTsOIpInAlBufferUnderflow_Type = NtcAlarmState
_NtcProtTsOIpInAlBufferUnderflow_Object = MibScalar
ntcProtTsOIpInAlBufferUnderflow = _NtcProtTsOIpInAlBufferUnderflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 6, 4),
    _NtcProtTsOIpInAlBufferUnderflow_Type()
)
ntcProtTsOIpInAlBufferUnderflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlBufferUnderflow.setStatus("current")
_NtcProtTsOIpInAlBufferOverflow_Type = NtcAlarmState
_NtcProtTsOIpInAlBufferOverflow_Object = MibScalar
ntcProtTsOIpInAlBufferOverflow = _NtcProtTsOIpInAlBufferOverflow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 6, 5),
    _NtcProtTsOIpInAlBufferOverflow_Type()
)
ntcProtTsOIpInAlBufferOverflow.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlBufferOverflow.setStatus("current")
_NtcProtTsOIpInAlRtpNoSync_Type = NtcAlarmState
_NtcProtTsOIpInAlRtpNoSync_Object = MibScalar
ntcProtTsOIpInAlRtpNoSync = _NtcProtTsOIpInAlRtpNoSync_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 6, 6),
    _NtcProtTsOIpInAlRtpNoSync_Type()
)
ntcProtTsOIpInAlRtpNoSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcProtTsOIpInAlRtpNoSync.setStatus("current")
_NtcProtTsOIpInNpRangeThr_ObjectIdentity = ObjectIdentity
ntcProtTsOIpInNpRangeThr = _NtcProtTsOIpInNpRangeThr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 7)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInNpRangeThr.setStatus("current")


class _NtcProtTsOIpInNpRangeThrEnable_Type(NtcEnable):
    """Custom type ntcProtTsOIpInNpRangeThrEnable based on NtcEnable"""
    defaultValue = 0


_NtcProtTsOIpInNpRangeThrEnable_Type.__name__ = "NtcEnable"
_NtcProtTsOIpInNpRangeThrEnable_Object = MibScalar
ntcProtTsOIpInNpRangeThrEnable = _NtcProtTsOIpInNpRangeThrEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 7, 1),
    _NtcProtTsOIpInNpRangeThrEnable_Type()
)
ntcProtTsOIpInNpRangeThrEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInNpRangeThrEnable.setStatus("current")


class _NtcProtTsOIpInNpRangeThrMaxRate_Type(Unsigned32):
    """Custom type ntcProtTsOIpInNpRangeThrMaxRate based on Unsigned32"""
    defaultValue = 0


_NtcProtTsOIpInNpRangeThrMaxRate_Type.__name__ = "Unsigned32"
_NtcProtTsOIpInNpRangeThrMaxRate_Object = MibScalar
ntcProtTsOIpInNpRangeThrMaxRate = _NtcProtTsOIpInNpRangeThrMaxRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 7, 2),
    _NtcProtTsOIpInNpRangeThrMaxRate_Type()
)
ntcProtTsOIpInNpRangeThrMaxRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInNpRangeThrMaxRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInNpRangeThrMaxRate.setUnits("bps")


class _NtcProtTsOIpInNpRangeTimeWindow_Type(Integer32):
    """Custom type ntcProtTsOIpInNpRangeTimeWindow based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 50),
    )


_NtcProtTsOIpInNpRangeTimeWindow_Type.__name__ = "Integer32"
_NtcProtTsOIpInNpRangeTimeWindow_Object = MibScalar
ntcProtTsOIpInNpRangeTimeWindow = _NtcProtTsOIpInNpRangeTimeWindow_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 1, 7, 3),
    _NtcProtTsOIpInNpRangeTimeWindow_Type()
)
ntcProtTsOIpInNpRangeTimeWindow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcProtTsOIpInNpRangeTimeWindow.setStatus("current")
if mibBuilder.loadTexts:
    ntcProtTsOIpInNpRangeTimeWindow.setUnits("s")
_NtcProtTsOIpInConformance_ObjectIdentity = ObjectIdentity
ntcProtTsOIpInConformance = _NtcProtTsOIpInConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 2)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInConformance.setStatus("current")
_NtcProtTsOIpInConfCompliance_ObjectIdentity = ObjectIdentity
ntcProtTsOIpInConfCompliance = _NtcProtTsOIpInConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 2, 1)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInConfCompliance.setStatus("current")
_NtcProtTsOIpInConfGroup_ObjectIdentity = ObjectIdentity
ntcProtTsOIpInConfGroup = _NtcProtTsOIpInConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 2, 2)
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInConfGroup.setStatus("current")

# Managed Objects groups

ntcProtTsOIpInConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 2, 2, 1)
)
ntcProtTsOIpInConfGrpV1Standard.setObjects(
      *(("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInEnable"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInProtInpSelection"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInInpSelection"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInTsEncapProtocol"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInIpAddressType"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMulticastAddress"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMulticastSourceA"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMulticastSourceB"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInUdpPort"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInTrafficProfile"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInInputRateType"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInAutoPcrDetection"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInPcrPid"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMaxBufferDelay"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInInputTsBitRate"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInCounterReset"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMInpSelTsBRate"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInSwitchCount"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInActiveInput"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonMeasInTsBitRate"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonBufferDelay"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonMinBufferFill"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonMaxBufferFill"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonSourceInfo"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonRtpFecScheme"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonTsInCount"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonRtpInCount"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonRtpColFecInCnt"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonRtpRowFecInCnt"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonTsOutCount"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonTsDropCount"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonTsOverflowCount"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonRtpDropCount"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonRtpFecDropCount"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInMonRtpRepairCount"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInActivePcrPid"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInNoInputData"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInBufferUnderflow"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInBufferOverflow"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInRtpNoSync"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInAlRedFailure"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInAlRedDegraded"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInAlNoInputData"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInAlBufferUnderflow"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInAlBufferOverflow"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInAlRtpNoSync"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInNpRangeThrEnable"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInNpRangeThrMaxRate"),
        ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInNpRangeTimeWindow"))
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcProtTsOIpInConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 9400, 2, 1, 1)
)
ntcProtTsOIpInConfCompV1Standard.setObjects(
    ("NEWTEC-PROTECTEDTSOVERIPIN-MIB", "ntcProtTsOIpInConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcProtTsOIpInConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-PROTECTEDTSOVERIPIN-MIB",
    **{"ntcProtectedTsOverIpIn": ntcProtectedTsOverIpIn,
       "ntcProtTsOIpInObjects": ntcProtTsOIpInObjects,
       "ntcProtTsOIpInEnable": ntcProtTsOIpInEnable,
       "ntcProtTsOIpInProtInpSelection": ntcProtTsOIpInProtInpSelection,
       "ntcProtTsOIpInConfTable": ntcProtTsOIpInConfTable,
       "ntcProtTsOIpInConfEntry": ntcProtTsOIpInConfEntry,
       "ntcProtTsOIpInConfName": ntcProtTsOIpInConfName,
       "ntcProtTsOIpInInpSelection": ntcProtTsOIpInInpSelection,
       "ntcProtTsOIpInTsEncapProtocol": ntcProtTsOIpInTsEncapProtocol,
       "ntcProtTsOIpInIpAddressType": ntcProtTsOIpInIpAddressType,
       "ntcProtTsOIpInMulticastAddress": ntcProtTsOIpInMulticastAddress,
       "ntcProtTsOIpInMulticastSourceA": ntcProtTsOIpInMulticastSourceA,
       "ntcProtTsOIpInMulticastSourceB": ntcProtTsOIpInMulticastSourceB,
       "ntcProtTsOIpInUdpPort": ntcProtTsOIpInUdpPort,
       "ntcProtTsOIpInTrafficProfile": ntcProtTsOIpInTrafficProfile,
       "ntcProtTsOIpInInputRateType": ntcProtTsOIpInInputRateType,
       "ntcProtTsOIpInAutoPcrDetection": ntcProtTsOIpInAutoPcrDetection,
       "ntcProtTsOIpInPcrPid": ntcProtTsOIpInPcrPid,
       "ntcProtTsOIpInMaxBufferDelay": ntcProtTsOIpInMaxBufferDelay,
       "ntcProtTsOIpInInputTsBitRate": ntcProtTsOIpInInputTsBitRate,
       "ntcProtTsOIpInMon": ntcProtTsOIpInMon,
       "ntcProtTsOIpInCounterReset": ntcProtTsOIpInCounterReset,
       "ntcProtTsOIpInMInpSelTsBRate": ntcProtTsOIpInMInpSelTsBRate,
       "ntcProtTsOIpInSwitchCount": ntcProtTsOIpInSwitchCount,
       "ntcProtTsOIpInActiveInput": ntcProtTsOIpInActiveInput,
       "ntcProtTsOIpInMonTable": ntcProtTsOIpInMonTable,
       "ntcProtTsOIpInMonEntry": ntcProtTsOIpInMonEntry,
       "ntcProtTsOIpInMonName": ntcProtTsOIpInMonName,
       "ntcProtTsOIpInMonMeasInTsBitRate": ntcProtTsOIpInMonMeasInTsBitRate,
       "ntcProtTsOIpInMonBufferDelay": ntcProtTsOIpInMonBufferDelay,
       "ntcProtTsOIpInMonMinBufferFill": ntcProtTsOIpInMonMinBufferFill,
       "ntcProtTsOIpInMonMaxBufferFill": ntcProtTsOIpInMonMaxBufferFill,
       "ntcProtTsOIpInMonSourceInfo": ntcProtTsOIpInMonSourceInfo,
       "ntcProtTsOIpInMonRtpFecScheme": ntcProtTsOIpInMonRtpFecScheme,
       "ntcProtTsOIpInMonTsInCount": ntcProtTsOIpInMonTsInCount,
       "ntcProtTsOIpInMonRtpInCount": ntcProtTsOIpInMonRtpInCount,
       "ntcProtTsOIpInMonRtpColFecInCnt": ntcProtTsOIpInMonRtpColFecInCnt,
       "ntcProtTsOIpInMonRtpRowFecInCnt": ntcProtTsOIpInMonRtpRowFecInCnt,
       "ntcProtTsOIpInMonTsOutCount": ntcProtTsOIpInMonTsOutCount,
       "ntcProtTsOIpInMonTsDropCount": ntcProtTsOIpInMonTsDropCount,
       "ntcProtTsOIpInMonTsOverflowCount": ntcProtTsOIpInMonTsOverflowCount,
       "ntcProtTsOIpInMonRtpDropCount": ntcProtTsOIpInMonRtpDropCount,
       "ntcProtTsOIpInMonRtpFecDropCount": ntcProtTsOIpInMonRtpFecDropCount,
       "ntcProtTsOIpInMonRtpRepairCount": ntcProtTsOIpInMonRtpRepairCount,
       "ntcProtTsOIpInActivePcrPid": ntcProtTsOIpInActivePcrPid,
       "ntcProtTsOIpInAlarms": ntcProtTsOIpInAlarms,
       "ntcProtTsOIpInAlarmStatusTable": ntcProtTsOIpInAlarmStatusTable,
       "ntcProtTsOIpInAlarmStatusEntry": ntcProtTsOIpInAlarmStatusEntry,
       "ntcProtTsOIpInAlarmStatusName": ntcProtTsOIpInAlarmStatusName,
       "ntcProtTsOIpInNoInputData": ntcProtTsOIpInNoInputData,
       "ntcProtTsOIpInBufferUnderflow": ntcProtTsOIpInBufferUnderflow,
       "ntcProtTsOIpInBufferOverflow": ntcProtTsOIpInBufferOverflow,
       "ntcProtTsOIpInRtpNoSync": ntcProtTsOIpInRtpNoSync,
       "ntcProtTsOIpInAlarm": ntcProtTsOIpInAlarm,
       "ntcProtTsOIpInAlRedFailure": ntcProtTsOIpInAlRedFailure,
       "ntcProtTsOIpInAlRedDegraded": ntcProtTsOIpInAlRedDegraded,
       "ntcProtTsOIpInAlNoInputData": ntcProtTsOIpInAlNoInputData,
       "ntcProtTsOIpInAlBufferUnderflow": ntcProtTsOIpInAlBufferUnderflow,
       "ntcProtTsOIpInAlBufferOverflow": ntcProtTsOIpInAlBufferOverflow,
       "ntcProtTsOIpInAlRtpNoSync": ntcProtTsOIpInAlRtpNoSync,
       "ntcProtTsOIpInNpRangeThr": ntcProtTsOIpInNpRangeThr,
       "ntcProtTsOIpInNpRangeThrEnable": ntcProtTsOIpInNpRangeThrEnable,
       "ntcProtTsOIpInNpRangeThrMaxRate": ntcProtTsOIpInNpRangeThrMaxRate,
       "ntcProtTsOIpInNpRangeTimeWindow": ntcProtTsOIpInNpRangeTimeWindow,
       "ntcProtTsOIpInConformance": ntcProtTsOIpInConformance,
       "ntcProtTsOIpInConfCompliance": ntcProtTsOIpInConfCompliance,
       "ntcProtTsOIpInConfCompV1Standard": ntcProtTsOIpInConfCompV1Standard,
       "ntcProtTsOIpInConfGroup": ntcProtTsOIpInConfGroup,
       "ntcProtTsOIpInConfGrpV1Standard": ntcProtTsOIpInConfGrpV1Standard}
)
