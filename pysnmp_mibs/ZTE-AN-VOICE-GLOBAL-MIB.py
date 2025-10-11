# SNMP MIB module (ZTE-AN-VOICE-GLOBAL-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-AN-VOICE-GLOBAL-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:07 2025
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

zxAnVoiceGlobalMib = ModuleIdentity(
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
_ZxAnVoiceGlobalConfig_ObjectIdentity = ObjectIdentity
zxAnVoiceGlobalConfig = _ZxAnVoiceGlobalConfig_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1)
)
_MsagRingProfileTable_Object = MibTable
msagRingProfileTable = _MsagRingProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6)
)
if mibBuilder.loadTexts:
    msagRingProfileTable.setStatus("current")
_MsagRingProfileEntry_Object = MibTableRow
msagRingProfileEntry = _MsagRingProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1)
)
msagRingProfileEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "msagRPRingProfile"),
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "msagRPId"),
)
if mibBuilder.loadTexts:
    msagRingProfileEntry.setStatus("current")


class _MsagRPRingProfile_Type(Integer32):
    """Custom type msagRPRingProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              12,
              15)
        )
    )
    namedValues = NamedValues(
        *(("profMainLand", 1),
          ("profHongkong", 2),
          ("profSingapore", 3),
          ("profRussia", 4),
          ("profEurope", 5),
          ("profBELGIUM", 12),
          ("profSrilanka", 15))
    )


_MsagRPRingProfile_Type.__name__ = "Integer32"
_MsagRPRingProfile_Object = MibTableColumn
msagRPRingProfile = _MsagRPRingProfile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 1),
    _MsagRPRingProfile_Type()
)
msagRPRingProfile.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagRPRingProfile.setStatus("current")


class _MsagRPId_Type(Integer32):
    """Custom type msagRPId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 15),
    )


_MsagRPId_Type.__name__ = "Integer32"
_MsagRPId_Object = MibTableColumn
msagRPId = _MsagRPId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 2),
    _MsagRPId_Type()
)
msagRPId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    msagRPId.setStatus("current")


class _MsagRPTime_Type(Integer32):
    """Custom type msagRPTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPTime_Type.__name__ = "Integer32"
_MsagRPTime_Object = MibTableColumn
msagRPTime = _MsagRPTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 3),
    _MsagRPTime_Type()
)
msagRPTime.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPTime.setStatus("current")


class _MsagRPOn1_Type(Integer32):
    """Custom type msagRPOn1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPOn1_Type.__name__ = "Integer32"
_MsagRPOn1_Object = MibTableColumn
msagRPOn1 = _MsagRPOn1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 4),
    _MsagRPOn1_Type()
)
msagRPOn1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPOn1.setStatus("current")


class _MsagRPOff1_Type(Integer32):
    """Custom type msagRPOff1 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPOff1_Type.__name__ = "Integer32"
_MsagRPOff1_Object = MibTableColumn
msagRPOff1 = _MsagRPOff1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 5),
    _MsagRPOff1_Type()
)
msagRPOff1.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPOff1.setStatus("current")


class _MsagRPOn2_Type(Integer32):
    """Custom type msagRPOn2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPOn2_Type.__name__ = "Integer32"
_MsagRPOn2_Object = MibTableColumn
msagRPOn2 = _MsagRPOn2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 6),
    _MsagRPOn2_Type()
)
msagRPOn2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPOn2.setStatus("current")


class _MsagRPOff2_Type(Integer32):
    """Custom type msagRPOff2 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPOff2_Type.__name__ = "Integer32"
_MsagRPOff2_Object = MibTableColumn
msagRPOff2 = _MsagRPOff2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 7),
    _MsagRPOff2_Type()
)
msagRPOff2.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPOff2.setStatus("current")


class _MsagRPOn3_Type(Integer32):
    """Custom type msagRPOn3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPOn3_Type.__name__ = "Integer32"
_MsagRPOn3_Object = MibTableColumn
msagRPOn3 = _MsagRPOn3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 8),
    _MsagRPOn3_Type()
)
msagRPOn3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPOn3.setStatus("current")


class _MsagRPOff3_Type(Integer32):
    """Custom type msagRPOff3 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPOff3_Type.__name__ = "Integer32"
_MsagRPOff3_Object = MibTableColumn
msagRPOff3 = _MsagRPOff3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 9),
    _MsagRPOff3_Type()
)
msagRPOff3.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPOff3.setStatus("current")


class _MsagRPOn4_Type(Integer32):
    """Custom type msagRPOn4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPOn4_Type.__name__ = "Integer32"
_MsagRPOn4_Object = MibTableColumn
msagRPOn4 = _MsagRPOn4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 10),
    _MsagRPOn4_Type()
)
msagRPOn4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPOn4.setStatus("current")


class _MsagRPOff4_Type(Integer32):
    """Custom type msagRPOff4 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPOff4_Type.__name__ = "Integer32"
_MsagRPOff4_Object = MibTableColumn
msagRPOff4 = _MsagRPOff4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 11),
    _MsagRPOff4_Type()
)
msagRPOff4.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPOff4.setStatus("current")


class _MsagRPOn5_Type(Integer32):
    """Custom type msagRPOn5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPOn5_Type.__name__ = "Integer32"
_MsagRPOn5_Object = MibTableColumn
msagRPOn5 = _MsagRPOn5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 12),
    _MsagRPOn5_Type()
)
msagRPOn5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPOn5.setStatus("current")


