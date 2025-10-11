# SNMP MIB module (H3C-EVB-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/h3c/H3C-EVB-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:18:10 2025
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

(h3cCommon,) = mibBuilder.importSymbols(
    "HUAWEI-3COM-OID-MIB",
    "h3cCommon")

(IEEE8021BridgePortNumber,) = mibBuilder.importSymbols(
    "IEEE8021-TC-MIB",
    "IEEE8021BridgePortNumber")

(InterfaceIndexOrZero,) = mibBuilder.importSymbols(
    "IF-MIB",
    "InterfaceIndexOrZero")

(VlanIndex,) = mibBuilder.importSymbols(
    "Q-BRIDGE-MIB",
    "VlanIndex")

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


# MODULE-IDENTITY

h3cEvb = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134)
)
if mibBuilder.loadTexts:
    h3cEvb.setRevisions(
        ("2012-12-21 12:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_H3cEvbSysObjects_ObjectIdentity = ObjectIdentity
h3cEvbSysObjects = _H3cEvbSysObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 1)
)


class _H3cEvbSetResult_Type(Integer32):
    """Custom type h3cEvbSetResult based on Integer32"""
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
        *(("unknown", 1),
          ("processing", 2),
          ("success", 3),
          ("failed", 4))
    )


_H3cEvbSetResult_Type.__name__ = "Integer32"
_H3cEvbSetResult_Object = MibScalar
h3cEvbSetResult = _H3cEvbSetResult_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 1, 1),
    _H3cEvbSetResult_Type()
)
h3cEvbSetResult.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvbSetResult.setStatus("current")
_H3cEvbDefaultManagerTable_Object = MibTable
h3cEvbDefaultManagerTable = _H3cEvbDefaultManagerTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 1, 2)
)
if mibBuilder.loadTexts:
    h3cEvbDefaultManagerTable.setStatus("current")
_H3cEvbDefaultManagerEntry_Object = MibTableRow
h3cEvbDefaultManagerEntry = _H3cEvbDefaultManagerEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 1, 2, 1)
)
h3cEvbDefaultManagerEntry.setIndexNames(
    (0, "H3C-EVB-MIB", "h3cEvbManagerIndex"),
)
if mibBuilder.loadTexts:
    h3cEvbDefaultManagerEntry.setStatus("current")
_H3cEvbManagerIndex_Type = Unsigned32
_H3cEvbManagerIndex_Object = MibTableColumn
h3cEvbManagerIndex = _H3cEvbManagerIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 1, 2, 1, 1),
    _H3cEvbManagerIndex_Type()
)
h3cEvbManagerIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvbManagerIndex.setStatus("current")


class _H3cEvbManagerType_Type(Integer32):
    """Custom type h3cEvbManagerType based on Integer32"""
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
        *(("ipv4", 1),
          ("ipv6", 2),
          ("name", 3),
          ("local", 4))
    )


_H3cEvbManagerType_Type.__name__ = "Integer32"
_H3cEvbManagerType_Object = MibTableColumn
h3cEvbManagerType = _H3cEvbManagerType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 1, 2, 1, 2),
    _H3cEvbManagerType_Type()
)
h3cEvbManagerType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvbManagerType.setStatus("current")


