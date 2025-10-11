# SNMP MIB module (ARICENT-OSPF-TE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-OSPF-TE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:24 2025
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

futOspfTe = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 72)
)
if mibBuilder.loadTexts:
    futOspfTe.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AreaID(TextualConvention, IpAddress):
    status = "current"


class RouterID(TextualConvention, IpAddress):
    status = "current"


class InterfaceIndex(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"


class BandWidth(TextualConvention, Counter64):
    status = "current"
    displayHint = "d"


class TeLinkPriority(TextualConvention, Integer32):
    status = "current"
    displayHint = "d"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )



class TeLinkEncodingType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              5,
              7,
              8,
              9,
              11)
        )
    )
    namedValues = NamedValues(
        *(("packet", 1),
          ("ethernet", 2),
          ("ansiEtsiPdh", 3),
          ("sdhItuSonetAnsi", 5),
          ("digitalWrapper", 7),
          ("lambda", 8),
          ("fiber", 9),
          ("fiberChannel", 11))
    )



# MIB Managed Objects in the order of their OIDs

_FutOspfTeGeneralGroup_ObjectIdentity = ObjectIdentity
futOspfTeGeneralGroup = _FutOspfTeGeneralGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2076, 72, 1)
)


class _FutOspfTeAdminStatus_Type(Integer32):
    """Custom type futOspfTeAdminStatus based on Integer32"""
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


_FutOspfTeAdminStatus_Type.__name__ = "Integer32"
_FutOspfTeAdminStatus_Object = MibScalar
futOspfTeAdminStatus = _FutOspfTeAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 1, 1),
    _FutOspfTeAdminStatus_Type()
)
futOspfTeAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfTeAdminStatus.setStatus("current")


class _FutOspfTeTraceLevel_Type(Integer32):
    """Custom type futOspfTeTraceLevel based on Integer32"""
    defaultValue = 1


_FutOspfTeTraceLevel_Type.__name__ = "Integer32"
_FutOspfTeTraceLevel_Object = MibScalar
futOspfTeTraceLevel = _FutOspfTeTraceLevel_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 1, 2),
    _FutOspfTeTraceLevel_Type()
)
futOspfTeTraceLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    futOspfTeTraceLevel.setStatus("current")
_FutOspfTeCspfRunCnt_Type = Counter32
_FutOspfTeCspfRunCnt_Object = MibScalar
futOspfTeCspfRunCnt = _FutOspfTeCspfRunCnt_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 1, 3),
    _FutOspfTeCspfRunCnt_Type()
)
futOspfTeCspfRunCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeCspfRunCnt.setStatus("current")
_FutOspfTeLsdbTable_Object = MibTable
futOspfTeLsdbTable = _FutOspfTeLsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 2)
)
if mibBuilder.loadTexts:
    futOspfTeLsdbTable.setStatus("current")
_FutOspfTeLsdbEntry_Object = MibTableRow
futOspfTeLsdbEntry = _FutOspfTeLsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 2, 1)
)
futOspfTeLsdbEntry.setIndexNames(
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeLsdbAreaId"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeLsdbType"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeLsdbLsid"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeLsdbRouterId"),
)
if mibBuilder.loadTexts:
    futOspfTeLsdbEntry.setStatus("current")
_FutOspfTeLsdbAreaId_Type = AreaID
_FutOspfTeLsdbAreaId_Object = MibTableColumn
futOspfTeLsdbAreaId = _FutOspfTeLsdbAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 2, 1, 1),
    _FutOspfTeLsdbAreaId_Type()
)
futOspfTeLsdbAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeLsdbAreaId.setStatus("current")


