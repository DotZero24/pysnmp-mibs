# SNMP MIB module (MX-SUBSCRIBER-SERVICES-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/media5/MX-SUBSCRIBER-SERVICES-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:46 2025
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

(MxActivationState,
 MxEnableState) = mibBuilder.importSymbols(
    "MX-TC",
    "MxActivationState",
    "MxEnableState")

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

subscriberServicesMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62)
)
if mibBuilder.loadTexts:
    subscriberServicesMIB.setRevisions(
        ("2010-07-30 00:00",
         "2008-06-12 00:00",
         "2008-06-10 00:00",
         "2005-07-14 00:00",
         "2003-05-28 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SubscriberServicesMIBObjects_ObjectIdentity = ObjectIdentity
subscriberServicesMIBObjects = _SubscriberServicesMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1)
)
_SubscriberServicesIfEnablingTable_Object = MibTable
subscriberServicesIfEnablingTable = _SubscriberServicesIfEnablingTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10)
)
if mibBuilder.loadTexts:
    subscriberServicesIfEnablingTable.setStatus("current")
_SubscriberServicesIfEnablingEntry_Object = MibTableRow
subscriberServicesIfEnablingEntry = _SubscriberServicesIfEnablingEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10, 1)
)
subscriberServicesIfEnablingEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    subscriberServicesIfEnablingEntry.setStatus("current")


class _SubscriberServicesHoldEnable_Type(MxEnableState):
    """Custom type subscriberServicesHoldEnable based on MxEnableState"""
    defaultValue = 1


_SubscriberServicesHoldEnable_Type.__name__ = "MxEnableState"
_SubscriberServicesHoldEnable_Object = MibTableColumn
subscriberServicesHoldEnable = _SubscriberServicesHoldEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10, 1, 5),
    _SubscriberServicesHoldEnable_Type()
)
subscriberServicesHoldEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesHoldEnable.setStatus("current")


class _SubscriberServicesCallWaitingEnable_Type(MxEnableState):
    """Custom type subscriberServicesCallWaitingEnable based on MxEnableState"""
    defaultValue = 1


_SubscriberServicesCallWaitingEnable_Type.__name__ = "MxEnableState"
_SubscriberServicesCallWaitingEnable_Object = MibTableColumn
subscriberServicesCallWaitingEnable = _SubscriberServicesCallWaitingEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10, 1, 10),
    _SubscriberServicesCallWaitingEnable_Type()
)
subscriberServicesCallWaitingEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallWaitingEnable.setStatus("current")


class _SubscriberServicesSecondCallEnable_Type(MxEnableState):
    """Custom type subscriberServicesSecondCallEnable based on MxEnableState"""
    defaultValue = 1


_SubscriberServicesSecondCallEnable_Type.__name__ = "MxEnableState"
_SubscriberServicesSecondCallEnable_Object = MibTableColumn
subscriberServicesSecondCallEnable = _SubscriberServicesSecondCallEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10, 1, 15),
    _SubscriberServicesSecondCallEnable_Type()
)
subscriberServicesSecondCallEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesSecondCallEnable.setStatus("current")


class _SubscriberServicesBlindTransferEnable_Type(MxEnableState):
    """Custom type subscriberServicesBlindTransferEnable based on MxEnableState"""
    defaultValue = 1


_SubscriberServicesBlindTransferEnable_Type.__name__ = "MxEnableState"
_SubscriberServicesBlindTransferEnable_Object = MibTableColumn
subscriberServicesBlindTransferEnable = _SubscriberServicesBlindTransferEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10, 1, 20),
    _SubscriberServicesBlindTransferEnable_Type()
)
subscriberServicesBlindTransferEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesBlindTransferEnable.setStatus("current")


class _SubscriberServicesAttendedTransferEnable_Type(MxEnableState):
    """Custom type subscriberServicesAttendedTransferEnable based on MxEnableState"""
    defaultValue = 1


_SubscriberServicesAttendedTransferEnable_Type.__name__ = "MxEnableState"
_SubscriberServicesAttendedTransferEnable_Object = MibTableColumn
subscriberServicesAttendedTransferEnable = _SubscriberServicesAttendedTransferEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10, 1, 25),
    _SubscriberServicesAttendedTransferEnable_Type()
)
subscriberServicesAttendedTransferEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesAttendedTransferEnable.setStatus("current")