class _MsagRPOff5_Type(Integer32):
    """Custom type msagRPOff5 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_MsagRPOff5_Type.__name__ = "Integer32"
_MsagRPOff5_Object = MibTableColumn
msagRPOff5 = _MsagRPOff5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 13),
    _MsagRPOff5_Type()
)
msagRPOff5.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPOff5.setStatus("current")
_MsagRPRowStatus_Type = RowStatus
_MsagRPRowStatus_Object = MibTableColumn
msagRPRowStatus = _MsagRPRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 6, 1, 14),
    _MsagRPRowStatus_Type()
)
msagRPRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    msagRPRowStatus.setStatus("current")
_ZxAnDsx1Table_Object = MibTable
zxAnDsx1Table = _ZxAnDsx1Table_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 16)
)
if mibBuilder.loadTexts:
    zxAnDsx1Table.setStatus("current")
_ZxAnDsx1Entry_Object = MibTableRow
zxAnDsx1Entry = _ZxAnDsx1Entry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 16, 1)
)
zxAnDsx1Entry.setIndexNames(
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "zxAnDsx1Rack"),
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "zxAnDsx1Shelf"),
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "zxAnDsx1Slot"),
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "zxAnDsx1LinkNo"),
)
if mibBuilder.loadTexts:
    zxAnDsx1Entry.setStatus("current")


class _ZxAnDsx1Rack_Type(Integer32):
    """Custom type zxAnDsx1Rack based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnDsx1Rack_Type.__name__ = "Integer32"
_ZxAnDsx1Rack_Object = MibTableColumn
zxAnDsx1Rack = _ZxAnDsx1Rack_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 16, 1, 1),
    _ZxAnDsx1Rack_Type()
)
zxAnDsx1Rack.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsx1Rack.setStatus("current")


class _ZxAnDsx1Shelf_Type(Integer32):
    """Custom type zxAnDsx1Shelf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 5),
    )


_ZxAnDsx1Shelf_Type.__name__ = "Integer32"
_ZxAnDsx1Shelf_Object = MibTableColumn
zxAnDsx1Shelf = _ZxAnDsx1Shelf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 16, 1, 2),
    _ZxAnDsx1Shelf_Type()
)
zxAnDsx1Shelf.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsx1Shelf.setStatus("current")


class _ZxAnDsx1Slot_Type(Integer32):
    """Custom type zxAnDsx1Slot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 24),
    )


_ZxAnDsx1Slot_Type.__name__ = "Integer32"
_ZxAnDsx1Slot_Object = MibTableColumn
zxAnDsx1Slot = _ZxAnDsx1Slot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 16, 1, 3),
    _ZxAnDsx1Slot_Type()
)
zxAnDsx1Slot.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsx1Slot.setStatus("current")


class _ZxAnDsx1LinkNo_Type(Integer32):
    """Custom type zxAnDsx1LinkNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnDsx1LinkNo_Type.__name__ = "Integer32"
_ZxAnDsx1LinkNo_Object = MibTableColumn
zxAnDsx1LinkNo = _ZxAnDsx1LinkNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 16, 1, 4),
    _ZxAnDsx1LinkNo_Type()
)
zxAnDsx1LinkNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnDsx1LinkNo.setStatus("current")


class _ZxAnDsx1Loopback_Type(Integer32):
    """Custom type zxAnDsx1Loopback based on Integer32"""
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
        *(("noLoopback", 1),
          ("localLoopback", 2),
          ("remoteLineLoopback", 3))
    )


_ZxAnDsx1Loopback_Type.__name__ = "Integer32"
_ZxAnDsx1Loopback_Object = MibTableColumn
zxAnDsx1Loopback = _ZxAnDsx1Loopback_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 16, 1, 5),
    _ZxAnDsx1Loopback_Type()
)
zxAnDsx1Loopback.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDsx1Loopback.setStatus("current")


class _ZxAnDsx1FramingMode_Type(Integer32):
    """Custom type zxAnDsx1FramingMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("withoutCrc", 1),
          ("withCrc", 2),
          ("sameAsPeers", 3))
    )


_ZxAnDsx1FramingMode_Type.__name__ = "Integer32"
_ZxAnDsx1FramingMode_Object = MibTableColumn
zxAnDsx1FramingMode = _ZxAnDsx1FramingMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 16, 1, 6),
    _ZxAnDsx1FramingMode_Type()
)
zxAnDsx1FramingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnDsx1FramingMode.setStatus("current")
_ZxAnVoiceGlobalObjects_ObjectIdentity = ObjectIdentity
zxAnVoiceGlobalObjects = _ZxAnVoiceGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1000)
)


class _ZxAnVoiceGlobalMgmtCapabilities_Type(Bits):
    """Custom type zxAnVoiceGlobalMgmtCapabilities based on Bits"""
    namedValues = NamedValues(
        ("nbPlatform", 0)
    )

_ZxAnVoiceGlobalMgmtCapabilities_Type.__name__ = "Bits"
_ZxAnVoiceGlobalMgmtCapabilities_Object = MibScalar
zxAnVoiceGlobalMgmtCapabilities = _ZxAnVoiceGlobalMgmtCapabilities_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1000, 1),
    _ZxAnVoiceGlobalMgmtCapabilities_Type()
)
zxAnVoiceGlobalMgmtCapabilities.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceGlobalMgmtCapabilities.setStatus("current")


class _ZxAnVoiceServiceLicense_Type(Bits):
    """Custom type zxAnVoiceServiceLicense based on Bits"""
    namedValues = NamedValues(
        *(("h248", 0),
          ("mgcp", 1),
          ("v5", 2),
          ("voipIsdn", 3),
          ("reserved1", 4),
          ("reserved2", 5),
          ("sip", 6))
    )

_ZxAnVoiceServiceLicense_Type.__name__ = "Bits"
_ZxAnVoiceServiceLicense_Object = MibScalar
zxAnVoiceServiceLicense = _ZxAnVoiceServiceLicense_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1000, 2),
    _ZxAnVoiceServiceLicense_Type()
)
zxAnVoiceServiceLicense.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceServiceLicense.setStatus("current")
_ZxAnVoiceSysMgmtObjects_ObjectIdentity = ObjectIdentity
zxAnVoiceSysMgmtObjects = _ZxAnVoiceSysMgmtObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1000, 10)
)


