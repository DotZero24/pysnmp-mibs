# SNMP MIB module (MX-TELEPHONY-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-TELEPHONY-SERVICES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:06:05 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(mediatrixConfig,) = mibBuilder.importSymbols(
    "MX-SMI",
    "mediatrixConfig")

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

telephonyServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60)
)
if mibBuilder.loadTexts:
    telephonyServicesMIB.setRevisions(
        ("1903-04-30 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TelephonyServicesMIBObjects_ObjectIdentity = ObjectIdentity
telephonyServicesMIBObjects = _TelephonyServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1)
)
_TelephonyServicesIfActivationTable_Object = MibTable
telephonyServicesIfActivationTable = _TelephonyServicesIfActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 10)
)
if mibBuilder.loadTexts:
    telephonyServicesIfActivationTable.setStatus("deprecated")
_TelephonyServicesIfActivationEntry_Object = MibTableRow
telephonyServicesIfActivationEntry = _TelephonyServicesIfActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 10, 1)
)
telephonyServicesIfActivationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyServicesIfActivationEntry.setStatus("deprecated")


class _TelephonyServicesHoldEnable_Type(Integer32):
    """Custom type telephonyServicesHoldEnable based on Integer32"""
    defaultValue = 1

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


_TelephonyServicesHoldEnable_Type.__name__ = "Integer32"
_TelephonyServicesHoldEnable_Object = MibTableColumn
telephonyServicesHoldEnable = _TelephonyServicesHoldEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 10, 1, 5),
    _TelephonyServicesHoldEnable_Type()
)
telephonyServicesHoldEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesHoldEnable.setStatus("deprecated")


class _TelephonyServicesCallWaitingEnable_Type(Integer32):
    """Custom type telephonyServicesCallWaitingEnable based on Integer32"""
    defaultValue = 1

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


_TelephonyServicesCallWaitingEnable_Type.__name__ = "Integer32"
_TelephonyServicesCallWaitingEnable_Object = MibTableColumn
telephonyServicesCallWaitingEnable = _TelephonyServicesCallWaitingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 10, 1, 10),
    _TelephonyServicesCallWaitingEnable_Type()
)
telephonyServicesCallWaitingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallWaitingEnable.setStatus("deprecated")


class _TelephonyServicesSecondCallEnable_Type(Integer32):
    """Custom type telephonyServicesSecondCallEnable based on Integer32"""
    defaultValue = 1

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


_TelephonyServicesSecondCallEnable_Type.__name__ = "Integer32"
_TelephonyServicesSecondCallEnable_Object = MibTableColumn
telephonyServicesSecondCallEnable = _TelephonyServicesSecondCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 10, 1, 15),
    _TelephonyServicesSecondCallEnable_Type()
)
telephonyServicesSecondCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesSecondCallEnable.setStatus("deprecated")


class _TelephonyServicesBlindTransferEnable_Type(Integer32):
    """Custom type telephonyServicesBlindTransferEnable based on Integer32"""
    defaultValue = 1

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


_TelephonyServicesBlindTransferEnable_Type.__name__ = "Integer32"
_TelephonyServicesBlindTransferEnable_Object = MibTableColumn
telephonyServicesBlindTransferEnable = _TelephonyServicesBlindTransferEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 10, 1, 20),
    _TelephonyServicesBlindTransferEnable_Type()
)
telephonyServicesBlindTransferEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesBlindTransferEnable.setStatus("deprecated")


class _TelephonyServicesAttendedTransferEnable_Type(Integer32):
    """Custom type telephonyServicesAttendedTransferEnable based on Integer32"""
    defaultValue = 1

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


_TelephonyServicesAttendedTransferEnable_Type.__name__ = "Integer32"
_TelephonyServicesAttendedTransferEnable_Object = MibTableColumn
telephonyServicesAttendedTransferEnable = _TelephonyServicesAttendedTransferEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 10, 1, 25),
    _TelephonyServicesAttendedTransferEnable_Type()
)
telephonyServicesAttendedTransferEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesAttendedTransferEnable.setStatus("deprecated")


class _TelephonyServicesConferenceEnable_Type(Integer32):
    """Custom type telephonyServicesConferenceEnable based on Integer32"""
    defaultValue = 1

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


_TelephonyServicesConferenceEnable_Type.__name__ = "Integer32"
_TelephonyServicesConferenceEnable_Object = MibTableColumn
telephonyServicesConferenceEnable = _TelephonyServicesConferenceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 10, 1, 30),
    _TelephonyServicesConferenceEnable_Type()
)
telephonyServicesConferenceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesConferenceEnable.setStatus("deprecated")
_TelephonyServicesIfStatusTable_Object = MibTable
telephonyServicesIfStatusTable = _TelephonyServicesIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 15)
)
if mibBuilder.loadTexts:
    telephonyServicesIfStatusTable.setStatus("deprecated")
_TelephonyServicesIfStatusEntry_Object = MibTableRow
telephonyServicesIfStatusEntry = _TelephonyServicesIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 15, 1)
)
telephonyServicesIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyServicesIfStatusEntry.setStatus("deprecated")


class _TelephonyServicesHoldStatus_Type(Integer32):
    """Custom type telephonyServicesHoldStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TelephonyServicesHoldStatus_Type.__name__ = "Integer32"
_TelephonyServicesHoldStatus_Object = MibTableColumn
telephonyServicesHoldStatus = _TelephonyServicesHoldStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 15, 1, 5),
    _TelephonyServicesHoldStatus_Type()
)
telephonyServicesHoldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyServicesHoldStatus.setStatus("deprecated")


class _TelephonyServicesCallWaitingStatus_Type(Integer32):
    """Custom type telephonyServicesCallWaitingStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TelephonyServicesCallWaitingStatus_Type.__name__ = "Integer32"
