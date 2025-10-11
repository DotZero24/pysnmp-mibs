# SNMP MIB module (NETFLOW-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/bdcom/NETFLOW-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:05:16 2025
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

(InetAddress,
 InetAddressType,
 InetPortNumber) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType",
    "InetPortNumber")

(nmsMgmt,) = mibBuilder.importSymbols(
    "NMS-SMI",
    "nmsMgmt")

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

netflowMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226)
)
if mibBuilder.loadTexts:
    netflowMIB.setRevisions(
        ("2012-03-19 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class NetflowInterfaceDirectionTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("interfaceDirNone", 0),
          ("interfaceDirIngress", 1),
          ("interfaceDirEgress", 2),
          ("interfaceDirBoth", 3))
    )



class NetflowAggregationtypes(TextualConvention, Integer32):
    status = "current"
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
              8,
              9,
              10,
              11,
              12)
        )
    )
    namedValues = NamedValues(
        *(("main", 0),
          ("as", 1),
          ("protocolPort", 2),
          ("sourcePrefix", 3),
          ("destinationPrefix", 4),
          ("prefix", 5),
          ("asTos", 6),
          ("protocolPortTos", 7),
          ("sourcePrefixTos", 8),
          ("destinationPrefixTos", 9),
          ("prefixTos", 10),
          ("prefixPort", 11),
          ("bgpNexthopTos", 12))
    )



class NetflowVersionType(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              5,
              9)
        )
    )
    namedValues = NamedValues(
        *(("version1", 1),
          ("version5", 5),
          ("version9", 9))
    )



class NetflowTemplateTypes(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("template", 1),
          ("optionTemplate", 2))
    )



# MIB Managed Objects in the order of their OIDs

_NetflowMIBObjects_ObjectIdentity = ObjectIdentity
netflowMIBObjects = _NetflowMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1)
)
_NetflowCacheInfo_ObjectIdentity = ObjectIdentity
netflowCacheInfo = _NetflowCacheInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1)
)
_NetflowInterfaceTable_Object = MibTable
netflowInterfaceTable = _NetflowInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 1)
)
if mibBuilder.loadTexts:
    netflowInterfaceTable.setStatus("current")
_NetflowInterfaceEntry_Object = MibTableRow
netflowInterfaceEntry = _NetflowInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 1, 1)
)
netflowInterfaceEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    netflowInterfaceEntry.setStatus("current")
_NetflowCacheNetflowEnable_Type = NetflowInterfaceDirectionTypes
_NetflowCacheNetflowEnable_Object = MibTableColumn
netflowCacheNetflowEnable = _NetflowCacheNetflowEnable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 1, 1, 1),
    _NetflowCacheNetflowEnable_Type()
)
netflowCacheNetflowEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowCacheNetflowEnable.setStatus("current")
_NetflowCacheTable_Object = MibTable
netflowCacheTable = _NetflowCacheTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 2)
)
if mibBuilder.loadTexts:
    netflowCacheTable.setStatus("current")
_NetflowCacheEntry_Object = MibTableRow
netflowCacheEntry = _NetflowCacheEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 2, 1)
)
netflowCacheEntry.setIndexNames(
    (0, "NETFLOW-MIB", "netflowCacheType"),
)
if mibBuilder.loadTexts:
    netflowCacheEntry.setStatus("current")
