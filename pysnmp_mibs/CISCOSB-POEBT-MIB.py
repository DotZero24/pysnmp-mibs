# SNMP MIB module (CISCOSB-POEBT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/ciscosb/CISCOSB-POEBT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:39:43 2025
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

(switch001,) = mibBuilder.importSymbols(
    "CISCOSB-MIB",
    "switch001")

(rlPethPsePortEntry,) = mibBuilder.importSymbols(
    "CISCOSB-POE-MIB",
    "rlPethPsePortEntry")

(InterfaceIndex,
 InterfaceIndexOrZero) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "InterfaceIndexOrZero")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

rlPoeBt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151)
)
if mibBuilder.loadTexts:
    rlPoeBt.setRevisions(
        ("2020-04-10 00:00",
         "2020-04-10 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class RlPoeBtClass(TextualConvention, Integer32):
    status = "current"
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
        *(("noClass", 1),
          ("class1", 2),
          ("class2", 3),
          ("class3", 4),
          ("class4", 5),
          ("class5", 6),
          ("class6", 7),
          ("class7", 8),
          ("class8", 9))
    )



# MIB Managed Objects in the order of their OIDs

_RlPethPseBtPortTable_Object = MibTable
rlPethPseBtPortTable = _RlPethPseBtPortTable_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1)
)
if mibBuilder.loadTexts:
    rlPethPseBtPortTable.setStatus("current")
_RlPethPseBtPortEntry_Object = MibTableRow
rlPethPseBtPortEntry = _RlPethPseBtPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1)
)
if mibBuilder.loadTexts:
    rlPethPseBtPortEntry.setStatus("current")


class _RlPethPseBtPortAltAStatus_Type(Integer32):
    """Custom type rlPethPseBtPortAltAStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPseBtPortAltAStatus_Type.__name__ = "Integer32"
_RlPethPseBtPortAltAStatus_Object = MibTableColumn
rlPethPseBtPortAltAStatus = _RlPethPseBtPortAltAStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 1),
    _RlPethPseBtPortAltAStatus_Type()
)
rlPethPseBtPortAltAStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltAStatus.setStatus("current")


class _RlPethPseBtPortAltADetectionStatus_Type(Integer32):
    """Custom type rlPethPseBtPortAltADetectionStatus based on Integer32"""
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
        *(("disabled", 1),
          ("searching", 2),
          ("deliveringPower", 3),
          ("fault", 4))
    )


_RlPethPseBtPortAltADetectionStatus_Type.__name__ = "Integer32"
_RlPethPseBtPortAltADetectionStatus_Object = MibTableColumn
rlPethPseBtPortAltADetectionStatus = _RlPethPseBtPortAltADetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 2),
    _RlPethPseBtPortAltADetectionStatus_Type()
)
rlPethPseBtPortAltADetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltADetectionStatus.setStatus("current")
_RlPethPseBtPortAltAMeasuredClass_Type = RlPoeBtClass
_RlPethPseBtPortAltAMeasuredClass_Object = MibTableColumn
rlPethPseBtPortAltAMeasuredClass = _RlPethPseBtPortAltAMeasuredClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 3),
    _RlPethPseBtPortAltAMeasuredClass_Type()
)
rlPethPseBtPortAltAMeasuredClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltAMeasuredClass.setStatus("current")
_RlPethPseBtPortAltAAssignedClass_Type = RlPoeBtClass
_RlPethPseBtPortAltAAssignedClass_Object = MibTableColumn
rlPethPseBtPortAltAAssignedClass = _RlPethPseBtPortAltAAssignedClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 4),
    _RlPethPseBtPortAltAAssignedClass_Type()
)
rlPethPseBtPortAltAAssignedClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltAAssignedClass.setStatus("current")


class _RlPethPseBtPortAltAAllocPower_Type(Integer32):
    """Custom type rlPethPseBtPortAltAAllocPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPseBtPortAltAAllocPower_Type.__name__ = "Integer32"
