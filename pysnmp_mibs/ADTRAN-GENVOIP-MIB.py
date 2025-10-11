# SNMP MIB module (ADTRAN-GENVOIP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENVOIP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:37 2025
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

(adGenVoip,
 adGenVoipID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenVoip",
    "adGenVoipID")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero",
    "ifIndex")

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
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenVoipIdentity = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 20, 1)
)
if mibBuilder.loadTexts:
    adGenVoipIdentity.setRevisions(
        ("2021-11-02 00:00",
         "2019-10-08 00:00",
         "2019-07-31 00:00",
         "2019-04-24 00:00",
         "2019-04-04 00:00",
         "2018-04-11 00:00",
         "2018-01-08 00:00",
         "2017-09-08 00:00",
         "2014-10-31 00:00",
         "2014-09-30 00:00",
         "2014-02-26 00:00",
         "2013-08-28 00:00",
         "2013-05-13 00:00",
         "2012-11-19 00:00",
         "2012-11-08 00:00",
         "2012-10-31 00:00",
         "2012-07-23 00:00",
         "2012-07-10 00:00",
         "2011-06-13 00:00",
         "2011-03-03 00:00",
         "2009-10-06 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenVoipTrunkName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(10, 10),
    )
    fixed_length = 10



class AdGenVoipCallServiceClassName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



class AdGenVoipUserNumber(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(20, 20),
    )
    fixed_length = 20



class AdGenVoipDialingProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



class AdGenVoipCodecProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



class AdGenVoipMediaProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



class AdGenVoipCodecProfileType(TextualConvention, Integer32):
    status = "current"
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
          ("g711ulaw", 1),
          ("g711alaw", 2),
          ("g729", 3))
    )



class AdGenVoipCallFeatureProfileName(TextualConvention, OctetString):
    status = "current"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )



class AdGenVoipCallReverseLookupIfIndex(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000000000),
    )



# MIB Managed Objects in the order of their OIDs

_AdGenVoipProvisioning_ObjectIdentity = ObjectIdentity
adGenVoipProvisioning = _AdGenVoipProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1)
)
_AdGenVoipTrunkProv_ObjectIdentity = ObjectIdentity
adGenVoipTrunkProv = _AdGenVoipTrunkProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 1)
)
_AdGenVoipTrunkProvTable_Object = MibTable
adGenVoipTrunkProvTable = _AdGenVoipTrunkProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenVoipTrunkProvTable.setStatus("current")
_AdGenVoipTrunkProvEntry_Object = MibTableRow
adGenVoipTrunkProvEntry = _AdGenVoipTrunkProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 1, 1, 1)
)
adGenVoipTrunkProvEntry.setIndexNames(
    (0, "ADTRAN-GENVOIP-MIB", "adGenVoipTrunkEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipTrunkProvEntry.setStatus("current")
_AdGenVoipTrunkEntryIndex_Type = AdGenVoipTrunkName
_AdGenVoipTrunkEntryIndex_Object = MibTableColumn
adGenVoipTrunkEntryIndex = _AdGenVoipTrunkEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 1, 1, 1, 1),
    _AdGenVoipTrunkEntryIndex_Type()
)
adGenVoipTrunkEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipTrunkEntryIndex.setStatus("current")


class _AdGenVoipTrunkTransfer_Type(Integer32):
    """Custom type adGenVoipTrunkTransfer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("blind", 1),
          ("unattended", 2))
    )


_AdGenVoipTrunkTransfer_Type.__name__ = "Integer32"
_AdGenVoipTrunkTransfer_Object = MibTableColumn
adGenVoipTrunkTransfer = _AdGenVoipTrunkTransfer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 1, 1, 1, 2),
    _AdGenVoipTrunkTransfer_Type()
)
adGenVoipTrunkTransfer.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipTrunkTransfer.setStatus("current")
_AdGenVoipDialPlanProv_ObjectIdentity = ObjectIdentity
adGenVoipDialPlanProv = _AdGenVoipDialPlanProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2)
)
_AdGenVoipDialPlanProvCurrentNumber_Type = Integer32
_AdGenVoipDialPlanProvCurrentNumber_Object = MibScalar
adGenVoipDialPlanProvCurrentNumber = _AdGenVoipDialPlanProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2, 1),
    _AdGenVoipDialPlanProvCurrentNumber_Type()
)
adGenVoipDialPlanProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialPlanProvCurrentNumber.setStatus("current")
_AdGenVoipDialPlanProvLastCreateError_Type = DisplayString
_AdGenVoipDialPlanProvLastCreateError_Object = MibScalar
adGenVoipDialPlanProvLastCreateError = _AdGenVoipDialPlanProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2, 2),
    _AdGenVoipDialPlanProvLastCreateError_Type()
)
adGenVoipDialPlanProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialPlanProvLastCreateError.setStatus("current")
_AdGenVoipDialPlanProvTable_Object = MibTable
adGenVoipDialPlanProvTable = _AdGenVoipDialPlanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2, 3)
)
if mibBuilder.loadTexts:
    adGenVoipDialPlanProvTable.setStatus("current")
_AdGenVoipDialPlanProvEntry_Object = MibTableRow
adGenVoipDialPlanProvEntry = _AdGenVoipDialPlanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2, 3, 1)
)
adGenVoipDialPlanProvEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipDialPlanPatternEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipDialPlanProvEntry.setStatus("current")


class _AdGenVoipDialPlanPatternEntryIndex_Type(DisplayString):
    """Custom type adGenVoipDialPlanPatternEntryIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 40),
    )


_AdGenVoipDialPlanPatternEntryIndex_Type.__name__ = "DisplayString"
_AdGenVoipDialPlanPatternEntryIndex_Object = MibTableColumn
adGenVoipDialPlanPatternEntryIndex = _AdGenVoipDialPlanPatternEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2, 3, 1, 1),
    _AdGenVoipDialPlanPatternEntryIndex_Type()
)
adGenVoipDialPlanPatternEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipDialPlanPatternEntryIndex.setStatus("current")
_AdGenVoipDialPlanRowStatus_Type = RowStatus
_AdGenVoipDialPlanRowStatus_Object = MibTableColumn
adGenVoipDialPlanRowStatus = _AdGenVoipDialPlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2, 3, 1, 2),
    _AdGenVoipDialPlanRowStatus_Type()
)
adGenVoipDialPlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialPlanRowStatus.setStatus("current")
_AdGenVoipDialPlanLastErrorString_Type = DisplayString
_AdGenVoipDialPlanLastErrorString_Object = MibTableColumn
adGenVoipDialPlanLastErrorString = _AdGenVoipDialPlanLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2, 3, 1, 3),
    _AdGenVoipDialPlanLastErrorString_Type()
)
adGenVoipDialPlanLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialPlanLastErrorString.setStatus("current")


class _AdGenVoipDialPlanType_Type(Integer32):
    """Custom type adGenVoipDialPlanType based on Integer32"""
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
        *(("alwaysPermitted", 1),
          ("extensions", 2),
          ("local", 3),
          ("national", 4),
          ("tollFree", 5),
          ("a900Number", 6),
          ("international", 7),
          ("operatorAssisted", 8),
          ("specifyCarrier", 9),
          ("user1", 10),
          ("user2", 11),
          ("user3", 12))
    )


_AdGenVoipDialPlanType_Type.__name__ = "Integer32"
_AdGenVoipDialPlanType_Object = MibTableColumn
adGenVoipDialPlanType = _AdGenVoipDialPlanType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2, 3, 1, 4),
    _AdGenVoipDialPlanType_Type()
)
adGenVoipDialPlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialPlanType.setStatus("current")


class _AdGenVoipDialPlanEmergencyNumber_Type(Integer32):
    """Custom type adGenVoipDialPlanEmergencyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isEmergencyNumber", 1),
          ("notEmergencyNumber", 2))
    )


_AdGenVoipDialPlanEmergencyNumber_Type.__name__ = "Integer32"
_AdGenVoipDialPlanEmergencyNumber_Object = MibTableColumn
adGenVoipDialPlanEmergencyNumber = _AdGenVoipDialPlanEmergencyNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2, 3, 1, 5),
    _AdGenVoipDialPlanEmergencyNumber_Type()
)
adGenVoipDialPlanEmergencyNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialPlanEmergencyNumber.setStatus("current")


class _AdGenVoipDialPlanExternalLineCode_Type(Integer32):
    """Custom type adGenVoipDialPlanExternalLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("optional", 1),
          ("prohibited", 2),
          ("required", 3))
    )


_AdGenVoipDialPlanExternalLineCode_Type.__name__ = "Integer32"
_AdGenVoipDialPlanExternalLineCode_Object = MibTableColumn
adGenVoipDialPlanExternalLineCode = _AdGenVoipDialPlanExternalLineCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 2, 3, 1, 6),
    _AdGenVoipDialPlanExternalLineCode_Type()
)
adGenVoipDialPlanExternalLineCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialPlanExternalLineCode.setStatus("current")
_AdGenVoipSPREPatternProv_ObjectIdentity = ObjectIdentity
adGenVoipSPREPatternProv = _AdGenVoipSPREPatternProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 3)
)
_AdGenVoipSPREPatternProvCurrentNumber_Type = Integer32
_AdGenVoipSPREPatternProvCurrentNumber_Object = MibScalar
adGenVoipSPREPatternProvCurrentNumber = _AdGenVoipSPREPatternProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 3, 1),
    _AdGenVoipSPREPatternProvCurrentNumber_Type()
)
adGenVoipSPREPatternProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipSPREPatternProvCurrentNumber.setStatus("current")
_AdGenVoipSPREPatternProvLastCreateError_Type = DisplayString
_AdGenVoipSPREPatternProvLastCreateError_Object = MibScalar
adGenVoipSPREPatternProvLastCreateError = _AdGenVoipSPREPatternProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 3, 2),
    _AdGenVoipSPREPatternProvLastCreateError_Type()
)
adGenVoipSPREPatternProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipSPREPatternProvLastCreateError.setStatus("current")
_AdGenVoipSPREPatternProvTable_Object = MibTable
adGenVoipSPREPatternProvTable = _AdGenVoipSPREPatternProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 3, 3)
)
if mibBuilder.loadTexts:
    adGenVoipSPREPatternProvTable.setStatus("current")
_AdGenVoipSPREPatternProvEntry_Object = MibTableRow
adGenVoipSPREPatternProvEntry = _AdGenVoipSPREPatternProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 3, 3, 1)
)
adGenVoipSPREPatternProvEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipSPREPatternEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipSPREPatternProvEntry.setStatus("current")


