# SNMP MIB module (FS-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/fscom/FS-ADDRESS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:13:09 2025
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

(fsMgmt,) = mibBuilder.importSymbols(
    "FS-SMI",
    "fsMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "FS-TC",
    "IfIndex")

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

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
 MacAddress,
 PhysAddress,
 RowStatus,
 TextualConvention,
 TimeStamp) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TimeStamp")


# MODULE-IDENTITY

fsAddressMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22)
)
if mibBuilder.loadTexts:
    fsAddressMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FsAddressMIBObjects_ObjectIdentity = ObjectIdentity
fsAddressMIBObjects = _FsAddressMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1)
)
_FsAddressManagementObjects_ObjectIdentity = ObjectIdentity
fsAddressManagementObjects = _FsAddressManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1)
)
_FsDynamicAddressCurrentNum_Type = Integer32
_FsDynamicAddressCurrentNum_Object = MibScalar
fsDynamicAddressCurrentNum = _FsDynamicAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 1),
    _FsDynamicAddressCurrentNum_Type()
)
fsDynamicAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsDynamicAddressCurrentNum.setStatus("current")
_FsStaticAddressCurrentNum_Type = Integer32
_FsStaticAddressCurrentNum_Object = MibScalar
fsStaticAddressCurrentNum = _FsStaticAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 2),
    _FsStaticAddressCurrentNum_Type()
)
fsStaticAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsStaticAddressCurrentNum.setStatus("current")
_FsFilterAddressCurrentNum_Type = Integer32
_FsFilterAddressCurrentNum_Object = MibScalar
fsFilterAddressCurrentNum = _FsFilterAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 3),
    _FsFilterAddressCurrentNum_Type()
)
fsFilterAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsFilterAddressCurrentNum.setStatus("current")
_FsAddressAvailableNum_Type = Integer32
_FsAddressAvailableNum_Object = MibScalar
fsAddressAvailableNum = _FsAddressAvailableNum_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 4),
    _FsAddressAvailableNum_Type()
)
fsAddressAvailableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsAddressAvailableNum.setStatus("current")
_FsMacAddressTable_Object = MibTable
fsMacAddressTable = _FsMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 5)
)
if mibBuilder.loadTexts:
    fsMacAddressTable.setStatus("current")
_FsMacAddressEntry_Object = MibTableRow
fsMacAddressEntry = _FsMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 5, 1)
)
fsMacAddressEntry.setIndexNames(
    (0, "FS-ADDRESS-MIB", "fsMacAddressFdbId"),
    (0, "FS-ADDRESS-MIB", "fsMacAddress"),
)
if mibBuilder.loadTexts:
    fsMacAddressEntry.setStatus("current")
_FsMacAddressFdbId_Type = Unsigned32
_FsMacAddressFdbId_Object = MibTableColumn
fsMacAddressFdbId = _FsMacAddressFdbId_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 5, 1, 1),
    _FsMacAddressFdbId_Type()
)
fsMacAddressFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMacAddressFdbId.setStatus("current")
_FsMacAddress_Type = MacAddress
_FsMacAddress_Object = MibTableColumn
fsMacAddress = _FsMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 5, 1, 2),
    _FsMacAddress_Type()
)
fsMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMacAddress.setStatus("current")
_FsMacAddressPort_Type = IfIndex
_FsMacAddressPort_Object = MibTableColumn
fsMacAddressPort = _FsMacAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 5, 1, 3),
    _FsMacAddressPort_Type()
)
fsMacAddressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMacAddressPort.setStatus("current")


class _FsMacAddressType_Type(Integer32):
    """Custom type fsMacAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2),
          ("filter", 3))
    )


_FsMacAddressType_Type.__name__ = "Integer32"
_FsMacAddressType_Object = MibTableColumn
fsMacAddressType = _FsMacAddressType_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 5, 1, 4),
    _FsMacAddressType_Type()
)
fsMacAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMacAddressType.setStatus("current")
_FsMacAddressStatus_Type = RowStatus
_FsMacAddressStatus_Object = MibTableColumn
fsMacAddressStatus = _FsMacAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 1, 5, 1, 5),
    _FsMacAddressStatus_Type()
)
fsMacAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fsMacAddressStatus.setStatus("current")
_FsAddressNotificationObjects_ObjectIdentity = ObjectIdentity
fsAddressNotificationObjects = _FsAddressNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2)
)
_FsMacNotiGlobalEnabled_Type = EnabledStatus
_FsMacNotiGlobalEnabled_Object = MibScalar
fsMacNotiGlobalEnabled = _FsMacNotiGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 1),
    _FsMacNotiGlobalEnabled_Type()
)
fsMacNotiGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMacNotiGlobalEnabled.setStatus("current")


class _FsMacNotificationInterval_Type(Unsigned32):
    """Custom type fsMacNotificationInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_FsMacNotificationInterval_Type.__name__ = "Unsigned32"
