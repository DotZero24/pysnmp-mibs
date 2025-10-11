# SNMP MIB module (TIMETRA-BIER-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TIMETRA-BIER-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:55:19 2025
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

(InetAddress,
 InetAddressType) = mibBuilder.importSymbols(
    "INET-ADDRESS-MIB",
    "InetAddress",
    "InetAddressType")

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
 TimeStamp,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp",
    "TruthValue")

(timetraSRMIBModules,
 tmnxSRConfs,
 tmnxSRNotifyPrefix,
 tmnxSRObjs) = mibBuilder.importSymbols(
    "TIMETRA-GLOBAL-MIB",
    "timetraSRMIBModules",
    "tmnxSRConfs",
    "tmnxSRNotifyPrefix",
    "tmnxSRObjs")

(TNamedItem,
 TmnxAdminState,
 TmnxLongDisplayString,
 TmnxOperState) = mibBuilder.importSymbols(
    "TIMETRA-TC-MIB",
    "TNamedItem",
    "TmnxAdminState",
    "TmnxLongDisplayString",
    "TmnxOperState")

(vRtrID,
 vRtrIfIndex) = mibBuilder.importSymbols(
    "TIMETRA-VRTR-MIB",
    "vRtrID",
    "vRtrIfIndex")


# MODULE-IDENTITY

timetraBierMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 1, 1, 3, 123)
)
if mibBuilder.loadTexts:
    timetraBierMIBModule.setRevisions(
        ("2018-01-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TmnxBierMultiTopology(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("ipv4-unicast", 0),
          ("ipv6-unicast", 2),
          ("ipv4-multicast", 3),
          ("ipv6-multicast", 4))
    )



# MIB Managed Objects in the order of their OIDs

_TmnxBierConformance_ObjectIdentity = ObjectIdentity
tmnxBierConformance = _TmnxBierConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 123)
)
_TmnxBierCompliances_ObjectIdentity = ObjectIdentity
tmnxBierCompliances = _TmnxBierCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 123, 1)
)
_TmnxBierGroups_ObjectIdentity = ObjectIdentity
tmnxBierGroups = _TmnxBierGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 123, 2)
)
_TmnxBierObjs_ObjectIdentity = ObjectIdentity
tmnxBierObjs = _TmnxBierObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123)
)
_VRtrBierGeneralTableLastChanged_Type = TimeStamp
_VRtrBierGeneralTableLastChanged_Object = MibScalar
vRtrBierGeneralTableLastChanged = _VRtrBierGeneralTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 1),
    _VRtrBierGeneralTableLastChanged_Type()
)
vRtrBierGeneralTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierGeneralTableLastChanged.setStatus("current")
_VRtrBierGeneralTable_Object = MibTable
vRtrBierGeneralTable = _VRtrBierGeneralTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 2)
)
if mibBuilder.loadTexts:
    vRtrBierGeneralTable.setStatus("current")
_VRtrBierGeneralEntry_Object = MibTableRow
vRtrBierGeneralEntry = _VRtrBierGeneralEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 2, 1)
)
vRtrBierGeneralEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrBierGeneralEntry.setStatus("current")
_VRtrBierGeneralRowStatus_Type = RowStatus
_VRtrBierGeneralRowStatus_Object = MibTableColumn
vRtrBierGeneralRowStatus = _VRtrBierGeneralRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 2, 1, 1),
    _VRtrBierGeneralRowStatus_Type()
)
vRtrBierGeneralRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBierGeneralRowStatus.setStatus("current")


class _VRtrBierGeneralAdminState_Type(TmnxAdminState):
    """Custom type vRtrBierGeneralAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrBierGeneralAdminState_Type.__name__ = "TmnxAdminState"
_VRtrBierGeneralAdminState_Object = MibTableColumn
vRtrBierGeneralAdminState = _VRtrBierGeneralAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 2, 1, 2),
    _VRtrBierGeneralAdminState_Type()
)
vRtrBierGeneralAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBierGeneralAdminState.setStatus("current")
_VRtrBierGeneralRowLastChange_Type = TimeStamp
_VRtrBierGeneralRowLastChange_Object = MibTableColumn
vRtrBierGeneralRowLastChange = _VRtrBierGeneralRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 2, 1, 3),
    _VRtrBierGeneralRowLastChange_Type()
)
vRtrBierGeneralRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierGeneralRowLastChange.setStatus("current")
_VRtrBierTemplateTableLastChanged_Type = TimeStamp
_VRtrBierTemplateTableLastChanged_Object = MibScalar
vRtrBierTemplateTableLastChanged = _VRtrBierTemplateTableLastChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 3),
    _VRtrBierTemplateTableLastChanged_Type()
)
vRtrBierTemplateTableLastChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTemplateTableLastChanged.setStatus("current")
_VRtrBierTemplateTable_Object = MibTable
vRtrBierTemplateTable = _VRtrBierTemplateTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 4)
)
if mibBuilder.loadTexts:
    vRtrBierTemplateTable.setStatus("current")
_VRtrBierTemplateEntry_Object = MibTableRow
vRtrBierTemplateEntry = _VRtrBierTemplateEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 4, 1)
)
vRtrBierTemplateEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierTemplateName"),
)
if mibBuilder.loadTexts:
    vRtrBierTemplateEntry.setStatus("current")
_VRtrBierTemplateName_Type = TNamedItem
_VRtrBierTemplateName_Object = MibTableColumn
vRtrBierTemplateName = _VRtrBierTemplateName_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 4, 1, 1),
    _VRtrBierTemplateName_Type()
)
vRtrBierTemplateName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierTemplateName.setStatus("current")
_VRtrBierTemplateRowStatus_Type = RowStatus
_VRtrBierTemplateRowStatus_Object = MibTableColumn
vRtrBierTemplateRowStatus = _VRtrBierTemplateRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 4, 1, 2),
    _VRtrBierTemplateRowStatus_Type()
)
vRtrBierTemplateRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBierTemplateRowStatus.setStatus("current")


class _VRtrBierTemplateAdminState_Type(TmnxAdminState):
    """Custom type vRtrBierTemplateAdminState based on TmnxAdminState"""
    defaultValue = 3


_VRtrBierTemplateAdminState_Type.__name__ = "TmnxAdminState"
_VRtrBierTemplateAdminState_Object = MibTableColumn
vRtrBierTemplateAdminState = _VRtrBierTemplateAdminState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 4, 1, 3),
    _VRtrBierTemplateAdminState_Type()
)
vRtrBierTemplateAdminState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBierTemplateAdminState.setStatus("current")
_VRtrBierTemplateRowLastChange_Type = TimeStamp
_VRtrBierTemplateRowLastChange_Object = MibTableColumn
vRtrBierTemplateRowLastChange = _VRtrBierTemplateRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 4, 1, 4),
    _VRtrBierTemplateRowLastChange_Type()
)
vRtrBierTemplateRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTemplateRowLastChange.setStatus("current")
_VRtrBierSubDomainTableLstChanged_Type = TimeStamp
_VRtrBierSubDomainTableLstChanged_Object = MibScalar
vRtrBierSubDomainTableLstChanged = _VRtrBierSubDomainTableLstChanged_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 5),
    _VRtrBierSubDomainTableLstChanged_Type()
)
vRtrBierSubDomainTableLstChanged.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierSubDomainTableLstChanged.setStatus("current")
_VRtrBierSubDomainTable_Object = MibTable
vRtrBierSubDomainTable = _VRtrBierSubDomainTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 6)
)
if mibBuilder.loadTexts:
    vRtrBierSubDomainTable.setStatus("current")
_VRtrBierSubDomainEntry_Object = MibTableRow
vRtrBierSubDomainEntry = _VRtrBierSubDomainEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 6, 1)
)
vRtrBierSubDomainEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierTemplateName"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierSubDomainStart"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierSubDomainEnd"),
)
if mibBuilder.loadTexts:
    vRtrBierSubDomainEntry.setStatus("current")


class _VRtrBierSubDomainStart_Type(Unsigned32):
    """Custom type vRtrBierSubDomainStart based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrBierSubDomainStart_Type.__name__ = "Unsigned32"
_VRtrBierSubDomainStart_Object = MibTableColumn
vRtrBierSubDomainStart = _VRtrBierSubDomainStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 6, 1, 1),
    _VRtrBierSubDomainStart_Type()
)
vRtrBierSubDomainStart.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierSubDomainStart.setStatus("current")


class _VRtrBierSubDomainEnd_Type(Unsigned32):
    """Custom type vRtrBierSubDomainEnd based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_VRtrBierSubDomainEnd_Type.__name__ = "Unsigned32"
_VRtrBierSubDomainEnd_Object = MibTableColumn
vRtrBierSubDomainEnd = _VRtrBierSubDomainEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 6, 1, 2),
    _VRtrBierSubDomainEnd_Type()
)
vRtrBierSubDomainEnd.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierSubDomainEnd.setStatus("current")


class _VRtrBierSubDomainPrefixType_Type(InetAddressType):
    """Custom type vRtrBierSubDomainPrefixType based on InetAddressType"""
    defaultValue = 0


_VRtrBierSubDomainPrefixType_Type.__name__ = "InetAddressType"
_VRtrBierSubDomainPrefixType_Object = MibTableColumn
vRtrBierSubDomainPrefixType = _VRtrBierSubDomainPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 6, 1, 3),
    _VRtrBierSubDomainPrefixType_Type()
)
vRtrBierSubDomainPrefixType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBierSubDomainPrefixType.setStatus("current")


class _VRtrBierSubDomainPrefix_Type(InetAddress):
    """Custom type vRtrBierSubDomainPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierSubDomainPrefix_Type.__name__ = "InetAddress"
