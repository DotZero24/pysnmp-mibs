# SNMP MIB module (AC-PM-Control-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/mediant/AC-PM-Control-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:22:06 2025
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

(acBoardMibs,
 acGeneric,
 acPerformance,
 acProducts,
 acRegistrations,
 audioCodes) = mibBuilder.importSymbols(
    "AUDIOCODES-TYPES-MIB",
    "acBoardMibs",
    "acGeneric",
    "acPerformance",
    "acProducts",
    "acRegistrations",
    "audioCodes")

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 enterprises,
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
    "enterprises",
    "iso")

(DateAndTime,
 DisplayString,
 PhysAddress,
 TAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TAddress",
    "TextualConvention")


# MODULE-IDENTITY

acPMControl = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AcPMControlConfiguration_ObjectIdentity = ObjectIdentity
acPMControlConfiguration = _AcPMControlConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1)
)


class _AcPMControlConfigurationPeriodLength_Type(Unsigned32):
    """Custom type acPMControlConfigurationPeriodLength based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 894780),
    )


_AcPMControlConfigurationPeriodLength_Type.__name__ = "Unsigned32"
_AcPMControlConfigurationPeriodLength_Object = MibScalar
acPMControlConfigurationPeriodLength = _AcPMControlConfigurationPeriodLength_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 1),
    _AcPMControlConfigurationPeriodLength_Type()
)
acPMControlConfigurationPeriodLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMControlConfigurationPeriodLength.setStatus("current")


class _AcPMControlConfigurationResetTotalCounters_Type(Integer32):
    """Custom type acPMControlConfigurationResetTotalCounters based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("resetCountersDone", 1),
          ("resetTotalCounters", 2))
    )


_AcPMControlConfigurationResetTotalCounters_Type.__name__ = "Integer32"
_AcPMControlConfigurationResetTotalCounters_Object = MibScalar
acPMControlConfigurationResetTotalCounters = _AcPMControlConfigurationResetTotalCounters_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 2),
    _AcPMControlConfigurationResetTotalCounters_Type()
)
acPMControlConfigurationResetTotalCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMControlConfigurationResetTotalCounters.setStatus("current")
_AcPMCPConnectionAttributes_ObjectIdentity = ObjectIdentity
acPMCPConnectionAttributes = _AcPMCPConnectionAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32)
)


class _AcPMCPConnectionAttributesLifetimeHighThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesLifetimeHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesLifetimeHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesLifetimeHighThreshold_Object = MibScalar
acPMCPConnectionAttributesLifetimeHighThreshold = _AcPMCPConnectionAttributesLifetimeHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 1),
    _AcPMCPConnectionAttributesLifetimeHighThreshold_Type()
)
acPMCPConnectionAttributesLifetimeHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesLifetimeHighThreshold.setStatus("current")


class _AcPMCPConnectionAttributesLifetimeLowThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesLifetimeLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesLifetimeLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesLifetimeLowThreshold_Object = MibScalar
acPMCPConnectionAttributesLifetimeLowThreshold = _AcPMCPConnectionAttributesLifetimeLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 2),
    _AcPMCPConnectionAttributesLifetimeLowThreshold_Type()
)
acPMCPConnectionAttributesLifetimeLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesLifetimeLowThreshold.setStatus("current")


class _AcPMCPConnectionAttributesStateHighThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesStateHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesStateHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesStateHighThreshold_Object = MibScalar
acPMCPConnectionAttributesStateHighThreshold = _AcPMCPConnectionAttributesStateHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 3),
    _AcPMCPConnectionAttributesStateHighThreshold_Type()
)
acPMCPConnectionAttributesStateHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesStateHighThreshold.setStatus("current")


class _AcPMCPConnectionAttributesStateLowThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesStateLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesStateLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesStateLowThreshold_Object = MibScalar
acPMCPConnectionAttributesStateLowThreshold = _AcPMCPConnectionAttributesStateLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 4),
    _AcPMCPConnectionAttributesStateLowThreshold_Type()
)
acPMCPConnectionAttributesStateLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesStateLowThreshold.setStatus("current")


class _AcPMCPConnectionAttributesCommandCounterHighThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesCommandCounterHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesCommandCounterHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesCommandCounterHighThreshold_Object = MibScalar
acPMCPConnectionAttributesCommandCounterHighThreshold = _AcPMCPConnectionAttributesCommandCounterHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 5),
    _AcPMCPConnectionAttributesCommandCounterHighThreshold_Type()
)
acPMCPConnectionAttributesCommandCounterHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesCommandCounterHighThreshold.setStatus("current")


class _AcPMCPConnectionAttributesCommandCounterLowThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesCommandCounterLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesCommandCounterLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesCommandCounterLowThreshold_Object = MibScalar
acPMCPConnectionAttributesCommandCounterLowThreshold = _AcPMCPConnectionAttributesCommandCounterLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 6),
    _AcPMCPConnectionAttributesCommandCounterLowThreshold_Type()
)
acPMCPConnectionAttributesCommandCounterLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesCommandCounterLowThreshold.setStatus("current")


class _AcPMCPConnectionAttributesRetransmissionCountHighThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesRetransmissionCountHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesRetransmissionCountHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesRetransmissionCountHighThreshold_Object = MibScalar
acPMCPConnectionAttributesRetransmissionCountHighThreshold = _AcPMCPConnectionAttributesRetransmissionCountHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 7),
    _AcPMCPConnectionAttributesRetransmissionCountHighThreshold_Type()
)
acPMCPConnectionAttributesRetransmissionCountHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesRetransmissionCountHighThreshold.setStatus("current")


class _AcPMCPConnectionAttributesRetransmissionCountLowThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesRetransmissionCountLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesRetransmissionCountLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesRetransmissionCountLowThreshold_Object = MibScalar
acPMCPConnectionAttributesRetransmissionCountLowThreshold = _AcPMCPConnectionAttributesRetransmissionCountLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 8),
    _AcPMCPConnectionAttributesRetransmissionCountLowThreshold_Type()
)
acPMCPConnectionAttributesRetransmissionCountLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesRetransmissionCountLowThreshold.setStatus("current")


class _AcPMCPConnectionAttributesActiveContextCountHighThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesActiveContextCountHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesActiveContextCountHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesActiveContextCountHighThreshold_Object = MibScalar
acPMCPConnectionAttributesActiveContextCountHighThreshold = _AcPMCPConnectionAttributesActiveContextCountHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 9),
    _AcPMCPConnectionAttributesActiveContextCountHighThreshold_Type()
)
acPMCPConnectionAttributesActiveContextCountHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesActiveContextCountHighThreshold.setStatus("current")


class _AcPMCPConnectionAttributesActiveContextCountLowThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesActiveContextCountLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesActiveContextCountLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesActiveContextCountLowThreshold_Object = MibScalar
acPMCPConnectionAttributesActiveContextCountLowThreshold = _AcPMCPConnectionAttributesActiveContextCountLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 10),
    _AcPMCPConnectionAttributesActiveContextCountLowThreshold_Type()
)
acPMCPConnectionAttributesActiveContextCountLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesActiveContextCountLowThreshold.setStatus("current")


class _AcPMCPConnectionAttributesCommandSuccessCountHighThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesCommandSuccessCountHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesCommandSuccessCountHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesCommandSuccessCountHighThreshold_Object = MibScalar
acPMCPConnectionAttributesCommandSuccessCountHighThreshold = _AcPMCPConnectionAttributesCommandSuccessCountHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 11),
    _AcPMCPConnectionAttributesCommandSuccessCountHighThreshold_Type()
)
acPMCPConnectionAttributesCommandSuccessCountHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesCommandSuccessCountHighThreshold.setStatus("obsolete")


class _AcPMCPConnectionAttributesCommandSuccessCountLowThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesCommandSuccessCountLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesCommandSuccessCountLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesCommandSuccessCountLowThreshold_Object = MibScalar
acPMCPConnectionAttributesCommandSuccessCountLowThreshold = _AcPMCPConnectionAttributesCommandSuccessCountLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 12),
    _AcPMCPConnectionAttributesCommandSuccessCountLowThreshold_Type()
)
acPMCPConnectionAttributesCommandSuccessCountLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesCommandSuccessCountLowThreshold.setStatus("obsolete")


class _AcPMCPConnectionAttributesCommandFailureCountHighThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesCommandFailureCountHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesCommandFailureCountHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesCommandFailureCountHighThreshold_Object = MibScalar
acPMCPConnectionAttributesCommandFailureCountHighThreshold = _AcPMCPConnectionAttributesCommandFailureCountHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 13),
    _AcPMCPConnectionAttributesCommandFailureCountHighThreshold_Type()
)
acPMCPConnectionAttributesCommandFailureCountHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesCommandFailureCountHighThreshold.setStatus("obsolete")


class _AcPMCPConnectionAttributesCommandFailureCountLowThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesCommandFailureCountLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesCommandFailureCountLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesCommandFailureCountLowThreshold_Object = MibScalar
acPMCPConnectionAttributesCommandFailureCountLowThreshold = _AcPMCPConnectionAttributesCommandFailureCountLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 14),
    _AcPMCPConnectionAttributesCommandFailureCountLowThreshold_Type()
)
acPMCPConnectionAttributesCommandFailureCountLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesCommandFailureCountLowThreshold.setStatus("obsolete")


class _AcPMCPConnectionAttributesCommandProcessTimeHighThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesCommandProcessTimeHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesCommandProcessTimeHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesCommandProcessTimeHighThreshold_Object = MibScalar
acPMCPConnectionAttributesCommandProcessTimeHighThreshold = _AcPMCPConnectionAttributesCommandProcessTimeHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 15),
    _AcPMCPConnectionAttributesCommandProcessTimeHighThreshold_Type()
)
acPMCPConnectionAttributesCommandProcessTimeHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesCommandProcessTimeHighThreshold.setStatus("current")


class _AcPMCPConnectionAttributesCommandProcessTimeLowThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesCommandProcessTimeLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesCommandProcessTimeLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesCommandProcessTimeLowThreshold_Object = MibScalar
acPMCPConnectionAttributesCommandProcessTimeLowThreshold = _AcPMCPConnectionAttributesCommandProcessTimeLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 16),
    _AcPMCPConnectionAttributesCommandProcessTimeLowThreshold_Type()
)
acPMCPConnectionAttributesCommandProcessTimeLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesCommandProcessTimeLowThreshold.setStatus("current")


class _AcPMCPConnectionAttributesTransactionProcessTimerHighThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesTransactionProcessTimerHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesTransactionProcessTimerHighThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesTransactionProcessTimerHighThreshold_Object = MibScalar
acPMCPConnectionAttributesTransactionProcessTimerHighThreshold = _AcPMCPConnectionAttributesTransactionProcessTimerHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 17),
    _AcPMCPConnectionAttributesTransactionProcessTimerHighThreshold_Type()
)
acPMCPConnectionAttributesTransactionProcessTimerHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesTransactionProcessTimerHighThreshold.setStatus("current")


class _AcPMCPConnectionAttributesTransactionProcessTimerLowThreshold_Type(Unsigned32):
    """Custom type acPMCPConnectionAttributesTransactionProcessTimerLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMCPConnectionAttributesTransactionProcessTimerLowThreshold_Type.__name__ = "Unsigned32"
_AcPMCPConnectionAttributesTransactionProcessTimerLowThreshold_Object = MibScalar
acPMCPConnectionAttributesTransactionProcessTimerLowThreshold = _AcPMCPConnectionAttributesTransactionProcessTimerLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 32, 18),
    _AcPMCPConnectionAttributesTransactionProcessTimerLowThreshold_Type()
)
acPMCPConnectionAttributesTransactionProcessTimerLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMCPConnectionAttributesTransactionProcessTimerLowThreshold.setStatus("current")
_AcPMMegacoAttributes_ObjectIdentity = ObjectIdentity
acPMMegacoAttributes = _AcPMMegacoAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 33)
)


class _AcPMMegacoAttributesServiceChangeCountHighThreshold_Type(Unsigned32):
    """Custom type acPMMegacoAttributesServiceChangeCountHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMegacoAttributesServiceChangeCountHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMegacoAttributesServiceChangeCountHighThreshold_Object = MibScalar
acPMMegacoAttributesServiceChangeCountHighThreshold = _AcPMMegacoAttributesServiceChangeCountHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 33, 1),
    _AcPMMegacoAttributesServiceChangeCountHighThreshold_Type()
)
acPMMegacoAttributesServiceChangeCountHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMegacoAttributesServiceChangeCountHighThreshold.setStatus("current")


class _AcPMMegacoAttributesServiceChangeCountLowThreshold_Type(Unsigned32):
    """Custom type acPMMegacoAttributesServiceChangeCountLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMegacoAttributesServiceChangeCountLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMegacoAttributesServiceChangeCountLowThreshold_Object = MibScalar
acPMMegacoAttributesServiceChangeCountLowThreshold = _AcPMMegacoAttributesServiceChangeCountLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 33, 2),
    _AcPMMegacoAttributesServiceChangeCountLowThreshold_Type()
)
acPMMegacoAttributesServiceChangeCountLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMegacoAttributesServiceChangeCountLowThreshold.setStatus("current")


class _AcPMMegacoAttributesCmdSuccessCountHighThreshold_Type(Unsigned32):
    """Custom type acPMMegacoAttributesCmdSuccessCountHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMegacoAttributesCmdSuccessCountHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMegacoAttributesCmdSuccessCountHighThreshold_Object = MibScalar
acPMMegacoAttributesCmdSuccessCountHighThreshold = _AcPMMegacoAttributesCmdSuccessCountHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 33, 3),
    _AcPMMegacoAttributesCmdSuccessCountHighThreshold_Type()
)
acPMMegacoAttributesCmdSuccessCountHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMegacoAttributesCmdSuccessCountHighThreshold.setStatus("obsolete")


class _AcPMMegacoAttributesCmdSuccessCountLowThreshold_Type(Unsigned32):
    """Custom type acPMMegacoAttributesCmdSuccessCountLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMegacoAttributesCmdSuccessCountLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMegacoAttributesCmdSuccessCountLowThreshold_Object = MibScalar
acPMMegacoAttributesCmdSuccessCountLowThreshold = _AcPMMegacoAttributesCmdSuccessCountLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 33, 4),
    _AcPMMegacoAttributesCmdSuccessCountLowThreshold_Type()
)
acPMMegacoAttributesCmdSuccessCountLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMegacoAttributesCmdSuccessCountLowThreshold.setStatus("obsolete")


class _AcPMMegacoAttributesCmdFailureCountHighThreshold_Type(Unsigned32):
    """Custom type acPMMegacoAttributesCmdFailureCountHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMegacoAttributesCmdFailureCountHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMegacoAttributesCmdFailureCountHighThreshold_Object = MibScalar
acPMMegacoAttributesCmdFailureCountHighThreshold = _AcPMMegacoAttributesCmdFailureCountHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 33, 5),
    _AcPMMegacoAttributesCmdFailureCountHighThreshold_Type()
)
acPMMegacoAttributesCmdFailureCountHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMegacoAttributesCmdFailureCountHighThreshold.setStatus("obsolete")


class _AcPMMegacoAttributesCmdFailureCountLowThreshold_Type(Unsigned32):
    """Custom type acPMMegacoAttributesCmdFailureCountLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMegacoAttributesCmdFailureCountLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMegacoAttributesCmdFailureCountLowThreshold_Object = MibScalar
acPMMegacoAttributesCmdFailureCountLowThreshold = _AcPMMegacoAttributesCmdFailureCountLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 33, 6),
    _AcPMMegacoAttributesCmdFailureCountLowThreshold_Type()
)
acPMMegacoAttributesCmdFailureCountLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMegacoAttributesCmdFailureCountLowThreshold.setStatus("obsolete")
_AcPMSipAttributes_ObjectIdentity = ObjectIdentity
acPMSipAttributes = _AcPMSipAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34)
)


class _AcPMSipAttributesCallDurationHighThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesCallDurationHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSipAttributesCallDurationHighThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesCallDurationHighThreshold_Object = MibScalar
acPMSipAttributesCallDurationHighThreshold = _AcPMSipAttributesCallDurationHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 1),
    _AcPMSipAttributesCallDurationHighThreshold_Type()
)
acPMSipAttributesCallDurationHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesCallDurationHighThreshold.setStatus("current")


class _AcPMSipAttributesCallDurationLowThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesCallDurationLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSipAttributesCallDurationLowThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesCallDurationLowThreshold_Object = MibScalar
acPMSipAttributesCallDurationLowThreshold = _AcPMSipAttributesCallDurationLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 2),
    _AcPMSipAttributesCallDurationLowThreshold_Type()
)
acPMSipAttributesCallDurationLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesCallDurationLowThreshold.setStatus("current")


class _AcPMSipAttributesTrunkGroupUtilizationHighThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesTrunkGroupUtilizationHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2016),
    )


_AcPMSipAttributesTrunkGroupUtilizationHighThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesTrunkGroupUtilizationHighThreshold_Object = MibScalar
acPMSipAttributesTrunkGroupUtilizationHighThreshold = _AcPMSipAttributesTrunkGroupUtilizationHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 3),
    _AcPMSipAttributesTrunkGroupUtilizationHighThreshold_Type()
)
acPMSipAttributesTrunkGroupUtilizationHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesTrunkGroupUtilizationHighThreshold.setStatus("current")


class _AcPMSipAttributesTrunkGroupUtilizationLowThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesTrunkGroupUtilizationLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2016),
    )


_AcPMSipAttributesTrunkGroupUtilizationLowThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesTrunkGroupUtilizationLowThreshold_Object = MibScalar
acPMSipAttributesTrunkGroupUtilizationLowThreshold = _AcPMSipAttributesTrunkGroupUtilizationLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 4),
    _AcPMSipAttributesTrunkGroupUtilizationLowThreshold_Type()
)
acPMSipAttributesTrunkGroupUtilizationLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesTrunkGroupUtilizationLowThreshold.setStatus("current")


class _AcPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold_Object = MibScalar
acPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold = _AcPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 5),
    _AcPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold_Type()
)
acPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold.setStatus("current")


class _AcPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold_Object = MibScalar
acPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold = _AcPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 6),
    _AcPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold_Type()
)
acPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold.setStatus("current")


class _AcPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold_Object = MibScalar
acPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold = _AcPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 7),
    _AcPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold_Type()
)
acPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold.setStatus("current")


class _AcPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold_Object = MibScalar
acPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold = _AcPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 8),
    _AcPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold_Type()
)
acPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold.setStatus("current")


class _AcPMSipAttributesIPGroupINVITEDialogsHighThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesIPGroupINVITEDialogsHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSipAttributesIPGroupINVITEDialogsHighThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesIPGroupINVITEDialogsHighThreshold_Object = MibScalar
acPMSipAttributesIPGroupINVITEDialogsHighThreshold = _AcPMSipAttributesIPGroupINVITEDialogsHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 25),
    _AcPMSipAttributesIPGroupINVITEDialogsHighThreshold_Type()
)
acPMSipAttributesIPGroupINVITEDialogsHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesIPGroupINVITEDialogsHighThreshold.setStatus("current")


class _AcPMSipAttributesIPGroupINVITEDialogsLowThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesIPGroupINVITEDialogsLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSipAttributesIPGroupINVITEDialogsLowThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesIPGroupINVITEDialogsLowThreshold_Object = MibScalar
acPMSipAttributesIPGroupINVITEDialogsLowThreshold = _AcPMSipAttributesIPGroupINVITEDialogsLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 26),
    _AcPMSipAttributesIPGroupINVITEDialogsLowThreshold_Type()
)
acPMSipAttributesIPGroupINVITEDialogsLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesIPGroupINVITEDialogsLowThreshold.setStatus("current")


class _AcPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold_Object = MibScalar
acPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold = _AcPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 33),
    _AcPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold_Type()
)
acPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold.setStatus("current")


class _AcPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold_Type(Unsigned32):
    """Custom type acPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold_Type.__name__ = "Unsigned32"
_AcPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold_Object = MibScalar
acPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold = _AcPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 34, 34),
    _AcPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold_Type()
)
acPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold.setStatus("current")
_AcPMMediaRealmAttributes_ObjectIdentity = ObjectIdentity
acPMMediaRealmAttributes = _AcPMMediaRealmAttributes_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35)
)


class _AcPMMediaRealmAttributesMediaRealmBytesTxHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmBytesTxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmBytesTxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmBytesTxHighThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmBytesTxHighThreshold = _AcPMMediaRealmAttributesMediaRealmBytesTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 1),
    _AcPMMediaRealmAttributesMediaRealmBytesTxHighThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmBytesTxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmBytesTxHighThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmBytesTxLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmBytesTxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmBytesTxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmBytesTxLowThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmBytesTxLowThreshold = _AcPMMediaRealmAttributesMediaRealmBytesTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 2),
    _AcPMMediaRealmAttributesMediaRealmBytesTxLowThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmBytesTxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmBytesTxLowThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmBytesRxHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmBytesRxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmBytesRxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmBytesRxHighThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmBytesRxHighThreshold = _AcPMMediaRealmAttributesMediaRealmBytesRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 3),
    _AcPMMediaRealmAttributesMediaRealmBytesRxHighThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmBytesRxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmBytesRxHighThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmBytesRxLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmBytesRxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmBytesRxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmBytesRxLowThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmBytesRxLowThreshold = _AcPMMediaRealmAttributesMediaRealmBytesRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 4),
    _AcPMMediaRealmAttributesMediaRealmBytesRxLowThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmBytesRxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmBytesRxLowThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold = _AcPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 5),
    _AcPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold = _AcPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 6),
    _AcPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold = _AcPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 7),
    _AcPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold = _AcPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 8),
    _AcPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold.setStatus("current")


class _AcPMMediaRealmAttributesVERealmPacketDelayHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesVERealmPacketDelayHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesVERealmPacketDelayHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesVERealmPacketDelayHighThreshold_Object = MibScalar
acPMMediaRealmAttributesVERealmPacketDelayHighThreshold = _AcPMMediaRealmAttributesVERealmPacketDelayHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 9),
    _AcPMMediaRealmAttributesVERealmPacketDelayHighThreshold_Type()
)
acPMMediaRealmAttributesVERealmPacketDelayHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesVERealmPacketDelayHighThreshold.setStatus("current")


class _AcPMMediaRealmAttributesVERealmPacketDelayLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesVERealmPacketDelayLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesVERealmPacketDelayLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesVERealmPacketDelayLowThreshold_Object = MibScalar
acPMMediaRealmAttributesVERealmPacketDelayLowThreshold = _AcPMMediaRealmAttributesVERealmPacketDelayLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 10),
    _AcPMMediaRealmAttributesVERealmPacketDelayLowThreshold_Type()
)
acPMMediaRealmAttributesVERealmPacketDelayLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesVERealmPacketDelayLowThreshold.setStatus("current")


class _AcPMMediaRealmAttributesVERealmPacketJitterHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesVERealmPacketJitterHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesVERealmPacketJitterHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesVERealmPacketJitterHighThreshold_Object = MibScalar
acPMMediaRealmAttributesVERealmPacketJitterHighThreshold = _AcPMMediaRealmAttributesVERealmPacketJitterHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 11),
    _AcPMMediaRealmAttributesVERealmPacketJitterHighThreshold_Type()
)
acPMMediaRealmAttributesVERealmPacketJitterHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesVERealmPacketJitterHighThreshold.setStatus("current")


class _AcPMMediaRealmAttributesVERealmPacketJitterLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesVERealmPacketJitterLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesVERealmPacketJitterLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesVERealmPacketJitterLowThreshold_Object = MibScalar
acPMMediaRealmAttributesVERealmPacketJitterLowThreshold = _AcPMMediaRealmAttributesVERealmPacketJitterLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 12),
    _AcPMMediaRealmAttributesVERealmPacketJitterLowThreshold_Type()
)
acPMMediaRealmAttributesVERealmPacketJitterLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesVERealmPacketJitterLowThreshold.setStatus("current")


class _AcPMMediaRealmAttributesRealmMOSHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesRealmMOSHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesRealmMOSHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesRealmMOSHighThreshold_Object = MibScalar
acPMMediaRealmAttributesRealmMOSHighThreshold = _AcPMMediaRealmAttributesRealmMOSHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 13),
    _AcPMMediaRealmAttributesRealmMOSHighThreshold_Type()
)
acPMMediaRealmAttributesRealmMOSHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesRealmMOSHighThreshold.setStatus("current")


class _AcPMMediaRealmAttributesRealmMOSLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesRealmMOSLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesRealmMOSLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesRealmMOSLowThreshold_Object = MibScalar
acPMMediaRealmAttributesRealmMOSLowThreshold = _AcPMMediaRealmAttributesRealmMOSLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 14),
    _AcPMMediaRealmAttributesRealmMOSLowThreshold_Type()
)
acPMMediaRealmAttributesRealmMOSLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesRealmMOSLowThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmBwRxHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmBwRxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmBwRxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmBwRxHighThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmBwRxHighThreshold = _AcPMMediaRealmAttributesMediaRealmBwRxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 15),
    _AcPMMediaRealmAttributesMediaRealmBwRxHighThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmBwRxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmBwRxHighThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmBwRxLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmBwRxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmBwRxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmBwRxLowThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmBwRxLowThreshold = _AcPMMediaRealmAttributesMediaRealmBwRxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 16),
    _AcPMMediaRealmAttributesMediaRealmBwRxLowThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmBwRxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmBwRxLowThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmBwTxHighThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmBwTxHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmBwTxHighThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmBwTxHighThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmBwTxHighThreshold = _AcPMMediaRealmAttributesMediaRealmBwTxHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 17),
    _AcPMMediaRealmAttributesMediaRealmBwTxHighThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmBwTxHighThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmBwTxHighThreshold.setStatus("current")


class _AcPMMediaRealmAttributesMediaRealmBwTxLowThreshold_Type(Unsigned32):
    """Custom type acPMMediaRealmAttributesMediaRealmBwTxLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMMediaRealmAttributesMediaRealmBwTxLowThreshold_Type.__name__ = "Unsigned32"
_AcPMMediaRealmAttributesMediaRealmBwTxLowThreshold_Object = MibScalar
acPMMediaRealmAttributesMediaRealmBwTxLowThreshold = _AcPMMediaRealmAttributesMediaRealmBwTxLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 1, 35, 18),
    _AcPMMediaRealmAttributesMediaRealmBwTxLowThreshold_Type()
)
acPMMediaRealmAttributesMediaRealmBwTxLowThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    acPMMediaRealmAttributesMediaRealmBwTxLowThreshold.setStatus("current")
_AcPMControlData_ObjectIdentity = ObjectIdentity
acPMControlData = _AcPMControlData_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2)
)


class _AcPMControlDataAcPMControlTimeFromStartOfInterval_Type(Unsigned32):
    """Custom type acPMControlDataAcPMControlTimeFromStartOfInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMControlDataAcPMControlTimeFromStartOfInterval_Type.__name__ = "Unsigned32"
_AcPMControlDataAcPMControlTimeFromStartOfInterval_Object = MibScalar
acPMControlDataAcPMControlTimeFromStartOfInterval = _AcPMControlDataAcPMControlTimeFromStartOfInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 1),
    _AcPMControlDataAcPMControlTimeFromStartOfInterval_Type()
)
acPMControlDataAcPMControlTimeFromStartOfInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMControlDataAcPMControlTimeFromStartOfInterval.setStatus("current")
_AcPMCPConnection_ObjectIdentity = ObjectIdentity
acPMCPConnection = _AcPMCPConnection_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31)
)
_AcPMCPConnectionLifetimeTable_Object = MibTable
acPMCPConnectionLifetimeTable = _AcPMCPConnectionLifetimeTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1)
)
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeTable.setStatus("current")
_AcPMCPConnectionLifetimeEntry_Object = MibTableRow
acPMCPConnectionLifetimeEntry = _AcPMCPConnectionLifetimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1)
)
acPMCPConnectionLifetimeEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMCPConnectionLifetimeInterval"),
)
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeEntry.setStatus("current")


class _AcPMCPConnectionLifetimeInterval_Type(Unsigned32):
    """Custom type acPMCPConnectionLifetimeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4),
    )


_AcPMCPConnectionLifetimeInterval_Type.__name__ = "Unsigned32"
_AcPMCPConnectionLifetimeInterval_Object = MibTableColumn
acPMCPConnectionLifetimeInterval = _AcPMCPConnectionLifetimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 1),
    _AcPMCPConnectionLifetimeInterval_Type()
)
acPMCPConnectionLifetimeInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeInterval.setStatus("current")
_AcPMCPConnectionLifetimeVal_Type = Gauge32
_AcPMCPConnectionLifetimeVal_Object = MibTableColumn
acPMCPConnectionLifetimeVal = _AcPMCPConnectionLifetimeVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 2),
    _AcPMCPConnectionLifetimeVal_Type()
)
acPMCPConnectionLifetimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeVal.setStatus("current")


class _AcPMCPConnectionLifetimeAverage_Type(Integer32):
    """Custom type acPMCPConnectionLifetimeAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPConnectionLifetimeAverage_Type.__name__ = "Integer32"
_AcPMCPConnectionLifetimeAverage_Object = MibTableColumn
acPMCPConnectionLifetimeAverage = _AcPMCPConnectionLifetimeAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 3),
    _AcPMCPConnectionLifetimeAverage_Type()
)
acPMCPConnectionLifetimeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeAverage.setStatus("current")


class _AcPMCPConnectionLifetimeMax_Type(Integer32):
    """Custom type acPMCPConnectionLifetimeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPConnectionLifetimeMax_Type.__name__ = "Integer32"
_AcPMCPConnectionLifetimeMax_Object = MibTableColumn
acPMCPConnectionLifetimeMax = _AcPMCPConnectionLifetimeMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 4),
    _AcPMCPConnectionLifetimeMax_Type()
)
acPMCPConnectionLifetimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeMax.setStatus("current")


class _AcPMCPConnectionLifetimeMin_Type(Integer32):
    """Custom type acPMCPConnectionLifetimeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPConnectionLifetimeMin_Type.__name__ = "Integer32"
_AcPMCPConnectionLifetimeMin_Object = MibTableColumn
acPMCPConnectionLifetimeMin = _AcPMCPConnectionLifetimeMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 5),
    _AcPMCPConnectionLifetimeMin_Type()
)
acPMCPConnectionLifetimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeMin.setStatus("current")
_AcPMCPConnectionLifetimeVolume_Type = Counter32
_AcPMCPConnectionLifetimeVolume_Object = MibTableColumn
acPMCPConnectionLifetimeVolume = _AcPMCPConnectionLifetimeVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 6),
    _AcPMCPConnectionLifetimeVolume_Type()
)
acPMCPConnectionLifetimeVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeVolume.setStatus("current")


class _AcPMCPConnectionLifetimeTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMCPConnectionLifetimeTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCPConnectionLifetimeTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMCPConnectionLifetimeTimeBelowLowThreshold_Object = MibTableColumn
acPMCPConnectionLifetimeTimeBelowLowThreshold = _AcPMCPConnectionLifetimeTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 7),
    _AcPMCPConnectionLifetimeTimeBelowLowThreshold_Type()
)
acPMCPConnectionLifetimeTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeTimeBelowLowThreshold.setStatus("current")


class _AcPMCPConnectionLifetimeTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMCPConnectionLifetimeTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCPConnectionLifetimeTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMCPConnectionLifetimeTimeBetweenThresholds_Object = MibTableColumn
acPMCPConnectionLifetimeTimeBetweenThresholds = _AcPMCPConnectionLifetimeTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 8),
    _AcPMCPConnectionLifetimeTimeBetweenThresholds_Type()
)
acPMCPConnectionLifetimeTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeTimeBetweenThresholds.setStatus("current")


class _AcPMCPConnectionLifetimeTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMCPConnectionLifetimeTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCPConnectionLifetimeTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMCPConnectionLifetimeTimeAboveHighThreshold_Object = MibTableColumn
acPMCPConnectionLifetimeTimeAboveHighThreshold = _AcPMCPConnectionLifetimeTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 9),
    _AcPMCPConnectionLifetimeTimeAboveHighThreshold_Type()
)
acPMCPConnectionLifetimeTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeTimeAboveHighThreshold.setStatus("current")


class _AcPMCPConnectionLifetimeFullDayAverage_Type(Integer32):
    """Custom type acPMCPConnectionLifetimeFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPConnectionLifetimeFullDayAverage_Type.__name__ = "Integer32"
_AcPMCPConnectionLifetimeFullDayAverage_Object = MibTableColumn
acPMCPConnectionLifetimeFullDayAverage = _AcPMCPConnectionLifetimeFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 10),
    _AcPMCPConnectionLifetimeFullDayAverage_Type()
)
acPMCPConnectionLifetimeFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeFullDayAverage.setStatus("current")


class _AcPMCPConnectionLifetimeTotal_Type(Integer32):
    """Custom type acPMCPConnectionLifetimeTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPConnectionLifetimeTotal_Type.__name__ = "Integer32"
_AcPMCPConnectionLifetimeTotal_Object = MibTableColumn
acPMCPConnectionLifetimeTotal = _AcPMCPConnectionLifetimeTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 1, 1, 11),
    _AcPMCPConnectionLifetimeTotal_Type()
)
acPMCPConnectionLifetimeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionLifetimeTotal.setStatus("current")
_AcPMCPConnectionStateTable_Object = MibTable
acPMCPConnectionStateTable = _AcPMCPConnectionStateTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 2)
)
if mibBuilder.loadTexts:
    acPMCPConnectionStateTable.setStatus("current")
_AcPMCPConnectionStateEntry_Object = MibTableRow
acPMCPConnectionStateEntry = _AcPMCPConnectionStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 2, 1)
)
acPMCPConnectionStateEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMCPConnectionStateInterval"),
)
if mibBuilder.loadTexts:
    acPMCPConnectionStateEntry.setStatus("current")


class _AcPMCPConnectionStateInterval_Type(Unsigned32):
    """Custom type acPMCPConnectionStateInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCPConnectionStateInterval_Type.__name__ = "Unsigned32"
_AcPMCPConnectionStateInterval_Object = MibTableColumn
acPMCPConnectionStateInterval = _AcPMCPConnectionStateInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 2, 1, 1),
    _AcPMCPConnectionStateInterval_Type()
)
acPMCPConnectionStateInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPConnectionStateInterval.setStatus("current")
_AcPMCPConnectionStateChanges_Type = Gauge32
_AcPMCPConnectionStateChanges_Object = MibTableColumn
acPMCPConnectionStateChanges = _AcPMCPConnectionStateChanges_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 2, 1, 2),
    _AcPMCPConnectionStateChanges_Type()
)
acPMCPConnectionStateChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionStateChanges.setStatus("current")


class _AcPMCPConnectionStateActiveTime_Type(Integer32):
    """Custom type acPMCPConnectionStateActiveTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMCPConnectionStateActiveTime_Type.__name__ = "Integer32"
_AcPMCPConnectionStateActiveTime_Object = MibTableColumn
acPMCPConnectionStateActiveTime = _AcPMCPConnectionStateActiveTime_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 2, 1, 3),
    _AcPMCPConnectionStateActiveTime_Type()
)
acPMCPConnectionStateActiveTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPConnectionStateActiveTime.setStatus("current")
_AcPMCPCommandCounterTable_Object = MibTable
acPMCPCommandCounterTable = _AcPMCPCommandCounterTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 3)
)
if mibBuilder.loadTexts:
    acPMCPCommandCounterTable.setStatus("current")
_AcPMCPCommandCounterEntry_Object = MibTableRow
acPMCPCommandCounterEntry = _AcPMCPCommandCounterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 3, 1)
)
acPMCPCommandCounterEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMCPCommandCounterDirection"),
    (0, "AC-PM-Control-MIB", "acPMCPCommandCounterInterval"),
)
if mibBuilder.loadTexts:
    acPMCPCommandCounterEntry.setStatus("current")


class _AcPMCPCommandCounterDirection_Type(Integer32):
    """Custom type acPMCPCommandCounterDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tx", 0),
          ("rx", 1))
    )


_AcPMCPCommandCounterDirection_Type.__name__ = "Integer32"
_AcPMCPCommandCounterDirection_Object = MibTableColumn
acPMCPCommandCounterDirection = _AcPMCPCommandCounterDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 3, 1, 1),
    _AcPMCPCommandCounterDirection_Type()
)
acPMCPCommandCounterDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCommandCounterDirection.setStatus("current")


class _AcPMCPCommandCounterInterval_Type(Unsigned32):
    """Custom type acPMCPCommandCounterInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCPCommandCounterInterval_Type.__name__ = "Unsigned32"
