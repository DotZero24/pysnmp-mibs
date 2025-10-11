# SNMP MIB module (HMIT-SMI) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hirschmann/HMIT-SMI
# Produced by pysmi-1.6.2 at Fri Oct 10 18:54:27 2025
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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

hirschmann = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 248)
)
if mibBuilder.loadTexts:
    hirschmann.setRevisions(
        ("2010-01-08 17:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_HmVendor_ObjectIdentity = ObjectIdentity
hmVendor = _HmVendor_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100)
)
if mibBuilder.loadTexts:
    hmVendor.setStatus("current")
_HmITSwitch_ObjectIdentity = ObjectIdentity
hmITSwitch = _HmITSwitch_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1)
)
if mibBuilder.loadTexts:
    hmITSwitch.setStatus("current")
_HmITProducts_ObjectIdentity = ObjectIdentity
hmITProducts = _HmITProducts_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 1)
)
if mibBuilder.loadTexts:
    hmITProducts.setStatus("current")
_HmITTrapObject_ObjectIdentity = ObjectIdentity
hmITTrapObject = _HmITTrapObject_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 2)
)
if mibBuilder.loadTexts:
    hmITTrapObject.setStatus("current")
_HmITMgmt_ObjectIdentity = ObjectIdentity
hmITMgmt = _HmITMgmt_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 3)
)
if mibBuilder.loadTexts:
    hmITMgmt.setStatus("current")
_HmITExperiment_ObjectIdentity = ObjectIdentity
hmITExperiment = _HmITExperiment_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 4)
)
if mibBuilder.loadTexts:
    hmITExperiment.setStatus("current")
_HmITSecurity_ObjectIdentity = ObjectIdentity
hmITSecurity = _HmITSecurity_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 5)
)
if mibBuilder.loadTexts:
    hmITSecurity.setStatus("current")
_HmITMgmt2_ObjectIdentity = ObjectIdentity
hmITMgmt2 = _HmITMgmt2_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6)
)
if mibBuilder.loadTexts:
    hmITMgmt2.setStatus("current")
_HmITSystem_ObjectIdentity = ObjectIdentity
hmITSystem = _HmITSystem_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 1)
)
if mibBuilder.loadTexts:
    hmITSystem.setStatus("current")
_HmITRouterTech_ObjectIdentity = ObjectIdentity
hmITRouterTech = _HmITRouterTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 2)
)
if mibBuilder.loadTexts:
    hmITRouterTech.setStatus("current")
_HmITSwitchTech_ObjectIdentity = ObjectIdentity
hmITSwitchTech = _HmITSwitchTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 3)
)
if mibBuilder.loadTexts:
    hmITSwitchTech.setStatus("current")
_HmITVoipTech_ObjectIdentity = ObjectIdentity
hmITVoipTech = _HmITVoipTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 4)
)
if mibBuilder.loadTexts:
    hmITVoipTech.setStatus("current")
_HmITSecurityTech_ObjectIdentity = ObjectIdentity
hmITSecurityTech = _HmITSecurityTech_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 5)
)
if mibBuilder.loadTexts:
    hmITSecurityTech.setStatus("current")
_HmITApp_ObjectIdentity = ObjectIdentity
hmITApp = _HmITApp_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 6)
)
if mibBuilder.loadTexts:
    hmITApp.setStatus("current")
_HmITOtherSys_ObjectIdentity = ObjectIdentity
hmITOtherSys = _HmITOtherSys_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 248, 100, 1, 6, 7)
)
if mibBuilder.loadTexts:
    hmITOtherSys.setStatus("current")

# Managed Objects groups


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "HMIT-SMI",
    **{"hirschmann": hirschmann,
       "hmVendor": hmVendor,
       "hmITSwitch": hmITSwitch,
       "hmITProducts": hmITProducts,
       "hmITTrapObject": hmITTrapObject,
       "hmITMgmt": hmITMgmt,
       "hmITExperiment": hmITExperiment,
       "hmITSecurity": hmITSecurity,
       "hmITMgmt2": hmITMgmt2,
       "hmITSystem": hmITSystem,
       "hmITRouterTech": hmITRouterTech,
       "hmITSwitchTech": hmITSwitchTech,
       "hmITVoipTech": hmITVoipTech,
       "hmITSecurityTech": hmITSecurityTech,
       "hmITApp": hmITApp,
       "hmITOtherSys": hmITOtherSys}
)
