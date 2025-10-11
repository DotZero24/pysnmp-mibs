# SNMP MIB module (ADTRAN-GENSHAPER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENSHAPER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:02 2025
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

(adGenShaper,
 adGenShaperID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenShaper",
    "adGenShaperID")

(InterfaceIndex,
 InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

adGenShaperMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 19, 1)
)
if mibBuilder.loadTexts:
    adGenShaperMIB.setRevisions(
        ("2009-09-03 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenShaperProvisioning_ObjectIdentity = ObjectIdentity
adGenShaperProvisioning = _AdGenShaperProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1)
)
_AdGenShaperProvTable_Object = MibTable
adGenShaperProvTable = _AdGenShaperProvTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1)
)
if mibBuilder.loadTexts:
    adGenShaperProvTable.setStatus("current")
_AdGenShaperProvEntry_Object = MibTableRow
adGenShaperProvEntry = _AdGenShaperProvEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1, 1)
)
adGenShaperProvEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENSHAPER-MIB", "adGenShaperProvName"),
)
if mibBuilder.loadTexts:
    adGenShaperProvEntry.setStatus("current")


class _AdGenShaperProvName_Type(DisplayString):
    """Custom type adGenShaperProvName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenShaperProvName_Type.__name__ = "DisplayString"
_AdGenShaperProvName_Object = MibTableColumn
adGenShaperProvName = _AdGenShaperProvName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1, 1, 1),
    _AdGenShaperProvName_Type()
)
adGenShaperProvName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenShaperProvName.setStatus("current")
_AdGenShaperProvRowStatus_Type = RowStatus
_AdGenShaperProvRowStatus_Object = MibTableColumn
adGenShaperProvRowStatus = _AdGenShaperProvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1, 1, 2),
    _AdGenShaperProvRowStatus_Type()
)
adGenShaperProvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenShaperProvRowStatus.setStatus("current")


class _AdGenShaperProvOperStatus_Type(Integer32):
    """Custom type adGenShaperProvOperStatus based on Integer32"""
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


_AdGenShaperProvOperStatus_Type.__name__ = "Integer32"
_AdGenShaperProvOperStatus_Object = MibTableColumn
adGenShaperProvOperStatus = _AdGenShaperProvOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1, 1, 3),
    _AdGenShaperProvOperStatus_Type()
)
adGenShaperProvOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenShaperProvOperStatus.setStatus("current")
_AdGenShaperProvOperStatusDetail_Type = DisplayString
_AdGenShaperProvOperStatusDetail_Object = MibTableColumn
adGenShaperProvOperStatusDetail = _AdGenShaperProvOperStatusDetail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1, 1, 4),
    _AdGenShaperProvOperStatusDetail_Type()
)
adGenShaperProvOperStatusDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenShaperProvOperStatusDetail.setStatus("current")
_AdGenShaperProvLastProvError_Type = DisplayString
_AdGenShaperProvLastProvError_Object = MibTableColumn
adGenShaperProvLastProvError = _AdGenShaperProvLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1, 1, 5),
    _AdGenShaperProvLastProvError_Type()
)
adGenShaperProvLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenShaperProvLastProvError.setStatus("current")


class _AdGenShaperProvApplication_Type(Integer32):
    """Custom type adGenShaperProvApplication based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("perInterface", 2))
    )


