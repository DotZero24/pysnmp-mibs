# SNMP MIB module (ADTRAN-GEN-ETHERNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GEN-ETHERNET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:29 2025
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

(adGenEthernet,
 adGenEthernetID) = mibBuilder.importSymbols(
    "ADTRAN-GENTA5K-MIB",
    "adGenEthernet",
    "adGenEthernetID")

(AtmVcIdentifier,
 AtmVpIdentifier) = mibBuilder.importSymbols(
    "ATM-TC-MIB",
    "AtmVcIdentifier",
    "AtmVpIdentifier")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
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

adGenEthernetMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 67, 1, 15, 1)
)
if mibBuilder.loadTexts:
    adGenEthernetMIB.setRevisions(
        ("2011-10-10 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AdGenEthernetCtag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



class AdGenEthernetCrossConnectType(TextualConvention, Integer32):
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("vplCrossConnect", 2),
          ("vclCrossConnect", 3),
          ("evplCrossConnect", 4),
          ("evclCrossConnect", 5),
          ("vplEvplCrossConnect", 6),
          ("vclEvclCrossConnect", 7))
    )



class AdGenEthernetLastChange(TextualConvention, TimeTicks):
    status = "current"


class AdGenEthernetOperStatus(TextualConvention, Integer32):
    status = "current"
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
        *(("up", 1),
          ("down", 2),
          ("testing", 3),
          ("unknown", 4))
    )



class AdGenEthernetStag(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )



# MIB Managed Objects in the order of their OIDs

_AdGenEthernetMIBObjects_ObjectIdentity = ObjectIdentity
adGenEthernetMIBObjects = _AdGenEthernetMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1)
)
_AdGenEthernetModuleConfTable_Object = MibTable
adGenEthernetModuleConfTable = _AdGenEthernetModuleConfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEthernetModuleConfTable.setStatus("current")
_AdGenEthernetModuleConfEntry_Object = MibTableRow
adGenEthernetModuleConfEntry = _AdGenEthernetModuleConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 1, 1)
)
adGenEthernetModuleConfEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetModuleConfEntry.setStatus("current")


class _AdGenEthernetModuleMaxEvpls_Type(Integer32):
    """Custom type adGenEthernetModuleMaxEvpls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenEthernetModuleMaxEvpls_Type.__name__ = "Integer32"
_AdGenEthernetModuleMaxEvpls_Object = MibTableColumn
adGenEthernetModuleMaxEvpls = _AdGenEthernetModuleMaxEvpls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 1, 1, 1),
    _AdGenEthernetModuleMaxEvpls_Type()
)
adGenEthernetModuleMaxEvpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetModuleMaxEvpls.setStatus("current")


class _AdGenEthernetModuleMaxEvcls_Type(Integer32):
    """Custom type adGenEthernetModuleMaxEvcls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenEthernetModuleMaxEvcls_Type.__name__ = "Integer32"
_AdGenEthernetModuleMaxEvcls_Object = MibTableColumn
adGenEthernetModuleMaxEvcls = _AdGenEthernetModuleMaxEvcls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 1, 1, 2),
    _AdGenEthernetModuleMaxEvcls_Type()
)
adGenEthernetModuleMaxEvcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetModuleMaxEvcls.setStatus("current")


class _AdGenEthernetModuleConfEvpls_Type(Integer32):
    """Custom type adGenEthernetModuleConfEvpls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenEthernetModuleConfEvpls_Type.__name__ = "Integer32"
_AdGenEthernetModuleConfEvpls_Object = MibTableColumn
adGenEthernetModuleConfEvpls = _AdGenEthernetModuleConfEvpls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 1, 1, 3),
    _AdGenEthernetModuleConfEvpls_Type()
)
adGenEthernetModuleConfEvpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetModuleConfEvpls.setStatus("current")


class _AdGenEthernetModuleConfEvcls_Type(Integer32):
    """Custom type adGenEthernetModuleConfEvcls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenEthernetModuleConfEvcls_Type.__name__ = "Integer32"
_AdGenEthernetModuleConfEvcls_Object = MibTableColumn
adGenEthernetModuleConfEvcls = _AdGenEthernetModuleConfEvcls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 1, 1, 4),
    _AdGenEthernetModuleConfEvcls_Type()
)
adGenEthernetModuleConfEvcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetModuleConfEvcls.setStatus("current")
_AdGenEthernetInterfaceConfTable_Object = MibTable
adGenEthernetInterfaceConfTable = _AdGenEthernetInterfaceConfTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 2)
)
if mibBuilder.loadTexts:
    adGenEthernetInterfaceConfTable.setStatus("current")
_AdGenEthernetInterfaceConfEntry_Object = MibTableRow
adGenEthernetInterfaceConfEntry = _AdGenEthernetInterfaceConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 2, 1)
)
adGenEthernetInterfaceConfEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetInterfaceConfEntry.setStatus("current")


class _AdGenEthernetInterfaceMaxEvpls_Type(Integer32):
    """Custom type adGenEthernetInterfaceMaxEvpls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenEthernetInterfaceMaxEvpls_Type.__name__ = "Integer32"
_AdGenEthernetInterfaceMaxEvpls_Object = MibTableColumn
adGenEthernetInterfaceMaxEvpls = _AdGenEthernetInterfaceMaxEvpls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 2, 1, 1),
    _AdGenEthernetInterfaceMaxEvpls_Type()
)
adGenEthernetInterfaceMaxEvpls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthernetInterfaceMaxEvpls.setStatus("current")


class _AdGenEthernetInterfaceMaxEvcls_Type(Integer32):
    """Custom type adGenEthernetInterfaceMaxEvcls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenEthernetInterfaceMaxEvcls_Type.__name__ = "Integer32"
_AdGenEthernetInterfaceMaxEvcls_Object = MibTableColumn
adGenEthernetInterfaceMaxEvcls = _AdGenEthernetInterfaceMaxEvcls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 2, 1, 2),
    _AdGenEthernetInterfaceMaxEvcls_Type()
)
adGenEthernetInterfaceMaxEvcls.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenEthernetInterfaceMaxEvcls.setStatus("current")


class _AdGenEthernetInterfaceConfEvpls_Type(Integer32):
    """Custom type adGenEthernetInterfaceConfEvpls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenEthernetInterfaceConfEvpls_Type.__name__ = "Integer32"
_AdGenEthernetInterfaceConfEvpls_Object = MibTableColumn
adGenEthernetInterfaceConfEvpls = _AdGenEthernetInterfaceConfEvpls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 2, 1, 3),
    _AdGenEthernetInterfaceConfEvpls_Type()
)
adGenEthernetInterfaceConfEvpls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetInterfaceConfEvpls.setStatus("current")


class _AdGenEthernetInterfaceConfEvcls_Type(Integer32):
    """Custom type adGenEthernetInterfaceConfEvcls based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenEthernetInterfaceConfEvcls_Type.__name__ = "Integer32"
