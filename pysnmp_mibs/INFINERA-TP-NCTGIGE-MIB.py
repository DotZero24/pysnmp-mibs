# SNMP MIB module (INFINERA-TP-NCTGIGE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-NCTGIGE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:52 2025
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

(ifIndex,) = mibBuilder.importSymbols(
    "IF-MIB",
    "ifIndex")

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatTenths,
 InfnChassisType,
 InfnNctType) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatTenths",
    "InfnChassisType",
    "InfnNctType")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nctGigEMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12)
)
if mibBuilder.loadTexts:
    nctGigEMIB.setRevisions(
        ("2008-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_NctGigETable_Object = MibTable
nctGigETable = _NctGigETable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 1)
)
if mibBuilder.loadTexts:
    nctGigETable.setStatus("current")
_NctGigEEntry_Object = MibTableRow
nctGigEEntry = _NctGigEEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 1, 1)
)
nctGigEEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    nctGigEEntry.setStatus("current")


class _NctGigEPortType_Type(Integer32):
    """Custom type nctGigEPortType based on Integer32"""
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
        *(("none", 1),
          ("nct", 2),
          ("gige", 3))
    )


_NctGigEPortType_Type.__name__ = "Integer32"
_NctGigEPortType_Object = MibTableColumn
nctGigEPortType = _NctGigEPortType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 1, 1, 1),
    _NctGigEPortType_Type()
)
nctGigEPortType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nctGigEPortType.setStatus("current")


class _NctGigEForwardingState_Type(Integer32):
    """Custom type nctGigEForwardingState based on Integer32"""
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
        *(("disabled", 1),
          ("enabled", 2),
          ("unknown", 3))
    )


_NctGigEForwardingState_Type.__name__ = "Integer32"
_NctGigEForwardingState_Object = MibTableColumn
nctGigEForwardingState = _NctGigEForwardingState_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 1, 1, 2),
    _NctGigEForwardingState_Type()
)
nctGigEForwardingState.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nctGigEForwardingState.setStatus("current")


class _NctGigEPeerPortId_Type(Integer32):
    """Custom type nctGigEPeerPortId based on Integer32"""
    defaultValue = 1

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
          ("nct1", 2),
          ("nct2", 3),
          ("gige", 4))
    )


_NctGigEPeerPortId_Type.__name__ = "Integer32"
_NctGigEPeerPortId_Object = MibTableColumn
nctGigEPeerPortId = _NctGigEPeerPortId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 1, 1, 3),
    _NctGigEPeerPortId_Type()
)
nctGigEPeerPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nctGigEPeerPortId.setStatus("current")
_NctGigEPeerChassisSerNum_Type = DisplayString
_NctGigEPeerChassisSerNum_Object = MibTableColumn
nctGigEPeerChassisSerNum = _NctGigEPeerChassisSerNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 1, 1, 4),
    _NctGigEPeerChassisSerNum_Type()
)
nctGigEPeerChassisSerNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nctGigEPeerChassisSerNum.setStatus("current")
_NctGigEPeerChassisId_Type = DisplayString
_NctGigEPeerChassisId_Object = MibTableColumn
nctGigEPeerChassisId = _NctGigEPeerChassisId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 1, 1, 5),
    _NctGigEPeerChassisId_Type()
)
nctGigEPeerChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nctGigEPeerChassisId.setStatus("current")


class _NctGigEPeerMcmSlotNum_Type(Integer32):
    """Custom type nctGigEPeerMcmSlotNum based on Integer32"""
    defaultValue = 0


_NctGigEPeerMcmSlotNum_Type.__name__ = "Integer32"
_NctGigEPeerMcmSlotNum_Object = MibTableColumn
nctGigEPeerMcmSlotNum = _NctGigEPeerMcmSlotNum_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 1, 1, 6),
    _NctGigEPeerMcmSlotNum_Type()
)
nctGigEPeerMcmSlotNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nctGigEPeerMcmSlotNum.setStatus("current")


class _NctGigEPeerChassisType_Type(InfnChassisType):
    """Custom type nctGigEPeerChassisType based on InfnChassisType"""
    defaultValue = 1


_NctGigEPeerChassisType_Type.__name__ = "InfnChassisType"
_NctGigEPeerChassisType_Object = MibTableColumn
nctGigEPeerChassisType = _NctGigEPeerChassisType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 1, 1, 7),
    _NctGigEPeerChassisType_Type()
)
nctGigEPeerChassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nctGigEPeerChassisType.setStatus("current")
_InterfaceTypeNCT_Type = InfnNctType
_InterfaceTypeNCT_Object = MibTableColumn
interfaceTypeNCT = _InterfaceTypeNCT_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 1, 1, 8),
    _InterfaceTypeNCT_Type()
)
interfaceTypeNCT.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    interfaceTypeNCT.setStatus("current")
_NctGigEConformance_ObjectIdentity = ObjectIdentity
nctGigEConformance = _NctGigEConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 3)
)
_NctGigECompliances_ObjectIdentity = ObjectIdentity
nctGigECompliances = _NctGigECompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 3, 1)
)
_NctGigEGroups_ObjectIdentity = ObjectIdentity
nctGigEGroups = _NctGigEGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 3, 2)
)

# Managed Objects groups

nctGigEGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 3, 2, 1)
)
nctGigEGroup.setObjects(
      *(("INFINERA-TP-NCTGIGE-MIB", "nctGigEPortType"),
        ("INFINERA-TP-NCTGIGE-MIB", "nctGigEForwardingState"),
        ("INFINERA-TP-NCTGIGE-MIB", "nctGigEPeerPortId"),
        ("INFINERA-TP-NCTGIGE-MIB", "nctGigEPeerChassisSerNum"),
        ("INFINERA-TP-NCTGIGE-MIB", "nctGigEPeerChassisId"),
        ("INFINERA-TP-NCTGIGE-MIB", "nctGigEPeerMcmSlotNum"),
        ("INFINERA-TP-NCTGIGE-MIB", "nctGigEPeerChassisType"),
        ("INFINERA-TP-NCTGIGE-MIB", "interfaceTypeNCT"))
)
if mibBuilder.loadTexts:
    nctGigEGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

nctGigECompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 12, 3, 1, 1)
)
nctGigECompliance.setObjects(
    ("INFINERA-TP-NCTGIGE-MIB", "nctGigEGroup")
)
if mibBuilder.loadTexts:
    nctGigECompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-NCTGIGE-MIB",
    **{"nctGigEMIB": nctGigEMIB,
       "nctGigETable": nctGigETable,
       "nctGigEEntry": nctGigEEntry,
       "nctGigEPortType": nctGigEPortType,
       "nctGigEForwardingState": nctGigEForwardingState,
       "nctGigEPeerPortId": nctGigEPeerPortId,
       "nctGigEPeerChassisSerNum": nctGigEPeerChassisSerNum,
       "nctGigEPeerChassisId": nctGigEPeerChassisId,
       "nctGigEPeerMcmSlotNum": nctGigEPeerMcmSlotNum,
       "nctGigEPeerChassisType": nctGigEPeerChassisType,
       "interfaceTypeNCT": interfaceTypeNCT,
       "nctGigEConformance": nctGigEConformance,
       "nctGigECompliances": nctGigECompliances,
       "nctGigECompliance": nctGigECompliance,
       "nctGigEGroups": nctGigEGroups,
       "nctGigEGroup": nctGigEGroup}
)
