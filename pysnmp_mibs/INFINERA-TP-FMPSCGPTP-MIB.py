# SNMP MIB module (INFINERA-TP-FMPSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-FMPSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:15:34 2025
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

fmpScgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53)
)
if mibBuilder.loadTexts:
    fmpScgPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_FmpScgPtpTable_Object = MibTable
fmpScgPtpTable = _FmpScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1)
)
if mibBuilder.loadTexts:
    fmpScgPtpTable.setStatus("current")
_FmpScgPtpEntry_Object = MibTableRow
fmpScgPtpEntry = _FmpScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1, 1)
)
fmpScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    fmpScgPtpEntry.setStatus("current")
_FmpScgPtpProvisionedNeighborTP_Type = DisplayString
_FmpScgPtpProvisionedNeighborTP_Object = MibTableColumn
fmpScgPtpProvisionedNeighborTP = _FmpScgPtpProvisionedNeighborTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1, 1, 1),
    _FmpScgPtpProvisionedNeighborTP_Type()
)
fmpScgPtpProvisionedNeighborTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmpScgPtpProvisionedNeighborTP.setStatus("current")
_FmpScgPtpMPOAID_Type = DisplayString
_FmpScgPtpMPOAID_Object = MibTableColumn
fmpScgPtpMPOAID = _FmpScgPtpMPOAID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1, 1, 2),
    _FmpScgPtpMPOAID_Type()
)
fmpScgPtpMPOAID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmpScgPtpMPOAID.setStatus("current")
_FmpScgPtpProvisionedOpenWaveRemoteTP_Type = DisplayString
_FmpScgPtpProvisionedOpenWaveRemoteTP_Object = MibTableColumn
fmpScgPtpProvisionedOpenWaveRemoteTP = _FmpScgPtpProvisionedOpenWaveRemoteTP_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1, 1, 3),
    _FmpScgPtpProvisionedOpenWaveRemoteTP_Type()
)
fmpScgPtpProvisionedOpenWaveRemoteTP.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmpScgPtpProvisionedOpenWaveRemoteTP.setStatus("current")
_FmpScgPtpNeighborFPMPOID_Type = DisplayString
_FmpScgPtpNeighborFPMPOID_Object = MibTableColumn
fmpScgPtpNeighborFPMPOID = _FmpScgPtpNeighborFPMPOID_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 1, 1, 4),
    _FmpScgPtpNeighborFPMPOID_Type()
)
fmpScgPtpNeighborFPMPOID.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    fmpScgPtpNeighborFPMPOID.setStatus("current")
_FmpScgPtpConformance_ObjectIdentity = ObjectIdentity
fmpScgPtpConformance = _FmpScgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 3)
)
_FmpScgPtpCompliances_ObjectIdentity = ObjectIdentity
fmpScgPtpCompliances = _FmpScgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 3, 1)
)
_FmpScgPtpGroups_ObjectIdentity = ObjectIdentity
fmpScgPtpGroups = _FmpScgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 3, 2)
)

# Managed Objects groups

fmpScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 3, 2, 1)
)
fmpScgPtpGroup.setObjects(
      *(("INFINERA-TP-FMPSCGPTP-MIB", "fmpScgPtpProvisionedNeighborTP"),
        ("INFINERA-TP-FMPSCGPTP-MIB", "fmpScgPtpMPOAID"),
        ("INFINERA-TP-FMPSCGPTP-MIB", "fmpScgPtpProvisionedOpenWaveRemoteTP"),
        ("INFINERA-TP-FMPSCGPTP-MIB", "fmpScgPtpNeighborFPMPOID"))
)
if mibBuilder.loadTexts:
    fmpScgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

fmpScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 53, 3, 1, 1)
)
fmpScgPtpCompliance.setObjects(
    ("INFINERA-TP-FMPSCGPTP-MIB", "fmpScgPtpGroup")
)
if mibBuilder.loadTexts:
    fmpScgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-FMPSCGPTP-MIB",
    **{"fmpScgPtpMIB": fmpScgPtpMIB,
       "fmpScgPtpTable": fmpScgPtpTable,
       "fmpScgPtpEntry": fmpScgPtpEntry,
       "fmpScgPtpProvisionedNeighborTP": fmpScgPtpProvisionedNeighborTP,
       "fmpScgPtpMPOAID": fmpScgPtpMPOAID,
       "fmpScgPtpProvisionedOpenWaveRemoteTP": fmpScgPtpProvisionedOpenWaveRemoteTP,
       "fmpScgPtpNeighborFPMPOID": fmpScgPtpNeighborFPMPOID,
       "fmpScgPtpConformance": fmpScgPtpConformance,
       "fmpScgPtpCompliances": fmpScgPtpCompliances,
       "fmpScgPtpCompliance": fmpScgPtpCompliance,
       "fmpScgPtpGroups": fmpScgPtpGroups,
       "fmpScgPtpGroup": fmpScgPtpGroup}
)