_RlPethPseBtPortAltAAllocPower_Object = MibTableColumn
rlPethPseBtPortAltAAllocPower = _RlPethPseBtPortAltAAllocPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 5),
    _RlPethPseBtPortAltAAllocPower_Type()
)
rlPethPseBtPortAltAAllocPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltAAllocPower.setStatus("current")
_RlPethPseBtPortAltAInvalidSigCounter_Type = Counter32
_RlPethPseBtPortAltAInvalidSigCounter_Object = MibTableColumn
rlPethPseBtPortAltAInvalidSigCounter = _RlPethPseBtPortAltAInvalidSigCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 6),
    _RlPethPseBtPortAltAInvalidSigCounter_Type()
)
rlPethPseBtPortAltAInvalidSigCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltAInvalidSigCounter.setStatus("current")
_RlPethPseBtPortAltAPowerDeniedCounter_Type = Counter32
_RlPethPseBtPortAltAPowerDeniedCounter_Object = MibTableColumn
rlPethPseBtPortAltAPowerDeniedCounter = _RlPethPseBtPortAltAPowerDeniedCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 7),
    _RlPethPseBtPortAltAPowerDeniedCounter_Type()
)
rlPethPseBtPortAltAPowerDeniedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltAPowerDeniedCounter.setStatus("current")
_RlPethPseBtPortAltAOverloadCounter_Type = Counter32
_RlPethPseBtPortAltAOverloadCounter_Object = MibTableColumn
rlPethPseBtPortAltAOverloadCounter = _RlPethPseBtPortAltAOverloadCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 8),
    _RlPethPseBtPortAltAOverloadCounter_Type()
)
rlPethPseBtPortAltAOverloadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltAOverloadCounter.setStatus("current")
_RlPethPseBtPortAltAMPSAbsentCounter_Type = Counter32
_RlPethPseBtPortAltAMPSAbsentCounter_Object = MibTableColumn
rlPethPseBtPortAltAMPSAbsentCounter = _RlPethPseBtPortAltAMPSAbsentCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 9),
    _RlPethPseBtPortAltAMPSAbsentCounter_Type()
)
rlPethPseBtPortAltAMPSAbsentCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltAMPSAbsentCounter.setStatus("current")


class _RlPethPseBtPortAltBStatus_Type(Integer32):
    """Custom type rlPethPseBtPortAltBStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPseBtPortAltBStatus_Type.__name__ = "Integer32"
_RlPethPseBtPortAltBStatus_Object = MibTableColumn
rlPethPseBtPortAltBStatus = _RlPethPseBtPortAltBStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 10),
    _RlPethPseBtPortAltBStatus_Type()
)
rlPethPseBtPortAltBStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltBStatus.setStatus("current")


class _RlPethPseBtPortAltBDetectionStatus_Type(Integer32):
    """Custom type rlPethPseBtPortAltBDetectionStatus based on Integer32"""
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
        *(("disabled", 1),
          ("searching", 2),
          ("deliveringPower", 3),
          ("fault", 4))
    )


_RlPethPseBtPortAltBDetectionStatus_Type.__name__ = "Integer32"
_RlPethPseBtPortAltBDetectionStatus_Object = MibTableColumn
rlPethPseBtPortAltBDetectionStatus = _RlPethPseBtPortAltBDetectionStatus_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 11),
    _RlPethPseBtPortAltBDetectionStatus_Type()
)
rlPethPseBtPortAltBDetectionStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltBDetectionStatus.setStatus("current")
_RlPethPseBtPortAltBMeasuredClass_Type = RlPoeBtClass
_RlPethPseBtPortAltBMeasuredClass_Object = MibTableColumn
rlPethPseBtPortAltBMeasuredClass = _RlPethPseBtPortAltBMeasuredClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 12),
    _RlPethPseBtPortAltBMeasuredClass_Type()
)
rlPethPseBtPortAltBMeasuredClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltBMeasuredClass.setStatus("current")
_RlPethPseBtPortAltBAssignedClass_Type = RlPoeBtClass
_RlPethPseBtPortAltBAssignedClass_Object = MibTableColumn
rlPethPseBtPortAltBAssignedClass = _RlPethPseBtPortAltBAssignedClass_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 13),
    _RlPethPseBtPortAltBAssignedClass_Type()
)
rlPethPseBtPortAltBAssignedClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltBAssignedClass.setStatus("current")


class _RlPethPseBtPortAltBAllocPower_Type(Integer32):
    """Custom type rlPethPseBtPortAltBAllocPower based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_RlPethPseBtPortAltBAllocPower_Type.__name__ = "Integer32"
