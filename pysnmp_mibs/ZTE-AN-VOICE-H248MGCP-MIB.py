# SNMP MIB module (ZTE-AN-VOICE-H248MGCP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-VOICE-H248MGCP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:10 2025
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

(DateAndTime,
 DisplayString,
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DateAndTime",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

zxAnVoiceH248MgcpMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxAn_ObjectIdentity = ObjectIdentity
zxAn = _ZxAn_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015)
)
_ZxAnVoiceMgmt_ObjectIdentity = ObjectIdentity
zxAnVoiceMgmt = _ZxAnVoiceMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3)
)
_ZxAnH248MgcpConfig_ObjectIdentity = ObjectIdentity
zxAnH248MgcpConfig = _ZxAnH248MgcpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1)
)
_Md5InfoTable_Object = MibTable
md5InfoTable = _Md5InfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 12)
)
if mibBuilder.loadTexts:
    md5InfoTable.setStatus("current")
_Md5InfoEntry_Object = MibTableRow
md5InfoEntry = _Md5InfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 12, 1)
)
md5InfoEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "md5infoID"),
)
if mibBuilder.loadTexts:
    md5InfoEntry.setStatus("current")


class _Md5infoID_Type(Integer32):
    """Custom type md5infoID based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_Md5infoID_Type.__name__ = "Integer32"
_Md5infoID_Object = MibTableColumn
md5infoID = _Md5infoID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 12, 1, 1),
    _Md5infoID_Type()
)
md5infoID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    md5infoID.setStatus("current")


class _Md5infoG_Type(Integer32):
    """Custom type md5infoG based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 10),
    )


_Md5infoG_Type.__name__ = "Integer32"
_Md5infoG_Object = MibTableColumn
md5infoG = _Md5infoG_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 12, 1, 2),
    _Md5infoG_Type()
)
md5infoG.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    md5infoG.setStatus("current")


class _Md5infoKi_Type(DisplayString):
    """Custom type md5infoKi based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Md5infoKi_Type.__name__ = "DisplayString"
_Md5infoKi_Object = MibTableColumn
md5infoKi = _Md5infoKi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 12, 1, 3),
    _Md5infoKi_Type()
)
md5infoKi.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    md5infoKi.setStatus("current")


class _Md5infoMginfo_Type(DisplayString):
    """Custom type md5infoMginfo based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_Md5infoMginfo_Type.__name__ = "DisplayString"
_Md5infoMginfo_Object = MibTableColumn
md5infoMginfo = _Md5infoMginfo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 12, 1, 4),
    _Md5infoMginfo_Type()
)
md5infoMginfo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    md5infoMginfo.setStatus("current")


class _Md5infoPLenth_Type(Integer32):
    """Custom type md5infoPLenth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 256),
    )


_Md5infoPLenth_Type.__name__ = "Integer32"
_Md5infoPLenth_Object = MibTableColumn
md5infoPLenth = _Md5infoPLenth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 12, 1, 5),
    _Md5infoPLenth_Type()
)
md5infoPLenth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    md5infoPLenth.setStatus("current")


class _Md5infoP_Type(DisplayString):
    """Custom type md5infoP based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 256),
    )


_Md5infoP_Type.__name__ = "DisplayString"
_Md5infoP_Object = MibTableColumn
md5infoP = _Md5infoP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 12, 1, 6),
    _Md5infoP_Type()
)
md5infoP.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    md5infoP.setStatus("current")
_Md5infoRowStatus_Type = RowStatus
_Md5infoRowStatus_Object = MibTableColumn
md5infoRowStatus = _Md5infoRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 12, 1, 7),
    _Md5infoRowStatus_Type()
)
md5infoRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    md5infoRowStatus.setStatus("current")
_ZxAnH248MgcpGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnH248MgcpGlobalObjects = _ZxAnH248MgcpGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1100)
)


class _ZxAnH248MgcpMgmtCapabilities_Type(Bits):
    """Custom type zxAnH248MgcpMgmtCapabilities based on Bits"""
    namedValues = NamedValues(
        ("nbPlatform", 0)
    )

_ZxAnH248MgcpMgmtCapabilities_Type.__name__ = "Bits"
_ZxAnH248MgcpMgmtCapabilities_Object = MibScalar
zxAnH248MgcpMgmtCapabilities = _ZxAnH248MgcpMgmtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1100, 1),
    _ZxAnH248MgcpMgmtCapabilities_Type()
)
zxAnH248MgcpMgmtCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248MgcpMgmtCapabilities.setStatus("current")


class _ZxAnH248MgcpLinkStatus_Type(Integer32):
    """Custom type zxAnH248MgcpLinkStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("normal", 1),
          ("broken", 2))
    )


_ZxAnH248MgcpLinkStatus_Type.__name__ = "Integer32"
_ZxAnH248MgcpLinkStatus_Object = MibScalar
zxAnH248MgcpLinkStatus = _ZxAnH248MgcpLinkStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1100, 2),
    _ZxAnH248MgcpLinkStatus_Type()
)
zxAnH248MgcpLinkStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248MgcpLinkStatus.setStatus("current")
_ZxAnMgcTypeTable_Object = MibTable
zxAnMgcTypeTable = _ZxAnMgcTypeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101)
)
if mibBuilder.loadTexts:
    zxAnMgcTypeTable.setStatus("current")
_ZxAnMgcTypeEntry_Object = MibTableRow
zxAnMgcTypeEntry = _ZxAnMgcTypeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1)
)
zxAnMgcTypeEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnMgcType"),
)
if mibBuilder.loadTexts:
    zxAnMgcTypeEntry.setStatus("current")


class _ZxAnMgcType_Type(Integer32):
    """Custom type zxAnMgcType based on Integer32"""
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
        *(("zte", 1),
          ("hw", 2),
          ("cisco", 3),
          ("alcatel", 4),
          ("nortelMgcp", 5),
          ("nortelH248", 6),
          ("siemens", 7),
          ("ericsson", 8),
          ("metaswitch", 9))
    )


_ZxAnMgcType_Type.__name__ = "Integer32"
_ZxAnMgcType_Object = MibTableColumn
zxAnMgcType = _ZxAnMgcType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 1),
    _ZxAnMgcType_Type()
)
zxAnMgcType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMgcType.setStatus("current")


class _ZxAnMgcRegPktWithAddress_Type(TruthValue):
    """Custom type zxAnMgcRegPktWithAddress based on TruthValue"""
    defaultValue = 1


_ZxAnMgcRegPktWithAddress_Type.__name__ = "TruthValue"
_ZxAnMgcRegPktWithAddress_Object = MibTableColumn
zxAnMgcRegPktWithAddress = _ZxAnMgcRegPktWithAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 4),
    _ZxAnMgcRegPktWithAddress_Type()
)
zxAnMgcRegPktWithAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktWithAddress.setStatus("current")


class _ZxAnMgcRegPktWithVersion_Type(TruthValue):
    """Custom type zxAnMgcRegPktWithVersion based on TruthValue"""
    defaultValue = 1


_ZxAnMgcRegPktWithVersion_Type.__name__ = "TruthValue"
_ZxAnMgcRegPktWithVersion_Object = MibTableColumn
zxAnMgcRegPktWithVersion = _ZxAnMgcRegPktWithVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 5),
    _ZxAnMgcRegPktWithVersion_Type()
)
zxAnMgcRegPktWithVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktWithVersion.setStatus("current")


class _ZxAnMgcRegPktWithDelay_Type(TruthValue):
    """Custom type zxAnMgcRegPktWithDelay based on TruthValue"""
    defaultValue = 2


_ZxAnMgcRegPktWithDelay_Type.__name__ = "TruthValue"
_ZxAnMgcRegPktWithDelay_Object = MibTableColumn
zxAnMgcRegPktWithDelay = _ZxAnMgcRegPktWithDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 6),
    _ZxAnMgcRegPktWithDelay_Type()
)
zxAnMgcRegPktWithDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktWithDelay.setStatus("current")


class _ZxAnMgcRegPktWithProfile_Type(TruthValue):
    """Custom type zxAnMgcRegPktWithProfile based on TruthValue"""
    defaultValue = 1


_ZxAnMgcRegPktWithProfile_Type.__name__ = "TruthValue"
_ZxAnMgcRegPktWithProfile_Object = MibTableColumn
zxAnMgcRegPktWithProfile = _ZxAnMgcRegPktWithProfile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 7),
    _ZxAnMgcRegPktWithProfile_Type()
)
zxAnMgcRegPktWithProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktWithProfile.setStatus("current")


class _ZxAnMgcRegPktWithTimeStamp_Type(TruthValue):
    """Custom type zxAnMgcRegPktWithTimeStamp based on TruthValue"""
    defaultValue = 2


_ZxAnMgcRegPktWithTimeStamp_Type.__name__ = "TruthValue"
_ZxAnMgcRegPktWithTimeStamp_Object = MibTableColumn
zxAnMgcRegPktWithTimeStamp = _ZxAnMgcRegPktWithTimeStamp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 8),
    _ZxAnMgcRegPktWithTimeStamp_Type()
)
zxAnMgcRegPktWithTimeStamp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktWithTimeStamp.setStatus("current")


class _ZxAnMgcRegPktWithReason_Type(TruthValue):
    """Custom type zxAnMgcRegPktWithReason based on TruthValue"""
    defaultValue = 1


_ZxAnMgcRegPktWithReason_Type.__name__ = "TruthValue"
_ZxAnMgcRegPktWithReason_Object = MibTableColumn
zxAnMgcRegPktWithReason = _ZxAnMgcRegPktWithReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 9),
    _ZxAnMgcRegPktWithReason_Type()
)
zxAnMgcRegPktWithReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktWithReason.setStatus("current")


class _ZxAnMgcRegPktBraceDblQuotation_Type(TruthValue):
    """Custom type zxAnMgcRegPktBraceDblQuotation based on TruthValue"""
    defaultValue = 2


_ZxAnMgcRegPktBraceDblQuotation_Type.__name__ = "TruthValue"
_ZxAnMgcRegPktBraceDblQuotation_Object = MibTableColumn
zxAnMgcRegPktBraceDblQuotation = _ZxAnMgcRegPktBraceDblQuotation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 10),
    _ZxAnMgcRegPktBraceDblQuotation_Type()
)
zxAnMgcRegPktBraceDblQuotation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktBraceDblQuotation.setStatus("current")


class _ZxAnMgcRegPktMethod_Type(Integer32):
    """Custom type zxAnMgcRegPktMethod based on Integer32"""
    defaultValue = 2

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
        *(("failover", 1),
          ("restart", 2),
          ("graceful", 3),
          ("forced", 4),
          ("disconnected", 5),
          ("handoff", 6))
    )


_ZxAnMgcRegPktMethod_Type.__name__ = "Integer32"
_ZxAnMgcRegPktMethod_Object = MibTableColumn
zxAnMgcRegPktMethod = _ZxAnMgcRegPktMethod_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 11),
    _ZxAnMgcRegPktMethod_Type()
)
zxAnMgcRegPktMethod.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktMethod.setStatus("current")


class _ZxAnMgcRegPktVersion_Type(Integer32):
    """Custom type zxAnMgcRegPktVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnMgcRegPktVersion_Type.__name__ = "Integer32"
