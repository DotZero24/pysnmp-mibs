# SNMP MIB module (ADTRAN-GENTA8XX-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENTA8XX-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:55 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenSlotAlarmStatus,
 adGenSlotInfoIndex) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotAlarmStatus",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adGenTA8xx,
 adGenTA8xxID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-EOCU-MIB",
    "adGenTA8xx",
    "adGenTA8xxID")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(InetAddressIPv6,
 InetAddressPrefixLength) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddressIPv6",
    "InetAddressPrefixLength")

(ModuleCompliance,
 NotificationGroup,
 ObjectGroup) = mibBuilder.importSymbols(
    "SNMPv2-CONF",
    "ModuleCompliance",
    "NotificationGroup",
    "ObjectGroup")

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

(DisplayString,
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenTA8xxMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 2, 1)
)
if mibBuilder.loadTexts:
    adGenTA8xxMIB.setRevisions(
        ("2015-10-29 00:00",
         "2014-12-10 00:00",
         "2014-05-16 00:00",
         "2007-04-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenTA8xxEvents_ObjectIdentity = ObjectIdentity
adGenTA8xxEvents = _AdGenTA8xxEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0)
)
_AdGenTA8xxConfiguration_ObjectIdentity = ObjectIdentity
adGenTA8xxConfiguration = _AdGenTA8xxConfiguration_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1)
)
_AdGenTA8xxConfigTable_Object = MibTable
adGenTA8xxConfigTable = _AdGenTA8xxConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 1)
)
if mibBuilder.loadTexts:
    adGenTA8xxConfigTable.setStatus("current")
_AdGenTA8xxConfigEntry_Object = MibTableRow
adGenTA8xxConfigEntry = _AdGenTA8xxConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 1, 1)
)
adGenTA8xxConfigEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxConfigEntry.setStatus("current")
_AdGenTA8xxBootVersion_Type = DisplayString
_AdGenTA8xxBootVersion_Object = MibTableColumn
adGenTA8xxBootVersion = _AdGenTA8xxBootVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 1, 1, 1),
    _AdGenTA8xxBootVersion_Type()
)
adGenTA8xxBootVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxBootVersion.setStatus("current")
_AdGenTA8xxSwChecksum_Type = DisplayString
_AdGenTA8xxSwChecksum_Object = MibTableColumn
adGenTA8xxSwChecksum = _AdGenTA8xxSwChecksum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 1, 1, 2),
    _AdGenTA8xxSwChecksum_Type()
)
adGenTA8xxSwChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxSwChecksum.setStatus("current")
_AdGenTA8xxBootChecksum_Type = DisplayString
_AdGenTA8xxBootChecksum_Object = MibTableColumn
adGenTA8xxBootChecksum = _AdGenTA8xxBootChecksum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 1, 1, 3),
    _AdGenTA8xxBootChecksum_Type()
)
adGenTA8xxBootChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxBootChecksum.setStatus("current")
_AdGenTA8xxSavedSwVersion_Type = DisplayString
_AdGenTA8xxSavedSwVersion_Object = MibTableColumn
adGenTA8xxSavedSwVersion = _AdGenTA8xxSavedSwVersion_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 1, 1, 4),
    _AdGenTA8xxSavedSwVersion_Type()
)
adGenTA8xxSavedSwVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxSavedSwVersion.setStatus("current")
_AdGenTA8xxFarEndConfigTable_Object = MibTable
adGenTA8xxFarEndConfigTable = _AdGenTA8xxFarEndConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 2)
)
if mibBuilder.loadTexts:
    adGenTA8xxFarEndConfigTable.setStatus("current")
_AdGenTA8xxFarEndConfigEntry_Object = MibTableRow
adGenTA8xxFarEndConfigEntry = _AdGenTA8xxFarEndConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 2, 1)
)
adGenTA8xxFarEndConfigEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxFarEndConfigEntry.setStatus("current")
_AdGenTA8xxFarEndIfIndex_Type = InterfaceIndex
_AdGenTA8xxFarEndIfIndex_Object = MibTableColumn
adGenTA8xxFarEndIfIndex = _AdGenTA8xxFarEndIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 2, 1, 1),
    _AdGenTA8xxFarEndIfIndex_Type()
)
adGenTA8xxFarEndIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxFarEndIfIndex.setStatus("current")
_AdGenTA8xxFarEndIPAddress_Type = IpAddress
_AdGenTA8xxFarEndIPAddress_Object = MibTableColumn
adGenTA8xxFarEndIPAddress = _AdGenTA8xxFarEndIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 2, 1, 2),
    _AdGenTA8xxFarEndIPAddress_Type()
)
adGenTA8xxFarEndIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxFarEndIPAddress.setStatus("current")
_AdGenTA8xxFarEndSysName_Type = DisplayString
_AdGenTA8xxFarEndSysName_Object = MibTableColumn
adGenTA8xxFarEndSysName = _AdGenTA8xxFarEndSysName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 1, 2, 1, 3),
    _AdGenTA8xxFarEndSysName_Type()
)
adGenTA8xxFarEndSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxFarEndSysName.setStatus("current")
_AdGenTA8xxProvisioning_ObjectIdentity = ObjectIdentity
adGenTA8xxProvisioning = _AdGenTA8xxProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2)
)
_AdGenTA8xxPrvScalars_ObjectIdentity = ObjectIdentity
adGenTA8xxPrvScalars = _AdGenTA8xxPrvScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1)
)


class _AdGenTA8xxAutoLogoffTime_Type(Integer32):
    """Custom type adGenTA8xxAutoLogoffTime based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneMin", 2),
          ("fiveMin", 3),
          ("tenMin", 4),
          ("fifteenMin", 5),
          ("thirtyMin", 6),
          ("fortyfiveMin", 7),
          ("oneHour", 8))
    )


_AdGenTA8xxAutoLogoffTime_Type.__name__ = "Integer32"
_AdGenTA8xxAutoLogoffTime_Object = MibScalar
adGenTA8xxAutoLogoffTime = _AdGenTA8xxAutoLogoffTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 1),
    _AdGenTA8xxAutoLogoffTime_Type()
)
adGenTA8xxAutoLogoffTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxAutoLogoffTime.setStatus("current")


class _AdGenTA8xxSaveProv_Type(Integer32):
    """Custom type adGenTA8xxSaveProv based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("saveConfig", 1)
    )


_AdGenTA8xxSaveProv_Type.__name__ = "Integer32"
_AdGenTA8xxSaveProv_Object = MibScalar
adGenTA8xxSaveProv = _AdGenTA8xxSaveProv_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 2),
    _AdGenTA8xxSaveProv_Type()
)
adGenTA8xxSaveProv.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxSaveProv.setStatus("current")


class _AdGenTA8xxScheduledResetTime_Type(OctetString):
    """Custom type adGenTA8xxScheduledResetTime based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(17, 17),
    )
    fixed_length = 17


_AdGenTA8xxScheduledResetTime_Type.__name__ = "OctetString"
_AdGenTA8xxScheduledResetTime_Object = MibScalar
adGenTA8xxScheduledResetTime = _AdGenTA8xxScheduledResetTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 3),
    _AdGenTA8xxScheduledResetTime_Type()
)
adGenTA8xxScheduledResetTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxScheduledResetTime.setStatus("current")
_AdGenTA8xxSecondaryTelnetPort_Type = Integer32
_AdGenTA8xxSecondaryTelnetPort_Object = MibScalar
adGenTA8xxSecondaryTelnetPort = _AdGenTA8xxSecondaryTelnetPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 4),
    _AdGenTA8xxSecondaryTelnetPort_Type()
)
adGenTA8xxSecondaryTelnetPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxSecondaryTelnetPort.setStatus("current")
_AdGenTA8xxBondingPrimaryRef_Type = Integer32
_AdGenTA8xxBondingPrimaryRef_Object = MibScalar
adGenTA8xxBondingPrimaryRef = _AdGenTA8xxBondingPrimaryRef_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 5),
    _AdGenTA8xxBondingPrimaryRef_Type()
)
adGenTA8xxBondingPrimaryRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxBondingPrimaryRef.setStatus("current")
_AdGenTA8xxBondingSecondaryRef_Type = Integer32
_AdGenTA8xxBondingSecondaryRef_Object = MibScalar
adGenTA8xxBondingSecondaryRef = _AdGenTA8xxBondingSecondaryRef_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 6),
    _AdGenTA8xxBondingSecondaryRef_Type()
)
adGenTA8xxBondingSecondaryRef.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxBondingSecondaryRef.setStatus("current")
_AdGenTA8xxCapabilities_Type = OctetString
_AdGenTA8xxCapabilities_Object = MibScalar
adGenTA8xxCapabilities = _AdGenTA8xxCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 7),
    _AdGenTA8xxCapabilities_Type()
)
adGenTA8xxCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxCapabilities.setStatus("deprecated")


class _AdGenTA8xxIpACLState_Type(Integer32):
    """Custom type adGenTA8xxIpACLState based on Integer32"""
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


_AdGenTA8xxIpACLState_Type.__name__ = "Integer32"
_AdGenTA8xxIpACLState_Object = MibScalar
adGenTA8xxIpACLState = _AdGenTA8xxIpACLState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 8),
    _AdGenTA8xxIpACLState_Type()
)
adGenTA8xxIpACLState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxIpACLState.setStatus("current")
_AdGenTA8xxIpACLInsert_Type = IpAddress
_AdGenTA8xxIpACLInsert_Object = MibScalar
adGenTA8xxIpACLInsert = _AdGenTA8xxIpACLInsert_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 9),
    _AdGenTA8xxIpACLInsert_Type()
)
adGenTA8xxIpACLInsert.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxIpACLInsert.setStatus("current")
_AdGenTA8xxIpACLRemove_Type = IpAddress
_AdGenTA8xxIpACLRemove_Object = MibScalar
adGenTA8xxIpACLRemove = _AdGenTA8xxIpACLRemove_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 10),
    _AdGenTA8xxIpACLRemove_Type()
)
adGenTA8xxIpACLRemove.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxIpACLRemove.setStatus("current")


class _AdGenTA8xxIpACLRemoveAll_Type(Integer32):
    """Custom type adGenTA8xxIpACLRemoveAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("clearACL", 1)
    )


_AdGenTA8xxIpACLRemoveAll_Type.__name__ = "Integer32"
_AdGenTA8xxIpACLRemoveAll_Object = MibScalar
adGenTA8xxIpACLRemoveAll = _AdGenTA8xxIpACLRemoveAll_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 11),
    _AdGenTA8xxIpACLRemoveAll_Type()
)
adGenTA8xxIpACLRemoveAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxIpACLRemoveAll.setStatus("current")
_AdGenTA8xxTemperatureThresholdCelsuis_Type = Integer32
_AdGenTA8xxTemperatureThresholdCelsuis_Object = MibScalar
adGenTA8xxTemperatureThresholdCelsuis = _AdGenTA8xxTemperatureThresholdCelsuis_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 12),
    _AdGenTA8xxTemperatureThresholdCelsuis_Type()
)
adGenTA8xxTemperatureThresholdCelsuis.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTemperatureThresholdCelsuis.setStatus("current")
_AdGenTA8xxTemperatureThresholdFahrenheit_Type = Integer32
_AdGenTA8xxTemperatureThresholdFahrenheit_Object = MibScalar
adGenTA8xxTemperatureThresholdFahrenheit = _AdGenTA8xxTemperatureThresholdFahrenheit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 13),
    _AdGenTA8xxTemperatureThresholdFahrenheit_Type()
)
adGenTA8xxTemperatureThresholdFahrenheit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTemperatureThresholdFahrenheit.setStatus("current")
_AdGenTA8xxRollingAverageInterval_Type = Integer32
_AdGenTA8xxRollingAverageInterval_Object = MibScalar
adGenTA8xxRollingAverageInterval = _AdGenTA8xxRollingAverageInterval_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 1, 14),
    _AdGenTA8xxRollingAverageInterval_Type()
)
adGenTA8xxRollingAverageInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxRollingAverageInterval.setStatus("current")
_AdGenTA8xxPrv10100EthPortTable_Object = MibTable
adGenTA8xxPrv10100EthPortTable = _AdGenTA8xxPrv10100EthPortTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 2)
)
if mibBuilder.loadTexts:
    adGenTA8xxPrv10100EthPortTable.setStatus("current")
_AdGenTA8xxPrv10100EthPortEntry_Object = MibTableRow
adGenTA8xxPrv10100EthPortEntry = _AdGenTA8xxPrv10100EthPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 2, 1)
)
adGenTA8xxPrv10100EthPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxPrv10100EthPortEntry.setStatus("current")


class _AdGenTA8xx10100EthPortState_Type(Integer32):
    """Custom type adGenTA8xx10100EthPortState based on Integer32"""
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


_AdGenTA8xx10100EthPortState_Type.__name__ = "Integer32"
_AdGenTA8xx10100EthPortState_Object = MibTableColumn
adGenTA8xx10100EthPortState = _AdGenTA8xx10100EthPortState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 2, 1, 1),
    _AdGenTA8xx10100EthPortState_Type()
)
adGenTA8xx10100EthPortState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthPortState.setStatus("current")


class _AdGenTA8xx10100EthPortRateDuplex_Type(Integer32):
    """Custom type adGenTA8xx10100EthPortRateDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("auto", 4),
          ("half10Mbps", 5),
          ("full10Mbps", 6),
          ("half100Mbps", 7),
          ("full100Mbps", 8))
    )


_AdGenTA8xx10100EthPortRateDuplex_Type.__name__ = "Integer32"
_AdGenTA8xx10100EthPortRateDuplex_Object = MibTableColumn
adGenTA8xx10100EthPortRateDuplex = _AdGenTA8xx10100EthPortRateDuplex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 2, 1, 2),
    _AdGenTA8xx10100EthPortRateDuplex_Type()
)
adGenTA8xx10100EthPortRateDuplex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthPortRateDuplex.setStatus("current")


class _AdGenTA8xx10100EthPortCrossOverMode_Type(Integer32):
    """Custom type adGenTA8xx10100EthPortCrossOverMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mdi", 1),
          ("mdix", 2),
          ("auto", 3))
    )


_AdGenTA8xx10100EthPortCrossOverMode_Type.__name__ = "Integer32"
_AdGenTA8xx10100EthPortCrossOverMode_Object = MibTableColumn
adGenTA8xx10100EthPortCrossOverMode = _AdGenTA8xx10100EthPortCrossOverMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 2, 1, 3),
    _AdGenTA8xx10100EthPortCrossOverMode_Type()
)
adGenTA8xx10100EthPortCrossOverMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthPortCrossOverMode.setStatus("current")


class _AdGenTA8xx10100EthPortLsa_Type(Integer32):
    """Custom type adGenTA8xx10100EthPortLsa based on Integer32"""
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


_AdGenTA8xx10100EthPortLsa_Type.__name__ = "Integer32"
_AdGenTA8xx10100EthPortLsa_Object = MibTableColumn
adGenTA8xx10100EthPortLsa = _AdGenTA8xx10100EthPortLsa_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 2, 1, 4),
    _AdGenTA8xx10100EthPortLsa_Type()
)
adGenTA8xx10100EthPortLsa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthPortLsa.setStatus("current")
_AdGenTA8xx10100EthPortName_Type = DisplayString
_AdGenTA8xx10100EthPortName_Object = MibTableColumn
adGenTA8xx10100EthPortName = _AdGenTA8xx10100EthPortName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 2, 1, 5),
    _AdGenTA8xx10100EthPortName_Type()
)
adGenTA8xx10100EthPortName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthPortName.setStatus("current")
_AdGenTA8xx10100EthPortLsaBandwidthMinimum_Type = Gauge32
_AdGenTA8xx10100EthPortLsaBandwidthMinimum_Object = MibTableColumn
adGenTA8xx10100EthPortLsaBandwidthMinimum = _AdGenTA8xx10100EthPortLsaBandwidthMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 2, 1, 6),
    _AdGenTA8xx10100EthPortLsaBandwidthMinimum_Type()
)
adGenTA8xx10100EthPortLsaBandwidthMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthPortLsaBandwidthMinimum.setStatus("current")
_AdGenTA8xx10100EthPortLsaLinksMinimum_Type = Gauge32
_AdGenTA8xx10100EthPortLsaLinksMinimum_Object = MibTableColumn
adGenTA8xx10100EthPortLsaLinksMinimum = _AdGenTA8xx10100EthPortLsaLinksMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 2, 1, 7),
    _AdGenTA8xx10100EthPortLsaLinksMinimum_Type()
)
adGenTA8xx10100EthPortLsaLinksMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthPortLsaLinksMinimum.setStatus("current")
_AdGenTA8xxPrvGigEthTable_Object = MibTable
adGenTA8xxPrvGigEthTable = _AdGenTA8xxPrvGigEthTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 3)
)
if mibBuilder.loadTexts:
    adGenTA8xxPrvGigEthTable.setStatus("current")
_AdGenTA8xxPrvGigEthEntry_Object = MibTableRow
adGenTA8xxPrvGigEthEntry = _AdGenTA8xxPrvGigEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 3, 1)
)
adGenTA8xxPrvGigEthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxPrvGigEthEntry.setStatus("current")


class _AdGenTA8xxGigEthState_Type(Integer32):
    """Custom type adGenTA8xxGigEthState based on Integer32"""
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


_AdGenTA8xxGigEthState_Type.__name__ = "Integer32"
_AdGenTA8xxGigEthState_Object = MibTableColumn
adGenTA8xxGigEthState = _AdGenTA8xxGigEthState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 3, 1, 1),
    _AdGenTA8xxGigEthState_Type()
)
adGenTA8xxGigEthState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthState.setStatus("current")


class _AdGenTA8xxGigEthLsa_Type(Integer32):
    """Custom type adGenTA8xxGigEthLsa based on Integer32"""
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


_AdGenTA8xxGigEthLsa_Type.__name__ = "Integer32"
_AdGenTA8xxGigEthLsa_Object = MibTableColumn
adGenTA8xxGigEthLsa = _AdGenTA8xxGigEthLsa_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 3, 1, 2),
    _AdGenTA8xxGigEthLsa_Type()
)
adGenTA8xxGigEthLsa.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthLsa.setStatus("current")
_AdGenTA8xxGigEthName_Type = DisplayString
_AdGenTA8xxGigEthName_Object = MibTableColumn
adGenTA8xxGigEthName = _AdGenTA8xxGigEthName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 3, 1, 3),
    _AdGenTA8xxGigEthName_Type()
)
adGenTA8xxGigEthName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthName.setStatus("current")


class _AdGenTA8xxGigEthPortSpeed_Type(Integer32):
    """Custom type adGenTA8xxGigEthPortSpeed based on Integer32"""
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
        *(("auto", 1),
          ("speed100Mbps", 2),
          ("speed1000Mbps", 3),
          ("speed10Mbps", 4),
          ("speed2500Mbps", 5))
    )


_AdGenTA8xxGigEthPortSpeed_Type.__name__ = "Integer32"
_AdGenTA8xxGigEthPortSpeed_Object = MibTableColumn
adGenTA8xxGigEthPortSpeed = _AdGenTA8xxGigEthPortSpeed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 3, 1, 4),
    _AdGenTA8xxGigEthPortSpeed_Type()
)
adGenTA8xxGigEthPortSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthPortSpeed.setStatus("current")
_AdGenTA8xxGigEthLsaBandwidthMinimum_Type = Gauge32
_AdGenTA8xxGigEthLsaBandwidthMinimum_Object = MibTableColumn
adGenTA8xxGigEthLsaBandwidthMinimum = _AdGenTA8xxGigEthLsaBandwidthMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 3, 1, 5),
    _AdGenTA8xxGigEthLsaBandwidthMinimum_Type()
)
adGenTA8xxGigEthLsaBandwidthMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthLsaBandwidthMinimum.setStatus("current")
_AdGenTA8xxGigEthLsaLinksMinimum_Type = Gauge32
_AdGenTA8xxGigEthLsaLinksMinimum_Object = MibTableColumn
adGenTA8xxGigEthLsaLinksMinimum = _AdGenTA8xxGigEthLsaLinksMinimum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 3, 1, 6),
    _AdGenTA8xxGigEthLsaLinksMinimum_Type()
)
adGenTA8xxGigEthLsaLinksMinimum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthLsaLinksMinimum.setStatus("current")
_AdGenTA8xxCardPrvTable_Object = MibTable
adGenTA8xxCardPrvTable = _AdGenTA8xxCardPrvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 4)
)
if mibBuilder.loadTexts:
    adGenTA8xxCardPrvTable.setStatus("current")
_AdGenTA8xxCardPrvEntry_Object = MibTableRow
adGenTA8xxCardPrvEntry = _AdGenTA8xxCardPrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 4, 1)
)
adGenTA8xxCardPrvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxCardPrvEntry.setStatus("current")


class _AdGenTA8xxRestoreFactoryDefaults_Type(Integer32):
    """Custom type adGenTA8xxRestoreFactoryDefaults based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restoreFactoryDefaults", 1)
    )


_AdGenTA8xxRestoreFactoryDefaults_Type.__name__ = "Integer32"
_AdGenTA8xxRestoreFactoryDefaults_Object = MibTableColumn
adGenTA8xxRestoreFactoryDefaults = _AdGenTA8xxRestoreFactoryDefaults_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 4, 1, 1),
    _AdGenTA8xxRestoreFactoryDefaults_Type()
)
adGenTA8xxRestoreFactoryDefaults.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxRestoreFactoryDefaults.setStatus("current")


class _AdGenTA8xxReset_Type(Integer32):
    """Custom type adGenTA8xxReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenTA8xxReset_Type.__name__ = "Integer32"
_AdGenTA8xxReset_Object = MibTableColumn
adGenTA8xxReset = _AdGenTA8xxReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 2, 4, 1, 2),
    _AdGenTA8xxReset_Type()
)
adGenTA8xxReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxReset.setStatus("current")
_AdGenTA8xxStatus_ObjectIdentity = ObjectIdentity
adGenTA8xxStatus = _AdGenTA8xxStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3)
)
_AdGenTA8xxStatScalars_ObjectIdentity = ObjectIdentity
adGenTA8xxStatScalars = _AdGenTA8xxStatScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1)
)


class _AdGenTA8xxCardStatus_Type(Integer32):
    """Custom type adGenTA8xxCardStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4,
              6)
        )
    )
    namedValues = NamedValues(
        *(("softwareUpdate", 3),
          ("cardFailure", 4),
          ("normal", 6))
    )


_AdGenTA8xxCardStatus_Type.__name__ = "Integer32"
_AdGenTA8xxCardStatus_Object = MibScalar
adGenTA8xxCardStatus = _AdGenTA8xxCardStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 1),
    _AdGenTA8xxCardStatus_Type()
)
adGenTA8xxCardStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxCardStatus.setStatus("current")


class _AdGenTA8xxCritRelay_Type(Integer32):
    """Custom type adGenTA8xxCritRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenTA8xxCritRelay_Type.__name__ = "Integer32"
_AdGenTA8xxCritRelay_Object = MibScalar
adGenTA8xxCritRelay = _AdGenTA8xxCritRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 2),
    _AdGenTA8xxCritRelay_Type()
)
adGenTA8xxCritRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxCritRelay.setStatus("current")


class _AdGenTA8xxMajRelay_Type(Integer32):
    """Custom type adGenTA8xxMajRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenTA8xxMajRelay_Type.__name__ = "Integer32"
_AdGenTA8xxMajRelay_Object = MibScalar
adGenTA8xxMajRelay = _AdGenTA8xxMajRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 3),
    _AdGenTA8xxMajRelay_Type()
)
adGenTA8xxMajRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxMajRelay.setStatus("current")


class _AdGenTA8xxMinRelay_Type(Integer32):
    """Custom type adGenTA8xxMinRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenTA8xxMinRelay_Type.__name__ = "Integer32"
_AdGenTA8xxMinRelay_Object = MibScalar
adGenTA8xxMinRelay = _AdGenTA8xxMinRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 4),
    _AdGenTA8xxMinRelay_Type()
)
adGenTA8xxMinRelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxMinRelay.setStatus("current")


class _AdGenTA8xxacoStatus_Type(Integer32):
    """Custom type adGenTA8xxacoStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("released", 1),
          ("pressed", 2))
    )


_AdGenTA8xxacoStatus_Type.__name__ = "Integer32"
_AdGenTA8xxacoStatus_Object = MibScalar
adGenTA8xxacoStatus = _AdGenTA8xxacoStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 5),
    _AdGenTA8xxacoStatus_Type()
)
adGenTA8xxacoStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxacoStatus.setStatus("current")


class _AdGenTA8xxACPwrInStatus_Type(Integer32):
    """Custom type adGenTA8xxACPwrInStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenTA8xxACPwrInStatus_Type.__name__ = "Integer32"
_AdGenTA8xxACPwrInStatus_Object = MibScalar
adGenTA8xxACPwrInStatus = _AdGenTA8xxACPwrInStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 6),
    _AdGenTA8xxACPwrInStatus_Type()
)
adGenTA8xxACPwrInStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxACPwrInStatus.setStatus("current")


class _AdGenTA8xxPowerAStatus_Type(Integer32):
    """Custom type adGenTA8xxPowerAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenTA8xxPowerAStatus_Type.__name__ = "Integer32"
_AdGenTA8xxPowerAStatus_Object = MibScalar
adGenTA8xxPowerAStatus = _AdGenTA8xxPowerAStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 7),
    _AdGenTA8xxPowerAStatus_Type()
)
adGenTA8xxPowerAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxPowerAStatus.setStatus("current")


class _AdGenTA8xxPowerBStatus_Type(Integer32):
    """Custom type adGenTA8xxPowerBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenTA8xxPowerBStatus_Type.__name__ = "Integer32"
_AdGenTA8xxPowerBStatus_Object = MibScalar
adGenTA8xxPowerBStatus = _AdGenTA8xxPowerBStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 8),
    _AdGenTA8xxPowerBStatus_Type()
)
adGenTA8xxPowerBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxPowerBStatus.setStatus("current")


class _AdGenTA8xxEnvAlarmsAggregateStatus_Type(Integer32):
    """Custom type adGenTA8xxEnvAlarmsAggregateStatus based on Integer32"""
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
        *(("ok", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenTA8xxEnvAlarmsAggregateStatus_Type.__name__ = "Integer32"
_AdGenTA8xxEnvAlarmsAggregateStatus_Object = MibScalar
adGenTA8xxEnvAlarmsAggregateStatus = _AdGenTA8xxEnvAlarmsAggregateStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 9),
    _AdGenTA8xxEnvAlarmsAggregateStatus_Type()
)
adGenTA8xxEnvAlarmsAggregateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxEnvAlarmsAggregateStatus.setStatus("current")
_AdGenTA8xxIPAddress_Type = IpAddress
_AdGenTA8xxIPAddress_Object = MibScalar
adGenTA8xxIPAddress = _AdGenTA8xxIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 10),
    _AdGenTA8xxIPAddress_Type()
)
adGenTA8xxIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxIPAddress.setStatus("current")
_AdGenTA8xxSubnetMask_Type = IpAddress
_AdGenTA8xxSubnetMask_Object = MibScalar
adGenTA8xxSubnetMask = _AdGenTA8xxSubnetMask_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 11),
    _AdGenTA8xxSubnetMask_Type()
)
adGenTA8xxSubnetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxSubnetMask.setStatus("current")
_AdGenTA8xxDefaultGateway_Type = IpAddress
_AdGenTA8xxDefaultGateway_Object = MibScalar
adGenTA8xxDefaultGateway = _AdGenTA8xxDefaultGateway_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 12),
    _AdGenTA8xxDefaultGateway_Type()
)
adGenTA8xxDefaultGateway.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxDefaultGateway.setStatus("current")