class _AdGenVoipSPREPatternEntryIndex_Type(DisplayString):
    """Custom type adGenVoipSPREPatternEntryIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 44),
    )


_AdGenVoipSPREPatternEntryIndex_Type.__name__ = "DisplayString"
_AdGenVoipSPREPatternEntryIndex_Object = MibTableColumn
adGenVoipSPREPatternEntryIndex = _AdGenVoipSPREPatternEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 3, 3, 1, 1),
    _AdGenVoipSPREPatternEntryIndex_Type()
)
adGenVoipSPREPatternEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipSPREPatternEntryIndex.setStatus("current")
_AdGenVoipSPREPatternRowStatus_Type = RowStatus
_AdGenVoipSPREPatternRowStatus_Object = MibTableColumn
adGenVoipSPREPatternRowStatus = _AdGenVoipSPREPatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 3, 3, 1, 2),
    _AdGenVoipSPREPatternRowStatus_Type()
)
adGenVoipSPREPatternRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipSPREPatternRowStatus.setStatus("current")
_AdGenVoipSPREPatternLastErrorString_Type = DisplayString
_AdGenVoipSPREPatternLastErrorString_Object = MibTableColumn
adGenVoipSPREPatternLastErrorString = _AdGenVoipSPREPatternLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 3, 3, 1, 3),
    _AdGenVoipSPREPatternLastErrorString_Type()
)
adGenVoipSPREPatternLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipSPREPatternLastErrorString.setStatus("current")


class _AdGenVoipSPREPatternTone_Type(Integer32):
    """Custom type adGenVoipSPREPatternTone based on Integer32"""
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
          ("dial", 2),
          ("stutterDial", 3))
    )


_AdGenVoipSPREPatternTone_Type.__name__ = "Integer32"
_AdGenVoipSPREPatternTone_Object = MibTableColumn
adGenVoipSPREPatternTone = _AdGenVoipSPREPatternTone_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 3, 3, 1, 4),
    _AdGenVoipSPREPatternTone_Type()
)
adGenVoipSPREPatternTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipSPREPatternTone.setStatus("current")
_AdGenVoipCallServiceClassProv_ObjectIdentity = ObjectIdentity
adGenVoipCallServiceClassProv = _AdGenVoipCallServiceClassProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4)
)
_AdGenVoipCallServiceClassProvCurrentNumber_Type = Integer32
_AdGenVoipCallServiceClassProvCurrentNumber_Object = MibScalar
adGenVoipCallServiceClassProvCurrentNumber = _AdGenVoipCallServiceClassProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 1),
    _AdGenVoipCallServiceClassProvCurrentNumber_Type()
)
adGenVoipCallServiceClassProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassProvCurrentNumber.setStatus("current")
_AdGenVoipCallServiceClassProvLastCreateError_Type = DisplayString
_AdGenVoipCallServiceClassProvLastCreateError_Object = MibScalar
adGenVoipCallServiceClassProvLastCreateError = _AdGenVoipCallServiceClassProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 2),
    _AdGenVoipCallServiceClassProvLastCreateError_Type()
)
adGenVoipCallServiceClassProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassProvLastCreateError.setStatus("current")
_AdGenVoipCallServiceClassProvTable_Object = MibTable
adGenVoipCallServiceClassProvTable = _AdGenVoipCallServiceClassProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3)
)
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassProvTable.setStatus("current")
_AdGenVoipCallServiceClassProvEntry_Object = MibTableRow
adGenVoipCallServiceClassProvEntry = _AdGenVoipCallServiceClassProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1)
)
adGenVoipCallServiceClassProvEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipCallServiceClassEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassProvEntry.setStatus("current")
_AdGenVoipCallServiceClassEntryIndex_Type = AdGenVoipCallServiceClassName
_AdGenVoipCallServiceClassEntryIndex_Object = MibTableColumn
adGenVoipCallServiceClassEntryIndex = _AdGenVoipCallServiceClassEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 1),
    _AdGenVoipCallServiceClassEntryIndex_Type()
)
adGenVoipCallServiceClassEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassEntryIndex.setStatus("current")
_AdGenVoipCallServiceClassRowStatus_Type = RowStatus
_AdGenVoipCallServiceClassRowStatus_Object = MibTableColumn
adGenVoipCallServiceClassRowStatus = _AdGenVoipCallServiceClassRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 2),
    _AdGenVoipCallServiceClassRowStatus_Type()
)
adGenVoipCallServiceClassRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassRowStatus.setStatus("current")
_AdGenVoipCallServiceClassLastErrorString_Type = DisplayString
_AdGenVoipCallServiceClassLastErrorString_Object = MibTableColumn
adGenVoipCallServiceClassLastErrorString = _AdGenVoipCallServiceClassLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 3),
    _AdGenVoipCallServiceClassLastErrorString_Type()
)
adGenVoipCallServiceClassLastErrorString.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassLastErrorString.setStatus("current")
_AdGenVoipCallServiceClass900Number_Type = TruthValue
_AdGenVoipCallServiceClass900Number_Object = MibTableColumn
adGenVoipCallServiceClass900Number = _AdGenVoipCallServiceClass900Number_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 4),
    _AdGenVoipCallServiceClass900Number_Type()
)
adGenVoipCallServiceClass900Number.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClass900Number.setStatus("current")
_AdGenVoipCallServiceClassExtensions_Type = TruthValue
_AdGenVoipCallServiceClassExtensions_Object = MibTableColumn
adGenVoipCallServiceClassExtensions = _AdGenVoipCallServiceClassExtensions_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 5),
    _AdGenVoipCallServiceClassExtensions_Type()
)
adGenVoipCallServiceClassExtensions.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassExtensions.setStatus("current")
_AdGenVoipCallServiceClassInternational_Type = TruthValue
_AdGenVoipCallServiceClassInternational_Object = MibTableColumn
adGenVoipCallServiceClassInternational = _AdGenVoipCallServiceClassInternational_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 6),
    _AdGenVoipCallServiceClassInternational_Type()
)
adGenVoipCallServiceClassInternational.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassInternational.setStatus("current")
_AdGenVoipCallServiceClassLocal_Type = TruthValue
_AdGenVoipCallServiceClassLocal_Object = MibTableColumn
adGenVoipCallServiceClassLocal = _AdGenVoipCallServiceClassLocal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 7),
    _AdGenVoipCallServiceClassLocal_Type()
)
adGenVoipCallServiceClassLocal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassLocal.setStatus("current")
_AdGenVoipCallServiceClassNational_Type = TruthValue
_AdGenVoipCallServiceClassNational_Object = MibTableColumn
adGenVoipCallServiceClassNational = _AdGenVoipCallServiceClassNational_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 8),
    _AdGenVoipCallServiceClassNational_Type()
)
adGenVoipCallServiceClassNational.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassNational.setStatus("current")
_AdGenVoipCallServiceClassOperatorAssisted_Type = TruthValue
_AdGenVoipCallServiceClassOperatorAssisted_Object = MibTableColumn
adGenVoipCallServiceClassOperatorAssisted = _AdGenVoipCallServiceClassOperatorAssisted_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 9),
    _AdGenVoipCallServiceClassOperatorAssisted_Type()
)
adGenVoipCallServiceClassOperatorAssisted.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassOperatorAssisted.setStatus("current")
_AdGenVoipCallServiceClassSpecifyCarrier_Type = TruthValue
_AdGenVoipCallServiceClassSpecifyCarrier_Object = MibTableColumn
adGenVoipCallServiceClassSpecifyCarrier = _AdGenVoipCallServiceClassSpecifyCarrier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 10),
    _AdGenVoipCallServiceClassSpecifyCarrier_Type()
)
adGenVoipCallServiceClassSpecifyCarrier.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassSpecifyCarrier.setStatus("current")
_AdGenVoipCallServiceClassTollFree_Type = TruthValue
_AdGenVoipCallServiceClassTollFree_Object = MibTableColumn
adGenVoipCallServiceClassTollFree = _AdGenVoipCallServiceClassTollFree_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 11),
    _AdGenVoipCallServiceClassTollFree_Type()
)
adGenVoipCallServiceClassTollFree.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassTollFree.setStatus("current")
_AdGenVoipCallServiceClassUser1_Type = TruthValue
_AdGenVoipCallServiceClassUser1_Object = MibTableColumn
adGenVoipCallServiceClassUser1 = _AdGenVoipCallServiceClassUser1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 12),
    _AdGenVoipCallServiceClassUser1_Type()
)
adGenVoipCallServiceClassUser1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassUser1.setStatus("current")
_AdGenVoipCallServiceClassUser2_Type = TruthValue
_AdGenVoipCallServiceClassUser2_Object = MibTableColumn
adGenVoipCallServiceClassUser2 = _AdGenVoipCallServiceClassUser2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 13),
    _AdGenVoipCallServiceClassUser2_Type()
)
adGenVoipCallServiceClassUser2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassUser2.setStatus("current")
_AdGenVoipCallServiceClassUser3_Type = TruthValue
_AdGenVoipCallServiceClassUser3_Object = MibTableColumn
adGenVoipCallServiceClassUser3 = _AdGenVoipCallServiceClassUser3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 14),
    _AdGenVoipCallServiceClassUser3_Type()
)
adGenVoipCallServiceClassUser3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceClassUser3.setStatus("current")
_AdGenVoipCallServiceConference_Type = TruthValue
_AdGenVoipCallServiceConference_Object = MibTableColumn
adGenVoipCallServiceConference = _AdGenVoipCallServiceConference_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 15),
    _AdGenVoipCallServiceConference_Type()
)
adGenVoipCallServiceConference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceConference.setStatus("current")
_AdGenVoipCallServiceDisableCallWaiting_Type = TruthValue
_AdGenVoipCallServiceDisableCallWaiting_Object = MibTableColumn
adGenVoipCallServiceDisableCallWaiting = _AdGenVoipCallServiceDisableCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 4, 3, 1, 16),
    _AdGenVoipCallServiceDisableCallWaiting_Type()
)
adGenVoipCallServiceDisableCallWaiting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallServiceDisableCallWaiting.setStatus("current")
_AdGenVoipUserProv_ObjectIdentity = ObjectIdentity
adGenVoipUserProv = _AdGenVoipUserProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5)
)
_AdGenVoipUserProvCurrentNumber_Type = Integer32
_AdGenVoipUserProvCurrentNumber_Object = MibScalar
adGenVoipUserProvCurrentNumber = _AdGenVoipUserProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 1),
    _AdGenVoipUserProvCurrentNumber_Type()
)
adGenVoipUserProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipUserProvCurrentNumber.setStatus("current")
_AdGenVoipUserProvLastCreateError_Type = DisplayString
_AdGenVoipUserProvLastCreateError_Object = MibScalar
adGenVoipUserProvLastCreateError = _AdGenVoipUserProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 2),
    _AdGenVoipUserProvLastCreateError_Type()
)
adGenVoipUserProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipUserProvLastCreateError.setStatus("current")
_AdGenVoipUserProvTable_Object = MibTable
adGenVoipUserProvTable = _AdGenVoipUserProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3)
)
if mibBuilder.loadTexts:
    adGenVoipUserProvTable.setStatus("current")
_AdGenVoipUserProvEntry_Object = MibTableRow
adGenVoipUserProvEntry = _AdGenVoipUserProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1)
)
adGenVoipUserProvEntry.setIndexNames(
    (0, "ADTRAN-GENVOIP-MIB", "adGenVoipUserEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipUserProvEntry.setStatus("current")
_AdGenVoipUserEntryIndex_Type = AdGenVoipUserNumber
_AdGenVoipUserEntryIndex_Object = MibTableColumn
adGenVoipUserEntryIndex = _AdGenVoipUserEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 1),
    _AdGenVoipUserEntryIndex_Type()
)
adGenVoipUserEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipUserEntryIndex.setStatus("current")
_AdGenVoipUserRowStatus_Type = RowStatus
_AdGenVoipUserRowStatus_Object = MibTableColumn
adGenVoipUserRowStatus = _AdGenVoipUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 2),
    _AdGenVoipUserRowStatus_Type()
)
adGenVoipUserRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserRowStatus.setStatus("current")
_AdGenVoipUserLastErrorString_Type = DisplayString
_AdGenVoipUserLastErrorString_Object = MibTableColumn
adGenVoipUserLastErrorString = _AdGenVoipUserLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 3),
    _AdGenVoipUserLastErrorString_Type()
)
adGenVoipUserLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipUserLastErrorString.setStatus("current")
_AdGenVoipUserFxsPort_Type = InterfaceIndexOrZero
_AdGenVoipUserFxsPort_Object = MibTableColumn
adGenVoipUserFxsPort = _AdGenVoipUserFxsPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 4),
    _AdGenVoipUserFxsPort_Type()
)
adGenVoipUserFxsPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserFxsPort.setStatus("current")
_AdGenVoipUserCallClass_Type = AdGenVoipCallServiceClassName
_AdGenVoipUserCallClass_Object = MibTableColumn
adGenVoipUserCallClass = _AdGenVoipUserCallClass_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 5),
    _AdGenVoipUserCallClass_Type()
)
adGenVoipUserCallClass.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserCallClass.setStatus("current")
_AdGenVoipUserCallWaiting_Type = TruthValue
_AdGenVoipUserCallWaiting_Object = MibTableColumn
adGenVoipUserCallWaiting = _AdGenVoipUserCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 6),
    _AdGenVoipUserCallWaiting_Type()
)
adGenVoipUserCallWaiting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserCallWaiting.setStatus("current")
_AdGenVoipUserDialingProfile_Type = AdGenVoipDialingProfileName
_AdGenVoipUserDialingProfile_Object = MibTableColumn
adGenVoipUserDialingProfile = _AdGenVoipUserDialingProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 7),
    _AdGenVoipUserDialingProfile_Type()
)
adGenVoipUserDialingProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserDialingProfile.setStatus("current")


class _AdGenVoipUserHotlineEnabled_Type(TruthValue):
    """Custom type adGenVoipUserHotlineEnabled based on TruthValue"""
    defaultValue = 2


_AdGenVoipUserHotlineEnabled_Type.__name__ = "TruthValue"
_AdGenVoipUserHotlineEnabled_Object = MibTableColumn
adGenVoipUserHotlineEnabled = _AdGenVoipUserHotlineEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 8),
    _AdGenVoipUserHotlineEnabled_Type()
)
adGenVoipUserHotlineEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserHotlineEnabled.setStatus("current")


class _AdGenVoipUserHotlineNumber_Type(DisplayString):
    """Custom type adGenVoipUserHotlineNumber based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdGenVoipUserHotlineNumber_Type.__name__ = "DisplayString"
_AdGenVoipUserHotlineNumber_Object = MibTableColumn
adGenVoipUserHotlineNumber = _AdGenVoipUserHotlineNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 9),
    _AdGenVoipUserHotlineNumber_Type()
)
adGenVoipUserHotlineNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserHotlineNumber.setStatus("current")


class _AdGenVoipUserSipTrunkManualSelect_Type(DisplayString):
    """Custom type adGenVoipUserSipTrunkManualSelect based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_AdGenVoipUserSipTrunkManualSelect_Type.__name__ = "DisplayString"
_AdGenVoipUserSipTrunkManualSelect_Object = MibTableColumn
adGenVoipUserSipTrunkManualSelect = _AdGenVoipUserSipTrunkManualSelect_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 10),
    _AdGenVoipUserSipTrunkManualSelect_Type()
)
adGenVoipUserSipTrunkManualSelect.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserSipTrunkManualSelect.setStatus("current")


class _AdGenVoipUserWarmlineEnabled_Type(TruthValue):
    """Custom type adGenVoipUserWarmlineEnabled based on TruthValue"""
    defaultValue = 2


_AdGenVoipUserWarmlineEnabled_Type.__name__ = "TruthValue"
_AdGenVoipUserWarmlineEnabled_Object = MibTableColumn
adGenVoipUserWarmlineEnabled = _AdGenVoipUserWarmlineEnabled_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 11),
    _AdGenVoipUserWarmlineEnabled_Type()
)
adGenVoipUserWarmlineEnabled.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserWarmlineEnabled.setStatus("current")


class _AdGenVoipUserWarmlineNumber_Type(DisplayString):
    """Custom type adGenVoipUserWarmlineNumber based on DisplayString"""
    defaultValue = OctetString("")

    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AdGenVoipUserWarmlineNumber_Type.__name__ = "DisplayString"
_AdGenVoipUserWarmlineNumber_Object = MibTableColumn
adGenVoipUserWarmlineNumber = _AdGenVoipUserWarmlineNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 12),
    _AdGenVoipUserWarmlineNumber_Type()
)
adGenVoipUserWarmlineNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserWarmlineNumber.setStatus("current")


class _AdGenVoipUserWarmlineDelay_Type(Integer32):
    """Custom type adGenVoipUserWarmlineDelay based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AdGenVoipUserWarmlineDelay_Type.__name__ = "Integer32"
_AdGenVoipUserWarmlineDelay_Object = MibTableColumn
adGenVoipUserWarmlineDelay = _AdGenVoipUserWarmlineDelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 3, 1, 13),
    _AdGenVoipUserWarmlineDelay_Type()
)
adGenVoipUserWarmlineDelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipUserWarmlineDelay.setStatus("current")
_AdGenVoipUserProvBulkInstance_Type = Unsigned32
_AdGenVoipUserProvBulkInstance_Object = MibScalar
adGenVoipUserProvBulkInstance = _AdGenVoipUserProvBulkInstance_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 5, 4),
    _AdGenVoipUserProvBulkInstance_Type()
)
adGenVoipUserProvBulkInstance.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipUserProvBulkInstance.setStatus("current")
_AdGenVoipScalarProv_ObjectIdentity = ObjectIdentity
adGenVoipScalarProv = _AdGenVoipScalarProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6)
)


class _AdGenVoipScalarFlashhookMode_Type(Integer32):
    """Custom type adGenVoipScalarFlashhookMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("interpreted", 1),
          ("transparent", 2))
    )


_AdGenVoipScalarFlashhookMode_Type.__name__ = "Integer32"
_AdGenVoipScalarFlashhookMode_Object = MibScalar
adGenVoipScalarFlashhookMode = _AdGenVoipScalarFlashhookMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 1),
    _AdGenVoipScalarFlashhookMode_Type()
)
adGenVoipScalarFlashhookMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarFlashhookMode.setStatus("current")


class _AdGenVoipScalarConferenceMode_Type(Integer32):
    """Custom type adGenVoipScalarConferenceMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("local", 2))
    )


_AdGenVoipScalarConferenceMode_Type.__name__ = "Integer32"
_AdGenVoipScalarConferenceMode_Object = MibScalar
adGenVoipScalarConferenceMode = _AdGenVoipScalarConferenceMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 2),
    _AdGenVoipScalarConferenceMode_Type()
)
adGenVoipScalarConferenceMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarConferenceMode.setStatus("current")


class _AdGenVoipScalarConfLocalOriginatorFlashhook_Type(Integer32):
    """Custom type adGenVoipScalarConfLocalOriginatorFlashhook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("drop", 1),
          ("ignore", 2),
          ("split", 3))
    )


_AdGenVoipScalarConfLocalOriginatorFlashhook_Type.__name__ = "Integer32"
_AdGenVoipScalarConfLocalOriginatorFlashhook_Object = MibScalar
adGenVoipScalarConfLocalOriginatorFlashhook = _AdGenVoipScalarConfLocalOriginatorFlashhook_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 3),
    _AdGenVoipScalarConfLocalOriginatorFlashhook_Type()
)
adGenVoipScalarConfLocalOriginatorFlashhook.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarConfLocalOriginatorFlashhook.setStatus("current")


class _AdGenVoipScalarConfLocalOriginatorOnhook_Type(Integer32):
    """Custom type adGenVoipScalarConfLocalOriginatorOnhook based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("persist", 1),
          ("terminate", 2))
    )


_AdGenVoipScalarConfLocalOriginatorOnhook_Type.__name__ = "Integer32"
_AdGenVoipScalarConfLocalOriginatorOnhook_Object = MibScalar
adGenVoipScalarConfLocalOriginatorOnhook = _AdGenVoipScalarConfLocalOriginatorOnhook_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 4),
    _AdGenVoipScalarConfLocalOriginatorOnhook_Type()
)
adGenVoipScalarConfLocalOriginatorOnhook.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarConfLocalOriginatorOnhook.setStatus("current")


