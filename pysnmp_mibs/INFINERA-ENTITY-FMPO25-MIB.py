# SNMP MIB module (INFINERA-ENTITY-FMPO25-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-FMPO25-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:44 2025
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

fmpo25MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Fmpo25Table_Object = MibTable
fmpo25Table = _Fmpo25Table_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 1)
)
if mibBuilder.loadTexts:
    fmpo25Table.setStatus("current")
_Fmpo25Entry_Object = MibTableRow
fmpo25Entry = _Fmpo25Entry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 1, 1)
)
fmpo25Entry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    fmpo25Entry.setStatus("current")
_Fmpo25MoId_Type = DisplayString
_Fmpo25MoId_Object = MibTableColumn
fmpo25MoId = _Fmpo25MoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 1, 1, 1),
    _Fmpo25MoId_Type()
)
fmpo25MoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fmpo25MoId.setStatus("current")
_Fmpo25ProvEqptType_Type = InfnEqptType
_Fmpo25ProvEqptType_Object = MibTableColumn
fmpo25ProvEqptType = _Fmpo25ProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 1, 1, 2),
    _Fmpo25ProvEqptType_Type()
)
fmpo25ProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    fmpo25ProvEqptType.setStatus("current")
_Fmpo25ProvSerialNumber_Type = DisplayString
_Fmpo25ProvSerialNumber_Object = MibTableColumn
fmpo25ProvSerialNumber = _Fmpo25ProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 1, 1, 3),
    _Fmpo25ProvSerialNumber_Type()
)
fmpo25ProvSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmpo25ProvSerialNumber.setStatus("current")
_Fmpo25Conformance_ObjectIdentity = ObjectIdentity
fmpo25Conformance = _Fmpo25Conformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 3)
)
_Fmpo25Compliances_ObjectIdentity = ObjectIdentity
fmpo25Compliances = _Fmpo25Compliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 3, 1)
)
_Fmpo25Groups_ObjectIdentity = ObjectIdentity
fmpo25Groups = _Fmpo25Groups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 3, 2)
)

# Managed Objects groups

fmpo25Group = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 3, 2, 1)
)
fmpo25Group.setObjects(
      *(("INFINERA-ENTITY-FMPO25-MIB", "fmpo25MoId"),
        ("INFINERA-ENTITY-FMPO25-MIB", "fmpo25ProvEqptType"),
        ("INFINERA-ENTITY-FMPO25-MIB", "fmpo25ProvSerialNumber"))
)
if mibBuilder.loadTexts:
    fmpo25Group.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmpo25Compliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 51, 3, 1, 1)
)
fmpo25Compliance.setObjects(
    ("INFINERA-ENTITY-FMPO25-MIB", "fmpo25Group")
)
if mibBuilder.loadTexts:
    fmpo25Compliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-FMPO25-MIB",
    **{"fmpo25MIB": fmpo25MIB,
       "fmpo25Table": fmpo25Table,
       "fmpo25Entry": fmpo25Entry,
       "fmpo25MoId": fmpo25MoId,
       "fmpo25ProvEqptType": fmpo25ProvEqptType,
       "fmpo25ProvSerialNumber": fmpo25ProvSerialNumber,
       "fmpo25Conformance": fmpo25Conformance,
       "fmpo25Compliances": fmpo25Compliances,
       "fmpo25Compliance": fmpo25Compliance,
       "fmpo25Groups": fmpo25Groups,
       "fmpo25Group": fmpo25Group}
)
