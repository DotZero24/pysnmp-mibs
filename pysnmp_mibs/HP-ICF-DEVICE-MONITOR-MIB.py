# SNMP MIB module (HP-ICF-DEVICE-MONITOR-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/HP-ICF-DEVICE-MONITOR-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:40:24 2025
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

(hpSwitch,) = mibBuilder.importSymbols(
    "HP-ICF-OID",
    "hpSwitch")

(InterfaceIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

hpicfDeviceFingerPrintMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138)
)
if mibBuilder.loadTexts:
    hpicfDeviceFingerPrintMIB.setRevisions(
        ("2021-01-04 07:10",
         "2018-02-05 07:10",
         "2018-01-30 07:10",
         "2018-01-16 07:10",
         "2017-09-15 07:10")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HpicfDevFingerPrinNotifications_ObjectIdentity = ObjectIdentity
hpicfDevFingerPrinNotifications = _HpicfDevFingerPrinNotifications_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 0)
)
_HpicfDevFingerPrinObjects_ObjectIdentity = ObjectIdentity
hpicfDevFingerPrinObjects = _HpicfDevFingerPrinObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1)
)
_HpicfDevFingerPrinConfigObjects_ObjectIdentity = ObjectIdentity
hpicfDevFingerPrinConfigObjects = _HpicfDevFingerPrinConfigObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1)
)
_HpicfDevFingerPrinScalarObjects_ObjectIdentity = ObjectIdentity
hpicfDevFingerPrinScalarObjects = _HpicfDevFingerPrinScalarObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 1)
)
_HpicfDevFingerPrinProfileTable_Object = MibTable
hpicfDevFingerPrinProfileTable = _HpicfDevFingerPrinProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 2)
)
if mibBuilder.loadTexts:
    hpicfDevFingerPrinProfileTable.setStatus("current")
_HpicfDevFingerPrinProfileEntry_Object = MibTableRow
hpicfDevFingerPrinProfileEntry = _HpicfDevFingerPrinProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 2, 1)
)
hpicfDevFingerPrinProfileEntry.setIndexNames(
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinProfileName"),
)
if mibBuilder.loadTexts:
    hpicfDevFingerPrinProfileEntry.setStatus("current")


