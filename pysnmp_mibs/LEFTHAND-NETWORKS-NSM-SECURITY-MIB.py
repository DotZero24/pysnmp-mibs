# SNMP MIB module (LEFTHAND-NETWORKS-NSM-SECURITY-MIB) expressed in pysnmp data model.
#
# This Python module is designed to be imported and executed by the
# pysnmp library.
#
# See https://www.pysnmp.com/pysnmp for further information.
#
# Notes
# -----
# ASN.1 source file://mibs/hp/LEFTHAND-NETWORKS-NSM-SECURITY-MIB
# Produced by pysmi-1.6.2 at Fri Oct 10 19:33:06 2025
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

(lhnModules,
 lhnNsm) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-GLOBAL-REG-MIB",
    "lhnModules",
    "lhnNsm")

(lhnNsmSecurity,) = mibBuilder.importSymbols(
    "LEFTHAND-NETWORKS-NSM-MIB",
    "lhnNsmSecurity")

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
 RowStatus,
 TextualConvention) = mibBuilder.importSymbols(
    "SNMPv2-TC",
    "DisplayString",
    "PhysAddress",
    "RowStatus",
    "TextualConvention")


# MODULE-IDENTITY

lhnNsmSecurityModule = ModuleIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 11)
)
if mibBuilder.loadTexts:
    lhnNsmSecurityModule.setRevisions(
        ("2013-11-19 00:00",
         "2013-06-25 00:00",
         "2012-09-04 00:00",
         "2011-06-21 00:00",
         "2010-09-07 00:00",
         "2010-07-19 00:00",
         "2009-11-20 00:00",
         "2009-03-10 00:00",
         "2008-01-24 00:00")
    )


# Types definitions


# TEXTUAL-CONVENTIONS



# MIB Managed Objects in the order of their OIDs

_LhnNsmSecurityModuleConformance_ObjectIdentity = ObjectIdentity
lhnNsmSecurityModuleConformance = _LhnNsmSecurityModuleConformance_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 11, 1)
)
_LhnNsmSecurityModuleCompliances_ObjectIdentity = ObjectIdentity
lhnNsmSecurityModuleCompliances = _LhnNsmSecurityModuleCompliances_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 11, 1, 1)
)
_LhnNsmSecurityModuleGroups_ObjectIdentity = ObjectIdentity
lhnNsmSecurityModuleGroups = _LhnNsmSecurityModuleGroups_ObjectIdentity(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 11, 1, 2)
)
_SecUserCount_Type = Integer32
_SecUserCount_Object = MibScalar
secUserCount = _SecUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 1),
    _SecUserCount_Type()
)
secUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secUserCount.setStatus("obsolete")
_SecUserTable_Object = MibTable
secUserTable = _SecUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2)
)
if mibBuilder.loadTexts:
    secUserTable.setStatus("obsolete")
_SecUserEntry_Object = MibTableRow
secUserEntry = _SecUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1)
)
secUserEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secUserIndex"),
)
if mibBuilder.loadTexts:
    secUserEntry.setStatus("obsolete")
_SecUserIndex_Type = Unsigned32
_SecUserIndex_Object = MibTableColumn
secUserIndex = _SecUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1, 1),
    _SecUserIndex_Type()
)
secUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secUserIndex.setStatus("obsolete")
_SecUserName_Type = DisplayString
_SecUserName_Object = MibTableColumn
secUserName = _SecUserName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1, 2),
    _SecUserName_Type()
)
secUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secUserName.setStatus("obsolete")
_SecUserDesc_Type = DisplayString
_SecUserDesc_Object = MibTableColumn
secUserDesc = _SecUserDesc_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1, 3),
    _SecUserDesc_Type()
)
secUserDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secUserDesc.setStatus("obsolete")
_SecUserPassword_Type = DisplayString
_SecUserPassword_Object = MibTableColumn
secUserPassword = _SecUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1, 4),
    _SecUserPassword_Type()
)
secUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secUserPassword.setStatus("obsolete")
_SecUserRowStatus_Type = RowStatus
_SecUserRowStatus_Object = MibTableColumn
secUserRowStatus = _SecUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 2, 1, 5),
    _SecUserRowStatus_Type()
)
secUserRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secUserRowStatus.setStatus("obsolete")
_SecGroupCount_Type = Integer32
_SecGroupCount_Object = MibScalar
secGroupCount = _SecGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 3),
    _SecGroupCount_Type()
)
secGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secGroupCount.setStatus("obsolete")
_SecGroupTable_Object = MibTable
secGroupTable = _SecGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4)
)
if mibBuilder.loadTexts:
    secGroupTable.setStatus("obsolete")
