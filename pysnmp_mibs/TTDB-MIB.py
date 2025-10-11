# SNMP MIB module (TTDB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/westermo/TTDB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:54:25 2025
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

iec61375p2 = ModuleIdentity(
    (1, 0, 61375, 2)
)
if mibBuilder.loadTexts:
    iec61375p2.setRevisions(
        ("2019-11-27 00:00",
         "2014-05-22 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TtdbOrient(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("direct", 1),
          ("inverse", 2),
          ("undefined", 3))
    )



class TtdbValidity(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("valid", 2),
          ("shared", 3))
    )



class TtdbConfirmation(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unconfirmed", 1),
          ("confirmed", 2))
    )



# MIB Managed Objects in the order of their OIDs

_Std_ObjectIdentity = ObjectIdentity
std = _Std_ObjectIdentity(
    (1, 0)
)
_Stdx61375_ObjectIdentity = ObjectIdentity
stdx61375 = _Stdx61375_ObjectIdentity(
    (1, 0, 61375)
)
_Ttdb_ObjectIdentity = ObjectIdentity
ttdb = _Ttdb_ObjectIdentity(
    (1, 0, 61375, 2, 3)
)
_TtdbObjects_ObjectIdentity = ObjectIdentity
ttdbObjects = _TtdbObjects_ObjectIdentity(
    (1, 0, 61375, 2, 3, 1)
)
_TtdbGenInfo_ObjectIdentity = ObjectIdentity
ttdbGenInfo = _TtdbGenInfo_ObjectIdentity(
    (1, 0, 61375, 2, 3, 1, 1)
)


class _TtdbEtbId_Type(Unsigned32):
    """Custom type ttdbEtbId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4),
    )


_TtdbEtbId_Type.__name__ = "Unsigned32"
_TtdbEtbId_Object = MibScalar
ttdbEtbId = _TtdbEtbId_Object(
    (1, 0, 61375, 2, 3, 1, 1, 1),
    _TtdbEtbId_Type()
)
ttdbEtbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbEtbId.setStatus("current")
_TtdbValidityState_Type = TtdbValidity
_TtdbValidityState_Object = MibScalar
ttdbValidityState = _TtdbValidityState_Object(
    (1, 0, 61375, 2, 3, 1, 1, 2),
    _TtdbValidityState_Type()
)
ttdbValidityState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbValidityState.setStatus("current")
_TtdbConfirmationState_Type = TtdbConfirmation
_TtdbConfirmationState_Object = MibScalar
ttdbConfirmationState = _TtdbConfirmationState_Object(
    (1, 0, 61375, 2, 3, 1, 1, 3),
    _TtdbConfirmationState_Type()
)
ttdbConfirmationState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbConfirmationState.setStatus("current")


class _TtdbTrainId_Type(OctetString):
    """Custom type ttdbTrainId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_TtdbTrainId_Type.__name__ = "OctetString"
_TtdbTrainId_Object = MibScalar
ttdbTrainId = _TtdbTrainId_Object(
    (1, 0, 61375, 2, 3, 1, 1, 4),
    _TtdbTrainId_Type()
)
ttdbTrainId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbTrainId.setStatus("current")
_TtdbOpTrnTopoCnt_Type = Unsigned32
_TtdbOpTrnTopoCnt_Object = MibScalar
ttdbOpTrnTopoCnt = _TtdbOpTrnTopoCnt_Object(
    (1, 0, 61375, 2, 3, 1, 1, 5),
    _TtdbOpTrnTopoCnt_Type()
)
ttdbOpTrnTopoCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbOpTrnTopoCnt.setStatus("current")
_TtdbOpVehList_ObjectIdentity = ObjectIdentity
ttdbOpVehList = _TtdbOpVehList_ObjectIdentity(
    (1, 0, 61375, 2, 3, 1, 2)
)


