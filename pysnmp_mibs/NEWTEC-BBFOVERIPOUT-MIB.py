# SNMP MIB module (NEWTEC-BBFOVERIPOUT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/newtec/NEWTEC-BBFOVERIPOUT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:03:58 2025
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

(NtcEnable,) = mibBuilder.importSymbols(
    "NEWTEC-TC-MIB",
    "NtcEnable")

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

ntcBbfOverIpOut = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300)
)
if mibBuilder.loadTexts:
    ntcBbfOverIpOut.setRevisions(
        ("2018-02-02 09:00",
         "2017-10-16 12:00",
         "2015-04-13 07:00",
         "2013-05-22 06:00",
         "2013-01-08 12:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NtcBbfOIpOutObjects_ObjectIdentity = ObjectIdentity
ntcBbfOIpOutObjects = _NtcBbfOIpOutObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1)
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutObjects.setStatus("current")


class _NtcBbfOIpOutEnable_Type(NtcEnable):
    """Custom type ntcBbfOIpOutEnable based on NtcEnable"""
    defaultValue = 0


_NtcBbfOIpOutEnable_Type.__name__ = "NtcEnable"
_NtcBbfOIpOutEnable_Object = MibScalar
ntcBbfOIpOutEnable = _NtcBbfOIpOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 1),
    _NtcBbfOIpOutEnable_Type()
)
ntcBbfOIpOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpOutEnable.setStatus("current")


class _NtcBbfOIpOutOutputSelection_Type(Integer32):
    """Custom type ntcBbfOIpOutOutputSelection based on Integer32"""
    defaultValue = 1

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
        *(("data1", 1),
          ("data2", 2),
          ("data", 3),
          ("sat1", 4),
          ("sat2", 5),
          ("sat", 6))
    )


_NtcBbfOIpOutOutputSelection_Type.__name__ = "Integer32"
_NtcBbfOIpOutOutputSelection_Object = MibScalar
ntcBbfOIpOutOutputSelection = _NtcBbfOIpOutOutputSelection_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 2),
    _NtcBbfOIpOutOutputSelection_Type()
)
ntcBbfOIpOutOutputSelection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpOutOutputSelection.setStatus("current")
_NtcBbfOIpOutDestinationsTable_Object = MibTable
ntcBbfOIpOutDestinationsTable = _NtcBbfOIpOutDestinationsTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 3)
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutDestinationsTable.setStatus("current")
_NtcBbfOIpOutDestinationsEntry_Object = MibTableRow
ntcBbfOIpOutDestinationsEntry = _NtcBbfOIpOutDestinationsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 3, 1)
)
ntcBbfOIpOutDestinationsEntry.setIndexNames(
    (0, "NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutDestinationsDemodId"),
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutDestinationsEntry.setStatus("current")


class _NtcBbfOIpOutDestinationsDemodId_Type(Integer32):
    """Custom type ntcBbfOIpOutDestinationsDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcBbfOIpOutDestinationsDemodId_Type.__name__ = "Integer32"
_NtcBbfOIpOutDestinationsDemodId_Object = MibTableColumn
ntcBbfOIpOutDestinationsDemodId = _NtcBbfOIpOutDestinationsDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 3, 1, 1),
    _NtcBbfOIpOutDestinationsDemodId_Type()
)
ntcBbfOIpOutDestinationsDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcBbfOIpOutDestinationsDemodId.setStatus("current")


class _NtcBbfOIpOutBbfOutEnable_Type(NtcEnable):
    """Custom type ntcBbfOIpOutBbfOutEnable based on NtcEnable"""
    defaultValue = 0


_NtcBbfOIpOutBbfOutEnable_Type.__name__ = "NtcEnable"
_NtcBbfOIpOutBbfOutEnable_Object = MibTableColumn
ntcBbfOIpOutBbfOutEnable = _NtcBbfOIpOutBbfOutEnable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 3, 1, 2),
    _NtcBbfOIpOutBbfOutEnable_Type()
)
ntcBbfOIpOutBbfOutEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpOutBbfOutEnable.setStatus("current")
_NtcBbfOIpOutDestinationIpAddress_Type = IpAddress
_NtcBbfOIpOutDestinationIpAddress_Object = MibTableColumn
ntcBbfOIpOutDestinationIpAddress = _NtcBbfOIpOutDestinationIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 3, 1, 3),
    _NtcBbfOIpOutDestinationIpAddress_Type()
)
ntcBbfOIpOutDestinationIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpOutDestinationIpAddress.setStatus("current")


class _NtcBbfOIpOutDestinationUdpPort_Type(Unsigned32):
    """Custom type ntcBbfOIpOutDestinationUdpPort based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_NtcBbfOIpOutDestinationUdpPort_Type.__name__ = "Unsigned32"
_NtcBbfOIpOutDestinationUdpPort_Object = MibTableColumn
ntcBbfOIpOutDestinationUdpPort = _NtcBbfOIpOutDestinationUdpPort_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 3, 1, 4),
    _NtcBbfOIpOutDestinationUdpPort_Type()
)
ntcBbfOIpOutDestinationUdpPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpOutDestinationUdpPort.setStatus("current")