_SecGroupEntry_Object = MibTableRow
secGroupEntry = _SecGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1)
)
secGroupEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secGroupIndex"),
)
if mibBuilder.loadTexts:
    secGroupEntry.setStatus("obsolete")
_SecGroupIndex_Type = Unsigned32
_SecGroupIndex_Object = MibTableColumn
secGroupIndex = _SecGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1, 1),
    _SecGroupIndex_Type()
)
secGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secGroupIndex.setStatus("obsolete")
_SecGroupName_Type = DisplayString
_SecGroupName_Object = MibTableColumn
secGroupName = _SecGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1, 2),
    _SecGroupName_Type()
)
secGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secGroupName.setStatus("obsolete")
_SecGroupDesc_Type = DisplayString
_SecGroupDesc_Object = MibTableColumn
secGroupDesc = _SecGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1, 3),
    _SecGroupDesc_Type()
)
secGroupDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secGroupDesc.setStatus("obsolete")
_SecGroupUserCount_Type = Integer32
_SecGroupUserCount_Object = MibTableColumn
secGroupUserCount = _SecGroupUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1, 4),
    _SecGroupUserCount_Type()
)
secGroupUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secGroupUserCount.setStatus("obsolete")
_SecGroupRowStatus_Type = RowStatus
_SecGroupRowStatus_Object = MibTableColumn
secGroupRowStatus = _SecGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 4, 1, 5),
    _SecGroupRowStatus_Type()
)
secGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secGroupRowStatus.setStatus("obsolete")
_SecGroupUserTable_Object = MibTable
secGroupUserTable = _SecGroupUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 5)
)
if mibBuilder.loadTexts:
    secGroupUserTable.setStatus("obsolete")
_SecGroupUserEntry_Object = MibTableRow
secGroupUserEntry = _SecGroupUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 5, 1)
)
secGroupUserEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secGroupIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secGroupUserIndex"),
)
if mibBuilder.loadTexts:
    secGroupUserEntry.setStatus("obsolete")
_SecGroupUserIndex_Type = Unsigned32
_SecGroupUserIndex_Object = MibTableColumn
secGroupUserIndex = _SecGroupUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 5, 1, 1),
    _SecGroupUserIndex_Type()
)
secGroupUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secGroupUserIndex.setStatus("obsolete")
_SecGroupUserName_Type = DisplayString
_SecGroupUserName_Object = MibTableColumn
secGroupUserName = _SecGroupUserName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 5, 1, 2),
    _SecGroupUserName_Type()
)
secGroupUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secGroupUserName.setStatus("obsolete")
_SecGroupUserRowStatus_Type = RowStatus
_SecGroupUserRowStatus_Object = MibTableColumn
secGroupUserRowStatus = _SecGroupUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 5, 1, 3),
    _SecGroupUserRowStatus_Type()
)
secGroupUserRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secGroupUserRowStatus.setStatus("obsolete")
_SecAdminUserCount_Type = Integer32
_SecAdminUserCount_Object = MibScalar
secAdminUserCount = _SecAdminUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 6),
    _SecAdminUserCount_Type()
)
secAdminUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminUserCount.setStatus("current")
_SecAdminUserTable_Object = MibTable
secAdminUserTable = _SecAdminUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7)
)
if mibBuilder.loadTexts:
    secAdminUserTable.setStatus("current")
_SecAdminUserEntry_Object = MibTableRow
secAdminUserEntry = _SecAdminUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1)
)
secAdminUserEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminUserIndex"),
)
if mibBuilder.loadTexts:
    secAdminUserEntry.setStatus("current")
