# SNMP MIB module (QTECH-FRAME-RELAY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-FRAME-RELAY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:59:43 2025
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

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

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

qtechFrameRelayMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50)
)
if mibBuilder.loadTexts:
    qtechFrameRelayMIB.setRevisions(
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



class QtechfrMapProtocols(TextualConvention, Integer32):
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

_QtechFrMIBObjects_ObjectIdentity = ObjectIdentity
qtechFrMIBObjects = _QtechFrMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1)
)
_QtechfrLmiObjs_ObjectIdentity = ObjectIdentity
qtechfrLmiObjs = _QtechfrLmiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1)
)
_QtechfrLmiTable_Object = MibTable
qtechfrLmiTable = _QtechfrLmiTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechfrLmiTable.setStatus("current")
_QtechfrLmiEntry_Object = MibTableRow
qtechfrLmiEntry = _QtechfrLmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    qtechfrLmiEntry.setStatus("current")


class _QtechfrLmiLinkstatus_Type(Integer32):
    """Custom type qtechfrLmiLinkstatus based on Integer32"""
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


_QtechfrLmiLinkstatus_Type.__name__ = "Integer32"
_QtechfrLmiLinkstatus_Object = MibTableColumn
qtechfrLmiLinkstatus = _QtechfrLmiLinkstatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 1),
    _QtechfrLmiLinkstatus_Type()
)
qtechfrLmiLinkstatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiLinkstatus.setStatus("current")


class _QtechfrLmiLinkType_Type(Integer32):
    """Custom type qtechfrLmiLinkType based on Integer32"""
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


_QtechfrLmiLinkType_Type.__name__ = "Integer32"
_QtechfrLmiLinkType_Object = MibTableColumn
qtechfrLmiLinkType = _QtechfrLmiLinkType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 2),
    _QtechfrLmiLinkType_Type()
)
qtechfrLmiLinkType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiLinkType.setStatus("current")
_QtechfrLmiEnquiryIns_Type = Counter32
_QtechfrLmiEnquiryIns_Object = MibTableColumn
qtechfrLmiEnquiryIns = _QtechfrLmiEnquiryIns_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 3),
    _QtechfrLmiEnquiryIns_Type()
)
qtechfrLmiEnquiryIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiEnquiryIns.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrLmiEnquiryIns.setUnits("messages")
_QtechfrLmiEnquiryOuts_Type = Counter32
_QtechfrLmiEnquiryOuts_Object = MibTableColumn
qtechfrLmiEnquiryOuts = _QtechfrLmiEnquiryOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 4),
    _QtechfrLmiEnquiryOuts_Type()
)
qtechfrLmiEnquiryOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiEnquiryOuts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrLmiEnquiryOuts.setUnits("messages")
_QtechfrLmiStatusIns_Type = Counter32
_QtechfrLmiStatusIns_Object = MibTableColumn
qtechfrLmiStatusIns = _QtechfrLmiStatusIns_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 5),
    _QtechfrLmiStatusIns_Type()
)
qtechfrLmiStatusIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiStatusIns.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrLmiStatusIns.setUnits("messages")
_QtechfrLmiStatusOuts_Type = Counter32
_QtechfrLmiStatusOuts_Object = MibTableColumn
qtechfrLmiStatusOuts = _QtechfrLmiStatusOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 6),
    _QtechfrLmiStatusOuts_Type()
)
qtechfrLmiStatusOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiStatusOuts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrLmiStatusOuts.setUnits("messages")
_QtechfrLmiUpdateStatusIns_Type = Counter32
_QtechfrLmiUpdateStatusIns_Object = MibTableColumn
qtechfrLmiUpdateStatusIns = _QtechfrLmiUpdateStatusIns_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 7),
    _QtechfrLmiUpdateStatusIns_Type()
)
qtechfrLmiUpdateStatusIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiUpdateStatusIns.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrLmiUpdateStatusIns.setUnits("messages")
_QtechfrLmiUpdateStatusOuts_Type = Counter32
_QtechfrLmiUpdateStatusOuts_Object = MibTableColumn
qtechfrLmiUpdateStatusOuts = _QtechfrLmiUpdateStatusOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 8),
    _QtechfrLmiUpdateStatusOuts_Type()
)
qtechfrLmiUpdateStatusOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiUpdateStatusOuts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrLmiUpdateStatusOuts.setUnits("messages")
_QtechfrLmiStatusTimeouts_Type = Counter32
_QtechfrLmiStatusTimeouts_Object = MibTableColumn
qtechfrLmiStatusTimeouts = _QtechfrLmiStatusTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 9),
    _QtechfrLmiStatusTimeouts_Type()
)
qtechfrLmiStatusTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiStatusTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrLmiStatusTimeouts.setUnits("times")
_QtechfrLmiStatusEnqTimeouts_Type = Counter32
_QtechfrLmiStatusEnqTimeouts_Object = MibTableColumn
qtechfrLmiStatusEnqTimeouts = _QtechfrLmiStatusEnqTimeouts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 10),
    _QtechfrLmiStatusEnqTimeouts_Type()
)
qtechfrLmiStatusEnqTimeouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiStatusEnqTimeouts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrLmiStatusEnqTimeouts.setUnits("times")


class _QtechfrLmiN392Dce_Type(Integer32):
    """Custom type qtechfrLmiN392Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_QtechfrLmiN392Dce_Type.__name__ = "Integer32"
_QtechfrLmiN392Dce_Object = MibTableColumn
qtechfrLmiN392Dce = _QtechfrLmiN392Dce_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 11),
    _QtechfrLmiN392Dce_Type()
)
qtechfrLmiN392Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiN392Dce.setStatus("current")


class _QtechfrLmiN393Dce_Type(Integer32):
    """Custom type qtechfrLmiN393Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 10),
    )


_QtechfrLmiN393Dce_Type.__name__ = "Integer32"
_QtechfrLmiN393Dce_Object = MibTableColumn
qtechfrLmiN393Dce = _QtechfrLmiN393Dce_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 12),
    _QtechfrLmiN393Dce_Type()
)
qtechfrLmiN393Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiN393Dce.setStatus("current")


class _QtechfrLmiT392Dce_Type(Integer32):
    """Custom type qtechfrLmiT392Dce based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_QtechfrLmiT392Dce_Type.__name__ = "Integer32"
_QtechfrLmiT392Dce_Object = MibTableColumn
qtechfrLmiT392Dce = _QtechfrLmiT392Dce_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 1, 1, 1, 13),
    _QtechfrLmiT392Dce_Type()
)
qtechfrLmiT392Dce.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrLmiT392Dce.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrLmiT392Dce.setUnits("seconds")
_QtechfrCircuitObjs_ObjectIdentity = ObjectIdentity
qtechfrCircuitObjs = _QtechfrCircuitObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2)
)
_QtechfrCircuitTable_Object = MibTable
qtechfrCircuitTable = _QtechfrCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 1)
)
if mibBuilder.loadTexts:
    qtechfrCircuitTable.setStatus("current")
_QtechfrCircuitEntry_Object = MibTableRow
qtechfrCircuitEntry = _QtechfrCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 1, 1)
)
if mibBuilder.loadTexts:
    qtechfrCircuitEntry.setStatus("current")
_QtechfrCircuitDEins_Type = Counter32
_QtechfrCircuitDEins_Object = MibTableColumn
qtechfrCircuitDEins = _QtechfrCircuitDEins_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 1, 1, 1),
    _QtechfrCircuitDEins_Type()
)
qtechfrCircuitDEins.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrCircuitDEins.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrCircuitDEins.setUnits("packets")
_QtechfrCircuitDEouts_Type = Counter32
_QtechfrCircuitDEouts_Object = MibTableColumn
qtechfrCircuitDEouts = _QtechfrCircuitDEouts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 1, 1, 2),
    _QtechfrCircuitDEouts_Type()
)
qtechfrCircuitDEouts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrCircuitDEouts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrCircuitDEouts.setUnits("packets")
_QtechfrCircuitDropPktsOuts_Type = Counter32
_QtechfrCircuitDropPktsOuts_Object = MibTableColumn
qtechfrCircuitDropPktsOuts = _QtechfrCircuitDropPktsOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 1, 1, 3),
    _QtechfrCircuitDropPktsOuts_Type()
)
qtechfrCircuitDropPktsOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrCircuitDropPktsOuts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrCircuitDropPktsOuts.setUnits("packets")


class _QtechfrCircuitType_Type(Integer32):
    """Custom type qtechfrCircuitType based on Integer32"""
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


_QtechfrCircuitType_Type.__name__ = "Integer32"
_QtechfrCircuitType_Object = MibTableColumn
qtechfrCircuitType = _QtechfrCircuitType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 1, 1, 4),
    _QtechfrCircuitType_Type()
)
qtechfrCircuitType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrCircuitType.setStatus("current")
_QtechfrExtCircuitTable_Object = MibTable
qtechfrExtCircuitTable = _QtechfrExtCircuitTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2)
)
if mibBuilder.loadTexts:
    qtechfrExtCircuitTable.setStatus("current")
_QtechfrExtCircuitEntry_Object = MibTableRow
qtechfrExtCircuitEntry = _QtechfrExtCircuitEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1)
)
if mibBuilder.loadTexts:
    qtechfrExtCircuitEntry.setStatus("current")
_QtechfrExtCircuitIfName_Type = DisplayString
_QtechfrExtCircuitIfName_Object = MibTableColumn
qtechfrExtCircuitIfName = _QtechfrExtCircuitIfName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 1),
    _QtechfrExtCircuitIfName_Type()
)
qtechfrExtCircuitIfName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitIfName.setStatus("current")


class _QtechfrExtCircuitIfType_Type(Integer32):
    """Custom type qtechfrExtCircuitIfType based on Integer32"""
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


_QtechfrExtCircuitIfType_Type.__name__ = "Integer32"
_QtechfrExtCircuitIfType_Object = MibTableColumn
qtechfrExtCircuitIfType = _QtechfrExtCircuitIfType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 2),
    _QtechfrExtCircuitIfType_Type()
)
qtechfrExtCircuitIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitIfType.setStatus("current")
_QtechfrExtCircuitSubifIndex_Type = InterfaceIndex
_QtechfrExtCircuitSubifIndex_Object = MibTableColumn
qtechfrExtCircuitSubifIndex = _QtechfrExtCircuitSubifIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 3),
    _QtechfrExtCircuitSubifIndex_Type()
)
qtechfrExtCircuitSubifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitSubifIndex.setStatus("current")


class _QtechfrExtCircuitMapStatus_Type(Integer32):
    """Custom type qtechfrExtCircuitMapStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 2047),
    )