_TelephonyServicesCallWaitingStatus_Object = MibTableColumn
telephonyServicesCallWaitingStatus = _TelephonyServicesCallWaitingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 15, 1, 10),
    _TelephonyServicesCallWaitingStatus_Type()
)
telephonyServicesCallWaitingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyServicesCallWaitingStatus.setStatus("deprecated")


class _TelephonyServicesSecondCallStatus_Type(Integer32):
    """Custom type telephonyServicesSecondCallStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TelephonyServicesSecondCallStatus_Type.__name__ = "Integer32"
_TelephonyServicesSecondCallStatus_Object = MibTableColumn
telephonyServicesSecondCallStatus = _TelephonyServicesSecondCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 15, 1, 15),
    _TelephonyServicesSecondCallStatus_Type()
)
telephonyServicesSecondCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyServicesSecondCallStatus.setStatus("deprecated")


class _TelephonyServicesBlindTransferStatus_Type(Integer32):
    """Custom type telephonyServicesBlindTransferStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TelephonyServicesBlindTransferStatus_Type.__name__ = "Integer32"
_TelephonyServicesBlindTransferStatus_Object = MibTableColumn
telephonyServicesBlindTransferStatus = _TelephonyServicesBlindTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 15, 1, 20),
    _TelephonyServicesBlindTransferStatus_Type()
)
telephonyServicesBlindTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyServicesBlindTransferStatus.setStatus("deprecated")


class _TelephonyServicesAttendedTransferStatus_Type(Integer32):
    """Custom type telephonyServicesAttendedTransferStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TelephonyServicesAttendedTransferStatus_Type.__name__ = "Integer32"
_TelephonyServicesAttendedTransferStatus_Object = MibTableColumn
telephonyServicesAttendedTransferStatus = _TelephonyServicesAttendedTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 15, 1, 25),
    _TelephonyServicesAttendedTransferStatus_Type()
)
telephonyServicesAttendedTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyServicesAttendedTransferStatus.setStatus("deprecated")


class _TelephonyServicesConferenceStatus_Type(Integer32):
    """Custom type telephonyServicesConferenceStatus based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TelephonyServicesConferenceStatus_Type.__name__ = "Integer32"
_TelephonyServicesConferenceStatus_Object = MibTableColumn
telephonyServicesConferenceStatus = _TelephonyServicesConferenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 15, 1, 30),
    _TelephonyServicesConferenceStatus_Type()
)
telephonyServicesConferenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    telephonyServicesConferenceStatus.setStatus("deprecated")
_TelephonyServicesCustomization_ObjectIdentity = ObjectIdentity
telephonyServicesCustomization = _TelephonyServicesCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20)
)
_TelephonyServicesAutoSpeedDial_ObjectIdentity = ObjectIdentity
telephonyServicesAutoSpeedDial = _TelephonyServicesAutoSpeedDial_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 10)
)
_TelephonyServicesIfAutoSpeedDialTable_Object = MibTable
telephonyServicesIfAutoSpeedDialTable = _TelephonyServicesIfAutoSpeedDialTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 10, 10)
)
if mibBuilder.loadTexts:
    telephonyServicesIfAutoSpeedDialTable.setStatus("deprecated")
_TelephonyServicesIfAutoSpeedDialEntry_Object = MibTableRow
telephonyServicesIfAutoSpeedDialEntry = _TelephonyServicesIfAutoSpeedDialEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 10, 10, 1)
)
telephonyServicesIfAutoSpeedDialEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyServicesIfAutoSpeedDialEntry.setStatus("deprecated")


class _TelephonyServicesAutoSpeedDialEnable_Type(Integer32):
    """Custom type telephonyServicesAutoSpeedDialEnable based on Integer32"""
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


_TelephonyServicesAutoSpeedDialEnable_Type.__name__ = "Integer32"
_TelephonyServicesAutoSpeedDialEnable_Object = MibTableColumn
telephonyServicesAutoSpeedDialEnable = _TelephonyServicesAutoSpeedDialEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 10, 10, 1, 5),
    _TelephonyServicesAutoSpeedDialEnable_Type()
)
telephonyServicesAutoSpeedDialEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesAutoSpeedDialEnable.setStatus("deprecated")


class _TelephonyServicesAutoSpeedDialTargetAddress_Type(OctetString):
    """Custom type telephonyServicesAutoSpeedDialTargetAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TelephonyServicesAutoSpeedDialTargetAddress_Type.__name__ = "OctetString"
_TelephonyServicesAutoSpeedDialTargetAddress_Object = MibTableColumn
telephonyServicesAutoSpeedDialTargetAddress = _TelephonyServicesAutoSpeedDialTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 10, 10, 1, 10),
    _TelephonyServicesAutoSpeedDialTargetAddress_Type()
)
telephonyServicesAutoSpeedDialTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesAutoSpeedDialTargetAddress.setStatus("deprecated")
_TelephonyServicesCallForwardCustomization_ObjectIdentity = ObjectIdentity
telephonyServicesCallForwardCustomization = _TelephonyServicesCallForwardCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20)
)
_TelephonyServicesCallForwardUnconditionnal_ObjectIdentity = ObjectIdentity
telephonyServicesCallForwardUnconditionnal = _TelephonyServicesCallForwardUnconditionnal_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 5)
)


class _TelephonyServicesCallForwardUnconditionnalEnableDigitMap_Type(OctetString):
    """Custom type telephonyServicesCallForwardUnconditionnalEnableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TelephonyServicesCallForwardUnconditionnalEnableDigitMap_Type.__name__ = "OctetString"
_TelephonyServicesCallForwardUnconditionnalEnableDigitMap_Object = MibScalar
telephonyServicesCallForwardUnconditionnalEnableDigitMap = _TelephonyServicesCallForwardUnconditionnalEnableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 5, 5),
    _TelephonyServicesCallForwardUnconditionnalEnableDigitMap_Type()
)
telephonyServicesCallForwardUnconditionnalEnableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardUnconditionnalEnableDigitMap.setStatus("deprecated")


