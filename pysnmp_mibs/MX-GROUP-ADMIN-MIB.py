_P='groupAdminGroupVer1'
_O='groupAdminParentGroup'
_N='groupAdminDescription'
_M='groupAdminType'
_L='groupReset'
_K='groupUsageState'
_J='groupOpState'
_I='groupAdminState'
_H='groupSetAdmin'
_G='read-write'
_F='groupAdminIndex'
_E='OctetString'
_D='read-only'
_C='Integer32'
_B='MX-GROUP-ADMIN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer',_E,'ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
mediatrixAdmin,=mibBuilder.importSymbols('MX-SMI','mediatrixAdmin')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
groupAdminMIB=ModuleIdentity((1,3,6,1,4,1,4935,5,5))
if mibBuilder.loadTexts:groupAdminMIB.setRevisions(('2005-08-23 00:00',))
_GroupAdminMIBObjects_ObjectIdentity=ObjectIdentity
groupAdminMIBObjects=_GroupAdminMIBObjects_ObjectIdentity((1,3,6,1,4,1,4935,5,5,1))
_GroupAdminTable_Object=MibTable
groupAdminTable=_GroupAdminTable_Object((1,3,6,1,4,1,4935,5,5,1,1))
if mibBuilder.loadTexts:groupAdminTable.setStatus(_A)
_GroupAdminEntry_Object=MibTableRow
groupAdminEntry=_GroupAdminEntry_Object((1,3,6,1,4,1,4935,5,5,1,1,1))
groupAdminEntry.setIndexNames((0,_B,_F))
if mibBuilder.loadTexts:groupAdminEntry.setStatus(_A)
_GroupAdminIndex_Type=Integer32
_GroupAdminIndex_Object=MibTableColumn
groupAdminIndex=_GroupAdminIndex_Object((1,3,6,1,4,1,4935,5,5,1,1,1,1),_GroupAdminIndex_Type())
groupAdminIndex.setMaxAccess('not-accessible')
if mibBuilder.loadTexts:groupAdminIndex.setStatus(_A)
class _GroupSetAdmin_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*(('noOp',0),('unlock',1),('lock',2),('forcelock',3)))
_GroupSetAdmin_Type.__name__=_C
_GroupSetAdmin_Object=MibTableColumn
groupSetAdmin=_GroupSetAdmin_Object((1,3,6,1,4,1,4935,5,5,1,1,1,2),_GroupSetAdmin_Type())
groupSetAdmin.setMaxAccess(_G)
if mibBuilder.loadTexts:groupSetAdmin.setStatus(_A)
class _GroupAdminState_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('unlocked',1),('shuttingDown',2),('locked',3)))
_GroupAdminState_Type.__name__=_C
_GroupAdminState_Object=MibTableColumn
groupAdminState=_GroupAdminState_Object((1,3,6,1,4,1,4935,5,5,1,1,1,3),_GroupAdminState_Type())
groupAdminState.setMaxAccess(_D)
if mibBuilder.loadTexts:groupAdminState.setStatus(_A)
class _GroupOpState_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('enabled',1),('disabled',2)))
_GroupOpState_Type.__name__=_C
_GroupOpState_Object=MibTableColumn
groupOpState=_GroupOpState_Object((1,3,6,1,4,1,4935,5,5,1,1,1,4),_GroupOpState_Type())
groupOpState.setMaxAccess(_D)
if mibBuilder.loadTexts:groupOpState.setStatus(_A)
class _GroupUsageState_Type(Integer32):defaultValue=4;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('idle',1),('active',2),('busy',3),('idle-unusable',4)))
_GroupUsageState_Type.__name__=_C
_GroupUsageState_Object=MibTableColumn
groupUsageState=_GroupUsageState_Object((1,3,6,1,4,1,4935,5,5,1,1,1,6),_GroupUsageState_Type())
groupUsageState.setMaxAccess(_D)
if mibBuilder.loadTexts:groupUsageState.setStatus(_A)
class _GroupReset_Type(Integer32):defaultValue=0;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1)));namedValues=NamedValues(*(('noOp',0),('softReset',1)))
_GroupReset_Type.__name__=_C
_GroupReset_Object=MibTableColumn
groupReset=_GroupReset_Object((1,3,6,1,4,1,4935,5,5,1,1,1,8),_GroupReset_Type())
groupReset.setMaxAccess(_G)
if mibBuilder.loadTexts:groupReset.setStatus(_A)
class _GroupAdminType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(1));namedValues=NamedValues(('gateway',1))
_GroupAdminType_Type.__name__=_C
_GroupAdminType_Object=MibTableColumn
groupAdminType=_GroupAdminType_Object((1,3,6,1,4,1,4935,5,5,1,1,1,11),_GroupAdminType_Type())
groupAdminType.setMaxAccess(_D)
if mibBuilder.loadTexts:groupAdminType.setStatus(_A)
class _GroupAdminDescription_Type(OctetString):subtypeSpec=OctetString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,255))
_GroupAdminDescription_Type.__name__=_E
_GroupAdminDescription_Object=MibTableColumn
groupAdminDescription=_GroupAdminDescription_Object((1,3,6,1,4,1,4935,5,5,1,1,1,12),_GroupAdminDescription_Type())
groupAdminDescription.setMaxAccess(_D)
if mibBuilder.loadTexts:groupAdminDescription.setStatus(_A)
class _GroupAdminParentGroup_Type(Integer32):defaultValue=-1
_GroupAdminParentGroup_Type.__name__=_C
_GroupAdminParentGroup_Object=MibTableColumn
groupAdminParentGroup=_GroupAdminParentGroup_Object((1,3,6,1,4,1,4935,5,5,1,1,1,15),_GroupAdminParentGroup_Type())
groupAdminParentGroup.setMaxAccess(_D)
if mibBuilder.loadTexts:groupAdminParentGroup.setStatus(_A)
_GroupAdminConformance_ObjectIdentity=ObjectIdentity
groupAdminConformance=_GroupAdminConformance_ObjectIdentity((1,3,6,1,4,1,4935,5,5,2))
_GroupAdminCompliances_ObjectIdentity=ObjectIdentity
groupAdminCompliances=_GroupAdminCompliances_ObjectIdentity((1,3,6,1,4,1,4935,5,5,2,1))
_GroupAdminGroups_ObjectIdentity=ObjectIdentity
groupAdminGroups=_GroupAdminGroups_ObjectIdentity((1,3,6,1,4,1,4935,5,5,2,2))
groupAdminGroupVer1=ObjectGroup((1,3,6,1,4,1,4935,5,5,2,2,1))
groupAdminGroupVer1.setObjects(*((_B,_H),(_B,_I),(_B,_J),(_B,_K),(_B,_L),(_B,_M),(_B,_N),(_B,_O)))
if mibBuilder.loadTexts:groupAdminGroupVer1.setStatus(_A)
groupAdminComplVer1=ModuleCompliance((1,3,6,1,4,1,4935,5,5,2,1,1))
groupAdminComplVer1.setObjects((_B,_P))
if mibBuilder.loadTexts:groupAdminComplVer1.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'groupAdminMIB':groupAdminMIB,'groupAdminMIBObjects':groupAdminMIBObjects,'groupAdminTable':groupAdminTable,'groupAdminEntry':groupAdminEntry,_F:groupAdminIndex,_H:groupSetAdmin,_I:groupAdminState,_J:groupOpState,_K:groupUsageState,_L:groupReset,_M:groupAdminType,_N:groupAdminDescription,_O:groupAdminParentGroup,'groupAdminConformance':groupAdminConformance,'groupAdminCompliances':groupAdminCompliances,'groupAdminComplVer1':groupAdminComplVer1,'groupAdminGroups':groupAdminGroups,_P:groupAdminGroupVer1})