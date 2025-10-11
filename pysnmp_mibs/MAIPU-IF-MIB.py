# SNMP MIB module (MAIPU-IF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/maipu/MAIPU-IF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:11:14 2025
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

(ifDescr,
 ifIndex,
 ifType) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifDescr",
    "ifIndex",
    "ifType")

(mpMgmt,) = mibBuilder.importSymbols(
    "MAIPU-SMI",
    "mpMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(snmpTraps,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "snmpTraps")

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

mpIfMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EthConfTable_Object = MibTable
ethConfTable = _EthConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1)
)
if mibBuilder.loadTexts:
    ethConfTable.setStatus("current")
_EthConfEntry_Object = MibTableRow
ethConfEntry = _EthConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1)
)
ethConfEntry.setIndexNames(
    (0, "MAIPU-IF-MIB", "ethConfIfIndex"),
)
if mibBuilder.loadTexts:
    ethConfEntry.setStatus("current")
_EthConfIfIndex_Type = Integer32
_EthConfIfIndex_Object = MibTableColumn
ethConfIfIndex = _EthConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1, 1),
    _EthConfIfIndex_Type()
)
ethConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethConfIfIndex.setStatus("current")


class _EthMtu_Type(Integer32):
    """Custom type ethMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 18000),
    )


_EthMtu_Type.__name__ = "Integer32"
_EthMtu_Object = MibTableColumn
ethMtu = _EthMtu_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1, 2),
    _EthMtu_Type()
)
ethMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethMtu.setStatus("current")
_EthDescription_Type = DisplayString
_EthDescription_Object = MibTableColumn
ethDescription = _EthDescription_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1, 3),
    _EthDescription_Type()
)
ethDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDescription.setStatus("current")
_EthUcastAddr_Type = IpAddress
_EthUcastAddr_Object = MibTableColumn
ethUcastAddr = _EthUcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1, 4),
    _EthUcastAddr_Type()
)
ethUcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethUcastAddr.setStatus("current")
_EthUcastMask_Type = IpAddress
_EthUcastMask_Object = MibTableColumn
ethUcastMask = _EthUcastMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1, 5),
    _EthUcastMask_Type()
)
ethUcastMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethUcastMask.setStatus("current")
_EthUcastUnnumber_Type = Integer32
_EthUcastUnnumber_Object = MibTableColumn
ethUcastUnnumber = _EthUcastUnnumber_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1, 6),
    _EthUcastUnnumber_Type()
)
ethUcastUnnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethUcastUnnumber.setStatus("current")
_EthBcastAddr_Type = IpAddress
_EthBcastAddr_Object = MibTableColumn
ethBcastAddr = _EthBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1, 7),
    _EthBcastAddr_Type()
)
ethBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethBcastAddr.setStatus("current")


class _EthMetric_Type(Integer32):
    """Custom type ethMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_EthMetric_Type.__name__ = "Integer32"
_EthMetric_Object = MibTableColumn
ethMetric = _EthMetric_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1, 8),
    _EthMetric_Type()
)
ethMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethMetric.setStatus("current")


class _EthDuplex_Type(Integer32):
    """Custom type ethDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2),
          ("auto", 3))
    )


_EthDuplex_Type.__name__ = "Integer32"
_EthDuplex_Object = MibTableColumn
ethDuplex = _EthDuplex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1, 9),
    _EthDuplex_Type()
)
ethDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethDuplex.setStatus("current")
_EthRate_Type = Integer32
_EthRate_Object = MibTableColumn
ethRate = _EthRate_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 1, 1, 10),
    _EthRate_Type()
)
ethRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ethRate.setStatus("current")
_SecondaryTable_Object = MibTable
secondaryTable = _SecondaryTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 2)
)
if mibBuilder.loadTexts:
    secondaryTable.setStatus("current")
_SecondaryEntry_Object = MibTableRow
secondaryEntry = _SecondaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 2, 1)
)
secondaryEntry.setIndexNames(
    (0, "MAIPU-IF-MIB", "secondaryIfIndex"),
    (0, "MAIPU-IF-MIB", "secondaryIp"),
)
if mibBuilder.loadTexts:
    secondaryEntry.setStatus("current")
_SecondaryIfIndex_Type = Integer32
_SecondaryIfIndex_Object = MibTableColumn
secondaryIfIndex = _SecondaryIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 2, 1, 1),
    _SecondaryIfIndex_Type()
)
secondaryIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secondaryIfIndex.setStatus("current")
_SecondaryIp_Type = IpAddress
_SecondaryIp_Object = MibTableColumn
secondaryIp = _SecondaryIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 2, 1, 2),
    _SecondaryIp_Type()
)
secondaryIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secondaryIp.setStatus("current")
_SecondaryMask_Type = IpAddress
_SecondaryMask_Object = MibTableColumn
secondaryMask = _SecondaryMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 2, 1, 3),
    _SecondaryMask_Type()
)
secondaryMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secondaryMask.setStatus("current")
_SecondaryStatus_Type = RowStatus
_SecondaryStatus_Object = MibTableColumn
secondaryStatus = _SecondaryStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 2, 1, 4),
    _SecondaryStatus_Type()
)
secondaryStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    secondaryStatus.setStatus("current")
_SerialConfTable_Object = MibTable
serialConfTable = _SerialConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3)
)
if mibBuilder.loadTexts:
    serialConfTable.setStatus("current")
_SerialConfEntry_Object = MibTableRow
serialConfEntry = _SerialConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1)
)
serialConfEntry.setIndexNames(
    (0, "MAIPU-IF-MIB", "serialConfIndex"),
)
if mibBuilder.loadTexts:
    serialConfEntry.setStatus("current")
_SerialConfIndex_Type = Integer32
_SerialConfIndex_Object = MibTableColumn
serialConfIndex = _SerialConfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 1),
    _SerialConfIndex_Type()
)
serialConfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    serialConfIndex.setStatus("current")


class _SerialMtu_Type(Integer32):
    """Custom type serialMtu based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(64, 18000),
    )


