# SNMP MIB module (INFINERA-TP-OFXSCGPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-OFXSCGPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:16:03 2025
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
 FloatTenths,
 InfnEnableDisable,
 InfnEncoding,
 InfnEqptType,
 InfnOperatingMode) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "FloatHundredths",
    "FloatTenths",
    "InfnEnableDisable",
    "InfnEncoding",
    "InfnEqptType",
    "InfnOperatingMode")

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

ofxScgPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42)
)
if mibBuilder.loadTexts:
    ofxScgPtpMIB.setRevisions(
        ("2013-10-20 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_OfxScgPtpTable_Object = MibTable
ofxScgPtpTable = _OfxScgPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1)
)
if mibBuilder.loadTexts:
    ofxScgPtpTable.setStatus("current")
_OfxScgPtpEntry_Object = MibTableRow
ofxScgPtpEntry = _OfxScgPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1)
)
ofxScgPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    ofxScgPtpEntry.setStatus("current")
_OfxScgPtpPowerControlLoop_Type = InfnEnableDisable
_OfxScgPtpPowerControlLoop_Object = MibTableColumn
ofxScgPtpPowerControlLoop = _OfxScgPtpPowerControlLoop_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1, 1),
    _OfxScgPtpPowerControlLoop_Type()
)
ofxScgPtpPowerControlLoop.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxScgPtpPowerControlLoop.setStatus("current")
_OfxScgPtpProvEncodingMode_Type = InfnEncoding
_OfxScgPtpProvEncodingMode_Object = MibTableColumn
ofxScgPtpProvEncodingMode = _OfxScgPtpProvEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1, 2),
    _OfxScgPtpProvEncodingMode_Type()
)
ofxScgPtpProvEncodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxScgPtpProvEncodingMode.setStatus("current")


class _OfxScgPtpLineSystemMode_Type(Integer32):
    """Custom type ofxScgPtpLineSystemMode based on Integer32"""
    subtypeSpec = Integer32.subtypeSpec
    subtypeSpec += ConstraintsUnion(
        SingleValueConstraint(
            *(1,
              2,
              3,
              4)
        )
    )
    namedValues = NamedValues(
        *(("modeOcg", 1),
          ("modeOpenWave", 2),
          ("modeScg", 3),
          ("modeScgPassiveMux1", 4))
    )


_OfxScgPtpLineSystemMode_Type.__name__ = "Integer32"
_OfxScgPtpLineSystemMode_Object = MibTableColumn
ofxScgPtpLineSystemMode = _OfxScgPtpLineSystemMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1, 3),
    _OfxScgPtpLineSystemMode_Type()
)
ofxScgPtpLineSystemMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxScgPtpLineSystemMode.setStatus("current")
_OfxScgPtpInstalledEncodingMode_Type = InfnEncoding
_OfxScgPtpInstalledEncodingMode_Object = MibTableColumn
ofxScgPtpInstalledEncodingMode = _OfxScgPtpInstalledEncodingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1, 4),
    _OfxScgPtpInstalledEncodingMode_Type()
)
ofxScgPtpInstalledEncodingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxScgPtpInstalledEncodingMode.setStatus("current")
_OfxScgPtpRxPowerOffset_Type = FloatHundredths
_OfxScgPtpRxPowerOffset_Object = MibTableColumn
ofxScgPtpRxPowerOffset = _OfxScgPtpRxPowerOffset_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1, 5),
    _OfxScgPtpRxPowerOffset_Type()
)
ofxScgPtpRxPowerOffset.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxScgPtpRxPowerOffset.setStatus("current")
_OfxScgPtpProvisionedPeerTp_Type = DisplayString
_OfxScgPtpProvisionedPeerTp_Object = MibTableColumn
ofxScgPtpProvisionedPeerTp = _OfxScgPtpProvisionedPeerTp_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1, 6),
    _OfxScgPtpProvisionedPeerTp_Type()
)
ofxScgPtpProvisionedPeerTp.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxScgPtpProvisionedPeerTp.setStatus("current")
_OfxScgPtpOpenwaveTargetTxScgPower_Type = FloatTenths
_OfxScgPtpOpenwaveTargetTxScgPower_Object = MibTableColumn
ofxScgPtpOpenwaveTargetTxScgPower = _OfxScgPtpOpenwaveTargetTxScgPower_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1, 7),
    _OfxScgPtpOpenwaveTargetTxScgPower_Type()
)
ofxScgPtpOpenwaveTargetTxScgPower.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxScgPtpOpenwaveTargetTxScgPower.setStatus("current")
_OfxScgPtpCarrierCount_Type = FloatHundredths
_OfxScgPtpCarrierCount_Object = MibTableColumn
ofxScgPtpCarrierCount = _OfxScgPtpCarrierCount_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1, 8),
    _OfxScgPtpCarrierCount_Type()
)
ofxScgPtpCarrierCount.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxScgPtpCarrierCount.setStatus("current")
_OfxScgPtpOperatingMode_Type = InfnOperatingMode
_OfxScgPtpOperatingMode_Object = MibTableColumn
ofxScgPtpOperatingMode = _OfxScgPtpOperatingMode_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1, 9),
    _OfxScgPtpOperatingMode_Type()
)
ofxScgPtpOperatingMode.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    ofxScgPtpOperatingMode.setStatus("current")
_OfxScgPtpUnAssignedCarrierList_Type = DisplayString
_OfxScgPtpUnAssignedCarrierList_Object = MibTableColumn
ofxScgPtpUnAssignedCarrierList = _OfxScgPtpUnAssignedCarrierList_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 1, 1, 10),
    _OfxScgPtpUnAssignedCarrierList_Type()
)
ofxScgPtpUnAssignedCarrierList.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    ofxScgPtpUnAssignedCarrierList.setStatus("current")
_OfxScgPtpConformance_ObjectIdentity = ObjectIdentity
ofxScgPtpConformance = _OfxScgPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 3)
)
_OfxScgPtpCompliances_ObjectIdentity = ObjectIdentity
ofxScgPtpCompliances = _OfxScgPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 3, 1)
)
_OfxScgPtpGroups_ObjectIdentity = ObjectIdentity
ofxScgPtpGroups = _OfxScgPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 3, 2)
)