_AdGenShaperProvApplication_Type.__name__ = "Integer32"
_AdGenShaperProvApplication_Object = MibTableColumn
adGenShaperProvApplication = _AdGenShaperProvApplication_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1, 1, 6),
    _AdGenShaperProvApplication_Type()
)
adGenShaperProvApplication.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenShaperProvApplication.setStatus("current")
_AdGenShaperProvRate_Type = Unsigned32
_AdGenShaperProvRate_Object = MibTableColumn
adGenShaperProvRate = _AdGenShaperProvRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1, 1, 7),
    _AdGenShaperProvRate_Type()
)
adGenShaperProvRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenShaperProvRate.setStatus("current")
_AdGenShaperProvInterface_Type = InterfaceIndexOrZero
_AdGenShaperProvInterface_Object = MibTableColumn
adGenShaperProvInterface = _AdGenShaperProvInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1, 1, 8),
    _AdGenShaperProvInterface_Type()
)
adGenShaperProvInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenShaperProvInterface.setStatus("current")
_AdGenShaperBurstSize_Type = Unsigned32
_AdGenShaperBurstSize_Object = MibTableColumn
adGenShaperBurstSize = _AdGenShaperBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 1, 1, 9),
    _AdGenShaperBurstSize_Type()
)
adGenShaperBurstSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenShaperBurstSize.setStatus("current")
_AdGenShaperSlotTable_Object = MibTable
adGenShaperSlotTable = _AdGenShaperSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 2)
)
if mibBuilder.loadTexts:
    adGenShaperSlotTable.setStatus("current")
_AdGenShaperSlotEntry_Object = MibTableRow
adGenShaperSlotEntry = _AdGenShaperSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 2, 1)
)
adGenShaperSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenShaperSlotEntry.setStatus("current")
_AdGenShaperSlotLastCreateError_Type = DisplayString
_AdGenShaperSlotLastCreateError_Object = MibTableColumn
adGenShaperSlotLastCreateError = _AdGenShaperSlotLastCreateError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 2, 1, 1),
    _AdGenShaperSlotLastCreateError_Type()
)
adGenShaperSlotLastCreateError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenShaperSlotLastCreateError.setStatus("current")
_AdGenShaperLookupPerInterfaceTable_Object = MibTable
adGenShaperLookupPerInterfaceTable = _AdGenShaperLookupPerInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 3)
)
if mibBuilder.loadTexts:
    adGenShaperLookupPerInterfaceTable.setStatus("current")
_AdGenShaperLookupPerInterfaceEntry_Object = MibTableRow
adGenShaperLookupPerInterfaceEntry = _AdGenShaperLookupPerInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 3, 1)
)
adGenShaperLookupPerInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenShaperLookupPerInterfaceEntry.setStatus("current")
_AdGenShaperLookupPerInterface_Type = DisplayString
_AdGenShaperLookupPerInterface_Object = MibTableColumn
adGenShaperLookupPerInterface = _AdGenShaperLookupPerInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 19, 1, 3, 1, 1),
    _AdGenShaperLookupPerInterface_Type()
)
adGenShaperLookupPerInterface.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenShaperLookupPerInterface.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENSHAPER-MIB",
    **{"adGenShaperProvisioning": adGenShaperProvisioning,
       "adGenShaperProvTable": adGenShaperProvTable,
       "adGenShaperProvEntry": adGenShaperProvEntry,
       "adGenShaperProvName": adGenShaperProvName,
       "adGenShaperProvRowStatus": adGenShaperProvRowStatus,
       "adGenShaperProvOperStatus": adGenShaperProvOperStatus,
       "adGenShaperProvOperStatusDetail": adGenShaperProvOperStatusDetail,
       "adGenShaperProvLastProvError": adGenShaperProvLastProvError,
       "adGenShaperProvApplication": adGenShaperProvApplication,
       "adGenShaperProvRate": adGenShaperProvRate,
       "adGenShaperProvInterface": adGenShaperProvInterface,
       "adGenShaperBurstSize": adGenShaperBurstSize,
       "adGenShaperSlotTable": adGenShaperSlotTable,
       "adGenShaperSlotEntry": adGenShaperSlotEntry,
       "adGenShaperSlotLastCreateError": adGenShaperSlotLastCreateError,
       "adGenShaperLookupPerInterfaceTable": adGenShaperLookupPerInterfaceTable,
       "adGenShaperLookupPerInterfaceEntry": adGenShaperLookupPerInterfaceEntry,
       "adGenShaperLookupPerInterface": adGenShaperLookupPerInterface,
       "adGenShaperMIB": adGenShaperMIB}
)
