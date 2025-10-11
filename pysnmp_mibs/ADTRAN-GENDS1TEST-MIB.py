# SNMP MIB module (ADTRAN-GENDS1TEST-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENDS1TEST-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:38 2025
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

(adGenSlotInfoIndex,) = mibBuilder.importSymbols(
    "ADTRAN-GENSLOT-MIB",
    "adGenSlotInfoIndex")

(adTrapInformSeqNum,) = mibBuilder.importSymbols(
    "ADTRAN-GENTRAPINFORM-MIB",
    "adTrapInformSeqNum")

(adShared,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adShared")

(adDS1,
 adGenDS1TestID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-DS1-MIB",
    "adDS1",
    "adGenDS1TestID")

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

adGenDS1TestIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 78, 1, 1)
)
if mibBuilder.loadTexts:
    adGenDS1TestIdentity.setRevisions(
        ("2014-05-06 00:00",
         "2011-08-22 00:00",
         "2011-07-12 00:00",
         "2011-03-24 00:00",
         "2008-09-18 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenDS1Test_ObjectIdentity = ObjectIdentity
adGenDS1Test = _AdGenDS1Test_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1)
)
_AdGenDS1TestCommand_ObjectIdentity = ObjectIdentity
adGenDS1TestCommand = _AdGenDS1TestCommand_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 1)
)
_AdGenDS1TestCommandTable_Object = MibTable
adGenDS1TestCommandTable = _AdGenDS1TestCommandTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenDS1TestCommandTable.setStatus("current")
_AdGenDS1TestCommandEntry_Object = MibTableRow
adGenDS1TestCommandEntry = _AdGenDS1TestCommandEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 1, 1, 1)
)
adGenDS1TestCommandEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenDS1TestCommandEntry.setStatus("current")
_AdGenDS1TestTimeout_Type = Integer32
_AdGenDS1TestTimeout_Object = MibTableColumn
adGenDS1TestTimeout = _AdGenDS1TestTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 1, 1, 1, 1),
    _AdGenDS1TestTimeout_Type()
)
adGenDS1TestTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestTimeout.setStatus("current")


