_N='fsVcConfigExtEntry'
_M='fsVcmFreeVcId'
_L='fsVcmVlanId'
_K='fsVcmL2VcId'
_J='fsVcmIfIndex'
_I='read-create'
_H='not-accessible'
_G='fsVCId'
_F='DisplayString'
_E='read-only'
_D='VCM-MIB'
_C='read-write'
_B='Integer32'
_A='current'
if'mibBuilder'not in globals():import sys;sys.stderr.write(__doc__);sys.exit(1)
Integer,OctetString,ObjectIdentifier=mibBuilder.importSymbols('ASN1','Integer','OctetString','ObjectIdentifier')
NamedValues,=mibBuilder.importSymbols('ASN1-ENUMERATION','NamedValues')
ConstraintsIntersection,ConstraintsUnion,SingleValueConstraint,ValueRangeConstraint,ValueSizeConstraint=mibBuilder.importSymbols('ASN1-REFINEMENT','ConstraintsIntersection','ConstraintsUnion','SingleValueConstraint','ValueRangeConstraint','ValueSizeConstraint')
InterfaceIndex,InterfaceIndexOrZero=mibBuilder.importSymbols('IF-MIB','InterfaceIndex','InterfaceIndexOrZero')
ModuleCompliance,NotificationGroup=mibBuilder.importSymbols('SNMPv2-CONF','ModuleCompliance','NotificationGroup')
Bits,Counter32,Counter64,Gauge32,Integer32,IpAddress,ModuleIdentity,MibIdentifier,NotificationType,ObjectIdentity,MibScalar,MibTable,MibTableRow,MibTableColumn,TimeTicks,Unsigned32,enterprises,iso=mibBuilder.importSymbols('SNMPv2-SMI','Bits','Counter32','Counter64','Gauge32',_B,'IpAddress','ModuleIdentity','MibIdentifier','NotificationType','ObjectIdentity','MibScalar','MibTable','MibTableRow','MibTableColumn','TimeTicks','Unsigned32','enterprises','iso')
DisplayString,MacAddress,PhysAddress,RowStatus,TextualConvention=mibBuilder.importSymbols('SNMPv2-TC',_F,'MacAddress','PhysAddress','RowStatus','TextualConvention')
fsVcmMib=ModuleIdentity((1,3,6,1,4,1,10876,101,1,93))
if mibBuilder.loadTexts:fsVcmMib.setRevisions(('2012-09-05 00:00',))
_FsVcmConfig_ObjectIdentity=ObjectIdentity
fsVcmConfig=_FsVcmConfig_ObjectIdentity((1,3,6,1,4,1,10876,101,1,93,1))
class _FsVcmTraceOption_Type(Integer32):defaultValue=0
_FsVcmTraceOption_Type.__name__=_B
_FsVcmTraceOption_Object=MibScalar
fsVcmTraceOption=_FsVcmTraceOption_Object((1,3,6,1,4,1,10876,101,1,93,1,1),_FsVcmTraceOption_Type())
fsVcmTraceOption.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcmTraceOption.setStatus(_A)
_FsVcmConfigTable_Object=MibTable
fsVcmConfigTable=_FsVcmConfigTable_Object((1,3,6,1,4,1,10876,101,1,93,1,2))
if mibBuilder.loadTexts:fsVcmConfigTable.setStatus(_A)
_FsVcmConfigEntry_Object=MibTableRow
fsVcmConfigEntry=_FsVcmConfigEntry_Object((1,3,6,1,4,1,10876,101,1,93,1,2,1))
fsVcmConfigEntry.setIndexNames((0,_D,_G))
if mibBuilder.loadTexts:fsVcmConfigEntry.setStatus(_A)
class _FsVCId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsVCId_Type.__name__=_B
_FsVCId_Object=MibTableColumn
fsVCId=_FsVCId_Object((1,3,6,1,4,1,10876,101,1,93,1,2,1,1),_FsVCId_Type())
fsVCId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVCId.setStatus(_A)
_FsVCNextFreeHlPortId_Type=InterfaceIndexOrZero
_FsVCNextFreeHlPortId_Object=MibTableColumn
fsVCNextFreeHlPortId=_FsVCNextFreeHlPortId_Object((1,3,6,1,4,1,10876,101,1,93,1,2,1,2),_FsVCNextFreeHlPortId_Type())
fsVCNextFreeHlPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVCNextFreeHlPortId.setStatus(_A)
_FsVCMacAddress_Type=MacAddress
_FsVCMacAddress_Object=MibTableColumn
fsVCMacAddress=_FsVCMacAddress_Object((1,3,6,1,4,1,10876,101,1,93,1,2,1,3),_FsVCMacAddress_Type())
fsVCMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVCMacAddress.setStatus(_A)
class _FsVcAlias_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsVcAlias_Type.__name__=_F
_FsVcAlias_Object=MibTableColumn
fsVcAlias=_FsVcAlias_Object((1,3,6,1,4,1,10876,101,1,93,1,2,1,4),_FsVcAlias_Type())
fsVcAlias.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcAlias.setStatus(_A)
class _FsVcCxtType_Type(Integer32):defaultValue=1;subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(SingleValueConstraint(*(1,2,3)));namedValues=NamedValues(*(('l2Context',1),('l3Context',2),('both',3)))
_FsVcCxtType_Type.__name__=_B
_FsVcCxtType_Object=MibTableColumn
fsVcCxtType=_FsVcCxtType_Object((1,3,6,1,4,1,10876,101,1,93,1,2,1,5),_FsVcCxtType_Type())
fsVcCxtType.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcCxtType.setStatus(_A)
_FsVCStatus_Type=RowStatus
_FsVCStatus_Object=MibTableColumn
fsVCStatus=_FsVCStatus_Object((1,3,6,1,4,1,10876,101,1,93,1,2,1,6),_FsVCStatus_Type())
fsVCStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsVCStatus.setStatus(_A)
_FsVRMacAddress_Type=MacAddress
_FsVRMacAddress_Object=MibTableColumn
fsVRMacAddress=_FsVRMacAddress_Object((1,3,6,1,4,1,10876,101,1,93,1,2,1,7),_FsVRMacAddress_Type())
fsVRMacAddress.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVRMacAddress.setStatus(_A)
_FsVcmIfMappingTable_Object=MibTable
fsVcmIfMappingTable=_FsVcmIfMappingTable_Object((1,3,6,1,4,1,10876,101,1,93,1,3))
if mibBuilder.loadTexts:fsVcmIfMappingTable.setStatus(_A)
_FsVcmIfMappingEntry_Object=MibTableRow
fsVcmIfMappingEntry=_FsVcmIfMappingEntry_Object((1,3,6,1,4,1,10876,101,1,93,1,3,1))
fsVcmIfMappingEntry.setIndexNames((0,_D,_J))
if mibBuilder.loadTexts:fsVcmIfMappingEntry.setStatus(_A)
_FsVcmIfIndex_Type=InterfaceIndex
_FsVcmIfIndex_Object=MibTableColumn
fsVcmIfIndex=_FsVcmIfIndex_Object((1,3,6,1,4,1,10876,101,1,93,1,3,1,1),_FsVcmIfIndex_Type())
fsVcmIfIndex.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVcmIfIndex.setStatus(_A)
class _FsVcId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(-1,-1),ValueRangeConstraint(0,65535))
_FsVcId_Type.__name__=_B
_FsVcId_Object=MibTableColumn
fsVcId=_FsVcId_Object((1,3,6,1,4,1,10876,101,1,93,1,3,1,2),_FsVcId_Type())
fsVcId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcId.setStatus(_A)
_FsVcHlPortId_Type=InterfaceIndexOrZero
_FsVcHlPortId_Object=MibTableColumn
fsVcHlPortId=_FsVcHlPortId_Object((1,3,6,1,4,1,10876,101,1,93,1,3,1,3),_FsVcHlPortId_Type())
fsVcHlPortId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVcHlPortId.setStatus(_A)
class _FsVcL2ContextId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsVcL2ContextId_Type.__name__=_B
_FsVcL2ContextId_Object=MibTableColumn
fsVcL2ContextId=_FsVcL2ContextId_Object((1,3,6,1,4,1,10876,101,1,93,1,3,1,4),_FsVcL2ContextId_Type())
fsVcL2ContextId.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcL2ContextId.setStatus(_A)
_FsVcIfRowStatus_Type=RowStatus
_FsVcIfRowStatus_Object=MibTableColumn
fsVcIfRowStatus=_FsVcIfRowStatus_Object((1,3,6,1,4,1,10876,101,1,93,1,3,1,5),_FsVcIfRowStatus_Type())
fsVcIfRowStatus.setMaxAccess(_I)
if mibBuilder.loadTexts:fsVcIfRowStatus.setStatus(_A)
_FsVcmL2CxtAndVlanToIPIfaceMapTable_Object=MibTable
fsVcmL2CxtAndVlanToIPIfaceMapTable=_FsVcmL2CxtAndVlanToIPIfaceMapTable_Object((1,3,6,1,4,1,10876,101,1,93,1,4))
if mibBuilder.loadTexts:fsVcmL2CxtAndVlanToIPIfaceMapTable.setStatus(_A)
_FsVcmL2CxtAndVlanToIPIfaceMapEntry_Object=MibTableRow
fsVcmL2CxtAndVlanToIPIfaceMapEntry=_FsVcmL2CxtAndVlanToIPIfaceMapEntry_Object((1,3,6,1,4,1,10876,101,1,93,1,4,1))
fsVcmL2CxtAndVlanToIPIfaceMapEntry.setIndexNames((0,_D,_K),(0,_D,_L))
if mibBuilder.loadTexts:fsVcmL2CxtAndVlanToIPIfaceMapEntry.setStatus(_A)
class _FsVcmL2VcId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,255))
_FsVcmL2VcId_Type.__name__=_B
_FsVcmL2VcId_Object=MibTableColumn
fsVcmL2VcId=_FsVcmL2VcId_Object((1,3,6,1,4,1,10876,101,1,93,1,4,1,1),_FsVcmL2VcId_Type())
fsVcmL2VcId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVcmL2VcId.setStatus(_A)
class _FsVcmVlanId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(1,4094))
_FsVcmVlanId_Type.__name__=_B
_FsVcmVlanId_Object=MibTableColumn
fsVcmVlanId=_FsVcmVlanId_Object((1,3,6,1,4,1,10876,101,1,93,1,4,1,2),_FsVcmVlanId_Type())
fsVcmVlanId.setMaxAccess(_H)
if mibBuilder.loadTexts:fsVcmVlanId.setStatus(_A)
class _FsVcmL2VcName_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,32))
_FsVcmL2VcName_Type.__name__=_F
_FsVcmL2VcName_Object=MibTableColumn
fsVcmL2VcName=_FsVcmL2VcName_Object((1,3,6,1,4,1,10876,101,1,93,1,4,1,3),_FsVcmL2VcName_Type())
fsVcmL2VcName.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVcmL2VcName.setStatus(_A)
_FsVcmIPIfIndex_Type=InterfaceIndex
_FsVcmIPIfIndex_Object=MibTableColumn
fsVcmIPIfIndex=_FsVcmIPIfIndex_Object((1,3,6,1,4,1,10876,101,1,93,1,4,1,4),_FsVcmIPIfIndex_Type())
fsVcmIPIfIndex.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVcmIPIfIndex.setStatus(_A)
_FsVcConfigExtTable_Object=MibTable
fsVcConfigExtTable=_FsVcConfigExtTable_Object((1,3,6,1,4,1,10876,101,1,93,1,5))
if mibBuilder.loadTexts:fsVcConfigExtTable.setStatus(_A)
_FsVcConfigExtEntry_Object=MibTableRow
fsVcConfigExtEntry=_FsVcConfigExtEntry_Object((1,3,6,1,4,1,10876,101,1,93,1,5,1))
if mibBuilder.loadTexts:fsVcConfigExtEntry.setStatus(_A)
class _FsVcOwner_Type(DisplayString):subtypeSpec=DisplayString.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueSizeConstraint(0,16))
_FsVcOwner_Type.__name__=_F
_FsVcOwner_Object=MibTableColumn
fsVcOwner=_FsVcOwner_Object((1,3,6,1,4,1,10876,101,1,93,1,5,1,1),_FsVcOwner_Type())
fsVcOwner.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcOwner.setStatus(_A)
_FsVcmFreeVcIdTable_Object=MibTable
fsVcmFreeVcIdTable=_FsVcmFreeVcIdTable_Object((1,3,6,1,4,1,10876,101,1,93,1,6))
if mibBuilder.loadTexts:fsVcmFreeVcIdTable.setStatus(_A)
_FsVcmFreeVcIdEntry_Object=MibTableRow
fsVcmFreeVcIdEntry=_FsVcmFreeVcIdEntry_Object((1,3,6,1,4,1,10876,101,1,93,1,6,1))
fsVcmFreeVcIdEntry.setIndexNames((0,_D,_M))
if mibBuilder.loadTexts:fsVcmFreeVcIdEntry.setStatus(_A)
class _FsVcmFreeVcId_Type(Integer32):subtypeSpec=Integer32.subtypeSpec;subtypeSpec+=ConstraintsUnion(ValueRangeConstraint(0,65535))
_FsVcmFreeVcId_Type.__name__=_B
_FsVcmFreeVcId_Object=MibTableColumn
fsVcmFreeVcId=_FsVcmFreeVcId_Object((1,3,6,1,4,1,10876,101,1,93,1,6,1,1),_FsVcmFreeVcId_Type())
fsVcmFreeVcId.setMaxAccess(_E)
if mibBuilder.loadTexts:fsVcmFreeVcId.setStatus(_A)
_FsVcmTraps_ObjectIdentity=ObjectIdentity
fsVcmTraps=_FsVcmTraps_ObjectIdentity((1,3,6,1,4,1,10876,101,1,93,2))
_FsVcmAppContextConfig_ObjectIdentity=ObjectIdentity
fsVcmAppContextConfig=_FsVcmAppContextConfig_ObjectIdentity((1,3,6,1,4,1,10876,101,1,93,3))
class _FsVcmFirmwareUpgradeCxt_Type(Integer32):defaultValue=1
_FsVcmFirmwareUpgradeCxt_Type.__name__=_B
_FsVcmFirmwareUpgradeCxt_Object=MibScalar
fsVcmFirmwareUpgradeCxt=_FsVcmFirmwareUpgradeCxt_Object((1,3,6,1,4,1,10876,101,1,93,3,1),_FsVcmFirmwareUpgradeCxt_Type())
fsVcmFirmwareUpgradeCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcmFirmwareUpgradeCxt.setStatus(_A)
class _FsVcmFileCopyCxt_Type(Integer32):defaultValue=1
_FsVcmFileCopyCxt_Type.__name__=_B
_FsVcmFileCopyCxt_Object=MibScalar
fsVcmFileCopyCxt=_FsVcmFileCopyCxt_Object((1,3,6,1,4,1,10876,101,1,93,3,2),_FsVcmFileCopyCxt_Type())
fsVcmFileCopyCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcmFileCopyCxt.setStatus(_A)
class _FsVcmCoredumpPutCxt_Type(Integer32):defaultValue=1
_FsVcmCoredumpPutCxt_Type.__name__=_B
_FsVcmCoredumpPutCxt_Object=MibScalar
fsVcmCoredumpPutCxt=_FsVcmCoredumpPutCxt_Object((1,3,6,1,4,1,10876,101,1,93,3,3),_FsVcmCoredumpPutCxt_Type())
fsVcmCoredumpPutCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcmCoredumpPutCxt.setStatus(_A)
class _FsVcmSyslogClientCxt_Type(Integer32):defaultValue=1
_FsVcmSyslogClientCxt_Type.__name__=_B
_FsVcmSyslogClientCxt_Object=MibScalar
fsVcmSyslogClientCxt=_FsVcmSyslogClientCxt_Object((1,3,6,1,4,1,10876,101,1,93,3,4),_FsVcmSyslogClientCxt_Type())
fsVcmSyslogClientCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcmSyslogClientCxt.setStatus(_A)
class _FsVcmSnmpTrapClientCxt_Type(Integer32):defaultValue=1
_FsVcmSnmpTrapClientCxt_Type.__name__=_B
_FsVcmSnmpTrapClientCxt_Object=MibScalar
fsVcmSnmpTrapClientCxt=_FsVcmSnmpTrapClientCxt_Object((1,3,6,1,4,1,10876,101,1,93,3,5),_FsVcmSnmpTrapClientCxt_Type())
fsVcmSnmpTrapClientCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcmSnmpTrapClientCxt.setStatus(_A)
class _FsVcmSntpClientCxt_Type(Integer32):defaultValue=1
_FsVcmSntpClientCxt_Type.__name__=_B
_FsVcmSntpClientCxt_Object=MibScalar
fsVcmSntpClientCxt=_FsVcmSntpClientCxt_Object((1,3,6,1,4,1,10876,101,1,93,3,6),_FsVcmSntpClientCxt_Type())
fsVcmSntpClientCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcmSntpClientCxt.setStatus(_A)
class _FsVcmSnmpAgentxCxt_Type(Integer32):defaultValue=1
_FsVcmSnmpAgentxCxt_Type.__name__=_B
_FsVcmSnmpAgentxCxt_Object=MibScalar
fsVcmSnmpAgentxCxt=_FsVcmSnmpAgentxCxt_Object((1,3,6,1,4,1,10876,101,1,93,3,7),_FsVcmSnmpAgentxCxt_Type())
fsVcmSnmpAgentxCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcmSnmpAgentxCxt.setStatus(_A)
class _FsVcmTacacsClientCxt_Type(Integer32):defaultValue=1
_FsVcmTacacsClientCxt_Type.__name__=_B
_FsVcmTacacsClientCxt_Object=MibScalar
fsVcmTacacsClientCxt=_FsVcmTacacsClientCxt_Object((1,3,6,1,4,1,10876,101,1,93,3,8),_FsVcmTacacsClientCxt_Type())
fsVcmTacacsClientCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcmTacacsClientCxt.setStatus(_A)
class _FsVcmRadiusClientCxt_Type(Integer32):defaultValue=1
_FsVcmRadiusClientCxt_Type.__name__=_B
_FsVcmRadiusClientCxt_Object=MibScalar
fsVcmRadiusClientCxt=_FsVcmRadiusClientCxt_Object((1,3,6,1,4,1,10876,101,1,93,3,9),_FsVcmRadiusClientCxt_Type())
fsVcmRadiusClientCxt.setMaxAccess(_C)
if mibBuilder.loadTexts:fsVcmRadiusClientCxt.setStatus(_A)
fsVcmConfigEntry.registerAugmentions((_D,_N))
fsVcConfigExtEntry.setIndexNames(*fsVcmConfigEntry.getIndexNames())
fsVcmContextCreatedTrap=NotificationType((1,3,6,1,4,1,10876,101,1,93,2,1))
fsVcmContextCreatedTrap.setObjects((_D,_G))
if mibBuilder.loadTexts:fsVcmContextCreatedTrap.setStatus(_A)
fsVcmContextDeletedTrap=NotificationType((1,3,6,1,4,1,10876,101,1,93,2,2))
fsVcmContextDeletedTrap.setObjects((_D,_G))
if mibBuilder.loadTexts:fsVcmContextDeletedTrap.setStatus(_A)
mibBuilder.exportSymbols(_D,**{'fsVcmMib':fsVcmMib,'fsVcmConfig':fsVcmConfig,'fsVcmTraceOption':fsVcmTraceOption,'fsVcmConfigTable':fsVcmConfigTable,'fsVcmConfigEntry':fsVcmConfigEntry,_G:fsVCId,'fsVCNextFreeHlPortId':fsVCNextFreeHlPortId,'fsVCMacAddress':fsVCMacAddress,'fsVcAlias':fsVcAlias,'fsVcCxtType':fsVcCxtType,'fsVCStatus':fsVCStatus,'fsVRMacAddress':fsVRMacAddress,'fsVcmIfMappingTable':fsVcmIfMappingTable,'fsVcmIfMappingEntry':fsVcmIfMappingEntry,_J:fsVcmIfIndex,'fsVcId':fsVcId,'fsVcHlPortId':fsVcHlPortId,'fsVcL2ContextId':fsVcL2ContextId,'fsVcIfRowStatus':fsVcIfRowStatus,'fsVcmL2CxtAndVlanToIPIfaceMapTable':fsVcmL2CxtAndVlanToIPIfaceMapTable,'fsVcmL2CxtAndVlanToIPIfaceMapEntry':fsVcmL2CxtAndVlanToIPIfaceMapEntry,_K:fsVcmL2VcId,_L:fsVcmVlanId,'fsVcmL2VcName':fsVcmL2VcName,'fsVcmIPIfIndex':fsVcmIPIfIndex,'fsVcConfigExtTable':fsVcConfigExtTable,_N:fsVcConfigExtEntry,'fsVcOwner':fsVcOwner,'fsVcmFreeVcIdTable':fsVcmFreeVcIdTable,'fsVcmFreeVcIdEntry':fsVcmFreeVcIdEntry,_M:fsVcmFreeVcId,'fsVcmTraps':fsVcmTraps,'fsVcmContextCreatedTrap':fsVcmContextCreatedTrap,'fsVcmContextDeletedTrap':fsVcmContextDeletedTrap,'fsVcmAppContextConfig':fsVcmAppContextConfig,'fsVcmFirmwareUpgradeCxt':fsVcmFirmwareUpgradeCxt,'fsVcmFileCopyCxt':fsVcmFileCopyCxt,'fsVcmCoredumpPutCxt':fsVcmCoredumpPutCxt,'fsVcmSyslogClientCxt':fsVcmSyslogClientCxt,'fsVcmSnmpTrapClientCxt':fsVcmSnmpTrapClientCxt,'fsVcmSntpClientCxt':fsVcmSntpClientCxt,'fsVcmSnmpAgentxCxt':fsVcmSnmpAgentxCxt,'fsVcmTacacsClientCxt':fsVcmTacacsClientCxt,'fsVcmRadiusClientCxt':fsVcmRadiusClientCxt})