_AcPMCPCommandCounterInterval_Object = MibTableColumn
acPMCPCommandCounterInterval = _AcPMCPCommandCounterInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 3, 1, 2),
    _AcPMCPCommandCounterInterval_Type()
)
acPMCPCommandCounterInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCommandCounterInterval.setStatus("current")
_AcPMCPCommandCounterVal_Type = Counter32
_AcPMCPCommandCounterVal_Object = MibTableColumn
acPMCPCommandCounterVal = _AcPMCPCommandCounterVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 3, 1, 3),
    _AcPMCPCommandCounterVal_Type()
)
acPMCPCommandCounterVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCommandCounterVal.setStatus("current")


class _AcPMCPCommandCounterTotal_Type(Integer32):
    """Custom type acPMCPCommandCounterTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPCommandCounterTotal_Type.__name__ = "Integer32"
_AcPMCPCommandCounterTotal_Object = MibTableColumn
acPMCPCommandCounterTotal = _AcPMCPCommandCounterTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 3, 1, 4),
    _AcPMCPCommandCounterTotal_Type()
)
acPMCPCommandCounterTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCommandCounterTotal.setStatus("current")
_AcPMCPRetransmissionCountTable_Object = MibTable
acPMCPRetransmissionCountTable = _AcPMCPRetransmissionCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 4)
)
if mibBuilder.loadTexts:
    acPMCPRetransmissionCountTable.setStatus("current")
_AcPMCPRetransmissionCountEntry_Object = MibTableRow
acPMCPRetransmissionCountEntry = _AcPMCPRetransmissionCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 4, 1)
)
acPMCPRetransmissionCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMCPRetransmissionCountDirection"),
    (0, "AC-PM-Control-MIB", "acPMCPRetransmissionCountInterval"),
)
if mibBuilder.loadTexts:
    acPMCPRetransmissionCountEntry.setStatus("current")


class _AcPMCPRetransmissionCountDirection_Type(Integer32):
    """Custom type acPMCPRetransmissionCountDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tx", 0),
          ("rx", 1))
    )


_AcPMCPRetransmissionCountDirection_Type.__name__ = "Integer32"
_AcPMCPRetransmissionCountDirection_Object = MibTableColumn
acPMCPRetransmissionCountDirection = _AcPMCPRetransmissionCountDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 4, 1, 1),
    _AcPMCPRetransmissionCountDirection_Type()
)
acPMCPRetransmissionCountDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPRetransmissionCountDirection.setStatus("current")


class _AcPMCPRetransmissionCountInterval_Type(Unsigned32):
    """Custom type acPMCPRetransmissionCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCPRetransmissionCountInterval_Type.__name__ = "Unsigned32"
_AcPMCPRetransmissionCountInterval_Object = MibTableColumn
acPMCPRetransmissionCountInterval = _AcPMCPRetransmissionCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 4, 1, 2),
    _AcPMCPRetransmissionCountInterval_Type()
)
acPMCPRetransmissionCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPRetransmissionCountInterval.setStatus("current")
_AcPMCPRetransmissionCountVal_Type = Gauge32
_AcPMCPRetransmissionCountVal_Object = MibTableColumn
acPMCPRetransmissionCountVal = _AcPMCPRetransmissionCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 4, 1, 3),
    _AcPMCPRetransmissionCountVal_Type()
)
acPMCPRetransmissionCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPRetransmissionCountVal.setStatus("current")


class _AcPMCPRetransmissionCountTotal_Type(Integer32):
    """Custom type acPMCPRetransmissionCountTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPRetransmissionCountTotal_Type.__name__ = "Integer32"
_AcPMCPRetransmissionCountTotal_Object = MibTableColumn
acPMCPRetransmissionCountTotal = _AcPMCPRetransmissionCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 4, 1, 4),
    _AcPMCPRetransmissionCountTotal_Type()
)
acPMCPRetransmissionCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPRetransmissionCountTotal.setStatus("current")
_AcPMActiveContextCountTable_Object = MibTable
acPMActiveContextCountTable = _AcPMActiveContextCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5)
)
if mibBuilder.loadTexts:
    acPMActiveContextCountTable.setStatus("current")
_AcPMActiveContextCountEntry_Object = MibTableRow
acPMActiveContextCountEntry = _AcPMActiveContextCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1)
)
acPMActiveContextCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMActiveContextCountInterval"),
)
if mibBuilder.loadTexts:
    acPMActiveContextCountEntry.setStatus("current")


class _AcPMActiveContextCountInterval_Type(Unsigned32):
    """Custom type acPMActiveContextCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMActiveContextCountInterval_Type.__name__ = "Unsigned32"
_AcPMActiveContextCountInterval_Object = MibTableColumn
acPMActiveContextCountInterval = _AcPMActiveContextCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 1),
    _AcPMActiveContextCountInterval_Type()
)
acPMActiveContextCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMActiveContextCountInterval.setStatus("current")
_AcPMActiveContextCountVal_Type = Gauge32
_AcPMActiveContextCountVal_Object = MibTableColumn
acPMActiveContextCountVal = _AcPMActiveContextCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 2),
    _AcPMActiveContextCountVal_Type()
)
acPMActiveContextCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMActiveContextCountVal.setStatus("current")


class _AcPMActiveContextCountAverage_Type(Integer32):
    """Custom type acPMActiveContextCountAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMActiveContextCountAverage_Type.__name__ = "Integer32"
_AcPMActiveContextCountAverage_Object = MibTableColumn
acPMActiveContextCountAverage = _AcPMActiveContextCountAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 3),
    _AcPMActiveContextCountAverage_Type()
)
acPMActiveContextCountAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMActiveContextCountAverage.setStatus("current")


class _AcPMActiveContextCountMax_Type(Integer32):
    """Custom type acPMActiveContextCountMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMActiveContextCountMax_Type.__name__ = "Integer32"
_AcPMActiveContextCountMax_Object = MibTableColumn
acPMActiveContextCountMax = _AcPMActiveContextCountMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 4),
    _AcPMActiveContextCountMax_Type()
)
acPMActiveContextCountMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMActiveContextCountMax.setStatus("current")


class _AcPMActiveContextCountMin_Type(Integer32):
    """Custom type acPMActiveContextCountMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMActiveContextCountMin_Type.__name__ = "Integer32"
_AcPMActiveContextCountMin_Object = MibTableColumn
acPMActiveContextCountMin = _AcPMActiveContextCountMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 5),
    _AcPMActiveContextCountMin_Type()
)
acPMActiveContextCountMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMActiveContextCountMin.setStatus("current")
_AcPMActiveContextCountVolume_Type = Counter32
_AcPMActiveContextCountVolume_Object = MibTableColumn
acPMActiveContextCountVolume = _AcPMActiveContextCountVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 6),
    _AcPMActiveContextCountVolume_Type()
)
acPMActiveContextCountVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMActiveContextCountVolume.setStatus("current")


class _AcPMActiveContextCountTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMActiveContextCountTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMActiveContextCountTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMActiveContextCountTimeBelowLowThreshold_Object = MibTableColumn
acPMActiveContextCountTimeBelowLowThreshold = _AcPMActiveContextCountTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 7),
    _AcPMActiveContextCountTimeBelowLowThreshold_Type()
)
acPMActiveContextCountTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMActiveContextCountTimeBelowLowThreshold.setStatus("current")


class _AcPMActiveContextCountTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMActiveContextCountTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMActiveContextCountTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMActiveContextCountTimeBetweenThresholds_Object = MibTableColumn
acPMActiveContextCountTimeBetweenThresholds = _AcPMActiveContextCountTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 8),
    _AcPMActiveContextCountTimeBetweenThresholds_Type()
)
acPMActiveContextCountTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMActiveContextCountTimeBetweenThresholds.setStatus("current")


class _AcPMActiveContextCountTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMActiveContextCountTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMActiveContextCountTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMActiveContextCountTimeAboveHighThreshold_Object = MibTableColumn
acPMActiveContextCountTimeAboveHighThreshold = _AcPMActiveContextCountTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 9),
    _AcPMActiveContextCountTimeAboveHighThreshold_Type()
)
acPMActiveContextCountTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMActiveContextCountTimeAboveHighThreshold.setStatus("current")


class _AcPMActiveContextCountFullDayAverage_Type(Integer32):
    """Custom type acPMActiveContextCountFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMActiveContextCountFullDayAverage_Type.__name__ = "Integer32"
_AcPMActiveContextCountFullDayAverage_Object = MibTableColumn
acPMActiveContextCountFullDayAverage = _AcPMActiveContextCountFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 10),
    _AcPMActiveContextCountFullDayAverage_Type()
)
acPMActiveContextCountFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMActiveContextCountFullDayAverage.setStatus("current")


class _AcPMActiveContextCountTotal_Type(Integer32):
    """Custom type acPMActiveContextCountTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMActiveContextCountTotal_Type.__name__ = "Integer32"
_AcPMActiveContextCountTotal_Object = MibTableColumn
acPMActiveContextCountTotal = _AcPMActiveContextCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 5, 1, 11),
    _AcPMActiveContextCountTotal_Type()
)
acPMActiveContextCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMActiveContextCountTotal.setStatus("current")
_AcPMCPCommandSuccessCountTable_Object = MibTable
acPMCPCommandSuccessCountTable = _AcPMCPCommandSuccessCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 6)
)
if mibBuilder.loadTexts:
    acPMCPCommandSuccessCountTable.setStatus("obsolete")
_AcPMCPCommandSuccessCountEntry_Object = MibTableRow
acPMCPCommandSuccessCountEntry = _AcPMCPCommandSuccessCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 6, 1)
)
acPMCPCommandSuccessCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMCPCommandSuccessCountCommandType"),
    (0, "AC-PM-Control-MIB", "acPMCPCommandSuccessCountInterval"),
)
if mibBuilder.loadTexts:
    acPMCPCommandSuccessCountEntry.setStatus("obsolete")


class _AcPMCPCommandSuccessCountCommandType_Type(Integer32):
    """Custom type acPMCPCommandSuccessCountCommandType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("move", 1),
          ("modify", 2),
          ("subtract", 3),
          ("sc", 4),
          ("auditValue", 5),
          ("auditCapabilities", 6),
          ("notify", 7))
    )


_AcPMCPCommandSuccessCountCommandType_Type.__name__ = "Integer32"
_AcPMCPCommandSuccessCountCommandType_Object = MibTableColumn
acPMCPCommandSuccessCountCommandType = _AcPMCPCommandSuccessCountCommandType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 6, 1, 1),
    _AcPMCPCommandSuccessCountCommandType_Type()
)
acPMCPCommandSuccessCountCommandType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCommandSuccessCountCommandType.setStatus("obsolete")


class _AcPMCPCommandSuccessCountInterval_Type(Unsigned32):
    """Custom type acPMCPCommandSuccessCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCPCommandSuccessCountInterval_Type.__name__ = "Unsigned32"
_AcPMCPCommandSuccessCountInterval_Object = MibTableColumn
acPMCPCommandSuccessCountInterval = _AcPMCPCommandSuccessCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 6, 1, 2),
    _AcPMCPCommandSuccessCountInterval_Type()
)
acPMCPCommandSuccessCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCommandSuccessCountInterval.setStatus("obsolete")
_AcPMCPCommandSuccessCountVal_Type = Gauge32
_AcPMCPCommandSuccessCountVal_Object = MibTableColumn
acPMCPCommandSuccessCountVal = _AcPMCPCommandSuccessCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 6, 1, 3),
    _AcPMCPCommandSuccessCountVal_Type()
)
acPMCPCommandSuccessCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCommandSuccessCountVal.setStatus("obsolete")


class _AcPMCPCommandSuccessCountTotal_Type(Integer32):
    """Custom type acPMCPCommandSuccessCountTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPCommandSuccessCountTotal_Type.__name__ = "Integer32"
_AcPMCPCommandSuccessCountTotal_Object = MibTableColumn
acPMCPCommandSuccessCountTotal = _AcPMCPCommandSuccessCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 6, 1, 4),
    _AcPMCPCommandSuccessCountTotal_Type()
)
acPMCPCommandSuccessCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCommandSuccessCountTotal.setStatus("obsolete")
_AcPMCPCommandFailureCountTable_Object = MibTable
acPMCPCommandFailureCountTable = _AcPMCPCommandFailureCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 7)
)
if mibBuilder.loadTexts:
    acPMCPCommandFailureCountTable.setStatus("obsolete")
_AcPMCPCommandFailureCountEntry_Object = MibTableRow
acPMCPCommandFailureCountEntry = _AcPMCPCommandFailureCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 7, 1)
)
acPMCPCommandFailureCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMCPCommandFailureCountCommandType"),
    (0, "AC-PM-Control-MIB", "acPMCPCommandFailureCountInterval"),
)
if mibBuilder.loadTexts:
    acPMCPCommandFailureCountEntry.setStatus("obsolete")


class _AcPMCPCommandFailureCountCommandType_Type(Integer32):
    """Custom type acPMCPCommandFailureCountCommandType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("move", 1),
          ("modify", 2),
          ("subtract", 3),
          ("sc", 4),
          ("auditValue", 5),
          ("auditCapabilities", 6),
          ("notify", 7))
    )


_AcPMCPCommandFailureCountCommandType_Type.__name__ = "Integer32"
_AcPMCPCommandFailureCountCommandType_Object = MibTableColumn
acPMCPCommandFailureCountCommandType = _AcPMCPCommandFailureCountCommandType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 7, 1, 1),
    _AcPMCPCommandFailureCountCommandType_Type()
)
acPMCPCommandFailureCountCommandType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCommandFailureCountCommandType.setStatus("obsolete")


class _AcPMCPCommandFailureCountInterval_Type(Unsigned32):
    """Custom type acPMCPCommandFailureCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCPCommandFailureCountInterval_Type.__name__ = "Unsigned32"
_AcPMCPCommandFailureCountInterval_Object = MibTableColumn
acPMCPCommandFailureCountInterval = _AcPMCPCommandFailureCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 7, 1, 2),
    _AcPMCPCommandFailureCountInterval_Type()
)
acPMCPCommandFailureCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCommandFailureCountInterval.setStatus("obsolete")
_AcPMCPCommandFailureCountVal_Type = Gauge32
_AcPMCPCommandFailureCountVal_Object = MibTableColumn
acPMCPCommandFailureCountVal = _AcPMCPCommandFailureCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 7, 1, 3),
    _AcPMCPCommandFailureCountVal_Type()
)
acPMCPCommandFailureCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCommandFailureCountVal.setStatus("obsolete")


class _AcPMCPCommandFailureCountTotal_Type(Integer32):
    """Custom type acPMCPCommandFailureCountTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPCommandFailureCountTotal_Type.__name__ = "Integer32"
_AcPMCPCommandFailureCountTotal_Object = MibTableColumn
acPMCPCommandFailureCountTotal = _AcPMCPCommandFailureCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 7, 1, 4),
    _AcPMCPCommandFailureCountTotal_Type()
)
acPMCPCommandFailureCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCommandFailureCountTotal.setStatus("current")
_AcPMcpCmdProcessTimeTable_Object = MibTable
acPMcpCmdProcessTimeTable = _AcPMcpCmdProcessTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8)
)
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeTable.setStatus("current")
_AcPMcpCmdProcessTimeEntry_Object = MibTableRow
acPMcpCmdProcessTimeEntry = _AcPMcpCmdProcessTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1)
)
acPMcpCmdProcessTimeEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMcpCmdProcessTimeInterval"),
)
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeEntry.setStatus("current")


class _AcPMcpCmdProcessTimeInterval_Type(Unsigned32):
    """Custom type acPMcpCmdProcessTimeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMcpCmdProcessTimeInterval_Type.__name__ = "Unsigned32"
_AcPMcpCmdProcessTimeInterval_Object = MibTableColumn
acPMcpCmdProcessTimeInterval = _AcPMcpCmdProcessTimeInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 1),
    _AcPMcpCmdProcessTimeInterval_Type()
)
acPMcpCmdProcessTimeInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeInterval.setStatus("current")
_AcPMcpCmdProcessTimeVal_Type = Gauge32
_AcPMcpCmdProcessTimeVal_Object = MibTableColumn
acPMcpCmdProcessTimeVal = _AcPMcpCmdProcessTimeVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 2),
    _AcPMcpCmdProcessTimeVal_Type()
)
acPMcpCmdProcessTimeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeVal.setStatus("current")


class _AcPMcpCmdProcessTimeAverage_Type(Integer32):
    """Custom type acPMcpCmdProcessTimeAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMcpCmdProcessTimeAverage_Type.__name__ = "Integer32"
_AcPMcpCmdProcessTimeAverage_Object = MibTableColumn
acPMcpCmdProcessTimeAverage = _AcPMcpCmdProcessTimeAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 3),
    _AcPMcpCmdProcessTimeAverage_Type()
)
acPMcpCmdProcessTimeAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeAverage.setStatus("current")


class _AcPMcpCmdProcessTimeMax_Type(Integer32):
    """Custom type acPMcpCmdProcessTimeMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMcpCmdProcessTimeMax_Type.__name__ = "Integer32"
_AcPMcpCmdProcessTimeMax_Object = MibTableColumn
acPMcpCmdProcessTimeMax = _AcPMcpCmdProcessTimeMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 4),
    _AcPMcpCmdProcessTimeMax_Type()
)
acPMcpCmdProcessTimeMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeMax.setStatus("current")


class _AcPMcpCmdProcessTimeMin_Type(Integer32):
    """Custom type acPMcpCmdProcessTimeMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMcpCmdProcessTimeMin_Type.__name__ = "Integer32"
_AcPMcpCmdProcessTimeMin_Object = MibTableColumn
acPMcpCmdProcessTimeMin = _AcPMcpCmdProcessTimeMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 5),
    _AcPMcpCmdProcessTimeMin_Type()
)
acPMcpCmdProcessTimeMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeMin.setStatus("current")
_AcPMcpCmdProcessTimeVolume_Type = Counter32
_AcPMcpCmdProcessTimeVolume_Object = MibTableColumn
acPMcpCmdProcessTimeVolume = _AcPMcpCmdProcessTimeVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 6),
    _AcPMcpCmdProcessTimeVolume_Type()
)
acPMcpCmdProcessTimeVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeVolume.setStatus("current")


class _AcPMcpCmdProcessTimeTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMcpCmdProcessTimeTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMcpCmdProcessTimeTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMcpCmdProcessTimeTimeBelowLowThreshold_Object = MibTableColumn
acPMcpCmdProcessTimeTimeBelowLowThreshold = _AcPMcpCmdProcessTimeTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 7),
    _AcPMcpCmdProcessTimeTimeBelowLowThreshold_Type()
)
acPMcpCmdProcessTimeTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeTimeBelowLowThreshold.setStatus("current")


class _AcPMcpCmdProcessTimeTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMcpCmdProcessTimeTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMcpCmdProcessTimeTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMcpCmdProcessTimeTimeBetweenThresholds_Object = MibTableColumn
acPMcpCmdProcessTimeTimeBetweenThresholds = _AcPMcpCmdProcessTimeTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 8),
    _AcPMcpCmdProcessTimeTimeBetweenThresholds_Type()
)
acPMcpCmdProcessTimeTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeTimeBetweenThresholds.setStatus("current")


class _AcPMcpCmdProcessTimeTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMcpCmdProcessTimeTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMcpCmdProcessTimeTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMcpCmdProcessTimeTimeAboveHighThreshold_Object = MibTableColumn
acPMcpCmdProcessTimeTimeAboveHighThreshold = _AcPMcpCmdProcessTimeTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 9),
    _AcPMcpCmdProcessTimeTimeAboveHighThreshold_Type()
)
acPMcpCmdProcessTimeTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeTimeAboveHighThreshold.setStatus("current")


class _AcPMcpCmdProcessTimeFullDayAverage_Type(Integer32):
    """Custom type acPMcpCmdProcessTimeFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMcpCmdProcessTimeFullDayAverage_Type.__name__ = "Integer32"
_AcPMcpCmdProcessTimeFullDayAverage_Object = MibTableColumn
acPMcpCmdProcessTimeFullDayAverage = _AcPMcpCmdProcessTimeFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 10),
    _AcPMcpCmdProcessTimeFullDayAverage_Type()
)
acPMcpCmdProcessTimeFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeFullDayAverage.setStatus("current")


class _AcPMcpCmdProcessTimeTotal_Type(Integer32):
    """Custom type acPMcpCmdProcessTimeTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMcpCmdProcessTimeTotal_Type.__name__ = "Integer32"
_AcPMcpCmdProcessTimeTotal_Object = MibTableColumn
acPMcpCmdProcessTimeTotal = _AcPMcpCmdProcessTimeTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 8, 1, 11),
    _AcPMcpCmdProcessTimeTotal_Type()
)
acPMcpCmdProcessTimeTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpCmdProcessTimeTotal.setStatus("current")
_AcPMcpTransactionProcessTimerTable_Object = MibTable
acPMcpTransactionProcessTimerTable = _AcPMcpTransactionProcessTimerTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9)
)
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerTable.setStatus("current")
_AcPMcpTransactionProcessTimerEntry_Object = MibTableRow
acPMcpTransactionProcessTimerEntry = _AcPMcpTransactionProcessTimerEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1)
)
acPMcpTransactionProcessTimerEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMcpTransactionProcessTimerInterval"),
)
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerEntry.setStatus("current")


class _AcPMcpTransactionProcessTimerInterval_Type(Unsigned32):
    """Custom type acPMcpTransactionProcessTimerInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMcpTransactionProcessTimerInterval_Type.__name__ = "Unsigned32"
_AcPMcpTransactionProcessTimerInterval_Object = MibTableColumn
acPMcpTransactionProcessTimerInterval = _AcPMcpTransactionProcessTimerInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 1),
    _AcPMcpTransactionProcessTimerInterval_Type()
)
acPMcpTransactionProcessTimerInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerInterval.setStatus("current")
_AcPMcpTransactionProcessTimerVal_Type = Gauge32
_AcPMcpTransactionProcessTimerVal_Object = MibTableColumn
acPMcpTransactionProcessTimerVal = _AcPMcpTransactionProcessTimerVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 2),
    _AcPMcpTransactionProcessTimerVal_Type()
)
acPMcpTransactionProcessTimerVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerVal.setStatus("current")


class _AcPMcpTransactionProcessTimerAverage_Type(Integer32):
    """Custom type acPMcpTransactionProcessTimerAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMcpTransactionProcessTimerAverage_Type.__name__ = "Integer32"
_AcPMcpTransactionProcessTimerAverage_Object = MibTableColumn
acPMcpTransactionProcessTimerAverage = _AcPMcpTransactionProcessTimerAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 3),
    _AcPMcpTransactionProcessTimerAverage_Type()
)
acPMcpTransactionProcessTimerAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerAverage.setStatus("current")


class _AcPMcpTransactionProcessTimerMax_Type(Integer32):
    """Custom type acPMcpTransactionProcessTimerMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMcpTransactionProcessTimerMax_Type.__name__ = "Integer32"
_AcPMcpTransactionProcessTimerMax_Object = MibTableColumn
acPMcpTransactionProcessTimerMax = _AcPMcpTransactionProcessTimerMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 4),
    _AcPMcpTransactionProcessTimerMax_Type()
)
acPMcpTransactionProcessTimerMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerMax.setStatus("current")


class _AcPMcpTransactionProcessTimerMin_Type(Integer32):
    """Custom type acPMcpTransactionProcessTimerMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMcpTransactionProcessTimerMin_Type.__name__ = "Integer32"
_AcPMcpTransactionProcessTimerMin_Object = MibTableColumn
acPMcpTransactionProcessTimerMin = _AcPMcpTransactionProcessTimerMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 5),
    _AcPMcpTransactionProcessTimerMin_Type()
)
acPMcpTransactionProcessTimerMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerMin.setStatus("current")
_AcPMcpTransactionProcessTimerVolume_Type = Counter32
_AcPMcpTransactionProcessTimerVolume_Object = MibTableColumn
acPMcpTransactionProcessTimerVolume = _AcPMcpTransactionProcessTimerVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 6),
    _AcPMcpTransactionProcessTimerVolume_Type()
)
acPMcpTransactionProcessTimerVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerVolume.setStatus("current")


class _AcPMcpTransactionProcessTimerTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMcpTransactionProcessTimerTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMcpTransactionProcessTimerTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMcpTransactionProcessTimerTimeBelowLowThreshold_Object = MibTableColumn
acPMcpTransactionProcessTimerTimeBelowLowThreshold = _AcPMcpTransactionProcessTimerTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 7),
    _AcPMcpTransactionProcessTimerTimeBelowLowThreshold_Type()
)
acPMcpTransactionProcessTimerTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerTimeBelowLowThreshold.setStatus("current")


class _AcPMcpTransactionProcessTimerTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMcpTransactionProcessTimerTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMcpTransactionProcessTimerTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMcpTransactionProcessTimerTimeBetweenThresholds_Object = MibTableColumn
acPMcpTransactionProcessTimerTimeBetweenThresholds = _AcPMcpTransactionProcessTimerTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 8),
    _AcPMcpTransactionProcessTimerTimeBetweenThresholds_Type()
)
acPMcpTransactionProcessTimerTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerTimeBetweenThresholds.setStatus("current")


class _AcPMcpTransactionProcessTimerTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMcpTransactionProcessTimerTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMcpTransactionProcessTimerTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMcpTransactionProcessTimerTimeAboveHighThreshold_Object = MibTableColumn
acPMcpTransactionProcessTimerTimeAboveHighThreshold = _AcPMcpTransactionProcessTimerTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 9),
    _AcPMcpTransactionProcessTimerTimeAboveHighThreshold_Type()
)
acPMcpTransactionProcessTimerTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerTimeAboveHighThreshold.setStatus("current")


class _AcPMcpTransactionProcessTimerFullDayAverage_Type(Integer32):
    """Custom type acPMcpTransactionProcessTimerFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMcpTransactionProcessTimerFullDayAverage_Type.__name__ = "Integer32"
_AcPMcpTransactionProcessTimerFullDayAverage_Object = MibTableColumn
acPMcpTransactionProcessTimerFullDayAverage = _AcPMcpTransactionProcessTimerFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 10),
    _AcPMcpTransactionProcessTimerFullDayAverage_Type()
)
acPMcpTransactionProcessTimerFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerFullDayAverage.setStatus("current")


class _AcPMcpTransactionProcessTimerTotal_Type(Integer32):
    """Custom type acPMcpTransactionProcessTimerTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMcpTransactionProcessTimerTotal_Type.__name__ = "Integer32"
_AcPMcpTransactionProcessTimerTotal_Object = MibTableColumn
acPMcpTransactionProcessTimerTotal = _AcPMcpTransactionProcessTimerTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 9, 1, 11),
    _AcPMcpTransactionProcessTimerTotal_Type()
)
acPMcpTransactionProcessTimerTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpTransactionProcessTimerTotal.setStatus("current")
_AcPMCPCallAttemptsPerSecTable_Object = MibTable
acPMCPCallAttemptsPerSecTable = _AcPMCPCallAttemptsPerSecTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 10)
)
if mibBuilder.loadTexts:
    acPMCPCallAttemptsPerSecTable.setStatus("current")
_AcPMCPCallAttemptsPerSecEntry_Object = MibTableRow
acPMCPCallAttemptsPerSecEntry = _AcPMCPCallAttemptsPerSecEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 10, 1)
)
acPMCPCallAttemptsPerSecEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMCPCallAttemptsPerSecInterval"),
)
if mibBuilder.loadTexts:
    acPMCPCallAttemptsPerSecEntry.setStatus("current")


class _AcPMCPCallAttemptsPerSecInterval_Type(Unsigned32):
    """Custom type acPMCPCallAttemptsPerSecInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCPCallAttemptsPerSecInterval_Type.__name__ = "Unsigned32"
_AcPMCPCallAttemptsPerSecInterval_Object = MibTableColumn
acPMCPCallAttemptsPerSecInterval = _AcPMCPCallAttemptsPerSecInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 10, 1, 1),
    _AcPMCPCallAttemptsPerSecInterval_Type()
)
acPMCPCallAttemptsPerSecInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCallAttemptsPerSecInterval.setStatus("current")
_AcPMCPCallAttemptsPerSecVal_Type = Gauge32
_AcPMCPCallAttemptsPerSecVal_Object = MibTableColumn
acPMCPCallAttemptsPerSecVal = _AcPMCPCallAttemptsPerSecVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 10, 1, 2),
    _AcPMCPCallAttemptsPerSecVal_Type()
)
acPMCPCallAttemptsPerSecVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCallAttemptsPerSecVal.setStatus("current")


class _AcPMCPCallAttemptsPerSecAverage_Type(Integer32):
    """Custom type acPMCPCallAttemptsPerSecAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPCallAttemptsPerSecAverage_Type.__name__ = "Integer32"
_AcPMCPCallAttemptsPerSecAverage_Object = MibTableColumn
acPMCPCallAttemptsPerSecAverage = _AcPMCPCallAttemptsPerSecAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 10, 1, 3),
    _AcPMCPCallAttemptsPerSecAverage_Type()
)
acPMCPCallAttemptsPerSecAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCallAttemptsPerSecAverage.setStatus("current")


class _AcPMCPCallAttemptsPerSecMax_Type(Integer32):
    """Custom type acPMCPCallAttemptsPerSecMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPCallAttemptsPerSecMax_Type.__name__ = "Integer32"
_AcPMCPCallAttemptsPerSecMax_Object = MibTableColumn
acPMCPCallAttemptsPerSecMax = _AcPMCPCallAttemptsPerSecMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 10, 1, 4),
    _AcPMCPCallAttemptsPerSecMax_Type()
)
acPMCPCallAttemptsPerSecMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCallAttemptsPerSecMax.setStatus("current")


class _AcPMCPCallAttemptsPerSecMin_Type(Integer32):
    """Custom type acPMCPCallAttemptsPerSecMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPCallAttemptsPerSecMin_Type.__name__ = "Integer32"
_AcPMCPCallAttemptsPerSecMin_Object = MibTableColumn
acPMCPCallAttemptsPerSecMin = _AcPMCPCallAttemptsPerSecMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 10, 1, 5),
    _AcPMCPCallAttemptsPerSecMin_Type()
)
acPMCPCallAttemptsPerSecMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCallAttemptsPerSecMin.setStatus("current")
_AcPMCPCallAttemptsPerSecVolume_Type = Counter32
_AcPMCPCallAttemptsPerSecVolume_Object = MibTableColumn
acPMCPCallAttemptsPerSecVolume = _AcPMCPCallAttemptsPerSecVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 31, 10, 1, 6),
    _AcPMCPCallAttemptsPerSecVolume_Type()
)
acPMCPCallAttemptsPerSecVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCallAttemptsPerSecVolume.setStatus("current")
_AcPMMegaco_ObjectIdentity = ObjectIdentity
acPMMegaco = _AcPMMegaco_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41)
)
_AcPMMegacoServiceChangeCountTable_Object = MibTable
acPMMegacoServiceChangeCountTable = _AcPMMegacoServiceChangeCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 1)
)
if mibBuilder.loadTexts:
    acPMMegacoServiceChangeCountTable.setStatus("current")
_AcPMMegacoServiceChangeCountEntry_Object = MibTableRow
acPMMegacoServiceChangeCountEntry = _AcPMMegacoServiceChangeCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 1, 1)
)
acPMMegacoServiceChangeCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMegacoServiceChangeCountMethod"),
    (0, "AC-PM-Control-MIB", "acPMMegacoServiceChangeCountInterval"),
)
if mibBuilder.loadTexts:
    acPMMegacoServiceChangeCountEntry.setStatus("current")


class _AcPMMegacoServiceChangeCountMethod_Type(Integer32):
    """Custom type acPMMegacoServiceChangeCountMethod based on Integer32"""
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
        *(("failOver", 0),
          ("forced", 1),
          ("graceful", 2),
          ("restart", 3),
          ("disconnected", 4),
          ("handoff", 5))
    )


_AcPMMegacoServiceChangeCountMethod_Type.__name__ = "Integer32"
_AcPMMegacoServiceChangeCountMethod_Object = MibTableColumn
acPMMegacoServiceChangeCountMethod = _AcPMMegacoServiceChangeCountMethod_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 1, 1, 1),
    _AcPMMegacoServiceChangeCountMethod_Type()
)
acPMMegacoServiceChangeCountMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMegacoServiceChangeCountMethod.setStatus("current")


class _AcPMMegacoServiceChangeCountInterval_Type(Unsigned32):
    """Custom type acPMMegacoServiceChangeCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMegacoServiceChangeCountInterval_Type.__name__ = "Unsigned32"
_AcPMMegacoServiceChangeCountInterval_Object = MibTableColumn
acPMMegacoServiceChangeCountInterval = _AcPMMegacoServiceChangeCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 1, 1, 2),
    _AcPMMegacoServiceChangeCountInterval_Type()
)
acPMMegacoServiceChangeCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMegacoServiceChangeCountInterval.setStatus("current")
_AcPMMegacoServiceChangeCountVal_Type = Gauge32
_AcPMMegacoServiceChangeCountVal_Object = MibTableColumn
acPMMegacoServiceChangeCountVal = _AcPMMegacoServiceChangeCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 1, 1, 3),
    _AcPMMegacoServiceChangeCountVal_Type()
)
acPMMegacoServiceChangeCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMegacoServiceChangeCountVal.setStatus("current")
_AcPMCPCmdSuccessCountTable_Object = MibTable
acPMCPCmdSuccessCountTable = _AcPMCPCmdSuccessCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 2)
)
if mibBuilder.loadTexts:
    acPMCPCmdSuccessCountTable.setStatus("current")
_AcPMCPCmdSuccessCountEntry_Object = MibTableRow
acPMCPCmdSuccessCountEntry = _AcPMCPCmdSuccessCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 2, 1)
)
acPMCPCmdSuccessCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMCPCmdSuccessCountCommandType"),
    (0, "AC-PM-Control-MIB", "acPMCPCmdSuccessCountInterval"),
)
if mibBuilder.loadTexts:
    acPMCPCmdSuccessCountEntry.setStatus("current")


class _AcPMCPCmdSuccessCountCommandType_Type(Integer32):
    """Custom type acPMCPCmdSuccessCountCommandType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("move", 1),
          ("modify", 2),
          ("subtract", 3),
          ("sc", 4),
          ("auditValue", 5),
          ("auditCapabilities", 6),
          ("notify", 7))
    )


_AcPMCPCmdSuccessCountCommandType_Type.__name__ = "Integer32"
_AcPMCPCmdSuccessCountCommandType_Object = MibTableColumn
acPMCPCmdSuccessCountCommandType = _AcPMCPCmdSuccessCountCommandType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 2, 1, 1),
    _AcPMCPCmdSuccessCountCommandType_Type()
)
acPMCPCmdSuccessCountCommandType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCmdSuccessCountCommandType.setStatus("current")


class _AcPMCPCmdSuccessCountInterval_Type(Unsigned32):
    """Custom type acPMCPCmdSuccessCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCPCmdSuccessCountInterval_Type.__name__ = "Unsigned32"
_AcPMCPCmdSuccessCountInterval_Object = MibTableColumn
acPMCPCmdSuccessCountInterval = _AcPMCPCmdSuccessCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 2, 1, 2),
    _AcPMCPCmdSuccessCountInterval_Type()
)
acPMCPCmdSuccessCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCmdSuccessCountInterval.setStatus("current")
_AcPMCPCmdSuccessCountVal_Type = Gauge32
_AcPMCPCmdSuccessCountVal_Object = MibTableColumn
acPMCPCmdSuccessCountVal = _AcPMCPCmdSuccessCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 2, 1, 3),
    _AcPMCPCmdSuccessCountVal_Type()
)
acPMCPCmdSuccessCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCmdSuccessCountVal.setStatus("current")


class _AcPMCPCmdSuccessCountTotal_Type(Integer32):
    """Custom type acPMCPCmdSuccessCountTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPCmdSuccessCountTotal_Type.__name__ = "Integer32"
_AcPMCPCmdSuccessCountTotal_Object = MibTableColumn
acPMCPCmdSuccessCountTotal = _AcPMCPCmdSuccessCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 2, 1, 4),
    _AcPMCPCmdSuccessCountTotal_Type()
)
acPMCPCmdSuccessCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCmdSuccessCountTotal.setStatus("current")
_AcPMCPCmdFailureCountTable_Object = MibTable
acPMCPCmdFailureCountTable = _AcPMCPCmdFailureCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 3)
)
if mibBuilder.loadTexts:
    acPMCPCmdFailureCountTable.setStatus("current")
