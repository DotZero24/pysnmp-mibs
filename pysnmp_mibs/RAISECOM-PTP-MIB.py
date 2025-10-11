# SNMP MIB module (RAISECOM-PTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/raisecom/RAISECOM-PTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:36:42 2025
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

(raisecomAgent,) = mibBuilder.importSymbols(
    "RAISECOM-BASE-MIB",
    "raisecomAgent")

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

(rcPortIndex,) = mibBuilder.importSymbols(
    "SWITCH-SYSTEM-MIB",
    "rcPortIndex")

(EnableVar,) = mibBuilder.importSymbols(
    "SWITCH-TC",
    "EnableVar")


# MODULE-IDENTITY

raisecomPtp = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26)
)
if mibBuilder.loadTexts:
    raisecomPtp.setRevisions(
        ("2010-10-29 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class PTPTimeStamp(TextualConvention, OctetString):
    status = "current"
    displayHint = "6d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10



class PTPTimeInterval(TextualConvention, OctetString):
    status = "current"
    displayHint = "8d.4d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(12, 12),
    )
    fixed_length = 12



class PTPClockIdentity(TextualConvention, OctetString):
    status = "current"
    displayHint = "1h:1h:1h:1h:1h:1h:1h:1h"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8



class PTPPortIdentity(TextualConvention, OctetString):
    status = "current"
    displayHint = "1h:1h:1h:1h:1h:1h:1h:1h.2d"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10



# MIB Managed Objects in the order of their OIDs

_RaisecomPtpGlobal_ObjectIdentity = ObjectIdentity
raisecomPtpGlobal = _RaisecomPtpGlobal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1)
)


class _RaisecomPtpEnable_Type(Integer32):
    """Custom type raisecomPtpEnable based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RaisecomPtpEnable_Type.__name__ = "Integer32"
_RaisecomPtpEnable_Object = MibScalar
raisecomPtpEnable = _RaisecomPtpEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 1),
    _RaisecomPtpEnable_Type()
)
raisecomPtpEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpEnable.setStatus("current")


class _RaisecomPtpClockMode_Type(Integer32):
    """Custom type raisecomPtpClockMode based on Integer32"""
    defaultValue = 1

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
        *(("ordinary", 1),
          ("boundary", 2),
          ("e2e-transparent", 3),
          ("p2p-transparent", 4))
    )


_RaisecomPtpClockMode_Type.__name__ = "Integer32"
_RaisecomPtpClockMode_Object = MibScalar
raisecomPtpClockMode = _RaisecomPtpClockMode_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 2),
    _RaisecomPtpClockMode_Type()
)
raisecomPtpClockMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpClockMode.setStatus("current")


class _RaisecomPtpClockUnicastFlag_Type(Integer32):
    """Custom type raisecomPtpClockUnicastFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("multicast", 0),
          ("unicast", 1))
    )


_RaisecomPtpClockUnicastFlag_Type.__name__ = "Integer32"
_RaisecomPtpClockUnicastFlag_Object = MibScalar
raisecomPtpClockUnicastFlag = _RaisecomPtpClockUnicastFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 3),
    _RaisecomPtpClockUnicastFlag_Type()
)
raisecomPtpClockUnicastFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpClockUnicastFlag.setStatus("current")


class _RaisecomPtpClockStepFlag_Type(Integer32):
    """Custom type raisecomPtpClockStepFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("onestep", 1),
          ("twostep", 2))
    )


_RaisecomPtpClockStepFlag_Type.__name__ = "Integer32"
_RaisecomPtpClockStepFlag_Object = MibScalar
raisecomPtpClockStepFlag = _RaisecomPtpClockStepFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 4),
    _RaisecomPtpClockStepFlag_Type()
)
raisecomPtpClockStepFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpClockStepFlag.setStatus("current")


class _RaisecomPtpClockStatisticClear_Type(Integer32):
    """Custom type raisecomPtpClockStatisticClear based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("clear", 1))
    )


_RaisecomPtpClockStatisticClear_Type.__name__ = "Integer32"
_RaisecomPtpClockStatisticClear_Object = MibScalar
raisecomPtpClockStatisticClear = _RaisecomPtpClockStatisticClear_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 5),
    _RaisecomPtpClockStatisticClear_Type()
)
raisecomPtpClockStatisticClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpClockStatisticClear.setStatus("current")
_RaisecomPtpGlobalPortTable_Object = MibTable
raisecomPtpGlobalPortTable = _RaisecomPtpGlobalPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 6)
)
if mibBuilder.loadTexts:
    raisecomPtpGlobalPortTable.setStatus("current")
_RaisecomPtpGlobalPortEntry_Object = MibTableRow
raisecomPtpGlobalPortEntry = _RaisecomPtpGlobalPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 6, 1)
)
raisecomPtpGlobalPortEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
)
if mibBuilder.loadTexts:
    raisecomPtpGlobalPortEntry.setStatus("current")


class _RaisecomPtpPortEnable_Type(Integer32):
    """Custom type raisecomPtpPortEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("disable", 0),
          ("enable", 1))
    )


_RaisecomPtpPortEnable_Type.__name__ = "Integer32"
_RaisecomPtpPortEnable_Object = MibTableColumn
raisecomPtpPortEnable = _RaisecomPtpPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 6, 1, 1),
    _RaisecomPtpPortEnable_Type()
)
raisecomPtpPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortEnable.setStatus("current")


class _RaisecomPtpPortTransmitProtocol_Type(Integer32):
    """Custom type raisecomPtpPortTransmitProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              3)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("ethernet", 3))
    )


_RaisecomPtpPortTransmitProtocol_Type.__name__ = "Integer32"
_RaisecomPtpPortTransmitProtocol_Object = MibTableColumn
raisecomPtpPortTransmitProtocol = _RaisecomPtpPortTransmitProtocol_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 6, 1, 2),
    _RaisecomPtpPortTransmitProtocol_Type()
)
raisecomPtpPortTransmitProtocol.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortTransmitProtocol.setStatus("current")


class _RaisecomPtpPortVlan_Type(Integer32):
    """Custom type raisecomPtpPortVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_RaisecomPtpPortVlan_Type.__name__ = "Integer32"
_RaisecomPtpPortVlan_Object = MibTableColumn
raisecomPtpPortVlan = _RaisecomPtpPortVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 6, 1, 3),
    _RaisecomPtpPortVlan_Type()
)
raisecomPtpPortVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortVlan.setStatus("current")
_RaisecomPtpPortAsymmetryDelay_Type = Integer32
_RaisecomPtpPortAsymmetryDelay_Object = MibTableColumn
raisecomPtpPortAsymmetryDelay = _RaisecomPtpPortAsymmetryDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 1, 6, 1, 4),
    _RaisecomPtpPortAsymmetryDelay_Type()
)
raisecomPtpPortAsymmetryDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortAsymmetryDelay.setStatus("current")
if mibBuilder.loadTexts:
    raisecomPtpPortAsymmetryDelay.setUnits("nanseconds")
_RaisecomPtpClock_ObjectIdentity = ObjectIdentity
raisecomPtpClock = _RaisecomPtpClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 2)
)
_RaisecomPtpClockIdentity_Type = PTPClockIdentity
_RaisecomPtpClockIdentity_Object = MibScalar
raisecomPtpClockIdentity = _RaisecomPtpClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 2, 1),
    _RaisecomPtpClockIdentity_Type()
)
raisecomPtpClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpClockIdentity.setStatus("current")


class _RaisecomPtpClockDomain_Type(Integer32):
    """Custom type raisecomPtpClockDomain based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpClockDomain_Type.__name__ = "Integer32"
_RaisecomPtpClockDomain_Object = MibScalar
raisecomPtpClockDomain = _RaisecomPtpClockDomain_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 2, 2),
    _RaisecomPtpClockDomain_Type()
)
raisecomPtpClockDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpClockDomain.setStatus("current")


class _RaisecomPtpClockPriority1_Type(Integer32):
    """Custom type raisecomPtpClockPriority1 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpClockPriority1_Type.__name__ = "Integer32"
_RaisecomPtpClockPriority1_Object = MibScalar
raisecomPtpClockPriority1 = _RaisecomPtpClockPriority1_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 2, 3),
    _RaisecomPtpClockPriority1_Type()
)
raisecomPtpClockPriority1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpClockPriority1.setStatus("current")


class _RaisecomPtpClockPriority2_Type(Integer32):
    """Custom type raisecomPtpClockPriority2 based on Integer32"""
    defaultValue = 128

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpClockPriority2_Type.__name__ = "Integer32"
_RaisecomPtpClockPriority2_Object = MibScalar
raisecomPtpClockPriority2 = _RaisecomPtpClockPriority2_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 2, 4),
    _RaisecomPtpClockPriority2_Type()
)
raisecomPtpClockPriority2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpClockPriority2.setStatus("current")


class _RaisecomPtpClockClass_Type(Integer32):
    """Custom type raisecomPtpClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpClockClass_Type.__name__ = "Integer32"
_RaisecomPtpClockClass_Object = MibScalar
raisecomPtpClockClass = _RaisecomPtpClockClass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 2, 5),
    _RaisecomPtpClockClass_Type()
)
raisecomPtpClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpClockClass.setStatus("current")


class _RaisecomPtpClockAccuracy_Type(Integer32):
    """Custom type raisecomPtpClockAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpClockAccuracy_Type.__name__ = "Integer32"
_RaisecomPtpClockAccuracy_Object = MibScalar
raisecomPtpClockAccuracy = _RaisecomPtpClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 2, 6),
    _RaisecomPtpClockAccuracy_Type()
)
raisecomPtpClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpClockAccuracy.setStatus("current")


class _RaisecomPtpClockOffsetScaledLogVariance_Type(Integer32):
    """Custom type raisecomPtpClockOffsetScaledLogVariance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomPtpClockOffsetScaledLogVariance_Type.__name__ = "Integer32"
