_P='shelfEntryIndex'
_O='nscEntryIndex'
_N='critical'
_M='hostEntryIndex'
_L='scellEntryIndex'
_K='degraded'
_J='agentEntryIndex'
_I='NotificationType'
_H='major'
_G='minor'
_F='informational'
_E='failed'
_D='CPQHSV300V9-MIB'
_C='Integer32'
_B='read-only'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,NotificationType,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_C,'IpAddress','ModuleIdentity','MibIdentifier',_I,'ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn',_I,'TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Compaq_ObjectIdentity=ObjectIdentity
compaq=_Compaq_ObjectIdentity((1,3,6,1,4,1,232))
_CpqElementManager_ObjectIdentity=ObjectIdentity
cpqElementManager=_CpqElementManager_ObjectIdentity((1,3,6,1,4,1,232,136))
_CpqHSV_ObjectIdentity=ObjectIdentity
cpqHSV=_CpqHSV_ObjectIdentity((1,3,6,1,4,1,232,136,1))
_CpqHSVAgent_ObjectIdentity=ObjectIdentity
cpqHSVAgent=_CpqHSVAgent_ObjectIdentity((1,3,6,1,4,1,232,136,1,1))
_AgManufacturer_Type=DisplayString
_AgManufacturer_Object=MibScalar
agManufacturer=_AgManufacturer_Object((1,3,6,1,4,1,232,136,1,1,1),_AgManufacturer_Type())
agManufacturer.setMaxAccess(_B)
if mibBuilder.loadTexts:agManufacturer.setStatus(_A)
_AgMajVersion_Type=Integer32
_AgMajVersion_Object=MibScalar
agMajVersion=_AgMajVersion_Object((1,3,6,1,4,1,232,136,1,1,2),_AgMajVersion_Type())
agMajVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agMajVersion.setStatus(_A)
_AgMinVersion_Type=Integer32
_AgMinVersion_Object=MibScalar
agMinVersion=_AgMinVersion_Object((1,3,6,1,4,1,232,136,1,1,3),_AgMinVersion_Type())
agMinVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:agMinVersion.setStatus(_A)
_AgHostName_Type=DisplayString
_AgHostName_Object=MibScalar
agHostName=_AgHostName_Object((1,3,6,1,4,1,232,136,1,1,4),_AgHostName_Type())
agHostName.setMaxAccess(_B)
if mibBuilder.loadTexts:agHostName.setStatus(_A)
_AgEnterprise_Type=ObjectIdentifier
_AgEnterprise_Object=MibScalar
agEnterprise=_AgEnterprise_Object((1,3,6,1,4,1,232,136,1,1,5),_AgEnterprise_Type())
agEnterprise.setMaxAccess(_B)
if mibBuilder.loadTexts:agEnterprise.setStatus(_A)
_AgDescription_Type=DisplayString
_AgDescription_Object=MibScalar
agDescription=_AgDescription_Object((1,3,6,1,4,1,232,136,1,1,6),_AgDescription_Type())
agDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:agDescription.setStatus(_A)
_AgStatusTable_Object=MibTable
agStatusTable=_AgStatusTable_Object((1,3,6,1,4,1,232,136,1,1,7))
if mibBuilder.loadTexts:agStatusTable.setStatus(_A)
_AgentEntry_Object=MibTableRow
agentEntry=_AgentEntry_Object((1,3,6,1,4,1,232,136,1,1,7,1))
agentEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:agentEntry.setStatus(_A)
_AgentEntryIndex_Type=Integer32
_AgentEntryIndex_Object=MibTableColumn
agentEntryIndex=_AgentEntryIndex_Object((1,3,6,1,4,1,232,136,1,1,7,1,1),_AgentEntryIndex_Type())
agentEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEntryIndex.setStatus(_A)
class _AgentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),(_K,3),(_E,4)))
_AgentStatus_Type.__name__=_C
_AgentStatus_Object=MibTableColumn
agentStatus=_AgentStatus_Object((1,3,6,1,4,1,232,136,1,1,7,1,2),_AgentStatus_Type())
agentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:agentStatus.setStatus(_A)
_AgentEventCode_Type=Integer32
_AgentEventCode_Object=MibTableColumn
agentEventCode=_AgentEventCode_Object((1,3,6,1,4,1,232,136,1,1,7,1,3),_AgentEventCode_Type())
agentEventCode.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEventCode.setStatus(_A)
_AgentEventLevel_Type=Integer32
_AgentEventLevel_Object=MibTableColumn
agentEventLevel=_AgentEventLevel_Object((1,3,6,1,4,1,232,136,1,1,7,1,4),_AgentEventLevel_Type())
agentEventLevel.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEventLevel.setStatus(_A)
_AgentEventTimeDate_Type=DisplayString
_AgentEventTimeDate_Object=MibTableColumn
agentEventTimeDate=_AgentEventTimeDate_Object((1,3,6,1,4,1,232,136,1,1,7,1,5),_AgentEventTimeDate_Type())
agentEventTimeDate.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEventTimeDate.setStatus(_A)
_AgentEventDescription_Type=DisplayString
_AgentEventDescription_Object=MibTableColumn
agentEventDescription=_AgentEventDescription_Object((1,3,6,1,4,1,232,136,1,1,7,1,6),_AgentEventDescription_Type())
agentEventDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:agentEventDescription.setStatus(_A)
_CpqHSVServer_ObjectIdentity=ObjectIdentity
cpqHSVServer=_CpqHSVServer_ObjectIdentity((1,3,6,1,4,1,232,136,1,2))
_SrvCPU_Type=DisplayString
_SrvCPU_Object=MibScalar
srvCPU=_SrvCPU_Object((1,3,6,1,4,1,232,136,1,2,1),_SrvCPU_Type())
srvCPU.setMaxAccess(_B)
if mibBuilder.loadTexts:srvCPU.setStatus(_A)
_SrvComputerType_Type=DisplayString
_SrvComputerType_Object=MibScalar
srvComputerType=_SrvComputerType_Object((1,3,6,1,4,1,232,136,1,2,2),_SrvComputerType_Type())
srvComputerType.setMaxAccess(_B)
if mibBuilder.loadTexts:srvComputerType.setStatus(_A)
_SrvModel_Type=Integer32
_SrvModel_Object=MibScalar
srvModel=_SrvModel_Object((1,3,6,1,4,1,232,136,1,2,3),_SrvModel_Type())
srvModel.setMaxAccess(_B)
if mibBuilder.loadTexts:srvModel.setStatus(_A)
_SrvSubModel_Type=Integer32
_SrvSubModel_Object=MibScalar
srvSubModel=_SrvSubModel_Object((1,3,6,1,4,1,232,136,1,2,4),_SrvSubModel_Type())
srvSubModel.setMaxAccess(_B)
if mibBuilder.loadTexts:srvSubModel.setStatus(_A)
_SrvBiosVersion_Type=DisplayString
_SrvBiosVersion_Object=MibScalar
srvBiosVersion=_SrvBiosVersion_Object((1,3,6,1,4,1,232,136,1,2,5),_SrvBiosVersion_Type())
srvBiosVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:srvBiosVersion.setStatus(_A)
_SrvOS_Type=DisplayString
_SrvOS_Object=MibScalar
srvOS=_SrvOS_Object((1,3,6,1,4,1,232,136,1,2,6),_SrvOS_Type())
srvOS.setMaxAccess(_B)
if mibBuilder.loadTexts:srvOS.setStatus(_A)
_SrvOSMajVersion_Type=Integer32
_SrvOSMajVersion_Object=MibScalar
srvOSMajVersion=_SrvOSMajVersion_Object((1,3,6,1,4,1,232,136,1,2,7),_SrvOSMajVersion_Type())
srvOSMajVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:srvOSMajVersion.setStatus(_A)
_SrvOSMinVersion_Type=Integer32
_SrvOSMinVersion_Object=MibScalar
srvOSMinVersion=_SrvOSMinVersion_Object((1,3,6,1,4,1,232,136,1,2,8),_SrvOSMinVersion_Type())
srvOSMinVersion.setMaxAccess(_B)
if mibBuilder.loadTexts:srvOSMinVersion.setStatus(_A)
_HsvObject_ObjectIdentity=ObjectIdentity
hsvObject=_HsvObject_ObjectIdentity((1,3,6,1,4,1,232,136,1,3))
_Scell_ObjectIdentity=ObjectIdentity
scell=_Scell_ObjectIdentity((1,3,6,1,4,1,232,136,1,3,1))
_ScellTotal_Type=Integer32
_ScellTotal_Object=MibScalar
scellTotal=_ScellTotal_Object((1,3,6,1,4,1,232,136,1,3,1,1),_ScellTotal_Type())
scellTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:scellTotal.setStatus(_A)
_ScellStatusTable_Object=MibTable
scellStatusTable=_ScellStatusTable_Object((1,3,6,1,4,1,232,136,1,3,1,2))
if mibBuilder.loadTexts:scellStatusTable.setStatus(_A)
_ScellEntry_Object=MibTableRow
scellEntry=_ScellEntry_Object((1,3,6,1,4,1,232,136,1,3,1,2,1))
scellEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:scellEntry.setStatus(_A)
_ScellEntryIndex_Type=Integer32
_ScellEntryIndex_Object=MibTableColumn
scellEntryIndex=_ScellEntryIndex_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,1),_ScellEntryIndex_Type())
scellEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:scellEntryIndex.setStatus(_A)
_ScellName_Type=DisplayString
_ScellName_Object=MibTableColumn
scellName=_ScellName_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,2),_ScellName_Type())
scellName.setMaxAccess(_B)
if mibBuilder.loadTexts:scellName.setStatus(_A)
_ScellUUID_Type=DisplayString
_ScellUUID_Object=MibTableColumn
scellUUID=_ScellUUID_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,3),_ScellUUID_Type())
scellUUID.setMaxAccess(_B)
if mibBuilder.loadTexts:scellUUID.setStatus(_A)
class _ScellStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*((_F,1),(_G,2),(_H,3),(_E,4)))
_ScellStatus_Type.__name__=_C
_ScellStatus_Object=MibTableColumn
scellStatus=_ScellStatus_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,4),_ScellStatus_Type())
scellStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:scellStatus.setStatus(_A)
_ScellEventDescription_Type=DisplayString
_ScellEventDescription_Object=MibTableColumn
scellEventDescription=_ScellEventDescription_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,5),_ScellEventDescription_Type())
scellEventDescription.setMaxAccess(_B)
if mibBuilder.loadTexts:scellEventDescription.setStatus(_A)
_ScellEventTimeDate_Type=DisplayString
_ScellEventTimeDate_Object=MibTableColumn
scellEventTimeDate=_ScellEventTimeDate_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,6),_ScellEventTimeDate_Type())
scellEventTimeDate.setMaxAccess(_B)
if mibBuilder.loadTexts:scellEventTimeDate.setStatus(_A)
_ScellEventCode_Type=DisplayString
_ScellEventCode_Object=MibTableColumn
scellEventCode=_ScellEventCode_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,7),_ScellEventCode_Type())
scellEventCode.setMaxAccess(_B)
if mibBuilder.loadTexts:scellEventCode.setStatus(_A)
_ScellSWComponent_Type=Integer32
_ScellSWComponent_Object=MibTableColumn
scellSWComponent=_ScellSWComponent_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,8),_ScellSWComponent_Type())
scellSWComponent.setMaxAccess(_B)
if mibBuilder.loadTexts:scellSWComponent.setStatus(_A)
_ScellECode_Type=Integer32
_ScellECode_Object=MibTableColumn
scellECode=_ScellECode_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,9),_ScellECode_Type())
scellECode.setMaxAccess(_B)
if mibBuilder.loadTexts:scellECode.setStatus(_A)
_ScellCAC_Type=Integer32
_ScellCAC_Object=MibTableColumn
scellCAC=_ScellCAC_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,10),_ScellCAC_Type())
scellCAC.setMaxAccess(_B)
if mibBuilder.loadTexts:scellCAC.setStatus(_A)
_ScellEIP_Type=Integer32
_ScellEIP_Object=MibTableColumn
scellEIP=_ScellEIP_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,11),_ScellEIP_Type())
scellEIP.setMaxAccess(_B)
if mibBuilder.loadTexts:scellEIP.setStatus(_A)
_ScellNameDateTime_Type=DisplayString
_ScellNameDateTime_Object=MibTableColumn
scellNameDateTime=_ScellNameDateTime_Object((1,3,6,1,4,1,232,136,1,3,1,2,1,12),_ScellNameDateTime_Type())
scellNameDateTime.setMaxAccess(_B)
if mibBuilder.loadTexts:scellNameDateTime.setStatus(_A)
_Agent_ObjectIdentity=ObjectIdentity
agent=_Agent_ObjectIdentity((1,3,6,1,4,1,232,136,1,3,2))
_Host_ObjectIdentity=ObjectIdentity
host=_Host_ObjectIdentity((1,3,6,1,4,1,232,136,1,3,3))
_HostTotal_Type=Integer32
_HostTotal_Object=MibScalar
hostTotal=_HostTotal_Object((1,3,6,1,4,1,232,136,1,3,3,1),_HostTotal_Type())
hostTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:hostTotal.setStatus(_A)
_HostStatusTable_Object=MibTable
hostStatusTable=_HostStatusTable_Object((1,3,6,1,4,1,232,136,1,3,3,2))
if mibBuilder.loadTexts:hostStatusTable.setStatus(_A)
_HostEntry_Object=MibTableRow
hostEntry=_HostEntry_Object((1,3,6,1,4,1,232,136,1,3,3,2,1))
hostEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:hostEntry.setStatus(_A)
_HostEntryIndex_Type=Integer32
_HostEntryIndex_Object=MibTableColumn
hostEntryIndex=_HostEntryIndex_Object((1,3,6,1,4,1,232,136,1,3,3,2,1,1),_HostEntryIndex_Type())
hostEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:hostEntryIndex.setStatus(_A)
_HostName_Type=DisplayString
_HostName_Object=MibTableColumn
hostName=_HostName_Object((1,3,6,1,4,1,232,136,1,3,3,2,1,2),_HostName_Type())
hostName.setMaxAccess(_B)
if mibBuilder.loadTexts:hostName.setStatus(_A)
_HostUUID_Type=DisplayString
_HostUUID_Object=MibTableColumn
hostUUID=_HostUUID_Object((1,3,6,1,4,1,232,136,1,3,3,2,1,3),_HostUUID_Type())
hostUUID.setMaxAccess(_B)
if mibBuilder.loadTexts:hostUUID.setStatus(_A)
class _HostStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_N,3)))
_HostStatus_Type.__name__=_C
_HostStatus_Object=MibTableColumn
hostStatus=_HostStatus_Object((1,3,6,1,4,1,232,136,1,3,3,2,1,4),_HostStatus_Type())
hostStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:hostStatus.setStatus(_A)
_Nsc_ObjectIdentity=ObjectIdentity
nsc=_Nsc_ObjectIdentity((1,3,6,1,4,1,232,136,1,3,4))
_NscTotal_Type=Integer32
_NscTotal_Object=MibScalar
nscTotal=_NscTotal_Object((1,3,6,1,4,1,232,136,1,3,4,1),_NscTotal_Type())
nscTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:nscTotal.setStatus(_A)
_NscStatusTable_Object=MibTable
nscStatusTable=_NscStatusTable_Object((1,3,6,1,4,1,232,136,1,3,4,2))
if mibBuilder.loadTexts:nscStatusTable.setStatus(_A)
_NscEntry_Object=MibTableRow
nscEntry=_NscEntry_Object((1,3,6,1,4,1,232,136,1,3,4,2,1))
nscEntry.setIndexNames((0,_D,_O))
if mibBuilder.loadTexts:nscEntry.setStatus(_A)
_NscEntryIndex_Type=Integer32
_NscEntryIndex_Object=MibTableColumn
nscEntryIndex=_NscEntryIndex_Object((1,3,6,1,4,1,232,136,1,3,4,2,1,1),_NscEntryIndex_Type())
nscEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:nscEntryIndex.setStatus(_A)
_NscName_Type=DisplayString
_NscName_Object=MibTableColumn
nscName=_NscName_Object((1,3,6,1,4,1,232,136,1,3,4,2,1,2),_NscName_Type())
nscName.setMaxAccess(_B)
if mibBuilder.loadTexts:nscName.setStatus(_A)
_NscUUID_Type=DisplayString
_NscUUID_Object=MibTableColumn
nscUUID=_NscUUID_Object((1,3,6,1,4,1,232,136,1,3,4,2,1,3),_NscUUID_Type())
nscUUID.setMaxAccess(_B)
if mibBuilder.loadTexts:nscUUID.setStatus(_A)
class _NscStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_F,0),(_G,1),(_H,2),(_N,3)))
_NscStatus_Type.__name__=_C
_NscStatus_Object=MibTableColumn
nscStatus=_NscStatus_Object((1,3,6,1,4,1,232,136,1,3,4,2,1,4),_NscStatus_Type())
nscStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:nscStatus.setStatus(_A)
_Shelf_ObjectIdentity=ObjectIdentity
shelf=_Shelf_ObjectIdentity((1,3,6,1,4,1,232,136,1,3,8))
_ShelfTotal_Type=Integer32
_ShelfTotal_Object=MibScalar
shelfTotal=_ShelfTotal_Object((1,3,6,1,4,1,232,136,1,3,8,1),_ShelfTotal_Type())
shelfTotal.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfTotal.setStatus(_A)
_ShelfStatusTable_Object=MibTable
shelfStatusTable=_ShelfStatusTable_Object((1,3,6,1,4,1,232,136,1,3,8,2))
if mibBuilder.loadTexts:shelfStatusTable.setStatus(_A)
_ShelfEntry_Object=MibTableRow
shelfEntry=_ShelfEntry_Object((1,3,6,1,4,1,232,136,1,3,8,2,1))
shelfEntry.setIndexNames((0,_D,_P))
if mibBuilder.loadTexts:shelfEntry.setStatus(_A)
_ShelfEntryIndex_Type=Integer32
_ShelfEntryIndex_Object=MibTableColumn
shelfEntryIndex=_ShelfEntryIndex_Object((1,3,6,1,4,1,232,136,1,3,8,2,1,1),_ShelfEntryIndex_Type())
shelfEntryIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfEntryIndex.setStatus(_A)
class _ShelfStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4)));namedValues=NamedValues(*(('other',1),('ok',2),(_K,3),(_E,4)))
_ShelfStatus_Type.__name__=_C
_ShelfStatus_Object=MibTableColumn
shelfStatus=_ShelfStatus_Object((1,3,6,1,4,1,232,136,1,3,8,2,1,2),_ShelfStatus_Type())
shelfStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfStatus.setStatus(_A)
_ShelfId_Type=Integer32
_ShelfId_Object=MibTableColumn
shelfId=_ShelfId_Object((1,3,6,1,4,1,232,136,1,3,8,2,1,3),_ShelfId_Type())
shelfId.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfId.setStatus(_A)
_ShelfElementType_Type=Integer32
_ShelfElementType_Object=MibTableColumn
shelfElementType=_ShelfElementType_Object((1,3,6,1,4,1,232,136,1,3,8,2,1,4),_ShelfElementType_Type())
shelfElementType.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfElementType.setStatus(_A)
_ShelfElementNum_Type=Integer32
_ShelfElementNum_Object=MibTableColumn
shelfElementNum=_ShelfElementNum_Object((1,3,6,1,4,1,232,136,1,3,8,2,1,5),_ShelfElementNum_Type())
shelfElementNum.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfElementNum.setStatus(_A)
_ShelfErrorCode_Type=Integer32
_ShelfErrorCode_Object=MibTableColumn
shelfErrorCode=_ShelfErrorCode_Object((1,3,6,1,4,1,232,136,1,3,8,2,1,6),_ShelfErrorCode_Type())
shelfErrorCode.setMaxAccess(_B)
if mibBuilder.loadTexts:shelfErrorCode.setStatus(_A)
_MaHSVMibRev_ObjectIdentity=ObjectIdentity
maHSVMibRev=_MaHSVMibRev_ObjectIdentity((1,3,6,1,4,1,232,136,1,4))
_MaHSVMibRevMajor_Type=Integer32
_MaHSVMibRevMajor_Object=MibScalar
maHSVMibRevMajor=_MaHSVMibRevMajor_Object((1,3,6,1,4,1,232,136,1,4,1),_MaHSVMibRevMajor_Type())
maHSVMibRevMajor.setMaxAccess(_B)
if mibBuilder.loadTexts:maHSVMibRevMajor.setStatus(_A)
_MaHSVMibRevMinor_Type=Integer32
_MaHSVMibRevMinor_Object=MibScalar
maHSVMibRevMinor=_MaHSVMibRevMinor_Object((1,3,6,1,4,1,232,136,1,4,2),_MaHSVMibRevMinor_Type())
maHSVMibRevMinor.setMaxAccess(_B)
if mibBuilder.loadTexts:maHSVMibRevMinor.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'compaq':compaq,'cpqElementManager':cpqElementManager,'cpqHSV':cpqHSV,'cpqHSVAgent':cpqHSVAgent,'agManufacturer':agManufacturer,'agMajVersion':agMajVersion,'agMinVersion':agMinVersion,'agHostName':agHostName,'agEnterprise':agEnterprise,'agDescription':agDescription,'agStatusTable':agStatusTable,'agentEntry':agentEntry,_J:agentEntryIndex,'agentStatus':agentStatus,'agentEventCode':agentEventCode,'agentEventLevel':agentEventLevel,'agentEventTimeDate':agentEventTimeDate,'agentEventDescription':agentEventDescription,'cpqHSVServer':cpqHSVServer,'srvCPU':srvCPU,'srvComputerType':srvComputerType,'srvModel':srvModel,'srvSubModel':srvSubModel,'srvBiosVersion':srvBiosVersion,'srvOS':srvOS,'srvOSMajVersion':srvOSMajVersion,'srvOSMinVersion':srvOSMinVersion,'hsvObject':hsvObject,'scell':scell,'scellTotal':scellTotal,'scellStatusTable':scellStatusTable,'scellEntry':scellEntry,_L:scellEntryIndex,'scellName':scellName,'scellUUID':scellUUID,'scellStatus':scellStatus,'scellEventDescription':scellEventDescription,'scellEventTimeDate':scellEventTimeDate,'scellEventCode':scellEventCode,'scellSWComponent':scellSWComponent,'scellECode':scellECode,'scellCAC':scellCAC,'scellEIP':scellEIP,'scellNameDateTime':scellNameDateTime,'agent':agent,'host':host,'hostTotal':hostTotal,'hostStatusTable':hostStatusTable,'hostEntry':hostEntry,_M:hostEntryIndex,'hostName':hostName,'hostUUID':hostUUID,'hostStatus':hostStatus,'nsc':nsc,'nscTotal':nscTotal,'nscStatusTable':nscStatusTable,'nscEntry':nscEntry,_O:nscEntryIndex,'nscName':nscName,'nscUUID':nscUUID,'nscStatus':nscStatus,'shelf':shelf,'shelfTotal':shelfTotal,'shelfStatusTable':shelfStatusTable,'shelfEntry':shelfEntry,_P:shelfEntryIndex,'shelfStatus':shelfStatus,'shelfId':shelfId,'shelfElementType':shelfElementType,'shelfElementNum':shelfElementNum,'shelfErrorCode':shelfErrorCode,'maHSVMibRev':maHSVMibRev,'maHSVMibRevMajor':maHSVMibRevMajor,'maHSVMibRevMinor':maHSVMibRevMinor})