_NetflowCacheType_Type = NetflowAggregationtypes
_NetflowCacheType_Object = MibTableColumn
netflowCacheType = _NetflowCacheType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 2, 1, 1),
    _NetflowCacheType_Type()
)
netflowCacheType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netflowCacheType.setStatus("current")
_NetflowCacheEnable_Type = TruthValue
_NetflowCacheEnable_Object = MibTableColumn
netflowCacheEnable = _NetflowCacheEnable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 2, 1, 2),
    _NetflowCacheEnable_Type()
)
netflowCacheEnable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowCacheEnable.setStatus("current")
_NetflowCacheEntries_Type = Unsigned32
_NetflowCacheEntries_Object = MibTableColumn
netflowCacheEntries = _NetflowCacheEntries_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 2, 1, 3),
    _NetflowCacheEntries_Type()
)
netflowCacheEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowCacheEntries.setStatus("current")
_NetflowUsedEntries_Type = Unsigned32
_NetflowUsedEntries_Object = MibTableColumn
netflowUsedEntries = _NetflowUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 2, 1, 4),
    _NetflowUsedEntries_Type()
)
netflowUsedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowUsedEntries.setStatus("current")
_NetflowUnUsedEntries_Type = Unsigned32
_NetflowUnUsedEntries_Object = MibTableColumn
netflowUnUsedEntries = _NetflowUnUsedEntries_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 2, 1, 5),
    _NetflowUnUsedEntries_Type()
)
netflowUnUsedEntries.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowUnUsedEntries.setStatus("current")
_NetflowActiveTimeOut_Type = Unsigned32
_NetflowActiveTimeOut_Object = MibTableColumn
netflowActiveTimeOut = _NetflowActiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 2, 1, 6),
    _NetflowActiveTimeOut_Type()
)
netflowActiveTimeOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowActiveTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    netflowActiveTimeOut.setUnits("minutes")
_NetflowInactiveTimeOut_Type = Unsigned32
_NetflowInactiveTimeOut_Object = MibTableColumn
netflowInactiveTimeOut = _NetflowInactiveTimeOut_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 1, 2, 1, 7),
    _NetflowInactiveTimeOut_Type()
)
netflowInactiveTimeOut.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowInactiveTimeOut.setStatus("current")
if mibBuilder.loadTexts:
    netflowInactiveTimeOut.setUnits("seconds")
_NetflowCollectorInfo_ObjectIdentity = ObjectIdentity
netflowCollectorInfo = _NetflowCollectorInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2)
)
_NetflowCollectorVersionInfoTable_Object = MibTable
netflowCollectorVersionInfoTable = _NetflowCollectorVersionInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2, 1)
)
if mibBuilder.loadTexts:
    netflowCollectorVersionInfoTable.setStatus("current")
_NetflowCollectorVersionInfoEntry_Object = MibTableRow
netflowCollectorVersionInfoEntry = _NetflowCollectorVersionInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2, 1, 1)
)
netflowCollectorVersionInfoEntry.setIndexNames(
    (0, "NETFLOW-MIB", "netflowCacheType"),
)
if mibBuilder.loadTexts:
    netflowCollectorVersionInfoEntry.setStatus("current")
_NetflowExportVersion_Type = NetflowVersionType
_NetflowExportVersion_Object = MibTableColumn
netflowExportVersion = _NetflowExportVersion_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2, 1, 1, 1),
    _NetflowExportVersion_Type()
)
netflowExportVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowExportVersion.setStatus("current")
_NetflowMaxCollectors_Type = Unsigned32
_NetflowMaxCollectors_Object = MibScalar
netflowMaxCollectors = _NetflowMaxCollectors_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2, 2),
    _NetflowMaxCollectors_Type()
)
netflowMaxCollectors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowMaxCollectors.setStatus("current")
_NetflowCollectorTable_Object = MibTable
netflowCollectorTable = _NetflowCollectorTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2, 3)
)
if mibBuilder.loadTexts:
    netflowCollectorTable.setStatus("current")
_NetflowCollectorEntry_Object = MibTableRow
netflowCollectorEntry = _NetflowCollectorEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2, 3, 1)
)
netflowCollectorEntry.setIndexNames(
    (0, "NETFLOW-MIB", "netflowCacheType"),
)
if mibBuilder.loadTexts:
    netflowCollectorEntry.setStatus("current")