class _SubscriberServicesConferenceEnable_Type(MxEnableState):
    """Custom type subscriberServicesConferenceEnable based on MxEnableState"""
    defaultValue = 1


_SubscriberServicesConferenceEnable_Type.__name__ = "MxEnableState"
_SubscriberServicesConferenceEnable_Object = MibTableColumn
subscriberServicesConferenceEnable = _SubscriberServicesConferenceEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10, 1, 30),
    _SubscriberServicesConferenceEnable_Type()
)
subscriberServicesConferenceEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesConferenceEnable.setStatus("current")


class _SubscriberServicesCallForwardUnconditionalEnable_Type(MxEnableState):
    """Custom type subscriberServicesCallForwardUnconditionalEnable based on MxEnableState"""
    defaultValue = 0


_SubscriberServicesCallForwardUnconditionalEnable_Type.__name__ = "MxEnableState"
_SubscriberServicesCallForwardUnconditionalEnable_Object = MibTableColumn
subscriberServicesCallForwardUnconditionalEnable = _SubscriberServicesCallForwardUnconditionalEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10, 1, 35),
    _SubscriberServicesCallForwardUnconditionalEnable_Type()
)
subscriberServicesCallForwardUnconditionalEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardUnconditionalEnable.setStatus("current")


class _SubscriberServicesCallForwardOnBusyEnable_Type(MxEnableState):
    """Custom type subscriberServicesCallForwardOnBusyEnable based on MxEnableState"""
    defaultValue = 0


_SubscriberServicesCallForwardOnBusyEnable_Type.__name__ = "MxEnableState"
_SubscriberServicesCallForwardOnBusyEnable_Object = MibTableColumn
subscriberServicesCallForwardOnBusyEnable = _SubscriberServicesCallForwardOnBusyEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10, 1, 40),
    _SubscriberServicesCallForwardOnBusyEnable_Type()
)
subscriberServicesCallForwardOnBusyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnBusyEnable.setStatus("current")


class _SubscriberServicesCallForwardOnNoAnswerEnable_Type(MxEnableState):
    """Custom type subscriberServicesCallForwardOnNoAnswerEnable based on MxEnableState"""
    defaultValue = 0


_SubscriberServicesCallForwardOnNoAnswerEnable_Type.__name__ = "MxEnableState"
_SubscriberServicesCallForwardOnNoAnswerEnable_Object = MibTableColumn
subscriberServicesCallForwardOnNoAnswerEnable = _SubscriberServicesCallForwardOnNoAnswerEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 10, 1, 45),
    _SubscriberServicesCallForwardOnNoAnswerEnable_Type()
)
subscriberServicesCallForwardOnNoAnswerEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnNoAnswerEnable.setStatus("current")
_SubscriberServicesIfStatusTable_Object = MibTable
subscriberServicesIfStatusTable = _SubscriberServicesIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 15)
)
if mibBuilder.loadTexts:
    subscriberServicesIfStatusTable.setStatus("current")
_SubscriberServicesIfStatusEntry_Object = MibTableRow
subscriberServicesIfStatusEntry = _SubscriberServicesIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 15, 1)
)
subscriberServicesIfStatusEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    subscriberServicesIfStatusEntry.setStatus("current")


class _SubscriberServicesHoldStatus_Type(MxActivationState):
    """Custom type subscriberServicesHoldStatus based on MxActivationState"""
    defaultValue = 1


_SubscriberServicesHoldStatus_Type.__name__ = "MxActivationState"
_SubscriberServicesHoldStatus_Object = MibTableColumn
subscriberServicesHoldStatus = _SubscriberServicesHoldStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 15, 1, 5),
    _SubscriberServicesHoldStatus_Type()
)
subscriberServicesHoldStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServicesHoldStatus.setStatus("current")


class _SubscriberServicesCallWaitingStatus_Type(MxActivationState):
    """Custom type subscriberServicesCallWaitingStatus based on MxActivationState"""
    defaultValue = 1


