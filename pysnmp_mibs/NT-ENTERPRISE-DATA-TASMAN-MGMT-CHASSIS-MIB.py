# SNMP MIB module (NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:20:06 2025
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

(ntEnterpriseDataTasmanMgmt,) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanMgmt")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

nnchassisMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2)
)
if mibBuilder.loadTexts:
    nnchassisMib.setRevisions(
        ("1999-07-01 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _NnchassisType_Type(DisplayString):
    """Custom type nnchassisType based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )


_NnchassisType_Type.__name__ = "DisplayString"
_NnchassisType_Object = MibScalar
nnchassisType = _NnchassisType_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 1),
    _NnchassisType_Type()
)
nnchassisType.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisType.setStatus("current")


class _NnchassisSerialNumber_Type(DisplayString):
    """Custom type nnchassisSerialNumber based on DisplayString"""
    subtypeSpec = DisplayString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 30),
    )


_NnchassisSerialNumber_Type.__name__ = "DisplayString"
_NnchassisSerialNumber_Object = MibScalar
nnchassisSerialNumber = _NnchassisSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 1, 2, 2),
    _NnchassisSerialNumber_Type()
)
nnchassisSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    nnchassisSerialNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "NT-ENTERPRISE-DATA-TASMAN-MGMT-CHASSIS-MIB",
    **{"nnchassisMib": nnchassisMib,
       "nnchassisType": nnchassisType,
       "nnchassisSerialNumber": nnchassisSerialNumber}
)