_NetflowCollectorAddressType_Type = InetAddressType
_NetflowCollectorAddressType_Object = MibTableColumn
netflowCollectorAddressType = _NetflowCollectorAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2, 3, 1, 1),
    _NetflowCollectorAddressType_Type()
)
netflowCollectorAddressType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowCollectorAddressType.setStatus("current")
_NetflowCollectorAddress_Type = InetAddress
_NetflowCollectorAddress_Object = MibTableColumn
netflowCollectorAddress = _NetflowCollectorAddress_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2, 3, 1, 2),
    _NetflowCollectorAddress_Type()
)
netflowCollectorAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowCollectorAddress.setStatus("current")
_NetflowCollectorPort_Type = InetPortNumber
_NetflowCollectorPort_Object = MibTableColumn
netflowCollectorPort = _NetflowCollectorPort_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2, 3, 1, 3),
    _NetflowCollectorPort_Type()
)
netflowCollectorPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowCollectorPort.setStatus("current")
_NetflowCollectorStatus_Type = RowStatus
_NetflowCollectorStatus_Object = MibTableColumn
netflowCollectorStatus = _NetflowCollectorStatus_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 2, 3, 1, 4),
    _NetflowCollectorStatus_Type()
)
netflowCollectorStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    netflowCollectorStatus.setStatus("current")
_NetflowExportStatistics_ObjectIdentity = ObjectIdentity
netflowExportStatistics = _NetflowExportStatistics_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 3)
)
_NetflowOctetsExport_Type = Counter32
_NetflowOctetsExport_Object = MibScalar
netflowOctetsExport = _NetflowOctetsExport_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 3, 1),
    _NetflowOctetsExport_Type()
)
netflowOctetsExport.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowOctetsExport.setStatus("current")
_NetflowRecordsExported_Type = Counter32
_NetflowRecordsExported_Object = MibScalar
netflowRecordsExported = _NetflowRecordsExported_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 3, 2),
    _NetflowRecordsExported_Type()
)
netflowRecordsExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowRecordsExported.setStatus("current")
_NetflowPktsExported_Type = Counter32
_NetflowPktsExported_Object = MibScalar
netflowPktsExported = _NetflowPktsExported_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 3, 3),
    _NetflowPktsExported_Type()
)
netflowPktsExported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowPktsExported.setStatus("current")
_NetflowPktsFailed_Type = Counter32
_NetflowPktsFailed_Object = MibScalar
netflowPktsFailed = _NetflowPktsFailed_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 3, 4),
    _NetflowPktsFailed_Type()
)
netflowPktsFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowPktsFailed.setStatus("current")
_NetflowTemplateInfo_ObjectIdentity = ObjectIdentity
netflowTemplateInfo = _NetflowTemplateInfo_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4)
)
_NetflowTemplateOptionsFlag_Type = TruthValue
_NetflowTemplateOptionsFlag_Object = MibScalar
netflowTemplateOptionsFlag = _NetflowTemplateOptionsFlag_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 1),
    _NetflowTemplateOptionsFlag_Type()
)
netflowTemplateOptionsFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowTemplateOptionsFlag.setStatus("current")
_NetflowTemplateTable_Object = MibTable
netflowTemplateTable = _NetflowTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 2)
)
if mibBuilder.loadTexts:
    netflowTemplateTable.setStatus("current")
_NetflowTemplateEntry_Object = MibTableRow
netflowTemplateEntry = _NetflowTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 2, 1)
)
netflowTemplateEntry.setIndexNames(
    (0, "NETFLOW-MIB", "netflowTemplateType"),
)
if mibBuilder.loadTexts:
    netflowTemplateEntry.setStatus("current")
