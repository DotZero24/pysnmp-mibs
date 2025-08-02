_L='sunSubTreeDispatchIndex'
_K='sunSubTreeDispatchAgentID'
_J='sunSubTreeIndex'
_I='sunSubTreeAgentID'
_H='sunSubAgentID'
_G='inactive'
_F='active'
_E='SUN-MASTER-AGENT-MIB'
_D='Integer32'
_C='read-only'
_B='read-write'
_A='mandatory'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_D,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
_Sun_ObjectIdentity=ObjectIdentity
sun=_Sun_ObjectIdentity((1,3,6,1,4,1,42))
_Products_ObjectIdentity=ObjectIdentity
products=_Products_ObjectIdentity((1,3,6,1,4,1,42,2))
_SunMasterAgent_ObjectIdentity=ObjectIdentity
sunMasterAgent=_SunMasterAgent_ObjectIdentity((1,3,6,1,4,1,42,2,15))
_SunMasterAgentStatusFile_Type=DisplayString
_SunMasterAgentStatusFile_Object=MibScalar
sunMasterAgentStatusFile=_SunMasterAgentStatusFile_Object((1,3,6,1,4,1,42,2,15,1),_SunMasterAgentStatusFile_Type())
sunMasterAgentStatusFile.setMaxAccess(_C)
if mibBuilder.loadTexts:sunMasterAgentStatusFile.setStatus(_A)
_SunMasterAgentResourceConfigFile_Type=DisplayString
_SunMasterAgentResourceConfigFile_Object=MibScalar
sunMasterAgentResourceConfigFile=_SunMasterAgentResourceConfigFile_Object((1,3,6,1,4,1,42,2,15,2),_SunMasterAgentResourceConfigFile_Type())
sunMasterAgentResourceConfigFile.setMaxAccess(_C)
if mibBuilder.loadTexts:sunMasterAgentResourceConfigFile.setStatus(_A)
_SunMasterAgentConfigurationDir_Type=DisplayString
_SunMasterAgentConfigurationDir_Object=MibScalar
sunMasterAgentConfigurationDir=_SunMasterAgentConfigurationDir_Object((1,3,6,1,4,1,42,2,15,3),_SunMasterAgentConfigurationDir_Type())
sunMasterAgentConfigurationDir.setMaxAccess(_C)
if mibBuilder.loadTexts:sunMasterAgentConfigurationDir.setStatus(_A)
_SunMasterAgentTrapPort_Type=Integer32
_SunMasterAgentTrapPort_Object=MibScalar
sunMasterAgentTrapPort=_SunMasterAgentTrapPort_Object((1,3,6,1,4,1,42,2,15,4),_SunMasterAgentTrapPort_Type())
sunMasterAgentTrapPort.setMaxAccess(_C)
if mibBuilder.loadTexts:sunMasterAgentTrapPort.setStatus(_A)
_SunCheckSubAgentName_Type=DisplayString
_SunCheckSubAgentName_Object=MibScalar
sunCheckSubAgentName=_SunCheckSubAgentName_Object((1,3,6,1,4,1,42,2,15,5),_SunCheckSubAgentName_Type())
sunCheckSubAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:sunCheckSubAgentName.setStatus(_A)
_SunMasterAgentPollInterval_Type=Integer32
_SunMasterAgentPollInterval_Object=MibScalar
sunMasterAgentPollInterval=_SunMasterAgentPollInterval_Object((1,3,6,1,4,1,42,2,15,6),_SunMasterAgentPollInterval_Type())
sunMasterAgentPollInterval.setMaxAccess(_C)
if mibBuilder.loadTexts:sunMasterAgentPollInterval.setStatus(_A)
_SunMasterAgentMaxAgentTimeOut_Type=Integer32
_SunMasterAgentMaxAgentTimeOut_Object=MibScalar
sunMasterAgentMaxAgentTimeOut=_SunMasterAgentMaxAgentTimeOut_Object((1,3,6,1,4,1,42,2,15,7),_SunMasterAgentMaxAgentTimeOut_Type())
sunMasterAgentMaxAgentTimeOut.setMaxAccess(_C)
if mibBuilder.loadTexts:sunMasterAgentMaxAgentTimeOut.setStatus(_A)
_SunSubAgentTable_Object=MibTable
sunSubAgentTable=_SunSubAgentTable_Object((1,3,6,1,4,1,42,2,15,8))
if mibBuilder.loadTexts:sunSubAgentTable.setStatus(_A)
_SunSubAgentEntry_Object=MibTableRow
sunSubAgentEntry=_SunSubAgentEntry_Object((1,3,6,1,4,1,42,2,15,8,1))
sunSubAgentEntry.setIndexNames((0,_E,_H))
if mibBuilder.loadTexts:sunSubAgentEntry.setStatus(_A)
_SunSubAgentID_Type=Integer32
_SunSubAgentID_Object=MibTableColumn
sunSubAgentID=_SunSubAgentID_Object((1,3,6,1,4,1,42,2,15,8,1,1),_SunSubAgentID_Type())
sunSubAgentID.setMaxAccess(_C)
if mibBuilder.loadTexts:sunSubAgentID.setStatus(_A)
class _SunSubAgentStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5)));namedValues=NamedValues(*(('init',1),('load',2),(_F,3),(_G,4),('destroy',5)))
_SunSubAgentStatus_Type.__name__=_D
_SunSubAgentStatus_Object=MibTableColumn
sunSubAgentStatus=_SunSubAgentStatus_Object((1,3,6,1,4,1,42,2,15,8,1,2),_SunSubAgentStatus_Type())
sunSubAgentStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentStatus.setStatus(_A)
_SunSubAgentTimeout_Type=Integer32
_SunSubAgentTimeout_Object=MibTableColumn
sunSubAgentTimeout=_SunSubAgentTimeout_Object((1,3,6,1,4,1,42,2,15,8,1,3),_SunSubAgentTimeout_Type())
sunSubAgentTimeout.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentTimeout.setStatus(_A)
class _SunSubAgentPortNumber_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SunSubAgentPortNumber_Type.__name__=_D
_SunSubAgentPortNumber_Object=MibTableColumn
sunSubAgentPortNumber=_SunSubAgentPortNumber_Object((1,3,6,1,4,1,42,2,15,8,1,4),_SunSubAgentPortNumber_Type())
sunSubAgentPortNumber.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentPortNumber.setStatus(_A)
_SunSubAgentRegistrationFile_Type=DisplayString
_SunSubAgentRegistrationFile_Object=MibTableColumn
sunSubAgentRegistrationFile=_SunSubAgentRegistrationFile_Object((1,3,6,1,4,1,42,2,15,8,1,5),_SunSubAgentRegistrationFile_Type())
sunSubAgentRegistrationFile.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentRegistrationFile.setStatus(_A)
_SunSubAgentAccessControlFile_Type=DisplayString
_SunSubAgentAccessControlFile_Object=MibTableColumn
sunSubAgentAccessControlFile=_SunSubAgentAccessControlFile_Object((1,3,6,1,4,1,42,2,15,8,1,6),_SunSubAgentAccessControlFile_Type())
sunSubAgentAccessControlFile.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentAccessControlFile.setStatus(_A)
_SunSubAgentExecutable_Type=DisplayString
_SunSubAgentExecutable_Object=MibTableColumn
sunSubAgentExecutable=_SunSubAgentExecutable_Object((1,3,6,1,4,1,42,2,15,8,1,7),_SunSubAgentExecutable_Type())
sunSubAgentExecutable.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentExecutable.setStatus(_A)
_SunSubAgentVersionNum_Type=DisplayString
_SunSubAgentVersionNum_Object=MibTableColumn
sunSubAgentVersionNum=_SunSubAgentVersionNum_Object((1,3,6,1,4,1,42,2,15,8,1,8),_SunSubAgentVersionNum_Type())
sunSubAgentVersionNum.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentVersionNum.setStatus(_A)
_SunSubAgentProcessID_Type=Integer32
_SunSubAgentProcessID_Object=MibTableColumn
sunSubAgentProcessID=_SunSubAgentProcessID_Object((1,3,6,1,4,1,42,2,15,8,1,9),_SunSubAgentProcessID_Type())
sunSubAgentProcessID.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentProcessID.setStatus(_A)
_SunSubAgentName_Type=DisplayString
_SunSubAgentName_Object=MibTableColumn
sunSubAgentName=_SunSubAgentName_Object((1,3,6,1,4,1,42,2,15,8,1,10),_SunSubAgentName_Type())
sunSubAgentName.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentName.setStatus(_A)
_SunSubAgentSystemUpTime_Type=TimeTicks
_SunSubAgentSystemUpTime_Object=MibTableColumn
sunSubAgentSystemUpTime=_SunSubAgentSystemUpTime_Object((1,3,6,1,4,1,42,2,15,8,1,11),_SunSubAgentSystemUpTime_Type())
sunSubAgentSystemUpTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentSystemUpTime.setStatus(_A)
_SunSubAgentWatchDogTime_Type=Integer32
_SunSubAgentWatchDogTime_Object=MibTableColumn
sunSubAgentWatchDogTime=_SunSubAgentWatchDogTime_Object((1,3,6,1,4,1,42,2,15,8,1,12),_SunSubAgentWatchDogTime_Type())
sunSubAgentWatchDogTime.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentWatchDogTime.setStatus(_A)
class _SunSubAgentTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SunSubAgentTableIndex_Type.__name__=_D
_SunSubAgentTableIndex_Object=MibScalar
sunSubAgentTableIndex=_SunSubAgentTableIndex_Object((1,3,6,1,4,1,42,2,15,9),_SunSubAgentTableIndex_Type())
sunSubAgentTableIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubAgentTableIndex.setStatus(_A)
_SunSubTreeConfigurationTable_Object=MibTable
sunSubTreeConfigurationTable=_SunSubTreeConfigurationTable_Object((1,3,6,1,4,1,42,2,15,10))
if mibBuilder.loadTexts:sunSubTreeConfigurationTable.setStatus(_A)
_SunSubTreeConfigurationEntry_Object=MibTableRow
sunSubTreeConfigurationEntry=_SunSubTreeConfigurationEntry_Object((1,3,6,1,4,1,42,2,15,10,1))
sunSubTreeConfigurationEntry.setIndexNames((0,_E,_I),(0,_E,_J))
if mibBuilder.loadTexts:sunSubTreeConfigurationEntry.setStatus(_A)
_SunSubTreeIndex_Type=Integer32
_SunSubTreeIndex_Object=MibTableColumn
sunSubTreeIndex=_SunSubTreeIndex_Object((1,3,6,1,4,1,42,2,15,10,1,1),_SunSubTreeIndex_Type())
sunSubTreeIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sunSubTreeIndex.setStatus(_A)
_SunSubTreeAgentID_Type=Integer32
_SunSubTreeAgentID_Object=MibTableColumn
sunSubTreeAgentID=_SunSubTreeAgentID_Object((1,3,6,1,4,1,42,2,15,10,1,2),_SunSubTreeAgentID_Type())
sunSubTreeAgentID.setMaxAccess(_C)
if mibBuilder.loadTexts:sunSubTreeAgentID.setStatus(_A)
_SunSubTreeOID_Type=ObjectIdentifier
_SunSubTreeOID_Object=MibTableColumn
sunSubTreeOID=_SunSubTreeOID_Object((1,3,6,1,4,1,42,2,15,10,1,3),_SunSubTreeOID_Type())
sunSubTreeOID.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubTreeOID.setStatus(_A)
_SunSubTreeStartColumn_Type=Integer32
_SunSubTreeStartColumn_Object=MibTableColumn
sunSubTreeStartColumn=_SunSubTreeStartColumn_Object((1,3,6,1,4,1,42,2,15,10,1,4),_SunSubTreeStartColumn_Type())
sunSubTreeStartColumn.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubTreeStartColumn.setStatus(_A)
_SunSubTreeEndColumn_Type=Integer32
_SunSubTreeEndColumn_Object=MibTableColumn
sunSubTreeEndColumn=_SunSubTreeEndColumn_Object((1,3,6,1,4,1,42,2,15,10,1,5),_SunSubTreeEndColumn_Type())
sunSubTreeEndColumn.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubTreeEndColumn.setStatus(_A)
_SunSubTreeStartRow_Type=Integer32
_SunSubTreeStartRow_Object=MibTableColumn
sunSubTreeStartRow=_SunSubTreeStartRow_Object((1,3,6,1,4,1,42,2,15,10,1,6),_SunSubTreeStartRow_Type())
sunSubTreeStartRow.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubTreeStartRow.setStatus(_A)
_SunSubTreeEndRow_Type=Integer32
_SunSubTreeEndRow_Object=MibTableColumn
sunSubTreeEndRow=_SunSubTreeEndRow_Object((1,3,6,1,4,1,42,2,15,10,1,7),_SunSubTreeEndRow_Type())
sunSubTreeEndRow.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubTreeEndRow.setStatus(_A)
class _SunSubTreeStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SunSubTreeStatus_Type.__name__=_D
_SunSubTreeStatus_Object=MibTableColumn
sunSubTreeStatus=_SunSubTreeStatus_Object((1,3,6,1,4,1,42,2,15,10,1,8),_SunSubTreeStatus_Type())
sunSubTreeStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubTreeStatus.setStatus(_A)
class _SunSubTreeConfigurationTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SunSubTreeConfigurationTableIndex_Type.__name__=_D
_SunSubTreeConfigurationTableIndex_Object=MibScalar
sunSubTreeConfigurationTableIndex=_SunSubTreeConfigurationTableIndex_Object((1,3,6,1,4,1,42,2,15,11),_SunSubTreeConfigurationTableIndex_Type())
sunSubTreeConfigurationTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sunSubTreeConfigurationTableIndex.setStatus(_A)
_SunSubTreeDispatchTable_Object=MibTable
sunSubTreeDispatchTable=_SunSubTreeDispatchTable_Object((1,3,6,1,4,1,42,2,15,12))
if mibBuilder.loadTexts:sunSubTreeDispatchTable.setStatus(_A)
_SunSubTreeDispatchEntry_Object=MibTableRow
sunSubTreeDispatchEntry=_SunSubTreeDispatchEntry_Object((1,3,6,1,4,1,42,2,15,12,1))
sunSubTreeDispatchEntry.setIndexNames((0,_E,_K),(0,_E,_L))
if mibBuilder.loadTexts:sunSubTreeDispatchEntry.setStatus(_A)
_SunSubTreeDispatchIndex_Type=Integer32
_SunSubTreeDispatchIndex_Object=MibTableColumn
sunSubTreeDispatchIndex=_SunSubTreeDispatchIndex_Object((1,3,6,1,4,1,42,2,15,12,1,1),_SunSubTreeDispatchIndex_Type())
sunSubTreeDispatchIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sunSubTreeDispatchIndex.setStatus(_A)
_SunSubTreeDispatchAgentID_Type=Integer32
_SunSubTreeDispatchAgentID_Object=MibTableColumn
sunSubTreeDispatchAgentID=_SunSubTreeDispatchAgentID_Object((1,3,6,1,4,1,42,2,15,12,1,2),_SunSubTreeDispatchAgentID_Type())
sunSubTreeDispatchAgentID.setMaxAccess(_C)
if mibBuilder.loadTexts:sunSubTreeDispatchAgentID.setStatus(_A)
_SunSubTreeDispatchOID_Type=ObjectIdentifier
_SunSubTreeDispatchOID_Object=MibTableColumn
sunSubTreeDispatchOID=_SunSubTreeDispatchOID_Object((1,3,6,1,4,1,42,2,15,12,1,3),_SunSubTreeDispatchOID_Type())
sunSubTreeDispatchOID.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubTreeDispatchOID.setStatus(_A)
class _SunSubTreeDispatchStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_F,1),(_G,2)))
_SunSubTreeDispatchStatus_Type.__name__=_D
_SunSubTreeDispatchStatus_Object=MibTableColumn
sunSubTreeDispatchStatus=_SunSubTreeDispatchStatus_Object((1,3,6,1,4,1,42,2,15,12,1,4),_SunSubTreeDispatchStatus_Type())
sunSubTreeDispatchStatus.setMaxAccess(_B)
if mibBuilder.loadTexts:sunSubTreeDispatchStatus.setStatus(_A)
class _SunSubTreeDispatchTableIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_SunSubTreeDispatchTableIndex_Type.__name__=_D
_SunSubTreeDispatchTableIndex_Object=MibScalar
sunSubTreeDispatchTableIndex=_SunSubTreeDispatchTableIndex_Object((1,3,6,1,4,1,42,2,15,13),_SunSubTreeDispatchTableIndex_Type())
sunSubTreeDispatchTableIndex.setMaxAccess(_C)
if mibBuilder.loadTexts:sunSubTreeDispatchTableIndex.setStatus(_A)
mibBuilder.exportSymbols(_E,**{'sun':sun,'products':products,'sunMasterAgent':sunMasterAgent,'sunMasterAgentStatusFile':sunMasterAgentStatusFile,'sunMasterAgentResourceConfigFile':sunMasterAgentResourceConfigFile,'sunMasterAgentConfigurationDir':sunMasterAgentConfigurationDir,'sunMasterAgentTrapPort':sunMasterAgentTrapPort,'sunCheckSubAgentName':sunCheckSubAgentName,'sunMasterAgentPollInterval':sunMasterAgentPollInterval,'sunMasterAgentMaxAgentTimeOut':sunMasterAgentMaxAgentTimeOut,'sunSubAgentTable':sunSubAgentTable,'sunSubAgentEntry':sunSubAgentEntry,_H:sunSubAgentID,'sunSubAgentStatus':sunSubAgentStatus,'sunSubAgentTimeout':sunSubAgentTimeout,'sunSubAgentPortNumber':sunSubAgentPortNumber,'sunSubAgentRegistrationFile':sunSubAgentRegistrationFile,'sunSubAgentAccessControlFile':sunSubAgentAccessControlFile,'sunSubAgentExecutable':sunSubAgentExecutable,'sunSubAgentVersionNum':sunSubAgentVersionNum,'sunSubAgentProcessID':sunSubAgentProcessID,'sunSubAgentName':sunSubAgentName,'sunSubAgentSystemUpTime':sunSubAgentSystemUpTime,'sunSubAgentWatchDogTime':sunSubAgentWatchDogTime,'sunSubAgentTableIndex':sunSubAgentTableIndex,'sunSubTreeConfigurationTable':sunSubTreeConfigurationTable,'sunSubTreeConfigurationEntry':sunSubTreeConfigurationEntry,_J:sunSubTreeIndex,_I:sunSubTreeAgentID,'sunSubTreeOID':sunSubTreeOID,'sunSubTreeStartColumn':sunSubTreeStartColumn,'sunSubTreeEndColumn':sunSubTreeEndColumn,'sunSubTreeStartRow':sunSubTreeStartRow,'sunSubTreeEndRow':sunSubTreeEndRow,'sunSubTreeStatus':sunSubTreeStatus,'sunSubTreeConfigurationTableIndex':sunSubTreeConfigurationTableIndex,'sunSubTreeDispatchTable':sunSubTreeDispatchTable,'sunSubTreeDispatchEntry':sunSubTreeDispatchEntry,_L:sunSubTreeDispatchIndex,_K:sunSubTreeDispatchAgentID,'sunSubTreeDispatchOID':sunSubTreeDispatchOID,'sunSubTreeDispatchStatus':sunSubTreeDispatchStatus,'sunSubTreeDispatchTableIndex':sunSubTreeDispatchTableIndex})