_RaisecomPtpClockOffsetScaledLogVariance_Object = MibScalar
raisecomPtpClockOffsetScaledLogVariance = _RaisecomPtpClockOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 2, 7),
    _RaisecomPtpClockOffsetScaledLogVariance_Type()
)
raisecomPtpClockOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpClockOffsetScaledLogVariance.setStatus("current")


class _RaisecomPtpClockNumberPorts_Type(Integer32):
    """Custom type raisecomPtpClockNumberPorts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomPtpClockNumberPorts_Type.__name__ = "Integer32"
_RaisecomPtpClockNumberPorts_Object = MibScalar
raisecomPtpClockNumberPorts = _RaisecomPtpClockNumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 2, 8),
    _RaisecomPtpClockNumberPorts_Type()
)
raisecomPtpClockNumberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpClockNumberPorts.setStatus("current")


class _RaisecomPtpClockSlaveOnly_Type(Integer32):
    """Custom type raisecomPtpClockSlaveOnly based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("non-slave-only", 0),
          ("slave-only", 1))
    )


_RaisecomPtpClockSlaveOnly_Type.__name__ = "Integer32"
_RaisecomPtpClockSlaveOnly_Object = MibScalar
raisecomPtpClockSlaveOnly = _RaisecomPtpClockSlaveOnly_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 2, 9),
    _RaisecomPtpClockSlaveOnly_Type()
)
raisecomPtpClockSlaveOnly.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpClockSlaveOnly.setStatus("current")
_RaisecomPtpCurrent_ObjectIdentity = ObjectIdentity
raisecomPtpCurrent = _RaisecomPtpCurrent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 3)
)
_RaisecomPtpCurrentEndMeanPathDelay_Type = PTPTimeInterval
_RaisecomPtpCurrentEndMeanPathDelay_Object = MibScalar
raisecomPtpCurrentEndMeanPathDelay = _RaisecomPtpCurrentEndMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 3, 1),
    _RaisecomPtpCurrentEndMeanPathDelay_Type()
)
raisecomPtpCurrentEndMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpCurrentEndMeanPathDelay.setStatus("current")
_RaisecomPtpCurrentOffsetFromParent_Type = PTPTimeInterval
_RaisecomPtpCurrentOffsetFromParent_Object = MibScalar
raisecomPtpCurrentOffsetFromParent = _RaisecomPtpCurrentOffsetFromParent_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 3, 2),
    _RaisecomPtpCurrentOffsetFromParent_Type()
)
raisecomPtpCurrentOffsetFromParent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpCurrentOffsetFromParent.setStatus("current")


class _RaisecomPtpCurrentStepsRemoved_Type(Integer32):
    """Custom type raisecomPtpCurrentStepsRemoved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_RaisecomPtpCurrentStepsRemoved_Type.__name__ = "Integer32"
_RaisecomPtpCurrentStepsRemoved_Object = MibScalar
raisecomPtpCurrentStepsRemoved = _RaisecomPtpCurrentStepsRemoved_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 3, 3),
    _RaisecomPtpCurrentStepsRemoved_Type()
)
raisecomPtpCurrentStepsRemoved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpCurrentStepsRemoved.setStatus("current")
_RaisecomPtpParent_ObjectIdentity = ObjectIdentity
raisecomPtpParent = _RaisecomPtpParent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4)
)
_RaisecomPtpParentPortIdentity_Type = PTPPortIdentity
_RaisecomPtpParentPortIdentity_Object = MibScalar
raisecomPtpParentPortIdentity = _RaisecomPtpParentPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4, 1),
    _RaisecomPtpParentPortIdentity_Type()
)
raisecomPtpParentPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpParentPortIdentity.setStatus("current")


class _RaisecomPtpParentSatisticsFlag_Type(Integer32):
    """Custom type raisecomPtpParentSatisticsFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("nosatistics", 0),
          ("satistics", 1))
    )


_RaisecomPtpParentSatisticsFlag_Type.__name__ = "Integer32"
_RaisecomPtpParentSatisticsFlag_Object = MibScalar
raisecomPtpParentSatisticsFlag = _RaisecomPtpParentSatisticsFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4, 2),
    _RaisecomPtpParentSatisticsFlag_Type()
)
raisecomPtpParentSatisticsFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpParentSatisticsFlag.setStatus("current")


class _RaisecomPtpParentOffsetScaledLogVariance_Type(Integer32):
    """Custom type raisecomPtpParentOffsetScaledLogVariance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomPtpParentOffsetScaledLogVariance_Type.__name__ = "Integer32"
_RaisecomPtpParentOffsetScaledLogVariance_Object = MibScalar
raisecomPtpParentOffsetScaledLogVariance = _RaisecomPtpParentOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4, 3),
    _RaisecomPtpParentOffsetScaledLogVariance_Type()
)
raisecomPtpParentOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpParentOffsetScaledLogVariance.setStatus("current")
_RaisecomPtpParentPhaseChangeRate_Type = Integer32
_RaisecomPtpParentPhaseChangeRate_Object = MibScalar
raisecomPtpParentPhaseChangeRate = _RaisecomPtpParentPhaseChangeRate_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4, 4),
    _RaisecomPtpParentPhaseChangeRate_Type()
)
raisecomPtpParentPhaseChangeRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpParentPhaseChangeRate.setStatus("current")
_RaisecomPtpGrandmasterIdentity_Type = PTPClockIdentity
_RaisecomPtpGrandmasterIdentity_Object = MibScalar
raisecomPtpGrandmasterIdentity = _RaisecomPtpGrandmasterIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4, 5),
    _RaisecomPtpGrandmasterIdentity_Type()
)
raisecomPtpGrandmasterIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpGrandmasterIdentity.setStatus("current")


class _RaisecomPtpGrandmasterPriority1_Type(Integer32):
    """Custom type raisecomPtpGrandmasterPriority1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpGrandmasterPriority1_Type.__name__ = "Integer32"
_RaisecomPtpGrandmasterPriority1_Object = MibScalar
raisecomPtpGrandmasterPriority1 = _RaisecomPtpGrandmasterPriority1_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4, 6),
    _RaisecomPtpGrandmasterPriority1_Type()
)
raisecomPtpGrandmasterPriority1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpGrandmasterPriority1.setStatus("current")


class _RaisecomPtpGrandmasterPriority2_Type(Integer32):
    """Custom type raisecomPtpGrandmasterPriority2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpGrandmasterPriority2_Type.__name__ = "Integer32"
_RaisecomPtpGrandmasterPriority2_Object = MibScalar
raisecomPtpGrandmasterPriority2 = _RaisecomPtpGrandmasterPriority2_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4, 7),
    _RaisecomPtpGrandmasterPriority2_Type()
)
raisecomPtpGrandmasterPriority2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpGrandmasterPriority2.setStatus("current")


class _RaisecomPtpGrandmasterClockClass_Type(Integer32):
    """Custom type raisecomPtpGrandmasterClockClass based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpGrandmasterClockClass_Type.__name__ = "Integer32"
_RaisecomPtpGrandmasterClockClass_Object = MibScalar
raisecomPtpGrandmasterClockClass = _RaisecomPtpGrandmasterClockClass_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4, 8),
    _RaisecomPtpGrandmasterClockClass_Type()
)
raisecomPtpGrandmasterClockClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpGrandmasterClockClass.setStatus("current")


class _RaisecomPtpGrandmasterClockAccuracy_Type(Integer32):
    """Custom type raisecomPtpGrandmasterClockAccuracy based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpGrandmasterClockAccuracy_Type.__name__ = "Integer32"
_RaisecomPtpGrandmasterClockAccuracy_Object = MibScalar
raisecomPtpGrandmasterClockAccuracy = _RaisecomPtpGrandmasterClockAccuracy_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4, 9),
    _RaisecomPtpGrandmasterClockAccuracy_Type()
)
raisecomPtpGrandmasterClockAccuracy.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpGrandmasterClockAccuracy.setStatus("current")


class _RaisecomPtpGrandmasterOffsetScaledLogVariance_Type(Integer32):
    """Custom type raisecomPtpGrandmasterOffsetScaledLogVariance based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomPtpGrandmasterOffsetScaledLogVariance_Type.__name__ = "Integer32"
_RaisecomPtpGrandmasterOffsetScaledLogVariance_Object = MibScalar
raisecomPtpGrandmasterOffsetScaledLogVariance = _RaisecomPtpGrandmasterOffsetScaledLogVariance_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 4, 10),
    _RaisecomPtpGrandmasterOffsetScaledLogVariance_Type()
)
raisecomPtpGrandmasterOffsetScaledLogVariance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpGrandmasterOffsetScaledLogVariance.setStatus("current")
_RaisecomPtpTimeProperty_ObjectIdentity = ObjectIdentity
raisecomPtpTimeProperty = _RaisecomPtpTimeProperty_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 5)
)


class _RaisecomPtpTimeProCurrentUtcOffset_Type(Integer32):
    """Custom type raisecomPtpTimeProCurrentUtcOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomPtpTimeProCurrentUtcOffset_Type.__name__ = "Integer32"
_RaisecomPtpTimeProCurrentUtcOffset_Object = MibScalar
raisecomPtpTimeProCurrentUtcOffset = _RaisecomPtpTimeProCurrentUtcOffset_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 5, 1),
    _RaisecomPtpTimeProCurrentUtcOffset_Type()
)
raisecomPtpTimeProCurrentUtcOffset.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTimeProCurrentUtcOffset.setStatus("current")
if mibBuilder.loadTexts:
    raisecomPtpTimeProCurrentUtcOffset.setUnits("seconds")


class _RaisecomPtpTimeProCurrentUtcOffsetValid_Type(Integer32):
    """Custom type raisecomPtpTimeProCurrentUtcOffsetValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("novalid", 0),
          ("valid", 1))
    )