_SubscriberServicesCallWaitingStatus_Type.__name__ = "MxActivationState"
_SubscriberServicesCallWaitingStatus_Object = MibTableColumn
subscriberServicesCallWaitingStatus = _SubscriberServicesCallWaitingStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 15, 1, 10),
    _SubscriberServicesCallWaitingStatus_Type()
)
subscriberServicesCallWaitingStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServicesCallWaitingStatus.setStatus("current")


class _SubscriberServicesSecondCallStatus_Type(MxActivationState):
    """Custom type subscriberServicesSecondCallStatus based on MxActivationState"""
    defaultValue = 1


_SubscriberServicesSecondCallStatus_Type.__name__ = "MxActivationState"
_SubscriberServicesSecondCallStatus_Object = MibTableColumn
subscriberServicesSecondCallStatus = _SubscriberServicesSecondCallStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 15, 1, 15),
    _SubscriberServicesSecondCallStatus_Type()
)
subscriberServicesSecondCallStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServicesSecondCallStatus.setStatus("current")


class _SubscriberServicesBlindTransferStatus_Type(MxActivationState):
    """Custom type subscriberServicesBlindTransferStatus based on MxActivationState"""
    defaultValue = 1


_SubscriberServicesBlindTransferStatus_Type.__name__ = "MxActivationState"
_SubscriberServicesBlindTransferStatus_Object = MibTableColumn
subscriberServicesBlindTransferStatus = _SubscriberServicesBlindTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 15, 1, 20),
    _SubscriberServicesBlindTransferStatus_Type()
)
subscriberServicesBlindTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServicesBlindTransferStatus.setStatus("current")


class _SubscriberServicesAttendedTransferStatus_Type(MxActivationState):
    """Custom type subscriberServicesAttendedTransferStatus based on MxActivationState"""
    defaultValue = 1


_SubscriberServicesAttendedTransferStatus_Type.__name__ = "MxActivationState"
_SubscriberServicesAttendedTransferStatus_Object = MibTableColumn
subscriberServicesAttendedTransferStatus = _SubscriberServicesAttendedTransferStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 15, 1, 25),
    _SubscriberServicesAttendedTransferStatus_Type()
)
subscriberServicesAttendedTransferStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServicesAttendedTransferStatus.setStatus("current")


class _SubscriberServicesConferenceStatus_Type(MxActivationState):
    """Custom type subscriberServicesConferenceStatus based on MxActivationState"""
    defaultValue = 1


_SubscriberServicesConferenceStatus_Type.__name__ = "MxActivationState"
_SubscriberServicesConferenceStatus_Object = MibTableColumn
subscriberServicesConferenceStatus = _SubscriberServicesConferenceStatus_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 15, 1, 30),
    _SubscriberServicesConferenceStatus_Type()
)
subscriberServicesConferenceStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    subscriberServicesConferenceStatus.setStatus("current")
_SubscriberServicesIfCallForwardActivationTable_Object = MibTable
subscriberServicesIfCallForwardActivationTable = _SubscriberServicesIfCallForwardActivationTable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 21)
)
if mibBuilder.loadTexts:
    subscriberServicesIfCallForwardActivationTable.setStatus("current")
_SubscriberServicesIfCallForwardActivationEntry_Object = MibTableRow
subscriberServicesIfCallForwardActivationEntry = _SubscriberServicesIfCallForwardActivationEntry_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 21, 1)
)
subscriberServicesIfCallForwardActivationEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    subscriberServicesIfCallForwardActivationEntry.setStatus("current")


class _SubscriberServicesCallForwardUnconditionalActivation_Type(MxActivationState):
    """Custom type subscriberServicesCallForwardUnconditionalActivation based on MxActivationState"""
    defaultValue = 0


_SubscriberServicesCallForwardUnconditionalActivation_Type.__name__ = "MxActivationState"
_SubscriberServicesCallForwardUnconditionalActivation_Object = MibTableColumn
subscriberServicesCallForwardUnconditionalActivation = _SubscriberServicesCallForwardUnconditionalActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 21, 1, 5),
    _SubscriberServicesCallForwardUnconditionalActivation_Type()
)
subscriberServicesCallForwardUnconditionalActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardUnconditionalActivation.setStatus("current")