_VRtrBierSubDomainPrefix_Object = MibTableColumn
vRtrBierSubDomainPrefix = _VRtrBierSubDomainPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 6, 1, 4),
    _VRtrBierSubDomainPrefix_Type()
)
vRtrBierSubDomainPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBierSubDomainPrefix.setStatus("current")


class _VRtrBierSubDomainBfrId_Type(Unsigned32):
    """Custom type vRtrBierSubDomainBfrId based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_VRtrBierSubDomainBfrId_Type.__name__ = "Unsigned32"
_VRtrBierSubDomainBfrId_Object = MibTableColumn
vRtrBierSubDomainBfrId = _VRtrBierSubDomainBfrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 6, 1, 5),
    _VRtrBierSubDomainBfrId_Type()
)
vRtrBierSubDomainBfrId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBierSubDomainBfrId.setStatus("current")


class _VRtrBierSubDomainMT_Type(TmnxBierMultiTopology):
    """Custom type vRtrBierSubDomainMT based on TmnxBierMultiTopology"""
    defaultValue = 0


_VRtrBierSubDomainMT_Type.__name__ = "TmnxBierMultiTopology"
_VRtrBierSubDomainMT_Object = MibTableColumn
vRtrBierSubDomainMT = _VRtrBierSubDomainMT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 6, 1, 6),
    _VRtrBierSubDomainMT_Type()
)
vRtrBierSubDomainMT.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBierSubDomainMT.setStatus("current")
_VRtrBierSubDomainRowStatus_Type = RowStatus
_VRtrBierSubDomainRowStatus_Object = MibTableColumn
vRtrBierSubDomainRowStatus = _VRtrBierSubDomainRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 6, 1, 7),
    _VRtrBierSubDomainRowStatus_Type()
)
vRtrBierSubDomainRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    vRtrBierSubDomainRowStatus.setStatus("current")
_VRtrBierSubDomainRowLastChange_Type = TimeStamp
_VRtrBierSubDomainRowLastChange_Object = MibTableColumn
vRtrBierSubDomainRowLastChange = _VRtrBierSubDomainRowLastChange_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 6, 1, 8),
    _VRtrBierSubDomainRowLastChange_Type()
)
vRtrBierSubDomainRowLastChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierSubDomainRowLastChange.setStatus("current")
_VRtrBierDatabaseTable_Object = MibTable
vRtrBierDatabaseTable = _VRtrBierDatabaseTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7)
)
if mibBuilder.loadTexts:
    vRtrBierDatabaseTable.setStatus("current")
_VRtrBierDatabaseEntry_Object = MibTableRow
vRtrBierDatabaseEntry = _VRtrBierDatabaseEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7, 1)
)
vRtrBierDatabaseEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierTemplateName"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierDatabaseSubDomainId"),
)
if mibBuilder.loadTexts:
    vRtrBierDatabaseEntry.setStatus("current")
_VRtrBierDatabaseSubDomainId_Type = Unsigned32
_VRtrBierDatabaseSubDomainId_Object = MibTableColumn
vRtrBierDatabaseSubDomainId = _VRtrBierDatabaseSubDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7, 1, 1),
    _VRtrBierDatabaseSubDomainId_Type()
)
vRtrBierDatabaseSubDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierDatabaseSubDomainId.setStatus("current")
_VRtrBierDatabaseBitStringLen_Type = Unsigned32
_VRtrBierDatabaseBitStringLen_Object = MibTableColumn
vRtrBierDatabaseBitStringLen = _VRtrBierDatabaseBitStringLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7, 1, 2),
    _VRtrBierDatabaseBitStringLen_Type()
)
vRtrBierDatabaseBitStringLen.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierDatabaseBitStringLen.setStatus("current")


class _VRtrBierDatabasePrefixType_Type(InetAddressType):
    """Custom type vRtrBierDatabasePrefixType based on InetAddressType"""
    defaultValue = 0


_VRtrBierDatabasePrefixType_Type.__name__ = "InetAddressType"
_VRtrBierDatabasePrefixType_Object = MibTableColumn
vRtrBierDatabasePrefixType = _VRtrBierDatabasePrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7, 1, 3),
    _VRtrBierDatabasePrefixType_Type()
)
vRtrBierDatabasePrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierDatabasePrefixType.setStatus("current")


class _VRtrBierDatabasePrefix_Type(InetAddress):
    """Custom type vRtrBierDatabasePrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierDatabasePrefix_Type.__name__ = "InetAddress"
_VRtrBierDatabasePrefix_Object = MibTableColumn
vRtrBierDatabasePrefix = _VRtrBierDatabasePrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7, 1, 4),
    _VRtrBierDatabasePrefix_Type()
)
vRtrBierDatabasePrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierDatabasePrefix.setStatus("current")
_VRtrBierDatabaseBfrId_Type = Unsigned32
_VRtrBierDatabaseBfrId_Object = MibTableColumn
vRtrBierDatabaseBfrId = _VRtrBierDatabaseBfrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7, 1, 5),
    _VRtrBierDatabaseBfrId_Type()
)
vRtrBierDatabaseBfrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierDatabaseBfrId.setStatus("current")
_VRtrBierDatabaseMT_Type = TmnxBierMultiTopology
_VRtrBierDatabaseMT_Object = MibTableColumn
vRtrBierDatabaseMT = _VRtrBierDatabaseMT_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7, 1, 6),
    _VRtrBierDatabaseMT_Type()
)
vRtrBierDatabaseMT.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierDatabaseMT.setStatus("current")
_VRtrBierDatabaseMplsLabelStart_Type = Unsigned32
_VRtrBierDatabaseMplsLabelStart_Object = MibTableColumn
vRtrBierDatabaseMplsLabelStart = _VRtrBierDatabaseMplsLabelStart_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7, 1, 7),
    _VRtrBierDatabaseMplsLabelStart_Type()
)
vRtrBierDatabaseMplsLabelStart.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierDatabaseMplsLabelStart.setStatus("current")
_VRtrBierDatabaseMplsLabelEnd_Type = Unsigned32
_VRtrBierDatabaseMplsLabelEnd_Object = MibTableColumn
vRtrBierDatabaseMplsLabelEnd = _VRtrBierDatabaseMplsLabelEnd_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7, 1, 8),
    _VRtrBierDatabaseMplsLabelEnd_Type()
)
vRtrBierDatabaseMplsLabelEnd.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierDatabaseMplsLabelEnd.setStatus("current")
_VRtrBierDatabaseMplsLabelTotal_Type = Unsigned32
_VRtrBierDatabaseMplsLabelTotal_Object = MibTableColumn
vRtrBierDatabaseMplsLabelTotal = _VRtrBierDatabaseMplsLabelTotal_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 7, 1, 9),
    _VRtrBierDatabaseMplsLabelTotal_Type()
)
vRtrBierDatabaseMplsLabelTotal.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierDatabaseMplsLabelTotal.setStatus("current")
_VRtrBierForwardingTable_Object = MibTable
vRtrBierForwardingTable = _VRtrBierForwardingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8)
)
if mibBuilder.loadTexts:
    vRtrBierForwardingTable.setStatus("current")
_VRtrBierForwardingEntry_Object = MibTableRow
vRtrBierForwardingEntry = _VRtrBierForwardingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1)
)
vRtrBierForwardingEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierForwardingSubDomainId"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierForwardingBitStringLen"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierForwardingNhopPrefixType"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierForwardingNhopPrefix"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierForwardingNhopIfIndex"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierForwardingBierSetId"),
)
if mibBuilder.loadTexts:
    vRtrBierForwardingEntry.setStatus("current")
_VRtrBierForwardingSubDomainId_Type = Unsigned32
_VRtrBierForwardingSubDomainId_Object = MibTableColumn
vRtrBierForwardingSubDomainId = _VRtrBierForwardingSubDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1, 1),
    _VRtrBierForwardingSubDomainId_Type()
)
vRtrBierForwardingSubDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierForwardingSubDomainId.setStatus("current")
_VRtrBierForwardingBitStringLen_Type = Unsigned32
_VRtrBierForwardingBitStringLen_Object = MibTableColumn
vRtrBierForwardingBitStringLen = _VRtrBierForwardingBitStringLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1, 2),
    _VRtrBierForwardingBitStringLen_Type()
)
vRtrBierForwardingBitStringLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierForwardingBitStringLen.setStatus("current")


class _VRtrBierForwardingNhopPrefixType_Type(InetAddressType):
    """Custom type vRtrBierForwardingNhopPrefixType based on InetAddressType"""
    defaultValue = 0


_VRtrBierForwardingNhopPrefixType_Type.__name__ = "InetAddressType"
_VRtrBierForwardingNhopPrefixType_Object = MibTableColumn
vRtrBierForwardingNhopPrefixType = _VRtrBierForwardingNhopPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1, 3),
    _VRtrBierForwardingNhopPrefixType_Type()
)
vRtrBierForwardingNhopPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierForwardingNhopPrefixType.setStatus("current")