class _H3cEvbManagerID_Type(OctetString):
    """Custom type h3cEvbManagerID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 127),
    )


_H3cEvbManagerID_Type.__name__ = "OctetString"
_H3cEvbManagerID_Object = MibTableColumn
h3cEvbManagerID = _H3cEvbManagerID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 1, 2, 1, 3),
    _H3cEvbManagerID_Type()
)
h3cEvbManagerID.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvbManagerID.setStatus("current")


class _H3cEvbManagerPort_Type(Unsigned32):
    """Custom type h3cEvbManagerPort based on Unsigned32"""
    defaultValue = 8080

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 65535),
    )


_H3cEvbManagerPort_Type.__name__ = "Unsigned32"
_H3cEvbManagerPort_Object = MibTableColumn
h3cEvbManagerPort = _H3cEvbManagerPort_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 1, 2, 1, 4),
    _H3cEvbManagerPort_Type()
)
h3cEvbManagerPort.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvbManagerPort.setStatus("current")
_H3cEvbManagerRowStatus_Type = RowStatus
_H3cEvbManagerRowStatus_Object = MibTableColumn
h3cEvbManagerRowStatus = _H3cEvbManagerRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 1, 2, 1, 5),
    _H3cEvbManagerRowStatus_Type()
)
h3cEvbManagerRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvbManagerRowStatus.setStatus("current")
_H3cEvbPortObjects_ObjectIdentity = ObjectIdentity
h3cEvbPortObjects = _H3cEvbPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2)
)
_H3cEvbPortConfigTable_Object = MibTable
h3cEvbPortConfigTable = _H3cEvbPortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 1)
)
if mibBuilder.loadTexts:
    h3cEvbPortConfigTable.setStatus("current")
_H3cEvbPortConfigEntry_Object = MibTableRow
h3cEvbPortConfigEntry = _H3cEvbPortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 1, 1)
)
h3cEvbPortConfigEntry.setIndexNames(
    (0, "H3C-EVB-MIB", "h3cEvbPortNumber"),
)
if mibBuilder.loadTexts:
    h3cEvbPortConfigEntry.setStatus("current")
_H3cEvbPortNumber_Type = IEEE8021BridgePortNumber
_H3cEvbPortNumber_Object = MibTableColumn
h3cEvbPortNumber = _H3cEvbPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 1, 1, 1),
    _H3cEvbPortNumber_Type()
)
h3cEvbPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvbPortNumber.setStatus("current")


class _H3cEvbRWD_Type(Unsigned32):
    """Custom type h3cEvbRWD based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(15, 31),
    )


_H3cEvbRWD_Type.__name__ = "Unsigned32"
_H3cEvbRWD_Object = MibTableColumn
h3cEvbRWD = _H3cEvbRWD_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 1, 1, 2),
    _H3cEvbRWD_Type()
)
h3cEvbRWD.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEvbRWD.setStatus("current")


class _H3cEvbRKA_Type(Unsigned32):
    """Custom type h3cEvbRKA based on Unsigned32"""
    defaultValue = 20

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(14, 31),
    )


_H3cEvbRKA_Type.__name__ = "Unsigned32"
_H3cEvbRKA_Object = MibTableColumn
h3cEvbRKA = _H3cEvbRKA_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 1, 1, 3),
    _H3cEvbRKA_Type()
)
h3cEvbRKA.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEvbRKA.setStatus("current")
_H3cEvbSchannelConfigTable_Object = MibTable
h3cEvbSchannelConfigTable = _H3cEvbSchannelConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 2)
)
if mibBuilder.loadTexts:
    h3cEvbSchannelConfigTable.setStatus("current")
_H3cEvbSchannelConfigEntry_Object = MibTableRow
h3cEvbSchannelConfigEntry = _H3cEvbSchannelConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 2, 1)
)
h3cEvbSchannelConfigEntry.setIndexNames(
    (0, "H3C-EVB-MIB", "h3cEvbPortNumber"),
    (0, "H3C-EVB-MIB", "h3cEvbSchannelID"),
)
if mibBuilder.loadTexts:
    h3cEvbSchannelConfigEntry.setStatus("current")
_H3cEvbSchannelID_Type = Unsigned32
_H3cEvbSchannelID_Object = MibTableColumn
h3cEvbSchannelID = _H3cEvbSchannelID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 2, 1, 1),
    _H3cEvbSchannelID_Type()
)
h3cEvbSchannelID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvbSchannelID.setStatus("current")


class _H3cEvbSchannelSVLAN_Type(Unsigned32):
    """Custom type h3cEvbSchannelSVLAN based on Unsigned32"""
    defaultValue = 0

    subtypeSpec = Unsigned32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(0, 4094),
    )


_H3cEvbSchannelSVLAN_Type.__name__ = "Unsigned32"
_H3cEvbSchannelSVLAN_Object = MibTableColumn
h3cEvbSchannelSVLAN = _H3cEvbSchannelSVLAN_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 2, 1, 2),
    _H3cEvbSchannelSVLAN_Type()
)
h3cEvbSchannelSVLAN.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvbSchannelSVLAN.setStatus("current")


class _H3cEvbMacLearningStatus_Type(TruthValue):
    """Custom type h3cEvbMacLearningStatus based on TruthValue"""
    defaultValue = 1


