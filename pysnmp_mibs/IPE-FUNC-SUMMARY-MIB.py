# SNMP MIB module (IPE-FUNC-SUMMARY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nec/IPE-FUNC-SUMMARY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:53:52 2025
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
 Opaque,
 TimeTicks,
 Unsigned32,
 enterprises,
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
    "Opaque",
    "TimeTicks",
    "Unsigned32",
    "enterprises",
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


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Nec_ObjectIdentity = ObjectIdentity
nec = _Nec_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119)
)
_Nec_mib_ObjectIdentity = ObjectIdentity
nec_mib = _Nec_mib_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2)
)
_NecProductDepend_ObjectIdentity = ObjectIdentity
necProductDepend = _NecProductDepend_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3)
)
_RadioEquipment_ObjectIdentity = ObjectIdentity
radioEquipment = _RadioEquipment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69)
)
_PasoNeoIpe_common_ObjectIdentity = ObjectIdentity
pasoNeoIpe_common = _PasoNeoIpe_common_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501)
)
_SummaryGroup_ObjectIdentity = ObjectIdentity
summaryGroup = _SummaryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1)
)
_MaintSummaryGroup_ObjectIdentity = ObjectIdentity
maintSummaryGroup = _MaintSummaryGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2)
)
_MaintFuncSummaryTable_Object = MibTable
maintFuncSummaryTable = _MaintFuncSummaryTable_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2)
)
if mibBuilder.loadTexts:
    maintFuncSummaryTable.setStatus("current")
_MaintFuncSummaryEntry_Object = MibTableRow
maintFuncSummaryEntry = _MaintFuncSummaryEntry_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2, 1)
)
maintFuncSummaryEntry.setIndexNames(
    (0, "IPE-FUNC-SUMMARY-MIB", "maintFuncSummaryCategory"),
)
if mibBuilder.loadTexts:
    maintFuncSummaryEntry.setStatus("current")


class _MaintFuncSummaryCategory_Type(Integer32):
    """Custom type maintFuncSummaryCategory based on Integer32"""
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
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("modemLb", 1),
          ("modemMaint", 2),
          ("modemSwgMaint", 3),
          ("e1Lb1", 4),
          ("e1Lb2", 5),
          ("stm1Lb1", 6),
          ("stm1Lb2", 7),
          ("sncpControl", 8),
          ("timingSourceControl", 9),
          ("laserShutdownControl", 10),
          ("fileUpdate", 11),
          ("etherring", 12),
          ("aps", 13),
          ("dot3ah", 14),
          ("modemL2Lb1", 16),
          ("modemL2Lb2", 17))
    )


_MaintFuncSummaryCategory_Type.__name__ = "Integer32"
_MaintFuncSummaryCategory_Object = MibTableColumn
maintFuncSummaryCategory = _MaintFuncSummaryCategory_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2, 1, 1),
    _MaintFuncSummaryCategory_Type()
)
maintFuncSummaryCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintFuncSummaryCategory.setStatus("current")
_MaintFuncSummaryNEAddress_Type = IpAddress
_MaintFuncSummaryNEAddress_Object = MibTableColumn
maintFuncSummaryNEAddress = _MaintFuncSummaryNEAddress_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2, 1, 2),
    _MaintFuncSummaryNEAddress_Type()
)
maintFuncSummaryNEAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    maintFuncSummaryNEAddress.setStatus("current")


class _MaintFuncSummary_Type(Integer32):
    """Custom type maintFuncSummary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("none", 1),
          ("executed", 2))
    )


_MaintFuncSummary_Type.__name__ = "Integer32"
_MaintFuncSummary_Object = MibTableColumn
maintFuncSummary = _MaintFuncSummary_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2, 1, 3),
    _MaintFuncSummary_Type()
)
maintFuncSummary.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintFuncSummary.setStatus("current")
_MaintFuncSummaryLastUpdated_Type = DateAndTime
_MaintFuncSummaryLastUpdated_Object = MibTableColumn
maintFuncSummaryLastUpdated = _MaintFuncSummaryLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 119, 2, 3, 69, 501, 1, 2, 2, 1, 4),
    _MaintFuncSummaryLastUpdated_Type()
)
maintFuncSummaryLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    maintFuncSummaryLastUpdated.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "IPE-FUNC-SUMMARY-MIB",
    **{"nec": nec,
       "nec-mib": nec_mib,
       "necProductDepend": necProductDepend,
       "radioEquipment": radioEquipment,
       "pasoNeoIpe-common": pasoNeoIpe_common,
       "summaryGroup": summaryGroup,
       "maintSummaryGroup": maintSummaryGroup,
       "maintFuncSummaryTable": maintFuncSummaryTable,
       "maintFuncSummaryEntry": maintFuncSummaryEntry,
       "maintFuncSummaryCategory": maintFuncSummaryCategory,
       "maintFuncSummaryNEAddress": maintFuncSummaryNEAddress,
       "maintFuncSummary": maintFuncSummary,
       "maintFuncSummaryLastUpdated": maintFuncSummaryLastUpdated}
)
