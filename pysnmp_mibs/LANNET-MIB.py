# SNMP MIB module (LANNET-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/radware/LANNET-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:15:12 2025
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

(DisplayString,
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Lannet_ObjectIdentity = ObjectIdentity
lannet = _Lannet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81)
)
_LntBoxIdent_ObjectIdentity = ObjectIdentity
lntBoxIdent = _LntBoxIdent_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 5)
)
_LntLanSwitch_ObjectIdentity = ObjectIdentity
lntLanSwitch = _LntLanSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19)
)
_VnsPacket_ObjectIdentity = ObjectIdentity
vnsPacket = _VnsPacket_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 81, 19, 7)
)
_VnsPacketTable_Object = MibTable
vnsPacketTable = _VnsPacketTable_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1)
)
if mibBuilder.loadTexts:
    vnsPacketTable.setStatus("mandatory")
_VnsPacketEntry_Object = MibTableRow
vnsPacketEntry = _VnsPacketEntry_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1)
)
vnsPacketEntry.setIndexNames(
    (0, "LANNET-MIB", "vnsPacketMACAddress"),
)
if mibBuilder.loadTexts:
    vnsPacketEntry.setStatus("mandatory")


class _VnsPacketMACAddress_Type(OctetString):
    """Custom type vnsPacketMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_VnsPacketMACAddress_Type.__name__ = "OctetString"
_VnsPacketMACAddress_Object = MibTableColumn
vnsPacketMACAddress = _VnsPacketMACAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 1),
    _VnsPacketMACAddress_Type()
)
vnsPacketMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketMACAddress.setStatus("mandatory")


class _VnsPacketProtocolTypeMask_Type(OctetString):
    """Custom type vnsPacketProtocolTypeMask based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(1, 1),
    )
    fixed_length = 1


_VnsPacketProtocolTypeMask_Type.__name__ = "OctetString"
_VnsPacketProtocolTypeMask_Object = MibTableColumn
vnsPacketProtocolTypeMask = _VnsPacketProtocolTypeMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 2),
    _VnsPacketProtocolTypeMask_Type()
)
vnsPacketProtocolTypeMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketProtocolTypeMask.setStatus("mandatory")
_VnsPacketIPAddress_Type = IpAddress
_VnsPacketIPAddress_Object = MibTableColumn
vnsPacketIPAddress = _VnsPacketIPAddress_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 3),
    _VnsPacketIPAddress_Type()
)
vnsPacketIPAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketIPAddress.setStatus("mandatory")
_VnsPacketIPNetMask_Type = IpAddress
_VnsPacketIPNetMask_Object = MibTableColumn
vnsPacketIPNetMask = _VnsPacketIPNetMask_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 4),
    _VnsPacketIPNetMask_Type()
)
vnsPacketIPNetMask.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketIPNetMask.setStatus("mandatory")


class _VnsPacketIPXnetwork_Type(OctetString):
    """Custom type vnsPacketIPXnetwork based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(4, 4),
    )
    fixed_length = 4


_VnsPacketIPXnetwork_Type.__name__ = "OctetString"
_VnsPacketIPXnetwork_Object = MibTableColumn
vnsPacketIPXnetwork = _VnsPacketIPXnetwork_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 5),
    _VnsPacketIPXnetwork_Type()
)
vnsPacketIPXnetwork.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketIPXnetwork.setStatus("mandatory")


class _VnsPacketStationType_Type(Integer32):
    """Custom type vnsPacketStationType based on Integer32"""
    defaultValue = 255

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("client", 2),
          ("server", 3),
          ("notSupported", 255))
    )


_VnsPacketStationType_Type.__name__ = "Integer32"
_VnsPacketStationType_Object = MibTableColumn
vnsPacketStationType = _VnsPacketStationType_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 6),
    _VnsPacketStationType_Type()
)
vnsPacketStationType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketStationType.setStatus("mandatory")


class _VnsPacketPortGroupId_Type(Integer32):
    """Custom type vnsPacketPortGroupId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VnsPacketPortGroupId_Type.__name__ = "Integer32"
_VnsPacketPortGroupId_Object = MibTableColumn
vnsPacketPortGroupId = _VnsPacketPortGroupId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 7),
    _VnsPacketPortGroupId_Type()
)
vnsPacketPortGroupId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketPortGroupId.setStatus("mandatory")


