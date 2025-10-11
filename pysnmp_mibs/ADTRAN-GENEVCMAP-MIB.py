# SNMP MIB module (ADTRAN-GENEVCMAP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENEVCMAP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:33:45 2025
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

(adGenEVCMap,
 adGenEVCMapID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenEVCMap",
    "adGenEVCMapID")

(GenSystemInterfaceType,) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-TC-MIB",
    "GenSystemInterfaceType")

(InterfaceIndexOrZero,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

adGenEVCMapMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 28, 1)
)
if mibBuilder.loadTexts:
    adGenEVCMapMIB.setRevisions(
        ("2019-08-07 00:00",
         "2014-08-04 00:00",
         "2013-07-15 00:00",
         "2010-07-21 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenEVCMapProvisioning_ObjectIdentity = ObjectIdentity
adGenEVCMapProvisioning = _AdGenEVCMapProvisioning_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1)
)
_AdGenEVCMapTable_Object = MibTable
adGenEVCMapTable = _AdGenEVCMapTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1)
)
if mibBuilder.loadTexts:
    adGenEVCMapTable.setStatus("current")
_AdGenEVCMapEntry_Object = MibTableRow
adGenEVCMapEntry = _AdGenEVCMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1)
)
adGenEVCMapEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (1, "ADTRAN-GENEVCMAP-MIB", "adGenEVCMapName"),
)
if mibBuilder.loadTexts:
    adGenEVCMapEntry.setStatus("current")


class _AdGenEVCMapName_Type(DisplayString):
    """Custom type adGenEVCMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenEVCMapName_Type.__name__ = "DisplayString"
_AdGenEVCMapName_Object = MibTableColumn
adGenEVCMapName = _AdGenEVCMapName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 1),
    _AdGenEVCMapName_Type()
)
adGenEVCMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEVCMapName.setStatus("current")
_AdGenEVCMapRowStatus_Type = RowStatus
_AdGenEVCMapRowStatus_Object = MibTableColumn
adGenEVCMapRowStatus = _AdGenEVCMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 2),
    _AdGenEVCMapRowStatus_Type()
)
adGenEVCMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapRowStatus.setStatus("current")


class _AdGenEVCMapOperStatus_Type(Integer32):
    """Custom type adGenEVCMapOperStatus based on Integer32"""
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


_AdGenEVCMapOperStatus_Type.__name__ = "Integer32"
_AdGenEVCMapOperStatus_Object = MibTableColumn
adGenEVCMapOperStatus = _AdGenEVCMapOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 3),
    _AdGenEVCMapOperStatus_Type()
)
adGenEVCMapOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapOperStatus.setStatus("current")
_AdGenEVCMapOperStatusDetail_Type = DisplayString
_AdGenEVCMapOperStatusDetail_Object = MibTableColumn
adGenEVCMapOperStatusDetail = _AdGenEVCMapOperStatusDetail_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 4),
    _AdGenEVCMapOperStatusDetail_Type()
)
adGenEVCMapOperStatusDetail.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapOperStatusDetail.setStatus("current")
_AdGenEVCMapLastProvError_Type = DisplayString
_AdGenEVCMapLastProvError_Object = MibTableColumn
adGenEVCMapLastProvError = _AdGenEVCMapLastProvError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 5),
    _AdGenEVCMapLastProvError_Type()
)
adGenEVCMapLastProvError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapLastProvError.setStatus("current")


class _AdGenEVCMapConnectEVC_Type(DisplayString):
    """Custom type adGenEVCMapConnectEVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenEVCMapConnectEVC_Type.__name__ = "DisplayString"
_AdGenEVCMapConnectEVC_Object = MibTableColumn
adGenEVCMapConnectEVC = _AdGenEVCMapConnectEVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 6),
    _AdGenEVCMapConnectEVC_Type()
)
adGenEVCMapConnectEVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapConnectEVC.setStatus("current")


