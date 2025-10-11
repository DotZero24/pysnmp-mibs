# SNMP MIB module (INFINERA-ENTITY-FMPO50-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-FMPO50-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:26 2025
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

(entLPPhysicalIndex,) = mibBuilder.importSymbols(
    "ENTITY-MIB",
    "entLPPhysicalIndex")

(equipment,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "equipment")

(InfnEqptType,) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnEqptType")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

fmpo50MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fmpo50Table_Object = MibTable
fmpo50Table = _Fmpo50Table_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 1)
)
if mibBuilder.loadTexts:
    fmpo50Table.setStatus("current")
_Fmpo50Entry_Object = MibTableRow
fmpo50Entry = _Fmpo50Entry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 1, 1)
)
fmpo50Entry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fmpo50Entry.setStatus("current")
_Fmpo50MoId_Type = DisplayString
_Fmpo50MoId_Object = MibTableColumn
fmpo50MoId = _Fmpo50MoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 1, 1, 1),
    _Fmpo50MoId_Type()
)
fmpo50MoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fmpo50MoId.setStatus("current")
_Fmpo50ProvEqptType_Type = InfnEqptType
_Fmpo50ProvEqptType_Object = MibTableColumn
fmpo50ProvEqptType = _Fmpo50ProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 1, 1, 2),
    _Fmpo50ProvEqptType_Type()
)
fmpo50ProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fmpo50ProvEqptType.setStatus("current")
_Fmpo50ProvSerialNumber_Type = DisplayString
_Fmpo50ProvSerialNumber_Object = MibTableColumn
fmpo50ProvSerialNumber = _Fmpo50ProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 1, 1, 3),
    _Fmpo50ProvSerialNumber_Type()
)
fmpo50ProvSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmpo50ProvSerialNumber.setStatus("current")
_Fmpo50Conformance_ObjectIdentity = ObjectIdentity
fmpo50Conformance = _Fmpo50Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 3)
)
_Fmpo50Compliances_ObjectIdentity = ObjectIdentity
fmpo50Compliances = _Fmpo50Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 3, 1)
)
_Fmpo50Groups_ObjectIdentity = ObjectIdentity
fmpo50Groups = _Fmpo50Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 3, 2)
)

# Managed Objects groups

fmpo50Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 3, 2, 1)
)
fmpo50Group.setObjects(
      *(("INFINERA-ENTITY-FMPO50-MIB", "fmpo50MoId"),
        ("INFINERA-ENTITY-FMPO50-MIB", "fmpo50ProvEqptType"),
        ("INFINERA-ENTITY-FMPO50-MIB", "fmpo50ProvSerialNumber"))
)
if mibBuilder.loadTexts:
    fmpo50Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmpo50Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 52, 3, 1, 1)
)
fmpo50Compliance.setObjects(
    ("INFINERA-ENTITY-FMPO50-MIB", "fmpo50Group")
)
if mibBuilder.loadTexts:
    fmpo50Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-FMPO50-MIB",
    **{"fmpo50MIB": fmpo50MIB,
       "fmpo50Table": fmpo50Table,
       "fmpo50Entry": fmpo50Entry,
       "fmpo50MoId": fmpo50MoId,
       "fmpo50ProvEqptType": fmpo50ProvEqptType,
       "fmpo50ProvSerialNumber": fmpo50ProvSerialNumber,
       "fmpo50Conformance": fmpo50Conformance,
       "fmpo50Compliances": fmpo50Compliances,
       "fmpo50Compliance": fmpo50Compliance,
       "fmpo50Groups": fmpo50Groups,
       "fmpo50Group": fmpo50Group}
)