class _VRtrBierForwardingNhopPrefix_Type(InetAddress):
    """Custom type vRtrBierForwardingNhopPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierForwardingNhopPrefix_Type.__name__ = "InetAddress"
_VRtrBierForwardingNhopPrefix_Object = MibTableColumn
vRtrBierForwardingNhopPrefix = _VRtrBierForwardingNhopPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1, 4),
    _VRtrBierForwardingNhopPrefix_Type()
)
vRtrBierForwardingNhopPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierForwardingNhopPrefix.setStatus("current")
_VRtrBierForwardingNhopIfIndex_Type = Unsigned32
_VRtrBierForwardingNhopIfIndex_Object = MibTableColumn
vRtrBierForwardingNhopIfIndex = _VRtrBierForwardingNhopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1, 5),
    _VRtrBierForwardingNhopIfIndex_Type()
)
vRtrBierForwardingNhopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierForwardingNhopIfIndex.setStatus("current")
_VRtrBierForwardingBierSetId_Type = Unsigned32
_VRtrBierForwardingBierSetId_Object = MibTableColumn
vRtrBierForwardingBierSetId = _VRtrBierForwardingBierSetId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1, 6),
    _VRtrBierForwardingBierSetId_Type()
)
vRtrBierForwardingBierSetId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierForwardingBierSetId.setStatus("current")
_VRtrBierForwardingNbrPrefixType_Type = InetAddressType
_VRtrBierForwardingNbrPrefixType_Object = MibTableColumn
vRtrBierForwardingNbrPrefixType = _VRtrBierForwardingNbrPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1, 7),
    _VRtrBierForwardingNbrPrefixType_Type()
)
vRtrBierForwardingNbrPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierForwardingNbrPrefixType.setStatus("current")


class _VRtrBierForwardingNbrPrefix_Type(InetAddress):
    """Custom type vRtrBierForwardingNbrPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierForwardingNbrPrefix_Type.__name__ = "InetAddress"
_VRtrBierForwardingNbrPrefix_Object = MibTableColumn
vRtrBierForwardingNbrPrefix = _VRtrBierForwardingNbrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1, 8),
    _VRtrBierForwardingNbrPrefix_Type()
)
vRtrBierForwardingNbrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierForwardingNbrPrefix.setStatus("current")


class _VRtrBierForwardingBitMask_Type(TmnxLongDisplayString):
    """Custom type vRtrBierForwardingBitMask based on TmnxLongDisplayString"""
    subtypeSpec = TmnxLongDisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 256),
    )


_VRtrBierForwardingBitMask_Type.__name__ = "TmnxLongDisplayString"
_VRtrBierForwardingBitMask_Object = MibTableColumn
vRtrBierForwardingBitMask = _VRtrBierForwardingBitMask_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1, 9),
    _VRtrBierForwardingBitMask_Type()
)
vRtrBierForwardingBitMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierForwardingBitMask.setStatus("current")
_VRtrBierForwardingMplsLabel_Type = Unsigned32
_VRtrBierForwardingMplsLabel_Object = MibTableColumn
vRtrBierForwardingMplsLabel = _VRtrBierForwardingMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 8, 1, 10),
    _VRtrBierForwardingMplsLabel_Type()
)
vRtrBierForwardingMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierForwardingMplsLabel.setStatus("current")
_VRtrBierRoutingTable_Object = MibTable
vRtrBierRoutingTable = _VRtrBierRoutingTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9)
)
if mibBuilder.loadTexts:
    vRtrBierRoutingTable.setStatus("current")
_VRtrBierRoutingEntry_Object = MibTableRow
vRtrBierRoutingEntry = _VRtrBierRoutingEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1)
)
vRtrBierRoutingEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierRoutingSubDomainId"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierRoutingBitStringLen"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierRoutingNhopPrefixType"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierRoutingNhopPrefix"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierRoutingNhopIfIndex"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierRoutingDestPrefixType"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierRoutingDestPrefix"),
)
if mibBuilder.loadTexts:
    vRtrBierRoutingEntry.setStatus("current")
_VRtrBierRoutingSubDomainId_Type = Unsigned32
_VRtrBierRoutingSubDomainId_Object = MibTableColumn
vRtrBierRoutingSubDomainId = _VRtrBierRoutingSubDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 1),
    _VRtrBierRoutingSubDomainId_Type()
)
vRtrBierRoutingSubDomainId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierRoutingSubDomainId.setStatus("current")
_VRtrBierRoutingBitStringLen_Type = Unsigned32
_VRtrBierRoutingBitStringLen_Object = MibTableColumn
vRtrBierRoutingBitStringLen = _VRtrBierRoutingBitStringLen_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 2),
    _VRtrBierRoutingBitStringLen_Type()
)
vRtrBierRoutingBitStringLen.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierRoutingBitStringLen.setStatus("current")


class _VRtrBierRoutingNhopPrefixType_Type(InetAddressType):
    """Custom type vRtrBierRoutingNhopPrefixType based on InetAddressType"""
    defaultValue = 0


_VRtrBierRoutingNhopPrefixType_Type.__name__ = "InetAddressType"
_VRtrBierRoutingNhopPrefixType_Object = MibTableColumn
vRtrBierRoutingNhopPrefixType = _VRtrBierRoutingNhopPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 3),
    _VRtrBierRoutingNhopPrefixType_Type()
)
vRtrBierRoutingNhopPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierRoutingNhopPrefixType.setStatus("current")


class _VRtrBierRoutingNhopPrefix_Type(InetAddress):
    """Custom type vRtrBierRoutingNhopPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierRoutingNhopPrefix_Type.__name__ = "InetAddress"
_VRtrBierRoutingNhopPrefix_Object = MibTableColumn
vRtrBierRoutingNhopPrefix = _VRtrBierRoutingNhopPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 4),
    _VRtrBierRoutingNhopPrefix_Type()
)
vRtrBierRoutingNhopPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierRoutingNhopPrefix.setStatus("current")
_VRtrBierRoutingNhopIfIndex_Type = Unsigned32
_VRtrBierRoutingNhopIfIndex_Object = MibTableColumn
vRtrBierRoutingNhopIfIndex = _VRtrBierRoutingNhopIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 5),
    _VRtrBierRoutingNhopIfIndex_Type()
)
vRtrBierRoutingNhopIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierRoutingNhopIfIndex.setStatus("current")


class _VRtrBierRoutingDestPrefixType_Type(InetAddressType):
    """Custom type vRtrBierRoutingDestPrefixType based on InetAddressType"""
    defaultValue = 0


_VRtrBierRoutingDestPrefixType_Type.__name__ = "InetAddressType"
_VRtrBierRoutingDestPrefixType_Object = MibTableColumn
vRtrBierRoutingDestPrefixType = _VRtrBierRoutingDestPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 6),
    _VRtrBierRoutingDestPrefixType_Type()
)
vRtrBierRoutingDestPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierRoutingDestPrefixType.setStatus("current")


class _VRtrBierRoutingDestPrefix_Type(InetAddress):
    """Custom type vRtrBierRoutingDestPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierRoutingDestPrefix_Type.__name__ = "InetAddress"
_VRtrBierRoutingDestPrefix_Object = MibTableColumn
vRtrBierRoutingDestPrefix = _VRtrBierRoutingDestPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 7),
    _VRtrBierRoutingDestPrefix_Type()
)
vRtrBierRoutingDestPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierRoutingDestPrefix.setStatus("current")
_VRtrBierRoutingNbrPrefixType_Type = InetAddressType
_VRtrBierRoutingNbrPrefixType_Object = MibTableColumn
vRtrBierRoutingNbrPrefixType = _VRtrBierRoutingNbrPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 8),
    _VRtrBierRoutingNbrPrefixType_Type()
)
vRtrBierRoutingNbrPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierRoutingNbrPrefixType.setStatus("current")


class _VRtrBierRoutingNbrPrefix_Type(InetAddress):
    """Custom type vRtrBierRoutingNbrPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierRoutingNbrPrefix_Type.__name__ = "InetAddress"
_VRtrBierRoutingNbrPrefix_Object = MibTableColumn
vRtrBierRoutingNbrPrefix = _VRtrBierRoutingNbrPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 9),
    _VRtrBierRoutingNbrPrefix_Type()
)
vRtrBierRoutingNbrPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierRoutingNbrPrefix.setStatus("current")
_VRtrBierRoutingBfrId_Type = Unsigned32
_VRtrBierRoutingBfrId_Object = MibTableColumn
vRtrBierRoutingBfrId = _VRtrBierRoutingBfrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 10),
    _VRtrBierRoutingBfrId_Type()
)
vRtrBierRoutingBfrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierRoutingBfrId.setStatus("current")
_VRtrBierRoutingLastUpdated_Type = TimeStamp
_VRtrBierRoutingLastUpdated_Object = MibTableColumn
vRtrBierRoutingLastUpdated = _VRtrBierRoutingLastUpdated_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 9, 1, 11),
    _VRtrBierRoutingLastUpdated_Type()
)
vRtrBierRoutingLastUpdated.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierRoutingLastUpdated.setStatus("current")
_VRtrBierTunnelTable_Object = MibTable
vRtrBierTunnelTable = _VRtrBierTunnelTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10)
)
if mibBuilder.loadTexts:
    vRtrBierTunnelTable.setStatus("current")
_VRtrBierTunnelEntry_Object = MibTableRow
vRtrBierTunnelEntry = _VRtrBierTunnelEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1)
)
vRtrBierTunnelEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
)
if mibBuilder.loadTexts:
    vRtrBierTunnelEntry.setStatus("current")


class _VRtrBierTunnelType_Type(Integer32):
    """Custom type vRtrBierTunnelType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("tx", 0),
          ("rx", 1))
    )


