# SNMP MIB module (TN-SAS-IEEE8021-PAE-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/nokia/TN-SAS-IEEE8021-PAE-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:58:51 2025
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

(dot1xAuthConfigEntry,) = mibBuilder.importSymbols(
    "IEEE8021-PAE-MIB",
    "dot1xAuthConfigEntry")

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

(tnSASModules,
 tnSASObjs) = mibBuilder.importSymbols(
    "TROPIC-GLOBAL-REG",
    "tnSASModules",
    "tnSASObjs")


# MODULE-IDENTITY

tnSASIEEE8021PaeMIBModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 1, 1, 17)
)
if mibBuilder.loadTexts:
    tnSASIEEE8021PaeMIBModule.setRevisions(
        ("2015-01-09 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_TnSASDot1xMIBObjs_ObjectIdentity = ObjectIdentity
tnSASDot1xMIBObjs = _TnSASDot1xMIBObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16)
)
_TnSASDot1xAuthenticatorObjs_ObjectIdentity = ObjectIdentity
tnSASDot1xAuthenticatorObjs = _TnSASDot1xAuthenticatorObjs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 1)
)
_TnDot1xAuthConfigExtnTable_Object = MibTable
tnDot1xAuthConfigExtnTable = _TnDot1xAuthConfigExtnTable_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 1, 1)
)
if mibBuilder.loadTexts:
    tnDot1xAuthConfigExtnTable.setStatus("current")
_TnDot1xAuthConfigExtnEntry_Object = MibTableRow
tnDot1xAuthConfigExtnEntry = _TnDot1xAuthConfigExtnEntry_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 1, 1, 1)
)
if mibBuilder.loadTexts:
    tnDot1xAuthConfigExtnEntry.setStatus("current")


class _TnDot1xPortEtherTunnel_Type(TruthValue):
    """Custom type tnDot1xPortEtherTunnel based on TruthValue"""
    defaultValue = 2


_TnDot1xPortEtherTunnel_Type.__name__ = "TruthValue"
_TnDot1xPortEtherTunnel_Object = MibTableColumn
tnDot1xPortEtherTunnel = _TnDot1xPortEtherTunnel_Object(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 1, 1, 1, 1),
    _TnDot1xPortEtherTunnel_Type()
)
tnDot1xPortEtherTunnel.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    tnDot1xPortEtherTunnel.setStatus("current")
_TnDot1xSASCompliancs_ObjectIdentity = ObjectIdentity
tnDot1xSASCompliancs = _TnDot1xSASCompliancs_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 2)
)
_TnDot1xSASGroups_ObjectIdentity = ObjectIdentity
tnDot1xSASGroups = _TnDot1xSASGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 3)
)
dot1xAuthConfigEntry.registerAugmentions(
    ("TN-SAS-IEEE8021-PAE-MIB",
     "tnDot1xAuthConfigExtnEntry")
)
tnDot1xAuthConfigExtnEntry.setIndexNames(*dot1xAuthConfigEntry.getIndexNames())

# Managed Objects groups

tnDot1xAuthConfigExtnGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 3, 1)
)
tnDot1xAuthConfigExtnGroup.setObjects(
    ("TN-SAS-IEEE8021-PAE-MIB", "tnDot1xPortEtherTunnel")
)
if mibBuilder.loadTexts:
    tnDot1xAuthConfigExtnGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

tnDot1xAuthConfigExtnCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 7483, 7, 2, 2, 2, 16, 2, 1)
)
tnDot1xAuthConfigExtnCompliance.setObjects(
    ("TN-SAS-IEEE8021-PAE-MIB", "tnDot1xAuthConfigExtnGroup")
)
if mibBuilder.loadTexts:
    tnDot1xAuthConfigExtnCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "TN-SAS-IEEE8021-PAE-MIB",
    **{"tnSASIEEE8021PaeMIBModule": tnSASIEEE8021PaeMIBModule,
       "tnSASDot1xMIBObjs": tnSASDot1xMIBObjs,
       "tnSASDot1xAuthenticatorObjs": tnSASDot1xAuthenticatorObjs,
       "tnDot1xAuthConfigExtnTable": tnDot1xAuthConfigExtnTable,
       "tnDot1xAuthConfigExtnEntry": tnDot1xAuthConfigExtnEntry,
       "tnDot1xPortEtherTunnel": tnDot1xPortEtherTunnel,
       "tnDot1xSASCompliancs": tnDot1xSASCompliancs,
       "tnDot1xAuthConfigExtnCompliance": tnDot1xAuthConfigExtnCompliance,
       "tnDot1xSASGroups": tnDot1xSASGroups,
       "tnDot1xAuthConfigExtnGroup": tnDot1xAuthConfigExtnGroup}
)