_RaisecomPtpTimeProCurrentUtcOffsetValid_Type.__name__ = "Integer32"
_RaisecomPtpTimeProCurrentUtcOffsetValid_Object = MibScalar
raisecomPtpTimeProCurrentUtcOffsetValid = _RaisecomPtpTimeProCurrentUtcOffsetValid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 5, 2),
    _RaisecomPtpTimeProCurrentUtcOffsetValid_Type()
)
raisecomPtpTimeProCurrentUtcOffsetValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTimeProCurrentUtcOffsetValid.setStatus("current")


class _RaisecomPtpTimeProLeap_Type(Integer32):
    """Custom type raisecomPtpTimeProLeap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noleap", 0),
          ("leap61", 1),
          ("leap59", 2))
    )


_RaisecomPtpTimeProLeap_Type.__name__ = "Integer32"
_RaisecomPtpTimeProLeap_Object = MibScalar
raisecomPtpTimeProLeap = _RaisecomPtpTimeProLeap_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 5, 3),
    _RaisecomPtpTimeProLeap_Type()
)
raisecomPtpTimeProLeap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTimeProLeap.setStatus("current")


class _RaisecomPtpTimeProTimeFrequencyTraceable_Type(Integer32):
    """Custom type raisecomPtpTimeProTimeFrequencyTraceable based on Integer32"""
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
        *(("none", 0),
          ("time", 1),
          ("frequency", 2),
          ("both", 3))
    )


_RaisecomPtpTimeProTimeFrequencyTraceable_Type.__name__ = "Integer32"
_RaisecomPtpTimeProTimeFrequencyTraceable_Object = MibScalar
raisecomPtpTimeProTimeFrequencyTraceable = _RaisecomPtpTimeProTimeFrequencyTraceable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 5, 4),
    _RaisecomPtpTimeProTimeFrequencyTraceable_Type()
)
raisecomPtpTimeProTimeFrequencyTraceable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTimeProTimeFrequencyTraceable.setStatus("current")


class _RaisecomPtpTimeProMatchTimescale_Type(Integer32):
    """Custom type raisecomPtpTimeProMatchTimescale based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("noptptime", 0),
          ("ptptime", 1))
    )


_RaisecomPtpTimeProMatchTimescale_Type.__name__ = "Integer32"
_RaisecomPtpTimeProMatchTimescale_Object = MibScalar
raisecomPtpTimeProMatchTimescale = _RaisecomPtpTimeProMatchTimescale_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 5, 5),
    _RaisecomPtpTimeProMatchTimescale_Type()
)
raisecomPtpTimeProMatchTimescale.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTimeProMatchTimescale.setStatus("current")


class _RaisecomPtpTimeProTimeSource_Type(Integer32):
    """Custom type raisecomPtpTimeProTimeSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpTimeProTimeSource_Type.__name__ = "Integer32"
_RaisecomPtpTimeProTimeSource_Object = MibScalar
raisecomPtpTimeProTimeSource = _RaisecomPtpTimeProTimeSource_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 5, 6),
    _RaisecomPtpTimeProTimeSource_Type()
)
raisecomPtpTimeProTimeSource.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpTimeProTimeSource.setStatus("current")


class _RaisecomPtpTimeProTimeSourceOper_Type(Integer32):
    """Custom type raisecomPtpTimeProTimeSourceOper based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_RaisecomPtpTimeProTimeSourceOper_Type.__name__ = "Integer32"
_RaisecomPtpTimeProTimeSourceOper_Object = MibScalar
raisecomPtpTimeProTimeSourceOper = _RaisecomPtpTimeProTimeSourceOper_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 5, 7),
    _RaisecomPtpTimeProTimeSourceOper_Type()
)
raisecomPtpTimeProTimeSourceOper.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTimeProTimeSourceOper.setStatus("current")
_RaisecomPtpPorts_ObjectIdentity = ObjectIdentity
raisecomPtpPorts = _RaisecomPtpPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6)
)
_RaisecomPtpPortTable_Object = MibTable
raisecomPtpPortTable = _RaisecomPtpPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1)
)
if mibBuilder.loadTexts:
    raisecomPtpPortTable.setStatus("current")
_RaisecomPtpPortEntry_Object = MibTableRow
raisecomPtpPortEntry = _RaisecomPtpPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1)
)
raisecomPtpPortEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
)
if mibBuilder.loadTexts:
    raisecomPtpPortEntry.setStatus("current")
_RaisecomPtpPortIdentity_Type = OctetString
_RaisecomPtpPortIdentity_Object = MibTableColumn
raisecomPtpPortIdentity = _RaisecomPtpPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 1),
    _RaisecomPtpPortIdentity_Type()
)
raisecomPtpPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpPortIdentity.setStatus("current")


class _RaisecomPtpPortState_Type(Integer32):
    """Custom type raisecomPtpPortState based on Integer32"""
    defaultValue = 0

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
              8,
              9)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("initializing", 1),
          ("faulty", 2),
          ("disabled", 3),
          ("listening", 4),
          ("premaster", 5),
          ("master", 6),
          ("passive", 7),
          ("uncalibrated", 8),
          ("slave", 9))
    )


_RaisecomPtpPortState_Type.__name__ = "Integer32"
_RaisecomPtpPortState_Object = MibTableColumn
raisecomPtpPortState = _RaisecomPtpPortState_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 2),
    _RaisecomPtpPortState_Type()
)
raisecomPtpPortState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpPortState.setStatus("current")


class _RaisecomPtpPortStateForce_Type(Integer32):
    """Custom type raisecomPtpPortStateForce based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              6,
              7,
              9)
        )
    )
    namedValues = NamedValues(
        *(("noforce", 0),
          ("master", 6),
          ("passive", 7),
          ("slave", 9))
    )


_RaisecomPtpPortStateForce_Type.__name__ = "Integer32"
_RaisecomPtpPortStateForce_Object = MibTableColumn
raisecomPtpPortStateForce = _RaisecomPtpPortStateForce_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 3),
    _RaisecomPtpPortStateForce_Type()
)
raisecomPtpPortStateForce.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortStateForce.setStatus("current")


class _RaisecomPtpPortDelayMechanism_Type(Integer32):
    """Custom type raisecomPtpPortDelayMechanism based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end-to-end", 1),
          ("peer-to-peer", 2))
    )


_RaisecomPtpPortDelayMechanism_Type.__name__ = "Integer32"
_RaisecomPtpPortDelayMechanism_Object = MibTableColumn
raisecomPtpPortDelayMechanism = _RaisecomPtpPortDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 4),
    _RaisecomPtpPortDelayMechanism_Type()
)
raisecomPtpPortDelayMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortDelayMechanism.setStatus("current")
_RaisecomPtpPortPeerMeanPathDelay_Type = PTPTimeInterval
_RaisecomPtpPortPeerMeanPathDelay_Object = MibTableColumn
raisecomPtpPortPeerMeanPathDelay = _RaisecomPtpPortPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 5),
    _RaisecomPtpPortPeerMeanPathDelay_Type()
)
raisecomPtpPortPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpPortPeerMeanPathDelay.setStatus("current")


class _RaisecomPtpPortLogSyncInterval_Type(Integer32):
    """Custom type raisecomPtpPortLogSyncInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, -1),
    )


_RaisecomPtpPortLogSyncInterval_Type.__name__ = "Integer32"
_RaisecomPtpPortLogSyncInterval_Object = MibTableColumn
raisecomPtpPortLogSyncInterval = _RaisecomPtpPortLogSyncInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 6),
    _RaisecomPtpPortLogSyncInterval_Type()
)
raisecomPtpPortLogSyncInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortLogSyncInterval.setStatus("current")


class _RaisecomPtpPortLogAnnounceInterval_Type(Integer32):
    """Custom type raisecomPtpPortLogAnnounceInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 4),
    )


_RaisecomPtpPortLogAnnounceInterval_Type.__name__ = "Integer32"
_RaisecomPtpPortLogAnnounceInterval_Object = MibTableColumn
raisecomPtpPortLogAnnounceInterval = _RaisecomPtpPortLogAnnounceInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 7),
    _RaisecomPtpPortLogAnnounceInterval_Type()
)
raisecomPtpPortLogAnnounceInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortLogAnnounceInterval.setStatus("current")


class _RaisecomPtpPortLogMinDelayRequestInterval_Type(Integer32):
    """Custom type raisecomPtpPortLogMinDelayRequestInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, -1),
    )


_RaisecomPtpPortLogMinDelayRequestInterval_Type.__name__ = "Integer32"
_RaisecomPtpPortLogMinDelayRequestInterval_Object = MibTableColumn
raisecomPtpPortLogMinDelayRequestInterval = _RaisecomPtpPortLogMinDelayRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 8),
    _RaisecomPtpPortLogMinDelayRequestInterval_Type()
)
raisecomPtpPortLogMinDelayRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortLogMinDelayRequestInterval.setStatus("current")


class _RaisecomPtpPortAnnounceReceiptTimeout_Type(Integer32):
    """Custom type raisecomPtpPortAnnounceReceiptTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(3, 16),
    )