_FsMacNotificationInterval_Object = MibScalar
fsMacNotificationInterval = _FsMacNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 2),
    _FsMacNotificationInterval_Type()
)
fsMacNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMacNotificationInterval.setStatus("current")


class _FsMacNotiHisTableMaxLength_Type(Unsigned32):
    """Custom type fsMacNotiHisTableMaxLength based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_FsMacNotiHisTableMaxLength_Type.__name__ = "Unsigned32"
_FsMacNotiHisTableMaxLength_Object = MibScalar
fsMacNotiHisTableMaxLength = _FsMacNotiHisTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 3),
    _FsMacNotiHisTableMaxLength_Type()
)
fsMacNotiHisTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMacNotiHisTableMaxLength.setStatus("current")
_FsMacNotiHisTableCurrentLength_Type = Unsigned32
_FsMacNotiHisTableCurrentLength_Object = MibScalar
fsMacNotiHisTableCurrentLength = _FsMacNotiHisTableCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 4),
    _FsMacNotiHisTableCurrentLength_Type()
)
fsMacNotiHisTableCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMacNotiHisTableCurrentLength.setStatus("current")
_FsMacNotiHisTable_Object = MibTable
fsMacNotiHisTable = _FsMacNotiHisTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 5)
)
if mibBuilder.loadTexts:
    fsMacNotiHisTable.setStatus("current")
_FsMacNotiHisEntry_Object = MibTableRow
fsMacNotiHisEntry = _FsMacNotiHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 5, 1)
)
fsMacNotiHisEntry.setIndexNames(
    (0, "FS-ADDRESS-MIB", "fsMacNotiHisIndex"),
)
if mibBuilder.loadTexts:
    fsMacNotiHisEntry.setStatus("current")


class _FsMacNotiHisIndex_Type(Unsigned32):
    """Custom type fsMacNotiHisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_FsMacNotiHisIndex_Type.__name__ = "Unsigned32"
_FsMacNotiHisIndex_Object = MibTableColumn
fsMacNotiHisIndex = _FsMacNotiHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 5, 1, 1),
    _FsMacNotiHisIndex_Type()
)
fsMacNotiHisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMacNotiHisIndex.setStatus("current")