class _HpicfDevFingerPrinProfileName_Type(DisplayString):
    """Custom type hpicfDevFingerPrinProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfDevFingerPrinProfileName_Type.__name__ = "DisplayString"
_HpicfDevFingerPrinProfileName_Object = MibTableColumn
hpicfDevFingerPrinProfileName = _HpicfDevFingerPrinProfileName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 2, 1, 1),
    _HpicfDevFingerPrinProfileName_Type()
)
hpicfDevFingerPrinProfileName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDevFingerPrinProfileName.setStatus("current")
_HpicfDFPProfRowStatus_Type = RowStatus
_HpicfDFPProfRowStatus_Object = MibTableColumn
hpicfDFPProfRowStatus = _HpicfDFPProfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 2, 1, 2),
    _HpicfDFPProfRowStatus_Type()
)
hpicfDFPProfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDFPProfRowStatus.setStatus("current")
_HpicfDFPProfOptionTable_Object = MibTable
hpicfDFPProfOptionTable = _HpicfDFPProfOptionTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 3)
)
if mibBuilder.loadTexts:
    hpicfDFPProfOptionTable.setStatus("current")
_HpicfDFPProfOptionEntry_Object = MibTableRow
hpicfDFPProfOptionEntry = _HpicfDFPProfOptionEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 3, 1)
)
hpicfDFPProfOptionEntry.setIndexNames(
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinProfileName"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfOptionType"),
)
if mibBuilder.loadTexts:
    hpicfDFPProfOptionEntry.setStatus("current")


class _HpicfDFPProfOptionType_Type(Integer32):
    """Custom type hpicfDFPProfOptionType based on Integer32"""
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
        *(("apply", 1),
          ("dhcp", 2),
          ("http", 3),
          ("lldp", 4),
          ("cdp", 5),
          ("protocol", 6))
    )


_HpicfDFPProfOptionType_Type.__name__ = "Integer32"
_HpicfDFPProfOptionType_Object = MibTableColumn
hpicfDFPProfOptionType = _HpicfDFPProfOptionType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 3, 1, 1),
    _HpicfDFPProfOptionType_Type()
)
hpicfDFPProfOptionType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDFPProfOptionType.setStatus("current")
_HpicfDFPProfOptionRowStatus_Type = RowStatus
_HpicfDFPProfOptionRowStatus_Object = MibTableColumn
hpicfDFPProfOptionRowStatus = _HpicfDFPProfOptionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 3, 1, 2),
    _HpicfDFPProfOptionRowStatus_Type()
)
hpicfDFPProfOptionRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDFPProfOptionRowStatus.setStatus("current")
_HpicfDFPProfProtoEncodTable_Object = MibTable
hpicfDFPProfProtoEncodTable = _HpicfDFPProfProtoEncodTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 4)
)
if mibBuilder.loadTexts:
    hpicfDFPProfProtoEncodTable.setStatus("current")
_HpicfDFPProfProtoEncodEntry_Object = MibTableRow
hpicfDFPProfProtoEncodEntry = _HpicfDFPProfProtoEncodEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 4, 1)
)
hpicfDFPProfProtoEncodEntry.setIndexNames(
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinProfileName"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfOptionType"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoEncodType"),
)
if mibBuilder.loadTexts:
    hpicfDFPProfProtoEncodEntry.setStatus("current")


class _HpicfDFPProfProtoEncodType_Type(Integer32):
    """Custom type hpicfDFPProfProtoEncodType based on Integer32"""
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
        *(("optionNumber", 1),
          ("optionName", 2),
          ("tlvNumber", 3),
          ("tlvName", 4),
          ("optionsList", 5))
    )


_HpicfDFPProfProtoEncodType_Type.__name__ = "Integer32"
_HpicfDFPProfProtoEncodType_Object = MibTableColumn
hpicfDFPProfProtoEncodType = _HpicfDFPProfProtoEncodType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 4, 1, 1),
    _HpicfDFPProfProtoEncodType_Type()
)
hpicfDFPProfProtoEncodType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDFPProfProtoEncodType.setStatus("current")
_HpicfDFPProfProtoEncodRowStat_Type = RowStatus
_HpicfDFPProfProtoEncodRowStat_Object = MibTableColumn
hpicfDFPProfProtoEncodRowStat = _HpicfDFPProfProtoEncodRowStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 4, 1, 2),
    _HpicfDFPProfProtoEncodRowStat_Type()
)
hpicfDFPProfProtoEncodRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDFPProfProtoEncodRowStat.setStatus("current")
_HpicfDFPProfAttrEncodTable_Object = MibTable
hpicfDFPProfAttrEncodTable = _HpicfDFPProfAttrEncodTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 5)
)
if mibBuilder.loadTexts:
    hpicfDFPProfAttrEncodTable.setStatus("current")
_HpicfDFPProfAttrEncodEntry_Object = MibTableRow
hpicfDFPProfAttrEncodEntry = _HpicfDFPProfAttrEncodEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 5, 1)
)
hpicfDFPProfAttrEncodEntry.setIndexNames(
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinProfileName"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfOptionType"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoEncodType"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoAttr"),
)
if mibBuilder.loadTexts:
    hpicfDFPProfAttrEncodEntry.setStatus("current")


class _HpicfDFPProfProtoAttr_Type(Integer32):
    """Custom type hpicfDFPProfProtoAttr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 254),
    )


_HpicfDFPProfProtoAttr_Type.__name__ = "Integer32"
_HpicfDFPProfProtoAttr_Object = MibTableColumn
hpicfDFPProfProtoAttr = _HpicfDFPProfProtoAttr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 5, 1, 1),
    _HpicfDFPProfProtoAttr_Type()
)
hpicfDFPProfProtoAttr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDFPProfProtoAttr.setStatus("current")
_HpicfDFPProfAttrEncodRowStat_Type = RowStatus
_HpicfDFPProfAttrEncodRowStat_Object = MibTableColumn
hpicfDFPProfAttrEncodRowStat = _HpicfDFPProfAttrEncodRowStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 5, 1, 2),
    _HpicfDFPProfAttrEncodRowStat_Type()
)
hpicfDFPProfAttrEncodRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDFPProfAttrEncodRowStat.setStatus("current")
_HpicfDFPProfApplyTable_Object = MibTable
hpicfDFPProfApplyTable = _HpicfDFPProfApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 6)
)
if mibBuilder.loadTexts:
    hpicfDFPProfApplyTable.setStatus("current")
