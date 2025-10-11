# SNMP MIB module (ADTRAN-DYNAMIC-COUNTERS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-DYNAMIC-COUNTERS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:32:49 2025
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

(adIdentity,) = mibBuilder.importSymbols(
    "ADTRAN-MIB",
    "adIdentity")

(adGenDynamicCounter,
 adGenDynamicCounterID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenDynamicCounter",
    "adGenDynamicCounterID")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

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

adGenDynamicCounterMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 53, 1)
)
if mibBuilder.loadTexts:
    adGenDynamicCounterMIB.setRevisions(
        ("2014-07-31 00:00",
         "2014-06-05 00:00",
         "2013-02-11 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenDynamicCounterTables_ObjectIdentity = ObjectIdentity
adGenDynamicCounterTables = _AdGenDynamicCounterTables_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1)
)
_AdGenDCSlotTable_Object = MibTable
adGenDCSlotTable = _AdGenDCSlotTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 1)
)
if mibBuilder.loadTexts:
    adGenDCSlotTable.setStatus("current")
_AdGenDCSlotEntry_Object = MibTableRow
adGenDCSlotEntry = _AdGenDCSlotEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 1, 1)
)
adGenDCSlotEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
)
if mibBuilder.loadTexts:
    adGenDCSlotEntry.setStatus("current")


class _AdGenDCSlotSupport_Type(Bits):
    """Custom type adGenDCSlotSupport based on Bits"""
    namedValues = NamedValues(
        *(("color", 0),
          ("pBit", 1),
          ("sTag", 2),
          ("destMacByType", 3),
          ("destMac", 4),
          ("destIpByType", 5),
          ("destIp", 6),
          ("srcMacByType", 7),
          ("srcMac", 8),
          ("srcIpByType", 9),
          ("srcIp", 10),
          ("ipAndMac", 11),
          ("destAndSrc", 12),
          ("tx", 13),
          ("rx", 14),
          ("queue", 15),
          ("include", 16),
          ("exclude", 17))
    )

_AdGenDCSlotSupport_Type.__name__ = "Bits"
_AdGenDCSlotSupport_Object = MibTableColumn
adGenDCSlotSupport = _AdGenDCSlotSupport_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 1, 1, 1),
    _AdGenDCSlotSupport_Type()
)
adGenDCSlotSupport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCSlotSupport.setStatus("current")
_AdGenDCSlotMaxDCProfileIndex_Type = Integer32
_AdGenDCSlotMaxDCProfileIndex_Object = MibTableColumn
adGenDCSlotMaxDCProfileIndex = _AdGenDCSlotMaxDCProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 1, 1, 2),
    _AdGenDCSlotMaxDCProfileIndex_Type()
)
adGenDCSlotMaxDCProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCSlotMaxDCProfileIndex.setStatus("current")
_AdGenDCSlotNextDCProfileIndex_Type = Integer32
_AdGenDCSlotNextDCProfileIndex_Object = MibTableColumn
adGenDCSlotNextDCProfileIndex = _AdGenDCSlotNextDCProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 1, 1, 3),
    _AdGenDCSlotNextDCProfileIndex_Type()
)
adGenDCSlotNextDCProfileIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCSlotNextDCProfileIndex.setStatus("current")
_AdGenDCSlotMaxDCIndex_Type = Integer32
_AdGenDCSlotMaxDCIndex_Object = MibTableColumn
adGenDCSlotMaxDCIndex = _AdGenDCSlotMaxDCIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 1, 1, 4),
    _AdGenDCSlotMaxDCIndex_Type()
)
adGenDCSlotMaxDCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCSlotMaxDCIndex.setStatus("current")
_AdGenDCSlotNextDCIndex_Type = Integer32
_AdGenDCSlotNextDCIndex_Object = MibTableColumn
adGenDCSlotNextDCIndex = _AdGenDCSlotNextDCIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 1, 1, 5),
    _AdGenDCSlotNextDCIndex_Type()
)
adGenDCSlotNextDCIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCSlotNextDCIndex.setStatus("current")


