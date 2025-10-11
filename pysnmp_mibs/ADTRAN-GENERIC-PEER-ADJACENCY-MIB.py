# SNMP MIB module (ADTRAN-GENERIC-PEER-ADJACENCY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/adtran/ADTRAN-GENERIC-PEER-ADJACENCY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:30:29 2025
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

(adGenPeerAdjacency,
 adGenPeerAdjacencyID) = mibBuilder.importSymbols(
    "ADTRAN-SHARED-CND-SYSTEM-MIB",
    "adGenPeerAdjacency",
    "adGenPeerAdjacencyID")

(InterfaceIndex,
 ifIndex) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndex",
    "ifIndex")

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
 PhysAddress,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

adGenPeerAdjacencyMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 664, 6, 10000, 70, 47, 1)
)
if mibBuilder.loadTexts:
    adGenPeerAdjacencyMIB.setRevisions(
        ("2011-10-26 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AdGenPeerAdjacencyLogical_ObjectIdentity = ObjectIdentity
adGenPeerAdjacencyLogical = _AdGenPeerAdjacencyLogical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 1)
)
_AdGenPeerAdjacencyLogicalTable_Object = MibTable
adGenPeerAdjacencyLogicalTable = _AdGenPeerAdjacencyLogicalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 1, 1)
)
if mibBuilder.loadTexts:
    adGenPeerAdjacencyLogicalTable.setStatus("current")
