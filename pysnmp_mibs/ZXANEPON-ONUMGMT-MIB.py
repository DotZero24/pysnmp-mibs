# SNMP MIB module (ZXANEPON-ONUMGMT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZXANEPON-ONUMGMT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:45:32 2025
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
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "MacAddress",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")

(zxAnEponMib,) = mibBuilder.importSymbols(
    "ZTE-MASTER-MIB",
    "zxAnEponMib")


# MODULE-IDENTITY

zxAnEponOnuRemoteMgmt = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_ZxAnEponOnuExtendedAttrMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuExtendedAttrMgmt = _ZxAnEponOnuExtendedAttrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1)
)
_ZxAnEponOnuSnTable_Object = MibTable
zxAnEponOnuSnTable = _ZxAnEponOnuSnTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuSnTable.setStatus("current")
_ZxAnEponOnuSnEntry_Object = MibTableRow
zxAnEponOnuSnEntry = _ZxAnEponOnuSnEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 1, 1)
)
zxAnEponOnuSnEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuSnEntry.setStatus("current")
_ZxAnEponOnuIfIndex_Type = Integer32
_ZxAnEponOnuIfIndex_Object = MibTableColumn
zxAnEponOnuIfIndex = _ZxAnEponOnuIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 1, 1, 1),
    _ZxAnEponOnuIfIndex_Type()
)
zxAnEponOnuIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuIfIndex.setStatus("current")


class _ZxAnEponOnuVendorId_Type(OctetString):
    """Custom type zxAnEponOnuVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ZxAnEponOnuVendorId_Type.__name__ = "OctetString"
_ZxAnEponOnuVendorId_Object = MibTableColumn
zxAnEponOnuVendorId = _ZxAnEponOnuVendorId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 1, 1, 2),
    _ZxAnEponOnuVendorId_Type()
)
zxAnEponOnuVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVendorId.setStatus("current")


class _ZxAnEponOnuModel_Type(OctetString):
    """Custom type zxAnEponOnuModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_ZxAnEponOnuModel_Type.__name__ = "OctetString"
_ZxAnEponOnuModel_Object = MibTableColumn
zxAnEponOnuModel = _ZxAnEponOnuModel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 1, 1, 3),
    _ZxAnEponOnuModel_Type()
)
zxAnEponOnuModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuModel.setStatus("current")
_ZxAnEponOnuMacAddr_Type = MacAddress
_ZxAnEponOnuMacAddr_Object = MibTableColumn
zxAnEponOnuMacAddr = _ZxAnEponOnuMacAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 1, 1, 4),
    _ZxAnEponOnuMacAddr_Type()
)
zxAnEponOnuMacAddr.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuMacAddr.setStatus("current")


class _ZxAnEponOnuHardwareVersion_Type(OctetString):
    """Custom type zxAnEponOnuHardwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnEponOnuHardwareVersion_Type.__name__ = "OctetString"
_ZxAnEponOnuHardwareVersion_Object = MibTableColumn
zxAnEponOnuHardwareVersion = _ZxAnEponOnuHardwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 1, 1, 5),
    _ZxAnEponOnuHardwareVersion_Type()
)
zxAnEponOnuHardwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuHardwareVersion.setStatus("current")


class _ZxAnEponOnuSoftwareVersion_Type(OctetString):
    """Custom type zxAnEponOnuSoftwareVersion based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ZxAnEponOnuSoftwareVersion_Type.__name__ = "OctetString"
_ZxAnEponOnuSoftwareVersion_Object = MibTableColumn
zxAnEponOnuSoftwareVersion = _ZxAnEponOnuSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 1, 1, 6),
    _ZxAnEponOnuSoftwareVersion_Type()
)
zxAnEponOnuSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuSoftwareVersion.setStatus("current")


class _ZxAnEponOnuExtendedModel_Type(OctetString):
    """Custom type zxAnEponOnuExtendedModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ZxAnEponOnuExtendedModel_Type.__name__ = "OctetString"
_ZxAnEponOnuExtendedModel_Object = MibTableColumn
zxAnEponOnuExtendedModel = _ZxAnEponOnuExtendedModel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 1, 1, 7),
    _ZxAnEponOnuExtendedModel_Type()
)
zxAnEponOnuExtendedModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuExtendedModel.setStatus("current")
_ZxAnEponOnuFirmwareVerTable_Object = MibTable
zxAnEponOnuFirmwareVerTable = _ZxAnEponOnuFirmwareVerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuFirmwareVerTable.setStatus("current")
_ZxAnEponOnuFirmwareVerEntry_Object = MibTableRow
zxAnEponOnuFirmwareVerEntry = _ZxAnEponOnuFirmwareVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 2, 1)
)
zxAnEponOnuFirmwareVerEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuFirmwareVerEntry.setStatus("current")


class _ZxAnEponOnuFirmwareVer_Type(OctetString):
    """Custom type zxAnEponOnuFirmwareVer based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 16),
    )
    fixed_length = 16


_ZxAnEponOnuFirmwareVer_Type.__name__ = "OctetString"
_ZxAnEponOnuFirmwareVer_Object = MibTableColumn
zxAnEponOnuFirmwareVer = _ZxAnEponOnuFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 2, 1, 1),
    _ZxAnEponOnuFirmwareVer_Type()
)
zxAnEponOnuFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuFirmwareVer.setStatus("current")
_ZxAnEponOnuChipsetIdTable_Object = MibTable
zxAnEponOnuChipsetIdTable = _ZxAnEponOnuChipsetIdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 3)
)
if mibBuilder.loadTexts:
    zxAnEponOnuChipsetIdTable.setStatus("current")
_ZxAnEponOnuChipsetIdEntry_Object = MibTableRow
zxAnEponOnuChipsetIdEntry = _ZxAnEponOnuChipsetIdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 3, 1)
)
zxAnEponOnuChipsetIdEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuChipsetIdEntry.setStatus("current")


class _ZxAnEponOnuChipVendorId_Type(OctetString):
    """Custom type zxAnEponOnuChipVendorId based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_ZxAnEponOnuChipVendorId_Type.__name__ = "OctetString"
_ZxAnEponOnuChipVendorId_Object = MibTableColumn
zxAnEponOnuChipVendorId = _ZxAnEponOnuChipVendorId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 3, 1, 1),
    _ZxAnEponOnuChipVendorId_Type()
)
zxAnEponOnuChipVendorId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuChipVendorId.setStatus("current")


class _ZxAnEponOnuChipModel_Type(OctetString):
    """Custom type zxAnEponOnuChipModel based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(2, 2),
    )
    fixed_length = 2


_ZxAnEponOnuChipModel_Type.__name__ = "OctetString"
_ZxAnEponOnuChipModel_Object = MibTableColumn
zxAnEponOnuChipModel = _ZxAnEponOnuChipModel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 3, 1, 2),
    _ZxAnEponOnuChipModel_Type()
)
zxAnEponOnuChipModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuChipModel.setStatus("current")
_ZxAnEponOnuChipRevision_Type = Integer32
_ZxAnEponOnuChipRevision_Object = MibTableColumn
zxAnEponOnuChipRevision = _ZxAnEponOnuChipRevision_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 3, 1, 3),
    _ZxAnEponOnuChipRevision_Type()
)
zxAnEponOnuChipRevision.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuChipRevision.setStatus("current")


class _ZxAnEponOnuChipDate_Type(OctetString):
    """Custom type zxAnEponOnuChipDate based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(3, 3),
    )
    fixed_length = 3


_ZxAnEponOnuChipDate_Type.__name__ = "OctetString"
_ZxAnEponOnuChipDate_Object = MibTableColumn
zxAnEponOnuChipDate = _ZxAnEponOnuChipDate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 3, 1, 4),
    _ZxAnEponOnuChipDate_Type()
)
zxAnEponOnuChipDate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuChipDate.setStatus("current")
_ZxAnEponOnuCapabilityTable_Object = MibTable
zxAnEponOnuCapabilityTable = _ZxAnEponOnuCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4)
)
if mibBuilder.loadTexts:
    zxAnEponOnuCapabilityTable.setStatus("current")
_ZxAnEponOnuCapabilityEntry_Object = MibTableRow
zxAnEponOnuCapabilityEntry = _ZxAnEponOnuCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1)
)
zxAnEponOnuCapabilityEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuCapabilityEntry.setStatus("current")


class _ZxAnEponOnuServiceSupported_Type(Bits):
    """Custom type zxAnEponOnuServiceSupported based on Bits"""
    namedValues = NamedValues(
        *(("gePortSupport", 0),
          ("fePortSupport", 1),
          ("voipSupport", 2),
          ("e1Support", 3),
          ("onuOffLine", 4))
    )

_ZxAnEponOnuServiceSupported_Type.__name__ = "Bits"
_ZxAnEponOnuServiceSupported_Object = MibTableColumn
zxAnEponOnuServiceSupported = _ZxAnEponOnuServiceSupported_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 1),
    _ZxAnEponOnuServiceSupported_Type()
)
zxAnEponOnuServiceSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuServiceSupported.setStatus("current")


class _ZxAnEponOnuGePortNumber_Type(Integer32):
    """Custom type zxAnEponOnuGePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnEponOnuGePortNumber_Type.__name__ = "Integer32"
_ZxAnEponOnuGePortNumber_Object = MibTableColumn
zxAnEponOnuGePortNumber = _ZxAnEponOnuGePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 2),
    _ZxAnEponOnuGePortNumber_Type()
)
zxAnEponOnuGePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuGePortNumber.setStatus("current")


class _ZxAnEponOnuGePortBitmap_Type(OctetString):
    """Custom type zxAnEponOnuGePortBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnEponOnuGePortBitmap_Type.__name__ = "OctetString"
_ZxAnEponOnuGePortBitmap_Object = MibTableColumn
zxAnEponOnuGePortBitmap = _ZxAnEponOnuGePortBitmap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 3),
    _ZxAnEponOnuGePortBitmap_Type()
)
zxAnEponOnuGePortBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuGePortBitmap.setStatus("current")


class _ZxAnEponOnuFePortNumber_Type(Integer32):
    """Custom type zxAnEponOnuFePortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnEponOnuFePortNumber_Type.__name__ = "Integer32"
_ZxAnEponOnuFePortNumber_Object = MibTableColumn
zxAnEponOnuFePortNumber = _ZxAnEponOnuFePortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 4),
    _ZxAnEponOnuFePortNumber_Type()
)
zxAnEponOnuFePortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuFePortNumber.setStatus("current")


class _ZxAnEponOnuFePortBitmap_Type(OctetString):
    """Custom type zxAnEponOnuFePortBitmap based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(8, 8),
    )
    fixed_length = 8


_ZxAnEponOnuFePortBitmap_Type.__name__ = "OctetString"
_ZxAnEponOnuFePortBitmap_Object = MibTableColumn
zxAnEponOnuFePortBitmap = _ZxAnEponOnuFePortBitmap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 5),
    _ZxAnEponOnuFePortBitmap_Type()
)
zxAnEponOnuFePortBitmap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuFePortBitmap.setStatus("current")


class _ZxAnEponOnuPotsPortNumber_Type(Integer32):
    """Custom type zxAnEponOnuPotsPortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnEponOnuPotsPortNumber_Type.__name__ = "Integer32"
_ZxAnEponOnuPotsPortNumber_Object = MibTableColumn
zxAnEponOnuPotsPortNumber = _ZxAnEponOnuPotsPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 6),
    _ZxAnEponOnuPotsPortNumber_Type()
)
zxAnEponOnuPotsPortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPotsPortNumber.setStatus("current")


class _ZxAnEponOnuE1PortNumber_Type(Integer32):
    """Custom type zxAnEponOnuE1PortNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnEponOnuE1PortNumber_Type.__name__ = "Integer32"
_ZxAnEponOnuE1PortNumber_Object = MibTableColumn
zxAnEponOnuE1PortNumber = _ZxAnEponOnuE1PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 7),
    _ZxAnEponOnuE1PortNumber_Type()
)
zxAnEponOnuE1PortNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuE1PortNumber.setStatus("current")


class _ZxAnEponOnuUsQueueNumber_Type(Integer32):
    """Custom type zxAnEponOnuUsQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnEponOnuUsQueueNumber_Type.__name__ = "Integer32"
_ZxAnEponOnuUsQueueNumber_Object = MibTableColumn
zxAnEponOnuUsQueueNumber = _ZxAnEponOnuUsQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 8),
    _ZxAnEponOnuUsQueueNumber_Type()
)
zxAnEponOnuUsQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuUsQueueNumber.setStatus("current")


class _ZxAnEponOnuUsPortMaxQueueNumber_Type(Integer32):
    """Custom type zxAnEponOnuUsPortMaxQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnEponOnuUsPortMaxQueueNumber_Type.__name__ = "Integer32"
_ZxAnEponOnuUsPortMaxQueueNumber_Object = MibTableColumn
zxAnEponOnuUsPortMaxQueueNumber = _ZxAnEponOnuUsPortMaxQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 9),
    _ZxAnEponOnuUsPortMaxQueueNumber_Type()
)
zxAnEponOnuUsPortMaxQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuUsPortMaxQueueNumber.setStatus("current")


class _ZxAnEponOnuDsQueueNumber_Type(Integer32):
    """Custom type zxAnEponOnuDsQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnEponOnuDsQueueNumber_Type.__name__ = "Integer32"
_ZxAnEponOnuDsQueueNumber_Object = MibTableColumn
zxAnEponOnuDsQueueNumber = _ZxAnEponOnuDsQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 10),
    _ZxAnEponOnuDsQueueNumber_Type()
)
zxAnEponOnuDsQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuDsQueueNumber.setStatus("current")


class _ZxAnEponOnuDsPortMaxQueueNumber_Type(Integer32):
    """Custom type zxAnEponOnuDsPortMaxQueueNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnEponOnuDsPortMaxQueueNumber_Type.__name__ = "Integer32"
_ZxAnEponOnuDsPortMaxQueueNumber_Object = MibTableColumn
zxAnEponOnuDsPortMaxQueueNumber = _ZxAnEponOnuDsPortMaxQueueNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 11),
    _ZxAnEponOnuDsPortMaxQueueNumber_Type()
)
zxAnEponOnuDsPortMaxQueueNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuDsPortMaxQueueNumber.setStatus("current")
_ZxAnEponOnuBatteryBackup_Type = TruthValue
_ZxAnEponOnuBatteryBackup_Object = MibTableColumn
zxAnEponOnuBatteryBackup = _ZxAnEponOnuBatteryBackup_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 4, 1, 12),
    _ZxAnEponOnuBatteryBackup_Type()
)
zxAnEponOnuBatteryBackup.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuBatteryBackup.setStatus("current")
_ZxAnEponOnuEthLinkStateTable_Object = MibTable
zxAnEponOnuEthLinkStateTable = _ZxAnEponOnuEthLinkStateTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 5)
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthLinkStateTable.setStatus("current")
_ZxAnEponOnuEthLinkStateEntry_Object = MibTableRow
zxAnEponOnuEthLinkStateEntry = _ZxAnEponOnuEthLinkStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 5, 1)
)
zxAnEponOnuEthLinkStateEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthLinkStateEntry.setStatus("current")
_ZxAnEponOnuPortId_Type = Integer32
_ZxAnEponOnuPortId_Object = MibTableColumn
zxAnEponOnuPortId = _ZxAnEponOnuPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 5, 1, 1),
    _ZxAnEponOnuPortId_Type()
)
zxAnEponOnuPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuPortId.setStatus("current")


class _ZxAnEponOnuEthPortLinkState_Type(Integer32):
    """Custom type zxAnEponOnuEthPortLinkState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("down", 1),
          ("up", 2))
    )


_ZxAnEponOnuEthPortLinkState_Type.__name__ = "Integer32"
_ZxAnEponOnuEthPortLinkState_Object = MibTableColumn
zxAnEponOnuEthPortLinkState = _ZxAnEponOnuEthPortLinkState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 5, 1, 2),
    _ZxAnEponOnuEthPortLinkState_Type()
)
zxAnEponOnuEthPortLinkState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuEthPortLinkState.setStatus("current")
_ZxAnEponOnuEthPortPauseTable_Object = MibTable
zxAnEponOnuEthPortPauseTable = _ZxAnEponOnuEthPortPauseTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 6)
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthPortPauseTable.setStatus("current")
_ZxAnEponOnuEthPortPauseEntry_Object = MibTableRow
zxAnEponOnuEthPortPauseEntry = _ZxAnEponOnuEthPortPauseEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 6, 1)
)
zxAnEponOnuEthPortPauseEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthPortPauseEntry.setStatus("current")


class _ZxAnEponOnuPortBackPressure_Type(Integer32):
    """Custom type zxAnEponOnuPortBackPressure based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deactive", 1),
          ("active", 2))
    )


_ZxAnEponOnuPortBackPressure_Type.__name__ = "Integer32"
_ZxAnEponOnuPortBackPressure_Object = MibTableColumn
zxAnEponOnuPortBackPressure = _ZxAnEponOnuPortBackPressure_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 6, 1, 1),
    _ZxAnEponOnuPortBackPressure_Type()
)
zxAnEponOnuPortBackPressure.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortBackPressure.setStatus("current")
_ZxAnEponOnuEthPortPolicingTable_Object = MibTable
zxAnEponOnuEthPortPolicingTable = _ZxAnEponOnuEthPortPolicingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 7)
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthPortPolicingTable.setStatus("current")
_ZxAnEponOnuEthPortPolicingEntry_Object = MibTableRow
zxAnEponOnuEthPortPolicingEntry = _ZxAnEponOnuEthPortPolicingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 7, 1)
)
zxAnEponOnuEthPortPolicingEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuEthPortPolicingEntry.setStatus("current")


class _ZxAnEponOnuPortPolicing_Type(Integer32):
    """Custom type zxAnEponOnuPortPolicing based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("deactive", 1),
          ("active", 2))
    )


_ZxAnEponOnuPortPolicing_Type.__name__ = "Integer32"
_ZxAnEponOnuPortPolicing_Object = MibTableColumn
zxAnEponOnuPortPolicing = _ZxAnEponOnuPortPolicing_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 7, 1, 1),
    _ZxAnEponOnuPortPolicing_Type()
)
zxAnEponOnuPortPolicing.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortPolicing.setStatus("current")


class _ZxAnEponOnuPortPolicingCir_Type(Integer32):
    """Custom type zxAnEponOnuPortPolicingCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ZxAnEponOnuPortPolicingCir_Type.__name__ = "Integer32"
_ZxAnEponOnuPortPolicingCir_Object = MibTableColumn
zxAnEponOnuPortPolicingCir = _ZxAnEponOnuPortPolicingCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 7, 1, 2),
    _ZxAnEponOnuPortPolicingCir_Type()
)
zxAnEponOnuPortPolicingCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortPolicingCir.setStatus("current")


class _ZxAnEponOnuPortPolicingBucketDepth_Type(Integer32):
    """Custom type zxAnEponOnuPortPolicingBucketDepth based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 16777215),
    )


_ZxAnEponOnuPortPolicingBucketDepth_Type.__name__ = "Integer32"
_ZxAnEponOnuPortPolicingBucketDepth_Object = MibTableColumn
zxAnEponOnuPortPolicingBucketDepth = _ZxAnEponOnuPortPolicingBucketDepth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 7, 1, 3),
    _ZxAnEponOnuPortPolicingBucketDepth_Type()
)
zxAnEponOnuPortPolicingBucketDepth.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortPolicingBucketDepth.setStatus("current")


class _ZxAnEponOnuPortPolicingExtraBurstSize_Type(Integer32):
    """Custom type zxAnEponOnuPortPolicingExtraBurstSize based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1522),
    )


_ZxAnEponOnuPortPolicingExtraBurstSize_Type.__name__ = "Integer32"
_ZxAnEponOnuPortPolicingExtraBurstSize_Object = MibTableColumn
zxAnEponOnuPortPolicingExtraBurstSize = _ZxAnEponOnuPortPolicingExtraBurstSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 7, 1, 4),
    _ZxAnEponOnuPortPolicingExtraBurstSize_Type()
)
zxAnEponOnuPortPolicingExtraBurstSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortPolicingExtraBurstSize.setStatus("current")


class _ZxAnEponOnuPortPolicingDownStream_Type(Integer32):
    """Custom type zxAnEponOnuPortPolicingDownStream based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("notavailable", 0),
          ("deactive", 1),
          ("active", 2))
    )


_ZxAnEponOnuPortPolicingDownStream_Type.__name__ = "Integer32"
_ZxAnEponOnuPortPolicingDownStream_Object = MibTableColumn
zxAnEponOnuPortPolicingDownStream = _ZxAnEponOnuPortPolicingDownStream_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 7, 1, 5),
    _ZxAnEponOnuPortPolicingDownStream_Type()
)
zxAnEponOnuPortPolicingDownStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortPolicingDownStream.setStatus("current")


class _ZxAnEponOnuPortPolicingCirDownStream_Type(Integer32):
    """Custom type zxAnEponOnuPortPolicingCirDownStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ZxAnEponOnuPortPolicingCirDownStream_Type.__name__ = "Integer32"
_ZxAnEponOnuPortPolicingCirDownStream_Object = MibTableColumn
zxAnEponOnuPortPolicingCirDownStream = _ZxAnEponOnuPortPolicingCirDownStream_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 7, 1, 6),
    _ZxAnEponOnuPortPolicingCirDownStream_Type()
)
zxAnEponOnuPortPolicingCirDownStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortPolicingCirDownStream.setStatus("current")


class _ZxAnEponOnuPortPolicingBucketDepthDownStream_Type(Integer32):
    """Custom type zxAnEponOnuPortPolicingBucketDepthDownStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 16777215),
    )


_ZxAnEponOnuPortPolicingBucketDepthDownStream_Type.__name__ = "Integer32"
_ZxAnEponOnuPortPolicingBucketDepthDownStream_Object = MibTableColumn
zxAnEponOnuPortPolicingBucketDepthDownStream = _ZxAnEponOnuPortPolicingBucketDepthDownStream_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 7, 1, 7),
    _ZxAnEponOnuPortPolicingBucketDepthDownStream_Type()
)
zxAnEponOnuPortPolicingBucketDepthDownStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortPolicingBucketDepthDownStream.setStatus("current")


class _ZxAnEponOnuPortPolicingExtraBurstSizeDownStream_Type(Integer32):
    """Custom type zxAnEponOnuPortPolicingExtraBurstSizeDownStream based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1522),
    )


_ZxAnEponOnuPortPolicingExtraBurstSizeDownStream_Type.__name__ = "Integer32"
_ZxAnEponOnuPortPolicingExtraBurstSizeDownStream_Object = MibTableColumn
zxAnEponOnuPortPolicingExtraBurstSizeDownStream = _ZxAnEponOnuPortPolicingExtraBurstSizeDownStream_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 7, 1, 8),
    _ZxAnEponOnuPortPolicingExtraBurstSizeDownStream_Type()
)
zxAnEponOnuPortPolicingExtraBurstSizeDownStream.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortPolicingExtraBurstSizeDownStream.setStatus("current")
_ZxAnEponOnuVoipPortTable_Object = MibTable
zxAnEponOnuVoipPortTable = _ZxAnEponOnuVoipPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 8)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVoipPortTable.setStatus("current")
_ZxAnEponOnuVoipPortEntry_Object = MibTableRow
zxAnEponOnuVoipPortEntry = _ZxAnEponOnuVoipPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 8, 1)
)
zxAnEponOnuVoipPortEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVoipPortEntry.setStatus("current")


class _ZxAnEponOnuVoipPortEnable_Type(Integer32):
    """Custom type zxAnEponOnuVoipPortEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuVoipPortEnable_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipPortEnable_Object = MibTableColumn
zxAnEponOnuVoipPortEnable = _ZxAnEponOnuVoipPortEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 8, 1, 1),
    _ZxAnEponOnuVoipPortEnable_Type()
)
zxAnEponOnuVoipPortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipPortEnable.setStatus("current")
_ZxAnEponOnuE1PortTable_Object = MibTable
zxAnEponOnuE1PortTable = _ZxAnEponOnuE1PortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 9)
)
if mibBuilder.loadTexts:
    zxAnEponOnuE1PortTable.setStatus("current")
_ZxAnEponOnuE1PortEntry_Object = MibTableRow
zxAnEponOnuE1PortEntry = _ZxAnEponOnuE1PortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 9, 1)
)
zxAnEponOnuE1PortEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuE1PortEntry.setStatus("current")


class _ZxAnEponOnuE1PortEnable_Type(Integer32):
    """Custom type zxAnEponOnuE1PortEnable based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuE1PortEnable_Type.__name__ = "Integer32"
_ZxAnEponOnuE1PortEnable_Object = MibTableColumn
zxAnEponOnuE1PortEnable = _ZxAnEponOnuE1PortEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 9, 1, 1),
    _ZxAnEponOnuE1PortEnable_Type()
)
zxAnEponOnuE1PortEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuE1PortEnable.setStatus("current")
_ZxAnEponOnuVlanCfgMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuVlanCfgMgmt = _ZxAnEponOnuVlanCfgMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10)
)
_ZxAnEponOnuVlanCfgTable_Object = MibTable
zxAnEponOnuVlanCfgTable = _ZxAnEponOnuVlanCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVlanCfgTable.setStatus("current")
_ZxAnEponOnuVlanCfgEntry_Object = MibTableRow
zxAnEponOnuVlanCfgEntry = _ZxAnEponOnuVlanCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 1, 1)
)
zxAnEponOnuVlanCfgEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVlanCfgEntry.setStatus("current")


class _ZxAnEponOnuVlanMode_Type(Integer32):
    """Custom type zxAnEponOnuVlanMode based on Integer32"""
    defaultValue = 1

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
        *(("transparent", 1),
          ("tag", 2),
          ("translation", 3),
          ("trunk", 4),
          ("hybrid", 5),
          ("aggregation", 6))
    )


_ZxAnEponOnuVlanMode_Type.__name__ = "Integer32"
_ZxAnEponOnuVlanMode_Object = MibTableColumn
zxAnEponOnuVlanMode = _ZxAnEponOnuVlanMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 1, 1, 1),
    _ZxAnEponOnuVlanMode_Type()
)
zxAnEponOnuVlanMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanMode.setStatus("current")


class _ZxAnEponOnuVlanCfgState_Type(Integer32):
    """Custom type zxAnEponOnuVlanCfgState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("not-finish", 1),
          ("finish", 2))
    )


_ZxAnEponOnuVlanCfgState_Type.__name__ = "Integer32"
_ZxAnEponOnuVlanCfgState_Object = MibTableColumn
zxAnEponOnuVlanCfgState = _ZxAnEponOnuVlanCfgState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 1, 1, 2),
    _ZxAnEponOnuVlanCfgState_Type()
)
zxAnEponOnuVlanCfgState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanCfgState.setStatus("current")
_ZxAnEponOnuVlanTagTable_Object = MibTable
zxAnEponOnuVlanTagTable = _ZxAnEponOnuVlanTagTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTagTable.setStatus("current")
_ZxAnEponOnuVlanTagEntry_Object = MibTableRow
zxAnEponOnuVlanTagEntry = _ZxAnEponOnuVlanTagEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 2, 1)
)
zxAnEponOnuVlanTagEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTagEntry.setStatus("current")


class _ZxAnEponOnuVlanTagVid_Type(Integer32):
    """Custom type zxAnEponOnuVlanTagVid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxAnEponOnuVlanTagVid_Type.__name__ = "Integer32"
_ZxAnEponOnuVlanTagVid_Object = MibTableColumn
zxAnEponOnuVlanTagVid = _ZxAnEponOnuVlanTagVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 2, 1, 1),
    _ZxAnEponOnuVlanTagVid_Type()
)
zxAnEponOnuVlanTagVid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTagVid.setStatus("current")
_ZxAnEponOnuVlanTagTpid_Type = Integer32
_ZxAnEponOnuVlanTagTpid_Object = MibTableColumn
zxAnEponOnuVlanTagTpid = _ZxAnEponOnuVlanTagTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 2, 1, 2),
    _ZxAnEponOnuVlanTagTpid_Type()
)
zxAnEponOnuVlanTagTpid.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTagTpid.setStatus("current")


class _ZxAnEponOnuVlanTagCfi_Type(Integer32):
    """Custom type zxAnEponOnuVlanTagCfi based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ZxAnEponOnuVlanTagCfi_Type.__name__ = "Integer32"
_ZxAnEponOnuVlanTagCfi_Object = MibTableColumn
zxAnEponOnuVlanTagCfi = _ZxAnEponOnuVlanTagCfi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 2, 1, 3),
    _ZxAnEponOnuVlanTagCfi_Type()
)
zxAnEponOnuVlanTagCfi.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTagCfi.setStatus("current")


class _ZxAnEponOnuVlanPriority_Type(Integer32):
    """Custom type zxAnEponOnuVlanPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnEponOnuVlanPriority_Type.__name__ = "Integer32"
_ZxAnEponOnuVlanPriority_Object = MibTableColumn
zxAnEponOnuVlanPriority = _ZxAnEponOnuVlanPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 2, 1, 4),
    _ZxAnEponOnuVlanPriority_Type()
)
zxAnEponOnuVlanPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanPriority.setStatus("current")
_ZxAnEponOnuVlanTranslationTable_Object = MibTable
zxAnEponOnuVlanTranslationTable = _ZxAnEponOnuVlanTranslationTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 3)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTranslationTable.setStatus("current")
_ZxAnEponOnuVlanTranslationEntry_Object = MibTableRow
zxAnEponOnuVlanTranslationEntry = _ZxAnEponOnuVlanTranslationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 3, 1)
)
zxAnEponOnuVlanTranslationEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuVlanTransModeEntryId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTranslationEntry.setStatus("current")
_ZxAnEponOnuVlanTransModeEntryId_Type = Integer32
_ZxAnEponOnuVlanTransModeEntryId_Object = MibTableColumn
zxAnEponOnuVlanTransModeEntryId = _ZxAnEponOnuVlanTransModeEntryId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 3, 1, 1),
    _ZxAnEponOnuVlanTransModeEntryId_Type()
)
zxAnEponOnuVlanTransModeEntryId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTransModeEntryId.setStatus("current")
_ZxAnEponOnuVlanTransOriginalTag_Type = Unsigned32
_ZxAnEponOnuVlanTransOriginalTag_Object = MibTableColumn
zxAnEponOnuVlanTransOriginalTag = _ZxAnEponOnuVlanTransOriginalTag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 3, 1, 2),
    _ZxAnEponOnuVlanTransOriginalTag_Type()
)
zxAnEponOnuVlanTransOriginalTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTransOriginalTag.setStatus("current")
_ZxAnEponOnuVlanTransNewTag_Type = Unsigned32
_ZxAnEponOnuVlanTransNewTag_Object = MibTableColumn
zxAnEponOnuVlanTransNewTag = _ZxAnEponOnuVlanTransNewTag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 3, 1, 3),
    _ZxAnEponOnuVlanTransNewTag_Type()
)
zxAnEponOnuVlanTransNewTag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTransNewTag.setStatus("current")
_ZxAnEponOnuVlanTransModeRowStatus_Type = RowStatus
_ZxAnEponOnuVlanTransModeRowStatus_Object = MibTableColumn
zxAnEponOnuVlanTransModeRowStatus = _ZxAnEponOnuVlanTransModeRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 3, 1, 4),
    _ZxAnEponOnuVlanTransModeRowStatus_Type()
)
zxAnEponOnuVlanTransModeRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTransModeRowStatus.setStatus("current")
_ZxAnEponOnuVlanTrunkTable_Object = MibTable
zxAnEponOnuVlanTrunkTable = _ZxAnEponOnuVlanTrunkTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 4)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTrunkTable.setStatus("current")
_ZxAnEponOnuVlanTrunkEntry_Object = MibTableRow
zxAnEponOnuVlanTrunkEntry = _ZxAnEponOnuVlanTrunkEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 4, 1)
)
zxAnEponOnuVlanTrunkEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTrunkEntry.setStatus("current")
_ZxAnEponOnuVlanTrunkModeVlan_Type = OctetString
_ZxAnEponOnuVlanTrunkModeVlan_Object = MibTableColumn
zxAnEponOnuVlanTrunkModeVlan = _ZxAnEponOnuVlanTrunkModeVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 4, 1, 1),
    _ZxAnEponOnuVlanTrunkModeVlan_Type()
)
zxAnEponOnuVlanTrunkModeVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanTrunkModeVlan.setStatus("current")
_ZxAnEponOnuVlanAggregationTable_Object = MibTable
zxAnEponOnuVlanAggregationTable = _ZxAnEponOnuVlanAggregationTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 5)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVlanAggregationTable.setStatus("current")
_ZxAnEponOnuVlanAggregationEntry_Object = MibTableRow
zxAnEponOnuVlanAggregationEntry = _ZxAnEponOnuVlanAggregationEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 5, 1)
)
zxAnEponOnuVlanAggregationEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuVlanAggGrpId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVlanAggregationEntry.setStatus("current")


class _ZxAnEponOnuVlanAggGrpId_Type(Integer32):
    """Custom type zxAnEponOnuVlanAggGrpId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnEponOnuVlanAggGrpId_Type.__name__ = "Integer32"
_ZxAnEponOnuVlanAggGrpId_Object = MibTableColumn
zxAnEponOnuVlanAggGrpId = _ZxAnEponOnuVlanAggGrpId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 5, 1, 1),
    _ZxAnEponOnuVlanAggGrpId_Type()
)
zxAnEponOnuVlanAggGrpId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanAggGrpId.setStatus("current")
_ZxAnEponOnuVlamAggSrcVlanList_Type = DisplayString
_ZxAnEponOnuVlamAggSrcVlanList_Object = MibTableColumn
zxAnEponOnuVlamAggSrcVlanList = _ZxAnEponOnuVlamAggSrcVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 5, 1, 2),
    _ZxAnEponOnuVlamAggSrcVlanList_Type()
)
zxAnEponOnuVlamAggSrcVlanList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuVlamAggSrcVlanList.setStatus("current")


class _ZxAnEponOnuVlanAggDestVlan_Type(Integer32):
    """Custom type zxAnEponOnuVlanAggDestVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponOnuVlanAggDestVlan_Type.__name__ = "Integer32"
_ZxAnEponOnuVlanAggDestVlan_Object = MibTableColumn
zxAnEponOnuVlanAggDestVlan = _ZxAnEponOnuVlanAggDestVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 5, 1, 3),
    _ZxAnEponOnuVlanAggDestVlan_Type()
)
zxAnEponOnuVlanAggDestVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanAggDestVlan.setStatus("current")
_ZxAnEponOnuVlanAggRowStatus_Type = RowStatus
_ZxAnEponOnuVlanAggRowStatus_Object = MibTableColumn
zxAnEponOnuVlanAggRowStatus = _ZxAnEponOnuVlanAggRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 10, 5, 1, 10),
    _ZxAnEponOnuVlanAggRowStatus_Type()
)
zxAnEponOnuVlanAggRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuVlanAggRowStatus.setStatus("current")
_ZxAnEponOnuClassMarkingAttrMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuClassMarkingAttrMgmt = _ZxAnEponOnuClassMarkingAttrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11)
)
_ZxAnEponOnuClassMarkingConditionTable_Object = MibTable
zxAnEponOnuClassMarkingConditionTable = _ZxAnEponOnuClassMarkingConditionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingConditionTable.setStatus("current")
_ZxAnEponOnuClassMarkingConditionEntry_Object = MibTableRow
zxAnEponOnuClassMarkingConditionEntry = _ZxAnEponOnuClassMarkingConditionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 1, 1)
)
zxAnEponOnuClassMarkingConditionEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuClassMarkingConditionId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingConditionEntry.setStatus("current")
_ZxAnEponOnuClassMarkingConditionId_Type = Integer32
_ZxAnEponOnuClassMarkingConditionId_Object = MibTableColumn
zxAnEponOnuClassMarkingConditionId = _ZxAnEponOnuClassMarkingConditionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 1, 1, 1),
    _ZxAnEponOnuClassMarkingConditionId_Type()
)
zxAnEponOnuClassMarkingConditionId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingConditionId.setStatus("current")


class _ZxAnEponOnuClassMarkingConditionName_Type(OctetString):
    """Custom type zxAnEponOnuClassMarkingConditionName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnEponOnuClassMarkingConditionName_Type.__name__ = "OctetString"
_ZxAnEponOnuClassMarkingConditionName_Object = MibTableColumn
zxAnEponOnuClassMarkingConditionName = _ZxAnEponOnuClassMarkingConditionName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 1, 1, 2),
    _ZxAnEponOnuClassMarkingConditionName_Type()
)
zxAnEponOnuClassMarkingConditionName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingConditionName.setStatus("current")


class _ZxAnEponOnuClassMarkingField_Type(Integer32):
    """Custom type zxAnEponOnuClassMarkingField based on Integer32"""
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
              14)
        )
    )
    namedValues = NamedValues(
        *(("da", 1),
          ("sa", 2),
          ("priority", 3),
          ("vlan", 4),
          ("ethType", 5),
          ("destIp", 6),
          ("srcIp", 7),
          ("ipProtType", 8),
          ("ipV4", 9),
          ("ipV6", 10),
          ("l4SrcPort", 11),
          ("l4DestPort", 12),
          ("linkIndex", 13),
          ("ipPrecedence", 14))
    )


_ZxAnEponOnuClassMarkingField_Type.__name__ = "Integer32"
_ZxAnEponOnuClassMarkingField_Object = MibTableColumn
zxAnEponOnuClassMarkingField = _ZxAnEponOnuClassMarkingField_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 1, 1, 3),
    _ZxAnEponOnuClassMarkingField_Type()
)
zxAnEponOnuClassMarkingField.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingField.setStatus("current")


class _ZxAnEponOnuClassMarkingMatchValue_Type(OctetString):
    """Custom type zxAnEponOnuClassMarkingMatchValue based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_ZxAnEponOnuClassMarkingMatchValue_Type.__name__ = "OctetString"
_ZxAnEponOnuClassMarkingMatchValue_Object = MibTableColumn
zxAnEponOnuClassMarkingMatchValue = _ZxAnEponOnuClassMarkingMatchValue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 1, 1, 4),
    _ZxAnEponOnuClassMarkingMatchValue_Type()
)
zxAnEponOnuClassMarkingMatchValue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingMatchValue.setStatus("current")


class _ZxAnEponOnuClassMarkingOperator_Type(Integer32):
    """Custom type zxAnEponOnuClassMarkingOperator based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("never-match", 1),
          ("equal", 2),
          ("not-equal", 3),
          ("less-and-equal", 4),
          ("greater-and-equal", 5),
          ("exist", 6),
          ("not-exist", 7),
          ("always-match", 8))
    )


_ZxAnEponOnuClassMarkingOperator_Type.__name__ = "Integer32"
_ZxAnEponOnuClassMarkingOperator_Object = MibTableColumn
zxAnEponOnuClassMarkingOperator = _ZxAnEponOnuClassMarkingOperator_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 1, 1, 5),
    _ZxAnEponOnuClassMarkingOperator_Type()
)
zxAnEponOnuClassMarkingOperator.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingOperator.setStatus("current")
_ZxAnEponOnuClassMarkingConditionRefCnt_Type = Integer32
_ZxAnEponOnuClassMarkingConditionRefCnt_Object = MibTableColumn
zxAnEponOnuClassMarkingConditionRefCnt = _ZxAnEponOnuClassMarkingConditionRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 1, 1, 6),
    _ZxAnEponOnuClassMarkingConditionRefCnt_Type()
)
zxAnEponOnuClassMarkingConditionRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingConditionRefCnt.setStatus("current")
_ZxAnEponOnuClassMarkingConditionRowStatus_Type = RowStatus
_ZxAnEponOnuClassMarkingConditionRowStatus_Object = MibTableColumn
zxAnEponOnuClassMarkingConditionRowStatus = _ZxAnEponOnuClassMarkingConditionRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 1, 1, 7),
    _ZxAnEponOnuClassMarkingConditionRowStatus_Type()
)
zxAnEponOnuClassMarkingConditionRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingConditionRowStatus.setStatus("current")
_ZxAnEponOnuClassMarkingRuleTable_Object = MibTable
zxAnEponOnuClassMarkingRuleTable = _ZxAnEponOnuClassMarkingRuleTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleTable.setStatus("current")
_ZxAnEponOnuClassMarkingRuleEntry_Object = MibTableRow
zxAnEponOnuClassMarkingRuleEntry = _ZxAnEponOnuClassMarkingRuleEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 2, 1)
)
zxAnEponOnuClassMarkingRuleEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuClassMarkingRuleId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleEntry.setStatus("current")
_ZxAnEponOnuClassMarkingRuleId_Type = Integer32
_ZxAnEponOnuClassMarkingRuleId_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleId = _ZxAnEponOnuClassMarkingRuleId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 2, 1, 1),
    _ZxAnEponOnuClassMarkingRuleId_Type()
)
zxAnEponOnuClassMarkingRuleId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleId.setStatus("current")


class _ZxAnEponOnuClassMarkingRuleName_Type(OctetString):
    """Custom type zxAnEponOnuClassMarkingRuleName based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnEponOnuClassMarkingRuleName_Type.__name__ = "OctetString"
_ZxAnEponOnuClassMarkingRuleName_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleName = _ZxAnEponOnuClassMarkingRuleName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 2, 1, 2),
    _ZxAnEponOnuClassMarkingRuleName_Type()
)
zxAnEponOnuClassMarkingRuleName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleName.setStatus("current")
_ZxAnEponOnuClassMarkingQueue_Type = Integer32
_ZxAnEponOnuClassMarkingQueue_Object = MibTableColumn
zxAnEponOnuClassMarkingQueue = _ZxAnEponOnuClassMarkingQueue_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 2, 1, 3),
    _ZxAnEponOnuClassMarkingQueue_Type()
)
zxAnEponOnuClassMarkingQueue.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingQueue.setStatus("current")


class _ZxAnEponOnuClassMarkingPriority_Type(Integer32):
    """Custom type zxAnEponOnuClassMarkingPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnEponOnuClassMarkingPriority_Type.__name__ = "Integer32"
_ZxAnEponOnuClassMarkingPriority_Object = MibTableColumn
zxAnEponOnuClassMarkingPriority = _ZxAnEponOnuClassMarkingPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 2, 1, 4),
    _ZxAnEponOnuClassMarkingPriority_Type()
)
zxAnEponOnuClassMarkingPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingPriority.setStatus("current")
_ZxAnEponOnuClassMarkingRuleRefCnt_Type = Integer32
_ZxAnEponOnuClassMarkingRuleRefCnt_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleRefCnt = _ZxAnEponOnuClassMarkingRuleRefCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 2, 1, 5),
    _ZxAnEponOnuClassMarkingRuleRefCnt_Type()
)
zxAnEponOnuClassMarkingRuleRefCnt.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleRefCnt.setStatus("current")
_ZxAnEponOnuClassMarkingRuleRowStatus_Type = RowStatus
_ZxAnEponOnuClassMarkingRuleRowStatus_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleRowStatus = _ZxAnEponOnuClassMarkingRuleRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 2, 1, 6),
    _ZxAnEponOnuClassMarkingRuleRowStatus_Type()
)
zxAnEponOnuClassMarkingRuleRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleRowStatus.setStatus("current")
_ZxAnEponOnuClassMarkingTable_Object = MibTable
zxAnEponOnuClassMarkingTable = _ZxAnEponOnuClassMarkingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 3)
)
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingTable.setStatus("current")
_ZxAnEponOnuClassMarkingEntry_Object = MibTableRow
zxAnEponOnuClassMarkingEntry = _ZxAnEponOnuClassMarkingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 3, 1)
)
zxAnEponOnuClassMarkingEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuClassMarkingRulePrecedence"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingEntry.setStatus("current")
_ZxAnEponOnuClassMarkingRulePrecedence_Type = Integer32
_ZxAnEponOnuClassMarkingRulePrecedence_Object = MibTableColumn
zxAnEponOnuClassMarkingRulePrecedence = _ZxAnEponOnuClassMarkingRulePrecedence_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 3, 1, 1),
    _ZxAnEponOnuClassMarkingRulePrecedence_Type()
)
zxAnEponOnuClassMarkingRulePrecedence.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRulePrecedence.setStatus("current")
_ZxAnEponOnuClassMarkingRuleIndex_Type = Integer32
_ZxAnEponOnuClassMarkingRuleIndex_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleIndex = _ZxAnEponOnuClassMarkingRuleIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 3, 1, 2),
    _ZxAnEponOnuClassMarkingRuleIndex_Type()
)
zxAnEponOnuClassMarkingRuleIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleIndex.setStatus("current")
_ZxAnEponOnuClassMarkingRuleConditionList_Type = OctetString
_ZxAnEponOnuClassMarkingRuleConditionList_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleConditionList = _ZxAnEponOnuClassMarkingRuleConditionList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 3, 1, 3),
    _ZxAnEponOnuClassMarkingRuleConditionList_Type()
)
zxAnEponOnuClassMarkingRuleConditionList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleConditionList.setStatus("current")
_ZxAnEponOnuClassMarkingRowStatus_Type = RowStatus
_ZxAnEponOnuClassMarkingRowStatus_Object = MibTableColumn
zxAnEponOnuClassMarkingRowStatus = _ZxAnEponOnuClassMarkingRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 3, 1, 4),
    _ZxAnEponOnuClassMarkingRowStatus_Type()
)
zxAnEponOnuClassMarkingRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRowStatus.setStatus("current")
_ZxAnEponOnuClassMarkingRulePriority_Type = Integer32
_ZxAnEponOnuClassMarkingRulePriority_Object = MibTableColumn
zxAnEponOnuClassMarkingRulePriority = _ZxAnEponOnuClassMarkingRulePriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 3, 1, 5),
    _ZxAnEponOnuClassMarkingRulePriority_Type()
)
zxAnEponOnuClassMarkingRulePriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRulePriority.setStatus("current")


class _ZxAnEponOnuClassMarkingRuleDirection_Type(Integer32):
    """Custom type zxAnEponOnuClassMarkingRuleDirection based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("downstream", 1),
          ("upstream", 2))
    )


_ZxAnEponOnuClassMarkingRuleDirection_Type.__name__ = "Integer32"
_ZxAnEponOnuClassMarkingRuleDirection_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleDirection = _ZxAnEponOnuClassMarkingRuleDirection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 3, 1, 6),
    _ZxAnEponOnuClassMarkingRuleDirection_Type()
)
zxAnEponOnuClassMarkingRuleDirection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleDirection.setStatus("current")


class _ZxAnEponOnuClassMarkingRuleType_Type(Integer32):
    """Custom type zxAnEponOnuClassMarkingRuleType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("classification", 1),
          ("filter", 2))
    )


_ZxAnEponOnuClassMarkingRuleType_Type.__name__ = "Integer32"
_ZxAnEponOnuClassMarkingRuleType_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleType = _ZxAnEponOnuClassMarkingRuleType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 3, 1, 7),
    _ZxAnEponOnuClassMarkingRuleType_Type()
)
zxAnEponOnuClassMarkingRuleType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleType.setStatus("current")
_ZxAnEponOnuClassMarkingClearTable_Object = MibTable
zxAnEponOnuClassMarkingClearTable = _ZxAnEponOnuClassMarkingClearTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 4)
)
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingClearTable.setStatus("current")
_ZxAnEponOnuClassMarkingClearEntry_Object = MibTableRow
zxAnEponOnuClassMarkingClearEntry = _ZxAnEponOnuClassMarkingClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 4, 1)
)
zxAnEponOnuClassMarkingClearEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingClearEntry.setStatus("current")
_ZxAnEponOnuClassMarkingClear_Type = Integer32
_ZxAnEponOnuClassMarkingClear_Object = MibTableColumn
zxAnEponOnuClassMarkingClear = _ZxAnEponOnuClassMarkingClear_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 4, 1, 1),
    _ZxAnEponOnuClassMarkingClear_Type()
)
zxAnEponOnuClassMarkingClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingClear.setStatus("current")
_ZxAnEponOnuClassMarkingCompatibilityTable_Object = MibTable
zxAnEponOnuClassMarkingCompatibilityTable = _ZxAnEponOnuClassMarkingCompatibilityTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 101)
)
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingCompatibilityTable.setStatus("current")
_ZxAnEponOnuClassMarkingCompatibilityEntry_Object = MibTableRow
zxAnEponOnuClassMarkingCompatibilityEntry = _ZxAnEponOnuClassMarkingCompatibilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 101, 1)
)
zxAnEponOnuClassMarkingCompatibilityEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingCompatibilityEntry.setStatus("current")


class _ZxAnEponOnuClassMarkingRulePriorityFlag_Type(Integer32):
    """Custom type zxAnEponOnuClassMarkingRulePriorityFlag based on Integer32"""
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


_ZxAnEponOnuClassMarkingRulePriorityFlag_Type.__name__ = "Integer32"
_ZxAnEponOnuClassMarkingRulePriorityFlag_Object = MibTableColumn
zxAnEponOnuClassMarkingRulePriorityFlag = _ZxAnEponOnuClassMarkingRulePriorityFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 101, 1, 1),
    _ZxAnEponOnuClassMarkingRulePriorityFlag_Type()
)
zxAnEponOnuClassMarkingRulePriorityFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRulePriorityFlag.setStatus("current")


class _ZxAnEponOnuClassMarkingRuleDirectionFlag_Type(Integer32):
    """Custom type zxAnEponOnuClassMarkingRuleDirectionFlag based on Integer32"""
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


_ZxAnEponOnuClassMarkingRuleDirectionFlag_Type.__name__ = "Integer32"
_ZxAnEponOnuClassMarkingRuleDirectionFlag_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleDirectionFlag = _ZxAnEponOnuClassMarkingRuleDirectionFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 101, 1, 2),
    _ZxAnEponOnuClassMarkingRuleDirectionFlag_Type()
)
zxAnEponOnuClassMarkingRuleDirectionFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleDirectionFlag.setStatus("current")


class _ZxAnEponOnuClassMarkingRuleTypeFlag_Type(Integer32):
    """Custom type zxAnEponOnuClassMarkingRuleTypeFlag based on Integer32"""
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


_ZxAnEponOnuClassMarkingRuleTypeFlag_Type.__name__ = "Integer32"
_ZxAnEponOnuClassMarkingRuleTypeFlag_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleTypeFlag = _ZxAnEponOnuClassMarkingRuleTypeFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 11, 101, 1, 3),
    _ZxAnEponOnuClassMarkingRuleTypeFlag_Type()
)
zxAnEponOnuClassMarkingRuleTypeFlag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleTypeFlag.setStatus("current")
_ZxAnEponOnuMulticastVlanTable_Object = MibTable
zxAnEponOnuMulticastVlanTable = _ZxAnEponOnuMulticastVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 12)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastVlanTable.setStatus("current")
_ZxAnEponOnuMulticastVlanEntry_Object = MibTableRow
zxAnEponOnuMulticastVlanEntry = _ZxAnEponOnuMulticastVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 12, 1)
)
zxAnEponOnuMulticastVlanEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastVlanEntry.setStatus("current")


class _ZxAnEponOnuMulticastVlanAction_Type(Integer32):
    """Custom type zxAnEponOnuMulticastVlanAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 0),
          ("add", 1),
          ("clear", 2))
    )


_ZxAnEponOnuMulticastVlanAction_Type.__name__ = "Integer32"
_ZxAnEponOnuMulticastVlanAction_Object = MibTableColumn
zxAnEponOnuMulticastVlanAction = _ZxAnEponOnuMulticastVlanAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 12, 1, 1),
    _ZxAnEponOnuMulticastVlanAction_Type()
)
zxAnEponOnuMulticastVlanAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastVlanAction.setStatus("current")
_ZxAnEponOnuMulticastVlanList_Type = OctetString
_ZxAnEponOnuMulticastVlanList_Object = MibTableColumn
zxAnEponOnuMulticastVlanList = _ZxAnEponOnuMulticastVlanList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 12, 1, 2),
    _ZxAnEponOnuMulticastVlanList_Type()
)
zxAnEponOnuMulticastVlanList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastVlanList.setStatus("current")
_ZxAnEponOnuMulticastTagCfgTable_Object = MibTable
zxAnEponOnuMulticastTagCfgTable = _ZxAnEponOnuMulticastTagCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 13)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastTagCfgTable.setStatus("current")
_ZxAnEponOnuMulticastTagCfgEntry_Object = MibTableRow
zxAnEponOnuMulticastTagCfgEntry = _ZxAnEponOnuMulticastTagCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 13, 1)
)
zxAnEponOnuMulticastTagCfgEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastTagCfgEntry.setStatus("current")


class _ZxAnEponOnuMulticastTagStripe_Type(Integer32):
    """Custom type zxAnEponOnuMulticastTagStripe based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("not-striped", 1),
          ("striped", 2),
          ("tagSwitch", 3))
    )


_ZxAnEponOnuMulticastTagStripe_Type.__name__ = "Integer32"
_ZxAnEponOnuMulticastTagStripe_Object = MibTableColumn
zxAnEponOnuMulticastTagStripe = _ZxAnEponOnuMulticastTagStripe_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 13, 1, 1),
    _ZxAnEponOnuMulticastTagStripe_Type()
)
zxAnEponOnuMulticastTagStripe.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastTagStripe.setStatus("current")
_ZxAnEponOnuMulticastSwitchTable_Object = MibTable
zxAnEponOnuMulticastSwitchTable = _ZxAnEponOnuMulticastSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 14)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastSwitchTable.setStatus("current")
_ZxAnEponOnuMulticastSwitchEntry_Object = MibTableRow
zxAnEponOnuMulticastSwitchEntry = _ZxAnEponOnuMulticastSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 14, 1)
)
zxAnEponOnuMulticastSwitchEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastSwitchEntry.setStatus("current")


class _ZxAnEponOnuMulticastSwitchAttr_Type(Integer32):
    """Custom type zxAnEponOnuMulticastSwitchAttr based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("igmpsnooping", 1),
          ("ctrl-multicast", 2))
    )


_ZxAnEponOnuMulticastSwitchAttr_Type.__name__ = "Integer32"
_ZxAnEponOnuMulticastSwitchAttr_Object = MibTableColumn
zxAnEponOnuMulticastSwitchAttr = _ZxAnEponOnuMulticastSwitchAttr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 14, 1, 1),
    _ZxAnEponOnuMulticastSwitchAttr_Type()
)
zxAnEponOnuMulticastSwitchAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastSwitchAttr.setStatus("current")
_ZxAnEponOnuMulticastControlMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuMulticastControlMgmt = _ZxAnEponOnuMulticastControlMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15)
)
_ZxAnEponOnuMulticastControlClearTable_Object = MibTable
zxAnEponOnuMulticastControlClearTable = _ZxAnEponOnuMulticastControlClearTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastControlClearTable.setStatus("current")
_ZxAnEponOnuMulticastControlClearEntry_Object = MibTableRow
zxAnEponOnuMulticastControlClearEntry = _ZxAnEponOnuMulticastControlClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 1, 1)
)
zxAnEponOnuMulticastControlClearEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastControlClearEntry.setStatus("current")
_ZxAnEponOnuMcstCtrlClear_Type = Integer32
_ZxAnEponOnuMcstCtrlClear_Object = MibTableColumn
zxAnEponOnuMcstCtrlClear = _ZxAnEponOnuMcstCtrlClear_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 1, 1, 1),
    _ZxAnEponOnuMcstCtrlClear_Type()
)
zxAnEponOnuMcstCtrlClear.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMcstCtrlClear.setStatus("current")
_ZxAnEponOnuMulticastControlTable_Object = MibTable
zxAnEponOnuMulticastControlTable = _ZxAnEponOnuMulticastControlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastControlTable.setStatus("current")
_ZxAnEponOnuMulticastControlEntry_Object = MibTableRow
zxAnEponOnuMulticastControlEntry = _ZxAnEponOnuMulticastControlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 2, 1)
)
zxAnEponOnuMulticastControlEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuMcstCtrlEntryIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMulticastControlEntry.setStatus("current")
_ZxAnEponOnuMcstCtrlEntryIndex_Type = Integer32
_ZxAnEponOnuMcstCtrlEntryIndex_Object = MibTableColumn
zxAnEponOnuMcstCtrlEntryIndex = _ZxAnEponOnuMcstCtrlEntryIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 2, 1, 1),
    _ZxAnEponOnuMcstCtrlEntryIndex_Type()
)
zxAnEponOnuMcstCtrlEntryIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuMcstCtrlEntryIndex.setStatus("current")


class _ZxAnEponOnuMcstCtrlAction_Type(Integer32):
    """Custom type zxAnEponOnuMcstCtrlAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("delete", 1),
          ("add", 2))
    )


_ZxAnEponOnuMcstCtrlAction_Type.__name__ = "Integer32"
_ZxAnEponOnuMcstCtrlAction_Object = MibTableColumn
zxAnEponOnuMcstCtrlAction = _ZxAnEponOnuMcstCtrlAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 2, 1, 2),
    _ZxAnEponOnuMcstCtrlAction_Type()
)
zxAnEponOnuMcstCtrlAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMcstCtrlAction.setStatus("current")


class _ZxAnEponOnuMcstCtrlType_Type(Integer32):
    """Custom type zxAnEponOnuMcstCtrlType based on Integer32"""
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
        *(("gda", 1),
          ("gda-and-vlan", 2),
          ("gda-and-sa", 3),
          ("gip-and-vlan", 4))
    )


_ZxAnEponOnuMcstCtrlType_Type.__name__ = "Integer32"
_ZxAnEponOnuMcstCtrlType_Object = MibTableColumn
zxAnEponOnuMcstCtrlType = _ZxAnEponOnuMcstCtrlType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 2, 1, 3),
    _ZxAnEponOnuMcstCtrlType_Type()
)
zxAnEponOnuMcstCtrlType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMcstCtrlType.setStatus("current")


class _ZxAnEponOnuMcstCtrlUserId_Type(Integer32):
    """Custom type zxAnEponOnuMcstCtrlUserId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponOnuMcstCtrlUserId_Type.__name__ = "Integer32"
_ZxAnEponOnuMcstCtrlUserId_Object = MibTableColumn
zxAnEponOnuMcstCtrlUserId = _ZxAnEponOnuMcstCtrlUserId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 2, 1, 4),
    _ZxAnEponOnuMcstCtrlUserId_Type()
)
zxAnEponOnuMcstCtrlUserId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMcstCtrlUserId.setStatus("current")
_ZxAnEponOnuMcstCtrlGda_Type = MacAddress
_ZxAnEponOnuMcstCtrlGda_Object = MibTableColumn
zxAnEponOnuMcstCtrlGda = _ZxAnEponOnuMcstCtrlGda_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 2, 1, 5),
    _ZxAnEponOnuMcstCtrlGda_Type()
)
zxAnEponOnuMcstCtrlGda.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMcstCtrlGda.setStatus("current")


class _ZxAnEponOnuMcstCtrlMvlan_Type(Integer32):
    """Custom type zxAnEponOnuMcstCtrlMvlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponOnuMcstCtrlMvlan_Type.__name__ = "Integer32"
_ZxAnEponOnuMcstCtrlMvlan_Object = MibTableColumn
zxAnEponOnuMcstCtrlMvlan = _ZxAnEponOnuMcstCtrlMvlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 2, 1, 6),
    _ZxAnEponOnuMcstCtrlMvlan_Type()
)
zxAnEponOnuMcstCtrlMvlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMcstCtrlMvlan.setStatus("current")
_ZxAnEponOnuMcstCtrlGdaIp_Type = IpAddress
_ZxAnEponOnuMcstCtrlGdaIp_Object = MibTableColumn
zxAnEponOnuMcstCtrlGdaIp = _ZxAnEponOnuMcstCtrlGdaIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 15, 2, 1, 7),
    _ZxAnEponOnuMcstCtrlGdaIp_Type()
)
zxAnEponOnuMcstCtrlGdaIp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMcstCtrlGdaIp.setStatus("current")
_ZxAnEponOnuMaxGroupNumTable_Object = MibTable
zxAnEponOnuMaxGroupNumTable = _ZxAnEponOnuMaxGroupNumTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 16)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMaxGroupNumTable.setStatus("current")
_ZxAnEponOnuMaxGroupNumEntry_Object = MibTableRow
zxAnEponOnuMaxGroupNumEntry = _ZxAnEponOnuMaxGroupNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 16, 1)
)
zxAnEponOnuMaxGroupNumEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMaxGroupNumEntry.setStatus("current")


class _ZxAnEponOnuMaxGroupNum_Type(Integer32):
    """Custom type zxAnEponOnuMaxGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnEponOnuMaxGroupNum_Type.__name__ = "Integer32"
_ZxAnEponOnuMaxGroupNum_Object = MibTableColumn
zxAnEponOnuMaxGroupNum = _ZxAnEponOnuMaxGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 16, 1, 1),
    _ZxAnEponOnuMaxGroupNum_Type()
)
zxAnEponOnuMaxGroupNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMaxGroupNum.setStatus("current")
_ZxAnEponOnuAlarmCtrlTable_Object = MibTable
zxAnEponOnuAlarmCtrlTable = _ZxAnEponOnuAlarmCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 17)
)
if mibBuilder.loadTexts:
    zxAnEponOnuAlarmCtrlTable.setStatus("current")
_ZxAnEponOnuAlarmCtrlEntry_Object = MibTableRow
zxAnEponOnuAlarmCtrlEntry = _ZxAnEponOnuAlarmCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 17, 1)
)
zxAnEponOnuAlarmCtrlEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuAlarmCtrlEntry.setStatus("current")


class _ZxAnEponOnuAlarmCtr_Type(Integer32):
    """Custom type zxAnEponOnuAlarmCtr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuAlarmCtr_Type.__name__ = "Integer32"
_ZxAnEponOnuAlarmCtr_Object = MibTableColumn
zxAnEponOnuAlarmCtr = _ZxAnEponOnuAlarmCtr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 17, 1, 1),
    _ZxAnEponOnuAlarmCtr_Type()
)
zxAnEponOnuAlarmCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuAlarmCtr.setStatus("current")
_ZxAnEponOnuMACNumTable_Object = MibTable
zxAnEponOnuMACNumTable = _ZxAnEponOnuMACNumTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 18)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMACNumTable.setStatus("current")
_ZxAnEponOnuMACNumEntry_Object = MibTableRow
zxAnEponOnuMACNumEntry = _ZxAnEponOnuMACNumEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 18, 1)
)
zxAnEponOnuMACNumEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMACNumEntry.setStatus("current")


class _ZxAnEponOnuMACNum_Type(Integer32):
    """Custom type zxAnEponOnuMACNum based on Integer32"""
    defaultValue = 65535

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEponOnuMACNum_Type.__name__ = "Integer32"
_ZxAnEponOnuMACNum_Object = MibTableColumn
zxAnEponOnuMACNum = _ZxAnEponOnuMACNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 18, 1, 1),
    _ZxAnEponOnuMACNum_Type()
)
zxAnEponOnuMACNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMACNum.setStatus("current")


class _ZxAnEponOnuUniLearnedMacs_Type(Integer32):
    """Custom type zxAnEponOnuUniLearnedMacs based on Integer32"""
    defaultValue = 0


_ZxAnEponOnuUniLearnedMacs_Type.__name__ = "Integer32"
_ZxAnEponOnuUniLearnedMacs_Object = MibTableColumn
zxAnEponOnuUniLearnedMacs = _ZxAnEponOnuUniLearnedMacs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 18, 1, 2),
    _ZxAnEponOnuUniLearnedMacs_Type()
)
zxAnEponOnuUniLearnedMacs.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuUniLearnedMacs.setStatus("current")
_ZxAnEponOnuMACAgingTimeTable_Object = MibTable
zxAnEponOnuMACAgingTimeTable = _ZxAnEponOnuMACAgingTimeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 19)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMACAgingTimeTable.setStatus("current")
_ZxAnEponOnuMACAgingTimeEntry_Object = MibTableRow
zxAnEponOnuMACAgingTimeEntry = _ZxAnEponOnuMACAgingTimeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 19, 1)
)
zxAnEponOnuMACAgingTimeEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMACAgingTimeEntry.setStatus("current")


class _ZxAnEponOnuMACAgingTimeAttr_Type(Integer32):
    """Custom type zxAnEponOnuMACAgingTimeAttr based on Integer32"""
    defaultValue = 300

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 86400),
    )


_ZxAnEponOnuMACAgingTimeAttr_Type.__name__ = "Integer32"
_ZxAnEponOnuMACAgingTimeAttr_Object = MibTableColumn
zxAnEponOnuMACAgingTimeAttr = _ZxAnEponOnuMACAgingTimeAttr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 19, 1, 1),
    _ZxAnEponOnuMACAgingTimeAttr_Type()
)
zxAnEponOnuMACAgingTimeAttr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMACAgingTimeAttr.setStatus("current")
_ZxAnEponOnuFilterMACTable_Object = MibTable
zxAnEponOnuFilterMACTable = _ZxAnEponOnuFilterMACTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 20)
)
if mibBuilder.loadTexts:
    zxAnEponOnuFilterMACTable.setStatus("current")
_ZxAnEponOnuFilterMACEntry_Object = MibTableRow
zxAnEponOnuFilterMACEntry = _ZxAnEponOnuFilterMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 20, 1)
)
zxAnEponOnuFilterMACEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuFilterMAC"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxEponFilterVlan"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuFilterMACEntry.setStatus("current")
_ZxAnEponOnuFilterMAC_Type = MacAddress
_ZxAnEponOnuFilterMAC_Object = MibTableColumn
zxAnEponOnuFilterMAC = _ZxAnEponOnuFilterMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 20, 1, 1),
    _ZxAnEponOnuFilterMAC_Type()
)
zxAnEponOnuFilterMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuFilterMAC.setStatus("current")


class _ZxEponFilterVlan_Type(Integer32):
    """Custom type zxEponFilterVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxEponFilterVlan_Type.__name__ = "Integer32"
_ZxEponFilterVlan_Object = MibTableColumn
zxEponFilterVlan = _ZxEponFilterVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 20, 1, 2),
    _ZxEponFilterVlan_Type()
)
zxEponFilterVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxEponFilterVlan.setStatus("current")
_ZxAnEponOnuFilterMACEntryStatus_Type = RowStatus
_ZxAnEponOnuFilterMACEntryStatus_Object = MibTableColumn
zxAnEponOnuFilterMACEntryStatus = _ZxAnEponOnuFilterMACEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 20, 1, 3),
    _ZxAnEponOnuFilterMACEntryStatus_Type()
)
zxAnEponOnuFilterMACEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuFilterMACEntryStatus.setStatus("current")
_ZxAnEponOnuBindMACTable_Object = MibTable
zxAnEponOnuBindMACTable = _ZxAnEponOnuBindMACTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 21)
)
if mibBuilder.loadTexts:
    zxAnEponOnuBindMACTable.setStatus("current")
_ZxAnEponOnuBindMACEntry_Object = MibTableRow
zxAnEponOnuBindMACEntry = _ZxAnEponOnuBindMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 21, 1)
)
zxAnEponOnuBindMACEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuBindMAC"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxEponBindVlan"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuBindMACEntry.setStatus("current")
_ZxAnEponOnuBindMAC_Type = MacAddress
_ZxAnEponOnuBindMAC_Object = MibTableColumn
zxAnEponOnuBindMAC = _ZxAnEponOnuBindMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 21, 1, 1),
    _ZxAnEponOnuBindMAC_Type()
)
zxAnEponOnuBindMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuBindMAC.setStatus("current")


class _ZxEponBindVlan_Type(Integer32):
    """Custom type zxEponBindVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxEponBindVlan_Type.__name__ = "Integer32"
_ZxEponBindVlan_Object = MibTableColumn
zxEponBindVlan = _ZxEponBindVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 21, 1, 2),
    _ZxEponBindVlan_Type()
)
zxEponBindVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxEponBindVlan.setStatus("current")
_ZxAnEponOnuBindMACEntryStatus_Type = RowStatus
_ZxAnEponOnuBindMACEntryStatus_Object = MibTableColumn
zxAnEponOnuBindMACEntryStatus = _ZxAnEponOnuBindMACEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 21, 1, 3),
    _ZxAnEponOnuBindMACEntryStatus_Type()
)
zxAnEponOnuBindMACEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuBindMACEntryStatus.setStatus("current")
_ZxAnEponOnuStaticMACTable_Object = MibTable
zxAnEponOnuStaticMACTable = _ZxAnEponOnuStaticMACTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 22)
)
if mibBuilder.loadTexts:
    zxAnEponOnuStaticMACTable.setStatus("current")
_ZxAnEponOnuStaticMACEntry_Object = MibTableRow
zxAnEponOnuStaticMACEntry = _ZxAnEponOnuStaticMACEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 22, 1)
)
zxAnEponOnuStaticMACEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuStaticMAC"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxEponStaticVlan"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuStaticMACEntry.setStatus("current")
_ZxAnEponOnuStaticMAC_Type = MacAddress
_ZxAnEponOnuStaticMAC_Object = MibTableColumn
zxAnEponOnuStaticMAC = _ZxAnEponOnuStaticMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 22, 1, 1),
    _ZxAnEponOnuStaticMAC_Type()
)
zxAnEponOnuStaticMAC.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuStaticMAC.setStatus("current")


class _ZxEponStaticVlan_Type(Integer32):
    """Custom type zxEponStaticVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxEponStaticVlan_Type.__name__ = "Integer32"
_ZxEponStaticVlan_Object = MibTableColumn
zxEponStaticVlan = _ZxEponStaticVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 22, 1, 2),
    _ZxEponStaticVlan_Type()
)
zxEponStaticVlan.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxEponStaticVlan.setStatus("current")
_ZxAnEponOnuStaicMACEntryStatus_Type = RowStatus
_ZxAnEponOnuStaicMACEntryStatus_Object = MibTableColumn
zxAnEponOnuStaicMACEntryStatus = _ZxAnEponOnuStaicMACEntryStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 22, 1, 3),
    _ZxAnEponOnuStaicMACEntryStatus_Type()
)
zxAnEponOnuStaicMACEntryStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuStaicMACEntryStatus.setStatus("current")
_ZxAnEponOnuMACAddressClearTable_Object = MibTable
zxAnEponOnuMACAddressClearTable = _ZxAnEponOnuMACAddressClearTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 23)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMACAddressClearTable.setStatus("current")
_ZxAnEponOnuMACAddressClearEntry_Object = MibTableRow
zxAnEponOnuMACAddressClearEntry = _ZxAnEponOnuMACAddressClearEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 23, 1)
)
zxAnEponOnuMACAddressClearEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMACAddressClearEntry.setStatus("current")


class _ZxAnEponOnuMACAddressType_Type(Integer32):
    """Custom type zxAnEponOnuMACAddressType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("filter", 1),
          ("bind", 2),
          ("static", 3))
    )


_ZxAnEponOnuMACAddressType_Type.__name__ = "Integer32"
_ZxAnEponOnuMACAddressType_Object = MibTableColumn
zxAnEponOnuMACAddressType = _ZxAnEponOnuMACAddressType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 23, 1, 1),
    _ZxAnEponOnuMACAddressType_Type()
)
zxAnEponOnuMACAddressType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMACAddressType.setStatus("current")
_ZxAnEponOnuManagerIPTable_Object = MibTable
zxAnEponOnuManagerIPTable = _ZxAnEponOnuManagerIPTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24)
)
if mibBuilder.loadTexts:
    zxAnEponOnuManagerIPTable.setStatus("current")
_ZxAnEponOnuManagerIPTableEntry_Object = MibTableRow
zxAnEponOnuManagerIPTableEntry = _ZxAnEponOnuManagerIPTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24, 1)
)
zxAnEponOnuManagerIPTableEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuManagerIPTableEntry.setStatus("current")
_ZxEponOnuIPAddress_Type = IpAddress
_ZxEponOnuIPAddress_Object = MibTableColumn
zxEponOnuIPAddress = _ZxEponOnuIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24, 1, 1),
    _ZxEponOnuIPAddress_Type()
)
zxEponOnuIPAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuIPAddress.setStatus("current")
_ZxEponOnuIPMask_Type = IpAddress
_ZxEponOnuIPMask_Object = MibTableColumn
zxEponOnuIPMask = _ZxEponOnuIPMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24, 1, 2),
    _ZxEponOnuIPMask_Type()
)
zxEponOnuIPMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuIPMask.setStatus("current")


class _ZxEponMangementPriority_Type(Integer32):
    """Custom type zxEponMangementPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxEponMangementPriority_Type.__name__ = "Integer32"
_ZxEponMangementPriority_Object = MibTableColumn
zxEponMangementPriority = _ZxEponMangementPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24, 1, 3),
    _ZxEponMangementPriority_Type()
)
zxEponMangementPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMangementPriority.setStatus("current")


class _ZxEponMangementVlan_Type(Integer32):
    """Custom type zxEponMangementVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxEponMangementVlan_Type.__name__ = "Integer32"
_ZxEponMangementVlan_Object = MibTableColumn
zxEponMangementVlan = _ZxEponMangementVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24, 1, 4),
    _ZxEponMangementVlan_Type()
)
zxEponMangementVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMangementVlan.setStatus("current")
_ZxEponManagementHostIP_Type = IpAddress
_ZxEponManagementHostIP_Object = MibTableColumn
zxEponManagementHostIP = _ZxEponManagementHostIP_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24, 1, 5),
    _ZxEponManagementHostIP_Type()
)
zxEponManagementHostIP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponManagementHostIP.setStatus("current")
_ZxEponManagementHostMask_Type = IpAddress
_ZxEponManagementHostMask_Object = MibTableColumn
zxEponManagementHostMask = _ZxEponManagementHostMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24, 1, 6),
    _ZxEponManagementHostMask_Type()
)
zxEponManagementHostMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponManagementHostMask.setStatus("current")
_ZxEponManagementGateway_Type = IpAddress
_ZxEponManagementGateway_Object = MibTableColumn
zxEponManagementGateway = _ZxEponManagementGateway_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24, 1, 7),
    _ZxEponManagementGateway_Type()
)
zxEponManagementGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponManagementGateway.setStatus("current")


class _ZxEponOnuIPConfigureStatus_Type(Integer32):
    """Custom type zxEponOnuIPConfigureStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxEponOnuIPConfigureStatus_Type.__name__ = "Integer32"
_ZxEponOnuIPConfigureStatus_Object = MibTableColumn
zxEponOnuIPConfigureStatus = _ZxEponOnuIPConfigureStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24, 1, 8),
    _ZxEponOnuIPConfigureStatus_Type()
)
zxEponOnuIPConfigureStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuIPConfigureStatus.setStatus("current")


class _ZxEponMangementSVlan_Type(Integer32):
    """Custom type zxEponMangementSVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_ZxEponMangementSVlan_Type.__name__ = "Integer32"
_ZxEponMangementSVlan_Object = MibTableColumn
zxEponMangementSVlan = _ZxEponMangementSVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 24, 1, 9),
    _ZxEponMangementSVlan_Type()
)
zxEponMangementSVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMangementSVlan.setStatus("current")
_ZxAnEponOnuIsolationCtrlTable_Object = MibTable
zxAnEponOnuIsolationCtrlTable = _ZxAnEponOnuIsolationCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 25)
)
if mibBuilder.loadTexts:
    zxAnEponOnuIsolationCtrlTable.setStatus("current")
_ZxAnEponOnuIsolationCtrlEntry_Object = MibTableRow
zxAnEponOnuIsolationCtrlEntry = _ZxAnEponOnuIsolationCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 25, 1)
)
zxAnEponOnuIsolationCtrlEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuIsolationCtrlEntry.setStatus("current")


class _ZxAnEponOnuIsolationCtr_Type(Integer32):
    """Custom type zxAnEponOnuIsolationCtr based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuIsolationCtr_Type.__name__ = "Integer32"
_ZxAnEponOnuIsolationCtr_Object = MibTableColumn
zxAnEponOnuIsolationCtr = _ZxAnEponOnuIsolationCtr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 25, 1, 1),
    _ZxAnEponOnuIsolationCtr_Type()
)
zxAnEponOnuIsolationCtr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuIsolationCtr.setStatus("current")
_ZxAnEponRmFastLeaveAbiTable_Object = MibTable
zxAnEponRmFastLeaveAbiTable = _ZxAnEponRmFastLeaveAbiTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 26)
)
if mibBuilder.loadTexts:
    zxAnEponRmFastLeaveAbiTable.setStatus("current")
_ZxAnEponRmFastLeaveAbiEntry_Object = MibTableRow
zxAnEponRmFastLeaveAbiEntry = _ZxAnEponRmFastLeaveAbiEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 26, 1)
)
zxAnEponRmFastLeaveAbiEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmFastLeaveAbiEntry.setStatus("current")
_Fastleaveabi_Type = Integer32
_Fastleaveabi_Object = MibTableColumn
fastleaveabi = _Fastleaveabi_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 26, 1, 1),
    _Fastleaveabi_Type()
)
fastleaveabi.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    fastleaveabi.setStatus("current")
_EponRmFastLeaveAdminStateTable_Object = MibTable
eponRmFastLeaveAdminStateTable = _EponRmFastLeaveAdminStateTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 27)
)
if mibBuilder.loadTexts:
    eponRmFastLeaveAdminStateTable.setStatus("current")
_EponRmFastLeaveAdminStateEntry_Object = MibTableRow
eponRmFastLeaveAdminStateEntry = _EponRmFastLeaveAdminStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 27, 1)
)
eponRmFastLeaveAdminStateEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    eponRmFastLeaveAdminStateEntry.setStatus("current")


class _GetState_Type(Integer32):
    """Custom type getState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noResult", 0),
          ("disable", 1),
          ("enable", 2))
    )


_GetState_Type.__name__ = "Integer32"
_GetState_Object = MibTableColumn
getState = _GetState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 27, 1, 1),
    _GetState_Type()
)
getState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    getState.setStatus("current")
_EponIpGlobalTable_Object = MibTable
eponIpGlobalTable = _EponIpGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28)
)
if mibBuilder.loadTexts:
    eponIpGlobalTable.setStatus("current")
_EponIpGlobalEntry_Object = MibTableRow
eponIpGlobalEntry = _EponIpGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1)
)
eponIpGlobalEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuVioceCardIndex"),
)
if mibBuilder.loadTexts:
    eponIpGlobalEntry.setStatus("current")
_ZxAnEponOnuVioceCardIndex_Type = Integer32
_ZxAnEponOnuVioceCardIndex_Object = MibTableColumn
zxAnEponOnuVioceCardIndex = _ZxAnEponOnuVioceCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 1),
    _ZxAnEponOnuVioceCardIndex_Type()
)
zxAnEponOnuVioceCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuVioceCardIndex.setStatus("current")


class _ZxAnEponOnuVoiceIpMngIpRelation_Type(Integer32):
    """Custom type zxAnEponOnuVoiceIpMngIpRelation based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("standalone", 1),
          ("useVOIPIP", 2))
    )


_ZxAnEponOnuVoiceIpMngIpRelation_Type.__name__ = "Integer32"
_ZxAnEponOnuVoiceIpMngIpRelation_Object = MibTableColumn
zxAnEponOnuVoiceIpMngIpRelation = _ZxAnEponOnuVoiceIpMngIpRelation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 2),
    _ZxAnEponOnuVoiceIpMngIpRelation_Type()
)
zxAnEponOnuVoiceIpMngIpRelation.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoiceIpMngIpRelation.setStatus("current")


class _ZxAnEponOnuVoiceIpMode_Type(Integer32):
    """Custom type zxAnEponOnuVoiceIpMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("static", 1),
          ("dhcp", 2),
          ("pppoe", 3))
    )


_ZxAnEponOnuVoiceIpMode_Type.__name__ = "Integer32"
_ZxAnEponOnuVoiceIpMode_Object = MibTableColumn
zxAnEponOnuVoiceIpMode = _ZxAnEponOnuVoiceIpMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 3),
    _ZxAnEponOnuVoiceIpMode_Type()
)
zxAnEponOnuVoiceIpMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoiceIpMode.setStatus("current")
_ZxAnEponOnuVoiceIpAddress_Type = IpAddress
_ZxAnEponOnuVoiceIpAddress_Object = MibTableColumn
zxAnEponOnuVoiceIpAddress = _ZxAnEponOnuVoiceIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 4),
    _ZxAnEponOnuVoiceIpAddress_Type()
)
zxAnEponOnuVoiceIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoiceIpAddress.setStatus("current")
_ZxAnEponOnuVoiceDnsServer_Type = IpAddress
_ZxAnEponOnuVoiceDnsServer_Object = MibTableColumn
zxAnEponOnuVoiceDnsServer = _ZxAnEponOnuVoiceDnsServer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 5),
    _ZxAnEponOnuVoiceDnsServer_Type()
)
zxAnEponOnuVoiceDnsServer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoiceDnsServer.setStatus("current")
_ZxAnEponOnuVoiceIpMask_Type = IpAddress
_ZxAnEponOnuVoiceIpMask_Object = MibTableColumn
zxAnEponOnuVoiceIpMask = _ZxAnEponOnuVoiceIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 6),
    _ZxAnEponOnuVoiceIpMask_Type()
)
zxAnEponOnuVoiceIpMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoiceIpMask.setStatus("current")
_ZxAnEponOnuVoiceGateway_Type = IpAddress
_ZxAnEponOnuVoiceGateway_Object = MibTableColumn
zxAnEponOnuVoiceGateway = _ZxAnEponOnuVoiceGateway_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 7),
    _ZxAnEponOnuVoiceGateway_Type()
)
zxAnEponOnuVoiceGateway.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoiceGateway.setStatus("current")


class _ZxAnEponOnuVoicePPPoEMode_Type(Integer32):
    """Custom type zxAnEponOnuVoicePPPoEMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto", 1),
          ("chap", 2),
          ("pap", 3))
    )


_ZxAnEponOnuVoicePPPoEMode_Type.__name__ = "Integer32"
_ZxAnEponOnuVoicePPPoEMode_Object = MibTableColumn
zxAnEponOnuVoicePPPoEMode = _ZxAnEponOnuVoicePPPoEMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 8),
    _ZxAnEponOnuVoicePPPoEMode_Type()
)
zxAnEponOnuVoicePPPoEMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoicePPPoEMode.setStatus("current")
_ZxAnEponOnuVoicePPPoEUserName_Type = DisplayString
_ZxAnEponOnuVoicePPPoEUserName_Object = MibTableColumn
zxAnEponOnuVoicePPPoEUserName = _ZxAnEponOnuVoicePPPoEUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 9),
    _ZxAnEponOnuVoicePPPoEUserName_Type()
)
zxAnEponOnuVoicePPPoEUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoicePPPoEUserName.setStatus("current")
_ZxAnEponOnuVoicePPPoEPassword_Type = DisplayString
_ZxAnEponOnuVoicePPPoEPassword_Object = MibTableColumn
zxAnEponOnuVoicePPPoEPassword = _ZxAnEponOnuVoicePPPoEPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 10),
    _ZxAnEponOnuVoicePPPoEPassword_Type()
)
zxAnEponOnuVoicePPPoEPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoicePPPoEPassword.setStatus("current")


class _ZxAnEponOnuVoiceTaggedFlag_Type(Integer32):
    """Custom type zxAnEponOnuVoiceTaggedFlag based on Integer32"""
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


_ZxAnEponOnuVoiceTaggedFlag_Type.__name__ = "Integer32"
_ZxAnEponOnuVoiceTaggedFlag_Object = MibTableColumn
zxAnEponOnuVoiceTaggedFlag = _ZxAnEponOnuVoiceTaggedFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 11),
    _ZxAnEponOnuVoiceTaggedFlag_Type()
)
zxAnEponOnuVoiceTaggedFlag.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoiceTaggedFlag.setStatus("current")
_ZxAnEponOnuVoiceDataVlan_Type = Integer32
_ZxAnEponOnuVoiceDataVlan_Object = MibTableColumn
zxAnEponOnuVoiceDataVlan = _ZxAnEponOnuVoiceDataVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 12),
    _ZxAnEponOnuVoiceDataVlan_Type()
)
zxAnEponOnuVoiceDataVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoiceDataVlan.setStatus("current")


class _ZxAnEponOnuVoiceDataPriority_Type(Integer32):
    """Custom type zxAnEponOnuVoiceDataPriority based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("pri0", 1),
          ("pri1", 2),
          ("pri2", 3),
          ("pri3", 4),
          ("pri4", 5),
          ("pri5", 6),
          ("pri6", 7),
          ("pri7", 8))
    )


_ZxAnEponOnuVoiceDataPriority_Type.__name__ = "Integer32"
_ZxAnEponOnuVoiceDataPriority_Object = MibTableColumn
zxAnEponOnuVoiceDataPriority = _ZxAnEponOnuVoiceDataPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 13),
    _ZxAnEponOnuVoiceDataPriority_Type()
)
zxAnEponOnuVoiceDataPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoiceDataPriority.setStatus("current")
_ZxAnEponOnuVoiceDhcpLeaseTime_Type = Integer32
_ZxAnEponOnuVoiceDhcpLeaseTime_Object = MibTableColumn
zxAnEponOnuVoiceDhcpLeaseTime = _ZxAnEponOnuVoiceDhcpLeaseTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 14),
    _ZxAnEponOnuVoiceDhcpLeaseTime_Type()
)
zxAnEponOnuVoiceDhcpLeaseTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVoiceDhcpLeaseTime.setStatus("current")


class _ZxAnEponOnuVoicePPPoEStatus_Type(Integer32):
    """Custom type zxAnEponOnuVoicePPPoEStatus based on Integer32"""
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
        *(("dhcping", 1),
          ("dhcpfinish", 2),
          ("pppoeing", 3),
          ("pppoefinish", 4))
    )


_ZxAnEponOnuVoicePPPoEStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuVoicePPPoEStatus_Object = MibTableColumn
zxAnEponOnuVoicePPPoEStatus = _ZxAnEponOnuVoicePPPoEStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 28, 1, 15),
    _ZxAnEponOnuVoicePPPoEStatus_Type()
)
zxAnEponOnuVoicePPPoEStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVoicePPPoEStatus.setStatus("current")
_Epon0pticalTransceiverDiagnosisTable_Object = MibTable
epon0pticalTransceiverDiagnosisTable = _Epon0pticalTransceiverDiagnosisTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 29)
)
if mibBuilder.loadTexts:
    epon0pticalTransceiverDiagnosisTable.setStatus("current")
_Epon0pticalTransceiverDiagnosisEntry_Object = MibTableRow
epon0pticalTransceiverDiagnosisEntry = _Epon0pticalTransceiverDiagnosisEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 29, 1)
)
epon0pticalTransceiverDiagnosisEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    epon0pticalTransceiverDiagnosisEntry.setStatus("current")
_ZxAnEponOnuTransTemperature_Type = DisplayString
_ZxAnEponOnuTransTemperature_Object = MibTableColumn
zxAnEponOnuTransTemperature = _ZxAnEponOnuTransTemperature_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 29, 1, 1),
    _ZxAnEponOnuTransTemperature_Type()
)
zxAnEponOnuTransTemperature.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTransTemperature.setStatus("current")
_ZxAnEponOnuSupplyVoltage_Type = DisplayString
_ZxAnEponOnuSupplyVoltage_Object = MibTableColumn
zxAnEponOnuSupplyVoltage = _ZxAnEponOnuSupplyVoltage_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 29, 1, 2),
    _ZxAnEponOnuSupplyVoltage_Type()
)
zxAnEponOnuSupplyVoltage.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuSupplyVoltage.setStatus("current")
_ZxAnEponOnuTxBiasCurrent_Type = DisplayString
_ZxAnEponOnuTxBiasCurrent_Object = MibTableColumn
zxAnEponOnuTxBiasCurrent = _ZxAnEponOnuTxBiasCurrent_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 29, 1, 3),
    _ZxAnEponOnuTxBiasCurrent_Type()
)
zxAnEponOnuTxBiasCurrent.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTxBiasCurrent.setStatus("current")
_ZxAnEponOnuTxPower_Type = DisplayString
_ZxAnEponOnuTxPower_Object = MibTableColumn
zxAnEponOnuTxPower = _ZxAnEponOnuTxPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 29, 1, 4),
    _ZxAnEponOnuTxPower_Type()
)
zxAnEponOnuTxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTxPower.setStatus("current")
_ZxAnEponOnuRxPower_Type = DisplayString
_ZxAnEponOnuRxPower_Object = MibTableColumn
zxAnEponOnuRxPower = _ZxAnEponOnuRxPower_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 29, 1, 5),
    _ZxAnEponOnuRxPower_Type()
)
zxAnEponOnuRxPower.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuRxPower.setStatus("current")
_EponRmOnuTransAlarmCfgTable_Object = MibTable
eponRmOnuTransAlarmCfgTable = _EponRmOnuTransAlarmCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 30)
)
if mibBuilder.loadTexts:
    eponRmOnuTransAlarmCfgTable.setStatus("current")
_EponRmOnuTransAlarmCfgTableEntry_Object = MibTableRow
eponRmOnuTransAlarmCfgTableEntry = _EponRmOnuTransAlarmCfgTableEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 30, 1)
)
eponRmOnuTransAlarmCfgTableEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    eponRmOnuTransAlarmCfgTableEntry.setStatus("current")


class _ZxAnEponOnuTrans_Type(Integer32):
    """Custom type zxAnEponOnuTrans based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuTrans_Type.__name__ = "Integer32"
_ZxAnEponOnuTrans_Object = MibTableColumn
zxAnEponOnuTrans = _ZxAnEponOnuTrans_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 30, 1, 1),
    _ZxAnEponOnuTrans_Type()
)
zxAnEponOnuTrans.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTrans.setStatus("current")
_EponRmOnuTransAlarmThresholdTable_Object = MibTable
eponRmOnuTransAlarmThresholdTable = _EponRmOnuTransAlarmThresholdTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31)
)
if mibBuilder.loadTexts:
    eponRmOnuTransAlarmThresholdTable.setStatus("current")
_EponRmOnuTransAlarmThresholdEntry_Object = MibTableRow
eponRmOnuTransAlarmThresholdEntry = _EponRmOnuTransAlarmThresholdEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1)
)
eponRmOnuTransAlarmThresholdEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    eponRmOnuTransAlarmThresholdEntry.setStatus("current")
_ZxAnEponOnuTempHighAlarm_Type = DisplayString
_ZxAnEponOnuTempHighAlarm_Object = MibTableColumn
zxAnEponOnuTempHighAlarm = _ZxAnEponOnuTempHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 1),
    _ZxAnEponOnuTempHighAlarm_Type()
)
zxAnEponOnuTempHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTempHighAlarm.setStatus("current")
_ZxAnEponOnuTempLowAlarm_Type = DisplayString
_ZxAnEponOnuTempLowAlarm_Object = MibTableColumn
zxAnEponOnuTempLowAlarm = _ZxAnEponOnuTempLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 2),
    _ZxAnEponOnuTempLowAlarm_Type()
)
zxAnEponOnuTempLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTempLowAlarm.setStatus("current")
_ZxAnEponOnuTempHighWarning_Type = DisplayString
_ZxAnEponOnuTempHighWarning_Object = MibTableColumn
zxAnEponOnuTempHighWarning = _ZxAnEponOnuTempHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 3),
    _ZxAnEponOnuTempHighWarning_Type()
)
zxAnEponOnuTempHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTempHighWarning.setStatus("current")
_ZxAnEponOnuTempLowwarning_Type = DisplayString
_ZxAnEponOnuTempLowwarning_Object = MibTableColumn
zxAnEponOnuTempLowwarning = _ZxAnEponOnuTempLowwarning_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 4),
    _ZxAnEponOnuTempLowwarning_Type()
)
zxAnEponOnuTempLowwarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTempLowwarning.setStatus("current")
_ZxAnEponOnuVoltageHighAlarm_Type = DisplayString
_ZxAnEponOnuVoltageHighAlarm_Object = MibTableColumn
zxAnEponOnuVoltageHighAlarm = _ZxAnEponOnuVoltageHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 5),
    _ZxAnEponOnuVoltageHighAlarm_Type()
)
zxAnEponOnuVoltageHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoltageHighAlarm.setStatus("current")
_ZxAnEponOnuVoltageLowAlarm_Type = DisplayString
_ZxAnEponOnuVoltageLowAlarm_Object = MibTableColumn
zxAnEponOnuVoltageLowAlarm = _ZxAnEponOnuVoltageLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 6),
    _ZxAnEponOnuVoltageLowAlarm_Type()
)
zxAnEponOnuVoltageLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoltageLowAlarm.setStatus("current")
_ZxAnEponOnuVoltageHighWarning_Type = DisplayString
_ZxAnEponOnuVoltageHighWarning_Object = MibTableColumn
zxAnEponOnuVoltageHighWarning = _ZxAnEponOnuVoltageHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 7),
    _ZxAnEponOnuVoltageHighWarning_Type()
)
zxAnEponOnuVoltageHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoltageHighWarning.setStatus("current")
_ZxAnEponOnuVoltageLowWarning_Type = DisplayString
_ZxAnEponOnuVoltageLowWarning_Object = MibTableColumn
zxAnEponOnuVoltageLowWarning = _ZxAnEponOnuVoltageLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 8),
    _ZxAnEponOnuVoltageLowWarning_Type()
)
zxAnEponOnuVoltageLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoltageLowWarning.setStatus("current")
_ZxAnEponOnuBiasHighAlarm_Type = DisplayString
_ZxAnEponOnuBiasHighAlarm_Object = MibTableColumn
zxAnEponOnuBiasHighAlarm = _ZxAnEponOnuBiasHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 9),
    _ZxAnEponOnuBiasHighAlarm_Type()
)
zxAnEponOnuBiasHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuBiasHighAlarm.setStatus("current")
_ZxAnEponOnuBiasLowAlarm_Type = DisplayString
_ZxAnEponOnuBiasLowAlarm_Object = MibTableColumn
zxAnEponOnuBiasLowAlarm = _ZxAnEponOnuBiasLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 10),
    _ZxAnEponOnuBiasLowAlarm_Type()
)
zxAnEponOnuBiasLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuBiasLowAlarm.setStatus("current")
_ZxAnEponOnuBiasHighWarning_Type = DisplayString
_ZxAnEponOnuBiasHighWarning_Object = MibTableColumn
zxAnEponOnuBiasHighWarning = _ZxAnEponOnuBiasHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 11),
    _ZxAnEponOnuBiasHighWarning_Type()
)
zxAnEponOnuBiasHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuBiasHighWarning.setStatus("current")
_ZxAnEponOnuBiasLowWarning_Type = DisplayString
_ZxAnEponOnuBiasLowWarning_Object = MibTableColumn
zxAnEponOnuBiasLowWarning = _ZxAnEponOnuBiasLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 12),
    _ZxAnEponOnuBiasLowWarning_Type()
)
zxAnEponOnuBiasLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuBiasLowWarning.setStatus("current")
_ZxAnEponOnuTxPowerHighAlarm_Type = DisplayString
_ZxAnEponOnuTxPowerHighAlarm_Object = MibTableColumn
zxAnEponOnuTxPowerHighAlarm = _ZxAnEponOnuTxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 13),
    _ZxAnEponOnuTxPowerHighAlarm_Type()
)
zxAnEponOnuTxPowerHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTxPowerHighAlarm.setStatus("current")
_ZxAnEponOnuTxPowerLowAlarm_Type = DisplayString
_ZxAnEponOnuTxPowerLowAlarm_Object = MibTableColumn
zxAnEponOnuTxPowerLowAlarm = _ZxAnEponOnuTxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 14),
    _ZxAnEponOnuTxPowerLowAlarm_Type()
)
zxAnEponOnuTxPowerLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTxPowerLowAlarm.setStatus("current")
_ZxAnEponOnuTxPowerHighWarning_Type = DisplayString
_ZxAnEponOnuTxPowerHighWarning_Object = MibTableColumn
zxAnEponOnuTxPowerHighWarning = _ZxAnEponOnuTxPowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 15),
    _ZxAnEponOnuTxPowerHighWarning_Type()
)
zxAnEponOnuTxPowerHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTxPowerHighWarning.setStatus("current")
_ZxAnEponOnuTxPowerLowWarning_Type = DisplayString
_ZxAnEponOnuTxPowerLowWarning_Object = MibTableColumn
zxAnEponOnuTxPowerLowWarning = _ZxAnEponOnuTxPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 16),
    _ZxAnEponOnuTxPowerLowWarning_Type()
)
zxAnEponOnuTxPowerLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTxPowerLowWarning.setStatus("current")
_ZxAnEponOnuRxPowerHighAlarm_Type = DisplayString
_ZxAnEponOnuRxPowerHighAlarm_Object = MibTableColumn
zxAnEponOnuRxPowerHighAlarm = _ZxAnEponOnuRxPowerHighAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 17),
    _ZxAnEponOnuRxPowerHighAlarm_Type()
)
zxAnEponOnuRxPowerHighAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuRxPowerHighAlarm.setStatus("current")
_ZxAnEponOnuRxPowerLowAlarm_Type = DisplayString
_ZxAnEponOnuRxPowerLowAlarm_Object = MibTableColumn
zxAnEponOnuRxPowerLowAlarm = _ZxAnEponOnuRxPowerLowAlarm_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 18),
    _ZxAnEponOnuRxPowerLowAlarm_Type()
)
zxAnEponOnuRxPowerLowAlarm.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuRxPowerLowAlarm.setStatus("current")
_ZxAnEponOnuRxPowerHighWarning_Type = DisplayString
_ZxAnEponOnuRxPowerHighWarning_Object = MibTableColumn
zxAnEponOnuRxPowerHighWarning = _ZxAnEponOnuRxPowerHighWarning_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 19),
    _ZxAnEponOnuRxPowerHighWarning_Type()
)
zxAnEponOnuRxPowerHighWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuRxPowerHighWarning.setStatus("current")
_ZxAnEponOnuRxPowerLowWarning_Type = DisplayString
_ZxAnEponOnuRxPowerLowWarning_Object = MibTableColumn
zxAnEponOnuRxPowerLowWarning = _ZxAnEponOnuRxPowerLowWarning_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 31, 1, 20),
    _ZxAnEponOnuRxPowerLowWarning_Type()
)
zxAnEponOnuRxPowerLowWarning.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuRxPowerLowWarning.setStatus("current")
_ZxEponUniProfileAdmin_ObjectIdentity = ObjectIdentity
zxEponUniProfileAdmin = _ZxEponUniProfileAdmin_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32)
)
_ZxEponUniProfileTable_Object = MibTable
zxEponUniProfileTable = _ZxEponUniProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1)
)
if mibBuilder.loadTexts:
    zxEponUniProfileTable.setStatus("current")
_ZxEponUniProfileEntry_Object = MibTableRow
zxEponUniProfileEntry = _ZxEponUniProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1, 1)
)
zxEponUniProfileEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "uniProfileIndex"),
)
if mibBuilder.loadTexts:
    zxEponUniProfileEntry.setStatus("current")
_UniProfileIndex_Type = Integer32
_UniProfileIndex_Object = MibTableColumn
uniProfileIndex = _UniProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1, 1, 1),
    _UniProfileIndex_Type()
)
uniProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    uniProfileIndex.setStatus("current")


class _UniProfileName_Type(DisplayString):
    """Custom type uniProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 31),
    )


_UniProfileName_Type.__name__ = "DisplayString"
_UniProfileName_Object = MibTableColumn
uniProfileName = _UniProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1, 1, 2),
    _UniProfileName_Type()
)
uniProfileName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniProfileName.setStatus("current")


class _UniProfileUpCir_Type(Integer32):
    """Custom type uniProfileUpCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_UniProfileUpCir_Type.__name__ = "Integer32"
_UniProfileUpCir_Object = MibTableColumn
uniProfileUpCir = _UniProfileUpCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1, 1, 3),
    _UniProfileUpCir_Type()
)
uniProfileUpCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniProfileUpCir.setStatus("current")


class _UniProfileUpCbs_Type(Integer32):
    """Custom type uniProfileUpCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 16777215),
    )


_UniProfileUpCbs_Type.__name__ = "Integer32"
_UniProfileUpCbs_Object = MibTableColumn
uniProfileUpCbs = _UniProfileUpCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1, 1, 4),
    _UniProfileUpCbs_Type()
)
uniProfileUpCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniProfileUpCbs.setStatus("current")


class _UniProfileUpEbs_Type(Integer32):
    """Custom type uniProfileUpEbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1522),
    )


_UniProfileUpEbs_Type.__name__ = "Integer32"
_UniProfileUpEbs_Object = MibTableColumn
uniProfileUpEbs = _UniProfileUpEbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1, 1, 5),
    _UniProfileUpEbs_Type()
)
uniProfileUpEbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniProfileUpEbs.setStatus("current")


class _UniProfileDownCir_Type(Integer32):
    """Custom type uniProfileDownCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_UniProfileDownCir_Type.__name__ = "Integer32"
_UniProfileDownCir_Object = MibTableColumn
uniProfileDownCir = _UniProfileDownCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1, 1, 6),
    _UniProfileDownCir_Type()
)
uniProfileDownCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniProfileDownCir.setStatus("current")


class _UniProfileDownCbs_Type(Integer32):
    """Custom type uniProfileDownCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 16777215),
    )


_UniProfileDownCbs_Type.__name__ = "Integer32"
_UniProfileDownCbs_Object = MibTableColumn
uniProfileDownCbs = _UniProfileDownCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1, 1, 7),
    _UniProfileDownCbs_Type()
)
uniProfileDownCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniProfileDownCbs.setStatus("current")


class _UniProfileDownEbs_Type(Integer32):
    """Custom type uniProfileDownEbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1522),
    )


_UniProfileDownEbs_Type.__name__ = "Integer32"
_UniProfileDownEbs_Object = MibTableColumn
uniProfileDownEbs = _UniProfileDownEbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1, 1, 8),
    _UniProfileDownEbs_Type()
)
uniProfileDownEbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniProfileDownEbs.setStatus("current")
_UniProfileRowStatus_Type = RowStatus
_UniProfileRowStatus_Object = MibTableColumn
uniProfileRowStatus = _UniProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 1, 1, 9),
    _UniProfileRowStatus_Type()
)
uniProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    uniProfileRowStatus.setStatus("current")
_UniProfileNextIndex_Type = Integer32
_UniProfileNextIndex_Object = MibScalar
uniProfileNextIndex = _UniProfileNextIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 32, 2),
    _UniProfileNextIndex_Type()
)
uniProfileNextIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    uniProfileNextIndex.setStatus("current")
_ZxEponUniLimitCfgTable_Object = MibTable
zxEponUniLimitCfgTable = _ZxEponUniLimitCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 34)
)
if mibBuilder.loadTexts:
    zxEponUniLimitCfgTable.setStatus("current")
_ZxEponUniLimitCfgEntry_Object = MibTableRow
zxEponUniLimitCfgEntry = _ZxEponUniLimitCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 34, 1)
)
zxEponUniLimitCfgEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxEponUniLimitCfgEntry.setStatus("current")


class _UniCfgLimitProfileIndex_Type(Integer32):
    """Custom type uniCfgLimitProfileIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 256),
    )


_UniCfgLimitProfileIndex_Type.__name__ = "Integer32"
_UniCfgLimitProfileIndex_Object = MibTableColumn
uniCfgLimitProfileIndex = _UniCfgLimitProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 34, 1, 1),
    _UniCfgLimitProfileIndex_Type()
)
uniCfgLimitProfileIndex.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    uniCfgLimitProfileIndex.setStatus("current")
_ZxAnEponRmVoipProfileMgmt_ObjectIdentity = ObjectIdentity
zxAnEponRmVoipProfileMgmt = _ZxAnEponRmVoipProfileMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35)
)
_ZxAnEponRmVoipIpProfileIdxNext_Type = Integer32
_ZxAnEponRmVoipIpProfileIdxNext_Object = MibScalar
zxAnEponRmVoipIpProfileIdxNext = _ZxAnEponRmVoipIpProfileIdxNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 1),
    _ZxAnEponRmVoipIpProfileIdxNext_Type()
)
zxAnEponRmVoipIpProfileIdxNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpProfileIdxNext.setStatus("current")
_ZxAnEponRmVoipIpProfileTable_Object = MibTable
zxAnEponRmVoipIpProfileTable = _ZxAnEponRmVoipIpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 2)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpProfileTable.setStatus("current")
_ZxAnEponRmVoipIpProfileEntry_Object = MibTableRow
zxAnEponRmVoipIpProfileEntry = _ZxAnEponRmVoipIpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 2, 1)
)
zxAnEponRmVoipIpProfileEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmVoipIpProfileIdx"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpProfileEntry.setStatus("current")
_ZxAnEponRmVoipIpProfileIdx_Type = Integer32
_ZxAnEponRmVoipIpProfileIdx_Object = MibTableColumn
zxAnEponRmVoipIpProfileIdx = _ZxAnEponRmVoipIpProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 2, 1, 1),
    _ZxAnEponRmVoipIpProfileIdx_Type()
)
zxAnEponRmVoipIpProfileIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpProfileIdx.setStatus("current")


class _ZxAnEponRmVoipIpProfileName_Type(DisplayString):
    """Custom type zxAnEponRmVoipIpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmVoipIpProfileName_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipIpProfileName_Object = MibTableColumn
zxAnEponRmVoipIpProfileName = _ZxAnEponRmVoipIpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 2, 1, 2),
    _ZxAnEponRmVoipIpProfileName_Type()
)
zxAnEponRmVoipIpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpProfileName.setStatus("current")


class _ZxAnEponRmVoipIpMngIpRelation_Type(Integer32):
    """Custom type zxAnEponRmVoipIpMngIpRelation based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("independent", 1),
          ("shared", 2))
    )


_ZxAnEponRmVoipIpMngIpRelation_Type.__name__ = "Integer32"
_ZxAnEponRmVoipIpMngIpRelation_Object = MibTableColumn
zxAnEponRmVoipIpMngIpRelation = _ZxAnEponRmVoipIpMngIpRelation_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 2, 1, 3),
    _ZxAnEponRmVoipIpMngIpRelation_Type()
)
zxAnEponRmVoipIpMngIpRelation.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpMngIpRelation.setStatus("current")


class _ZxAnEponRmVoipIpMode_Type(Integer32):
    """Custom type zxAnEponRmVoipIpMode based on Integer32"""
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
        *(("static", 1),
          ("dhcp", 2),
          ("pppoe", 3))
    )


_ZxAnEponRmVoipIpMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipIpMode_Object = MibTableColumn
zxAnEponRmVoipIpMode = _ZxAnEponRmVoipIpMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 2, 1, 4),
    _ZxAnEponRmVoipIpMode_Type()
)
zxAnEponRmVoipIpMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpMode.setStatus("current")
_ZxAnEponRmVoipIpDefaultGateWay_Type = IpAddress
_ZxAnEponRmVoipIpDefaultGateWay_Object = MibTableColumn
zxAnEponRmVoipIpDefaultGateWay = _ZxAnEponRmVoipIpDefaultGateWay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 2, 1, 5),
    _ZxAnEponRmVoipIpDefaultGateWay_Type()
)
zxAnEponRmVoipIpDefaultGateWay.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpDefaultGateWay.setStatus("current")
_ZxAnEponRmVoipIpPrimaryDNSServerIp_Type = IpAddress
_ZxAnEponRmVoipIpPrimaryDNSServerIp_Object = MibTableColumn
zxAnEponRmVoipIpPrimaryDNSServerIp = _ZxAnEponRmVoipIpPrimaryDNSServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 2, 1, 6),
    _ZxAnEponRmVoipIpPrimaryDNSServerIp_Type()
)
zxAnEponRmVoipIpPrimaryDNSServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpPrimaryDNSServerIp.setStatus("current")


class _ZxAnEponRmVoipIpPPPoEMode_Type(Integer32):
    """Custom type zxAnEponRmVoipIpPPPoEMode based on Integer32"""
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
        *(("auto", 1),
          ("chap", 2),
          ("pap", 3))
    )


_ZxAnEponRmVoipIpPPPoEMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipIpPPPoEMode_Object = MibTableColumn
zxAnEponRmVoipIpPPPoEMode = _ZxAnEponRmVoipIpPPPoEMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 2, 1, 7),
    _ZxAnEponRmVoipIpPPPoEMode_Type()
)
zxAnEponRmVoipIpPPPoEMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpPPPoEMode.setStatus("current")
_ZxAnEponRmVoipIpRowStatus_Type = RowStatus
_ZxAnEponRmVoipIpRowStatus_Object = MibTableColumn
zxAnEponRmVoipIpRowStatus = _ZxAnEponRmVoipIpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 2, 1, 30),
    _ZxAnEponRmVoipIpRowStatus_Type()
)
zxAnEponRmVoipIpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpRowStatus.setStatus("current")
_ZxAnEponRmVoipVlanProfileIdxNext_Type = Integer32
_ZxAnEponRmVoipVlanProfileIdxNext_Object = MibScalar
zxAnEponRmVoipVlanProfileIdxNext = _ZxAnEponRmVoipVlanProfileIdxNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 3),
    _ZxAnEponRmVoipVlanProfileIdxNext_Type()
)
zxAnEponRmVoipVlanProfileIdxNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipVlanProfileIdxNext.setStatus("current")
_ZxAnEponRmVoipVlanProfileTable_Object = MibTable
zxAnEponRmVoipVlanProfileTable = _ZxAnEponRmVoipVlanProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 4)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipVlanProfileTable.setStatus("current")
_ZxAnEponRmVoipVlanProfileEntry_Object = MibTableRow
zxAnEponRmVoipVlanProfileEntry = _ZxAnEponRmVoipVlanProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 4, 1)
)
zxAnEponRmVoipVlanProfileEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmVoipVlanProfileIdx"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipVlanProfileEntry.setStatus("current")
_ZxAnEponRmVoipVlanProfileIdx_Type = Integer32
_ZxAnEponRmVoipVlanProfileIdx_Object = MibTableColumn
zxAnEponRmVoipVlanProfileIdx = _ZxAnEponRmVoipVlanProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 4, 1, 1),
    _ZxAnEponRmVoipVlanProfileIdx_Type()
)
zxAnEponRmVoipVlanProfileIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmVoipVlanProfileIdx.setStatus("current")


class _ZxAnEponRmVoipVlanProfileName_Type(DisplayString):
    """Custom type zxAnEponRmVoipVlanProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmVoipVlanProfileName_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipVlanProfileName_Object = MibTableColumn
zxAnEponRmVoipVlanProfileName = _ZxAnEponRmVoipVlanProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 4, 1, 2),
    _ZxAnEponRmVoipVlanProfileName_Type()
)
zxAnEponRmVoipVlanProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipVlanProfileName.setStatus("current")


class _ZxAnEponRmVoipVlanTagMode_Type(Integer32):
    """Custom type zxAnEponRmVoipVlanTagMode based on Integer32"""
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
        *(("transparent", 1),
          ("tag", 2),
          ("vlanStacking", 3))
    )


_ZxAnEponRmVoipVlanTagMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipVlanTagMode_Object = MibTableColumn
zxAnEponRmVoipVlanTagMode = _ZxAnEponRmVoipVlanTagMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 4, 1, 3),
    _ZxAnEponRmVoipVlanTagMode_Type()
)
zxAnEponRmVoipVlanTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipVlanTagMode.setStatus("current")


class _ZxAnEponRmVoipVlanTagCVlan_Type(Integer32):
    """Custom type zxAnEponRmVoipVlanTagCVlan based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponRmVoipVlanTagCVlan_Type.__name__ = "Integer32"
_ZxAnEponRmVoipVlanTagCVlan_Object = MibTableColumn
zxAnEponRmVoipVlanTagCVlan = _ZxAnEponRmVoipVlanTagCVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 4, 1, 4),
    _ZxAnEponRmVoipVlanTagCVlan_Type()
)
zxAnEponRmVoipVlanTagCVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipVlanTagCVlan.setStatus("current")


class _ZxAnEponRmVoipVlanTagPriority_Type(Integer32):
    """Custom type zxAnEponRmVoipVlanTagPriority based on Integer32"""
    defaultValue = 7

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnEponRmVoipVlanTagPriority_Type.__name__ = "Integer32"
_ZxAnEponRmVoipVlanTagPriority_Object = MibTableColumn
zxAnEponRmVoipVlanTagPriority = _ZxAnEponRmVoipVlanTagPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 4, 1, 5),
    _ZxAnEponRmVoipVlanTagPriority_Type()
)
zxAnEponRmVoipVlanTagPriority.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipVlanTagPriority.setStatus("current")


class _ZxAnEponRmVoipVlanTagSVlan_Type(Integer32):
    """Custom type zxAnEponRmVoipVlanTagSVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponRmVoipVlanTagSVlan_Type.__name__ = "Integer32"
_ZxAnEponRmVoipVlanTagSVlan_Object = MibTableColumn
zxAnEponRmVoipVlanTagSVlan = _ZxAnEponRmVoipVlanTagSVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 4, 1, 6),
    _ZxAnEponRmVoipVlanTagSVlan_Type()
)
zxAnEponRmVoipVlanTagSVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipVlanTagSVlan.setStatus("current")
_ZxAnEponRmVoipVlanRowStatus_Type = RowStatus
_ZxAnEponRmVoipVlanRowStatus_Object = MibTableColumn
zxAnEponRmVoipVlanRowStatus = _ZxAnEponRmVoipVlanRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 4, 1, 30),
    _ZxAnEponRmVoipVlanRowStatus_Type()
)
zxAnEponRmVoipVlanRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipVlanRowStatus.setStatus("current")
_ZxAnEponRmVoipH248ProfileIdxNext_Type = Integer32
_ZxAnEponRmVoipH248ProfileIdxNext_Object = MibScalar
zxAnEponRmVoipH248ProfileIdxNext = _ZxAnEponRmVoipH248ProfileIdxNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 5),
    _ZxAnEponRmVoipH248ProfileIdxNext_Type()
)
zxAnEponRmVoipH248ProfileIdxNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248ProfileIdxNext.setStatus("current")
_ZxAnEponRmVoipH248ProfileTable_Object = MibTable
zxAnEponRmVoipH248ProfileTable = _ZxAnEponRmVoipH248ProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248ProfileTable.setStatus("current")
_ZxAnEponRmVoipH248ProfileEntry_Object = MibTableRow
zxAnEponRmVoipH248ProfileEntry = _ZxAnEponRmVoipH248ProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1)
)
zxAnEponRmVoipH248ProfileEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmVoipH248ProfileIdx"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248ProfileEntry.setStatus("current")
_ZxAnEponRmVoipH248ProfileIdx_Type = Integer32
_ZxAnEponRmVoipH248ProfileIdx_Object = MibTableColumn
zxAnEponRmVoipH248ProfileIdx = _ZxAnEponRmVoipH248ProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 1),
    _ZxAnEponRmVoipH248ProfileIdx_Type()
)
zxAnEponRmVoipH248ProfileIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248ProfileIdx.setStatus("current")


class _ZxAnEponRmVoipH248ProfileName_Type(DisplayString):
    """Custom type zxAnEponRmVoipH248ProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmVoipH248ProfileName_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipH248ProfileName_Object = MibTableColumn
zxAnEponRmVoipH248ProfileName = _ZxAnEponRmVoipH248ProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 2),
    _ZxAnEponRmVoipH248ProfileName_Type()
)
zxAnEponRmVoipH248ProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248ProfileName.setStatus("current")
_ZxAnEponRmVoipH248RegServerIp_Type = IpAddress
_ZxAnEponRmVoipH248RegServerIp_Object = MibTableColumn
zxAnEponRmVoipH248RegServerIp = _ZxAnEponRmVoipH248RegServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 3),
    _ZxAnEponRmVoipH248RegServerIp_Type()
)
zxAnEponRmVoipH248RegServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248RegServerIp.setStatus("current")


class _ZxAnEponRmVoipH248RegServerPort_Type(Integer32):
    """Custom type zxAnEponRmVoipH248RegServerPort based on Integer32"""
    defaultValue = 2944

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipH248RegServerPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248RegServerPort_Object = MibTableColumn
zxAnEponRmVoipH248RegServerPort = _ZxAnEponRmVoipH248RegServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 4),
    _ZxAnEponRmVoipH248RegServerPort_Type()
)
zxAnEponRmVoipH248RegServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248RegServerPort.setStatus("current")
_ZxAnEponRmVoipH248BackRegServerIp_Type = IpAddress
_ZxAnEponRmVoipH248BackRegServerIp_Object = MibTableColumn
zxAnEponRmVoipH248BackRegServerIp = _ZxAnEponRmVoipH248BackRegServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 5),
    _ZxAnEponRmVoipH248BackRegServerIp_Type()
)
zxAnEponRmVoipH248BackRegServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248BackRegServerIp.setStatus("current")


class _ZxAnEponRmVoipH248BackRegServerPort_Type(Integer32):
    """Custom type zxAnEponRmVoipH248BackRegServerPort based on Integer32"""
    defaultValue = 2944

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipH248BackRegServerPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248BackRegServerPort_Object = MibTableColumn
zxAnEponRmVoipH248BackRegServerPort = _ZxAnEponRmVoipH248BackRegServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 6),
    _ZxAnEponRmVoipH248BackRegServerPort_Type()
)
zxAnEponRmVoipH248BackRegServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248BackRegServerPort.setStatus("current")


class _ZxAnEponRmVoipH248RtpLinkKeptFlag_Type(Integer32):
    """Custom type zxAnEponRmVoipH248RtpLinkKeptFlag based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ZxAnEponRmVoipH248RtpLinkKeptFlag_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248RtpLinkKeptFlag_Object = MibTableColumn
zxAnEponRmVoipH248RtpLinkKeptFlag = _ZxAnEponRmVoipH248RtpLinkKeptFlag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 7),
    _ZxAnEponRmVoipH248RtpLinkKeptFlag_Type()
)
zxAnEponRmVoipH248RtpLinkKeptFlag.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248RtpLinkKeptFlag.setStatus("current")


class _ZxAnEponRmVoipH248OnuHeartbeatMode_Type(Integer32):
    """Custom type zxAnEponRmVoipH248OnuHeartbeatMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("h248ServiceChange", 2),
          ("h248Ctc", 3))
    )


_ZxAnEponRmVoipH248OnuHeartbeatMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248OnuHeartbeatMode_Object = MibTableColumn
zxAnEponRmVoipH248OnuHeartbeatMode = _ZxAnEponRmVoipH248OnuHeartbeatMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 8),
    _ZxAnEponRmVoipH248OnuHeartbeatMode_Type()
)
zxAnEponRmVoipH248OnuHeartbeatMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248OnuHeartbeatMode.setStatus("current")


class _ZxAnEponRmVoipH248OnuHeartbeatCycle_Type(Integer32):
    """Custom type zxAnEponRmVoipH248OnuHeartbeatCycle based on Integer32"""
    defaultValue = 60

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(10, 65535),
    )


_ZxAnEponRmVoipH248OnuHeartbeatCycle_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248OnuHeartbeatCycle_Object = MibTableColumn
zxAnEponRmVoipH248OnuHeartbeatCycle = _ZxAnEponRmVoipH248OnuHeartbeatCycle_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 9),
    _ZxAnEponRmVoipH248OnuHeartbeatCycle_Type()
)
zxAnEponRmVoipH248OnuHeartbeatCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248OnuHeartbeatCycle.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248OnuHeartbeatCycle.setUnits("Seconds")


class _ZxAnEponRmVoipH248OnuHeartbeatCount_Type(Integer32):
    """Custom type zxAnEponRmVoipH248OnuHeartbeatCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnEponRmVoipH248OnuHeartbeatCount_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248OnuHeartbeatCount_Object = MibTableColumn
zxAnEponRmVoipH248OnuHeartbeatCount = _ZxAnEponRmVoipH248OnuHeartbeatCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 10),
    _ZxAnEponRmVoipH248OnuHeartbeatCount_Type()
)
zxAnEponRmVoipH248OnuHeartbeatCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248OnuHeartbeatCount.setStatus("current")


class _ZxAnEponRmVoipH248MgRegMode_Type(Integer32):
    """Custom type zxAnEponRmVoipH248MgRegMode based on Integer32"""
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
        *(("domainName", 1),
          ("ip", 2),
          ("deviceName", 3))
    )


_ZxAnEponRmVoipH248MgRegMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248MgRegMode_Object = MibTableColumn
zxAnEponRmVoipH248MgRegMode = _ZxAnEponRmVoipH248MgRegMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 11),
    _ZxAnEponRmVoipH248MgRegMode_Type()
)
zxAnEponRmVoipH248MgRegMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgRegMode.setStatus("current")


class _ZxAnEponRmVoipH248MgPort_Type(Integer32):
    """Custom type zxAnEponRmVoipH248MgPort based on Integer32"""
    defaultValue = 2944

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipH248MgPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248MgPort_Object = MibTableColumn
zxAnEponRmVoipH248MgPort = _ZxAnEponRmVoipH248MgPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 12),
    _ZxAnEponRmVoipH248MgPort_Type()
)
zxAnEponRmVoipH248MgPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgPort.setStatus("current")
_ZxAnEponRmVoipH248RowStatus_Type = RowStatus
_ZxAnEponRmVoipH248RowStatus_Object = MibTableColumn
zxAnEponRmVoipH248RowStatus = _ZxAnEponRmVoipH248RowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 6, 1, 30),
    _ZxAnEponRmVoipH248RowStatus_Type()
)
zxAnEponRmVoipH248RowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248RowStatus.setStatus("current")
_ZxAnEponRmVoipMgcpProfileIdxNext_Type = Integer32
_ZxAnEponRmVoipMgcpProfileIdxNext_Object = MibScalar
zxAnEponRmVoipMgcpProfileIdxNext = _ZxAnEponRmVoipMgcpProfileIdxNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 7),
    _ZxAnEponRmVoipMgcpProfileIdxNext_Type()
)
zxAnEponRmVoipMgcpProfileIdxNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpProfileIdxNext.setStatus("current")
_ZxAnEponRmVoipMgcpProfileTable_Object = MibTable
zxAnEponRmVoipMgcpProfileTable = _ZxAnEponRmVoipMgcpProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpProfileTable.setStatus("current")
_ZxAnEponRmVoipMgcpProfileEntry_Object = MibTableRow
zxAnEponRmVoipMgcpProfileEntry = _ZxAnEponRmVoipMgcpProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1)
)
zxAnEponRmVoipMgcpProfileEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmVoipMgcpProfileIdx"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpProfileEntry.setStatus("current")
_ZxAnEponRmVoipMgcpProfileIdx_Type = Integer32
_ZxAnEponRmVoipMgcpProfileIdx_Object = MibTableColumn
zxAnEponRmVoipMgcpProfileIdx = _ZxAnEponRmVoipMgcpProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 1),
    _ZxAnEponRmVoipMgcpProfileIdx_Type()
)
zxAnEponRmVoipMgcpProfileIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpProfileIdx.setStatus("current")


class _ZxAnEponRmVoipMgcpProfileName_Type(DisplayString):
    """Custom type zxAnEponRmVoipMgcpProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmVoipMgcpProfileName_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipMgcpProfileName_Object = MibTableColumn
zxAnEponRmVoipMgcpProfileName = _ZxAnEponRmVoipMgcpProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 2),
    _ZxAnEponRmVoipMgcpProfileName_Type()
)
zxAnEponRmVoipMgcpProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpProfileName.setStatus("current")
_ZxAnEponRmVoipMgcpRegServerIp_Type = IpAddress
_ZxAnEponRmVoipMgcpRegServerIp_Object = MibTableColumn
zxAnEponRmVoipMgcpRegServerIp = _ZxAnEponRmVoipMgcpRegServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 3),
    _ZxAnEponRmVoipMgcpRegServerIp_Type()
)
zxAnEponRmVoipMgcpRegServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpRegServerIp.setStatus("current")


class _ZxAnEponRmVoipMgcpRegServerPort_Type(Integer32):
    """Custom type zxAnEponRmVoipMgcpRegServerPort based on Integer32"""
    defaultValue = 2727

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipMgcpRegServerPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipMgcpRegServerPort_Object = MibTableColumn
zxAnEponRmVoipMgcpRegServerPort = _ZxAnEponRmVoipMgcpRegServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 4),
    _ZxAnEponRmVoipMgcpRegServerPort_Type()
)
zxAnEponRmVoipMgcpRegServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpRegServerPort.setStatus("current")
_ZxAnEponRmVoipMgcpBackRegServerIp_Type = IpAddress
_ZxAnEponRmVoipMgcpBackRegServerIp_Object = MibTableColumn
zxAnEponRmVoipMgcpBackRegServerIp = _ZxAnEponRmVoipMgcpBackRegServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 5),
    _ZxAnEponRmVoipMgcpBackRegServerIp_Type()
)
zxAnEponRmVoipMgcpBackRegServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpBackRegServerIp.setStatus("current")


class _ZxAnEponRmVoipMgcpBackRegServerPort_Type(Integer32):
    """Custom type zxAnEponRmVoipMgcpBackRegServerPort based on Integer32"""
    defaultValue = 2727

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipMgcpBackRegServerPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipMgcpBackRegServerPort_Object = MibTableColumn
zxAnEponRmVoipMgcpBackRegServerPort = _ZxAnEponRmVoipMgcpBackRegServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 6),
    _ZxAnEponRmVoipMgcpBackRegServerPort_Type()
)
zxAnEponRmVoipMgcpBackRegServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpBackRegServerPort.setStatus("current")


class _ZxAnEponRmVoipMgcpOnuHeartbeatMode_Type(Integer32):
    """Custom type zxAnEponRmVoipMgcpOnuHeartbeatMode based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("mgcp", 2))
    )


_ZxAnEponRmVoipMgcpOnuHeartbeatMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipMgcpOnuHeartbeatMode_Object = MibTableColumn
zxAnEponRmVoipMgcpOnuHeartbeatMode = _ZxAnEponRmVoipMgcpOnuHeartbeatMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 7),
    _ZxAnEponRmVoipMgcpOnuHeartbeatMode_Type()
)
zxAnEponRmVoipMgcpOnuHeartbeatMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpOnuHeartbeatMode.setStatus("current")


class _ZxAnEponRmVoipMgcpOnuHeartbeatCycle_Type(Integer32):
    """Custom type zxAnEponRmVoipMgcpOnuHeartbeatCycle based on Integer32"""
    defaultValue = 30

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(30, 3600),
    )


_ZxAnEponRmVoipMgcpOnuHeartbeatCycle_Type.__name__ = "Integer32"
_ZxAnEponRmVoipMgcpOnuHeartbeatCycle_Object = MibTableColumn
zxAnEponRmVoipMgcpOnuHeartbeatCycle = _ZxAnEponRmVoipMgcpOnuHeartbeatCycle_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 8),
    _ZxAnEponRmVoipMgcpOnuHeartbeatCycle_Type()
)
zxAnEponRmVoipMgcpOnuHeartbeatCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpOnuHeartbeatCycle.setStatus("current")


class _ZxAnEponRmVoipMgcpOnuHeartbeatCount_Type(Integer32):
    """Custom type zxAnEponRmVoipMgcpOnuHeartbeatCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnEponRmVoipMgcpOnuHeartbeatCount_Type.__name__ = "Integer32"
_ZxAnEponRmVoipMgcpOnuHeartbeatCount_Object = MibTableColumn
zxAnEponRmVoipMgcpOnuHeartbeatCount = _ZxAnEponRmVoipMgcpOnuHeartbeatCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 9),
    _ZxAnEponRmVoipMgcpOnuHeartbeatCount_Type()
)
zxAnEponRmVoipMgcpOnuHeartbeatCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpOnuHeartbeatCount.setStatus("current")


class _ZxAnEponRmVoipMgcpMgRegMode_Type(Integer32):
    """Custom type zxAnEponRmVoipMgcpMgRegMode based on Integer32"""
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
        *(("domainName", 1),
          ("ip", 2),
          ("deviceName", 3))
    )


_ZxAnEponRmVoipMgcpMgRegMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipMgcpMgRegMode_Object = MibTableColumn
zxAnEponRmVoipMgcpMgRegMode = _ZxAnEponRmVoipMgcpMgRegMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 10),
    _ZxAnEponRmVoipMgcpMgRegMode_Type()
)
zxAnEponRmVoipMgcpMgRegMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpMgRegMode.setStatus("current")


class _ZxAnEponRmVoipMgcpMgPort_Type(Integer32):
    """Custom type zxAnEponRmVoipMgcpMgPort based on Integer32"""
    defaultValue = 2427

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipMgcpMgPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipMgcpMgPort_Object = MibTableColumn
zxAnEponRmVoipMgcpMgPort = _ZxAnEponRmVoipMgcpMgPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 11),
    _ZxAnEponRmVoipMgcpMgPort_Type()
)
zxAnEponRmVoipMgcpMgPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpMgPort.setStatus("current")
_ZxAnEponRmVoipMgcpRowStatus_Type = RowStatus
_ZxAnEponRmVoipMgcpRowStatus_Object = MibTableColumn
zxAnEponRmVoipMgcpRowStatus = _ZxAnEponRmVoipMgcpRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 8, 1, 30),
    _ZxAnEponRmVoipMgcpRowStatus_Type()
)
zxAnEponRmVoipMgcpRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMgcpRowStatus.setStatus("current")
_ZxAnEponRmVoipSipProfileIdxNext_Type = Integer32
_ZxAnEponRmVoipSipProfileIdxNext_Object = MibScalar
zxAnEponRmVoipSipProfileIdxNext = _ZxAnEponRmVoipSipProfileIdxNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 9),
    _ZxAnEponRmVoipSipProfileIdxNext_Type()
)
zxAnEponRmVoipSipProfileIdxNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipProfileIdxNext.setStatus("current")
_ZxAnEponRmVoipSipProfileTable_Object = MibTable
zxAnEponRmVoipSipProfileTable = _ZxAnEponRmVoipSipProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipProfileTable.setStatus("current")
_ZxAnEponRmVoipSipProfileEntry_Object = MibTableRow
zxAnEponRmVoipSipProfileEntry = _ZxAnEponRmVoipSipProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1)
)
zxAnEponRmVoipSipProfileEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmVoipSipProfileIdx"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipProfileEntry.setStatus("current")
_ZxAnEponRmVoipSipProfileIdx_Type = Integer32
_ZxAnEponRmVoipSipProfileIdx_Object = MibTableColumn
zxAnEponRmVoipSipProfileIdx = _ZxAnEponRmVoipSipProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 1),
    _ZxAnEponRmVoipSipProfileIdx_Type()
)
zxAnEponRmVoipSipProfileIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipProfileIdx.setStatus("current")


class _ZxAnEponRmVoipSipProfileName_Type(DisplayString):
    """Custom type zxAnEponRmVoipSipProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmVoipSipProfileName_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipSipProfileName_Object = MibTableColumn
zxAnEponRmVoipSipProfileName = _ZxAnEponRmVoipSipProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 2),
    _ZxAnEponRmVoipSipProfileName_Type()
)
zxAnEponRmVoipSipProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipProfileName.setStatus("current")


class _ZxAnEponRmVoipSipMgPort_Type(Integer32):
    """Custom type zxAnEponRmVoipSipMgPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipSipMgPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipMgPort_Object = MibTableColumn
zxAnEponRmVoipSipMgPort = _ZxAnEponRmVoipSipMgPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 3),
    _ZxAnEponRmVoipSipMgPort_Type()
)
zxAnEponRmVoipSipMgPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipMgPort.setStatus("current")
_ZxAnEponRmVoipSipRegServerIp_Type = IpAddress
_ZxAnEponRmVoipSipRegServerIp_Object = MibTableColumn
zxAnEponRmVoipSipRegServerIp = _ZxAnEponRmVoipSipRegServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 4),
    _ZxAnEponRmVoipSipRegServerIp_Type()
)
zxAnEponRmVoipSipRegServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipRegServerIp.setStatus("current")


class _ZxAnEponRmVoipSipRegServerPort_Type(Integer32):
    """Custom type zxAnEponRmVoipSipRegServerPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipSipRegServerPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipRegServerPort_Object = MibTableColumn
zxAnEponRmVoipSipRegServerPort = _ZxAnEponRmVoipSipRegServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 5),
    _ZxAnEponRmVoipSipRegServerPort_Type()
)
zxAnEponRmVoipSipRegServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipRegServerPort.setStatus("current")
_ZxAnEponRmVoipSipBackRegServerIp_Type = IpAddress
_ZxAnEponRmVoipSipBackRegServerIp_Object = MibTableColumn
zxAnEponRmVoipSipBackRegServerIp = _ZxAnEponRmVoipSipBackRegServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 6),
    _ZxAnEponRmVoipSipBackRegServerIp_Type()
)
zxAnEponRmVoipSipBackRegServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipBackRegServerIp.setStatus("current")


class _ZxAnEponRmVoipSipBackRegServerPort_Type(Integer32):
    """Custom type zxAnEponRmVoipSipBackRegServerPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipSipBackRegServerPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipBackRegServerPort_Object = MibTableColumn
zxAnEponRmVoipSipBackRegServerPort = _ZxAnEponRmVoipSipBackRegServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 7),
    _ZxAnEponRmVoipSipBackRegServerPort_Type()
)
zxAnEponRmVoipSipBackRegServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipBackRegServerPort.setStatus("current")
_ZxAnEponRmVoipSipProxyServerIp_Type = IpAddress
_ZxAnEponRmVoipSipProxyServerIp_Object = MibTableColumn
zxAnEponRmVoipSipProxyServerIp = _ZxAnEponRmVoipSipProxyServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 8),
    _ZxAnEponRmVoipSipProxyServerIp_Type()
)
zxAnEponRmVoipSipProxyServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipProxyServerIp.setStatus("current")


class _ZxAnEponRmVoipSipProxyServerPort_Type(Integer32):
    """Custom type zxAnEponRmVoipSipProxyServerPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipSipProxyServerPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipProxyServerPort_Object = MibTableColumn
zxAnEponRmVoipSipProxyServerPort = _ZxAnEponRmVoipSipProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 9),
    _ZxAnEponRmVoipSipProxyServerPort_Type()
)
zxAnEponRmVoipSipProxyServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipProxyServerPort.setStatus("current")
_ZxAnEponRmVoipSipBackProxyServerIp_Type = IpAddress
_ZxAnEponRmVoipSipBackProxyServerIp_Object = MibTableColumn
zxAnEponRmVoipSipBackProxyServerIp = _ZxAnEponRmVoipSipBackProxyServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 10),
    _ZxAnEponRmVoipSipBackProxyServerIp_Type()
)
zxAnEponRmVoipSipBackProxyServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipBackProxyServerIp.setStatus("current")


class _ZxAnEponRmVoipSipBackProxyServerPort_Type(Integer32):
    """Custom type zxAnEponRmVoipSipBackProxyServerPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipSipBackProxyServerPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipBackProxyServerPort_Object = MibTableColumn
zxAnEponRmVoipSipBackProxyServerPort = _ZxAnEponRmVoipSipBackProxyServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 11),
    _ZxAnEponRmVoipSipBackProxyServerPort_Type()
)
zxAnEponRmVoipSipBackProxyServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipBackProxyServerPort.setStatus("current")
_ZxAnEponRmVoipSipOutBoundServerIp_Type = IpAddress
_ZxAnEponRmVoipSipOutBoundServerIp_Object = MibTableColumn
zxAnEponRmVoipSipOutBoundServerIp = _ZxAnEponRmVoipSipOutBoundServerIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 12),
    _ZxAnEponRmVoipSipOutBoundServerIp_Type()
)
zxAnEponRmVoipSipOutBoundServerIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipOutBoundServerIp.setStatus("current")


class _ZxAnEponRmVoipSipOutBoundServerPort_Type(Integer32):
    """Custom type zxAnEponRmVoipSipOutBoundServerPort based on Integer32"""
    defaultValue = 5060

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1001, 65535),
    )


_ZxAnEponRmVoipSipOutBoundServerPort_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipOutBoundServerPort_Object = MibTableColumn
zxAnEponRmVoipSipOutBoundServerPort = _ZxAnEponRmVoipSipOutBoundServerPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 13),
    _ZxAnEponRmVoipSipOutBoundServerPort_Type()
)
zxAnEponRmVoipSipOutBoundServerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipOutBoundServerPort.setStatus("current")


class _ZxAnEponRmVoipSipRegInterval_Type(Integer32):
    """Custom type zxAnEponRmVoipSipRegInterval based on Integer32"""
    defaultValue = 3600

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEponRmVoipSipRegInterval_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipRegInterval_Object = MibTableColumn
zxAnEponRmVoipSipRegInterval = _ZxAnEponRmVoipSipRegInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 14),
    _ZxAnEponRmVoipSipRegInterval_Type()
)
zxAnEponRmVoipSipRegInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipRegInterval.setStatus("current")


class _ZxAnEponRmVoipSipHeartbeatSwitch_Type(Integer32):
    """Custom type zxAnEponRmVoipSipHeartbeatSwitch based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("off", 1),
          ("on", 2))
    )


_ZxAnEponRmVoipSipHeartbeatSwitch_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipHeartbeatSwitch_Object = MibTableColumn
zxAnEponRmVoipSipHeartbeatSwitch = _ZxAnEponRmVoipSipHeartbeatSwitch_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 15),
    _ZxAnEponRmVoipSipHeartbeatSwitch_Type()
)
zxAnEponRmVoipSipHeartbeatSwitch.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipHeartbeatSwitch.setStatus("current")


class _ZxAnEponRmVoipSipHeartbeatCycle_Type(Integer32):
    """Custom type zxAnEponRmVoipSipHeartbeatCycle based on Integer32"""
    defaultValue = 20

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEponRmVoipSipHeartbeatCycle_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipHeartbeatCycle_Object = MibTableColumn
zxAnEponRmVoipSipHeartbeatCycle = _ZxAnEponRmVoipSipHeartbeatCycle_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 16),
    _ZxAnEponRmVoipSipHeartbeatCycle_Type()
)
zxAnEponRmVoipSipHeartbeatCycle.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipHeartbeatCycle.setStatus("current")


class _ZxAnEponRmVoipSipHeartbeatCount_Type(Integer32):
    """Custom type zxAnEponRmVoipSipHeartbeatCount based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnEponRmVoipSipHeartbeatCount_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipHeartbeatCount_Object = MibTableColumn
zxAnEponRmVoipSipHeartbeatCount = _ZxAnEponRmVoipSipHeartbeatCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 17),
    _ZxAnEponRmVoipSipHeartbeatCount_Type()
)
zxAnEponRmVoipSipHeartbeatCount.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipHeartbeatCount.setStatus("current")
_ZxAnEponRmVoipSipRowStatus_Type = RowStatus
_ZxAnEponRmVoipSipRowStatus_Object = MibTableColumn
zxAnEponRmVoipSipRowStatus = _ZxAnEponRmVoipSipRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 10, 1, 30),
    _ZxAnEponRmVoipSipRowStatus_Type()
)
zxAnEponRmVoipSipRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipRowStatus.setStatus("current")
_ZxAnEponRmVoipFaxProfileIdxNext_Type = Integer32
_ZxAnEponRmVoipFaxProfileIdxNext_Object = MibScalar
zxAnEponRmVoipFaxProfileIdxNext = _ZxAnEponRmVoipFaxProfileIdxNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 11),
    _ZxAnEponRmVoipFaxProfileIdxNext_Type()
)
zxAnEponRmVoipFaxProfileIdxNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipFaxProfileIdxNext.setStatus("current")
_ZxAnEponRmVoipFaxProfileTable_Object = MibTable
zxAnEponRmVoipFaxProfileTable = _ZxAnEponRmVoipFaxProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 12)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipFaxProfileTable.setStatus("current")
_ZxAnEponRmVoipFaxProfileEntry_Object = MibTableRow
zxAnEponRmVoipFaxProfileEntry = _ZxAnEponRmVoipFaxProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 12, 1)
)
zxAnEponRmVoipFaxProfileEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmVoipFaxProfileIdx"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipFaxProfileEntry.setStatus("current")
_ZxAnEponRmVoipFaxProfileIdx_Type = Integer32
_ZxAnEponRmVoipFaxProfileIdx_Object = MibTableColumn
zxAnEponRmVoipFaxProfileIdx = _ZxAnEponRmVoipFaxProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 12, 1, 1),
    _ZxAnEponRmVoipFaxProfileIdx_Type()
)
zxAnEponRmVoipFaxProfileIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmVoipFaxProfileIdx.setStatus("current")


class _ZxAnEponRmVoipFaxProfileName_Type(DisplayString):
    """Custom type zxAnEponRmVoipFaxProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmVoipFaxProfileName_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipFaxProfileName_Object = MibTableColumn
zxAnEponRmVoipFaxProfileName = _ZxAnEponRmVoipFaxProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 12, 1, 2),
    _ZxAnEponRmVoipFaxProfileName_Type()
)
zxAnEponRmVoipFaxProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipFaxProfileName.setStatus("current")


class _ZxAnEponRmVoipFaxMode_Type(Integer32):
    """Custom type zxAnEponRmVoipFaxMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("t30", 1),
          ("t38", 2))
    )


_ZxAnEponRmVoipFaxMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipFaxMode_Object = MibTableColumn
zxAnEponRmVoipFaxMode = _ZxAnEponRmVoipFaxMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 12, 1, 3),
    _ZxAnEponRmVoipFaxMode_Type()
)
zxAnEponRmVoipFaxMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipFaxMode.setStatus("current")


class _ZxAnEponRmVoipFaxControlMode_Type(Integer32):
    """Custom type zxAnEponRmVoipFaxControlMode based on Integer32"""
    defaultValue = 3

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
        *(("none", 1),
          ("rtcp", 2),
          ("ss", 3),
          ("autoVbd", 4))
    )


_ZxAnEponRmVoipFaxControlMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipFaxControlMode_Object = MibTableColumn
zxAnEponRmVoipFaxControlMode = _ZxAnEponRmVoipFaxControlMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 12, 1, 4),
    _ZxAnEponRmVoipFaxControlMode_Type()
)
zxAnEponRmVoipFaxControlMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipFaxControlMode.setStatus("current")
_ZxAnEponRmVoipFaxRowStatus_Type = RowStatus
_ZxAnEponRmVoipFaxRowStatus_Object = MibTableColumn
zxAnEponRmVoipFaxRowStatus = _ZxAnEponRmVoipFaxRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 35, 12, 1, 30),
    _ZxAnEponRmVoipFaxRowStatus_Type()
)
zxAnEponRmVoipFaxRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipFaxRowStatus.setStatus("current")
_ZxAnEponRmVoipMgmt_ObjectIdentity = ObjectIdentity
zxAnEponRmVoipMgmt = _ZxAnEponRmVoipMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36)
)
_ZxAnEponRmVoipIpInfoTable_Object = MibTable
zxAnEponRmVoipIpInfoTable = _ZxAnEponRmVoipIpInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 1)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpInfoTable.setStatus("current")
_ZxAnEponRmVoipIpInfoEntry_Object = MibTableRow
zxAnEponRmVoipIpInfoEntry = _ZxAnEponRmVoipIpInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 1, 1)
)
zxAnEponRmVoipIpInfoEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpInfoEntry.setStatus("current")
_ZxAnEponOnuCardIndex_Type = Integer32
_ZxAnEponOnuCardIndex_Object = MibTableColumn
zxAnEponOnuCardIndex = _ZxAnEponOnuCardIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 1, 1, 1),
    _ZxAnEponOnuCardIndex_Type()
)
zxAnEponOnuCardIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuCardIndex.setStatus("current")
_ZxAnEponRmVoipIpAddress_Type = IpAddress
_ZxAnEponRmVoipIpAddress_Object = MibTableColumn
zxAnEponRmVoipIpAddress = _ZxAnEponRmVoipIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 1, 1, 2),
    _ZxAnEponRmVoipIpAddress_Type()
)
zxAnEponRmVoipIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpAddress.setStatus("current")
_ZxAnEponRmVoipIpNetMask_Type = IpAddress
_ZxAnEponRmVoipIpNetMask_Object = MibTableColumn
zxAnEponRmVoipIpNetMask = _ZxAnEponRmVoipIpNetMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 1, 1, 3),
    _ZxAnEponRmVoipIpNetMask_Type()
)
zxAnEponRmVoipIpNetMask.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipIpNetMask.setStatus("current")
_ZxAnEponRmVoipPppoeInfoTable_Object = MibTable
zxAnEponRmVoipPppoeInfoTable = _ZxAnEponRmVoipPppoeInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 2)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipPppoeInfoTable.setStatus("current")
_ZxAnEponRmVoipPppoeInfoEntry_Object = MibTableRow
zxAnEponRmVoipPppoeInfoEntry = _ZxAnEponRmVoipPppoeInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 2, 1)
)
zxAnEponRmVoipPppoeInfoEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipPppoeInfoEntry.setStatus("current")


class _ZxAnEponRmVoipPppoeUserName_Type(DisplayString):
    """Custom type zxAnEponRmVoipPppoeUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmVoipPppoeUserName_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipPppoeUserName_Object = MibTableColumn
zxAnEponRmVoipPppoeUserName = _ZxAnEponRmVoipPppoeUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 2, 1, 1),
    _ZxAnEponRmVoipPppoeUserName_Type()
)
zxAnEponRmVoipPppoeUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipPppoeUserName.setStatus("current")


class _ZxAnEponRmVoipPppoePassword_Type(DisplayString):
    """Custom type zxAnEponRmVoipPppoePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmVoipPppoePassword_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipPppoePassword_Object = MibTableColumn
zxAnEponRmVoipPppoePassword = _ZxAnEponRmVoipPppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 2, 1, 2),
    _ZxAnEponRmVoipPppoePassword_Type()
)
zxAnEponRmVoipPppoePassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipPppoePassword.setStatus("current")
_ZxAnEponRmVoipH248MgcpAttrTable_Object = MibTable
zxAnEponRmVoipH248MgcpAttrTable = _ZxAnEponRmVoipH248MgcpAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 3)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpAttrTable.setStatus("current")
_ZxAnEponRmVoipH248MgcpAttrEntry_Object = MibTableRow
zxAnEponRmVoipH248MgcpAttrEntry = _ZxAnEponRmVoipH248MgcpAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 3, 1)
)
zxAnEponRmVoipH248MgcpAttrEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpAttrEntry.setStatus("current")


class _ZxAnEponRmVoipH248MgcpMID_Type(DisplayString):
    """Custom type zxAnEponRmVoipH248MgcpMID based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 64),
    )


_ZxAnEponRmVoipH248MgcpMID_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipH248MgcpMID_Object = MibTableColumn
zxAnEponRmVoipH248MgcpMID = _ZxAnEponRmVoipH248MgcpMID_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 3, 1, 1),
    _ZxAnEponRmVoipH248MgcpMID_Type()
)
zxAnEponRmVoipH248MgcpMID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpMID.setStatus("current")


class _ZxAnEponRmVoipH248MgcpActiveMgc_Type(Integer32):
    """Custom type zxAnEponRmVoipH248MgcpActiveMgc based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("secondary", 1),
          ("primary", 2))
    )


_ZxAnEponRmVoipH248MgcpActiveMgc_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248MgcpActiveMgc_Object = MibTableColumn
zxAnEponRmVoipH248MgcpActiveMgc = _ZxAnEponRmVoipH248MgcpActiveMgc_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 3, 1, 2),
    _ZxAnEponRmVoipH248MgcpActiveMgc_Type()
)
zxAnEponRmVoipH248MgcpActiveMgc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpActiveMgc.setStatus("current")
_ZxAnEponRmVoipH248MgcpUserTidCfgTable_Object = MibTable
zxAnEponRmVoipH248MgcpUserTidCfgTable = _ZxAnEponRmVoipH248MgcpUserTidCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 4)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidCfgTable.setStatus("current")
_ZxAnEponRmVoipH248MgcpUserTidCfgEntry_Object = MibTableRow
zxAnEponRmVoipH248MgcpUserTidCfgEntry = _ZxAnEponRmVoipH248MgcpUserTidCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 4, 1)
)
zxAnEponRmVoipH248MgcpUserTidCfgEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmVoipH248MgcpUserTidGroupIdx"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidCfgEntry.setStatus("current")
_ZxAnEponRmVoipH248MgcpUserTidGroupIdx_Type = Integer32
_ZxAnEponRmVoipH248MgcpUserTidGroupIdx_Object = MibTableColumn
zxAnEponRmVoipH248MgcpUserTidGroupIdx = _ZxAnEponRmVoipH248MgcpUserTidGroupIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 4, 1, 1),
    _ZxAnEponRmVoipH248MgcpUserTidGroupIdx_Type()
)
zxAnEponRmVoipH248MgcpUserTidGroupIdx.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidGroupIdx.setStatus("current")


class _ZxAnEponRmVoipH248MgcpUserTidBeginIdx_Type(Integer32):
    """Custom type zxAnEponRmVoipH248MgcpUserTidBeginIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnEponRmVoipH248MgcpUserTidBeginIdx_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248MgcpUserTidBeginIdx_Object = MibTableColumn
zxAnEponRmVoipH248MgcpUserTidBeginIdx = _ZxAnEponRmVoipH248MgcpUserTidBeginIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 4, 1, 2),
    _ZxAnEponRmVoipH248MgcpUserTidBeginIdx_Type()
)
zxAnEponRmVoipH248MgcpUserTidBeginIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidBeginIdx.setStatus("current")


class _ZxAnEponRmVoipH248MgcpUserTidNumber_Type(Integer32):
    """Custom type zxAnEponRmVoipH248MgcpUserTidNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnEponRmVoipH248MgcpUserTidNumber_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248MgcpUserTidNumber_Object = MibTableColumn
zxAnEponRmVoipH248MgcpUserTidNumber = _ZxAnEponRmVoipH248MgcpUserTidNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 4, 1, 3),
    _ZxAnEponRmVoipH248MgcpUserTidNumber_Type()
)
zxAnEponRmVoipH248MgcpUserTidNumber.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidNumber.setStatus("current")


class _ZxAnEponRmVoipH248MgcpUserTidPrefix_Type(DisplayString):
    """Custom type zxAnEponRmVoipH248MgcpUserTidPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnEponRmVoipH248MgcpUserTidPrefix_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipH248MgcpUserTidPrefix_Object = MibTableColumn
zxAnEponRmVoipH248MgcpUserTidPrefix = _ZxAnEponRmVoipH248MgcpUserTidPrefix_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 4, 1, 4),
    _ZxAnEponRmVoipH248MgcpUserTidPrefix_Type()
)
zxAnEponRmVoipH248MgcpUserTidPrefix.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidPrefix.setStatus("current")


class _ZxAnEponRmVoipH248MgcpUserTidBeginDigit_Type(DisplayString):
    """Custom type zxAnEponRmVoipH248MgcpUserTidBeginDigit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ZxAnEponRmVoipH248MgcpUserTidBeginDigit_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipH248MgcpUserTidBeginDigit_Object = MibTableColumn
zxAnEponRmVoipH248MgcpUserTidBeginDigit = _ZxAnEponRmVoipH248MgcpUserTidBeginDigit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 4, 1, 5),
    _ZxAnEponRmVoipH248MgcpUserTidBeginDigit_Type()
)
zxAnEponRmVoipH248MgcpUserTidBeginDigit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidBeginDigit.setStatus("current")


class _ZxAnEponRmVoipH248MgcpUserTidDigitAlignMode_Type(Integer32):
    """Custom type zxAnEponRmVoipH248MgcpUserTidDigitAlignMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("align", 1),
          ("noAlign", 2))
    )


_ZxAnEponRmVoipH248MgcpUserTidDigitAlignMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248MgcpUserTidDigitAlignMode_Object = MibTableColumn
zxAnEponRmVoipH248MgcpUserTidDigitAlignMode = _ZxAnEponRmVoipH248MgcpUserTidDigitAlignMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 4, 1, 6),
    _ZxAnEponRmVoipH248MgcpUserTidDigitAlignMode_Type()
)
zxAnEponRmVoipH248MgcpUserTidDigitAlignMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidDigitAlignMode.setStatus("current")


class _ZxAnEponRmVoipH248MgcpUserTidDigitLength_Type(Integer32):
    """Custom type zxAnEponRmVoipH248MgcpUserTidDigitLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_ZxAnEponRmVoipH248MgcpUserTidDigitLength_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248MgcpUserTidDigitLength_Object = MibTableColumn
zxAnEponRmVoipH248MgcpUserTidDigitLength = _ZxAnEponRmVoipH248MgcpUserTidDigitLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 4, 1, 7),
    _ZxAnEponRmVoipH248MgcpUserTidDigitLength_Type()
)
zxAnEponRmVoipH248MgcpUserTidDigitLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidDigitLength.setStatus("current")
_ZxAnEponRmVoipH248MgcpUserTidRowStatus_Type = RowStatus
_ZxAnEponRmVoipH248MgcpUserTidRowStatus_Object = MibTableColumn
zxAnEponRmVoipH248MgcpUserTidRowStatus = _ZxAnEponRmVoipH248MgcpUserTidRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 4, 1, 30),
    _ZxAnEponRmVoipH248MgcpUserTidRowStatus_Type()
)
zxAnEponRmVoipH248MgcpUserTidRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidRowStatus.setStatus("current")
_ZxAnEponRmVoipH248MgcpRtpTidCfgTable_Object = MibTable
zxAnEponRmVoipH248MgcpRtpTidCfgTable = _ZxAnEponRmVoipH248MgcpRtpTidCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 5)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidCfgTable.setStatus("current")
_ZxAnEponRmVoipH248MgcpRtpTidCfgEntry_Object = MibTableRow
zxAnEponRmVoipH248MgcpRtpTidCfgEntry = _ZxAnEponRmVoipH248MgcpRtpTidCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 5, 1)
)
zxAnEponRmVoipH248MgcpRtpTidCfgEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidCfgEntry.setStatus("current")


class _ZxAnEponRmVoipH248MgcpRtpTidPrefix_Type(DisplayString):
    """Custom type zxAnEponRmVoipH248MgcpRtpTidPrefix based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnEponRmVoipH248MgcpRtpTidPrefix_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipH248MgcpRtpTidPrefix_Object = MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidPrefix = _ZxAnEponRmVoipH248MgcpRtpTidPrefix_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 5, 1, 1),
    _ZxAnEponRmVoipH248MgcpRtpTidPrefix_Type()
)
zxAnEponRmVoipH248MgcpRtpTidPrefix.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidPrefix.setStatus("current")


class _ZxAnEponRmVoipH248MgcpRtpTidBeginDigit_Type(DisplayString):
    """Custom type zxAnEponRmVoipH248MgcpRtpTidBeginDigit based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 5),
    )


_ZxAnEponRmVoipH248MgcpRtpTidBeginDigit_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipH248MgcpRtpTidBeginDigit_Object = MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidBeginDigit = _ZxAnEponRmVoipH248MgcpRtpTidBeginDigit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 5, 1, 2),
    _ZxAnEponRmVoipH248MgcpRtpTidBeginDigit_Type()
)
zxAnEponRmVoipH248MgcpRtpTidBeginDigit.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidBeginDigit.setStatus("current")


class _ZxAnEponRmVoipH248MgcpRtpTidDigitAlignMode_Type(Integer32):
    """Custom type zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("align", 1),
          ("noAlign", 2))
    )


_ZxAnEponRmVoipH248MgcpRtpTidDigitAlignMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248MgcpRtpTidDigitAlignMode_Object = MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode = _ZxAnEponRmVoipH248MgcpRtpTidDigitAlignMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 5, 1, 3),
    _ZxAnEponRmVoipH248MgcpRtpTidDigitAlignMode_Type()
)
zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode.setStatus("current")


class _ZxAnEponRmVoipH248MgcpRtpTidDigitLength_Type(Integer32):
    """Custom type zxAnEponRmVoipH248MgcpRtpTidDigitLength based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 5),
    )


_ZxAnEponRmVoipH248MgcpRtpTidDigitLength_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248MgcpRtpTidDigitLength_Object = MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidDigitLength = _ZxAnEponRmVoipH248MgcpRtpTidDigitLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 5, 1, 4),
    _ZxAnEponRmVoipH248MgcpRtpTidDigitLength_Type()
)
zxAnEponRmVoipH248MgcpRtpTidDigitLength.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidDigitLength.setStatus("current")


class _ZxAnEponRmVoipH248MgcpRtpTidNum_Type(Integer32):
    """Custom type zxAnEponRmVoipH248MgcpRtpTidNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnEponRmVoipH248MgcpRtpTidNum_Type.__name__ = "Integer32"
_ZxAnEponRmVoipH248MgcpRtpTidNum_Object = MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidNum = _ZxAnEponRmVoipH248MgcpRtpTidNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 5, 1, 5),
    _ZxAnEponRmVoipH248MgcpRtpTidNum_Type()
)
zxAnEponRmVoipH248MgcpRtpTidNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidNum.setStatus("current")
_ZxAnEponRmVoipSipUserCfgTable_Object = MibTable
zxAnEponRmVoipSipUserCfgTable = _ZxAnEponRmVoipSipUserCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 6)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipUserCfgTable.setStatus("current")
_ZxAnEponRmVoipSipUserCfgEntry_Object = MibTableRow
zxAnEponRmVoipSipUserCfgEntry = _ZxAnEponRmVoipSipUserCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 6, 1)
)
zxAnEponRmVoipSipUserCfgEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipUserCfgEntry.setStatus("current")


class _ZxAnEponRmVoipSipUserAccount_Type(DisplayString):
    """Custom type zxAnEponRmVoipSipUserAccount based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnEponRmVoipSipUserAccount_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipSipUserAccount_Object = MibTableColumn
zxAnEponRmVoipSipUserAccount = _ZxAnEponRmVoipSipUserAccount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 6, 1, 1),
    _ZxAnEponRmVoipSipUserAccount_Type()
)
zxAnEponRmVoipSipUserAccount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipUserAccount.setStatus("current")


class _ZxAnEponRmVoipSipUserName_Type(DisplayString):
    """Custom type zxAnEponRmVoipSipUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmVoipSipUserName_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipSipUserName_Object = MibTableColumn
zxAnEponRmVoipSipUserName = _ZxAnEponRmVoipSipUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 6, 1, 2),
    _ZxAnEponRmVoipSipUserName_Type()
)
zxAnEponRmVoipSipUserName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipUserName.setStatus("current")


class _ZxAnEponRmVoipSipUserPassword_Type(DisplayString):
    """Custom type zxAnEponRmVoipSipUserPassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 16),
    )


_ZxAnEponRmVoipSipUserPassword_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipSipUserPassword_Object = MibTableColumn
zxAnEponRmVoipSipUserPassword = _ZxAnEponRmVoipSipUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 6, 1, 3),
    _ZxAnEponRmVoipSipUserPassword_Type()
)
zxAnEponRmVoipSipUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipUserPassword.setStatus("current")
_ZxAnEponRmVoipBaseInfoTable_Object = MibTable
zxAnEponRmVoipBaseInfoTable = _ZxAnEponRmVoipBaseInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 7)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipBaseInfoTable.setStatus("current")
_ZxAnEponRmVoipBaseInfoEntry_Object = MibTableRow
zxAnEponRmVoipBaseInfoEntry = _ZxAnEponRmVoipBaseInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 7, 1)
)
zxAnEponRmVoipBaseInfoEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipBaseInfoEntry.setStatus("current")
_ZxAnEponRmVoipMacAddress_Type = MacAddress
_ZxAnEponRmVoipMacAddress_Object = MibTableColumn
zxAnEponRmVoipMacAddress = _ZxAnEponRmVoipMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 7, 1, 1),
    _ZxAnEponRmVoipMacAddress_Type()
)
zxAnEponRmVoipMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipMacAddress.setStatus("current")


class _ZxAnEponRmVoipProtocolSupported_Type(Bits):
    """Custom type zxAnEponRmVoipProtocolSupported based on Bits"""
    namedValues = NamedValues(
        *(("sip", 0),
          ("h248", 1),
          ("mgcp", 2))
    )

_ZxAnEponRmVoipProtocolSupported_Type.__name__ = "Bits"
_ZxAnEponRmVoipProtocolSupported_Object = MibTableColumn
zxAnEponRmVoipProtocolSupported = _ZxAnEponRmVoipProtocolSupported_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 7, 1, 2),
    _ZxAnEponRmVoipProtocolSupported_Type()
)
zxAnEponRmVoipProtocolSupported.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipProtocolSupported.setStatus("current")


class _ZxAnEponRmVoipSoftwareVersion_Type(DisplayString):
    """Custom type zxAnEponRmVoipSoftwareVersion based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnEponRmVoipSoftwareVersion_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipSoftwareVersion_Object = MibTableColumn
zxAnEponRmVoipSoftwareVersion = _ZxAnEponRmVoipSoftwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 7, 1, 3),
    _ZxAnEponRmVoipSoftwareVersion_Type()
)
zxAnEponRmVoipSoftwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSoftwareVersion.setStatus("current")


class _ZxAnEponRmVoipSoftwareVersionTime_Type(DisplayString):
    """Custom type zxAnEponRmVoipSoftwareVersionTime based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnEponRmVoipSoftwareVersionTime_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipSoftwareVersionTime_Object = MibTableColumn
zxAnEponRmVoipSoftwareVersionTime = _ZxAnEponRmVoipSoftwareVersionTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 7, 1, 4),
    _ZxAnEponRmVoipSoftwareVersionTime_Type()
)
zxAnEponRmVoipSoftwareVersionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSoftwareVersionTime.setStatus("current")
_ZxAnEponRmVoipUserCount_Type = Integer32
_ZxAnEponRmVoipUserCount_Object = MibTableColumn
zxAnEponRmVoipUserCount = _ZxAnEponRmVoipUserCount_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 7, 1, 5),
    _ZxAnEponRmVoipUserCount_Type()
)
zxAnEponRmVoipUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipUserCount.setStatus("current")


class _ZxAnEponRmVoipProtocolUsed_Type(Integer32):
    """Custom type zxAnEponRmVoipProtocolUsed based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("h248", 2),
          ("mgcp", 3))
    )


_ZxAnEponRmVoipProtocolUsed_Type.__name__ = "Integer32"
_ZxAnEponRmVoipProtocolUsed_Object = MibTableColumn
zxAnEponRmVoipProtocolUsed = _ZxAnEponRmVoipProtocolUsed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 7, 1, 6),
    _ZxAnEponRmVoipProtocolUsed_Type()
)
zxAnEponRmVoipProtocolUsed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipProtocolUsed.setStatus("current")
_ZxAnEponRmVoipH248MgcpUserTidInfoTable_Object = MibTable
zxAnEponRmVoipH248MgcpUserTidInfoTable = _ZxAnEponRmVoipH248MgcpUserTidInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 8)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidInfoTable.setStatus("current")
_ZxAnEponRmVoipH248MgcpUserTidInfoEntry_Object = MibTableRow
zxAnEponRmVoipH248MgcpUserTidInfoEntry = _ZxAnEponRmVoipH248MgcpUserTidInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 8, 1)
)
zxAnEponRmVoipH248MgcpUserTidInfoEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidInfoEntry.setStatus("current")


class _ZxAnEponRmVoipH248MgcpUserTidName_Type(DisplayString):
    """Custom type zxAnEponRmVoipH248MgcpUserTidName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnEponRmVoipH248MgcpUserTidName_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipH248MgcpUserTidName_Object = MibTableColumn
zxAnEponRmVoipH248MgcpUserTidName = _ZxAnEponRmVoipH248MgcpUserTidName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 8, 1, 1),
    _ZxAnEponRmVoipH248MgcpUserTidName_Type()
)
zxAnEponRmVoipH248MgcpUserTidName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpUserTidName.setStatus("current")
_ZxAnEponRmVoipH248MgcpRtpTidInfoTable_Object = MibTable
zxAnEponRmVoipH248MgcpRtpTidInfoTable = _ZxAnEponRmVoipH248MgcpRtpTidInfoTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 9)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidInfoTable.setStatus("current")
_ZxAnEponRmVoipH248MgcpRtpTidInfoEntry_Object = MibTableRow
zxAnEponRmVoipH248MgcpRtpTidInfoEntry = _ZxAnEponRmVoipH248MgcpRtpTidInfoEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 9, 1)
)
zxAnEponRmVoipH248MgcpRtpTidInfoEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidInfoEntry.setStatus("current")
_ZxAnEponRmVoipH248MgcpRtpTidNumber_Type = Integer32
_ZxAnEponRmVoipH248MgcpRtpTidNumber_Object = MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidNumber = _ZxAnEponRmVoipH248MgcpRtpTidNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 9, 1, 1),
    _ZxAnEponRmVoipH248MgcpRtpTidNumber_Type()
)
zxAnEponRmVoipH248MgcpRtpTidNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidNumber.setStatus("current")


class _ZxAnEponRmVoipH248MgcpRtpTidFirstName_Type(DisplayString):
    """Custom type zxAnEponRmVoipH248MgcpRtpTidFirstName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnEponRmVoipH248MgcpRtpTidFirstName_Type.__name__ = "DisplayString"
_ZxAnEponRmVoipH248MgcpRtpTidFirstName_Object = MibTableColumn
zxAnEponRmVoipH248MgcpRtpTidFirstName = _ZxAnEponRmVoipH248MgcpRtpTidFirstName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 9, 1, 2),
    _ZxAnEponRmVoipH248MgcpRtpTidFirstName_Type()
)
zxAnEponRmVoipH248MgcpRtpTidFirstName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipH248MgcpRtpTidFirstName.setStatus("current")
_ZxAnEponRmVoipModuleStatusTable_Object = MibTable
zxAnEponRmVoipModuleStatusTable = _ZxAnEponRmVoipModuleStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 10)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipModuleStatusTable.setStatus("current")
_ZxAnEponRmVoipModuleStatusEntry_Object = MibTableRow
zxAnEponRmVoipModuleStatusEntry = _ZxAnEponRmVoipModuleStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 10, 1)
)
zxAnEponRmVoipModuleStatusEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipModuleStatusEntry.setStatus("current")


class _ZxAnEponRmVoipModuleStatus_Type(Integer32):
    """Custom type zxAnEponRmVoipModuleStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              255)
        )
    )
    namedValues = NamedValues(
        *(("registering", 1),
          ("registerSuccess", 2),
          ("fault", 3),
          ("deregister", 4),
          ("rebooting", 5),
          ("other", 255))
    )


_ZxAnEponRmVoipModuleStatus_Type.__name__ = "Integer32"
_ZxAnEponRmVoipModuleStatus_Object = MibTableColumn
zxAnEponRmVoipModuleStatus = _ZxAnEponRmVoipModuleStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 10, 1, 1),
    _ZxAnEponRmVoipModuleStatus_Type()
)
zxAnEponRmVoipModuleStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipModuleStatus.setStatus("current")


class _ZxAnEponRmVoipModuleAction_Type(Integer32):
    """Custom type zxAnEponRmVoipModuleAction based on Integer32"""
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
        *(("register", 1),
          ("deregister", 2),
          ("reset", 3),
          ("restore", 4))
    )


_ZxAnEponRmVoipModuleAction_Type.__name__ = "Integer32"
_ZxAnEponRmVoipModuleAction_Object = MibTableColumn
zxAnEponRmVoipModuleAction = _ZxAnEponRmVoipModuleAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 10, 1, 2),
    _ZxAnEponRmVoipModuleAction_Type()
)
zxAnEponRmVoipModuleAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipModuleAction.setStatus("current")
_ZxAnEponRmVoipUserIfStatusTable_Object = MibTable
zxAnEponRmVoipUserIfStatusTable = _ZxAnEponRmVoipUserIfStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 11)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipUserIfStatusTable.setStatus("current")
_ZxAnEponRmVoipUserIfStatusEntry_Object = MibTableRow
zxAnEponRmVoipUserIfStatusEntry = _ZxAnEponRmVoipUserIfStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 11, 1)
)
zxAnEponRmVoipUserIfStatusEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipUserIfStatusEntry.setStatus("current")


class _ZxAnEponRmVoipPortOperStatus_Type(Integer32):
    """Custom type zxAnEponRmVoipPortOperStatus based on Integer32"""
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
              12)
        )
    )
    namedValues = NamedValues(
        *(("registering", 1),
          ("idle", 2),
          ("hold", 3),
          ("dialing", 4),
          ("ringing", 5),
          ("ringingBack", 6),
          ("connecting", 7),
          ("connected", 8),
          ("releasing", 9),
          ("busy", 10),
          ("registerFail", 11),
          ("deactive", 12))
    )


_ZxAnEponRmVoipPortOperStatus_Type.__name__ = "Integer32"
_ZxAnEponRmVoipPortOperStatus_Object = MibTableColumn
zxAnEponRmVoipPortOperStatus = _ZxAnEponRmVoipPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 11, 1, 1),
    _ZxAnEponRmVoipPortOperStatus_Type()
)
zxAnEponRmVoipPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipPortOperStatus.setStatus("current")


class _ZxAnEponRmVoipPortServiceType_Type(Integer32):
    """Custom type zxAnEponRmVoipPortServiceType based on Integer32"""
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
        *(("normal", 1),
          ("innerSpc", 2),
          ("ipSpc", 3),
          ("notInService", 4),
          ("notSupport", 5))
    )


_ZxAnEponRmVoipPortServiceType_Type.__name__ = "Integer32"
_ZxAnEponRmVoipPortServiceType_Object = MibTableColumn
zxAnEponRmVoipPortServiceType = _ZxAnEponRmVoipPortServiceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 11, 1, 2),
    _ZxAnEponRmVoipPortServiceType_Type()
)
zxAnEponRmVoipPortServiceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipPortServiceType.setStatus("current")


class _ZxAnEponRmVoipPortServiceState_Type(Integer32):
    """Custom type zxAnEponRmVoipPortServiceState based on Integer32"""
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
        *(("endLocal", 1),
          ("endRemote", 2),
          ("endAuto", 3),
          ("normalState", 4))
    )


_ZxAnEponRmVoipPortServiceState_Type.__name__ = "Integer32"
_ZxAnEponRmVoipPortServiceState_Object = MibTableColumn
zxAnEponRmVoipPortServiceState = _ZxAnEponRmVoipPortServiceState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 11, 1, 3),
    _ZxAnEponRmVoipPortServiceState_Type()
)
zxAnEponRmVoipPortServiceState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipPortServiceState.setStatus("current")


class _ZxAnEponRmVoipPortCodecMode_Type(Integer32):
    """Custom type zxAnEponRmVoipPortCodecMode based on Integer32"""
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
              8)
        )
    )
    namedValues = NamedValues(
        *(("g711U", 1),
          ("g711A", 2),
          ("g723", 3),
          ("g729", 4),
          ("g726", 5),
          ("t38", 6),
          ("connectionless", 7),
          ("other", 8))
    )


_ZxAnEponRmVoipPortCodecMode_Type.__name__ = "Integer32"
_ZxAnEponRmVoipPortCodecMode_Object = MibTableColumn
zxAnEponRmVoipPortCodecMode = _ZxAnEponRmVoipPortCodecMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 11, 1, 4),
    _ZxAnEponRmVoipPortCodecMode_Type()
)
zxAnEponRmVoipPortCodecMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipPortCodecMode.setStatus("current")


class _ZxAnEponRmVoipPortAction_Type(Integer32):
    """Custom type zxAnEponRmVoipPortAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("register", 1),
          ("deregister", 2))
    )


_ZxAnEponRmVoipPortAction_Type.__name__ = "Integer32"
_ZxAnEponRmVoipPortAction_Object = MibTableColumn
zxAnEponRmVoipPortAction = _ZxAnEponRmVoipPortAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 11, 1, 5),
    _ZxAnEponRmVoipPortAction_Type()
)
zxAnEponRmVoipPortAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipPortAction.setStatus("current")


class _ZxAnEponRmVoipPortReversalCtrl_Type(Integer32):
    """Custom type zxAnEponRmVoipPortReversalCtrl based on Integer32"""
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


_ZxAnEponRmVoipPortReversalCtrl_Type.__name__ = "Integer32"
_ZxAnEponRmVoipPortReversalCtrl_Object = MibTableColumn
zxAnEponRmVoipPortReversalCtrl = _ZxAnEponRmVoipPortReversalCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 11, 1, 6),
    _ZxAnEponRmVoipPortReversalCtrl_Type()
)
zxAnEponRmVoipPortReversalCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipPortReversalCtrl.setStatus("current")
_ZxAnEponRmVoipPortPcmToPktGain_Type = Integer32
_ZxAnEponRmVoipPortPcmToPktGain_Object = MibTableColumn
zxAnEponRmVoipPortPcmToPktGain = _ZxAnEponRmVoipPortPcmToPktGain_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 11, 1, 7),
    _ZxAnEponRmVoipPortPcmToPktGain_Type()
)
zxAnEponRmVoipPortPcmToPktGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipPortPcmToPktGain.setStatus("current")
_ZxAnEponRmVoipPortPktToPcmGain_Type = Integer32
_ZxAnEponRmVoipPortPktToPcmGain_Object = MibTableColumn
zxAnEponRmVoipPortPktToPcmGain = _ZxAnEponRmVoipPortPktToPcmGain_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 11, 1, 8),
    _ZxAnEponRmVoipPortPktToPcmGain_Type()
)
zxAnEponRmVoipPortPktToPcmGain.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipPortPktToPcmGain.setStatus("current")
_ZxAnEponRmVoipProfileApplyTable_Object = MibTable
zxAnEponRmVoipProfileApplyTable = _ZxAnEponRmVoipProfileApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 12)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipProfileApplyTable.setStatus("current")
_ZxAnEponRmVoipProfileApplyEntry_Object = MibTableRow
zxAnEponRmVoipProfileApplyEntry = _ZxAnEponRmVoipProfileApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 12, 1)
)
zxAnEponRmVoipProfileApplyEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipProfileApplyEntry.setStatus("current")
_ZxAnEponRmVoipCurrIpProfileIdx_Type = Integer32
_ZxAnEponRmVoipCurrIpProfileIdx_Object = MibTableColumn
zxAnEponRmVoipCurrIpProfileIdx = _ZxAnEponRmVoipCurrIpProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 12, 1, 1),
    _ZxAnEponRmVoipCurrIpProfileIdx_Type()
)
zxAnEponRmVoipCurrIpProfileIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipCurrIpProfileIdx.setStatus("current")
_ZxAnEponRmVoipCurrVlanProfileIdx_Type = Integer32
_ZxAnEponRmVoipCurrVlanProfileIdx_Object = MibTableColumn
zxAnEponRmVoipCurrVlanProfileIdx = _ZxAnEponRmVoipCurrVlanProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 12, 1, 2),
    _ZxAnEponRmVoipCurrVlanProfileIdx_Type()
)
zxAnEponRmVoipCurrVlanProfileIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipCurrVlanProfileIdx.setStatus("current")


class _ZxAnEponRmVoipCurrProtocolProfileType_Type(Integer32):
    """Custom type zxAnEponRmVoipCurrProtocolProfileType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sip", 1),
          ("h248", 2),
          ("mgcp", 3))
    )


_ZxAnEponRmVoipCurrProtocolProfileType_Type.__name__ = "Integer32"
_ZxAnEponRmVoipCurrProtocolProfileType_Object = MibTableColumn
zxAnEponRmVoipCurrProtocolProfileType = _ZxAnEponRmVoipCurrProtocolProfileType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 12, 1, 3),
    _ZxAnEponRmVoipCurrProtocolProfileType_Type()
)
zxAnEponRmVoipCurrProtocolProfileType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipCurrProtocolProfileType.setStatus("current")
_ZxAnEponRmVoipCurrProtocolProfileIdx_Type = Integer32
_ZxAnEponRmVoipCurrProtocolProfileIdx_Object = MibTableColumn
zxAnEponRmVoipCurrProtocolProfileIdx = _ZxAnEponRmVoipCurrProtocolProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 12, 1, 4),
    _ZxAnEponRmVoipCurrProtocolProfileIdx_Type()
)
zxAnEponRmVoipCurrProtocolProfileIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipCurrProtocolProfileIdx.setStatus("current")
_ZxAnEponRmVoipCurrFaxProfileIdx_Type = Integer32
_ZxAnEponRmVoipCurrFaxProfileIdx_Object = MibTableColumn
zxAnEponRmVoipCurrFaxProfileIdx = _ZxAnEponRmVoipCurrFaxProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 12, 1, 5),
    _ZxAnEponRmVoipCurrFaxProfileIdx_Type()
)
zxAnEponRmVoipCurrFaxProfileIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmVoipCurrFaxProfileIdx.setStatus("current")
_ZxAnEponRmVoipSipAttrTable_Object = MibTable
zxAnEponRmVoipSipAttrTable = _ZxAnEponRmVoipSipAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 13)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipAttrTable.setStatus("current")
_ZxAnEponRmVoipSipAttrEntry_Object = MibTableRow
zxAnEponRmVoipSipAttrEntry = _ZxAnEponRmVoipSipAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 13, 1)
)
zxAnEponRmVoipSipAttrEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipAttrEntry.setStatus("current")


class _ZxAnEponRmVoipSipActiveProxyServer_Type(Integer32):
    """Custom type zxAnEponRmVoipSipActiveProxyServer based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("secondary", 1),
          ("primary", 2))
    )


_ZxAnEponRmVoipSipActiveProxyServer_Type.__name__ = "Integer32"
_ZxAnEponRmVoipSipActiveProxyServer_Object = MibTableColumn
zxAnEponRmVoipSipActiveProxyServer = _ZxAnEponRmVoipSipActiveProxyServer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 13, 1, 1),
    _ZxAnEponRmVoipSipActiveProxyServer_Type()
)
zxAnEponRmVoipSipActiveProxyServer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipActiveProxyServer.setStatus("current")
_ZxAnEponRmVoipSipDigitMapTable_Object = MibTable
zxAnEponRmVoipSipDigitMapTable = _ZxAnEponRmVoipSipDigitMapTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 14)
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipDigitMapTable.setStatus("current")
_ZxAnEponRmVoipSipDigitMapEntry_Object = MibTableRow
zxAnEponRmVoipSipDigitMapEntry = _ZxAnEponRmVoipSipDigitMapEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 14, 1)
)
zxAnEponRmVoipSipDigitMapEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmVoipSipDigitMapEntry.setStatus("current")


class _ZxEponRmVoipSipDigitMap_Type(DisplayString):
    """Custom type zxEponRmVoipSipDigitMap based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1024),
    )


_ZxEponRmVoipSipDigitMap_Type.__name__ = "DisplayString"
_ZxEponRmVoipSipDigitMap_Object = MibTableColumn
zxEponRmVoipSipDigitMap = _ZxEponRmVoipSipDigitMap_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 14, 1, 1),
    _ZxEponRmVoipSipDigitMap_Type()
)
zxEponRmVoipSipDigitMap.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponRmVoipSipDigitMap.setStatus("current")
_ZxAnEponOnuVoipPresentingTable_Object = MibTable
zxAnEponOnuVoipPresentingTable = _ZxAnEponOnuVoipPresentingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 15)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVoipPresentingTable.setStatus("current")
_ZxAnEponOnuVoipPresentingEntry_Object = MibTableRow
zxAnEponOnuVoipPresentingEntry = _ZxAnEponOnuVoipPresentingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 15, 1)
)
zxAnEponOnuVoipPresentingEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVoipPresentingEntry.setStatus("current")


class _ZxAnEponOnuVoipPresentingCallNbrState_Type(Integer32):
    """Custom type zxAnEponOnuVoipPresentingCallNbrState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuVoipPresentingCallNbrState_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipPresentingCallNbrState_Object = MibTableColumn
zxAnEponOnuVoipPresentingCallNbrState = _ZxAnEponOnuVoipPresentingCallNbrState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 15, 1, 1),
    _ZxAnEponOnuVoipPresentingCallNbrState_Type()
)
zxAnEponOnuVoipPresentingCallNbrState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipPresentingCallNbrState.setStatus("current")


class _ZxAnEponOnuVoipPresentingCallNbrType_Type(Integer32):
    """Custom type zxAnEponOnuVoipPresentingCallNbrType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("fsk", 1),
          ("dtmf", 2))
    )


_ZxAnEponOnuVoipPresentingCallNbrType_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipPresentingCallNbrType_Object = MibTableColumn
zxAnEponOnuVoipPresentingCallNbrType = _ZxAnEponOnuVoipPresentingCallNbrType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 15, 1, 2),
    _ZxAnEponOnuVoipPresentingCallNbrType_Type()
)
zxAnEponOnuVoipPresentingCallNbrType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipPresentingCallNbrType.setStatus("current")
_ZxAnEponOnuVoipTimerConfigTable_Object = MibTable
zxAnEponOnuVoipTimerConfigTable = _ZxAnEponOnuVoipTimerConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 16)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVoipTimerConfigTable.setStatus("current")
_ZxAnEponOnuVoipTimerConfigEntry_Object = MibTableRow
zxAnEponOnuVoipTimerConfigEntry = _ZxAnEponOnuVoipTimerConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 16, 1)
)
zxAnEponOnuVoipTimerConfigEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVoipTimerConfigEntry.setStatus("current")


class _ZxAnEponOnuVoipTimerConfigDml_Type(Integer32):
    """Custom type zxAnEponOnuVoipTimerConfigDml based on Integer32"""
    defaultValue = 5

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxAnEponOnuVoipTimerConfigDml_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipTimerConfigDml_Object = MibTableColumn
zxAnEponOnuVoipTimerConfigDml = _ZxAnEponOnuVoipTimerConfigDml_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 16, 1, 1),
    _ZxAnEponOnuVoipTimerConfigDml_Type()
)
zxAnEponOnuVoipTimerConfigDml.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipTimerConfigDml.setStatus("current")


class _ZxAnEponOnuVoipTimerConfigDms_Type(Integer32):
    """Custom type zxAnEponOnuVoipTimerConfigDms based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 60),
    )


_ZxAnEponOnuVoipTimerConfigDms_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipTimerConfigDms_Object = MibTableColumn
zxAnEponOnuVoipTimerConfigDms = _ZxAnEponOnuVoipTimerConfigDms_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 16, 1, 2),
    _ZxAnEponOnuVoipTimerConfigDms_Type()
)
zxAnEponOnuVoipTimerConfigDms.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipTimerConfigDms.setStatus("current")
_ZxAnEponOnuVoipStatsTable_Object = MibTable
zxAnEponOnuVoipStatsTable = _ZxAnEponOnuVoipStatsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVoipStatsTable.setStatus("current")
_ZxAnEponOnuVoipStatsEntry_Object = MibTableRow
zxAnEponOnuVoipStatsEntry = _ZxAnEponOnuVoipStatsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1)
)
zxAnEponOnuVoipStatsEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVoipStatsEntry.setStatus("current")
_ZxAnEponOnuVoipRxPkts_Type = Counter64
_ZxAnEponOnuVoipRxPkts_Object = MibTableColumn
zxAnEponOnuVoipRxPkts = _ZxAnEponOnuVoipRxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1, 1),
    _ZxAnEponOnuVoipRxPkts_Type()
)
zxAnEponOnuVoipRxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipRxPkts.setStatus("current")
_ZxAnEponOnuVoipTxPkts_Type = Counter64
_ZxAnEponOnuVoipTxPkts_Object = MibTableColumn
zxAnEponOnuVoipTxPkts = _ZxAnEponOnuVoipTxPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1, 2),
    _ZxAnEponOnuVoipTxPkts_Type()
)
zxAnEponOnuVoipTxPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipTxPkts.setStatus("current")


class _ZxAnEponOnuVoipAverageDelay_Type(Integer32):
    """Custom type zxAnEponOnuVoipAverageDelay based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEponOnuVoipAverageDelay_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipAverageDelay_Object = MibTableColumn
zxAnEponOnuVoipAverageDelay = _ZxAnEponOnuVoipAverageDelay_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1, 3),
    _ZxAnEponOnuVoipAverageDelay_Type()
)
zxAnEponOnuVoipAverageDelay.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipAverageDelay.setStatus("current")


class _ZxAnEponOnuVoipAverageJitter_Type(Integer32):
    """Custom type zxAnEponOnuVoipAverageJitter based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEponOnuVoipAverageJitter_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipAverageJitter_Object = MibTableColumn
zxAnEponOnuVoipAverageJitter = _ZxAnEponOnuVoipAverageJitter_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1, 4),
    _ZxAnEponOnuVoipAverageJitter_Type()
)
zxAnEponOnuVoipAverageJitter.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipAverageJitter.setStatus("current")


class _ZxAnEponOnuVoipLoss_Type(Integer32):
    """Custom type zxAnEponOnuVoipLoss based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuVoipLoss_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipLoss_Object = MibTableColumn
zxAnEponOnuVoipLoss = _ZxAnEponOnuVoipLoss_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1, 5),
    _ZxAnEponOnuVoipLoss_Type()
)
zxAnEponOnuVoipLoss.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipLoss.setStatus("current")
_ZxAnEponRmUniVoipRxMediaDataRate_Type = Gauge32
_ZxAnEponRmUniVoipRxMediaDataRate_Object = MibTableColumn
zxAnEponRmUniVoipRxMediaDataRate = _ZxAnEponRmUniVoipRxMediaDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1, 6),
    _ZxAnEponRmUniVoipRxMediaDataRate_Type()
)
zxAnEponRmUniVoipRxMediaDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmUniVoipRxMediaDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponRmUniVoipRxMediaDataRate.setUnits("kbps")
_ZxAnEponRmUniVoipTxMediaDataRate_Type = Gauge32
_ZxAnEponRmUniVoipTxMediaDataRate_Object = MibTableColumn
zxAnEponRmUniVoipTxMediaDataRate = _ZxAnEponRmUniVoipTxMediaDataRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1, 7),
    _ZxAnEponRmUniVoipTxMediaDataRate_Type()
)
zxAnEponRmUniVoipTxMediaDataRate.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmUniVoipTxMediaDataRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponRmUniVoipTxMediaDataRate.setUnits("kbps")
_ZxAnEponRmUniVoipCurCallDuration_Type = Unsigned32
_ZxAnEponRmUniVoipCurCallDuration_Object = MibTableColumn
zxAnEponRmUniVoipCurCallDuration = _ZxAnEponRmUniVoipCurCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1, 8),
    _ZxAnEponRmUniVoipCurCallDuration_Type()
)
zxAnEponRmUniVoipCurCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmUniVoipCurCallDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponRmUniVoipCurCallDuration.setUnits("Seconds")
_ZxAnEponRmUniVoipTotCallDuration_Type = Unsigned32
_ZxAnEponRmUniVoipTotCallDuration_Object = MibTableColumn
zxAnEponRmUniVoipTotCallDuration = _ZxAnEponRmUniVoipTotCallDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1, 9),
    _ZxAnEponRmUniVoipTotCallDuration_Type()
)
zxAnEponRmUniVoipTotCallDuration.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmUniVoipTotCallDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponRmUniVoipTotCallDuration.setUnits("Seconds")
_ZxAnEponRmUniVoipCallTimes_Type = Unsigned32
_ZxAnEponRmUniVoipCallTimes_Object = MibTableColumn
zxAnEponRmUniVoipCallTimes = _ZxAnEponRmUniVoipCallTimes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 17, 1, 10),
    _ZxAnEponRmUniVoipCallTimes_Type()
)
zxAnEponRmUniVoipCallTimes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmUniVoipCallTimes.setStatus("current")
_ZxAnEponOnuVoipOtherConfigTable_Object = MibTable
zxAnEponOnuVoipOtherConfigTable = _ZxAnEponOnuVoipOtherConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 18)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVoipOtherConfigTable.setStatus("current")
_ZxAnEponOnuVoipOtherConfigEntry_Object = MibTableRow
zxAnEponOnuVoipOtherConfigEntry = _ZxAnEponOnuVoipOtherConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 18, 1)
)
zxAnEponOnuVoipOtherConfigEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVoipOtherConfigEntry.setStatus("current")


class _ZxAnEponOnuVoipComfortableNoise_Type(Integer32):
    """Custom type zxAnEponOnuVoipComfortableNoise based on Integer32"""
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


_ZxAnEponOnuVoipComfortableNoise_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipComfortableNoise_Object = MibTableColumn
zxAnEponOnuVoipComfortableNoise = _ZxAnEponOnuVoipComfortableNoise_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 18, 1, 1),
    _ZxAnEponOnuVoipComfortableNoise_Type()
)
zxAnEponOnuVoipComfortableNoise.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipComfortableNoise.setStatus("current")


class _ZxAnEponOnuVoipSilenceDetection_Type(Integer32):
    """Custom type zxAnEponOnuVoipSilenceDetection based on Integer32"""
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


_ZxAnEponOnuVoipSilenceDetection_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipSilenceDetection_Object = MibTableColumn
zxAnEponOnuVoipSilenceDetection = _ZxAnEponOnuVoipSilenceDetection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 18, 1, 2),
    _ZxAnEponOnuVoipSilenceDetection_Type()
)
zxAnEponOnuVoipSilenceDetection.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipSilenceDetection.setStatus("current")


class _ZxAnEponOnuVoipEchoCanceller_Type(Integer32):
    """Custom type zxAnEponOnuVoipEchoCanceller based on Integer32"""
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


_ZxAnEponOnuVoipEchoCanceller_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipEchoCanceller_Object = MibTableColumn
zxAnEponOnuVoipEchoCanceller = _ZxAnEponOnuVoipEchoCanceller_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 18, 1, 3),
    _ZxAnEponOnuVoipEchoCanceller_Type()
)
zxAnEponOnuVoipEchoCanceller.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipEchoCanceller.setStatus("current")


class _ZxAnEponOnuVoipDtmpTransferMode_Type(Integer32):
    """Custom type zxAnEponOnuVoipDtmpTransferMode based on Integer32"""
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
        *(("voiceCoding", 1),
          ("nredRfc2833", 2),
          ("redRfc2833", 3),
          ("aal2OrIetf", 4),
          ("noForwarding", 5))
    )


_ZxAnEponOnuVoipDtmpTransferMode_Type.__name__ = "Integer32"
_ZxAnEponOnuVoipDtmpTransferMode_Object = MibTableColumn
zxAnEponOnuVoipDtmpTransferMode = _ZxAnEponOnuVoipDtmpTransferMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 18, 1, 4),
    _ZxAnEponOnuVoipDtmpTransferMode_Type()
)
zxAnEponOnuVoipDtmpTransferMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVoipDtmpTransferMode.setStatus("current")
_ZxAnEponRmOnuVoipSrvPerfTable_Object = MibTable
zxAnEponRmOnuVoipSrvPerfTable = _ZxAnEponRmOnuVoipSrvPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 19)
)
if mibBuilder.loadTexts:
    zxAnEponRmOnuVoipSrvPerfTable.setStatus("current")
_ZxAnEponRmOnuVoipSrvPerfEntry_Object = MibTableRow
zxAnEponRmOnuVoipSrvPerfEntry = _ZxAnEponRmOnuVoipSrvPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 19, 1)
)
zxAnEponRmOnuVoipSrvPerfEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmOnuVoipSrvPerfEntry.setStatus("current")
_ZxAnEponRmOnuVoipRxSignalMsg_Type = Counter64
_ZxAnEponRmOnuVoipRxSignalMsg_Object = MibTableColumn
zxAnEponRmOnuVoipRxSignalMsg = _ZxAnEponRmOnuVoipRxSignalMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 19, 1, 1),
    _ZxAnEponRmOnuVoipRxSignalMsg_Type()
)
zxAnEponRmOnuVoipRxSignalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmOnuVoipRxSignalMsg.setStatus("current")
_ZxAnEponRmOnuVoipTxSignalMsg_Type = Counter64
_ZxAnEponRmOnuVoipTxSignalMsg_Object = MibTableColumn
zxAnEponRmOnuVoipTxSignalMsg = _ZxAnEponRmOnuVoipTxSignalMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 19, 1, 2),
    _ZxAnEponRmOnuVoipTxSignalMsg_Type()
)
zxAnEponRmOnuVoipTxSignalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmOnuVoipTxSignalMsg.setStatus("current")
_ZxAnEponRmOnuVoipLossSignalMsg_Type = Counter32
_ZxAnEponRmOnuVoipLossSignalMsg_Object = MibTableColumn
zxAnEponRmOnuVoipLossSignalMsg = _ZxAnEponRmOnuVoipLossSignalMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 19, 1, 3),
    _ZxAnEponRmOnuVoipLossSignalMsg_Type()
)
zxAnEponRmOnuVoipLossSignalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmOnuVoipLossSignalMsg.setStatus("current")
_ZxAnEponRmOnuVoipReTxSignalMsg_Type = Counter32
_ZxAnEponRmOnuVoipReTxSignalMsg_Object = MibTableColumn
zxAnEponRmOnuVoipReTxSignalMsg = _ZxAnEponRmOnuVoipReTxSignalMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 19, 1, 4),
    _ZxAnEponRmOnuVoipReTxSignalMsg_Type()
)
zxAnEponRmOnuVoipReTxSignalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmOnuVoipReTxSignalMsg.setStatus("current")
_ZxAnEponRmOnuVoipErrSignalMsg_Type = Counter32
_ZxAnEponRmOnuVoipErrSignalMsg_Object = MibTableColumn
zxAnEponRmOnuVoipErrSignalMsg = _ZxAnEponRmOnuVoipErrSignalMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 19, 1, 5),
    _ZxAnEponRmOnuVoipErrSignalMsg_Type()
)
zxAnEponRmOnuVoipErrSignalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmOnuVoipErrSignalMsg.setStatus("current")
_ZxAnEponRmOnuVoipUnknowSignalMsg_Type = Counter32
_ZxAnEponRmOnuVoipUnknowSignalMsg_Object = MibTableColumn
zxAnEponRmOnuVoipUnknowSignalMsg = _ZxAnEponRmOnuVoipUnknowSignalMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 36, 19, 1, 6),
    _ZxAnEponRmOnuVoipUnknowSignalMsg_Type()
)
zxAnEponRmOnuVoipUnknowSignalMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmOnuVoipUnknowSignalMsg.setStatus("current")
_ZxAnEponOnuCapabilityExtTable_Object = MibTable
zxAnEponOnuCapabilityExtTable = _ZxAnEponOnuCapabilityExtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37)
)
if mibBuilder.loadTexts:
    zxAnEponOnuCapabilityExtTable.setStatus("current")
_ZxAnEponOnuCapabilityExtEntry_Object = MibTableRow
zxAnEponOnuCapabilityExtEntry = _ZxAnEponOnuCapabilityExtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37, 1)
)
zxAnEponOnuCapabilityExtEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuCapabilityExtEntry.setStatus("current")


class _ZxAnEponOnuType_Type(Integer32):
    """Custom type zxAnEponOnuType based on Integer32"""
    defaultValue = 1

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
        *(("sfu", 1),
          ("hgu", 2),
          ("sbu", 3),
          ("ethMduCompactBox", 4),
          ("ethMduCards", 5),
          ("dslMduCardsCompactBox", 6),
          ("dslMduCardsRack", 7),
          ("bybridMduCards", 8),
          ("mtu", 9))
    )


_ZxAnEponOnuType_Type.__name__ = "Integer32"
_ZxAnEponOnuType_Object = MibTableColumn
zxAnEponOnuType = _ZxAnEponOnuType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37, 1, 1),
    _ZxAnEponOnuType_Type()
)
zxAnEponOnuType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuType.setStatus("current")


class _ZxAnEponOnuMultiLlid_Type(Integer32):
    """Custom type zxAnEponOnuMultiLlid based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 8),
    )


_ZxAnEponOnuMultiLlid_Type.__name__ = "Integer32"
_ZxAnEponOnuMultiLlid_Object = MibTableColumn
zxAnEponOnuMultiLlid = _ZxAnEponOnuMultiLlid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37, 1, 2),
    _ZxAnEponOnuMultiLlid_Type()
)
zxAnEponOnuMultiLlid.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuMultiLlid.setStatus("current")


class _ZxAnEponOnuProtection_Type(Integer32):
    """Custom type zxAnEponOnuProtection based on Integer32"""
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
        *(("notSupport", 1),
          ("typeC", 2),
          ("typeD", 3))
    )


_ZxAnEponOnuProtection_Type.__name__ = "Integer32"
_ZxAnEponOnuProtection_Object = MibTableColumn
zxAnEponOnuProtection = _ZxAnEponOnuProtection_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37, 1, 3),
    _ZxAnEponOnuProtection_Type()
)
zxAnEponOnuProtection.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuProtection.setStatus("current")
_ZxAnEponOnuPonPorts_Type = Integer32
_ZxAnEponOnuPonPorts_Object = MibTableColumn
zxAnEponOnuPonPorts = _ZxAnEponOnuPonPorts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37, 1, 4),
    _ZxAnEponOnuPonPorts_Type()
)
zxAnEponOnuPonPorts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPonPorts.setStatus("current")
_ZxAnEponOnuSlots_Type = Integer32
_ZxAnEponOnuSlots_Object = MibTableColumn
zxAnEponOnuSlots = _ZxAnEponOnuSlots_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37, 1, 5),
    _ZxAnEponOnuSlots_Type()
)
zxAnEponOnuSlots.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuSlots.setStatus("current")


class _ZxAnEponOnuBatteryBackupStatus_Type(Integer32):
    """Custom type zxAnEponOnuBatteryBackupStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("noBatteryBackup", 1),
          ("batteryBackup", 2))
    )


_ZxAnEponOnuBatteryBackupStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuBatteryBackupStatus_Object = MibTableColumn
zxAnEponOnuBatteryBackupStatus = _ZxAnEponOnuBatteryBackupStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37, 1, 6),
    _ZxAnEponOnuBatteryBackupStatus_Type()
)
zxAnEponOnuBatteryBackupStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuBatteryBackupStatus.setStatus("current")


class _ZxAnEponOnuIsSupportIpv6_Type(Integer32):
    """Custom type zxAnEponOnuIsSupportIpv6 based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_ZxAnEponOnuIsSupportIpv6_Type.__name__ = "Integer32"
_ZxAnEponOnuIsSupportIpv6_Object = MibTableColumn
zxAnEponOnuIsSupportIpv6 = _ZxAnEponOnuIsSupportIpv6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37, 1, 7),
    _ZxAnEponOnuIsSupportIpv6_Type()
)
zxAnEponOnuIsSupportIpv6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuIsSupportIpv6.setStatus("current")


class _ZxAnEponOnuPwrSdSupportMode_Type(Integer32):
    """Custom type zxAnEponOnuPwrSdSupportMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unsupported", 1),
          ("supportTx", 2),
          ("supportTrx", 3))
    )


_ZxAnEponOnuPwrSdSupportMode_Type.__name__ = "Integer32"
_ZxAnEponOnuPwrSdSupportMode_Object = MibTableColumn
zxAnEponOnuPwrSdSupportMode = _ZxAnEponOnuPwrSdSupportMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37, 1, 8),
    _ZxAnEponOnuPwrSdSupportMode_Type()
)
zxAnEponOnuPwrSdSupportMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSdSupportMode.setStatus("current")


class _ZxAnEponOnuSlaNumber_Type(Integer32):
    """Custom type zxAnEponOnuSlaNumber based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnEponOnuSlaNumber_Type.__name__ = "Integer32"
_ZxAnEponOnuSlaNumber_Object = MibTableColumn
zxAnEponOnuSlaNumber = _ZxAnEponOnuSlaNumber_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 37, 1, 9),
    _ZxAnEponOnuSlaNumber_Type()
)
zxAnEponOnuSlaNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuSlaNumber.setStatus("current")
_ZxAnEponOnuInterfaceTable_Object = MibTable
zxAnEponOnuInterfaceTable = _ZxAnEponOnuInterfaceTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 38)
)
if mibBuilder.loadTexts:
    zxAnEponOnuInterfaceTable.setStatus("current")
_ZxAnEponOnuInterfaceEntry_Object = MibTableRow
zxAnEponOnuInterfaceEntry = _ZxAnEponOnuInterfaceEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 38, 1)
)
zxAnEponOnuInterfaceEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuInterfaceType"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuInterfaceEntry.setStatus("current")


class _ZxAnEponOnuInterfaceType_Type(Integer32):
    """Custom type zxAnEponOnuInterfaceType based on Integer32"""
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
        *(("ge", 1),
          ("fe", 2),
          ("voip", 3),
          ("tdm", 4),
          ("adsl2Plus", 5),
          ("vdsl2", 6),
          ("wlan", 7),
          ("usb", 8),
          ("catvRf", 9))
    )


_ZxAnEponOnuInterfaceType_Type.__name__ = "Integer32"
_ZxAnEponOnuInterfaceType_Object = MibTableColumn
zxAnEponOnuInterfaceType = _ZxAnEponOnuInterfaceType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 38, 1, 1),
    _ZxAnEponOnuInterfaceType_Type()
)
zxAnEponOnuInterfaceType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuInterfaceType.setStatus("current")
_ZxAnEponOnuInterfaceNum_Type = Integer32
_ZxAnEponOnuInterfaceNum_Object = MibTableColumn
zxAnEponOnuInterfaceNum = _ZxAnEponOnuInterfaceNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 38, 1, 2),
    _ZxAnEponOnuInterfaceNum_Type()
)
zxAnEponOnuInterfaceNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuInterfaceNum.setStatus("current")
_ZxAnEponMduCardTable_Object = MibTable
zxAnEponMduCardTable = _ZxAnEponMduCardTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 39)
)
if mibBuilder.loadTexts:
    zxAnEponMduCardTable.setStatus("current")
_ZxAnEponMduCardEntry_Object = MibTableRow
zxAnEponMduCardEntry = _ZxAnEponMduCardEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 39, 1)
)
zxAnEponMduCardEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuCardIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponMduCardEntry.setStatus("current")


class _ZxAnEponMduCardOperStatus_Type(Integer32):
    """Custom type zxAnEponMduCardOperStatus based on Integer32"""
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
              10)
        )
    )
    namedValues = NamedValues(
        *(("inService", 1),
          ("notInService", 2),
          ("hwOnline", 3),
          ("hwOffline", 4),
          ("configuring", 5),
          ("configFailed", 6),
          ("typeMismatch", 7),
          ("deactived", 8),
          ("faulty", 9),
          ("invalid", 10))
    )


_ZxAnEponMduCardOperStatus_Type.__name__ = "Integer32"
_ZxAnEponMduCardOperStatus_Object = MibTableColumn
zxAnEponMduCardOperStatus = _ZxAnEponMduCardOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 39, 1, 1),
    _ZxAnEponMduCardOperStatus_Type()
)
zxAnEponMduCardOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponMduCardOperStatus.setStatus("current")


class _ZxAnEponMduCardAdminStatus_Type(Integer32):
    """Custom type zxAnEponMduCardAdminStatus based on Integer32"""
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
        *(("reset", 1),
          ("switch", 2),
          ("stopService", 3),
          ("active", 4),
          ("deactive", 5))
    )


_ZxAnEponMduCardAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponMduCardAdminStatus_Object = MibTableColumn
zxAnEponMduCardAdminStatus = _ZxAnEponMduCardAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 39, 1, 2),
    _ZxAnEponMduCardAdminStatus_Type()
)
zxAnEponMduCardAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponMduCardAdminStatus.setStatus("current")
_ZxAnEponMduSnmpParamMgmt_ObjectIdentity = ObjectIdentity
zxAnEponMduSnmpParamMgmt = _ZxAnEponMduSnmpParamMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40)
)
_ZxAnEponMduSnmpParamTable_Object = MibTable
zxAnEponMduSnmpParamTable = _ZxAnEponMduSnmpParamTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 1)
)
if mibBuilder.loadTexts:
    zxAnEponMduSnmpParamTable.setStatus("current")
_ZxAnEponMduSnmpParamEntry_Object = MibTableRow
zxAnEponMduSnmpParamEntry = _ZxAnEponMduSnmpParamEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 1, 1)
)
zxAnEponMduSnmpParamEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponMduSnmpParamEntry.setStatus("current")


class _ZxEponMduSnmpVersion_Type(Integer32):
    """Custom type zxEponMduSnmpVersion based on Integer32"""
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
        *(("snmpV1", 1),
          ("snmpV2c", 2),
          ("snmpV3", 3))
    )


_ZxEponMduSnmpVersion_Type.__name__ = "Integer32"
_ZxEponMduSnmpVersion_Object = MibTableColumn
zxEponMduSnmpVersion = _ZxEponMduSnmpVersion_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 1, 1, 1),
    _ZxEponMduSnmpVersion_Type()
)
zxEponMduSnmpVersion.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpVersion.setStatus("current")


class _ZxEponMduSnmpServicePort_Type(Integer32):
    """Custom type zxEponMduSnmpServicePort based on Integer32"""
    defaultValue = 161

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxEponMduSnmpServicePort_Type.__name__ = "Integer32"
_ZxEponMduSnmpServicePort_Object = MibTableColumn
zxEponMduSnmpServicePort = _ZxEponMduSnmpServicePort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 1, 1, 2),
    _ZxEponMduSnmpServicePort_Type()
)
zxEponMduSnmpServicePort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpServicePort.setStatus("current")


class _ZxEponMduSnmpTrapPort_Type(Integer32):
    """Custom type zxEponMduSnmpTrapPort based on Integer32"""
    defaultValue = 162

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxEponMduSnmpTrapPort_Type.__name__ = "Integer32"
_ZxEponMduSnmpTrapPort_Object = MibTableColumn
zxEponMduSnmpTrapPort = _ZxEponMduSnmpTrapPort_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 1, 1, 3),
    _ZxEponMduSnmpTrapPort_Type()
)
zxEponMduSnmpTrapPort.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpTrapPort.setStatus("current")


class _ZxEponMduSnmpReadCommunity_Type(DisplayString):
    """Custom type zxEponMduSnmpReadCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxEponMduSnmpReadCommunity_Type.__name__ = "DisplayString"
_ZxEponMduSnmpReadCommunity_Object = MibTableColumn
zxEponMduSnmpReadCommunity = _ZxEponMduSnmpReadCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 1, 1, 4),
    _ZxEponMduSnmpReadCommunity_Type()
)
zxEponMduSnmpReadCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpReadCommunity.setStatus("current")


class _ZxEponMduSnmpWriteCommunity_Type(DisplayString):
    """Custom type zxEponMduSnmpWriteCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxEponMduSnmpWriteCommunity_Type.__name__ = "DisplayString"
_ZxEponMduSnmpWriteCommunity_Object = MibTableColumn
zxEponMduSnmpWriteCommunity = _ZxEponMduSnmpWriteCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 1, 1, 5),
    _ZxEponMduSnmpWriteCommunity_Type()
)
zxEponMduSnmpWriteCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpWriteCommunity.setStatus("current")
_ZxEponMduSnmpTrapHostTable_Object = MibTable
zxEponMduSnmpTrapHostTable = _ZxEponMduSnmpTrapHostTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 2)
)
if mibBuilder.loadTexts:
    zxEponMduSnmpTrapHostTable.setStatus("current")
_ZxEponMduSnmpTrapHostEntry_Object = MibTableRow
zxEponMduSnmpTrapHostEntry = _ZxEponMduSnmpTrapHostEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 2, 1)
)
zxEponMduSnmpTrapHostEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxEponMduSnmpTrapHostIndex"),
)
if mibBuilder.loadTexts:
    zxEponMduSnmpTrapHostEntry.setStatus("current")


class _ZxEponMduSnmpTrapHostIndex_Type(Integer32):
    """Custom type zxEponMduSnmpTrapHostIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxEponMduSnmpTrapHostIndex_Type.__name__ = "Integer32"
_ZxEponMduSnmpTrapHostIndex_Object = MibTableColumn
zxEponMduSnmpTrapHostIndex = _ZxEponMduSnmpTrapHostIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 2, 1, 1),
    _ZxEponMduSnmpTrapHostIndex_Type()
)
zxEponMduSnmpTrapHostIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxEponMduSnmpTrapHostIndex.setStatus("current")
_ZxEponMduSnmpTrapHostIpAddr_Type = IpAddress
_ZxEponMduSnmpTrapHostIpAddr_Object = MibTableColumn
zxEponMduSnmpTrapHostIpAddr = _ZxEponMduSnmpTrapHostIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 2, 1, 2),
    _ZxEponMduSnmpTrapHostIpAddr_Type()
)
zxEponMduSnmpTrapHostIpAddr.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpTrapHostIpAddr.setStatus("current")


class _ZxEponMduSnmpTrapHostSnmpVer_Type(Integer32):
    """Custom type zxEponMduSnmpTrapHostSnmpVer based on Integer32"""
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
        *(("snmpV1", 1),
          ("snmpV2c", 2),
          ("snmpV3", 3))
    )


_ZxEponMduSnmpTrapHostSnmpVer_Type.__name__ = "Integer32"
_ZxEponMduSnmpTrapHostSnmpVer_Object = MibTableColumn
zxEponMduSnmpTrapHostSnmpVer = _ZxEponMduSnmpTrapHostSnmpVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 2, 1, 3),
    _ZxEponMduSnmpTrapHostSnmpVer_Type()
)
zxEponMduSnmpTrapHostSnmpVer.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpTrapHostSnmpVer.setStatus("current")


class _ZxEponMduSnmpTrapHostCommunity_Type(DisplayString):
    """Custom type zxEponMduSnmpTrapHostCommunity based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxEponMduSnmpTrapHostCommunity_Type.__name__ = "DisplayString"
_ZxEponMduSnmpTrapHostCommunity_Object = MibTableColumn
zxEponMduSnmpTrapHostCommunity = _ZxEponMduSnmpTrapHostCommunity_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 2, 1, 4),
    _ZxEponMduSnmpTrapHostCommunity_Type()
)
zxEponMduSnmpTrapHostCommunity.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpTrapHostCommunity.setStatus("current")


class _ZxEponMduSnmpTrapHostMinEventLevel_Type(Integer32):
    """Custom type zxEponMduSnmpTrapHostMinEventLevel based on Integer32"""
    defaultValue = 6

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2,
              3,
              4,
              5,
              6)
        )
    )
    namedValues = NamedValues(
        *(("critical", 0),
          ("major", 1),
          ("minor", 2),
          ("warning", 3),
          ("indeterminate", 4),
          ("cleared", 5),
          ("notification", 6))
    )


_ZxEponMduSnmpTrapHostMinEventLevel_Type.__name__ = "Integer32"
_ZxEponMduSnmpTrapHostMinEventLevel_Object = MibTableColumn
zxEponMduSnmpTrapHostMinEventLevel = _ZxEponMduSnmpTrapHostMinEventLevel_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 2, 1, 5),
    _ZxEponMduSnmpTrapHostMinEventLevel_Type()
)
zxEponMduSnmpTrapHostMinEventLevel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpTrapHostMinEventLevel.setStatus("current")


class _ZxEponMduSnmpTrapHostEnable_Type(Integer32):
    """Custom type zxEponMduSnmpTrapHostEnable based on Integer32"""
    defaultValue = 1

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


_ZxEponMduSnmpTrapHostEnable_Type.__name__ = "Integer32"
_ZxEponMduSnmpTrapHostEnable_Object = MibTableColumn
zxEponMduSnmpTrapHostEnable = _ZxEponMduSnmpTrapHostEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 2, 1, 6),
    _ZxEponMduSnmpTrapHostEnable_Type()
)
zxEponMduSnmpTrapHostEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpTrapHostEnable.setStatus("current")
_ZxEponMduSnmpTrapHostRowStatus_Type = RowStatus
_ZxEponMduSnmpTrapHostRowStatus_Object = MibTableColumn
zxEponMduSnmpTrapHostRowStatus = _ZxEponMduSnmpTrapHostRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 40, 2, 1, 7),
    _ZxEponMduSnmpTrapHostRowStatus_Type()
)
zxEponMduSnmpTrapHostRowStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponMduSnmpTrapHostRowStatus.setStatus("current")
_ZxAnEponOnuMVlanSwitchTable_Object = MibTable
zxAnEponOnuMVlanSwitchTable = _ZxAnEponOnuMVlanSwitchTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 41)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMVlanSwitchTable.setStatus("current")
_ZxAnEponOnuMVlanSwitchEntry_Object = MibTableRow
zxAnEponOnuMVlanSwitchEntry = _ZxAnEponOnuMVlanSwitchEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 41, 1)
)
zxAnEponOnuMVlanSwitchEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuMVlan"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIptvUserVlan"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMVlanSwitchEntry.setStatus("current")


class _ZxAnEponOnuMVlan_Type(Integer32):
    """Custom type zxAnEponOnuMVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponOnuMVlan_Type.__name__ = "Integer32"
_ZxAnEponOnuMVlan_Object = MibTableColumn
zxAnEponOnuMVlan = _ZxAnEponOnuMVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 41, 1, 1),
    _ZxAnEponOnuMVlan_Type()
)
zxAnEponOnuMVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuMVlan.setStatus("current")


class _ZxAnEponOnuIptvUserVlan_Type(Integer32):
    """Custom type zxAnEponOnuIptvUserVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponOnuIptvUserVlan_Type.__name__ = "Integer32"
_ZxAnEponOnuIptvUserVlan_Object = MibTableColumn
zxAnEponOnuIptvUserVlan = _ZxAnEponOnuIptvUserVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 41, 1, 2),
    _ZxAnEponOnuIptvUserVlan_Type()
)
zxAnEponOnuIptvUserVlan.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuIptvUserVlan.setStatus("current")
_ZxAnEponOnuMVlanSwitchRowStatus_Type = RowStatus
_ZxAnEponOnuMVlanSwitchRowStatus_Object = MibTableColumn
zxAnEponOnuMVlanSwitchRowStatus = _ZxAnEponOnuMVlanSwitchRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 41, 1, 10),
    _ZxAnEponOnuMVlanSwitchRowStatus_Type()
)
zxAnEponOnuMVlanSwitchRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuMVlanSwitchRowStatus.setStatus("current")
_ZxAnEponOnuPortTable_Object = MibTable
zxAnEponOnuPortTable = _ZxAnEponOnuPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 42)
)
if mibBuilder.loadTexts:
    zxAnEponOnuPortTable.setStatus("current")
_ZxAnEponOnuPortEntry_Object = MibTableRow
zxAnEponOnuPortEntry = _ZxAnEponOnuPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 42, 1)
)
zxAnEponOnuPortEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuPortEntry.setStatus("current")


class _ZxAnEponOnuPortLoopbackDetectStatus_Type(Integer32):
    """Custom type zxAnEponOnuPortLoopbackDetectStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuPortLoopbackDetectStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuPortLoopbackDetectStatus_Object = MibTableColumn
zxAnEponOnuPortLoopbackDetectStatus = _ZxAnEponOnuPortLoopbackDetectStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 42, 1, 1),
    _ZxAnEponOnuPortLoopbackDetectStatus_Type()
)
zxAnEponOnuPortLoopbackDetectStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortLoopbackDetectStatus.setStatus("current")


class _ZxAnEponOnuPortLoopbackAutoSdEn_Type(Integer32):
    """Custom type zxAnEponOnuPortLoopbackAutoSdEn based on Integer32"""
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


_ZxAnEponOnuPortLoopbackAutoSdEn_Type.__name__ = "Integer32"
_ZxAnEponOnuPortLoopbackAutoSdEn_Object = MibTableColumn
zxAnEponOnuPortLoopbackAutoSdEn = _ZxAnEponOnuPortLoopbackAutoSdEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 42, 1, 2),
    _ZxAnEponOnuPortLoopbackAutoSdEn_Type()
)
zxAnEponOnuPortLoopbackAutoSdEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPortLoopbackAutoSdEn.setStatus("current")
_ZxAnEponOnuLlidQueueTable_Object = MibTable
zxAnEponOnuLlidQueueTable = _ZxAnEponOnuLlidQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43)
)
if mibBuilder.loadTexts:
    zxAnEponOnuLlidQueueTable.setStatus("current")
_ZxAnEponOnuLlidQueueEntry_Object = MibTableRow
zxAnEponOnuLlidQueueEntry = _ZxAnEponOnuLlidQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43, 1)
)
zxAnEponOnuLlidQueueEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuLlid"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuLlidQueueEntry.setStatus("current")
_ZxAnEponOnuLlid_Type = Integer32
_ZxAnEponOnuLlid_Object = MibTableColumn
zxAnEponOnuLlid = _ZxAnEponOnuLlid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43, 1, 1),
    _ZxAnEponOnuLlid_Type()
)
zxAnEponOnuLlid.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuLlid.setStatus("current")


class _ZxAnEponOnuLlidQueue1WrrWeight_Type(Integer32):
    """Custom type zxAnEponOnuLlidQueue1WrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuLlidQueue1WrrWeight_Type.__name__ = "Integer32"
_ZxAnEponOnuLlidQueue1WrrWeight_Object = MibTableColumn
zxAnEponOnuLlidQueue1WrrWeight = _ZxAnEponOnuLlidQueue1WrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43, 1, 2),
    _ZxAnEponOnuLlidQueue1WrrWeight_Type()
)
zxAnEponOnuLlidQueue1WrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidQueue1WrrWeight.setStatus("current")


class _ZxAnEponOnuLlidQueue2WrrWeight_Type(Integer32):
    """Custom type zxAnEponOnuLlidQueue2WrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuLlidQueue2WrrWeight_Type.__name__ = "Integer32"
_ZxAnEponOnuLlidQueue2WrrWeight_Object = MibTableColumn
zxAnEponOnuLlidQueue2WrrWeight = _ZxAnEponOnuLlidQueue2WrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43, 1, 3),
    _ZxAnEponOnuLlidQueue2WrrWeight_Type()
)
zxAnEponOnuLlidQueue2WrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidQueue2WrrWeight.setStatus("current")


class _ZxAnEponOnuLlidQueue3WrrWeight_Type(Integer32):
    """Custom type zxAnEponOnuLlidQueue3WrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuLlidQueue3WrrWeight_Type.__name__ = "Integer32"
_ZxAnEponOnuLlidQueue3WrrWeight_Object = MibTableColumn
zxAnEponOnuLlidQueue3WrrWeight = _ZxAnEponOnuLlidQueue3WrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43, 1, 4),
    _ZxAnEponOnuLlidQueue3WrrWeight_Type()
)
zxAnEponOnuLlidQueue3WrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidQueue3WrrWeight.setStatus("current")


class _ZxAnEponOnuLlidQueue4WrrWeight_Type(Integer32):
    """Custom type zxAnEponOnuLlidQueue4WrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuLlidQueue4WrrWeight_Type.__name__ = "Integer32"
_ZxAnEponOnuLlidQueue4WrrWeight_Object = MibTableColumn
zxAnEponOnuLlidQueue4WrrWeight = _ZxAnEponOnuLlidQueue4WrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43, 1, 5),
    _ZxAnEponOnuLlidQueue4WrrWeight_Type()
)
zxAnEponOnuLlidQueue4WrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidQueue4WrrWeight.setStatus("current")


class _ZxAnEponOnuLlidQueue5WrrWeight_Type(Integer32):
    """Custom type zxAnEponOnuLlidQueue5WrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuLlidQueue5WrrWeight_Type.__name__ = "Integer32"
_ZxAnEponOnuLlidQueue5WrrWeight_Object = MibTableColumn
zxAnEponOnuLlidQueue5WrrWeight = _ZxAnEponOnuLlidQueue5WrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43, 1, 6),
    _ZxAnEponOnuLlidQueue5WrrWeight_Type()
)
zxAnEponOnuLlidQueue5WrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidQueue5WrrWeight.setStatus("current")


class _ZxAnEponOnuLlidQueue6WrrWeight_Type(Integer32):
    """Custom type zxAnEponOnuLlidQueue6WrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuLlidQueue6WrrWeight_Type.__name__ = "Integer32"
_ZxAnEponOnuLlidQueue6WrrWeight_Object = MibTableColumn
zxAnEponOnuLlidQueue6WrrWeight = _ZxAnEponOnuLlidQueue6WrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43, 1, 7),
    _ZxAnEponOnuLlidQueue6WrrWeight_Type()
)
zxAnEponOnuLlidQueue6WrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidQueue6WrrWeight.setStatus("current")


class _ZxAnEponOnuLlidQueue7WrrWeight_Type(Integer32):
    """Custom type zxAnEponOnuLlidQueue7WrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuLlidQueue7WrrWeight_Type.__name__ = "Integer32"
_ZxAnEponOnuLlidQueue7WrrWeight_Object = MibTableColumn
zxAnEponOnuLlidQueue7WrrWeight = _ZxAnEponOnuLlidQueue7WrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43, 1, 8),
    _ZxAnEponOnuLlidQueue7WrrWeight_Type()
)
zxAnEponOnuLlidQueue7WrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidQueue7WrrWeight.setStatus("current")


class _ZxAnEponOnuLlidQueue8WrrWeight_Type(Integer32):
    """Custom type zxAnEponOnuLlidQueue8WrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuLlidQueue8WrrWeight_Type.__name__ = "Integer32"
_ZxAnEponOnuLlidQueue8WrrWeight_Object = MibTableColumn
zxAnEponOnuLlidQueue8WrrWeight = _ZxAnEponOnuLlidQueue8WrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 43, 1, 9),
    _ZxAnEponOnuLlidQueue8WrrWeight_Type()
)
zxAnEponOnuLlidQueue8WrrWeight.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLlidQueue8WrrWeight.setStatus("current")
_ZxAnEponOnuPonIfTable_Object = MibTable
zxAnEponOnuPonIfTable = _ZxAnEponOnuPonIfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 44)
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonIfTable.setStatus("current")
_ZxAnEponOnuPonIfEntry_Object = MibTableRow
zxAnEponOnuPonIfEntry = _ZxAnEponOnuPonIfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 44, 1)
)
zxAnEponOnuPonIfEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonIfEntry.setStatus("current")


class _ZxAnEponOnuActivePonIf_Type(Integer32):
    """Custom type zxAnEponOnuActivePonIf based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2),
    )


_ZxAnEponOnuActivePonIf_Type.__name__ = "Integer32"
_ZxAnEponOnuActivePonIf_Object = MibTableColumn
zxAnEponOnuActivePonIf = _ZxAnEponOnuActivePonIf_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 44, 1, 1),
    _ZxAnEponOnuActivePonIf_Type()
)
zxAnEponOnuActivePonIf.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuActivePonIf.setStatus("current")
_ZxAnEponOnuSlaMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuSlaMgmt = _ZxAnEponOnuSlaMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45)
)
_ZxAnEponOnuSlaProfileIdxNext_Type = Integer32
_ZxAnEponOnuSlaProfileIdxNext_Object = MibScalar
zxAnEponOnuSlaProfileIdxNext = _ZxAnEponOnuSlaProfileIdxNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 1),
    _ZxAnEponOnuSlaProfileIdxNext_Type()
)
zxAnEponOnuSlaProfileIdxNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuSlaProfileIdxNext.setStatus("current")
_ZxAnEponOnuSlaProfileTable_Object = MibTable
zxAnEponOnuSlaProfileTable = _ZxAnEponOnuSlaProfileTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuSlaProfileTable.setStatus("current")
_ZxAnEponOnuSlaProfileEntry_Object = MibTableRow
zxAnEponOnuSlaProfileEntry = _ZxAnEponOnuSlaProfileEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 2, 1)
)
zxAnEponOnuSlaProfileEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuSlaProfileIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuSlaProfileEntry.setStatus("current")
_ZxAnEponOnuSlaProfileIndex_Type = Integer32
_ZxAnEponOnuSlaProfileIndex_Object = MibTableColumn
zxAnEponOnuSlaProfileIndex = _ZxAnEponOnuSlaProfileIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 2, 1, 1),
    _ZxAnEponOnuSlaProfileIndex_Type()
)
zxAnEponOnuSlaProfileIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuSlaProfileIndex.setStatus("current")


class _ZxAnEponOnuSlaProfileName_Type(DisplayString):
    """Custom type zxAnEponOnuSlaProfileName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponOnuSlaProfileName_Type.__name__ = "DisplayString"
_ZxAnEponOnuSlaProfileName_Object = MibTableColumn
zxAnEponOnuSlaProfileName = _ZxAnEponOnuSlaProfileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 2, 1, 2),
    _ZxAnEponOnuSlaProfileName_Type()
)
zxAnEponOnuSlaProfileName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuSlaProfileName.setStatus("current")


class _ZxAnEponOnuServiceDbaEnable_Type(Integer32):
    """Custom type zxAnEponOnuServiceDbaEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuServiceDbaEnable_Type.__name__ = "Integer32"
_ZxAnEponOnuServiceDbaEnable_Object = MibTableColumn
zxAnEponOnuServiceDbaEnable = _ZxAnEponOnuServiceDbaEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 2, 1, 3),
    _ZxAnEponOnuServiceDbaEnable_Type()
)
zxAnEponOnuServiceDbaEnable.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuServiceDbaEnable.setStatus("current")


class _ZxAnEponOnuBestEffortSchedulingScheme_Type(Integer32):
    """Custom type zxAnEponOnuBestEffortSchedulingScheme based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("sp", 1),
          ("wrr", 2),
          ("spWrr", 3))
    )


_ZxAnEponOnuBestEffortSchedulingScheme_Type.__name__ = "Integer32"
_ZxAnEponOnuBestEffortSchedulingScheme_Object = MibTableColumn
zxAnEponOnuBestEffortSchedulingScheme = _ZxAnEponOnuBestEffortSchedulingScheme_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 2, 1, 4),
    _ZxAnEponOnuBestEffortSchedulingScheme_Type()
)
zxAnEponOnuBestEffortSchedulingScheme.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuBestEffortSchedulingScheme.setStatus("current")


class _ZxAnEponOnuHighPriorityBoundary_Type(Integer32):
    """Custom type zxAnEponOnuHighPriorityBoundary based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnEponOnuHighPriorityBoundary_Type.__name__ = "Integer32"
_ZxAnEponOnuHighPriorityBoundary_Object = MibTableColumn
zxAnEponOnuHighPriorityBoundary = _ZxAnEponOnuHighPriorityBoundary_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 2, 1, 5),
    _ZxAnEponOnuHighPriorityBoundary_Type()
)
zxAnEponOnuHighPriorityBoundary.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuHighPriorityBoundary.setStatus("current")
_ZxAnEponOnuServiceDbaCycleLength_Type = Integer32
_ZxAnEponOnuServiceDbaCycleLength_Object = MibTableColumn
zxAnEponOnuServiceDbaCycleLength = _ZxAnEponOnuServiceDbaCycleLength_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 2, 1, 6),
    _ZxAnEponOnuServiceDbaCycleLength_Type()
)
zxAnEponOnuServiceDbaCycleLength.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuServiceDbaCycleLength.setStatus("current")
_ZxAnEponOnuSlaServiceIdxNext_Type = Integer32
_ZxAnEponOnuSlaServiceIdxNext_Object = MibTableColumn
zxAnEponOnuSlaServiceIdxNext = _ZxAnEponOnuSlaServiceIdxNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 2, 1, 29),
    _ZxAnEponOnuSlaServiceIdxNext_Type()
)
zxAnEponOnuSlaServiceIdxNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuSlaServiceIdxNext.setStatus("current")
_ZxAnEponOnuSlaProfileRowStatus_Type = RowStatus
_ZxAnEponOnuSlaProfileRowStatus_Object = MibTableColumn
zxAnEponOnuSlaProfileRowStatus = _ZxAnEponOnuSlaProfileRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 2, 1, 30),
    _ZxAnEponOnuSlaProfileRowStatus_Type()
)
zxAnEponOnuSlaProfileRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuSlaProfileRowStatus.setStatus("current")
_ZxAnEponOnuServiceQueueTable_Object = MibTable
zxAnEponOnuServiceQueueTable = _ZxAnEponOnuServiceQueueTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3)
)
if mibBuilder.loadTexts:
    zxAnEponOnuServiceQueueTable.setStatus("current")
_ZxAnEponOnuServiceQueueEntry_Object = MibTableRow
zxAnEponOnuServiceQueueEntry = _ZxAnEponOnuServiceQueueEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3, 1)
)
zxAnEponOnuServiceQueueEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuSlaProfileIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuSlaServiceIdx"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuServiceQueueEntry.setStatus("current")


class _ZxAnEponOnuSlaServiceIdx_Type(Integer32):
    """Custom type zxAnEponOnuSlaServiceIdx based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnEponOnuSlaServiceIdx_Type.__name__ = "Integer32"
_ZxAnEponOnuSlaServiceIdx_Object = MibTableColumn
zxAnEponOnuSlaServiceIdx = _ZxAnEponOnuSlaServiceIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3, 1, 1),
    _ZxAnEponOnuSlaServiceIdx_Type()
)
zxAnEponOnuSlaServiceIdx.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuSlaServiceIdx.setStatus("current")
_ZxAnEponOnuServiceName_Type = DisplayString
_ZxAnEponOnuServiceName_Object = MibTableColumn
zxAnEponOnuServiceName = _ZxAnEponOnuServiceName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3, 1, 2),
    _ZxAnEponOnuServiceName_Type()
)
zxAnEponOnuServiceName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuServiceName.setStatus("current")
_ZxAnEponOnuQueueId_Type = Integer32
_ZxAnEponOnuQueueId_Object = MibTableColumn
zxAnEponOnuQueueId = _ZxAnEponOnuQueueId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3, 1, 3),
    _ZxAnEponOnuQueueId_Type()
)
zxAnEponOnuQueueId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuQueueId.setStatus("current")
_ZxAnEponOnuServiceFixedPktSize_Type = Integer32
_ZxAnEponOnuServiceFixedPktSize_Object = MibTableColumn
zxAnEponOnuServiceFixedPktSize = _ZxAnEponOnuServiceFixedPktSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3, 1, 4),
    _ZxAnEponOnuServiceFixedPktSize_Type()
)
zxAnEponOnuServiceFixedPktSize.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuServiceFixedPktSize.setStatus("current")
_ZxAnEponOnuServiceFixedBandwidth_Type = Integer32
_ZxAnEponOnuServiceFixedBandwidth_Object = MibTableColumn
zxAnEponOnuServiceFixedBandwidth = _ZxAnEponOnuServiceFixedBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3, 1, 5),
    _ZxAnEponOnuServiceFixedBandwidth_Type()
)
zxAnEponOnuServiceFixedBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuServiceFixedBandwidth.setStatus("current")
_ZxAnEponOnuServiceAssuredBandwidth_Type = Integer32
_ZxAnEponOnuServiceAssuredBandwidth_Object = MibTableColumn
zxAnEponOnuServiceAssuredBandwidth = _ZxAnEponOnuServiceAssuredBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3, 1, 6),
    _ZxAnEponOnuServiceAssuredBandwidth_Type()
)
zxAnEponOnuServiceAssuredBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuServiceAssuredBandwidth.setStatus("current")
_ZxAnEponOnuServiceBestEffortBandwidth_Type = Integer32
_ZxAnEponOnuServiceBestEffortBandwidth_Object = MibTableColumn
zxAnEponOnuServiceBestEffortBandwidth = _ZxAnEponOnuServiceBestEffortBandwidth_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3, 1, 7),
    _ZxAnEponOnuServiceBestEffortBandwidth_Type()
)
zxAnEponOnuServiceBestEffortBandwidth.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuServiceBestEffortBandwidth.setStatus("current")


class _ZxAnEponOnuServiceWrrWeight_Type(Integer32):
    """Custom type zxAnEponOnuServiceWrrWeight based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuServiceWrrWeight_Type.__name__ = "Integer32"
_ZxAnEponOnuServiceWrrWeight_Object = MibTableColumn
zxAnEponOnuServiceWrrWeight = _ZxAnEponOnuServiceWrrWeight_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3, 1, 8),
    _ZxAnEponOnuServiceWrrWeight_Type()
)
zxAnEponOnuServiceWrrWeight.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuServiceWrrWeight.setStatus("current")
_ZxAnEponOnuServiceRowStatus_Type = RowStatus
_ZxAnEponOnuServiceRowStatus_Object = MibTableColumn
zxAnEponOnuServiceRowStatus = _ZxAnEponOnuServiceRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 3, 1, 30),
    _ZxAnEponOnuServiceRowStatus_Type()
)
zxAnEponOnuServiceRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponOnuServiceRowStatus.setStatus("current")
_ZxAnEponOnuSlaProfileApplyTable_Object = MibTable
zxAnEponOnuSlaProfileApplyTable = _ZxAnEponOnuSlaProfileApplyTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 4)
)
if mibBuilder.loadTexts:
    zxAnEponOnuSlaProfileApplyTable.setStatus("current")
_ZxAnEponOnuSlaProfileApplyEntry_Object = MibTableRow
zxAnEponOnuSlaProfileApplyEntry = _ZxAnEponOnuSlaProfileApplyEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 4, 1)
)
zxAnEponOnuSlaProfileApplyEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuSlaProfileApplyEntry.setStatus("current")
_ZxAnEponOnuCurrSlaProfileIdx_Type = Integer32
_ZxAnEponOnuCurrSlaProfileIdx_Object = MibTableColumn
zxAnEponOnuCurrSlaProfileIdx = _ZxAnEponOnuCurrSlaProfileIdx_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 45, 4, 1, 1),
    _ZxAnEponOnuCurrSlaProfileIdx_Type()
)
zxAnEponOnuCurrSlaProfileIdx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuCurrSlaProfileIdx.setStatus("current")
_ZxAnEponOnuHoldoverTable_Object = MibTable
zxAnEponOnuHoldoverTable = _ZxAnEponOnuHoldoverTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 46)
)
if mibBuilder.loadTexts:
    zxAnEponOnuHoldoverTable.setStatus("current")
_ZxAnEponOnuHoldoverEntry_Object = MibTableRow
zxAnEponOnuHoldoverEntry = _ZxAnEponOnuHoldoverEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 46, 1)
)
zxAnEponOnuHoldoverEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuHoldoverEntry.setStatus("current")


class _ZxAnEponOnuHoldoverState_Type(Integer32):
    """Custom type zxAnEponOnuHoldoverState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuHoldoverState_Type.__name__ = "Integer32"
_ZxAnEponOnuHoldoverState_Object = MibTableColumn
zxAnEponOnuHoldoverState = _ZxAnEponOnuHoldoverState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 46, 1, 1),
    _ZxAnEponOnuHoldoverState_Type()
)
zxAnEponOnuHoldoverState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuHoldoverState.setStatus("current")


class _ZxAnEponOnuHoldoverTime_Type(Integer32):
    """Custom type zxAnEponOnuHoldoverTime based on Integer32"""
    defaultValue = 500

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(500, 1000),
    )


_ZxAnEponOnuHoldoverTime_Type.__name__ = "Integer32"
_ZxAnEponOnuHoldoverTime_Object = MibTableColumn
zxAnEponOnuHoldoverTime = _ZxAnEponOnuHoldoverTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 46, 1, 2),
    _ZxAnEponOnuHoldoverTime_Type()
)
zxAnEponOnuHoldoverTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuHoldoverTime.setStatus("current")
_ZxAnEponOnuAlarmMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuAlarmMgmt = _ZxAnEponOnuAlarmMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48)
)
_ZxAnEponOnuLvlAlarmCtrlTable_Object = MibTable
zxAnEponOnuLvlAlarmCtrlTable = _ZxAnEponOnuLvlAlarmCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuLvlAlarmCtrlTable.setStatus("current")
_ZxAnEponOnuLvlAlarmCtrlEntry_Object = MibTableRow
zxAnEponOnuLvlAlarmCtrlEntry = _ZxAnEponOnuLvlAlarmCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 1, 1)
)
zxAnEponOnuLvlAlarmCtrlEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuLvlAlarmCode"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuLvlAlarmCtrlEntry.setStatus("current")
_ZxAnEponOnuLvlAlarmCode_Type = Integer32
_ZxAnEponOnuLvlAlarmCode_Object = MibTableColumn
zxAnEponOnuLvlAlarmCode = _ZxAnEponOnuLvlAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 1, 1, 1),
    _ZxAnEponOnuLvlAlarmCode_Type()
)
zxAnEponOnuLvlAlarmCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuLvlAlarmCode.setStatus("current")


class _ZxAnEponOnuLvlAlarmEnable_Type(Integer32):
    """Custom type zxAnEponOnuLvlAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuLvlAlarmEnable_Type.__name__ = "Integer32"
_ZxAnEponOnuLvlAlarmEnable_Object = MibTableColumn
zxAnEponOnuLvlAlarmEnable = _ZxAnEponOnuLvlAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 1, 1, 2),
    _ZxAnEponOnuLvlAlarmEnable_Type()
)
zxAnEponOnuLvlAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLvlAlarmEnable.setStatus("current")
_ZxAnEponOnuLvlAlarmThreshold_Type = Integer32
_ZxAnEponOnuLvlAlarmThreshold_Object = MibTableColumn
zxAnEponOnuLvlAlarmThreshold = _ZxAnEponOnuLvlAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 1, 1, 3),
    _ZxAnEponOnuLvlAlarmThreshold_Type()
)
zxAnEponOnuLvlAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLvlAlarmThreshold.setStatus("current")
_ZxAnEponOnuLvlAlarmRestoreThreshold_Type = Integer32
_ZxAnEponOnuLvlAlarmRestoreThreshold_Object = MibTableColumn
zxAnEponOnuLvlAlarmRestoreThreshold = _ZxAnEponOnuLvlAlarmRestoreThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 1, 1, 4),
    _ZxAnEponOnuLvlAlarmRestoreThreshold_Type()
)
zxAnEponOnuLvlAlarmRestoreThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuLvlAlarmRestoreThreshold.setStatus("current")
_ZxAnEponOnuPonAlarmCtrlTable_Object = MibTable
zxAnEponOnuPonAlarmCtrlTable = _ZxAnEponOnuPonAlarmCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonAlarmCtrlTable.setStatus("current")
_ZxAnEponOnuPonAlarmCtrlEntry_Object = MibTableRow
zxAnEponOnuPonAlarmCtrlEntry = _ZxAnEponOnuPonAlarmCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 2, 1)
)
zxAnEponOnuPonAlarmCtrlEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPonAlarmCode"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonAlarmCtrlEntry.setStatus("current")
_ZxAnEponOnuPonAlarmCode_Type = Integer32
_ZxAnEponOnuPonAlarmCode_Object = MibTableColumn
zxAnEponOnuPonAlarmCode = _ZxAnEponOnuPonAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 2, 1, 1),
    _ZxAnEponOnuPonAlarmCode_Type()
)
zxAnEponOnuPonAlarmCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuPonAlarmCode.setStatus("current")


class _ZxAnEponOnuPonAlarmEnable_Type(Integer32):
    """Custom type zxAnEponOnuPonAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuPonAlarmEnable_Type.__name__ = "Integer32"
_ZxAnEponOnuPonAlarmEnable_Object = MibTableColumn
zxAnEponOnuPonAlarmEnable = _ZxAnEponOnuPonAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 2, 1, 2),
    _ZxAnEponOnuPonAlarmEnable_Type()
)
zxAnEponOnuPonAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPonAlarmEnable.setStatus("current")
_ZxAnEponOnuPonAlarmThreshold_Type = Integer32
_ZxAnEponOnuPonAlarmThreshold_Object = MibTableColumn
zxAnEponOnuPonAlarmThreshold = _ZxAnEponOnuPonAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 2, 1, 3),
    _ZxAnEponOnuPonAlarmThreshold_Type()
)
zxAnEponOnuPonAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPonAlarmThreshold.setStatus("current")
_ZxAnEponOnuPonAlarmRestoreThreshold_Type = Integer32
_ZxAnEponOnuPonAlarmRestoreThreshold_Object = MibTableColumn
zxAnEponOnuPonAlarmRestoreThreshold = _ZxAnEponOnuPonAlarmRestoreThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 2, 1, 4),
    _ZxAnEponOnuPonAlarmRestoreThreshold_Type()
)
zxAnEponOnuPonAlarmRestoreThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPonAlarmRestoreThreshold.setStatus("current")
_ZxAnEponOnuUniAlarmCtrlTable_Object = MibTable
zxAnEponOnuUniAlarmCtrlTable = _ZxAnEponOnuUniAlarmCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 3)
)
if mibBuilder.loadTexts:
    zxAnEponOnuUniAlarmCtrlTable.setStatus("current")
_ZxAnEponOnuUniAlarmCtrlEntry_Object = MibTableRow
zxAnEponOnuUniAlarmCtrlEntry = _ZxAnEponOnuUniAlarmCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 3, 1)
)
zxAnEponOnuUniAlarmCtrlEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuUniAlarmCode"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuUniAlarmCtrlEntry.setStatus("current")
_ZxAnEponOnuUniAlarmCode_Type = Integer32
_ZxAnEponOnuUniAlarmCode_Object = MibTableColumn
zxAnEponOnuUniAlarmCode = _ZxAnEponOnuUniAlarmCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 3, 1, 1),
    _ZxAnEponOnuUniAlarmCode_Type()
)
zxAnEponOnuUniAlarmCode.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuUniAlarmCode.setStatus("current")


class _ZxAnEponOnuUniAlarmEnable_Type(Integer32):
    """Custom type zxAnEponOnuUniAlarmEnable based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disable", 1),
          ("enable", 2))
    )


_ZxAnEponOnuUniAlarmEnable_Type.__name__ = "Integer32"
_ZxAnEponOnuUniAlarmEnable_Object = MibTableColumn
zxAnEponOnuUniAlarmEnable = _ZxAnEponOnuUniAlarmEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 3, 1, 2),
    _ZxAnEponOnuUniAlarmEnable_Type()
)
zxAnEponOnuUniAlarmEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuUniAlarmEnable.setStatus("current")


class _ZxAnEponOnuUniAlarmThreshold_Type(Unsigned32):
    """Custom type zxAnEponOnuUniAlarmThreshold based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ZxAnEponOnuUniAlarmThreshold_Type.__name__ = "Unsigned32"
_ZxAnEponOnuUniAlarmThreshold_Object = MibTableColumn
zxAnEponOnuUniAlarmThreshold = _ZxAnEponOnuUniAlarmThreshold_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 3, 1, 3),
    _ZxAnEponOnuUniAlarmThreshold_Type()
)
zxAnEponOnuUniAlarmThreshold.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuUniAlarmThreshold.setStatus("current")


class _ZxAnEponOnuUniAlarmRestoreThresh_Type(Unsigned32):
    """Custom type zxAnEponOnuUniAlarmRestoreThresh based on Unsigned32"""
    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ZxAnEponOnuUniAlarmRestoreThresh_Type.__name__ = "Unsigned32"
_ZxAnEponOnuUniAlarmRestoreThresh_Object = MibTableColumn
zxAnEponOnuUniAlarmRestoreThresh = _ZxAnEponOnuUniAlarmRestoreThresh_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 48, 3, 1, 4),
    _ZxAnEponOnuUniAlarmRestoreThresh_Type()
)
zxAnEponOnuUniAlarmRestoreThresh.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuUniAlarmRestoreThresh.setStatus("current")
_ZxAnEponOnuVersionMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuVersionMgmt = _ZxAnEponOnuVersionMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49)
)
_ZxAnEponOnuVersionTable_Object = MibTable
zxAnEponOnuVersionTable = _ZxAnEponOnuVersionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVersionTable.setStatus("current")
_ZxAnEponOnuVersionEntry_Object = MibTableRow
zxAnEponOnuVersionEntry = _ZxAnEponOnuVersionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 1, 1)
)
zxAnEponOnuVersionEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuVersionId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVersionEntry.setStatus("current")
_ZxAnEponOnuVersionId_Type = Integer32
_ZxAnEponOnuVersionId_Object = MibTableColumn
zxAnEponOnuVersionId = _ZxAnEponOnuVersionId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 1, 1, 1),
    _ZxAnEponOnuVersionId_Type()
)
zxAnEponOnuVersionId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionId.setStatus("current")
_ZxAnEponOnuVersionFileName_Type = DisplayString
_ZxAnEponOnuVersionFileName_Object = MibTableColumn
zxAnEponOnuVersionFileName = _ZxAnEponOnuVersionFileName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 1, 1, 2),
    _ZxAnEponOnuVersionFileName_Type()
)
zxAnEponOnuVersionFileName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionFileName.setStatus("current")
_ZxAnEponOnuVersionType_Type = DisplayString
_ZxAnEponOnuVersionType_Object = MibTableColumn
zxAnEponOnuVersionType = _ZxAnEponOnuVersionType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 1, 1, 3),
    _ZxAnEponOnuVersionType_Type()
)
zxAnEponOnuVersionType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionType.setStatus("current")
_ZxAnEponOnuVersionTag_Type = DisplayString
_ZxAnEponOnuVersionTag_Object = MibTableColumn
zxAnEponOnuVersionTag = _ZxAnEponOnuVersionTag_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 1, 1, 4),
    _ZxAnEponOnuVersionTag_Type()
)
zxAnEponOnuVersionTag.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionTag.setStatus("current")
_ZxAnEponOnuVersionBuildTime_Type = DisplayString
_ZxAnEponOnuVersionBuildTime_Object = MibTableColumn
zxAnEponOnuVersionBuildTime = _ZxAnEponOnuVersionBuildTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 1, 1, 5),
    _ZxAnEponOnuVersionBuildTime_Type()
)
zxAnEponOnuVersionBuildTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionBuildTime.setStatus("current")
_ZxAnEponOnuVersionUpdateTable_Object = MibTable
zxAnEponOnuVersionUpdateTable = _ZxAnEponOnuVersionUpdateTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateTable.setStatus("current")
_ZxAnEponOnuVersionUpdateEntry_Object = MibTableRow
zxAnEponOnuVersionUpdateEntry = _ZxAnEponOnuVersionUpdateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 2, 1)
)
zxAnEponOnuVersionUpdateEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuVersionId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateEntry.setStatus("current")
_ZxAnEponOnuVersionUpdateOnuType_Type = DisplayString
_ZxAnEponOnuVersionUpdateOnuType_Object = MibTableColumn
zxAnEponOnuVersionUpdateOnuType = _ZxAnEponOnuVersionUpdateOnuType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 2, 1, 1),
    _ZxAnEponOnuVersionUpdateOnuType_Type()
)
zxAnEponOnuVersionUpdateOnuType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateOnuType.setStatus("current")


class _ZxAnEponOnuVersionUpdateLocType_Type(Integer32):
    """Custom type zxAnEponOnuVersionUpdateLocType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("slot", 1),
          ("olt", 2),
          ("onuList", 3))
    )


_ZxAnEponOnuVersionUpdateLocType_Type.__name__ = "Integer32"
_ZxAnEponOnuVersionUpdateLocType_Object = MibTableColumn
zxAnEponOnuVersionUpdateLocType = _ZxAnEponOnuVersionUpdateLocType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 2, 1, 2),
    _ZxAnEponOnuVersionUpdateLocType_Type()
)
zxAnEponOnuVersionUpdateLocType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateLocType.setStatus("current")
_ZxAnEponOnuVersionUpdateSlotId_Type = Integer32
_ZxAnEponOnuVersionUpdateSlotId_Object = MibTableColumn
zxAnEponOnuVersionUpdateSlotId = _ZxAnEponOnuVersionUpdateSlotId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 2, 1, 3),
    _ZxAnEponOnuVersionUpdateSlotId_Type()
)
zxAnEponOnuVersionUpdateSlotId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateSlotId.setStatus("current")
_ZxAnEponOnuVersionUpdateOltId_Type = Integer32
_ZxAnEponOnuVersionUpdateOltId_Object = MibTableColumn
zxAnEponOnuVersionUpdateOltId = _ZxAnEponOnuVersionUpdateOltId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 2, 1, 4),
    _ZxAnEponOnuVersionUpdateOltId_Type()
)
zxAnEponOnuVersionUpdateOltId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateOltId.setStatus("current")
_ZxAnEponOnuVersionUpdateOnuList_Type = DisplayString
_ZxAnEponOnuVersionUpdateOnuList_Object = MibTableColumn
zxAnEponOnuVersionUpdateOnuList = _ZxAnEponOnuVersionUpdateOnuList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 2, 1, 5),
    _ZxAnEponOnuVersionUpdateOnuList_Type()
)
zxAnEponOnuVersionUpdateOnuList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateOnuList.setStatus("current")


class _ZxAnEponOnuVersionUpdateAction_Type(Integer32):
    """Custom type zxAnEponOnuVersionUpdateAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              99)
        )
    )
    namedValues = NamedValues(
        *(("download", 1),
          ("downloadAndActivate", 2),
          ("downloadAndCommit", 3),
          ("activate", 4),
          ("commit", 5),
          ("abort", 99))
    )


_ZxAnEponOnuVersionUpdateAction_Type.__name__ = "Integer32"
_ZxAnEponOnuVersionUpdateAction_Object = MibTableColumn
zxAnEponOnuVersionUpdateAction = _ZxAnEponOnuVersionUpdateAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 2, 1, 6),
    _ZxAnEponOnuVersionUpdateAction_Type()
)
zxAnEponOnuVersionUpdateAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateAction.setStatus("current")
_ZxAnEponOnuVersionUpdateStatusTable_Object = MibTable
zxAnEponOnuVersionUpdateStatusTable = _ZxAnEponOnuVersionUpdateStatusTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateStatusTable.setStatus("current")
_ZxAnEponOnuVersionUpdateStatusEntry_Object = MibTableRow
zxAnEponOnuVersionUpdateStatusEntry = _ZxAnEponOnuVersionUpdateStatusEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3, 1)
)
zxAnEponOnuVersionUpdateStatusEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateStatusEntry.setStatus("current")


class _ZxAnEponOnuVersionUpdateState_Type(Integer32):
    """Custom type zxAnEponOnuVersionUpdateState based on Integer32"""
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
        *(("notStart", 1),
          ("updateFailed", 2),
          ("downloading", 3),
          ("waitEndResponse", 4),
          ("finished", 5))
    )


_ZxAnEponOnuVersionUpdateState_Type.__name__ = "Integer32"
_ZxAnEponOnuVersionUpdateState_Object = MibTableColumn
zxAnEponOnuVersionUpdateState = _ZxAnEponOnuVersionUpdateState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3, 1, 1),
    _ZxAnEponOnuVersionUpdateState_Type()
)
zxAnEponOnuVersionUpdateState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateState.setStatus("current")


class _ZxAnEponOnuVersionUpdateAbortReason_Type(Integer32):
    """Custom type zxAnEponOnuVersionUpdateAbortReason based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("none", 1),
          ("downloadError", 2),
          ("downloadTimeout", 3),
          ("onuReturnError", 4),
          ("endDownloadCheckError", 5),
          ("userAbort", 6),
          ("onuOffLine", 7))
    )


_ZxAnEponOnuVersionUpdateAbortReason_Type.__name__ = "Integer32"
_ZxAnEponOnuVersionUpdateAbortReason_Object = MibTableColumn
zxAnEponOnuVersionUpdateAbortReason = _ZxAnEponOnuVersionUpdateAbortReason_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3, 1, 2),
    _ZxAnEponOnuVersionUpdateAbortReason_Type()
)
zxAnEponOnuVersionUpdateAbortReason.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateAbortReason.setStatus("current")
_ZxAnEponOnuVersionUpdateErrCode_Type = Integer32
_ZxAnEponOnuVersionUpdateErrCode_Object = MibTableColumn
zxAnEponOnuVersionUpdateErrCode = _ZxAnEponOnuVersionUpdateErrCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3, 1, 3),
    _ZxAnEponOnuVersionUpdateErrCode_Type()
)
zxAnEponOnuVersionUpdateErrCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateErrCode.setStatus("current")


class _ZxAnEponOnuVersionUpdateErrMsg_Type(DisplayString):
    """Custom type zxAnEponOnuVersionUpdateErrMsg based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 128),
    )


_ZxAnEponOnuVersionUpdateErrMsg_Type.__name__ = "DisplayString"
_ZxAnEponOnuVersionUpdateErrMsg_Object = MibTableColumn
zxAnEponOnuVersionUpdateErrMsg = _ZxAnEponOnuVersionUpdateErrMsg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3, 1, 4),
    _ZxAnEponOnuVersionUpdateErrMsg_Type()
)
zxAnEponOnuVersionUpdateErrMsg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateErrMsg.setStatus("current")


class _ZxAnEponOnuVersionUpdateProgress_Type(Integer32):
    """Custom type zxAnEponOnuVersionUpdateProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 100),
    )


_ZxAnEponOnuVersionUpdateProgress_Type.__name__ = "Integer32"
_ZxAnEponOnuVersionUpdateProgress_Object = MibTableColumn
zxAnEponOnuVersionUpdateProgress = _ZxAnEponOnuVersionUpdateProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3, 1, 5),
    _ZxAnEponOnuVersionUpdateProgress_Type()
)
zxAnEponOnuVersionUpdateProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionUpdateProgress.setStatus("current")
_ZxAnEponOnuCurrentUsedVersionName_Type = DisplayString
_ZxAnEponOnuCurrentUsedVersionName_Object = MibTableColumn
zxAnEponOnuCurrentUsedVersionName = _ZxAnEponOnuCurrentUsedVersionName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3, 1, 6),
    _ZxAnEponOnuCurrentUsedVersionName_Type()
)
zxAnEponOnuCurrentUsedVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuCurrentUsedVersionName.setStatus("current")
_ZxAnEponOnuCurrentUsedVersionTime_Type = DisplayString
_ZxAnEponOnuCurrentUsedVersionTime_Object = MibTableColumn
zxAnEponOnuCurrentUsedVersionTime = _ZxAnEponOnuCurrentUsedVersionTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3, 1, 7),
    _ZxAnEponOnuCurrentUsedVersionTime_Type()
)
zxAnEponOnuCurrentUsedVersionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuCurrentUsedVersionTime.setStatus("current")
_ZxAnEponOnuUpdatingVersionName_Type = DisplayString
_ZxAnEponOnuUpdatingVersionName_Object = MibTableColumn
zxAnEponOnuUpdatingVersionName = _ZxAnEponOnuUpdatingVersionName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3, 1, 8),
    _ZxAnEponOnuUpdatingVersionName_Type()
)
zxAnEponOnuUpdatingVersionName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuUpdatingVersionName.setStatus("current")
_ZxAnEponOnuUpdatingVersionTime_Type = DisplayString
_ZxAnEponOnuUpdatingVersionTime_Object = MibTableColumn
zxAnEponOnuUpdatingVersionTime = _ZxAnEponOnuUpdatingVersionTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 3, 1, 9),
    _ZxAnEponOnuUpdatingVersionTime_Type()
)
zxAnEponOnuUpdatingVersionTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuUpdatingVersionTime.setStatus("current")
_ZxAnEponOnuVersionActionTable_Object = MibTable
zxAnEponOnuVersionActionTable = _ZxAnEponOnuVersionActionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 4)
)
if mibBuilder.loadTexts:
    zxAnEponOnuVersionActionTable.setStatus("current")
_ZxAnEponOnuVersionActionEntry_Object = MibTableRow
zxAnEponOnuVersionActionEntry = _ZxAnEponOnuVersionActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 4, 1)
)
zxAnEponOnuVersionActionEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuVersionImageIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuVersionActionEntry.setStatus("current")
_ZxAnEponOnuVersionImageIndex_Type = Integer32
_ZxAnEponOnuVersionImageIndex_Object = MibTableColumn
zxAnEponOnuVersionImageIndex = _ZxAnEponOnuVersionImageIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 4, 1, 1),
    _ZxAnEponOnuVersionImageIndex_Type()
)
zxAnEponOnuVersionImageIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionImageIndex.setStatus("current")


class _ZxAnEponOnuVersionImageAction_Type(Integer32):
    """Custom type zxAnEponOnuVersionImageAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("activate", 1),
          ("commit", 2))
    )


_ZxAnEponOnuVersionImageAction_Type.__name__ = "Integer32"
_ZxAnEponOnuVersionImageAction_Object = MibTableColumn
zxAnEponOnuVersionImageAction = _ZxAnEponOnuVersionImageAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 4, 1, 2),
    _ZxAnEponOnuVersionImageAction_Type()
)
zxAnEponOnuVersionImageAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionImageAction.setStatus("current")


class _ZxAnEponOnuVersionImageCommitState_Type(Integer32):
    """Custom type zxAnEponOnuVersionImageCommitState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("committed", 1),
          ("notCommitted", 2))
    )


_ZxAnEponOnuVersionImageCommitState_Type.__name__ = "Integer32"
_ZxAnEponOnuVersionImageCommitState_Object = MibTableColumn
zxAnEponOnuVersionImageCommitState = _ZxAnEponOnuVersionImageCommitState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 4, 1, 3),
    _ZxAnEponOnuVersionImageCommitState_Type()
)
zxAnEponOnuVersionImageCommitState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionImageCommitState.setStatus("current")


class _ZxAnEponOnuVersionImageActiveState_Type(Integer32):
    """Custom type zxAnEponOnuVersionImageActiveState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("actived", 1),
          ("notActived", 2))
    )


_ZxAnEponOnuVersionImageActiveState_Type.__name__ = "Integer32"
_ZxAnEponOnuVersionImageActiveState_Object = MibTableColumn
zxAnEponOnuVersionImageActiveState = _ZxAnEponOnuVersionImageActiveState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 4, 1, 4),
    _ZxAnEponOnuVersionImageActiveState_Type()
)
zxAnEponOnuVersionImageActiveState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionImageActiveState.setStatus("current")


class _ZxAnEponOnuVersionImageValidState_Type(Integer32):
    """Custom type zxAnEponOnuVersionImageValidState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("valid", 1),
          ("notValid", 2))
    )


_ZxAnEponOnuVersionImageValidState_Type.__name__ = "Integer32"
_ZxAnEponOnuVersionImageValidState_Object = MibTableColumn
zxAnEponOnuVersionImageValidState = _ZxAnEponOnuVersionImageValidState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 49, 4, 1, 5),
    _ZxAnEponOnuVersionImageValidState_Type()
)
zxAnEponOnuVersionImageValidState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuVersionImageValidState.setStatus("current")
_ZxAnEponOnuPonMacShapingMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuPonMacShapingMgmt = _ZxAnEponOnuPonMacShapingMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50)
)
_ZxAnEponOnuPonMacShapingTable_Object = MibTable
zxAnEponOnuPonMacShapingTable = _ZxAnEponOnuPonMacShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacShapingTable.setStatus("current")
_ZxAnEponOnuPonMacShapingEntry_Object = MibTableRow
zxAnEponOnuPonMacShapingEntry = _ZxAnEponOnuPonMacShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 1, 1)
)
zxAnEponOnuPonMacShapingEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacShapingEntry.setStatus("current")


class _ZxAnEponOnuShappingAdminStatus_Type(Integer32):
    """Custom type zxAnEponOnuShappingAdminStatus based on Integer32"""
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


_ZxAnEponOnuShappingAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuShappingAdminStatus_Object = MibTableColumn
zxAnEponOnuShappingAdminStatus = _ZxAnEponOnuShappingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 1, 1, 1),
    _ZxAnEponOnuShappingAdminStatus_Type()
)
zxAnEponOnuShappingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuShappingAdminStatus.setStatus("current")


class _ZxAnEponOnuShappingCir_Type(Integer32):
    """Custom type zxAnEponOnuShappingCir based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16777215),
    )


_ZxAnEponOnuShappingCir_Type.__name__ = "Integer32"
_ZxAnEponOnuShappingCir_Object = MibTableColumn
zxAnEponOnuShappingCir = _ZxAnEponOnuShappingCir_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 1, 1, 2),
    _ZxAnEponOnuShappingCir_Type()
)
zxAnEponOnuShappingCir.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuShappingCir.setStatus("current")


class _ZxAnEponOnuShappingCbs_Type(Integer32):
    """Custom type zxAnEponOnuShappingCbs based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1522, 16777215),
    )


_ZxAnEponOnuShappingCbs_Type.__name__ = "Integer32"
_ZxAnEponOnuShappingCbs_Object = MibTableColumn
zxAnEponOnuShappingCbs = _ZxAnEponOnuShappingCbs_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 1, 1, 3),
    _ZxAnEponOnuShappingCbs_Type()
)
zxAnEponOnuShappingCbs.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuShappingCbs.setStatus("current")
_ZxAnEponOnuPonMacBufferTable_Object = MibTable
zxAnEponOnuPonMacBufferTable = _ZxAnEponOnuPonMacBufferTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacBufferTable.setStatus("current")
_ZxAnEponOnuPonMacBufferEntry_Object = MibTableRow
zxAnEponOnuPonMacBufferEntry = _ZxAnEponOnuPonMacBufferEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 2, 1)
)
zxAnEponOnuPonMacBufferEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacBufferEntry.setStatus("current")


class _ZxAnEponOnuPonMacDsBufferAdminStatus_Type(Integer32):
    """Custom type zxAnEponOnuPonMacDsBufferAdminStatus based on Integer32"""
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


_ZxAnEponOnuPonMacDsBufferAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuPonMacDsBufferAdminStatus_Object = MibTableColumn
zxAnEponOnuPonMacDsBufferAdminStatus = _ZxAnEponOnuPonMacDsBufferAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 2, 1, 1),
    _ZxAnEponOnuPonMacDsBufferAdminStatus_Type()
)
zxAnEponOnuPonMacDsBufferAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacDsBufferAdminStatus.setStatus("current")


class _ZxAnEponOnuPonMacDsBufferOperStatus_Type(Integer32):
    """Custom type zxAnEponOnuPonMacDsBufferOperStatus based on Integer32"""
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


_ZxAnEponOnuPonMacDsBufferOperStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuPonMacDsBufferOperStatus_Object = MibTableColumn
zxAnEponOnuPonMacDsBufferOperStatus = _ZxAnEponOnuPonMacDsBufferOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 2, 1, 2),
    _ZxAnEponOnuPonMacDsBufferOperStatus_Type()
)
zxAnEponOnuPonMacDsBufferOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacDsBufferOperStatus.setStatus("current")
_ZxAnEponOnuPonMacDsConfBufferSize_Type = Integer32
_ZxAnEponOnuPonMacDsConfBufferSize_Object = MibTableColumn
zxAnEponOnuPonMacDsConfBufferSize = _ZxAnEponOnuPonMacDsConfBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 2, 1, 3),
    _ZxAnEponOnuPonMacDsConfBufferSize_Type()
)
zxAnEponOnuPonMacDsConfBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacDsConfBufferSize.setStatus("current")
_ZxAnEponOnuPonMacDsActBufferSize_Type = Integer32
_ZxAnEponOnuPonMacDsActBufferSize_Object = MibTableColumn
zxAnEponOnuPonMacDsActBufferSize = _ZxAnEponOnuPonMacDsActBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 2, 1, 4),
    _ZxAnEponOnuPonMacDsActBufferSize_Type()
)
zxAnEponOnuPonMacDsActBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacDsActBufferSize.setStatus("current")


class _ZxAnEponOnuPonMacUsBufferAdminStatus_Type(Integer32):
    """Custom type zxAnEponOnuPonMacUsBufferAdminStatus based on Integer32"""
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


_ZxAnEponOnuPonMacUsBufferAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuPonMacUsBufferAdminStatus_Object = MibTableColumn
zxAnEponOnuPonMacUsBufferAdminStatus = _ZxAnEponOnuPonMacUsBufferAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 2, 1, 5),
    _ZxAnEponOnuPonMacUsBufferAdminStatus_Type()
)
zxAnEponOnuPonMacUsBufferAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacUsBufferAdminStatus.setStatus("current")


class _ZxAnEponOnuPonMacUsBufferOperStatus_Type(Integer32):
    """Custom type zxAnEponOnuPonMacUsBufferOperStatus based on Integer32"""
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


_ZxAnEponOnuPonMacUsBufferOperStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuPonMacUsBufferOperStatus_Object = MibTableColumn
zxAnEponOnuPonMacUsBufferOperStatus = _ZxAnEponOnuPonMacUsBufferOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 2, 1, 6),
    _ZxAnEponOnuPonMacUsBufferOperStatus_Type()
)
zxAnEponOnuPonMacUsBufferOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacUsBufferOperStatus.setStatus("current")
_ZxAnEponOnuPonMacUsConfBufferSize_Type = Integer32
_ZxAnEponOnuPonMacUsConfBufferSize_Object = MibTableColumn
zxAnEponOnuPonMacUsConfBufferSize = _ZxAnEponOnuPonMacUsConfBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 2, 1, 7),
    _ZxAnEponOnuPonMacUsConfBufferSize_Type()
)
zxAnEponOnuPonMacUsConfBufferSize.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacUsConfBufferSize.setStatus("current")
_ZxAnEponOnuPonMacUsActBufferSize_Type = Integer32
_ZxAnEponOnuPonMacUsActBufferSize_Object = MibTableColumn
zxAnEponOnuPonMacUsActBufferSize = _ZxAnEponOnuPonMacUsActBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 2, 1, 8),
    _ZxAnEponOnuPonMacUsActBufferSize_Type()
)
zxAnEponOnuPonMacUsActBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacUsActBufferSize.setStatus("current")
_ZxAnEponOnuPonMacBufferCapabilityTable_Object = MibTable
zxAnEponOnuPonMacBufferCapabilityTable = _ZxAnEponOnuPonMacBufferCapabilityTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 3)
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacBufferCapabilityTable.setStatus("current")
_ZxAnEponOnuPonMacBufferCapabilityEntry_Object = MibTableRow
zxAnEponOnuPonMacBufferCapabilityEntry = _ZxAnEponOnuPonMacBufferCapabilityEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 3, 1)
)
zxAnEponOnuPonMacBufferCapabilityEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacBufferCapabilityEntry.setStatus("current")


class _ZxAnEponOnuPonMacBufferCapability_Type(Integer32):
    """Custom type zxAnEponOnuPonMacBufferCapability based on Integer32"""
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


_ZxAnEponOnuPonMacBufferCapability_Type.__name__ = "Integer32"
_ZxAnEponOnuPonMacBufferCapability_Object = MibTableColumn
zxAnEponOnuPonMacBufferCapability = _ZxAnEponOnuPonMacBufferCapability_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 3, 1, 1),
    _ZxAnEponOnuPonMacBufferCapability_Type()
)
zxAnEponOnuPonMacBufferCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacBufferCapability.setStatus("current")
_ZxAnEponOnuPonMacMinDsBufferSize_Type = Integer32
_ZxAnEponOnuPonMacMinDsBufferSize_Object = MibTableColumn
zxAnEponOnuPonMacMinDsBufferSize = _ZxAnEponOnuPonMacMinDsBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 3, 1, 2),
    _ZxAnEponOnuPonMacMinDsBufferSize_Type()
)
zxAnEponOnuPonMacMinDsBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacMinDsBufferSize.setStatus("current")
_ZxAnEponOnuPonMacMaxDsBufferSize_Type = Integer32
_ZxAnEponOnuPonMacMaxDsBufferSize_Object = MibTableColumn
zxAnEponOnuPonMacMaxDsBufferSize = _ZxAnEponOnuPonMacMaxDsBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 3, 1, 3),
    _ZxAnEponOnuPonMacMaxDsBufferSize_Type()
)
zxAnEponOnuPonMacMaxDsBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacMaxDsBufferSize.setStatus("current")
_ZxAnEponOnuPonMacMinUsBufferSize_Type = Integer32
_ZxAnEponOnuPonMacMinUsBufferSize_Object = MibTableColumn
zxAnEponOnuPonMacMinUsBufferSize = _ZxAnEponOnuPonMacMinUsBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 3, 1, 4),
    _ZxAnEponOnuPonMacMinUsBufferSize_Type()
)
zxAnEponOnuPonMacMinUsBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacMinUsBufferSize.setStatus("current")
_ZxAnEponOnuPonMacMaxUsBufferSize_Type = Integer32
_ZxAnEponOnuPonMacMaxUsBufferSize_Object = MibTableColumn
zxAnEponOnuPonMacMaxUsBufferSize = _ZxAnEponOnuPonMacMaxUsBufferSize_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 50, 3, 1, 5),
    _ZxAnEponOnuPonMacMaxUsBufferSize_Type()
)
zxAnEponOnuPonMacMaxUsBufferSize.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPonMacMaxUsBufferSize.setStatus("current")
_ZxAnEponOnuUniMacTable_Object = MibTable
zxAnEponOnuUniMacTable = _ZxAnEponOnuUniMacTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 51)
)
if mibBuilder.loadTexts:
    zxAnEponOnuUniMacTable.setStatus("current")
_ZxAnEponOnuUniMacEntry_Object = MibTableRow
zxAnEponOnuUniMacEntry = _ZxAnEponOnuUniMacEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 51, 1)
)
zxAnEponOnuUniMacEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuUniVlanId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuUniMacSequenceNo"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuUniMacEntry.setStatus("current")


class _ZxAnEponOnuUniVlanId_Type(Integer32):
    """Custom type zxAnEponOnuUniVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponOnuUniVlanId_Type.__name__ = "Integer32"
_ZxAnEponOnuUniVlanId_Object = MibTableColumn
zxAnEponOnuUniVlanId = _ZxAnEponOnuUniVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 51, 1, 1),
    _ZxAnEponOnuUniVlanId_Type()
)
zxAnEponOnuUniVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuUniVlanId.setStatus("current")
_ZxAnEponOnuUniMacSequenceNo_Type = Integer32
_ZxAnEponOnuUniMacSequenceNo_Object = MibTableColumn
zxAnEponOnuUniMacSequenceNo = _ZxAnEponOnuUniMacSequenceNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 51, 1, 2),
    _ZxAnEponOnuUniMacSequenceNo_Type()
)
zxAnEponOnuUniMacSequenceNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuUniMacSequenceNo.setStatus("current")


class _ZxAnEponOnuUniMacType_Type(Integer32):
    """Custom type zxAnEponOnuUniMacType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("dynamic", 1),
          ("static", 2))
    )


_ZxAnEponOnuUniMacType_Type.__name__ = "Integer32"
_ZxAnEponOnuUniMacType_Object = MibTableColumn
zxAnEponOnuUniMacType = _ZxAnEponOnuUniMacType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 51, 1, 3),
    _ZxAnEponOnuUniMacType_Type()
)
zxAnEponOnuUniMacType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuUniMacType.setStatus("current")
_ZxAnEponOnuUniMacAddress_Type = MacAddress
_ZxAnEponOnuUniMacAddress_Object = MibTableColumn
zxAnEponOnuUniMacAddress = _ZxAnEponOnuUniMacAddress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 51, 1, 4),
    _ZxAnEponOnuUniMacAddress_Type()
)
zxAnEponOnuUniMacAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuUniMacAddress.setStatus("current")
_ZxAnEponOnuMgmtIpDHCPCfgTable_Object = MibTable
zxAnEponOnuMgmtIpDHCPCfgTable = _ZxAnEponOnuMgmtIpDHCPCfgTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 52)
)
if mibBuilder.loadTexts:
    zxAnEponOnuMgmtIpDHCPCfgTable.setStatus("current")
_ZxAnEponOnuMgmtIpDHCPCfgEntry_Object = MibTableRow
zxAnEponOnuMgmtIpDHCPCfgEntry = _ZxAnEponOnuMgmtIpDHCPCfgEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 52, 1)
)
zxAnEponOnuMgmtIpDHCPCfgEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuMgmtIpDHCPCfgEntry.setStatus("current")


class _ZxAnEponOnuMgmtIpDHCPCfgVlan_Type(Integer32):
    """Custom type zxAnEponOnuMgmtIpDHCPCfgVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponOnuMgmtIpDHCPCfgVlan_Type.__name__ = "Integer32"
_ZxAnEponOnuMgmtIpDHCPCfgVlan_Object = MibTableColumn
zxAnEponOnuMgmtIpDHCPCfgVlan = _ZxAnEponOnuMgmtIpDHCPCfgVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 52, 1, 1),
    _ZxAnEponOnuMgmtIpDHCPCfgVlan_Type()
)
zxAnEponOnuMgmtIpDHCPCfgVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMgmtIpDHCPCfgVlan.setStatus("current")


class _ZxAnEponOnuMgmtIpDHCPCfgPriority_Type(Integer32):
    """Custom type zxAnEponOnuMgmtIpDHCPCfgPriority based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnEponOnuMgmtIpDHCPCfgPriority_Type.__name__ = "Integer32"
_ZxAnEponOnuMgmtIpDHCPCfgPriority_Object = MibTableColumn
zxAnEponOnuMgmtIpDHCPCfgPriority = _ZxAnEponOnuMgmtIpDHCPCfgPriority_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 52, 1, 2),
    _ZxAnEponOnuMgmtIpDHCPCfgPriority_Type()
)
zxAnEponOnuMgmtIpDHCPCfgPriority.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMgmtIpDHCPCfgPriority.setStatus("current")


class _ZxAnEponOnuMgmtIpDHCPCfgEnableState_Type(Integer32):
    """Custom type zxAnEponOnuMgmtIpDHCPCfgEnableState based on Integer32"""
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


_ZxAnEponOnuMgmtIpDHCPCfgEnableState_Type.__name__ = "Integer32"
_ZxAnEponOnuMgmtIpDHCPCfgEnableState_Object = MibTableColumn
zxAnEponOnuMgmtIpDHCPCfgEnableState = _ZxAnEponOnuMgmtIpDHCPCfgEnableState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 52, 1, 3),
    _ZxAnEponOnuMgmtIpDHCPCfgEnableState_Type()
)
zxAnEponOnuMgmtIpDHCPCfgEnableState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuMgmtIpDHCPCfgEnableState.setStatus("current")


class _ZxAnEponOnuMgmtIpDHCPCfgState_Type(Integer32):
    """Custom type zxAnEponOnuMgmtIpDHCPCfgState based on Integer32"""
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
              7)
        )
    )
    namedValues = NamedValues(
        *(("init", 0),
          ("selecting", 1),
          ("requesting", 2),
          ("init-reboot", 3),
          ("rebooting", 4),
          ("bound", 5),
          ("renewing", 6),
          ("rebinding", 7))
    )


_ZxAnEponOnuMgmtIpDHCPCfgState_Type.__name__ = "Integer32"
_ZxAnEponOnuMgmtIpDHCPCfgState_Object = MibTableColumn
zxAnEponOnuMgmtIpDHCPCfgState = _ZxAnEponOnuMgmtIpDHCPCfgState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 52, 1, 4),
    _ZxAnEponOnuMgmtIpDHCPCfgState_Type()
)
zxAnEponOnuMgmtIpDHCPCfgState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuMgmtIpDHCPCfgState.setStatus("current")
_ZxAnEponRmOnuWanMgmt_ObjectIdentity = ObjectIdentity
zxAnEponRmOnuWanMgmt = _ZxAnEponRmOnuWanMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53)
)
_ZxAnEponRmWanPrfTable_Object = MibTable
zxAnEponRmWanPrfTable = _ZxAnEponRmWanPrfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2)
)
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfTable.setStatus("current")
_ZxAnEponRmWanPrfEntry_Object = MibTableRow
zxAnEponRmWanPrfEntry = _ZxAnEponRmWanPrfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1)
)
zxAnEponRmWanPrfEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmWanPrfName"),
)
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfEntry.setStatus("current")


class _ZxAnEponRmWanPrfName_Type(DisplayString):
    """Custom type zxAnEponRmWanPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmWanPrfName_Type.__name__ = "DisplayString"
_ZxAnEponRmWanPrfName_Object = MibTableColumn
zxAnEponRmWanPrfName = _ZxAnEponRmWanPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 1),
    _ZxAnEponRmWanPrfName_Type()
)
zxAnEponRmWanPrfName.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfName.setStatus("current")


class _ZxAnEponRmWanPrfWorkMode_Type(Integer32):
    """Custom type zxAnEponRmWanPrfWorkMode based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("bridge", 1),
          ("route", 2))
    )


_ZxAnEponRmWanPrfWorkMode_Type.__name__ = "Integer32"
_ZxAnEponRmWanPrfWorkMode_Object = MibTableColumn
zxAnEponRmWanPrfWorkMode = _ZxAnEponRmWanPrfWorkMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 2),
    _ZxAnEponRmWanPrfWorkMode_Type()
)
zxAnEponRmWanPrfWorkMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfWorkMode.setStatus("current")


class _ZxAnEponRmWanPrfSrvType_Type(Bits):
    """Custom type zxAnEponRmWanPrfSrvType based on Bits"""
    namedValues = NamedValues(
        *(("internet", 0),
          ("tr069", 1),
          ("voip", 2),
          ("other", 3))
    )

_ZxAnEponRmWanPrfSrvType_Type.__name__ = "Bits"
_ZxAnEponRmWanPrfSrvType_Object = MibTableColumn
zxAnEponRmWanPrfSrvType = _ZxAnEponRmWanPrfSrvType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 3),
    _ZxAnEponRmWanPrfSrvType_Type()
)
zxAnEponRmWanPrfSrvType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfSrvType.setStatus("current")


class _ZxAnEponRmWanPrfIpStackMode_Type(Integer32):
    """Custom type zxAnEponRmWanPrfIpStackMode based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("ipv4AndIpv6", 3))
    )


_ZxAnEponRmWanPrfIpStackMode_Type.__name__ = "Integer32"
_ZxAnEponRmWanPrfIpStackMode_Object = MibTableColumn
zxAnEponRmWanPrfIpStackMode = _ZxAnEponRmWanPrfIpStackMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 4),
    _ZxAnEponRmWanPrfIpStackMode_Type()
)
zxAnEponRmWanPrfIpStackMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfIpStackMode.setStatus("current")


class _ZxAnEponRmWanPrfNatNum_Type(Integer32):
    """Custom type zxAnEponRmWanPrfNatNum based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEponRmWanPrfNatNum_Type.__name__ = "Integer32"
_ZxAnEponRmWanPrfNatNum_Object = MibTableColumn
zxAnEponRmWanPrfNatNum = _ZxAnEponRmWanPrfNatNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 5),
    _ZxAnEponRmWanPrfNatNum_Type()
)
zxAnEponRmWanPrfNatNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfNatNum.setStatus("current")


class _ZxAnEponRmWanPrfTransTagMode_Type(Integer32):
    """Custom type zxAnEponRmWanPrfTransTagMode based on Integer32"""
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
        *(("transparent", 1),
          ("tagged", 2),
          ("untagged", 3))
    )


_ZxAnEponRmWanPrfTransTagMode_Type.__name__ = "Integer32"
_ZxAnEponRmWanPrfTransTagMode_Object = MibTableColumn
zxAnEponRmWanPrfTransTagMode = _ZxAnEponRmWanPrfTransTagMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 6),
    _ZxAnEponRmWanPrfTransTagMode_Type()
)
zxAnEponRmWanPrfTransTagMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfTransTagMode.setStatus("current")


class _ZxAnEponRmWanPrfTagTpid_Type(Integer32):
    """Custom type zxAnEponRmWanPrfTagTpid based on Integer32"""
    defaultValue = 33024

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnEponRmWanPrfTagTpid_Type.__name__ = "Integer32"
_ZxAnEponRmWanPrfTagTpid_Object = MibTableColumn
zxAnEponRmWanPrfTagTpid = _ZxAnEponRmWanPrfTagTpid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 7),
    _ZxAnEponRmWanPrfTagTpid_Type()
)
zxAnEponRmWanPrfTagTpid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfTagTpid.setStatus("current")


class _ZxAnEponRmWanPrfTagVid_Type(Integer32):
    """Custom type zxAnEponRmWanPrfTagVid based on Integer32"""
    defaultValue = 4092

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponRmWanPrfTagVid_Type.__name__ = "Integer32"
_ZxAnEponRmWanPrfTagVid_Object = MibTableColumn
zxAnEponRmWanPrfTagVid = _ZxAnEponRmWanPrfTagVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 8),
    _ZxAnEponRmWanPrfTagVid_Type()
)
zxAnEponRmWanPrfTagVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfTagVid.setStatus("current")


class _ZxAnEponRmWanPrfTagPrior_Type(Integer32):
    """Custom type zxAnEponRmWanPrfTagPrior based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 7),
    )


_ZxAnEponRmWanPrfTagPrior_Type.__name__ = "Integer32"
_ZxAnEponRmWanPrfTagPrior_Object = MibTableColumn
zxAnEponRmWanPrfTagPrior = _ZxAnEponRmWanPrfTagPrior_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 9),
    _ZxAnEponRmWanPrfTagPrior_Type()
)
zxAnEponRmWanPrfTagPrior.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfTagPrior.setStatus("current")


class _ZxAnEponRmWanPrfMaxTransUnit_Type(Integer32):
    """Custom type zxAnEponRmWanPrfMaxTransUnit based on Integer32"""
    defaultValue = 1522

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2000),
    )


_ZxAnEponRmWanPrfMaxTransUnit_Type.__name__ = "Integer32"
_ZxAnEponRmWanPrfMaxTransUnit_Object = MibTableColumn
zxAnEponRmWanPrfMaxTransUnit = _ZxAnEponRmWanPrfMaxTransUnit_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 10),
    _ZxAnEponRmWanPrfMaxTransUnit_Type()
)
zxAnEponRmWanPrfMaxTransUnit.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfMaxTransUnit.setStatus("current")


class _ZxAnEponRmWanPrfMVid_Type(Integer32):
    """Custom type zxAnEponRmWanPrfMVid based on Integer32"""
    defaultValue = 4096

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
        ValueRangeConstraint(4096, 4096),
    )


_ZxAnEponRmWanPrfMVid_Type.__name__ = "Integer32"
_ZxAnEponRmWanPrfMVid_Object = MibTableColumn
zxAnEponRmWanPrfMVid = _ZxAnEponRmWanPrfMVid_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 11),
    _ZxAnEponRmWanPrfMVid_Type()
)
zxAnEponRmWanPrfMVid.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfMVid.setStatus("current")


class _ZxAnEponRmWanPrfBindLanPortList_Type(Bits):
    """Custom type zxAnEponRmWanPrfBindLanPortList based on Bits"""
    namedValues = NamedValues(
        *(("lan1", 0),
          ("lan2", 1),
          ("lan3", 2),
          ("lan4", 3),
          ("lan5", 4),
          ("lan6", 5),
          ("lan7", 6),
          ("lan8", 7),
          ("lan9", 8),
          ("lan10", 9),
          ("lan11", 10),
          ("lan12", 11),
          ("lan13", 12),
          ("lan14", 13),
          ("lan15", 14),
          ("lan16", 15))
    )

_ZxAnEponRmWanPrfBindLanPortList_Type.__name__ = "Bits"
_ZxAnEponRmWanPrfBindLanPortList_Object = MibTableColumn
zxAnEponRmWanPrfBindLanPortList = _ZxAnEponRmWanPrfBindLanPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 12),
    _ZxAnEponRmWanPrfBindLanPortList_Type()
)
zxAnEponRmWanPrfBindLanPortList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfBindLanPortList.setStatus("current")


class _ZxAnEponRmWanPrfBindSsidList_Type(Bits):
    """Custom type zxAnEponRmWanPrfBindSsidList based on Bits"""
    namedValues = NamedValues(
        *(("ssid1", 0),
          ("ssid2", 1),
          ("ssid3", 2),
          ("ssid4", 3),
          ("ssid5", 4),
          ("ssid6", 5),
          ("ssid7", 6),
          ("ssid8", 7),
          ("ssid9", 8),
          ("ssid10", 9),
          ("ssid11", 10),
          ("ssid12", 11),
          ("ssid13", 12),
          ("ssid14", 13),
          ("ssid15", 14),
          ("ssid16", 15))
    )

_ZxAnEponRmWanPrfBindSsidList_Type.__name__ = "Bits"
_ZxAnEponRmWanPrfBindSsidList_Object = MibTableColumn
zxAnEponRmWanPrfBindSsidList = _ZxAnEponRmWanPrfBindSsidList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 13),
    _ZxAnEponRmWanPrfBindSsidList_Type()
)
zxAnEponRmWanPrfBindSsidList.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfBindSsidList.setStatus("current")
_ZxAnEponRmWanPrfRowStatus_Type = RowStatus
_ZxAnEponRmWanPrfRowStatus_Object = MibTableColumn
zxAnEponRmWanPrfRowStatus = _ZxAnEponRmWanPrfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 2, 1, 50),
    _ZxAnEponRmWanPrfRowStatus_Type()
)
zxAnEponRmWanPrfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmWanPrfRowStatus.setStatus("current")
_ZxAnEponRmOnuWanConfTable_Object = MibTable
zxAnEponRmOnuWanConfTable = _ZxAnEponRmOnuWanConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3)
)
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanConfTable.setStatus("current")
_ZxAnEponRmOnuWanConfEntry_Object = MibTableRow
zxAnEponRmOnuWanConfEntry = _ZxAnEponRmOnuWanConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1)
)
zxAnEponRmOnuWanConfEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmOnuWanPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanConfEntry.setStatus("current")


class _ZxAnEponRmOnuWanPortId_Type(Integer32):
    """Custom type zxAnEponRmOnuWanPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 8),
    )


_ZxAnEponRmOnuWanPortId_Type.__name__ = "Integer32"
_ZxAnEponRmOnuWanPortId_Object = MibTableColumn
zxAnEponRmOnuWanPortId = _ZxAnEponRmOnuWanPortId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 1),
    _ZxAnEponRmOnuWanPortId_Type()
)
zxAnEponRmOnuWanPortId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanPortId.setStatus("current")


class _ZxAnEponRmOnuWanPrfName_Type(DisplayString):
    """Custom type zxAnEponRmOnuWanPrfName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 32),
    )


_ZxAnEponRmOnuWanPrfName_Type.__name__ = "DisplayString"
_ZxAnEponRmOnuWanPrfName_Object = MibTableColumn
zxAnEponRmOnuWanPrfName = _ZxAnEponRmOnuWanPrfName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 2),
    _ZxAnEponRmOnuWanPrfName_Type()
)
zxAnEponRmOnuWanPrfName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanPrfName.setStatus("current")


class _ZxAnEponRmOnuWanIpAllocationMode_Type(Integer32):
    """Custom type zxAnEponRmOnuWanIpAllocationMode based on Integer32"""
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
        *(("static", 1),
          ("dhcp", 2),
          ("pppoe", 3))
    )


_ZxAnEponRmOnuWanIpAllocationMode_Type.__name__ = "Integer32"
_ZxAnEponRmOnuWanIpAllocationMode_Object = MibTableColumn
zxAnEponRmOnuWanIpAllocationMode = _ZxAnEponRmOnuWanIpAllocationMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 3),
    _ZxAnEponRmOnuWanIpAllocationMode_Type()
)
zxAnEponRmOnuWanIpAllocationMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanIpAllocationMode.setStatus("current")
_ZxAnEponRmOnuWanIpAddr_Type = IpAddress
_ZxAnEponRmOnuWanIpAddr_Object = MibTableColumn
zxAnEponRmOnuWanIpAddr = _ZxAnEponRmOnuWanIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 4),
    _ZxAnEponRmOnuWanIpAddr_Type()
)
zxAnEponRmOnuWanIpAddr.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanIpAddr.setStatus("current")
_ZxAnEponRmOnuWanIpMask_Type = IpAddress
_ZxAnEponRmOnuWanIpMask_Object = MibTableColumn
zxAnEponRmOnuWanIpMask = _ZxAnEponRmOnuWanIpMask_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 5),
    _ZxAnEponRmOnuWanIpMask_Type()
)
zxAnEponRmOnuWanIpMask.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanIpMask.setStatus("current")
_ZxAnEponRmOnuWanIpGateway_Type = IpAddress
_ZxAnEponRmOnuWanIpGateway_Object = MibTableColumn
zxAnEponRmOnuWanIpGateway = _ZxAnEponRmOnuWanIpGateway_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 6),
    _ZxAnEponRmOnuWanIpGateway_Type()
)
zxAnEponRmOnuWanIpGateway.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanIpGateway.setStatus("current")
_ZxAnEponRmOnuWanPriDnsSvrIp_Type = IpAddress
_ZxAnEponRmOnuWanPriDnsSvrIp_Object = MibTableColumn
zxAnEponRmOnuWanPriDnsSvrIp = _ZxAnEponRmOnuWanPriDnsSvrIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 7),
    _ZxAnEponRmOnuWanPriDnsSvrIp_Type()
)
zxAnEponRmOnuWanPriDnsSvrIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanPriDnsSvrIp.setStatus("current")
_ZxAnEponRmOnuWanSecDnsSvrIp_Type = IpAddress
_ZxAnEponRmOnuWanSecDnsSvrIp_Object = MibTableColumn
zxAnEponRmOnuWanSecDnsSvrIp = _ZxAnEponRmOnuWanSecDnsSvrIp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 8),
    _ZxAnEponRmOnuWanSecDnsSvrIp_Type()
)
zxAnEponRmOnuWanSecDnsSvrIp.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanSecDnsSvrIp.setStatus("current")


class _ZxAnEponRmOnuWanPppoeAuthMode_Type(Integer32):
    """Custom type zxAnEponRmOnuWanPppoeAuthMode based on Integer32"""
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
        *(("auto", 1),
          ("chap", 2),
          ("pap", 3))
    )


_ZxAnEponRmOnuWanPppoeAuthMode_Type.__name__ = "Integer32"
_ZxAnEponRmOnuWanPppoeAuthMode_Object = MibTableColumn
zxAnEponRmOnuWanPppoeAuthMode = _ZxAnEponRmOnuWanPppoeAuthMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 9),
    _ZxAnEponRmOnuWanPppoeAuthMode_Type()
)
zxAnEponRmOnuWanPppoeAuthMode.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanPppoeAuthMode.setStatus("current")


class _ZxAnEponRmOnuWanPppoeUserName_Type(DisplayString):
    """Custom type zxAnEponRmOnuWanPppoeUserName based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnEponRmOnuWanPppoeUserName_Type.__name__ = "DisplayString"
_ZxAnEponRmOnuWanPppoeUserName_Object = MibTableColumn
zxAnEponRmOnuWanPppoeUserName = _ZxAnEponRmOnuWanPppoeUserName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 10),
    _ZxAnEponRmOnuWanPppoeUserName_Type()
)
zxAnEponRmOnuWanPppoeUserName.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanPppoeUserName.setStatus("current")


class _ZxAnEponRmOnuWanPppoePassword_Type(DisplayString):
    """Custom type zxAnEponRmOnuWanPppoePassword based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_ZxAnEponRmOnuWanPppoePassword_Type.__name__ = "DisplayString"
_ZxAnEponRmOnuWanPppoePassword_Object = MibTableColumn
zxAnEponRmOnuWanPppoePassword = _ZxAnEponRmOnuWanPppoePassword_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 11),
    _ZxAnEponRmOnuWanPppoePassword_Type()
)
zxAnEponRmOnuWanPppoePassword.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanPppoePassword.setStatus("current")


class _ZxAnEponRmOnuWanPppoePrxyNum_Type(Integer32):
    """Custom type zxAnEponRmOnuWanPppoePrxyNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEponRmOnuWanPppoePrxyNum_Type.__name__ = "Integer32"
_ZxAnEponRmOnuWanPppoePrxyNum_Object = MibTableColumn
zxAnEponRmOnuWanPppoePrxyNum = _ZxAnEponRmOnuWanPppoePrxyNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 12),
    _ZxAnEponRmOnuWanPppoePrxyNum_Type()
)
zxAnEponRmOnuWanPppoePrxyNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanPppoePrxyNum.setStatus("current")


class _ZxAnEponRmOnuWanPppoePrxyUserNum_Type(Integer32):
    """Custom type zxAnEponRmOnuWanPppoePrxyUserNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_ZxAnEponRmOnuWanPppoePrxyUserNum_Type.__name__ = "Integer32"
_ZxAnEponRmOnuWanPppoePrxyUserNum_Object = MibTableColumn
zxAnEponRmOnuWanPppoePrxyUserNum = _ZxAnEponRmOnuWanPppoePrxyUserNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 13),
    _ZxAnEponRmOnuWanPppoePrxyUserNum_Type()
)
zxAnEponRmOnuWanPppoePrxyUserNum.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanPppoePrxyUserNum.setStatus("current")


class _ZxAnEponRmOnuWanPortUpTime_Type(Unsigned32):
    """Custom type zxAnEponRmOnuWanPortUpTime based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ZxAnEponRmOnuWanPortUpTime_Type.__name__ = "Unsigned32"
_ZxAnEponRmOnuWanPortUpTime_Object = MibTableColumn
zxAnEponRmOnuWanPortUpTime = _ZxAnEponRmOnuWanPortUpTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 14),
    _ZxAnEponRmOnuWanPortUpTime_Type()
)
zxAnEponRmOnuWanPortUpTime.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanPortUpTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanPortUpTime.setUnits("Seconds")
_ZxAnEponRmOnuWanConfRowStatus_Type = RowStatus
_ZxAnEponRmOnuWanConfRowStatus_Object = MibTableColumn
zxAnEponRmOnuWanConfRowStatus = _ZxAnEponRmOnuWanConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 3, 1, 50),
    _ZxAnEponRmOnuWanConfRowStatus_Type()
)
zxAnEponRmOnuWanConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanConfRowStatus.setStatus("current")
_ZxAnEponRmOnuWanGlobalConfTable_Object = MibTable
zxAnEponRmOnuWanGlobalConfTable = _ZxAnEponRmOnuWanGlobalConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 4)
)
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanGlobalConfTable.setStatus("current")
_ZxAnEponRmOnuWanGlobalConfEntry_Object = MibTableRow
zxAnEponRmOnuWanGlobalConfEntry = _ZxAnEponRmOnuWanGlobalConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 4, 1)
)
zxAnEponRmOnuWanGlobalConfEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanGlobalConfEntry.setStatus("current")


class _ZxAnEponRmOnuWanGlbMaxUserNum_Type(Integer32):
    """Custom type zxAnEponRmOnuWanGlbMaxUserNum based on Integer32"""
    defaultValue = 254

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 255),
    )


_ZxAnEponRmOnuWanGlbMaxUserNum_Type.__name__ = "Integer32"
_ZxAnEponRmOnuWanGlbMaxUserNum_Object = MibTableColumn
zxAnEponRmOnuWanGlbMaxUserNum = _ZxAnEponRmOnuWanGlbMaxUserNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 53, 4, 1, 1),
    _ZxAnEponRmOnuWanGlbMaxUserNum_Type()
)
zxAnEponRmOnuWanGlbMaxUserNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponRmOnuWanGlbMaxUserNum.setStatus("current")
_ZxAnEponOnuPowerSavingMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuPowerSavingMgmt = _ZxAnEponOnuPowerSavingMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55)
)
_ZxAnEponOnuPowerSavingTable_Object = MibTable
zxAnEponOnuPowerSavingTable = _ZxAnEponOnuPowerSavingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuPowerSavingTable.setStatus("current")
_ZxAnEponOnuPowerSavingEntry_Object = MibTableRow
zxAnEponOnuPowerSavingEntry = _ZxAnEponOnuPowerSavingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55, 2, 1)
)
zxAnEponOnuPowerSavingEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuPowerSavingEntry.setStatus("current")


class _ZxAnEponOnuPwrSaveEnable_Type(Integer32):
    """Custom type zxAnEponOnuPwrSaveEnable based on Integer32"""
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


_ZxAnEponOnuPwrSaveEnable_Type.__name__ = "Integer32"
_ZxAnEponOnuPwrSaveEnable_Object = MibTableColumn
zxAnEponOnuPwrSaveEnable = _ZxAnEponOnuPwrSaveEnable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55, 2, 1, 1),
    _ZxAnEponOnuPwrSaveEnable_Type()
)
zxAnEponOnuPwrSaveEnable.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveEnable.setStatus("current")


class _ZxAnEponOnuPwrSaveSleepMode_Type(Bits):
    """Custom type zxAnEponOnuPwrSaveSleepMode based on Bits"""
    namedValues = NamedValues(
        *(("tx", 0),
          ("trx", 1))
    )

_ZxAnEponOnuPwrSaveSleepMode_Type.__name__ = "Bits"
_ZxAnEponOnuPwrSaveSleepMode_Object = MibTableColumn
zxAnEponOnuPwrSaveSleepMode = _ZxAnEponOnuPwrSaveSleepMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55, 2, 1, 2),
    _ZxAnEponOnuPwrSaveSleepMode_Type()
)
zxAnEponOnuPwrSaveSleepMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveSleepMode.setStatus("current")


class _ZxAnEponOnuPwrSaveSleepConfMode_Type(Integer32):
    """Custom type zxAnEponOnuPwrSaveSleepConfMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tx", 1),
          ("trx", 2))
    )


_ZxAnEponOnuPwrSaveSleepConfMode_Type.__name__ = "Integer32"
_ZxAnEponOnuPwrSaveSleepConfMode_Object = MibTableColumn
zxAnEponOnuPwrSaveSleepConfMode = _ZxAnEponOnuPwrSaveSleepConfMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55, 2, 1, 3),
    _ZxAnEponOnuPwrSaveSleepConfMode_Type()
)
zxAnEponOnuPwrSaveSleepConfMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveSleepConfMode.setStatus("current")


class _ZxAnEponOnuPwrSaveEarlyWakeUp_Type(Integer32):
    """Custom type zxAnEponOnuPwrSaveEarlyWakeUp based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("supported", 1),
          ("unsupported", 2))
    )


_ZxAnEponOnuPwrSaveEarlyWakeUp_Type.__name__ = "Integer32"
_ZxAnEponOnuPwrSaveEarlyWakeUp_Object = MibTableColumn
zxAnEponOnuPwrSaveEarlyWakeUp = _ZxAnEponOnuPwrSaveEarlyWakeUp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55, 2, 1, 4),
    _ZxAnEponOnuPwrSaveEarlyWakeUp_Type()
)
zxAnEponOnuPwrSaveEarlyWakeUp.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveEarlyWakeUp.setStatus("current")


class _ZxAnEponOnuPwrSaveEarlyWakeUpEn_Type(Integer32):
    """Custom type zxAnEponOnuPwrSaveEarlyWakeUpEn based on Integer32"""
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


_ZxAnEponOnuPwrSaveEarlyWakeUpEn_Type.__name__ = "Integer32"
_ZxAnEponOnuPwrSaveEarlyWakeUpEn_Object = MibTableColumn
zxAnEponOnuPwrSaveEarlyWakeUpEn = _ZxAnEponOnuPwrSaveEarlyWakeUpEn_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55, 2, 1, 5),
    _ZxAnEponOnuPwrSaveEarlyWakeUpEn_Type()
)
zxAnEponOnuPwrSaveEarlyWakeUpEn.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveEarlyWakeUpEn.setStatus("current")


class _ZxAnEponOnuPwrSaveSleepDuration_Type(Integer32):
    """Custom type zxAnEponOnuPwrSaveSleepDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62500000),
    )


_ZxAnEponOnuPwrSaveSleepDuration_Type.__name__ = "Integer32"
_ZxAnEponOnuPwrSaveSleepDuration_Object = MibTableColumn
zxAnEponOnuPwrSaveSleepDuration = _ZxAnEponOnuPwrSaveSleepDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55, 2, 1, 6),
    _ZxAnEponOnuPwrSaveSleepDuration_Type()
)
zxAnEponOnuPwrSaveSleepDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveSleepDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveSleepDuration.setUnits("TQ")


class _ZxAnEponOnuPwrSaveWakeUpDuration_Type(Integer32):
    """Custom type zxAnEponOnuPwrSaveWakeUpDuration based on Integer32"""
    defaultValue = 0

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 62500000),
    )


_ZxAnEponOnuPwrSaveWakeUpDuration_Type.__name__ = "Integer32"
_ZxAnEponOnuPwrSaveWakeUpDuration_Object = MibTableColumn
zxAnEponOnuPwrSaveWakeUpDuration = _ZxAnEponOnuPwrSaveWakeUpDuration_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55, 2, 1, 7),
    _ZxAnEponOnuPwrSaveWakeUpDuration_Type()
)
zxAnEponOnuPwrSaveWakeUpDuration.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveWakeUpDuration.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveWakeUpDuration.setUnits("TQ")


class _ZxAnEponOnuPwrSaveMaxRefreshTime_Type(Unsigned32):
    """Custom type zxAnEponOnuPwrSaveMaxRefreshTime based on Unsigned32"""
    defaultValue = 8000

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4294967295),
    )


_ZxAnEponOnuPwrSaveMaxRefreshTime_Type.__name__ = "Unsigned32"
_ZxAnEponOnuPwrSaveMaxRefreshTime_Object = MibTableColumn
zxAnEponOnuPwrSaveMaxRefreshTime = _ZxAnEponOnuPwrSaveMaxRefreshTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 55, 2, 1, 8),
    _ZxAnEponOnuPwrSaveMaxRefreshTime_Type()
)
zxAnEponOnuPwrSaveMaxRefreshTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveMaxRefreshTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponOnuPwrSaveMaxRefreshTime.setUnits("125Microseconds")
_ZxAnEponOnuProtectMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuProtectMgmt = _ZxAnEponOnuProtectMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 56)
)
_ZxAnOnuProtectConfTable_Object = MibTable
zxAnOnuProtectConfTable = _ZxAnOnuProtectConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 56, 56)
)
if mibBuilder.loadTexts:
    zxAnOnuProtectConfTable.setStatus("current")
_ZxAnOnuProtectConfEntry_Object = MibTableRow
zxAnOnuProtectConfEntry = _ZxAnOnuProtectConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 56, 56, 1)
)
zxAnOnuProtectConfEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnOnuProtectConfEntry.setStatus("current")


class _ZxAnOnuProtectLosTimeByOptSignal_Type(Integer32):
    """Custom type zxAnOnuProtectLosTimeByOptSignal based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnOnuProtectLosTimeByOptSignal_Type.__name__ = "Integer32"
_ZxAnOnuProtectLosTimeByOptSignal_Object = MibTableColumn
zxAnOnuProtectLosTimeByOptSignal = _ZxAnOnuProtectLosTimeByOptSignal_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 56, 56, 1, 1),
    _ZxAnOnuProtectLosTimeByOptSignal_Type()
)
zxAnOnuProtectLosTimeByOptSignal.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOnuProtectLosTimeByOptSignal.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOnuProtectLosTimeByOptSignal.setUnits("Milliseconds")


class _ZxAnOnuProtectLosTimeByMpcp_Type(Integer32):
    """Custom type zxAnOnuProtectLosTimeByMpcp based on Integer32"""
    defaultValue = 55

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 65535),
    )


_ZxAnOnuProtectLosTimeByMpcp_Type.__name__ = "Integer32"
_ZxAnOnuProtectLosTimeByMpcp_Object = MibTableColumn
zxAnOnuProtectLosTimeByMpcp = _ZxAnOnuProtectLosTimeByMpcp_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 1, 56, 56, 1, 2),
    _ZxAnOnuProtectLosTimeByMpcp_Type()
)
zxAnOnuProtectLosTimeByMpcp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnOnuProtectLosTimeByMpcp.setStatus("current")
if mibBuilder.loadTexts:
    zxAnOnuProtectLosTimeByMpcp.setUnits("Milliseconds")
_ZxAnEponOnuExtendedActionMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuExtendedActionMgmt = _ZxAnEponOnuExtendedActionMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2)
)
_ZxAnEponOnuActionTable_Object = MibTable
zxAnEponOnuActionTable = _ZxAnEponOnuActionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuActionTable.setStatus("current")
_ZxAnEponOnuActionEntry_Object = MibTableRow
zxAnEponOnuActionEntry = _ZxAnEponOnuActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 1, 1)
)
zxAnEponOnuActionEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuActionEntry.setStatus("current")


class _ZxAnEponOnuAction_Type(Integer32):
    """Custom type zxAnEponOnuAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("reset", 1)
    )


_ZxAnEponOnuAction_Type.__name__ = "Integer32"
_ZxAnEponOnuAction_Object = MibTableColumn
zxAnEponOnuAction = _ZxAnEponOnuAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 1, 1, 1),
    _ZxAnEponOnuAction_Type()
)
zxAnEponOnuAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuAction.setStatus("current")
_ZxAnEponOnuSaveActionTable_Object = MibTable
zxAnEponOnuSaveActionTable = _ZxAnEponOnuSaveActionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuSaveActionTable.setStatus("current")
_ZxAnEponOnuSaveActionEntry_Object = MibTableRow
zxAnEponOnuSaveActionEntry = _ZxAnEponOnuSaveActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 2, 1)
)
zxAnEponOnuSaveActionEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuSaveActionEntry.setStatus("current")


class _ZxAnEponOnuSaveAction_Type(Integer32):
    """Custom type zxAnEponOnuSaveAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("save", 1),
          ("clear", 2),
          ("restoreFactory", 3))
    )


_ZxAnEponOnuSaveAction_Type.__name__ = "Integer32"
_ZxAnEponOnuSaveAction_Object = MibTableColumn
zxAnEponOnuSaveAction = _ZxAnEponOnuSaveAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 2, 1, 1),
    _ZxAnEponOnuSaveAction_Type()
)
zxAnEponOnuSaveAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuSaveAction.setStatus("current")
_ZxAnEponOnuSetHGMACCodeTable_Object = MibTable
zxAnEponOnuSetHGMACCodeTable = _ZxAnEponOnuSetHGMACCodeTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 3)
)
if mibBuilder.loadTexts:
    zxAnEponOnuSetHGMACCodeTable.setStatus("current")
_ZxAnEponOnuSetHGMACCodeEntry_Object = MibTableRow
zxAnEponOnuSetHGMACCodeEntry = _ZxAnEponOnuSetHGMACCodeEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 3, 1)
)
zxAnEponOnuSetHGMACCodeEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuSetHGMACCodeEntry.setStatus("current")
_ZxAnEponOnuHGMACCode_Type = OctetString
_ZxAnEponOnuHGMACCode_Object = MibTableColumn
zxAnEponOnuHGMACCode = _ZxAnEponOnuHGMACCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 3, 1, 1),
    _ZxAnEponOnuHGMACCode_Type()
)
zxAnEponOnuHGMACCode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuHGMACCode.setStatus("current")
_ZxAnEponOnuHGMACVlanTable_Object = MibTable
zxAnEponOnuHGMACVlanTable = _ZxAnEponOnuHGMACVlanTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 4)
)
if mibBuilder.loadTexts:
    zxAnEponOnuHGMACVlanTable.setStatus("current")
_ZxAnEponOnuHGMACVlanEntry_Object = MibTableRow
zxAnEponOnuHGMACVlanEntry = _ZxAnEponOnuHGMACVlanEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 4, 1)
)
zxAnEponOnuHGMACVlanEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuHGMACVlanEntry.setStatus("current")


class _ZxAnEponOnuHGVlan_Type(Integer32):
    """Custom type zxAnEponOnuHGVlan based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponOnuHGVlan_Type.__name__ = "Integer32"
_ZxAnEponOnuHGVlan_Object = MibTableColumn
zxAnEponOnuHGVlan = _ZxAnEponOnuHGVlan_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 4, 1, 1),
    _ZxAnEponOnuHGVlan_Type()
)
zxAnEponOnuHGVlan.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuHGVlan.setStatus("current")
_ZxAnEponOnuHGStateTable_Object = MibTable
zxAnEponOnuHGStateTable = _ZxAnEponOnuHGStateTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 5)
)
if mibBuilder.loadTexts:
    zxAnEponOnuHGStateTable.setStatus("current")
_ZxAnEponOnuHGStateEntry_Object = MibTableRow
zxAnEponOnuHGStateEntry = _ZxAnEponOnuHGStateEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 5, 1)
)
zxAnEponOnuHGStateEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuHGStateEntry.setStatus("current")
_ZxAnEponOnuHGMAC_Type = MacAddress
_ZxAnEponOnuHGMAC_Object = MibTableColumn
zxAnEponOnuHGMAC = _ZxAnEponOnuHGMAC_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 5, 1, 1),
    _ZxAnEponOnuHGMAC_Type()
)
zxAnEponOnuHGMAC.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuHGMAC.setStatus("current")


class _ZxEponOnuHGState_Type(Integer32):
    """Custom type zxEponOnuHGState based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 1),
    )


_ZxEponOnuHGState_Type.__name__ = "Integer32"
_ZxEponOnuHGState_Object = MibTableColumn
zxEponOnuHGState = _ZxEponOnuHGState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 2, 5, 1, 2),
    _ZxEponOnuHGState_Type()
)
zxEponOnuHGState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxEponOnuHGState.setStatus("current")
_ZxAnEponOnuStdAttrMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuStdAttrMgmt = _ZxAnEponOnuStdAttrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3)
)
_ZxAnEponOnuPhyMgmtTable_Object = MibTable
zxAnEponOnuPhyMgmtTable = _ZxAnEponOnuPhyMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuPhyMgmtTable.setStatus("current")
_ZxAnEponOnuPhyMgmtEntry_Object = MibTableRow
zxAnEponOnuPhyMgmtEntry = _ZxAnEponOnuPhyMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 1, 1)
)
zxAnEponOnuPhyMgmtEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuPhyMgmtEntry.setStatus("current")


class _ZxAnEponOnuPhyAdminState_Type(Integer32):
    """Custom type zxAnEponOnuPhyAdminState based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ZxAnEponOnuPhyAdminState_Type.__name__ = "Integer32"
_ZxAnEponOnuPhyAdminState_Object = MibTableColumn
zxAnEponOnuPhyAdminState = _ZxAnEponOnuPhyAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 1, 1, 1),
    _ZxAnEponOnuPhyAdminState_Type()
)
zxAnEponOnuPhyAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuPhyAdminState.setStatus("current")
_ZxAnEponOnuAutoNegAttrTable_Object = MibTable
zxAnEponOnuAutoNegAttrTable = _ZxAnEponOnuAutoNegAttrTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuAutoNegAttrTable.setStatus("current")
_ZxAnEponOnuAutoNegAttrEntry_Object = MibTableRow
zxAnEponOnuAutoNegAttrEntry = _ZxAnEponOnuAutoNegAttrEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 2, 1)
)
zxAnEponOnuAutoNegAttrEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuAutoNegAttrEntry.setStatus("current")


class _ZxAnEponOnuAutoNegAdminState_Type(Integer32):
    """Custom type zxAnEponOnuAutoNegAdminState based on Integer32"""
    defaultValue = 2

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("disabled", 1),
          ("enabled", 2))
    )


_ZxAnEponOnuAutoNegAdminState_Type.__name__ = "Integer32"
_ZxAnEponOnuAutoNegAdminState_Object = MibTableColumn
zxAnEponOnuAutoNegAdminState = _ZxAnEponOnuAutoNegAdminState_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 2, 1, 1),
    _ZxAnEponOnuAutoNegAdminState_Type()
)
zxAnEponOnuAutoNegAdminState.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuAutoNegAdminState.setStatus("current")


class _ZxAnEponOnuAutoNegCapability_Type(Bits):
    """Custom type zxAnEponOnuAutoNegCapability based on Bits"""
    namedValues = NamedValues(
        *(("zx-GLOBAL", 0),
          ("zx-OTHER", 1),
          ("zx-UNKNOWN", 2),
          ("zx-10BASE-T", 3),
          ("zx-10BASE-TFD", 4),
          ("zx-100BASE-T4", 5),
          ("zx-100BASE-TX", 6),
          ("zx-100BASE-TXFD", 7),
          ("zx-FDX-PAUSE", 8),
          ("zx-FDX-APAUSE", 9),
          ("zx-FDX-SPAUSE", 10),
          ("zx-FDX-BPAUSE", 11),
          ("zx-100BASE-T2", 12),
          ("zx-100BASE-T2FD", 13),
          ("zx-1000BASE-X", 14),
          ("zx-1000BASE-XFD", 15),
          ("zx-1000BASE-T", 16),
          ("zx-1000BASE-TFD", 17),
          ("zx-REM-FAULT1", 18),
          ("zx-REM-FAULT2", 19),
          ("zx-ISO-ETHERNET", 20))
    )

_ZxAnEponOnuAutoNegCapability_Type.__name__ = "Bits"
_ZxAnEponOnuAutoNegCapability_Object = MibTableColumn
zxAnEponOnuAutoNegCapability = _ZxAnEponOnuAutoNegCapability_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 2, 1, 2),
    _ZxAnEponOnuAutoNegCapability_Type()
)
zxAnEponOnuAutoNegCapability.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuAutoNegCapability.setStatus("current")


class _ZxAnEponOnuAutoNegCapAdvertised_Type(Bits):
    """Custom type zxAnEponOnuAutoNegCapAdvertised based on Bits"""
    namedValues = NamedValues(
        *(("zx-GLOBAL", 0),
          ("zx-OTHER", 1),
          ("zx-UNKNOWN", 2),
          ("zx-10BASE-T", 3),
          ("zx-10BASE-TFD", 4),
          ("zx-100BASE-T4", 5),
          ("zx-100BASE-TX", 6),
          ("zx-100BASE-TXFD", 7),
          ("zx-FDX-PAUSE", 8),
          ("zx-FDX-APAUSE", 9),
          ("zx-FDX-SPAUSE", 10),
          ("zx-FDX-BPAUSE", 11),
          ("zx-100BASE-T2", 12),
          ("zx-100BASE-T2FD", 13),
          ("zx-1000BASE-X", 14),
          ("zx-1000BASE-XFD", 15),
          ("zx-1000BASE-T", 16),
          ("zx-1000BASE-TFD", 17),
          ("zx-REM-FAULT1", 18),
          ("zx-REM-FAULT2", 19),
          ("zx-ISO-ETHERNET", 20))
    )

_ZxAnEponOnuAutoNegCapAdvertised_Type.__name__ = "Bits"
_ZxAnEponOnuAutoNegCapAdvertised_Object = MibTableColumn
zxAnEponOnuAutoNegCapAdvertised = _ZxAnEponOnuAutoNegCapAdvertised_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 2, 1, 3),
    _ZxAnEponOnuAutoNegCapAdvertised_Type()
)
zxAnEponOnuAutoNegCapAdvertised.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuAutoNegCapAdvertised.setStatus("current")


class _ZxAnEponOnuEthIfConfDuplexSpeed_Type(Integer32):
    """Custom type zxAnEponOnuEthIfConfDuplexSpeed based on Integer32"""
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
              99)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 1),
          ("half-10", 2),
          ("full-10", 3),
          ("half-100", 4),
          ("full-100", 5),
          ("full-1000", 6),
          ("full-10000", 7),
          ("illegal", 99))
    )


_ZxAnEponOnuEthIfConfDuplexSpeed_Type.__name__ = "Integer32"
_ZxAnEponOnuEthIfConfDuplexSpeed_Object = MibTableColumn
zxAnEponOnuEthIfConfDuplexSpeed = _ZxAnEponOnuEthIfConfDuplexSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 2, 1, 4),
    _ZxAnEponOnuEthIfConfDuplexSpeed_Type()
)
zxAnEponOnuEthIfConfDuplexSpeed.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuEthIfConfDuplexSpeed.setStatus("current")


class _ZxAnEponOnuEthIfActualDuplex_Type(Integer32):
    """Custom type zxAnEponOnuEthIfActualDuplex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("auto-negotiate", 1),
          ("half", 2),
          ("full", 3))
    )


_ZxAnEponOnuEthIfActualDuplex_Type.__name__ = "Integer32"
_ZxAnEponOnuEthIfActualDuplex_Object = MibTableColumn
zxAnEponOnuEthIfActualDuplex = _ZxAnEponOnuEthIfActualDuplex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 2, 1, 5),
    _ZxAnEponOnuEthIfActualDuplex_Type()
)
zxAnEponOnuEthIfActualDuplex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuEthIfActualDuplex.setStatus("current")


class _ZxAnEponOnuEthIfActualSpeed_Type(Integer32):
    """Custom type zxAnEponOnuEthIfActualSpeed based on Integer32"""
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
        *(("speed-10", 1),
          ("speed-100", 2),
          ("speed-1000", 3),
          ("speed-10000", 4),
          ("auto-speed", 5))
    )


_ZxAnEponOnuEthIfActualSpeed_Type.__name__ = "Integer32"
_ZxAnEponOnuEthIfActualSpeed_Object = MibTableColumn
zxAnEponOnuEthIfActualSpeed = _ZxAnEponOnuEthIfActualSpeed_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 2, 1, 6),
    _ZxAnEponOnuEthIfActualSpeed_Type()
)
zxAnEponOnuEthIfActualSpeed.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuEthIfActualSpeed.setStatus("current")
_ZxAnEponOnuFecMgmtTable_Object = MibTable
zxAnEponOnuFecMgmtTable = _ZxAnEponOnuFecMgmtTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 3)
)
if mibBuilder.loadTexts:
    zxAnEponOnuFecMgmtTable.setStatus("current")
_ZxAnEponOnuFecMgmtEntry_Object = MibTableRow
zxAnEponOnuFecMgmtEntry = _ZxAnEponOnuFecMgmtEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 3, 1)
)
zxAnEponOnuFecMgmtEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuFecMgmtEntry.setStatus("current")


class _ZxAnEponOnuFecAbility_Type(Integer32):
    """Custom type zxAnEponOnuFecAbility based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("supported", 2),
          ("notsupported", 3))
    )


_ZxAnEponOnuFecAbility_Type.__name__ = "Integer32"
_ZxAnEponOnuFecAbility_Object = MibTableColumn
zxAnEponOnuFecAbility = _ZxAnEponOnuFecAbility_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 3, 1, 1),
    _ZxAnEponOnuFecAbility_Type()
)
zxAnEponOnuFecAbility.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuFecAbility.setStatus("current")


class _ZxAnEponOnuFecMode_Type(Integer32):
    """Custom type zxAnEponOnuFecMode based on Integer32"""
    defaultValue = 3

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("enabled", 2),
          ("disabled", 3))
    )


_ZxAnEponOnuFecMode_Type.__name__ = "Integer32"
_ZxAnEponOnuFecMode_Object = MibTableColumn
zxAnEponOnuFecMode = _ZxAnEponOnuFecMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 3, 3, 1, 2),
    _ZxAnEponOnuFecMode_Type()
)
zxAnEponOnuFecMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuFecMode.setStatus("current")
_ZxAnEponOnuStdActionMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuStdActionMgmt = _ZxAnEponOnuStdActionMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 4)
)
_ZxAnEponOnuAutoNegActionTable_Object = MibTable
zxAnEponOnuAutoNegActionTable = _ZxAnEponOnuAutoNegActionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 4, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuAutoNegActionTable.setStatus("current")
_ZxAnEponOnuAutoNegActionEntry_Object = MibTableRow
zxAnEponOnuAutoNegActionEntry = _ZxAnEponOnuAutoNegActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 4, 1, 1)
)
zxAnEponOnuAutoNegActionEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuAutoNegActionEntry.setStatus("current")


class _ZxAnEponOnuAutoNegAction_Type(Integer32):
    """Custom type zxAnEponOnuAutoNegAction based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restart", 1)
    )


_ZxAnEponOnuAutoNegAction_Type.__name__ = "Integer32"
_ZxAnEponOnuAutoNegAction_Object = MibTableColumn
zxAnEponOnuAutoNegAction = _ZxAnEponOnuAutoNegAction_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 4, 1, 1, 1),
    _ZxAnEponOnuAutoNegAction_Type()
)
zxAnEponOnuAutoNegAction.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuAutoNegAction.setStatus("current")
_ZxAnEponOnuDbaAttrMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuDbaAttrMgmt = _ZxAnEponOnuDbaAttrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5)
)
_ZxAnEponOnuDbaQueueThresholdsTable_Object = MibTable
zxAnEponOnuDbaQueueThresholdsTable = _ZxAnEponOnuDbaQueueThresholdsTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueThresholdsTable.setStatus("current")
_ZxAnEponOnuDbaQueueThresholdsEntry_Object = MibTableRow
zxAnEponOnuDbaQueueThresholdsEntry = _ZxAnEponOnuDbaQueueThresholdsEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1, 1)
)
zxAnEponOnuDbaQueueThresholdsEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuDbaQueueSetIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueThresholdsEntry.setStatus("current")


class _ZxAnEponOnuDbaQueueSetIndex_Type(Integer32):
    """Custom type zxAnEponOnuDbaQueueSetIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 3),
    )


_ZxAnEponOnuDbaQueueSetIndex_Type.__name__ = "Integer32"
_ZxAnEponOnuDbaQueueSetIndex_Object = MibTableColumn
zxAnEponOnuDbaQueueSetIndex = _ZxAnEponOnuDbaQueueSetIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1, 1, 1),
    _ZxAnEponOnuDbaQueueSetIndex_Type()
)
zxAnEponOnuDbaQueueSetIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueSetIndex.setStatus("current")
_ZxAnEponOnuDbaQueueThresholds1_Type = Integer32
_ZxAnEponOnuDbaQueueThresholds1_Object = MibTableColumn
zxAnEponOnuDbaQueueThresholds1 = _ZxAnEponOnuDbaQueueThresholds1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1, 1, 2),
    _ZxAnEponOnuDbaQueueThresholds1_Type()
)
zxAnEponOnuDbaQueueThresholds1.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueThresholds1.setStatus("current")
_ZxAnEponOnuDbaQueueThresholds2_Type = Integer32
_ZxAnEponOnuDbaQueueThresholds2_Object = MibTableColumn
zxAnEponOnuDbaQueueThresholds2 = _ZxAnEponOnuDbaQueueThresholds2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1, 1, 3),
    _ZxAnEponOnuDbaQueueThresholds2_Type()
)
zxAnEponOnuDbaQueueThresholds2.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueThresholds2.setStatus("current")
_ZxAnEponOnuDbaQueueThresholds3_Type = Integer32
_ZxAnEponOnuDbaQueueThresholds3_Object = MibTableColumn
zxAnEponOnuDbaQueueThresholds3 = _ZxAnEponOnuDbaQueueThresholds3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1, 1, 4),
    _ZxAnEponOnuDbaQueueThresholds3_Type()
)
zxAnEponOnuDbaQueueThresholds3.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueThresholds3.setStatus("current")
_ZxAnEponOnuDbaQueueThresholds4_Type = Integer32
_ZxAnEponOnuDbaQueueThresholds4_Object = MibTableColumn
zxAnEponOnuDbaQueueThresholds4 = _ZxAnEponOnuDbaQueueThresholds4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1, 1, 5),
    _ZxAnEponOnuDbaQueueThresholds4_Type()
)
zxAnEponOnuDbaQueueThresholds4.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueThresholds4.setStatus("current")
_ZxAnEponOnuDbaQueueThresholds5_Type = Integer32
_ZxAnEponOnuDbaQueueThresholds5_Object = MibTableColumn
zxAnEponOnuDbaQueueThresholds5 = _ZxAnEponOnuDbaQueueThresholds5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1, 1, 6),
    _ZxAnEponOnuDbaQueueThresholds5_Type()
)
zxAnEponOnuDbaQueueThresholds5.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueThresholds5.setStatus("current")
_ZxAnEponOnuDbaQueueThresholds6_Type = Integer32
_ZxAnEponOnuDbaQueueThresholds6_Object = MibTableColumn
zxAnEponOnuDbaQueueThresholds6 = _ZxAnEponOnuDbaQueueThresholds6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1, 1, 7),
    _ZxAnEponOnuDbaQueueThresholds6_Type()
)
zxAnEponOnuDbaQueueThresholds6.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueThresholds6.setStatus("current")
_ZxAnEponOnuDbaQueueThresholds7_Type = Integer32
_ZxAnEponOnuDbaQueueThresholds7_Object = MibTableColumn
zxAnEponOnuDbaQueueThresholds7 = _ZxAnEponOnuDbaQueueThresholds7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1, 1, 8),
    _ZxAnEponOnuDbaQueueThresholds7_Type()
)
zxAnEponOnuDbaQueueThresholds7.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueThresholds7.setStatus("current")
_ZxAnEponOnuDbaQueueThresholds8_Type = Integer32
_ZxAnEponOnuDbaQueueThresholds8_Object = MibTableColumn
zxAnEponOnuDbaQueueThresholds8 = _ZxAnEponOnuDbaQueueThresholds8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 1, 1, 9),
    _ZxAnEponOnuDbaQueueThresholds8_Type()
)
zxAnEponOnuDbaQueueThresholds8.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueThresholds8.setStatus("current")
_ZxAnEponOnuDbaQueueSetActiveTable_Object = MibTable
zxAnEponOnuDbaQueueSetActiveTable = _ZxAnEponOnuDbaQueueSetActiveTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 2)
)
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueSetActiveTable.setStatus("current")
_ZxAnEponOnuDbaQueueSetActiveEntry_Object = MibTableRow
zxAnEponOnuDbaQueueSetActiveEntry = _ZxAnEponOnuDbaQueueSetActiveEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 2, 1)
)
zxAnEponOnuDbaQueueSetActiveEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueSetActiveEntry.setStatus("current")
_ZxAnEponOnuDbaQueueSetList_Type = OctetString
_ZxAnEponOnuDbaQueueSetList_Object = MibTableColumn
zxAnEponOnuDbaQueueSetList = _ZxAnEponOnuDbaQueueSetList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 5, 2, 1, 1),
    _ZxAnEponOnuDbaQueueSetList_Type()
)
zxAnEponOnuDbaQueueSetList.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuDbaQueueSetList.setStatus("current")
_ZxAnEponOnuProfileMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuProfileMgmt = _ZxAnEponOnuProfileMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 6)
)
_ZxAnEponOnuProfileIndexNextTable_Object = MibTable
zxAnEponOnuProfileIndexNextTable = _ZxAnEponOnuProfileIndexNextTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 6, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuProfileIndexNextTable.setStatus("current")
_ZxAnEponOnuProfileIndexNextEntry_Object = MibTableRow
zxAnEponOnuProfileIndexNextEntry = _ZxAnEponOnuProfileIndexNextEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 6, 1, 1)
)
zxAnEponOnuProfileIndexNextEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuProfileIndexNextEntry.setStatus("current")
_ZxAnEponOnuClassMarkingConditionIdNext_Type = Integer32
_ZxAnEponOnuClassMarkingConditionIdNext_Object = MibTableColumn
zxAnEponOnuClassMarkingConditionIdNext = _ZxAnEponOnuClassMarkingConditionIdNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 6, 1, 1, 1),
    _ZxAnEponOnuClassMarkingConditionIdNext_Type()
)
zxAnEponOnuClassMarkingConditionIdNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingConditionIdNext.setStatus("current")
_ZxAnEponOnuClassMarkingRuleIdNext_Type = Integer32
_ZxAnEponOnuClassMarkingRuleIdNext_Object = MibTableColumn
zxAnEponOnuClassMarkingRuleIdNext = _ZxAnEponOnuClassMarkingRuleIdNext_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 6, 1, 1, 2),
    _ZxAnEponOnuClassMarkingRuleIdNext_Type()
)
zxAnEponOnuClassMarkingRuleIdNext.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuClassMarkingRuleIdNext.setStatus("current")
_ZxAnEponOnuPfmncStatis_ObjectIdentity = ObjectIdentity
zxAnEponOnuPfmncStatis = _ZxAnEponOnuPfmncStatis_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7)
)
_ZxAnEponOnuPfmncStatisTable_Object = MibTable
zxAnEponOnuPfmncStatisTable = _ZxAnEponOnuPfmncStatisTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1)
)
if mibBuilder.loadTexts:
    zxAnEponOnuPfmncStatisTable.setStatus("current")
_ZxAnEponOnuPfmncStatisEntry_Object = MibTableRow
zxAnEponOnuPfmncStatisEntry = _ZxAnEponOnuPfmncStatisEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1)
)
zxAnEponOnuPfmncStatisEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "portType"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuPfmncStatisEntry.setStatus("current")


class _PortType_Type(Integer32):
    """Custom type portType based on Integer32"""
    defaultValue = 0


_PortType_Type.__name__ = "Integer32"
_PortType_Object = MibTableColumn
portType = _PortType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 1),
    _PortType_Type()
)
portType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    portType.setStatus("current")
_Parameter1_Type = Counter64
_Parameter1_Object = MibTableColumn
parameter1 = _Parameter1_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 2),
    _Parameter1_Type()
)
parameter1.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter1.setStatus("current")
_Parameter2_Type = Counter64
_Parameter2_Object = MibTableColumn
parameter2 = _Parameter2_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 3),
    _Parameter2_Type()
)
parameter2.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter2.setStatus("current")
_Parameter3_Type = Counter64
_Parameter3_Object = MibTableColumn
parameter3 = _Parameter3_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 4),
    _Parameter3_Type()
)
parameter3.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter3.setStatus("current")
_Parameter4_Type = Counter64
_Parameter4_Object = MibTableColumn
parameter4 = _Parameter4_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 5),
    _Parameter4_Type()
)
parameter4.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter4.setStatus("current")
_Parameter5_Type = Counter64
_Parameter5_Object = MibTableColumn
parameter5 = _Parameter5_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 6),
    _Parameter5_Type()
)
parameter5.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter5.setStatus("current")
_Parameter6_Type = Counter64
_Parameter6_Object = MibTableColumn
parameter6 = _Parameter6_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 7),
    _Parameter6_Type()
)
parameter6.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter6.setStatus("current")
_Parameter7_Type = Counter64
_Parameter7_Object = MibTableColumn
parameter7 = _Parameter7_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 8),
    _Parameter7_Type()
)
parameter7.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter7.setStatus("current")
_Parameter8_Type = Counter64
_Parameter8_Object = MibTableColumn
parameter8 = _Parameter8_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 9),
    _Parameter8_Type()
)
parameter8.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter8.setStatus("current")
_Parameter9_Type = Counter64
_Parameter9_Object = MibTableColumn
parameter9 = _Parameter9_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 10),
    _Parameter9_Type()
)
parameter9.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter9.setStatus("current")
_Parameter10_Type = Counter64
_Parameter10_Object = MibTableColumn
parameter10 = _Parameter10_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 11),
    _Parameter10_Type()
)
parameter10.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter10.setStatus("current")
_Parameter11_Type = Counter64
_Parameter11_Object = MibTableColumn
parameter11 = _Parameter11_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 12),
    _Parameter11_Type()
)
parameter11.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter11.setStatus("current")
_Parameter12_Type = Counter64
_Parameter12_Object = MibTableColumn
parameter12 = _Parameter12_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 13),
    _Parameter12_Type()
)
parameter12.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter12.setStatus("current")
_Parameter13_Type = Counter64
_Parameter13_Object = MibTableColumn
parameter13 = _Parameter13_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 1, 1, 14),
    _Parameter13_Type()
)
parameter13.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    parameter13.setStatus("current")
_ZxAnEponRmPerfConfTable_Object = MibTable
zxAnEponRmPerfConfTable = _ZxAnEponRmPerfConfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 2)
)
if mibBuilder.loadTexts:
    zxAnEponRmPerfConfTable.setStatus("current")
_ZxAnEponRmPerfConfEntry_Object = MibTableRow
zxAnEponRmPerfConfEntry = _ZxAnEponRmPerfConfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 2, 1)
)
zxAnEponRmPerfConfEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmPerfOnuPortType"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponRmPerfConfEntry.setStatus("current")


class _ZxAnEponRmPerfOnuPortType_Type(Integer32):
    """Custom type zxAnEponRmPerfOnuPortType based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ponPort", 1),
          ("ethPort", 2))
    )


_ZxAnEponRmPerfOnuPortType_Type.__name__ = "Integer32"
_ZxAnEponRmPerfOnuPortType_Object = MibTableColumn
zxAnEponRmPerfOnuPortType = _ZxAnEponRmPerfOnuPortType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 2, 1, 1),
    _ZxAnEponRmPerfOnuPortType_Type()
)
zxAnEponRmPerfOnuPortType.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmPerfOnuPortType.setStatus("current")


class _ZxAnEponRmPerfOnuHisStatInterval_Type(Integer32):
    """Custom type zxAnEponRmPerfOnuHisStatInterval based on Integer32"""
    defaultValue = 900

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_ZxAnEponRmPerfOnuHisStatInterval_Type.__name__ = "Integer32"
_ZxAnEponRmPerfOnuHisStatInterval_Object = MibTableColumn
zxAnEponRmPerfOnuHisStatInterval = _ZxAnEponRmPerfOnuHisStatInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 2, 1, 2),
    _ZxAnEponRmPerfOnuHisStatInterval_Type()
)
zxAnEponRmPerfOnuHisStatInterval.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmPerfOnuHisStatInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponRmPerfOnuHisStatInterval.setUnits("Seconds")
_ZxAnEponRmPerfConfRowStatus_Type = RowStatus
_ZxAnEponRmPerfConfRowStatus_Object = MibTableColumn
zxAnEponRmPerfConfRowStatus = _ZxAnEponRmPerfConfRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 2, 1, 50),
    _ZxAnEponRmPerfConfRowStatus_Type()
)
zxAnEponRmPerfConfRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    zxAnEponRmPerfConfRowStatus.setStatus("current")
_ZxAnEponRmEthCurPerfTable_Object = MibTable
zxAnEponRmEthCurPerfTable = _ZxAnEponRmEthCurPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3)
)
if mibBuilder.loadTexts:
    zxAnEponRmEthCurPerfTable.setStatus("current")
_ZxAnEponRmEthCurPerfEntry_Object = MibTableRow
zxAnEponRmEthCurPerfEntry = _ZxAnEponRmEthCurPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1)
)
zxAnEponRmEthCurPerfEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmPerfOnuPortType"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponRmEthCurPerfEntry.setStatus("current")
_ZxAnEponRmCurDsDropEvents_Type = Counter64
_ZxAnEponRmCurDsDropEvents_Object = MibTableColumn
zxAnEponRmCurDsDropEvents = _ZxAnEponRmCurDsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 1),
    _ZxAnEponRmCurDsDropEvents_Type()
)
zxAnEponRmCurDsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsDropEvents.setStatus("current")
_ZxAnEponRmCurDsOctets_Type = Counter64
_ZxAnEponRmCurDsOctets_Object = MibTableColumn
zxAnEponRmCurDsOctets = _ZxAnEponRmCurDsOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 2),
    _ZxAnEponRmCurDsOctets_Type()
)
zxAnEponRmCurDsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsOctets.setStatus("current")
_ZxAnEponRmCurDsPkts_Type = Counter64
_ZxAnEponRmCurDsPkts_Object = MibTableColumn
zxAnEponRmCurDsPkts = _ZxAnEponRmCurDsPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 3),
    _ZxAnEponRmCurDsPkts_Type()
)
zxAnEponRmCurDsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsPkts.setStatus("current")
_ZxAnEponRmCurDsBcastPkts_Type = Counter64
_ZxAnEponRmCurDsBcastPkts_Object = MibTableColumn
zxAnEponRmCurDsBcastPkts = _ZxAnEponRmCurDsBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 4),
    _ZxAnEponRmCurDsBcastPkts_Type()
)
zxAnEponRmCurDsBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsBcastPkts.setStatus("current")
_ZxAnEponRmCurDsMcastPkts_Type = Counter64
_ZxAnEponRmCurDsMcastPkts_Object = MibTableColumn
zxAnEponRmCurDsMcastPkts = _ZxAnEponRmCurDsMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 5),
    _ZxAnEponRmCurDsMcastPkts_Type()
)
zxAnEponRmCurDsMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsMcastPkts.setStatus("current")
_ZxAnEponRmCurDsCrcErrPkts_Type = Counter64
_ZxAnEponRmCurDsCrcErrPkts_Object = MibTableColumn
zxAnEponRmCurDsCrcErrPkts = _ZxAnEponRmCurDsCrcErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 6),
    _ZxAnEponRmCurDsCrcErrPkts_Type()
)
zxAnEponRmCurDsCrcErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsCrcErrPkts.setStatus("current")
_ZxAnEponRmCurDsUndersizePkts_Type = Counter64
_ZxAnEponRmCurDsUndersizePkts_Object = MibTableColumn
zxAnEponRmCurDsUndersizePkts = _ZxAnEponRmCurDsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 7),
    _ZxAnEponRmCurDsUndersizePkts_Type()
)
zxAnEponRmCurDsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsUndersizePkts.setStatus("current")
_ZxAnEponRmCurDsOversizePkts_Type = Counter64
_ZxAnEponRmCurDsOversizePkts_Object = MibTableColumn
zxAnEponRmCurDsOversizePkts = _ZxAnEponRmCurDsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 8),
    _ZxAnEponRmCurDsOversizePkts_Type()
)
zxAnEponRmCurDsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsOversizePkts.setStatus("current")
_ZxAnEponRmCurDsFragments_Type = Counter64
_ZxAnEponRmCurDsFragments_Object = MibTableColumn
zxAnEponRmCurDsFragments = _ZxAnEponRmCurDsFragments_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 9),
    _ZxAnEponRmCurDsFragments_Type()
)
zxAnEponRmCurDsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsFragments.setStatus("current")
_ZxAnEponRmCurDsJabbers_Type = Counter64
_ZxAnEponRmCurDsJabbers_Object = MibTableColumn
zxAnEponRmCurDsJabbers = _ZxAnEponRmCurDsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 10),
    _ZxAnEponRmCurDsJabbers_Type()
)
zxAnEponRmCurDsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsJabbers.setStatus("current")
_ZxAnEponRmCurDsPkts64Octets_Type = Counter64
_ZxAnEponRmCurDsPkts64Octets_Object = MibTableColumn
zxAnEponRmCurDsPkts64Octets = _ZxAnEponRmCurDsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 11),
    _ZxAnEponRmCurDsPkts64Octets_Type()
)
zxAnEponRmCurDsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsPkts64Octets.setStatus("current")
_ZxAnEponRmCurDs65To127Octets_Type = Counter64
_ZxAnEponRmCurDs65To127Octets_Object = MibTableColumn
zxAnEponRmCurDs65To127Octets = _ZxAnEponRmCurDs65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 12),
    _ZxAnEponRmCurDs65To127Octets_Type()
)
zxAnEponRmCurDs65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDs65To127Octets.setStatus("current")
_ZxAnEponRmCurDs128To255Octets_Type = Counter64
_ZxAnEponRmCurDs128To255Octets_Object = MibTableColumn
zxAnEponRmCurDs128To255Octets = _ZxAnEponRmCurDs128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 13),
    _ZxAnEponRmCurDs128To255Octets_Type()
)
zxAnEponRmCurDs128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDs128To255Octets.setStatus("current")
_ZxAnEponRmCurDs256To511Octets_Type = Counter64
_ZxAnEponRmCurDs256To511Octets_Object = MibTableColumn
zxAnEponRmCurDs256To511Octets = _ZxAnEponRmCurDs256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 14),
    _ZxAnEponRmCurDs256To511Octets_Type()
)
zxAnEponRmCurDs256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDs256To511Octets.setStatus("current")
_ZxAnEponRmCurDs512To1023Octets_Type = Counter64
_ZxAnEponRmCurDs512To1023Octets_Object = MibTableColumn
zxAnEponRmCurDs512To1023Octets = _ZxAnEponRmCurDs512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 15),
    _ZxAnEponRmCurDs512To1023Octets_Type()
)
zxAnEponRmCurDs512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDs512To1023Octets.setStatus("current")
_ZxAnEponRmCurDs1024To1518Octets_Type = Counter64
_ZxAnEponRmCurDs1024To1518Octets_Object = MibTableColumn
zxAnEponRmCurDs1024To1518Octets = _ZxAnEponRmCurDs1024To1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 16),
    _ZxAnEponRmCurDs1024To1518Octets_Type()
)
zxAnEponRmCurDs1024To1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDs1024To1518Octets.setStatus("current")
_ZxAnEponRmCurDsDiscards_Type = Counter64
_ZxAnEponRmCurDsDiscards_Object = MibTableColumn
zxAnEponRmCurDsDiscards = _ZxAnEponRmCurDsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 17),
    _ZxAnEponRmCurDsDiscards_Type()
)
zxAnEponRmCurDsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsDiscards.setStatus("current")
_ZxAnEponRmCurDsErrors_Type = Counter64
_ZxAnEponRmCurDsErrors_Object = MibTableColumn
zxAnEponRmCurDsErrors = _ZxAnEponRmCurDsErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 18),
    _ZxAnEponRmCurDsErrors_Type()
)
zxAnEponRmCurDsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurDsErrors.setStatus("current")
_ZxAnEponRmCurUsDropEvents_Type = Counter64
_ZxAnEponRmCurUsDropEvents_Object = MibTableColumn
zxAnEponRmCurUsDropEvents = _ZxAnEponRmCurUsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 19),
    _ZxAnEponRmCurUsDropEvents_Type()
)
zxAnEponRmCurUsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsDropEvents.setStatus("current")
_ZxAnEponRmCurUsOctets_Type = Counter64
_ZxAnEponRmCurUsOctets_Object = MibTableColumn
zxAnEponRmCurUsOctets = _ZxAnEponRmCurUsOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 20),
    _ZxAnEponRmCurUsOctets_Type()
)
zxAnEponRmCurUsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsOctets.setStatus("current")
_ZxAnEponRmCurUsPkts_Type = Counter64
_ZxAnEponRmCurUsPkts_Object = MibTableColumn
zxAnEponRmCurUsPkts = _ZxAnEponRmCurUsPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 21),
    _ZxAnEponRmCurUsPkts_Type()
)
zxAnEponRmCurUsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsPkts.setStatus("current")
_ZxAnEponRmCurUsBcastPkts_Type = Counter64
_ZxAnEponRmCurUsBcastPkts_Object = MibTableColumn
zxAnEponRmCurUsBcastPkts = _ZxAnEponRmCurUsBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 22),
    _ZxAnEponRmCurUsBcastPkts_Type()
)
zxAnEponRmCurUsBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsBcastPkts.setStatus("current")
_ZxAnEponRmCurUsMcastPkts_Type = Counter64
_ZxAnEponRmCurUsMcastPkts_Object = MibTableColumn
zxAnEponRmCurUsMcastPkts = _ZxAnEponRmCurUsMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 23),
    _ZxAnEponRmCurUsMcastPkts_Type()
)
zxAnEponRmCurUsMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsMcastPkts.setStatus("current")
_ZxAnEponRmCurUsCrcErrPkts_Type = Counter64
_ZxAnEponRmCurUsCrcErrPkts_Object = MibTableColumn
zxAnEponRmCurUsCrcErrPkts = _ZxAnEponRmCurUsCrcErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 24),
    _ZxAnEponRmCurUsCrcErrPkts_Type()
)
zxAnEponRmCurUsCrcErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsCrcErrPkts.setStatus("current")
_ZxAnEponRmCurUsUndersizePkts_Type = Counter64
_ZxAnEponRmCurUsUndersizePkts_Object = MibTableColumn
zxAnEponRmCurUsUndersizePkts = _ZxAnEponRmCurUsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 25),
    _ZxAnEponRmCurUsUndersizePkts_Type()
)
zxAnEponRmCurUsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsUndersizePkts.setStatus("current")
_ZxAnEponRmCurUsOversizePkts_Type = Counter64
_ZxAnEponRmCurUsOversizePkts_Object = MibTableColumn
zxAnEponRmCurUsOversizePkts = _ZxAnEponRmCurUsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 26),
    _ZxAnEponRmCurUsOversizePkts_Type()
)
zxAnEponRmCurUsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsOversizePkts.setStatus("current")
_ZxAnEponRmCurUsFragments_Type = Counter64
_ZxAnEponRmCurUsFragments_Object = MibTableColumn
zxAnEponRmCurUsFragments = _ZxAnEponRmCurUsFragments_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 27),
    _ZxAnEponRmCurUsFragments_Type()
)
zxAnEponRmCurUsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsFragments.setStatus("current")
_ZxAnEponRmCurUsJabbers_Type = Counter64
_ZxAnEponRmCurUsJabbers_Object = MibTableColumn
zxAnEponRmCurUsJabbers = _ZxAnEponRmCurUsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 28),
    _ZxAnEponRmCurUsJabbers_Type()
)
zxAnEponRmCurUsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsJabbers.setStatus("current")
_ZxAnEponRmCurUsPkts64Octets_Type = Counter64
_ZxAnEponRmCurUsPkts64Octets_Object = MibTableColumn
zxAnEponRmCurUsPkts64Octets = _ZxAnEponRmCurUsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 29),
    _ZxAnEponRmCurUsPkts64Octets_Type()
)
zxAnEponRmCurUsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsPkts64Octets.setStatus("current")
_ZxAnEponRmCurUs65To127Octets_Type = Counter64
_ZxAnEponRmCurUs65To127Octets_Object = MibTableColumn
zxAnEponRmCurUs65To127Octets = _ZxAnEponRmCurUs65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 30),
    _ZxAnEponRmCurUs65To127Octets_Type()
)
zxAnEponRmCurUs65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUs65To127Octets.setStatus("current")
_ZxAnEponRmCurUs128To255Octets_Type = Counter64
_ZxAnEponRmCurUs128To255Octets_Object = MibTableColumn
zxAnEponRmCurUs128To255Octets = _ZxAnEponRmCurUs128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 31),
    _ZxAnEponRmCurUs128To255Octets_Type()
)
zxAnEponRmCurUs128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUs128To255Octets.setStatus("current")
_ZxAnEponRmCurUs256To511Octets_Type = Counter64
_ZxAnEponRmCurUs256To511Octets_Object = MibTableColumn
zxAnEponRmCurUs256To511Octets = _ZxAnEponRmCurUs256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 32),
    _ZxAnEponRmCurUs256To511Octets_Type()
)
zxAnEponRmCurUs256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUs256To511Octets.setStatus("current")
_ZxAnEponRmCurUs512To1023Octets_Type = Counter64
_ZxAnEponRmCurUs512To1023Octets_Object = MibTableColumn
zxAnEponRmCurUs512To1023Octets = _ZxAnEponRmCurUs512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 33),
    _ZxAnEponRmCurUs512To1023Octets_Type()
)
zxAnEponRmCurUs512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUs512To1023Octets.setStatus("current")
_ZxAnEponRmCurUs1024To1518Octets_Type = Counter64
_ZxAnEponRmCurUs1024To1518Octets_Object = MibTableColumn
zxAnEponRmCurUs1024To1518Octets = _ZxAnEponRmCurUs1024To1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 34),
    _ZxAnEponRmCurUs1024To1518Octets_Type()
)
zxAnEponRmCurUs1024To1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUs1024To1518Octets.setStatus("current")
_ZxAnEponRmCurUsDiscards_Type = Counter64
_ZxAnEponRmCurUsDiscards_Object = MibTableColumn
zxAnEponRmCurUsDiscards = _ZxAnEponRmCurUsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 35),
    _ZxAnEponRmCurUsDiscards_Type()
)
zxAnEponRmCurUsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsDiscards.setStatus("current")
_ZxAnEponRmCurUsErrors_Type = Counter64
_ZxAnEponRmCurUsErrors_Object = MibTableColumn
zxAnEponRmCurUsErrors = _ZxAnEponRmCurUsErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 36),
    _ZxAnEponRmCurUsErrors_Type()
)
zxAnEponRmCurUsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurUsErrors.setStatus("current")
_ZxAnEponRmCurPortStatusChanges_Type = Counter64
_ZxAnEponRmCurPortStatusChanges_Object = MibTableColumn
zxAnEponRmCurPortStatusChanges = _ZxAnEponRmCurPortStatusChanges_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 3, 1, 37),
    _ZxAnEponRmCurPortStatusChanges_Type()
)
zxAnEponRmCurPortStatusChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmCurPortStatusChanges.setStatus("current")
_ZxAnEponRmEthHisPerfTable_Object = MibTable
zxAnEponRmEthHisPerfTable = _ZxAnEponRmEthHisPerfTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4)
)
if mibBuilder.loadTexts:
    zxAnEponRmEthHisPerfTable.setStatus("current")
_ZxAnEponRmEthHisPerfEntry_Object = MibTableRow
zxAnEponRmEthHisPerfEntry = _ZxAnEponRmEthHisPerfEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1)
)
zxAnEponRmEthHisPerfEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmPerfOnuPortType"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponRmEthHisIntervalNo"),
)
if mibBuilder.loadTexts:
    zxAnEponRmEthHisPerfEntry.setStatus("current")


class _ZxAnEponRmEthHisIntervalNo_Type(Integer32):
    """Custom type zxAnEponRmEthHisIntervalNo based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 96),
    )


_ZxAnEponRmEthHisIntervalNo_Type.__name__ = "Integer32"
_ZxAnEponRmEthHisIntervalNo_Object = MibTableColumn
zxAnEponRmEthHisIntervalNo = _ZxAnEponRmEthHisIntervalNo_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 1),
    _ZxAnEponRmEthHisIntervalNo_Type()
)
zxAnEponRmEthHisIntervalNo.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponRmEthHisIntervalNo.setStatus("current")
_ZxAnEponRmHisDsDropEvents_Type = Counter64
_ZxAnEponRmHisDsDropEvents_Object = MibTableColumn
zxAnEponRmHisDsDropEvents = _ZxAnEponRmHisDsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 2),
    _ZxAnEponRmHisDsDropEvents_Type()
)
zxAnEponRmHisDsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsDropEvents.setStatus("current")
_ZxAnEponRmHisDsOctets_Type = Counter64
_ZxAnEponRmHisDsOctets_Object = MibTableColumn
zxAnEponRmHisDsOctets = _ZxAnEponRmHisDsOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 3),
    _ZxAnEponRmHisDsOctets_Type()
)
zxAnEponRmHisDsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsOctets.setStatus("current")
_ZxAnEponRmHisDsPkts_Type = Counter64
_ZxAnEponRmHisDsPkts_Object = MibTableColumn
zxAnEponRmHisDsPkts = _ZxAnEponRmHisDsPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 4),
    _ZxAnEponRmHisDsPkts_Type()
)
zxAnEponRmHisDsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsPkts.setStatus("current")
_ZxAnEponRmHisDsBcastPkts_Type = Counter64
_ZxAnEponRmHisDsBcastPkts_Object = MibTableColumn
zxAnEponRmHisDsBcastPkts = _ZxAnEponRmHisDsBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 5),
    _ZxAnEponRmHisDsBcastPkts_Type()
)
zxAnEponRmHisDsBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsBcastPkts.setStatus("current")
_ZxAnEponRmHisDsMcastPkts_Type = Counter64
_ZxAnEponRmHisDsMcastPkts_Object = MibTableColumn
zxAnEponRmHisDsMcastPkts = _ZxAnEponRmHisDsMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 6),
    _ZxAnEponRmHisDsMcastPkts_Type()
)
zxAnEponRmHisDsMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsMcastPkts.setStatus("current")
_ZxAnEponRmHisDsCrcErrPkts_Type = Counter64
_ZxAnEponRmHisDsCrcErrPkts_Object = MibTableColumn
zxAnEponRmHisDsCrcErrPkts = _ZxAnEponRmHisDsCrcErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 7),
    _ZxAnEponRmHisDsCrcErrPkts_Type()
)
zxAnEponRmHisDsCrcErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsCrcErrPkts.setStatus("current")
_ZxAnEponRmHisDsUndersizePkts_Type = Counter64
_ZxAnEponRmHisDsUndersizePkts_Object = MibTableColumn
zxAnEponRmHisDsUndersizePkts = _ZxAnEponRmHisDsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 8),
    _ZxAnEponRmHisDsUndersizePkts_Type()
)
zxAnEponRmHisDsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsUndersizePkts.setStatus("current")
_ZxAnEponRmHisDsOversizePkts_Type = Counter64
_ZxAnEponRmHisDsOversizePkts_Object = MibTableColumn
zxAnEponRmHisDsOversizePkts = _ZxAnEponRmHisDsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 9),
    _ZxAnEponRmHisDsOversizePkts_Type()
)
zxAnEponRmHisDsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsOversizePkts.setStatus("current")
_ZxAnEponRmHisDsFragments_Type = Counter64
_ZxAnEponRmHisDsFragments_Object = MibTableColumn
zxAnEponRmHisDsFragments = _ZxAnEponRmHisDsFragments_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 10),
    _ZxAnEponRmHisDsFragments_Type()
)
zxAnEponRmHisDsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsFragments.setStatus("current")
_ZxAnEponRmHisDsJabbers_Type = Counter64
_ZxAnEponRmHisDsJabbers_Object = MibTableColumn
zxAnEponRmHisDsJabbers = _ZxAnEponRmHisDsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 11),
    _ZxAnEponRmHisDsJabbers_Type()
)
zxAnEponRmHisDsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsJabbers.setStatus("current")
_ZxAnEponRmHisDsPkts64Octets_Type = Counter64
_ZxAnEponRmHisDsPkts64Octets_Object = MibTableColumn
zxAnEponRmHisDsPkts64Octets = _ZxAnEponRmHisDsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 12),
    _ZxAnEponRmHisDsPkts64Octets_Type()
)
zxAnEponRmHisDsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsPkts64Octets.setStatus("current")
_ZxAnEponRmHisDs65To127Octets_Type = Counter64
_ZxAnEponRmHisDs65To127Octets_Object = MibTableColumn
zxAnEponRmHisDs65To127Octets = _ZxAnEponRmHisDs65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 13),
    _ZxAnEponRmHisDs65To127Octets_Type()
)
zxAnEponRmHisDs65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDs65To127Octets.setStatus("current")
_ZxAnEponRmHisDs128To255Octets_Type = Counter64
_ZxAnEponRmHisDs128To255Octets_Object = MibTableColumn
zxAnEponRmHisDs128To255Octets = _ZxAnEponRmHisDs128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 14),
    _ZxAnEponRmHisDs128To255Octets_Type()
)
zxAnEponRmHisDs128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDs128To255Octets.setStatus("current")
_ZxAnEponRmHisDs256To511Octets_Type = Counter64
_ZxAnEponRmHisDs256To511Octets_Object = MibTableColumn
zxAnEponRmHisDs256To511Octets = _ZxAnEponRmHisDs256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 15),
    _ZxAnEponRmHisDs256To511Octets_Type()
)
zxAnEponRmHisDs256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDs256To511Octets.setStatus("current")
_ZxAnEponRmHisDs512To1023Octets_Type = Counter64
_ZxAnEponRmHisDs512To1023Octets_Object = MibTableColumn
zxAnEponRmHisDs512To1023Octets = _ZxAnEponRmHisDs512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 16),
    _ZxAnEponRmHisDs512To1023Octets_Type()
)
zxAnEponRmHisDs512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDs512To1023Octets.setStatus("current")
_ZxAnEponRmHisDs1024To1518Octets_Type = Counter64
_ZxAnEponRmHisDs1024To1518Octets_Object = MibTableColumn
zxAnEponRmHisDs1024To1518Octets = _ZxAnEponRmHisDs1024To1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 17),
    _ZxAnEponRmHisDs1024To1518Octets_Type()
)
zxAnEponRmHisDs1024To1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDs1024To1518Octets.setStatus("current")
_ZxAnEponRmHisDsDiscards_Type = Counter64
_ZxAnEponRmHisDsDiscards_Object = MibTableColumn
zxAnEponRmHisDsDiscards = _ZxAnEponRmHisDsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 18),
    _ZxAnEponRmHisDsDiscards_Type()
)
zxAnEponRmHisDsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsDiscards.setStatus("current")
_ZxAnEponRmHisDsErrors_Type = Counter64
_ZxAnEponRmHisDsErrors_Object = MibTableColumn
zxAnEponRmHisDsErrors = _ZxAnEponRmHisDsErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 19),
    _ZxAnEponRmHisDsErrors_Type()
)
zxAnEponRmHisDsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisDsErrors.setStatus("current")
_ZxAnEponRmHisUsDropEvents_Type = Counter64
_ZxAnEponRmHisUsDropEvents_Object = MibTableColumn
zxAnEponRmHisUsDropEvents = _ZxAnEponRmHisUsDropEvents_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 20),
    _ZxAnEponRmHisUsDropEvents_Type()
)
zxAnEponRmHisUsDropEvents.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsDropEvents.setStatus("current")
_ZxAnEponRmHisUsOctets_Type = Counter64
_ZxAnEponRmHisUsOctets_Object = MibTableColumn
zxAnEponRmHisUsOctets = _ZxAnEponRmHisUsOctets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 21),
    _ZxAnEponRmHisUsOctets_Type()
)
zxAnEponRmHisUsOctets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsOctets.setStatus("current")
_ZxAnEponRmHisUsPkts_Type = Counter64
_ZxAnEponRmHisUsPkts_Object = MibTableColumn
zxAnEponRmHisUsPkts = _ZxAnEponRmHisUsPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 22),
    _ZxAnEponRmHisUsPkts_Type()
)
zxAnEponRmHisUsPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsPkts.setStatus("current")
_ZxAnEponRmHisUsBcastPkts_Type = Counter64
_ZxAnEponRmHisUsBcastPkts_Object = MibTableColumn
zxAnEponRmHisUsBcastPkts = _ZxAnEponRmHisUsBcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 23),
    _ZxAnEponRmHisUsBcastPkts_Type()
)
zxAnEponRmHisUsBcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsBcastPkts.setStatus("current")
_ZxAnEponRmHisUsMcastPkts_Type = Counter64
_ZxAnEponRmHisUsMcastPkts_Object = MibTableColumn
zxAnEponRmHisUsMcastPkts = _ZxAnEponRmHisUsMcastPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 24),
    _ZxAnEponRmHisUsMcastPkts_Type()
)
zxAnEponRmHisUsMcastPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsMcastPkts.setStatus("current")
_ZxAnEponRmHisUsCrcErrPkts_Type = Counter64
_ZxAnEponRmHisUsCrcErrPkts_Object = MibTableColumn
zxAnEponRmHisUsCrcErrPkts = _ZxAnEponRmHisUsCrcErrPkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 25),
    _ZxAnEponRmHisUsCrcErrPkts_Type()
)
zxAnEponRmHisUsCrcErrPkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsCrcErrPkts.setStatus("current")
_ZxAnEponRmHisUsUndersizePkts_Type = Counter64
_ZxAnEponRmHisUsUndersizePkts_Object = MibTableColumn
zxAnEponRmHisUsUndersizePkts = _ZxAnEponRmHisUsUndersizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 26),
    _ZxAnEponRmHisUsUndersizePkts_Type()
)
zxAnEponRmHisUsUndersizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsUndersizePkts.setStatus("current")
_ZxAnEponRmHisUsOversizePkts_Type = Counter64
_ZxAnEponRmHisUsOversizePkts_Object = MibTableColumn
zxAnEponRmHisUsOversizePkts = _ZxAnEponRmHisUsOversizePkts_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 27),
    _ZxAnEponRmHisUsOversizePkts_Type()
)
zxAnEponRmHisUsOversizePkts.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsOversizePkts.setStatus("current")
_ZxAnEponRmHisUsFragments_Type = Counter64
_ZxAnEponRmHisUsFragments_Object = MibTableColumn
zxAnEponRmHisUsFragments = _ZxAnEponRmHisUsFragments_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 28),
    _ZxAnEponRmHisUsFragments_Type()
)
zxAnEponRmHisUsFragments.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsFragments.setStatus("current")
_ZxAnEponRmHisUsJabbers_Type = Counter64
_ZxAnEponRmHisUsJabbers_Object = MibTableColumn
zxAnEponRmHisUsJabbers = _ZxAnEponRmHisUsJabbers_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 29),
    _ZxAnEponRmHisUsJabbers_Type()
)
zxAnEponRmHisUsJabbers.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsJabbers.setStatus("current")
_ZxAnEponRmHisUsPkts64Octets_Type = Counter64
_ZxAnEponRmHisUsPkts64Octets_Object = MibTableColumn
zxAnEponRmHisUsPkts64Octets = _ZxAnEponRmHisUsPkts64Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 30),
    _ZxAnEponRmHisUsPkts64Octets_Type()
)
zxAnEponRmHisUsPkts64Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsPkts64Octets.setStatus("current")
_ZxAnEponRmHisUs65To127Octets_Type = Counter64
_ZxAnEponRmHisUs65To127Octets_Object = MibTableColumn
zxAnEponRmHisUs65To127Octets = _ZxAnEponRmHisUs65To127Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 31),
    _ZxAnEponRmHisUs65To127Octets_Type()
)
zxAnEponRmHisUs65To127Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUs65To127Octets.setStatus("current")
_ZxAnEponRmHisUs128To255Octets_Type = Counter64
_ZxAnEponRmHisUs128To255Octets_Object = MibTableColumn
zxAnEponRmHisUs128To255Octets = _ZxAnEponRmHisUs128To255Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 32),
    _ZxAnEponRmHisUs128To255Octets_Type()
)
zxAnEponRmHisUs128To255Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUs128To255Octets.setStatus("current")
_ZxAnEponRmHisUs256To511Octets_Type = Counter64
_ZxAnEponRmHisUs256To511Octets_Object = MibTableColumn
zxAnEponRmHisUs256To511Octets = _ZxAnEponRmHisUs256To511Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 33),
    _ZxAnEponRmHisUs256To511Octets_Type()
)
zxAnEponRmHisUs256To511Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUs256To511Octets.setStatus("current")
_ZxAnEponRmHisUs512To1023Octets_Type = Counter64
_ZxAnEponRmHisUs512To1023Octets_Object = MibTableColumn
zxAnEponRmHisUs512To1023Octets = _ZxAnEponRmHisUs512To1023Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 34),
    _ZxAnEponRmHisUs512To1023Octets_Type()
)
zxAnEponRmHisUs512To1023Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUs512To1023Octets.setStatus("current")
_ZxAnEponRmHisUs1024To1518Octets_Type = Counter64
_ZxAnEponRmHisUs1024To1518Octets_Object = MibTableColumn
zxAnEponRmHisUs1024To1518Octets = _ZxAnEponRmHisUs1024To1518Octets_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 35),
    _ZxAnEponRmHisUs1024To1518Octets_Type()
)
zxAnEponRmHisUs1024To1518Octets.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUs1024To1518Octets.setStatus("current")
_ZxAnEponRmHisUsDiscards_Type = Counter64
_ZxAnEponRmHisUsDiscards_Object = MibTableColumn
zxAnEponRmHisUsDiscards = _ZxAnEponRmHisUsDiscards_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 36),
    _ZxAnEponRmHisUsDiscards_Type()
)
zxAnEponRmHisUsDiscards.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsDiscards.setStatus("current")
_ZxAnEponRmHisUsErrors_Type = Counter64
_ZxAnEponRmHisUsErrors_Object = MibTableColumn
zxAnEponRmHisUsErrors = _ZxAnEponRmHisUsErrors_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 37),
    _ZxAnEponRmHisUsErrors_Type()
)
zxAnEponRmHisUsErrors.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisUsErrors.setStatus("current")
_ZxAnEponRmHisPortStatusChanges_Type = Counter64
_ZxAnEponRmHisPortStatusChanges_Object = MibTableColumn
zxAnEponRmHisPortStatusChanges = _ZxAnEponRmHisPortStatusChanges_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 7, 4, 1, 38),
    _ZxAnEponRmHisPortStatusChanges_Type()
)
zxAnEponRmHisPortStatusChanges.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponRmHisPortStatusChanges.setStatus("current")
_ZxAnPtpExtOamMgmt_ObjectIdentity = ObjectIdentity
zxAnPtpExtOamMgmt = _ZxAnPtpExtOamMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 8)
)
_ZxAnPtpExtOamTable_Object = MibTable
zxAnPtpExtOamTable = _ZxAnPtpExtOamTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 8, 2)
)
if mibBuilder.loadTexts:
    zxAnPtpExtOamTable.setStatus("current")
_ZxAnPtpExtOamEntry_Object = MibTableRow
zxAnPtpExtOamEntry = _ZxAnPtpExtOamEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 8, 2, 1)
)
zxAnPtpExtOamEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnPtpIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnPtpExtOamEntry.setStatus("current")
_ZxAnPtpIfIndex_Type = Integer32
_ZxAnPtpIfIndex_Object = MibTableColumn
zxAnPtpIfIndex = _ZxAnPtpIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 8, 2, 1, 1),
    _ZxAnPtpIfIndex_Type()
)
zxAnPtpIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnPtpIfIndex.setStatus("current")


class _ZxAnPtpExtOamAdminStatus_Type(Integer32):
    """Custom type zxAnPtpExtOamAdminStatus based on Integer32"""
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


_ZxAnPtpExtOamAdminStatus_Type.__name__ = "Integer32"
_ZxAnPtpExtOamAdminStatus_Object = MibTableColumn
zxAnPtpExtOamAdminStatus = _ZxAnPtpExtOamAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 8, 2, 1, 2),
    _ZxAnPtpExtOamAdminStatus_Type()
)
zxAnPtpExtOamAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnPtpExtOamAdminStatus.setStatus("current")
_ZxAnEponOnuCustomMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuCustomMgmt = _ZxAnEponOnuCustomMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101)
)
_ZxAnEponOnuTkMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuTkMgmt = _ZxAnEponOnuTkMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31)
)
_ZxAnEponOnuTkAttrMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuTkAttrMgmt = _ZxAnEponOnuTkAttrMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31)
)
_ZxAnEponOnuTkGlobalTable_Object = MibTable
zxAnEponOnuTkGlobalTable = _ZxAnEponOnuTkGlobalTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 31)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalTable.setStatus("current")
_ZxAnEponOnuTkGlobalEntry_Object = MibTableRow
zxAnEponOnuTkGlobalEntry = _ZxAnEponOnuTkGlobalEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 31, 1)
)
zxAnEponOnuTkGlobalEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalEntry.setStatus("current")
_ZxAnEponOnuTkFirmwareVer_Type = DisplayString
_ZxAnEponOnuTkFirmwareVer_Object = MibTableColumn
zxAnEponOnuTkFirmwareVer = _ZxAnEponOnuTkFirmwareVer_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 31, 1, 1),
    _ZxAnEponOnuTkFirmwareVer_Type()
)
zxAnEponOnuTkFirmwareVer.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkFirmwareVer.setStatus("current")
_ZxAnEponOnuTkModeName_Type = DisplayString
_ZxAnEponOnuTkModeName_Object = MibTableColumn
zxAnEponOnuTkModeName = _ZxAnEponOnuTkModeName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 31, 1, 2),
    _ZxAnEponOnuTkModeName_Type()
)
zxAnEponOnuTkModeName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkModeName.setStatus("current")
_ZxAnEponOnuTkPortTable_Object = MibTable
zxAnEponOnuTkPortTable = _ZxAnEponOnuTkPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 32)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortTable.setStatus("current")
_ZxAnEponOnuTkPortEntry_Object = MibTableRow
zxAnEponOnuTkPortEntry = _ZxAnEponOnuTkPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 32, 1)
)
zxAnEponOnuTkPortEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortEntry.setStatus("current")


class _ZxAnEponOnuTkPortOperStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkPortOperStatus based on Integer32"""
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


_ZxAnEponOnuTkPortOperStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkPortOperStatus_Object = MibTableColumn
zxAnEponOnuTkPortOperStatus = _ZxAnEponOnuTkPortOperStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 32, 1, 1),
    _ZxAnEponOnuTkPortOperStatus_Type()
)
zxAnEponOnuTkPortOperStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortOperStatus.setStatus("current")


class _ZxAnEponOnuTkPortAutoNegStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkPortAutoNegStatus based on Integer32"""
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


_ZxAnEponOnuTkPortAutoNegStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkPortAutoNegStatus_Object = MibTableColumn
zxAnEponOnuTkPortAutoNegStatus = _ZxAnEponOnuTkPortAutoNegStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 32, 1, 2),
    _ZxAnEponOnuTkPortAutoNegStatus_Type()
)
zxAnEponOnuTkPortAutoNegStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortAutoNegStatus.setStatus("current")


class _ZxAnEponOnuTkPortFlowCtrlStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkPortFlowCtrlStatus based on Integer32"""
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


_ZxAnEponOnuTkPortFlowCtrlStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkPortFlowCtrlStatus_Object = MibTableColumn
zxAnEponOnuTkPortFlowCtrlStatus = _ZxAnEponOnuTkPortFlowCtrlStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 32, 1, 3),
    _ZxAnEponOnuTkPortFlowCtrlStatus_Type()
)
zxAnEponOnuTkPortFlowCtrlStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortFlowCtrlStatus.setStatus("current")


class _ZxAnEponOnuTkPortDuplexMode_Type(Integer32):
    """Custom type zxAnEponOnuTkPortDuplexMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("half", 1),
          ("full", 2))
    )


_ZxAnEponOnuTkPortDuplexMode_Type.__name__ = "Integer32"
_ZxAnEponOnuTkPortDuplexMode_Object = MibTableColumn
zxAnEponOnuTkPortDuplexMode = _ZxAnEponOnuTkPortDuplexMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 32, 1, 4),
    _ZxAnEponOnuTkPortDuplexMode_Type()
)
zxAnEponOnuTkPortDuplexMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortDuplexMode.setStatus("current")


class _ZxAnEponOnuTkPortAdminStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkPortAdminStatus based on Integer32"""
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


_ZxAnEponOnuTkPortAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkPortAdminStatus_Object = MibTableColumn
zxAnEponOnuTkPortAdminStatus = _ZxAnEponOnuTkPortAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 32, 1, 5),
    _ZxAnEponOnuTkPortAdminStatus_Type()
)
zxAnEponOnuTkPortAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortAdminStatus.setStatus("current")
_ZxAnEponOnuTkLoopbackTable_Object = MibTable
zxAnEponOnuTkLoopbackTable = _ZxAnEponOnuTkLoopbackTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 33)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkLoopbackTable.setStatus("current")
_ZxAnEponOnuTkLoopbackEntry_Object = MibTableRow
zxAnEponOnuTkLoopbackEntry = _ZxAnEponOnuTkLoopbackEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 33, 1)
)
zxAnEponOnuTkLoopbackEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkLoopbackEntry.setStatus("current")


class _ZxAnEponOnuTkLoopbackAdminStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkLoopbackAdminStatus based on Integer32"""
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


_ZxAnEponOnuTkLoopbackAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkLoopbackAdminStatus_Object = MibTableColumn
zxAnEponOnuTkLoopbackAdminStatus = _ZxAnEponOnuTkLoopbackAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 33, 1, 1),
    _ZxAnEponOnuTkLoopbackAdminStatus_Type()
)
zxAnEponOnuTkLoopbackAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkLoopbackAdminStatus.setStatus("current")
_ZxAnEponOnuTkLinkBlockTable_Object = MibTable
zxAnEponOnuTkLinkBlockTable = _ZxAnEponOnuTkLinkBlockTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 34)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkLinkBlockTable.setStatus("current")
_ZxAnEponOnuTkLinkBlockEntry_Object = MibTableRow
zxAnEponOnuTkLinkBlockEntry = _ZxAnEponOnuTkLinkBlockEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 34, 1)
)
zxAnEponOnuTkLinkBlockEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkLinkBlockEntry.setStatus("current")


class _ZxAnEponOnuTkLinkBlockAdminStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkLinkBlockAdminStatus based on Integer32"""
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


_ZxAnEponOnuTkLinkBlockAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkLinkBlockAdminStatus_Object = MibTableColumn
zxAnEponOnuTkLinkBlockAdminStatus = _ZxAnEponOnuTkLinkBlockAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 34, 1, 1),
    _ZxAnEponOnuTkLinkBlockAdminStatus_Type()
)
zxAnEponOnuTkLinkBlockAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkLinkBlockAdminStatus.setStatus("current")


class _ZxAnEponOnuTkLinkBlockOamType_Type(Integer32):
    """Custom type zxAnEponOnuTkLinkBlockOamType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tk-oam", 1),
          ("kt-oam", 2))
    )


_ZxAnEponOnuTkLinkBlockOamType_Type.__name__ = "Integer32"
_ZxAnEponOnuTkLinkBlockOamType_Object = MibTableColumn
zxAnEponOnuTkLinkBlockOamType = _ZxAnEponOnuTkLinkBlockOamType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 34, 1, 2),
    _ZxAnEponOnuTkLinkBlockOamType_Type()
)
zxAnEponOnuTkLinkBlockOamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkLinkBlockOamType.setStatus("current")
_ZxAnEponOnuTkOpticalCtrlTable_Object = MibTable
zxAnEponOnuTkOpticalCtrlTable = _ZxAnEponOnuTkOpticalCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 35)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkOpticalCtrlTable.setStatus("current")
_ZxAnEponOnuTkOpticalCtrlEntry_Object = MibTableRow
zxAnEponOnuTkOpticalCtrlEntry = _ZxAnEponOnuTkOpticalCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 35, 1)
)
zxAnEponOnuTkOpticalCtrlEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkOpticalCtrlEntry.setStatus("current")


class _ZxAnEponOnuTkOpticalBlockStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkOpticalBlockStatus based on Integer32"""
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


_ZxAnEponOnuTkOpticalBlockStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkOpticalBlockStatus_Object = MibTableColumn
zxAnEponOnuTkOpticalBlockStatus = _ZxAnEponOnuTkOpticalBlockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 35, 1, 1),
    _ZxAnEponOnuTkOpticalBlockStatus_Type()
)
zxAnEponOnuTkOpticalBlockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkOpticalBlockStatus.setStatus("current")


class _ZxAnEponOnuTkOpticalBlockDurationTime_Type(Integer32):
    """Custom type zxAnEponOnuTkOpticalBlockDurationTime based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnEponOnuTkOpticalBlockDurationTime_Type.__name__ = "Integer32"
_ZxAnEponOnuTkOpticalBlockDurationTime_Object = MibTableColumn
zxAnEponOnuTkOpticalBlockDurationTime = _ZxAnEponOnuTkOpticalBlockDurationTime_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 35, 1, 2),
    _ZxAnEponOnuTkOpticalBlockDurationTime_Type()
)
zxAnEponOnuTkOpticalBlockDurationTime.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkOpticalBlockDurationTime.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponOnuTkOpticalBlockDurationTime.setUnits("second")


class _ZxAnEponOnuTkOpticalBlockOamType_Type(Integer32):
    """Custom type zxAnEponOnuTkOpticalBlockOamType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tk-oam", 1),
          ("kt-oam", 2))
    )


_ZxAnEponOnuTkOpticalBlockOamType_Type.__name__ = "Integer32"
_ZxAnEponOnuTkOpticalBlockOamType_Object = MibTableColumn
zxAnEponOnuTkOpticalBlockOamType = _ZxAnEponOnuTkOpticalBlockOamType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 35, 1, 3),
    _ZxAnEponOnuTkOpticalBlockOamType_Type()
)
zxAnEponOnuTkOpticalBlockOamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkOpticalBlockOamType.setStatus("current")
_ZxAnEponOnuTkRstpCtrlTable_Object = MibTable
zxAnEponOnuTkRstpCtrlTable = _ZxAnEponOnuTkRstpCtrlTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 36)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkRstpCtrlTable.setStatus("current")
_ZxAnEponOnuTkRstpCtrlEntry_Object = MibTableRow
zxAnEponOnuTkRstpCtrlEntry = _ZxAnEponOnuTkRstpCtrlEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 36, 1)
)
zxAnEponOnuTkRstpCtrlEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkRstpCtrlEntry.setStatus("current")


class _ZxAnEponOnuTkRstpAdminStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkRstpAdminStatus based on Integer32"""
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
        *(("enable", 1),
          ("disable", 2),
          ("passthrough", 3))
    )


_ZxAnEponOnuTkRstpAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkRstpAdminStatus_Object = MibTableColumn
zxAnEponOnuTkRstpAdminStatus = _ZxAnEponOnuTkRstpAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 36, 1, 1),
    _ZxAnEponOnuTkRstpAdminStatus_Type()
)
zxAnEponOnuTkRstpAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkRstpAdminStatus.setStatus("current")
_ZxAnEponOnuTkMacLearningTable_Object = MibTable
zxAnEponOnuTkMacLearningTable = _ZxAnEponOnuTkMacLearningTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 37)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkMacLearningTable.setStatus("current")
_ZxAnEponOnuTkMacLearningEntry_Object = MibTableRow
zxAnEponOnuTkMacLearningEntry = _ZxAnEponOnuTkMacLearningEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 37, 1)
)
zxAnEponOnuTkMacLearningEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkMacLearningEntry.setStatus("current")


class _ZxAnEponOnuTkMacLearningMaxNum_Type(Integer32):
    """Custom type zxAnEponOnuTkMacLearningMaxNum based on Integer32"""
    defaultValue = 64

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 64),
    )


_ZxAnEponOnuTkMacLearningMaxNum_Type.__name__ = "Integer32"
_ZxAnEponOnuTkMacLearningMaxNum_Object = MibTableColumn
zxAnEponOnuTkMacLearningMaxNum = _ZxAnEponOnuTkMacLearningMaxNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 37, 1, 1),
    _ZxAnEponOnuTkMacLearningMaxNum_Type()
)
zxAnEponOnuTkMacLearningMaxNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkMacLearningMaxNum.setStatus("current")


class _ZxAnEponOnuTkMacLearningOamType_Type(Integer32):
    """Custom type zxAnEponOnuTkMacLearningOamType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tk-oam", 1),
          ("kt-oam", 2))
    )


_ZxAnEponOnuTkMacLearningOamType_Type.__name__ = "Integer32"
_ZxAnEponOnuTkMacLearningOamType_Object = MibTableColumn
zxAnEponOnuTkMacLearningOamType = _ZxAnEponOnuTkMacLearningOamType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 37, 1, 2),
    _ZxAnEponOnuTkMacLearningOamType_Type()
)
zxAnEponOnuTkMacLearningOamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkMacLearningOamType.setStatus("current")
_ZxAnEponOnuTkSnoopingTable_Object = MibTable
zxAnEponOnuTkSnoopingTable = _ZxAnEponOnuTkSnoopingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 38)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkSnoopingTable.setStatus("current")
_ZxAnEponOnuTkSnoopingEntry_Object = MibTableRow
zxAnEponOnuTkSnoopingEntry = _ZxAnEponOnuTkSnoopingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 38, 1)
)
zxAnEponOnuTkSnoopingEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkSnoopingEntry.setStatus("current")


class _ZxAnEponOnuTkSnoopingCtrl_Type(Integer32):
    """Custom type zxAnEponOnuTkSnoopingCtrl based on Integer32"""
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


_ZxAnEponOnuTkSnoopingCtrl_Type.__name__ = "Integer32"
_ZxAnEponOnuTkSnoopingCtrl_Object = MibTableColumn
zxAnEponOnuTkSnoopingCtrl = _ZxAnEponOnuTkSnoopingCtrl_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 38, 1, 1),
    _ZxAnEponOnuTkSnoopingCtrl_Type()
)
zxAnEponOnuTkSnoopingCtrl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkSnoopingCtrl.setStatus("current")


class _ZxAnEponOnuTkSnoopingRobustCnt_Type(Integer32):
    """Custom type zxAnEponOnuTkSnoopingRobustCnt based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ZxAnEponOnuTkSnoopingRobustCnt_Type.__name__ = "Integer32"
_ZxAnEponOnuTkSnoopingRobustCnt_Object = MibTableColumn
zxAnEponOnuTkSnoopingRobustCnt = _ZxAnEponOnuTkSnoopingRobustCnt_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 38, 1, 2),
    _ZxAnEponOnuTkSnoopingRobustCnt_Type()
)
zxAnEponOnuTkSnoopingRobustCnt.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkSnoopingRobustCnt.setStatus("current")


class _ZxAnEponOnuTkSnoopingLsmq_Type(Integer32):
    """Custom type zxAnEponOnuTkSnoopingLsmq based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 12),
    )


_ZxAnEponOnuTkSnoopingLsmq_Type.__name__ = "Integer32"
_ZxAnEponOnuTkSnoopingLsmq_Object = MibTableColumn
zxAnEponOnuTkSnoopingLsmq = _ZxAnEponOnuTkSnoopingLsmq_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 38, 1, 3),
    _ZxAnEponOnuTkSnoopingLsmq_Type()
)
zxAnEponOnuTkSnoopingLsmq.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkSnoopingLsmq.setStatus("current")


class _ZxAnEponOnuTkSnoopingMaxGroupNum_Type(Integer32):
    """Custom type zxAnEponOnuTkSnoopingMaxGroupNum based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 16),
    )


_ZxAnEponOnuTkSnoopingMaxGroupNum_Type.__name__ = "Integer32"
_ZxAnEponOnuTkSnoopingMaxGroupNum_Object = MibTableColumn
zxAnEponOnuTkSnoopingMaxGroupNum = _ZxAnEponOnuTkSnoopingMaxGroupNum_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 38, 1, 4),
    _ZxAnEponOnuTkSnoopingMaxGroupNum_Type()
)
zxAnEponOnuTkSnoopingMaxGroupNum.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkSnoopingMaxGroupNum.setStatus("current")
_ZxAnEponOnuTkIgmpTable_Object = MibTable
zxAnEponOnuTkIgmpTable = _ZxAnEponOnuTkIgmpTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 39)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkIgmpTable.setStatus("current")
_ZxAnEponOnuTkIgmpEntry_Object = MibTableRow
zxAnEponOnuTkIgmpEntry = _ZxAnEponOnuTkIgmpEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 39, 1)
)
zxAnEponOnuTkIgmpEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuTkIgmpVlanId"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuTkIgmpIpAddr"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkIgmpEntry.setStatus("current")


class _ZxAnEponOnuTkIgmpVlanId_Type(Integer32):
    """Custom type zxAnEponOnuTkIgmpVlanId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 4094),
    )


_ZxAnEponOnuTkIgmpVlanId_Type.__name__ = "Integer32"
_ZxAnEponOnuTkIgmpVlanId_Object = MibTableColumn
zxAnEponOnuTkIgmpVlanId = _ZxAnEponOnuTkIgmpVlanId_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 39, 1, 1),
    _ZxAnEponOnuTkIgmpVlanId_Type()
)
zxAnEponOnuTkIgmpVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuTkIgmpVlanId.setStatus("current")
_ZxAnEponOnuTkIgmpIpAddr_Type = IpAddress
_ZxAnEponOnuTkIgmpIpAddr_Object = MibTableColumn
zxAnEponOnuTkIgmpIpAddr = _ZxAnEponOnuTkIgmpIpAddr_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 39, 1, 2),
    _ZxAnEponOnuTkIgmpIpAddr_Type()
)
zxAnEponOnuTkIgmpIpAddr.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOnuTkIgmpIpAddr.setStatus("current")
_ZxAnEponOnuTkIgmpPortList_Type = OctetString
_ZxAnEponOnuTkIgmpPortList_Object = MibTableColumn
zxAnEponOnuTkIgmpPortList = _ZxAnEponOnuTkIgmpPortList_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 39, 1, 3),
    _ZxAnEponOnuTkIgmpPortList_Type()
)
zxAnEponOnuTkIgmpPortList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkIgmpPortList.setStatus("current")
_ZxAnEponOnuTkLoopDetectTable_Object = MibTable
zxAnEponOnuTkLoopDetectTable = _ZxAnEponOnuTkLoopDetectTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 40)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkLoopDetectTable.setStatus("current")
_ZxAnEponOnuTkLoopDetectEntry_Object = MibTableRow
zxAnEponOnuTkLoopDetectEntry = _ZxAnEponOnuTkLoopDetectEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 40, 1)
)
zxAnEponOnuTkLoopDetectEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkLoopDetectEntry.setStatus("current")


class _ZxAnEponOnuTkLoopDetectAdminStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkLoopDetectAdminStatus based on Integer32"""
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


_ZxAnEponOnuTkLoopDetectAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkLoopDetectAdminStatus_Object = MibTableColumn
zxAnEponOnuTkLoopDetectAdminStatus = _ZxAnEponOnuTkLoopDetectAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 40, 1, 1),
    _ZxAnEponOnuTkLoopDetectAdminStatus_Type()
)
zxAnEponOnuTkLoopDetectAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkLoopDetectAdminStatus.setStatus("current")


class _ZxAnEponOnuTkLoopDetectInterval_Type(Integer32):
    """Custom type zxAnEponOnuTkLoopDetectInterval based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_ZxAnEponOnuTkLoopDetectInterval_Type.__name__ = "Integer32"
_ZxAnEponOnuTkLoopDetectInterval_Object = MibTableColumn
zxAnEponOnuTkLoopDetectInterval = _ZxAnEponOnuTkLoopDetectInterval_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 40, 1, 2),
    _ZxAnEponOnuTkLoopDetectInterval_Type()
)
zxAnEponOnuTkLoopDetectInterval.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkLoopDetectInterval.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponOnuTkLoopDetectInterval.setUnits("second")


class _ZxAnEponOnuTkLoopDetectOamType_Type(Integer32):
    """Custom type zxAnEponOnuTkLoopDetectOamType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tk-oam", 1),
          ("kt-oam", 2))
    )


_ZxAnEponOnuTkLoopDetectOamType_Type.__name__ = "Integer32"
_ZxAnEponOnuTkLoopDetectOamType_Object = MibTableColumn
zxAnEponOnuTkLoopDetectOamType = _ZxAnEponOnuTkLoopDetectOamType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 40, 1, 3),
    _ZxAnEponOnuTkLoopDetectOamType_Type()
)
zxAnEponOnuTkLoopDetectOamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkLoopDetectOamType.setStatus("current")
_ZxAnEponOnuTkPortShapingTable_Object = MibTable
zxAnEponOnuTkPortShapingTable = _ZxAnEponOnuTkPortShapingTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 41)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortShapingTable.setStatus("current")
_ZxAnEponOnuTkPortShapingEntry_Object = MibTableRow
zxAnEponOnuTkPortShapingEntry = _ZxAnEponOnuTkPortShapingEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 41, 1)
)
zxAnEponOnuTkPortShapingEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortShapingEntry.setStatus("current")


class _ZxAnEponOnuTkPortDsShapingAdminStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkPortDsShapingAdminStatus based on Integer32"""
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


_ZxAnEponOnuTkPortDsShapingAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkPortDsShapingAdminStatus_Object = MibTableColumn
zxAnEponOnuTkPortDsShapingAdminStatus = _ZxAnEponOnuTkPortDsShapingAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 41, 1, 1),
    _ZxAnEponOnuTkPortDsShapingAdminStatus_Type()
)
zxAnEponOnuTkPortDsShapingAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortDsShapingAdminStatus.setStatus("current")
_ZxAnEponOnuTkPortDsShapingRate_Type = Integer32
_ZxAnEponOnuTkPortDsShapingRate_Object = MibTableColumn
zxAnEponOnuTkPortDsShapingRate = _ZxAnEponOnuTkPortDsShapingRate_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 41, 1, 2),
    _ZxAnEponOnuTkPortDsShapingRate_Type()
)
zxAnEponOnuTkPortDsShapingRate.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortDsShapingRate.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortDsShapingRate.setUnits("kbps")


class _ZxAnEponOnuTkPortDsShapingOamType_Type(Integer32):
    """Custom type zxAnEponOnuTkPortDsShapingOamType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tk-oam", 1),
          ("kt-oam", 2))
    )


_ZxAnEponOnuTkPortDsShapingOamType_Type.__name__ = "Integer32"
_ZxAnEponOnuTkPortDsShapingOamType_Object = MibTableColumn
zxAnEponOnuTkPortDsShapingOamType = _ZxAnEponOnuTkPortDsShapingOamType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 31, 41, 1, 3),
    _ZxAnEponOnuTkPortDsShapingOamType_Type()
)
zxAnEponOnuTkPortDsShapingOamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortDsShapingOamType.setStatus("current")
_ZxAnEponOnuTkActionMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuTkActionMgmt = _ZxAnEponOnuTkActionMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32)
)
_ZxAnEponOnuTkRestoreActionTable_Object = MibTable
zxAnEponOnuTkRestoreActionTable = _ZxAnEponOnuTkRestoreActionTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 31)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkRestoreActionTable.setStatus("current")
_ZxAnEponOnuTkRestoreActionEntry_Object = MibTableRow
zxAnEponOnuTkRestoreActionEntry = _ZxAnEponOnuTkRestoreActionEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 31, 1)
)
zxAnEponOnuTkRestoreActionEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkRestoreActionEntry.setStatus("current")


class _ZxAnEponOnuTkRestoreFactorySettings_Type(Integer32):
    """Custom type zxAnEponOnuTkRestoreFactorySettings based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            1
        )
    )
    namedValues = NamedValues(
        ("restore", 1)
    )


_ZxAnEponOnuTkRestoreFactorySettings_Type.__name__ = "Integer32"
_ZxAnEponOnuTkRestoreFactorySettings_Object = MibTableColumn
zxAnEponOnuTkRestoreFactorySettings = _ZxAnEponOnuTkRestoreFactorySettings_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 31, 1, 1),
    _ZxAnEponOnuTkRestoreFactorySettings_Type()
)
zxAnEponOnuTkRestoreFactorySettings.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkRestoreFactorySettings.setStatus("current")


class _ZxAnEponOnuTkRestoreOamType_Type(Integer32):
    """Custom type zxAnEponOnuTkRestoreOamType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tk-oam", 1),
          ("kt-oam", 2))
    )


_ZxAnEponOnuTkRestoreOamType_Type.__name__ = "Integer32"
_ZxAnEponOnuTkRestoreOamType_Object = MibTableColumn
zxAnEponOnuTkRestoreOamType = _ZxAnEponOnuTkRestoreOamType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 31, 1, 2),
    _ZxAnEponOnuTkRestoreOamType_Type()
)
zxAnEponOnuTkRestoreOamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkRestoreOamType.setStatus("current")
_ZxAnEponOnuTkUpdateVerTable_Object = MibTable
zxAnEponOnuTkUpdateVerTable = _ZxAnEponOnuTkUpdateVerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 32)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkUpdateVerTable.setStatus("current")
_ZxAnEponOnuTkUpdateVerEntry_Object = MibTableRow
zxAnEponOnuTkUpdateVerEntry = _ZxAnEponOnuTkUpdateVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 32, 1)
)
zxAnEponOnuTkUpdateVerEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkUpdateVerEntry.setStatus("current")


class _ZxAnEponOnuTkVerType_Type(Integer32):
    """Custom type zxAnEponOnuTkVerType based on Integer32"""
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
        *(("boot", 1),
          ("application", 2),
          ("personality", 3),
          ("diagnostic", 4),
          ("dsan", 5))
    )


_ZxAnEponOnuTkVerType_Type.__name__ = "Integer32"
_ZxAnEponOnuTkVerType_Object = MibTableColumn
zxAnEponOnuTkVerType = _ZxAnEponOnuTkVerType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 32, 1, 1),
    _ZxAnEponOnuTkVerType_Type()
)
zxAnEponOnuTkVerType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkVerType.setStatus("current")
_ZxAnEponOnuTkVerName_Type = DisplayString
_ZxAnEponOnuTkVerName_Object = MibTableColumn
zxAnEponOnuTkVerName = _ZxAnEponOnuTkVerName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 32, 1, 2),
    _ZxAnEponOnuTkVerName_Type()
)
zxAnEponOnuTkVerName.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkVerName.setStatus("current")


class _ZxAnEponOnuTkUpdateStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkUpdateStatus based on Integer32"""
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
        *(("noStart", 1),
          ("failed", 2),
          ("downloading", 3),
          ("writtingImage", 4),
          ("finished", 5))
    )


_ZxAnEponOnuTkUpdateStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkUpdateStatus_Object = MibTableColumn
zxAnEponOnuTkUpdateStatus = _ZxAnEponOnuTkUpdateStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 32, 1, 3),
    _ZxAnEponOnuTkUpdateStatus_Type()
)
zxAnEponOnuTkUpdateStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkUpdateStatus.setStatus("current")


class _ZxAnEponOnuTkUpdateProgress_Type(Integer32):
    """Custom type zxAnEponOnuTkUpdateProgress based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 100),
    )


_ZxAnEponOnuTkUpdateProgress_Type.__name__ = "Integer32"
_ZxAnEponOnuTkUpdateProgress_Object = MibTableColumn
zxAnEponOnuTkUpdateProgress = _ZxAnEponOnuTkUpdateProgress_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 32, 1, 4),
    _ZxAnEponOnuTkUpdateProgress_Type()
)
zxAnEponOnuTkUpdateProgress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkUpdateProgress.setStatus("current")
if mibBuilder.loadTexts:
    zxAnEponOnuTkUpdateProgress.setUnits("percent")
_ZxAnEponOnuTkOnuAckCode_Type = Integer32
_ZxAnEponOnuTkOnuAckCode_Object = MibTableColumn
zxAnEponOnuTkOnuAckCode = _ZxAnEponOnuTkOnuAckCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 32, 1, 5),
    _ZxAnEponOnuTkOnuAckCode_Type()
)
zxAnEponOnuTkOnuAckCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkOnuAckCode.setStatus("current")
_ZxAnEponOnuTkErrorCode_Type = Integer32
_ZxAnEponOnuTkErrorCode_Object = MibTableColumn
zxAnEponOnuTkErrorCode = _ZxAnEponOnuTkErrorCode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 32, 1, 6),
    _ZxAnEponOnuTkErrorCode_Type()
)
zxAnEponOnuTkErrorCode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkErrorCode.setStatus("current")
_ZxAnEponOnuTkUpdattingVerName_Type = DisplayString
_ZxAnEponOnuTkUpdattingVerName_Object = MibTableColumn
zxAnEponOnuTkUpdattingVerName = _ZxAnEponOnuTkUpdattingVerName_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 32, 1, 7),
    _ZxAnEponOnuTkUpdattingVerName_Type()
)
zxAnEponOnuTkUpdattingVerName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkUpdattingVerName.setStatus("current")
_ZxAnEponOnuTkAutoUpdateVerTable_Object = MibTable
zxAnEponOnuTkAutoUpdateVerTable = _ZxAnEponOnuTkAutoUpdateVerTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 33)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkAutoUpdateVerTable.setStatus("current")
_ZxAnEponOnuTkAutoUpdateVerEntry_Object = MibTableRow
zxAnEponOnuTkAutoUpdateVerEntry = _ZxAnEponOnuTkAutoUpdateVerEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 33, 1)
)
zxAnEponOnuTkAutoUpdateVerEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOltIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkAutoUpdateVerEntry.setStatus("current")
_ZxAnEponOltIfIndex_Type = Integer32
_ZxAnEponOltIfIndex_Object = MibTableColumn
zxAnEponOltIfIndex = _ZxAnEponOltIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 33, 1, 1),
    _ZxAnEponOltIfIndex_Type()
)
zxAnEponOltIfIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    zxAnEponOltIfIndex.setStatus("current")


class _ZxAnEponOnuTkAutoUpdateAdminStatus_Type(Integer32):
    """Custom type zxAnEponOnuTkAutoUpdateAdminStatus based on Integer32"""
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


_ZxAnEponOnuTkAutoUpdateAdminStatus_Type.__name__ = "Integer32"
_ZxAnEponOnuTkAutoUpdateAdminStatus_Object = MibTableColumn
zxAnEponOnuTkAutoUpdateAdminStatus = _ZxAnEponOnuTkAutoUpdateAdminStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 33, 1, 2),
    _ZxAnEponOnuTkAutoUpdateAdminStatus_Type()
)
zxAnEponOnuTkAutoUpdateAdminStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkAutoUpdateAdminStatus.setStatus("current")


class _ZxAnEponOnuTkVerActiveMode_Type(Integer32):
    """Custom type zxAnEponOnuTkVerActiveMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("immediately", 1),
          ("next", 2))
    )


_ZxAnEponOnuTkVerActiveMode_Type.__name__ = "Integer32"
_ZxAnEponOnuTkVerActiveMode_Object = MibTableColumn
zxAnEponOnuTkVerActiveMode = _ZxAnEponOnuTkVerActiveMode_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 32, 33, 1, 3),
    _ZxAnEponOnuTkVerActiveMode_Type()
)
zxAnEponOnuTkVerActiveMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkVerActiveMode.setStatus("current")
_ZxAnEponOnuTkStatisticMgmt_ObjectIdentity = ObjectIdentity
zxAnEponOnuTkStatisticMgmt = _ZxAnEponOnuTkStatisticMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33)
)
_ZxAnEponOnuTkGlobalStatTable_Object = MibTable
zxAnEponOnuTkGlobalStatTable = _ZxAnEponOnuTkGlobalStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 31)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalStatTable.setStatus("current")
_ZxAnEponOnuTkGlobalStatEntry_Object = MibTableRow
zxAnEponOnuTkGlobalStatEntry = _ZxAnEponOnuTkGlobalStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 31, 1)
)
zxAnEponOnuTkGlobalStatEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalStatEntry.setStatus("current")
_ZxAnEponOnuTkGlobalStatResetCounter_Type = Integer32
_ZxAnEponOnuTkGlobalStatResetCounter_Object = MibTableColumn
zxAnEponOnuTkGlobalStatResetCounter = _ZxAnEponOnuTkGlobalStatResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 31, 1, 1),
    _ZxAnEponOnuTkGlobalStatResetCounter_Type()
)
zxAnEponOnuTkGlobalStatResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalStatResetCounter.setStatus("current")


class _ZxAnEponOnuTkGlobalStatOamType_Type(Integer32):
    """Custom type zxAnEponOnuTkGlobalStatOamType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tk-oam", 1),
          ("kt-oam", 2))
    )


_ZxAnEponOnuTkGlobalStatOamType_Type.__name__ = "Integer32"
_ZxAnEponOnuTkGlobalStatOamType_Object = MibTableColumn
zxAnEponOnuTkGlobalStatOamType = _ZxAnEponOnuTkGlobalStatOamType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 31, 1, 2),
    _ZxAnEponOnuTkGlobalStatOamType_Type()
)
zxAnEponOnuTkGlobalStatOamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalStatOamType.setStatus("current")
_ZxAnEponOnuTkGlobalStatTxRegReq_Type = Counter64
_ZxAnEponOnuTkGlobalStatTxRegReq_Object = MibTableColumn
zxAnEponOnuTkGlobalStatTxRegReq = _ZxAnEponOnuTkGlobalStatTxRegReq_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 31, 1, 32),
    _ZxAnEponOnuTkGlobalStatTxRegReq_Type()
)
zxAnEponOnuTkGlobalStatTxRegReq.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalStatTxRegReq.setStatus("current")
_ZxAnEponOnuTkGlobalStatRxReg_Type = Counter64
_ZxAnEponOnuTkGlobalStatRxReg_Object = MibTableColumn
zxAnEponOnuTkGlobalStatRxReg = _ZxAnEponOnuTkGlobalStatRxReg_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 31, 1, 33),
    _ZxAnEponOnuTkGlobalStatRxReg_Type()
)
zxAnEponOnuTkGlobalStatRxReg.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalStatRxReg.setStatus("current")
_ZxAnEponOnuTkGlobalStatTxRegAck_Type = Counter64
_ZxAnEponOnuTkGlobalStatTxRegAck_Object = MibTableColumn
zxAnEponOnuTkGlobalStatTxRegAck = _ZxAnEponOnuTkGlobalStatTxRegAck_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 31, 1, 34),
    _ZxAnEponOnuTkGlobalStatTxRegAck_Type()
)
zxAnEponOnuTkGlobalStatTxRegAck.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalStatTxRegAck.setStatus("current")
_ZxAnEponOnuTkGlobalStatRxGateFrames_Type = Counter64
_ZxAnEponOnuTkGlobalStatRxGateFrames_Object = MibTableColumn
zxAnEponOnuTkGlobalStatRxGateFrames = _ZxAnEponOnuTkGlobalStatRxGateFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 31, 1, 35),
    _ZxAnEponOnuTkGlobalStatRxGateFrames_Type()
)
zxAnEponOnuTkGlobalStatRxGateFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalStatRxGateFrames.setStatus("current")
_ZxAnEponOnuTkGlobalStatTxReportFrames_Type = Counter64
_ZxAnEponOnuTkGlobalStatTxReportFrames_Object = MibTableColumn
zxAnEponOnuTkGlobalStatTxReportFrames = _ZxAnEponOnuTkGlobalStatTxReportFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 31, 1, 36),
    _ZxAnEponOnuTkGlobalStatTxReportFrames_Type()
)
zxAnEponOnuTkGlobalStatTxReportFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkGlobalStatTxReportFrames.setStatus("current")
_ZxAnEponOnuTkPortStatTable_Object = MibTable
zxAnEponOnuTkPortStatTable = _ZxAnEponOnuTkPortStatTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32)
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatTable.setStatus("current")
_ZxAnEponOnuTkPortStatEntry_Object = MibTableRow
zxAnEponOnuTkPortStatEntry = _ZxAnEponOnuTkPortStatEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1)
)
zxAnEponOnuTkPortStatEntry.setIndexNames(
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuIfIndex"),
    (0, "ZXANEPON-ONUMGMT-MIB", "zxAnEponOnuPortId"),
)
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatEntry.setStatus("current")
_ZxAnEponOnuTkPortStatResetCounter_Type = Integer32
_ZxAnEponOnuTkPortStatResetCounter_Object = MibTableColumn
zxAnEponOnuTkPortStatResetCounter = _ZxAnEponOnuTkPortStatResetCounter_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 1),
    _ZxAnEponOnuTkPortStatResetCounter_Type()
)
zxAnEponOnuTkPortStatResetCounter.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatResetCounter.setStatus("current")


class _ZxAnEponOnuTkPortStatOamType_Type(Integer32):
    """Custom type zxAnEponOnuTkPortStatOamType based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("tk-oam", 1),
          ("kt-oam", 2))
    )


_ZxAnEponOnuTkPortStatOamType_Type.__name__ = "Integer32"
_ZxAnEponOnuTkPortStatOamType_Object = MibTableColumn
zxAnEponOnuTkPortStatOamType = _ZxAnEponOnuTkPortStatOamType_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 2),
    _ZxAnEponOnuTkPortStatOamType_Type()
)
zxAnEponOnuTkPortStatOamType.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatOamType.setStatus("current")
_ZxAnEponOnuTkPortStatTxFrames_Type = Counter64
_ZxAnEponOnuTkPortStatTxFrames_Object = MibTableColumn
zxAnEponOnuTkPortStatTxFrames = _ZxAnEponOnuTkPortStatTxFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 31),
    _ZxAnEponOnuTkPortStatTxFrames_Type()
)
zxAnEponOnuTkPortStatTxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatTxFrames.setStatus("current")
_ZxAnEponOnuTkPortStatTxBytes_Type = Counter64
_ZxAnEponOnuTkPortStatTxBytes_Object = MibTableColumn
zxAnEponOnuTkPortStatTxBytes = _ZxAnEponOnuTkPortStatTxBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 32),
    _ZxAnEponOnuTkPortStatTxBytes_Type()
)
zxAnEponOnuTkPortStatTxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatTxBytes.setStatus("current")
_ZxAnEponOnuTkPortStatTxMulticast_Type = Counter64
_ZxAnEponOnuTkPortStatTxMulticast_Object = MibTableColumn
zxAnEponOnuTkPortStatTxMulticast = _ZxAnEponOnuTkPortStatTxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 33),
    _ZxAnEponOnuTkPortStatTxMulticast_Type()
)
zxAnEponOnuTkPortStatTxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatTxMulticast.setStatus("current")
_ZxAnEponOnuTkPortStatTxBroadcast_Type = Counter64
_ZxAnEponOnuTkPortStatTxBroadcast_Object = MibTableColumn
zxAnEponOnuTkPortStatTxBroadcast = _ZxAnEponOnuTkPortStatTxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 34),
    _ZxAnEponOnuTkPortStatTxBroadcast_Type()
)
zxAnEponOnuTkPortStatTxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatTxBroadcast.setStatus("current")
_ZxAnEponOnuTkPortStatTxDropedFrames_Type = Counter64
_ZxAnEponOnuTkPortStatTxDropedFrames_Object = MibTableColumn
zxAnEponOnuTkPortStatTxDropedFrames = _ZxAnEponOnuTkPortStatTxDropedFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 35),
    _ZxAnEponOnuTkPortStatTxDropedFrames_Type()
)
zxAnEponOnuTkPortStatTxDropedFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatTxDropedFrames.setStatus("current")
_ZxAnEponOnuTkPortStatRxFrames_Type = Counter64
_ZxAnEponOnuTkPortStatRxFrames_Object = MibTableColumn
zxAnEponOnuTkPortStatRxFrames = _ZxAnEponOnuTkPortStatRxFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 36),
    _ZxAnEponOnuTkPortStatRxFrames_Type()
)
zxAnEponOnuTkPortStatRxFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatRxFrames.setStatus("current")
_ZxAnEponOnuTkPortStatRxBytes_Type = Counter64
_ZxAnEponOnuTkPortStatRxBytes_Object = MibTableColumn
zxAnEponOnuTkPortStatRxBytes = _ZxAnEponOnuTkPortStatRxBytes_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 37),
    _ZxAnEponOnuTkPortStatRxBytes_Type()
)
zxAnEponOnuTkPortStatRxBytes.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatRxBytes.setStatus("current")
_ZxAnEponOnuTkPortStatRxMulticast_Type = Counter64
_ZxAnEponOnuTkPortStatRxMulticast_Object = MibTableColumn
zxAnEponOnuTkPortStatRxMulticast = _ZxAnEponOnuTkPortStatRxMulticast_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 38),
    _ZxAnEponOnuTkPortStatRxMulticast_Type()
)
zxAnEponOnuTkPortStatRxMulticast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatRxMulticast.setStatus("current")
_ZxAnEponOnuTkPortStatRxBroadcast_Type = Counter64
_ZxAnEponOnuTkPortStatRxBroadcast_Object = MibTableColumn
zxAnEponOnuTkPortStatRxBroadcast = _ZxAnEponOnuTkPortStatRxBroadcast_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 39),
    _ZxAnEponOnuTkPortStatRxBroadcast_Type()
)
zxAnEponOnuTkPortStatRxBroadcast.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatRxBroadcast.setStatus("current")
_ZxAnEponOnuTkPortStatRxOversizeFrames_Type = Counter64
_ZxAnEponOnuTkPortStatRxOversizeFrames_Object = MibTableColumn
zxAnEponOnuTkPortStatRxOversizeFrames = _ZxAnEponOnuTkPortStatRxOversizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 40),
    _ZxAnEponOnuTkPortStatRxOversizeFrames_Type()
)
zxAnEponOnuTkPortStatRxOversizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatRxOversizeFrames.setStatus("current")
_ZxAnEponOnuTkPortStatRxUnderSizeFrames_Type = Counter64
_ZxAnEponOnuTkPortStatRxUnderSizeFrames_Object = MibTableColumn
zxAnEponOnuTkPortStatRxUnderSizeFrames = _ZxAnEponOnuTkPortStatRxUnderSizeFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 41),
    _ZxAnEponOnuTkPortStatRxUnderSizeFrames_Type()
)
zxAnEponOnuTkPortStatRxUnderSizeFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatRxUnderSizeFrames.setStatus("current")
_ZxAnEponOnuTkPortStatRxCrcFrames_Type = Counter64
_ZxAnEponOnuTkPortStatRxCrcFrames_Object = MibTableColumn
zxAnEponOnuTkPortStatRxCrcFrames = _ZxAnEponOnuTkPortStatRxCrcFrames_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1015, 1010, 1, 1, 101, 31, 33, 32, 1, 42),
    _ZxAnEponOnuTkPortStatRxCrcFrames_Type()
)
zxAnEponOnuTkPortStatRxCrcFrames.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    zxAnEponOnuTkPortStatRxCrcFrames.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZXANEPON-ONUMGMT-MIB",
    **{"zxAnEponOnuRemoteMgmt": zxAnEponOnuRemoteMgmt,
       "zxAnEponOnuExtendedAttrMgmt": zxAnEponOnuExtendedAttrMgmt,
       "zxAnEponOnuSnTable": zxAnEponOnuSnTable,
       "zxAnEponOnuSnEntry": zxAnEponOnuSnEntry,
       "zxAnEponOnuIfIndex": zxAnEponOnuIfIndex,
       "zxAnEponOnuVendorId": zxAnEponOnuVendorId,
       "zxAnEponOnuModel": zxAnEponOnuModel,
       "zxAnEponOnuMacAddr": zxAnEponOnuMacAddr,
       "zxAnEponOnuHardwareVersion": zxAnEponOnuHardwareVersion,
       "zxAnEponOnuSoftwareVersion": zxAnEponOnuSoftwareVersion,
       "zxAnEponOnuExtendedModel": zxAnEponOnuExtendedModel,
       "zxAnEponOnuFirmwareVerTable": zxAnEponOnuFirmwareVerTable,
       "zxAnEponOnuFirmwareVerEntry": zxAnEponOnuFirmwareVerEntry,
       "zxAnEponOnuFirmwareVer": zxAnEponOnuFirmwareVer,
       "zxAnEponOnuChipsetIdTable": zxAnEponOnuChipsetIdTable,
       "zxAnEponOnuChipsetIdEntry": zxAnEponOnuChipsetIdEntry,
       "zxAnEponOnuChipVendorId": zxAnEponOnuChipVendorId,
       "zxAnEponOnuChipModel": zxAnEponOnuChipModel,
       "zxAnEponOnuChipRevision": zxAnEponOnuChipRevision,
       "zxAnEponOnuChipDate": zxAnEponOnuChipDate,
       "zxAnEponOnuCapabilityTable": zxAnEponOnuCapabilityTable,
       "zxAnEponOnuCapabilityEntry": zxAnEponOnuCapabilityEntry,
       "zxAnEponOnuServiceSupported": zxAnEponOnuServiceSupported,
       "zxAnEponOnuGePortNumber": zxAnEponOnuGePortNumber,
       "zxAnEponOnuGePortBitmap": zxAnEponOnuGePortBitmap,
       "zxAnEponOnuFePortNumber": zxAnEponOnuFePortNumber,
       "zxAnEponOnuFePortBitmap": zxAnEponOnuFePortBitmap,
       "zxAnEponOnuPotsPortNumber": zxAnEponOnuPotsPortNumber,
       "zxAnEponOnuE1PortNumber": zxAnEponOnuE1PortNumber,
       "zxAnEponOnuUsQueueNumber": zxAnEponOnuUsQueueNumber,
       "zxAnEponOnuUsPortMaxQueueNumber": zxAnEponOnuUsPortMaxQueueNumber,
       "zxAnEponOnuDsQueueNumber": zxAnEponOnuDsQueueNumber,
       "zxAnEponOnuDsPortMaxQueueNumber": zxAnEponOnuDsPortMaxQueueNumber,
       "zxAnEponOnuBatteryBackup": zxAnEponOnuBatteryBackup,
       "zxAnEponOnuEthLinkStateTable": zxAnEponOnuEthLinkStateTable,
       "zxAnEponOnuEthLinkStateEntry": zxAnEponOnuEthLinkStateEntry,
       "zxAnEponOnuPortId": zxAnEponOnuPortId,
       "zxAnEponOnuEthPortLinkState": zxAnEponOnuEthPortLinkState,
       "zxAnEponOnuEthPortPauseTable": zxAnEponOnuEthPortPauseTable,
       "zxAnEponOnuEthPortPauseEntry": zxAnEponOnuEthPortPauseEntry,
       "zxAnEponOnuPortBackPressure": zxAnEponOnuPortBackPressure,
       "zxAnEponOnuEthPortPolicingTable": zxAnEponOnuEthPortPolicingTable,
       "zxAnEponOnuEthPortPolicingEntry": zxAnEponOnuEthPortPolicingEntry,
       "zxAnEponOnuPortPolicing": zxAnEponOnuPortPolicing,
       "zxAnEponOnuPortPolicingCir": zxAnEponOnuPortPolicingCir,
       "zxAnEponOnuPortPolicingBucketDepth": zxAnEponOnuPortPolicingBucketDepth,
       "zxAnEponOnuPortPolicingExtraBurstSize": zxAnEponOnuPortPolicingExtraBurstSize,
       "zxAnEponOnuPortPolicingDownStream": zxAnEponOnuPortPolicingDownStream,
       "zxAnEponOnuPortPolicingCirDownStream": zxAnEponOnuPortPolicingCirDownStream,
       "zxAnEponOnuPortPolicingBucketDepthDownStream": zxAnEponOnuPortPolicingBucketDepthDownStream,
       "zxAnEponOnuPortPolicingExtraBurstSizeDownStream": zxAnEponOnuPortPolicingExtraBurstSizeDownStream,
       "zxAnEponOnuVoipPortTable": zxAnEponOnuVoipPortTable,
       "zxAnEponOnuVoipPortEntry": zxAnEponOnuVoipPortEntry,
       "zxAnEponOnuVoipPortEnable": zxAnEponOnuVoipPortEnable,
       "zxAnEponOnuE1PortTable": zxAnEponOnuE1PortTable,
       "zxAnEponOnuE1PortEntry": zxAnEponOnuE1PortEntry,
       "zxAnEponOnuE1PortEnable": zxAnEponOnuE1PortEnable,
       "zxAnEponOnuVlanCfgMgmt": zxAnEponOnuVlanCfgMgmt,
       "zxAnEponOnuVlanCfgTable": zxAnEponOnuVlanCfgTable,
       "zxAnEponOnuVlanCfgEntry": zxAnEponOnuVlanCfgEntry,
       "zxAnEponOnuVlanMode": zxAnEponOnuVlanMode,
       "zxAnEponOnuVlanCfgState": zxAnEponOnuVlanCfgState,
       "zxAnEponOnuVlanTagTable": zxAnEponOnuVlanTagTable,
       "zxAnEponOnuVlanTagEntry": zxAnEponOnuVlanTagEntry,
       "zxAnEponOnuVlanTagVid": zxAnEponOnuVlanTagVid,
       "zxAnEponOnuVlanTagTpid": zxAnEponOnuVlanTagTpid,
       "zxAnEponOnuVlanTagCfi": zxAnEponOnuVlanTagCfi,
       "zxAnEponOnuVlanPriority": zxAnEponOnuVlanPriority,
       "zxAnEponOnuVlanTranslationTable": zxAnEponOnuVlanTranslationTable,
       "zxAnEponOnuVlanTranslationEntry": zxAnEponOnuVlanTranslationEntry,
       "zxAnEponOnuVlanTransModeEntryId": zxAnEponOnuVlanTransModeEntryId,
       "zxAnEponOnuVlanTransOriginalTag": zxAnEponOnuVlanTransOriginalTag,
       "zxAnEponOnuVlanTransNewTag": zxAnEponOnuVlanTransNewTag,
       "zxAnEponOnuVlanTransModeRowStatus": zxAnEponOnuVlanTransModeRowStatus,
       "zxAnEponOnuVlanTrunkTable": zxAnEponOnuVlanTrunkTable,
       "zxAnEponOnuVlanTrunkEntry": zxAnEponOnuVlanTrunkEntry,
       "zxAnEponOnuVlanTrunkModeVlan": zxAnEponOnuVlanTrunkModeVlan,
       "zxAnEponOnuVlanAggregationTable": zxAnEponOnuVlanAggregationTable,
       "zxAnEponOnuVlanAggregationEntry": zxAnEponOnuVlanAggregationEntry,
       "zxAnEponOnuVlanAggGrpId": zxAnEponOnuVlanAggGrpId,
       "zxAnEponOnuVlamAggSrcVlanList": zxAnEponOnuVlamAggSrcVlanList,
       "zxAnEponOnuVlanAggDestVlan": zxAnEponOnuVlanAggDestVlan,
       "zxAnEponOnuVlanAggRowStatus": zxAnEponOnuVlanAggRowStatus,
       "zxAnEponOnuClassMarkingAttrMgmt": zxAnEponOnuClassMarkingAttrMgmt,
       "zxAnEponOnuClassMarkingConditionTable": zxAnEponOnuClassMarkingConditionTable,
       "zxAnEponOnuClassMarkingConditionEntry": zxAnEponOnuClassMarkingConditionEntry,
       "zxAnEponOnuClassMarkingConditionId": zxAnEponOnuClassMarkingConditionId,
       "zxAnEponOnuClassMarkingConditionName": zxAnEponOnuClassMarkingConditionName,
       "zxAnEponOnuClassMarkingField": zxAnEponOnuClassMarkingField,
       "zxAnEponOnuClassMarkingMatchValue": zxAnEponOnuClassMarkingMatchValue,
       "zxAnEponOnuClassMarkingOperator": zxAnEponOnuClassMarkingOperator,
       "zxAnEponOnuClassMarkingConditionRefCnt": zxAnEponOnuClassMarkingConditionRefCnt,
       "zxAnEponOnuClassMarkingConditionRowStatus": zxAnEponOnuClassMarkingConditionRowStatus,
       "zxAnEponOnuClassMarkingRuleTable": zxAnEponOnuClassMarkingRuleTable,
       "zxAnEponOnuClassMarkingRuleEntry": zxAnEponOnuClassMarkingRuleEntry,
       "zxAnEponOnuClassMarkingRuleId": zxAnEponOnuClassMarkingRuleId,
       "zxAnEponOnuClassMarkingRuleName": zxAnEponOnuClassMarkingRuleName,
       "zxAnEponOnuClassMarkingQueue": zxAnEponOnuClassMarkingQueue,
       "zxAnEponOnuClassMarkingPriority": zxAnEponOnuClassMarkingPriority,
       "zxAnEponOnuClassMarkingRuleRefCnt": zxAnEponOnuClassMarkingRuleRefCnt,
       "zxAnEponOnuClassMarkingRuleRowStatus": zxAnEponOnuClassMarkingRuleRowStatus,
       "zxAnEponOnuClassMarkingTable": zxAnEponOnuClassMarkingTable,
       "zxAnEponOnuClassMarkingEntry": zxAnEponOnuClassMarkingEntry,
       "zxAnEponOnuClassMarkingRulePrecedence": zxAnEponOnuClassMarkingRulePrecedence,
       "zxAnEponOnuClassMarkingRuleIndex": zxAnEponOnuClassMarkingRuleIndex,
       "zxAnEponOnuClassMarkingRuleConditionList": zxAnEponOnuClassMarkingRuleConditionList,
       "zxAnEponOnuClassMarkingRowStatus": zxAnEponOnuClassMarkingRowStatus,
       "zxAnEponOnuClassMarkingRulePriority": zxAnEponOnuClassMarkingRulePriority,
       "zxAnEponOnuClassMarkingRuleDirection": zxAnEponOnuClassMarkingRuleDirection,
       "zxAnEponOnuClassMarkingRuleType": zxAnEponOnuClassMarkingRuleType,
       "zxAnEponOnuClassMarkingClearTable": zxAnEponOnuClassMarkingClearTable,
       "zxAnEponOnuClassMarkingClearEntry": zxAnEponOnuClassMarkingClearEntry,
       "zxAnEponOnuClassMarkingClear": zxAnEponOnuClassMarkingClear,
       "zxAnEponOnuClassMarkingCompatibilityTable": zxAnEponOnuClassMarkingCompatibilityTable,
       "zxAnEponOnuClassMarkingCompatibilityEntry": zxAnEponOnuClassMarkingCompatibilityEntry,
       "zxAnEponOnuClassMarkingRulePriorityFlag": zxAnEponOnuClassMarkingRulePriorityFlag,
       "zxAnEponOnuClassMarkingRuleDirectionFlag": zxAnEponOnuClassMarkingRuleDirectionFlag,
       "zxAnEponOnuClassMarkingRuleTypeFlag": zxAnEponOnuClassMarkingRuleTypeFlag,
       "zxAnEponOnuMulticastVlanTable": zxAnEponOnuMulticastVlanTable,
       "zxAnEponOnuMulticastVlanEntry": zxAnEponOnuMulticastVlanEntry,
       "zxAnEponOnuMulticastVlanAction": zxAnEponOnuMulticastVlanAction,
       "zxAnEponOnuMulticastVlanList": zxAnEponOnuMulticastVlanList,
       "zxAnEponOnuMulticastTagCfgTable": zxAnEponOnuMulticastTagCfgTable,
       "zxAnEponOnuMulticastTagCfgEntry": zxAnEponOnuMulticastTagCfgEntry,
       "zxAnEponOnuMulticastTagStripe": zxAnEponOnuMulticastTagStripe,
       "zxAnEponOnuMulticastSwitchTable": zxAnEponOnuMulticastSwitchTable,
       "zxAnEponOnuMulticastSwitchEntry": zxAnEponOnuMulticastSwitchEntry,
       "zxAnEponOnuMulticastSwitchAttr": zxAnEponOnuMulticastSwitchAttr,
       "zxAnEponOnuMulticastControlMgmt": zxAnEponOnuMulticastControlMgmt,
       "zxAnEponOnuMulticastControlClearTable": zxAnEponOnuMulticastControlClearTable,
       "zxAnEponOnuMulticastControlClearEntry": zxAnEponOnuMulticastControlClearEntry,
       "zxAnEponOnuMcstCtrlClear": zxAnEponOnuMcstCtrlClear,
       "zxAnEponOnuMulticastControlTable": zxAnEponOnuMulticastControlTable,
       "zxAnEponOnuMulticastControlEntry": zxAnEponOnuMulticastControlEntry,
       "zxAnEponOnuMcstCtrlEntryIndex": zxAnEponOnuMcstCtrlEntryIndex,
       "zxAnEponOnuMcstCtrlAction": zxAnEponOnuMcstCtrlAction,
       "zxAnEponOnuMcstCtrlType": zxAnEponOnuMcstCtrlType,
       "zxAnEponOnuMcstCtrlUserId": zxAnEponOnuMcstCtrlUserId,
       "zxAnEponOnuMcstCtrlGda": zxAnEponOnuMcstCtrlGda,
       "zxAnEponOnuMcstCtrlMvlan": zxAnEponOnuMcstCtrlMvlan,
       "zxAnEponOnuMcstCtrlGdaIp": zxAnEponOnuMcstCtrlGdaIp,
       "zxAnEponOnuMaxGroupNumTable": zxAnEponOnuMaxGroupNumTable,
       "zxAnEponOnuMaxGroupNumEntry": zxAnEponOnuMaxGroupNumEntry,
       "zxAnEponOnuMaxGroupNum": zxAnEponOnuMaxGroupNum,
       "zxAnEponOnuAlarmCtrlTable": zxAnEponOnuAlarmCtrlTable,
       "zxAnEponOnuAlarmCtrlEntry": zxAnEponOnuAlarmCtrlEntry,
       "zxAnEponOnuAlarmCtr": zxAnEponOnuAlarmCtr,
       "zxAnEponOnuMACNumTable": zxAnEponOnuMACNumTable,
       "zxAnEponOnuMACNumEntry": zxAnEponOnuMACNumEntry,
       "zxAnEponOnuMACNum": zxAnEponOnuMACNum,
       "zxAnEponOnuUniLearnedMacs": zxAnEponOnuUniLearnedMacs,
       "zxAnEponOnuMACAgingTimeTable": zxAnEponOnuMACAgingTimeTable,
       "zxAnEponOnuMACAgingTimeEntry": zxAnEponOnuMACAgingTimeEntry,
       "zxAnEponOnuMACAgingTimeAttr": zxAnEponOnuMACAgingTimeAttr,
       "zxAnEponOnuFilterMACTable": zxAnEponOnuFilterMACTable,
       "zxAnEponOnuFilterMACEntry": zxAnEponOnuFilterMACEntry,
       "zxAnEponOnuFilterMAC": zxAnEponOnuFilterMAC,
       "zxEponFilterVlan": zxEponFilterVlan,
       "zxAnEponOnuFilterMACEntryStatus": zxAnEponOnuFilterMACEntryStatus,
       "zxAnEponOnuBindMACTable": zxAnEponOnuBindMACTable,
       "zxAnEponOnuBindMACEntry": zxAnEponOnuBindMACEntry,
       "zxAnEponOnuBindMAC": zxAnEponOnuBindMAC,
       "zxEponBindVlan": zxEponBindVlan,
       "zxAnEponOnuBindMACEntryStatus": zxAnEponOnuBindMACEntryStatus,
       "zxAnEponOnuStaticMACTable": zxAnEponOnuStaticMACTable,
       "zxAnEponOnuStaticMACEntry": zxAnEponOnuStaticMACEntry,
       "zxAnEponOnuStaticMAC": zxAnEponOnuStaticMAC,
       "zxEponStaticVlan": zxEponStaticVlan,
       "zxAnEponOnuStaicMACEntryStatus": zxAnEponOnuStaicMACEntryStatus,
       "zxAnEponOnuMACAddressClearTable": zxAnEponOnuMACAddressClearTable,
       "zxAnEponOnuMACAddressClearEntry": zxAnEponOnuMACAddressClearEntry,
       "zxAnEponOnuMACAddressType": zxAnEponOnuMACAddressType,
       "zxAnEponOnuManagerIPTable": zxAnEponOnuManagerIPTable,
       "zxAnEponOnuManagerIPTableEntry": zxAnEponOnuManagerIPTableEntry,
       "zxEponOnuIPAddress": zxEponOnuIPAddress,
       "zxEponOnuIPMask": zxEponOnuIPMask,
       "zxEponMangementPriority": zxEponMangementPriority,
       "zxEponMangementVlan": zxEponMangementVlan,
       "zxEponManagementHostIP": zxEponManagementHostIP,
       "zxEponManagementHostMask": zxEponManagementHostMask,
       "zxEponManagementGateway": zxEponManagementGateway,
       "zxEponOnuIPConfigureStatus": zxEponOnuIPConfigureStatus,
       "zxEponMangementSVlan": zxEponMangementSVlan,
       "zxAnEponOnuIsolationCtrlTable": zxAnEponOnuIsolationCtrlTable,
       "zxAnEponOnuIsolationCtrlEntry": zxAnEponOnuIsolationCtrlEntry,
       "zxAnEponOnuIsolationCtr": zxAnEponOnuIsolationCtr,
       "zxAnEponRmFastLeaveAbiTable": zxAnEponRmFastLeaveAbiTable,
       "zxAnEponRmFastLeaveAbiEntry": zxAnEponRmFastLeaveAbiEntry,
       "fastleaveabi": fastleaveabi,
       "eponRmFastLeaveAdminStateTable": eponRmFastLeaveAdminStateTable,
       "eponRmFastLeaveAdminStateEntry": eponRmFastLeaveAdminStateEntry,
       "getState": getState,
       "eponIpGlobalTable": eponIpGlobalTable,
       "eponIpGlobalEntry": eponIpGlobalEntry,
       "zxAnEponOnuVioceCardIndex": zxAnEponOnuVioceCardIndex,
       "zxAnEponOnuVoiceIpMngIpRelation": zxAnEponOnuVoiceIpMngIpRelation,
       "zxAnEponOnuVoiceIpMode": zxAnEponOnuVoiceIpMode,
       "zxAnEponOnuVoiceIpAddress": zxAnEponOnuVoiceIpAddress,
       "zxAnEponOnuVoiceDnsServer": zxAnEponOnuVoiceDnsServer,
       "zxAnEponOnuVoiceIpMask": zxAnEponOnuVoiceIpMask,
       "zxAnEponOnuVoiceGateway": zxAnEponOnuVoiceGateway,
       "zxAnEponOnuVoicePPPoEMode": zxAnEponOnuVoicePPPoEMode,
       "zxAnEponOnuVoicePPPoEUserName": zxAnEponOnuVoicePPPoEUserName,
       "zxAnEponOnuVoicePPPoEPassword": zxAnEponOnuVoicePPPoEPassword,
       "zxAnEponOnuVoiceTaggedFlag": zxAnEponOnuVoiceTaggedFlag,
       "zxAnEponOnuVoiceDataVlan": zxAnEponOnuVoiceDataVlan,
       "zxAnEponOnuVoiceDataPriority": zxAnEponOnuVoiceDataPriority,
       "zxAnEponOnuVoiceDhcpLeaseTime": zxAnEponOnuVoiceDhcpLeaseTime,
       "zxAnEponOnuVoicePPPoEStatus": zxAnEponOnuVoicePPPoEStatus,
       "epon0pticalTransceiverDiagnosisTable": epon0pticalTransceiverDiagnosisTable,
       "epon0pticalTransceiverDiagnosisEntry": epon0pticalTransceiverDiagnosisEntry,
       "zxAnEponOnuTransTemperature": zxAnEponOnuTransTemperature,
       "zxAnEponOnuSupplyVoltage": zxAnEponOnuSupplyVoltage,
       "zxAnEponOnuTxBiasCurrent": zxAnEponOnuTxBiasCurrent,
       "zxAnEponOnuTxPower": zxAnEponOnuTxPower,
       "zxAnEponOnuRxPower": zxAnEponOnuRxPower,
       "eponRmOnuTransAlarmCfgTable": eponRmOnuTransAlarmCfgTable,
       "eponRmOnuTransAlarmCfgTableEntry": eponRmOnuTransAlarmCfgTableEntry,
       "zxAnEponOnuTrans": zxAnEponOnuTrans,
       "eponRmOnuTransAlarmThresholdTable": eponRmOnuTransAlarmThresholdTable,
       "eponRmOnuTransAlarmThresholdEntry": eponRmOnuTransAlarmThresholdEntry,
       "zxAnEponOnuTempHighAlarm": zxAnEponOnuTempHighAlarm,
       "zxAnEponOnuTempLowAlarm": zxAnEponOnuTempLowAlarm,
       "zxAnEponOnuTempHighWarning": zxAnEponOnuTempHighWarning,
       "zxAnEponOnuTempLowwarning": zxAnEponOnuTempLowwarning,
       "zxAnEponOnuVoltageHighAlarm": zxAnEponOnuVoltageHighAlarm,
       "zxAnEponOnuVoltageLowAlarm": zxAnEponOnuVoltageLowAlarm,
       "zxAnEponOnuVoltageHighWarning": zxAnEponOnuVoltageHighWarning,
       "zxAnEponOnuVoltageLowWarning": zxAnEponOnuVoltageLowWarning,
       "zxAnEponOnuBiasHighAlarm": zxAnEponOnuBiasHighAlarm,
       "zxAnEponOnuBiasLowAlarm": zxAnEponOnuBiasLowAlarm,
       "zxAnEponOnuBiasHighWarning": zxAnEponOnuBiasHighWarning,
       "zxAnEponOnuBiasLowWarning": zxAnEponOnuBiasLowWarning,
       "zxAnEponOnuTxPowerHighAlarm": zxAnEponOnuTxPowerHighAlarm,
       "zxAnEponOnuTxPowerLowAlarm": zxAnEponOnuTxPowerLowAlarm,
       "zxAnEponOnuTxPowerHighWarning": zxAnEponOnuTxPowerHighWarning,
       "zxAnEponOnuTxPowerLowWarning": zxAnEponOnuTxPowerLowWarning,
       "zxAnEponOnuRxPowerHighAlarm": zxAnEponOnuRxPowerHighAlarm,
       "zxAnEponOnuRxPowerLowAlarm": zxAnEponOnuRxPowerLowAlarm,
       "zxAnEponOnuRxPowerHighWarning": zxAnEponOnuRxPowerHighWarning,
       "zxAnEponOnuRxPowerLowWarning": zxAnEponOnuRxPowerLowWarning,
       "zxEponUniProfileAdmin": zxEponUniProfileAdmin,
       "zxEponUniProfileTable": zxEponUniProfileTable,
       "zxEponUniProfileEntry": zxEponUniProfileEntry,
       "uniProfileIndex": uniProfileIndex,
       "uniProfileName": uniProfileName,
       "uniProfileUpCir": uniProfileUpCir,
       "uniProfileUpCbs": uniProfileUpCbs,
       "uniProfileUpEbs": uniProfileUpEbs,
       "uniProfileDownCir": uniProfileDownCir,
       "uniProfileDownCbs": uniProfileDownCbs,
       "uniProfileDownEbs": uniProfileDownEbs,
       "uniProfileRowStatus": uniProfileRowStatus,
       "uniProfileNextIndex": uniProfileNextIndex,
       "zxEponUniLimitCfgTable": zxEponUniLimitCfgTable,
       "zxEponUniLimitCfgEntry": zxEponUniLimitCfgEntry,
       "uniCfgLimitProfileIndex": uniCfgLimitProfileIndex,
       "zxAnEponRmVoipProfileMgmt": zxAnEponRmVoipProfileMgmt,
       "zxAnEponRmVoipIpProfileIdxNext": zxAnEponRmVoipIpProfileIdxNext,
       "zxAnEponRmVoipIpProfileTable": zxAnEponRmVoipIpProfileTable,
       "zxAnEponRmVoipIpProfileEntry": zxAnEponRmVoipIpProfileEntry,
       "zxAnEponRmVoipIpProfileIdx": zxAnEponRmVoipIpProfileIdx,
       "zxAnEponRmVoipIpProfileName": zxAnEponRmVoipIpProfileName,
       "zxAnEponRmVoipIpMngIpRelation": zxAnEponRmVoipIpMngIpRelation,
       "zxAnEponRmVoipIpMode": zxAnEponRmVoipIpMode,
       "zxAnEponRmVoipIpDefaultGateWay": zxAnEponRmVoipIpDefaultGateWay,
       "zxAnEponRmVoipIpPrimaryDNSServerIp": zxAnEponRmVoipIpPrimaryDNSServerIp,
       "zxAnEponRmVoipIpPPPoEMode": zxAnEponRmVoipIpPPPoEMode,
       "zxAnEponRmVoipIpRowStatus": zxAnEponRmVoipIpRowStatus,
       "zxAnEponRmVoipVlanProfileIdxNext": zxAnEponRmVoipVlanProfileIdxNext,
       "zxAnEponRmVoipVlanProfileTable": zxAnEponRmVoipVlanProfileTable,
       "zxAnEponRmVoipVlanProfileEntry": zxAnEponRmVoipVlanProfileEntry,
       "zxAnEponRmVoipVlanProfileIdx": zxAnEponRmVoipVlanProfileIdx,
       "zxAnEponRmVoipVlanProfileName": zxAnEponRmVoipVlanProfileName,
       "zxAnEponRmVoipVlanTagMode": zxAnEponRmVoipVlanTagMode,
       "zxAnEponRmVoipVlanTagCVlan": zxAnEponRmVoipVlanTagCVlan,
       "zxAnEponRmVoipVlanTagPriority": zxAnEponRmVoipVlanTagPriority,
       "zxAnEponRmVoipVlanTagSVlan": zxAnEponRmVoipVlanTagSVlan,
       "zxAnEponRmVoipVlanRowStatus": zxAnEponRmVoipVlanRowStatus,
       "zxAnEponRmVoipH248ProfileIdxNext": zxAnEponRmVoipH248ProfileIdxNext,
       "zxAnEponRmVoipH248ProfileTable": zxAnEponRmVoipH248ProfileTable,
       "zxAnEponRmVoipH248ProfileEntry": zxAnEponRmVoipH248ProfileEntry,
       "zxAnEponRmVoipH248ProfileIdx": zxAnEponRmVoipH248ProfileIdx,
       "zxAnEponRmVoipH248ProfileName": zxAnEponRmVoipH248ProfileName,
       "zxAnEponRmVoipH248RegServerIp": zxAnEponRmVoipH248RegServerIp,
       "zxAnEponRmVoipH248RegServerPort": zxAnEponRmVoipH248RegServerPort,
       "zxAnEponRmVoipH248BackRegServerIp": zxAnEponRmVoipH248BackRegServerIp,
       "zxAnEponRmVoipH248BackRegServerPort": zxAnEponRmVoipH248BackRegServerPort,
       "zxAnEponRmVoipH248RtpLinkKeptFlag": zxAnEponRmVoipH248RtpLinkKeptFlag,
       "zxAnEponRmVoipH248OnuHeartbeatMode": zxAnEponRmVoipH248OnuHeartbeatMode,
       "zxAnEponRmVoipH248OnuHeartbeatCycle": zxAnEponRmVoipH248OnuHeartbeatCycle,
       "zxAnEponRmVoipH248OnuHeartbeatCount": zxAnEponRmVoipH248OnuHeartbeatCount,
       "zxAnEponRmVoipH248MgRegMode": zxAnEponRmVoipH248MgRegMode,
       "zxAnEponRmVoipH248MgPort": zxAnEponRmVoipH248MgPort,
       "zxAnEponRmVoipH248RowStatus": zxAnEponRmVoipH248RowStatus,
       "zxAnEponRmVoipMgcpProfileIdxNext": zxAnEponRmVoipMgcpProfileIdxNext,
       "zxAnEponRmVoipMgcpProfileTable": zxAnEponRmVoipMgcpProfileTable,
       "zxAnEponRmVoipMgcpProfileEntry": zxAnEponRmVoipMgcpProfileEntry,
       "zxAnEponRmVoipMgcpProfileIdx": zxAnEponRmVoipMgcpProfileIdx,
       "zxAnEponRmVoipMgcpProfileName": zxAnEponRmVoipMgcpProfileName,
       "zxAnEponRmVoipMgcpRegServerIp": zxAnEponRmVoipMgcpRegServerIp,
       "zxAnEponRmVoipMgcpRegServerPort": zxAnEponRmVoipMgcpRegServerPort,
       "zxAnEponRmVoipMgcpBackRegServerIp": zxAnEponRmVoipMgcpBackRegServerIp,
       "zxAnEponRmVoipMgcpBackRegServerPort": zxAnEponRmVoipMgcpBackRegServerPort,
       "zxAnEponRmVoipMgcpOnuHeartbeatMode": zxAnEponRmVoipMgcpOnuHeartbeatMode,
       "zxAnEponRmVoipMgcpOnuHeartbeatCycle": zxAnEponRmVoipMgcpOnuHeartbeatCycle,
       "zxAnEponRmVoipMgcpOnuHeartbeatCount": zxAnEponRmVoipMgcpOnuHeartbeatCount,
       "zxAnEponRmVoipMgcpMgRegMode": zxAnEponRmVoipMgcpMgRegMode,
       "zxAnEponRmVoipMgcpMgPort": zxAnEponRmVoipMgcpMgPort,
       "zxAnEponRmVoipMgcpRowStatus": zxAnEponRmVoipMgcpRowStatus,
       "zxAnEponRmVoipSipProfileIdxNext": zxAnEponRmVoipSipProfileIdxNext,
       "zxAnEponRmVoipSipProfileTable": zxAnEponRmVoipSipProfileTable,
       "zxAnEponRmVoipSipProfileEntry": zxAnEponRmVoipSipProfileEntry,
       "zxAnEponRmVoipSipProfileIdx": zxAnEponRmVoipSipProfileIdx,
       "zxAnEponRmVoipSipProfileName": zxAnEponRmVoipSipProfileName,
       "zxAnEponRmVoipSipMgPort": zxAnEponRmVoipSipMgPort,
       "zxAnEponRmVoipSipRegServerIp": zxAnEponRmVoipSipRegServerIp,
       "zxAnEponRmVoipSipRegServerPort": zxAnEponRmVoipSipRegServerPort,
       "zxAnEponRmVoipSipBackRegServerIp": zxAnEponRmVoipSipBackRegServerIp,
       "zxAnEponRmVoipSipBackRegServerPort": zxAnEponRmVoipSipBackRegServerPort,
       "zxAnEponRmVoipSipProxyServerIp": zxAnEponRmVoipSipProxyServerIp,
       "zxAnEponRmVoipSipProxyServerPort": zxAnEponRmVoipSipProxyServerPort,
       "zxAnEponRmVoipSipBackProxyServerIp": zxAnEponRmVoipSipBackProxyServerIp,
       "zxAnEponRmVoipSipBackProxyServerPort": zxAnEponRmVoipSipBackProxyServerPort,
       "zxAnEponRmVoipSipOutBoundServerIp": zxAnEponRmVoipSipOutBoundServerIp,
       "zxAnEponRmVoipSipOutBoundServerPort": zxAnEponRmVoipSipOutBoundServerPort,
       "zxAnEponRmVoipSipRegInterval": zxAnEponRmVoipSipRegInterval,
       "zxAnEponRmVoipSipHeartbeatSwitch": zxAnEponRmVoipSipHeartbeatSwitch,
       "zxAnEponRmVoipSipHeartbeatCycle": zxAnEponRmVoipSipHeartbeatCycle,
       "zxAnEponRmVoipSipHeartbeatCount": zxAnEponRmVoipSipHeartbeatCount,
       "zxAnEponRmVoipSipRowStatus": zxAnEponRmVoipSipRowStatus,
       "zxAnEponRmVoipFaxProfileIdxNext": zxAnEponRmVoipFaxProfileIdxNext,
       "zxAnEponRmVoipFaxProfileTable": zxAnEponRmVoipFaxProfileTable,
       "zxAnEponRmVoipFaxProfileEntry": zxAnEponRmVoipFaxProfileEntry,
       "zxAnEponRmVoipFaxProfileIdx": zxAnEponRmVoipFaxProfileIdx,
       "zxAnEponRmVoipFaxProfileName": zxAnEponRmVoipFaxProfileName,
       "zxAnEponRmVoipFaxMode": zxAnEponRmVoipFaxMode,
       "zxAnEponRmVoipFaxControlMode": zxAnEponRmVoipFaxControlMode,
       "zxAnEponRmVoipFaxRowStatus": zxAnEponRmVoipFaxRowStatus,
       "zxAnEponRmVoipMgmt": zxAnEponRmVoipMgmt,
       "zxAnEponRmVoipIpInfoTable": zxAnEponRmVoipIpInfoTable,
       "zxAnEponRmVoipIpInfoEntry": zxAnEponRmVoipIpInfoEntry,
       "zxAnEponOnuCardIndex": zxAnEponOnuCardIndex,
       "zxAnEponRmVoipIpAddress": zxAnEponRmVoipIpAddress,
       "zxAnEponRmVoipIpNetMask": zxAnEponRmVoipIpNetMask,
       "zxAnEponRmVoipPppoeInfoTable": zxAnEponRmVoipPppoeInfoTable,
       "zxAnEponRmVoipPppoeInfoEntry": zxAnEponRmVoipPppoeInfoEntry,
       "zxAnEponRmVoipPppoeUserName": zxAnEponRmVoipPppoeUserName,
       "zxAnEponRmVoipPppoePassword": zxAnEponRmVoipPppoePassword,
       "zxAnEponRmVoipH248MgcpAttrTable": zxAnEponRmVoipH248MgcpAttrTable,
       "zxAnEponRmVoipH248MgcpAttrEntry": zxAnEponRmVoipH248MgcpAttrEntry,
       "zxAnEponRmVoipH248MgcpMID": zxAnEponRmVoipH248MgcpMID,
       "zxAnEponRmVoipH248MgcpActiveMgc": zxAnEponRmVoipH248MgcpActiveMgc,
       "zxAnEponRmVoipH248MgcpUserTidCfgTable": zxAnEponRmVoipH248MgcpUserTidCfgTable,
       "zxAnEponRmVoipH248MgcpUserTidCfgEntry": zxAnEponRmVoipH248MgcpUserTidCfgEntry,
       "zxAnEponRmVoipH248MgcpUserTidGroupIdx": zxAnEponRmVoipH248MgcpUserTidGroupIdx,
       "zxAnEponRmVoipH248MgcpUserTidBeginIdx": zxAnEponRmVoipH248MgcpUserTidBeginIdx,
       "zxAnEponRmVoipH248MgcpUserTidNumber": zxAnEponRmVoipH248MgcpUserTidNumber,
       "zxAnEponRmVoipH248MgcpUserTidPrefix": zxAnEponRmVoipH248MgcpUserTidPrefix,
       "zxAnEponRmVoipH248MgcpUserTidBeginDigit": zxAnEponRmVoipH248MgcpUserTidBeginDigit,
       "zxAnEponRmVoipH248MgcpUserTidDigitAlignMode": zxAnEponRmVoipH248MgcpUserTidDigitAlignMode,
       "zxAnEponRmVoipH248MgcpUserTidDigitLength": zxAnEponRmVoipH248MgcpUserTidDigitLength,
       "zxAnEponRmVoipH248MgcpUserTidRowStatus": zxAnEponRmVoipH248MgcpUserTidRowStatus,
       "zxAnEponRmVoipH248MgcpRtpTidCfgTable": zxAnEponRmVoipH248MgcpRtpTidCfgTable,
       "zxAnEponRmVoipH248MgcpRtpTidCfgEntry": zxAnEponRmVoipH248MgcpRtpTidCfgEntry,
       "zxAnEponRmVoipH248MgcpRtpTidPrefix": zxAnEponRmVoipH248MgcpRtpTidPrefix,
       "zxAnEponRmVoipH248MgcpRtpTidBeginDigit": zxAnEponRmVoipH248MgcpRtpTidBeginDigit,
       "zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode": zxAnEponRmVoipH248MgcpRtpTidDigitAlignMode,
       "zxAnEponRmVoipH248MgcpRtpTidDigitLength": zxAnEponRmVoipH248MgcpRtpTidDigitLength,
       "zxAnEponRmVoipH248MgcpRtpTidNum": zxAnEponRmVoipH248MgcpRtpTidNum,
       "zxAnEponRmVoipSipUserCfgTable": zxAnEponRmVoipSipUserCfgTable,
       "zxAnEponRmVoipSipUserCfgEntry": zxAnEponRmVoipSipUserCfgEntry,
       "zxAnEponRmVoipSipUserAccount": zxAnEponRmVoipSipUserAccount,
       "zxAnEponRmVoipSipUserName": zxAnEponRmVoipSipUserName,
       "zxAnEponRmVoipSipUserPassword": zxAnEponRmVoipSipUserPassword,
       "zxAnEponRmVoipBaseInfoTable": zxAnEponRmVoipBaseInfoTable,
       "zxAnEponRmVoipBaseInfoEntry": zxAnEponRmVoipBaseInfoEntry,
       "zxAnEponRmVoipMacAddress": zxAnEponRmVoipMacAddress,
       "zxAnEponRmVoipProtocolSupported": zxAnEponRmVoipProtocolSupported,
       "zxAnEponRmVoipSoftwareVersion": zxAnEponRmVoipSoftwareVersion,
       "zxAnEponRmVoipSoftwareVersionTime": zxAnEponRmVoipSoftwareVersionTime,
       "zxAnEponRmVoipUserCount": zxAnEponRmVoipUserCount,
       "zxAnEponRmVoipProtocolUsed": zxAnEponRmVoipProtocolUsed,
       "zxAnEponRmVoipH248MgcpUserTidInfoTable": zxAnEponRmVoipH248MgcpUserTidInfoTable,
       "zxAnEponRmVoipH248MgcpUserTidInfoEntry": zxAnEponRmVoipH248MgcpUserTidInfoEntry,
       "zxAnEponRmVoipH248MgcpUserTidName": zxAnEponRmVoipH248MgcpUserTidName,
       "zxAnEponRmVoipH248MgcpRtpTidInfoTable": zxAnEponRmVoipH248MgcpRtpTidInfoTable,
       "zxAnEponRmVoipH248MgcpRtpTidInfoEntry": zxAnEponRmVoipH248MgcpRtpTidInfoEntry,
       "zxAnEponRmVoipH248MgcpRtpTidNumber": zxAnEponRmVoipH248MgcpRtpTidNumber,
       "zxAnEponRmVoipH248MgcpRtpTidFirstName": zxAnEponRmVoipH248MgcpRtpTidFirstName,
       "zxAnEponRmVoipModuleStatusTable": zxAnEponRmVoipModuleStatusTable,
       "zxAnEponRmVoipModuleStatusEntry": zxAnEponRmVoipModuleStatusEntry,
       "zxAnEponRmVoipModuleStatus": zxAnEponRmVoipModuleStatus,
       "zxAnEponRmVoipModuleAction": zxAnEponRmVoipModuleAction,
       "zxAnEponRmVoipUserIfStatusTable": zxAnEponRmVoipUserIfStatusTable,
       "zxAnEponRmVoipUserIfStatusEntry": zxAnEponRmVoipUserIfStatusEntry,
       "zxAnEponRmVoipPortOperStatus": zxAnEponRmVoipPortOperStatus,
       "zxAnEponRmVoipPortServiceType": zxAnEponRmVoipPortServiceType,
       "zxAnEponRmVoipPortServiceState": zxAnEponRmVoipPortServiceState,
       "zxAnEponRmVoipPortCodecMode": zxAnEponRmVoipPortCodecMode,
       "zxAnEponRmVoipPortAction": zxAnEponRmVoipPortAction,
       "zxAnEponRmVoipPortReversalCtrl": zxAnEponRmVoipPortReversalCtrl,
       "zxAnEponRmVoipPortPcmToPktGain": zxAnEponRmVoipPortPcmToPktGain,
       "zxAnEponRmVoipPortPktToPcmGain": zxAnEponRmVoipPortPktToPcmGain,
       "zxAnEponRmVoipProfileApplyTable": zxAnEponRmVoipProfileApplyTable,
       "zxAnEponRmVoipProfileApplyEntry": zxAnEponRmVoipProfileApplyEntry,
       "zxAnEponRmVoipCurrIpProfileIdx": zxAnEponRmVoipCurrIpProfileIdx,
       "zxAnEponRmVoipCurrVlanProfileIdx": zxAnEponRmVoipCurrVlanProfileIdx,
       "zxAnEponRmVoipCurrProtocolProfileType": zxAnEponRmVoipCurrProtocolProfileType,
       "zxAnEponRmVoipCurrProtocolProfileIdx": zxAnEponRmVoipCurrProtocolProfileIdx,
       "zxAnEponRmVoipCurrFaxProfileIdx": zxAnEponRmVoipCurrFaxProfileIdx,
       "zxAnEponRmVoipSipAttrTable": zxAnEponRmVoipSipAttrTable,
       "zxAnEponRmVoipSipAttrEntry": zxAnEponRmVoipSipAttrEntry,
       "zxAnEponRmVoipSipActiveProxyServer": zxAnEponRmVoipSipActiveProxyServer,
       "zxAnEponRmVoipSipDigitMapTable": zxAnEponRmVoipSipDigitMapTable,
       "zxAnEponRmVoipSipDigitMapEntry": zxAnEponRmVoipSipDigitMapEntry,
       "zxEponRmVoipSipDigitMap": zxEponRmVoipSipDigitMap,
       "zxAnEponOnuVoipPresentingTable": zxAnEponOnuVoipPresentingTable,
       "zxAnEponOnuVoipPresentingEntry": zxAnEponOnuVoipPresentingEntry,
       "zxAnEponOnuVoipPresentingCallNbrState": zxAnEponOnuVoipPresentingCallNbrState,
       "zxAnEponOnuVoipPresentingCallNbrType": zxAnEponOnuVoipPresentingCallNbrType,
       "zxAnEponOnuVoipTimerConfigTable": zxAnEponOnuVoipTimerConfigTable,
       "zxAnEponOnuVoipTimerConfigEntry": zxAnEponOnuVoipTimerConfigEntry,
       "zxAnEponOnuVoipTimerConfigDml": zxAnEponOnuVoipTimerConfigDml,
       "zxAnEponOnuVoipTimerConfigDms": zxAnEponOnuVoipTimerConfigDms,
       "zxAnEponOnuVoipStatsTable": zxAnEponOnuVoipStatsTable,
       "zxAnEponOnuVoipStatsEntry": zxAnEponOnuVoipStatsEntry,
       "zxAnEponOnuVoipRxPkts": zxAnEponOnuVoipRxPkts,
       "zxAnEponOnuVoipTxPkts": zxAnEponOnuVoipTxPkts,
       "zxAnEponOnuVoipAverageDelay": zxAnEponOnuVoipAverageDelay,
       "zxAnEponOnuVoipAverageJitter": zxAnEponOnuVoipAverageJitter,
       "zxAnEponOnuVoipLoss": zxAnEponOnuVoipLoss,
       "zxAnEponRmUniVoipRxMediaDataRate": zxAnEponRmUniVoipRxMediaDataRate,
       "zxAnEponRmUniVoipTxMediaDataRate": zxAnEponRmUniVoipTxMediaDataRate,
       "zxAnEponRmUniVoipCurCallDuration": zxAnEponRmUniVoipCurCallDuration,
       "zxAnEponRmUniVoipTotCallDuration": zxAnEponRmUniVoipTotCallDuration,
       "zxAnEponRmUniVoipCallTimes": zxAnEponRmUniVoipCallTimes,
       "zxAnEponOnuVoipOtherConfigTable": zxAnEponOnuVoipOtherConfigTable,
       "zxAnEponOnuVoipOtherConfigEntry": zxAnEponOnuVoipOtherConfigEntry,
       "zxAnEponOnuVoipComfortableNoise": zxAnEponOnuVoipComfortableNoise,
       "zxAnEponOnuVoipSilenceDetection": zxAnEponOnuVoipSilenceDetection,
       "zxAnEponOnuVoipEchoCanceller": zxAnEponOnuVoipEchoCanceller,
       "zxAnEponOnuVoipDtmpTransferMode": zxAnEponOnuVoipDtmpTransferMode,
       "zxAnEponRmOnuVoipSrvPerfTable": zxAnEponRmOnuVoipSrvPerfTable,
       "zxAnEponRmOnuVoipSrvPerfEntry": zxAnEponRmOnuVoipSrvPerfEntry,
       "zxAnEponRmOnuVoipRxSignalMsg": zxAnEponRmOnuVoipRxSignalMsg,
       "zxAnEponRmOnuVoipTxSignalMsg": zxAnEponRmOnuVoipTxSignalMsg,
       "zxAnEponRmOnuVoipLossSignalMsg": zxAnEponRmOnuVoipLossSignalMsg,
       "zxAnEponRmOnuVoipReTxSignalMsg": zxAnEponRmOnuVoipReTxSignalMsg,
       "zxAnEponRmOnuVoipErrSignalMsg": zxAnEponRmOnuVoipErrSignalMsg,
       "zxAnEponRmOnuVoipUnknowSignalMsg": zxAnEponRmOnuVoipUnknowSignalMsg,
       "zxAnEponOnuCapabilityExtTable": zxAnEponOnuCapabilityExtTable,
       "zxAnEponOnuCapabilityExtEntry": zxAnEponOnuCapabilityExtEntry,
       "zxAnEponOnuType": zxAnEponOnuType,
       "zxAnEponOnuMultiLlid": zxAnEponOnuMultiLlid,
       "zxAnEponOnuProtection": zxAnEponOnuProtection,
       "zxAnEponOnuPonPorts": zxAnEponOnuPonPorts,
       "zxAnEponOnuSlots": zxAnEponOnuSlots,
       "zxAnEponOnuBatteryBackupStatus": zxAnEponOnuBatteryBackupStatus,
       "zxAnEponOnuIsSupportIpv6": zxAnEponOnuIsSupportIpv6,
       "zxAnEponOnuPwrSdSupportMode": zxAnEponOnuPwrSdSupportMode,
       "zxAnEponOnuSlaNumber": zxAnEponOnuSlaNumber,
       "zxAnEponOnuInterfaceTable": zxAnEponOnuInterfaceTable,
       "zxAnEponOnuInterfaceEntry": zxAnEponOnuInterfaceEntry,
       "zxAnEponOnuInterfaceType": zxAnEponOnuInterfaceType,
       "zxAnEponOnuInterfaceNum": zxAnEponOnuInterfaceNum,
       "zxAnEponMduCardTable": zxAnEponMduCardTable,
       "zxAnEponMduCardEntry": zxAnEponMduCardEntry,
       "zxAnEponMduCardOperStatus": zxAnEponMduCardOperStatus,
       "zxAnEponMduCardAdminStatus": zxAnEponMduCardAdminStatus,
       "zxAnEponMduSnmpParamMgmt": zxAnEponMduSnmpParamMgmt,
       "zxAnEponMduSnmpParamTable": zxAnEponMduSnmpParamTable,
       "zxAnEponMduSnmpParamEntry": zxAnEponMduSnmpParamEntry,
       "zxEponMduSnmpVersion": zxEponMduSnmpVersion,
       "zxEponMduSnmpServicePort": zxEponMduSnmpServicePort,
       "zxEponMduSnmpTrapPort": zxEponMduSnmpTrapPort,
       "zxEponMduSnmpReadCommunity": zxEponMduSnmpReadCommunity,
       "zxEponMduSnmpWriteCommunity": zxEponMduSnmpWriteCommunity,
       "zxEponMduSnmpTrapHostTable": zxEponMduSnmpTrapHostTable,
       "zxEponMduSnmpTrapHostEntry": zxEponMduSnmpTrapHostEntry,
       "zxEponMduSnmpTrapHostIndex": zxEponMduSnmpTrapHostIndex,
       "zxEponMduSnmpTrapHostIpAddr": zxEponMduSnmpTrapHostIpAddr,
       "zxEponMduSnmpTrapHostSnmpVer": zxEponMduSnmpTrapHostSnmpVer,
       "zxEponMduSnmpTrapHostCommunity": zxEponMduSnmpTrapHostCommunity,
       "zxEponMduSnmpTrapHostMinEventLevel": zxEponMduSnmpTrapHostMinEventLevel,
       "zxEponMduSnmpTrapHostEnable": zxEponMduSnmpTrapHostEnable,
       "zxEponMduSnmpTrapHostRowStatus": zxEponMduSnmpTrapHostRowStatus,
       "zxAnEponOnuMVlanSwitchTable": zxAnEponOnuMVlanSwitchTable,
       "zxAnEponOnuMVlanSwitchEntry": zxAnEponOnuMVlanSwitchEntry,
       "zxAnEponOnuMVlan": zxAnEponOnuMVlan,
       "zxAnEponOnuIptvUserVlan": zxAnEponOnuIptvUserVlan,
       "zxAnEponOnuMVlanSwitchRowStatus": zxAnEponOnuMVlanSwitchRowStatus,
       "zxAnEponOnuPortTable": zxAnEponOnuPortTable,
       "zxAnEponOnuPortEntry": zxAnEponOnuPortEntry,
       "zxAnEponOnuPortLoopbackDetectStatus": zxAnEponOnuPortLoopbackDetectStatus,
       "zxAnEponOnuPortLoopbackAutoSdEn": zxAnEponOnuPortLoopbackAutoSdEn,
       "zxAnEponOnuLlidQueueTable": zxAnEponOnuLlidQueueTable,
       "zxAnEponOnuLlidQueueEntry": zxAnEponOnuLlidQueueEntry,
       "zxAnEponOnuLlid": zxAnEponOnuLlid,
       "zxAnEponOnuLlidQueue1WrrWeight": zxAnEponOnuLlidQueue1WrrWeight,
       "zxAnEponOnuLlidQueue2WrrWeight": zxAnEponOnuLlidQueue2WrrWeight,
       "zxAnEponOnuLlidQueue3WrrWeight": zxAnEponOnuLlidQueue3WrrWeight,
       "zxAnEponOnuLlidQueue4WrrWeight": zxAnEponOnuLlidQueue4WrrWeight,
       "zxAnEponOnuLlidQueue5WrrWeight": zxAnEponOnuLlidQueue5WrrWeight,
       "zxAnEponOnuLlidQueue6WrrWeight": zxAnEponOnuLlidQueue6WrrWeight,
       "zxAnEponOnuLlidQueue7WrrWeight": zxAnEponOnuLlidQueue7WrrWeight,
       "zxAnEponOnuLlidQueue8WrrWeight": zxAnEponOnuLlidQueue8WrrWeight,
       "zxAnEponOnuPonIfTable": zxAnEponOnuPonIfTable,
       "zxAnEponOnuPonIfEntry": zxAnEponOnuPonIfEntry,
       "zxAnEponOnuActivePonIf": zxAnEponOnuActivePonIf,
       "zxAnEponOnuSlaMgmt": zxAnEponOnuSlaMgmt,
       "zxAnEponOnuSlaProfileIdxNext": zxAnEponOnuSlaProfileIdxNext,
       "zxAnEponOnuSlaProfileTable": zxAnEponOnuSlaProfileTable,
       "zxAnEponOnuSlaProfileEntry": zxAnEponOnuSlaProfileEntry,
       "zxAnEponOnuSlaProfileIndex": zxAnEponOnuSlaProfileIndex,
       "zxAnEponOnuSlaProfileName": zxAnEponOnuSlaProfileName,
       "zxAnEponOnuServiceDbaEnable": zxAnEponOnuServiceDbaEnable,
       "zxAnEponOnuBestEffortSchedulingScheme": zxAnEponOnuBestEffortSchedulingScheme,
       "zxAnEponOnuHighPriorityBoundary": zxAnEponOnuHighPriorityBoundary,
       "zxAnEponOnuServiceDbaCycleLength": zxAnEponOnuServiceDbaCycleLength,
       "zxAnEponOnuSlaServiceIdxNext": zxAnEponOnuSlaServiceIdxNext,
       "zxAnEponOnuSlaProfileRowStatus": zxAnEponOnuSlaProfileRowStatus,
       "zxAnEponOnuServiceQueueTable": zxAnEponOnuServiceQueueTable,
       "zxAnEponOnuServiceQueueEntry": zxAnEponOnuServiceQueueEntry,
       "zxAnEponOnuSlaServiceIdx": zxAnEponOnuSlaServiceIdx,
       "zxAnEponOnuServiceName": zxAnEponOnuServiceName,
       "zxAnEponOnuQueueId": zxAnEponOnuQueueId,
       "zxAnEponOnuServiceFixedPktSize": zxAnEponOnuServiceFixedPktSize,
       "zxAnEponOnuServiceFixedBandwidth": zxAnEponOnuServiceFixedBandwidth,
       "zxAnEponOnuServiceAssuredBandwidth": zxAnEponOnuServiceAssuredBandwidth,
       "zxAnEponOnuServiceBestEffortBandwidth": zxAnEponOnuServiceBestEffortBandwidth,
       "zxAnEponOnuServiceWrrWeight": zxAnEponOnuServiceWrrWeight,
       "zxAnEponOnuServiceRowStatus": zxAnEponOnuServiceRowStatus,
       "zxAnEponOnuSlaProfileApplyTable": zxAnEponOnuSlaProfileApplyTable,
       "zxAnEponOnuSlaProfileApplyEntry": zxAnEponOnuSlaProfileApplyEntry,
       "zxAnEponOnuCurrSlaProfileIdx": zxAnEponOnuCurrSlaProfileIdx,
       "zxAnEponOnuHoldoverTable": zxAnEponOnuHoldoverTable,
       "zxAnEponOnuHoldoverEntry": zxAnEponOnuHoldoverEntry,
       "zxAnEponOnuHoldoverState": zxAnEponOnuHoldoverState,
       "zxAnEponOnuHoldoverTime": zxAnEponOnuHoldoverTime,
       "zxAnEponOnuAlarmMgmt": zxAnEponOnuAlarmMgmt,
       "zxAnEponOnuLvlAlarmCtrlTable": zxAnEponOnuLvlAlarmCtrlTable,
       "zxAnEponOnuLvlAlarmCtrlEntry": zxAnEponOnuLvlAlarmCtrlEntry,
       "zxAnEponOnuLvlAlarmCode": zxAnEponOnuLvlAlarmCode,
       "zxAnEponOnuLvlAlarmEnable": zxAnEponOnuLvlAlarmEnable,
       "zxAnEponOnuLvlAlarmThreshold": zxAnEponOnuLvlAlarmThreshold,
       "zxAnEponOnuLvlAlarmRestoreThreshold": zxAnEponOnuLvlAlarmRestoreThreshold,
       "zxAnEponOnuPonAlarmCtrlTable": zxAnEponOnuPonAlarmCtrlTable,
       "zxAnEponOnuPonAlarmCtrlEntry": zxAnEponOnuPonAlarmCtrlEntry,
       "zxAnEponOnuPonAlarmCode": zxAnEponOnuPonAlarmCode,
       "zxAnEponOnuPonAlarmEnable": zxAnEponOnuPonAlarmEnable,
       "zxAnEponOnuPonAlarmThreshold": zxAnEponOnuPonAlarmThreshold,
       "zxAnEponOnuPonAlarmRestoreThreshold": zxAnEponOnuPonAlarmRestoreThreshold,
       "zxAnEponOnuUniAlarmCtrlTable": zxAnEponOnuUniAlarmCtrlTable,
       "zxAnEponOnuUniAlarmCtrlEntry": zxAnEponOnuUniAlarmCtrlEntry,
       "zxAnEponOnuUniAlarmCode": zxAnEponOnuUniAlarmCode,
       "zxAnEponOnuUniAlarmEnable": zxAnEponOnuUniAlarmEnable,
       "zxAnEponOnuUniAlarmThreshold": zxAnEponOnuUniAlarmThreshold,
       "zxAnEponOnuUniAlarmRestoreThresh": zxAnEponOnuUniAlarmRestoreThresh,
       "zxAnEponOnuVersionMgmt": zxAnEponOnuVersionMgmt,
       "zxAnEponOnuVersionTable": zxAnEponOnuVersionTable,
       "zxAnEponOnuVersionEntry": zxAnEponOnuVersionEntry,
       "zxAnEponOnuVersionId": zxAnEponOnuVersionId,
       "zxAnEponOnuVersionFileName": zxAnEponOnuVersionFileName,
       "zxAnEponOnuVersionType": zxAnEponOnuVersionType,
       "zxAnEponOnuVersionTag": zxAnEponOnuVersionTag,
       "zxAnEponOnuVersionBuildTime": zxAnEponOnuVersionBuildTime,
       "zxAnEponOnuVersionUpdateTable": zxAnEponOnuVersionUpdateTable,
       "zxAnEponOnuVersionUpdateEntry": zxAnEponOnuVersionUpdateEntry,
       "zxAnEponOnuVersionUpdateOnuType": zxAnEponOnuVersionUpdateOnuType,
       "zxAnEponOnuVersionUpdateLocType": zxAnEponOnuVersionUpdateLocType,
       "zxAnEponOnuVersionUpdateSlotId": zxAnEponOnuVersionUpdateSlotId,
       "zxAnEponOnuVersionUpdateOltId": zxAnEponOnuVersionUpdateOltId,
       "zxAnEponOnuVersionUpdateOnuList": zxAnEponOnuVersionUpdateOnuList,
       "zxAnEponOnuVersionUpdateAction": zxAnEponOnuVersionUpdateAction,
       "zxAnEponOnuVersionUpdateStatusTable": zxAnEponOnuVersionUpdateStatusTable,
       "zxAnEponOnuVersionUpdateStatusEntry": zxAnEponOnuVersionUpdateStatusEntry,
       "zxAnEponOnuVersionUpdateState": zxAnEponOnuVersionUpdateState,
       "zxAnEponOnuVersionUpdateAbortReason": zxAnEponOnuVersionUpdateAbortReason,
       "zxAnEponOnuVersionUpdateErrCode": zxAnEponOnuVersionUpdateErrCode,
       "zxAnEponOnuVersionUpdateErrMsg": zxAnEponOnuVersionUpdateErrMsg,
       "zxAnEponOnuVersionUpdateProgress": zxAnEponOnuVersionUpdateProgress,
       "zxAnEponOnuCurrentUsedVersionName": zxAnEponOnuCurrentUsedVersionName,
       "zxAnEponOnuCurrentUsedVersionTime": zxAnEponOnuCurrentUsedVersionTime,
       "zxAnEponOnuUpdatingVersionName": zxAnEponOnuUpdatingVersionName,
       "zxAnEponOnuUpdatingVersionTime": zxAnEponOnuUpdatingVersionTime,
       "zxAnEponOnuVersionActionTable": zxAnEponOnuVersionActionTable,
       "zxAnEponOnuVersionActionEntry": zxAnEponOnuVersionActionEntry,
       "zxAnEponOnuVersionImageIndex": zxAnEponOnuVersionImageIndex,
       "zxAnEponOnuVersionImageAction": zxAnEponOnuVersionImageAction,
       "zxAnEponOnuVersionImageCommitState": zxAnEponOnuVersionImageCommitState,
       "zxAnEponOnuVersionImageActiveState": zxAnEponOnuVersionImageActiveState,
       "zxAnEponOnuVersionImageValidState": zxAnEponOnuVersionImageValidState,
       "zxAnEponOnuPonMacShapingMgmt": zxAnEponOnuPonMacShapingMgmt,
       "zxAnEponOnuPonMacShapingTable": zxAnEponOnuPonMacShapingTable,
       "zxAnEponOnuPonMacShapingEntry": zxAnEponOnuPonMacShapingEntry,
       "zxAnEponOnuShappingAdminStatus": zxAnEponOnuShappingAdminStatus,
       "zxAnEponOnuShappingCir": zxAnEponOnuShappingCir,
       "zxAnEponOnuShappingCbs": zxAnEponOnuShappingCbs,
       "zxAnEponOnuPonMacBufferTable": zxAnEponOnuPonMacBufferTable,
       "zxAnEponOnuPonMacBufferEntry": zxAnEponOnuPonMacBufferEntry,
       "zxAnEponOnuPonMacDsBufferAdminStatus": zxAnEponOnuPonMacDsBufferAdminStatus,
       "zxAnEponOnuPonMacDsBufferOperStatus": zxAnEponOnuPonMacDsBufferOperStatus,
       "zxAnEponOnuPonMacDsConfBufferSize": zxAnEponOnuPonMacDsConfBufferSize,
       "zxAnEponOnuPonMacDsActBufferSize": zxAnEponOnuPonMacDsActBufferSize,
       "zxAnEponOnuPonMacUsBufferAdminStatus": zxAnEponOnuPonMacUsBufferAdminStatus,
       "zxAnEponOnuPonMacUsBufferOperStatus": zxAnEponOnuPonMacUsBufferOperStatus,
       "zxAnEponOnuPonMacUsConfBufferSize": zxAnEponOnuPonMacUsConfBufferSize,
       "zxAnEponOnuPonMacUsActBufferSize": zxAnEponOnuPonMacUsActBufferSize,
       "zxAnEponOnuPonMacBufferCapabilityTable": zxAnEponOnuPonMacBufferCapabilityTable,
       "zxAnEponOnuPonMacBufferCapabilityEntry": zxAnEponOnuPonMacBufferCapabilityEntry,
       "zxAnEponOnuPonMacBufferCapability": zxAnEponOnuPonMacBufferCapability,
       "zxAnEponOnuPonMacMinDsBufferSize": zxAnEponOnuPonMacMinDsBufferSize,
       "zxAnEponOnuPonMacMaxDsBufferSize": zxAnEponOnuPonMacMaxDsBufferSize,
       "zxAnEponOnuPonMacMinUsBufferSize": zxAnEponOnuPonMacMinUsBufferSize,
       "zxAnEponOnuPonMacMaxUsBufferSize": zxAnEponOnuPonMacMaxUsBufferSize,
       "zxAnEponOnuUniMacTable": zxAnEponOnuUniMacTable,
       "zxAnEponOnuUniMacEntry": zxAnEponOnuUniMacEntry,
       "zxAnEponOnuUniVlanId": zxAnEponOnuUniVlanId,
       "zxAnEponOnuUniMacSequenceNo": zxAnEponOnuUniMacSequenceNo,
       "zxAnEponOnuUniMacType": zxAnEponOnuUniMacType,
       "zxAnEponOnuUniMacAddress": zxAnEponOnuUniMacAddress,
       "zxAnEponOnuMgmtIpDHCPCfgTable": zxAnEponOnuMgmtIpDHCPCfgTable,
       "zxAnEponOnuMgmtIpDHCPCfgEntry": zxAnEponOnuMgmtIpDHCPCfgEntry,
       "zxAnEponOnuMgmtIpDHCPCfgVlan": zxAnEponOnuMgmtIpDHCPCfgVlan,
       "zxAnEponOnuMgmtIpDHCPCfgPriority": zxAnEponOnuMgmtIpDHCPCfgPriority,
       "zxAnEponOnuMgmtIpDHCPCfgEnableState": zxAnEponOnuMgmtIpDHCPCfgEnableState,
       "zxAnEponOnuMgmtIpDHCPCfgState": zxAnEponOnuMgmtIpDHCPCfgState,
       "zxAnEponRmOnuWanMgmt": zxAnEponRmOnuWanMgmt,
       "zxAnEponRmWanPrfTable": zxAnEponRmWanPrfTable,
       "zxAnEponRmWanPrfEntry": zxAnEponRmWanPrfEntry,
       "zxAnEponRmWanPrfName": zxAnEponRmWanPrfName,
       "zxAnEponRmWanPrfWorkMode": zxAnEponRmWanPrfWorkMode,
       "zxAnEponRmWanPrfSrvType": zxAnEponRmWanPrfSrvType,
       "zxAnEponRmWanPrfIpStackMode": zxAnEponRmWanPrfIpStackMode,
       "zxAnEponRmWanPrfNatNum": zxAnEponRmWanPrfNatNum,
       "zxAnEponRmWanPrfTransTagMode": zxAnEponRmWanPrfTransTagMode,
       "zxAnEponRmWanPrfTagTpid": zxAnEponRmWanPrfTagTpid,
       "zxAnEponRmWanPrfTagVid": zxAnEponRmWanPrfTagVid,
       "zxAnEponRmWanPrfTagPrior": zxAnEponRmWanPrfTagPrior,
       "zxAnEponRmWanPrfMaxTransUnit": zxAnEponRmWanPrfMaxTransUnit,
       "zxAnEponRmWanPrfMVid": zxAnEponRmWanPrfMVid,
       "zxAnEponRmWanPrfBindLanPortList": zxAnEponRmWanPrfBindLanPortList,
       "zxAnEponRmWanPrfBindSsidList": zxAnEponRmWanPrfBindSsidList,
       "zxAnEponRmWanPrfRowStatus": zxAnEponRmWanPrfRowStatus,
       "zxAnEponRmOnuWanConfTable": zxAnEponRmOnuWanConfTable,
       "zxAnEponRmOnuWanConfEntry": zxAnEponRmOnuWanConfEntry,
       "zxAnEponRmOnuWanPortId": zxAnEponRmOnuWanPortId,
       "zxAnEponRmOnuWanPrfName": zxAnEponRmOnuWanPrfName,
       "zxAnEponRmOnuWanIpAllocationMode": zxAnEponRmOnuWanIpAllocationMode,
       "zxAnEponRmOnuWanIpAddr": zxAnEponRmOnuWanIpAddr,
       "zxAnEponRmOnuWanIpMask": zxAnEponRmOnuWanIpMask,
       "zxAnEponRmOnuWanIpGateway": zxAnEponRmOnuWanIpGateway,
       "zxAnEponRmOnuWanPriDnsSvrIp": zxAnEponRmOnuWanPriDnsSvrIp,
       "zxAnEponRmOnuWanSecDnsSvrIp": zxAnEponRmOnuWanSecDnsSvrIp,
       "zxAnEponRmOnuWanPppoeAuthMode": zxAnEponRmOnuWanPppoeAuthMode,
       "zxAnEponRmOnuWanPppoeUserName": zxAnEponRmOnuWanPppoeUserName,
       "zxAnEponRmOnuWanPppoePassword": zxAnEponRmOnuWanPppoePassword,
       "zxAnEponRmOnuWanPppoePrxyNum": zxAnEponRmOnuWanPppoePrxyNum,
       "zxAnEponRmOnuWanPppoePrxyUserNum": zxAnEponRmOnuWanPppoePrxyUserNum,
       "zxAnEponRmOnuWanPortUpTime": zxAnEponRmOnuWanPortUpTime,
       "zxAnEponRmOnuWanConfRowStatus": zxAnEponRmOnuWanConfRowStatus,
       "zxAnEponRmOnuWanGlobalConfTable": zxAnEponRmOnuWanGlobalConfTable,
       "zxAnEponRmOnuWanGlobalConfEntry": zxAnEponRmOnuWanGlobalConfEntry,
       "zxAnEponRmOnuWanGlbMaxUserNum": zxAnEponRmOnuWanGlbMaxUserNum,
       "zxAnEponOnuPowerSavingMgmt": zxAnEponOnuPowerSavingMgmt,
       "zxAnEponOnuPowerSavingTable": zxAnEponOnuPowerSavingTable,
       "zxAnEponOnuPowerSavingEntry": zxAnEponOnuPowerSavingEntry,
       "zxAnEponOnuPwrSaveEnable": zxAnEponOnuPwrSaveEnable,
       "zxAnEponOnuPwrSaveSleepMode": zxAnEponOnuPwrSaveSleepMode,
       "zxAnEponOnuPwrSaveSleepConfMode": zxAnEponOnuPwrSaveSleepConfMode,
       "zxAnEponOnuPwrSaveEarlyWakeUp": zxAnEponOnuPwrSaveEarlyWakeUp,
       "zxAnEponOnuPwrSaveEarlyWakeUpEn": zxAnEponOnuPwrSaveEarlyWakeUpEn,
       "zxAnEponOnuPwrSaveSleepDuration": zxAnEponOnuPwrSaveSleepDuration,
       "zxAnEponOnuPwrSaveWakeUpDuration": zxAnEponOnuPwrSaveWakeUpDuration,
       "zxAnEponOnuPwrSaveMaxRefreshTime": zxAnEponOnuPwrSaveMaxRefreshTime,
       "zxAnEponOnuProtectMgmt": zxAnEponOnuProtectMgmt,
       "zxAnOnuProtectConfTable": zxAnOnuProtectConfTable,
       "zxAnOnuProtectConfEntry": zxAnOnuProtectConfEntry,
       "zxAnOnuProtectLosTimeByOptSignal": zxAnOnuProtectLosTimeByOptSignal,
       "zxAnOnuProtectLosTimeByMpcp": zxAnOnuProtectLosTimeByMpcp,
       "zxAnEponOnuExtendedActionMgmt": zxAnEponOnuExtendedActionMgmt,
       "zxAnEponOnuActionTable": zxAnEponOnuActionTable,
       "zxAnEponOnuActionEntry": zxAnEponOnuActionEntry,
       "zxAnEponOnuAction": zxAnEponOnuAction,
       "zxAnEponOnuSaveActionTable": zxAnEponOnuSaveActionTable,
       "zxAnEponOnuSaveActionEntry": zxAnEponOnuSaveActionEntry,
       "zxAnEponOnuSaveAction": zxAnEponOnuSaveAction,
       "zxAnEponOnuSetHGMACCodeTable": zxAnEponOnuSetHGMACCodeTable,
       "zxAnEponOnuSetHGMACCodeEntry": zxAnEponOnuSetHGMACCodeEntry,
       "zxAnEponOnuHGMACCode": zxAnEponOnuHGMACCode,
       "zxAnEponOnuHGMACVlanTable": zxAnEponOnuHGMACVlanTable,
       "zxAnEponOnuHGMACVlanEntry": zxAnEponOnuHGMACVlanEntry,
       "zxAnEponOnuHGVlan": zxAnEponOnuHGVlan,
       "zxAnEponOnuHGStateTable": zxAnEponOnuHGStateTable,
       "zxAnEponOnuHGStateEntry": zxAnEponOnuHGStateEntry,
       "zxAnEponOnuHGMAC": zxAnEponOnuHGMAC,
       "zxEponOnuHGState": zxEponOnuHGState,
       "zxAnEponOnuStdAttrMgmt": zxAnEponOnuStdAttrMgmt,
       "zxAnEponOnuPhyMgmtTable": zxAnEponOnuPhyMgmtTable,
       "zxAnEponOnuPhyMgmtEntry": zxAnEponOnuPhyMgmtEntry,
       "zxAnEponOnuPhyAdminState": zxAnEponOnuPhyAdminState,
       "zxAnEponOnuAutoNegAttrTable": zxAnEponOnuAutoNegAttrTable,
       "zxAnEponOnuAutoNegAttrEntry": zxAnEponOnuAutoNegAttrEntry,
       "zxAnEponOnuAutoNegAdminState": zxAnEponOnuAutoNegAdminState,
       "zxAnEponOnuAutoNegCapability": zxAnEponOnuAutoNegCapability,
       "zxAnEponOnuAutoNegCapAdvertised": zxAnEponOnuAutoNegCapAdvertised,
       "zxAnEponOnuEthIfConfDuplexSpeed": zxAnEponOnuEthIfConfDuplexSpeed,
       "zxAnEponOnuEthIfActualDuplex": zxAnEponOnuEthIfActualDuplex,
       "zxAnEponOnuEthIfActualSpeed": zxAnEponOnuEthIfActualSpeed,
       "zxAnEponOnuFecMgmtTable": zxAnEponOnuFecMgmtTable,
       "zxAnEponOnuFecMgmtEntry": zxAnEponOnuFecMgmtEntry,
       "zxAnEponOnuFecAbility": zxAnEponOnuFecAbility,
       "zxAnEponOnuFecMode": zxAnEponOnuFecMode,
       "zxAnEponOnuStdActionMgmt": zxAnEponOnuStdActionMgmt,
       "zxAnEponOnuAutoNegActionTable": zxAnEponOnuAutoNegActionTable,
       "zxAnEponOnuAutoNegActionEntry": zxAnEponOnuAutoNegActionEntry,
       "zxAnEponOnuAutoNegAction": zxAnEponOnuAutoNegAction,
       "zxAnEponOnuDbaAttrMgmt": zxAnEponOnuDbaAttrMgmt,
       "zxAnEponOnuDbaQueueThresholdsTable": zxAnEponOnuDbaQueueThresholdsTable,
       "zxAnEponOnuDbaQueueThresholdsEntry": zxAnEponOnuDbaQueueThresholdsEntry,
       "zxAnEponOnuDbaQueueSetIndex": zxAnEponOnuDbaQueueSetIndex,
       "zxAnEponOnuDbaQueueThresholds1": zxAnEponOnuDbaQueueThresholds1,
       "zxAnEponOnuDbaQueueThresholds2": zxAnEponOnuDbaQueueThresholds2,
       "zxAnEponOnuDbaQueueThresholds3": zxAnEponOnuDbaQueueThresholds3,
       "zxAnEponOnuDbaQueueThresholds4": zxAnEponOnuDbaQueueThresholds4,
       "zxAnEponOnuDbaQueueThresholds5": zxAnEponOnuDbaQueueThresholds5,
       "zxAnEponOnuDbaQueueThresholds6": zxAnEponOnuDbaQueueThresholds6,
       "zxAnEponOnuDbaQueueThresholds7": zxAnEponOnuDbaQueueThresholds7,
       "zxAnEponOnuDbaQueueThresholds8": zxAnEponOnuDbaQueueThresholds8,
       "zxAnEponOnuDbaQueueSetActiveTable": zxAnEponOnuDbaQueueSetActiveTable,
       "zxAnEponOnuDbaQueueSetActiveEntry": zxAnEponOnuDbaQueueSetActiveEntry,
       "zxAnEponOnuDbaQueueSetList": zxAnEponOnuDbaQueueSetList,
       "zxAnEponOnuProfileMgmt": zxAnEponOnuProfileMgmt,
       "zxAnEponOnuProfileIndexNextTable": zxAnEponOnuProfileIndexNextTable,
       "zxAnEponOnuProfileIndexNextEntry": zxAnEponOnuProfileIndexNextEntry,
       "zxAnEponOnuClassMarkingConditionIdNext": zxAnEponOnuClassMarkingConditionIdNext,
       "zxAnEponOnuClassMarkingRuleIdNext": zxAnEponOnuClassMarkingRuleIdNext,
       "zxAnEponOnuPfmncStatis": zxAnEponOnuPfmncStatis,
       "zxAnEponOnuPfmncStatisTable": zxAnEponOnuPfmncStatisTable,
       "zxAnEponOnuPfmncStatisEntry": zxAnEponOnuPfmncStatisEntry,
       "portType": portType,
       "parameter1": parameter1,
       "parameter2": parameter2,
       "parameter3": parameter3,
       "parameter4": parameter4,
       "parameter5": parameter5,
       "parameter6": parameter6,
       "parameter7": parameter7,
       "parameter8": parameter8,
       "parameter9": parameter9,
       "parameter10": parameter10,
       "parameter11": parameter11,
       "parameter12": parameter12,
       "parameter13": parameter13,
       "zxAnEponRmPerfConfTable": zxAnEponRmPerfConfTable,
       "zxAnEponRmPerfConfEntry": zxAnEponRmPerfConfEntry,
       "zxAnEponRmPerfOnuPortType": zxAnEponRmPerfOnuPortType,
       "zxAnEponRmPerfOnuHisStatInterval": zxAnEponRmPerfOnuHisStatInterval,
       "zxAnEponRmPerfConfRowStatus": zxAnEponRmPerfConfRowStatus,
       "zxAnEponRmEthCurPerfTable": zxAnEponRmEthCurPerfTable,
       "zxAnEponRmEthCurPerfEntry": zxAnEponRmEthCurPerfEntry,
       "zxAnEponRmCurDsDropEvents": zxAnEponRmCurDsDropEvents,
       "zxAnEponRmCurDsOctets": zxAnEponRmCurDsOctets,
       "zxAnEponRmCurDsPkts": zxAnEponRmCurDsPkts,
       "zxAnEponRmCurDsBcastPkts": zxAnEponRmCurDsBcastPkts,
       "zxAnEponRmCurDsMcastPkts": zxAnEponRmCurDsMcastPkts,
       "zxAnEponRmCurDsCrcErrPkts": zxAnEponRmCurDsCrcErrPkts,
       "zxAnEponRmCurDsUndersizePkts": zxAnEponRmCurDsUndersizePkts,
       "zxAnEponRmCurDsOversizePkts": zxAnEponRmCurDsOversizePkts,
       "zxAnEponRmCurDsFragments": zxAnEponRmCurDsFragments,
       "zxAnEponRmCurDsJabbers": zxAnEponRmCurDsJabbers,
       "zxAnEponRmCurDsPkts64Octets": zxAnEponRmCurDsPkts64Octets,
       "zxAnEponRmCurDs65To127Octets": zxAnEponRmCurDs65To127Octets,
       "zxAnEponRmCurDs128To255Octets": zxAnEponRmCurDs128To255Octets,
       "zxAnEponRmCurDs256To511Octets": zxAnEponRmCurDs256To511Octets,
       "zxAnEponRmCurDs512To1023Octets": zxAnEponRmCurDs512To1023Octets,
       "zxAnEponRmCurDs1024To1518Octets": zxAnEponRmCurDs1024To1518Octets,
       "zxAnEponRmCurDsDiscards": zxAnEponRmCurDsDiscards,
       "zxAnEponRmCurDsErrors": zxAnEponRmCurDsErrors,
       "zxAnEponRmCurUsDropEvents": zxAnEponRmCurUsDropEvents,
       "zxAnEponRmCurUsOctets": zxAnEponRmCurUsOctets,
       "zxAnEponRmCurUsPkts": zxAnEponRmCurUsPkts,
       "zxAnEponRmCurUsBcastPkts": zxAnEponRmCurUsBcastPkts,
       "zxAnEponRmCurUsMcastPkts": zxAnEponRmCurUsMcastPkts,
       "zxAnEponRmCurUsCrcErrPkts": zxAnEponRmCurUsCrcErrPkts,
       "zxAnEponRmCurUsUndersizePkts": zxAnEponRmCurUsUndersizePkts,
       "zxAnEponRmCurUsOversizePkts": zxAnEponRmCurUsOversizePkts,
       "zxAnEponRmCurUsFragments": zxAnEponRmCurUsFragments,
       "zxAnEponRmCurUsJabbers": zxAnEponRmCurUsJabbers,
       "zxAnEponRmCurUsPkts64Octets": zxAnEponRmCurUsPkts64Octets,
       "zxAnEponRmCurUs65To127Octets": zxAnEponRmCurUs65To127Octets,
       "zxAnEponRmCurUs128To255Octets": zxAnEponRmCurUs128To255Octets,
       "zxAnEponRmCurUs256To511Octets": zxAnEponRmCurUs256To511Octets,
       "zxAnEponRmCurUs512To1023Octets": zxAnEponRmCurUs512To1023Octets,
       "zxAnEponRmCurUs1024To1518Octets": zxAnEponRmCurUs1024To1518Octets,
       "zxAnEponRmCurUsDiscards": zxAnEponRmCurUsDiscards,
       "zxAnEponRmCurUsErrors": zxAnEponRmCurUsErrors,
       "zxAnEponRmCurPortStatusChanges": zxAnEponRmCurPortStatusChanges,
       "zxAnEponRmEthHisPerfTable": zxAnEponRmEthHisPerfTable,
       "zxAnEponRmEthHisPerfEntry": zxAnEponRmEthHisPerfEntry,
       "zxAnEponRmEthHisIntervalNo": zxAnEponRmEthHisIntervalNo,
       "zxAnEponRmHisDsDropEvents": zxAnEponRmHisDsDropEvents,
       "zxAnEponRmHisDsOctets": zxAnEponRmHisDsOctets,
       "zxAnEponRmHisDsPkts": zxAnEponRmHisDsPkts,
       "zxAnEponRmHisDsBcastPkts": zxAnEponRmHisDsBcastPkts,
       "zxAnEponRmHisDsMcastPkts": zxAnEponRmHisDsMcastPkts,
       "zxAnEponRmHisDsCrcErrPkts": zxAnEponRmHisDsCrcErrPkts,
       "zxAnEponRmHisDsUndersizePkts": zxAnEponRmHisDsUndersizePkts,
       "zxAnEponRmHisDsOversizePkts": zxAnEponRmHisDsOversizePkts,
       "zxAnEponRmHisDsFragments": zxAnEponRmHisDsFragments,
       "zxAnEponRmHisDsJabbers": zxAnEponRmHisDsJabbers,
       "zxAnEponRmHisDsPkts64Octets": zxAnEponRmHisDsPkts64Octets,
       "zxAnEponRmHisDs65To127Octets": zxAnEponRmHisDs65To127Octets,
       "zxAnEponRmHisDs128To255Octets": zxAnEponRmHisDs128To255Octets,
       "zxAnEponRmHisDs256To511Octets": zxAnEponRmHisDs256To511Octets,
       "zxAnEponRmHisDs512To1023Octets": zxAnEponRmHisDs512To1023Octets,
       "zxAnEponRmHisDs1024To1518Octets": zxAnEponRmHisDs1024To1518Octets,
       "zxAnEponRmHisDsDiscards": zxAnEponRmHisDsDiscards,
       "zxAnEponRmHisDsErrors": zxAnEponRmHisDsErrors,
       "zxAnEponRmHisUsDropEvents": zxAnEponRmHisUsDropEvents,
       "zxAnEponRmHisUsOctets": zxAnEponRmHisUsOctets,
       "zxAnEponRmHisUsPkts": zxAnEponRmHisUsPkts,
       "zxAnEponRmHisUsBcastPkts": zxAnEponRmHisUsBcastPkts,
       "zxAnEponRmHisUsMcastPkts": zxAnEponRmHisUsMcastPkts,
       "zxAnEponRmHisUsCrcErrPkts": zxAnEponRmHisUsCrcErrPkts,
       "zxAnEponRmHisUsUndersizePkts": zxAnEponRmHisUsUndersizePkts,
       "zxAnEponRmHisUsOversizePkts": zxAnEponRmHisUsOversizePkts,
       "zxAnEponRmHisUsFragments": zxAnEponRmHisUsFragments,
       "zxAnEponRmHisUsJabbers": zxAnEponRmHisUsJabbers,
       "zxAnEponRmHisUsPkts64Octets": zxAnEponRmHisUsPkts64Octets,
       "zxAnEponRmHisUs65To127Octets": zxAnEponRmHisUs65To127Octets,
       "zxAnEponRmHisUs128To255Octets": zxAnEponRmHisUs128To255Octets,
       "zxAnEponRmHisUs256To511Octets": zxAnEponRmHisUs256To511Octets,
       "zxAnEponRmHisUs512To1023Octets": zxAnEponRmHisUs512To1023Octets,
       "zxAnEponRmHisUs1024To1518Octets": zxAnEponRmHisUs1024To1518Octets,
       "zxAnEponRmHisUsDiscards": zxAnEponRmHisUsDiscards,
       "zxAnEponRmHisUsErrors": zxAnEponRmHisUsErrors,
       "zxAnEponRmHisPortStatusChanges": zxAnEponRmHisPortStatusChanges,
       "zxAnPtpExtOamMgmt": zxAnPtpExtOamMgmt,
       "zxAnPtpExtOamTable": zxAnPtpExtOamTable,
       "zxAnPtpExtOamEntry": zxAnPtpExtOamEntry,
       "zxAnPtpIfIndex": zxAnPtpIfIndex,
       "zxAnPtpExtOamAdminStatus": zxAnPtpExtOamAdminStatus,
       "zxAnEponOnuCustomMgmt": zxAnEponOnuCustomMgmt,
       "zxAnEponOnuTkMgmt": zxAnEponOnuTkMgmt,
       "zxAnEponOnuTkAttrMgmt": zxAnEponOnuTkAttrMgmt,
       "zxAnEponOnuTkGlobalTable": zxAnEponOnuTkGlobalTable,
       "zxAnEponOnuTkGlobalEntry": zxAnEponOnuTkGlobalEntry,
       "zxAnEponOnuTkFirmwareVer": zxAnEponOnuTkFirmwareVer,
       "zxAnEponOnuTkModeName": zxAnEponOnuTkModeName,
       "zxAnEponOnuTkPortTable": zxAnEponOnuTkPortTable,
       "zxAnEponOnuTkPortEntry": zxAnEponOnuTkPortEntry,
       "zxAnEponOnuTkPortOperStatus": zxAnEponOnuTkPortOperStatus,
       "zxAnEponOnuTkPortAutoNegStatus": zxAnEponOnuTkPortAutoNegStatus,
       "zxAnEponOnuTkPortFlowCtrlStatus": zxAnEponOnuTkPortFlowCtrlStatus,
       "zxAnEponOnuTkPortDuplexMode": zxAnEponOnuTkPortDuplexMode,
       "zxAnEponOnuTkPortAdminStatus": zxAnEponOnuTkPortAdminStatus,
       "zxAnEponOnuTkLoopbackTable": zxAnEponOnuTkLoopbackTable,
       "zxAnEponOnuTkLoopbackEntry": zxAnEponOnuTkLoopbackEntry,
       "zxAnEponOnuTkLoopbackAdminStatus": zxAnEponOnuTkLoopbackAdminStatus,
       "zxAnEponOnuTkLinkBlockTable": zxAnEponOnuTkLinkBlockTable,
       "zxAnEponOnuTkLinkBlockEntry": zxAnEponOnuTkLinkBlockEntry,
       "zxAnEponOnuTkLinkBlockAdminStatus": zxAnEponOnuTkLinkBlockAdminStatus,
       "zxAnEponOnuTkLinkBlockOamType": zxAnEponOnuTkLinkBlockOamType,
       "zxAnEponOnuTkOpticalCtrlTable": zxAnEponOnuTkOpticalCtrlTable,
       "zxAnEponOnuTkOpticalCtrlEntry": zxAnEponOnuTkOpticalCtrlEntry,
       "zxAnEponOnuTkOpticalBlockStatus": zxAnEponOnuTkOpticalBlockStatus,
       "zxAnEponOnuTkOpticalBlockDurationTime": zxAnEponOnuTkOpticalBlockDurationTime,
       "zxAnEponOnuTkOpticalBlockOamType": zxAnEponOnuTkOpticalBlockOamType,
       "zxAnEponOnuTkRstpCtrlTable": zxAnEponOnuTkRstpCtrlTable,
       "zxAnEponOnuTkRstpCtrlEntry": zxAnEponOnuTkRstpCtrlEntry,
       "zxAnEponOnuTkRstpAdminStatus": zxAnEponOnuTkRstpAdminStatus,
       "zxAnEponOnuTkMacLearningTable": zxAnEponOnuTkMacLearningTable,
       "zxAnEponOnuTkMacLearningEntry": zxAnEponOnuTkMacLearningEntry,
       "zxAnEponOnuTkMacLearningMaxNum": zxAnEponOnuTkMacLearningMaxNum,
       "zxAnEponOnuTkMacLearningOamType": zxAnEponOnuTkMacLearningOamType,
       "zxAnEponOnuTkSnoopingTable": zxAnEponOnuTkSnoopingTable,
       "zxAnEponOnuTkSnoopingEntry": zxAnEponOnuTkSnoopingEntry,
       "zxAnEponOnuTkSnoopingCtrl": zxAnEponOnuTkSnoopingCtrl,
       "zxAnEponOnuTkSnoopingRobustCnt": zxAnEponOnuTkSnoopingRobustCnt,
       "zxAnEponOnuTkSnoopingLsmq": zxAnEponOnuTkSnoopingLsmq,
       "zxAnEponOnuTkSnoopingMaxGroupNum": zxAnEponOnuTkSnoopingMaxGroupNum,
       "zxAnEponOnuTkIgmpTable": zxAnEponOnuTkIgmpTable,
       "zxAnEponOnuTkIgmpEntry": zxAnEponOnuTkIgmpEntry,
       "zxAnEponOnuTkIgmpVlanId": zxAnEponOnuTkIgmpVlanId,
       "zxAnEponOnuTkIgmpIpAddr": zxAnEponOnuTkIgmpIpAddr,
       "zxAnEponOnuTkIgmpPortList": zxAnEponOnuTkIgmpPortList,
       "zxAnEponOnuTkLoopDetectTable": zxAnEponOnuTkLoopDetectTable,
       "zxAnEponOnuTkLoopDetectEntry": zxAnEponOnuTkLoopDetectEntry,
       "zxAnEponOnuTkLoopDetectAdminStatus": zxAnEponOnuTkLoopDetectAdminStatus,
       "zxAnEponOnuTkLoopDetectInterval": zxAnEponOnuTkLoopDetectInterval,
       "zxAnEponOnuTkLoopDetectOamType": zxAnEponOnuTkLoopDetectOamType,
       "zxAnEponOnuTkPortShapingTable": zxAnEponOnuTkPortShapingTable,
       "zxAnEponOnuTkPortShapingEntry": zxAnEponOnuTkPortShapingEntry,
       "zxAnEponOnuTkPortDsShapingAdminStatus": zxAnEponOnuTkPortDsShapingAdminStatus,
       "zxAnEponOnuTkPortDsShapingRate": zxAnEponOnuTkPortDsShapingRate,
       "zxAnEponOnuTkPortDsShapingOamType": zxAnEponOnuTkPortDsShapingOamType,
       "zxAnEponOnuTkActionMgmt": zxAnEponOnuTkActionMgmt,
       "zxAnEponOnuTkRestoreActionTable": zxAnEponOnuTkRestoreActionTable,
       "zxAnEponOnuTkRestoreActionEntry": zxAnEponOnuTkRestoreActionEntry,
       "zxAnEponOnuTkRestoreFactorySettings": zxAnEponOnuTkRestoreFactorySettings,
       "zxAnEponOnuTkRestoreOamType": zxAnEponOnuTkRestoreOamType,
       "zxAnEponOnuTkUpdateVerTable": zxAnEponOnuTkUpdateVerTable,
       "zxAnEponOnuTkUpdateVerEntry": zxAnEponOnuTkUpdateVerEntry,
       "zxAnEponOnuTkVerType": zxAnEponOnuTkVerType,
       "zxAnEponOnuTkVerName": zxAnEponOnuTkVerName,
       "zxAnEponOnuTkUpdateStatus": zxAnEponOnuTkUpdateStatus,
       "zxAnEponOnuTkUpdateProgress": zxAnEponOnuTkUpdateProgress,
       "zxAnEponOnuTkOnuAckCode": zxAnEponOnuTkOnuAckCode,
       "zxAnEponOnuTkErrorCode": zxAnEponOnuTkErrorCode,
       "zxAnEponOnuTkUpdattingVerName": zxAnEponOnuTkUpdattingVerName,
       "zxAnEponOnuTkAutoUpdateVerTable": zxAnEponOnuTkAutoUpdateVerTable,
       "zxAnEponOnuTkAutoUpdateVerEntry": zxAnEponOnuTkAutoUpdateVerEntry,
       "zxAnEponOltIfIndex": zxAnEponOltIfIndex,
       "zxAnEponOnuTkAutoUpdateAdminStatus": zxAnEponOnuTkAutoUpdateAdminStatus,
       "zxAnEponOnuTkVerActiveMode": zxAnEponOnuTkVerActiveMode,
       "zxAnEponOnuTkStatisticMgmt": zxAnEponOnuTkStatisticMgmt,
       "zxAnEponOnuTkGlobalStatTable": zxAnEponOnuTkGlobalStatTable,
       "zxAnEponOnuTkGlobalStatEntry": zxAnEponOnuTkGlobalStatEntry,
       "zxAnEponOnuTkGlobalStatResetCounter": zxAnEponOnuTkGlobalStatResetCounter,
       "zxAnEponOnuTkGlobalStatOamType": zxAnEponOnuTkGlobalStatOamType,
       "zxAnEponOnuTkGlobalStatTxRegReq": zxAnEponOnuTkGlobalStatTxRegReq,
       "zxAnEponOnuTkGlobalStatRxReg": zxAnEponOnuTkGlobalStatRxReg,
       "zxAnEponOnuTkGlobalStatTxRegAck": zxAnEponOnuTkGlobalStatTxRegAck,
       "zxAnEponOnuTkGlobalStatRxGateFrames": zxAnEponOnuTkGlobalStatRxGateFrames,
       "zxAnEponOnuTkGlobalStatTxReportFrames": zxAnEponOnuTkGlobalStatTxReportFrames,
       "zxAnEponOnuTkPortStatTable": zxAnEponOnuTkPortStatTable,
       "zxAnEponOnuTkPortStatEntry": zxAnEponOnuTkPortStatEntry,
       "zxAnEponOnuTkPortStatResetCounter": zxAnEponOnuTkPortStatResetCounter,
       "zxAnEponOnuTkPortStatOamType": zxAnEponOnuTkPortStatOamType,
       "zxAnEponOnuTkPortStatTxFrames": zxAnEponOnuTkPortStatTxFrames,
       "zxAnEponOnuTkPortStatTxBytes": zxAnEponOnuTkPortStatTxBytes,
       "zxAnEponOnuTkPortStatTxMulticast": zxAnEponOnuTkPortStatTxMulticast,
       "zxAnEponOnuTkPortStatTxBroadcast": zxAnEponOnuTkPortStatTxBroadcast,
       "zxAnEponOnuTkPortStatTxDropedFrames": zxAnEponOnuTkPortStatTxDropedFrames,
       "zxAnEponOnuTkPortStatRxFrames": zxAnEponOnuTkPortStatRxFrames,
       "zxAnEponOnuTkPortStatRxBytes": zxAnEponOnuTkPortStatRxBytes,
       "zxAnEponOnuTkPortStatRxMulticast": zxAnEponOnuTkPortStatRxMulticast,
       "zxAnEponOnuTkPortStatRxBroadcast": zxAnEponOnuTkPortStatRxBroadcast,
       "zxAnEponOnuTkPortStatRxOversizeFrames": zxAnEponOnuTkPortStatRxOversizeFrames,
       "zxAnEponOnuTkPortStatRxUnderSizeFrames": zxAnEponOnuTkPortStatRxUnderSizeFrames,
       "zxAnEponOnuTkPortStatRxCrcFrames": zxAnEponOnuTkPortStatRxCrcFrames}
)
