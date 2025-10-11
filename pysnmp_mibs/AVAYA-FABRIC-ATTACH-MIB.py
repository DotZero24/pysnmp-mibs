# SNMP MIB module (AVAYA-FABRIC-ATTACH-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/AVAYA-FABRIC-ATTACH-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:19:19 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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

(bayStackMibs,) = mibBuilder.importSymbols(
    "SYNOPTICS-ROOT-MIB",
    "bayStackMibs")


# MODULE-IDENTITY

avayaFabricAttachMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 46)
)
if mibBuilder.loadTexts:
    avayaFabricAttachMib.setRevisions(
        ("2020-09-04 00:00",
         "2020-08-03 00:00",
         "2018-01-25 00:00",
         "2016-11-21 00:00",
         "2016-10-26 00:00",
         "2016-07-12 00:00",
         "2016-05-09 00:00",
         "2016-04-04 00:00",
         "2016-02-12 00:00",
         "2016-01-26 00:00",
         "2015-11-12 00:00",
         "2015-10-30 00:00",
         "2015-10-30 00:00",
         "2015-09-01 00:00",
         "2015-04-27 00:00",
         "2015-04-20 00:00",
         "2015-04-08 00:00",
         "2015-03-11 00:00",
         "2014-12-18 00:00",
         "2014-12-05 00:00",
         "2014-11-10 00:00",
         "2014-10-28 00:00",
         "2014-10-06 00:00",
         "2014-09-10 00:00",
         "2014-07-16 00:00",
         "2014-04-24 00:00",
         "2014-03-03 00:00",
         "2014-01-30 00:00",
         "2013-11-22 00:00",
         "2013-10-11 00:00",
         "2013-08-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AvFabricAttachNotifications_ObjectIdentity = ObjectIdentity
avFabricAttachNotifications = _AvFabricAttachNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 0)
)
_AvFabricAttachObjects_ObjectIdentity = ObjectIdentity
avFabricAttachObjects = _AvFabricAttachObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1)
)


class _AvFabricAttachService_Type(Integer32):
    """Custom type avFabricAttachService based on Integer32"""
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


_AvFabricAttachService_Type.__name__ = "Integer32"
_AvFabricAttachService_Object = MibScalar
avFabricAttachService = _AvFabricAttachService_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 1),
    _AvFabricAttachService_Type()
)
avFabricAttachService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachService.setStatus("current")


class _AvFabricAttachElementType_Type(Integer32):
    """Custom type avFabricAttachElementType based on Integer32"""
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
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("faServer", 2),
          ("faProxy", 3),
          ("faServerNoAuth", 4),
          ("faProxyNoAuth", 5),
          ("faClientWapType1", 6),
          ("faClientWapType2", 7),
          ("faClientSwitch", 8),
          ("faClientRouter", 9),
          ("faClientIpPhone", 10),
          ("faClientIpCamera", 11),
          ("faClientIpVideo", 12),
          ("faClientSecurityDev", 13),
          ("faClientVirtSwitch", 14),
          ("faClientSrvrEndpt", 15),
          ("faClientOnaSdn", 16),
          ("faClientOnaSpbOIp", 17))
    )


_AvFabricAttachElementType_Type.__name__ = "Integer32"
_AvFabricAttachElementType_Object = MibScalar
avFabricAttachElementType = _AvFabricAttachElementType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 2),
    _AvFabricAttachElementType_Type()
)
avFabricAttachElementType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachElementType.setStatus("current")


class _AvFabricAttachPrimaryServerId_Type(OctetString):
    """Custom type avFabricAttachPrimaryServerId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvFabricAttachPrimaryServerId_Type.__name__ = "OctetString"
_AvFabricAttachPrimaryServerId_Object = MibScalar
avFabricAttachPrimaryServerId = _AvFabricAttachPrimaryServerId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 3),
    _AvFabricAttachPrimaryServerId_Type()
)
avFabricAttachPrimaryServerId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachPrimaryServerId.setStatus("current")


class _AvFabricAttachPrimaryServerDescr_Type(SnmpAdminString):
    """Custom type avFabricAttachPrimaryServerDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 128),
    )


_AvFabricAttachPrimaryServerDescr_Type.__name__ = "SnmpAdminString"
_AvFabricAttachPrimaryServerDescr_Object = MibScalar
avFabricAttachPrimaryServerDescr = _AvFabricAttachPrimaryServerDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 4),
    _AvFabricAttachPrimaryServerDescr_Type()
)
avFabricAttachPrimaryServerDescr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachPrimaryServerDescr.setStatus("current")
_AvFabricAttachIsidVlanAsgnsTable_Object = MibTable
avFabricAttachIsidVlanAsgnsTable = _AvFabricAttachIsidVlanAsgnsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 5)
)
if mibBuilder.loadTexts:
    avFabricAttachIsidVlanAsgnsTable.setStatus("current")
_AvFabricAttachIsidVlanAsgnsEntry_Object = MibTableRow
avFabricAttachIsidVlanAsgnsEntry = _AvFabricAttachIsidVlanAsgnsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 5, 1)
)
avFabricAttachIsidVlanAsgnsEntry.setIndexNames(
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachIsidVlanAsgnsIfIndex"),
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachIsidVlanAsgnsIsid"),
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachIsidVlanAsgnsVlan"),
)
if mibBuilder.loadTexts:
    avFabricAttachIsidVlanAsgnsEntry.setStatus("current")


class _AvFabricAttachIsidVlanAsgnsIfIndex_Type(Integer32):
    """Custom type avFabricAttachIsidVlanAsgnsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AvFabricAttachIsidVlanAsgnsIfIndex_Type.__name__ = "Integer32"
_AvFabricAttachIsidVlanAsgnsIfIndex_Object = MibTableColumn
avFabricAttachIsidVlanAsgnsIfIndex = _AvFabricAttachIsidVlanAsgnsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 5, 1, 1),
    _AvFabricAttachIsidVlanAsgnsIfIndex_Type()
)
avFabricAttachIsidVlanAsgnsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachIsidVlanAsgnsIfIndex.setStatus("current")


class _AvFabricAttachIsidVlanAsgnsIsid_Type(Integer32):
    """Custom type avFabricAttachIsidVlanAsgnsIsid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AvFabricAttachIsidVlanAsgnsIsid_Type.__name__ = "Integer32"
_AvFabricAttachIsidVlanAsgnsIsid_Object = MibTableColumn
avFabricAttachIsidVlanAsgnsIsid = _AvFabricAttachIsidVlanAsgnsIsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 5, 1, 2),
    _AvFabricAttachIsidVlanAsgnsIsid_Type()
)
avFabricAttachIsidVlanAsgnsIsid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachIsidVlanAsgnsIsid.setStatus("current")


class _AvFabricAttachIsidVlanAsgnsVlan_Type(Integer32):
    """Custom type avFabricAttachIsidVlanAsgnsVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AvFabricAttachIsidVlanAsgnsVlan_Type.__name__ = "Integer32"
_AvFabricAttachIsidVlanAsgnsVlan_Object = MibTableColumn
avFabricAttachIsidVlanAsgnsVlan = _AvFabricAttachIsidVlanAsgnsVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 5, 1, 3),
    _AvFabricAttachIsidVlanAsgnsVlan_Type()
)
avFabricAttachIsidVlanAsgnsVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachIsidVlanAsgnsVlan.setStatus("current")


class _AvFabricAttachIsidVlanAsgnsState_Type(Integer32):
    """Custom type avFabricAttachIsidVlanAsgnsState based on Integer32"""
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
        *(("other", 1),
          ("pending", 2),
          ("active", 3),
          ("rejected", 4))
    )


_AvFabricAttachIsidVlanAsgnsState_Type.__name__ = "Integer32"
_AvFabricAttachIsidVlanAsgnsState_Object = MibTableColumn
avFabricAttachIsidVlanAsgnsState = _AvFabricAttachIsidVlanAsgnsState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 5, 1, 4),
    _AvFabricAttachIsidVlanAsgnsState_Type()
)
avFabricAttachIsidVlanAsgnsState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachIsidVlanAsgnsState.setStatus("current")
_AvFabricAttachIsidVlanAsgnsRowStatus_Type = RowStatus
_AvFabricAttachIsidVlanAsgnsRowStatus_Object = MibTableColumn
avFabricAttachIsidVlanAsgnsRowStatus = _AvFabricAttachIsidVlanAsgnsRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 5, 1, 5),
    _AvFabricAttachIsidVlanAsgnsRowStatus_Type()
)
avFabricAttachIsidVlanAsgnsRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachIsidVlanAsgnsRowStatus.setStatus("current")


class _AvFabricAttachIsidVlanAsgnsOrigin_Type(Integer32):
    """Custom type avFabricAttachIsidVlanAsgnsOrigin based on Integer32"""
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
        *(("other", 1),
          ("faProxy", 2),
          ("faClient", 3),
          ("faRadiusClient", 4),
          ("faZeroTouchClient", 5))
    )


_AvFabricAttachIsidVlanAsgnsOrigin_Type.__name__ = "Integer32"
_AvFabricAttachIsidVlanAsgnsOrigin_Object = MibTableColumn
avFabricAttachIsidVlanAsgnsOrigin = _AvFabricAttachIsidVlanAsgnsOrigin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 5, 1, 6),
    _AvFabricAttachIsidVlanAsgnsOrigin_Type()
)
avFabricAttachIsidVlanAsgnsOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachIsidVlanAsgnsOrigin.setStatus("current")


class _AvFabricAttachIsidVlanAsgnsIsidName_Type(DisplayString):
    """Custom type avFabricAttachIsidVlanAsgnsIsidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvFabricAttachIsidVlanAsgnsIsidName_Type.__name__ = "DisplayString"
