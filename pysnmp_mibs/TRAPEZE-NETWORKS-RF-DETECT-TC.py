# SNMP MIB module (TRAPEZE-NETWORKS-RF-DETECT-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/trapeze/TRAPEZE-NETWORKS-RF-DETECT-TC
# Produced by pysmi-1.6.2 at Fri Oct 10 22:05:16 2025
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

(trpzMibs,) = mibBuilder.importSymbols(
    "TRAPEZE-NETWORKS-ROOT-MIB",
    "trpzMibs")


# MODULE-IDENTITY

trpzRFDetectTc = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 14525, 4, 11)
)
if mibBuilder.loadTexts:
    trpzRFDetectTc.setRevisions(
        ("2011-07-27 00:11",
         "2009-08-13 00:10",
         "2007-04-18 00:02",
         "2007-03-28 00:01")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class TrpzRFDetectClassificationReason(TextualConvention, Integer32):
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
              7,
              8,
              9,
              10,
              11)
        )
    )
    namedValues = NamedValues(
        *(("other", 1),
          ("default-classification", 2),
          ("rogue-list", 3),
          ("ap-in-modo", 4),
          ("neighbor-list", 5),
          ("ssid-masquerade", 6),
          ("seen-in-network", 7),
          ("ad-hoc", 8),
          ("ssid-list", 9),
          ("pass-fingerprint", 10),
          ("fail-fingerprint", 11))
    )



class TrpzRFDetectClassification(TextualConvention, Integer32):
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
        *(("other", 1),
          ("not-classified", 2),
          ("member", 3),
          ("neighbor", 4),
          ("suspect", 5),
          ("rogue", 6),
          ("tag", 7))
    )



class TrpzRFDetectNetworkingMode(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("ad-hoc", 1),
          ("infrastructure", 2))
    )



class TrpzRFDetectDot11ModulationStandard(TextualConvention, Integer32):
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
        *(("dot11Unknown", 1),
          ("dot11Other", 2),
          ("dot11A", 3),
          ("dot11B", 4),
          ("dot11G", 5),
          ("dot11NA", 6),
          ("dot11NG", 7))
    )



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TRAPEZE-NETWORKS-RF-DETECT-TC",
    **{"TrpzRFDetectClassificationReason": TrpzRFDetectClassificationReason,
       "TrpzRFDetectClassification": TrpzRFDetectClassification,
       "TrpzRFDetectNetworkingMode": TrpzRFDetectNetworkingMode,
       "TrpzRFDetectDot11ModulationStandard": TrpzRFDetectDot11ModulationStandard,
       "trpzRFDetectTc": trpzRFDetectTc}
)