class _AdGenTA8xxBondingFunctLineSource_Type(Integer32):
    """Custom type adGenTA8xxBondingFunctLineSource based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("primaryLine", 1),
          ("secondaryLine", 2),
          ("fail", 3))
    )


_AdGenTA8xxBondingFunctLineSource_Type.__name__ = "Integer32"
_AdGenTA8xxBondingFunctLineSource_Object = MibScalar
adGenTA8xxBondingFunctLineSource = _AdGenTA8xxBondingFunctLineSource_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 13),
    _AdGenTA8xxBondingFunctLineSource_Type()
)
adGenTA8xxBondingFunctLineSource.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxBondingFunctLineSource.setStatus("current")


class _AdGenTA8xxBondingPriRefStatus_Type(Integer32):
    """Custom type adGenTA8xxBondingPriRefStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fail", 2),
          ("notApplicable", 3))
    )


_AdGenTA8xxBondingPriRefStatus_Type.__name__ = "Integer32"
_AdGenTA8xxBondingPriRefStatus_Object = MibScalar
adGenTA8xxBondingPriRefStatus = _AdGenTA8xxBondingPriRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 14),
    _AdGenTA8xxBondingPriRefStatus_Type()
)
adGenTA8xxBondingPriRefStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxBondingPriRefStatus.setStatus("current")


class _AdGenTA8xxBondingSecRefStatus_Type(Integer32):
    """Custom type adGenTA8xxBondingSecRefStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("ok", 1),
          ("fail", 2),
          ("notApplicable", 3))
    )


_AdGenTA8xxBondingSecRefStatus_Type.__name__ = "Integer32"
_AdGenTA8xxBondingSecRefStatus_Object = MibScalar
adGenTA8xxBondingSecRefStatus = _AdGenTA8xxBondingSecRefStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 15),
    _AdGenTA8xxBondingSecRefStatus_Type()
)
adGenTA8xxBondingSecRefStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxBondingSecRefStatus.setStatus("current")
_AdGenTA8xxIpACLDepth_Type = Integer32
_AdGenTA8xxIpACLDepth_Object = MibScalar
adGenTA8xxIpACLDepth = _AdGenTA8xxIpACLDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 16),
    _AdGenTA8xxIpACLDepth_Type()
)
adGenTA8xxIpACLDepth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxIpACLDepth.setStatus("current")
_AdGenTA8xxCurrentCPUUtilization_Type = DisplayString
_AdGenTA8xxCurrentCPUUtilization_Object = MibScalar
adGenTA8xxCurrentCPUUtilization = _AdGenTA8xxCurrentCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 17),
    _AdGenTA8xxCurrentCPUUtilization_Type()
)
adGenTA8xxCurrentCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxCurrentCPUUtilization.setStatus("current")
_AdGenTA8xxMaxCPUUtilization_Type = DisplayString
_AdGenTA8xxMaxCPUUtilization_Object = MibScalar
adGenTA8xxMaxCPUUtilization = _AdGenTA8xxMaxCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 18),
    _AdGenTA8xxMaxCPUUtilization_Type()
)
adGenTA8xxMaxCPUUtilization.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxMaxCPUUtilization.setStatus("current")


class _AdGenTA8xxResetMaxCPUUtilization_Type(Integer32):
    """Custom type adGenTA8xxResetMaxCPUUtilization based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenTA8xxResetMaxCPUUtilization_Type.__name__ = "Integer32"
_AdGenTA8xxResetMaxCPUUtilization_Object = MibScalar
adGenTA8xxResetMaxCPUUtilization = _AdGenTA8xxResetMaxCPUUtilization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 19),
    _AdGenTA8xxResetMaxCPUUtilization_Type()
)
adGenTA8xxResetMaxCPUUtilization.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxResetMaxCPUUtilization.setStatus("current")
_AdGenTA8xxTemperatureCelsuis_Type = DisplayString
_AdGenTA8xxTemperatureCelsuis_Object = MibScalar
adGenTA8xxTemperatureCelsuis = _AdGenTA8xxTemperatureCelsuis_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 20),
    _AdGenTA8xxTemperatureCelsuis_Type()
)
adGenTA8xxTemperatureCelsuis.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxTemperatureCelsuis.setStatus("current")
_AdGenTA8xxTemperatureFahrenheit_Type = DisplayString
_AdGenTA8xxTemperatureFahrenheit_Object = MibScalar
adGenTA8xxTemperatureFahrenheit = _AdGenTA8xxTemperatureFahrenheit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 21),
    _AdGenTA8xxTemperatureFahrenheit_Type()
)
adGenTA8xxTemperatureFahrenheit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxTemperatureFahrenheit.setStatus("current")


class _AdGenTA8xxCustomerDoor_Type(Integer32):
    """Custom type adGenTA8xxCustomerDoor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )


_AdGenTA8xxCustomerDoor_Type.__name__ = "Integer32"
_AdGenTA8xxCustomerDoor_Object = MibScalar
adGenTA8xxCustomerDoor = _AdGenTA8xxCustomerDoor_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 22),
    _AdGenTA8xxCustomerDoor_Type()
)
adGenTA8xxCustomerDoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxCustomerDoor.setStatus("current")


class _AdGenTA8xxTelcoDoor_Type(Integer32):
    """Custom type adGenTA8xxTelcoDoor based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )


_AdGenTA8xxTelcoDoor_Type.__name__ = "Integer32"
_AdGenTA8xxTelcoDoor_Object = MibScalar
adGenTA8xxTelcoDoor = _AdGenTA8xxTelcoDoor_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 23),
    _AdGenTA8xxTelcoDoor_Type()
)
adGenTA8xxTelcoDoor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxTelcoDoor.setStatus("current")


class _AdGenTA8xxAux1Door_Type(Integer32):
    """Custom type adGenTA8xxAux1Door based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("open", 1),
          ("closed", 2))
    )


_AdGenTA8xxAux1Door_Type.__name__ = "Integer32"
_AdGenTA8xxAux1Door_Object = MibScalar
adGenTA8xxAux1Door = _AdGenTA8xxAux1Door_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 24),
    _AdGenTA8xxAux1Door_Type()
)
adGenTA8xxAux1Door.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxAux1Door.setStatus("current")
_AdGenTA8xxIpv6AddressPrefixLength_Type = InetAddressPrefixLength
_AdGenTA8xxIpv6AddressPrefixLength_Object = MibScalar
adGenTA8xxIpv6AddressPrefixLength = _AdGenTA8xxIpv6AddressPrefixLength_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 25),
    _AdGenTA8xxIpv6AddressPrefixLength_Type()
)
adGenTA8xxIpv6AddressPrefixLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxIpv6AddressPrefixLength.setStatus("current")
_AdGenTA8xxIpv6AddressEui64_Type = TruthValue
_AdGenTA8xxIpv6AddressEui64_Object = MibScalar
adGenTA8xxIpv6AddressEui64 = _AdGenTA8xxIpv6AddressEui64_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 26),
    _AdGenTA8xxIpv6AddressEui64_Type()
)
adGenTA8xxIpv6AddressEui64.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxIpv6AddressEui64.setStatus("current")
_AdGenTA8xxIpv6Address_Type = InetAddressIPv6
_AdGenTA8xxIpv6Address_Object = MibScalar
adGenTA8xxIpv6Address = _AdGenTA8xxIpv6Address_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 27),
    _AdGenTA8xxIpv6Address_Type()
)
adGenTA8xxIpv6Address.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxIpv6Address.setStatus("current")
_AdGenTA8xxIpv6AddressOperational_Type = InetAddressIPv6
_AdGenTA8xxIpv6AddressOperational_Object = MibScalar
adGenTA8xxIpv6AddressOperational = _AdGenTA8xxIpv6AddressOperational_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 28),
    _AdGenTA8xxIpv6AddressOperational_Type()
)
adGenTA8xxIpv6AddressOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxIpv6AddressOperational.setStatus("current")
_AdGenTA8xxIpv6AddressLinkLocal_Type = InetAddressIPv6
_AdGenTA8xxIpv6AddressLinkLocal_Object = MibScalar
adGenTA8xxIpv6AddressLinkLocal = _AdGenTA8xxIpv6AddressLinkLocal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 29),
    _AdGenTA8xxIpv6AddressLinkLocal_Type()
)
adGenTA8xxIpv6AddressLinkLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxIpv6AddressLinkLocal.setStatus("current")
_AdGenTA8xxIpv6AddressLinkLocalOperational_Type = InetAddressIPv6
_AdGenTA8xxIpv6AddressLinkLocalOperational_Object = MibScalar
adGenTA8xxIpv6AddressLinkLocalOperational = _AdGenTA8xxIpv6AddressLinkLocalOperational_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 1, 30),
    _AdGenTA8xxIpv6AddressLinkLocalOperational_Type()
)
adGenTA8xxIpv6AddressLinkLocalOperational.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxIpv6AddressLinkLocalOperational.setStatus("current")
_AdGenTA8xxStat10100EthTable_Object = MibTable
adGenTA8xxStat10100EthTable = _AdGenTA8xxStat10100EthTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 2)
)
if mibBuilder.loadTexts:
    adGenTA8xxStat10100EthTable.setStatus("current")
_AdGenTA8xxStat10100EthEntry_Object = MibTableRow
adGenTA8xxStat10100EthEntry = _AdGenTA8xxStat10100EthEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 2, 1)
)
adGenTA8xxStat10100EthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxStat10100EthEntry.setStatus("current")


class _AdGenTA8xx10100EthLinkStatus_Type(Integer32):
    """Custom type adGenTA8xx10100EthLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AdGenTA8xx10100EthLinkStatus_Type.__name__ = "Integer32"
_AdGenTA8xx10100EthLinkStatus_Object = MibTableColumn
adGenTA8xx10100EthLinkStatus = _AdGenTA8xx10100EthLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 2, 1, 1),
    _AdGenTA8xx10100EthLinkStatus_Type()
)
adGenTA8xx10100EthLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthLinkStatus.setStatus("current")


class _AdGenTA8xx10100EthLinkSpeedDuplex_Type(Integer32):
    """Custom type adGenTA8xx10100EthLinkSpeedDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("half10Mbps", 5),
          ("full10Mbps", 6),
          ("half100Mbps", 7),
          ("full100Mbps", 8))
    )


_AdGenTA8xx10100EthLinkSpeedDuplex_Type.__name__ = "Integer32"
_AdGenTA8xx10100EthLinkSpeedDuplex_Object = MibTableColumn
adGenTA8xx10100EthLinkSpeedDuplex = _AdGenTA8xx10100EthLinkSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 2, 1, 2),
    _AdGenTA8xx10100EthLinkSpeedDuplex_Type()
)
adGenTA8xx10100EthLinkSpeedDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthLinkSpeedDuplex.setStatus("current")
_AdGenTA8xxStatGigEthTable_Object = MibTable
adGenTA8xxStatGigEthTable = _AdGenTA8xxStatGigEthTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3)
)
if mibBuilder.loadTexts:
    adGenTA8xxStatGigEthTable.setStatus("current")
_AdGenTA8xxStatGigEthEntry_Object = MibTableRow
adGenTA8xxStatGigEthEntry = _AdGenTA8xxStatGigEthEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1)
)
adGenTA8xxStatGigEthEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxStatGigEthEntry.setStatus("current")


class _AdGenTA8xxGigEthLinkStatus_Type(Integer32):
    """Custom type adGenTA8xxGigEthLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("up", 1),
          ("down", 2))
    )


_AdGenTA8xxGigEthLinkStatus_Type.__name__ = "Integer32"
_AdGenTA8xxGigEthLinkStatus_Object = MibTableColumn
adGenTA8xxGigEthLinkStatus = _AdGenTA8xxGigEthLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 1),
    _AdGenTA8xxGigEthLinkStatus_Type()
)
adGenTA8xxGigEthLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthLinkStatus.setStatus("current")
_AdGenTA8xxGigEthSFPDescription_Type = DisplayString
_AdGenTA8xxGigEthSFPDescription_Object = MibTableColumn
adGenTA8xxGigEthSFPDescription = _AdGenTA8xxGigEthSFPDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 2),
    _AdGenTA8xxGigEthSFPDescription_Type()
)
adGenTA8xxGigEthSFPDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthSFPDescription.setStatus("current")
_AdGenTA8xxGigEthSFPADTRANSerialNumber_Type = DisplayString
_AdGenTA8xxGigEthSFPADTRANSerialNumber_Object = MibTableColumn
adGenTA8xxGigEthSFPADTRANSerialNumber = _AdGenTA8xxGigEthSFPADTRANSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 3),
    _AdGenTA8xxGigEthSFPADTRANSerialNumber_Type()
)
adGenTA8xxGigEthSFPADTRANSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthSFPADTRANSerialNumber.setStatus("current")
_AdGenTA8xxGigEthSFPADTRANPartNumber_Type = DisplayString
_AdGenTA8xxGigEthSFPADTRANPartNumber_Object = MibTableColumn
adGenTA8xxGigEthSFPADTRANPartNumber = _AdGenTA8xxGigEthSFPADTRANPartNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 4),
    _AdGenTA8xxGigEthSFPADTRANPartNumber_Type()
)
adGenTA8xxGigEthSFPADTRANPartNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthSFPADTRANPartNumber.setStatus("current")
_AdGenTA8xxGigEthSFPADTRANCLEICode_Type = DisplayString
_AdGenTA8xxGigEthSFPADTRANCLEICode_Object = MibTableColumn
adGenTA8xxGigEthSFPADTRANCLEICode = _AdGenTA8xxGigEthSFPADTRANCLEICode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 5),
    _AdGenTA8xxGigEthSFPADTRANCLEICode_Type()
)
adGenTA8xxGigEthSFPADTRANCLEICode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthSFPADTRANCLEICode.setStatus("current")


class _AdGenTA8xxGigEthSFPJackType_Type(Integer32):
    """Custom type adGenTA8xxGigEthSFPJackType based on Integer32"""
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
        *(("other", 1),
          ("fiberLC", 2),
          ("fiberSC", 3),
          ("mtrj", 4),
          ("hssdc", 5),
          ("copperRJ45", 6))
    )


_AdGenTA8xxGigEthSFPJackType_Type.__name__ = "Integer32"
_AdGenTA8xxGigEthSFPJackType_Object = MibTableColumn
adGenTA8xxGigEthSFPJackType = _AdGenTA8xxGigEthSFPJackType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 6),
    _AdGenTA8xxGigEthSFPJackType_Type()
)
adGenTA8xxGigEthSFPJackType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthSFPJackType.setStatus("current")


class _AdGenTA8xxGigEthSFPADTRANApproved_Type(Integer32):
    """Custom type adGenTA8xxGigEthSFPADTRANApproved based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notApplicable", 1),
          ("approved", 2),
          ("notApproved", 3))
    )


_AdGenTA8xxGigEthSFPADTRANApproved_Type.__name__ = "Integer32"
_AdGenTA8xxGigEthSFPADTRANApproved_Object = MibTableColumn
adGenTA8xxGigEthSFPADTRANApproved = _AdGenTA8xxGigEthSFPADTRANApproved_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 7),
    _AdGenTA8xxGigEthSFPADTRANApproved_Type()
)
adGenTA8xxGigEthSFPADTRANApproved.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthSFPADTRANApproved.setStatus("current")
_AdGenTA8xxGigEthSFPTemperature_Type = DisplayString
_AdGenTA8xxGigEthSFPTemperature_Object = MibTableColumn
adGenTA8xxGigEthSFPTemperature = _AdGenTA8xxGigEthSFPTemperature_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 8),
    _AdGenTA8xxGigEthSFPTemperature_Type()
)
adGenTA8xxGigEthSFPTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthSFPTemperature.setStatus("current")
_AdGenTA8xxGigEthSFPTxBias_Type = DisplayString
_AdGenTA8xxGigEthSFPTxBias_Object = MibTableColumn
adGenTA8xxGigEthSFPTxBias = _AdGenTA8xxGigEthSFPTxBias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 9),
    _AdGenTA8xxGigEthSFPTxBias_Type()
)
adGenTA8xxGigEthSFPTxBias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthSFPTxBias.setStatus("current")
_AdGenTA8xxGigEthSFPTxPower_Type = DisplayString
_AdGenTA8xxGigEthSFPTxPower_Object = MibTableColumn
adGenTA8xxGigEthSFPTxPower = _AdGenTA8xxGigEthSFPTxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 10),
    _AdGenTA8xxGigEthSFPTxPower_Type()
)
adGenTA8xxGigEthSFPTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthSFPTxPower.setStatus("current")
_AdGenTA8xxGigEthSFPRxPower_Type = DisplayString
_AdGenTA8xxGigEthSFPRxPower_Object = MibTableColumn
adGenTA8xxGigEthSFPRxPower = _AdGenTA8xxGigEthSFPRxPower_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 11),
    _AdGenTA8xxGigEthSFPRxPower_Type()
)
adGenTA8xxGigEthSFPRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthSFPRxPower.setStatus("current")


class _AdGenTA8xxGigEthLinkSpeedDuplex_Type(Integer32):
    """Custom type adGenTA8xxGigEthLinkSpeedDuplex based on Integer32"""
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
              9)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("half10Mbps", 2),
          ("full10Mbps", 3),
          ("half100Mbps", 4),
          ("full100Mbps", 5),
          ("half1000Mbps", 6),
          ("full1000Mbps", 7),
          ("half2500Mbps", 8),
          ("full2500Mbps", 9))
    )


_AdGenTA8xxGigEthLinkSpeedDuplex_Type.__name__ = "Integer32"
_AdGenTA8xxGigEthLinkSpeedDuplex_Object = MibTableColumn
adGenTA8xxGigEthLinkSpeedDuplex = _AdGenTA8xxGigEthLinkSpeedDuplex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 3, 1, 12),
    _AdGenTA8xxGigEthLinkSpeedDuplex_Type()
)
adGenTA8xxGigEthLinkSpeedDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthLinkSpeedDuplex.setStatus("current")
_AdGenTA8xxStatIpAclTable_Object = MibTable
adGenTA8xxStatIpAclTable = _AdGenTA8xxStatIpAclTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 4)
)
if mibBuilder.loadTexts:
    adGenTA8xxStatIpAclTable.setStatus("current")
_AdGenTA8xxStatIpAclEntry_Object = MibTableRow
adGenTA8xxStatIpAclEntry = _AdGenTA8xxStatIpAclEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 4, 1)
)
adGenTA8xxStatIpAclEntry.setIndexNames(
    (0, "ADTRAN-GENTA8XX-MIB", "adGenTA8xxIpAclEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxStatIpAclEntry.setStatus("current")
_AdGenTA8xxIpAclEntryIndex_Type = Integer32
_AdGenTA8xxIpAclEntryIndex_Object = MibTableColumn
adGenTA8xxIpAclEntryIndex = _AdGenTA8xxIpAclEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 4, 1, 1),
    _AdGenTA8xxIpAclEntryIndex_Type()
)
adGenTA8xxIpAclEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxIpAclEntryIndex.setStatus("current")
_AdGenTA8xxIpAclEntries_Type = IpAddress
_AdGenTA8xxIpAclEntries_Object = MibTableColumn
adGenTA8xxIpAclEntries = _AdGenTA8xxIpAclEntries_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 3, 4, 1, 2),
    _AdGenTA8xxIpAclEntries_Type()
)
adGenTA8xxIpAclEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxIpAclEntries.setStatus("current")
_AdGenTA8xxPerformance_ObjectIdentity = ObjectIdentity
adGenTA8xxPerformance = _AdGenTA8xxPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4)
)
_AdGenTA8xxPerformanceScalars_ObjectIdentity = ObjectIdentity
adGenTA8xxPerformanceScalars = _AdGenTA8xxPerformanceScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 1)
)


class _AdGenTA8xxRstAllCurrentIntervals_Type(Integer32):
    """Custom type adGenTA8xxRstAllCurrentIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rstAllCurrentIntervals", 1)
    )


_AdGenTA8xxRstAllCurrentIntervals_Type.__name__ = "Integer32"
_AdGenTA8xxRstAllCurrentIntervals_Object = MibScalar
adGenTA8xxRstAllCurrentIntervals = _AdGenTA8xxRstAllCurrentIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 1, 1),
    _AdGenTA8xxRstAllCurrentIntervals_Type()
)
adGenTA8xxRstAllCurrentIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxRstAllCurrentIntervals.setStatus("current")


class _AdGenTA8xxRstAllIntervals_Type(Integer32):
    """Custom type adGenTA8xxRstAllIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("rstAllIntervals", 1)
    )


_AdGenTA8xxRstAllIntervals_Type.__name__ = "Integer32"
_AdGenTA8xxRstAllIntervals_Object = MibScalar
adGenTA8xxRstAllIntervals = _AdGenTA8xxRstAllIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 1, 2),
    _AdGenTA8xxRstAllIntervals_Type()
)
adGenTA8xxRstAllIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxRstAllIntervals.setStatus("current")
_AdGenTA8xxMgmtStatsCurrentTxFrames_Type = Gauge32
_AdGenTA8xxMgmtStatsCurrentTxFrames_Object = MibScalar
adGenTA8xxMgmtStatsCurrentTxFrames = _AdGenTA8xxMgmtStatsCurrentTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 1, 3),
    _AdGenTA8xxMgmtStatsCurrentTxFrames_Type()
)
adGenTA8xxMgmtStatsCurrentTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxMgmtStatsCurrentTxFrames.setStatus("current")
_AdGenTA8xxMgmtStatsCurrentRxFrames_Type = Gauge32
_AdGenTA8xxMgmtStatsCurrentRxFrames_Object = MibScalar
adGenTA8xxMgmtStatsCurrentRxFrames = _AdGenTA8xxMgmtStatsCurrentRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 1, 4),
    _AdGenTA8xxMgmtStatsCurrentRxFrames_Type()
)
adGenTA8xxMgmtStatsCurrentRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxMgmtStatsCurrentRxFrames.setStatus("current")
_AdGenTA8xx10100EthPerformance_ObjectIdentity = ObjectIdentity
adGenTA8xx10100EthPerformance = _AdGenTA8xx10100EthPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2)
)
_AdGenTA8xx10100EthPerformanceScalars_ObjectIdentity = ObjectIdentity
adGenTA8xx10100EthPerformanceScalars = _AdGenTA8xx10100EthPerformanceScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 1)
)


class _AdGenTA8xx10100EthRstCurrentIntervals_Type(Integer32):
    """Custom type adGenTA8xx10100EthRstCurrentIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethRstAllCurrentIntervals", 1)
    )


_AdGenTA8xx10100EthRstCurrentIntervals_Type.__name__ = "Integer32"
_AdGenTA8xx10100EthRstCurrentIntervals_Object = MibScalar
adGenTA8xx10100EthRstCurrentIntervals = _AdGenTA8xx10100EthRstCurrentIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 1, 1),
    _AdGenTA8xx10100EthRstCurrentIntervals_Type()
)
adGenTA8xx10100EthRstCurrentIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthRstCurrentIntervals.setStatus("current")