_H3cEvbMacLearningStatus_Type.__name__ = "TruthValue"
_H3cEvbMacLearningStatus_Object = MibTableColumn
h3cEvbMacLearningStatus = _H3cEvbMacLearningStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 2, 1, 3),
    _H3cEvbMacLearningStatus_Type()
)
h3cEvbMacLearningStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEvbMacLearningStatus.setStatus("current")


class _H3cEvbRRStatus_Type(TruthValue):
    """Custom type h3cEvbRRStatus based on TruthValue"""
    defaultValue = 2


_H3cEvbRRStatus_Type.__name__ = "TruthValue"
_H3cEvbRRStatus_Object = MibTableColumn
h3cEvbRRStatus = _H3cEvbRRStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 2, 1, 4),
    _H3cEvbRRStatus_Type()
)
h3cEvbRRStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEvbRRStatus.setStatus("current")
_H3cEvbSchannelRowStatus_Type = RowStatus
_H3cEvbSchannelRowStatus_Object = MibTableColumn
h3cEvbSchannelRowStatus = _H3cEvbSchannelRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 2, 1, 5),
    _H3cEvbSchannelRowStatus_Type()
)
h3cEvbSchannelRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvbSchannelRowStatus.setStatus("current")
_H3cEvbVSIConfigTable_Object = MibTable
h3cEvbVSIConfigTable = _H3cEvbVSIConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 3)
)
if mibBuilder.loadTexts:
    h3cEvbVSIConfigTable.setStatus("current")
_H3cEvbVSIConfigEntry_Object = MibTableRow
h3cEvbVSIConfigEntry = _H3cEvbVSIConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 3, 1)
)
h3cEvbVSIConfigEntry.setIndexNames(
    (0, "H3C-EVB-MIB", "h3cEvbSBPPortNumber"),
    (0, "H3C-EVB-MIB", "h3cEvbVSILocalID"),
)
if mibBuilder.loadTexts:
    h3cEvbVSIConfigEntry.setStatus("current")
_H3cEvbSBPPortNumber_Type = IEEE8021BridgePortNumber
_H3cEvbSBPPortNumber_Object = MibTableColumn
h3cEvbSBPPortNumber = _H3cEvbSBPPortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 3, 1, 1),
    _H3cEvbSBPPortNumber_Type()
)
h3cEvbSBPPortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvbSBPPortNumber.setStatus("current")
_H3cEvbVSILocalID_Type = Unsigned32
_H3cEvbVSILocalID_Object = MibTableColumn
h3cEvbVSILocalID = _H3cEvbVSILocalID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 3, 1, 2),
    _H3cEvbVSILocalID_Type()
)
h3cEvbVSILocalID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvbVSILocalID.setStatus("current")


class _H3cEvbVSICommand_Type(Integer32):
    """Custom type h3cEvbVSICommand based on Integer32"""
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
        *(("preAssociate", 1),
          ("preAssociateWithRsrcReservation", 2),
          ("associate", 3),
          ("deAssociate", 4))
    )


_H3cEvbVSICommand_Type.__name__ = "Integer32"
_H3cEvbVSICommand_Object = MibTableColumn
h3cEvbVSICommand = _H3cEvbVSICommand_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 3, 1, 3),
    _H3cEvbVSICommand_Type()
)
h3cEvbVSICommand.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvbVSICommand.setStatus("current")
_H3cEvbVSIIfIndex_Type = InterfaceIndexOrZero
_H3cEvbVSIIfIndex_Object = MibTableColumn
h3cEvbVSIIfIndex = _H3cEvbVSIIfIndex_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 3, 1, 4),
    _H3cEvbVSIIfIndex_Type()
)
h3cEvbVSIIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cEvbVSIIfIndex.setStatus("current")


class _H3cEvbVSIIsActive_Type(TruthValue):
    """Custom type h3cEvbVSIIsActive based on TruthValue"""
    defaultValue = 2