_AvFabricAttachIsidVlanAsgnsIsidName_Object = MibTableColumn
avFabricAttachIsidVlanAsgnsIsidName = _AvFabricAttachIsidVlanAsgnsIsidName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 5, 1, 7),
    _AvFabricAttachIsidVlanAsgnsIsidName_Type()
)
avFabricAttachIsidVlanAsgnsIsidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachIsidVlanAsgnsIsidName.setStatus("current")
_AvFabricAttachPortTable_Object = MibTable
avFabricAttachPortTable = _AvFabricAttachPortTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6)
)
if mibBuilder.loadTexts:
    avFabricAttachPortTable.setStatus("current")
_AvFabricAttachPortEntry_Object = MibTableRow
avFabricAttachPortEntry = _AvFabricAttachPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6, 1)
)
avFabricAttachPortEntry.setIndexNames(
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachPortIfIndex"),
)
if mibBuilder.loadTexts:
    avFabricAttachPortEntry.setStatus("current")


class _AvFabricAttachPortIfIndex_Type(Integer32):
    """Custom type avFabricAttachPortIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AvFabricAttachPortIfIndex_Type.__name__ = "Integer32"
_AvFabricAttachPortIfIndex_Object = MibTableColumn
avFabricAttachPortIfIndex = _AvFabricAttachPortIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6, 1, 1),
    _AvFabricAttachPortIfIndex_Type()
)
avFabricAttachPortIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachPortIfIndex.setStatus("current")


class _AvFabricAttachPortState_Type(Integer32):
    """Custom type avFabricAttachPortState based on Integer32"""
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


_AvFabricAttachPortState_Type.__name__ = "Integer32"
_AvFabricAttachPortState_Object = MibTableColumn
avFabricAttachPortState = _AvFabricAttachPortState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6, 1, 2),
    _AvFabricAttachPortState_Type()
)
avFabricAttachPortState.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachPortState.setStatus("current")
_AvFabricAttachPortRowStatus_Type = RowStatus
_AvFabricAttachPortRowStatus_Object = MibTableColumn
avFabricAttachPortRowStatus = _AvFabricAttachPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6, 1, 3),
    _AvFabricAttachPortRowStatus_Type()
)
avFabricAttachPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachPortRowStatus.setStatus("current")


class _AvFabricAttachPortMsgAuthStatus_Type(Integer32):
    """Custom type avFabricAttachPortMsgAuthStatus based on Integer32"""
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


_AvFabricAttachPortMsgAuthStatus_Type.__name__ = "Integer32"
_AvFabricAttachPortMsgAuthStatus_Object = MibTableColumn
avFabricAttachPortMsgAuthStatus = _AvFabricAttachPortMsgAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6, 1, 4),
    _AvFabricAttachPortMsgAuthStatus_Type()
)
avFabricAttachPortMsgAuthStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachPortMsgAuthStatus.setStatus("current")


class _AvFabricAttachPortMsgAuthKey_Type(OctetString):
    """Custom type avFabricAttachPortMsgAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvFabricAttachPortMsgAuthKey_Type.__name__ = "OctetString"
_AvFabricAttachPortMsgAuthKey_Object = MibTableColumn
avFabricAttachPortMsgAuthKey = _AvFabricAttachPortMsgAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6, 1, 5),
    _AvFabricAttachPortMsgAuthKey_Type()
)
avFabricAttachPortMsgAuthKey.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachPortMsgAuthKey.setStatus("current")


class _AvFabricAttachPortMgmtIsid_Type(Integer32):
    """Custom type avFabricAttachPortMgmtIsid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_AvFabricAttachPortMgmtIsid_Type.__name__ = "Integer32"
_AvFabricAttachPortMgmtIsid_Object = MibTableColumn
avFabricAttachPortMgmtIsid = _AvFabricAttachPortMgmtIsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6, 1, 6),
    _AvFabricAttachPortMgmtIsid_Type()
)
avFabricAttachPortMgmtIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachPortMgmtIsid.setStatus("current")


class _AvFabricAttachPortMgmtCvid_Type(Integer32):
    """Custom type avFabricAttachPortMgmtCvid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4096),
    )


_AvFabricAttachPortMgmtCvid_Type.__name__ = "Integer32"
_AvFabricAttachPortMgmtCvid_Object = MibTableColumn
avFabricAttachPortMgmtCvid = _AvFabricAttachPortMgmtCvid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6, 1, 7),
    _AvFabricAttachPortMgmtCvid_Type()
)
avFabricAttachPortMgmtCvid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachPortMgmtCvid.setStatus("current")


class _AvFabricAttachPortMsgAuthKeymode_Type(Integer32):
    """Custom type avFabricAttachPortMsgAuthKeymode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("strict", 1),
          ("standard", 2))
    )


_AvFabricAttachPortMsgAuthKeymode_Type.__name__ = "Integer32"
_AvFabricAttachPortMsgAuthKeymode_Object = MibTableColumn
avFabricAttachPortMsgAuthKeymode = _AvFabricAttachPortMsgAuthKeymode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6, 1, 8),
    _AvFabricAttachPortMsgAuthKeymode_Type()
)
avFabricAttachPortMsgAuthKeymode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachPortMsgAuthKeymode.setStatus("current")


class _AvFabricAttachPortOrigin_Type(Integer32):
    """Custom type avFabricAttachPortOrigin based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("config", 1),
          ("autoSense", 2))
    )


_AvFabricAttachPortOrigin_Type.__name__ = "Integer32"
_AvFabricAttachPortOrigin_Object = MibTableColumn
avFabricAttachPortOrigin = _AvFabricAttachPortOrigin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 6, 1, 9),
    _AvFabricAttachPortOrigin_Type()
)
avFabricAttachPortOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachPortOrigin.setStatus("current")


class _AvFabricAttachZeroTouchService_Type(Integer32):
    """Custom type avFabricAttachZeroTouchService based on Integer32"""
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


_AvFabricAttachZeroTouchService_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchService_Object = MibScalar
avFabricAttachZeroTouchService = _AvFabricAttachZeroTouchService_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 7),
    _AvFabricAttachZeroTouchService_Type()
)
avFabricAttachZeroTouchService.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchService.setStatus("current")


class _AvFabricAttachMsgAuthStatus_Type(Integer32):
    """Custom type avFabricAttachMsgAuthStatus based on Integer32"""
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


_AvFabricAttachMsgAuthStatus_Type.__name__ = "Integer32"
_AvFabricAttachMsgAuthStatus_Object = MibScalar
avFabricAttachMsgAuthStatus = _AvFabricAttachMsgAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 8),
    _AvFabricAttachMsgAuthStatus_Type()
)
avFabricAttachMsgAuthStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachMsgAuthStatus.setStatus("current")


class _AvFabricAttachMsgAuthKey_Type(OctetString):
    """Custom type avFabricAttachMsgAuthKey based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvFabricAttachMsgAuthKey_Type.__name__ = "OctetString"
_AvFabricAttachMsgAuthKey_Object = MibScalar
avFabricAttachMsgAuthKey = _AvFabricAttachMsgAuthKey_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 9),
    _AvFabricAttachMsgAuthKey_Type()
)
avFabricAttachMsgAuthKey.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachMsgAuthKey.setStatus("current")


class _AvFabricAttachClientProxyStatus_Type(Integer32):
    """Custom type avFabricAttachClientProxyStatus based on Integer32"""
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


_AvFabricAttachClientProxyStatus_Type.__name__ = "Integer32"
_AvFabricAttachClientProxyStatus_Object = MibScalar
avFabricAttachClientProxyStatus = _AvFabricAttachClientProxyStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 10),
    _AvFabricAttachClientProxyStatus_Type()
)
avFabricAttachClientProxyStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachClientProxyStatus.setStatus("current")
_AvFabricAttachDiscElemsTable_Object = MibTable
avFabricAttachDiscElemsTable = _AvFabricAttachDiscElemsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11)
)
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsTable.setStatus("current")
_AvFabricAttachDiscElemsEntry_Object = MibTableRow
avFabricAttachDiscElemsEntry = _AvFabricAttachDiscElemsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1)
)
avFabricAttachDiscElemsEntry.setIndexNames(
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachDiscElemsIfIndex"),
)
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsEntry.setStatus("current")


class _AvFabricAttachDiscElemsIfIndex_Type(Integer32):
    """Custom type avFabricAttachDiscElemsIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AvFabricAttachDiscElemsIfIndex_Type.__name__ = "Integer32"
_AvFabricAttachDiscElemsIfIndex_Object = MibTableColumn
avFabricAttachDiscElemsIfIndex = _AvFabricAttachDiscElemsIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1, 1),
    _AvFabricAttachDiscElemsIfIndex_Type()
)
avFabricAttachDiscElemsIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsIfIndex.setStatus("current")


class _AvFabricAttachDiscElemsElementType_Type(Integer32):
    """Custom type avFabricAttachDiscElemsElementType based on Integer32"""
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
              14,
              15,
              16,
              17)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("faServer", 2),
          ("faProxy", 3),
          ("faServerNoAuth", 4),
          ("faProxyNoAuth", 5),
          ("faClientWapType1", 6),
          ("faClientWapType2", 7),
          ("faClientSwitch", 8),
          ("faClientRouter", 9),
          ("faClientIpPhone", 10),
          ("faClientIpCamera", 11),
          ("faClientIpVideo", 12),
          ("faClientSecurityDev", 13),
          ("faClientVirtSwitch", 14),
          ("faClientSrvrEndpt", 15),
          ("faClientOnaSdn", 16),
          ("faClientOnaSpbOIp", 17))
    )


_AvFabricAttachDiscElemsElementType_Type.__name__ = "Integer32"
_AvFabricAttachDiscElemsElementType_Object = MibTableColumn
avFabricAttachDiscElemsElementType = _AvFabricAttachDiscElemsElementType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1, 2),
    _AvFabricAttachDiscElemsElementType_Type()
)
avFabricAttachDiscElemsElementType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsElementType.setStatus("current")


