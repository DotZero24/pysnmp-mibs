# SNMP MIB module (INFINERA-TP-PASSIVE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-PASSIVE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:29 2025
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

(commonTerminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "commonTerminationPoint")

(FloatHundredths,
 InfnEnableDisable) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnEnableDisable")

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

passivePtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2)
)
if mibBuilder.loadTexts:
    passivePtpMIB.setRevisions(
        ("2017-01-08 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_PassivePtpTable_Object = MibTable
passivePtpTable = _PassivePtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 1)
)
if mibBuilder.loadTexts:
    passivePtpTable.setStatus("current")
_PassivePtpEntry_Object = MibTableRow
passivePtpEntry = _PassivePtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 1, 1)
)
passivePtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    passivePtpEntry.setStatus("current")
_PassiveMoId_Type = DisplayString
_PassiveMoId_Object = MibTableColumn
passiveMoId = _PassiveMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 1, 1, 1),
    _PassiveMoId_Type()
)
passiveMoId.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passiveMoId.setStatus("current")
_PassivePtpType_Type = DisplayString
_PassivePtpType_Object = MibTableColumn
passivePtpType = _PassivePtpType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 1, 1, 2),
    _PassivePtpType_Type()
)
passivePtpType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    passivePtpType.setStatus("current")
_PassivePtpProvNbrTP_Type = DisplayString
_PassivePtpProvNbrTP_Object = MibTableColumn
passivePtpProvNbrTP = _PassivePtpProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 1, 1, 3),
    _PassivePtpProvNbrTP_Type()
)
passivePtpProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    passivePtpProvNbrTP.setStatus("current")
_PassivePtpConformance_ObjectIdentity = ObjectIdentity
passivePtpConformance = _PassivePtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 3)
)
_PassivePtpCompliances_ObjectIdentity = ObjectIdentity
passivePtpCompliances = _PassivePtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 3, 1)
)
_PassivePtpGroups_ObjectIdentity = ObjectIdentity
passivePtpGroups = _PassivePtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 3, 2)
)

# Managed Objects groups

passivePtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 3, 2, 1)
)
passivePtpGroup.setObjects(
      *(("INFINERA-TP-PASSIVE-MIB", "passiveMoId"),
        ("INFINERA-TP-PASSIVE-MIB", "passivePtpType"),
        ("INFINERA-TP-PASSIVE-MIB", "passivePtpProvNbrTP"))
)
if mibBuilder.loadTexts:
    passivePtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

passivePtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 1, 10, 2, 3, 1, 1)
)
passivePtpCompliance.setObjects(
    ("INFINERA-TP-PASSIVE-MIB", "passivePtpGroup")
)
if mibBuilder.loadTexts:
    passivePtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-PASSIVE-MIB",
    **{"passivePtpMIB": passivePtpMIB,
       "passivePtpTable": passivePtpTable,
       "passivePtpEntry": passivePtpEntry,
       "passiveMoId": passiveMoId,
       "passivePtpType": passivePtpType,
       "passivePtpProvNbrTP": passivePtpProvNbrTP,
       "passivePtpConformance": passivePtpConformance,
       "passivePtpCompliances": passivePtpCompliances,
       "passivePtpCompliance": passivePtpCompliance,
       "passivePtpGroups": passivePtpGroups,
       "passivePtpGroup": passivePtpGroup}
)