_QtechfrExtCircuitMapStatus_Type.__name__ = "Integer32"
_QtechfrExtCircuitMapStatus_Object = MibTableColumn
qtechfrExtCircuitMapStatus = _QtechfrExtCircuitMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 4),
    _QtechfrExtCircuitMapStatus_Type()
)
qtechfrExtCircuitMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitMapStatus.setStatus("current")


class _QtechfrExtCircuitCreateType_Type(Integer32):
    """Custom type qtechfrExtCircuitCreateType based on Integer32"""
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


_QtechfrExtCircuitCreateType_Type.__name__ = "Integer32"
_QtechfrExtCircuitCreateType_Object = MibTableColumn
qtechfrExtCircuitCreateType = _QtechfrExtCircuitCreateType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 5),
    _QtechfrExtCircuitCreateType_Type()
)
qtechfrExtCircuitCreateType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitCreateType.setStatus("current")
_QtechfrExtCircuitMulticast_Type = TruthValue
_QtechfrExtCircuitMulticast_Object = MibTableColumn
qtechfrExtCircuitMulticast = _QtechfrExtCircuitMulticast_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 6),
    _QtechfrExtCircuitMulticast_Type()
)
qtechfrExtCircuitMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitMulticast.setStatus("current")
_QtechfrExtCircuitRoutedDlci_Type = DlciNumber
_QtechfrExtCircuitRoutedDlci_Object = MibTableColumn
qtechfrExtCircuitRoutedDlci = _QtechfrExtCircuitRoutedDlci_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 7),
    _QtechfrExtCircuitRoutedDlci_Type()
)
qtechfrExtCircuitRoutedDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitRoutedDlci.setStatus("current")
_QtechfrExtCircuitRoutedIf_Type = InterfaceIndex
_QtechfrExtCircuitRoutedIf_Object = MibTableColumn
qtechfrExtCircuitRoutedIf = _QtechfrExtCircuitRoutedIf_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 8),
    _QtechfrExtCircuitRoutedIf_Type()
)
qtechfrExtCircuitRoutedIf.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitRoutedIf.setStatus("current")
_QtechfrExtCircuitUncompressIns_Type = Counter32
_QtechfrExtCircuitUncompressIns_Object = MibTableColumn
qtechfrExtCircuitUncompressIns = _QtechfrExtCircuitUncompressIns_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 9),
    _QtechfrExtCircuitUncompressIns_Type()
)
qtechfrExtCircuitUncompressIns.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitUncompressIns.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrExtCircuitUncompressIns.setUnits("octets")
_QtechfrExtCircuitUncompressOuts_Type = Counter32
_QtechfrExtCircuitUncompressOuts_Object = MibTableColumn
qtechfrExtCircuitUncompressOuts = _QtechfrExtCircuitUncompressOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 10),
    _QtechfrExtCircuitUncompressOuts_Type()
)
qtechfrExtCircuitUncompressOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitUncompressOuts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrExtCircuitUncompressOuts.setUnits("octets")
_QtechfrExtCircuitFECNOuts_Type = Counter32
_QtechfrExtCircuitFECNOuts_Object = MibTableColumn
qtechfrExtCircuitFECNOuts = _QtechfrExtCircuitFECNOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 11),
    _QtechfrExtCircuitFECNOuts_Type()
)
qtechfrExtCircuitFECNOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitFECNOuts.setStatus("current")
_QtechfrExtCircuitBECNOuts_Type = Counter32
_QtechfrExtCircuitBECNOuts_Object = MibTableColumn
qtechfrExtCircuitBECNOuts = _QtechfrExtCircuitBECNOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 12),
    _QtechfrExtCircuitBECNOuts_Type()
)
qtechfrExtCircuitBECNOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitBECNOuts.setStatus("current")


class _QtechfrExtCircuitMinThruputOut_Type(Integer32):
    """Custom type qtechfrExtCircuitMinThruputOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_QtechfrExtCircuitMinThruputOut_Type.__name__ = "Integer32"
_QtechfrExtCircuitMinThruputOut_Object = MibTableColumn
qtechfrExtCircuitMinThruputOut = _QtechfrExtCircuitMinThruputOut_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 13),
    _QtechfrExtCircuitMinThruputOut_Type()
)
qtechfrExtCircuitMinThruputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitMinThruputOut.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrExtCircuitMinThruputOut.setUnits("bits per second")


class _QtechfrExtCircuitMinThruputIn_Type(Integer32):
    """Custom type qtechfrExtCircuitMinThruputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_QtechfrExtCircuitMinThruputIn_Type.__name__ = "Integer32"
_QtechfrExtCircuitMinThruputIn_Object = MibTableColumn
qtechfrExtCircuitMinThruputIn = _QtechfrExtCircuitMinThruputIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 14),
    _QtechfrExtCircuitMinThruputIn_Type()
)
qtechfrExtCircuitMinThruputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitMinThruputIn.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrExtCircuitMinThruputIn.setUnits("bits per second")
_QtechfrExtCircuitBcastPktOuts_Type = Counter32
_QtechfrExtCircuitBcastPktOuts_Object = MibTableColumn
qtechfrExtCircuitBcastPktOuts = _QtechfrExtCircuitBcastPktOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 15),
    _QtechfrExtCircuitBcastPktOuts_Type()
)
qtechfrExtCircuitBcastPktOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitBcastPktOuts.setStatus("current")
_QtechfrExtCircuitBcastByteOuts_Type = Counter32
_QtechfrExtCircuitBcastByteOuts_Object = MibTableColumn
qtechfrExtCircuitBcastByteOuts = _QtechfrExtCircuitBcastByteOuts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 16),
    _QtechfrExtCircuitBcastByteOuts_Type()
)
qtechfrExtCircuitBcastByteOuts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitBcastByteOuts.setStatus("current")


class _QtechfrExtCircuitBandwidth_Type(Integer32):
    """Custom type qtechfrExtCircuitBandwidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_QtechfrExtCircuitBandwidth_Type.__name__ = "Integer32"
_QtechfrExtCircuitBandwidth_Object = MibTableColumn
qtechfrExtCircuitBandwidth = _QtechfrExtCircuitBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 17),
    _QtechfrExtCircuitBandwidth_Type()
)
qtechfrExtCircuitBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrExtCircuitBandwidth.setUnits("bits per second")


class _QtechfrExtCircuitShapeByteLimit_Type(Integer32):
    """Custom type qtechfrExtCircuitShapeByteLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 2147483647),
    )


_QtechfrExtCircuitShapeByteLimit_Type.__name__ = "Integer32"
_QtechfrExtCircuitShapeByteLimit_Object = MibTableColumn
qtechfrExtCircuitShapeByteLimit = _QtechfrExtCircuitShapeByteLimit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 18),
    _QtechfrExtCircuitShapeByteLimit_Type()
)
qtechfrExtCircuitShapeByteLimit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeByteLimit.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeByteLimit.setUnits("octets")


class _QtechfrExtCircuitShapeInterval_Type(Integer32):
    """Custom type qtechfrExtCircuitShapeInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 125),
    )


_QtechfrExtCircuitShapeInterval_Type.__name__ = "Integer32"
_QtechfrExtCircuitShapeInterval_Object = MibTableColumn
qtechfrExtCircuitShapeInterval = _QtechfrExtCircuitShapeInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 19),
    _QtechfrExtCircuitShapeInterval_Type()
)
qtechfrExtCircuitShapeInterval.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeInterval.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeInterval.setUnits("milliseconds")


class _QtechfrExtCircuitShapeByteIncrement_Type(Integer32):
    """Custom type qtechfrExtCircuitShapeByteIncrement based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(125, 2147483647),
    )