class _AdGenDS1TestStartStop_Type(Integer32):
    """Custom type adGenDS1TestStartStop based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("nearEndStart", 1),
          ("farEndStart", 2),
          ("allStop", 3))
    )


_AdGenDS1TestStartStop_Type.__name__ = "Integer32"
_AdGenDS1TestStartStop_Object = MibTableColumn
adGenDS1TestStartStop = _AdGenDS1TestStartStop_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 1, 1, 1, 2),
    _AdGenDS1TestStartStop_Type()
)
adGenDS1TestStartStop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestStartStop.setStatus("current")


class _AdGenDS1TestStatus_Type(Integer32):
    """Custom type adGenDS1TestStatus based on Integer32"""
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
              50)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("nearEndLine", 2),
          ("nearEndPayload", 3),
          ("nearEndCsu", 4),
          ("nearEndFdlPayload", 5),
          ("nearEndFeacLine", 6),
          ("pattQrss", 7),
          ("pattOneInEight", 8),
          ("pattAllOnes", 9),
          ("pattAllZeros", 10),
          ("farEndPattQrssCsu", 11),
          ("farEndPattOneInEightCsu", 12),
          ("farEndPattAllOnesCsu", 13),
          ("farEndPattAllZerosCsu", 14),
          ("farEndPattQrssFdlPayload", 15),
          ("farEndPattOneInEightFdlPayload", 16),
          ("farEndPattAllOnesFdlPayload", 17),
          ("farEndPattAllZerosFdlPayload", 18),
          ("farEndPattQrssFac2niu", 19),
          ("farEndPattOneInEightFac2niu", 20),
          ("farEndPattAllOnesFac2niu", 21),
          ("farEndPattAllZerosFac2niu", 22),
          ("farEndPattQrssFeac", 23),
          ("farEndPattOneInEightFeac", 24),
          ("farEndPattAllOnesFeac", 25),
          ("farEndPattAllZerosFeac", 26),
          ("nearEndFac2niu", 27),
          ("farEndCsu", 28),
          ("farEndFdlPayload", 29),
          ("farEndFac2Niu", 30),
          ("farEndFeac", 31),
          ("nearEndInward", 32),
          ("nearEndCsuInward", 33),
          ("nearEndFac2niuInward", 34),
          ("pattTwoInEight", 35),
          ("pattThreeInTwentyFour", 36),
          ("patt2to23", 37),
          ("patt2to15", 38),
          ("patt2to20", 39),
          ("patt511", 40),
          ("farEndPattTwoInEightCsu", 41),
          ("farEndPattTwoInEightFdlPayload", 42),
          ("farEndPattTwoInEightFac2Niu", 43),
          ("farEndPattTwoInEightFeac", 44),
          ("farEndPattThreeInTwentyFourCsu", 45),
          ("farEndPattThreeInTwentyFourFdlPayload", 46),
          ("farEndPattThreeInTwentyFourFac2Niu", 47),
          ("farEndPattThreeInTwentyFourFeac", 48),
          ("farEndFdlLine", 49),
          ("farEndNiuInband", 50))
    )


_AdGenDS1TestStatus_Type.__name__ = "Integer32"
_AdGenDS1TestStatus_Object = MibTableColumn
adGenDS1TestStatus = _AdGenDS1TestStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 1, 1, 1, 3),
    _AdGenDS1TestStatus_Type()
)
adGenDS1TestStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDS1TestStatus.setStatus("current")
_AdGenDS1TestTimeRemaining_Type = Unsigned32
_AdGenDS1TestTimeRemaining_Object = MibTableColumn
adGenDS1TestTimeRemaining = _AdGenDS1TestTimeRemaining_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 1, 1, 1, 4),
    _AdGenDS1TestTimeRemaining_Type()
)
adGenDS1TestTimeRemaining.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDS1TestTimeRemaining.setStatus("current")
_AdGenDS1TestTimeElapsed_Type = Unsigned32
_AdGenDS1TestTimeElapsed_Object = MibTableColumn
adGenDS1TestTimeElapsed = _AdGenDS1TestTimeElapsed_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 1, 1, 1, 5),
    _AdGenDS1TestTimeElapsed_Type()
)
adGenDS1TestTimeElapsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDS1TestTimeElapsed.setStatus("current")
_AdGenDS1TestNearEndLoopback_ObjectIdentity = ObjectIdentity
adGenDS1TestNearEndLoopback = _AdGenDS1TestNearEndLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 2)
)
_AdGenDS1TestNearEndLoopbackTable_Object = MibTable
adGenDS1TestNearEndLoopbackTable = _AdGenDS1TestNearEndLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 2, 1)
)
if mibBuilder.loadTexts:
    adGenDS1TestNearEndLoopbackTable.setStatus("current")
_AdGenDS1TestNearEndLoopbackEntry_Object = MibTableRow
adGenDS1TestNearEndLoopbackEntry = _AdGenDS1TestNearEndLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 2, 1, 1)
)
adGenDS1TestNearEndLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenDS1TestNearEndLoopbackEntry.setStatus("current")


class _AdGenDS1TestNearEndLoopbackType_Type(Integer32):
    """Custom type adGenDS1TestNearEndLoopbackType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("line", 1),
          ("payload", 2),
          ("inward", 3))
    )


_AdGenDS1TestNearEndLoopbackType_Type.__name__ = "Integer32"
_AdGenDS1TestNearEndLoopbackType_Object = MibTableColumn
adGenDS1TestNearEndLoopbackType = _AdGenDS1TestNearEndLoopbackType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 2, 1, 1, 1),
    _AdGenDS1TestNearEndLoopbackType_Type()
)
adGenDS1TestNearEndLoopbackType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestNearEndLoopbackType.setStatus("current")
_AdGenDS1TestFarEndLoopback_ObjectIdentity = ObjectIdentity
adGenDS1TestFarEndLoopback = _AdGenDS1TestFarEndLoopback_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 3)
)
_AdGenDS1TestFarEndLoopbackTable_Object = MibTable
adGenDS1TestFarEndLoopbackTable = _AdGenDS1TestFarEndLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 3, 1)
)
if mibBuilder.loadTexts:
    adGenDS1TestFarEndLoopbackTable.setStatus("current")
_AdGenDS1TestFarEndLoopbackEntry_Object = MibTableRow
adGenDS1TestFarEndLoopbackEntry = _AdGenDS1TestFarEndLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 3, 1, 1)
)
adGenDS1TestFarEndLoopbackEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenDS1TestFarEndLoopbackEntry.setStatus("current")