class _ZxAnVoiceSysArea_Type(Integer32):
    """Custom type zxAnVoiceSysArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              15)
        )
    )
    namedValues = NamedValues(
        *(("mainland", 1),
          ("hongkong", 2),
          ("singapore", 3),
          ("russia", 4),
          ("europe", 5),
          ("srilanka", 15))
    )


_ZxAnVoiceSysArea_Type.__name__ = "Integer32"
_ZxAnVoiceSysArea_Object = MibScalar
zxAnVoiceSysArea = _ZxAnVoiceSysArea_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1000, 10, 1),
    _ZxAnVoiceSysArea_Type()
)
zxAnVoiceSysArea.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceSysArea.setStatus("current")


class _ZxAnVoiceSysCallMatchType_Type(Integer32):
    """Custom type zxAnVoiceSysCallMatchType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("longMatch", 1),
          ("shortMatch", 2))
    )


_ZxAnVoiceSysCallMatchType_Type.__name__ = "Integer32"
_ZxAnVoiceSysCallMatchType_Object = MibScalar
zxAnVoiceSysCallMatchType = _ZxAnVoiceSysCallMatchType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1000, 10, 2),
    _ZxAnVoiceSysCallMatchType_Type()
)
zxAnVoiceSysCallMatchType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceSysCallMatchType.setStatus("current")


class _ZxAnVoiceSysLoadDftRingProfile_Type(Integer32):
    """Custom type zxAnVoiceSysLoadDftRingProfile based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("load", 1)
    )


_ZxAnVoiceSysLoadDftRingProfile_Type.__name__ = "Integer32"
_ZxAnVoiceSysLoadDftRingProfile_Object = MibScalar
zxAnVoiceSysLoadDftRingProfile = _ZxAnVoiceSysLoadDftRingProfile_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1000, 10, 3),
    _ZxAnVoiceSysLoadDftRingProfile_Type()
)
zxAnVoiceSysLoadDftRingProfile.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceSysLoadDftRingProfile.setStatus("current")
_ZxAnVoiceFirstRingingTable_Object = MibTable
zxAnVoiceFirstRingingTable = _ZxAnVoiceFirstRingingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1002)
)
if mibBuilder.loadTexts:
    zxAnVoiceFirstRingingTable.setStatus("current")
_ZxAnVoiceFirstRingingEntry_Object = MibTableRow
zxAnVoiceFirstRingingEntry = _ZxAnVoiceFirstRingingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1002, 1)
)
zxAnVoiceFirstRingingEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "zxAnVoiceFirstRingingMgId"),
)
if mibBuilder.loadTexts:
    zxAnVoiceFirstRingingEntry.setStatus("current")
_ZxAnVoiceFirstRingingMgId_Type = Integer32
_ZxAnVoiceFirstRingingMgId_Object = MibTableColumn
zxAnVoiceFirstRingingMgId = _ZxAnVoiceFirstRingingMgId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1002, 1, 1),
    _ZxAnVoiceFirstRingingMgId_Type()
)
zxAnVoiceFirstRingingMgId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoiceFirstRingingMgId.setStatus("current")


class _ZxAnVoiceFirstRingingType_Type(Integer32):
    """Custom type zxAnVoiceFirstRingingType based on Integer32"""
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
        *(("accordingToCid", 1),
          ("differentFromOtherRings", 2),
          ("sameWithOtherRings", 3))
    )


_ZxAnVoiceFirstRingingType_Type.__name__ = "Integer32"
_ZxAnVoiceFirstRingingType_Object = MibTableColumn
zxAnVoiceFirstRingingType = _ZxAnVoiceFirstRingingType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1002, 1, 2),
    _ZxAnVoiceFirstRingingType_Type()
)
zxAnVoiceFirstRingingType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceFirstRingingType.setStatus("current")


class _ZxAnVoiceFirstRingingTime_Type(Integer32):
    """Custom type zxAnVoiceFirstRingingTime based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 120),
    )


_ZxAnVoiceFirstRingingTime_Type.__name__ = "Integer32"
_ZxAnVoiceFirstRingingTime_Object = MibTableColumn
zxAnVoiceFirstRingingTime = _ZxAnVoiceFirstRingingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1002, 1, 3),
    _ZxAnVoiceFirstRingingTime_Type()
)
zxAnVoiceFirstRingingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceFirstRingingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceFirstRingingTime.setUnits("10ms")


class _ZxAnVoiceFirstRingingInterval_Type(Integer32):
    """Custom type zxAnVoiceFirstRingingInterval based on Integer32"""
    defaultValue = 400

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(200, 400),
    )


_ZxAnVoiceFirstRingingInterval_Type.__name__ = "Integer32"
_ZxAnVoiceFirstRingingInterval_Object = MibTableColumn
zxAnVoiceFirstRingingInterval = _ZxAnVoiceFirstRingingInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1002, 1, 4),
    _ZxAnVoiceFirstRingingInterval_Type()
)
zxAnVoiceFirstRingingInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceFirstRingingInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceFirstRingingInterval.setUnits("10ms")
_ZxAnVoiceToneProfileTable_Object = MibTable
zxAnVoiceToneProfileTable = _ZxAnVoiceToneProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003)
)
if mibBuilder.loadTexts:
    zxAnVoiceToneProfileTable.setStatus("current")
_ZxAnVoiceToneProfileEntry_Object = MibTableRow
zxAnVoiceToneProfileEntry = _ZxAnVoiceToneProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1)
)
zxAnVoiceToneProfileEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "zxAnVoiceToneArea"),
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "zxAnVoiceToneCategory"),
)
if mibBuilder.loadTexts:
    zxAnVoiceToneProfileEntry.setStatus("current")