class _AdGenDCSlotClearAllDC_Type(Integer32):
    """Custom type adGenDCSlotClearAllDC based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clearAll", 1),
          ("idle", 2))
    )


_AdGenDCSlotClearAllDC_Type.__name__ = "Integer32"
_AdGenDCSlotClearAllDC_Object = MibTableColumn
adGenDCSlotClearAllDC = _AdGenDCSlotClearAllDC_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 1, 1, 6),
    _AdGenDCSlotClearAllDC_Type()
)
adGenDCSlotClearAllDC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDCSlotClearAllDC.setStatus("current")
_AdGenDCSlotLastError_Type = DisplayString
_AdGenDCSlotLastError_Object = MibTableColumn
adGenDCSlotLastError = _AdGenDCSlotLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 1, 1, 7),
    _AdGenDCSlotLastError_Type()
)
adGenDCSlotLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCSlotLastError.setStatus("current")
_AdGenDCProfileTable_Object = MibTable
adGenDCProfileTable = _AdGenDCProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2)
)
if mibBuilder.loadTexts:
    adGenDCProfileTable.setStatus("current")
_AdGenDCProfileEntry_Object = MibTableRow
adGenDCProfileEntry = _AdGenDCProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1)
)
adGenDCProfileEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-DYNAMIC-COUNTERS-MIB", "adGenDCProfileIndex"),
)
if mibBuilder.loadTexts:
    adGenDCProfileEntry.setStatus("current")
_AdGenDCProfileIndex_Type = Integer32
_AdGenDCProfileIndex_Object = MibTableColumn
adGenDCProfileIndex = _AdGenDCProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 1),
    _AdGenDCProfileIndex_Type()
)
adGenDCProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenDCProfileIndex.setStatus("current")
_AdGenDCProfileRowStatus_Type = RowStatus
_AdGenDCProfileRowStatus_Object = MibTableColumn
adGenDCProfileRowStatus = _AdGenDCProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 2),
    _AdGenDCProfileRowStatus_Type()
)
adGenDCProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileRowStatus.setStatus("current")


class _AdGenDCProfileColorType_Type(Integer32):
    """Custom type adGenDCProfileColorType based on Integer32"""
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
        *(("noMatching", 1),
          ("green", 2),
          ("yellow", 3),
          ("red", 4))
    )


_AdGenDCProfileColorType_Type.__name__ = "Integer32"
_AdGenDCProfileColorType_Object = MibTableColumn
adGenDCProfileColorType = _AdGenDCProfileColorType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 3),
    _AdGenDCProfileColorType_Type()
)
adGenDCProfileColorType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileColorType.setStatus("current")


class _AdGenDCProfilePBitType_Type(Integer32):
    """Custom type adGenDCProfilePBitType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noMatching", 1),
          ("pBit", 2))
    )


_AdGenDCProfilePBitType_Type.__name__ = "Integer32"
_AdGenDCProfilePBitType_Object = MibTableColumn
adGenDCProfilePBitType = _AdGenDCProfilePBitType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 4),
    _AdGenDCProfilePBitType_Type()
)
adGenDCProfilePBitType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfilePBitType.setStatus("current")


class _AdGenDCProfilePBit_Type(Integer32):
    """Custom type adGenDCProfilePBit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenDCProfilePBit_Type.__name__ = "Integer32"
_AdGenDCProfilePBit_Object = MibTableColumn
adGenDCProfilePBit = _AdGenDCProfilePBit_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 5),
    _AdGenDCProfilePBit_Type()
)
adGenDCProfilePBit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfilePBit.setStatus("current")


class _AdGenDCProfileSTagType_Type(Integer32):
    """Custom type adGenDCProfileSTagType based on Integer32"""
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
        *(("noMatching", 1),
          ("sTag", 2),
          ("allSTags", 3),
          ("noSTag", 4))
    )


_AdGenDCProfileSTagType_Type.__name__ = "Integer32"
_AdGenDCProfileSTagType_Object = MibTableColumn
adGenDCProfileSTagType = _AdGenDCProfileSTagType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 6),
    _AdGenDCProfileSTagType_Type()
)
adGenDCProfileSTagType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileSTagType.setStatus("current")


class _AdGenDCProfileSTag_Type(Integer32):
    """Custom type adGenDCProfileSTag based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AdGenDCProfileSTag_Type.__name__ = "Integer32"