_ZxAnMgcRegPktVersion_Object = MibTableColumn
zxAnMgcRegPktVersion = _ZxAnMgcRegPktVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 12),
    _ZxAnMgcRegPktVersion_Type()
)
zxAnMgcRegPktVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktVersion.setStatus("current")


class _ZxAnMgcRegPktDelay_Type(Integer32):
    """Custom type zxAnMgcRegPktDelay based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnMgcRegPktDelay_Type.__name__ = "Integer32"
_ZxAnMgcRegPktDelay_Object = MibTableColumn
zxAnMgcRegPktDelay = _ZxAnMgcRegPktDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 13),
    _ZxAnMgcRegPktDelay_Type()
)
zxAnMgcRegPktDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktDelay.setStatus("current")


class _ZxAnMgcRegPktProfile_Type(DisplayString):
    """Custom type zxAnMgcRegPktProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 10),
    )


_ZxAnMgcRegPktProfile_Type.__name__ = "DisplayString"
_ZxAnMgcRegPktProfile_Object = MibTableColumn
zxAnMgcRegPktProfile = _ZxAnMgcRegPktProfile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 14),
    _ZxAnMgcRegPktProfile_Type()
)
zxAnMgcRegPktProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktProfile.setStatus("current")


class _ZxAnMgcRegPktReason_Type(Integer32):
    """Custom type zxAnMgcRegPktReason based on Integer32"""
    defaultValue = 901

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(900, 903),
    )


_ZxAnMgcRegPktReason_Type.__name__ = "Integer32"
_ZxAnMgcRegPktReason_Object = MibTableColumn
zxAnMgcRegPktReason = _ZxAnMgcRegPktReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1101, 1, 15),
    _ZxAnMgcRegPktReason_Type()
)
zxAnMgcRegPktReason.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcRegPktReason.setStatus("current")
_ZxAnMgcCfgTable_Object = MibTable
zxAnMgcCfgTable = _ZxAnMgcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102)
)
if mibBuilder.loadTexts:
    zxAnMgcCfgTable.setStatus("current")
_ZxAnMgcCfgEntry_Object = MibTableRow
zxAnMgcCfgEntry = _ZxAnMgcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102, 1)
)
zxAnMgcCfgEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnMgcId"),
)
if mibBuilder.loadTexts:
    zxAnMgcCfgEntry.setStatus("current")


class _ZxAnMgcId_Type(Integer32):
    """Custom type zxAnMgcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 9),
    )


_ZxAnMgcId_Type.__name__ = "Integer32"
_ZxAnMgcId_Object = MibTableColumn
zxAnMgcId = _ZxAnMgcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102, 1, 1),
    _ZxAnMgcId_Type()
)
zxAnMgcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMgcId.setStatus("current")


class _ZxAnMgcTypeId_Type(Integer32):
    """Custom type zxAnMgcTypeId based on Integer32"""
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
        *(("zte", 1),
          ("hw", 2),
          ("cisco", 3),
          ("alcatel", 4),
          ("nortelMgcp", 5),
          ("nortelH248", 6),
          ("siemens", 7),
          ("ericsson", 8),
          ("metaswitch", 9))
    )


_ZxAnMgcTypeId_Type.__name__ = "Integer32"
_ZxAnMgcTypeId_Object = MibTableColumn
zxAnMgcTypeId = _ZxAnMgcTypeId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102, 1, 2),
    _ZxAnMgcTypeId_Type()
)
zxAnMgcTypeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcTypeId.setStatus("current")


class _ZxAnMgcCfgPort_Type(Integer32):
    """Custom type zxAnMgcCfgPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnMgcCfgPort_Type.__name__ = "Integer32"
_ZxAnMgcCfgPort_Object = MibTableColumn
zxAnMgcCfgPort = _ZxAnMgcCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102, 1, 3),
    _ZxAnMgcCfgPort_Type()
)
zxAnMgcCfgPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcCfgPort.setStatus("current")


class _ZxAnMgcNamingType_Type(Integer32):
    """Custom type zxAnMgcNamingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useIp", 1),
          ("useDomainName", 2))
    )


_ZxAnMgcNamingType_Type.__name__ = "Integer32"
_ZxAnMgcNamingType_Object = MibTableColumn
zxAnMgcNamingType = _ZxAnMgcNamingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102, 1, 4),
    _ZxAnMgcNamingType_Type()
)
zxAnMgcNamingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcNamingType.setStatus("current")
_ZxAnMgcIpAddress_Type = IpAddress
_ZxAnMgcIpAddress_Object = MibTableColumn
zxAnMgcIpAddress = _ZxAnMgcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102, 1, 5),
    _ZxAnMgcIpAddress_Type()
)
zxAnMgcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcIpAddress.setStatus("current")


class _ZxAnMgcDomainName_Type(DisplayString):
    """Custom type zxAnMgcDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnMgcDomainName_Type.__name__ = "DisplayString"
_ZxAnMgcDomainName_Object = MibTableColumn
zxAnMgcDomainName = _ZxAnMgcDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102, 1, 6),
    _ZxAnMgcDomainName_Type()
)
zxAnMgcDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcDomainName.setStatus("current")


class _ZxAnMgcMd5Id_Type(Integer32):
    """Custom type zxAnMgcMd5Id based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 9),
    )


_ZxAnMgcMd5Id_Type.__name__ = "Integer32"
_ZxAnMgcMd5Id_Object = MibTableColumn
zxAnMgcMd5Id = _ZxAnMgcMd5Id_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102, 1, 7),
    _ZxAnMgcMd5Id_Type()
)
zxAnMgcMd5Id.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcMd5Id.setStatus("current")


class _ZxAnMgcDescription_Type(DisplayString):
    """Custom type zxAnMgcDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnMgcDescription_Type.__name__ = "DisplayString"
_ZxAnMgcDescription_Object = MibTableColumn
zxAnMgcDescription = _ZxAnMgcDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102, 1, 8),
    _ZxAnMgcDescription_Type()
)
zxAnMgcDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcDescription.setStatus("current")
_ZxAnMgcRowStatus_Type = RowStatus
_ZxAnMgcRowStatus_Object = MibTableColumn
zxAnMgcRowStatus = _ZxAnMgcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1102, 1, 30),
    _ZxAnMgcRowStatus_Type()
)
zxAnMgcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcRowStatus.setStatus("current")
_ZxAnMgCfgTable_Object = MibTable
zxAnMgCfgTable = _ZxAnMgCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110)
)
if mibBuilder.loadTexts:
    zxAnMgCfgTable.setStatus("current")
_ZxAnMgCfgEntry_Object = MibTableRow
zxAnMgCfgEntry = _ZxAnMgCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1)
)
zxAnMgCfgEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnMgId"),
)
if mibBuilder.loadTexts:
    zxAnMgCfgEntry.setStatus("current")


class _ZxAnMgId_Type(Integer32):
    """Custom type zxAnMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnMgId_Type.__name__ = "Integer32"
_ZxAnMgId_Object = MibTableColumn
zxAnMgId = _ZxAnMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 1),
    _ZxAnMgId_Type()
)
zxAnMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMgId.setStatus("current")


class _ZxAnMgProtocolType_Type(Integer32):
    """Custom type zxAnMgProtocolType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("h248", 1),
          ("mgcp", 2))
    )


_ZxAnMgProtocolType_Type.__name__ = "Integer32"
_ZxAnMgProtocolType_Object = MibTableColumn
zxAnMgProtocolType = _ZxAnMgProtocolType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 2),
    _ZxAnMgProtocolType_Type()
)
zxAnMgProtocolType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgProtocolType.setStatus("deprecated")


class _ZxAnMgCfgPort_Type(Integer32):
    """Custom type zxAnMgCfgPort based on Integer32"""
    defaultValue = 2944

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnMgCfgPort_Type.__name__ = "Integer32"
_ZxAnMgCfgPort_Object = MibTableColumn
zxAnMgCfgPort = _ZxAnMgCfgPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 3),
    _ZxAnMgCfgPort_Type()
)
zxAnMgCfgPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgCfgPort.setStatus("current")


class _ZxAnMgCfgDomainName_Type(DisplayString):
    """Custom type zxAnMgCfgDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnMgCfgDomainName_Type.__name__ = "DisplayString"
_ZxAnMgCfgDomainName_Object = MibTableColumn
zxAnMgCfgDomainName = _ZxAnMgCfgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 4),
    _ZxAnMgCfgDomainName_Type()
)
zxAnMgCfgDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgCfgDomainName.setStatus("current")


class _ZxAnMgDescription_Type(DisplayString):
    """Custom type zxAnMgDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnMgDescription_Type.__name__ = "DisplayString"
_ZxAnMgDescription_Object = MibTableColumn
zxAnMgDescription = _ZxAnMgDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 5),
    _ZxAnMgDescription_Type()
)
zxAnMgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgDescription.setStatus("current")


class _ZxAnMgNamingType_Type(Integer32):
    """Custom type zxAnMgNamingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("useIp", 1),
          ("useDomainName", 2))
    )


_ZxAnMgNamingType_Type.__name__ = "Integer32"
_ZxAnMgNamingType_Object = MibTableColumn
zxAnMgNamingType = _ZxAnMgNamingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 6),
    _ZxAnMgNamingType_Type()
)
zxAnMgNamingType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgNamingType.setStatus("current")


class _ZxAnMgcId1_Type(Integer32):
    """Custom type zxAnMgcId1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnMgcId1_Type.__name__ = "Integer32"
_ZxAnMgcId1_Object = MibTableColumn
zxAnMgcId1 = _ZxAnMgcId1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 7),
    _ZxAnMgcId1_Type()
)
zxAnMgcId1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcId1.setStatus("current")