_AcPMCPCmdFailureCountEntry_Object = MibTableRow
acPMCPCmdFailureCountEntry = _AcPMCPCmdFailureCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 3, 1)
)
acPMCPCmdFailureCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMCPCmdFailureCountCommandType"),
    (0, "AC-PM-Control-MIB", "acPMCPCmdFailureCountInterval"),
)
if mibBuilder.loadTexts:
    acPMCPCmdFailureCountEntry.setStatus("current")


class _AcPMCPCmdFailureCountCommandType_Type(Integer32):
    """Custom type acPMCPCmdFailureCountCommandType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("move", 1),
          ("modify", 2),
          ("subtract", 3),
          ("sc", 4),
          ("auditValue", 5),
          ("auditCapabilities", 6),
          ("notify", 7))
    )


_AcPMCPCmdFailureCountCommandType_Type.__name__ = "Integer32"
_AcPMCPCmdFailureCountCommandType_Object = MibTableColumn
acPMCPCmdFailureCountCommandType = _AcPMCPCmdFailureCountCommandType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 3, 1, 1),
    _AcPMCPCmdFailureCountCommandType_Type()
)
acPMCPCmdFailureCountCommandType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCmdFailureCountCommandType.setStatus("current")


class _AcPMCPCmdFailureCountInterval_Type(Unsigned32):
    """Custom type acPMCPCmdFailureCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMCPCmdFailureCountInterval_Type.__name__ = "Unsigned32"
_AcPMCPCmdFailureCountInterval_Object = MibTableColumn
acPMCPCmdFailureCountInterval = _AcPMCPCmdFailureCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 3, 1, 2),
    _AcPMCPCmdFailureCountInterval_Type()
)
acPMCPCmdFailureCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMCPCmdFailureCountInterval.setStatus("current")
_AcPMCPCmdFailureCountVal_Type = Gauge32
_AcPMCPCmdFailureCountVal_Object = MibTableColumn
acPMCPCmdFailureCountVal = _AcPMCPCmdFailureCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 3, 1, 3),
    _AcPMCPCmdFailureCountVal_Type()
)
acPMCPCmdFailureCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCmdFailureCountVal.setStatus("current")


class _AcPMCPCmdFailureCountTotal_Type(Integer32):
    """Custom type acPMCPCmdFailureCountTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMCPCmdFailureCountTotal_Type.__name__ = "Integer32"
_AcPMCPCmdFailureCountTotal_Object = MibTableColumn
acPMCPCmdFailureCountTotal = _AcPMCPCmdFailureCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 3, 1, 4),
    _AcPMCPCmdFailureCountTotal_Type()
)
acPMCPCmdFailureCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMCPCmdFailureCountTotal.setStatus("current")
_AcPMcpUMTSHandOverCountTable_Object = MibTable
acPMcpUMTSHandOverCountTable = _AcPMcpUMTSHandOverCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 4)
)
if mibBuilder.loadTexts:
    acPMcpUMTSHandOverCountTable.setStatus("current")
_AcPMcpUMTSHandOverCountEntry_Object = MibTableRow
acPMcpUMTSHandOverCountEntry = _AcPMcpUMTSHandOverCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 4, 1)
)
acPMcpUMTSHandOverCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMcpUMTSHandOverCountInterval"),
)
if mibBuilder.loadTexts:
    acPMcpUMTSHandOverCountEntry.setStatus("current")


class _AcPMcpUMTSHandOverCountInterval_Type(Unsigned32):
    """Custom type acPMcpUMTSHandOverCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMcpUMTSHandOverCountInterval_Type.__name__ = "Unsigned32"
_AcPMcpUMTSHandOverCountInterval_Object = MibTableColumn
acPMcpUMTSHandOverCountInterval = _AcPMcpUMTSHandOverCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 4, 1, 1),
    _AcPMcpUMTSHandOverCountInterval_Type()
)
acPMcpUMTSHandOverCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMcpUMTSHandOverCountInterval.setStatus("current")
_AcPMcpUMTSHandOverCountVal_Type = Gauge32
_AcPMcpUMTSHandOverCountVal_Object = MibTableColumn
acPMcpUMTSHandOverCountVal = _AcPMcpUMTSHandOverCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 4, 1, 2),
    _AcPMcpUMTSHandOverCountVal_Type()
)
acPMcpUMTSHandOverCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMcpUMTSHandOverCountVal.setStatus("current")
_AcPMMegacoAddFailureCountTable_Object = MibTable
acPMMegacoAddFailureCountTable = _AcPMMegacoAddFailureCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 5)
)
if mibBuilder.loadTexts:
    acPMMegacoAddFailureCountTable.setStatus("current")
_AcPMMegacoAddFailureCountEntry_Object = MibTableRow
acPMMegacoAddFailureCountEntry = _AcPMMegacoAddFailureCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 5, 1)
)
acPMMegacoAddFailureCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMegacoAddFailureCountInterval"),
)
if mibBuilder.loadTexts:
    acPMMegacoAddFailureCountEntry.setStatus("current")


class _AcPMMegacoAddFailureCountInterval_Type(Unsigned32):
    """Custom type acPMMegacoAddFailureCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMegacoAddFailureCountInterval_Type.__name__ = "Unsigned32"
_AcPMMegacoAddFailureCountInterval_Object = MibTableColumn
acPMMegacoAddFailureCountInterval = _AcPMMegacoAddFailureCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 5, 1, 1),
    _AcPMMegacoAddFailureCountInterval_Type()
)
acPMMegacoAddFailureCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMegacoAddFailureCountInterval.setStatus("current")
_AcPMMegacoAddFailureCountVal_Type = Gauge32
_AcPMMegacoAddFailureCountVal_Object = MibTableColumn
acPMMegacoAddFailureCountVal = _AcPMMegacoAddFailureCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 5, 1, 2),
    _AcPMMegacoAddFailureCountVal_Type()
)
acPMMegacoAddFailureCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMegacoAddFailureCountVal.setStatus("current")
_AcPMMegacoModifyFailureCountTable_Object = MibTable
acPMMegacoModifyFailureCountTable = _AcPMMegacoModifyFailureCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 6)
)
if mibBuilder.loadTexts:
    acPMMegacoModifyFailureCountTable.setStatus("current")
_AcPMMegacoModifyFailureCountEntry_Object = MibTableRow
acPMMegacoModifyFailureCountEntry = _AcPMMegacoModifyFailureCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 6, 1)
)
acPMMegacoModifyFailureCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMegacoModifyFailureCountInterval"),
)
if mibBuilder.loadTexts:
    acPMMegacoModifyFailureCountEntry.setStatus("current")


class _AcPMMegacoModifyFailureCountInterval_Type(Unsigned32):
    """Custom type acPMMegacoModifyFailureCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMegacoModifyFailureCountInterval_Type.__name__ = "Unsigned32"
_AcPMMegacoModifyFailureCountInterval_Object = MibTableColumn
acPMMegacoModifyFailureCountInterval = _AcPMMegacoModifyFailureCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 6, 1, 1),
    _AcPMMegacoModifyFailureCountInterval_Type()
)
acPMMegacoModifyFailureCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMegacoModifyFailureCountInterval.setStatus("current")
_AcPMMegacoModifyFailureCountVal_Type = Gauge32
_AcPMMegacoModifyFailureCountVal_Object = MibTableColumn
acPMMegacoModifyFailureCountVal = _AcPMMegacoModifyFailureCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 6, 1, 2),
    _AcPMMegacoModifyFailureCountVal_Type()
)
acPMMegacoModifyFailureCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMegacoModifyFailureCountVal.setStatus("current")
_AcPMMegacoSuccessfulAddWithLoopbackTable_Object = MibTable
acPMMegacoSuccessfulAddWithLoopbackTable = _AcPMMegacoSuccessfulAddWithLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 7)
)
if mibBuilder.loadTexts:
    acPMMegacoSuccessfulAddWithLoopbackTable.setStatus("current")
_AcPMMegacoSuccessfulAddWithLoopbackEntry_Object = MibTableRow
acPMMegacoSuccessfulAddWithLoopbackEntry = _AcPMMegacoSuccessfulAddWithLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 7, 1)
)
acPMMegacoSuccessfulAddWithLoopbackEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMegacoSuccessfulAddWithLoopbackInterval"),
)
if mibBuilder.loadTexts:
    acPMMegacoSuccessfulAddWithLoopbackEntry.setStatus("current")


class _AcPMMegacoSuccessfulAddWithLoopbackInterval_Type(Unsigned32):
    """Custom type acPMMegacoSuccessfulAddWithLoopbackInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMegacoSuccessfulAddWithLoopbackInterval_Type.__name__ = "Unsigned32"
_AcPMMegacoSuccessfulAddWithLoopbackInterval_Object = MibTableColumn
acPMMegacoSuccessfulAddWithLoopbackInterval = _AcPMMegacoSuccessfulAddWithLoopbackInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 7, 1, 1),
    _AcPMMegacoSuccessfulAddWithLoopbackInterval_Type()
)
acPMMegacoSuccessfulAddWithLoopbackInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMegacoSuccessfulAddWithLoopbackInterval.setStatus("current")
_AcPMMegacoSuccessfulAddWithLoopbackVal_Type = Gauge32
_AcPMMegacoSuccessfulAddWithLoopbackVal_Object = MibTableColumn
acPMMegacoSuccessfulAddWithLoopbackVal = _AcPMMegacoSuccessfulAddWithLoopbackVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 7, 1, 2),
    _AcPMMegacoSuccessfulAddWithLoopbackVal_Type()
)
acPMMegacoSuccessfulAddWithLoopbackVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMegacoSuccessfulAddWithLoopbackVal.setStatus("current")
_AcPMMegacoFailedAddWithLoopbackTable_Object = MibTable
acPMMegacoFailedAddWithLoopbackTable = _AcPMMegacoFailedAddWithLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 8)
)
if mibBuilder.loadTexts:
    acPMMegacoFailedAddWithLoopbackTable.setStatus("current")
_AcPMMegacoFailedAddWithLoopbackEntry_Object = MibTableRow
acPMMegacoFailedAddWithLoopbackEntry = _AcPMMegacoFailedAddWithLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 8, 1)
)
acPMMegacoFailedAddWithLoopbackEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMegacoFailedAddWithLoopbackInterval"),
)
if mibBuilder.loadTexts:
    acPMMegacoFailedAddWithLoopbackEntry.setStatus("current")


class _AcPMMegacoFailedAddWithLoopbackInterval_Type(Unsigned32):
    """Custom type acPMMegacoFailedAddWithLoopbackInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMegacoFailedAddWithLoopbackInterval_Type.__name__ = "Unsigned32"
_AcPMMegacoFailedAddWithLoopbackInterval_Object = MibTableColumn
acPMMegacoFailedAddWithLoopbackInterval = _AcPMMegacoFailedAddWithLoopbackInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 8, 1, 1),
    _AcPMMegacoFailedAddWithLoopbackInterval_Type()
)
acPMMegacoFailedAddWithLoopbackInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMegacoFailedAddWithLoopbackInterval.setStatus("current")
_AcPMMegacoFailedAddWithLoopbackVal_Type = Gauge32
_AcPMMegacoFailedAddWithLoopbackVal_Object = MibTableColumn
acPMMegacoFailedAddWithLoopbackVal = _AcPMMegacoFailedAddWithLoopbackVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 8, 1, 2),
    _AcPMMegacoFailedAddWithLoopbackVal_Type()
)
acPMMegacoFailedAddWithLoopbackVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMegacoFailedAddWithLoopbackVal.setStatus("current")
_AcPMMegacoOutgoingCommandSuccessCountTable_Object = MibTable
acPMMegacoOutgoingCommandSuccessCountTable = _AcPMMegacoOutgoingCommandSuccessCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 9)
)
if mibBuilder.loadTexts:
    acPMMegacoOutgoingCommandSuccessCountTable.setStatus("current")
_AcPMMegacoOutgoingCommandSuccessCountEntry_Object = MibTableRow
acPMMegacoOutgoingCommandSuccessCountEntry = _AcPMMegacoOutgoingCommandSuccessCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 9, 1)
)
acPMMegacoOutgoingCommandSuccessCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMegacoOutgoingCommandSuccessCountInterval"),
)
if mibBuilder.loadTexts:
    acPMMegacoOutgoingCommandSuccessCountEntry.setStatus("current")


class _AcPMMegacoOutgoingCommandSuccessCountInterval_Type(Unsigned32):
    """Custom type acPMMegacoOutgoingCommandSuccessCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMegacoOutgoingCommandSuccessCountInterval_Type.__name__ = "Unsigned32"
_AcPMMegacoOutgoingCommandSuccessCountInterval_Object = MibTableColumn
acPMMegacoOutgoingCommandSuccessCountInterval = _AcPMMegacoOutgoingCommandSuccessCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 9, 1, 1),
    _AcPMMegacoOutgoingCommandSuccessCountInterval_Type()
)
acPMMegacoOutgoingCommandSuccessCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMegacoOutgoingCommandSuccessCountInterval.setStatus("current")
_AcPMMegacoOutgoingCommandSuccessCountVal_Type = Gauge32
_AcPMMegacoOutgoingCommandSuccessCountVal_Object = MibTableColumn
acPMMegacoOutgoingCommandSuccessCountVal = _AcPMMegacoOutgoingCommandSuccessCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 9, 1, 2),
    _AcPMMegacoOutgoingCommandSuccessCountVal_Type()
)
acPMMegacoOutgoingCommandSuccessCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMegacoOutgoingCommandSuccessCountVal.setStatus("current")
_AcPMMegacoOutgoingCommandFailureCountTable_Object = MibTable
acPMMegacoOutgoingCommandFailureCountTable = _AcPMMegacoOutgoingCommandFailureCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 10)
)
if mibBuilder.loadTexts:
    acPMMegacoOutgoingCommandFailureCountTable.setStatus("current")
_AcPMMegacoOutgoingCommandFailureCountEntry_Object = MibTableRow
acPMMegacoOutgoingCommandFailureCountEntry = _AcPMMegacoOutgoingCommandFailureCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 10, 1)
)
acPMMegacoOutgoingCommandFailureCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMegacoOutgoingCommandFailureCountInterval"),
)
if mibBuilder.loadTexts:
    acPMMegacoOutgoingCommandFailureCountEntry.setStatus("current")


class _AcPMMegacoOutgoingCommandFailureCountInterval_Type(Unsigned32):
    """Custom type acPMMegacoOutgoingCommandFailureCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMegacoOutgoingCommandFailureCountInterval_Type.__name__ = "Unsigned32"
_AcPMMegacoOutgoingCommandFailureCountInterval_Object = MibTableColumn
acPMMegacoOutgoingCommandFailureCountInterval = _AcPMMegacoOutgoingCommandFailureCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 10, 1, 1),
    _AcPMMegacoOutgoingCommandFailureCountInterval_Type()
)
acPMMegacoOutgoingCommandFailureCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMegacoOutgoingCommandFailureCountInterval.setStatus("current")
_AcPMMegacoOutgoingCommandFailureCountVal_Type = Gauge32
_AcPMMegacoOutgoingCommandFailureCountVal_Object = MibTableColumn
acPMMegacoOutgoingCommandFailureCountVal = _AcPMMegacoOutgoingCommandFailureCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 41, 10, 1, 2),
    _AcPMMegacoOutgoingCommandFailureCountVal_Type()
)
acPMMegacoOutgoingCommandFailureCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMegacoOutgoingCommandFailureCountVal.setStatus("current")
_AcPMMGCP_ObjectIdentity = ObjectIdentity
acPMMGCP = _AcPMMGCP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51)
)
_AcPMMGCPRsipReasonCountTable_Object = MibTable
acPMMGCPRsipReasonCountTable = _AcPMMGCPRsipReasonCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 1)
)
if mibBuilder.loadTexts:
    acPMMGCPRsipReasonCountTable.setStatus("current")
_AcPMMGCPRsipReasonCountEntry_Object = MibTableRow
acPMMGCPRsipReasonCountEntry = _AcPMMGCPRsipReasonCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 1, 1)
)
acPMMGCPRsipReasonCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPRsipReasonCountReasonCode"),
    (0, "AC-PM-Control-MIB", "acPMMGCPRsipReasonCountInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPRsipReasonCountEntry.setStatus("current")


class _AcPMMGCPRsipReasonCountReasonCode_Type(Integer32):
    """Custom type acPMMGCPRsipReasonCountReasonCode based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("restart", 0),
          ("forced", 1),
          ("disconnected", 2),
          ("keepAlive", 3),
          ("graceful", 4),
          ("cancelGraceful", 5),
          ("resetBoard", 6),
          ("nonVoice", 7))
    )


_AcPMMGCPRsipReasonCountReasonCode_Type.__name__ = "Integer32"
_AcPMMGCPRsipReasonCountReasonCode_Object = MibTableColumn
acPMMGCPRsipReasonCountReasonCode = _AcPMMGCPRsipReasonCountReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 1, 1, 1),
    _AcPMMGCPRsipReasonCountReasonCode_Type()
)
acPMMGCPRsipReasonCountReasonCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPRsipReasonCountReasonCode.setStatus("current")


class _AcPMMGCPRsipReasonCountInterval_Type(Unsigned32):
    """Custom type acPMMGCPRsipReasonCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPRsipReasonCountInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPRsipReasonCountInterval_Object = MibTableColumn
acPMMGCPRsipReasonCountInterval = _AcPMMGCPRsipReasonCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 1, 1, 2),
    _AcPMMGCPRsipReasonCountInterval_Type()
)
acPMMGCPRsipReasonCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPRsipReasonCountInterval.setStatus("current")
_AcPMMGCPRsipReasonCountVal_Type = Counter32
_AcPMMGCPRsipReasonCountVal_Object = MibTableColumn
acPMMGCPRsipReasonCountVal = _AcPMMGCPRsipReasonCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 1, 1, 3),
    _AcPMMGCPRsipReasonCountVal_Type()
)
acPMMGCPRsipReasonCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPRsipReasonCountVal.setStatus("current")
_AcPMMGCPGeneratedDLCXTable_Object = MibTable
acPMMGCPGeneratedDLCXTable = _AcPMMGCPGeneratedDLCXTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 2)
)
if mibBuilder.loadTexts:
    acPMMGCPGeneratedDLCXTable.setStatus("current")
_AcPMMGCPGeneratedDLCXEntry_Object = MibTableRow
acPMMGCPGeneratedDLCXEntry = _AcPMMGCPGeneratedDLCXEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 2, 1)
)
acPMMGCPGeneratedDLCXEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPGeneratedDLCXInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPGeneratedDLCXEntry.setStatus("current")


class _AcPMMGCPGeneratedDLCXInterval_Type(Unsigned32):
    """Custom type acPMMGCPGeneratedDLCXInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPGeneratedDLCXInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPGeneratedDLCXInterval_Object = MibTableColumn
acPMMGCPGeneratedDLCXInterval = _AcPMMGCPGeneratedDLCXInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 2, 1, 1),
    _AcPMMGCPGeneratedDLCXInterval_Type()
)
acPMMGCPGeneratedDLCXInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPGeneratedDLCXInterval.setStatus("current")
_AcPMMGCPGeneratedDLCXVal_Type = Counter32
_AcPMMGCPGeneratedDLCXVal_Object = MibTableColumn
acPMMGCPGeneratedDLCXVal = _AcPMMGCPGeneratedDLCXVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 2, 1, 2),
    _AcPMMGCPGeneratedDLCXVal_Type()
)
acPMMGCPGeneratedDLCXVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPGeneratedDLCXVal.setStatus("current")
_AcPMMGCPCommandSuccessCountTable_Object = MibTable
acPMMGCPCommandSuccessCountTable = _AcPMMGCPCommandSuccessCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 3)
)
if mibBuilder.loadTexts:
    acPMMGCPCommandSuccessCountTable.setStatus("current")
_AcPMMGCPCommandSuccessCountEntry_Object = MibTableRow
acPMMGCPCommandSuccessCountEntry = _AcPMMGCPCommandSuccessCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 3, 1)
)
acPMMGCPCommandSuccessCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPCommandSuccessCountCommandType"),
    (0, "AC-PM-Control-MIB", "acPMMGCPCommandSuccessCountInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPCommandSuccessCountEntry.setStatus("current")


class _AcPMMGCPCommandSuccessCountCommandType_Type(Integer32):
    """Custom type acPMMGCPCommandSuccessCountCommandType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("move", 1),
          ("modify", 2),
          ("subtract", 3),
          ("sc", 4),
          ("auditValue", 5),
          ("auditCapabilities", 6),
          ("notify", 7))
    )


_AcPMMGCPCommandSuccessCountCommandType_Type.__name__ = "Integer32"
_AcPMMGCPCommandSuccessCountCommandType_Object = MibTableColumn
acPMMGCPCommandSuccessCountCommandType = _AcPMMGCPCommandSuccessCountCommandType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 3, 1, 1),
    _AcPMMGCPCommandSuccessCountCommandType_Type()
)
acPMMGCPCommandSuccessCountCommandType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPCommandSuccessCountCommandType.setStatus("current")


class _AcPMMGCPCommandSuccessCountInterval_Type(Unsigned32):
    """Custom type acPMMGCPCommandSuccessCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPCommandSuccessCountInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPCommandSuccessCountInterval_Object = MibTableColumn
acPMMGCPCommandSuccessCountInterval = _AcPMMGCPCommandSuccessCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 3, 1, 2),
    _AcPMMGCPCommandSuccessCountInterval_Type()
)
acPMMGCPCommandSuccessCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPCommandSuccessCountInterval.setStatus("current")
_AcPMMGCPCommandSuccessCountVal_Type = Gauge32
_AcPMMGCPCommandSuccessCountVal_Object = MibTableColumn
acPMMGCPCommandSuccessCountVal = _AcPMMGCPCommandSuccessCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 3, 1, 3),
    _AcPMMGCPCommandSuccessCountVal_Type()
)
acPMMGCPCommandSuccessCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPCommandSuccessCountVal.setStatus("current")


class _AcPMMGCPCommandSuccessCountTotal_Type(Integer32):
    """Custom type acPMMGCPCommandSuccessCountTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMGCPCommandSuccessCountTotal_Type.__name__ = "Integer32"
_AcPMMGCPCommandSuccessCountTotal_Object = MibTableColumn
acPMMGCPCommandSuccessCountTotal = _AcPMMGCPCommandSuccessCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 3, 1, 4),
    _AcPMMGCPCommandSuccessCountTotal_Type()
)
acPMMGCPCommandSuccessCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPCommandSuccessCountTotal.setStatus("current")
_AcPMMGCPCommandFailureCountTable_Object = MibTable
acPMMGCPCommandFailureCountTable = _AcPMMGCPCommandFailureCountTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 4)
)
if mibBuilder.loadTexts:
    acPMMGCPCommandFailureCountTable.setStatus("current")
_AcPMMGCPCommandFailureCountEntry_Object = MibTableRow
acPMMGCPCommandFailureCountEntry = _AcPMMGCPCommandFailureCountEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 4, 1)
)
acPMMGCPCommandFailureCountEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPCommandFailureCountCommandType"),
    (0, "AC-PM-Control-MIB", "acPMMGCPCommandFailureCountInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPCommandFailureCountEntry.setStatus("current")


class _AcPMMGCPCommandFailureCountCommandType_Type(Integer32):
    """Custom type acPMMGCPCommandFailureCountCommandType based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("add", 0),
          ("move", 1),
          ("modify", 2),
          ("subtract", 3),
          ("sc", 4),
          ("auditValue", 5),
          ("auditCapabilities", 6),
          ("notify", 7))
    )


_AcPMMGCPCommandFailureCountCommandType_Type.__name__ = "Integer32"
_AcPMMGCPCommandFailureCountCommandType_Object = MibTableColumn
acPMMGCPCommandFailureCountCommandType = _AcPMMGCPCommandFailureCountCommandType_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 4, 1, 1),
    _AcPMMGCPCommandFailureCountCommandType_Type()
)
acPMMGCPCommandFailureCountCommandType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPCommandFailureCountCommandType.setStatus("current")


class _AcPMMGCPCommandFailureCountInterval_Type(Unsigned32):
    """Custom type acPMMGCPCommandFailureCountInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPCommandFailureCountInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPCommandFailureCountInterval_Object = MibTableColumn
acPMMGCPCommandFailureCountInterval = _AcPMMGCPCommandFailureCountInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 4, 1, 2),
    _AcPMMGCPCommandFailureCountInterval_Type()
)
acPMMGCPCommandFailureCountInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPCommandFailureCountInterval.setStatus("current")
_AcPMMGCPCommandFailureCountVal_Type = Gauge32
_AcPMMGCPCommandFailureCountVal_Object = MibTableColumn
acPMMGCPCommandFailureCountVal = _AcPMMGCPCommandFailureCountVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 4, 1, 3),
    _AcPMMGCPCommandFailureCountVal_Type()
)
acPMMGCPCommandFailureCountVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPCommandFailureCountVal.setStatus("current")


class _AcPMMGCPCommandFailureCountTotal_Type(Integer32):
    """Custom type acPMMGCPCommandFailureCountTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMMGCPCommandFailureCountTotal_Type.__name__ = "Integer32"
_AcPMMGCPCommandFailureCountTotal_Object = MibTableColumn
acPMMGCPCommandFailureCountTotal = _AcPMMGCPCommandFailureCountTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 4, 1, 4),
    _AcPMMGCPCommandFailureCountTotal_Type()
)
acPMMGCPCommandFailureCountTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPCommandFailureCountTotal.setStatus("current")
_AcPMMGCPLoopbackCRCXTable_Object = MibTable
acPMMGCPLoopbackCRCXTable = _AcPMMGCPLoopbackCRCXTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 5)
)
if mibBuilder.loadTexts:
    acPMMGCPLoopbackCRCXTable.setStatus("current")
_AcPMMGCPLoopbackCRCXEntry_Object = MibTableRow
acPMMGCPLoopbackCRCXEntry = _AcPMMGCPLoopbackCRCXEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 5, 1)
)
acPMMGCPLoopbackCRCXEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPLoopbackCRCXInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPLoopbackCRCXEntry.setStatus("current")


class _AcPMMGCPLoopbackCRCXInterval_Type(Unsigned32):
    """Custom type acPMMGCPLoopbackCRCXInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPLoopbackCRCXInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPLoopbackCRCXInterval_Object = MibTableColumn
acPMMGCPLoopbackCRCXInterval = _AcPMMGCPLoopbackCRCXInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 5, 1, 1),
    _AcPMMGCPLoopbackCRCXInterval_Type()
)
acPMMGCPLoopbackCRCXInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPLoopbackCRCXInterval.setStatus("current")
_AcPMMGCPLoopbackCRCXVal_Type = Counter32
_AcPMMGCPLoopbackCRCXVal_Object = MibTableColumn
acPMMGCPLoopbackCRCXVal = _AcPMMGCPLoopbackCRCXVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 5, 1, 2),
    _AcPMMGCPLoopbackCRCXVal_Type()
)
acPMMGCPLoopbackCRCXVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPLoopbackCRCXVal.setStatus("current")
_AcPMMGCPFailedLoopbackCRCXTable_Object = MibTable
acPMMGCPFailedLoopbackCRCXTable = _AcPMMGCPFailedLoopbackCRCXTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 6)
)
if mibBuilder.loadTexts:
    acPMMGCPFailedLoopbackCRCXTable.setStatus("current")
_AcPMMGCPFailedLoopbackCRCXEntry_Object = MibTableRow
acPMMGCPFailedLoopbackCRCXEntry = _AcPMMGCPFailedLoopbackCRCXEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 6, 1)
)
acPMMGCPFailedLoopbackCRCXEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPFailedLoopbackCRCXInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPFailedLoopbackCRCXEntry.setStatus("current")


class _AcPMMGCPFailedLoopbackCRCXInterval_Type(Unsigned32):
    """Custom type acPMMGCPFailedLoopbackCRCXInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPFailedLoopbackCRCXInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPFailedLoopbackCRCXInterval_Object = MibTableColumn
acPMMGCPFailedLoopbackCRCXInterval = _AcPMMGCPFailedLoopbackCRCXInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 6, 1, 1),
    _AcPMMGCPFailedLoopbackCRCXInterval_Type()
)
acPMMGCPFailedLoopbackCRCXInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPFailedLoopbackCRCXInterval.setStatus("current")
_AcPMMGCPFailedLoopbackCRCXVal_Type = Counter32
_AcPMMGCPFailedLoopbackCRCXVal_Object = MibTableColumn
acPMMGCPFailedLoopbackCRCXVal = _AcPMMGCPFailedLoopbackCRCXVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 6, 1, 2),
    _AcPMMGCPFailedLoopbackCRCXVal_Type()
)
acPMMGCPFailedLoopbackCRCXVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPFailedLoopbackCRCXVal.setStatus("current")
_AcPMMGCPGeneratedNTFYTable_Object = MibTable
acPMMGCPGeneratedNTFYTable = _AcPMMGCPGeneratedNTFYTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 7)
)
if mibBuilder.loadTexts:
    acPMMGCPGeneratedNTFYTable.setStatus("current")
_AcPMMGCPGeneratedNTFYEntry_Object = MibTableRow
acPMMGCPGeneratedNTFYEntry = _AcPMMGCPGeneratedNTFYEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 7, 1)
)
acPMMGCPGeneratedNTFYEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPGeneratedNTFYInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPGeneratedNTFYEntry.setStatus("current")


class _AcPMMGCPGeneratedNTFYInterval_Type(Unsigned32):
    """Custom type acPMMGCPGeneratedNTFYInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPGeneratedNTFYInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPGeneratedNTFYInterval_Object = MibTableColumn
acPMMGCPGeneratedNTFYInterval = _AcPMMGCPGeneratedNTFYInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 7, 1, 1),
    _AcPMMGCPGeneratedNTFYInterval_Type()
)
acPMMGCPGeneratedNTFYInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPGeneratedNTFYInterval.setStatus("current")
_AcPMMGCPGeneratedNTFYVal_Type = Counter32
_AcPMMGCPGeneratedNTFYVal_Object = MibTableColumn
acPMMGCPGeneratedNTFYVal = _AcPMMGCPGeneratedNTFYVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 7, 1, 2),
    _AcPMMGCPGeneratedNTFYVal_Type()
)
acPMMGCPGeneratedNTFYVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPGeneratedNTFYVal.setStatus("current")
_AcPMMGCPFailedNTFYResponsesTable_Object = MibTable
acPMMGCPFailedNTFYResponsesTable = _AcPMMGCPFailedNTFYResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 8)
)
if mibBuilder.loadTexts:
    acPMMGCPFailedNTFYResponsesTable.setStatus("current")
_AcPMMGCPFailedNTFYResponsesEntry_Object = MibTableRow
acPMMGCPFailedNTFYResponsesEntry = _AcPMMGCPFailedNTFYResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 8, 1)
)
acPMMGCPFailedNTFYResponsesEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPFailedNTFYResponsesInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPFailedNTFYResponsesEntry.setStatus("current")


class _AcPMMGCPFailedNTFYResponsesInterval_Type(Unsigned32):
    """Custom type acPMMGCPFailedNTFYResponsesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPFailedNTFYResponsesInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPFailedNTFYResponsesInterval_Object = MibTableColumn
acPMMGCPFailedNTFYResponsesInterval = _AcPMMGCPFailedNTFYResponsesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 8, 1, 1),
    _AcPMMGCPFailedNTFYResponsesInterval_Type()
)
acPMMGCPFailedNTFYResponsesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPFailedNTFYResponsesInterval.setStatus("current")
_AcPMMGCPFailedNTFYResponsesVal_Type = Counter32
_AcPMMGCPFailedNTFYResponsesVal_Object = MibTableColumn
acPMMGCPFailedNTFYResponsesVal = _AcPMMGCPFailedNTFYResponsesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 8, 1, 2),
    _AcPMMGCPFailedNTFYResponsesVal_Type()
)
acPMMGCPFailedNTFYResponsesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPFailedNTFYResponsesVal.setStatus("current")
_AcPMMGCPFailedRSIPResponsesTable_Object = MibTable
acPMMGCPFailedRSIPResponsesTable = _AcPMMGCPFailedRSIPResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 9)
)
if mibBuilder.loadTexts:
    acPMMGCPFailedRSIPResponsesTable.setStatus("current")
_AcPMMGCPFailedRSIPResponsesEntry_Object = MibTableRow
acPMMGCPFailedRSIPResponsesEntry = _AcPMMGCPFailedRSIPResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 9, 1)
)
acPMMGCPFailedRSIPResponsesEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPFailedRSIPResponsesInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPFailedRSIPResponsesEntry.setStatus("current")


class _AcPMMGCPFailedRSIPResponsesInterval_Type(Unsigned32):
    """Custom type acPMMGCPFailedRSIPResponsesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPFailedRSIPResponsesInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPFailedRSIPResponsesInterval_Object = MibTableColumn
acPMMGCPFailedRSIPResponsesInterval = _AcPMMGCPFailedRSIPResponsesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 9, 1, 1),
    _AcPMMGCPFailedRSIPResponsesInterval_Type()
)
acPMMGCPFailedRSIPResponsesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPFailedRSIPResponsesInterval.setStatus("current")
_AcPMMGCPFailedRSIPResponsesVal_Type = Counter32
_AcPMMGCPFailedRSIPResponsesVal_Object = MibTableColumn
acPMMGCPFailedRSIPResponsesVal = _AcPMMGCPFailedRSIPResponsesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 9, 1, 2),
    _AcPMMGCPFailedRSIPResponsesVal_Type()
)
acPMMGCPFailedRSIPResponsesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPFailedRSIPResponsesVal.setStatus("current")
_AcPMMGCPFailedCRCXResponsesTable_Object = MibTable
acPMMGCPFailedCRCXResponsesTable = _AcPMMGCPFailedCRCXResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 10)
)
if mibBuilder.loadTexts:
    acPMMGCPFailedCRCXResponsesTable.setStatus("current")
_AcPMMGCPFailedCRCXResponsesEntry_Object = MibTableRow
acPMMGCPFailedCRCXResponsesEntry = _AcPMMGCPFailedCRCXResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 10, 1)
)
acPMMGCPFailedCRCXResponsesEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPFailedCRCXResponsesReasonCode"),
    (0, "AC-PM-Control-MIB", "acPMMGCPFailedCRCXResponsesInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPFailedCRCXResponsesEntry.setStatus("current")


class _AcPMMGCPFailedCRCXResponsesReasonCode_Type(Integer32):
    """Custom type acPMMGCPFailedCRCXResponsesReasonCode based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("reasoncode-400", 0),
          ("reasoncode-401", 1),
          ("reasoncode-402", 2),
          ("reasoncode-403", 3),
          ("reasoncode-404", 4),
          ("reasoncode-405", 5),
          ("reasoncode-406", 6),
          ("reasoncode-407", 7),
          ("reasoncode-409", 8),
          ("reasoncode-410", 9),
          ("reasoncode-500", 10),
          ("reasoncode-501", 11),
          ("reasoncode-502", 12),
          ("reasoncode-503", 13),
          ("reasoncode-504", 14),
          ("reasoncode-505", 15),
          ("reasoncode-506", 16),
          ("reasoncode-507", 17),
          ("reasoncode-508", 18),
          ("reasoncode-509", 19),
          ("reasoncode-510", 20),
          ("reasoncode-511", 21),
          ("reasoncode-512", 22),
          ("reasoncode-513", 23),
          ("reasoncode-514", 24),
          ("reasoncode-515", 25),
          ("reasoncode-516", 26),
          ("reasoncode-517", 27),
          ("reasoncode-518", 28),
          ("reasoncode-519", 29),
          ("reasoncode-520", 30),
          ("reasoncode-521", 31),
          ("reasoncode-522", 32),
          ("reasoncode-523", 33),
          ("reasoncode-524", 34),
          ("reasoncode-525", 35),
          ("reasoncode-526", 36),
          ("reasoncode-527", 37),
          ("reasoncode-528", 38),
          ("reasoncode-529", 39),
          ("reasoncode-530", 40),
          ("reasoncode-531", 41),
          ("reasoncode-532", 42),
          ("reasoncode-533", 43),
          ("reasoncode-534", 44),
          ("reasoncode-535", 45),
          ("reasoncode-536", 46),
          ("reasoncode-537", 47),
          ("reasoncode-538", 48),
          ("reasoncode-539", 49),
          ("reasoncode-540", 50),
          ("reasoncode-541", 51))
    )


_AcPMMGCPFailedCRCXResponsesReasonCode_Type.__name__ = "Integer32"
_AcPMMGCPFailedCRCXResponsesReasonCode_Object = MibTableColumn
acPMMGCPFailedCRCXResponsesReasonCode = _AcPMMGCPFailedCRCXResponsesReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 10, 1, 1),
    _AcPMMGCPFailedCRCXResponsesReasonCode_Type()
)
acPMMGCPFailedCRCXResponsesReasonCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPFailedCRCXResponsesReasonCode.setStatus("current")


class _AcPMMGCPFailedCRCXResponsesInterval_Type(Unsigned32):
    """Custom type acPMMGCPFailedCRCXResponsesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPFailedCRCXResponsesInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPFailedCRCXResponsesInterval_Object = MibTableColumn
acPMMGCPFailedCRCXResponsesInterval = _AcPMMGCPFailedCRCXResponsesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 10, 1, 2),
    _AcPMMGCPFailedCRCXResponsesInterval_Type()
)
acPMMGCPFailedCRCXResponsesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPFailedCRCXResponsesInterval.setStatus("current")
_AcPMMGCPFailedCRCXResponsesVal_Type = Counter32
_AcPMMGCPFailedCRCXResponsesVal_Object = MibTableColumn
acPMMGCPFailedCRCXResponsesVal = _AcPMMGCPFailedCRCXResponsesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 10, 1, 3),
    _AcPMMGCPFailedCRCXResponsesVal_Type()
)
acPMMGCPFailedCRCXResponsesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPFailedCRCXResponsesVal.setStatus("current")
_AcPMMGCPFailedMDCXResponsesTable_Object = MibTable
acPMMGCPFailedMDCXResponsesTable = _AcPMMGCPFailedMDCXResponsesTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 11)
)
if mibBuilder.loadTexts:
    acPMMGCPFailedMDCXResponsesTable.setStatus("current")