class _AdGenDS1TestFarEndLpbkType_Type(Integer32):
    """Custom type adGenDS1TestFarEndLpbkType based on Integer32"""
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
        *(("none", 1),
          ("csu", 2),
          ("fdlPayload", 3),
          ("fac2niu", 4),
          ("feac", 5),
          ("fdlLine", 6),
          ("niuInband", 7))
    )


_AdGenDS1TestFarEndLpbkType_Type.__name__ = "Integer32"
_AdGenDS1TestFarEndLpbkType_Object = MibTableColumn
adGenDS1TestFarEndLpbkType = _AdGenDS1TestFarEndLpbkType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 3, 1, 1, 1),
    _AdGenDS1TestFarEndLpbkType_Type()
)
adGenDS1TestFarEndLpbkType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestFarEndLpbkType.setStatus("current")


class _AdGenDS1TestFarEndCSURequest_Type(Integer32):
    """Custom type adGenDS1TestFarEndCSURequest based on Integer32"""
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


_AdGenDS1TestFarEndCSURequest_Type.__name__ = "Integer32"
_AdGenDS1TestFarEndCSURequest_Object = MibTableColumn
adGenDS1TestFarEndCSURequest = _AdGenDS1TestFarEndCSURequest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 3, 1, 1, 2),
    _AdGenDS1TestFarEndCSURequest_Type()
)
adGenDS1TestFarEndCSURequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestFarEndCSURequest.setStatus("current")


class _AdGenDS1TestFarEndFDLRequest_Type(Integer32):
    """Custom type adGenDS1TestFarEndFDLRequest based on Integer32"""
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


_AdGenDS1TestFarEndFDLRequest_Type.__name__ = "Integer32"
_AdGenDS1TestFarEndFDLRequest_Object = MibTableColumn
adGenDS1TestFarEndFDLRequest = _AdGenDS1TestFarEndFDLRequest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 3, 1, 1, 3),
    _AdGenDS1TestFarEndFDLRequest_Type()
)
adGenDS1TestFarEndFDLRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestFarEndFDLRequest.setStatus("current")


class _AdGenDS1TestFarEndFEACRequest_Type(Integer32):
    """Custom type adGenDS1TestFarEndFEACRequest based on Integer32"""
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


_AdGenDS1TestFarEndFEACRequest_Type.__name__ = "Integer32"
_AdGenDS1TestFarEndFEACRequest_Object = MibTableColumn
adGenDS1TestFarEndFEACRequest = _AdGenDS1TestFarEndFEACRequest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 3, 1, 1, 4),
    _AdGenDS1TestFarEndFEACRequest_Type()
)
adGenDS1TestFarEndFEACRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestFarEndFEACRequest.setStatus("current")


class _AdGenDS1TestFarEndFAC2NIURequest_Type(Integer32):
    """Custom type adGenDS1TestFarEndFAC2NIURequest based on Integer32"""
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


_AdGenDS1TestFarEndFAC2NIURequest_Type.__name__ = "Integer32"
_AdGenDS1TestFarEndFAC2NIURequest_Object = MibTableColumn
adGenDS1TestFarEndFAC2NIURequest = _AdGenDS1TestFarEndFAC2NIURequest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 3, 1, 1, 5),
    _AdGenDS1TestFarEndFAC2NIURequest_Type()
)
adGenDS1TestFarEndFAC2NIURequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestFarEndFAC2NIURequest.setStatus("current")


class _AdGenDS1TestFarEndCSUInwardRequest_Type(Integer32):
    """Custom type adGenDS1TestFarEndCSUInwardRequest based on Integer32"""
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


_AdGenDS1TestFarEndCSUInwardRequest_Type.__name__ = "Integer32"
_AdGenDS1TestFarEndCSUInwardRequest_Object = MibTableColumn
adGenDS1TestFarEndCSUInwardRequest = _AdGenDS1TestFarEndCSUInwardRequest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 3, 1, 1, 6),
    _AdGenDS1TestFarEndCSUInwardRequest_Type()
)
adGenDS1TestFarEndCSUInwardRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestFarEndCSUInwardRequest.setStatus("current")


class _AdGenDS1TestFarEndFAC2NIUInwardRequest_Type(Integer32):
    """Custom type adGenDS1TestFarEndFAC2NIUInwardRequest based on Integer32"""
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


