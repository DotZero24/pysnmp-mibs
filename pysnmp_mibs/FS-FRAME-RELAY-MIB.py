# SNMP MIB module (FS-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-FRAME-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:20 2025
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

(frCircuitDlci,
 frCircuitEntry,
 frCircuitIfIndex,
 frDlcmiEntry) = mibBuilder.importSymbols(
    "FRAME-RELAY-DTE-MIB",
    "frCircuitDlci",
    "frCircuitEntry",
    "frCircuitIfIndex",
    "frDlcmiEntry")

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

fsFrameRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50)
)
if mibBuilder.loadTexts:
    fsFrameRelayMIB.setRevisions(
        ("2000-10-13 00:00",
         "2000-05-22 00:00",
         "2000-05-16 00:00",
         "2009-05-18 00:00",
         "1999-08-21 00:00",
         "1996-08-15 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class DlciNumber(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )



class FSfrMapProtocols(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              6,
              7,
              10,
              11,
              12,
              13,
              16,
              18,
              22,
              25,
              37,
              38,
              39,
              40,
              47,
              48,
              49,
              53,
              63,
              74,
              83,
              999)
        )
    )
    namedValues = NamedValues(
        *(("arp", 1),
          ("serialArp", 6),
          ("ip", 7),
          ("xns", 10),
          ("novell", 11),
          ("apollo", 12),
          ("vines", 13),
          ("appletalk", 16),
          ("ieeeSpanning", 18),
          ("decnet", 22),
          ("clns", 25),
          ("rsrb", 37),
          ("bridge", 38),
          ("stun", 39),
          ("frArp", 40),
          ("uncompressedTcp", 47),
          ("compressedTcp", 48),
          ("llc2", 49),
          ("frSwitch", 53),
          ("dlsw", 63),
          ("nhrp", 74),
          ("compressedRtp", 83),
          ("wildcard", 999))
    )



# MIB Managed Objects in the order of their OIDs

_FsFrMIBObjects_ObjectIdentity = ObjectIdentity
fsFrMIBObjects = _FsFrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1)
)
_FsfrLmiObjs_ObjectIdentity = ObjectIdentity
fsfrLmiObjs = _FsfrLmiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1)
)
_FsfrLmiTable_Object = MibTable
fsfrLmiTable = _FsfrLmiTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsfrLmiTable.setStatus("current")
_FsfrLmiEntry_Object = MibTableRow
fsfrLmiEntry = _FsfrLmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    fsfrLmiEntry.setStatus("current")


class _FsfrLmiLinkstatus_Type(Integer32):
    """Custom type fsfrLmiLinkstatus based on Integer32"""
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


_FsfrLmiLinkstatus_Type.__name__ = "Integer32"
_FsfrLmiLinkstatus_Object = MibTableColumn
fsfrLmiLinkstatus = _FsfrLmiLinkstatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 1),
    _FsfrLmiLinkstatus_Type()
)
fsfrLmiLinkstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiLinkstatus.setStatus("current")


class _FsfrLmiLinkType_Type(Integer32):
    """Custom type fsfrLmiLinkType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dte", 1),
          ("dce", 2),
          ("nni", 3))
    )


_FsfrLmiLinkType_Type.__name__ = "Integer32"
_FsfrLmiLinkType_Object = MibTableColumn
fsfrLmiLinkType = _FsfrLmiLinkType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 2),
    _FsfrLmiLinkType_Type()
)
fsfrLmiLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiLinkType.setStatus("current")
_FsfrLmiEnquiryIns_Type = Counter32
_FsfrLmiEnquiryIns_Object = MibTableColumn
fsfrLmiEnquiryIns = _FsfrLmiEnquiryIns_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 3),
    _FsfrLmiEnquiryIns_Type()
)
fsfrLmiEnquiryIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiEnquiryIns.setStatus("current")
if mibBuilder.loadTexts:
    fsfrLmiEnquiryIns.setUnits("messages")
_FsfrLmiEnquiryOuts_Type = Counter32
_FsfrLmiEnquiryOuts_Object = MibTableColumn
fsfrLmiEnquiryOuts = _FsfrLmiEnquiryOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 4),
    _FsfrLmiEnquiryOuts_Type()
)
fsfrLmiEnquiryOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiEnquiryOuts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrLmiEnquiryOuts.setUnits("messages")
_FsfrLmiStatusIns_Type = Counter32
_FsfrLmiStatusIns_Object = MibTableColumn
fsfrLmiStatusIns = _FsfrLmiStatusIns_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 5),
    _FsfrLmiStatusIns_Type()
)
fsfrLmiStatusIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiStatusIns.setStatus("current")
if mibBuilder.loadTexts:
    fsfrLmiStatusIns.setUnits("messages")
_FsfrLmiStatusOuts_Type = Counter32
_FsfrLmiStatusOuts_Object = MibTableColumn
fsfrLmiStatusOuts = _FsfrLmiStatusOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 6),
    _FsfrLmiStatusOuts_Type()
)
fsfrLmiStatusOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiStatusOuts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrLmiStatusOuts.setUnits("messages")
_FsfrLmiUpdateStatusIns_Type = Counter32
_FsfrLmiUpdateStatusIns_Object = MibTableColumn
fsfrLmiUpdateStatusIns = _FsfrLmiUpdateStatusIns_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 7),
    _FsfrLmiUpdateStatusIns_Type()
)
fsfrLmiUpdateStatusIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiUpdateStatusIns.setStatus("current")
if mibBuilder.loadTexts:
    fsfrLmiUpdateStatusIns.setUnits("messages")
_FsfrLmiUpdateStatusOuts_Type = Counter32
_FsfrLmiUpdateStatusOuts_Object = MibTableColumn
fsfrLmiUpdateStatusOuts = _FsfrLmiUpdateStatusOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 8),
    _FsfrLmiUpdateStatusOuts_Type()
)
fsfrLmiUpdateStatusOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiUpdateStatusOuts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrLmiUpdateStatusOuts.setUnits("messages")
_FsfrLmiStatusTimeouts_Type = Counter32
_FsfrLmiStatusTimeouts_Object = MibTableColumn
fsfrLmiStatusTimeouts = _FsfrLmiStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 9),
    _FsfrLmiStatusTimeouts_Type()
)
fsfrLmiStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiStatusTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrLmiStatusTimeouts.setUnits("times")
_FsfrLmiStatusEnqTimeouts_Type = Counter32
_FsfrLmiStatusEnqTimeouts_Object = MibTableColumn
fsfrLmiStatusEnqTimeouts = _FsfrLmiStatusEnqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 10),
    _FsfrLmiStatusEnqTimeouts_Type()
)
fsfrLmiStatusEnqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiStatusEnqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrLmiStatusEnqTimeouts.setUnits("times")


class _FsfrLmiN392Dce_Type(Integer32):
    """Custom type fsfrLmiN392Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsfrLmiN392Dce_Type.__name__ = "Integer32"
_FsfrLmiN392Dce_Object = MibTableColumn
fsfrLmiN392Dce = _FsfrLmiN392Dce_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 11),
    _FsfrLmiN392Dce_Type()
)
fsfrLmiN392Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiN392Dce.setStatus("current")


class _FsfrLmiN393Dce_Type(Integer32):
    """Custom type fsfrLmiN393Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_FsfrLmiN393Dce_Type.__name__ = "Integer32"
_FsfrLmiN393Dce_Object = MibTableColumn
fsfrLmiN393Dce = _FsfrLmiN393Dce_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 12),
    _FsfrLmiN393Dce_Type()
)
fsfrLmiN393Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiN393Dce.setStatus("current")


class _FsfrLmiT392Dce_Type(Integer32):
    """Custom type fsfrLmiT392Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_FsfrLmiT392Dce_Type.__name__ = "Integer32"
_FsfrLmiT392Dce_Object = MibTableColumn
fsfrLmiT392Dce = _FsfrLmiT392Dce_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 1, 1, 1, 13),
    _FsfrLmiT392Dce_Type()
)
fsfrLmiT392Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrLmiT392Dce.setStatus("current")
if mibBuilder.loadTexts:
    fsfrLmiT392Dce.setUnits("seconds")
_FsfrCircuitObjs_ObjectIdentity = ObjectIdentity
fsfrCircuitObjs = _FsfrCircuitObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2)
)
_FsfrCircuitTable_Object = MibTable
fsfrCircuitTable = _FsfrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 1)
)
if mibBuilder.loadTexts:
    fsfrCircuitTable.setStatus("current")
_FsfrCircuitEntry_Object = MibTableRow
fsfrCircuitEntry = _FsfrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    fsfrCircuitEntry.setStatus("current")
_FsfrCircuitDEins_Type = Counter32
_FsfrCircuitDEins_Object = MibTableColumn
fsfrCircuitDEins = _FsfrCircuitDEins_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 1, 1, 1),
    _FsfrCircuitDEins_Type()
)
fsfrCircuitDEins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrCircuitDEins.setStatus("current")
if mibBuilder.loadTexts:
    fsfrCircuitDEins.setUnits("packets")
_FsfrCircuitDEouts_Type = Counter32
_FsfrCircuitDEouts_Object = MibTableColumn
fsfrCircuitDEouts = _FsfrCircuitDEouts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 1, 1, 2),
    _FsfrCircuitDEouts_Type()
)
fsfrCircuitDEouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrCircuitDEouts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrCircuitDEouts.setUnits("packets")
_FsfrCircuitDropPktsOuts_Type = Counter32
_FsfrCircuitDropPktsOuts_Object = MibTableColumn
fsfrCircuitDropPktsOuts = _FsfrCircuitDropPktsOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 1, 1, 3),
    _FsfrCircuitDropPktsOuts_Type()
)
fsfrCircuitDropPktsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrCircuitDropPktsOuts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrCircuitDropPktsOuts.setUnits("packets")