_SerialMtu_Type.__name__ = "Integer32"
_SerialMtu_Object = MibTableColumn
serialMtu = _SerialMtu_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 2),
    _SerialMtu_Type()
)
serialMtu.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialMtu.setStatus("current")
_SerialDescription_Type = DisplayString
_SerialDescription_Object = MibTableColumn
serialDescription = _SerialDescription_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 3),
    _SerialDescription_Type()
)
serialDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDescription.setStatus("current")
_SerialUcastAddr_Type = IpAddress
_SerialUcastAddr_Object = MibTableColumn
serialUcastAddr = _SerialUcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 4),
    _SerialUcastAddr_Type()
)
serialUcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialUcastAddr.setStatus("current")
_SerialUcastMask_Type = IpAddress
_SerialUcastMask_Object = MibTableColumn
serialUcastMask = _SerialUcastMask_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 5),
    _SerialUcastMask_Type()
)
serialUcastMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialUcastMask.setStatus("current")
_SerialUnnumber_Type = Integer32
_SerialUnnumber_Object = MibTableColumn
serialUnnumber = _SerialUnnumber_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 6),
    _SerialUnnumber_Type()
)
serialUnnumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialUnnumber.setStatus("current")
_SerialBcastAddr_Type = IpAddress
_SerialBcastAddr_Object = MibTableColumn
serialBcastAddr = _SerialBcastAddr_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 7),
    _SerialBcastAddr_Type()
)
serialBcastAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialBcastAddr.setStatus("current")


class _SerialMetric_Type(Integer32):
    """Custom type serialMetric based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SerialMetric_Type.__name__ = "Integer32"
_SerialMetric_Object = MibTableColumn
serialMetric = _SerialMetric_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 8),
    _SerialMetric_Type()
)
serialMetric.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialMetric.setStatus("current")
_SerialClockSpeed_Type = Integer32
_SerialClockSpeed_Object = MibTableColumn
serialClockSpeed = _SerialClockSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 9),
    _SerialClockSpeed_Type()
)
serialClockSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialClockSpeed.setStatus("current")


class _SerialClockLine_Type(Integer32):
    """Custom type serialClockLine based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("multiplex", 2))
    )


_SerialClockLine_Type.__name__ = "Integer32"
_SerialClockLine_Object = MibTableColumn
serialClockLine = _SerialClockLine_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 10),
    _SerialClockLine_Type()
)
serialClockLine.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialClockLine.setStatus("current")


class _SerialClockInvert_Type(Integer32):
    """Custom type serialClockInvert based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("restore", 1),
          ("invert", 2))
    )


_SerialClockInvert_Type.__name__ = "Integer32"
_SerialClockInvert_Object = MibTableColumn
serialClockInvert = _SerialClockInvert_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 11),
    _SerialClockInvert_Type()
)
serialClockInvert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialClockInvert.setStatus("current")


class _SerialNrziEncode_Type(Integer32):
    """Custom type serialNrziEncode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("nrz", 1),
          ("nrzi", 2))
    )


_SerialNrziEncode_Type.__name__ = "Integer32"
_SerialNrziEncode_Object = MibTableColumn
serialNrziEncode = _SerialNrziEncode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 12),
    _SerialNrziEncode_Type()
)
serialNrziEncode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialNrziEncode.setStatus("current")


