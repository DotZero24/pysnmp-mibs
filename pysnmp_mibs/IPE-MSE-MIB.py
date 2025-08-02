_N='provMseClockSelectCardId'
_M='provMseClockModeExtIfIndex'
_L='provMseClockModeIfIndex'
_K='provMseLineModeIfIndex'
_J='asMseLineIfIndex'
_I='asMseCardIndex'
_H='IpeEnableDisableValue'
_G='invalid'
_F='read-write'
_E='Integer32'
_D='IPE-MSE-MIB'
_C='read-only'
_B='not-accessible'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,=mibBuilder.importSymbols('IF-MIB','InterfaceIndex')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,Opaque,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_E,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','Opaque','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,PhysAddress,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC','DisplayString','PhysAddress','TextualConvention')
class IpeEnableDisableValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('disabled',1),('enabled',2)))
class SeverityValue(TextualConvention,Integer32):status=_A;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3,4,5,6)));namedValues=NamedValues(*(('cleared',1),('indetermine',2),('critical',3),('major',4),('minor',5),('warning',6)))
_Nec_ObjectIdentity=ObjectIdentity
nec=_Nec_ObjectIdentity((1,3,6,1,4,1,119))
_Nec_mib_ObjectIdentity=ObjectIdentity
nec_mib=_Nec_mib_ObjectIdentity((1,3,6,1,4,1,119,2))
_NecProductDepend_ObjectIdentity=ObjectIdentity
necProductDepend=_NecProductDepend_ObjectIdentity((1,3,6,1,4,1,119,2,3))
_RadioEquipment_ObjectIdentity=ObjectIdentity
radioEquipment=_RadioEquipment_ObjectIdentity((1,3,6,1,4,1,119,2,3,69))
_PasoNeoIpe_common_ObjectIdentity=ObjectIdentity
pasoNeoIpe_common=_PasoNeoIpe_common_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501))
_AlarmStatusGroup_ObjectIdentity=ObjectIdentity
alarmStatusGroup=_AlarmStatusGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,3))
_AsMseGroup_ObjectIdentity=ObjectIdentity
asMseGroup=_AsMseGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,3,40))
_AsMseCardTable_Object=MibTable
asMseCardTable=_AsMseCardTable_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1))
if mibBuilder.loadTexts:asMseCardTable.setStatus(_A)
_AsMseCardEntry_Object=MibTableRow
asMseCardEntry=_AsMseCardEntry_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1,1))
asMseCardEntry.setIndexNames((0,_D,_I))
if mibBuilder.loadTexts:asMseCardEntry.setStatus(_A)
_AsMseCardIndex_Type=Integer32
_AsMseCardIndex_Object=MibTableColumn
asMseCardIndex=_AsMseCardIndex_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1,1,1),_AsMseCardIndex_Type())
asMseCardIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:asMseCardIndex.setStatus(_A)
_AsMseCardNEAddress_Type=IpAddress
_AsMseCardNEAddress_Object=MibTableColumn
asMseCardNEAddress=_AsMseCardNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1,1,2),_AsMseCardNEAddress_Type())
asMseCardNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:asMseCardNEAddress.setStatus(_A)
_AsMseCardModuleFail_Type=SeverityValue
_AsMseCardModuleFail_Object=MibTableColumn
asMseCardModuleFail=_AsMseCardModuleFail_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1,1,3),_AsMseCardModuleFail_Type())
asMseCardModuleFail.setMaxAccess(_C)
if mibBuilder.loadTexts:asMseCardModuleFail.setStatus(_A)
_AsMseCardComFailAlarm_Type=SeverityValue
_AsMseCardComFailAlarm_Object=MibTableColumn
asMseCardComFailAlarm=_AsMseCardComFailAlarm_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1,1,4),_AsMseCardComFailAlarm_Type())
asMseCardComFailAlarm.setMaxAccess(_C)
if mibBuilder.loadTexts:asMseCardComFailAlarm.setStatus(_A)
_AsMseCardUnequipped_Type=SeverityValue
_AsMseCardUnequipped_Object=MibTableColumn
asMseCardUnequipped=_AsMseCardUnequipped_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1,1,5),_AsMseCardUnequipped_Type())
asMseCardUnequipped.setMaxAccess(_C)
if mibBuilder.loadTexts:asMseCardUnequipped.setStatus(_A)
_AsMseCardTypeMismatch_Type=SeverityValue
_AsMseCardTypeMismatch_Object=MibTableColumn
asMseCardTypeMismatch=_AsMseCardTypeMismatch_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1,1,6),_AsMseCardTypeMismatch_Type())
asMseCardTypeMismatch.setMaxAccess(_C)
if mibBuilder.loadTexts:asMseCardTypeMismatch.setStatus(_A)
_AsMseCardBusErrorTx_Type=SeverityValue
_AsMseCardBusErrorTx_Object=MibTableColumn
asMseCardBusErrorTx=_AsMseCardBusErrorTx_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1,1,7),_AsMseCardBusErrorTx_Type())
asMseCardBusErrorTx.setMaxAccess(_C)
if mibBuilder.loadTexts:asMseCardBusErrorTx.setStatus(_A)
_AsMseCardBusErrorRx_Type=SeverityValue
_AsMseCardBusErrorRx_Object=MibTableColumn
asMseCardBusErrorRx=_AsMseCardBusErrorRx_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1,1,8),_AsMseCardBusErrorRx_Type())
asMseCardBusErrorRx.setMaxAccess(_C)
if mibBuilder.loadTexts:asMseCardBusErrorRx.setStatus(_A)
_AsMseCardClkFail_Type=SeverityValue
_AsMseCardClkFail_Object=MibTableColumn
asMseCardClkFail=_AsMseCardClkFail_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,1,1,9),_AsMseCardClkFail_Type())
asMseCardClkFail.setMaxAccess(_C)
if mibBuilder.loadTexts:asMseCardClkFail.setStatus('obsolete')
_AsMseLineTable_Object=MibTable
asMseLineTable=_AsMseLineTable_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,2))
if mibBuilder.loadTexts:asMseLineTable.setStatus(_A)
_AsMseLineEntry_Object=MibTableRow
asMseLineEntry=_AsMseLineEntry_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,2,1))
asMseLineEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:asMseLineEntry.setStatus(_A)
_AsMseLineIfIndex_Type=InterfaceIndex
_AsMseLineIfIndex_Object=MibTableColumn
asMseLineIfIndex=_AsMseLineIfIndex_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,2,1,1),_AsMseLineIfIndex_Type())
asMseLineIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:asMseLineIfIndex.setStatus(_A)
_AsMseLineNEAddress_Type=IpAddress
_AsMseLineNEAddress_Object=MibTableColumn
asMseLineNEAddress=_AsMseLineNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,2,1,2),_AsMseLineNEAddress_Type())
asMseLineNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:asMseLineNEAddress.setStatus(_A)
_AsMseLineBfrUnderrun_Type=SeverityValue
_AsMseLineBfrUnderrun_Object=MibTableColumn
asMseLineBfrUnderrun=_AsMseLineBfrUnderrun_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,2,1,5),_AsMseLineBfrUnderrun_Type())
asMseLineBfrUnderrun.setMaxAccess(_C)
if mibBuilder.loadTexts:asMseLineBfrUnderrun.setStatus(_A)
class _AsMseLineAdaptiveClkStatus_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('holdover',1),('acquiring',2),('acquired',3)))
_AsMseLineAdaptiveClkStatus_Type.__name__=_E
_AsMseLineAdaptiveClkStatus_Object=MibTableColumn
asMseLineAdaptiveClkStatus=_AsMseLineAdaptiveClkStatus_Object((1,3,6,1,4,1,119,2,3,69,501,3,40,2,1,6),_AsMseLineAdaptiveClkStatus_Type())
asMseLineAdaptiveClkStatus.setMaxAccess(_C)
if mibBuilder.loadTexts:asMseLineAdaptiveClkStatus.setStatus(_A)
_ProvisioningGroup_ObjectIdentity=ObjectIdentity
provisioningGroup=_ProvisioningGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,5))
_ProvMseGroup_ObjectIdentity=ObjectIdentity
provMseGroup=_ProvMseGroup_ObjectIdentity((1,3,6,1,4,1,119,2,3,69,501,5,40))
_ProvMseLineModeTable_Object=MibTable
provMseLineModeTable=_ProvMseLineModeTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,1))
if mibBuilder.loadTexts:provMseLineModeTable.setStatus(_A)
_ProvMseLineModeEntry_Object=MibTableRow
provMseLineModeEntry=_ProvMseLineModeEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,1,1))
provMseLineModeEntry.setIndexNames((0,_D,_K))
if mibBuilder.loadTexts:provMseLineModeEntry.setStatus(_A)
_ProvMseLineModeIfIndex_Type=InterfaceIndex
_ProvMseLineModeIfIndex_Object=MibTableColumn
provMseLineModeIfIndex=_ProvMseLineModeIfIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,1,1,1),_ProvMseLineModeIfIndex_Type())
provMseLineModeIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provMseLineModeIfIndex.setStatus(_A)
_ProvMseLineModeNEAddress_Type=IpAddress
_ProvMseLineModeNEAddress_Object=MibTableColumn
provMseLineModeNEAddress=_ProvMseLineModeNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,1,1,2),_ProvMseLineModeNEAddress_Type())
provMseLineModeNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provMseLineModeNEAddress.setStatus(_A)
class _ProvMseLineModeType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2)));namedValues=NamedValues(*((_G,0),('none',1),('satop',2)))
_ProvMseLineModeType_Type.__name__=_E
_ProvMseLineModeType_Object=MibTableColumn
provMseLineModeType=_ProvMseLineModeType_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,1,1,3),_ProvMseLineModeType_Type())
provMseLineModeType.setMaxAccess(_F)
if mibBuilder.loadTexts:provMseLineModeType.setStatus(_A)
_ProvMseClockModeTable_Object=MibTable
provMseClockModeTable=_ProvMseClockModeTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,2))
if mibBuilder.loadTexts:provMseClockModeTable.setStatus(_A)
_ProvMseClockModeEntry_Object=MibTableRow
provMseClockModeEntry=_ProvMseClockModeEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,2,1))
provMseClockModeEntry.setIndexNames((0,_D,_L))
if mibBuilder.loadTexts:provMseClockModeEntry.setStatus(_A)
_ProvMseClockModeIfIndex_Type=InterfaceIndex
_ProvMseClockModeIfIndex_Object=MibTableColumn
provMseClockModeIfIndex=_ProvMseClockModeIfIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,2,1,1),_ProvMseClockModeIfIndex_Type())
provMseClockModeIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provMseClockModeIfIndex.setStatus(_A)
_ProvMseClockModeNEAddress_Type=IpAddress
_ProvMseClockModeNEAddress_Object=MibTableColumn
provMseClockModeNEAddress=_ProvMseClockModeNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,2,1,2),_ProvMseClockModeNEAddress_Type())
provMseClockModeNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provMseClockModeNEAddress.setStatus(_A)
class _ProvMseClockModeType_Type(Integer32):defaultValue=2;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(0,1,2,3)));namedValues=NamedValues(*((_G,0),('syncToSystem',1),('syncToPw',2),('syncToLine',3)))
_ProvMseClockModeType_Type.__name__=_E
_ProvMseClockModeType_Object=MibTableColumn
provMseClockModeType=_ProvMseClockModeType_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,2,1,3),_ProvMseClockModeType_Type())
provMseClockModeType.setMaxAccess(_F)
if mibBuilder.loadTexts:provMseClockModeType.setStatus(_A)
class _ProvMseClockACRLineSelect_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ProvMseClockACRLineSelect_Type.__name__=_E
_ProvMseClockACRLineSelect_Object=MibTableColumn
provMseClockACRLineSelect=_ProvMseClockACRLineSelect_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,2,1,4),_ProvMseClockACRLineSelect_Type())
provMseClockACRLineSelect.setMaxAccess(_F)
if mibBuilder.loadTexts:provMseClockACRLineSelect.setStatus(_A)
_ProvMseClockModeExtTable_Object=MibTable
provMseClockModeExtTable=_ProvMseClockModeExtTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,3))
if mibBuilder.loadTexts:provMseClockModeExtTable.setStatus(_A)
_ProvMseClockModeExtEntry_Object=MibTableRow
provMseClockModeExtEntry=_ProvMseClockModeExtEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,3,1))
provMseClockModeExtEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:provMseClockModeExtEntry.setStatus(_A)
_ProvMseClockModeExtIfIndex_Type=InterfaceIndex
_ProvMseClockModeExtIfIndex_Object=MibTableColumn
provMseClockModeExtIfIndex=_ProvMseClockModeExtIfIndex_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,3,1,1),_ProvMseClockModeExtIfIndex_Type())
provMseClockModeExtIfIndex.setMaxAccess(_B)
if mibBuilder.loadTexts:provMseClockModeExtIfIndex.setStatus(_A)
_ProvMseClockModeExtNEAddress_Type=IpAddress
_ProvMseClockModeExtNEAddress_Object=MibTableColumn
provMseClockModeExtNEAddress=_ProvMseClockModeExtNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,3,1,2),_ProvMseClockModeExtNEAddress_Type())
provMseClockModeExtNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provMseClockModeExtNEAddress.setStatus(_A)
class _ProvMseClockModeReply2Master_Type(IpeEnableDisableValue):defaultValue=2
_ProvMseClockModeReply2Master_Type.__name__=_H
_ProvMseClockModeReply2Master_Object=MibTableColumn
provMseClockModeReply2Master=_ProvMseClockModeReply2Master_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,3,1,3),_ProvMseClockModeReply2Master_Type())
provMseClockModeReply2Master.setMaxAccess(_F)
if mibBuilder.loadTexts:provMseClockModeReply2Master.setStatus(_A)
class _ProvMseClockSupplyMode_Type(IpeEnableDisableValue):defaultValue=1
_ProvMseClockSupplyMode_Type.__name__=_H
_ProvMseClockSupplyMode_Object=MibTableColumn
provMseClockSupplyMode=_ProvMseClockSupplyMode_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,3,1,4),_ProvMseClockSupplyMode_Type())
provMseClockSupplyMode.setMaxAccess(_F)
if mibBuilder.loadTexts:provMseClockSupplyMode.setStatus(_A)
_ProvMseClockSelectTable_Object=MibTable
provMseClockSelectTable=_ProvMseClockSelectTable_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,4))
if mibBuilder.loadTexts:provMseClockSelectTable.setStatus(_A)
_ProvMseClockSelectEntry_Object=MibTableRow
provMseClockSelectEntry=_ProvMseClockSelectEntry_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,4,1))
provMseClockSelectEntry.setIndexNames((0,_D,_N))
if mibBuilder.loadTexts:provMseClockSelectEntry.setStatus(_A)
_ProvMseClockSelectCardId_Type=Integer32
_ProvMseClockSelectCardId_Object=MibTableColumn
provMseClockSelectCardId=_ProvMseClockSelectCardId_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,4,1,1),_ProvMseClockSelectCardId_Type())
provMseClockSelectCardId.setMaxAccess(_B)
if mibBuilder.loadTexts:provMseClockSelectCardId.setStatus(_A)
_ProvMseClockSelectNEAddress_Type=IpAddress
_ProvMseClockSelectNEAddress_Object=MibTableColumn
provMseClockSelectNEAddress=_ProvMseClockSelectNEAddress_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,4,1,2),_ProvMseClockSelectNEAddress_Type())
provMseClockSelectNEAddress.setMaxAccess(_B)
if mibBuilder.loadTexts:provMseClockSelectNEAddress.setStatus(_A)
class _ProvMseClockSelectLineNum_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,16))
_ProvMseClockSelectLineNum_Type.__name__=_E
_ProvMseClockSelectLineNum_Object=MibTableColumn
provMseClockSelectLineNum=_ProvMseClockSelectLineNum_Object((1,3,6,1,4,1,119,2,3,69,501,5,40,4,1,3),_ProvMseClockSelectLineNum_Type())
provMseClockSelectLineNum.setMaxAccess(_F)
if mibBuilder.loadTexts:provMseClockSelectLineNum.setStatus(_A)
mibBuilder.exportSymbols(_D,**{_H:IpeEnableDisableValue,'SeverityValue':SeverityValue,'nec':nec,'nec-mib':nec_mib,'necProductDepend':necProductDepend,'radioEquipment':radioEquipment,'pasoNeoIpe-common':pasoNeoIpe_common,'alarmStatusGroup':alarmStatusGroup,'asMseGroup':asMseGroup,'asMseCardTable':asMseCardTable,'asMseCardEntry':asMseCardEntry,_I:asMseCardIndex,'asMseCardNEAddress':asMseCardNEAddress,'asMseCardModuleFail':asMseCardModuleFail,'asMseCardComFailAlarm':asMseCardComFailAlarm,'asMseCardUnequipped':asMseCardUnequipped,'asMseCardTypeMismatch':asMseCardTypeMismatch,'asMseCardBusErrorTx':asMseCardBusErrorTx,'asMseCardBusErrorRx':asMseCardBusErrorRx,'asMseCardClkFail':asMseCardClkFail,'asMseLineTable':asMseLineTable,'asMseLineEntry':asMseLineEntry,_J:asMseLineIfIndex,'asMseLineNEAddress':asMseLineNEAddress,'asMseLineBfrUnderrun':asMseLineBfrUnderrun,'asMseLineAdaptiveClkStatus':asMseLineAdaptiveClkStatus,'provisioningGroup':provisioningGroup,'provMseGroup':provMseGroup,'provMseLineModeTable':provMseLineModeTable,'provMseLineModeEntry':provMseLineModeEntry,_K:provMseLineModeIfIndex,'provMseLineModeNEAddress':provMseLineModeNEAddress,'provMseLineModeType':provMseLineModeType,'provMseClockModeTable':provMseClockModeTable,'provMseClockModeEntry':provMseClockModeEntry,_L:provMseClockModeIfIndex,'provMseClockModeNEAddress':provMseClockModeNEAddress,'provMseClockModeType':provMseClockModeType,'provMseClockACRLineSelect':provMseClockACRLineSelect,'provMseClockModeExtTable':provMseClockModeExtTable,'provMseClockModeExtEntry':provMseClockModeExtEntry,_M:provMseClockModeExtIfIndex,'provMseClockModeExtNEAddress':provMseClockModeExtNEAddress,'provMseClockModeReply2Master':provMseClockModeReply2Master,'provMseClockSupplyMode':provMseClockSupplyMode,'provMseClockSelectTable':provMseClockSelectTable,'provMseClockSelectEntry':provMseClockSelectEntry,_N:provMseClockSelectCardId,'provMseClockSelectNEAddress':provMseClockSelectNEAddress,'provMseClockSelectLineNum':provMseClockSelectLineNum})