_AdGenEthernetInterfaceConfEvcls_Object = MibTableColumn
adGenEthernetInterfaceConfEvcls = _AdGenEthernetInterfaceConfEvcls_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 2, 1, 4),
    _AdGenEthernetInterfaceConfEvcls_Type()
)
adGenEthernetInterfaceConfEvcls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetInterfaceConfEvcls.setStatus("current")
_AdGenEthernetVplStatus_Type = DisplayString
_AdGenEthernetVplStatus_Object = MibScalar
adGenEthernetVplStatus = _AdGenEthernetVplStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 3),
    _AdGenEthernetVplStatus_Type()
)
adGenEthernetVplStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplStatus.setStatus("current")
_AdGenEthernetVplTable_Object = MibTable
adGenEthernetVplTable = _AdGenEthernetVplTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 4)
)
if mibBuilder.loadTexts:
    adGenEthernetVplTable.setStatus("current")
_AdGenEthernetVplEntry_Object = MibTableRow
adGenEthernetVplEntry = _AdGenEthernetVplEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 4, 1)
)
adGenEthernetVplEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVplStag"),
)
if mibBuilder.loadTexts:
    adGenEthernetVplEntry.setStatus("current")
_AdGenEthernetVplStag_Type = AdGenEthernetStag
_AdGenEthernetVplStag_Object = MibTableColumn
adGenEthernetVplStag = _AdGenEthernetVplStag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 4, 1, 1),
    _AdGenEthernetVplStag_Type()
)
adGenEthernetVplStag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVplStag.setStatus("current")
_AdGenEthernetVplName_Type = DisplayString
_AdGenEthernetVplName_Object = MibTableColumn
adGenEthernetVplName = _AdGenEthernetVplName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 4, 1, 2),
    _AdGenEthernetVplName_Type()
)
adGenEthernetVplName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetVplName.setStatus("current")
_AdGenEthernetVplOperStatus_Type = AdGenEthernetOperStatus
_AdGenEthernetVplOperStatus_Object = MibTableColumn
adGenEthernetVplOperStatus = _AdGenEthernetVplOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 4, 1, 3),
    _AdGenEthernetVplOperStatus_Type()
)
adGenEthernetVplOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplOperStatus.setStatus("current")
_AdGenEthernetVplLastChange_Type = AdGenEthernetLastChange
_AdGenEthernetVplLastChange_Object = MibTableColumn
adGenEthernetVplLastChange = _AdGenEthernetVplLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 4, 1, 4),
    _AdGenEthernetVplLastChange_Type()
)
adGenEthernetVplLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplLastChange.setStatus("current")
_AdGenEthernetVplCrossConnectType_Type = AdGenEthernetCrossConnectType
_AdGenEthernetVplCrossConnectType_Object = MibTableColumn
adGenEthernetVplCrossConnectType = _AdGenEthernetVplCrossConnectType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 4, 1, 5),
    _AdGenEthernetVplCrossConnectType_Type()
)
adGenEthernetVplCrossConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplCrossConnectType.setStatus("current")


class _AdGenEthernetVplCrossConnectIdentifier_Type(Integer32):
    """Custom type adGenEthernetVplCrossConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AdGenEthernetVplCrossConnectIdentifier_Type.__name__ = "Integer32"
_AdGenEthernetVplCrossConnectIdentifier_Object = MibTableColumn
adGenEthernetVplCrossConnectIdentifier = _AdGenEthernetVplCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 4, 1, 6),
    _AdGenEthernetVplCrossConnectIdentifier_Type()
)
adGenEthernetVplCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplCrossConnectIdentifier.setStatus("current")
_AdGenEthernetVplLastError_Type = DisplayString
_AdGenEthernetVplLastError_Object = MibTableColumn
adGenEthernetVplLastError = _AdGenEthernetVplLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 4, 1, 7),
    _AdGenEthernetVplLastError_Type()
)
adGenEthernetVplLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplLastError.setStatus("current")


class _AdGenEthernetVplRowStatus_Type(RowStatus):
    """Custom type adGenEthernetVplRowStatus based on RowStatus"""
    defaultValue = 1


_AdGenEthernetVplRowStatus_Type.__name__ = "RowStatus"
_AdGenEthernetVplRowStatus_Object = MibTableColumn
adGenEthernetVplRowStatus = _AdGenEthernetVplRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 4, 1, 8),
    _AdGenEthernetVplRowStatus_Type()
)
adGenEthernetVplRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetVplRowStatus.setStatus("current")
_AdGenEthernetVclStatus_Type = DisplayString
_AdGenEthernetVclStatus_Object = MibScalar
adGenEthernetVclStatus = _AdGenEthernetVclStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 5),
    _AdGenEthernetVclStatus_Type()
)
adGenEthernetVclStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclStatus.setStatus("current")
_AdGenEthernetVclTable_Object = MibTable
adGenEthernetVclTable = _AdGenEthernetVclTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6)
)
if mibBuilder.loadTexts:
    adGenEthernetVclTable.setStatus("current")
_AdGenEthernetVclEntry_Object = MibTableRow
adGenEthernetVclEntry = _AdGenEthernetVclEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6, 1)
)
adGenEthernetVclEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVclStag"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVclCtag"),
)
if mibBuilder.loadTexts:
    adGenEthernetVclEntry.setStatus("current")
_AdGenEthernetVclStag_Type = AdGenEthernetStag
_AdGenEthernetVclStag_Object = MibTableColumn
adGenEthernetVclStag = _AdGenEthernetVclStag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6, 1, 1),
    _AdGenEthernetVclStag_Type()
)
adGenEthernetVclStag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVclStag.setStatus("current")
_AdGenEthernetVclCtag_Type = AdGenEthernetCtag
_AdGenEthernetVclCtag_Object = MibTableColumn
adGenEthernetVclCtag = _AdGenEthernetVclCtag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6, 1, 2),
    _AdGenEthernetVclCtag_Type()
)
adGenEthernetVclCtag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVclCtag.setStatus("current")
_AdGenEthernetVclName_Type = DisplayString
_AdGenEthernetVclName_Object = MibTableColumn
adGenEthernetVclName = _AdGenEthernetVclName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6, 1, 3),
    _AdGenEthernetVclName_Type()
)
adGenEthernetVclName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetVclName.setStatus("current")
_AdGenEthernetVclOperStatus_Type = AdGenEthernetOperStatus
_AdGenEthernetVclOperStatus_Object = MibTableColumn
adGenEthernetVclOperStatus = _AdGenEthernetVclOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6, 1, 4),
    _AdGenEthernetVclOperStatus_Type()
)
adGenEthernetVclOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclOperStatus.setStatus("current")
_AdGenEthernetVclLastChange_Type = AdGenEthernetLastChange
_AdGenEthernetVclLastChange_Object = MibTableColumn
adGenEthernetVclLastChange = _AdGenEthernetVclLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6, 1, 5),
    _AdGenEthernetVclLastChange_Type()
)
adGenEthernetVclLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclLastChange.setStatus("current")
_AdGenEthernetVclCrossConnectType_Type = AdGenEthernetCrossConnectType
_AdGenEthernetVclCrossConnectType_Object = MibTableColumn
adGenEthernetVclCrossConnectType = _AdGenEthernetVclCrossConnectType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6, 1, 6),
    _AdGenEthernetVclCrossConnectType_Type()
)
adGenEthernetVclCrossConnectType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclCrossConnectType.setStatus("current")


class _AdGenEthernetVclCrossConnectIdentifier_Type(Integer32):
    """Custom type adGenEthernetVclCrossConnectIdentifier based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2147483647),
    )