_VRtrBierTunnelType_Type.__name__ = "Integer32"
_VRtrBierTunnelType_Object = MibTableColumn
vRtrBierTunnelType = _VRtrBierTunnelType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1, 1),
    _VRtrBierTunnelType_Type()
)
vRtrBierTunnelType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTunnelType.setStatus("current")
_VRtrBierTunnelPrefixType_Type = InetAddressType
_VRtrBierTunnelPrefixType_Object = MibTableColumn
vRtrBierTunnelPrefixType = _VRtrBierTunnelPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1, 2),
    _VRtrBierTunnelPrefixType_Type()
)
vRtrBierTunnelPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTunnelPrefixType.setStatus("current")


class _VRtrBierTunnelPrefix_Type(InetAddress):
    """Custom type vRtrBierTunnelPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierTunnelPrefix_Type.__name__ = "InetAddress"
_VRtrBierTunnelPrefix_Object = MibTableColumn
vRtrBierTunnelPrefix = _VRtrBierTunnelPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1, 3),
    _VRtrBierTunnelPrefix_Type()
)
vRtrBierTunnelPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTunnelPrefix.setStatus("current")
_VRtrBierTunnelSubDomain_Type = Unsigned32
_VRtrBierTunnelSubDomain_Object = MibTableColumn
vRtrBierTunnelSubDomain = _VRtrBierTunnelSubDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1, 4),
    _VRtrBierTunnelSubDomain_Type()
)
vRtrBierTunnelSubDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTunnelSubDomain.setStatus("current")
_VRtrBierTunnelMplsLabel_Type = Unsigned32
_VRtrBierTunnelMplsLabel_Object = MibTableColumn
vRtrBierTunnelMplsLabel = _VRtrBierTunnelMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1, 5),
    _VRtrBierTunnelMplsLabel_Type()
)
vRtrBierTunnelMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTunnelMplsLabel.setStatus("current")
_VRtrBierTunnelBfrId_Type = Unsigned32
_VRtrBierTunnelBfrId_Object = MibTableColumn
vRtrBierTunnelBfrId = _VRtrBierTunnelBfrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1, 6),
    _VRtrBierTunnelBfrId_Type()
)
vRtrBierTunnelBfrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTunnelBfrId.setStatus("current")
_VRtrBierTunnelOperState_Type = TmnxAdminState
_VRtrBierTunnelOperState_Object = MibTableColumn
vRtrBierTunnelOperState = _VRtrBierTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1, 7),
    _VRtrBierTunnelOperState_Type()
)
vRtrBierTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTunnelOperState.setStatus("current")
_VRtrBierTunnelNumLeaves_Type = Unsigned32
_VRtrBierTunnelNumLeaves_Object = MibTableColumn
vRtrBierTunnelNumLeaves = _VRtrBierTunnelNumLeaves_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1, 8),
    _VRtrBierTunnelNumLeaves_Type()
)
vRtrBierTunnelNumLeaves.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTunnelNumLeaves.setStatus("current")
_VRtrBierTunnelLastOperDownReason_Type = Unsigned32
_VRtrBierTunnelLastOperDownReason_Object = MibTableColumn
vRtrBierTunnelLastOperDownReason = _VRtrBierTunnelLastOperDownReason_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1, 9),
    _VRtrBierTunnelLastOperDownReason_Type()
)
vRtrBierTunnelLastOperDownReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTunnelLastOperDownReason.setStatus("current")
_VRtrBierTunnelIsInBand_Type = TruthValue
_VRtrBierTunnelIsInBand_Object = MibTableColumn
vRtrBierTunnelIsInBand = _VRtrBierTunnelIsInBand_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 10, 1, 10),
    _VRtrBierTunnelIsInBand_Type()
)
vRtrBierTunnelIsInBand.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTunnelIsInBand.setStatus("current")
_VRtrBierTxTunnelLeafTable_Object = MibTable
vRtrBierTxTunnelLeafTable = _VRtrBierTxTunnelLeafTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11)
)
if mibBuilder.loadTexts:
    vRtrBierTxTunnelLeafTable.setStatus("current")
_VRtrBierTxTunnelLeafEntry_Object = MibTableRow
vRtrBierTxTunnelLeafEntry = _VRtrBierTxTunnelLeafEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1)
)
vRtrBierTxTunnelLeafEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-VRTR-MIB", "vRtrIfIndex"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierTxTunnelLeafPrefixType"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierTxTunnelLeafPrefix"),
)
if mibBuilder.loadTexts:
    vRtrBierTxTunnelLeafEntry.setStatus("current")


class _VRtrBierTxTunnelLeafPrefixType_Type(InetAddressType):
    """Custom type vRtrBierTxTunnelLeafPrefixType based on InetAddressType"""
    defaultValue = 0


_VRtrBierTxTunnelLeafPrefixType_Type.__name__ = "InetAddressType"
_VRtrBierTxTunnelLeafPrefixType_Object = MibTableColumn
vRtrBierTxTunnelLeafPrefixType = _VRtrBierTxTunnelLeafPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1, 2),
    _VRtrBierTxTunnelLeafPrefixType_Type()
)
vRtrBierTxTunnelLeafPrefixType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierTxTunnelLeafPrefixType.setStatus("current")


class _VRtrBierTxTunnelLeafPrefix_Type(InetAddress):
    """Custom type vRtrBierTxTunnelLeafPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierTxTunnelLeafPrefix_Type.__name__ = "InetAddress"
_VRtrBierTxTunnelLeafPrefix_Object = MibTableColumn
vRtrBierTxTunnelLeafPrefix = _VRtrBierTxTunnelLeafPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1, 3),
    _VRtrBierTxTunnelLeafPrefix_Type()
)
vRtrBierTxTunnelLeafPrefix.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    vRtrBierTxTunnelLeafPrefix.setStatus("current")
_VRtrBierTxTunnelMvpnId_Type = Unsigned32
_VRtrBierTxTunnelMvpnId_Object = MibTableColumn
vRtrBierTxTunnelMvpnId = _VRtrBierTxTunnelMvpnId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1, 4),
    _VRtrBierTxTunnelMvpnId_Type()
)
vRtrBierTxTunnelMvpnId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTxTunnelMvpnId.setStatus("current")
_VRtrBierTxTunnelOperState_Type = TmnxAdminState
_VRtrBierTxTunnelOperState_Object = MibTableColumn
vRtrBierTxTunnelOperState = _VRtrBierTxTunnelOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1, 5),
    _VRtrBierTxTunnelOperState_Type()
)
vRtrBierTxTunnelOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTxTunnelOperState.setStatus("current")
_VRtrBierTxTunnelPtaPrefixType_Type = InetAddressType
_VRtrBierTxTunnelPtaPrefixType_Object = MibTableColumn
vRtrBierTxTunnelPtaPrefixType = _VRtrBierTxTunnelPtaPrefixType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1, 6),
    _VRtrBierTxTunnelPtaPrefixType_Type()
)
vRtrBierTxTunnelPtaPrefixType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTxTunnelPtaPrefixType.setStatus("current")