_RaisecomPtpPortAnnounceReceiptTimeout_Type.__name__ = "Integer32"
_RaisecomPtpPortAnnounceReceiptTimeout_Object = MibTableColumn
raisecomPtpPortAnnounceReceiptTimeout = _RaisecomPtpPortAnnounceReceiptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 9),
    _RaisecomPtpPortAnnounceReceiptTimeout_Type()
)
raisecomPtpPortAnnounceReceiptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortAnnounceReceiptTimeout.setStatus("current")


class _RaisecomPtpPortLogMinPDelayRequestInterval_Type(Integer32):
    """Custom type raisecomPtpPortLogMinPDelayRequestInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, -1),
    )


_RaisecomPtpPortLogMinPDelayRequestInterval_Type.__name__ = "Integer32"
_RaisecomPtpPortLogMinPDelayRequestInterval_Object = MibTableColumn
raisecomPtpPortLogMinPDelayRequestInterval = _RaisecomPtpPortLogMinPDelayRequestInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 10),
    _RaisecomPtpPortLogMinPDelayRequestInterval_Type()
)
raisecomPtpPortLogMinPDelayRequestInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpPortLogMinPDelayRequestInterval.setStatus("current")


class _RaisecomPtpPortVersionNumber_Type(Integer32):
    """Custom type raisecomPtpPortVersionNumber based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_RaisecomPtpPortVersionNumber_Type.__name__ = "Integer32"
_RaisecomPtpPortVersionNumber_Object = MibTableColumn
raisecomPtpPortVersionNumber = _RaisecomPtpPortVersionNumber_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 11),
    _RaisecomPtpPortVersionNumber_Type()
)
raisecomPtpPortVersionNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpPortVersionNumber.setStatus("current")
_RaisecomPtpPortUnicastMasterMaxIndex_Type = Integer32
_RaisecomPtpPortUnicastMasterMaxIndex_Object = MibTableColumn
raisecomPtpPortUnicastMasterMaxIndex = _RaisecomPtpPortUnicastMasterMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 12),
    _RaisecomPtpPortUnicastMasterMaxIndex_Type()
)
raisecomPtpPortUnicastMasterMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpPortUnicastMasterMaxIndex.setStatus("current")
_RaisecomPtpPortUnicastPeerMaxIndex_Type = Integer32
_RaisecomPtpPortUnicastPeerMaxIndex_Object = MibTableColumn
raisecomPtpPortUnicastPeerMaxIndex = _RaisecomPtpPortUnicastPeerMaxIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 6, 1, 1, 13),
    _RaisecomPtpPortUnicastPeerMaxIndex_Type()
)
raisecomPtpPortUnicastPeerMaxIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpPortUnicastPeerMaxIndex.setStatus("current")
_RaisecomPtpForeignRecords_ObjectIdentity = ObjectIdentity
raisecomPtpForeignRecords = _RaisecomPtpForeignRecords_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 7)
)
_RaisecomPtpForeignRecordTable_Object = MibTable
raisecomPtpForeignRecordTable = _RaisecomPtpForeignRecordTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 7, 1)
)
if mibBuilder.loadTexts:
    raisecomPtpForeignRecordTable.setStatus("current")
_RaisecomPtpForeignRecordEntry_Object = MibTableRow
raisecomPtpForeignRecordEntry = _RaisecomPtpForeignRecordEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 7, 1, 1)
)
raisecomPtpForeignRecordEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
    (0, "RAISECOM-PTP-MIB", "raisecomPtpForeignRecordIndex"),
)
if mibBuilder.loadTexts:
    raisecomPtpForeignRecordEntry.setStatus("current")


class _RaisecomPtpForeignRecordIndex_Type(Integer32):
    """Custom type raisecomPtpForeignRecordIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_RaisecomPtpForeignRecordIndex_Type.__name__ = "Integer32"
_RaisecomPtpForeignRecordIndex_Object = MibTableColumn
raisecomPtpForeignRecordIndex = _RaisecomPtpForeignRecordIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 7, 1, 1, 1),
    _RaisecomPtpForeignRecordIndex_Type()
)
raisecomPtpForeignRecordIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomPtpForeignRecordIndex.setStatus("current")


class _RaisecomPtpForeignRecordValid_Type(Integer32):
    """Custom type raisecomPtpForeignRecordValid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("novalid", 0),
          ("valid", 1))
    )


_RaisecomPtpForeignRecordValid_Type.__name__ = "Integer32"
_RaisecomPtpForeignRecordValid_Object = MibTableColumn
raisecomPtpForeignRecordValid = _RaisecomPtpForeignRecordValid_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 7, 1, 1, 2),
    _RaisecomPtpForeignRecordValid_Type()
)
raisecomPtpForeignRecordValid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpForeignRecordValid.setStatus("current")
_RaisecomPtpForeignRecordPortIdentity_Type = PTPPortIdentity
_RaisecomPtpForeignRecordPortIdentity_Object = MibTableColumn
raisecomPtpForeignRecordPortIdentity = _RaisecomPtpForeignRecordPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 7, 1, 1, 3),
    _RaisecomPtpForeignRecordPortIdentity_Type()
)
raisecomPtpForeignRecordPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpForeignRecordPortIdentity.setStatus("current")
_RaisecomPtpForeignRecordAnnounceNum_Type = Integer32
_RaisecomPtpForeignRecordAnnounceNum_Object = MibTableColumn
raisecomPtpForeignRecordAnnounceNum = _RaisecomPtpForeignRecordAnnounceNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 7, 1, 1, 4),
    _RaisecomPtpForeignRecordAnnounceNum_Type()
)
raisecomPtpForeignRecordAnnounceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpForeignRecordAnnounceNum.setStatus("current")
_RaisecomPtpMessageStat_ObjectIdentity = ObjectIdentity
raisecomPtpMessageStat = _RaisecomPtpMessageStat_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8)
)
_RaisecomPtpMessageStatTable_Object = MibTable
raisecomPtpMessageStatTable = _RaisecomPtpMessageStatTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1)
)
if mibBuilder.loadTexts:
    raisecomPtpMessageStatTable.setStatus("current")
_RaisecomPtpMessageStatEntry_Object = MibTableRow
raisecomPtpMessageStatEntry = _RaisecomPtpMessageStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1)
)
raisecomPtpMessageStatEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
)
if mibBuilder.loadTexts:
    raisecomPtpMessageStatEntry.setStatus("current")
