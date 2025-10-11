# SNMP MIB module (ADTRAN-TACONTROLER-PRODUCT2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-TACONTROLER-PRODUCT2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:44 2025
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

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adTaControllerMgmt,) = mibBuilder.importSymbols(
    "ADTRAN-TACONTROLER-PRODUCT-MIB",
    "adTaControllerMgmt")

(ModuleCompliance,
 NotificationGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup")

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adTaCtrlProduct2 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1)
)
if mibBuilder.loadTexts:
    adTaCtrlProduct2.setRevisions(
        ("2007-05-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdTaSysCtrlNotifications_ObjectIdentity = ObjectIdentity
adTaSysCtrlNotifications = _AdTaSysCtrlNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 0)
)
_AdTaSysCtrlScalars_ObjectIdentity = ObjectIdentity
adTaSysCtrlScalars = _AdTaSysCtrlScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 10)
)


class _AdTaCtrlChassisSlotNumber_Type(Integer32):
    """Custom type adTaCtrlChassisSlotNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdTaCtrlChassisSlotNumber_Type.__name__ = "Integer32"
_AdTaCtrlChassisSlotNumber_Object = MibScalar
adTaCtrlChassisSlotNumber = _AdTaCtrlChassisSlotNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 10, 10),
    _AdTaCtrlChassisSlotNumber_Type()
)
adTaCtrlChassisSlotNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaCtrlChassisSlotNumber.setStatus("current")


class _AdTaCtrlChassisShelfNumber_Type(Integer32):
    """Custom type adTaCtrlChassisShelfNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_AdTaCtrlChassisShelfNumber_Type.__name__ = "Integer32"
_AdTaCtrlChassisShelfNumber_Object = MibScalar
adTaCtrlChassisShelfNumber = _AdTaCtrlChassisShelfNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 10, 11),
    _AdTaCtrlChassisShelfNumber_Type()
)
adTaCtrlChassisShelfNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaCtrlChassisShelfNumber.setStatus("current")
_AdTaCtrlChassisTimeStamp_Type = DateAndTime
_AdTaCtrlChassisTimeStamp_Object = MibScalar
adTaCtrlChassisTimeStamp = _AdTaCtrlChassisTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 10, 12),
    _AdTaCtrlChassisTimeStamp_Type()
)
adTaCtrlChassisTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaCtrlChassisTimeStamp.setStatus("current")
_AdTaCtrlEventDetails_Type = OctetString
_AdTaCtrlEventDetails_Object = MibScalar
adTaCtrlEventDetails = _AdTaCtrlEventDetails_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 10, 15),
    _AdTaCtrlEventDetails_Type()
)
adTaCtrlEventDetails.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaCtrlEventDetails.setStatus("current")
_AdTaCtrlProvisionSnmpOID_Type = ObjectIdentifier
_AdTaCtrlProvisionSnmpOID_Object = MibScalar
adTaCtrlProvisionSnmpOID = _AdTaCtrlProvisionSnmpOID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 10, 16),
    _AdTaCtrlProvisionSnmpOID_Type()
)
adTaCtrlProvisionSnmpOID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaCtrlProvisionSnmpOID.setStatus("current")
_AdTaCtrlProvisionSnmpOIDIndex_Type = ObjectIdentifier
_AdTaCtrlProvisionSnmpOIDIndex_Object = MibScalar
adTaCtrlProvisionSnmpOIDIndex = _AdTaCtrlProvisionSnmpOIDIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 10, 17),
    _AdTaCtrlProvisionSnmpOIDIndex_Type()
)
adTaCtrlProvisionSnmpOIDIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaCtrlProvisionSnmpOIDIndex.setStatus("current")
_AdTaCtrlProvisionClientIPAddress_Type = IpAddress
_AdTaCtrlProvisionClientIPAddress_Object = MibScalar
adTaCtrlProvisionClientIPAddress = _AdTaCtrlProvisionClientIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 10, 18),
    _AdTaCtrlProvisionClientIPAddress_Type()
)
adTaCtrlProvisionClientIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaCtrlProvisionClientIPAddress.setStatus("current")
_AdTaCtrlProvisionScmIPAddress_Type = IpAddress
_AdTaCtrlProvisionScmIPAddress_Object = MibScalar
adTaCtrlProvisionScmIPAddress = _AdTaCtrlProvisionScmIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 10, 19),
    _AdTaCtrlProvisionScmIPAddress_Type()
)
adTaCtrlProvisionScmIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adTaCtrlProvisionScmIPAddress.setStatus("current")
_AdTaSysCtrlSnmpProvChange_ObjectIdentity = ObjectIdentity
adTaSysCtrlSnmpProvChange = _AdTaSysCtrlSnmpProvChange_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11)
)


