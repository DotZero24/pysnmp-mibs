# SNMP MIB module (QTECH-ADDRESS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/qtech/QTECH-ADDRESS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:56:46 2025
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

(EnabledStatus,) = mibBuilder.importSymbols(
    "P-BRIDGE-MIB",
    "EnabledStatus")

(qtechMgmt,) = mibBuilder.importSymbols(
    "QTECH-SMI",
    "qtechMgmt")

(IfIndex,) = mibBuilder.importSymbols(
    "QTECH-TC",
    "IfIndex")

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

qtechAddressMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22)
)
if mibBuilder.loadTexts:
    qtechAddressMIB.setRevisions(
        ("2002-03-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_QtechAddressMIBObjects_ObjectIdentity = ObjectIdentity
qtechAddressMIBObjects = _QtechAddressMIBObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1)
)
_QtechAddressManagementObjects_ObjectIdentity = ObjectIdentity
qtechAddressManagementObjects = _QtechAddressManagementObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1)
)
_QtechDynamicAddressCurrentNum_Type = Integer32
_QtechDynamicAddressCurrentNum_Object = MibScalar
qtechDynamicAddressCurrentNum = _QtechDynamicAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 1),
    _QtechDynamicAddressCurrentNum_Type()
)
qtechDynamicAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechDynamicAddressCurrentNum.setStatus("current")
_QtechStaticAddressCurrentNum_Type = Integer32
_QtechStaticAddressCurrentNum_Object = MibScalar
qtechStaticAddressCurrentNum = _QtechStaticAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 2),
    _QtechStaticAddressCurrentNum_Type()
)
qtechStaticAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechStaticAddressCurrentNum.setStatus("current")
_QtechFilterAddressCurrentNum_Type = Integer32
_QtechFilterAddressCurrentNum_Object = MibScalar
qtechFilterAddressCurrentNum = _QtechFilterAddressCurrentNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 3),
    _QtechFilterAddressCurrentNum_Type()
)
qtechFilterAddressCurrentNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechFilterAddressCurrentNum.setStatus("current")
_QtechAddressAvailableNum_Type = Integer32
_QtechAddressAvailableNum_Object = MibScalar
qtechAddressAvailableNum = _QtechAddressAvailableNum_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 4),
    _QtechAddressAvailableNum_Type()
)
qtechAddressAvailableNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechAddressAvailableNum.setStatus("current")
_QtechMacAddressTable_Object = MibTable
qtechMacAddressTable = _QtechMacAddressTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 5)
)
if mibBuilder.loadTexts:
    qtechMacAddressTable.setStatus("current")
_QtechMacAddressEntry_Object = MibTableRow
qtechMacAddressEntry = _QtechMacAddressEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 5, 1)
)
qtechMacAddressEntry.setIndexNames(
    (0, "QTECH-ADDRESS-MIB", "qtechMacAddressFdbId"),
    (0, "QTECH-ADDRESS-MIB", "qtechMacAddress"),
)
if mibBuilder.loadTexts:
    qtechMacAddressEntry.setStatus("current")
_QtechMacAddressFdbId_Type = Unsigned32
_QtechMacAddressFdbId_Object = MibTableColumn
qtechMacAddressFdbId = _QtechMacAddressFdbId_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 5, 1, 1),
    _QtechMacAddressFdbId_Type()
)
qtechMacAddressFdbId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMacAddressFdbId.setStatus("current")
_QtechMacAddress_Type = MacAddress
_QtechMacAddress_Object = MibTableColumn
qtechMacAddress = _QtechMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 5, 1, 2),
    _QtechMacAddress_Type()
)
qtechMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMacAddress.setStatus("current")
_QtechMacAddressPort_Type = IfIndex
_QtechMacAddressPort_Object = MibTableColumn
qtechMacAddressPort = _QtechMacAddressPort_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 5, 1, 3),
    _QtechMacAddressPort_Type()
)
qtechMacAddressPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMacAddressPort.setStatus("current")


class _QtechMacAddressType_Type(Integer32):
    """Custom type qtechMacAddressType based on Integer32"""
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