_QtechfrExtCircuitShapeByteIncrement_Type.__name__ = "Integer32"
_QtechfrExtCircuitShapeByteIncrement_Object = MibTableColumn
qtechfrExtCircuitShapeByteIncrement = _QtechfrExtCircuitShapeByteIncrement_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 20),
    _QtechfrExtCircuitShapeByteIncrement_Type()
)
qtechfrExtCircuitShapeByteIncrement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeByteIncrement.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeByteIncrement.setUnits("octets")
_QtechfrExtCircuitShapePkts_Type = Counter32
_QtechfrExtCircuitShapePkts_Object = MibTableColumn
qtechfrExtCircuitShapePkts = _QtechfrExtCircuitShapePkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 21),
    _QtechfrExtCircuitShapePkts_Type()
)
qtechfrExtCircuitShapePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapePkts.setStatus("current")
_QtechfrExtCircuitShapeBytes_Type = Counter32
_QtechfrExtCircuitShapeBytes_Object = MibTableColumn
qtechfrExtCircuitShapeBytes = _QtechfrExtCircuitShapeBytes_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 22),
    _QtechfrExtCircuitShapeBytes_Type()
)
qtechfrExtCircuitShapeBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeBytes.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeBytes.setUnits("octets")
_QtechfrExtCircuitShapePktsDelay_Type = Counter32
_QtechfrExtCircuitShapePktsDelay_Object = MibTableColumn
qtechfrExtCircuitShapePktsDelay = _QtechfrExtCircuitShapePktsDelay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 23),
    _QtechfrExtCircuitShapePktsDelay_Type()
)
qtechfrExtCircuitShapePktsDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapePktsDelay.setStatus("current")
_QtechfrExtCircuitShapeBytesDelay_Type = Counter32
_QtechfrExtCircuitShapeBytesDelay_Object = MibTableColumn
qtechfrExtCircuitShapeBytesDelay = _QtechfrExtCircuitShapeBytesDelay_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 24),
    _QtechfrExtCircuitShapeBytesDelay_Type()
)
qtechfrExtCircuitShapeBytesDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeBytesDelay.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeBytesDelay.setUnits("octets")
_QtechfrExtCircuitShapeActive_Type = TruthValue
_QtechfrExtCircuitShapeActive_Object = MibTableColumn
qtechfrExtCircuitShapeActive = _QtechfrExtCircuitShapeActive_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 25),
    _QtechfrExtCircuitShapeActive_Type()
)
qtechfrExtCircuitShapeActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeActive.setStatus("current")


class _QtechfrExtCircuitShapeAdapting_Type(Integer32):
    """Custom type qtechfrExtCircuitShapeAdapting based on Integer32"""
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


_QtechfrExtCircuitShapeAdapting_Type.__name__ = "Integer32"
_QtechfrExtCircuitShapeAdapting_Object = MibTableColumn
qtechfrExtCircuitShapeAdapting = _QtechfrExtCircuitShapeAdapting_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 26),
    _QtechfrExtCircuitShapeAdapting_Type()
)
qtechfrExtCircuitShapeAdapting.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitShapeAdapting.setStatus("current")


class _QtechfrExtCircuitTxDataRate_Type(Integer32):
    """Custom type qtechfrExtCircuitTxDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_QtechfrExtCircuitTxDataRate_Type.__name__ = "Integer32"
_QtechfrExtCircuitTxDataRate_Object = MibTableColumn
qtechfrExtCircuitTxDataRate = _QtechfrExtCircuitTxDataRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 27),
    _QtechfrExtCircuitTxDataRate_Type()
)
qtechfrExtCircuitTxDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitTxDataRate.setStatus("current")


class _QtechfrExtCircuitTxPktRate_Type(Integer32):
    """Custom type qtechfrExtCircuitTxPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_QtechfrExtCircuitTxPktRate_Type.__name__ = "Integer32"
_QtechfrExtCircuitTxPktRate_Object = MibTableColumn
qtechfrExtCircuitTxPktRate = _QtechfrExtCircuitTxPktRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 28),
    _QtechfrExtCircuitTxPktRate_Type()
)
qtechfrExtCircuitTxPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitTxPktRate.setStatus("current")


class _QtechfrExtCircuitRcvDataRate_Type(Integer32):
    """Custom type qtechfrExtCircuitRcvDataRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_QtechfrExtCircuitRcvDataRate_Type.__name__ = "Integer32"
_QtechfrExtCircuitRcvDataRate_Object = MibTableColumn
qtechfrExtCircuitRcvDataRate = _QtechfrExtCircuitRcvDataRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 29),
    _QtechfrExtCircuitRcvDataRate_Type()
)
qtechfrExtCircuitRcvDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitRcvDataRate.setStatus("current")


class _QtechfrExtCircuitRcvPktRate_Type(Integer32):
    """Custom type qtechfrExtCircuitRcvPktRate based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 45000000),
    )


_QtechfrExtCircuitRcvPktRate_Type.__name__ = "Integer32"
_QtechfrExtCircuitRcvPktRate_Object = MibTableColumn
qtechfrExtCircuitRcvPktRate = _QtechfrExtCircuitRcvPktRate_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 2, 2, 1, 30),
    _QtechfrExtCircuitRcvPktRate_Type()
)
qtechfrExtCircuitRcvPktRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrExtCircuitRcvPktRate.setStatus("current")
_QtechfrMapObjs_ObjectIdentity = ObjectIdentity
qtechfrMapObjs = _QtechfrMapObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3)
)
_QtechfrMapTable_Object = MibTable
qtechfrMapTable = _QtechfrMapTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1)
)
if mibBuilder.loadTexts:
    qtechfrMapTable.setStatus("current")
_QtechfrMapEntry_Object = MibTableRow
qtechfrMapEntry = _QtechfrMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1)
)
qtechfrMapEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
    (0, "QTECH-FRAME-RELAY-MIB", "qtechfrMapIndex"),
)
if mibBuilder.loadTexts:
    qtechfrMapEntry.setStatus("current")


class _QtechfrMapIndex_Type(Integer32):
    """Custom type qtechfrMapIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 999),
    )


_QtechfrMapIndex_Type.__name__ = "Integer32"
_QtechfrMapIndex_Object = MibTableColumn
qtechfrMapIndex = _QtechfrMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1, 1),
    _QtechfrMapIndex_Type()
)
qtechfrMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrMapIndex.setStatus("current")
_QtechfrMapProtocol_Type = QtechfrMapProtocols
_QtechfrMapProtocol_Object = MibTableColumn
qtechfrMapProtocol = _QtechfrMapProtocol_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1, 2),
    _QtechfrMapProtocol_Type()
)
qtechfrMapProtocol.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrMapProtocol.setStatus("current")


class _QtechfrMapAddress_Type(OctetString):
    """Custom type qtechfrMapAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_QtechfrMapAddress_Type.__name__ = "OctetString"
_QtechfrMapAddress_Object = MibTableColumn
qtechfrMapAddress = _QtechfrMapAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1, 3),
    _QtechfrMapAddress_Type()
)
qtechfrMapAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrMapAddress.setStatus("current")


class _QtechfrMapType_Type(Integer32):
    """Custom type qtechfrMapType based on Integer32"""
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


_QtechfrMapType_Type.__name__ = "Integer32"
_QtechfrMapType_Object = MibTableColumn
qtechfrMapType = _QtechfrMapType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1, 4),
    _QtechfrMapType_Type()
)
qtechfrMapType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrMapType.setStatus("current")


class _QtechfrMapEncaps_Type(Integer32):
    """Custom type qtechfrMapEncaps based on Integer32"""
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


_QtechfrMapEncaps_Type.__name__ = "Integer32"
_QtechfrMapEncaps_Object = MibTableColumn
qtechfrMapEncaps = _QtechfrMapEncaps_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1, 5),
    _QtechfrMapEncaps_Type()
)
qtechfrMapEncaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrMapEncaps.setStatus("current")
_QtechfrMapBroadcast_Type = TruthValue
_QtechfrMapBroadcast_Object = MibTableColumn
qtechfrMapBroadcast = _QtechfrMapBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1, 6),
    _QtechfrMapBroadcast_Type()
)
qtechfrMapBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrMapBroadcast.setStatus("current")
_QtechfrMapPayloadCompress_Type = TruthValue
_QtechfrMapPayloadCompress_Object = MibTableColumn
qtechfrMapPayloadCompress = _QtechfrMapPayloadCompress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1, 7),
    _QtechfrMapPayloadCompress_Type()
)
qtechfrMapPayloadCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrMapPayloadCompress.setStatus("deprecated")


class _QtechfrMapTcpHdrCompress_Type(Integer32):
    """Custom type qtechfrMapTcpHdrCompress based on Integer32"""
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


_QtechfrMapTcpHdrCompress_Type.__name__ = "Integer32"
_QtechfrMapTcpHdrCompress_Object = MibTableColumn
qtechfrMapTcpHdrCompress = _QtechfrMapTcpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1, 8),
    _QtechfrMapTcpHdrCompress_Type()
)
qtechfrMapTcpHdrCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrMapTcpHdrCompress.setStatus("current")


class _QtechfrMapRtpHdrCompress_Type(Integer32):
    """Custom type qtechfrMapRtpHdrCompress based on Integer32"""
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


_QtechfrMapRtpHdrCompress_Type.__name__ = "Integer32"
_QtechfrMapRtpHdrCompress_Object = MibTableColumn
qtechfrMapRtpHdrCompress = _QtechfrMapRtpHdrCompress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1, 9),
    _QtechfrMapRtpHdrCompress_Type()
)
qtechfrMapRtpHdrCompress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrMapRtpHdrCompress.setStatus("current")


class _QtechfrMapPayloadCompressType_Type(Integer32):
    """Custom type qtechfrMapPayloadCompressType based on Integer32"""
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


_QtechfrMapPayloadCompressType_Type.__name__ = "Integer32"
_QtechfrMapPayloadCompressType_Object = MibTableColumn
qtechfrMapPayloadCompressType = _QtechfrMapPayloadCompressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 3, 1, 1, 10),
    _QtechfrMapPayloadCompressType_Type()
)
qtechfrMapPayloadCompressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrMapPayloadCompressType.setStatus("current")
_QtechfrSvcObjs_ObjectIdentity = ObjectIdentity
qtechfrSvcObjs = _QtechfrSvcObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4)
)
_QtechfrSvcTable_Object = MibTable
qtechfrSvcTable = _QtechfrSvcTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4, 1)
)
if mibBuilder.loadTexts:
    qtechfrSvcTable.setStatus("current")