class _FutOspfTeLsdbType_Type(Integer32):
    """Custom type futOspfTeLsdbType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              10)
        )
    )
    namedValues = NamedValues(
        *(("routerLSA", 1),
          ("networkLSA", 2),
          ("type10OpaqueLSA", 10))
    )


_FutOspfTeLsdbType_Type.__name__ = "Integer32"
_FutOspfTeLsdbType_Object = MibTableColumn
futOspfTeLsdbType = _FutOspfTeLsdbType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 2, 1, 2),
    _FutOspfTeLsdbType_Type()
)
futOspfTeLsdbType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeLsdbType.setStatus("current")
_FutOspfTeLsdbLsid_Type = IpAddress
_FutOspfTeLsdbLsid_Object = MibTableColumn
futOspfTeLsdbLsid = _FutOspfTeLsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 2, 1, 3),
    _FutOspfTeLsdbLsid_Type()
)
futOspfTeLsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeLsdbLsid.setStatus("current")
_FutOspfTeLsdbRouterId_Type = RouterID
_FutOspfTeLsdbRouterId_Object = MibTableColumn
futOspfTeLsdbRouterId = _FutOspfTeLsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 2, 1, 4),
    _FutOspfTeLsdbRouterId_Type()
)
futOspfTeLsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeLsdbRouterId.setStatus("current")
_FutOspfTeLsdbChecksum_Type = Integer32
_FutOspfTeLsdbChecksum_Object = MibTableColumn
futOspfTeLsdbChecksum = _FutOspfTeLsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 2, 1, 5),
    _FutOspfTeLsdbChecksum_Type()
)
futOspfTeLsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeLsdbChecksum.setStatus("current")


class _FutOspfTeLsdbAdvertisement_Type(OctetString):
    """Custom type futOspfTeLsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_FutOspfTeLsdbAdvertisement_Type.__name__ = "OctetString"
_FutOspfTeLsdbAdvertisement_Object = MibTableColumn
futOspfTeLsdbAdvertisement = _FutOspfTeLsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 2, 1, 6),
    _FutOspfTeLsdbAdvertisement_Type()
)
futOspfTeLsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeLsdbAdvertisement.setStatus("current")
_FutOspfTeType9LsdbTable_Object = MibTable
futOspfTeType9LsdbTable = _FutOspfTeType9LsdbTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 3)
)
if mibBuilder.loadTexts:
    futOspfTeType9LsdbTable.setStatus("current")
_FutOspfTeType9LsdbEntry_Object = MibTableRow
futOspfTeType9LsdbEntry = _FutOspfTeType9LsdbEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 3, 1)
)
futOspfTeType9LsdbEntry.setIndexNames(
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeType9LsdbIfIpAddress"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeType9LsdbIfIndex"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeType9LsdbLsid"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeType9LsdbRouterId"),
)
if mibBuilder.loadTexts:
    futOspfTeType9LsdbEntry.setStatus("current")
_FutOspfTeType9LsdbIfIpAddress_Type = IpAddress
_FutOspfTeType9LsdbIfIpAddress_Object = MibTableColumn
futOspfTeType9LsdbIfIpAddress = _FutOspfTeType9LsdbIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 3, 1, 1),
    _FutOspfTeType9LsdbIfIpAddress_Type()
)
futOspfTeType9LsdbIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeType9LsdbIfIpAddress.setStatus("current")