class _AdGenEVCMapConnectMEVC_Type(DisplayString):
    """Custom type adGenEVCMapConnectMEVC based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenEVCMapConnectMEVC_Type.__name__ = "DisplayString"
_AdGenEVCMapConnectMEVC_Object = MibTableColumn
adGenEVCMapConnectMEVC = _AdGenEVCMapConnectMEVC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 7),
    _AdGenEVCMapConnectMEVC_Type()
)
adGenEVCMapConnectMEVC.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapConnectMEVC.setStatus("current")


class _AdGenEVCMapConnectUNIMethod_Type(Integer32):
    """Custom type adGenEVCMapConnectUNIMethod based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("byIfIndex", 1),
          ("byTypeAndString", 2))
    )


_AdGenEVCMapConnectUNIMethod_Type.__name__ = "Integer32"
_AdGenEVCMapConnectUNIMethod_Object = MibTableColumn
adGenEVCMapConnectUNIMethod = _AdGenEVCMapConnectUNIMethod_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 8),
    _AdGenEVCMapConnectUNIMethod_Type()
)
adGenEVCMapConnectUNIMethod.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapConnectUNIMethod.setStatus("current")
_AdGenEVCMapConnectUNIByIfIndex_Type = InterfaceIndexOrZero
_AdGenEVCMapConnectUNIByIfIndex_Object = MibTableColumn
adGenEVCMapConnectUNIByIfIndex = _AdGenEVCMapConnectUNIByIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 9),
    _AdGenEVCMapConnectUNIByIfIndex_Type()
)
adGenEVCMapConnectUNIByIfIndex.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapConnectUNIByIfIndex.setStatus("current")
_AdGenEVCMapConnectUNIByTypeAndStringTypeValue_Type = GenSystemInterfaceType
_AdGenEVCMapConnectUNIByTypeAndStringTypeValue_Object = MibTableColumn
adGenEVCMapConnectUNIByTypeAndStringTypeValue = _AdGenEVCMapConnectUNIByTypeAndStringTypeValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 10),
    _AdGenEVCMapConnectUNIByTypeAndStringTypeValue_Type()
)
adGenEVCMapConnectUNIByTypeAndStringTypeValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapConnectUNIByTypeAndStringTypeValue.setStatus("current")
_AdGenEVCMapConnectUNIByTypeAndStringStringValue_Type = OctetString
_AdGenEVCMapConnectUNIByTypeAndStringStringValue_Object = MibTableColumn
adGenEVCMapConnectUNIByTypeAndStringStringValue = _AdGenEVCMapConnectUNIByTypeAndStringStringValue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 11),
    _AdGenEVCMapConnectUNIByTypeAndStringStringValue_Type()
)
adGenEVCMapConnectUNIByTypeAndStringStringValue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapConnectUNIByTypeAndStringStringValue.setStatus("current")


class _AdGenEVCMapMENPriority_Type(Integer32):
    """Custom type adGenEVCMapMENPriority based on Integer32"""
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


_AdGenEVCMapMENPriority_Type.__name__ = "Integer32"
_AdGenEVCMapMENPriority_Object = MibTableColumn
adGenEVCMapMENPriority = _AdGenEVCMapMENPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 20),
    _AdGenEVCMapMENPriority_Type()
)
adGenEVCMapMENPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMENPriority.setStatus("current")


class _AdGenEVCMapMENQueue_Type(Integer32):
    """Custom type adGenEVCMapMENQueue based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8)
        )
    )
    namedValues = NamedValues(
        *(("inheritFromMenPriAndQosMap", 0),
          ("queue0", 1),
          ("queue1", 2),
          ("queue2", 3),
          ("queue3", 4),
          ("queue4", 5),
          ("queue5", 6),
          ("queue6", 7),
          ("queue7", 8))
    )


_AdGenEVCMapMENQueue_Type.__name__ = "Integer32"
_AdGenEVCMapMENQueue_Object = MibTableColumn
adGenEVCMapMENQueue = _AdGenEVCMapMENQueue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 21),
    _AdGenEVCMapMENQueue_Type()
)
adGenEVCMapMENQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMENQueue.setStatus("current")


class _AdGenEVCMapMENCtag_Type(Integer32):
    """Custom type adGenEVCMapMENCtag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4095),
    )


