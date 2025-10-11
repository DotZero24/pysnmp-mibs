# SNMP MIB module (ARRIS-SIP-DOC30-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/arris/ARRIS-SIP-DOC30-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:10:03 2025
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

(arrisSipMib,) = mibBuilder.importSymbols(
    "ARRIS-SIP-MIB",
    "arrisSipMib")

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
 TextualConvention,
 TruthValue) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention",
    "TruthValue")


# MODULE-IDENTITY

sipCfgDoc30 = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4115, 11, 3)
)


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs



class _SipCfgDoc30FeatureSwitch_Type(Bits):
    """Custom type sipCfgDoc30FeatureSwitch based on Bits"""
    defaultHexValue = "00000000"

    namedValues = NamedValues(
        *(("removeMACfromUAHeader", 0),
          ("unused1", 1),
          ("unused2", 2),
          ("unused3", 3),
          ("unused4", 4),
          ("unused5", 5),
          ("unused6", 6),
          ("unused7", 7),
          ("unused8", 8),
          ("unused9", 9),
          ("unused10", 10),
          ("unused11", 11),
          ("unused12", 12),
          ("unused13", 13),
          ("unused14", 14),
          ("unused15", 15),
          ("unused16", 16),
          ("unused17", 17),
          ("unused18", 18),
          ("unused19", 19),
          ("unused20", 20),
          ("unused21", 21),
          ("unused22", 22),
          ("unused23", 23),
          ("unused24", 24),
          ("unused25", 25),
          ("unused26", 26),
          ("unused27", 27),
          ("unused28", 28),
          ("unused29", 29),
          ("unused30", 30),
          ("unused31", 31))
    )

_SipCfgDoc30FeatureSwitch_Type.__name__ = "Bits"
_SipCfgDoc30FeatureSwitch_Object = MibScalar
sipCfgDoc30FeatureSwitch = _SipCfgDoc30FeatureSwitch_Object(
    (1, 3, 6, 1, 4, 1, 4115, 11, 3, 1),
    _SipCfgDoc30FeatureSwitch_Type()
)
sipCfgDoc30FeatureSwitch.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    sipCfgDoc30FeatureSwitch.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "ARRIS-SIP-DOC30-MIB",
    **{"sipCfgDoc30": sipCfgDoc30,
       "sipCfgDoc30FeatureSwitch": sipCfgDoc30FeatureSwitch}
)