_AdGenEthernetVclCrossConnectIdentifier_Type.__name__ = "Integer32"
_AdGenEthernetVclCrossConnectIdentifier_Object = MibTableColumn
adGenEthernetVclCrossConnectIdentifier = _AdGenEthernetVclCrossConnectIdentifier_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6, 1, 7),
    _AdGenEthernetVclCrossConnectIdentifier_Type()
)
adGenEthernetVclCrossConnectIdentifier.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclCrossConnectIdentifier.setStatus("current")
_AdGenEthernetVclLastError_Type = DisplayString
_AdGenEthernetVclLastError_Object = MibTableColumn
adGenEthernetVclLastError = _AdGenEthernetVclLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6, 1, 8),
    _AdGenEthernetVclLastError_Type()
)
adGenEthernetVclLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclLastError.setStatus("current")


class _AdGenEthernetVclRowStatus_Type(RowStatus):
    """Custom type adGenEthernetVclRowStatus based on RowStatus"""
    defaultValue = 1


_AdGenEthernetVclRowStatus_Type.__name__ = "RowStatus"
_AdGenEthernetVclRowStatus_Object = MibTableColumn
adGenEthernetVclRowStatus = _AdGenEthernetVclRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 6, 1, 9),
    _AdGenEthernetVclRowStatus_Type()
)
adGenEthernetVclRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetVclRowStatus.setStatus("current")
_AdGenEthernetVclEvclCrossConnectNumberNext_Type = Integer32
_AdGenEthernetVclEvclCrossConnectNumberNext_Object = MibScalar
adGenEthernetVclEvclCrossConnectNumberNext = _AdGenEthernetVclEvclCrossConnectNumberNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 7),
    _AdGenEthernetVclEvclCrossConnectNumberNext_Type()
)
adGenEthernetVclEvclCrossConnectNumberNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectNumberNext.setStatus("current")
_AdGenEthernetVclEvclCrossConnectFailureCounter_Type = Integer32
_AdGenEthernetVclEvclCrossConnectFailureCounter_Object = MibScalar
adGenEthernetVclEvclCrossConnectFailureCounter = _AdGenEthernetVclEvclCrossConnectFailureCounter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 8),
    _AdGenEthernetVclEvclCrossConnectFailureCounter_Type()
)
adGenEthernetVclEvclCrossConnectFailureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectFailureCounter.setStatus("current")
_AdGenEthernetVclEvclCrossConnectStatus_Type = DisplayString
_AdGenEthernetVclEvclCrossConnectStatus_Object = MibScalar
adGenEthernetVclEvclCrossConnectStatus = _AdGenEthernetVclEvclCrossConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 9),
    _AdGenEthernetVclEvclCrossConnectStatus_Type()
)
adGenEthernetVclEvclCrossConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectStatus.setStatus("current")
_AdGenEthernetVclEvclCrossConnectTable_Object = MibTable
adGenEthernetVclEvclCrossConnectTable = _AdGenEthernetVclEvclCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10)
)
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectTable.setStatus("current")
_AdGenEthernetVclEvclCrossConnectEntry_Object = MibTableRow
adGenEthernetVclEvclCrossConnectEntry = _AdGenEthernetVclEvclCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1)
)
adGenEthernetVclEvclCrossConnectEntry.setIndexNames(
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVclEvclCrossConnectIndex"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVclEvclCrossConnectAtmIfIndex"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVclEvclCrossConnectAtmVpi"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVclEvclCrossConnectAtmVci"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVclEvclCrossConnectEthIfIndex"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVclEvclCrossConnectEthStag"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVclEvclCrossConnectEthCtag"),
)
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectEntry.setStatus("current")