class _AdGenTA8xx10100EthRstAll_Type(Integer32):
    """Custom type adGenTA8xx10100EthRstAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethRstAll", 1)
    )


_AdGenTA8xx10100EthRstAll_Type.__name__ = "Integer32"
_AdGenTA8xx10100EthRstAll_Object = MibScalar
adGenTA8xx10100EthRstAll = _AdGenTA8xx10100EthRstAll_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 1, 2),
    _AdGenTA8xx10100EthRstAll_Type()
)
adGenTA8xx10100EthRstAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthRstAll.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentTable_Object = MibTable
adGenTA8xx10100Eth15MinCurrentTable = _AdGenTA8xx10100Eth15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2)
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentTable.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentEntry_Object = MibTableRow
adGenTA8xx10100Eth15MinCurrentEntry = _AdGenTA8xx10100Eth15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1)
)
adGenTA8xx10100Eth15MinCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentEntry.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentTxBytes_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentTxBytes_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentTxBytes = _AdGenTA8xx10100Eth15MinCurrentTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 1),
    _AdGenTA8xx10100Eth15MinCurrentTxBytes_Type()
)
adGenTA8xx10100Eth15MinCurrentTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentTxBytes.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentTxFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentTxFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentTxFrames = _AdGenTA8xx10100Eth15MinCurrentTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 2),
    _AdGenTA8xx10100Eth15MinCurrentTxFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentTxFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxBytes_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxBytes_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxBytes = _AdGenTA8xx10100Eth15MinCurrentRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 3),
    _AdGenTA8xx10100Eth15MinCurrentRxBytes_Type()
)
adGenTA8xx10100Eth15MinCurrentRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxBytes.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxFrames = _AdGenTA8xx10100Eth15MinCurrentRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 4),
    _AdGenTA8xx10100Eth15MinCurrentRxFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxCRCAlignErrs_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxCRCAlignErrs_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxCRCAlignErrs = _AdGenTA8xx10100Eth15MinCurrentRxCRCAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 5),
    _AdGenTA8xx10100Eth15MinCurrentRxCRCAlignErrs_Type()
)
adGenTA8xx10100Eth15MinCurrentRxCRCAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxCRCAlignErrs.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxUndersizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxUndersizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxUndersizeFrames = _AdGenTA8xx10100Eth15MinCurrentRxUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 6),
    _AdGenTA8xx10100Eth15MinCurrentRxUndersizeFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentRxUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxUndersizeFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxOversizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxOversizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxOversizeFrames = _AdGenTA8xx10100Eth15MinCurrentRxOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 7),
    _AdGenTA8xx10100Eth15MinCurrentRxOversizeFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentRxOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxOversizeFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxCollisions_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxCollisions_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxCollisions = _AdGenTA8xx10100Eth15MinCurrentRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 8),
    _AdGenTA8xx10100Eth15MinCurrentRxCollisions_Type()
)
adGenTA8xx10100Eth15MinCurrentRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxCollisions.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxDiscardedFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxDiscardedFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxDiscardedFrames = _AdGenTA8xx10100Eth15MinCurrentRxDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 9),
    _AdGenTA8xx10100Eth15MinCurrentRxDiscardedFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentRxDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxDiscardedFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxMulticastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxMulticastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxMulticastFrames = _AdGenTA8xx10100Eth15MinCurrentRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 10),
    _AdGenTA8xx10100Eth15MinCurrentRxMulticastFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxMulticastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxBroadcastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxBroadcastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxBroadcastFrames = _AdGenTA8xx10100Eth15MinCurrentRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 11),
    _AdGenTA8xx10100Eth15MinCurrentRxBroadcastFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxBroadcastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxUnicastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxUnicastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxUnicastFrames = _AdGenTA8xx10100Eth15MinCurrentRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 12),
    _AdGenTA8xx10100Eth15MinCurrentRxUnicastFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxUnicastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentTxMulticastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentTxMulticastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentTxMulticastFrames = _AdGenTA8xx10100Eth15MinCurrentTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 13),
    _AdGenTA8xx10100Eth15MinCurrentTxMulticastFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentTxMulticastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentTxBroadcastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentTxBroadcastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentTxBroadcastFrames = _AdGenTA8xx10100Eth15MinCurrentTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 14),
    _AdGenTA8xx10100Eth15MinCurrentTxBroadcastFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentTxBroadcastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentTxUnicastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentTxUnicastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentTxUnicastFrames = _AdGenTA8xx10100Eth15MinCurrentTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 15),
    _AdGenTA8xx10100Eth15MinCurrentTxUnicastFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentTxUnicastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxGoodBytes_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxGoodBytes_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxGoodBytes = _AdGenTA8xx10100Eth15MinCurrentRxGoodBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 16),
    _AdGenTA8xx10100Eth15MinCurrentRxGoodBytes_Type()
)
adGenTA8xx10100Eth15MinCurrentRxGoodBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxGoodBytes.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxGoodFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxGoodFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxGoodFrames = _AdGenTA8xx10100Eth15MinCurrentRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 17),
    _AdGenTA8xx10100Eth15MinCurrentRxGoodFrames_Type()
)
adGenTA8xx10100Eth15MinCurrentRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxGoodFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxJabbers_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxJabbers_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxJabbers = _AdGenTA8xx10100Eth15MinCurrentRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 18),
    _AdGenTA8xx10100Eth15MinCurrentRxJabbers_Type()
)
adGenTA8xx10100Eth15MinCurrentRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxJabbers.setStatus("current")
_AdGenTA8xx10100Eth15MinCurrentRxFragments_Type = Gauge32
_AdGenTA8xx10100Eth15MinCurrentRxFragments_Object = MibTableColumn
adGenTA8xx10100Eth15MinCurrentRxFragments = _AdGenTA8xx10100Eth15MinCurrentRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 2, 1, 19),
    _AdGenTA8xx10100Eth15MinCurrentRxFragments_Type()
)
adGenTA8xx10100Eth15MinCurrentRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinCurrentRxFragments.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalTable_Object = MibTable
adGenTA8xx10100Eth15MinIntervalTable = _AdGenTA8xx10100Eth15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3)
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalTable.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalEntry_Object = MibTableRow
adGenTA8xx10100Eth15MinIntervalEntry = _AdGenTA8xx10100Eth15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1)
)
adGenTA8xx10100Eth15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalEntry.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalNumber_Type = Integer32
_AdGenTA8xx10100Eth15MinIntervalNumber_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalNumber = _AdGenTA8xx10100Eth15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 1),
    _AdGenTA8xx10100Eth15MinIntervalNumber_Type()
)
adGenTA8xx10100Eth15MinIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalNumber.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalTxBytes_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalTxBytes_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalTxBytes = _AdGenTA8xx10100Eth15MinIntervalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 2),
    _AdGenTA8xx10100Eth15MinIntervalTxBytes_Type()
)
adGenTA8xx10100Eth15MinIntervalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalTxBytes.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalTxFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalTxFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalTxFrames = _AdGenTA8xx10100Eth15MinIntervalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 3),
    _AdGenTA8xx10100Eth15MinIntervalTxFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalTxFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxBytes_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxBytes_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxBytes = _AdGenTA8xx10100Eth15MinIntervalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 4),
    _AdGenTA8xx10100Eth15MinIntervalRxBytes_Type()
)
adGenTA8xx10100Eth15MinIntervalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxBytes.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxFrames = _AdGenTA8xx10100Eth15MinIntervalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 5),
    _AdGenTA8xx10100Eth15MinIntervalRxFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxCRCAlignErrs_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxCRCAlignErrs_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxCRCAlignErrs = _AdGenTA8xx10100Eth15MinIntervalRxCRCAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 6),
    _AdGenTA8xx10100Eth15MinIntervalRxCRCAlignErrs_Type()
)
adGenTA8xx10100Eth15MinIntervalRxCRCAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxCRCAlignErrs.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxUndersizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxUndersizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxUndersizeFrames = _AdGenTA8xx10100Eth15MinIntervalRxUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 7),
    _AdGenTA8xx10100Eth15MinIntervalRxUndersizeFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalRxUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxUndersizeFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxOversizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxOversizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxOversizeFrames = _AdGenTA8xx10100Eth15MinIntervalRxOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 8),
    _AdGenTA8xx10100Eth15MinIntervalRxOversizeFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalRxOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxOversizeFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxCollisions_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxCollisions_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxCollisions = _AdGenTA8xx10100Eth15MinIntervalRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 9),
    _AdGenTA8xx10100Eth15MinIntervalRxCollisions_Type()
)
adGenTA8xx10100Eth15MinIntervalRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxCollisions.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxDiscardedFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxDiscardedFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxDiscardedFrames = _AdGenTA8xx10100Eth15MinIntervalRxDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 10),
    _AdGenTA8xx10100Eth15MinIntervalRxDiscardedFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalRxDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxDiscardedFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxMulticastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxMulticastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxMulticastFrames = _AdGenTA8xx10100Eth15MinIntervalRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 11),
    _AdGenTA8xx10100Eth15MinIntervalRxMulticastFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxMulticastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxBroadcastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxBroadcastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxBroadcastFrames = _AdGenTA8xx10100Eth15MinIntervalRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 12),
    _AdGenTA8xx10100Eth15MinIntervalRxBroadcastFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxBroadcastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxUnicastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxUnicastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxUnicastFrames = _AdGenTA8xx10100Eth15MinIntervalRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 13),
    _AdGenTA8xx10100Eth15MinIntervalRxUnicastFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxUnicastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalTxMulticastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalTxMulticastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalTxMulticastFrames = _AdGenTA8xx10100Eth15MinIntervalTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 14),
    _AdGenTA8xx10100Eth15MinIntervalTxMulticastFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalTxMulticastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalTxBroadcastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalTxBroadcastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalTxBroadcastFrames = _AdGenTA8xx10100Eth15MinIntervalTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 15),
    _AdGenTA8xx10100Eth15MinIntervalTxBroadcastFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalTxBroadcastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalTxUnicastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalTxUnicastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalTxUnicastFrames = _AdGenTA8xx10100Eth15MinIntervalTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 16),
    _AdGenTA8xx10100Eth15MinIntervalTxUnicastFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalTxUnicastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxGoodBytes_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxGoodBytes_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxGoodBytes = _AdGenTA8xx10100Eth15MinIntervalRxGoodBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 17),
    _AdGenTA8xx10100Eth15MinIntervalRxGoodBytes_Type()
)
adGenTA8xx10100Eth15MinIntervalRxGoodBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxGoodBytes.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxGoodFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxGoodFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxGoodFrames = _AdGenTA8xx10100Eth15MinIntervalRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 18),
    _AdGenTA8xx10100Eth15MinIntervalRxGoodFrames_Type()
)
adGenTA8xx10100Eth15MinIntervalRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxGoodFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxJabbers_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxJabbers_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxJabbers = _AdGenTA8xx10100Eth15MinIntervalRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 19),
    _AdGenTA8xx10100Eth15MinIntervalRxJabbers_Type()
)
adGenTA8xx10100Eth15MinIntervalRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxJabbers.setStatus("current")
_AdGenTA8xx10100Eth15MinIntervalRxFragments_Type = Gauge32
_AdGenTA8xx10100Eth15MinIntervalRxFragments_Object = MibTableColumn
adGenTA8xx10100Eth15MinIntervalRxFragments = _AdGenTA8xx10100Eth15MinIntervalRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 3, 1, 20),
    _AdGenTA8xx10100Eth15MinIntervalRxFragments_Type()
)
adGenTA8xx10100Eth15MinIntervalRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinIntervalRxFragments.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentTable_Object = MibTable
adGenTA8xx10100Eth24HrCurrentTable = _AdGenTA8xx10100Eth24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4)
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentTable.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentEntry_Object = MibTableRow
adGenTA8xx10100Eth24HrCurrentEntry = _AdGenTA8xx10100Eth24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1)
)
adGenTA8xx10100Eth24HrCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentEntry.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentTxBytes_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentTxBytes_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentTxBytes = _AdGenTA8xx10100Eth24HrCurrentTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 1),
    _AdGenTA8xx10100Eth24HrCurrentTxBytes_Type()
)
adGenTA8xx10100Eth24HrCurrentTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentTxBytes.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentTxFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentTxFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentTxFrames = _AdGenTA8xx10100Eth24HrCurrentTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 2),
    _AdGenTA8xx10100Eth24HrCurrentTxFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentTxFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxBytes_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxBytes_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxBytes = _AdGenTA8xx10100Eth24HrCurrentRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 3),
    _AdGenTA8xx10100Eth24HrCurrentRxBytes_Type()
)
adGenTA8xx10100Eth24HrCurrentRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxBytes.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxFrames = _AdGenTA8xx10100Eth24HrCurrentRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 4),
    _AdGenTA8xx10100Eth24HrCurrentRxFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxCRCAlignErrs_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxCRCAlignErrs_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxCRCAlignErrs = _AdGenTA8xx10100Eth24HrCurrentRxCRCAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 5),
    _AdGenTA8xx10100Eth24HrCurrentRxCRCAlignErrs_Type()
)
adGenTA8xx10100Eth24HrCurrentRxCRCAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxCRCAlignErrs.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxUndersizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxUndersizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxUndersizeFrames = _AdGenTA8xx10100Eth24HrCurrentRxUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 6),
    _AdGenTA8xx10100Eth24HrCurrentRxUndersizeFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentRxUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxUndersizeFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxOversizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxOversizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxOversizeFrames = _AdGenTA8xx10100Eth24HrCurrentRxOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 7),
    _AdGenTA8xx10100Eth24HrCurrentRxOversizeFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentRxOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxOversizeFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxCollisions_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxCollisions_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxCollisions = _AdGenTA8xx10100Eth24HrCurrentRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 8),
    _AdGenTA8xx10100Eth24HrCurrentRxCollisions_Type()
)
adGenTA8xx10100Eth24HrCurrentRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxCollisions.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxDiscardedFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxDiscardedFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxDiscardedFrames = _AdGenTA8xx10100Eth24HrCurrentRxDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 9),
    _AdGenTA8xx10100Eth24HrCurrentRxDiscardedFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentRxDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxDiscardedFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxMulticastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxMulticastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxMulticastFrames = _AdGenTA8xx10100Eth24HrCurrentRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 10),
    _AdGenTA8xx10100Eth24HrCurrentRxMulticastFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxMulticastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxBroadcastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxBroadcastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxBroadcastFrames = _AdGenTA8xx10100Eth24HrCurrentRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 11),
    _AdGenTA8xx10100Eth24HrCurrentRxBroadcastFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxBroadcastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxUnicastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxUnicastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxUnicastFrames = _AdGenTA8xx10100Eth24HrCurrentRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 12),
    _AdGenTA8xx10100Eth24HrCurrentRxUnicastFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxUnicastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentTxMulticastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentTxMulticastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentTxMulticastFrames = _AdGenTA8xx10100Eth24HrCurrentTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 13),
    _AdGenTA8xx10100Eth24HrCurrentTxMulticastFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentTxMulticastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentTxBroadcastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentTxBroadcastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentTxBroadcastFrames = _AdGenTA8xx10100Eth24HrCurrentTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 14),
    _AdGenTA8xx10100Eth24HrCurrentTxBroadcastFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentTxBroadcastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentTxUnicastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentTxUnicastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentTxUnicastFrames = _AdGenTA8xx10100Eth24HrCurrentTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 15),
    _AdGenTA8xx10100Eth24HrCurrentTxUnicastFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentTxUnicastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxGoodBytes_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxGoodBytes_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxGoodBytes = _AdGenTA8xx10100Eth24HrCurrentRxGoodBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 16),
    _AdGenTA8xx10100Eth24HrCurrentRxGoodBytes_Type()
)
adGenTA8xx10100Eth24HrCurrentRxGoodBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxGoodBytes.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxGoodFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxGoodFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxGoodFrames = _AdGenTA8xx10100Eth24HrCurrentRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 17),
    _AdGenTA8xx10100Eth24HrCurrentRxGoodFrames_Type()
)
adGenTA8xx10100Eth24HrCurrentRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxGoodFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxJabbers_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxJabbers_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxJabbers = _AdGenTA8xx10100Eth24HrCurrentRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 18),
    _AdGenTA8xx10100Eth24HrCurrentRxJabbers_Type()
)
adGenTA8xx10100Eth24HrCurrentRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxJabbers.setStatus("current")
_AdGenTA8xx10100Eth24HrCurrentRxFragments_Type = Gauge32
_AdGenTA8xx10100Eth24HrCurrentRxFragments_Object = MibTableColumn
adGenTA8xx10100Eth24HrCurrentRxFragments = _AdGenTA8xx10100Eth24HrCurrentRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 4, 1, 19),
    _AdGenTA8xx10100Eth24HrCurrentRxFragments_Type()
)
adGenTA8xx10100Eth24HrCurrentRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrCurrentRxFragments.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalTable_Object = MibTable
adGenTA8xx10100Eth24HrIntervalTable = _AdGenTA8xx10100Eth24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5)
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalTable.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalEntry_Object = MibTableRow
adGenTA8xx10100Eth24HrIntervalEntry = _AdGenTA8xx10100Eth24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1)
)
adGenTA8xx10100Eth24HrIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalEntry.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalNumber_Type = Integer32
_AdGenTA8xx10100Eth24HrIntervalNumber_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalNumber = _AdGenTA8xx10100Eth24HrIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 1),
    _AdGenTA8xx10100Eth24HrIntervalNumber_Type()
)
adGenTA8xx10100Eth24HrIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalNumber.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalTxBytes_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalTxBytes_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalTxBytes = _AdGenTA8xx10100Eth24HrIntervalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 2),
    _AdGenTA8xx10100Eth24HrIntervalTxBytes_Type()
)
adGenTA8xx10100Eth24HrIntervalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalTxBytes.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalTxFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalTxFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalTxFrames = _AdGenTA8xx10100Eth24HrIntervalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 3),
    _AdGenTA8xx10100Eth24HrIntervalTxFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalTxFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxBytes_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxBytes_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxBytes = _AdGenTA8xx10100Eth24HrIntervalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 4),
    _AdGenTA8xx10100Eth24HrIntervalRxBytes_Type()
)
adGenTA8xx10100Eth24HrIntervalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxBytes.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxFrames = _AdGenTA8xx10100Eth24HrIntervalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 5),
    _AdGenTA8xx10100Eth24HrIntervalRxFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxCRCAlignErrs_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxCRCAlignErrs_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxCRCAlignErrs = _AdGenTA8xx10100Eth24HrIntervalRxCRCAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 6),
    _AdGenTA8xx10100Eth24HrIntervalRxCRCAlignErrs_Type()
)
adGenTA8xx10100Eth24HrIntervalRxCRCAlignErrs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxCRCAlignErrs.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxUndersizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxUndersizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxUndersizeFrames = _AdGenTA8xx10100Eth24HrIntervalRxUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 7),
    _AdGenTA8xx10100Eth24HrIntervalRxUndersizeFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalRxUndersizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxUndersizeFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxOversizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxOversizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxOversizeFrames = _AdGenTA8xx10100Eth24HrIntervalRxOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 8),
    _AdGenTA8xx10100Eth24HrIntervalRxOversizeFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalRxOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxOversizeFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxCollisions_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxCollisions_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxCollisions = _AdGenTA8xx10100Eth24HrIntervalRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 9),
    _AdGenTA8xx10100Eth24HrIntervalRxCollisions_Type()
)
adGenTA8xx10100Eth24HrIntervalRxCollisions.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxCollisions.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxDiscardedFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxDiscardedFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxDiscardedFrames = _AdGenTA8xx10100Eth24HrIntervalRxDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 10),
    _AdGenTA8xx10100Eth24HrIntervalRxDiscardedFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalRxDiscardedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxDiscardedFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxMulticastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxMulticastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxMulticastFrames = _AdGenTA8xx10100Eth24HrIntervalRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 11),
    _AdGenTA8xx10100Eth24HrIntervalRxMulticastFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxMulticastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxBroadcastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxBroadcastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxBroadcastFrames = _AdGenTA8xx10100Eth24HrIntervalRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 12),
    _AdGenTA8xx10100Eth24HrIntervalRxBroadcastFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxBroadcastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxUnicastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxUnicastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxUnicastFrames = _AdGenTA8xx10100Eth24HrIntervalRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 13),
    _AdGenTA8xx10100Eth24HrIntervalRxUnicastFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxUnicastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalTxMulticastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalTxMulticastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalTxMulticastFrames = _AdGenTA8xx10100Eth24HrIntervalTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 14),
    _AdGenTA8xx10100Eth24HrIntervalTxMulticastFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalTxMulticastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalTxBroadcastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalTxBroadcastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalTxBroadcastFrames = _AdGenTA8xx10100Eth24HrIntervalTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 15),
    _AdGenTA8xx10100Eth24HrIntervalTxBroadcastFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalTxBroadcastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalTxUnicastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalTxUnicastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalTxUnicastFrames = _AdGenTA8xx10100Eth24HrIntervalTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 16),
    _AdGenTA8xx10100Eth24HrIntervalTxUnicastFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalTxUnicastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxGoodBytes_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxGoodBytes_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxGoodBytes = _AdGenTA8xx10100Eth24HrIntervalRxGoodBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 17),
    _AdGenTA8xx10100Eth24HrIntervalRxGoodBytes_Type()
)
adGenTA8xx10100Eth24HrIntervalRxGoodBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxGoodBytes.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxGoodFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxGoodFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxGoodFrames = _AdGenTA8xx10100Eth24HrIntervalRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 18),
    _AdGenTA8xx10100Eth24HrIntervalRxGoodFrames_Type()
)
adGenTA8xx10100Eth24HrIntervalRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxGoodFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxJabbers_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxJabbers_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxJabbers = _AdGenTA8xx10100Eth24HrIntervalRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 19),
    _AdGenTA8xx10100Eth24HrIntervalRxJabbers_Type()
)
adGenTA8xx10100Eth24HrIntervalRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxJabbers.setStatus("current")
_AdGenTA8xx10100Eth24HrIntervalRxFragments_Type = Gauge32
_AdGenTA8xx10100Eth24HrIntervalRxFragments_Object = MibTableColumn
adGenTA8xx10100Eth24HrIntervalRxFragments = _AdGenTA8xx10100Eth24HrIntervalRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 5, 1, 20),
    _AdGenTA8xx10100Eth24HrIntervalRxFragments_Type()
)
adGenTA8xx10100Eth24HrIntervalRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrIntervalRxFragments.setStatus("current")
_AdGenTA8xx10100EthPerfResetTable_Object = MibTable
adGenTA8xx10100EthPerfResetTable = _AdGenTA8xx10100EthPerfResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 6)
)
if mibBuilder.loadTexts:
    adGenTA8xx10100EthPerfResetTable.setStatus("current")
_AdGenTA8xx10100EthPerfResetEntry_Object = MibTableRow
adGenTA8xx10100EthPerfResetEntry = _AdGenTA8xx10100EthPerfResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 6, 1)
)
adGenTA8xx10100EthPerfResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xx10100EthPerfResetEntry.setStatus("current")


class _AdGenTA8xx10100EthPerfReset_Type(Integer32):
    """Custom type adGenTA8xx10100EthPerfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethPerfRst", 1)
    )


_AdGenTA8xx10100EthPerfReset_Type.__name__ = "Integer32"
_AdGenTA8xx10100EthPerfReset_Object = MibTableColumn
adGenTA8xx10100EthPerfReset = _AdGenTA8xx10100EthPerfReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 2, 6, 1, 1),
    _AdGenTA8xx10100EthPerfReset_Type()
)
adGenTA8xx10100EthPerfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100EthPerfReset.setStatus("current")
_AdGenTA8xxGigEthPerformance_ObjectIdentity = ObjectIdentity
adGenTA8xxGigEthPerformance = _AdGenTA8xxGigEthPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3)
)
_AdGenTA8xxGigEthPerformanceScalars_ObjectIdentity = ObjectIdentity
adGenTA8xxGigEthPerformanceScalars = _AdGenTA8xxGigEthPerformanceScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 1)
)


class _AdGenTA8xxGigEthRstCurrentIntervals_Type(Integer32):
    """Custom type adGenTA8xxGigEthRstCurrentIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethRstAllCurrentIntervals", 1)
    )


_AdGenTA8xxGigEthRstCurrentIntervals_Type.__name__ = "Integer32"
_AdGenTA8xxGigEthRstCurrentIntervals_Object = MibScalar
adGenTA8xxGigEthRstCurrentIntervals = _AdGenTA8xxGigEthRstCurrentIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 1, 1),
    _AdGenTA8xxGigEthRstCurrentIntervals_Type()
)
adGenTA8xxGigEthRstCurrentIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthRstCurrentIntervals.setStatus("current")


class _AdGenTA8xxGigEthRstAll_Type(Integer32):
    """Custom type adGenTA8xxGigEthRstAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethRstAll", 1)
    )