class _SubscriberServicesCallForwardUnconditionalForwardingAddress_Type(OctetString):
    """Custom type subscriberServicesCallForwardUnconditionalForwardingAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SubscriberServicesCallForwardUnconditionalForwardingAddress_Type.__name__ = "OctetString"
_SubscriberServicesCallForwardUnconditionalForwardingAddress_Object = MibTableColumn
subscriberServicesCallForwardUnconditionalForwardingAddress = _SubscriberServicesCallForwardUnconditionalForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 21, 1, 10),
    _SubscriberServicesCallForwardUnconditionalForwardingAddress_Type()
)
subscriberServicesCallForwardUnconditionalForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardUnconditionalForwardingAddress.setStatus("current")


class _SubscriberServicesCallForwardOnBusyActivation_Type(MxActivationState):
    """Custom type subscriberServicesCallForwardOnBusyActivation based on MxActivationState"""
    defaultValue = 0


_SubscriberServicesCallForwardOnBusyActivation_Type.__name__ = "MxActivationState"
_SubscriberServicesCallForwardOnBusyActivation_Object = MibTableColumn
subscriberServicesCallForwardOnBusyActivation = _SubscriberServicesCallForwardOnBusyActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 21, 1, 15),
    _SubscriberServicesCallForwardOnBusyActivation_Type()
)
subscriberServicesCallForwardOnBusyActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnBusyActivation.setStatus("current")


class _SubscriberServicesCallForwardOnBusyForwardingAddress_Type(OctetString):
    """Custom type subscriberServicesCallForwardOnBusyForwardingAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SubscriberServicesCallForwardOnBusyForwardingAddress_Type.__name__ = "OctetString"
_SubscriberServicesCallForwardOnBusyForwardingAddress_Object = MibTableColumn
subscriberServicesCallForwardOnBusyForwardingAddress = _SubscriberServicesCallForwardOnBusyForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 21, 1, 20),
    _SubscriberServicesCallForwardOnBusyForwardingAddress_Type()
)
subscriberServicesCallForwardOnBusyForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnBusyForwardingAddress.setStatus("current")


class _SubscriberServicesCallForwardOnNoAnswerActivation_Type(MxActivationState):
    """Custom type subscriberServicesCallForwardOnNoAnswerActivation based on MxActivationState"""
    defaultValue = 0


_SubscriberServicesCallForwardOnNoAnswerActivation_Type.__name__ = "MxActivationState"
_SubscriberServicesCallForwardOnNoAnswerActivation_Object = MibTableColumn
subscriberServicesCallForwardOnNoAnswerActivation = _SubscriberServicesCallForwardOnNoAnswerActivation_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 21, 1, 25),
    _SubscriberServicesCallForwardOnNoAnswerActivation_Type()
)
subscriberServicesCallForwardOnNoAnswerActivation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnNoAnswerActivation.setStatus("current")


class _SubscriberServicesCallForwardOnNoAnswerForwardingAddress_Type(OctetString):
    """Custom type subscriberServicesCallForwardOnNoAnswerForwardingAddress based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_SubscriberServicesCallForwardOnNoAnswerForwardingAddress_Type.__name__ = "OctetString"
_SubscriberServicesCallForwardOnNoAnswerForwardingAddress_Object = MibTableColumn
subscriberServicesCallForwardOnNoAnswerForwardingAddress = _SubscriberServicesCallForwardOnNoAnswerForwardingAddress_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 21, 1, 30),
    _SubscriberServicesCallForwardOnNoAnswerForwardingAddress_Type()
)
subscriberServicesCallForwardOnNoAnswerForwardingAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnNoAnswerForwardingAddress.setStatus("current")


class _SubscriberServicesCallForwardOnNoAnswerTimeout_Type(Unsigned32):
    """Custom type subscriberServicesCallForwardOnNoAnswerTimeout based on Unsigned32"""
    defaultValue = 5000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 120000),
    )


_SubscriberServicesCallForwardOnNoAnswerTimeout_Type.__name__ = "Unsigned32"
_SubscriberServicesCallForwardOnNoAnswerTimeout_Object = MibTableColumn
subscriberServicesCallForwardOnNoAnswerTimeout = _SubscriberServicesCallForwardOnNoAnswerTimeout_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 21, 1, 35),
    _SubscriberServicesCallForwardOnNoAnswerTimeout_Type()
)
subscriberServicesCallForwardOnNoAnswerTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnNoAnswerTimeout.setStatus("current")
_SubscriberServicesActivationDigitmaps_ObjectIdentity = ObjectIdentity
subscriberServicesActivationDigitmaps = _SubscriberServicesActivationDigitmaps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 25)
)


class _SubscriberServicesCallForwardUnconditionalEnableDigitMap_Type(OctetString):
    """Custom type subscriberServicesCallForwardUnconditionalEnableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SubscriberServicesCallForwardUnconditionalEnableDigitMap_Type.__name__ = "OctetString"
