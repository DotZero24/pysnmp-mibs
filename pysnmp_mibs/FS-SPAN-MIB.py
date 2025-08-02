_J='fsSPANMIBGroup'
_I='fsSPANEntryStatus'
_H='fsSPANIfRole'
_G='read-create'
_F='Integer32'
_E='fsSPANIfIndex'
_D='fsSPANSession'
_C='read-only'
_B='FS-SPAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
fsMgmt,=mibBuilder.importSymbols('FS-SMI','fsMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('FS-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
fsSPANMIB=ModuleIdentity((1,3,6,1,4,1,52642,1,1,10,2,23))
if mibBuilder.loadTexts:fsSPANMIB.setRevisions(('2002-03-20 00:00',))
_FsSPANMIBObjects_ObjectIdentity=ObjectIdentity
fsSPANMIBObjects=_FsSPANMIBObjects_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,23,1))
_FsSPANSessionNum_Type=Integer32
_FsSPANSessionNum_Object=MibScalar
fsSPANSessionNum=_FsSPANSessionNum_Object((1,3,6,1,4,1,52642,1,1,10,2,23,1,1),_FsSPANSessionNum_Type())
fsSPANSessionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSPANSessionNum.setStatus(_A)
_FsSPANTable_Object=MibTable
fsSPANTable=_FsSPANTable_Object((1,3,6,1,4,1,52642,1,1,10,2,23,1,2))
if mibBuilder.loadTexts:fsSPANTable.setStatus(_A)
_FsSPANEntry_Object=MibTableRow
fsSPANEntry=_FsSPANEntry_Object((1,3,6,1,4,1,52642,1,1,10,2,23,1,2,1))
fsSPANEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:fsSPANEntry.setStatus(_A)
_FsSPANSession_Type=Integer32
_FsSPANSession_Object=MibTableColumn
fsSPANSession=_FsSPANSession_Object((1,3,6,1,4,1,52642,1,1,10,2,23,1,2,1,1),_FsSPANSession_Type())
fsSPANSession.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSPANSession.setStatus(_A)
_FsSPANIfIndex_Type=IfIndex
_FsSPANIfIndex_Object=MibTableColumn
fsSPANIfIndex=_FsSPANIfIndex_Object((1,3,6,1,4,1,52642,1,1,10,2,23,1,2,1,2),_FsSPANIfIndex_Type())
fsSPANIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:fsSPANIfIndex.setStatus(_A)
class _FsSPANIfRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('span-desc',1),('span-src-rx',2),('span-src-tx',3),('span-src-all',4)))
_FsSPANIfRole_Type.__name__=_F
_FsSPANIfRole_Object=MibTableColumn
fsSPANIfRole=_FsSPANIfRole_Object((1,3,6,1,4,1,52642,1,1,10,2,23,1,2,1,3),_FsSPANIfRole_Type())
fsSPANIfRole.setMaxAccess(_G)
if mibBuilder.loadTexts:fsSPANIfRole.setStatus(_A)
_FsSPANEntryStatus_Type=ConfigStatus
_FsSPANEntryStatus_Object=MibTableColumn
fsSPANEntryStatus=_FsSPANEntryStatus_Object((1,3,6,1,4,1,52642,1,1,10,2,23,1,2,1,4),_FsSPANEntryStatus_Type())
fsSPANEntryStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:fsSPANEntryStatus.setStatus(_A)
_FsSPANMIBConformance_ObjectIdentity=ObjectIdentity
fsSPANMIBConformance=_FsSPANMIBConformance_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,23,3))
_FsSPANMIBCompliances_ObjectIdentity=ObjectIdentity
fsSPANMIBCompliances=_FsSPANMIBCompliances_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,23,3,1))
_FsSPANMIBGroups_ObjectIdentity=ObjectIdentity
fsSPANMIBGroups=_FsSPANMIBGroups_ObjectIdentity((1,3,6,1,4,1,52642,1,1,10,2,23,3,2))
fsSPANMIBGroup=ObjectGroup((1,3,6,1,4,1,52642,1,1,10,2,23,3,2,1))
fsSPANMIBGroup.setObjects(*((_B,_D),(_B,_E),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:fsSPANMIBGroup.setStatus(_A)
fsSPANMIBCompliance=ModuleCompliance((1,3,6,1,4,1,52642,1,1,10,2,23,3,1,1))
fsSPANMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:fsSPANMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'fsSPANMIB':fsSPANMIB,'fsSPANMIBObjects':fsSPANMIBObjects,'fsSPANSessionNum':fsSPANSessionNum,'fsSPANTable':fsSPANTable,'fsSPANEntry':fsSPANEntry,_D:fsSPANSession,_E:fsSPANIfIndex,_H:fsSPANIfRole,_I:fsSPANEntryStatus,'fsSPANMIBConformance':fsSPANMIBConformance,'fsSPANMIBCompliances':fsSPANMIBCompliances,'fsSPANMIBCompliance':fsSPANMIBCompliance,'fsSPANMIBGroups':fsSPANMIBGroups,_J:fsSPANMIBGroup})