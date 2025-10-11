# SNMP MIB module (SONICWALL-COMMON-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/sonicwall/SONICWALL-COMMON-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:48:37 2025
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
 PhysAddress,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")

(sonicwallCommon,) = mibBuilder.importSymbols(
    "SONICWALL-SMI",
    "sonicwallCommon")


# MODULE-IDENTITY

snwlCommonModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 2, 1)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_SnwlSys_ObjectIdentity = ObjectIdentity
snwlSys = _SnwlSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 8741, 2, 1, 1)
)
_SnwlSysModel_Type = DisplayString
_SnwlSysModel_Object = MibScalar
snwlSysModel = _SnwlSysModel_Object(
    (1, 3, 6, 1, 4, 1, 8741, 2, 1, 1, 1),
    _SnwlSysModel_Type()
)
snwlSysModel.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snwlSysModel.setStatus("current")
_SnwlSysSerialNumber_Type = DisplayString
_SnwlSysSerialNumber_Object = MibScalar
snwlSysSerialNumber = _SnwlSysSerialNumber_Object(
    (1, 3, 6, 1, 4, 1, 8741, 2, 1, 1, 2),
    _SnwlSysSerialNumber_Type()
)
snwlSysSerialNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snwlSysSerialNumber.setStatus("current")
_SnwlSysFirmwareVersion_Type = DisplayString
_SnwlSysFirmwareVersion_Object = MibScalar
snwlSysFirmwareVersion = _SnwlSysFirmwareVersion_Object(
    (1, 3, 6, 1, 4, 1, 8741, 2, 1, 1, 3),
    _SnwlSysFirmwareVersion_Type()
)
snwlSysFirmwareVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snwlSysFirmwareVersion.setStatus("current")
_SnwlSysROMVersion_Type = DisplayString
_SnwlSysROMVersion_Object = MibScalar
snwlSysROMVersion = _SnwlSysROMVersion_Object(
    (1, 3, 6, 1, 4, 1, 8741, 2, 1, 1, 4),
    _SnwlSysROMVersion_Type()
)
snwlSysROMVersion.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snwlSysROMVersion.setStatus("current")
_SnwlSysAssetNumber_Type = DisplayString
_SnwlSysAssetNumber_Object = MibScalar
snwlSysAssetNumber = _SnwlSysAssetNumber_Object(
    (1, 3, 6, 1, 4, 1, 8741, 2, 1, 1, 5),
    _SnwlSysAssetNumber_Type()
)
snwlSysAssetNumber.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    snwlSysAssetNumber.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "SONICWALL-COMMON-MIB",
    **{"snwlCommonModule": snwlCommonModule,
       "snwlSys": snwlSys,
       "snwlSysModel": snwlSysModel,
       "snwlSysSerialNumber": snwlSysSerialNumber,
       "snwlSysFirmwareVersion": snwlSysFirmwareVersion,
       "snwlSysROMVersion": snwlSysROMVersion,
       "snwlSysAssetNumber": snwlSysAssetNumber}
)