_AdGenEVCMapMENCtag_Type.__name__ = "Integer32"
_AdGenEVCMapMENCtag_Object = MibTableColumn
adGenEVCMapMENCtag = _AdGenEVCMapMENCtag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 22),
    _AdGenEVCMapMENCtag_Type()
)
adGenEVCMapMENCtag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMENCtag.setStatus("current")


class _AdGenEVCMapMENCtagPriority_Type(Integer32):
    """Custom type adGenEVCMapMENCtagPriority based on Integer32"""
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


_AdGenEVCMapMENCtagPriority_Type.__name__ = "Integer32"
_AdGenEVCMapMENCtagPriority_Object = MibTableColumn
adGenEVCMapMENCtagPriority = _AdGenEVCMapMENCtagPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 23),
    _AdGenEVCMapMENCtagPriority_Type()
)
adGenEVCMapMENCtagPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMENCtagPriority.setStatus("current")


class _AdGenEVCMapMatchCEVLANID_Type(Integer32):
    """Custom type adGenEVCMapMatchCEVLANID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenEVCMapMatchCEVLANID_Type.__name__ = "Integer32"
_AdGenEVCMapMatchCEVLANID_Object = MibTableColumn
adGenEVCMapMatchCEVLANID = _AdGenEVCMapMatchCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 24),
    _AdGenEVCMapMatchCEVLANID_Type()
)
adGenEVCMapMatchCEVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMatchCEVLANID.setStatus("current")
_AdGenEVCMapMatchCEVLANPriority_Type = DisplayString
_AdGenEVCMapMatchCEVLANPriority_Object = MibTableColumn
adGenEVCMapMatchCEVLANPriority = _AdGenEVCMapMatchCEVLANPriority_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 25),
    _AdGenEVCMapMatchCEVLANPriority_Type()
)
adGenEVCMapMatchCEVLANPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMatchCEVLANPriority.setStatus("current")
_AdGenMEFMapDSCPRange_Type = DisplayString
_AdGenMEFMapDSCPRange_Object = MibTableColumn
adGenMEFMapDSCPRange = _AdGenMEFMapDSCPRange_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 26),
    _AdGenMEFMapDSCPRange_Type()
)
adGenMEFMapDSCPRange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenMEFMapDSCPRange.setStatus("current")


class _AdGenEVCMapMatchUntagged_Type(Integer32):
    """Custom type adGenEVCMapMatchUntagged based on Integer32"""
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


_AdGenEVCMapMatchUntagged_Type.__name__ = "Integer32"
_AdGenEVCMapMatchUntagged_Object = MibTableColumn
adGenEVCMapMatchUntagged = _AdGenEVCMapMatchUntagged_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 27),
    _AdGenEVCMapMatchUntagged_Type()
)
adGenEVCMapMatchUntagged.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMatchUntagged.setStatus("current")


class _AdGenEVCMapMatchUnicast_Type(Integer32):
    """Custom type adGenEVCMapMatchUnicast based on Integer32"""
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


_AdGenEVCMapMatchUnicast_Type.__name__ = "Integer32"
_AdGenEVCMapMatchUnicast_Object = MibTableColumn
adGenEVCMapMatchUnicast = _AdGenEVCMapMatchUnicast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 28),
    _AdGenEVCMapMatchUnicast_Type()
)
adGenEVCMapMatchUnicast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMatchUnicast.setStatus("current")


class _AdGenEVCMapMatchBroadcast_Type(Integer32):
    """Custom type adGenEVCMapMatchBroadcast based on Integer32"""
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


_AdGenEVCMapMatchBroadcast_Type.__name__ = "Integer32"
_AdGenEVCMapMatchBroadcast_Object = MibTableColumn
adGenEVCMapMatchBroadcast = _AdGenEVCMapMatchBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 29),
    _AdGenEVCMapMatchBroadcast_Type()
)
adGenEVCMapMatchBroadcast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMatchBroadcast.setStatus("current")


class _AdGenEVCMapMatchMulticast_Type(Integer32):
    """Custom type adGenEVCMapMatchMulticast based on Integer32"""
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


_AdGenEVCMapMatchMulticast_Type.__name__ = "Integer32"
_AdGenEVCMapMatchMulticast_Object = MibTableColumn
adGenEVCMapMatchMulticast = _AdGenEVCMapMatchMulticast_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 30),
    _AdGenEVCMapMatchMulticast_Type()
)
adGenEVCMapMatchMulticast.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMatchMulticast.setStatus("current")


class _AdGenEVCMapMatchL2CP_Type(Integer32):
    """Custom type adGenEVCMapMatchL2CP based on Integer32"""
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


_AdGenEVCMapMatchL2CP_Type.__name__ = "Integer32"
_AdGenEVCMapMatchL2CP_Object = MibTableColumn
adGenEVCMapMatchL2CP = _AdGenEVCMapMatchL2CP_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 31),
    _AdGenEVCMapMatchL2CP_Type()
)
adGenEVCMapMatchL2CP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMatchL2CP.setStatus("current")


class _AdGenEVCMapConnectDiscard_Type(Integer32):
    """Custom type adGenEVCMapConnectDiscard based on Integer32"""
    defaultValue = 2

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


_AdGenEVCMapConnectDiscard_Type.__name__ = "Integer32"
_AdGenEVCMapConnectDiscard_Object = MibTableColumn
adGenEVCMapConnectDiscard = _AdGenEVCMapConnectDiscard_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 32),
    _AdGenEVCMapConnectDiscard_Type()
)
adGenEVCMapConnectDiscard.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapConnectDiscard.setStatus("current")
_AdGenEVCMapMatchDestMacAddress_Type = MacAddress
_AdGenEVCMapMatchDestMacAddress_Object = MibTableColumn
adGenEVCMapMatchDestMacAddress = _AdGenEVCMapMatchDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 33),
    _AdGenEVCMapMatchDestMacAddress_Type()
)
adGenEVCMapMatchDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMatchDestMacAddress.setStatus("current")
_AdGenEVCMapActivePolicerName_Type = DisplayString
_AdGenEVCMapActivePolicerName_Object = MibTableColumn
adGenEVCMapActivePolicerName = _AdGenEVCMapActivePolicerName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 34),
    _AdGenEVCMapActivePolicerName_Type()
)
adGenEVCMapActivePolicerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapActivePolicerName.setStatus("current")


class _AdGenEVCMapMatchInnerCEVLANID_Type(Integer32):
    """Custom type adGenEVCMapMatchInnerCEVLANID based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AdGenEVCMapMatchInnerCEVLANID_Type.__name__ = "Integer32"
