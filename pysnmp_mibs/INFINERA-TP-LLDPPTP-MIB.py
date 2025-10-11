# SNMP MIB module (INFINERA-TP-LLDPPTP-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/infinera/INFINERA-TP-LLDPPTP-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 20:12:46 2025
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

(InfnChassisIdSubtype,
 InfnManAddrIfSubtype,
 InfnManAddrSubtype,
 InfnPortIdSubtype) = mibBuilder.importSymbols(
    "INFINERA-TC-MIB",
    "InfnChassisIdSubtype",
    "InfnManAddrIfSubtype",
    "InfnManAddrSubtype",
    "InfnPortIdSubtype")

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

lldpPtpMIB = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56)
)
if mibBuilder.loadTexts:
    lldpPtpMIB.setRevisions(
        ("2015-06-24 00:00",)
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LldpRemoteSysPtpTable_Object = MibTable
lldpRemoteSysPtpTable = _LldpRemoteSysPtpTable_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1)
)
if mibBuilder.loadTexts:
    lldpRemoteSysPtpTable.setStatus("current")
_LldpPtpEntry_Object = MibTableRow
lldpPtpEntry = _LldpPtpEntry_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1, 1)
)
lldpPtpEntry.setIndexNames(
    (0, "IF-MIB", "ifIndex"),
)
if mibBuilder.loadTexts:
    lldpPtpEntry.setStatus("current")
_LldpRemoteSysChassisIdSubtype_Type = InfnChassisIdSubtype
_LldpRemoteSysChassisIdSubtype_Object = MibTableColumn
lldpRemoteSysChassisIdSubtype = _LldpRemoteSysChassisIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1, 1, 1),
    _LldpRemoteSysChassisIdSubtype_Type()
)
lldpRemoteSysChassisIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSysChassisIdSubtype.setStatus("current")
_LldpRemoteSysChassisId_Type = DisplayString
_LldpRemoteSysChassisId_Object = MibTableColumn
lldpRemoteSysChassisId = _LldpRemoteSysChassisId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1, 1, 2),
    _LldpRemoteSysChassisId_Type()
)
lldpRemoteSysChassisId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSysChassisId.setStatus("current")
_LldpRemoteSysPortIdSubtype_Type = InfnPortIdSubtype
_LldpRemoteSysPortIdSubtype_Object = MibTableColumn
lldpRemoteSysPortIdSubtype = _LldpRemoteSysPortIdSubtype_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1, 1, 3),
    _LldpRemoteSysPortIdSubtype_Type()
)
lldpRemoteSysPortIdSubtype.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSysPortIdSubtype.setStatus("current")
_LldpRemoteSysPortId_Type = DisplayString
_LldpRemoteSysPortId_Object = MibTableColumn
lldpRemoteSysPortId = _LldpRemoteSysPortId_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1, 1, 4),
    _LldpRemoteSysPortId_Type()
)
lldpRemoteSysPortId.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSysPortId.setStatus("current")
_LldpRemoteSysTtl_Type = Integer32
_LldpRemoteSysTtl_Object = MibTableColumn
lldpRemoteSysTtl = _LldpRemoteSysTtl_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1, 1, 5),
    _LldpRemoteSysTtl_Type()
)
lldpRemoteSysTtl.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSysTtl.setStatus("current")
_LldpRemoteSysPortDesc_Type = DisplayString
_LldpRemoteSysPortDesc_Object = MibTableColumn
lldpRemoteSysPortDesc = _LldpRemoteSysPortDesc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1, 1, 6),
    _LldpRemoteSysPortDesc_Type()
)
lldpRemoteSysPortDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSysPortDesc.setStatus("current")
_LldpRemoteSysSysName_Type = DisplayString
_LldpRemoteSysSysName_Object = MibTableColumn
lldpRemoteSysSysName = _LldpRemoteSysSysName_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1, 1, 7),
    _LldpRemoteSysSysName_Type()
)
lldpRemoteSysSysName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSysSysName.setStatus("current")
_LldpRemoteSysSysDesc_Type = DisplayString
_LldpRemoteSysSysDesc_Object = MibTableColumn
lldpRemoteSysSysDesc = _LldpRemoteSysSysDesc_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1, 1, 8),
    _LldpRemoteSysSysDesc_Type()
)
lldpRemoteSysSysDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    lldpRemoteSysSysDesc.setStatus("current")
_LldpRemoteSysLastReceivedTimeString_Type = DisplayString
_LldpRemoteSysLastReceivedTimeString_Object = MibTableColumn
lldpRemoteSysLastReceivedTimeString = _LldpRemoteSysLastReceivedTimeString_Object(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 1, 1, 9),
    _LldpRemoteSysLastReceivedTimeString_Type()
)
lldpRemoteSysLastReceivedTimeString.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    lldpRemoteSysLastReceivedTimeString.setStatus("current")
_LldpPtpConformance_ObjectIdentity = ObjectIdentity
lldpPtpConformance = _LldpPtpConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 3)
)
_LldpPtpCompliances_ObjectIdentity = ObjectIdentity
lldpPtpCompliances = _LldpPtpCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 3, 1)
)
_LldpPtpGroups_ObjectIdentity = ObjectIdentity
lldpPtpGroups = _LldpPtpGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 3, 2)
)