class _AvFabricAttachDiscElemsElementVlan_Type(Integer32):
    """Custom type avFabricAttachDiscElemsElementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4095),
    )


_AvFabricAttachDiscElemsElementVlan_Type.__name__ = "Integer32"
_AvFabricAttachDiscElemsElementVlan_Object = MibTableColumn
avFabricAttachDiscElemsElementVlan = _AvFabricAttachDiscElemsElementVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1, 3),
    _AvFabricAttachDiscElemsElementVlan_Type()
)
avFabricAttachDiscElemsElementVlan.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsElementVlan.setStatus("current")


class _AvFabricAttachDiscElemsElementId_Type(OctetString):
    """Custom type avFabricAttachDiscElemsElementId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvFabricAttachDiscElemsElementId_Type.__name__ = "OctetString"
_AvFabricAttachDiscElemsElementId_Object = MibTableColumn
avFabricAttachDiscElemsElementId = _AvFabricAttachDiscElemsElementId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1, 4),
    _AvFabricAttachDiscElemsElementId_Type()
)
avFabricAttachDiscElemsElementId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsElementId.setStatus("current")


class _AvFabricAttachDiscElemsElementState_Type(Bits):
    """Custom type avFabricAttachDiscElemsElementState based on Bits"""
    namedValues = NamedValues(
        *(("trafficTagged", 0),
          ("trafficTaggedAndUntagged", 1),
          ("provisionModeDisabled", 2),
          ("provisionModeSpbm", 3),
          ("provisionModeVlan", 4))
    )

_AvFabricAttachDiscElemsElementState_Type.__name__ = "Bits"
_AvFabricAttachDiscElemsElementState_Object = MibTableColumn
avFabricAttachDiscElemsElementState = _AvFabricAttachDiscElemsElementState_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1, 5),
    _AvFabricAttachDiscElemsElementState_Type()
)
avFabricAttachDiscElemsElementState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsElementState.setStatus("current")


class _AvFabricAttachDiscElemsElementAuth_Type(Integer32):
    """Custom type avFabricAttachDiscElemsElementAuth based on Integer32"""
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
        *(("authenticationPass", 1),
          ("authenticationFail", 2),
          ("notAuthenticated", 3),
          ("none", 4))
    )


_AvFabricAttachDiscElemsElementAuth_Type.__name__ = "Integer32"
_AvFabricAttachDiscElemsElementAuth_Object = MibTableColumn
avFabricAttachDiscElemsElementAuth = _AvFabricAttachDiscElemsElementAuth_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1, 6),
    _AvFabricAttachDiscElemsElementAuth_Type()
)
avFabricAttachDiscElemsElementAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsElementAuth.setStatus("current")


class _AvFabricAttachDiscElemsElementTrunkId_Type(Integer32):
    """Custom type avFabricAttachDiscElemsElementTrunkId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AvFabricAttachDiscElemsElementTrunkId_Type.__name__ = "Integer32"
_AvFabricAttachDiscElemsElementTrunkId_Object = MibTableColumn
avFabricAttachDiscElemsElementTrunkId = _AvFabricAttachDiscElemsElementTrunkId_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1, 7),
    _AvFabricAttachDiscElemsElementTrunkId_Type()
)
avFabricAttachDiscElemsElementTrunkId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsElementTrunkId.setStatus("current")


class _AvFabricAttachDiscElemsElementOperAuthStatus_Type(Integer32):
    """Custom type avFabricAttachDiscElemsElementOperAuthStatus based on Integer32"""
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
        *(("none", 1),
          ("successNoAuth", 2),
          ("successAuth", 3),
          ("failMismatchedKeys", 4),
          ("failLocalAuthRemoteNoAuth", 5),
          ("failLocalNoAuthRemoteAuth", 6))
    )


_AvFabricAttachDiscElemsElementOperAuthStatus_Type.__name__ = "Integer32"
_AvFabricAttachDiscElemsElementOperAuthStatus_Object = MibTableColumn
avFabricAttachDiscElemsElementOperAuthStatus = _AvFabricAttachDiscElemsElementOperAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1, 8),
    _AvFabricAttachDiscElemsElementOperAuthStatus_Type()
)
avFabricAttachDiscElemsElementOperAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsElementOperAuthStatus.setStatus("current")


class _AvFabricAttachDiscElemsElementAsgnsOperAuthStatus_Type(Integer32):
    """Custom type avFabricAttachDiscElemsElementAsgnsOperAuthStatus based on Integer32"""
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
        *(("none", 1),
          ("successNoAuth", 2),
          ("successAuth", 3),
          ("failMismatchedKeys", 4),
          ("failLocalAuthRemoteNoAuth", 5),
          ("failLocalNoAuthRemoteAuth", 6))
    )


_AvFabricAttachDiscElemsElementAsgnsOperAuthStatus_Type.__name__ = "Integer32"
_AvFabricAttachDiscElemsElementAsgnsOperAuthStatus_Object = MibTableColumn
avFabricAttachDiscElemsElementAsgnsOperAuthStatus = _AvFabricAttachDiscElemsElementAsgnsOperAuthStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1, 9),
    _AvFabricAttachDiscElemsElementAsgnsOperAuthStatus_Type()
)
avFabricAttachDiscElemsElementAsgnsOperAuthStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsElementAsgnsOperAuthStatus.setStatus("current")


class _AvFabricAttachDiscElemsAsgnsAuth_Type(Integer32):
    """Custom type avFabricAttachDiscElemsAsgnsAuth based on Integer32"""
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
        *(("authenticationPass", 1),
          ("authenticationFail", 2),
          ("notAuthenticated", 3),
          ("none", 4))
    )


_AvFabricAttachDiscElemsAsgnsAuth_Type.__name__ = "Integer32"
_AvFabricAttachDiscElemsAsgnsAuth_Object = MibTableColumn
avFabricAttachDiscElemsAsgnsAuth = _AvFabricAttachDiscElemsAsgnsAuth_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 11, 1, 10),
    _AvFabricAttachDiscElemsAsgnsAuth_Type()
)
avFabricAttachDiscElemsAsgnsAuth.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsAsgnsAuth.setStatus("current")


class _AvFabricAttachAutoProvision_Type(Integer32):
    """Custom type avFabricAttachAutoProvision based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("faServer", 2),
          ("faProxy", 3))
    )


_AvFabricAttachAutoProvision_Type.__name__ = "Integer32"
_AvFabricAttachAutoProvision_Object = MibScalar
avFabricAttachAutoProvision = _AvFabricAttachAutoProvision_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 12),
    _AvFabricAttachAutoProvision_Type()
)
avFabricAttachAutoProvision.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachAutoProvision.setStatus("current")


class _AvFabricAttachProvisionMode_Type(Integer32):
    """Custom type avFabricAttachProvisionMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("spbm", 2),
          ("vlan", 3))
    )


_AvFabricAttachProvisionMode_Type.__name__ = "Integer32"
_AvFabricAttachProvisionMode_Object = MibScalar
avFabricAttachProvisionMode = _AvFabricAttachProvisionMode_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 13),
    _AvFabricAttachProvisionMode_Type()
)
avFabricAttachProvisionMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachProvisionMode.setStatus("current")


class _AvFabricAttachZeroTouchOptionFlags_Type(Bits):
    """Custom type avFabricAttachZeroTouchOptionFlags based on Bits"""
    namedValues = NamedValues(
        *(("ipAddrDhcp", 0),
          ("autoPortModeFaClient", 1),
          ("autoPortModeMhmv", 2),
          ("radiusServer", 3),
          ("nsv", 4),
          ("autoTrustedModeFaClient", 5),
          ("autoPvidModeFaClient", 6),
          ("autoClientAttach", 7),
          ("autoMgmtVlanFaClient", 8))
    )

_AvFabricAttachZeroTouchOptionFlags_Type.__name__ = "Bits"
_AvFabricAttachZeroTouchOptionFlags_Object = MibScalar
avFabricAttachZeroTouchOptionFlags = _AvFabricAttachZeroTouchOptionFlags_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 14),
    _AvFabricAttachZeroTouchOptionFlags_Type()
)
avFabricAttachZeroTouchOptionFlags.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchOptionFlags.setStatus("current")
_AvFabricAttachZeroTouchNsvTable_Object = MibTable
avFabricAttachZeroTouchNsvTable = _AvFabricAttachZeroTouchNsvTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 15)
)
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchNsvTable.setStatus("current")
_AvFabricAttachZeroTouchNsvEntry_Object = MibTableRow
avFabricAttachZeroTouchNsvEntry = _AvFabricAttachZeroTouchNsvEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 15, 1)
)
avFabricAttachZeroTouchNsvEntry.setIndexNames(
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachZeroTouchNsvType"),
)
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchNsvEntry.setStatus("current")


class _AvFabricAttachZeroTouchNsvType_Type(Integer32):
    """Custom type avFabricAttachZeroTouchNsvType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AvFabricAttachZeroTouchNsvType_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchNsvType_Object = MibTableColumn
avFabricAttachZeroTouchNsvType = _AvFabricAttachZeroTouchNsvType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 15, 1, 1),
    _AvFabricAttachZeroTouchNsvType_Type()
)
avFabricAttachZeroTouchNsvType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchNsvType.setStatus("current")


class _AvFabricAttachZeroTouchNsvVlan_Type(Integer32):
    """Custom type avFabricAttachZeroTouchNsvVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_AvFabricAttachZeroTouchNsvVlan_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchNsvVlan_Object = MibTableColumn
avFabricAttachZeroTouchNsvVlan = _AvFabricAttachZeroTouchNsvVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 15, 1, 2),
    _AvFabricAttachZeroTouchNsvVlan_Type()
)
avFabricAttachZeroTouchNsvVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchNsvVlan.setStatus("current")


class _AvFabricAttachZeroTouchNsvPortPriority_Type(Integer32):
    """Custom type avFabricAttachZeroTouchNsvPortPriority based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_AvFabricAttachZeroTouchNsvPortPriority_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchNsvPortPriority_Object = MibTableColumn
