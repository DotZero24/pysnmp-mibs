# SNMP MIB module (EDFA-oa-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/cdata/EDFA-oa-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:00:12 2025
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
    "TimeTicks",
    "Unsigned32",
    "enterprises",
    "iso")

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

eponeoc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 34592)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_IpProduct_ObjectIdentity = ObjectIdentity
ipProduct = _IpProduct_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1)
)
if mibBuilder.loadTexts:
    ipProduct.setStatus("current")
_MediaConverter_ObjectIdentity = ObjectIdentity
mediaConverter = _MediaConverter_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 1)
)
if mibBuilder.loadTexts:
    mediaConverter.setStatus("current")
_Edfa_ObjectIdentity = ObjectIdentity
edfa = _Edfa_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5)
)
if mibBuilder.loadTexts:
    edfa.setStatus("current")
_OaEDFAAlarmRangeTable_Object = MibTable
oaEDFAAlarmRangeTable = _OaEDFAAlarmRangeTable_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1)
)
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeTable.setStatus("current")
_OaEDFAAlarmRangeEntry_Object = MibTableRow
oaEDFAAlarmRangeEntry = _OaEDFAAlarmRangeEntry_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1)
)
oaEDFAAlarmRangeEntry.setIndexNames(
    (0, "EDFA-oa-MIB", "oaEDFAAlarmRangeIndex"),
)
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeEntry.setStatus("current")