class _FsfrCircuitType_Type(Integer32):
    """Custom type fsfrCircuitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pvc", 1),
          ("svc", 2))
    )


_FsfrCircuitType_Type.__name__ = "Integer32"
_FsfrCircuitType_Object = MibTableColumn
fsfrCircuitType = _FsfrCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 1, 1, 4),
    _FsfrCircuitType_Type()
)
fsfrCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrCircuitType.setStatus("current")
_FsfrExtCircuitTable_Object = MibTable
fsfrExtCircuitTable = _FsfrExtCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2)
)
if mibBuilder.loadTexts:
    fsfrExtCircuitTable.setStatus("current")
_FsfrExtCircuitEntry_Object = MibTableRow
fsfrExtCircuitEntry = _FsfrExtCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    fsfrExtCircuitEntry.setStatus("current")
_FsfrExtCircuitIfName_Type = DisplayString
_FsfrExtCircuitIfName_Object = MibTableColumn
fsfrExtCircuitIfName = _FsfrExtCircuitIfName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 1),
    _FsfrExtCircuitIfName_Type()
)
fsfrExtCircuitIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitIfName.setStatus("current")


class _FsfrExtCircuitIfType_Type(Integer32):
    """Custom type fsfrExtCircuitIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("mainInterface", 1),
          ("pointToPoint", 2),
          ("multipoint", 3))
    )


_FsfrExtCircuitIfType_Type.__name__ = "Integer32"
_FsfrExtCircuitIfType_Object = MibTableColumn
fsfrExtCircuitIfType = _FsfrExtCircuitIfType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 2),
    _FsfrExtCircuitIfType_Type()
)
fsfrExtCircuitIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitIfType.setStatus("current")
_FsfrExtCircuitSubifIndex_Type = InterfaceIndex
_FsfrExtCircuitSubifIndex_Object = MibTableColumn
fsfrExtCircuitSubifIndex = _FsfrExtCircuitSubifIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 3),
    _FsfrExtCircuitSubifIndex_Type()
)
fsfrExtCircuitSubifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitSubifIndex.setStatus("current")


class _FsfrExtCircuitMapStatus_Type(Integer32):
    """Custom type fsfrExtCircuitMapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_FsfrExtCircuitMapStatus_Type.__name__ = "Integer32"
_FsfrExtCircuitMapStatus_Object = MibTableColumn
fsfrExtCircuitMapStatus = _FsfrExtCircuitMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 4),
    _FsfrExtCircuitMapStatus_Type()
)
fsfrExtCircuitMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitMapStatus.setStatus("current")


class _FsfrExtCircuitCreateType_Type(Integer32):
    """Custom type fsfrExtCircuitCreateType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_FsfrExtCircuitCreateType_Type.__name__ = "Integer32"
_FsfrExtCircuitCreateType_Object = MibTableColumn
fsfrExtCircuitCreateType = _FsfrExtCircuitCreateType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 5),
    _FsfrExtCircuitCreateType_Type()
)
fsfrExtCircuitCreateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitCreateType.setStatus("current")
_FsfrExtCircuitMulticast_Type = TruthValue
_FsfrExtCircuitMulticast_Object = MibTableColumn
fsfrExtCircuitMulticast = _FsfrExtCircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 6),
    _FsfrExtCircuitMulticast_Type()
)
fsfrExtCircuitMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitMulticast.setStatus("current")
_FsfrExtCircuitRoutedDlci_Type = DlciNumber
_FsfrExtCircuitRoutedDlci_Object = MibTableColumn
fsfrExtCircuitRoutedDlci = _FsfrExtCircuitRoutedDlci_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 7),
    _FsfrExtCircuitRoutedDlci_Type()
)
fsfrExtCircuitRoutedDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitRoutedDlci.setStatus("current")
_FsfrExtCircuitRoutedIf_Type = InterfaceIndex
_FsfrExtCircuitRoutedIf_Object = MibTableColumn
fsfrExtCircuitRoutedIf = _FsfrExtCircuitRoutedIf_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 8),
    _FsfrExtCircuitRoutedIf_Type()
)
fsfrExtCircuitRoutedIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitRoutedIf.setStatus("current")
_FsfrExtCircuitUncompressIns_Type = Counter32
_FsfrExtCircuitUncompressIns_Object = MibTableColumn
fsfrExtCircuitUncompressIns = _FsfrExtCircuitUncompressIns_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 9),
    _FsfrExtCircuitUncompressIns_Type()
)
fsfrExtCircuitUncompressIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitUncompressIns.setStatus("current")
if mibBuilder.loadTexts:
    fsfrExtCircuitUncompressIns.setUnits("octets")
_FsfrExtCircuitUncompressOuts_Type = Counter32
_FsfrExtCircuitUncompressOuts_Object = MibTableColumn
fsfrExtCircuitUncompressOuts = _FsfrExtCircuitUncompressOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 10),
    _FsfrExtCircuitUncompressOuts_Type()
)
fsfrExtCircuitUncompressOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitUncompressOuts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrExtCircuitUncompressOuts.setUnits("octets")
_FsfrExtCircuitFECNOuts_Type = Counter32
_FsfrExtCircuitFECNOuts_Object = MibTableColumn
fsfrExtCircuitFECNOuts = _FsfrExtCircuitFECNOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 11),
    _FsfrExtCircuitFECNOuts_Type()
)
fsfrExtCircuitFECNOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitFECNOuts.setStatus("current")
_FsfrExtCircuitBECNOuts_Type = Counter32
_FsfrExtCircuitBECNOuts_Object = MibTableColumn
fsfrExtCircuitBECNOuts = _FsfrExtCircuitBECNOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 12),
    _FsfrExtCircuitBECNOuts_Type()
)
fsfrExtCircuitBECNOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitBECNOuts.setStatus("current")


class _FsfrExtCircuitMinThruputOut_Type(Integer32):
    """Custom type fsfrExtCircuitMinThruputOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_FsfrExtCircuitMinThruputOut_Type.__name__ = "Integer32"
_FsfrExtCircuitMinThruputOut_Object = MibTableColumn
fsfrExtCircuitMinThruputOut = _FsfrExtCircuitMinThruputOut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 13),
    _FsfrExtCircuitMinThruputOut_Type()
)
fsfrExtCircuitMinThruputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitMinThruputOut.setStatus("current")
if mibBuilder.loadTexts:
    fsfrExtCircuitMinThruputOut.setUnits("bits per second")


class _FsfrExtCircuitMinThruputIn_Type(Integer32):
    """Custom type fsfrExtCircuitMinThruputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_FsfrExtCircuitMinThruputIn_Type.__name__ = "Integer32"
_FsfrExtCircuitMinThruputIn_Object = MibTableColumn
fsfrExtCircuitMinThruputIn = _FsfrExtCircuitMinThruputIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 14),
    _FsfrExtCircuitMinThruputIn_Type()
)
fsfrExtCircuitMinThruputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitMinThruputIn.setStatus("current")
if mibBuilder.loadTexts:
    fsfrExtCircuitMinThruputIn.setUnits("bits per second")
_FsfrExtCircuitBcastPktOuts_Type = Counter32
_FsfrExtCircuitBcastPktOuts_Object = MibTableColumn
fsfrExtCircuitBcastPktOuts = _FsfrExtCircuitBcastPktOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 15),
    _FsfrExtCircuitBcastPktOuts_Type()
)
fsfrExtCircuitBcastPktOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitBcastPktOuts.setStatus("current")
_FsfrExtCircuitBcastByteOuts_Type = Counter32
_FsfrExtCircuitBcastByteOuts_Object = MibTableColumn
fsfrExtCircuitBcastByteOuts = _FsfrExtCircuitBcastByteOuts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 16),
    _FsfrExtCircuitBcastByteOuts_Type()
)
fsfrExtCircuitBcastByteOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitBcastByteOuts.setStatus("current")


class _FsfrExtCircuitBandwidth_Type(Integer32):
    """Custom type fsfrExtCircuitBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_FsfrExtCircuitBandwidth_Type.__name__ = "Integer32"
_FsfrExtCircuitBandwidth_Object = MibTableColumn
fsfrExtCircuitBandwidth = _FsfrExtCircuitBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 17),
    _FsfrExtCircuitBandwidth_Type()
)
fsfrExtCircuitBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    fsfrExtCircuitBandwidth.setUnits("bits per second")


class _FsfrExtCircuitShapeByteLimit_Type(Integer32):
    """Custom type fsfrExtCircuitShapeByteLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 2147483647),
    )


_FsfrExtCircuitShapeByteLimit_Type.__name__ = "Integer32"
_FsfrExtCircuitShapeByteLimit_Object = MibTableColumn
fsfrExtCircuitShapeByteLimit = _FsfrExtCircuitShapeByteLimit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 18),
    _FsfrExtCircuitShapeByteLimit_Type()
)
fsfrExtCircuitShapeByteLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeByteLimit.setStatus("current")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeByteLimit.setUnits("octets")


