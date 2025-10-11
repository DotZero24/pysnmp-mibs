# SNMP MIB module (QTECH-L3Igmp-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-L3Igmp-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:57:39 2025
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

(PortList,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "PortList")

(gbnL3,) = mibBuilder.importSymbols(
    "QTECH-MASTER-MIB",
    "gbnL3")

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
 iso,
 mib_2) = mibBuilder.importSymbols(
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
    "iso",
    "mib-2")

(DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

gbnL3IgmpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7)
)
if mibBuilder.loadTexts:
    gbnL3IgmpMib.setRevisions(
        ("1904-11-19 00:01",)
    )


# Types definitions



class FilterMode(Integer32):
    """Custom type FilterMode based on Integer32"""
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




# TEXTUAL-CONVENTIONS



class PortList(TextualConvention, OctetString):
    status = "current"


# MIB Managed Objects in the order of their OIDs

_GbnL3IgmpProxyGroup_ObjectIdentity = ObjectIdentity
gbnL3IgmpProxyGroup = _GbnL3IgmpProxyGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 1)
)
_IgmpProxyEnable_Type = TruthValue
_IgmpProxyEnable_Object = MibScalar
igmpProxyEnable = _IgmpProxyEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 1, 1),
    _IgmpProxyEnable_Type()
)
igmpProxyEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpProxyEnable.setStatus("current")
_IgmpProxyIfIndex_Type = Integer32
_IgmpProxyIfIndex_Object = MibScalar
igmpProxyIfIndex = _IgmpProxyIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 1, 2),
    _IgmpProxyIfIndex_Type()
)
igmpProxyIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpProxyIfIndex.setStatus("current")
_IgmpGrpNum_Type = Integer32
_IgmpGrpNum_Object = MibScalar
igmpGrpNum = _IgmpGrpNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 1, 3),
    _IgmpGrpNum_Type()
)
igmpGrpNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGrpNum.setStatus("current")
_IgmpGrpMembNum_Type = Integer32
_IgmpGrpMembNum_Object = MibScalar
igmpGrpMembNum = _IgmpGrpMembNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 1, 4),
    _IgmpGrpMembNum_Type()
)
igmpGrpMembNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpGrpMembNum.setStatus("current")
_IgmpIfExTable_Object = MibTable
igmpIfExTable = _IgmpIfExTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 2)
)
if mibBuilder.loadTexts:
    igmpIfExTable.setStatus("current")
_IgmpIfExEntry_Object = MibTableRow
igmpIfExEntry = _IgmpIfExEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 2, 1)
)
igmpIfExEntry.setIndexNames(
    (0, "QTECH-L3Igmp-MIB", "igmpifIndex"),
)
if mibBuilder.loadTexts:
    igmpIfExEntry.setStatus("current")
_IgmpifIndex_Type = Integer32
_IgmpifIndex_Object = MibTableColumn
igmpifIndex = _IgmpifIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 2, 1, 1),
    _IgmpifIndex_Type()
)
igmpifIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpifIndex.setStatus("current")
_IgmpIfPortList_Type = PortList
_IgmpIfPortList_Object = MibTableColumn
igmpIfPortList = _IgmpIfPortList_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 2, 1, 2),
    _IgmpIfPortList_Type()
)
igmpIfPortList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpIfPortList.setStatus("current")
_IgmpifAccessNum_Type = Integer32
_IgmpifAccessNum_Object = MibTableColumn
igmpifAccessNum = _IgmpifAccessNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 2, 1, 3),
    _IgmpifAccessNum_Type()
)
igmpifAccessNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpifAccessNum.setStatus("current")
_IgmpifQuerierExpire_Type = Integer32
_IgmpifQuerierExpire_Object = MibTableColumn
igmpifQuerierExpire = _IgmpifQuerierExpire_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 2, 1, 4),
    _IgmpifQuerierExpire_Type()
)
igmpifQuerierExpire.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpifQuerierExpire.setStatus("current")
_IgmpifV2QuerierTimer_Type = TimeTicks
_IgmpifV2QuerierTimer_Object = MibTableColumn
igmpifV2QuerierTimer = _IgmpifV2QuerierTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 2, 1, 5),
    _IgmpifV2QuerierTimer_Type()
)
igmpifV2QuerierTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpifV2QuerierTimer.setStatus("current")
_IgmpifLimiGroupNum_Type = Integer32
_IgmpifLimiGroupNum_Object = MibTableColumn
igmpifLimiGroupNum = _IgmpifLimiGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 2, 1, 6),
    _IgmpifLimiGroupNum_Type()
)
igmpifLimiGroupNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpifLimiGroupNum.setStatus("current")
_IgmpGroupVlanTable_Object = MibTable
igmpGroupVlanTable = _IgmpGroupVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 3)
)
if mibBuilder.loadTexts:
    igmpGroupVlanTable.setStatus("current")