avFabricAttachZeroTouchNsvPortPriority = _AvFabricAttachZeroTouchNsvPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 15, 1, 3),
    _AvFabricAttachZeroTouchNsvPortPriority_Type()
)
avFabricAttachZeroTouchNsvPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchNsvPortPriority.setStatus("current")


class _AvFabricAttachZeroTouchNsvStateFlags_Type(Bits):
    """Custom type avFabricAttachZeroTouchNsvStateFlags based on Bits"""
    namedValues = NamedValues(
        *(("updatePvid", 0),
          ("updatePortPriority", 1))
    )

_AvFabricAttachZeroTouchNsvStateFlags_Type.__name__ = "Bits"
_AvFabricAttachZeroTouchNsvStateFlags_Object = MibTableColumn
avFabricAttachZeroTouchNsvStateFlags = _AvFabricAttachZeroTouchNsvStateFlags_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 15, 1, 4),
    _AvFabricAttachZeroTouchNsvStateFlags_Type()
)
avFabricAttachZeroTouchNsvStateFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchNsvStateFlags.setStatus("current")
_AvFabricAttachZeroTouchNsvRowStatus_Type = RowStatus
_AvFabricAttachZeroTouchNsvRowStatus_Object = MibTableColumn
avFabricAttachZeroTouchNsvRowStatus = _AvFabricAttachZeroTouchNsvRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 15, 1, 5),
    _AvFabricAttachZeroTouchNsvRowStatus_Type()
)
avFabricAttachZeroTouchNsvRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchNsvRowStatus.setStatus("current")


class _AvFabricAttachZeroTouchNsvIsid_Type(Integer32):
    """Custom type avFabricAttachZeroTouchNsvIsid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_AvFabricAttachZeroTouchNsvIsid_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchNsvIsid_Object = MibTableColumn
avFabricAttachZeroTouchNsvIsid = _AvFabricAttachZeroTouchNsvIsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 15, 1, 6),
    _AvFabricAttachZeroTouchNsvIsid_Type()
)
avFabricAttachZeroTouchNsvIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchNsvIsid.setStatus("current")


class _AvFabricAttachZeroTouchRadiusPriSrvrIpv4Addr_Type(OctetString):
    """Custom type avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_AvFabricAttachZeroTouchRadiusPriSrvrIpv4Addr_Type.__name__ = "OctetString"
_AvFabricAttachZeroTouchRadiusPriSrvrIpv4Addr_Object = MibScalar
avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr = _AvFabricAttachZeroTouchRadiusPriSrvrIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 16),
    _AvFabricAttachZeroTouchRadiusPriSrvrIpv4Addr_Type()
)
avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr.setStatus("current")


class _AvFabricAttachZeroTouchRadiusSecSrvrIpv4Addr_Type(OctetString):
    """Custom type avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_AvFabricAttachZeroTouchRadiusSecSrvrIpv4Addr_Type.__name__ = "OctetString"
_AvFabricAttachZeroTouchRadiusSecSrvrIpv4Addr_Object = MibScalar
avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr = _AvFabricAttachZeroTouchRadiusSecSrvrIpv4Addr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 17),
    _AvFabricAttachZeroTouchRadiusSecSrvrIpv4Addr_Type()
)
avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr.setStatus("current")


class _AvFabricAttachZeroTouchRadiusTimeout_Type(Integer32):
    """Custom type avFabricAttachZeroTouchRadiusTimeout based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_AvFabricAttachZeroTouchRadiusTimeout_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchRadiusTimeout_Object = MibScalar
avFabricAttachZeroTouchRadiusTimeout = _AvFabricAttachZeroTouchRadiusTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 18),
    _AvFabricAttachZeroTouchRadiusTimeout_Type()
)
avFabricAttachZeroTouchRadiusTimeout.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchRadiusTimeout.setStatus("current")


class _AvFabricAttachStandaloneProxy_Type(Integer32):
    """Custom type avFabricAttachStandaloneProxy based on Integer32"""
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


_AvFabricAttachStandaloneProxy_Type.__name__ = "Integer32"
_AvFabricAttachStandaloneProxy_Object = MibScalar
avFabricAttachStandaloneProxy = _AvFabricAttachStandaloneProxy_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 19),
    _AvFabricAttachStandaloneProxy_Type()
)
avFabricAttachStandaloneProxy.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachStandaloneProxy.setStatus("current")


class _AvFabricAttachStaticUplinkIfIndex_Type(Integer32):
    """Custom type avFabricAttachStaticUplinkIfIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AvFabricAttachStaticUplinkIfIndex_Type.__name__ = "Integer32"
_AvFabricAttachStaticUplinkIfIndex_Object = MibScalar
avFabricAttachStaticUplinkIfIndex = _AvFabricAttachStaticUplinkIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 20),
    _AvFabricAttachStaticUplinkIfIndex_Type()
)
avFabricAttachStaticUplinkIfIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachStaticUplinkIfIndex.setStatus("current")


class _AvFabricAttachStaticUplinkTrunk_Type(Integer32):
    """Custom type avFabricAttachStaticUplinkTrunk based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1023),
    )


_AvFabricAttachStaticUplinkTrunk_Type.__name__ = "Integer32"
_AvFabricAttachStaticUplinkTrunk_Object = MibScalar
avFabricAttachStaticUplinkTrunk = _AvFabricAttachStaticUplinkTrunk_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 21),
    _AvFabricAttachStaticUplinkTrunk_Type()
)
avFabricAttachStaticUplinkTrunk.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachStaticUplinkTrunk.setStatus("current")


class _AvFabricAttachAsgnTimeout_Type(Integer32):
    """Custom type avFabricAttachAsgnTimeout based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 480),
    )


_AvFabricAttachAsgnTimeout_Type.__name__ = "Integer32"
_AvFabricAttachAsgnTimeout_Object = MibScalar
avFabricAttachAsgnTimeout = _AvFabricAttachAsgnTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 22),
    _AvFabricAttachAsgnTimeout_Type()
)
avFabricAttachAsgnTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachAsgnTimeout.setStatus("current")
_AvFabricAttachStatsTable_Object = MibTable
avFabricAttachStatsTable = _AvFabricAttachStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23)
)
if mibBuilder.loadTexts:
    avFabricAttachStatsTable.setStatus("current")
_AvFabricAttachStatsEntry_Object = MibTableRow
avFabricAttachStatsEntry = _AvFabricAttachStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1)
)
avFabricAttachStatsEntry.setIndexNames(
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachStatsPortIndex"),
)
if mibBuilder.loadTexts:
    avFabricAttachStatsEntry.setStatus("current")


class _AvFabricAttachStatsPortIndex_Type(Integer32):
    """Custom type avFabricAttachStatsPortIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AvFabricAttachStatsPortIndex_Type.__name__ = "Integer32"
