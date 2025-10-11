# SNMP MIB module (OA-ETHERNET-OAM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mrv/OA-ETHERNET-OAM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:05:12 2025
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

(MepList,
 nbSwitchG1Il) = mibBuilder.importSymbols(
    "OS-COMMON-TC-MIB",
    "MepList",
    "nbSwitchG1Il")

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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nbEthOam = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17)
)
if mibBuilder.loadTexts:
    nbEthOam.setRevisions(
        ("2018-12-30 00:00",
         "2013-02-18 00:00",
         "2012-10-21 00:00",
         "2012-04-15 00:00",
         "2011-09-22 00:00",
         "2011-05-30 00:00",
         "2010-03-15 00:00",
         "2007-01-07 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NbEthOamMepId(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )



class NbEthOamMepIdOrZero(TextualConvention, Unsigned32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4095),
    )



class TestRunMethod(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("slow", 2),
          ("fast", 3),
          ("none", 4))
    )



class NbEthOamCcmHighestDefectPri(TextualConvention, Integer32):
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
          ("defRDICCM", 1),
          ("defMACstatus", 2),
          ("defRemoteCCM", 3),
          ("defErrorCCM", 4),
          ("defXconCCM", 5))
    )



class DestinationType(TextualConvention, Integer32):
    status = "current"
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
        *(("singleRMepId", 1),
          ("macAddress", 2),
          ("listOfRMeps", 3),
          ("multicastClass1", 4),
          ("multicastClass2", 5))
    )



# MIB Managed Objects in the order of their OIDs

_NbEthOamNotifications_ObjectIdentity = ObjectIdentity
nbEthOamNotifications = _NbEthOamNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 0)
)
_NbEthOamCapabilities_ObjectIdentity = ObjectIdentity
nbEthOamCapabilities = _NbEthOamCapabilities_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 1)
)


class _NbEthOamFeaturesSupport_Type(Bits):
    """Custom type nbEthOamFeaturesSupport based on Bits"""
    namedValues = NamedValues(
        *(("mayDoSlowTests", 0),
          ("mayDoFastTests", 1))
    )

_NbEthOamFeaturesSupport_Type.__name__ = "Bits"
_NbEthOamFeaturesSupport_Object = MibScalar
nbEthOamFeaturesSupport = _NbEthOamFeaturesSupport_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 1, 1),
    _NbEthOamFeaturesSupport_Type()
)
nbEthOamFeaturesSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamFeaturesSupport.setStatus("current")


class _NbEthOamCcmIntervals_Type(Bits):
    """Custom type nbEthOamCcmIntervals based on Bits"""
    namedValues = NamedValues(
        *(("supports300Hz", 0),
          ("supports10ms", 1),
          ("supports100ms", 2),
          ("supports1s", 3),
          ("supports10s", 4),
          ("supports1min", 5),
          ("supports10min", 6))
    )

_NbEthOamCcmIntervals_Type.__name__ = "Bits"
_NbEthOamCcmIntervals_Object = MibScalar
nbEthOamCcmIntervals = _NbEthOamCcmIntervals_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 1, 2),
    _NbEthOamCcmIntervals_Type()
)
nbEthOamCcmIntervals.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamCcmIntervals.setStatus("current")
_NbEthOamLb_ObjectIdentity = ObjectIdentity
nbEthOamLb = _NbEthOamLb_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10)
)
_NbEthOamLbConfTable_Object = MibTable
nbEthOamLbConfTable = _NbEthOamLbConfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1)
)
if mibBuilder.loadTexts:
    nbEthOamLbConfTable.setStatus("current")
_NbEthOamLbConfEntry_Object = MibTableRow
nbEthOamLbConfEntry = _NbEthOamLbConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1)
)
nbEthOamLbConfEntry.setIndexNames(
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMdIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMaIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMepIdentifier"),
)
if mibBuilder.loadTexts:
    nbEthOamLbConfEntry.setStatus("current")


class _NbEthOamMdIndex_Type(Unsigned32):
    """Custom type nbEthOamMdIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_NbEthOamMdIndex_Type.__name__ = "Unsigned32"
_NbEthOamMdIndex_Object = MibTableColumn
nbEthOamMdIndex = _NbEthOamMdIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 1),
    _NbEthOamMdIndex_Type()
)
nbEthOamMdIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbEthOamMdIndex.setStatus("current")


class _NbEthOamMaIndex_Type(Unsigned32):
    """Custom type nbEthOamMaIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NbEthOamMaIndex_Type.__name__ = "Unsigned32"
_NbEthOamMaIndex_Object = MibTableColumn
nbEthOamMaIndex = _NbEthOamMaIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 2),
    _NbEthOamMaIndex_Type()
)
nbEthOamMaIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbEthOamMaIndex.setStatus("current")
_NbEthOamMepIdentifier_Type = NbEthOamMepId
_NbEthOamMepIdentifier_Object = MibTableColumn
nbEthOamMepIdentifier = _NbEthOamMepIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 3),
    _NbEthOamMepIdentifier_Type()
)
nbEthOamMepIdentifier.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbEthOamMepIdentifier.setStatus("current")


class _NbEthOamLbConfHistorySize_Type(Unsigned32):
    """Custom type nbEthOamLbConfHistorySize based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_NbEthOamLbConfHistorySize_Type.__name__ = "Unsigned32"
_NbEthOamLbConfHistorySize_Object = MibTableColumn
nbEthOamLbConfHistorySize = _NbEthOamLbConfHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 5),
    _NbEthOamLbConfHistorySize_Type()
)
nbEthOamLbConfHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbConfHistorySize.setUnits("lines")


class _NbEthOamLbConfInterval_Type(Unsigned32):
    """Custom type nbEthOamLbConfInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NbEthOamLbConfInterval_Type.__name__ = "Unsigned32"
_NbEthOamLbConfInterval_Object = MibTableColumn
nbEthOamLbConfInterval = _NbEthOamLbConfInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 6),
    _NbEthOamLbConfInterval_Type()
)
nbEthOamLbConfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfInterval.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbConfInterval.setUnits("milliseconds")


class _NbEthOamLbConfTimeout_Type(Unsigned32):
    """Custom type nbEthOamLbConfTimeout based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_NbEthOamLbConfTimeout_Type.__name__ = "Unsigned32"
_NbEthOamLbConfTimeout_Object = MibTableColumn
nbEthOamLbConfTimeout = _NbEthOamLbConfTimeout_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 7),
    _NbEthOamLbConfTimeout_Type()
)
nbEthOamLbConfTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfTimeout.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbConfTimeout.setUnits("milliseconds")


class _NbEthOamLbConfDataLength_Type(Unsigned32):
    """Custom type nbEthOamLbConfDataLength based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 9000),
    )


_NbEthOamLbConfDataLength_Type.__name__ = "Unsigned32"
_NbEthOamLbConfDataLength_Object = MibTableColumn
nbEthOamLbConfDataLength = _NbEthOamLbConfDataLength_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 8),
    _NbEthOamLbConfDataLength_Type()
)
nbEthOamLbConfDataLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfDataLength.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbConfDataLength.setUnits("octets")


class _NbEthOamLbConfDataFill_Type(OctetString):
    """Custom type nbEthOamLbConfDataFill based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1436),
    )


_NbEthOamLbConfDataFill_Type.__name__ = "OctetString"
_NbEthOamLbConfDataFill_Object = MibTableColumn
nbEthOamLbConfDataFill = _NbEthOamLbConfDataFill_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 9),
    _NbEthOamLbConfDataFill_Type()
)
nbEthOamLbConfDataFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfDataFill.setStatus("current")


class _NbEthOamLbConfPriority_Type(Unsigned32):
    """Custom type nbEthOamLbConfPriority based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(8, 8),
    )


_NbEthOamLbConfPriority_Type.__name__ = "Unsigned32"
_NbEthOamLbConfPriority_Object = MibTableColumn
nbEthOamLbConfPriority = _NbEthOamLbConfPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 10),
    _NbEthOamLbConfPriority_Type()
)
nbEthOamLbConfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfPriority.setStatus("current")
_NbEthOamLbConfDestMepId_Type = NbEthOamMepIdOrZero
_NbEthOamLbConfDestMepId_Object = MibTableColumn
nbEthOamLbConfDestMepId = _NbEthOamLbConfDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 11),
    _NbEthOamLbConfDestMepId_Type()
)
nbEthOamLbConfDestMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfDestMepId.setStatus("current")
_NbEthOamLbConfDestMepMac_Type = MacAddress
_NbEthOamLbConfDestMepMac_Object = MibTableColumn
nbEthOamLbConfDestMepMac = _NbEthOamLbConfDestMepMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 12),
    _NbEthOamLbConfDestMepMac_Type()
)
nbEthOamLbConfDestMepMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfDestMepMac.setStatus("current")


class _NbEthOamLbConfDestIsMepId_Type(DestinationType):
    """Custom type nbEthOamLbConfDestIsMepId based on DestinationType"""
    defaultValue = 2


_NbEthOamLbConfDestIsMepId_Type.__name__ = "DestinationType"
_NbEthOamLbConfDestIsMepId_Object = MibTableColumn
nbEthOamLbConfDestIsMepId = _NbEthOamLbConfDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 13),
    _NbEthOamLbConfDestIsMepId_Type()
)
nbEthOamLbConfDestIsMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfDestIsMepId.setStatus("current")


class _NbEthOamLbConfMessages_Type(Unsigned32):
    """Custom type nbEthOamLbConfMessages based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_NbEthOamLbConfMessages_Type.__name__ = "Unsigned32"
_NbEthOamLbConfMessages_Object = MibTableColumn
nbEthOamLbConfMessages = _NbEthOamLbConfMessages_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 14),
    _NbEthOamLbConfMessages_Type()
)
nbEthOamLbConfMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfMessages.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbConfMessages.setUnits("packets")


class _NbEthOamLbConfBurstInterval_Type(Unsigned32):
    """Custom type nbEthOamLbConfBurstInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_NbEthOamLbConfBurstInterval_Type.__name__ = "Unsigned32"
_NbEthOamLbConfBurstInterval_Object = MibTableColumn
nbEthOamLbConfBurstInterval = _NbEthOamLbConfBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 15),
    _NbEthOamLbConfBurstInterval_Type()
)
nbEthOamLbConfBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfBurstInterval.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbConfBurstInterval.setUnits("seconds")


class _NbEthOamLbConfNumberOfBursts_Type(Unsigned32):
    """Custom type nbEthOamLbConfNumberOfBursts based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_NbEthOamLbConfNumberOfBursts_Type.__name__ = "Unsigned32"
_NbEthOamLbConfNumberOfBursts_Object = MibTableColumn
nbEthOamLbConfNumberOfBursts = _NbEthOamLbConfNumberOfBursts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 16),
    _NbEthOamLbConfNumberOfBursts_Type()
)
nbEthOamLbConfNumberOfBursts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfNumberOfBursts.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbConfNumberOfBursts.setUnits("bursts")


class _NbEthOamLbConfRunMethod_Type(TestRunMethod):
    """Custom type nbEthOamLbConfRunMethod based on TestRunMethod"""
    defaultValue = 4


_NbEthOamLbConfRunMethod_Type.__name__ = "TestRunMethod"
_NbEthOamLbConfRunMethod_Object = MibTableColumn
nbEthOamLbConfRunMethod = _NbEthOamLbConfRunMethod_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 21),
    _NbEthOamLbConfRunMethod_Type()
)
nbEthOamLbConfRunMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfRunMethod.setStatus("current")


class _NbEthOamLbConfIntervalMicro_Type(Unsigned32):
    """Custom type nbEthOamLbConfIntervalMicro based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_NbEthOamLbConfIntervalMicro_Type.__name__ = "Unsigned32"
_NbEthOamLbConfIntervalMicro_Object = MibTableColumn
nbEthOamLbConfIntervalMicro = _NbEthOamLbConfIntervalMicro_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 1, 1, 22),
    _NbEthOamLbConfIntervalMicro_Type()
)
nbEthOamLbConfIntervalMicro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfIntervalMicro.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbConfIntervalMicro.setUnits("microseconds")
_NbEthOamLbHistTable_Object = MibTable
nbEthOamLbHistTable = _NbEthOamLbHistTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2)
)
if mibBuilder.loadTexts:
    nbEthOamLbHistTable.setStatus("current")
_NbEthOamLbHistEntry_Object = MibTableRow
nbEthOamLbHistEntry = _NbEthOamLbHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1)
)
nbEthOamLbHistEntry.setIndexNames(
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMdIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMaIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMepIdentifier"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamLbHistSampleIndex"),
)
if mibBuilder.loadTexts:
    nbEthOamLbHistEntry.setStatus("current")