_IgmpGroupVlanEntry_Object = MibTableRow
igmpGroupVlanEntry = _IgmpGroupVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 3, 1)
)
igmpGroupVlanEntry.setIndexNames(
    (0, "QTECH-L3Igmp-MIB", "igmpGroupIP"),
    (0, "QTECH-L3Igmp-MIB", "igmpVlanID"),
)
if mibBuilder.loadTexts:
    igmpGroupVlanEntry.setStatus("current")
_IgmpGroupIP_Type = IpAddress
_IgmpGroupIP_Object = MibTableColumn
igmpGroupIP = _IgmpGroupIP_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 3, 1, 1),
    _IgmpGroupIP_Type()
)
igmpGroupIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpGroupIP.setStatus("current")
_IgmpVlanID_Type = Integer32
_IgmpVlanID_Object = MibTableColumn
igmpVlanID = _IgmpVlanID_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 3, 1, 2),
    _IgmpVlanID_Type()
)
igmpVlanID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpVlanID.setStatus("current")
_IgmpGroupVlanStatus_Type = RowStatus
_IgmpGroupVlanStatus_Object = MibTableColumn
igmpGroupVlanStatus = _IgmpGroupVlanStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 3, 1, 3),
    _IgmpGroupVlanStatus_Type()
)
igmpGroupVlanStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpGroupVlanStatus.setStatus("current")
_IgmpCacheTableEx_Object = MibTable
igmpCacheTableEx = _IgmpCacheTableEx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 4)
)
if mibBuilder.loadTexts:
    igmpCacheTableEx.setStatus("current")
_IgmpCacheExEntry_Object = MibTableRow
igmpCacheExEntry = _IgmpCacheExEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 4, 1)
)
igmpCacheExEntry.setIndexNames(
    (0, "QTECH-L3Igmp-MIB", "igmpCacheAddressEx"),
    (0, "QTECH-L3Igmp-MIB", "igmpCacheIfIdxEx"),
)
if mibBuilder.loadTexts:
    igmpCacheExEntry.setStatus("current")
_IgmpCacheAddressEx_Type = IpAddress
_IgmpCacheAddressEx_Object = MibTableColumn
igmpCacheAddressEx = _IgmpCacheAddressEx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 4, 1, 1),
    _IgmpCacheAddressEx_Type()
)
igmpCacheAddressEx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpCacheAddressEx.setStatus("current")
_IgmpCacheIfIdxEx_Type = Integer32
_IgmpCacheIfIdxEx_Object = MibTableColumn
igmpCacheIfIdxEx = _IgmpCacheIfIdxEx_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 4, 1, 2),
    _IgmpCacheIfIdxEx_Type()
)
igmpCacheIfIdxEx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    igmpCacheIfIdxEx.setStatus("current")
_IgmpCacheVersion2HostTimer_Type = TimeTicks
_IgmpCacheVersion2HostTimer_Object = MibTableColumn
igmpCacheVersion2HostTimer = _IgmpCacheVersion2HostTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 4, 1, 3),
    _IgmpCacheVersion2HostTimer_Type()
)
igmpCacheVersion2HostTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheVersion2HostTimer.setStatus("current")
_IgmpCacheFilterMode_Type = FilterMode
_IgmpCacheFilterMode_Object = MibTableColumn
igmpCacheFilterMode = _IgmpCacheFilterMode_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 4, 1, 4),
    _IgmpCacheFilterMode_Type()
)
igmpCacheFilterMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpCacheFilterMode.setStatus("current")
_IgmpSrcInfoTable_Object = MibTable
igmpSrcInfoTable = _IgmpSrcInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 5)
)
if mibBuilder.loadTexts:
    igmpSrcInfoTable.setStatus("current")