_QtechfrSvcEntry_Object = MibTableRow
qtechfrSvcEntry = _QtechfrSvcEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4, 1, 1)
)
qtechfrSvcEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    qtechfrSvcEntry.setStatus("current")


class _QtechfrSvcAddrLocal_Type(OctetString):
    """Custom type qtechfrSvcAddrLocal based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_QtechfrSvcAddrLocal_Type.__name__ = "OctetString"
_QtechfrSvcAddrLocal_Object = MibTableColumn
qtechfrSvcAddrLocal = _QtechfrSvcAddrLocal_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4, 1, 1, 1),
    _QtechfrSvcAddrLocal_Type()
)
qtechfrSvcAddrLocal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrSvcAddrLocal.setStatus("current")


class _QtechfrSvcAddrRemote_Type(OctetString):
    """Custom type qtechfrSvcAddrRemote based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_QtechfrSvcAddrRemote_Type.__name__ = "OctetString"
_QtechfrSvcAddrRemote_Object = MibTableColumn
qtechfrSvcAddrRemote = _QtechfrSvcAddrRemote_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4, 1, 1, 2),
    _QtechfrSvcAddrRemote_Type()
)
qtechfrSvcAddrRemote.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrSvcAddrRemote.setStatus("current")


class _QtechfrSvcThroughputIn_Type(Integer32):
    """Custom type qtechfrSvcThroughputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_QtechfrSvcThroughputIn_Type.__name__ = "Integer32"
_QtechfrSvcThroughputIn_Object = MibTableColumn
qtechfrSvcThroughputIn = _QtechfrSvcThroughputIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4, 1, 1, 3),
    _QtechfrSvcThroughputIn_Type()
)
qtechfrSvcThroughputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrSvcThroughputIn.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrSvcThroughputIn.setUnits("bits per second")


class _QtechfrSvcMinThruputOut_Type(Integer32):
    """Custom type qtechfrSvcMinThruputOut based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_QtechfrSvcMinThruputOut_Type.__name__ = "Integer32"
_QtechfrSvcMinThruputOut_Object = MibTableColumn
qtechfrSvcMinThruputOut = _QtechfrSvcMinThruputOut_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4, 1, 1, 4),
    _QtechfrSvcMinThruputOut_Type()
)
qtechfrSvcMinThruputOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrSvcMinThruputOut.setStatus("deprecated")
if mibBuilder.loadTexts:
    qtechfrSvcMinThruputOut.setUnits("bits per second")


class _QtechfrSvcMinThruputIn_Type(Integer32):
    """Custom type qtechfrSvcMinThruputIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_QtechfrSvcMinThruputIn_Type.__name__ = "Integer32"
_QtechfrSvcMinThruputIn_Object = MibTableColumn
qtechfrSvcMinThruputIn = _QtechfrSvcMinThruputIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4, 1, 1, 5),
    _QtechfrSvcMinThruputIn_Type()
)
qtechfrSvcMinThruputIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrSvcMinThruputIn.setStatus("deprecated")
if mibBuilder.loadTexts:
    qtechfrSvcMinThruputIn.setUnits("bits per second")


class _QtechfrSvcCommitBurstIn_Type(Integer32):
    """Custom type qtechfrSvcCommitBurstIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 1544000),
    )


_QtechfrSvcCommitBurstIn_Type.__name__ = "Integer32"
_QtechfrSvcCommitBurstIn_Object = MibTableColumn
qtechfrSvcCommitBurstIn = _QtechfrSvcCommitBurstIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4, 1, 1, 6),
    _QtechfrSvcCommitBurstIn_Type()
)
qtechfrSvcCommitBurstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrSvcCommitBurstIn.setStatus("current")


class _QtechfrSvcExcessBurstIn_Type(Integer32):
    """Custom type qtechfrSvcExcessBurstIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(9600, 2440000),
    )


_QtechfrSvcExcessBurstIn_Type.__name__ = "Integer32"
_QtechfrSvcExcessBurstIn_Object = MibTableColumn
qtechfrSvcExcessBurstIn = _QtechfrSvcExcessBurstIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4, 1, 1, 7),
    _QtechfrSvcExcessBurstIn_Type()
)
qtechfrSvcExcessBurstIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrSvcExcessBurstIn.setStatus("current")
_QtechfrSvcIdleTime_Type = Integer32
_QtechfrSvcIdleTime_Object = MibTableColumn
qtechfrSvcIdleTime = _QtechfrSvcIdleTime_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 4, 1, 1, 8),
    _QtechfrSvcIdleTime_Type()
)
qtechfrSvcIdleTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrSvcIdleTime.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrSvcIdleTime.setUnits("seconds")
_QtechfrElmiObjs_ObjectIdentity = ObjectIdentity
qtechfrElmiObjs = _QtechfrElmiObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5)
)
_QtechfrElmiIpAddr_Type = IpAddress
_QtechfrElmiIpAddr_Object = MibScalar
qtechfrElmiIpAddr = _QtechfrElmiIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 1),
    _QtechfrElmiIpAddr_Type()
)
qtechfrElmiIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrElmiIpAddr.setStatus("current")
_QtechfrElmiTable_Object = MibTable
qtechfrElmiTable = _QtechfrElmiTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 2)
)
if mibBuilder.loadTexts:
    qtechfrElmiTable.setStatus("current")
_QtechfrElmiEntry_Object = MibTableRow
qtechfrElmiEntry = _QtechfrElmiEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 2, 1)
)
qtechfrElmiEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qtechfrElmiEntry.setStatus("current")


class _QtechfrElmiLinkStatus_Type(Integer32):
    """Custom type qtechfrElmiLinkStatus based on Integer32"""
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


_QtechfrElmiLinkStatus_Type.__name__ = "Integer32"
_QtechfrElmiLinkStatus_Object = MibTableColumn
qtechfrElmiLinkStatus = _QtechfrElmiLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 2, 1, 1),
    _QtechfrElmiLinkStatus_Type()
)
qtechfrElmiLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrElmiLinkStatus.setStatus("current")


class _QtechfrElmiArStatus_Type(Integer32):
    """Custom type qtechfrElmiArStatus based on Integer32"""
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


_QtechfrElmiArStatus_Type.__name__ = "Integer32"
_QtechfrElmiArStatus_Object = MibTableColumn
qtechfrElmiArStatus = _QtechfrElmiArStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 2, 1, 2),
    _QtechfrElmiArStatus_Type()
)
qtechfrElmiArStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrElmiArStatus.setStatus("current")


class _QtechfrElmiRemoteStatus_Type(Integer32):
    """Custom type qtechfrElmiRemoteStatus based on Integer32"""
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


_QtechfrElmiRemoteStatus_Type.__name__ = "Integer32"
_QtechfrElmiRemoteStatus_Object = MibTableColumn
qtechfrElmiRemoteStatus = _QtechfrElmiRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 2, 1, 3),
    _QtechfrElmiRemoteStatus_Type()
)
qtechfrElmiRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrElmiRemoteStatus.setStatus("current")
_QtechfrElmiNeighborTable_Object = MibTable
qtechfrElmiNeighborTable = _QtechfrElmiNeighborTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 3)
)
if mibBuilder.loadTexts:
    qtechfrElmiNeighborTable.setStatus("current")
_QtechfrElmiNeighborEntry_Object = MibTableRow
qtechfrElmiNeighborEntry = _QtechfrElmiNeighborEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 3, 1)
)
qtechfrElmiNeighborEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    qtechfrElmiNeighborEntry.setStatus("current")


class _QtechfrElmiNeighborArStatus_Type(Integer32):
    """Custom type qtechfrElmiNeighborArStatus based on Integer32"""
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


_QtechfrElmiNeighborArStatus_Type.__name__ = "Integer32"
_QtechfrElmiNeighborArStatus_Object = MibTableColumn
qtechfrElmiNeighborArStatus = _QtechfrElmiNeighborArStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 3, 1, 1),
    _QtechfrElmiNeighborArStatus_Type()
)
qtechfrElmiNeighborArStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrElmiNeighborArStatus.setStatus("current")
_QtechfrElmiNeighborIpAddress_Type = IpAddress
_QtechfrElmiNeighborIpAddress_Object = MibTableColumn
qtechfrElmiNeighborIpAddress = _QtechfrElmiNeighborIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 3, 1, 2),
    _QtechfrElmiNeighborIpAddress_Type()
)
qtechfrElmiNeighborIpAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrElmiNeighborIpAddress.setStatus("current")
_QtechfrElmiNeighborIfIndex_Type = InterfaceIndex
_QtechfrElmiNeighborIfIndex_Object = MibTableColumn
qtechfrElmiNeighborIfIndex = _QtechfrElmiNeighborIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 3, 1, 3),
    _QtechfrElmiNeighborIfIndex_Type()
)
qtechfrElmiNeighborIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrElmiNeighborIfIndex.setStatus("current")
_QtechfrElmiNeighborVendorName_Type = DisplayString
_QtechfrElmiNeighborVendorName_Object = MibTableColumn
qtechfrElmiNeighborVendorName = _QtechfrElmiNeighborVendorName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 3, 1, 4),
    _QtechfrElmiNeighborVendorName_Type()
)
qtechfrElmiNeighborVendorName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrElmiNeighborVendorName.setStatus("current")
_QtechfrElmiNeighborPlatformName_Type = DisplayString
_QtechfrElmiNeighborPlatformName_Object = MibTableColumn
qtechfrElmiNeighborPlatformName = _QtechfrElmiNeighborPlatformName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 3, 1, 5),
    _QtechfrElmiNeighborPlatformName_Type()
)
qtechfrElmiNeighborPlatformName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrElmiNeighborPlatformName.setStatus("current")
_QtechfrElmiNeighborDeviceName_Type = DisplayString
_QtechfrElmiNeighborDeviceName_Object = MibTableColumn
qtechfrElmiNeighborDeviceName = _QtechfrElmiNeighborDeviceName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 5, 3, 1, 6),
    _QtechfrElmiNeighborDeviceName_Type()
)
qtechfrElmiNeighborDeviceName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrElmiNeighborDeviceName.setStatus("current")
_QtechfrFragObjs_ObjectIdentity = ObjectIdentity
qtechfrFragObjs = _QtechfrFragObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6)
)
_QtechfrFragTable_Object = MibTable
qtechfrFragTable = _QtechfrFragTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1)
)
if mibBuilder.loadTexts:
    qtechfrFragTable.setStatus("current")
_QtechfrFragEntry_Object = MibTableRow
qtechfrFragEntry = _QtechfrFragEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1)
)
qtechfrFragEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    qtechfrFragEntry.setStatus("current")


class _QtechfrFragSize_Type(Integer32):
    """Custom type qtechfrFragSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(16, 1600),
    )