_NetflowTemplateType_Type = NetflowTemplateTypes
_NetflowTemplateType_Object = MibTableColumn
netflowTemplateType = _NetflowTemplateType_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 2, 1, 1),
    _NetflowTemplateType_Type()
)
netflowTemplateType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    netflowTemplateType.setStatus("current")
_NetflowTemplateAdded_Type = Unsigned32
_NetflowTemplateAdded_Object = MibTableColumn
netflowTemplateAdded = _NetflowTemplateAdded_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 2, 1, 2),
    _NetflowTemplateAdded_Type()
)
netflowTemplateAdded.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowTemplateAdded.setStatus("current")
_NetflowTemplateActive_Type = Unsigned32
_NetflowTemplateActive_Object = MibTableColumn
netflowTemplateActive = _NetflowTemplateActive_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 2, 1, 3),
    _NetflowTemplateActive_Type()
)
netflowTemplateActive.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowTemplateActive.setStatus("current")
_NetflowTemplateAgerPolls_Type = Unsigned32
_NetflowTemplateAgerPolls_Object = MibTableColumn
netflowTemplateAgerPolls = _NetflowTemplateAgerPolls_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 2, 1, 4),
    _NetflowTemplateAgerPolls_Type()
)
netflowTemplateAgerPolls.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowTemplateAgerPolls.setStatus("current")
_NetflowTemplateExportInfoTable_Object = MibTable
netflowTemplateExportInfoTable = _NetflowTemplateExportInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 3)
)
if mibBuilder.loadTexts:
    netflowTemplateExportInfoTable.setStatus("current")
_NetflowTemplateExportInfoEntry_Object = MibTableRow
netflowTemplateExportInfoEntry = _NetflowTemplateExportInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 3, 1)
)
netflowTemplateExportInfoEntry.setIndexNames(
    (0, "NETFLOW-MIB", "netflowCacheType"),
)
if mibBuilder.loadTexts:
    netflowTemplateExportInfoEntry.setStatus("current")
_NetflowTemplateExportVer9Enable_Type = TruthValue
_NetflowTemplateExportVer9Enable_Object = MibTableColumn
netflowTemplateExportVer9Enable = _NetflowTemplateExportVer9Enable_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 3, 1, 1),
    _NetflowTemplateExportVer9Enable_Type()
)
netflowTemplateExportVer9Enable.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    netflowTemplateExportVer9Enable.setStatus("current")
_NetflowTemplateExportVer9TplTimeout_Type = Unsigned32
_NetflowTemplateExportVer9TplTimeout_Object = MibTableColumn
netflowTemplateExportVer9TplTimeout = _NetflowTemplateExportVer9TplTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 3, 1, 2),
    _NetflowTemplateExportVer9TplTimeout_Type()
)
netflowTemplateExportVer9TplTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowTemplateExportVer9TplTimeout.setStatus("current")
if mibBuilder.loadTexts:
    netflowTemplateExportVer9TplTimeout.setUnits("minutes")
_NetflowTemplateExportVer9OptTimeout_Type = Unsigned32
_NetflowTemplateExportVer9OptTimeout_Object = MibTableColumn
netflowTemplateExportVer9OptTimeout = _NetflowTemplateExportVer9OptTimeout_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 3, 1, 3),
    _NetflowTemplateExportVer9OptTimeout_Type()
)
netflowTemplateExportVer9OptTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowTemplateExportVer9OptTimeout.setStatus("current")
if mibBuilder.loadTexts:
    netflowTemplateExportVer9OptTimeout.setUnits("minutes")