class _OaEDFAAlarmRangeIndex_Type(Integer32):
    """Custom type oaEDFAAlarmRangeIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_OaEDFAAlarmRangeIndex_Type.__name__ = "Integer32"
_OaEDFAAlarmRangeIndex_Object = MibTableColumn
oaEDFAAlarmRangeIndex = _OaEDFAAlarmRangeIndex_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 1),
    _OaEDFAAlarmRangeIndex_Type()
)
oaEDFAAlarmRangeIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeIndex.setStatus("current")
_OaEDFAAlarmRangeDecr_Type = DisplayString
_OaEDFAAlarmRangeDecr_Object = MibTableColumn
oaEDFAAlarmRangeDecr = _OaEDFAAlarmRangeDecr_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 2),
    _OaEDFAAlarmRangeDecr_Type()
)
oaEDFAAlarmRangeDecr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeDecr.setStatus("mandatory")
_OaEDFAAlarmRangeHIHItoHI_Type = Integer32
_OaEDFAAlarmRangeHIHItoHI_Object = MibTableColumn
oaEDFAAlarmRangeHIHItoHI = _OaEDFAAlarmRangeHIHItoHI_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 3),
    _OaEDFAAlarmRangeHIHItoHI_Type()
)
oaEDFAAlarmRangeHIHItoHI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeHIHItoHI.setStatus("current")
_OaEDFAAlarmRangeHIHItoLO_Type = Integer32
_OaEDFAAlarmRangeHIHItoLO_Object = MibTableColumn
oaEDFAAlarmRangeHIHItoLO = _OaEDFAAlarmRangeHIHItoLO_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 4),
    _OaEDFAAlarmRangeHIHItoLO_Type()
)
oaEDFAAlarmRangeHIHItoLO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeHIHItoLO.setStatus("current")
_OaEDFAAlarmRangeHItoHI_Type = Integer32
_OaEDFAAlarmRangeHItoHI_Object = MibTableColumn
oaEDFAAlarmRangeHItoHI = _OaEDFAAlarmRangeHItoHI_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 5),
    _OaEDFAAlarmRangeHItoHI_Type()
)
oaEDFAAlarmRangeHItoHI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeHItoHI.setStatus("current")
_OaEDFAAlarmRangeHItoLO_Type = Integer32
_OaEDFAAlarmRangeHItoLO_Object = MibTableColumn
oaEDFAAlarmRangeHItoLO = _OaEDFAAlarmRangeHItoLO_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 6),
    _OaEDFAAlarmRangeHItoLO_Type()
)
oaEDFAAlarmRangeHItoLO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeHItoLO.setStatus("current")
_OaEDFAAlarmRangeLOtoHI_Type = Integer32
_OaEDFAAlarmRangeLOtoHI_Object = MibTableColumn
oaEDFAAlarmRangeLOtoHI = _OaEDFAAlarmRangeLOtoHI_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 7),
    _OaEDFAAlarmRangeLOtoHI_Type()
)
oaEDFAAlarmRangeLOtoHI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeLOtoHI.setStatus("current")
_OaEDFAAlarmRangeLOtoLO_Type = Integer32
_OaEDFAAlarmRangeLOtoLO_Object = MibTableColumn
oaEDFAAlarmRangeLOtoLO = _OaEDFAAlarmRangeLOtoLO_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 8),
    _OaEDFAAlarmRangeLOtoLO_Type()
)
oaEDFAAlarmRangeLOtoLO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeLOtoLO.setStatus("current")
_OaEDFAAlarmRangeLOLOtoHI_Type = Integer32
_OaEDFAAlarmRangeLOLOtoHI_Object = MibTableColumn
oaEDFAAlarmRangeLOLOtoHI = _OaEDFAAlarmRangeLOLOtoHI_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 9),
    _OaEDFAAlarmRangeLOLOtoHI_Type()
)
oaEDFAAlarmRangeLOLOtoHI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeLOLOtoHI.setStatus("current")
_OaEDFAAlarmRangeLOLOtoLO_Type = Integer32
_OaEDFAAlarmRangeLOLOtoLO_Object = MibTableColumn
oaEDFAAlarmRangeLOLOtoLO = _OaEDFAAlarmRangeLOLOtoLO_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 10),
    _OaEDFAAlarmRangeLOLOtoLO_Type()
)
oaEDFAAlarmRangeLOLOtoLO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeLOLOtoLO.setStatus("current")
_OaEDFAAlarmRangeDDtoHI_Type = Integer32
_OaEDFAAlarmRangeDDtoHI_Object = MibTableColumn
oaEDFAAlarmRangeDDtoHI = _OaEDFAAlarmRangeDDtoHI_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 11),
    _OaEDFAAlarmRangeDDtoHI_Type()
)
oaEDFAAlarmRangeDDtoHI.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeDDtoHI.setStatus("current")
_OaEDFAAlarmRangeDDtoLO_Type = Integer32
_OaEDFAAlarmRangeDDtoLO_Object = MibTableColumn
oaEDFAAlarmRangeDDtoLO = _OaEDFAAlarmRangeDDtoLO_Object(
    (1, 3, 6, 1, 4, 1, 34592, 1, 5, 1, 1, 12),
    _OaEDFAAlarmRangeDDtoLO_Type()
)
oaEDFAAlarmRangeDDtoLO.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    oaEDFAAlarmRangeDDtoLO.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "EDFA-oa-MIB",
    **{"eponeoc": eponeoc,
       "ipProduct": ipProduct,
       "mediaConverter": mediaConverter,
       "edfa": edfa,
       "oaEDFAAlarmRangeTable": oaEDFAAlarmRangeTable,
       "oaEDFAAlarmRangeEntry": oaEDFAAlarmRangeEntry,
       "oaEDFAAlarmRangeIndex": oaEDFAAlarmRangeIndex,
       "oaEDFAAlarmRangeDecr": oaEDFAAlarmRangeDecr,
       "oaEDFAAlarmRangeHIHItoHI": oaEDFAAlarmRangeHIHItoHI,
       "oaEDFAAlarmRangeHIHItoLO": oaEDFAAlarmRangeHIHItoLO,
       "oaEDFAAlarmRangeHItoHI": oaEDFAAlarmRangeHItoHI,
       "oaEDFAAlarmRangeHItoLO": oaEDFAAlarmRangeHItoLO,
       "oaEDFAAlarmRangeLOtoHI": oaEDFAAlarmRangeLOtoHI,
       "oaEDFAAlarmRangeLOtoLO": oaEDFAAlarmRangeLOtoLO,
       "oaEDFAAlarmRangeLOLOtoHI": oaEDFAAlarmRangeLOLOtoHI,
       "oaEDFAAlarmRangeLOLOtoLO": oaEDFAAlarmRangeLOLOtoLO,
       "oaEDFAAlarmRangeDDtoHI": oaEDFAAlarmRangeDDtoHI,
       "oaEDFAAlarmRangeDDtoLO": oaEDFAAlarmRangeDDtoLO}
)