class _VRtrBierTxTunnelPtaPrefix_Type(InetAddress):
    """Custom type vRtrBierTxTunnelPtaPrefix based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierTxTunnelPtaPrefix_Type.__name__ = "InetAddress"
_VRtrBierTxTunnelPtaPrefix_Object = MibTableColumn
vRtrBierTxTunnelPtaPrefix = _VRtrBierTxTunnelPtaPrefix_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1, 7),
    _VRtrBierTxTunnelPtaPrefix_Type()
)
vRtrBierTxTunnelPtaPrefix.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTxTunnelPtaPrefix.setStatus("current")
_VRtrBierTxTunnelPtaBfrId_Type = Unsigned32
_VRtrBierTxTunnelPtaBfrId_Object = MibTableColumn
vRtrBierTxTunnelPtaBfrId = _VRtrBierTxTunnelPtaBfrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1, 8),
    _VRtrBierTxTunnelPtaBfrId_Type()
)
vRtrBierTxTunnelPtaBfrId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTxTunnelPtaBfrId.setStatus("current")
_VRtrBierTxTunnelPtaSubDomain_Type = Unsigned32
_VRtrBierTxTunnelPtaSubDomain_Object = MibTableColumn
vRtrBierTxTunnelPtaSubDomain = _VRtrBierTxTunnelPtaSubDomain_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1, 9),
    _VRtrBierTxTunnelPtaSubDomain_Type()
)
vRtrBierTxTunnelPtaSubDomain.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTxTunnelPtaSubDomain.setStatus("current")
_VRtrBierTxTunnelPtaMplsLabel_Type = Unsigned32
_VRtrBierTxTunnelPtaMplsLabel_Object = MibTableColumn
vRtrBierTxTunnelPtaMplsLabel = _VRtrBierTxTunnelPtaMplsLabel_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1, 10),
    _VRtrBierTxTunnelPtaMplsLabel_Type()
)
vRtrBierTxTunnelPtaMplsLabel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTxTunnelPtaMplsLabel.setStatus("current")
_VRtrBierTxTunnelLeafBfrID_Type = Unsigned32
_VRtrBierTxTunnelLeafBfrID_Object = MibTableColumn
vRtrBierTxTunnelLeafBfrID = _VRtrBierTxTunnelLeafBfrID_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 11, 1, 11),
    _VRtrBierTxTunnelLeafBfrID_Type()
)
vRtrBierTxTunnelLeafBfrID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTxTunnelLeafBfrID.setStatus("current")
_VRtrBierStatsTable_Object = MibTable
vRtrBierStatsTable = _VRtrBierStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12)
)
if mibBuilder.loadTexts:
    vRtrBierStatsTable.setStatus("current")
_VRtrBierStatsEntry_Object = MibTableRow
vRtrBierStatsEntry = _VRtrBierStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1)
)
vRtrBierStatsEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrBierStatsEntry.setStatus("current")
_VRtrBierStatsTotalLearntRoutes_Type = Counter32
_VRtrBierStatsTotalLearntRoutes_Object = MibTableColumn
vRtrBierStatsTotalLearntRoutes = _VRtrBierStatsTotalLearntRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 1),
    _VRtrBierStatsTotalLearntRoutes_Type()
)
vRtrBierStatsTotalLearntRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsTotalLearntRoutes.setStatus("current")
_VRtrBierStatsTotalValidRoutes_Type = Counter32
_VRtrBierStatsTotalValidRoutes_Object = MibTableColumn
vRtrBierStatsTotalValidRoutes = _VRtrBierStatsTotalValidRoutes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 2),
    _VRtrBierStatsTotalValidRoutes_Type()
)
vRtrBierStatsTotalValidRoutes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsTotalValidRoutes.setStatus("current")
_VRtrBierStatsValidNbrNextHops_Type = Counter32
_VRtrBierStatsValidNbrNextHops_Object = MibTableColumn
vRtrBierStatsValidNbrNextHops = _VRtrBierStatsValidNbrNextHops_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 3),
    _VRtrBierStatsValidNbrNextHops_Type()
)
vRtrBierStatsValidNbrNextHops.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsValidNbrNextHops.setStatus("current")
_VRtrBierStatsRxInvalidBierInfo_Type = Counter32
_VRtrBierStatsRxInvalidBierInfo_Object = MibTableColumn
vRtrBierStatsRxInvalidBierInfo = _VRtrBierStatsRxInvalidBierInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 4),
    _VRtrBierStatsRxInvalidBierInfo_Type()
)
vRtrBierStatsRxInvalidBierInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsRxInvalidBierInfo.setStatus("current")
_VRtrBierStatsRxInvalidBfrInfo_Type = Counter32
_VRtrBierStatsRxInvalidBfrInfo_Object = MibTableColumn
vRtrBierStatsRxInvalidBfrInfo = _VRtrBierStatsRxInvalidBfrInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 5),
    _VRtrBierStatsRxInvalidBfrInfo_Type()
)
vRtrBierStatsRxInvalidBfrInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsRxInvalidBfrInfo.setStatus("current")
_VRtrBierStatsRxInvalidEncapInfo_Type = Counter32
_VRtrBierStatsRxInvalidEncapInfo_Object = MibTableColumn
vRtrBierStatsRxInvalidEncapInfo = _VRtrBierStatsRxInvalidEncapInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 6),
    _VRtrBierStatsRxInvalidEncapInfo_Type()
)
vRtrBierStatsRxInvalidEncapInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsRxInvalidEncapInfo.setStatus("current")
_VRtrBierStatsRxInvalidMplsInfo_Type = Counter32
_VRtrBierStatsRxInvalidMplsInfo_Object = MibTableColumn
vRtrBierStatsRxInvalidMplsInfo = _VRtrBierStatsRxInvalidMplsInfo_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 7),
    _VRtrBierStatsRxInvalidMplsInfo_Type()
)
vRtrBierStatsRxInvalidMplsInfo.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsRxInvalidMplsInfo.setStatus("current")
_VRtrBierStatsDiscardTunnelNhop_Type = Counter32
_VRtrBierStatsDiscardTunnelNhop_Object = MibTableColumn
vRtrBierStatsDiscardTunnelNhop = _VRtrBierStatsDiscardTunnelNhop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 8),
    _VRtrBierStatsDiscardTunnelNhop_Type()
)
vRtrBierStatsDiscardTunnelNhop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsDiscardTunnelNhop.setStatus("current")
_VRtrBierStatsDiscardNonNtwIfNhop_Type = Counter32
_VRtrBierStatsDiscardNonNtwIfNhop_Object = MibTableColumn
vRtrBierStatsDiscardNonNtwIfNhop = _VRtrBierStatsDiscardNonNtwIfNhop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 9),
    _VRtrBierStatsDiscardNonNtwIfNhop_Type()
)
vRtrBierStatsDiscardNonNtwIfNhop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsDiscardNonNtwIfNhop.setStatus("current")
_VRtrBierStatsDiscardNonFp4Nhop_Type = Counter32
_VRtrBierStatsDiscardNonFp4Nhop_Object = MibTableColumn
vRtrBierStatsDiscardNonFp4Nhop = _VRtrBierStatsDiscardNonFp4Nhop_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 10),
    _VRtrBierStatsDiscardNonFp4Nhop_Type()
)
vRtrBierStatsDiscardNonFp4Nhop.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsDiscardNonFp4Nhop.setStatus("current")
_VRtrBierStatsSdBslMismatch_Type = Counter32
_VRtrBierStatsSdBslMismatch_Object = MibTableColumn
vRtrBierStatsSdBslMismatch = _VRtrBierStatsSdBslMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 11),
    _VRtrBierStatsSdBslMismatch_Type()
)
vRtrBierStatsSdBslMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsSdBslMismatch.setStatus("current")
_VRtrBierStatsMultiTopoMismatch_Type = Counter32
_VRtrBierStatsMultiTopoMismatch_Object = MibTableColumn
vRtrBierStatsMultiTopoMismatch = _VRtrBierStatsMultiTopoMismatch_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 12),
    _VRtrBierStatsMultiTopoMismatch_Type()
)
vRtrBierStatsMultiTopoMismatch.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsMultiTopoMismatch.setStatus("current")
_VRtrBierStatsUnsupIpv6Routes_Type = Counter32
_VRtrBierStatsUnsupIpv6Routes_Object = MibTableColumn
vRtrBierStatsUnsupIpv6Routes = _VRtrBierStatsUnsupIpv6Routes_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 13),
    _VRtrBierStatsUnsupIpv6Routes_Type()
)
vRtrBierStatsUnsupIpv6Routes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsUnsupIpv6Routes.setStatus("current")
_VRtrBierStatsBfrIdDuplicate_Type = Counter32
_VRtrBierStatsBfrIdDuplicate_Object = MibTableColumn
vRtrBierStatsBfrIdDuplicate = _VRtrBierStatsBfrIdDuplicate_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 12, 1, 14),
    _VRtrBierStatsBfrIdDuplicate_Type()
)
vRtrBierStatsBfrIdDuplicate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierStatsBfrIdDuplicate.setStatus("current")
_VRtrBierNotificationObjs_ObjectIdentity = ObjectIdentity
vRtrBierNotificationObjs = _VRtrBierNotificationObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13)
)
_VRtrBierNotifySubDomainId_Type = Unsigned32
_VRtrBierNotifySubDomainId_Object = MibScalar
vRtrBierNotifySubDomainId = _VRtrBierNotifySubDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 1),
    _VRtrBierNotifySubDomainId_Type()
)
vRtrBierNotifySubDomainId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierNotifySubDomainId.setStatus("current")
_VRtrBierNotifyRecvSubDomainId_Type = Unsigned32
_VRtrBierNotifyRecvSubDomainId_Object = MibScalar
vRtrBierNotifyRecvSubDomainId = _VRtrBierNotifyRecvSubDomainId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 2),
    _VRtrBierNotifyRecvSubDomainId_Type()
)
vRtrBierNotifyRecvSubDomainId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierNotifyRecvSubDomainId.setStatus("current")
_VRtrBierNotifyBsl_Type = Unsigned32
_VRtrBierNotifyBsl_Object = MibScalar
vRtrBierNotifyBsl = _VRtrBierNotifyBsl_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 3),
    _VRtrBierNotifyBsl_Type()
)
vRtrBierNotifyBsl.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierNotifyBsl.setStatus("current")
_VRtrBierNotifyBfrId_Type = Unsigned32
_VRtrBierNotifyBfrId_Object = MibScalar
vRtrBierNotifyBfrId = _VRtrBierNotifyBfrId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 4),
    _VRtrBierNotifyBfrId_Type()
)
vRtrBierNotifyBfrId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierNotifyBfrId.setStatus("current")
_VRtrBierNotifyMTId_Type = TmnxBierMultiTopology
_VRtrBierNotifyMTId_Object = MibScalar
vRtrBierNotifyMTId = _VRtrBierNotifyMTId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 5),
    _VRtrBierNotifyMTId_Type()
)
vRtrBierNotifyMTId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierNotifyMTId.setStatus("current")
_VRtrBierNotifyRecvMTId_Type = TmnxBierMultiTopology
_VRtrBierNotifyRecvMTId_Object = MibScalar
vRtrBierNotifyRecvMTId = _VRtrBierNotifyRecvMTId_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 6),
    _VRtrBierNotifyRecvMTId_Type()
)
vRtrBierNotifyRecvMTId.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierNotifyRecvMTId.setStatus("current")
_VRtrBierPrefix1AddrType_Type = InetAddressType
_VRtrBierPrefix1AddrType_Object = MibScalar
vRtrBierPrefix1AddrType = _VRtrBierPrefix1AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 7),
    _VRtrBierPrefix1AddrType_Type()
)
vRtrBierPrefix1AddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierPrefix1AddrType.setStatus("current")


class _VRtrBierPrefix1Address_Type(InetAddress):
    """Custom type vRtrBierPrefix1Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierPrefix1Address_Type.__name__ = "InetAddress"
_VRtrBierPrefix1Address_Object = MibScalar
vRtrBierPrefix1Address = _VRtrBierPrefix1Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 8),
    _VRtrBierPrefix1Address_Type()
)
vRtrBierPrefix1Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierPrefix1Address.setStatus("current")
_VRtrBierPrefix2AddrType_Type = InetAddressType
_VRtrBierPrefix2AddrType_Object = MibScalar
vRtrBierPrefix2AddrType = _VRtrBierPrefix2AddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 9),
    _VRtrBierPrefix2AddrType_Type()
)
vRtrBierPrefix2AddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierPrefix2AddrType.setStatus("current")