class _SerialIdleMode_Type(Integer32):
    """Custom type serialIdleMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("marks", 1),
          ("flags", 2))
    )


_SerialIdleMode_Type.__name__ = "Integer32"
_SerialIdleMode_Object = MibTableColumn
serialIdleMode = _SerialIdleMode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 13),
    _SerialIdleMode_Type()
)
serialIdleMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialIdleMode.setStatus("current")


class _SerialSpeed_Type(Integer32):
    """Custom type serialSpeed based on Integer32"""
    defaultValue = 115200


_SerialSpeed_Type.__name__ = "Integer32"
_SerialSpeed_Object = MibTableColumn
serialSpeed = _SerialSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 14),
    _SerialSpeed_Type()
)
serialSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialSpeed.setStatus("current")


class _SerialDataBits_Type(Integer32):
    """Custom type serialDataBits based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_SerialDataBits_Type.__name__ = "Integer32"
_SerialDataBits_Object = MibTableColumn
serialDataBits = _SerialDataBits_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 15),
    _SerialDataBits_Type()
)
serialDataBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialDataBits.setStatus("current")


class _SerialStopBits_Type(Integer32):
    """Custom type serialStopBits based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_SerialStopBits_Type.__name__ = "Integer32"
_SerialStopBits_Object = MibTableColumn
serialStopBits = _SerialStopBits_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 16),
    _SerialStopBits_Type()
)
serialStopBits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialStopBits.setStatus("current")


class _SerialParity_Type(Integer32):
    """Custom type serialParity based on Integer32"""
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
          ("odd", 2),
          ("even", 3),
          ("space", 4),
          ("mark", 5))
    )


_SerialParity_Type.__name__ = "Integer32"
_SerialParity_Object = MibTableColumn
serialParity = _SerialParity_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 17),
    _SerialParity_Type()
)
serialParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialParity.setStatus("current")


class _SerialFlowCtl_Type(Integer32):
    """Custom type serialFlowCtl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("software", 2),
          ("hardware", 3))
    )


_SerialFlowCtl_Type.__name__ = "Integer32"
_SerialFlowCtl_Object = MibTableColumn
serialFlowCtl = _SerialFlowCtl_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 18),
    _SerialFlowCtl_Type()
)
serialFlowCtl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialFlowCtl.setStatus("current")


class _SerialMru_Type(Integer32):
    """Custom type serialMru based on Integer32"""
    defaultValue = 1500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(128, 4096),
    )


_SerialMru_Type.__name__ = "Integer32"
_SerialMru_Object = MibTableColumn
serialMru = _SerialMru_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 19),
    _SerialMru_Type()
)
serialMru.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialMru.setStatus("current")


class _SerialStartCharacter_Type(Integer32):
    """Custom type serialStartCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SerialStartCharacter_Type.__name__ = "Integer32"
_SerialStartCharacter_Object = MibTableColumn
serialStartCharacter = _SerialStartCharacter_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 20),
    _SerialStartCharacter_Type()
)
serialStartCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialStartCharacter.setStatus("current")


class _SerialStopCharacter_Type(Integer32):
    """Custom type serialStopCharacter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_SerialStopCharacter_Type.__name__ = "Integer32"
_SerialStopCharacter_Object = MibTableColumn
serialStopCharacter = _SerialStopCharacter_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 21),
    _SerialStopCharacter_Type()
)
serialStopCharacter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialStopCharacter.setStatus("current")


class _SerialEncapsulation_Type(Integer32):
    """Custom type serialEncapsulation based on Integer32"""
    defaultValue = 6

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
              10)
        )
    )
    namedValues = NamedValues(
        *(("slip", 1),
          ("ppp", 2),
          ("frame-relay", 3),
          ("x25", 4),
          ("lapb", 5),
          ("hdlc", 6),
          ("sdlcPri", 7),
          ("sdlcSec", 8),
          ("sdlc", 9),
          ("trans", 10))
    )


_SerialEncapsulation_Type.__name__ = "Integer32"
_SerialEncapsulation_Object = MibTableColumn
serialEncapsulation = _SerialEncapsulation_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 22),
    _SerialEncapsulation_Type()
)
serialEncapsulation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialEncapsulation.setStatus("current")


class _SerialPhyLayer_Type(Integer32):
    """Custom type serialPhyLayer based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("syn", 1),
          ("asyn", 2))
    )


_SerialPhyLayer_Type.__name__ = "Integer32"
_SerialPhyLayer_Object = MibTableColumn
serialPhyLayer = _SerialPhyLayer_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 23),
    _SerialPhyLayer_Type()
)
serialPhyLayer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialPhyLayer.setStatus("current")


class _SerialIpTcpHeadCompress_Type(Integer32):
    """Custom type serialIpTcpHeadCompress based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("noCompress", 1),
          ("compress", 2),
          ("compressRx", 3))
    )


_SerialIpTcpHeadCompress_Type.__name__ = "Integer32"
_SerialIpTcpHeadCompress_Object = MibTableColumn
serialIpTcpHeadCompress = _SerialIpTcpHeadCompress_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 24),
    _SerialIpTcpHeadCompress_Type()
)
serialIpTcpHeadCompress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialIpTcpHeadCompress.setStatus("current")