_RlPethPseBtPortAltBAllocPower_Object = MibTableColumn
rlPethPseBtPortAltBAllocPower = _RlPethPseBtPortAltBAllocPower_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 14),
    _RlPethPseBtPortAltBAllocPower_Type()
)
rlPethPseBtPortAltBAllocPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltBAllocPower.setStatus("current")
_RlPethPseBtPortAltBInvalidSigCounter_Type = Counter32
_RlPethPseBtPortAltBInvalidSigCounter_Object = MibTableColumn
rlPethPseBtPortAltBInvalidSigCounter = _RlPethPseBtPortAltBInvalidSigCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 15),
    _RlPethPseBtPortAltBInvalidSigCounter_Type()
)
rlPethPseBtPortAltBInvalidSigCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltBInvalidSigCounter.setStatus("current")
_RlPethPseBtPortAltBPowerDeniedCounter_Type = Counter32
_RlPethPseBtPortAltBPowerDeniedCounter_Object = MibTableColumn
rlPethPseBtPortAltBPowerDeniedCounter = _RlPethPseBtPortAltBPowerDeniedCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 16),
    _RlPethPseBtPortAltBPowerDeniedCounter_Type()
)
rlPethPseBtPortAltBPowerDeniedCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltBPowerDeniedCounter.setStatus("current")
_RlPethPseBtPortAltBOverloadCounter_Type = Counter32
_RlPethPseBtPortAltBOverloadCounter_Object = MibTableColumn
rlPethPseBtPortAltBOverloadCounter = _RlPethPseBtPortAltBOverloadCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 17),
    _RlPethPseBtPortAltBOverloadCounter_Type()
)
rlPethPseBtPortAltBOverloadCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltBOverloadCounter.setStatus("current")
_RlPethPseBtPortAltBMPSAbsentCounter_Type = Counter32
_RlPethPseBtPortAltBMPSAbsentCounter_Object = MibTableColumn
rlPethPseBtPortAltBMPSAbsentCounter = _RlPethPseBtPortAltBMPSAbsentCounter_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 18),
    _RlPethPseBtPortAltBMPSAbsentCounter_Type()
)
rlPethPseBtPortAltBMPSAbsentCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltBMPSAbsentCounter.setStatus("current")


class _RlPethPseBtPortPowerClassMethod_Type(Integer32):
    """Custom type rlPethPseBtPortPowerClassMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("powerClassMethodRegular", 1),
          ("powerClassMethodAutoClass", 2))
    )


_RlPethPseBtPortPowerClassMethod_Type.__name__ = "Integer32"
_RlPethPseBtPortPowerClassMethod_Object = MibTableColumn
rlPethPseBtPortPowerClassMethod = _RlPethPseBtPortPowerClassMethod_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 19),
    _RlPethPseBtPortPowerClassMethod_Type()
)
rlPethPseBtPortPowerClassMethod.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortPowerClassMethod.setStatus("current")


class _RlPethPseBtPortAltAStatusDescription_Type(DisplayString):
    """Custom type rlPethPseBtPortAltAStatusDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_RlPethPseBtPortAltAStatusDescription_Type.__name__ = "DisplayString"