_AdGenEVCMapMatchInnerCEVLANID_Object = MibTableColumn
adGenEVCMapMatchInnerCEVLANID = _AdGenEVCMapMatchInnerCEVLANID_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 1, 1, 35),
    _AdGenEVCMapMatchInnerCEVLANID_Type()
)
adGenEVCMapMatchInnerCEVLANID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenEVCMapMatchInnerCEVLANID.setStatus("current")
_AdGenEVCMapErrorTable_Object = MibTable
adGenEVCMapErrorTable = _AdGenEVCMapErrorTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 2)
)
if mibBuilder.loadTexts:
    adGenEVCMapErrorTable.setStatus("current")
_AdGenEVCMapErrorEntry_Object = MibTableRow
adGenEVCMapErrorEntry = _AdGenEVCMapErrorEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 2, 1)
)
adGenEVCMapErrorEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenEVCMapErrorEntry.setStatus("current")
_AdGenEVCMapError_Type = DisplayString
_AdGenEVCMapError_Object = MibTableColumn
adGenEVCMapError = _AdGenEVCMapError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 2, 1, 1),
    _AdGenEVCMapError_Type()
)
adGenEVCMapError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapError.setStatus("current")
_AdGenEVCMapUNINumberOfMapsTable_Object = MibTable
adGenEVCMapUNINumberOfMapsTable = _AdGenEVCMapUNINumberOfMapsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 3)
)
if mibBuilder.loadTexts:
    adGenEVCMapUNINumberOfMapsTable.setStatus("current")
