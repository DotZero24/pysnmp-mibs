# SNMP MIB module (INFINERA-TP-LMM-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-LMM-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:13:02 2025
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

(terminationPoint,) = mibBuilder.importSymbols(
    "INFINERA-REG-MIB",
    "terminationPoint")

(FloatHundredths,
 InfnEnableDisable) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "InfnEnableDisable")

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
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "TextualConvention")


# MODULE-IDENTITY

lmmPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55)
)
if mibBuilder.loadTexts:
    lmmPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LmmPtpTable_Object = MibTable
lmmPtpTable = _LmmPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 1)
)
if mibBuilder.loadTexts:
    lmmPtpTable.setStatus("current")
_LmmPtpEntry_Object = MibTableRow
lmmPtpEntry = _LmmPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 1, 1)
)
lmmPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lmmPtpEntry.setStatus("current")
_LmmPtpRxProvNbrTP_Type = DisplayString
_LmmPtpRxProvNbrTP_Object = MibTableColumn
lmmPtpRxProvNbrTP = _LmmPtpRxProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 1, 1, 1),
    _LmmPtpRxProvNbrTP_Type()
)
lmmPtpRxProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmmPtpRxProvNbrTP.setStatus("current")
_LmmPtpTxProvNbrTP_Type = DisplayString
_LmmPtpTxProvNbrTP_Object = MibTableColumn
lmmPtpTxProvNbrTP = _LmmPtpTxProvNbrTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 1, 1, 2),
    _LmmPtpTxProvNbrTP_Type()
)
lmmPtpTxProvNbrTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmmPtpTxProvNbrTP.setStatus("current")
_LmmPtpProvisionedOpenWaveRemoteTP_Type = DisplayString
_LmmPtpProvisionedOpenWaveRemoteTP_Object = MibTableColumn
lmmPtpProvisionedOpenWaveRemoteTP = _LmmPtpProvisionedOpenWaveRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 1, 1, 3),
    _LmmPtpProvisionedOpenWaveRemoteTP_Type()
)
lmmPtpProvisionedOpenWaveRemoteTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lmmPtpProvisionedOpenWaveRemoteTP.setStatus("current")
_LmmPtpConformance_ObjectIdentity = ObjectIdentity
lmmPtpConformance = _LmmPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 3)
)
_LmmPtpCompliances_ObjectIdentity = ObjectIdentity
lmmPtpCompliances = _LmmPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 3, 1)
)
_LmmPtpGroups_ObjectIdentity = ObjectIdentity
lmmPtpGroups = _LmmPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 3, 2)
)

# Managed Objects groups

lmmPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 3, 2, 1)
)
lmmPtpGroup.setObjects(
      *(("INFINERA-TP-LMM-MIB", "lmmPtpRxProvNbrTP"),
        ("INFINERA-TP-LMM-MIB", "lmmPtpTxProvNbrTP"),
        ("INFINERA-TP-LMM-MIB", "lmmPtpProvisionedOpenWaveRemoteTP"))
)
if mibBuilder.loadTexts:
    lmmPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lmmPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 55, 3, 1, 1)
)
lmmPtpCompliance.setObjects(
    ("INFINERA-TP-LMM-MIB", "lmmPtpGroup")
)
if mibBuilder.loadTexts:
    lmmPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-LMM-MIB",
    **{"lmmPtpMIB": lmmPtpMIB,
       "lmmPtpTable": lmmPtpTable,
       "lmmPtpEntry": lmmPtpEntry,
       "lmmPtpRxProvNbrTP": lmmPtpRxProvNbrTP,
       "lmmPtpTxProvNbrTP": lmmPtpTxProvNbrTP,
       "lmmPtpProvisionedOpenWaveRemoteTP": lmmPtpProvisionedOpenWaveRemoteTP,
       "lmmPtpConformance": lmmPtpConformance,
       "lmmPtpCompliances": lmmPtpCompliances,
       "lmmPtpCompliance": lmmPtpCompliance,
       "lmmPtpGroups": lmmPtpGroups,
       "lmmPtpGroup": lmmPtpGroup}
)