class _AdGenEthernetVclEvclCrossConnectIndex_Type(Integer32):
    """Custom type adGenEthernetVclEvclCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdGenEthernetVclEvclCrossConnectIndex_Type.__name__ = "Integer32"
_AdGenEthernetVclEvclCrossConnectIndex_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectIndex = _AdGenEthernetVclEvclCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 1),
    _AdGenEthernetVclEvclCrossConnectIndex_Type()
)
adGenEthernetVclEvclCrossConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectIndex.setStatus("current")
_AdGenEthernetVclEvclCrossConnectAtmIfIndex_Type = InterfaceIndex
_AdGenEthernetVclEvclCrossConnectAtmIfIndex_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectAtmIfIndex = _AdGenEthernetVclEvclCrossConnectAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 2),
    _AdGenEthernetVclEvclCrossConnectAtmIfIndex_Type()
)
adGenEthernetVclEvclCrossConnectAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectAtmIfIndex.setStatus("current")
_AdGenEthernetVclEvclCrossConnectAtmVpi_Type = AtmVpIdentifier
_AdGenEthernetVclEvclCrossConnectAtmVpi_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectAtmVpi = _AdGenEthernetVclEvclCrossConnectAtmVpi_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 3),
    _AdGenEthernetVclEvclCrossConnectAtmVpi_Type()
)
adGenEthernetVclEvclCrossConnectAtmVpi.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectAtmVpi.setStatus("current")
_AdGenEthernetVclEvclCrossConnectAtmVci_Type = AtmVcIdentifier
_AdGenEthernetVclEvclCrossConnectAtmVci_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectAtmVci = _AdGenEthernetVclEvclCrossConnectAtmVci_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 4),
    _AdGenEthernetVclEvclCrossConnectAtmVci_Type()
)
adGenEthernetVclEvclCrossConnectAtmVci.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectAtmVci.setStatus("current")
_AdGenEthernetVclEvclCrossConnectEthIfIndex_Type = InterfaceIndex
_AdGenEthernetVclEvclCrossConnectEthIfIndex_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectEthIfIndex = _AdGenEthernetVclEvclCrossConnectEthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 5),
    _AdGenEthernetVclEvclCrossConnectEthIfIndex_Type()
)
adGenEthernetVclEvclCrossConnectEthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectEthIfIndex.setStatus("current")
_AdGenEthernetVclEvclCrossConnectEthStag_Type = AdGenEthernetStag
_AdGenEthernetVclEvclCrossConnectEthStag_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectEthStag = _AdGenEthernetVclEvclCrossConnectEthStag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 6),
    _AdGenEthernetVclEvclCrossConnectEthStag_Type()
)
adGenEthernetVclEvclCrossConnectEthStag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectEthStag.setStatus("current")
_AdGenEthernetVclEvclCrossConnectEthCtag_Type = AdGenEthernetCtag
_AdGenEthernetVclEvclCrossConnectEthCtag_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectEthCtag = _AdGenEthernetVclEvclCrossConnectEthCtag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 7),
    _AdGenEthernetVclEvclCrossConnectEthCtag_Type()
)
adGenEthernetVclEvclCrossConnectEthCtag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectEthCtag.setStatus("current")
_AdGenEthernetVclEvclCrossConnectName_Type = DisplayString
_AdGenEthernetVclEvclCrossConnectName_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectName = _AdGenEthernetVclEvclCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 8),
    _AdGenEthernetVclEvclCrossConnectName_Type()
)
adGenEthernetVclEvclCrossConnectName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectName.setStatus("current")
_AdGenEthernetVclEvclCrossConnectOperStatus_Type = AdGenEthernetOperStatus
_AdGenEthernetVclEvclCrossConnectOperStatus_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectOperStatus = _AdGenEthernetVclEvclCrossConnectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 9),
    _AdGenEthernetVclEvclCrossConnectOperStatus_Type()
)
adGenEthernetVclEvclCrossConnectOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectOperStatus.setStatus("current")
_AdGenEthernetVclEvclCrossConnectLastChange_Type = AdGenEthernetLastChange
_AdGenEthernetVclEvclCrossConnectLastChange_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectLastChange = _AdGenEthernetVclEvclCrossConnectLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 10),
    _AdGenEthernetVclEvclCrossConnectLastChange_Type()
)
adGenEthernetVclEvclCrossConnectLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectLastChange.setStatus("current")
_AdGenEthernetVclEvclCrossConnectLastError_Type = DisplayString
_AdGenEthernetVclEvclCrossConnectLastError_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectLastError = _AdGenEthernetVclEvclCrossConnectLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 11),
    _AdGenEthernetVclEvclCrossConnectLastError_Type()
)
adGenEthernetVclEvclCrossConnectLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectLastError.setStatus("current")


class _AdGenEthernetVclEvclCrossConnectRowStatus_Type(RowStatus):
    """Custom type adGenEthernetVclEvclCrossConnectRowStatus based on RowStatus"""
    defaultValue = 1


_AdGenEthernetVclEvclCrossConnectRowStatus_Type.__name__ = "RowStatus"
_AdGenEthernetVclEvclCrossConnectRowStatus_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectRowStatus = _AdGenEthernetVclEvclCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 12),
    _AdGenEthernetVclEvclCrossConnectRowStatus_Type()
)
adGenEthernetVclEvclCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectRowStatus.setStatus("current")
_AdGenEthernetVclEvclCrossConnectOption82Insert_Type = TruthValue
_AdGenEthernetVclEvclCrossConnectOption82Insert_Object = MibTableColumn
adGenEthernetVclEvclCrossConnectOption82Insert = _AdGenEthernetVclEvclCrossConnectOption82Insert_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 10, 1, 13),
    _AdGenEthernetVclEvclCrossConnectOption82Insert_Type()
)
adGenEthernetVclEvclCrossConnectOption82Insert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetVclEvclCrossConnectOption82Insert.setStatus("current")
_AdGenEthernetVplEvplCrossConnectNumberNext_Type = Integer32
_AdGenEthernetVplEvplCrossConnectNumberNext_Object = MibScalar
adGenEthernetVplEvplCrossConnectNumberNext = _AdGenEthernetVplEvplCrossConnectNumberNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 11),
    _AdGenEthernetVplEvplCrossConnectNumberNext_Type()
)
adGenEthernetVplEvplCrossConnectNumberNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectNumberNext.setStatus("current")
_AdGenEthernetVplEvplCrossConnectFailureCounter_Type = Integer32
_AdGenEthernetVplEvplCrossConnectFailureCounter_Object = MibScalar
adGenEthernetVplEvplCrossConnectFailureCounter = _AdGenEthernetVplEvplCrossConnectFailureCounter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 12),
    _AdGenEthernetVplEvplCrossConnectFailureCounter_Type()
)
adGenEthernetVplEvplCrossConnectFailureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectFailureCounter.setStatus("current")
_AdGenEthernetVplEvplCrossConnectStatus_Type = DisplayString
_AdGenEthernetVplEvplCrossConnectStatus_Object = MibScalar
adGenEthernetVplEvplCrossConnectStatus = _AdGenEthernetVplEvplCrossConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 13),
    _AdGenEthernetVplEvplCrossConnectStatus_Type()
)
adGenEthernetVplEvplCrossConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectStatus.setStatus("current")
_AdGenEthernetVplEvplCrossConnectTable_Object = MibTable
adGenEthernetVplEvplCrossConnectTable = _AdGenEthernetVplEvplCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14)
)
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectTable.setStatus("current")
_AdGenEthernetVplEvplCrossConnectEntry_Object = MibTableRow
adGenEthernetVplEvplCrossConnectEntry = _AdGenEthernetVplEvplCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1)
)
adGenEthernetVplEvplCrossConnectEntry.setIndexNames(
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVplEvplCrossConnectIndex"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVplEvplCrossConnectAtmIfIndex"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVplEvplCrossConnectAtmVp"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVplEvplCrossConnectEthIfIndex"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVplEvplCrossConnectEthStag"),
)
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectEntry.setStatus("current")


class _AdGenEthernetVplEvplCrossConnectIndex_Type(Integer32):
    """Custom type adGenEthernetVplEvplCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdGenEthernetVplEvplCrossConnectIndex_Type.__name__ = "Integer32"
_AdGenEthernetVplEvplCrossConnectIndex_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectIndex = _AdGenEthernetVplEvplCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 1),
    _AdGenEthernetVplEvplCrossConnectIndex_Type()
)
adGenEthernetVplEvplCrossConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectIndex.setStatus("current")
_AdGenEthernetVplEvplCrossConnectAtmIfIndex_Type = InterfaceIndex
_AdGenEthernetVplEvplCrossConnectAtmIfIndex_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectAtmIfIndex = _AdGenEthernetVplEvplCrossConnectAtmIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 2),
    _AdGenEthernetVplEvplCrossConnectAtmIfIndex_Type()
)
adGenEthernetVplEvplCrossConnectAtmIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectAtmIfIndex.setStatus("current")
_AdGenEthernetVplEvplCrossConnectAtmVp_Type = AtmVpIdentifier
_AdGenEthernetVplEvplCrossConnectAtmVp_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectAtmVp = _AdGenEthernetVplEvplCrossConnectAtmVp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 3),
    _AdGenEthernetVplEvplCrossConnectAtmVp_Type()
)
adGenEthernetVplEvplCrossConnectAtmVp.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectAtmVp.setStatus("current")
_AdGenEthernetVplEvplCrossConnectEthIfIndex_Type = InterfaceIndex
_AdGenEthernetVplEvplCrossConnectEthIfIndex_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectEthIfIndex = _AdGenEthernetVplEvplCrossConnectEthIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 4),
    _AdGenEthernetVplEvplCrossConnectEthIfIndex_Type()
)
adGenEthernetVplEvplCrossConnectEthIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectEthIfIndex.setStatus("current")
_AdGenEthernetVplEvplCrossConnectEthStag_Type = AdGenEthernetStag
_AdGenEthernetVplEvplCrossConnectEthStag_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectEthStag = _AdGenEthernetVplEvplCrossConnectEthStag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 5),
    _AdGenEthernetVplEvplCrossConnectEthStag_Type()
)
adGenEthernetVplEvplCrossConnectEthStag.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectEthStag.setStatus("current")
_AdGenEthernetVplEvplCrossConnectName_Type = DisplayString
_AdGenEthernetVplEvplCrossConnectName_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectName = _AdGenEthernetVplEvplCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 6),
    _AdGenEthernetVplEvplCrossConnectName_Type()
)
adGenEthernetVplEvplCrossConnectName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectName.setStatus("current")
_AdGenEthernetVplEvplCrossConnectOperStatus_Type = AdGenEthernetOperStatus
_AdGenEthernetVplEvplCrossConnectOperStatus_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectOperStatus = _AdGenEthernetVplEvplCrossConnectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 7),
    _AdGenEthernetVplEvplCrossConnectOperStatus_Type()
)
adGenEthernetVplEvplCrossConnectOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectOperStatus.setStatus("current")
_AdGenEthernetVplEvplCrossConnectLastChange_Type = AdGenEthernetLastChange
_AdGenEthernetVplEvplCrossConnectLastChange_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectLastChange = _AdGenEthernetVplEvplCrossConnectLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 8),
    _AdGenEthernetVplEvplCrossConnectLastChange_Type()
)
adGenEthernetVplEvplCrossConnectLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectLastChange.setStatus("current")
_AdGenEthernetVplEvplCrossConnectLastError_Type = DisplayString
_AdGenEthernetVplEvplCrossConnectLastError_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectLastError = _AdGenEthernetVplEvplCrossConnectLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 9),
    _AdGenEthernetVplEvplCrossConnectLastError_Type()
)
adGenEthernetVplEvplCrossConnectLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectLastError.setStatus("current")