class _ZxAnVoiceToneArea_Type(Integer32):
    """Custom type zxAnVoiceToneArea based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              15)
        )
    )
    namedValues = NamedValues(
        *(("mainland", 1),
          ("hongkong", 2),
          ("singapore", 3),
          ("russia", 4),
          ("europe", 5),
          ("srilanka", 15))
    )


_ZxAnVoiceToneArea_Type.__name__ = "Integer32"
_ZxAnVoiceToneArea_Object = MibTableColumn
zxAnVoiceToneArea = _ZxAnVoiceToneArea_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 1),
    _ZxAnVoiceToneArea_Type()
)
zxAnVoiceToneArea.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoiceToneArea.setStatus("current")


class _ZxAnVoiceToneCategory_Type(Integer32):
    """Custom type zxAnVoiceToneCategory based on Integer32"""
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
              10013,
              10014,
              10015,
              10016,
              10017,
              10018,
              10019,
              10020,
              10021,
              10025,
              10031,
              10032,
              10033,
              10035,
              10036,
              10037,
              10038,
              10039)
        )
    )
    namedValues = NamedValues(
        *(("dialTone", 1),
          ("ringbackTone", 2),
          ("busyTone", 3),
          ("congestionTone", 4),
          ("specialDialTone", 5),
          ("howlerTone", 6),
          ("verificationTone", 7),
          ("callWaitingTone", 8),
          ("stutterDialTone", 9),
          ("numberUnobtainableTone", 10),
          ("recallDialTone", 11),
          ("holdingTone", 12),
          ("callWaitingToneA", 10013),
          ("callWaitingToneB", 10014),
          ("callWaitingToneC", 10015),
          ("callWaitingToneD", 10016),
          ("callWaitingToneE", 10017),
          ("expensiveRouteWarningTone", 10018),
          ("bargeInTone", 10019),
          ("testNumberTone", 10020),
          ("intrusionTone", 10021),
          ("sitTone", 10025),
          ("busyHowlerTone", 10031),
          ("conferenceNoReadyTone", 10032),
          ("conferenceExitTone", 10033),
          ("advancedSpecialInfoTone", 10035),
          ("trunkBusyTone", 10036),
          ("advancedHoldingTone", 10037),
          ("interventionTone", 10038),
          ("wrongDialTone", 10039))
    )


_ZxAnVoiceToneCategory_Type.__name__ = "Integer32"
_ZxAnVoiceToneCategory_Object = MibTableColumn
zxAnVoiceToneCategory = _ZxAnVoiceToneCategory_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 2),
    _ZxAnVoiceToneCategory_Type()
)
zxAnVoiceToneCategory.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoiceToneCategory.setStatus("current")


class _ZxAnVoiceToneDuration_Type(Integer32):
    """Custom type zxAnVoiceToneDuration based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnVoiceToneDuration_Type.__name__ = "Integer32"
_ZxAnVoiceToneDuration_Object = MibTableColumn
zxAnVoiceToneDuration = _ZxAnVoiceToneDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 3),
    _ZxAnVoiceToneDuration_Type()
)
zxAnVoiceToneDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceToneDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceToneDuration.setUnits("100ms")


class _ZxAnVoiceToneFirstWaveFrequency_Type(Integer32):
    """Custom type zxAnVoiceToneFirstWaveFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoiceToneFirstWaveFrequency_Type.__name__ = "Integer32"
_ZxAnVoiceToneFirstWaveFrequency_Object = MibTableColumn
zxAnVoiceToneFirstWaveFrequency = _ZxAnVoiceToneFirstWaveFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 4),
    _ZxAnVoiceToneFirstWaveFrequency_Type()
)
zxAnVoiceToneFirstWaveFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceToneFirstWaveFrequency.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceToneFirstWaveFrequency.setUnits("Hz")


class _ZxAnVoiceToneFirstWaveAmplitude_Type(Integer32):
    """Custom type zxAnVoiceToneFirstWaveAmplitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ZxAnVoiceToneFirstWaveAmplitude_Type.__name__ = "Integer32"
_ZxAnVoiceToneFirstWaveAmplitude_Object = MibTableColumn
zxAnVoiceToneFirstWaveAmplitude = _ZxAnVoiceToneFirstWaveAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 5),
    _ZxAnVoiceToneFirstWaveAmplitude_Type()
)
zxAnVoiceToneFirstWaveAmplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceToneFirstWaveAmplitude.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceToneFirstWaveAmplitude.setUnits("0.1dBov")


class _ZxAnVoiceToneSecondWaveFrequency_Type(Integer32):
    """Custom type zxAnVoiceToneSecondWaveFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoiceToneSecondWaveFrequency_Type.__name__ = "Integer32"
_ZxAnVoiceToneSecondWaveFrequency_Object = MibTableColumn
zxAnVoiceToneSecondWaveFrequency = _ZxAnVoiceToneSecondWaveFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 6),
    _ZxAnVoiceToneSecondWaveFrequency_Type()
)
zxAnVoiceToneSecondWaveFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceToneSecondWaveFrequency.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceToneSecondWaveFrequency.setUnits("Hz")


class _ZxAnVoiceToneSecondWaveAmplitude_Type(Integer32):
    """Custom type zxAnVoiceToneSecondWaveAmplitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ZxAnVoiceToneSecondWaveAmplitude_Type.__name__ = "Integer32"
_ZxAnVoiceToneSecondWaveAmplitude_Object = MibTableColumn
zxAnVoiceToneSecondWaveAmplitude = _ZxAnVoiceToneSecondWaveAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 7),
    _ZxAnVoiceToneSecondWaveAmplitude_Type()
)
zxAnVoiceToneSecondWaveAmplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceToneSecondWaveAmplitude.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceToneSecondWaveAmplitude.setUnits("0.1dBov")


class _ZxAnVoiceToneThirdWaveFrequency_Type(Integer32):
    """Custom type zxAnVoiceToneThirdWaveFrequency based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoiceToneThirdWaveFrequency_Type.__name__ = "Integer32"
_ZxAnVoiceToneThirdWaveFrequency_Object = MibTableColumn
zxAnVoiceToneThirdWaveFrequency = _ZxAnVoiceToneThirdWaveFrequency_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 8),
    _ZxAnVoiceToneThirdWaveFrequency_Type()
)
zxAnVoiceToneThirdWaveFrequency.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceToneThirdWaveFrequency.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceToneThirdWaveFrequency.setUnits("Hz")


class _ZxAnVoiceToneThirdWaveAmplitude_Type(Integer32):
    """Custom type zxAnVoiceToneThirdWaveAmplitude based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1000),
    )