class _NbEthOamLbHistSampleIndex_Type(Unsigned32):
    """Custom type nbEthOamLbHistSampleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NbEthOamLbHistSampleIndex_Type.__name__ = "Unsigned32"
_NbEthOamLbHistSampleIndex_Object = MibTableColumn
nbEthOamLbHistSampleIndex = _NbEthOamLbHistSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 5),
    _NbEthOamLbHistSampleIndex_Type()
)
nbEthOamLbHistSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbEthOamLbHistSampleIndex.setStatus("current")
_NbEthOamLbHistStarted_Type = DateAndTime
_NbEthOamLbHistStarted_Object = MibTableColumn
nbEthOamLbHistStarted = _NbEthOamLbHistStarted_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 6),
    _NbEthOamLbHistStarted_Type()
)
nbEthOamLbHistStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistStarted.setStatus("current")
_NbEthOamLbHistDestMepId_Type = NbEthOamMepIdOrZero
_NbEthOamLbHistDestMepId_Object = MibTableColumn
nbEthOamLbHistDestMepId = _NbEthOamLbHistDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 7),
    _NbEthOamLbHistDestMepId_Type()
)
nbEthOamLbHistDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistDestMepId.setStatus("current")
_NbEthOamLbHistDestMepMac_Type = MacAddress
_NbEthOamLbHistDestMepMac_Object = MibTableColumn
nbEthOamLbHistDestMepMac = _NbEthOamLbHistDestMepMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 8),
    _NbEthOamLbHistDestMepMac_Type()
)
nbEthOamLbHistDestMepMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistDestMepMac.setStatus("current")
_NbEthOamLbHistMsgTransmitted_Type = Unsigned32
_NbEthOamLbHistMsgTransmitted_Object = MibTableColumn
nbEthOamLbHistMsgTransmitted = _NbEthOamLbHistMsgTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 9),
    _NbEthOamLbHistMsgTransmitted_Type()
)
nbEthOamLbHistMsgTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistMsgTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistMsgTransmitted.setUnits("packets")
_NbEthOamLbHistMsgReceived_Type = Unsigned32
_NbEthOamLbHistMsgReceived_Object = MibTableColumn
nbEthOamLbHistMsgReceived = _NbEthOamLbHistMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 10),
    _NbEthOamLbHistMsgReceived_Type()
)
nbEthOamLbHistMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistMsgReceived.setUnits("packets")
_NbEthOamLbHistRttMin_Type = Unsigned32
_NbEthOamLbHistRttMin_Object = MibTableColumn
nbEthOamLbHistRttMin = _NbEthOamLbHistRttMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 12),
    _NbEthOamLbHistRttMin_Type()
)
nbEthOamLbHistRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistRttMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistRttMin.setUnits("microseconds")
_NbEthOamLbHistRttMax_Type = Unsigned32
_NbEthOamLbHistRttMax_Object = MibTableColumn
nbEthOamLbHistRttMax = _NbEthOamLbHistRttMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 13),
    _NbEthOamLbHistRttMax_Type()
)
nbEthOamLbHistRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistRttMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistRttMax.setUnits("microseconds")
_NbEthOamLbHistRttAverage_Type = Unsigned32
_NbEthOamLbHistRttAverage_Object = MibTableColumn
nbEthOamLbHistRttAverage = _NbEthOamLbHistRttAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 14),
    _NbEthOamLbHistRttAverage_Type()
)
nbEthOamLbHistRttAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistRttAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistRttAverage.setUnits("microseconds")
_NbEthOamLbHistRttSum2_Type = Unsigned32
_NbEthOamLbHistRttSum2_Object = MibTableColumn
nbEthOamLbHistRttSum2 = _NbEthOamLbHistRttSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 15),
    _NbEthOamLbHistRttSum2_Type()
)
nbEthOamLbHistRttSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistRttSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistRttSum2.setUnits("square of milliseconds")
_NbEthOamLbHistJittNumber_Type = Unsigned32
_NbEthOamLbHistJittNumber_Object = MibTableColumn
nbEthOamLbHistJittNumber = _NbEthOamLbHistJittNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 23),
    _NbEthOamLbHistJittNumber_Type()
)
nbEthOamLbHistJittNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittNumber.setStatus("current")
_NbEthOamLbHistJittMin_Type = Unsigned32
_NbEthOamLbHistJittMin_Object = MibTableColumn
nbEthOamLbHistJittMin = _NbEthOamLbHistJittMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 24),
    _NbEthOamLbHistJittMin_Type()
)
nbEthOamLbHistJittMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittMin.setUnits("microseconds")
_NbEthOamLbHistJittMax_Type = Unsigned32
_NbEthOamLbHistJittMax_Object = MibTableColumn
nbEthOamLbHistJittMax = _NbEthOamLbHistJittMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 25),
    _NbEthOamLbHistJittMax_Type()
)
nbEthOamLbHistJittMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittMax.setUnits("microseconds")
_NbEthOamLbHistJittAverage_Type = Unsigned32
_NbEthOamLbHistJittAverage_Object = MibTableColumn
nbEthOamLbHistJittAverage = _NbEthOamLbHistJittAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 26),
    _NbEthOamLbHistJittAverage_Type()
)
nbEthOamLbHistJittAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittAverage.setUnits("microseconds")
_NbEthOamLbHistJittSum2_Type = Unsigned32
_NbEthOamLbHistJittSum2_Object = MibTableColumn
nbEthOamLbHistJittSum2 = _NbEthOamLbHistJittSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 27),
    _NbEthOamLbHistJittSum2_Type()
)
nbEthOamLbHistJittSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittSum2.setUnits("square of milliseconds")
_NbEthOamLbHistJittIA_Type = Unsigned32
_NbEthOamLbHistJittIA_Object = MibTableColumn
nbEthOamLbHistJittIA = _NbEthOamLbHistJittIA_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 30),
    _NbEthOamLbHistJittIA_Type()
)
nbEthOamLbHistJittIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittIA.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistJittIA.setUnits("microseconds")
_NbEthOamLbHistPcktLoss_Type = Unsigned32
_NbEthOamLbHistPcktLoss_Object = MibTableColumn
nbEthOamLbHistPcktLoss = _NbEthOamLbHistPcktLoss_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 31),
    _NbEthOamLbHistPcktLoss_Type()
)
nbEthOamLbHistPcktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistPcktLoss.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbHistPcktLoss.setUnits("0.01%")
_NbEthOamLbHistType_Type = TestRunMethod
_NbEthOamLbHistType_Object = MibTableColumn
nbEthOamLbHistType = _NbEthOamLbHistType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 32),
    _NbEthOamLbHistType_Type()
)
nbEthOamLbHistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistType.setStatus("current")


class _NbEthOamLbHistPriority_Type(Unsigned32):
    """Custom type nbEthOamLbHistPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbEthOamLbHistPriority_Type.__name__ = "Unsigned32"
_NbEthOamLbHistPriority_Object = MibTableColumn
nbEthOamLbHistPriority = _NbEthOamLbHistPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 2, 1, 33),
    _NbEthOamLbHistPriority_Type()
)
nbEthOamLbHistPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbHistPriority.setStatus("current")
_NbEthOamLbLastTable_Object = MibTable
nbEthOamLbLastTable = _NbEthOamLbLastTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3)
)
if mibBuilder.loadTexts:
    nbEthOamLbLastTable.setStatus("current")
_NbEthOamLbLastEntry_Object = MibTableRow
nbEthOamLbLastEntry = _NbEthOamLbLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1)
)
nbEthOamLbLastEntry.setIndexNames(
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMdIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMaIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMepIdentifier"),
)
if mibBuilder.loadTexts:
    nbEthOamLbLastEntry.setStatus("current")
_NbEthOamLbLastStarted_Type = DateAndTime
_NbEthOamLbLastStarted_Object = MibTableColumn
nbEthOamLbLastStarted = _NbEthOamLbLastStarted_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 6),
    _NbEthOamLbLastStarted_Type()
)
nbEthOamLbLastStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastStarted.setStatus("current")
_NbEthOamLbLastDestMepId_Type = NbEthOamMepIdOrZero
_NbEthOamLbLastDestMepId_Object = MibTableColumn
nbEthOamLbLastDestMepId = _NbEthOamLbLastDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 7),
    _NbEthOamLbLastDestMepId_Type()
)
nbEthOamLbLastDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastDestMepId.setStatus("current")
_NbEthOamLbLastDestMepMac_Type = MacAddress
_NbEthOamLbLastDestMepMac_Object = MibTableColumn
nbEthOamLbLastDestMepMac = _NbEthOamLbLastDestMepMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 8),
    _NbEthOamLbLastDestMepMac_Type()
)
nbEthOamLbLastDestMepMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastDestMepMac.setStatus("current")
_NbEthOamLbLastMsgTransmitted_Type = Unsigned32
_NbEthOamLbLastMsgTransmitted_Object = MibTableColumn
nbEthOamLbLastMsgTransmitted = _NbEthOamLbLastMsgTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 9),
    _NbEthOamLbLastMsgTransmitted_Type()
)
nbEthOamLbLastMsgTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastMsgTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastMsgTransmitted.setUnits("packets")
_NbEthOamLbLastMsgReceived_Type = Unsigned32
_NbEthOamLbLastMsgReceived_Object = MibTableColumn
nbEthOamLbLastMsgReceived = _NbEthOamLbLastMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 10),
    _NbEthOamLbLastMsgReceived_Type()
)
nbEthOamLbLastMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastMsgReceived.setUnits("packets")
_NbEthOamLbLastRttMin_Type = Unsigned32
_NbEthOamLbLastRttMin_Object = MibTableColumn
nbEthOamLbLastRttMin = _NbEthOamLbLastRttMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 12),
    _NbEthOamLbLastRttMin_Type()
)
nbEthOamLbLastRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastRttMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastRttMin.setUnits("microseconds")
_NbEthOamLbLastRttMax_Type = Unsigned32
_NbEthOamLbLastRttMax_Object = MibTableColumn
nbEthOamLbLastRttMax = _NbEthOamLbLastRttMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 13),
    _NbEthOamLbLastRttMax_Type()
)
nbEthOamLbLastRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastRttMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastRttMax.setUnits("microseconds")
_NbEthOamLbLastRttAverage_Type = Unsigned32
_NbEthOamLbLastRttAverage_Object = MibTableColumn
nbEthOamLbLastRttAverage = _NbEthOamLbLastRttAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 14),
    _NbEthOamLbLastRttAverage_Type()
)
nbEthOamLbLastRttAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastRttAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastRttAverage.setUnits("microseconds")
_NbEthOamLbLastRttSum2_Type = Unsigned32
_NbEthOamLbLastRttSum2_Object = MibTableColumn
nbEthOamLbLastRttSum2 = _NbEthOamLbLastRttSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 15),
    _NbEthOamLbLastRttSum2_Type()
)
nbEthOamLbLastRttSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastRttSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastRttSum2.setUnits("square of milliseconds")
_NbEthOamLbLastJittNumber_Type = Unsigned32
_NbEthOamLbLastJittNumber_Object = MibTableColumn
nbEthOamLbLastJittNumber = _NbEthOamLbLastJittNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 23),
    _NbEthOamLbLastJittNumber_Type()
)
nbEthOamLbLastJittNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittNumber.setStatus("current")
_NbEthOamLbLastJittMin_Type = Unsigned32
_NbEthOamLbLastJittMin_Object = MibTableColumn
nbEthOamLbLastJittMin = _NbEthOamLbLastJittMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 24),
    _NbEthOamLbLastJittMin_Type()
)
nbEthOamLbLastJittMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittMin.setUnits("microseconds")
_NbEthOamLbLastJittMax_Type = Unsigned32
_NbEthOamLbLastJittMax_Object = MibTableColumn
nbEthOamLbLastJittMax = _NbEthOamLbLastJittMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 25),
    _NbEthOamLbLastJittMax_Type()
)
nbEthOamLbLastJittMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittMax.setUnits("microseconds")
_NbEthOamLbLastJittAverage_Type = Unsigned32
_NbEthOamLbLastJittAverage_Object = MibTableColumn
nbEthOamLbLastJittAverage = _NbEthOamLbLastJittAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 26),
    _NbEthOamLbLastJittAverage_Type()
)
nbEthOamLbLastJittAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittAverage.setUnits("microseconds")
_NbEthOamLbLastJittSum2_Type = Unsigned32
_NbEthOamLbLastJittSum2_Object = MibTableColumn
nbEthOamLbLastJittSum2 = _NbEthOamLbLastJittSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 27),
    _NbEthOamLbLastJittSum2_Type()
)
nbEthOamLbLastJittSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittSum2.setUnits("square of milliseconds")
_NbEthOamLbLastJittIA_Type = Unsigned32
_NbEthOamLbLastJittIA_Object = MibTableColumn
nbEthOamLbLastJittIA = _NbEthOamLbLastJittIA_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 30),
    _NbEthOamLbLastJittIA_Type()
)
nbEthOamLbLastJittIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittIA.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastJittIA.setUnits("microseconds")
_NbEthOamLbLastPcktLoss_Type = Unsigned32
_NbEthOamLbLastPcktLoss_Object = MibTableColumn
nbEthOamLbLastPcktLoss = _NbEthOamLbLastPcktLoss_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 31),
    _NbEthOamLbLastPcktLoss_Type()
)
nbEthOamLbLastPcktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastPcktLoss.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamLbLastPcktLoss.setUnits("0.01%")
_NbEthOamLbLastType_Type = TestRunMethod
_NbEthOamLbLastType_Object = MibTableColumn
nbEthOamLbLastType = _NbEthOamLbLastType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 32),
    _NbEthOamLbLastType_Type()
)
nbEthOamLbLastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastType.setStatus("current")


