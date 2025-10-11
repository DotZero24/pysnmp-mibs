# SNMP MIB module (NORTEL-OME40G-OM-COUNTS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NORTEL-OME40G-OM-COUNTS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:19:31 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(nnOme40G,) = mibBuilder.importSymbols(
    "NORTEL-OME40G-MIB",
    "nnOme40G")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nnOme40GOmCounts = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5)
)
if mibBuilder.loadTexts:
    nnOme40GOmCounts.setRevisions(
        ("2007-02-02 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Generic_ObjectIdentity = ObjectIdentity
generic = _Generic_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1)
)
_WanCountsTable_Object = MibTable
wanCountsTable = _WanCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 1)
)
if mibBuilder.loadTexts:
    wanCountsTable.setStatus("current")
_WanCountsEntry_Object = MibTableRow
wanCountsEntry = _WanCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 1, 1)
)
wanCountsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    wanCountsEntry.setStatus("current")
_WanINFRAMES_Type = Counter64
_WanINFRAMES_Object = MibTableColumn
wanINFRAMES = _WanINFRAMES_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 1, 1, 1),
    _WanINFRAMES_Type()
)
wanINFRAMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanINFRAMES.setStatus("current")
_WanINFRAMESERR_Type = Counter64
_WanINFRAMESERR_Object = MibTableColumn
wanINFRAMESERR = _WanINFRAMESERR_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 1, 1, 2),
    _WanINFRAMESERR_Type()
)
wanINFRAMESERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanINFRAMESERR.setStatus("current")
_WanINDFR_Type = Counter64
_WanINDFR_Object = MibTableColumn
wanINDFR = _WanINDFR_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 1, 1, 3),
    _WanINDFR_Type()
)
wanINDFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    wanINDFR.setStatus("current")
_EthCountsTable_Object = MibTable
ethCountsTable = _EthCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2)
)
if mibBuilder.loadTexts:
    ethCountsTable.setStatus("current")
_EthCountsEntry_Object = MibTableRow
ethCountsEntry = _EthCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1)
)
ethCountsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ethCountsEntry.setStatus("current")
_EthINFRAMES_Type = Counter64
_EthINFRAMES_Object = MibTableColumn
ethINFRAMES = _EthINFRAMES_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1, 1),
    _EthINFRAMES_Type()
)
ethINFRAMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethINFRAMES.setStatus("current")
_EthINFRAMESERR_Type = Counter64
_EthINFRAMESERR_Object = MibTableColumn
ethINFRAMESERR = _EthINFRAMESERR_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1, 2),
    _EthINFRAMESERR_Type()
)
ethINFRAMESERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethINFRAMESERR.setStatus("current")
_EthINDFR_Type = Counter64
_EthINDFR_Object = MibTableColumn
ethINDFR = _EthINDFR_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1, 3),
    _EthINDFR_Type()
)
ethINDFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethINDFR.setStatus("current")
_EthINFRAMESDISCS_Type = Counter64
_EthINFRAMESDISCS_Object = MibTableColumn
ethINFRAMESDISCS = _EthINFRAMESDISCS_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1, 4),
    _EthINFRAMESDISCS_Type()
)
ethINFRAMESDISCS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethINFRAMESDISCS.setStatus("current")
_EthOUTFRAMES_Type = Counter64
_EthOUTFRAMES_Object = MibTableColumn
ethOUTFRAMES = _EthOUTFRAMES_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1, 5),
    _EthOUTFRAMES_Type()
)
ethOUTFRAMES.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOUTFRAMES.setStatus("current")
_EthOUTFRAMESERR_Type = Counter64
_EthOUTFRAMESERR_Object = MibTableColumn
ethOUTFRAMESERR = _EthOUTFRAMESERR_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1, 6),
    _EthOUTFRAMESERR_Type()
)
ethOUTFRAMESERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOUTFRAMESERR.setStatus("current")
_EthINOCTETS_Type = Counter64
_EthINOCTETS_Object = MibTableColumn
ethINOCTETS = _EthINOCTETS_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1, 7),
    _EthINOCTETS_Type()
)
ethINOCTETS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethINOCTETS.setStatus("current")
_EthOUTOCTETS_Type = Counter64
_EthOUTOCTETS_Object = MibTableColumn
ethOUTOCTETS = _EthOUTOCTETS_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1, 8),
    _EthOUTOCTETS_Type()
)
ethOUTOCTETS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOUTOCTETS.setStatus("current")
_EthOUTDFR_Type = Counter64
_EthOUTDFR_Object = MibTableColumn
ethOUTDFR = _EthOUTDFR_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1, 9),
    _EthOUTDFR_Type()
)
ethOUTDFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOUTDFR.setStatus("current")
_EthOUTFRAMESDISCDS_Type = Counter64
_EthOUTFRAMESDISCDS_Object = MibTableColumn
ethOUTFRAMESDISCDS = _EthOUTFRAMESDISCDS_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 1, 2, 1, 10),
    _EthOUTFRAMESDISCDS_Type()
)
ethOUTFRAMESDISCDS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOUTFRAMESDISCDS.setStatus("current")
_Enet_ObjectIdentity = ObjectIdentity
enet = _Enet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2)
)
_EnetCountsTable_Object = MibTable
enetCountsTable = _EnetCountsTable_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2, 1)
)
if mibBuilder.loadTexts:
    enetCountsTable.setStatus("current")