_AdGenTA8xxGigEthRstAll_Type.__name__ = "Integer32"
_AdGenTA8xxGigEthRstAll_Object = MibScalar
adGenTA8xxGigEthRstAll = _AdGenTA8xxGigEthRstAll_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 1, 2),
    _AdGenTA8xxGigEthRstAll_Type()
)
adGenTA8xxGigEthRstAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthRstAll.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentTable_Object = MibTable
adGenTA8xxGigEth15MinCurrentTable = _AdGenTA8xxGigEth15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2)
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentTable.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentEntry_Object = MibTableRow
adGenTA8xxGigEth15MinCurrentEntry = _AdGenTA8xxGigEth15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1)
)
adGenTA8xxGigEth15MinCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentEntry.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentTxBytes_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentTxBytes_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentTxBytes = _AdGenTA8xxGigEth15MinCurrentTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 1),
    _AdGenTA8xxGigEth15MinCurrentTxBytes_Type()
)
adGenTA8xxGigEth15MinCurrentTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentTxBytes.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentTxFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentTxFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentTxFrames = _AdGenTA8xxGigEth15MinCurrentTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 2),
    _AdGenTA8xxGigEth15MinCurrentTxFrames_Type()
)
adGenTA8xxGigEth15MinCurrentTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentTxFrames.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxBytes_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxBytes_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxBytes = _AdGenTA8xxGigEth15MinCurrentRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 3),
    _AdGenTA8xxGigEth15MinCurrentRxBytes_Type()
)
adGenTA8xxGigEth15MinCurrentRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxBytes.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxFrames = _AdGenTA8xxGigEth15MinCurrentRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 4),
    _AdGenTA8xxGigEth15MinCurrentRxFrames_Type()
)
adGenTA8xxGigEth15MinCurrentRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxFrames.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxGoodBytes_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxGoodBytes_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxGoodBytes = _AdGenTA8xxGigEth15MinCurrentRxGoodBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 5),
    _AdGenTA8xxGigEth15MinCurrentRxGoodBytes_Type()
)
adGenTA8xxGigEth15MinCurrentRxGoodBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxGoodBytes.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxGoodFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxGoodFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxGoodFrames = _AdGenTA8xxGigEth15MinCurrentRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 6),
    _AdGenTA8xxGigEth15MinCurrentRxGoodFrames_Type()
)
adGenTA8xxGigEth15MinCurrentRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxGoodFrames.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxFCSErrors_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxFCSErrors_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxFCSErrors = _AdGenTA8xxGigEth15MinCurrentRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 7),
    _AdGenTA8xxGigEth15MinCurrentRxFCSErrors_Type()
)
adGenTA8xxGigEth15MinCurrentRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxFCSErrors.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxDroppedFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxDroppedFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxDroppedFrames = _AdGenTA8xxGigEth15MinCurrentRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 8),
    _AdGenTA8xxGigEth15MinCurrentRxDroppedFrames_Type()
)
adGenTA8xxGigEth15MinCurrentRxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxDroppedFrames.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxFramesTooBig_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxFramesTooBig_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxFramesTooBig = _AdGenTA8xxGigEth15MinCurrentRxFramesTooBig_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 9),
    _AdGenTA8xxGigEth15MinCurrentRxFramesTooBig_Type()
)
adGenTA8xxGigEth15MinCurrentRxFramesTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxFramesTooBig.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxFramesTooSmall_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxFramesTooSmall_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxFramesTooSmall = _AdGenTA8xxGigEth15MinCurrentRxFramesTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 10),
    _AdGenTA8xxGigEth15MinCurrentRxFramesTooSmall_Type()
)
adGenTA8xxGigEth15MinCurrentRxFramesTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxFramesTooSmall.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxMulticastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxMulticastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxMulticastFrames = _AdGenTA8xxGigEth15MinCurrentRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 11),
    _AdGenTA8xxGigEth15MinCurrentRxMulticastFrames_Type()
)
adGenTA8xxGigEth15MinCurrentRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxMulticastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxBroadcastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxBroadcastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxBroadcastFrames = _AdGenTA8xxGigEth15MinCurrentRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 12),
    _AdGenTA8xxGigEth15MinCurrentRxBroadcastFrames_Type()
)
adGenTA8xxGigEth15MinCurrentRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxBroadcastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxUnicastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxUnicastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxUnicastFrames = _AdGenTA8xxGigEth15MinCurrentRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 13),
    _AdGenTA8xxGigEth15MinCurrentRxUnicastFrames_Type()
)
adGenTA8xxGigEth15MinCurrentRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxUnicastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentTxMulticastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentTxMulticastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentTxMulticastFrames = _AdGenTA8xxGigEth15MinCurrentTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 14),
    _AdGenTA8xxGigEth15MinCurrentTxMulticastFrames_Type()
)
adGenTA8xxGigEth15MinCurrentTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentTxMulticastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentTxBroadcastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentTxBroadcastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentTxBroadcastFrames = _AdGenTA8xxGigEth15MinCurrentTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 15),
    _AdGenTA8xxGigEth15MinCurrentTxBroadcastFrames_Type()
)
adGenTA8xxGigEth15MinCurrentTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentTxBroadcastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentTxUnicastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentTxUnicastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentTxUnicastFrames = _AdGenTA8xxGigEth15MinCurrentTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 16),
    _AdGenTA8xxGigEth15MinCurrentTxUnicastFrames_Type()
)
adGenTA8xxGigEth15MinCurrentTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentTxUnicastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxJabbers_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxJabbers_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxJabbers = _AdGenTA8xxGigEth15MinCurrentRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 17),
    _AdGenTA8xxGigEth15MinCurrentRxJabbers_Type()
)
adGenTA8xxGigEth15MinCurrentRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxJabbers.setStatus("current")
_AdGenTA8xxGigEth15MinCurrentRxFragments_Type = Gauge32
_AdGenTA8xxGigEth15MinCurrentRxFragments_Object = MibTableColumn
adGenTA8xxGigEth15MinCurrentRxFragments = _AdGenTA8xxGigEth15MinCurrentRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 2, 1, 18),
    _AdGenTA8xxGigEth15MinCurrentRxFragments_Type()
)
adGenTA8xxGigEth15MinCurrentRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinCurrentRxFragments.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalTable_Object = MibTable
adGenTA8xxGigEth15MinIntervalTable = _AdGenTA8xxGigEth15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3)
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalTable.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalEntry_Object = MibTableRow
adGenTA8xxGigEth15MinIntervalEntry = _AdGenTA8xxGigEth15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1)
)
adGenTA8xxGigEth15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalEntry.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalNumber_Type = Integer32
_AdGenTA8xxGigEth15MinIntervalNumber_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalNumber = _AdGenTA8xxGigEth15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 1),
    _AdGenTA8xxGigEth15MinIntervalNumber_Type()
)
adGenTA8xxGigEth15MinIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalNumber.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalTxBytes_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalTxBytes_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalTxBytes = _AdGenTA8xxGigEth15MinIntervalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 2),
    _AdGenTA8xxGigEth15MinIntervalTxBytes_Type()
)
adGenTA8xxGigEth15MinIntervalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalTxBytes.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalTxFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalTxFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalTxFrames = _AdGenTA8xxGigEth15MinIntervalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 3),
    _AdGenTA8xxGigEth15MinIntervalTxFrames_Type()
)
adGenTA8xxGigEth15MinIntervalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalTxFrames.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxBytes_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxBytes_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxBytes = _AdGenTA8xxGigEth15MinIntervalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 4),
    _AdGenTA8xxGigEth15MinIntervalRxBytes_Type()
)
adGenTA8xxGigEth15MinIntervalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxBytes.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxFrames = _AdGenTA8xxGigEth15MinIntervalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 5),
    _AdGenTA8xxGigEth15MinIntervalRxFrames_Type()
)
adGenTA8xxGigEth15MinIntervalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxFrames.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxGoodBytes_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxGoodBytes_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxGoodBytes = _AdGenTA8xxGigEth15MinIntervalRxGoodBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 6),
    _AdGenTA8xxGigEth15MinIntervalRxGoodBytes_Type()
)
adGenTA8xxGigEth15MinIntervalRxGoodBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxGoodBytes.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxGoodFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxGoodFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxGoodFrames = _AdGenTA8xxGigEth15MinIntervalRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 7),
    _AdGenTA8xxGigEth15MinIntervalRxGoodFrames_Type()
)
adGenTA8xxGigEth15MinIntervalRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxGoodFrames.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxFCSErrors_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxFCSErrors_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxFCSErrors = _AdGenTA8xxGigEth15MinIntervalRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 8),
    _AdGenTA8xxGigEth15MinIntervalRxFCSErrors_Type()
)
adGenTA8xxGigEth15MinIntervalRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxFCSErrors.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxDroppedFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxDroppedFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxDroppedFrames = _AdGenTA8xxGigEth15MinIntervalRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 9),
    _AdGenTA8xxGigEth15MinIntervalRxDroppedFrames_Type()
)
adGenTA8xxGigEth15MinIntervalRxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxDroppedFrames.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxFramesTooBig_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxFramesTooBig_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxFramesTooBig = _AdGenTA8xxGigEth15MinIntervalRxFramesTooBig_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 10),
    _AdGenTA8xxGigEth15MinIntervalRxFramesTooBig_Type()
)
adGenTA8xxGigEth15MinIntervalRxFramesTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxFramesTooBig.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxFramesTooSmall_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxFramesTooSmall_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxFramesTooSmall = _AdGenTA8xxGigEth15MinIntervalRxFramesTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 11),
    _AdGenTA8xxGigEth15MinIntervalRxFramesTooSmall_Type()
)
adGenTA8xxGigEth15MinIntervalRxFramesTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxFramesTooSmall.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxMulticastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxMulticastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxMulticastFrames = _AdGenTA8xxGigEth15MinIntervalRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 12),
    _AdGenTA8xxGigEth15MinIntervalRxMulticastFrames_Type()
)
adGenTA8xxGigEth15MinIntervalRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxMulticastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxBroadcastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxBroadcastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxBroadcastFrames = _AdGenTA8xxGigEth15MinIntervalRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 13),
    _AdGenTA8xxGigEth15MinIntervalRxBroadcastFrames_Type()
)
adGenTA8xxGigEth15MinIntervalRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxBroadcastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxUnicastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxUnicastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxUnicastFrames = _AdGenTA8xxGigEth15MinIntervalRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 14),
    _AdGenTA8xxGigEth15MinIntervalRxUnicastFrames_Type()
)
adGenTA8xxGigEth15MinIntervalRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxUnicastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalTxMulticastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalTxMulticastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalTxMulticastFrames = _AdGenTA8xxGigEth15MinIntervalTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 15),
    _AdGenTA8xxGigEth15MinIntervalTxMulticastFrames_Type()
)
adGenTA8xxGigEth15MinIntervalTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalTxMulticastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalTxBroadcastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalTxBroadcastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalTxBroadcastFrames = _AdGenTA8xxGigEth15MinIntervalTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 16),
    _AdGenTA8xxGigEth15MinIntervalTxBroadcastFrames_Type()
)
adGenTA8xxGigEth15MinIntervalTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalTxBroadcastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalTxUnicastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalTxUnicastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalTxUnicastFrames = _AdGenTA8xxGigEth15MinIntervalTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 17),
    _AdGenTA8xxGigEth15MinIntervalTxUnicastFrames_Type()
)
adGenTA8xxGigEth15MinIntervalTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalTxUnicastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxJabbers_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxJabbers_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxJabbers = _AdGenTA8xxGigEth15MinIntervalRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 18),
    _AdGenTA8xxGigEth15MinIntervalRxJabbers_Type()
)
adGenTA8xxGigEth15MinIntervalRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxJabbers.setStatus("current")
_AdGenTA8xxGigEth15MinIntervalRxFragments_Type = Gauge32
_AdGenTA8xxGigEth15MinIntervalRxFragments_Object = MibTableColumn
adGenTA8xxGigEth15MinIntervalRxFragments = _AdGenTA8xxGigEth15MinIntervalRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 3, 1, 19),
    _AdGenTA8xxGigEth15MinIntervalRxFragments_Type()
)
adGenTA8xxGigEth15MinIntervalRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinIntervalRxFragments.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentTable_Object = MibTable
adGenTA8xxGigEth24HrCurrentTable = _AdGenTA8xxGigEth24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4)
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentTable.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentEntry_Object = MibTableRow
adGenTA8xxGigEth24HrCurrentEntry = _AdGenTA8xxGigEth24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1)
)
adGenTA8xxGigEth24HrCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentEntry.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentTxBytes_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentTxBytes_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentTxBytes = _AdGenTA8xxGigEth24HrCurrentTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 1),
    _AdGenTA8xxGigEth24HrCurrentTxBytes_Type()
)
adGenTA8xxGigEth24HrCurrentTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentTxBytes.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentTxFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentTxFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentTxFrames = _AdGenTA8xxGigEth24HrCurrentTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 2),
    _AdGenTA8xxGigEth24HrCurrentTxFrames_Type()
)
adGenTA8xxGigEth24HrCurrentTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentTxFrames.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxBytes_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxBytes_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxBytes = _AdGenTA8xxGigEth24HrCurrentRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 3),
    _AdGenTA8xxGigEth24HrCurrentRxBytes_Type()
)
adGenTA8xxGigEth24HrCurrentRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxBytes.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxFrames = _AdGenTA8xxGigEth24HrCurrentRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 4),
    _AdGenTA8xxGigEth24HrCurrentRxFrames_Type()
)
adGenTA8xxGigEth24HrCurrentRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxFrames.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxGoodBytes_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxGoodBytes_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxGoodBytes = _AdGenTA8xxGigEth24HrCurrentRxGoodBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 5),
    _AdGenTA8xxGigEth24HrCurrentRxGoodBytes_Type()
)
adGenTA8xxGigEth24HrCurrentRxGoodBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxGoodBytes.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxGoodFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxGoodFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxGoodFrames = _AdGenTA8xxGigEth24HrCurrentRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 6),
    _AdGenTA8xxGigEth24HrCurrentRxGoodFrames_Type()
)
adGenTA8xxGigEth24HrCurrentRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxGoodFrames.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxFCSErrors_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxFCSErrors_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxFCSErrors = _AdGenTA8xxGigEth24HrCurrentRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 7),
    _AdGenTA8xxGigEth24HrCurrentRxFCSErrors_Type()
)
adGenTA8xxGigEth24HrCurrentRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxFCSErrors.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxDroppedFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxDroppedFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxDroppedFrames = _AdGenTA8xxGigEth24HrCurrentRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 8),
    _AdGenTA8xxGigEth24HrCurrentRxDroppedFrames_Type()
)
adGenTA8xxGigEth24HrCurrentRxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxDroppedFrames.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxFramesTooBig_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxFramesTooBig_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxFramesTooBig = _AdGenTA8xxGigEth24HrCurrentRxFramesTooBig_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 9),
    _AdGenTA8xxGigEth24HrCurrentRxFramesTooBig_Type()
)
adGenTA8xxGigEth24HrCurrentRxFramesTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxFramesTooBig.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxFramesTooSmall_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxFramesTooSmall_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxFramesTooSmall = _AdGenTA8xxGigEth24HrCurrentRxFramesTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 10),
    _AdGenTA8xxGigEth24HrCurrentRxFramesTooSmall_Type()
)
adGenTA8xxGigEth24HrCurrentRxFramesTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxFramesTooSmall.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxMulticastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxMulticastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxMulticastFrames = _AdGenTA8xxGigEth24HrCurrentRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 11),
    _AdGenTA8xxGigEth24HrCurrentRxMulticastFrames_Type()
)
adGenTA8xxGigEth24HrCurrentRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxMulticastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxBroadcastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxBroadcastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxBroadcastFrames = _AdGenTA8xxGigEth24HrCurrentRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 12),
    _AdGenTA8xxGigEth24HrCurrentRxBroadcastFrames_Type()
)
adGenTA8xxGigEth24HrCurrentRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxBroadcastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxUnicastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxUnicastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxUnicastFrames = _AdGenTA8xxGigEth24HrCurrentRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 13),
    _AdGenTA8xxGigEth24HrCurrentRxUnicastFrames_Type()
)
adGenTA8xxGigEth24HrCurrentRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxUnicastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentTxMulticastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentTxMulticastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentTxMulticastFrames = _AdGenTA8xxGigEth24HrCurrentTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 14),
    _AdGenTA8xxGigEth24HrCurrentTxMulticastFrames_Type()
)
adGenTA8xxGigEth24HrCurrentTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentTxMulticastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentTxBroadcastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentTxBroadcastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentTxBroadcastFrames = _AdGenTA8xxGigEth24HrCurrentTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 15),
    _AdGenTA8xxGigEth24HrCurrentTxBroadcastFrames_Type()
)
adGenTA8xxGigEth24HrCurrentTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentTxBroadcastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentTxUnicastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentTxUnicastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentTxUnicastFrames = _AdGenTA8xxGigEth24HrCurrentTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 16),
    _AdGenTA8xxGigEth24HrCurrentTxUnicastFrames_Type()
)
adGenTA8xxGigEth24HrCurrentTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentTxUnicastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxJabbers_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxJabbers_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxJabbers = _AdGenTA8xxGigEth24HrCurrentRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 17),
    _AdGenTA8xxGigEth24HrCurrentRxJabbers_Type()
)
adGenTA8xxGigEth24HrCurrentRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxJabbers.setStatus("current")
_AdGenTA8xxGigEth24HrCurrentRxFragments_Type = Gauge32
_AdGenTA8xxGigEth24HrCurrentRxFragments_Object = MibTableColumn
adGenTA8xxGigEth24HrCurrentRxFragments = _AdGenTA8xxGigEth24HrCurrentRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 4, 1, 18),
    _AdGenTA8xxGigEth24HrCurrentRxFragments_Type()
)
adGenTA8xxGigEth24HrCurrentRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrCurrentRxFragments.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalTable_Object = MibTable
adGenTA8xxGigEth24HrIntervalTable = _AdGenTA8xxGigEth24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5)
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalTable.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalEntry_Object = MibTableRow
adGenTA8xxGigEth24HrIntervalEntry = _AdGenTA8xxGigEth24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1)
)
adGenTA8xxGigEth24HrIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalEntry.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalNumber_Type = Integer32
_AdGenTA8xxGigEth24HrIntervalNumber_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalNumber = _AdGenTA8xxGigEth24HrIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 1),
    _AdGenTA8xxGigEth24HrIntervalNumber_Type()
)
adGenTA8xxGigEth24HrIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalNumber.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalTxBytes_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalTxBytes_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalTxBytes = _AdGenTA8xxGigEth24HrIntervalTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 2),
    _AdGenTA8xxGigEth24HrIntervalTxBytes_Type()
)
adGenTA8xxGigEth24HrIntervalTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalTxBytes.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalTxFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalTxFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalTxFrames = _AdGenTA8xxGigEth24HrIntervalTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 3),
    _AdGenTA8xxGigEth24HrIntervalTxFrames_Type()
)
adGenTA8xxGigEth24HrIntervalTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalTxFrames.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxBytes_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxBytes_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxBytes = _AdGenTA8xxGigEth24HrIntervalRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 4),
    _AdGenTA8xxGigEth24HrIntervalRxBytes_Type()
)
adGenTA8xxGigEth24HrIntervalRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxBytes.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxFrames = _AdGenTA8xxGigEth24HrIntervalRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 5),
    _AdGenTA8xxGigEth24HrIntervalRxFrames_Type()
)
adGenTA8xxGigEth24HrIntervalRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxFrames.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxGoodBytes_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxGoodBytes_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxGoodBytes = _AdGenTA8xxGigEth24HrIntervalRxGoodBytes_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 6),
    _AdGenTA8xxGigEth24HrIntervalRxGoodBytes_Type()
)
adGenTA8xxGigEth24HrIntervalRxGoodBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxGoodBytes.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxGoodFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxGoodFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxGoodFrames = _AdGenTA8xxGigEth24HrIntervalRxGoodFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 7),
    _AdGenTA8xxGigEth24HrIntervalRxGoodFrames_Type()
)
adGenTA8xxGigEth24HrIntervalRxGoodFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxGoodFrames.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxFCSErrors_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxFCSErrors_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxFCSErrors = _AdGenTA8xxGigEth24HrIntervalRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 8),
    _AdGenTA8xxGigEth24HrIntervalRxFCSErrors_Type()
)
adGenTA8xxGigEth24HrIntervalRxFCSErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxFCSErrors.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxDroppedFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxDroppedFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxDroppedFrames = _AdGenTA8xxGigEth24HrIntervalRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 9),
    _AdGenTA8xxGigEth24HrIntervalRxDroppedFrames_Type()
)
adGenTA8xxGigEth24HrIntervalRxDroppedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxDroppedFrames.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxFramesTooBig_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxFramesTooBig_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxFramesTooBig = _AdGenTA8xxGigEth24HrIntervalRxFramesTooBig_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 10),
    _AdGenTA8xxGigEth24HrIntervalRxFramesTooBig_Type()
)
adGenTA8xxGigEth24HrIntervalRxFramesTooBig.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxFramesTooBig.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxFramesTooSmall_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxFramesTooSmall_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxFramesTooSmall = _AdGenTA8xxGigEth24HrIntervalRxFramesTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 11),
    _AdGenTA8xxGigEth24HrIntervalRxFramesTooSmall_Type()
)
adGenTA8xxGigEth24HrIntervalRxFramesTooSmall.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxFramesTooSmall.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxMulticastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxMulticastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxMulticastFrames = _AdGenTA8xxGigEth24HrIntervalRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 12),
    _AdGenTA8xxGigEth24HrIntervalRxMulticastFrames_Type()
)
adGenTA8xxGigEth24HrIntervalRxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxMulticastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxBroadcastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxBroadcastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxBroadcastFrames = _AdGenTA8xxGigEth24HrIntervalRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 13),
    _AdGenTA8xxGigEth24HrIntervalRxBroadcastFrames_Type()
)
adGenTA8xxGigEth24HrIntervalRxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxBroadcastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxUnicastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxUnicastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxUnicastFrames = _AdGenTA8xxGigEth24HrIntervalRxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 14),
    _AdGenTA8xxGigEth24HrIntervalRxUnicastFrames_Type()
)
adGenTA8xxGigEth24HrIntervalRxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxUnicastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalTxMulticastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalTxMulticastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalTxMulticastFrames = _AdGenTA8xxGigEth24HrIntervalTxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 15),
    _AdGenTA8xxGigEth24HrIntervalTxMulticastFrames_Type()
)
adGenTA8xxGigEth24HrIntervalTxMulticastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalTxMulticastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalTxBroadcastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalTxBroadcastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalTxBroadcastFrames = _AdGenTA8xxGigEth24HrIntervalTxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 16),
    _AdGenTA8xxGigEth24HrIntervalTxBroadcastFrames_Type()
)
adGenTA8xxGigEth24HrIntervalTxBroadcastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalTxBroadcastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalTxUnicastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalTxUnicastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalTxUnicastFrames = _AdGenTA8xxGigEth24HrIntervalTxUnicastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 17),
    _AdGenTA8xxGigEth24HrIntervalTxUnicastFrames_Type()
)
adGenTA8xxGigEth24HrIntervalTxUnicastFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalTxUnicastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxJabbers_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxJabbers_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxJabbers = _AdGenTA8xxGigEth24HrIntervalRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 18),
    _AdGenTA8xxGigEth24HrIntervalRxJabbers_Type()
)
adGenTA8xxGigEth24HrIntervalRxJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxJabbers.setStatus("current")
_AdGenTA8xxGigEth24HrIntervalRxFragments_Type = Gauge32
_AdGenTA8xxGigEth24HrIntervalRxFragments_Object = MibTableColumn
adGenTA8xxGigEth24HrIntervalRxFragments = _AdGenTA8xxGigEth24HrIntervalRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 5, 1, 19),
    _AdGenTA8xxGigEth24HrIntervalRxFragments_Type()
)
adGenTA8xxGigEth24HrIntervalRxFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrIntervalRxFragments.setStatus("current")
_AdGenTA8xxGigEthPerfResetTable_Object = MibTable
adGenTA8xxGigEthPerfResetTable = _AdGenTA8xxGigEthPerfResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 6)
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEthPerfResetTable.setStatus("current")
_AdGenTA8xxGigEthPerfResetEntry_Object = MibTableRow
adGenTA8xxGigEthPerfResetEntry = _AdGenTA8xxGigEthPerfResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 6, 1)
)
adGenTA8xxGigEthPerfResetEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEthPerfResetEntry.setStatus("current")


class _AdGenTA8xxGigEthPerfReset_Type(Integer32):
    """Custom type adGenTA8xxGigEthPerfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethPerfRst", 1)
    )


_AdGenTA8xxGigEthPerfReset_Type.__name__ = "Integer32"
_AdGenTA8xxGigEthPerfReset_Object = MibTableColumn
adGenTA8xxGigEthPerfReset = _AdGenTA8xxGigEthPerfReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 3, 6, 1, 1),
    _AdGenTA8xxGigEthPerfReset_Type()
)
adGenTA8xxGigEthPerfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEthPerfReset.setStatus("current")
_AdGenTA8xx10100EthPerfThresholds_ObjectIdentity = ObjectIdentity
adGenTA8xx10100EthPerfThresholds = _AdGenTA8xx10100EthPerfThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4)
)
_AdGenTA8xx10100Eth15MinThreshTable_Object = MibTable
adGenTA8xx10100Eth15MinThreshTable = _AdGenTA8xx10100Eth15MinThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1)
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshTable.setStatus("current")
_AdGenTA8xx10100Eth15MinThreshEntry_Object = MibTableRow
adGenTA8xx10100Eth15MinThreshEntry = _AdGenTA8xx10100Eth15MinThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1, 1)
)
adGenTA8xx10100Eth15MinThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshEntry.setStatus("current")
_AdGenTA8xx10100Eth15MinThreshRxCRCAlignErrs_Type = Gauge32
_AdGenTA8xx10100Eth15MinThreshRxCRCAlignErrs_Object = MibTableColumn
adGenTA8xx10100Eth15MinThreshRxCRCAlignErrs = _AdGenTA8xx10100Eth15MinThreshRxCRCAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1, 1, 1),
    _AdGenTA8xx10100Eth15MinThreshRxCRCAlignErrs_Type()
)
adGenTA8xx10100Eth15MinThreshRxCRCAlignErrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshRxCRCAlignErrs.setStatus("current")
_AdGenTA8xx10100Eth15MinThreshRxUndersizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinThreshRxUndersizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinThreshRxUndersizeFrames = _AdGenTA8xx10100Eth15MinThreshRxUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1, 1, 2),
    _AdGenTA8xx10100Eth15MinThreshRxUndersizeFrames_Type()
)
adGenTA8xx10100Eth15MinThreshRxUndersizeFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshRxUndersizeFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinThreshRxOversizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinThreshRxOversizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinThreshRxOversizeFrames = _AdGenTA8xx10100Eth15MinThreshRxOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1, 1, 3),
    _AdGenTA8xx10100Eth15MinThreshRxOversizeFrames_Type()
)
adGenTA8xx10100Eth15MinThreshRxOversizeFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshRxOversizeFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinThreshRxCollisions_Type = Gauge32
_AdGenTA8xx10100Eth15MinThreshRxCollisions_Object = MibTableColumn
adGenTA8xx10100Eth15MinThreshRxCollisions = _AdGenTA8xx10100Eth15MinThreshRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1, 1, 4),
    _AdGenTA8xx10100Eth15MinThreshRxCollisions_Type()
)
adGenTA8xx10100Eth15MinThreshRxCollisions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshRxCollisions.setStatus("current")
_AdGenTA8xx10100Eth15MinThreshRxDiscardedFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinThreshRxDiscardedFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinThreshRxDiscardedFrames = _AdGenTA8xx10100Eth15MinThreshRxDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1, 1, 5),
    _AdGenTA8xx10100Eth15MinThreshRxDiscardedFrames_Type()
)
adGenTA8xx10100Eth15MinThreshRxDiscardedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshRxDiscardedFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinThreshRxMulticastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinThreshRxMulticastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinThreshRxMulticastFrames = _AdGenTA8xx10100Eth15MinThreshRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1, 1, 6),
    _AdGenTA8xx10100Eth15MinThreshRxMulticastFrames_Type()
)
adGenTA8xx10100Eth15MinThreshRxMulticastFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshRxMulticastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinThreshRxBroadcastFrames_Type = Gauge32
_AdGenTA8xx10100Eth15MinThreshRxBroadcastFrames_Object = MibTableColumn
adGenTA8xx10100Eth15MinThreshRxBroadcastFrames = _AdGenTA8xx10100Eth15MinThreshRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1, 1, 7),
    _AdGenTA8xx10100Eth15MinThreshRxBroadcastFrames_Type()
)
adGenTA8xx10100Eth15MinThreshRxBroadcastFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshRxBroadcastFrames.setStatus("current")
_AdGenTA8xx10100Eth15MinThreshRxJabbers_Type = Gauge32
_AdGenTA8xx10100Eth15MinThreshRxJabbers_Object = MibTableColumn
adGenTA8xx10100Eth15MinThreshRxJabbers = _AdGenTA8xx10100Eth15MinThreshRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1, 1, 8),
    _AdGenTA8xx10100Eth15MinThreshRxJabbers_Type()
)
adGenTA8xx10100Eth15MinThreshRxJabbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshRxJabbers.setStatus("current")
_AdGenTA8xx10100Eth15MinThreshRxFragments_Type = Gauge32
_AdGenTA8xx10100Eth15MinThreshRxFragments_Object = MibTableColumn
adGenTA8xx10100Eth15MinThreshRxFragments = _AdGenTA8xx10100Eth15MinThreshRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 1, 1, 9),
    _AdGenTA8xx10100Eth15MinThreshRxFragments_Type()
)
adGenTA8xx10100Eth15MinThreshRxFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth15MinThreshRxFragments.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshTable_Object = MibTable
adGenTA8xx10100Eth24HrThreshTable = _AdGenTA8xx10100Eth24HrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2)
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshTable.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshEntry_Object = MibTableRow
adGenTA8xx10100Eth24HrThreshEntry = _AdGenTA8xx10100Eth24HrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2, 1)
)
adGenTA8xx10100Eth24HrThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshEntry.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshRxCRCAlignErrs_Type = Gauge32
_AdGenTA8xx10100Eth24HrThreshRxCRCAlignErrs_Object = MibTableColumn
adGenTA8xx10100Eth24HrThreshRxCRCAlignErrs = _AdGenTA8xx10100Eth24HrThreshRxCRCAlignErrs_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2, 1, 1),
    _AdGenTA8xx10100Eth24HrThreshRxCRCAlignErrs_Type()
)
adGenTA8xx10100Eth24HrThreshRxCRCAlignErrs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshRxCRCAlignErrs.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshRxUndersizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrThreshRxUndersizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrThreshRxUndersizeFrames = _AdGenTA8xx10100Eth24HrThreshRxUndersizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2, 1, 2),
    _AdGenTA8xx10100Eth24HrThreshRxUndersizeFrames_Type()
)
adGenTA8xx10100Eth24HrThreshRxUndersizeFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshRxUndersizeFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshRxOversizeFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrThreshRxOversizeFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrThreshRxOversizeFrames = _AdGenTA8xx10100Eth24HrThreshRxOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2, 1, 3),
    _AdGenTA8xx10100Eth24HrThreshRxOversizeFrames_Type()
)
adGenTA8xx10100Eth24HrThreshRxOversizeFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshRxOversizeFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshRxCollisions_Type = Gauge32
_AdGenTA8xx10100Eth24HrThreshRxCollisions_Object = MibTableColumn
adGenTA8xx10100Eth24HrThreshRxCollisions = _AdGenTA8xx10100Eth24HrThreshRxCollisions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2, 1, 4),
    _AdGenTA8xx10100Eth24HrThreshRxCollisions_Type()
)
adGenTA8xx10100Eth24HrThreshRxCollisions.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshRxCollisions.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshRxDiscardedFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrThreshRxDiscardedFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrThreshRxDiscardedFrames = _AdGenTA8xx10100Eth24HrThreshRxDiscardedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2, 1, 5),
    _AdGenTA8xx10100Eth24HrThreshRxDiscardedFrames_Type()
)
adGenTA8xx10100Eth24HrThreshRxDiscardedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshRxDiscardedFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshRxMulticastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrThreshRxMulticastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrThreshRxMulticastFrames = _AdGenTA8xx10100Eth24HrThreshRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2, 1, 6),
    _AdGenTA8xx10100Eth24HrThreshRxMulticastFrames_Type()
)
adGenTA8xx10100Eth24HrThreshRxMulticastFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshRxMulticastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshRxBroadcastFrames_Type = Gauge32
_AdGenTA8xx10100Eth24HrThreshRxBroadcastFrames_Object = MibTableColumn
adGenTA8xx10100Eth24HrThreshRxBroadcastFrames = _AdGenTA8xx10100Eth24HrThreshRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2, 1, 7),
    _AdGenTA8xx10100Eth24HrThreshRxBroadcastFrames_Type()
)
adGenTA8xx10100Eth24HrThreshRxBroadcastFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshRxBroadcastFrames.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshRxJabbers_Type = Gauge32
_AdGenTA8xx10100Eth24HrThreshRxJabbers_Object = MibTableColumn
adGenTA8xx10100Eth24HrThreshRxJabbers = _AdGenTA8xx10100Eth24HrThreshRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2, 1, 8),
    _AdGenTA8xx10100Eth24HrThreshRxJabbers_Type()
)
adGenTA8xx10100Eth24HrThreshRxJabbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshRxJabbers.setStatus("current")
_AdGenTA8xx10100Eth24HrThreshRxFragments_Type = Gauge32
_AdGenTA8xx10100Eth24HrThreshRxFragments_Object = MibTableColumn
adGenTA8xx10100Eth24HrThreshRxFragments = _AdGenTA8xx10100Eth24HrThreshRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 4, 2, 1, 9),
    _AdGenTA8xx10100Eth24HrThreshRxFragments_Type()
)
adGenTA8xx10100Eth24HrThreshRxFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xx10100Eth24HrThreshRxFragments.setStatus("current")
_AdGenTA8xxGigEthPerfThresholds_ObjectIdentity = ObjectIdentity
adGenTA8xxGigEthPerfThresholds = _AdGenTA8xxGigEthPerfThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5)
)
_AdGenTA8xxGigEth15MinThreshTable_Object = MibTable
adGenTA8xxGigEth15MinThreshTable = _AdGenTA8xxGigEth15MinThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 1)
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinThreshTable.setStatus("current")
_AdGenTA8xxGigEth15MinThreshEntry_Object = MibTableRow
adGenTA8xxGigEth15MinThreshEntry = _AdGenTA8xxGigEth15MinThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 1, 1)
)
adGenTA8xxGigEth15MinThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinThreshEntry.setStatus("current")
_AdGenTA8xxGigEth15MinThreshRxFCSErrors_Type = Gauge32
_AdGenTA8xxGigEth15MinThreshRxFCSErrors_Object = MibTableColumn
adGenTA8xxGigEth15MinThreshRxFCSErrors = _AdGenTA8xxGigEth15MinThreshRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 1, 1, 1),
    _AdGenTA8xxGigEth15MinThreshRxFCSErrors_Type()
)
adGenTA8xxGigEth15MinThreshRxFCSErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinThreshRxFCSErrors.setStatus("current")
_AdGenTA8xxGigEth15MinThreshRxDroppedFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinThreshRxDroppedFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinThreshRxDroppedFrames = _AdGenTA8xxGigEth15MinThreshRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 1, 1, 2),
    _AdGenTA8xxGigEth15MinThreshRxDroppedFrames_Type()
)
adGenTA8xxGigEth15MinThreshRxDroppedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinThreshRxDroppedFrames.setStatus("current")
_AdGenTA8xxGigEth15MinThreshRxFramesTooBig_Type = Gauge32
_AdGenTA8xxGigEth15MinThreshRxFramesTooBig_Object = MibTableColumn
adGenTA8xxGigEth15MinThreshRxFramesTooBig = _AdGenTA8xxGigEth15MinThreshRxFramesTooBig_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 1, 1, 3),
    _AdGenTA8xxGigEth15MinThreshRxFramesTooBig_Type()
)
adGenTA8xxGigEth15MinThreshRxFramesTooBig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinThreshRxFramesTooBig.setStatus("current")
_AdGenTA8xxGigEth15MinThreshRxFramesTooSmall_Type = Gauge32
_AdGenTA8xxGigEth15MinThreshRxFramesTooSmall_Object = MibTableColumn
adGenTA8xxGigEth15MinThreshRxFramesTooSmall = _AdGenTA8xxGigEth15MinThreshRxFramesTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 1, 1, 4),
    _AdGenTA8xxGigEth15MinThreshRxFramesTooSmall_Type()
)
adGenTA8xxGigEth15MinThreshRxFramesTooSmall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinThreshRxFramesTooSmall.setStatus("current")
_AdGenTA8xxGigEth15MinThreshRxMulticastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinThreshRxMulticastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinThreshRxMulticastFrames = _AdGenTA8xxGigEth15MinThreshRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 1, 1, 5),
    _AdGenTA8xxGigEth15MinThreshRxMulticastFrames_Type()
)
adGenTA8xxGigEth15MinThreshRxMulticastFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinThreshRxMulticastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinThreshRxBroadcastFrames_Type = Gauge32
_AdGenTA8xxGigEth15MinThreshRxBroadcastFrames_Object = MibTableColumn
adGenTA8xxGigEth15MinThreshRxBroadcastFrames = _AdGenTA8xxGigEth15MinThreshRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 1, 1, 6),
    _AdGenTA8xxGigEth15MinThreshRxBroadcastFrames_Type()
)
adGenTA8xxGigEth15MinThreshRxBroadcastFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinThreshRxBroadcastFrames.setStatus("current")
_AdGenTA8xxGigEth15MinThreshRxJabbers_Type = Gauge32
_AdGenTA8xxGigEth15MinThreshRxJabbers_Object = MibTableColumn
adGenTA8xxGigEth15MinThreshRxJabbers = _AdGenTA8xxGigEth15MinThreshRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 1, 1, 7),
    _AdGenTA8xxGigEth15MinThreshRxJabbers_Type()
)
adGenTA8xxGigEth15MinThreshRxJabbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinThreshRxJabbers.setStatus("current")
_AdGenTA8xxGigEth15MinThreshRxFragments_Type = Gauge32
_AdGenTA8xxGigEth15MinThreshRxFragments_Object = MibTableColumn
adGenTA8xxGigEth15MinThreshRxFragments = _AdGenTA8xxGigEth15MinThreshRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 1, 1, 8),
    _AdGenTA8xxGigEth15MinThreshRxFragments_Type()
)
adGenTA8xxGigEth15MinThreshRxFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth15MinThreshRxFragments.setStatus("current")
_AdGenTA8xxGigEth24HrThreshTable_Object = MibTable
adGenTA8xxGigEth24HrThreshTable = _AdGenTA8xxGigEth24HrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 2)
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrThreshTable.setStatus("current")
_AdGenTA8xxGigEth24HrThreshEntry_Object = MibTableRow
adGenTA8xxGigEth24HrThreshEntry = _AdGenTA8xxGigEth24HrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 2, 1)
)
adGenTA8xxGigEth24HrThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrThreshEntry.setStatus("current")
_AdGenTA8xxGigEth24HrThreshRxFCSErrors_Type = Gauge32
_AdGenTA8xxGigEth24HrThreshRxFCSErrors_Object = MibTableColumn
adGenTA8xxGigEth24HrThreshRxFCSErrors = _AdGenTA8xxGigEth24HrThreshRxFCSErrors_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 2, 1, 1),
    _AdGenTA8xxGigEth24HrThreshRxFCSErrors_Type()
)
adGenTA8xxGigEth24HrThreshRxFCSErrors.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrThreshRxFCSErrors.setStatus("current")
_AdGenTA8xxGigEth24HrThreshRxDroppedFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrThreshRxDroppedFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrThreshRxDroppedFrames = _AdGenTA8xxGigEth24HrThreshRxDroppedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 2, 1, 2),
    _AdGenTA8xxGigEth24HrThreshRxDroppedFrames_Type()
)
adGenTA8xxGigEth24HrThreshRxDroppedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrThreshRxDroppedFrames.setStatus("current")
_AdGenTA8xxGigEth24HrThreshRxFramesTooBig_Type = Gauge32
_AdGenTA8xxGigEth24HrThreshRxFramesTooBig_Object = MibTableColumn
adGenTA8xxGigEth24HrThreshRxFramesTooBig = _AdGenTA8xxGigEth24HrThreshRxFramesTooBig_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 2, 1, 3),
    _AdGenTA8xxGigEth24HrThreshRxFramesTooBig_Type()
)
adGenTA8xxGigEth24HrThreshRxFramesTooBig.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrThreshRxFramesTooBig.setStatus("current")
_AdGenTA8xxGigEth24HrThreshRxFramesTooSmall_Type = Gauge32
_AdGenTA8xxGigEth24HrThreshRxFramesTooSmall_Object = MibTableColumn
adGenTA8xxGigEth24HrThreshRxFramesTooSmall = _AdGenTA8xxGigEth24HrThreshRxFramesTooSmall_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 2, 1, 4),
    _AdGenTA8xxGigEth24HrThreshRxFramesTooSmall_Type()
)
adGenTA8xxGigEth24HrThreshRxFramesTooSmall.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrThreshRxFramesTooSmall.setStatus("current")
_AdGenTA8xxGigEth24HrThreshRxMulticastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrThreshRxMulticastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrThreshRxMulticastFrames = _AdGenTA8xxGigEth24HrThreshRxMulticastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 2, 1, 5),
    _AdGenTA8xxGigEth24HrThreshRxMulticastFrames_Type()
)
adGenTA8xxGigEth24HrThreshRxMulticastFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrThreshRxMulticastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrThreshRxBroadcastFrames_Type = Gauge32
_AdGenTA8xxGigEth24HrThreshRxBroadcastFrames_Object = MibTableColumn
adGenTA8xxGigEth24HrThreshRxBroadcastFrames = _AdGenTA8xxGigEth24HrThreshRxBroadcastFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 2, 1, 6),
    _AdGenTA8xxGigEth24HrThreshRxBroadcastFrames_Type()
)
adGenTA8xxGigEth24HrThreshRxBroadcastFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrThreshRxBroadcastFrames.setStatus("current")
_AdGenTA8xxGigEth24HrThreshRxJabbers_Type = Gauge32
_AdGenTA8xxGigEth24HrThreshRxJabbers_Object = MibTableColumn
adGenTA8xxGigEth24HrThreshRxJabbers = _AdGenTA8xxGigEth24HrThreshRxJabbers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 2, 1, 7),
    _AdGenTA8xxGigEth24HrThreshRxJabbers_Type()
)
adGenTA8xxGigEth24HrThreshRxJabbers.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrThreshRxJabbers.setStatus("current")
_AdGenTA8xxGigEth24HrThreshRxFragments_Type = Gauge32
_AdGenTA8xxGigEth24HrThreshRxFragments_Object = MibTableColumn
adGenTA8xxGigEth24HrThreshRxFragments = _AdGenTA8xxGigEth24HrThreshRxFragments_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 4, 5, 2, 1, 8),
    _AdGenTA8xxGigEth24HrThreshRxFragments_Type()
)
adGenTA8xxGigEth24HrThreshRxFragments.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxGigEth24HrThreshRxFragments.setStatus("current")
_AdGenTA8xxTest_ObjectIdentity = ObjectIdentity
adGenTA8xxTest = _AdGenTA8xxTest_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5)
)
_AdGenTA8xxTstScalars_ObjectIdentity = ObjectIdentity
adGenTA8xxTstScalars = _AdGenTA8xxTstScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 1)
)


class _AdGenTA8xxResetTests_Type(Integer32):
    """Custom type adGenTA8xxResetTests based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("resetTests", 1)
    )