class _SerialBackup_Type(Integer32):
    """Custom type serialBackup based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primary", 1),
          ("backup", 2),
          ("none", 3))
    )


_SerialBackup_Type.__name__ = "Integer32"
_SerialBackup_Object = MibTableColumn
serialBackup = _SerialBackup_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 25),
    _SerialBackup_Type()
)
serialBackup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialBackup.setStatus("current")
_SerialBackupIf_Type = Integer32
_SerialBackupIf_Object = MibTableColumn
serialBackupIf = _SerialBackupIf_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 26),
    _SerialBackupIf_Type()
)
serialBackupIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialBackupIf.setStatus("current")


class _SerialBackupAct_Type(Unsigned32):
    """Custom type serialBackupAct based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_SerialBackupAct_Type.__name__ = "Unsigned32"
_SerialBackupAct_Object = MibTableColumn
serialBackupAct = _SerialBackupAct_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 27),
    _SerialBackupAct_Type()
)
serialBackupAct.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialBackupAct.setStatus("current")


class _SerialBackupDeact_Type(Unsigned32):
    """Custom type serialBackupDeact based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967294),
    )


_SerialBackupDeact_Type.__name__ = "Unsigned32"
_SerialBackupDeact_Object = MibTableColumn
serialBackupDeact = _SerialBackupDeact_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 28),
    _SerialBackupDeact_Type()
)
serialBackupDeact.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialBackupDeact.setStatus("current")


class _SerialQos_Type(Integer32):
    """Custom type serialQos based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("fifo", 1),
          ("wfq", 2),
          ("pq", 3))
    )


_SerialQos_Type.__name__ = "Integer32"
_SerialQos_Object = MibTableColumn
serialQos = _SerialQos_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 29),
    _SerialQos_Type()
)
serialQos.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialQos.setStatus("current")


class _SerialQosList_Type(Integer32):
    """Custom type serialQosList based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_SerialQosList_Type.__name__ = "Integer32"
_SerialQosList_Object = MibTableColumn
serialQosList = _SerialQosList_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 30),
    _SerialQosList_Type()
)
serialQosList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialQosList.setStatus("current")


class _SerialTxHigh_Type(Integer32):
    """Custom type serialTxHigh based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 500),
    )


_SerialTxHigh_Type.__name__ = "Integer32"
_SerialTxHigh_Object = MibTableColumn
serialTxHigh = _SerialTxHigh_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 31),
    _SerialTxHigh_Type()
)
serialTxHigh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTxHigh.setStatus("current")


class _SerialTxMedium_Type(Integer32):
    """Custom type serialTxMedium based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 500),
    )


_SerialTxMedium_Type.__name__ = "Integer32"
_SerialTxMedium_Object = MibTableColumn
serialTxMedium = _SerialTxMedium_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 32),
    _SerialTxMedium_Type()
)
serialTxMedium.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTxMedium.setStatus("current")


class _SerialTxNormal_Type(Integer32):
    """Custom type serialTxNormal based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 500),
    )


_SerialTxNormal_Type.__name__ = "Integer32"
_SerialTxNormal_Object = MibTableColumn
serialTxNormal = _SerialTxNormal_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 33),
    _SerialTxNormal_Type()
)
serialTxNormal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTxNormal.setStatus("current")


class _SerialTxLow_Type(Integer32):
    """Custom type serialTxLow based on Integer32"""
    defaultValue = 50

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 500),
    )


_SerialTxLow_Type.__name__ = "Integer32"
_SerialTxLow_Object = MibTableColumn
serialTxLow = _SerialTxLow_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 34),
    _SerialTxLow_Type()
)
serialTxLow.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTxLow.setStatus("current")


class _SerialTbds_Type(Integer32):
    """Custom type serialTbds based on Integer32"""
    defaultValue = 16

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 16),
    )


_SerialTbds_Type.__name__ = "Integer32"
_SerialTbds_Object = MibTableColumn
serialTbds = _SerialTbds_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 3, 1, 35),
    _SerialTbds_Type()
)
serialTbds.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    serialTbds.setStatus("current")
_TerminalTable_Object = MibTable
terminalTable = _TerminalTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5)
)
if mibBuilder.loadTexts:
    terminalTable.setStatus("current")
_TerminalEntry_Object = MibTableRow
terminalEntry = _TerminalEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1)
)
terminalEntry.setIndexNames(
    (0, "MAIPU-IF-MIB", "termIndex"),
)
if mibBuilder.loadTexts:
    terminalEntry.setStatus("current")
_TermIndex_Type = Integer32
_TermIndex_Object = MibTableColumn
termIndex = _TermIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 1),
    _TermIndex_Type()
)
termIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termIndex.setStatus("current")


