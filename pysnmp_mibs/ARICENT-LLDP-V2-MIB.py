# SNMP MIB module (ARICENT-LLDP-V2-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/aricent/ARICENT-LLDP-V2-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 21:42:13 2025
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

(LldpPortNumber,
 lldpExtensions) = mibBuilder.importSymbols(
    "LLDP-MIB",
    "LldpPortNumber",
    "lldpExtensions")

(TimeFilter,) = mibBuilder.importSymbols(
    "RMON2-MIB",
    "TimeFilter")

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

fslldpV2MIB = ModuleIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001)
)
if mibBuilder.loadTexts:
    fslldpV2MIB.setRevisions(
        ("2012-09-05 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpV2Objects_ObjectIdentity = ObjectIdentity
lldpV2Objects = _LldpV2Objects_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001, 1)
)
_LldpV2Configuration_ObjectIdentity = ObjectIdentity
lldpV2Configuration = _LldpV2Configuration_ObjectIdentity(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001, 1, 1)
)
_LldpV2RemTimeMark_Type = TimeFilter
_LldpV2RemTimeMark_Object = MibScalar
lldpV2RemTimeMark = _LldpV2RemTimeMark_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001, 1, 1, 1),
    _LldpV2RemTimeMark_Type()
)
lldpV2RemTimeMark.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemTimeMark.setStatus("current")
_LldpV2RemLocalIfIndex_Type = LldpPortNumber
_LldpV2RemLocalIfIndex_Object = MibScalar
lldpV2RemLocalIfIndex = _LldpV2RemLocalIfIndex_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001, 1, 1, 2),
    _LldpV2RemLocalIfIndex_Type()
)
lldpV2RemLocalIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemLocalIfIndex.setStatus("current")
_LldpV2LocPortIfIndex_Type = LldpPortNumber
_LldpV2LocPortIfIndex_Object = MibScalar
lldpV2LocPortIfIndex = _LldpV2LocPortIfIndex_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001, 1, 1, 3),
    _LldpV2LocPortIfIndex_Type()
)
lldpV2LocPortIfIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2LocPortIfIndex.setStatus("current")


class _LldpV2RemIndex_Type(Integer32):
    """Custom type lldpV2RemIndex based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueRangeConstraint(1, 2147483647),
    )


_LldpV2RemIndex_Type.__name__ = "Integer32"
_LldpV2RemIndex_Object = MibScalar
lldpV2RemIndex = _LldpV2RemIndex_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001, 1, 1, 4),
    _LldpV2RemIndex_Type()
)
lldpV2RemIndex.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemIndex.setStatus("current")


class _LldpV2RemLocalDestMACAddress_Type(OctetString):
    """Custom type lldpV2RemLocalDestMACAddress based on OctetString"""
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6


_LldpV2RemLocalDestMACAddress_Type.__name__ = "OctetString"
_LldpV2RemLocalDestMACAddress_Object = MibScalar
lldpV2RemLocalDestMACAddress = _LldpV2RemLocalDestMACAddress_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001, 1, 1, 5),
    _LldpV2RemLocalDestMACAddress_Type()
)
lldpV2RemLocalDestMACAddress.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2RemLocalDestMACAddress.setStatus("current")
_LldpV2PortConfigTable_Object = MibTable
lldpV2PortConfigTable = _LldpV2PortConfigTable_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001, 1, 1, 6)
)
if mibBuilder.loadTexts:
    lldpV2PortConfigTable.setStatus("current")
_LldpV2PortConfigEntry_Object = MibTableRow
lldpV2PortConfigEntry = _LldpV2PortConfigEntry_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001, 1, 1, 6, 1)
)
lldpV2PortConfigEntry.setIndexNames(
    (0, "ARICENT-LLDP-V2-MIB", "lldpV2PortConfigPortNum"),
)
if mibBuilder.loadTexts:
    lldpV2PortConfigEntry.setStatus("current")
_LldpV2PortConfigPortNum_Type = LldpPortNumber
_LldpV2PortConfigPortNum_Object = MibTableColumn
lldpV2PortConfigPortNum = _LldpV2PortConfigPortNum_Object(
    (1, 0, 8802, 1, 1, 2, 1, 5, 40001, 1, 1, 6, 1, 1),
    _LldpV2PortConfigPortNum_Type()
)
lldpV2PortConfigPortNum.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpV2PortConfigPortNum.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARICENT-LLDP-V2-MIB",
    **{"fslldpV2MIB": fslldpV2MIB,
       "lldpV2Objects": lldpV2Objects,
       "lldpV2Configuration": lldpV2Configuration,
       "lldpV2RemTimeMark": lldpV2RemTimeMark,
       "lldpV2RemLocalIfIndex": lldpV2RemLocalIfIndex,
       "lldpV2LocPortIfIndex": lldpV2LocPortIfIndex,
       "lldpV2RemIndex": lldpV2RemIndex,
       "lldpV2RemLocalDestMACAddress": lldpV2RemLocalDestMACAddress,
       "lldpV2PortConfigTable": lldpV2PortConfigTable,
       "lldpV2PortConfigEntry": lldpV2PortConfigEntry,
       "lldpV2PortConfigPortNum": lldpV2PortConfigPortNum}
)