class _AdGenVoipScalarConfLocalPartyDisconnect_Type(Integer32):
    """Custom type adGenVoipScalarConfLocalPartyDisconnect based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("continue", 1),
          ("transfer", 2))
    )


_AdGenVoipScalarConfLocalPartyDisconnect_Type.__name__ = "Integer32"
_AdGenVoipScalarConfLocalPartyDisconnect_Object = MibScalar
adGenVoipScalarConfLocalPartyDisconnect = _AdGenVoipScalarConfLocalPartyDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 5),
    _AdGenVoipScalarConfLocalPartyDisconnect_Type()
)
adGenVoipScalarConfLocalPartyDisconnect.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarConfLocalPartyDisconnect.setStatus("current")


class _AdGenVoipScalarRtpUdpOffset_Type(Integer32):
    """Custom type adGenVoipScalarRtpUdpOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1026, 60000),
    )


_AdGenVoipScalarRtpUdpOffset_Type.__name__ = "Integer32"
_AdGenVoipScalarRtpUdpOffset_Object = MibScalar
adGenVoipScalarRtpUdpOffset = _AdGenVoipScalarRtpUdpOffset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 6),
    _AdGenVoipScalarRtpUdpOffset_Type()
)
adGenVoipScalarRtpUdpOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarRtpUdpOffset.setStatus("current")


class _AdGenVoipScalarSPREMode_Type(Integer32):
    """Custom type adGenVoipScalarSPREMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("local", 2))
    )


_AdGenVoipScalarSPREMode_Type.__name__ = "Integer32"
_AdGenVoipScalarSPREMode_Object = MibScalar
adGenVoipScalarSPREMode = _AdGenVoipScalarSPREMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 7),
    _AdGenVoipScalarSPREMode_Type()
)
adGenVoipScalarSPREMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarSPREMode.setStatus("current")


class _AdGenVoipScalarInterdigitTimer_Type(Integer32):
    """Custom type adGenVoipScalarInterdigitTimer based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AdGenVoipScalarInterdigitTimer_Type.__name__ = "Integer32"
_AdGenVoipScalarInterdigitTimer_Object = MibScalar
adGenVoipScalarInterdigitTimer = _AdGenVoipScalarInterdigitTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 8),
    _AdGenVoipScalarInterdigitTimer_Type()
)
adGenVoipScalarInterdigitTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarInterdigitTimer.setStatus("current")


class _AdGenVoipScalarAlertingTimer_Type(Integer32):
    """Custom type adGenVoipScalarAlertingTimer based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AdGenVoipScalarAlertingTimer_Type.__name__ = "Integer32"
_AdGenVoipScalarAlertingTimer_Object = MibScalar
adGenVoipScalarAlertingTimer = _AdGenVoipScalarAlertingTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 9),
    _AdGenVoipScalarAlertingTimer_Type()
)
adGenVoipScalarAlertingTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarAlertingTimer.setStatus("current")
_AdGenVoipScalarTransferOnHangup_Type = TruthValue
_AdGenVoipScalarTransferOnHangup_Object = MibScalar
adGenVoipScalarTransferOnHangup = _AdGenVoipScalarTransferOnHangup_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 10),
    _AdGenVoipScalarTransferOnHangup_Type()
)
adGenVoipScalarTransferOnHangup.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarTransferOnHangup.setStatus("current")


class _AdGenVoipScalarFlashhookThreholdMin_Type(Integer32):
    """Custom type adGenVoipScalarFlashhookThreholdMin based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 1550),
    )


_AdGenVoipScalarFlashhookThreholdMin_Type.__name__ = "Integer32"
_AdGenVoipScalarFlashhookThreholdMin_Object = MibScalar
adGenVoipScalarFlashhookThreholdMin = _AdGenVoipScalarFlashhookThreholdMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 11),
    _AdGenVoipScalarFlashhookThreholdMin_Type()
)
adGenVoipScalarFlashhookThreholdMin.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarFlashhookThreholdMin.setStatus("current")


class _AdGenVoipScalarFlashhookThreholdMax_Type(Integer32):
    """Custom type adGenVoipScalarFlashhookThreholdMax based on Integer32"""
    defaultValue = 1000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 1550),
    )


_AdGenVoipScalarFlashhookThreholdMax_Type.__name__ = "Integer32"
_AdGenVoipScalarFlashhookThreholdMax_Object = MibScalar
adGenVoipScalarFlashhookThreholdMax = _AdGenVoipScalarFlashhookThreholdMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 12),
    _AdGenVoipScalarFlashhookThreholdMax_Type()
)
adGenVoipScalarFlashhookThreholdMax.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarFlashhookThreholdMax.setStatus("current")


class _AdGenVoipScalarEmergencyNumberInhibitOnHook_Type(TruthValue):
    """Custom type adGenVoipScalarEmergencyNumberInhibitOnHook based on TruthValue"""
    defaultValue = 2


_AdGenVoipScalarEmergencyNumberInhibitOnHook_Type.__name__ = "TruthValue"
_AdGenVoipScalarEmergencyNumberInhibitOnHook_Object = MibScalar
adGenVoipScalarEmergencyNumberInhibitOnHook = _AdGenVoipScalarEmergencyNumberInhibitOnHook_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 13),
    _AdGenVoipScalarEmergencyNumberInhibitOnHook_Type()
)
adGenVoipScalarEmergencyNumberInhibitOnHook.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarEmergencyNumberInhibitOnHook.setStatus("current")


class _AdGenVoipScalarEmergencyNumberRingingTimemout_Type(Integer32):
    """Custom type adGenVoipScalarEmergencyNumberRingingTimemout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AdGenVoipScalarEmergencyNumberRingingTimemout_Type.__name__ = "Integer32"
_AdGenVoipScalarEmergencyNumberRingingTimemout_Object = MibScalar
adGenVoipScalarEmergencyNumberRingingTimemout = _AdGenVoipScalarEmergencyNumberRingingTimemout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 14),
    _AdGenVoipScalarEmergencyNumberRingingTimemout_Type()
)
adGenVoipScalarEmergencyNumberRingingTimemout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarEmergencyNumberRingingTimemout.setStatus("current")


class _AdGenVoipScalarDefaultSipTrunk_Type(DisplayString):
    """Custom type adGenVoipScalarDefaultSipTrunk based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_AdGenVoipScalarDefaultSipTrunk_Type.__name__ = "DisplayString"
_AdGenVoipScalarDefaultSipTrunk_Object = MibScalar
adGenVoipScalarDefaultSipTrunk = _AdGenVoipScalarDefaultSipTrunk_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 15),
    _AdGenVoipScalarDefaultSipTrunk_Type()
)
adGenVoipScalarDefaultSipTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarDefaultSipTrunk.setStatus("current")


class _AdGenVoipScalarConnectedTimer_Type(Integer32):
    """Custom type adGenVoipScalarConnectedTimer based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_AdGenVoipScalarConnectedTimer_Type.__name__ = "Integer32"
_AdGenVoipScalarConnectedTimer_Object = MibScalar
adGenVoipScalarConnectedTimer = _AdGenVoipScalarConnectedTimer_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 6, 16),
    _AdGenVoipScalarConnectedTimer_Type()
)
adGenVoipScalarConnectedTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarConnectedTimer.setStatus("current")
_AdGenVoipSPREMapScalarProv_ObjectIdentity = ObjectIdentity
adGenVoipSPREMapScalarProv = _AdGenVoipSPREMapScalarProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 7)
)


class _AdGenVoipScalarSPREMapDisableCallWaiting_Type(DisplayString):
    """Custom type adGenVoipScalarSPREMapDisableCallWaiting based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 49),
    )


_AdGenVoipScalarSPREMapDisableCallWaiting_Type.__name__ = "DisplayString"
_AdGenVoipScalarSPREMapDisableCallWaiting_Object = MibScalar
adGenVoipScalarSPREMapDisableCallWaiting = _AdGenVoipScalarSPREMapDisableCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 7, 1),
    _AdGenVoipScalarSPREMapDisableCallWaiting_Type()
)
adGenVoipScalarSPREMapDisableCallWaiting.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarSPREMapDisableCallWaiting.setStatus("current")


class _AdGenVoipScalarSPREMapDNDDisableEnable_Type(DisplayString):
    """Custom type adGenVoipScalarSPREMapDNDDisableEnable based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 49),
    )


_AdGenVoipScalarSPREMapDNDDisableEnable_Type.__name__ = "DisplayString"
_AdGenVoipScalarSPREMapDNDDisableEnable_Object = MibScalar
adGenVoipScalarSPREMapDNDDisableEnable = _AdGenVoipScalarSPREMapDNDDisableEnable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 7, 2),
    _AdGenVoipScalarSPREMapDNDDisableEnable_Type()
)
adGenVoipScalarSPREMapDNDDisableEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarSPREMapDNDDisableEnable.setStatus("current")


class _AdGenVoipScalarSPREMapBlockCallerID_Type(DisplayString):
    """Custom type adGenVoipScalarSPREMapBlockCallerID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 49),
    )


_AdGenVoipScalarSPREMapBlockCallerID_Type.__name__ = "DisplayString"
_AdGenVoipScalarSPREMapBlockCallerID_Object = MibScalar
adGenVoipScalarSPREMapBlockCallerID = _AdGenVoipScalarSPREMapBlockCallerID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 7, 3),
    _AdGenVoipScalarSPREMapBlockCallerID_Type()
)
adGenVoipScalarSPREMapBlockCallerID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipScalarSPREMapBlockCallerID.setStatus("current")
_AdGenVoipDialingProfileProv_ObjectIdentity = ObjectIdentity
adGenVoipDialingProfileProv = _AdGenVoipDialingProfileProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8)
)
_AdGenVoipDialingProfileDialPlanProv_ObjectIdentity = ObjectIdentity
adGenVoipDialingProfileDialPlanProv = _AdGenVoipDialingProfileDialPlanProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1)
)
_AdGenVoipDialingProfileDialPlanProvCurrentNumber_Type = Integer32
_AdGenVoipDialingProfileDialPlanProvCurrentNumber_Object = MibScalar
adGenVoipDialingProfileDialPlanProvCurrentNumber = _AdGenVoipDialingProfileDialPlanProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 1),
    _AdGenVoipDialingProfileDialPlanProvCurrentNumber_Type()
)
adGenVoipDialingProfileDialPlanProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanProvCurrentNumber.setStatus("current")
_AdGenVoipDialingProfileDialPlanProvLastCreateError_Type = DisplayString
_AdGenVoipDialingProfileDialPlanProvLastCreateError_Object = MibScalar
adGenVoipDialingProfileDialPlanProvLastCreateError = _AdGenVoipDialingProfileDialPlanProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 2),
    _AdGenVoipDialingProfileDialPlanProvLastCreateError_Type()
)
adGenVoipDialingProfileDialPlanProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanProvLastCreateError.setStatus("current")
_AdGenVoipDialingProfileDialPlanProvTable_Object = MibTable
adGenVoipDialingProfileDialPlanProvTable = _AdGenVoipDialingProfileDialPlanProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 3)
)
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanProvTable.setStatus("current")
_AdGenVoipDialingProfileDialPlanProvEntry_Object = MibTableRow
adGenVoipDialingProfileDialPlanProvEntry = _AdGenVoipDialingProfileDialPlanProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 3, 1)
)
adGenVoipDialingProfileDialPlanProvEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipDialingProfileDialPlanPatternEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanProvEntry.setStatus("current")


class _AdGenVoipDialingProfileDialPlanPatternEntryIndex_Type(DisplayString):
    """Custom type adGenVoipDialingProfileDialPlanPatternEntryIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 76),
    )


_AdGenVoipDialingProfileDialPlanPatternEntryIndex_Type.__name__ = "DisplayString"
_AdGenVoipDialingProfileDialPlanPatternEntryIndex_Object = MibTableColumn
adGenVoipDialingProfileDialPlanPatternEntryIndex = _AdGenVoipDialingProfileDialPlanPatternEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 3, 1, 1),
    _AdGenVoipDialingProfileDialPlanPatternEntryIndex_Type()
)
adGenVoipDialingProfileDialPlanPatternEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanPatternEntryIndex.setStatus("current")
_AdGenVoipDialingProfileDialPlanRowStatus_Type = RowStatus
_AdGenVoipDialingProfileDialPlanRowStatus_Object = MibTableColumn
adGenVoipDialingProfileDialPlanRowStatus = _AdGenVoipDialingProfileDialPlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 3, 1, 2),
    _AdGenVoipDialingProfileDialPlanRowStatus_Type()
)
adGenVoipDialingProfileDialPlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanRowStatus.setStatus("current")
_AdGenVoipDialingProfileDialPlanLastErrorString_Type = DisplayString
_AdGenVoipDialingProfileDialPlanLastErrorString_Object = MibTableColumn
adGenVoipDialingProfileDialPlanLastErrorString = _AdGenVoipDialingProfileDialPlanLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 3, 1, 3),
    _AdGenVoipDialingProfileDialPlanLastErrorString_Type()
)
adGenVoipDialingProfileDialPlanLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanLastErrorString.setStatus("current")


class _AdGenVoipDialingProfileDialPlanType_Type(Integer32):
    """Custom type adGenVoipDialingProfileDialPlanType based on Integer32"""
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
        *(("alwaysPermitted", 1),
          ("extensions", 2),
          ("local", 3),
          ("national", 4),
          ("tollFree", 5),
          ("a900Number", 6),
          ("international", 7),
          ("operatorAssisted", 8),
          ("specifyCarrier", 9),
          ("user1", 10),
          ("user2", 11),
          ("user3", 12))
    )


_AdGenVoipDialingProfileDialPlanType_Type.__name__ = "Integer32"
_AdGenVoipDialingProfileDialPlanType_Object = MibTableColumn
adGenVoipDialingProfileDialPlanType = _AdGenVoipDialingProfileDialPlanType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 3, 1, 4),
    _AdGenVoipDialingProfileDialPlanType_Type()
)
adGenVoipDialingProfileDialPlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanType.setStatus("current")


class _AdGenVoipDialingProfileDialPlanEmergencyNumber_Type(Integer32):
    """Custom type adGenVoipDialingProfileDialPlanEmergencyNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("isEmergencyNumber", 1),
          ("notEmergencyNumber", 2))
    )


_AdGenVoipDialingProfileDialPlanEmergencyNumber_Type.__name__ = "Integer32"
_AdGenVoipDialingProfileDialPlanEmergencyNumber_Object = MibTableColumn
adGenVoipDialingProfileDialPlanEmergencyNumber = _AdGenVoipDialingProfileDialPlanEmergencyNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 3, 1, 5),
    _AdGenVoipDialingProfileDialPlanEmergencyNumber_Type()
)
adGenVoipDialingProfileDialPlanEmergencyNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanEmergencyNumber.setStatus("current")