_AdGenPeerAdjacencyLogicalEntry_Object = MibTableRow
adGenPeerAdjacencyLogicalEntry = _AdGenPeerAdjacencyLogicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 1, 1, 1)
)
adGenPeerAdjacencyLogicalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPeerAdjacencyLogicalEntry.setStatus("current")
_AdGenPeerAdjacencyLogicalIpAddress_Type = IpAddress
_AdGenPeerAdjacencyLogicalIpAddress_Object = MibTableColumn
adGenPeerAdjacencyLogicalIpAddress = _AdGenPeerAdjacencyLogicalIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 1, 1, 1, 1),
    _AdGenPeerAdjacencyLogicalIpAddress_Type()
)
adGenPeerAdjacencyLogicalIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyLogicalIpAddress.setStatus("current")
_AdGenPeerAdjacencyLogicalChassisId_Type = OctetString
_AdGenPeerAdjacencyLogicalChassisId_Object = MibTableColumn
adGenPeerAdjacencyLogicalChassisId = _AdGenPeerAdjacencyLogicalChassisId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 1, 1, 1, 2),
    _AdGenPeerAdjacencyLogicalChassisId_Type()
)
adGenPeerAdjacencyLogicalChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyLogicalChassisId.setStatus("current")
_AdGenPeerAdjacencyLogicalPortId_Type = OctetString
_AdGenPeerAdjacencyLogicalPortId_Object = MibTableColumn
adGenPeerAdjacencyLogicalPortId = _AdGenPeerAdjacencyLogicalPortId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 1, 1, 1, 3),
    _AdGenPeerAdjacencyLogicalPortId_Type()
)
adGenPeerAdjacencyLogicalPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyLogicalPortId.setStatus("current")
_AdGenPeerAdjacencyPhysical_ObjectIdentity = ObjectIdentity
adGenPeerAdjacencyPhysical = _AdGenPeerAdjacencyPhysical_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2)
)
_AdGenPeerAdjacencyPhysicalTable_Object = MibTable
adGenPeerAdjacencyPhysicalTable = _AdGenPeerAdjacencyPhysicalTable_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1)
)
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTable.setStatus("current")
_AdGenPeerAdjacencyPhysicalEntry_Object = MibTableRow
adGenPeerAdjacencyPhysicalEntry = _AdGenPeerAdjacencyPhysicalEntry_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1)
)
adGenPeerAdjacencyPhysicalEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalEntry.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneDescriptionTx_Type = OctetString
_AdGenPeerAdjacencyPhysicalOneDescriptionTx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneDescriptionTx = _AdGenPeerAdjacencyPhysicalOneDescriptionTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 1),
    _AdGenPeerAdjacencyPhysicalOneDescriptionTx_Type()
)
adGenPeerAdjacencyPhysicalOneDescriptionTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneDescriptionTx.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneDescriptionRx_Type = OctetString
_AdGenPeerAdjacencyPhysicalOneDescriptionRx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneDescriptionRx = _AdGenPeerAdjacencyPhysicalOneDescriptionRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 2),
    _AdGenPeerAdjacencyPhysicalOneDescriptionRx_Type()
)
adGenPeerAdjacencyPhysicalOneDescriptionRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneDescriptionRx.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneIpAddressTx_Type = IpAddress
_AdGenPeerAdjacencyPhysicalOneIpAddressTx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneIpAddressTx = _AdGenPeerAdjacencyPhysicalOneIpAddressTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 3),
    _AdGenPeerAdjacencyPhysicalOneIpAddressTx_Type()
)
adGenPeerAdjacencyPhysicalOneIpAddressTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneIpAddressTx.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneIpAddressRx_Type = IpAddress
_AdGenPeerAdjacencyPhysicalOneIpAddressRx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneIpAddressRx = _AdGenPeerAdjacencyPhysicalOneIpAddressRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 4),
    _AdGenPeerAdjacencyPhysicalOneIpAddressRx_Type()
)
adGenPeerAdjacencyPhysicalOneIpAddressRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneIpAddressRx.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneChassisIdTx_Type = OctetString
_AdGenPeerAdjacencyPhysicalOneChassisIdTx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneChassisIdTx = _AdGenPeerAdjacencyPhysicalOneChassisIdTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 5),
    _AdGenPeerAdjacencyPhysicalOneChassisIdTx_Type()
)
adGenPeerAdjacencyPhysicalOneChassisIdTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneChassisIdTx.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneChassisIdRx_Type = OctetString
_AdGenPeerAdjacencyPhysicalOneChassisIdRx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneChassisIdRx = _AdGenPeerAdjacencyPhysicalOneChassisIdRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 6),
    _AdGenPeerAdjacencyPhysicalOneChassisIdRx_Type()
)
adGenPeerAdjacencyPhysicalOneChassisIdRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneChassisIdRx.setStatus("current")
_AdGenPeerAdjacencyPhysicalOnePortIdTx_Type = OctetString
_AdGenPeerAdjacencyPhysicalOnePortIdTx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOnePortIdTx = _AdGenPeerAdjacencyPhysicalOnePortIdTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 7),
    _AdGenPeerAdjacencyPhysicalOnePortIdTx_Type()
)
adGenPeerAdjacencyPhysicalOnePortIdTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOnePortIdTx.setStatus("current")
_AdGenPeerAdjacencyPhysicalOnePortIdRx_Type = OctetString
_AdGenPeerAdjacencyPhysicalOnePortIdRx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOnePortIdRx = _AdGenPeerAdjacencyPhysicalOnePortIdRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 8),
    _AdGenPeerAdjacencyPhysicalOnePortIdRx_Type()
)
adGenPeerAdjacencyPhysicalOnePortIdRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOnePortIdRx.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneUnknownDeviceTx_Type = TruthValue
_AdGenPeerAdjacencyPhysicalOneUnknownDeviceTx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneUnknownDeviceTx = _AdGenPeerAdjacencyPhysicalOneUnknownDeviceTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 9),
    _AdGenPeerAdjacencyPhysicalOneUnknownDeviceTx_Type()
)
adGenPeerAdjacencyPhysicalOneUnknownDeviceTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneUnknownDeviceTx.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneUnknownDeviceRx_Type = TruthValue
_AdGenPeerAdjacencyPhysicalOneUnknownDeviceRx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneUnknownDeviceRx = _AdGenPeerAdjacencyPhysicalOneUnknownDeviceRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 10),
    _AdGenPeerAdjacencyPhysicalOneUnknownDeviceRx_Type()
)
adGenPeerAdjacencyPhysicalOneUnknownDeviceRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneUnknownDeviceRx.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoDescriptionTx_Type = OctetString
_AdGenPeerAdjacencyPhysicalTwoDescriptionTx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoDescriptionTx = _AdGenPeerAdjacencyPhysicalTwoDescriptionTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 11),
    _AdGenPeerAdjacencyPhysicalTwoDescriptionTx_Type()
)
adGenPeerAdjacencyPhysicalTwoDescriptionTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoDescriptionTx.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoDescriptionRx_Type = OctetString
_AdGenPeerAdjacencyPhysicalTwoDescriptionRx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoDescriptionRx = _AdGenPeerAdjacencyPhysicalTwoDescriptionRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 12),
    _AdGenPeerAdjacencyPhysicalTwoDescriptionRx_Type()
)
adGenPeerAdjacencyPhysicalTwoDescriptionRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoDescriptionRx.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoIpAddressTx_Type = IpAddress
_AdGenPeerAdjacencyPhysicalTwoIpAddressTx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoIpAddressTx = _AdGenPeerAdjacencyPhysicalTwoIpAddressTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 13),
    _AdGenPeerAdjacencyPhysicalTwoIpAddressTx_Type()
)
adGenPeerAdjacencyPhysicalTwoIpAddressTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoIpAddressTx.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoIpAddressRx_Type = IpAddress
_AdGenPeerAdjacencyPhysicalTwoIpAddressRx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoIpAddressRx = _AdGenPeerAdjacencyPhysicalTwoIpAddressRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 14),
    _AdGenPeerAdjacencyPhysicalTwoIpAddressRx_Type()
)
adGenPeerAdjacencyPhysicalTwoIpAddressRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoIpAddressRx.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoChassisIdTx_Type = OctetString
_AdGenPeerAdjacencyPhysicalTwoChassisIdTx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoChassisIdTx = _AdGenPeerAdjacencyPhysicalTwoChassisIdTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 15),
    _AdGenPeerAdjacencyPhysicalTwoChassisIdTx_Type()
)
adGenPeerAdjacencyPhysicalTwoChassisIdTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoChassisIdTx.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoChassisIdRx_Type = OctetString
_AdGenPeerAdjacencyPhysicalTwoChassisIdRx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoChassisIdRx = _AdGenPeerAdjacencyPhysicalTwoChassisIdRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 16),
    _AdGenPeerAdjacencyPhysicalTwoChassisIdRx_Type()
)
adGenPeerAdjacencyPhysicalTwoChassisIdRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoChassisIdRx.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoPortIdTx_Type = OctetString
_AdGenPeerAdjacencyPhysicalTwoPortIdTx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoPortIdTx = _AdGenPeerAdjacencyPhysicalTwoPortIdTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 17),
    _AdGenPeerAdjacencyPhysicalTwoPortIdTx_Type()
)
adGenPeerAdjacencyPhysicalTwoPortIdTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoPortIdTx.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoPortIdRx_Type = OctetString
_AdGenPeerAdjacencyPhysicalTwoPortIdRx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoPortIdRx = _AdGenPeerAdjacencyPhysicalTwoPortIdRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 18),
    _AdGenPeerAdjacencyPhysicalTwoPortIdRx_Type()
)
adGenPeerAdjacencyPhysicalTwoPortIdRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoPortIdRx.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoUnknownDeviceTx_Type = TruthValue
_AdGenPeerAdjacencyPhysicalTwoUnknownDeviceTx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoUnknownDeviceTx = _AdGenPeerAdjacencyPhysicalTwoUnknownDeviceTx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 19),
    _AdGenPeerAdjacencyPhysicalTwoUnknownDeviceTx_Type()
)
adGenPeerAdjacencyPhysicalTwoUnknownDeviceTx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoUnknownDeviceTx.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoUnknownDeviceRx_Type = TruthValue
_AdGenPeerAdjacencyPhysicalTwoUnknownDeviceRx_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoUnknownDeviceRx = _AdGenPeerAdjacencyPhysicalTwoUnknownDeviceRx_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 20),
    _AdGenPeerAdjacencyPhysicalTwoUnknownDeviceRx_Type()
)
adGenPeerAdjacencyPhysicalTwoUnknownDeviceRx.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoUnknownDeviceRx.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneDescription_Type = OctetString
_AdGenPeerAdjacencyPhysicalOneDescription_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneDescription = _AdGenPeerAdjacencyPhysicalOneDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 21),
    _AdGenPeerAdjacencyPhysicalOneDescription_Type()
)
adGenPeerAdjacencyPhysicalOneDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneDescription.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneIpAddress_Type = IpAddress
_AdGenPeerAdjacencyPhysicalOneIpAddress_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneIpAddress = _AdGenPeerAdjacencyPhysicalOneIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 22),
    _AdGenPeerAdjacencyPhysicalOneIpAddress_Type()
)
adGenPeerAdjacencyPhysicalOneIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneIpAddress.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneChassisId_Type = OctetString
_AdGenPeerAdjacencyPhysicalOneChassisId_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneChassisId = _AdGenPeerAdjacencyPhysicalOneChassisId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 23),
    _AdGenPeerAdjacencyPhysicalOneChassisId_Type()
)
adGenPeerAdjacencyPhysicalOneChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneChassisId.setStatus("current")
_AdGenPeerAdjacencyPhysicalOnePortId_Type = OctetString
_AdGenPeerAdjacencyPhysicalOnePortId_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOnePortId = _AdGenPeerAdjacencyPhysicalOnePortId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 24),
    _AdGenPeerAdjacencyPhysicalOnePortId_Type()
)
adGenPeerAdjacencyPhysicalOnePortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOnePortId.setStatus("current")
_AdGenPeerAdjacencyPhysicalOneUnknownDevice_Type = TruthValue
_AdGenPeerAdjacencyPhysicalOneUnknownDevice_Object = MibTableColumn
adGenPeerAdjacencyPhysicalOneUnknownDevice = _AdGenPeerAdjacencyPhysicalOneUnknownDevice_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 25),
    _AdGenPeerAdjacencyPhysicalOneUnknownDevice_Type()
)
adGenPeerAdjacencyPhysicalOneUnknownDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalOneUnknownDevice.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoDescription_Type = OctetString
_AdGenPeerAdjacencyPhysicalTwoDescription_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoDescription = _AdGenPeerAdjacencyPhysicalTwoDescription_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 26),
    _AdGenPeerAdjacencyPhysicalTwoDescription_Type()
)
adGenPeerAdjacencyPhysicalTwoDescription.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoDescription.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoIpAddress_Type = IpAddress
_AdGenPeerAdjacencyPhysicalTwoIpAddress_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoIpAddress = _AdGenPeerAdjacencyPhysicalTwoIpAddress_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 27),
    _AdGenPeerAdjacencyPhysicalTwoIpAddress_Type()
)
adGenPeerAdjacencyPhysicalTwoIpAddress.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoIpAddress.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoChassisId_Type = OctetString
_AdGenPeerAdjacencyPhysicalTwoChassisId_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoChassisId = _AdGenPeerAdjacencyPhysicalTwoChassisId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 28),
    _AdGenPeerAdjacencyPhysicalTwoChassisId_Type()
)
adGenPeerAdjacencyPhysicalTwoChassisId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoChassisId.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoPortId_Type = OctetString
_AdGenPeerAdjacencyPhysicalTwoPortId_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoPortId = _AdGenPeerAdjacencyPhysicalTwoPortId_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 29),
    _AdGenPeerAdjacencyPhysicalTwoPortId_Type()
)
adGenPeerAdjacencyPhysicalTwoPortId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoPortId.setStatus("current")
_AdGenPeerAdjacencyPhysicalTwoUnknownDevice_Type = TruthValue
_AdGenPeerAdjacencyPhysicalTwoUnknownDevice_Object = MibTableColumn
adGenPeerAdjacencyPhysicalTwoUnknownDevice = _AdGenPeerAdjacencyPhysicalTwoUnknownDevice_Object(
    (1, 3, 6, 1, 4, 1, 664, 5, 70, 47, 2, 1, 1, 30),
    _AdGenPeerAdjacencyPhysicalTwoUnknownDevice_Type()
)
adGenPeerAdjacencyPhysicalTwoUnknownDevice.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    adGenPeerAdjacencyPhysicalTwoUnknownDevice.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ADTRAN-GENERIC-PEER-ADJACENCY-MIB",
    **{"adGenPeerAdjacencyLogical": adGenPeerAdjacencyLogical,
       "adGenPeerAdjacencyLogicalTable": adGenPeerAdjacencyLogicalTable,
       "adGenPeerAdjacencyLogicalEntry": adGenPeerAdjacencyLogicalEntry,
       "adGenPeerAdjacencyLogicalIpAddress": adGenPeerAdjacencyLogicalIpAddress,
       "adGenPeerAdjacencyLogicalChassisId": adGenPeerAdjacencyLogicalChassisId,
       "adGenPeerAdjacencyLogicalPortId": adGenPeerAdjacencyLogicalPortId,
       "adGenPeerAdjacencyPhysical": adGenPeerAdjacencyPhysical,
       "adGenPeerAdjacencyPhysicalTable": adGenPeerAdjacencyPhysicalTable,
       "adGenPeerAdjacencyPhysicalEntry": adGenPeerAdjacencyPhysicalEntry,
       "adGenPeerAdjacencyPhysicalOneDescriptionTx": adGenPeerAdjacencyPhysicalOneDescriptionTx,
       "adGenPeerAdjacencyPhysicalOneDescriptionRx": adGenPeerAdjacencyPhysicalOneDescriptionRx,
       "adGenPeerAdjacencyPhysicalOneIpAddressTx": adGenPeerAdjacencyPhysicalOneIpAddressTx,
       "adGenPeerAdjacencyPhysicalOneIpAddressRx": adGenPeerAdjacencyPhysicalOneIpAddressRx,
       "adGenPeerAdjacencyPhysicalOneChassisIdTx": adGenPeerAdjacencyPhysicalOneChassisIdTx,
       "adGenPeerAdjacencyPhysicalOneChassisIdRx": adGenPeerAdjacencyPhysicalOneChassisIdRx,
       "adGenPeerAdjacencyPhysicalOnePortIdTx": adGenPeerAdjacencyPhysicalOnePortIdTx,
       "adGenPeerAdjacencyPhysicalOnePortIdRx": adGenPeerAdjacencyPhysicalOnePortIdRx,
       "adGenPeerAdjacencyPhysicalOneUnknownDeviceTx": adGenPeerAdjacencyPhysicalOneUnknownDeviceTx,
       "adGenPeerAdjacencyPhysicalOneUnknownDeviceRx": adGenPeerAdjacencyPhysicalOneUnknownDeviceRx,
       "adGenPeerAdjacencyPhysicalTwoDescriptionTx": adGenPeerAdjacencyPhysicalTwoDescriptionTx,
       "adGenPeerAdjacencyPhysicalTwoDescriptionRx": adGenPeerAdjacencyPhysicalTwoDescriptionRx,
       "adGenPeerAdjacencyPhysicalTwoIpAddressTx": adGenPeerAdjacencyPhysicalTwoIpAddressTx,
       "adGenPeerAdjacencyPhysicalTwoIpAddressRx": adGenPeerAdjacencyPhysicalTwoIpAddressRx,
       "adGenPeerAdjacencyPhysicalTwoChassisIdTx": adGenPeerAdjacencyPhysicalTwoChassisIdTx,
       "adGenPeerAdjacencyPhysicalTwoChassisIdRx": adGenPeerAdjacencyPhysicalTwoChassisIdRx,
       "adGenPeerAdjacencyPhysicalTwoPortIdTx": adGenPeerAdjacencyPhysicalTwoPortIdTx,
       "adGenPeerAdjacencyPhysicalTwoPortIdRx": adGenPeerAdjacencyPhysicalTwoPortIdRx,
       "adGenPeerAdjacencyPhysicalTwoUnknownDeviceTx": adGenPeerAdjacencyPhysicalTwoUnknownDeviceTx,
       "adGenPeerAdjacencyPhysicalTwoUnknownDeviceRx": adGenPeerAdjacencyPhysicalTwoUnknownDeviceRx,
       "adGenPeerAdjacencyPhysicalOneDescription": adGenPeerAdjacencyPhysicalOneDescription,
       "adGenPeerAdjacencyPhysicalOneIpAddress": adGenPeerAdjacencyPhysicalOneIpAddress,
       "adGenPeerAdjacencyPhysicalOneChassisId": adGenPeerAdjacencyPhysicalOneChassisId,
       "adGenPeerAdjacencyPhysicalOnePortId": adGenPeerAdjacencyPhysicalOnePortId,
       "adGenPeerAdjacencyPhysicalOneUnknownDevice": adGenPeerAdjacencyPhysicalOneUnknownDevice,
       "adGenPeerAdjacencyPhysicalTwoDescription": adGenPeerAdjacencyPhysicalTwoDescription,
       "adGenPeerAdjacencyPhysicalTwoIpAddress": adGenPeerAdjacencyPhysicalTwoIpAddress,
       "adGenPeerAdjacencyPhysicalTwoChassisId": adGenPeerAdjacencyPhysicalTwoChassisId,
       "adGenPeerAdjacencyPhysicalTwoPortId": adGenPeerAdjacencyPhysicalTwoPortId,
       "adGenPeerAdjacencyPhysicalTwoUnknownDevice": adGenPeerAdjacencyPhysicalTwoUnknownDevice,
       "adGenPeerAdjacencyMIB": adGenPeerAdjacencyMIB}
)