_AdGenEVCMapUNINumberOfMapsEntry_Object = MibTableRow
adGenEVCMapUNINumberOfMapsEntry = _AdGenEVCMapUNINumberOfMapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 3, 1)
)
adGenEVCMapUNINumberOfMapsEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenEVCMapUNINumberOfMapsEntry.setStatus("current")
_AdGenEVCMapUNINumberOfMaps_Type = Integer32
_AdGenEVCMapUNINumberOfMaps_Object = MibTableColumn
adGenEVCMapUNINumberOfMaps = _AdGenEVCMapUNINumberOfMaps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 3, 1, 1),
    _AdGenEVCMapUNINumberOfMaps_Type()
)
adGenEVCMapUNINumberOfMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapUNINumberOfMaps.setStatus("current")
_AdGenEVCMapUNILookupTable_Object = MibTable
adGenEVCMapUNILookupTable = _AdGenEVCMapUNILookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 4)
)
if mibBuilder.loadTexts:
    adGenEVCMapUNILookupTable.setStatus("current")
_AdGenEVCMapUNILookupEntry_Object = MibTableRow
adGenEVCMapUNILookupEntry = _AdGenEVCMapUNILookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 4, 1)
)
adGenEVCMapUNILookupEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
    (0, "ADTRAN-GENEVCMAP-MIB", "adGenEVCMapUNILookupIndex"),
)
if mibBuilder.loadTexts:
    adGenEVCMapUNILookupEntry.setStatus("current")
_AdGenEVCMapUNILookupIndex_Type = Integer32
_AdGenEVCMapUNILookupIndex_Object = MibTableColumn
adGenEVCMapUNILookupIndex = _AdGenEVCMapUNILookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 4, 1, 1),
    _AdGenEVCMapUNILookupIndex_Type()
)
adGenEVCMapUNILookupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEVCMapUNILookupIndex.setStatus("current")
_AdGenEVCMapUNILookupName_Type = DisplayString
_AdGenEVCMapUNILookupName_Object = MibTableColumn
adGenEVCMapUNILookupName = _AdGenEVCMapUNILookupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 4, 1, 2),
    _AdGenEVCMapUNILookupName_Type()
)
adGenEVCMapUNILookupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapUNILookupName.setStatus("current")
_AdGenEVCMapMEVCNumberOfMapsTable_Object = MibTable
adGenEVCMapMEVCNumberOfMapsTable = _AdGenEVCMapMEVCNumberOfMapsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 5)
)
if mibBuilder.loadTexts:
    adGenEVCMapMEVCNumberOfMapsTable.setStatus("current")
_AdGenEVCMapMEVCNumberOfMapsEntry_Object = MibTableRow
adGenEVCMapMEVCNumberOfMapsEntry = _AdGenEVCMapMEVCNumberOfMapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 5, 1)
)
adGenEVCMapMEVCNumberOfMapsEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENEVCMAP-MIB", "adGenEVCMapMEVCName"),
)
if mibBuilder.loadTexts:
    adGenEVCMapMEVCNumberOfMapsEntry.setStatus("current")