class _TermStatus_Type(Integer32):
    """Custom type termStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_TermStatus_Type.__name__ = "Integer32"
_TermStatus_Object = MibTableColumn
termStatus = _TermStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 2),
    _TermStatus_Type()
)
termStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termStatus.setStatus("current")
_TermSpeed_Type = Integer32
_TermSpeed_Object = MibTableColumn
termSpeed = _TermSpeed_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 3),
    _TermSpeed_Type()
)
termSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termSpeed.setStatus("current")


class _TermDatabits_Type(Integer32):
    """Custom type termDatabits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5, 8),
    )


_TermDatabits_Type.__name__ = "Integer32"
_TermDatabits_Object = MibTableColumn
termDatabits = _TermDatabits_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 4),
    _TermDatabits_Type()
)
termDatabits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termDatabits.setStatus("current")


class _TermStopbits_Type(Integer32):
    """Custom type termStopbits based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_TermStopbits_Type.__name__ = "Integer32"
_TermStopbits_Object = MibTableColumn
termStopbits = _TermStopbits_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 5),
    _TermStopbits_Type()
)
termStopbits.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termStopbits.setStatus("current")


class _TermParity_Type(Integer32):
    """Custom type termParity based on Integer32"""
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
        *(("even", 1),
          ("mark", 2),
          ("none", 3),
          ("odd", 4),
          ("space", 5))
    )


_TermParity_Type.__name__ = "Integer32"
_TermParity_Object = MibTableColumn
termParity = _TermParity_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 6),
    _TermParity_Type()
)
termParity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termParity.setStatus("current")


class _TermFlowCtrl_Type(Integer32):
    """Custom type termFlowCtrl based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("hard", 1),
          ("soft", 2),
          ("none", 3))
    )


_TermFlowCtrl_Type.__name__ = "Integer32"
_TermFlowCtrl_Object = MibTableColumn
termFlowCtrl = _TermFlowCtrl_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 7),
    _TermFlowCtrl_Type()
)
termFlowCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termFlowCtrl.setStatus("current")


class _TermLineOn_Type(Integer32):
    """Custom type termLineOn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("cts", 1),
          ("dcd", 2),
          ("dsr", 3))
    )


_TermLineOn_Type.__name__ = "Integer32"
_TermLineOn_Object = MibTableColumn
termLineOn = _TermLineOn_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 8),
    _TermLineOn_Type()
)
termLineOn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termLineOn.setStatus("current")


class _TermRxBuf_Type(Integer32):
    """Custom type termRxBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 8192),
    )


_TermRxBuf_Type.__name__ = "Integer32"
_TermRxBuf_Object = MibTableColumn
termRxBuf = _TermRxBuf_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 9),
    _TermRxBuf_Type()
)
termRxBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termRxBuf.setStatus("current")


class _TermTxBuf_Type(Integer32):
    """Custom type termTxBuf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(32, 8192),
    )


_TermTxBuf_Type.__name__ = "Integer32"
_TermTxBuf_Object = MibTableColumn
termTxBuf = _TermTxBuf_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 10),
    _TermTxBuf_Type()
)
termTxBuf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termTxBuf.setStatus("current")


class _TermPrint_Type(Integer32):
    """Custom type termPrint based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_TermPrint_Type.__name__ = "Integer32"
_TermPrint_Object = MibTableColumn
termPrint = _TermPrint_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 11),
    _TermPrint_Type()
)
termPrint.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termPrint.setStatus("current")


class _TermAutoLink_Type(Integer32):
    """Custom type termAutoLink based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_TermAutoLink_Type.__name__ = "Integer32"
_TermAutoLink_Object = MibTableColumn
termAutoLink = _TermAutoLink_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 12),
    _TermAutoLink_Type()
)
termAutoLink.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termAutoLink.setStatus("current")


class _TermAutoLinkNo_Type(Integer32):
    """Custom type termAutoLinkNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TermAutoLinkNo_Type.__name__ = "Integer32"
_TermAutoLinkNo_Object = MibTableColumn
termAutoLinkNo = _TermAutoLinkNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 13),
    _TermAutoLinkNo_Type()
)
termAutoLinkNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termAutoLinkNo.setStatus("current")