class _ZxAnMgcId2_Type(Integer32):
    """Custom type zxAnMgcId2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnMgcId2_Type.__name__ = "Integer32"
_ZxAnMgcId2_Object = MibTableColumn
zxAnMgcId2 = _ZxAnMgcId2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 8),
    _ZxAnMgcId2_Type()
)
zxAnMgcId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcId2.setStatus("current")


class _ZxAnMgcId3_Type(Integer32):
    """Custom type zxAnMgcId3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnMgcId3_Type.__name__ = "Integer32"
_ZxAnMgcId3_Object = MibTableColumn
zxAnMgcId3 = _ZxAnMgcId3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 9),
    _ZxAnMgcId3_Type()
)
zxAnMgcId3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcId3.setStatus("current")


class _ZxAnMgcId4_Type(Integer32):
    """Custom type zxAnMgcId4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnMgcId4_Type.__name__ = "Integer32"
_ZxAnMgcId4_Object = MibTableColumn
zxAnMgcId4 = _ZxAnMgcId4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 10),
    _ZxAnMgcId4_Type()
)
zxAnMgcId4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcId4.setStatus("current")


class _ZxAnCurrentMgcId_Type(Integer32):
    """Custom type zxAnCurrentMgcId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnCurrentMgcId_Type.__name__ = "Integer32"
_ZxAnCurrentMgcId_Object = MibTableColumn
zxAnCurrentMgcId = _ZxAnCurrentMgcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 11),
    _ZxAnCurrentMgcId_Type()
)
zxAnCurrentMgcId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnCurrentMgcId.setStatus("current")


class _ZxAnMgTranslay_Type(Integer32):
    """Custom type zxAnMgTranslay based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ip", 1),
          ("atm", 2))
    )


_ZxAnMgTranslay_Type.__name__ = "Integer32"
_ZxAnMgTranslay_Object = MibTableColumn
zxAnMgTranslay = _ZxAnMgTranslay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 12),
    _ZxAnMgTranslay_Type()
)
zxAnMgTranslay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgTranslay.setStatus("current")


class _ZxAnMgTransProtocol_Type(Integer32):
    """Custom type zxAnMgTransProtocol based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("udp", 1),
          ("tcp", 2))
    )


_ZxAnMgTransProtocol_Type.__name__ = "Integer32"
_ZxAnMgTransProtocol_Object = MibTableColumn
zxAnMgTransProtocol = _ZxAnMgTransProtocol_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 13),
    _ZxAnMgTransProtocol_Type()
)
zxAnMgTransProtocol.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgTransProtocol.setStatus("current")


class _ZxAnTransactionNum_Type(Integer32):
    """Custom type zxAnTransactionNum based on Integer32"""
    defaultValue = 6000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(5000, 7000),
    )


_ZxAnTransactionNum_Type.__name__ = "Integer32"
_ZxAnTransactionNum_Object = MibTableColumn
zxAnTransactionNum = _ZxAnTransactionNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 14),
    _ZxAnTransactionNum_Type()
)
zxAnTransactionNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnTransactionNum.setStatus("current")


class _ZxAnRtpFaxPri1_Type(Integer32):
    """Custom type zxAnRtpFaxPri1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faxVbd", 1),
          ("faxT38", 2))
    )


_ZxAnRtpFaxPri1_Type.__name__ = "Integer32"
_ZxAnRtpFaxPri1_Object = MibTableColumn
zxAnRtpFaxPri1 = _ZxAnRtpFaxPri1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 15),
    _ZxAnRtpFaxPri1_Type()
)
zxAnRtpFaxPri1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRtpFaxPri1.setStatus("current")


class _ZxAnRtpFaxPri2_Type(Integer32):
    """Custom type zxAnRtpFaxPri2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faxVBD", 1),
          ("faxT38", 2))
    )


_ZxAnRtpFaxPri2_Type.__name__ = "Integer32"
_ZxAnRtpFaxPri2_Object = MibTableColumn
zxAnRtpFaxPri2 = _ZxAnRtpFaxPri2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 16),
    _ZxAnRtpFaxPri2_Type()
)
zxAnRtpFaxPri2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRtpFaxPri2.setStatus("current")


class _ZxAnSelfExchange_Type(TruthValue):
    """Custom type zxAnSelfExchange based on TruthValue"""
    defaultValue = 2


_ZxAnSelfExchange_Type.__name__ = "TruthValue"
_ZxAnSelfExchange_Object = MibTableColumn
zxAnSelfExchange = _ZxAnSelfExchange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 17),
    _ZxAnSelfExchange_Type()
)
zxAnSelfExchange.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSelfExchange.setStatus("current")


class _ZxAnProtectCall_Type(TruthValue):
    """Custom type zxAnProtectCall based on TruthValue"""
    defaultValue = 2


_ZxAnProtectCall_Type.__name__ = "TruthValue"
_ZxAnProtectCall_Object = MibTableColumn
zxAnProtectCall = _ZxAnProtectCall_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 18),
    _ZxAnProtectCall_Type()
)
zxAnProtectCall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnProtectCall.setStatus("current")


class _ZxAnRtp2833PayloadTypeCode_Type(Integer32):
    """Custom type zxAnRtp2833PayloadTypeCode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("negotiatedBySdp", 1),
          ("specifiedByLocalRtpParameter", 2))
    )


_ZxAnRtp2833PayloadTypeCode_Type.__name__ = "Integer32"
_ZxAnRtp2833PayloadTypeCode_Object = MibTableColumn
zxAnRtp2833PayloadTypeCode = _ZxAnRtp2833PayloadTypeCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 19),
    _ZxAnRtp2833PayloadTypeCode_Type()
)
zxAnRtp2833PayloadTypeCode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnRtp2833PayloadTypeCode.setStatus("current")


class _ZxAnPacketMaxTransactionNumber_Type(Integer32):
    """Custom type zxAnPacketMaxTransactionNumber based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnPacketMaxTransactionNumber_Type.__name__ = "Integer32"
_ZxAnPacketMaxTransactionNumber_Object = MibTableColumn
zxAnPacketMaxTransactionNumber = _ZxAnPacketMaxTransactionNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 20),
    _ZxAnPacketMaxTransactionNumber_Type()
)
zxAnPacketMaxTransactionNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnPacketMaxTransactionNumber.setStatus("current")


class _ZxAnHotlineWithSpace_Type(Integer32):
    """Custom type zxAnHotlineWithSpace based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("withoutSpace", 1),
          ("withSpace", 2),
          ("withT", 3))
    )


_ZxAnHotlineWithSpace_Type.__name__ = "Integer32"
_ZxAnHotlineWithSpace_Object = MibTableColumn
zxAnHotlineWithSpace = _ZxAnHotlineWithSpace_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 21),
    _ZxAnHotlineWithSpace_Type()
)
zxAnHotlineWithSpace.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnHotlineWithSpace.setStatus("current")


class _ZxAnAlwaysReportOffhookEvent_Type(TruthValue):
    """Custom type zxAnAlwaysReportOffhookEvent based on TruthValue"""
    defaultValue = 1


_ZxAnAlwaysReportOffhookEvent_Type.__name__ = "TruthValue"
_ZxAnAlwaysReportOffhookEvent_Object = MibTableColumn
zxAnAlwaysReportOffhookEvent = _ZxAnAlwaysReportOffhookEvent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 22),
    _ZxAnAlwaysReportOffhookEvent_Type()
)
zxAnAlwaysReportOffhookEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAlwaysReportOffhookEvent.setStatus("current")


class _ZxAnAlwaysReportOnhookEvent_Type(TruthValue):
    """Custom type zxAnAlwaysReportOnhookEvent based on TruthValue"""
    defaultValue = 1


_ZxAnAlwaysReportOnhookEvent_Type.__name__ = "TruthValue"
_ZxAnAlwaysReportOnhookEvent_Object = MibTableColumn
zxAnAlwaysReportOnhookEvent = _ZxAnAlwaysReportOnhookEvent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 23),
    _ZxAnAlwaysReportOnhookEvent_Type()
)
zxAnAlwaysReportOnhookEvent.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnAlwaysReportOnhookEvent.setStatus("current")


class _ZxAnSubSuspendRtp_Type(TruthValue):
    """Custom type zxAnSubSuspendRtp based on TruthValue"""
    defaultValue = 1


_ZxAnSubSuspendRtp_Type.__name__ = "TruthValue"
_ZxAnSubSuspendRtp_Object = MibTableColumn
zxAnSubSuspendRtp = _ZxAnSubSuspendRtp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 24),
    _ZxAnSubSuspendRtp_Type()
)
zxAnSubSuspendRtp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSubSuspendRtp.setStatus("current")


class _ZxAnDisasterProt_Type(TruthValue):
    """Custom type zxAnDisasterProt based on TruthValue"""
    defaultValue = 1


_ZxAnDisasterProt_Type.__name__ = "TruthValue"
_ZxAnDisasterProt_Object = MibTableColumn
zxAnDisasterProt = _ZxAnDisasterProt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 25),
    _ZxAnDisasterProt_Type()
)
zxAnDisasterProt.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnDisasterProt.setStatus("current")
_ZxAnMgCfgRowStatus_Type = RowStatus
_ZxAnMgCfgRowStatus_Object = MibTableColumn
zxAnMgCfgRowStatus = _ZxAnMgCfgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1110, 1, 100),
    _ZxAnMgCfgRowStatus_Type()
)
zxAnMgCfgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgCfgRowStatus.setStatus("current")
_ZxAnH248ProtocolTable_Object = MibTable
zxAnH248ProtocolTable = _ZxAnH248ProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111)
)
if mibBuilder.loadTexts:
    zxAnH248ProtocolTable.setStatus("current")
_ZxAnH248ProtocolEntry_Object = MibTableRow
zxAnH248ProtocolEntry = _ZxAnH248ProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1)
)
zxAnH248ProtocolEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnH248ProtocolMgId"),
)
if mibBuilder.loadTexts:
    zxAnH248ProtocolEntry.setStatus("current")


class _ZxAnH248ProtocolMgId_Type(Integer32):
    """Custom type zxAnH248ProtocolMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnH248ProtocolMgId_Type.__name__ = "Integer32"
_ZxAnH248ProtocolMgId_Object = MibTableColumn
zxAnH248ProtocolMgId = _ZxAnH248ProtocolMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 1),
    _ZxAnH248ProtocolMgId_Type()
)
zxAnH248ProtocolMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnH248ProtocolMgId.setStatus("current")