_AvFabricAttachStatsPortIndex_Object = MibTableColumn
avFabricAttachStatsPortIndex = _AvFabricAttachStatsPortIndex_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 1),
    _AvFabricAttachStatsPortIndex_Type()
)
avFabricAttachStatsPortIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachStatsPortIndex.setStatus("current")
_AvFabricAttachStatsDiscElemReceived_Type = Counter32
_AvFabricAttachStatsDiscElemReceived_Object = MibTableColumn
avFabricAttachStatsDiscElemReceived = _AvFabricAttachStatsDiscElemReceived_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 2),
    _AvFabricAttachStatsDiscElemReceived_Type()
)
avFabricAttachStatsDiscElemReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachStatsDiscElemReceived.setStatus("current")
_AvFabricAttachStatsAsgnReceived_Type = Counter32
_AvFabricAttachStatsAsgnReceived_Object = MibTableColumn
avFabricAttachStatsAsgnReceived = _AvFabricAttachStatsAsgnReceived_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 3),
    _AvFabricAttachStatsAsgnReceived_Type()
)
avFabricAttachStatsAsgnReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachStatsAsgnReceived.setStatus("current")
_AvFabricAttachStatsAsgnAccepted_Type = Counter32
_AvFabricAttachStatsAsgnAccepted_Object = MibTableColumn
avFabricAttachStatsAsgnAccepted = _AvFabricAttachStatsAsgnAccepted_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 4),
    _AvFabricAttachStatsAsgnAccepted_Type()
)
avFabricAttachStatsAsgnAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachStatsAsgnAccepted.setStatus("current")
_AvFabricAttachStatsAsgnRejected_Type = Counter32
_AvFabricAttachStatsAsgnRejected_Object = MibTableColumn
avFabricAttachStatsAsgnRejected = _AvFabricAttachStatsAsgnRejected_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 5),
    _AvFabricAttachStatsAsgnRejected_Type()
)
avFabricAttachStatsAsgnRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachStatsAsgnRejected.setStatus("current")
_AvFabricAttachStatsAsgnExpired_Type = Counter32
_AvFabricAttachStatsAsgnExpired_Object = MibTableColumn
avFabricAttachStatsAsgnExpired = _AvFabricAttachStatsAsgnExpired_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 6),
    _AvFabricAttachStatsAsgnExpired_Type()
)
avFabricAttachStatsAsgnExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachStatsAsgnExpired.setStatus("current")
_AvFabricAttachStatsDiscAuthFailed_Type = Counter32
_AvFabricAttachStatsDiscAuthFailed_Object = MibTableColumn
avFabricAttachStatsDiscAuthFailed = _AvFabricAttachStatsDiscAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 7),
    _AvFabricAttachStatsDiscAuthFailed_Type()
)
avFabricAttachStatsDiscAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachStatsDiscAuthFailed.setStatus("current")
_AvFabricAttachStatsDiscElemExpired_Type = Counter32
_AvFabricAttachStatsDiscElemExpired_Object = MibTableColumn
avFabricAttachStatsDiscElemExpired = _AvFabricAttachStatsDiscElemExpired_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 8),
    _AvFabricAttachStatsDiscElemExpired_Type()
)
avFabricAttachStatsDiscElemExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachStatsDiscElemExpired.setStatus("current")
_AvFabricAttachStatsDiscElemDeleted_Type = Counter32
_AvFabricAttachStatsDiscElemDeleted_Object = MibTableColumn
avFabricAttachStatsDiscElemDeleted = _AvFabricAttachStatsDiscElemDeleted_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 9),
    _AvFabricAttachStatsDiscElemDeleted_Type()
)
avFabricAttachStatsDiscElemDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachStatsDiscElemDeleted.setStatus("current")
_AvFabricAttachStatsAsgnDeleted_Type = Counter32
_AvFabricAttachStatsAsgnDeleted_Object = MibTableColumn
avFabricAttachStatsAsgnDeleted = _AvFabricAttachStatsAsgnDeleted_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 10),
    _AvFabricAttachStatsAsgnDeleted_Type()
)
avFabricAttachStatsAsgnDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachStatsAsgnDeleted.setStatus("current")
_AvFabricAttachStatsAsgnAuthFailed_Type = Counter32
_AvFabricAttachStatsAsgnAuthFailed_Object = MibTableColumn
avFabricAttachStatsAsgnAuthFailed = _AvFabricAttachStatsAsgnAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 23, 1, 11),
    _AvFabricAttachStatsAsgnAuthFailed_Type()
)
avFabricAttachStatsAsgnAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachStatsAsgnAuthFailed.setStatus("current")
_AvFabricAttachGlobalStats_ObjectIdentity = ObjectIdentity
avFabricAttachGlobalStats = _AvFabricAttachGlobalStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24)
)
_AvFabricAttachGlobalStatsDiscElemReceived_Type = Counter32
_AvFabricAttachGlobalStatsDiscElemReceived_Object = MibScalar
avFabricAttachGlobalStatsDiscElemReceived = _AvFabricAttachGlobalStatsDiscElemReceived_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 1),
    _AvFabricAttachGlobalStatsDiscElemReceived_Type()
)
avFabricAttachGlobalStatsDiscElemReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsDiscElemReceived.setStatus("current")
_AvFabricAttachGlobalStatsAsgnReceived_Type = Counter32
_AvFabricAttachGlobalStatsAsgnReceived_Object = MibScalar
avFabricAttachGlobalStatsAsgnReceived = _AvFabricAttachGlobalStatsAsgnReceived_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 2),
    _AvFabricAttachGlobalStatsAsgnReceived_Type()
)
avFabricAttachGlobalStatsAsgnReceived.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsAsgnReceived.setStatus("current")
_AvFabricAttachGlobalStatsAsgnAccepted_Type = Counter32
_AvFabricAttachGlobalStatsAsgnAccepted_Object = MibScalar
avFabricAttachGlobalStatsAsgnAccepted = _AvFabricAttachGlobalStatsAsgnAccepted_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 3),
    _AvFabricAttachGlobalStatsAsgnAccepted_Type()
)
avFabricAttachGlobalStatsAsgnAccepted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsAsgnAccepted.setStatus("current")
_AvFabricAttachGlobalStatsAsgnRejected_Type = Counter32
_AvFabricAttachGlobalStatsAsgnRejected_Object = MibScalar
avFabricAttachGlobalStatsAsgnRejected = _AvFabricAttachGlobalStatsAsgnRejected_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 4),
    _AvFabricAttachGlobalStatsAsgnRejected_Type()
)
avFabricAttachGlobalStatsAsgnRejected.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsAsgnRejected.setStatus("current")
_AvFabricAttachGlobalStatsAsgnExpired_Type = Counter32
_AvFabricAttachGlobalStatsAsgnExpired_Object = MibScalar
avFabricAttachGlobalStatsAsgnExpired = _AvFabricAttachGlobalStatsAsgnExpired_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 5),
    _AvFabricAttachGlobalStatsAsgnExpired_Type()
)
avFabricAttachGlobalStatsAsgnExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsAsgnExpired.setStatus("current")
_AvFabricAttachGlobalStatsDiscAuthFailed_Type = Counter32
_AvFabricAttachGlobalStatsDiscAuthFailed_Object = MibScalar
avFabricAttachGlobalStatsDiscAuthFailed = _AvFabricAttachGlobalStatsDiscAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 6),
    _AvFabricAttachGlobalStatsDiscAuthFailed_Type()
)
avFabricAttachGlobalStatsDiscAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsDiscAuthFailed.setStatus("current")
_AvFabricAttachGlobalStatsDiscElemExpired_Type = Counter32
_AvFabricAttachGlobalStatsDiscElemExpired_Object = MibScalar
avFabricAttachGlobalStatsDiscElemExpired = _AvFabricAttachGlobalStatsDiscElemExpired_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 7),
    _AvFabricAttachGlobalStatsDiscElemExpired_Type()
)
avFabricAttachGlobalStatsDiscElemExpired.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsDiscElemExpired.setStatus("current")
_AvFabricAttachGlobalStatsDiscElemDeleted_Type = Counter32
_AvFabricAttachGlobalStatsDiscElemDeleted_Object = MibScalar
avFabricAttachGlobalStatsDiscElemDeleted = _AvFabricAttachGlobalStatsDiscElemDeleted_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 8),
    _AvFabricAttachGlobalStatsDiscElemDeleted_Type()
)
avFabricAttachGlobalStatsDiscElemDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsDiscElemDeleted.setStatus("current")
_AvFabricAttachGlobalStatsAsgnDeleted_Type = Counter32
_AvFabricAttachGlobalStatsAsgnDeleted_Object = MibScalar
avFabricAttachGlobalStatsAsgnDeleted = _AvFabricAttachGlobalStatsAsgnDeleted_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 9),
    _AvFabricAttachGlobalStatsAsgnDeleted_Type()
)
avFabricAttachGlobalStatsAsgnDeleted.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsAsgnDeleted.setStatus("current")
_AvFabricAttachGlobalStatsAsgnAuthFailed_Type = Counter32
_AvFabricAttachGlobalStatsAsgnAuthFailed_Object = MibScalar
avFabricAttachGlobalStatsAsgnAuthFailed = _AvFabricAttachGlobalStatsAsgnAuthFailed_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 10),
    _AvFabricAttachGlobalStatsAsgnAuthFailed_Type()
)
avFabricAttachGlobalStatsAsgnAuthFailed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsAsgnAuthFailed.setStatus("current")
_AvFabricAttachGlobalStatsCurReceivedBindings_Type = Counter32
_AvFabricAttachGlobalStatsCurReceivedBindings_Object = MibScalar
avFabricAttachGlobalStatsCurReceivedBindings = _AvFabricAttachGlobalStatsCurReceivedBindings_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 11),
    _AvFabricAttachGlobalStatsCurReceivedBindings_Type()
)
avFabricAttachGlobalStatsCurReceivedBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsCurReceivedBindings.setStatus("current")
_AvFabricAttachGlobalStatsCurAdvertisedBindings_Type = Counter32
_AvFabricAttachGlobalStatsCurAdvertisedBindings_Object = MibScalar
avFabricAttachGlobalStatsCurAdvertisedBindings = _AvFabricAttachGlobalStatsCurAdvertisedBindings_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 24, 12),
    _AvFabricAttachGlobalStatsCurAdvertisedBindings_Type()
)
avFabricAttachGlobalStatsCurAdvertisedBindings.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachGlobalStatsCurAdvertisedBindings.setStatus("current")


class _AvFabricAttachExtendedLogging_Type(Integer32):
    """Custom type avFabricAttachExtendedLogging based on Integer32"""
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


_AvFabricAttachExtendedLogging_Type.__name__ = "Integer32"
_AvFabricAttachExtendedLogging_Object = MibScalar
avFabricAttachExtendedLogging = _AvFabricAttachExtendedLogging_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 25),
    _AvFabricAttachExtendedLogging_Type()
)
avFabricAttachExtendedLogging.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachExtendedLogging.setStatus("current")


class _AvFabricAttachDiscTimeout_Type(Integer32):
    """Custom type avFabricAttachDiscTimeout based on Integer32"""
    defaultValue = 240

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 480),
    )


_AvFabricAttachDiscTimeout_Type.__name__ = "Integer32"
_AvFabricAttachDiscTimeout_Object = MibScalar
avFabricAttachDiscTimeout = _AvFabricAttachDiscTimeout_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 26),
    _AvFabricAttachDiscTimeout_Type()
)
avFabricAttachDiscTimeout.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachDiscTimeout.setStatus("current")
_AvFabricAttachZeroTouchClientTable_Object = MibTable
avFabricAttachZeroTouchClientTable = _AvFabricAttachZeroTouchClientTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 27)
)
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientTable.setStatus("current")
_AvFabricAttachZeroTouchClientEntry_Object = MibTableRow
avFabricAttachZeroTouchClientEntry = _AvFabricAttachZeroTouchClientEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 27, 1)
)
avFabricAttachZeroTouchClientEntry.setIndexNames(
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachZeroTouchClientType"),
)
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientEntry.setStatus("current")


class _AvFabricAttachZeroTouchClientType_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AvFabricAttachZeroTouchClientType_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientType_Object = MibTableColumn
avFabricAttachZeroTouchClientType = _AvFabricAttachZeroTouchClientType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 27, 1, 1),
    _AvFabricAttachZeroTouchClientType_Type()
)
avFabricAttachZeroTouchClientType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientType.setStatus("current")