_AdGenDCProfileSTag_Object = MibTableColumn
adGenDCProfileSTag = _AdGenDCProfileSTag_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 7),
    _AdGenDCProfileSTag_Type()
)
adGenDCProfileSTag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileSTag.setStatus("current")


class _AdGenDCProfileDestMacType_Type(Integer32):
    """Custom type adGenDCProfileDestMacType based on Integer32"""
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
        *(("noMatching", 1),
          ("mac", 2),
          ("unicast", 3),
          ("multicast", 4),
          ("broadcast", 5))
    )


_AdGenDCProfileDestMacType_Type.__name__ = "Integer32"
_AdGenDCProfileDestMacType_Object = MibTableColumn
adGenDCProfileDestMacType = _AdGenDCProfileDestMacType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 8),
    _AdGenDCProfileDestMacType_Type()
)
adGenDCProfileDestMacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileDestMacType.setStatus("current")
_AdGenDCProfileDestMacAddress_Type = PhysAddress
_AdGenDCProfileDestMacAddress_Object = MibTableColumn
adGenDCProfileDestMacAddress = _AdGenDCProfileDestMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 9),
    _AdGenDCProfileDestMacAddress_Type()
)
adGenDCProfileDestMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileDestMacAddress.setStatus("current")


class _AdGenDCProfileDestIpType_Type(Integer32):
    """Custom type adGenDCProfileDestIpType based on Integer32"""
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
        *(("noMatching", 1),
          ("ip", 2),
          ("unicast", 3),
          ("multicast", 4),
          ("any", 5),
          ("none", 6))
    )


_AdGenDCProfileDestIpType_Type.__name__ = "Integer32"
_AdGenDCProfileDestIpType_Object = MibTableColumn
adGenDCProfileDestIpType = _AdGenDCProfileDestIpType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 10),
    _AdGenDCProfileDestIpType_Type()
)
adGenDCProfileDestIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileDestIpType.setStatus("current")
_AdGenDCProfileDestIpAddress_Type = IpAddress
_AdGenDCProfileDestIpAddress_Object = MibTableColumn
adGenDCProfileDestIpAddress = _AdGenDCProfileDestIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 11),
    _AdGenDCProfileDestIpAddress_Type()
)
adGenDCProfileDestIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileDestIpAddress.setStatus("current")


class _AdGenDCProfileSrcMacType_Type(Integer32):
    """Custom type adGenDCProfileSrcMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noMatching", 1),
          ("mac", 2))
    )


_AdGenDCProfileSrcMacType_Type.__name__ = "Integer32"
_AdGenDCProfileSrcMacType_Object = MibTableColumn
adGenDCProfileSrcMacType = _AdGenDCProfileSrcMacType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 12),
    _AdGenDCProfileSrcMacType_Type()
)
adGenDCProfileSrcMacType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileSrcMacType.setStatus("current")
_AdGenDCProfileSrcMacAddress_Type = PhysAddress
_AdGenDCProfileSrcMacAddress_Object = MibTableColumn
adGenDCProfileSrcMacAddress = _AdGenDCProfileSrcMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 13),
    _AdGenDCProfileSrcMacAddress_Type()
)
adGenDCProfileSrcMacAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileSrcMacAddress.setStatus("current")


class _AdGenDCProfileSrcIpType_Type(Integer32):
    """Custom type adGenDCProfileSrcIpType based on Integer32"""
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
        *(("noMatching", 1),
          ("ip", 2),
          ("any", 3),
          ("none", 4))
    )


_AdGenDCProfileSrcIpType_Type.__name__ = "Integer32"
_AdGenDCProfileSrcIpType_Object = MibTableColumn
adGenDCProfileSrcIpType = _AdGenDCProfileSrcIpType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 14),
    _AdGenDCProfileSrcIpType_Type()
)
adGenDCProfileSrcIpType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileSrcIpType.setStatus("current")
_AdGenDCProfileSrcIpAddress_Type = IpAddress
_AdGenDCProfileSrcIpAddress_Object = MibTableColumn
adGenDCProfileSrcIpAddress = _AdGenDCProfileSrcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 15),
    _AdGenDCProfileSrcIpAddress_Type()
)
adGenDCProfileSrcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileSrcIpAddress.setStatus("current")
_AdGenDCProfileLastError_Type = DisplayString
_AdGenDCProfileLastError_Object = MibTableColumn
adGenDCProfileLastError = _AdGenDCProfileLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 16),
    _AdGenDCProfileLastError_Type()
)
adGenDCProfileLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCProfileLastError.setStatus("current")


class _AdGenDCProfileEgressQueueType_Type(Integer32):
    """Custom type adGenDCProfileEgressQueueType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noMatching", 1),
          ("egressQueue", 2))
    )


