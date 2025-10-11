# SNMP MIB module (ARRIS-SPEED-TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-SPEED-TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:09:26 2025
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

(arrisProdIdCM,) = mibBuilder.importSymbols(
    "ARRIS-MIB",
    "arrisProdIdCM")

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

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
 TextualConvention,
 TimeInterval,
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TimeInterval",
    "TimeStamp",
    "TruthValue")


# MODULE-IDENTITY

arrisSpeedTestMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6)
)
if mibBuilder.loadTexts:
    arrisSpeedTestMib.setRevisions(
        ("1911-08-09 00:00",
         "1911-07-26 00:00",
         "1910-07-16 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ArrisSpeedTestMibObjects_ObjectIdentity = ObjectIdentity
arrisSpeedTestMibObjects = _ArrisSpeedTestMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1)
)
_ArrisSpeedTestConfig_ObjectIdentity = ObjectIdentity
arrisSpeedTestConfig = _ArrisSpeedTestConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 1)
)


class _ArrisSpeedTestConfigDownlinkURL_Type(OctetString):
    """Custom type arrisSpeedTestConfigDownlinkURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ArrisSpeedTestConfigDownlinkURL_Type.__name__ = "OctetString"
_ArrisSpeedTestConfigDownlinkURL_Object = MibScalar
arrisSpeedTestConfigDownlinkURL = _ArrisSpeedTestConfigDownlinkURL_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 1, 1),
    _ArrisSpeedTestConfigDownlinkURL_Type()
)
arrisSpeedTestConfigDownlinkURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisSpeedTestConfigDownlinkURL.setStatus("current")


class _ArrisSpeedTestConfigUplinkURL_Type(OctetString):
    """Custom type arrisSpeedTestConfigUplinkURL based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ArrisSpeedTestConfigUplinkURL_Type.__name__ = "OctetString"
_ArrisSpeedTestConfigUplinkURL_Object = MibScalar
arrisSpeedTestConfigUplinkURL = _ArrisSpeedTestConfigUplinkURL_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 1, 2),
    _ArrisSpeedTestConfigUplinkURL_Type()
)
arrisSpeedTestConfigUplinkURL.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisSpeedTestConfigUplinkURL.setStatus("current")
_ArrisSpeedTestConfigEndUserGui_Type = TruthValue
_ArrisSpeedTestConfigEndUserGui_Object = MibScalar
arrisSpeedTestConfigEndUserGui = _ArrisSpeedTestConfigEndUserGui_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 1, 3),
    _ArrisSpeedTestConfigEndUserGui_Type()
)
arrisSpeedTestConfigEndUserGui.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisSpeedTestConfigEndUserGui.setStatus("current")
_ArrisSpeedTestConfigSyslogReports_Type = TruthValue
_ArrisSpeedTestConfigSyslogReports_Object = MibScalar
arrisSpeedTestConfigSyslogReports = _ArrisSpeedTestConfigSyslogReports_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 1, 4),
    _ArrisSpeedTestConfigSyslogReports_Type()
)
arrisSpeedTestConfigSyslogReports.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisSpeedTestConfigSyslogReports.setStatus("current")
_ArrisSpeedTestConfigCpeAccess_Type = TruthValue
_ArrisSpeedTestConfigCpeAccess_Object = MibScalar
arrisSpeedTestConfigCpeAccess = _ArrisSpeedTestConfigCpeAccess_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 1, 5),
    _ArrisSpeedTestConfigCpeAccess_Type()
)
arrisSpeedTestConfigCpeAccess.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisSpeedTestConfigCpeAccess.setStatus("current")


class _ArrisSpeedTestConfigStartStopTest_Type(Integer32):
    """Custom type arrisSpeedTestConfigStartStopTest based on Integer32"""
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
        *(("stopTest", 0),
          ("startDownlinkTest", 1),
          ("startUplinkTest", 2),
          ("startDownlinkUplinkTest", 3))
    )


_ArrisSpeedTestConfigStartStopTest_Type.__name__ = "Integer32"
_ArrisSpeedTestConfigStartStopTest_Object = MibScalar
arrisSpeedTestConfigStartStopTest = _ArrisSpeedTestConfigStartStopTest_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 1, 6),
    _ArrisSpeedTestConfigStartStopTest_Type()
)
arrisSpeedTestConfigStartStopTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    arrisSpeedTestConfigStartStopTest.setStatus("current")
_ArrisSpeedTestResultsTable_Object = MibTable
arrisSpeedTestResultsTable = _ArrisSpeedTestResultsTable_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 2)
)
if mibBuilder.loadTexts:
    arrisSpeedTestResultsTable.setStatus("current")
_ArrisSpeedTestResultsEntry_Object = MibTableRow
arrisSpeedTestResultsEntry = _ArrisSpeedTestResultsEntry_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 2, 1)
)
arrisSpeedTestResultsEntry.setIndexNames(
    (0, "ARRIS-SPEED-TEST-MIB", "arrisSpeedTestResultsIndex"),
)
if mibBuilder.loadTexts:
    arrisSpeedTestResultsEntry.setStatus("current")


class _ArrisSpeedTestResultsIndex_Type(Integer32):
    """Custom type arrisSpeedTestResultsIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ArrisSpeedTestResultsIndex_Type.__name__ = "Integer32"
_ArrisSpeedTestResultsIndex_Object = MibTableColumn
arrisSpeedTestResultsIndex = _ArrisSpeedTestResultsIndex_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 2, 1, 1),
    _ArrisSpeedTestResultsIndex_Type()
)
arrisSpeedTestResultsIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    arrisSpeedTestResultsIndex.setStatus("current")


class _ArrisSpeedTestResultsStatus_Type(OctetString):
    """Custom type arrisSpeedTestResultsStatus based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 512),
    )


_ArrisSpeedTestResultsStatus_Type.__name__ = "OctetString"
_ArrisSpeedTestResultsStatus_Object = MibTableColumn
arrisSpeedTestResultsStatus = _ArrisSpeedTestResultsStatus_Object(
    (1, 3, 6, 1, 4, 1, 4115, 1, 3, 6, 1, 2, 1, 2),
    _ArrisSpeedTestResultsStatus_Type()
)
arrisSpeedTestResultsStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    arrisSpeedTestResultsStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-SPEED-TEST-MIB",
    **{"arrisSpeedTestMib": arrisSpeedTestMib,
       "arrisSpeedTestMibObjects": arrisSpeedTestMibObjects,
       "arrisSpeedTestConfig": arrisSpeedTestConfig,
       "arrisSpeedTestConfigDownlinkURL": arrisSpeedTestConfigDownlinkURL,
       "arrisSpeedTestConfigUplinkURL": arrisSpeedTestConfigUplinkURL,
       "arrisSpeedTestConfigEndUserGui": arrisSpeedTestConfigEndUserGui,
       "arrisSpeedTestConfigSyslogReports": arrisSpeedTestConfigSyslogReports,
       "arrisSpeedTestConfigCpeAccess": arrisSpeedTestConfigCpeAccess,
       "arrisSpeedTestConfigStartStopTest": arrisSpeedTestConfigStartStopTest,
       "arrisSpeedTestResultsTable": arrisSpeedTestResultsTable,
       "arrisSpeedTestResultsEntry": arrisSpeedTestResultsEntry,
       "arrisSpeedTestResultsIndex": arrisSpeedTestResultsIndex,
       "arrisSpeedTestResultsStatus": arrisSpeedTestResultsStatus}
)