_AdGenDS1TestFarEndFAC2NIUInwardRequest_Type.__name__ = "Integer32"
_AdGenDS1TestFarEndFAC2NIUInwardRequest_Object = MibTableColumn
adGenDS1TestFarEndFAC2NIUInwardRequest = _AdGenDS1TestFarEndFAC2NIUInwardRequest_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 3, 1, 1, 7),
    _AdGenDS1TestFarEndFAC2NIUInwardRequest_Type()
)
adGenDS1TestFarEndFAC2NIUInwardRequest.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestFarEndFAC2NIUInwardRequest.setStatus("current")
_AdGenDS1TestPattern_ObjectIdentity = ObjectIdentity
adGenDS1TestPattern = _AdGenDS1TestPattern_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 4)
)
_AdGenDS1TestPatternTable_Object = MibTable
adGenDS1TestPatternTable = _AdGenDS1TestPatternTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 4, 1)
)
if mibBuilder.loadTexts:
    adGenDS1TestPatternTable.setStatus("current")
_AdGenDS1TestPatternEntry_Object = MibTableRow
adGenDS1TestPatternEntry = _AdGenDS1TestPatternEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 4, 1, 1)
)
adGenDS1TestPatternEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenDS1TestPatternEntry.setStatus("current")


class _AdGenDS1TestPatternType_Type(Integer32):
    """Custom type adGenDS1TestPatternType based on Integer32"""
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
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("notUsed1", 1),
          ("qrss", 2),
          ("notUsed3", 3),
          ("allOnes", 4),
          ("allZeros", 5),
          ("notUsed6", 6),
          ("notUsed7", 7),
          ("notUsed8", 8),
          ("notUsed9", 9),
          ("oneInEight", 10),
          ("twoInEight", 11),
          ("threeInTwentyFour", 12))
    )


_AdGenDS1TestPatternType_Type.__name__ = "Integer32"
_AdGenDS1TestPatternType_Object = MibTableColumn
adGenDS1TestPatternType = _AdGenDS1TestPatternType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 4, 1, 1, 1),
    _AdGenDS1TestPatternType_Type()
)
adGenDS1TestPatternType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestPatternType.setStatus("current")


class _AdGenDS1TestPatternSync_Type(Integer32):
    """Custom type adGenDS1TestPatternSync based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("true", 1),
          ("false", 2))
    )


_AdGenDS1TestPatternSync_Type.__name__ = "Integer32"
_AdGenDS1TestPatternSync_Object = MibTableColumn
adGenDS1TestPatternSync = _AdGenDS1TestPatternSync_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 4, 1, 1, 2),
    _AdGenDS1TestPatternSync_Type()
)
adGenDS1TestPatternSync.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDS1TestPatternSync.setStatus("current")
_AdGenDS1TestPatternErrorsRcvd_Type = Gauge32
_AdGenDS1TestPatternErrorsRcvd_Object = MibTableColumn
adGenDS1TestPatternErrorsRcvd = _AdGenDS1TestPatternErrorsRcvd_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 4, 1, 1, 3),
    _AdGenDS1TestPatternErrorsRcvd_Type()
)
adGenDS1TestPatternErrorsRcvd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDS1TestPatternErrorsRcvd.setStatus("current")


class _AdGenDS1TestPatternInsertError_Type(Integer32):
    """Custom type adGenDS1TestPatternInsertError based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("insert", 1)
    )


_AdGenDS1TestPatternInsertError_Type.__name__ = "Integer32"
_AdGenDS1TestPatternInsertError_Object = MibTableColumn
adGenDS1TestPatternInsertError = _AdGenDS1TestPatternInsertError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 4, 1, 1, 4),
    _AdGenDS1TestPatternInsertError_Type()
)
adGenDS1TestPatternInsertError.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestPatternInsertError.setStatus("current")