class _AdTaSysCtrlSnmpProvChgMode_Type(Integer32):
    """Custom type adTaSysCtrlSnmpProvChgMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaSysCtrlSnmpProvChgMode_Type.__name__ = "Integer32"
_AdTaSysCtrlSnmpProvChgMode_Object = MibScalar
adTaSysCtrlSnmpProvChgMode = _AdTaSysCtrlSnmpProvChgMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11, 2),
    _AdTaSysCtrlSnmpProvChgMode_Type()
)
adTaSysCtrlSnmpProvChgMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSnmpProvChgMode.setStatus("current")


class _AdTaSysCtrlSCMProvChgTrapMode_Type(Integer32):
    """Custom type adTaSysCtrlSCMProvChgTrapMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaSysCtrlSCMProvChgTrapMode_Type.__name__ = "Integer32"
_AdTaSysCtrlSCMProvChgTrapMode_Object = MibScalar
adTaSysCtrlSCMProvChgTrapMode = _AdTaSysCtrlSCMProvChgTrapMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11, 3),
    _AdTaSysCtrlSCMProvChgTrapMode_Type()
)
adTaSysCtrlSCMProvChgTrapMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSCMProvChgTrapMode.setStatus("current")


class _AdTaSysCtrlSnmpNotifyHost1_Type(Integer32):
    """Custom type adTaSysCtrlSnmpNotifyHost1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaSysCtrlSnmpNotifyHost1_Type.__name__ = "Integer32"
_AdTaSysCtrlSnmpNotifyHost1_Object = MibScalar
adTaSysCtrlSnmpNotifyHost1 = _AdTaSysCtrlSnmpNotifyHost1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11, 5),
    _AdTaSysCtrlSnmpNotifyHost1_Type()
)
adTaSysCtrlSnmpNotifyHost1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSnmpNotifyHost1.setStatus("current")


class _AdTaSysCtrlSnmpNotifyHost2_Type(Integer32):
    """Custom type adTaSysCtrlSnmpNotifyHost2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaSysCtrlSnmpNotifyHost2_Type.__name__ = "Integer32"
_AdTaSysCtrlSnmpNotifyHost2_Object = MibScalar
adTaSysCtrlSnmpNotifyHost2 = _AdTaSysCtrlSnmpNotifyHost2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11, 6),
    _AdTaSysCtrlSnmpNotifyHost2_Type()
)
adTaSysCtrlSnmpNotifyHost2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSnmpNotifyHost2.setStatus("current")


class _AdTaSysCtrlSnmpNotifyHost3_Type(Integer32):
    """Custom type adTaSysCtrlSnmpNotifyHost3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaSysCtrlSnmpNotifyHost3_Type.__name__ = "Integer32"
_AdTaSysCtrlSnmpNotifyHost3_Object = MibScalar
adTaSysCtrlSnmpNotifyHost3 = _AdTaSysCtrlSnmpNotifyHost3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11, 7),
    _AdTaSysCtrlSnmpNotifyHost3_Type()
)
adTaSysCtrlSnmpNotifyHost3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSnmpNotifyHost3.setStatus("current")


class _AdTaSysCtrlSnmpNotifyHost4_Type(Integer32):
    """Custom type adTaSysCtrlSnmpNotifyHost4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_AdTaSysCtrlSnmpNotifyHost4_Type.__name__ = "Integer32"
_AdTaSysCtrlSnmpNotifyHost4_Object = MibScalar
adTaSysCtrlSnmpNotifyHost4 = _AdTaSysCtrlSnmpNotifyHost4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11, 8),
    _AdTaSysCtrlSnmpNotifyHost4_Type()
)
adTaSysCtrlSnmpNotifyHost4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlSnmpNotifyHost4.setStatus("current")
_AdTaSysCtrlOriginatorHostTable_Object = MibTable
adTaSysCtrlOriginatorHostTable = _AdTaSysCtrlOriginatorHostTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11, 10)
)
if mibBuilder.loadTexts:
    adTaSysCtrlOriginatorHostTable.setStatus("current")
_AdTaSysCtrlOriginatorHostEntry_Object = MibTableRow
adTaSysCtrlOriginatorHostEntry = _AdTaSysCtrlOriginatorHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11, 10, 1)
)
adTaSysCtrlOriginatorHostEntry.setIndexNames(
    (0, "ADTRAN-TACONTROLER-PRODUCT2-MIB", "adTaSysCtrlHostIndex"),
)
if mibBuilder.loadTexts:
    adTaSysCtrlOriginatorHostEntry.setStatus("current")