_RlPethPseBtPortAltAStatusDescription_Object = MibTableColumn
rlPethPseBtPortAltAStatusDescription = _RlPethPseBtPortAltAStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 20),
    _RlPethPseBtPortAltAStatusDescription_Type()
)
rlPethPseBtPortAltAStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltAStatusDescription.setStatus("current")


class _RlPethPseBtPortAltBStatusDescription_Type(DisplayString):
    """Custom type rlPethPseBtPortAltBStatusDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 120),
    )


_RlPethPseBtPortAltBStatusDescription_Type.__name__ = "DisplayString"
_RlPethPseBtPortAltBStatusDescription_Object = MibTableColumn
rlPethPseBtPortAltBStatusDescription = _RlPethPseBtPortAltBStatusDescription_Object(
    (1, 3, 6, 1, 4, 1, 9, 6, 1, 101, 151, 1, 1, 21),
    _RlPethPseBtPortAltBStatusDescription_Type()
)
rlPethPseBtPortAltBStatusDescription.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    rlPethPseBtPortAltBStatusDescription.setStatus("current")
rlPethPsePortEntry.registerAugmentions(
    ("CISCOSB-POEBT-MIB",
     "rlPethPseBtPortEntry")
)
rlPethPseBtPortEntry.setIndexNames(*rlPethPsePortEntry.getIndexNames())

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "CISCOSB-POEBT-MIB",
    **{"RlPoeBtClass": RlPoeBtClass,
       "rlPoeBt": rlPoeBt,
       "rlPethPseBtPortTable": rlPethPseBtPortTable,
       "rlPethPseBtPortEntry": rlPethPseBtPortEntry,
       "rlPethPseBtPortAltAStatus": rlPethPseBtPortAltAStatus,
       "rlPethPseBtPortAltADetectionStatus": rlPethPseBtPortAltADetectionStatus,
       "rlPethPseBtPortAltAMeasuredClass": rlPethPseBtPortAltAMeasuredClass,
       "rlPethPseBtPortAltAAssignedClass": rlPethPseBtPortAltAAssignedClass,
       "rlPethPseBtPortAltAAllocPower": rlPethPseBtPortAltAAllocPower,
       "rlPethPseBtPortAltAInvalidSigCounter": rlPethPseBtPortAltAInvalidSigCounter,
       "rlPethPseBtPortAltAPowerDeniedCounter": rlPethPseBtPortAltAPowerDeniedCounter,
       "rlPethPseBtPortAltAOverloadCounter": rlPethPseBtPortAltAOverloadCounter,
       "rlPethPseBtPortAltAMPSAbsentCounter": rlPethPseBtPortAltAMPSAbsentCounter,
       "rlPethPseBtPortAltBStatus": rlPethPseBtPortAltBStatus,
       "rlPethPseBtPortAltBDetectionStatus": rlPethPseBtPortAltBDetectionStatus,
       "rlPethPseBtPortAltBMeasuredClass": rlPethPseBtPortAltBMeasuredClass,
       "rlPethPseBtPortAltBAssignedClass": rlPethPseBtPortAltBAssignedClass,
       "rlPethPseBtPortAltBAllocPower": rlPethPseBtPortAltBAllocPower,
       "rlPethPseBtPortAltBInvalidSigCounter": rlPethPseBtPortAltBInvalidSigCounter,
       "rlPethPseBtPortAltBPowerDeniedCounter": rlPethPseBtPortAltBPowerDeniedCounter,
       "rlPethPseBtPortAltBOverloadCounter": rlPethPseBtPortAltBOverloadCounter,
       "rlPethPseBtPortAltBMPSAbsentCounter": rlPethPseBtPortAltBMPSAbsentCounter,
       "rlPethPseBtPortPowerClassMethod": rlPethPseBtPortPowerClassMethod,
       "rlPethPseBtPortAltAStatusDescription": rlPethPseBtPortAltAStatusDescription,
       "rlPethPseBtPortAltBStatusDescription": rlPethPseBtPortAltBStatusDescription}
)