class _FsMacNotiHisMacChangedMsg_Type(OctetString):
    """Custom type fsMacNotiHisMacChangedMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_FsMacNotiHisMacChangedMsg_Type.__name__ = "OctetString"
_FsMacNotiHisMacChangedMsg_Object = MibTableColumn
fsMacNotiHisMacChangedMsg = _FsMacNotiHisMacChangedMsg_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 5, 1, 2),
    _FsMacNotiHisMacChangedMsg_Type()
)
fsMacNotiHisMacChangedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMacNotiHisMacChangedMsg.setStatus("current")
_FsMacNotiHisTimestamp_Type = TimeStamp
_FsMacNotiHisTimestamp_Object = MibTableColumn
fsMacNotiHisTimestamp = _FsMacNotiHisTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 5, 1, 3),
    _FsMacNotiHisTimestamp_Type()
)
fsMacNotiHisTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMacNotiHisTimestamp.setStatus("current")
_FsMacNotiIfCfgTable_Object = MibTable
fsMacNotiIfCfgTable = _FsMacNotiIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 6)
)
if mibBuilder.loadTexts:
    fsMacNotiIfCfgTable.setStatus("current")
_FsMacNotiIfCfgEntry_Object = MibTableRow
fsMacNotiIfCfgEntry = _FsMacNotiIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 6, 1)
)
fsMacNotiIfCfgEntry.setIndexNames(
    (0, "FS-ADDRESS-MIB", "fsMacNotiIfIndex"),
)
if mibBuilder.loadTexts:
    fsMacNotiIfCfgEntry.setStatus("current")
_FsMacNotiIfIndex_Type = IfIndex
_FsMacNotiIfIndex_Object = MibTableColumn
fsMacNotiIfIndex = _FsMacNotiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 6, 1, 1),
    _FsMacNotiIfIndex_Type()
)
fsMacNotiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMacNotiIfIndex.setStatus("current")


class _FsIfMacAddrLearntEnable_Type(EnabledStatus):
    """Custom type fsIfMacAddrLearntEnable based on EnabledStatus"""
    defaultValue = 2


_FsIfMacAddrLearntEnable_Type.__name__ = "EnabledStatus"
_FsIfMacAddrLearntEnable_Object = MibTableColumn
fsIfMacAddrLearntEnable = _FsIfMacAddrLearntEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 6, 1, 2),
    _FsIfMacAddrLearntEnable_Type()
)
fsIfMacAddrLearntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfMacAddrLearntEnable.setStatus("current")


class _FsIfMacAddrRemovedEnable_Type(EnabledStatus):
    """Custom type fsIfMacAddrRemovedEnable based on EnabledStatus"""
    defaultValue = 2


_FsIfMacAddrRemovedEnable_Type.__name__ = "EnabledStatus"
_FsIfMacAddrRemovedEnable_Object = MibTableColumn
fsIfMacAddrRemovedEnable = _FsIfMacAddrRemovedEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 6, 1, 3),
    _FsIfMacAddrRemovedEnable_Type()
)
fsIfMacAddrRemovedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsIfMacAddrRemovedEnable.setStatus("current")
_FsMacIfLearnTable_Object = MibTable
fsMacIfLearnTable = _FsMacIfLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 7)
)
if mibBuilder.loadTexts:
    fsMacIfLearnTable.setStatus("current")
_FsMacIfLearnEntry_Object = MibTableRow
fsMacIfLearnEntry = _FsMacIfLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 7, 1)
)
fsMacIfLearnEntry.setIndexNames(
    (0, "FS-ADDRESS-MIB", "fsMacIfLearnIfIndex"),
)
if mibBuilder.loadTexts:
    fsMacIfLearnEntry.setStatus("current")
_FsMacIfLearnIfIndex_Type = IfIndex
_FsMacIfLearnIfIndex_Object = MibTableColumn
fsMacIfLearnIfIndex = _FsMacIfLearnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 7, 1, 1),
    _FsMacIfLearnIfIndex_Type()
)
fsMacIfLearnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fsMacIfLearnIfIndex.setStatus("current")


class _FsMacIfLearnEnable_Type(EnabledStatus):
    """Custom type fsMacIfLearnEnable based on EnabledStatus"""
    defaultValue = 1


_FsMacIfLearnEnable_Type.__name__ = "EnabledStatus"
_FsMacIfLearnEnable_Object = MibTableColumn
fsMacIfLearnEnable = _FsMacIfLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 7, 1, 2),
    _FsMacIfLearnEnable_Type()
)
fsMacIfLearnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMacIfLearnEnable.setStatus("current")


class _FsMacGlobalLearnEnabled_Type(EnabledStatus):
    """Custom type fsMacGlobalLearnEnabled based on EnabledStatus"""
    defaultValue = 1


_FsMacGlobalLearnEnabled_Type.__name__ = "EnabledStatus"
_FsMacGlobalLearnEnabled_Object = MibScalar
fsMacGlobalLearnEnabled = _FsMacGlobalLearnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 1, 2, 8),
    _FsMacGlobalLearnEnabled_Type()
)
fsMacGlobalLearnEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fsMacGlobalLearnEnabled.setStatus("current")
_FsAddressTraps_ObjectIdentity = ObjectIdentity
fsAddressTraps = _FsAddressTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 2)
)
_FsAddressMIBConformance_ObjectIdentity = ObjectIdentity
fsAddressMIBConformance = _FsAddressMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 3)
)
_FsAddressMIBCompliances_ObjectIdentity = ObjectIdentity
fsAddressMIBCompliances = _FsAddressMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 3, 1)
)
_FsAddressMIBGroups_ObjectIdentity = ObjectIdentity
fsAddressMIBGroups = _FsAddressMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 3, 2)
)

# Managed Objects groups

fsMacAddressMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 3, 2, 1)
)
fsMacAddressMIBGroup.setObjects(
      *(("FS-ADDRESS-MIB", "fsDynamicAddressCurrentNum"),
        ("FS-ADDRESS-MIB", "fsStaticAddressCurrentNum"),
        ("FS-ADDRESS-MIB", "fsFilterAddressCurrentNum"),
        ("FS-ADDRESS-MIB", "fsAddressAvailableNum"),
        ("FS-ADDRESS-MIB", "fsMacAddressFdbId"),
        ("FS-ADDRESS-MIB", "fsMacAddress"),
        ("FS-ADDRESS-MIB", "fsMacAddressPort"),
        ("FS-ADDRESS-MIB", "fsMacAddressType"),
        ("FS-ADDRESS-MIB", "fsMacAddressStatus"))
)
if mibBuilder.loadTexts:
    fsMacAddressMIBGroup.setStatus("current")

fsAddressNotificationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 3, 2, 2)
)
fsAddressNotificationMIBGroup.setObjects(
      *(("FS-ADDRESS-MIB", "fsMacNotiGlobalEnabled"),
        ("FS-ADDRESS-MIB", "fsMacNotificationInterval"),
        ("FS-ADDRESS-MIB", "fsMacNotiHisTableMaxLength"),
        ("FS-ADDRESS-MIB", "fsMacNotiHisTableCurrentLength"),
        ("FS-ADDRESS-MIB", "fsMacNotiHisIndex"),
        ("FS-ADDRESS-MIB", "fsMacNotiHisMacChangedMsg"),
        ("FS-ADDRESS-MIB", "fsMacNotiHisTimestamp"),
        ("FS-ADDRESS-MIB", "fsMacNotiIfIndex"),
        ("FS-ADDRESS-MIB", "fsIfMacAddrLearntEnable"),
        ("FS-ADDRESS-MIB", "fsIfMacAddrRemovedEnable"))
)
if mibBuilder.loadTexts:
    fsAddressNotificationMIBGroup.setStatus("current")


# Notification objects

macChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 2, 1)
)
macChangedNotification.setObjects(
    ("FS-ADDRESS-MIB", "fsMacNotiHisMacChangedMsg")
)
if mibBuilder.loadTexts:
    macChangedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

fsAddressMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 52642, 1, 1, 10, 2, 22, 3, 1, 1)
)
fsAddressMIBCompliance.setObjects(
      *(("FS-ADDRESS-MIB", "fsMacAddressMIBGroup"),
        ("FS-ADDRESS-MIB", "fsAddressNotificationMIBGroup"))
)
if mibBuilder.loadTexts:
    fsAddressMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "FS-ADDRESS-MIB",
    **{"fsAddressMIB": fsAddressMIB,
       "fsAddressMIBObjects": fsAddressMIBObjects,
       "fsAddressManagementObjects": fsAddressManagementObjects,
       "fsDynamicAddressCurrentNum": fsDynamicAddressCurrentNum,
       "fsStaticAddressCurrentNum": fsStaticAddressCurrentNum,
       "fsFilterAddressCurrentNum": fsFilterAddressCurrentNum,
       "fsAddressAvailableNum": fsAddressAvailableNum,
       "fsMacAddressTable": fsMacAddressTable,
       "fsMacAddressEntry": fsMacAddressEntry,
       "fsMacAddressFdbId": fsMacAddressFdbId,
       "fsMacAddress": fsMacAddress,
       "fsMacAddressPort": fsMacAddressPort,
       "fsMacAddressType": fsMacAddressType,
       "fsMacAddressStatus": fsMacAddressStatus,
       "fsAddressNotificationObjects": fsAddressNotificationObjects,
       "fsMacNotiGlobalEnabled": fsMacNotiGlobalEnabled,
       "fsMacNotificationInterval": fsMacNotificationInterval,
       "fsMacNotiHisTableMaxLength": fsMacNotiHisTableMaxLength,
       "fsMacNotiHisTableCurrentLength": fsMacNotiHisTableCurrentLength,
       "fsMacNotiHisTable": fsMacNotiHisTable,
       "fsMacNotiHisEntry": fsMacNotiHisEntry,
       "fsMacNotiHisIndex": fsMacNotiHisIndex,
       "fsMacNotiHisMacChangedMsg": fsMacNotiHisMacChangedMsg,
       "fsMacNotiHisTimestamp": fsMacNotiHisTimestamp,
       "fsMacNotiIfCfgTable": fsMacNotiIfCfgTable,
       "fsMacNotiIfCfgEntry": fsMacNotiIfCfgEntry,
       "fsMacNotiIfIndex": fsMacNotiIfIndex,
       "fsIfMacAddrLearntEnable": fsIfMacAddrLearntEnable,
       "fsIfMacAddrRemovedEnable": fsIfMacAddrRemovedEnable,
       "fsMacIfLearnTable": fsMacIfLearnTable,
       "fsMacIfLearnEntry": fsMacIfLearnEntry,
       "fsMacIfLearnIfIndex": fsMacIfLearnIfIndex,
       "fsMacIfLearnEnable": fsMacIfLearnEnable,
       "fsMacGlobalLearnEnabled": fsMacGlobalLearnEnabled,
       "fsAddressTraps": fsAddressTraps,
       "macChangedNotification": macChangedNotification,
       "fsAddressMIBConformance": fsAddressMIBConformance,
       "fsAddressMIBCompliances": fsAddressMIBCompliances,
       "fsAddressMIBCompliance": fsAddressMIBCompliance,
       "fsAddressMIBGroups": fsAddressMIBGroups,
       "fsMacAddressMIBGroup": fsMacAddressMIBGroup,
       "fsAddressNotificationMIBGroup": fsAddressNotificationMIBGroup}
)