class _VRtrBierPrefix2Address_Type(InetAddress):
    """Custom type vRtrBierPrefix2Address based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierPrefix2Address_Type.__name__ = "InetAddress"
_VRtrBierPrefix2Address_Object = MibScalar
vRtrBierPrefix2Address = _VRtrBierPrefix2Address_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 10),
    _VRtrBierPrefix2Address_Type()
)
vRtrBierPrefix2Address.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierPrefix2Address.setStatus("current")
_VRtrBierNextHopAddrType_Type = InetAddressType
_VRtrBierNextHopAddrType_Object = MibScalar
vRtrBierNextHopAddrType = _VRtrBierNextHopAddrType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 11),
    _VRtrBierNextHopAddrType_Type()
)
vRtrBierNextHopAddrType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierNextHopAddrType.setStatus("current")


class _VRtrBierNextHopAddress_Type(InetAddress):
    """Custom type vRtrBierNextHopAddress based on InetAddress"""
    subtypeSpec = InetAddress.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 0),
        ValueSizeConstraint(4, 4),
        ValueSizeConstraint(16, 16),
    )


_VRtrBierNextHopAddress_Type.__name__ = "InetAddress"
_VRtrBierNextHopAddress_Object = MibScalar
vRtrBierNextHopAddress = _VRtrBierNextHopAddress_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 12),
    _VRtrBierNextHopAddress_Type()
)
vRtrBierNextHopAddress.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierNextHopAddress.setStatus("current")


class _VRtrBierNextHopeType_Type(Integer32):
    """Custom type vRtrBierNextHopeType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tunnel", 0),
          ("non-nw-if", 1),
          ("non-fp4", 2))
    )


_VRtrBierNextHopeType_Type.__name__ = "Integer32"
_VRtrBierNextHopeType_Object = MibScalar
vRtrBierNextHopeType = _VRtrBierNextHopeType_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 13),
    _VRtrBierNextHopeType_Type()
)
vRtrBierNextHopeType.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierNextHopeType.setStatus("current")
_VRtrBierUnsupportedNhopState_Type = TruthValue
_VRtrBierUnsupportedNhopState_Object = MibScalar
vRtrBierUnsupportedNhopState = _VRtrBierUnsupportedNhopState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 13, 14),
    _VRtrBierUnsupportedNhopState_Type()
)
vRtrBierUnsupportedNhopState.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    vRtrBierUnsupportedNhopState.setStatus("current")
_VRtrBierGeneralOperTable_Object = MibTable
vRtrBierGeneralOperTable = _VRtrBierGeneralOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 14)
)
if mibBuilder.loadTexts:
    vRtrBierGeneralOperTable.setStatus("current")
_VRtrBierGeneralOperEntry_Object = MibTableRow
vRtrBierGeneralOperEntry = _VRtrBierGeneralOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 14, 1)
)
vRtrBierGeneralOperEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
)
if mibBuilder.loadTexts:
    vRtrBierGeneralOperEntry.setStatus("current")


class _VRtrBierGeneralOperState_Type(TmnxOperState):
    """Custom type vRtrBierGeneralOperState based on TmnxOperState"""
    defaultValue = 3


_VRtrBierGeneralOperState_Type.__name__ = "TmnxOperState"
_VRtrBierGeneralOperState_Object = MibTableColumn
vRtrBierGeneralOperState = _VRtrBierGeneralOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 14, 1, 1),
    _VRtrBierGeneralOperState_Type()
)
vRtrBierGeneralOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierGeneralOperState.setStatus("current")
_VRtrBierTemplateOperTable_Object = MibTable
vRtrBierTemplateOperTable = _VRtrBierTemplateOperTable_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 15)
)
if mibBuilder.loadTexts:
    vRtrBierTemplateOperTable.setStatus("current")
_VRtrBierTemplateOperEntry_Object = MibTableRow
vRtrBierTemplateOperEntry = _VRtrBierTemplateOperEntry_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 15, 1)
)
vRtrBierTemplateOperEntry.setIndexNames(
    (0, "TIMETRA-VRTR-MIB", "vRtrID"),
    (0, "TIMETRA-BIER-MIB", "vRtrBierTemplateName"),
)
if mibBuilder.loadTexts:
    vRtrBierTemplateOperEntry.setStatus("current")


class _VRtrBierTemplateOperState_Type(TmnxOperState):
    """Custom type vRtrBierTemplateOperState based on TmnxOperState"""
    defaultValue = 3


_VRtrBierTemplateOperState_Type.__name__ = "TmnxOperState"
_VRtrBierTemplateOperState_Object = MibTableColumn
vRtrBierTemplateOperState = _VRtrBierTemplateOperState_Object(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 2, 123, 15, 1, 1),
    _VRtrBierTemplateOperState_Type()
)
vRtrBierTemplateOperState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vRtrBierTemplateOperState.setStatus("current")
_VRtrBierNotifyPrefix_ObjectIdentity = ObjectIdentity
vRtrBierNotifyPrefix = _VRtrBierNotifyPrefix_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 123)
)
_VRtrBierNotifications_ObjectIdentity = ObjectIdentity
vRtrBierNotifications = _VRtrBierNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 123, 0)
)

# Managed Objects groups

tmnxBierV16v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 123, 2, 1)
)
tmnxBierV16v0Group.setObjects(
      *(("TIMETRA-BIER-MIB", "vRtrBierGeneralTableLastChanged"),
        ("TIMETRA-BIER-MIB", "vRtrBierGeneralRowStatus"),
        ("TIMETRA-BIER-MIB", "vRtrBierGeneralAdminState"),
        ("TIMETRA-BIER-MIB", "vRtrBierGeneralRowLastChange"),
        ("TIMETRA-BIER-MIB", "vRtrBierTemplateTableLastChanged"),
        ("TIMETRA-BIER-MIB", "vRtrBierTemplateRowStatus"),
        ("TIMETRA-BIER-MIB", "vRtrBierTemplateAdminState"),
        ("TIMETRA-BIER-MIB", "vRtrBierTemplateRowLastChange"),
        ("TIMETRA-BIER-MIB", "vRtrBierSubDomainTableLstChanged"),
        ("TIMETRA-BIER-MIB", "vRtrBierSubDomainPrefixType"),
        ("TIMETRA-BIER-MIB", "vRtrBierSubDomainPrefix"),
        ("TIMETRA-BIER-MIB", "vRtrBierSubDomainBfrId"),
        ("TIMETRA-BIER-MIB", "vRtrBierSubDomainMT"),
        ("TIMETRA-BIER-MIB", "vRtrBierSubDomainRowStatus"),
        ("TIMETRA-BIER-MIB", "vRtrBierSubDomainRowLastChange"),
        ("TIMETRA-BIER-MIB", "vRtrBierDatabaseBitStringLen"),
        ("TIMETRA-BIER-MIB", "vRtrBierDatabasePrefixType"),
        ("TIMETRA-BIER-MIB", "vRtrBierDatabasePrefix"),
        ("TIMETRA-BIER-MIB", "vRtrBierDatabaseBfrId"),
        ("TIMETRA-BIER-MIB", "vRtrBierDatabaseMT"),
        ("TIMETRA-BIER-MIB", "vRtrBierDatabaseMplsLabelStart"),
        ("TIMETRA-BIER-MIB", "vRtrBierDatabaseMplsLabelEnd"),
        ("TIMETRA-BIER-MIB", "vRtrBierDatabaseMplsLabelTotal"),
        ("TIMETRA-BIER-MIB", "vRtrBierForwardingNbrPrefixType"),
        ("TIMETRA-BIER-MIB", "vRtrBierForwardingNbrPrefix"),
        ("TIMETRA-BIER-MIB", "vRtrBierForwardingBitMask"),
        ("TIMETRA-BIER-MIB", "vRtrBierForwardingMplsLabel"),
        ("TIMETRA-BIER-MIB", "vRtrBierRoutingNbrPrefixType"),
        ("TIMETRA-BIER-MIB", "vRtrBierRoutingNbrPrefix"),
        ("TIMETRA-BIER-MIB", "vRtrBierRoutingBfrId"),
        ("TIMETRA-BIER-MIB", "vRtrBierRoutingLastUpdated"),
        ("TIMETRA-BIER-MIB", "vRtrBierTunnelType"),
        ("TIMETRA-BIER-MIB", "vRtrBierTunnelPrefixType"),
        ("TIMETRA-BIER-MIB", "vRtrBierTunnelPrefix"),
        ("TIMETRA-BIER-MIB", "vRtrBierTunnelSubDomain"),
        ("TIMETRA-BIER-MIB", "vRtrBierTunnelMplsLabel"),
        ("TIMETRA-BIER-MIB", "vRtrBierTunnelBfrId"),
        ("TIMETRA-BIER-MIB", "vRtrBierTunnelOperState"),
        ("TIMETRA-BIER-MIB", "vRtrBierTunnelNumLeaves"),
        ("TIMETRA-BIER-MIB", "vRtrBierTunnelLastOperDownReason"),
        ("TIMETRA-BIER-MIB", "vRtrBierTxTunnelMvpnId"),
        ("TIMETRA-BIER-MIB", "vRtrBierTxTunnelOperState"),
        ("TIMETRA-BIER-MIB", "vRtrBierTxTunnelPtaPrefixType"),
        ("TIMETRA-BIER-MIB", "vRtrBierTxTunnelPtaPrefix"),
        ("TIMETRA-BIER-MIB", "vRtrBierTxTunnelPtaBfrId"),
        ("TIMETRA-BIER-MIB", "vRtrBierTxTunnelPtaSubDomain"),
        ("TIMETRA-BIER-MIB", "vRtrBierTxTunnelPtaMplsLabel"),
        ("TIMETRA-BIER-MIB", "vRtrBierTxTunnelLeafBfrID"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsTotalLearntRoutes"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsTotalValidRoutes"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsValidNbrNextHops"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsRxInvalidBierInfo"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsRxInvalidBfrInfo"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsRxInvalidEncapInfo"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsRxInvalidMplsInfo"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsDiscardTunnelNhop"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsDiscardNonNtwIfNhop"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsDiscardNonFp4Nhop"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsSdBslMismatch"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsMultiTopoMismatch"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsUnsupIpv6Routes"),
        ("TIMETRA-BIER-MIB", "vRtrBierStatsBfrIdDuplicate"))
)
if mibBuilder.loadTexts:
    tmnxBierV16v0Group.setStatus("current")

tmnxBierNotifyObjsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 123, 2, 2)
)
tmnxBierNotifyObjsGroup.setObjects(
      *(("TIMETRA-BIER-MIB", "vRtrBierNotifySubDomainId"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyRecvSubDomainId"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyBsl"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyBfrId"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyMTId"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyRecvMTId"),
        ("TIMETRA-BIER-MIB", "vRtrBierPrefix1AddrType"),
        ("TIMETRA-BIER-MIB", "vRtrBierPrefix1Address"),
        ("TIMETRA-BIER-MIB", "vRtrBierPrefix2AddrType"),
        ("TIMETRA-BIER-MIB", "vRtrBierPrefix2Address"),
        ("TIMETRA-BIER-MIB", "vRtrBierNextHopAddrType"),
        ("TIMETRA-BIER-MIB", "vRtrBierNextHopAddress"),
        ("TIMETRA-BIER-MIB", "vRtrBierNextHopeType"),
        ("TIMETRA-BIER-MIB", "vRtrBierUnsupportedNhopState"))
)
if mibBuilder.loadTexts:
    tmnxBierNotifyObjsGroup.setStatus("current")

tmnxBierOperStateGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 123, 2, 4)
)
tmnxBierOperStateGroup.setObjects(
      *(("TIMETRA-BIER-MIB", "vRtrBierGeneralOperState"),
        ("TIMETRA-BIER-MIB", "vRtrBierTemplateOperState"))
)
if mibBuilder.loadTexts:
    tmnxBierOperStateGroup.setStatus("current")