_H3cEvbVSIIsActive_Type.__name__ = "TruthValue"
_H3cEvbVSIIsActive_Object = MibTableColumn
h3cEvbVSIIsActive = _H3cEvbVSIIsActive_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 3, 1, 5),
    _H3cEvbVSIIsActive_Type()
)
h3cEvbVSIIsActive.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cEvbVSIIsActive.setStatus("current")
_H3cEvbVSIRowStatus_Type = RowStatus
_H3cEvbVSIRowStatus_Object = MibTableColumn
h3cEvbVSIRowStatus = _H3cEvbVSIRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 3, 1, 6),
    _H3cEvbVSIRowStatus_Type()
)
h3cEvbVSIRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvbVSIRowStatus.setStatus("current")
_H3cEvbVSIFilterConfigTable_Object = MibTable
h3cEvbVSIFilterConfigTable = _H3cEvbVSIFilterConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 4)
)
if mibBuilder.loadTexts:
    h3cEvbVSIFilterConfigTable.setStatus("current")
_H3cEvbVSIFilterConfigEntry_Object = MibTableRow
h3cEvbVSIFilterConfigEntry = _H3cEvbVSIFilterConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 4, 1)
)
h3cEvbVSIFilterConfigEntry.setIndexNames(
    (0, "H3C-EVB-MIB", "h3cEvbSBPPortNumber"),
    (0, "H3C-EVB-MIB", "h3cEvbVSILocalID"),
    (0, "H3C-EVB-MIB", "h3cEvbGroupID"),
    (0, "H3C-EVB-MIB", "h3cEvbVSIMac"),
    (0, "H3C-EVB-MIB", "h3cEvbVSIVlanId"),
)
if mibBuilder.loadTexts:
    h3cEvbVSIFilterConfigEntry.setStatus("current")
_H3cEvbGroupID_Type = Unsigned32
_H3cEvbGroupID_Object = MibTableColumn
h3cEvbGroupID = _H3cEvbGroupID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 4, 1, 1),
    _H3cEvbGroupID_Type()
)
h3cEvbGroupID.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvbGroupID.setStatus("current")
_H3cEvbVSIMac_Type = MacAddress
_H3cEvbVSIMac_Object = MibTableColumn
h3cEvbVSIMac = _H3cEvbVSIMac_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 4, 1, 2),
    _H3cEvbVSIMac_Type()
)
h3cEvbVSIMac.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvbVSIMac.setStatus("current")
_H3cEvbVSIVlanId_Type = VlanIndex
_H3cEvbVSIVlanId_Object = MibTableColumn
h3cEvbVSIVlanId = _H3cEvbVSIVlanId_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 4, 1, 3),
    _H3cEvbVSIVlanId_Type()
)
h3cEvbVSIVlanId.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cEvbVSIVlanId.setStatus("current")
_H3cEvbVSIFilterRowStatus_Type = RowStatus
_H3cEvbVSIFilterRowStatus_Object = MibTableColumn
h3cEvbVSIFilterRowStatus = _H3cEvbVSIFilterRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 2, 4, 1, 4),
    _H3cEvbVSIFilterRowStatus_Type()
)
h3cEvbVSIFilterRowStatus.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    h3cEvbVSIFilterRowStatus.setStatus("current")
_H3cFlex10Objects_ObjectIdentity = ObjectIdentity
h3cFlex10Objects = _H3cFlex10Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3)
)
_H3cFlex10PortConfigTable_Object = MibTable
h3cFlex10PortConfigTable = _H3cFlex10PortConfigTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 1)
)
if mibBuilder.loadTexts:
    h3cFlex10PortConfigTable.setStatus("current")
_H3cFlex10PortConfigEntry_Object = MibTableRow
h3cFlex10PortConfigEntry = _H3cFlex10PortConfigEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 1, 1)
)
h3cFlex10PortConfigEntry.setIndexNames(
    (0, "H3C-EVB-MIB", "h3cFlex10PortNumber"),
)
if mibBuilder.loadTexts:
    h3cFlex10PortConfigEntry.setStatus("current")
_H3cFlex10PortNumber_Type = IEEE8021BridgePortNumber
_H3cFlex10PortNumber_Object = MibTableColumn
h3cFlex10PortNumber = _H3cFlex10PortNumber_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 1, 1, 1),
    _H3cFlex10PortNumber_Type()
)
h3cFlex10PortNumber.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    h3cFlex10PortNumber.setStatus("current")


class _H3cFlex10PortEnableStatus_Type(TruthValue):
    """Custom type h3cFlex10PortEnableStatus based on TruthValue"""
    defaultValue = 2