class _FutOspfTeType9LsdbIfIndex_Type(InterfaceIndex):
    """Custom type futOspfTeType9LsdbIfIndex based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FutOspfTeType9LsdbIfIndex_Type.__name__ = "InterfaceIndex"
_FutOspfTeType9LsdbIfIndex_Object = MibTableColumn
futOspfTeType9LsdbIfIndex = _FutOspfTeType9LsdbIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 3, 1, 2),
    _FutOspfTeType9LsdbIfIndex_Type()
)
futOspfTeType9LsdbIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeType9LsdbIfIndex.setStatus("current")
_FutOspfTeType9LsdbLsid_Type = IpAddress
_FutOspfTeType9LsdbLsid_Object = MibTableColumn
futOspfTeType9LsdbLsid = _FutOspfTeType9LsdbLsid_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 3, 1, 3),
    _FutOspfTeType9LsdbLsid_Type()
)
futOspfTeType9LsdbLsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeType9LsdbLsid.setStatus("current")
_FutOspfTeType9LsdbRouterId_Type = RouterID
_FutOspfTeType9LsdbRouterId_Object = MibTableColumn
futOspfTeType9LsdbRouterId = _FutOspfTeType9LsdbRouterId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 3, 1, 4),
    _FutOspfTeType9LsdbRouterId_Type()
)
futOspfTeType9LsdbRouterId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeType9LsdbRouterId.setStatus("current")
_FutOspfTeType9LsdbChecksum_Type = Integer32
_FutOspfTeType9LsdbChecksum_Object = MibTableColumn
futOspfTeType9LsdbChecksum = _FutOspfTeType9LsdbChecksum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 3, 1, 5),
    _FutOspfTeType9LsdbChecksum_Type()
)
futOspfTeType9LsdbChecksum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeType9LsdbChecksum.setStatus("current")


class _FutOspfTeType9LsdbAdvertisement_Type(OctetString):
    """Custom type futOspfTeType9LsdbAdvertisement based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 65535),
    )


_FutOspfTeType9LsdbAdvertisement_Type.__name__ = "OctetString"
_FutOspfTeType9LsdbAdvertisement_Object = MibTableColumn
futOspfTeType9LsdbAdvertisement = _FutOspfTeType9LsdbAdvertisement_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 3, 1, 6),
    _FutOspfTeType9LsdbAdvertisement_Type()
)
futOspfTeType9LsdbAdvertisement.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeType9LsdbAdvertisement.setStatus("current")
_FutOspfTeAreaTable_Object = MibTable
futOspfTeAreaTable = _FutOspfTeAreaTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 4)
)
if mibBuilder.loadTexts:
    futOspfTeAreaTable.setStatus("current")
_FutOspfTeAreaEntry_Object = MibTableRow
futOspfTeAreaEntry = _FutOspfTeAreaEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 4, 1)
)
futOspfTeAreaEntry.setIndexNames(
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeAreaId"),
)
if mibBuilder.loadTexts:
    futOspfTeAreaEntry.setStatus("current")
_FutOspfTeAreaId_Type = AreaID
_FutOspfTeAreaId_Object = MibTableColumn
futOspfTeAreaId = _FutOspfTeAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 4, 1, 1),
    _FutOspfTeAreaId_Type()
)
futOspfTeAreaId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeAreaId.setStatus("current")
_FutOspfTeAreaLsaCount_Type = Integer32
_FutOspfTeAreaLsaCount_Object = MibTableColumn
futOspfTeAreaLsaCount = _FutOspfTeAreaLsaCount_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 4, 1, 2),
    _FutOspfTeAreaLsaCount_Type()
)
futOspfTeAreaLsaCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeAreaLsaCount.setStatus("current")
_FutOspfTeType10AreaCksumSum_Type = Integer32
_FutOspfTeType10AreaCksumSum_Object = MibTableColumn
futOspfTeType10AreaCksumSum = _FutOspfTeType10AreaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 4, 1, 3),
    _FutOspfTeType10AreaCksumSum_Type()
)
futOspfTeType10AreaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeType10AreaCksumSum.setStatus("current")
_FutOspfTeType2AreaCksumSum_Type = Integer32
_FutOspfTeType2AreaCksumSum_Object = MibTableColumn
futOspfTeType2AreaCksumSum = _FutOspfTeType2AreaCksumSum_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 4, 1, 4),
    _FutOspfTeType2AreaCksumSum_Type()
)
futOspfTeType2AreaCksumSum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeType2AreaCksumSum.setStatus("current")
_FutOspfTeIfTable_Object = MibTable
futOspfTeIfTable = _FutOspfTeIfTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5)
)
if mibBuilder.loadTexts:
    futOspfTeIfTable.setStatus("current")
_FutOspfTeIfEntry_Object = MibTableRow
futOspfTeIfEntry = _FutOspfTeIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1)
)
futOspfTeIfEntry.setIndexNames(
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeIfIpAddress"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeAddressLessIf"),
)
if mibBuilder.loadTexts:
    futOspfTeIfEntry.setStatus("current")