_QtechfrFragSize_Type.__name__ = "Integer32"
_QtechfrFragSize_Object = MibTableColumn
qtechfrFragSize = _QtechfrFragSize_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 1),
    _QtechfrFragSize_Type()
)
qtechfrFragSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragSize.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragSize.setUnits("octets")
_QtechfrFragType_Type = DisplayString
_QtechfrFragType_Object = MibTableColumn
qtechfrFragType = _QtechfrFragType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 2),
    _QtechfrFragType_Type()
)
qtechfrFragType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragType.setStatus("current")
_QtechfrFragInPkts_Type = Counter32
_QtechfrFragInPkts_Object = MibTableColumn
qtechfrFragInPkts = _QtechfrFragInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 3),
    _QtechfrFragInPkts_Type()
)
qtechfrFragInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragInPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragInPkts.setUnits("packets")
_QtechfrFragOutPkts_Type = Counter32
_QtechfrFragOutPkts_Object = MibTableColumn
qtechfrFragOutPkts = _QtechfrFragOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 4),
    _QtechfrFragOutPkts_Type()
)
qtechfrFragOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragOutPkts.setUnits("packets")
_QtechfrFragInOctets_Type = Counter32
_QtechfrFragInOctets_Object = MibTableColumn
qtechfrFragInOctets = _QtechfrFragInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 5),
    _QtechfrFragInOctets_Type()
)
qtechfrFragInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragInOctets.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragInOctets.setUnits("octets")
_QtechfrFragOutOctets_Type = Counter32
_QtechfrFragOutOctets_Object = MibTableColumn
qtechfrFragOutOctets = _QtechfrFragOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 6),
    _QtechfrFragOutOctets_Type()
)
qtechfrFragOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragOutOctets.setUnits("octets")
_QtechfrFragNotInPkts_Type = Counter32
_QtechfrFragNotInPkts_Object = MibTableColumn
qtechfrFragNotInPkts = _QtechfrFragNotInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 7),
    _QtechfrFragNotInPkts_Type()
)
qtechfrFragNotInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragNotInPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragNotInPkts.setUnits("packets")
_QtechfrFragNotOutPkts_Type = Counter32
_QtechfrFragNotOutPkts_Object = MibTableColumn
qtechfrFragNotOutPkts = _QtechfrFragNotOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 8),
    _QtechfrFragNotOutPkts_Type()
)
qtechfrFragNotOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragNotOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragNotOutPkts.setUnits("packets")
_QtechfrFragNotInOctets_Type = Counter32
_QtechfrFragNotInOctets_Object = MibTableColumn
qtechfrFragNotInOctets = _QtechfrFragNotInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 9),
    _QtechfrFragNotInOctets_Type()
)
qtechfrFragNotInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragNotInOctets.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragNotInOctets.setUnits("octets")
_QtechfrFragNotOutOctets_Type = Counter32
_QtechfrFragNotOutOctets_Object = MibTableColumn
qtechfrFragNotOutOctets = _QtechfrFragNotOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 10),
    _QtechfrFragNotOutOctets_Type()
)
qtechfrFragNotOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragNotOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragNotOutOctets.setUnits("octets")
_QtechfrFragAssembledInPkts_Type = Counter32
_QtechfrFragAssembledInPkts_Object = MibTableColumn
qtechfrFragAssembledInPkts = _QtechfrFragAssembledInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 11),
    _QtechfrFragAssembledInPkts_Type()
)
qtechfrFragAssembledInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragAssembledInPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragAssembledInPkts.setUnits("packets")
_QtechfrFragAssembledInOctets_Type = Counter32
_QtechfrFragAssembledInOctets_Object = MibTableColumn
qtechfrFragAssembledInOctets = _QtechfrFragAssembledInOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 12),
    _QtechfrFragAssembledInOctets_Type()
)
qtechfrFragAssembledInOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragAssembledInOctets.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragAssembledInOctets.setUnits("octets")
_QtechfrFragPreOutPkts_Type = Counter32
_QtechfrFragPreOutPkts_Object = MibTableColumn
qtechfrFragPreOutPkts = _QtechfrFragPreOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 13),
    _QtechfrFragPreOutPkts_Type()
)
qtechfrFragPreOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragPreOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragPreOutPkts.setUnits("packets")
_QtechfrFragPreOutOctets_Type = Counter32
_QtechfrFragPreOutOctets_Object = MibTableColumn
qtechfrFragPreOutOctets = _QtechfrFragPreOutOctets_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 14),
    _QtechfrFragPreOutOctets_Type()
)
qtechfrFragPreOutOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragPreOutOctets.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragPreOutOctets.setUnits("octets")
_QtechfrFragDroppedReAssembledInPkts_Type = Counter32
_QtechfrFragDroppedReAssembledInPkts_Object = MibTableColumn
qtechfrFragDroppedReAssembledInPkts = _QtechfrFragDroppedReAssembledInPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 15),
    _QtechfrFragDroppedReAssembledInPkts_Type()
)
qtechfrFragDroppedReAssembledInPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragDroppedReAssembledInPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragDroppedReAssembledInPkts.setUnits("packets")
_QtechfrFragDroppedFragmentedOutPkts_Type = Counter32
_QtechfrFragDroppedFragmentedOutPkts_Object = MibTableColumn
qtechfrFragDroppedFragmentedOutPkts = _QtechfrFragDroppedFragmentedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 16),
    _QtechfrFragDroppedFragmentedOutPkts_Type()
)
qtechfrFragDroppedFragmentedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragDroppedFragmentedOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragDroppedFragmentedOutPkts.setUnits("packets")


class _QtechfrFragTimeoutsIn_Type(Integer32):
    """Custom type qtechfrFragTimeoutsIn based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_QtechfrFragTimeoutsIn_Type.__name__ = "Integer32"
_QtechfrFragTimeoutsIn_Object = MibTableColumn
qtechfrFragTimeoutsIn = _QtechfrFragTimeoutsIn_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 17),
    _QtechfrFragTimeoutsIn_Type()
)
qtechfrFragTimeoutsIn.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragTimeoutsIn.setStatus("current")
_QtechfrFragOutOfSeqFragPkts_Type = Counter32
_QtechfrFragOutOfSeqFragPkts_Object = MibTableColumn
qtechfrFragOutOfSeqFragPkts = _QtechfrFragOutOfSeqFragPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 18),
    _QtechfrFragOutOfSeqFragPkts_Type()
)
qtechfrFragOutOfSeqFragPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragOutOfSeqFragPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragOutOfSeqFragPkts.setUnits("packets")
_QtechfrFragUnexpectedBBitSetPkts_Type = Counter32
_QtechfrFragUnexpectedBBitSetPkts_Object = MibTableColumn
qtechfrFragUnexpectedBBitSetPkts = _QtechfrFragUnexpectedBBitSetPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 19),
    _QtechfrFragUnexpectedBBitSetPkts_Type()
)
qtechfrFragUnexpectedBBitSetPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragUnexpectedBBitSetPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragUnexpectedBBitSetPkts.setUnits("packets")
_QtechfrFragSeqMissedPkts_Type = Counter32
_QtechfrFragSeqMissedPkts_Object = MibTableColumn
qtechfrFragSeqMissedPkts = _QtechfrFragSeqMissedPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 20),
    _QtechfrFragSeqMissedPkts_Type()
)
qtechfrFragSeqMissedPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragSeqMissedPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragSeqMissedPkts.setUnits("packets")
_QtechfrFragInterleavedOutPkts_Type = Counter32
_QtechfrFragInterleavedOutPkts_Object = MibTableColumn
qtechfrFragInterleavedOutPkts = _QtechfrFragInterleavedOutPkts_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 6, 1, 1, 21),
    _QtechfrFragInterleavedOutPkts_Type()
)
qtechfrFragInterleavedOutPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrFragInterleavedOutPkts.setStatus("current")
if mibBuilder.loadTexts:
    qtechfrFragInterleavedOutPkts.setUnits("packets")
_QtechfrConnectionObjs_ObjectIdentity = ObjectIdentity
qtechfrConnectionObjs = _QtechfrConnectionObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7)
)
_QtechfrConnectionTable_Object = MibTable
qtechfrConnectionTable = _QtechfrConnectionTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1)
)
if mibBuilder.loadTexts:
    qtechfrConnectionTable.setStatus("current")
_QtechfrConnectionEntry_Object = MibTableRow
qtechfrConnectionEntry = _QtechfrConnectionEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1)
)
qtechfrConnectionEntry.setIndexNames(
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitIfIndex"),
    (0, "FRAME-RELAY-DTE-MIB", "frCircuitDlci"),
)
if mibBuilder.loadTexts:
    qtechfrConnectionEntry.setStatus("current")
_QtechfrConnName_Type = DisplayString
_QtechfrConnName_Object = MibTableColumn
qtechfrConnName = _QtechfrConnName_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 1),
    _QtechfrConnName_Type()
)
qtechfrConnName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnName.setStatus("current")


class _QtechfrConnID_Type(Integer32):
    """Custom type qtechfrConnID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_QtechfrConnID_Type.__name__ = "Integer32"