class _AdGenEVCMapMEVCName_Type(OctetString):
    """Custom type adGenEVCMapMEVCName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenEVCMapMEVCName_Type.__name__ = "OctetString"
_AdGenEVCMapMEVCName_Object = MibTableColumn
adGenEVCMapMEVCName = _AdGenEVCMapMEVCName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 5, 1, 1),
    _AdGenEVCMapMEVCName_Type()
)
adGenEVCMapMEVCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEVCMapMEVCName.setStatus("current")
_AdGenEVCMapMEVCNumberOfMaps_Type = Integer32
_AdGenEVCMapMEVCNumberOfMaps_Object = MibTableColumn
adGenEVCMapMEVCNumberOfMaps = _AdGenEVCMapMEVCNumberOfMaps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 5, 1, 2),
    _AdGenEVCMapMEVCNumberOfMaps_Type()
)
adGenEVCMapMEVCNumberOfMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapMEVCNumberOfMaps.setStatus("current")
_AdGenEVCMapMEVCLookupTable_Object = MibTable
adGenEVCMapMEVCLookupTable = _AdGenEVCMapMEVCLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 6)
)
if mibBuilder.loadTexts:
    adGenEVCMapMEVCLookupTable.setStatus("current")
_AdGenEVCMapMEVCLookupEntry_Object = MibTableRow
adGenEVCMapMEVCLookupEntry = _AdGenEVCMapMEVCLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 6, 1)
)
adGenEVCMapMEVCLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENEVCMAP-MIB", "adGenEVCMapMEVCFixedLengthName"),
    (0, "ADTRAN-GENEVCMAP-MIB", "adGenEVCMapMEVCLookupIndex"),
)
if mibBuilder.loadTexts:
    adGenEVCMapMEVCLookupEntry.setStatus("current")


class _AdGenEVCMapMEVCFixedLengthName_Type(OctetString):
    """Custom type adGenEVCMapMEVCFixedLengthName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_AdGenEVCMapMEVCFixedLengthName_Type.__name__ = "OctetString"
_AdGenEVCMapMEVCFixedLengthName_Object = MibTableColumn
adGenEVCMapMEVCFixedLengthName = _AdGenEVCMapMEVCFixedLengthName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 6, 1, 1),
    _AdGenEVCMapMEVCFixedLengthName_Type()
)
adGenEVCMapMEVCFixedLengthName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEVCMapMEVCFixedLengthName.setStatus("current")
_AdGenEVCMapMEVCLookupIndex_Type = Integer32
_AdGenEVCMapMEVCLookupIndex_Object = MibTableColumn
adGenEVCMapMEVCLookupIndex = _AdGenEVCMapMEVCLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 6, 1, 2),
    _AdGenEVCMapMEVCLookupIndex_Type()
)
adGenEVCMapMEVCLookupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEVCMapMEVCLookupIndex.setStatus("current")
_AdGenEVCMapMEVCLookupName_Type = DisplayString
_AdGenEVCMapMEVCLookupName_Object = MibTableColumn
adGenEVCMapMEVCLookupName = _AdGenEVCMapMEVCLookupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 6, 1, 3),
    _AdGenEVCMapMEVCLookupName_Type()
)
adGenEVCMapMEVCLookupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapMEVCLookupName.setStatus("current")
_AdGenEVCMapEVCNumberOfMapsTable_Object = MibTable
adGenEVCMapEVCNumberOfMapsTable = _AdGenEVCMapEVCNumberOfMapsTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 7)
)
if mibBuilder.loadTexts:
    adGenEVCMapEVCNumberOfMapsTable.setStatus("current")
_AdGenEVCMapEVCNumberOfMapsEntry_Object = MibTableRow
adGenEVCMapEVCNumberOfMapsEntry = _AdGenEVCMapEVCNumberOfMapsEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 7, 1)
)
adGenEVCMapEVCNumberOfMapsEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENEVCMAP-MIB", "adGenEVCMapEVCName"),
)
if mibBuilder.loadTexts:
    adGenEVCMapEVCNumberOfMapsEntry.setStatus("current")