_SecAdminUserIndex_Type = Unsigned32
_SecAdminUserIndex_Object = MibTableColumn
secAdminUserIndex = _SecAdminUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1, 1),
    _SecAdminUserIndex_Type()
)
secAdminUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secAdminUserIndex.setStatus("current")
_SecAdminUserName_Type = DisplayString
_SecAdminUserName_Object = MibTableColumn
secAdminUserName = _SecAdminUserName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1, 2),
    _SecAdminUserName_Type()
)
secAdminUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminUserName.setStatus("current")
_SecAdminUserDesc_Type = DisplayString
_SecAdminUserDesc_Object = MibTableColumn
secAdminUserDesc = _SecAdminUserDesc_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1, 3),
    _SecAdminUserDesc_Type()
)
secAdminUserDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminUserDesc.setStatus("current")
_SecAdminUserPassword_Type = DisplayString
_SecAdminUserPassword_Object = MibTableColumn
secAdminUserPassword = _SecAdminUserPassword_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1, 4),
    _SecAdminUserPassword_Type()
)
secAdminUserPassword.setMaxAccess("read-write")
if mibBuilder.loadTexts:
    secAdminUserPassword.setStatus("obsolete")
_SecAdminUserRowStatus_Type = RowStatus
_SecAdminUserRowStatus_Object = MibTableColumn
secAdminUserRowStatus = _SecAdminUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 7, 1, 5),
    _SecAdminUserRowStatus_Type()
)
secAdminUserRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminUserRowStatus.setStatus("obsolete")
_SecAdminGroupCount_Type = Integer32
_SecAdminGroupCount_Object = MibScalar
secAdminGroupCount = _SecAdminGroupCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 8),
    _SecAdminGroupCount_Type()
)
secAdminGroupCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupCount.setStatus("current")
_SecAdminGroupTable_Object = MibTable
secAdminGroupTable = _SecAdminGroupTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9)
)
if mibBuilder.loadTexts:
    secAdminGroupTable.setStatus("current")
_SecAdminGroupEntry_Object = MibTableRow
secAdminGroupEntry = _SecAdminGroupEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1)
)
secAdminGroupEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupIndex"),
)
if mibBuilder.loadTexts:
    secAdminGroupEntry.setStatus("current")
_SecAdminGroupIndex_Type = Unsigned32
_SecAdminGroupIndex_Object = MibTableColumn
secAdminGroupIndex = _SecAdminGroupIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1, 1),
    _SecAdminGroupIndex_Type()
)
secAdminGroupIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secAdminGroupIndex.setStatus("current")
_SecAdminGroupName_Type = DisplayString
_SecAdminGroupName_Object = MibTableColumn
secAdminGroupName = _SecAdminGroupName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1, 2),
    _SecAdminGroupName_Type()
)
secAdminGroupName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupName.setStatus("current")
_SecAdminGroupDesc_Type = DisplayString
_SecAdminGroupDesc_Object = MibTableColumn
secAdminGroupDesc = _SecAdminGroupDesc_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1, 3),
    _SecAdminGroupDesc_Type()
)
secAdminGroupDesc.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupDesc.setStatus("current")
_SecAdminGroupUserCount_Type = Integer32
_SecAdminGroupUserCount_Object = MibTableColumn
secAdminGroupUserCount = _SecAdminGroupUserCount_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1, 4),
    _SecAdminGroupUserCount_Type()
)
secAdminGroupUserCount.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupUserCount.setStatus("current")
_SecAdminGroupRowStatus_Type = RowStatus
_SecAdminGroupRowStatus_Object = MibTableColumn
secAdminGroupRowStatus = _SecAdminGroupRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 9, 1, 5),
    _SecAdminGroupRowStatus_Type()
)
secAdminGroupRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupRowStatus.setStatus("obsolete")
_SecAdminGroupUserTable_Object = MibTable
secAdminGroupUserTable = _SecAdminGroupUserTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 10)
)
if mibBuilder.loadTexts:
    secAdminGroupUserTable.setStatus("current")
_SecAdminGroupUserEntry_Object = MibTableRow
secAdminGroupUserEntry = _SecAdminGroupUserEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 10, 1)
)
secAdminGroupUserEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupUserIndex"),
)
if mibBuilder.loadTexts:
    secAdminGroupUserEntry.setStatus("current")