class _AdGenVoipDialingProfileDialPlanExternalLineCode_Type(Integer32):
    """Custom type adGenVoipDialingProfileDialPlanExternalLineCode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("optional", 1),
          ("prohibited", 2),
          ("required", 3))
    )


_AdGenVoipDialingProfileDialPlanExternalLineCode_Type.__name__ = "Integer32"
_AdGenVoipDialingProfileDialPlanExternalLineCode_Object = MibTableColumn
adGenVoipDialingProfileDialPlanExternalLineCode = _AdGenVoipDialingProfileDialPlanExternalLineCode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 3, 1, 6),
    _AdGenVoipDialingProfileDialPlanExternalLineCode_Type()
)
adGenVoipDialingProfileDialPlanExternalLineCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanExternalLineCode.setStatus("current")
_AdGenVoipDialingProfileDialPlanPattern_Type = DisplayString
_AdGenVoipDialingProfileDialPlanPattern_Object = MibTableColumn
adGenVoipDialingProfileDialPlanPattern = _AdGenVoipDialingProfileDialPlanPattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 3, 1, 7),
    _AdGenVoipDialingProfileDialPlanPattern_Type()
)
adGenVoipDialingProfileDialPlanPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanPattern.setStatus("current")
_AdGenVoipDialingProfileDialPlanDialingProfile_Type = AdGenVoipDialingProfileName
_AdGenVoipDialingProfileDialPlanDialingProfile_Object = MibTableColumn
adGenVoipDialingProfileDialPlanDialingProfile = _AdGenVoipDialingProfileDialPlanDialingProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 1, 3, 1, 8),
    _AdGenVoipDialingProfileDialPlanDialingProfile_Type()
)
adGenVoipDialingProfileDialPlanDialingProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileDialPlanDialingProfile.setStatus("current")
_AdGenVoipDialingProfileSPREPatternProv_ObjectIdentity = ObjectIdentity
adGenVoipDialingProfileSPREPatternProv = _AdGenVoipDialingProfileSPREPatternProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2)
)
_AdGenVoipDialingProfileSPREPatternProvCurrentNumber_Type = Integer32
_AdGenVoipDialingProfileSPREPatternProvCurrentNumber_Object = MibScalar
adGenVoipDialingProfileSPREPatternProvCurrentNumber = _AdGenVoipDialingProfileSPREPatternProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2, 1),
    _AdGenVoipDialingProfileSPREPatternProvCurrentNumber_Type()
)
adGenVoipDialingProfileSPREPatternProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileSPREPatternProvCurrentNumber.setStatus("current")
_AdGenVoipDialingProfileSPREPatternProvLastCreateError_Type = DisplayString
_AdGenVoipDialingProfileSPREPatternProvLastCreateError_Object = MibScalar
adGenVoipDialingProfileSPREPatternProvLastCreateError = _AdGenVoipDialingProfileSPREPatternProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2, 2),
    _AdGenVoipDialingProfileSPREPatternProvLastCreateError_Type()
)
adGenVoipDialingProfileSPREPatternProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileSPREPatternProvLastCreateError.setStatus("current")
_AdGenVoipDialingProfileSPREPatternProvTable_Object = MibTable
adGenVoipDialingProfileSPREPatternProvTable = _AdGenVoipDialingProfileSPREPatternProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2, 3)
)
if mibBuilder.loadTexts:
    adGenVoipDialingProfileSPREPatternProvTable.setStatus("current")
_AdGenVoipDialingProfileSPREPatternProvEntry_Object = MibTableRow
adGenVoipDialingProfileSPREPatternProvEntry = _AdGenVoipDialingProfileSPREPatternProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2, 3, 1)
)
adGenVoipDialingProfileSPREPatternProvEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipDialingProfileSPREPatternEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipDialingProfileSPREPatternProvEntry.setStatus("current")


class _AdGenVoipDialingProfileSPREPatternEntryIndex_Type(DisplayString):
    """Custom type adGenVoipDialingProfileSPREPatternEntryIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 80),
    )


_AdGenVoipDialingProfileSPREPatternEntryIndex_Type.__name__ = "DisplayString"
_AdGenVoipDialingProfileSPREPatternEntryIndex_Object = MibTableColumn
adGenVoipDialingProfileSPREPatternEntryIndex = _AdGenVoipDialingProfileSPREPatternEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2, 3, 1, 1),
    _AdGenVoipDialingProfileSPREPatternEntryIndex_Type()
)
adGenVoipDialingProfileSPREPatternEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileSPREPatternEntryIndex.setStatus("current")
_AdGenVoipDialingProfileSPREPatternRowStatus_Type = RowStatus
_AdGenVoipDialingProfileSPREPatternRowStatus_Object = MibTableColumn
adGenVoipDialingProfileSPREPatternRowStatus = _AdGenVoipDialingProfileSPREPatternRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2, 3, 1, 2),
    _AdGenVoipDialingProfileSPREPatternRowStatus_Type()
)
adGenVoipDialingProfileSPREPatternRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileSPREPatternRowStatus.setStatus("current")
_AdGenVoipDialingProfileSPREPatternLastErrorString_Type = DisplayString
_AdGenVoipDialingProfileSPREPatternLastErrorString_Object = MibTableColumn
adGenVoipDialingProfileSPREPatternLastErrorString = _AdGenVoipDialingProfileSPREPatternLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2, 3, 1, 3),
    _AdGenVoipDialingProfileSPREPatternLastErrorString_Type()
)
adGenVoipDialingProfileSPREPatternLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileSPREPatternLastErrorString.setStatus("current")


class _AdGenVoipDialingProfileSPREPatternTone_Type(Integer32):
    """Custom type adGenVoipDialingProfileSPREPatternTone based on Integer32"""
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
          ("dial", 2),
          ("stutterDial", 3))
    )


_AdGenVoipDialingProfileSPREPatternTone_Type.__name__ = "Integer32"
_AdGenVoipDialingProfileSPREPatternTone_Object = MibTableColumn
adGenVoipDialingProfileSPREPatternTone = _AdGenVoipDialingProfileSPREPatternTone_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2, 3, 1, 4),
    _AdGenVoipDialingProfileSPREPatternTone_Type()
)
adGenVoipDialingProfileSPREPatternTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileSPREPatternTone.setStatus("current")
_AdGenVoipDialingProfileSPREPattern_Type = DisplayString
_AdGenVoipDialingProfileSPREPattern_Object = MibTableColumn
adGenVoipDialingProfileSPREPattern = _AdGenVoipDialingProfileSPREPattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2, 3, 1, 5),
    _AdGenVoipDialingProfileSPREPattern_Type()
)
adGenVoipDialingProfileSPREPattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileSPREPattern.setStatus("current")
_AdGenVoipDialingProfileSPREPatternDialingProfile_Type = AdGenVoipDialingProfileName
_AdGenVoipDialingProfileSPREPatternDialingProfile_Object = MibTableColumn
adGenVoipDialingProfileSPREPatternDialingProfile = _AdGenVoipDialingProfileSPREPatternDialingProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 2, 3, 1, 6),
    _AdGenVoipDialingProfileSPREPatternDialingProfile_Type()
)
adGenVoipDialingProfileSPREPatternDialingProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileSPREPatternDialingProfile.setStatus("current")
_AdGenVoipDialingProfileExternalLineCodeProv_ObjectIdentity = ObjectIdentity
adGenVoipDialingProfileExternalLineCodeProv = _AdGenVoipDialingProfileExternalLineCodeProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3)
)
_AdGenVoipDialingProfileExternalLineCodeProvCurrentNumber_Type = Integer32
_AdGenVoipDialingProfileExternalLineCodeProvCurrentNumber_Object = MibScalar
adGenVoipDialingProfileExternalLineCodeProvCurrentNumber = _AdGenVoipDialingProfileExternalLineCodeProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3, 1),
    _AdGenVoipDialingProfileExternalLineCodeProvCurrentNumber_Type()
)
adGenVoipDialingProfileExternalLineCodeProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileExternalLineCodeProvCurrentNumber.setStatus("current")
_AdGenVoipDialingProfileExternalLineCodeProvLastCreateError_Type = DisplayString
_AdGenVoipDialingProfileExternalLineCodeProvLastCreateError_Object = MibScalar
adGenVoipDialingProfileExternalLineCodeProvLastCreateError = _AdGenVoipDialingProfileExternalLineCodeProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3, 2),
    _AdGenVoipDialingProfileExternalLineCodeProvLastCreateError_Type()
)
adGenVoipDialingProfileExternalLineCodeProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileExternalLineCodeProvLastCreateError.setStatus("current")
_AdGenVoipDialingProfileExternalLineCodeProvTable_Object = MibTable
adGenVoipDialingProfileExternalLineCodeProvTable = _AdGenVoipDialingProfileExternalLineCodeProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3, 3)
)
if mibBuilder.loadTexts:
    adGenVoipDialingProfileExternalLineCodeProvTable.setStatus("current")
_AdGenVoipDialingProfileExternalLineCodeProvEntry_Object = MibTableRow
adGenVoipDialingProfileExternalLineCodeProvEntry = _AdGenVoipDialingProfileExternalLineCodeProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3, 3, 1)
)
adGenVoipDialingProfileExternalLineCodeProvEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipDialingProfileExternalLineCodeEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipDialingProfileExternalLineCodeProvEntry.setStatus("current")


class _AdGenVoipDialingProfileExternalLineCodeEntryIndex_Type(DisplayString):
    """Custom type adGenVoipDialingProfileExternalLineCodeEntryIndex based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 80),
    )


_AdGenVoipDialingProfileExternalLineCodeEntryIndex_Type.__name__ = "DisplayString"
_AdGenVoipDialingProfileExternalLineCodeEntryIndex_Object = MibTableColumn
adGenVoipDialingProfileExternalLineCodeEntryIndex = _AdGenVoipDialingProfileExternalLineCodeEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3, 3, 1, 1),
    _AdGenVoipDialingProfileExternalLineCodeEntryIndex_Type()
)
adGenVoipDialingProfileExternalLineCodeEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileExternalLineCodeEntryIndex.setStatus("current")
_AdGenVoipDialingProfileExternalLineCodeRowStatus_Type = RowStatus
_AdGenVoipDialingProfileExternalLineCodeRowStatus_Object = MibTableColumn
adGenVoipDialingProfileExternalLineCodeRowStatus = _AdGenVoipDialingProfileExternalLineCodeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3, 3, 1, 2),
    _AdGenVoipDialingProfileExternalLineCodeRowStatus_Type()
)
adGenVoipDialingProfileExternalLineCodeRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileExternalLineCodeRowStatus.setStatus("current")
_AdGenVoipDialingProfileExternalLineCodeLastErrorString_Type = DisplayString
_AdGenVoipDialingProfileExternalLineCodeLastErrorString_Object = MibTableColumn
adGenVoipDialingProfileExternalLineCodeLastErrorString = _AdGenVoipDialingProfileExternalLineCodeLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3, 3, 1, 3),
    _AdGenVoipDialingProfileExternalLineCodeLastErrorString_Type()
)
adGenVoipDialingProfileExternalLineCodeLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileExternalLineCodeLastErrorString.setStatus("current")


class _AdGenVoipDialingProfileExternalLineCodeTone_Type(Integer32):
    """Custom type adGenVoipDialingProfileExternalLineCodeTone based on Integer32"""
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
          ("dial", 2),
          ("stutterDial", 3))
    )


_AdGenVoipDialingProfileExternalLineCodeTone_Type.__name__ = "Integer32"
_AdGenVoipDialingProfileExternalLineCodeTone_Object = MibTableColumn
adGenVoipDialingProfileExternalLineCodeTone = _AdGenVoipDialingProfileExternalLineCodeTone_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3, 3, 1, 4),
    _AdGenVoipDialingProfileExternalLineCodeTone_Type()
)
adGenVoipDialingProfileExternalLineCodeTone.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileExternalLineCodeTone.setStatus("current")
_AdGenVoipDialingProfileExternalLineCodePattern_Type = DisplayString
_AdGenVoipDialingProfileExternalLineCodePattern_Object = MibTableColumn
adGenVoipDialingProfileExternalLineCodePattern = _AdGenVoipDialingProfileExternalLineCodePattern_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3, 3, 1, 5),
    _AdGenVoipDialingProfileExternalLineCodePattern_Type()
)
adGenVoipDialingProfileExternalLineCodePattern.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileExternalLineCodePattern.setStatus("current")
_AdGenVoipDialingProfileExternalLineCodeDialingProfile_Type = AdGenVoipDialingProfileName
_AdGenVoipDialingProfileExternalLineCodeDialingProfile_Object = MibTableColumn
adGenVoipDialingProfileExternalLineCodeDialingProfile = _AdGenVoipDialingProfileExternalLineCodeDialingProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 3, 3, 1, 6),
    _AdGenVoipDialingProfileExternalLineCodeDialingProfile_Type()
)
adGenVoipDialingProfileExternalLineCodeDialingProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileExternalLineCodeDialingProfile.setStatus("current")
_AdGenVoipDialingProfileProvExt_ObjectIdentity = ObjectIdentity
adGenVoipDialingProfileProvExt = _AdGenVoipDialingProfileProvExt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 4)
)
_AdGenVoipDialingProfileProvExtTable_Object = MibTable
adGenVoipDialingProfileProvExtTable = _AdGenVoipDialingProfileProvExtTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 4, 1)
)
if mibBuilder.loadTexts:
    adGenVoipDialingProfileProvExtTable.setStatus("deprecated")
_AdGenVoipDialingProfileProvExtEntry_Object = MibTableRow
adGenVoipDialingProfileProvExtEntry = _AdGenVoipDialingProfileProvExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 4, 1, 1)
)
adGenVoipDialingProfileProvExtEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipDialingProfileProvExtEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipDialingProfileProvExtEntry.setStatus("deprecated")
_AdGenVoipDialingProfileProvExtEntryIndex_Type = AdGenVoipDialingProfileName
_AdGenVoipDialingProfileProvExtEntryIndex_Object = MibTableColumn
adGenVoipDialingProfileProvExtEntryIndex = _AdGenVoipDialingProfileProvExtEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 4, 1, 1, 1),
    _AdGenVoipDialingProfileProvExtEntryIndex_Type()
)
adGenVoipDialingProfileProvExtEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileProvExtEntryIndex.setStatus("deprecated")
_AdGenVoipDialingProfileProvExtNumVoiceUsers_Type = Unsigned32
_AdGenVoipDialingProfileProvExtNumVoiceUsers_Object = MibTableColumn
adGenVoipDialingProfileProvExtNumVoiceUsers = _AdGenVoipDialingProfileProvExtNumVoiceUsers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 4, 1, 1, 2),
    _AdGenVoipDialingProfileProvExtNumVoiceUsers_Type()
)
adGenVoipDialingProfileProvExtNumVoiceUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileProvExtNumVoiceUsers.setStatus("deprecated")


class _AdGenVoipDialingProfileProvExtRemoveProfile_Type(Integer32):
    """Custom type adGenVoipDialingProfileProvExtRemoveProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("remove", 1)
    )


_AdGenVoipDialingProfileProvExtRemoveProfile_Type.__name__ = "Integer32"
_AdGenVoipDialingProfileProvExtRemoveProfile_Object = MibTableColumn
adGenVoipDialingProfileProvExtRemoveProfile = _AdGenVoipDialingProfileProvExtRemoveProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 4, 1, 1, 3),
    _AdGenVoipDialingProfileProvExtRemoveProfile_Type()
)
adGenVoipDialingProfileProvExtRemoveProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileProvExtRemoveProfile.setStatus("deprecated")
_AdGenVoipDialingProfileCommonProv_ObjectIdentity = ObjectIdentity
adGenVoipDialingProfileCommonProv = _AdGenVoipDialingProfileCommonProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5)
)
_AdGenVoipDialingProfileCommonProvCurrentNumber_Type = Integer32
_AdGenVoipDialingProfileCommonProvCurrentNumber_Object = MibScalar
adGenVoipDialingProfileCommonProvCurrentNumber = _AdGenVoipDialingProfileCommonProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5, 1),
    _AdGenVoipDialingProfileCommonProvCurrentNumber_Type()
)
adGenVoipDialingProfileCommonProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileCommonProvCurrentNumber.setStatus("current")
_AdGenVoipDialingProfileCommonProvLastCreateError_Type = DisplayString
_AdGenVoipDialingProfileCommonProvLastCreateError_Object = MibScalar
adGenVoipDialingProfileCommonProvLastCreateError = _AdGenVoipDialingProfileCommonProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5, 2),
    _AdGenVoipDialingProfileCommonProvLastCreateError_Type()
)
adGenVoipDialingProfileCommonProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileCommonProvLastCreateError.setStatus("current")
_AdGenVoipDialingProfileCommonProvTable_Object = MibTable
adGenVoipDialingProfileCommonProvTable = _AdGenVoipDialingProfileCommonProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5, 3)
)
if mibBuilder.loadTexts:
    adGenVoipDialingProfileCommonProvTable.setStatus("current")