_ZxAnVoiceToneThirdWaveAmplitude_Type.__name__ = "Integer32"
_ZxAnVoiceToneThirdWaveAmplitude_Object = MibTableColumn
zxAnVoiceToneThirdWaveAmplitude = _ZxAnVoiceToneThirdWaveAmplitude_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 9),
    _ZxAnVoiceToneThirdWaveAmplitude_Type()
)
zxAnVoiceToneThirdWaveAmplitude.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceToneThirdWaveAmplitude.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceToneThirdWaveAmplitude.setUnits("0.1dBov")


class _ZxAnVoicFirstWaveTimeSlot_Type(Integer32):
    """Custom type zxAnVoicFirstWaveTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnVoicFirstWaveTimeSlot_Type.__name__ = "Integer32"
_ZxAnVoicFirstWaveTimeSlot_Object = MibTableColumn
zxAnVoicFirstWaveTimeSlot = _ZxAnVoicFirstWaveTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 10),
    _ZxAnVoicFirstWaveTimeSlot_Type()
)
zxAnVoicFirstWaveTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoicFirstWaveTimeSlot.setStatus("current")


class _ZxAnVoicSecondWaveTimeSlot_Type(Integer32):
    """Custom type zxAnVoicSecondWaveTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnVoicSecondWaveTimeSlot_Type.__name__ = "Integer32"
_ZxAnVoicSecondWaveTimeSlot_Object = MibTableColumn
zxAnVoicSecondWaveTimeSlot = _ZxAnVoicSecondWaveTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 11),
    _ZxAnVoicSecondWaveTimeSlot_Type()
)
zxAnVoicSecondWaveTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoicSecondWaveTimeSlot.setStatus("current")


class _ZxAnVoicThirdWaveTimeSlot_Type(Integer32):
    """Custom type zxAnVoicThirdWaveTimeSlot based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnVoicThirdWaveTimeSlot_Type.__name__ = "Integer32"
_ZxAnVoicThirdWaveTimeSlot_Object = MibTableColumn
zxAnVoicThirdWaveTimeSlot = _ZxAnVoicThirdWaveTimeSlot_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 12),
    _ZxAnVoicThirdWaveTimeSlot_Type()
)
zxAnVoicThirdWaveTimeSlot.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoicThirdWaveTimeSlot.setStatus("current")


class _ZxAnVoiceFirstToneSendingTime_Type(Integer32):
    """Custom type zxAnVoiceFirstToneSendingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoiceFirstToneSendingTime_Type.__name__ = "Integer32"
_ZxAnVoiceFirstToneSendingTime_Object = MibTableColumn
zxAnVoiceFirstToneSendingTime = _ZxAnVoiceFirstToneSendingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 13),
    _ZxAnVoiceFirstToneSendingTime_Type()
)
zxAnVoiceFirstToneSendingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceFirstToneSendingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceFirstToneSendingTime.setUnits("10ms")


class _ZxAnVoiceFirstToneBreakTime_Type(Integer32):
    """Custom type zxAnVoiceFirstToneBreakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoiceFirstToneBreakTime_Type.__name__ = "Integer32"
_ZxAnVoiceFirstToneBreakTime_Object = MibTableColumn
zxAnVoiceFirstToneBreakTime = _ZxAnVoiceFirstToneBreakTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 14),
    _ZxAnVoiceFirstToneBreakTime_Type()
)
zxAnVoiceFirstToneBreakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceFirstToneBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceFirstToneBreakTime.setUnits("10ms")


class _ZxAnVoiceSecondToneSendingTime_Type(Integer32):
    """Custom type zxAnVoiceSecondToneSendingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoiceSecondToneSendingTime_Type.__name__ = "Integer32"
_ZxAnVoiceSecondToneSendingTime_Object = MibTableColumn
zxAnVoiceSecondToneSendingTime = _ZxAnVoiceSecondToneSendingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 15),
    _ZxAnVoiceSecondToneSendingTime_Type()
)
zxAnVoiceSecondToneSendingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceSecondToneSendingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceSecondToneSendingTime.setUnits("10ms")


class _ZxAnVoiceSecondToneBreakTime_Type(Integer32):
    """Custom type zxAnVoiceSecondToneBreakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoiceSecondToneBreakTime_Type.__name__ = "Integer32"
_ZxAnVoiceSecondToneBreakTime_Object = MibTableColumn
zxAnVoiceSecondToneBreakTime = _ZxAnVoiceSecondToneBreakTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 16),
    _ZxAnVoiceSecondToneBreakTime_Type()
)
zxAnVoiceSecondToneBreakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceSecondToneBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceSecondToneBreakTime.setUnits("10ms")


class _ZxAnVoiceThirdToneSendingTime_Type(Integer32):
    """Custom type zxAnVoiceThirdToneSendingTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoiceThirdToneSendingTime_Type.__name__ = "Integer32"
_ZxAnVoiceThirdToneSendingTime_Object = MibTableColumn
zxAnVoiceThirdToneSendingTime = _ZxAnVoiceThirdToneSendingTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 17),
    _ZxAnVoiceThirdToneSendingTime_Type()
)
zxAnVoiceThirdToneSendingTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceThirdToneSendingTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceThirdToneSendingTime.setUnits("10ms")