class _TelephonyServicesCallForwardUnconditionnalDisableDigitMap_Type(OctetString):
    """Custom type telephonyServicesCallForwardUnconditionnalDisableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TelephonyServicesCallForwardUnconditionnalDisableDigitMap_Type.__name__ = "OctetString"
_TelephonyServicesCallForwardUnconditionnalDisableDigitMap_Object = MibScalar
telephonyServicesCallForwardUnconditionnalDisableDigitMap = _TelephonyServicesCallForwardUnconditionnalDisableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 5, 10),
    _TelephonyServicesCallForwardUnconditionnalDisableDigitMap_Type()
)
telephonyServicesCallForwardUnconditionnalDisableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardUnconditionnalDisableDigitMap.setStatus("deprecated")
_TelephonyServicesIfCallForwardUnconditionnalTable_Object = MibTable
telephonyServicesIfCallForwardUnconditionnalTable = _TelephonyServicesIfCallForwardUnconditionnalTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 5, 15)
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardUnconditionnalTable.setStatus("deprecated")
_TelephonyServicesIfCallForwardUnconditionnalEntry_Object = MibTableRow
telephonyServicesIfCallForwardUnconditionnalEntry = _TelephonyServicesIfCallForwardUnconditionnalEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 5, 15, 1)
)
telephonyServicesIfCallForwardUnconditionnalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardUnconditionnalEntry.setStatus("deprecated")


class _TelephonyServicesCallForwardUnconditionnalEnable_Type(Integer32):
    """Custom type telephonyServicesCallForwardUnconditionnalEnable based on Integer32"""
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


_TelephonyServicesCallForwardUnconditionnalEnable_Type.__name__ = "Integer32"
_TelephonyServicesCallForwardUnconditionnalEnable_Object = MibTableColumn
telephonyServicesCallForwardUnconditionnalEnable = _TelephonyServicesCallForwardUnconditionnalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 5, 15, 1, 5),
    _TelephonyServicesCallForwardUnconditionnalEnable_Type()
)
telephonyServicesCallForwardUnconditionnalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardUnconditionnalEnable.setStatus("deprecated")


class _TelephonyServicesCallForwardUnconditionnalForwardingAddress_Type(OctetString):
    """Custom type telephonyServicesCallForwardUnconditionnalForwardingAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TelephonyServicesCallForwardUnconditionnalForwardingAddress_Type.__name__ = "OctetString"
_TelephonyServicesCallForwardUnconditionnalForwardingAddress_Object = MibTableColumn
telephonyServicesCallForwardUnconditionnalForwardingAddress = _TelephonyServicesCallForwardUnconditionnalForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 5, 15, 1, 10),
    _TelephonyServicesCallForwardUnconditionnalForwardingAddress_Type()
)
telephonyServicesCallForwardUnconditionnalForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardUnconditionnalForwardingAddress.setStatus("deprecated")
_TelephonyServicesIfCallForwardUnconditionnalActivationTable_Object = MibTable
telephonyServicesIfCallForwardUnconditionnalActivationTable = _TelephonyServicesIfCallForwardUnconditionnalActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 5, 20)
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardUnconditionnalActivationTable.setStatus("deprecated")
_TelephonyServicesIfCallForwardUnconditionnalActivationEntry_Object = MibTableRow
telephonyServicesIfCallForwardUnconditionnalActivationEntry = _TelephonyServicesIfCallForwardUnconditionnalActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 5, 20, 1)
)
telephonyServicesIfCallForwardUnconditionnalActivationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardUnconditionnalActivationEntry.setStatus("deprecated")


class _TelephonyServicesCallForwardUnconditionnalActivation_Type(Integer32):
    """Custom type telephonyServicesCallForwardUnconditionnalActivation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TelephonyServicesCallForwardUnconditionnalActivation_Type.__name__ = "Integer32"
_TelephonyServicesCallForwardUnconditionnalActivation_Object = MibTableColumn
telephonyServicesCallForwardUnconditionnalActivation = _TelephonyServicesCallForwardUnconditionnalActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 5, 20, 1, 5),
    _TelephonyServicesCallForwardUnconditionnalActivation_Type()
)
telephonyServicesCallForwardUnconditionnalActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardUnconditionnalActivation.setStatus("deprecated")
_TelephonyServicesCallForwardBusy_ObjectIdentity = ObjectIdentity
telephonyServicesCallForwardBusy = _TelephonyServicesCallForwardBusy_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 10)
)


class _TelephonyServicesCallForwardBusyEnableDigitMap_Type(OctetString):
    """Custom type telephonyServicesCallForwardBusyEnableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TelephonyServicesCallForwardBusyEnableDigitMap_Type.__name__ = "OctetString"
_TelephonyServicesCallForwardBusyEnableDigitMap_Object = MibScalar
telephonyServicesCallForwardBusyEnableDigitMap = _TelephonyServicesCallForwardBusyEnableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 10, 5),
    _TelephonyServicesCallForwardBusyEnableDigitMap_Type()
)
telephonyServicesCallForwardBusyEnableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardBusyEnableDigitMap.setStatus("deprecated")