_H3cFlex10PortEnableStatus_Type.__name__ = "TruthValue"
_H3cFlex10PortEnableStatus_Object = MibTableColumn
h3cFlex10PortEnableStatus = _H3cFlex10PortEnableStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 1, 1, 2),
    _H3cFlex10PortEnableStatus_Type()
)
h3cFlex10PortEnableStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    h3cFlex10PortEnableStatus.setStatus("current")
_H3cFlex10RemoteSchannelTable_Object = MibTable
h3cFlex10RemoteSchannelTable = _H3cFlex10RemoteSchannelTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 2)
)
if mibBuilder.loadTexts:
    h3cFlex10RemoteSchannelTable.setStatus("current")
_H3cFlex10RemoteSchannelEntry_Object = MibTableRow
h3cFlex10RemoteSchannelEntry = _H3cFlex10RemoteSchannelEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 2, 1)
)
h3cFlex10RemoteSchannelEntry.setIndexNames(
    (0, "H3C-EVB-MIB", "h3cFlex10PortNumber"),
    (0, "H3C-EVB-MIB", "h3cEvbSchannelID"),
)
if mibBuilder.loadTexts:
    h3cFlex10RemoteSchannelEntry.setStatus("current")


class _H3cFlex10RemSchDesFormat_Type(Bits):
    """Custom type h3cFlex10RemSchDesFormat based on Bits"""
    namedValues = NamedValues(
        *(("format0", 0),
          ("format1", 1))
    )

_H3cFlex10RemSchDesFormat_Type.__name__ = "Bits"
_H3cFlex10RemSchDesFormat_Object = MibTableColumn
h3cFlex10RemSchDesFormat = _H3cFlex10RemSchDesFormat_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 2, 1, 1),
    _H3cFlex10RemSchDesFormat_Type()
)
h3cFlex10RemSchDesFormat.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlex10RemSchDesFormat.setStatus("current")
_H3cFlex10RemSchTerminationType_Type = Integer32
_H3cFlex10RemSchTerminationType_Object = MibTableColumn
h3cFlex10RemSchTerminationType = _H3cFlex10RemSchTerminationType_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 2, 1, 2),
    _H3cFlex10RemSchTerminationType_Type()
)
h3cFlex10RemSchTerminationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlex10RemSchTerminationType.setStatus("current")


class _H3cFlex10RemSchTerminationCap_Type(Bits):
    """Custom type h3cFlex10RemSchTerminationCap based on Bits"""
    namedValues = NamedValues(
        *(("ethernet", 0),
          ("fCOE", 1),
          ("iSCSI", 2),
          ("roCEE", 3))
    )

_H3cFlex10RemSchTerminationCap_Type.__name__ = "Bits"
_H3cFlex10RemSchTerminationCap_Object = MibTableColumn
h3cFlex10RemSchTerminationCap = _H3cFlex10RemSchTerminationCap_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 2, 1, 3),
    _H3cFlex10RemSchTerminationCap_Type()
)
h3cFlex10RemSchTerminationCap.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlex10RemSchTerminationCap.setStatus("current")


class _H3cFlex10RemSchTrafficClass_Type(Bits):
    """Custom type h3cFlex10RemSchTrafficClass based on Bits"""
    namedValues = NamedValues(
        *(("class0", 0),
          ("class1", 1),
          ("class2", 2),
          ("class3", 3),
          ("class4", 4),
          ("class5", 5),
          ("class6", 6),
          ("class7", 7))
    )

_H3cFlex10RemSchTrafficClass_Type.__name__ = "Bits"
_H3cFlex10RemSchTrafficClass_Object = MibTableColumn
h3cFlex10RemSchTrafficClass = _H3cFlex10RemSchTrafficClass_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 2, 1, 4),
    _H3cFlex10RemSchTrafficClass_Type()
)
h3cFlex10RemSchTrafficClass.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlex10RemSchTrafficClass.setStatus("current")
_H3cFlex10RemSchCir_Type = Integer32
_H3cFlex10RemSchCir_Object = MibTableColumn
h3cFlex10RemSchCir = _H3cFlex10RemSchCir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 2, 1, 5),
    _H3cFlex10RemSchCir_Type()
)
h3cFlex10RemSchCir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlex10RemSchCir.setStatus("current")
if mibBuilder.loadTexts:
    h3cFlex10RemSchCir.setUnits("mbps")