_AdGenTA8xxResetTests_Type.__name__ = "Integer32"
_AdGenTA8xxResetTests_Object = MibScalar
adGenTA8xxResetTests = _AdGenTA8xxResetTests_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 1, 1),
    _AdGenTA8xxResetTests_Type()
)
adGenTA8xxResetTests.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxResetTests.setStatus("current")


class _AdGenTA8xxTestTimeout_Type(Integer32):
    """Custom type adGenTA8xxTestTimeout based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("oneMin", 2),
          ("fiveMin", 3),
          ("tenMin", 4),
          ("fifteenMin", 5),
          ("thirtyMin", 6),
          ("fortyfiveMin", 7),
          ("sixtyMin", 8))
    )


_AdGenTA8xxTestTimeout_Type.__name__ = "Integer32"
_AdGenTA8xxTestTimeout_Object = MibScalar
adGenTA8xxTestTimeout = _AdGenTA8xxTestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 1, 2),
    _AdGenTA8xxTestTimeout_Type()
)
adGenTA8xxTestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTestTimeout.setStatus("current")


class _AdGenTA8xxRelayTest_Type(Integer32):
    """Custom type adGenTA8xxRelayTest based on Integer32"""
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


_AdGenTA8xxRelayTest_Type.__name__ = "Integer32"
_AdGenTA8xxRelayTest_Object = MibScalar
adGenTA8xxRelayTest = _AdGenTA8xxRelayTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 1, 3),
    _AdGenTA8xxRelayTest_Type()
)
adGenTA8xxRelayTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxRelayTest.setStatus("current")


class _AdGenTA8xxTestCriticalRelay_Type(Integer32):
    """Custom type adGenTA8xxTestCriticalRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenTA8xxTestCriticalRelay_Type.__name__ = "Integer32"
_AdGenTA8xxTestCriticalRelay_Object = MibScalar
adGenTA8xxTestCriticalRelay = _AdGenTA8xxTestCriticalRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 1, 4),
    _AdGenTA8xxTestCriticalRelay_Type()
)
adGenTA8xxTestCriticalRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTestCriticalRelay.setStatus("current")


class _AdGenTA8xxTestMajorRelay_Type(Integer32):
    """Custom type adGenTA8xxTestMajorRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenTA8xxTestMajorRelay_Type.__name__ = "Integer32"
_AdGenTA8xxTestMajorRelay_Object = MibScalar
adGenTA8xxTestMajorRelay = _AdGenTA8xxTestMajorRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 1, 5),
    _AdGenTA8xxTestMajorRelay_Type()
)
adGenTA8xxTestMajorRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTestMajorRelay.setStatus("current")


class _AdGenTA8xxTestMinorRelay_Type(Integer32):
    """Custom type adGenTA8xxTestMinorRelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inactive", 1),
          ("active", 2))
    )


_AdGenTA8xxTestMinorRelay_Type.__name__ = "Integer32"
_AdGenTA8xxTestMinorRelay_Object = MibScalar
adGenTA8xxTestMinorRelay = _AdGenTA8xxTestMinorRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 1, 6),
    _AdGenTA8xxTestMinorRelay_Type()
)
adGenTA8xxTestMinorRelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTestMinorRelay.setStatus("current")
_AdGenTA8xxTstBertPrvTable_Object = MibTable
adGenTA8xxTstBertPrvTable = _AdGenTA8xxTstBertPrvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 2)
)
if mibBuilder.loadTexts:
    adGenTA8xxTstBertPrvTable.setStatus("current")
_AdGenTA8xxTstBertPrvEntry_Object = MibTableRow
adGenTA8xxTstBertPrvEntry = _AdGenTA8xxTstBertPrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 2, 1)
)
adGenTA8xxTstBertPrvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxTstBertPrvEntry.setStatus("current")


class _AdGenTA8xxTstBertStartAndStop_Type(Integer32):
    """Custom type adGenTA8xxTstBertStartAndStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("stopBert", 1),
          ("startBert", 2))
    )


_AdGenTA8xxTstBertStartAndStop_Type.__name__ = "Integer32"
_AdGenTA8xxTstBertStartAndStop_Object = MibTableColumn
adGenTA8xxTstBertStartAndStop = _AdGenTA8xxTstBertStartAndStop_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 2, 1, 1),
    _AdGenTA8xxTstBertStartAndStop_Type()
)
adGenTA8xxTstBertStartAndStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertStartAndStop.setStatus("current")


class _AdGenTA8xxTstBertResetStatistics_Type(Integer32):
    """Custom type adGenTA8xxTstBertResetStatistics based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_AdGenTA8xxTstBertResetStatistics_Type.__name__ = "Integer32"
_AdGenTA8xxTstBertResetStatistics_Object = MibTableColumn
adGenTA8xxTstBertResetStatistics = _AdGenTA8xxTstBertResetStatistics_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 2, 1, 2),
    _AdGenTA8xxTstBertResetStatistics_Type()
)
adGenTA8xxTstBertResetStatistics.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertResetStatistics.setStatus("current")


class _AdGenTA8xxTstBertPattern_Type(Integer32):
    """Custom type adGenTA8xxTstBertPattern based on Integer32"""
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
        *(("bertTwoToFifteenMinusOne", 1),
          ("bertTwoToTwentyMinusOne", 2),
          ("bertAllOnes", 3),
          ("bertAllZeroes", 4),
          ("bertTwoToTwentyThreeMinusOne", 5))
    )


_AdGenTA8xxTstBertPattern_Type.__name__ = "Integer32"
_AdGenTA8xxTstBertPattern_Object = MibTableColumn
adGenTA8xxTstBertPattern = _AdGenTA8xxTstBertPattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 2, 1, 3),
    _AdGenTA8xxTstBertPattern_Type()
)
adGenTA8xxTstBertPattern.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertPattern.setStatus("current")


class _AdGenTA8xxTstBertPatternPolarity_Type(Integer32):
    """Custom type adGenTA8xxTstBertPatternPolarity based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("inverted", 2))
    )


_AdGenTA8xxTstBertPatternPolarity_Type.__name__ = "Integer32"
_AdGenTA8xxTstBertPatternPolarity_Object = MibTableColumn
adGenTA8xxTstBertPatternPolarity = _AdGenTA8xxTstBertPatternPolarity_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 2, 1, 4),
    _AdGenTA8xxTstBertPatternPolarity_Type()
)
adGenTA8xxTstBertPatternPolarity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertPatternPolarity.setStatus("current")


class _AdGenTA8xxTstBertErrorInject_Type(Integer32):
    """Custom type adGenTA8xxTstBertErrorInject based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("inject", 1)
    )


_AdGenTA8xxTstBertErrorInject_Type.__name__ = "Integer32"
_AdGenTA8xxTstBertErrorInject_Object = MibTableColumn
adGenTA8xxTstBertErrorInject = _AdGenTA8xxTstBertErrorInject_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 2, 1, 5),
    _AdGenTA8xxTstBertErrorInject_Type()
)
adGenTA8xxTstBertErrorInject.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertErrorInject.setStatus("current")
_AdGenTA8xxTstBertStatTable_Object = MibTable
adGenTA8xxTstBertStatTable = _AdGenTA8xxTstBertStatTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 3)
)
if mibBuilder.loadTexts:
    adGenTA8xxTstBertStatTable.setStatus("current")
_AdGenTA8xxTstBertStatEntry_Object = MibTableRow
adGenTA8xxTstBertStatEntry = _AdGenTA8xxTstBertStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 3, 1)
)
adGenTA8xxTstBertStatEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxTstBertStatEntry.setStatus("current")


class _AdGenTA8xxTstBertStatus_Type(Integer32):
    """Custom type adGenTA8xxTstBertStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabledPatternSync", 2),
          ("enabledNoPatternSync", 3))
    )


_AdGenTA8xxTstBertStatus_Type.__name__ = "Integer32"
_AdGenTA8xxTstBertStatus_Object = MibTableColumn
adGenTA8xxTstBertStatus = _AdGenTA8xxTstBertStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 3, 1, 1),
    _AdGenTA8xxTstBertStatus_Type()
)
adGenTA8xxTstBertStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertStatus.setStatus("current")
_AdGenTA8xxTstBertBER_Type = DisplayString
_AdGenTA8xxTstBertBER_Object = MibTableColumn
adGenTA8xxTstBertBER = _AdGenTA8xxTstBertBER_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 3, 1, 2),
    _AdGenTA8xxTstBertBER_Type()
)
adGenTA8xxTstBertBER.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertBER.setStatus("current")
_AdGenTA8xxTstBertErrorCount_Type = Gauge32
_AdGenTA8xxTstBertErrorCount_Object = MibTableColumn
adGenTA8xxTstBertErrorCount = _AdGenTA8xxTstBertErrorCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 3, 1, 3),
    _AdGenTA8xxTstBertErrorCount_Type()
)
adGenTA8xxTstBertErrorCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertErrorCount.setStatus("current")
_AdGenTA8xxTstBertPattSyncLossCount_Type = Gauge32
_AdGenTA8xxTstBertPattSyncLossCount_Object = MibTableColumn
adGenTA8xxTstBertPattSyncLossCount = _AdGenTA8xxTstBertPattSyncLossCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 3, 1, 4),
    _AdGenTA8xxTstBertPattSyncLossCount_Type()
)
adGenTA8xxTstBertPattSyncLossCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertPattSyncLossCount.setStatus("current")
_AdGenTA8xxTstBertErroredSeconds_Type = Gauge32
_AdGenTA8xxTstBertErroredSeconds_Object = MibTableColumn
adGenTA8xxTstBertErroredSeconds = _AdGenTA8xxTstBertErroredSeconds_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 3, 1, 5),
    _AdGenTA8xxTstBertErroredSeconds_Type()
)
adGenTA8xxTstBertErroredSeconds.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertErroredSeconds.setStatus("current")
_AdGenTA8xxTstBertElapsedTime_Type = DisplayString
_AdGenTA8xxTstBertElapsedTime_Object = MibTableColumn
adGenTA8xxTstBertElapsedTime = _AdGenTA8xxTstBertElapsedTime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 3, 1, 6),
    _AdGenTA8xxTstBertElapsedTime_Type()
)
adGenTA8xxTstBertElapsedTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxTstBertElapsedTime.setStatus("current")
_AdGenTA8xxTstLpbkPrvTable_Object = MibTable
adGenTA8xxTstLpbkPrvTable = _AdGenTA8xxTstLpbkPrvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 4)
)
if mibBuilder.loadTexts:
    adGenTA8xxTstLpbkPrvTable.setStatus("current")
_AdGenTA8xxTstLpbkPrvEntry_Object = MibTableRow
adGenTA8xxTstLpbkPrvEntry = _AdGenTA8xxTstLpbkPrvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 4, 1)
)
adGenTA8xxTstLpbkPrvEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenTA8xxTstLpbkPrvEntry.setStatus("current")


class _AdGenTA8xxTstIncomingLoopbackPatterns_Type(Integer32):
    """Custom type adGenTA8xxTstIncomingLoopbackPatterns based on Integer32"""
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
        *(("disableInband", 1),
          ("enableInband", 2),
          ("disableFDL", 3),
          ("enableFDL", 4))
    )


_AdGenTA8xxTstIncomingLoopbackPatterns_Type.__name__ = "Integer32"
_AdGenTA8xxTstIncomingLoopbackPatterns_Object = MibTableColumn
adGenTA8xxTstIncomingLoopbackPatterns = _AdGenTA8xxTstIncomingLoopbackPatterns_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 4, 1, 1),
    _AdGenTA8xxTstIncomingLoopbackPatterns_Type()
)
adGenTA8xxTstIncomingLoopbackPatterns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTstIncomingLoopbackPatterns.setStatus("current")


class _AdGenTA8xxTstRequestRemoteLoopback_Type(Integer32):
    """Custom type adGenTA8xxTstRequestRemoteLoopback based on Integer32"""
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
        *(("reqInbandLoopUp", 1),
          ("reqInbandLoopDown", 2),
          ("reqFDLLoopUp", 3),
          ("reqFDLLoopDown", 4),
          ("reqFDLUniversalLoopDown", 5),
          ("reqSendNoCode", 6))
    )


_AdGenTA8xxTstRequestRemoteLoopback_Type.__name__ = "Integer32"
_AdGenTA8xxTstRequestRemoteLoopback_Object = MibTableColumn
adGenTA8xxTstRequestRemoteLoopback = _AdGenTA8xxTstRequestRemoteLoopback_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 4, 1, 2),
    _AdGenTA8xxTstRequestRemoteLoopback_Type()
)
adGenTA8xxTstRequestRemoteLoopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTstRequestRemoteLoopback.setStatus("current")


class _AdGenTA8xxTstIncomingInbandLoopbackPatterns_Type(Integer32):
    """Custom type adGenTA8xxTstIncomingInbandLoopbackPatterns based on Integer32"""
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


_AdGenTA8xxTstIncomingInbandLoopbackPatterns_Type.__name__ = "Integer32"
_AdGenTA8xxTstIncomingInbandLoopbackPatterns_Object = MibTableColumn
adGenTA8xxTstIncomingInbandLoopbackPatterns = _AdGenTA8xxTstIncomingInbandLoopbackPatterns_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 4, 1, 3),
    _AdGenTA8xxTstIncomingInbandLoopbackPatterns_Type()
)
adGenTA8xxTstIncomingInbandLoopbackPatterns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTstIncomingInbandLoopbackPatterns.setStatus("current")


class _AdGenTA8xxTstIncomingFDLLoopbackPatterns_Type(Integer32):
    """Custom type adGenTA8xxTstIncomingFDLLoopbackPatterns based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("disable", 3),
          ("enable", 4))
    )


_AdGenTA8xxTstIncomingFDLLoopbackPatterns_Type.__name__ = "Integer32"
_AdGenTA8xxTstIncomingFDLLoopbackPatterns_Object = MibTableColumn
adGenTA8xxTstIncomingFDLLoopbackPatterns = _AdGenTA8xxTstIncomingFDLLoopbackPatterns_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 5, 4, 1, 4),
    _AdGenTA8xxTstIncomingFDLLoopbackPatterns_Type()
)
adGenTA8xxTstIncomingFDLLoopbackPatterns.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxTstIncomingFDLLoopbackPatterns.setStatus("current")
_AdGenTA8xxAlarms_ObjectIdentity = ObjectIdentity
adGenTA8xxAlarms = _AdGenTA8xxAlarms_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 6)
)
_AdGenTA8xxAlarmScalars_ObjectIdentity = ObjectIdentity
adGenTA8xxAlarmScalars = _AdGenTA8xxAlarmScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 6, 1)
)


class _AdGenTA8xxTrapAlarmLevel_Type(Integer32):
    """Custom type adGenTA8xxTrapAlarmLevel based on Integer32"""
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
        *(("disabled", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenTA8xxTrapAlarmLevel_Type.__name__ = "Integer32"
_AdGenTA8xxTrapAlarmLevel_Object = MibScalar
adGenTA8xxTrapAlarmLevel = _AdGenTA8xxTrapAlarmLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 6, 1, 1),
    _AdGenTA8xxTrapAlarmLevel_Type()
)
adGenTA8xxTrapAlarmLevel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenTA8xxTrapAlarmLevel.setStatus("current")


class _AdGenTA8xxACPwrInLevel_Type(Integer32):
    """Custom type adGenTA8xxACPwrInLevel based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6),
          ("aco", 7))
    )


_AdGenTA8xxACPwrInLevel_Type.__name__ = "Integer32"
_AdGenTA8xxACPwrInLevel_Object = MibScalar
adGenTA8xxACPwrInLevel = _AdGenTA8xxACPwrInLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 6, 1, 2),
    _AdGenTA8xxACPwrInLevel_Type()
)
adGenTA8xxACPwrInLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxACPwrInLevel.setStatus("current")


class _AdGenTA8xxPwrALevel_Type(Integer32):
    """Custom type adGenTA8xxPwrALevel based on Integer32"""
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
        *(("disabled", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenTA8xxPwrALevel_Type.__name__ = "Integer32"
_AdGenTA8xxPwrALevel_Object = MibScalar
adGenTA8xxPwrALevel = _AdGenTA8xxPwrALevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 6, 1, 3),
    _AdGenTA8xxPwrALevel_Type()
)
adGenTA8xxPwrALevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxPwrALevel.setStatus("current")


class _AdGenTA8xxPwrBLevel_Type(Integer32):
    """Custom type adGenTA8xxPwrBLevel based on Integer32"""
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
        *(("disabled", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenTA8xxPwrBLevel_Type.__name__ = "Integer32"
_AdGenTA8xxPwrBLevel_Object = MibScalar
adGenTA8xxPwrBLevel = _AdGenTA8xxPwrBLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 6, 1, 4),
    _AdGenTA8xxPwrBLevel_Type()
)
adGenTA8xxPwrBLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxPwrBLevel.setStatus("current")


class _AdGenTA8xxAcknowledgeAlarms_Type(Integer32):
    """Custom type adGenTA8xxAcknowledgeAlarms based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("ackControllers", 2),
          ("ackModuleA", 3),
          ("ackModuleB", 4),
          ("ackAll", 5))
    )


_AdGenTA8xxAcknowledgeAlarms_Type.__name__ = "Integer32"
_AdGenTA8xxAcknowledgeAlarms_Object = MibScalar
adGenTA8xxAcknowledgeAlarms = _AdGenTA8xxAcknowledgeAlarms_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 6, 1, 5),
    _AdGenTA8xxAcknowledgeAlarms_Type()
)
adGenTA8xxAcknowledgeAlarms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxAcknowledgeAlarms.setStatus("current")
_AdGenTA8xxSpecificTrapEnable_Type = OctetString
_AdGenTA8xxSpecificTrapEnable_Object = MibScalar
adGenTA8xxSpecificTrapEnable = _AdGenTA8xxSpecificTrapEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 6, 1, 6),
    _AdGenTA8xxSpecificTrapEnable_Type()
)
adGenTA8xxSpecificTrapEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxSpecificTrapEnable.setStatus("current")


class _AdGenTA8xxLoginFailureLevel_Type(Integer32):
    """Custom type adGenTA8xxLoginFailureLevel based on Integer32"""
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
        *(("disabled", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenTA8xxLoginFailureLevel_Type.__name__ = "Integer32"
_AdGenTA8xxLoginFailureLevel_Object = MibScalar
adGenTA8xxLoginFailureLevel = _AdGenTA8xxLoginFailureLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 6, 1, 7),
    _AdGenTA8xxLoginFailureLevel_Type()
)
adGenTA8xxLoginFailureLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxLoginFailureLevel.setStatus("current")


