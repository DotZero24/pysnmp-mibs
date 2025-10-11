# SNMP MIB module (ADTRAN-GEN-SELTDELT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-SELTDELT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:29:49 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adGenXdsl,
 adGenXdslID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-XDSL-MIB",
    "adGenXdsl",
    "adGenXdslID")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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

adGenSeltDeltMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 73, 1, 1)
)
if mibBuilder.loadTexts:
    adGenSeltDeltMIB.setRevisions(
        ("2013-12-03 00:00",
         "2008-07-17 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenSeltDelt_ObjectIdentity = ObjectIdentity
adGenSeltDelt = _AdGenSeltDelt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1)
)
_AdGenSeltDeltTable_Object = MibTable
adGenSeltDeltTable = _AdGenSeltDeltTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenSeltDeltTable.setStatus("current")
_AdGenSeltDeltEntry_Object = MibTableRow
adGenSeltDeltEntry = _AdGenSeltDeltEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1)
)
adGenSeltDeltEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenSeltDeltEntry.setStatus("current")


class _AdGenSeltDeltTestPortNumber_Type(Integer32):
    """Custom type adGenSeltDeltTestPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AdGenSeltDeltTestPortNumber_Type.__name__ = "Integer32"
_AdGenSeltDeltTestPortNumber_Object = MibTableColumn
adGenSeltDeltTestPortNumber = _AdGenSeltDeltTestPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1, 1),
    _AdGenSeltDeltTestPortNumber_Type()
)
adGenSeltDeltTestPortNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSeltDeltTestPortNumber.setStatus("current")
_AdGenSeltDeltTestFilename_Type = DisplayString
_AdGenSeltDeltTestFilename_Object = MibTableColumn
adGenSeltDeltTestFilename = _AdGenSeltDeltTestFilename_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1, 2),
    _AdGenSeltDeltTestFilename_Type()
)
adGenSeltDeltTestFilename.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSeltDeltTestFilename.setStatus("current")


class _AdGenSeltDeltStartSELTTest_Type(Integer32):
    """Custom type adGenSeltDeltStartSELTTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_AdGenSeltDeltStartSELTTest_Type.__name__ = "Integer32"
_AdGenSeltDeltStartSELTTest_Object = MibTableColumn
adGenSeltDeltStartSELTTest = _AdGenSeltDeltStartSELTTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1, 3),
    _AdGenSeltDeltStartSELTTest_Type()
)
adGenSeltDeltStartSELTTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSeltDeltStartSELTTest.setStatus("current")


class _AdGenSeltDeltStartDELTTest_Type(Integer32):
    """Custom type adGenSeltDeltStartDELTTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("start", 1)
    )


_AdGenSeltDeltStartDELTTest_Type.__name__ = "Integer32"
_AdGenSeltDeltStartDELTTest_Object = MibTableColumn
adGenSeltDeltStartDELTTest = _AdGenSeltDeltStartDELTTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1, 4),
    _AdGenSeltDeltStartDELTTest_Type()
)
adGenSeltDeltStartDELTTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSeltDeltStartDELTTest.setStatus("current")


class _AdGenSeltDeltStopTest_Type(Integer32):
    """Custom type adGenSeltDeltStopTest based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("stop", 1)
    )


_AdGenSeltDeltStopTest_Type.__name__ = "Integer32"
_AdGenSeltDeltStopTest_Object = MibTableColumn
adGenSeltDeltStopTest = _AdGenSeltDeltStopTest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1, 5),
    _AdGenSeltDeltStopTest_Type()
)
adGenSeltDeltStopTest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSeltDeltStopTest.setStatus("current")
_AdGenSeltDeltCurrentTestStatus_Type = DisplayString
_AdGenSeltDeltCurrentTestStatus_Object = MibTableColumn
adGenSeltDeltCurrentTestStatus = _AdGenSeltDeltCurrentTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1, 6),
    _AdGenSeltDeltCurrentTestStatus_Type()
)
adGenSeltDeltCurrentTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSeltDeltCurrentTestStatus.setStatus("current")
_AdGenSeltDeltLastTestStatus_Type = DisplayString
_AdGenSeltDeltLastTestStatus_Object = MibTableColumn
adGenSeltDeltLastTestStatus = _AdGenSeltDeltLastTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1, 7),
    _AdGenSeltDeltLastTestStatus_Type()
)
adGenSeltDeltLastTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSeltDeltLastTestStatus.setStatus("current")