_RaisecomPtpMsgStatSendSync_Type = Integer32
_RaisecomPtpMsgStatSendSync_Object = MibTableColumn
raisecomPtpMsgStatSendSync = _RaisecomPtpMsgStatSendSync_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 1),
    _RaisecomPtpMsgStatSendSync_Type()
)
raisecomPtpMsgStatSendSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendSync.setStatus("current")
_RaisecomPtpMsgStatReceiveSync_Type = Integer32
_RaisecomPtpMsgStatReceiveSync_Object = MibTableColumn
raisecomPtpMsgStatReceiveSync = _RaisecomPtpMsgStatReceiveSync_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 2),
    _RaisecomPtpMsgStatReceiveSync_Type()
)
raisecomPtpMsgStatReceiveSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceiveSync.setStatus("current")
_RaisecomPtpMsgStatSendAnnounce_Type = Integer32
_RaisecomPtpMsgStatSendAnnounce_Object = MibTableColumn
raisecomPtpMsgStatSendAnnounce = _RaisecomPtpMsgStatSendAnnounce_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 3),
    _RaisecomPtpMsgStatSendAnnounce_Type()
)
raisecomPtpMsgStatSendAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendAnnounce.setStatus("current")
_RaisecomPtpMsgStatReceiveAnnounce_Type = Integer32
_RaisecomPtpMsgStatReceiveAnnounce_Object = MibTableColumn
raisecomPtpMsgStatReceiveAnnounce = _RaisecomPtpMsgStatReceiveAnnounce_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 4),
    _RaisecomPtpMsgStatReceiveAnnounce_Type()
)
raisecomPtpMsgStatReceiveAnnounce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceiveAnnounce.setStatus("current")
_RaisecomPtpMsgStatSendFollowUp_Type = Integer32
_RaisecomPtpMsgStatSendFollowUp_Object = MibTableColumn
raisecomPtpMsgStatSendFollowUp = _RaisecomPtpMsgStatSendFollowUp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 5),
    _RaisecomPtpMsgStatSendFollowUp_Type()
)
raisecomPtpMsgStatSendFollowUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendFollowUp.setStatus("current")
_RaisecomPtpMsgStatReceiveFollowUp_Type = Integer32
_RaisecomPtpMsgStatReceiveFollowUp_Object = MibTableColumn
raisecomPtpMsgStatReceiveFollowUp = _RaisecomPtpMsgStatReceiveFollowUp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 6),
    _RaisecomPtpMsgStatReceiveFollowUp_Type()
)
raisecomPtpMsgStatReceiveFollowUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceiveFollowUp.setStatus("current")
_RaisecomPtpMsgStatSendDelayReq_Type = Integer32
_RaisecomPtpMsgStatSendDelayReq_Object = MibTableColumn
raisecomPtpMsgStatSendDelayReq = _RaisecomPtpMsgStatSendDelayReq_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 7),
    _RaisecomPtpMsgStatSendDelayReq_Type()
)
raisecomPtpMsgStatSendDelayReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendDelayReq.setStatus("current")
_RaisecomPtpMsgStatReceiveDelayReq_Type = Integer32
_RaisecomPtpMsgStatReceiveDelayReq_Object = MibTableColumn
raisecomPtpMsgStatReceiveDelayReq = _RaisecomPtpMsgStatReceiveDelayReq_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 8),
    _RaisecomPtpMsgStatReceiveDelayReq_Type()
)
raisecomPtpMsgStatReceiveDelayReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceiveDelayReq.setStatus("current")
_RaisecomPtpMsgStatSendDelayResp_Type = Integer32
_RaisecomPtpMsgStatSendDelayResp_Object = MibTableColumn
raisecomPtpMsgStatSendDelayResp = _RaisecomPtpMsgStatSendDelayResp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 9),
    _RaisecomPtpMsgStatSendDelayResp_Type()
)
raisecomPtpMsgStatSendDelayResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendDelayResp.setStatus("current")
_RaisecomPtpMsgStatReceiveDelayResp_Type = Integer32
_RaisecomPtpMsgStatReceiveDelayResp_Object = MibTableColumn
raisecomPtpMsgStatReceiveDelayResp = _RaisecomPtpMsgStatReceiveDelayResp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 10),
    _RaisecomPtpMsgStatReceiveDelayResp_Type()
)
raisecomPtpMsgStatReceiveDelayResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceiveDelayResp.setStatus("current")
_RaisecomPtpMsgStatSendPdelayReq_Type = Integer32
_RaisecomPtpMsgStatSendPdelayReq_Object = MibTableColumn
raisecomPtpMsgStatSendPdelayReq = _RaisecomPtpMsgStatSendPdelayReq_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 11),
    _RaisecomPtpMsgStatSendPdelayReq_Type()
)
raisecomPtpMsgStatSendPdelayReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendPdelayReq.setStatus("current")
_RaisecomPtpMsgStatReceivePdelayReq_Type = Integer32
_RaisecomPtpMsgStatReceivePdelayReq_Object = MibTableColumn
raisecomPtpMsgStatReceivePdelayReq = _RaisecomPtpMsgStatReceivePdelayReq_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 12),
    _RaisecomPtpMsgStatReceivePdelayReq_Type()
)
raisecomPtpMsgStatReceivePdelayReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceivePdelayReq.setStatus("current")
_RaisecomPtpMsgStatSendPdelayResp_Type = Integer32
_RaisecomPtpMsgStatSendPdelayResp_Object = MibTableColumn
raisecomPtpMsgStatSendPdelayResp = _RaisecomPtpMsgStatSendPdelayResp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 13),
    _RaisecomPtpMsgStatSendPdelayResp_Type()
)
raisecomPtpMsgStatSendPdelayResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendPdelayResp.setStatus("current")
_RaisecomPtpMsgStatReceivePdelayResp_Type = Integer32
_RaisecomPtpMsgStatReceivePdelayResp_Object = MibTableColumn
raisecomPtpMsgStatReceivePdelayResp = _RaisecomPtpMsgStatReceivePdelayResp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 14),
    _RaisecomPtpMsgStatReceivePdelayResp_Type()
)
raisecomPtpMsgStatReceivePdelayResp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceivePdelayResp.setStatus("current")
_RaisecomPtpMsgStatSendPdelayRespFUp_Type = Integer32
_RaisecomPtpMsgStatSendPdelayRespFUp_Object = MibTableColumn
raisecomPtpMsgStatSendPdelayRespFUp = _RaisecomPtpMsgStatSendPdelayRespFUp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 15),
    _RaisecomPtpMsgStatSendPdelayRespFUp_Type()
)
raisecomPtpMsgStatSendPdelayRespFUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendPdelayRespFUp.setStatus("current")
_RaisecomPtpMsgStatReceivePdelayRespFUp_Type = Integer32
_RaisecomPtpMsgStatReceivePdelayRespFUp_Object = MibTableColumn
raisecomPtpMsgStatReceivePdelayRespFUp = _RaisecomPtpMsgStatReceivePdelayRespFUp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 16),
    _RaisecomPtpMsgStatReceivePdelayRespFUp_Type()
)
raisecomPtpMsgStatReceivePdelayRespFUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceivePdelayRespFUp.setStatus("current")
_RaisecomPtpMsgStatSendSignaling_Type = Integer32
_RaisecomPtpMsgStatSendSignaling_Object = MibTableColumn
raisecomPtpMsgStatSendSignaling = _RaisecomPtpMsgStatSendSignaling_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 17),
    _RaisecomPtpMsgStatSendSignaling_Type()
)
raisecomPtpMsgStatSendSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendSignaling.setStatus("current")
_RaisecomPtpMsgStatReceiveSignaling_Type = Integer32
_RaisecomPtpMsgStatReceiveSignaling_Object = MibTableColumn
raisecomPtpMsgStatReceiveSignaling = _RaisecomPtpMsgStatReceiveSignaling_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 18),
    _RaisecomPtpMsgStatReceiveSignaling_Type()
)
raisecomPtpMsgStatReceiveSignaling.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceiveSignaling.setStatus("current")
_RaisecomPtpMsgStatSendManagement_Type = Integer32
_RaisecomPtpMsgStatSendManagement_Object = MibTableColumn
raisecomPtpMsgStatSendManagement = _RaisecomPtpMsgStatSendManagement_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 19),
    _RaisecomPtpMsgStatSendManagement_Type()
)
raisecomPtpMsgStatSendManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendManagement.setStatus("current")
_RaisecomPtpMsgStatReceiveManagement_Type = Integer32
_RaisecomPtpMsgStatReceiveManagement_Object = MibTableColumn
raisecomPtpMsgStatReceiveManagement = _RaisecomPtpMsgStatReceiveManagement_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 20),
    _RaisecomPtpMsgStatReceiveManagement_Type()
)
raisecomPtpMsgStatReceiveManagement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceiveManagement.setStatus("current")
_RaisecomPtpMsgStatSendError_Type = Integer32
_RaisecomPtpMsgStatSendError_Object = MibTableColumn
raisecomPtpMsgStatSendError = _RaisecomPtpMsgStatSendError_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 21),
    _RaisecomPtpMsgStatSendError_Type()
)
raisecomPtpMsgStatSendError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendError.setStatus("current")
_RaisecomPtpMsgStatReceiveUnknown_Type = Integer32
_RaisecomPtpMsgStatReceiveUnknown_Object = MibTableColumn
raisecomPtpMsgStatReceiveUnknown = _RaisecomPtpMsgStatReceiveUnknown_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 22),
    _RaisecomPtpMsgStatReceiveUnknown_Type()
)
raisecomPtpMsgStatReceiveUnknown.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceiveUnknown.setStatus("current")
_RaisecomPtpMsgStatSendTotalNum_Type = Integer32
_RaisecomPtpMsgStatSendTotalNum_Object = MibTableColumn
raisecomPtpMsgStatSendTotalNum = _RaisecomPtpMsgStatSendTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 23),
    _RaisecomPtpMsgStatSendTotalNum_Type()
)
raisecomPtpMsgStatSendTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatSendTotalNum.setStatus("current")
_RaisecomPtpMsgStatReceiveTotalNum_Type = Integer32
_RaisecomPtpMsgStatReceiveTotalNum_Object = MibTableColumn
raisecomPtpMsgStatReceiveTotalNum = _RaisecomPtpMsgStatReceiveTotalNum_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 8, 1, 1, 24),
    _RaisecomPtpMsgStatReceiveTotalNum_Type()
)
raisecomPtpMsgStatReceiveTotalNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpMsgStatReceiveTotalNum.setStatus("current")
_RaisecomPtpUnicastAddr_ObjectIdentity = ObjectIdentity
raisecomPtpUnicastAddr = _RaisecomPtpUnicastAddr_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9)
)
_RaisecomPtpUnicastMasterPoolTable_Object = MibTable
raisecomPtpUnicastMasterPoolTable = _RaisecomPtpUnicastMasterPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 1)
)
if mibBuilder.loadTexts:
    raisecomPtpUnicastMasterPoolTable.setStatus("current")
_RaisecomPtpUnicastMasterPoolEntry_Object = MibTableRow
raisecomPtpUnicastMasterPoolEntry = _RaisecomPtpUnicastMasterPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 1, 1)
)
raisecomPtpUnicastMasterPoolEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
    (0, "RAISECOM-PTP-MIB", "raisecomPtpUnicastMasterPoolIndex"),
)
if mibBuilder.loadTexts:
    raisecomPtpUnicastMasterPoolEntry.setStatus("current")
_RaisecomPtpUnicastMasterPoolIndex_Type = Integer32
_RaisecomPtpUnicastMasterPoolIndex_Object = MibTableColumn
raisecomPtpUnicastMasterPoolIndex = _RaisecomPtpUnicastMasterPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 1, 1, 1),
    _RaisecomPtpUnicastMasterPoolIndex_Type()
)
raisecomPtpUnicastMasterPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomPtpUnicastMasterPoolIndex.setStatus("current")
_RaisecomPtpUnicastMasterPoolMac_Type = MacAddress
_RaisecomPtpUnicastMasterPoolMac_Object = MibTableColumn
raisecomPtpUnicastMasterPoolMac = _RaisecomPtpUnicastMasterPoolMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 1, 1, 2),
    _RaisecomPtpUnicastMasterPoolMac_Type()
)
raisecomPtpUnicastMasterPoolMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomPtpUnicastMasterPoolMac.setStatus("current")


