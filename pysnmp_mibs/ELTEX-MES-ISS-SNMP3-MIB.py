# SNMP MIB module (ELTEX-MES-ISS-SNMP3-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/eltex/ELTEX-MES-ISS-SNMP3-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:50:33 2025
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

(eltMesIss,) = mibBuilder.importSymbols(
    "ELTEX-MES-ISS-MIB",
    "eltMesIss")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

eltMesIssSnmp3MIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 19)
)
if mibBuilder.loadTexts:
    eltMesIssSnmp3MIB.setRevisions(
        ("2019-11-06 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_EltMesIssSnmp3Objects_ObjectIdentity = ObjectIdentity
eltMesIssSnmp3Objects = _EltMesIssSnmp3Objects_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 19, 1)
)
_EltMesIssSnmp3Globals_ObjectIdentity = ObjectIdentity
eltMesIssSnmp3Globals = _EltMesIssSnmp3Globals_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 19, 1, 1)
)


class _EltMesIssWarmStartTrapControl_Type(Integer32):
    """Custom type eltMesIssWarmStartTrapControl based on Integer32"""
    defaultValue = 1

    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("enabled", 1),
          ("disabled", 2))
    )


_EltMesIssWarmStartTrapControl_Type.__name__ = "Integer32"
_EltMesIssWarmStartTrapControl_Object = MibScalar
eltMesIssWarmStartTrapControl = _EltMesIssWarmStartTrapControl_Object(
    (1, 3, 6, 1, 4, 1, 35265, 1, 139, 19, 1, 1, 1),
    _EltMesIssWarmStartTrapControl_Type()
)
eltMesIssWarmStartTrapControl.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    eltMesIssWarmStartTrapControl.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ELTEX-MES-ISS-SNMP3-MIB",
    **{"eltMesIssSnmp3MIB": eltMesIssSnmp3MIB,
       "eltMesIssSnmp3Objects": eltMesIssSnmp3Objects,
       "eltMesIssSnmp3Globals": eltMesIssSnmp3Globals,
       "eltMesIssWarmStartTrapControl": eltMesIssWarmStartTrapControl}
)