_IgmpSrcInfoEntry_Object = MibTableRow
igmpSrcInfoEntry = _IgmpSrcInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 5, 1)
)
igmpSrcInfoEntry.setIndexNames(
    (0, "QTECH-L3Igmp-MIB", "igmpCacheAddressEx"),
    (0, "QTECH-L3Igmp-MIB", "igmpCacheIfIdxEx"),
    (0, "QTECH-L3Igmp-MIB", "igmpSrcAddress"),
)
if mibBuilder.loadTexts:
    igmpSrcInfoEntry.setStatus("current")
_IgmpSrcAddress_Type = IpAddress
_IgmpSrcAddress_Object = MibTableColumn
igmpSrcAddress = _IgmpSrcAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 5, 1, 1),
    _IgmpSrcAddress_Type()
)
igmpSrcAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSrcAddress.setStatus("current")
_IgmpSrcTimer_Type = TimeTicks
_IgmpSrcTimer_Object = MibTableColumn
igmpSrcTimer = _IgmpSrcTimer_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 5, 1, 2),
    _IgmpSrcTimer_Type()
)
igmpSrcTimer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    igmpSrcTimer.setStatus("current")
_IgmpSrcInfoStatus_Type = RowStatus
_IgmpSrcInfoStatus_Object = MibTableColumn
igmpSrcInfoStatus = _IgmpSrcInfoStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 2, 5, 7, 5, 1, 3),
    _IgmpSrcInfoStatus_Type()
)
igmpSrcInfoStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    igmpSrcInfoStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-L3Igmp-MIB",
    **{"PortList": PortList,
       "FilterMode": FilterMode,
       "gbnL3IgmpMib": gbnL3IgmpMib,
       "gbnL3IgmpProxyGroup": gbnL3IgmpProxyGroup,
       "igmpProxyEnable": igmpProxyEnable,
       "igmpProxyIfIndex": igmpProxyIfIndex,
       "igmpGrpNum": igmpGrpNum,
       "igmpGrpMembNum": igmpGrpMembNum,
       "igmpIfExTable": igmpIfExTable,
       "igmpIfExEntry": igmpIfExEntry,
       "igmpifIndex": igmpifIndex,
       "igmpIfPortList": igmpIfPortList,
       "igmpifAccessNum": igmpifAccessNum,
       "igmpifQuerierExpire": igmpifQuerierExpire,
       "igmpifV2QuerierTimer": igmpifV2QuerierTimer,
       "igmpifLimiGroupNum": igmpifLimiGroupNum,
       "igmpGroupVlanTable": igmpGroupVlanTable,
       "igmpGroupVlanEntry": igmpGroupVlanEntry,
       "igmpGroupIP": igmpGroupIP,
       "igmpVlanID": igmpVlanID,
       "igmpGroupVlanStatus": igmpGroupVlanStatus,
       "igmpCacheTableEx": igmpCacheTableEx,
       "igmpCacheExEntry": igmpCacheExEntry,
       "igmpCacheAddressEx": igmpCacheAddressEx,
       "igmpCacheIfIdxEx": igmpCacheIfIdxEx,
       "igmpCacheVersion2HostTimer": igmpCacheVersion2HostTimer,
       "igmpCacheFilterMode": igmpCacheFilterMode,
       "igmpSrcInfoTable": igmpSrcInfoTable,
       "igmpSrcInfoEntry": igmpSrcInfoEntry,
       "igmpSrcAddress": igmpSrcAddress,
       "igmpSrcTimer": igmpSrcTimer,
       "igmpSrcInfoStatus": igmpSrcInfoStatus}
)