_AcPMMGCPFailedMDCXResponsesEntry_Object = MibTableRow
acPMMGCPFailedMDCXResponsesEntry = _AcPMMGCPFailedMDCXResponsesEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 11, 1)
)
acPMMGCPFailedMDCXResponsesEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPFailedMDCXResponsesReasonCode"),
    (0, "AC-PM-Control-MIB", "acPMMGCPFailedMDCXResponsesInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPFailedMDCXResponsesEntry.setStatus("current")


class _AcPMMGCPFailedMDCXResponsesReasonCode_Type(Integer32):
    """Custom type acPMMGCPFailedMDCXResponsesReasonCode based on Integer32"""
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
              9,
              10,
              11,
              12,
              13,
              14,
              15,
              16,
              17,
              18,
              19,
              20,
              21,
              22,
              23,
              24,
              25,
              26,
              27,
              28,
              29,
              30,
              31,
              32,
              33,
              34,
              35,
              36,
              37,
              38,
              39,
              40,
              41,
              42,
              43,
              44,
              45,
              46,
              47,
              48,
              49,
              50,
              51)
        )
    )
    namedValues = NamedValues(
        *(("reasoncode-400", 0),
          ("reasoncode-401", 1),
          ("reasoncode-402", 2),
          ("reasoncode-403", 3),
          ("reasoncode-404", 4),
          ("reasoncode-405", 5),
          ("reasoncode-406", 6),
          ("reasoncode-407", 7),
          ("reasoncode-409", 8),
          ("reasoncode-410", 9),
          ("reasoncode-500", 10),
          ("reasoncode-501", 11),
          ("reasoncode-502", 12),
          ("reasoncode-503", 13),
          ("reasoncode-504", 14),
          ("reasoncode-505", 15),
          ("reasoncode-506", 16),
          ("reasoncode-507", 17),
          ("reasoncode-508", 18),
          ("reasoncode-509", 19),
          ("reasoncode-510", 20),
          ("reasoncode-511", 21),
          ("reasoncode-512", 22),
          ("reasoncode-513", 23),
          ("reasoncode-514", 24),
          ("reasoncode-515", 25),
          ("reasoncode-516", 26),
          ("reasoncode-517", 27),
          ("reasoncode-518", 28),
          ("reasoncode-519", 29),
          ("reasoncode-520", 30),
          ("reasoncode-521", 31),
          ("reasoncode-522", 32),
          ("reasoncode-523", 33),
          ("reasoncode-524", 34),
          ("reasoncode-525", 35),
          ("reasoncode-526", 36),
          ("reasoncode-527", 37),
          ("reasoncode-528", 38),
          ("reasoncode-529", 39),
          ("reasoncode-530", 40),
          ("reasoncode-531", 41),
          ("reasoncode-532", 42),
          ("reasoncode-533", 43),
          ("reasoncode-534", 44),
          ("reasoncode-535", 45),
          ("reasoncode-536", 46),
          ("reasoncode-537", 47),
          ("reasoncode-538", 48),
          ("reasoncode-539", 49),
          ("reasoncode-540", 50),
          ("reasoncode-541", 51))
    )


_AcPMMGCPFailedMDCXResponsesReasonCode_Type.__name__ = "Integer32"
_AcPMMGCPFailedMDCXResponsesReasonCode_Object = MibTableColumn
acPMMGCPFailedMDCXResponsesReasonCode = _AcPMMGCPFailedMDCXResponsesReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 11, 1, 1),
    _AcPMMGCPFailedMDCXResponsesReasonCode_Type()
)
acPMMGCPFailedMDCXResponsesReasonCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPFailedMDCXResponsesReasonCode.setStatus("current")


class _AcPMMGCPFailedMDCXResponsesInterval_Type(Unsigned32):
    """Custom type acPMMGCPFailedMDCXResponsesInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPFailedMDCXResponsesInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPFailedMDCXResponsesInterval_Object = MibTableColumn
acPMMGCPFailedMDCXResponsesInterval = _AcPMMGCPFailedMDCXResponsesInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 11, 1, 2),
    _AcPMMGCPFailedMDCXResponsesInterval_Type()
)
acPMMGCPFailedMDCXResponsesInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPFailedMDCXResponsesInterval.setStatus("current")
_AcPMMGCPFailedMDCXResponsesVal_Type = Counter32
_AcPMMGCPFailedMDCXResponsesVal_Object = MibTableColumn
acPMMGCPFailedMDCXResponsesVal = _AcPMMGCPFailedMDCXResponsesVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 11, 1, 3),
    _AcPMMGCPFailedMDCXResponsesVal_Type()
)
acPMMGCPFailedMDCXResponsesVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPFailedMDCXResponsesVal.setStatus("current")
_AcPMMGCPGeneratedDLCXPerReasonCodeTable_Object = MibTable
acPMMGCPGeneratedDLCXPerReasonCodeTable = _AcPMMGCPGeneratedDLCXPerReasonCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 12)
)
if mibBuilder.loadTexts:
    acPMMGCPGeneratedDLCXPerReasonCodeTable.setStatus("current")
_AcPMMGCPGeneratedDLCXPerReasonCodeEntry_Object = MibTableRow
acPMMGCPGeneratedDLCXPerReasonCodeEntry = _AcPMMGCPGeneratedDLCXPerReasonCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 12, 1)
)
acPMMGCPGeneratedDLCXPerReasonCodeEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMGCPGeneratedDLCXPerReasonCodeReasonCode"),
    (0, "AC-PM-Control-MIB", "acPMMGCPGeneratedDLCXPerReasonCodeInterval"),
)
if mibBuilder.loadTexts:
    acPMMGCPGeneratedDLCXPerReasonCodeEntry.setStatus("current")


class _AcPMMGCPGeneratedDLCXPerReasonCodeReasonCode_Type(Integer32):
    """Custom type acPMMGCPGeneratedDLCXPerReasonCodeReasonCode based on Integer32"""
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
        *(("eNDPOINT-MALFUNCTIONING-900", 0),
          ("eNDPOINT-TAKEN-OUT-OF-SERVICE-901", 1),
          ("lOSS-OF-LOWER-LAYER-CONNECTIVITY-902", 2),
          ("qOS-RESOURCE-RESERVATION-WAS-LOST-903", 3),
          ("mANUAL-INTERVENTION-904", 4),
          ("fACILITY-FAILURE-905", 5))
    )


_AcPMMGCPGeneratedDLCXPerReasonCodeReasonCode_Type.__name__ = "Integer32"
_AcPMMGCPGeneratedDLCXPerReasonCodeReasonCode_Object = MibTableColumn
acPMMGCPGeneratedDLCXPerReasonCodeReasonCode = _AcPMMGCPGeneratedDLCXPerReasonCodeReasonCode_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 12, 1, 1),
    _AcPMMGCPGeneratedDLCXPerReasonCodeReasonCode_Type()
)
acPMMGCPGeneratedDLCXPerReasonCodeReasonCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPGeneratedDLCXPerReasonCodeReasonCode.setStatus("current")


class _AcPMMGCPGeneratedDLCXPerReasonCodeInterval_Type(Unsigned32):
    """Custom type acPMMGCPGeneratedDLCXPerReasonCodeInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMGCPGeneratedDLCXPerReasonCodeInterval_Type.__name__ = "Unsigned32"
_AcPMMGCPGeneratedDLCXPerReasonCodeInterval_Object = MibTableColumn
acPMMGCPGeneratedDLCXPerReasonCodeInterval = _AcPMMGCPGeneratedDLCXPerReasonCodeInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 12, 1, 2),
    _AcPMMGCPGeneratedDLCXPerReasonCodeInterval_Type()
)
acPMMGCPGeneratedDLCXPerReasonCodeInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMGCPGeneratedDLCXPerReasonCodeInterval.setStatus("current")
_AcPMMGCPGeneratedDLCXPerReasonCodeVal_Type = Counter32
_AcPMMGCPGeneratedDLCXPerReasonCodeVal_Object = MibTableColumn
acPMMGCPGeneratedDLCXPerReasonCodeVal = _AcPMMGCPGeneratedDLCXPerReasonCodeVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 51, 12, 1, 3),
    _AcPMMGCPGeneratedDLCXPerReasonCodeVal_Type()
)
acPMMGCPGeneratedDLCXPerReasonCodeVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMGCPGeneratedDLCXPerReasonCodeVal.setStatus("current")
_AcPMSIP_ObjectIdentity = ObjectIdentity
acPMSIP = _AcPMSIP_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52)
)
_AcPMSIPAttemptedCallsTable_Object = MibTable
acPMSIPAttemptedCallsTable = _AcPMSIPAttemptedCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 1)
)
if mibBuilder.loadTexts:
    acPMSIPAttemptedCallsTable.setStatus("current")
_AcPMSIPAttemptedCallsEntry_Object = MibTableRow
acPMSIPAttemptedCallsEntry = _AcPMSIPAttemptedCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 1, 1)
)
acPMSIPAttemptedCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPAttemptedCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPAttemptedCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPAttemptedCallsEntry.setStatus("current")


class _AcPMSIPAttemptedCallsDirection_Type(Integer32):
    """Custom type acPMSIPAttemptedCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPAttemptedCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPAttemptedCallsDirection_Object = MibTableColumn
acPMSIPAttemptedCallsDirection = _AcPMSIPAttemptedCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 1, 1, 1),
    _AcPMSIPAttemptedCallsDirection_Type()
)
acPMSIPAttemptedCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPAttemptedCallsDirection.setStatus("current")


class _AcPMSIPAttemptedCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPAttemptedCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPAttemptedCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPAttemptedCallsInterval_Object = MibTableColumn
acPMSIPAttemptedCallsInterval = _AcPMSIPAttemptedCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 1, 1, 2),
    _AcPMSIPAttemptedCallsInterval_Type()
)
acPMSIPAttemptedCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPAttemptedCallsInterval.setStatus("current")
_AcPMSIPAttemptedCallsVal_Type = Counter32
_AcPMSIPAttemptedCallsVal_Object = MibTableColumn
acPMSIPAttemptedCallsVal = _AcPMSIPAttemptedCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 1, 1, 3),
    _AcPMSIPAttemptedCallsVal_Type()
)
acPMSIPAttemptedCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPAttemptedCallsVal.setStatus("current")
_AcPMSIPCallDurationTable_Object = MibTable
acPMSIPCallDurationTable = _AcPMSIPCallDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2)
)
if mibBuilder.loadTexts:
    acPMSIPCallDurationTable.setStatus("current")
_AcPMSIPCallDurationEntry_Object = MibTableRow
acPMSIPCallDurationEntry = _AcPMSIPCallDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1)
)
acPMSIPCallDurationEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPCallDurationDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPCallDurationInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPCallDurationEntry.setStatus("current")


class _AcPMSIPCallDurationDirection_Type(Integer32):
    """Custom type acPMSIPCallDurationDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPCallDurationDirection_Type.__name__ = "Integer32"
_AcPMSIPCallDurationDirection_Object = MibTableColumn
acPMSIPCallDurationDirection = _AcPMSIPCallDurationDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 1),
    _AcPMSIPCallDurationDirection_Type()
)
acPMSIPCallDurationDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPCallDurationDirection.setStatus("current")


class _AcPMSIPCallDurationInterval_Type(Unsigned32):
    """Custom type acPMSIPCallDurationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPCallDurationInterval_Type.__name__ = "Unsigned32"
_AcPMSIPCallDurationInterval_Object = MibTableColumn
acPMSIPCallDurationInterval = _AcPMSIPCallDurationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 2),
    _AcPMSIPCallDurationInterval_Type()
)
acPMSIPCallDurationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPCallDurationInterval.setStatus("current")
_AcPMSIPCallDurationVal_Type = Gauge32
_AcPMSIPCallDurationVal_Object = MibTableColumn
acPMSIPCallDurationVal = _AcPMSIPCallDurationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 3),
    _AcPMSIPCallDurationVal_Type()
)
acPMSIPCallDurationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPCallDurationVal.setStatus("current")


class _AcPMSIPCallDurationAverage_Type(Integer32):
    """Custom type acPMSIPCallDurationAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSIPCallDurationAverage_Type.__name__ = "Integer32"
_AcPMSIPCallDurationAverage_Object = MibTableColumn
acPMSIPCallDurationAverage = _AcPMSIPCallDurationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 4),
    _AcPMSIPCallDurationAverage_Type()
)
acPMSIPCallDurationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPCallDurationAverage.setStatus("current")


class _AcPMSIPCallDurationMax_Type(Integer32):
    """Custom type acPMSIPCallDurationMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSIPCallDurationMax_Type.__name__ = "Integer32"
_AcPMSIPCallDurationMax_Object = MibTableColumn
acPMSIPCallDurationMax = _AcPMSIPCallDurationMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 5),
    _AcPMSIPCallDurationMax_Type()
)
acPMSIPCallDurationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPCallDurationMax.setStatus("current")


class _AcPMSIPCallDurationMin_Type(Integer32):
    """Custom type acPMSIPCallDurationMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSIPCallDurationMin_Type.__name__ = "Integer32"
_AcPMSIPCallDurationMin_Object = MibTableColumn
acPMSIPCallDurationMin = _AcPMSIPCallDurationMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 6),
    _AcPMSIPCallDurationMin_Type()
)
acPMSIPCallDurationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPCallDurationMin.setStatus("current")
_AcPMSIPCallDurationVolume_Type = Counter32
_AcPMSIPCallDurationVolume_Object = MibTableColumn
acPMSIPCallDurationVolume = _AcPMSIPCallDurationVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 7),
    _AcPMSIPCallDurationVolume_Type()
)
acPMSIPCallDurationVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPCallDurationVolume.setStatus("current")


class _AcPMSIPCallDurationTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMSIPCallDurationTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSIPCallDurationTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMSIPCallDurationTimeBelowLowThreshold_Object = MibTableColumn
acPMSIPCallDurationTimeBelowLowThreshold = _AcPMSIPCallDurationTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 8),
    _AcPMSIPCallDurationTimeBelowLowThreshold_Type()
)
acPMSIPCallDurationTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPCallDurationTimeBelowLowThreshold.setStatus("current")


class _AcPMSIPCallDurationTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMSIPCallDurationTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSIPCallDurationTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMSIPCallDurationTimeBetweenThresholds_Object = MibTableColumn
acPMSIPCallDurationTimeBetweenThresholds = _AcPMSIPCallDurationTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 9),
    _AcPMSIPCallDurationTimeBetweenThresholds_Type()
)
acPMSIPCallDurationTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPCallDurationTimeBetweenThresholds.setStatus("current")


class _AcPMSIPCallDurationTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMSIPCallDurationTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMSIPCallDurationTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMSIPCallDurationTimeAboveHighThreshold_Object = MibTableColumn
acPMSIPCallDurationTimeAboveHighThreshold = _AcPMSIPCallDurationTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 10),
    _AcPMSIPCallDurationTimeAboveHighThreshold_Type()
)
acPMSIPCallDurationTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPCallDurationTimeAboveHighThreshold.setStatus("current")


class _AcPMSIPCallDurationFullDayAverage_Type(Integer32):
    """Custom type acPMSIPCallDurationFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSIPCallDurationFullDayAverage_Type.__name__ = "Integer32"
_AcPMSIPCallDurationFullDayAverage_Object = MibTableColumn
acPMSIPCallDurationFullDayAverage = _AcPMSIPCallDurationFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 11),
    _AcPMSIPCallDurationFullDayAverage_Type()
)
acPMSIPCallDurationFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPCallDurationFullDayAverage.setStatus("current")


class _AcPMSIPCallDurationTotal_Type(Integer32):
    """Custom type acPMSIPCallDurationTotal based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2147483647),
    )


_AcPMSIPCallDurationTotal_Type.__name__ = "Integer32"
_AcPMSIPCallDurationTotal_Object = MibTableColumn
acPMSIPCallDurationTotal = _AcPMSIPCallDurationTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 2, 1, 12),
    _AcPMSIPCallDurationTotal_Type()
)
acPMSIPCallDurationTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPCallDurationTotal.setStatus("current")
_AcPMSIPNoMatchCallsTable_Object = MibTable
acPMSIPNoMatchCallsTable = _AcPMSIPNoMatchCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 3)
)
if mibBuilder.loadTexts:
    acPMSIPNoMatchCallsTable.setStatus("current")
_AcPMSIPNoMatchCallsEntry_Object = MibTableRow
acPMSIPNoMatchCallsEntry = _AcPMSIPNoMatchCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 3, 1)
)
acPMSIPNoMatchCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPNoMatchCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPNoMatchCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPNoMatchCallsEntry.setStatus("current")


class _AcPMSIPNoMatchCallsDirection_Type(Integer32):
    """Custom type acPMSIPNoMatchCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPNoMatchCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPNoMatchCallsDirection_Object = MibTableColumn
acPMSIPNoMatchCallsDirection = _AcPMSIPNoMatchCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 3, 1, 1),
    _AcPMSIPNoMatchCallsDirection_Type()
)
acPMSIPNoMatchCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPNoMatchCallsDirection.setStatus("current")


class _AcPMSIPNoMatchCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPNoMatchCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPNoMatchCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPNoMatchCallsInterval_Object = MibTableColumn
acPMSIPNoMatchCallsInterval = _AcPMSIPNoMatchCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 3, 1, 2),
    _AcPMSIPNoMatchCallsInterval_Type()
)
acPMSIPNoMatchCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPNoMatchCallsInterval.setStatus("current")
_AcPMSIPNoMatchCallsVal_Type = Counter32
_AcPMSIPNoMatchCallsVal_Object = MibTableColumn
acPMSIPNoMatchCallsVal = _AcPMSIPNoMatchCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 3, 1, 3),
    _AcPMSIPNoMatchCallsVal_Type()
)
acPMSIPNoMatchCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPNoMatchCallsVal.setStatus("current")
_AcPMSIPBusyCallsTable_Object = MibTable
acPMSIPBusyCallsTable = _AcPMSIPBusyCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 4)
)
if mibBuilder.loadTexts:
    acPMSIPBusyCallsTable.setStatus("current")
_AcPMSIPBusyCallsEntry_Object = MibTableRow
acPMSIPBusyCallsEntry = _AcPMSIPBusyCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 4, 1)
)
acPMSIPBusyCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPBusyCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPBusyCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPBusyCallsEntry.setStatus("current")


class _AcPMSIPBusyCallsDirection_Type(Integer32):
    """Custom type acPMSIPBusyCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPBusyCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPBusyCallsDirection_Object = MibTableColumn
acPMSIPBusyCallsDirection = _AcPMSIPBusyCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 4, 1, 1),
    _AcPMSIPBusyCallsDirection_Type()
)
acPMSIPBusyCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPBusyCallsDirection.setStatus("current")


class _AcPMSIPBusyCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPBusyCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPBusyCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPBusyCallsInterval_Object = MibTableColumn
acPMSIPBusyCallsInterval = _AcPMSIPBusyCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 4, 1, 2),
    _AcPMSIPBusyCallsInterval_Type()
)
acPMSIPBusyCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPBusyCallsInterval.setStatus("current")
_AcPMSIPBusyCallsVal_Type = Counter32
_AcPMSIPBusyCallsVal_Object = MibTableColumn
acPMSIPBusyCallsVal = _AcPMSIPBusyCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 4, 1, 3),
    _AcPMSIPBusyCallsVal_Type()
)
acPMSIPBusyCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPBusyCallsVal.setStatus("current")
_AcPMSIPNoAnswerCallsTable_Object = MibTable
acPMSIPNoAnswerCallsTable = _AcPMSIPNoAnswerCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 5)
)
if mibBuilder.loadTexts:
    acPMSIPNoAnswerCallsTable.setStatus("current")
_AcPMSIPNoAnswerCallsEntry_Object = MibTableRow
acPMSIPNoAnswerCallsEntry = _AcPMSIPNoAnswerCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 5, 1)
)
acPMSIPNoAnswerCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPNoAnswerCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPNoAnswerCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPNoAnswerCallsEntry.setStatus("current")


class _AcPMSIPNoAnswerCallsDirection_Type(Integer32):
    """Custom type acPMSIPNoAnswerCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPNoAnswerCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPNoAnswerCallsDirection_Object = MibTableColumn
acPMSIPNoAnswerCallsDirection = _AcPMSIPNoAnswerCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 5, 1, 1),
    _AcPMSIPNoAnswerCallsDirection_Type()
)
acPMSIPNoAnswerCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPNoAnswerCallsDirection.setStatus("current")


class _AcPMSIPNoAnswerCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPNoAnswerCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPNoAnswerCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPNoAnswerCallsInterval_Object = MibTableColumn
acPMSIPNoAnswerCallsInterval = _AcPMSIPNoAnswerCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 5, 1, 2),
    _AcPMSIPNoAnswerCallsInterval_Type()
)
acPMSIPNoAnswerCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPNoAnswerCallsInterval.setStatus("current")
_AcPMSIPNoAnswerCallsVal_Type = Counter32
_AcPMSIPNoAnswerCallsVal_Object = MibTableColumn
acPMSIPNoAnswerCallsVal = _AcPMSIPNoAnswerCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 5, 1, 3),
    _AcPMSIPNoAnswerCallsVal_Type()
)
acPMSIPNoAnswerCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPNoAnswerCallsVal.setStatus("current")
_AcPMSIPNoRouteCallsTable_Object = MibTable
acPMSIPNoRouteCallsTable = _AcPMSIPNoRouteCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 6)
)
if mibBuilder.loadTexts:
    acPMSIPNoRouteCallsTable.setStatus("current")
_AcPMSIPNoRouteCallsEntry_Object = MibTableRow
acPMSIPNoRouteCallsEntry = _AcPMSIPNoRouteCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 6, 1)
)
acPMSIPNoRouteCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPNoRouteCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPNoRouteCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPNoRouteCallsEntry.setStatus("current")


class _AcPMSIPNoRouteCallsDirection_Type(Integer32):
    """Custom type acPMSIPNoRouteCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPNoRouteCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPNoRouteCallsDirection_Object = MibTableColumn
acPMSIPNoRouteCallsDirection = _AcPMSIPNoRouteCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 6, 1, 1),
    _AcPMSIPNoRouteCallsDirection_Type()
)
acPMSIPNoRouteCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPNoRouteCallsDirection.setStatus("current")


class _AcPMSIPNoRouteCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPNoRouteCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPNoRouteCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPNoRouteCallsInterval_Object = MibTableColumn
acPMSIPNoRouteCallsInterval = _AcPMSIPNoRouteCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 6, 1, 2),
    _AcPMSIPNoRouteCallsInterval_Type()
)
acPMSIPNoRouteCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPNoRouteCallsInterval.setStatus("current")
_AcPMSIPNoRouteCallsVal_Type = Counter32
_AcPMSIPNoRouteCallsVal_Object = MibTableColumn
acPMSIPNoRouteCallsVal = _AcPMSIPNoRouteCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 6, 1, 3),
    _AcPMSIPNoRouteCallsVal_Type()
)
acPMSIPNoRouteCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPNoRouteCallsVal.setStatus("current")
_AcPMSIPFailCallsTable_Object = MibTable
acPMSIPFailCallsTable = _AcPMSIPFailCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 7)
)
if mibBuilder.loadTexts:
    acPMSIPFailCallsTable.setStatus("current")
_AcPMSIPFailCallsEntry_Object = MibTableRow
acPMSIPFailCallsEntry = _AcPMSIPFailCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 7, 1)
)
acPMSIPFailCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPFailCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPFailCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPFailCallsEntry.setStatus("current")


class _AcPMSIPFailCallsDirection_Type(Integer32):
    """Custom type acPMSIPFailCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPFailCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPFailCallsDirection_Object = MibTableColumn
acPMSIPFailCallsDirection = _AcPMSIPFailCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 7, 1, 1),
    _AcPMSIPFailCallsDirection_Type()
)
acPMSIPFailCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPFailCallsDirection.setStatus("current")


class _AcPMSIPFailCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPFailCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPFailCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPFailCallsInterval_Object = MibTableColumn
acPMSIPFailCallsInterval = _AcPMSIPFailCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 7, 1, 2),
    _AcPMSIPFailCallsInterval_Type()
)
acPMSIPFailCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPFailCallsInterval.setStatus("current")
_AcPMSIPFailCallsVal_Type = Counter32
_AcPMSIPFailCallsVal_Object = MibTableColumn
acPMSIPFailCallsVal = _AcPMSIPFailCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 7, 1, 3),
    _AcPMSIPFailCallsVal_Type()
)
acPMSIPFailCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPFailCallsVal.setStatus("current")
_AcPMSIPEstablishedCallsTable_Object = MibTable
acPMSIPEstablishedCallsTable = _AcPMSIPEstablishedCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 8)
)
if mibBuilder.loadTexts:
    acPMSIPEstablishedCallsTable.setStatus("current")
_AcPMSIPEstablishedCallsEntry_Object = MibTableRow
acPMSIPEstablishedCallsEntry = _AcPMSIPEstablishedCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 8, 1)
)
acPMSIPEstablishedCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPEstablishedCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPEstablishedCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPEstablishedCallsEntry.setStatus("current")


class _AcPMSIPEstablishedCallsDirection_Type(Integer32):
    """Custom type acPMSIPEstablishedCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPEstablishedCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPEstablishedCallsDirection_Object = MibTableColumn
acPMSIPEstablishedCallsDirection = _AcPMSIPEstablishedCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 8, 1, 1),
    _AcPMSIPEstablishedCallsDirection_Type()
)
acPMSIPEstablishedCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPEstablishedCallsDirection.setStatus("current")


class _AcPMSIPEstablishedCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPEstablishedCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPEstablishedCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPEstablishedCallsInterval_Object = MibTableColumn
acPMSIPEstablishedCallsInterval = _AcPMSIPEstablishedCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 8, 1, 2),
    _AcPMSIPEstablishedCallsInterval_Type()
)
acPMSIPEstablishedCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPEstablishedCallsInterval.setStatus("current")
_AcPMSIPEstablishedCallsVal_Type = Counter32
_AcPMSIPEstablishedCallsVal_Object = MibTableColumn
acPMSIPEstablishedCallsVal = _AcPMSIPEstablishedCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 8, 1, 3),
    _AcPMSIPEstablishedCallsVal_Type()
)
acPMSIPEstablishedCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPEstablishedCallsVal.setStatus("current")
_AcPMSIPFaxAttemptedCallsTable_Object = MibTable
acPMSIPFaxAttemptedCallsTable = _AcPMSIPFaxAttemptedCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 9)
)
if mibBuilder.loadTexts:
    acPMSIPFaxAttemptedCallsTable.setStatus("current")
_AcPMSIPFaxAttemptedCallsEntry_Object = MibTableRow
acPMSIPFaxAttemptedCallsEntry = _AcPMSIPFaxAttemptedCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 9, 1)
)
acPMSIPFaxAttemptedCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPFaxAttemptedCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPFaxAttemptedCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPFaxAttemptedCallsEntry.setStatus("current")


class _AcPMSIPFaxAttemptedCallsDirection_Type(Integer32):
    """Custom type acPMSIPFaxAttemptedCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPFaxAttemptedCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPFaxAttemptedCallsDirection_Object = MibTableColumn
acPMSIPFaxAttemptedCallsDirection = _AcPMSIPFaxAttemptedCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 9, 1, 1),
    _AcPMSIPFaxAttemptedCallsDirection_Type()
)
acPMSIPFaxAttemptedCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPFaxAttemptedCallsDirection.setStatus("current")


class _AcPMSIPFaxAttemptedCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPFaxAttemptedCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPFaxAttemptedCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPFaxAttemptedCallsInterval_Object = MibTableColumn
acPMSIPFaxAttemptedCallsInterval = _AcPMSIPFaxAttemptedCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 9, 1, 2),
    _AcPMSIPFaxAttemptedCallsInterval_Type()
)
acPMSIPFaxAttemptedCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPFaxAttemptedCallsInterval.setStatus("current")
_AcPMSIPFaxAttemptedCallsVal_Type = Counter32
_AcPMSIPFaxAttemptedCallsVal_Object = MibTableColumn
acPMSIPFaxAttemptedCallsVal = _AcPMSIPFaxAttemptedCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 9, 1, 3),
    _AcPMSIPFaxAttemptedCallsVal_Type()
)
acPMSIPFaxAttemptedCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPFaxAttemptedCallsVal.setStatus("current")
_AcPMSIPFaxSuccessCallsTable_Object = MibTable
acPMSIPFaxSuccessCallsTable = _AcPMSIPFaxSuccessCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 10)
)
if mibBuilder.loadTexts:
    acPMSIPFaxSuccessCallsTable.setStatus("current")
_AcPMSIPFaxSuccessCallsEntry_Object = MibTableRow
acPMSIPFaxSuccessCallsEntry = _AcPMSIPFaxSuccessCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 10, 1)
)
acPMSIPFaxSuccessCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPFaxSuccessCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPFaxSuccessCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPFaxSuccessCallsEntry.setStatus("current")


class _AcPMSIPFaxSuccessCallsDirection_Type(Integer32):
    """Custom type acPMSIPFaxSuccessCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPFaxSuccessCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPFaxSuccessCallsDirection_Object = MibTableColumn
acPMSIPFaxSuccessCallsDirection = _AcPMSIPFaxSuccessCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 10, 1, 1),
    _AcPMSIPFaxSuccessCallsDirection_Type()
)
acPMSIPFaxSuccessCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPFaxSuccessCallsDirection.setStatus("current")


class _AcPMSIPFaxSuccessCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPFaxSuccessCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPFaxSuccessCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPFaxSuccessCallsInterval_Object = MibTableColumn
acPMSIPFaxSuccessCallsInterval = _AcPMSIPFaxSuccessCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 10, 1, 2),
    _AcPMSIPFaxSuccessCallsInterval_Type()
)
acPMSIPFaxSuccessCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPFaxSuccessCallsInterval.setStatus("current")
_AcPMSIPFaxSuccessCallsVal_Type = Counter32
_AcPMSIPFaxSuccessCallsVal_Object = MibTableColumn
acPMSIPFaxSuccessCallsVal = _AcPMSIPFaxSuccessCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 10, 1, 3),
    _AcPMSIPFaxSuccessCallsVal_Type()
)
acPMSIPFaxSuccessCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPFaxSuccessCallsVal.setStatus("current")
_AcPMSIPForwardedCallsTable_Object = MibTable
acPMSIPForwardedCallsTable = _AcPMSIPForwardedCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 11)
)
if mibBuilder.loadTexts:
    acPMSIPForwardedCallsTable.setStatus("current")
_AcPMSIPForwardedCallsEntry_Object = MibTableRow
acPMSIPForwardedCallsEntry = _AcPMSIPForwardedCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 11, 1)
)
acPMSIPForwardedCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPForwardedCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPForwardedCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPForwardedCallsEntry.setStatus("current")


class _AcPMSIPForwardedCallsDirection_Type(Integer32):
    """Custom type acPMSIPForwardedCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPForwardedCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPForwardedCallsDirection_Object = MibTableColumn
acPMSIPForwardedCallsDirection = _AcPMSIPForwardedCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 11, 1, 1),
    _AcPMSIPForwardedCallsDirection_Type()
)
acPMSIPForwardedCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPForwardedCallsDirection.setStatus("current")


class _AcPMSIPForwardedCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPForwardedCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPForwardedCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPForwardedCallsInterval_Object = MibTableColumn
acPMSIPForwardedCallsInterval = _AcPMSIPForwardedCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 11, 1, 2),
    _AcPMSIPForwardedCallsInterval_Type()
)
acPMSIPForwardedCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPForwardedCallsInterval.setStatus("current")
_AcPMSIPForwardedCallsVal_Type = Counter32
_AcPMSIPForwardedCallsVal_Object = MibTableColumn
acPMSIPForwardedCallsVal = _AcPMSIPForwardedCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 11, 1, 3),
    _AcPMSIPForwardedCallsVal_Type()
)
acPMSIPForwardedCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPForwardedCallsVal.setStatus("current")
_AcPMSIPNoResourcesCallsTable_Object = MibTable
acPMSIPNoResourcesCallsTable = _AcPMSIPNoResourcesCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 12)
)
if mibBuilder.loadTexts:
    acPMSIPNoResourcesCallsTable.setStatus("current")
_AcPMSIPNoResourcesCallsEntry_Object = MibTableRow
acPMSIPNoResourcesCallsEntry = _AcPMSIPNoResourcesCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 12, 1)
)
acPMSIPNoResourcesCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPNoResourcesCallsDirection"),
    (0, "AC-PM-Control-MIB", "acPMSIPNoResourcesCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPNoResourcesCallsEntry.setStatus("current")


class _AcPMSIPNoResourcesCallsDirection_Type(Integer32):
    """Custom type acPMSIPNoResourcesCallsDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tel2IP", 0),
          ("iP2Tel", 1))
    )


_AcPMSIPNoResourcesCallsDirection_Type.__name__ = "Integer32"
_AcPMSIPNoResourcesCallsDirection_Object = MibTableColumn
acPMSIPNoResourcesCallsDirection = _AcPMSIPNoResourcesCallsDirection_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 12, 1, 1),
    _AcPMSIPNoResourcesCallsDirection_Type()
)
acPMSIPNoResourcesCallsDirection.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPNoResourcesCallsDirection.setStatus("current")


class _AcPMSIPNoResourcesCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPNoResourcesCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPNoResourcesCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPNoResourcesCallsInterval_Object = MibTableColumn
acPMSIPNoResourcesCallsInterval = _AcPMSIPNoResourcesCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 12, 1, 2),
    _AcPMSIPNoResourcesCallsInterval_Type()
)
acPMSIPNoResourcesCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPNoResourcesCallsInterval.setStatus("current")
_AcPMSIPNoResourcesCallsVal_Type = Counter32
_AcPMSIPNoResourcesCallsVal_Object = MibTableColumn
acPMSIPNoResourcesCallsVal = _AcPMSIPNoResourcesCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 12, 1, 3),
    _AcPMSIPNoResourcesCallsVal_Type()
)
acPMSIPNoResourcesCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPNoResourcesCallsVal.setStatus("current")
_AcPMSIPTel2IPTrunkEstablishedCallsTable_Object = MibTable
acPMSIPTel2IPTrunkEstablishedCallsTable = _AcPMSIPTel2IPTrunkEstablishedCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 13)
)
if mibBuilder.loadTexts:
    acPMSIPTel2IPTrunkEstablishedCallsTable.setStatus("current")
_AcPMSIPTel2IPTrunkEstablishedCallsEntry_Object = MibTableRow
acPMSIPTel2IPTrunkEstablishedCallsEntry = _AcPMSIPTel2IPTrunkEstablishedCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 13, 1)
)
acPMSIPTel2IPTrunkEstablishedCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPTel2IPTrunkEstablishedCallsTrunkNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPTel2IPTrunkEstablishedCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPTel2IPTrunkEstablishedCallsEntry.setStatus("current")