_HpicfDFPProfApplyEntry_Object = MibTableRow
hpicfDFPProfApplyEntry = _HpicfDFPProfApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 6, 1)
)
hpicfDFPProfApplyEntry.setIndexNames(
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinProfileName"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfOptionType"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfApplyPort"),
)
if mibBuilder.loadTexts:
    hpicfDFPProfApplyEntry.setStatus("current")
_HpicfDFPProfApplyPort_Type = InterfaceIndex
_HpicfDFPProfApplyPort_Object = MibTableColumn
hpicfDFPProfApplyPort = _HpicfDFPProfApplyPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 6, 1, 1),
    _HpicfDFPProfApplyPort_Type()
)
hpicfDFPProfApplyPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDFPProfApplyPort.setStatus("current")
_HpicfDFPProfApplyRowStatus_Type = RowStatus
_HpicfDFPProfApplyRowStatus_Object = MibTableColumn
hpicfDFPProfApplyRowStatus = _HpicfDFPProfApplyRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 6, 1, 2),
    _HpicfDFPProfApplyRowStatus_Type()
)
hpicfDFPProfApplyRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDFPProfApplyRowStatus.setStatus("current")
_HpicfDFPProfProtoConnTable_Object = MibTable
hpicfDFPProfProtoConnTable = _HpicfDFPProfProtoConnTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 7)
)
if mibBuilder.loadTexts:
    hpicfDFPProfProtoConnTable.setStatus("current")
_HpicfDFPProfProtoConnEntry_Object = MibTableRow
hpicfDFPProfProtoConnEntry = _HpicfDFPProfProtoConnEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 7, 1)
)
hpicfDFPProfProtoConnEntry.setIndexNames(
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinProfileName"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfOptionType"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoConnType"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoConnPort"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoConnOffset"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoConnWidth"),
)
if mibBuilder.loadTexts:
    hpicfDFPProfProtoConnEntry.setStatus("current")


class _HpicfDFPProfProtoConnType_Type(Integer32):
    """Custom type hpicfDFPProfProtoConnType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tcp", 1),
          ("udp", 2))
    )


_HpicfDFPProfProtoConnType_Type.__name__ = "Integer32"
_HpicfDFPProfProtoConnType_Object = MibTableColumn
hpicfDFPProfProtoConnType = _HpicfDFPProfProtoConnType_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 7, 1, 1),
    _HpicfDFPProfProtoConnType_Type()
)
hpicfDFPProfProtoConnType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDFPProfProtoConnType.setStatus("current")


class _HpicfDFPProfProtoConnPort_Type(Integer32):
    """Custom type hpicfDFPProfProtoConnPort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfDFPProfProtoConnPort_Type.__name__ = "Integer32"
_HpicfDFPProfProtoConnPort_Object = MibTableColumn
hpicfDFPProfProtoConnPort = _HpicfDFPProfProtoConnPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 7, 1, 2),
    _HpicfDFPProfProtoConnPort_Type()
)
hpicfDFPProfProtoConnPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDFPProfProtoConnPort.setStatus("current")


class _HpicfDFPProfProtoConnOffset_Type(Integer32):
    """Custom type hpicfDFPProfProtoConnOffset based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfDFPProfProtoConnOffset_Type.__name__ = "Integer32"
_HpicfDFPProfProtoConnOffset_Object = MibTableColumn
hpicfDFPProfProtoConnOffset = _HpicfDFPProfProtoConnOffset_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 7, 1, 3),
    _HpicfDFPProfProtoConnOffset_Type()
)
hpicfDFPProfProtoConnOffset.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDFPProfProtoConnOffset.setStatus("current")


class _HpicfDFPProfProtoConnWidth_Type(Integer32):
    """Custom type hpicfDFPProfProtoConnWidth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_HpicfDFPProfProtoConnWidth_Type.__name__ = "Integer32"