class _ZxAnH248ProtocolVersion_Type(Integer32):
    """Custom type zxAnH248ProtocolVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2),
          ("v3", 3))
    )


_ZxAnH248ProtocolVersion_Type.__name__ = "Integer32"
_ZxAnH248ProtocolVersion_Object = MibTableColumn
zxAnH248ProtocolVersion = _ZxAnH248ProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 2),
    _ZxAnH248ProtocolVersion_Type()
)
zxAnH248ProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248ProtocolVersion.setStatus("current")


class _ZxAnH248EncodingType_Type(Integer32):
    """Custom type zxAnH248EncodingType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("text", 1),
          ("binary", 2))
    )


_ZxAnH248EncodingType_Type.__name__ = "Integer32"
_ZxAnH248EncodingType_Object = MibTableColumn
zxAnH248EncodingType = _ZxAnH248EncodingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 3),
    _ZxAnH248EncodingType_Type()
)
zxAnH248EncodingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248EncodingType.setStatus("current")


class _ZxAnH248PacketTokenAbbreviated_Type(TruthValue):
    """Custom type zxAnH248PacketTokenAbbreviated based on TruthValue"""
    defaultValue = 1


_ZxAnH248PacketTokenAbbreviated_Type.__name__ = "TruthValue"
_ZxAnH248PacketTokenAbbreviated_Object = MibTableColumn
zxAnH248PacketTokenAbbreviated = _ZxAnH248PacketTokenAbbreviated_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 4),
    _ZxAnH248PacketTokenAbbreviated_Type()
)
zxAnH248PacketTokenAbbreviated.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248PacketTokenAbbreviated.setStatus("current")


class _ZxAnH248MinTransactionId_Type(Integer32):
    """Custom type zxAnH248MinTransactionId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 6000),
    )


_ZxAnH248MinTransactionId_Type.__name__ = "Integer32"
_ZxAnH248MinTransactionId_Object = MibTableColumn
zxAnH248MinTransactionId = _ZxAnH248MinTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 5),
    _ZxAnH248MinTransactionId_Type()
)
zxAnH248MinTransactionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248MinTransactionId.setStatus("current")


class _ZxAnH248MaxTransactionId_Type(Integer32):
    """Custom type zxAnH248MaxTransactionId based on Integer32"""
    defaultValue = 8000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 429496729),
    )


_ZxAnH248MaxTransactionId_Type.__name__ = "Integer32"
_ZxAnH248MaxTransactionId_Object = MibTableColumn
zxAnH248MaxTransactionId = _ZxAnH248MaxTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 6),
    _ZxAnH248MaxTransactionId_Type()
)
zxAnH248MaxTransactionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248MaxTransactionId.setStatus("current")


class _ZxAnH248SendResponseAck_Type(TruthValue):
    """Custom type zxAnH248SendResponseAck based on TruthValue"""
    defaultValue = 1


_ZxAnH248SendResponseAck_Type.__name__ = "TruthValue"
_ZxAnH248SendResponseAck_Object = MibTableColumn
zxAnH248SendResponseAck = _ZxAnH248SendResponseAck_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 7),
    _ZxAnH248SendResponseAck_Type()
)
zxAnH248SendResponseAck.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248SendResponseAck.setStatus("current")


class _ZxAnH248ResponseCacheTime_Type(Integer32):
    """Custom type zxAnH248ResponseCacheTime based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_ZxAnH248ResponseCacheTime_Type.__name__ = "Integer32"
_ZxAnH248ResponseCacheTime_Object = MibTableColumn
zxAnH248ResponseCacheTime = _ZxAnH248ResponseCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 8),
    _ZxAnH248ResponseCacheTime_Type()
)
zxAnH248ResponseCacheTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248ResponseCacheTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnH248ResponseCacheTime.setUnits("second")


class _ZxAnH248SendTransactionPending_Type(TruthValue):
    """Custom type zxAnH248SendTransactionPending based on TruthValue"""
    defaultValue = 1


_ZxAnH248SendTransactionPending_Type.__name__ = "TruthValue"
_ZxAnH248SendTransactionPending_Object = MibTableColumn
zxAnH248SendTransactionPending = _ZxAnH248SendTransactionPending_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 9),
    _ZxAnH248SendTransactionPending_Type()
)
zxAnH248SendTransactionPending.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248SendTransactionPending.setStatus("current")


class _ZxAnH248ProfileNegotiation_Type(TruthValue):
    """Custom type zxAnH248ProfileNegotiation based on TruthValue"""
    defaultValue = 2


_ZxAnH248ProfileNegotiation_Type.__name__ = "TruthValue"
_ZxAnH248ProfileNegotiation_Object = MibTableColumn
zxAnH248ProfileNegotiation = _ZxAnH248ProfileNegotiation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 10),
    _ZxAnH248ProfileNegotiation_Type()
)
zxAnH248ProfileNegotiation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248ProfileNegotiation.setStatus("current")


class _ZxAnH248RebootMaxWaitingDelay_Type(Integer32):
    """Custom type zxAnH248RebootMaxWaitingDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_ZxAnH248RebootMaxWaitingDelay_Type.__name__ = "Integer32"
_ZxAnH248RebootMaxWaitingDelay_Object = MibTableColumn
zxAnH248RebootMaxWaitingDelay = _ZxAnH248RebootMaxWaitingDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 11),
    _ZxAnH248RebootMaxWaitingDelay_Type()
)
zxAnH248RebootMaxWaitingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248RebootMaxWaitingDelay.setStatus("current")
if mibBuilder.loadTexts:
    zxAnH248RebootMaxWaitingDelay.setUnits("second")


class _ZxAnH248MgcMaxInactivityTime_Type(Integer32):
    """Custom type zxAnH248MgcMaxInactivityTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 300),
    )


_ZxAnH248MgcMaxInactivityTime_Type.__name__ = "Integer32"
_ZxAnH248MgcMaxInactivityTime_Object = MibTableColumn
zxAnH248MgcMaxInactivityTime = _ZxAnH248MgcMaxInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 12),
    _ZxAnH248MgcMaxInactivityTime_Type()
)
zxAnH248MgcMaxInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248MgcMaxInactivityTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnH248MgcMaxInactivityTime.setUnits("second")


class _ZxAnH248TranRetranMode_Type(Integer32):
    """Custom type zxAnH248TranRetranMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fixedInteval", 1),
          ("exponentialGrowthInteval", 2))
    )


_ZxAnH248TranRetranMode_Type.__name__ = "Integer32"
_ZxAnH248TranRetranMode_Object = MibTableColumn
zxAnH248TranRetranMode = _ZxAnH248TranRetranMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 13),
    _ZxAnH248TranRetranMode_Type()
)
zxAnH248TranRetranMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248TranRetranMode.setStatus("current")


class _ZxAnH248TranRetranInterval_Type(Integer32):
    """Custom type zxAnH248TranRetranInterval based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ZxAnH248TranRetranInterval_Type.__name__ = "Integer32"
_ZxAnH248TranRetranInterval_Object = MibTableColumn
zxAnH248TranRetranInterval = _ZxAnH248TranRetranInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 14),
    _ZxAnH248TranRetranInterval_Type()
)
zxAnH248TranRetranInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248TranRetranInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnH248TranRetranInterval.setUnits("second")


class _ZxAnH248TranMaxRetries_Type(Integer32):
    """Custom type zxAnH248TranMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ZxAnH248TranMaxRetries_Type.__name__ = "Integer32"
_ZxAnH248TranMaxRetries_Object = MibTableColumn
zxAnH248TranMaxRetries = _ZxAnH248TranMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 15),
    _ZxAnH248TranMaxRetries_Type()
)
zxAnH248TranMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248TranMaxRetries.setStatus("current")


class _ZxAnH248TranPendInterval_Type(Integer32):
    """Custom type zxAnH248TranPendInterval based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8),
    )


_ZxAnH248TranPendInterval_Type.__name__ = "Integer32"
_ZxAnH248TranPendInterval_Object = MibTableColumn
zxAnH248TranPendInterval = _ZxAnH248TranPendInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 16),
    _ZxAnH248TranPendInterval_Type()
)
zxAnH248TranPendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248TranPendInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnH248TranPendInterval.setUnits("second")


class _ZxAnH248TranPendLimit_Type(Integer32):
    """Custom type zxAnH248TranPendLimit based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 40),
    )


_ZxAnH248TranPendLimit_Type.__name__ = "Integer32"
_ZxAnH248TranPendLimit_Object = MibTableColumn
zxAnH248TranPendLimit = _ZxAnH248TranPendLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 17),
    _ZxAnH248TranPendLimit_Type()
)
zxAnH248TranPendLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248TranPendLimit.setStatus("current")


class _ZxAnH248HeartbeatMechanism_Type(Integer32):
    """Custom type zxAnH248HeartbeatMechanism based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("controlByMgc", 1),
          ("controlByMg", 2))
    )


_ZxAnH248HeartbeatMechanism_Type.__name__ = "Integer32"
_ZxAnH248HeartbeatMechanism_Object = MibTableColumn
zxAnH248HeartbeatMechanism = _ZxAnH248HeartbeatMechanism_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 18),
    _ZxAnH248HeartbeatMechanism_Type()
)
zxAnH248HeartbeatMechanism.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248HeartbeatMechanism.setStatus("current")


class _ZxAnH248MgcHbMaxInactivityTime_Type(Integer32):
    """Custom type zxAnH248MgcHbMaxInactivityTime based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 600),
    )


_ZxAnH248MgcHbMaxInactivityTime_Type.__name__ = "Integer32"
_ZxAnH248MgcHbMaxInactivityTime_Object = MibTableColumn
zxAnH248MgcHbMaxInactivityTime = _ZxAnH248MgcHbMaxInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 19),
    _ZxAnH248MgcHbMaxInactivityTime_Type()
)
zxAnH248MgcHbMaxInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248MgcHbMaxInactivityTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnH248MgcHbMaxInactivityTime.setUnits("second")


class _ZxAnH248HeartbeatFormat_Type(Integer32):
    """Custom type zxAnH248HeartbeatFormat based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("sv", 1),
          ("itito", 2))
    )


_ZxAnH248HeartbeatFormat_Type.__name__ = "Integer32"
_ZxAnH248HeartbeatFormat_Object = MibTableColumn
zxAnH248HeartbeatFormat = _ZxAnH248HeartbeatFormat_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 20),
    _ZxAnH248HeartbeatFormat_Type()
)
zxAnH248HeartbeatFormat.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248HeartbeatFormat.setStatus("current")


