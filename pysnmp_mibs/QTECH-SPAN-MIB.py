_J='qtechSPANMIBGroup'
_I='qtechSPANEntryStatus'
_H='qtechSPANIfRole'
_G='read-create'
_F='Integer32'
_E='qtechSPANIfIndex'
_D='qtechSPANSession'
_C='read-only'
_B='QTECH-SPAN-MIB'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
qtechMgmt,=mibBuilder.importSymbols('QTECH-SMI','qtechMgmt')
ConfigStatus,IfIndex=mibBuilder.importSymbols('QTECH-TC','ConfigStatus','IfIndex')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_F,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
qtechSPANMIB=ModuleIdentity((1,3,6,1,4,1,27514,1,1,10,2,23))
if mibBuilder.loadTexts:qtechSPANMIB.setRevisions(('2002-03-20 00:00',))
_QtechSPANMIBObjects_ObjectIdentity=ObjectIdentity
qtechSPANMIBObjects=_QtechSPANMIBObjects_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,23,1))
_QtechSPANSessionNum_Type=Integer32
_QtechSPANSessionNum_Object=MibScalar
qtechSPANSessionNum=_QtechSPANSessionNum_Object((1,3,6,1,4,1,27514,1,1,10,2,23,1,1),_QtechSPANSessionNum_Type())
qtechSPANSessionNum.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSPANSessionNum.setStatus(_A)
_QtechSPANTable_Object=MibTable
qtechSPANTable=_QtechSPANTable_Object((1,3,6,1,4,1,27514,1,1,10,2,23,1,2))
if mibBuilder.loadTexts:qtechSPANTable.setStatus(_A)
_QtechSPANEntry_Object=MibTableRow
qtechSPANEntry=_QtechSPANEntry_Object((1,3,6,1,4,1,27514,1,1,10,2,23,1,2,1))
qtechSPANEntry.setIndexNames((0,_B,_D),(0,_B,_E))
if mibBuilder.loadTexts:qtechSPANEntry.setStatus(_A)
_QtechSPANSession_Type=Integer32
_QtechSPANSession_Object=MibTableColumn
qtechSPANSession=_QtechSPANSession_Object((1,3,6,1,4,1,27514,1,1,10,2,23,1,2,1,1),_QtechSPANSession_Type())
qtechSPANSession.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSPANSession.setStatus(_A)
_QtechSPANIfIndex_Type=IfIndex
_QtechSPANIfIndex_Object=MibTableColumn
qtechSPANIfIndex=_QtechSPANIfIndex_Object((1,3,6,1,4,1,27514,1,1,10,2,23,1,2,1,2),_QtechSPANIfIndex_Type())
qtechSPANIfIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:qtechSPANIfIndex.setStatus(_A)
class _QtechSPANIfRole_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('span-desc',1),('span-src-rx',2),('span-src-tx',3),('span-src-all',4)))
_QtechSPANIfRole_Type.__name__=_F
_QtechSPANIfRole_Object=MibTableColumn
qtechSPANIfRole=_QtechSPANIfRole_Object((1,3,6,1,4,1,27514,1,1,10,2,23,1,2,1,3),_QtechSPANIfRole_Type())
qtechSPANIfRole.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechSPANIfRole.setStatus(_A)
_QtechSPANEntryStatus_Type=ConfigStatus
_QtechSPANEntryStatus_Object=MibTableColumn
qtechSPANEntryStatus=_QtechSPANEntryStatus_Object((1,3,6,1,4,1,27514,1,1,10,2,23,1,2,1,4),_QtechSPANEntryStatus_Type())
qtechSPANEntryStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:qtechSPANEntryStatus.setStatus(_A)
_QtechSPANMIBConformance_ObjectIdentity=ObjectIdentity
qtechSPANMIBConformance=_QtechSPANMIBConformance_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,23,3))
_QtechSPANMIBCompliances_ObjectIdentity=ObjectIdentity
qtechSPANMIBCompliances=_QtechSPANMIBCompliances_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,23,3,1))
_QtechSPANMIBGroups_ObjectIdentity=ObjectIdentity
qtechSPANMIBGroups=_QtechSPANMIBGroups_ObjectIdentity((1,3,6,1,4,1,27514,1,1,10,2,23,3,2))
qtechSPANMIBGroup=ObjectGroup((1,3,6,1,4,1,27514,1,1,10,2,23,3,2,1))
qtechSPANMIBGroup.setObjects(*((_B,_D),(_B,_E),(_B,_H),(_B,_I)))
if mibBuilder.loadTexts:qtechSPANMIBGroup.setStatus(_A)
qtechSPANMIBCompliance=ModuleCompliance((1,3,6,1,4,1,27514,1,1,10,2,23,3,1,1))
qtechSPANMIBCompliance.setObjects((_B,_J))
if mibBuilder.loadTexts:qtechSPANMIBCompliance.setStatus(_A)
mibBuilder.exportSymbols(_B,**{'qtechSPANMIB':qtechSPANMIB,'qtechSPANMIBObjects':qtechSPANMIBObjects,'qtechSPANSessionNum':qtechSPANSessionNum,'qtechSPANTable':qtechSPANTable,'qtechSPANEntry':qtechSPANEntry,_D:qtechSPANSession,_E:qtechSPANIfIndex,_H:qtechSPANIfRole,_I:qtechSPANEntryStatus,'qtechSPANMIBConformance':qtechSPANMIBConformance,'qtechSPANMIBCompliances':qtechSPANMIBCompliances,'qtechSPANMIBCompliance':qtechSPANMIBCompliance,'qtechSPANMIBGroups':qtechSPANMIBGroups,_J:qtechSPANMIBGroup})