# SNMP MIB module (AUTOMATION-TC) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/AUTOMATION-TC
# Produced by pysmi-1.6.2 at Fri Oct 10 20:06:47 2025
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

(automationModules,) = mibBuilder.importSymbols(
    "AUTOMATION-SMI",
    "automationModules")

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

automationTcModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 2, 1)
)
if mibBuilder.loadTexts:
    automationTcModule.setRevisions(
        ("2013-06-30 00:00",
         "2012-09-19 00:00",
         "2012-07-27 00:00",
         "2008-11-10 00:00",
         "2008-04-29 00:00",
         "2005-01-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



class AutomationOrderNumberTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(16, 32),
    )



class AutomationSerialNumberTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32



class AutomationVersionNumberTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(0, 32),
    )



class AutomationMacAddressTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1x:"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(6, 6),
    )
    fixed_length = 6



class AutomationIpAddressTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "1a"


class AutomationStatusTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(0,
              1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("invalid", 0),
          ("enable", 1),
          ("disable", 2))
    )



class AutomationTriggerTC(TextualConvention, Integer32):
    status = "current"
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2)
        )
    )
    namedValues = NamedValues(
        *(("trigger", 1),
          ("notTriggered", 2))
    )



class AutomationFunctionStringTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "32a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(32, 32),
    )
    fixed_length = 32



class AutomationLocationStringTC(TextualConvention, OctetString):
    status = "current"
    displayHint = "22a"
    subtypeSpec = OctetString.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        ValueSizeConstraint(22, 22),
    )
    fixed_length = 22



# MIB Managed Objects in the order of their OIDs


# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AUTOMATION-TC",
    **{"AutomationOrderNumberTC": AutomationOrderNumberTC,
       "AutomationSerialNumberTC": AutomationSerialNumberTC,
       "AutomationVersionNumberTC": AutomationVersionNumberTC,
       "AutomationMacAddressTC": AutomationMacAddressTC,
       "AutomationIpAddressTC": AutomationIpAddressTC,
       "AutomationStatusTC": AutomationStatusTC,
       "AutomationTriggerTC": AutomationTriggerTC,
       "AutomationFunctionStringTC": AutomationFunctionStringTC,
       "AutomationLocationStringTC": AutomationLocationStringTC,
       "automationTcModule": automationTcModule}
)