_NetflowTemplateExportVer9TplRefreshRate_Type = Unsigned32
_NetflowTemplateExportVer9TplRefreshRate_Object = MibTableColumn
netflowTemplateExportVer9TplRefreshRate = _NetflowTemplateExportVer9TplRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 3, 1, 4),
    _NetflowTemplateExportVer9TplRefreshRate_Type()
)
netflowTemplateExportVer9TplRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowTemplateExportVer9TplRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    netflowTemplateExportVer9TplRefreshRate.setUnits("packets")
_NetflowTemplateExportVer9OptRefreshRate_Type = Unsigned32
_NetflowTemplateExportVer9OptRefreshRate_Object = MibTableColumn
netflowTemplateExportVer9OptRefreshRate = _NetflowTemplateExportVer9OptRefreshRate_Object(
    (1, 3, 6, 1, 4, 1, 3320, 9, 226, 1, 4, 3, 1, 5),
    _NetflowTemplateExportVer9OptRefreshRate_Type()
)
netflowTemplateExportVer9OptRefreshRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    netflowTemplateExportVer9OptRefreshRate.setStatus("current")
if mibBuilder.loadTexts:
    netflowTemplateExportVer9OptRefreshRate.setUnits("packets")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NETFLOW-MIB",
    **{"NetflowInterfaceDirectionTypes": NetflowInterfaceDirectionTypes,
       "NetflowAggregationtypes": NetflowAggregationtypes,
       "NetflowVersionType": NetflowVersionType,
       "NetflowTemplateTypes": NetflowTemplateTypes,
       "netflowMIB": netflowMIB,
       "netflowMIBObjects": netflowMIBObjects,
       "netflowCacheInfo": netflowCacheInfo,
       "netflowInterfaceTable": netflowInterfaceTable,
       "netflowInterfaceEntry": netflowInterfaceEntry,
       "netflowCacheNetflowEnable": netflowCacheNetflowEnable,
       "netflowCacheTable": netflowCacheTable,
       "netflowCacheEntry": netflowCacheEntry,
       "netflowCacheType": netflowCacheType,
       "netflowCacheEnable": netflowCacheEnable,
       "netflowCacheEntries": netflowCacheEntries,
       "netflowUsedEntries": netflowUsedEntries,
       "netflowUnUsedEntries": netflowUnUsedEntries,
       "netflowActiveTimeOut": netflowActiveTimeOut,
       "netflowInactiveTimeOut": netflowInactiveTimeOut,
       "netflowCollectorInfo": netflowCollectorInfo,
       "netflowCollectorVersionInfoTable": netflowCollectorVersionInfoTable,
       "netflowCollectorVersionInfoEntry": netflowCollectorVersionInfoEntry,
       "netflowExportVersion": netflowExportVersion,
       "netflowMaxCollectors": netflowMaxCollectors,
       "netflowCollectorTable": netflowCollectorTable,
       "netflowCollectorEntry": netflowCollectorEntry,
       "netflowCollectorAddressType": netflowCollectorAddressType,
       "netflowCollectorAddress": netflowCollectorAddress,
       "netflowCollectorPort": netflowCollectorPort,
       "netflowCollectorStatus": netflowCollectorStatus,
       "netflowExportStatistics": netflowExportStatistics,
       "netflowOctetsExport": netflowOctetsExport,
       "netflowRecordsExported": netflowRecordsExported,
       "netflowPktsExported": netflowPktsExported,
       "netflowPktsFailed": netflowPktsFailed,
       "netflowTemplateInfo": netflowTemplateInfo,
       "netflowTemplateOptionsFlag": netflowTemplateOptionsFlag,
       "netflowTemplateTable": netflowTemplateTable,
       "netflowTemplateEntry": netflowTemplateEntry,
       "netflowTemplateType": netflowTemplateType,
       "netflowTemplateAdded": netflowTemplateAdded,
       "netflowTemplateActive": netflowTemplateActive,
       "netflowTemplateAgerPolls": netflowTemplateAgerPolls,
       "netflowTemplateExportInfoTable": netflowTemplateExportInfoTable,
       "netflowTemplateExportInfoEntry": netflowTemplateExportInfoEntry,
       "netflowTemplateExportVer9Enable": netflowTemplateExportVer9Enable,
       "netflowTemplateExportVer9TplTimeout": netflowTemplateExportVer9TplTimeout,
       "netflowTemplateExportVer9OptTimeout": netflowTemplateExportVer9OptTimeout,
       "netflowTemplateExportVer9TplRefreshRate": netflowTemplateExportVer9TplRefreshRate,
       "netflowTemplateExportVer9OptRefreshRate": netflowTemplateExportVer9OptRefreshRate}
)