_AdGenDCProfileEgressQueueType_Type.__name__ = "Integer32"
_AdGenDCProfileEgressQueueType_Object = MibTableColumn
adGenDCProfileEgressQueueType = _AdGenDCProfileEgressQueueType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 17),
    _AdGenDCProfileEgressQueueType_Type()
)
adGenDCProfileEgressQueueType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileEgressQueueType.setStatus("current")


class _AdGenDCProfileEgressQueue_Type(Integer32):
    """Custom type adGenDCProfileEgressQueue based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenDCProfileEgressQueue_Type.__name__ = "Integer32"
_AdGenDCProfileEgressQueue_Object = MibTableColumn
adGenDCProfileEgressQueue = _AdGenDCProfileEgressQueue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 18),
    _AdGenDCProfileEgressQueue_Type()
)
adGenDCProfileEgressQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileEgressQueue.setStatus("current")


class _AdGenDCProfileCtagVlanType_Type(Integer32):
    """Custom type adGenDCProfileCtagVlanType based on Integer32"""
    defaultValue = 1

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
        *(("noMatching", 1),
          ("cTag", 2),
          ("allCTags", 3),
          ("noCTag", 4))
    )


_AdGenDCProfileCtagVlanType_Type.__name__ = "Integer32"
_AdGenDCProfileCtagVlanType_Object = MibTableColumn
adGenDCProfileCtagVlanType = _AdGenDCProfileCtagVlanType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 19),
    _AdGenDCProfileCtagVlanType_Type()
)
adGenDCProfileCtagVlanType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileCtagVlanType.setStatus("current")


class _AdGenDCProfileCtagVlan_Type(Integer32):
    """Custom type adGenDCProfileCtagVlan based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_AdGenDCProfileCtagVlan_Type.__name__ = "Integer32"
_AdGenDCProfileCtagVlan_Object = MibTableColumn
adGenDCProfileCtagVlan = _AdGenDCProfileCtagVlan_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 20),
    _AdGenDCProfileCtagVlan_Type()
)
adGenDCProfileCtagVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileCtagVlan.setStatus("current")


class _AdGenDCProfileCtagPriType_Type(Integer32):
    """Custom type adGenDCProfileCtagPriType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noMatching", 1),
          ("cTagPri", 2))
    )


_AdGenDCProfileCtagPriType_Type.__name__ = "Integer32"
_AdGenDCProfileCtagPriType_Object = MibTableColumn
adGenDCProfileCtagPriType = _AdGenDCProfileCtagPriType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 21),
    _AdGenDCProfileCtagPriType_Type()
)
adGenDCProfileCtagPriType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileCtagPriType.setStatus("current")


class _AdGenDCProfileCtagPri_Type(Integer32):
    """Custom type adGenDCProfileCtagPri based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AdGenDCProfileCtagPri_Type.__name__ = "Integer32"