class _AdGenEVCMapEVCName_Type(OctetString):
    """Custom type adGenEVCMapEVCName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 50),
    )


_AdGenEVCMapEVCName_Type.__name__ = "OctetString"
_AdGenEVCMapEVCName_Object = MibTableColumn
adGenEVCMapEVCName = _AdGenEVCMapEVCName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 7, 1, 1),
    _AdGenEVCMapEVCName_Type()
)
adGenEVCMapEVCName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEVCMapEVCName.setStatus("current")
_AdGenEVCMapEVCNumberOfMaps_Type = Integer32
_AdGenEVCMapEVCNumberOfMaps_Object = MibTableColumn
adGenEVCMapEVCNumberOfMaps = _AdGenEVCMapEVCNumberOfMaps_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 7, 1, 2),
    _AdGenEVCMapEVCNumberOfMaps_Type()
)
adGenEVCMapEVCNumberOfMaps.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapEVCNumberOfMaps.setStatus("current")
_AdGenEVCMapEVCLookupTable_Object = MibTable
adGenEVCMapEVCLookupTable = _AdGenEVCMapEVCLookupTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 8)
)
if mibBuilder.loadTexts:
    adGenEVCMapEVCLookupTable.setStatus("current")
_AdGenEVCMapEVCLookupEntry_Object = MibTableRow
adGenEVCMapEVCLookupEntry = _AdGenEVCMapEVCLookupEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 8, 1)
)
adGenEVCMapEVCLookupEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-GENEVCMAP-MIB", "adGenEVCMapEVCFixedLengthName"),
    (0, "ADTRAN-GENEVCMAP-MIB", "adGenEVCMapEVCLookupIndex"),
)
if mibBuilder.loadTexts:
    adGenEVCMapEVCLookupEntry.setStatus("current")


class _AdGenEVCMapEVCFixedLengthName_Type(OctetString):
    """Custom type adGenEVCMapEVCFixedLengthName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(50, 50),
    )
    fixed_length = 50