class _TermRxDelay_Type(Integer32):
    """Custom type termRxDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_TermRxDelay_Type.__name__ = "Integer32"
_TermRxDelay_Object = MibTableColumn
termRxDelay = _TermRxDelay_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 14),
    _TermRxDelay_Type()
)
termRxDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termRxDelay.setStatus("current")
_TermEscChar_Type = OctetString
_TermEscChar_Object = MibTableColumn
termEscChar = _TermEscChar_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 15),
    _TermEscChar_Type()
)
termEscChar.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termEscChar.setStatus("current")
_TermLocalHost_Type = IpAddress
_TermLocalHost_Object = MibTableColumn
termLocalHost = _TermLocalHost_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 16),
    _TermLocalHost_Type()
)
termLocalHost.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termLocalHost.setStatus("current")
_TermTxBytes_Type = Integer32
_TermTxBytes_Object = MibTableColumn
termTxBytes = _TermTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 17),
    _TermTxBytes_Type()
)
termTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termTxBytes.setStatus("current")
_TermRxBytes_Type = Integer32
_TermRxBytes_Object = MibTableColumn
termRxBytes = _TermRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 18),
    _TermRxBytes_Type()
)
termRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termRxBytes.setStatus("current")
_TermRowStatus_Type = RowStatus
_TermRowStatus_Object = MibTableColumn
termRowStatus = _TermRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 5, 1, 19),
    _TermRowStatus_Type()
)
termRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    termRowStatus.setStatus("current")
_TerminalHostTable_Object = MibTable
terminalHostTable = _TerminalHostTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6)
)
if mibBuilder.loadTexts:
    terminalHostTable.setStatus("current")
_TerminalHostEntry_Object = MibTableRow
terminalHostEntry = _TerminalHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1)
)
terminalHostEntry.setIndexNames(
    (0, "MAIPU-IF-MIB", "termHostIndex"),
    (0, "MAIPU-IF-MIB", "termHostNo"),
)
if mibBuilder.loadTexts:
    terminalHostEntry.setStatus("current")
_TermHostIndex_Type = Integer32
_TermHostIndex_Object = MibTableColumn
termHostIndex = _TermHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 1),
    _TermHostIndex_Type()
)
termHostIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termHostIndex.setStatus("current")


class _TermHostNo_Type(Integer32):
    """Custom type termHostNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_TermHostNo_Type.__name__ = "Integer32"
_TermHostNo_Object = MibTableColumn
termHostNo = _TermHostNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 2),
    _TermHostNo_Type()
)
termHostNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    termHostNo.setStatus("current")


class _TermHostName_Type(DisplayString):
    """Custom type termHostName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TermHostName_Type.__name__ = "DisplayString"
_TermHostName_Object = MibTableColumn
termHostName = _TermHostName_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 3),
    _TermHostName_Type()
)
termHostName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostName.setStatus("current")
_TermHostIp_Type = IpAddress
_TermHostIp_Object = MibTableColumn
termHostIp = _TermHostIp_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 4),
    _TermHostIp_Type()
)
termHostIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostIp.setStatus("current")
_TermHostPort_Type = Integer32
_TermHostPort_Object = MibTableColumn
termHostPort = _TermHostPort_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 5),
    _TermHostPort_Type()
)
termHostPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostPort.setStatus("current")


class _TermHostType_Type(Integer32):
    """Custom type termHostType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("telnet", 1),
          ("rlogin", 2),
          ("fixterm", 3))
    )


_TermHostType_Type.__name__ = "Integer32"
_TermHostType_Object = MibTableColumn
termHostType = _TermHostType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 6),
    _TermHostType_Type()
)
termHostType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostType.setStatus("current")


class _TermHostTelnetType_Type(DisplayString):
    """Custom type termHostTelnetType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TermHostTelnetType_Type.__name__ = "DisplayString"
_TermHostTelnetType_Object = MibTableColumn
termHostTelnetType = _TermHostTelnetType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 7),
    _TermHostTelnetType_Type()
)
termHostTelnetType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostTelnetType.setStatus("current")


class _TermHostStauts_Type(Integer32):
    """Custom type termHostStauts based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("standby", 1),
          ("connect", 2),
          ("disconnet", 3))
    )


_TermHostStauts_Type.__name__ = "Integer32"
_TermHostStauts_Object = MibTableColumn
termHostStauts = _TermHostStauts_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 8),
    _TermHostStauts_Type()
)
termHostStauts.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostStauts.setStatus("current")


class _TermHostFixtermType_Type(Integer32):
    """Custom type termHostFixtermType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("client", 1),
          ("server", 2))
    )


_TermHostFixtermType_Type.__name__ = "Integer32"
_TermHostFixtermType_Object = MibTableColumn
termHostFixtermType = _TermHostFixtermType_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 9),
    _TermHostFixtermType_Type()
)
termHostFixtermType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostFixtermType.setStatus("current")


class _TermHostFixtermAuth_Type(Integer32):
    """Custom type termHostFixtermAuth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("authentic", 1),
          ("non-authentic", 2))
    )


