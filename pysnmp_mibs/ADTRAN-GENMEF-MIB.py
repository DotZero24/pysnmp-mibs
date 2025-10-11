# SNMP MIB module (ADTRAN-GENMEF-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENMEF-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:32 2025
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

(adGenPortTrapIdentifier,) = mibBuilder.importSymbols(
    "ADTRAN-GENPORT-MIB",
    "adGenPortTrapIdentifier")

(adGenMEF,
 adGenMEFID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-EOCU-MIB",
    "adGenMEF",
    "adGenMEFID")

(Unsigned64TC,) = mibBuilder.importSymbols(
    "APPLICATION-MIB",
    "Unsigned64TC")

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

(sysName,) = mibBuilder.importSymbols(
    "SNMPv2-MIB",
    "sysName")

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

adGenMEFMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 69, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMEFMIB.setRevisions(
        ("2013-01-14 00:00",
         "2010-02-03 00:00",
         "2007-04-05 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenMEFEvents_ObjectIdentity = ObjectIdentity
adGenMEFEvents = _AdGenMEFEvents_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0)
)
_AdGenMEFProvisioning_ObjectIdentity = ObjectIdentity
adGenMEFProvisioning = _AdGenMEFProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1)
)
_AdGenMEFProvisioningScalars_ObjectIdentity = ObjectIdentity
adGenMEFProvisioningScalars = _AdGenMEFProvisioningScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 1)
)


class _AdGenMEFDeleteAll_Type(Integer32):
    """Custom type adGenMEFDeleteAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("deleteAllMaps", 1)
    )


_AdGenMEFDeleteAll_Type.__name__ = "Integer32"
_AdGenMEFDeleteAll_Object = MibScalar
adGenMEFDeleteAll = _AdGenMEFDeleteAll_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 1, 2),
    _AdGenMEFDeleteAll_Type()
)
adGenMEFDeleteAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFDeleteAll.setStatus("current")
_AdGenMEFEVCIndexNext_Type = Integer32
_AdGenMEFEVCIndexNext_Object = MibScalar
adGenMEFEVCIndexNext = _AdGenMEFEVCIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 1, 3),
    _AdGenMEFEVCIndexNext_Type()
)
adGenMEFEVCIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFEVCIndexNext.setStatus("current")
_AdGenMEFMapIndexNext_Type = Integer32
_AdGenMEFMapIndexNext_Object = MibScalar
adGenMEFMapIndexNext = _AdGenMEFMapIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 1, 4),
    _AdGenMEFMapIndexNext_Type()
)
adGenMEFMapIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFMapIndexNext.setStatus("current")
_AdGenMEFProfileIndexNext_Type = Integer32
_AdGenMEFProfileIndexNext_Object = MibScalar
adGenMEFProfileIndexNext = _AdGenMEFProfileIndexNext_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 1, 5),
    _AdGenMEFProfileIndexNext_Type()
)
adGenMEFProfileIndexNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFProfileIndexNext.setStatus("current")
_AdGenMEFEVCEthertype_Type = Integer32
_AdGenMEFEVCEthertype_Object = MibScalar
adGenMEFEVCEthertype = _AdGenMEFEVCEthertype_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 1, 6),
    _AdGenMEFEVCEthertype_Type()
)
adGenMEFEVCEthertype.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFEVCEthertype.setStatus("current")
_AdGenMEFEVCsTable_Object = MibTable
adGenMEFEVCsTable = _AdGenMEFEVCsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2)
)
if mibBuilder.loadTexts:
    adGenMEFEVCsTable.setStatus("current")
_AdGenMEFEVCsEntry_Object = MibTableRow
adGenMEFEVCsEntry = _AdGenMEFEVCsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1)
)
adGenMEFEVCsEntry.setIndexNames(
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFEVCIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFEVCsEntry.setStatus("current")
_AdGenMEFEVCIndex_Type = Integer32
_AdGenMEFEVCIndex_Object = MibTableColumn
adGenMEFEVCIndex = _AdGenMEFEVCIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1, 1),
    _AdGenMEFEVCIndex_Type()
)
adGenMEFEVCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFEVCIndex.setStatus("current")
_AdGenMEFEVCRowStatus_Type = RowStatus
_AdGenMEFEVCRowStatus_Object = MibTableColumn
adGenMEFEVCRowStatus = _AdGenMEFEVCRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1, 2),
    _AdGenMEFEVCRowStatus_Type()
)
adGenMEFEVCRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFEVCRowStatus.setStatus("current")
_AdGenMEFEVCAlias_Type = DisplayString
_AdGenMEFEVCAlias_Object = MibTableColumn
adGenMEFEVCAlias = _AdGenMEFEVCAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1, 3),
    _AdGenMEFEVCAlias_Type()
)
adGenMEFEVCAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFEVCAlias.setStatus("current")


class _AdGenMEFEVCStatus_Type(Integer32):
    """Custom type adGenMEFEVCStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("running", 2),
          ("noMapsRunning", 3),
          ("invalidEVCPort", 4),
          ("invalidEVCVID", 5),
          ("disabled", 6),
          ("evcVIDNotAllowed", 7),
          ("duplicateEVC", 8),
          ("vlanMgmtConflict", 9),
          ("transparentEVCConflict", 10))
    )


_AdGenMEFEVCStatus_Type.__name__ = "Integer32"
_AdGenMEFEVCStatus_Object = MibTableColumn
adGenMEFEVCStatus = _AdGenMEFEVCStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1, 4),
    _AdGenMEFEVCStatus_Type()
)
adGenMEFEVCStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFEVCStatus.setStatus("current")
_AdGenMEFEVCPort_Type = InterfaceIndex
_AdGenMEFEVCPort_Object = MibTableColumn
adGenMEFEVCPort = _AdGenMEFEVCPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1, 5),
    _AdGenMEFEVCPort_Type()
)
adGenMEFEVCPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFEVCPort.setStatus("current")


class _AdGenMEFEVCCEVLANIDPreservation_Type(Integer32):
    """Custom type adGenMEFEVCCEVLANIDPreservation based on Integer32"""
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


_AdGenMEFEVCCEVLANIDPreservation_Type.__name__ = "Integer32"
_AdGenMEFEVCCEVLANIDPreservation_Object = MibTableColumn
adGenMEFEVCCEVLANIDPreservation = _AdGenMEFEVCCEVLANIDPreservation_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1, 6),
    _AdGenMEFEVCCEVLANIDPreservation_Type()
)
adGenMEFEVCCEVLANIDPreservation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFEVCCEVLANIDPreservation.setStatus("current")
_AdGenMEFEVCVLANID_Type = Integer32
_AdGenMEFEVCVLANID_Object = MibTableColumn
adGenMEFEVCVLANID = _AdGenMEFEVCVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1, 7),
    _AdGenMEFEVCVLANID_Type()
)
adGenMEFEVCVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFEVCVLANID.setStatus("current")
_AdGenMEFEVCMapsByAlias_Type = DisplayString
_AdGenMEFEVCMapsByAlias_Object = MibTableColumn
adGenMEFEVCMapsByAlias = _AdGenMEFEVCMapsByAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1, 8),
    _AdGenMEFEVCMapsByAlias_Type()
)
adGenMEFEVCMapsByAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFEVCMapsByAlias.setStatus("obsolete")
_AdGenMEFEVCMapsByIndex_Type = DisplayString
_AdGenMEFEVCMapsByIndex_Object = MibTableColumn
adGenMEFEVCMapsByIndex = _AdGenMEFEVCMapsByIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1, 9),
    _AdGenMEFEVCMapsByIndex_Type()
)
adGenMEFEVCMapsByIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFEVCMapsByIndex.setStatus("current")
_AdGenMEFEVCNumMaps_Type = Unsigned32
_AdGenMEFEVCNumMaps_Object = MibTableColumn
adGenMEFEVCNumMaps = _AdGenMEFEVCNumMaps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 2, 1, 10),
    _AdGenMEFEVCNumMaps_Type()
)
adGenMEFEVCNumMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFEVCNumMaps.setStatus("current")
_AdGenMEFMapsTable_Object = MibTable
adGenMEFMapsTable = _AdGenMEFMapsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3)
)
if mibBuilder.loadTexts:
    adGenMEFMapsTable.setStatus("current")
_AdGenMEFMapsEntry_Object = MibTableRow
adGenMEFMapsEntry = _AdGenMEFMapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1)
)
adGenMEFMapsEntry.setIndexNames(
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFMapIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFMapsEntry.setStatus("current")
_AdGenMEFMapIndex_Type = Integer32
_AdGenMEFMapIndex_Object = MibTableColumn
adGenMEFMapIndex = _AdGenMEFMapIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 1),
    _AdGenMEFMapIndex_Type()
)
adGenMEFMapIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFMapIndex.setStatus("current")
_AdGenMEFMapRowStatus_Type = RowStatus
_AdGenMEFMapRowStatus_Object = MibTableColumn
adGenMEFMapRowStatus = _AdGenMEFMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 2),
    _AdGenMEFMapRowStatus_Type()
)
adGenMEFMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapRowStatus.setStatus("current")
_AdGenMEFMapAlias_Type = DisplayString
_AdGenMEFMapAlias_Object = MibTableColumn
adGenMEFMapAlias = _AdGenMEFMapAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 3),
    _AdGenMEFMapAlias_Type()
)
adGenMEFMapAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapAlias.setStatus("current")


class _AdGenMEFMapStatus_Type(Integer32):
    """Custom type adGenMEFMapStatus based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("running", 2),
          ("noEVCconnected", 3),
          ("evcNotRunning", 4),
          ("invalidUNIport", 5),
          ("disabled", 6),
          ("duplicateMap", 7),
          ("vlanMGMTconflict", 8),
          ("tagOptionConflict", 9),
          ("excessUNIsPerEVC", 10),
          ("uniPortEqualEVCPort", 11),
          ("preserveConflict", 12),
          ("resourcesUnavailable", 13),
          ("cTagOptionConflict", 14))
    )


_AdGenMEFMapStatus_Type.__name__ = "Integer32"
_AdGenMEFMapStatus_Object = MibTableColumn
adGenMEFMapStatus = _AdGenMEFMapStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 4),
    _AdGenMEFMapStatus_Type()
)
adGenMEFMapStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFMapStatus.setStatus("current")
_AdGenMEFMapAssociatedEVCAlias_Type = DisplayString
_AdGenMEFMapAssociatedEVCAlias_Object = MibTableColumn
adGenMEFMapAssociatedEVCAlias = _AdGenMEFMapAssociatedEVCAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 5),
    _AdGenMEFMapAssociatedEVCAlias_Type()
)
adGenMEFMapAssociatedEVCAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapAssociatedEVCAlias.setStatus("current")
_AdGenMEFMapAssociatedEVCIndex_Type = Integer32
_AdGenMEFMapAssociatedEVCIndex_Object = MibTableColumn
adGenMEFMapAssociatedEVCIndex = _AdGenMEFMapAssociatedEVCIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 6),
    _AdGenMEFMapAssociatedEVCIndex_Type()
)
adGenMEFMapAssociatedEVCIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapAssociatedEVCIndex.setStatus("current")
_AdGenMEFMapUNIPort_Type = InterfaceIndex
_AdGenMEFMapUNIPort_Object = MibTableColumn
adGenMEFMapUNIPort = _AdGenMEFMapUNIPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 7),
    _AdGenMEFMapUNIPort_Type()
)
adGenMEFMapUNIPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapUNIPort.setStatus("current")
_AdGenMEFMapCEVLANID_Type = Integer32
_AdGenMEFMapCEVLANID_Object = MibTableColumn
adGenMEFMapCEVLANID = _AdGenMEFMapCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 8),
    _AdGenMEFMapCEVLANID_Type()
)
adGenMEFMapCEVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapCEVLANID.setStatus("current")
_AdGenMEFMapCEVLANPRI_Type = DisplayString
_AdGenMEFMapCEVLANPRI_Object = MibTableColumn
adGenMEFMapCEVLANPRI = _AdGenMEFMapCEVLANPRI_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 9),
    _AdGenMEFMapCEVLANPRI_Type()
)
adGenMEFMapCEVLANPRI.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapCEVLANPRI.setStatus("current")
_AdGenMEFMapDSCP_Type = Integer32
_AdGenMEFMapDSCP_Object = MibTableColumn
adGenMEFMapDSCP = _AdGenMEFMapDSCP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 10),
    _AdGenMEFMapDSCP_Type()
)
adGenMEFMapDSCP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapDSCP.setStatus("deprecated")


class _AdGenMEFMapUntagged_Type(Integer32):
    """Custom type adGenMEFMapUntagged based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disallow", 1),
          ("allow", 2))
    )


_AdGenMEFMapUntagged_Type.__name__ = "Integer32"
_AdGenMEFMapUntagged_Object = MibTableColumn
adGenMEFMapUntagged = _AdGenMEFMapUntagged_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 11),
    _AdGenMEFMapUntagged_Type()
)
adGenMEFMapUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapUntagged.setStatus("current")


class _AdGenMEFMapCoS_Type(Integer32):
    """Custom type adGenMEFMapCoS based on Integer32"""
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
        *(("explicit0", 1),
          ("explicit1", 2),
          ("explicit2", 3),
          ("explicit3", 4),
          ("explicit4", 5),
          ("explicit5", 6),
          ("explicit6", 7),
          ("explicit7", 8),
          ("inheritFromCEVLANPbits", 9))
    )


_AdGenMEFMapCoS_Type.__name__ = "Integer32"
_AdGenMEFMapCoS_Object = MibTableColumn
adGenMEFMapCoS = _AdGenMEFMapCoS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 12),
    _AdGenMEFMapCoS_Type()
)
adGenMEFMapCoS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapCoS.setStatus("current")
_AdGenMEFMapAttachedProfileAlias_Type = DisplayString
_AdGenMEFMapAttachedProfileAlias_Object = MibTableColumn
adGenMEFMapAttachedProfileAlias = _AdGenMEFMapAttachedProfileAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 13),
    _AdGenMEFMapAttachedProfileAlias_Type()
)
adGenMEFMapAttachedProfileAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFMapAttachedProfileAlias.setStatus("current")
_AdGenMEFMapAttachedProfileIndex_Type = Integer32
_AdGenMEFMapAttachedProfileIndex_Object = MibTableColumn
adGenMEFMapAttachedProfileIndex = _AdGenMEFMapAttachedProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 14),
    _AdGenMEFMapAttachedProfileIndex_Type()
)
adGenMEFMapAttachedProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFMapAttachedProfileIndex.setStatus("current")


class _AdGenMEFMapBroadcast_Type(Integer32):
    """Custom type adGenMEFMapBroadcast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disallow", 1),
          ("allow", 2))
    )


_AdGenMEFMapBroadcast_Type.__name__ = "Integer32"
_AdGenMEFMapBroadcast_Object = MibTableColumn
adGenMEFMapBroadcast = _AdGenMEFMapBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 15),
    _AdGenMEFMapBroadcast_Type()
)
adGenMEFMapBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapBroadcast.setStatus("current")


class _AdGenMEFMapMulticast_Type(Integer32):
    """Custom type adGenMEFMapMulticast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disallow", 1),
          ("allow", 2))
    )


_AdGenMEFMapMulticast_Type.__name__ = "Integer32"
_AdGenMEFMapMulticast_Object = MibTableColumn
adGenMEFMapMulticast = _AdGenMEFMapMulticast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 16),
    _AdGenMEFMapMulticast_Type()
)
adGenMEFMapMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapMulticast.setStatus("current")


class _AdGenMEFMapUnicast_Type(Integer32):
    """Custom type adGenMEFMapUnicast based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disallow", 1),
          ("allow", 2))
    )


_AdGenMEFMapUnicast_Type.__name__ = "Integer32"
_AdGenMEFMapUnicast_Object = MibTableColumn
adGenMEFMapUnicast = _AdGenMEFMapUnicast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 17),
    _AdGenMEFMapUnicast_Type()
)
adGenMEFMapUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapUnicast.setStatus("current")


class _AdGenMEFMapL2CP_Type(Integer32):
    """Custom type adGenMEFMapL2CP based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disallow", 1),
          ("allow", 2))
    )


_AdGenMEFMapL2CP_Type.__name__ = "Integer32"
_AdGenMEFMapL2CP_Object = MibTableColumn
adGenMEFMapL2CP = _AdGenMEFMapL2CP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 18),
    _AdGenMEFMapL2CP_Type()
)
adGenMEFMapL2CP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapL2CP.setStatus("current")


class _AdGenMEFMapMenCTag_Type(Integer32):
    """Custom type adGenMEFMapMenCTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 4095),
    )


_AdGenMEFMapMenCTag_Type.__name__ = "Integer32"
_AdGenMEFMapMenCTag_Object = MibTableColumn
adGenMEFMapMenCTag = _AdGenMEFMapMenCTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 19),
    _AdGenMEFMapMenCTag_Type()
)
adGenMEFMapMenCTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapMenCTag.setStatus("current")


class _AdGenMEFMapMenCTagPri_Type(Integer32):
    """Custom type adGenMEFMapMenCTagPri based on Integer32"""
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
        *(("explicit0", 1),
          ("explicit1", 2),
          ("explicit2", 3),
          ("explicit3", 4),
          ("explicit4", 5),
          ("explicit5", 6),
          ("explicit6", 7),
          ("explicit7", 8),
          ("inheritFromCEVLANPbits", 9))
    )


_AdGenMEFMapMenCTagPri_Type.__name__ = "Integer32"
_AdGenMEFMapMenCTagPri_Object = MibTableColumn
adGenMEFMapMenCTagPri = _AdGenMEFMapMenCTagPri_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 20),
    _AdGenMEFMapMenCTagPri_Type()
)
adGenMEFMapMenCTagPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapMenCTagPri.setStatus("current")
_AdGenMEFMapDSCPRange_Type = DisplayString
_AdGenMEFMapDSCPRange_Object = MibTableColumn
adGenMEFMapDSCPRange = _AdGenMEFMapDSCPRange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 21),
    _AdGenMEFMapDSCPRange_Type()
)
adGenMEFMapDSCPRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapDSCPRange.setStatus("current")


class _AdGenMEFMapIpHost_Type(OctetString):
    """Custom type adGenMEFMapIpHost based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 84),
    )


_AdGenMEFMapIpHost_Type.__name__ = "OctetString"
_AdGenMEFMapIpHost_Object = MibTableColumn
adGenMEFMapIpHost = _AdGenMEFMapIpHost_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 3, 1, 22),
    _AdGenMEFMapIpHost_Type()
)
adGenMEFMapIpHost.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapIpHost.setStatus("current")
_AdGenMEFProfilesTable_Object = MibTable
adGenMEFProfilesTable = _AdGenMEFProfilesTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4)
)
if mibBuilder.loadTexts:
    adGenMEFProfilesTable.setStatus("current")