class _ZxAnVoiceThirdToneBreakTime_Type(Integer32):
    """Custom type zxAnVoiceThirdToneBreakTime based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoiceThirdToneBreakTime_Type.__name__ = "Integer32"
_ZxAnVoiceThirdToneBreakTime_Object = MibTableColumn
zxAnVoiceThirdToneBreakTime = _ZxAnVoiceThirdToneBreakTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1003, 1, 18),
    _ZxAnVoiceThirdToneBreakTime_Type()
)
zxAnVoiceThirdToneBreakTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnVoiceThirdToneBreakTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnVoiceThirdToneBreakTime.setUnits("10ms")
_ZxAnVoiceCtrlPortTable_Object = MibTable
zxAnVoiceCtrlPortTable = _ZxAnVoiceCtrlPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1004)
)
if mibBuilder.loadTexts:
    zxAnVoiceCtrlPortTable.setStatus("current")
_ZxAnVoiceCtrlPortEntry_Object = MibTableRow
zxAnVoiceCtrlPortEntry = _ZxAnVoiceCtrlPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1004, 1)
)
zxAnVoiceCtrlPortEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "zxAnVoiceCtrlPortId"),
)
if mibBuilder.loadTexts:
    zxAnVoiceCtrlPortEntry.setStatus("current")


class _ZxAnVoiceCtrlPortId_Type(Integer32):
    """Custom type zxAnVoiceCtrlPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 40),
    )


_ZxAnVoiceCtrlPortId_Type.__name__ = "Integer32"
_ZxAnVoiceCtrlPortId_Object = MibTableColumn
zxAnVoiceCtrlPortId = _ZxAnVoiceCtrlPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1004, 1, 1),
    _ZxAnVoiceCtrlPortId_Type()
)
zxAnVoiceCtrlPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoiceCtrlPortId.setStatus("current")


class _ZxAnVoiceCtrlPortType_Type(Integer32):
    """Custom type zxAnVoiceCtrlPortType based on Integer32"""
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


_ZxAnVoiceCtrlPortType_Type.__name__ = "Integer32"
_ZxAnVoiceCtrlPortType_Object = MibTableColumn
zxAnVoiceCtrlPortType = _ZxAnVoiceCtrlPortType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1004, 1, 2),
    _ZxAnVoiceCtrlPortType_Type()
)
zxAnVoiceCtrlPortType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoiceCtrlPortType.setStatus("current")


class _ZxAnVoiceCtrlPortNo_Type(Integer32):
    """Custom type zxAnVoiceCtrlPortNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnVoiceCtrlPortNo_Type.__name__ = "Integer32"
_ZxAnVoiceCtrlPortNo_Object = MibTableColumn
zxAnVoiceCtrlPortNo = _ZxAnVoiceCtrlPortNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1004, 1, 3),
    _ZxAnVoiceCtrlPortNo_Type()
)
zxAnVoiceCtrlPortNo.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoiceCtrlPortNo.setStatus("current")
_ZxAnVoiceCtrlPortRowStatus_Type = RowStatus
_ZxAnVoiceCtrlPortRowStatus_Object = MibTableColumn
zxAnVoiceCtrlPortRowStatus = _ZxAnVoiceCtrlPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1004, 1, 20),
    _ZxAnVoiceCtrlPortRowStatus_Type()
)
zxAnVoiceCtrlPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoiceCtrlPortRowStatus.setStatus("current")
_ZxAnVoiceDigitMapTable_Object = MibTable
zxAnVoiceDigitMapTable = _ZxAnVoiceDigitMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1005)
)
if mibBuilder.loadTexts:
    zxAnVoiceDigitMapTable.setStatus("current")
_ZxAnVoiceDigitMapEntry_Object = MibTableRow
zxAnVoiceDigitMapEntry = _ZxAnVoiceDigitMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1005, 1)
)
zxAnVoiceDigitMapEntry.setIndexNames(
    (0, "ZTE-AN-VOICE-GLOBAL-MIB", "zxAnVoiceDigitMapName"),
)
if mibBuilder.loadTexts:
    zxAnVoiceDigitMapEntry.setStatus("current")


class _ZxAnVoiceDigitMapName_Type(DisplayString):
    """Custom type zxAnVoiceDigitMapName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 20),
    )


_ZxAnVoiceDigitMapName_Type.__name__ = "DisplayString"
_ZxAnVoiceDigitMapName_Object = MibTableColumn
zxAnVoiceDigitMapName = _ZxAnVoiceDigitMapName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1005, 1, 1),
    _ZxAnVoiceDigitMapName_Type()
)
zxAnVoiceDigitMapName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnVoiceDigitMapName.setStatus("current")


class _ZxAnVoiceDigitMapType_Type(Integer32):
    """Custom type zxAnVoiceDigitMapType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("selfSwitch", 1),
          ("sip", 2),
          ("emergencyCall", 3))
    )


_ZxAnVoiceDigitMapType_Type.__name__ = "Integer32"
_ZxAnVoiceDigitMapType_Object = MibTableColumn
zxAnVoiceDigitMapType = _ZxAnVoiceDigitMapType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1005, 1, 2),
    _ZxAnVoiceDigitMapType_Type()
)
zxAnVoiceDigitMapType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoiceDigitMapType.setStatus("current")


class _ZxAnVoiceDigitMapBody_Type(DisplayString):
    """Custom type zxAnVoiceDigitMapBody based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 4095),
    )