_AdGenVoipDialingProfileCommonProvEntry_Object = MibTableRow
adGenVoipDialingProfileCommonProvEntry = _AdGenVoipDialingProfileCommonProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5, 3, 1)
)
adGenVoipDialingProfileCommonProvEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipDialingProfileCommonProvEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipDialingProfileCommonProvEntry.setStatus("current")
_AdGenVoipDialingProfileCommonProvEntryIndex_Type = AdGenVoipDialingProfileName
_AdGenVoipDialingProfileCommonProvEntryIndex_Object = MibTableColumn
adGenVoipDialingProfileCommonProvEntryIndex = _AdGenVoipDialingProfileCommonProvEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5, 3, 1, 1),
    _AdGenVoipDialingProfileCommonProvEntryIndex_Type()
)
adGenVoipDialingProfileCommonProvEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileCommonProvEntryIndex.setStatus("current")
_AdGenVoipDialingProfileCommonProvNumVoiceUsers_Type = Unsigned32
_AdGenVoipDialingProfileCommonProvNumVoiceUsers_Object = MibTableColumn
adGenVoipDialingProfileCommonProvNumVoiceUsers = _AdGenVoipDialingProfileCommonProvNumVoiceUsers_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5, 3, 1, 2),
    _AdGenVoipDialingProfileCommonProvNumVoiceUsers_Type()
)
adGenVoipDialingProfileCommonProvNumVoiceUsers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileCommonProvNumVoiceUsers.setStatus("current")


class _AdGenVoipDialingProfileCommonProvRemoveProfile_Type(Integer32):
    """Custom type adGenVoipDialingProfileCommonProvRemoveProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("remove", 1)
    )


_AdGenVoipDialingProfileCommonProvRemoveProfile_Type.__name__ = "Integer32"
_AdGenVoipDialingProfileCommonProvRemoveProfile_Object = MibTableColumn
adGenVoipDialingProfileCommonProvRemoveProfile = _AdGenVoipDialingProfileCommonProvRemoveProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5, 3, 1, 3),
    _AdGenVoipDialingProfileCommonProvRemoveProfile_Type()
)
adGenVoipDialingProfileCommonProvRemoveProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileCommonProvRemoveProfile.setStatus("current")


class _AdGenVoipDialingProfileCommonProvDescription_Type(DisplayString):
    """Custom type adGenVoipDialingProfileCommonProvDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AdGenVoipDialingProfileCommonProvDescription_Type.__name__ = "DisplayString"
_AdGenVoipDialingProfileCommonProvDescription_Object = MibTableColumn
adGenVoipDialingProfileCommonProvDescription = _AdGenVoipDialingProfileCommonProvDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5, 3, 1, 4),
    _AdGenVoipDialingProfileCommonProvDescription_Type()
)
adGenVoipDialingProfileCommonProvDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileCommonProvDescription.setStatus("current")
_AdGenVoipDialingProfileCommonProvRowStatus_Type = RowStatus
_AdGenVoipDialingProfileCommonProvRowStatus_Object = MibTableColumn
adGenVoipDialingProfileCommonProvRowStatus = _AdGenVoipDialingProfileCommonProvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5, 3, 1, 5),
    _AdGenVoipDialingProfileCommonProvRowStatus_Type()
)
adGenVoipDialingProfileCommonProvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileCommonProvRowStatus.setStatus("current")
_AdGenVoipDialingProfileCommonProvLastErrorString_Type = DisplayString
_AdGenVoipDialingProfileCommonProvLastErrorString_Object = MibTableColumn
adGenVoipDialingProfileCommonProvLastErrorString = _AdGenVoipDialingProfileCommonProvLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 8, 5, 3, 1, 6),
    _AdGenVoipDialingProfileCommonProvLastErrorString_Type()
)
adGenVoipDialingProfileCommonProvLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipDialingProfileCommonProvLastErrorString.setStatus("current")
_AdGenVoipCodecProfileNameProv_ObjectIdentity = ObjectIdentity
adGenVoipCodecProfileNameProv = _AdGenVoipCodecProfileNameProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 9)
)
_AdGenVoipCodecProfileNameProvCurrentNumber_Type = Integer32
_AdGenVoipCodecProfileNameProvCurrentNumber_Object = MibScalar
adGenVoipCodecProfileNameProvCurrentNumber = _AdGenVoipCodecProfileNameProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 9, 1),
    _AdGenVoipCodecProfileNameProvCurrentNumber_Type()
)
adGenVoipCodecProfileNameProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipCodecProfileNameProvCurrentNumber.setStatus("current")
_AdGenVoipCodecProfileNameProvLastCreateError_Type = DisplayString
_AdGenVoipCodecProfileNameProvLastCreateError_Object = MibScalar
adGenVoipCodecProfileNameProvLastCreateError = _AdGenVoipCodecProfileNameProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 9, 2),
    _AdGenVoipCodecProfileNameProvLastCreateError_Type()
)
adGenVoipCodecProfileNameProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipCodecProfileNameProvLastCreateError.setStatus("current")
_AdGenVoipCodecProfileNameProvTable_Object = MibTable
adGenVoipCodecProfileNameProvTable = _AdGenVoipCodecProfileNameProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 9, 3)
)
if mibBuilder.loadTexts:
    adGenVoipCodecProfileNameProvTable.setStatus("current")
_AdGenVoipCodecProfileNameProvEntry_Object = MibTableRow
adGenVoipCodecProfileNameProvEntry = _AdGenVoipCodecProfileNameProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 9, 3, 1)
)
adGenVoipCodecProfileNameProvEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipCodecProfileNameProvIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipCodecProfileNameProvEntry.setStatus("current")
_AdGenVoipCodecProfileNameProvIndex_Type = AdGenVoipCodecProfileName
_AdGenVoipCodecProfileNameProvIndex_Object = MibTableColumn
adGenVoipCodecProfileNameProvIndex = _AdGenVoipCodecProfileNameProvIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 9, 3, 1, 1),
    _AdGenVoipCodecProfileNameProvIndex_Type()
)
adGenVoipCodecProfileNameProvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipCodecProfileNameProvIndex.setStatus("current")
_AdGenVoipCodecProfileNameProvRowStatus_Type = RowStatus
_AdGenVoipCodecProfileNameProvRowStatus_Object = MibTableColumn
adGenVoipCodecProfileNameProvRowStatus = _AdGenVoipCodecProfileNameProvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 9, 3, 1, 2),
    _AdGenVoipCodecProfileNameProvRowStatus_Type()
)
adGenVoipCodecProfileNameProvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCodecProfileNameProvRowStatus.setStatus("current")
_AdGenVoipCodecProfileNameProvLastErrorString_Type = DisplayString
_AdGenVoipCodecProfileNameProvLastErrorString_Object = MibTableColumn
adGenVoipCodecProfileNameProvLastErrorString = _AdGenVoipCodecProfileNameProvLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 9, 3, 1, 3),
    _AdGenVoipCodecProfileNameProvLastErrorString_Type()
)
adGenVoipCodecProfileNameProvLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipCodecProfileNameProvLastErrorString.setStatus("current")
_AdGenVoipCodecProfilePreferenceLastCreateError_Type = DisplayString
_AdGenVoipCodecProfilePreferenceLastCreateError_Object = MibTableColumn
adGenVoipCodecProfilePreferenceLastCreateError = _AdGenVoipCodecProfilePreferenceLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 9, 3, 1, 4),
    _AdGenVoipCodecProfilePreferenceLastCreateError_Type()
)
adGenVoipCodecProfilePreferenceLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipCodecProfilePreferenceLastCreateError.setStatus("current")
_AdGenVoipCodecProfileProv_ObjectIdentity = ObjectIdentity
adGenVoipCodecProfileProv = _AdGenVoipCodecProfileProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 10)
)
_AdGenVoipCodecProfileProvTable_Object = MibTable
adGenVoipCodecProfileProvTable = _AdGenVoipCodecProfileProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 10, 1)
)
if mibBuilder.loadTexts:
    adGenVoipCodecProfileProvTable.setStatus("current")
_AdGenVoipCodecProfileProvEntry_Object = MibTableRow
adGenVoipCodecProfileProvEntry = _AdGenVoipCodecProfileProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 10, 1, 1)
)
adGenVoipCodecProfileProvEntry.setIndexNames(
    (0, "ADTRAN-GENVOIP-MIB", "adGenVoipCodecProfileNameProvIndex"),
    (0, "ADTRAN-GENVOIP-MIB", "adGenVoipCodecProfileProvIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipCodecProfileProvEntry.setStatus("current")
_AdGenVoipCodecProfileProvIndex_Type = Unsigned32
_AdGenVoipCodecProfileProvIndex_Object = MibTableColumn
adGenVoipCodecProfileProvIndex = _AdGenVoipCodecProfileProvIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 10, 1, 1, 1),
    _AdGenVoipCodecProfileProvIndex_Type()
)
adGenVoipCodecProfileProvIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipCodecProfileProvIndex.setStatus("current")
_AdGenVoipCodecProfileProvRowStatus_Type = RowStatus
_AdGenVoipCodecProfileProvRowStatus_Object = MibTableColumn
adGenVoipCodecProfileProvRowStatus = _AdGenVoipCodecProfileProvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 10, 1, 1, 2),
    _AdGenVoipCodecProfileProvRowStatus_Type()
)
adGenVoipCodecProfileProvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCodecProfileProvRowStatus.setStatus("current")
_AdGenVoipCodecProfileProvLastErrorString_Type = DisplayString
_AdGenVoipCodecProfileProvLastErrorString_Object = MibTableColumn
adGenVoipCodecProfileProvLastErrorString = _AdGenVoipCodecProfileProvLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 10, 1, 1, 3),
    _AdGenVoipCodecProfileProvLastErrorString_Type()
)
adGenVoipCodecProfileProvLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipCodecProfileProvLastErrorString.setStatus("current")


class _AdGenVoipCodecProfileProvPreference_Type(AdGenVoipCodecProfileType):
    """Custom type adGenVoipCodecProfileProvPreference based on AdGenVoipCodecProfileType"""
    defaultValue = 1


_AdGenVoipCodecProfileProvPreference_Type.__name__ = "AdGenVoipCodecProfileType"
_AdGenVoipCodecProfileProvPreference_Object = MibTableColumn
adGenVoipCodecProfileProvPreference = _AdGenVoipCodecProfileProvPreference_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 10, 1, 1, 4),
    _AdGenVoipCodecProfileProvPreference_Type()
)
adGenVoipCodecProfileProvPreference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCodecProfileProvPreference.setStatus("current")
_AdGenVoipMediaProfileProv_ObjectIdentity = ObjectIdentity
adGenVoipMediaProfileProv = _AdGenVoipMediaProfileProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11)
)
_AdGenVoipMediaProfileProvCurrentNumber_Type = Integer32
_AdGenVoipMediaProfileProvCurrentNumber_Object = MibScalar
adGenVoipMediaProfileProvCurrentNumber = _AdGenVoipMediaProfileProvCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 1),
    _AdGenVoipMediaProfileProvCurrentNumber_Type()
)
adGenVoipMediaProfileProvCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvCurrentNumber.setStatus("current")
_AdGenVoipMediaProfileProvLastCreateError_Type = DisplayString
_AdGenVoipMediaProfileProvLastCreateError_Object = MibScalar
adGenVoipMediaProfileProvLastCreateError = _AdGenVoipMediaProfileProvLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 2),
    _AdGenVoipMediaProfileProvLastCreateError_Type()
)
adGenVoipMediaProfileProvLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvLastCreateError.setStatus("current")
_AdGenVoipMediaProfileProvTable_Object = MibTable
adGenVoipMediaProfileProvTable = _AdGenVoipMediaProfileProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3)
)
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvTable.setStatus("current")
_AdGenVoipMediaProfileProvEntry_Object = MibTableRow
adGenVoipMediaProfileProvEntry = _AdGenVoipMediaProfileProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1)
)
adGenVoipMediaProfileProvEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipMediaProfileProvEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvEntry.setStatus("current")
_AdGenVoipMediaProfileProvEntryIndex_Type = AdGenVoipMediaProfileName
_AdGenVoipMediaProfileProvEntryIndex_Object = MibTableColumn
adGenVoipMediaProfileProvEntryIndex = _AdGenVoipMediaProfileProvEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 1),
    _AdGenVoipMediaProfileProvEntryIndex_Type()
)
adGenVoipMediaProfileProvEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvEntryIndex.setStatus("current")
_AdGenVoipMediaProfileProvRowStatus_Type = RowStatus
_AdGenVoipMediaProfileProvRowStatus_Object = MibTableColumn
adGenVoipMediaProfileProvRowStatus = _AdGenVoipMediaProfileProvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 2),
    _AdGenVoipMediaProfileProvRowStatus_Type()
)
adGenVoipMediaProfileProvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRowStatus.setStatus("current")
_AdGenVoipMediaProfileProvLastErrorString_Type = DisplayString
_AdGenVoipMediaProfileProvLastErrorString_Object = MibTableColumn
adGenVoipMediaProfileProvLastErrorString = _AdGenVoipMediaProfileProvLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 3),
    _AdGenVoipMediaProfileProvLastErrorString_Type()
)
adGenVoipMediaProfileProvLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvLastErrorString.setStatus("current")


class _AdGenVoipMediaProfileProvRtpFramePktization_Type(Unsigned32):
    """Custom type adGenVoipMediaProfileProvRtpFramePktization based on Unsigned32"""
    defaultValue = 10


_AdGenVoipMediaProfileProvRtpFramePktization_Type.__name__ = "Unsigned32"
_AdGenVoipMediaProfileProvRtpFramePktization_Object = MibTableColumn
adGenVoipMediaProfileProvRtpFramePktization = _AdGenVoipMediaProfileProvRtpFramePktization_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 4),
    _AdGenVoipMediaProfileProvRtpFramePktization_Type()
)
adGenVoipMediaProfileProvRtpFramePktization.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpFramePktization.setStatus("current")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpFramePktization.setUnits("milliseconds")