_AdGenMEFProfilesEntry_Object = MibTableRow
adGenMEFProfilesEntry = _AdGenMEFProfilesEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1)
)
adGenMEFProfilesEntry.setIndexNames(
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFProfilesEntry.setStatus("current")
_AdGenMEFProfileIndex_Type = Integer32
_AdGenMEFProfileIndex_Object = MibTableColumn
adGenMEFProfileIndex = _AdGenMEFProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 1),
    _AdGenMEFProfileIndex_Type()
)
adGenMEFProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFProfileIndex.setStatus("current")
_AdGenMEFProfileRowStatus_Type = RowStatus
_AdGenMEFProfileRowStatus_Object = MibTableColumn
adGenMEFProfileRowStatus = _AdGenMEFProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 2),
    _AdGenMEFProfileRowStatus_Type()
)
adGenMEFProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileRowStatus.setStatus("current")
_AdGenMEFProfileAlias_Type = DisplayString
_AdGenMEFProfileAlias_Object = MibTableColumn
adGenMEFProfileAlias = _AdGenMEFProfileAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 3),
    _AdGenMEFProfileAlias_Type()
)
adGenMEFProfileAlias.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileAlias.setStatus("current")


class _AdGenMEFProfileStatus_Type(Integer32):
    """Custom type adGenMEFProfileStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("running", 2),
          ("disabled", 3),
          ("invalidUNIPort", 4),
          ("invalidEVC", 5),
          ("duplicateProfile", 6),
          ("invalidRates", 7),
          ("invalidApplication", 8),
          ("invalidCoS", 9),
          ("mapConflict", 10))
    )


_AdGenMEFProfileStatus_Type.__name__ = "Integer32"
_AdGenMEFProfileStatus_Object = MibTableColumn
adGenMEFProfileStatus = _AdGenMEFProfileStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 4),
    _AdGenMEFProfileStatus_Type()
)
adGenMEFProfileStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFProfileStatus.setStatus("current")


class _AdGenMEFProfileApp_Type(Integer32):
    """Custom type adGenMEFProfileApp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5)
        )
    )
    namedValues = NamedValues(
        *(("unspecified", 1),
          ("uniPort", 2),
          ("evc", 3),
          ("ceVLANCoS", 4),
          ("custom", 5))
    )


_AdGenMEFProfileApp_Type.__name__ = "Integer32"
_AdGenMEFProfileApp_Object = MibTableColumn
adGenMEFProfileApp = _AdGenMEFProfileApp_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 5),
    _AdGenMEFProfileApp_Type()
)
adGenMEFProfileApp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileApp.setStatus("current")
_AdGenMEFProfileUNIPort_Type = InterfaceIndex
_AdGenMEFProfileUNIPort_Object = MibTableColumn
adGenMEFProfileUNIPort = _AdGenMEFProfileUNIPort_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 6),
    _AdGenMEFProfileUNIPort_Type()
)
adGenMEFProfileUNIPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileUNIPort.setStatus("current")
_AdGenMEFProfileEVC_Type = Integer32
_AdGenMEFProfileEVC_Object = MibTableColumn
adGenMEFProfileEVC = _AdGenMEFProfileEVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 7),
    _AdGenMEFProfileEVC_Type()
)
adGenMEFProfileEVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileEVC.setStatus("current")
_AdGenMEFProfileCoSValue_Type = DisplayString
_AdGenMEFProfileCoSValue_Object = MibTableColumn
adGenMEFProfileCoSValue = _AdGenMEFProfileCoSValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 8),
    _AdGenMEFProfileCoSValue_Type()
)
adGenMEFProfileCoSValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileCoSValue.setStatus("current")


class _AdGenMEFProfileRateCoupling_Type(Integer32):
    """Custom type adGenMEFProfileRateCoupling based on Integer32"""
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


_AdGenMEFProfileRateCoupling_Type.__name__ = "Integer32"
_AdGenMEFProfileRateCoupling_Object = MibTableColumn
adGenMEFProfileRateCoupling = _AdGenMEFProfileRateCoupling_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 9),
    _AdGenMEFProfileRateCoupling_Type()
)
adGenMEFProfileRateCoupling.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileRateCoupling.setStatus("current")
_AdGenMEFProfileCIR_Type = Integer32
_AdGenMEFProfileCIR_Object = MibTableColumn
adGenMEFProfileCIR = _AdGenMEFProfileCIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 10),
    _AdGenMEFProfileCIR_Type()
)
adGenMEFProfileCIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileCIR.setStatus("deprecated")
_AdGenMEFProfileCBS_Type = Integer32
_AdGenMEFProfileCBS_Object = MibTableColumn
adGenMEFProfileCBS = _AdGenMEFProfileCBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 11),
    _AdGenMEFProfileCBS_Type()
)
adGenMEFProfileCBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileCBS.setStatus("current")
_AdGenMEFProfileEIR_Type = Integer32
_AdGenMEFProfileEIR_Object = MibTableColumn
adGenMEFProfileEIR = _AdGenMEFProfileEIR_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 12),
    _AdGenMEFProfileEIR_Type()
)
adGenMEFProfileEIR.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileEIR.setStatus("deprecated")
_AdGenMEFProfileEBS_Type = Integer32
_AdGenMEFProfileEBS_Object = MibTableColumn
adGenMEFProfileEBS = _AdGenMEFProfileEBS_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 13),
    _AdGenMEFProfileEBS_Type()
)
adGenMEFProfileEBS.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileEBS.setStatus("current")
_AdGenMEFProfileAddMap_Type = DisplayString
_AdGenMEFProfileAddMap_Object = MibTableColumn
adGenMEFProfileAddMap = _AdGenMEFProfileAddMap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 14),
    _AdGenMEFProfileAddMap_Type()
)
adGenMEFProfileAddMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileAddMap.setStatus("current")
_AdGenMEFProfileRemoveMap_Type = DisplayString
_AdGenMEFProfileRemoveMap_Object = MibTableColumn
adGenMEFProfileRemoveMap = _AdGenMEFProfileRemoveMap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 15),
    _AdGenMEFProfileRemoveMap_Type()
)
adGenMEFProfileRemoveMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileRemoveMap.setStatus("current")
_AdGenMEFProfileMapsByAlias_Type = DisplayString
_AdGenMEFProfileMapsByAlias_Object = MibTableColumn
adGenMEFProfileMapsByAlias = _AdGenMEFProfileMapsByAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 16),
    _AdGenMEFProfileMapsByAlias_Type()
)
adGenMEFProfileMapsByAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFProfileMapsByAlias.setStatus("current")
_AdGenMEFProfileMapsByIndex_Type = DisplayString
_AdGenMEFProfileMapsByIndex_Object = MibTableColumn
adGenMEFProfileMapsByIndex = _AdGenMEFProfileMapsByIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 17),
    _AdGenMEFProfileMapsByIndex_Type()
)
adGenMEFProfileMapsByIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFProfileMapsByIndex.setStatus("current")
_AdGenMEFProfileDroppedPackets_Type = Gauge32
_AdGenMEFProfileDroppedPackets_Object = MibTableColumn
adGenMEFProfileDroppedPackets = _AdGenMEFProfileDroppedPackets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 18),
    _AdGenMEFProfileDroppedPackets_Type()
)
adGenMEFProfileDroppedPackets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFProfileDroppedPackets.setStatus("current")
_AdGenMEFProfileCommittedInformationRate_Type = Integer32
_AdGenMEFProfileCommittedInformationRate_Object = MibTableColumn
adGenMEFProfileCommittedInformationRate = _AdGenMEFProfileCommittedInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 19),
    _AdGenMEFProfileCommittedInformationRate_Type()
)
adGenMEFProfileCommittedInformationRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileCommittedInformationRate.setStatus("current")
_AdGenMEFProfileExcessInformationRate_Type = Integer32
_AdGenMEFProfileExcessInformationRate_Object = MibTableColumn
adGenMEFProfileExcessInformationRate = _AdGenMEFProfileExcessInformationRate_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 4, 1, 20),
    _AdGenMEFProfileExcessInformationRate_Type()
)
adGenMEFProfileExcessInformationRate.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFProfileExcessInformationRate.setStatus("current")
_AdGenMEFQueueScalars_ObjectIdentity = ObjectIdentity
adGenMEFQueueScalars = _AdGenMEFQueueScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5)
)


class _AdGenMEFQueueWREDTimeConstant_Type(Integer32):
    """Custom type adGenMEFQueueWREDTimeConstant based on Integer32"""
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
        *(("approx2ms", 1),
          ("approx4ms", 2),
          ("approx8ms", 3),
          ("approx16ms", 4),
          ("approx32ms", 5),
          ("approx62ms", 6),
          ("approx125ms", 7),
          ("approx250ms", 8),
          ("approx500ms", 9))
    )


_AdGenMEFQueueWREDTimeConstant_Type.__name__ = "Integer32"
_AdGenMEFQueueWREDTimeConstant_Object = MibScalar
adGenMEFQueueWREDTimeConstant = _AdGenMEFQueueWREDTimeConstant_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5, 1),
    _AdGenMEFQueueWREDTimeConstant_Type()
)
adGenMEFQueueWREDTimeConstant.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFQueueWREDTimeConstant.setStatus("current")
_AdGenMEFQueueCoSMapForPri0_Type = Integer32
_AdGenMEFQueueCoSMapForPri0_Object = MibScalar
adGenMEFQueueCoSMapForPri0 = _AdGenMEFQueueCoSMapForPri0_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5, 2),
    _AdGenMEFQueueCoSMapForPri0_Type()
)
adGenMEFQueueCoSMapForPri0.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFQueueCoSMapForPri0.setStatus("current")
_AdGenMEFQueueCoSMapForPri1_Type = Integer32
_AdGenMEFQueueCoSMapForPri1_Object = MibScalar
adGenMEFQueueCoSMapForPri1 = _AdGenMEFQueueCoSMapForPri1_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5, 3),
    _AdGenMEFQueueCoSMapForPri1_Type()
)
adGenMEFQueueCoSMapForPri1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFQueueCoSMapForPri1.setStatus("current")
_AdGenMEFQueueCoSMapForPri2_Type = Integer32
_AdGenMEFQueueCoSMapForPri2_Object = MibScalar
adGenMEFQueueCoSMapForPri2 = _AdGenMEFQueueCoSMapForPri2_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5, 4),
    _AdGenMEFQueueCoSMapForPri2_Type()
)
adGenMEFQueueCoSMapForPri2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFQueueCoSMapForPri2.setStatus("current")
_AdGenMEFQueueCoSMapForPri3_Type = Integer32
_AdGenMEFQueueCoSMapForPri3_Object = MibScalar
adGenMEFQueueCoSMapForPri3 = _AdGenMEFQueueCoSMapForPri3_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5, 5),
    _AdGenMEFQueueCoSMapForPri3_Type()
)
adGenMEFQueueCoSMapForPri3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFQueueCoSMapForPri3.setStatus("current")
_AdGenMEFQueueCoSMapForPri4_Type = Integer32
_AdGenMEFQueueCoSMapForPri4_Object = MibScalar
adGenMEFQueueCoSMapForPri4 = _AdGenMEFQueueCoSMapForPri4_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5, 6),
    _AdGenMEFQueueCoSMapForPri4_Type()
)
adGenMEFQueueCoSMapForPri4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFQueueCoSMapForPri4.setStatus("current")
_AdGenMEFQueueCoSMapForPri5_Type = Integer32
_AdGenMEFQueueCoSMapForPri5_Object = MibScalar
adGenMEFQueueCoSMapForPri5 = _AdGenMEFQueueCoSMapForPri5_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5, 7),
    _AdGenMEFQueueCoSMapForPri5_Type()
)
adGenMEFQueueCoSMapForPri5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFQueueCoSMapForPri5.setStatus("current")
_AdGenMEFQueueCoSMapForPri6_Type = Integer32
_AdGenMEFQueueCoSMapForPri6_Object = MibScalar
adGenMEFQueueCoSMapForPri6 = _AdGenMEFQueueCoSMapForPri6_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5, 8),
    _AdGenMEFQueueCoSMapForPri6_Type()
)
adGenMEFQueueCoSMapForPri6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFQueueCoSMapForPri6.setStatus("current")
_AdGenMEFQueueCoSMapForPri7_Type = Integer32
_AdGenMEFQueueCoSMapForPri7_Object = MibScalar
adGenMEFQueueCoSMapForPri7 = _AdGenMEFQueueCoSMapForPri7_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5, 9),
    _AdGenMEFQueueCoSMapForPri7_Type()
)
adGenMEFQueueCoSMapForPri7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFQueueCoSMapForPri7.setStatus("current")
_AdGenMEFQosUntagged_Type = Integer32
_AdGenMEFQosUntagged_Object = MibScalar
adGenMEFQosUntagged = _AdGenMEFQosUntagged_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 5, 10),
    _AdGenMEFQosUntagged_Type()
)
adGenMEFQosUntagged.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFQosUntagged.setStatus("current")
_AdGenMEF10100EthQueuesTable_Object = MibTable
adGenMEF10100EthQueuesTable = _AdGenMEF10100EthQueuesTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6)
)
if mibBuilder.loadTexts:
    adGenMEF10100EthQueuesTable.setStatus("current")
_AdGenMEF10100EthQueuesEntry_Object = MibTableRow
adGenMEF10100EthQueuesEntry = _AdGenMEF10100EthQueuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6, 1)
)
adGenMEF10100EthQueuesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMEF-MIB", "adGenMEF10100EthCoSIndex"),
)
if mibBuilder.loadTexts:
    adGenMEF10100EthQueuesEntry.setStatus("current")
_AdGenMEF10100EthCoSIndex_Type = Integer32
_AdGenMEF10100EthCoSIndex_Object = MibTableColumn
adGenMEF10100EthCoSIndex = _AdGenMEF10100EthCoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6, 1, 1),
    _AdGenMEF10100EthCoSIndex_Type()
)
adGenMEF10100EthCoSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEF10100EthCoSIndex.setStatus("current")
_AdGenMEF10100EthQueueMaxDepth_Type = Integer32
_AdGenMEF10100EthQueueMaxDepth_Object = MibTableColumn
adGenMEF10100EthQueueMaxDepth = _AdGenMEF10100EthQueueMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6, 1, 2),
    _AdGenMEF10100EthQueueMaxDepth_Type()
)
adGenMEF10100EthQueueMaxDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEF10100EthQueueMaxDepth.setStatus("current")


class _AdGenMEF10100EthQueueWREDState_Type(Integer32):
    """Custom type adGenMEF10100EthQueueWREDState based on Integer32"""
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


_AdGenMEF10100EthQueueWREDState_Type.__name__ = "Integer32"
_AdGenMEF10100EthQueueWREDState_Object = MibTableColumn
adGenMEF10100EthQueueWREDState = _AdGenMEF10100EthQueueWREDState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6, 1, 3),
    _AdGenMEF10100EthQueueWREDState_Type()
)
adGenMEF10100EthQueueWREDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEF10100EthQueueWREDState.setStatus("current")
_AdGenMEF10100EthQueueWREDGreenMaxThresh_Type = Integer32
_AdGenMEF10100EthQueueWREDGreenMaxThresh_Object = MibTableColumn
adGenMEF10100EthQueueWREDGreenMaxThresh = _AdGenMEF10100EthQueueWREDGreenMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6, 1, 4),
    _AdGenMEF10100EthQueueWREDGreenMaxThresh_Type()
)
adGenMEF10100EthQueueWREDGreenMaxThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEF10100EthQueueWREDGreenMaxThresh.setStatus("current")
_AdGenMEF10100EthQueueWREDGreenMinThresh_Type = Integer32
_AdGenMEF10100EthQueueWREDGreenMinThresh_Object = MibTableColumn
adGenMEF10100EthQueueWREDGreenMinThresh = _AdGenMEF10100EthQueueWREDGreenMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6, 1, 5),
    _AdGenMEF10100EthQueueWREDGreenMinThresh_Type()
)
adGenMEF10100EthQueueWREDGreenMinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEF10100EthQueueWREDGreenMinThresh.setStatus("current")
_AdGenMEF10100EthQueueWREDGreenDropProb_Type = Integer32
_AdGenMEF10100EthQueueWREDGreenDropProb_Object = MibTableColumn
adGenMEF10100EthQueueWREDGreenDropProb = _AdGenMEF10100EthQueueWREDGreenDropProb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6, 1, 6),
    _AdGenMEF10100EthQueueWREDGreenDropProb_Type()
)
adGenMEF10100EthQueueWREDGreenDropProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEF10100EthQueueWREDGreenDropProb.setStatus("current")
_AdGenMEF10100EthQueueWREDYellowMaxThresh_Type = Integer32
_AdGenMEF10100EthQueueWREDYellowMaxThresh_Object = MibTableColumn
adGenMEF10100EthQueueWREDYellowMaxThresh = _AdGenMEF10100EthQueueWREDYellowMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6, 1, 7),
    _AdGenMEF10100EthQueueWREDYellowMaxThresh_Type()
)
adGenMEF10100EthQueueWREDYellowMaxThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEF10100EthQueueWREDYellowMaxThresh.setStatus("current")
_AdGenMEF10100EthQueueWREDYellowMinThresh_Type = Integer32
_AdGenMEF10100EthQueueWREDYellowMinThresh_Object = MibTableColumn
adGenMEF10100EthQueueWREDYellowMinThresh = _AdGenMEF10100EthQueueWREDYellowMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6, 1, 8),
    _AdGenMEF10100EthQueueWREDYellowMinThresh_Type()
)
adGenMEF10100EthQueueWREDYellowMinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEF10100EthQueueWREDYellowMinThresh.setStatus("current")
_AdGenMEF10100EthQueueWREDYellowDropProb_Type = Integer32
_AdGenMEF10100EthQueueWREDYellowDropProb_Object = MibTableColumn
adGenMEF10100EthQueueWREDYellowDropProb = _AdGenMEF10100EthQueueWREDYellowDropProb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 6, 1, 9),
    _AdGenMEF10100EthQueueWREDYellowDropProb_Type()
)
adGenMEF10100EthQueueWREDYellowDropProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEF10100EthQueueWREDYellowDropProb.setStatus("current")
_AdGenMEFGigEthQueuesTable_Object = MibTable
adGenMEFGigEthQueuesTable = _AdGenMEFGigEthQueuesTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7)
)
if mibBuilder.loadTexts:
    adGenMEFGigEthQueuesTable.setStatus("current")
_AdGenMEFGigEthQueuesEntry_Object = MibTableRow
adGenMEFGigEthQueuesEntry = _AdGenMEFGigEthQueuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7, 1)
)
adGenMEFGigEthQueuesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFGigEthCoSIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFGigEthQueuesEntry.setStatus("current")
_AdGenMEFGigEthCoSIndex_Type = Integer32
_AdGenMEFGigEthCoSIndex_Object = MibTableColumn
adGenMEFGigEthCoSIndex = _AdGenMEFGigEthCoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7, 1, 1),
    _AdGenMEFGigEthCoSIndex_Type()
)
adGenMEFGigEthCoSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFGigEthCoSIndex.setStatus("current")
_AdGenMEFGigEthQueueMaxDepth_Type = Integer32
_AdGenMEFGigEthQueueMaxDepth_Object = MibTableColumn
adGenMEFGigEthQueueMaxDepth = _AdGenMEFGigEthQueueMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7, 1, 2),
    _AdGenMEFGigEthQueueMaxDepth_Type()
)
adGenMEFGigEthQueueMaxDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFGigEthQueueMaxDepth.setStatus("current")


class _AdGenMEFGigEthQueueWREDState_Type(Integer32):
    """Custom type adGenMEFGigEthQueueWREDState based on Integer32"""
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