_H3cFlex10RemSchPir_Type = Integer32
_H3cFlex10RemSchPir_Object = MibTableColumn
h3cFlex10RemSchPir = _H3cFlex10RemSchPir_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 2, 1, 6),
    _H3cFlex10RemSchPir_Type()
)
h3cFlex10RemSchPir.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlex10RemSchPir.setStatus("current")
if mibBuilder.loadTexts:
    h3cFlex10RemSchPir.setUnits("mbps")


class _H3cFlex10RemSchConnectionID_Type(OctetString):
    """Custom type h3cFlex10RemSchConnectionID based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 16),
    )


_H3cFlex10RemSchConnectionID_Type.__name__ = "OctetString"
_H3cFlex10RemSchConnectionID_Object = MibTableColumn
h3cFlex10RemSchConnectionID = _H3cFlex10RemSchConnectionID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 2, 1, 7),
    _H3cFlex10RemSchConnectionID_Type()
)
h3cFlex10RemSchConnectionID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlex10RemSchConnectionID.setStatus("current")
_H3cFlex10SchannelLinkCtlTable_Object = MibTable
h3cFlex10SchannelLinkCtlTable = _H3cFlex10SchannelLinkCtlTable_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 3)
)
if mibBuilder.loadTexts:
    h3cFlex10SchannelLinkCtlTable.setStatus("current")
_H3cFlex10SchannelLinkCtlEntry_Object = MibTableRow
h3cFlex10SchannelLinkCtlEntry = _H3cFlex10SchannelLinkCtlEntry_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 3, 1)
)
h3cFlex10SchannelLinkCtlEntry.setIndexNames(
    (0, "H3C-EVB-MIB", "h3cFlex10PortNumber"),
    (0, "H3C-EVB-MIB", "h3cEvbSchannelID"),
)
if mibBuilder.loadTexts:
    h3cFlex10SchannelLinkCtlEntry.setStatus("current")
_H3cFlex10SchannelSVID_Type = VlanIndex
_H3cFlex10SchannelSVID_Object = MibTableColumn
h3cFlex10SchannelSVID = _H3cFlex10SchannelSVID_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 3, 1, 1),
    _H3cFlex10SchannelSVID_Type()
)
h3cFlex10SchannelSVID.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlex10SchannelSVID.setStatus("current")


class _H3cFlex10SchannelLocalStatus_Type(Integer32):
    """Custom type h3cFlex10SchannelLocalStatus based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 3))
    )


_H3cFlex10SchannelLocalStatus_Type.__name__ = "Integer32"
_H3cFlex10SchannelLocalStatus_Object = MibTableColumn
h3cFlex10SchannelLocalStatus = _H3cFlex10SchannelLocalStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 3, 1, 2),
    _H3cFlex10SchannelLocalStatus_Type()
)
h3cFlex10SchannelLocalStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlex10SchannelLocalStatus.setStatus("current")


class _H3cFlex10SchannelRemoteStatus_Type(Integer32):
    """Custom type h3cFlex10SchannelRemoteStatus based on Integer32"""
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
          ("disabled", 2),
          ("enabled", 3))
    )