_SecAdminGroupUserIndex_Type = Unsigned32
_SecAdminGroupUserIndex_Object = MibTableColumn
secAdminGroupUserIndex = _SecAdminGroupUserIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 10, 1, 1),
    _SecAdminGroupUserIndex_Type()
)
secAdminGroupUserIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secAdminGroupUserIndex.setStatus("current")
_SecAdminGroupUserName_Type = DisplayString
_SecAdminGroupUserName_Object = MibTableColumn
secAdminGroupUserName = _SecAdminGroupUserName_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 10, 1, 2),
    _SecAdminGroupUserName_Type()
)
secAdminGroupUserName.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupUserName.setStatus("current")
_SecAdminGroupUserRowStatus_Type = RowStatus
_SecAdminGroupUserRowStatus_Object = MibTableColumn
secAdminGroupUserRowStatus = _SecAdminGroupUserRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 10, 1, 3),
    _SecAdminGroupUserRowStatus_Type()
)
secAdminGroupUserRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupUserRowStatus.setStatus("obsolete")
_SecAdminGroupAccessTable_Object = MibTable
secAdminGroupAccessTable = _SecAdminGroupAccessTable_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11)
)
if mibBuilder.loadTexts:
    secAdminGroupAccessTable.setStatus("obsolete")
_SecAdminGroupAccessEntry_Object = MibTableRow
secAdminGroupAccessEntry = _SecAdminGroupAccessEntry_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11, 1)
)
secAdminGroupAccessEntry.setIndexNames(
    (0, "LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupIndex"),
    (0, "LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupAccessIndex"),
)
if mibBuilder.loadTexts:
    secAdminGroupAccessEntry.setStatus("obsolete")
_SecAdminGroupAccessIndex_Type = Unsigned32
_SecAdminGroupAccessIndex_Object = MibTableColumn
secAdminGroupAccessIndex = _SecAdminGroupAccessIndex_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11, 1, 1),
    _SecAdminGroupAccessIndex_Type()
)
secAdminGroupAccessIndex.setMaxAccess("not-accessible")
if mibBuilder.loadTexts:
    secAdminGroupAccessIndex.setStatus("obsolete")
_SecAdminGroupAccessKey_Type = DisplayString
_SecAdminGroupAccessKey_Object = MibTableColumn
secAdminGroupAccessKey = _SecAdminGroupAccessKey_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11, 1, 2),
    _SecAdminGroupAccessKey_Type()
)
secAdminGroupAccessKey.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupAccessKey.setStatus("obsolete")


class _SecAdminGroupAccessMode_Type(Bits):
    """Custom type secAdminGroupAccessMode based on Bits"""
    namedValues = NamedValues(
        *(("get", 0),
          ("set", 1),
          ("add", 2),
          ("delete", 3))
    )

_SecAdminGroupAccessMode_Type.__name__ = "Bits"
_SecAdminGroupAccessMode_Object = MibTableColumn
secAdminGroupAccessMode = _SecAdminGroupAccessMode_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11, 1, 3),
    _SecAdminGroupAccessMode_Type()
)
secAdminGroupAccessMode.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupAccessMode.setStatus("obsolete")
_SecAdminGroupAccessRowStatus_Type = RowStatus
_SecAdminGroupAccessRowStatus_Object = MibTableColumn
secAdminGroupAccessRowStatus = _SecAdminGroupAccessRowStatus_Object(
    (1, 3, 6, 1, 4, 1, 9804, 3, 1, 1, 2, 11, 11, 1, 4),
    _SecAdminGroupAccessRowStatus_Type()
)
secAdminGroupAccessRowStatus.setMaxAccess("read-only")
if mibBuilder.loadTexts:
    secAdminGroupAccessRowStatus.setStatus("obsolete")

# Managed Objects groups

lefthandNetworksNsmSecurityGroup = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 11, 1, 2, 1)
)
lefthandNetworksNsmSecurityGroup.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminUserCount"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupCount"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminUserName"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminUserDesc"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupName"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupUserName"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupDesc"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupUserCount"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmSecurityGroup.setStatus("current")

lefthandNetworksNsmSecurityGroupObsolete = ObjectGroup(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 11, 1, 2, 2)
)
lefthandNetworksNsmSecurityGroupObsolete.setObjects(
      *(("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secUserCount"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secUserName"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secUserDesc"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secUserPassword"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secUserRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secGroupCount"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secGroupName"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secGroupDesc"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secGroupUserCount"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secGroupRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secGroupUserName"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secGroupUserRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminUserPassword"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminUserRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupUserRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupAccessKey"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupAccessMode"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupAccessRowStatus"),
        ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "secAdminGroupRowStatus"))
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmSecurityGroupObsolete.setStatus("obsolete")