_QtechfrConnID_Object = MibTableColumn
qtechfrConnID = _QtechfrConnID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 2),
    _QtechfrConnID_Type()
)
qtechfrConnID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnID.setStatus("current")
_QtechfrConnState_Type = DisplayString
_QtechfrConnState_Object = MibTableColumn
qtechfrConnState = _QtechfrConnState_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 3),
    _QtechfrConnState_Type()
)
qtechfrConnState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnState.setStatus("current")
_QtechfrConnSegment1Name_Type = DisplayString
_QtechfrConnSegment1Name_Object = MibTableColumn
qtechfrConnSegment1Name = _QtechfrConnSegment1Name_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 4),
    _QtechfrConnSegment1Name_Type()
)
qtechfrConnSegment1Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnSegment1Name.setStatus("current")
_QtechfrConnSegment1VCGroup_Type = DisplayString
_QtechfrConnSegment1VCGroup_Object = MibTableColumn
qtechfrConnSegment1VCGroup = _QtechfrConnSegment1VCGroup_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 5),
    _QtechfrConnSegment1VCGroup_Type()
)
qtechfrConnSegment1VCGroup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnSegment1VCGroup.setStatus("current")
_QtechfrConnSegment1Dlci_Type = DlciNumber
_QtechfrConnSegment1Dlci_Object = MibTableColumn
qtechfrConnSegment1Dlci = _QtechfrConnSegment1Dlci_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 6),
    _QtechfrConnSegment1Dlci_Type()
)
qtechfrConnSegment1Dlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnSegment1Dlci.setStatus("current")
_QtechfrConnSegment2Name_Type = DisplayString
_QtechfrConnSegment2Name_Object = MibTableColumn
qtechfrConnSegment2Name = _QtechfrConnSegment2Name_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 7),
    _QtechfrConnSegment2Name_Type()
)
qtechfrConnSegment2Name.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnSegment2Name.setStatus("current")


class _QtechfrConnSegment2Vpi_Type(Integer32):
    """Custom type qtechfrConnSegment2Vpi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_QtechfrConnSegment2Vpi_Type.__name__ = "Integer32"
_QtechfrConnSegment2Vpi_Object = MibTableColumn
qtechfrConnSegment2Vpi = _QtechfrConnSegment2Vpi_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 8),
    _QtechfrConnSegment2Vpi_Type()
)
qtechfrConnSegment2Vpi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnSegment2Vpi.setStatus("current")


class _QtechfrConnSegment2Vci_Type(Integer32):
    """Custom type qtechfrConnSegment2Vci based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_QtechfrConnSegment2Vci_Type.__name__ = "Integer32"
_QtechfrConnSegment2Vci_Object = MibTableColumn
qtechfrConnSegment2Vci = _QtechfrConnSegment2Vci_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 9),
    _QtechfrConnSegment2Vci_Type()
)
qtechfrConnSegment2Vci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnSegment2Vci.setStatus("current")


class _QtechfrConnServiceTranslation_Type(Integer32):
    """Custom type qtechfrConnServiceTranslation based on Integer32"""
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


_QtechfrConnServiceTranslation_Type.__name__ = "Integer32"
_QtechfrConnServiceTranslation_Object = MibTableColumn
qtechfrConnServiceTranslation = _QtechfrConnServiceTranslation_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 10),
    _QtechfrConnServiceTranslation_Type()
)
qtechfrConnServiceTranslation.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnServiceTranslation.setStatus("current")
_QtechfrConnFrSscsDlci_Type = DlciNumber
_QtechfrConnFrSscsDlci_Object = MibTableColumn
qtechfrConnFrSscsDlci = _QtechfrConnFrSscsDlci_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 11),
    _QtechfrConnFrSscsDlci_Type()
)
qtechfrConnFrSscsDlci.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnFrSscsDlci.setStatus("current")


class _QtechfrConnEfciBit_Type(Integer32):
    """Custom type qtechfrConnEfciBit based on Integer32"""
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


_QtechfrConnEfciBit_Type.__name__ = "Integer32"
_QtechfrConnEfciBit_Object = MibTableColumn
qtechfrConnEfciBit = _QtechfrConnEfciBit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 12),
    _QtechfrConnEfciBit_Type()
)
qtechfrConnEfciBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnEfciBit.setStatus("current")


class _QtechfrConnDeBit_Type(Integer32):
    """Custom type qtechfrConnDeBit based on Integer32"""
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


_QtechfrConnDeBit_Type.__name__ = "Integer32"
_QtechfrConnDeBit_Object = MibTableColumn
qtechfrConnDeBit = _QtechfrConnDeBit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 13),
    _QtechfrConnDeBit_Type()
)
qtechfrConnDeBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnDeBit.setStatus("current")


class _QtechfrConnClpBit_Type(Integer32):
    """Custom type qtechfrConnClpBit based on Integer32"""
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


_QtechfrConnClpBit_Type.__name__ = "Integer32"
_QtechfrConnClpBit_Object = MibTableColumn
qtechfrConnClpBit = _QtechfrConnClpBit_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 1, 7, 1, 1, 14),
    _QtechfrConnClpBit_Type()
)
qtechfrConnClpBit.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechfrConnClpBit.setStatus("current")
_QtechFrMIBConformance_ObjectIdentity = ObjectIdentity
qtechFrMIBConformance = _QtechFrMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3)
)
_QtechFrMIBCompliances_ObjectIdentity = ObjectIdentity
qtechFrMIBCompliances = _QtechFrMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 1)
)
_QtechFrMIBGroups_ObjectIdentity = ObjectIdentity
qtechFrMIBGroups = _QtechFrMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2)
)
frDlcmiEntry.registerAugmentions(
    ("QTECH-FRAME-RELAY-MIB",
     "qtechfrLmiEntry")
)
qtechfrLmiEntry.setIndexNames(*frDlcmiEntry.getIndexNames())
frCircuitEntry.registerAugmentions(
    ("QTECH-FRAME-RELAY-MIB",
     "qtechfrCircuitEntry")
)
qtechfrCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())
frCircuitEntry.registerAugmentions(
    ("QTECH-FRAME-RELAY-MIB",
     "qtechfrExtCircuitEntry")
)
qtechfrExtCircuitEntry.setIndexNames(*frCircuitEntry.getIndexNames())

# Managed Objects groups

qtechFrMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 1)
)
qtechFrMIBGroup.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrLmiLinkstatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiLinkType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiEnquiryIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiEnquiryOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiUpdateStatusIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiUpdateStatusOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusTimeouts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusEnqTimeouts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiN392Dce"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiN393Dce"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiT392Dce"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitDEins"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitDEouts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitDropPktsOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitIfName"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitIfType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitSubifIndex"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMapStatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitCreateType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMulticast"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitRoutedDlci"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitRoutedIf"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapIndex"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapProtocol"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapAddress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapEncaps"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapBroadcast"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapPayloadCompress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapTcpHdrCompress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcAddrLocal"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcAddrRemote"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcThroughputIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcMinThruputOut"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcMinThruputIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcCommitBurstIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcExcessBurstIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    qtechFrMIBGroup.setStatus("deprecated")

qtechFrMIBGroupRev1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 2)
)
qtechFrMIBGroupRev1.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrLmiLinkstatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiLinkType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiEnquiryIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiEnquiryOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiUpdateStatusIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiUpdateStatusOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusTimeouts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusEnqTimeouts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiN392Dce"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiN393Dce"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiT392Dce"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitDEins"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitDEouts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitDropPktsOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitIfName"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitIfType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitSubifIndex"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMapStatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitCreateType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMulticast"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitRoutedDlci"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitRoutedIf"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitUncompressIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitUncompressOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapIndex"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapProtocol"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapAddress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapEncaps"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapBroadcast"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapTcpHdrCompress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapRtpHdrCompress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapPayloadCompressType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcAddrLocal"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcAddrRemote"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcThroughputIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcMinThruputOut"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcMinThruputIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcCommitBurstIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcExcessBurstIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    qtechFrMIBGroupRev1.setStatus("deprecated")

qtechFrLmiMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 3)
)
qtechFrLmiMIBGroup.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrLmiLinkstatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiLinkType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiEnquiryIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiEnquiryOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiUpdateStatusIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiUpdateStatusOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusTimeouts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiStatusEnqTimeouts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiN392Dce"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiN393Dce"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrLmiT392Dce"))
)
if mibBuilder.loadTexts:
    qtechFrLmiMIBGroup.setStatus("current")

qtechFrCircuitMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 4)
)
qtechFrCircuitMIBGroup.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitDEins"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitDEouts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitDropPktsOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrCircuitType"))
)
if mibBuilder.loadTexts:
    qtechFrCircuitMIBGroup.setStatus("current")

qtechExtCircuitMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 5)
)
qtechExtCircuitMIBGroup.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitIfName"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitIfType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitSubifIndex"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMapStatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitCreateType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMulticast"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitRoutedDlci"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitRoutedIf"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitUncompressIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitUncompressOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitFECNOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitBECNOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMinThruputOut"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMinThruputIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitBcastPktOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitBcastByteOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitBandwidth"))
)
if mibBuilder.loadTexts:
    qtechExtCircuitMIBGroup.setStatus("deprecated")

qtechFrTsMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 6)
)
qtechFrTsMIBGroup.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitShapeByteLimit"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitShapeInterval"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitShapeByteIncrement"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitShapePkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitShapeBytes"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitShapePktsDelay"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitShapeBytesDelay"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitShapeActive"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitShapeAdapting"))
)
if mibBuilder.loadTexts:
    qtechFrTsMIBGroup.setStatus("current")

qtechFrMapMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 7)
)
qtechFrMapMIBGroup.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrMapIndex"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapProtocol"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapAddress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapEncaps"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapBroadcast"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapTcpHdrCompress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapRtpHdrCompress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrMapPayloadCompressType"))
)
if mibBuilder.loadTexts:
    qtechFrMapMIBGroup.setStatus("current")

qtechFrSvcMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 8)
)
qtechFrSvcMIBGroup.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrSvcAddrLocal"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcAddrRemote"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcThroughputIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcCommitBurstIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcExcessBurstIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrSvcIdleTime"))
)
if mibBuilder.loadTexts:
    qtechFrSvcMIBGroup.setStatus("current")

qtechFrElmiMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 9)
)
qtechFrElmiMIBGroup.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrElmiIpAddr"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiArStatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiRemoteStatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborArStatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborIpAddress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborIfIndex"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborVendorName"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborPlatformName"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborDeviceName"))
)
if mibBuilder.loadTexts:
    qtechFrElmiMIBGroup.setStatus("deprecated")

qtechFrElmiMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 10)
)
qtechFrElmiMIBGroup1.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrElmiIpAddr"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiArStatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiRemoteStatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborArStatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborIpAddress"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborIfIndex"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborVendorName"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborPlatformName"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiNeighborDeviceName"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrElmiLinkStatus"))
)
if mibBuilder.loadTexts:
    qtechFrElmiMIBGroup1.setStatus("current")

qtechFrFragMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 11)
)
qtechFrFragMIBGroup.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrFragSize"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragInPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragOutPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragInOctets"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragOutOctets"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragNotInPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragNotOutPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragNotInOctets"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragNotOutOctets"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragAssembledInPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragAssembledInOctets"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragPreOutPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragPreOutOctets"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragDroppedReAssembledInPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragDroppedFragmentedOutPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragTimeoutsIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragOutOfSeqFragPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragUnexpectedBBitSetPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragSeqMissedPkts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrFragInterleavedOutPkts"))
)
if mibBuilder.loadTexts:
    qtechFrFragMIBGroup.setStatus("current")

qtechFrConnMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 12)
)
qtechFrConnMIBGroup.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrConnName"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnID"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnState"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnSegment1Name"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnSegment1VCGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnSegment1Dlci"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnSegment2Name"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnSegment2Vpi"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnSegment2Vci"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnServiceTranslation"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnFrSscsDlci"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnEfciBit"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnDeBit"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrConnClpBit"))
)
if mibBuilder.loadTexts:
    qtechFrConnMIBGroup.setStatus("current")

qtechExtCircuitMIBGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 2, 13)
)
qtechExtCircuitMIBGroup1.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitIfName"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitIfType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitSubifIndex"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMapStatus"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitCreateType"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMulticast"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitRoutedDlci"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitRoutedIf"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitUncompressIns"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitUncompressOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitFECNOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitBECNOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMinThruputOut"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitMinThruputIn"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitBcastPktOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitBcastByteOuts"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitBandwidth"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitTxDataRate"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitTxPktRate"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitRcvDataRate"),
        ("QTECH-FRAME-RELAY-MIB", "qtechfrExtCircuitRcvPktRate"))
)
if mibBuilder.loadTexts:
    qtechExtCircuitMIBGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

qtechFrMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 1, 1)
)
qtechFrMIBCompliance.setObjects(
    ("QTECH-FRAME-RELAY-MIB", "qtechFrMIBGroup")
)
if mibBuilder.loadTexts:
    qtechFrMIBCompliance.setStatus(
        "obsolete"
    )

qtechFrMIBCompliancesRev1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 1, 2)
)
qtechFrMIBCompliancesRev1.setObjects(
    ("QTECH-FRAME-RELAY-MIB", "qtechFrMIBGroupRev1")
)
if mibBuilder.loadTexts:
    qtechFrMIBCompliancesRev1.setStatus(
        "obsolete"
    )

qtechFrMIBCompliancesRev2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 1, 3)
)
qtechFrMIBCompliancesRev2.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechFrLmiMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrCircuitMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechExtCircuitMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrTsMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrMapMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrSvcMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechFrMIBCompliancesRev2.setStatus(
        "obsolete"
    )

qtechFrMIBCompliancesRev3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 1, 4)
)
qtechFrMIBCompliancesRev3.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechFrLmiMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrCircuitMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechExtCircuitMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrTsMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrMapMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrSvcMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrElmiMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechFrMIBCompliancesRev3.setStatus(
        "deprecated"
    )