_FutOspfTeIfIpAddress_Type = IpAddress
_FutOspfTeIfIpAddress_Object = MibTableColumn
futOspfTeIfIpAddress = _FutOspfTeIfIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 1),
    _FutOspfTeIfIpAddress_Type()
)
futOspfTeIfIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeIfIpAddress.setStatus("current")


class _FutOspfTeAddressLessIf_Type(InterfaceIndex):
    """Custom type futOspfTeAddressLessIf based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FutOspfTeAddressLessIf_Type.__name__ = "InterfaceIndex"
_FutOspfTeAddressLessIf_Object = MibTableColumn
futOspfTeAddressLessIf = _FutOspfTeAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 2),
    _FutOspfTeAddressLessIf_Type()
)
futOspfTeAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeAddressLessIf.setStatus("current")
_FutOspfTeIfAreaId_Type = AreaID
_FutOspfTeIfAreaId_Object = MibTableColumn
futOspfTeIfAreaId = _FutOspfTeIfAreaId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 3),
    _FutOspfTeIfAreaId_Type()
)
futOspfTeIfAreaId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfAreaId.setStatus("current")


class _FutOspfTeIfType_Type(Integer32):
    """Custom type futOspfTeIfType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("pointToPoint", 1),
          ("multiaccess", 2))
    )


_FutOspfTeIfType_Type.__name__ = "Integer32"
_FutOspfTeIfType_Object = MibTableColumn
futOspfTeIfType = _FutOspfTeIfType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 4),
    _FutOspfTeIfType_Type()
)
futOspfTeIfType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfType.setStatus("current")
_FutOspfTeIfMetric_Type = Integer32
_FutOspfTeIfMetric_Object = MibTableColumn
futOspfTeIfMetric = _FutOspfTeIfMetric_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 5),
    _FutOspfTeIfMetric_Type()
)
futOspfTeIfMetric.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfMetric.setStatus("current")
_FutOspfTeIfMaxBw_Type = BandWidth
_FutOspfTeIfMaxBw_Object = MibTableColumn
futOspfTeIfMaxBw = _FutOspfTeIfMaxBw_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 6),
    _FutOspfTeIfMaxBw_Type()
)
futOspfTeIfMaxBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfMaxBw.setStatus("current")
_FutOspfTeIfMaxReservBw_Type = BandWidth
_FutOspfTeIfMaxReservBw_Object = MibTableColumn
futOspfTeIfMaxReservBw = _FutOspfTeIfMaxReservBw_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 7),
    _FutOspfTeIfMaxReservBw_Type()
)
futOspfTeIfMaxReservBw.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfMaxReservBw.setStatus("current")
_FutOspfTeIfRsrcClassColor_Type = Integer32
_FutOspfTeIfRsrcClassColor_Object = MibTableColumn
futOspfTeIfRsrcClassColor = _FutOspfTeIfRsrcClassColor_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 8),
    _FutOspfTeIfRsrcClassColor_Type()
)
futOspfTeIfRsrcClassColor.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfRsrcClassColor.setStatus("current")