class _NbEthOamLbLastPriority_Type(Unsigned32):
    """Custom type nbEthOamLbLastPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbEthOamLbLastPriority_Type.__name__ = "Unsigned32"
_NbEthOamLbLastPriority_Object = MibTableColumn
nbEthOamLbLastPriority = _NbEthOamLbLastPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 33),
    _NbEthOamLbLastPriority_Type()
)
nbEthOamLbLastPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastPriority.setStatus("current")
_NbEthOamLbLastHistIndx_Type = Unsigned32
_NbEthOamLbLastHistIndx_Object = MibTableColumn
nbEthOamLbLastHistIndx = _NbEthOamLbLastHistIndx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 3, 1, 50),
    _NbEthOamLbLastHistIndx_Type()
)
nbEthOamLbLastHistIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamLbLastHistIndx.setStatus("current")
_NbEthOamLbConfExtTable_Object = MibTable
nbEthOamLbConfExtTable = _NbEthOamLbConfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 4)
)
if mibBuilder.loadTexts:
    nbEthOamLbConfExtTable.setStatus("current")
_NbEthOamLbConfExtEntry_Object = MibTableRow
nbEthOamLbConfExtEntry = _NbEthOamLbConfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 4, 1)
)
if mibBuilder.loadTexts:
    nbEthOamLbConfExtEntry.setStatus("current")
_NbEthOamLbConfDestMepList_Type = MepList
_NbEthOamLbConfDestMepList_Object = MibTableColumn
nbEthOamLbConfDestMepList = _NbEthOamLbConfDestMepList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 10, 4, 1, 12),
    _NbEthOamLbConfDestMepList_Type()
)
nbEthOamLbConfDestMepList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamLbConfDestMepList.setStatus("current")
_NbEthOamDm_ObjectIdentity = ObjectIdentity
nbEthOamDm = _NbEthOamDm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11)
)
_NbEthOamDmConfTable_Object = MibTable
nbEthOamDmConfTable = _NbEthOamDmConfTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1)
)
if mibBuilder.loadTexts:
    nbEthOamDmConfTable.setStatus("current")
_NbEthOamDmConfEntry_Object = MibTableRow
nbEthOamDmConfEntry = _NbEthOamDmConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1)
)
nbEthOamDmConfEntry.setIndexNames(
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMdIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMaIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMepIdentifier"),
)
if mibBuilder.loadTexts:
    nbEthOamDmConfEntry.setStatus("current")


class _NbEthOamDmConfHistorySize_Type(Unsigned32):
    """Custom type nbEthOamDmConfHistorySize based on Unsigned32"""
    defaultValue = 5

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 65535),
    )


_NbEthOamDmConfHistorySize_Type.__name__ = "Unsigned32"
_NbEthOamDmConfHistorySize_Object = MibTableColumn
nbEthOamDmConfHistorySize = _NbEthOamDmConfHistorySize_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 5),
    _NbEthOamDmConfHistorySize_Type()
)
nbEthOamDmConfHistorySize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfHistorySize.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmConfHistorySize.setUnits("lines")


class _NbEthOamDmConfInterval_Type(Unsigned32):
    """Custom type nbEthOamDmConfInterval based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_NbEthOamDmConfInterval_Type.__name__ = "Unsigned32"
_NbEthOamDmConfInterval_Object = MibTableColumn
nbEthOamDmConfInterval = _NbEthOamDmConfInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 6),
    _NbEthOamDmConfInterval_Type()
)
nbEthOamDmConfInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfInterval.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmConfInterval.setUnits("milliseconds")


class _NbEthOamDmConfTimeout_Type(Unsigned32):
    """Custom type nbEthOamDmConfTimeout based on Unsigned32"""
    defaultValue = 200

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60000),
    )


_NbEthOamDmConfTimeout_Type.__name__ = "Unsigned32"
_NbEthOamDmConfTimeout_Object = MibTableColumn
nbEthOamDmConfTimeout = _NbEthOamDmConfTimeout_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 7),
    _NbEthOamDmConfTimeout_Type()
)
nbEthOamDmConfTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfTimeout.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmConfTimeout.setUnits("milliseconds")


class _NbEthOamDmConfDataLength_Type(Unsigned32):
    """Custom type nbEthOamDmConfDataLength based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 9000),
    )


_NbEthOamDmConfDataLength_Type.__name__ = "Unsigned32"
_NbEthOamDmConfDataLength_Object = MibTableColumn
nbEthOamDmConfDataLength = _NbEthOamDmConfDataLength_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 8),
    _NbEthOamDmConfDataLength_Type()
)
nbEthOamDmConfDataLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfDataLength.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmConfDataLength.setUnits("octets")


class _NbEthOamDmConfDataFill_Type(OctetString):
    """Custom type nbEthOamDmConfDataFill based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 1436),
    )


_NbEthOamDmConfDataFill_Type.__name__ = "OctetString"
_NbEthOamDmConfDataFill_Object = MibTableColumn
nbEthOamDmConfDataFill = _NbEthOamDmConfDataFill_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 9),
    _NbEthOamDmConfDataFill_Type()
)
nbEthOamDmConfDataFill.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfDataFill.setStatus("current")


class _NbEthOamDmConfPriority_Type(Unsigned32):
    """Custom type nbEthOamDmConfPriority based on Unsigned32"""
    defaultValue = 8

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
        ValueRangeConstraint(8, 8),
    )


_NbEthOamDmConfPriority_Type.__name__ = "Unsigned32"
_NbEthOamDmConfPriority_Object = MibTableColumn
nbEthOamDmConfPriority = _NbEthOamDmConfPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 10),
    _NbEthOamDmConfPriority_Type()
)
nbEthOamDmConfPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfPriority.setStatus("current")
_NbEthOamDmConfDestMepId_Type = NbEthOamMepIdOrZero
_NbEthOamDmConfDestMepId_Object = MibTableColumn
nbEthOamDmConfDestMepId = _NbEthOamDmConfDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 11),
    _NbEthOamDmConfDestMepId_Type()
)
nbEthOamDmConfDestMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfDestMepId.setStatus("current")
_NbEthOamDmConfDestMepMac_Type = MacAddress
_NbEthOamDmConfDestMepMac_Object = MibTableColumn
nbEthOamDmConfDestMepMac = _NbEthOamDmConfDestMepMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 12),
    _NbEthOamDmConfDestMepMac_Type()
)
nbEthOamDmConfDestMepMac.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfDestMepMac.setStatus("current")


class _NbEthOamDmConfDestIsMepId_Type(DestinationType):
    """Custom type nbEthOamDmConfDestIsMepId based on DestinationType"""
    defaultValue = 2


_NbEthOamDmConfDestIsMepId_Type.__name__ = "DestinationType"
_NbEthOamDmConfDestIsMepId_Object = MibTableColumn
nbEthOamDmConfDestIsMepId = _NbEthOamDmConfDestIsMepId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 13),
    _NbEthOamDmConfDestIsMepId_Type()
)
nbEthOamDmConfDestIsMepId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfDestIsMepId.setStatus("current")


class _NbEthOamDmConfMessages_Type(Unsigned32):
    """Custom type nbEthOamDmConfMessages based on Unsigned32"""
    defaultValue = 3

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_NbEthOamDmConfMessages_Type.__name__ = "Unsigned32"
_NbEthOamDmConfMessages_Object = MibTableColumn
nbEthOamDmConfMessages = _NbEthOamDmConfMessages_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 14),
    _NbEthOamDmConfMessages_Type()
)
nbEthOamDmConfMessages.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfMessages.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmConfMessages.setUnits("packets")


class _NbEthOamDmConfBurstInterval_Type(Unsigned32):
    """Custom type nbEthOamDmConfBurstInterval based on Unsigned32"""
    defaultValue = 60

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 86400),
    )


_NbEthOamDmConfBurstInterval_Type.__name__ = "Unsigned32"
_NbEthOamDmConfBurstInterval_Object = MibTableColumn
nbEthOamDmConfBurstInterval = _NbEthOamDmConfBurstInterval_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 15),
    _NbEthOamDmConfBurstInterval_Type()
)
nbEthOamDmConfBurstInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfBurstInterval.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmConfBurstInterval.setUnits("seconds")


class _NbEthOamDmConfNumberOfBursts_Type(Unsigned32):
    """Custom type nbEthOamDmConfNumberOfBursts based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 4294967295),
    )


_NbEthOamDmConfNumberOfBursts_Type.__name__ = "Unsigned32"
_NbEthOamDmConfNumberOfBursts_Object = MibTableColumn
nbEthOamDmConfNumberOfBursts = _NbEthOamDmConfNumberOfBursts_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 16),
    _NbEthOamDmConfNumberOfBursts_Type()
)
nbEthOamDmConfNumberOfBursts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfNumberOfBursts.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmConfNumberOfBursts.setUnits("bursts")


class _NbEthOamDmConfRunMethod_Type(TestRunMethod):
    """Custom type nbEthOamDmConfRunMethod based on TestRunMethod"""
    defaultValue = 4


_NbEthOamDmConfRunMethod_Type.__name__ = "TestRunMethod"
_NbEthOamDmConfRunMethod_Object = MibTableColumn
nbEthOamDmConfRunMethod = _NbEthOamDmConfRunMethod_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 21),
    _NbEthOamDmConfRunMethod_Type()
)
nbEthOamDmConfRunMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfRunMethod.setStatus("current")


class _NbEthOamDmConfIntervalMicro_Type(Unsigned32):
    """Custom type nbEthOamDmConfIntervalMicro based on Unsigned32"""
    defaultValue = 100000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 1000000),
    )


_NbEthOamDmConfIntervalMicro_Type.__name__ = "Unsigned32"
_NbEthOamDmConfIntervalMicro_Object = MibTableColumn
nbEthOamDmConfIntervalMicro = _NbEthOamDmConfIntervalMicro_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 1, 1, 22),
    _NbEthOamDmConfIntervalMicro_Type()
)
nbEthOamDmConfIntervalMicro.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfIntervalMicro.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmConfIntervalMicro.setUnits("microseconds")
_NbEthOamDmHistTable_Object = MibTable
nbEthOamDmHistTable = _NbEthOamDmHistTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2)
)
if mibBuilder.loadTexts:
    nbEthOamDmHistTable.setStatus("current")
_NbEthOamDmHistEntry_Object = MibTableRow
nbEthOamDmHistEntry = _NbEthOamDmHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1)
)
nbEthOamDmHistEntry.setIndexNames(
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMdIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMaIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMepIdentifier"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamDmHistSampleIndex"),
)
if mibBuilder.loadTexts:
    nbEthOamDmHistEntry.setStatus("current")


class _NbEthOamDmHistSampleIndex_Type(Unsigned32):
    """Custom type nbEthOamDmHistSampleIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_NbEthOamDmHistSampleIndex_Type.__name__ = "Unsigned32"