_AdGenMEFGigEthQueueWREDState_Type.__name__ = "Integer32"
_AdGenMEFGigEthQueueWREDState_Object = MibTableColumn
adGenMEFGigEthQueueWREDState = _AdGenMEFGigEthQueueWREDState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7, 1, 3),
    _AdGenMEFGigEthQueueWREDState_Type()
)
adGenMEFGigEthQueueWREDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFGigEthQueueWREDState.setStatus("current")
_AdGenMEFGigEthQueueWREDGreenMaxThresh_Type = Integer32
_AdGenMEFGigEthQueueWREDGreenMaxThresh_Object = MibTableColumn
adGenMEFGigEthQueueWREDGreenMaxThresh = _AdGenMEFGigEthQueueWREDGreenMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7, 1, 4),
    _AdGenMEFGigEthQueueWREDGreenMaxThresh_Type()
)
adGenMEFGigEthQueueWREDGreenMaxThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFGigEthQueueWREDGreenMaxThresh.setStatus("current")
_AdGenMEFGigEthQueueWREDGreenMinThresh_Type = Integer32
_AdGenMEFGigEthQueueWREDGreenMinThresh_Object = MibTableColumn
adGenMEFGigEthQueueWREDGreenMinThresh = _AdGenMEFGigEthQueueWREDGreenMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7, 1, 5),
    _AdGenMEFGigEthQueueWREDGreenMinThresh_Type()
)
adGenMEFGigEthQueueWREDGreenMinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFGigEthQueueWREDGreenMinThresh.setStatus("current")
_AdGenMEFGigEthQueueWREDGreenDropProb_Type = Integer32
_AdGenMEFGigEthQueueWREDGreenDropProb_Object = MibTableColumn
adGenMEFGigEthQueueWREDGreenDropProb = _AdGenMEFGigEthQueueWREDGreenDropProb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7, 1, 6),
    _AdGenMEFGigEthQueueWREDGreenDropProb_Type()
)
adGenMEFGigEthQueueWREDGreenDropProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFGigEthQueueWREDGreenDropProb.setStatus("current")
_AdGenMEFGigEthQueueWREDYellowMaxThresh_Type = Integer32
_AdGenMEFGigEthQueueWREDYellowMaxThresh_Object = MibTableColumn
adGenMEFGigEthQueueWREDYellowMaxThresh = _AdGenMEFGigEthQueueWREDYellowMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7, 1, 7),
    _AdGenMEFGigEthQueueWREDYellowMaxThresh_Type()
)
adGenMEFGigEthQueueWREDYellowMaxThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFGigEthQueueWREDYellowMaxThresh.setStatus("current")
_AdGenMEFGigEthQueueWREDYellowMinThresh_Type = Integer32
_AdGenMEFGigEthQueueWREDYellowMinThresh_Object = MibTableColumn
adGenMEFGigEthQueueWREDYellowMinThresh = _AdGenMEFGigEthQueueWREDYellowMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7, 1, 8),
    _AdGenMEFGigEthQueueWREDYellowMinThresh_Type()
)
adGenMEFGigEthQueueWREDYellowMinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFGigEthQueueWREDYellowMinThresh.setStatus("current")
_AdGenMEFGigEthQueueWREDYellowDropProb_Type = Integer32
_AdGenMEFGigEthQueueWREDYellowDropProb_Object = MibTableColumn
adGenMEFGigEthQueueWREDYellowDropProb = _AdGenMEFGigEthQueueWREDYellowDropProb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 7, 1, 9),
    _AdGenMEFGigEthQueueWREDYellowDropProb_Type()
)
adGenMEFGigEthQueueWREDYellowDropProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFGigEthQueueWREDYellowDropProb.setStatus("current")
_AdGenMEFBondGrpQueuesTable_Object = MibTable
adGenMEFBondGrpQueuesTable = _AdGenMEFBondGrpQueuesTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8)
)
if mibBuilder.loadTexts:
    adGenMEFBondGrpQueuesTable.setStatus("current")
_AdGenMEFBondGrpQueuesEntry_Object = MibTableRow
adGenMEFBondGrpQueuesEntry = _AdGenMEFBondGrpQueuesEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8, 1)
)
adGenMEFBondGrpQueuesEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFBondGrpCoSIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFBondGrpQueuesEntry.setStatus("current")
_AdGenMEFBondGrpCoSIndex_Type = Integer32
_AdGenMEFBondGrpCoSIndex_Object = MibTableColumn
adGenMEFBondGrpCoSIndex = _AdGenMEFBondGrpCoSIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8, 1, 1),
    _AdGenMEFBondGrpCoSIndex_Type()
)
adGenMEFBondGrpCoSIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFBondGrpCoSIndex.setStatus("current")
_AdGenMEFBondGrpQueueMaxDepth_Type = Integer32
_AdGenMEFBondGrpQueueMaxDepth_Object = MibTableColumn
adGenMEFBondGrpQueueMaxDepth = _AdGenMEFBondGrpQueueMaxDepth_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8, 1, 2),
    _AdGenMEFBondGrpQueueMaxDepth_Type()
)
adGenMEFBondGrpQueueMaxDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFBondGrpQueueMaxDepth.setStatus("current")


class _AdGenMEFBondGrpQueueWREDState_Type(Integer32):
    """Custom type adGenMEFBondGrpQueueWREDState based on Integer32"""
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


_AdGenMEFBondGrpQueueWREDState_Type.__name__ = "Integer32"
_AdGenMEFBondGrpQueueWREDState_Object = MibTableColumn
adGenMEFBondGrpQueueWREDState = _AdGenMEFBondGrpQueueWREDState_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8, 1, 3),
    _AdGenMEFBondGrpQueueWREDState_Type()
)
adGenMEFBondGrpQueueWREDState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFBondGrpQueueWREDState.setStatus("current")
_AdGenMEFBondGrpQueueWREDGreenMaxThresh_Type = Integer32
_AdGenMEFBondGrpQueueWREDGreenMaxThresh_Object = MibTableColumn
adGenMEFBondGrpQueueWREDGreenMaxThresh = _AdGenMEFBondGrpQueueWREDGreenMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8, 1, 4),
    _AdGenMEFBondGrpQueueWREDGreenMaxThresh_Type()
)
adGenMEFBondGrpQueueWREDGreenMaxThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFBondGrpQueueWREDGreenMaxThresh.setStatus("current")
_AdGenMEFBondGrpQueueWREDGreenMinThresh_Type = Integer32
_AdGenMEFBondGrpQueueWREDGreenMinThresh_Object = MibTableColumn
adGenMEFBondGrpQueueWREDGreenMinThresh = _AdGenMEFBondGrpQueueWREDGreenMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8, 1, 5),
    _AdGenMEFBondGrpQueueWREDGreenMinThresh_Type()
)
adGenMEFBondGrpQueueWREDGreenMinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFBondGrpQueueWREDGreenMinThresh.setStatus("current")
_AdGenMEFBondGrpQueueWREDGreenDropProb_Type = Integer32
_AdGenMEFBondGrpQueueWREDGreenDropProb_Object = MibTableColumn
adGenMEFBondGrpQueueWREDGreenDropProb = _AdGenMEFBondGrpQueueWREDGreenDropProb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8, 1, 6),
    _AdGenMEFBondGrpQueueWREDGreenDropProb_Type()
)
adGenMEFBondGrpQueueWREDGreenDropProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFBondGrpQueueWREDGreenDropProb.setStatus("current")
_AdGenMEFBondGrpQueueWREDYellowMaxThresh_Type = Integer32
_AdGenMEFBondGrpQueueWREDYellowMaxThresh_Object = MibTableColumn
adGenMEFBondGrpQueueWREDYellowMaxThresh = _AdGenMEFBondGrpQueueWREDYellowMaxThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8, 1, 7),
    _AdGenMEFBondGrpQueueWREDYellowMaxThresh_Type()
)
adGenMEFBondGrpQueueWREDYellowMaxThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFBondGrpQueueWREDYellowMaxThresh.setStatus("current")
_AdGenMEFBondGrpQueueWREDYellowMinThresh_Type = Integer32
_AdGenMEFBondGrpQueueWREDYellowMinThresh_Object = MibTableColumn
adGenMEFBondGrpQueueWREDYellowMinThresh = _AdGenMEFBondGrpQueueWREDYellowMinThresh_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8, 1, 8),
    _AdGenMEFBondGrpQueueWREDYellowMinThresh_Type()
)
adGenMEFBondGrpQueueWREDYellowMinThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFBondGrpQueueWREDYellowMinThresh.setStatus("current")
_AdGenMEFBondGrpQueueWREDYellowDropProb_Type = Integer32
_AdGenMEFBondGrpQueueWREDYellowDropProb_Object = MibTableColumn
adGenMEFBondGrpQueueWREDYellowDropProb = _AdGenMEFBondGrpQueueWREDYellowDropProb_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 8, 1, 9),
    _AdGenMEFBondGrpQueueWREDYellowDropProb_Type()
)
adGenMEFBondGrpQueueWREDYellowDropProb.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFBondGrpQueueWREDYellowDropProb.setStatus("current")
_AdGenMEFUNITable_Object = MibTable
adGenMEFUNITable = _AdGenMEFUNITable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 9)
)
if mibBuilder.loadTexts:
    adGenMEFUNITable.setStatus("current")
_AdGenMEFUNIEntry_Object = MibTableRow
adGenMEFUNIEntry = _AdGenMEFUNIEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 9, 1)
)
adGenMEFUNIEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFUNIEntry.setStatus("current")
_AdGenMEFUNIMapsByAlias_Type = DisplayString
_AdGenMEFUNIMapsByAlias_Object = MibTableColumn
adGenMEFUNIMapsByAlias = _AdGenMEFUNIMapsByAlias_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 9, 1, 1),
    _AdGenMEFUNIMapsByAlias_Type()
)
adGenMEFUNIMapsByAlias.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFUNIMapsByAlias.setStatus("current")
_AdGenMEFUNIMapsByIndex_Type = DisplayString
_AdGenMEFUNIMapsByIndex_Object = MibTableColumn
adGenMEFUNIMapsByIndex = _AdGenMEFUNIMapsByIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 9, 1, 2),
    _AdGenMEFUNIMapsByIndex_Type()
)
adGenMEFUNIMapsByIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFUNIMapsByIndex.setStatus("current")
_AdGenMEFMENTable_Object = MibTable
adGenMEFMENTable = _AdGenMEFMENTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 10)
)
if mibBuilder.loadTexts:
    adGenMEFMENTable.setStatus("current")
_AdGenMEFMENEntry_Object = MibTableRow
adGenMEFMENEntry = _AdGenMEFMENEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 10, 1)
)
adGenMEFMENEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFMENEntry.setStatus("current")
_AdGenMEFMENVLANIDPool_Type = DisplayString
_AdGenMEFMENVLANIDPool_Object = MibTableColumn
adGenMEFMENVLANIDPool = _AdGenMEFMENVLANIDPool_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 1, 10, 1, 1),
    _AdGenMEFMENVLANIDPool_Type()
)
adGenMEFMENVLANIDPool.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFMENVLANIDPool.setStatus("current")
_AdGenMEFMibConformance_ObjectIdentity = ObjectIdentity
adGenMEFMibConformance = _AdGenMEFMibConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5)
)
_AdGenMEFMibGroups_ObjectIdentity = ObjectIdentity
adGenMEFMibGroups = _AdGenMEFMibGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1)
)
_AdGenMEFPerformance_ObjectIdentity = ObjectIdentity
adGenMEFPerformance = _AdGenMEFPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6)
)
_AdGenMEF10100EthAnomaliesPerformance_ObjectIdentity = ObjectIdentity
adGenMEF10100EthAnomaliesPerformance = _AdGenMEF10100EthAnomaliesPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1)
)
_AdGenMEF10100EthAnomalies15MinCurrentTable_Object = MibTable
adGenMEF10100EthAnomalies15MinCurrentTable = _AdGenMEF10100EthAnomalies15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 1)
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies15MinCurrentTable.setStatus("current")
_AdGenMEF10100EthAnomalies15MinCurrentEntry_Object = MibTableRow
adGenMEF10100EthAnomalies15MinCurrentEntry = _AdGenMEF10100EthAnomalies15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 1, 1)
)
adGenMEF10100EthAnomalies15MinCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies15MinCurrentEntry.setStatus("current")
_AdGenMEF10100EthAnomalies15MinCurrentFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEF10100EthAnomalies15MinCurrentFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEF10100EthAnomalies15MinCurrentFramesWithInvalidCEVLANID = _AdGenMEF10100EthAnomalies15MinCurrentFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 1, 1, 1),
    _AdGenMEF10100EthAnomalies15MinCurrentFramesWithInvalidCEVLANID_Type()
)
adGenMEF10100EthAnomalies15MinCurrentFramesWithInvalidCEVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies15MinCurrentFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEF10100EthAnomalies15MinIntervalTable_Object = MibTable
adGenMEF10100EthAnomalies15MinIntervalTable = _AdGenMEF10100EthAnomalies15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 2)
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies15MinIntervalTable.setStatus("current")
_AdGenMEF10100EthAnomalies15MinIntervalEntry_Object = MibTableRow
adGenMEF10100EthAnomalies15MinIntervalEntry = _AdGenMEF10100EthAnomalies15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 2, 1)
)
adGenMEF10100EthAnomalies15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMEF-MIB", "adGenMEF10100EthAnomalies15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies15MinIntervalEntry.setStatus("current")
_AdGenMEF10100EthAnomalies15MinIntervalNumber_Type = Integer32
_AdGenMEF10100EthAnomalies15MinIntervalNumber_Object = MibTableColumn
adGenMEF10100EthAnomalies15MinIntervalNumber = _AdGenMEF10100EthAnomalies15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 2, 1, 1),
    _AdGenMEF10100EthAnomalies15MinIntervalNumber_Type()
)
adGenMEF10100EthAnomalies15MinIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies15MinIntervalNumber.setStatus("current")
_AdGenMEF10100EthAnomalies15MinIntervalFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEF10100EthAnomalies15MinIntervalFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEF10100EthAnomalies15MinIntervalFramesWithInvalidCEVLANID = _AdGenMEF10100EthAnomalies15MinIntervalFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 2, 1, 2),
    _AdGenMEF10100EthAnomalies15MinIntervalFramesWithInvalidCEVLANID_Type()
)
adGenMEF10100EthAnomalies15MinIntervalFramesWithInvalidCEVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies15MinIntervalFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEF10100EthAnomalies24HrCurrentTable_Object = MibTable
adGenMEF10100EthAnomalies24HrCurrentTable = _AdGenMEF10100EthAnomalies24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 3)
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies24HrCurrentTable.setStatus("current")
_AdGenMEF10100EthAnomalies24HrCurrentEntry_Object = MibTableRow
adGenMEF10100EthAnomalies24HrCurrentEntry = _AdGenMEF10100EthAnomalies24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 3, 1)
)
adGenMEF10100EthAnomalies24HrCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies24HrCurrentEntry.setStatus("current")
_AdGenMEF10100EthAnomalies24HrCurrentFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEF10100EthAnomalies24HrCurrentFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEF10100EthAnomalies24HrCurrentFramesWithInvalidCEVLANID = _AdGenMEF10100EthAnomalies24HrCurrentFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 3, 1, 1),
    _AdGenMEF10100EthAnomalies24HrCurrentFramesWithInvalidCEVLANID_Type()
)
adGenMEF10100EthAnomalies24HrCurrentFramesWithInvalidCEVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies24HrCurrentFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEF10100EthAnomalies24HrIntervalTable_Object = MibTable
adGenMEF10100EthAnomalies24HrIntervalTable = _AdGenMEF10100EthAnomalies24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 4)
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies24HrIntervalTable.setStatus("current")
_AdGenMEF10100EthAnomalies24HrIntervalEntry_Object = MibTableRow
adGenMEF10100EthAnomalies24HrIntervalEntry = _AdGenMEF10100EthAnomalies24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 4, 1)
)
adGenMEF10100EthAnomalies24HrIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMEF-MIB", "adGenMEF10100EthAnomalies24HrIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies24HrIntervalEntry.setStatus("current")
_AdGenMEF10100EthAnomalies24HrIntervalNumber_Type = Integer32
_AdGenMEF10100EthAnomalies24HrIntervalNumber_Object = MibTableColumn
adGenMEF10100EthAnomalies24HrIntervalNumber = _AdGenMEF10100EthAnomalies24HrIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 4, 1, 1),
    _AdGenMEF10100EthAnomalies24HrIntervalNumber_Type()
)
adGenMEF10100EthAnomalies24HrIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies24HrIntervalNumber.setStatus("current")
_AdGenMEF10100EthAnomalies24HrIntervalFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEF10100EthAnomalies24HrIntervalFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEF10100EthAnomalies24HrIntervalFramesWithInvalidCEVLANID = _AdGenMEF10100EthAnomalies24HrIntervalFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 1, 4, 1, 2),
    _AdGenMEF10100EthAnomalies24HrIntervalFramesWithInvalidCEVLANID_Type()
)
adGenMEF10100EthAnomalies24HrIntervalFramesWithInvalidCEVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies24HrIntervalFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEFGigEthAnomaliesPerformance_ObjectIdentity = ObjectIdentity
adGenMEFGigEthAnomaliesPerformance = _AdGenMEFGigEthAnomaliesPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2)
)
_AdGenMEFGigEthAnomalies15MinCurrentTable_Object = MibTable
adGenMEFGigEthAnomalies15MinCurrentTable = _AdGenMEFGigEthAnomalies15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 1)
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies15MinCurrentTable.setStatus("current")
_AdGenMEFGigEthAnomalies15MinCurrentEntry_Object = MibTableRow
adGenMEFGigEthAnomalies15MinCurrentEntry = _AdGenMEFGigEthAnomalies15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 1, 1)
)
adGenMEFGigEthAnomalies15MinCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies15MinCurrentEntry.setStatus("current")
_AdGenMEFGigEthAnomalies15MinCurrentFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEFGigEthAnomalies15MinCurrentFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEFGigEthAnomalies15MinCurrentFramesWithInvalidCEVLANID = _AdGenMEFGigEthAnomalies15MinCurrentFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 1, 1, 1),
    _AdGenMEFGigEthAnomalies15MinCurrentFramesWithInvalidCEVLANID_Type()
)
adGenMEFGigEthAnomalies15MinCurrentFramesWithInvalidCEVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies15MinCurrentFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEFGigEthAnomalies15MinIntervalTable_Object = MibTable
adGenMEFGigEthAnomalies15MinIntervalTable = _AdGenMEFGigEthAnomalies15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 2)
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies15MinIntervalTable.setStatus("current")
_AdGenMEFGigEthAnomalies15MinIntervalEntry_Object = MibTableRow
adGenMEFGigEthAnomalies15MinIntervalEntry = _AdGenMEFGigEthAnomalies15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 2, 1)
)
adGenMEFGigEthAnomalies15MinIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFGigEthAnomalies15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies15MinIntervalEntry.setStatus("current")
_AdGenMEFGigEthAnomalies15MinIntervalNumber_Type = Integer32
_AdGenMEFGigEthAnomalies15MinIntervalNumber_Object = MibTableColumn
adGenMEFGigEthAnomalies15MinIntervalNumber = _AdGenMEFGigEthAnomalies15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 2, 1, 1),
    _AdGenMEFGigEthAnomalies15MinIntervalNumber_Type()
)
adGenMEFGigEthAnomalies15MinIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies15MinIntervalNumber.setStatus("current")
_AdGenMEFGigEthAnomalies15MinIntervalFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEFGigEthAnomalies15MinIntervalFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEFGigEthAnomalies15MinIntervalFramesWithInvalidCEVLANID = _AdGenMEFGigEthAnomalies15MinIntervalFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 2, 1, 2),
    _AdGenMEFGigEthAnomalies15MinIntervalFramesWithInvalidCEVLANID_Type()
)
adGenMEFGigEthAnomalies15MinIntervalFramesWithInvalidCEVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies15MinIntervalFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEFGigEthAnomalies24HrCurrentTable_Object = MibTable
adGenMEFGigEthAnomalies24HrCurrentTable = _AdGenMEFGigEthAnomalies24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 3)
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies24HrCurrentTable.setStatus("current")
_AdGenMEFGigEthAnomalies24HrCurrentEntry_Object = MibTableRow
adGenMEFGigEthAnomalies24HrCurrentEntry = _AdGenMEFGigEthAnomalies24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 3, 1)
)
adGenMEFGigEthAnomalies24HrCurrentEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies24HrCurrentEntry.setStatus("current")
_AdGenMEFGigEthAnomalies24HrCurrentFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEFGigEthAnomalies24HrCurrentFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEFGigEthAnomalies24HrCurrentFramesWithInvalidCEVLANID = _AdGenMEFGigEthAnomalies24HrCurrentFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 3, 1, 1),
    _AdGenMEFGigEthAnomalies24HrCurrentFramesWithInvalidCEVLANID_Type()
)
adGenMEFGigEthAnomalies24HrCurrentFramesWithInvalidCEVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies24HrCurrentFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEFGigEthAnomalies24HrIntervalTable_Object = MibTable
adGenMEFGigEthAnomalies24HrIntervalTable = _AdGenMEFGigEthAnomalies24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 4)
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies24HrIntervalTable.setStatus("current")
_AdGenMEFGigEthAnomalies24HrIntervalEntry_Object = MibTableRow
adGenMEFGigEthAnomalies24HrIntervalEntry = _AdGenMEFGigEthAnomalies24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 4, 1)
)
adGenMEFGigEthAnomalies24HrIntervalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFGigEthAnomalies24HrIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies24HrIntervalEntry.setStatus("current")
_AdGenMEFGigEthAnomalies24HrIntervalNumber_Type = Integer32
_AdGenMEFGigEthAnomalies24HrIntervalNumber_Object = MibTableColumn
adGenMEFGigEthAnomalies24HrIntervalNumber = _AdGenMEFGigEthAnomalies24HrIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 4, 1, 1),
    _AdGenMEFGigEthAnomalies24HrIntervalNumber_Type()
)
adGenMEFGigEthAnomalies24HrIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies24HrIntervalNumber.setStatus("current")
_AdGenMEFGigEthAnomalies24HrIntervalFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEFGigEthAnomalies24HrIntervalFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEFGigEthAnomalies24HrIntervalFramesWithInvalidCEVLANID = _AdGenMEFGigEthAnomalies24HrIntervalFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 2, 4, 1, 2),
    _AdGenMEFGigEthAnomalies24HrIntervalFramesWithInvalidCEVLANID_Type()
)
adGenMEFGigEthAnomalies24HrIntervalFramesWithInvalidCEVLANID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies24HrIntervalFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEFPolicerPerformance_ObjectIdentity = ObjectIdentity
adGenMEFPolicerPerformance = _AdGenMEFPolicerPerformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3)
)
_AdGenMEFPolicerPerformanceScalars_ObjectIdentity = ObjectIdentity
adGenMEFPolicerPerformanceScalars = _AdGenMEFPolicerPerformanceScalars_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 1)
)


