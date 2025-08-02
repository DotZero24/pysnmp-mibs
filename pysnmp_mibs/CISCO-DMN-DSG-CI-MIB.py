_R='ciSystemIDIndex'
_Q='ciSystemIDSlot'
_P='ciStatusSlot'
_O='ciCompConfigID'
_N='ciProgramDecrPEID'
_M='ciConfigInstance'
_L='bottom'
_K='top'
_J='enable'
_I='disable'
_H='not-accessible'
_G='read-create'
_F='CISCO-DMN-DSG-CI-MIB'
_E='read-write'
_D='read-only'
_C='DisplayString'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
ciscoDSGUtilities,=mibBuilder.importSymbols('CISCO-DMN-DSG-ROOT-MIB','ciscoDSGUtilities')
ModuleCompliance,NotificationGroup,ObjectGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup','ObjectGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','iso')
DisplayString,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_C,'PhysAddress','RowStatus','TextualConvention')
ciscoDSGCI=ModuleIdentity((1,3,6,1,4,1,1429,2,2,5,12))
if mibBuilder.loadTexts:ciscoDSGCI.setRevisions(('2012-03-20 08:00','2010-10-13 08:00','2010-08-30 09:00','2010-04-12 09:00','2010-03-22 05:00','2010-02-12 12:00','2009-12-07 12:00'))
_CiTable_ObjectIdentity=ObjectIdentity
ciTable=_CiTable_ObjectIdentity((1,3,6,1,4,1,1429,2,2,5,12,2))
_CiConfigTable_Object=MibTable
ciConfigTable=_CiConfigTable_Object((1,3,6,1,4,1,1429,2,2,5,12,2,1))
if mibBuilder.loadTexts:ciConfigTable.setStatus(_A)
_CiConfigEntry_Object=MibTableRow
ciConfigEntry=_CiConfigEntry_Object((1,3,6,1,4,1,1429,2,2,5,12,2,1,1))
ciConfigEntry.setIndexNames((0,_F,_M))
if mibBuilder.loadTexts:ciConfigEntry.setStatus(_A)
class _CiConfigInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,1))
_CiConfigInstance_Type.__name__=_B
_CiConfigInstance_Object=MibTableColumn
ciConfigInstance=_CiConfigInstance_Object((1,3,6,1,4,1,1429,2,2,5,12,2,1,1,1),_CiConfigInstance_Type())
ciConfigInstance.setMaxAccess(_H)
if mibBuilder.loadTexts:ciConfigInstance.setStatus(_A)
class _CiConfigQuery_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CiConfigQuery_Type.__name__=_B
_CiConfigQuery_Object=MibTableColumn
ciConfigQuery=_CiConfigQuery_Object((1,3,6,1,4,1,1429,2,2,5,12,2,1,1,2),_CiConfigQuery_Type())
ciConfigQuery.setMaxAccess(_E)
if mibBuilder.loadTexts:ciConfigQuery.setStatus(_A)
class _CiConfigAutoReset_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CiConfigAutoReset_Type.__name__=_B
_CiConfigAutoReset_Object=MibTableColumn
ciConfigAutoReset=_CiConfigAutoReset_Object((1,3,6,1,4,1,1429,2,2,5,12,2,1,1,3),_CiConfigAutoReset_Type())
ciConfigAutoReset.setMaxAccess(_E)
if mibBuilder.loadTexts:ciConfigAutoReset.setStatus(_A)
class _CiConfigListMgmt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('addDelete',1),('updateAll',2)))
_CiConfigListMgmt_Type.__name__=_B
_CiConfigListMgmt_Object=MibTableColumn
ciConfigListMgmt=_CiConfigListMgmt_Object((1,3,6,1,4,1,1429,2,2,5,12,2,1,1,4),_CiConfigListMgmt_Type())
ciConfigListMgmt.setMaxAccess(_E)
if mibBuilder.loadTexts:ciConfigListMgmt.setStatus(_A)
class _CiConfigOrgNetIDUse_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_I,1),(_J,2)))
_CiConfigOrgNetIDUse_Type.__name__=_B
_CiConfigOrgNetIDUse_Object=MibTableColumn
ciConfigOrgNetIDUse=_CiConfigOrgNetIDUse_Object((1,3,6,1,4,1,1429,2,2,5,12,2,1,1,5),_CiConfigOrgNetIDUse_Type())
ciConfigOrgNetIDUse.setMaxAccess(_E)
if mibBuilder.loadTexts:ciConfigOrgNetIDUse.setStatus(_A)
class _CiConfigTransportId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiConfigTransportId_Type.__name__=_B
_CiConfigTransportId_Object=MibTableColumn
ciConfigTransportId=_CiConfigTransportId_Object((1,3,6,1,4,1,1429,2,2,5,12,2,1,1,6),_CiConfigTransportId_Type())
ciConfigTransportId.setMaxAccess(_E)
if mibBuilder.loadTexts:ciConfigTransportId.setStatus(_A)
class _CiConfigOrgNetID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_CiConfigOrgNetID_Type.__name__=_B
_CiConfigOrgNetID_Object=MibTableColumn
ciConfigOrgNetID=_CiConfigOrgNetID_Object((1,3,6,1,4,1,1429,2,2,5,12,2,1,1,7),_CiConfigOrgNetID_Type())
ciConfigOrgNetID.setMaxAccess(_E)
if mibBuilder.loadTexts:ciConfigOrgNetID.setStatus(_A)
class _CiConfigTsHandling_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('entire',1),('partial',2)))
_CiConfigTsHandling_Type.__name__=_B
_CiConfigTsHandling_Object=MibTableColumn
ciConfigTsHandling=_CiConfigTsHandling_Object((1,3,6,1,4,1,1429,2,2,5,12,2,1,1,8),_CiConfigTsHandling_Type())
ciConfigTsHandling.setMaxAccess(_E)
if mibBuilder.loadTexts:ciConfigTsHandling.setStatus(_A)
_CiProgramDecrTable_Object=MibTable
ciProgramDecrTable=_CiProgramDecrTable_Object((1,3,6,1,4,1,1429,2,2,5,12,2,2))
if mibBuilder.loadTexts:ciProgramDecrTable.setStatus(_A)
_CiProgramDecrEntry_Object=MibTableRow
ciProgramDecrEntry=_CiProgramDecrEntry_Object((1,3,6,1,4,1,1429,2,2,5,12,2,2,1))
ciProgramDecrEntry.setIndexNames((0,_F,_N))
if mibBuilder.loadTexts:ciProgramDecrEntry.setStatus(_A)
class _CiProgramDecrPEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CiProgramDecrPEID_Type.__name__=_B
_CiProgramDecrPEID_Object=MibTableColumn
ciProgramDecrPEID=_CiProgramDecrPEID_Object((1,3,6,1,4,1,1429,2,2,5,12,2,2,1,1),_CiProgramDecrPEID_Type())
ciProgramDecrPEID.setMaxAccess(_H)
if mibBuilder.loadTexts:ciProgramDecrPEID.setStatus(_A)
class _CiProgramDecrDecrypt_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('off',1),('on',2),('comp',3)))
_CiProgramDecrDecrypt_Type.__name__=_B
_CiProgramDecrDecrypt_Object=MibTableColumn
ciProgramDecrDecrypt=_CiProgramDecrDecrypt_Object((1,3,6,1,4,1,1429,2,2,5,12,2,2,1,2),_CiProgramDecrDecrypt_Type())
ciProgramDecrDecrypt.setMaxAccess(_E)
if mibBuilder.loadTexts:ciProgramDecrDecrypt.setStatus(_A)
class _CiProgramDecrCISlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_CiProgramDecrCISlot_Type.__name__=_B
_CiProgramDecrCISlot_Object=MibTableColumn
ciProgramDecrCISlot=_CiProgramDecrCISlot_Object((1,3,6,1,4,1,1429,2,2,5,12,2,2,1,3),_CiProgramDecrCISlot_Type())
ciProgramDecrCISlot.setMaxAccess(_E)
if mibBuilder.loadTexts:ciProgramDecrCISlot.setStatus(_A)
_CiCompConfigTable_Object=MibTable
ciCompConfigTable=_CiCompConfigTable_Object((1,3,6,1,4,1,1429,2,2,5,12,2,3))
if mibBuilder.loadTexts:ciCompConfigTable.setStatus(_A)
_CiCompConfigEntry_Object=MibTableRow
ciCompConfigEntry=_CiCompConfigEntry_Object((1,3,6,1,4,1,1429,2,2,5,12,2,3,1))
ciCompConfigEntry.setIndexNames((0,_F,_O))
if mibBuilder.loadTexts:ciCompConfigEntry.setStatus(_A)
class _CiCompConfigID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CiCompConfigID_Type.__name__=_B
_CiCompConfigID_Object=MibTableColumn
ciCompConfigID=_CiCompConfigID_Object((1,3,6,1,4,1,1429,2,2,5,12,2,3,1,1),_CiCompConfigID_Type())
ciCompConfigID.setMaxAccess(_H)
if mibBuilder.loadTexts:ciCompConfigID.setStatus(_A)
class _CiCompConfigPEID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CiCompConfigPEID_Type.__name__=_B
_CiCompConfigPEID_Object=MibTableColumn
ciCompConfigPEID=_CiCompConfigPEID_Object((1,3,6,1,4,1,1429,2,2,5,12,2,3,1,2),_CiCompConfigPEID_Type())
ciCompConfigPEID.setMaxAccess(_G)
if mibBuilder.loadTexts:ciCompConfigPEID.setStatus(_A)
class _CiCompConfigMode_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('pid',1),('stream',2)))
_CiCompConfigMode_Type.__name__=_B
_CiCompConfigMode_Object=MibTableColumn
ciCompConfigMode=_CiCompConfigMode_Object((1,3,6,1,4,1,1429,2,2,5,12,2,3,1,3),_CiCompConfigMode_Type())
ciCompConfigMode.setMaxAccess(_G)
if mibBuilder.loadTexts:ciCompConfigMode.setStatus(_A)
class _CiCompConfigPID_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,8192))
_CiCompConfigPID_Type.__name__=_B
_CiCompConfigPID_Object=MibTableColumn
ciCompConfigPID=_CiCompConfigPID_Object((1,3,6,1,4,1,1429,2,2,5,12,2,3,1,4),_CiCompConfigPID_Type())
ciCompConfigPID.setMaxAccess(_G)
if mibBuilder.loadTexts:ciCompConfigPID.setStatus(_A)
class _CiCompConfigStreamCategory_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(2,3,4,8,12)));namedValues=NamedValues(*(('vid',2),('aud',3),('subt',4),('ttx',8),('user',12)))
_CiCompConfigStreamCategory_Type.__name__=_B
_CiCompConfigStreamCategory_Object=MibTableColumn
ciCompConfigStreamCategory=_CiCompConfigStreamCategory_Object((1,3,6,1,4,1,1429,2,2,5,12,2,3,1,5),_CiCompConfigStreamCategory_Type())
ciCompConfigStreamCategory.setMaxAccess(_G)
if mibBuilder.loadTexts:ciCompConfigStreamCategory.setStatus(_A)
class _CiCompConfigStreamTypeVal_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_CiCompConfigStreamTypeVal_Type.__name__=_B
_CiCompConfigStreamTypeVal_Object=MibTableColumn
ciCompConfigStreamTypeVal=_CiCompConfigStreamTypeVal_Object((1,3,6,1,4,1,1429,2,2,5,12,2,3,1,6),_CiCompConfigStreamTypeVal_Type())
ciCompConfigStreamTypeVal.setMaxAccess(_G)
if mibBuilder.loadTexts:ciCompConfigStreamTypeVal.setStatus(_A)
class _CiCompConfigStreamInstance_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,64))
_CiCompConfigStreamInstance_Type.__name__=_B
_CiCompConfigStreamInstance_Object=MibTableColumn
ciCompConfigStreamInstance=_CiCompConfigStreamInstance_Object((1,3,6,1,4,1,1429,2,2,5,12,2,3,1,7),_CiCompConfigStreamInstance_Type())
ciCompConfigStreamInstance.setMaxAccess(_G)
if mibBuilder.loadTexts:ciCompConfigStreamInstance.setStatus(_A)
_CiCompConfigRowCmdStatus_Type=RowStatus
_CiCompConfigRowCmdStatus_Object=MibTableColumn
ciCompConfigRowCmdStatus=_CiCompConfigRowCmdStatus_Object((1,3,6,1,4,1,1429,2,2,5,12,2,3,1,8),_CiCompConfigRowCmdStatus_Type())
ciCompConfigRowCmdStatus.setMaxAccess(_G)
if mibBuilder.loadTexts:ciCompConfigRowCmdStatus.setStatus(_A)
_CiCompStatusTable_Object=MibTable
ciCompStatusTable=_CiCompStatusTable_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4))
if mibBuilder.loadTexts:ciCompStatusTable.setStatus(_A)
_CiCompStatusEntry_Object=MibTableRow
ciCompStatusEntry=_CiCompStatusEntry_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1))
ciCompStatusEntry.setIndexNames((0,_F,_P))
if mibBuilder.loadTexts:ciCompStatusEntry.setStatus(_A)
class _CiStatusSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_CiStatusSlot_Type.__name__=_B
_CiStatusSlot_Object=MibTableColumn
ciStatusSlot=_CiStatusSlot_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1,1),_CiStatusSlot_Type())
ciStatusSlot.setMaxAccess(_H)
if mibBuilder.loadTexts:ciStatusSlot.setStatus(_A)
class _CiStatusSysName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_CiStatusSysName_Type.__name__=_C
_CiStatusSysName_Object=MibTableColumn
ciStatusSysName=_CiStatusSysName_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1,2),_CiStatusSysName_Type())
ciStatusSysName.setMaxAccess(_D)
if mibBuilder.loadTexts:ciStatusSysName.setStatus(_A)
class _CiStatusMFGID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CiStatusMFGID_Type.__name__=_C
_CiStatusMFGID_Object=MibTableColumn
ciStatusMFGID=_CiStatusMFGID_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1,3),_CiStatusMFGID_Type())
ciStatusMFGID.setMaxAccess(_D)
if mibBuilder.loadTexts:ciStatusMFGID.setStatus(_A)
class _CiStatusMFGCode_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CiStatusMFGCode_Type.__name__=_C
_CiStatusMFGCode_Object=MibTableColumn
ciStatusMFGCode=_CiStatusMFGCode_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1,4),_CiStatusMFGCode_Type())
ciStatusMFGCode.setMaxAccess(_D)
if mibBuilder.loadTexts:ciStatusMFGCode.setStatus(_A)
class _CiStatusSerialNum_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CiStatusSerialNum_Type.__name__=_C
_CiStatusSerialNum_Object=MibTableColumn
ciStatusSerialNum=_CiStatusSerialNum_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1,5),_CiStatusSerialNum_Type())
ciStatusSerialNum.setMaxAccess(_D)
if mibBuilder.loadTexts:ciStatusSerialNum.setStatus(_A)
class _CiStatusHWVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CiStatusHWVer_Type.__name__=_C
_CiStatusHWVer_Object=MibTableColumn
ciStatusHWVer=_CiStatusHWVer_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1,6),_CiStatusHWVer_Type())
ciStatusHWVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ciStatusHWVer.setStatus(_A)
class _CiStatusAppVer_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,63))
_CiStatusAppVer_Type.__name__=_C
_CiStatusAppVer_Object=MibTableColumn
ciStatusAppVer=_CiStatusAppVer_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1,7),_CiStatusAppVer_Type())
ciStatusAppVer.setMaxAccess(_D)
if mibBuilder.loadTexts:ciStatusAppVer.setStatus(_A)
class _CiStatusCompany_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,39))
_CiStatusCompany_Type.__name__=_C
_CiStatusCompany_Object=MibTableColumn
ciStatusCompany=_CiStatusCompany_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1,8),_CiStatusCompany_Type())
ciStatusCompany.setMaxAccess(_D)
if mibBuilder.loadTexts:ciStatusCompany.setStatus(_A)
class _CiStatusProdname_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,39))
_CiStatusProdname_Type.__name__=_C
_CiStatusProdname_Object=MibTableColumn
ciStatusProdname=_CiStatusProdname_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1,9),_CiStatusProdname_Type())
ciStatusProdname.setMaxAccess(_D)
if mibBuilder.loadTexts:ciStatusProdname.setStatus(_A)
class _CiStatusCamStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*(('notReady',1),('ready',2)))
_CiStatusCamStatus_Type.__name__=_B
_CiStatusCamStatus_Object=MibTableColumn
ciStatusCamStatus=_CiStatusCamStatus_Object((1,3,6,1,4,1,1429,2,2,5,12,2,4,1,10),_CiStatusCamStatus_Type())
ciStatusCamStatus.setMaxAccess(_D)
if mibBuilder.loadTexts:ciStatusCamStatus.setStatus(_A)
_CiSystemIDTable_Object=MibTable
ciSystemIDTable=_CiSystemIDTable_Object((1,3,6,1,4,1,1429,2,2,5,12,2,5))
if mibBuilder.loadTexts:ciSystemIDTable.setStatus(_A)
_CiSystemIDEntry_Object=MibTableRow
ciSystemIDEntry=_CiSystemIDEntry_Object((1,3,6,1,4,1,1429,2,2,5,12,2,5,1))
ciSystemIDEntry.setIndexNames((0,_F,_Q),(0,_F,_R))
if mibBuilder.loadTexts:ciSystemIDEntry.setStatus(_A)
class _CiSystemIDSlot_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2)));namedValues=NamedValues(*((_K,1),(_L,2)))
_CiSystemIDSlot_Type.__name__=_B
_CiSystemIDSlot_Object=MibTableColumn
ciSystemIDSlot=_CiSystemIDSlot_Object((1,3,6,1,4,1,1429,2,2,5,12,2,5,1,1),_CiSystemIDSlot_Type())
ciSystemIDSlot.setMaxAccess(_H)
if mibBuilder.loadTexts:ciSystemIDSlot.setStatus(_A)
class _CiSystemIDIndex_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,32))
_CiSystemIDIndex_Type.__name__=_B
_CiSystemIDIndex_Object=MibTableColumn
ciSystemIDIndex=_CiSystemIDIndex_Object((1,3,6,1,4,1,1429,2,2,5,12,2,5,1,2),_CiSystemIDIndex_Type())
ciSystemIDIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:ciSystemIDIndex.setStatus(_A)
class _CiSystemIDName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CiSystemIDName_Type.__name__=_C
_CiSystemIDName_Object=MibTableColumn
ciSystemIDName=_CiSystemIDName_Object((1,3,6,1,4,1,1429,2,2,5,12,2,5,1,3),_CiSystemIDName_Type())
ciSystemIDName.setMaxAccess(_D)
if mibBuilder.loadTexts:ciSystemIDName.setStatus(_A)
class _CiSystemID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(1,32))
_CiSystemID_Type.__name__=_C
_CiSystemID_Object=MibTableColumn
ciSystemID=_CiSystemID_Object((1,3,6,1,4,1,1429,2,2,5,12,2,5,1,4),_CiSystemID_Type())
ciSystemID.setMaxAccess(_D)
if mibBuilder.loadTexts:ciSystemID.setStatus(_A)
class _CiSystemSysNameID_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,37))
_CiSystemSysNameID_Type.__name__=_C
_CiSystemSysNameID_Object=MibTableColumn
ciSystemSysNameID=_CiSystemSysNameID_Object((1,3,6,1,4,1,1429,2,2,5,12,2,5,1,5),_CiSystemSysNameID_Type())
ciSystemSysNameID.setMaxAccess(_D)
if mibBuilder.loadTexts:ciSystemSysNameID.setStatus(_A)
mibBuilder.exportSymbols(_F,**{'ciscoDSGCI':ciscoDSGCI,'ciTable':ciTable,'ciConfigTable':ciConfigTable,'ciConfigEntry':ciConfigEntry,_M:ciConfigInstance,'ciConfigQuery':ciConfigQuery,'ciConfigAutoReset':ciConfigAutoReset,'ciConfigListMgmt':ciConfigListMgmt,'ciConfigOrgNetIDUse':ciConfigOrgNetIDUse,'ciConfigTransportId':ciConfigTransportId,'ciConfigOrgNetID':ciConfigOrgNetID,'ciConfigTsHandling':ciConfigTsHandling,'ciProgramDecrTable':ciProgramDecrTable,'ciProgramDecrEntry':ciProgramDecrEntry,_N:ciProgramDecrPEID,'ciProgramDecrDecrypt':ciProgramDecrDecrypt,'ciProgramDecrCISlot':ciProgramDecrCISlot,'ciCompConfigTable':ciCompConfigTable,'ciCompConfigEntry':ciCompConfigEntry,_O:ciCompConfigID,'ciCompConfigPEID':ciCompConfigPEID,'ciCompConfigMode':ciCompConfigMode,'ciCompConfigPID':ciCompConfigPID,'ciCompConfigStreamCategory':ciCompConfigStreamCategory,'ciCompConfigStreamTypeVal':ciCompConfigStreamTypeVal,'ciCompConfigStreamInstance':ciCompConfigStreamInstance,'ciCompConfigRowCmdStatus':ciCompConfigRowCmdStatus,'ciCompStatusTable':ciCompStatusTable,'ciCompStatusEntry':ciCompStatusEntry,_P:ciStatusSlot,'ciStatusSysName':ciStatusSysName,'ciStatusMFGID':ciStatusMFGID,'ciStatusMFGCode':ciStatusMFGCode,'ciStatusSerialNum':ciStatusSerialNum,'ciStatusHWVer':ciStatusHWVer,'ciStatusAppVer':ciStatusAppVer,'ciStatusCompany':ciStatusCompany,'ciStatusProdname':ciStatusProdname,'ciStatusCamStatus':ciStatusCamStatus,'ciSystemIDTable':ciSystemIDTable,'ciSystemIDEntry':ciSystemIDEntry,_Q:ciSystemIDSlot,_R:ciSystemIDIndex,'ciSystemIDName':ciSystemIDName,'ciSystemID':ciSystemID,'ciSystemSysNameID':ciSystemSysNameID})