_NbEthOamDmHistSampleIndex_Object = MibTableColumn
nbEthOamDmHistSampleIndex = _NbEthOamDmHistSampleIndex_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 5),
    _NbEthOamDmHistSampleIndex_Type()
)
nbEthOamDmHistSampleIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    nbEthOamDmHistSampleIndex.setStatus("current")
_NbEthOamDmHistStarted_Type = DateAndTime
_NbEthOamDmHistStarted_Object = MibTableColumn
nbEthOamDmHistStarted = _NbEthOamDmHistStarted_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 6),
    _NbEthOamDmHistStarted_Type()
)
nbEthOamDmHistStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistStarted.setStatus("current")
_NbEthOamDmHistDestMepId_Type = NbEthOamMepIdOrZero
_NbEthOamDmHistDestMepId_Object = MibTableColumn
nbEthOamDmHistDestMepId = _NbEthOamDmHistDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 7),
    _NbEthOamDmHistDestMepId_Type()
)
nbEthOamDmHistDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistDestMepId.setStatus("current")
_NbEthOamDmHistDestMepMac_Type = MacAddress
_NbEthOamDmHistDestMepMac_Object = MibTableColumn
nbEthOamDmHistDestMepMac = _NbEthOamDmHistDestMepMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 8),
    _NbEthOamDmHistDestMepMac_Type()
)
nbEthOamDmHistDestMepMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistDestMepMac.setStatus("current")
_NbEthOamDmHistMsgTransmitted_Type = Unsigned32
_NbEthOamDmHistMsgTransmitted_Object = MibTableColumn
nbEthOamDmHistMsgTransmitted = _NbEthOamDmHistMsgTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 9),
    _NbEthOamDmHistMsgTransmitted_Type()
)
nbEthOamDmHistMsgTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistMsgTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistMsgTransmitted.setUnits("frames")
_NbEthOamDmHistMsgReceived_Type = Unsigned32
_NbEthOamDmHistMsgReceived_Object = MibTableColumn
nbEthOamDmHistMsgReceived = _NbEthOamDmHistMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 10),
    _NbEthOamDmHistMsgReceived_Type()
)
nbEthOamDmHistMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistMsgReceived.setUnits("packets")
_NbEthOamDmHistRttMin_Type = Unsigned32
_NbEthOamDmHistRttMin_Object = MibTableColumn
nbEthOamDmHistRttMin = _NbEthOamDmHistRttMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 12),
    _NbEthOamDmHistRttMin_Type()
)
nbEthOamDmHistRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistRttMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistRttMin.setUnits("microseconds")
_NbEthOamDmHistRttMax_Type = Unsigned32
_NbEthOamDmHistRttMax_Object = MibTableColumn
nbEthOamDmHistRttMax = _NbEthOamDmHistRttMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 13),
    _NbEthOamDmHistRttMax_Type()
)
nbEthOamDmHistRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistRttMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistRttMax.setUnits("microseconds")
_NbEthOamDmHistRttAverage_Type = Unsigned32
_NbEthOamDmHistRttAverage_Object = MibTableColumn
nbEthOamDmHistRttAverage = _NbEthOamDmHistRttAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 14),
    _NbEthOamDmHistRttAverage_Type()
)
nbEthOamDmHistRttAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistRttAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistRttAverage.setUnits("microseconds")
_NbEthOamDmHistRttSum2_Type = Unsigned32
_NbEthOamDmHistRttSum2_Object = MibTableColumn
nbEthOamDmHistRttSum2 = _NbEthOamDmHistRttSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 15),
    _NbEthOamDmHistRttSum2_Type()
)
nbEthOamDmHistRttSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistRttSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistRttSum2.setUnits("square of milliseconds")
_NbEthOamDmHistDSJittNumber_Type = Unsigned32
_NbEthOamDmHistDSJittNumber_Object = MibTableColumn
nbEthOamDmHistDSJittNumber = _NbEthOamDmHistDSJittNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 23),
    _NbEthOamDmHistDSJittNumber_Type()
)
nbEthOamDmHistDSJittNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittNumber.setStatus("current")
_NbEthOamDmHistDSJittMin_Type = Unsigned32
_NbEthOamDmHistDSJittMin_Object = MibTableColumn
nbEthOamDmHistDSJittMin = _NbEthOamDmHistDSJittMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 24),
    _NbEthOamDmHistDSJittMin_Type()
)
nbEthOamDmHistDSJittMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittMin.setUnits("microseconds")
_NbEthOamDmHistDSJittMax_Type = Unsigned32
_NbEthOamDmHistDSJittMax_Object = MibTableColumn
nbEthOamDmHistDSJittMax = _NbEthOamDmHistDSJittMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 25),
    _NbEthOamDmHistDSJittMax_Type()
)
nbEthOamDmHistDSJittMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittMax.setUnits("microseconds")
_NbEthOamDmHistDSJittAverage_Type = Unsigned32
_NbEthOamDmHistDSJittAverage_Object = MibTableColumn
nbEthOamDmHistDSJittAverage = _NbEthOamDmHistDSJittAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 26),
    _NbEthOamDmHistDSJittAverage_Type()
)
nbEthOamDmHistDSJittAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittAverage.setUnits("microseconds")
_NbEthOamDmHistDSJittSum2_Type = Unsigned32
_NbEthOamDmHistDSJittSum2_Object = MibTableColumn
nbEthOamDmHistDSJittSum2 = _NbEthOamDmHistDSJittSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 27),
    _NbEthOamDmHistDSJittSum2_Type()
)
nbEthOamDmHistDSJittSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittSum2.setUnits("square of milliseconds")
_NbEthOamDmHistDSJittIA_Type = Unsigned32
_NbEthOamDmHistDSJittIA_Object = MibTableColumn
nbEthOamDmHistDSJittIA = _NbEthOamDmHistDSJittIA_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 30),
    _NbEthOamDmHistDSJittIA_Type()
)
nbEthOamDmHistDSJittIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittIA.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistDSJittIA.setUnits("microseconds")
_NbEthOamDmHistSDJittNumber_Type = Unsigned32
_NbEthOamDmHistSDJittNumber_Object = MibTableColumn
nbEthOamDmHistSDJittNumber = _NbEthOamDmHistSDJittNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 36),
    _NbEthOamDmHistSDJittNumber_Type()
)
nbEthOamDmHistSDJittNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittNumber.setStatus("current")
_NbEthOamDmHistSDJittMin_Type = Unsigned32
_NbEthOamDmHistSDJittMin_Object = MibTableColumn
nbEthOamDmHistSDJittMin = _NbEthOamDmHistSDJittMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 37),
    _NbEthOamDmHistSDJittMin_Type()
)
nbEthOamDmHistSDJittMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittMin.setUnits("microseconds")
_NbEthOamDmHistSDJittMax_Type = Unsigned32
_NbEthOamDmHistSDJittMax_Object = MibTableColumn
nbEthOamDmHistSDJittMax = _NbEthOamDmHistSDJittMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 38),
    _NbEthOamDmHistSDJittMax_Type()
)
nbEthOamDmHistSDJittMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittMax.setUnits("microseconds")
_NbEthOamDmHistSDJittAverage_Type = Unsigned32
_NbEthOamDmHistSDJittAverage_Object = MibTableColumn
nbEthOamDmHistSDJittAverage = _NbEthOamDmHistSDJittAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 39),
    _NbEthOamDmHistSDJittAverage_Type()
)
nbEthOamDmHistSDJittAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittAverage.setUnits("microseconds")
_NbEthOamDmHistSDJittSum2_Type = Unsigned32
_NbEthOamDmHistSDJittSum2_Object = MibTableColumn
nbEthOamDmHistSDJittSum2 = _NbEthOamDmHistSDJittSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 40),
    _NbEthOamDmHistSDJittSum2_Type()
)
nbEthOamDmHistSDJittSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittSum2.setUnits("square of milliseconds")
_NbEthOamDmHistSDJittIA_Type = Unsigned32
_NbEthOamDmHistSDJittIA_Object = MibTableColumn
nbEthOamDmHistSDJittIA = _NbEthOamDmHistSDJittIA_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 41),
    _NbEthOamDmHistSDJittIA_Type()
)
nbEthOamDmHistSDJittIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittIA.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistSDJittIA.setUnits("microseconds")
_NbEthOamDmHistPcktLoss_Type = Unsigned32
_NbEthOamDmHistPcktLoss_Object = MibTableColumn
nbEthOamDmHistPcktLoss = _NbEthOamDmHistPcktLoss_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 42),
    _NbEthOamDmHistPcktLoss_Type()
)
nbEthOamDmHistPcktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistPcktLoss.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHistPcktLoss.setUnits("0.01%")
_NbEthOamDmHistType_Type = TestRunMethod
_NbEthOamDmHistType_Object = MibTableColumn
nbEthOamDmHistType = _NbEthOamDmHistType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 43),
    _NbEthOamDmHistType_Type()
)
nbEthOamDmHistType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistType.setStatus("current")


class _NbEthOamDmHistPriority_Type(Unsigned32):
    """Custom type nbEthOamDmHistPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbEthOamDmHistPriority_Type.__name__ = "Unsigned32"
_NbEthOamDmHistPriority_Object = MibTableColumn
nbEthOamDmHistPriority = _NbEthOamDmHistPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 2, 1, 44),
    _NbEthOamDmHistPriority_Type()
)
nbEthOamDmHistPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHistPriority.setStatus("current")
_NbEthOamDmLastTable_Object = MibTable
nbEthOamDmLastTable = _NbEthOamDmLastTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3)
)
if mibBuilder.loadTexts:
    nbEthOamDmLastTable.setStatus("current")
_NbEthOamDmLastEntry_Object = MibTableRow
nbEthOamDmLastEntry = _NbEthOamDmLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1)
)
nbEthOamDmLastEntry.setIndexNames(
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMdIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMaIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMepIdentifier"),
)
if mibBuilder.loadTexts:
    nbEthOamDmLastEntry.setStatus("current")
_NbEthOamDmLastStarted_Type = DateAndTime
_NbEthOamDmLastStarted_Object = MibTableColumn
nbEthOamDmLastStarted = _NbEthOamDmLastStarted_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 6),
    _NbEthOamDmLastStarted_Type()
)
nbEthOamDmLastStarted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastStarted.setStatus("current")
_NbEthOamDmLastDestMepId_Type = NbEthOamMepIdOrZero
_NbEthOamDmLastDestMepId_Object = MibTableColumn
nbEthOamDmLastDestMepId = _NbEthOamDmLastDestMepId_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 7),
    _NbEthOamDmLastDestMepId_Type()
)
nbEthOamDmLastDestMepId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastDestMepId.setStatus("current")
_NbEthOamDmLastDestMepMac_Type = MacAddress
_NbEthOamDmLastDestMepMac_Object = MibTableColumn
nbEthOamDmLastDestMepMac = _NbEthOamDmLastDestMepMac_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 8),
    _NbEthOamDmLastDestMepMac_Type()
)
nbEthOamDmLastDestMepMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastDestMepMac.setStatus("current")
_NbEthOamDmLastMsgTransmitted_Type = Unsigned32
_NbEthOamDmLastMsgTransmitted_Object = MibTableColumn
nbEthOamDmLastMsgTransmitted = _NbEthOamDmLastMsgTransmitted_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 9),
    _NbEthOamDmLastMsgTransmitted_Type()
)
nbEthOamDmLastMsgTransmitted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastMsgTransmitted.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastMsgTransmitted.setUnits("frames")
_NbEthOamDmLastMsgReceived_Type = Unsigned32
_NbEthOamDmLastMsgReceived_Object = MibTableColumn
nbEthOamDmLastMsgReceived = _NbEthOamDmLastMsgReceived_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 10),
    _NbEthOamDmLastMsgReceived_Type()
)
nbEthOamDmLastMsgReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastMsgReceived.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastMsgReceived.setUnits("packets")
_NbEthOamDmLastRttMin_Type = Unsigned32
_NbEthOamDmLastRttMin_Object = MibTableColumn
nbEthOamDmLastRttMin = _NbEthOamDmLastRttMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 12),
    _NbEthOamDmLastRttMin_Type()
)
nbEthOamDmLastRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastRttMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastRttMin.setUnits("microseconds")
_NbEthOamDmLastRttMax_Type = Unsigned32
_NbEthOamDmLastRttMax_Object = MibTableColumn
nbEthOamDmLastRttMax = _NbEthOamDmLastRttMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 13),
    _NbEthOamDmLastRttMax_Type()
)
nbEthOamDmLastRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastRttMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastRttMax.setUnits("microseconds")
_NbEthOamDmLastRttAverage_Type = Unsigned32
_NbEthOamDmLastRttAverage_Object = MibTableColumn
nbEthOamDmLastRttAverage = _NbEthOamDmLastRttAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 14),
    _NbEthOamDmLastRttAverage_Type()
)
nbEthOamDmLastRttAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastRttAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastRttAverage.setUnits("microseconds")
_NbEthOamDmLastRttSum2_Type = Unsigned32
_NbEthOamDmLastRttSum2_Object = MibTableColumn
nbEthOamDmLastRttSum2 = _NbEthOamDmLastRttSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 15),
    _NbEthOamDmLastRttSum2_Type()
)
nbEthOamDmLastRttSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastRttSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastRttSum2.setUnits("square of milliseconds")
_NbEthOamDmLastDSJittNumber_Type = Unsigned32
_NbEthOamDmLastDSJittNumber_Object = MibTableColumn
nbEthOamDmLastDSJittNumber = _NbEthOamDmLastDSJittNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 23),
    _NbEthOamDmLastDSJittNumber_Type()
)
nbEthOamDmLastDSJittNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittNumber.setStatus("current")
_NbEthOamDmLastDSJittMin_Type = Unsigned32
_NbEthOamDmLastDSJittMin_Object = MibTableColumn
nbEthOamDmLastDSJittMin = _NbEthOamDmLastDSJittMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 24),
    _NbEthOamDmLastDSJittMin_Type()
)
nbEthOamDmLastDSJittMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittMin.setUnits("microseconds")
_NbEthOamDmLastDSJittMax_Type = Unsigned32
_NbEthOamDmLastDSJittMax_Object = MibTableColumn
nbEthOamDmLastDSJittMax = _NbEthOamDmLastDSJittMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 25),
    _NbEthOamDmLastDSJittMax_Type()
)
nbEthOamDmLastDSJittMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittMax.setUnits("microseconds")
_NbEthOamDmLastDSJittAverage_Type = Unsigned32
_NbEthOamDmLastDSJittAverage_Object = MibTableColumn
nbEthOamDmLastDSJittAverage = _NbEthOamDmLastDSJittAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 26),
    _NbEthOamDmLastDSJittAverage_Type()
)
nbEthOamDmLastDSJittAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittAverage.setUnits("microseconds")
_NbEthOamDmLastDSJittSum2_Type = Unsigned32
_NbEthOamDmLastDSJittSum2_Object = MibTableColumn
nbEthOamDmLastDSJittSum2 = _NbEthOamDmLastDSJittSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 27),
    _NbEthOamDmLastDSJittSum2_Type()
)
nbEthOamDmLastDSJittSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittSum2.setUnits("square of milliseconds")
_NbEthOamDmLastDSJittIA_Type = Unsigned32
_NbEthOamDmLastDSJittIA_Object = MibTableColumn
nbEthOamDmLastDSJittIA = _NbEthOamDmLastDSJittIA_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 30),
    _NbEthOamDmLastDSJittIA_Type()
)
nbEthOamDmLastDSJittIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittIA.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastDSJittIA.setUnits("microseconds")
_NbEthOamDmLastSDJittNumber_Type = Unsigned32
_NbEthOamDmLastSDJittNumber_Object = MibTableColumn
nbEthOamDmLastSDJittNumber = _NbEthOamDmLastSDJittNumber_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 36),
    _NbEthOamDmLastSDJittNumber_Type()
)
nbEthOamDmLastSDJittNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittNumber.setStatus("current")
_NbEthOamDmLastSDJittMin_Type = Unsigned32
_NbEthOamDmLastSDJittMin_Object = MibTableColumn
nbEthOamDmLastSDJittMin = _NbEthOamDmLastSDJittMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 37),
    _NbEthOamDmLastSDJittMin_Type()
)
nbEthOamDmLastSDJittMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittMin.setUnits("microseconds")
_NbEthOamDmLastSDJittMax_Type = Unsigned32
_NbEthOamDmLastSDJittMax_Object = MibTableColumn
nbEthOamDmLastSDJittMax = _NbEthOamDmLastSDJittMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 38),
    _NbEthOamDmLastSDJittMax_Type()
)
nbEthOamDmLastSDJittMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittMax.setUnits("microseconds")
_NbEthOamDmLastSDJittAverage_Type = Unsigned32
_NbEthOamDmLastSDJittAverage_Object = MibTableColumn
nbEthOamDmLastSDJittAverage = _NbEthOamDmLastSDJittAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 39),
    _NbEthOamDmLastSDJittAverage_Type()
)
nbEthOamDmLastSDJittAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittAverage.setUnits("microseconds")
_NbEthOamDmLastSDJittSum2_Type = Unsigned32
_NbEthOamDmLastSDJittSum2_Object = MibTableColumn
nbEthOamDmLastSDJittSum2 = _NbEthOamDmLastSDJittSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 40),
    _NbEthOamDmLastSDJittSum2_Type()
)
nbEthOamDmLastSDJittSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittSum2.setUnits("square of milliseconds")
_NbEthOamDmLastSDJittIA_Type = Unsigned32
_NbEthOamDmLastSDJittIA_Object = MibTableColumn
nbEthOamDmLastSDJittIA = _NbEthOamDmLastSDJittIA_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 41),
    _NbEthOamDmLastSDJittIA_Type()
)
nbEthOamDmLastSDJittIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittIA.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastSDJittIA.setUnits("microseconds")
_NbEthOamDmLastPcktLoss_Type = Unsigned32
_NbEthOamDmLastPcktLoss_Object = MibTableColumn
nbEthOamDmLastPcktLoss = _NbEthOamDmLastPcktLoss_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 42),
    _NbEthOamDmLastPcktLoss_Type()
)
nbEthOamDmLastPcktLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastPcktLoss.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmLastPcktLoss.setUnits("0.01%")
_NbEthOamDmLastType_Type = TestRunMethod
_NbEthOamDmLastType_Object = MibTableColumn
nbEthOamDmLastType = _NbEthOamDmLastType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 43),
    _NbEthOamDmLastType_Type()
)
nbEthOamDmLastType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastType.setStatus("current")


class _NbEthOamDmLastPriority_Type(Unsigned32):
    """Custom type nbEthOamDmLastPriority based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_NbEthOamDmLastPriority_Type.__name__ = "Unsigned32"