class _ZxAnH248HbRetranInterval_Type(Integer32):
    """Custom type zxAnH248HbRetranInterval based on Integer32"""
    defaultValue = 100

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ZxAnH248HbRetranInterval_Type.__name__ = "Integer32"
_ZxAnH248HbRetranInterval_Object = MibTableColumn
zxAnH248HbRetranInterval = _ZxAnH248HbRetranInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 21),
    _ZxAnH248HbRetranInterval_Type()
)
zxAnH248HbRetranInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248HbRetranInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnH248HbRetranInterval.setUnits("second")


class _ZxAnH248HbMaxRetries_Type(Integer32):
    """Custom type zxAnH248HbMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ZxAnH248HbMaxRetries_Type.__name__ = "Integer32"
_ZxAnH248HbMaxRetries_Object = MibTableColumn
zxAnH248HbMaxRetries = _ZxAnH248HbMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1111, 1, 22),
    _ZxAnH248HbMaxRetries_Type()
)
zxAnH248HbMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnH248HbMaxRetries.setStatus("current")
_ZxAnSlcTermIDTable_Object = MibTable
zxAnSlcTermIDTable = _ZxAnSlcTermIDTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120)
)
if mibBuilder.loadTexts:
    zxAnSlcTermIDTable.setStatus("current")
_ZxAnSlcTermIDEntry_Object = MibTableRow
zxAnSlcTermIDEntry = _ZxAnSlcTermIDEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1)
)
zxAnSlcTermIDEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnSlcTermIDRackNo"),
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnSlcTermIDShelfNo"),
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnSlcTermIDSlotNo"),
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnSlcTermIDBeginIndex"),
)
if mibBuilder.loadTexts:
    zxAnSlcTermIDEntry.setStatus("current")
_ZxAnSlcTermIDRackNo_Type = Integer32
_ZxAnSlcTermIDRackNo_Object = MibTableColumn
zxAnSlcTermIDRackNo = _ZxAnSlcTermIDRackNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 1),
    _ZxAnSlcTermIDRackNo_Type()
)
zxAnSlcTermIDRackNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSlcTermIDRackNo.setStatus("current")
_ZxAnSlcTermIDShelfNo_Type = Integer32
_ZxAnSlcTermIDShelfNo_Object = MibTableColumn
zxAnSlcTermIDShelfNo = _ZxAnSlcTermIDShelfNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 2),
    _ZxAnSlcTermIDShelfNo_Type()
)
zxAnSlcTermIDShelfNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSlcTermIDShelfNo.setStatus("current")
_ZxAnSlcTermIDSlotNo_Type = Integer32
_ZxAnSlcTermIDSlotNo_Object = MibTableColumn
zxAnSlcTermIDSlotNo = _ZxAnSlcTermIDSlotNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 3),
    _ZxAnSlcTermIDSlotNo_Type()
)
zxAnSlcTermIDSlotNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSlcTermIDSlotNo.setStatus("current")


class _ZxAnSlcTermIDBeginIndex_Type(Integer32):
    """Custom type zxAnSlcTermIDBeginIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 64),
    )


_ZxAnSlcTermIDBeginIndex_Type.__name__ = "Integer32"
_ZxAnSlcTermIDBeginIndex_Object = MibTableColumn
zxAnSlcTermIDBeginIndex = _ZxAnSlcTermIDBeginIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 4),
    _ZxAnSlcTermIDBeginIndex_Type()
)
zxAnSlcTermIDBeginIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnSlcTermIDBeginIndex.setStatus("current")


class _ZxAnSlcTermIDOperSum_Type(Integer32):
    """Custom type zxAnSlcTermIDOperSum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 192),
    )


_ZxAnSlcTermIDOperSum_Type.__name__ = "Integer32"
_ZxAnSlcTermIDOperSum_Object = MibTableColumn
zxAnSlcTermIDOperSum = _ZxAnSlcTermIDOperSum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 5),
    _ZxAnSlcTermIDOperSum_Type()
)
zxAnSlcTermIDOperSum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSlcTermIDOperSum.setStatus("current")


class _ZxAnSlcTermIDTMID_Type(DisplayString):
    """Custom type zxAnSlcTermIDTMID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSlcTermIDTMID_Type.__name__ = "DisplayString"
_ZxAnSlcTermIDTMID_Object = MibTableColumn
zxAnSlcTermIDTMID = _ZxAnSlcTermIDTMID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 6),
    _ZxAnSlcTermIDTMID_Type()
)
zxAnSlcTermIDTMID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSlcTermIDTMID.setStatus("current")


class _ZxAnSlcTermIDType_Type(Integer32):
    """Custom type zxAnSlcTermIDType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("type1", 1),
          ("type2", 2),
          ("type3", 3))
    )


_ZxAnSlcTermIDType_Type.__name__ = "Integer32"
_ZxAnSlcTermIDType_Object = MibTableColumn
zxAnSlcTermIDType = _ZxAnSlcTermIDType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 7),
    _ZxAnSlcTermIDType_Type()
)
zxAnSlcTermIDType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSlcTermIDType.setStatus("current")
_ZxAnSlcTermIDBeginNo_Type = Integer32
_ZxAnSlcTermIDBeginNo_Object = MibTableColumn
zxAnSlcTermIDBeginNo = _ZxAnSlcTermIDBeginNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 8),
    _ZxAnSlcTermIDBeginNo_Type()
)
zxAnSlcTermIDBeginNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSlcTermIDBeginNo.setStatus("current")


class _ZxAnSlcTermIDDigitLen_Type(Integer32):
    """Custom type zxAnSlcTermIDDigitLen based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 63),
    )


_ZxAnSlcTermIDDigitLen_Type.__name__ = "Integer32"
_ZxAnSlcTermIDDigitLen_Object = MibTableColumn
zxAnSlcTermIDDigitLen = _ZxAnSlcTermIDDigitLen_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 9),
    _ZxAnSlcTermIDDigitLen_Type()
)
zxAnSlcTermIDDigitLen.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSlcTermIDDigitLen.setStatus("current")


class _ZxAnSlcTermIDMgId_Type(Integer32):
    """Custom type zxAnSlcTermIDMgId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnSlcTermIDMgId_Type.__name__ = "Integer32"
_ZxAnSlcTermIDMgId_Object = MibTableColumn
zxAnSlcTermIDMgId = _ZxAnSlcTermIDMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 11),
    _ZxAnSlcTermIDMgId_Type()
)
zxAnSlcTermIDMgId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSlcTermIDMgId.setStatus("current")


class _ZxAnSlcTerminationID_Type(DisplayString):
    """Custom type zxAnSlcTerminationID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnSlcTerminationID_Type.__name__ = "DisplayString"
_ZxAnSlcTerminationID_Object = MibTableColumn
zxAnSlcTerminationID = _ZxAnSlcTerminationID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 12),
    _ZxAnSlcTerminationID_Type()
)
zxAnSlcTerminationID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnSlcTerminationID.setStatus("current")
_ZxAnSlcTermIDRowStatus_Type = RowStatus
_ZxAnSlcTermIDRowStatus_Object = MibTableColumn
zxAnSlcTermIDRowStatus = _ZxAnSlcTermIDRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1120, 1, 13),
    _ZxAnSlcTermIDRowStatus_Type()
)
zxAnSlcTermIDRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnSlcTermIDRowStatus.setStatus("current")
_ZxAnMgcpConfig_ObjectIdentity = ObjectIdentity
zxAnMgcpConfig = _ZxAnMgcpConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150)
)
_ZxAnMgcpMgcCfgTable_Object = MibTable
zxAnMgcpMgcCfgTable = _ZxAnMgcpMgcCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 1)
)
if mibBuilder.loadTexts:
    zxAnMgcpMgcCfgTable.setStatus("current")
_ZxAnMgcpMgcCfgEntry_Object = MibTableRow
zxAnMgcpMgcCfgEntry = _ZxAnMgcpMgcCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 1, 1)
)
zxAnMgcpMgcCfgEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnMgcpMgcId"),
)
if mibBuilder.loadTexts:
    zxAnMgcpMgcCfgEntry.setStatus("current")


class _ZxAnMgcpMgcId_Type(Integer32):
    """Custom type zxAnMgcpMgcId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 12),
    )


_ZxAnMgcpMgcId_Type.__name__ = "Integer32"
_ZxAnMgcpMgcId_Object = MibTableColumn
zxAnMgcpMgcId = _ZxAnMgcpMgcId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 1, 1, 1),
    _ZxAnMgcpMgcId_Type()
)
zxAnMgcpMgcId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMgcpMgcId.setStatus("current")


class _ZxAnMgcpMgcTypeId_Type(Integer32):
    """Custom type zxAnMgcpMgcTypeId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              7)
        )
    )
    namedValues = NamedValues(
        *(("zte", 1),
          ("hw", 2),
          ("cisco", 3),
          ("alcatel", 4),
          ("nortelMgcp", 5),
          ("siemens", 7))
    )


_ZxAnMgcpMgcTypeId_Type.__name__ = "Integer32"
_ZxAnMgcpMgcTypeId_Object = MibTableColumn
zxAnMgcpMgcTypeId = _ZxAnMgcpMgcTypeId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 1, 1, 2),
    _ZxAnMgcpMgcTypeId_Type()
)
zxAnMgcpMgcTypeId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcTypeId.setStatus("current")


class _ZxAnMgcpMgcPort_Type(Integer32):
    """Custom type zxAnMgcpMgcPort based on Integer32"""
    defaultValue = 2727

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnMgcpMgcPort_Type.__name__ = "Integer32"
_ZxAnMgcpMgcPort_Object = MibTableColumn
zxAnMgcpMgcPort = _ZxAnMgcpMgcPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 1, 1, 3),
    _ZxAnMgcpMgcPort_Type()
)
zxAnMgcpMgcPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcPort.setStatus("current")


class _ZxAnMgcpMgcIpAddrType_Type(InetAddressType):
    """Custom type zxAnMgcpMgcIpAddrType based on InetAddressType"""
    defaultValue = 1


_ZxAnMgcpMgcIpAddrType_Type.__name__ = "InetAddressType"
_ZxAnMgcpMgcIpAddrType_Object = MibTableColumn
zxAnMgcpMgcIpAddrType = _ZxAnMgcpMgcIpAddrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 1, 1, 4),
    _ZxAnMgcpMgcIpAddrType_Type()
)
zxAnMgcpMgcIpAddrType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcIpAddrType.setStatus("current")
_ZxAnMgcpMgcIpAddress_Type = InetAddress
_ZxAnMgcpMgcIpAddress_Object = MibTableColumn
zxAnMgcpMgcIpAddress = _ZxAnMgcpMgcIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 1, 1, 5),
    _ZxAnMgcpMgcIpAddress_Type()
)
zxAnMgcpMgcIpAddress.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcIpAddress.setStatus("current")