_SubscriberServicesCallForwardUnconditionalEnableDigitMap_Object = MibScalar
subscriberServicesCallForwardUnconditionalEnableDigitMap = _SubscriberServicesCallForwardUnconditionalEnableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 25, 5),
    _SubscriberServicesCallForwardUnconditionalEnableDigitMap_Type()
)
subscriberServicesCallForwardUnconditionalEnableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardUnconditionalEnableDigitMap.setStatus("current")


class _SubscriberServicesCallForwardUnconditionalDisableDigitMap_Type(OctetString):
    """Custom type subscriberServicesCallForwardUnconditionalDisableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SubscriberServicesCallForwardUnconditionalDisableDigitMap_Type.__name__ = "OctetString"
_SubscriberServicesCallForwardUnconditionalDisableDigitMap_Object = MibScalar
subscriberServicesCallForwardUnconditionalDisableDigitMap = _SubscriberServicesCallForwardUnconditionalDisableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 25, 10),
    _SubscriberServicesCallForwardUnconditionalDisableDigitMap_Type()
)
subscriberServicesCallForwardUnconditionalDisableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardUnconditionalDisableDigitMap.setStatus("current")


class _SubscriberServicesCallForwardOnBusyEnableDigitMap_Type(OctetString):
    """Custom type subscriberServicesCallForwardOnBusyEnableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SubscriberServicesCallForwardOnBusyEnableDigitMap_Type.__name__ = "OctetString"
_SubscriberServicesCallForwardOnBusyEnableDigitMap_Object = MibScalar
subscriberServicesCallForwardOnBusyEnableDigitMap = _SubscriberServicesCallForwardOnBusyEnableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 25, 15),
    _SubscriberServicesCallForwardOnBusyEnableDigitMap_Type()
)
subscriberServicesCallForwardOnBusyEnableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnBusyEnableDigitMap.setStatus("current")


class _SubscriberServicesCallForwardOnBusyDisableDigitMap_Type(OctetString):
    """Custom type subscriberServicesCallForwardOnBusyDisableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SubscriberServicesCallForwardOnBusyDisableDigitMap_Type.__name__ = "OctetString"
_SubscriberServicesCallForwardOnBusyDisableDigitMap_Object = MibScalar
subscriberServicesCallForwardOnBusyDisableDigitMap = _SubscriberServicesCallForwardOnBusyDisableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 25, 20),
    _SubscriberServicesCallForwardOnBusyDisableDigitMap_Type()
)
subscriberServicesCallForwardOnBusyDisableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnBusyDisableDigitMap.setStatus("current")


class _SubscriberServicesCallForwardOnNoAnswerEnableDigitMap_Type(OctetString):
    """Custom type subscriberServicesCallForwardOnNoAnswerEnableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SubscriberServicesCallForwardOnNoAnswerEnableDigitMap_Type.__name__ = "OctetString"
_SubscriberServicesCallForwardOnNoAnswerEnableDigitMap_Object = MibScalar
subscriberServicesCallForwardOnNoAnswerEnableDigitMap = _SubscriberServicesCallForwardOnNoAnswerEnableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 25, 25),
    _SubscriberServicesCallForwardOnNoAnswerEnableDigitMap_Type()
)
subscriberServicesCallForwardOnNoAnswerEnableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnNoAnswerEnableDigitMap.setStatus("current")


