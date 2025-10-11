# SNMP MIB module (AUTOMATION-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/siemens/AUTOMATION-SMI
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

(siemens,) = mibBuilder.importSymbols(
    "SIEMENS-SMI",
    "siemens")

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

automation = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6)
)
if mibBuilder.loadTexts:
    automation.setRevisions(
        ("2013-06-25 00:00",
         "2012-07-27 00:00",
         "2008-11-10 00:00",
         "2008-06-02 00:00",
         "2008-04-29 00:00",
         "2005-01-12 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_AutomationProducts_ObjectIdentity = ObjectIdentity
automationProducts = _AutomationProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 1)
)
if mibBuilder.loadTexts:
    automationProducts.setStatus("current")
_AutomationPlc_ObjectIdentity = ObjectIdentity
automationPlc = _AutomationPlc_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 1, 1)
)
if mibBuilder.loadTexts:
    automationPlc.setStatus("current")
_AutomationSimaticNet_ObjectIdentity = ObjectIdentity
automationSimaticNet = _AutomationSimaticNet_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 1, 2)
)
if mibBuilder.loadTexts:
    automationSimaticNet.setStatus("current")
_AutomationMotionControl_ObjectIdentity = ObjectIdentity
automationMotionControl = _AutomationMotionControl_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 1, 3)
)
if mibBuilder.loadTexts:
    automationMotionControl.setStatus("current")
_AutomationHmi_ObjectIdentity = ObjectIdentity
automationHmi = _AutomationHmi_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 1, 4)
)
if mibBuilder.loadTexts:
    automationHmi.setStatus("current")
_AutomationSitopPower_ObjectIdentity = ObjectIdentity
automationSitopPower = _AutomationSitopPower_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 1, 5)
)
if mibBuilder.loadTexts:
    automationSitopPower.setStatus("current")
_AutomationModules_ObjectIdentity = ObjectIdentity
automationModules = _AutomationModules_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 2)
)
if mibBuilder.loadTexts:
    automationModules.setStatus("current")
_AutomationMgmt_ObjectIdentity = ObjectIdentity
automationMgmt = _AutomationMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 3)
)
if mibBuilder.loadTexts:
    automationMgmt.setStatus("current")
_AutomationAgentCapability_ObjectIdentity = ObjectIdentity
automationAgentCapability = _AutomationAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 4)
)
if mibBuilder.loadTexts:
    automationAgentCapability.setStatus("current")
_AutomationPlcAgentCapability_ObjectIdentity = ObjectIdentity
automationPlcAgentCapability = _AutomationPlcAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 4, 1)
)
if mibBuilder.loadTexts:
    automationPlcAgentCapability.setStatus("current")
_AutomationSimaticNetAgentCapability_ObjectIdentity = ObjectIdentity
automationSimaticNetAgentCapability = _AutomationSimaticNetAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 4, 2)
)
if mibBuilder.loadTexts:
    automationSimaticNetAgentCapability.setStatus("current")
_AutomationMotionControlAgentCapability_ObjectIdentity = ObjectIdentity
automationMotionControlAgentCapability = _AutomationMotionControlAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 4, 3)
)
if mibBuilder.loadTexts:
    automationMotionControlAgentCapability.setStatus("current")
_AutomationHmiAgentCapability_ObjectIdentity = ObjectIdentity
automationHmiAgentCapability = _AutomationHmiAgentCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 4, 4)
)
if mibBuilder.loadTexts:
    automationHmiAgentCapability.setStatus("current")
_AutomationSitopPowerCapability_ObjectIdentity = ObjectIdentity
automationSitopPowerCapability = _AutomationSitopPowerCapability_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 4329, 6, 4, 5)
)
if mibBuilder.loadTexts:
    automationSitopPowerCapability.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "AUTOMATION-SMI",
    **{"automation": automation,
       "automationProducts": automationProducts,
       "automationPlc": automationPlc,
       "automationSimaticNet": automationSimaticNet,
       "automationMotionControl": automationMotionControl,
       "automationHmi": automationHmi,
       "automationSitopPower": automationSitopPower,
       "automationModules": automationModules,
       "automationMgmt": automationMgmt,
       "automationAgentCapability": automationAgentCapability,
       "automationPlcAgentCapability": automationPlcAgentCapability,
       "automationSimaticNetAgentCapability": automationSimaticNetAgentCapability,
       "automationMotionControlAgentCapability": automationMotionControlAgentCapability,
       "automationHmiAgentCapability": automationHmiAgentCapability,
       "automationSitopPowerCapability": automationSitopPowerCapability}
)