tmnxBierV19v0Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 123, 2, 5)
)
tmnxBierV19v0Group.setObjects(
    ("TIMETRA-BIER-MIB", "vRtrBierTunnelIsInBand")
)
if mibBuilder.loadTexts:
    tmnxBierV19v0Group.setStatus("current")


# Notification objects

vRtrBierBfrIdCollision = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 123, 0, 1)
)
vRtrBierBfrIdCollision.setObjects(
      *(("TIMETRA-BIER-MIB", "vRtrBierNotifySubDomainId"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyBsl"),
        ("TIMETRA-BIER-MIB", "vRtrBierPrefix1AddrType"),
        ("TIMETRA-BIER-MIB", "vRtrBierPrefix1Address"),
        ("TIMETRA-BIER-MIB", "vRtrBierPrefix2AddrType"),
        ("TIMETRA-BIER-MIB", "vRtrBierPrefix2Address"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyBfrId"))
)
if mibBuilder.loadTexts:
    vRtrBierBfrIdCollision.setStatus(
        "current"
    )

vRtrBierMtMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 123, 0, 2)
)
vRtrBierMtMismatch.setObjects(
      *(("TIMETRA-BIER-MIB", "vRtrBierNotifySubDomainId"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyBsl"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyMTId"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyRecvMTId"))
)
if mibBuilder.loadTexts:
    vRtrBierMtMismatch.setStatus(
        "current"
    )

vRtrBierSubDomainMismatch = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 123, 0, 3)
)
vRtrBierSubDomainMismatch.setObjects(
      *(("TIMETRA-BIER-MIB", "vRtrBierNotifySubDomainId"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyBsl"),
        ("TIMETRA-BIER-MIB", "vRtrBierNotifyRecvSubDomainId"))
)
if mibBuilder.loadTexts:
    vRtrBierSubDomainMismatch.setStatus(
        "current"
    )

vRtrBierUnsupportedNhop = NotificationType(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 3, 123, 0, 4)
)
vRtrBierUnsupportedNhop.setObjects(
      *(("TIMETRA-BIER-MIB", "vRtrBierNextHopeType"),
        ("TIMETRA-BIER-MIB", "vRtrBierUnsupportedNhopState"),
        ("TIMETRA-BIER-MIB", "vRtrBierPrefix1AddrType"),
        ("TIMETRA-BIER-MIB", "vRtrBierPrefix1Address"),
        ("TIMETRA-BIER-MIB", "vRtrBierNextHopAddrType"),
        ("TIMETRA-BIER-MIB", "vRtrBierNextHopAddress"),
        ("TIMETRA-VRTR-MIB", "vRtrIfIndex"))
)
if mibBuilder.loadTexts:
    vRtrBierUnsupportedNhop.setStatus(
        "current"
    )


# Notifications groups

tmnxBierNotificationV16v0Group = NotificationGroup(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 123, 2, 3)
)
tmnxBierNotificationV16v0Group.setObjects(
      *(("TIMETRA-BIER-MIB", "vRtrBierBfrIdCollision"),
        ("TIMETRA-BIER-MIB", "vRtrBierMtMismatch"),
        ("TIMETRA-BIER-MIB", "vRtrBierSubDomainMismatch"),
        ("TIMETRA-BIER-MIB", "vRtrBierUnsupportedNhop"))
)
if mibBuilder.loadTexts:
    tmnxBierNotificationV16v0Group.setStatus(
        "current"
    )


# Agent capabilities


# Module compliance

tmnxBierV16v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 123, 1, 1)
)
tmnxBierV16v0Compliance.setObjects(
      *(("TIMETRA-BIER-MIB", "tmnxBierV16v0Group"),
        ("TIMETRA-BIER-MIB", "tmnxBierNotificationV16v0Group"),
        ("TIMETRA-BIER-MIB", "tmnxBierOperStateGroup"))
)
if mibBuilder.loadTexts:
    tmnxBierV16v0Compliance.setStatus(
        "current"
    )