_H3cFlex10SchannelRemoteStatus_Type.__name__ = "Integer32"
_H3cFlex10SchannelRemoteStatus_Object = MibTableColumn
h3cFlex10SchannelRemoteStatus = _H3cFlex10SchannelRemoteStatus_Object(
    (1, 3, 6, 1, 4, 1, 2011, 10, 2, 134, 3, 3, 1, 3),
    _H3cFlex10SchannelRemoteStatus_Type()
)
h3cFlex10SchannelRemoteStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    h3cFlex10SchannelRemoteStatus.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "H3C-EVB-MIB",
    **{"h3cEvb": h3cEvb,
       "h3cEvbSysObjects": h3cEvbSysObjects,
       "h3cEvbSetResult": h3cEvbSetResult,
       "h3cEvbDefaultManagerTable": h3cEvbDefaultManagerTable,
       "h3cEvbDefaultManagerEntry": h3cEvbDefaultManagerEntry,
       "h3cEvbManagerIndex": h3cEvbManagerIndex,
       "h3cEvbManagerType": h3cEvbManagerType,
       "h3cEvbManagerID": h3cEvbManagerID,
       "h3cEvbManagerPort": h3cEvbManagerPort,
       "h3cEvbManagerRowStatus": h3cEvbManagerRowStatus,
       "h3cEvbPortObjects": h3cEvbPortObjects,
       "h3cEvbPortConfigTable": h3cEvbPortConfigTable,
       "h3cEvbPortConfigEntry": h3cEvbPortConfigEntry,
       "h3cEvbPortNumber": h3cEvbPortNumber,
       "h3cEvbRWD": h3cEvbRWD,
       "h3cEvbRKA": h3cEvbRKA,
       "h3cEvbSchannelConfigTable": h3cEvbSchannelConfigTable,
       "h3cEvbSchannelConfigEntry": h3cEvbSchannelConfigEntry,
       "h3cEvbSchannelID": h3cEvbSchannelID,
       "h3cEvbSchannelSVLAN": h3cEvbSchannelSVLAN,
       "h3cEvbMacLearningStatus": h3cEvbMacLearningStatus,
       "h3cEvbRRStatus": h3cEvbRRStatus,
       "h3cEvbSchannelRowStatus": h3cEvbSchannelRowStatus,
       "h3cEvbVSIConfigTable": h3cEvbVSIConfigTable,
       "h3cEvbVSIConfigEntry": h3cEvbVSIConfigEntry,
       "h3cEvbSBPPortNumber": h3cEvbSBPPortNumber,
       "h3cEvbVSILocalID": h3cEvbVSILocalID,
       "h3cEvbVSICommand": h3cEvbVSICommand,
       "h3cEvbVSIIfIndex": h3cEvbVSIIfIndex,
       "h3cEvbVSIIsActive": h3cEvbVSIIsActive,
       "h3cEvbVSIRowStatus": h3cEvbVSIRowStatus,
       "h3cEvbVSIFilterConfigTable": h3cEvbVSIFilterConfigTable,
       "h3cEvbVSIFilterConfigEntry": h3cEvbVSIFilterConfigEntry,
       "h3cEvbGroupID": h3cEvbGroupID,
       "h3cEvbVSIMac": h3cEvbVSIMac,
       "h3cEvbVSIVlanId": h3cEvbVSIVlanId,
       "h3cEvbVSIFilterRowStatus": h3cEvbVSIFilterRowStatus,
       "h3cFlex10Objects": h3cFlex10Objects,
       "h3cFlex10PortConfigTable": h3cFlex10PortConfigTable,
       "h3cFlex10PortConfigEntry": h3cFlex10PortConfigEntry,
       "h3cFlex10PortNumber": h3cFlex10PortNumber,
       "h3cFlex10PortEnableStatus": h3cFlex10PortEnableStatus,
       "h3cFlex10RemoteSchannelTable": h3cFlex10RemoteSchannelTable,
       "h3cFlex10RemoteSchannelEntry": h3cFlex10RemoteSchannelEntry,
       "h3cFlex10RemSchDesFormat": h3cFlex10RemSchDesFormat,
       "h3cFlex10RemSchTerminationType": h3cFlex10RemSchTerminationType,
       "h3cFlex10RemSchTerminationCap": h3cFlex10RemSchTerminationCap,
       "h3cFlex10RemSchTrafficClass": h3cFlex10RemSchTrafficClass,
       "h3cFlex10RemSchCir": h3cFlex10RemSchCir,
       "h3cFlex10RemSchPir": h3cFlex10RemSchPir,
       "h3cFlex10RemSchConnectionID": h3cFlex10RemSchConnectionID,
       "h3cFlex10SchannelLinkCtlTable": h3cFlex10SchannelLinkCtlTable,
       "h3cFlex10SchannelLinkCtlEntry": h3cFlex10SchannelLinkCtlEntry,
       "h3cFlex10SchannelSVID": h3cFlex10SchannelSVID,
       "h3cFlex10SchannelLocalStatus": h3cFlex10SchannelLocalStatus,
       "h3cFlex10SchannelRemoteStatus": h3cFlex10SchannelRemoteStatus}
)