class _AcPMSIPTel2IPTrunkEstablishedCallsTrunkNum_Type(Unsigned32):
    """Custom type acPMSIPTel2IPTrunkEstablishedCallsTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMSIPTel2IPTrunkEstablishedCallsTrunkNum_Type.__name__ = "Unsigned32"
_AcPMSIPTel2IPTrunkEstablishedCallsTrunkNum_Object = MibTableColumn
acPMSIPTel2IPTrunkEstablishedCallsTrunkNum = _AcPMSIPTel2IPTrunkEstablishedCallsTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 13, 1, 1),
    _AcPMSIPTel2IPTrunkEstablishedCallsTrunkNum_Type()
)
acPMSIPTel2IPTrunkEstablishedCallsTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTel2IPTrunkEstablishedCallsTrunkNum.setStatus("current")


class _AcPMSIPTel2IPTrunkEstablishedCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPTel2IPTrunkEstablishedCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPTel2IPTrunkEstablishedCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPTel2IPTrunkEstablishedCallsInterval_Object = MibTableColumn
acPMSIPTel2IPTrunkEstablishedCallsInterval = _AcPMSIPTel2IPTrunkEstablishedCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 13, 1, 2),
    _AcPMSIPTel2IPTrunkEstablishedCallsInterval_Type()
)
acPMSIPTel2IPTrunkEstablishedCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTel2IPTrunkEstablishedCallsInterval.setStatus("current")
_AcPMSIPTel2IPTrunkEstablishedCallsVal_Type = Counter32
_AcPMSIPTel2IPTrunkEstablishedCallsVal_Object = MibTableColumn
acPMSIPTel2IPTrunkEstablishedCallsVal = _AcPMSIPTel2IPTrunkEstablishedCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 13, 1, 3),
    _AcPMSIPTel2IPTrunkEstablishedCallsVal_Type()
)
acPMSIPTel2IPTrunkEstablishedCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTel2IPTrunkEstablishedCallsVal.setStatus("current")
_AcPMSIPIP2TelTrunkEstablishedCallsTable_Object = MibTable
acPMSIPIP2TelTrunkEstablishedCallsTable = _AcPMSIPIP2TelTrunkEstablishedCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 14)
)
if mibBuilder.loadTexts:
    acPMSIPIP2TelTrunkEstablishedCallsTable.setStatus("current")
_AcPMSIPIP2TelTrunkEstablishedCallsEntry_Object = MibTableRow
acPMSIPIP2TelTrunkEstablishedCallsEntry = _AcPMSIPIP2TelTrunkEstablishedCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 14, 1)
)
acPMSIPIP2TelTrunkEstablishedCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPIP2TelTrunkEstablishedCallsTrunkNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPIP2TelTrunkEstablishedCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPIP2TelTrunkEstablishedCallsEntry.setStatus("current")


class _AcPMSIPIP2TelTrunkEstablishedCallsTrunkNum_Type(Unsigned32):
    """Custom type acPMSIPIP2TelTrunkEstablishedCallsTrunkNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMSIPIP2TelTrunkEstablishedCallsTrunkNum_Type.__name__ = "Unsigned32"
_AcPMSIPIP2TelTrunkEstablishedCallsTrunkNum_Object = MibTableColumn
acPMSIPIP2TelTrunkEstablishedCallsTrunkNum = _AcPMSIPIP2TelTrunkEstablishedCallsTrunkNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 14, 1, 1),
    _AcPMSIPIP2TelTrunkEstablishedCallsTrunkNum_Type()
)
acPMSIPIP2TelTrunkEstablishedCallsTrunkNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIP2TelTrunkEstablishedCallsTrunkNum.setStatus("current")


class _AcPMSIPIP2TelTrunkEstablishedCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPIP2TelTrunkEstablishedCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPIP2TelTrunkEstablishedCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPIP2TelTrunkEstablishedCallsInterval_Object = MibTableColumn
acPMSIPIP2TelTrunkEstablishedCallsInterval = _AcPMSIPIP2TelTrunkEstablishedCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 14, 1, 2),
    _AcPMSIPIP2TelTrunkEstablishedCallsInterval_Type()
)
acPMSIPIP2TelTrunkEstablishedCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIP2TelTrunkEstablishedCallsInterval.setStatus("current")
_AcPMSIPIP2TelTrunkEstablishedCallsVal_Type = Counter32
_AcPMSIPIP2TelTrunkEstablishedCallsVal_Object = MibTableColumn
acPMSIPIP2TelTrunkEstablishedCallsVal = _AcPMSIPIP2TelTrunkEstablishedCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 14, 1, 3),
    _AcPMSIPIP2TelTrunkEstablishedCallsVal_Type()
)
acPMSIPIP2TelTrunkEstablishedCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIP2TelTrunkEstablishedCallsVal.setStatus("current")
_AcPMSIPTel2IPTrunkGroupEstablishedCallsTable_Object = MibTable
acPMSIPTel2IPTrunkGroupEstablishedCallsTable = _AcPMSIPTel2IPTrunkGroupEstablishedCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 15)
)
if mibBuilder.loadTexts:
    acPMSIPTel2IPTrunkGroupEstablishedCallsTable.setStatus("current")
_AcPMSIPTel2IPTrunkGroupEstablishedCallsEntry_Object = MibTableRow
acPMSIPTel2IPTrunkGroupEstablishedCallsEntry = _AcPMSIPTel2IPTrunkGroupEstablishedCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 15, 1)
)
acPMSIPTel2IPTrunkGroupEstablishedCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPTel2IPTrunkGroupEstablishedCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPTel2IPTrunkGroupEstablishedCallsEntry.setStatus("current")


class _AcPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum_Type(Unsigned32):
    """Custom type acPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum_Object = MibTableColumn
acPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum = _AcPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 15, 1, 1),
    _AcPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum_Type()
)
acPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum.setStatus("current")


class _AcPMSIPTel2IPTrunkGroupEstablishedCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPTel2IPTrunkGroupEstablishedCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPTel2IPTrunkGroupEstablishedCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPTel2IPTrunkGroupEstablishedCallsInterval_Object = MibTableColumn
acPMSIPTel2IPTrunkGroupEstablishedCallsInterval = _AcPMSIPTel2IPTrunkGroupEstablishedCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 15, 1, 2),
    _AcPMSIPTel2IPTrunkGroupEstablishedCallsInterval_Type()
)
acPMSIPTel2IPTrunkGroupEstablishedCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTel2IPTrunkGroupEstablishedCallsInterval.setStatus("current")
_AcPMSIPTel2IPTrunkGroupEstablishedCallsVal_Type = Counter32
_AcPMSIPTel2IPTrunkGroupEstablishedCallsVal_Object = MibTableColumn
acPMSIPTel2IPTrunkGroupEstablishedCallsVal = _AcPMSIPTel2IPTrunkGroupEstablishedCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 15, 1, 3),
    _AcPMSIPTel2IPTrunkGroupEstablishedCallsVal_Type()
)
acPMSIPTel2IPTrunkGroupEstablishedCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTel2IPTrunkGroupEstablishedCallsVal.setStatus("current")
_AcPMSIPIP2TelTrunkGroupEstablishedCallsTable_Object = MibTable
acPMSIPIP2TelTrunkGroupEstablishedCallsTable = _AcPMSIPIP2TelTrunkGroupEstablishedCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 16)
)
if mibBuilder.loadTexts:
    acPMSIPIP2TelTrunkGroupEstablishedCallsTable.setStatus("current")
_AcPMSIPIP2TelTrunkGroupEstablishedCallsEntry_Object = MibTableRow
acPMSIPIP2TelTrunkGroupEstablishedCallsEntry = _AcPMSIPIP2TelTrunkGroupEstablishedCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 16, 1)
)
acPMSIPIP2TelTrunkGroupEstablishedCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPIP2TelTrunkGroupEstablishedCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPIP2TelTrunkGroupEstablishedCallsEntry.setStatus("current")


class _AcPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum_Type(Unsigned32):
    """Custom type acPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum_Object = MibTableColumn
acPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum = _AcPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 16, 1, 1),
    _AcPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum_Type()
)
acPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum.setStatus("current")


class _AcPMSIPIP2TelTrunkGroupEstablishedCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPIP2TelTrunkGroupEstablishedCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPIP2TelTrunkGroupEstablishedCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPIP2TelTrunkGroupEstablishedCallsInterval_Object = MibTableColumn
acPMSIPIP2TelTrunkGroupEstablishedCallsInterval = _AcPMSIPIP2TelTrunkGroupEstablishedCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 16, 1, 2),
    _AcPMSIPIP2TelTrunkGroupEstablishedCallsInterval_Type()
)
acPMSIPIP2TelTrunkGroupEstablishedCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIP2TelTrunkGroupEstablishedCallsInterval.setStatus("current")
_AcPMSIPIP2TelTrunkGroupEstablishedCallsVal_Type = Counter32
_AcPMSIPIP2TelTrunkGroupEstablishedCallsVal_Object = MibTableColumn
acPMSIPIP2TelTrunkGroupEstablishedCallsVal = _AcPMSIPIP2TelTrunkGroupEstablishedCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 16, 1, 3),
    _AcPMSIPIP2TelTrunkGroupEstablishedCallsVal_Type()
)
acPMSIPIP2TelTrunkGroupEstablishedCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIP2TelTrunkGroupEstablishedCallsVal.setStatus("current")
_AcPMSIPSRDDialogsTable_Object = MibTable
acPMSIPSRDDialogsTable = _AcPMSIPSRDDialogsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 17)
)
if mibBuilder.loadTexts:
    acPMSIPSRDDialogsTable.setStatus("current")
_AcPMSIPSRDDialogsEntry_Object = MibTableRow
acPMSIPSRDDialogsEntry = _AcPMSIPSRDDialogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 17, 1)
)
acPMSIPSRDDialogsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPSRDDialogsSrdNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPSRDDialogsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPSRDDialogsEntry.setStatus("current")


class _AcPMSIPSRDDialogsSrdNum_Type(Unsigned32):
    """Custom type acPMSIPSRDDialogsSrdNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AcPMSIPSRDDialogsSrdNum_Type.__name__ = "Unsigned32"
_AcPMSIPSRDDialogsSrdNum_Object = MibTableColumn
acPMSIPSRDDialogsSrdNum = _AcPMSIPSRDDialogsSrdNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 17, 1, 1),
    _AcPMSIPSRDDialogsSrdNum_Type()
)
acPMSIPSRDDialogsSrdNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPSRDDialogsSrdNum.setStatus("current")


class _AcPMSIPSRDDialogsInterval_Type(Unsigned32):
    """Custom type acPMSIPSRDDialogsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPSRDDialogsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPSRDDialogsInterval_Object = MibTableColumn
acPMSIPSRDDialogsInterval = _AcPMSIPSRDDialogsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 17, 1, 2),
    _AcPMSIPSRDDialogsInterval_Type()
)
acPMSIPSRDDialogsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPSRDDialogsInterval.setStatus("current")
_AcPMSIPSRDDialogsVal_Type = Counter32
_AcPMSIPSRDDialogsVal_Object = MibTableColumn
acPMSIPSRDDialogsVal = _AcPMSIPSRDDialogsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 17, 1, 3),
    _AcPMSIPSRDDialogsVal_Type()
)
acPMSIPSRDDialogsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPSRDDialogsVal.setStatus("current")
_AcPMSIPSRDInviteDialogsTable_Object = MibTable
acPMSIPSRDInviteDialogsTable = _AcPMSIPSRDInviteDialogsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 18)
)
if mibBuilder.loadTexts:
    acPMSIPSRDInviteDialogsTable.setStatus("current")
_AcPMSIPSRDInviteDialogsEntry_Object = MibTableRow
acPMSIPSRDInviteDialogsEntry = _AcPMSIPSRDInviteDialogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 18, 1)
)
acPMSIPSRDInviteDialogsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPSRDInviteDialogsSrdNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPSRDInviteDialogsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPSRDInviteDialogsEntry.setStatus("current")


class _AcPMSIPSRDInviteDialogsSrdNum_Type(Unsigned32):
    """Custom type acPMSIPSRDInviteDialogsSrdNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AcPMSIPSRDInviteDialogsSrdNum_Type.__name__ = "Unsigned32"
_AcPMSIPSRDInviteDialogsSrdNum_Object = MibTableColumn
acPMSIPSRDInviteDialogsSrdNum = _AcPMSIPSRDInviteDialogsSrdNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 18, 1, 1),
    _AcPMSIPSRDInviteDialogsSrdNum_Type()
)
acPMSIPSRDInviteDialogsSrdNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPSRDInviteDialogsSrdNum.setStatus("current")


class _AcPMSIPSRDInviteDialogsInterval_Type(Unsigned32):
    """Custom type acPMSIPSRDInviteDialogsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPSRDInviteDialogsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPSRDInviteDialogsInterval_Object = MibTableColumn
acPMSIPSRDInviteDialogsInterval = _AcPMSIPSRDInviteDialogsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 18, 1, 2),
    _AcPMSIPSRDInviteDialogsInterval_Type()
)
acPMSIPSRDInviteDialogsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPSRDInviteDialogsInterval.setStatus("current")
_AcPMSIPSRDInviteDialogsVal_Type = Counter32
_AcPMSIPSRDInviteDialogsVal_Object = MibTableColumn
acPMSIPSRDInviteDialogsVal = _AcPMSIPSRDInviteDialogsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 18, 1, 3),
    _AcPMSIPSRDInviteDialogsVal_Type()
)
acPMSIPSRDInviteDialogsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPSRDInviteDialogsVal.setStatus("current")
_AcPMSIPSRDSubscribeDialogsTable_Object = MibTable
acPMSIPSRDSubscribeDialogsTable = _AcPMSIPSRDSubscribeDialogsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 19)
)
if mibBuilder.loadTexts:
    acPMSIPSRDSubscribeDialogsTable.setStatus("current")
_AcPMSIPSRDSubscribeDialogsEntry_Object = MibTableRow
acPMSIPSRDSubscribeDialogsEntry = _AcPMSIPSRDSubscribeDialogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 19, 1)
)
acPMSIPSRDSubscribeDialogsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPSRDSubscribeDialogsSrdNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPSRDSubscribeDialogsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPSRDSubscribeDialogsEntry.setStatus("current")


class _AcPMSIPSRDSubscribeDialogsSrdNum_Type(Unsigned32):
    """Custom type acPMSIPSRDSubscribeDialogsSrdNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AcPMSIPSRDSubscribeDialogsSrdNum_Type.__name__ = "Unsigned32"
_AcPMSIPSRDSubscribeDialogsSrdNum_Object = MibTableColumn
acPMSIPSRDSubscribeDialogsSrdNum = _AcPMSIPSRDSubscribeDialogsSrdNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 19, 1, 1),
    _AcPMSIPSRDSubscribeDialogsSrdNum_Type()
)
acPMSIPSRDSubscribeDialogsSrdNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPSRDSubscribeDialogsSrdNum.setStatus("current")


class _AcPMSIPSRDSubscribeDialogsInterval_Type(Unsigned32):
    """Custom type acPMSIPSRDSubscribeDialogsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPSRDSubscribeDialogsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPSRDSubscribeDialogsInterval_Object = MibTableColumn
acPMSIPSRDSubscribeDialogsInterval = _AcPMSIPSRDSubscribeDialogsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 19, 1, 2),
    _AcPMSIPSRDSubscribeDialogsInterval_Type()
)
acPMSIPSRDSubscribeDialogsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPSRDSubscribeDialogsInterval.setStatus("current")
_AcPMSIPSRDSubscribeDialogsVal_Type = Counter32
_AcPMSIPSRDSubscribeDialogsVal_Object = MibTableColumn
acPMSIPSRDSubscribeDialogsVal = _AcPMSIPSRDSubscribeDialogsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 19, 1, 3),
    _AcPMSIPSRDSubscribeDialogsVal_Type()
)
acPMSIPSRDSubscribeDialogsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPSRDSubscribeDialogsVal.setStatus("current")
_AcPMSIPSRDOtherDialogsTable_Object = MibTable
acPMSIPSRDOtherDialogsTable = _AcPMSIPSRDOtherDialogsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 20)
)
if mibBuilder.loadTexts:
    acPMSIPSRDOtherDialogsTable.setStatus("current")
_AcPMSIPSRDOtherDialogsEntry_Object = MibTableRow
acPMSIPSRDOtherDialogsEntry = _AcPMSIPSRDOtherDialogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 20, 1)
)
acPMSIPSRDOtherDialogsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPSRDOtherDialogsSrdNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPSRDOtherDialogsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPSRDOtherDialogsEntry.setStatus("current")


class _AcPMSIPSRDOtherDialogsSrdNum_Type(Unsigned32):
    """Custom type acPMSIPSRDOtherDialogsSrdNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_AcPMSIPSRDOtherDialogsSrdNum_Type.__name__ = "Unsigned32"
_AcPMSIPSRDOtherDialogsSrdNum_Object = MibTableColumn
acPMSIPSRDOtherDialogsSrdNum = _AcPMSIPSRDOtherDialogsSrdNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 20, 1, 1),
    _AcPMSIPSRDOtherDialogsSrdNum_Type()
)
acPMSIPSRDOtherDialogsSrdNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPSRDOtherDialogsSrdNum.setStatus("current")


class _AcPMSIPSRDOtherDialogsInterval_Type(Unsigned32):
    """Custom type acPMSIPSRDOtherDialogsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPSRDOtherDialogsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPSRDOtherDialogsInterval_Object = MibTableColumn
acPMSIPSRDOtherDialogsInterval = _AcPMSIPSRDOtherDialogsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 20, 1, 2),
    _AcPMSIPSRDOtherDialogsInterval_Type()
)
acPMSIPSRDOtherDialogsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPSRDOtherDialogsInterval.setStatus("current")
_AcPMSIPSRDOtherDialogsVal_Type = Counter32
_AcPMSIPSRDOtherDialogsVal_Object = MibTableColumn
acPMSIPSRDOtherDialogsVal = _AcPMSIPSRDOtherDialogsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 20, 1, 3),
    _AcPMSIPSRDOtherDialogsVal_Type()
)
acPMSIPSRDOtherDialogsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPSRDOtherDialogsVal.setStatus("current")
_AcPMSIPIPGroupDialogsTable_Object = MibTable
acPMSIPIPGroupDialogsTable = _AcPMSIPIPGroupDialogsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 21)
)
if mibBuilder.loadTexts:
    acPMSIPIPGroupDialogsTable.setStatus("current")
_AcPMSIPIPGroupDialogsEntry_Object = MibTableRow
acPMSIPIPGroupDialogsEntry = _AcPMSIPIPGroupDialogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 21, 1)
)
acPMSIPIPGroupDialogsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPIPGroupDialogsIPGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPIPGroupDialogsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPIPGroupDialogsEntry.setStatus("current")


class _AcPMSIPIPGroupDialogsIPGroupNum_Type(Unsigned32):
    """Custom type acPMSIPIPGroupDialogsIPGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33),
    )


_AcPMSIPIPGroupDialogsIPGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupDialogsIPGroupNum_Object = MibTableColumn
acPMSIPIPGroupDialogsIPGroupNum = _AcPMSIPIPGroupDialogsIPGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 21, 1, 1),
    _AcPMSIPIPGroupDialogsIPGroupNum_Type()
)
acPMSIPIPGroupDialogsIPGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIPGroupDialogsIPGroupNum.setStatus("current")


class _AcPMSIPIPGroupDialogsInterval_Type(Unsigned32):
    """Custom type acPMSIPIPGroupDialogsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPIPGroupDialogsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupDialogsInterval_Object = MibTableColumn
acPMSIPIPGroupDialogsInterval = _AcPMSIPIPGroupDialogsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 21, 1, 2),
    _AcPMSIPIPGroupDialogsInterval_Type()
)
acPMSIPIPGroupDialogsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIPGroupDialogsInterval.setStatus("current")
_AcPMSIPIPGroupDialogsVal_Type = Counter32
_AcPMSIPIPGroupDialogsVal_Object = MibTableColumn
acPMSIPIPGroupDialogsVal = _AcPMSIPIPGroupDialogsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 21, 1, 3),
    _AcPMSIPIPGroupDialogsVal_Type()
)
acPMSIPIPGroupDialogsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIPGroupDialogsVal.setStatus("current")
_AcPMSIPIPGroupInviteDialogsTable_Object = MibTable
acPMSIPIPGroupInviteDialogsTable = _AcPMSIPIPGroupInviteDialogsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22)
)
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsTable.setStatus("current")
_AcPMSIPIPGroupInviteDialogsEntry_Object = MibTableRow
acPMSIPIPGroupInviteDialogsEntry = _AcPMSIPIPGroupInviteDialogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22, 1)
)
acPMSIPIPGroupInviteDialogsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPIPGroupInviteDialogsIPGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPIPGroupInviteDialogsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsEntry.setStatus("current")


class _AcPMSIPIPGroupInviteDialogsIPGroupNum_Type(Unsigned32):
    """Custom type acPMSIPIPGroupInviteDialogsIPGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33),
    )


_AcPMSIPIPGroupInviteDialogsIPGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupInviteDialogsIPGroupNum_Object = MibTableColumn
acPMSIPIPGroupInviteDialogsIPGroupNum = _AcPMSIPIPGroupInviteDialogsIPGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22, 1, 1),
    _AcPMSIPIPGroupInviteDialogsIPGroupNum_Type()
)
acPMSIPIPGroupInviteDialogsIPGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsIPGroupNum.setStatus("current")


class _AcPMSIPIPGroupInviteDialogsInterval_Type(Unsigned32):
    """Custom type acPMSIPIPGroupInviteDialogsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPIPGroupInviteDialogsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupInviteDialogsInterval_Object = MibTableColumn
acPMSIPIPGroupInviteDialogsInterval = _AcPMSIPIPGroupInviteDialogsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22, 1, 2),
    _AcPMSIPIPGroupInviteDialogsInterval_Type()
)
acPMSIPIPGroupInviteDialogsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsInterval.setStatus("current")
_AcPMSIPIPGroupInviteDialogsVal_Type = Counter32
_AcPMSIPIPGroupInviteDialogsVal_Object = MibTableColumn
acPMSIPIPGroupInviteDialogsVal = _AcPMSIPIPGroupInviteDialogsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22, 1, 3),
    _AcPMSIPIPGroupInviteDialogsVal_Type()
)
acPMSIPIPGroupInviteDialogsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsVal.setStatus("current")


class _AcPMSIPIPGroupInviteDialogsAverage_Type(Unsigned32):
    """Custom type acPMSIPIPGroupInviteDialogsAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSIPIPGroupInviteDialogsAverage_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupInviteDialogsAverage_Object = MibTableColumn
acPMSIPIPGroupInviteDialogsAverage = _AcPMSIPIPGroupInviteDialogsAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22, 1, 4),
    _AcPMSIPIPGroupInviteDialogsAverage_Type()
)
acPMSIPIPGroupInviteDialogsAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsAverage.setStatus("current")


class _AcPMSIPIPGroupInviteDialogsMax_Type(Unsigned32):
    """Custom type acPMSIPIPGroupInviteDialogsMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSIPIPGroupInviteDialogsMax_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupInviteDialogsMax_Object = MibTableColumn
acPMSIPIPGroupInviteDialogsMax = _AcPMSIPIPGroupInviteDialogsMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22, 1, 5),
    _AcPMSIPIPGroupInviteDialogsMax_Type()
)
acPMSIPIPGroupInviteDialogsMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsMax.setStatus("current")


class _AcPMSIPIPGroupInviteDialogsMin_Type(Unsigned32):
    """Custom type acPMSIPIPGroupInviteDialogsMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSIPIPGroupInviteDialogsMin_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupInviteDialogsMin_Object = MibTableColumn
acPMSIPIPGroupInviteDialogsMin = _AcPMSIPIPGroupInviteDialogsMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22, 1, 6),
    _AcPMSIPIPGroupInviteDialogsMin_Type()
)
acPMSIPIPGroupInviteDialogsMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsMin.setStatus("current")


class _AcPMSIPIPGroupInviteDialogsTimeBelowLowThreshold_Type(Unsigned32):
    """Custom type acPMSIPIPGroupInviteDialogsTimeBelowLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPIPGroupInviteDialogsTimeBelowLowThreshold_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupInviteDialogsTimeBelowLowThreshold_Object = MibTableColumn
acPMSIPIPGroupInviteDialogsTimeBelowLowThreshold = _AcPMSIPIPGroupInviteDialogsTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22, 1, 7),
    _AcPMSIPIPGroupInviteDialogsTimeBelowLowThreshold_Type()
)
acPMSIPIPGroupInviteDialogsTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsTimeBelowLowThreshold.setStatus("current")


class _AcPMSIPIPGroupInviteDialogsTimeBetweenThresholds_Type(Unsigned32):
    """Custom type acPMSIPIPGroupInviteDialogsTimeBetweenThresholds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPIPGroupInviteDialogsTimeBetweenThresholds_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupInviteDialogsTimeBetweenThresholds_Object = MibTableColumn
acPMSIPIPGroupInviteDialogsTimeBetweenThresholds = _AcPMSIPIPGroupInviteDialogsTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22, 1, 8),
    _AcPMSIPIPGroupInviteDialogsTimeBetweenThresholds_Type()
)
acPMSIPIPGroupInviteDialogsTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsTimeBetweenThresholds.setStatus("current")


class _AcPMSIPIPGroupInviteDialogsTimeAboveHighThreshold_Type(Unsigned32):
    """Custom type acPMSIPIPGroupInviteDialogsTimeAboveHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPIPGroupInviteDialogsTimeAboveHighThreshold_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupInviteDialogsTimeAboveHighThreshold_Object = MibTableColumn
acPMSIPIPGroupInviteDialogsTimeAboveHighThreshold = _AcPMSIPIPGroupInviteDialogsTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 22, 1, 9),
    _AcPMSIPIPGroupInviteDialogsTimeAboveHighThreshold_Type()
)
acPMSIPIPGroupInviteDialogsTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIPGroupInviteDialogsTimeAboveHighThreshold.setStatus("current")
_AcPMSIPIPGroupSubscribeDialogsTable_Object = MibTable
acPMSIPIPGroupSubscribeDialogsTable = _AcPMSIPIPGroupSubscribeDialogsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 23)
)
if mibBuilder.loadTexts:
    acPMSIPIPGroupSubscribeDialogsTable.setStatus("current")
_AcPMSIPIPGroupSubscribeDialogsEntry_Object = MibTableRow
acPMSIPIPGroupSubscribeDialogsEntry = _AcPMSIPIPGroupSubscribeDialogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 23, 1)
)
acPMSIPIPGroupSubscribeDialogsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPIPGroupSubscribeDialogsIPGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPIPGroupSubscribeDialogsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPIPGroupSubscribeDialogsEntry.setStatus("current")


class _AcPMSIPIPGroupSubscribeDialogsIPGroupNum_Type(Unsigned32):
    """Custom type acPMSIPIPGroupSubscribeDialogsIPGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33),
    )


_AcPMSIPIPGroupSubscribeDialogsIPGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupSubscribeDialogsIPGroupNum_Object = MibTableColumn
acPMSIPIPGroupSubscribeDialogsIPGroupNum = _AcPMSIPIPGroupSubscribeDialogsIPGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 23, 1, 1),
    _AcPMSIPIPGroupSubscribeDialogsIPGroupNum_Type()
)
acPMSIPIPGroupSubscribeDialogsIPGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIPGroupSubscribeDialogsIPGroupNum.setStatus("current")


class _AcPMSIPIPGroupSubscribeDialogsInterval_Type(Unsigned32):
    """Custom type acPMSIPIPGroupSubscribeDialogsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPIPGroupSubscribeDialogsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupSubscribeDialogsInterval_Object = MibTableColumn
acPMSIPIPGroupSubscribeDialogsInterval = _AcPMSIPIPGroupSubscribeDialogsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 23, 1, 2),
    _AcPMSIPIPGroupSubscribeDialogsInterval_Type()
)
acPMSIPIPGroupSubscribeDialogsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIPGroupSubscribeDialogsInterval.setStatus("current")
_AcPMSIPIPGroupSubscribeDialogsVal_Type = Counter32
_AcPMSIPIPGroupSubscribeDialogsVal_Object = MibTableColumn
acPMSIPIPGroupSubscribeDialogsVal = _AcPMSIPIPGroupSubscribeDialogsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 23, 1, 3),
    _AcPMSIPIPGroupSubscribeDialogsVal_Type()
)
acPMSIPIPGroupSubscribeDialogsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIPGroupSubscribeDialogsVal.setStatus("current")
_AcPMSIPIPGroupOtherDialogsTable_Object = MibTable
acPMSIPIPGroupOtherDialogsTable = _AcPMSIPIPGroupOtherDialogsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 24)
)
if mibBuilder.loadTexts:
    acPMSIPIPGroupOtherDialogsTable.setStatus("current")
_AcPMSIPIPGroupOtherDialogsEntry_Object = MibTableRow
acPMSIPIPGroupOtherDialogsEntry = _AcPMSIPIPGroupOtherDialogsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 24, 1)
)
acPMSIPIPGroupOtherDialogsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPIPGroupOtherDialogsIPGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPIPGroupOtherDialogsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPIPGroupOtherDialogsEntry.setStatus("current")


class _AcPMSIPIPGroupOtherDialogsIPGroupNum_Type(Unsigned32):
    """Custom type acPMSIPIPGroupOtherDialogsIPGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 33),
    )


_AcPMSIPIPGroupOtherDialogsIPGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupOtherDialogsIPGroupNum_Object = MibTableColumn
acPMSIPIPGroupOtherDialogsIPGroupNum = _AcPMSIPIPGroupOtherDialogsIPGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 24, 1, 1),
    _AcPMSIPIPGroupOtherDialogsIPGroupNum_Type()
)
acPMSIPIPGroupOtherDialogsIPGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIPGroupOtherDialogsIPGroupNum.setStatus("current")


class _AcPMSIPIPGroupOtherDialogsInterval_Type(Unsigned32):
    """Custom type acPMSIPIPGroupOtherDialogsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPIPGroupOtherDialogsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPIPGroupOtherDialogsInterval_Object = MibTableColumn
acPMSIPIPGroupOtherDialogsInterval = _AcPMSIPIPGroupOtherDialogsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 24, 1, 2),
    _AcPMSIPIPGroupOtherDialogsInterval_Type()
)
acPMSIPIPGroupOtherDialogsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPIPGroupOtherDialogsInterval.setStatus("current")
_AcPMSIPIPGroupOtherDialogsVal_Type = Counter32
_AcPMSIPIPGroupOtherDialogsVal_Object = MibTableColumn
acPMSIPIPGroupOtherDialogsVal = _AcPMSIPIPGroupOtherDialogsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 24, 1, 3),
    _AcPMSIPIPGroupOtherDialogsVal_Type()
)
acPMSIPIPGroupOtherDialogsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPIPGroupOtherDialogsVal.setStatus("current")
_AcPMSIPTrunkGroupAllTrunksBusyTable_Object = MibTable
acPMSIPTrunkGroupAllTrunksBusyTable = _AcPMSIPTrunkGroupAllTrunksBusyTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 25)
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupAllTrunksBusyTable.setStatus("current")
_AcPMSIPTrunkGroupAllTrunksBusyEntry_Object = MibTableRow
acPMSIPTrunkGroupAllTrunksBusyEntry = _AcPMSIPTrunkGroupAllTrunksBusyEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 25, 1)
)
acPMSIPTrunkGroupAllTrunksBusyEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupAllTrunksBusyInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupAllTrunksBusyEntry.setStatus("current")


class _AcPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum_Object = MibTableColumn
acPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum = _AcPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 25, 1, 1),
    _AcPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum_Type()
)
acPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum.setStatus("current")


class _AcPMSIPTrunkGroupAllTrunksBusyInterval_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupAllTrunksBusyInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPTrunkGroupAllTrunksBusyInterval_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupAllTrunksBusyInterval_Object = MibTableColumn
acPMSIPTrunkGroupAllTrunksBusyInterval = _AcPMSIPTrunkGroupAllTrunksBusyInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 25, 1, 2),
    _AcPMSIPTrunkGroupAllTrunksBusyInterval_Type()
)
acPMSIPTrunkGroupAllTrunksBusyInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupAllTrunksBusyInterval.setStatus("current")
_AcPMSIPTrunkGroupAllTrunksBusyVal_Type = Counter32
_AcPMSIPTrunkGroupAllTrunksBusyVal_Object = MibTableColumn
acPMSIPTrunkGroupAllTrunksBusyVal = _AcPMSIPTrunkGroupAllTrunksBusyVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 25, 1, 3),
    _AcPMSIPTrunkGroupAllTrunksBusyVal_Type()
)
acPMSIPTrunkGroupAllTrunksBusyVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupAllTrunksBusyVal.setStatus("current")
_AcPMSIPTrunkGroupUtilizationTable_Object = MibTable
acPMSIPTrunkGroupUtilizationTable = _AcPMSIPTrunkGroupUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26)
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationTable.setStatus("current")
_AcPMSIPTrunkGroupUtilizationEntry_Object = MibTableRow
acPMSIPTrunkGroupUtilizationEntry = _AcPMSIPTrunkGroupUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1)
)
acPMSIPTrunkGroupUtilizationEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupUtilizationTrunkGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupUtilizationInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationEntry.setStatus("current")


class _AcPMSIPTrunkGroupUtilizationTrunkGroupNum_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupUtilizationTrunkGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMSIPTrunkGroupUtilizationTrunkGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupUtilizationTrunkGroupNum_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationTrunkGroupNum = _AcPMSIPTrunkGroupUtilizationTrunkGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 1),
    _AcPMSIPTrunkGroupUtilizationTrunkGroupNum_Type()
)
acPMSIPTrunkGroupUtilizationTrunkGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationTrunkGroupNum.setStatus("current")


class _AcPMSIPTrunkGroupUtilizationInterval_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupUtilizationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPTrunkGroupUtilizationInterval_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupUtilizationInterval_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationInterval = _AcPMSIPTrunkGroupUtilizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 2),
    _AcPMSIPTrunkGroupUtilizationInterval_Type()
)
acPMSIPTrunkGroupUtilizationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationInterval.setStatus("current")
_AcPMSIPTrunkGroupUtilizationVal_Type = Gauge32
_AcPMSIPTrunkGroupUtilizationVal_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationVal = _AcPMSIPTrunkGroupUtilizationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 3),
    _AcPMSIPTrunkGroupUtilizationVal_Type()
)
acPMSIPTrunkGroupUtilizationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationVal.setStatus("current")


class _AcPMSIPTrunkGroupUtilizationTimeBelowLowThreshold_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupUtilizationTimeBelowLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPTrunkGroupUtilizationTimeBelowLowThreshold_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupUtilizationTimeBelowLowThreshold_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationTimeBelowLowThreshold = _AcPMSIPTrunkGroupUtilizationTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 4),
    _AcPMSIPTrunkGroupUtilizationTimeBelowLowThreshold_Type()
)
acPMSIPTrunkGroupUtilizationTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationTimeBelowLowThreshold.setStatus("current")


class _AcPMSIPTrunkGroupUtilizationTimeBetweenThresholds_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupUtilizationTimeBetweenThresholds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPTrunkGroupUtilizationTimeBetweenThresholds_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupUtilizationTimeBetweenThresholds_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationTimeBetweenThresholds = _AcPMSIPTrunkGroupUtilizationTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 5),
    _AcPMSIPTrunkGroupUtilizationTimeBetweenThresholds_Type()
)
acPMSIPTrunkGroupUtilizationTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationTimeBetweenThresholds.setStatus("current")


class _AcPMSIPTrunkGroupUtilizationTimeAboveHighThreshold_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupUtilizationTimeAboveHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPTrunkGroupUtilizationTimeAboveHighThreshold_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupUtilizationTimeAboveHighThreshold_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationTimeAboveHighThreshold = _AcPMSIPTrunkGroupUtilizationTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 6),
    _AcPMSIPTrunkGroupUtilizationTimeAboveHighThreshold_Type()
)
acPMSIPTrunkGroupUtilizationTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationTimeAboveHighThreshold.setStatus("current")


class _AcPMSIPTrunkGroupUtilizationAverage_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupUtilizationAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2016),
    )


_AcPMSIPTrunkGroupUtilizationAverage_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupUtilizationAverage_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationAverage = _AcPMSIPTrunkGroupUtilizationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 7),
    _AcPMSIPTrunkGroupUtilizationAverage_Type()
)
acPMSIPTrunkGroupUtilizationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationAverage.setStatus("current")


class _AcPMSIPTrunkGroupUtilizationMax_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupUtilizationMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2016),
    )