class _AdGenDS1TestPatternResetCount_Type(Integer32):
    """Custom type adGenDS1TestPatternResetCount based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_AdGenDS1TestPatternResetCount_Type.__name__ = "Integer32"
_AdGenDS1TestPatternResetCount_Object = MibTableColumn
adGenDS1TestPatternResetCount = _AdGenDS1TestPatternResetCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 4, 1, 1, 5),
    _AdGenDS1TestPatternResetCount_Type()
)
adGenDS1TestPatternResetCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDS1TestPatternResetCount.setStatus("current")
_AdGenDS1TestMibConformance_ObjectIdentity = ObjectIdentity
adGenDS1TestMibConformance = _AdGenDS1TestMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 5)
)
_AdGenDS1TestMibGroups_ObjectIdentity = ObjectIdentity
adGenDS1TestMibGroups = _AdGenDS1TestMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 5, 1)
)

# Managed Objects groups

adGenDS1TestGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 78, 1, 5, 1, 1)
)
adGenDS1TestGroup.setObjects(
      *(("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestTimeout"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestStartStop"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestStatus"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestTimeRemaining"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestTimeElapsed"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestNearEndLoopbackType"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestFarEndLpbkType"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestFarEndCSURequest"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestFarEndFDLRequest"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestFarEndFEACRequest"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestFarEndFAC2NIURequest"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestFarEndCSUInwardRequest"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestFarEndFAC2NIUInwardRequest"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestPatternType"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestPatternSync"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestPatternErrorsRcvd"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestPatternInsertError"),
        ("ADTRAN-GENDS1TEST-MIB", "adGenDS1TestPatternResetCount"))
)
if mibBuilder.loadTexts:
    adGenDS1TestGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENDS1TEST-MIB",
    **{"adGenDS1Test": adGenDS1Test,
       "adGenDS1TestCommand": adGenDS1TestCommand,
       "adGenDS1TestCommandTable": adGenDS1TestCommandTable,
       "adGenDS1TestCommandEntry": adGenDS1TestCommandEntry,
       "adGenDS1TestTimeout": adGenDS1TestTimeout,
       "adGenDS1TestStartStop": adGenDS1TestStartStop,
       "adGenDS1TestStatus": adGenDS1TestStatus,
       "adGenDS1TestTimeRemaining": adGenDS1TestTimeRemaining,
       "adGenDS1TestTimeElapsed": adGenDS1TestTimeElapsed,
       "adGenDS1TestNearEndLoopback": adGenDS1TestNearEndLoopback,
       "adGenDS1TestNearEndLoopbackTable": adGenDS1TestNearEndLoopbackTable,
       "adGenDS1TestNearEndLoopbackEntry": adGenDS1TestNearEndLoopbackEntry,
       "adGenDS1TestNearEndLoopbackType": adGenDS1TestNearEndLoopbackType,
       "adGenDS1TestFarEndLoopback": adGenDS1TestFarEndLoopback,
       "adGenDS1TestFarEndLoopbackTable": adGenDS1TestFarEndLoopbackTable,
       "adGenDS1TestFarEndLoopbackEntry": adGenDS1TestFarEndLoopbackEntry,
       "adGenDS1TestFarEndLpbkType": adGenDS1TestFarEndLpbkType,
       "adGenDS1TestFarEndCSURequest": adGenDS1TestFarEndCSURequest,
       "adGenDS1TestFarEndFDLRequest": adGenDS1TestFarEndFDLRequest,
       "adGenDS1TestFarEndFEACRequest": adGenDS1TestFarEndFEACRequest,
       "adGenDS1TestFarEndFAC2NIURequest": adGenDS1TestFarEndFAC2NIURequest,
       "adGenDS1TestFarEndCSUInwardRequest": adGenDS1TestFarEndCSUInwardRequest,
       "adGenDS1TestFarEndFAC2NIUInwardRequest": adGenDS1TestFarEndFAC2NIUInwardRequest,
       "adGenDS1TestPattern": adGenDS1TestPattern,
       "adGenDS1TestPatternTable": adGenDS1TestPatternTable,
       "adGenDS1TestPatternEntry": adGenDS1TestPatternEntry,
       "adGenDS1TestPatternType": adGenDS1TestPatternType,
       "adGenDS1TestPatternSync": adGenDS1TestPatternSync,
       "adGenDS1TestPatternErrorsRcvd": adGenDS1TestPatternErrorsRcvd,
       "adGenDS1TestPatternInsertError": adGenDS1TestPatternInsertError,
       "adGenDS1TestPatternResetCount": adGenDS1TestPatternResetCount,
       "adGenDS1TestMibConformance": adGenDS1TestMibConformance,
       "adGenDS1TestMibGroups": adGenDS1TestMibGroups,
       "adGenDS1TestGroup": adGenDS1TestGroup,
       "adGenDS1TestIdentity": adGenDS1TestIdentity}
)