class _AdGenMEFPolicerRstCurrentIntervals_Type(Integer32):
    """Custom type adGenMEFPolicerRstCurrentIntervals based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethRstAllCurrentIntervals", 1)
    )


_AdGenMEFPolicerRstCurrentIntervals_Type.__name__ = "Integer32"
_AdGenMEFPolicerRstCurrentIntervals_Object = MibScalar
adGenMEFPolicerRstCurrentIntervals = _AdGenMEFPolicerRstCurrentIntervals_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 1, 1),
    _AdGenMEFPolicerRstCurrentIntervals_Type()
)
adGenMEFPolicerRstCurrentIntervals.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicerRstCurrentIntervals.setStatus("current")


class _AdGenMEFPolicerRstAll_Type(Integer32):
    """Custom type adGenMEFPolicerRstAll based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("ethRstAll", 1)
    )


_AdGenMEFPolicerRstAll_Type.__name__ = "Integer32"
_AdGenMEFPolicerRstAll_Object = MibScalar
adGenMEFPolicerRstAll = _AdGenMEFPolicerRstAll_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 1, 2),
    _AdGenMEFPolicerRstAll_Type()
)
adGenMEFPolicerRstAll.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicerRstAll.setStatus("current")
_AdGenMEFPolicer15MinCurrentTable_Object = MibTable
adGenMEFPolicer15MinCurrentTable = _AdGenMEFPolicer15MinCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2)
)
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentTable.setStatus("current")
_AdGenMEFPolicer15MinCurrentEntry_Object = MibTableRow
adGenMEFPolicer15MinCurrentEntry = _AdGenMEFPolicer15MinCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1)
)
adGenMEFPolicer15MinCurrentEntry.setIndexNames(
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentEntry.setStatus("current")
_AdGenMEFPolicer15MinCurrentIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer15MinCurrentIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinCurrentIngressGreenFrames = _AdGenMEFPolicer15MinCurrentIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 1),
    _AdGenMEFPolicer15MinCurrentIngressGreenFrames_Type()
)
adGenMEFPolicer15MinCurrentIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinCurrentIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer15MinCurrentIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinCurrentIngressYellowFrames = _AdGenMEFPolicer15MinCurrentIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 2),
    _AdGenMEFPolicer15MinCurrentIngressYellowFrames_Type()
)
adGenMEFPolicer15MinCurrentIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinCurrentIngressRedFrames_Type = Gauge32
_AdGenMEFPolicer15MinCurrentIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer15MinCurrentIngressRedFrames = _AdGenMEFPolicer15MinCurrentIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 3),
    _AdGenMEFPolicer15MinCurrentIngressRedFrames_Type()
)
adGenMEFPolicer15MinCurrentIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentIngressRedFrames.setStatus("current")
_AdGenMEFPolicer15MinCurrentIngressGreenOctets_Type = Gauge32
_AdGenMEFPolicer15MinCurrentIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer15MinCurrentIngressGreenOctets = _AdGenMEFPolicer15MinCurrentIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 4),
    _AdGenMEFPolicer15MinCurrentIngressGreenOctets_Type()
)
adGenMEFPolicer15MinCurrentIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer15MinCurrentIngressYellowOctets_Type = Gauge32
_AdGenMEFPolicer15MinCurrentIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer15MinCurrentIngressYellowOctets = _AdGenMEFPolicer15MinCurrentIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 5),
    _AdGenMEFPolicer15MinCurrentIngressYellowOctets_Type()
)
adGenMEFPolicer15MinCurrentIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer15MinCurrentIngressRedOctets_Type = Gauge32
_AdGenMEFPolicer15MinCurrentIngressRedOctets_Object = MibTableColumn
adGenMEFPolicer15MinCurrentIngressRedOctets = _AdGenMEFPolicer15MinCurrentIngressRedOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 6),
    _AdGenMEFPolicer15MinCurrentIngressRedOctets_Type()
)
adGenMEFPolicer15MinCurrentIngressRedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentIngressRedOctets.setStatus("current")
_AdGenMEFPolicer15MinCurrentCongDiscardsIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer15MinCurrentCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenFrames = _AdGenMEFPolicer15MinCurrentCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 7),
    _AdGenMEFPolicer15MinCurrentCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinCurrentCongDiscardsIngressGreenOctets_Type = Gauge32
_AdGenMEFPolicer15MinCurrentCongDiscardsIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenOctets = _AdGenMEFPolicer15MinCurrentCongDiscardsIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 8),
    _AdGenMEFPolicer15MinCurrentCongDiscardsIngressGreenOctets_Type()
)
adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer15MinCurrentCongDiscardsIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer15MinCurrentCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowFrames = _AdGenMEFPolicer15MinCurrentCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 9),
    _AdGenMEFPolicer15MinCurrentCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinCurrentCongDiscardsIngressYellowOctets_Type = Gauge32
_AdGenMEFPolicer15MinCurrentCongDiscardsIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowOctets = _AdGenMEFPolicer15MinCurrentCongDiscardsIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 10),
    _AdGenMEFPolicer15MinCurrentCongDiscardsIngressYellowOctets_Type()
)
adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer15MinCurrentHCIngressGreenFrames_Type = Counter64
_AdGenMEFPolicer15MinCurrentHCIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinCurrentHCIngressGreenFrames = _AdGenMEFPolicer15MinCurrentHCIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 11),
    _AdGenMEFPolicer15MinCurrentHCIngressGreenFrames_Type()
)
adGenMEFPolicer15MinCurrentHCIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentHCIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinCurrentHCIngressYellowFrames_Type = Counter64
_AdGenMEFPolicer15MinCurrentHCIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinCurrentHCIngressYellowFrames = _AdGenMEFPolicer15MinCurrentHCIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 12),
    _AdGenMEFPolicer15MinCurrentHCIngressYellowFrames_Type()
)
adGenMEFPolicer15MinCurrentHCIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentHCIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinCurrentHCIngressRedFrames_Type = Counter64
_AdGenMEFPolicer15MinCurrentHCIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer15MinCurrentHCIngressRedFrames = _AdGenMEFPolicer15MinCurrentHCIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 13),
    _AdGenMEFPolicer15MinCurrentHCIngressRedFrames_Type()
)
adGenMEFPolicer15MinCurrentHCIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentHCIngressRedFrames.setStatus("current")
_AdGenMEFPolicer15MinCurrentHCIngressGreenOctets_Type = Counter64
_AdGenMEFPolicer15MinCurrentHCIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer15MinCurrentHCIngressGreenOctets = _AdGenMEFPolicer15MinCurrentHCIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 14),
    _AdGenMEFPolicer15MinCurrentHCIngressGreenOctets_Type()
)
adGenMEFPolicer15MinCurrentHCIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentHCIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer15MinCurrentHCIngressYellowOctets_Type = Counter64
_AdGenMEFPolicer15MinCurrentHCIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer15MinCurrentHCIngressYellowOctets = _AdGenMEFPolicer15MinCurrentHCIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 15),
    _AdGenMEFPolicer15MinCurrentHCIngressYellowOctets_Type()
)
adGenMEFPolicer15MinCurrentHCIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentHCIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer15MinCurrentHCIngressRedOctets_Type = Counter64
_AdGenMEFPolicer15MinCurrentHCIngressRedOctets_Object = MibTableColumn
adGenMEFPolicer15MinCurrentHCIngressRedOctets = _AdGenMEFPolicer15MinCurrentHCIngressRedOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 16),
    _AdGenMEFPolicer15MinCurrentHCIngressRedOctets_Type()
)
adGenMEFPolicer15MinCurrentHCIngressRedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentHCIngressRedOctets.setStatus("current")
_AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenFrames_Type = Counter64
_AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenFrames = _AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 17),
    _AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenOctets_Type = Counter64
_AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenOctets = _AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 18),
    _AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenOctets_Type()
)
adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowFrames_Type = Counter64
_AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowFrames = _AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 19),
    _AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowOctets_Type = Counter64
_AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowOctets = _AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 2, 1, 20),
    _AdGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowOctets_Type()
)
adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer15MinIntervalTable_Object = MibTable
adGenMEFPolicer15MinIntervalTable = _AdGenMEFPolicer15MinIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3)
)
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalTable.setStatus("current")
_AdGenMEFPolicer15MinIntervalEntry_Object = MibTableRow
adGenMEFPolicer15MinIntervalEntry = _AdGenMEFPolicer15MinIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1)
)
adGenMEFPolicer15MinIntervalEntry.setIndexNames(
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"),
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalEntry.setStatus("current")
_AdGenMEFPolicer15MinIntervalNumber_Type = Integer32
_AdGenMEFPolicer15MinIntervalNumber_Object = MibTableColumn
adGenMEFPolicer15MinIntervalNumber = _AdGenMEFPolicer15MinIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 1),
    _AdGenMEFPolicer15MinIntervalNumber_Type()
)
adGenMEFPolicer15MinIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalNumber.setStatus("current")
_AdGenMEFPolicer15MinIntervalIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer15MinIntervalIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinIntervalIngressGreenFrames = _AdGenMEFPolicer15MinIntervalIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 2),
    _AdGenMEFPolicer15MinIntervalIngressGreenFrames_Type()
)
adGenMEFPolicer15MinIntervalIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinIntervalIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer15MinIntervalIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinIntervalIngressYellowFrames = _AdGenMEFPolicer15MinIntervalIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 3),
    _AdGenMEFPolicer15MinIntervalIngressYellowFrames_Type()
)
adGenMEFPolicer15MinIntervalIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinIntervalIngressRedFrames_Type = Gauge32
_AdGenMEFPolicer15MinIntervalIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer15MinIntervalIngressRedFrames = _AdGenMEFPolicer15MinIntervalIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 4),
    _AdGenMEFPolicer15MinIntervalIngressRedFrames_Type()
)
adGenMEFPolicer15MinIntervalIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalIngressRedFrames.setStatus("current")
_AdGenMEFPolicer15MinIntervalIngressGreenOctets_Type = Gauge32
_AdGenMEFPolicer15MinIntervalIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer15MinIntervalIngressGreenOctets = _AdGenMEFPolicer15MinIntervalIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 5),
    _AdGenMEFPolicer15MinIntervalIngressGreenOctets_Type()
)
adGenMEFPolicer15MinIntervalIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer15MinIntervalIngressYellowOctets_Type = Gauge32
_AdGenMEFPolicer15MinIntervalIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer15MinIntervalIngressYellowOctets = _AdGenMEFPolicer15MinIntervalIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 6),
    _AdGenMEFPolicer15MinIntervalIngressYellowOctets_Type()
)
adGenMEFPolicer15MinIntervalIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer15MinIntervalIngressRedOctets_Type = Gauge32
_AdGenMEFPolicer15MinIntervalIngressRedOctets_Object = MibTableColumn
adGenMEFPolicer15MinIntervalIngressRedOctets = _AdGenMEFPolicer15MinIntervalIngressRedOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 7),
    _AdGenMEFPolicer15MinIntervalIngressRedOctets_Type()
)
adGenMEFPolicer15MinIntervalIngressRedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalIngressRedOctets.setStatus("current")
_AdGenMEFPolicer15MinIntervalCongDiscardsIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer15MinIntervalCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenFrames = _AdGenMEFPolicer15MinIntervalCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 8),
    _AdGenMEFPolicer15MinIntervalCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinIntervalCongDiscardsIngressGreenOctets_Type = Gauge32
_AdGenMEFPolicer15MinIntervalCongDiscardsIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenOctets = _AdGenMEFPolicer15MinIntervalCongDiscardsIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 9),
    _AdGenMEFPolicer15MinIntervalCongDiscardsIngressGreenOctets_Type()
)
adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer15MinIntervalCongDiscardsIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer15MinIntervalCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowFrames = _AdGenMEFPolicer15MinIntervalCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 10),
    _AdGenMEFPolicer15MinIntervalCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinIntervalCongDiscardsIngressYellowOctets_Type = Gauge32
_AdGenMEFPolicer15MinIntervalCongDiscardsIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowOctets = _AdGenMEFPolicer15MinIntervalCongDiscardsIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 11),
    _AdGenMEFPolicer15MinIntervalCongDiscardsIngressYellowOctets_Type()
)
adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer15MinIntervalHCIngressGreenFrames_Type = Counter64
_AdGenMEFPolicer15MinIntervalHCIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinIntervalHCIngressGreenFrames = _AdGenMEFPolicer15MinIntervalHCIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 12),
    _AdGenMEFPolicer15MinIntervalHCIngressGreenFrames_Type()
)
adGenMEFPolicer15MinIntervalHCIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalHCIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinIntervalHCIngressYellowFrames_Type = Counter64
_AdGenMEFPolicer15MinIntervalHCIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinIntervalHCIngressYellowFrames = _AdGenMEFPolicer15MinIntervalHCIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 13),
    _AdGenMEFPolicer15MinIntervalHCIngressYellowFrames_Type()
)
adGenMEFPolicer15MinIntervalHCIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalHCIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinIntervalHCIngressRedFrames_Type = Counter64
_AdGenMEFPolicer15MinIntervalHCIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer15MinIntervalHCIngressRedFrames = _AdGenMEFPolicer15MinIntervalHCIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 14),
    _AdGenMEFPolicer15MinIntervalHCIngressRedFrames_Type()
)
adGenMEFPolicer15MinIntervalHCIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalHCIngressRedFrames.setStatus("current")
_AdGenMEFPolicer15MinIntervalHCIngressGreenOctets_Type = Counter64
_AdGenMEFPolicer15MinIntervalHCIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer15MinIntervalHCIngressGreenOctets = _AdGenMEFPolicer15MinIntervalHCIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 15),
    _AdGenMEFPolicer15MinIntervalHCIngressGreenOctets_Type()
)
adGenMEFPolicer15MinIntervalHCIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalHCIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer15MinIntervalHCIngressYellowOctets_Type = Counter64
_AdGenMEFPolicer15MinIntervalHCIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer15MinIntervalHCIngressYellowOctets = _AdGenMEFPolicer15MinIntervalHCIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 16),
    _AdGenMEFPolicer15MinIntervalHCIngressYellowOctets_Type()
)
adGenMEFPolicer15MinIntervalHCIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalHCIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer15MinIntervalHCIngressRedOctets_Type = Counter64
_AdGenMEFPolicer15MinIntervalHCIngressRedOctets_Object = MibTableColumn
adGenMEFPolicer15MinIntervalHCIngressRedOctets = _AdGenMEFPolicer15MinIntervalHCIngressRedOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 17),
    _AdGenMEFPolicer15MinIntervalHCIngressRedOctets_Type()
)
adGenMEFPolicer15MinIntervalHCIngressRedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalHCIngressRedOctets.setStatus("current")
_AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenFrames_Type = Counter64
_AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenFrames = _AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 18),
    _AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenOctets_Type = Counter64
_AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenOctets = _AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 19),
    _AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenOctets_Type()
)
adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowFrames_Type = Counter64
_AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowFrames = _AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 20),
    _AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowOctets_Type = Counter64
_AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowOctets = _AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 3, 1, 21),
    _AdGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowOctets_Type()
)
adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer24HrCurrentTable_Object = MibTable
adGenMEFPolicer24HrCurrentTable = _AdGenMEFPolicer24HrCurrentTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4)
)
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentTable.setStatus("current")
_AdGenMEFPolicer24HrCurrentEntry_Object = MibTableRow
adGenMEFPolicer24HrCurrentEntry = _AdGenMEFPolicer24HrCurrentEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1)
)
adGenMEFPolicer24HrCurrentEntry.setIndexNames(
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentEntry.setStatus("current")
_AdGenMEFPolicer24HrCurrentIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer24HrCurrentIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrCurrentIngressGreenFrames = _AdGenMEFPolicer24HrCurrentIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 1),
    _AdGenMEFPolicer24HrCurrentIngressGreenFrames_Type()
)
adGenMEFPolicer24HrCurrentIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrCurrentIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer24HrCurrentIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrCurrentIngressYellowFrames = _AdGenMEFPolicer24HrCurrentIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 2),
    _AdGenMEFPolicer24HrCurrentIngressYellowFrames_Type()
)
adGenMEFPolicer24HrCurrentIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrCurrentIngressRedFrames_Type = Gauge32
_AdGenMEFPolicer24HrCurrentIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer24HrCurrentIngressRedFrames = _AdGenMEFPolicer24HrCurrentIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 3),
    _AdGenMEFPolicer24HrCurrentIngressRedFrames_Type()
)
adGenMEFPolicer24HrCurrentIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentIngressRedFrames.setStatus("current")
_AdGenMEFPolicer24HrCurrentIngressGreenOctets_Type = Gauge32
_AdGenMEFPolicer24HrCurrentIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer24HrCurrentIngressGreenOctets = _AdGenMEFPolicer24HrCurrentIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 4),
    _AdGenMEFPolicer24HrCurrentIngressGreenOctets_Type()
)
adGenMEFPolicer24HrCurrentIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer24HrCurrentIngressYellowOctets_Type = Gauge32
_AdGenMEFPolicer24HrCurrentIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer24HrCurrentIngressYellowOctets = _AdGenMEFPolicer24HrCurrentIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 5),
    _AdGenMEFPolicer24HrCurrentIngressYellowOctets_Type()
)
adGenMEFPolicer24HrCurrentIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer24HrCurrentIngressRedOctets_Type = Gauge32
_AdGenMEFPolicer24HrCurrentIngressRedOctets_Object = MibTableColumn
adGenMEFPolicer24HrCurrentIngressRedOctets = _AdGenMEFPolicer24HrCurrentIngressRedOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 6),
    _AdGenMEFPolicer24HrCurrentIngressRedOctets_Type()
)
adGenMEFPolicer24HrCurrentIngressRedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentIngressRedOctets.setStatus("current")
_AdGenMEFPolicer24HrCurrentCongDiscardsIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer24HrCurrentCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenFrames = _AdGenMEFPolicer24HrCurrentCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 7),
    _AdGenMEFPolicer24HrCurrentCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrCurrentCongDiscardsIngressGreenOctets_Type = Gauge32
_AdGenMEFPolicer24HrCurrentCongDiscardsIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenOctets = _AdGenMEFPolicer24HrCurrentCongDiscardsIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 8),
    _AdGenMEFPolicer24HrCurrentCongDiscardsIngressGreenOctets_Type()
)
adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer24HrCurrentCongDiscardsIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer24HrCurrentCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowFrames = _AdGenMEFPolicer24HrCurrentCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 9),
    _AdGenMEFPolicer24HrCurrentCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrCurrentCongDiscardsIngressYellowOctets_Type = Gauge32
_AdGenMEFPolicer24HrCurrentCongDiscardsIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowOctets = _AdGenMEFPolicer24HrCurrentCongDiscardsIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 10),
    _AdGenMEFPolicer24HrCurrentCongDiscardsIngressYellowOctets_Type()
)
adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer24HrCurrentHCIngressGreenFrames_Type = Counter64
_AdGenMEFPolicer24HrCurrentHCIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrCurrentHCIngressGreenFrames = _AdGenMEFPolicer24HrCurrentHCIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 11),
    _AdGenMEFPolicer24HrCurrentHCIngressGreenFrames_Type()
)
adGenMEFPolicer24HrCurrentHCIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentHCIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrCurrentHCIngressYellowFrames_Type = Counter64
_AdGenMEFPolicer24HrCurrentHCIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrCurrentHCIngressYellowFrames = _AdGenMEFPolicer24HrCurrentHCIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 12),
    _AdGenMEFPolicer24HrCurrentHCIngressYellowFrames_Type()
)
adGenMEFPolicer24HrCurrentHCIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentHCIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrCurrentHCIngressRedFrames_Type = Counter64
_AdGenMEFPolicer24HrCurrentHCIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer24HrCurrentHCIngressRedFrames = _AdGenMEFPolicer24HrCurrentHCIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 13),
    _AdGenMEFPolicer24HrCurrentHCIngressRedFrames_Type()
)
adGenMEFPolicer24HrCurrentHCIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentHCIngressRedFrames.setStatus("current")
_AdGenMEFPolicer24HrCurrentHCIngressGreenOctets_Type = Counter64
_AdGenMEFPolicer24HrCurrentHCIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer24HrCurrentHCIngressGreenOctets = _AdGenMEFPolicer24HrCurrentHCIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 14),
    _AdGenMEFPolicer24HrCurrentHCIngressGreenOctets_Type()
)
adGenMEFPolicer24HrCurrentHCIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentHCIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer24HrCurrentHCIngressYellowOctets_Type = Counter64
_AdGenMEFPolicer24HrCurrentHCIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer24HrCurrentHCIngressYellowOctets = _AdGenMEFPolicer24HrCurrentHCIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 15),
    _AdGenMEFPolicer24HrCurrentHCIngressYellowOctets_Type()
)
adGenMEFPolicer24HrCurrentHCIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentHCIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer24HrCurrentHCIngressRedOctets_Type = Counter64
_AdGenMEFPolicer24HrCurrentHCIngressRedOctets_Object = MibTableColumn
adGenMEFPolicer24HrCurrentHCIngressRedOctets = _AdGenMEFPolicer24HrCurrentHCIngressRedOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 16),
    _AdGenMEFPolicer24HrCurrentHCIngressRedOctets_Type()
)
adGenMEFPolicer24HrCurrentHCIngressRedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentHCIngressRedOctets.setStatus("current")
_AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenFrames_Type = Counter64
_AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenFrames = _AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 17),
    _AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenOctets_Type = Counter64
_AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenOctets = _AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 18),
    _AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenOctets_Type()
)
adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowFrames_Type = Counter64
_AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowFrames = _AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 19),
    _AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowOctets_Type = Counter64
_AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowOctets = _AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 4, 1, 20),
    _AdGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowOctets_Type()
)
adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer24HrIntervalTable_Object = MibTable
adGenMEFPolicer24HrIntervalTable = _AdGenMEFPolicer24HrIntervalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5)
)
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalTable.setStatus("current")
_AdGenMEFPolicer24HrIntervalEntry_Object = MibTableRow
adGenMEFPolicer24HrIntervalEntry = _AdGenMEFPolicer24HrIntervalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1)
)
adGenMEFPolicer24HrIntervalEntry.setIndexNames(
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"),
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalNumber"),
)
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalEntry.setStatus("current")
_AdGenMEFPolicer24HrIntervalNumber_Type = Integer32
_AdGenMEFPolicer24HrIntervalNumber_Object = MibTableColumn
adGenMEFPolicer24HrIntervalNumber = _AdGenMEFPolicer24HrIntervalNumber_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 1),
    _AdGenMEFPolicer24HrIntervalNumber_Type()
)
adGenMEFPolicer24HrIntervalNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalNumber.setStatus("current")
_AdGenMEFPolicer24HrIntervalIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer24HrIntervalIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrIntervalIngressGreenFrames = _AdGenMEFPolicer24HrIntervalIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 2),
    _AdGenMEFPolicer24HrIntervalIngressGreenFrames_Type()
)
adGenMEFPolicer24HrIntervalIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrIntervalIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer24HrIntervalIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrIntervalIngressYellowFrames = _AdGenMEFPolicer24HrIntervalIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 3),
    _AdGenMEFPolicer24HrIntervalIngressYellowFrames_Type()
)
adGenMEFPolicer24HrIntervalIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrIntervalIngressRedFrames_Type = Gauge32
_AdGenMEFPolicer24HrIntervalIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer24HrIntervalIngressRedFrames = _AdGenMEFPolicer24HrIntervalIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 4),
    _AdGenMEFPolicer24HrIntervalIngressRedFrames_Type()
)
adGenMEFPolicer24HrIntervalIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalIngressRedFrames.setStatus("current")
_AdGenMEFPolicer24HrIntervalIngressGreenOctets_Type = Gauge32
_AdGenMEFPolicer24HrIntervalIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer24HrIntervalIngressGreenOctets = _AdGenMEFPolicer24HrIntervalIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 5),
    _AdGenMEFPolicer24HrIntervalIngressGreenOctets_Type()
)
adGenMEFPolicer24HrIntervalIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer24HrIntervalIngressYellowOctets_Type = Gauge32
_AdGenMEFPolicer24HrIntervalIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer24HrIntervalIngressYellowOctets = _AdGenMEFPolicer24HrIntervalIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 6),
    _AdGenMEFPolicer24HrIntervalIngressYellowOctets_Type()
)
adGenMEFPolicer24HrIntervalIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer24HrIntervalIngressRedOctets_Type = Gauge32
_AdGenMEFPolicer24HrIntervalIngressRedOctets_Object = MibTableColumn
adGenMEFPolicer24HrIntervalIngressRedOctets = _AdGenMEFPolicer24HrIntervalIngressRedOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 7),
    _AdGenMEFPolicer24HrIntervalIngressRedOctets_Type()
)
adGenMEFPolicer24HrIntervalIngressRedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalIngressRedOctets.setStatus("current")
_AdGenMEFPolicer24HrIntervalCongDiscardsIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer24HrIntervalCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenFrames = _AdGenMEFPolicer24HrIntervalCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 8),
    _AdGenMEFPolicer24HrIntervalCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrIntervalCongDiscardsIngressGreenOctets_Type = Gauge32
_AdGenMEFPolicer24HrIntervalCongDiscardsIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenOctets = _AdGenMEFPolicer24HrIntervalCongDiscardsIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 9),
    _AdGenMEFPolicer24HrIntervalCongDiscardsIngressGreenOctets_Type()
)
adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer24HrIntervalCongDiscardsIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer24HrIntervalCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowFrames = _AdGenMEFPolicer24HrIntervalCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 10),
    _AdGenMEFPolicer24HrIntervalCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrIntervalCongDiscardsIngressYellowOctets_Type = Gauge32
_AdGenMEFPolicer24HrIntervalCongDiscardsIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowOctets = _AdGenMEFPolicer24HrIntervalCongDiscardsIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 11),
    _AdGenMEFPolicer24HrIntervalCongDiscardsIngressYellowOctets_Type()
)
adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer24HrIntervalHCIngressGreenFrames_Type = Counter64
_AdGenMEFPolicer24HrIntervalHCIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrIntervalHCIngressGreenFrames = _AdGenMEFPolicer24HrIntervalHCIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 12),
    _AdGenMEFPolicer24HrIntervalHCIngressGreenFrames_Type()
)
adGenMEFPolicer24HrIntervalHCIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalHCIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrIntervalHCIngressYellowFrames_Type = Counter64
_AdGenMEFPolicer24HrIntervalHCIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrIntervalHCIngressYellowFrames = _AdGenMEFPolicer24HrIntervalHCIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 13),
    _AdGenMEFPolicer24HrIntervalHCIngressYellowFrames_Type()
)
adGenMEFPolicer24HrIntervalHCIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalHCIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrIntervalHCIngressRedFrames_Type = Counter64
_AdGenMEFPolicer24HrIntervalHCIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer24HrIntervalHCIngressRedFrames = _AdGenMEFPolicer24HrIntervalHCIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 14),
    _AdGenMEFPolicer24HrIntervalHCIngressRedFrames_Type()
)
adGenMEFPolicer24HrIntervalHCIngressRedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalHCIngressRedFrames.setStatus("current")
_AdGenMEFPolicer24HrIntervalHCIngressGreenOctets_Type = Counter64
_AdGenMEFPolicer24HrIntervalHCIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer24HrIntervalHCIngressGreenOctets = _AdGenMEFPolicer24HrIntervalHCIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 15),
    _AdGenMEFPolicer24HrIntervalHCIngressGreenOctets_Type()
)
adGenMEFPolicer24HrIntervalHCIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalHCIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer24HrIntervalHCIngressYellowOctets_Type = Counter64
_AdGenMEFPolicer24HrIntervalHCIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer24HrIntervalHCIngressYellowOctets = _AdGenMEFPolicer24HrIntervalHCIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 16),
    _AdGenMEFPolicer24HrIntervalHCIngressYellowOctets_Type()
)
adGenMEFPolicer24HrIntervalHCIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalHCIngressYellowOctets.setStatus("current")
_AdGenMEFPolicer24HrIntervalHCIngressRedOctets_Type = Counter64
_AdGenMEFPolicer24HrIntervalHCIngressRedOctets_Object = MibTableColumn
adGenMEFPolicer24HrIntervalHCIngressRedOctets = _AdGenMEFPolicer24HrIntervalHCIngressRedOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 17),
    _AdGenMEFPolicer24HrIntervalHCIngressRedOctets_Type()
)
adGenMEFPolicer24HrIntervalHCIngressRedOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalHCIngressRedOctets.setStatus("current")
_AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenFrames_Type = Counter64
_AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenFrames = _AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 18),
    _AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenOctets_Type = Counter64
_AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenOctets_Object = MibTableColumn
adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenOctets = _AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 19),
    _AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenOctets_Type()
)
adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenOctets.setStatus("current")
_AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowFrames_Type = Counter64
_AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowFrames = _AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 20),
    _AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowOctets_Type = Counter64
_AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowOctets_Object = MibTableColumn
adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowOctets = _AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 5, 1, 21),
    _AdGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowOctets_Type()
)
adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowOctets.setStatus("current")
_AdGenMEFPolicerPerfResetTable_Object = MibTable
adGenMEFPolicerPerfResetTable = _AdGenMEFPolicerPerfResetTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 6)
)
if mibBuilder.loadTexts:
    adGenMEFPolicerPerfResetTable.setStatus("current")