class _AdGenVoipMediaProfileProvRtpPktDelayNominal_Type(Unsigned32):
    """Custom type adGenVoipMediaProfileProvRtpPktDelayNominal based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 240),
    )


_AdGenVoipMediaProfileProvRtpPktDelayNominal_Type.__name__ = "Unsigned32"
_AdGenVoipMediaProfileProvRtpPktDelayNominal_Object = MibTableColumn
adGenVoipMediaProfileProvRtpPktDelayNominal = _AdGenVoipMediaProfileProvRtpPktDelayNominal_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 5),
    _AdGenVoipMediaProfileProvRtpPktDelayNominal_Type()
)
adGenVoipMediaProfileProvRtpPktDelayNominal.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpPktDelayNominal.setStatus("current")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpPktDelayNominal.setUnits("milliseconds")


class _AdGenVoipMediaProfileProvRtpPktDelayMaximum_Type(Unsigned32):
    """Custom type adGenVoipMediaProfileProvRtpPktDelayMaximum based on Unsigned32"""
    defaultValue = 100

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 320),
    )


_AdGenVoipMediaProfileProvRtpPktDelayMaximum_Type.__name__ = "Unsigned32"
_AdGenVoipMediaProfileProvRtpPktDelayMaximum_Object = MibTableColumn
adGenVoipMediaProfileProvRtpPktDelayMaximum = _AdGenVoipMediaProfileProvRtpPktDelayMaximum_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 6),
    _AdGenVoipMediaProfileProvRtpPktDelayMaximum_Type()
)
adGenVoipMediaProfileProvRtpPktDelayMaximum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpPktDelayMaximum.setStatus("current")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpPktDelayMaximum.setUnits("milliseconds")


class _AdGenVoipMediaProfileProvRtpDtmfRelay_Type(Unsigned32):
    """Custom type adGenVoipMediaProfileProvRtpDtmfRelay based on Unsigned32"""
    defaultValue = 2


_AdGenVoipMediaProfileProvRtpDtmfRelay_Type.__name__ = "Unsigned32"
_AdGenVoipMediaProfileProvRtpDtmfRelay_Object = MibTableColumn
adGenVoipMediaProfileProvRtpDtmfRelay = _AdGenVoipMediaProfileProvRtpDtmfRelay_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 7),
    _AdGenVoipMediaProfileProvRtpDtmfRelay_Type()
)
adGenVoipMediaProfileProvRtpDtmfRelay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpDtmfRelay.setStatus("current")


class _AdGenVoipMediaProfileProvRtpQosDscp_Type(Unsigned32):
    """Custom type adGenVoipMediaProfileProvRtpQosDscp based on Unsigned32"""
    defaultValue = 46

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AdGenVoipMediaProfileProvRtpQosDscp_Type.__name__ = "Unsigned32"
_AdGenVoipMediaProfileProvRtpQosDscp_Object = MibTableColumn
adGenVoipMediaProfileProvRtpQosDscp = _AdGenVoipMediaProfileProvRtpQosDscp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 8),
    _AdGenVoipMediaProfileProvRtpQosDscp_Type()
)
adGenVoipMediaProfileProvRtpQosDscp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpQosDscp.setStatus("current")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpQosDscp.setUnits("priority")


class _AdGenVoipMediaProfileProvRtpLocalPortMin_Type(Unsigned32):
    """Custom type adGenVoipMediaProfileProvRtpLocalPortMin based on Unsigned32"""
    defaultValue = 10000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1026, 60000),
    )


_AdGenVoipMediaProfileProvRtpLocalPortMin_Type.__name__ = "Unsigned32"
_AdGenVoipMediaProfileProvRtpLocalPortMin_Object = MibTableColumn
adGenVoipMediaProfileProvRtpLocalPortMin = _AdGenVoipMediaProfileProvRtpLocalPortMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 9),
    _AdGenVoipMediaProfileProvRtpLocalPortMin_Type()
)
adGenVoipMediaProfileProvRtpLocalPortMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpLocalPortMin.setStatus("current")


class _AdGenVoipMediaProfileProvRtpLocalPortMax_Type(Unsigned32):
    """Custom type adGenVoipMediaProfileProvRtpLocalPortMax based on Unsigned32"""
    defaultValue = 60000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1026, 60000),
    )


_AdGenVoipMediaProfileProvRtpLocalPortMax_Type.__name__ = "Unsigned32"
_AdGenVoipMediaProfileProvRtpLocalPortMax_Object = MibTableColumn
adGenVoipMediaProfileProvRtpLocalPortMax = _AdGenVoipMediaProfileProvRtpLocalPortMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 10),
    _AdGenVoipMediaProfileProvRtpLocalPortMax_Type()
)
adGenVoipMediaProfileProvRtpLocalPortMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvRtpLocalPortMax.setStatus("current")


class _AdGenVoipMediaProfileProvFaxMode_Type(Integer32):
    """Custom type adGenVoipMediaProfileProvFaxMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("modemPassThrough", 1),
          ("t38", 2))
    )


_AdGenVoipMediaProfileProvFaxMode_Type.__name__ = "Integer32"
_AdGenVoipMediaProfileProvFaxMode_Object = MibTableColumn
adGenVoipMediaProfileProvFaxMode = _AdGenVoipMediaProfileProvFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 11),
    _AdGenVoipMediaProfileProvFaxMode_Type()
)
adGenVoipMediaProfileProvFaxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvFaxMode.setStatus("current")


class _AdGenVoipMediaProfileProvEchoCancellation_Type(Integer32):
    """Custom type adGenVoipMediaProfileProvEchoCancellation based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenVoipMediaProfileProvEchoCancellation_Type.__name__ = "Integer32"
_AdGenVoipMediaProfileProvEchoCancellation_Object = MibTableColumn
adGenVoipMediaProfileProvEchoCancellation = _AdGenVoipMediaProfileProvEchoCancellation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 12),
    _AdGenVoipMediaProfileProvEchoCancellation_Type()
)
adGenVoipMediaProfileProvEchoCancellation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvEchoCancellation.setStatus("current")


class _AdGenVoipMediaProfileProvFlashHookMin_Type(Unsigned32):
    """Custom type adGenVoipMediaProfileProvFlashHookMin based on Unsigned32"""
    defaultValue = 300

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 1550),
    )


_AdGenVoipMediaProfileProvFlashHookMin_Type.__name__ = "Unsigned32"
_AdGenVoipMediaProfileProvFlashHookMin_Object = MibTableColumn
adGenVoipMediaProfileProvFlashHookMin = _AdGenVoipMediaProfileProvFlashHookMin_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 13),
    _AdGenVoipMediaProfileProvFlashHookMin_Type()
)
adGenVoipMediaProfileProvFlashHookMin.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvFlashHookMin.setStatus("current")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvFlashHookMin.setUnits("milliseconds")


class _AdGenVoipMediaProfileProvFlashHookMax_Type(Unsigned32):
    """Custom type adGenVoipMediaProfileProvFlashHookMax based on Unsigned32"""
    defaultValue = 1000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(40, 1550),
    )


_AdGenVoipMediaProfileProvFlashHookMax_Type.__name__ = "Unsigned32"
_AdGenVoipMediaProfileProvFlashHookMax_Object = MibTableColumn
adGenVoipMediaProfileProvFlashHookMax = _AdGenVoipMediaProfileProvFlashHookMax_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 14),
    _AdGenVoipMediaProfileProvFlashHookMax_Type()
)
adGenVoipMediaProfileProvFlashHookMax.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvFlashHookMax.setStatus("current")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvFlashHookMax.setUnits("milliseconds")


class _AdGenVoipMediaProfileProvVAD_Type(Integer32):
    """Custom type adGenVoipMediaProfileProvVAD based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_AdGenVoipMediaProfileProvVAD_Type.__name__ = "Integer32"
_AdGenVoipMediaProfileProvVAD_Object = MibTableColumn
adGenVoipMediaProfileProvVAD = _AdGenVoipMediaProfileProvVAD_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 11, 3, 1, 15),
    _AdGenVoipMediaProfileProvVAD_Type()
)
adGenVoipMediaProfileProvVAD.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipMediaProfileProvVAD.setStatus("current")
_AdGenVoipCallFeatureProfileProv_ObjectIdentity = ObjectIdentity
adGenVoipCallFeatureProfileProv = _AdGenVoipCallFeatureProfileProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12)
)
_AdGenVoipCallFeatureProfileCurrentNumber_Type = Integer32
_AdGenVoipCallFeatureProfileCurrentNumber_Object = MibScalar
adGenVoipCallFeatureProfileCurrentNumber = _AdGenVoipCallFeatureProfileCurrentNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 1),
    _AdGenVoipCallFeatureProfileCurrentNumber_Type()
)
adGenVoipCallFeatureProfileCurrentNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileCurrentNumber.setStatus("current")
_AdGenVoipCallFeatureProfileLastCreateError_Type = DisplayString
_AdGenVoipCallFeatureProfileLastCreateError_Object = MibScalar
adGenVoipCallFeatureProfileLastCreateError = _AdGenVoipCallFeatureProfileLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 2),
    _AdGenVoipCallFeatureProfileLastCreateError_Type()
)
adGenVoipCallFeatureProfileLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileLastCreateError.setStatus("current")
_AdGenVoipCallFeatureProfileProvTable_Object = MibTable
adGenVoipCallFeatureProfileProvTable = _AdGenVoipCallFeatureProfileProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3)
)
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileProvTable.setStatus("current")
_AdGenVoipCallFeatureProfileProvEntry_Object = MibTableRow
adGenVoipCallFeatureProfileProvEntry = _AdGenVoipCallFeatureProfileProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1)
)
adGenVoipCallFeatureProfileProvEntry.setIndexNames(
    (1, "ADTRAN-GENVOIP-MIB", "adGenVoipCallFeatureProfileEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileProvEntry.setStatus("current")
_AdGenVoipCallFeatureProfileEntryIndex_Type = AdGenVoipCallFeatureProfileName
_AdGenVoipCallFeatureProfileEntryIndex_Object = MibTableColumn
adGenVoipCallFeatureProfileEntryIndex = _AdGenVoipCallFeatureProfileEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 1),
    _AdGenVoipCallFeatureProfileEntryIndex_Type()
)
adGenVoipCallFeatureProfileEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileEntryIndex.setStatus("current")
_AdGenVoipCallFeatureProfileRowStatus_Type = RowStatus
_AdGenVoipCallFeatureProfileRowStatus_Object = MibTableColumn
adGenVoipCallFeatureProfileRowStatus = _AdGenVoipCallFeatureProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 2),
    _AdGenVoipCallFeatureProfileRowStatus_Type()
)
adGenVoipCallFeatureProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileRowStatus.setStatus("current")
_AdGenVoipCallFeatureProfileLastErrorString_Type = DisplayString
_AdGenVoipCallFeatureProfileLastErrorString_Object = MibTableColumn
adGenVoipCallFeatureProfileLastErrorString = _AdGenVoipCallFeatureProfileLastErrorString_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 3),
    _AdGenVoipCallFeatureProfileLastErrorString_Type()
)
adGenVoipCallFeatureProfileLastErrorString.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileLastErrorString.setStatus("current")


class _AdGenVoipCallFeatureProfileEmergencyNumberRingingTimeout_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout based on Integer32"""
    defaultValue = 10

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AdGenVoipCallFeatureProfileEmergencyNumberRingingTimeout_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileEmergencyNumberRingingTimeout_Object = MibTableColumn
adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout = _AdGenVoipCallFeatureProfileEmergencyNumberRingingTimeout_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 4),
    _AdGenVoipCallFeatureProfileEmergencyNumberRingingTimeout_Type()
)
adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout.setStatus("current")


class _AdGenVoipCallFeatureProfileEmergencyNumberOnhook_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileEmergencyNumberOnhook based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("inhibit", 1),
          ("allow", 2))
    )


_AdGenVoipCallFeatureProfileEmergencyNumberOnhook_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileEmergencyNumberOnhook_Object = MibTableColumn
adGenVoipCallFeatureProfileEmergencyNumberOnhook = _AdGenVoipCallFeatureProfileEmergencyNumberOnhook_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 5),
    _AdGenVoipCallFeatureProfileEmergencyNumberOnhook_Type()
)
adGenVoipCallFeatureProfileEmergencyNumberOnhook.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileEmergencyNumberOnhook.setStatus("current")


class _AdGenVoipCallFeatureProfileCallWaiting_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileCallWaiting based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenVoipCallFeatureProfileCallWaiting_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileCallWaiting_Object = MibTableColumn
adGenVoipCallFeatureProfileCallWaiting = _AdGenVoipCallFeatureProfileCallWaiting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 6),
    _AdGenVoipCallFeatureProfileCallWaiting_Type()
)
adGenVoipCallFeatureProfileCallWaiting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileCallWaiting.setStatus("current")


class _AdGenVoipCallFeatureProfileCallerIdInbound_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileCallerIdInbound based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenVoipCallFeatureProfileCallerIdInbound_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileCallerIdInbound_Object = MibTableColumn
adGenVoipCallFeatureProfileCallerIdInbound = _AdGenVoipCallFeatureProfileCallerIdInbound_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 7),
    _AdGenVoipCallFeatureProfileCallerIdInbound_Type()
)
adGenVoipCallFeatureProfileCallerIdInbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileCallerIdInbound.setStatus("current")


class _AdGenVoipCallFeatureProfileCallerIdOutbound_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileCallerIdOutbound based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenVoipCallFeatureProfileCallerIdOutbound_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileCallerIdOutbound_Object = MibTableColumn
adGenVoipCallFeatureProfileCallerIdOutbound = _AdGenVoipCallFeatureProfileCallerIdOutbound_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 8),
    _AdGenVoipCallFeatureProfileCallerIdOutbound_Type()
)
adGenVoipCallFeatureProfileCallerIdOutbound.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileCallerIdOutbound.setStatus("current")


class _AdGenVoipCallFeatureProfileTransferOnHangup_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileTransferOnHangup based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_AdGenVoipCallFeatureProfileTransferOnHangup_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileTransferOnHangup_Object = MibTableColumn
adGenVoipCallFeatureProfileTransferOnHangup = _AdGenVoipCallFeatureProfileTransferOnHangup_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 9),
    _AdGenVoipCallFeatureProfileTransferOnHangup_Type()
)
adGenVoipCallFeatureProfileTransferOnHangup.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileTransferOnHangup.setStatus("current")


class _AdGenVoipCallFeatureProfileTimeoutAlerting_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileTimeoutAlerting based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60),
    )


_AdGenVoipCallFeatureProfileTimeoutAlerting_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileTimeoutAlerting_Object = MibTableColumn
adGenVoipCallFeatureProfileTimeoutAlerting = _AdGenVoipCallFeatureProfileTimeoutAlerting_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 10),
    _AdGenVoipCallFeatureProfileTimeoutAlerting_Type()
)
adGenVoipCallFeatureProfileTimeoutAlerting.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileTimeoutAlerting.setStatus("current")


class _AdGenVoipCallFeatureProfileTimeoutInterdigit_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileTimeoutInterdigit based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 16),
    )


_AdGenVoipCallFeatureProfileTimeoutInterdigit_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileTimeoutInterdigit_Object = MibTableColumn
adGenVoipCallFeatureProfileTimeoutInterdigit = _AdGenVoipCallFeatureProfileTimeoutInterdigit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 11),
    _AdGenVoipCallFeatureProfileTimeoutInterdigit_Type()
)
adGenVoipCallFeatureProfileTimeoutInterdigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileTimeoutInterdigit.setStatus("current")


class _AdGenVoipCallFeatureProfileConference_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileConference based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disabled", 2))
    )


_AdGenVoipCallFeatureProfileConference_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileConference_Object = MibTableColumn
adGenVoipCallFeatureProfileConference = _AdGenVoipCallFeatureProfileConference_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 12),
    _AdGenVoipCallFeatureProfileConference_Type()
)
adGenVoipCallFeatureProfileConference.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileConference.setStatus("current")


class _AdGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook based on Integer32"""
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
        *(("drop", 1),
          ("ignore", 2),
          ("split", 3))
    )


_AdGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook_Object = MibTableColumn
adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook = _AdGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 13),
    _AdGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook_Type()
)
adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook.setStatus("current")