class _NtcBbfOIpOutPassInvalidFrames_Type(NtcEnable):
    """Custom type ntcBbfOIpOutPassInvalidFrames based on NtcEnable"""
    defaultValue = 0


_NtcBbfOIpOutPassInvalidFrames_Type.__name__ = "NtcEnable"
_NtcBbfOIpOutPassInvalidFrames_Object = MibTableColumn
ntcBbfOIpOutPassInvalidFrames = _NtcBbfOIpOutPassInvalidFrames_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 3, 1, 5),
    _NtcBbfOIpOutPassInvalidFrames_Type()
)
ntcBbfOIpOutPassInvalidFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpOutPassInvalidFrames.setStatus("current")


class _NtcBbfOIpOutEncapProt_Type(Integer32):
    """Custom type ntcBbfOIpOutEncapProt based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("udp", 0),
          ("rtp", 1))
    )


_NtcBbfOIpOutEncapProt_Type.__name__ = "Integer32"
_NtcBbfOIpOutEncapProt_Object = MibTableColumn
ntcBbfOIpOutEncapProt = _NtcBbfOIpOutEncapProt_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 3, 1, 6),
    _NtcBbfOIpOutEncapProt_Type()
)
ntcBbfOIpOutEncapProt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpOutEncapProt.setStatus("current")
_NtcBbfOIpOutMonitor_ObjectIdentity = ObjectIdentity
ntcBbfOIpOutMonitor = _NtcBbfOIpOutMonitor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4)
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonitor.setStatus("current")


class _NtcBbfOIpOutMonReset_Type(Integer32):
    """Custom type ntcBbfOIpOutMonReset based on Integer32"""
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


_NtcBbfOIpOutMonReset_Type.__name__ = "Integer32"
_NtcBbfOIpOutMonReset_Object = MibScalar
ntcBbfOIpOutMonReset = _NtcBbfOIpOutMonReset_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 1),
    _NtcBbfOIpOutMonReset_Type()
)
ntcBbfOIpOutMonReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonReset.setStatus("current")
_NtcBbfOIpOutMonOutputBbfBitRate_Type = Unsigned32
_NtcBbfOIpOutMonOutputBbfBitRate_Object = MibScalar
ntcBbfOIpOutMonOutputBbfBitRate = _NtcBbfOIpOutMonOutputBbfBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 2),
    _NtcBbfOIpOutMonOutputBbfBitRate_Type()
)
ntcBbfOIpOutMonOutputBbfBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonOutputBbfBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonOutputBbfBitRate.setUnits("bps")
_NtcBbfOIpOutMonBbfInCount_Type = Counter32
_NtcBbfOIpOutMonBbfInCount_Object = MibScalar
ntcBbfOIpOutMonBbfInCount = _NtcBbfOIpOutMonBbfInCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 3),
    _NtcBbfOIpOutMonBbfInCount_Type()
)
ntcBbfOIpOutMonBbfInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonBbfInCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonBbfInCount.setUnits("frames")
_NtcBbfOIpOutMonBbfOutCount_Type = Counter32
_NtcBbfOIpOutMonBbfOutCount_Object = MibScalar
ntcBbfOIpOutMonBbfOutCount = _NtcBbfOIpOutMonBbfOutCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 4),
    _NtcBbfOIpOutMonBbfOutCount_Type()
)
ntcBbfOIpOutMonBbfOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonBbfOutCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonBbfOutCount.setUnits("frames")
_NtcBbfOIpOutMonBbfDropCount_Type = Counter32
_NtcBbfOIpOutMonBbfDropCount_Object = MibScalar
ntcBbfOIpOutMonBbfDropCount = _NtcBbfOIpOutMonBbfDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 5),
    _NtcBbfOIpOutMonBbfDropCount_Type()
)
ntcBbfOIpOutMonBbfDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonBbfDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonBbfDropCount.setUnits("frames")
_NtcBbfOIpOutMonDestTable_Object = MibTable
ntcBbfOIpOutMonDestTable = _NtcBbfOIpOutMonDestTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 6)
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestTable.setStatus("current")
_NtcBbfOIpOutMonDestEntry_Object = MibTableRow
ntcBbfOIpOutMonDestEntry = _NtcBbfOIpOutMonDestEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 6, 1)
)
ntcBbfOIpOutMonDestEntry.setIndexNames(
    (0, "NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonDestDemodId"),
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestEntry.setStatus("current")


class _NtcBbfOIpOutMonDestDemodId_Type(Integer32):
    """Custom type ntcBbfOIpOutMonDestDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcBbfOIpOutMonDestDemodId_Type.__name__ = "Integer32"