class _AdTaSysCtrlHostIndex_Type(Integer32):
    """Custom type adTaSysCtrlHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_AdTaSysCtrlHostIndex_Type.__name__ = "Integer32"
_AdTaSysCtrlHostIndex_Object = MibTableColumn
adTaSysCtrlHostIndex = _AdTaSysCtrlHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11, 10, 1, 1),
    _AdTaSysCtrlHostIndex_Type()
)
adTaSysCtrlHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adTaSysCtrlHostIndex.setStatus("current")
_AdTaSysCtrlOriginatorHostDisable_Type = IpAddress
_AdTaSysCtrlOriginatorHostDisable_Object = MibTableColumn
adTaSysCtrlOriginatorHostDisable = _AdTaSysCtrlOriginatorHostDisable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 11, 10, 1, 2),
    _AdTaSysCtrlOriginatorHostDisable_Type()
)
adTaSysCtrlOriginatorHostDisable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adTaSysCtrlOriginatorHostDisable.setStatus("current")

# Managed Objects groups


# Notification objects

adTAModuleProvisionChange = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 63, 1, 0, 2)
)
adTAModuleProvisionChange.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-TACONTROLER-PRODUCT2-MIB", "adTaCtrlProvisionSnmpOID"),
        ("ADTRAN-TACONTROLER-PRODUCT2-MIB", "adTaCtrlProvisionSnmpOIDIndex"),
        ("ADTRAN-TACONTROLER-PRODUCT2-MIB", "adTaCtrlChassisTimeStamp"),
        ("ADTRAN-TACONTROLER-PRODUCT2-MIB", "adTaCtrlProvisionScmIPAddress"),
        ("ADTRAN-TACONTROLER-PRODUCT2-MIB", "adTaCtrlProvisionClientIPAddress"),
        ("ADTRAN-TACONTROLER-PRODUCT2-MIB", "adTaCtrlChassisShelfNumber"),
        ("ADTRAN-TACONTROLER-PRODUCT2-MIB", "adTaCtrlChassisSlotNumber"),
        ("ADTRAN-TACONTROLER-PRODUCT2-MIB", "adTaCtrlEventDetails"))
)
if mibBuilder.loadTexts:
    adTAModuleProvisionChange.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-TACONTROLER-PRODUCT2-MIB",
    **{"adTaCtrlProduct2": adTaCtrlProduct2,
       "adTaSysCtrlNotifications": adTaSysCtrlNotifications,
       "adTAModuleProvisionChange": adTAModuleProvisionChange,
       "adTaSysCtrlScalars": adTaSysCtrlScalars,
       "adTaCtrlChassisSlotNumber": adTaCtrlChassisSlotNumber,
       "adTaCtrlChassisShelfNumber": adTaCtrlChassisShelfNumber,
       "adTaCtrlChassisTimeStamp": adTaCtrlChassisTimeStamp,
       "adTaCtrlEventDetails": adTaCtrlEventDetails,
       "adTaCtrlProvisionSnmpOID": adTaCtrlProvisionSnmpOID,
       "adTaCtrlProvisionSnmpOIDIndex": adTaCtrlProvisionSnmpOIDIndex,
       "adTaCtrlProvisionClientIPAddress": adTaCtrlProvisionClientIPAddress,
       "adTaCtrlProvisionScmIPAddress": adTaCtrlProvisionScmIPAddress,
       "adTaSysCtrlSnmpProvChange": adTaSysCtrlSnmpProvChange,
       "adTaSysCtrlSnmpProvChgMode": adTaSysCtrlSnmpProvChgMode,
       "adTaSysCtrlSCMProvChgTrapMode": adTaSysCtrlSCMProvChgTrapMode,
       "adTaSysCtrlSnmpNotifyHost1": adTaSysCtrlSnmpNotifyHost1,
       "adTaSysCtrlSnmpNotifyHost2": adTaSysCtrlSnmpNotifyHost2,
       "adTaSysCtrlSnmpNotifyHost3": adTaSysCtrlSnmpNotifyHost3,
       "adTaSysCtrlSnmpNotifyHost4": adTaSysCtrlSnmpNotifyHost4,
       "adTaSysCtrlOriginatorHostTable": adTaSysCtrlOriginatorHostTable,
       "adTaSysCtrlOriginatorHostEntry": adTaSysCtrlOriginatorHostEntry,
       "adTaSysCtrlHostIndex": adTaSysCtrlHostIndex,
       "adTaSysCtrlOriginatorHostDisable": adTaSysCtrlOriginatorHostDisable}
)
