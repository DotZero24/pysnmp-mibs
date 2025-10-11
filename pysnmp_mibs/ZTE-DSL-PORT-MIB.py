# SNMP MIB module (ZTE-DSL-PORT-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/zte/ZTE-DSL-PORT-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:44:56 2025
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

(SnmpAdminString,) = mibBuilder.importSymbols(
    "SNMP-FRAMEWORK-MIB",
    "SnmpAdminString")

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
 RowStatus,
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

zxDslPortMib = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 43)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_Zte_ObjectIdentity = ObjectIdentity
zte = _Zte_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902)
)
_ZxDsl_ObjectIdentity = ObjectIdentity
zxDsl = _ZxDsl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004)
)
_ZxDslPortMibObjects_ObjectIdentity = ObjectIdentity
zxDslPortMibObjects = _ZxDslPortMibObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1)
)
_ZxDslPortObjects_ObjectIdentity = ObjectIdentity
zxDslPortObjects = _ZxDslPortObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1, 1)
)
_ZxDslPortTable_Object = MibTable
zxDslPortTable = _ZxDslPortTable_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1, 1, 10)
)
if mibBuilder.loadTexts:
    zxDslPortTable.setStatus("current")
_ZxDslPortEntry_Object = MibTableRow
zxDslPortEntry = _ZxDslPortEntry_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1, 1, 10, 1)
)
zxDslPortEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    zxDslPortEntry.setStatus("current")


class _ZxDslPortLockStatus_Type(Integer32):
    """Custom type zxDslPortLockStatus based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("unlock", 1),
          ("lock", 2))
    )


_ZxDslPortLockStatus_Type.__name__ = "Integer32"
_ZxDslPortLockStatus_Object = MibTableColumn
zxDslPortLockStatus = _ZxDslPortLockStatus_Object(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1, 1, 10, 1, 1),
    _ZxDslPortLockStatus_Type()
)
zxDslPortLockStatus.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    zxDslPortLockStatus.setStatus("current")
_ZxDslPortTrapObjects_ObjectIdentity = ObjectIdentity
zxDslPortTrapObjects = _ZxDslPortTrapObjects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 3902, 1004, 43, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ZTE-DSL-PORT-MIB",
    **{"zte": zte,
       "zxDsl": zxDsl,
       "zxDslPortMib": zxDslPortMib,
       "zxDslPortMibObjects": zxDslPortMibObjects,
       "zxDslPortObjects": zxDslPortObjects,
       "zxDslPortTable": zxDslPortTable,
       "zxDslPortEntry": zxDslPortEntry,
       "zxDslPortLockStatus": zxDslPortLockStatus,
       "zxDslPortTrapObjects": zxDslPortTrapObjects}
)