class _SubscriberServicesCallForwardOnNoAnswerDisableDigitMap_Type(OctetString):
    """Custom type subscriberServicesCallForwardOnNoAnswerDisableDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SubscriberServicesCallForwardOnNoAnswerDisableDigitMap_Type.__name__ = "OctetString"
_SubscriberServicesCallForwardOnNoAnswerDisableDigitMap_Object = MibScalar
subscriberServicesCallForwardOnNoAnswerDisableDigitMap = _SubscriberServicesCallForwardOnNoAnswerDisableDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 25, 30),
    _SubscriberServicesCallForwardOnNoAnswerDisableDigitMap_Type()
)
subscriberServicesCallForwardOnNoAnswerDisableDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallForwardOnNoAnswerDisableDigitMap.setStatus("current")


class _SubscriberServicesCallWaitingCancelDigitMap_Type(OctetString):
    """Custom type subscriberServicesCallWaitingCancelDigitMap based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SubscriberServicesCallWaitingCancelDigitMap_Type.__name__ = "OctetString"
_SubscriberServicesCallWaitingCancelDigitMap_Object = MibScalar
subscriberServicesCallWaitingCancelDigitMap = _SubscriberServicesCallWaitingCancelDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 25, 35),
    _SubscriberServicesCallWaitingCancelDigitMap_Type()
)
subscriberServicesCallWaitingCancelDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallWaitingCancelDigitMap.setStatus("current")


class _SubscriberServicesCallWaitingPermanentDigitMapEnable_Type(OctetString):
    """Custom type subscriberServicesCallWaitingPermanentDigitMapEnable based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SubscriberServicesCallWaitingPermanentDigitMapEnable_Type.__name__ = "OctetString"
_SubscriberServicesCallWaitingPermanentDigitMapEnable_Object = MibScalar
subscriberServicesCallWaitingPermanentDigitMapEnable = _SubscriberServicesCallWaitingPermanentDigitMapEnable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 25, 40),
    _SubscriberServicesCallWaitingPermanentDigitMapEnable_Type()
)
subscriberServicesCallWaitingPermanentDigitMapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallWaitingPermanentDigitMapEnable.setStatus("current")


class _SubscriberServicesCallWaitingPermanentDigitMapDisable_Type(OctetString):
    """Custom type subscriberServicesCallWaitingPermanentDigitMapDisable based on OctetString"""
    defaultValue = OctetString("")

    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 63),
    )


_SubscriberServicesCallWaitingPermanentDigitMapDisable_Type.__name__ = "OctetString"
_SubscriberServicesCallWaitingPermanentDigitMapDisable_Object = MibScalar
subscriberServicesCallWaitingPermanentDigitMapDisable = _SubscriberServicesCallWaitingPermanentDigitMapDisable_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 25, 45),
    _SubscriberServicesCallWaitingPermanentDigitMapDisable_Type()
)
subscriberServicesCallWaitingPermanentDigitMapDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesCallWaitingPermanentDigitMapDisable.setStatus("current")
_SubscriberServicesProcessing_ObjectIdentity = ObjectIdentity
subscriberServicesProcessing = _SubscriberServicesProcessing_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 50)
)


class _SubscriberServicesProcessingTrigger_Type(Integer32):
    """Custom type subscriberServicesProcessingTrigger based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("flashHook", 0),
          ("flashHookAndDigits", 1))
    )


_SubscriberServicesProcessingTrigger_Type.__name__ = "Integer32"
_SubscriberServicesProcessingTrigger_Object = MibScalar
subscriberServicesProcessingTrigger = _SubscriberServicesProcessingTrigger_Object(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 1, 50, 5),
    _SubscriberServicesProcessingTrigger_Type()
)
subscriberServicesProcessingTrigger.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    subscriberServicesProcessingTrigger.setStatus("current")
_SubscriberServicesConformance_ObjectIdentity = ObjectIdentity
subscriberServicesConformance = _SubscriberServicesConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 2)
)
_SubscriberServicesCompliances_ObjectIdentity = ObjectIdentity
subscriberServicesCompliances = _SubscriberServicesCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 2, 1)
)
_SubscriberServicesGroups_ObjectIdentity = ObjectIdentity
subscriberServicesGroups = _SubscriberServicesGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 2, 5)
)