class _FsfrExtCircuitShapeInterval_Type(Integer32):
    """Custom type fsfrExtCircuitShapeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 125),
    )


_FsfrExtCircuitShapeInterval_Type.__name__ = "Integer32"
_FsfrExtCircuitShapeInterval_Object = MibTableColumn
fsfrExtCircuitShapeInterval = _FsfrExtCircuitShapeInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 19),
    _FsfrExtCircuitShapeInterval_Type()
)
fsfrExtCircuitShapeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeInterval.setStatus("current")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeInterval.setUnits("milliseconds")


class _FsfrExtCircuitShapeByteIncrement_Type(Integer32):
    """Custom type fsfrExtCircuitShapeByteIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 2147483647),
    )


_FsfrExtCircuitShapeByteIncrement_Type.__name__ = "Integer32"
_FsfrExtCircuitShapeByteIncrement_Object = MibTableColumn
fsfrExtCircuitShapeByteIncrement = _FsfrExtCircuitShapeByteIncrement_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 20),
    _FsfrExtCircuitShapeByteIncrement_Type()
)
fsfrExtCircuitShapeByteIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeByteIncrement.setStatus("current")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeByteIncrement.setUnits("octets")
_FsfrExtCircuitShapePkts_Type = Counter32
_FsfrExtCircuitShapePkts_Object = MibTableColumn
fsfrExtCircuitShapePkts = _FsfrExtCircuitShapePkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 21),
    _FsfrExtCircuitShapePkts_Type()
)
fsfrExtCircuitShapePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapePkts.setStatus("current")
_FsfrExtCircuitShapeBytes_Type = Counter32
_FsfrExtCircuitShapeBytes_Object = MibTableColumn
fsfrExtCircuitShapeBytes = _FsfrExtCircuitShapeBytes_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 22),
    _FsfrExtCircuitShapeBytes_Type()
)
fsfrExtCircuitShapeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeBytes.setStatus("current")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeBytes.setUnits("octets")
_FsfrExtCircuitShapePktsDelay_Type = Counter32
_FsfrExtCircuitShapePktsDelay_Object = MibTableColumn
fsfrExtCircuitShapePktsDelay = _FsfrExtCircuitShapePktsDelay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 23),
    _FsfrExtCircuitShapePktsDelay_Type()
)
fsfrExtCircuitShapePktsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapePktsDelay.setStatus("current")
_FsfrExtCircuitShapeBytesDelay_Type = Counter32
_FsfrExtCircuitShapeBytesDelay_Object = MibTableColumn
fsfrExtCircuitShapeBytesDelay = _FsfrExtCircuitShapeBytesDelay_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 24),
    _FsfrExtCircuitShapeBytesDelay_Type()
)
fsfrExtCircuitShapeBytesDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeBytesDelay.setStatus("current")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeBytesDelay.setUnits("octets")
_FsfrExtCircuitShapeActive_Type = TruthValue
_FsfrExtCircuitShapeActive_Object = MibTableColumn
fsfrExtCircuitShapeActive = _FsfrExtCircuitShapeActive_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 25),
    _FsfrExtCircuitShapeActive_Type()
)
fsfrExtCircuitShapeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeActive.setStatus("current")


class _FsfrExtCircuitShapeAdapting_Type(Integer32):
    """Custom type fsfrExtCircuitShapeAdapting based on Integer32"""
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
          ("becn", 2),
          ("foreSight", 3))
    )


_FsfrExtCircuitShapeAdapting_Type.__name__ = "Integer32"
_FsfrExtCircuitShapeAdapting_Object = MibTableColumn
fsfrExtCircuitShapeAdapting = _FsfrExtCircuitShapeAdapting_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 26),
    _FsfrExtCircuitShapeAdapting_Type()
)
fsfrExtCircuitShapeAdapting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitShapeAdapting.setStatus("current")


class _FsfrExtCircuitTxDataRate_Type(Integer32):
    """Custom type fsfrExtCircuitTxDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_FsfrExtCircuitTxDataRate_Type.__name__ = "Integer32"
_FsfrExtCircuitTxDataRate_Object = MibTableColumn
fsfrExtCircuitTxDataRate = _FsfrExtCircuitTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 27),
    _FsfrExtCircuitTxDataRate_Type()
)
fsfrExtCircuitTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitTxDataRate.setStatus("current")


class _FsfrExtCircuitTxPktRate_Type(Integer32):
    """Custom type fsfrExtCircuitTxPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_FsfrExtCircuitTxPktRate_Type.__name__ = "Integer32"
_FsfrExtCircuitTxPktRate_Object = MibTableColumn
fsfrExtCircuitTxPktRate = _FsfrExtCircuitTxPktRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 28),
    _FsfrExtCircuitTxPktRate_Type()
)
fsfrExtCircuitTxPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitTxPktRate.setStatus("current")


class _FsfrExtCircuitRcvDataRate_Type(Integer32):
    """Custom type fsfrExtCircuitRcvDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_FsfrExtCircuitRcvDataRate_Type.__name__ = "Integer32"
_FsfrExtCircuitRcvDataRate_Object = MibTableColumn
fsfrExtCircuitRcvDataRate = _FsfrExtCircuitRcvDataRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 29),
    _FsfrExtCircuitRcvDataRate_Type()
)
fsfrExtCircuitRcvDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitRcvDataRate.setStatus("current")


class _FsfrExtCircuitRcvPktRate_Type(Integer32):
    """Custom type fsfrExtCircuitRcvPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_FsfrExtCircuitRcvPktRate_Type.__name__ = "Integer32"
_FsfrExtCircuitRcvPktRate_Object = MibTableColumn
fsfrExtCircuitRcvPktRate = _FsfrExtCircuitRcvPktRate_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 2, 2, 1, 30),
    _FsfrExtCircuitRcvPktRate_Type()
)
fsfrExtCircuitRcvPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrExtCircuitRcvPktRate.setStatus("current")
_FsfrMapObjs_ObjectIdentity = ObjectIdentity
fsfrMapObjs = _FsfrMapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3)
)
_FsfrMapTable_Object = MibTable
fsfrMapTable = _FsfrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1)
)
if mibBuilder.loadTexts:
    fsfrMapTable.setStatus("current")
_FsfrMapEntry_Object = MibTableRow
fsfrMapEntry = _FsfrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1)
)
fsfrMapEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
    (0, "FS-FRAME-RELAY-MIB", "fsfrMapIndex"),
)
if mibBuilder.loadTexts:
    fsfrMapEntry.setStatus("current")


class _FsfrMapIndex_Type(Integer32):
    """Custom type fsfrMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_FsfrMapIndex_Type.__name__ = "Integer32"
_FsfrMapIndex_Object = MibTableColumn
fsfrMapIndex = _FsfrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1, 1),
    _FsfrMapIndex_Type()
)
fsfrMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrMapIndex.setStatus("current")
_FsfrMapProtocol_Type = FSfrMapProtocols
_FsfrMapProtocol_Object = MibTableColumn
fsfrMapProtocol = _FsfrMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1, 2),
    _FsfrMapProtocol_Type()
)
fsfrMapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrMapProtocol.setStatus("current")


class _FsfrMapAddress_Type(OctetString):
    """Custom type fsfrMapAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsfrMapAddress_Type.__name__ = "OctetString"
_FsfrMapAddress_Object = MibTableColumn
fsfrMapAddress = _FsfrMapAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1, 3),
    _FsfrMapAddress_Type()
)
fsfrMapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrMapAddress.setStatus("current")


class _FsfrMapType_Type(Integer32):
    """Custom type fsfrMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dynamic", 2),
          ("svc", 3))
    )


_FsfrMapType_Type.__name__ = "Integer32"
_FsfrMapType_Object = MibTableColumn
fsfrMapType = _FsfrMapType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1, 4),
    _FsfrMapType_Type()
)
fsfrMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrMapType.setStatus("current")


class _FsfrMapEncaps_Type(Integer32):
    """Custom type fsfrMapEncaps based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ietf", 1),
          ("cisco", 2))
    )


_FsfrMapEncaps_Type.__name__ = "Integer32"
_FsfrMapEncaps_Object = MibTableColumn
fsfrMapEncaps = _FsfrMapEncaps_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1, 5),
    _FsfrMapEncaps_Type()
)
fsfrMapEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrMapEncaps.setStatus("current")
_FsfrMapBroadcast_Type = TruthValue
_FsfrMapBroadcast_Object = MibTableColumn
fsfrMapBroadcast = _FsfrMapBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1, 6),
    _FsfrMapBroadcast_Type()
)
fsfrMapBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrMapBroadcast.setStatus("current")
_FsfrMapPayloadCompress_Type = TruthValue
_FsfrMapPayloadCompress_Object = MibTableColumn
fsfrMapPayloadCompress = _FsfrMapPayloadCompress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1, 7),
    _FsfrMapPayloadCompress_Type()
)
fsfrMapPayloadCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrMapPayloadCompress.setStatus("deprecated")


class _FsfrMapTcpHdrCompress_Type(Integer32):
    """Custom type fsfrMapTcpHdrCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inapplicable", 1),
          ("passive", 2),
          ("active", 3))
    )


_FsfrMapTcpHdrCompress_Type.__name__ = "Integer32"
_FsfrMapTcpHdrCompress_Object = MibTableColumn
fsfrMapTcpHdrCompress = _FsfrMapTcpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1, 8),
    _FsfrMapTcpHdrCompress_Type()
)
fsfrMapTcpHdrCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrMapTcpHdrCompress.setStatus("current")


class _FsfrMapRtpHdrCompress_Type(Integer32):
    """Custom type fsfrMapRtpHdrCompress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("inapplicable", 1),
          ("passive", 2),
          ("active", 3))
    )