_TermHostFixtermAuth_Type.__name__ = "Integer32"
_TermHostFixtermAuth_Object = MibTableColumn
termHostFixtermAuth = _TermHostFixtermAuth_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 10),
    _TermHostFixtermAuth_Type()
)
termHostFixtermAuth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostFixtermAuth.setStatus("current")
_TermHostFixtermChars_Type = OctetString
_TermHostFixtermChars_Object = MibTableColumn
termHostFixtermChars = _TermHostFixtermChars_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 11),
    _TermHostFixtermChars_Type()
)
termHostFixtermChars.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostFixtermChars.setStatus("current")


class _TermHostRloginUser_Type(Integer32):
    """Custom type termHostRloginUser based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_TermHostRloginUser_Type.__name__ = "Integer32"
_TermHostRloginUser_Object = MibTableColumn
termHostRloginUser = _TermHostRloginUser_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 12),
    _TermHostRloginUser_Type()
)
termHostRloginUser.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostRloginUser.setStatus("current")


class _TermHostRloginLocal_Type(DisplayString):
    """Custom type termHostRloginLocal based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TermHostRloginLocal_Type.__name__ = "DisplayString"
_TermHostRloginLocal_Object = MibTableColumn
termHostRloginLocal = _TermHostRloginLocal_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 13),
    _TermHostRloginLocal_Type()
)
termHostRloginLocal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostRloginLocal.setStatus("current")


class _TermHostRloginRemote_Type(DisplayString):
    """Custom type termHostRloginRemote based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 40),
    )


_TermHostRloginRemote_Type.__name__ = "DisplayString"
_TermHostRloginRemote_Object = MibTableColumn
termHostRloginRemote = _TermHostRloginRemote_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 14),
    _TermHostRloginRemote_Type()
)
termHostRloginRemote.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    termHostRloginRemote.setStatus("current")
_TermHostRowStatus_Type = RowStatus
_TermHostRowStatus_Object = MibTableColumn
termHostRowStatus = _TermHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 6, 1, 15),
    _TermHostRowStatus_Type()
)
termHostRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    termHostRowStatus.setStatus("current")
_LineConfTable_Object = MibTable
lineConfTable = _LineConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 7)
)
if mibBuilder.loadTexts:
    lineConfTable.setStatus("current")
_LineConfEntry_Object = MibTableRow
lineConfEntry = _LineConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 7, 1)
)
lineConfEntry.setIndexNames(
    (0, "MAIPU-IF-MIB", "lineConfNo"),
)
if mibBuilder.loadTexts:
    lineConfEntry.setStatus("current")
_LineConfNo_Type = Integer32
_LineConfNo_Object = MibTableColumn
lineConfNo = _LineConfNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 7, 1, 1),
    _LineConfNo_Type()
)
lineConfNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lineConfNo.setStatus("current")


class _LineConfMode_Type(Integer32):
    """Custom type lineConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interface", 1),
          ("terminal", 2),
          ("free", 3))
    )


_LineConfMode_Type.__name__ = "Integer32"
_LineConfMode_Object = MibTableColumn
lineConfMode = _LineConfMode_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 7, 1, 2),
    _LineConfMode_Type()
)
lineConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lineConfMode.setStatus("current")
_LineConfRowStatus_Type = RowStatus
_LineConfRowStatus_Object = MibTableColumn
lineConfRowStatus = _LineConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 7, 1, 3),
    _LineConfRowStatus_Type()
)
lineConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    lineConfRowStatus.setStatus("current")
_BridgeConfTable_Object = MibTable
bridgeConfTable = _BridgeConfTable_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 8)
)
if mibBuilder.loadTexts:
    bridgeConfTable.setStatus("current")
_BridgeConfEntry_Object = MibTableRow
bridgeConfEntry = _BridgeConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 8, 1)
)
bridgeConfEntry.setIndexNames(
    (0, "MAIPU-IF-MIB", "bridgeConfIfIndex"),
)
if mibBuilder.loadTexts:
    bridgeConfEntry.setStatus("current")
_BridgeConfIfIndex_Type = Integer32
_BridgeConfIfIndex_Object = MibTableColumn
bridgeConfIfIndex = _BridgeConfIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 8, 1, 1),
    _BridgeConfIfIndex_Type()
)
bridgeConfIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    bridgeConfIfIndex.setStatus("current")