class _RaisecomPtpUnicastMasterPoolVlan_Type(Integer32):
    """Custom type raisecomPtpUnicastMasterPoolVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomPtpUnicastMasterPoolVlan_Type.__name__ = "Integer32"
_RaisecomPtpUnicastMasterPoolVlan_Object = MibTableColumn
raisecomPtpUnicastMasterPoolVlan = _RaisecomPtpUnicastMasterPoolVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 1, 1, 3),
    _RaisecomPtpUnicastMasterPoolVlan_Type()
)
raisecomPtpUnicastMasterPoolVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomPtpUnicastMasterPoolVlan.setStatus("current")
_RaisecomPtpUnicastMasterPoolIp_Type = IpAddress
_RaisecomPtpUnicastMasterPoolIp_Object = MibTableColumn
raisecomPtpUnicastMasterPoolIp = _RaisecomPtpUnicastMasterPoolIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 1, 1, 4),
    _RaisecomPtpUnicastMasterPoolIp_Type()
)
raisecomPtpUnicastMasterPoolIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomPtpUnicastMasterPoolIp.setStatus("current")
_RaisecomPtpUnicastMasterPoolRowStatus_Type = RowStatus
_RaisecomPtpUnicastMasterPoolRowStatus_Object = MibTableColumn
raisecomPtpUnicastMasterPoolRowStatus = _RaisecomPtpUnicastMasterPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 1, 1, 5),
    _RaisecomPtpUnicastMasterPoolRowStatus_Type()
)
raisecomPtpUnicastMasterPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomPtpUnicastMasterPoolRowStatus.setStatus("current")


class _RaisecomPtpUnicastMasterPoolFlag_Type(Integer32):
    """Custom type raisecomPtpUnicastMasterPoolFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("announce", 1),
          ("sync", 2),
          ("delay", 3),
          ("pdelay", 4))
    )


_RaisecomPtpUnicastMasterPoolFlag_Type.__name__ = "Integer32"
_RaisecomPtpUnicastMasterPoolFlag_Object = MibTableColumn
raisecomPtpUnicastMasterPoolFlag = _RaisecomPtpUnicastMasterPoolFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 1, 1, 6),
    _RaisecomPtpUnicastMasterPoolFlag_Type()
)
raisecomPtpUnicastMasterPoolFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpUnicastMasterPoolFlag.setStatus("current")
_RaisecomPtpUnicastSlavePoolTable_Object = MibTable
raisecomPtpUnicastSlavePoolTable = _RaisecomPtpUnicastSlavePoolTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 2)
)
if mibBuilder.loadTexts:
    raisecomPtpUnicastSlavePoolTable.setStatus("current")
_RaisecomPtpUnicastSlavePoolEntry_Object = MibTableRow
raisecomPtpUnicastSlavePoolEntry = _RaisecomPtpUnicastSlavePoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 2, 1)
)
raisecomPtpUnicastSlavePoolEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
    (0, "RAISECOM-PTP-MIB", "raisecomPtpUnicastSlavePoolIndex"),
)
if mibBuilder.loadTexts:
    raisecomPtpUnicastSlavePoolEntry.setStatus("current")
_RaisecomPtpUnicastSlavePoolIndex_Type = Integer32
_RaisecomPtpUnicastSlavePoolIndex_Object = MibTableColumn
raisecomPtpUnicastSlavePoolIndex = _RaisecomPtpUnicastSlavePoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 2, 1, 1),
    _RaisecomPtpUnicastSlavePoolIndex_Type()
)
raisecomPtpUnicastSlavePoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomPtpUnicastSlavePoolIndex.setStatus("current")
_RaisecomPtpUnicastSlavePoolMac_Type = MacAddress
_RaisecomPtpUnicastSlavePoolMac_Object = MibTableColumn
raisecomPtpUnicastSlavePoolMac = _RaisecomPtpUnicastSlavePoolMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 2, 1, 2),
    _RaisecomPtpUnicastSlavePoolMac_Type()
)
raisecomPtpUnicastSlavePoolMac.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpUnicastSlavePoolMac.setStatus("current")


class _RaisecomPtpUnicastSlavePoolVlan_Type(Integer32):
    """Custom type raisecomPtpUnicastSlavePoolVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomPtpUnicastSlavePoolVlan_Type.__name__ = "Integer32"
_RaisecomPtpUnicastSlavePoolVlan_Object = MibTableColumn
raisecomPtpUnicastSlavePoolVlan = _RaisecomPtpUnicastSlavePoolVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 2, 1, 3),
    _RaisecomPtpUnicastSlavePoolVlan_Type()
)
raisecomPtpUnicastSlavePoolVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpUnicastSlavePoolVlan.setStatus("current")
_RaisecomPtpUnicastSlavePoolIp_Type = IpAddress
_RaisecomPtpUnicastSlavePoolIp_Object = MibTableColumn
raisecomPtpUnicastSlavePoolIp = _RaisecomPtpUnicastSlavePoolIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 2, 1, 4),
    _RaisecomPtpUnicastSlavePoolIp_Type()
)
raisecomPtpUnicastSlavePoolIp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpUnicastSlavePoolIp.setStatus("current")


class _RaisecomPtpUnicastSlavePoolFlag_Type(Integer32):
    """Custom type raisecomPtpUnicastSlavePoolFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("announce", 1),
          ("sync", 2),
          ("delay", 3),
          ("pdelay", 4))
    )


_RaisecomPtpUnicastSlavePoolFlag_Type.__name__ = "Integer32"
_RaisecomPtpUnicastSlavePoolFlag_Object = MibTableColumn
raisecomPtpUnicastSlavePoolFlag = _RaisecomPtpUnicastSlavePoolFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 2, 1, 5),
    _RaisecomPtpUnicastSlavePoolFlag_Type()
)
raisecomPtpUnicastSlavePoolFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpUnicastSlavePoolFlag.setStatus("current")
_RaisecomPtpUnicastPeerPoolTable_Object = MibTable
raisecomPtpUnicastPeerPoolTable = _RaisecomPtpUnicastPeerPoolTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 3)
)
if mibBuilder.loadTexts:
    raisecomPtpUnicastPeerPoolTable.setStatus("current")
_RaisecomPtpUnicastPeerPoolEntry_Object = MibTableRow
raisecomPtpUnicastPeerPoolEntry = _RaisecomPtpUnicastPeerPoolEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 3, 1)
)
raisecomPtpUnicastPeerPoolEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
    (0, "RAISECOM-PTP-MIB", "raisecomPtpUnicastPeerPoolIndex"),
)
if mibBuilder.loadTexts:
    raisecomPtpUnicastPeerPoolEntry.setStatus("current")
_RaisecomPtpUnicastPeerPoolIndex_Type = Integer32
_RaisecomPtpUnicastPeerPoolIndex_Object = MibTableColumn
raisecomPtpUnicastPeerPoolIndex = _RaisecomPtpUnicastPeerPoolIndex_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 3, 1, 1),
    _RaisecomPtpUnicastPeerPoolIndex_Type()
)
raisecomPtpUnicastPeerPoolIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    raisecomPtpUnicastPeerPoolIndex.setStatus("current")
_RaisecomPtpUnicastPeerPoolMac_Type = MacAddress
_RaisecomPtpUnicastPeerPoolMac_Object = MibTableColumn
raisecomPtpUnicastPeerPoolMac = _RaisecomPtpUnicastPeerPoolMac_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 3, 1, 2),
    _RaisecomPtpUnicastPeerPoolMac_Type()
)
raisecomPtpUnicastPeerPoolMac.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomPtpUnicastPeerPoolMac.setStatus("current")


class _RaisecomPtpUnicastPeerPoolVlan_Type(Integer32):
    """Custom type raisecomPtpUnicastPeerPoolVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_RaisecomPtpUnicastPeerPoolVlan_Type.__name__ = "Integer32"
_RaisecomPtpUnicastPeerPoolVlan_Object = MibTableColumn
raisecomPtpUnicastPeerPoolVlan = _RaisecomPtpUnicastPeerPoolVlan_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 3, 1, 3),
    _RaisecomPtpUnicastPeerPoolVlan_Type()
)
raisecomPtpUnicastPeerPoolVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomPtpUnicastPeerPoolVlan.setStatus("current")
_RaisecomPtpUnicastPeerPoolIp_Type = IpAddress
_RaisecomPtpUnicastPeerPoolIp_Object = MibTableColumn
raisecomPtpUnicastPeerPoolIp = _RaisecomPtpUnicastPeerPoolIp_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 3, 1, 4),
    _RaisecomPtpUnicastPeerPoolIp_Type()
)
raisecomPtpUnicastPeerPoolIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomPtpUnicastPeerPoolIp.setStatus("current")
_RaisecomPtpUnicastPeerPoolRowStatus_Type = RowStatus
_RaisecomPtpUnicastPeerPoolRowStatus_Object = MibTableColumn
raisecomPtpUnicastPeerPoolRowStatus = _RaisecomPtpUnicastPeerPoolRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 3, 1, 5),
    _RaisecomPtpUnicastPeerPoolRowStatus_Type()
)
raisecomPtpUnicastPeerPoolRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    raisecomPtpUnicastPeerPoolRowStatus.setStatus("current")


class _RaisecomPtpUnicastPeerPoolFlag_Type(Integer32):
    """Custom type raisecomPtpUnicastPeerPoolFlag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("announce", 1),
          ("sync", 2),
          ("delay", 3),
          ("pdelay", 4))
    )


_RaisecomPtpUnicastPeerPoolFlag_Type.__name__ = "Integer32"
_RaisecomPtpUnicastPeerPoolFlag_Object = MibTableColumn
raisecomPtpUnicastPeerPoolFlag = _RaisecomPtpUnicastPeerPoolFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 9, 3, 1, 6),
    _RaisecomPtpUnicastPeerPoolFlag_Type()
)
raisecomPtpUnicastPeerPoolFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpUnicastPeerPoolFlag.setStatus("current")
_RaisecomPtpTClock_ObjectIdentity = ObjectIdentity
raisecomPtpTClock = _RaisecomPtpTClock_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 10)
)
_RaisecomPtpTClockIdentity_Type = PTPClockIdentity
_RaisecomPtpTClockIdentity_Object = MibScalar
raisecomPtpTClockIdentity = _RaisecomPtpTClockIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 10, 1),
    _RaisecomPtpTClockIdentity_Type()
)
raisecomPtpTClockIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTClockIdentity.setStatus("current")