class _AdGenEthernetVplEvplCrossConnectRowStatus_Type(RowStatus):
    """Custom type adGenEthernetVplEvplCrossConnectRowStatus based on RowStatus"""
    defaultValue = 1


_AdGenEthernetVplEvplCrossConnectRowStatus_Type.__name__ = "RowStatus"
_AdGenEthernetVplEvplCrossConnectRowStatus_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectRowStatus = _AdGenEthernetVplEvplCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 10),
    _AdGenEthernetVplEvplCrossConnectRowStatus_Type()
)
adGenEthernetVplEvplCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectRowStatus.setStatus("current")
_AdGenEthernetVplEvplCrossConnectOption82Insert_Type = TruthValue
_AdGenEthernetVplEvplCrossConnectOption82Insert_Object = MibTableColumn
adGenEthernetVplEvplCrossConnectOption82Insert = _AdGenEthernetVplEvplCrossConnectOption82Insert_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 14, 1, 11),
    _AdGenEthernetVplEvplCrossConnectOption82Insert_Type()
)
adGenEthernetVplEvplCrossConnectOption82Insert.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetVplEvplCrossConnectOption82Insert.setStatus("current")
_AdGenEthernetEvplCrossConnectNumberNext_Type = Integer32
_AdGenEthernetEvplCrossConnectNumberNext_Object = MibScalar
adGenEthernetEvplCrossConnectNumberNext = _AdGenEthernetEvplCrossConnectNumberNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 15),
    _AdGenEthernetEvplCrossConnectNumberNext_Type()
)
adGenEthernetEvplCrossConnectNumberNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectNumberNext.setStatus("current")
_AdGenEthernetEvplCrossConnectFailureCounter_Type = Integer32
_AdGenEthernetEvplCrossConnectFailureCounter_Object = MibScalar
adGenEthernetEvplCrossConnectFailureCounter = _AdGenEthernetEvplCrossConnectFailureCounter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 16),
    _AdGenEthernetEvplCrossConnectFailureCounter_Type()
)
adGenEthernetEvplCrossConnectFailureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectFailureCounter.setStatus("current")
_AdGenEthernetEvplCrossConnectStatus_Type = DisplayString
_AdGenEthernetEvplCrossConnectStatus_Object = MibScalar
adGenEthernetEvplCrossConnectStatus = _AdGenEthernetEvplCrossConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 17),
    _AdGenEthernetEvplCrossConnectStatus_Type()
)
adGenEthernetEvplCrossConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectStatus.setStatus("current")
_AdGenEthernetEvplCrossConnectTable_Object = MibTable
adGenEthernetEvplCrossConnectTable = _AdGenEthernetEvplCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18)
)
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectTable.setStatus("current")
_AdGenEthernetEvplCrossConnectEntry_Object = MibTableRow
adGenEthernetEvplCrossConnectEntry = _AdGenEthernetEvplCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1)
)
adGenEthernetEvplCrossConnectEntry.setIndexNames(
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvplCrossConnectIndex"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvplCrossConnectIfIndex1"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvplCrossConnectStag1"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvplCrossConnectIfIndex2"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvplCrossConnectStag2"),
)
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectEntry.setStatus("current")