_FsfrMapRtpHdrCompress_Type.__name__ = "Integer32"
_FsfrMapRtpHdrCompress_Object = MibTableColumn
fsfrMapRtpHdrCompress = _FsfrMapRtpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1, 9),
    _FsfrMapRtpHdrCompress_Type()
)
fsfrMapRtpHdrCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrMapRtpHdrCompress.setStatus("current")


class _FsfrMapPayloadCompressType_Type(Integer32):
    """Custom type fsfrMapPayloadCompressType based on Integer32"""
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
        *(("inapplicable", 1),
          ("cisco", 2),
          ("frf9Software", 3),
          ("frf9Hardware", 4))
    )


_FsfrMapPayloadCompressType_Type.__name__ = "Integer32"
_FsfrMapPayloadCompressType_Object = MibTableColumn
fsfrMapPayloadCompressType = _FsfrMapPayloadCompressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 3, 1, 1, 10),
    _FsfrMapPayloadCompressType_Type()
)
fsfrMapPayloadCompressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrMapPayloadCompressType.setStatus("current")
_FsfrSvcObjs_ObjectIdentity = ObjectIdentity
fsfrSvcObjs = _FsfrSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4)
)
_FsfrSvcTable_Object = MibTable
fsfrSvcTable = _FsfrSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4, 1)
)
if mibBuilder.loadTexts:
    fsfrSvcTable.setStatus("current")
_FsfrSvcEntry_Object = MibTableRow
fsfrSvcEntry = _FsfrSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4, 1, 1)
)
fsfrSvcEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    fsfrSvcEntry.setStatus("current")


class _FsfrSvcAddrLocal_Type(OctetString):
    """Custom type fsfrSvcAddrLocal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsfrSvcAddrLocal_Type.__name__ = "OctetString"
_FsfrSvcAddrLocal_Object = MibTableColumn
fsfrSvcAddrLocal = _FsfrSvcAddrLocal_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4, 1, 1, 1),
    _FsfrSvcAddrLocal_Type()
)
fsfrSvcAddrLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrSvcAddrLocal.setStatus("current")


class _FsfrSvcAddrRemote_Type(OctetString):
    """Custom type fsfrSvcAddrRemote based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_FsfrSvcAddrRemote_Type.__name__ = "OctetString"
_FsfrSvcAddrRemote_Object = MibTableColumn
fsfrSvcAddrRemote = _FsfrSvcAddrRemote_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4, 1, 1, 2),
    _FsfrSvcAddrRemote_Type()
)
fsfrSvcAddrRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrSvcAddrRemote.setStatus("current")


class _FsfrSvcThroughputIn_Type(Integer32):
    """Custom type fsfrSvcThroughputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_FsfrSvcThroughputIn_Type.__name__ = "Integer32"
_FsfrSvcThroughputIn_Object = MibTableColumn
fsfrSvcThroughputIn = _FsfrSvcThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4, 1, 1, 3),
    _FsfrSvcThroughputIn_Type()
)
fsfrSvcThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrSvcThroughputIn.setStatus("current")
if mibBuilder.loadTexts:
    fsfrSvcThroughputIn.setUnits("bits per second")


class _FsfrSvcMinThruputOut_Type(Integer32):
    """Custom type fsfrSvcMinThruputOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_FsfrSvcMinThruputOut_Type.__name__ = "Integer32"
_FsfrSvcMinThruputOut_Object = MibTableColumn
fsfrSvcMinThruputOut = _FsfrSvcMinThruputOut_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4, 1, 1, 4),
    _FsfrSvcMinThruputOut_Type()
)
fsfrSvcMinThruputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrSvcMinThruputOut.setStatus("deprecated")
if mibBuilder.loadTexts:
    fsfrSvcMinThruputOut.setUnits("bits per second")


class _FsfrSvcMinThruputIn_Type(Integer32):
    """Custom type fsfrSvcMinThruputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_FsfrSvcMinThruputIn_Type.__name__ = "Integer32"
_FsfrSvcMinThruputIn_Object = MibTableColumn
fsfrSvcMinThruputIn = _FsfrSvcMinThruputIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4, 1, 1, 5),
    _FsfrSvcMinThruputIn_Type()
)
fsfrSvcMinThruputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrSvcMinThruputIn.setStatus("deprecated")
if mibBuilder.loadTexts:
    fsfrSvcMinThruputIn.setUnits("bits per second")


class _FsfrSvcCommitBurstIn_Type(Integer32):
    """Custom type fsfrSvcCommitBurstIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_FsfrSvcCommitBurstIn_Type.__name__ = "Integer32"
_FsfrSvcCommitBurstIn_Object = MibTableColumn
fsfrSvcCommitBurstIn = _FsfrSvcCommitBurstIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4, 1, 1, 6),
    _FsfrSvcCommitBurstIn_Type()
)
fsfrSvcCommitBurstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrSvcCommitBurstIn.setStatus("current")


class _FsfrSvcExcessBurstIn_Type(Integer32):
    """Custom type fsfrSvcExcessBurstIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 2440000),
    )


_FsfrSvcExcessBurstIn_Type.__name__ = "Integer32"
_FsfrSvcExcessBurstIn_Object = MibTableColumn
fsfrSvcExcessBurstIn = _FsfrSvcExcessBurstIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4, 1, 1, 7),
    _FsfrSvcExcessBurstIn_Type()
)
fsfrSvcExcessBurstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrSvcExcessBurstIn.setStatus("current")
_FsfrSvcIdleTime_Type = Integer32
_FsfrSvcIdleTime_Object = MibTableColumn
fsfrSvcIdleTime = _FsfrSvcIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 4, 1, 1, 8),
    _FsfrSvcIdleTime_Type()
)
fsfrSvcIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrSvcIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    fsfrSvcIdleTime.setUnits("seconds")
_FsfrElmiObjs_ObjectIdentity = ObjectIdentity
fsfrElmiObjs = _FsfrElmiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5)
)
_FsfrElmiIpAddr_Type = IpAddress
_FsfrElmiIpAddr_Object = MibScalar
fsfrElmiIpAddr = _FsfrElmiIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 1),
    _FsfrElmiIpAddr_Type()
)
fsfrElmiIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrElmiIpAddr.setStatus("current")
_FsfrElmiTable_Object = MibTable
fsfrElmiTable = _FsfrElmiTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 2)
)
if mibBuilder.loadTexts:
    fsfrElmiTable.setStatus("current")
_FsfrElmiEntry_Object = MibTableRow
fsfrElmiEntry = _FsfrElmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 2, 1)
)
fsfrElmiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsfrElmiEntry.setStatus("current")


class _FsfrElmiLinkStatus_Type(Integer32):
    """Custom type fsfrElmiLinkStatus based on Integer32"""
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


_FsfrElmiLinkStatus_Type.__name__ = "Integer32"
_FsfrElmiLinkStatus_Object = MibTableColumn
fsfrElmiLinkStatus = _FsfrElmiLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 2, 1, 1),
    _FsfrElmiLinkStatus_Type()
)
fsfrElmiLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrElmiLinkStatus.setStatus("current")


class _FsfrElmiArStatus_Type(Integer32):
    """Custom type fsfrElmiArStatus based on Integer32"""
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


_FsfrElmiArStatus_Type.__name__ = "Integer32"
_FsfrElmiArStatus_Object = MibTableColumn
fsfrElmiArStatus = _FsfrElmiArStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 2, 1, 2),
    _FsfrElmiArStatus_Type()
)
fsfrElmiArStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrElmiArStatus.setStatus("current")


class _FsfrElmiRemoteStatus_Type(Integer32):
    """Custom type fsfrElmiRemoteStatus based on Integer32"""
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


_FsfrElmiRemoteStatus_Type.__name__ = "Integer32"
_FsfrElmiRemoteStatus_Object = MibTableColumn
fsfrElmiRemoteStatus = _FsfrElmiRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 2, 1, 3),
    _FsfrElmiRemoteStatus_Type()
)
fsfrElmiRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrElmiRemoteStatus.setStatus("current")
_FsfrElmiNeighborTable_Object = MibTable
fsfrElmiNeighborTable = _FsfrElmiNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 3)
)
if mibBuilder.loadTexts:
    fsfrElmiNeighborTable.setStatus("current")
_FsfrElmiNeighborEntry_Object = MibTableRow
fsfrElmiNeighborEntry = _FsfrElmiNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 3, 1)
)
fsfrElmiNeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fsfrElmiNeighborEntry.setStatus("current")


class _FsfrElmiNeighborArStatus_Type(Integer32):
    """Custom type fsfrElmiNeighborArStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("notsupported", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_FsfrElmiNeighborArStatus_Type.__name__ = "Integer32"
_FsfrElmiNeighborArStatus_Object = MibTableColumn
fsfrElmiNeighborArStatus = _FsfrElmiNeighborArStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 3, 1, 1),
    _FsfrElmiNeighborArStatus_Type()
)
fsfrElmiNeighborArStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrElmiNeighborArStatus.setStatus("current")
_FsfrElmiNeighborIpAddress_Type = IpAddress
_FsfrElmiNeighborIpAddress_Object = MibTableColumn
fsfrElmiNeighborIpAddress = _FsfrElmiNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 3, 1, 2),
    _FsfrElmiNeighborIpAddress_Type()
)
fsfrElmiNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrElmiNeighborIpAddress.setStatus("current")
_FsfrElmiNeighborIfIndex_Type = InterfaceIndex
_FsfrElmiNeighborIfIndex_Object = MibTableColumn
fsfrElmiNeighborIfIndex = _FsfrElmiNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 3, 1, 3),
    _FsfrElmiNeighborIfIndex_Type()
)
fsfrElmiNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrElmiNeighborIfIndex.setStatus("current")
_FsfrElmiNeighborVendorName_Type = DisplayString
_FsfrElmiNeighborVendorName_Object = MibTableColumn
fsfrElmiNeighborVendorName = _FsfrElmiNeighborVendorName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 3, 1, 4),
    _FsfrElmiNeighborVendorName_Type()
)
fsfrElmiNeighborVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrElmiNeighborVendorName.setStatus("current")
_FsfrElmiNeighborPlatformName_Type = DisplayString
_FsfrElmiNeighborPlatformName_Object = MibTableColumn
fsfrElmiNeighborPlatformName = _FsfrElmiNeighborPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 3, 1, 5),
    _FsfrElmiNeighborPlatformName_Type()
)
fsfrElmiNeighborPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrElmiNeighborPlatformName.setStatus("current")
_FsfrElmiNeighborDeviceName_Type = DisplayString
_FsfrElmiNeighborDeviceName_Object = MibTableColumn
fsfrElmiNeighborDeviceName = _FsfrElmiNeighborDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 5, 3, 1, 6),
    _FsfrElmiNeighborDeviceName_Type()
)
fsfrElmiNeighborDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrElmiNeighborDeviceName.setStatus("current")
_FsfrFragObjs_ObjectIdentity = ObjectIdentity
fsfrFragObjs = _FsfrFragObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6)
)
_FsfrFragTable_Object = MibTable
fsfrFragTable = _FsfrFragTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1)
)
if mibBuilder.loadTexts:
    fsfrFragTable.setStatus("current")