class _AdGenVoipCallFeatureProfileFeatureMode_Type(Integer32):
    """Custom type adGenVoipCallFeatureProfileFeatureMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("network", 1),
          ("local", 2))
    )


_AdGenVoipCallFeatureProfileFeatureMode_Type.__name__ = "Integer32"
_AdGenVoipCallFeatureProfileFeatureMode_Object = MibTableColumn
adGenVoipCallFeatureProfileFeatureMode = _AdGenVoipCallFeatureProfileFeatureMode_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 12, 3, 1, 14),
    _AdGenVoipCallFeatureProfileFeatureMode_Type()
)
adGenVoipCallFeatureProfileFeatureMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenVoipCallFeatureProfileFeatureMode.setStatus("current")
_AdGenVoipUserReverseLookup_ObjectIdentity = ObjectIdentity
adGenVoipUserReverseLookup = _AdGenVoipUserReverseLookup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 13)
)
_AdGenVoipUserReverseLookupTable_Object = MibTable
adGenVoipUserReverseLookupTable = _AdGenVoipUserReverseLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 13, 1)
)
if mibBuilder.loadTexts:
    adGenVoipUserReverseLookupTable.setStatus("current")
_AdGenVoipUserReverseLookupTableEntry_Object = MibTableRow
adGenVoipUserReverseLookupTableEntry = _AdGenVoipUserReverseLookupTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 13, 1, 1)
)
adGenVoipUserReverseLookupTableEntry.setIndexNames(
    (0, "ADTRAN-GENVOIP-MIB", "adGenVoipUserReverseLookupTableEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipUserReverseLookupTableEntry.setStatus("current")
_AdGenVoipUserReverseLookupTableEntryIndex_Type = AdGenVoipCallReverseLookupIfIndex
_AdGenVoipUserReverseLookupTableEntryIndex_Object = MibTableColumn
adGenVoipUserReverseLookupTableEntryIndex = _AdGenVoipUserReverseLookupTableEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 13, 1, 1, 1),
    _AdGenVoipUserReverseLookupTableEntryIndex_Type()
)
adGenVoipUserReverseLookupTableEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipUserReverseLookupTableEntryIndex.setStatus("current")
_AdGenVoipUserReverseLookupTableUserName_Type = DisplayString
_AdGenVoipUserReverseLookupTableUserName_Object = MibTableColumn
adGenVoipUserReverseLookupTableUserName = _AdGenVoipUserReverseLookupTableUserName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 13, 1, 1, 2),
    _AdGenVoipUserReverseLookupTableUserName_Type()
)
adGenVoipUserReverseLookupTableUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipUserReverseLookupTableUserName.setStatus("current")
_AdGenVoipSDPProv_ObjectIdentity = ObjectIdentity
adGenVoipSDPProv = _AdGenVoipSDPProv_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 14)
)


class _AdGenVoipSDPGrammarPtime_Type(TruthValue):
    """Custom type adGenVoipSDPGrammarPtime based on TruthValue"""
    defaultValue = 2


_AdGenVoipSDPGrammarPtime_Type.__name__ = "TruthValue"
_AdGenVoipSDPGrammarPtime_Object = MibScalar
adGenVoipSDPGrammarPtime = _AdGenVoipSDPGrammarPtime_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 14, 1),
    _AdGenVoipSDPGrammarPtime_Type()
)
adGenVoipSDPGrammarPtime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipSDPGrammarPtime.setStatus("current")


class _AdGenVoipSDPGrammarSuppressSilenceSupp_Type(TruthValue):
    """Custom type adGenVoipSDPGrammarSuppressSilenceSupp based on TruthValue"""
    defaultValue = 2


_AdGenVoipSDPGrammarSuppressSilenceSupp_Type.__name__ = "TruthValue"
_AdGenVoipSDPGrammarSuppressSilenceSupp_Object = MibScalar
adGenVoipSDPGrammarSuppressSilenceSupp = _AdGenVoipSDPGrammarSuppressSilenceSupp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 1, 14, 2),
    _AdGenVoipSDPGrammarSuppressSilenceSupp_Type()
)
adGenVoipSDPGrammarSuppressSilenceSupp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenVoipSDPGrammarSuppressSilenceSupp.setStatus("current")
_AdGenVoipStatus_ObjectIdentity = ObjectIdentity
adGenVoipStatus = _AdGenVoipStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2)
)
_AdGenVoipUserStatus_ObjectIdentity = ObjectIdentity
adGenVoipUserStatus = _AdGenVoipUserStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2, 1)
)
_AdGenVoipUserHotlineStatus_ObjectIdentity = ObjectIdentity
adGenVoipUserHotlineStatus = _AdGenVoipUserHotlineStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2, 1, 1)
)
_AdGenVoipUserHotlineStatusTable_Object = MibTable
adGenVoipUserHotlineStatusTable = _AdGenVoipUserHotlineStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2, 1, 1, 1)
)
if mibBuilder.loadTexts:
    adGenVoipUserHotlineStatusTable.setStatus("current")
_AdGenVoipUserHotlineStatusTableEntry_Object = MibTableRow
adGenVoipUserHotlineStatusTableEntry = _AdGenVoipUserHotlineStatusTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2, 1, 1, 1, 1)
)
adGenVoipUserHotlineStatusTableEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENVOIP-MIB", "adGenVoipUserHotlineStatusEntryIndex"),
)
if mibBuilder.loadTexts:
    adGenVoipUserHotlineStatusTableEntry.setStatus("current")
_AdGenVoipUserHotlineStatusEntryIndex_Type = AdGenVoipUserNumber
_AdGenVoipUserHotlineStatusEntryIndex_Object = MibTableColumn
adGenVoipUserHotlineStatusEntryIndex = _AdGenVoipUserHotlineStatusEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2, 1, 1, 1, 1, 1),
    _AdGenVoipUserHotlineStatusEntryIndex_Type()
)
adGenVoipUserHotlineStatusEntryIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipUserHotlineStatusEntryIndex.setStatus("current")


class _AdGenVoipUserHotlineStatusNumber_Type(DisplayString):
    """Custom type adGenVoipUserHotlineStatusNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 80),
    )