class _ZxAnMgcpMgcDomainName_Type(DisplayString):
    """Custom type zxAnMgcpMgcDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ZxAnMgcpMgcDomainName_Type.__name__ = "DisplayString"
_ZxAnMgcpMgcDomainName_Object = MibTableColumn
zxAnMgcpMgcDomainName = _ZxAnMgcpMgcDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 1, 1, 6),
    _ZxAnMgcpMgcDomainName_Type()
)
zxAnMgcpMgcDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcDomainName.setStatus("current")


class _ZxAnMgcpMgcDescription_Type(DisplayString):
    """Custom type zxAnMgcpMgcDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnMgcpMgcDescription_Type.__name__ = "DisplayString"
_ZxAnMgcpMgcDescription_Object = MibTableColumn
zxAnMgcpMgcDescription = _ZxAnMgcpMgcDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 1, 1, 7),
    _ZxAnMgcpMgcDescription_Type()
)
zxAnMgcpMgcDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcDescription.setStatus("current")
_ZxAnMgcpMgcRowStatus_Type = RowStatus
_ZxAnMgcpMgcRowStatus_Object = MibTableColumn
zxAnMgcpMgcRowStatus = _ZxAnMgcpMgcRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 1, 1, 100),
    _ZxAnMgcpMgcRowStatus_Type()
)
zxAnMgcpMgcRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcRowStatus.setStatus("current")
_ZxAnMgcpMgCfgTable_Object = MibTable
zxAnMgcpMgCfgTable = _ZxAnMgcpMgCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2)
)
if mibBuilder.loadTexts:
    zxAnMgcpMgCfgTable.setStatus("current")
_ZxAnMgcpMgCfgEntry_Object = MibTableRow
zxAnMgcpMgCfgEntry = _ZxAnMgcpMgCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1)
)
zxAnMgcpMgCfgEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnMgcpMgId"),
)
if mibBuilder.loadTexts:
    zxAnMgcpMgCfgEntry.setStatus("current")


class _ZxAnMgcpMgId_Type(Integer32):
    """Custom type zxAnMgcpMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnMgcpMgId_Type.__name__ = "Integer32"
_ZxAnMgcpMgId_Object = MibTableColumn
zxAnMgcpMgId = _ZxAnMgcpMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 1),
    _ZxAnMgcpMgId_Type()
)
zxAnMgcpMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMgcpMgId.setStatus("current")


class _ZxAnMgcpMgPort_Type(Integer32):
    """Custom type zxAnMgcpMgPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnMgcpMgPort_Type.__name__ = "Integer32"
_ZxAnMgcpMgPort_Object = MibTableColumn
zxAnMgcpMgPort = _ZxAnMgcpMgPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 2),
    _ZxAnMgcpMgPort_Type()
)
zxAnMgcpMgPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgPort.setStatus("current")


class _ZxAnMgcpMgDomainName_Type(DisplayString):
    """Custom type zxAnMgcpMgDomainName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 80),
    )


_ZxAnMgcpMgDomainName_Type.__name__ = "DisplayString"
_ZxAnMgcpMgDomainName_Object = MibTableColumn
zxAnMgcpMgDomainName = _ZxAnMgcpMgDomainName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 3),
    _ZxAnMgcpMgDomainName_Type()
)
zxAnMgcpMgDomainName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgDomainName.setStatus("current")


class _ZxAnMgcpMgDescription_Type(DisplayString):
    """Custom type zxAnMgcpMgDescription based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnMgcpMgDescription_Type.__name__ = "DisplayString"
_ZxAnMgcpMgDescription_Object = MibTableColumn
zxAnMgcpMgDescription = _ZxAnMgcpMgDescription_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 4),
    _ZxAnMgcpMgDescription_Type()
)
zxAnMgcpMgDescription.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgDescription.setStatus("current")


class _ZxAnMgcpMgcId1_Type(Integer32):
    """Custom type zxAnMgcpMgcId1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ZxAnMgcpMgcId1_Type.__name__ = "Integer32"
_ZxAnMgcpMgcId1_Object = MibTableColumn
zxAnMgcpMgcId1 = _ZxAnMgcpMgcId1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 5),
    _ZxAnMgcpMgcId1_Type()
)
zxAnMgcpMgcId1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcId1.setStatus("current")


class _ZxAnMgcpMgcId2_Type(Integer32):
    """Custom type zxAnMgcpMgcId2 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ZxAnMgcpMgcId2_Type.__name__ = "Integer32"
_ZxAnMgcpMgcId2_Object = MibTableColumn
zxAnMgcpMgcId2 = _ZxAnMgcpMgcId2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 6),
    _ZxAnMgcpMgcId2_Type()
)
zxAnMgcpMgcId2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcId2.setStatus("current")


class _ZxAnMgcpMgcId3_Type(Integer32):
    """Custom type zxAnMgcpMgcId3 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ZxAnMgcpMgcId3_Type.__name__ = "Integer32"
_ZxAnMgcpMgcId3_Object = MibTableColumn
zxAnMgcpMgcId3 = _ZxAnMgcpMgcId3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 7),
    _ZxAnMgcpMgcId3_Type()
)
zxAnMgcpMgcId3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcId3.setStatus("current")


class _ZxAnMgcpMgcId4_Type(Integer32):
    """Custom type zxAnMgcpMgcId4 based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ZxAnMgcpMgcId4_Type.__name__ = "Integer32"
_ZxAnMgcpMgcId4_Object = MibTableColumn
zxAnMgcpMgcId4 = _ZxAnMgcpMgcId4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 8),
    _ZxAnMgcpMgcId4_Type()
)
zxAnMgcpMgcId4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgcId4.setStatus("current")


class _ZxAnMgcpRtpFaxPri1_Type(Integer32):
    """Custom type zxAnMgcpRtpFaxPri1 based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faxVbd", 1),
          ("faxT38", 2))
    )


_ZxAnMgcpRtpFaxPri1_Type.__name__ = "Integer32"
_ZxAnMgcpRtpFaxPri1_Object = MibTableColumn
zxAnMgcpRtpFaxPri1 = _ZxAnMgcpRtpFaxPri1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 9),
    _ZxAnMgcpRtpFaxPri1_Type()
)
zxAnMgcpRtpFaxPri1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpRtpFaxPri1.setStatus("current")


class _ZxAnMgcpRtpFaxPri2_Type(Integer32):
    """Custom type zxAnMgcpRtpFaxPri2 based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("faxVbd", 1),
          ("faxT38", 2))
    )


_ZxAnMgcpRtpFaxPri2_Type.__name__ = "Integer32"
_ZxAnMgcpRtpFaxPri2_Object = MibTableColumn
zxAnMgcpRtpFaxPri2 = _ZxAnMgcpRtpFaxPri2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 10),
    _ZxAnMgcpRtpFaxPri2_Type()
)
zxAnMgcpRtpFaxPri2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpRtpFaxPri2.setStatus("current")


class _ZxAnMgcpMgSelfSwitch_Type(Integer32):
    """Custom type zxAnMgcpMgSelfSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMgcpMgSelfSwitch_Type.__name__ = "Integer32"
_ZxAnMgcpMgSelfSwitch_Object = MibTableColumn
zxAnMgcpMgSelfSwitch = _ZxAnMgcpMgSelfSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 11),
    _ZxAnMgcpMgSelfSwitch_Type()
)
zxAnMgcpMgSelfSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgSelfSwitch.setStatus("current")


class _ZxAnMgcpMgProtectCall_Type(Integer32):
    """Custom type zxAnMgcpMgProtectCall based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enable", 1),
          ("disable", 2))
    )


_ZxAnMgcpMgProtectCall_Type.__name__ = "Integer32"
_ZxAnMgcpMgProtectCall_Object = MibTableColumn
zxAnMgcpMgProtectCall = _ZxAnMgcpMgProtectCall_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 12),
    _ZxAnMgcpMgProtectCall_Type()
)
zxAnMgcpMgProtectCall.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgProtectCall.setStatus("current")


class _ZxAnMgcpMgRtp2833Type_Type(Integer32):
    """Custom type zxAnMgcpMgRtp2833Type based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("type2833Redun", 1),
          ("typeRtp", 2))
    )


_ZxAnMgcpMgRtp2833Type_Type.__name__ = "Integer32"
_ZxAnMgcpMgRtp2833Type_Object = MibTableColumn
zxAnMgcpMgRtp2833Type = _ZxAnMgcpMgRtp2833Type_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 13),
    _ZxAnMgcpMgRtp2833Type_Type()
)
zxAnMgcpMgRtp2833Type.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgRtp2833Type.setStatus("current")
_ZxAnMgcpMgRowStatus_Type = RowStatus
_ZxAnMgcpMgRowStatus_Object = MibTableColumn
zxAnMgcpMgRowStatus = _ZxAnMgcpMgRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 2, 1, 100),
    _ZxAnMgcpMgRowStatus_Type()
)
zxAnMgcpMgRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnMgcpMgRowStatus.setStatus("current")
_ZxAnMgcpProtocolTable_Object = MibTable
zxAnMgcpProtocolTable = _ZxAnMgcpProtocolTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3)
)
if mibBuilder.loadTexts:
    zxAnMgcpProtocolTable.setStatus("current")
_ZxAnMgcpProtocolEntry_Object = MibTableRow
zxAnMgcpProtocolEntry = _ZxAnMgcpProtocolEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1)
)
zxAnMgcpProtocolEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-H248MGCP-MIB", "zxAnMgcpProtocolMgId"),
)
if mibBuilder.loadTexts:
    zxAnMgcpProtocolEntry.setStatus("current")


class _ZxAnMgcpProtocolMgId_Type(Integer32):
    """Custom type zxAnMgcpProtocolMgId based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnMgcpProtocolMgId_Type.__name__ = "Integer32"
_ZxAnMgcpProtocolMgId_Object = MibTableColumn
zxAnMgcpProtocolMgId = _ZxAnMgcpProtocolMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1, 1),
    _ZxAnMgcpProtocolMgId_Type()
)
zxAnMgcpProtocolMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnMgcpProtocolMgId.setStatus("current")