_EnetCountsEntry_Object = MibTableRow
enetCountsEntry = _EnetCountsEntry_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2, 1, 1)
)
enetCountsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    enetCountsEntry.setStatus("current")
_EthFCSERR_Type = Counter64
_EthFCSERR_Object = MibTableColumn
ethFCSERR = _EthFCSERR_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2, 1, 1, 1),
    _EthFCSERR_Type()
)
ethFCSERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFCSERR.setStatus("current")
_EthJAB_Type = Counter64
_EthJAB_Object = MibTableColumn
ethJAB = _EthJAB_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2, 1, 1, 2),
    _EthJAB_Type()
)
ethJAB.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethJAB.setStatus("current")
_EthFRAG_Type = Counter64
_EthFRAG_Object = MibTableColumn
ethFRAG = _EthFRAG_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2, 1, 1, 3),
    _EthFRAG_Type()
)
ethFRAG.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFRAG.setStatus("current")
_EthFRTOOLONGS_Type = Counter64
_EthFRTOOLONGS_Object = MibTableColumn
ethFRTOOLONGS = _EthFRTOOLONGS_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2, 1, 1, 4),
    _EthFRTOOLONGS_Type()
)
ethFRTOOLONGS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFRTOOLONGS.setStatus("current")
_EthFRTOOSHORTS_Type = Counter64
_EthFRTOOSHORTS_Object = MibTableColumn
ethFRTOOSHORTS = _EthFRTOOSHORTS_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2, 1, 1, 5),
    _EthFRTOOSHORTS_Type()
)
ethFRTOOSHORTS.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethFRTOOSHORTS.setStatus("current")
_EthSYMBOLERR_Type = Counter64
_EthSYMBOLERR_Object = MibTableColumn
ethSYMBOLERR = _EthSYMBOLERR_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2, 1, 1, 6),
    _EthSYMBOLERR_Type()
)
ethSYMBOLERR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethSYMBOLERR.setStatus("current")
_EthINPAUSEFR_Type = Counter64
_EthINPAUSEFR_Object = MibTableColumn
ethINPAUSEFR = _EthINPAUSEFR_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2, 1, 1, 7),
    _EthINPAUSEFR_Type()
)
ethINPAUSEFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethINPAUSEFR.setStatus("current")
_EthOUTPAUSEFR_Type = Counter64
_EthOUTPAUSEFR_Object = MibTableColumn
ethOUTPAUSEFR = _EthOUTPAUSEFR_Object(
    (1, 3, 6, 1, 4, 1, 562, 68, 11, 3, 5, 2, 1, 1, 8),
    _EthOUTPAUSEFR_Type()
)
ethOUTPAUSEFR.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ethOUTPAUSEFR.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NORTEL-OME40G-OM-COUNTS-MIB",
    **{"nnOme40GOmCounts": nnOme40GOmCounts,
       "generic": generic,
       "wanCountsTable": wanCountsTable,
       "wanCountsEntry": wanCountsEntry,
       "wanINFRAMES": wanINFRAMES,
       "wanINFRAMESERR": wanINFRAMESERR,
       "wanINDFR": wanINDFR,
       "ethCountsTable": ethCountsTable,
       "ethCountsEntry": ethCountsEntry,
       "ethINFRAMES": ethINFRAMES,
       "ethINFRAMESERR": ethINFRAMESERR,
       "ethINDFR": ethINDFR,
       "ethINFRAMESDISCS": ethINFRAMESDISCS,
       "ethOUTFRAMES": ethOUTFRAMES,
       "ethOUTFRAMESERR": ethOUTFRAMESERR,
       "ethINOCTETS": ethINOCTETS,
       "ethOUTOCTETS": ethOUTOCTETS,
       "ethOUTDFR": ethOUTDFR,
       "ethOUTFRAMESDISCDS": ethOUTFRAMESDISCDS,
       "enet": enet,
       "enetCountsTable": enetCountsTable,
       "enetCountsEntry": enetCountsEntry,
       "ethFCSERR": ethFCSERR,
       "ethJAB": ethJAB,
       "ethFRAG": ethFRAG,
       "ethFRTOOLONGS": ethFRTOOLONGS,
       "ethFRTOOSHORTS": ethFRTOOSHORTS,
       "ethSYMBOLERR": ethSYMBOLERR,
       "ethINPAUSEFR": ethINPAUSEFR,
       "ethOUTPAUSEFR": ethOUTPAUSEFR}
)