_QtechMacAddressType_Type.__name__ = "Integer32"
_QtechMacAddressType_Object = MibTableColumn
qtechMacAddressType = _QtechMacAddressType_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 5, 1, 4),
    _QtechMacAddressType_Type()
)
qtechMacAddressType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMacAddressType.setStatus("current")
_QtechMacAddressStatus_Type = RowStatus
_QtechMacAddressStatus_Object = MibTableColumn
qtechMacAddressStatus = _QtechMacAddressStatus_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 1, 5, 1, 5),
    _QtechMacAddressStatus_Type()
)
qtechMacAddressStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    qtechMacAddressStatus.setStatus("current")
_QtechAddressNotificationObjects_ObjectIdentity = ObjectIdentity
qtechAddressNotificationObjects = _QtechAddressNotificationObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2)
)
_QtechMacNotiGlobalEnabled_Type = EnabledStatus
_QtechMacNotiGlobalEnabled_Object = MibScalar
qtechMacNotiGlobalEnabled = _QtechMacNotiGlobalEnabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 1),
    _QtechMacNotiGlobalEnabled_Type()
)
qtechMacNotiGlobalEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMacNotiGlobalEnabled.setStatus("current")


class _QtechMacNotificationInterval_Type(Unsigned32):
    """Custom type qtechMacNotificationInterval based on Unsigned32"""
    defaultValue = 1

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 3600),
    )


_QtechMacNotificationInterval_Type.__name__ = "Unsigned32"
_QtechMacNotificationInterval_Object = MibScalar
qtechMacNotificationInterval = _QtechMacNotificationInterval_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 2),
    _QtechMacNotificationInterval_Type()
)
qtechMacNotificationInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMacNotificationInterval.setStatus("current")


class _QtechMacNotiHisTableMaxLength_Type(Unsigned32):
    """Custom type qtechMacNotiHisTableMaxLength based on Unsigned32"""
    defaultValue = 50

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 200),
    )


_QtechMacNotiHisTableMaxLength_Type.__name__ = "Unsigned32"
_QtechMacNotiHisTableMaxLength_Object = MibScalar
qtechMacNotiHisTableMaxLength = _QtechMacNotiHisTableMaxLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 3),
    _QtechMacNotiHisTableMaxLength_Type()
)
qtechMacNotiHisTableMaxLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMacNotiHisTableMaxLength.setStatus("current")
_QtechMacNotiHisTableCurrentLength_Type = Unsigned32
_QtechMacNotiHisTableCurrentLength_Object = MibScalar
qtechMacNotiHisTableCurrentLength = _QtechMacNotiHisTableCurrentLength_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 4),
    _QtechMacNotiHisTableCurrentLength_Type()
)
qtechMacNotiHisTableCurrentLength.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMacNotiHisTableCurrentLength.setStatus("current")
_QtechMacNotiHisTable_Object = MibTable
qtechMacNotiHisTable = _QtechMacNotiHisTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 5)
)
if mibBuilder.loadTexts:
    qtechMacNotiHisTable.setStatus("current")
_QtechMacNotiHisEntry_Object = MibTableRow
qtechMacNotiHisEntry = _QtechMacNotiHisEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 5, 1)
)
qtechMacNotiHisEntry.setIndexNames(
    (0, "QTECH-ADDRESS-MIB", "qtechMacNotiHisIndex"),
)
if mibBuilder.loadTexts:
    qtechMacNotiHisEntry.setStatus("current")


class _QtechMacNotiHisIndex_Type(Unsigned32):
    """Custom type qtechMacNotiHisIndex based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4294967295),
    )


_QtechMacNotiHisIndex_Type.__name__ = "Unsigned32"
_QtechMacNotiHisIndex_Object = MibTableColumn
qtechMacNotiHisIndex = _QtechMacNotiHisIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 5, 1, 1),
    _QtechMacNotiHisIndex_Type()
)
qtechMacNotiHisIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMacNotiHisIndex.setStatus("current")


class _QtechMacNotiHisMacChangedMsg_Type(OctetString):
    """Custom type qtechMacNotiHisMacChangedMsg based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 254),
    )