_NbEthOamDmLastPriority_Object = MibTableColumn
nbEthOamDmLastPriority = _NbEthOamDmLastPriority_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 44),
    _NbEthOamDmLastPriority_Type()
)
nbEthOamDmLastPriority.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastPriority.setStatus("current")
_NbEthOamDmLastHistIndx_Type = Unsigned32
_NbEthOamDmLastHistIndx_Object = MibTableColumn
nbEthOamDmLastHistIndx = _NbEthOamDmLastHistIndx_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 3, 1, 50),
    _NbEthOamDmLastHistIndx_Type()
)
nbEthOamDmLastHistIndx.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmLastHistIndx.setStatus("current")
_NbEthOamDmConfExtTable_Object = MibTable
nbEthOamDmConfExtTable = _NbEthOamDmConfExtTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 4)
)
if mibBuilder.loadTexts:
    nbEthOamDmConfExtTable.setStatus("current")
_NbEthOamDmConfExtEntry_Object = MibTableRow
nbEthOamDmConfExtEntry = _NbEthOamDmConfExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 4, 1)
)
if mibBuilder.loadTexts:
    nbEthOamDmConfExtEntry.setStatus("current")
_NbEthOamDmConfDestMepList_Type = MepList
_NbEthOamDmConfDestMepList_Object = MibTableColumn
nbEthOamDmConfDestMepList = _NbEthOamDmConfDestMepList_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 4, 1, 12),
    _NbEthOamDmConfDestMepList_Type()
)
nbEthOamDmConfDestMepList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDmConfDestMepList.setStatus("current")
_NbEthOamDmHcHistTable_Object = MibTable
nbEthOamDmHcHistTable = _NbEthOamDmHcHistTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5)
)
if mibBuilder.loadTexts:
    nbEthOamDmHcHistTable.setStatus("current")
_NbEthOamDmHcHistEntry_Object = MibTableRow
nbEthOamDmHcHistEntry = _NbEthOamDmHcHistEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1)
)
if mibBuilder.loadTexts:
    nbEthOamDmHcHistEntry.setStatus("current")
_NbEthOamDmHcHistRttMin_Type = Counter64
_NbEthOamDmHcHistRttMin_Object = MibTableColumn
nbEthOamDmHcHistRttMin = _NbEthOamDmHcHistRttMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 12),
    _NbEthOamDmHcHistRttMin_Type()
)
nbEthOamDmHcHistRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistRttMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistRttMin.setUnits("nanoseconds")
_NbEthOamDmHcHistRttMax_Type = Counter64
_NbEthOamDmHcHistRttMax_Object = MibTableColumn
nbEthOamDmHcHistRttMax = _NbEthOamDmHcHistRttMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 13),
    _NbEthOamDmHcHistRttMax_Type()
)
nbEthOamDmHcHistRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistRttMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistRttMax.setUnits("nanoseconds")
_NbEthOamDmHcHistRttAverage_Type = Counter64
_NbEthOamDmHcHistRttAverage_Object = MibTableColumn
nbEthOamDmHcHistRttAverage = _NbEthOamDmHcHistRttAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 14),
    _NbEthOamDmHcHistRttAverage_Type()
)
nbEthOamDmHcHistRttAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistRttAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistRttAverage.setUnits("nanoseconds")
_NbEthOamDmHcHistRttSum2_Type = Counter64
_NbEthOamDmHcHistRttSum2_Object = MibTableColumn
nbEthOamDmHcHistRttSum2 = _NbEthOamDmHcHistRttSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 15),
    _NbEthOamDmHcHistRttSum2_Type()
)
nbEthOamDmHcHistRttSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistRttSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistRttSum2.setUnits("square of milliseconds")
_NbEthOamDmHcHistDSJittMin_Type = Counter64
_NbEthOamDmHcHistDSJittMin_Object = MibTableColumn
nbEthOamDmHcHistDSJittMin = _NbEthOamDmHcHistDSJittMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 24),
    _NbEthOamDmHcHistDSJittMin_Type()
)
nbEthOamDmHcHistDSJittMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistDSJittMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistDSJittMin.setUnits("nanoseconds")
_NbEthOamDmHcHistDSJittMax_Type = Counter64
_NbEthOamDmHcHistDSJittMax_Object = MibTableColumn
nbEthOamDmHcHistDSJittMax = _NbEthOamDmHcHistDSJittMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 25),
    _NbEthOamDmHcHistDSJittMax_Type()
)
nbEthOamDmHcHistDSJittMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistDSJittMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistDSJittMax.setUnits("nanoseconds")
_NbEthOamDmHcHistDSJittAverage_Type = Counter64
_NbEthOamDmHcHistDSJittAverage_Object = MibTableColumn
nbEthOamDmHcHistDSJittAverage = _NbEthOamDmHcHistDSJittAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 26),
    _NbEthOamDmHcHistDSJittAverage_Type()
)
nbEthOamDmHcHistDSJittAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistDSJittAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistDSJittAverage.setUnits("nanoseconds")
_NbEthOamDmHcHistDSJittSum2_Type = Counter64
_NbEthOamDmHcHistDSJittSum2_Object = MibTableColumn
nbEthOamDmHcHistDSJittSum2 = _NbEthOamDmHcHistDSJittSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 27),
    _NbEthOamDmHcHistDSJittSum2_Type()
)
nbEthOamDmHcHistDSJittSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistDSJittSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistDSJittSum2.setUnits("square of nanoseconds")
_NbEthOamDmHcHistDSJittIA_Type = Counter64
_NbEthOamDmHcHistDSJittIA_Object = MibTableColumn
nbEthOamDmHcHistDSJittIA = _NbEthOamDmHcHistDSJittIA_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 30),
    _NbEthOamDmHcHistDSJittIA_Type()
)
nbEthOamDmHcHistDSJittIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistDSJittIA.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistDSJittIA.setUnits("nanoseconds")
_NbEthOamDmHcHistSDJittMin_Type = Counter64
_NbEthOamDmHcHistSDJittMin_Object = MibTableColumn
nbEthOamDmHcHistSDJittMin = _NbEthOamDmHcHistSDJittMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 37),
    _NbEthOamDmHcHistSDJittMin_Type()
)
nbEthOamDmHcHistSDJittMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistSDJittMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistSDJittMin.setUnits("nanoseconds")
_NbEthOamDmHcHistSDJittMax_Type = Counter64
_NbEthOamDmHcHistSDJittMax_Object = MibTableColumn
nbEthOamDmHcHistSDJittMax = _NbEthOamDmHcHistSDJittMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 38),
    _NbEthOamDmHcHistSDJittMax_Type()
)
nbEthOamDmHcHistSDJittMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistSDJittMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistSDJittMax.setUnits("nanoseconds")
_NbEthOamDmHcHistSDJittAverage_Type = Counter64
_NbEthOamDmHcHistSDJittAverage_Object = MibTableColumn
nbEthOamDmHcHistSDJittAverage = _NbEthOamDmHcHistSDJittAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 39),
    _NbEthOamDmHcHistSDJittAverage_Type()
)
nbEthOamDmHcHistSDJittAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistSDJittAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistSDJittAverage.setUnits("nanoseconds")
_NbEthOamDmHcHistSDJittSum2_Type = Counter64
_NbEthOamDmHcHistSDJittSum2_Object = MibTableColumn
nbEthOamDmHcHistSDJittSum2 = _NbEthOamDmHcHistSDJittSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 40),
    _NbEthOamDmHcHistSDJittSum2_Type()
)
nbEthOamDmHcHistSDJittSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistSDJittSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistSDJittSum2.setUnits("square of nanoseconds")
_NbEthOamDmHcHistSDJittIA_Type = Counter64
_NbEthOamDmHcHistSDJittIA_Object = MibTableColumn
nbEthOamDmHcHistSDJittIA = _NbEthOamDmHcHistSDJittIA_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 5, 1, 41),
    _NbEthOamDmHcHistSDJittIA_Type()
)
nbEthOamDmHcHistSDJittIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistSDJittIA.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcHistSDJittIA.setUnits("nanoseconds")
_NbEthOamDmHcLastTable_Object = MibTable
nbEthOamDmHcLastTable = _NbEthOamDmHcLastTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6)
)
if mibBuilder.loadTexts:
    nbEthOamDmHcLastTable.setStatus("current")
_NbEthOamDmHcLastEntry_Object = MibTableRow
nbEthOamDmHcLastEntry = _NbEthOamDmHcLastEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1)
)
if mibBuilder.loadTexts:
    nbEthOamDmHcLastEntry.setStatus("current")
_NbEthOamDmHcLastRttMin_Type = Counter64
_NbEthOamDmHcLastRttMin_Object = MibTableColumn
nbEthOamDmHcLastRttMin = _NbEthOamDmHcLastRttMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 12),
    _NbEthOamDmHcLastRttMin_Type()
)
nbEthOamDmHcLastRttMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastRttMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastRttMin.setUnits("microseconds")
_NbEthOamDmHcLastRttMax_Type = Counter64
_NbEthOamDmHcLastRttMax_Object = MibTableColumn
nbEthOamDmHcLastRttMax = _NbEthOamDmHcLastRttMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 13),
    _NbEthOamDmHcLastRttMax_Type()
)
nbEthOamDmHcLastRttMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastRttMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastRttMax.setUnits("nanoseconds")
_NbEthOamDmHcLastRttAverage_Type = Counter64
_NbEthOamDmHcLastRttAverage_Object = MibTableColumn
nbEthOamDmHcLastRttAverage = _NbEthOamDmHcLastRttAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 14),
    _NbEthOamDmHcLastRttAverage_Type()
)
nbEthOamDmHcLastRttAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastRttAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastRttAverage.setUnits("nanoseconds")
_NbEthOamDmHcLastRttSum2_Type = Counter64
_NbEthOamDmHcLastRttSum2_Object = MibTableColumn
nbEthOamDmHcLastRttSum2 = _NbEthOamDmHcLastRttSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 15),
    _NbEthOamDmHcLastRttSum2_Type()
)
nbEthOamDmHcLastRttSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastRttSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastRttSum2.setUnits("square of milliseconds")
_NbEthOamDmHcLastDSJittMin_Type = Counter64
_NbEthOamDmHcLastDSJittMin_Object = MibTableColumn
nbEthOamDmHcLastDSJittMin = _NbEthOamDmHcLastDSJittMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 24),
    _NbEthOamDmHcLastDSJittMin_Type()
)
nbEthOamDmHcLastDSJittMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastDSJittMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastDSJittMin.setUnits("nanoseconds")
_NbEthOamDmHcLastDSJittMax_Type = Counter64
_NbEthOamDmHcLastDSJittMax_Object = MibTableColumn
nbEthOamDmHcLastDSJittMax = _NbEthOamDmHcLastDSJittMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 25),
    _NbEthOamDmHcLastDSJittMax_Type()
)
nbEthOamDmHcLastDSJittMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastDSJittMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastDSJittMax.setUnits("nanoseconds")
_NbEthOamDmHcLastDSJittAverage_Type = Counter64
_NbEthOamDmHcLastDSJittAverage_Object = MibTableColumn
nbEthOamDmHcLastDSJittAverage = _NbEthOamDmHcLastDSJittAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 26),
    _NbEthOamDmHcLastDSJittAverage_Type()
)
nbEthOamDmHcLastDSJittAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastDSJittAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastDSJittAverage.setUnits("nanoseconds")
_NbEthOamDmHcLastDSJittSum2_Type = Counter64
_NbEthOamDmHcLastDSJittSum2_Object = MibTableColumn
nbEthOamDmHcLastDSJittSum2 = _NbEthOamDmHcLastDSJittSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 27),
    _NbEthOamDmHcLastDSJittSum2_Type()
)
nbEthOamDmHcLastDSJittSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastDSJittSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastDSJittSum2.setUnits("square of nanoseconds")
_NbEthOamDmHcLastDSJittIA_Type = Counter64
_NbEthOamDmHcLastDSJittIA_Object = MibTableColumn
nbEthOamDmHcLastDSJittIA = _NbEthOamDmHcLastDSJittIA_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 30),
    _NbEthOamDmHcLastDSJittIA_Type()
)
nbEthOamDmHcLastDSJittIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastDSJittIA.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastDSJittIA.setUnits("nanoseconds")
_NbEthOamDmHcLastSDJittMin_Type = Counter64
_NbEthOamDmHcLastSDJittMin_Object = MibTableColumn
nbEthOamDmHcLastSDJittMin = _NbEthOamDmHcLastSDJittMin_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 37),
    _NbEthOamDmHcLastSDJittMin_Type()
)
nbEthOamDmHcLastSDJittMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastSDJittMin.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastSDJittMin.setUnits("nanoseconds")
_NbEthOamDmHcLastSDJittMax_Type = Counter64
_NbEthOamDmHcLastSDJittMax_Object = MibTableColumn
nbEthOamDmHcLastSDJittMax = _NbEthOamDmHcLastSDJittMax_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 38),
    _NbEthOamDmHcLastSDJittMax_Type()
)
nbEthOamDmHcLastSDJittMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastSDJittMax.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastSDJittMax.setUnits("nanoseconds")
_NbEthOamDmHcLastSDJittAverage_Type = Counter64
_NbEthOamDmHcLastSDJittAverage_Object = MibTableColumn
nbEthOamDmHcLastSDJittAverage = _NbEthOamDmHcLastSDJittAverage_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 39),
    _NbEthOamDmHcLastSDJittAverage_Type()
)
nbEthOamDmHcLastSDJittAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastSDJittAverage.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastSDJittAverage.setUnits("nanoseconds")
_NbEthOamDmHcLastSDJittSum2_Type = Counter64
_NbEthOamDmHcLastSDJittSum2_Object = MibTableColumn
nbEthOamDmHcLastSDJittSum2 = _NbEthOamDmHcLastSDJittSum2_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 40),
    _NbEthOamDmHcLastSDJittSum2_Type()
)
nbEthOamDmHcLastSDJittSum2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastSDJittSum2.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastSDJittSum2.setUnits("square of nanoseconds")
_NbEthOamDmHcLastSDJittIA_Type = Counter64
_NbEthOamDmHcLastSDJittIA_Object = MibTableColumn
nbEthOamDmHcLastSDJittIA = _NbEthOamDmHcLastSDJittIA_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 41),
    _NbEthOamDmHcLastSDJittIA_Type()
)
nbEthOamDmHcLastSDJittIA.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastSDJittIA.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastSDJittIA.setUnits("nanoseconds")