class _TelephonyServicesCallForwardBusyDisableDigitMap_Type(OctetString):
    """Custom type telephonyServicesCallForwardBusyDisableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TelephonyServicesCallForwardBusyDisableDigitMap_Type.__name__ = "OctetString"
_TelephonyServicesCallForwardBusyDisableDigitMap_Object = MibScalar
telephonyServicesCallForwardBusyDisableDigitMap = _TelephonyServicesCallForwardBusyDisableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 10, 10),
    _TelephonyServicesCallForwardBusyDisableDigitMap_Type()
)
telephonyServicesCallForwardBusyDisableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardBusyDisableDigitMap.setStatus("deprecated")
_TelephonyServicesIfCallForwardBusyTable_Object = MibTable
telephonyServicesIfCallForwardBusyTable = _TelephonyServicesIfCallForwardBusyTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 10, 15)
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardBusyTable.setStatus("deprecated")
_TelephonyServicesIfCallForwardBusyEntry_Object = MibTableRow
telephonyServicesIfCallForwardBusyEntry = _TelephonyServicesIfCallForwardBusyEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 10, 15, 1)
)
telephonyServicesIfCallForwardBusyEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardBusyEntry.setStatus("deprecated")


class _TelephonyServicesCallForwardBusyEnable_Type(Integer32):
    """Custom type telephonyServicesCallForwardBusyEnable based on Integer32"""
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


_TelephonyServicesCallForwardBusyEnable_Type.__name__ = "Integer32"
_TelephonyServicesCallForwardBusyEnable_Object = MibTableColumn
telephonyServicesCallForwardBusyEnable = _TelephonyServicesCallForwardBusyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 10, 15, 1, 5),
    _TelephonyServicesCallForwardBusyEnable_Type()
)
telephonyServicesCallForwardBusyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardBusyEnable.setStatus("deprecated")


class _TelephonyServicesCallForwardBusyForwardingAddress_Type(OctetString):
    """Custom type telephonyServicesCallForwardBusyForwardingAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TelephonyServicesCallForwardBusyForwardingAddress_Type.__name__ = "OctetString"
_TelephonyServicesCallForwardBusyForwardingAddress_Object = MibTableColumn
telephonyServicesCallForwardBusyForwardingAddress = _TelephonyServicesCallForwardBusyForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 10, 15, 1, 10),
    _TelephonyServicesCallForwardBusyForwardingAddress_Type()
)
telephonyServicesCallForwardBusyForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardBusyForwardingAddress.setStatus("deprecated")
_TelephonyServicesIfCallForwardBusyActivationTable_Object = MibTable
telephonyServicesIfCallForwardBusyActivationTable = _TelephonyServicesIfCallForwardBusyActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 10, 20)
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardBusyActivationTable.setStatus("deprecated")
_TelephonyServicesIfCallForwardBusyActivationEntry_Object = MibTableRow
telephonyServicesIfCallForwardBusyActivationEntry = _TelephonyServicesIfCallForwardBusyActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 10, 20, 1)
)
telephonyServicesIfCallForwardBusyActivationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardBusyActivationEntry.setStatus("deprecated")


class _TelephonyServicesCallForwardBusyActivation_Type(Integer32):
    """Custom type telephonyServicesCallForwardBusyActivation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TelephonyServicesCallForwardBusyActivation_Type.__name__ = "Integer32"
_TelephonyServicesCallForwardBusyActivation_Object = MibTableColumn
telephonyServicesCallForwardBusyActivation = _TelephonyServicesCallForwardBusyActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 10, 20, 1, 5),
    _TelephonyServicesCallForwardBusyActivation_Type()
)
telephonyServicesCallForwardBusyActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardBusyActivation.setStatus("deprecated")
_TelephonyServicesCallForwardOnNoAnswer_ObjectIdentity = ObjectIdentity
telephonyServicesCallForwardOnNoAnswer = _TelephonyServicesCallForwardOnNoAnswer_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15)
)


class _TelephonyServicesCallForwardOnNoAnswerEnableDigitMap_Type(OctetString):
    """Custom type telephonyServicesCallForwardOnNoAnswerEnableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TelephonyServicesCallForwardOnNoAnswerEnableDigitMap_Type.__name__ = "OctetString"
_TelephonyServicesCallForwardOnNoAnswerEnableDigitMap_Object = MibScalar
telephonyServicesCallForwardOnNoAnswerEnableDigitMap = _TelephonyServicesCallForwardOnNoAnswerEnableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15, 5),
    _TelephonyServicesCallForwardOnNoAnswerEnableDigitMap_Type()
)
telephonyServicesCallForwardOnNoAnswerEnableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardOnNoAnswerEnableDigitMap.setStatus("deprecated")


class _TelephonyServicesCallForwardOnNoAnswerDisableDigitMap_Type(OctetString):
    """Custom type telephonyServicesCallForwardOnNoAnswerDisableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TelephonyServicesCallForwardOnNoAnswerDisableDigitMap_Type.__name__ = "OctetString"
_TelephonyServicesCallForwardOnNoAnswerDisableDigitMap_Object = MibScalar
telephonyServicesCallForwardOnNoAnswerDisableDigitMap = _TelephonyServicesCallForwardOnNoAnswerDisableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15, 10),
    _TelephonyServicesCallForwardOnNoAnswerDisableDigitMap_Type()
)
telephonyServicesCallForwardOnNoAnswerDisableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardOnNoAnswerDisableDigitMap.setStatus("deprecated")
_TelephonyServicesIfCallForwardOnNoAnswerTable_Object = MibTable
telephonyServicesIfCallForwardOnNoAnswerTable = _TelephonyServicesIfCallForwardOnNoAnswerTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15, 15)
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardOnNoAnswerTable.setStatus("deprecated")
_TelephonyServicesIfCallForwardOnNoAnswerEntry_Object = MibTableRow
telephonyServicesIfCallForwardOnNoAnswerEntry = _TelephonyServicesIfCallForwardOnNoAnswerEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15, 15, 1)
)
telephonyServicesIfCallForwardOnNoAnswerEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardOnNoAnswerEntry.setStatus("deprecated")


class _TelephonyServicesCallForwardOnNoAnswerEnable_Type(Integer32):
    """Custom type telephonyServicesCallForwardOnNoAnswerEnable based on Integer32"""
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


_TelephonyServicesCallForwardOnNoAnswerEnable_Type.__name__ = "Integer32"
_TelephonyServicesCallForwardOnNoAnswerEnable_Object = MibTableColumn
telephonyServicesCallForwardOnNoAnswerEnable = _TelephonyServicesCallForwardOnNoAnswerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15, 15, 1, 5),
    _TelephonyServicesCallForwardOnNoAnswerEnable_Type()
)
telephonyServicesCallForwardOnNoAnswerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardOnNoAnswerEnable.setStatus("deprecated")


class _TelephonyServicesCallForwardOnNoAnswerForwardingAddress_Type(OctetString):
    """Custom type telephonyServicesCallForwardOnNoAnswerForwardingAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TelephonyServicesCallForwardOnNoAnswerForwardingAddress_Type.__name__ = "OctetString"