_QtechMacNotiHisMacChangedMsg_Type.__name__ = "OctetString"
_QtechMacNotiHisMacChangedMsg_Object = MibTableColumn
qtechMacNotiHisMacChangedMsg = _QtechMacNotiHisMacChangedMsg_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 5, 1, 2),
    _QtechMacNotiHisMacChangedMsg_Type()
)
qtechMacNotiHisMacChangedMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMacNotiHisMacChangedMsg.setStatus("current")
_QtechMacNotiHisTimestamp_Type = TimeStamp
_QtechMacNotiHisTimestamp_Object = MibTableColumn
qtechMacNotiHisTimestamp = _QtechMacNotiHisTimestamp_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 5, 1, 3),
    _QtechMacNotiHisTimestamp_Type()
)
qtechMacNotiHisTimestamp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMacNotiHisTimestamp.setStatus("current")
_QtechMacNotiIfCfgTable_Object = MibTable
qtechMacNotiIfCfgTable = _QtechMacNotiIfCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 6)
)
if mibBuilder.loadTexts:
    qtechMacNotiIfCfgTable.setStatus("current")
_QtechMacNotiIfCfgEntry_Object = MibTableRow
qtechMacNotiIfCfgEntry = _QtechMacNotiIfCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 6, 1)
)
qtechMacNotiIfCfgEntry.setIndexNames(
    (0, "QTECH-ADDRESS-MIB", "qtechMacNotiIfIndex"),
)
if mibBuilder.loadTexts:
    qtechMacNotiIfCfgEntry.setStatus("current")
_QtechMacNotiIfIndex_Type = IfIndex
_QtechMacNotiIfIndex_Object = MibTableColumn
qtechMacNotiIfIndex = _QtechMacNotiIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 6, 1, 1),
    _QtechMacNotiIfIndex_Type()
)
qtechMacNotiIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMacNotiIfIndex.setStatus("current")


class _QtechIfMacAddrLearntEnable_Type(EnabledStatus):
    """Custom type qtechIfMacAddrLearntEnable based on EnabledStatus"""
    defaultValue = 2


_QtechIfMacAddrLearntEnable_Type.__name__ = "EnabledStatus"
_QtechIfMacAddrLearntEnable_Object = MibTableColumn
qtechIfMacAddrLearntEnable = _QtechIfMacAddrLearntEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 6, 1, 2),
    _QtechIfMacAddrLearntEnable_Type()
)
qtechIfMacAddrLearntEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfMacAddrLearntEnable.setStatus("current")


class _QtechIfMacAddrRemovedEnable_Type(EnabledStatus):
    """Custom type qtechIfMacAddrRemovedEnable based on EnabledStatus"""
    defaultValue = 2


_QtechIfMacAddrRemovedEnable_Type.__name__ = "EnabledStatus"
_QtechIfMacAddrRemovedEnable_Object = MibTableColumn
qtechIfMacAddrRemovedEnable = _QtechIfMacAddrRemovedEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 6, 1, 3),
    _QtechIfMacAddrRemovedEnable_Type()
)
qtechIfMacAddrRemovedEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechIfMacAddrRemovedEnable.setStatus("current")
_QtechMacIfLearnTable_Object = MibTable
qtechMacIfLearnTable = _QtechMacIfLearnTable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 7)
)
if mibBuilder.loadTexts:
    qtechMacIfLearnTable.setStatus("current")
_QtechMacIfLearnEntry_Object = MibTableRow
qtechMacIfLearnEntry = _QtechMacIfLearnEntry_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 7, 1)
)
qtechMacIfLearnEntry.setIndexNames(
    (0, "QTECH-ADDRESS-MIB", "qtechMacIfLearnIfIndex"),
)
if mibBuilder.loadTexts:
    qtechMacIfLearnEntry.setStatus("current")
_QtechMacIfLearnIfIndex_Type = IfIndex
_QtechMacIfLearnIfIndex_Object = MibTableColumn
qtechMacIfLearnIfIndex = _QtechMacIfLearnIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 7, 1, 1),
    _QtechMacIfLearnIfIndex_Type()
)
qtechMacIfLearnIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    qtechMacIfLearnIfIndex.setStatus("current")