_AdGenDCProfileCtagPri_Object = MibTableColumn
adGenDCProfileCtagPri = _AdGenDCProfileCtagPri_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 22),
    _AdGenDCProfileCtagPri_Type()
)
adGenDCProfileCtagPri.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileCtagPri.setStatus("current")
_AdGenDCProfileEvcMap_Type = DisplayString
_AdGenDCProfileEvcMap_Object = MibTableColumn
adGenDCProfileEvcMap = _AdGenDCProfileEvcMap_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 23),
    _AdGenDCProfileEvcMap_Type()
)
adGenDCProfileEvcMap.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileEvcMap.setStatus("current")


class _AdGenDCProfileDiscardReason_Type(Integer32):
    """Custom type adGenDCProfileDiscardReason based on Integer32"""
    defaultValue = 1

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
              11)
        )
    )
    namedValues = NamedValues(
        *(("noMatching", 1),
          ("any", 2),
          ("stagMatchFailed", 3),
          ("egressRecDrop", 4),
          ("forwardingFailed", 5),
          ("fullQueue", 6),
          ("invalidQueueDrop", 7),
          ("lagNotValid", 8),
          ("multicastBufferFull", 9),
          ("macsaMatchFailed", 10),
          ("none", 11))
    )


_AdGenDCProfileDiscardReason_Type.__name__ = "Integer32"
_AdGenDCProfileDiscardReason_Object = MibTableColumn
adGenDCProfileDiscardReason = _AdGenDCProfileDiscardReason_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 2, 1, 24),
    _AdGenDCProfileDiscardReason_Type()
)
adGenDCProfileDiscardReason.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCProfileDiscardReason.setStatus("current")
_AdGenDCConfigTable_Object = MibTable
adGenDCConfigTable = _AdGenDCConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 3)
)
if mibBuilder.loadTexts:
    adGenDCConfigTable.setStatus("current")
_AdGenDCConfigEntry_Object = MibTableRow
adGenDCConfigEntry = _AdGenDCConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 3, 1)
)
adGenDCConfigEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-DYNAMIC-COUNTERS-MIB", "adGenDCConfigIndex"),
)
if mibBuilder.loadTexts:
    adGenDCConfigEntry.setStatus("current")
_AdGenDCConfigIndex_Type = Integer32
_AdGenDCConfigIndex_Object = MibTableColumn
adGenDCConfigIndex = _AdGenDCConfigIndex_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 3, 1, 1),
    _AdGenDCConfigIndex_Type()
)
adGenDCConfigIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    adGenDCConfigIndex.setStatus("current")
_AdGenDCConfigRowStatus_Type = RowStatus
_AdGenDCConfigRowStatus_Object = MibTableColumn
adGenDCConfigRowStatus = _AdGenDCConfigRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 3, 1, 2),
    _AdGenDCConfigRowStatus_Type()
)
adGenDCConfigRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCConfigRowStatus.setStatus("current")
_AdGenDCConfigProfile_Type = Integer32
_AdGenDCConfigProfile_Object = MibTableColumn
adGenDCConfigProfile = _AdGenDCConfigProfile_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 3, 1, 3),
    _AdGenDCConfigProfile_Type()
)
adGenDCConfigProfile.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCConfigProfile.setStatus("current")
_AdGenDCConfigInterface_Type = InterfaceIndexOrZero
_AdGenDCConfigInterface_Object = MibTableColumn
adGenDCConfigInterface = _AdGenDCConfigInterface_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 3, 1, 4),
    _AdGenDCConfigInterface_Type()
)
adGenDCConfigInterface.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCConfigInterface.setStatus("current")


class _AdGenDCConfigType_Type(Integer32):
    """Custom type adGenDCConfigType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("rx", 2),
          ("queue", 3))
    )


_AdGenDCConfigType_Type.__name__ = "Integer32"
_AdGenDCConfigType_Object = MibTableColumn
adGenDCConfigType = _AdGenDCConfigType_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 3, 1, 5),
    _AdGenDCConfigType_Type()
)
adGenDCConfigType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCConfigType.setStatus("current")
_AdGenDCConfigInterfaceQueue_Type = Integer32
_AdGenDCConfigInterfaceQueue_Object = MibTableColumn
adGenDCConfigInterfaceQueue = _AdGenDCConfigInterfaceQueue_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 3, 1, 6),
    _AdGenDCConfigInterfaceQueue_Type()
)
adGenDCConfigInterfaceQueue.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCConfigInterfaceQueue.setStatus("current")


class _AdGenDCConfigInclude_Type(Integer32):
    """Custom type adGenDCConfigInclude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("include", 1),
          ("exclude", 2))
    )