class _ZxAnMgcpProtocolVersion_Type(Integer32):
    """Custom type zxAnMgcpProtocolVersion based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("v1", 1),
          ("v2", 2))
    )


_ZxAnMgcpProtocolVersion_Type.__name__ = "Integer32"
_ZxAnMgcpProtocolVersion_Object = MibTableColumn
zxAnMgcpProtocolVersion = _ZxAnMgcpProtocolVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1, 2),
    _ZxAnMgcpProtocolVersion_Type()
)
zxAnMgcpProtocolVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcpProtocolVersion.setStatus("current")


class _ZxAnMgcpMgcMaxInactivityTime_Type(Integer32):
    """Custom type zxAnMgcpMgcMaxInactivityTime based on Integer32"""
    defaultValue = 126

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 300),
    )


_ZxAnMgcpMgcMaxInactivityTime_Type.__name__ = "Integer32"
_ZxAnMgcpMgcMaxInactivityTime_Object = MibTableColumn
zxAnMgcpMgcMaxInactivityTime = _ZxAnMgcpMgcMaxInactivityTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1, 3),
    _ZxAnMgcpMgcMaxInactivityTime_Type()
)
zxAnMgcpMgcMaxInactivityTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcpMgcMaxInactivityTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMgcpMgcMaxInactivityTime.setUnits("second")


class _ZxAnMgcpMinTransactionId_Type(Integer32):
    """Custom type zxAnMgcpMinTransactionId based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 60000),
    )


_ZxAnMgcpMinTransactionId_Type.__name__ = "Integer32"
_ZxAnMgcpMinTransactionId_Object = MibTableColumn
zxAnMgcpMinTransactionId = _ZxAnMgcpMinTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1, 4),
    _ZxAnMgcpMinTransactionId_Type()
)
zxAnMgcpMinTransactionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcpMinTransactionId.setStatus("current")


class _ZxAnMgcpMaxTransactionId_Type(Integer32):
    """Custom type zxAnMgcpMaxTransactionId based on Integer32"""
    defaultValue = 80000

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ZxAnMgcpMaxTransactionId_Type.__name__ = "Integer32"
_ZxAnMgcpMaxTransactionId_Object = MibTableColumn
zxAnMgcpMaxTransactionId = _ZxAnMgcpMaxTransactionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1, 5),
    _ZxAnMgcpMaxTransactionId_Type()
)
zxAnMgcpMaxTransactionId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcpMaxTransactionId.setStatus("current")


class _ZxAnMgcpResponseCacheTime_Type(Integer32):
    """Custom type zxAnMgcpResponseCacheTime based on Integer32"""
    defaultValue = 12

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 30),
    )


_ZxAnMgcpResponseCacheTime_Type.__name__ = "Integer32"
_ZxAnMgcpResponseCacheTime_Object = MibTableColumn
zxAnMgcpResponseCacheTime = _ZxAnMgcpResponseCacheTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1, 6),
    _ZxAnMgcpResponseCacheTime_Type()
)
zxAnMgcpResponseCacheTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcpResponseCacheTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMgcpResponseCacheTime.setUnits("second")


class _ZxAnMgcpTranMaxRetries_Type(Integer32):
    """Custom type zxAnMgcpTranMaxRetries based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 10),
    )


_ZxAnMgcpTranMaxRetries_Type.__name__ = "Integer32"
_ZxAnMgcpTranMaxRetries_Object = MibTableColumn
zxAnMgcpTranMaxRetries = _ZxAnMgcpTranMaxRetries_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1, 7),
    _ZxAnMgcpTranMaxRetries_Type()
)
zxAnMgcpTranMaxRetries.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcpTranMaxRetries.setStatus("current")


class _ZxAnMgcpTranPendInterval_Type(Integer32):
    """Custom type zxAnMgcpTranPendInterval based on Integer32"""
    defaultValue = 4

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8),
    )


_ZxAnMgcpTranPendInterval_Type.__name__ = "Integer32"
_ZxAnMgcpTranPendInterval_Object = MibTableColumn
zxAnMgcpTranPendInterval = _ZxAnMgcpTranPendInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1, 8),
    _ZxAnMgcpTranPendInterval_Type()
)
zxAnMgcpTranPendInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcpTranPendInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMgcpTranPendInterval.setUnits("second")


class _ZxAnMgcpTranPendLimit_Type(Integer32):
    """Custom type zxAnMgcpTranPendLimit based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(20, 40),
    )


_ZxAnMgcpTranPendLimit_Type.__name__ = "Integer32"
_ZxAnMgcpTranPendLimit_Object = MibTableColumn
zxAnMgcpTranPendLimit = _ZxAnMgcpTranPendLimit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1, 9),
    _ZxAnMgcpTranPendLimit_Type()
)
zxAnMgcpTranPendLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcpTranPendLimit.setStatus("current")