_FsfrFragEntry_Object = MibTableRow
fsfrFragEntry = _FsfrFragEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1)
)
fsfrFragEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    fsfrFragEntry.setStatus("current")


class _FsfrFragSize_Type(Integer32):
    """Custom type fsfrFragSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1600),
    )


_FsfrFragSize_Type.__name__ = "Integer32"
_FsfrFragSize_Object = MibTableColumn
fsfrFragSize = _FsfrFragSize_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 1),
    _FsfrFragSize_Type()
)
fsfrFragSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragSize.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragSize.setUnits("octets")
_FsfrFragType_Type = DisplayString
_FsfrFragType_Object = MibTableColumn
fsfrFragType = _FsfrFragType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 2),
    _FsfrFragType_Type()
)
fsfrFragType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragType.setStatus("current")
_FsfrFragInPkts_Type = Counter32
_FsfrFragInPkts_Object = MibTableColumn
fsfrFragInPkts = _FsfrFragInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 3),
    _FsfrFragInPkts_Type()
)
fsfrFragInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragInPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragInPkts.setUnits("packets")
_FsfrFragOutPkts_Type = Counter32
_FsfrFragOutPkts_Object = MibTableColumn
fsfrFragOutPkts = _FsfrFragOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 4),
    _FsfrFragOutPkts_Type()
)
fsfrFragOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragOutPkts.setUnits("packets")
_FsfrFragInOctets_Type = Counter32
_FsfrFragInOctets_Object = MibTableColumn
fsfrFragInOctets = _FsfrFragInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 5),
    _FsfrFragInOctets_Type()
)
fsfrFragInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragInOctets.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragInOctets.setUnits("octets")
_FsfrFragOutOctets_Type = Counter32
_FsfrFragOutOctets_Object = MibTableColumn
fsfrFragOutOctets = _FsfrFragOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 6),
    _FsfrFragOutOctets_Type()
)
fsfrFragOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragOutOctets.setUnits("octets")
_FsfrFragNotInPkts_Type = Counter32
_FsfrFragNotInPkts_Object = MibTableColumn
fsfrFragNotInPkts = _FsfrFragNotInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 7),
    _FsfrFragNotInPkts_Type()
)
fsfrFragNotInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragNotInPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragNotInPkts.setUnits("packets")
_FsfrFragNotOutPkts_Type = Counter32
_FsfrFragNotOutPkts_Object = MibTableColumn
fsfrFragNotOutPkts = _FsfrFragNotOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 8),
    _FsfrFragNotOutPkts_Type()
)
fsfrFragNotOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragNotOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragNotOutPkts.setUnits("packets")
_FsfrFragNotInOctets_Type = Counter32
_FsfrFragNotInOctets_Object = MibTableColumn
fsfrFragNotInOctets = _FsfrFragNotInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 9),
    _FsfrFragNotInOctets_Type()
)
fsfrFragNotInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragNotInOctets.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragNotInOctets.setUnits("octets")
_FsfrFragNotOutOctets_Type = Counter32
_FsfrFragNotOutOctets_Object = MibTableColumn
fsfrFragNotOutOctets = _FsfrFragNotOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 10),
    _FsfrFragNotOutOctets_Type()
)
fsfrFragNotOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragNotOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragNotOutOctets.setUnits("octets")
_FsfrFragAssembledInPkts_Type = Counter32
_FsfrFragAssembledInPkts_Object = MibTableColumn
fsfrFragAssembledInPkts = _FsfrFragAssembledInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 11),
    _FsfrFragAssembledInPkts_Type()
)
fsfrFragAssembledInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragAssembledInPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragAssembledInPkts.setUnits("packets")
_FsfrFragAssembledInOctets_Type = Counter32
_FsfrFragAssembledInOctets_Object = MibTableColumn
fsfrFragAssembledInOctets = _FsfrFragAssembledInOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 12),
    _FsfrFragAssembledInOctets_Type()
)
fsfrFragAssembledInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragAssembledInOctets.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragAssembledInOctets.setUnits("octets")
_FsfrFragPreOutPkts_Type = Counter32
_FsfrFragPreOutPkts_Object = MibTableColumn
fsfrFragPreOutPkts = _FsfrFragPreOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 13),
    _FsfrFragPreOutPkts_Type()
)
fsfrFragPreOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragPreOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragPreOutPkts.setUnits("packets")
_FsfrFragPreOutOctets_Type = Counter32
_FsfrFragPreOutOctets_Object = MibTableColumn
fsfrFragPreOutOctets = _FsfrFragPreOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 14),
    _FsfrFragPreOutOctets_Type()
)
fsfrFragPreOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragPreOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragPreOutOctets.setUnits("octets")
_FsfrFragDroppedReAssembledInPkts_Type = Counter32
_FsfrFragDroppedReAssembledInPkts_Object = MibTableColumn
fsfrFragDroppedReAssembledInPkts = _FsfrFragDroppedReAssembledInPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 15),
    _FsfrFragDroppedReAssembledInPkts_Type()
)
fsfrFragDroppedReAssembledInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragDroppedReAssembledInPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragDroppedReAssembledInPkts.setUnits("packets")
_FsfrFragDroppedFragmentedOutPkts_Type = Counter32
_FsfrFragDroppedFragmentedOutPkts_Object = MibTableColumn
fsfrFragDroppedFragmentedOutPkts = _FsfrFragDroppedFragmentedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 16),
    _FsfrFragDroppedFragmentedOutPkts_Type()
)
fsfrFragDroppedFragmentedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragDroppedFragmentedOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragDroppedFragmentedOutPkts.setUnits("packets")


class _FsfrFragTimeoutsIn_Type(Integer32):
    """Custom type fsfrFragTimeoutsIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_FsfrFragTimeoutsIn_Type.__name__ = "Integer32"
_FsfrFragTimeoutsIn_Object = MibTableColumn
fsfrFragTimeoutsIn = _FsfrFragTimeoutsIn_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 17),
    _FsfrFragTimeoutsIn_Type()
)
fsfrFragTimeoutsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragTimeoutsIn.setStatus("current")
_FsfrFragOutOfSeqFragPkts_Type = Counter32
_FsfrFragOutOfSeqFragPkts_Object = MibTableColumn
fsfrFragOutOfSeqFragPkts = _FsfrFragOutOfSeqFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 18),
    _FsfrFragOutOfSeqFragPkts_Type()
)
fsfrFragOutOfSeqFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragOutOfSeqFragPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragOutOfSeqFragPkts.setUnits("packets")
_FsfrFragUnexpectedBBitSetPkts_Type = Counter32
_FsfrFragUnexpectedBBitSetPkts_Object = MibTableColumn
fsfrFragUnexpectedBBitSetPkts = _FsfrFragUnexpectedBBitSetPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 19),
    _FsfrFragUnexpectedBBitSetPkts_Type()
)
fsfrFragUnexpectedBBitSetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragUnexpectedBBitSetPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragUnexpectedBBitSetPkts.setUnits("packets")
_FsfrFragSeqMissedPkts_Type = Counter32
_FsfrFragSeqMissedPkts_Object = MibTableColumn
fsfrFragSeqMissedPkts = _FsfrFragSeqMissedPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 20),
    _FsfrFragSeqMissedPkts_Type()
)
fsfrFragSeqMissedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragSeqMissedPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragSeqMissedPkts.setUnits("packets")
_FsfrFragInterleavedOutPkts_Type = Counter32
_FsfrFragInterleavedOutPkts_Object = MibTableColumn
fsfrFragInterleavedOutPkts = _FsfrFragInterleavedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 6, 1, 1, 21),
    _FsfrFragInterleavedOutPkts_Type()
)
fsfrFragInterleavedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrFragInterleavedOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    fsfrFragInterleavedOutPkts.setUnits("packets")
_FsfrConnectionObjs_ObjectIdentity = ObjectIdentity
fsfrConnectionObjs = _FsfrConnectionObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7)
)
_FsfrConnectionTable_Object = MibTable
fsfrConnectionTable = _FsfrConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1)
)
if mibBuilder.loadTexts:
    fsfrConnectionTable.setStatus("current")