_AdGenDCConfigInclude_Type.__name__ = "Integer32"
_AdGenDCConfigInclude_Object = MibTableColumn
adGenDCConfigInclude = _AdGenDCConfigInclude_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 3, 1, 7),
    _AdGenDCConfigInclude_Type()
)
adGenDCConfigInclude.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    adGenDCConfigInclude.setStatus("current")
_AdGenDCConfigLastError_Type = DisplayString
_AdGenDCConfigLastError_Object = MibTableColumn
adGenDCConfigLastError = _AdGenDCConfigLastError_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 3, 1, 8),
    _AdGenDCConfigLastError_Type()
)
adGenDCConfigLastError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCConfigLastError.setStatus("current")
_AdGenDCStatusTable_Object = MibTable
adGenDCStatusTable = _AdGenDCStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 4)
)
if mibBuilder.loadTexts:
    adGenDCStatusTable.setStatus("current")
_AdGenDCStatusEntry_Object = MibTableRow
adGenDCStatusEntry = _AdGenDCStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 4, 1)
)
adGenDCStatusEntry.setIndexNames(
    (0, "ADTRAN-GENSLOT-MIB", "adGenSlotInfoIndex"),
    (0, "ADTRAN-DYNAMIC-COUNTERS-MIB", "adGenDCConfigIndex"),
)
if mibBuilder.loadTexts:
    adGenDCStatusEntry.setStatus("current")
_AdGenDCStatusRowStatus_Type = RowStatus
_AdGenDCStatusRowStatus_Object = MibTableColumn
adGenDCStatusRowStatus = _AdGenDCStatusRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 4, 1, 1),
    _AdGenDCStatusRowStatus_Type()
)
adGenDCStatusRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCStatusRowStatus.setStatus("current")
_AdGenDCStatusOctets_Type = Counter64
_AdGenDCStatusOctets_Object = MibTableColumn
adGenDCStatusOctets = _AdGenDCStatusOctets_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 4, 1, 2),
    _AdGenDCStatusOctets_Type()
)
adGenDCStatusOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCStatusOctets.setStatus("current")
_AdGenDCStatusPkts_Type = Counter64
_AdGenDCStatusPkts_Object = MibTableColumn
adGenDCStatusPkts = _AdGenDCStatusPkts_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 4, 1, 3),
    _AdGenDCStatusPkts_Type()
)
adGenDCStatusPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCStatusPkts.setStatus("current")
_AdGenDCStatusAvgBitsPerSec_Type = Gauge32
_AdGenDCStatusAvgBitsPerSec_Object = MibTableColumn
adGenDCStatusAvgBitsPerSec = _AdGenDCStatusAvgBitsPerSec_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 4, 1, 4),
    _AdGenDCStatusAvgBitsPerSec_Type()
)
adGenDCStatusAvgBitsPerSec.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    adGenDCStatusAvgBitsPerSec.setStatus("current")