_HpicfDFPProfProtoConnWidth_Object = MibTableColumn
hpicfDFPProfProtoConnWidth = _HpicfDFPProfProtoConnWidth_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 7, 1, 4),
    _HpicfDFPProfProtoConnWidth_Type()
)
hpicfDFPProfProtoConnWidth.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDFPProfProtoConnWidth.setStatus("current")
_HpicfDFPProfProtoConnRowStat_Type = RowStatus
_HpicfDFPProfProtoConnRowStat_Object = MibTableColumn
hpicfDFPProfProtoConnRowStat = _HpicfDFPProfProtoConnRowStat_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 7, 1, 5),
    _HpicfDFPProfProtoConnRowStat_Type()
)
hpicfDFPProfProtoConnRowStat.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDFPProfProtoConnRowStat.setStatus("current")
_HpicfDevFingerPrinPortTable_Object = MibTable
hpicfDevFingerPrinPortTable = _HpicfDevFingerPrinPortTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 8)
)
if mibBuilder.loadTexts:
    hpicfDevFingerPrinPortTable.setStatus("deprecated")
_HpicfDevFingerPrinPortEntry_Object = MibTableRow
hpicfDevFingerPrinPortEntry = _HpicfDevFingerPrinPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 8, 1)
)
hpicfDevFingerPrinPortEntry.setIndexNames(
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinPortNumber"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinMaxNumber"),
)
if mibBuilder.loadTexts:
    hpicfDevFingerPrinPortEntry.setStatus("deprecated")
_HpicfDevFingerPrinPortNumber_Type = InterfaceIndex
_HpicfDevFingerPrinPortNumber_Object = MibTableColumn
hpicfDevFingerPrinPortNumber = _HpicfDevFingerPrinPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 8, 1, 1),
    _HpicfDevFingerPrinPortNumber_Type()
)
hpicfDevFingerPrinPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDevFingerPrinPortNumber.setStatus("deprecated")


class _HpicfDevFingerPrinMaxNumber_Type(Integer32):
    """Custom type hpicfDevFingerPrinMaxNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_HpicfDevFingerPrinMaxNumber_Type.__name__ = "Integer32"
_HpicfDevFingerPrinMaxNumber_Object = MibTableColumn
hpicfDevFingerPrinMaxNumber = _HpicfDevFingerPrinMaxNumber_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 8, 1, 2),
    _HpicfDevFingerPrinMaxNumber_Type()
)
hpicfDevFingerPrinMaxNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDevFingerPrinMaxNumber.setStatus("deprecated")
_HpicfDFPPortRowStatus_Type = RowStatus
_HpicfDFPPortRowStatus_Object = MibTableColumn
hpicfDFPPortRowStatus = _HpicfDFPPortRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 8, 1, 3),
    _HpicfDFPPortRowStatus_Type()
)
hpicfDFPPortRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    hpicfDFPPortRowStatus.setStatus("deprecated")
_HpicfDFPClientConfigTable_Object = MibTable
hpicfDFPClientConfigTable = _HpicfDFPClientConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 9)
)
if mibBuilder.loadTexts:
    hpicfDFPClientConfigTable.setStatus("current")
_HpicfDFPClientConfigEntry_Object = MibTableRow
hpicfDFPClientConfigEntry = _HpicfDFPClientConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 9, 1)
)
hpicfDFPClientConfigEntry.setIndexNames(
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPConfigPort"),
)
if mibBuilder.loadTexts:
    hpicfDFPClientConfigEntry.setStatus("current")
_HpicfDFPConfigPort_Type = InterfaceIndex
_HpicfDFPConfigPort_Object = MibTableColumn
hpicfDFPConfigPort = _HpicfDFPConfigPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 9, 1, 1),
    _HpicfDFPConfigPort_Type()
)
hpicfDFPConfigPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDFPConfigPort.setStatus("current")


class _HpicfDFPConfigIncomingClients_Type(Integer32):
    """Custom type hpicfDFPConfigIncomingClients based on Integer32"""
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


_HpicfDFPConfigIncomingClients_Type.__name__ = "Integer32"
_HpicfDFPConfigIncomingClients_Object = MibTableColumn
hpicfDFPConfigIncomingClients = _HpicfDFPConfigIncomingClients_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 9, 1, 2),
    _HpicfDFPConfigIncomingClients_Type()
)
hpicfDFPConfigIncomingClients.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDFPConfigIncomingClients.setStatus("current")


class _HpicfDFPConfigClientLimit_Type(Integer32):
    """Custom type hpicfDFPConfigClientLimit based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(2, 8),
    )