_AdGenMEFPolicerPerfResetEntry_Object = MibTableRow
adGenMEFPolicerPerfResetEntry = _AdGenMEFPolicerPerfResetEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 6, 1)
)
adGenMEFPolicerPerfResetEntry.setIndexNames(
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFPolicerPerfResetEntry.setStatus("current")


class _AdGenMEFPolicerPerfReset_Type(Integer32):
    """Custom type adGenMEFPolicerPerfReset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("policerPerfRst", 1)
    )


_AdGenMEFPolicerPerfReset_Type.__name__ = "Integer32"
_AdGenMEFPolicerPerfReset_Object = MibTableColumn
adGenMEFPolicerPerfReset = _AdGenMEFPolicerPerfReset_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 3, 6, 1, 1),
    _AdGenMEFPolicerPerfReset_Type()
)
adGenMEFPolicerPerfReset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicerPerfReset.setStatus("current")
_AdGenMEF10100EthAnomaliesPerfThresholds_ObjectIdentity = ObjectIdentity
adGenMEF10100EthAnomaliesPerfThresholds = _AdGenMEF10100EthAnomaliesPerfThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 4)
)
_AdGenMEF10100EthAnomalies15MinThreshTable_Object = MibTable
adGenMEF10100EthAnomalies15MinThreshTable = _AdGenMEF10100EthAnomalies15MinThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 4, 1)
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies15MinThreshTable.setStatus("current")
_AdGenMEF10100EthAnomalies15MinThreshEntry_Object = MibTableRow
adGenMEF10100EthAnomalies15MinThreshEntry = _AdGenMEF10100EthAnomalies15MinThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 4, 1, 1)
)
adGenMEF10100EthAnomalies15MinThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies15MinThreshEntry.setStatus("current")
_AdGenMEF10100EthAnomalies15MinThreshFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEF10100EthAnomalies15MinThreshFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEF10100EthAnomalies15MinThreshFramesWithInvalidCEVLANID = _AdGenMEF10100EthAnomalies15MinThreshFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 4, 1, 1, 1),
    _AdGenMEF10100EthAnomalies15MinThreshFramesWithInvalidCEVLANID_Type()
)
adGenMEF10100EthAnomalies15MinThreshFramesWithInvalidCEVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies15MinThreshFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEF10100EthAnomalies24HrThreshTable_Object = MibTable
adGenMEF10100EthAnomalies24HrThreshTable = _AdGenMEF10100EthAnomalies24HrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 4, 2)
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies24HrThreshTable.setStatus("current")
_AdGenMEF10100EthAnomalies24HrThreshEntry_Object = MibTableRow
adGenMEF10100EthAnomalies24HrThreshEntry = _AdGenMEF10100EthAnomalies24HrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 4, 2, 1)
)
adGenMEF10100EthAnomalies24HrThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies24HrThreshEntry.setStatus("current")
_AdGenMEF10100EthAnomalies24HrThreshFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEF10100EthAnomalies24HrThreshFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEF10100EthAnomalies24HrThreshFramesWithInvalidCEVLANID = _AdGenMEF10100EthAnomalies24HrThreshFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 4, 2, 1, 1),
    _AdGenMEF10100EthAnomalies24HrThreshFramesWithInvalidCEVLANID_Type()
)
adGenMEF10100EthAnomalies24HrThreshFramesWithInvalidCEVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEF10100EthAnomalies24HrThreshFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEFGigEthAnomaliesPerfThresholds_ObjectIdentity = ObjectIdentity
adGenMEFGigEthAnomaliesPerfThresholds = _AdGenMEFGigEthAnomaliesPerfThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 5)
)
_AdGenMEFGigEthAnomalies15MinThreshTable_Object = MibTable
adGenMEFGigEthAnomalies15MinThreshTable = _AdGenMEFGigEthAnomalies15MinThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 5, 1)
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies15MinThreshTable.setStatus("current")
_AdGenMEFGigEthAnomalies15MinThreshEntry_Object = MibTableRow
adGenMEFGigEthAnomalies15MinThreshEntry = _AdGenMEFGigEthAnomalies15MinThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 5, 1, 1)
)
adGenMEFGigEthAnomalies15MinThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies15MinThreshEntry.setStatus("current")
_AdGenMEFGigEthAnomalies15MinThreshFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEFGigEthAnomalies15MinThreshFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEFGigEthAnomalies15MinThreshFramesWithInvalidCEVLANID = _AdGenMEFGigEthAnomalies15MinThreshFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 5, 1, 1, 1),
    _AdGenMEFGigEthAnomalies15MinThreshFramesWithInvalidCEVLANID_Type()
)
adGenMEFGigEthAnomalies15MinThreshFramesWithInvalidCEVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies15MinThreshFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEFGigEthAnomalies24HrThreshTable_Object = MibTable
adGenMEFGigEthAnomalies24HrThreshTable = _AdGenMEFGigEthAnomalies24HrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 5, 2)
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies24HrThreshTable.setStatus("current")
_AdGenMEFGigEthAnomalies24HrThreshEntry_Object = MibTableRow
adGenMEFGigEthAnomalies24HrThreshEntry = _AdGenMEFGigEthAnomalies24HrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 5, 2, 1)
)
adGenMEFGigEthAnomalies24HrThreshEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies24HrThreshEntry.setStatus("current")
_AdGenMEFGigEthAnomalies24HrThreshFramesWithInvalidCEVLANID_Type = Gauge32
_AdGenMEFGigEthAnomalies24HrThreshFramesWithInvalidCEVLANID_Object = MibTableColumn
adGenMEFGigEthAnomalies24HrThreshFramesWithInvalidCEVLANID = _AdGenMEFGigEthAnomalies24HrThreshFramesWithInvalidCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 5, 2, 1, 1),
    _AdGenMEFGigEthAnomalies24HrThreshFramesWithInvalidCEVLANID_Type()
)
adGenMEFGigEthAnomalies24HrThreshFramesWithInvalidCEVLANID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFGigEthAnomalies24HrThreshFramesWithInvalidCEVLANID.setStatus("current")
_AdGenMEFPolicerPerfThresholds_ObjectIdentity = ObjectIdentity
adGenMEFPolicerPerfThresholds = _AdGenMEFPolicerPerfThresholds_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6)
)
_AdGenMEFPolicer15MinThreshTable_Object = MibTable
adGenMEFPolicer15MinThreshTable = _AdGenMEFPolicer15MinThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1)
)
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThreshTable.setStatus("current")
_AdGenMEFPolicer15MinThreshEntry_Object = MibTableRow
adGenMEFPolicer15MinThreshEntry = _AdGenMEFPolicer15MinThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1)
)
adGenMEFPolicer15MinThreshEntry.setIndexNames(
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThreshEntry.setStatus("current")
_AdGenMEFPolicer15MinThresholdIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer15MinThresholdIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinThresholdIngressGreenFrames = _AdGenMEFPolicer15MinThresholdIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1, 1),
    _AdGenMEFPolicer15MinThresholdIngressGreenFrames_Type()
)
adGenMEFPolicer15MinThresholdIngressGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThresholdIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinThresholdIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer15MinThresholdIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinThresholdIngressYellowFrames = _AdGenMEFPolicer15MinThresholdIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1, 2),
    _AdGenMEFPolicer15MinThresholdIngressYellowFrames_Type()
)
adGenMEFPolicer15MinThresholdIngressYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThresholdIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinThresholdIngressRedFrames_Type = Gauge32
_AdGenMEFPolicer15MinThresholdIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer15MinThresholdIngressRedFrames = _AdGenMEFPolicer15MinThresholdIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1, 3),
    _AdGenMEFPolicer15MinThresholdIngressRedFrames_Type()
)
adGenMEFPolicer15MinThresholdIngressRedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThresholdIngressRedFrames.setStatus("current")
_AdGenMEFPolicer15MinThresholdCongDiscardsIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer15MinThresholdCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinThresholdCongDiscardsIngressGreenFrames = _AdGenMEFPolicer15MinThresholdCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1, 4),
    _AdGenMEFPolicer15MinThresholdCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer15MinThresholdCongDiscardsIngressGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThresholdCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinThresholdCongDiscardsIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer15MinThresholdCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinThresholdCongDiscardsIngressYellowFrames = _AdGenMEFPolicer15MinThresholdCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1, 5),
    _AdGenMEFPolicer15MinThresholdCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer15MinThresholdCongDiscardsIngressYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThresholdCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinThresholdHCIngressGreenFrames_Type = Unsigned64TC
_AdGenMEFPolicer15MinThresholdHCIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinThresholdHCIngressGreenFrames = _AdGenMEFPolicer15MinThresholdHCIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1, 6),
    _AdGenMEFPolicer15MinThresholdHCIngressGreenFrames_Type()
)
adGenMEFPolicer15MinThresholdHCIngressGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThresholdHCIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinThresholdHCIngressYellowFrames_Type = Unsigned64TC
_AdGenMEFPolicer15MinThresholdHCIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinThresholdHCIngressYellowFrames = _AdGenMEFPolicer15MinThresholdHCIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1, 7),
    _AdGenMEFPolicer15MinThresholdHCIngressYellowFrames_Type()
)
adGenMEFPolicer15MinThresholdHCIngressYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThresholdHCIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer15MinThresholdHCIngressRedFrames_Type = Unsigned64TC
_AdGenMEFPolicer15MinThresholdHCIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer15MinThresholdHCIngressRedFrames = _AdGenMEFPolicer15MinThresholdHCIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1, 8),
    _AdGenMEFPolicer15MinThresholdHCIngressRedFrames_Type()
)
adGenMEFPolicer15MinThresholdHCIngressRedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThresholdHCIngressRedFrames.setStatus("current")
_AdGenMEFPolicer15MinThresholdHCCongDiscardsIngressGreenFrames_Type = Unsigned64TC
_AdGenMEFPolicer15MinThresholdHCCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer15MinThresholdHCCongDiscardsIngressGreenFrames = _AdGenMEFPolicer15MinThresholdHCCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1, 9),
    _AdGenMEFPolicer15MinThresholdHCCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer15MinThresholdHCCongDiscardsIngressGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThresholdHCCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer15MinThresholdHCCongDiscardsIngressYellowFrames_Type = Unsigned64TC
_AdGenMEFPolicer15MinThresholdHCCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer15MinThresholdHCCongDiscardsIngressYellowFrames = _AdGenMEFPolicer15MinThresholdHCCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 1, 1, 10),
    _AdGenMEFPolicer15MinThresholdHCCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer15MinThresholdHCCongDiscardsIngressYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer15MinThresholdHCCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrThreshTable_Object = MibTable
adGenMEFPolicer24HrThreshTable = _AdGenMEFPolicer24HrThreshTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2)
)
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThreshTable.setStatus("current")
_AdGenMEFPolicer24HrThreshEntry_Object = MibTableRow
adGenMEFPolicer24HrThreshEntry = _AdGenMEFPolicer24HrThreshEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1)
)
adGenMEFPolicer24HrThreshEntry.setIndexNames(
    (0, "ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"),
)
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThreshEntry.setStatus("current")
_AdGenMEFPolicer24HrThresholdIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer24HrThresholdIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrThresholdIngressGreenFrames = _AdGenMEFPolicer24HrThresholdIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1, 1),
    _AdGenMEFPolicer24HrThresholdIngressGreenFrames_Type()
)
adGenMEFPolicer24HrThresholdIngressGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThresholdIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrThresholdIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer24HrThresholdIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrThresholdIngressYellowFrames = _AdGenMEFPolicer24HrThresholdIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1, 2),
    _AdGenMEFPolicer24HrThresholdIngressYellowFrames_Type()
)
adGenMEFPolicer24HrThresholdIngressYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThresholdIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrThresholdIngressRedFrames_Type = Gauge32
_AdGenMEFPolicer24HrThresholdIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer24HrThresholdIngressRedFrames = _AdGenMEFPolicer24HrThresholdIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1, 3),
    _AdGenMEFPolicer24HrThresholdIngressRedFrames_Type()
)
adGenMEFPolicer24HrThresholdIngressRedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThresholdIngressRedFrames.setStatus("current")
_AdGenMEFPolicer24HrThresholdCongDiscardsIngressGreenFrames_Type = Gauge32
_AdGenMEFPolicer24HrThresholdCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrThresholdCongDiscardsIngressGreenFrames = _AdGenMEFPolicer24HrThresholdCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1, 4),
    _AdGenMEFPolicer24HrThresholdCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer24HrThresholdCongDiscardsIngressGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThresholdCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrThresholdCongDiscardsIngressYellowFrames_Type = Gauge32
_AdGenMEFPolicer24HrThresholdCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrThresholdCongDiscardsIngressYellowFrames = _AdGenMEFPolicer24HrThresholdCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1, 5),
    _AdGenMEFPolicer24HrThresholdCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer24HrThresholdCongDiscardsIngressYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThresholdCongDiscardsIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrThresholdHCIngressGreenFrames_Type = Unsigned64TC
_AdGenMEFPolicer24HrThresholdHCIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrThresholdHCIngressGreenFrames = _AdGenMEFPolicer24HrThresholdHCIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1, 6),
    _AdGenMEFPolicer24HrThresholdHCIngressGreenFrames_Type()
)
adGenMEFPolicer24HrThresholdHCIngressGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThresholdHCIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrThresholdHCIngressYellowFrames_Type = Unsigned64TC
_AdGenMEFPolicer24HrThresholdHCIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrThresholdHCIngressYellowFrames = _AdGenMEFPolicer24HrThresholdHCIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1, 7),
    _AdGenMEFPolicer24HrThresholdHCIngressYellowFrames_Type()
)
adGenMEFPolicer24HrThresholdHCIngressYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThresholdHCIngressYellowFrames.setStatus("current")
_AdGenMEFPolicer24HrThresholdHCIngressRedFrames_Type = Unsigned64TC
_AdGenMEFPolicer24HrThresholdHCIngressRedFrames_Object = MibTableColumn
adGenMEFPolicer24HrThresholdHCIngressRedFrames = _AdGenMEFPolicer24HrThresholdHCIngressRedFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1, 8),
    _AdGenMEFPolicer24HrThresholdHCIngressRedFrames_Type()
)
adGenMEFPolicer24HrThresholdHCIngressRedFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThresholdHCIngressRedFrames.setStatus("current")
_AdGenMEFPolicer24HrThresholdHCCongDiscardsIngressGreenFrames_Type = Unsigned64TC
_AdGenMEFPolicer24HrThresholdHCCongDiscardsIngressGreenFrames_Object = MibTableColumn
adGenMEFPolicer24HrThresholdHCCongDiscardsIngressGreenFrames = _AdGenMEFPolicer24HrThresholdHCCongDiscardsIngressGreenFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1, 9),
    _AdGenMEFPolicer24HrThresholdHCCongDiscardsIngressGreenFrames_Type()
)
adGenMEFPolicer24HrThresholdHCCongDiscardsIngressGreenFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThresholdHCCongDiscardsIngressGreenFrames.setStatus("current")
_AdGenMEFPolicer24HrThresholdHCCongDiscardsIngressYellowFrames_Type = Unsigned64TC
_AdGenMEFPolicer24HrThresholdHCCongDiscardsIngressYellowFrames_Object = MibTableColumn
adGenMEFPolicer24HrThresholdHCCongDiscardsIngressYellowFrames = _AdGenMEFPolicer24HrThresholdHCCongDiscardsIngressYellowFrames_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 6, 6, 2, 1, 10),
    _AdGenMEFPolicer24HrThresholdHCCongDiscardsIngressYellowFrames_Type()
)
adGenMEFPolicer24HrThresholdHCCongDiscardsIngressYellowFrames.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenMEFPolicer24HrThresholdHCCongDiscardsIngressYellowFrames.setStatus("current")

# Managed Objects groups

adGenMEFProvScalarGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 1)
)
adGenMEFProvScalarGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFDeleteAll"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFEVCIndexNext"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapIndexNext"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndexNext"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFEVCEthertype"))
)
if mibBuilder.loadTexts:
    adGenMEFProvScalarGroup.setStatus("current")

adGenMEFProvEVCGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 2)
)
adGenMEFProvEVCGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFEVCIndex"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFEVCRowStatus"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFEVCAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFEVCStatus"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFEVCPort"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFEVCCEVLANIDPreservation"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFEVCVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFEVCMapsByIndex"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFEVCNumMaps"))
)
if mibBuilder.loadTexts:
    adGenMEFProvEVCGroup.setStatus("current")

adGenMEFProvMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 3)
)
adGenMEFProvMapGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFMapIndex"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapRowStatus"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapStatus"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapAssociatedEVCAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapAssociatedEVCIndex"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapUNIPort"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapCEVLANPRI"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapUntagged"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapCoS"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapAttachedProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapAttachedProfileIndex"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapBroadcast"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapMulticast"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapUnicast"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapL2CP"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapMenCTag"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapMenCTagPri"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapDSCPRange"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapIpHost"))
)
if mibBuilder.loadTexts:
    adGenMEFProvMapGroup.setStatus("current")

adGenMEFProvProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 4)
)
adGenMEFProvProfileGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileRowStatus"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileStatus"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileApp"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileUNIPort"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileEVC"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileCoSValue"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileRateCoupling"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileCBS"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileEBS"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAddMap"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileRemoveMap"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileMapsByAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileMapsByIndex"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileDroppedPackets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileCommittedInformationRate"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileExcessInformationRate"))
)
if mibBuilder.loadTexts:
    adGenMEFProvProfileGroup.setStatus("current")

adGenMEFProv10100EthQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 5)
)
adGenMEFProv10100EthQueueGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFQueueWREDTimeConstant"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthCoSIndex"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthQueueMaxDepth"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthQueueWREDState"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthQueueWREDGreenMaxThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthQueueWREDGreenMinThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthQueueWREDGreenDropProb"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthQueueWREDYellowMaxThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthQueueWREDYellowMinThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthQueueWREDYellowDropProb"))
)
if mibBuilder.loadTexts:
    adGenMEFProv10100EthQueueGroup.setStatus("current")

adGenMEFProvGigEthQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 6)
)
adGenMEFProvGigEthQueueGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFQueueWREDTimeConstant"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthCoSIndex"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthQueueMaxDepth"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthQueueWREDState"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthQueueWREDGreenMaxThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthQueueWREDGreenMinThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthQueueWREDGreenDropProb"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthQueueWREDYellowMaxThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthQueueWREDYellowMinThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthQueueWREDYellowDropProb"))
)
if mibBuilder.loadTexts:
    adGenMEFProvGigEthQueueGroup.setStatus("current")

adGenMEFProvBondGrpQueueGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 7)
)
adGenMEFProvBondGrpQueueGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFQueueWREDTimeConstant"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFBondGrpCoSIndex"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFBondGrpQueueMaxDepth"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFBondGrpQueueWREDState"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFBondGrpQueueWREDGreenMaxThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFBondGrpQueueWREDGreenMinThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFBondGrpQueueWREDGreenDropProb"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFBondGrpQueueWREDYellowMaxThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFBondGrpQueueWREDYellowMinThresh"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFBondGrpQueueWREDYellowDropProb"))
)
if mibBuilder.loadTexts:
    adGenMEFProvBondGrpQueueGroup.setStatus("current")

adGenMEFProvUNIGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 8)
)
adGenMEFProvUNIGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFUNIMapsByAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFUNIMapsByIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFProvUNIGroup.setStatus("current")

adGenMEFProvMENGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 9)
)
adGenMEFProvMENGroup.setObjects(
    ("ADTRAN-GENMEF-MIB", "adGenMEFMENVLANIDPool")
)
if mibBuilder.loadTexts:
    adGenMEFProvMENGroup.setStatus("current")

adGenMEFProvQueueCoSMapGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 10)
)
adGenMEFProvQueueCoSMapGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFQueueCoSMapForPri0"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFQueueCoSMapForPri1"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFQueueCoSMapForPri2"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFQueueCoSMapForPri3"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFQueueCoSMapForPri4"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFQueueCoSMapForPri5"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFQueueCoSMapForPri6"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFQueueCoSMapForPri7"))
)
if mibBuilder.loadTexts:
    adGenMEFProvQueueCoSMapGroup.setStatus("current")

adGenMEFPolicerRstPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 11)
)
adGenMEFPolicerRstPerfGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFPolicerRstCurrentIntervals"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicerRstAll"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicerPerfReset"))
)
if mibBuilder.loadTexts:
    adGenMEFPolicerRstPerfGroup.setStatus("current")

adGenMEFPolicerPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 12)
)
adGenMEFPolicerPerfGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentIngressRedOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentHCIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentHCIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentHCIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentHCIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentHCIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentHCIngressRedOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalNumber"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalIngressRedOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalHCIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalHCIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalHCIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalHCIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalHCIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalHCIngressRedOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentIngressRedOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentHCIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentHCIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentHCIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentHCIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentHCIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentHCIngressRedOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalNumber"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalIngressRedOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalHCIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalHCIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalHCIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalHCIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalHCIngressYellowOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalHCIngressRedOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenOctets"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowOctets"))
)
if mibBuilder.loadTexts:
    adGenMEFPolicerPerfGroup.setStatus("current")

adGenMEFEthPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 13)
)
adGenMEFEthPerfGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEF10100EthAnomalies15MinCurrentFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthAnomalies15MinIntervalNumber"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthAnomalies15MinIntervalFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthAnomalies24HrCurrentFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthAnomalies24HrIntervalNumber"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthAnomalies24HrIntervalFramesWithInvalidCEVLANID"))
)
if mibBuilder.loadTexts:
    adGenMEFEthPerfGroup.setStatus("current")

adGenMEFGigEthPerfGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 14)
)
adGenMEFGigEthPerfGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFGigEthAnomalies15MinCurrentFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthAnomalies15MinIntervalNumber"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthAnomalies15MinIntervalFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthAnomalies24HrCurrentFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthAnomalies24HrIntervalNumber"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthAnomalies24HrIntervalFramesWithInvalidCEVLANID"))
)
if mibBuilder.loadTexts:
    adGenMEFGigEthPerfGroup.setStatus("current")

adGenMEFEthThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 15)
)
adGenMEFEthThreshGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEF10100EthAnomalies15MinThreshFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEF10100EthAnomalies24HrThreshFramesWithInvalidCEVLANID"))
)
if mibBuilder.loadTexts:
    adGenMEFEthThreshGroup.setStatus("current")

adGenMEFGigEthThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 16)
)
adGenMEFGigEthThreshGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFGigEthAnomalies15MinThreshFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFGigEthAnomalies24HrThreshFramesWithInvalidCEVLANID"))
)
if mibBuilder.loadTexts:
    adGenMEFGigEthThreshGroup.setStatus("current")

adGenMEFPolicerThreshGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 17)
)
adGenMEFPolicerThreshGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinThresholdIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinThresholdIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinThresholdIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinThresholdCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinThresholdCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinThresholdHCIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinThresholdHCIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinThresholdHCIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinThresholdHCCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer15MinThresholdHCCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrThresholdIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrThresholdIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrThresholdIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrThresholdCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrThresholdCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrThresholdHCIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrThresholdHCIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrThresholdHCIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrThresholdHCCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFPolicer24HrThresholdHCCongDiscardsIngressYellowFrames"))
)
if mibBuilder.loadTexts:
    adGenMEFPolicerThreshGroup.setStatus("current")

adGenMEFDeprecatedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 19)
)
adGenMEFDeprecatedGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFProfileCIR"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileEIR"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFMapDSCP"))
)
if mibBuilder.loadTexts:
    adGenMEFDeprecatedGroup.setStatus("deprecated")

adGenMEFObsoletedGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 20)
)
adGenMEFObsoletedGroup.setObjects(
    ("ADTRAN-GENMEF-MIB", "adGenMEFEVCMapsByAlias")
)
if mibBuilder.loadTexts:
    adGenMEFObsoletedGroup.setStatus("obsolete")


# Notification objects

adGenMEFSet10100EthAnomalies15MinFramesWithInvalidCEVLANID = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 1)
)
adGenMEFSet10100EthAnomalies15MinFramesWithInvalidCEVLANID.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSet10100EthAnomalies15MinFramesWithInvalidCEVLANID.setStatus(
        "current"
    )

adGenMEFSet10100EthAnomalies24HrFramesWithInvalidCEVLANID = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 2)
)
adGenMEFSet10100EthAnomalies24HrFramesWithInvalidCEVLANID.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSet10100EthAnomalies24HrFramesWithInvalidCEVLANID.setStatus(
        "current"
    )

adGenMEFSetGigEthAnomalies15MinFramesWithInvalidCEVLANID = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 3)
)
adGenMEFSetGigEthAnomalies15MinFramesWithInvalidCEVLANID.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetGigEthAnomalies15MinFramesWithInvalidCEVLANID.setStatus(
        "current"
    )

adGenMEFSetGigEthAnomalies24HrFramesWithInvalidCEVLANID = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 4)
)
adGenMEFSetGigEthAnomalies24HrFramesWithInvalidCEVLANID.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENPORT-MIB", "adGenPortTrapIdentifier"),
        ("IF-MIB", "ifIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetGigEthAnomalies24HrFramesWithInvalidCEVLANID.setStatus(
        "current"
    )

adGenMEFSetPolicer15MinIngressGreenFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 5)
)
adGenMEFSetPolicer15MinIngressGreenFrames.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetPolicer15MinIngressGreenFrames.setStatus(
        "current"
    )

adGenMEFSetPolicer15MinIngressYellowFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 6)
)
adGenMEFSetPolicer15MinIngressYellowFrames.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetPolicer15MinIngressYellowFrames.setStatus(
        "current"
    )

adGenMEFSetPolicer15MinIngressRedFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 7)
)
adGenMEFSetPolicer15MinIngressRedFrames.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetPolicer15MinIngressRedFrames.setStatus(
        "current"
    )

adGenMEFSetPolicer15MinCongDiscardsIngressGreenFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 8)
)
adGenMEFSetPolicer15MinCongDiscardsIngressGreenFrames.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetPolicer15MinCongDiscardsIngressGreenFrames.setStatus(
        "current"
    )

adGenMEFSetPolicer15MinCongDiscardsIngressYellowFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 9)
)
adGenMEFSetPolicer15MinCongDiscardsIngressYellowFrames.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetPolicer15MinCongDiscardsIngressYellowFrames.setStatus(
        "current"
    )

adGenMEFSetPolicer24HrIngressGreenFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 10)
)
adGenMEFSetPolicer24HrIngressGreenFrames.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetPolicer24HrIngressGreenFrames.setStatus(
        "current"
    )

adGenMEFSetPolicer24HrIngressYellowFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 11)
)
adGenMEFSetPolicer24HrIngressYellowFrames.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetPolicer24HrIngressYellowFrames.setStatus(
        "current"
    )

adGenMEFSetPolicer24HrIngressRedFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 12)
)
adGenMEFSetPolicer24HrIngressRedFrames.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetPolicer24HrIngressRedFrames.setStatus(
        "current"
    )

adGenMEFSetPolicer24HrCongDiscardsIngressGreenFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 13)
)
adGenMEFSetPolicer24HrCongDiscardsIngressGreenFrames.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetPolicer24HrCongDiscardsIngressGreenFrames.setStatus(
        "current"
    )

adGenMEFSetPolicer24HrCongDiscardsIngressYellowFrames = NotificationType(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 0, 14)
)
adGenMEFSetPolicer24HrCongDiscardsIngressYellowFrames.setObjects(
      *(("SNMPv2-MIB", "sysName"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileAlias"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFProfileIndex"))
)
if mibBuilder.loadTexts:
    adGenMEFSetPolicer24HrCongDiscardsIngressYellowFrames.setStatus(
        "current"
    )


# Notifications groups

adGenMEFEventGroup = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 664, 5, 69, 1, 5, 1, 18)
)
adGenMEFEventGroup.setObjects(
      *(("ADTRAN-GENMEF-MIB", "adGenMEFSet10100EthAnomalies15MinFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSet10100EthAnomalies24HrFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetGigEthAnomalies15MinFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetGigEthAnomalies24HrFramesWithInvalidCEVLANID"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetPolicer15MinIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetPolicer15MinIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetPolicer15MinIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetPolicer15MinCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetPolicer15MinCongDiscardsIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetPolicer24HrIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetPolicer24HrIngressYellowFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetPolicer24HrIngressRedFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetPolicer24HrCongDiscardsIngressGreenFrames"),
        ("ADTRAN-GENMEF-MIB", "adGenMEFSetPolicer24HrCongDiscardsIngressYellowFrames"))
)
if mibBuilder.loadTexts:
    adGenMEFEventGroup.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENMEF-MIB",
    **{"adGenMEFEvents": adGenMEFEvents,
       "adGenMEFSet10100EthAnomalies15MinFramesWithInvalidCEVLANID": adGenMEFSet10100EthAnomalies15MinFramesWithInvalidCEVLANID,
       "adGenMEFSet10100EthAnomalies24HrFramesWithInvalidCEVLANID": adGenMEFSet10100EthAnomalies24HrFramesWithInvalidCEVLANID,
       "adGenMEFSetGigEthAnomalies15MinFramesWithInvalidCEVLANID": adGenMEFSetGigEthAnomalies15MinFramesWithInvalidCEVLANID,
       "adGenMEFSetGigEthAnomalies24HrFramesWithInvalidCEVLANID": adGenMEFSetGigEthAnomalies24HrFramesWithInvalidCEVLANID,
       "adGenMEFSetPolicer15MinIngressGreenFrames": adGenMEFSetPolicer15MinIngressGreenFrames,
       "adGenMEFSetPolicer15MinIngressYellowFrames": adGenMEFSetPolicer15MinIngressYellowFrames,
       "adGenMEFSetPolicer15MinIngressRedFrames": adGenMEFSetPolicer15MinIngressRedFrames,
       "adGenMEFSetPolicer15MinCongDiscardsIngressGreenFrames": adGenMEFSetPolicer15MinCongDiscardsIngressGreenFrames,
       "adGenMEFSetPolicer15MinCongDiscardsIngressYellowFrames": adGenMEFSetPolicer15MinCongDiscardsIngressYellowFrames,
       "adGenMEFSetPolicer24HrIngressGreenFrames": adGenMEFSetPolicer24HrIngressGreenFrames,
       "adGenMEFSetPolicer24HrIngressYellowFrames": adGenMEFSetPolicer24HrIngressYellowFrames,
       "adGenMEFSetPolicer24HrIngressRedFrames": adGenMEFSetPolicer24HrIngressRedFrames,
       "adGenMEFSetPolicer24HrCongDiscardsIngressGreenFrames": adGenMEFSetPolicer24HrCongDiscardsIngressGreenFrames,
       "adGenMEFSetPolicer24HrCongDiscardsIngressYellowFrames": adGenMEFSetPolicer24HrCongDiscardsIngressYellowFrames,
       "adGenMEFProvisioning": adGenMEFProvisioning,
       "adGenMEFProvisioningScalars": adGenMEFProvisioningScalars,
       "adGenMEFDeleteAll": adGenMEFDeleteAll,
       "adGenMEFEVCIndexNext": adGenMEFEVCIndexNext,
       "adGenMEFMapIndexNext": adGenMEFMapIndexNext,
       "adGenMEFProfileIndexNext": adGenMEFProfileIndexNext,
       "adGenMEFEVCEthertype": adGenMEFEVCEthertype,
       "adGenMEFEVCsTable": adGenMEFEVCsTable,
       "adGenMEFEVCsEntry": adGenMEFEVCsEntry,
       "adGenMEFEVCIndex": adGenMEFEVCIndex,
       "adGenMEFEVCRowStatus": adGenMEFEVCRowStatus,
       "adGenMEFEVCAlias": adGenMEFEVCAlias,
       "adGenMEFEVCStatus": adGenMEFEVCStatus,
       "adGenMEFEVCPort": adGenMEFEVCPort,
       "adGenMEFEVCCEVLANIDPreservation": adGenMEFEVCCEVLANIDPreservation,
       "adGenMEFEVCVLANID": adGenMEFEVCVLANID,
       "adGenMEFEVCMapsByAlias": adGenMEFEVCMapsByAlias,
       "adGenMEFEVCMapsByIndex": adGenMEFEVCMapsByIndex,
       "adGenMEFEVCNumMaps": adGenMEFEVCNumMaps,
       "adGenMEFMapsTable": adGenMEFMapsTable,
       "adGenMEFMapsEntry": adGenMEFMapsEntry,
       "adGenMEFMapIndex": adGenMEFMapIndex,
       "adGenMEFMapRowStatus": adGenMEFMapRowStatus,
       "adGenMEFMapAlias": adGenMEFMapAlias,
       "adGenMEFMapStatus": adGenMEFMapStatus,
       "adGenMEFMapAssociatedEVCAlias": adGenMEFMapAssociatedEVCAlias,
       "adGenMEFMapAssociatedEVCIndex": adGenMEFMapAssociatedEVCIndex,
       "adGenMEFMapUNIPort": adGenMEFMapUNIPort,
       "adGenMEFMapCEVLANID": adGenMEFMapCEVLANID,
       "adGenMEFMapCEVLANPRI": adGenMEFMapCEVLANPRI,
       "adGenMEFMapDSCP": adGenMEFMapDSCP,
       "adGenMEFMapUntagged": adGenMEFMapUntagged,
       "adGenMEFMapCoS": adGenMEFMapCoS,
       "adGenMEFMapAttachedProfileAlias": adGenMEFMapAttachedProfileAlias,
       "adGenMEFMapAttachedProfileIndex": adGenMEFMapAttachedProfileIndex,
       "adGenMEFMapBroadcast": adGenMEFMapBroadcast,
       "adGenMEFMapMulticast": adGenMEFMapMulticast,
       "adGenMEFMapUnicast": adGenMEFMapUnicast,
       "adGenMEFMapL2CP": adGenMEFMapL2CP,
       "adGenMEFMapMenCTag": adGenMEFMapMenCTag,
       "adGenMEFMapMenCTagPri": adGenMEFMapMenCTagPri,
       "adGenMEFMapDSCPRange": adGenMEFMapDSCPRange,
       "adGenMEFMapIpHost": adGenMEFMapIpHost,
       "adGenMEFProfilesTable": adGenMEFProfilesTable,
       "adGenMEFProfilesEntry": adGenMEFProfilesEntry,
       "adGenMEFProfileIndex": adGenMEFProfileIndex,
       "adGenMEFProfileRowStatus": adGenMEFProfileRowStatus,
       "adGenMEFProfileAlias": adGenMEFProfileAlias,
       "adGenMEFProfileStatus": adGenMEFProfileStatus,
       "adGenMEFProfileApp": adGenMEFProfileApp,
       "adGenMEFProfileUNIPort": adGenMEFProfileUNIPort,
       "adGenMEFProfileEVC": adGenMEFProfileEVC,
       "adGenMEFProfileCoSValue": adGenMEFProfileCoSValue,
       "adGenMEFProfileRateCoupling": adGenMEFProfileRateCoupling,
       "adGenMEFProfileCIR": adGenMEFProfileCIR,
       "adGenMEFProfileCBS": adGenMEFProfileCBS,
       "adGenMEFProfileEIR": adGenMEFProfileEIR,
       "adGenMEFProfileEBS": adGenMEFProfileEBS,
       "adGenMEFProfileAddMap": adGenMEFProfileAddMap,
       "adGenMEFProfileRemoveMap": adGenMEFProfileRemoveMap,
       "adGenMEFProfileMapsByAlias": adGenMEFProfileMapsByAlias,
       "adGenMEFProfileMapsByIndex": adGenMEFProfileMapsByIndex,
       "adGenMEFProfileDroppedPackets": adGenMEFProfileDroppedPackets,
       "adGenMEFProfileCommittedInformationRate": adGenMEFProfileCommittedInformationRate,
       "adGenMEFProfileExcessInformationRate": adGenMEFProfileExcessInformationRate,
       "adGenMEFQueueScalars": adGenMEFQueueScalars,
       "adGenMEFQueueWREDTimeConstant": adGenMEFQueueWREDTimeConstant,
       "adGenMEFQueueCoSMapForPri0": adGenMEFQueueCoSMapForPri0,
       "adGenMEFQueueCoSMapForPri1": adGenMEFQueueCoSMapForPri1,
       "adGenMEFQueueCoSMapForPri2": adGenMEFQueueCoSMapForPri2,
       "adGenMEFQueueCoSMapForPri3": adGenMEFQueueCoSMapForPri3,
       "adGenMEFQueueCoSMapForPri4": adGenMEFQueueCoSMapForPri4,
       "adGenMEFQueueCoSMapForPri5": adGenMEFQueueCoSMapForPri5,
       "adGenMEFQueueCoSMapForPri6": adGenMEFQueueCoSMapForPri6,
       "adGenMEFQueueCoSMapForPri7": adGenMEFQueueCoSMapForPri7,
       "adGenMEFQosUntagged": adGenMEFQosUntagged,
       "adGenMEF10100EthQueuesTable": adGenMEF10100EthQueuesTable,
       "adGenMEF10100EthQueuesEntry": adGenMEF10100EthQueuesEntry,
       "adGenMEF10100EthCoSIndex": adGenMEF10100EthCoSIndex,
       "adGenMEF10100EthQueueMaxDepth": adGenMEF10100EthQueueMaxDepth,
       "adGenMEF10100EthQueueWREDState": adGenMEF10100EthQueueWREDState,
       "adGenMEF10100EthQueueWREDGreenMaxThresh": adGenMEF10100EthQueueWREDGreenMaxThresh,
       "adGenMEF10100EthQueueWREDGreenMinThresh": adGenMEF10100EthQueueWREDGreenMinThresh,
       "adGenMEF10100EthQueueWREDGreenDropProb": adGenMEF10100EthQueueWREDGreenDropProb,
       "adGenMEF10100EthQueueWREDYellowMaxThresh": adGenMEF10100EthQueueWREDYellowMaxThresh,
       "adGenMEF10100EthQueueWREDYellowMinThresh": adGenMEF10100EthQueueWREDYellowMinThresh,
       "adGenMEF10100EthQueueWREDYellowDropProb": adGenMEF10100EthQueueWREDYellowDropProb,
       "adGenMEFGigEthQueuesTable": adGenMEFGigEthQueuesTable,
       "adGenMEFGigEthQueuesEntry": adGenMEFGigEthQueuesEntry,
       "adGenMEFGigEthCoSIndex": adGenMEFGigEthCoSIndex,
       "adGenMEFGigEthQueueMaxDepth": adGenMEFGigEthQueueMaxDepth,
       "adGenMEFGigEthQueueWREDState": adGenMEFGigEthQueueWREDState,
       "adGenMEFGigEthQueueWREDGreenMaxThresh": adGenMEFGigEthQueueWREDGreenMaxThresh,
       "adGenMEFGigEthQueueWREDGreenMinThresh": adGenMEFGigEthQueueWREDGreenMinThresh,
       "adGenMEFGigEthQueueWREDGreenDropProb": adGenMEFGigEthQueueWREDGreenDropProb,
       "adGenMEFGigEthQueueWREDYellowMaxThresh": adGenMEFGigEthQueueWREDYellowMaxThresh,
       "adGenMEFGigEthQueueWREDYellowMinThresh": adGenMEFGigEthQueueWREDYellowMinThresh,
       "adGenMEFGigEthQueueWREDYellowDropProb": adGenMEFGigEthQueueWREDYellowDropProb,
       "adGenMEFBondGrpQueuesTable": adGenMEFBondGrpQueuesTable,
       "adGenMEFBondGrpQueuesEntry": adGenMEFBondGrpQueuesEntry,
       "adGenMEFBondGrpCoSIndex": adGenMEFBondGrpCoSIndex,
       "adGenMEFBondGrpQueueMaxDepth": adGenMEFBondGrpQueueMaxDepth,
       "adGenMEFBondGrpQueueWREDState": adGenMEFBondGrpQueueWREDState,
       "adGenMEFBondGrpQueueWREDGreenMaxThresh": adGenMEFBondGrpQueueWREDGreenMaxThresh,
       "adGenMEFBondGrpQueueWREDGreenMinThresh": adGenMEFBondGrpQueueWREDGreenMinThresh,
       "adGenMEFBondGrpQueueWREDGreenDropProb": adGenMEFBondGrpQueueWREDGreenDropProb,
       "adGenMEFBondGrpQueueWREDYellowMaxThresh": adGenMEFBondGrpQueueWREDYellowMaxThresh,
       "adGenMEFBondGrpQueueWREDYellowMinThresh": adGenMEFBondGrpQueueWREDYellowMinThresh,
       "adGenMEFBondGrpQueueWREDYellowDropProb": adGenMEFBondGrpQueueWREDYellowDropProb,
       "adGenMEFUNITable": adGenMEFUNITable,
       "adGenMEFUNIEntry": adGenMEFUNIEntry,
       "adGenMEFUNIMapsByAlias": adGenMEFUNIMapsByAlias,
       "adGenMEFUNIMapsByIndex": adGenMEFUNIMapsByIndex,
       "adGenMEFMENTable": adGenMEFMENTable,
       "adGenMEFMENEntry": adGenMEFMENEntry,
       "adGenMEFMENVLANIDPool": adGenMEFMENVLANIDPool,
       "adGenMEFMibConformance": adGenMEFMibConformance,
       "adGenMEFMibGroups": adGenMEFMibGroups,
       "adGenMEFProvScalarGroup": adGenMEFProvScalarGroup,
       "adGenMEFProvEVCGroup": adGenMEFProvEVCGroup,
       "adGenMEFProvMapGroup": adGenMEFProvMapGroup,
       "adGenMEFProvProfileGroup": adGenMEFProvProfileGroup,
       "adGenMEFProv10100EthQueueGroup": adGenMEFProv10100EthQueueGroup,
       "adGenMEFProvGigEthQueueGroup": adGenMEFProvGigEthQueueGroup,
       "adGenMEFProvBondGrpQueueGroup": adGenMEFProvBondGrpQueueGroup,
       "adGenMEFProvUNIGroup": adGenMEFProvUNIGroup,
       "adGenMEFProvMENGroup": adGenMEFProvMENGroup,
       "adGenMEFProvQueueCoSMapGroup": adGenMEFProvQueueCoSMapGroup,
       "adGenMEFPolicerRstPerfGroup": adGenMEFPolicerRstPerfGroup,
       "adGenMEFPolicerPerfGroup": adGenMEFPolicerPerfGroup,
       "adGenMEFEthPerfGroup": adGenMEFEthPerfGroup,
       "adGenMEFGigEthPerfGroup": adGenMEFGigEthPerfGroup,
       "adGenMEFEthThreshGroup": adGenMEFEthThreshGroup,
       "adGenMEFGigEthThreshGroup": adGenMEFGigEthThreshGroup,
       "adGenMEFPolicerThreshGroup": adGenMEFPolicerThreshGroup,
       "adGenMEFEventGroup": adGenMEFEventGroup,
       "adGenMEFDeprecatedGroup": adGenMEFDeprecatedGroup,
       "adGenMEFObsoletedGroup": adGenMEFObsoletedGroup,
       "adGenMEFPerformance": adGenMEFPerformance,
       "adGenMEF10100EthAnomaliesPerformance": adGenMEF10100EthAnomaliesPerformance,
       "adGenMEF10100EthAnomalies15MinCurrentTable": adGenMEF10100EthAnomalies15MinCurrentTable,
       "adGenMEF10100EthAnomalies15MinCurrentEntry": adGenMEF10100EthAnomalies15MinCurrentEntry,
       "adGenMEF10100EthAnomalies15MinCurrentFramesWithInvalidCEVLANID": adGenMEF10100EthAnomalies15MinCurrentFramesWithInvalidCEVLANID,
       "adGenMEF10100EthAnomalies15MinIntervalTable": adGenMEF10100EthAnomalies15MinIntervalTable,
       "adGenMEF10100EthAnomalies15MinIntervalEntry": adGenMEF10100EthAnomalies15MinIntervalEntry,
       "adGenMEF10100EthAnomalies15MinIntervalNumber": adGenMEF10100EthAnomalies15MinIntervalNumber,
       "adGenMEF10100EthAnomalies15MinIntervalFramesWithInvalidCEVLANID": adGenMEF10100EthAnomalies15MinIntervalFramesWithInvalidCEVLANID,
       "adGenMEF10100EthAnomalies24HrCurrentTable": adGenMEF10100EthAnomalies24HrCurrentTable,
       "adGenMEF10100EthAnomalies24HrCurrentEntry": adGenMEF10100EthAnomalies24HrCurrentEntry,
       "adGenMEF10100EthAnomalies24HrCurrentFramesWithInvalidCEVLANID": adGenMEF10100EthAnomalies24HrCurrentFramesWithInvalidCEVLANID,
       "adGenMEF10100EthAnomalies24HrIntervalTable": adGenMEF10100EthAnomalies24HrIntervalTable,
       "adGenMEF10100EthAnomalies24HrIntervalEntry": adGenMEF10100EthAnomalies24HrIntervalEntry,
       "adGenMEF10100EthAnomalies24HrIntervalNumber": adGenMEF10100EthAnomalies24HrIntervalNumber,
       "adGenMEF10100EthAnomalies24HrIntervalFramesWithInvalidCEVLANID": adGenMEF10100EthAnomalies24HrIntervalFramesWithInvalidCEVLANID,
       "adGenMEFGigEthAnomaliesPerformance": adGenMEFGigEthAnomaliesPerformance,
       "adGenMEFGigEthAnomalies15MinCurrentTable": adGenMEFGigEthAnomalies15MinCurrentTable,
       "adGenMEFGigEthAnomalies15MinCurrentEntry": adGenMEFGigEthAnomalies15MinCurrentEntry,
       "adGenMEFGigEthAnomalies15MinCurrentFramesWithInvalidCEVLANID": adGenMEFGigEthAnomalies15MinCurrentFramesWithInvalidCEVLANID,
       "adGenMEFGigEthAnomalies15MinIntervalTable": adGenMEFGigEthAnomalies15MinIntervalTable,
       "adGenMEFGigEthAnomalies15MinIntervalEntry": adGenMEFGigEthAnomalies15MinIntervalEntry,
       "adGenMEFGigEthAnomalies15MinIntervalNumber": adGenMEFGigEthAnomalies15MinIntervalNumber,
       "adGenMEFGigEthAnomalies15MinIntervalFramesWithInvalidCEVLANID": adGenMEFGigEthAnomalies15MinIntervalFramesWithInvalidCEVLANID,
       "adGenMEFGigEthAnomalies24HrCurrentTable": adGenMEFGigEthAnomalies24HrCurrentTable,
       "adGenMEFGigEthAnomalies24HrCurrentEntry": adGenMEFGigEthAnomalies24HrCurrentEntry,
       "adGenMEFGigEthAnomalies24HrCurrentFramesWithInvalidCEVLANID": adGenMEFGigEthAnomalies24HrCurrentFramesWithInvalidCEVLANID,
       "adGenMEFGigEthAnomalies24HrIntervalTable": adGenMEFGigEthAnomalies24HrIntervalTable,
       "adGenMEFGigEthAnomalies24HrIntervalEntry": adGenMEFGigEthAnomalies24HrIntervalEntry,
       "adGenMEFGigEthAnomalies24HrIntervalNumber": adGenMEFGigEthAnomalies24HrIntervalNumber,
       "adGenMEFGigEthAnomalies24HrIntervalFramesWithInvalidCEVLANID": adGenMEFGigEthAnomalies24HrIntervalFramesWithInvalidCEVLANID,
       "adGenMEFPolicerPerformance": adGenMEFPolicerPerformance,
       "adGenMEFPolicerPerformanceScalars": adGenMEFPolicerPerformanceScalars,
       "adGenMEFPolicerRstCurrentIntervals": adGenMEFPolicerRstCurrentIntervals,
       "adGenMEFPolicerRstAll": adGenMEFPolicerRstAll,
       "adGenMEFPolicer15MinCurrentTable": adGenMEFPolicer15MinCurrentTable,
       "adGenMEFPolicer15MinCurrentEntry": adGenMEFPolicer15MinCurrentEntry,
       "adGenMEFPolicer15MinCurrentIngressGreenFrames": adGenMEFPolicer15MinCurrentIngressGreenFrames,
       "adGenMEFPolicer15MinCurrentIngressYellowFrames": adGenMEFPolicer15MinCurrentIngressYellowFrames,
       "adGenMEFPolicer15MinCurrentIngressRedFrames": adGenMEFPolicer15MinCurrentIngressRedFrames,
       "adGenMEFPolicer15MinCurrentIngressGreenOctets": adGenMEFPolicer15MinCurrentIngressGreenOctets,
       "adGenMEFPolicer15MinCurrentIngressYellowOctets": adGenMEFPolicer15MinCurrentIngressYellowOctets,
       "adGenMEFPolicer15MinCurrentIngressRedOctets": adGenMEFPolicer15MinCurrentIngressRedOctets,
       "adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenFrames": adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenOctets": adGenMEFPolicer15MinCurrentCongDiscardsIngressGreenOctets,
       "adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowFrames": adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowOctets": adGenMEFPolicer15MinCurrentCongDiscardsIngressYellowOctets,
       "adGenMEFPolicer15MinCurrentHCIngressGreenFrames": adGenMEFPolicer15MinCurrentHCIngressGreenFrames,
       "adGenMEFPolicer15MinCurrentHCIngressYellowFrames": adGenMEFPolicer15MinCurrentHCIngressYellowFrames,
       "adGenMEFPolicer15MinCurrentHCIngressRedFrames": adGenMEFPolicer15MinCurrentHCIngressRedFrames,
       "adGenMEFPolicer15MinCurrentHCIngressGreenOctets": adGenMEFPolicer15MinCurrentHCIngressGreenOctets,
       "adGenMEFPolicer15MinCurrentHCIngressYellowOctets": adGenMEFPolicer15MinCurrentHCIngressYellowOctets,
       "adGenMEFPolicer15MinCurrentHCIngressRedOctets": adGenMEFPolicer15MinCurrentHCIngressRedOctets,
       "adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenFrames": adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenOctets": adGenMEFPolicer15MinCurrentHCCongDiscardsIngressGreenOctets,
       "adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowFrames": adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowOctets": adGenMEFPolicer15MinCurrentHCCongDiscardsIngressYellowOctets,
       "adGenMEFPolicer15MinIntervalTable": adGenMEFPolicer15MinIntervalTable,
       "adGenMEFPolicer15MinIntervalEntry": adGenMEFPolicer15MinIntervalEntry,
       "adGenMEFPolicer15MinIntervalNumber": adGenMEFPolicer15MinIntervalNumber,
       "adGenMEFPolicer15MinIntervalIngressGreenFrames": adGenMEFPolicer15MinIntervalIngressGreenFrames,
       "adGenMEFPolicer15MinIntervalIngressYellowFrames": adGenMEFPolicer15MinIntervalIngressYellowFrames,
       "adGenMEFPolicer15MinIntervalIngressRedFrames": adGenMEFPolicer15MinIntervalIngressRedFrames,
       "adGenMEFPolicer15MinIntervalIngressGreenOctets": adGenMEFPolicer15MinIntervalIngressGreenOctets,
       "adGenMEFPolicer15MinIntervalIngressYellowOctets": adGenMEFPolicer15MinIntervalIngressYellowOctets,
       "adGenMEFPolicer15MinIntervalIngressRedOctets": adGenMEFPolicer15MinIntervalIngressRedOctets,
       "adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenFrames": adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenOctets": adGenMEFPolicer15MinIntervalCongDiscardsIngressGreenOctets,
       "adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowFrames": adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowOctets": adGenMEFPolicer15MinIntervalCongDiscardsIngressYellowOctets,
       "adGenMEFPolicer15MinIntervalHCIngressGreenFrames": adGenMEFPolicer15MinIntervalHCIngressGreenFrames,
       "adGenMEFPolicer15MinIntervalHCIngressYellowFrames": adGenMEFPolicer15MinIntervalHCIngressYellowFrames,
       "adGenMEFPolicer15MinIntervalHCIngressRedFrames": adGenMEFPolicer15MinIntervalHCIngressRedFrames,
       "adGenMEFPolicer15MinIntervalHCIngressGreenOctets": adGenMEFPolicer15MinIntervalHCIngressGreenOctets,
       "adGenMEFPolicer15MinIntervalHCIngressYellowOctets": adGenMEFPolicer15MinIntervalHCIngressYellowOctets,
       "adGenMEFPolicer15MinIntervalHCIngressRedOctets": adGenMEFPolicer15MinIntervalHCIngressRedOctets,
       "adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenFrames": adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenOctets": adGenMEFPolicer15MinIntervalHCCongDiscardsIngressGreenOctets,
       "adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowFrames": adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowOctets": adGenMEFPolicer15MinIntervalHCCongDiscardsIngressYellowOctets,
       "adGenMEFPolicer24HrCurrentTable": adGenMEFPolicer24HrCurrentTable,
       "adGenMEFPolicer24HrCurrentEntry": adGenMEFPolicer24HrCurrentEntry,
       "adGenMEFPolicer24HrCurrentIngressGreenFrames": adGenMEFPolicer24HrCurrentIngressGreenFrames,
       "adGenMEFPolicer24HrCurrentIngressYellowFrames": adGenMEFPolicer24HrCurrentIngressYellowFrames,
       "adGenMEFPolicer24HrCurrentIngressRedFrames": adGenMEFPolicer24HrCurrentIngressRedFrames,
       "adGenMEFPolicer24HrCurrentIngressGreenOctets": adGenMEFPolicer24HrCurrentIngressGreenOctets,
       "adGenMEFPolicer24HrCurrentIngressYellowOctets": adGenMEFPolicer24HrCurrentIngressYellowOctets,
       "adGenMEFPolicer24HrCurrentIngressRedOctets": adGenMEFPolicer24HrCurrentIngressRedOctets,
       "adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenFrames": adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenOctets": adGenMEFPolicer24HrCurrentCongDiscardsIngressGreenOctets,
       "adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowFrames": adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowOctets": adGenMEFPolicer24HrCurrentCongDiscardsIngressYellowOctets,
       "adGenMEFPolicer24HrCurrentHCIngressGreenFrames": adGenMEFPolicer24HrCurrentHCIngressGreenFrames,
       "adGenMEFPolicer24HrCurrentHCIngressYellowFrames": adGenMEFPolicer24HrCurrentHCIngressYellowFrames,
       "adGenMEFPolicer24HrCurrentHCIngressRedFrames": adGenMEFPolicer24HrCurrentHCIngressRedFrames,
       "adGenMEFPolicer24HrCurrentHCIngressGreenOctets": adGenMEFPolicer24HrCurrentHCIngressGreenOctets,
       "adGenMEFPolicer24HrCurrentHCIngressYellowOctets": adGenMEFPolicer24HrCurrentHCIngressYellowOctets,
       "adGenMEFPolicer24HrCurrentHCIngressRedOctets": adGenMEFPolicer24HrCurrentHCIngressRedOctets,
       "adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenFrames": adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenOctets": adGenMEFPolicer24HrCurrentHCCongDiscardsIngressGreenOctets,
       "adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowFrames": adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowOctets": adGenMEFPolicer24HrCurrentHCCongDiscardsIngressYellowOctets,
       "adGenMEFPolicer24HrIntervalTable": adGenMEFPolicer24HrIntervalTable,
       "adGenMEFPolicer24HrIntervalEntry": adGenMEFPolicer24HrIntervalEntry,
       "adGenMEFPolicer24HrIntervalNumber": adGenMEFPolicer24HrIntervalNumber,
       "adGenMEFPolicer24HrIntervalIngressGreenFrames": adGenMEFPolicer24HrIntervalIngressGreenFrames,
       "adGenMEFPolicer24HrIntervalIngressYellowFrames": adGenMEFPolicer24HrIntervalIngressYellowFrames,
       "adGenMEFPolicer24HrIntervalIngressRedFrames": adGenMEFPolicer24HrIntervalIngressRedFrames,
       "adGenMEFPolicer24HrIntervalIngressGreenOctets": adGenMEFPolicer24HrIntervalIngressGreenOctets,
       "adGenMEFPolicer24HrIntervalIngressYellowOctets": adGenMEFPolicer24HrIntervalIngressYellowOctets,
       "adGenMEFPolicer24HrIntervalIngressRedOctets": adGenMEFPolicer24HrIntervalIngressRedOctets,
       "adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenFrames": adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenOctets": adGenMEFPolicer24HrIntervalCongDiscardsIngressGreenOctets,
       "adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowFrames": adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowOctets": adGenMEFPolicer24HrIntervalCongDiscardsIngressYellowOctets,
       "adGenMEFPolicer24HrIntervalHCIngressGreenFrames": adGenMEFPolicer24HrIntervalHCIngressGreenFrames,
       "adGenMEFPolicer24HrIntervalHCIngressYellowFrames": adGenMEFPolicer24HrIntervalHCIngressYellowFrames,
       "adGenMEFPolicer24HrIntervalHCIngressRedFrames": adGenMEFPolicer24HrIntervalHCIngressRedFrames,
       "adGenMEFPolicer24HrIntervalHCIngressGreenOctets": adGenMEFPolicer24HrIntervalHCIngressGreenOctets,
       "adGenMEFPolicer24HrIntervalHCIngressYellowOctets": adGenMEFPolicer24HrIntervalHCIngressYellowOctets,
       "adGenMEFPolicer24HrIntervalHCIngressRedOctets": adGenMEFPolicer24HrIntervalHCIngressRedOctets,
       "adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenFrames": adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenOctets": adGenMEFPolicer24HrIntervalHCCongDiscardsIngressGreenOctets,
       "adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowFrames": adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowOctets": adGenMEFPolicer24HrIntervalHCCongDiscardsIngressYellowOctets,
       "adGenMEFPolicerPerfResetTable": adGenMEFPolicerPerfResetTable,
       "adGenMEFPolicerPerfResetEntry": adGenMEFPolicerPerfResetEntry,
       "adGenMEFPolicerPerfReset": adGenMEFPolicerPerfReset,
       "adGenMEF10100EthAnomaliesPerfThresholds": adGenMEF10100EthAnomaliesPerfThresholds,
       "adGenMEF10100EthAnomalies15MinThreshTable": adGenMEF10100EthAnomalies15MinThreshTable,
       "adGenMEF10100EthAnomalies15MinThreshEntry": adGenMEF10100EthAnomalies15MinThreshEntry,
       "adGenMEF10100EthAnomalies15MinThreshFramesWithInvalidCEVLANID": adGenMEF10100EthAnomalies15MinThreshFramesWithInvalidCEVLANID,
       "adGenMEF10100EthAnomalies24HrThreshTable": adGenMEF10100EthAnomalies24HrThreshTable,
       "adGenMEF10100EthAnomalies24HrThreshEntry": adGenMEF10100EthAnomalies24HrThreshEntry,
       "adGenMEF10100EthAnomalies24HrThreshFramesWithInvalidCEVLANID": adGenMEF10100EthAnomalies24HrThreshFramesWithInvalidCEVLANID,
       "adGenMEFGigEthAnomaliesPerfThresholds": adGenMEFGigEthAnomaliesPerfThresholds,
       "adGenMEFGigEthAnomalies15MinThreshTable": adGenMEFGigEthAnomalies15MinThreshTable,
       "adGenMEFGigEthAnomalies15MinThreshEntry": adGenMEFGigEthAnomalies15MinThreshEntry,
       "adGenMEFGigEthAnomalies15MinThreshFramesWithInvalidCEVLANID": adGenMEFGigEthAnomalies15MinThreshFramesWithInvalidCEVLANID,
       "adGenMEFGigEthAnomalies24HrThreshTable": adGenMEFGigEthAnomalies24HrThreshTable,
       "adGenMEFGigEthAnomalies24HrThreshEntry": adGenMEFGigEthAnomalies24HrThreshEntry,
       "adGenMEFGigEthAnomalies24HrThreshFramesWithInvalidCEVLANID": adGenMEFGigEthAnomalies24HrThreshFramesWithInvalidCEVLANID,
       "adGenMEFPolicerPerfThresholds": adGenMEFPolicerPerfThresholds,
       "adGenMEFPolicer15MinThreshTable": adGenMEFPolicer15MinThreshTable,
       "adGenMEFPolicer15MinThreshEntry": adGenMEFPolicer15MinThreshEntry,
       "adGenMEFPolicer15MinThresholdIngressGreenFrames": adGenMEFPolicer15MinThresholdIngressGreenFrames,
       "adGenMEFPolicer15MinThresholdIngressYellowFrames": adGenMEFPolicer15MinThresholdIngressYellowFrames,
       "adGenMEFPolicer15MinThresholdIngressRedFrames": adGenMEFPolicer15MinThresholdIngressRedFrames,
       "adGenMEFPolicer15MinThresholdCongDiscardsIngressGreenFrames": adGenMEFPolicer15MinThresholdCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer15MinThresholdCongDiscardsIngressYellowFrames": adGenMEFPolicer15MinThresholdCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer15MinThresholdHCIngressGreenFrames": adGenMEFPolicer15MinThresholdHCIngressGreenFrames,
       "adGenMEFPolicer15MinThresholdHCIngressYellowFrames": adGenMEFPolicer15MinThresholdHCIngressYellowFrames,
       "adGenMEFPolicer15MinThresholdHCIngressRedFrames": adGenMEFPolicer15MinThresholdHCIngressRedFrames,
       "adGenMEFPolicer15MinThresholdHCCongDiscardsIngressGreenFrames": adGenMEFPolicer15MinThresholdHCCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer15MinThresholdHCCongDiscardsIngressYellowFrames": adGenMEFPolicer15MinThresholdHCCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer24HrThreshTable": adGenMEFPolicer24HrThreshTable,
       "adGenMEFPolicer24HrThreshEntry": adGenMEFPolicer24HrThreshEntry,
       "adGenMEFPolicer24HrThresholdIngressGreenFrames": adGenMEFPolicer24HrThresholdIngressGreenFrames,
       "adGenMEFPolicer24HrThresholdIngressYellowFrames": adGenMEFPolicer24HrThresholdIngressYellowFrames,
       "adGenMEFPolicer24HrThresholdIngressRedFrames": adGenMEFPolicer24HrThresholdIngressRedFrames,
       "adGenMEFPolicer24HrThresholdCongDiscardsIngressGreenFrames": adGenMEFPolicer24HrThresholdCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer24HrThresholdCongDiscardsIngressYellowFrames": adGenMEFPolicer24HrThresholdCongDiscardsIngressYellowFrames,
       "adGenMEFPolicer24HrThresholdHCIngressGreenFrames": adGenMEFPolicer24HrThresholdHCIngressGreenFrames,
       "adGenMEFPolicer24HrThresholdHCIngressYellowFrames": adGenMEFPolicer24HrThresholdHCIngressYellowFrames,
       "adGenMEFPolicer24HrThresholdHCIngressRedFrames": adGenMEFPolicer24HrThresholdHCIngressRedFrames,
       "adGenMEFPolicer24HrThresholdHCCongDiscardsIngressGreenFrames": adGenMEFPolicer24HrThresholdHCCongDiscardsIngressGreenFrames,
       "adGenMEFPolicer24HrThresholdHCCongDiscardsIngressYellowFrames": adGenMEFPolicer24HrThresholdHCCongDiscardsIngressYellowFrames,
       "adGenMEFMIB": adGenMEFMIB}
)