class _FutOspfTeIfOperStat_Type(Integer32):
    """Custom type futOspfTeIfOperStat based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 1),
          ("notInService", 2),
          ("active", 3))
    )


_FutOspfTeIfOperStat_Type.__name__ = "Integer32"
_FutOspfTeIfOperStat_Object = MibTableColumn
futOspfTeIfOperStat = _FutOspfTeIfOperStat_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 9),
    _FutOspfTeIfOperStat_Type()
)
futOspfTeIfOperStat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfOperStat.setStatus("current")
_FutOspfTeIfLinkId_Type = IpAddress
_FutOspfTeIfLinkId_Object = MibTableColumn
futOspfTeIfLinkId = _FutOspfTeIfLinkId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 10),
    _FutOspfTeIfLinkId_Type()
)
futOspfTeIfLinkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfLinkId.setStatus("current")
_FutOspfTeIfRemoteIpAddr_Type = IpAddress
_FutOspfTeIfRemoteIpAddr_Object = MibTableColumn
futOspfTeIfRemoteIpAddr = _FutOspfTeIfRemoteIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 11),
    _FutOspfTeIfRemoteIpAddr_Type()
)
futOspfTeIfRemoteIpAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfRemoteIpAddr.setStatus("current")


class _FutOspfTeIfProtectionType_Type(Integer32):
    """Custom type futOspfTeIfProtectionType based on Integer32"""
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
        *(("extraTraffic", 1),
          ("unprotected", 2),
          ("shared", 3),
          ("dedicated1For1", 4),
          ("dedicated1Plus1", 5),
          ("enhanced", 6))
    )


_FutOspfTeIfProtectionType_Type.__name__ = "Integer32"
_FutOspfTeIfProtectionType_Object = MibTableColumn
futOspfTeIfProtectionType = _FutOspfTeIfProtectionType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 12),
    _FutOspfTeIfProtectionType_Type()
)
futOspfTeIfProtectionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfProtectionType.setStatus("current")
_FutOspfTeIfSrlg_Type = OctetString
_FutOspfTeIfSrlg_Object = MibTableColumn
futOspfTeIfSrlg = _FutOspfTeIfSrlg_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 5, 1, 13),
    _FutOspfTeIfSrlg_Type()
)
futOspfTeIfSrlg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfSrlg.setStatus("current")
_FutOspfTeIfDescriptorTable_Object = MibTable
futOspfTeIfDescriptorTable = _FutOspfTeIfDescriptorTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 6)
)
if mibBuilder.loadTexts:
    futOspfTeIfDescriptorTable.setStatus("current")
_FutOspfTeIfDescriptorEntry_Object = MibTableRow
futOspfTeIfDescriptorEntry = _FutOspfTeIfDescriptorEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 6, 1)
)
futOspfTeIfDescriptorEntry.setIndexNames(
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeIfDescrIpAddress"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeIfDescrAddressLessIf"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeIfDescrId"),
)
if mibBuilder.loadTexts:
    futOspfTeIfDescriptorEntry.setStatus("current")
_FutOspfTeIfDescrIpAddress_Type = IpAddress
_FutOspfTeIfDescrIpAddress_Object = MibTableColumn
futOspfTeIfDescrIpAddress = _FutOspfTeIfDescrIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 6, 1, 1),
    _FutOspfTeIfDescrIpAddress_Type()
)
futOspfTeIfDescrIpAddress.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeIfDescrIpAddress.setStatus("current")


class _FutOspfTeIfDescrAddressLessIf_Type(InterfaceIndex):
    """Custom type futOspfTeIfDescrAddressLessIf based on InterfaceIndex"""
    subtypeSpec = InterfaceIndex.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_FutOspfTeIfDescrAddressLessIf_Type.__name__ = "InterfaceIndex"
_FutOspfTeIfDescrAddressLessIf_Object = MibTableColumn
futOspfTeIfDescrAddressLessIf = _FutOspfTeIfDescrAddressLessIf_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 6, 1, 2),
    _FutOspfTeIfDescrAddressLessIf_Type()
)
futOspfTeIfDescrAddressLessIf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeIfDescrAddressLessIf.setStatus("current")


class _FutOspfTeIfDescrId_Type(Unsigned32):
    """Custom type futOspfTeIfDescrId based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FutOspfTeIfDescrId_Type.__name__ = "Unsigned32"
_FutOspfTeIfDescrId_Object = MibTableColumn
futOspfTeIfDescrId = _FutOspfTeIfDescrId_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 6, 1, 3),
    _FutOspfTeIfDescrId_Type()
)
futOspfTeIfDescrId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeIfDescrId.setStatus("current")