_HpicfDFPConfigClientLimit_Type.__name__ = "Integer32"
_HpicfDFPConfigClientLimit_Object = MibTableColumn
hpicfDFPConfigClientLimit = _HpicfDFPConfigClientLimit_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 1, 9, 1, 3),
    _HpicfDFPConfigClientLimit_Type()
)
hpicfDFPConfigClientLimit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDFPConfigClientLimit.setStatus("current")
_HpicfDevFingerPrinStatsObjects_ObjectIdentity = ObjectIdentity
hpicfDevFingerPrinStatsObjects = _HpicfDevFingerPrinStatsObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 2)
)
_HpicfDFPClientStatsTable_Object = MibTable
hpicfDFPClientStatsTable = _HpicfDFPClientStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 2, 1)
)
if mibBuilder.loadTexts:
    hpicfDFPClientStatsTable.setStatus("current")
_HpicfDFPClientStatsEntry_Object = MibTableRow
hpicfDFPClientStatsEntry = _HpicfDFPClientStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 2, 1, 1)
)
hpicfDFPClientStatsEntry.setIndexNames(
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinClientPort"),
    (0, "HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinClientMacAddr"),
)
if mibBuilder.loadTexts:
    hpicfDFPClientStatsEntry.setStatus("current")
_HpicfDevFingerPrinClientPort_Type = InterfaceIndex
_HpicfDevFingerPrinClientPort_Object = MibTableColumn
hpicfDevFingerPrinClientPort = _HpicfDevFingerPrinClientPort_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 2, 1, 1, 1),
    _HpicfDevFingerPrinClientPort_Type()
)
hpicfDevFingerPrinClientPort.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDevFingerPrinClientPort.setStatus("current")
_HpicfDevFingerPrinClientMacAddr_Type = MacAddress
_HpicfDevFingerPrinClientMacAddr_Object = MibTableColumn
hpicfDevFingerPrinClientMacAddr = _HpicfDevFingerPrinClientMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 2, 1, 1, 2),
    _HpicfDevFingerPrinClientMacAddr_Type()
)
hpicfDevFingerPrinClientMacAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    hpicfDevFingerPrinClientMacAddr.setStatus("current")


class _HpicfDevFingerPrinClientProfile_Type(DisplayString):
    """Custom type hpicfDevFingerPrinClientProfile based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_HpicfDevFingerPrinClientProfile_Type.__name__ = "DisplayString"
_HpicfDevFingerPrinClientProfile_Object = MibTableColumn
hpicfDevFingerPrinClientProfile = _HpicfDevFingerPrinClientProfile_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 2, 1, 1, 3),
    _HpicfDevFingerPrinClientProfile_Type()
)
hpicfDevFingerPrinClientProfile.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDevFingerPrinClientProfile.setStatus("current")


class _HpicfDFPClientDevCategory_Type(DisplayString):
    """Custom type hpicfDFPClientDevCategory based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpicfDFPClientDevCategory_Type.__name__ = "DisplayString"
_HpicfDFPClientDevCategory_Object = MibTableColumn
hpicfDFPClientDevCategory = _HpicfDFPClientDevCategory_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 2, 1, 1, 4),
    _HpicfDFPClientDevCategory_Type()
)
hpicfDFPClientDevCategory.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDFPClientDevCategory.setStatus("current")