class _TtdbOpVehCnt_Type(Unsigned32):
    """Custom type ttdbOpVehCnt based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TtdbOpVehCnt_Type.__name__ = "Unsigned32"
_TtdbOpVehCnt_Object = MibScalar
ttdbOpVehCnt = _TtdbOpVehCnt_Object(
    (1, 0, 61375, 2, 3, 1, 2, 1),
    _TtdbOpVehCnt_Type()
)
ttdbOpVehCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbOpVehCnt.setStatus("current")
_TtdbOpVehTable_Object = MibTable
ttdbOpVehTable = _TtdbOpVehTable_Object(
    (1, 0, 61375, 2, 3, 1, 2, 2)
)
if mibBuilder.loadTexts:
    ttdbOpVehTable.setStatus("current")
_TtdbOpVehEntry_Object = MibTableRow
ttdbOpVehEntry = _TtdbOpVehEntry_Object(
    (1, 0, 61375, 2, 3, 1, 2, 2, 1)
)
ttdbOpVehEntry.setIndexNames(
    (0, "TTDB-MIB", "ttdbOpVehIdx"),
)
if mibBuilder.loadTexts:
    ttdbOpVehEntry.setStatus("current")


class _TtdbOpVehIdx_Type(Unsigned32):
    """Custom type ttdbOpVehIdx based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TtdbOpVehIdx_Type.__name__ = "Unsigned32"
_TtdbOpVehIdx_Object = MibTableColumn
ttdbOpVehIdx = _TtdbOpVehIdx_Object(
    (1, 0, 61375, 2, 3, 1, 2, 2, 1, 1),
    _TtdbOpVehIdx_Type()
)
ttdbOpVehIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    ttdbOpVehIdx.setStatus("current")


class _TtdbOpVehId_Type(OctetString):
    """Custom type ttdbOpVehId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_TtdbOpVehId_Type.__name__ = "OctetString"
_TtdbOpVehId_Object = MibTableColumn
ttdbOpVehId = _TtdbOpVehId_Object(
    (1, 0, 61375, 2, 3, 1, 2, 2, 1, 2),
    _TtdbOpVehId_Type()
)
ttdbOpVehId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbOpVehId.setStatus("current")


class _TtdbOpVehNo_Type(Unsigned32):
    """Custom type ttdbOpVehNo based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 63),
    )


_TtdbOpVehNo_Type.__name__ = "Unsigned32"
_TtdbOpVehNo_Object = MibTableColumn
ttdbOpVehNo = _TtdbOpVehNo_Object(
    (1, 0, 61375, 2, 3, 1, 2, 2, 1, 3),
    _TtdbOpVehNo_Type()
)
ttdbOpVehNo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbOpVehNo.setStatus("current")


class _TtdbOpVehIsLead_Type(Integer32):
    """Custom type ttdbOpVehIsLead based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notLeading", 1),
          ("leading", 2))
    )


_TtdbOpVehIsLead_Type.__name__ = "Integer32"
_TtdbOpVehIsLead_Object = MibTableColumn
ttdbOpVehIsLead = _TtdbOpVehIsLead_Object(
    (1, 0, 61375, 2, 3, 1, 2, 2, 1, 4),
    _TtdbOpVehIsLead_Type()
)
ttdbOpVehIsLead.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbOpVehIsLead.setStatus("current")


class _TtdbOpVehLeadDir_Type(Integer32):
    """Custom type ttdbOpVehLeadDir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dir1", 1),
          ("dir2", 2))
    )