class _ZxAnMgcpRebootMaxWaitingDelay_Type(Integer32):
    """Custom type zxAnMgcpRebootMaxWaitingDelay based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 600),
    )


_ZxAnMgcpRebootMaxWaitingDelay_Type.__name__ = "Integer32"
_ZxAnMgcpRebootMaxWaitingDelay_Object = MibTableColumn
zxAnMgcpRebootMaxWaitingDelay = _ZxAnMgcpRebootMaxWaitingDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1150, 3, 1, 10),
    _ZxAnMgcpRebootMaxWaitingDelay_Type()
)
zxAnMgcpRebootMaxWaitingDelay.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnMgcpRebootMaxWaitingDelay.setStatus("current")
if mibBuilder.loadTexts:
    zxAnMgcpRebootMaxWaitingDelay.setUnits("second")
_ZxAnH248Perf_ObjectIdentity = ObjectIdentity
zxAnH248Perf = _ZxAnH248Perf_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1170)
)
_ZxAnH248PSRecMsg_Type = Integer32
_ZxAnH248PSRecMsg_Object = MibScalar
zxAnH248PSRecMsg = _ZxAnH248PSRecMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1170, 1),
    _ZxAnH248PSRecMsg_Type()
)
zxAnH248PSRecMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248PSRecMsg.setStatus("current")
_ZxAnH248PSSendMsg_Type = Integer32
_ZxAnH248PSSendMsg_Object = MibScalar
zxAnH248PSSendMsg = _ZxAnH248PSSendMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1170, 2),
    _ZxAnH248PSSendMsg_Type()
)
zxAnH248PSSendMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248PSSendMsg.setStatus("current")
_ZxAnH248PSRecMsgByte_Type = Integer32
_ZxAnH248PSRecMsgByte_Object = MibScalar
zxAnH248PSRecMsgByte = _ZxAnH248PSRecMsgByte_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1170, 3),
    _ZxAnH248PSRecMsgByte_Type()
)
zxAnH248PSRecMsgByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248PSRecMsgByte.setStatus("current")
_ZxAnH248PSSendMsgByte_Type = Integer32
_ZxAnH248PSSendMsgByte_Object = MibScalar
zxAnH248PSSendMsgByte = _ZxAnH248PSSendMsgByte_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1170, 4),
    _ZxAnH248PSSendMsgByte_Type()
)
zxAnH248PSSendMsgByte.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248PSSendMsgByte.setStatus("current")
_ZxAnH248PSProtocolError_Type = Integer32
_ZxAnH248PSProtocolError_Object = MibScalar
zxAnH248PSProtocolError = _ZxAnH248PSProtocolError_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1170, 5),
    _ZxAnH248PSProtocolError_Type()
)
zxAnH248PSProtocolError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248PSProtocolError.setStatus("current")
_ZxAnH248PSTimerOut_Type = Integer32
_ZxAnH248PSTimerOut_Object = MibScalar
zxAnH248PSTimerOut = _ZxAnH248PSTimerOut_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1170, 6),
    _ZxAnH248PSTimerOut_Type()
)
zxAnH248PSTimerOut.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248PSTimerOut.setStatus("current")
_ZxAnH248PSDisconnect_Type = Integer32
_ZxAnH248PSDisconnect_Object = MibScalar
zxAnH248PSDisconnect = _ZxAnH248PSDisconnect_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1170, 7),
    _ZxAnH248PSDisconnect_Type()
)
zxAnH248PSDisconnect.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248PSDisconnect.setStatus("current")
_ZxAnH248PSMGCChange_Type = Integer32
_ZxAnH248PSMGCChange_Object = MibScalar
zxAnH248PSMGCChange = _ZxAnH248PSMGCChange_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1170, 8),
    _ZxAnH248PSMGCChange_Type()
)
zxAnH248PSMGCChange.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248PSMGCChange.setStatus("current")
_ZxAnH248PSTransmitError_Type = Integer32
_ZxAnH248PSTransmitError_Object = MibScalar
zxAnH248PSTransmitError = _ZxAnH248PSTransmitError_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1170, 9),
    _ZxAnH248PSTransmitError_Type()
)
zxAnH248PSTransmitError.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnH248PSTransmitError.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-VOICE-H248MGCP-MIB",
    **{"zte": zte,
       "zxAn": zxAn,
       "zxAnVoiceH248MgcpMib": zxAnVoiceH248MgcpMib,
       "zxAnVoiceMgmt": zxAnVoiceMgmt,
       "zxAnH248MgcpConfig": zxAnH248MgcpConfig,
       "md5InfoTable": md5InfoTable,
       "md5InfoEntry": md5InfoEntry,
       "md5infoID": md5infoID,
       "md5infoG": md5infoG,
       "md5infoKi": md5infoKi,
       "md5infoMginfo": md5infoMginfo,
       "md5infoPLenth": md5infoPLenth,
       "md5infoP": md5infoP,
       "md5infoRowStatus": md5infoRowStatus,
       "zxAnH248MgcpGlobalObjects": zxAnH248MgcpGlobalObjects,
       "zxAnH248MgcpMgmtCapabilities": zxAnH248MgcpMgmtCapabilities,
       "zxAnH248MgcpLinkStatus": zxAnH248MgcpLinkStatus,
       "zxAnMgcTypeTable": zxAnMgcTypeTable,
       "zxAnMgcTypeEntry": zxAnMgcTypeEntry,
       "zxAnMgcType": zxAnMgcType,
       "zxAnMgcRegPktWithAddress": zxAnMgcRegPktWithAddress,
       "zxAnMgcRegPktWithVersion": zxAnMgcRegPktWithVersion,
       "zxAnMgcRegPktWithDelay": zxAnMgcRegPktWithDelay,
       "zxAnMgcRegPktWithProfile": zxAnMgcRegPktWithProfile,
       "zxAnMgcRegPktWithTimeStamp": zxAnMgcRegPktWithTimeStamp,
       "zxAnMgcRegPktWithReason": zxAnMgcRegPktWithReason,
       "zxAnMgcRegPktBraceDblQuotation": zxAnMgcRegPktBraceDblQuotation,
       "zxAnMgcRegPktMethod": zxAnMgcRegPktMethod,
       "zxAnMgcRegPktVersion": zxAnMgcRegPktVersion,
       "zxAnMgcRegPktDelay": zxAnMgcRegPktDelay,
       "zxAnMgcRegPktProfile": zxAnMgcRegPktProfile,
       "zxAnMgcRegPktReason": zxAnMgcRegPktReason,
       "zxAnMgcCfgTable": zxAnMgcCfgTable,
       "zxAnMgcCfgEntry": zxAnMgcCfgEntry,
       "zxAnMgcId": zxAnMgcId,
       "zxAnMgcTypeId": zxAnMgcTypeId,
       "zxAnMgcCfgPort": zxAnMgcCfgPort,
       "zxAnMgcNamingType": zxAnMgcNamingType,
       "zxAnMgcIpAddress": zxAnMgcIpAddress,
       "zxAnMgcDomainName": zxAnMgcDomainName,
       "zxAnMgcMd5Id": zxAnMgcMd5Id,
       "zxAnMgcDescription": zxAnMgcDescription,
       "zxAnMgcRowStatus": zxAnMgcRowStatus,
       "zxAnMgCfgTable": zxAnMgCfgTable,
       "zxAnMgCfgEntry": zxAnMgCfgEntry,
       "zxAnMgId": zxAnMgId,
       "zxAnMgProtocolType": zxAnMgProtocolType,
       "zxAnMgCfgPort": zxAnMgCfgPort,
       "zxAnMgCfgDomainName": zxAnMgCfgDomainName,
       "zxAnMgDescription": zxAnMgDescription,
       "zxAnMgNamingType": zxAnMgNamingType,
       "zxAnMgcId1": zxAnMgcId1,
       "zxAnMgcId2": zxAnMgcId2,
       "zxAnMgcId3": zxAnMgcId3,
       "zxAnMgcId4": zxAnMgcId4,
       "zxAnCurrentMgcId": zxAnCurrentMgcId,
       "zxAnMgTranslay": zxAnMgTranslay,
       "zxAnMgTransProtocol": zxAnMgTransProtocol,
       "zxAnTransactionNum": zxAnTransactionNum,
       "zxAnRtpFaxPri1": zxAnRtpFaxPri1,
       "zxAnRtpFaxPri2": zxAnRtpFaxPri2,
       "zxAnSelfExchange": zxAnSelfExchange,
       "zxAnProtectCall": zxAnProtectCall,
       "zxAnRtp2833PayloadTypeCode": zxAnRtp2833PayloadTypeCode,
       "zxAnPacketMaxTransactionNumber": zxAnPacketMaxTransactionNumber,
       "zxAnHotlineWithSpace": zxAnHotlineWithSpace,
       "zxAnAlwaysReportOffhookEvent": zxAnAlwaysReportOffhookEvent,
       "zxAnAlwaysReportOnhookEvent": zxAnAlwaysReportOnhookEvent,
       "zxAnSubSuspendRtp": zxAnSubSuspendRtp,
       "zxAnDisasterProt": zxAnDisasterProt,
       "zxAnMgCfgRowStatus": zxAnMgCfgRowStatus,
       "zxAnH248ProtocolTable": zxAnH248ProtocolTable,
       "zxAnH248ProtocolEntry": zxAnH248ProtocolEntry,
       "zxAnH248ProtocolMgId": zxAnH248ProtocolMgId,
       "zxAnH248ProtocolVersion": zxAnH248ProtocolVersion,
       "zxAnH248EncodingType": zxAnH248EncodingType,
       "zxAnH248PacketTokenAbbreviated": zxAnH248PacketTokenAbbreviated,
       "zxAnH248MinTransactionId": zxAnH248MinTransactionId,
       "zxAnH248MaxTransactionId": zxAnH248MaxTransactionId,
       "zxAnH248SendResponseAck": zxAnH248SendResponseAck,
       "zxAnH248ResponseCacheTime": zxAnH248ResponseCacheTime,
       "zxAnH248SendTransactionPending": zxAnH248SendTransactionPending,
       "zxAnH248ProfileNegotiation": zxAnH248ProfileNegotiation,
       "zxAnH248RebootMaxWaitingDelay": zxAnH248RebootMaxWaitingDelay,
       "zxAnH248MgcMaxInactivityTime": zxAnH248MgcMaxInactivityTime,
       "zxAnH248TranRetranMode": zxAnH248TranRetranMode,
       "zxAnH248TranRetranInterval": zxAnH248TranRetranInterval,
       "zxAnH248TranMaxRetries": zxAnH248TranMaxRetries,
       "zxAnH248TranPendInterval": zxAnH248TranPendInterval,
       "zxAnH248TranPendLimit": zxAnH248TranPendLimit,
       "zxAnH248HeartbeatMechanism": zxAnH248HeartbeatMechanism,
       "zxAnH248MgcHbMaxInactivityTime": zxAnH248MgcHbMaxInactivityTime,
       "zxAnH248HeartbeatFormat": zxAnH248HeartbeatFormat,
       "zxAnH248HbRetranInterval": zxAnH248HbRetranInterval,
       "zxAnH248HbMaxRetries": zxAnH248HbMaxRetries,
       "zxAnSlcTermIDTable": zxAnSlcTermIDTable,
       "zxAnSlcTermIDEntry": zxAnSlcTermIDEntry,
       "zxAnSlcTermIDRackNo": zxAnSlcTermIDRackNo,
       "zxAnSlcTermIDShelfNo": zxAnSlcTermIDShelfNo,
       "zxAnSlcTermIDSlotNo": zxAnSlcTermIDSlotNo,
       "zxAnSlcTermIDBeginIndex": zxAnSlcTermIDBeginIndex,
       "zxAnSlcTermIDOperSum": zxAnSlcTermIDOperSum,
       "zxAnSlcTermIDTMID": zxAnSlcTermIDTMID,
       "zxAnSlcTermIDType": zxAnSlcTermIDType,
       "zxAnSlcTermIDBeginNo": zxAnSlcTermIDBeginNo,
       "zxAnSlcTermIDDigitLen": zxAnSlcTermIDDigitLen,
       "zxAnSlcTermIDMgId": zxAnSlcTermIDMgId,
       "zxAnSlcTerminationID": zxAnSlcTerminationID,
       "zxAnSlcTermIDRowStatus": zxAnSlcTermIDRowStatus,
       "zxAnMgcpConfig": zxAnMgcpConfig,
       "zxAnMgcpMgcCfgTable": zxAnMgcpMgcCfgTable,
       "zxAnMgcpMgcCfgEntry": zxAnMgcpMgcCfgEntry,
       "zxAnMgcpMgcId": zxAnMgcpMgcId,
       "zxAnMgcpMgcTypeId": zxAnMgcpMgcTypeId,
       "zxAnMgcpMgcPort": zxAnMgcpMgcPort,
       "zxAnMgcpMgcIpAddrType": zxAnMgcpMgcIpAddrType,
       "zxAnMgcpMgcIpAddress": zxAnMgcpMgcIpAddress,
       "zxAnMgcpMgcDomainName": zxAnMgcpMgcDomainName,
       "zxAnMgcpMgcDescription": zxAnMgcpMgcDescription,
       "zxAnMgcpMgcRowStatus": zxAnMgcpMgcRowStatus,
       "zxAnMgcpMgCfgTable": zxAnMgcpMgCfgTable,
       "zxAnMgcpMgCfgEntry": zxAnMgcpMgCfgEntry,
       "zxAnMgcpMgId": zxAnMgcpMgId,
       "zxAnMgcpMgPort": zxAnMgcpMgPort,
       "zxAnMgcpMgDomainName": zxAnMgcpMgDomainName,
       "zxAnMgcpMgDescription": zxAnMgcpMgDescription,
       "zxAnMgcpMgcId1": zxAnMgcpMgcId1,
       "zxAnMgcpMgcId2": zxAnMgcpMgcId2,
       "zxAnMgcpMgcId3": zxAnMgcpMgcId3,
       "zxAnMgcpMgcId4": zxAnMgcpMgcId4,
       "zxAnMgcpRtpFaxPri1": zxAnMgcpRtpFaxPri1,
       "zxAnMgcpRtpFaxPri2": zxAnMgcpRtpFaxPri2,
       "zxAnMgcpMgSelfSwitch": zxAnMgcpMgSelfSwitch,
       "zxAnMgcpMgProtectCall": zxAnMgcpMgProtectCall,
       "zxAnMgcpMgRtp2833Type": zxAnMgcpMgRtp2833Type,
       "zxAnMgcpMgRowStatus": zxAnMgcpMgRowStatus,
       "zxAnMgcpProtocolTable": zxAnMgcpProtocolTable,
       "zxAnMgcpProtocolEntry": zxAnMgcpProtocolEntry,
       "zxAnMgcpProtocolMgId": zxAnMgcpProtocolMgId,
       "zxAnMgcpProtocolVersion": zxAnMgcpProtocolVersion,
       "zxAnMgcpMgcMaxInactivityTime": zxAnMgcpMgcMaxInactivityTime,
       "zxAnMgcpMinTransactionId": zxAnMgcpMinTransactionId,
       "zxAnMgcpMaxTransactionId": zxAnMgcpMaxTransactionId,
       "zxAnMgcpResponseCacheTime": zxAnMgcpResponseCacheTime,
       "zxAnMgcpTranMaxRetries": zxAnMgcpTranMaxRetries,
       "zxAnMgcpTranPendInterval": zxAnMgcpTranPendInterval,
       "zxAnMgcpTranPendLimit": zxAnMgcpTranPendLimit,
       "zxAnMgcpRebootMaxWaitingDelay": zxAnMgcpRebootMaxWaitingDelay,
       "zxAnH248Perf": zxAnH248Perf,
       "zxAnH248PSRecMsg": zxAnH248PSRecMsg,
       "zxAnH248PSSendMsg": zxAnH248PSSendMsg,
       "zxAnH248PSRecMsgByte": zxAnH248PSRecMsgByte,
       "zxAnH248PSSendMsgByte": zxAnH248PSSendMsgByte,
       "zxAnH248PSProtocolError": zxAnH248PSProtocolError,
       "zxAnH248PSTimerOut": zxAnH248PSTimerOut,
       "zxAnH248PSDisconnect": zxAnH248PSDisconnect,
       "zxAnH248PSMGCChange": zxAnH248PSMGCChange,
       "zxAnH248PSTransmitError": zxAnH248PSTransmitError}
)