class _NbEthOamDmHcLastRunStatus_Type(Integer32):
    """Custom type nbEthOamDmHcLastRunStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              14,
              104)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 0),
          ("idle", 1),
          ("running", 2),
          ("scheduled", 3),
          ("deferred", 4),
          ("stopped", 5),
          ("noVlan", 6),
          ("error", 7),
          ("noMac", 14),
          ("deferredForMac", 104))
    )


_NbEthOamDmHcLastRunStatus_Type.__name__ = "Integer32"
_NbEthOamDmHcLastRunStatus_Object = MibTableColumn
nbEthOamDmHcLastRunStatus = _NbEthOamDmHcLastRunStatus_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 11, 6, 1, 59),
    _NbEthOamDmHcLastRunStatus_Type()
)
nbEthOamDmHcLastRunStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamDmHcLastRunStatus.setStatus("current")
_NbEthOamServiceTable_Object = MibTable
nbEthOamServiceTable = _NbEthOamServiceTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 16)
)
if mibBuilder.loadTexts:
    nbEthOamServiceTable.setStatus("current")
_NbEthOamServiceEntry_Object = MibTableRow
nbEthOamServiceEntry = _NbEthOamServiceEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 16, 1)
)
nbEthOamServiceEntry.setIndexNames(
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMdIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMaIndex"),
)
if mibBuilder.loadTexts:
    nbEthOamServiceEntry.setStatus("current")


class _NbEthOamServiceDmResponderSL_Type(Unsigned32):
    """Custom type nbEthOamServiceDmResponderSL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_NbEthOamServiceDmResponderSL_Type.__name__ = "Unsigned32"
_NbEthOamServiceDmResponderSL_Object = MibTableColumn
nbEthOamServiceDmResponderSL = _NbEthOamServiceDmResponderSL_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 16, 1, 20),
    _NbEthOamServiceDmResponderSL_Type()
)
nbEthOamServiceDmResponderSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamServiceDmResponderSL.setStatus("current")


class _NbEthOamServiceLbResponderSL_Type(Unsigned32):
    """Custom type nbEthOamServiceLbResponderSL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_NbEthOamServiceLbResponderSL_Type.__name__ = "Unsigned32"
_NbEthOamServiceLbResponderSL_Object = MibTableColumn
nbEthOamServiceLbResponderSL = _NbEthOamServiceLbResponderSL_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 16, 1, 21),
    _NbEthOamServiceLbResponderSL_Type()
)
nbEthOamServiceLbResponderSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamServiceLbResponderSL.setStatus("current")


class _NbEthOamServiceLmResponderSL_Type(Unsigned32):
    """Custom type nbEthOamServiceLmResponderSL based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 0),
        ValueRangeConstraint(1, 8),
    )


_NbEthOamServiceLmResponderSL_Type.__name__ = "Unsigned32"
_NbEthOamServiceLmResponderSL_Object = MibTableColumn
nbEthOamServiceLmResponderSL = _NbEthOamServiceLmResponderSL_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 16, 1, 22),
    _NbEthOamServiceLmResponderSL_Type()
)
nbEthOamServiceLmResponderSL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamServiceLmResponderSL.setStatus("current")
_NbEthOamTrapTable_Object = MibTable
nbEthOamTrapTable = _NbEthOamTrapTable_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20)
)
if mibBuilder.loadTexts:
    nbEthOamTrapTable.setStatus("current")
_NbEthOamTrapEntry_Object = MibTableRow
nbEthOamTrapEntry = _NbEthOamTrapEntry_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1)
)
nbEthOamTrapEntry.setIndexNames(
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMdIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMaIndex"),
    (0, "OA-ETHERNET-OAM-MIB", "nbEthOamMepIdentifier"),
)
if mibBuilder.loadTexts:
    nbEthOamTrapEntry.setStatus("current")


class _NbEthOamTrapTrapGeneration_Type(Bits):
    """Custom type nbEthOamTrapTrapGeneration based on Bits"""
    defaultBinValue = "0"

    namedValues = NamedValues(
        *(("ccmRecovery", 0),
          ("ccmFault", 1))
    )

_NbEthOamTrapTrapGeneration_Type.__name__ = "Bits"
_NbEthOamTrapTrapGeneration_Object = MibTableColumn
nbEthOamTrapTrapGeneration = _NbEthOamTrapTrapGeneration_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 1),
    _NbEthOamTrapTrapGeneration_Type()
)
nbEthOamTrapTrapGeneration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamTrapTrapGeneration.setStatus("current")
_NbEthOamTrapCcmHighestPrDefect_Type = NbEthOamCcmHighestDefectPri
_NbEthOamTrapCcmHighestPrDefect_Object = MibTableColumn
nbEthOamTrapCcmHighestPrDefect = _NbEthOamTrapCcmHighestPrDefect_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 2),
    _NbEthOamTrapCcmHighestPrDefect_Type()
)
nbEthOamTrapCcmHighestPrDefect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamTrapCcmHighestPrDefect.setStatus("current")


class _NbEthOamTrapCcmAlarmType_Type(Integer32):
    """Custom type nbEthOamTrapCcmAlarmType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fault", 1),
          ("recovery", 2))
    )


_NbEthOamTrapCcmAlarmType_Type.__name__ = "Integer32"
_NbEthOamTrapCcmAlarmType_Object = MibTableColumn
nbEthOamTrapCcmAlarmType = _NbEthOamTrapCcmAlarmType_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 3),
    _NbEthOamTrapCcmAlarmType_Type()
)
nbEthOamTrapCcmAlarmType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamTrapCcmAlarmType.setStatus("current")


class _NbEthOamTrapDmmReason_Type(Integer32):
    """Custom type nbEthOamTrapDmmReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("risingDmAlarm", 1),
          ("fallingDmAlarm", 2))
    )


_NbEthOamTrapDmmReason_Type.__name__ = "Integer32"
_NbEthOamTrapDmmReason_Object = MibTableColumn
nbEthOamTrapDmmReason = _NbEthOamTrapDmmReason_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 30),
    _NbEthOamTrapDmmReason_Type()
)
nbEthOamTrapDmmReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nbEthOamTrapDmmReason.setStatus("current")


class _NbEthOamFdRiseThold_Type(Unsigned32):
    """Custom type nbEthOamFdRiseThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamFdRiseThold_Type.__name__ = "Unsigned32"
_NbEthOamFdRiseThold_Object = MibTableColumn
nbEthOamFdRiseThold = _NbEthOamFdRiseThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 35),
    _NbEthOamFdRiseThold_Type()
)
nbEthOamFdRiseThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamFdRiseThold.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamFdRiseThold.setUnits("microseconds")


class _NbEthOamFdFallThold_Type(Unsigned32):
    """Custom type nbEthOamFdFallThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamFdFallThold_Type.__name__ = "Unsigned32"
_NbEthOamFdFallThold_Object = MibTableColumn
nbEthOamFdFallThold = _NbEthOamFdFallThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 36),
    _NbEthOamFdFallThold_Type()
)
nbEthOamFdFallThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamFdFallThold.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamFdFallThold.setUnits("microseconds")


class _NbEthOamDSJittRiseThold_Type(Unsigned32):
    """Custom type nbEthOamDSJittRiseThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamDSJittRiseThold_Type.__name__ = "Unsigned32"
_NbEthOamDSJittRiseThold_Object = MibTableColumn
nbEthOamDSJittRiseThold = _NbEthOamDSJittRiseThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 49),
    _NbEthOamDSJittRiseThold_Type()
)
nbEthOamDSJittRiseThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDSJittRiseThold.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDSJittRiseThold.setUnits("microseconds")


class _NbEthOamDSJittFallThold_Type(Unsigned32):
    """Custom type nbEthOamDSJittFallThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamDSJittFallThold_Type.__name__ = "Unsigned32"
_NbEthOamDSJittFallThold_Object = MibTableColumn
nbEthOamDSJittFallThold = _NbEthOamDSJittFallThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 50),
    _NbEthOamDSJittFallThold_Type()
)
nbEthOamDSJittFallThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDSJittFallThold.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamDSJittFallThold.setUnits("microseconds")


class _NbEthOamDSJittSum2RiseThold_Type(Unsigned32):
    """Custom type nbEthOamDSJittSum2RiseThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamDSJittSum2RiseThold_Type.__name__ = "Unsigned32"
_NbEthOamDSJittSum2RiseThold_Object = MibTableColumn
nbEthOamDSJittSum2RiseThold = _NbEthOamDSJittSum2RiseThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 51),
    _NbEthOamDSJittSum2RiseThold_Type()
)
nbEthOamDSJittSum2RiseThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDSJittSum2RiseThold.setStatus("current")


class _NbEthOamDSJittSum2FallThold_Type(Unsigned32):
    """Custom type nbEthOamDSJittSum2FallThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamDSJittSum2FallThold_Type.__name__ = "Unsigned32"
_NbEthOamDSJittSum2FallThold_Object = MibTableColumn
nbEthOamDSJittSum2FallThold = _NbEthOamDSJittSum2FallThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 52),
    _NbEthOamDSJittSum2FallThold_Type()
)
nbEthOamDSJittSum2FallThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamDSJittSum2FallThold.setStatus("current")


class _NbEthOamSDJittRiseThold_Type(Unsigned32):
    """Custom type nbEthOamSDJittRiseThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamSDJittRiseThold_Type.__name__ = "Unsigned32"
_NbEthOamSDJittRiseThold_Object = MibTableColumn
nbEthOamSDJittRiseThold = _NbEthOamSDJittRiseThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 63),
    _NbEthOamSDJittRiseThold_Type()
)
nbEthOamSDJittRiseThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamSDJittRiseThold.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamSDJittRiseThold.setUnits("microseconds")


class _NbEthOamSDJittFallThold_Type(Unsigned32):
    """Custom type nbEthOamSDJittFallThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamSDJittFallThold_Type.__name__ = "Unsigned32"
_NbEthOamSDJittFallThold_Object = MibTableColumn
nbEthOamSDJittFallThold = _NbEthOamSDJittFallThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 64),
    _NbEthOamSDJittFallThold_Type()
)
nbEthOamSDJittFallThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamSDJittFallThold.setStatus("current")
if mibBuilder.loadTexts:
    nbEthOamSDJittFallThold.setUnits("microseconds")


class _NbEthOamSDJittSum2RiseThold_Type(Unsigned32):
    """Custom type nbEthOamSDJittSum2RiseThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamSDJittSum2RiseThold_Type.__name__ = "Unsigned32"
_NbEthOamSDJittSum2RiseThold_Object = MibTableColumn
nbEthOamSDJittSum2RiseThold = _NbEthOamSDJittSum2RiseThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 66),
    _NbEthOamSDJittSum2RiseThold_Type()
)
nbEthOamSDJittSum2RiseThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamSDJittSum2RiseThold.setStatus("current")


class _NbEthOamSDJittSum2FallThold_Type(Unsigned32):
    """Custom type nbEthOamSDJittSum2FallThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamSDJittSum2FallThold_Type.__name__ = "Unsigned32"
_NbEthOamSDJittSum2FallThold_Object = MibTableColumn
nbEthOamSDJittSum2FallThold = _NbEthOamSDJittSum2FallThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 67),
    _NbEthOamSDJittSum2FallThold_Type()
)
nbEthOamSDJittSum2FallThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamSDJittSum2FallThold.setStatus("current")