class _AdGenEthernetEvplCrossConnectIndex_Type(Integer32):
    """Custom type adGenEthernetEvplCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdGenEthernetEvplCrossConnectIndex_Type.__name__ = "Integer32"
_AdGenEthernetEvplCrossConnectIndex_Object = MibTableColumn
adGenEthernetEvplCrossConnectIndex = _AdGenEthernetEvplCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1, 1),
    _AdGenEthernetEvplCrossConnectIndex_Type()
)
adGenEthernetEvplCrossConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectIndex.setStatus("current")
_AdGenEthernetEvplCrossConnectIfIndex1_Type = InterfaceIndex
_AdGenEthernetEvplCrossConnectIfIndex1_Object = MibTableColumn
adGenEthernetEvplCrossConnectIfIndex1 = _AdGenEthernetEvplCrossConnectIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1, 2),
    _AdGenEthernetEvplCrossConnectIfIndex1_Type()
)
adGenEthernetEvplCrossConnectIfIndex1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectIfIndex1.setStatus("current")
_AdGenEthernetEvplCrossConnectStag1_Type = AdGenEthernetStag
_AdGenEthernetEvplCrossConnectStag1_Object = MibTableColumn
adGenEthernetEvplCrossConnectStag1 = _AdGenEthernetEvplCrossConnectStag1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1, 3),
    _AdGenEthernetEvplCrossConnectStag1_Type()
)
adGenEthernetEvplCrossConnectStag1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectStag1.setStatus("current")
_AdGenEthernetEvplCrossConnectIfIndex2_Type = InterfaceIndex
_AdGenEthernetEvplCrossConnectIfIndex2_Object = MibTableColumn
adGenEthernetEvplCrossConnectIfIndex2 = _AdGenEthernetEvplCrossConnectIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1, 4),
    _AdGenEthernetEvplCrossConnectIfIndex2_Type()
)
adGenEthernetEvplCrossConnectIfIndex2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectIfIndex2.setStatus("current")
_AdGenEthernetEvplCrossConnectStag2_Type = AdGenEthernetStag
_AdGenEthernetEvplCrossConnectStag2_Object = MibTableColumn
adGenEthernetEvplCrossConnectStag2 = _AdGenEthernetEvplCrossConnectStag2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1, 5),
    _AdGenEthernetEvplCrossConnectStag2_Type()
)
adGenEthernetEvplCrossConnectStag2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectStag2.setStatus("current")
_AdGenEthernetEvplCrossConnectName_Type = DisplayString
_AdGenEthernetEvplCrossConnectName_Object = MibTableColumn
adGenEthernetEvplCrossConnectName = _AdGenEthernetEvplCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1, 6),
    _AdGenEthernetEvplCrossConnectName_Type()
)
adGenEthernetEvplCrossConnectName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectName.setStatus("current")
_AdGenEthernetEvplCrossConnectOperStatus_Type = AdGenEthernetOperStatus
_AdGenEthernetEvplCrossConnectOperStatus_Object = MibTableColumn
adGenEthernetEvplCrossConnectOperStatus = _AdGenEthernetEvplCrossConnectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1, 7),
    _AdGenEthernetEvplCrossConnectOperStatus_Type()
)
adGenEthernetEvplCrossConnectOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectOperStatus.setStatus("current")
_AdGenEthernetEvplCrossConnectLastChange_Type = AdGenEthernetLastChange
_AdGenEthernetEvplCrossConnectLastChange_Object = MibTableColumn
adGenEthernetEvplCrossConnectLastChange = _AdGenEthernetEvplCrossConnectLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1, 8),
    _AdGenEthernetEvplCrossConnectLastChange_Type()
)
adGenEthernetEvplCrossConnectLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectLastChange.setStatus("current")
_AdGenEthernetEvplCrossConnectLastError_Type = DisplayString
_AdGenEthernetEvplCrossConnectLastError_Object = MibTableColumn
adGenEthernetEvplCrossConnectLastError = _AdGenEthernetEvplCrossConnectLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1, 9),
    _AdGenEthernetEvplCrossConnectLastError_Type()
)
adGenEthernetEvplCrossConnectLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectLastError.setStatus("current")


class _AdGenEthernetEvplCrossConnectRowStatus_Type(RowStatus):
    """Custom type adGenEthernetEvplCrossConnectRowStatus based on RowStatus"""
    defaultValue = 1


_AdGenEthernetEvplCrossConnectRowStatus_Type.__name__ = "RowStatus"
_AdGenEthernetEvplCrossConnectRowStatus_Object = MibTableColumn
adGenEthernetEvplCrossConnectRowStatus = _AdGenEthernetEvplCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 18, 1, 10),
    _AdGenEthernetEvplCrossConnectRowStatus_Type()
)
adGenEthernetEvplCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetEvplCrossConnectRowStatus.setStatus("current")
_AdGenEthernetEvclCrossConnectNumberNext_Type = Integer32
_AdGenEthernetEvclCrossConnectNumberNext_Object = MibScalar
adGenEthernetEvclCrossConnectNumberNext = _AdGenEthernetEvclCrossConnectNumberNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 19),
    _AdGenEthernetEvclCrossConnectNumberNext_Type()
)
adGenEthernetEvclCrossConnectNumberNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectNumberNext.setStatus("current")
_AdGenEthernetEvclCrossConnectFailureCounter_Type = Integer32
_AdGenEthernetEvclCrossConnectFailureCounter_Object = MibScalar
adGenEthernetEvclCrossConnectFailureCounter = _AdGenEthernetEvclCrossConnectFailureCounter_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 20),
    _AdGenEthernetEvclCrossConnectFailureCounter_Type()
)
adGenEthernetEvclCrossConnectFailureCounter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectFailureCounter.setStatus("current")
_AdGenEthernetEvclCrossConnectStatus_Type = DisplayString
_AdGenEthernetEvclCrossConnectStatus_Object = MibScalar
adGenEthernetEvclCrossConnectStatus = _AdGenEthernetEvclCrossConnectStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 21),
    _AdGenEthernetEvclCrossConnectStatus_Type()
)
adGenEthernetEvclCrossConnectStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectStatus.setStatus("current")
_AdGenEthernetEvclCrossConnectTable_Object = MibTable
adGenEthernetEvclCrossConnectTable = _AdGenEthernetEvclCrossConnectTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22)
)
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectTable.setStatus("current")
_AdGenEthernetEvclCrossConnectEntry_Object = MibTableRow
adGenEthernetEvclCrossConnectEntry = _AdGenEthernetEvclCrossConnectEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1)
)
adGenEthernetEvclCrossConnectEntry.setIndexNames(
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvclCrossConnectIndex"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvclCrossConnectIfIndex1"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvclCrossConnectStag1"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvclCrossConnectCtag1"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvclCrossConnectIfIndex2"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvclCrossConnectStag2"),
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetEvclCrossConnectCtag2"),
)
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectEntry.setStatus("current")


class _AdGenEthernetEvclCrossConnectIndex_Type(Integer32):
    """Custom type adGenEthernetEvclCrossConnectIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_AdGenEthernetEvclCrossConnectIndex_Type.__name__ = "Integer32"
_AdGenEthernetEvclCrossConnectIndex_Object = MibTableColumn
adGenEthernetEvclCrossConnectIndex = _AdGenEthernetEvclCrossConnectIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 1),
    _AdGenEthernetEvclCrossConnectIndex_Type()
)
adGenEthernetEvclCrossConnectIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectIndex.setStatus("current")
_AdGenEthernetEvclCrossConnectIfIndex1_Type = InterfaceIndex
_AdGenEthernetEvclCrossConnectIfIndex1_Object = MibTableColumn
adGenEthernetEvclCrossConnectIfIndex1 = _AdGenEthernetEvclCrossConnectIfIndex1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 2),
    _AdGenEthernetEvclCrossConnectIfIndex1_Type()
)
adGenEthernetEvclCrossConnectIfIndex1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectIfIndex1.setStatus("current")
_AdGenEthernetEvclCrossConnectStag1_Type = AdGenEthernetStag
_AdGenEthernetEvclCrossConnectStag1_Object = MibTableColumn
adGenEthernetEvclCrossConnectStag1 = _AdGenEthernetEvclCrossConnectStag1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 3),
    _AdGenEthernetEvclCrossConnectStag1_Type()
)
adGenEthernetEvclCrossConnectStag1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectStag1.setStatus("current")
_AdGenEthernetEvclCrossConnectCtag1_Type = AdGenEthernetCtag
_AdGenEthernetEvclCrossConnectCtag1_Object = MibTableColumn
adGenEthernetEvclCrossConnectCtag1 = _AdGenEthernetEvclCrossConnectCtag1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 4),
    _AdGenEthernetEvclCrossConnectCtag1_Type()
)
adGenEthernetEvclCrossConnectCtag1.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectCtag1.setStatus("current")
_AdGenEthernetEvclCrossConnectIfIndex2_Type = InterfaceIndex
_AdGenEthernetEvclCrossConnectIfIndex2_Object = MibTableColumn
adGenEthernetEvclCrossConnectIfIndex2 = _AdGenEthernetEvclCrossConnectIfIndex2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 5),
    _AdGenEthernetEvclCrossConnectIfIndex2_Type()
)
adGenEthernetEvclCrossConnectIfIndex2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectIfIndex2.setStatus("current")
_AdGenEthernetEvclCrossConnectStag2_Type = AdGenEthernetStag
_AdGenEthernetEvclCrossConnectStag2_Object = MibTableColumn
adGenEthernetEvclCrossConnectStag2 = _AdGenEthernetEvclCrossConnectStag2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 6),
    _AdGenEthernetEvclCrossConnectStag2_Type()
)
adGenEthernetEvclCrossConnectStag2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectStag2.setStatus("current")
_AdGenEthernetEvclCrossConnectCtag2_Type = AdGenEthernetCtag
_AdGenEthernetEvclCrossConnectCtag2_Object = MibTableColumn
adGenEthernetEvclCrossConnectCtag2 = _AdGenEthernetEvclCrossConnectCtag2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 7),
    _AdGenEthernetEvclCrossConnectCtag2_Type()
)
adGenEthernetEvclCrossConnectCtag2.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectCtag2.setStatus("current")
_AdGenEthernetEvclCrossConnectName_Type = DisplayString
_AdGenEthernetEvclCrossConnectName_Object = MibTableColumn
adGenEthernetEvclCrossConnectName = _AdGenEthernetEvclCrossConnectName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 8),
    _AdGenEthernetEvclCrossConnectName_Type()
)
adGenEthernetEvclCrossConnectName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectName.setStatus("current")
_AdGenEthernetEvclCrossConnectOperStatus_Type = AdGenEthernetOperStatus
_AdGenEthernetEvclCrossConnectOperStatus_Object = MibTableColumn
adGenEthernetEvclCrossConnectOperStatus = _AdGenEthernetEvclCrossConnectOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 9),
    _AdGenEthernetEvclCrossConnectOperStatus_Type()
)
adGenEthernetEvclCrossConnectOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectOperStatus.setStatus("current")
_AdGenEthernetEvclCrossConnectLastChange_Type = AdGenEthernetLastChange
_AdGenEthernetEvclCrossConnectLastChange_Object = MibTableColumn
adGenEthernetEvclCrossConnectLastChange = _AdGenEthernetEvclCrossConnectLastChange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 10),
    _AdGenEthernetEvclCrossConnectLastChange_Type()
)
adGenEthernetEvclCrossConnectLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectLastChange.setStatus("current")
_AdGenEthernetEvclCrossConnectLastError_Type = DisplayString
_AdGenEthernetEvclCrossConnectLastError_Object = MibTableColumn
adGenEthernetEvclCrossConnectLastError = _AdGenEthernetEvclCrossConnectLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 11),
    _AdGenEthernetEvclCrossConnectLastError_Type()
)
adGenEthernetEvclCrossConnectLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectLastError.setStatus("current")