class _AdGenDCStatusClear_Type(Integer32):
    """Custom type adGenDCStatusClear based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("clear", 1),
          ("idle", 2))
    )


_AdGenDCStatusClear_Type.__name__ = "Integer32"
_AdGenDCStatusClear_Object = MibTableColumn
adGenDCStatusClear = _AdGenDCStatusClear_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 53, 1, 4, 1, 5),
    _AdGenDCStatusClear_Type()
)
adGenDCStatusClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenDCStatusClear.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-DYNAMIC-COUNTERS-MIB",
    **{"adGenDynamicCounterTables": adGenDynamicCounterTables,
       "adGenDCSlotTable": adGenDCSlotTable,
       "adGenDCSlotEntry": adGenDCSlotEntry,
       "adGenDCSlotSupport": adGenDCSlotSupport,
       "adGenDCSlotMaxDCProfileIndex": adGenDCSlotMaxDCProfileIndex,
       "adGenDCSlotNextDCProfileIndex": adGenDCSlotNextDCProfileIndex,
       "adGenDCSlotMaxDCIndex": adGenDCSlotMaxDCIndex,
       "adGenDCSlotNextDCIndex": adGenDCSlotNextDCIndex,
       "adGenDCSlotClearAllDC": adGenDCSlotClearAllDC,
       "adGenDCSlotLastError": adGenDCSlotLastError,
       "adGenDCProfileTable": adGenDCProfileTable,
       "adGenDCProfileEntry": adGenDCProfileEntry,
       "adGenDCProfileIndex": adGenDCProfileIndex,
       "adGenDCProfileRowStatus": adGenDCProfileRowStatus,
       "adGenDCProfileColorType": adGenDCProfileColorType,
       "adGenDCProfilePBitType": adGenDCProfilePBitType,
       "adGenDCProfilePBit": adGenDCProfilePBit,
       "adGenDCProfileSTagType": adGenDCProfileSTagType,
       "adGenDCProfileSTag": adGenDCProfileSTag,
       "adGenDCProfileDestMacType": adGenDCProfileDestMacType,
       "adGenDCProfileDestMacAddress": adGenDCProfileDestMacAddress,
       "adGenDCProfileDestIpType": adGenDCProfileDestIpType,
       "adGenDCProfileDestIpAddress": adGenDCProfileDestIpAddress,
       "adGenDCProfileSrcMacType": adGenDCProfileSrcMacType,
       "adGenDCProfileSrcMacAddress": adGenDCProfileSrcMacAddress,
       "adGenDCProfileSrcIpType": adGenDCProfileSrcIpType,
       "adGenDCProfileSrcIpAddress": adGenDCProfileSrcIpAddress,
       "adGenDCProfileLastError": adGenDCProfileLastError,
       "adGenDCProfileEgressQueueType": adGenDCProfileEgressQueueType,
       "adGenDCProfileEgressQueue": adGenDCProfileEgressQueue,
       "adGenDCProfileCtagVlanType": adGenDCProfileCtagVlanType,
       "adGenDCProfileCtagVlan": adGenDCProfileCtagVlan,
       "adGenDCProfileCtagPriType": adGenDCProfileCtagPriType,
       "adGenDCProfileCtagPri": adGenDCProfileCtagPri,
       "adGenDCProfileEvcMap": adGenDCProfileEvcMap,
       "adGenDCProfileDiscardReason": adGenDCProfileDiscardReason,
       "adGenDCConfigTable": adGenDCConfigTable,
       "adGenDCConfigEntry": adGenDCConfigEntry,
       "adGenDCConfigIndex": adGenDCConfigIndex,
       "adGenDCConfigRowStatus": adGenDCConfigRowStatus,
       "adGenDCConfigProfile": adGenDCConfigProfile,
       "adGenDCConfigInterface": adGenDCConfigInterface,
       "adGenDCConfigType": adGenDCConfigType,
       "adGenDCConfigInterfaceQueue": adGenDCConfigInterfaceQueue,
       "adGenDCConfigInclude": adGenDCConfigInclude,
       "adGenDCConfigLastError": adGenDCConfigLastError,
       "adGenDCStatusTable": adGenDCStatusTable,
       "adGenDCStatusEntry": adGenDCStatusEntry,
       "adGenDCStatusRowStatus": adGenDCStatusRowStatus,
       "adGenDCStatusOctets": adGenDCStatusOctets,
       "adGenDCStatusPkts": adGenDCStatusPkts,
       "adGenDCStatusAvgBitsPerSec": adGenDCStatusAvgBitsPerSec,
       "adGenDCStatusClear": adGenDCStatusClear,
       "adGenDynamicCounterMIB": adGenDynamicCounterMIB}
)