_AdGenEVCMapEVCFixedLengthName_Type.__name__ = "OctetString"
_AdGenEVCMapEVCFixedLengthName_Object = MibTableColumn
adGenEVCMapEVCFixedLengthName = _AdGenEVCMapEVCFixedLengthName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 8, 1, 1),
    _AdGenEVCMapEVCFixedLengthName_Type()
)
adGenEVCMapEVCFixedLengthName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEVCMapEVCFixedLengthName.setStatus("current")
_AdGenEVCMapEVCLookupIndex_Type = Integer32
_AdGenEVCMapEVCLookupIndex_Object = MibTableColumn
adGenEVCMapEVCLookupIndex = _AdGenEVCMapEVCLookupIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 8, 1, 2),
    _AdGenEVCMapEVCLookupIndex_Type()
)
adGenEVCMapEVCLookupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenEVCMapEVCLookupIndex.setStatus("current")
_AdGenEVCMapEVCLookupName_Type = DisplayString
_AdGenEVCMapEVCLookupName_Object = MibTableColumn
adGenEVCMapEVCLookupName = _AdGenEVCMapEVCLookupName_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 28, 1, 8, 1, 3),
    _AdGenEVCMapEVCLookupName_Type()
)
adGenEVCMapEVCLookupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenEVCMapEVCLookupName.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENEVCMAP-MIB",
    **{"adGenEVCMapProvisioning": adGenEVCMapProvisioning,
       "adGenEVCMapTable": adGenEVCMapTable,
       "adGenEVCMapEntry": adGenEVCMapEntry,
       "adGenEVCMapName": adGenEVCMapName,
       "adGenEVCMapRowStatus": adGenEVCMapRowStatus,
       "adGenEVCMapOperStatus": adGenEVCMapOperStatus,
       "adGenEVCMapOperStatusDetail": adGenEVCMapOperStatusDetail,
       "adGenEVCMapLastProvError": adGenEVCMapLastProvError,
       "adGenEVCMapConnectEVC": adGenEVCMapConnectEVC,
       "adGenEVCMapConnectMEVC": adGenEVCMapConnectMEVC,
       "adGenEVCMapConnectUNIMethod": adGenEVCMapConnectUNIMethod,
       "adGenEVCMapConnectUNIByIfIndex": adGenEVCMapConnectUNIByIfIndex,
       "adGenEVCMapConnectUNIByTypeAndStringTypeValue": adGenEVCMapConnectUNIByTypeAndStringTypeValue,
       "adGenEVCMapConnectUNIByTypeAndStringStringValue": adGenEVCMapConnectUNIByTypeAndStringStringValue,
       "adGenEVCMapMENPriority": adGenEVCMapMENPriority,
       "adGenEVCMapMENQueue": adGenEVCMapMENQueue,
       "adGenEVCMapMENCtag": adGenEVCMapMENCtag,
       "adGenEVCMapMENCtagPriority": adGenEVCMapMENCtagPriority,
       "adGenEVCMapMatchCEVLANID": adGenEVCMapMatchCEVLANID,
       "adGenEVCMapMatchCEVLANPriority": adGenEVCMapMatchCEVLANPriority,
       "adGenMEFMapDSCPRange": adGenMEFMapDSCPRange,
       "adGenEVCMapMatchUntagged": adGenEVCMapMatchUntagged,
       "adGenEVCMapMatchUnicast": adGenEVCMapMatchUnicast,
       "adGenEVCMapMatchBroadcast": adGenEVCMapMatchBroadcast,
       "adGenEVCMapMatchMulticast": adGenEVCMapMatchMulticast,
       "adGenEVCMapMatchL2CP": adGenEVCMapMatchL2CP,
       "adGenEVCMapConnectDiscard": adGenEVCMapConnectDiscard,
       "adGenEVCMapMatchDestMacAddress": adGenEVCMapMatchDestMacAddress,
       "adGenEVCMapActivePolicerName": adGenEVCMapActivePolicerName,
       "adGenEVCMapMatchInnerCEVLANID": adGenEVCMapMatchInnerCEVLANID,
       "adGenEVCMapErrorTable": adGenEVCMapErrorTable,
       "adGenEVCMapErrorEntry": adGenEVCMapErrorEntry,
       "adGenEVCMapError": adGenEVCMapError,
       "adGenEVCMapUNINumberOfMapsTable": adGenEVCMapUNINumberOfMapsTable,
       "adGenEVCMapUNINumberOfMapsEntry": adGenEVCMapUNINumberOfMapsEntry,
       "adGenEVCMapUNINumberOfMaps": adGenEVCMapUNINumberOfMaps,
       "adGenEVCMapUNILookupTable": adGenEVCMapUNILookupTable,
       "adGenEVCMapUNILookupEntry": adGenEVCMapUNILookupEntry,
       "adGenEVCMapUNILookupIndex": adGenEVCMapUNILookupIndex,
       "adGenEVCMapUNILookupName": adGenEVCMapUNILookupName,
       "adGenEVCMapMEVCNumberOfMapsTable": adGenEVCMapMEVCNumberOfMapsTable,
       "adGenEVCMapMEVCNumberOfMapsEntry": adGenEVCMapMEVCNumberOfMapsEntry,
       "adGenEVCMapMEVCName": adGenEVCMapMEVCName,
       "adGenEVCMapMEVCNumberOfMaps": adGenEVCMapMEVCNumberOfMaps,
       "adGenEVCMapMEVCLookupTable": adGenEVCMapMEVCLookupTable,
       "adGenEVCMapMEVCLookupEntry": adGenEVCMapMEVCLookupEntry,
       "adGenEVCMapMEVCFixedLengthName": adGenEVCMapMEVCFixedLengthName,
       "adGenEVCMapMEVCLookupIndex": adGenEVCMapMEVCLookupIndex,
       "adGenEVCMapMEVCLookupName": adGenEVCMapMEVCLookupName,
       "adGenEVCMapEVCNumberOfMapsTable": adGenEVCMapEVCNumberOfMapsTable,
       "adGenEVCMapEVCNumberOfMapsEntry": adGenEVCMapEVCNumberOfMapsEntry,
       "adGenEVCMapEVCName": adGenEVCMapEVCName,
       "adGenEVCMapEVCNumberOfMaps": adGenEVCMapEVCNumberOfMaps,
       "adGenEVCMapEVCLookupTable": adGenEVCMapEVCLookupTable,
       "adGenEVCMapEVCLookupEntry": adGenEVCMapEVCLookupEntry,
       "adGenEVCMapEVCFixedLengthName": adGenEVCMapEVCFixedLengthName,
       "adGenEVCMapEVCLookupIndex": adGenEVCMapEVCLookupIndex,
       "adGenEVCMapEVCLookupName": adGenEVCMapEVCLookupName,
       "adGenEVCMapMIB": adGenEVCMapMIB}
)