# Managed Objects groups

subscriberServicesEnablingVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 2, 5, 3)
)
subscriberServicesEnablingVer1.setObjects(
      *(("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesHoldEnable"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallWaitingEnable"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesSecondCallEnable"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesBlindTransferEnable"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesAttendedTransferEnable"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesConferenceEnable"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardUnconditionalEnable"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnBusyEnable"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnNoAnswerEnable"))
)
if mibBuilder.loadTexts:
    subscriberServicesEnablingVer1.setStatus("current")

subscriberServicesActivationVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 2, 5, 10)
)
subscriberServicesActivationVer1.setObjects(
      *(("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesHoldStatus"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallWaitingStatus"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesSecondCallStatus"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesBlindTransferStatus"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesAttendedTransferStatus"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesConferenceStatus"))
)
if mibBuilder.loadTexts:
    subscriberServicesActivationVer1.setStatus("current")

subscriberServicesCallForwardActivationVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 2, 5, 12)
)
subscriberServicesCallForwardActivationVer1.setObjects(
      *(("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardUnconditionalActivation"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardUnconditionalForwardingAddress"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnBusyActivation"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnBusyForwardingAddress"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnNoAnswerActivation"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnNoAnswerForwardingAddress"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnNoAnswerTimeout"))
)
if mibBuilder.loadTexts:
    subscriberServicesCallForwardActivationVer1.setStatus("current")

subscriberServicesActivationDigitmapsVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 2, 5, 15)
)
subscriberServicesActivationDigitmapsVer1.setObjects(
      *(("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardUnconditionalEnableDigitMap"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardUnconditionalDisableDigitMap"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnBusyEnableDigitMap"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnBusyDisableDigitMap"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnNoAnswerEnableDigitMap"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardOnNoAnswerDisableDigitMap"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallWaitingCancelDigitMap"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallWaitingPermanentDigitMapEnable"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallWaitingPermanentDigitMapDisable"))
)
if mibBuilder.loadTexts:
    subscriberServicesActivationDigitmapsVer1.setStatus("current")

subscriberServicesProcessingVer1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 2, 5, 18)
)
subscriberServicesProcessingVer1.setObjects(
    ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesProcessingTrigger")
)
if mibBuilder.loadTexts:
    subscriberServicesProcessingVer1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