_AdGenVoipUserHotlineStatusNumber_Type.__name__ = "DisplayString"
_AdGenVoipUserHotlineStatusNumber_Object = MibTableColumn
adGenVoipUserHotlineStatusNumber = _AdGenVoipUserHotlineStatusNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2, 1, 1, 1, 1, 2),
    _AdGenVoipUserHotlineStatusNumber_Type()
)
adGenVoipUserHotlineStatusNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipUserHotlineStatusNumber.setStatus("current")
_AdGenVoipUserHotlineStatusHotlineState_Type = DisplayString
_AdGenVoipUserHotlineStatusHotlineState_Object = MibTableColumn
adGenVoipUserHotlineStatusHotlineState = _AdGenVoipUserHotlineStatusHotlineState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2, 1, 1, 1, 1, 3),
    _AdGenVoipUserHotlineStatusHotlineState_Type()
)
adGenVoipUserHotlineStatusHotlineState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipUserHotlineStatusHotlineState.setStatus("current")
_AdGenVoipScalarStatus_ObjectIdentity = ObjectIdentity
adGenVoipScalarStatus = _AdGenVoipScalarStatus_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2, 2)
)
_AdGenVoipScalarStatusMaxSupportedSipTrunks_Type = Integer32
_AdGenVoipScalarStatusMaxSupportedSipTrunks_Object = MibScalar
adGenVoipScalarStatusMaxSupportedSipTrunks = _AdGenVoipScalarStatusMaxSupportedSipTrunks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2, 2, 1),
    _AdGenVoipScalarStatusMaxSupportedSipTrunks_Type()
)
adGenVoipScalarStatusMaxSupportedSipTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipScalarStatusMaxSupportedSipTrunks.setStatus("current")
_AdGenVoipScalarStatusNumberOfSipTrunks_Type = Integer32
_AdGenVoipScalarStatusNumberOfSipTrunks_Object = MibScalar
adGenVoipScalarStatusNumberOfSipTrunks = _AdGenVoipScalarStatusNumberOfSipTrunks_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 20, 2, 2, 2),
    _AdGenVoipScalarStatusNumberOfSipTrunks_Type()
)
adGenVoipScalarStatusNumberOfSipTrunks.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenVoipScalarStatusNumberOfSipTrunks.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENVOIP-MIB",
    **{"AdGenVoipTrunkName": AdGenVoipTrunkName,
       "AdGenVoipCallServiceClassName": AdGenVoipCallServiceClassName,
       "AdGenVoipUserNumber": AdGenVoipUserNumber,
       "AdGenVoipDialingProfileName": AdGenVoipDialingProfileName,
       "AdGenVoipCodecProfileName": AdGenVoipCodecProfileName,
       "AdGenVoipMediaProfileName": AdGenVoipMediaProfileName,
       "AdGenVoipCodecProfileType": AdGenVoipCodecProfileType,
       "AdGenVoipCallFeatureProfileName": AdGenVoipCallFeatureProfileName,
       "AdGenVoipCallReverseLookupIfIndex": AdGenVoipCallReverseLookupIfIndex,
       "adGenVoipProvisioning": adGenVoipProvisioning,
       "adGenVoipTrunkProv": adGenVoipTrunkProv,
       "adGenVoipTrunkProvTable": adGenVoipTrunkProvTable,
       "adGenVoipTrunkProvEntry": adGenVoipTrunkProvEntry,
       "adGenVoipTrunkEntryIndex": adGenVoipTrunkEntryIndex,
       "adGenVoipTrunkTransfer": adGenVoipTrunkTransfer,
       "adGenVoipDialPlanProv": adGenVoipDialPlanProv,
       "adGenVoipDialPlanProvCurrentNumber": adGenVoipDialPlanProvCurrentNumber,
       "adGenVoipDialPlanProvLastCreateError": adGenVoipDialPlanProvLastCreateError,
       "adGenVoipDialPlanProvTable": adGenVoipDialPlanProvTable,
       "adGenVoipDialPlanProvEntry": adGenVoipDialPlanProvEntry,
       "adGenVoipDialPlanPatternEntryIndex": adGenVoipDialPlanPatternEntryIndex,
       "adGenVoipDialPlanRowStatus": adGenVoipDialPlanRowStatus,
       "adGenVoipDialPlanLastErrorString": adGenVoipDialPlanLastErrorString,
       "adGenVoipDialPlanType": adGenVoipDialPlanType,
       "adGenVoipDialPlanEmergencyNumber": adGenVoipDialPlanEmergencyNumber,
       "adGenVoipDialPlanExternalLineCode": adGenVoipDialPlanExternalLineCode,
       "adGenVoipSPREPatternProv": adGenVoipSPREPatternProv,
       "adGenVoipSPREPatternProvCurrentNumber": adGenVoipSPREPatternProvCurrentNumber,
       "adGenVoipSPREPatternProvLastCreateError": adGenVoipSPREPatternProvLastCreateError,
       "adGenVoipSPREPatternProvTable": adGenVoipSPREPatternProvTable,
       "adGenVoipSPREPatternProvEntry": adGenVoipSPREPatternProvEntry,
       "adGenVoipSPREPatternEntryIndex": adGenVoipSPREPatternEntryIndex,
       "adGenVoipSPREPatternRowStatus": adGenVoipSPREPatternRowStatus,
       "adGenVoipSPREPatternLastErrorString": adGenVoipSPREPatternLastErrorString,
       "adGenVoipSPREPatternTone": adGenVoipSPREPatternTone,
       "adGenVoipCallServiceClassProv": adGenVoipCallServiceClassProv,
       "adGenVoipCallServiceClassProvCurrentNumber": adGenVoipCallServiceClassProvCurrentNumber,
       "adGenVoipCallServiceClassProvLastCreateError": adGenVoipCallServiceClassProvLastCreateError,
       "adGenVoipCallServiceClassProvTable": adGenVoipCallServiceClassProvTable,
       "adGenVoipCallServiceClassProvEntry": adGenVoipCallServiceClassProvEntry,
       "adGenVoipCallServiceClassEntryIndex": adGenVoipCallServiceClassEntryIndex,
       "adGenVoipCallServiceClassRowStatus": adGenVoipCallServiceClassRowStatus,
       "adGenVoipCallServiceClassLastErrorString": adGenVoipCallServiceClassLastErrorString,
       "adGenVoipCallServiceClass900Number": adGenVoipCallServiceClass900Number,
       "adGenVoipCallServiceClassExtensions": adGenVoipCallServiceClassExtensions,
       "adGenVoipCallServiceClassInternational": adGenVoipCallServiceClassInternational,
       "adGenVoipCallServiceClassLocal": adGenVoipCallServiceClassLocal,
       "adGenVoipCallServiceClassNational": adGenVoipCallServiceClassNational,
       "adGenVoipCallServiceClassOperatorAssisted": adGenVoipCallServiceClassOperatorAssisted,
       "adGenVoipCallServiceClassSpecifyCarrier": adGenVoipCallServiceClassSpecifyCarrier,
       "adGenVoipCallServiceClassTollFree": adGenVoipCallServiceClassTollFree,
       "adGenVoipCallServiceClassUser1": adGenVoipCallServiceClassUser1,
       "adGenVoipCallServiceClassUser2": adGenVoipCallServiceClassUser2,
       "adGenVoipCallServiceClassUser3": adGenVoipCallServiceClassUser3,
       "adGenVoipCallServiceConference": adGenVoipCallServiceConference,
       "adGenVoipCallServiceDisableCallWaiting": adGenVoipCallServiceDisableCallWaiting,
       "adGenVoipUserProv": adGenVoipUserProv,
       "adGenVoipUserProvCurrentNumber": adGenVoipUserProvCurrentNumber,
       "adGenVoipUserProvLastCreateError": adGenVoipUserProvLastCreateError,
       "adGenVoipUserProvTable": adGenVoipUserProvTable,
       "adGenVoipUserProvEntry": adGenVoipUserProvEntry,
       "adGenVoipUserEntryIndex": adGenVoipUserEntryIndex,
       "adGenVoipUserRowStatus": adGenVoipUserRowStatus,
       "adGenVoipUserLastErrorString": adGenVoipUserLastErrorString,
       "adGenVoipUserFxsPort": adGenVoipUserFxsPort,
       "adGenVoipUserCallClass": adGenVoipUserCallClass,
       "adGenVoipUserCallWaiting": adGenVoipUserCallWaiting,
       "adGenVoipUserDialingProfile": adGenVoipUserDialingProfile,
       "adGenVoipUserHotlineEnabled": adGenVoipUserHotlineEnabled,
       "adGenVoipUserHotlineNumber": adGenVoipUserHotlineNumber,
       "adGenVoipUserSipTrunkManualSelect": adGenVoipUserSipTrunkManualSelect,
       "adGenVoipUserWarmlineEnabled": adGenVoipUserWarmlineEnabled,
       "adGenVoipUserWarmlineNumber": adGenVoipUserWarmlineNumber,
       "adGenVoipUserWarmlineDelay": adGenVoipUserWarmlineDelay,
       "adGenVoipUserProvBulkInstance": adGenVoipUserProvBulkInstance,
       "adGenVoipScalarProv": adGenVoipScalarProv,
       "adGenVoipScalarFlashhookMode": adGenVoipScalarFlashhookMode,
       "adGenVoipScalarConferenceMode": adGenVoipScalarConferenceMode,
       "adGenVoipScalarConfLocalOriginatorFlashhook": adGenVoipScalarConfLocalOriginatorFlashhook,
       "adGenVoipScalarConfLocalOriginatorOnhook": adGenVoipScalarConfLocalOriginatorOnhook,
       "adGenVoipScalarConfLocalPartyDisconnect": adGenVoipScalarConfLocalPartyDisconnect,
       "adGenVoipScalarRtpUdpOffset": adGenVoipScalarRtpUdpOffset,
       "adGenVoipScalarSPREMode": adGenVoipScalarSPREMode,
       "adGenVoipScalarInterdigitTimer": adGenVoipScalarInterdigitTimer,
       "adGenVoipScalarAlertingTimer": adGenVoipScalarAlertingTimer,
       "adGenVoipScalarTransferOnHangup": adGenVoipScalarTransferOnHangup,
       "adGenVoipScalarFlashhookThreholdMin": adGenVoipScalarFlashhookThreholdMin,
       "adGenVoipScalarFlashhookThreholdMax": adGenVoipScalarFlashhookThreholdMax,
       "adGenVoipScalarEmergencyNumberInhibitOnHook": adGenVoipScalarEmergencyNumberInhibitOnHook,
       "adGenVoipScalarEmergencyNumberRingingTimemout": adGenVoipScalarEmergencyNumberRingingTimemout,
       "adGenVoipScalarDefaultSipTrunk": adGenVoipScalarDefaultSipTrunk,
       "adGenVoipScalarConnectedTimer": adGenVoipScalarConnectedTimer,
       "adGenVoipSPREMapScalarProv": adGenVoipSPREMapScalarProv,
       "adGenVoipScalarSPREMapDisableCallWaiting": adGenVoipScalarSPREMapDisableCallWaiting,
       "adGenVoipScalarSPREMapDNDDisableEnable": adGenVoipScalarSPREMapDNDDisableEnable,
       "adGenVoipScalarSPREMapBlockCallerID": adGenVoipScalarSPREMapBlockCallerID,
       "adGenVoipDialingProfileProv": adGenVoipDialingProfileProv,
       "adGenVoipDialingProfileDialPlanProv": adGenVoipDialingProfileDialPlanProv,
       "adGenVoipDialingProfileDialPlanProvCurrentNumber": adGenVoipDialingProfileDialPlanProvCurrentNumber,
       "adGenVoipDialingProfileDialPlanProvLastCreateError": adGenVoipDialingProfileDialPlanProvLastCreateError,
       "adGenVoipDialingProfileDialPlanProvTable": adGenVoipDialingProfileDialPlanProvTable,
       "adGenVoipDialingProfileDialPlanProvEntry": adGenVoipDialingProfileDialPlanProvEntry,
       "adGenVoipDialingProfileDialPlanPatternEntryIndex": adGenVoipDialingProfileDialPlanPatternEntryIndex,
       "adGenVoipDialingProfileDialPlanRowStatus": adGenVoipDialingProfileDialPlanRowStatus,
       "adGenVoipDialingProfileDialPlanLastErrorString": adGenVoipDialingProfileDialPlanLastErrorString,
       "adGenVoipDialingProfileDialPlanType": adGenVoipDialingProfileDialPlanType,
       "adGenVoipDialingProfileDialPlanEmergencyNumber": adGenVoipDialingProfileDialPlanEmergencyNumber,
       "adGenVoipDialingProfileDialPlanExternalLineCode": adGenVoipDialingProfileDialPlanExternalLineCode,
       "adGenVoipDialingProfileDialPlanPattern": adGenVoipDialingProfileDialPlanPattern,
       "adGenVoipDialingProfileDialPlanDialingProfile": adGenVoipDialingProfileDialPlanDialingProfile,
       "adGenVoipDialingProfileSPREPatternProv": adGenVoipDialingProfileSPREPatternProv,
       "adGenVoipDialingProfileSPREPatternProvCurrentNumber": adGenVoipDialingProfileSPREPatternProvCurrentNumber,
       "adGenVoipDialingProfileSPREPatternProvLastCreateError": adGenVoipDialingProfileSPREPatternProvLastCreateError,
       "adGenVoipDialingProfileSPREPatternProvTable": adGenVoipDialingProfileSPREPatternProvTable,
       "adGenVoipDialingProfileSPREPatternProvEntry": adGenVoipDialingProfileSPREPatternProvEntry,
       "adGenVoipDialingProfileSPREPatternEntryIndex": adGenVoipDialingProfileSPREPatternEntryIndex,
       "adGenVoipDialingProfileSPREPatternRowStatus": adGenVoipDialingProfileSPREPatternRowStatus,
       "adGenVoipDialingProfileSPREPatternLastErrorString": adGenVoipDialingProfileSPREPatternLastErrorString,
       "adGenVoipDialingProfileSPREPatternTone": adGenVoipDialingProfileSPREPatternTone,
       "adGenVoipDialingProfileSPREPattern": adGenVoipDialingProfileSPREPattern,
       "adGenVoipDialingProfileSPREPatternDialingProfile": adGenVoipDialingProfileSPREPatternDialingProfile,
       "adGenVoipDialingProfileExternalLineCodeProv": adGenVoipDialingProfileExternalLineCodeProv,
       "adGenVoipDialingProfileExternalLineCodeProvCurrentNumber": adGenVoipDialingProfileExternalLineCodeProvCurrentNumber,
       "adGenVoipDialingProfileExternalLineCodeProvLastCreateError": adGenVoipDialingProfileExternalLineCodeProvLastCreateError,
       "adGenVoipDialingProfileExternalLineCodeProvTable": adGenVoipDialingProfileExternalLineCodeProvTable,
       "adGenVoipDialingProfileExternalLineCodeProvEntry": adGenVoipDialingProfileExternalLineCodeProvEntry,
       "adGenVoipDialingProfileExternalLineCodeEntryIndex": adGenVoipDialingProfileExternalLineCodeEntryIndex,
       "adGenVoipDialingProfileExternalLineCodeRowStatus": adGenVoipDialingProfileExternalLineCodeRowStatus,
       "adGenVoipDialingProfileExternalLineCodeLastErrorString": adGenVoipDialingProfileExternalLineCodeLastErrorString,
       "adGenVoipDialingProfileExternalLineCodeTone": adGenVoipDialingProfileExternalLineCodeTone,
       "adGenVoipDialingProfileExternalLineCodePattern": adGenVoipDialingProfileExternalLineCodePattern,
       "adGenVoipDialingProfileExternalLineCodeDialingProfile": adGenVoipDialingProfileExternalLineCodeDialingProfile,
       "adGenVoipDialingProfileProvExt": adGenVoipDialingProfileProvExt,
       "adGenVoipDialingProfileProvExtTable": adGenVoipDialingProfileProvExtTable,
       "adGenVoipDialingProfileProvExtEntry": adGenVoipDialingProfileProvExtEntry,
       "adGenVoipDialingProfileProvExtEntryIndex": adGenVoipDialingProfileProvExtEntryIndex,
       "adGenVoipDialingProfileProvExtNumVoiceUsers": adGenVoipDialingProfileProvExtNumVoiceUsers,
       "adGenVoipDialingProfileProvExtRemoveProfile": adGenVoipDialingProfileProvExtRemoveProfile,
       "adGenVoipDialingProfileCommonProv": adGenVoipDialingProfileCommonProv,
       "adGenVoipDialingProfileCommonProvCurrentNumber": adGenVoipDialingProfileCommonProvCurrentNumber,
       "adGenVoipDialingProfileCommonProvLastCreateError": adGenVoipDialingProfileCommonProvLastCreateError,
       "adGenVoipDialingProfileCommonProvTable": adGenVoipDialingProfileCommonProvTable,
       "adGenVoipDialingProfileCommonProvEntry": adGenVoipDialingProfileCommonProvEntry,
       "adGenVoipDialingProfileCommonProvEntryIndex": adGenVoipDialingProfileCommonProvEntryIndex,
       "adGenVoipDialingProfileCommonProvNumVoiceUsers": adGenVoipDialingProfileCommonProvNumVoiceUsers,
       "adGenVoipDialingProfileCommonProvRemoveProfile": adGenVoipDialingProfileCommonProvRemoveProfile,
       "adGenVoipDialingProfileCommonProvDescription": adGenVoipDialingProfileCommonProvDescription,
       "adGenVoipDialingProfileCommonProvRowStatus": adGenVoipDialingProfileCommonProvRowStatus,
       "adGenVoipDialingProfileCommonProvLastErrorString": adGenVoipDialingProfileCommonProvLastErrorString,
       "adGenVoipCodecProfileNameProv": adGenVoipCodecProfileNameProv,
       "adGenVoipCodecProfileNameProvCurrentNumber": adGenVoipCodecProfileNameProvCurrentNumber,
       "adGenVoipCodecProfileNameProvLastCreateError": adGenVoipCodecProfileNameProvLastCreateError,
       "adGenVoipCodecProfileNameProvTable": adGenVoipCodecProfileNameProvTable,
       "adGenVoipCodecProfileNameProvEntry": adGenVoipCodecProfileNameProvEntry,
       "adGenVoipCodecProfileNameProvIndex": adGenVoipCodecProfileNameProvIndex,
       "adGenVoipCodecProfileNameProvRowStatus": adGenVoipCodecProfileNameProvRowStatus,
       "adGenVoipCodecProfileNameProvLastErrorString": adGenVoipCodecProfileNameProvLastErrorString,
       "adGenVoipCodecProfilePreferenceLastCreateError": adGenVoipCodecProfilePreferenceLastCreateError,
       "adGenVoipCodecProfileProv": adGenVoipCodecProfileProv,
       "adGenVoipCodecProfileProvTable": adGenVoipCodecProfileProvTable,
       "adGenVoipCodecProfileProvEntry": adGenVoipCodecProfileProvEntry,
       "adGenVoipCodecProfileProvIndex": adGenVoipCodecProfileProvIndex,
       "adGenVoipCodecProfileProvRowStatus": adGenVoipCodecProfileProvRowStatus,
       "adGenVoipCodecProfileProvLastErrorString": adGenVoipCodecProfileProvLastErrorString,
       "adGenVoipCodecProfileProvPreference": adGenVoipCodecProfileProvPreference,
       "adGenVoipMediaProfileProv": adGenVoipMediaProfileProv,
       "adGenVoipMediaProfileProvCurrentNumber": adGenVoipMediaProfileProvCurrentNumber,
       "adGenVoipMediaProfileProvLastCreateError": adGenVoipMediaProfileProvLastCreateError,
       "adGenVoipMediaProfileProvTable": adGenVoipMediaProfileProvTable,
       "adGenVoipMediaProfileProvEntry": adGenVoipMediaProfileProvEntry,
       "adGenVoipMediaProfileProvEntryIndex": adGenVoipMediaProfileProvEntryIndex,
       "adGenVoipMediaProfileProvRowStatus": adGenVoipMediaProfileProvRowStatus,
       "adGenVoipMediaProfileProvLastErrorString": adGenVoipMediaProfileProvLastErrorString,
       "adGenVoipMediaProfileProvRtpFramePktization": adGenVoipMediaProfileProvRtpFramePktization,
       "adGenVoipMediaProfileProvRtpPktDelayNominal": adGenVoipMediaProfileProvRtpPktDelayNominal,
       "adGenVoipMediaProfileProvRtpPktDelayMaximum": adGenVoipMediaProfileProvRtpPktDelayMaximum,
       "adGenVoipMediaProfileProvRtpDtmfRelay": adGenVoipMediaProfileProvRtpDtmfRelay,
       "adGenVoipMediaProfileProvRtpQosDscp": adGenVoipMediaProfileProvRtpQosDscp,
       "adGenVoipMediaProfileProvRtpLocalPortMin": adGenVoipMediaProfileProvRtpLocalPortMin,
       "adGenVoipMediaProfileProvRtpLocalPortMax": adGenVoipMediaProfileProvRtpLocalPortMax,
       "adGenVoipMediaProfileProvFaxMode": adGenVoipMediaProfileProvFaxMode,
       "adGenVoipMediaProfileProvEchoCancellation": adGenVoipMediaProfileProvEchoCancellation,
       "adGenVoipMediaProfileProvFlashHookMin": adGenVoipMediaProfileProvFlashHookMin,
       "adGenVoipMediaProfileProvFlashHookMax": adGenVoipMediaProfileProvFlashHookMax,
       "adGenVoipMediaProfileProvVAD": adGenVoipMediaProfileProvVAD,
       "adGenVoipCallFeatureProfileProv": adGenVoipCallFeatureProfileProv,
       "adGenVoipCallFeatureProfileCurrentNumber": adGenVoipCallFeatureProfileCurrentNumber,
       "adGenVoipCallFeatureProfileLastCreateError": adGenVoipCallFeatureProfileLastCreateError,
       "adGenVoipCallFeatureProfileProvTable": adGenVoipCallFeatureProfileProvTable,
       "adGenVoipCallFeatureProfileProvEntry": adGenVoipCallFeatureProfileProvEntry,
       "adGenVoipCallFeatureProfileEntryIndex": adGenVoipCallFeatureProfileEntryIndex,
       "adGenVoipCallFeatureProfileRowStatus": adGenVoipCallFeatureProfileRowStatus,
       "adGenVoipCallFeatureProfileLastErrorString": adGenVoipCallFeatureProfileLastErrorString,
       "adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout": adGenVoipCallFeatureProfileEmergencyNumberRingingTimeout,
       "adGenVoipCallFeatureProfileEmergencyNumberOnhook": adGenVoipCallFeatureProfileEmergencyNumberOnhook,
       "adGenVoipCallFeatureProfileCallWaiting": adGenVoipCallFeatureProfileCallWaiting,
       "adGenVoipCallFeatureProfileCallerIdInbound": adGenVoipCallFeatureProfileCallerIdInbound,
       "adGenVoipCallFeatureProfileCallerIdOutbound": adGenVoipCallFeatureProfileCallerIdOutbound,
       "adGenVoipCallFeatureProfileTransferOnHangup": adGenVoipCallFeatureProfileTransferOnHangup,
       "adGenVoipCallFeatureProfileTimeoutAlerting": adGenVoipCallFeatureProfileTimeoutAlerting,
       "adGenVoipCallFeatureProfileTimeoutInterdigit": adGenVoipCallFeatureProfileTimeoutInterdigit,
       "adGenVoipCallFeatureProfileConference": adGenVoipCallFeatureProfileConference,
       "adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook": adGenVoipCallFeatureProfileConferenceLocalOriginatorFlashhoook,
       "adGenVoipCallFeatureProfileFeatureMode": adGenVoipCallFeatureProfileFeatureMode,
       "adGenVoipUserReverseLookup": adGenVoipUserReverseLookup,
       "adGenVoipUserReverseLookupTable": adGenVoipUserReverseLookupTable,
       "adGenVoipUserReverseLookupTableEntry": adGenVoipUserReverseLookupTableEntry,
       "adGenVoipUserReverseLookupTableEntryIndex": adGenVoipUserReverseLookupTableEntryIndex,
       "adGenVoipUserReverseLookupTableUserName": adGenVoipUserReverseLookupTableUserName,
       "adGenVoipSDPProv": adGenVoipSDPProv,
       "adGenVoipSDPGrammarPtime": adGenVoipSDPGrammarPtime,
       "adGenVoipSDPGrammarSuppressSilenceSupp": adGenVoipSDPGrammarSuppressSilenceSupp,
       "adGenVoipStatus": adGenVoipStatus,
       "adGenVoipUserStatus": adGenVoipUserStatus,
       "adGenVoipUserHotlineStatus": adGenVoipUserHotlineStatus,
       "adGenVoipUserHotlineStatusTable": adGenVoipUserHotlineStatusTable,
       "adGenVoipUserHotlineStatusTableEntry": adGenVoipUserHotlineStatusTableEntry,
       "adGenVoipUserHotlineStatusEntryIndex": adGenVoipUserHotlineStatusEntryIndex,
       "adGenVoipUserHotlineStatusNumber": adGenVoipUserHotlineStatusNumber,
       "adGenVoipUserHotlineStatusHotlineState": adGenVoipUserHotlineStatusHotlineState,
       "adGenVoipScalarStatus": adGenVoipScalarStatus,
       "adGenVoipScalarStatusMaxSupportedSipTrunks": adGenVoipScalarStatusMaxSupportedSipTrunks,
       "adGenVoipScalarStatusNumberOfSipTrunks": adGenVoipScalarStatusNumberOfSipTrunks,
       "adGenVoipIdentity": adGenVoipIdentity}
)