class _AdGenTA8xxLoginSuccessLevel_Type(Integer32):
    """Custom type adGenTA8xxLoginSuccessLevel based on Integer32"""
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
        *(("disabled", 1),
          ("info", 2),
          ("alert", 3),
          ("minor", 4),
          ("major", 5),
          ("critical", 6))
    )


_AdGenTA8xxLoginSuccessLevel_Type.__name__ = "Integer32"
_AdGenTA8xxLoginSuccessLevel_Object = MibScalar
adGenTA8xxLoginSuccessLevel = _AdGenTA8xxLoginSuccessLevel_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 6, 1, 8),
    _AdGenTA8xxLoginSuccessLevel_Type()
)
adGenTA8xxLoginSuccessLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenTA8xxLoginSuccessLevel.setStatus("current")
_AdGenTA8xxMibConformance_ObjectIdentity = ObjectIdentity
adGenTA8xxMibConformance = _AdGenTA8xxMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8)
)
_AdGenTA8xxMibGroups_ObjectIdentity = ObjectIdentity
adGenTA8xxMibGroups = _AdGenTA8xxMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1)
)

# Managed Objects groups

adGenTA8xxConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 1)
)
adGenTA8xxConfigGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBootVersion"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSwChecksum"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBootChecksum"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSavedSwVersion"))
)
if mibBuilder.loadTexts:
    adGenTA8xxConfigGroup.setStatus("current")

adGenTA8xxCardProvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 2)
)
adGenTA8xxCardProvGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxAutoLogoffTime"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSaveProv"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxScheduledResetTime"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSecondaryTelnetPort"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxRestoreFactoryDefaults"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxReset"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBondingPrimaryRef"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBondingSecondaryRef"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxIpACLState"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxIpACLInsert"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxIpACLRemove"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureThresholdCelsuis"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureThresholdFahrenheit"))
)
if mibBuilder.loadTexts:
    adGenTA8xxCardProvGroup.setStatus("current")

adGenTA8xx10100EthProvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 3)
)
adGenTA8xx10100EthProvGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthPortState"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthPortRateDuplex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthPortCrossOverMode"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthPortLsa"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthPortName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthPortLsaBandwidthMinimum"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthPortLsaLinksMinimum"))
)
if mibBuilder.loadTexts:
    adGenTA8xx10100EthProvGroup.setStatus("current")

adGenTA8xxGigEthProvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 4)
)
adGenTA8xxGigEthProvGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthState"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthLsa"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthPortSpeed"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthLsaBandwidthMinimum"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthLsaLinksMinimum"))
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEthProvGroup.setStatus("current")

adGenTA8xxCardStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 5)
)
adGenTA8xxCardStatusGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxCardStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxCritRelay"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxMajRelay"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxMinRelay"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxacoStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxACPwrInStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxPowerAStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxPowerBStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxEnvAlarmsAggregateStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxIPAddress"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSubnetMask"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxDefaultGateway"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBondingFunctLineSource"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBondingPriRefStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBondingSecRefStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxIpACLDepth"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxCurrentCPUUtilization"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxMaxCPUUtilization"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxResetMaxCPUUtilization"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureCelsuis"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureFahrenheit"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxCustomerDoor"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTelcoDoor"))
)
if mibBuilder.loadTexts:
    adGenTA8xxCardStatusGroup.setStatus("current")

adGenTA8xx10100EthStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 6)
)
adGenTA8xx10100EthStatusGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthLinkStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthLinkSpeedDuplex"))
)
if mibBuilder.loadTexts:
    adGenTA8xx10100EthStatusGroup.setStatus("current")

adGenTA8xxGigEthStatusGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 7)
)
adGenTA8xxGigEthStatusGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthLinkStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthSFPDescription"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthSFPADTRANSerialNumber"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthSFPADTRANPartNumber"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthSFPADTRANCLEICode"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthSFPJackType"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthSFPADTRANApproved"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthSFPTemperature"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthSFPTxBias"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthSFPTxPower"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthSFPRxPower"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthLinkSpeedDuplex"))
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEthStatusGroup.setStatus("current")

adGenTA8xxCardPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 8)
)
adGenTA8xxCardPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxRstAllCurrentIntervals"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxRstAllIntervals"))
)
if mibBuilder.loadTexts:
    adGenTA8xxCardPerfGroup.setStatus("current")

adGenTA8xx10100EthRstPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 9)
)
adGenTA8xx10100EthRstPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthRstCurrentIntervals"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthRstAll"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100EthPerfReset"))
)
if mibBuilder.loadTexts:
    adGenTA8xx10100EthRstPerfGroup.setStatus("current")

adGenTA8xx10100EthCurr15MinPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 10)
)
adGenTA8xx10100EthCurr15MinPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentTxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentTxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxCRCAlignErrs"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxUndersizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxOversizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxCollisions"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxDiscardedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentTxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentTxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentTxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinCurrentRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xx10100EthCurr15MinPerfGroup.setStatus("current")

adGenTA8xx10100EthInt15MinPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 11)
)
adGenTA8xx10100EthInt15MinPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalNumber"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalTxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalTxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxCRCAlignErrs"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxUndersizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxOversizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxCollisions"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxDiscardedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalTxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalTxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalTxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinIntervalRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xx10100EthInt15MinPerfGroup.setStatus("current")

adGenTA8xx10100EthCurr24HrPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 12)
)
adGenTA8xx10100EthCurr24HrPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentTxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentTxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxCRCAlignErrs"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxUndersizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxOversizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxCollisions"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxDiscardedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentTxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentTxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentTxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrCurrentRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xx10100EthCurr24HrPerfGroup.setStatus("current")

adGenTA8xx10100EthInt24HrPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 13)
)
adGenTA8xx10100EthInt24HrPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalNumber"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalTxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalTxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxCRCAlignErrs"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxUndersizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxOversizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxCollisions"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxDiscardedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalTxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalTxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalTxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrIntervalRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xx10100EthInt24HrPerfGroup.setStatus("current")

adGenTA8xxGigEthRstPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 14)
)
adGenTA8xxGigEthRstPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthRstCurrentIntervals"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthRstAll"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEthPerfReset"))
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEthRstPerfGroup.setStatus("current")

adGenTA8xxGigEthCurr15MinPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 15)
)
adGenTA8xxGigEthCurr15MinPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentTxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentTxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxGoodBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxGoodFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxFCSErrors"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxDroppedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxFramesTooBig"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxFramesTooSmall"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentTxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentTxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentTxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinCurrentRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEthCurr15MinPerfGroup.setStatus("current")

adGenTA8xxGigEthInt15MinPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 16)
)
adGenTA8xxGigEthInt15MinPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalNumber"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalTxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalTxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxGoodBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxGoodFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxFCSErrors"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxDroppedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxFramesTooBig"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxFramesTooSmall"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalTxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalTxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalTxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinIntervalRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEthInt15MinPerfGroup.setStatus("current")

adGenTA8xxGigEthCurr24HrPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 17)
)
adGenTA8xxGigEthCurr24HrPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentTxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentTxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxGoodBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxGoodFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxFCSErrors"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxDroppedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxFramesTooBig"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxFramesTooSmall"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentTxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentTxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentTxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrCurrentRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEthCurr24HrPerfGroup.setStatus("current")

adGenTA8xxGigEthInt24HrPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 18)
)
adGenTA8xxGigEthInt24HrPerfGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalNumber"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalTxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalTxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxGoodBytes"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxGoodFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxFCSErrors"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxDroppedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxFramesTooBig"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxFramesTooSmall"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalTxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalTxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalTxUnicastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrIntervalRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEthInt24HrPerfGroup.setStatus("current")

adGenTA8xxTestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 19)
)
adGenTA8xxTestGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxResetTests"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTestTimeout"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxRelayTest"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTestCriticalRelay"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTestMajorRelay"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTestMinorRelay"))
)
if mibBuilder.loadTexts:
    adGenTA8xxTestGroup.setStatus("current")

adGenTA8xxAlarmGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 20)
)
adGenTA8xxAlarmGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxACPwrInLevel"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxPwrALevel"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxPwrBLevel"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxAcknowledgeAlarms"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSpecificTrapEnable"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxLoginFailureLevel"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxLoginSuccessLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxAlarmGroup.setStatus("current")

adGenTA8xxFarEndConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 22)
)
adGenTA8xxFarEndConfigGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxFarEndIfIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxFarEndIPAddress"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxFarEndSysName"))
)
if mibBuilder.loadTexts:
    adGenTA8xxFarEndConfigGroup.setStatus("current")

adGenTA8xx10100EthThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 23)
)
adGenTA8xx10100EthThreshGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinThreshRxCRCAlignErrs"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinThreshRxUndersizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinThreshRxOversizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinThreshRxCollisions"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrThreshRxCRCAlignErrs"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrThreshRxUndersizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrThreshRxOversizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrThreshRxCollisions"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinThreshRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinThreshRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrThreshRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrThreshRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinThreshRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth15MinThreshRxFragments"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrThreshRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xx10100Eth24HrThreshRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xx10100EthThreshGroup.setStatus("current")

adGenTA8xxGigEthThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 24)
)
adGenTA8xxGigEthThreshGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinThreshRxFCSErrors"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinThreshRxDroppedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinThreshRxFramesTooBig"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinThreshRxFramesTooSmall"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrThreshRxFCSErrors"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrThreshRxDroppedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrThreshRxFramesTooBig"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrThreshRxFramesTooSmall"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinThreshRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinThreshRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrThreshRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrThreshRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinThreshRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth15MinThreshRxFragments"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrThreshRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxGigEth24HrThreshRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xxGigEthThreshGroup.setStatus("current")

adGenTA8xxBertPrvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 25)
)
adGenTA8xxBertPrvGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertStartAndStop"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertResetStatistics"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertPattern"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertPatternPolarity"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertErrorInject"))
)
if mibBuilder.loadTexts:
    adGenTA8xxBertPrvGroup.setStatus("current")

adGenTA8xxBertStatGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 26)
)
adGenTA8xxBertStatGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertBER"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertErrorCount"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertPattSyncLossCount"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertErroredSeconds"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstBertElapsedTime"))
)
if mibBuilder.loadTexts:
    adGenTA8xxBertStatGroup.setStatus("current")

adGenTA8xxTstLpbkPrvGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 27)
)
adGenTA8xxTstLpbkPrvGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstIncomingLoopbackPatterns"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstRequestRemoteLoopback"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstIncomingInbandLoopbackPatterns"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTstIncomingFDLLoopbackPatterns"))
)
if mibBuilder.loadTexts:
    adGenTA8xxTstLpbkPrvGroup.setStatus("current")

adGenTA8xxMgmtStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 28)
)
adGenTA8xxMgmtStatsGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxMgmtStatsCurrentTxFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxMgmtStatsCurrentRxFrames"))
)
if mibBuilder.loadTexts:
    adGenTA8xxMgmtStatsGroup.setStatus("current")

adGenTA8xxDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 29)
)
adGenTA8xxDeprecatedGroup.setObjects(
    ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxCapabilities")
)
if mibBuilder.loadTexts:
    adGenTA8xxDeprecatedGroup.setStatus("deprecated")


# Notification objects

adGenTA8xxClrCardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 3)
)
adGenTA8xxClrCardFailure.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxClrCardFailure.setStatus(
        "current"
    )

adGenTA8xxSetCardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 4)
)
adGenTA8xxSetCardFailure.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotAlarmStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetCardFailure.setStatus(
        "current"
    )

adGenTA8xxClrSACardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 51)
)
adGenTA8xxClrSACardFailure.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxClrSACardFailure.setStatus(
        "current"
    )

adGenTA8xxSetSACardFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 52)
)
adGenTA8xxSetSACardFailure.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetSACardFailure.setStatus(
        "current"
    )

adGenTA8xxACPwrInAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 61)
)
adGenTA8xxACPwrInAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxACPwrInLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxACPwrInAlmClear.setStatus(
        "current"
    )

adGenTA8xxACPwrInAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 62)
)
adGenTA8xxACPwrInAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxACPwrInLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxACPwrInAlm.setStatus(
        "current"
    )

adGenTA8xxBusApwrAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 69)
)
adGenTA8xxBusApwrAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxPwrALevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxBusApwrAlmClear.setStatus(
        "current"
    )

adGenTA8xxBusApowerAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 70)
)
adGenTA8xxBusApowerAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxPwrALevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxBusApowerAlm.setStatus(
        "current"
    )

adGenTA8xxBusBpwrAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 71)
)
adGenTA8xxBusBpwrAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxPwrBLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxBusBpwrAlmClear.setStatus(
        "current"
    )

adGenTA8xxBusBpowerAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 72)
)
adGenTA8xxBusBpowerAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxPwrBLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxBusBpowerAlm.setStatus(
        "current"
    )

adGenTA8xxUserLockoutClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 73)
)
adGenTA8xxUserLockoutClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxUserLockoutClear.setStatus(
        "current"
    )

adGenTA8xxUserLockoutAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 74)
)
adGenTA8xxUserLockoutAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxUserLockoutAlm.setStatus(
        "current"
    )

adGenTA8xxUserLoginSuccess = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 75)
)
adGenTA8xxUserLoginSuccess.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxUserLoginSuccess.setStatus(
        "current"
    )

adGenTA8xxUserLoginFailure = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 76)
)
adGenTA8xxUserLoginFailure.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxUserLoginFailure.setStatus(
        "current"
    )

adGenTA8xxFanModuleAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 77)
)
adGenTA8xxFanModuleAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxFanModuleAlmClear.setStatus(
        "current"
    )

adGenTA8xxFanModuleAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 78)
)
adGenTA8xxFanModuleAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxFanModuleAlm.setStatus(
        "current"
    )

adGenTA8xxSingleFanFailureAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 79)
)
adGenTA8xxSingleFanFailureAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSingleFanFailureAlmClear.setStatus(
        "current"
    )

adGenTA8xxSingleFanFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 80)
)
adGenTA8xxSingleFanFailureAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSingleFanFailureAlm.setStatus(
        "current"
    )

adGenTA8xxMultipleFanFailureAlmClear = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 81)
)
adGenTA8xxMultipleFanFailureAlmClear.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxMultipleFanFailureAlmClear.setStatus(
        "current"
    )

adGenTA8xxMultipleFanFailureAlm = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 82)
)
adGenTA8xxMultipleFanFailureAlm.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxMultipleFanFailureAlm.setStatus(
        "current"
    )

adGenTA8xxClr10100EthLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 89)
)
adGenTA8xxClr10100EthLinkDown.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxClr10100EthLinkDown.setStatus(
        "current"
    )

adGenTA8xxSet10100EthLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 90)
)
adGenTA8xxSet10100EthLinkDown.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100EthLinkDown.setStatus(
        "current"
    )

adGenTA8xxClrGigEthLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 91)
)
adGenTA8xxClrGigEthLinkDown.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxClrGigEthLinkDown.setStatus(
        "current"
    )

adGenTA8xxSetGigEthLinkDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 92)
)
adGenTA8xxSetGigEthLinkDown.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEthLinkDown.setStatus(
        "current"
    )

adGenTA8xxClrGigEthUnapprovedSFP = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 93)
)
adGenTA8xxClrGigEthUnapprovedSFP.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxClrGigEthUnapprovedSFP.setStatus(
        "current"
    )

adGenTA8xxSetGigEthUnapprovedSFP = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 94)
)
adGenTA8xxSetGigEthUnapprovedSFP.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEthUnapprovedSFP.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth15MinRxCRCAlignErrs = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 100)
)
adGenTA8xxSet10100Eth15MinRxCRCAlignErrs.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth15MinRxCRCAlignErrs.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth15MinRxUndersizeFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 101)
)
adGenTA8xxSet10100Eth15MinRxUndersizeFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth15MinRxUndersizeFrames.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth15MinRxOversizeFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 102)
)
adGenTA8xxSet10100Eth15MinRxOversizeFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth15MinRxOversizeFrames.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth15MinRxCollisions = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 103)
)
adGenTA8xxSet10100Eth15MinRxCollisions.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth15MinRxCollisions.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth15MinRxDiscardedFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 104)
)
adGenTA8xxSet10100Eth15MinRxDiscardedFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth15MinRxDiscardedFrames.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth24HrRxCRCAlignErrs = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 105)
)
adGenTA8xxSet10100Eth24HrRxCRCAlignErrs.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth24HrRxCRCAlignErrs.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth24HrRxUndersizeFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 106)
)
adGenTA8xxSet10100Eth24HrRxUndersizeFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth24HrRxUndersizeFrames.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth24HrRxOversizeFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 107)
)
adGenTA8xxSet10100Eth24HrRxOversizeFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth24HrRxOversizeFrames.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth24HrRxCollisions = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 108)
)
adGenTA8xxSet10100Eth24HrRxCollisions.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth24HrRxCollisions.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth24HrRxDiscardedFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 109)
)
adGenTA8xxSet10100Eth24HrRxDiscardedFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth24HrRxDiscardedFrames.setStatus(
        "current"
    )

adGenTA8xxSetGigEth15MinRxFCSErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 110)
)
adGenTA8xxSetGigEth15MinRxFCSErrors.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth15MinRxFCSErrors.setStatus(
        "current"
    )

adGenTA8xxSetGigEth15MinRxDroppedFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 111)
)
adGenTA8xxSetGigEth15MinRxDroppedFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth15MinRxDroppedFrames.setStatus(
        "current"
    )

adGenTA8xxSetGigEth15MinRxFramesTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 112)
)
adGenTA8xxSetGigEth15MinRxFramesTooBig.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth15MinRxFramesTooBig.setStatus(
        "current"
    )

adGenTA8xxSetGigEth15MinRxFramesTooSmall = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 113)
)
adGenTA8xxSetGigEth15MinRxFramesTooSmall.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth15MinRxFramesTooSmall.setStatus(
        "current"
    )

adGenTA8xxSetGigEth24HrRxFCSErrors = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 114)
)
adGenTA8xxSetGigEth24HrRxFCSErrors.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth24HrRxFCSErrors.setStatus(
        "current"
    )

adGenTA8xxSetGigEth24HrRxDroppedFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 115)
)
adGenTA8xxSetGigEth24HrRxDroppedFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth24HrRxDroppedFrames.setStatus(
        "current"
    )

adGenTA8xxSetGigEth24HrRxFramesTooBig = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 116)
)
adGenTA8xxSetGigEth24HrRxFramesTooBig.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth24HrRxFramesTooBig.setStatus(
        "current"
    )

adGenTA8xxSetGigEth24HrRxFramesTooSmall = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 117)
)
adGenTA8xxSetGigEth24HrRxFramesTooSmall.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth24HrRxFramesTooSmall.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth15MinRxMulticastFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 118)
)
adGenTA8xxSet10100Eth15MinRxMulticastFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth15MinRxMulticastFrames.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth15MinRxBroadcastFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 119)
)
adGenTA8xxSet10100Eth15MinRxBroadcastFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth15MinRxBroadcastFrames.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth24HrRxMulticastFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 120)
)
adGenTA8xxSet10100Eth24HrRxMulticastFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth24HrRxMulticastFrames.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth24HrRxBroadcastFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 121)
)
adGenTA8xxSet10100Eth24HrRxBroadcastFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth24HrRxBroadcastFrames.setStatus(
        "current"
    )

adGenTA8xxSetGigEth15MinRxMulticastFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 122)
)
adGenTA8xxSetGigEth15MinRxMulticastFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth15MinRxMulticastFrames.setStatus(
        "current"
    )

adGenTA8xxSetGigEth15MinRxBroadcastFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 123)
)
adGenTA8xxSetGigEth15MinRxBroadcastFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth15MinRxBroadcastFrames.setStatus(
        "current"
    )

adGenTA8xxSetGigEth24HrRxMulticastFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 124)
)
adGenTA8xxSetGigEth24HrRxMulticastFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth24HrRxMulticastFrames.setStatus(
        "current"
    )

adGenTA8xxSetGigEth24HrRxBroadcastFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 125)
)
adGenTA8xxSetGigEth24HrRxBroadcastFrames.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth24HrRxBroadcastFrames.setStatus(
        "current"
    )

adGenTA8xxTemperatureHigh = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 126)
)
adGenTA8xxTemperatureHigh.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureCelsuis"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureThresholdCelsuis"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureFahrenheit"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureThresholdFahrenheit"))
)
if mibBuilder.loadTexts:
    adGenTA8xxTemperatureHigh.setStatus(
        "current"
    )

adGenTA8xxTemperatureNormal = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 127)
)
adGenTA8xxTemperatureNormal.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureCelsuis"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureThresholdCelsuis"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureFahrenheit"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureThresholdFahrenheit"))
)
if mibBuilder.loadTexts:
    adGenTA8xxTemperatureNormal.setStatus(
        "current"
    )

adGenTA8xxCustomerDoorStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 128)
)
adGenTA8xxCustomerDoorStatus.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxCustomerDoor"))
)
if mibBuilder.loadTexts:
    adGenTA8xxCustomerDoorStatus.setStatus(
        "current"
    )

adGenTA8xxTelcoDoorStatus = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 129)
)
adGenTA8xxTelcoDoorStatus.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTelcoDoor"))
)
if mibBuilder.loadTexts:
    adGenTA8xxTelcoDoorStatus.setStatus(
        "current"
    )

adGenTA8xxClr10100EthLinkLsaForcedDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 130)
)
adGenTA8xxClr10100EthLinkLsaForcedDown.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxClr10100EthLinkLsaForcedDown.setStatus(
        "current"
    )

adGenTA8xxSet10100EthLinkLsaForcedDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 131)
)
adGenTA8xxSet10100EthLinkLsaForcedDown.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100EthLinkLsaForcedDown.setStatus(
        "current"
    )

adGenTA8xxClrGigEthLinkLsaForcedDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 132)
)
adGenTA8xxClrGigEthLinkLsaForcedDown.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxClrGigEthLinkLsaForcedDown.setStatus(
        "current"
    )

adGenTA8xxSetGigEthLinkLsaForcedDown = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 133)
)
adGenTA8xxSetGigEthLinkLsaForcedDown.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEthLinkLsaForcedDown.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth15MinRxJabbers = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 134)
)
adGenTA8xxSet10100Eth15MinRxJabbers.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth15MinRxJabbers.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth24HrRxJabbers = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 135)
)
adGenTA8xxSet10100Eth24HrRxJabbers.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth24HrRxJabbers.setStatus(
        "current"
    )

adGenTA8xxSetGigEth15MinRxJabbers = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 136)
)
adGenTA8xxSetGigEth15MinRxJabbers.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth15MinRxJabbers.setStatus(
        "current"
    )

adGenTA8xxSetGigEth24HrRxJabbers = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 137)
)
adGenTA8xxSetGigEth24HrRxJabbers.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth24HrRxJabbers.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth15MinRxFragments = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 138)
)
adGenTA8xxSet10100Eth15MinRxFragments.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth15MinRxFragments.setStatus(
        "current"
    )

adGenTA8xxSet10100Eth24HrRxFragments = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 139)
)
adGenTA8xxSet10100Eth24HrRxFragments.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSet10100Eth24HrRxFragments.setStatus(
        "current"
    )

adGenTA8xxSetGigEth15MinRxFragments = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 140)
)
adGenTA8xxSetGigEth15MinRxFragments.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth15MinRxFragments.setStatus(
        "current"
    )

adGenTA8xxSetGigEth24HrRxFragments = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 0, 141)
)
adGenTA8xxSetGigEth24HrRxFragments.setObjects(
      *(("ADTRAN-GENTRAPINFORM-MIB", "adTrapInformSeqNum"),
        ("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTrapAlarmLevel"))
)
if mibBuilder.loadTexts:
    adGenTA8xxSetGigEth24HrRxFragments.setStatus(
        "current"
    )


# Notifications groups