_NtcBbfOIpOutMonDestDemodId_Object = MibTableColumn
ntcBbfOIpOutMonDestDemodId = _NtcBbfOIpOutMonDestDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 6, 1, 1),
    _NtcBbfOIpOutMonDestDemodId_Type()
)
ntcBbfOIpOutMonDestDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestDemodId.setStatus("current")
_NtcBbfOIpOutMonDestBitRate_Type = Unsigned32
_NtcBbfOIpOutMonDestBitRate_Object = MibTableColumn
ntcBbfOIpOutMonDestBitRate = _NtcBbfOIpOutMonDestBitRate_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 6, 1, 2),
    _NtcBbfOIpOutMonDestBitRate_Type()
)
ntcBbfOIpOutMonDestBitRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestBitRate.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestBitRate.setUnits("bps")
_NtcBbfOIpOutMonDestBbfInCount_Type = Counter32
_NtcBbfOIpOutMonDestBbfInCount_Object = MibTableColumn
ntcBbfOIpOutMonDestBbfInCount = _NtcBbfOIpOutMonDestBbfInCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 6, 1, 3),
    _NtcBbfOIpOutMonDestBbfInCount_Type()
)
ntcBbfOIpOutMonDestBbfInCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestBbfInCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestBbfInCount.setUnits("frames")
_NtcBbfOIpOutMonDestBbfOutCount_Type = Counter32
_NtcBbfOIpOutMonDestBbfOutCount_Object = MibTableColumn
ntcBbfOIpOutMonDestBbfOutCount = _NtcBbfOIpOutMonDestBbfOutCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 6, 1, 4),
    _NtcBbfOIpOutMonDestBbfOutCount_Type()
)
ntcBbfOIpOutMonDestBbfOutCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestBbfOutCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestBbfOutCount.setUnits("frames")
_NtcBbfOIpOutMonDestBbfDropCount_Type = Counter32
_NtcBbfOIpOutMonDestBbfDropCount_Object = MibTableColumn
ntcBbfOIpOutMonDestBbfDropCount = _NtcBbfOIpOutMonDestBbfDropCount_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 6, 1, 5),
    _NtcBbfOIpOutMonDestBbfDropCount_Type()
)
ntcBbfOIpOutMonDestBbfDropCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestBbfDropCount.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonDestBbfDropCount.setUnits("frames")
_NtcBbfOIpOutMonInvalFramTable_Object = MibTable
ntcBbfOIpOutMonInvalFramTable = _NtcBbfOIpOutMonInvalFramTable_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 7)
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonInvalFramTable.setStatus("current")
_NtcBbfOIpOutMonInvalFramEntry_Object = MibTableRow
ntcBbfOIpOutMonInvalFramEntry = _NtcBbfOIpOutMonInvalFramEntry_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 7, 1)
)
ntcBbfOIpOutMonInvalFramEntry.setIndexNames(
    (0, "NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonInvalFramDemodId"),
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonInvalFramEntry.setStatus("current")


class _NtcBbfOIpOutMonInvalFramDemodId_Type(Integer32):
    """Custom type ntcBbfOIpOutMonInvalFramDemodId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("demod1", 1),
          ("demod2", 2),
          ("demod3", 3))
    )


_NtcBbfOIpOutMonInvalFramDemodId_Type.__name__ = "Integer32"
_NtcBbfOIpOutMonInvalFramDemodId_Object = MibTableColumn
ntcBbfOIpOutMonInvalFramDemodId = _NtcBbfOIpOutMonInvalFramDemodId_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 7, 1, 1),
    _NtcBbfOIpOutMonInvalFramDemodId_Type()
)
ntcBbfOIpOutMonInvalFramDemodId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonInvalFramDemodId.setStatus("current")
_NtcBbfOIpOutMonInvalCrc8_Type = Counter32
_NtcBbfOIpOutMonInvalCrc8_Object = MibTableColumn
ntcBbfOIpOutMonInvalCrc8 = _NtcBbfOIpOutMonInvalCrc8_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 7, 1, 2),
    _NtcBbfOIpOutMonInvalCrc8_Type()
)
ntcBbfOIpOutMonInvalCrc8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonInvalCrc8.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonInvalCrc8.setUnits("frames")
_NtcBbfOIpOutMonInvalPadd_Type = Counter32
_NtcBbfOIpOutMonInvalPadd_Object = MibTableColumn
ntcBbfOIpOutMonInvalPadd = _NtcBbfOIpOutMonInvalPadd_Object(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 1, 4, 7, 1, 3),
    _NtcBbfOIpOutMonInvalPadd_Type()
)
ntcBbfOIpOutMonInvalPadd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonInvalPadd.setStatus("current")
if mibBuilder.loadTexts:
    ntcBbfOIpOutMonInvalPadd.setUnits("frames")
_NtcBbfOIpOutConformance_ObjectIdentity = ObjectIdentity
ntcBbfOIpOutConformance = _NtcBbfOIpOutConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 2)
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutConformance.setStatus("current")
_NtcBbfOIpOutConfCompliance_ObjectIdentity = ObjectIdentity
ntcBbfOIpOutConfCompliance = _NtcBbfOIpOutConfCompliance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 2, 1)
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutConfCompliance.setStatus("current")
_NtcBbfOIpOutConfGroup_ObjectIdentity = ObjectIdentity
ntcBbfOIpOutConfGroup = _NtcBbfOIpOutConfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 2, 2)
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutConfGroup.setStatus("current")

# Managed Objects groups

ntcBbfOIpOutConfGrpV1Standard = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 2, 2, 1)
)
ntcBbfOIpOutConfGrpV1Standard.setObjects(
      *(("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutEnable"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutOutputSelection"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutBbfOutEnable"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutDestinationIpAddress"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutDestinationUdpPort"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutPassInvalidFrames"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutEncapProt"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonReset"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonOutputBbfBitRate"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonBbfInCount"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonBbfOutCount"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonBbfDropCount"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonDestBitRate"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonDestBbfInCount"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonDestBbfOutCount"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonDestBbfDropCount"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonInvalCrc8"),
        ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutMonInvalPadd"))
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutConfGrpV1Standard.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ntcBbfOIpOutConfCompV1Standard = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 5835, 5, 2, 1300, 2, 1, 1)
)
ntcBbfOIpOutConfCompV1Standard.setObjects(
    ("NEWTEC-BBFOVERIPOUT-MIB", "ntcBbfOIpOutConfGrpV1Standard")
)
if mibBuilder.loadTexts:
    ntcBbfOIpOutConfCompV1Standard.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NEWTEC-BBFOVERIPOUT-MIB",
    **{"ntcBbfOverIpOut": ntcBbfOverIpOut,
       "ntcBbfOIpOutObjects": ntcBbfOIpOutObjects,
       "ntcBbfOIpOutEnable": ntcBbfOIpOutEnable,
       "ntcBbfOIpOutOutputSelection": ntcBbfOIpOutOutputSelection,
       "ntcBbfOIpOutDestinationsTable": ntcBbfOIpOutDestinationsTable,
       "ntcBbfOIpOutDestinationsEntry": ntcBbfOIpOutDestinationsEntry,
       "ntcBbfOIpOutDestinationsDemodId": ntcBbfOIpOutDestinationsDemodId,
       "ntcBbfOIpOutBbfOutEnable": ntcBbfOIpOutBbfOutEnable,
       "ntcBbfOIpOutDestinationIpAddress": ntcBbfOIpOutDestinationIpAddress,
       "ntcBbfOIpOutDestinationUdpPort": ntcBbfOIpOutDestinationUdpPort,
       "ntcBbfOIpOutPassInvalidFrames": ntcBbfOIpOutPassInvalidFrames,
       "ntcBbfOIpOutEncapProt": ntcBbfOIpOutEncapProt,
       "ntcBbfOIpOutMonitor": ntcBbfOIpOutMonitor,
       "ntcBbfOIpOutMonReset": ntcBbfOIpOutMonReset,
       "ntcBbfOIpOutMonOutputBbfBitRate": ntcBbfOIpOutMonOutputBbfBitRate,
       "ntcBbfOIpOutMonBbfInCount": ntcBbfOIpOutMonBbfInCount,
       "ntcBbfOIpOutMonBbfOutCount": ntcBbfOIpOutMonBbfOutCount,
       "ntcBbfOIpOutMonBbfDropCount": ntcBbfOIpOutMonBbfDropCount,
       "ntcBbfOIpOutMonDestTable": ntcBbfOIpOutMonDestTable,
       "ntcBbfOIpOutMonDestEntry": ntcBbfOIpOutMonDestEntry,
       "ntcBbfOIpOutMonDestDemodId": ntcBbfOIpOutMonDestDemodId,
       "ntcBbfOIpOutMonDestBitRate": ntcBbfOIpOutMonDestBitRate,
       "ntcBbfOIpOutMonDestBbfInCount": ntcBbfOIpOutMonDestBbfInCount,
       "ntcBbfOIpOutMonDestBbfOutCount": ntcBbfOIpOutMonDestBbfOutCount,
       "ntcBbfOIpOutMonDestBbfDropCount": ntcBbfOIpOutMonDestBbfDropCount,
       "ntcBbfOIpOutMonInvalFramTable": ntcBbfOIpOutMonInvalFramTable,
       "ntcBbfOIpOutMonInvalFramEntry": ntcBbfOIpOutMonInvalFramEntry,
       "ntcBbfOIpOutMonInvalFramDemodId": ntcBbfOIpOutMonInvalFramDemodId,
       "ntcBbfOIpOutMonInvalCrc8": ntcBbfOIpOutMonInvalCrc8,
       "ntcBbfOIpOutMonInvalPadd": ntcBbfOIpOutMonInvalPadd,
       "ntcBbfOIpOutConformance": ntcBbfOIpOutConformance,
       "ntcBbfOIpOutConfCompliance": ntcBbfOIpOutConfCompliance,
       "ntcBbfOIpOutConfCompV1Standard": ntcBbfOIpOutConfCompV1Standard,
       "ntcBbfOIpOutConfGroup": ntcBbfOIpOutConfGroup,
       "ntcBbfOIpOutConfGrpV1Standard": ntcBbfOIpOutConfGrpV1Standard}
)