class _NbEthOamPcktLossRiseThold_Type(Unsigned32):
    """Custom type nbEthOamPcktLossRiseThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamPcktLossRiseThold_Type.__name__ = "Unsigned32"
_NbEthOamPcktLossRiseThold_Object = MibTableColumn
nbEthOamPcktLossRiseThold = _NbEthOamPcktLossRiseThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 68),
    _NbEthOamPcktLossRiseThold_Type()
)
nbEthOamPcktLossRiseThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamPcktLossRiseThold.setStatus("current")


class _NbEthOamPcktLossFallThold_Type(Unsigned32):
    """Custom type nbEthOamPcktLossFallThold based on Unsigned32"""
    defaultValue = 0


_NbEthOamPcktLossFallThold_Type.__name__ = "Unsigned32"
_NbEthOamPcktLossFallThold_Object = MibTableColumn
nbEthOamPcktLossFallThold = _NbEthOamPcktLossFallThold_Object(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 20, 1, 69),
    _NbEthOamPcktLossFallThold_Type()
)
nbEthOamPcktLossFallThold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    nbEthOamPcktLossFallThold.setStatus("current")
_NbEthOamConformance_ObjectIdentity = ObjectIdentity
nbEthOamConformance = _NbEthOamConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 100)
)
_NbEthOamMIBCompliances_ObjectIdentity = ObjectIdentity
nbEthOamMIBCompliances = _NbEthOamMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 100, 1)
)
_NbEthOamMIBGroups_ObjectIdentity = ObjectIdentity
nbEthOamMIBGroups = _NbEthOamMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 100, 2)
)
nbEthOamLbConfEntry.registerAugmentions(
    ("OA-ETHERNET-OAM-MIB",
     "nbEthOamLbConfExtEntry")
)
nbEthOamLbConfExtEntry.setIndexNames(*nbEthOamLbConfEntry.getIndexNames())
nbEthOamDmConfEntry.registerAugmentions(
    ("OA-ETHERNET-OAM-MIB",
     "nbEthOamDmConfExtEntry")
)
nbEthOamDmConfExtEntry.setIndexNames(*nbEthOamDmConfEntry.getIndexNames())
nbEthOamDmHistEntry.registerAugmentions(
    ("OA-ETHERNET-OAM-MIB",
     "nbEthOamDmHcHistEntry")
)
nbEthOamDmHcHistEntry.setIndexNames(*nbEthOamDmHistEntry.getIndexNames())
nbEthOamDmLastEntry.registerAugmentions(
    ("OA-ETHERNET-OAM-MIB",
     "nbEthOamDmHcLastEntry")
)
nbEthOamDmHcLastEntry.setIndexNames(*nbEthOamDmLastEntry.getIndexNames())

# Managed Objects groups

nbEthOamMandatoryGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 100, 2, 1)
)
nbEthOamMandatoryGroup.setObjects(
      *(("OA-ETHERNET-OAM-MIB", "nbEthOamFeaturesSupport"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamCcmIntervals"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfHistorySize"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfInterval"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfIntervalMicro"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfTimeout"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfDataLength"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfDataFill"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfPriority"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfDestMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfDestMepMac"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfDestMepList"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfDestIsMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfMessages"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistStarted"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistDestMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistDestMepMac"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistMsgTransmitted"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistMsgReceived"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistRttMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistRttMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistRttAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistRttSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistJittNumber"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistJittMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistJittMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistJittSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistJittIA"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistPcktLoss"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistType"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbHistPriority"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfHistorySize"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfInterval"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfIntervalMicro"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfTimeout"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfDataLength"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfDataFill"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfPriority"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfDestMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfDestMepMac"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfDestMepList"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfDestIsMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfMessages"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistStarted"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistDestMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistDestMepMac"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistMsgTransmitted"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistMsgReceived"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistRttMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistRttMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistRttAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistRttSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistDSJittNumber"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistDSJittMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistDSJittMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistDSJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistDSJittSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistDSJittIA"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistSDJittNumber"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistSDJittMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistSDJittMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistSDJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistSDJittSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistSDJittIA"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistPcktLoss"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistType"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHistPriority"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastStarted"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastDestMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastDestMepMac"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastMsgTransmitted"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastMsgReceived"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastRttMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastRttMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastRttAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastRttSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastJittNumber"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastJittMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastJittMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastJittSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastJittIA"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastPcktLoss"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastPriority"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastHistIndx"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbLastType"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastStarted"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDestMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDestMepMac"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastMsgTransmitted"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastMsgReceived"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastRttMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastRttMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastRttAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastRttSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDSJittNumber"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDSJittMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDSJittMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDSJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDSJittSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDSJittIA"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastSDJittNumber"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastSDJittMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastSDJittMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastSDJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastSDJittSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastSDJittIA"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastPcktLoss"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastPriority"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastHistIndx"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastType"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistRttMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistRttMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistRttAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistRttSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistDSJittMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistDSJittMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistDSJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistDSJittSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistDSJittIA"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistSDJittMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistSDJittMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistSDJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistSDJittSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcHistSDJittIA"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastRttMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastRttMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastRttAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastRttSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastDSJittMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastDSJittMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastDSJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastDSJittSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastDSJittIA"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastSDJittMin"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastSDJittMax"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastSDJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastSDJittSum2"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastSDJittIA"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmHcLastRunStatus"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfBurstInterval"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfNumberOfBursts"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamLbConfRunMethod"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfBurstInterval"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfNumberOfBursts"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmConfRunMethod"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamTrapTrapGeneration"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamTrapCcmHighestPrDefect"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamTrapCcmAlarmType"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamTrapDmmReason"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamFdRiseThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamFdFallThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDSJittRiseThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDSJittFallThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDSJittSum2RiseThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDSJittSum2FallThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamSDJittRiseThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamSDJittFallThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamSDJittSum2RiseThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamSDJittSum2FallThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamPcktLossRiseThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamPcktLossFallThold"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamServiceDmResponderSL"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamServiceLbResponderSL"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamServiceLmResponderSL"))
)
if mibBuilder.loadTexts:
    nbEthOamMandatoryGroup.setStatus("current")


# Notification objects

nbEthOamCcmAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 0, 1)
)
nbEthOamCcmAlarm.setObjects(
      *(("OA-ETHERNET-OAM-MIB", "nbEthOamTrapCcmHighestPrDefect"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamTrapCcmAlarmType"))
)
if mibBuilder.loadTexts:
    nbEthOamCcmAlarm.setStatus(
        "current"
    )

nbEthOamFdAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 0, 4)
)
nbEthOamFdAlarm.setObjects(
      *(("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastRttAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamTrapDmmReason"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDestMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDestMepMac"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastHistIndx"))
)
if mibBuilder.loadTexts:
    nbEthOamFdAlarm.setStatus(
        "current"
    )

nbEthOamSDJittAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 0, 8)
)
nbEthOamSDJittAlarm.setObjects(
      *(("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastSDJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamTrapDmmReason"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDestMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDestMepMac"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastHistIndx"))
)
if mibBuilder.loadTexts:
    nbEthOamSDJittAlarm.setStatus(
        "current"
    )

nbEthOamDSJittAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 0, 14)
)
nbEthOamDSJittAlarm.setObjects(
      *(("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDSJittAverage"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamTrapDmmReason"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDestMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDestMepMac"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastHistIndx"))
)
if mibBuilder.loadTexts:
    nbEthOamDSJittAlarm.setStatus(
        "current"
    )

nbEthOamPcktLossAlarm = NotificationType(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 0, 20)
)
nbEthOamPcktLossAlarm.setObjects(
      *(("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastPcktLoss"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamTrapDmmReason"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDestMepId"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastDestMepMac"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDmLastHistIndx"))
)
if mibBuilder.loadTexts:
    nbEthOamPcktLossAlarm.setStatus(
        "current"
    )


# Notifications groups

nbEthOamNotificationsGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 100, 2, 2)
)
nbEthOamNotificationsGroup.setObjects(
      *(("OA-ETHERNET-OAM-MIB", "nbEthOamCcmAlarm"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamFdAlarm"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamSDJittAlarm"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamDSJittAlarm"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamPcktLossAlarm"))
)
if mibBuilder.loadTexts:
    nbEthOamNotificationsGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

nbEthOamMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 629, 1, 50, 17, 100, 1, 1)
)
nbEthOamMIBCompliance.setObjects(
      *(("OA-ETHERNET-OAM-MIB", "nbEthOamMandatoryGroup"),
        ("OA-ETHERNET-OAM-MIB", "nbEthOamNotificationsGroup"))
)
if mibBuilder.loadTexts:
    nbEthOamMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "OA-ETHERNET-OAM-MIB",
    **{"NbEthOamMepId": NbEthOamMepId,
       "NbEthOamMepIdOrZero": NbEthOamMepIdOrZero,
       "TestRunMethod": TestRunMethod,
       "NbEthOamCcmHighestDefectPri": NbEthOamCcmHighestDefectPri,
       "DestinationType": DestinationType,
       "nbEthOam": nbEthOam,
       "nbEthOamNotifications": nbEthOamNotifications,
       "nbEthOamCcmAlarm": nbEthOamCcmAlarm,
       "nbEthOamFdAlarm": nbEthOamFdAlarm,
       "nbEthOamSDJittAlarm": nbEthOamSDJittAlarm,
       "nbEthOamDSJittAlarm": nbEthOamDSJittAlarm,
       "nbEthOamPcktLossAlarm": nbEthOamPcktLossAlarm,
       "nbEthOamCapabilities": nbEthOamCapabilities,
       "nbEthOamFeaturesSupport": nbEthOamFeaturesSupport,
       "nbEthOamCcmIntervals": nbEthOamCcmIntervals,
       "nbEthOamLb": nbEthOamLb,
       "nbEthOamLbConfTable": nbEthOamLbConfTable,
       "nbEthOamLbConfEntry": nbEthOamLbConfEntry,
       "nbEthOamMdIndex": nbEthOamMdIndex,
       "nbEthOamMaIndex": nbEthOamMaIndex,
       "nbEthOamMepIdentifier": nbEthOamMepIdentifier,
       "nbEthOamLbConfHistorySize": nbEthOamLbConfHistorySize,
       "nbEthOamLbConfInterval": nbEthOamLbConfInterval,
       "nbEthOamLbConfTimeout": nbEthOamLbConfTimeout,
       "nbEthOamLbConfDataLength": nbEthOamLbConfDataLength,
       "nbEthOamLbConfDataFill": nbEthOamLbConfDataFill,
       "nbEthOamLbConfPriority": nbEthOamLbConfPriority,
       "nbEthOamLbConfDestMepId": nbEthOamLbConfDestMepId,
       "nbEthOamLbConfDestMepMac": nbEthOamLbConfDestMepMac,
       "nbEthOamLbConfDestIsMepId": nbEthOamLbConfDestIsMepId,
       "nbEthOamLbConfMessages": nbEthOamLbConfMessages,
       "nbEthOamLbConfBurstInterval": nbEthOamLbConfBurstInterval,
       "nbEthOamLbConfNumberOfBursts": nbEthOamLbConfNumberOfBursts,
       "nbEthOamLbConfRunMethod": nbEthOamLbConfRunMethod,
       "nbEthOamLbConfIntervalMicro": nbEthOamLbConfIntervalMicro,
       "nbEthOamLbHistTable": nbEthOamLbHistTable,
       "nbEthOamLbHistEntry": nbEthOamLbHistEntry,
       "nbEthOamLbHistSampleIndex": nbEthOamLbHistSampleIndex,
       "nbEthOamLbHistStarted": nbEthOamLbHistStarted,
       "nbEthOamLbHistDestMepId": nbEthOamLbHistDestMepId,
       "nbEthOamLbHistDestMepMac": nbEthOamLbHistDestMepMac,
       "nbEthOamLbHistMsgTransmitted": nbEthOamLbHistMsgTransmitted,
       "nbEthOamLbHistMsgReceived": nbEthOamLbHistMsgReceived,
       "nbEthOamLbHistRttMin": nbEthOamLbHistRttMin,
       "nbEthOamLbHistRttMax": nbEthOamLbHistRttMax,
       "nbEthOamLbHistRttAverage": nbEthOamLbHistRttAverage,
       "nbEthOamLbHistRttSum2": nbEthOamLbHistRttSum2,
       "nbEthOamLbHistJittNumber": nbEthOamLbHistJittNumber,
       "nbEthOamLbHistJittMin": nbEthOamLbHistJittMin,
       "nbEthOamLbHistJittMax": nbEthOamLbHistJittMax,
       "nbEthOamLbHistJittAverage": nbEthOamLbHistJittAverage,
       "nbEthOamLbHistJittSum2": nbEthOamLbHistJittSum2,
       "nbEthOamLbHistJittIA": nbEthOamLbHistJittIA,
       "nbEthOamLbHistPcktLoss": nbEthOamLbHistPcktLoss,
       "nbEthOamLbHistType": nbEthOamLbHistType,
       "nbEthOamLbHistPriority": nbEthOamLbHistPriority,
       "nbEthOamLbLastTable": nbEthOamLbLastTable,
       "nbEthOamLbLastEntry": nbEthOamLbLastEntry,
       "nbEthOamLbLastStarted": nbEthOamLbLastStarted,
       "nbEthOamLbLastDestMepId": nbEthOamLbLastDestMepId,
       "nbEthOamLbLastDestMepMac": nbEthOamLbLastDestMepMac,
       "nbEthOamLbLastMsgTransmitted": nbEthOamLbLastMsgTransmitted,
       "nbEthOamLbLastMsgReceived": nbEthOamLbLastMsgReceived,
       "nbEthOamLbLastRttMin": nbEthOamLbLastRttMin,
       "nbEthOamLbLastRttMax": nbEthOamLbLastRttMax,
       "nbEthOamLbLastRttAverage": nbEthOamLbLastRttAverage,
       "nbEthOamLbLastRttSum2": nbEthOamLbLastRttSum2,
       "nbEthOamLbLastJittNumber": nbEthOamLbLastJittNumber,
       "nbEthOamLbLastJittMin": nbEthOamLbLastJittMin,
       "nbEthOamLbLastJittMax": nbEthOamLbLastJittMax,
       "nbEthOamLbLastJittAverage": nbEthOamLbLastJittAverage,
       "nbEthOamLbLastJittSum2": nbEthOamLbLastJittSum2,
       "nbEthOamLbLastJittIA": nbEthOamLbLastJittIA,
       "nbEthOamLbLastPcktLoss": nbEthOamLbLastPcktLoss,
       "nbEthOamLbLastType": nbEthOamLbLastType,
       "nbEthOamLbLastPriority": nbEthOamLbLastPriority,
       "nbEthOamLbLastHistIndx": nbEthOamLbLastHistIndx,
       "nbEthOamLbConfExtTable": nbEthOamLbConfExtTable,
       "nbEthOamLbConfExtEntry": nbEthOamLbConfExtEntry,
       "nbEthOamLbConfDestMepList": nbEthOamLbConfDestMepList,
       "nbEthOamDm": nbEthOamDm,
       "nbEthOamDmConfTable": nbEthOamDmConfTable,
       "nbEthOamDmConfEntry": nbEthOamDmConfEntry,
       "nbEthOamDmConfHistorySize": nbEthOamDmConfHistorySize,
       "nbEthOamDmConfInterval": nbEthOamDmConfInterval,
       "nbEthOamDmConfTimeout": nbEthOamDmConfTimeout,
       "nbEthOamDmConfDataLength": nbEthOamDmConfDataLength,
       "nbEthOamDmConfDataFill": nbEthOamDmConfDataFill,
       "nbEthOamDmConfPriority": nbEthOamDmConfPriority,
       "nbEthOamDmConfDestMepId": nbEthOamDmConfDestMepId,
       "nbEthOamDmConfDestMepMac": nbEthOamDmConfDestMepMac,
       "nbEthOamDmConfDestIsMepId": nbEthOamDmConfDestIsMepId,
       "nbEthOamDmConfMessages": nbEthOamDmConfMessages,
       "nbEthOamDmConfBurstInterval": nbEthOamDmConfBurstInterval,
       "nbEthOamDmConfNumberOfBursts": nbEthOamDmConfNumberOfBursts,
       "nbEthOamDmConfRunMethod": nbEthOamDmConfRunMethod,
       "nbEthOamDmConfIntervalMicro": nbEthOamDmConfIntervalMicro,
       "nbEthOamDmHistTable": nbEthOamDmHistTable,
       "nbEthOamDmHistEntry": nbEthOamDmHistEntry,
       "nbEthOamDmHistSampleIndex": nbEthOamDmHistSampleIndex,
       "nbEthOamDmHistStarted": nbEthOamDmHistStarted,
       "nbEthOamDmHistDestMepId": nbEthOamDmHistDestMepId,
       "nbEthOamDmHistDestMepMac": nbEthOamDmHistDestMepMac,
       "nbEthOamDmHistMsgTransmitted": nbEthOamDmHistMsgTransmitted,
       "nbEthOamDmHistMsgReceived": nbEthOamDmHistMsgReceived,
       "nbEthOamDmHistRttMin": nbEthOamDmHistRttMin,
       "nbEthOamDmHistRttMax": nbEthOamDmHistRttMax,
       "nbEthOamDmHistRttAverage": nbEthOamDmHistRttAverage,
       "nbEthOamDmHistRttSum2": nbEthOamDmHistRttSum2,
       "nbEthOamDmHistDSJittNumber": nbEthOamDmHistDSJittNumber,
       "nbEthOamDmHistDSJittMin": nbEthOamDmHistDSJittMin,
       "nbEthOamDmHistDSJittMax": nbEthOamDmHistDSJittMax,
       "nbEthOamDmHistDSJittAverage": nbEthOamDmHistDSJittAverage,
       "nbEthOamDmHistDSJittSum2": nbEthOamDmHistDSJittSum2,
       "nbEthOamDmHistDSJittIA": nbEthOamDmHistDSJittIA,
       "nbEthOamDmHistSDJittNumber": nbEthOamDmHistSDJittNumber,
       "nbEthOamDmHistSDJittMin": nbEthOamDmHistSDJittMin,
       "nbEthOamDmHistSDJittMax": nbEthOamDmHistSDJittMax,
       "nbEthOamDmHistSDJittAverage": nbEthOamDmHistSDJittAverage,
       "nbEthOamDmHistSDJittSum2": nbEthOamDmHistSDJittSum2,
       "nbEthOamDmHistSDJittIA": nbEthOamDmHistSDJittIA,
       "nbEthOamDmHistPcktLoss": nbEthOamDmHistPcktLoss,
       "nbEthOamDmHistType": nbEthOamDmHistType,
       "nbEthOamDmHistPriority": nbEthOamDmHistPriority,
       "nbEthOamDmLastTable": nbEthOamDmLastTable,
       "nbEthOamDmLastEntry": nbEthOamDmLastEntry,
       "nbEthOamDmLastStarted": nbEthOamDmLastStarted,
       "nbEthOamDmLastDestMepId": nbEthOamDmLastDestMepId,
       "nbEthOamDmLastDestMepMac": nbEthOamDmLastDestMepMac,
       "nbEthOamDmLastMsgTransmitted": nbEthOamDmLastMsgTransmitted,
       "nbEthOamDmLastMsgReceived": nbEthOamDmLastMsgReceived,
       "nbEthOamDmLastRttMin": nbEthOamDmLastRttMin,
       "nbEthOamDmLastRttMax": nbEthOamDmLastRttMax,
       "nbEthOamDmLastRttAverage": nbEthOamDmLastRttAverage,
       "nbEthOamDmLastRttSum2": nbEthOamDmLastRttSum2,
       "nbEthOamDmLastDSJittNumber": nbEthOamDmLastDSJittNumber,
       "nbEthOamDmLastDSJittMin": nbEthOamDmLastDSJittMin,
       "nbEthOamDmLastDSJittMax": nbEthOamDmLastDSJittMax,
       "nbEthOamDmLastDSJittAverage": nbEthOamDmLastDSJittAverage,
       "nbEthOamDmLastDSJittSum2": nbEthOamDmLastDSJittSum2,
       "nbEthOamDmLastDSJittIA": nbEthOamDmLastDSJittIA,
       "nbEthOamDmLastSDJittNumber": nbEthOamDmLastSDJittNumber,
       "nbEthOamDmLastSDJittMin": nbEthOamDmLastSDJittMin,
       "nbEthOamDmLastSDJittMax": nbEthOamDmLastSDJittMax,
       "nbEthOamDmLastSDJittAverage": nbEthOamDmLastSDJittAverage,
       "nbEthOamDmLastSDJittSum2": nbEthOamDmLastSDJittSum2,
       "nbEthOamDmLastSDJittIA": nbEthOamDmLastSDJittIA,
       "nbEthOamDmLastPcktLoss": nbEthOamDmLastPcktLoss,
       "nbEthOamDmLastType": nbEthOamDmLastType,
       "nbEthOamDmLastPriority": nbEthOamDmLastPriority,
       "nbEthOamDmLastHistIndx": nbEthOamDmLastHistIndx,
       "nbEthOamDmConfExtTable": nbEthOamDmConfExtTable,
       "nbEthOamDmConfExtEntry": nbEthOamDmConfExtEntry,
       "nbEthOamDmConfDestMepList": nbEthOamDmConfDestMepList,
       "nbEthOamDmHcHistTable": nbEthOamDmHcHistTable,
       "nbEthOamDmHcHistEntry": nbEthOamDmHcHistEntry,
       "nbEthOamDmHcHistRttMin": nbEthOamDmHcHistRttMin,
       "nbEthOamDmHcHistRttMax": nbEthOamDmHcHistRttMax,
       "nbEthOamDmHcHistRttAverage": nbEthOamDmHcHistRttAverage,
       "nbEthOamDmHcHistRttSum2": nbEthOamDmHcHistRttSum2,
       "nbEthOamDmHcHistDSJittMin": nbEthOamDmHcHistDSJittMin,
       "nbEthOamDmHcHistDSJittMax": nbEthOamDmHcHistDSJittMax,
       "nbEthOamDmHcHistDSJittAverage": nbEthOamDmHcHistDSJittAverage,
       "nbEthOamDmHcHistDSJittSum2": nbEthOamDmHcHistDSJittSum2,
       "nbEthOamDmHcHistDSJittIA": nbEthOamDmHcHistDSJittIA,
       "nbEthOamDmHcHistSDJittMin": nbEthOamDmHcHistSDJittMin,
       "nbEthOamDmHcHistSDJittMax": nbEthOamDmHcHistSDJittMax,
       "nbEthOamDmHcHistSDJittAverage": nbEthOamDmHcHistSDJittAverage,
       "nbEthOamDmHcHistSDJittSum2": nbEthOamDmHcHistSDJittSum2,
       "nbEthOamDmHcHistSDJittIA": nbEthOamDmHcHistSDJittIA,
       "nbEthOamDmHcLastTable": nbEthOamDmHcLastTable,
       "nbEthOamDmHcLastEntry": nbEthOamDmHcLastEntry,
       "nbEthOamDmHcLastRttMin": nbEthOamDmHcLastRttMin,
       "nbEthOamDmHcLastRttMax": nbEthOamDmHcLastRttMax,
       "nbEthOamDmHcLastRttAverage": nbEthOamDmHcLastRttAverage,
       "nbEthOamDmHcLastRttSum2": nbEthOamDmHcLastRttSum2,
       "nbEthOamDmHcLastDSJittMin": nbEthOamDmHcLastDSJittMin,
       "nbEthOamDmHcLastDSJittMax": nbEthOamDmHcLastDSJittMax,
       "nbEthOamDmHcLastDSJittAverage": nbEthOamDmHcLastDSJittAverage,
       "nbEthOamDmHcLastDSJittSum2": nbEthOamDmHcLastDSJittSum2,
       "nbEthOamDmHcLastDSJittIA": nbEthOamDmHcLastDSJittIA,
       "nbEthOamDmHcLastSDJittMin": nbEthOamDmHcLastSDJittMin,
       "nbEthOamDmHcLastSDJittMax": nbEthOamDmHcLastSDJittMax,
       "nbEthOamDmHcLastSDJittAverage": nbEthOamDmHcLastSDJittAverage,
       "nbEthOamDmHcLastSDJittSum2": nbEthOamDmHcLastSDJittSum2,
       "nbEthOamDmHcLastSDJittIA": nbEthOamDmHcLastSDJittIA,
       "nbEthOamDmHcLastRunStatus": nbEthOamDmHcLastRunStatus,
       "nbEthOamServiceTable": nbEthOamServiceTable,
       "nbEthOamServiceEntry": nbEthOamServiceEntry,
       "nbEthOamServiceDmResponderSL": nbEthOamServiceDmResponderSL,
       "nbEthOamServiceLbResponderSL": nbEthOamServiceLbResponderSL,
       "nbEthOamServiceLmResponderSL": nbEthOamServiceLmResponderSL,
       "nbEthOamTrapTable": nbEthOamTrapTable,
       "nbEthOamTrapEntry": nbEthOamTrapEntry,
       "nbEthOamTrapTrapGeneration": nbEthOamTrapTrapGeneration,
       "nbEthOamTrapCcmHighestPrDefect": nbEthOamTrapCcmHighestPrDefect,
       "nbEthOamTrapCcmAlarmType": nbEthOamTrapCcmAlarmType,
       "nbEthOamTrapDmmReason": nbEthOamTrapDmmReason,
       "nbEthOamFdRiseThold": nbEthOamFdRiseThold,
       "nbEthOamFdFallThold": nbEthOamFdFallThold,
       "nbEthOamDSJittRiseThold": nbEthOamDSJittRiseThold,
       "nbEthOamDSJittFallThold": nbEthOamDSJittFallThold,
       "nbEthOamDSJittSum2RiseThold": nbEthOamDSJittSum2RiseThold,
       "nbEthOamDSJittSum2FallThold": nbEthOamDSJittSum2FallThold,
       "nbEthOamSDJittRiseThold": nbEthOamSDJittRiseThold,
       "nbEthOamSDJittFallThold": nbEthOamSDJittFallThold,
       "nbEthOamSDJittSum2RiseThold": nbEthOamSDJittSum2RiseThold,
       "nbEthOamSDJittSum2FallThold": nbEthOamSDJittSum2FallThold,
       "nbEthOamPcktLossRiseThold": nbEthOamPcktLossRiseThold,
       "nbEthOamPcktLossFallThold": nbEthOamPcktLossFallThold,
       "nbEthOamConformance": nbEthOamConformance,
       "nbEthOamMIBCompliances": nbEthOamMIBCompliances,
       "nbEthOamMIBCompliance": nbEthOamMIBCompliance,
       "nbEthOamMIBGroups": nbEthOamMIBGroups,
       "nbEthOamMandatoryGroup": nbEthOamMandatoryGroup,
       "nbEthOamNotificationsGroup": nbEthOamNotificationsGroup}
)