subscriberServicesComplVer1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 4935, 15, 62, 2, 1, 1)
)
subscriberServicesComplVer1.setObjects(
      *(("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesEnablingVer1"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesActivationVer1"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesCallForwardActivationVer1"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesActivationDigitmapsVer1"),
        ("MX-SUBSCRIBER-SERVICES-MIB", "subscriberServicesProcessingVer1"))
)
if mibBuilder.loadTexts:
    subscriberServicesComplVer1.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "MX-SUBSCRIBER-SERVICES-MIB",
    **{"subscriberServicesMIB": subscriberServicesMIB,
       "subscriberServicesMIBObjects": subscriberServicesMIBObjects,
       "subscriberServicesIfEnablingTable": subscriberServicesIfEnablingTable,
       "subscriberServicesIfEnablingEntry": subscriberServicesIfEnablingEntry,
       "subscriberServicesHoldEnable": subscriberServicesHoldEnable,
       "subscriberServicesCallWaitingEnable": subscriberServicesCallWaitingEnable,
       "subscriberServicesSecondCallEnable": subscriberServicesSecondCallEnable,
       "subscriberServicesBlindTransferEnable": subscriberServicesBlindTransferEnable,
       "subscriberServicesAttendedTransferEnable": subscriberServicesAttendedTransferEnable,
       "subscriberServicesConferenceEnable": subscriberServicesConferenceEnable,
       "subscriberServicesCallForwardUnconditionalEnable": subscriberServicesCallForwardUnconditionalEnable,
       "subscriberServicesCallForwardOnBusyEnable": subscriberServicesCallForwardOnBusyEnable,
       "subscriberServicesCallForwardOnNoAnswerEnable": subscriberServicesCallForwardOnNoAnswerEnable,
       "subscriberServicesIfStatusTable": subscriberServicesIfStatusTable,
       "subscriberServicesIfStatusEntry": subscriberServicesIfStatusEntry,
       "subscriberServicesHoldStatus": subscriberServicesHoldStatus,
       "subscriberServicesCallWaitingStatus": subscriberServicesCallWaitingStatus,
       "subscriberServicesSecondCallStatus": subscriberServicesSecondCallStatus,
       "subscriberServicesBlindTransferStatus": subscriberServicesBlindTransferStatus,
       "subscriberServicesAttendedTransferStatus": subscriberServicesAttendedTransferStatus,
       "subscriberServicesConferenceStatus": subscriberServicesConferenceStatus,
       "subscriberServicesIfCallForwardActivationTable": subscriberServicesIfCallForwardActivationTable,
       "subscriberServicesIfCallForwardActivationEntry": subscriberServicesIfCallForwardActivationEntry,
       "subscriberServicesCallForwardUnconditionalActivation": subscriberServicesCallForwardUnconditionalActivation,
       "subscriberServicesCallForwardUnconditionalForwardingAddress": subscriberServicesCallForwardUnconditionalForwardingAddress,
       "subscriberServicesCallForwardOnBusyActivation": subscriberServicesCallForwardOnBusyActivation,
       "subscriberServicesCallForwardOnBusyForwardingAddress": subscriberServicesCallForwardOnBusyForwardingAddress,
       "subscriberServicesCallForwardOnNoAnswerActivation": subscriberServicesCallForwardOnNoAnswerActivation,
       "subscriberServicesCallForwardOnNoAnswerForwardingAddress": subscriberServicesCallForwardOnNoAnswerForwardingAddress,
       "subscriberServicesCallForwardOnNoAnswerTimeout": subscriberServicesCallForwardOnNoAnswerTimeout,
       "subscriberServicesActivationDigitmaps": subscriberServicesActivationDigitmaps,
       "subscriberServicesCallForwardUnconditionalEnableDigitMap": subscriberServicesCallForwardUnconditionalEnableDigitMap,
       "subscriberServicesCallForwardUnconditionalDisableDigitMap": subscriberServicesCallForwardUnconditionalDisableDigitMap,
       "subscriberServicesCallForwardOnBusyEnableDigitMap": subscriberServicesCallForwardOnBusyEnableDigitMap,
       "subscriberServicesCallForwardOnBusyDisableDigitMap": subscriberServicesCallForwardOnBusyDisableDigitMap,
       "subscriberServicesCallForwardOnNoAnswerEnableDigitMap": subscriberServicesCallForwardOnNoAnswerEnableDigitMap,
       "subscriberServicesCallForwardOnNoAnswerDisableDigitMap": subscriberServicesCallForwardOnNoAnswerDisableDigitMap,
       "subscriberServicesCallWaitingCancelDigitMap": subscriberServicesCallWaitingCancelDigitMap,
       "subscriberServicesCallWaitingPermanentDigitMapEnable": subscriberServicesCallWaitingPermanentDigitMapEnable,
       "subscriberServicesCallWaitingPermanentDigitMapDisable": subscriberServicesCallWaitingPermanentDigitMapDisable,
       "subscriberServicesProcessing": subscriberServicesProcessing,
       "subscriberServicesProcessingTrigger": subscriberServicesProcessingTrigger,
       "subscriberServicesConformance": subscriberServicesConformance,
       "subscriberServicesCompliances": subscriberServicesCompliances,
       "subscriberServicesComplVer1": subscriberServicesComplVer1,
       "subscriberServicesGroups": subscriberServicesGroups,
       "subscriberServicesEnablingVer1": subscriberServicesEnablingVer1,
       "subscriberServicesActivationVer1": subscriberServicesActivationVer1,
       "subscriberServicesCallForwardActivationVer1": subscriberServicesCallForwardActivationVer1,
       "subscriberServicesActivationDigitmapsVer1": subscriberServicesActivationDigitmapsVer1,
       "subscriberServicesProcessingVer1": subscriberServicesProcessingVer1}
)