_ZxAnVoiceDigitMapBody_Type.__name__ = "DisplayString"
_ZxAnVoiceDigitMapBody_Object = MibTableColumn
zxAnVoiceDigitMapBody = _ZxAnVoiceDigitMapBody_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1005, 1, 3),
    _ZxAnVoiceDigitMapBody_Type()
)
zxAnVoiceDigitMapBody.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoiceDigitMapBody.setStatus("current")
_ZxAnVoiceDigitMapRowStatus_Type = RowStatus
_ZxAnVoiceDigitMapRowStatus_Object = MibTableColumn
zxAnVoiceDigitMapRowStatus = _ZxAnVoiceDigitMapRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1005, 1, 30),
    _ZxAnVoiceDigitMapRowStatus_Type()
)
zxAnVoiceDigitMapRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnVoiceDigitMapRowStatus.setStatus("current")
_ZxAnVoicePortNumberStatsObjects_ObjectIdentity = ObjectIdentity
zxAnVoicePortNumberStatsObjects = _ZxAnVoicePortNumberStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050)
)
_ZxAnVoiceActivePortStatsObjects_ObjectIdentity = ObjectIdentity
zxAnVoiceActivePortStatsObjects = _ZxAnVoiceActivePortStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1)
)
_ZxAnVoiceActiveV5PotsPorts_Type = Integer32
_ZxAnVoiceActiveV5PotsPorts_Object = MibScalar
zxAnVoiceActiveV5PotsPorts = _ZxAnVoiceActiveV5PotsPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1, 1),
    _ZxAnVoiceActiveV5PotsPorts_Type()
)
zxAnVoiceActiveV5PotsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceActiveV5PotsPorts.setStatus("current")
_ZxAnVoiceActiveV5BriPorts_Type = Integer32
_ZxAnVoiceActiveV5BriPorts_Object = MibScalar
zxAnVoiceActiveV5BriPorts = _ZxAnVoiceActiveV5BriPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1, 2),
    _ZxAnVoiceActiveV5BriPorts_Type()
)
zxAnVoiceActiveV5BriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceActiveV5BriPorts.setStatus("current")
_ZxAnVoiceActiveV5PriPorts_Type = Integer32
_ZxAnVoiceActiveV5PriPorts_Object = MibScalar
zxAnVoiceActiveV5PriPorts = _ZxAnVoiceActiveV5PriPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1, 3),
    _ZxAnVoiceActiveV5PriPorts_Type()
)
zxAnVoiceActiveV5PriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceActiveV5PriPorts.setStatus("current")
_ZxAnVoiceActiveH248PotsPorts_Type = Integer32
_ZxAnVoiceActiveH248PotsPorts_Object = MibScalar
zxAnVoiceActiveH248PotsPorts = _ZxAnVoiceActiveH248PotsPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1, 4),
    _ZxAnVoiceActiveH248PotsPorts_Type()
)
zxAnVoiceActiveH248PotsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceActiveH248PotsPorts.setStatus("current")
_ZxAnVoiceActiveH248BriPorts_Type = Integer32
_ZxAnVoiceActiveH248BriPorts_Object = MibScalar
zxAnVoiceActiveH248BriPorts = _ZxAnVoiceActiveH248BriPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1, 5),
    _ZxAnVoiceActiveH248BriPorts_Type()
)
zxAnVoiceActiveH248BriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceActiveH248BriPorts.setStatus("current")
_ZxAnVoiceActiveH248PriPorts_Type = Integer32
_ZxAnVoiceActiveH248PriPorts_Object = MibScalar
zxAnVoiceActiveH248PriPorts = _ZxAnVoiceActiveH248PriPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1, 6),
    _ZxAnVoiceActiveH248PriPorts_Type()
)
zxAnVoiceActiveH248PriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceActiveH248PriPorts.setStatus("current")
_ZxAnVoiceActiveSipPotsPorts_Type = Integer32
_ZxAnVoiceActiveSipPotsPorts_Object = MibScalar
zxAnVoiceActiveSipPotsPorts = _ZxAnVoiceActiveSipPotsPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1, 7),
    _ZxAnVoiceActiveSipPotsPorts_Type()
)
zxAnVoiceActiveSipPotsPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceActiveSipPotsPorts.setStatus("current")
_ZxAnVoiceActiveSipBriPorts_Type = Integer32
_ZxAnVoiceActiveSipBriPorts_Object = MibScalar
zxAnVoiceActiveSipBriPorts = _ZxAnVoiceActiveSipBriPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1, 8),
    _ZxAnVoiceActiveSipBriPorts_Type()
)
zxAnVoiceActiveSipBriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceActiveSipBriPorts.setStatus("current")
_ZxAnVoiceActiveSipPriPorts_Type = Integer32
_ZxAnVoiceActiveSipPriPorts_Object = MibScalar
zxAnVoiceActiveSipPriPorts = _ZxAnVoiceActiveSipPriPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1, 9),
    _ZxAnVoiceActiveSipPriPorts_Type()
)
zxAnVoiceActiveSipPriPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceActiveSipPriPorts.setStatus("current")
_ZxAnVoiceActiveLeasedLinePorts_Type = Integer32
_ZxAnVoiceActiveLeasedLinePorts_Object = MibScalar
zxAnVoiceActiveLeasedLinePorts = _ZxAnVoiceActiveLeasedLinePorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 5200, 3, 1, 1050, 1, 10),
    _ZxAnVoiceActiveLeasedLinePorts_Type()
)
zxAnVoiceActiveLeasedLinePorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnVoiceActiveLeasedLinePorts.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-AN-VOICE-GLOBAL-MIB",
    **{"zte": zte,
       "zxAn": zxAn,
       "zxAnVoiceGlobalMib": zxAnVoiceGlobalMib,
       "zxAnVoiceMgmt": zxAnVoiceMgmt,
       "zxAnVoiceGlobalConfig": zxAnVoiceGlobalConfig,
       "msagRingProfileTable": msagRingProfileTable,
       "msagRingProfileEntry": msagRingProfileEntry,
       "msagRPRingProfile": msagRPRingProfile,
       "msagRPId": msagRPId,
       "msagRPTime": msagRPTime,
       "msagRPOn1": msagRPOn1,
       "msagRPOff1": msagRPOff1,
       "msagRPOn2": msagRPOn2,
       "msagRPOff2": msagRPOff2,
       "msagRPOn3": msagRPOn3,
       "msagRPOff3": msagRPOff3,
       "msagRPOn4": msagRPOn4,
       "msagRPOff4": msagRPOff4,
       "msagRPOn5": msagRPOn5,
       "msagRPOff5": msagRPOff5,
       "msagRPRowStatus": msagRPRowStatus,
       "zxAnDsx1Table": zxAnDsx1Table,
       "zxAnDsx1Entry": zxAnDsx1Entry,
       "zxAnDsx1Rack": zxAnDsx1Rack,
       "zxAnDsx1Shelf": zxAnDsx1Shelf,
       "zxAnDsx1Slot": zxAnDsx1Slot,
       "zxAnDsx1LinkNo": zxAnDsx1LinkNo,
       "zxAnDsx1Loopback": zxAnDsx1Loopback,
       "zxAnDsx1FramingMode": zxAnDsx1FramingMode,
       "zxAnVoiceGlobalObjects": zxAnVoiceGlobalObjects,
       "zxAnVoiceGlobalMgmtCapabilities": zxAnVoiceGlobalMgmtCapabilities,
       "zxAnVoiceServiceLicense": zxAnVoiceServiceLicense,
       "zxAnVoiceSysMgmtObjects": zxAnVoiceSysMgmtObjects,
       "zxAnVoiceSysArea": zxAnVoiceSysArea,
       "zxAnVoiceSysCallMatchType": zxAnVoiceSysCallMatchType,
       "zxAnVoiceSysLoadDftRingProfile": zxAnVoiceSysLoadDftRingProfile,
       "zxAnVoiceFirstRingingTable": zxAnVoiceFirstRingingTable,
       "zxAnVoiceFirstRingingEntry": zxAnVoiceFirstRingingEntry,
       "zxAnVoiceFirstRingingMgId": zxAnVoiceFirstRingingMgId,
       "zxAnVoiceFirstRingingType": zxAnVoiceFirstRingingType,
       "zxAnVoiceFirstRingingTime": zxAnVoiceFirstRingingTime,
       "zxAnVoiceFirstRingingInterval": zxAnVoiceFirstRingingInterval,
       "zxAnVoiceToneProfileTable": zxAnVoiceToneProfileTable,
       "zxAnVoiceToneProfileEntry": zxAnVoiceToneProfileEntry,
       "zxAnVoiceToneArea": zxAnVoiceToneArea,
       "zxAnVoiceToneCategory": zxAnVoiceToneCategory,
       "zxAnVoiceToneDuration": zxAnVoiceToneDuration,
       "zxAnVoiceToneFirstWaveFrequency": zxAnVoiceToneFirstWaveFrequency,
       "zxAnVoiceToneFirstWaveAmplitude": zxAnVoiceToneFirstWaveAmplitude,
       "zxAnVoiceToneSecondWaveFrequency": zxAnVoiceToneSecondWaveFrequency,
       "zxAnVoiceToneSecondWaveAmplitude": zxAnVoiceToneSecondWaveAmplitude,
       "zxAnVoiceToneThirdWaveFrequency": zxAnVoiceToneThirdWaveFrequency,
       "zxAnVoiceToneThirdWaveAmplitude": zxAnVoiceToneThirdWaveAmplitude,
       "zxAnVoicFirstWaveTimeSlot": zxAnVoicFirstWaveTimeSlot,
       "zxAnVoicSecondWaveTimeSlot": zxAnVoicSecondWaveTimeSlot,
       "zxAnVoicThirdWaveTimeSlot": zxAnVoicThirdWaveTimeSlot,
       "zxAnVoiceFirstToneSendingTime": zxAnVoiceFirstToneSendingTime,
       "zxAnVoiceFirstToneBreakTime": zxAnVoiceFirstToneBreakTime,
       "zxAnVoiceSecondToneSendingTime": zxAnVoiceSecondToneSendingTime,
       "zxAnVoiceSecondToneBreakTime": zxAnVoiceSecondToneBreakTime,
       "zxAnVoiceThirdToneSendingTime": zxAnVoiceThirdToneSendingTime,
       "zxAnVoiceThirdToneBreakTime": zxAnVoiceThirdToneBreakTime,
       "zxAnVoiceCtrlPortTable": zxAnVoiceCtrlPortTable,
       "zxAnVoiceCtrlPortEntry": zxAnVoiceCtrlPortEntry,
       "zxAnVoiceCtrlPortId": zxAnVoiceCtrlPortId,
       "zxAnVoiceCtrlPortType": zxAnVoiceCtrlPortType,
       "zxAnVoiceCtrlPortNo": zxAnVoiceCtrlPortNo,
       "zxAnVoiceCtrlPortRowStatus": zxAnVoiceCtrlPortRowStatus,
       "zxAnVoiceDigitMapTable": zxAnVoiceDigitMapTable,
       "zxAnVoiceDigitMapEntry": zxAnVoiceDigitMapEntry,
       "zxAnVoiceDigitMapName": zxAnVoiceDigitMapName,
       "zxAnVoiceDigitMapType": zxAnVoiceDigitMapType,
       "zxAnVoiceDigitMapBody": zxAnVoiceDigitMapBody,
       "zxAnVoiceDigitMapRowStatus": zxAnVoiceDigitMapRowStatus,
       "zxAnVoicePortNumberStatsObjects": zxAnVoicePortNumberStatsObjects,
       "zxAnVoiceActivePortStatsObjects": zxAnVoiceActivePortStatsObjects,
       "zxAnVoiceActiveV5PotsPorts": zxAnVoiceActiveV5PotsPorts,
       "zxAnVoiceActiveV5BriPorts": zxAnVoiceActiveV5BriPorts,
       "zxAnVoiceActiveV5PriPorts": zxAnVoiceActiveV5PriPorts,
       "zxAnVoiceActiveH248PotsPorts": zxAnVoiceActiveH248PotsPorts,
       "zxAnVoiceActiveH248BriPorts": zxAnVoiceActiveH248BriPorts,
       "zxAnVoiceActiveH248PriPorts": zxAnVoiceActiveH248PriPorts,
       "zxAnVoiceActiveSipPotsPorts": zxAnVoiceActiveSipPotsPorts,
       "zxAnVoiceActiveSipBriPorts": zxAnVoiceActiveSipBriPorts,
       "zxAnVoiceActiveSipPriPorts": zxAnVoiceActiveSipPriPorts,
       "zxAnVoiceActiveLeasedLinePorts": zxAnVoiceActiveLeasedLinePorts}
)