class _AvFabricAttachZeroTouchClientDescr_Type(SnmpAdminString):
    """Custom type avFabricAttachZeroTouchClientDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_AvFabricAttachZeroTouchClientDescr_Type.__name__ = "SnmpAdminString"
_AvFabricAttachZeroTouchClientDescr_Object = MibTableColumn
avFabricAttachZeroTouchClientDescr = _AvFabricAttachZeroTouchClientDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 27, 1, 2),
    _AvFabricAttachZeroTouchClientDescr_Type()
)
avFabricAttachZeroTouchClientDescr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientDescr.setStatus("current")


class _AvFabricAttachZeroTouchClientOptionFlags_Type(Bits):
    """Custom type avFabricAttachZeroTouchClientOptionFlags based on Bits"""
    namedValues = NamedValues(
        *(("ipAddrDhcp", 0),
          ("autoPortModeFaClient", 1),
          ("autoPortModeMhmv", 2),
          ("radiusServer", 3),
          ("nsv", 4),
          ("autoTrustedModeFaClient", 5),
          ("autoPvidModeFaClient", 6),
          ("autoClientAttach", 7),
          ("autoMgmtVlanFaClient", 8))
    )

_AvFabricAttachZeroTouchClientOptionFlags_Type.__name__ = "Bits"
_AvFabricAttachZeroTouchClientOptionFlags_Object = MibTableColumn
avFabricAttachZeroTouchClientOptionFlags = _AvFabricAttachZeroTouchClientOptionFlags_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 27, 1, 3),
    _AvFabricAttachZeroTouchClientOptionFlags_Type()
)
avFabricAttachZeroTouchClientOptionFlags.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientOptionFlags.setStatus("current")
_AvFabricAttachZeroTouchClientRowStatus_Type = RowStatus
_AvFabricAttachZeroTouchClientRowStatus_Object = MibTableColumn
avFabricAttachZeroTouchClientRowStatus = _AvFabricAttachZeroTouchClientRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 27, 1, 4),
    _AvFabricAttachZeroTouchClientRowStatus_Type()
)
avFabricAttachZeroTouchClientRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientRowStatus.setStatus("current")


class _AvFabricAttachZeroTouchClientName_Type(SnmpAdminString):
    """Custom type avFabricAttachZeroTouchClientName based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvFabricAttachZeroTouchClientName_Type.__name__ = "SnmpAdminString"
_AvFabricAttachZeroTouchClientName_Object = MibTableColumn
avFabricAttachZeroTouchClientName = _AvFabricAttachZeroTouchClientName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 27, 1, 5),
    _AvFabricAttachZeroTouchClientName_Type()
)
avFabricAttachZeroTouchClientName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientName.setStatus("current")


class _AvFabricAttachZeroTouchClientOrigin_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientOrigin based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standard", 1),
          ("custom", 2))
    )


_AvFabricAttachZeroTouchClientOrigin_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientOrigin_Object = MibTableColumn
avFabricAttachZeroTouchClientOrigin = _AvFabricAttachZeroTouchClientOrigin_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 27, 1, 6),
    _AvFabricAttachZeroTouchClientOrigin_Type()
)
avFabricAttachZeroTouchClientOrigin.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientOrigin.setStatus("current")
_AvFabricAttachStats_ObjectIdentity = ObjectIdentity
avFabricAttachStats = _AvFabricAttachStats_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 28)
)


class _AvFabricAttachStatsClearErrorCounters_Type(TruthValue):
    """Custom type avFabricAttachStatsClearErrorCounters based on TruthValue"""
    defaultValue = 2


_AvFabricAttachStatsClearErrorCounters_Type.__name__ = "TruthValue"
_AvFabricAttachStatsClearErrorCounters_Object = MibScalar
avFabricAttachStatsClearErrorCounters = _AvFabricAttachStatsClearErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 28, 1),
    _AvFabricAttachStatsClearErrorCounters_Type()
)
avFabricAttachStatsClearErrorCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachStatsClearErrorCounters.setStatus("current")


class _AvFabricAttachStatsClearGlobalErrorCounters_Type(TruthValue):
    """Custom type avFabricAttachStatsClearGlobalErrorCounters based on TruthValue"""
    defaultValue = 2


_AvFabricAttachStatsClearGlobalErrorCounters_Type.__name__ = "TruthValue"
_AvFabricAttachStatsClearGlobalErrorCounters_Object = MibScalar
avFabricAttachStatsClearGlobalErrorCounters = _AvFabricAttachStatsClearGlobalErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 28, 2),
    _AvFabricAttachStatsClearGlobalErrorCounters_Type()
)
avFabricAttachStatsClearGlobalErrorCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachStatsClearGlobalErrorCounters.setStatus("current")


class _AvFabricAttachStatsClearPortErrorCounters_Type(Integer32):
    """Custom type avFabricAttachStatsClearPortErrorCounters based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_AvFabricAttachStatsClearPortErrorCounters_Type.__name__ = "Integer32"
_AvFabricAttachStatsClearPortErrorCounters_Object = MibScalar
avFabricAttachStatsClearPortErrorCounters = _AvFabricAttachStatsClearPortErrorCounters_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 28, 3),
    _AvFabricAttachStatsClearPortErrorCounters_Type()
)
avFabricAttachStatsClearPortErrorCounters.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachStatsClearPortErrorCounters.setStatus("current")
_AvFabricAttachZeroTouchClientAttachTable_Object = MibTable
avFabricAttachZeroTouchClientAttachTable = _AvFabricAttachZeroTouchClientAttachTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 29)
)
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientAttachTable.setStatus("current")
_AvFabricAttachZeroTouchClientAttachEntry_Object = MibTableRow
avFabricAttachZeroTouchClientAttachEntry = _AvFabricAttachZeroTouchClientAttachEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 29, 1)
)
avFabricAttachZeroTouchClientAttachEntry.setIndexNames(
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachZeroTouchClientAttachType"),
)
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientAttachEntry.setStatus("current")


class _AvFabricAttachZeroTouchClientAttachType_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientAttachType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AvFabricAttachZeroTouchClientAttachType_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientAttachType_Object = MibTableColumn
avFabricAttachZeroTouchClientAttachType = _AvFabricAttachZeroTouchClientAttachType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 29, 1, 1),
    _AvFabricAttachZeroTouchClientAttachType_Type()
)
avFabricAttachZeroTouchClientAttachType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientAttachType.setStatus("current")


class _AvFabricAttachZeroTouchClientAttachVlan_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientAttachVlan based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4096),
    )


_AvFabricAttachZeroTouchClientAttachVlan_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientAttachVlan_Object = MibTableColumn
avFabricAttachZeroTouchClientAttachVlan = _AvFabricAttachZeroTouchClientAttachVlan_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 29, 1, 2),
    _AvFabricAttachZeroTouchClientAttachVlan_Type()
)
avFabricAttachZeroTouchClientAttachVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientAttachVlan.setStatus("current")


class _AvFabricAttachZeroTouchClientAttachPortPriority_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientAttachPortPriority based on Integer32"""
    defaultValue = 8

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_AvFabricAttachZeroTouchClientAttachPortPriority_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientAttachPortPriority_Object = MibTableColumn
avFabricAttachZeroTouchClientAttachPortPriority = _AvFabricAttachZeroTouchClientAttachPortPriority_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 29, 1, 3),
    _AvFabricAttachZeroTouchClientAttachPortPriority_Type()
)
avFabricAttachZeroTouchClientAttachPortPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientAttachPortPriority.setStatus("current")


class _AvFabricAttachZeroTouchClientAttachIsid_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientAttachIsid based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777214),
    )


_AvFabricAttachZeroTouchClientAttachIsid_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientAttachIsid_Object = MibTableColumn
avFabricAttachZeroTouchClientAttachIsid = _AvFabricAttachZeroTouchClientAttachIsid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 29, 1, 4),
    _AvFabricAttachZeroTouchClientAttachIsid_Type()
)
avFabricAttachZeroTouchClientAttachIsid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientAttachIsid.setStatus("current")
_AvFabricAttachZeroTouchClientAttachRowStatus_Type = RowStatus
_AvFabricAttachZeroTouchClientAttachRowStatus_Object = MibTableColumn
avFabricAttachZeroTouchClientAttachRowStatus = _AvFabricAttachZeroTouchClientAttachRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 29, 1, 5),
    _AvFabricAttachZeroTouchClientAttachRowStatus_Type()
)
avFabricAttachZeroTouchClientAttachRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientAttachRowStatus.setStatus("current")


class _AvFabricAttachZeroTouchClientAttachExcludeStatic_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientAttachExcludeStatic based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("keepStaticVlans", 1),
          ("removeStaticVlans", 2))
    )


_AvFabricAttachZeroTouchClientAttachExcludeStatic_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientAttachExcludeStatic_Object = MibTableColumn
avFabricAttachZeroTouchClientAttachExcludeStatic = _AvFabricAttachZeroTouchClientAttachExcludeStatic_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 29, 1, 6),
    _AvFabricAttachZeroTouchClientAttachExcludeStatic_Type()
)
avFabricAttachZeroTouchClientAttachExcludeStatic.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientAttachExcludeStatic.setStatus("current")