_TelephonyServicesCallForwardOnNoAnswerForwardingAddress_Object = MibTableColumn
telephonyServicesCallForwardOnNoAnswerForwardingAddress = _TelephonyServicesCallForwardOnNoAnswerForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15, 15, 1, 10),
    _TelephonyServicesCallForwardOnNoAnswerForwardingAddress_Type()
)
telephonyServicesCallForwardOnNoAnswerForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardOnNoAnswerForwardingAddress.setStatus("deprecated")


class _TelephonyServicesCallForwardOnNoAnswerTimeout_Type(Unsigned32):
    """Custom type telephonyServicesCallForwardOnNoAnswerTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 120000),
    )


_TelephonyServicesCallForwardOnNoAnswerTimeout_Type.__name__ = "Unsigned32"
_TelephonyServicesCallForwardOnNoAnswerTimeout_Object = MibTableColumn
telephonyServicesCallForwardOnNoAnswerTimeout = _TelephonyServicesCallForwardOnNoAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15, 15, 1, 15),
    _TelephonyServicesCallForwardOnNoAnswerTimeout_Type()
)
telephonyServicesCallForwardOnNoAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardOnNoAnswerTimeout.setStatus("deprecated")
_TelephonyServicesIfCallForwardOnNoAnswerActivationTable_Object = MibTable
telephonyServicesIfCallForwardOnNoAnswerActivationTable = _TelephonyServicesIfCallForwardOnNoAnswerActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15, 20)
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardOnNoAnswerActivationTable.setStatus("deprecated")
_TelephonyServicesIfCallForwardOnNoAnswerActivationEntry_Object = MibTableRow
telephonyServicesIfCallForwardOnNoAnswerActivationEntry = _TelephonyServicesIfCallForwardOnNoAnswerActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15, 20, 1)
)
telephonyServicesIfCallForwardOnNoAnswerActivationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallForwardOnNoAnswerActivationEntry.setStatus("deprecated")


class _TelephonyServicesCallForwardOnNoAnswerActivation_Type(Integer32):
    """Custom type telephonyServicesCallForwardOnNoAnswerActivation based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 0),
          ("active", 1))
    )


_TelephonyServicesCallForwardOnNoAnswerActivation_Type.__name__ = "Integer32"
_TelephonyServicesCallForwardOnNoAnswerActivation_Object = MibTableColumn
telephonyServicesCallForwardOnNoAnswerActivation = _TelephonyServicesCallForwardOnNoAnswerActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 20, 15, 20, 1, 5),
    _TelephonyServicesCallForwardOnNoAnswerActivation_Type()
)
telephonyServicesCallForwardOnNoAnswerActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallForwardOnNoAnswerActivation.setStatus("deprecated")
_TelephonyServicesCallWaitingCustomization_ObjectIdentity = ObjectIdentity
telephonyServicesCallWaitingCustomization = _TelephonyServicesCallWaitingCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 30)
)
_TelephonyServicesCallWaitingCancel_ObjectIdentity = ObjectIdentity
telephonyServicesCallWaitingCancel = _TelephonyServicesCallWaitingCancel_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 30, 5)
)


class _TelephonyServicesCallWaitingCancelDigitMap_Type(OctetString):
    """Custom type telephonyServicesCallWaitingCancelDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TelephonyServicesCallWaitingCancelDigitMap_Type.__name__ = "OctetString"
_TelephonyServicesCallWaitingCancelDigitMap_Object = MibScalar
telephonyServicesCallWaitingCancelDigitMap = _TelephonyServicesCallWaitingCancelDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 30, 5, 5),
    _TelephonyServicesCallWaitingCancelDigitMap_Type()
)
telephonyServicesCallWaitingCancelDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallWaitingCancelDigitMap.setStatus("deprecated")
_TelephonyServicesIfCallWaitingCancelTable_Object = MibTable
telephonyServicesIfCallWaitingCancelTable = _TelephonyServicesIfCallWaitingCancelTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 30, 5, 10)
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallWaitingCancelTable.setStatus("deprecated")
_TelephonyServicesIfCallWaitingCancelEntry_Object = MibTableRow
telephonyServicesIfCallWaitingCancelEntry = _TelephonyServicesIfCallWaitingCancelEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 30, 5, 10, 1)
)
telephonyServicesIfCallWaitingCancelEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    telephonyServicesIfCallWaitingCancelEntry.setStatus("deprecated")


class _TelephonyServicesCallWaitingCancelEnable_Type(Integer32):
    """Custom type telephonyServicesCallWaitingCancelEnable based on Integer32"""
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


_TelephonyServicesCallWaitingCancelEnable_Type.__name__ = "Integer32"
_TelephonyServicesCallWaitingCancelEnable_Object = MibTableColumn
telephonyServicesCallWaitingCancelEnable = _TelephonyServicesCallWaitingCancelEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 30, 5, 10, 1, 5),
    _TelephonyServicesCallWaitingCancelEnable_Type()
)
telephonyServicesCallWaitingCancelEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesCallWaitingCancelEnable.setStatus("deprecated")
_TelephonyServicesUrgentGatewayCustomization_ObjectIdentity = ObjectIdentity
telephonyServicesUrgentGatewayCustomization = _TelephonyServicesUrgentGatewayCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 35)
)


class _TelephonyServicesUrgentGatewayEnable_Type(Integer32):
    """Custom type telephonyServicesUrgentGatewayEnable based on Integer32"""
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


_TelephonyServicesUrgentGatewayEnable_Type.__name__ = "Integer32"
_TelephonyServicesUrgentGatewayEnable_Object = MibScalar
telephonyServicesUrgentGatewayEnable = _TelephonyServicesUrgentGatewayEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 35, 5),
    _TelephonyServicesUrgentGatewayEnable_Type()
)
telephonyServicesUrgentGatewayEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesUrgentGatewayEnable.setStatus("deprecated")


class _TelephonyServicesUrgentGatewayDigitMap_Type(OctetString):
    """Custom type telephonyServicesUrgentGatewayDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_TelephonyServicesUrgentGatewayDigitMap_Type.__name__ = "OctetString"