class _RaisecomPtpTClockNumberPorts_Type(Integer32):
    """Custom type raisecomPtpTClockNumberPorts based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_RaisecomPtpTClockNumberPorts_Type.__name__ = "Integer32"
_RaisecomPtpTClockNumberPorts_Object = MibScalar
raisecomPtpTClockNumberPorts = _RaisecomPtpTClockNumberPorts_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 10, 2),
    _RaisecomPtpTClockNumberPorts_Type()
)
raisecomPtpTClockNumberPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTClockNumberPorts.setStatus("current")


class _RaisecomPtpTClockDelayMechanism_Type(Integer32):
    """Custom type raisecomPtpTClockDelayMechanism based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("end-to-end", 1),
          ("peer-to-peer", 2))
    )


_RaisecomPtpTClockDelayMechanism_Type.__name__ = "Integer32"
_RaisecomPtpTClockDelayMechanism_Object = MibScalar
raisecomPtpTClockDelayMechanism = _RaisecomPtpTClockDelayMechanism_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 10, 3),
    _RaisecomPtpTClockDelayMechanism_Type()
)
raisecomPtpTClockDelayMechanism.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTClockDelayMechanism.setStatus("current")


class _RaisecomPtpTClockPrimaryDomain_Type(Integer32):
    """Custom type raisecomPtpTClockPrimaryDomain based on Integer32"""
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
        *(("default", 0),
          ("alternate-domain1", 1),
          ("alternate-domain2", 2),
          ("alternate-domain3", 3))
    )


_RaisecomPtpTClockPrimaryDomain_Type.__name__ = "Integer32"
_RaisecomPtpTClockPrimaryDomain_Object = MibScalar
raisecomPtpTClockPrimaryDomain = _RaisecomPtpTClockPrimaryDomain_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 10, 4),
    _RaisecomPtpTClockPrimaryDomain_Type()
)
raisecomPtpTClockPrimaryDomain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpTClockPrimaryDomain.setStatus("current")
_RaisecomPtpTCPorts_ObjectIdentity = ObjectIdentity
raisecomPtpTCPorts = _RaisecomPtpTCPorts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 11)
)
_RaisecomPtpTCPortTable_Object = MibTable
raisecomPtpTCPortTable = _RaisecomPtpTCPortTable_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 11, 1)
)
if mibBuilder.loadTexts:
    raisecomPtpTCPortTable.setStatus("current")
_RaisecomPtpTCPortEntry_Object = MibTableRow
raisecomPtpTCPortEntry = _RaisecomPtpTCPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 11, 1, 1)
)
raisecomPtpTCPortEntry.setIndexNames(
    (0, "SWITCH-SYSTEM-MIB", "rcPortIndex"),
)
if mibBuilder.loadTexts:
    raisecomPtpTCPortEntry.setStatus("current")
_RaisecomPtpTCPortIdentity_Type = OctetString
_RaisecomPtpTCPortIdentity_Object = MibTableColumn
raisecomPtpTCPortIdentity = _RaisecomPtpTCPortIdentity_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 11, 1, 1, 1),
    _RaisecomPtpTCPortIdentity_Type()
)
raisecomPtpTCPortIdentity.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTCPortIdentity.setStatus("current")


class _RaisecomPtpTCPortLogMinPdelayReqInterval_Type(Integer32):
    """Custom type raisecomPtpTCPortLogMinPdelayReqInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-6, -1),
    )


_RaisecomPtpTCPortLogMinPdelayReqInterval_Type.__name__ = "Integer32"
_RaisecomPtpTCPortLogMinPdelayReqInterval_Object = MibTableColumn
raisecomPtpTCPortLogMinPdelayReqInterval = _RaisecomPtpTCPortLogMinPdelayReqInterval_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 11, 1, 1, 2),
    _RaisecomPtpTCPortLogMinPdelayReqInterval_Type()
)
raisecomPtpTCPortLogMinPdelayReqInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpTCPortLogMinPdelayReqInterval.setStatus("current")


class _RaisecomPtpTCPortFaultyFlag_Type(Integer32):
    """Custom type raisecomPtpTCPortFaultyFlag based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("normal", 0),
          ("faulty", 1))
    )


_RaisecomPtpTCPortFaultyFlag_Type.__name__ = "Integer32"
_RaisecomPtpTCPortFaultyFlag_Object = MibTableColumn
raisecomPtpTCPortFaultyFlag = _RaisecomPtpTCPortFaultyFlag_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 11, 1, 1, 3),
    _RaisecomPtpTCPortFaultyFlag_Type()
)
raisecomPtpTCPortFaultyFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    raisecomPtpTCPortFaultyFlag.setStatus("current")
_RaisecomPtpTCPortPeerMeanPathDelay_Type = PTPTimeInterval
_RaisecomPtpTCPortPeerMeanPathDelay_Object = MibTableColumn
raisecomPtpTCPortPeerMeanPathDelay = _RaisecomPtpTCPortPeerMeanPathDelay_Object(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 11, 1, 1, 4),
    _RaisecomPtpTCPortPeerMeanPathDelay_Type()
)
raisecomPtpTCPortPeerMeanPathDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    raisecomPtpTCPortPeerMeanPathDelay.setStatus("current")
_RaisecomPtpTraps_ObjectIdentity = ObjectIdentity
raisecomPtpTraps = _RaisecomPtpTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 12)
)

# Managed Objects groups


# Notification objects

raisecomPtpSyncTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 8886, 1, 26, 12, 15)
)
raisecomPtpSyncTrap.setObjects(
      *(("RAISECOM-PTP-MIB", "raisecomPtpPortState"),
        ("RAISECOM-PTP-MIB", "raisecomPtpPortIdentity"))
)
if mibBuilder.loadTexts:
    raisecomPtpSyncTrap.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "RAISECOM-PTP-MIB",
    **{"PTPTimeStamp": PTPTimeStamp,
       "PTPTimeInterval": PTPTimeInterval,
       "PTPClockIdentity": PTPClockIdentity,
       "PTPPortIdentity": PTPPortIdentity,
       "raisecomPtp": raisecomPtp,
       "raisecomPtpGlobal": raisecomPtpGlobal,
       "raisecomPtpEnable": raisecomPtpEnable,
       "raisecomPtpClockMode": raisecomPtpClockMode,
       "raisecomPtpClockUnicastFlag": raisecomPtpClockUnicastFlag,
       "raisecomPtpClockStepFlag": raisecomPtpClockStepFlag,
       "raisecomPtpClockStatisticClear": raisecomPtpClockStatisticClear,
       "raisecomPtpGlobalPortTable": raisecomPtpGlobalPortTable,
       "raisecomPtpGlobalPortEntry": raisecomPtpGlobalPortEntry,
       "raisecomPtpPortEnable": raisecomPtpPortEnable,
       "raisecomPtpPortTransmitProtocol": raisecomPtpPortTransmitProtocol,
       "raisecomPtpPortVlan": raisecomPtpPortVlan,
       "raisecomPtpPortAsymmetryDelay": raisecomPtpPortAsymmetryDelay,
       "raisecomPtpClock": raisecomPtpClock,
       "raisecomPtpClockIdentity": raisecomPtpClockIdentity,
       "raisecomPtpClockDomain": raisecomPtpClockDomain,
       "raisecomPtpClockPriority1": raisecomPtpClockPriority1,
       "raisecomPtpClockPriority2": raisecomPtpClockPriority2,
       "raisecomPtpClockClass": raisecomPtpClockClass,
       "raisecomPtpClockAccuracy": raisecomPtpClockAccuracy,
       "raisecomPtpClockOffsetScaledLogVariance": raisecomPtpClockOffsetScaledLogVariance,
       "raisecomPtpClockNumberPorts": raisecomPtpClockNumberPorts,
       "raisecomPtpClockSlaveOnly": raisecomPtpClockSlaveOnly,
       "raisecomPtpCurrent": raisecomPtpCurrent,
       "raisecomPtpCurrentEndMeanPathDelay": raisecomPtpCurrentEndMeanPathDelay,
       "raisecomPtpCurrentOffsetFromParent": raisecomPtpCurrentOffsetFromParent,
       "raisecomPtpCurrentStepsRemoved": raisecomPtpCurrentStepsRemoved,
       "raisecomPtpParent": raisecomPtpParent,
       "raisecomPtpParentPortIdentity": raisecomPtpParentPortIdentity,
       "raisecomPtpParentSatisticsFlag": raisecomPtpParentSatisticsFlag,
       "raisecomPtpParentOffsetScaledLogVariance": raisecomPtpParentOffsetScaledLogVariance,
       "raisecomPtpParentPhaseChangeRate": raisecomPtpParentPhaseChangeRate,
       "raisecomPtpGrandmasterIdentity": raisecomPtpGrandmasterIdentity,
       "raisecomPtpGrandmasterPriority1": raisecomPtpGrandmasterPriority1,
       "raisecomPtpGrandmasterPriority2": raisecomPtpGrandmasterPriority2,
       "raisecomPtpGrandmasterClockClass": raisecomPtpGrandmasterClockClass,
       "raisecomPtpGrandmasterClockAccuracy": raisecomPtpGrandmasterClockAccuracy,
       "raisecomPtpGrandmasterOffsetScaledLogVariance": raisecomPtpGrandmasterOffsetScaledLogVariance,
       "raisecomPtpTimeProperty": raisecomPtpTimeProperty,
       "raisecomPtpTimeProCurrentUtcOffset": raisecomPtpTimeProCurrentUtcOffset,
       "raisecomPtpTimeProCurrentUtcOffsetValid": raisecomPtpTimeProCurrentUtcOffsetValid,
       "raisecomPtpTimeProLeap": raisecomPtpTimeProLeap,
       "raisecomPtpTimeProTimeFrequencyTraceable": raisecomPtpTimeProTimeFrequencyTraceable,
       "raisecomPtpTimeProMatchTimescale": raisecomPtpTimeProMatchTimescale,
       "raisecomPtpTimeProTimeSource": raisecomPtpTimeProTimeSource,
       "raisecomPtpTimeProTimeSourceOper": raisecomPtpTimeProTimeSourceOper,
       "raisecomPtpPorts": raisecomPtpPorts,
       "raisecomPtpPortTable": raisecomPtpPortTable,
       "raisecomPtpPortEntry": raisecomPtpPortEntry,
       "raisecomPtpPortIdentity": raisecomPtpPortIdentity,
       "raisecomPtpPortState": raisecomPtpPortState,
       "raisecomPtpPortStateForce": raisecomPtpPortStateForce,
       "raisecomPtpPortDelayMechanism": raisecomPtpPortDelayMechanism,
       "raisecomPtpPortPeerMeanPathDelay": raisecomPtpPortPeerMeanPathDelay,
       "raisecomPtpPortLogSyncInterval": raisecomPtpPortLogSyncInterval,
       "raisecomPtpPortLogAnnounceInterval": raisecomPtpPortLogAnnounceInterval,
       "raisecomPtpPortLogMinDelayRequestInterval": raisecomPtpPortLogMinDelayRequestInterval,
       "raisecomPtpPortAnnounceReceiptTimeout": raisecomPtpPortAnnounceReceiptTimeout,
       "raisecomPtpPortLogMinPDelayRequestInterval": raisecomPtpPortLogMinPDelayRequestInterval,
       "raisecomPtpPortVersionNumber": raisecomPtpPortVersionNumber,
       "raisecomPtpPortUnicastMasterMaxIndex": raisecomPtpPortUnicastMasterMaxIndex,
       "raisecomPtpPortUnicastPeerMaxIndex": raisecomPtpPortUnicastPeerMaxIndex,
       "raisecomPtpForeignRecords": raisecomPtpForeignRecords,
       "raisecomPtpForeignRecordTable": raisecomPtpForeignRecordTable,
       "raisecomPtpForeignRecordEntry": raisecomPtpForeignRecordEntry,
       "raisecomPtpForeignRecordIndex": raisecomPtpForeignRecordIndex,
       "raisecomPtpForeignRecordValid": raisecomPtpForeignRecordValid,
       "raisecomPtpForeignRecordPortIdentity": raisecomPtpForeignRecordPortIdentity,
       "raisecomPtpForeignRecordAnnounceNum": raisecomPtpForeignRecordAnnounceNum,
       "raisecomPtpMessageStat": raisecomPtpMessageStat,
       "raisecomPtpMessageStatTable": raisecomPtpMessageStatTable,
       "raisecomPtpMessageStatEntry": raisecomPtpMessageStatEntry,
       "raisecomPtpMsgStatSendSync": raisecomPtpMsgStatSendSync,
       "raisecomPtpMsgStatReceiveSync": raisecomPtpMsgStatReceiveSync,
       "raisecomPtpMsgStatSendAnnounce": raisecomPtpMsgStatSendAnnounce,
       "raisecomPtpMsgStatReceiveAnnounce": raisecomPtpMsgStatReceiveAnnounce,
       "raisecomPtpMsgStatSendFollowUp": raisecomPtpMsgStatSendFollowUp,
       "raisecomPtpMsgStatReceiveFollowUp": raisecomPtpMsgStatReceiveFollowUp,
       "raisecomPtpMsgStatSendDelayReq": raisecomPtpMsgStatSendDelayReq,
       "raisecomPtpMsgStatReceiveDelayReq": raisecomPtpMsgStatReceiveDelayReq,
       "raisecomPtpMsgStatSendDelayResp": raisecomPtpMsgStatSendDelayResp,
       "raisecomPtpMsgStatReceiveDelayResp": raisecomPtpMsgStatReceiveDelayResp,
       "raisecomPtpMsgStatSendPdelayReq": raisecomPtpMsgStatSendPdelayReq,
       "raisecomPtpMsgStatReceivePdelayReq": raisecomPtpMsgStatReceivePdelayReq,
       "raisecomPtpMsgStatSendPdelayResp": raisecomPtpMsgStatSendPdelayResp,
       "raisecomPtpMsgStatReceivePdelayResp": raisecomPtpMsgStatReceivePdelayResp,
       "raisecomPtpMsgStatSendPdelayRespFUp": raisecomPtpMsgStatSendPdelayRespFUp,
       "raisecomPtpMsgStatReceivePdelayRespFUp": raisecomPtpMsgStatReceivePdelayRespFUp,
       "raisecomPtpMsgStatSendSignaling": raisecomPtpMsgStatSendSignaling,
       "raisecomPtpMsgStatReceiveSignaling": raisecomPtpMsgStatReceiveSignaling,
       "raisecomPtpMsgStatSendManagement": raisecomPtpMsgStatSendManagement,
       "raisecomPtpMsgStatReceiveManagement": raisecomPtpMsgStatReceiveManagement,
       "raisecomPtpMsgStatSendError": raisecomPtpMsgStatSendError,
       "raisecomPtpMsgStatReceiveUnknown": raisecomPtpMsgStatReceiveUnknown,
       "raisecomPtpMsgStatSendTotalNum": raisecomPtpMsgStatSendTotalNum,
       "raisecomPtpMsgStatReceiveTotalNum": raisecomPtpMsgStatReceiveTotalNum,
       "raisecomPtpUnicastAddr": raisecomPtpUnicastAddr,
       "raisecomPtpUnicastMasterPoolTable": raisecomPtpUnicastMasterPoolTable,
       "raisecomPtpUnicastMasterPoolEntry": raisecomPtpUnicastMasterPoolEntry,
       "raisecomPtpUnicastMasterPoolIndex": raisecomPtpUnicastMasterPoolIndex,
       "raisecomPtpUnicastMasterPoolMac": raisecomPtpUnicastMasterPoolMac,
       "raisecomPtpUnicastMasterPoolVlan": raisecomPtpUnicastMasterPoolVlan,
       "raisecomPtpUnicastMasterPoolIp": raisecomPtpUnicastMasterPoolIp,
       "raisecomPtpUnicastMasterPoolRowStatus": raisecomPtpUnicastMasterPoolRowStatus,
       "raisecomPtpUnicastMasterPoolFlag": raisecomPtpUnicastMasterPoolFlag,
       "raisecomPtpUnicastSlavePoolTable": raisecomPtpUnicastSlavePoolTable,
       "raisecomPtpUnicastSlavePoolEntry": raisecomPtpUnicastSlavePoolEntry,
       "raisecomPtpUnicastSlavePoolIndex": raisecomPtpUnicastSlavePoolIndex,
       "raisecomPtpUnicastSlavePoolMac": raisecomPtpUnicastSlavePoolMac,
       "raisecomPtpUnicastSlavePoolVlan": raisecomPtpUnicastSlavePoolVlan,
       "raisecomPtpUnicastSlavePoolIp": raisecomPtpUnicastSlavePoolIp,
       "raisecomPtpUnicastSlavePoolFlag": raisecomPtpUnicastSlavePoolFlag,
       "raisecomPtpUnicastPeerPoolTable": raisecomPtpUnicastPeerPoolTable,
       "raisecomPtpUnicastPeerPoolEntry": raisecomPtpUnicastPeerPoolEntry,
       "raisecomPtpUnicastPeerPoolIndex": raisecomPtpUnicastPeerPoolIndex,
       "raisecomPtpUnicastPeerPoolMac": raisecomPtpUnicastPeerPoolMac,
       "raisecomPtpUnicastPeerPoolVlan": raisecomPtpUnicastPeerPoolVlan,
       "raisecomPtpUnicastPeerPoolIp": raisecomPtpUnicastPeerPoolIp,
       "raisecomPtpUnicastPeerPoolRowStatus": raisecomPtpUnicastPeerPoolRowStatus,
       "raisecomPtpUnicastPeerPoolFlag": raisecomPtpUnicastPeerPoolFlag,
       "raisecomPtpTClock": raisecomPtpTClock,
       "raisecomPtpTClockIdentity": raisecomPtpTClockIdentity,
       "raisecomPtpTClockNumberPorts": raisecomPtpTClockNumberPorts,
       "raisecomPtpTClockDelayMechanism": raisecomPtpTClockDelayMechanism,
       "raisecomPtpTClockPrimaryDomain": raisecomPtpTClockPrimaryDomain,
       "raisecomPtpTCPorts": raisecomPtpTCPorts,
       "raisecomPtpTCPortTable": raisecomPtpTCPortTable,
       "raisecomPtpTCPortEntry": raisecomPtpTCPortEntry,
       "raisecomPtpTCPortIdentity": raisecomPtpTCPortIdentity,
       "raisecomPtpTCPortLogMinPdelayReqInterval": raisecomPtpTCPortLogMinPdelayReqInterval,
       "raisecomPtpTCPortFaultyFlag": raisecomPtpTCPortFaultyFlag,
       "raisecomPtpTCPortPeerMeanPathDelay": raisecomPtpTCPortPeerMeanPathDelay,
       "raisecomPtpTraps": raisecomPtpTraps,
       "raisecomPtpSyncTrap": raisecomPtpSyncTrap}
)