class _AvFabricAttachZeroTouchClientAttachIsidName_Type(DisplayString):
    """Custom type avFabricAttachZeroTouchClientAttachIsidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 64),
    )


_AvFabricAttachZeroTouchClientAttachIsidName_Type.__name__ = "DisplayString"
_AvFabricAttachZeroTouchClientAttachIsidName_Object = MibTableColumn
avFabricAttachZeroTouchClientAttachIsidName = _AvFabricAttachZeroTouchClientAttachIsidName_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 29, 1, 7),
    _AvFabricAttachZeroTouchClientAttachIsidName_Type()
)
avFabricAttachZeroTouchClientAttachIsidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientAttachIsidName.setStatus("current")
_AvFabricAttachZeroTouchClientDetectTable_Object = MibTable
avFabricAttachZeroTouchClientDetectTable = _AvFabricAttachZeroTouchClientDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 30)
)
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientDetectTable.setStatus("current")
_AvFabricAttachZeroTouchClientDetectEntry_Object = MibTableRow
avFabricAttachZeroTouchClientDetectEntry = _AvFabricAttachZeroTouchClientDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 30, 1)
)
avFabricAttachZeroTouchClientDetectEntry.setIndexNames(
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachZeroTouchClientDetectType"),
    (0, "AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachZeroTouchClientDetectMethod"),
)
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientDetectEntry.setStatus("current")


class _AvFabricAttachZeroTouchClientDetectType_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientDetectType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_AvFabricAttachZeroTouchClientDetectType_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientDetectType_Object = MibTableColumn
avFabricAttachZeroTouchClientDetectType = _AvFabricAttachZeroTouchClientDetectType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 30, 1, 1),
    _AvFabricAttachZeroTouchClientDetectType_Type()
)
avFabricAttachZeroTouchClientDetectType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientDetectType.setStatus("current")


class _AvFabricAttachZeroTouchClientDetectMethod_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientDetectMethod based on Integer32"""
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
        *(("lldpChassisIdMac", 1),
          ("lldpChassisIdString", 2),
          ("lldpSystemDescrString", 3),
          ("lldpMgmtAddrIPv4", 4))
    )


_AvFabricAttachZeroTouchClientDetectMethod_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientDetectMethod_Object = MibTableColumn
avFabricAttachZeroTouchClientDetectMethod = _AvFabricAttachZeroTouchClientDetectMethod_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 30, 1, 2),
    _AvFabricAttachZeroTouchClientDetectMethod_Type()
)
avFabricAttachZeroTouchClientDetectMethod.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientDetectMethod.setStatus("current")


class _AvFabricAttachZeroTouchClientDetectData_Type(OctetString):
    """Custom type avFabricAttachZeroTouchClientDetectData based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_AvFabricAttachZeroTouchClientDetectData_Type.__name__ = "OctetString"
_AvFabricAttachZeroTouchClientDetectData_Object = MibTableColumn
avFabricAttachZeroTouchClientDetectData = _AvFabricAttachZeroTouchClientDetectData_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 30, 1, 3),
    _AvFabricAttachZeroTouchClientDetectData_Type()
)
avFabricAttachZeroTouchClientDetectData.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientDetectData.setStatus("current")


class _AvFabricAttachZeroTouchClientDetectElementType_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientDetectElementType based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_AvFabricAttachZeroTouchClientDetectElementType_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientDetectElementType_Object = MibTableColumn
avFabricAttachZeroTouchClientDetectElementType = _AvFabricAttachZeroTouchClientDetectElementType_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 30, 1, 4),
    _AvFabricAttachZeroTouchClientDetectElementType_Type()
)
avFabricAttachZeroTouchClientDetectElementType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientDetectElementType.setStatus("current")


class _AvFabricAttachZeroTouchClientDetectLogicOper_Type(Integer32):
    """Custom type avFabricAttachZeroTouchClientDetectLogicOper based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("and", 1),
          ("or", 2))
    )


_AvFabricAttachZeroTouchClientDetectLogicOper_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchClientDetectLogicOper_Object = MibTableColumn
avFabricAttachZeroTouchClientDetectLogicOper = _AvFabricAttachZeroTouchClientDetectLogicOper_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 30, 1, 5),
    _AvFabricAttachZeroTouchClientDetectLogicOper_Type()
)
avFabricAttachZeroTouchClientDetectLogicOper.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientDetectLogicOper.setStatus("current")
_AvFabricAttachZeroTouchClientDetectRowStatus_Type = RowStatus
_AvFabricAttachZeroTouchClientDetectRowStatus_Object = MibTableColumn
avFabricAttachZeroTouchClientDetectRowStatus = _AvFabricAttachZeroTouchClientDetectRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 30, 1, 6),
    _AvFabricAttachZeroTouchClientDetectRowStatus_Type()
)
avFabricAttachZeroTouchClientDetectRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchClientDetectRowStatus.setStatus("current")


class _AvFabricAttachZeroTouchMgmtVlanDist_Type(Integer32):
    """Custom type avFabricAttachZeroTouchMgmtVlanDist based on Integer32"""
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


_AvFabricAttachZeroTouchMgmtVlanDist_Type.__name__ = "Integer32"
_AvFabricAttachZeroTouchMgmtVlanDist_Object = MibScalar
avFabricAttachZeroTouchMgmtVlanDist = _AvFabricAttachZeroTouchMgmtVlanDist_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 1, 31),
    _AvFabricAttachZeroTouchMgmtVlanDist_Type()
)
avFabricAttachZeroTouchMgmtVlanDist.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    avFabricAttachZeroTouchMgmtVlanDist.setStatus("current")
_AvFabricAttachNotifyObjects_ObjectIdentity = ObjectIdentity
avFabricAttachNotifyObjects = _AvFabricAttachNotifyObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 2)
)


class _AvFabricAttachDiscElemsSysDescr_Type(SnmpAdminString):
    """Custom type avFabricAttachDiscElemsSysDescr based on SnmpAdminString"""
    subtypeSpec = SnmpAdminString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 255),
    )


_AvFabricAttachDiscElemsSysDescr_Type.__name__ = "SnmpAdminString"
_AvFabricAttachDiscElemsSysDescr_Object = MibScalar
avFabricAttachDiscElemsSysDescr = _AvFabricAttachDiscElemsSysDescr_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 2, 1),
    _AvFabricAttachDiscElemsSysDescr_Type()
)
avFabricAttachDiscElemsSysDescr.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsSysDescr.setStatus("current")
_AvFabricAttachDiscElemsMgmtOid_Type = ObjectIdentifier
_AvFabricAttachDiscElemsMgmtOid_Object = MibScalar
avFabricAttachDiscElemsMgmtOid = _AvFabricAttachDiscElemsMgmtOid_Object(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 2, 2),
    _AvFabricAttachDiscElemsMgmtOid_Type()
)
avFabricAttachDiscElemsMgmtOid.setMaxAccess("accessible-for-notify")
if mibBuilder.loadTexts:
    avFabricAttachDiscElemsMgmtOid.setStatus("current")

# Managed Objects groups


# Notification objects

avFabricAttachDiscoveredElement = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 0, 1)
)
avFabricAttachDiscoveredElement.setObjects(
      *(("AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachDiscElemsElementType"),
        ("AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachDiscElemsElementId"),
        ("AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachDiscElemsElementAuth"),
        ("AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachDiscElemsSysDescr"),
        ("AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachDiscElemsMgmtOid"))
)
if mibBuilder.loadTexts:
    avFabricAttachDiscoveredElement.setStatus(
        "current"
    )

