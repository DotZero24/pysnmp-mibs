# SNMP MIB module (DSX-TC-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nortel/DSX-TC-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:21:02 2025
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

(ntEnterpriseDataTasmanInterfaces,
 ntEnterpriseDataTasmanMgmt,
 ntEnterpriseDataTasmanModules) = mibBuilder.importSymbols(
    "NT-ENTERPRISE-DATA-MIB",
    "ntEnterpriseDataTasmanInterfaces",
    "ntEnterpriseDataTasmanMgmt",
    "ntEnterpriseDataTasmanModules")

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

nndsxTC = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 3, 2)
)
if mibBuilder.loadTexts:
    nndsxTC.setRevisions(
        ("1999-04-23 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AlarmStatus(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1)
        )
    )
    namedValues = NamedValues(
        *(("off", 0),
          ("on", 1))
    )



class LEDState(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4,
              5,
              6,
              7)
        )
    )
    namedValues = NamedValues(
        *(("led-off", 1),
          ("led-green", 2),
          ("led-red", 3),
          ("led-yellow", 4),
          ("led-blinking-green", 5),
          ("led-blinking-red", 6),
          ("led-blinking-yellow", 7))
    )



# MIB Managed Objects in the order of their OIDs

_NndsxMIB_ObjectIdentity = ObjectIdentity
nndsxMIB = _NndsxMIB_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1)
)
_NndsxT1E1IfGroup_ObjectIdentity = ObjectIdentity
nndsxT1E1IfGroup = _NndsxT1E1IfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 2)
)
_NndsxT3E3IfGroup_ObjectIdentity = ObjectIdentity
nndsxT3E3IfGroup = _NndsxT3E3IfGroup_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 562, 73, 1, 1, 2, 1, 3)
)

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "DSX-TC-MIB",
    **{"AlarmStatus": AlarmStatus,
       "LEDState": LEDState,
       "nndsxMIB": nndsxMIB,
       "nndsxT1E1IfGroup": nndsxT1E1IfGroup,
       "nndsxT3E3IfGroup": nndsxT3E3IfGroup,
       "nndsxTC": nndsxTC}
)