# Notification objects


# Notifications groups


# Agent capabilities


# Module compliance

lefthandNetworksNsmSecurityMibCompliance = ModuleCompliance(
    (1, 3, 6, 1, 4, 1, 9804, 2, 1, 11, 1, 1, 1)
)
lefthandNetworksNsmSecurityMibCompliance.setObjects(
    ("LEFTHAND-NETWORKS-NSM-SECURITY-MIB", "lefthandNetworksNsmSecurityGroup")
)
if mibBuilder.loadTexts:
    lefthandNetworksNsmSecurityMibCompliance.setStatus(
        "current"
    )


# Export all MIB objects to the MIB builder

mibBuilder.exportSymbols(
    "LEFTHAND-NETWORKS-NSM-SECURITY-MIB",
    **{"lhnNsmSecurityModule": lhnNsmSecurityModule,
       "lhnNsmSecurityModuleConformance": lhnNsmSecurityModuleConformance,
       "lhnNsmSecurityModuleCompliances": lhnNsmSecurityModuleCompliances,
       "lefthandNetworksNsmSecurityMibCompliance": lefthandNetworksNsmSecurityMibCompliance,
       "lhnNsmSecurityModuleGroups": lhnNsmSecurityModuleGroups,
       "lefthandNetworksNsmSecurityGroup": lefthandNetworksNsmSecurityGroup,
       "lefthandNetworksNsmSecurityGroupObsolete": lefthandNetworksNsmSecurityGroupObsolete,
       "secUserCount": secUserCount,
       "secUserTable": secUserTable,
       "secUserEntry": secUserEntry,
       "secUserIndex": secUserIndex,
       "secUserName": secUserName,
       "secUserDesc": secUserDesc,
       "secUserPassword": secUserPassword,
       "secUserRowStatus": secUserRowStatus,
       "secGroupCount": secGroupCount,
       "secGroupTable": secGroupTable,
       "secGroupEntry": secGroupEntry,
       "secGroupIndex": secGroupIndex,
       "secGroupName": secGroupName,
       "secGroupDesc": secGroupDesc,
       "secGroupUserCount": secGroupUserCount,
       "secGroupRowStatus": secGroupRowStatus,
       "secGroupUserTable": secGroupUserTable,
       "secGroupUserEntry": secGroupUserEntry,
       "secGroupUserIndex": secGroupUserIndex,
       "secGroupUserName": secGroupUserName,
       "secGroupUserRowStatus": secGroupUserRowStatus,
       "secAdminUserCount": secAdminUserCount,
       "secAdminUserTable": secAdminUserTable,
       "secAdminUserEntry": secAdminUserEntry,
       "secAdminUserIndex": secAdminUserIndex,
       "secAdminUserName": secAdminUserName,
       "secAdminUserDesc": secAdminUserDesc,
       "secAdminUserPassword": secAdminUserPassword,
       "secAdminUserRowStatus": secAdminUserRowStatus,
       "secAdminGroupCount": secAdminGroupCount,
       "secAdminGroupTable": secAdminGroupTable,
       "secAdminGroupEntry": secAdminGroupEntry,
       "secAdminGroupIndex": secAdminGroupIndex,
       "secAdminGroupName": secAdminGroupName,
       "secAdminGroupDesc": secAdminGroupDesc,
       "secAdminGroupUserCount": secAdminGroupUserCount,
       "secAdminGroupRowStatus": secAdminGroupRowStatus,
       "secAdminGroupUserTable": secAdminGroupUserTable,
       "secAdminGroupUserEntry": secAdminGroupUserEntry,
       "secAdminGroupUserIndex": secAdminGroupUserIndex,
       "secAdminGroupUserName": secAdminGroupUserName,
       "secAdminGroupUserRowStatus": secAdminGroupUserRowStatus,
       "secAdminGroupAccessTable": secAdminGroupAccessTable,
       "secAdminGroupAccessEntry": secAdminGroupAccessEntry,
       "secAdminGroupAccessIndex": secAdminGroupAccessIndex,
       "secAdminGroupAccessKey": secAdminGroupAccessKey,
       "secAdminGroupAccessMode": secAdminGroupAccessMode,
       "secAdminGroupAccessRowStatus": secAdminGroupAccessRowStatus}
)