avFabricAttachExpiredElement = NotificationType(
    (1, 3, 6, 1, 4, 1, 45, 5, 46, 0, 2)
)
avFabricAttachExpiredElement.setObjects(
      *(("AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachDiscElemsElementType"),
        ("AVAYA-FABRIC-ATTACH-MIB", "avFabricAttachDiscElemsElementId"))
)
if mibBuilder.loadTexts:
    avFabricAttachExpiredElement.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AVAYA-FABRIC-ATTACH-MIB",
    **{"avayaFabricAttachMib": avayaFabricAttachMib,
       "avFabricAttachNotifications": avFabricAttachNotifications,
       "avFabricAttachDiscoveredElement": avFabricAttachDiscoveredElement,
       "avFabricAttachExpiredElement": avFabricAttachExpiredElement,
       "avFabricAttachObjects": avFabricAttachObjects,
       "avFabricAttachService": avFabricAttachService,
       "avFabricAttachElementType": avFabricAttachElementType,
       "avFabricAttachPrimaryServerId": avFabricAttachPrimaryServerId,
       "avFabricAttachPrimaryServerDescr": avFabricAttachPrimaryServerDescr,
       "avFabricAttachIsidVlanAsgnsTable": avFabricAttachIsidVlanAsgnsTable,
       "avFabricAttachIsidVlanAsgnsEntry": avFabricAttachIsidVlanAsgnsEntry,
       "avFabricAttachIsidVlanAsgnsIfIndex": avFabricAttachIsidVlanAsgnsIfIndex,
       "avFabricAttachIsidVlanAsgnsIsid": avFabricAttachIsidVlanAsgnsIsid,
       "avFabricAttachIsidVlanAsgnsVlan": avFabricAttachIsidVlanAsgnsVlan,
       "avFabricAttachIsidVlanAsgnsState": avFabricAttachIsidVlanAsgnsState,
       "avFabricAttachIsidVlanAsgnsRowStatus": avFabricAttachIsidVlanAsgnsRowStatus,
       "avFabricAttachIsidVlanAsgnsOrigin": avFabricAttachIsidVlanAsgnsOrigin,
       "avFabricAttachIsidVlanAsgnsIsidName": avFabricAttachIsidVlanAsgnsIsidName,
       "avFabricAttachPortTable": avFabricAttachPortTable,
       "avFabricAttachPortEntry": avFabricAttachPortEntry,
       "avFabricAttachPortIfIndex": avFabricAttachPortIfIndex,
       "avFabricAttachPortState": avFabricAttachPortState,
       "avFabricAttachPortRowStatus": avFabricAttachPortRowStatus,
       "avFabricAttachPortMsgAuthStatus": avFabricAttachPortMsgAuthStatus,
       "avFabricAttachPortMsgAuthKey": avFabricAttachPortMsgAuthKey,
       "avFabricAttachPortMgmtIsid": avFabricAttachPortMgmtIsid,
       "avFabricAttachPortMgmtCvid": avFabricAttachPortMgmtCvid,
       "avFabricAttachPortMsgAuthKeymode": avFabricAttachPortMsgAuthKeymode,
       "avFabricAttachPortOrigin": avFabricAttachPortOrigin,
       "avFabricAttachZeroTouchService": avFabricAttachZeroTouchService,
       "avFabricAttachMsgAuthStatus": avFabricAttachMsgAuthStatus,
       "avFabricAttachMsgAuthKey": avFabricAttachMsgAuthKey,
       "avFabricAttachClientProxyStatus": avFabricAttachClientProxyStatus,
       "avFabricAttachDiscElemsTable": avFabricAttachDiscElemsTable,
       "avFabricAttachDiscElemsEntry": avFabricAttachDiscElemsEntry,
       "avFabricAttachDiscElemsIfIndex": avFabricAttachDiscElemsIfIndex,
       "avFabricAttachDiscElemsElementType": avFabricAttachDiscElemsElementType,
       "avFabricAttachDiscElemsElementVlan": avFabricAttachDiscElemsElementVlan,
       "avFabricAttachDiscElemsElementId": avFabricAttachDiscElemsElementId,
       "avFabricAttachDiscElemsElementState": avFabricAttachDiscElemsElementState,
       "avFabricAttachDiscElemsElementAuth": avFabricAttachDiscElemsElementAuth,
       "avFabricAttachDiscElemsElementTrunkId": avFabricAttachDiscElemsElementTrunkId,
       "avFabricAttachDiscElemsElementOperAuthStatus": avFabricAttachDiscElemsElementOperAuthStatus,
       "avFabricAttachDiscElemsElementAsgnsOperAuthStatus": avFabricAttachDiscElemsElementAsgnsOperAuthStatus,
       "avFabricAttachDiscElemsAsgnsAuth": avFabricAttachDiscElemsAsgnsAuth,
       "avFabricAttachAutoProvision": avFabricAttachAutoProvision,
       "avFabricAttachProvisionMode": avFabricAttachProvisionMode,
       "avFabricAttachZeroTouchOptionFlags": avFabricAttachZeroTouchOptionFlags,
       "avFabricAttachZeroTouchNsvTable": avFabricAttachZeroTouchNsvTable,
       "avFabricAttachZeroTouchNsvEntry": avFabricAttachZeroTouchNsvEntry,
       "avFabricAttachZeroTouchNsvType": avFabricAttachZeroTouchNsvType,
       "avFabricAttachZeroTouchNsvVlan": avFabricAttachZeroTouchNsvVlan,
       "avFabricAttachZeroTouchNsvPortPriority": avFabricAttachZeroTouchNsvPortPriority,
       "avFabricAttachZeroTouchNsvStateFlags": avFabricAttachZeroTouchNsvStateFlags,
       "avFabricAttachZeroTouchNsvRowStatus": avFabricAttachZeroTouchNsvRowStatus,
       "avFabricAttachZeroTouchNsvIsid": avFabricAttachZeroTouchNsvIsid,
       "avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr": avFabricAttachZeroTouchRadiusPriSrvrIpv4Addr,
       "avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr": avFabricAttachZeroTouchRadiusSecSrvrIpv4Addr,
       "avFabricAttachZeroTouchRadiusTimeout": avFabricAttachZeroTouchRadiusTimeout,
       "avFabricAttachStandaloneProxy": avFabricAttachStandaloneProxy,
       "avFabricAttachStaticUplinkIfIndex": avFabricAttachStaticUplinkIfIndex,
       "avFabricAttachStaticUplinkTrunk": avFabricAttachStaticUplinkTrunk,
       "avFabricAttachAsgnTimeout": avFabricAttachAsgnTimeout,
       "avFabricAttachStatsTable": avFabricAttachStatsTable,
       "avFabricAttachStatsEntry": avFabricAttachStatsEntry,
       "avFabricAttachStatsPortIndex": avFabricAttachStatsPortIndex,
       "avFabricAttachStatsDiscElemReceived": avFabricAttachStatsDiscElemReceived,
       "avFabricAttachStatsAsgnReceived": avFabricAttachStatsAsgnReceived,
       "avFabricAttachStatsAsgnAccepted": avFabricAttachStatsAsgnAccepted,
       "avFabricAttachStatsAsgnRejected": avFabricAttachStatsAsgnRejected,
       "avFabricAttachStatsAsgnExpired": avFabricAttachStatsAsgnExpired,
       "avFabricAttachStatsDiscAuthFailed": avFabricAttachStatsDiscAuthFailed,
       "avFabricAttachStatsDiscElemExpired": avFabricAttachStatsDiscElemExpired,
       "avFabricAttachStatsDiscElemDeleted": avFabricAttachStatsDiscElemDeleted,
       "avFabricAttachStatsAsgnDeleted": avFabricAttachStatsAsgnDeleted,
       "avFabricAttachStatsAsgnAuthFailed": avFabricAttachStatsAsgnAuthFailed,
       "avFabricAttachGlobalStats": avFabricAttachGlobalStats,
       "avFabricAttachGlobalStatsDiscElemReceived": avFabricAttachGlobalStatsDiscElemReceived,
       "avFabricAttachGlobalStatsAsgnReceived": avFabricAttachGlobalStatsAsgnReceived,
       "avFabricAttachGlobalStatsAsgnAccepted": avFabricAttachGlobalStatsAsgnAccepted,
       "avFabricAttachGlobalStatsAsgnRejected": avFabricAttachGlobalStatsAsgnRejected,
       "avFabricAttachGlobalStatsAsgnExpired": avFabricAttachGlobalStatsAsgnExpired,
       "avFabricAttachGlobalStatsDiscAuthFailed": avFabricAttachGlobalStatsDiscAuthFailed,
       "avFabricAttachGlobalStatsDiscElemExpired": avFabricAttachGlobalStatsDiscElemExpired,
       "avFabricAttachGlobalStatsDiscElemDeleted": avFabricAttachGlobalStatsDiscElemDeleted,
       "avFabricAttachGlobalStatsAsgnDeleted": avFabricAttachGlobalStatsAsgnDeleted,
       "avFabricAttachGlobalStatsAsgnAuthFailed": avFabricAttachGlobalStatsAsgnAuthFailed,
       "avFabricAttachGlobalStatsCurReceivedBindings": avFabricAttachGlobalStatsCurReceivedBindings,
       "avFabricAttachGlobalStatsCurAdvertisedBindings": avFabricAttachGlobalStatsCurAdvertisedBindings,
       "avFabricAttachExtendedLogging": avFabricAttachExtendedLogging,
       "avFabricAttachDiscTimeout": avFabricAttachDiscTimeout,
       "avFabricAttachZeroTouchClientTable": avFabricAttachZeroTouchClientTable,
       "avFabricAttachZeroTouchClientEntry": avFabricAttachZeroTouchClientEntry,
       "avFabricAttachZeroTouchClientType": avFabricAttachZeroTouchClientType,
       "avFabricAttachZeroTouchClientDescr": avFabricAttachZeroTouchClientDescr,
       "avFabricAttachZeroTouchClientOptionFlags": avFabricAttachZeroTouchClientOptionFlags,
       "avFabricAttachZeroTouchClientRowStatus": avFabricAttachZeroTouchClientRowStatus,
       "avFabricAttachZeroTouchClientName": avFabricAttachZeroTouchClientName,
       "avFabricAttachZeroTouchClientOrigin": avFabricAttachZeroTouchClientOrigin,
       "avFabricAttachStats": avFabricAttachStats,
       "avFabricAttachStatsClearErrorCounters": avFabricAttachStatsClearErrorCounters,
       "avFabricAttachStatsClearGlobalErrorCounters": avFabricAttachStatsClearGlobalErrorCounters,
       "avFabricAttachStatsClearPortErrorCounters": avFabricAttachStatsClearPortErrorCounters,
       "avFabricAttachZeroTouchClientAttachTable": avFabricAttachZeroTouchClientAttachTable,
       "avFabricAttachZeroTouchClientAttachEntry": avFabricAttachZeroTouchClientAttachEntry,
       "avFabricAttachZeroTouchClientAttachType": avFabricAttachZeroTouchClientAttachType,
       "avFabricAttachZeroTouchClientAttachVlan": avFabricAttachZeroTouchClientAttachVlan,
       "avFabricAttachZeroTouchClientAttachPortPriority": avFabricAttachZeroTouchClientAttachPortPriority,
       "avFabricAttachZeroTouchClientAttachIsid": avFabricAttachZeroTouchClientAttachIsid,
       "avFabricAttachZeroTouchClientAttachRowStatus": avFabricAttachZeroTouchClientAttachRowStatus,
       "avFabricAttachZeroTouchClientAttachExcludeStatic": avFabricAttachZeroTouchClientAttachExcludeStatic,
       "avFabricAttachZeroTouchClientAttachIsidName": avFabricAttachZeroTouchClientAttachIsidName,
       "avFabricAttachZeroTouchClientDetectTable": avFabricAttachZeroTouchClientDetectTable,
       "avFabricAttachZeroTouchClientDetectEntry": avFabricAttachZeroTouchClientDetectEntry,
       "avFabricAttachZeroTouchClientDetectType": avFabricAttachZeroTouchClientDetectType,
       "avFabricAttachZeroTouchClientDetectMethod": avFabricAttachZeroTouchClientDetectMethod,
       "avFabricAttachZeroTouchClientDetectData": avFabricAttachZeroTouchClientDetectData,
       "avFabricAttachZeroTouchClientDetectElementType": avFabricAttachZeroTouchClientDetectElementType,
       "avFabricAttachZeroTouchClientDetectLogicOper": avFabricAttachZeroTouchClientDetectLogicOper,
       "avFabricAttachZeroTouchClientDetectRowStatus": avFabricAttachZeroTouchClientDetectRowStatus,
       "avFabricAttachZeroTouchMgmtVlanDist": avFabricAttachZeroTouchMgmtVlanDist,
       "avFabricAttachNotifyObjects": avFabricAttachNotifyObjects,
       "avFabricAttachDiscElemsSysDescr": avFabricAttachDiscElemsSysDescr,
       "avFabricAttachDiscElemsMgmtOid": avFabricAttachDiscElemsMgmtOid}
)