class _BridgeConfBriNo_Type(Integer32):
    """Custom type bridgeConfBriNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_BridgeConfBriNo_Type.__name__ = "Integer32"
_BridgeConfBriNo_Object = MibTableColumn
bridgeConfBriNo = _BridgeConfBriNo_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 8, 1, 2),
    _BridgeConfBriNo_Type()
)
bridgeConfBriNo.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    bridgeConfBriNo.setStatus("current")
_BridgeConfRowStatus_Type = RowStatus
_BridgeConfRowStatus_Object = MibTableColumn
bridgeConfRowStatus = _BridgeConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 5651, 3, 2, 8, 1, 3),
    _BridgeConfRowStatus_Type()
)
bridgeConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    bridgeConfRowStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MAIPU-IF-MIB",
    **{"mpIfMib": mpIfMib,
       "ethConfTable": ethConfTable,
       "ethConfEntry": ethConfEntry,
       "ethConfIfIndex": ethConfIfIndex,
       "ethMtu": ethMtu,
       "ethDescription": ethDescription,
       "ethUcastAddr": ethUcastAddr,
       "ethUcastMask": ethUcastMask,
       "ethUcastUnnumber": ethUcastUnnumber,
       "ethBcastAddr": ethBcastAddr,
       "ethMetric": ethMetric,
       "ethDuplex": ethDuplex,
       "ethRate": ethRate,
       "secondaryTable": secondaryTable,
       "secondaryEntry": secondaryEntry,
       "secondaryIfIndex": secondaryIfIndex,
       "secondaryIp": secondaryIp,
       "secondaryMask": secondaryMask,
       "secondaryStatus": secondaryStatus,
       "serialConfTable": serialConfTable,
       "serialConfEntry": serialConfEntry,
       "serialConfIndex": serialConfIndex,
       "serialMtu": serialMtu,
       "serialDescription": serialDescription,
       "serialUcastAddr": serialUcastAddr,
       "serialUcastMask": serialUcastMask,
       "serialUnnumber": serialUnnumber,
       "serialBcastAddr": serialBcastAddr,
       "serialMetric": serialMetric,
       "serialClockSpeed": serialClockSpeed,
       "serialClockLine": serialClockLine,
       "serialClockInvert": serialClockInvert,
       "serialNrziEncode": serialNrziEncode,
       "serialIdleMode": serialIdleMode,
       "serialSpeed": serialSpeed,
       "serialDataBits": serialDataBits,
       "serialStopBits": serialStopBits,
       "serialParity": serialParity,
       "serialFlowCtl": serialFlowCtl,
       "serialMru": serialMru,
       "serialStartCharacter": serialStartCharacter,
       "serialStopCharacter": serialStopCharacter,
       "serialEncapsulation": serialEncapsulation,
       "serialPhyLayer": serialPhyLayer,
       "serialIpTcpHeadCompress": serialIpTcpHeadCompress,
       "serialBackup": serialBackup,
       "serialBackupIf": serialBackupIf,
       "serialBackupAct": serialBackupAct,
       "serialBackupDeact": serialBackupDeact,
       "serialQos": serialQos,
       "serialQosList": serialQosList,
       "serialTxHigh": serialTxHigh,
       "serialTxMedium": serialTxMedium,
       "serialTxNormal": serialTxNormal,
       "serialTxLow": serialTxLow,
       "serialTbds": serialTbds,
       "terminalTable": terminalTable,
       "terminalEntry": terminalEntry,
       "termIndex": termIndex,
       "termStatus": termStatus,
       "termSpeed": termSpeed,
       "termDatabits": termDatabits,
       "termStopbits": termStopbits,
       "termParity": termParity,
       "termFlowCtrl": termFlowCtrl,
       "termLineOn": termLineOn,
       "termRxBuf": termRxBuf,
       "termTxBuf": termTxBuf,
       "termPrint": termPrint,
       "termAutoLink": termAutoLink,
       "termAutoLinkNo": termAutoLinkNo,
       "termRxDelay": termRxDelay,
       "termEscChar": termEscChar,
       "termLocalHost": termLocalHost,
       "termTxBytes": termTxBytes,
       "termRxBytes": termRxBytes,
       "termRowStatus": termRowStatus,
       "terminalHostTable": terminalHostTable,
       "terminalHostEntry": terminalHostEntry,
       "termHostIndex": termHostIndex,
       "termHostNo": termHostNo,
       "termHostName": termHostName,
       "termHostIp": termHostIp,
       "termHostPort": termHostPort,
       "termHostType": termHostType,
       "termHostTelnetType": termHostTelnetType,
       "termHostStauts": termHostStauts,
       "termHostFixtermType": termHostFixtermType,
       "termHostFixtermAuth": termHostFixtermAuth,
       "termHostFixtermChars": termHostFixtermChars,
       "termHostRloginUser": termHostRloginUser,
       "termHostRloginLocal": termHostRloginLocal,
       "termHostRloginRemote": termHostRloginRemote,
       "termHostRowStatus": termHostRowStatus,
       "lineConfTable": lineConfTable,
       "lineConfEntry": lineConfEntry,
       "lineConfNo": lineConfNo,
       "lineConfMode": lineConfMode,
       "lineConfRowStatus": lineConfRowStatus,
       "bridgeConfTable": bridgeConfTable,
       "bridgeConfEntry": bridgeConfEntry,
       "bridgeConfIfIndex": bridgeConfIfIndex,
       "bridgeConfBriNo": bridgeConfBriNo,
       "bridgeConfRowStatus": bridgeConfRowStatus}
)
