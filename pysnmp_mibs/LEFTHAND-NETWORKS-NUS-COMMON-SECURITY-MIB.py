_L='secAdminGroupAccessIndex'
_K='secAdminGroupUserOrSubGroupIndex'
_J='secAdminUserIndex'
_I='secGroupUserIndex'
_H='secUserIndex'
_G='secGroupIndex'
_F='secAdminGroupIndex'
_E='read-only'
_D='read-write'
_C='LEFTHAND-NETWORKS-NUS-COMMON-SECURITY-MIB'
_B='read-create'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
lhnModules,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-GLOBAL-REG','lhnModules')
lhnNusCommonSecurity,=mibBuilder.importSymbols('LEFTHAND-NETWORKS-NUS-COMMON-MIB','lhnNusCommonSecurity')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32','Integer32','IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention,TruthValue=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','RowStatus','TextualConvention','TruthValue')
lhnNusCommonSecurityModule=ModuleIdentity((1,3,6,1,4,1,9804,1,1,10))
_SecUserCount_Type=Integer32
_SecUserCount_Object=MibScalar
secUserCount=_SecUserCount_Object((1,3,6,1,4,1,9804,3,1,1,2,11,1),_SecUserCount_Type())
secUserCount.setMaxAccess(_E)
if mibBuilder.loadTexts:secUserCount.setStatus(_A)
_SecUserTable_Object=MibTable
secUserTable=_SecUserTable_Object((1,3,6,1,4,1,9804,3,1,1,2,11,2))
if mibBuilder.loadTexts:secUserTable.setStatus(_A)
_SecUserEntry_Object=MibTableRow
secUserEntry=_SecUserEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,11,2,1))
secUserEntry.setIndexNames((0,_C,_H))
if mibBuilder.loadTexts:secUserEntry.setStatus(_A)
_SecUserIndex_Type=Integer32
_SecUserIndex_Object=MibTableColumn
secUserIndex=_SecUserIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,11,2,1,1),_SecUserIndex_Type())
secUserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:secUserIndex.setStatus(_A)
_SecUserName_Type=OctetString
_SecUserName_Object=MibTableColumn
secUserName=_SecUserName_Object((1,3,6,1,4,1,9804,3,1,1,2,11,2,1,2),_SecUserName_Type())
secUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:secUserName.setStatus(_A)
_SecUserDesc_Type=OctetString
_SecUserDesc_Object=MibTableColumn
secUserDesc=_SecUserDesc_Object((1,3,6,1,4,1,9804,3,1,1,2,11,2,1,3),_SecUserDesc_Type())
secUserDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:secUserDesc.setStatus(_A)
_SecUserPasswd_Type=OctetString
_SecUserPasswd_Object=MibTableColumn
secUserPasswd=_SecUserPasswd_Object((1,3,6,1,4,1,9804,3,1,1,2,11,2,1,4),_SecUserPasswd_Type())
secUserPasswd.setMaxAccess(_D)
if mibBuilder.loadTexts:secUserPasswd.setStatus(_A)
_SecUserRowStatus_Type=RowStatus
_SecUserRowStatus_Object=MibTableColumn
secUserRowStatus=_SecUserRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,11,2,1,5),_SecUserRowStatus_Type())
secUserRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:secUserRowStatus.setStatus(_A)
_SecGroupCount_Type=Integer32
_SecGroupCount_Object=MibScalar
secGroupCount=_SecGroupCount_Object((1,3,6,1,4,1,9804,3,1,1,2,11,3),_SecGroupCount_Type())
secGroupCount.setMaxAccess(_E)
if mibBuilder.loadTexts:secGroupCount.setStatus(_A)
_SecGroupTable_Object=MibTable
secGroupTable=_SecGroupTable_Object((1,3,6,1,4,1,9804,3,1,1,2,11,4))
if mibBuilder.loadTexts:secGroupTable.setStatus(_A)
_SecGroupEntry_Object=MibTableRow
secGroupEntry=_SecGroupEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,11,4,1))
secGroupEntry.setIndexNames((0,_C,_G))
if mibBuilder.loadTexts:secGroupEntry.setStatus(_A)
_SecGroupIndex_Type=Integer32
_SecGroupIndex_Object=MibTableColumn
secGroupIndex=_SecGroupIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,11,4,1,1),_SecGroupIndex_Type())
secGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:secGroupIndex.setStatus(_A)
_SecGroupName_Type=OctetString
_SecGroupName_Object=MibTableColumn
secGroupName=_SecGroupName_Object((1,3,6,1,4,1,9804,3,1,1,2,11,4,1,2),_SecGroupName_Type())
secGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:secGroupName.setStatus(_A)
_SecGroupDesc_Type=OctetString
_SecGroupDesc_Object=MibTableColumn
secGroupDesc=_SecGroupDesc_Object((1,3,6,1,4,1,9804,3,1,1,2,11,4,1,3),_SecGroupDesc_Type())
secGroupDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:secGroupDesc.setStatus(_A)
_SecGroupUserCount_Type=Integer32
_SecGroupUserCount_Object=MibTableColumn
secGroupUserCount=_SecGroupUserCount_Object((1,3,6,1,4,1,9804,3,1,1,2,11,4,1,4),_SecGroupUserCount_Type())
secGroupUserCount.setMaxAccess(_D)
if mibBuilder.loadTexts:secGroupUserCount.setStatus(_A)
_SecGroupRowStatus_Type=RowStatus
_SecGroupRowStatus_Object=MibTableColumn
secGroupRowStatus=_SecGroupRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,11,4,1,5),_SecGroupRowStatus_Type())
secGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:secGroupRowStatus.setStatus(_A)
_SecGroupUserTable_Object=MibTable
secGroupUserTable=_SecGroupUserTable_Object((1,3,6,1,4,1,9804,3,1,1,2,11,5))
if mibBuilder.loadTexts:secGroupUserTable.setStatus(_A)
_SecGroupUserEntry_Object=MibTableRow
secGroupUserEntry=_SecGroupUserEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,11,5,1))
secGroupUserEntry.setIndexNames((0,_C,_G),(0,_C,_I))
if mibBuilder.loadTexts:secGroupUserEntry.setStatus(_A)
_SecGroupUserIndex_Type=Integer32
_SecGroupUserIndex_Object=MibTableColumn
secGroupUserIndex=_SecGroupUserIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,11,5,1,1),_SecGroupUserIndex_Type())
secGroupUserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:secGroupUserIndex.setStatus(_A)
_SecGroupUserName_Type=OctetString
_SecGroupUserName_Object=MibTableColumn
secGroupUserName=_SecGroupUserName_Object((1,3,6,1,4,1,9804,3,1,1,2,11,5,1,2),_SecGroupUserName_Type())
secGroupUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:secGroupUserName.setStatus(_A)
_SecGroupUserRowStatus_Type=RowStatus
_SecGroupUserRowStatus_Object=MibTableColumn
secGroupUserRowStatus=_SecGroupUserRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,11,5,1,3),_SecGroupUserRowStatus_Type())
secGroupUserRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:secGroupUserRowStatus.setStatus(_A)
_SecAdminUserCount_Type=Integer32
_SecAdminUserCount_Object=MibScalar
secAdminUserCount=_SecAdminUserCount_Object((1,3,6,1,4,1,9804,3,1,1,2,11,6),_SecAdminUserCount_Type())
secAdminUserCount.setMaxAccess(_E)
if mibBuilder.loadTexts:secAdminUserCount.setStatus(_A)
_SecAdminUserTable_Object=MibTable
secAdminUserTable=_SecAdminUserTable_Object((1,3,6,1,4,1,9804,3,1,1,2,11,7))
if mibBuilder.loadTexts:secAdminUserTable.setStatus(_A)
_SecAdminUserEntry_Object=MibTableRow
secAdminUserEntry=_SecAdminUserEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,11,7,1))
secAdminUserEntry.setIndexNames((0,_C,_J))
if mibBuilder.loadTexts:secAdminUserEntry.setStatus(_A)
_SecAdminUserIndex_Type=Integer32
_SecAdminUserIndex_Object=MibTableColumn
secAdminUserIndex=_SecAdminUserIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,11,7,1,1),_SecAdminUserIndex_Type())
secAdminUserIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminUserIndex.setStatus(_A)
_SecAdminUserName_Type=OctetString
_SecAdminUserName_Object=MibTableColumn
secAdminUserName=_SecAdminUserName_Object((1,3,6,1,4,1,9804,3,1,1,2,11,7,1,2),_SecAdminUserName_Type())
secAdminUserName.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminUserName.setStatus(_A)
_SecAdminUserDesc_Type=OctetString
_SecAdminUserDesc_Object=MibTableColumn
secAdminUserDesc=_SecAdminUserDesc_Object((1,3,6,1,4,1,9804,3,1,1,2,11,7,1,3),_SecAdminUserDesc_Type())
secAdminUserDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:secAdminUserDesc.setStatus(_A)
_SecAdminUserPasswd_Type=OctetString
_SecAdminUserPasswd_Object=MibTableColumn
secAdminUserPasswd=_SecAdminUserPasswd_Object((1,3,6,1,4,1,9804,3,1,1,2,11,7,1,4),_SecAdminUserPasswd_Type())
secAdminUserPasswd.setMaxAccess(_D)
if mibBuilder.loadTexts:secAdminUserPasswd.setStatus(_A)
_SecAdminUserRowStatus_Type=RowStatus
_SecAdminUserRowStatus_Object=MibTableColumn
secAdminUserRowStatus=_SecAdminUserRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,11,7,1,5),_SecAdminUserRowStatus_Type())
secAdminUserRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminUserRowStatus.setStatus(_A)
_SecAdminGroupCount_Type=Integer32
_SecAdminGroupCount_Object=MibScalar
secAdminGroupCount=_SecAdminGroupCount_Object((1,3,6,1,4,1,9804,3,1,1,2,11,8),_SecAdminGroupCount_Type())
secAdminGroupCount.setMaxAccess(_E)
if mibBuilder.loadTexts:secAdminGroupCount.setStatus(_A)
_SecAdminGroupTable_Object=MibTable
secAdminGroupTable=_SecAdminGroupTable_Object((1,3,6,1,4,1,9804,3,1,1,2,11,9))
if mibBuilder.loadTexts:secAdminGroupTable.setStatus(_A)
_SecAdminGroupEntry_Object=MibTableRow
secAdminGroupEntry=_SecAdminGroupEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,11,9,1))
secAdminGroupEntry.setIndexNames((0,_C,_F))
if mibBuilder.loadTexts:secAdminGroupEntry.setStatus(_A)
_SecAdminGroupIndex_Type=Integer32
_SecAdminGroupIndex_Object=MibTableColumn
secAdminGroupIndex=_SecAdminGroupIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,11,9,1,1),_SecAdminGroupIndex_Type())
secAdminGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminGroupIndex.setStatus(_A)
_SecAdminGroupName_Type=OctetString
_SecAdminGroupName_Object=MibTableColumn
secAdminGroupName=_SecAdminGroupName_Object((1,3,6,1,4,1,9804,3,1,1,2,11,9,1,2),_SecAdminGroupName_Type())
secAdminGroupName.setMaxAccess(_D)
if mibBuilder.loadTexts:secAdminGroupName.setStatus(_A)
_SecAdminGroupDesc_Type=OctetString
_SecAdminGroupDesc_Object=MibTableColumn
secAdminGroupDesc=_SecAdminGroupDesc_Object((1,3,6,1,4,1,9804,3,1,1,2,11,9,1,3),_SecAdminGroupDesc_Type())
secAdminGroupDesc.setMaxAccess(_D)
if mibBuilder.loadTexts:secAdminGroupDesc.setStatus(_A)
_SecAdminGroupUserOrSubGroupCount_Type=Integer32
_SecAdminGroupUserOrSubGroupCount_Object=MibTableColumn
secAdminGroupUserOrSubGroupCount=_SecAdminGroupUserOrSubGroupCount_Object((1,3,6,1,4,1,9804,3,1,1,2,11,9,1,4),_SecAdminGroupUserOrSubGroupCount_Type())
secAdminGroupUserOrSubGroupCount.setMaxAccess(_D)
if mibBuilder.loadTexts:secAdminGroupUserOrSubGroupCount.setStatus(_A)
_SecAdminGroupRowStatus_Type=RowStatus
_SecAdminGroupRowStatus_Object=MibTableColumn
secAdminGroupRowStatus=_SecAdminGroupRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,11,9,1,5),_SecAdminGroupRowStatus_Type())
secAdminGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminGroupRowStatus.setStatus(_A)
_SecAdminGroupUserOrSubGroupTable_Object=MibTable
secAdminGroupUserOrSubGroupTable=_SecAdminGroupUserOrSubGroupTable_Object((1,3,6,1,4,1,9804,3,1,1,2,11,10))
if mibBuilder.loadTexts:secAdminGroupUserOrSubGroupTable.setStatus(_A)
_SecAdminGroupUserOrSubGroupEntry_Object=MibTableRow
secAdminGroupUserOrSubGroupEntry=_SecAdminGroupUserOrSubGroupEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,11,10,1))
secAdminGroupUserOrSubGroupEntry.setIndexNames((0,_C,_F),(0,_C,_K))
if mibBuilder.loadTexts:secAdminGroupUserOrSubGroupEntry.setStatus(_A)
_SecAdminGroupUserOrSubGroupIndex_Type=Integer32
_SecAdminGroupUserOrSubGroupIndex_Object=MibTableColumn
secAdminGroupUserOrSubGroupIndex=_SecAdminGroupUserOrSubGroupIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,11,10,1,1),_SecAdminGroupUserOrSubGroupIndex_Type())
secAdminGroupUserOrSubGroupIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminGroupUserOrSubGroupIndex.setStatus(_A)
_SecAdminGroupUserOrSubGroupName_Type=OctetString
_SecAdminGroupUserOrSubGroupName_Object=MibTableColumn
secAdminGroupUserOrSubGroupName=_SecAdminGroupUserOrSubGroupName_Object((1,3,6,1,4,1,9804,3,1,1,2,11,10,1,2),_SecAdminGroupUserOrSubGroupName_Type())
secAdminGroupUserOrSubGroupName.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminGroupUserOrSubGroupName.setStatus(_A)
_SecAdminGroupUserOrSubGroupRowStatus_Type=RowStatus
_SecAdminGroupUserOrSubGroupRowStatus_Object=MibTableColumn
secAdminGroupUserOrSubGroupRowStatus=_SecAdminGroupUserOrSubGroupRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,11,10,1,3),_SecAdminGroupUserOrSubGroupRowStatus_Type())
secAdminGroupUserOrSubGroupRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminGroupUserOrSubGroupRowStatus.setStatus(_A)
_SecAdminGroupAccessTable_Object=MibTable
secAdminGroupAccessTable=_SecAdminGroupAccessTable_Object((1,3,6,1,4,1,9804,3,1,1,2,11,11))
if mibBuilder.loadTexts:secAdminGroupAccessTable.setStatus(_A)
_SecAdminGroupAccessEntry_Object=MibTableRow
secAdminGroupAccessEntry=_SecAdminGroupAccessEntry_Object((1,3,6,1,4,1,9804,3,1,1,2,11,11,1))
secAdminGroupAccessEntry.setIndexNames((0,_C,_F),(0,_C,_L))
if mibBuilder.loadTexts:secAdminGroupAccessEntry.setStatus(_A)
_SecAdminGroupAccessIndex_Type=Integer32
_SecAdminGroupAccessIndex_Object=MibTableColumn
secAdminGroupAccessIndex=_SecAdminGroupAccessIndex_Object((1,3,6,1,4,1,9804,3,1,1,2,11,11,1,1),_SecAdminGroupAccessIndex_Type())
secAdminGroupAccessIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminGroupAccessIndex.setStatus(_A)
_SecAdminGroupAccessKey_Type=OctetString
_SecAdminGroupAccessKey_Object=MibTableColumn
secAdminGroupAccessKey=_SecAdminGroupAccessKey_Object((1,3,6,1,4,1,9804,3,1,1,2,11,11,1,2),_SecAdminGroupAccessKey_Type())
secAdminGroupAccessKey.setMaxAccess(_D)
if mibBuilder.loadTexts:secAdminGroupAccessKey.setStatus(_A)
class _SecAdminGroupAccessMode_Type(Bits):namedValues=NamedValues(*(('get',0),('set',1),('add',2),('delete',3)))
_SecAdminGroupAccessMode_Type.__name__='Bits'
_SecAdminGroupAccessMode_Object=MibTableColumn
secAdminGroupAccessMode=_SecAdminGroupAccessMode_Object((1,3,6,1,4,1,9804,3,1,1,2,11,11,1,3),_SecAdminGroupAccessMode_Type())
secAdminGroupAccessMode.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminGroupAccessMode.setStatus(_A)
_SecAdminGroupAccessRowStatus_Type=RowStatus
_SecAdminGroupAccessRowStatus_Object=MibTableColumn
secAdminGroupAccessRowStatus=_SecAdminGroupAccessRowStatus_Object((1,3,6,1,4,1,9804,3,1,1,2,11,11,1,4),_SecAdminGroupAccessRowStatus_Type())
secAdminGroupAccessRowStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:secAdminGroupAccessRowStatus.setStatus(_A)
mibBuilder.exportSymbols(_C,**{'lhnNusCommonSecurityModule':lhnNusCommonSecurityModule,'secUserCount':secUserCount,'secUserTable':secUserTable,'secUserEntry':secUserEntry,_H:secUserIndex,'secUserName':secUserName,'secUserDesc':secUserDesc,'secUserPasswd':secUserPasswd,'secUserRowStatus':secUserRowStatus,'secGroupCount':secGroupCount,'secGroupTable':secGroupTable,'secGroupEntry':secGroupEntry,_G:secGroupIndex,'secGroupName':secGroupName,'secGroupDesc':secGroupDesc,'secGroupUserCount':secGroupUserCount,'secGroupRowStatus':secGroupRowStatus,'secGroupUserTable':secGroupUserTable,'secGroupUserEntry':secGroupUserEntry,_I:secGroupUserIndex,'secGroupUserName':secGroupUserName,'secGroupUserRowStatus':secGroupUserRowStatus,'secAdminUserCount':secAdminUserCount,'secAdminUserTable':secAdminUserTable,'secAdminUserEntry':secAdminUserEntry,_J:secAdminUserIndex,'secAdminUserName':secAdminUserName,'secAdminUserDesc':secAdminUserDesc,'secAdminUserPasswd':secAdminUserPasswd,'secAdminUserRowStatus':secAdminUserRowStatus,'secAdminGroupCount':secAdminGroupCount,'secAdminGroupTable':secAdminGroupTable,'secAdminGroupEntry':secAdminGroupEntry,_F:secAdminGroupIndex,'secAdminGroupName':secAdminGroupName,'secAdminGroupDesc':secAdminGroupDesc,'secAdminGroupUserOrSubGroupCount':secAdminGroupUserOrSubGroupCount,'secAdminGroupRowStatus':secAdminGroupRowStatus,'secAdminGroupUserOrSubGroupTable':secAdminGroupUserOrSubGroupTable,'secAdminGroupUserOrSubGroupEntry':secAdminGroupUserOrSubGroupEntry,_K:secAdminGroupUserOrSubGroupIndex,'secAdminGroupUserOrSubGroupName':secAdminGroupUserOrSubGroupName,'secAdminGroupUserOrSubGroupRowStatus':secAdminGroupUserOrSubGroupRowStatus,'secAdminGroupAccessTable':secAdminGroupAccessTable,'secAdminGroupAccessEntry':secAdminGroupAccessEntry,_L:secAdminGroupAccessIndex,'secAdminGroupAccessKey':secAdminGroupAccessKey,'secAdminGroupAccessMode':secAdminGroupAccessMode,'secAdminGroupAccessRowStatus':secAdminGroupAccessRowStatus})