# Managed Objects groups

lldpPtpGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 3, 2, 1)
)
lldpPtpGroup.setObjects(
      *(("INFINERA-TP-LLDPPTP-MIB", "lldpRemoteSysChassisIdSubtype"),
        ("INFINERA-TP-LLDPPTP-MIB", "lldpRemoteSysChassisId"),
        ("INFINERA-TP-LLDPPTP-MIB", "lldpRemoteSysPortIdSubtype"),
        ("INFINERA-TP-LLDPPTP-MIB", "lldpRemoteSysPortId"),
        ("INFINERA-TP-LLDPPTP-MIB", "lldpRemoteSysTtl"),
        ("INFINERA-TP-LLDPPTP-MIB", "lldpRemoteSysPortDesc"),
        ("INFINERA-TP-LLDPPTP-MIB", "lldpRemoteSysSysName"),
        ("INFINERA-TP-LLDPPTP-MIB", "lldpRemoteSysSysDesc"),
        ("INFINERA-TP-LLDPPTP-MIB", "lldpRemoteSysLastReceivedTimeString"))
)
if mibBuilder.loadTexts:
    lldpPtpGroup.setStatus("current")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lldpPtpCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 21296, 2, 2, 2, 2, 56, 3, 1, 1)
)
lldpPtpCompliance.setObjects(
    ("INFINERA-TP-LLDPPTP-MIB", "lldpPtpGroup")
)
if mibBuilder.loadTexts:
    lldpPtpCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "INFINERA-TP-LLDPPTP-MIB",
    **{"lldpPtpMIB": lldpPtpMIB,
       "lldpRemoteSysPtpTable": lldpRemoteSysPtpTable,
       "lldpPtpEntry": lldpPtpEntry,
       "lldpRemoteSysChassisIdSubtype": lldpRemoteSysChassisIdSubtype,
       "lldpRemoteSysChassisId": lldpRemoteSysChassisId,
       "lldpRemoteSysPortIdSubtype": lldpRemoteSysPortIdSubtype,
       "lldpRemoteSysPortId": lldpRemoteSysPortId,
       "lldpRemoteSysTtl": lldpRemoteSysTtl,
       "lldpRemoteSysPortDesc": lldpRemoteSysPortDesc,
       "lldpRemoteSysSysName": lldpRemoteSysSysName,
       "lldpRemoteSysSysDesc": lldpRemoteSysSysDesc,
       "lldpRemoteSysLastReceivedTimeString": lldpRemoteSysLastReceivedTimeString,
       "lldpPtpConformance": lldpPtpConformance,
       "lldpPtpCompliances": lldpPtpCompliances,
       "lldpPtpCompliance": lldpPtpCompliance,
       "lldpPtpGroups": lldpPtpGroups,
       "lldpPtpGroup": lldpPtpGroup}
)