class _AdGenEthernetEvclCrossConnectRowStatus_Type(RowStatus):
    """Custom type adGenEthernetEvclCrossConnectRowStatus based on RowStatus"""
    defaultValue = 1


_AdGenEthernetEvclCrossConnectRowStatus_Type.__name__ = "RowStatus"
_AdGenEthernetEvclCrossConnectRowStatus_Object = MibTableColumn
adGenEthernetEvclCrossConnectRowStatus = _AdGenEthernetEvclCrossConnectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 22, 1, 12),
    _AdGenEthernetEvclCrossConnectRowStatus_Type()
)
adGenEthernetEvclCrossConnectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEthernetEvclCrossConnectRowStatus.setStatus("current")
_AdGenEthernetStagMembershipTable_Object = MibTable
adGenEthernetStagMembershipTable = _AdGenEthernetStagMembershipTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 23)
)
if mibBuilder.loadTexts:
    adGenEthernetStagMembershipTable.setStatus("current")
_AdGenEthernetStagMembershipEntry_Object = MibTableRow
adGenEthernetStagMembershipEntry = _AdGenEthernetStagMembershipEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 23, 1)
)
adGenEthernetStagMembershipEntry.setIndexNames(
    (0, "ADTRAN-GEN-ETHERNET-MIB", "adGenEthernetVplStag"),
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEthernetStagMembershipEntry.setStatus("current")
_AdGenEthernetStagMembershipCount_Type = Counter32
_AdGenEthernetStagMembershipCount_Object = MibTableColumn
adGenEthernetStagMembershipCount = _AdGenEthernetStagMembershipCount_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 67, 1, 15, 1, 23, 1, 1),
    _AdGenEthernetStagMembershipCount_Type()
)
adGenEthernetStagMembershipCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEthernetStagMembershipCount.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GEN-ETHERNET-MIB",
    **{"AdGenEthernetCtag": AdGenEthernetCtag,
       "AdGenEthernetCrossConnectType": AdGenEthernetCrossConnectType,
       "AdGenEthernetLastChange": AdGenEthernetLastChange,
       "AdGenEthernetOperStatus": AdGenEthernetOperStatus,
       "AdGenEthernetStag": AdGenEthernetStag,
       "adGenEthernetMIBObjects": adGenEthernetMIBObjects,
       "adGenEthernetModuleConfTable": adGenEthernetModuleConfTable,
       "adGenEthernetModuleConfEntry": adGenEthernetModuleConfEntry,
       "adGenEthernetModuleMaxEvpls": adGenEthernetModuleMaxEvpls,
       "adGenEthernetModuleMaxEvcls": adGenEthernetModuleMaxEvcls,
       "adGenEthernetModuleConfEvpls": adGenEthernetModuleConfEvpls,
       "adGenEthernetModuleConfEvcls": adGenEthernetModuleConfEvcls,
       "adGenEthernetInterfaceConfTable": adGenEthernetInterfaceConfTable,
       "adGenEthernetInterfaceConfEntry": adGenEthernetInterfaceConfEntry,
       "adGenEthernetInterfaceMaxEvpls": adGenEthernetInterfaceMaxEvpls,
       "adGenEthernetInterfaceMaxEvcls": adGenEthernetInterfaceMaxEvcls,
       "adGenEthernetInterfaceConfEvpls": adGenEthernetInterfaceConfEvpls,
       "adGenEthernetInterfaceConfEvcls": adGenEthernetInterfaceConfEvcls,
       "adGenEthernetVplStatus": adGenEthernetVplStatus,
       "adGenEthernetVplTable": adGenEthernetVplTable,
       "adGenEthernetVplEntry": adGenEthernetVplEntry,
       "adGenEthernetVplStag": adGenEthernetVplStag,
       "adGenEthernetVplName": adGenEthernetVplName,
       "adGenEthernetVplOperStatus": adGenEthernetVplOperStatus,
       "adGenEthernetVplLastChange": adGenEthernetVplLastChange,
       "adGenEthernetVplCrossConnectType": adGenEthernetVplCrossConnectType,
       "adGenEthernetVplCrossConnectIdentifier": adGenEthernetVplCrossConnectIdentifier,
       "adGenEthernetVplLastError": adGenEthernetVplLastError,
       "adGenEthernetVplRowStatus": adGenEthernetVplRowStatus,
       "adGenEthernetVclStatus": adGenEthernetVclStatus,
       "adGenEthernetVclTable": adGenEthernetVclTable,
       "adGenEthernetVclEntry": adGenEthernetVclEntry,
       "adGenEthernetVclStag": adGenEthernetVclStag,
       "adGenEthernetVclCtag": adGenEthernetVclCtag,
       "adGenEthernetVclName": adGenEthernetVclName,
       "adGenEthernetVclOperStatus": adGenEthernetVclOperStatus,
       "adGenEthernetVclLastChange": adGenEthernetVclLastChange,
       "adGenEthernetVclCrossConnectType": adGenEthernetVclCrossConnectType,
       "adGenEthernetVclCrossConnectIdentifier": adGenEthernetVclCrossConnectIdentifier,
       "adGenEthernetVclLastError": adGenEthernetVclLastError,
       "adGenEthernetVclRowStatus": adGenEthernetVclRowStatus,
       "adGenEthernetVclEvclCrossConnectNumberNext": adGenEthernetVclEvclCrossConnectNumberNext,
       "adGenEthernetVclEvclCrossConnectFailureCounter": adGenEthernetVclEvclCrossConnectFailureCounter,
       "adGenEthernetVclEvclCrossConnectStatus": adGenEthernetVclEvclCrossConnectStatus,
       "adGenEthernetVclEvclCrossConnectTable": adGenEthernetVclEvclCrossConnectTable,
       "adGenEthernetVclEvclCrossConnectEntry": adGenEthernetVclEvclCrossConnectEntry,
       "adGenEthernetVclEvclCrossConnectIndex": adGenEthernetVclEvclCrossConnectIndex,
       "adGenEthernetVclEvclCrossConnectAtmIfIndex": adGenEthernetVclEvclCrossConnectAtmIfIndex,
       "adGenEthernetVclEvclCrossConnectAtmVpi": adGenEthernetVclEvclCrossConnectAtmVpi,
       "adGenEthernetVclEvclCrossConnectAtmVci": adGenEthernetVclEvclCrossConnectAtmVci,
       "adGenEthernetVclEvclCrossConnectEthIfIndex": adGenEthernetVclEvclCrossConnectEthIfIndex,
       "adGenEthernetVclEvclCrossConnectEthStag": adGenEthernetVclEvclCrossConnectEthStag,
       "adGenEthernetVclEvclCrossConnectEthCtag": adGenEthernetVclEvclCrossConnectEthCtag,
       "adGenEthernetVclEvclCrossConnectName": adGenEthernetVclEvclCrossConnectName,
       "adGenEthernetVclEvclCrossConnectOperStatus": adGenEthernetVclEvclCrossConnectOperStatus,
       "adGenEthernetVclEvclCrossConnectLastChange": adGenEthernetVclEvclCrossConnectLastChange,
       "adGenEthernetVclEvclCrossConnectLastError": adGenEthernetVclEvclCrossConnectLastError,
       "adGenEthernetVclEvclCrossConnectRowStatus": adGenEthernetVclEvclCrossConnectRowStatus,
       "adGenEthernetVclEvclCrossConnectOption82Insert": adGenEthernetVclEvclCrossConnectOption82Insert,
       "adGenEthernetVplEvplCrossConnectNumberNext": adGenEthernetVplEvplCrossConnectNumberNext,
       "adGenEthernetVplEvplCrossConnectFailureCounter": adGenEthernetVplEvplCrossConnectFailureCounter,
       "adGenEthernetVplEvplCrossConnectStatus": adGenEthernetVplEvplCrossConnectStatus,
       "adGenEthernetVplEvplCrossConnectTable": adGenEthernetVplEvplCrossConnectTable,
       "adGenEthernetVplEvplCrossConnectEntry": adGenEthernetVplEvplCrossConnectEntry,
       "adGenEthernetVplEvplCrossConnectIndex": adGenEthernetVplEvplCrossConnectIndex,
       "adGenEthernetVplEvplCrossConnectAtmIfIndex": adGenEthernetVplEvplCrossConnectAtmIfIndex,
       "adGenEthernetVplEvplCrossConnectAtmVp": adGenEthernetVplEvplCrossConnectAtmVp,
       "adGenEthernetVplEvplCrossConnectEthIfIndex": adGenEthernetVplEvplCrossConnectEthIfIndex,
       "adGenEthernetVplEvplCrossConnectEthStag": adGenEthernetVplEvplCrossConnectEthStag,
       "adGenEthernetVplEvplCrossConnectName": adGenEthernetVplEvplCrossConnectName,
       "adGenEthernetVplEvplCrossConnectOperStatus": adGenEthernetVplEvplCrossConnectOperStatus,
       "adGenEthernetVplEvplCrossConnectLastChange": adGenEthernetVplEvplCrossConnectLastChange,
       "adGenEthernetVplEvplCrossConnectLastError": adGenEthernetVplEvplCrossConnectLastError,
       "adGenEthernetVplEvplCrossConnectRowStatus": adGenEthernetVplEvplCrossConnectRowStatus,
       "adGenEthernetVplEvplCrossConnectOption82Insert": adGenEthernetVplEvplCrossConnectOption82Insert,
       "adGenEthernetEvplCrossConnectNumberNext": adGenEthernetEvplCrossConnectNumberNext,
       "adGenEthernetEvplCrossConnectFailureCounter": adGenEthernetEvplCrossConnectFailureCounter,
       "adGenEthernetEvplCrossConnectStatus": adGenEthernetEvplCrossConnectStatus,
       "adGenEthernetEvplCrossConnectTable": adGenEthernetEvplCrossConnectTable,
       "adGenEthernetEvplCrossConnectEntry": adGenEthernetEvplCrossConnectEntry,
       "adGenEthernetEvplCrossConnectIndex": adGenEthernetEvplCrossConnectIndex,
       "adGenEthernetEvplCrossConnectIfIndex1": adGenEthernetEvplCrossConnectIfIndex1,
       "adGenEthernetEvplCrossConnectStag1": adGenEthernetEvplCrossConnectStag1,
       "adGenEthernetEvplCrossConnectIfIndex2": adGenEthernetEvplCrossConnectIfIndex2,
       "adGenEthernetEvplCrossConnectStag2": adGenEthernetEvplCrossConnectStag2,
       "adGenEthernetEvplCrossConnectName": adGenEthernetEvplCrossConnectName,
       "adGenEthernetEvplCrossConnectOperStatus": adGenEthernetEvplCrossConnectOperStatus,
       "adGenEthernetEvplCrossConnectLastChange": adGenEthernetEvplCrossConnectLastChange,
       "adGenEthernetEvplCrossConnectLastError": adGenEthernetEvplCrossConnectLastError,
       "adGenEthernetEvplCrossConnectRowStatus": adGenEthernetEvplCrossConnectRowStatus,
       "adGenEthernetEvclCrossConnectNumberNext": adGenEthernetEvclCrossConnectNumberNext,
       "adGenEthernetEvclCrossConnectFailureCounter": adGenEthernetEvclCrossConnectFailureCounter,
       "adGenEthernetEvclCrossConnectStatus": adGenEthernetEvclCrossConnectStatus,
       "adGenEthernetEvclCrossConnectTable": adGenEthernetEvclCrossConnectTable,
       "adGenEthernetEvclCrossConnectEntry": adGenEthernetEvclCrossConnectEntry,
       "adGenEthernetEvclCrossConnectIndex": adGenEthernetEvclCrossConnectIndex,
       "adGenEthernetEvclCrossConnectIfIndex1": adGenEthernetEvclCrossConnectIfIndex1,
       "adGenEthernetEvclCrossConnectStag1": adGenEthernetEvclCrossConnectStag1,
       "adGenEthernetEvclCrossConnectCtag1": adGenEthernetEvclCrossConnectCtag1,
       "adGenEthernetEvclCrossConnectIfIndex2": adGenEthernetEvclCrossConnectIfIndex2,
       "adGenEthernetEvclCrossConnectStag2": adGenEthernetEvclCrossConnectStag2,
       "adGenEthernetEvclCrossConnectCtag2": adGenEthernetEvclCrossConnectCtag2,
       "adGenEthernetEvclCrossConnectName": adGenEthernetEvclCrossConnectName,
       "adGenEthernetEvclCrossConnectOperStatus": adGenEthernetEvclCrossConnectOperStatus,
       "adGenEthernetEvclCrossConnectLastChange": adGenEthernetEvclCrossConnectLastChange,
       "adGenEthernetEvclCrossConnectLastError": adGenEthernetEvclCrossConnectLastError,
       "adGenEthernetEvclCrossConnectRowStatus": adGenEthernetEvclCrossConnectRowStatus,
       "adGenEthernetStagMembershipTable": adGenEthernetStagMembershipTable,
       "adGenEthernetStagMembershipEntry": adGenEthernetStagMembershipEntry,
       "adGenEthernetStagMembershipCount": adGenEthernetStagMembershipCount,
       "adGenEthernetMIB": adGenEthernetMIB}
)