_TtdbOpVehLeadDir_Type.__name__ = "Integer32"
_TtdbOpVehLeadDir_Object = MibTableColumn
ttdbOpVehLeadDir = _TtdbOpVehLeadDir_Object(
    (1, 0, 61375, 2, 3, 1, 2, 2, 1, 5),
    _TtdbOpVehLeadDir_Type()
)
ttdbOpVehLeadDir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbOpVehLeadDir.setStatus("current")
_TtdbOpVehOrient_Type = TtdbOrient
_TtdbOpVehOrient_Object = MibTableColumn
ttdbOpVehOrient = _TtdbOpVehOrient_Object(
    (1, 0, 61375, 2, 3, 1, 2, 2, 1, 6),
    _TtdbOpVehOrient_Type()
)
ttdbOpVehOrient.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ttdbOpVehOrient.setStatus("current")
_TtdbConformance_ObjectIdentity = ObjectIdentity
ttdbConformance = _TtdbConformance_ObjectIdentity(
    (1, 0, 61375, 2, 3, 2)
)

# Managed Objects groups

ttdbBasicGroup = ObjectGroup(
    (1, 0, 61375, 2, 3, 2, 2)
)
ttdbBasicGroup.setObjects(
      *(("TTDB-MIB", "ttdbEtbId"),
        ("TTDB-MIB", "ttdbValidityState"),
        ("TTDB-MIB", "ttdbConfirmationState"),
        ("TTDB-MIB", "ttdbTrainId"),
        ("TTDB-MIB", "ttdbOpVehCnt"),
        ("TTDB-MIB", "ttdbOpTrnTopoCnt"))
)
if mibBuilder.loadTexts:
    ttdbBasicGroup.setStatus("current")

ttdbOpVehListGroup = ObjectGroup(
    (1, 0, 61375, 2, 3, 2, 3)
)
ttdbOpVehListGroup.setObjects(
      *(("TTDB-MIB", "ttdbOpVehId"),
        ("TTDB-MIB", "ttdbOpVehNo"),
        ("TTDB-MIB", "ttdbOpVehIsLead"),
        ("TTDB-MIB", "ttdbOpVehLeadDir"),
        ("TTDB-MIB", "ttdbOpVehOrient"))
)
if mibBuilder.loadTexts:
    ttdbOpVehListGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ttdbBasicCompliance = ModuleCompliance(
    (1, 0, 61375, 2, 3, 2, 4)
)
ttdbBasicCompliance.setObjects(
      *(("TTDB-MIB", "ttdbBasicGroup"),
        ("TTDB-MIB", "ttdbOpVehListGroup"))
)
if mibBuilder.loadTexts:
    ttdbBasicCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TTDB-MIB",
    **{"TtdbOrient": TtdbOrient,
       "TtdbValidity": TtdbValidity,
       "TtdbConfirmation": TtdbConfirmation,
       "std": std,
       "stdx61375": stdx61375,
       "iec61375p2": iec61375p2,
       "ttdb": ttdb,
       "ttdbObjects": ttdbObjects,
       "ttdbGenInfo": ttdbGenInfo,
       "ttdbEtbId": ttdbEtbId,
       "ttdbValidityState": ttdbValidityState,
       "ttdbConfirmationState": ttdbConfirmationState,
       "ttdbTrainId": ttdbTrainId,
       "ttdbOpTrnTopoCnt": ttdbOpTrnTopoCnt,
       "ttdbOpVehList": ttdbOpVehList,
       "ttdbOpVehCnt": ttdbOpVehCnt,
       "ttdbOpVehTable": ttdbOpVehTable,
       "ttdbOpVehEntry": ttdbOpVehEntry,
       "ttdbOpVehIdx": ttdbOpVehIdx,
       "ttdbOpVehId": ttdbOpVehId,
       "ttdbOpVehNo": ttdbOpVehNo,
       "ttdbOpVehIsLead": ttdbOpVehIsLead,
       "ttdbOpVehLeadDir": ttdbOpVehLeadDir,
       "ttdbOpVehOrient": ttdbOpVehOrient,
       "ttdbConformance": ttdbConformance,
       "ttdbBasicGroup": ttdbBasicGroup,
       "ttdbOpVehListGroup": ttdbOpVehListGroup,
       "ttdbBasicCompliance": ttdbBasicCompliance}
)