class _QtechMacIfLearnEnable_Type(EnabledStatus):
    """Custom type qtechMacIfLearnEnable based on EnabledStatus"""
    defaultValue = 1


_QtechMacIfLearnEnable_Type.__name__ = "EnabledStatus"
_QtechMacIfLearnEnable_Object = MibTableColumn
qtechMacIfLearnEnable = _QtechMacIfLearnEnable_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 7, 1, 2),
    _QtechMacIfLearnEnable_Type()
)
qtechMacIfLearnEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMacIfLearnEnable.setStatus("current")


class _QtechMacGlobalLearnEnabled_Type(EnabledStatus):
    """Custom type qtechMacGlobalLearnEnabled based on EnabledStatus"""
    defaultValue = 1


_QtechMacGlobalLearnEnabled_Type.__name__ = "EnabledStatus"
_QtechMacGlobalLearnEnabled_Object = MibScalar
qtechMacGlobalLearnEnabled = _QtechMacGlobalLearnEnabled_Object(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 1, 2, 8),
    _QtechMacGlobalLearnEnabled_Type()
)
qtechMacGlobalLearnEnabled.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    qtechMacGlobalLearnEnabled.setStatus("current")
_QtechAddressTraps_ObjectIdentity = ObjectIdentity
qtechAddressTraps = _QtechAddressTraps_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 2)
)
_QtechAddressMIBConformance_ObjectIdentity = ObjectIdentity
qtechAddressMIBConformance = _QtechAddressMIBConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 3)
)
_QtechAddressMIBCompliances_ObjectIdentity = ObjectIdentity
qtechAddressMIBCompliances = _QtechAddressMIBCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 3, 1)
)
_QtechAddressMIBGroups_ObjectIdentity = ObjectIdentity
qtechAddressMIBGroups = _QtechAddressMIBGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 3, 2)
)

# Managed Objects groups

qtechMacAddressMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 3, 2, 1)
)
qtechMacAddressMIBGroup.setObjects(
      *(("QTECH-ADDRESS-MIB", "qtechDynamicAddressCurrentNum"),
        ("QTECH-ADDRESS-MIB", "qtechStaticAddressCurrentNum"),
        ("QTECH-ADDRESS-MIB", "qtechFilterAddressCurrentNum"),
        ("QTECH-ADDRESS-MIB", "qtechAddressAvailableNum"),
        ("QTECH-ADDRESS-MIB", "qtechMacAddressFdbId"),
        ("QTECH-ADDRESS-MIB", "qtechMacAddress"),
        ("QTECH-ADDRESS-MIB", "qtechMacAddressPort"),
        ("QTECH-ADDRESS-MIB", "qtechMacAddressType"),
        ("QTECH-ADDRESS-MIB", "qtechMacAddressStatus"))
)
if mibBuilder.loadTexts:
    qtechMacAddressMIBGroup.setStatus("current")

qtechAddressNotificationMIBGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 3, 2, 2)
)
qtechAddressNotificationMIBGroup.setObjects(
      *(("QTECH-ADDRESS-MIB", "qtechMacNotiGlobalEnabled"),
        ("QTECH-ADDRESS-MIB", "qtechMacNotificationInterval"),
        ("QTECH-ADDRESS-MIB", "qtechMacNotiHisTableMaxLength"),
        ("QTECH-ADDRESS-MIB", "qtechMacNotiHisTableCurrentLength"),
        ("QTECH-ADDRESS-MIB", "qtechMacNotiHisIndex"),
        ("QTECH-ADDRESS-MIB", "qtechMacNotiHisMacChangedMsg"),
        ("QTECH-ADDRESS-MIB", "qtechMacNotiHisTimestamp"),
        ("QTECH-ADDRESS-MIB", "qtechMacNotiIfIndex"),
        ("QTECH-ADDRESS-MIB", "qtechIfMacAddrLearntEnable"),
        ("QTECH-ADDRESS-MIB", "qtechIfMacAddrRemovedEnable"))
)
if mibBuilder.loadTexts:
    qtechAddressNotificationMIBGroup.setStatus("current")


# Notification objects