class _HpicfDFPClientDevOsFamily_Type(DisplayString):
    """Custom type hpicfDFPClientDevOsFamily based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpicfDFPClientDevOsFamily_Type.__name__ = "DisplayString"
_HpicfDFPClientDevOsFamily_Object = MibTableColumn
hpicfDFPClientDevOsFamily = _HpicfDFPClientDevOsFamily_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 2, 1, 1, 5),
    _HpicfDFPClientDevOsFamily_Type()
)
hpicfDFPClientDevOsFamily.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDFPClientDevOsFamily.setStatus("current")


class _HpicfDFPClientDevName_Type(DisplayString):
    """Custom type hpicfDFPClientDevName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_HpicfDFPClientDevName_Type.__name__ = "DisplayString"
_HpicfDFPClientDevName_Object = MibTableColumn
hpicfDFPClientDevName = _HpicfDFPClientDevName_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 2, 1, 1, 6),
    _HpicfDFPClientDevName_Type()
)
hpicfDFPClientDevName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDFPClientDevName.setStatus("current")


class _HpicfDFPClientStatus_Type(Integer32):
    """Custom type hpicfDFPClientStatus based on Integer32"""
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
        *(("dataCollected", 1),
          ("dataNotCollected", 2),
          ("completed", 3),
          ("inprogress", 4))
    )


_HpicfDFPClientStatus_Type.__name__ = "Integer32"
_HpicfDFPClientStatus_Object = MibTableColumn
hpicfDFPClientStatus = _HpicfDFPClientStatus_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 2, 1, 1, 7),
    _HpicfDFPClientStatus_Type()
)
hpicfDFPClientStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    hpicfDFPClientStatus.setStatus("current")
_HpicfDevFingerPrinGlobalObjects_ObjectIdentity = ObjectIdentity
hpicfDevFingerPrinGlobalObjects = _HpicfDevFingerPrinGlobalObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 3)
)