_TelephonyServicesUrgentGatewayDigitMap_Object = MibScalar
telephonyServicesUrgentGatewayDigitMap = _TelephonyServicesUrgentGatewayDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 35, 10),
    _TelephonyServicesUrgentGatewayDigitMap_Type()
)
telephonyServicesUrgentGatewayDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesUrgentGatewayDigitMap.setStatus("deprecated")


class _TelephonyServicesUrgentGatewayTargetAddress_Type(OctetString):
    """Custom type telephonyServicesUrgentGatewayTargetAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_TelephonyServicesUrgentGatewayTargetAddress_Type.__name__ = "OctetString"
_TelephonyServicesUrgentGatewayTargetAddress_Object = MibScalar
telephonyServicesUrgentGatewayTargetAddress = _TelephonyServicesUrgentGatewayTargetAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 35, 15),
    _TelephonyServicesUrgentGatewayTargetAddress_Type()
)
telephonyServicesUrgentGatewayTargetAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesUrgentGatewayTargetAddress.setStatus("deprecated")
_TelephonyServicesIpAddressCallCustomization_ObjectIdentity = ObjectIdentity
telephonyServicesIpAddressCallCustomization = _TelephonyServicesIpAddressCallCustomization_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 99)
)


class _TelephonyServicesIpAddressCallEnable_Type(Integer32):
    """Custom type telephonyServicesIpAddressCallEnable based on Integer32"""
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


_TelephonyServicesIpAddressCallEnable_Type.__name__ = "Integer32"
_TelephonyServicesIpAddressCallEnable_Object = MibScalar
telephonyServicesIpAddressCallEnable = _TelephonyServicesIpAddressCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 1, 20, 99, 5),
    _TelephonyServicesIpAddressCallEnable_Type()
)
telephonyServicesIpAddressCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    telephonyServicesIpAddressCallEnable.setStatus("deprecated")
_TelephonyServicesConformance_ObjectIdentity = ObjectIdentity
telephonyServicesConformance = _TelephonyServicesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2)
)
_TelephonyServicesCompliances_ObjectIdentity = ObjectIdentity
telephonyServicesCompliances = _TelephonyServicesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 1)
)
_TelephonyServicesGroups_ObjectIdentity = ObjectIdentity
telephonyServicesGroups = _TelephonyServicesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5)
)

# Managed Objects groups

telephonyServicesStatusVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 3)
)
telephonyServicesStatusVer1.setObjects(
      *(("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesHoldStatus"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallWaitingStatus"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesSecondCallStatus"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesBlindTransferStatus"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesAttendedTransferStatus"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesConferenceStatus"))
)
if mibBuilder.loadTexts:
    telephonyServicesStatusVer1.setStatus("current")

telephonyServicesActivationVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 5)
)
telephonyServicesActivationVer1.setObjects(
      *(("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesHoldEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallWaitingEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesSecondCallEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesBlindTransferEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesAttendedTransferEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesConferenceEnable"))
)
if mibBuilder.loadTexts:
    telephonyServicesActivationVer1.setStatus("current")

telephonyServicesAutoSpeedDialVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 10)
)
telephonyServicesAutoSpeedDialVer1.setObjects(
      *(("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesAutoSpeedDialEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesAutoSpeedDialTargetAddress"))
)
if mibBuilder.loadTexts:
    telephonyServicesAutoSpeedDialVer1.setStatus("current")

telephonyServicesCallForwardUnconditionnalActivationVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 12)
)
telephonyServicesCallForwardUnconditionnalActivationVer1.setObjects(
    ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardUnconditionnalActivation")
)
if mibBuilder.loadTexts:
    telephonyServicesCallForwardUnconditionnalActivationVer1.setStatus("current")

telephonyServicesCallForwardUnconditionnalVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 15)
)
telephonyServicesCallForwardUnconditionnalVer1.setObjects(
      *(("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardUnconditionnalEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardUnconditionnalForwardingAddress"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardUnconditionnalEnableDigitMap"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardUnconditionnalDisableDigitMap"))
)
if mibBuilder.loadTexts:
    telephonyServicesCallForwardUnconditionnalVer1.setStatus("current")

telephonyServicesCallForwardBusyActivationVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 17)
)
telephonyServicesCallForwardBusyActivationVer1.setObjects(
    ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardBusyActivation")
)
if mibBuilder.loadTexts:
    telephonyServicesCallForwardBusyActivationVer1.setStatus("current")

telephonyServicesCallForwardBusyVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 20)
)
telephonyServicesCallForwardBusyVer1.setObjects(
      *(("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardBusyEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardBusyForwardingAddress"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardBusyEnableDigitMap"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardBusyDisableDigitMap"))
)
if mibBuilder.loadTexts:
    telephonyServicesCallForwardBusyVer1.setStatus("current")

telephonyServicesCallForwardOnNoAnswerActivationVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 22)
)
telephonyServicesCallForwardOnNoAnswerActivationVer1.setObjects(
    ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardOnNoAnswerActivation")
)
if mibBuilder.loadTexts:
    telephonyServicesCallForwardOnNoAnswerActivationVer1.setStatus("current")

telephonyServicesCallForwardOnNoAnswerVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 25)
)
telephonyServicesCallForwardOnNoAnswerVer1.setObjects(
      *(("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardOnNoAnswerEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardOnNoAnswerForwardingAddress"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardOnNoAnswerEnableDigitMap"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardOnNoAnswerDisableDigitMap"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardOnNoAnswerTimeout"))
)
if mibBuilder.loadTexts:
    telephonyServicesCallForwardOnNoAnswerVer1.setStatus("current")

telephonyServicesCallWaitingCancelVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 30)
)
telephonyServicesCallWaitingCancelVer1.setObjects(
      *(("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallWaitingCancelEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallWaitingCancelDigitMap"))
)
if mibBuilder.loadTexts:
    telephonyServicesCallWaitingCancelVer1.setStatus("current")

telephonyServicesUrgentGatewayVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 35)
)
telephonyServicesUrgentGatewayVer1.setObjects(
      *(("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesUrgentGatewayEnable"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesUrgentGatewayDigitMap"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesUrgentGatewayTargetAddress"))
)
if mibBuilder.loadTexts:
    telephonyServicesUrgentGatewayVer1.setStatus("current")

telephonyServicesIpAddressCallVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 5, 99)
)
telephonyServicesIpAddressCallVer1.setObjects(
    ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesIpAddressCallEnable")
)
if mibBuilder.loadTexts:
    telephonyServicesIpAddressCallVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

telephonyServicesComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 60, 2, 1, 1)
)
telephonyServicesComplVer1.setObjects(
      *(("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesStatusVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesActivationVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesAutoSpeedDialVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardUnconditionnalActivationVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardUnconditionnalVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardBusyActivationVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardBusyVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardOnNoAnswerActivationVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallForwardOnNoAnswerVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesCallWaitingCancelVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesUrgentGatewayVer1"),
        ("MX-TELEPHONY-SERVICES-MIB", "telephonyServicesIpAddressCallVer1"))
)
if mibBuilder.loadTexts:
    telephonyServicesComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-TELEPHONY-SERVICES-MIB",
    **{"telephonyServicesMIB": telephonyServicesMIB,
       "telephonyServicesMIBObjects": telephonyServicesMIBObjects,
       "telephonyServicesIfActivationTable": telephonyServicesIfActivationTable,
       "telephonyServicesIfActivationEntry": telephonyServicesIfActivationEntry,
       "telephonyServicesHoldEnable": telephonyServicesHoldEnable,
       "telephonyServicesCallWaitingEnable": telephonyServicesCallWaitingEnable,
       "telephonyServicesSecondCallEnable": telephonyServicesSecondCallEnable,
       "telephonyServicesBlindTransferEnable": telephonyServicesBlindTransferEnable,
       "telephonyServicesAttendedTransferEnable": telephonyServicesAttendedTransferEnable,
       "telephonyServicesConferenceEnable": telephonyServicesConferenceEnable,
       "telephonyServicesIfStatusTable": telephonyServicesIfStatusTable,
       "telephonyServicesIfStatusEntry": telephonyServicesIfStatusEntry,
       "telephonyServicesHoldStatus": telephonyServicesHoldStatus,
       "telephonyServicesCallWaitingStatus": telephonyServicesCallWaitingStatus,
       "telephonyServicesSecondCallStatus": telephonyServicesSecondCallStatus,
       "telephonyServicesBlindTransferStatus": telephonyServicesBlindTransferStatus,
       "telephonyServicesAttendedTransferStatus": telephonyServicesAttendedTransferStatus,
       "telephonyServicesConferenceStatus": telephonyServicesConferenceStatus,
       "telephonyServicesCustomization": telephonyServicesCustomization,
       "telephonyServicesAutoSpeedDial": telephonyServicesAutoSpeedDial,
       "telephonyServicesIfAutoSpeedDialTable": telephonyServicesIfAutoSpeedDialTable,
       "telephonyServicesIfAutoSpeedDialEntry": telephonyServicesIfAutoSpeedDialEntry,
       "telephonyServicesAutoSpeedDialEnable": telephonyServicesAutoSpeedDialEnable,
       "telephonyServicesAutoSpeedDialTargetAddress": telephonyServicesAutoSpeedDialTargetAddress,
       "telephonyServicesCallForwardCustomization": telephonyServicesCallForwardCustomization,
       "telephonyServicesCallForwardUnconditionnal": telephonyServicesCallForwardUnconditionnal,
       "telephonyServicesCallForwardUnconditionnalEnableDigitMap": telephonyServicesCallForwardUnconditionnalEnableDigitMap,
       "telephonyServicesCallForwardUnconditionnalDisableDigitMap": telephonyServicesCallForwardUnconditionnalDisableDigitMap,
       "telephonyServicesIfCallForwardUnconditionnalTable": telephonyServicesIfCallForwardUnconditionnalTable,
       "telephonyServicesIfCallForwardUnconditionnalEntry": telephonyServicesIfCallForwardUnconditionnalEntry,
       "telephonyServicesCallForwardUnconditionnalEnable": telephonyServicesCallForwardUnconditionnalEnable,
       "telephonyServicesCallForwardUnconditionnalForwardingAddress": telephonyServicesCallForwardUnconditionnalForwardingAddress,
       "telephonyServicesIfCallForwardUnconditionnalActivationTable": telephonyServicesIfCallForwardUnconditionnalActivationTable,
       "telephonyServicesIfCallForwardUnconditionnalActivationEntry": telephonyServicesIfCallForwardUnconditionnalActivationEntry,
       "telephonyServicesCallForwardUnconditionnalActivation": telephonyServicesCallForwardUnconditionnalActivation,
       "telephonyServicesCallForwardBusy": telephonyServicesCallForwardBusy,
       "telephonyServicesCallForwardBusyEnableDigitMap": telephonyServicesCallForwardBusyEnableDigitMap,
       "telephonyServicesCallForwardBusyDisableDigitMap": telephonyServicesCallForwardBusyDisableDigitMap,
       "telephonyServicesIfCallForwardBusyTable": telephonyServicesIfCallForwardBusyTable,
       "telephonyServicesIfCallForwardBusyEntry": telephonyServicesIfCallForwardBusyEntry,
       "telephonyServicesCallForwardBusyEnable": telephonyServicesCallForwardBusyEnable,
       "telephonyServicesCallForwardBusyForwardingAddress": telephonyServicesCallForwardBusyForwardingAddress,
       "telephonyServicesIfCallForwardBusyActivationTable": telephonyServicesIfCallForwardBusyActivationTable,
       "telephonyServicesIfCallForwardBusyActivationEntry": telephonyServicesIfCallForwardBusyActivationEntry,
       "telephonyServicesCallForwardBusyActivation": telephonyServicesCallForwardBusyActivation,
       "telephonyServicesCallForwardOnNoAnswer": telephonyServicesCallForwardOnNoAnswer,
       "telephonyServicesCallForwardOnNoAnswerEnableDigitMap": telephonyServicesCallForwardOnNoAnswerEnableDigitMap,
       "telephonyServicesCallForwardOnNoAnswerDisableDigitMap": telephonyServicesCallForwardOnNoAnswerDisableDigitMap,
       "telephonyServicesIfCallForwardOnNoAnswerTable": telephonyServicesIfCallForwardOnNoAnswerTable,
       "telephonyServicesIfCallForwardOnNoAnswerEntry": telephonyServicesIfCallForwardOnNoAnswerEntry,
       "telephonyServicesCallForwardOnNoAnswerEnable": telephonyServicesCallForwardOnNoAnswerEnable,
       "telephonyServicesCallForwardOnNoAnswerForwardingAddress": telephonyServicesCallForwardOnNoAnswerForwardingAddress,
       "telephonyServicesCallForwardOnNoAnswerTimeout": telephonyServicesCallForwardOnNoAnswerTimeout,
       "telephonyServicesIfCallForwardOnNoAnswerActivationTable": telephonyServicesIfCallForwardOnNoAnswerActivationTable,
       "telephonyServicesIfCallForwardOnNoAnswerActivationEntry": telephonyServicesIfCallForwardOnNoAnswerActivationEntry,
       "telephonyServicesCallForwardOnNoAnswerActivation": telephonyServicesCallForwardOnNoAnswerActivation,
       "telephonyServicesCallWaitingCustomization": telephonyServicesCallWaitingCustomization,
       "telephonyServicesCallWaitingCancel": telephonyServicesCallWaitingCancel,
       "telephonyServicesCallWaitingCancelDigitMap": telephonyServicesCallWaitingCancelDigitMap,
       "telephonyServicesIfCallWaitingCancelTable": telephonyServicesIfCallWaitingCancelTable,
       "telephonyServicesIfCallWaitingCancelEntry": telephonyServicesIfCallWaitingCancelEntry,
       "telephonyServicesCallWaitingCancelEnable": telephonyServicesCallWaitingCancelEnable,
       "telephonyServicesUrgentGatewayCustomization": telephonyServicesUrgentGatewayCustomization,
       "telephonyServicesUrgentGatewayEnable": telephonyServicesUrgentGatewayEnable,
       "telephonyServicesUrgentGatewayDigitMap": telephonyServicesUrgentGatewayDigitMap,
       "telephonyServicesUrgentGatewayTargetAddress": telephonyServicesUrgentGatewayTargetAddress,
       "telephonyServicesIpAddressCallCustomization": telephonyServicesIpAddressCallCustomization,
       "telephonyServicesIpAddressCallEnable": telephonyServicesIpAddressCallEnable,
       "telephonyServicesConformance": telephonyServicesConformance,
       "telephonyServicesCompliances": telephonyServicesCompliances,
       "telephonyServicesComplVer1": telephonyServicesComplVer1,
       "telephonyServicesGroups": telephonyServicesGroups,
       "telephonyServicesStatusVer1": telephonyServicesStatusVer1,
       "telephonyServicesActivationVer1": telephonyServicesActivationVer1,
       "telephonyServicesAutoSpeedDialVer1": telephonyServicesAutoSpeedDialVer1,
       "telephonyServicesCallForwardUnconditionnalActivationVer1": telephonyServicesCallForwardUnconditionnalActivationVer1,
       "telephonyServicesCallForwardUnconditionnalVer1": telephonyServicesCallForwardUnconditionnalVer1,
       "telephonyServicesCallForwardBusyActivationVer1": telephonyServicesCallForwardBusyActivationVer1,
       "telephonyServicesCallForwardBusyVer1": telephonyServicesCallForwardBusyVer1,
       "telephonyServicesCallForwardOnNoAnswerActivationVer1": telephonyServicesCallForwardOnNoAnswerActivationVer1,
       "telephonyServicesCallForwardOnNoAnswerVer1": telephonyServicesCallForwardOnNoAnswerVer1,
       "telephonyServicesCallWaitingCancelVer1": telephonyServicesCallWaitingCancelVer1,
       "telephonyServicesUrgentGatewayVer1": telephonyServicesUrgentGatewayVer1,
       "telephonyServicesIpAddressCallVer1": telephonyServicesIpAddressCallVer1}
)