qtechFrMIBCompliancesRev4 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 50, 3, 1, 5)
)
qtechFrMIBCompliancesRev4.setObjects(
      *(("QTECH-FRAME-RELAY-MIB", "qtechFrLmiMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrCircuitMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechExtCircuitMIBGroup1"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrTsMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrMapMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrSvcMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrElmiMIBGroup1"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrFragMIBGroup"),
        ("QTECH-FRAME-RELAY-MIB", "qtechFrConnMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechFrMIBCompliancesRev4.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-FRAME-RELAY-MIB",
    **{"DlciNumber": DlciNumber,
       "QtechfrMapProtocols": QtechfrMapProtocols,
       "qtechFrameRelayMIB": qtechFrameRelayMIB,
       "qtechFrMIBObjects": qtechFrMIBObjects,
       "qtechfrLmiObjs": qtechfrLmiObjs,
       "qtechfrLmiTable": qtechfrLmiTable,
       "qtechfrLmiEntry": qtechfrLmiEntry,
       "qtechfrLmiLinkstatus": qtechfrLmiLinkstatus,
       "qtechfrLmiLinkType": qtechfrLmiLinkType,
       "qtechfrLmiEnquiryIns": qtechfrLmiEnquiryIns,
       "qtechfrLmiEnquiryOuts": qtechfrLmiEnquiryOuts,
       "qtechfrLmiStatusIns": qtechfrLmiStatusIns,
       "qtechfrLmiStatusOuts": qtechfrLmiStatusOuts,
       "qtechfrLmiUpdateStatusIns": qtechfrLmiUpdateStatusIns,
       "qtechfrLmiUpdateStatusOuts": qtechfrLmiUpdateStatusOuts,
       "qtechfrLmiStatusTimeouts": qtechfrLmiStatusTimeouts,
       "qtechfrLmiStatusEnqTimeouts": qtechfrLmiStatusEnqTimeouts,
       "qtechfrLmiN392Dce": qtechfrLmiN392Dce,
       "qtechfrLmiN393Dce": qtechfrLmiN393Dce,
       "qtechfrLmiT392Dce": qtechfrLmiT392Dce,
       "qtechfrCircuitObjs": qtechfrCircuitObjs,
       "qtechfrCircuitTable": qtechfrCircuitTable,
       "qtechfrCircuitEntry": qtechfrCircuitEntry,
       "qtechfrCircuitDEins": qtechfrCircuitDEins,
       "qtechfrCircuitDEouts": qtechfrCircuitDEouts,
       "qtechfrCircuitDropPktsOuts": qtechfrCircuitDropPktsOuts,
       "qtechfrCircuitType": qtechfrCircuitType,
       "qtechfrExtCircuitTable": qtechfrExtCircuitTable,
       "qtechfrExtCircuitEntry": qtechfrExtCircuitEntry,
       "qtechfrExtCircuitIfName": qtechfrExtCircuitIfName,
       "qtechfrExtCircuitIfType": qtechfrExtCircuitIfType,
       "qtechfrExtCircuitSubifIndex": qtechfrExtCircuitSubifIndex,
       "qtechfrExtCircuitMapStatus": qtechfrExtCircuitMapStatus,
       "qtechfrExtCircuitCreateType": qtechfrExtCircuitCreateType,
       "qtechfrExtCircuitMulticast": qtechfrExtCircuitMulticast,
       "qtechfrExtCircuitRoutedDlci": qtechfrExtCircuitRoutedDlci,
       "qtechfrExtCircuitRoutedIf": qtechfrExtCircuitRoutedIf,
       "qtechfrExtCircuitUncompressIns": qtechfrExtCircuitUncompressIns,
       "qtechfrExtCircuitUncompressOuts": qtechfrExtCircuitUncompressOuts,
       "qtechfrExtCircuitFECNOuts": qtechfrExtCircuitFECNOuts,
       "qtechfrExtCircuitBECNOuts": qtechfrExtCircuitBECNOuts,
       "qtechfrExtCircuitMinThruputOut": qtechfrExtCircuitMinThruputOut,
       "qtechfrExtCircuitMinThruputIn": qtechfrExtCircuitMinThruputIn,
       "qtechfrExtCircuitBcastPktOuts": qtechfrExtCircuitBcastPktOuts,
       "qtechfrExtCircuitBcastByteOuts": qtechfrExtCircuitBcastByteOuts,
       "qtechfrExtCircuitBandwidth": qtechfrExtCircuitBandwidth,
       "qtechfrExtCircuitShapeByteLimit": qtechfrExtCircuitShapeByteLimit,
       "qtechfrExtCircuitShapeInterval": qtechfrExtCircuitShapeInterval,
       "qtechfrExtCircuitShapeByteIncrement": qtechfrExtCircuitShapeByteIncrement,
       "qtechfrExtCircuitShapePkts": qtechfrExtCircuitShapePkts,
       "qtechfrExtCircuitShapeBytes": qtechfrExtCircuitShapeBytes,
       "qtechfrExtCircuitShapePktsDelay": qtechfrExtCircuitShapePktsDelay,
       "qtechfrExtCircuitShapeBytesDelay": qtechfrExtCircuitShapeBytesDelay,
       "qtechfrExtCircuitShapeActive": qtechfrExtCircuitShapeActive,
       "qtechfrExtCircuitShapeAdapting": qtechfrExtCircuitShapeAdapting,
       "qtechfrExtCircuitTxDataRate": qtechfrExtCircuitTxDataRate,
       "qtechfrExtCircuitTxPktRate": qtechfrExtCircuitTxPktRate,
       "qtechfrExtCircuitRcvDataRate": qtechfrExtCircuitRcvDataRate,
       "qtechfrExtCircuitRcvPktRate": qtechfrExtCircuitRcvPktRate,
       "qtechfrMapObjs": qtechfrMapObjs,
       "qtechfrMapTable": qtechfrMapTable,
       "qtechfrMapEntry": qtechfrMapEntry,
       "qtechfrMapIndex": qtechfrMapIndex,
       "qtechfrMapProtocol": qtechfrMapProtocol,
       "qtechfrMapAddress": qtechfrMapAddress,
       "qtechfrMapType": qtechfrMapType,
       "qtechfrMapEncaps": qtechfrMapEncaps,
       "qtechfrMapBroadcast": qtechfrMapBroadcast,
       "qtechfrMapPayloadCompress": qtechfrMapPayloadCompress,
       "qtechfrMapTcpHdrCompress": qtechfrMapTcpHdrCompress,
       "qtechfrMapRtpHdrCompress": qtechfrMapRtpHdrCompress,
       "qtechfrMapPayloadCompressType": qtechfrMapPayloadCompressType,
       "qtechfrSvcObjs": qtechfrSvcObjs,
       "qtechfrSvcTable": qtechfrSvcTable,
       "qtechfrSvcEntry": qtechfrSvcEntry,
       "qtechfrSvcAddrLocal": qtechfrSvcAddrLocal,
       "qtechfrSvcAddrRemote": qtechfrSvcAddrRemote,
       "qtechfrSvcThroughputIn": qtechfrSvcThroughputIn,
       "qtechfrSvcMinThruputOut": qtechfrSvcMinThruputOut,
       "qtechfrSvcMinThruputIn": qtechfrSvcMinThruputIn,
       "qtechfrSvcCommitBurstIn": qtechfrSvcCommitBurstIn,
       "qtechfrSvcExcessBurstIn": qtechfrSvcExcessBurstIn,
       "qtechfrSvcIdleTime": qtechfrSvcIdleTime,
       "qtechfrElmiObjs": qtechfrElmiObjs,
       "qtechfrElmiIpAddr": qtechfrElmiIpAddr,
       "qtechfrElmiTable": qtechfrElmiTable,
       "qtechfrElmiEntry": qtechfrElmiEntry,
       "qtechfrElmiLinkStatus": qtechfrElmiLinkStatus,
       "qtechfrElmiArStatus": qtechfrElmiArStatus,
       "qtechfrElmiRemoteStatus": qtechfrElmiRemoteStatus,
       "qtechfrElmiNeighborTable": qtechfrElmiNeighborTable,
       "qtechfrElmiNeighborEntry": qtechfrElmiNeighborEntry,
       "qtechfrElmiNeighborArStatus": qtechfrElmiNeighborArStatus,
       "qtechfrElmiNeighborIpAddress": qtechfrElmiNeighborIpAddress,
       "qtechfrElmiNeighborIfIndex": qtechfrElmiNeighborIfIndex,
       "qtechfrElmiNeighborVendorName": qtechfrElmiNeighborVendorName,
       "qtechfrElmiNeighborPlatformName": qtechfrElmiNeighborPlatformName,
       "qtechfrElmiNeighborDeviceName": qtechfrElmiNeighborDeviceName,
       "qtechfrFragObjs": qtechfrFragObjs,
       "qtechfrFragTable": qtechfrFragTable,
       "qtechfrFragEntry": qtechfrFragEntry,
       "qtechfrFragSize": qtechfrFragSize,
       "qtechfrFragType": qtechfrFragType,
       "qtechfrFragInPkts": qtechfrFragInPkts,
       "qtechfrFragOutPkts": qtechfrFragOutPkts,
       "qtechfrFragInOctets": qtechfrFragInOctets,
       "qtechfrFragOutOctets": qtechfrFragOutOctets,
       "qtechfrFragNotInPkts": qtechfrFragNotInPkts,
       "qtechfrFragNotOutPkts": qtechfrFragNotOutPkts,
       "qtechfrFragNotInOctets": qtechfrFragNotInOctets,
       "qtechfrFragNotOutOctets": qtechfrFragNotOutOctets,
       "qtechfrFragAssembledInPkts": qtechfrFragAssembledInPkts,
       "qtechfrFragAssembledInOctets": qtechfrFragAssembledInOctets,
       "qtechfrFragPreOutPkts": qtechfrFragPreOutPkts,
       "qtechfrFragPreOutOctets": qtechfrFragPreOutOctets,
       "qtechfrFragDroppedReAssembledInPkts": qtechfrFragDroppedReAssembledInPkts,
       "qtechfrFragDroppedFragmentedOutPkts": qtechfrFragDroppedFragmentedOutPkts,
       "qtechfrFragTimeoutsIn": qtechfrFragTimeoutsIn,
       "qtechfrFragOutOfSeqFragPkts": qtechfrFragOutOfSeqFragPkts,
       "qtechfrFragUnexpectedBBitSetPkts": qtechfrFragUnexpectedBBitSetPkts,
       "qtechfrFragSeqMissedPkts": qtechfrFragSeqMissedPkts,
       "qtechfrFragInterleavedOutPkts": qtechfrFragInterleavedOutPkts,
       "qtechfrConnectionObjs": qtechfrConnectionObjs,
       "qtechfrConnectionTable": qtechfrConnectionTable,
       "qtechfrConnectionEntry": qtechfrConnectionEntry,
       "qtechfrConnName": qtechfrConnName,
       "qtechfrConnID": qtechfrConnID,
       "qtechfrConnState": qtechfrConnState,
       "qtechfrConnSegment1Name": qtechfrConnSegment1Name,
       "qtechfrConnSegment1VCGroup": qtechfrConnSegment1VCGroup,
       "qtechfrConnSegment1Dlci": qtechfrConnSegment1Dlci,
       "qtechfrConnSegment2Name": qtechfrConnSegment2Name,
       "qtechfrConnSegment2Vpi": qtechfrConnSegment2Vpi,
       "qtechfrConnSegment2Vci": qtechfrConnSegment2Vci,
       "qtechfrConnServiceTranslation": qtechfrConnServiceTranslation,
       "qtechfrConnFrSscsDlci": qtechfrConnFrSscsDlci,
       "qtechfrConnEfciBit": qtechfrConnEfciBit,
       "qtechfrConnDeBit": qtechfrConnDeBit,
       "qtechfrConnClpBit": qtechfrConnClpBit,
       "qtechFrMIBConformance": qtechFrMIBConformance,
       "qtechFrMIBCompliances": qtechFrMIBCompliances,
       "qtechFrMIBCompliance": qtechFrMIBCompliance,
       "qtechFrMIBCompliancesRev1": qtechFrMIBCompliancesRev1,
       "qtechFrMIBCompliancesRev2": qtechFrMIBCompliancesRev2,
       "qtechFrMIBCompliancesRev3": qtechFrMIBCompliancesRev3,
       "qtechFrMIBCompliancesRev4": qtechFrMIBCompliancesRev4,
       "qtechFrMIBGroups": qtechFrMIBGroups,
       "qtechFrMIBGroup": qtechFrMIBGroup,
       "qtechFrMIBGroupRev1": qtechFrMIBGroupRev1,
       "qtechFrLmiMIBGroup": qtechFrLmiMIBGroup,
       "qtechFrCircuitMIBGroup": qtechFrCircuitMIBGroup,
       "qtechExtCircuitMIBGroup": qtechExtCircuitMIBGroup,
       "qtechFrTsMIBGroup": qtechFrTsMIBGroup,
       "qtechFrMapMIBGroup": qtechFrMapMIBGroup,
       "qtechFrSvcMIBGroup": qtechFrSvcMIBGroup,
       "qtechFrElmiMIBGroup": qtechFrElmiMIBGroup,
       "qtechFrElmiMIBGroup1": qtechFrElmiMIBGroup1,
       "qtechFrFragMIBGroup": qtechFrFragMIBGroup,
       "qtechFrConnMIBGroup": qtechFrConnMIBGroup,
       "qtechExtCircuitMIBGroup1": qtechExtCircuitMIBGroup1}
)
