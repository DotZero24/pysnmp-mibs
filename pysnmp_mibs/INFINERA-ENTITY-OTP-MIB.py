# SNMP MIB module (INFINERA-ENTITY-OTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-ENTITY-OTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:14:53 2025
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

otpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OtpTable_Object = MibTable
otpTable = _OtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39, 1)
)
if mibBuilder.loadTexts:
    otpTable.setStatus("current")
_OtpEntry_Object = MibTableRow
otpEntry = _OtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39, 1, 1)
)
otpEntry.setIndexNames(
    (0, "ENTITY-MIB", "entLPPhysicalIndex"),
)
if mibBuilder.loadTexts:
    otpEntry.setStatus("current")
_OtpMoId_Type = DisplayString
_OtpMoId_Object = MibTableColumn
otpMoId = _OtpMoId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39, 1, 1, 1),
    _OtpMoId_Type()
)
otpMoId.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    otpMoId.setStatus("current")
_OtpProvEqptType_Type = InfnEqptType
_OtpProvEqptType_Object = MibTableColumn
otpProvEqptType = _OtpProvEqptType_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39, 1, 1, 2),
    _OtpProvEqptType_Type()
)
otpProvEqptType.setMaxAccess("read-create")
if mibBuilder.loadTexts:
    otpProvEqptType.setStatus("current")
_OtpProvSerialNumber_Type = DisplayString
_OtpProvSerialNumber_Object = MibTableColumn
otpProvSerialNumber = _OtpProvSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39, 1, 1, 3),
    _OtpProvSerialNumber_Type()
)
otpProvSerialNumber.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    otpProvSerialNumber.setStatus("current")
_OtpConformance_ObjectIdentity = ObjectIdentity
otpConformance = _OtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39, 3)
)
_OtpCompliances_ObjectIdentity = ObjectIdentity
otpCompliances = _OtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39, 3, 1)
)
_OtpGroups_ObjectIdentity = ObjectIdentity
otpGroups = _OtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39, 3, 2)
)

# Managed Objects groups

otpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39, 3, 2, 1)
)
otpGroup.setObjects(
      *(("INFINERA-ENTITY-OTP-MIB", "otpMoId"),
        ("INFINERA-ENTITY-OTP-MIB", "otpProvEqptType"),
        ("INFINERA-ENTITY-OTP-MIB", "otpProvSerialNumber"))
)
if mibBuilder.loadTexts:
    otpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

otpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 1, 39, 3, 1, 1)
)
otpCompliance.setObjects(
    ("INFINERA-ENTITY-OTP-MIB", "otpGroup")
)
if mibBuilder.loadTexts:
    otpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-ENTITY-OTP-MIB",
    **{"otpMIB": otpMIB,
       "otpTable": otpTable,
       "otpEntry": otpEntry,
       "otpMoId": otpMoId,
       "otpProvEqptType": otpProvEqptType,
       "otpProvSerialNumber": otpProvSerialNumber,
       "otpConformance": otpConformance,
       "otpCompliances": otpCompliances,
       "otpCompliance": otpCompliance,
       "otpGroups": otpGroups,
       "otpGroup": otpGroup}
)