_FsfrConnectionEntry_Object = MibTableRow
fsfrConnectionEntry = _FsfrConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1)
)
fsfrConnectionEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    fsfrConnectionEntry.setStatus("current")
_FsfrConnName_Type = DisplayString
_FsfrConnName_Object = MibTableColumn
fsfrConnName = _FsfrConnName_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 1),
    _FsfrConnName_Type()
)
fsfrConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnName.setStatus("current")


class _FsfrConnID_Type(Integer32):
    """Custom type fsfrConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_FsfrConnID_Type.__name__ = "Integer32"
_FsfrConnID_Object = MibTableColumn
fsfrConnID = _FsfrConnID_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 2),
    _FsfrConnID_Type()
)
fsfrConnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnID.setStatus("current")
_FsfrConnState_Type = DisplayString
_FsfrConnState_Object = MibTableColumn
fsfrConnState = _FsfrConnState_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 3),
    _FsfrConnState_Type()
)
fsfrConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnState.setStatus("current")
_FsfrConnSegment1Name_Type = DisplayString
_FsfrConnSegment1Name_Object = MibTableColumn
fsfrConnSegment1Name = _FsfrConnSegment1Name_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 4),
    _FsfrConnSegment1Name_Type()
)
fsfrConnSegment1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnSegment1Name.setStatus("current")
_FsfrConnSegment1VCGroup_Type = DisplayString
_FsfrConnSegment1VCGroup_Object = MibTableColumn
fsfrConnSegment1VCGroup = _FsfrConnSegment1VCGroup_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 5),
    _FsfrConnSegment1VCGroup_Type()
)
fsfrConnSegment1VCGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnSegment1VCGroup.setStatus("current")
_FsfrConnSegment1Dlci_Type = DlciNumber
_FsfrConnSegment1Dlci_Object = MibTableColumn
fsfrConnSegment1Dlci = _FsfrConnSegment1Dlci_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 6),
    _FsfrConnSegment1Dlci_Type()
)
fsfrConnSegment1Dlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnSegment1Dlci.setStatus("current")
_FsfrConnSegment2Name_Type = DisplayString
_FsfrConnSegment2Name_Object = MibTableColumn
fsfrConnSegment2Name = _FsfrConnSegment2Name_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 7),
    _FsfrConnSegment2Name_Type()
)
fsfrConnSegment2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnSegment2Name.setStatus("current")


class _FsfrConnSegment2Vpi_Type(Integer32):
    """Custom type fsfrConnSegment2Vpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_FsfrConnSegment2Vpi_Type.__name__ = "Integer32"
_FsfrConnSegment2Vpi_Object = MibTableColumn
fsfrConnSegment2Vpi = _FsfrConnSegment2Vpi_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 8),
    _FsfrConnSegment2Vpi_Type()
)
fsfrConnSegment2Vpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnSegment2Vpi.setStatus("current")


class _FsfrConnSegment2Vci_Type(Integer32):
    """Custom type fsfrConnSegment2Vci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_FsfrConnSegment2Vci_Type.__name__ = "Integer32"
_FsfrConnSegment2Vci_Object = MibTableColumn
fsfrConnSegment2Vci = _FsfrConnSegment2Vci_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 9),
    _FsfrConnSegment2Vci_Type()
)
fsfrConnSegment2Vci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnSegment2Vci.setStatus("current")


class _FsfrConnServiceTranslation_Type(Integer32):
    """Custom type fsfrConnServiceTranslation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("serviceTranslationEnabled", 1),
          ("serviceTranslationNotEnabled", 2))
    )


_FsfrConnServiceTranslation_Type.__name__ = "Integer32"
_FsfrConnServiceTranslation_Object = MibTableColumn
fsfrConnServiceTranslation = _FsfrConnServiceTranslation_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 10),
    _FsfrConnServiceTranslation_Type()
)
fsfrConnServiceTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnServiceTranslation.setStatus("current")
_FsfrConnFrSscsDlci_Type = DlciNumber
_FsfrConnFrSscsDlci_Object = MibTableColumn
fsfrConnFrSscsDlci = _FsfrConnFrSscsDlci_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 11),
    _FsfrConnFrSscsDlci_Type()
)
fsfrConnFrSscsDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnFrSscsDlci.setStatus("current")


class _FsfrConnEfciBit_Type(Integer32):
    """Custom type fsfrConnEfciBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("mapFecn", 1),
          ("notMapFecn", 2))
    )


_FsfrConnEfciBit_Type.__name__ = "Integer32"
_FsfrConnEfciBit_Object = MibTableColumn
fsfrConnEfciBit = _FsfrConnEfciBit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 12),
    _FsfrConnEfciBit_Type()
)
fsfrConnEfciBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnEfciBit.setStatus("current")


class _FsfrConnDeBit_Type(Integer32):
    """Custom type fsfrConnDeBit based on Integer32"""
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
        *(("noMapClp", 1),
          ("mapClp", 2),
          ("setDe0", 3),
          ("setDe1", 4))
    )


_FsfrConnDeBit_Type.__name__ = "Integer32"
_FsfrConnDeBit_Object = MibTableColumn
fsfrConnDeBit = _FsfrConnDeBit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 13),
    _FsfrConnDeBit_Type()
)
fsfrConnDeBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnDeBit.setStatus("current")


class _FsfrConnClpBit_Type(Integer32):
    """Custom type fsfrConnClpBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("setClpTo0AndCopyDeToFrsscsDe", 1),
          ("setClpTo1AndCopyDeToFrsscsDe", 2),
          ("copyDeToFrsscsDeAndClp", 3),
          ("copyDeToClp", 4),
          ("setClp1", 5),
          ("setClp0", 6))
    )


_FsfrConnClpBit_Type.__name__ = "Integer32"
_FsfrConnClpBit_Object = MibTableColumn
fsfrConnClpBit = _FsfrConnClpBit_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 1, 7, 1, 1, 14),
    _FsfrConnClpBit_Type()
)
fsfrConnClpBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsfrConnClpBit.setStatus("current")
_FsFrMIBConformance_ObjectIdentity = ObjectIdentity
fsFrMIBConformance = _FsFrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3)
)
_FsFrMIBCompliances_ObjectIdentity = ObjectIdentity
fsFrMIBCompliances = _FsFrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 1)
)
_FsFrMIBGroups_ObjectIdentity = ObjectIdentity
fsFrMIBGroups = _FsFrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2)
)
frDlcmiEntry.registerAugmentions(
    ("FS-FRAME-RELAY-MIB",
     "fsfrLmiEntry")
)
fsfrLmiEntry.setIndexNames(*frDlcmiEntry.getIndexNames())
frCircuitEntry.registerAugmentions(
    ("FS-FRAME-RELAY-MIB",
     "fsfrCircuitEntry")
)
fsfrCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())
frCircuitEntry.registerAugmentions(
    ("FS-FRAME-RELAY-MIB",
     "fsfrExtCircuitEntry")
)
fsfrExtCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())

# Managed Objects groups

fsFrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 1)
)
fsFrMIBGroup.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrLmiLinkstatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiLinkType"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiEnquiryIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiEnquiryOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiUpdateStatusIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiUpdateStatusOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusTimeouts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusEnqTimeouts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiN392Dce"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiN393Dce"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiT392Dce"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitDEins"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitDEouts"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitDropPktsOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitType"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitIfName"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitIfType"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitSubifIndex"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMapStatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitCreateType"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMulticast"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitRoutedDlci"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitRoutedIf"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapIndex"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapProtocol"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapAddress"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapType"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapEncaps"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapBroadcast"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapPayloadCompress"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapTcpHdrCompress"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcAddrLocal"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcAddrRemote"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcThroughputIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcMinThruputOut"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcMinThruputIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcCommitBurstIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcExcessBurstIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    fsFrMIBGroup.setStatus("deprecated")

fsFrMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 2)
)
fsFrMIBGroupRev1.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrLmiLinkstatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiLinkType"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiEnquiryIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiEnquiryOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiUpdateStatusIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiUpdateStatusOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusTimeouts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusEnqTimeouts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiN392Dce"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiN393Dce"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiT392Dce"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitDEins"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitDEouts"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitDropPktsOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitType"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitIfName"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitIfType"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitSubifIndex"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMapStatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitCreateType"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMulticast"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitRoutedDlci"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitRoutedIf"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitUncompressIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitUncompressOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapIndex"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapProtocol"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapAddress"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapType"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapEncaps"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapBroadcast"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapTcpHdrCompress"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapRtpHdrCompress"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapPayloadCompressType"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcAddrLocal"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcAddrRemote"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcThroughputIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcMinThruputOut"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcMinThruputIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcCommitBurstIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcExcessBurstIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    fsFrMIBGroupRev1.setStatus("deprecated")

fsFrLmiMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 3)
)
fsFrLmiMIBGroup.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrLmiLinkstatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiLinkType"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiEnquiryIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiEnquiryOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiUpdateStatusIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiUpdateStatusOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusTimeouts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiStatusEnqTimeouts"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiN392Dce"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiN393Dce"),
        ("FS-FRAME-RELAY-MIB", "fsfrLmiT392Dce"))
)
if mibBuilder.loadTexts:
    fsFrLmiMIBGroup.setStatus("current")

fsFrCircuitMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 4)
)
fsFrCircuitMIBGroup.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrCircuitDEins"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitDEouts"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitDropPktsOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrCircuitType"))
)
if mibBuilder.loadTexts:
    fsFrCircuitMIBGroup.setStatus("current")

fsExtCircuitMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 5)
)
fsExtCircuitMIBGroup.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrExtCircuitIfName"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitIfType"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitSubifIndex"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMapStatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitCreateType"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMulticast"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitRoutedDlci"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitRoutedIf"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitUncompressIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitUncompressOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitFECNOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitBECNOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMinThruputOut"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMinThruputIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitBcastPktOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitBcastByteOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitBandwidth"))
)
if mibBuilder.loadTexts:
    fsExtCircuitMIBGroup.setStatus("deprecated")

fsFrTsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 6)
)
fsFrTsMIBGroup.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrExtCircuitShapeByteLimit"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitShapeInterval"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitShapeByteIncrement"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitShapePkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitShapeBytes"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitShapePktsDelay"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitShapeBytesDelay"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitShapeActive"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitShapeAdapting"))
)
if mibBuilder.loadTexts:
    fsFrTsMIBGroup.setStatus("current")

fsFrMapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 7)
)
fsFrMapMIBGroup.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrMapIndex"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapProtocol"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapAddress"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapType"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapEncaps"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapBroadcast"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapTcpHdrCompress"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapRtpHdrCompress"),
        ("FS-FRAME-RELAY-MIB", "fsfrMapPayloadCompressType"))
)
if mibBuilder.loadTexts:
    fsFrMapMIBGroup.setStatus("current")

fsFrSvcMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 8)
)
fsFrSvcMIBGroup.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrSvcAddrLocal"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcAddrRemote"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcThroughputIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcCommitBurstIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcExcessBurstIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    fsFrSvcMIBGroup.setStatus("current")

fsFrElmiMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 9)
)
fsFrElmiMIBGroup.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrElmiIpAddr"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiArStatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiRemoteStatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborArStatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborIpAddress"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborIfIndex"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborVendorName"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborPlatformName"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborDeviceName"))
)
if mibBuilder.loadTexts:
    fsFrElmiMIBGroup.setStatus("deprecated")

fsFrElmiMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 10)
)
fsFrElmiMIBGroup1.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrElmiIpAddr"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiArStatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiRemoteStatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborArStatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborIpAddress"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborIfIndex"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborVendorName"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborPlatformName"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiNeighborDeviceName"),
        ("FS-FRAME-RELAY-MIB", "fsfrElmiLinkStatus"))
)
if mibBuilder.loadTexts:
    fsFrElmiMIBGroup1.setStatus("current")

fsFrFragMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 11)
)
fsFrFragMIBGroup.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrFragSize"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragType"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragInPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragOutPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragInOctets"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragOutOctets"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragNotInPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragNotOutPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragNotInOctets"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragNotOutOctets"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragAssembledInPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragAssembledInOctets"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragPreOutPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragPreOutOctets"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragDroppedReAssembledInPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragDroppedFragmentedOutPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragTimeoutsIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragOutOfSeqFragPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragUnexpectedBBitSetPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragSeqMissedPkts"),
        ("FS-FRAME-RELAY-MIB", "fsfrFragInterleavedOutPkts"))
)
if mibBuilder.loadTexts:
    fsFrFragMIBGroup.setStatus("current")

fsFrConnMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 12)
)
fsFrConnMIBGroup.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrConnName"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnID"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnState"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnSegment1Name"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnSegment1VCGroup"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnSegment1Dlci"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnSegment2Name"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnSegment2Vpi"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnSegment2Vci"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnServiceTranslation"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnFrSscsDlci"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnEfciBit"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnDeBit"),
        ("FS-FRAME-RELAY-MIB", "fsfrConnClpBit"))
)
if mibBuilder.loadTexts:
    fsFrConnMIBGroup.setStatus("current")

fsExtCircuitMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 2, 13)
)
fsExtCircuitMIBGroup1.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsfrExtCircuitIfName"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitIfType"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitSubifIndex"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMapStatus"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitCreateType"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMulticast"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitRoutedDlci"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitRoutedIf"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitUncompressIns"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitUncompressOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitFECNOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitBECNOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMinThruputOut"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitMinThruputIn"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitBcastPktOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitBcastByteOuts"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitBandwidth"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitTxDataRate"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitTxPktRate"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitRcvDataRate"),
        ("FS-FRAME-RELAY-MIB", "fsfrExtCircuitRcvPktRate"))
)
if mibBuilder.loadTexts:
    fsExtCircuitMIBGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fsFrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 1, 1)
)
fsFrMIBCompliance.setObjects(
    ("FS-FRAME-RELAY-MIB", "fsFrMIBGroup")
)
if mibBuilder.loadTexts:
    fsFrMIBCompliance.setStatus(
        "obsolete"
    )

fsFrMIBCompliancesRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 1, 2)
)
fsFrMIBCompliancesRev1.setObjects(
    ("FS-FRAME-RELAY-MIB", "fsFrMIBGroupRev1")
)
if mibBuilder.loadTexts:
    fsFrMIBCompliancesRev1.setStatus(
        "obsolete"
    )

fsFrMIBCompliancesRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 1, 3)
)
fsFrMIBCompliancesRev2.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsFrLmiMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrCircuitMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsExtCircuitMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrTsMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrMapMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrSvcMIBGroup"))
)
if mibBuilder.loadTexts:
    fsFrMIBCompliancesRev2.setStatus(
        "obsolete"
    )

fsFrMIBCompliancesRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 1, 4)
)
fsFrMIBCompliancesRev3.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsFrLmiMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrCircuitMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsExtCircuitMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrTsMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrMapMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrSvcMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrElmiMIBGroup"))
)
if mibBuilder.loadTexts:
    fsFrMIBCompliancesRev3.setStatus(
        "deprecated"
    )

fsFrMIBCompliancesRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 50, 3, 1, 5)
)
fsFrMIBCompliancesRev4.setObjects(
      *(("FS-FRAME-RELAY-MIB", "fsFrLmiMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrCircuitMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsExtCircuitMIBGroup1"),
        ("FS-FRAME-RELAY-MIB", "fsFrTsMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrMapMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrSvcMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrElmiMIBGroup1"),
        ("FS-FRAME-RELAY-MIB", "fsFrFragMIBGroup"),
        ("FS-FRAME-RELAY-MIB", "fsFrConnMIBGroup"))
)
if mibBuilder.loadTexts:
    fsFrMIBCompliancesRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-FRAME-RELAY-MIB",
    **{"DlciNumber": DlciNumber,
       "FSfrMapProtocols": FSfrMapProtocols,
       "fsFrameRelayMIB": fsFrameRelayMIB,
       "fsFrMIBObjects": fsFrMIBObjects,
       "fsfrLmiObjs": fsfrLmiObjs,
       "fsfrLmiTable": fsfrLmiTable,
       "fsfrLmiEntry": fsfrLmiEntry,
       "fsfrLmiLinkstatus": fsfrLmiLinkstatus,
       "fsfrLmiLinkType": fsfrLmiLinkType,
       "fsfrLmiEnquiryIns": fsfrLmiEnquiryIns,
       "fsfrLmiEnquiryOuts": fsfrLmiEnquiryOuts,
       "fsfrLmiStatusIns": fsfrLmiStatusIns,
       "fsfrLmiStatusOuts": fsfrLmiStatusOuts,
       "fsfrLmiUpdateStatusIns": fsfrLmiUpdateStatusIns,
       "fsfrLmiUpdateStatusOuts": fsfrLmiUpdateStatusOuts,
       "fsfrLmiStatusTimeouts": fsfrLmiStatusTimeouts,
       "fsfrLmiStatusEnqTimeouts": fsfrLmiStatusEnqTimeouts,
       "fsfrLmiN392Dce": fsfrLmiN392Dce,
       "fsfrLmiN393Dce": fsfrLmiN393Dce,
       "fsfrLmiT392Dce": fsfrLmiT392Dce,
       "fsfrCircuitObjs": fsfrCircuitObjs,
       "fsfrCircuitTable": fsfrCircuitTable,
       "fsfrCircuitEntry": fsfrCircuitEntry,
       "fsfrCircuitDEins": fsfrCircuitDEins,
       "fsfrCircuitDEouts": fsfrCircuitDEouts,
       "fsfrCircuitDropPktsOuts": fsfrCircuitDropPktsOuts,
       "fsfrCircuitType": fsfrCircuitType,
       "fsfrExtCircuitTable": fsfrExtCircuitTable,
       "fsfrExtCircuitEntry": fsfrExtCircuitEntry,
       "fsfrExtCircuitIfName": fsfrExtCircuitIfName,
       "fsfrExtCircuitIfType": fsfrExtCircuitIfType,
       "fsfrExtCircuitSubifIndex": fsfrExtCircuitSubifIndex,
       "fsfrExtCircuitMapStatus": fsfrExtCircuitMapStatus,
       "fsfrExtCircuitCreateType": fsfrExtCircuitCreateType,
       "fsfrExtCircuitMulticast": fsfrExtCircuitMulticast,
       "fsfrExtCircuitRoutedDlci": fsfrExtCircuitRoutedDlci,
       "fsfrExtCircuitRoutedIf": fsfrExtCircuitRoutedIf,
       "fsfrExtCircuitUncompressIns": fsfrExtCircuitUncompressIns,
       "fsfrExtCircuitUncompressOuts": fsfrExtCircuitUncompressOuts,
       "fsfrExtCircuitFECNOuts": fsfrExtCircuitFECNOuts,
       "fsfrExtCircuitBECNOuts": fsfrExtCircuitBECNOuts,
       "fsfrExtCircuitMinThruputOut": fsfrExtCircuitMinThruputOut,
       "fsfrExtCircuitMinThruputIn": fsfrExtCircuitMinThruputIn,
       "fsfrExtCircuitBcastPktOuts": fsfrExtCircuitBcastPktOuts,
       "fsfrExtCircuitBcastByteOuts": fsfrExtCircuitBcastByteOuts,
       "fsfrExtCircuitBandwidth": fsfrExtCircuitBandwidth,
       "fsfrExtCircuitShapeByteLimit": fsfrExtCircuitShapeByteLimit,
       "fsfrExtCircuitShapeInterval": fsfrExtCircuitShapeInterval,
       "fsfrExtCircuitShapeByteIncrement": fsfrExtCircuitShapeByteIncrement,
       "fsfrExtCircuitShapePkts": fsfrExtCircuitShapePkts,
       "fsfrExtCircuitShapeBytes": fsfrExtCircuitShapeBytes,
       "fsfrExtCircuitShapePktsDelay": fsfrExtCircuitShapePktsDelay,
       "fsfrExtCircuitShapeBytesDelay": fsfrExtCircuitShapeBytesDelay,
       "fsfrExtCircuitShapeActive": fsfrExtCircuitShapeActive,
       "fsfrExtCircuitShapeAdapting": fsfrExtCircuitShapeAdapting,
       "fsfrExtCircuitTxDataRate": fsfrExtCircuitTxDataRate,
       "fsfrExtCircuitTxPktRate": fsfrExtCircuitTxPktRate,
       "fsfrExtCircuitRcvDataRate": fsfrExtCircuitRcvDataRate,
       "fsfrExtCircuitRcvPktRate": fsfrExtCircuitRcvPktRate,
       "fsfrMapObjs": fsfrMapObjs,
       "fsfrMapTable": fsfrMapTable,
       "fsfrMapEntry": fsfrMapEntry,
       "fsfrMapIndex": fsfrMapIndex,
       "fsfrMapProtocol": fsfrMapProtocol,
       "fsfrMapAddress": fsfrMapAddress,
       "fsfrMapType": fsfrMapType,
       "fsfrMapEncaps": fsfrMapEncaps,
       "fsfrMapBroadcast": fsfrMapBroadcast,
       "fsfrMapPayloadCompress": fsfrMapPayloadCompress,
       "fsfrMapTcpHdrCompress": fsfrMapTcpHdrCompress,
       "fsfrMapRtpHdrCompress": fsfrMapRtpHdrCompress,
       "fsfrMapPayloadCompressType": fsfrMapPayloadCompressType,
       "fsfrSvcObjs": fsfrSvcObjs,
       "fsfrSvcTable": fsfrSvcTable,
       "fsfrSvcEntry": fsfrSvcEntry,
       "fsfrSvcAddrLocal": fsfrSvcAddrLocal,
       "fsfrSvcAddrRemote": fsfrSvcAddrRemote,
       "fsfrSvcThroughputIn": fsfrSvcThroughputIn,
       "fsfrSvcMinThruputOut": fsfrSvcMinThruputOut,
       "fsfrSvcMinThruputIn": fsfrSvcMinThruputIn,
       "fsfrSvcCommitBurstIn": fsfrSvcCommitBurstIn,
       "fsfrSvcExcessBurstIn": fsfrSvcExcessBurstIn,
       "fsfrSvcIdleTime": fsfrSvcIdleTime,
       "fsfrElmiObjs": fsfrElmiObjs,
       "fsfrElmiIpAddr": fsfrElmiIpAddr,
       "fsfrElmiTable": fsfrElmiTable,
       "fsfrElmiEntry": fsfrElmiEntry,
       "fsfrElmiLinkStatus": fsfrElmiLinkStatus,
       "fsfrElmiArStatus": fsfrElmiArStatus,
       "fsfrElmiRemoteStatus": fsfrElmiRemoteStatus,
       "fsfrElmiNeighborTable": fsfrElmiNeighborTable,
       "fsfrElmiNeighborEntry": fsfrElmiNeighborEntry,
       "fsfrElmiNeighborArStatus": fsfrElmiNeighborArStatus,
       "fsfrElmiNeighborIpAddress": fsfrElmiNeighborIpAddress,
       "fsfrElmiNeighborIfIndex": fsfrElmiNeighborIfIndex,
       "fsfrElmiNeighborVendorName": fsfrElmiNeighborVendorName,
       "fsfrElmiNeighborPlatformName": fsfrElmiNeighborPlatformName,
       "fsfrElmiNeighborDeviceName": fsfrElmiNeighborDeviceName,
       "fsfrFragObjs": fsfrFragObjs,
       "fsfrFragTable": fsfrFragTable,
       "fsfrFragEntry": fsfrFragEntry,
       "fsfrFragSize": fsfrFragSize,
       "fsfrFragType": fsfrFragType,
       "fsfrFragInPkts": fsfrFragInPkts,
       "fsfrFragOutPkts": fsfrFragOutPkts,
       "fsfrFragInOctets": fsfrFragInOctets,
       "fsfrFragOutOctets": fsfrFragOutOctets,
       "fsfrFragNotInPkts": fsfrFragNotInPkts,
       "fsfrFragNotOutPkts": fsfrFragNotOutPkts,
       "fsfrFragNotInOctets": fsfrFragNotInOctets,
       "fsfrFragNotOutOctets": fsfrFragNotOutOctets,
       "fsfrFragAssembledInPkts": fsfrFragAssembledInPkts,
       "fsfrFragAssembledInOctets": fsfrFragAssembledInOctets,
       "fsfrFragPreOutPkts": fsfrFragPreOutPkts,
       "fsfrFragPreOutOctets": fsfrFragPreOutOctets,
       "fsfrFragDroppedReAssembledInPkts": fsfrFragDroppedReAssembledInPkts,
       "fsfrFragDroppedFragmentedOutPkts": fsfrFragDroppedFragmentedOutPkts,
       "fsfrFragTimeoutsIn": fsfrFragTimeoutsIn,
       "fsfrFragOutOfSeqFragPkts": fsfrFragOutOfSeqFragPkts,
       "fsfrFragUnexpectedBBitSetPkts": fsfrFragUnexpectedBBitSetPkts,
       "fsfrFragSeqMissedPkts": fsfrFragSeqMissedPkts,
       "fsfrFragInterleavedOutPkts": fsfrFragInterleavedOutPkts,
       "fsfrConnectionObjs": fsfrConnectionObjs,
       "fsfrConnectionTable": fsfrConnectionTable,
       "fsfrConnectionEntry": fsfrConnectionEntry,
       "fsfrConnName": fsfrConnName,
       "fsfrConnID": fsfrConnID,
       "fsfrConnState": fsfrConnState,
       "fsfrConnSegment1Name": fsfrConnSegment1Name,
       "fsfrConnSegment1VCGroup": fsfrConnSegment1VCGroup,
       "fsfrConnSegment1Dlci": fsfrConnSegment1Dlci,
       "fsfrConnSegment2Name": fsfrConnSegment2Name,
       "fsfrConnSegment2Vpi": fsfrConnSegment2Vpi,
       "fsfrConnSegment2Vci": fsfrConnSegment2Vci,
       "fsfrConnServiceTranslation": fsfrConnServiceTranslation,
       "fsfrConnFrSscsDlci": fsfrConnFrSscsDlci,
       "fsfrConnEfciBit": fsfrConnEfciBit,
       "fsfrConnDeBit": fsfrConnDeBit,
       "fsfrConnClpBit": fsfrConnClpBit,
       "fsFrMIBConformance": fsFrMIBConformance,
       "fsFrMIBCompliances": fsFrMIBCompliances,
       "fsFrMIBCompliance": fsFrMIBCompliance,
       "fsFrMIBCompliancesRev1": fsFrMIBCompliancesRev1,
       "fsFrMIBCompliancesRev2": fsFrMIBCompliancesRev2,
       "fsFrMIBCompliancesRev3": fsFrMIBCompliancesRev3,
       "fsFrMIBCompliancesRev4": fsFrMIBCompliancesRev4,
       "fsFrMIBGroups": fsFrMIBGroups,
       "fsFrMIBGroup": fsFrMIBGroup,
       "fsFrMIBGroupRev1": fsFrMIBGroupRev1,
       "fsFrLmiMIBGroup": fsFrLmiMIBGroup,
       "fsFrCircuitMIBGroup": fsFrCircuitMIBGroup,
       "fsExtCircuitMIBGroup": fsExtCircuitMIBGroup,
       "fsFrTsMIBGroup": fsFrTsMIBGroup,
       "fsFrMapMIBGroup": fsFrMapMIBGroup,
       "fsFrSvcMIBGroup": fsFrSvcMIBGroup,
       "fsFrElmiMIBGroup": fsFrElmiMIBGroup,
       "fsFrElmiMIBGroup1": fsFrElmiMIBGroup1,
       "fsFrFragMIBGroup": fsFrFragMIBGroup,
       "fsFrConnMIBGroup": fsFrConnMIBGroup,
       "fsExtCircuitMIBGroup1": fsExtCircuitMIBGroup1}
)