adGenTA8xxEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 2, 8, 1, 21)
)
adGenTA8xxEventGroup.setObjects(
      *(("ADTRAN-GENTA8XX-MIB", "adGenTA8xxClrCardFailure"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetCardFailure"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxClrSACardFailure"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetSACardFailure"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxACPwrInAlmClear"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxACPwrInAlm"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBusApwrAlmClear"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBusApowerAlm"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBusBpwrAlmClear"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxBusBpowerAlm"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxUserLockoutClear"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxUserLockoutAlm"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxUserLoginSuccess"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxUserLoginFailure"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxClr10100EthLinkDown"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100EthLinkDown"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxClrGigEthLinkDown"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEthLinkDown"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth15MinRxCRCAlignErrs"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth15MinRxUndersizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth15MinRxOversizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth15MinRxCollisions"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth24HrRxCRCAlignErrs"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth24HrRxUndersizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth24HrRxOversizeFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth24HrRxCollisions"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth15MinRxFCSErrors"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth15MinRxDroppedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth15MinRxFramesTooBig"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth15MinRxFramesTooSmall"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth24HrRxFCSErrors"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth24HrRxDroppedFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth24HrRxFramesTooBig"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth24HrRxFramesTooSmall"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth15MinRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth15MinRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth24HrRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth24HrRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth15MinRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth15MinRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth24HrRxMulticastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth24HrRxBroadcastFrames"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxFanModuleAlm"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSingleFanFailureAlm"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxMultipleFanFailureAlm"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxFanModuleAlmClear"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSingleFanFailureAlmClear"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxMultipleFanFailureAlmClear"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureHigh"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTemperatureNormal"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxCustomerDoorStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxTelcoDoorStatus"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxClr10100EthLinkLsaForcedDown"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100EthLinkLsaForcedDown"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxClrGigEthLinkLsaForcedDown"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEthLinkLsaForcedDown"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth15MinRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth24HrRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth15MinRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth24HrRxJabbers"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth15MinRxFragments"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSet10100Eth24HrRxFragments"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth15MinRxFragments"),
        ("ADTRAN-GENTA8XX-MIB", "adGenTA8xxSetGigEth24HrRxFragments"))
)
if mibBuilder.loadTexts:
    adGenTA8xxEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENTA8XX-MIB",
    **{"adGenTA8xxEvents": adGenTA8xxEvents,
       "adGenTA8xxClrCardFailure": adGenTA8xxClrCardFailure,
       "adGenTA8xxSetCardFailure": adGenTA8xxSetCardFailure,
       "adGenTA8xxClrSACardFailure": adGenTA8xxClrSACardFailure,
       "adGenTA8xxSetSACardFailure": adGenTA8xxSetSACardFailure,
       "adGenTA8xxACPwrInAlmClear": adGenTA8xxACPwrInAlmClear,
       "adGenTA8xxACPwrInAlm": adGenTA8xxACPwrInAlm,
       "adGenTA8xxBusApwrAlmClear": adGenTA8xxBusApwrAlmClear,
       "adGenTA8xxBusApowerAlm": adGenTA8xxBusApowerAlm,
       "adGenTA8xxBusBpwrAlmClear": adGenTA8xxBusBpwrAlmClear,
       "adGenTA8xxBusBpowerAlm": adGenTA8xxBusBpowerAlm,
       "adGenTA8xxUserLockoutClear": adGenTA8xxUserLockoutClear,
       "adGenTA8xxUserLockoutAlm": adGenTA8xxUserLockoutAlm,
       "adGenTA8xxUserLoginSuccess": adGenTA8xxUserLoginSuccess,
       "adGenTA8xxUserLoginFailure": adGenTA8xxUserLoginFailure,
       "adGenTA8xxFanModuleAlmClear": adGenTA8xxFanModuleAlmClear,
       "adGenTA8xxFanModuleAlm": adGenTA8xxFanModuleAlm,
       "adGenTA8xxSingleFanFailureAlmClear": adGenTA8xxSingleFanFailureAlmClear,
       "adGenTA8xxSingleFanFailureAlm": adGenTA8xxSingleFanFailureAlm,
       "adGenTA8xxMultipleFanFailureAlmClear": adGenTA8xxMultipleFanFailureAlmClear,
       "adGenTA8xxMultipleFanFailureAlm": adGenTA8xxMultipleFanFailureAlm,
       "adGenTA8xxClr10100EthLinkDown": adGenTA8xxClr10100EthLinkDown,
       "adGenTA8xxSet10100EthLinkDown": adGenTA8xxSet10100EthLinkDown,
       "adGenTA8xxClrGigEthLinkDown": adGenTA8xxClrGigEthLinkDown,
       "adGenTA8xxSetGigEthLinkDown": adGenTA8xxSetGigEthLinkDown,
       "adGenTA8xxClrGigEthUnapprovedSFP": adGenTA8xxClrGigEthUnapprovedSFP,
       "adGenTA8xxSetGigEthUnapprovedSFP": adGenTA8xxSetGigEthUnapprovedSFP,
       "adGenTA8xxSet10100Eth15MinRxCRCAlignErrs": adGenTA8xxSet10100Eth15MinRxCRCAlignErrs,
       "adGenTA8xxSet10100Eth15MinRxUndersizeFrames": adGenTA8xxSet10100Eth15MinRxUndersizeFrames,
       "adGenTA8xxSet10100Eth15MinRxOversizeFrames": adGenTA8xxSet10100Eth15MinRxOversizeFrames,
       "adGenTA8xxSet10100Eth15MinRxCollisions": adGenTA8xxSet10100Eth15MinRxCollisions,
       "adGenTA8xxSet10100Eth15MinRxDiscardedFrames": adGenTA8xxSet10100Eth15MinRxDiscardedFrames,
       "adGenTA8xxSet10100Eth24HrRxCRCAlignErrs": adGenTA8xxSet10100Eth24HrRxCRCAlignErrs,
       "adGenTA8xxSet10100Eth24HrRxUndersizeFrames": adGenTA8xxSet10100Eth24HrRxUndersizeFrames,
       "adGenTA8xxSet10100Eth24HrRxOversizeFrames": adGenTA8xxSet10100Eth24HrRxOversizeFrames,
       "adGenTA8xxSet10100Eth24HrRxCollisions": adGenTA8xxSet10100Eth24HrRxCollisions,
       "adGenTA8xxSet10100Eth24HrRxDiscardedFrames": adGenTA8xxSet10100Eth24HrRxDiscardedFrames,
       "adGenTA8xxSetGigEth15MinRxFCSErrors": adGenTA8xxSetGigEth15MinRxFCSErrors,
       "adGenTA8xxSetGigEth15MinRxDroppedFrames": adGenTA8xxSetGigEth15MinRxDroppedFrames,
       "adGenTA8xxSetGigEth15MinRxFramesTooBig": adGenTA8xxSetGigEth15MinRxFramesTooBig,
       "adGenTA8xxSetGigEth15MinRxFramesTooSmall": adGenTA8xxSetGigEth15MinRxFramesTooSmall,
       "adGenTA8xxSetGigEth24HrRxFCSErrors": adGenTA8xxSetGigEth24HrRxFCSErrors,
       "adGenTA8xxSetGigEth24HrRxDroppedFrames": adGenTA8xxSetGigEth24HrRxDroppedFrames,
       "adGenTA8xxSetGigEth24HrRxFramesTooBig": adGenTA8xxSetGigEth24HrRxFramesTooBig,
       "adGenTA8xxSetGigEth24HrRxFramesTooSmall": adGenTA8xxSetGigEth24HrRxFramesTooSmall,
       "adGenTA8xxSet10100Eth15MinRxMulticastFrames": adGenTA8xxSet10100Eth15MinRxMulticastFrames,
       "adGenTA8xxSet10100Eth15MinRxBroadcastFrames": adGenTA8xxSet10100Eth15MinRxBroadcastFrames,
       "adGenTA8xxSet10100Eth24HrRxMulticastFrames": adGenTA8xxSet10100Eth24HrRxMulticastFrames,
       "adGenTA8xxSet10100Eth24HrRxBroadcastFrames": adGenTA8xxSet10100Eth24HrRxBroadcastFrames,
       "adGenTA8xxSetGigEth15MinRxMulticastFrames": adGenTA8xxSetGigEth15MinRxMulticastFrames,
       "adGenTA8xxSetGigEth15MinRxBroadcastFrames": adGenTA8xxSetGigEth15MinRxBroadcastFrames,
       "adGenTA8xxSetGigEth24HrRxMulticastFrames": adGenTA8xxSetGigEth24HrRxMulticastFrames,
       "adGenTA8xxSetGigEth24HrRxBroadcastFrames": adGenTA8xxSetGigEth24HrRxBroadcastFrames,
       "adGenTA8xxTemperatureHigh": adGenTA8xxTemperatureHigh,
       "adGenTA8xxTemperatureNormal": adGenTA8xxTemperatureNormal,
       "adGenTA8xxCustomerDoorStatus": adGenTA8xxCustomerDoorStatus,
       "adGenTA8xxTelcoDoorStatus": adGenTA8xxTelcoDoorStatus,
       "adGenTA8xxClr10100EthLinkLsaForcedDown": adGenTA8xxClr10100EthLinkLsaForcedDown,
       "adGenTA8xxSet10100EthLinkLsaForcedDown": adGenTA8xxSet10100EthLinkLsaForcedDown,
       "adGenTA8xxClrGigEthLinkLsaForcedDown": adGenTA8xxClrGigEthLinkLsaForcedDown,
       "adGenTA8xxSetGigEthLinkLsaForcedDown": adGenTA8xxSetGigEthLinkLsaForcedDown,
       "adGenTA8xxSet10100Eth15MinRxJabbers": adGenTA8xxSet10100Eth15MinRxJabbers,
       "adGenTA8xxSet10100Eth24HrRxJabbers": adGenTA8xxSet10100Eth24HrRxJabbers,
       "adGenTA8xxSetGigEth15MinRxJabbers": adGenTA8xxSetGigEth15MinRxJabbers,
       "adGenTA8xxSetGigEth24HrRxJabbers": adGenTA8xxSetGigEth24HrRxJabbers,
       "adGenTA8xxSet10100Eth15MinRxFragments": adGenTA8xxSet10100Eth15MinRxFragments,
       "adGenTA8xxSet10100Eth24HrRxFragments": adGenTA8xxSet10100Eth24HrRxFragments,
       "adGenTA8xxSetGigEth15MinRxFragments": adGenTA8xxSetGigEth15MinRxFragments,
       "adGenTA8xxSetGigEth24HrRxFragments": adGenTA8xxSetGigEth24HrRxFragments,
       "adGenTA8xxConfiguration": adGenTA8xxConfiguration,
       "adGenTA8xxConfigTable": adGenTA8xxConfigTable,
       "adGenTA8xxConfigEntry": adGenTA8xxConfigEntry,
       "adGenTA8xxBootVersion": adGenTA8xxBootVersion,
       "adGenTA8xxSwChecksum": adGenTA8xxSwChecksum,
       "adGenTA8xxBootChecksum": adGenTA8xxBootChecksum,
       "adGenTA8xxSavedSwVersion": adGenTA8xxSavedSwVersion,
       "adGenTA8xxFarEndConfigTable": adGenTA8xxFarEndConfigTable,
       "adGenTA8xxFarEndConfigEntry": adGenTA8xxFarEndConfigEntry,
       "adGenTA8xxFarEndIfIndex": adGenTA8xxFarEndIfIndex,
       "adGenTA8xxFarEndIPAddress": adGenTA8xxFarEndIPAddress,
       "adGenTA8xxFarEndSysName": adGenTA8xxFarEndSysName,
       "adGenTA8xxProvisioning": adGenTA8xxProvisioning,
       "adGenTA8xxPrvScalars": adGenTA8xxPrvScalars,
       "adGenTA8xxAutoLogoffTime": adGenTA8xxAutoLogoffTime,
       "adGenTA8xxSaveProv": adGenTA8xxSaveProv,
       "adGenTA8xxScheduledResetTime": adGenTA8xxScheduledResetTime,
       "adGenTA8xxSecondaryTelnetPort": adGenTA8xxSecondaryTelnetPort,
       "adGenTA8xxBondingPrimaryRef": adGenTA8xxBondingPrimaryRef,
       "adGenTA8xxBondingSecondaryRef": adGenTA8xxBondingSecondaryRef,
       "adGenTA8xxCapabilities": adGenTA8xxCapabilities,
       "adGenTA8xxIpACLState": adGenTA8xxIpACLState,
       "adGenTA8xxIpACLInsert": adGenTA8xxIpACLInsert,
       "adGenTA8xxIpACLRemove": adGenTA8xxIpACLRemove,
       "adGenTA8xxIpACLRemoveAll": adGenTA8xxIpACLRemoveAll,
       "adGenTA8xxTemperatureThresholdCelsuis": adGenTA8xxTemperatureThresholdCelsuis,
       "adGenTA8xxTemperatureThresholdFahrenheit": adGenTA8xxTemperatureThresholdFahrenheit,
       "adGenTA8xxRollingAverageInterval": adGenTA8xxRollingAverageInterval,
       "adGenTA8xxPrv10100EthPortTable": adGenTA8xxPrv10100EthPortTable,
       "adGenTA8xxPrv10100EthPortEntry": adGenTA8xxPrv10100EthPortEntry,
       "adGenTA8xx10100EthPortState": adGenTA8xx10100EthPortState,
       "adGenTA8xx10100EthPortRateDuplex": adGenTA8xx10100EthPortRateDuplex,
       "adGenTA8xx10100EthPortCrossOverMode": adGenTA8xx10100EthPortCrossOverMode,
       "adGenTA8xx10100EthPortLsa": adGenTA8xx10100EthPortLsa,
       "adGenTA8xx10100EthPortName": adGenTA8xx10100EthPortName,
       "adGenTA8xx10100EthPortLsaBandwidthMinimum": adGenTA8xx10100EthPortLsaBandwidthMinimum,
       "adGenTA8xx10100EthPortLsaLinksMinimum": adGenTA8xx10100EthPortLsaLinksMinimum,
       "adGenTA8xxPrvGigEthTable": adGenTA8xxPrvGigEthTable,
       "adGenTA8xxPrvGigEthEntry": adGenTA8xxPrvGigEthEntry,
       "adGenTA8xxGigEthState": adGenTA8xxGigEthState,
       "adGenTA8xxGigEthLsa": adGenTA8xxGigEthLsa,
       "adGenTA8xxGigEthName": adGenTA8xxGigEthName,
       "adGenTA8xxGigEthPortSpeed": adGenTA8xxGigEthPortSpeed,
       "adGenTA8xxGigEthLsaBandwidthMinimum": adGenTA8xxGigEthLsaBandwidthMinimum,
       "adGenTA8xxGigEthLsaLinksMinimum": adGenTA8xxGigEthLsaLinksMinimum,
       "adGenTA8xxCardPrvTable": adGenTA8xxCardPrvTable,
       "adGenTA8xxCardPrvEntry": adGenTA8xxCardPrvEntry,
       "adGenTA8xxRestoreFactoryDefaults": adGenTA8xxRestoreFactoryDefaults,
       "adGenTA8xxReset": adGenTA8xxReset,
       "adGenTA8xxStatus": adGenTA8xxStatus,
       "adGenTA8xxStatScalars": adGenTA8xxStatScalars,
       "adGenTA8xxCardStatus": adGenTA8xxCardStatus,
       "adGenTA8xxCritRelay": adGenTA8xxCritRelay,
       "adGenTA8xxMajRelay": adGenTA8xxMajRelay,
       "adGenTA8xxMinRelay": adGenTA8xxMinRelay,
       "adGenTA8xxacoStatus": adGenTA8xxacoStatus,
       "adGenTA8xxACPwrInStatus": adGenTA8xxACPwrInStatus,
       "adGenTA8xxPowerAStatus": adGenTA8xxPowerAStatus,
       "adGenTA8xxPowerBStatus": adGenTA8xxPowerBStatus,
       "adGenTA8xxEnvAlarmsAggregateStatus": adGenTA8xxEnvAlarmsAggregateStatus,
       "adGenTA8xxIPAddress": adGenTA8xxIPAddress,
       "adGenTA8xxSubnetMask": adGenTA8xxSubnetMask,
       "adGenTA8xxDefaultGateway": adGenTA8xxDefaultGateway,
       "adGenTA8xxBondingFunctLineSource": adGenTA8xxBondingFunctLineSource,
       "adGenTA8xxBondingPriRefStatus": adGenTA8xxBondingPriRefStatus,
       "adGenTA8xxBondingSecRefStatus": adGenTA8xxBondingSecRefStatus,
       "adGenTA8xxIpACLDepth": adGenTA8xxIpACLDepth,
       "adGenTA8xxCurrentCPUUtilization": adGenTA8xxCurrentCPUUtilization,
       "adGenTA8xxMaxCPUUtilization": adGenTA8xxMaxCPUUtilization,
       "adGenTA8xxResetMaxCPUUtilization": adGenTA8xxResetMaxCPUUtilization,
       "adGenTA8xxTemperatureCelsuis": adGenTA8xxTemperatureCelsuis,
       "adGenTA8xxTemperatureFahrenheit": adGenTA8xxTemperatureFahrenheit,
       "adGenTA8xxCustomerDoor": adGenTA8xxCustomerDoor,
       "adGenTA8xxTelcoDoor": adGenTA8xxTelcoDoor,
       "adGenTA8xxAux1Door": adGenTA8xxAux1Door,
       "adGenTA8xxIpv6AddressPrefixLength": adGenTA8xxIpv6AddressPrefixLength,
       "adGenTA8xxIpv6AddressEui64": adGenTA8xxIpv6AddressEui64,
       "adGenTA8xxIpv6Address": adGenTA8xxIpv6Address,
       "adGenTA8xxIpv6AddressOperational": adGenTA8xxIpv6AddressOperational,
       "adGenTA8xxIpv6AddressLinkLocal": adGenTA8xxIpv6AddressLinkLocal,
       "adGenTA8xxIpv6AddressLinkLocalOperational": adGenTA8xxIpv6AddressLinkLocalOperational,
       "adGenTA8xxStat10100EthTable": adGenTA8xxStat10100EthTable,
       "adGenTA8xxStat10100EthEntry": adGenTA8xxStat10100EthEntry,
       "adGenTA8xx10100EthLinkStatus": adGenTA8xx10100EthLinkStatus,
       "adGenTA8xx10100EthLinkSpeedDuplex": adGenTA8xx10100EthLinkSpeedDuplex,
       "adGenTA8xxStatGigEthTable": adGenTA8xxStatGigEthTable,
       "adGenTA8xxStatGigEthEntry": adGenTA8xxStatGigEthEntry,
       "adGenTA8xxGigEthLinkStatus": adGenTA8xxGigEthLinkStatus,
       "adGenTA8xxGigEthSFPDescription": adGenTA8xxGigEthSFPDescription,
       "adGenTA8xxGigEthSFPADTRANSerialNumber": adGenTA8xxGigEthSFPADTRANSerialNumber,
       "adGenTA8xxGigEthSFPADTRANPartNumber": adGenTA8xxGigEthSFPADTRANPartNumber,
       "adGenTA8xxGigEthSFPADTRANCLEICode": adGenTA8xxGigEthSFPADTRANCLEICode,
       "adGenTA8xxGigEthSFPJackType": adGenTA8xxGigEthSFPJackType,
       "adGenTA8xxGigEthSFPADTRANApproved": adGenTA8xxGigEthSFPADTRANApproved,
       "adGenTA8xxGigEthSFPTemperature": adGenTA8xxGigEthSFPTemperature,
       "adGenTA8xxGigEthSFPTxBias": adGenTA8xxGigEthSFPTxBias,
       "adGenTA8xxGigEthSFPTxPower": adGenTA8xxGigEthSFPTxPower,
       "adGenTA8xxGigEthSFPRxPower": adGenTA8xxGigEthSFPRxPower,
       "adGenTA8xxGigEthLinkSpeedDuplex": adGenTA8xxGigEthLinkSpeedDuplex,
       "adGenTA8xxStatIpAclTable": adGenTA8xxStatIpAclTable,
       "adGenTA8xxStatIpAclEntry": adGenTA8xxStatIpAclEntry,
       "adGenTA8xxIpAclEntryIndex": adGenTA8xxIpAclEntryIndex,
       "adGenTA8xxIpAclEntries": adGenTA8xxIpAclEntries,
       "adGenTA8xxPerformance": adGenTA8xxPerformance,
       "adGenTA8xxPerformanceScalars": adGenTA8xxPerformanceScalars,
       "adGenTA8xxRstAllCurrentIntervals": adGenTA8xxRstAllCurrentIntervals,
       "adGenTA8xxRstAllIntervals": adGenTA8xxRstAllIntervals,
       "adGenTA8xxMgmtStatsCurrentTxFrames": adGenTA8xxMgmtStatsCurrentTxFrames,
       "adGenTA8xxMgmtStatsCurrentRxFrames": adGenTA8xxMgmtStatsCurrentRxFrames,
       "adGenTA8xx10100EthPerformance": adGenTA8xx10100EthPerformance,
       "adGenTA8xx10100EthPerformanceScalars": adGenTA8xx10100EthPerformanceScalars,
       "adGenTA8xx10100EthRstCurrentIntervals": adGenTA8xx10100EthRstCurrentIntervals,
       "adGenTA8xx10100EthRstAll": adGenTA8xx10100EthRstAll,
       "adGenTA8xx10100Eth15MinCurrentTable": adGenTA8xx10100Eth15MinCurrentTable,
       "adGenTA8xx10100Eth15MinCurrentEntry": adGenTA8xx10100Eth15MinCurrentEntry,
       "adGenTA8xx10100Eth15MinCurrentTxBytes": adGenTA8xx10100Eth15MinCurrentTxBytes,
       "adGenTA8xx10100Eth15MinCurrentTxFrames": adGenTA8xx10100Eth15MinCurrentTxFrames,
       "adGenTA8xx10100Eth15MinCurrentRxBytes": adGenTA8xx10100Eth15MinCurrentRxBytes,
       "adGenTA8xx10100Eth15MinCurrentRxFrames": adGenTA8xx10100Eth15MinCurrentRxFrames,
       "adGenTA8xx10100Eth15MinCurrentRxCRCAlignErrs": adGenTA8xx10100Eth15MinCurrentRxCRCAlignErrs,
       "adGenTA8xx10100Eth15MinCurrentRxUndersizeFrames": adGenTA8xx10100Eth15MinCurrentRxUndersizeFrames,
       "adGenTA8xx10100Eth15MinCurrentRxOversizeFrames": adGenTA8xx10100Eth15MinCurrentRxOversizeFrames,
       "adGenTA8xx10100Eth15MinCurrentRxCollisions": adGenTA8xx10100Eth15MinCurrentRxCollisions,
       "adGenTA8xx10100Eth15MinCurrentRxDiscardedFrames": adGenTA8xx10100Eth15MinCurrentRxDiscardedFrames,
       "adGenTA8xx10100Eth15MinCurrentRxMulticastFrames": adGenTA8xx10100Eth15MinCurrentRxMulticastFrames,
       "adGenTA8xx10100Eth15MinCurrentRxBroadcastFrames": adGenTA8xx10100Eth15MinCurrentRxBroadcastFrames,
       "adGenTA8xx10100Eth15MinCurrentRxUnicastFrames": adGenTA8xx10100Eth15MinCurrentRxUnicastFrames,
       "adGenTA8xx10100Eth15MinCurrentTxMulticastFrames": adGenTA8xx10100Eth15MinCurrentTxMulticastFrames,
       "adGenTA8xx10100Eth15MinCurrentTxBroadcastFrames": adGenTA8xx10100Eth15MinCurrentTxBroadcastFrames,
       "adGenTA8xx10100Eth15MinCurrentTxUnicastFrames": adGenTA8xx10100Eth15MinCurrentTxUnicastFrames,
       "adGenTA8xx10100Eth15MinCurrentRxGoodBytes": adGenTA8xx10100Eth15MinCurrentRxGoodBytes,
       "adGenTA8xx10100Eth15MinCurrentRxGoodFrames": adGenTA8xx10100Eth15MinCurrentRxGoodFrames,
       "adGenTA8xx10100Eth15MinCurrentRxJabbers": adGenTA8xx10100Eth15MinCurrentRxJabbers,
       "adGenTA8xx10100Eth15MinCurrentRxFragments": adGenTA8xx10100Eth15MinCurrentRxFragments,
       "adGenTA8xx10100Eth15MinIntervalTable": adGenTA8xx10100Eth15MinIntervalTable,
       "adGenTA8xx10100Eth15MinIntervalEntry": adGenTA8xx10100Eth15MinIntervalEntry,
       "adGenTA8xx10100Eth15MinIntervalNumber": adGenTA8xx10100Eth15MinIntervalNumber,
       "adGenTA8xx10100Eth15MinIntervalTxBytes": adGenTA8xx10100Eth15MinIntervalTxBytes,
       "adGenTA8xx10100Eth15MinIntervalTxFrames": adGenTA8xx10100Eth15MinIntervalTxFrames,
       "adGenTA8xx10100Eth15MinIntervalRxBytes": adGenTA8xx10100Eth15MinIntervalRxBytes,
       "adGenTA8xx10100Eth15MinIntervalRxFrames": adGenTA8xx10100Eth15MinIntervalRxFrames,
       "adGenTA8xx10100Eth15MinIntervalRxCRCAlignErrs": adGenTA8xx10100Eth15MinIntervalRxCRCAlignErrs,
       "adGenTA8xx10100Eth15MinIntervalRxUndersizeFrames": adGenTA8xx10100Eth15MinIntervalRxUndersizeFrames,
       "adGenTA8xx10100Eth15MinIntervalRxOversizeFrames": adGenTA8xx10100Eth15MinIntervalRxOversizeFrames,
       "adGenTA8xx10100Eth15MinIntervalRxCollisions": adGenTA8xx10100Eth15MinIntervalRxCollisions,
       "adGenTA8xx10100Eth15MinIntervalRxDiscardedFrames": adGenTA8xx10100Eth15MinIntervalRxDiscardedFrames,
       "adGenTA8xx10100Eth15MinIntervalRxMulticastFrames": adGenTA8xx10100Eth15MinIntervalRxMulticastFrames,
       "adGenTA8xx10100Eth15MinIntervalRxBroadcastFrames": adGenTA8xx10100Eth15MinIntervalRxBroadcastFrames,
       "adGenTA8xx10100Eth15MinIntervalRxUnicastFrames": adGenTA8xx10100Eth15MinIntervalRxUnicastFrames,
       "adGenTA8xx10100Eth15MinIntervalTxMulticastFrames": adGenTA8xx10100Eth15MinIntervalTxMulticastFrames,
       "adGenTA8xx10100Eth15MinIntervalTxBroadcastFrames": adGenTA8xx10100Eth15MinIntervalTxBroadcastFrames,
       "adGenTA8xx10100Eth15MinIntervalTxUnicastFrames": adGenTA8xx10100Eth15MinIntervalTxUnicastFrames,
       "adGenTA8xx10100Eth15MinIntervalRxGoodBytes": adGenTA8xx10100Eth15MinIntervalRxGoodBytes,
       "adGenTA8xx10100Eth15MinIntervalRxGoodFrames": adGenTA8xx10100Eth15MinIntervalRxGoodFrames,
       "adGenTA8xx10100Eth15MinIntervalRxJabbers": adGenTA8xx10100Eth15MinIntervalRxJabbers,
       "adGenTA8xx10100Eth15MinIntervalRxFragments": adGenTA8xx10100Eth15MinIntervalRxFragments,
       "adGenTA8xx10100Eth24HrCurrentTable": adGenTA8xx10100Eth24HrCurrentTable,
       "adGenTA8xx10100Eth24HrCurrentEntry": adGenTA8xx10100Eth24HrCurrentEntry,
       "adGenTA8xx10100Eth24HrCurrentTxBytes": adGenTA8xx10100Eth24HrCurrentTxBytes,
       "adGenTA8xx10100Eth24HrCurrentTxFrames": adGenTA8xx10100Eth24HrCurrentTxFrames,
       "adGenTA8xx10100Eth24HrCurrentRxBytes": adGenTA8xx10100Eth24HrCurrentRxBytes,
       "adGenTA8xx10100Eth24HrCurrentRxFrames": adGenTA8xx10100Eth24HrCurrentRxFrames,
       "adGenTA8xx10100Eth24HrCurrentRxCRCAlignErrs": adGenTA8xx10100Eth24HrCurrentRxCRCAlignErrs,
       "adGenTA8xx10100Eth24HrCurrentRxUndersizeFrames": adGenTA8xx10100Eth24HrCurrentRxUndersizeFrames,
       "adGenTA8xx10100Eth24HrCurrentRxOversizeFrames": adGenTA8xx10100Eth24HrCurrentRxOversizeFrames,
       "adGenTA8xx10100Eth24HrCurrentRxCollisions": adGenTA8xx10100Eth24HrCurrentRxCollisions,
       "adGenTA8xx10100Eth24HrCurrentRxDiscardedFrames": adGenTA8xx10100Eth24HrCurrentRxDiscardedFrames,
       "adGenTA8xx10100Eth24HrCurrentRxMulticastFrames": adGenTA8xx10100Eth24HrCurrentRxMulticastFrames,
       "adGenTA8xx10100Eth24HrCurrentRxBroadcastFrames": adGenTA8xx10100Eth24HrCurrentRxBroadcastFrames,
       "adGenTA8xx10100Eth24HrCurrentRxUnicastFrames": adGenTA8xx10100Eth24HrCurrentRxUnicastFrames,
       "adGenTA8xx10100Eth24HrCurrentTxMulticastFrames": adGenTA8xx10100Eth24HrCurrentTxMulticastFrames,
       "adGenTA8xx10100Eth24HrCurrentTxBroadcastFrames": adGenTA8xx10100Eth24HrCurrentTxBroadcastFrames,
       "adGenTA8xx10100Eth24HrCurrentTxUnicastFrames": adGenTA8xx10100Eth24HrCurrentTxUnicastFrames,
       "adGenTA8xx10100Eth24HrCurrentRxGoodBytes": adGenTA8xx10100Eth24HrCurrentRxGoodBytes,
       "adGenTA8xx10100Eth24HrCurrentRxGoodFrames": adGenTA8xx10100Eth24HrCurrentRxGoodFrames,
       "adGenTA8xx10100Eth24HrCurrentRxJabbers": adGenTA8xx10100Eth24HrCurrentRxJabbers,
       "adGenTA8xx10100Eth24HrCurrentRxFragments": adGenTA8xx10100Eth24HrCurrentRxFragments,
       "adGenTA8xx10100Eth24HrIntervalTable": adGenTA8xx10100Eth24HrIntervalTable,
       "adGenTA8xx10100Eth24HrIntervalEntry": adGenTA8xx10100Eth24HrIntervalEntry,
       "adGenTA8xx10100Eth24HrIntervalNumber": adGenTA8xx10100Eth24HrIntervalNumber,
       "adGenTA8xx10100Eth24HrIntervalTxBytes": adGenTA8xx10100Eth24HrIntervalTxBytes,
       "adGenTA8xx10100Eth24HrIntervalTxFrames": adGenTA8xx10100Eth24HrIntervalTxFrames,
       "adGenTA8xx10100Eth24HrIntervalRxBytes": adGenTA8xx10100Eth24HrIntervalRxBytes,
       "adGenTA8xx10100Eth24HrIntervalRxFrames": adGenTA8xx10100Eth24HrIntervalRxFrames,
       "adGenTA8xx10100Eth24HrIntervalRxCRCAlignErrs": adGenTA8xx10100Eth24HrIntervalRxCRCAlignErrs,
       "adGenTA8xx10100Eth24HrIntervalRxUndersizeFrames": adGenTA8xx10100Eth24HrIntervalRxUndersizeFrames,
       "adGenTA8xx10100Eth24HrIntervalRxOversizeFrames": adGenTA8xx10100Eth24HrIntervalRxOversizeFrames,
       "adGenTA8xx10100Eth24HrIntervalRxCollisions": adGenTA8xx10100Eth24HrIntervalRxCollisions,
       "adGenTA8xx10100Eth24HrIntervalRxDiscardedFrames": adGenTA8xx10100Eth24HrIntervalRxDiscardedFrames,
       "adGenTA8xx10100Eth24HrIntervalRxMulticastFrames": adGenTA8xx10100Eth24HrIntervalRxMulticastFrames,
       "adGenTA8xx10100Eth24HrIntervalRxBroadcastFrames": adGenTA8xx10100Eth24HrIntervalRxBroadcastFrames,
       "adGenTA8xx10100Eth24HrIntervalRxUnicastFrames": adGenTA8xx10100Eth24HrIntervalRxUnicastFrames,
       "adGenTA8xx10100Eth24HrIntervalTxMulticastFrames": adGenTA8xx10100Eth24HrIntervalTxMulticastFrames,
       "adGenTA8xx10100Eth24HrIntervalTxBroadcastFrames": adGenTA8xx10100Eth24HrIntervalTxBroadcastFrames,
       "adGenTA8xx10100Eth24HrIntervalTxUnicastFrames": adGenTA8xx10100Eth24HrIntervalTxUnicastFrames,
       "adGenTA8xx10100Eth24HrIntervalRxGoodBytes": adGenTA8xx10100Eth24HrIntervalRxGoodBytes,
       "adGenTA8xx10100Eth24HrIntervalRxGoodFrames": adGenTA8xx10100Eth24HrIntervalRxGoodFrames,
       "adGenTA8xx10100Eth24HrIntervalRxJabbers": adGenTA8xx10100Eth24HrIntervalRxJabbers,
       "adGenTA8xx10100Eth24HrIntervalRxFragments": adGenTA8xx10100Eth24HrIntervalRxFragments,
       "adGenTA8xx10100EthPerfResetTable": adGenTA8xx10100EthPerfResetTable,
       "adGenTA8xx10100EthPerfResetEntry": adGenTA8xx10100EthPerfResetEntry,
       "adGenTA8xx10100EthPerfReset": adGenTA8xx10100EthPerfReset,
       "adGenTA8xxGigEthPerformance": adGenTA8xxGigEthPerformance,
       "adGenTA8xxGigEthPerformanceScalars": adGenTA8xxGigEthPerformanceScalars,
       "adGenTA8xxGigEthRstCurrentIntervals": adGenTA8xxGigEthRstCurrentIntervals,
       "adGenTA8xxGigEthRstAll": adGenTA8xxGigEthRstAll,
       "adGenTA8xxGigEth15MinCurrentTable": adGenTA8xxGigEth15MinCurrentTable,
       "adGenTA8xxGigEth15MinCurrentEntry": adGenTA8xxGigEth15MinCurrentEntry,
       "adGenTA8xxGigEth15MinCurrentTxBytes": adGenTA8xxGigEth15MinCurrentTxBytes,
       "adGenTA8xxGigEth15MinCurrentTxFrames": adGenTA8xxGigEth15MinCurrentTxFrames,
       "adGenTA8xxGigEth15MinCurrentRxBytes": adGenTA8xxGigEth15MinCurrentRxBytes,
       "adGenTA8xxGigEth15MinCurrentRxFrames": adGenTA8xxGigEth15MinCurrentRxFrames,
       "adGenTA8xxGigEth15MinCurrentRxGoodBytes": adGenTA8xxGigEth15MinCurrentRxGoodBytes,
       "adGenTA8xxGigEth15MinCurrentRxGoodFrames": adGenTA8xxGigEth15MinCurrentRxGoodFrames,
       "adGenTA8xxGigEth15MinCurrentRxFCSErrors": adGenTA8xxGigEth15MinCurrentRxFCSErrors,
       "adGenTA8xxGigEth15MinCurrentRxDroppedFrames": adGenTA8xxGigEth15MinCurrentRxDroppedFrames,
       "adGenTA8xxGigEth15MinCurrentRxFramesTooBig": adGenTA8xxGigEth15MinCurrentRxFramesTooBig,
       "adGenTA8xxGigEth15MinCurrentRxFramesTooSmall": adGenTA8xxGigEth15MinCurrentRxFramesTooSmall,
       "adGenTA8xxGigEth15MinCurrentRxMulticastFrames": adGenTA8xxGigEth15MinCurrentRxMulticastFrames,
       "adGenTA8xxGigEth15MinCurrentRxBroadcastFrames": adGenTA8xxGigEth15MinCurrentRxBroadcastFrames,
       "adGenTA8xxGigEth15MinCurrentRxUnicastFrames": adGenTA8xxGigEth15MinCurrentRxUnicastFrames,
       "adGenTA8xxGigEth15MinCurrentTxMulticastFrames": adGenTA8xxGigEth15MinCurrentTxMulticastFrames,
       "adGenTA8xxGigEth15MinCurrentTxBroadcastFrames": adGenTA8xxGigEth15MinCurrentTxBroadcastFrames,
       "adGenTA8xxGigEth15MinCurrentTxUnicastFrames": adGenTA8xxGigEth15MinCurrentTxUnicastFrames,
       "adGenTA8xxGigEth15MinCurrentRxJabbers": adGenTA8xxGigEth15MinCurrentRxJabbers,
       "adGenTA8xxGigEth15MinCurrentRxFragments": adGenTA8xxGigEth15MinCurrentRxFragments,
       "adGenTA8xxGigEth15MinIntervalTable": adGenTA8xxGigEth15MinIntervalTable,
       "adGenTA8xxGigEth15MinIntervalEntry": adGenTA8xxGigEth15MinIntervalEntry,
       "adGenTA8xxGigEth15MinIntervalNumber": adGenTA8xxGigEth15MinIntervalNumber,
       "adGenTA8xxGigEth15MinIntervalTxBytes": adGenTA8xxGigEth15MinIntervalTxBytes,
       "adGenTA8xxGigEth15MinIntervalTxFrames": adGenTA8xxGigEth15MinIntervalTxFrames,
       "adGenTA8xxGigEth15MinIntervalRxBytes": adGenTA8xxGigEth15MinIntervalRxBytes,
       "adGenTA8xxGigEth15MinIntervalRxFrames": adGenTA8xxGigEth15MinIntervalRxFrames,
       "adGenTA8xxGigEth15MinIntervalRxGoodBytes": adGenTA8xxGigEth15MinIntervalRxGoodBytes,
       "adGenTA8xxGigEth15MinIntervalRxGoodFrames": adGenTA8xxGigEth15MinIntervalRxGoodFrames,
       "adGenTA8xxGigEth15MinIntervalRxFCSErrors": adGenTA8xxGigEth15MinIntervalRxFCSErrors,
       "adGenTA8xxGigEth15MinIntervalRxDroppedFrames": adGenTA8xxGigEth15MinIntervalRxDroppedFrames,
       "adGenTA8xxGigEth15MinIntervalRxFramesTooBig": adGenTA8xxGigEth15MinIntervalRxFramesTooBig,
       "adGenTA8xxGigEth15MinIntervalRxFramesTooSmall": adGenTA8xxGigEth15MinIntervalRxFramesTooSmall,
       "adGenTA8xxGigEth15MinIntervalRxMulticastFrames": adGenTA8xxGigEth15MinIntervalRxMulticastFrames,
       "adGenTA8xxGigEth15MinIntervalRxBroadcastFrames": adGenTA8xxGigEth15MinIntervalRxBroadcastFrames,
       "adGenTA8xxGigEth15MinIntervalRxUnicastFrames": adGenTA8xxGigEth15MinIntervalRxUnicastFrames,
       "adGenTA8xxGigEth15MinIntervalTxMulticastFrames": adGenTA8xxGigEth15MinIntervalTxMulticastFrames,
       "adGenTA8xxGigEth15MinIntervalTxBroadcastFrames": adGenTA8xxGigEth15MinIntervalTxBroadcastFrames,
       "adGenTA8xxGigEth15MinIntervalTxUnicastFrames": adGenTA8xxGigEth15MinIntervalTxUnicastFrames,
       "adGenTA8xxGigEth15MinIntervalRxJabbers": adGenTA8xxGigEth15MinIntervalRxJabbers,
       "adGenTA8xxGigEth15MinIntervalRxFragments": adGenTA8xxGigEth15MinIntervalRxFragments,
       "adGenTA8xxGigEth24HrCurrentTable": adGenTA8xxGigEth24HrCurrentTable,
       "adGenTA8xxGigEth24HrCurrentEntry": adGenTA8xxGigEth24HrCurrentEntry,
       "adGenTA8xxGigEth24HrCurrentTxBytes": adGenTA8xxGigEth24HrCurrentTxBytes,
       "adGenTA8xxGigEth24HrCurrentTxFrames": adGenTA8xxGigEth24HrCurrentTxFrames,
       "adGenTA8xxGigEth24HrCurrentRxBytes": adGenTA8xxGigEth24HrCurrentRxBytes,
       "adGenTA8xxGigEth24HrCurrentRxFrames": adGenTA8xxGigEth24HrCurrentRxFrames,
       "adGenTA8xxGigEth24HrCurrentRxGoodBytes": adGenTA8xxGigEth24HrCurrentRxGoodBytes,
       "adGenTA8xxGigEth24HrCurrentRxGoodFrames": adGenTA8xxGigEth24HrCurrentRxGoodFrames,
       "adGenTA8xxGigEth24HrCurrentRxFCSErrors": adGenTA8xxGigEth24HrCurrentRxFCSErrors,
       "adGenTA8xxGigEth24HrCurrentRxDroppedFrames": adGenTA8xxGigEth24HrCurrentRxDroppedFrames,
       "adGenTA8xxGigEth24HrCurrentRxFramesTooBig": adGenTA8xxGigEth24HrCurrentRxFramesTooBig,
       "adGenTA8xxGigEth24HrCurrentRxFramesTooSmall": adGenTA8xxGigEth24HrCurrentRxFramesTooSmall,
       "adGenTA8xxGigEth24HrCurrentRxMulticastFrames": adGenTA8xxGigEth24HrCurrentRxMulticastFrames,
       "adGenTA8xxGigEth24HrCurrentRxBroadcastFrames": adGenTA8xxGigEth24HrCurrentRxBroadcastFrames,
       "adGenTA8xxGigEth24HrCurrentRxUnicastFrames": adGenTA8xxGigEth24HrCurrentRxUnicastFrames,
       "adGenTA8xxGigEth24HrCurrentTxMulticastFrames": adGenTA8xxGigEth24HrCurrentTxMulticastFrames,
       "adGenTA8xxGigEth24HrCurrentTxBroadcastFrames": adGenTA8xxGigEth24HrCurrentTxBroadcastFrames,
       "adGenTA8xxGigEth24HrCurrentTxUnicastFrames": adGenTA8xxGigEth24HrCurrentTxUnicastFrames,
       "adGenTA8xxGigEth24HrCurrentRxJabbers": adGenTA8xxGigEth24HrCurrentRxJabbers,
       "adGenTA8xxGigEth24HrCurrentRxFragments": adGenTA8xxGigEth24HrCurrentRxFragments,
       "adGenTA8xxGigEth24HrIntervalTable": adGenTA8xxGigEth24HrIntervalTable,
       "adGenTA8xxGigEth24HrIntervalEntry": adGenTA8xxGigEth24HrIntervalEntry,
       "adGenTA8xxGigEth24HrIntervalNumber": adGenTA8xxGigEth24HrIntervalNumber,
       "adGenTA8xxGigEth24HrIntervalTxBytes": adGenTA8xxGigEth24HrIntervalTxBytes,
       "adGenTA8xxGigEth24HrIntervalTxFrames": adGenTA8xxGigEth24HrIntervalTxFrames,
       "adGenTA8xxGigEth24HrIntervalRxBytes": adGenTA8xxGigEth24HrIntervalRxBytes,
       "adGenTA8xxGigEth24HrIntervalRxFrames": adGenTA8xxGigEth24HrIntervalRxFrames,
       "adGenTA8xxGigEth24HrIntervalRxGoodBytes": adGenTA8xxGigEth24HrIntervalRxGoodBytes,
       "adGenTA8xxGigEth24HrIntervalRxGoodFrames": adGenTA8xxGigEth24HrIntervalRxGoodFrames,
       "adGenTA8xxGigEth24HrIntervalRxFCSErrors": adGenTA8xxGigEth24HrIntervalRxFCSErrors,
       "adGenTA8xxGigEth24HrIntervalRxDroppedFrames": adGenTA8xxGigEth24HrIntervalRxDroppedFrames,
       "adGenTA8xxGigEth24HrIntervalRxFramesTooBig": adGenTA8xxGigEth24HrIntervalRxFramesTooBig,
       "adGenTA8xxGigEth24HrIntervalRxFramesTooSmall": adGenTA8xxGigEth24HrIntervalRxFramesTooSmall,
       "adGenTA8xxGigEth24HrIntervalRxMulticastFrames": adGenTA8xxGigEth24HrIntervalRxMulticastFrames,
       "adGenTA8xxGigEth24HrIntervalRxBroadcastFrames": adGenTA8xxGigEth24HrIntervalRxBroadcastFrames,
       "adGenTA8xxGigEth24HrIntervalRxUnicastFrames": adGenTA8xxGigEth24HrIntervalRxUnicastFrames,
       "adGenTA8xxGigEth24HrIntervalTxMulticastFrames": adGenTA8xxGigEth24HrIntervalTxMulticastFrames,
       "adGenTA8xxGigEth24HrIntervalTxBroadcastFrames": adGenTA8xxGigEth24HrIntervalTxBroadcastFrames,
       "adGenTA8xxGigEth24HrIntervalTxUnicastFrames": adGenTA8xxGigEth24HrIntervalTxUnicastFrames,
       "adGenTA8xxGigEth24HrIntervalRxJabbers": adGenTA8xxGigEth24HrIntervalRxJabbers,
       "adGenTA8xxGigEth24HrIntervalRxFragments": adGenTA8xxGigEth24HrIntervalRxFragments,
       "adGenTA8xxGigEthPerfResetTable": adGenTA8xxGigEthPerfResetTable,
       "adGenTA8xxGigEthPerfResetEntry": adGenTA8xxGigEthPerfResetEntry,
       "adGenTA8xxGigEthPerfReset": adGenTA8xxGigEthPerfReset,
       "adGenTA8xx10100EthPerfThresholds": adGenTA8xx10100EthPerfThresholds,
       "adGenTA8xx10100Eth15MinThreshTable": adGenTA8xx10100Eth15MinThreshTable,
       "adGenTA8xx10100Eth15MinThreshEntry": adGenTA8xx10100Eth15MinThreshEntry,
       "adGenTA8xx10100Eth15MinThreshRxCRCAlignErrs": adGenTA8xx10100Eth15MinThreshRxCRCAlignErrs,
       "adGenTA8xx10100Eth15MinThreshRxUndersizeFrames": adGenTA8xx10100Eth15MinThreshRxUndersizeFrames,
       "adGenTA8xx10100Eth15MinThreshRxOversizeFrames": adGenTA8xx10100Eth15MinThreshRxOversizeFrames,
       "adGenTA8xx10100Eth15MinThreshRxCollisions": adGenTA8xx10100Eth15MinThreshRxCollisions,
       "adGenTA8xx10100Eth15MinThreshRxDiscardedFrames": adGenTA8xx10100Eth15MinThreshRxDiscardedFrames,
       "adGenTA8xx10100Eth15MinThreshRxMulticastFrames": adGenTA8xx10100Eth15MinThreshRxMulticastFrames,
       "adGenTA8xx10100Eth15MinThreshRxBroadcastFrames": adGenTA8xx10100Eth15MinThreshRxBroadcastFrames,
       "adGenTA8xx10100Eth15MinThreshRxJabbers": adGenTA8xx10100Eth15MinThreshRxJabbers,
       "adGenTA8xx10100Eth15MinThreshRxFragments": adGenTA8xx10100Eth15MinThreshRxFragments,
       "adGenTA8xx10100Eth24HrThreshTable": adGenTA8xx10100Eth24HrThreshTable,
       "adGenTA8xx10100Eth24HrThreshEntry": adGenTA8xx10100Eth24HrThreshEntry,
       "adGenTA8xx10100Eth24HrThreshRxCRCAlignErrs": adGenTA8xx10100Eth24HrThreshRxCRCAlignErrs,
       "adGenTA8xx10100Eth24HrThreshRxUndersizeFrames": adGenTA8xx10100Eth24HrThreshRxUndersizeFrames,
       "adGenTA8xx10100Eth24HrThreshRxOversizeFrames": adGenTA8xx10100Eth24HrThreshRxOversizeFrames,
       "adGenTA8xx10100Eth24HrThreshRxCollisions": adGenTA8xx10100Eth24HrThreshRxCollisions,
       "adGenTA8xx10100Eth24HrThreshRxDiscardedFrames": adGenTA8xx10100Eth24HrThreshRxDiscardedFrames,
       "adGenTA8xx10100Eth24HrThreshRxMulticastFrames": adGenTA8xx10100Eth24HrThreshRxMulticastFrames,
       "adGenTA8xx10100Eth24HrThreshRxBroadcastFrames": adGenTA8xx10100Eth24HrThreshRxBroadcastFrames,
       "adGenTA8xx10100Eth24HrThreshRxJabbers": adGenTA8xx10100Eth24HrThreshRxJabbers,
       "adGenTA8xx10100Eth24HrThreshRxFragments": adGenTA8xx10100Eth24HrThreshRxFragments,
       "adGenTA8xxGigEthPerfThresholds": adGenTA8xxGigEthPerfThresholds,
       "adGenTA8xxGigEth15MinThreshTable": adGenTA8xxGigEth15MinThreshTable,
       "adGenTA8xxGigEth15MinThreshEntry": adGenTA8xxGigEth15MinThreshEntry,
       "adGenTA8xxGigEth15MinThreshRxFCSErrors": adGenTA8xxGigEth15MinThreshRxFCSErrors,
       "adGenTA8xxGigEth15MinThreshRxDroppedFrames": adGenTA8xxGigEth15MinThreshRxDroppedFrames,
       "adGenTA8xxGigEth15MinThreshRxFramesTooBig": adGenTA8xxGigEth15MinThreshRxFramesTooBig,
       "adGenTA8xxGigEth15MinThreshRxFramesTooSmall": adGenTA8xxGigEth15MinThreshRxFramesTooSmall,
       "adGenTA8xxGigEth15MinThreshRxMulticastFrames": adGenTA8xxGigEth15MinThreshRxMulticastFrames,
       "adGenTA8xxGigEth15MinThreshRxBroadcastFrames": adGenTA8xxGigEth15MinThreshRxBroadcastFrames,
       "adGenTA8xxGigEth15MinThreshRxJabbers": adGenTA8xxGigEth15MinThreshRxJabbers,
       "adGenTA8xxGigEth15MinThreshRxFragments": adGenTA8xxGigEth15MinThreshRxFragments,
       "adGenTA8xxGigEth24HrThreshTable": adGenTA8xxGigEth24HrThreshTable,
       "adGenTA8xxGigEth24HrThreshEntry": adGenTA8xxGigEth24HrThreshEntry,
       "adGenTA8xxGigEth24HrThreshRxFCSErrors": adGenTA8xxGigEth24HrThreshRxFCSErrors,
       "adGenTA8xxGigEth24HrThreshRxDroppedFrames": adGenTA8xxGigEth24HrThreshRxDroppedFrames,
       "adGenTA8xxGigEth24HrThreshRxFramesTooBig": adGenTA8xxGigEth24HrThreshRxFramesTooBig,
       "adGenTA8xxGigEth24HrThreshRxFramesTooSmall": adGenTA8xxGigEth24HrThreshRxFramesTooSmall,
       "adGenTA8xxGigEth24HrThreshRxMulticastFrames": adGenTA8xxGigEth24HrThreshRxMulticastFrames,
       "adGenTA8xxGigEth24HrThreshRxBroadcastFrames": adGenTA8xxGigEth24HrThreshRxBroadcastFrames,
       "adGenTA8xxGigEth24HrThreshRxJabbers": adGenTA8xxGigEth24HrThreshRxJabbers,
       "adGenTA8xxGigEth24HrThreshRxFragments": adGenTA8xxGigEth24HrThreshRxFragments,
       "adGenTA8xxTest": adGenTA8xxTest,
       "adGenTA8xxTstScalars": adGenTA8xxTstScalars,
       "adGenTA8xxResetTests": adGenTA8xxResetTests,
       "adGenTA8xxTestTimeout": adGenTA8xxTestTimeout,
       "adGenTA8xxRelayTest": adGenTA8xxRelayTest,
       "adGenTA8xxTestCriticalRelay": adGenTA8xxTestCriticalRelay,
       "adGenTA8xxTestMajorRelay": adGenTA8xxTestMajorRelay,
       "adGenTA8xxTestMinorRelay": adGenTA8xxTestMinorRelay,
       "adGenTA8xxTstBertPrvTable": adGenTA8xxTstBertPrvTable,
       "adGenTA8xxTstBertPrvEntry": adGenTA8xxTstBertPrvEntry,
       "adGenTA8xxTstBertStartAndStop": adGenTA8xxTstBertStartAndStop,
       "adGenTA8xxTstBertResetStatistics": adGenTA8xxTstBertResetStatistics,
       "adGenTA8xxTstBertPattern": adGenTA8xxTstBertPattern,
       "adGenTA8xxTstBertPatternPolarity": adGenTA8xxTstBertPatternPolarity,
       "adGenTA8xxTstBertErrorInject": adGenTA8xxTstBertErrorInject,
       "adGenTA8xxTstBertStatTable": adGenTA8xxTstBertStatTable,
       "adGenTA8xxTstBertStatEntry": adGenTA8xxTstBertStatEntry,
       "adGenTA8xxTstBertStatus": adGenTA8xxTstBertStatus,
       "adGenTA8xxTstBertBER": adGenTA8xxTstBertBER,
       "adGenTA8xxTstBertErrorCount": adGenTA8xxTstBertErrorCount,
       "adGenTA8xxTstBertPattSyncLossCount": adGenTA8xxTstBertPattSyncLossCount,
       "adGenTA8xxTstBertErroredSeconds": adGenTA8xxTstBertErroredSeconds,
       "adGenTA8xxTstBertElapsedTime": adGenTA8xxTstBertElapsedTime,
       "adGenTA8xxTstLpbkPrvTable": adGenTA8xxTstLpbkPrvTable,
       "adGenTA8xxTstLpbkPrvEntry": adGenTA8xxTstLpbkPrvEntry,
       "adGenTA8xxTstIncomingLoopbackPatterns": adGenTA8xxTstIncomingLoopbackPatterns,
       "adGenTA8xxTstRequestRemoteLoopback": adGenTA8xxTstRequestRemoteLoopback,
       "adGenTA8xxTstIncomingInbandLoopbackPatterns": adGenTA8xxTstIncomingInbandLoopbackPatterns,
       "adGenTA8xxTstIncomingFDLLoopbackPatterns": adGenTA8xxTstIncomingFDLLoopbackPatterns,
       "adGenTA8xxAlarms": adGenTA8xxAlarms,
       "adGenTA8xxAlarmScalars": adGenTA8xxAlarmScalars,
       "adGenTA8xxTrapAlarmLevel": adGenTA8xxTrapAlarmLevel,
       "adGenTA8xxACPwrInLevel": adGenTA8xxACPwrInLevel,
       "adGenTA8xxPwrALevel": adGenTA8xxPwrALevel,
       "adGenTA8xxPwrBLevel": adGenTA8xxPwrBLevel,
       "adGenTA8xxAcknowledgeAlarms": adGenTA8xxAcknowledgeAlarms,
       "adGenTA8xxSpecificTrapEnable": adGenTA8xxSpecificTrapEnable,
       "adGenTA8xxLoginFailureLevel": adGenTA8xxLoginFailureLevel,
       "adGenTA8xxLoginSuccessLevel": adGenTA8xxLoginSuccessLevel,
       "adGenTA8xxMibConformance": adGenTA8xxMibConformance,
       "adGenTA8xxMibGroups": adGenTA8xxMibGroups,
       "adGenTA8xxConfigGroup": adGenTA8xxConfigGroup,
       "adGenTA8xxCardProvGroup": adGenTA8xxCardProvGroup,
       "adGenTA8xx10100EthProvGroup": adGenTA8xx10100EthProvGroup,
       "adGenTA8xxGigEthProvGroup": adGenTA8xxGigEthProvGroup,
       "adGenTA8xxCardStatusGroup": adGenTA8xxCardStatusGroup,
       "adGenTA8xx10100EthStatusGroup": adGenTA8xx10100EthStatusGroup,
       "adGenTA8xxGigEthStatusGroup": adGenTA8xxGigEthStatusGroup,
       "adGenTA8xxCardPerfGroup": adGenTA8xxCardPerfGroup,
       "adGenTA8xx10100EthRstPerfGroup": adGenTA8xx10100EthRstPerfGroup,
       "adGenTA8xx10100EthCurr15MinPerfGroup": adGenTA8xx10100EthCurr15MinPerfGroup,
       "adGenTA8xx10100EthInt15MinPerfGroup": adGenTA8xx10100EthInt15MinPerfGroup,
       "adGenTA8xx10100EthCurr24HrPerfGroup": adGenTA8xx10100EthCurr24HrPerfGroup,
       "adGenTA8xx10100EthInt24HrPerfGroup": adGenTA8xx10100EthInt24HrPerfGroup,
       "adGenTA8xxGigEthRstPerfGroup": adGenTA8xxGigEthRstPerfGroup,
       "adGenTA8xxGigEthCurr15MinPerfGroup": adGenTA8xxGigEthCurr15MinPerfGroup,
       "adGenTA8xxGigEthInt15MinPerfGroup": adGenTA8xxGigEthInt15MinPerfGroup,
       "adGenTA8xxGigEthCurr24HrPerfGroup": adGenTA8xxGigEthCurr24HrPerfGroup,
       "adGenTA8xxGigEthInt24HrPerfGroup": adGenTA8xxGigEthInt24HrPerfGroup,
       "adGenTA8xxTestGroup": adGenTA8xxTestGroup,
       "adGenTA8xxAlarmGroup": adGenTA8xxAlarmGroup,
       "adGenTA8xxEventGroup": adGenTA8xxEventGroup,
       "adGenTA8xxFarEndConfigGroup": adGenTA8xxFarEndConfigGroup,
       "adGenTA8xx10100EthThreshGroup": adGenTA8xx10100EthThreshGroup,
       "adGenTA8xxGigEthThreshGroup": adGenTA8xxGigEthThreshGroup,
       "adGenTA8xxBertPrvGroup": adGenTA8xxBertPrvGroup,
       "adGenTA8xxBertStatGroup": adGenTA8xxBertStatGroup,
       "adGenTA8xxTstLpbkPrvGroup": adGenTA8xxTstLpbkPrvGroup,
       "adGenTA8xxMgmtStatsGroup": adGenTA8xxMgmtStatsGroup,
       "adGenTA8xxDeprecatedGroup": adGenTA8xxDeprecatedGroup,
       "adGenTA8xxMIB": adGenTA8xxMIB}
)