class _HpicfDevFingerPrinTimer_Type(Unsigned32):
    """Custom type hpicfDevFingerPrinTimer based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(60, 300),
    )


_HpicfDevFingerPrinTimer_Type.__name__ = "Unsigned32"
_HpicfDevFingerPrinTimer_Object = MibScalar
hpicfDevFingerPrinTimer = _HpicfDevFingerPrinTimer_Object(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 1, 3, 1),
    _HpicfDevFingerPrinTimer_Type()
)
hpicfDevFingerPrinTimer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    hpicfDevFingerPrinTimer.setStatus("current")
_HpicfDevFingerPrinConformance_ObjectIdentity = ObjectIdentity
hpicfDevFingerPrinConformance = _HpicfDevFingerPrinConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2)
)
_HpicfDevFingerPrinCompliances_ObjectIdentity = ObjectIdentity
hpicfDevFingerPrinCompliances = _HpicfDevFingerPrinCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 1)
)
_HpicfDevFingerPrinGroups_ObjectIdentity = ObjectIdentity
hpicfDevFingerPrinGroups = _HpicfDevFingerPrinGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 2)
)

# Managed Objects groups

hpicfDevFingerPrinProfileGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 2, 1)
)
hpicfDevFingerPrinProfileGroup.setObjects(
      *(("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfRowStatus"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfOptionRowStatus"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoEncodRowStat"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfAttrEncodRowStat"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoConnRowStat"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfApplyRowStatus"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPPortRowStatus"))
)
if mibBuilder.loadTexts:
    hpicfDevFingerPrinProfileGroup.setStatus("deprecated")

hpicfDFPClientStatsGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 2, 2)
)
hpicfDFPClientStatsGroup.setObjects(
      *(("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinClientProfile"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientDevCategory"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientDevOsFamily"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientDevName"))
)
if mibBuilder.loadTexts:
    hpicfDFPClientStatsGroup.setStatus("deprecated")

hpicfDFPClientStatsGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 2, 3)
)
hpicfDFPClientStatsGroup1.setObjects(
      *(("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinClientProfile"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientDevCategory"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientDevOsFamily"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientDevName"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientStatus"))
)
if mibBuilder.loadTexts:
    hpicfDFPClientStatsGroup1.setStatus("current")

hpicfDFPClientConfigGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 2, 4)
)
hpicfDFPClientConfigGroup.setObjects(
    ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPConfigIncomingClients")
)
if mibBuilder.loadTexts:
    hpicfDFPClientConfigGroup.setStatus("deprecated")

hpicfDevFingerPrinProfileGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 2, 5)
)
hpicfDevFingerPrinProfileGroup1.setObjects(
      *(("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfRowStatus"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfOptionRowStatus"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoEncodRowStat"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfAttrEncodRowStat"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfProtoConnRowStat"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPProfApplyRowStatus"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinTimer"))
)
if mibBuilder.loadTexts:
    hpicfDevFingerPrinProfileGroup1.setStatus("current")

hpicfDFPClientConfigGroup1 = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 2, 6)
)
hpicfDFPClientConfigGroup1.setObjects(
      *(("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPConfigIncomingClients"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPConfigClientLimit"))
)
if mibBuilder.loadTexts:
    hpicfDFPClientConfigGroup1.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

hpicfDevFingerPrinCompliance1 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 1, 1)
)
hpicfDevFingerPrinCompliance1.setObjects(
      *(("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinProfileGroup"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientStatsGroup"))
)
if mibBuilder.loadTexts:
    hpicfDevFingerPrinCompliance1.setStatus(
        "deprecated"
    )

hpicfDevFingerPrinCompliance2 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 1, 2)
)
hpicfDevFingerPrinCompliance2.setObjects(
      *(("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinProfileGroup"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientStatsGroup1"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientConfigGroup"))
)
if mibBuilder.loadTexts:
    hpicfDevFingerPrinCompliance2.setStatus(
        "deprecated"
    )

hpicfDevFingerPrinCompliance3 = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 138, 2, 1, 3)
)
hpicfDevFingerPrinCompliance3.setObjects(
      *(("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDevFingerPrinProfileGroup1"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientStatsGroup1"),
        ("HP-ICF-DEVICE-MONITOR-MIB", "hpicfDFPClientConfigGroup1"))
)
if mibBuilder.loadTexts:
    hpicfDevFingerPrinCompliance3.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HP-ICF-DEVICE-MONITOR-MIB",
    **{"hpicfDeviceFingerPrintMIB": hpicfDeviceFingerPrintMIB,
       "hpicfDevFingerPrinNotifications": hpicfDevFingerPrinNotifications,
       "hpicfDevFingerPrinObjects": hpicfDevFingerPrinObjects,
       "hpicfDevFingerPrinConfigObjects": hpicfDevFingerPrinConfigObjects,
       "hpicfDevFingerPrinScalarObjects": hpicfDevFingerPrinScalarObjects,
       "hpicfDevFingerPrinProfileTable": hpicfDevFingerPrinProfileTable,
       "hpicfDevFingerPrinProfileEntry": hpicfDevFingerPrinProfileEntry,
       "hpicfDevFingerPrinProfileName": hpicfDevFingerPrinProfileName,
       "hpicfDFPProfRowStatus": hpicfDFPProfRowStatus,
       "hpicfDFPProfOptionTable": hpicfDFPProfOptionTable,
       "hpicfDFPProfOptionEntry": hpicfDFPProfOptionEntry,
       "hpicfDFPProfOptionType": hpicfDFPProfOptionType,
       "hpicfDFPProfOptionRowStatus": hpicfDFPProfOptionRowStatus,
       "hpicfDFPProfProtoEncodTable": hpicfDFPProfProtoEncodTable,
       "hpicfDFPProfProtoEncodEntry": hpicfDFPProfProtoEncodEntry,
       "hpicfDFPProfProtoEncodType": hpicfDFPProfProtoEncodType,
       "hpicfDFPProfProtoEncodRowStat": hpicfDFPProfProtoEncodRowStat,
       "hpicfDFPProfAttrEncodTable": hpicfDFPProfAttrEncodTable,
       "hpicfDFPProfAttrEncodEntry": hpicfDFPProfAttrEncodEntry,
       "hpicfDFPProfProtoAttr": hpicfDFPProfProtoAttr,
       "hpicfDFPProfAttrEncodRowStat": hpicfDFPProfAttrEncodRowStat,
       "hpicfDFPProfApplyTable": hpicfDFPProfApplyTable,
       "hpicfDFPProfApplyEntry": hpicfDFPProfApplyEntry,
       "hpicfDFPProfApplyPort": hpicfDFPProfApplyPort,
       "hpicfDFPProfApplyRowStatus": hpicfDFPProfApplyRowStatus,
       "hpicfDFPProfProtoConnTable": hpicfDFPProfProtoConnTable,
       "hpicfDFPProfProtoConnEntry": hpicfDFPProfProtoConnEntry,
       "hpicfDFPProfProtoConnType": hpicfDFPProfProtoConnType,
       "hpicfDFPProfProtoConnPort": hpicfDFPProfProtoConnPort,
       "hpicfDFPProfProtoConnOffset": hpicfDFPProfProtoConnOffset,
       "hpicfDFPProfProtoConnWidth": hpicfDFPProfProtoConnWidth,
       "hpicfDFPProfProtoConnRowStat": hpicfDFPProfProtoConnRowStat,
       "hpicfDevFingerPrinPortTable": hpicfDevFingerPrinPortTable,
       "hpicfDevFingerPrinPortEntry": hpicfDevFingerPrinPortEntry,
       "hpicfDevFingerPrinPortNumber": hpicfDevFingerPrinPortNumber,
       "hpicfDevFingerPrinMaxNumber": hpicfDevFingerPrinMaxNumber,
       "hpicfDFPPortRowStatus": hpicfDFPPortRowStatus,
       "hpicfDFPClientConfigTable": hpicfDFPClientConfigTable,
       "hpicfDFPClientConfigEntry": hpicfDFPClientConfigEntry,
       "hpicfDFPConfigPort": hpicfDFPConfigPort,
       "hpicfDFPConfigIncomingClients": hpicfDFPConfigIncomingClients,
       "hpicfDFPConfigClientLimit": hpicfDFPConfigClientLimit,
       "hpicfDevFingerPrinStatsObjects": hpicfDevFingerPrinStatsObjects,
       "hpicfDFPClientStatsTable": hpicfDFPClientStatsTable,
       "hpicfDFPClientStatsEntry": hpicfDFPClientStatsEntry,
       "hpicfDevFingerPrinClientPort": hpicfDevFingerPrinClientPort,
       "hpicfDevFingerPrinClientMacAddr": hpicfDevFingerPrinClientMacAddr,
       "hpicfDevFingerPrinClientProfile": hpicfDevFingerPrinClientProfile,
       "hpicfDFPClientDevCategory": hpicfDFPClientDevCategory,
       "hpicfDFPClientDevOsFamily": hpicfDFPClientDevOsFamily,
       "hpicfDFPClientDevName": hpicfDFPClientDevName,
       "hpicfDFPClientStatus": hpicfDFPClientStatus,
       "hpicfDevFingerPrinGlobalObjects": hpicfDevFingerPrinGlobalObjects,
       "hpicfDevFingerPrinTimer": hpicfDevFingerPrinTimer,
       "hpicfDevFingerPrinConformance": hpicfDevFingerPrinConformance,
       "hpicfDevFingerPrinCompliances": hpicfDevFingerPrinCompliances,
       "hpicfDevFingerPrinCompliance1": hpicfDevFingerPrinCompliance1,
       "hpicfDevFingerPrinCompliance2": hpicfDevFingerPrinCompliance2,
       "hpicfDevFingerPrinCompliance3": hpicfDevFingerPrinCompliance3,
       "hpicfDevFingerPrinGroups": hpicfDevFingerPrinGroups,
       "hpicfDevFingerPrinProfileGroup": hpicfDevFingerPrinProfileGroup,
       "hpicfDFPClientStatsGroup": hpicfDFPClientStatsGroup,
       "hpicfDFPClientStatsGroup1": hpicfDFPClientStatsGroup1,
       "hpicfDFPClientConfigGroup": hpicfDFPClientConfigGroup,
       "hpicfDevFingerPrinProfileGroup1": hpicfDevFingerPrinProfileGroup1,
       "hpicfDFPClientConfigGroup1": hpicfDFPClientConfigGroup1}
)