class _AdGenSeltDeltRetrieveData_Type(Integer32):
    """Custom type adGenSeltDeltRetrieveData based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("beginTransfer", 1)
    )


_AdGenSeltDeltRetrieveData_Type.__name__ = "Integer32"
_AdGenSeltDeltRetrieveData_Object = MibTableColumn
adGenSeltDeltRetrieveData = _AdGenSeltDeltRetrieveData_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1, 8),
    _AdGenSeltDeltRetrieveData_Type()
)
adGenSeltDeltRetrieveData.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSeltDeltRetrieveData.setStatus("current")


class _AdGenSeltDeltEnumTestStatus_Type(Integer32):
    """Custom type adGenSeltDeltEnumTestStatus based on Integer32"""
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
        *(("idle", 1),
          ("active", 2),
          ("collectingData", 3),
          ("dataAvailable", 4),
          ("testFailed", 5))
    )


_AdGenSeltDeltEnumTestStatus_Type.__name__ = "Integer32"
_AdGenSeltDeltEnumTestStatus_Object = MibTableColumn
adGenSeltDeltEnumTestStatus = _AdGenSeltDeltEnumTestStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1, 9),
    _AdGenSeltDeltEnumTestStatus_Type()
)
adGenSeltDeltEnumTestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenSeltDeltEnumTestStatus.setStatus("current")
_AdGenSeltDeltTestRemoteDevice_Type = InterfaceIndex
_AdGenSeltDeltTestRemoteDevice_Object = MibTableColumn
adGenSeltDeltTestRemoteDevice = _AdGenSeltDeltTestRemoteDevice_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 1, 1, 1, 10),
    _AdGenSeltDeltTestRemoteDevice_Type()
)
adGenSeltDeltTestRemoteDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenSeltDeltTestRemoteDevice.setStatus("current")
_AdGenXdslMibConformance_ObjectIdentity = ObjectIdentity
adGenXdslMibConformance = _AdGenXdslMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 2)
)
_AdGenXdslMibGroups_ObjectIdentity = ObjectIdentity
adGenXdslMibGroups = _AdGenXdslMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 2, 1)
)

# Managed Objects groups

adGenXdslSeltDeltGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 73, 1, 2, 1, 1)
)
adGenXdslSeltDeltGroup.setObjects(
      *(("ADTRAN-GEN-SELTDELT-MIB", "adGenSeltDeltTestPortNumber"),
        ("ADTRAN-GEN-SELTDELT-MIB", "adGenSeltDeltTestFilename"),
        ("ADTRAN-GEN-SELTDELT-MIB", "adGenSeltDeltStartSELTTest"),
        ("ADTRAN-GEN-SELTDELT-MIB", "adGenSeltDeltStartDELTTest"),
        ("ADTRAN-GEN-SELTDELT-MIB", "adGenSeltDeltStopTest"),
        ("ADTRAN-GEN-SELTDELT-MIB", "adGenSeltDeltCurrentTestStatus"),
        ("ADTRAN-GEN-SELTDELT-MIB", "adGenSeltDeltLastTestStatus"),
        ("ADTRAN-GEN-SELTDELT-MIB", "adGenSeltDeltRetrieveData"),
        ("ADTRAN-GEN-SELTDELT-MIB", "adGenSeltDeltEnumTestStatus"),
        ("ADTRAN-GEN-SELTDELT-MIB", "adGenSeltDeltTestRemoteDevice"))
)
if mibBuilder.loadTexts:
    adGenXdslSeltDeltGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-SELTDELT-MIB",
    **{"adGenSeltDelt": adGenSeltDelt,
       "adGenSeltDeltTable": adGenSeltDeltTable,
       "adGenSeltDeltEntry": adGenSeltDeltEntry,
       "adGenSeltDeltTestPortNumber": adGenSeltDeltTestPortNumber,
       "adGenSeltDeltTestFilename": adGenSeltDeltTestFilename,
       "adGenSeltDeltStartSELTTest": adGenSeltDeltStartSELTTest,
       "adGenSeltDeltStartDELTTest": adGenSeltDeltStartDELTTest,
       "adGenSeltDeltStopTest": adGenSeltDeltStopTest,
       "adGenSeltDeltCurrentTestStatus": adGenSeltDeltCurrentTestStatus,
       "adGenSeltDeltLastTestStatus": adGenSeltDeltLastTestStatus,
       "adGenSeltDeltRetrieveData": adGenSeltDeltRetrieveData,
       "adGenSeltDeltEnumTestStatus": adGenSeltDeltEnumTestStatus,
       "adGenSeltDeltTestRemoteDevice": adGenSeltDeltTestRemoteDevice,
       "adGenXdslMibConformance": adGenXdslMibConformance,
       "adGenXdslMibGroups": adGenXdslMibGroups,
       "adGenXdslSeltDeltGroup": adGenXdslSeltDeltGroup,
       "adGenSeltDeltMIB": adGenSeltDeltMIB}
)