macChangedNotification = NotificationType(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 2, 1)
)
macChangedNotification.setObjects(
    ("QTECH-ADDRESS-MIB", "qtechMacNotiHisMacChangedMsg")
)
if mibBuilder.loadTexts:
    macChangedNotification.setStatus(
        "current"
    )


# Notifications groups


# Agent capabilities


# Module compliance

qtechAddressMIBCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 27514, 1, 1, 10, 2, 22, 3, 1, 1)
)
qtechAddressMIBCompliance.setObjects(
      *(("QTECH-ADDRESS-MIB", "qtechMacAddressMIBGroup"),
        ("QTECH-ADDRESS-MIB", "qtechAddressNotificationMIBGroup"))
)
if mibBuilder.loadTexts:
    qtechAddressMIBCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "QTECH-ADDRESS-MIB",
    **{"qtechAddressMIB": qtechAddressMIB,
       "qtechAddressMIBObjects": qtechAddressMIBObjects,
       "qtechAddressManagementObjects": qtechAddressManagementObjects,
       "qtechDynamicAddressCurrentNum": qtechDynamicAddressCurrentNum,
       "qtechStaticAddressCurrentNum": qtechStaticAddressCurrentNum,
       "qtechFilterAddressCurrentNum": qtechFilterAddressCurrentNum,
       "qtechAddressAvailableNum": qtechAddressAvailableNum,
       "qtechMacAddressTable": qtechMacAddressTable,
       "qtechMacAddressEntry": qtechMacAddressEntry,
       "qtechMacAddressFdbId": qtechMacAddressFdbId,
       "qtechMacAddress": qtechMacAddress,
       "qtechMacAddressPort": qtechMacAddressPort,
       "qtechMacAddressType": qtechMacAddressType,
       "qtechMacAddressStatus": qtechMacAddressStatus,
       "qtechAddressNotificationObjects": qtechAddressNotificationObjects,
       "qtechMacNotiGlobalEnabled": qtechMacNotiGlobalEnabled,
       "qtechMacNotificationInterval": qtechMacNotificationInterval,
       "qtechMacNotiHisTableMaxLength": qtechMacNotiHisTableMaxLength,
       "qtechMacNotiHisTableCurrentLength": qtechMacNotiHisTableCurrentLength,
       "qtechMacNotiHisTable": qtechMacNotiHisTable,
       "qtechMacNotiHisEntry": qtechMacNotiHisEntry,
       "qtechMacNotiHisIndex": qtechMacNotiHisIndex,
       "qtechMacNotiHisMacChangedMsg": qtechMacNotiHisMacChangedMsg,
       "qtechMacNotiHisTimestamp": qtechMacNotiHisTimestamp,
       "qtechMacNotiIfCfgTable": qtechMacNotiIfCfgTable,
       "qtechMacNotiIfCfgEntry": qtechMacNotiIfCfgEntry,
       "qtechMacNotiIfIndex": qtechMacNotiIfIndex,
       "qtechIfMacAddrLearntEnable": qtechIfMacAddrLearntEnable,
       "qtechIfMacAddrRemovedEnable": qtechIfMacAddrRemovedEnable,
       "qtechMacIfLearnTable": qtechMacIfLearnTable,
       "qtechMacIfLearnEntry": qtechMacIfLearnEntry,
       "qtechMacIfLearnIfIndex": qtechMacIfLearnIfIndex,
       "qtechMacIfLearnEnable": qtechMacIfLearnEnable,
       "qtechMacGlobalLearnEnabled": qtechMacGlobalLearnEnabled,
       "qtechAddressTraps": qtechAddressTraps,
       "macChangedNotification": macChangedNotification,
       "qtechAddressMIBConformance": qtechAddressMIBConformance,
       "qtechAddressMIBCompliances": qtechAddressMIBCompliances,
       "qtechAddressMIBCompliance": qtechAddressMIBCompliance,
       "qtechAddressMIBGroups": qtechAddressMIBGroups,
       "qtechMacAddressMIBGroup": qtechMacAddressMIBGroup,
       "qtechAddressNotificationMIBGroup": qtechAddressNotificationMIBGroup}
)