class _FutOspfTeIfDescrSwithingCap_Type(Integer32):
    """Custom type futOspfTeIfDescrSwithingCap based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              51,
              100,
              150,
              200)
        )
    )
    namedValues = NamedValues(
        *(("psc1", 1),
          ("psc2", 2),
          ("psc3", 3),
          ("psc4", 4),
          ("l2sc", 51),
          ("tdm", 100),
          ("lsc", 150),
          ("fsc", 200))
    )


_FutOspfTeIfDescrSwithingCap_Type.__name__ = "Integer32"
_FutOspfTeIfDescrSwithingCap_Object = MibTableColumn
futOspfTeIfDescrSwithingCap = _FutOspfTeIfDescrSwithingCap_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 6, 1, 4),
    _FutOspfTeIfDescrSwithingCap_Type()
)
futOspfTeIfDescrSwithingCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfDescrSwithingCap.setStatus("current")
_FutOspfTeIfDescrEncodingType_Type = TeLinkEncodingType
_FutOspfTeIfDescrEncodingType_Object = MibTableColumn
futOspfTeIfDescrEncodingType = _FutOspfTeIfDescrEncodingType_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 6, 1, 5),
    _FutOspfTeIfDescrEncodingType_Type()
)
futOspfTeIfDescrEncodingType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfDescrEncodingType.setStatus("current")
_FutOspfTeIfDescrMinLSPBandwidth_Type = BandWidth
_FutOspfTeIfDescrMinLSPBandwidth_Object = MibTableColumn
futOspfTeIfDescrMinLSPBandwidth = _FutOspfTeIfDescrMinLSPBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 6, 1, 6),
    _FutOspfTeIfDescrMinLSPBandwidth_Type()
)
futOspfTeIfDescrMinLSPBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfDescrMinLSPBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    futOspfTeIfDescrMinLSPBandwidth.setUnits("thousand bps")
_FutOspfTeIfDescrMTU_Type = Integer32
_FutOspfTeIfDescrMTU_Object = MibTableColumn
futOspfTeIfDescrMTU = _FutOspfTeIfDescrMTU_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 6, 1, 7),
    _FutOspfTeIfDescrMTU_Type()
)
futOspfTeIfDescrMTU.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfDescrMTU.setStatus("current")
_FutOspfTeIfDescrIndication_Type = Integer32
_FutOspfTeIfDescrIndication_Object = MibTableColumn
futOspfTeIfDescrIndication = _FutOspfTeIfDescrIndication_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 6, 1, 8),
    _FutOspfTeIfDescrIndication_Type()
)
futOspfTeIfDescrIndication.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfDescrIndication.setStatus("current")
_FutOspfTeIfSwDescrMaxBwTable_Object = MibTable
futOspfTeIfSwDescrMaxBwTable = _FutOspfTeIfSwDescrMaxBwTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 7)
)
if mibBuilder.loadTexts:
    futOspfTeIfSwDescrMaxBwTable.setStatus("current")
_FutOspfTeIfSwDescrMaxBwEntry_Object = MibTableRow
futOspfTeIfSwDescrMaxBwEntry = _FutOspfTeIfSwDescrMaxBwEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 7, 1)
)
futOspfTeIfSwDescrMaxBwEntry.setIndexNames(
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeIfDescrIpAddress"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeIfDescrAddressLessIf"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeIfDescrId"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeIfSwDescrMaxBwPriority"),
)
if mibBuilder.loadTexts:
    futOspfTeIfSwDescrMaxBwEntry.setStatus("current")
_FutOspfTeIfSwDescrMaxBwPriority_Type = TeLinkPriority
_FutOspfTeIfSwDescrMaxBwPriority_Object = MibTableColumn
futOspfTeIfSwDescrMaxBwPriority = _FutOspfTeIfSwDescrMaxBwPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 7, 1, 1),
    _FutOspfTeIfSwDescrMaxBwPriority_Type()
)
futOspfTeIfSwDescrMaxBwPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeIfSwDescrMaxBwPriority.setStatus("current")
_FutOspfTeIfSwDescrMaxLSPBandwidth_Type = BandWidth
_FutOspfTeIfSwDescrMaxLSPBandwidth_Object = MibTableColumn
futOspfTeIfSwDescrMaxLSPBandwidth = _FutOspfTeIfSwDescrMaxLSPBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 7, 1, 2),
    _FutOspfTeIfSwDescrMaxLSPBandwidth_Type()
)
futOspfTeIfSwDescrMaxLSPBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfSwDescrMaxLSPBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    futOspfTeIfSwDescrMaxLSPBandwidth.setUnits("thousand bps")
_FutOspfTeIfBandwidthTable_Object = MibTable
futOspfTeIfBandwidthTable = _FutOspfTeIfBandwidthTable_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 8)
)
if mibBuilder.loadTexts:
    futOspfTeIfBandwidthTable.setStatus("current")
_FutOspfTeIfBandwidthEntry_Object = MibTableRow
futOspfTeIfBandwidthEntry = _FutOspfTeIfBandwidthEntry_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 8, 1)
)
futOspfTeIfBandwidthEntry.setIndexNames(
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeIfIpAddress"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeAddressLessIf"),
    (0, "ARICENT-OSPF-TE-MIB", "futOspfTeIfBandwidthPriority"),
)
if mibBuilder.loadTexts:
    futOspfTeIfBandwidthEntry.setStatus("current")
_FutOspfTeIfBandwidthPriority_Type = TeLinkPriority
_FutOspfTeIfBandwidthPriority_Object = MibTableColumn
futOspfTeIfBandwidthPriority = _FutOspfTeIfBandwidthPriority_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 8, 1, 1),
    _FutOspfTeIfBandwidthPriority_Type()
)
futOspfTeIfBandwidthPriority.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    futOspfTeIfBandwidthPriority.setStatus("current")
_FutOspfTeIfUnreservedBandwidth_Type = BandWidth
_FutOspfTeIfUnreservedBandwidth_Object = MibTableColumn
futOspfTeIfUnreservedBandwidth = _FutOspfTeIfUnreservedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 2076, 72, 8, 1, 2),
    _FutOspfTeIfUnreservedBandwidth_Type()
)
futOspfTeIfUnreservedBandwidth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    futOspfTeIfUnreservedBandwidth.setStatus("current")
if mibBuilder.loadTexts:
    futOspfTeIfUnreservedBandwidth.setUnits("thousand bps")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-OSPF-TE-MIB",
    **{"AreaID": AreaID,
       "RouterID": RouterID,
       "InterfaceIndex": InterfaceIndex,
       "BandWidth": BandWidth,
       "TeLinkPriority": TeLinkPriority,
       "TeLinkEncodingType": TeLinkEncodingType,
       "futOspfTe": futOspfTe,
       "futOspfTeGeneralGroup": futOspfTeGeneralGroup,
       "futOspfTeAdminStatus": futOspfTeAdminStatus,
       "futOspfTeTraceLevel": futOspfTeTraceLevel,
       "futOspfTeCspfRunCnt": futOspfTeCspfRunCnt,
       "futOspfTeLsdbTable": futOspfTeLsdbTable,
       "futOspfTeLsdbEntry": futOspfTeLsdbEntry,
       "futOspfTeLsdbAreaId": futOspfTeLsdbAreaId,
       "futOspfTeLsdbType": futOspfTeLsdbType,
       "futOspfTeLsdbLsid": futOspfTeLsdbLsid,
       "futOspfTeLsdbRouterId": futOspfTeLsdbRouterId,
       "futOspfTeLsdbChecksum": futOspfTeLsdbChecksum,
       "futOspfTeLsdbAdvertisement": futOspfTeLsdbAdvertisement,
       "futOspfTeType9LsdbTable": futOspfTeType9LsdbTable,
       "futOspfTeType9LsdbEntry": futOspfTeType9LsdbEntry,
       "futOspfTeType9LsdbIfIpAddress": futOspfTeType9LsdbIfIpAddress,
       "futOspfTeType9LsdbIfIndex": futOspfTeType9LsdbIfIndex,
       "futOspfTeType9LsdbLsid": futOspfTeType9LsdbLsid,
       "futOspfTeType9LsdbRouterId": futOspfTeType9LsdbRouterId,
       "futOspfTeType9LsdbChecksum": futOspfTeType9LsdbChecksum,
       "futOspfTeType9LsdbAdvertisement": futOspfTeType9LsdbAdvertisement,
       "futOspfTeAreaTable": futOspfTeAreaTable,
       "futOspfTeAreaEntry": futOspfTeAreaEntry,
       "futOspfTeAreaId": futOspfTeAreaId,
       "futOspfTeAreaLsaCount": futOspfTeAreaLsaCount,
       "futOspfTeType10AreaCksumSum": futOspfTeType10AreaCksumSum,
       "futOspfTeType2AreaCksumSum": futOspfTeType2AreaCksumSum,
       "futOspfTeIfTable": futOspfTeIfTable,
       "futOspfTeIfEntry": futOspfTeIfEntry,
       "futOspfTeIfIpAddress": futOspfTeIfIpAddress,
       "futOspfTeAddressLessIf": futOspfTeAddressLessIf,
       "futOspfTeIfAreaId": futOspfTeIfAreaId,
       "futOspfTeIfType": futOspfTeIfType,
       "futOspfTeIfMetric": futOspfTeIfMetric,
       "futOspfTeIfMaxBw": futOspfTeIfMaxBw,
       "futOspfTeIfMaxReservBw": futOspfTeIfMaxReservBw,
       "futOspfTeIfRsrcClassColor": futOspfTeIfRsrcClassColor,
       "futOspfTeIfOperStat": futOspfTeIfOperStat,
       "futOspfTeIfLinkId": futOspfTeIfLinkId,
       "futOspfTeIfRemoteIpAddr": futOspfTeIfRemoteIpAddr,
       "futOspfTeIfProtectionType": futOspfTeIfProtectionType,
       "futOspfTeIfSrlg": futOspfTeIfSrlg,
       "futOspfTeIfDescriptorTable": futOspfTeIfDescriptorTable,
       "futOspfTeIfDescriptorEntry": futOspfTeIfDescriptorEntry,
       "futOspfTeIfDescrIpAddress": futOspfTeIfDescrIpAddress,
       "futOspfTeIfDescrAddressLessIf": futOspfTeIfDescrAddressLessIf,
       "futOspfTeIfDescrId": futOspfTeIfDescrId,
       "futOspfTeIfDescrSwithingCap": futOspfTeIfDescrSwithingCap,
       "futOspfTeIfDescrEncodingType": futOspfTeIfDescrEncodingType,
       "futOspfTeIfDescrMinLSPBandwidth": futOspfTeIfDescrMinLSPBandwidth,
       "futOspfTeIfDescrMTU": futOspfTeIfDescrMTU,
       "futOspfTeIfDescrIndication": futOspfTeIfDescrIndication,
       "futOspfTeIfSwDescrMaxBwTable": futOspfTeIfSwDescrMaxBwTable,
       "futOspfTeIfSwDescrMaxBwEntry": futOspfTeIfSwDescrMaxBwEntry,
       "futOspfTeIfSwDescrMaxBwPriority": futOspfTeIfSwDescrMaxBwPriority,
       "futOspfTeIfSwDescrMaxLSPBandwidth": futOspfTeIfSwDescrMaxLSPBandwidth,
       "futOspfTeIfBandwidthTable": futOspfTeIfBandwidthTable,
       "futOspfTeIfBandwidthEntry": futOspfTeIfBandwidthEntry,
       "futOspfTeIfBandwidthPriority": futOspfTeIfBandwidthPriority,
       "futOspfTeIfUnreservedBandwidth": futOspfTeIfUnreservedBandwidth}
)