class _VnsPacketPortId_Type(Integer32):
    """Custom type vnsPacketPortId based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 255),
    )


_VnsPacketPortId_Type.__name__ = "Integer32"
_VnsPacketPortId_Object = MibTableColumn
vnsPacketPortId = _VnsPacketPortId_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 8),
    _VnsPacketPortId_Type()
)
vnsPacketPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketPortId.setStatus("mandatory")


class _VnsPacketBackbonePort_Type(Integer32):
    """Custom type vnsPacketBackbonePort based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              255)
        )
    )
    namedValues = NamedValues(
        *(("unknown", 1),
          ("backbone", 2),
          ("noBackbone", 3),
          ("notSupported", 255))
    )


_VnsPacketBackbonePort_Type.__name__ = "Integer32"
_VnsPacketBackbonePort_Object = MibTableColumn
vnsPacketBackbonePort = _VnsPacketBackbonePort_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 9),
    _VnsPacketBackbonePort_Type()
)
vnsPacketBackbonePort.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketBackbonePort.setStatus("mandatory")
_VnsPacketExpectedVLAN_Type = Integer32
_VnsPacketExpectedVLAN_Object = MibTableColumn
vnsPacketExpectedVLAN = _VnsPacketExpectedVLAN_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 10),
    _VnsPacketExpectedVLAN_Type()
)
vnsPacketExpectedVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketExpectedVLAN.setStatus("mandatory")
_VnsPacketDetectedVLAN_Type = Integer32
_VnsPacketDetectedVLAN_Object = MibTableColumn
vnsPacketDetectedVLAN = _VnsPacketDetectedVLAN_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 11),
    _VnsPacketDetectedVLAN_Type()
)
vnsPacketDetectedVLAN.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketDetectedVLAN.setStatus("mandatory")
_VnsPacketBoxAgentIP_Type = IpAddress
_VnsPacketBoxAgentIP_Object = MibTableColumn
vnsPacketBoxAgentIP = _VnsPacketBoxAgentIP_Object(
    (1, 3, 6, 1, 4, 1, 81, 19, 7, 1, 1, 12),
    _VnsPacketBoxAgentIP_Type()
)
vnsPacketBoxAgentIP.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    vnsPacketBoxAgentIP.setStatus("mandatory")

# Managed Objects groups


# Notification objects

lreVLANViolationTrap = NotificationType(
    (1, 3, 6, 1, 4, 1, 81, 17, 1, 5, 0, 26)
)
lreVLANViolationTrap.setObjects(
      *(("LANNET-MIB", "vnsPacketMACAddress"),
        ("LANNET-MIB", "vnsPacketProtocolTypeMask"),
        ("LANNET-MIB", "vnsPacketIPAddress"),
        ("LANNET-MIB", "vnsPacketIPNetMask"),
        ("LANNET-MIB", "vnsPacketIPXnetwork"),
        ("LANNET-MIB", "vnsPacketPortGroupId"),
        ("LANNET-MIB", "vnsPacketPortId"),
        ("LANNET-MIB", "vnsPacketBackbonePort"),
        ("LANNET-MIB", "vnsPacketExpectedVLAN"),
        ("LANNET-MIB", "vnsPacketDetectedVLAN"),
        ("LANNET-MIB", "vnsPacketBoxAgentIP"))
)
if mibBuilder.loadTexts:
    lreVLANViolationTrap.setStatus(
        ""
    )


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LANNET-MIB",
    **{"lannet": lannet,
       "lntBoxIdent": lntBoxIdent,
       "lreVLANViolationTrap": lreVLANViolationTrap,
       "lntLanSwitch": lntLanSwitch,
       "vnsPacket": vnsPacket,
       "vnsPacketTable": vnsPacketTable,
       "vnsPacketEntry": vnsPacketEntry,
       "vnsPacketMACAddress": vnsPacketMACAddress,
       "vnsPacketProtocolTypeMask": vnsPacketProtocolTypeMask,
       "vnsPacketIPAddress": vnsPacketIPAddress,
       "vnsPacketIPNetMask": vnsPacketIPNetMask,
       "vnsPacketIPXnetwork": vnsPacketIPXnetwork,
       "vnsPacketStationType": vnsPacketStationType,
       "vnsPacketPortGroupId": vnsPacketPortGroupId,
       "vnsPacketPortId": vnsPacketPortId,
       "vnsPacketBackbonePort": vnsPacketBackbonePort,
       "vnsPacketExpectedVLAN": vnsPacketExpectedVLAN,
       "vnsPacketDetectedVLAN": vnsPacketDetectedVLAN,
       "vnsPacketBoxAgentIP": vnsPacketBoxAgentIP}
)