# Managed Objects groups

ofxScgPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 3, 2, 1)
)
ofxScgPtpGroup.setObjects(
      *(("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpPowerControlLoop"),
        ("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpProvEncodingMode"),
        ("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpLineSystemMode"),
        ("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpInstalledEncodingMode"),
        ("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpRxPowerOffset"),
        ("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpProvisionedPeerTp"),
        ("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpOpenwaveTargetTxScgPower"),
        ("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpCarrierCount"),
        ("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpOperatingMode"),
        ("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpUnAssignedCarrierList"))
)
if mibBuilder.loadTexts:
    ofxScgPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

ofxScgPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 42, 3, 1, 1)
)
ofxScgPtpCompliance.setObjects(
    ("INFINERA-TP-OFXSCGPTP-MIB", "ofxScgPtpGroup")
)
if mibBuilder.loadTexts:
    ofxScgPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-OFXSCGPTP-MIB",
    **{"ofxScgPtpMIB": ofxScgPtpMIB,
       "ofxScgPtpTable": ofxScgPtpTable,
       "ofxScgPtpEntry": ofxScgPtpEntry,
       "ofxScgPtpPowerControlLoop": ofxScgPtpPowerControlLoop,
       "ofxScgPtpProvEncodingMode": ofxScgPtpProvEncodingMode,
       "ofxScgPtpLineSystemMode": ofxScgPtpLineSystemMode,
       "ofxScgPtpInstalledEncodingMode": ofxScgPtpInstalledEncodingMode,
       "ofxScgPtpRxPowerOffset": ofxScgPtpRxPowerOffset,
       "ofxScgPtpProvisionedPeerTp": ofxScgPtpProvisionedPeerTp,
       "ofxScgPtpOpenwaveTargetTxScgPower": ofxScgPtpOpenwaveTargetTxScgPower,
       "ofxScgPtpCarrierCount": ofxScgPtpCarrierCount,
       "ofxScgPtpOperatingMode": ofxScgPtpOperatingMode,
       "ofxScgPtpUnAssignedCarrierList": ofxScgPtpUnAssignedCarrierList,
       "ofxScgPtpConformance": ofxScgPtpConformance,
       "ofxScgPtpCompliances": ofxScgPtpCompliances,
       "ofxScgPtpCompliance": ofxScgPtpCompliance,
       "ofxScgPtpGroups": ofxScgPtpGroups,
       "ofxScgPtpGroup": ofxScgPtpGroup}
)