_AcPMSIPTrunkGroupUtilizationMax_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupUtilizationMax_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationMax = _AcPMSIPTrunkGroupUtilizationMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 8),
    _AcPMSIPTrunkGroupUtilizationMax_Type()
)
acPMSIPTrunkGroupUtilizationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationMax.setStatus("current")


class _AcPMSIPTrunkGroupUtilizationMin_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupUtilizationMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2016),
    )


_AcPMSIPTrunkGroupUtilizationMin_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupUtilizationMin_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationMin = _AcPMSIPTrunkGroupUtilizationMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 9),
    _AcPMSIPTrunkGroupUtilizationMin_Type()
)
acPMSIPTrunkGroupUtilizationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationMin.setStatus("current")
_AcPMSIPTrunkGroupUtilizationTotal_Type = Counter32
_AcPMSIPTrunkGroupUtilizationTotal_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationTotal = _AcPMSIPTrunkGroupUtilizationTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 10),
    _AcPMSIPTrunkGroupUtilizationTotal_Type()
)
acPMSIPTrunkGroupUtilizationTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationTotal.setStatus("current")


class _AcPMSIPTrunkGroupUtilizationFullDayAverage_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupUtilizationFullDayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2016),
    )


_AcPMSIPTrunkGroupUtilizationFullDayAverage_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupUtilizationFullDayAverage_Object = MibTableColumn
acPMSIPTrunkGroupUtilizationFullDayAverage = _AcPMSIPTrunkGroupUtilizationFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 26, 1, 11),
    _AcPMSIPTrunkGroupUtilizationFullDayAverage_Type()
)
acPMSIPTrunkGroupUtilizationFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupUtilizationFullDayAverage.setStatus("current")
_AcPMSIPTrunkGroupPercentageUtilizationTable_Object = MibTable
acPMSIPTrunkGroupPercentageUtilizationTable = _AcPMSIPTrunkGroupPercentageUtilizationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27)
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationTable.setStatus("current")
_AcPMSIPTrunkGroupPercentageUtilizationEntry_Object = MibTableRow
acPMSIPTrunkGroupPercentageUtilizationEntry = _AcPMSIPTrunkGroupPercentageUtilizationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1)
)
acPMSIPTrunkGroupPercentageUtilizationEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupPercentageUtilizationInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationEntry.setStatus("current")


class _AcPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum_Object = MibTableColumn
acPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum = _AcPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1, 1),
    _AcPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum_Type()
)
acPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum.setStatus("current")


class _AcPMSIPTrunkGroupPercentageUtilizationInterval_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupPercentageUtilizationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPTrunkGroupPercentageUtilizationInterval_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupPercentageUtilizationInterval_Object = MibTableColumn
acPMSIPTrunkGroupPercentageUtilizationInterval = _AcPMSIPTrunkGroupPercentageUtilizationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1, 2),
    _AcPMSIPTrunkGroupPercentageUtilizationInterval_Type()
)
acPMSIPTrunkGroupPercentageUtilizationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationInterval.setStatus("current")
_AcPMSIPTrunkGroupPercentageUtilizationVal_Type = Gauge32
_AcPMSIPTrunkGroupPercentageUtilizationVal_Object = MibTableColumn
acPMSIPTrunkGroupPercentageUtilizationVal = _AcPMSIPTrunkGroupPercentageUtilizationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1, 3),
    _AcPMSIPTrunkGroupPercentageUtilizationVal_Type()
)
acPMSIPTrunkGroupPercentageUtilizationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationVal.setStatus("current")


class _AcPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold_Object = MibTableColumn
acPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold = _AcPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1, 4),
    _AcPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold_Type()
)
acPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold.setStatus("current")


class _AcPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds_Object = MibTableColumn
acPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds = _AcPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1, 5),
    _AcPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds_Type()
)
acPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds.setStatus("current")


class _AcPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold_Object = MibTableColumn
acPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold = _AcPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1, 6),
    _AcPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold_Type()
)
acPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold.setStatus("current")


class _AcPMSIPTrunkGroupPercentageUtilizationAverage_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupPercentageUtilizationAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPTrunkGroupPercentageUtilizationAverage_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupPercentageUtilizationAverage_Object = MibTableColumn
acPMSIPTrunkGroupPercentageUtilizationAverage = _AcPMSIPTrunkGroupPercentageUtilizationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1, 7),
    _AcPMSIPTrunkGroupPercentageUtilizationAverage_Type()
)
acPMSIPTrunkGroupPercentageUtilizationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationAverage.setStatus("current")


class _AcPMSIPTrunkGroupPercentageUtilizationMax_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupPercentageUtilizationMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPTrunkGroupPercentageUtilizationMax_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupPercentageUtilizationMax_Object = MibTableColumn
acPMSIPTrunkGroupPercentageUtilizationMax = _AcPMSIPTrunkGroupPercentageUtilizationMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1, 8),
    _AcPMSIPTrunkGroupPercentageUtilizationMax_Type()
)
acPMSIPTrunkGroupPercentageUtilizationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationMax.setStatus("current")


class _AcPMSIPTrunkGroupPercentageUtilizationMin_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupPercentageUtilizationMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPTrunkGroupPercentageUtilizationMin_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupPercentageUtilizationMin_Object = MibTableColumn
acPMSIPTrunkGroupPercentageUtilizationMin = _AcPMSIPTrunkGroupPercentageUtilizationMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1, 9),
    _AcPMSIPTrunkGroupPercentageUtilizationMin_Type()
)
acPMSIPTrunkGroupPercentageUtilizationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationMin.setStatus("current")


class _AcPMSIPTrunkGroupPercentageUtilizationFullDayAverage_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupPercentageUtilizationFullDayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_AcPMSIPTrunkGroupPercentageUtilizationFullDayAverage_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupPercentageUtilizationFullDayAverage_Object = MibTableColumn
acPMSIPTrunkGroupPercentageUtilizationFullDayAverage = _AcPMSIPTrunkGroupPercentageUtilizationFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 27, 1, 10),
    _AcPMSIPTrunkGroupPercentageUtilizationFullDayAverage_Type()
)
acPMSIPTrunkGroupPercentageUtilizationFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupPercentageUtilizationFullDayAverage.setStatus("current")
_AcPMSIPTrunkGroupNoResourcesCallsTable_Object = MibTable
acPMSIPTrunkGroupNoResourcesCallsTable = _AcPMSIPTrunkGroupNoResourcesCallsTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 28)
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupNoResourcesCallsTable.setStatus("current")
_AcPMSIPTrunkGroupNoResourcesCallsEntry_Object = MibTableRow
acPMSIPTrunkGroupNoResourcesCallsEntry = _AcPMSIPTrunkGroupNoResourcesCallsEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 28, 1)
)
acPMSIPTrunkGroupNoResourcesCallsEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupNoResourcesCallsInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupNoResourcesCallsEntry.setStatus("current")


class _AcPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum_Object = MibTableColumn
acPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum = _AcPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 28, 1, 1),
    _AcPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum_Type()
)
acPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum.setStatus("current")


class _AcPMSIPTrunkGroupNoResourcesCallsInterval_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupNoResourcesCallsInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPTrunkGroupNoResourcesCallsInterval_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupNoResourcesCallsInterval_Object = MibTableColumn
acPMSIPTrunkGroupNoResourcesCallsInterval = _AcPMSIPTrunkGroupNoResourcesCallsInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 28, 1, 2),
    _AcPMSIPTrunkGroupNoResourcesCallsInterval_Type()
)
acPMSIPTrunkGroupNoResourcesCallsInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupNoResourcesCallsInterval.setStatus("current")
_AcPMSIPTrunkGroupNoResourcesCallsVal_Type = Counter32
_AcPMSIPTrunkGroupNoResourcesCallsVal_Object = MibTableColumn
acPMSIPTrunkGroupNoResourcesCallsVal = _AcPMSIPTrunkGroupNoResourcesCallsVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 28, 1, 3),
    _AcPMSIPTrunkGroupNoResourcesCallsVal_Type()
)
acPMSIPTrunkGroupNoResourcesCallsVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupNoResourcesCallsVal.setStatus("current")
_AcPMSIPTrunkGroupNoResourcesCallsTotal_Type = Counter32
_AcPMSIPTrunkGroupNoResourcesCallsTotal_Object = MibTableColumn
acPMSIPTrunkGroupNoResourcesCallsTotal = _AcPMSIPTrunkGroupNoResourcesCallsTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 28, 1, 4),
    _AcPMSIPTrunkGroupNoResourcesCallsTotal_Type()
)
acPMSIPTrunkGroupNoResourcesCallsTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupNoResourcesCallsTotal.setStatus("current")
_AcPMSIPTrunkGroupCallDurationTable_Object = MibTable
acPMSIPTrunkGroupCallDurationTable = _AcPMSIPTrunkGroupCallDurationTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 29)
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupCallDurationTable.setStatus("current")
_AcPMSIPTrunkGroupCallDurationEntry_Object = MibTableRow
acPMSIPTrunkGroupCallDurationEntry = _AcPMSIPTrunkGroupCallDurationEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 29, 1)
)
acPMSIPTrunkGroupCallDurationEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupCallDurationTrunkGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupCallDurationInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupCallDurationEntry.setStatus("current")


class _AcPMSIPTrunkGroupCallDurationTrunkGroupNum_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupCallDurationTrunkGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMSIPTrunkGroupCallDurationTrunkGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupCallDurationTrunkGroupNum_Object = MibTableColumn
acPMSIPTrunkGroupCallDurationTrunkGroupNum = _AcPMSIPTrunkGroupCallDurationTrunkGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 29, 1, 1),
    _AcPMSIPTrunkGroupCallDurationTrunkGroupNum_Type()
)
acPMSIPTrunkGroupCallDurationTrunkGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupCallDurationTrunkGroupNum.setStatus("current")


class _AcPMSIPTrunkGroupCallDurationInterval_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupCallDurationInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPTrunkGroupCallDurationInterval_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupCallDurationInterval_Object = MibTableColumn
acPMSIPTrunkGroupCallDurationInterval = _AcPMSIPTrunkGroupCallDurationInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 29, 1, 2),
    _AcPMSIPTrunkGroupCallDurationInterval_Type()
)
acPMSIPTrunkGroupCallDurationInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupCallDurationInterval.setStatus("current")
_AcPMSIPTrunkGroupCallDurationVal_Type = Gauge32
_AcPMSIPTrunkGroupCallDurationVal_Object = MibTableColumn
acPMSIPTrunkGroupCallDurationVal = _AcPMSIPTrunkGroupCallDurationVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 29, 1, 3),
    _AcPMSIPTrunkGroupCallDurationVal_Type()
)
acPMSIPTrunkGroupCallDurationVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupCallDurationVal.setStatus("current")


class _AcPMSIPTrunkGroupCallDurationAverage_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupCallDurationAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSIPTrunkGroupCallDurationAverage_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupCallDurationAverage_Object = MibTableColumn
acPMSIPTrunkGroupCallDurationAverage = _AcPMSIPTrunkGroupCallDurationAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 29, 1, 4),
    _AcPMSIPTrunkGroupCallDurationAverage_Type()
)
acPMSIPTrunkGroupCallDurationAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupCallDurationAverage.setStatus("current")


class _AcPMSIPTrunkGroupCallDurationMax_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupCallDurationMax based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSIPTrunkGroupCallDurationMax_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupCallDurationMax_Object = MibTableColumn
acPMSIPTrunkGroupCallDurationMax = _AcPMSIPTrunkGroupCallDurationMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 29, 1, 5),
    _AcPMSIPTrunkGroupCallDurationMax_Type()
)
acPMSIPTrunkGroupCallDurationMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupCallDurationMax.setStatus("current")


class _AcPMSIPTrunkGroupCallDurationMin_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupCallDurationMin based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSIPTrunkGroupCallDurationMin_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupCallDurationMin_Object = MibTableColumn
acPMSIPTrunkGroupCallDurationMin = _AcPMSIPTrunkGroupCallDurationMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 29, 1, 6),
    _AcPMSIPTrunkGroupCallDurationMin_Type()
)
acPMSIPTrunkGroupCallDurationMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupCallDurationMin.setStatus("current")
_AcPMSIPTrunkGroupCallDurationTotal_Type = Counter32
_AcPMSIPTrunkGroupCallDurationTotal_Object = MibTableColumn
acPMSIPTrunkGroupCallDurationTotal = _AcPMSIPTrunkGroupCallDurationTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 29, 1, 7),
    _AcPMSIPTrunkGroupCallDurationTotal_Type()
)
acPMSIPTrunkGroupCallDurationTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupCallDurationTotal.setStatus("current")


class _AcPMSIPTrunkGroupCallDurationFullDayAverage_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupCallDurationFullDayAverage based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AcPMSIPTrunkGroupCallDurationFullDayAverage_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupCallDurationFullDayAverage_Object = MibTableColumn
acPMSIPTrunkGroupCallDurationFullDayAverage = _AcPMSIPTrunkGroupCallDurationFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 29, 1, 8),
    _AcPMSIPTrunkGroupCallDurationFullDayAverage_Type()
)
acPMSIPTrunkGroupCallDurationFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupCallDurationFullDayAverage.setStatus("current")
_AcPMSIPTrunkGroupAllTrunksBusyPercentageTable_Object = MibTable
acPMSIPTrunkGroupAllTrunksBusyPercentageTable = _AcPMSIPTrunkGroupAllTrunksBusyPercentageTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 40)
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupAllTrunksBusyPercentageTable.setStatus("current")
_AcPMSIPTrunkGroupAllTrunksBusyPercentageEntry_Object = MibTableRow
acPMSIPTrunkGroupAllTrunksBusyPercentageEntry = _AcPMSIPTrunkGroupAllTrunksBusyPercentageEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 40, 1)
)
acPMSIPTrunkGroupAllTrunksBusyPercentageEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum"),
    (0, "AC-PM-Control-MIB", "acPMSIPTrunkGroupAllTrunksBusyPercentageInterval"),
)
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupAllTrunksBusyPercentageEntry.setStatus("current")


class _AcPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 83),
    )


_AcPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum_Object = MibTableColumn
acPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum = _AcPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 40, 1, 1),
    _AcPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum_Type()
)
acPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum.setStatus("current")


class _AcPMSIPTrunkGroupAllTrunksBusyPercentageInterval_Type(Unsigned32):
    """Custom type acPMSIPTrunkGroupAllTrunksBusyPercentageInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMSIPTrunkGroupAllTrunksBusyPercentageInterval_Type.__name__ = "Unsigned32"
_AcPMSIPTrunkGroupAllTrunksBusyPercentageInterval_Object = MibTableColumn
acPMSIPTrunkGroupAllTrunksBusyPercentageInterval = _AcPMSIPTrunkGroupAllTrunksBusyPercentageInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 40, 1, 2),
    _AcPMSIPTrunkGroupAllTrunksBusyPercentageInterval_Type()
)
acPMSIPTrunkGroupAllTrunksBusyPercentageInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupAllTrunksBusyPercentageInterval.setStatus("current")
_AcPMSIPTrunkGroupAllTrunksBusyPercentageVal_Type = Gauge32
_AcPMSIPTrunkGroupAllTrunksBusyPercentageVal_Object = MibTableColumn
acPMSIPTrunkGroupAllTrunksBusyPercentageVal = _AcPMSIPTrunkGroupAllTrunksBusyPercentageVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 52, 40, 1, 3),
    _AcPMSIPTrunkGroupAllTrunksBusyPercentageVal_Type()
)
acPMSIPTrunkGroupAllTrunksBusyPercentageVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMSIPTrunkGroupAllTrunksBusyPercentageVal.setStatus("current")
_AcPMMediaRealm_ObjectIdentity = ObjectIdentity
acPMMediaRealm = _AcPMMediaRealm_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53)
)
_AcPMMediaRealmBytesTxTable_Object = MibTable
acPMMediaRealmBytesTxTable = _AcPMMediaRealmBytesTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 1)
)
if mibBuilder.loadTexts:
    acPMMediaRealmBytesTxTable.setStatus("current")
_AcPMMediaRealmBytesTxEntry_Object = MibTableRow
acPMMediaRealmBytesTxEntry = _AcPMMediaRealmBytesTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 1, 1)
)
acPMMediaRealmBytesTxEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmBytesTxMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmBytesTxInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmBytesTxEntry.setStatus("current")


class _AcPMMediaRealmBytesTxMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmBytesTxMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmBytesTxMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmBytesTxMediaRealmNum_Object = MibTableColumn
acPMMediaRealmBytesTxMediaRealmNum = _AcPMMediaRealmBytesTxMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 1, 1, 1),
    _AcPMMediaRealmBytesTxMediaRealmNum_Type()
)
acPMMediaRealmBytesTxMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmBytesTxMediaRealmNum.setStatus("current")


class _AcPMMediaRealmBytesTxInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmBytesTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmBytesTxInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmBytesTxInterval_Object = MibTableColumn
acPMMediaRealmBytesTxInterval = _AcPMMediaRealmBytesTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 1, 1, 2),
    _AcPMMediaRealmBytesTxInterval_Type()
)
acPMMediaRealmBytesTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmBytesTxInterval.setStatus("current")
_AcPMMediaRealmBytesTxVal_Type = Counter32
_AcPMMediaRealmBytesTxVal_Object = MibTableColumn
acPMMediaRealmBytesTxVal = _AcPMMediaRealmBytesTxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 1, 1, 3),
    _AcPMMediaRealmBytesTxVal_Type()
)
acPMMediaRealmBytesTxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBytesTxVal.setStatus("current")
_AcPMMediaRealmBytesTxVolume_Type = Counter32
_AcPMMediaRealmBytesTxVolume_Object = MibTableColumn
acPMMediaRealmBytesTxVolume = _AcPMMediaRealmBytesTxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 1, 1, 4),
    _AcPMMediaRealmBytesTxVolume_Type()
)
acPMMediaRealmBytesTxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBytesTxVolume.setStatus("current")
_AcPMMediaRealmBytesRxTable_Object = MibTable
acPMMediaRealmBytesRxTable = _AcPMMediaRealmBytesRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 2)
)
if mibBuilder.loadTexts:
    acPMMediaRealmBytesRxTable.setStatus("current")
_AcPMMediaRealmBytesRxEntry_Object = MibTableRow
acPMMediaRealmBytesRxEntry = _AcPMMediaRealmBytesRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 2, 1)
)
acPMMediaRealmBytesRxEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmBytesRxMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmBytesRxInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmBytesRxEntry.setStatus("current")


class _AcPMMediaRealmBytesRxMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmBytesRxMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmBytesRxMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmBytesRxMediaRealmNum_Object = MibTableColumn
acPMMediaRealmBytesRxMediaRealmNum = _AcPMMediaRealmBytesRxMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 2, 1, 1),
    _AcPMMediaRealmBytesRxMediaRealmNum_Type()
)
acPMMediaRealmBytesRxMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmBytesRxMediaRealmNum.setStatus("current")


class _AcPMMediaRealmBytesRxInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmBytesRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmBytesRxInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmBytesRxInterval_Object = MibTableColumn
acPMMediaRealmBytesRxInterval = _AcPMMediaRealmBytesRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 2, 1, 2),
    _AcPMMediaRealmBytesRxInterval_Type()
)
acPMMediaRealmBytesRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmBytesRxInterval.setStatus("current")
_AcPMMediaRealmBytesRxVal_Type = Counter32
_AcPMMediaRealmBytesRxVal_Object = MibTableColumn
acPMMediaRealmBytesRxVal = _AcPMMediaRealmBytesRxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 2, 1, 3),
    _AcPMMediaRealmBytesRxVal_Type()
)
acPMMediaRealmBytesRxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBytesRxVal.setStatus("current")
_AcPMMediaRealmBytesRxVolume_Type = Counter32
_AcPMMediaRealmBytesRxVolume_Object = MibTableColumn
acPMMediaRealmBytesRxVolume = _AcPMMediaRealmBytesRxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 2, 1, 4),
    _AcPMMediaRealmBytesRxVolume_Type()
)
acPMMediaRealmBytesRxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBytesRxVolume.setStatus("current")
_AcPMMediaRealmPacketsTxTable_Object = MibTable
acPMMediaRealmPacketsTxTable = _AcPMMediaRealmPacketsTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 3)
)
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsTxTable.setStatus("current")
_AcPMMediaRealmPacketsTxEntry_Object = MibTableRow
acPMMediaRealmPacketsTxEntry = _AcPMMediaRealmPacketsTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 3, 1)
)
acPMMediaRealmPacketsTxEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmPacketsTxMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmPacketsTxInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsTxEntry.setStatus("current")


class _AcPMMediaRealmPacketsTxMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmPacketsTxMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmPacketsTxMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmPacketsTxMediaRealmNum_Object = MibTableColumn
acPMMediaRealmPacketsTxMediaRealmNum = _AcPMMediaRealmPacketsTxMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 3, 1, 1),
    _AcPMMediaRealmPacketsTxMediaRealmNum_Type()
)
acPMMediaRealmPacketsTxMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsTxMediaRealmNum.setStatus("current")


class _AcPMMediaRealmPacketsTxInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmPacketsTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmPacketsTxInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmPacketsTxInterval_Object = MibTableColumn
acPMMediaRealmPacketsTxInterval = _AcPMMediaRealmPacketsTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 3, 1, 2),
    _AcPMMediaRealmPacketsTxInterval_Type()
)
acPMMediaRealmPacketsTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsTxInterval.setStatus("current")
_AcPMMediaRealmPacketsTxVal_Type = Counter32
_AcPMMediaRealmPacketsTxVal_Object = MibTableColumn
acPMMediaRealmPacketsTxVal = _AcPMMediaRealmPacketsTxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 3, 1, 3),
    _AcPMMediaRealmPacketsTxVal_Type()
)
acPMMediaRealmPacketsTxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsTxVal.setStatus("current")
_AcPMMediaRealmPacketsTxVolume_Type = Counter32
_AcPMMediaRealmPacketsTxVolume_Object = MibTableColumn
acPMMediaRealmPacketsTxVolume = _AcPMMediaRealmPacketsTxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 3, 1, 4),
    _AcPMMediaRealmPacketsTxVolume_Type()
)
acPMMediaRealmPacketsTxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsTxVolume.setStatus("current")
_AcPMMediaRealmPacketsRxTable_Object = MibTable
acPMMediaRealmPacketsRxTable = _AcPMMediaRealmPacketsRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 4)
)
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsRxTable.setStatus("current")
_AcPMMediaRealmPacketsRxEntry_Object = MibTableRow
acPMMediaRealmPacketsRxEntry = _AcPMMediaRealmPacketsRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 4, 1)
)
acPMMediaRealmPacketsRxEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmPacketsRxMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmPacketsRxInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsRxEntry.setStatus("current")


class _AcPMMediaRealmPacketsRxMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmPacketsRxMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmPacketsRxMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmPacketsRxMediaRealmNum_Object = MibTableColumn
acPMMediaRealmPacketsRxMediaRealmNum = _AcPMMediaRealmPacketsRxMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 4, 1, 1),
    _AcPMMediaRealmPacketsRxMediaRealmNum_Type()
)
acPMMediaRealmPacketsRxMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsRxMediaRealmNum.setStatus("current")


class _AcPMMediaRealmPacketsRxInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmPacketsRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmPacketsRxInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmPacketsRxInterval_Object = MibTableColumn
acPMMediaRealmPacketsRxInterval = _AcPMMediaRealmPacketsRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 4, 1, 2),
    _AcPMMediaRealmPacketsRxInterval_Type()
)
acPMMediaRealmPacketsRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsRxInterval.setStatus("current")
_AcPMMediaRealmPacketsRxVal_Type = Counter32
_AcPMMediaRealmPacketsRxVal_Object = MibTableColumn
acPMMediaRealmPacketsRxVal = _AcPMMediaRealmPacketsRxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 4, 1, 3),
    _AcPMMediaRealmPacketsRxVal_Type()
)
acPMMediaRealmPacketsRxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsRxVal.setStatus("current")
_AcPMMediaRealmPacketsRxVolume_Type = Counter32
_AcPMMediaRealmPacketsRxVolume_Object = MibTableColumn
acPMMediaRealmPacketsRxVolume = _AcPMMediaRealmPacketsRxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 4, 1, 4),
    _AcPMMediaRealmPacketsRxVolume_Type()
)
acPMMediaRealmPacketsRxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketsRxVolume.setStatus("current")
_AcPMMediaRealmVERealmPacketDelayTable_Object = MibTable
acPMMediaRealmVERealmPacketDelayTable = _AcPMMediaRealmVERealmPacketDelayTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 5)
)
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketDelayTable.setStatus("current")
_AcPMMediaRealmVERealmPacketDelayEntry_Object = MibTableRow
acPMMediaRealmVERealmPacketDelayEntry = _AcPMMediaRealmVERealmPacketDelayEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 5, 1)
)
acPMMediaRealmVERealmPacketDelayEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmVERealmPacketDelayMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmVERealmPacketDelayInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketDelayEntry.setStatus("current")


class _AcPMMediaRealmVERealmPacketDelayMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmVERealmPacketDelayMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmVERealmPacketDelayMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmVERealmPacketDelayMediaRealmNum_Object = MibTableColumn
acPMMediaRealmVERealmPacketDelayMediaRealmNum = _AcPMMediaRealmVERealmPacketDelayMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 5, 1, 1),
    _AcPMMediaRealmVERealmPacketDelayMediaRealmNum_Type()
)
acPMMediaRealmVERealmPacketDelayMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketDelayMediaRealmNum.setStatus("current")


class _AcPMMediaRealmVERealmPacketDelayInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmVERealmPacketDelayInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmVERealmPacketDelayInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmVERealmPacketDelayInterval_Object = MibTableColumn
acPMMediaRealmVERealmPacketDelayInterval = _AcPMMediaRealmVERealmPacketDelayInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 5, 1, 2),
    _AcPMMediaRealmVERealmPacketDelayInterval_Type()
)
acPMMediaRealmVERealmPacketDelayInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketDelayInterval.setStatus("current")
_AcPMMediaRealmVERealmPacketDelayVal_Type = Counter32
_AcPMMediaRealmVERealmPacketDelayVal_Object = MibTableColumn
acPMMediaRealmVERealmPacketDelayVal = _AcPMMediaRealmVERealmPacketDelayVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 5, 1, 3),
    _AcPMMediaRealmVERealmPacketDelayVal_Type()
)
acPMMediaRealmVERealmPacketDelayVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketDelayVal.setStatus("current")


class _AcPMMediaRealmVERealmPacketDelayAverage_Type(Integer32):
    """Custom type acPMMediaRealmVERealmPacketDelayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmVERealmPacketDelayAverage_Type.__name__ = "Integer32"
_AcPMMediaRealmVERealmPacketDelayAverage_Object = MibTableColumn
acPMMediaRealmVERealmPacketDelayAverage = _AcPMMediaRealmVERealmPacketDelayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 5, 1, 4),
    _AcPMMediaRealmVERealmPacketDelayAverage_Type()
)
acPMMediaRealmVERealmPacketDelayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketDelayAverage.setStatus("current")


class _AcPMMediaRealmVERealmPacketDelayMax_Type(Integer32):
    """Custom type acPMMediaRealmVERealmPacketDelayMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmVERealmPacketDelayMax_Type.__name__ = "Integer32"
_AcPMMediaRealmVERealmPacketDelayMax_Object = MibTableColumn
acPMMediaRealmVERealmPacketDelayMax = _AcPMMediaRealmVERealmPacketDelayMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 5, 1, 5),
    _AcPMMediaRealmVERealmPacketDelayMax_Type()
)
acPMMediaRealmVERealmPacketDelayMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketDelayMax.setStatus("current")


class _AcPMMediaRealmVERealmPacketDelayMin_Type(Integer32):
    """Custom type acPMMediaRealmVERealmPacketDelayMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmVERealmPacketDelayMin_Type.__name__ = "Integer32"
_AcPMMediaRealmVERealmPacketDelayMin_Object = MibTableColumn
acPMMediaRealmVERealmPacketDelayMin = _AcPMMediaRealmVERealmPacketDelayMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 5, 1, 6),
    _AcPMMediaRealmVERealmPacketDelayMin_Type()
)
acPMMediaRealmVERealmPacketDelayMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketDelayMin.setStatus("current")
_AcPMMediaRealmVERealmPacketJitterTable_Object = MibTable
acPMMediaRealmVERealmPacketJitterTable = _AcPMMediaRealmVERealmPacketJitterTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 6)
)
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketJitterTable.setStatus("current")
_AcPMMediaRealmVERealmPacketJitterEntry_Object = MibTableRow
acPMMediaRealmVERealmPacketJitterEntry = _AcPMMediaRealmVERealmPacketJitterEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 6, 1)
)
acPMMediaRealmVERealmPacketJitterEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmVERealmPacketJitterMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmVERealmPacketJitterInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketJitterEntry.setStatus("current")


class _AcPMMediaRealmVERealmPacketJitterMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmVERealmPacketJitterMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmVERealmPacketJitterMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmVERealmPacketJitterMediaRealmNum_Object = MibTableColumn
acPMMediaRealmVERealmPacketJitterMediaRealmNum = _AcPMMediaRealmVERealmPacketJitterMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 6, 1, 1),
    _AcPMMediaRealmVERealmPacketJitterMediaRealmNum_Type()
)
acPMMediaRealmVERealmPacketJitterMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketJitterMediaRealmNum.setStatus("current")


class _AcPMMediaRealmVERealmPacketJitterInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmVERealmPacketJitterInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmVERealmPacketJitterInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmVERealmPacketJitterInterval_Object = MibTableColumn
acPMMediaRealmVERealmPacketJitterInterval = _AcPMMediaRealmVERealmPacketJitterInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 6, 1, 2),
    _AcPMMediaRealmVERealmPacketJitterInterval_Type()
)
acPMMediaRealmVERealmPacketJitterInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketJitterInterval.setStatus("current")
_AcPMMediaRealmVERealmPacketJitterVal_Type = Counter32
_AcPMMediaRealmVERealmPacketJitterVal_Object = MibTableColumn
acPMMediaRealmVERealmPacketJitterVal = _AcPMMediaRealmVERealmPacketJitterVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 6, 1, 3),
    _AcPMMediaRealmVERealmPacketJitterVal_Type()
)
acPMMediaRealmVERealmPacketJitterVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketJitterVal.setStatus("current")


class _AcPMMediaRealmVERealmPacketJitterAverage_Type(Integer32):
    """Custom type acPMMediaRealmVERealmPacketJitterAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmVERealmPacketJitterAverage_Type.__name__ = "Integer32"
_AcPMMediaRealmVERealmPacketJitterAverage_Object = MibTableColumn
acPMMediaRealmVERealmPacketJitterAverage = _AcPMMediaRealmVERealmPacketJitterAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 6, 1, 4),
    _AcPMMediaRealmVERealmPacketJitterAverage_Type()
)
acPMMediaRealmVERealmPacketJitterAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketJitterAverage.setStatus("current")


class _AcPMMediaRealmVERealmPacketJitterMax_Type(Integer32):
    """Custom type acPMMediaRealmVERealmPacketJitterMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmVERealmPacketJitterMax_Type.__name__ = "Integer32"
_AcPMMediaRealmVERealmPacketJitterMax_Object = MibTableColumn
acPMMediaRealmVERealmPacketJitterMax = _AcPMMediaRealmVERealmPacketJitterMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 6, 1, 5),
    _AcPMMediaRealmVERealmPacketJitterMax_Type()
)
acPMMediaRealmVERealmPacketJitterMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketJitterMax.setStatus("current")


class _AcPMMediaRealmVERealmPacketJitterMin_Type(Integer32):
    """Custom type acPMMediaRealmVERealmPacketJitterMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmVERealmPacketJitterMin_Type.__name__ = "Integer32"
_AcPMMediaRealmVERealmPacketJitterMin_Object = MibTableColumn
acPMMediaRealmVERealmPacketJitterMin = _AcPMMediaRealmVERealmPacketJitterMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 6, 1, 6),
    _AcPMMediaRealmVERealmPacketJitterMin_Type()
)
acPMMediaRealmVERealmPacketJitterMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmVERealmPacketJitterMin.setStatus("current")
_AcPMMediaRealmRealmMOSTable_Object = MibTable
acPMMediaRealmRealmMOSTable = _AcPMMediaRealmRealmMOSTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 7)
)
if mibBuilder.loadTexts:
    acPMMediaRealmRealmMOSTable.setStatus("current")
_AcPMMediaRealmRealmMOSEntry_Object = MibTableRow
acPMMediaRealmRealmMOSEntry = _AcPMMediaRealmRealmMOSEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 7, 1)
)
acPMMediaRealmRealmMOSEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmRealmMOSMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmRealmMOSInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmRealmMOSEntry.setStatus("current")


class _AcPMMediaRealmRealmMOSMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmRealmMOSMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmRealmMOSMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmRealmMOSMediaRealmNum_Object = MibTableColumn
acPMMediaRealmRealmMOSMediaRealmNum = _AcPMMediaRealmRealmMOSMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 7, 1, 1),
    _AcPMMediaRealmRealmMOSMediaRealmNum_Type()
)
acPMMediaRealmRealmMOSMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmRealmMOSMediaRealmNum.setStatus("current")


class _AcPMMediaRealmRealmMOSInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmRealmMOSInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmRealmMOSInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmRealmMOSInterval_Object = MibTableColumn
acPMMediaRealmRealmMOSInterval = _AcPMMediaRealmRealmMOSInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 7, 1, 2),
    _AcPMMediaRealmRealmMOSInterval_Type()
)
acPMMediaRealmRealmMOSInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmRealmMOSInterval.setStatus("current")
_AcPMMediaRealmRealmMOSVal_Type = Counter32
_AcPMMediaRealmRealmMOSVal_Object = MibTableColumn
acPMMediaRealmRealmMOSVal = _AcPMMediaRealmRealmMOSVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 7, 1, 3),
    _AcPMMediaRealmRealmMOSVal_Type()
)
acPMMediaRealmRealmMOSVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmRealmMOSVal.setStatus("current")


class _AcPMMediaRealmRealmMOSAverage_Type(Integer32):
    """Custom type acPMMediaRealmRealmMOSAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmRealmMOSAverage_Type.__name__ = "Integer32"
_AcPMMediaRealmRealmMOSAverage_Object = MibTableColumn
acPMMediaRealmRealmMOSAverage = _AcPMMediaRealmRealmMOSAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 7, 1, 4),
    _AcPMMediaRealmRealmMOSAverage_Type()
)
acPMMediaRealmRealmMOSAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmRealmMOSAverage.setStatus("current")


class _AcPMMediaRealmRealmMOSMax_Type(Integer32):
    """Custom type acPMMediaRealmRealmMOSMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmRealmMOSMax_Type.__name__ = "Integer32"
_AcPMMediaRealmRealmMOSMax_Object = MibTableColumn
acPMMediaRealmRealmMOSMax = _AcPMMediaRealmRealmMOSMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 7, 1, 5),
    _AcPMMediaRealmRealmMOSMax_Type()
)
acPMMediaRealmRealmMOSMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmRealmMOSMax.setStatus("current")


class _AcPMMediaRealmRealmMOSMin_Type(Integer32):
    """Custom type acPMMediaRealmRealmMOSMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmRealmMOSMin_Type.__name__ = "Integer32"
_AcPMMediaRealmRealmMOSMin_Object = MibTableColumn
acPMMediaRealmRealmMOSMin = _AcPMMediaRealmRealmMOSMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 7, 1, 6),
    _AcPMMediaRealmRealmMOSMin_Type()
)
acPMMediaRealmRealmMOSMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmRealmMOSMin.setStatus("current")
_AcPMMediaRealmBwRxTable_Object = MibTable
acPMMediaRealmBwRxTable = _AcPMMediaRealmBwRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8)
)
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxTable.setStatus("current")
_AcPMMediaRealmBwRxEntry_Object = MibTableRow
acPMMediaRealmBwRxEntry = _AcPMMediaRealmBwRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1)
)
acPMMediaRealmBwRxEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmBwRxMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmBwRxInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxEntry.setStatus("current")


class _AcPMMediaRealmBwRxMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmBwRxMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmBwRxMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmBwRxMediaRealmNum_Object = MibTableColumn
acPMMediaRealmBwRxMediaRealmNum = _AcPMMediaRealmBwRxMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 1),
    _AcPMMediaRealmBwRxMediaRealmNum_Type()
)
acPMMediaRealmBwRxMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxMediaRealmNum.setStatus("current")


class _AcPMMediaRealmBwRxInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmBwRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmBwRxInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmBwRxInterval_Object = MibTableColumn
acPMMediaRealmBwRxInterval = _AcPMMediaRealmBwRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 2),
    _AcPMMediaRealmBwRxInterval_Type()
)
acPMMediaRealmBwRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxInterval.setStatus("current")
_AcPMMediaRealmBwRxVal_Type = Counter32
_AcPMMediaRealmBwRxVal_Object = MibTableColumn
acPMMediaRealmBwRxVal = _AcPMMediaRealmBwRxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 3),
    _AcPMMediaRealmBwRxVal_Type()
)
acPMMediaRealmBwRxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxVal.setStatus("current")


class _AcPMMediaRealmBwRxAverage_Type(Integer32):
    """Custom type acPMMediaRealmBwRxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmBwRxAverage_Type.__name__ = "Integer32"
_AcPMMediaRealmBwRxAverage_Object = MibTableColumn
acPMMediaRealmBwRxAverage = _AcPMMediaRealmBwRxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 4),
    _AcPMMediaRealmBwRxAverage_Type()
)
acPMMediaRealmBwRxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxAverage.setStatus("current")


class _AcPMMediaRealmBwRxMax_Type(Integer32):
    """Custom type acPMMediaRealmBwRxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmBwRxMax_Type.__name__ = "Integer32"
_AcPMMediaRealmBwRxMax_Object = MibTableColumn
acPMMediaRealmBwRxMax = _AcPMMediaRealmBwRxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 5),
    _AcPMMediaRealmBwRxMax_Type()
)
acPMMediaRealmBwRxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxMax.setStatus("current")


class _AcPMMediaRealmBwRxMin_Type(Integer32):
    """Custom type acPMMediaRealmBwRxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmBwRxMin_Type.__name__ = "Integer32"
_AcPMMediaRealmBwRxMin_Object = MibTableColumn
acPMMediaRealmBwRxMin = _AcPMMediaRealmBwRxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 6),
    _AcPMMediaRealmBwRxMin_Type()
)
acPMMediaRealmBwRxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxMin.setStatus("current")


class _AcPMMediaRealmBwRxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMMediaRealmBwRxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMMediaRealmBwRxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMMediaRealmBwRxTimeBelowLowThreshold_Object = MibTableColumn
acPMMediaRealmBwRxTimeBelowLowThreshold = _AcPMMediaRealmBwRxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 7),
    _AcPMMediaRealmBwRxTimeBelowLowThreshold_Type()
)
acPMMediaRealmBwRxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxTimeBelowLowThreshold.setStatus("current")


class _AcPMMediaRealmBwRxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMMediaRealmBwRxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMMediaRealmBwRxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMMediaRealmBwRxTimeBetweenThresholds_Object = MibTableColumn
acPMMediaRealmBwRxTimeBetweenThresholds = _AcPMMediaRealmBwRxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 8),
    _AcPMMediaRealmBwRxTimeBetweenThresholds_Type()
)
acPMMediaRealmBwRxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxTimeBetweenThresholds.setStatus("current")


class _AcPMMediaRealmBwRxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMMediaRealmBwRxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMMediaRealmBwRxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMMediaRealmBwRxTimeAboveHighThreshold_Object = MibTableColumn
acPMMediaRealmBwRxTimeAboveHighThreshold = _AcPMMediaRealmBwRxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 9),
    _AcPMMediaRealmBwRxTimeAboveHighThreshold_Type()
)
acPMMediaRealmBwRxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxTimeAboveHighThreshold.setStatus("current")


class _AcPMMediaRealmBwRxFullDayAverage_Type(Integer32):
    """Custom type acPMMediaRealmBwRxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmBwRxFullDayAverage_Type.__name__ = "Integer32"
_AcPMMediaRealmBwRxFullDayAverage_Object = MibTableColumn
acPMMediaRealmBwRxFullDayAverage = _AcPMMediaRealmBwRxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 10),
    _AcPMMediaRealmBwRxFullDayAverage_Type()
)
acPMMediaRealmBwRxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxFullDayAverage.setStatus("current")
_AcPMMediaRealmBwRxTotal_Type = Counter32
_AcPMMediaRealmBwRxTotal_Object = MibTableColumn
acPMMediaRealmBwRxTotal = _AcPMMediaRealmBwRxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 8, 1, 11),
    _AcPMMediaRealmBwRxTotal_Type()
)
acPMMediaRealmBwRxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwRxTotal.setStatus("current")
_AcPMMediaRealmBwTxTable_Object = MibTable
acPMMediaRealmBwTxTable = _AcPMMediaRealmBwTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9)
)
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxTable.setStatus("current")
_AcPMMediaRealmBwTxEntry_Object = MibTableRow
acPMMediaRealmBwTxEntry = _AcPMMediaRealmBwTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1)
)
acPMMediaRealmBwTxEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmBwTxMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmBwTxInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxEntry.setStatus("current")


class _AcPMMediaRealmBwTxMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmBwTxMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmBwTxMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmBwTxMediaRealmNum_Object = MibTableColumn
acPMMediaRealmBwTxMediaRealmNum = _AcPMMediaRealmBwTxMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 1),
    _AcPMMediaRealmBwTxMediaRealmNum_Type()
)
acPMMediaRealmBwTxMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxMediaRealmNum.setStatus("current")


class _AcPMMediaRealmBwTxInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmBwTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmBwTxInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmBwTxInterval_Object = MibTableColumn
acPMMediaRealmBwTxInterval = _AcPMMediaRealmBwTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 2),
    _AcPMMediaRealmBwTxInterval_Type()
)
acPMMediaRealmBwTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxInterval.setStatus("current")
_AcPMMediaRealmBwTxVal_Type = Counter32
_AcPMMediaRealmBwTxVal_Object = MibTableColumn
acPMMediaRealmBwTxVal = _AcPMMediaRealmBwTxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 3),
    _AcPMMediaRealmBwTxVal_Type()
)
acPMMediaRealmBwTxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxVal.setStatus("current")


class _AcPMMediaRealmBwTxAverage_Type(Integer32):
    """Custom type acPMMediaRealmBwTxAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmBwTxAverage_Type.__name__ = "Integer32"
_AcPMMediaRealmBwTxAverage_Object = MibTableColumn
acPMMediaRealmBwTxAverage = _AcPMMediaRealmBwTxAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 4),
    _AcPMMediaRealmBwTxAverage_Type()
)
acPMMediaRealmBwTxAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxAverage.setStatus("current")


class _AcPMMediaRealmBwTxMax_Type(Integer32):
    """Custom type acPMMediaRealmBwTxMax based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmBwTxMax_Type.__name__ = "Integer32"
_AcPMMediaRealmBwTxMax_Object = MibTableColumn
acPMMediaRealmBwTxMax = _AcPMMediaRealmBwTxMax_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 5),
    _AcPMMediaRealmBwTxMax_Type()
)
acPMMediaRealmBwTxMax.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxMax.setStatus("current")


class _AcPMMediaRealmBwTxMin_Type(Integer32):
    """Custom type acPMMediaRealmBwTxMin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmBwTxMin_Type.__name__ = "Integer32"
_AcPMMediaRealmBwTxMin_Object = MibTableColumn
acPMMediaRealmBwTxMin = _AcPMMediaRealmBwTxMin_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 6),
    _AcPMMediaRealmBwTxMin_Type()
)
acPMMediaRealmBwTxMin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxMin.setStatus("current")


class _AcPMMediaRealmBwTxTimeBelowLowThreshold_Type(Integer32):
    """Custom type acPMMediaRealmBwTxTimeBelowLowThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMMediaRealmBwTxTimeBelowLowThreshold_Type.__name__ = "Integer32"
_AcPMMediaRealmBwTxTimeBelowLowThreshold_Object = MibTableColumn
acPMMediaRealmBwTxTimeBelowLowThreshold = _AcPMMediaRealmBwTxTimeBelowLowThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 7),
    _AcPMMediaRealmBwTxTimeBelowLowThreshold_Type()
)
acPMMediaRealmBwTxTimeBelowLowThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxTimeBelowLowThreshold.setStatus("current")


class _AcPMMediaRealmBwTxTimeBetweenThresholds_Type(Integer32):
    """Custom type acPMMediaRealmBwTxTimeBetweenThresholds based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMMediaRealmBwTxTimeBetweenThresholds_Type.__name__ = "Integer32"
_AcPMMediaRealmBwTxTimeBetweenThresholds_Object = MibTableColumn
acPMMediaRealmBwTxTimeBetweenThresholds = _AcPMMediaRealmBwTxTimeBetweenThresholds_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 8),
    _AcPMMediaRealmBwTxTimeBetweenThresholds_Type()
)
acPMMediaRealmBwTxTimeBetweenThresholds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxTimeBetweenThresholds.setStatus("current")


class _AcPMMediaRealmBwTxTimeAboveHighThreshold_Type(Integer32):
    """Custom type acPMMediaRealmBwTxTimeAboveHighThreshold based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 100),
    )


_AcPMMediaRealmBwTxTimeAboveHighThreshold_Type.__name__ = "Integer32"
_AcPMMediaRealmBwTxTimeAboveHighThreshold_Object = MibTableColumn
acPMMediaRealmBwTxTimeAboveHighThreshold = _AcPMMediaRealmBwTxTimeAboveHighThreshold_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 9),
    _AcPMMediaRealmBwTxTimeAboveHighThreshold_Type()
)
acPMMediaRealmBwTxTimeAboveHighThreshold.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxTimeAboveHighThreshold.setStatus("current")


class _AcPMMediaRealmBwTxFullDayAverage_Type(Integer32):
    """Custom type acPMMediaRealmBwTxFullDayAverage based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(-1, 2150000000),
    )


_AcPMMediaRealmBwTxFullDayAverage_Type.__name__ = "Integer32"
_AcPMMediaRealmBwTxFullDayAverage_Object = MibTableColumn
acPMMediaRealmBwTxFullDayAverage = _AcPMMediaRealmBwTxFullDayAverage_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 10),
    _AcPMMediaRealmBwTxFullDayAverage_Type()
)
acPMMediaRealmBwTxFullDayAverage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxFullDayAverage.setStatus("current")
_AcPMMediaRealmBwTxTotal_Type = Counter32
_AcPMMediaRealmBwTxTotal_Object = MibTableColumn
acPMMediaRealmBwTxTotal = _AcPMMediaRealmBwTxTotal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 9, 1, 11),
    _AcPMMediaRealmBwTxTotal_Type()
)
acPMMediaRealmBwTxTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmBwTxTotal.setStatus("current")
_AcPMMediaRealmPacketLossRxTable_Object = MibTable
acPMMediaRealmPacketLossRxTable = _AcPMMediaRealmPacketLossRxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 10)
)
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossRxTable.setStatus("current")
_AcPMMediaRealmPacketLossRxEntry_Object = MibTableRow
acPMMediaRealmPacketLossRxEntry = _AcPMMediaRealmPacketLossRxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 10, 1)
)
acPMMediaRealmPacketLossRxEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmPacketLossRxMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmPacketLossRxInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossRxEntry.setStatus("current")


class _AcPMMediaRealmPacketLossRxMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmPacketLossRxMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmPacketLossRxMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmPacketLossRxMediaRealmNum_Object = MibTableColumn
acPMMediaRealmPacketLossRxMediaRealmNum = _AcPMMediaRealmPacketLossRxMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 10, 1, 1),
    _AcPMMediaRealmPacketLossRxMediaRealmNum_Type()
)
acPMMediaRealmPacketLossRxMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossRxMediaRealmNum.setStatus("current")


class _AcPMMediaRealmPacketLossRxInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmPacketLossRxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmPacketLossRxInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmPacketLossRxInterval_Object = MibTableColumn
acPMMediaRealmPacketLossRxInterval = _AcPMMediaRealmPacketLossRxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 10, 1, 2),
    _AcPMMediaRealmPacketLossRxInterval_Type()
)
acPMMediaRealmPacketLossRxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossRxInterval.setStatus("current")
_AcPMMediaRealmPacketLossRxVal_Type = Counter32
_AcPMMediaRealmPacketLossRxVal_Object = MibTableColumn
acPMMediaRealmPacketLossRxVal = _AcPMMediaRealmPacketLossRxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 10, 1, 3),
    _AcPMMediaRealmPacketLossRxVal_Type()
)
acPMMediaRealmPacketLossRxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossRxVal.setStatus("current")
_AcPMMediaRealmPacketLossRxVolume_Type = Counter32
_AcPMMediaRealmPacketLossRxVolume_Object = MibTableColumn
acPMMediaRealmPacketLossRxVolume = _AcPMMediaRealmPacketLossRxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 10, 1, 4),
    _AcPMMediaRealmPacketLossRxVolume_Type()
)
acPMMediaRealmPacketLossRxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossRxVolume.setStatus("current")
_AcPMMediaRealmPacketLossTxTable_Object = MibTable
acPMMediaRealmPacketLossTxTable = _AcPMMediaRealmPacketLossTxTable_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 11)
)
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossTxTable.setStatus("current")
_AcPMMediaRealmPacketLossTxEntry_Object = MibTableRow
acPMMediaRealmPacketLossTxEntry = _AcPMMediaRealmPacketLossTxEntry_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 11, 1)
)
acPMMediaRealmPacketLossTxEntry.setIndexNames(
    (0, "AC-PM-Control-MIB", "acPMMediaRealmPacketLossTxMediaRealmNum"),
    (0, "AC-PM-Control-MIB", "acPMMediaRealmPacketLossTxInterval"),
)
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossTxEntry.setStatus("current")


class _AcPMMediaRealmPacketLossTxMediaRealmNum_Type(Unsigned32):
    """Custom type acPMMediaRealmPacketLossTxMediaRealmNum based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AcPMMediaRealmPacketLossTxMediaRealmNum_Type.__name__ = "Unsigned32"
_AcPMMediaRealmPacketLossTxMediaRealmNum_Object = MibTableColumn
acPMMediaRealmPacketLossTxMediaRealmNum = _AcPMMediaRealmPacketLossTxMediaRealmNum_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 11, 1, 1),
    _AcPMMediaRealmPacketLossTxMediaRealmNum_Type()
)
acPMMediaRealmPacketLossTxMediaRealmNum.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossTxMediaRealmNum.setStatus("current")