tmnxBierV19v0Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 6527, 3, 1, 1, 123, 1, 2)
)
tmnxBierV19v0Compliance.setObjects(
    ("TIMETRA-BIER-MIB", "tmnxBierV19v0Group")
)
if mibBuilder.loadTexts:
    tmnxBierV19v0Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TIMETRA-BIER-MIB",
    **{"TmnxBierMultiTopology": TmnxBierMultiTopology,
       "timetraBierMIBModule": timetraBierMIBModule,
       "tmnxBierConformance": tmnxBierConformance,
       "tmnxBierCompliances": tmnxBierCompliances,
       "tmnxBierV16v0Compliance": tmnxBierV16v0Compliance,
       "tmnxBierV19v0Compliance": tmnxBierV19v0Compliance,
       "tmnxBierGroups": tmnxBierGroups,
       "tmnxBierV16v0Group": tmnxBierV16v0Group,
       "tmnxBierNotifyObjsGroup": tmnxBierNotifyObjsGroup,
       "tmnxBierNotificationV16v0Group": tmnxBierNotificationV16v0Group,
       "tmnxBierOperStateGroup": tmnxBierOperStateGroup,
       "tmnxBierV19v0Group": tmnxBierV19v0Group,
       "tmnxBierObjs": tmnxBierObjs,
       "vRtrBierGeneralTableLastChanged": vRtrBierGeneralTableLastChanged,
       "vRtrBierGeneralTable": vRtrBierGeneralTable,
       "vRtrBierGeneralEntry": vRtrBierGeneralEntry,
       "vRtrBierGeneralRowStatus": vRtrBierGeneralRowStatus,
       "vRtrBierGeneralAdminState": vRtrBierGeneralAdminState,
       "vRtrBierGeneralRowLastChange": vRtrBierGeneralRowLastChange,
       "vRtrBierTemplateTableLastChanged": vRtrBierTemplateTableLastChanged,
       "vRtrBierTemplateTable": vRtrBierTemplateTable,
       "vRtrBierTemplateEntry": vRtrBierTemplateEntry,
       "vRtrBierTemplateName": vRtrBierTemplateName,
       "vRtrBierTemplateRowStatus": vRtrBierTemplateRowStatus,
       "vRtrBierTemplateAdminState": vRtrBierTemplateAdminState,
       "vRtrBierTemplateRowLastChange": vRtrBierTemplateRowLastChange,
       "vRtrBierSubDomainTableLstChanged": vRtrBierSubDomainTableLstChanged,
       "vRtrBierSubDomainTable": vRtrBierSubDomainTable,
       "vRtrBierSubDomainEntry": vRtrBierSubDomainEntry,
       "vRtrBierSubDomainStart": vRtrBierSubDomainStart,
       "vRtrBierSubDomainEnd": vRtrBierSubDomainEnd,
       "vRtrBierSubDomainPrefixType": vRtrBierSubDomainPrefixType,
       "vRtrBierSubDomainPrefix": vRtrBierSubDomainPrefix,
       "vRtrBierSubDomainBfrId": vRtrBierSubDomainBfrId,
       "vRtrBierSubDomainMT": vRtrBierSubDomainMT,
       "vRtrBierSubDomainRowStatus": vRtrBierSubDomainRowStatus,
       "vRtrBierSubDomainRowLastChange": vRtrBierSubDomainRowLastChange,
       "vRtrBierDatabaseTable": vRtrBierDatabaseTable,
       "vRtrBierDatabaseEntry": vRtrBierDatabaseEntry,
       "vRtrBierDatabaseSubDomainId": vRtrBierDatabaseSubDomainId,
       "vRtrBierDatabaseBitStringLen": vRtrBierDatabaseBitStringLen,
       "vRtrBierDatabasePrefixType": vRtrBierDatabasePrefixType,
       "vRtrBierDatabasePrefix": vRtrBierDatabasePrefix,
       "vRtrBierDatabaseBfrId": vRtrBierDatabaseBfrId,
       "vRtrBierDatabaseMT": vRtrBierDatabaseMT,
       "vRtrBierDatabaseMplsLabelStart": vRtrBierDatabaseMplsLabelStart,
       "vRtrBierDatabaseMplsLabelEnd": vRtrBierDatabaseMplsLabelEnd,
       "vRtrBierDatabaseMplsLabelTotal": vRtrBierDatabaseMplsLabelTotal,
       "vRtrBierForwardingTable": vRtrBierForwardingTable,
       "vRtrBierForwardingEntry": vRtrBierForwardingEntry,
       "vRtrBierForwardingSubDomainId": vRtrBierForwardingSubDomainId,
       "vRtrBierForwardingBitStringLen": vRtrBierForwardingBitStringLen,
       "vRtrBierForwardingNhopPrefixType": vRtrBierForwardingNhopPrefixType,
       "vRtrBierForwardingNhopPrefix": vRtrBierForwardingNhopPrefix,
       "vRtrBierForwardingNhopIfIndex": vRtrBierForwardingNhopIfIndex,
       "vRtrBierForwardingBierSetId": vRtrBierForwardingBierSetId,
       "vRtrBierForwardingNbrPrefixType": vRtrBierForwardingNbrPrefixType,
       "vRtrBierForwardingNbrPrefix": vRtrBierForwardingNbrPrefix,
       "vRtrBierForwardingBitMask": vRtrBierForwardingBitMask,
       "vRtrBierForwardingMplsLabel": vRtrBierForwardingMplsLabel,
       "vRtrBierRoutingTable": vRtrBierRoutingTable,
       "vRtrBierRoutingEntry": vRtrBierRoutingEntry,
       "vRtrBierRoutingSubDomainId": vRtrBierRoutingSubDomainId,
       "vRtrBierRoutingBitStringLen": vRtrBierRoutingBitStringLen,
       "vRtrBierRoutingNhopPrefixType": vRtrBierRoutingNhopPrefixType,
       "vRtrBierRoutingNhopPrefix": vRtrBierRoutingNhopPrefix,
       "vRtrBierRoutingNhopIfIndex": vRtrBierRoutingNhopIfIndex,
       "vRtrBierRoutingDestPrefixType": vRtrBierRoutingDestPrefixType,
       "vRtrBierRoutingDestPrefix": vRtrBierRoutingDestPrefix,
       "vRtrBierRoutingNbrPrefixType": vRtrBierRoutingNbrPrefixType,
       "vRtrBierRoutingNbrPrefix": vRtrBierRoutingNbrPrefix,
       "vRtrBierRoutingBfrId": vRtrBierRoutingBfrId,
       "vRtrBierRoutingLastUpdated": vRtrBierRoutingLastUpdated,
       "vRtrBierTunnelTable": vRtrBierTunnelTable,
       "vRtrBierTunnelEntry": vRtrBierTunnelEntry,
       "vRtrBierTunnelType": vRtrBierTunnelType,
       "vRtrBierTunnelPrefixType": vRtrBierTunnelPrefixType,
       "vRtrBierTunnelPrefix": vRtrBierTunnelPrefix,
       "vRtrBierTunnelSubDomain": vRtrBierTunnelSubDomain,
       "vRtrBierTunnelMplsLabel": vRtrBierTunnelMplsLabel,
       "vRtrBierTunnelBfrId": vRtrBierTunnelBfrId,
       "vRtrBierTunnelOperState": vRtrBierTunnelOperState,
       "vRtrBierTunnelNumLeaves": vRtrBierTunnelNumLeaves,
       "vRtrBierTunnelLastOperDownReason": vRtrBierTunnelLastOperDownReason,
       "vRtrBierTunnelIsInBand": vRtrBierTunnelIsInBand,
       "vRtrBierTxTunnelLeafTable": vRtrBierTxTunnelLeafTable,
       "vRtrBierTxTunnelLeafEntry": vRtrBierTxTunnelLeafEntry,
       "vRtrBierTxTunnelLeafPrefixType": vRtrBierTxTunnelLeafPrefixType,
       "vRtrBierTxTunnelLeafPrefix": vRtrBierTxTunnelLeafPrefix,
       "vRtrBierTxTunnelMvpnId": vRtrBierTxTunnelMvpnId,
       "vRtrBierTxTunnelOperState": vRtrBierTxTunnelOperState,
       "vRtrBierTxTunnelPtaPrefixType": vRtrBierTxTunnelPtaPrefixType,
       "vRtrBierTxTunnelPtaPrefix": vRtrBierTxTunnelPtaPrefix,
       "vRtrBierTxTunnelPtaBfrId": vRtrBierTxTunnelPtaBfrId,
       "vRtrBierTxTunnelPtaSubDomain": vRtrBierTxTunnelPtaSubDomain,
       "vRtrBierTxTunnelPtaMplsLabel": vRtrBierTxTunnelPtaMplsLabel,
       "vRtrBierTxTunnelLeafBfrID": vRtrBierTxTunnelLeafBfrID,
       "vRtrBierStatsTable": vRtrBierStatsTable,
       "vRtrBierStatsEntry": vRtrBierStatsEntry,
       "vRtrBierStatsTotalLearntRoutes": vRtrBierStatsTotalLearntRoutes,
       "vRtrBierStatsTotalValidRoutes": vRtrBierStatsTotalValidRoutes,
       "vRtrBierStatsValidNbrNextHops": vRtrBierStatsValidNbrNextHops,
       "vRtrBierStatsRxInvalidBierInfo": vRtrBierStatsRxInvalidBierInfo,
       "vRtrBierStatsRxInvalidBfrInfo": vRtrBierStatsRxInvalidBfrInfo,
       "vRtrBierStatsRxInvalidEncapInfo": vRtrBierStatsRxInvalidEncapInfo,
       "vRtrBierStatsRxInvalidMplsInfo": vRtrBierStatsRxInvalidMplsInfo,
       "vRtrBierStatsDiscardTunnelNhop": vRtrBierStatsDiscardTunnelNhop,
       "vRtrBierStatsDiscardNonNtwIfNhop": vRtrBierStatsDiscardNonNtwIfNhop,
       "vRtrBierStatsDiscardNonFp4Nhop": vRtrBierStatsDiscardNonFp4Nhop,
       "vRtrBierStatsSdBslMismatch": vRtrBierStatsSdBslMismatch,
       "vRtrBierStatsMultiTopoMismatch": vRtrBierStatsMultiTopoMismatch,
       "vRtrBierStatsUnsupIpv6Routes": vRtrBierStatsUnsupIpv6Routes,
       "vRtrBierStatsBfrIdDuplicate": vRtrBierStatsBfrIdDuplicate,
       "vRtrBierNotificationObjs": vRtrBierNotificationObjs,
       "vRtrBierNotifySubDomainId": vRtrBierNotifySubDomainId,
       "vRtrBierNotifyRecvSubDomainId": vRtrBierNotifyRecvSubDomainId,
       "vRtrBierNotifyBsl": vRtrBierNotifyBsl,
       "vRtrBierNotifyBfrId": vRtrBierNotifyBfrId,
       "vRtrBierNotifyMTId": vRtrBierNotifyMTId,
       "vRtrBierNotifyRecvMTId": vRtrBierNotifyRecvMTId,
       "vRtrBierPrefix1AddrType": vRtrBierPrefix1AddrType,
       "vRtrBierPrefix1Address": vRtrBierPrefix1Address,
       "vRtrBierPrefix2AddrType": vRtrBierPrefix2AddrType,
       "vRtrBierPrefix2Address": vRtrBierPrefix2Address,
       "vRtrBierNextHopAddrType": vRtrBierNextHopAddrType,
       "vRtrBierNextHopAddress": vRtrBierNextHopAddress,
       "vRtrBierNextHopeType": vRtrBierNextHopeType,
       "vRtrBierUnsupportedNhopState": vRtrBierUnsupportedNhopState,
       "vRtrBierGeneralOperTable": vRtrBierGeneralOperTable,
       "vRtrBierGeneralOperEntry": vRtrBierGeneralOperEntry,
       "vRtrBierGeneralOperState": vRtrBierGeneralOperState,
       "vRtrBierTemplateOperTable": vRtrBierTemplateOperTable,
       "vRtrBierTemplateOperEntry": vRtrBierTemplateOperEntry,
       "vRtrBierTemplateOperState": vRtrBierTemplateOperState,
       "vRtrBierNotifyPrefix": vRtrBierNotifyPrefix,
       "vRtrBierNotifications": vRtrBierNotifications,
       "vRtrBierBfrIdCollision": vRtrBierBfrIdCollision,
       "vRtrBierMtMismatch": vRtrBierMtMismatch,
       "vRtrBierSubDomainMismatch": vRtrBierSubDomainMismatch,
       "vRtrBierUnsupportedNhop": vRtrBierUnsupportedNhop}
)