class _AcPMMediaRealmPacketLossTxInterval_Type(Unsigned32):
    """Custom type acPMMediaRealmPacketLossTxInterval based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2),
    )


_AcPMMediaRealmPacketLossTxInterval_Type.__name__ = "Unsigned32"
_AcPMMediaRealmPacketLossTxInterval_Object = MibTableColumn
acPMMediaRealmPacketLossTxInterval = _AcPMMediaRealmPacketLossTxInterval_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 11, 1, 2),
    _AcPMMediaRealmPacketLossTxInterval_Type()
)
acPMMediaRealmPacketLossTxInterval.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossTxInterval.setStatus("current")
_AcPMMediaRealmPacketLossTxVal_Type = Counter32
_AcPMMediaRealmPacketLossTxVal_Object = MibTableColumn
acPMMediaRealmPacketLossTxVal = _AcPMMediaRealmPacketLossTxVal_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 11, 1, 3),
    _AcPMMediaRealmPacketLossTxVal_Type()
)
acPMMediaRealmPacketLossTxVal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossTxVal.setStatus("current")
_AcPMMediaRealmPacketLossTxVolume_Type = Counter32
_AcPMMediaRealmPacketLossTxVolume_Object = MibTableColumn
acPMMediaRealmPacketLossTxVolume = _AcPMMediaRealmPacketLossTxVolume_Object(
    (1, 3, 6, 1, 4, 1, 5003, 10, 8, 2, 53, 11, 1, 4),
    _AcPMMediaRealmPacketLossTxVolume_Type()
)
acPMMediaRealmPacketLossTxVolume.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    acPMMediaRealmPacketLossTxVolume.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AC-PM-Control-MIB",
    **{"acPMControl": acPMControl,
       "acPMControlConfiguration": acPMControlConfiguration,
       "acPMControlConfigurationPeriodLength": acPMControlConfigurationPeriodLength,
       "acPMControlConfigurationResetTotalCounters": acPMControlConfigurationResetTotalCounters,
       "acPMCPConnectionAttributes": acPMCPConnectionAttributes,
       "acPMCPConnectionAttributesLifetimeHighThreshold": acPMCPConnectionAttributesLifetimeHighThreshold,
       "acPMCPConnectionAttributesLifetimeLowThreshold": acPMCPConnectionAttributesLifetimeLowThreshold,
       "acPMCPConnectionAttributesStateHighThreshold": acPMCPConnectionAttributesStateHighThreshold,
       "acPMCPConnectionAttributesStateLowThreshold": acPMCPConnectionAttributesStateLowThreshold,
       "acPMCPConnectionAttributesCommandCounterHighThreshold": acPMCPConnectionAttributesCommandCounterHighThreshold,
       "acPMCPConnectionAttributesCommandCounterLowThreshold": acPMCPConnectionAttributesCommandCounterLowThreshold,
       "acPMCPConnectionAttributesRetransmissionCountHighThreshold": acPMCPConnectionAttributesRetransmissionCountHighThreshold,
       "acPMCPConnectionAttributesRetransmissionCountLowThreshold": acPMCPConnectionAttributesRetransmissionCountLowThreshold,
       "acPMCPConnectionAttributesActiveContextCountHighThreshold": acPMCPConnectionAttributesActiveContextCountHighThreshold,
       "acPMCPConnectionAttributesActiveContextCountLowThreshold": acPMCPConnectionAttributesActiveContextCountLowThreshold,
       "acPMCPConnectionAttributesCommandSuccessCountHighThreshold": acPMCPConnectionAttributesCommandSuccessCountHighThreshold,
       "acPMCPConnectionAttributesCommandSuccessCountLowThreshold": acPMCPConnectionAttributesCommandSuccessCountLowThreshold,
       "acPMCPConnectionAttributesCommandFailureCountHighThreshold": acPMCPConnectionAttributesCommandFailureCountHighThreshold,
       "acPMCPConnectionAttributesCommandFailureCountLowThreshold": acPMCPConnectionAttributesCommandFailureCountLowThreshold,
       "acPMCPConnectionAttributesCommandProcessTimeHighThreshold": acPMCPConnectionAttributesCommandProcessTimeHighThreshold,
       "acPMCPConnectionAttributesCommandProcessTimeLowThreshold": acPMCPConnectionAttributesCommandProcessTimeLowThreshold,
       "acPMCPConnectionAttributesTransactionProcessTimerHighThreshold": acPMCPConnectionAttributesTransactionProcessTimerHighThreshold,
       "acPMCPConnectionAttributesTransactionProcessTimerLowThreshold": acPMCPConnectionAttributesTransactionProcessTimerLowThreshold,
       "acPMMegacoAttributes": acPMMegacoAttributes,
       "acPMMegacoAttributesServiceChangeCountHighThreshold": acPMMegacoAttributesServiceChangeCountHighThreshold,
       "acPMMegacoAttributesServiceChangeCountLowThreshold": acPMMegacoAttributesServiceChangeCountLowThreshold,
       "acPMMegacoAttributesCmdSuccessCountHighThreshold": acPMMegacoAttributesCmdSuccessCountHighThreshold,
       "acPMMegacoAttributesCmdSuccessCountLowThreshold": acPMMegacoAttributesCmdSuccessCountLowThreshold,
       "acPMMegacoAttributesCmdFailureCountHighThreshold": acPMMegacoAttributesCmdFailureCountHighThreshold,
       "acPMMegacoAttributesCmdFailureCountLowThreshold": acPMMegacoAttributesCmdFailureCountLowThreshold,
       "acPMSipAttributes": acPMSipAttributes,
       "acPMSipAttributesCallDurationHighThreshold": acPMSipAttributesCallDurationHighThreshold,
       "acPMSipAttributesCallDurationLowThreshold": acPMSipAttributesCallDurationLowThreshold,
       "acPMSipAttributesTrunkGroupUtilizationHighThreshold": acPMSipAttributesTrunkGroupUtilizationHighThreshold,
       "acPMSipAttributesTrunkGroupUtilizationLowThreshold": acPMSipAttributesTrunkGroupUtilizationLowThreshold,
       "acPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold": acPMSipAttributesTrunkGroupPercentageUtilizationHighThreshold,
       "acPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold": acPMSipAttributesTrunkGroupPercentageUtilizationLowThreshold,
       "acPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold": acPMSipAttributesTrunkGroupNoResourcesCallsHighThreshold,
       "acPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold": acPMSipAttributesTrunkGroupNoResourcesCallsLowThreshold,
       "acPMSipAttributesIPGroupINVITEDialogsHighThreshold": acPMSipAttributesIPGroupINVITEDialogsHighThreshold,
       "acPMSipAttributesIPGroupINVITEDialogsLowThreshold": acPMSipAttributesIPGroupINVITEDialogsLowThreshold,
       "acPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold": acPMSipAttributesTrunkGroupAllTrunksBusyPercentageHighThreshold,
       "acPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold": acPMSipAttributesTrunkGroupAllTrunksBusyPercentageLowThreshold,
       "acPMMediaRealmAttributes": acPMMediaRealmAttributes,
       "acPMMediaRealmAttributesMediaRealmBytesTxHighThreshold": acPMMediaRealmAttributesMediaRealmBytesTxHighThreshold,
       "acPMMediaRealmAttributesMediaRealmBytesTxLowThreshold": acPMMediaRealmAttributesMediaRealmBytesTxLowThreshold,
       "acPMMediaRealmAttributesMediaRealmBytesRxHighThreshold": acPMMediaRealmAttributesMediaRealmBytesRxHighThreshold,
       "acPMMediaRealmAttributesMediaRealmBytesRxLowThreshold": acPMMediaRealmAttributesMediaRealmBytesRxLowThreshold,
       "acPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold": acPMMediaRealmAttributesMediaRealmPacketsTxHighThreshold,
       "acPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold": acPMMediaRealmAttributesMediaRealmPacketsTxLowThreshold,
       "acPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold": acPMMediaRealmAttributesMediaRealmPacketsRxHighThreshold,
       "acPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold": acPMMediaRealmAttributesMediaRealmPacketsRxLowThreshold,
       "acPMMediaRealmAttributesVERealmPacketDelayHighThreshold": acPMMediaRealmAttributesVERealmPacketDelayHighThreshold,
       "acPMMediaRealmAttributesVERealmPacketDelayLowThreshold": acPMMediaRealmAttributesVERealmPacketDelayLowThreshold,
       "acPMMediaRealmAttributesVERealmPacketJitterHighThreshold": acPMMediaRealmAttributesVERealmPacketJitterHighThreshold,
       "acPMMediaRealmAttributesVERealmPacketJitterLowThreshold": acPMMediaRealmAttributesVERealmPacketJitterLowThreshold,
       "acPMMediaRealmAttributesRealmMOSHighThreshold": acPMMediaRealmAttributesRealmMOSHighThreshold,
       "acPMMediaRealmAttributesRealmMOSLowThreshold": acPMMediaRealmAttributesRealmMOSLowThreshold,
       "acPMMediaRealmAttributesMediaRealmBwRxHighThreshold": acPMMediaRealmAttributesMediaRealmBwRxHighThreshold,
       "acPMMediaRealmAttributesMediaRealmBwRxLowThreshold": acPMMediaRealmAttributesMediaRealmBwRxLowThreshold,
       "acPMMediaRealmAttributesMediaRealmBwTxHighThreshold": acPMMediaRealmAttributesMediaRealmBwTxHighThreshold,
       "acPMMediaRealmAttributesMediaRealmBwTxLowThreshold": acPMMediaRealmAttributesMediaRealmBwTxLowThreshold,
       "acPMControlData": acPMControlData,
       "acPMControlDataAcPMControlTimeFromStartOfInterval": acPMControlDataAcPMControlTimeFromStartOfInterval,
       "acPMCPConnection": acPMCPConnection,
       "acPMCPConnectionLifetimeTable": acPMCPConnectionLifetimeTable,
       "acPMCPConnectionLifetimeEntry": acPMCPConnectionLifetimeEntry,
       "acPMCPConnectionLifetimeInterval": acPMCPConnectionLifetimeInterval,
       "acPMCPConnectionLifetimeVal": acPMCPConnectionLifetimeVal,
       "acPMCPConnectionLifetimeAverage": acPMCPConnectionLifetimeAverage,
       "acPMCPConnectionLifetimeMax": acPMCPConnectionLifetimeMax,
       "acPMCPConnectionLifetimeMin": acPMCPConnectionLifetimeMin,
       "acPMCPConnectionLifetimeVolume": acPMCPConnectionLifetimeVolume,
       "acPMCPConnectionLifetimeTimeBelowLowThreshold": acPMCPConnectionLifetimeTimeBelowLowThreshold,
       "acPMCPConnectionLifetimeTimeBetweenThresholds": acPMCPConnectionLifetimeTimeBetweenThresholds,
       "acPMCPConnectionLifetimeTimeAboveHighThreshold": acPMCPConnectionLifetimeTimeAboveHighThreshold,
       "acPMCPConnectionLifetimeFullDayAverage": acPMCPConnectionLifetimeFullDayAverage,
       "acPMCPConnectionLifetimeTotal": acPMCPConnectionLifetimeTotal,
       "acPMCPConnectionStateTable": acPMCPConnectionStateTable,
       "acPMCPConnectionStateEntry": acPMCPConnectionStateEntry,
       "acPMCPConnectionStateInterval": acPMCPConnectionStateInterval,
       "acPMCPConnectionStateChanges": acPMCPConnectionStateChanges,
       "acPMCPConnectionStateActiveTime": acPMCPConnectionStateActiveTime,
       "acPMCPCommandCounterTable": acPMCPCommandCounterTable,
       "acPMCPCommandCounterEntry": acPMCPCommandCounterEntry,
       "acPMCPCommandCounterDirection": acPMCPCommandCounterDirection,
       "acPMCPCommandCounterInterval": acPMCPCommandCounterInterval,
       "acPMCPCommandCounterVal": acPMCPCommandCounterVal,
       "acPMCPCommandCounterTotal": acPMCPCommandCounterTotal,
       "acPMCPRetransmissionCountTable": acPMCPRetransmissionCountTable,
       "acPMCPRetransmissionCountEntry": acPMCPRetransmissionCountEntry,
       "acPMCPRetransmissionCountDirection": acPMCPRetransmissionCountDirection,
       "acPMCPRetransmissionCountInterval": acPMCPRetransmissionCountInterval,
       "acPMCPRetransmissionCountVal": acPMCPRetransmissionCountVal,
       "acPMCPRetransmissionCountTotal": acPMCPRetransmissionCountTotal,
       "acPMActiveContextCountTable": acPMActiveContextCountTable,
       "acPMActiveContextCountEntry": acPMActiveContextCountEntry,
       "acPMActiveContextCountInterval": acPMActiveContextCountInterval,
       "acPMActiveContextCountVal": acPMActiveContextCountVal,
       "acPMActiveContextCountAverage": acPMActiveContextCountAverage,
       "acPMActiveContextCountMax": acPMActiveContextCountMax,
       "acPMActiveContextCountMin": acPMActiveContextCountMin,
       "acPMActiveContextCountVolume": acPMActiveContextCountVolume,
       "acPMActiveContextCountTimeBelowLowThreshold": acPMActiveContextCountTimeBelowLowThreshold,
       "acPMActiveContextCountTimeBetweenThresholds": acPMActiveContextCountTimeBetweenThresholds,
       "acPMActiveContextCountTimeAboveHighThreshold": acPMActiveContextCountTimeAboveHighThreshold,
       "acPMActiveContextCountFullDayAverage": acPMActiveContextCountFullDayAverage,
       "acPMActiveContextCountTotal": acPMActiveContextCountTotal,
       "acPMCPCommandSuccessCountTable": acPMCPCommandSuccessCountTable,
       "acPMCPCommandSuccessCountEntry": acPMCPCommandSuccessCountEntry,
       "acPMCPCommandSuccessCountCommandType": acPMCPCommandSuccessCountCommandType,
       "acPMCPCommandSuccessCountInterval": acPMCPCommandSuccessCountInterval,
       "acPMCPCommandSuccessCountVal": acPMCPCommandSuccessCountVal,
       "acPMCPCommandSuccessCountTotal": acPMCPCommandSuccessCountTotal,
       "acPMCPCommandFailureCountTable": acPMCPCommandFailureCountTable,
       "acPMCPCommandFailureCountEntry": acPMCPCommandFailureCountEntry,
       "acPMCPCommandFailureCountCommandType": acPMCPCommandFailureCountCommandType,
       "acPMCPCommandFailureCountInterval": acPMCPCommandFailureCountInterval,
       "acPMCPCommandFailureCountVal": acPMCPCommandFailureCountVal,
       "acPMCPCommandFailureCountTotal": acPMCPCommandFailureCountTotal,
       "acPMcpCmdProcessTimeTable": acPMcpCmdProcessTimeTable,
       "acPMcpCmdProcessTimeEntry": acPMcpCmdProcessTimeEntry,
       "acPMcpCmdProcessTimeInterval": acPMcpCmdProcessTimeInterval,
       "acPMcpCmdProcessTimeVal": acPMcpCmdProcessTimeVal,
       "acPMcpCmdProcessTimeAverage": acPMcpCmdProcessTimeAverage,
       "acPMcpCmdProcessTimeMax": acPMcpCmdProcessTimeMax,
       "acPMcpCmdProcessTimeMin": acPMcpCmdProcessTimeMin,
       "acPMcpCmdProcessTimeVolume": acPMcpCmdProcessTimeVolume,
       "acPMcpCmdProcessTimeTimeBelowLowThreshold": acPMcpCmdProcessTimeTimeBelowLowThreshold,
       "acPMcpCmdProcessTimeTimeBetweenThresholds": acPMcpCmdProcessTimeTimeBetweenThresholds,
       "acPMcpCmdProcessTimeTimeAboveHighThreshold": acPMcpCmdProcessTimeTimeAboveHighThreshold,
       "acPMcpCmdProcessTimeFullDayAverage": acPMcpCmdProcessTimeFullDayAverage,
       "acPMcpCmdProcessTimeTotal": acPMcpCmdProcessTimeTotal,
       "acPMcpTransactionProcessTimerTable": acPMcpTransactionProcessTimerTable,
       "acPMcpTransactionProcessTimerEntry": acPMcpTransactionProcessTimerEntry,
       "acPMcpTransactionProcessTimerInterval": acPMcpTransactionProcessTimerInterval,
       "acPMcpTransactionProcessTimerVal": acPMcpTransactionProcessTimerVal,
       "acPMcpTransactionProcessTimerAverage": acPMcpTransactionProcessTimerAverage,
       "acPMcpTransactionProcessTimerMax": acPMcpTransactionProcessTimerMax,
       "acPMcpTransactionProcessTimerMin": acPMcpTransactionProcessTimerMin,
       "acPMcpTransactionProcessTimerVolume": acPMcpTransactionProcessTimerVolume,
       "acPMcpTransactionProcessTimerTimeBelowLowThreshold": acPMcpTransactionProcessTimerTimeBelowLowThreshold,
       "acPMcpTransactionProcessTimerTimeBetweenThresholds": acPMcpTransactionProcessTimerTimeBetweenThresholds,
       "acPMcpTransactionProcessTimerTimeAboveHighThreshold": acPMcpTransactionProcessTimerTimeAboveHighThreshold,
       "acPMcpTransactionProcessTimerFullDayAverage": acPMcpTransactionProcessTimerFullDayAverage,
       "acPMcpTransactionProcessTimerTotal": acPMcpTransactionProcessTimerTotal,
       "acPMCPCallAttemptsPerSecTable": acPMCPCallAttemptsPerSecTable,
       "acPMCPCallAttemptsPerSecEntry": acPMCPCallAttemptsPerSecEntry,
       "acPMCPCallAttemptsPerSecInterval": acPMCPCallAttemptsPerSecInterval,
       "acPMCPCallAttemptsPerSecVal": acPMCPCallAttemptsPerSecVal,
       "acPMCPCallAttemptsPerSecAverage": acPMCPCallAttemptsPerSecAverage,
       "acPMCPCallAttemptsPerSecMax": acPMCPCallAttemptsPerSecMax,
       "acPMCPCallAttemptsPerSecMin": acPMCPCallAttemptsPerSecMin,
       "acPMCPCallAttemptsPerSecVolume": acPMCPCallAttemptsPerSecVolume,
       "acPMMegaco": acPMMegaco,
       "acPMMegacoServiceChangeCountTable": acPMMegacoServiceChangeCountTable,
       "acPMMegacoServiceChangeCountEntry": acPMMegacoServiceChangeCountEntry,
       "acPMMegacoServiceChangeCountMethod": acPMMegacoServiceChangeCountMethod,
       "acPMMegacoServiceChangeCountInterval": acPMMegacoServiceChangeCountInterval,
       "acPMMegacoServiceChangeCountVal": acPMMegacoServiceChangeCountVal,
       "acPMCPCmdSuccessCountTable": acPMCPCmdSuccessCountTable,
       "acPMCPCmdSuccessCountEntry": acPMCPCmdSuccessCountEntry,
       "acPMCPCmdSuccessCountCommandType": acPMCPCmdSuccessCountCommandType,
       "acPMCPCmdSuccessCountInterval": acPMCPCmdSuccessCountInterval,
       "acPMCPCmdSuccessCountVal": acPMCPCmdSuccessCountVal,
       "acPMCPCmdSuccessCountTotal": acPMCPCmdSuccessCountTotal,
       "acPMCPCmdFailureCountTable": acPMCPCmdFailureCountTable,
       "acPMCPCmdFailureCountEntry": acPMCPCmdFailureCountEntry,
       "acPMCPCmdFailureCountCommandType": acPMCPCmdFailureCountCommandType,
       "acPMCPCmdFailureCountInterval": acPMCPCmdFailureCountInterval,
       "acPMCPCmdFailureCountVal": acPMCPCmdFailureCountVal,
       "acPMCPCmdFailureCountTotal": acPMCPCmdFailureCountTotal,
       "acPMcpUMTSHandOverCountTable": acPMcpUMTSHandOverCountTable,
       "acPMcpUMTSHandOverCountEntry": acPMcpUMTSHandOverCountEntry,
       "acPMcpUMTSHandOverCountInterval": acPMcpUMTSHandOverCountInterval,
       "acPMcpUMTSHandOverCountVal": acPMcpUMTSHandOverCountVal,
       "acPMMegacoAddFailureCountTable": acPMMegacoAddFailureCountTable,
       "acPMMegacoAddFailureCountEntry": acPMMegacoAddFailureCountEntry,
       "acPMMegacoAddFailureCountInterval": acPMMegacoAddFailureCountInterval,
       "acPMMegacoAddFailureCountVal": acPMMegacoAddFailureCountVal,
       "acPMMegacoModifyFailureCountTable": acPMMegacoModifyFailureCountTable,
       "acPMMegacoModifyFailureCountEntry": acPMMegacoModifyFailureCountEntry,
       "acPMMegacoModifyFailureCountInterval": acPMMegacoModifyFailureCountInterval,
       "acPMMegacoModifyFailureCountVal": acPMMegacoModifyFailureCountVal,
       "acPMMegacoSuccessfulAddWithLoopbackTable": acPMMegacoSuccessfulAddWithLoopbackTable,
       "acPMMegacoSuccessfulAddWithLoopbackEntry": acPMMegacoSuccessfulAddWithLoopbackEntry,
       "acPMMegacoSuccessfulAddWithLoopbackInterval": acPMMegacoSuccessfulAddWithLoopbackInterval,
       "acPMMegacoSuccessfulAddWithLoopbackVal": acPMMegacoSuccessfulAddWithLoopbackVal,
       "acPMMegacoFailedAddWithLoopbackTable": acPMMegacoFailedAddWithLoopbackTable,
       "acPMMegacoFailedAddWithLoopbackEntry": acPMMegacoFailedAddWithLoopbackEntry,
       "acPMMegacoFailedAddWithLoopbackInterval": acPMMegacoFailedAddWithLoopbackInterval,
       "acPMMegacoFailedAddWithLoopbackVal": acPMMegacoFailedAddWithLoopbackVal,
       "acPMMegacoOutgoingCommandSuccessCountTable": acPMMegacoOutgoingCommandSuccessCountTable,
       "acPMMegacoOutgoingCommandSuccessCountEntry": acPMMegacoOutgoingCommandSuccessCountEntry,
       "acPMMegacoOutgoingCommandSuccessCountInterval": acPMMegacoOutgoingCommandSuccessCountInterval,
       "acPMMegacoOutgoingCommandSuccessCountVal": acPMMegacoOutgoingCommandSuccessCountVal,
       "acPMMegacoOutgoingCommandFailureCountTable": acPMMegacoOutgoingCommandFailureCountTable,
       "acPMMegacoOutgoingCommandFailureCountEntry": acPMMegacoOutgoingCommandFailureCountEntry,
       "acPMMegacoOutgoingCommandFailureCountInterval": acPMMegacoOutgoingCommandFailureCountInterval,
       "acPMMegacoOutgoingCommandFailureCountVal": acPMMegacoOutgoingCommandFailureCountVal,
       "acPMMGCP": acPMMGCP,
       "acPMMGCPRsipReasonCountTable": acPMMGCPRsipReasonCountTable,
       "acPMMGCPRsipReasonCountEntry": acPMMGCPRsipReasonCountEntry,
       "acPMMGCPRsipReasonCountReasonCode": acPMMGCPRsipReasonCountReasonCode,
       "acPMMGCPRsipReasonCountInterval": acPMMGCPRsipReasonCountInterval,
       "acPMMGCPRsipReasonCountVal": acPMMGCPRsipReasonCountVal,
       "acPMMGCPGeneratedDLCXTable": acPMMGCPGeneratedDLCXTable,
       "acPMMGCPGeneratedDLCXEntry": acPMMGCPGeneratedDLCXEntry,
       "acPMMGCPGeneratedDLCXInterval": acPMMGCPGeneratedDLCXInterval,
       "acPMMGCPGeneratedDLCXVal": acPMMGCPGeneratedDLCXVal,
       "acPMMGCPCommandSuccessCountTable": acPMMGCPCommandSuccessCountTable,
       "acPMMGCPCommandSuccessCountEntry": acPMMGCPCommandSuccessCountEntry,
       "acPMMGCPCommandSuccessCountCommandType": acPMMGCPCommandSuccessCountCommandType,
       "acPMMGCPCommandSuccessCountInterval": acPMMGCPCommandSuccessCountInterval,
       "acPMMGCPCommandSuccessCountVal": acPMMGCPCommandSuccessCountVal,
       "acPMMGCPCommandSuccessCountTotal": acPMMGCPCommandSuccessCountTotal,
       "acPMMGCPCommandFailureCountTable": acPMMGCPCommandFailureCountTable,
       "acPMMGCPCommandFailureCountEntry": acPMMGCPCommandFailureCountEntry,
       "acPMMGCPCommandFailureCountCommandType": acPMMGCPCommandFailureCountCommandType,
       "acPMMGCPCommandFailureCountInterval": acPMMGCPCommandFailureCountInterval,
       "acPMMGCPCommandFailureCountVal": acPMMGCPCommandFailureCountVal,
       "acPMMGCPCommandFailureCountTotal": acPMMGCPCommandFailureCountTotal,
       "acPMMGCPLoopbackCRCXTable": acPMMGCPLoopbackCRCXTable,
       "acPMMGCPLoopbackCRCXEntry": acPMMGCPLoopbackCRCXEntry,
       "acPMMGCPLoopbackCRCXInterval": acPMMGCPLoopbackCRCXInterval,
       "acPMMGCPLoopbackCRCXVal": acPMMGCPLoopbackCRCXVal,
       "acPMMGCPFailedLoopbackCRCXTable": acPMMGCPFailedLoopbackCRCXTable,
       "acPMMGCPFailedLoopbackCRCXEntry": acPMMGCPFailedLoopbackCRCXEntry,
       "acPMMGCPFailedLoopbackCRCXInterval": acPMMGCPFailedLoopbackCRCXInterval,
       "acPMMGCPFailedLoopbackCRCXVal": acPMMGCPFailedLoopbackCRCXVal,
       "acPMMGCPGeneratedNTFYTable": acPMMGCPGeneratedNTFYTable,
       "acPMMGCPGeneratedNTFYEntry": acPMMGCPGeneratedNTFYEntry,
       "acPMMGCPGeneratedNTFYInterval": acPMMGCPGeneratedNTFYInterval,
       "acPMMGCPGeneratedNTFYVal": acPMMGCPGeneratedNTFYVal,
       "acPMMGCPFailedNTFYResponsesTable": acPMMGCPFailedNTFYResponsesTable,
       "acPMMGCPFailedNTFYResponsesEntry": acPMMGCPFailedNTFYResponsesEntry,
       "acPMMGCPFailedNTFYResponsesInterval": acPMMGCPFailedNTFYResponsesInterval,
       "acPMMGCPFailedNTFYResponsesVal": acPMMGCPFailedNTFYResponsesVal,
       "acPMMGCPFailedRSIPResponsesTable": acPMMGCPFailedRSIPResponsesTable,
       "acPMMGCPFailedRSIPResponsesEntry": acPMMGCPFailedRSIPResponsesEntry,
       "acPMMGCPFailedRSIPResponsesInterval": acPMMGCPFailedRSIPResponsesInterval,
       "acPMMGCPFailedRSIPResponsesVal": acPMMGCPFailedRSIPResponsesVal,
       "acPMMGCPFailedCRCXResponsesTable": acPMMGCPFailedCRCXResponsesTable,
       "acPMMGCPFailedCRCXResponsesEntry": acPMMGCPFailedCRCXResponsesEntry,
       "acPMMGCPFailedCRCXResponsesReasonCode": acPMMGCPFailedCRCXResponsesReasonCode,
       "acPMMGCPFailedCRCXResponsesInterval": acPMMGCPFailedCRCXResponsesInterval,
       "acPMMGCPFailedCRCXResponsesVal": acPMMGCPFailedCRCXResponsesVal,
       "acPMMGCPFailedMDCXResponsesTable": acPMMGCPFailedMDCXResponsesTable,
       "acPMMGCPFailedMDCXResponsesEntry": acPMMGCPFailedMDCXResponsesEntry,
       "acPMMGCPFailedMDCXResponsesReasonCode": acPMMGCPFailedMDCXResponsesReasonCode,
       "acPMMGCPFailedMDCXResponsesInterval": acPMMGCPFailedMDCXResponsesInterval,
       "acPMMGCPFailedMDCXResponsesVal": acPMMGCPFailedMDCXResponsesVal,
       "acPMMGCPGeneratedDLCXPerReasonCodeTable": acPMMGCPGeneratedDLCXPerReasonCodeTable,
       "acPMMGCPGeneratedDLCXPerReasonCodeEntry": acPMMGCPGeneratedDLCXPerReasonCodeEntry,
       "acPMMGCPGeneratedDLCXPerReasonCodeReasonCode": acPMMGCPGeneratedDLCXPerReasonCodeReasonCode,
       "acPMMGCPGeneratedDLCXPerReasonCodeInterval": acPMMGCPGeneratedDLCXPerReasonCodeInterval,
       "acPMMGCPGeneratedDLCXPerReasonCodeVal": acPMMGCPGeneratedDLCXPerReasonCodeVal,
       "acPMSIP": acPMSIP,
       "acPMSIPAttemptedCallsTable": acPMSIPAttemptedCallsTable,
       "acPMSIPAttemptedCallsEntry": acPMSIPAttemptedCallsEntry,
       "acPMSIPAttemptedCallsDirection": acPMSIPAttemptedCallsDirection,
       "acPMSIPAttemptedCallsInterval": acPMSIPAttemptedCallsInterval,
       "acPMSIPAttemptedCallsVal": acPMSIPAttemptedCallsVal,
       "acPMSIPCallDurationTable": acPMSIPCallDurationTable,
       "acPMSIPCallDurationEntry": acPMSIPCallDurationEntry,
       "acPMSIPCallDurationDirection": acPMSIPCallDurationDirection,
       "acPMSIPCallDurationInterval": acPMSIPCallDurationInterval,
       "acPMSIPCallDurationVal": acPMSIPCallDurationVal,
       "acPMSIPCallDurationAverage": acPMSIPCallDurationAverage,
       "acPMSIPCallDurationMax": acPMSIPCallDurationMax,
       "acPMSIPCallDurationMin": acPMSIPCallDurationMin,
       "acPMSIPCallDurationVolume": acPMSIPCallDurationVolume,
       "acPMSIPCallDurationTimeBelowLowThreshold": acPMSIPCallDurationTimeBelowLowThreshold,
       "acPMSIPCallDurationTimeBetweenThresholds": acPMSIPCallDurationTimeBetweenThresholds,
       "acPMSIPCallDurationTimeAboveHighThreshold": acPMSIPCallDurationTimeAboveHighThreshold,
       "acPMSIPCallDurationFullDayAverage": acPMSIPCallDurationFullDayAverage,
       "acPMSIPCallDurationTotal": acPMSIPCallDurationTotal,
       "acPMSIPNoMatchCallsTable": acPMSIPNoMatchCallsTable,
       "acPMSIPNoMatchCallsEntry": acPMSIPNoMatchCallsEntry,
       "acPMSIPNoMatchCallsDirection": acPMSIPNoMatchCallsDirection,
       "acPMSIPNoMatchCallsInterval": acPMSIPNoMatchCallsInterval,
       "acPMSIPNoMatchCallsVal": acPMSIPNoMatchCallsVal,
       "acPMSIPBusyCallsTable": acPMSIPBusyCallsTable,
       "acPMSIPBusyCallsEntry": acPMSIPBusyCallsEntry,
       "acPMSIPBusyCallsDirection": acPMSIPBusyCallsDirection,
       "acPMSIPBusyCallsInterval": acPMSIPBusyCallsInterval,
       "acPMSIPBusyCallsVal": acPMSIPBusyCallsVal,
       "acPMSIPNoAnswerCallsTable": acPMSIPNoAnswerCallsTable,
       "acPMSIPNoAnswerCallsEntry": acPMSIPNoAnswerCallsEntry,
       "acPMSIPNoAnswerCallsDirection": acPMSIPNoAnswerCallsDirection,
       "acPMSIPNoAnswerCallsInterval": acPMSIPNoAnswerCallsInterval,
       "acPMSIPNoAnswerCallsVal": acPMSIPNoAnswerCallsVal,
       "acPMSIPNoRouteCallsTable": acPMSIPNoRouteCallsTable,
       "acPMSIPNoRouteCallsEntry": acPMSIPNoRouteCallsEntry,
       "acPMSIPNoRouteCallsDirection": acPMSIPNoRouteCallsDirection,
       "acPMSIPNoRouteCallsInterval": acPMSIPNoRouteCallsInterval,
       "acPMSIPNoRouteCallsVal": acPMSIPNoRouteCallsVal,
       "acPMSIPFailCallsTable": acPMSIPFailCallsTable,
       "acPMSIPFailCallsEntry": acPMSIPFailCallsEntry,
       "acPMSIPFailCallsDirection": acPMSIPFailCallsDirection,
       "acPMSIPFailCallsInterval": acPMSIPFailCallsInterval,
       "acPMSIPFailCallsVal": acPMSIPFailCallsVal,
       "acPMSIPEstablishedCallsTable": acPMSIPEstablishedCallsTable,
       "acPMSIPEstablishedCallsEntry": acPMSIPEstablishedCallsEntry,
       "acPMSIPEstablishedCallsDirection": acPMSIPEstablishedCallsDirection,
       "acPMSIPEstablishedCallsInterval": acPMSIPEstablishedCallsInterval,
       "acPMSIPEstablishedCallsVal": acPMSIPEstablishedCallsVal,
       "acPMSIPFaxAttemptedCallsTable": acPMSIPFaxAttemptedCallsTable,
       "acPMSIPFaxAttemptedCallsEntry": acPMSIPFaxAttemptedCallsEntry,
       "acPMSIPFaxAttemptedCallsDirection": acPMSIPFaxAttemptedCallsDirection,
       "acPMSIPFaxAttemptedCallsInterval": acPMSIPFaxAttemptedCallsInterval,
       "acPMSIPFaxAttemptedCallsVal": acPMSIPFaxAttemptedCallsVal,
       "acPMSIPFaxSuccessCallsTable": acPMSIPFaxSuccessCallsTable,
       "acPMSIPFaxSuccessCallsEntry": acPMSIPFaxSuccessCallsEntry,
       "acPMSIPFaxSuccessCallsDirection": acPMSIPFaxSuccessCallsDirection,
       "acPMSIPFaxSuccessCallsInterval": acPMSIPFaxSuccessCallsInterval,
       "acPMSIPFaxSuccessCallsVal": acPMSIPFaxSuccessCallsVal,
       "acPMSIPForwardedCallsTable": acPMSIPForwardedCallsTable,
       "acPMSIPForwardedCallsEntry": acPMSIPForwardedCallsEntry,
       "acPMSIPForwardedCallsDirection": acPMSIPForwardedCallsDirection,
       "acPMSIPForwardedCallsInterval": acPMSIPForwardedCallsInterval,
       "acPMSIPForwardedCallsVal": acPMSIPForwardedCallsVal,
       "acPMSIPNoResourcesCallsTable": acPMSIPNoResourcesCallsTable,
       "acPMSIPNoResourcesCallsEntry": acPMSIPNoResourcesCallsEntry,
       "acPMSIPNoResourcesCallsDirection": acPMSIPNoResourcesCallsDirection,
       "acPMSIPNoResourcesCallsInterval": acPMSIPNoResourcesCallsInterval,
       "acPMSIPNoResourcesCallsVal": acPMSIPNoResourcesCallsVal,
       "acPMSIPTel2IPTrunkEstablishedCallsTable": acPMSIPTel2IPTrunkEstablishedCallsTable,
       "acPMSIPTel2IPTrunkEstablishedCallsEntry": acPMSIPTel2IPTrunkEstablishedCallsEntry,
       "acPMSIPTel2IPTrunkEstablishedCallsTrunkNum": acPMSIPTel2IPTrunkEstablishedCallsTrunkNum,
       "acPMSIPTel2IPTrunkEstablishedCallsInterval": acPMSIPTel2IPTrunkEstablishedCallsInterval,
       "acPMSIPTel2IPTrunkEstablishedCallsVal": acPMSIPTel2IPTrunkEstablishedCallsVal,
       "acPMSIPIP2TelTrunkEstablishedCallsTable": acPMSIPIP2TelTrunkEstablishedCallsTable,
       "acPMSIPIP2TelTrunkEstablishedCallsEntry": acPMSIPIP2TelTrunkEstablishedCallsEntry,
       "acPMSIPIP2TelTrunkEstablishedCallsTrunkNum": acPMSIPIP2TelTrunkEstablishedCallsTrunkNum,
       "acPMSIPIP2TelTrunkEstablishedCallsInterval": acPMSIPIP2TelTrunkEstablishedCallsInterval,
       "acPMSIPIP2TelTrunkEstablishedCallsVal": acPMSIPIP2TelTrunkEstablishedCallsVal,
       "acPMSIPTel2IPTrunkGroupEstablishedCallsTable": acPMSIPTel2IPTrunkGroupEstablishedCallsTable,
       "acPMSIPTel2IPTrunkGroupEstablishedCallsEntry": acPMSIPTel2IPTrunkGroupEstablishedCallsEntry,
       "acPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum": acPMSIPTel2IPTrunkGroupEstablishedCallsGroupNum,
       "acPMSIPTel2IPTrunkGroupEstablishedCallsInterval": acPMSIPTel2IPTrunkGroupEstablishedCallsInterval,
       "acPMSIPTel2IPTrunkGroupEstablishedCallsVal": acPMSIPTel2IPTrunkGroupEstablishedCallsVal,
       "acPMSIPIP2TelTrunkGroupEstablishedCallsTable": acPMSIPIP2TelTrunkGroupEstablishedCallsTable,
       "acPMSIPIP2TelTrunkGroupEstablishedCallsEntry": acPMSIPIP2TelTrunkGroupEstablishedCallsEntry,
       "acPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum": acPMSIPIP2TelTrunkGroupEstablishedCallsGroupNum,
       "acPMSIPIP2TelTrunkGroupEstablishedCallsInterval": acPMSIPIP2TelTrunkGroupEstablishedCallsInterval,
       "acPMSIPIP2TelTrunkGroupEstablishedCallsVal": acPMSIPIP2TelTrunkGroupEstablishedCallsVal,
       "acPMSIPSRDDialogsTable": acPMSIPSRDDialogsTable,
       "acPMSIPSRDDialogsEntry": acPMSIPSRDDialogsEntry,
       "acPMSIPSRDDialogsSrdNum": acPMSIPSRDDialogsSrdNum,
       "acPMSIPSRDDialogsInterval": acPMSIPSRDDialogsInterval,
       "acPMSIPSRDDialogsVal": acPMSIPSRDDialogsVal,
       "acPMSIPSRDInviteDialogsTable": acPMSIPSRDInviteDialogsTable,
       "acPMSIPSRDInviteDialogsEntry": acPMSIPSRDInviteDialogsEntry,
       "acPMSIPSRDInviteDialogsSrdNum": acPMSIPSRDInviteDialogsSrdNum,
       "acPMSIPSRDInviteDialogsInterval": acPMSIPSRDInviteDialogsInterval,
       "acPMSIPSRDInviteDialogsVal": acPMSIPSRDInviteDialogsVal,
       "acPMSIPSRDSubscribeDialogsTable": acPMSIPSRDSubscribeDialogsTable,
       "acPMSIPSRDSubscribeDialogsEntry": acPMSIPSRDSubscribeDialogsEntry,
       "acPMSIPSRDSubscribeDialogsSrdNum": acPMSIPSRDSubscribeDialogsSrdNum,
       "acPMSIPSRDSubscribeDialogsInterval": acPMSIPSRDSubscribeDialogsInterval,
       "acPMSIPSRDSubscribeDialogsVal": acPMSIPSRDSubscribeDialogsVal,
       "acPMSIPSRDOtherDialogsTable": acPMSIPSRDOtherDialogsTable,
       "acPMSIPSRDOtherDialogsEntry": acPMSIPSRDOtherDialogsEntry,
       "acPMSIPSRDOtherDialogsSrdNum": acPMSIPSRDOtherDialogsSrdNum,
       "acPMSIPSRDOtherDialogsInterval": acPMSIPSRDOtherDialogsInterval,
       "acPMSIPSRDOtherDialogsVal": acPMSIPSRDOtherDialogsVal,
       "acPMSIPIPGroupDialogsTable": acPMSIPIPGroupDialogsTable,
       "acPMSIPIPGroupDialogsEntry": acPMSIPIPGroupDialogsEntry,
       "acPMSIPIPGroupDialogsIPGroupNum": acPMSIPIPGroupDialogsIPGroupNum,
       "acPMSIPIPGroupDialogsInterval": acPMSIPIPGroupDialogsInterval,
       "acPMSIPIPGroupDialogsVal": acPMSIPIPGroupDialogsVal,
       "acPMSIPIPGroupInviteDialogsTable": acPMSIPIPGroupInviteDialogsTable,
       "acPMSIPIPGroupInviteDialogsEntry": acPMSIPIPGroupInviteDialogsEntry,
       "acPMSIPIPGroupInviteDialogsIPGroupNum": acPMSIPIPGroupInviteDialogsIPGroupNum,
       "acPMSIPIPGroupInviteDialogsInterval": acPMSIPIPGroupInviteDialogsInterval,
       "acPMSIPIPGroupInviteDialogsVal": acPMSIPIPGroupInviteDialogsVal,
       "acPMSIPIPGroupInviteDialogsAverage": acPMSIPIPGroupInviteDialogsAverage,
       "acPMSIPIPGroupInviteDialogsMax": acPMSIPIPGroupInviteDialogsMax,
       "acPMSIPIPGroupInviteDialogsMin": acPMSIPIPGroupInviteDialogsMin,
       "acPMSIPIPGroupInviteDialogsTimeBelowLowThreshold": acPMSIPIPGroupInviteDialogsTimeBelowLowThreshold,
       "acPMSIPIPGroupInviteDialogsTimeBetweenThresholds": acPMSIPIPGroupInviteDialogsTimeBetweenThresholds,
       "acPMSIPIPGroupInviteDialogsTimeAboveHighThreshold": acPMSIPIPGroupInviteDialogsTimeAboveHighThreshold,
       "acPMSIPIPGroupSubscribeDialogsTable": acPMSIPIPGroupSubscribeDialogsTable,
       "acPMSIPIPGroupSubscribeDialogsEntry": acPMSIPIPGroupSubscribeDialogsEntry,
       "acPMSIPIPGroupSubscribeDialogsIPGroupNum": acPMSIPIPGroupSubscribeDialogsIPGroupNum,
       "acPMSIPIPGroupSubscribeDialogsInterval": acPMSIPIPGroupSubscribeDialogsInterval,
       "acPMSIPIPGroupSubscribeDialogsVal": acPMSIPIPGroupSubscribeDialogsVal,
       "acPMSIPIPGroupOtherDialogsTable": acPMSIPIPGroupOtherDialogsTable,
       "acPMSIPIPGroupOtherDialogsEntry": acPMSIPIPGroupOtherDialogsEntry,
       "acPMSIPIPGroupOtherDialogsIPGroupNum": acPMSIPIPGroupOtherDialogsIPGroupNum,
       "acPMSIPIPGroupOtherDialogsInterval": acPMSIPIPGroupOtherDialogsInterval,
       "acPMSIPIPGroupOtherDialogsVal": acPMSIPIPGroupOtherDialogsVal,
       "acPMSIPTrunkGroupAllTrunksBusyTable": acPMSIPTrunkGroupAllTrunksBusyTable,
       "acPMSIPTrunkGroupAllTrunksBusyEntry": acPMSIPTrunkGroupAllTrunksBusyEntry,
       "acPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum": acPMSIPTrunkGroupAllTrunksBusyTrunkGroupNum,
       "acPMSIPTrunkGroupAllTrunksBusyInterval": acPMSIPTrunkGroupAllTrunksBusyInterval,
       "acPMSIPTrunkGroupAllTrunksBusyVal": acPMSIPTrunkGroupAllTrunksBusyVal,
       "acPMSIPTrunkGroupUtilizationTable": acPMSIPTrunkGroupUtilizationTable,
       "acPMSIPTrunkGroupUtilizationEntry": acPMSIPTrunkGroupUtilizationEntry,
       "acPMSIPTrunkGroupUtilizationTrunkGroupNum": acPMSIPTrunkGroupUtilizationTrunkGroupNum,
       "acPMSIPTrunkGroupUtilizationInterval": acPMSIPTrunkGroupUtilizationInterval,
       "acPMSIPTrunkGroupUtilizationVal": acPMSIPTrunkGroupUtilizationVal,
       "acPMSIPTrunkGroupUtilizationTimeBelowLowThreshold": acPMSIPTrunkGroupUtilizationTimeBelowLowThreshold,
       "acPMSIPTrunkGroupUtilizationTimeBetweenThresholds": acPMSIPTrunkGroupUtilizationTimeBetweenThresholds,
       "acPMSIPTrunkGroupUtilizationTimeAboveHighThreshold": acPMSIPTrunkGroupUtilizationTimeAboveHighThreshold,
       "acPMSIPTrunkGroupUtilizationAverage": acPMSIPTrunkGroupUtilizationAverage,
       "acPMSIPTrunkGroupUtilizationMax": acPMSIPTrunkGroupUtilizationMax,
       "acPMSIPTrunkGroupUtilizationMin": acPMSIPTrunkGroupUtilizationMin,
       "acPMSIPTrunkGroupUtilizationTotal": acPMSIPTrunkGroupUtilizationTotal,
       "acPMSIPTrunkGroupUtilizationFullDayAverage": acPMSIPTrunkGroupUtilizationFullDayAverage,
       "acPMSIPTrunkGroupPercentageUtilizationTable": acPMSIPTrunkGroupPercentageUtilizationTable,
       "acPMSIPTrunkGroupPercentageUtilizationEntry": acPMSIPTrunkGroupPercentageUtilizationEntry,
       "acPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum": acPMSIPTrunkGroupPercentageUtilizationTrunkGroupNum,
       "acPMSIPTrunkGroupPercentageUtilizationInterval": acPMSIPTrunkGroupPercentageUtilizationInterval,
       "acPMSIPTrunkGroupPercentageUtilizationVal": acPMSIPTrunkGroupPercentageUtilizationVal,
       "acPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold": acPMSIPTrunkGroupPercentageUtilizationTimeBelowLowThreshold,
       "acPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds": acPMSIPTrunkGroupPercentageUtilizationTimeBetweenThresholds,
       "acPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold": acPMSIPTrunkGroupPercentageUtilizationTimeAboveHighThreshold,
       "acPMSIPTrunkGroupPercentageUtilizationAverage": acPMSIPTrunkGroupPercentageUtilizationAverage,
       "acPMSIPTrunkGroupPercentageUtilizationMax": acPMSIPTrunkGroupPercentageUtilizationMax,
       "acPMSIPTrunkGroupPercentageUtilizationMin": acPMSIPTrunkGroupPercentageUtilizationMin,
       "acPMSIPTrunkGroupPercentageUtilizationFullDayAverage": acPMSIPTrunkGroupPercentageUtilizationFullDayAverage,
       "acPMSIPTrunkGroupNoResourcesCallsTable": acPMSIPTrunkGroupNoResourcesCallsTable,
       "acPMSIPTrunkGroupNoResourcesCallsEntry": acPMSIPTrunkGroupNoResourcesCallsEntry,
       "acPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum": acPMSIPTrunkGroupNoResourcesCallsTrunkGroupNum,
       "acPMSIPTrunkGroupNoResourcesCallsInterval": acPMSIPTrunkGroupNoResourcesCallsInterval,
       "acPMSIPTrunkGroupNoResourcesCallsVal": acPMSIPTrunkGroupNoResourcesCallsVal,
       "acPMSIPTrunkGroupNoResourcesCallsTotal": acPMSIPTrunkGroupNoResourcesCallsTotal,
       "acPMSIPTrunkGroupCallDurationTable": acPMSIPTrunkGroupCallDurationTable,
       "acPMSIPTrunkGroupCallDurationEntry": acPMSIPTrunkGroupCallDurationEntry,
       "acPMSIPTrunkGroupCallDurationTrunkGroupNum": acPMSIPTrunkGroupCallDurationTrunkGroupNum,
       "acPMSIPTrunkGroupCallDurationInterval": acPMSIPTrunkGroupCallDurationInterval,
       "acPMSIPTrunkGroupCallDurationVal": acPMSIPTrunkGroupCallDurationVal,
       "acPMSIPTrunkGroupCallDurationAverage": acPMSIPTrunkGroupCallDurationAverage,
       "acPMSIPTrunkGroupCallDurationMax": acPMSIPTrunkGroupCallDurationMax,
       "acPMSIPTrunkGroupCallDurationMin": acPMSIPTrunkGroupCallDurationMin,
       "acPMSIPTrunkGroupCallDurationTotal": acPMSIPTrunkGroupCallDurationTotal,
       "acPMSIPTrunkGroupCallDurationFullDayAverage": acPMSIPTrunkGroupCallDurationFullDayAverage,
       "acPMSIPTrunkGroupAllTrunksBusyPercentageTable": acPMSIPTrunkGroupAllTrunksBusyPercentageTable,
       "acPMSIPTrunkGroupAllTrunksBusyPercentageEntry": acPMSIPTrunkGroupAllTrunksBusyPercentageEntry,
       "acPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum": acPMSIPTrunkGroupAllTrunksBusyPercentageTrunkGroupNum,
       "acPMSIPTrunkGroupAllTrunksBusyPercentageInterval": acPMSIPTrunkGroupAllTrunksBusyPercentageInterval,
       "acPMSIPTrunkGroupAllTrunksBusyPercentageVal": acPMSIPTrunkGroupAllTrunksBusyPercentageVal,
       "acPMMediaRealm": acPMMediaRealm,
       "acPMMediaRealmBytesTxTable": acPMMediaRealmBytesTxTable,
       "acPMMediaRealmBytesTxEntry": acPMMediaRealmBytesTxEntry,
       "acPMMediaRealmBytesTxMediaRealmNum": acPMMediaRealmBytesTxMediaRealmNum,
       "acPMMediaRealmBytesTxInterval": acPMMediaRealmBytesTxInterval,
       "acPMMediaRealmBytesTxVal": acPMMediaRealmBytesTxVal,
       "acPMMediaRealmBytesTxVolume": acPMMediaRealmBytesTxVolume,
       "acPMMediaRealmBytesRxTable": acPMMediaRealmBytesRxTable,
       "acPMMediaRealmBytesRxEntry": acPMMediaRealmBytesRxEntry,
       "acPMMediaRealmBytesRxMediaRealmNum": acPMMediaRealmBytesRxMediaRealmNum,
       "acPMMediaRealmBytesRxInterval": acPMMediaRealmBytesRxInterval,
       "acPMMediaRealmBytesRxVal": acPMMediaRealmBytesRxVal,
       "acPMMediaRealmBytesRxVolume": acPMMediaRealmBytesRxVolume,
       "acPMMediaRealmPacketsTxTable": acPMMediaRealmPacketsTxTable,
       "acPMMediaRealmPacketsTxEntry": acPMMediaRealmPacketsTxEntry,
       "acPMMediaRealmPacketsTxMediaRealmNum": acPMMediaRealmPacketsTxMediaRealmNum,
       "acPMMediaRealmPacketsTxInterval": acPMMediaRealmPacketsTxInterval,
       "acPMMediaRealmPacketsTxVal": acPMMediaRealmPacketsTxVal,
       "acPMMediaRealmPacketsTxVolume": acPMMediaRealmPacketsTxVolume,
       "acPMMediaRealmPacketsRxTable": acPMMediaRealmPacketsRxTable,
       "acPMMediaRealmPacketsRxEntry": acPMMediaRealmPacketsRxEntry,
       "acPMMediaRealmPacketsRxMediaRealmNum": acPMMediaRealmPacketsRxMediaRealmNum,
       "acPMMediaRealmPacketsRxInterval": acPMMediaRealmPacketsRxInterval,
       "acPMMediaRealmPacketsRxVal": acPMMediaRealmPacketsRxVal,
       "acPMMediaRealmPacketsRxVolume": acPMMediaRealmPacketsRxVolume,
       "acPMMediaRealmVERealmPacketDelayTable": acPMMediaRealmVERealmPacketDelayTable,
       "acPMMediaRealmVERealmPacketDelayEntry": acPMMediaRealmVERealmPacketDelayEntry,
       "acPMMediaRealmVERealmPacketDelayMediaRealmNum": acPMMediaRealmVERealmPacketDelayMediaRealmNum,
       "acPMMediaRealmVERealmPacketDelayInterval": acPMMediaRealmVERealmPacketDelayInterval,
       "acPMMediaRealmVERealmPacketDelayVal": acPMMediaRealmVERealmPacketDelayVal,
       "acPMMediaRealmVERealmPacketDelayAverage": acPMMediaRealmVERealmPacketDelayAverage,
       "acPMMediaRealmVERealmPacketDelayMax": acPMMediaRealmVERealmPacketDelayMax,
       "acPMMediaRealmVERealmPacketDelayMin": acPMMediaRealmVERealmPacketDelayMin,
       "acPMMediaRealmVERealmPacketJitterTable": acPMMediaRealmVERealmPacketJitterTable,
       "acPMMediaRealmVERealmPacketJitterEntry": acPMMediaRealmVERealmPacketJitterEntry,
       "acPMMediaRealmVERealmPacketJitterMediaRealmNum": acPMMediaRealmVERealmPacketJitterMediaRealmNum,
       "acPMMediaRealmVERealmPacketJitterInterval": acPMMediaRealmVERealmPacketJitterInterval,
       "acPMMediaRealmVERealmPacketJitterVal": acPMMediaRealmVERealmPacketJitterVal,
       "acPMMediaRealmVERealmPacketJitterAverage": acPMMediaRealmVERealmPacketJitterAverage,
       "acPMMediaRealmVERealmPacketJitterMax": acPMMediaRealmVERealmPacketJitterMax,
       "acPMMediaRealmVERealmPacketJitterMin": acPMMediaRealmVERealmPacketJitterMin,
       "acPMMediaRealmRealmMOSTable": acPMMediaRealmRealmMOSTable,
       "acPMMediaRealmRealmMOSEntry": acPMMediaRealmRealmMOSEntry,
       "acPMMediaRealmRealmMOSMediaRealmNum": acPMMediaRealmRealmMOSMediaRealmNum,
       "acPMMediaRealmRealmMOSInterval": acPMMediaRealmRealmMOSInterval,
       "acPMMediaRealmRealmMOSVal": acPMMediaRealmRealmMOSVal,
       "acPMMediaRealmRealmMOSAverage": acPMMediaRealmRealmMOSAverage,
       "acPMMediaRealmRealmMOSMax": acPMMediaRealmRealmMOSMax,
       "acPMMediaRealmRealmMOSMin": acPMMediaRealmRealmMOSMin,
       "acPMMediaRealmBwRxTable": acPMMediaRealmBwRxTable,
       "acPMMediaRealmBwRxEntry": acPMMediaRealmBwRxEntry,
       "acPMMediaRealmBwRxMediaRealmNum": acPMMediaRealmBwRxMediaRealmNum,
       "acPMMediaRealmBwRxInterval": acPMMediaRealmBwRxInterval,
       "acPMMediaRealmBwRxVal": acPMMediaRealmBwRxVal,
       "acPMMediaRealmBwRxAverage": acPMMediaRealmBwRxAverage,
       "acPMMediaRealmBwRxMax": acPMMediaRealmBwRxMax,
       "acPMMediaRealmBwRxMin": acPMMediaRealmBwRxMin,
       "acPMMediaRealmBwRxTimeBelowLowThreshold": acPMMediaRealmBwRxTimeBelowLowThreshold,
       "acPMMediaRealmBwRxTimeBetweenThresholds": acPMMediaRealmBwRxTimeBetweenThresholds,
       "acPMMediaRealmBwRxTimeAboveHighThreshold": acPMMediaRealmBwRxTimeAboveHighThreshold,
       "acPMMediaRealmBwRxFullDayAverage": acPMMediaRealmBwRxFullDayAverage,
       "acPMMediaRealmBwRxTotal": acPMMediaRealmBwRxTotal,
       "acPMMediaRealmBwTxTable": acPMMediaRealmBwTxTable,
       "acPMMediaRealmBwTxEntry": acPMMediaRealmBwTxEntry,
       "acPMMediaRealmBwTxMediaRealmNum": acPMMediaRealmBwTxMediaRealmNum,
       "acPMMediaRealmBwTxInterval": acPMMediaRealmBwTxInterval,
       "acPMMediaRealmBwTxVal": acPMMediaRealmBwTxVal,
       "acPMMediaRealmBwTxAverage": acPMMediaRealmBwTxAverage,
       "acPMMediaRealmBwTxMax": acPMMediaRealmBwTxMax,
       "acPMMediaRealmBwTxMin": acPMMediaRealmBwTxMin,
       "acPMMediaRealmBwTxTimeBelowLowThreshold": acPMMediaRealmBwTxTimeBelowLowThreshold,
       "acPMMediaRealmBwTxTimeBetweenThresholds": acPMMediaRealmBwTxTimeBetweenThresholds,
       "acPMMediaRealmBwTxTimeAboveHighThreshold": acPMMediaRealmBwTxTimeAboveHighThreshold,
       "acPMMediaRealmBwTxFullDayAverage": acPMMediaRealmBwTxFullDayAverage,
       "acPMMediaRealmBwTxTotal": acPMMediaRealmBwTxTotal,
       "acPMMediaRealmPacketLossRxTable": acPMMediaRealmPacketLossRxTable,
       "acPMMediaRealmPacketLossRxEntry": acPMMediaRealmPacketLossRxEntry,
       "acPMMediaRealmPacketLossRxMediaRealmNum": acPMMediaRealmPacketLossRxMediaRealmNum,
       "acPMMediaRealmPacketLossRxInterval": acPMMediaRealmPacketLossRxInterval,
       "acPMMediaRealmPacketLossRxVal": acPMMediaRealmPacketLossRxVal,
       "acPMMediaRealmPacketLossRxVolume": acPMMediaRealmPacketLossRxVolume,
       "acPMMediaRealmPacketLossTxTable": acPMMediaRealmPacketLossTxTable,
       "acPMMediaRealmPacketLossTxEntry": acPMMediaRealmPacketLossTxEntry,
       "acPMMediaRealmPacketLossTxMediaRealmNum": acPMMediaRealmPacketLossTxMediaRealmNum,
       "acPMMediaRealmPacketLossTxInterval": acPMMediaRealmPacketLossTxInterval,
       "acPMMediaRealmPacketLossTxVal": acPMMediaRealmPacketLossTxVal,
       "acPMMediaRealmPacketLossTxVolume": acPMMediaRealmPacketLossTxVolume}
)
